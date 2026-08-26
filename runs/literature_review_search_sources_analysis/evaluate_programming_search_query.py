#!/usr/bin/env python3
"""Evaluate a reproducible programming-context query against local benchmarks."""

from __future__ import annotations

import csv
import json
import re
from collections import Counter
from pathlib import Path


RUN_DIR = Path(__file__).resolve().parent
ROOT = RUN_DIR.parents[1]
METADATA_CSV = ROOT / "database" / "ALL_AIS_Basket_11.csv"
FULLTEXT_RESULTS = ROOT / "database_fulltext_all" / "results.jsonl"
DIRECT_MATCHES = (
    ROOT
    / "runs"
    / "direct_programming_research_deepseek_analysis"
    / "output_v1"
    / "direct_programming_matches.csv"
)
OUTPUT = RUN_DIR / "programming_query_evaluation.json"

QUERY_TERMS = [
    "computer program*",
    "source code",
    "program comprehension",
    "code comprehension",
    "programmer*",
    "software developer*",
    "coding task*",
    "programming task*",
    "debugging",
    "pair programming",
    "test-driven development",
    "end-user programming",
    "spreadsheet programming/development/debugging/testing/error correction",
    "query formulation",
    "query development",
    "SQL query",
    "instantiation(s) of data model(s)",
    "AI-assisted programming/coding",
    "coding agent*",
    "programming assistant*",
    "code generation/review/inspection/modification",
    "writing code",
]

QUERY_RE = re.compile(
    r"computer program(?:ming|s)?|source code|program comprehension|"
    r"code comprehension|\bprogrammers?\b|software developers?|coding tasks?|"
    r"programming tasks?|\bdebugging\b|pair programming|"
    r"test[- ]driven development|end[- ]user programming|"
    r"spreadsheet (?:programming|development|debugging|testing|error correction)|"
    r"query formulation|query development|\bSQL quer(?:y|ies)\b|"
    r"instantiations? of data models?|AI[- ]assisted (?:programming|coding)|"
    r"coding agents?|programming assistants?|code generation|code review|"
    r"code inspection|code modification|writing code",
    re.IGNORECASE,
)


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def row_text(row: dict[str, str]) -> str:
    return " ".join(
        row.get(field, "") or ""
        for field in ("Title", "Abstract", "Author Keywords", "Index Keywords")
    )


def main() -> None:
    metadata = read_csv(METADATA_CSV)
    hits = [row for row in metadata if QUERY_RE.search(row_text(row))]
    hit_dois = {
        (row.get("DOI") or "").strip().casefold()
        for row in hits
        if row.get("DOI")
    }
    downloaded_dois = {
        str(item.get("doi") or "").strip().casefold()
        for item in (
            json.loads(line)
            for line in FULLTEXT_RESULTS.open("r", encoding="utf-8")
            if line.strip()
        )
        if item.get("status") == "downloaded" and item.get("doi")
    }

    direct = read_csv(DIRECT_MATCHES)
    direct_human = [
        row for row in direct if (row.get("has_human_programming_task") or "") == "True"
    ]

    def benchmark(rows: list[dict[str, str]]) -> dict:
        covered = [
            row
            for row in rows
            if (row.get("doi") or "").strip().casefold() in hit_dois
        ]
        missed = [
            {
                "title": row.get("title") or "",
                "year": row.get("year") or "",
                "direct_focus_type": row.get("direct_focus_type") or "",
            }
            for row in rows
            if row not in covered
        ]
        return {
            "benchmark_total": len(rows),
            "covered": len(covered),
            "recall": len(covered) / len(rows) if rows else None,
            "missed": missed,
        }

    output = {
        "query_version": "programming-metadata-v1",
        "searched_fields": [
            "Title",
            "Abstract",
            "Author Keywords",
            "Index Keywords",
        ],
        "query_terms": QUERY_TERMS,
        "basket_metadata_records": len(metadata),
        "query_hits": len(hits),
        "query_hits_with_local_fulltext": sum(
            (row.get("DOI") or "").strip().casefold() in downloaded_dois
            for row in hits
        ),
        "query_hits_without_doi": sum(not row.get("DOI") for row in hits),
        "recent_hits": {
            "2016+": sum(int(row["Year"]) >= 2016 for row in hits),
            "2021+": sum(int(row["Year"]) >= 2021 for row in hits),
        },
        "top_journals": Counter(row["Source title"] for row in hits).most_common(),
        "benchmark_direct_programming_28": benchmark(direct),
        "benchmark_direct_human_programming_21": benchmark(direct_human),
    }
    OUTPUT.write_text(
        json.dumps(output, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(output, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
