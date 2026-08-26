#!/usr/bin/env python3
"""Audit how AIS Basket literature reviews construct their search corpora."""

from __future__ import annotations

import builtins
import collections
import importlib.util
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


RUN_DIR = Path(__file__).resolve().parent
ENGINE_PATH = (
    RUN_DIR.parent
    / "new_construct_objective_measurement_deepseek_analysis"
    / "analyze_fulltext.py"
)
SPEC = importlib.util.spec_from_file_location("review_search_batch_engine", ENGINE_PATH)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError(f"Cannot load shared batch engine from {ENGINE_PATH}")
ENGINE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = ENGINE
SPEC.loader.exec_module(ENGINE)

STRATEGY_TYPES = {
    "broad_database",
    "bounded_authoritative_set",
    "hybrid",
    "citation_only",
    "unspecified",
    "not_review",
}
SOURCE_TYPES = {
    "bibliographic_database",
    "publisher_platform",
    "digital_library",
    "search_engine",
    "journal_set",
    "journal",
    "conference_set",
    "conference",
    "citation_chaining",
    "other",
}
SOURCE_ROLES = {
    "primary_search",
    "supplementary_search",
    "bounded_scope",
    "validation",
    "unclear",
}
SET_TYPES = {"journal_set", "conference_set", "other"}

SOURCE_ALIASES = {
    "ebsco": ("EBSCO", "bibliographic_database"),
    "ebscohost": ("EBSCO", "bibliographic_database"),
    "abi/inform": ("ABI/INFORM", "bibliographic_database"),
    "abi-inform": ("ABI/INFORM", "bibliographic_database"),
    "web of science": ("Web of Science", "bibliographic_database"),
    "wos": ("Web of Science", "bibliographic_database"),
    "scopus": ("Scopus", "bibliographic_database"),
    "business source complete": ("Business Source Complete", "bibliographic_database"),
    "business source premier": ("Business Source Premier", "bibliographic_database"),
    "ebsco business source premier": (
        "Business Source Premier",
        "bibliographic_database",
    ),
    "business source premier": ("Business Source Premier", "bibliographic_database"),
    "proquest": ("ProQuest", "bibliographic_database"),
    "proquest dissertations & theses": (
        "ProQuest Dissertations & Theses",
        "bibliographic_database",
    ),
    "psycinfo": ("PsycINFO", "bibliographic_database"),
    "psyinfo": ("PsycINFO", "bibliographic_database"),
    "science direct": ("ScienceDirect", "publisher_platform"),
    "sciencedirect": ("ScienceDirect", "publisher_platform"),
    "wiley-blackwell pilot 2015": ("Wiley Online Library", "publisher_platform"),
    "wiley online library": ("Wiley Online Library", "publisher_platform"),
    "springerlink": ("SpringerLink", "publisher_platform"),
    "emerald": ("Emerald Insight", "publisher_platform"),
    "emerald insight": ("Emerald Insight", "publisher_platform"),
    "ais electronic library": ("AIS eLibrary", "digital_library"),
    "ais electronic library (ais elibrary)": ("AIS eLibrary", "digital_library"),
    "ais elibrary": ("AIS eLibrary", "digital_library"),
    "aisel": ("AIS eLibrary", "digital_library"),
    "acm digital library": ("ACM Digital Library", "digital_library"),
    "ieee xplore": ("IEEE Xplore", "digital_library"),
    "ieee xplore digital library": ("IEEE Xplore", "digital_library"),
    "jstor": ("JSTOR", "digital_library"),
    "google scholar": ("Google Scholar", "search_engine"),
}


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def clean_text(value: Any) -> str:
    return str(value or "").strip()


def clean_string_list(value: Any) -> list[str]:
    values = value if isinstance(value, list) else []
    output: list[str] = []
    for item in values:
        text = clean_text(item)
        if text and text not in output:
            output.append(text)
    return output


def clean_optional_int(value: Any) -> int | None:
    if value is None or value == "":
        return None
    try:
        return int(value)
    except (TypeError, ValueError):
        return None


def clean_optional_bool(value: Any) -> bool | None:
    return value if isinstance(value, bool) else None


