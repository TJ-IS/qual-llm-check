from __future__ import annotations

import json
import re
from pathlib import Path


RUN_DIR = Path(__file__).resolve().parent
ROOT = RUN_DIR.parents[1]
FULLTEXT_DIR = ROOT / "database_fulltext_all"
AUDIT_DIR = RUN_DIR / "audit_v1"
MANIFEST = AUDIT_DIR / "sample_manifest.json"
OUTPUT = AUDIT_DIR / "evidence_packets.md"

HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*$", re.MULTILINE)
TARGET_RE = re.compile(
    r"abstract|introduction|evaluation|experiment|result|discussion|conclusion|implication|"
    r"validation|performance|findings|analysis|study\s+\d|method",
    re.IGNORECASE,
)


def clean(text: str) -> str:
    text = re.sub(r"!\[[^\]]*\]\([^\)]*\)", "[image omitted]", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def sections(text: str) -> list[tuple[int, str, str]]:
    matches = list(HEADING_RE.finditer(text))
    out: list[tuple[int, str, str]] = []
    for index, match in enumerate(matches):
        level = len(match.group(1))
        title = match.group(2).strip()
        end = len(text)
        for nxt in matches[index + 1 :]:
            if len(nxt.group(1)) <= level:
                end = nxt.start()
                break
        out.append((level, title, clean(text[match.end() : end])))
    return out


def select_evidence(text: str, max_chars: int = 15000) -> str:
    chosen: list[str] = []
    used = 0
    for level, title, body in sections(text):
        if not TARGET_RE.search(title):
            continue
        # Preserve enough of abstracts/conclusions; cap long methods/results sections.
        cap = 5000 if re.search(r"abstract|conclusion|discussion", title, re.I) else 2500
        excerpt = body[:cap]
        block = f"{'#' * min(level + 2, 6)} {title}\n\n{excerpt}\n"
        if used + len(block) > max_chars:
            remaining = max_chars - used
            if remaining > 500:
                chosen.append(block[:remaining])
            break
        chosen.append(block)
        used += len(block)
    if not chosen:
        return clean(text[:max_chars])
    return "\n".join(chosen)


def main() -> None:
    data = json.loads(MANIFEST.read_text(encoding="utf-8"))
    lines = [
        "# Manual-audit evidence packets",
        "",
        "Generated from the fixed stratified sample. Extracts are navigation aids; manual judgments must be checked against the source full text.",
        "",
    ]
    for index, record in enumerate(data["records"], 1):
        source = FULLTEXT_DIR / record["source_file"]
        text = source.read_text(encoding="utf-8", errors="replace")
        lines.extend(
            [
                f"# Audit {index:02d}: {record['title']}",
                "",
                f"- Group: `{record['audit_group']}`",
                f"- Model decision: `{record['strict_match']}`; centrality `{record['centrality']}`; layer `{record['solution_layer']}`",
                f"- Gates: `{json.dumps(record['gates'], ensure_ascii=False)}`",
                f"- Model reason: {record['decision_reason_cn']}",
                f"- Source: `{source}`",
                "",
                select_evidence(text),
                "",
            ]
        )
    OUTPUT.write_text("\n".join(lines), encoding="utf-8")
    print(json.dumps({"records": len(data["records"]), "output": str(OUTPUT)}, ensure_ascii=False))


if __name__ == "__main__":
    main()
