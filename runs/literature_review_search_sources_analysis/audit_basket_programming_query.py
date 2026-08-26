#!/usr/bin/env python3
"""Audit Basket programming-query candidates against prior full-text screens."""

from __future__ import annotations

import csv
import json
import re
from collections import Counter
from pathlib import Path


RUN_DIR = Path(__file__).resolve().parent
ROOT = RUN_DIR.parents[1]
METADATA_CSV = ROOT / "database" / "ALL_AIS_Basket_11.csv"
FIRST_PASS_JSONL = (
    ROOT
    / "runs"
    / "programming_context_deepseek_analysis"
    / "output_v1_fresh"
    / "decisions.jsonl"
)
DIRECT_DECISIONS_CSV = (
    ROOT
    / "runs"
    / "direct_programming_research_deepseek_analysis"
    / "output_v1"
    / "direct_programming_decisions.csv"
)

SUMMARY_JSON = RUN_DIR / "basket_programming_query_audit.json"
CANDIDATES_CSV = RUN_DIR / "basket_programming_query_candidates.csv"
RECENT_CSV = RUN_DIR / "basket_programming_query_recent_candidates.csv"
CORE_TERMS_CSV = RUN_DIR / "basket_core_20_metadata_terms.csv"
PROFESSIONAL_CANDIDATES_CSV = (
    RUN_DIR / "basket_ais_professional_vocabulary_candidates.csv"
)

FIELDS = ("Title", "Abstract", "Author Keywords", "Index Keywords")
CORE_FOCUS_TYPES = {
    "human_programming_task",
    "programming_method_process",
    "programming_education_task",
}

TERM_PATTERNS: list[tuple[str, str, re.Pattern[str]]] = [
    (
        "computer_programming",
        "computer program*",
        re.compile(r"computer program(?:ming|s)?", re.IGNORECASE),
    ),
    ("source_code", "source code", re.compile(r"source code", re.IGNORECASE)),
    (
        "program_comprehension",
        "program comprehension",
        re.compile(r"program comprehension", re.IGNORECASE),
    ),
    (
        "code_comprehension",
        "code comprehension",
        re.compile(r"code comprehension", re.IGNORECASE),
    ),
    ("programmer", "programmer*", re.compile(r"\bprogrammers?\b", re.IGNORECASE)),
    (
        "software_developer",
        "software developer*",
        re.compile(r"software developers?", re.IGNORECASE),
    ),
    (
        "coding_task",
        "coding task*",
        re.compile(r"coding tasks?", re.IGNORECASE),
    ),
    (
        "programming_task",
        "programming task*",
        re.compile(r"programming tasks?", re.IGNORECASE),
    ),
    ("debugging", "debugging", re.compile(r"\bdebugging\b", re.IGNORECASE)),
    (
        "pair_programming",
        "pair programming",
        re.compile(r"pair programming", re.IGNORECASE),
    ),
    (
        "test_driven_development",
        "test-driven development",
        re.compile(r"test[- ]driven development", re.IGNORECASE),
    ),
    (
        "end_user_programming",
        "end-user programming",
        re.compile(r"end[- ]user programming", re.IGNORECASE),
    ),
    (
        "spreadsheet_programming",
        "spreadsheet programming/development/debugging/testing/error correction",
        re.compile(
            r"spreadsheet (?:programming|development|debugging|testing|error correction)",
            re.IGNORECASE,
        ),
    ),
    (
        "query_formulation",
        "query formulation",
        re.compile(r"query formulation", re.IGNORECASE),
    ),
    (
        "query_development",
        "query development",
        re.compile(r"query development", re.IGNORECASE),
    ),
    ("sql_query", "SQL query", re.compile(r"\bSQL quer(?:y|ies)\b", re.IGNORECASE)),
    (
        "data_model_instantiation",
        "instantiation(s) of data model(s)",
        re.compile(r"instantiations? of data models?", re.IGNORECASE),
    ),
    (
        "ai_assisted_programming",
        "AI-assisted programming/coding",
        re.compile(r"AI[- ]assisted (?:programming|coding)", re.IGNORECASE),
    ),
    (
        "coding_agent",
        "coding agent*",
        re.compile(r"coding agents?", re.IGNORECASE),
    ),
    (
        "programming_assistant",
        "programming assistant*",
        re.compile(r"programming assistants?", re.IGNORECASE),
    ),
    (
        "code_generation",
        "code generation",
        re.compile(r"code generation", re.IGNORECASE),
    ),
    (
        "code_review",
        "code review",
        re.compile(r"code review", re.IGNORECASE),
    ),
    (
        "code_inspection",
        "code inspection",
        re.compile(r"code inspection", re.IGNORECASE),
    ),
    (
        "code_modification",
        "code modification",
        re.compile(r"code modification", re.IGNORECASE),
    ),
    (
        "code_completion",
        "code completion/autocompletion/suggestion",
        re.compile(
            r"code completion|code auto[- ]?complet(?:e|ion)|code suggestions?",
            re.IGNORECASE,
        ),
    ),
    ("writing_code", "writing code", re.compile(r"writing code", re.IGNORECASE)),
    (
        "open_source_development",
        "open-source software development",
        re.compile(r"open[- ]source software development", re.IGNORECASE),
    ),
]

