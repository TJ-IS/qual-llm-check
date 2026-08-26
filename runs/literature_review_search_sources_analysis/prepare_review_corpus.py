#!/usr/bin/env python3
"""Select high-confidence review papers from the local Otero Basket corpus."""

from __future__ import annotations

import json
import os
import re
from pathlib import Path


RUN_DIR = Path(__file__).resolve().parent
ROOT = RUN_DIR.parents[1]
DATABASE_DIR = ROOT / "database_fulltext_all"
METADATA_PATH = DATABASE_DIR / "metadata.jsonl"
RESULTS_PATH = DATABASE_DIR / "results.jsonl"
CORPUS_DIR = RUN_DIR / "review_fulltexts"
MANIFEST_PATH = RUN_DIR / "candidate_manifest.jsonl"
SUMMARY_PATH = RUN_DIR / "candidate_summary.json"

TITLE_RE = re.compile(
    r"(systematic|structured|integrative|scoping|critical|comprehensive) "
    r"(?:literature )?review|literature review|meta[- ]analys(?:is|es)|"
    r"bibliometric|research synthesis|synthesi[sz]ing research|"
    r"review and (?:research )?agenda|review of (?:the )?(?:literature|research)",
    re.IGNORECASE,
)
ABSTRACT_RE = re.compile(
    r"\b(systematic literature review|structured literature review|"
    r"scoping review|integrative literature review|meta[- ]analys(?:is|es)|"
    r"bibliometric (?:review|analysis)|"
    r"reviewed? (?:a |the )?(?:sample of )?\d+ (?:articles|papers|studies)|"
    r"review of \d+ (?:articles|papers|studies)|literature search|"
    r"search(?:ed|ing) (?:the following )?(?:electronic )?databases)\b",
    re.IGNORECASE,
)


def load_jsonl(path: Path) -> list[dict]:
    with path.open("r", encoding="utf-8") as handle:
        return [json.loads(line) for line in handle if line.strip()]


def extract_year(date_value: str) -> str:
    match = re.search(r"(?:19|20)\d{2}", date_value or "")
    return match.group(0) if match else ""


def main() -> None:
    results = {
        int(item["id"]): item
        for item in load_jsonl(RESULTS_PATH)
        if item.get("status") == "downloaded" and item.get("file")
    }
    candidates: list[dict] = []
    for item in load_jsonl(METADATA_PATH):
        fields = item.get("fields") or {}
        title = str(fields.get("title") or "")
        abstract = str(fields.get("abstractNote") or "")
        title_match = TITLE_RE.search(title)
        abstract_match = ABSTRACT_RE.search(abstract)
        if title_match is None and abstract_match is None:
            continue
        result = results.get(int(item["id"]))
        if result is None:
            continue
        source_path = DATABASE_DIR / str(result["file"])
        if not source_path.is_file():
            raise FileNotFoundError(source_path)
        candidates.append(
            {
                "otero_id": int(item["id"]),
                "title": title,
                "year": extract_year(str(fields.get("date") or "")),
                "journal": str(fields.get("publicationTitle") or ""),
                "doi": str(fields.get("DOI") or result.get("doi") or ""),
                "source_file": source_path.name,
                "selection_title_evidence": title_match.group(0) if title_match else "",
                "selection_abstract_evidence": (
                    abstract_match.group(0) if abstract_match else ""
                ),
            }
        )

    candidates.sort(
        key=lambda row: (
            row["journal"].casefold(),
            -(int(row["year"]) if row["year"] else 0),
            row["title"].casefold(),
        )
    )
    CORPUS_DIR.mkdir(parents=True, exist_ok=True)
    for candidate in candidates:
        source = DATABASE_DIR / candidate["source_file"]
        destination = CORPUS_DIR / candidate["source_file"]
        if destination.exists():
            continue
        try:
            os.link(source, destination)
        except OSError:
            destination.write_bytes(source.read_bytes())

    with MANIFEST_PATH.open("w", encoding="utf-8", newline="\n") as handle:
        for candidate in candidates:
            handle.write(json.dumps(candidate, ensure_ascii=False) + "\n")
    summary = {
        "selection_version": "review-candidate-v1",
        "candidates": len(candidates),
        "corpus_markdown_files": len(list(CORPUS_DIR.glob("*.md"))),
        "selection_logic": {
            "title_regex": TITLE_RE.pattern,
            "abstract_regex": ABSTRACT_RE.pattern,
        },
    }
    SUMMARY_PATH.write_text(
        json.dumps(summary, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
