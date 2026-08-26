#!/usr/bin/env python3
"""Screen Otero full texts for objectively measured higher-order constructs."""

from __future__ import annotations

import csv
import builtins
import importlib.util
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


RUN_DIR = Path(__file__).resolve().parent
ENGINE_PATH = RUN_DIR.parent / "new_construct_objective_measurement_deepseek_analysis" / "analyze_fulltext.py"
SPEC = importlib.util.spec_from_file_location("objective_construct_batch_engine", ENGINE_PATH)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError(f"Cannot load shared batch engine from {ENGINE_PATH}")
ENGINE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = ENGINE
SPEC.loader.exec_module(ENGINE)


OUTCOME_VALUES = {
    "target_match",
    "no_explicit_construct",
    "no_multidimensional_construct",
    "components_not_all_objective",
    "components_not_aggregated",
    "aggregation_not_same_construct",
    "unclear",
}


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def normalize_final(payload: dict[str, Any]) -> dict[str, Any]:
    boolean_fields = (
        "has_explicit_named_construct",
        "has_multidimensional_construct_candidate",
        "has_all_objective_component_measurement_candidate",
        "has_aggregation_to_construct_value_candidate",
        "objective_higher_order_construct_match",
    )
    normalized: dict[str, Any] = {}
    for field in boolean_fields:
        value = payload.get(field)
        if not isinstance(value, bool):
            raise ValueError(f"{field} must be boolean")
        normalized[field] = value

    outcome = str(payload.get("screening_outcome") or "").strip()
    if outcome not in OUTCOME_VALUES:
        raise ValueError(f"invalid screening_outcome: {outcome!r}")
    candidates = payload.get("construct_candidates")
    if not isinstance(candidates, list):
        candidates = []
    try:
        confidence = float(payload.get("confidence", 0.0))
    except (TypeError, ValueError):
        confidence = 0.0
    return {
        **normalized,
        "construct_candidates": candidates,
        "screening_outcome": outcome,
        "match_summary_cn": str(payload.get("match_summary_cn") or "").strip(),
        "confidence": max(0.0, min(1.0, confidence)),
        "limitations_cn": str(payload.get("limitations_cn") or "").strip(),
        # The shared engine's progress line still reads its three legacy flag
        # names. These aliases affect display only; the task-specific report
        # uses the fields above.
        "claims_new_construct_development": normalized["has_explicit_named_construct"],
        "objective_measurement_of_new_construct": normalized[
            "has_all_objective_component_measurement_candidate"
        ],
        "new_construct_with_objective_measurement": normalized[
            "objective_higher_order_construct_match"
        ],
    }


def write_reports(
    output_dir: Path,
    all_files: list[Path],
    decisions: dict[str, dict[str, Any]],
    analysis_version: str,
    fingerprint: str,
) -> None:
    csv_path = output_dir / "decisions.csv"
    temp_csv = csv_path.with_suffix(".csv.tmp")
    fields = [
        "source_file",
        "article_id",
        "title",
        "year",
        "journal",
        "doi",
        "analysis_version",
        "has_explicit_named_construct",
        "has_multidimensional_construct_candidate",
        "has_all_objective_component_measurement_candidate",
        "has_aggregation_to_construct_value_candidate",
        "objective_higher_order_construct_match",
        "screening_outcome",
        "match_summary_cn",
        "construct_candidates",
        "confidence",
        "analysis_mode",
        "fulltext_chars",
    ]
    with temp_csv.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for source_file in sorted(decisions):
            row = dict(decisions[source_file])
            row["construct_candidates"] = json.dumps(
                row.get("construct_candidates", []), ensure_ascii=False
            )
            writer.writerow({field: row.get(field, "") for field in fields})
    os.replace(temp_csv, csv_path)

    values = list(decisions.values())
    completed_files = {path.name for path in all_files} & set(decisions)
    summary = {
        "updated_at": utc_now(),
        "analysis_version": analysis_version,
        "prompt_fingerprint": fingerprint,
        "input_fulltext_files": len(all_files),
        "completed": len(completed_files),
        "pending": len(all_files) - len(completed_files),
        "has_explicit_named_construct_true": sum(
            row.get("has_explicit_named_construct") is True for row in values
        ),
        "has_multidimensional_construct_candidate_true": sum(
            row.get("has_multidimensional_construct_candidate") is True for row in values
        ),
        "has_all_objective_component_measurement_candidate_true": sum(
            row.get("has_all_objective_component_measurement_candidate") is True for row in values
        ),
        "has_aggregation_to_construct_value_candidate_true": sum(
            row.get("has_aggregation_to_construct_value_candidate") is True for row in values
        ),
        "objective_higher_order_construct_match_true": sum(
            row.get("objective_higher_order_construct_match") is True for row in values
        ),
        "screening_outcome_counts": {
            value: sum(row.get("screening_outcome") == value for row in values)
            for value in sorted(OUTCOME_VALUES)
        },
        "usage": {
            key: sum(int((row.get("usage") or {}).get(key, 0)) for row in values)
            for key in ("prompt_tokens", "completion_tokens", "total_tokens")
        },
    }
    summary_path = output_dir / "summary.json"
    temp_summary = summary_path.with_suffix(".json.tmp")
    temp_summary.write_text(
        json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    os.replace(temp_summary, summary_path)


def main() -> int:
    def task_print(*args: Any, **kwargs: Any) -> None:
        if args and isinstance(args[0], str):
            first = (
                args[0]
                .replace("new_construct=", "explicit_construct=")
                .replace("objective=", "all_components_objective=")
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