AIS_PROFESSIONAL_PATTERN = re.compile(
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
    r"code completion|code auto[- ]?complet(?:e|ion)|code suggestions?",
    re.IGNORECASE,
)

PROFESSIONAL_FAMILIES: list[tuple[str, str, re.Pattern[str]]] = [
    (
        "comprehension_modification",
        "program/software comprehension, understanding, modification",
        re.compile(
            r"(?:computer )?program comprehension|program understanding|"
            r"software comprehension|software modification",
            re.IGNORECASE,
        ),
    ),
    (
        "programming_task_performance",
        "programming task/performance/productivity/environment",
        re.compile(
            r"programming tasks?|programming performance|programmer performance|"
            r"programming productivity|programming environments?|program construction",
            re.IGNORECASE,
        ),
    ),
    (
        "maintenance",
        "program maintenance/maintainable software",
        re.compile(r"program maintenance|maintainable software", re.IGNORECASE),
    ),
    (
        "query_activity",
        "query formulation/development/reuse/complexity/query language",
        re.compile(
            r"query formulation|query development|query reuse|query complexity|"
            r"structured query languages?",
            re.IGNORECASE,
        ),
    ),
    ("plain_sql", "SQL", re.compile(r"\bSQL\b", re.IGNORECASE)),
    (
        "spreadsheet_activity",
        "spreadsheet errors/testing/development/debugging/programming",
        re.compile(
            r"spreadsheet (?:errors?|testing|development|debugging|programming|"
            r"error correction|code inspection|formulas?)",
            re.IGNORECASE,
        ),
    ),
    (
        "end_user_development",
        "end-user programming/computing/development",
        re.compile(
            r"end[- ]user (?:programming|computing|development)",
            re.IGNORECASE,
        ),
    ),
    (
        "pair_programming",
        "pair programming",
        re.compile(r"pair programming", re.IGNORECASE),
    ),
    (
        "test_driven_development",
        "test-driven development",
        re.compile(r"test[- ]driven development", re.IGNORECASE),
    ),
    (
        "inspection_review",
        "code inspection/review",
        re.compile(r"code inspection|code review", re.IGNORECASE),
    ),
    (
        "debugging_testing",
        "program/code debugging or software testing",
        re.compile(r"(?:program|code) debugging|software testing", re.IGNORECASE),
    ),
    (
        "development_representation",
        "knowledge-based systems development/database structure representation",
        re.compile(
            r"knowledge[- ]based systems? development|"
            r"database structure representation",
            re.IGNORECASE,
        ),
    ),
    (
        "modern_programming_agents",
        "AI-assisted programming/coding, coding agents/assistants, code completion",
        re.compile(
            r"AI[- ]assisted (?:programming|coding)|coding agents?|"
            r"programming agents?|(?:programming|coding|code) assistants?|"
            r"code completion|code auto[- ]?complet(?:e|ion)|code suggestions?",
            re.IGNORECASE,
        ),
    ),
]


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def read_jsonl(path: Path) -> list[dict]:
    rows: list[dict] = []
    with path.open("r", encoding="utf-8") as handle:
        for line in handle:
            if line.strip():
                rows.append(json.loads(line))
    return rows


