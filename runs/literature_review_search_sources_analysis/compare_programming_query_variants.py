#!/usr/bin/env python3
"""Compare candidate programming-review search blocks in Basket metadata."""

from __future__ import annotations

import csv
import json
import re
from collections import Counter
from pathlib import Path


RUN_DIR = Path(__file__).resolve().parent
ROOT = RUN_DIR.parents[1]
METADATA_CSV = ROOT / "database" / "ALL_AIS_Basket_11.csv"
DIRECT_MATCHES = (
    ROOT
    / "runs"
    / "direct_programming_research_deepseek_analysis"
    / "output_v1"
    / "direct_programming_matches.csv"
)
OUTPUT = RUN_DIR / "programming_query_variants.json"
FIELDS = ("Title", "Abstract", "Author Keywords", "Index Keywords")

STRICT = (
    r"program comprehension|code comprehension|programming tasks?|coding tasks?|"
    r"pair programming|test[- ]driven development|end[- ]user programming|"
    r"AI[- ]assisted (?:programming|coding)|coding agents?|programming assistants?|"
    r"code review|code inspection|code completion|code auto[- ]?complet(?:e|ion)|"
    r"code suggestions?|writing code"
)
EXPANDED = (
    r"computer program(?:ming|s)?|source code|program comprehension|"
    r"code comprehension|\bprogrammers?\b|software developers?|coding tasks?|"
    r"programming tasks?|\bdebugging\b|pair programming|"
    r"test[- ]driven development|end[- ]user programming|"
    r"spreadsheet (?:programming|development|debugging|testing|error correction)|"
    r"query formulation|query development|\bSQL quer(?:y|ies)\b|"
    r"instantiations? of data models?|AI[- ]assisted (?:programming|coding)|"
    r"coding agents?|programming assistants?|code generation|code review|"
    r"code inspection|code modification|code completion|"
    r"code auto[- ]?complet(?:e|ion)|code suggestions?|writing code"
)
MODERN_AGENT = (
    r"AI[- ]assisted (?:programming|coding|software development)|"
    r"AI pair programmers?|coding agents?|programming agents?|"
    r"programming assistants?|code assistants?|code completion|"
    r"code auto[- ]?complet(?:e|ion)|code suggestions?|GitHub Copilot|OpenAI Codex|"
    r"(?:large language models?|\bLLMs?\b|ChatGPT) .{0,80} "
    r"(?:programming|coding|source code|code generation|software development)|"
    r"(?:programming|coding|source code|code generation|software development) .{0,80} "
    r"(?:large language models?|\bLLMs?\b|ChatGPT)"
)
AIS_PROFESSIONAL = (
    r"(?:computer )?program comprehension|program understanding|"
    r"software comprehension|software modification|"
    r"programming tasks?|programming performance|programmer performance|"
    r"programming productivity|programming environments?|"
    r"program construction|program maintenance|maintainable software|"
    r"query formulation|query development|query reuse|query complexity|"
    r"structured query languages?|\bSQL\b|"
    r"spreadsheet (?:errors?|testing|development|debugging|programming|"
    r"error correction|code inspection|formulas?)|"
    r"end[- ]user (?:programming|computing|development)|"
    r"pair programming|test[- ]driven development|"
    r"code inspection|code review|(?:program|code) debugging|software testing|"
    r"knowledge[- ]based systems? development|database structure representation|"
    r"AI[- ]assisted (?:programming|coding)|coding agents?|programming agents?|"
    r"(?:programming|coding|code) assistants?|"
    r"code completion|code auto[- ]?complet(?:e|ion)|code suggestions?"
)
AIS_PROFESSIONAL_REFINED = (
    r"(?:computer )?program comprehension|program understanding|"
    r"software comprehension|software modification|"
    r"programming tasks?|programming performance|programmer performance|"
    r"programming productivity|programming environments?|"
    r"program construction|program maintenance|maintainable software|"
    r"query formulation|query development|query reuse|query complexity|"
    r"structured query languages?|"
    r"spreadsheet (?:errors?|testing|development|debugging|programming|"
    r"error correction|code inspection|formulas?|models?)|"
    r"end[- ]user (?:programming|development)|"
    r"end[- ]user computing.{0,50}(?:programming|productivity|spreadsheet)|"
    r"(?:programming|productivity|spreadsheet).{0,50}end[- ]user computing|"
    r"pair programming|test[- ]driven development|"
    r"code inspect(?:ion|ing)|code review|(?:program|code) debugging|"
    r"knowledge[- ]based systems? development|database structure representation|"
    r"AI[- ]assisted (?:programming|coding)|coding agents?|programming agents?|"
    r"(?:programming|coding|code) assistants?|code generation|"
    r"code completion|code auto[- ]?complet(?:e|ion)|code suggestions?|"
    r"writing code"
)

