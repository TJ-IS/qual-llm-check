#!/usr/bin/env python3
"""Classify the research level of the 264 programming-context matches."""

from __future__ import annotations

import builtins
import csv
import importlib.util
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


RUN_DIR = Path(__file__).resolve().parent
ENGINE_PATH = RUN_DIR.parent / "new_construct_objective_measurement_deepseek_analysis" / "analyze_fulltext.py"
SPEC = importlib.util.spec_from_file_location("research_level_batch_engine", ENGINE_PATH)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError(f"Cannot load shared batch engine from {ENGINE_PATH}")
ENGINE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = ENGINE
SPEC.loader.exec_module(ENGINE)

RESEARCH_LEVELS = {
    "individual",
    "dyadic",
    "team",
    "project",
    "organizational",
    "interorganizational",
    "community",
    "platform_ecosystem",
    "industry_market",
    "societal",
    "artifact_system",
    "mixed",
    "conceptual",
}


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def load_task_config() -> dict[str, Any]:
    with (RUN_DIR / "config.json").open("r", encoding="utf-8") as handle:
        return json.load(handle)


def resolve_from_run(value: str) -> Path:
    path = Path(value)
    return path.resolve() if path.is_absolute() else (RUN_DIR / path).resolve()


def source_csv_path() -> Path:
    return resolve_from_run(str(load_task_config()["source_matches_csv"]))


def load_source_rows() -> tuple[list[str], list[dict[str, str]]]:
    path = source_csv_path()
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        if not reader.fieldnames or "source_file" not in reader.fieldnames:
            raise ValueError(f"source_file column missing from {path}")
        rows = list(reader)
        fields = list(reader.fieldnames)
    names = [str(row.get("source_file") or "").strip() for row in rows]
    if any(not name for name in names):
        raise ValueError(f"Blank source_file in {path}")
    if len(names) != len(set(names)):
        raise ValueError(f"Duplicate source_file values in {path}")
    return fields, rows


def filter_to_prior_matches(files: list[Path], config: dict[str, Any]) -> list[Path]:
    del config
    _, rows = load_source_rows()
    selected = {str(row["source_file"]).strip() for row in rows}
    by_name = {path.name: path for path in files}
    missing = sorted(selected - set(by_name))
    if missing:
        raise FileNotFoundError(
            f"{len(missing)} prior match full texts are missing; first: {missing[:5]}"
        )
    return [by_name[name] for name in sorted(selected)]


def clean_text(value: Any) -> str:
    return str(value or "").strip()


def normalize_final(payload: dict[str, Any]) -> dict[str, Any]:
    level = clean_text(payload.get("research_level")).lower()
    if level not in RESEARCH_LEVELS:
        raise ValueError(f"invalid research_level: {level!r}")
    detail = clean_text(payload.get("research_level_detail_cn"))
    unit = clean_text(payload.get("unit_of_analysis_cn"))
    evidence = clean_text(payload.get("level_evidence_cn"))
    missing = [
        name
        for name, value in (
            ("research_level_detail_cn", detail),
            ("unit_of_analysis_cn", unit),
            ("level_evidence_cn", evidence),
        )
        if not value
    ]
    if missing:
        raise ValueError(f"missing required fields: {', '.join(missing)}")
    try:
        confidence = float(payload.get("confidence", 0.0))
    except (TypeError, ValueError):
        confidence = 0.0
    return {
        "research_level": level,
        "research_level_detail_cn": detail,
        "unit_of_analysis_cn": unit,
        "level_evidence_cn": evidence,
        "confidence": max(0.0, min(1.0, confidence)),
        # Compatibility aliases used only by the shared engine's progress line.
        "claims_new_construct_development": True,
        "objective_measurement_of_new_construct": True,
        "new_construct_with_objective_measurement": True,
    }


DECISION_FIELDS = [
    "source_file",
    "article_id",
    "title",
    "authors",
    "year",
    "journal",
    "doi",
    "analysis_version",
    "research_level",
    "research_level_detail_cn",
    "unit_of_analysis_cn",
    "level_evidence_cn",
    "confidence",
    "analysis_mode",
    "fulltext_chars",
]

ADDED_MERGED_FIELDS = [
    "research_level",
    "research_level_detail_cn",
    "unit_of_analysis_cn",
    "level_evidence_cn",
    "research_level_confidence",
    "research_level_analysis_version",
]


def write_csv(path: Path, fields: list[str], rows: list[dict[str, Any]]) -> None:
    temp_path = path.with_suffix(path.suffix + ".tmp")
    with temp_path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for row in rows:
            writer.writerow({field: row.get(field, "") for field in fields})
    os.replace(temp_path, path)


def write_reports(
    output_dir: Path,
    all_files: list[Path],
    decisions: dict[str, dict[str, Any]],
    analysis_version: str,
    fingerprint: str,
) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    decision_rows = [decisions[name] for name in sorted(decisions)]
    write_csv(output_dir / "research_level_decisions.csv", DECISION_FIELDS, decision_rows)

    original_fields, source_rows = load_source_rows()
    merged_fields = original_fields + [
        field for field in ADDED_MERGED_FIELDS if field not in original_fields
    ]
    merged_rows: list[dict[str, Any]] = []
    for source_row in source_rows:
        row: dict[str, Any] = dict(source_row)
        decision = decisions.get(str(source_row["source_file"]).strip())
        if decision:
            row.update(
                {
                    "research_level": decision["research_level"],
                    "research_level_detail_cn": decision["research_level_detail_cn"],
                    "unit_of_analysis_cn": decision["unit_of_analysis_cn"],
                    "level_evidence_cn": decision["level_evidence_cn"],
                    "research_level_confidence": decision["confidence"],
                    "research_level_analysis_version": decision["analysis_version"],
                }
            )
        merged_rows.append(row)
    write_csv(
        output_dir / "programming_context_matches_with_research_level.csv",
        merged_fields,
        merged_rows,
    )

    selected_names = {path.name for path in all_files}
    completed_names = selected_names & set(decisions)
    values = [decisions[name] for name in completed_names]
    summary = {
        "updated_at": utc_now(),
        "analysis_version": analysis_version,
        "prompt_fingerprint": fingerprint,
        "input_programming_context_matches": len(all_files),
        "completed": len(completed_names),
        "pending": len(all_files) - len(completed_names),
        "research_level_counts": {
            level: sum(row.get("research_level") == level for row in values)
            for level in sorted(RESEARCH_LEVELS)
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
                .replace("new_construct=", "level_fields=")
                .replace("objective=", "details=")
                .replace("target_match=", "valid_level=")
            )
            args = (first, *args[1:])
        builtins.print(*args, **kwargs)

    ENGINE.RUN_DIR = RUN_DIR
    ENGINE.CONFIG_PATH = RUN_DIR / "config.json"
    ENGINE.filter_selection = filter_to_prior_matches
    ENGINE.normalize_final = normalize_final
    ENGINE.write_reports = write_reports
    ENGINE.print = task_print
    return int(ENGINE.main())


if __name__ == "__main__":
    sys.exit(main())
