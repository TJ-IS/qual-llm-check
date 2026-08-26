from __future__ import annotations

import re
import sys
from pathlib import Path


def section_text(path: Path, heading: str) -> str:
    text = path.read_text(encoding="utf-8-sig")
    if re.fullmatch(r"\d+", heading):
        pattern = rf"^##\s+{re.escape(heading)}(?:\.|\s).*$"
    else:
        pattern = rf"^##\s+{re.escape(heading)}\s*$"
    match = re.search(pattern, text, flags=re.MULTILINE)
    if not match:
        raise ValueError(f"section not found: {heading}")
    remainder = text[match.end() :]
    next_heading = re.search(r"^##\s+", remainder, flags=re.MULTILINE)
    return remainder[: next_heading.start()] if next_heading else remainder


def prose_paragraphs(text: str) -> list[str]:
    paragraphs: list[str] = []
    for block in re.split(r"\n\s*\n", text):
        normalized = " ".join(line.strip() for line in block.splitlines()).strip()
        if not normalized or normalized.startswith(("#", "|", "```", "$$", "\\[", "\\begin{", "![", "**表", "**Table", "**算法", "**Algorithm")):
            continue
        paragraphs.append(normalized)
    return paragraphs


def sentence_list(paragraph: str) -> list[str]:
    return [part.strip() for part in re.split(r"(?<=[。！？])", paragraph) if part.strip()]


def main() -> None:
    if len(sys.argv) != 3:
        raise SystemExit("usage: audit_v10_draft_sections.py DRAFT HEADING")
    path = Path(sys.argv[1])
    paragraphs = prose_paragraphs(section_text(path, sys.argv[2]))
    groups = [sentence_list(paragraph) for paragraph in paragraphs]
    sentences = [sentence for group in groups for sentence in group]
    chars = sum(len(re.sub(r"\s+", "", paragraph)) for paragraph in paragraphs)
    citation_pattern = re.compile(r"[（(][^()（）]*(?:(?:19|20)\d{2}|et al\.)[^()（）]*[)）]")
    citation_groups = sum(len(citation_pattern.findall(paragraph)) for paragraph in paragraphs)
    citation_sentences = sum(bool(citation_pattern.search(sentence)) for sentence in sentences)
    print(f"file={path}")
    print(f"section={sys.argv[2]}")
    print(f"paragraphs={len(paragraphs)}")
    print(f"sentences={len(sentences)}")
    print(f"characters={chars}")
    print(f"sentences_per_paragraph={len(sentences) / len(paragraphs):.2f}")
    print(f"short_paragraphs={sum(len(group) <= 2 for group in groups)}")
    print(f"citation_groups={citation_groups}")
    print(f"citation_sentences={citation_sentences}")
    print(f"semicolons={sum(paragraph.count('；') for paragraph in paragraphs)}")
    print(f"colons={sum(paragraph.count('：') for paragraph in paragraphs)}")
    print(f"em_dashes={sum(paragraph.count('—') for paragraph in paragraphs)}")
    print("paragraph_detail=")
    for index, (paragraph, group) in enumerate(zip(paragraphs, groups), start=1):
        citations = len(citation_pattern.findall(paragraph))
        print(
            f"  {index}: sentences={len(group)}, characters={len(re.sub(r'\\s+', '', paragraph))}, "
            f"citations={citations}, opening={paragraph[:42]}"
        )


if __name__ == "__main__":
    main()
