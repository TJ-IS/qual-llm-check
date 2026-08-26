#!/usr/bin/env python3
"""Binary full-text screening for independently reproducible research methods."""

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
SPEC = importlib.util.spec_from_file_location("low_barrier_method_batch_engine", ENGINE_PATH)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError(f"Cannot load shared batch engine from {ENGINE_PATH}")
ENGINE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = ENGINE
SPEC.loader.exec_module(ENGINE)


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def normalize_final(payload: dict[str, Any]) -> dict[str, Any]:
    qualifies = payload.get("qualifies") is True
    uses_large_scale_compute = payload.get("uses_large_scale_compute") is True
    has_pure_survey = payload.get("has_pure_survey") is True
    has_pure_interview = payload.get("has_pure_interview") is True
    has_experiment = payload.get("has_experiment") is True
    method_name = str(payload.get("method_name") or "").strip()
    overview = str(payload.get("short_overview_cn") or "").strip()
    exclusion_reason = str(payload.get("exclusion_reason_cn") or "").strip()
    if qualifies and not (method_name and overview):
        qualifies = False
        exclusion_reason = exclusion_reason or "模型判为true，但没有同时返回方法名和短介绍。"
    if not qualifies:
        method_name = ""
        overview = ""

    return {
        "qualifies": qualifies,
        "uses_large_scale_compute": uses_large_scale_compute,
        "has_pure_survey": has_pure_survey,
        "has_pure_interview": has_pure_interview,
        "has_experiment": has_experiment,
        "method_name": method_name,
        "short_overview_cn": overview,
        "exclusion_reason_cn": "" if qualifies else exclusion_reason,
        # Compatibility aliases used by the shared engine's progress display.
        "claims_new_construct_development": bool(method_name),
        "objective_measurement_of_new_construct": qualifies,
        "new_construct_with_objective_measurement": qualifies,
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
        "qualifies",
        "uses_large_scale_compute",
        "has_pure_survey",
        "has_pure_interview",
        "has_experiment",
        "method_name",
        "short_overview_cn",
        "exclusion_reason_cn",
        "analysis_mode",
        "fulltext_chars",
    ]
    with temp_csv.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for source_file in sorted(decisions):
            row = dict(decisions[source_file])
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
        "qualifies_true": sum(row.get("qualifies") is True for row in values),
        "uses_large_scale_compute_true": sum(
            row.get("uses_large_scale_compute") is True for row in values
        ),
        "has_pure_survey_true": sum(
            row.get("has_pure_survey") is True for row in values
        ),
        "has_pure_interview_true": sum(
            row.get("has_pure_interview") is True for row in values
        ),
        "has_experiment_true": sum(
            row.get("has_experiment") is True for row in values
        ),
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
    config_path = RUN_DIR / "config.json"
    if "--config" in sys.argv:
        config_index = sys.argv.index("--config")
        try:
            raw_config_path = sys.argv[config_index + 1]
        except IndexError as exc:
            raise SystemExit("--config requires a JSON file path") from exc
        candidate = Path(raw_config_path)
        config_path = candidate if candidate.is_absolute() else RUN_DIR / candidate
        del sys.argv[config_index : config_index + 2]

    force_chunk = "--force-chunk" in sys.argv
    if force_chunk:
        sys.argv.remove("--force-chunk")
        original_load_config = ENGINE.load_config

        def load_config_forced_chunk() -> dict[str, Any]:
            config = original_load_config()
            config["batch"] = dict(config["batch"])
            config["batch"]["direct_max_chars"] = 0
            return config

        ENGINE.load_config = load_config_forced_chunk

    def task_print(*args: Any, **kwargs: Any) -> None:
        if args and isinstance(args[0], str):
            first = (
                args[0]
                .replace("new_construct=", "method_returned=")
                .replace("objective=", "qualifies=")
                .replace("target_match=", "qualifies=")
            )
            args = (first, *args[1:])
        builtins.print(*args, **kwargs)

    ENGINE.RUN_DIR = RUN_DIR
    ENGINE.CONFIG_PATH = config_path.resolve()
    ENGINE.normalize_final = normalize_final
    ENGINE.write_reports = write_reports
    ENGINE.print = task_print
    return int(ENGINE.main())


if __name__ == "__main__":
    sys.exit(main())
