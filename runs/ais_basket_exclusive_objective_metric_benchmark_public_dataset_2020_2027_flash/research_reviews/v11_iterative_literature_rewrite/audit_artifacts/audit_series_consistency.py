from __future__ import annotations

import argparse
import datetime
import difflib
import hashlib
import itertools
import json
import re
from pathlib import Path


REFERENCE_HEADING_RE = re.compile(
    r"^##\s+(?:参考文献|References|Bibliography)\s*$",
    re.MULTILINE | re.IGNORECASE,
)
CITATION_GROUP_RE = re.compile(
    r"[（(][^()（）]*(?:(?:19|20)\d{2}|et al\.)[^()（）]*[)）]"
)
EMPIRICAL_RE = re.compile(
    r"结果表明|我们发现|显著优于|显著提高|证明了|实验结果显示|结果证明"
)
FORBIDDEN_MARKS = ("：", "；", ";", ":", "—", "–", "“", "”", "‘", "’", "…", "→")
INLINE_PLACEHOLDER_RE = re.compile(r"\[\[待补文献[：:][^\n]*?\]\]")


def split_body_and_references(text: str) -> tuple[str, str]:
    match = REFERENCE_HEADING_RE.search(text)
    if not match:
        return text, ""
    return text[: match.start()], text[match.end() :]


def prose_blocks(text: str) -> list[tuple[int, str]]:
    blocks: list[tuple[int, str]] = []
    in_fence = False
    current: list[tuple[int, str]] = []

    def flush() -> None:
        nonlocal current
        if not current:
            return
        first_line = current[0][1].lstrip()
        excluded = (
            first_line.startswith("#")
            or first_line.startswith("|")
            or first_line.startswith("$$")
            or first_line.startswith("\\[")
            or first_line.startswith("\\begin{")
            or first_line.startswith("![")
            or first_line.startswith("**表")
            or first_line.startswith("**Table")
            or first_line.startswith("**算法")
            or first_line.startswith("**Algorithm")
        )
        if not excluded:
            blocks.append(
                (current[0][0], " ".join(line.strip() for _, line in current).strip())
            )
        current = []

    for number, line in enumerate(text.splitlines(), start=1):
        if line.lstrip().startswith("```"):
            flush()
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        if not line.strip():
            flush()
            continue
        current.append((number, line))
    flush()
    return blocks


def sentences(text: str) -> list[dict[str, object]]:
    result: list[dict[str, object]] = []
    for start_line, block in prose_blocks(text):
        for sentence in re.split(r"(?<=[。！？!?])", block):
            sentence = sentence.strip()
            if sentence:
                result.append({"line": start_line, "text": sentence})
    return result


def normalize(sentence: str) -> str:
    sentence = CITATION_GROUP_RE.sub("", sentence)
    sentence = re.sub(r"\$[^$]*\$", "<FORMULA>", sentence)
    sentence = re.sub(r"`[^`]*`", "<FIELD>", sentence)
    sentence = re.sub(r"\s+", "", sentence)
    sentence = re.sub(r"[，。！？、,.!?（）()\[\]{}*#]", "", sentence)
    return sentence.lower()


def reference_count(reference_text: str) -> int:
    return sum(
        1
        for line in reference_text.splitlines()
        if re.match(r"^[A-ZÀ-ÖØ-Þ][^\n]*\b(?:19|20)\d{2}[a-z]?\.", line.strip())
    )


