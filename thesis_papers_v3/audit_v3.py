from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


BANNED_PHRASES = (
    "唯一研究问题",
    "唯一命题",
    "公开资源",
    "实际运行",
    "可以运行",
    "可运行",
    "当前稿件",
    "不报告结果",
    "没有虚构",
    "研究设计稿",
    "内部证伪",
    "系列安排",
)

SPECIAL_PUNCTUATION = ("“", "”", '"', "：", ":", "；", ";")


def prose_for_style_scan(body: str) -> str:
    """Remove math and inline code before scanning ordinary prose punctuation."""
    without_display_math = re.sub(r"\\\[.*?\\\]", "", body, flags=re.DOTALL)
    without_inline_math = re.sub(r"\\\(.*?\\\)", "", without_display_math, flags=re.DOTALL)
    return re.sub(r"`[^`]*`", "", without_inline_math)


def substantive_paragraphs(body: str) -> list[str]:
    """Approximate rhetorical blocks by attaching display-math explanations.

    This is only a heuristic.  A section heading always terminates the pending
    attachment so equations at a section boundary cannot merge two sections.
    The raw Markdown prose-block count is reported separately below.
    """
    paragraphs: list[str] = []
    merge_after_display_math = False
    for block in re.split(r"\n\s*\n", body):
        block = block.strip()
        if not block:
            continue
        if block.startswith("#") or block.startswith("**关键词**"):
            merge_after_display_math = False
            continue
        if block.startswith("\\[") and block.endswith("\\]"):
            merge_after_display_math = bool(paragraphs)
            continue
        if merge_after_display_math and paragraphs:
            paragraphs[-1] = f"{paragraphs[-1]}\n{block}"
            merge_after_display_math = False
            continue
        paragraphs.append(block)
    return paragraphs


def raw_prose_blocks(body: str) -> list[str]:
    """Return nonheading, nonformula Markdown prose blocks without merging."""
    return [
        block.strip()
        for block in re.split(r"\n\s*\n", body)
        if block.strip()
        and not block.strip().startswith("#")
        and not block.strip().startswith("**关键词**")
        and not (
            block.strip().startswith("\\[")
            and block.strip().endswith("\\]")
        )
    ]


def citation_keys(body: str) -> set[tuple[str, str]]:
    keys: set[tuple[str, str]] = set()
    multi_author_patterns = (
        r"\b([A-Z][A-Za-zÀ-ž-]+)\s+et al\.\s*[（(]?((?:19|20)\d{2}[a-z]?)",
        r"\b([A-Z][A-Za-zÀ-ž-]+)\s+and\s+(?:[A-Z][A-Za-zÀ-ž-]+\s+)?[A-Z][A-Za-zÀ-ž-]+\s*[（(]?((?:19|20)\d{2}[a-z]?)",
    )
    for pattern in multi_author_patterns:
        for match in re.finditer(pattern, body):
            keys.add((match.group(1), match.group(2)))
    single_author_pattern = (
        r"\b([A-Z][A-Za-zÀ-ž-]+)\s*[（(]?((?:19|20)\d{2}[a-z]?)[）)]?"
    )
    for match in re.finditer(single_author_pattern, body):
        prefix = body[max(0, match.start() - 40) : match.start()]
        # Do not reinterpret the final token of a compound second-author surname,
        # such as "Mookerjee and Dos Santos (1993)", as a new citation key.
        if re.search(r"\band\s+(?:[A-Z][A-Za-zÀ-ž-]+\s+)?$", prefix):
            continue
        keys.add((match.group(1), match.group(2)))
    return keys


def reference_keys(reference_text: str) -> set[tuple[str, str]]:
    keys: set[tuple[str, str]] = set()
    for line in reference_text.splitlines():
        match = re.match(
            r"([A-Z][A-Za-zÀ-ž-]+)(?:,|\.).*?\b((?:19|20)\d{2}[a-z]?)\.",
            line.strip(),
        )
        if match:
            keys.add((match.group(1), match.group(2)))
    return keys


def audit_paper(path: Path) -> dict[str, object]:
    text = path.read_text(encoding="utf-8")
    if "## 参考文献" in text:
        body, reference_text = text.split("## 参考文献", 1)
    else:
        body, reference_text = text, ""

    citations = citation_keys(body)
    references = reference_keys(reference_text)
    prose = prose_for_style_scan(body)
    control_characters = [
        {"offset": index, "codepoint": ord(character)}
        for index, character in enumerate(text)
        if ord(character) < 32 and character not in "\n\r\t"
    ]

    return {
        "file": str(path),
        "characters": len(text),
        "substantive_paragraphs": len(substantive_paragraphs(body)),
        "raw_prose_blocks": len(raw_prose_blocks(body)),
        "reference_entries": len(references),
        "unique_citation_keys": len(citations),
        "missing_reference_keys": sorted(f"{author} {year}" for author, year in citations - references),
        "unused_reference_keys": sorted(f"{author} {year}" for author, year in references - citations),
        "banned_phrases": {
            phrase: body.count(phrase) for phrase in BANNED_PHRASES if phrase in body
        },
        "special_punctuation": {
            mark: prose.count(mark) for mark in SPECIAL_PUNCTUATION if mark in prose
        },
        "control_characters": control_characters,
        "replacement_characters": text.count("\ufffd"),
        "unresolved_placeholders": {
            marker: text.count(marker)
            for marker in ("[引文待核]", "TODO", "TBD", "待补", "待定")
            if marker in text
        },
        "has_abstract": "## 摘要" in body,
        "has_introduction": "## 1 引言" in body,
        "has_method": bool(re.search(r"^## 3 ", body, re.MULTILINE)),
        "has_evaluation": bool(re.search(r"^## 4 ", body, re.MULTILINE)),
        "has_contributions": bool(re.search(r"^## 5 ", body, re.MULTILINE)),
        "has_conclusion": bool(re.search(r"^## 6 ", body, re.MULTILINE)),
        "has_references": bool(reference_text.strip()),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("paths", nargs="+", type=Path)
    args = parser.parse_args()
    results = [audit_paper(path) for path in args.paths]
    print(json.dumps(results, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