VARIANTS = {
    "S1_strict_distinctive": re.compile(STRICT, re.IGNORECASE),
    "S2_expanded_direct_activity": re.compile(EXPANDED, re.IGNORECASE),
    "S3_expanded_plus_open_source_development": re.compile(
        EXPANDED + r"|open[- ]source software development",
        re.IGNORECASE,
    ),
    "S4_broad_software_development": re.compile(
        EXPANDED
        + r"|open[- ]source software development|software development|"
        + r"software engineering|information systems? development",
        re.IGNORECASE,
    ),
    "S5_modern_programming_agents": re.compile(MODERN_AGENT, re.IGNORECASE),
    "S6_ais_professional_vocabulary": re.compile(
        AIS_PROFESSIONAL,
        re.IGNORECASE,
    ),
    "S7_ais_professional_plus_open_source": re.compile(
        AIS_PROFESSIONAL + r"|open[- ]source software development",
        re.IGNORECASE,
    ),
    "S8_ais_professional_refined": re.compile(
        AIS_PROFESSIONAL_REFINED,
        re.IGNORECASE,
    ),
}


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def normalized_doi(row: dict[str, str], field: str) -> str:
    return (row.get(field) or "").strip().casefold()


def main() -> None:
    metadata = read_csv(METADATA_CSV)
    direct = read_csv(DIRECT_MATCHES)
    direct_human = [
        row for row in direct if (row.get("has_human_programming_task") or "") == "True"
    ]
    core_direct = [
        row
        for row in direct
        if (row.get("direct_focus_type") or "")
        in {
            "human_programming_task",
            "programming_method_process",
            "programming_education_task",
        }
    ]
    metadata_by_doi = {
        normalized_doi(row, "DOI"): row
        for row in metadata
        if normalized_doi(row, "DOI")
    }

    output: dict[str, dict] = {}
    for name, pattern in VARIANTS.items():
        hits = [
            row
            for row in metadata
            if pattern.search(" ".join(row.get(field, "") or "" for field in FIELDS))
        ]
        hit_dois = {
            normalized_doi(row, "DOI")
            for row in hits
            if normalized_doi(row, "DOI")
        }

        def benchmark(rows: list[dict[str, str]]) -> dict:
            covered = [
                row for row in rows if normalized_doi(row, "doi") in hit_dois
            ]
            return {
                "total": len(rows),
                "covered": len(covered),
                "recall": len(covered) / len(rows) if rows else None,
                "missed_titles": [
                    row.get("title") or "" for row in rows if row not in covered
                ],
            }

        output[name] = {
            "basket_hits": len(hits),
            "2016+": sum(int(row["Year"]) >= 2016 for row in hits),
            "2021+": sum(int(row["Year"]) >= 2021 for row in hits),
            "top_journals": Counter(row["Source title"] for row in hits).most_common(11),
            "direct_programming_28": benchmark(direct),
            "direct_human_programming_21": benchmark(direct_human),
            "manually_confirmed_core_20": benchmark(core_direct),
        }

    payload = {
        "searched_fields": list(FIELDS),
        "basket_metadata_records": len(metadata),
        "variants": output,
    }
    OUTPUT.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(payload, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
