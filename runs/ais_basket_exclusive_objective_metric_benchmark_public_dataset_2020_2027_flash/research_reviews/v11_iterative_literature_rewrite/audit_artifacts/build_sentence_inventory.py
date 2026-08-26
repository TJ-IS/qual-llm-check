from __future__ import annotations

import argparse
import datetime
import hashlib
import json
import re
from pathlib import Path


REFERENCE_HEADING_RE = re.compile(
    r"^##\s+(?:参考文献|References|Bibliography)\s*$", re.IGNORECASE
)
HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*$")
TABLE_SEPARATOR_RE = re.compile(
    r"^\|?\s*:?-{3,}:?\s*(?:\|\s*:?-{3,}:?\s*)+\|?$"
)
LIST_RE = re.compile(r"^\s*(?:[-*+]\s+|\d+[.)]\s+)(.*)$")
CHINESE_SENTENCE_END_RE = re.compile(r".+?[。！？!?](?=\s*|$)")
NATURAL_LANGUAGE_RE = re.compile(r"[\u3400-\u9fffA-Za-z]")


def sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def sha256_text(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def visible_text(value: str) -> str:
    value = value.strip()
    value = re.sub(r"^>\s?", "", value)
    value = value.replace("**", "").replace("__", "")
    value = re.sub(r"\s+", " ", value)
    return value.strip()


def sentence_parts(value: str) -> list[str]:
    value = visible_text(value)
    if not value:
        return []
    matches = list(CHINESE_SENTENCE_END_RE.finditer(value))
    if not matches:
        return [value]
    parts: list[str] = []
    cursor = 0
    for match in matches:
        prefix = value[cursor : match.end()].strip()
        if prefix:
            parts.append(prefix)
        cursor = match.end()
    tail = value[cursor:].strip()
    if tail:
        parts.append(tail)
    return parts


def table_cells(line: str) -> list[str]:
    stripped = line.strip().strip("|")
    if not stripped:
        return []
    return [visible_text(cell) for cell in re.split(r"(?<!\\)\|", stripped)]


def inventory(manuscript: Path, paper_id: str) -> dict[str, object]:
    raw = manuscript.read_bytes()
    lines = raw.decode("utf-8-sig").splitlines()
    body_end = len(lines)
    for index, line in enumerate(lines):
        if REFERENCE_HEADING_RE.match(line.strip()):
            body_end = index
            break

    current_section = "title"
    paragraph_number = 0
    units: list[dict[str, object]] = []
    prose_buffer: list[tuple[int, str]] = []
    math_buffer: list[tuple[int, str]] = []
    in_math = False

    def append_unit(
        unit_type: str,
        start_line: int,
        end_line: int,
        text: str,
        paragraph_id: str,
    ) -> None:
        normalized = visible_text(text)
        if not normalized:
            return
        unit_id = f"{paper_id}-U{len(units) + 1:04d}"
        units.append(
            {
                "target_id": unit_id,
                "type": unit_type,
                "section": current_section,
                "paragraph_id": paragraph_id,
                "target_lines": str(start_line)
                if start_line == end_line
                else f"{start_line}-{end_line}",
                "target_sentence": normalized,
                "target_sha256": sha256_text(normalized),
            }
        )

    def flush_prose() -> None:
        nonlocal paragraph_number
        if not prose_buffer:
            return
        paragraph_number += 1
        start_line = prose_buffer[0][0]
        end_line = prose_buffer[-1][0]
        combined = " ".join(text.strip() for _, text in prose_buffer)
        paragraph_id = f"{paper_id}-P{paragraph_number:04d}"
        for sentence in sentence_parts(combined):
            append_unit("prose", start_line, end_line, sentence, paragraph_id)
        prose_buffer.clear()

    def flush_math() -> None:
        nonlocal paragraph_number
        if not math_buffer:
            return
        paragraph_number += 1
        start_line = math_buffer[0][0]
        end_line = math_buffer[-1][0]
        combined = " ".join(text.strip() for _, text in math_buffer)
        append_unit(
            "formula_block",
            start_line,
            end_line,
            combined,
            f"{paper_id}-P{paragraph_number:04d}",
        )
        math_buffer.clear()

    for zero_index, raw_line in enumerate(lines[:body_end]):
        line_number = zero_index + 1
        stripped = raw_line.strip()

        if in_math:
            math_buffer.append((line_number, raw_line))
            if stripped in {"$$", "\\]"}:
                in_math = False
                flush_math()
            continue

        heading = HEADING_RE.match(stripped)
        if heading:
            flush_prose()
            current_section = visible_text(heading.group(2))
            continue

        if stripped in {"$$", "\\["}:
            flush_prose()
            in_math = True
            math_buffer.append((line_number, raw_line))
            continue

        if not stripped:
            flush_prose()
            continue

        if TABLE_SEPARATOR_RE.match(stripped):
            flush_prose()
            continue

        if stripped.startswith("|") and stripped.endswith("|"):
            flush_prose()
            paragraph_number += 1
            paragraph_id = f"{paper_id}-P{paragraph_number:04d}"
            for cell_index, cell in enumerate(table_cells(stripped), start=1):
                if not cell or not NATURAL_LANGUAGE_RE.search(cell):
                    continue
                for part in sentence_parts(cell):
                    append_unit(
                        f"table_cell_{cell_index}",
                        line_number,
                        line_number,
                        part,
                        paragraph_id,
                    )
            continue

        list_match = LIST_RE.match(raw_line)
        if list_match:
            flush_prose()
            paragraph_number += 1
            paragraph_id = f"{paper_id}-P{paragraph_number:04d}"
            for part in sentence_parts(list_match.group(1)):
                append_unit("list_item", line_number, line_number, part, paragraph_id)
            continue

        if stripped.startswith("```"):
            flush_prose()
            continue

        prose_buffer.append((line_number, raw_line))

    flush_prose()
    flush_math()
    return {
        "manuscript": str(manuscript),
        "manuscript_sha256": sha256_bytes(raw),
        "paper_id": paper_id,
        "generated_at_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "reference_heading_line": body_end + 1 if body_end < len(lines) else None,
        "unit_count": len(units),
        "counts_by_type": {
            key: sum(unit["type"] == key for unit in units)
            for key in sorted({str(unit["type"]) for unit in units})
        },
        "units": units,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("manuscript", type=Path)
    parser.add_argument("--paper-id", required=True, choices=("P1", "P2", "P3"))
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    result = inventory(args.manuscript, args.paper_id)
    rendered = json.dumps(result, ensure_ascii=False, indent=2) + "\n"
    if args.output:
        args.output.write_text(rendered, encoding="utf-8")
    else:
        print(rendered, end="")


if __name__ == "__main__":
    main()
