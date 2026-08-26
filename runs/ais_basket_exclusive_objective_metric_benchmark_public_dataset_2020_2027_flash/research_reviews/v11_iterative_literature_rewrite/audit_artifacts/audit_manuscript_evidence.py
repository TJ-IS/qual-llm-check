from __future__ import annotations

import argparse
import collections
import datetime
import hashlib
import json
import re
from pathlib import Path


SECTION_RE = re.compile(r"^##\s+([1-9]\d*)(?:\.|\s).*$", re.MULTILINE)
REFERENCE_HEADING_RE = re.compile(
    r"^##\s+(?:参考文献|References|Bibliography)\s*$",
    re.MULTILINE | re.IGNORECASE,
)
CITATION_GROUP_RE = re.compile(
    r"[（(]([^()（）]*(?:(?:19|20)\d{2}|et al\.)[^()（）]*)[)）]"
)
SOURCE_RE = re.compile(
    r"([A-Z][A-Za-zÀ-ÖØ-öø-ÿ'’\-]+"
    r"(?:\s+(?:and|&)\s+[A-Z][A-Za-zÀ-ÖØ-öø-ÿ'’\-]+|\s+et al\.)?)"
    r"\s*[,，]?\s*((?:19|20)\d{2})"
)
INLINE_PLACEHOLDER_RE = re.compile(r"\[\[待补文献[：:][^\n]*?\]\]")
EMPIRICAL_RE = re.compile(
    r"结果表明|我们发现|显著优于|显著提高|证明了|实验结果显示|结果证明"
)
FORBIDDEN_MARKS = ("：", "；", ";", ":", "—", "–", "“", "”", "‘", "’", "…", "→")


def section_slices(text: str) -> list[tuple[str, str]]:
    matches = list(SECTION_RE.finditer(text))
    sections: list[tuple[str, str]] = []
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        sections.append((match.group(1), text[match.end() : end]))
    return sections


def prose_paragraphs(section: str) -> list[str]:
    paragraphs: list[str] = []
    excluded_prefixes = (
        "#",
        "|",
        "```",
        "$$",
        "\\[",
        "\\begin{",
        "![",
        "**表",
        "**Table",
        "**算法",
        "**Algorithm",
    )
    for block in re.split(r"\n\s*\n", section):
        normalized = " ".join(line.strip() for line in block.splitlines()).strip()
        if not normalized or normalized.startswith(excluded_prefixes):
            continue
        paragraphs.append(normalized)
    return paragraphs


def sentence_list(paragraph: str) -> list[str]:
    return [
        part.strip()
        for part in re.split(r"(?<=[。！？!?])", paragraph)
        if part.strip()
    ]


def source_keys(group: str) -> list[str]:
    return [f"{author} {year}" for author, year in SOURCE_RE.findall(group)]


def audit_full_body(text: str) -> dict[str, object]:
    without_placeholders = INLINE_PLACEHOLDER_RE.sub("", text)
    empirical_hits = [
        {"line": number, "text": line.strip()}
        for number, line in enumerate(text.splitlines(), start=1)
        if EMPIRICAL_RE.search(line)
    ]
    return {
        "scope": "all content before the reference heading, including headings, tables, formulas, algorithms, captions and prose",
        "inline_placeholder_occurrences": len(INLINE_PLACEHOLDER_RE.findall(text)),
        "forbidden_punctuation": {
            mark: text.count(mark) for mark in FORBIDDEN_MARKS
        },
        "non_placeholder_forbidden_punctuation": {
            mark: without_placeholders.count(mark) for mark in FORBIDDEN_MARKS
        },
        "empirical_phrase_hits": empirical_hits,
    }