def normalize_sources(value: Any) -> list[dict[str, str]]:
    values = value if isinstance(value, list) else []
    output: list[dict[str, str]] = []
    seen: set[tuple[str, str, str]] = set()
    for item in values:
        if not isinstance(item, dict):
            continue
        name = clean_text(item.get("name"))
        normalized_name = clean_text(item.get("normalized_name")) or name
        source_type = clean_text(item.get("source_type"))
        role = clean_text(item.get("role"))
        alias = SOURCE_ALIASES.get(normalized_name.casefold()) or SOURCE_ALIASES.get(
            name.casefold()
        )
        if alias is not None:
            normalized_name, source_type = alias
        normalized_key = normalized_name.casefold()
        if normalized_key.startswith("web of science"):
            normalized_name, source_type = "Web of Science", "bibliographic_database"
        elif "abi/inform" in normalized_key or "ab/inform" in normalized_key:
            normalized_name, source_type = "ABI/INFORM", "bibliographic_database"
        elif "proquest dissertation" in normalized_key:
            normalized_name, source_type = (
                "ProQuest Dissertations & Theses",
                "bibliographic_database",
            )
        elif "worldcat dissertation" in normalized_key:
            normalized_name, source_type = (
                "WorldCat Dissertations & Theses",
                "bibliographic_database",
            )
        elif (
            source_type == "citation_chaining"
            or "citation chain" in normalized_key
            or "citation search" in normalized_key
            or "citation track" in normalized_key
            or "reference search" in normalized_key
            or "reference tracing" in normalized_key
            or "snowball" in normalized_key
        ):
            normalized_name, source_type = "Citation chaining", "citation_chaining"
        if not name or source_type not in SOURCE_TYPES:
            continue
        if role not in SOURCE_ROLES:
            role = "unclear"
        key = (normalized_name.casefold(), source_type, role)
        if key in seen:
            continue
        seen.add(key)
        output.append(
            {
                "name": name,
                "normalized_name": normalized_name,
                "source_type": source_type,
                "role": role,
                "evidence": clean_text(item.get("evidence")),
            }
        )
    return output


def normalize_sets(value: Any) -> list[dict[str, Any]]:
    values = value if isinstance(value, list) else []
    output: list[dict[str, Any]] = []
    seen: set[str] = set()
    for item in values:
        if not isinstance(item, dict):
            continue
        name = clean_text(item.get("name"))
        set_type = clean_text(item.get("set_type"))
        if not name:
            continue
        name_key = name.casefold()
        if "basket" in name_key or "senior scholars" in name_key:
            name = (
                "AIS Senior Scholars' Basket + DSS"
                if "decision support systems" in name_key or "plus dss" in name_key
                else "AIS Senior Scholars' Basket"
            )
            set_type = "journal_set"
        elif (
            "is conference proceedings" in name_key
            or "ais conferences" in name_key
            or all(acronym in name_key for acronym in ("icis", "ecis", "amcis"))
        ):
            name = "Major AIS conference proceedings"
            set_type = "conference_set"
        elif "four cs hci journals" in name_key:
            name = "Four core CS/HCI journals"
            set_type = "journal_set"
        elif "conference" in name_key:
            set_type = "conference_set"
        if set_type not in SET_TYPES:
            set_type = "other"
        key = name.casefold()
        if key in seen:
            continue
        seen.add(key)
        output.append(
            {
                "name": name,
                "set_type": set_type,
                "members": clean_string_list(item.get("members")),
                "evidence": clean_text(item.get("evidence")),
            }
        )
    return output


def normalize_final(payload: dict[str, Any]) -> dict[str, Any]:
    is_review = payload.get("is_literature_review") is True
    strategy = clean_text(payload.get("search_strategy_type"))
    if not is_review:
        strategy = "not_review"
    elif strategy not in STRATEGY_TYPES - {"not_review"}:
        strategy = "unspecified"
    sources = normalize_sources(payload.get("search_sources")) if is_review else []
    sets = normalize_sets(payload.get("authoritative_sets")) if is_review else []
    try:
        confidence = float(payload.get("confidence", 0.0))
    except (TypeError, ValueError):
        confidence = 0.0
    return {
        "is_literature_review": is_review,
        "review_type": clean_text(payload.get("review_type")) if is_review else "",
        "review_objective_cn": (
            clean_text(payload.get("review_objective_cn")) if is_review else ""
        ),
        "search_strategy_type": strategy,
        "search_sources": sources,
        "authoritative_sets": sets,
        "search_query_terms": (
            clean_string_list(payload.get("search_query_terms")) if is_review else []
        ),
        "publication_year_from": (
            clean_optional_int(payload.get("publication_year_from")) if is_review else None
        ),
        "publication_year_to": (
            clean_optional_int(payload.get("publication_year_to")) if is_review else None
        ),
        "initial_records": (
            clean_optional_int(payload.get("initial_records")) if is_review else None
        ),
        "included_studies": (
            clean_optional_int(payload.get("included_studies")) if is_review else None
        ),
        "backward_search": (
            clean_optional_bool(payload.get("backward_search")) if is_review else None
        ),
        "forward_search": (
            clean_optional_bool(payload.get("forward_search")) if is_review else None
        ),
        "hand_search": (
            clean_optional_bool(payload.get("hand_search")) if is_review else None
        ),
        "method_summary_cn": (
            clean_text(payload.get("method_summary_cn")) if is_review else ""
        ),
        "limitations_cn": clean_text(payload.get("limitations_cn")),
        "confidence": max(0.0, min(1.0, confidence)),
        # Compatibility aliases used by the shared engine's progress printer.
        "claims_new_construct_development": is_review,
        "objective_measurement_of_new_construct": bool(sources),
        "new_construct_with_objective_measurement": bool(sources),
    }


