#!/usr/bin/env python3
"""Report Markdown section/paragraph/sentence shape as a diagnostic.

The report deliberately has no scholarly PASS verdict. Sparse or fragmented
sections are inspection triggers; only direct reading can decide quality.
"""

from __future__ import annotations

import argparse
import json
import re
from dataclasses import dataclass, field
from pathlib import Path


HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*$")
SENTENCE_RE = re.compile(r"[^。！？!?\.]+[。！？!?\.]?|[^。！？!?\.]+$")
WORD_OR_CJK_RE = re.compile(r"[A-Za-z0-9\u3400-\u9fff]")
DEFAULT_EXCLUDED_HEADING_RE = re.compile(r"^(references|bibliography|参考文献)$", re.IGNORECASE)


@dataclass
class Section:
    heading: str
    level: int
    paragraphs: list[str] = field(default_factory=list)
    paragraph_owners: list[str | None] = field(default_factory=list)
    child_headings: list[str] = field(default_factory=list)

    @property
    def sentence_count(self) -> int:
        return sum(count_sentences(paragraph) for paragraph in self.paragraphs)

    @property
    def prose_chars(self) -> int:
        return sum(len(re.sub(r"\s+", "", paragraph)) for paragraph in self.paragraphs)

    def report(self, warn_below: int) -> dict[str, object]:
        warnings: list[str] = []
        subsection_reports: list[dict[str, object]] = []
        for heading in self.child_headings:
            paragraphs = [
                paragraph
                for paragraph, owner in zip(self.paragraphs, self.paragraph_owners)
                if owner == heading
            ]
            sentence_count = sum(count_sentences(paragraph) for paragraph in paragraphs)
            subsection_warnings: list[str] = []
            if len(paragraphs) <= 1:
                subsection_warnings.append("one or fewer prose paragraphs")
            if sentence_count < 4:
                subsection_warnings.append("fewer than 4 prose sentences")
            subsection_reports.append(
                {
                    "heading": heading,
                    "paragraphs": len(paragraphs),
                    "sentences": sentence_count,
                    "warnings": subsection_warnings,
                }
            )
        if self.heading != "(preamble)" and self.sentence_count < warn_below:
            warnings.append(f"fewer than {warn_below} prose sentences; inspect argument completeness")
        if self.child_headings and len(self.paragraphs) <= len(self.child_headings):
            warnings.append("one or fewer prose paragraphs per child heading; inspect fragmentation")
        micro_subsections = sum(1 for report in subsection_reports if report["warnings"])
        if micro_subsections:
            warnings.append(f"{micro_subsections} child headings are structurally thin; inspect heading fragmentation")
        return {
            "heading": self.heading,
            "level": self.level,
            "paragraphs": len(self.paragraphs),
            "sentences": self.sentence_count,
            "prose_chars": self.prose_chars,
            "child_headings": len(self.child_headings),
            "subsections": subsection_reports,
            "warnings": warnings,
        }


def count_sentences(text: str) -> int:
    return sum(1 for part in SENTENCE_RE.findall(text) if WORD_OR_CJK_RE.search(part))


def parse_sections(text: str, excluded_heading_re: re.Pattern[str]) -> list[Section]:
    sections: list[Section] = [Section("(preamble)", 0)]
    current = sections[0]
    current_child: str | None = None
    paragraph_lines: list[str] = []
    in_fence = False

    def flush() -> None:
        nonlocal paragraph_lines
        paragraph = " ".join(line.strip() for line in paragraph_lines if line.strip()).strip()
        if paragraph:
            current.paragraphs.append(paragraph)
            current.paragraph_owners.append(current_child)
        paragraph_lines = []

    for raw_line in text.splitlines():
        line = raw_line.rstrip()
        if line.lstrip().startswith("```") or line.lstrip().startswith("~~~"):
            flush()
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        match = HEADING_RE.match(line)
        if match:
            flush()
            level = len(match.group(1))
            heading = match.group(2).strip()
            if level <= 2:
                current = Section(heading, level)
                sections.append(current)
                current_child = None
            else:
                current.child_headings.append(heading)
                current_child = heading
            continue
        stripped = line.strip()
        if not stripped:
            flush()
        elif stripped.startswith("|") or stripped.startswith("<!--"):
            flush()
        else:
            paragraph_lines.append(stripped)
    flush()
    return [
        section
        for section in sections
        if (section.paragraphs or section.child_headings)
        and not excluded_heading_re.search(section.heading.strip())
    ]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("markdown", type=Path)
    parser.add_argument("--warn-below-sentences", type=int, default=8)
    parser.add_argument(
        "--exclude-heading-regex",
        default=DEFAULT_EXCLUDED_HEADING_RE.pattern,
        help="case-insensitive regex for non-prose major sections to omit",
    )
    parser.add_argument("--json", action="store_true", dest="as_json")
    args = parser.parse_args()

    text = args.markdown.read_text(encoding="utf-8-sig")
    excluded_heading_re = re.compile(args.exclude_heading_regex, re.IGNORECASE)
    reports = [
        section.report(args.warn_below_sentences)
        for section in parse_sections(text, excluded_heading_re)
    ]
    payload = {
        "file": str(args.markdown.resolve()),
        "interpretation": "diagnostic only; warnings are not acceptance verdicts",
        "sections": reports,
    }
    if args.as_json:
        print(json.dumps(payload, ensure_ascii=False, indent=2))
    else:
        print(payload["file"])
        print(payload["interpretation"])
        print("sentences\tparagraphs\tchild_headings\tprose_chars\theading")
        for report in reports:
            print(
                f"{report['sentences']}\t{report['paragraphs']}\t"
                f"{report['child_headings']}\t{report['prose_chars']}\t{report['heading']}"
            )
            for warning in report["warnings"]:
                print(f"  WARNING: {warning}")
            for subsection in report["subsections"]:
                if subsection["warnings"]:
                    print(
                        f"    SUBSECTION: {subsection['sentences']} sentences, "
                        f"{subsection['paragraphs']} paragraphs — {subsection['heading']} "
                        f"({'; '.join(subsection['warnings'])})"
                    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
