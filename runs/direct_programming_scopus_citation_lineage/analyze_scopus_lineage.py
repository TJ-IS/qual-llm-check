#!/usr/bin/env python3
"""Reproducible descriptive analysis of the 20-seed Scopus citation export."""

from __future__ import annotations

import csv
import json
import re
from collections import Counter, defaultdict
from pathlib import Path


HERE = Path(__file__).resolve().parent
RAW_CSV = HERE / "scopus_citing_20_seed_807_raw.csv"
SEED_CSV = HERE / "seed_articles.csv"
OUTPUT_JSON = HERE / "analysis_summary.json"

TEXT_FIELDS = ("Title", "Abstract", "Author Keywords", "Index Keywords")

THEMES = {
    "program_comprehension_and_cognition": (
        r"program comprehension|code comprehension|software comprehension|"
        r"cognitive fit|mental model|eye[- ]?track|visuali[sz]ation|"
        r"problem representation|domain knowledge|debugg"
    ),
    "spreadsheet_and_end_user_programming": (
        r"spreadsheet|microsoft excel|\bexcel\b|end[- ]user (?:comput|develop|program)"
    ),
    "query_database_and_conceptual_modeling": (
        r"\bsql\b|query formul|query develop|database|data model|"
        r"conceptual model|ontology|semantic model"
    ),
    "pair_agile_testing_and_quality": (
        r"pair[- ]?program|test[- ]driven|\btdd\b|agile|software test|"
        r"code inspection|fault locali[sz]ation|software quality"
    ),
    "general_software_engineering": (
        r"software engineer|software develop|computer program|programming|"
        r"programmer|source code|software design"
    ),
}

AI_RE = re.compile(
    r"large language model|\bllms?\b|chatgpt|copilot|codex|codegen|incoder|"
    r"generative (?:ai|artificial intelligence)|neural (?:language )?model",
    re.IGNORECASE,
)
PROGRAMMING_CONTEXT_RE = re.compile(
    r"program(?:ming|mer| comprehension)?|\bcod(?:e|ing)\b|software develop|"
    r"developer|query formul|spreadsheet|requirements engineering",
    re.IGNORECASE,
)

AIS_CONFERENCE_RE = re.compile(
    r"\b(?:ICIS|AMCIS|ECIS|PACIS|ACIS)\b|"
    r"Australasian Conference on Information Systems|"
    r"Pacific Asia Conference on Information Systems|"
    r"European Conference on Information Systems|"
    r"Americas Conference on Information Systems",
    re.IGNORECASE,
)

AIS_BASKET_11_SOURCES = {
    "Decision Support Systems",
    "Information and Management",
    "Information & Management",
    "MIS Quarterly: Management Information Systems",
    "Journal of Management Information Systems",
    "Information Systems Research",
    "European Journal of Information Systems",
    "Journal of Information Technology",
    "Information Systems Journal",
    "Journal of the Association for Information Systems",
    "Journal of Strategic Information Systems",
    "Information and Organization",
}


def load_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def normalize_title(value: str) -> str:
    return re.sub(r"\W+", " ", (value or "").casefold()).strip()


def split_keywords(value: str) -> list[str]:
    return [item.strip() for item in (value or "").split(";") if item.strip()]


def integer(value: str) -> int:
    try:
        return int(value)
    except (TypeError, ValueError):
        return 0


def compact_record(row: dict[str, str]) -> dict[str, object]:
    return {
        "title": row["Title"],
        "year": integer(row["Year"]),
        "source": row["Source title"],
        "document_type": row["Document Type"],
        "cited_by": integer(row["Cited by"]),
        "doi": row["DOI"],
        "eid": row["EID"],
        "abstract": row["Abstract"],
    }


def is_ais_branded(row: dict[str, str]) -> bool:
    venue_text = f"{row['Source title']} {row['Conference name']}"
    return (
        row["Publisher"].strip() == "Association for Information Systems"
        or AIS_CONFERENCE_RE.search(venue_text) is not None
    )