def audit_section(number: str, text: str) -> dict[str, object]:
    paragraphs = prose_paragraphs(text)
    paragraphs_without_placeholders = [
        INLINE_PLACEHOLDER_RE.sub("", paragraph) for paragraph in paragraphs
    ]
    sentences = [sentence for paragraph in paragraphs for sentence in sentence_list(paragraph)]
    groups = [
        group
        for paragraph in paragraphs
        for group in CITATION_GROUP_RE.findall(paragraph)
    ]
    sources = [source for group in groups for source in source_keys(group)]
    source_counts = collections.Counter(sources)
    citation_sentences = [
        sentence for sentence in sentences if CITATION_GROUP_RE.search(sentence)
    ]
    uncited_paragraphs = [
        {
            "paragraph": index,
            "sentences": len(sentence_list(paragraph)),
            "opening": paragraph[:80],
        }
        for index, paragraph in enumerate(paragraphs, start=1)
        if not CITATION_GROUP_RE.search(paragraph)
    ]
    colon_locations = [
        {
            "paragraph": index,
            "count": paragraph.count("：") + paragraph.count(":"),
            "opening": paragraph[:100],
        }
        for index, paragraph in enumerate(paragraphs, start=1)
        if "：" in paragraph or ":" in paragraph
    ]
    non_placeholder_colon_locations = [
        {
            "paragraph": index,
            "count": paragraph.count("：") + paragraph.count(":"),
            "opening": paragraph[:100],
        }
        for index, paragraph in enumerate(paragraphs_without_placeholders, start=1)
        if "：" in paragraph or ":" in paragraph
    ]
    top_count = source_counts.most_common(1)[0][1] if source_counts else 0
    return {
        "section": number,
        "paragraphs": len(paragraphs),
        "sentences": len(sentences),
        "characters": sum(len(re.sub(r"\s+", "", paragraph)) for paragraph in paragraphs),
        "sentences_per_paragraph": round(len(sentences) / len(paragraphs), 3)
        if paragraphs
        else 0,
        "citation_groups": len(groups),
        "citation_sentences": len(citation_sentences),
        "citation_sentence_share": round(len(citation_sentences) / len(sentences), 4)
        if sentences
        else 0,
        "source_mentions": len(sources),
        "unique_sources": len(source_counts),
        "top_source_share": round(top_count / len(sources), 4) if sources else 0,
        "top_sources": source_counts.most_common(12),
        "uncited_paragraphs": uncited_paragraphs,
        "semicolons": sum(paragraph.count("；") + paragraph.count(";") for paragraph in paragraphs),
        "colons": sum(paragraph.count("：") + paragraph.count(":") for paragraph in paragraphs),
        "em_dashes": sum(paragraph.count("—") for paragraph in paragraphs),
        "quotation_marks": sum(paragraph.count(mark) for paragraph in paragraphs for mark in ("“", "”")),
        "colon_locations": colon_locations,
        "inline_placeholder_occurrences": sum(
            len(INLINE_PLACEHOLDER_RE.findall(paragraph)) for paragraph in paragraphs
        ),
        "non_placeholder_semicolons": sum(
            paragraph.count("；") + paragraph.count(";")
            for paragraph in paragraphs_without_placeholders
        ),
        "non_placeholder_colons": sum(
            paragraph.count("：") + paragraph.count(":")
            for paragraph in paragraphs_without_placeholders
        ),
        "non_placeholder_em_dashes": sum(
            paragraph.count("—") for paragraph in paragraphs_without_placeholders
        ),
        "non_placeholder_quotation_marks": sum(
            paragraph.count(mark)
            for paragraph in paragraphs_without_placeholders
            for mark in ("“", "”")
        ),
        "non_placeholder_colon_locations": non_placeholder_colon_locations,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("manuscript", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    raw = args.manuscript.read_bytes()
    text = raw.decode("utf-8-sig")
    manuscript_body = REFERENCE_HEADING_RE.split(text, maxsplit=1)[0]
    result = {
        "manuscript": str(args.manuscript),
        "manuscript_sha256": hashlib.sha256(raw).hexdigest(),
        "audit_script": str(Path(__file__).resolve()),
        "audit_script_sha256": hashlib.sha256(
            Path(__file__).read_bytes()
        ).hexdigest(),
        "generated_at_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "full_body_scope": audit_full_body(manuscript_body),
        "sections": [
            audit_section(number, body)
            for number, body in section_slices(manuscript_body)
        ],
    }
    rendered = json.dumps(result, ensure_ascii=False, indent=2)
    if args.output:
        args.output.write_text(rendered + "\n", encoding="utf-8")
    else:
        print(rendered)


if __name__ == "__main__":
    main()