def inspect(path: Path) -> dict[str, object]:
    raw = path.read_bytes()
    text = raw.decode("utf-8-sig")
    body, references = split_body_and_references(text)
    body_sentences = sentences(body)
    punctuation = {
        mark: sum(block.count(mark) for _, block in prose_blocks(body))
        for mark in FORBIDDEN_MARKS
    }
    body_without_placeholders = INLINE_PLACEHOLDER_RE.sub("", body)
    non_placeholder_punctuation = {
        mark: sum(
            block.count(mark)
            for _, block in prose_blocks(body_without_placeholders)
        )
        for mark in FORBIDDEN_MARKS
    }
    empirical = [
        item for item in body_sentences if EMPIRICAL_RE.search(str(item["text"]))
    ]
    full_body_empirical = [
        {"line": number, "text": line.strip()}
        for number, line in enumerate(body.splitlines(), start=1)
        if EMPIRICAL_RE.search(line)
    ]
    return {
        "path": str(path),
        "sha256": hashlib.sha256(raw).hexdigest(),
        "body_sentences": body_sentences,
        "forbidden_punctuation": punctuation,
        "full_body_forbidden_punctuation": {
            mark: body.count(mark) for mark in FORBIDDEN_MARKS
        },
        "inline_placeholder_occurrences": len(INLINE_PLACEHOLDER_RE.findall(body)),
        "non_placeholder_forbidden_punctuation": non_placeholder_punctuation,
        "full_body_non_placeholder_forbidden_punctuation": {
            mark: body_without_placeholders.count(mark) for mark in FORBIDDEN_MARKS
        },
        "empirical_phrase_hits": empirical,
        "full_body_empirical_phrase_hits": full_body_empirical,
        "reference_entries": reference_count(references),
        "reference_urls": len(re.findall(r"https?://\S+", references)),
    }


def duplicate_pairs(records: list[dict[str, object]]) -> tuple[list[dict[str, object]], list[dict[str, object]]]:
    exact: list[dict[str, object]] = []
    near: list[dict[str, object]] = []
    for left, right in itertools.combinations(records, 2):
        left_sentences = left["body_sentences"]
        right_sentences = right["body_sentences"]
        for a in left_sentences:
            normalized_a = normalize(str(a["text"]))
            if len(normalized_a) < 35:
                continue
            for b in right_sentences:
                normalized_b = normalize(str(b["text"]))
                if len(normalized_b) < 35:
                    continue
                if normalized_a == normalized_b:
                    exact.append(
                        {
                            "left": left["path"],
                            "left_line": a["line"],
                            "right": right["path"],
                            "right_line": b["line"],
                            "text": a["text"],
                        }
                    )
                    continue
                length_ratio = min(len(normalized_a), len(normalized_b)) / max(
                    len(normalized_a), len(normalized_b)
                )
                if length_ratio < 0.85:
                    continue
                score = difflib.SequenceMatcher(None, normalized_a, normalized_b).ratio()
                if score >= 0.92:
                    near.append(
                        {
                            "score": round(score, 4),
                            "left": left["path"],
                            "left_line": a["line"],
                            "left_text": a["text"],
                            "right": right["path"],
                            "right_line": b["line"],
                            "right_text": b["text"],
                        }
                    )
    return exact, sorted(near, key=lambda item: item["score"], reverse=True)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("manuscripts", nargs="+", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    records = [inspect(path) for path in args.manuscripts]
    exact, near = duplicate_pairs(records)
    output_records = []
    for record in records:
        output_records.append(
            {key: value for key, value in record.items() if key != "body_sentences"}
        )
    result = {
        "generated_at_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "audit_script": str(Path(__file__).resolve()),
        "audit_script_sha256": hashlib.sha256(
            Path(__file__).read_bytes()
        ).hexdigest(),
        "manuscripts": output_records,
        "exact_cross_manuscript_duplicates": exact,
        "near_cross_manuscript_duplicates": near,
        "normalization_note": "Citations, inline formulas, inline code and spacing are normalized before cross-manuscript comparison. Near matches require at least 35 normalized characters, length ratio at least 0.85 and similarity at least 0.92.",
        "scope_note": "Sentence duplication uses prose blocks. Full-body punctuation and empirical-phrase fields include all content before the reference heading, including headings, tables, formulas, algorithms and captions.",
    }
    rendered = json.dumps(result, ensure_ascii=False, indent=2)
    if args.output:
        args.output.write_text(rendered + "\n", encoding="utf-8")
    else:
        print(rendered)


if __name__ == "__main__":
    main()