def main() -> None:
    rows = load_csv(RAW_CSV)
    seeds = load_csv(SEED_CSV)
    if len(rows) != 807:
        raise ValueError(f"Expected 807 Scopus rows, found {len(rows)}")

    eids = [row["EID"] for row in rows]
    if any(not eid for eid in eids) or len(set(eids)) != len(eids):
        raise ValueError("EIDs must be present and unique")

    title_groups: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        title_groups[normalize_title(row["Title"])].append(row)
    duplicate_groups = [
        [compact_record(row) for row in group]
        for group in title_groups.values()
        if len(group) > 1
    ]
    seed_eids = {row["eid"] for row in seeds}
    seed_records_in_export = [
        compact_record(row) for row in rows if row["EID"] in seed_eids
    ]
    external_rows = [row for row in rows if row["EID"] not in seed_eids]

    years = Counter(integer(row["Year"]) for row in rows)
    periods = {
        "2021+": sum(count for year, count in years.items() if year >= 2021),
        "2016-2020": sum(count for year, count in years.items() if 2016 <= year <= 2020),
        "2006-2015": sum(count for year, count in years.items() if 2006 <= year <= 2015),
        "<=2005": sum(count for year, count in years.items() if year <= 2005),
    }
    external_years = Counter(integer(row["Year"]) for row in external_rows)
    external_periods = {
        "2021+": sum(count for year, count in external_years.items() if year >= 2021),
        "2016-2020": sum(
            count for year, count in external_years.items() if 2016 <= year <= 2020
        ),
        "2006-2015": sum(
            count for year, count in external_years.items() if 2006 <= year <= 2015
        ),
        "<=2005": sum(count for year, count in external_years.items() if year <= 2005),
    }
    sources = Counter(row["Source title"] for row in rows)
    document_types = Counter(row["Document Type"] for row in rows)
    strict_ais_eids = {
        row["EID"]
        for row in rows
        if row["Publisher"].strip() == "Association for Information Systems"
    }
    expanded_ais_eids = {row["EID"] for row in rows if is_ais_branded(row)}
    basket_11_eids = {
        row["EID"] for row in rows if row["Source title"] in AIS_BASKET_11_SOURCES
    }
    ais_basket_union = expanded_ais_eids | basket_11_eids
    ais_document_types = Counter(
        row["Document Type"] for row in rows if row["EID"] in expanded_ais_eids
    )
    basket_sources = Counter(
        row["Source title"] for row in rows if row["EID"] in basket_11_eids
    )
    author_keywords = Counter()
    index_keywords = Counter()
    for row in rows:
        author_keywords.update(keyword.casefold() for keyword in split_keywords(row["Author Keywords"]))
        index_keywords.update(keyword.casefold() for keyword in split_keywords(row["Index Keywords"]))

    theme_records: dict[str, list[dict[str, object]]] = {}
    theme_period_counts: dict[str, dict[str, int]] = {}
    for theme, pattern in THEMES.items():
        matcher = re.compile(pattern, re.IGNORECASE)
        matching = []
        for row in rows:
            text = " ".join(row.get(field, "") or "" for field in TEXT_FIELDS)
            if matcher.search(text):
                matching.append(compact_record(row))
        theme_records[theme] = matching
        matching_years = Counter(int(item["year"]) for item in matching)
        theme_period_counts[theme] = {
            "2021+": sum(count for year, count in matching_years.items() if year >= 2021),
            "2016-2020": sum(
                count for year, count in matching_years.items() if 2016 <= year <= 2020
            ),
            "2006-2015": sum(
                count for year, count in matching_years.items() if 2006 <= year <= 2015
            ),
            "<=2005": sum(count for year, count in matching_years.items() if year <= 2005),
        }

    modern_ai = []
    for row in rows:
        text = " ".join(row.get(field, "") or "" for field in TEXT_FIELDS)
        if integer(row["Year"]) >= 2020 and AI_RE.search(text) and PROGRAMMING_CONTEXT_RE.search(text):
            modern_ai.append(compact_record(row))
    modern_ai.sort(key=lambda item: (-int(item["year"]), -int(item["cited_by"]), str(item["title"])))

    top_cited = sorted(
        (compact_record(row) for row in rows),
        key=lambda item: (-int(item["cited_by"]), -int(item["year"]), str(item["title"])),
    )[:30]

    seed_citations = [
        {
            "seed_id": integer(row["seed_id"]),
            "title": row["title"],
            "year": integer(row["year"]),
            "eid": row["eid"],
            "cited_by_local": integer(row["scopus_cited_by_local"]),
            "theme": row["theme"],
        }
        for row in seeds
    ]
    seed_citations.sort(key=lambda item: -int(item["cited_by_local"]))

    output = {
        "validation": {
            "scopus_records": len(rows),
            "unique_eids": len(set(eids)),
            "unique_dois": len({row["DOI"].casefold() for row in rows if row["DOI"]}),
            "missing_dois": sum(not row["DOI"] for row in rows),
            "unique_normalized_titles": len(title_groups),
            "duplicate_title_groups": len(duplicate_groups),
            "duplicate_title_extra_records": sum(len(group) - 1 for group in duplicate_groups),
            "seed_records_in_export": len(seed_records_in_export),
            "external_citing_records": len(rows) - len(seed_records_in_export),
            "year_min": min(years),
            "year_max": max(years),
        },
        "year_counts": dict(sorted(years.items(), reverse=True)),
        "period_counts": periods,
        "external_citing_period_counts": external_periods,
        "document_types": dict(document_types.most_common()),
        "venue_ecosystems": {
            "strict_association_for_information_systems_publisher": len(strict_ais_eids),
            "expanded_ais_branded_journals_and_conferences": len(expanded_ais_eids),
            "ais_basket_11": len(basket_11_eids),
            "expanded_ais_and_basket_overlap": len(expanded_ais_eids & basket_11_eids),
            "expanded_ais_or_basket_union": len(ais_basket_union),
            "outside_expanded_ais_and_basket": len(rows) - len(ais_basket_union),
            "expanded_ais_document_types": dict(ais_document_types.most_common()),
            "basket_11_sources": dict(basket_sources.most_common()),
            "distinct_source_titles": len(sources),
            "top_10_source_records": sum(count for _, count in sources.most_common(10)),
            "top_20_source_records": sum(count for _, count in sources.most_common(20)),
        },
        "top_sources": sources.most_common(30),
        "top_author_keywords": author_keywords.most_common(40),
        "top_index_keywords": index_keywords.most_common(40),
        "theme_counts_overlapping": {key: len(value) for key, value in theme_records.items()},
        "theme_period_counts_overlapping": theme_period_counts,
        "theme_records": theme_records,
        "modern_ai_candidates": modern_ai,
        "top_cited_records": top_cited,
        "duplicate_title_groups_detail": duplicate_groups,
        "seed_records_in_export_detail": seed_records_in_export,
        "seed_citations_local_snapshot": seed_citations,
        "seed_citation_sum_not_deduplicated": sum(
            int(item["cited_by_local"]) for item in seed_citations
        ),
    }
    OUTPUT_JSON.write_text(
        json.dumps(output, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    print(f"Wrote {OUTPUT_JSON}")
    print(json.dumps(output["validation"], ensure_ascii=False, indent=2))
    print("Periods:", periods)
    print("Overlapping theme counts:", output["theme_counts_overlapping"])
    print("Modern AI candidates:", len(modern_ai))


if __name__ == "__main__":
    main()