def write_jsonl_atomic(path: Path, rows: list[dict[str, Any]]) -> None:
    temp = path.with_suffix(path.suffix + ".tmp")
    with temp.open("w", encoding="utf-8", newline="\n") as handle:
        for row in rows:
            handle.write(json.dumps(row, ensure_ascii=False) + "\n")
    os.replace(temp, path)


def write_reports(
    output_dir: Path,
    all_files: list[Path],
    decisions: dict[str, dict[str, Any]],
    analysis_version: str,
    fingerprint: str,
) -> None:
    values = []
    for original in decisions.values():
        row = dict(original)
        row["search_sources"] = normalize_sources(row.get("search_sources"))
        row["authoritative_sets"] = normalize_sets(row.get("authoritative_sets"))
        values.append(row)
    values.sort(key=lambda row: str(row.get("source_file") or ""))
    formal_reviews = [row for row in values if row.get("is_literature_review") is True]
    write_jsonl_atomic(output_dir / "formal_reviews.jsonl", formal_reviews)

    source_counts: collections.Counter[tuple[str, str]] = collections.Counter()
    role_counts: collections.Counter[str] = collections.Counter()
    set_counts: collections.Counter[tuple[str, str]] = collections.Counter()
    for row in formal_reviews:
        seen_sources: set[tuple[str, str]] = set()
        for source in row.get("search_sources") or []:
            key = (
                clean_text(source.get("normalized_name")),
                clean_text(source.get("source_type")),
            )
            if key[0] and key not in seen_sources:
                source_counts[key] += 1
                seen_sources.add(key)
            role_counts[clean_text(source.get("role"))] += 1
        seen_sets: set[tuple[str, str]] = set()
        for item in row.get("authoritative_sets") or []:
            key = (clean_text(item.get("name")), clean_text(item.get("set_type")))
            if key[0] and key not in seen_sets:
                set_counts[key] += 1
                seen_sets.add(key)

    completed_names = {path.name for path in all_files} & set(decisions)
    summary = {
        "updated_at": utc_now(),
        "analysis_version": analysis_version,
        "prompt_fingerprint": fingerprint,
        "input_fulltext_files": len(all_files),
        "completed": len(completed_names),
        "pending": len(all_files) - len(completed_names),
        "formal_reviews": len(formal_reviews),
        "strategy_counts": {
            strategy: sum(
                row.get("search_strategy_type") == strategy for row in formal_reviews
            )
            for strategy in sorted(STRATEGY_TYPES - {"not_review"})
        },
        "workflow_counts": {
            key: sum(row.get(key) is True for row in formal_reviews)
            for key in ("backward_search", "forward_search", "hand_search")
        },
        "search_source_document_counts": [
            {"normalized_name": name, "source_type": source_type, "documents": count}
            for (name, source_type), count in source_counts.most_common()
        ],
        "search_source_role_mentions": dict(role_counts.most_common()),
        "authoritative_set_document_counts": [
            {"name": name, "set_type": set_type, "documents": count}
            for (name, set_type), count in set_counts.most_common()
        ],
        "usage": {
            key: sum(int((row.get("usage") or {}).get(key, 0)) for row in values)
            for key in ("prompt_tokens", "completion_tokens", "total_tokens")
        },
    }
    temp_summary = output_dir / "summary.json.tmp"
    temp_summary.write_text(
        json.dumps(summary, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    os.replace(temp_summary, output_dir / "summary.json")


def main() -> int:
    def task_print(*args: Any, **kwargs: Any) -> None:
        if args and isinstance(args[0], str):
            first = (
                args[0]
                .replace("new_construct=", "is_review=")
                .replace("objective=", "sources_found=")
                .replace("target_match=", "sources_found=")
            )
            args = (first, *args[1:])
        builtins.print(*args, **kwargs)

    ENGINE.RUN_DIR = RUN_DIR
    ENGINE.CONFIG_PATH = RUN_DIR / "config.json"
    ENGINE.normalize_final = normalize_final
    ENGINE.write_reports = write_reports
    ENGINE.print = task_print
    return int(ENGINE.main())


if __name__ == "__main__":
    sys.exit(main())