def normalize_doi(value: str | None) -> str:
    return (value or "").strip().casefold()


def normalize_title(value: str | None) -> str:
    return re.sub(r"[^a-z0-9]+", "", (value or "").casefold())


def join_key(row: dict, *, metadata: bool = False) -> str:
    doi_field = "DOI" if metadata else "doi"
    title_field = "Title" if metadata else "title"
    doi = normalize_doi(row.get(doi_field))
    if doi:
        return f"doi:{doi}"
    return f"title:{normalize_title(row.get(title_field))}"


def as_bool(value: object) -> bool:
    if isinstance(value, bool):
        return value
    return str(value).strip().casefold() == "true"


def matched_terms(row: dict[str, str]) -> list[str]:
    text = " ".join((row.get(field) or "") for field in FIELDS)
    return [name for name, _, pattern in TERM_PATTERNS if pattern.search(text)]


def evidence_stage(
    first: dict | None,
    direct: dict[str, str] | None,
) -> str:
    if direct and as_bool(direct.get("is_direct_programming_research")):
        if (direct.get("direct_focus_type") or "") in CORE_FOCUS_TYPES:
            return "core_20"
        return "direct_boundary_8"
    if direct:
        return "broad_context_not_direct"
    if first:
        if as_bool(first.get("is_programming_context")):
            return "broad_context_not_direct"
        return "fulltext_screen_false"
    return "no_fulltext_screen_record"


def write_csv(path: Path, rows: list[dict], fields: list[str]) -> None:
    with path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    metadata = read_csv(METADATA_CSV)
    first_rows = read_jsonl(FIRST_PASS_JSONL)
    direct_rows = read_csv(DIRECT_DECISIONS_CSV)

    first_by_key = {join_key(row): row for row in first_rows}
    direct_by_key = {join_key(row): row for row in direct_rows}

    def enrich_metadata_row(row: dict[str, str], terms: list[str]) -> dict:
        key = join_key(row, metadata=True)
        first = first_by_key.get(key)
        direct = direct_by_key.get(key)
        stage = evidence_stage(first, direct)
        return {
            "key": key,
            "eid": row.get("EID") or "",
            "doi": row.get("DOI") or "",
            "title": row.get("Title") or "",
            "year": row.get("Year") or "",
            "journal": row.get("Source title") or "",
            "author_keywords": row.get("Author Keywords") or "",
            "index_keywords": row.get("Index Keywords") or "",
            "matched_terms": "; ".join(terms),
            "evidence_stage": stage,
            "is_programming_context": (
                str(first.get("is_programming_context")) if first else ""
            ),
            "is_direct_programming_research": (
                direct.get("is_direct_programming_research") if direct else ""
            ),
            "direct_focus_type": direct.get("direct_focus_type") if direct else "",
            "has_human_programming_task": (
                direct.get("has_human_programming_task") if direct else ""
            ),
            "exclusion_or_decision_reason": (
                (direct.get("decision_reason_cn") or "")
                if direct
                else ((first or {}).get("exclusion_reason_cn") or "")
            ),
        }

    candidate_rows: list[dict] = []
    for row in metadata:
        terms = matched_terms(row)
        if not terms:
            continue
        candidate_rows.append(enrich_metadata_row(row, terms))

    # Keep Scopus records distinct by EID; fall back to DOI/title when EID is absent.
    deduped: dict[str, dict] = {}
    for row in candidate_rows:
        record_key = row["eid"] or row["key"]
        deduped.setdefault(record_key, row)
    candidates = list(deduped.values())

    stage_counts = Counter(row["evidence_stage"] for row in candidates)
    year_counts = Counter(row["year"] for row in candidates)
    journal_counts = Counter(row["journal"] for row in candidates)

    term_stats: list[dict] = []
    for name, display, _ in TERM_PATTERNS:
        hits = [row for row in candidates if name in row["matched_terms"].split("; ")]
        core_hits = [row for row in hits if row["evidence_stage"] == "core_20"]
        direct_hits = [
            row
            for row in hits
            if row["evidence_stage"] in {"core_20", "direct_boundary_8"}
        ]
        broad_hits = [
            row
            for row in hits
            if row["evidence_stage"]
            in {"core_20", "direct_boundary_8", "broad_context_not_direct"}
        ]
        term_stats.append(
            {
                "term_id": name,
                "display": display,
                "candidate_hits": len(hits),
                "broad_context_hits": len(broad_hits),
                "direct_28_hits": len(direct_hits),
                "core_20_hits": len(core_hits),
                "core_20_recall": len(core_hits) / 20,
                "candidate_core_yield": len(core_hits) / len(hits) if hits else None,
                "core_titles": [row["title"] for row in core_hits],
            }
        )

    core_direct = [
        row
        for row in direct_rows
        if as_bool(row.get("is_direct_programming_research"))
        and (row.get("direct_focus_type") or "") in CORE_FOCUS_TYPES
    ]
    core_metadata_rows: list[dict] = []
    metadata_by_key = {join_key(row, metadata=True): row for row in metadata}
    for direct in sorted(core_direct, key=lambda row: int(row.get("year") or 0), reverse=True):
        md = metadata_by_key.get(join_key(direct))
        terms = matched_terms(md) if md else []
        core_metadata_rows.append(
            {
                "year": direct.get("year") or "",
                "title": direct.get("title") or "",
                "journal": direct.get("journal") or "",
                "doi": direct.get("doi") or "",
                "direct_focus_type": direct.get("direct_focus_type") or "",
                "matched_terms": "; ".join(terms),
                "author_keywords": (md or {}).get("Author Keywords") or "",
                "index_keywords": (md or {}).get("Index Keywords") or "",
                "abstract": (md or {}).get("Abstract") or "",
            }
        )

    recent = sorted(
        [row for row in candidates if int(row["year"] or 0) >= 2016],
        key=lambda row: (int(row["year"] or 0), row["title"]),
        reverse=True,
    )

    candidate_fields = [
        "eid",
        "doi",
        "title",
        "year",
        "journal",
        "matched_terms",
        "evidence_stage",
        "is_programming_context",
        "is_direct_programming_research",
        "direct_focus_type",
        "has_human_programming_task",
        "author_keywords",
        "index_keywords",
        "exclusion_or_decision_reason",
    ]
    write_csv(CANDIDATES_CSV, candidates, candidate_fields)
    write_csv(RECENT_CSV, recent, candidate_fields)
    write_csv(
        CORE_TERMS_CSV,
        core_metadata_rows,
        [
            "year",
            "title",
            "journal",
            "doi",
            "direct_focus_type",
            "matched_terms",
            "author_keywords",
            "index_keywords",
            "abstract",
        ],
    )

    professional_rows = [
        enrich_metadata_row(row, ["ais_professional_vocabulary"])
        for row in metadata
        if AIS_PROFESSIONAL_PATTERN.search(
            " ".join((row.get(field) or "") for field in FIELDS)
        )
    ]
    professional_deduped: dict[str, dict] = {}
    for row in professional_rows:
        record_key = row["eid"] or row["key"]
        professional_deduped.setdefault(record_key, row)
    professional_candidates = list(professional_deduped.values())
    write_csv(
        PROFESSIONAL_CANDIDATES_CSV,
        professional_candidates,
        candidate_fields,
    )
    professional_stage_counts = Counter(
        row["evidence_stage"] for row in professional_candidates
    )
    professional_family_stats: list[dict] = []
    for family_id, display, pattern in PROFESSIONAL_FAMILIES:
        family_rows = [
            enrich_metadata_row(row, [family_id])
            for row in metadata
            if pattern.search(" ".join((row.get(field) or "") for field in FIELDS))
        ]
        family_deduped: dict[str, dict] = {}
        for row in family_rows:
            record_key = row["eid"] or row["key"]
            family_deduped.setdefault(record_key, row)
        family_candidates = list(family_deduped.values())
        family_stage_counts = Counter(
            row["evidence_stage"] for row in family_candidates
        )
        professional_family_stats.append(
            {
                "family_id": family_id,
                "display": display,
                "candidate_hits": len(family_candidates),
                "stage_counts": dict(family_stage_counts),
                "core_20_hits": family_stage_counts.get("core_20", 0),
                "core_20_recall": family_stage_counts.get("core_20", 0) / 20,
                "candidate_core_yield": (
                    family_stage_counts.get("core_20", 0) / len(family_candidates)
                    if family_candidates
                    else None
                ),
                "core_titles": [
                    row["title"]
                    for row in family_candidates
                    if row["evidence_stage"] == "core_20"
                ],
            }
        )

    summary = {
        "basket_metadata_records": len(metadata),
        "raw_query_hits": len(candidate_rows),
        "deduplicated_query_hits": len(candidates),
        "query_definition": "S3 expanded direct activity + open-source software development + code completion",
        "stage_counts": dict(stage_counts),
        "stage_percentages": {
            key: value / len(candidates) for key, value in stage_counts.items()
        },
        "recent_counts": {
            "2016+": len(recent),
            "2021+": sum(int(row["year"] or 0) >= 2021 for row in candidates),
            "core_20_2016+": sum(
                row["evidence_stage"] == "core_20" and int(row["year"] or 0) >= 2016
                for row in candidates
            ),
            "core_20_2021+": sum(
                row["evidence_stage"] == "core_20" and int(row["year"] or 0) >= 2021
                for row in candidates
            ),
        },
        "year_counts": dict(sorted(year_counts.items(), reverse=True)),
        "top_journals": journal_counts.most_common(20),
        "term_stats": term_stats,
        "professional_vocabulary_variant": {
            "raw_hits": len(professional_rows),
            "deduplicated_hits": len(professional_candidates),
            "stage_counts": dict(professional_stage_counts),
            "stage_percentages": {
                key: value / len(professional_candidates)
                for key, value in professional_stage_counts.items()
            },
            "recent_counts": {
                "2016+": sum(
                    int(row["year"] or 0) >= 2016 for row in professional_candidates
                ),
                "2021+": sum(
                    int(row["year"] or 0) >= 2021 for row in professional_candidates
                ),
                "core_20_2016+": sum(
                    row["evidence_stage"] == "core_20"
                    and int(row["year"] or 0) >= 2016
                    for row in professional_candidates
                ),
                "core_20_2021+": sum(
                    row["evidence_stage"] == "core_20"
                    and int(row["year"] or 0) >= 2021
                    for row in professional_candidates
                ),
            },
            "family_stats": professional_family_stats,
        },
        "core_20_records": core_metadata_rows,
        "recent_records": recent,
    }
    SUMMARY_JSON.write_text(
        json.dumps(summary, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(
        json.dumps(
            {
                "raw_query_hits": len(candidate_rows),
                "deduplicated_query_hits": len(candidates),
                "stage_counts": dict(stage_counts),
                "recent_counts": summary["recent_counts"],
                "professional_vocabulary_variant": summary[
                    "professional_vocabulary_variant"
                ],
                "top_terms": sorted(
                    term_stats,
                    key=lambda item: (
                        item["core_20_hits"],
                        item["candidate_core_yield"] or 0,
                    ),
                    reverse=True,
                )[:12],
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
