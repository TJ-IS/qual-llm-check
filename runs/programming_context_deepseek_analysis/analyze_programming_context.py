#!/usr/bin/env python3
"""Screen full-text articles for substantive programming research contexts."""

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
SPEC = importlib.util.spec_from_file_location("programming_context_batch_engine", ENGINE_PATH)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError(f"Cannot load shared batch engine from {ENGINE_PATH}")
ENGINE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = ENGINE
SPEC.loader.exec_module(ENGINE)

SA_RELATION_TYPES = {"explicit", "conceptually_related", "none"}
LIST_FIELDS = (
    "independent_variables",
    "mediators",
    "moderators",
    "dependent_variables",
    "theory_names",
)


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def clean_text(value: Any) -> str:
    return str(value or "").strip()


def clean_string_list(value: Any) -> list[str]:
    if value is None:
        return []
    values = value if isinstance(value, list) else [value]
    cleaned: list[str] = []
    for item in values:
        if isinstance(item, dict):
            text = json.dumps(item, ensure_ascii=False, sort_keys=True)
        else:
            text = clean_text(item)
        if text and text not in cleaned:
            cleaned.append(text)
    return cleaned


def normalize_final(payload: dict[str, Any]) -> dict[str, Any]:
    is_context = payload.get("is_programming_context") is True
    exclusion_reason = clean_text(payload.get("exclusion_reason_cn"))

    if not is_context:
        return {
            "is_programming_context": False,
            "content_summary_cn": "",
            "programming_context_definition_cn": "",
            **{field: [] for field in LIST_FIELDS},
            "research_method_cn": "",
            "situation_awareness_relation_type": "none",
            "situation_awareness_relation_cn": "",
            "exclusion_reason_cn": exclusion_reason or "全文未显示编程活动是实质研究情境。",
            "required_fields_complete": True,
            "normalization_warning_cn": "",
            "claims_new_construct_development": False,
            "objective_measurement_of_new_construct": False,
            "new_construct_with_objective_measurement": False,
        }

    summary = clean_text(payload.get("content_summary_cn"))
    definition = clean_text(payload.get("programming_context_definition_cn"))
    method = clean_text(payload.get("research_method_cn"))
    sa_relation = clean_text(payload.get("situation_awareness_relation_cn"))
    raw_sa_type = clean_text(payload.get("situation_awareness_relation_type")).lower()
    sa_type = raw_sa_type if raw_sa_type in SA_RELATION_TYPES else "none"

    missing: list[str] = []
    if not summary:
        missing.append("content_summary_cn")
        summary = "模型判定该文属于编程情境，但未返回研究内容概要。"
    if not definition:
        missing.append("programming_context_definition_cn")
        definition = "模型判定该文属于编程情境，但未返回本文对编程情境的操作性边界。"
    if not method:
        missing.append("research_method_cn")
        method = "模型判定该文属于编程情境，但未返回研究方法说明。"
    if not sa_relation:
        missing.append("situation_awareness_relation_cn")
        sa_type = "none"
        sa_relation = "全文未报告与 situation awareness 的明确或可论证关系。"

    return {
        "is_programming_context": True,
        "content_summary_cn": summary,
        "programming_context_definition_cn": definition,
        **{field: clean_string_list(payload.get(field)) for field in LIST_FIELDS},
        "research_method_cn": method,
        "situation_awareness_relation_type": sa_type,
        "situation_awareness_relation_cn": sa_relation,
        "exclusion_reason_cn": "",
        "required_fields_complete": not missing,
        "normalization_warning_cn": (
            "模型缺少必填字段：" + ", ".join(missing) if missing else ""
        ),
        # Compatibility aliases used only by the shared engine's progress line.
        "claims_new_construct_development": True,
        "objective_measurement_of_new_construct": True,
        "new_construct_with_objective_measurement": True,
    }


def write_reports(
    output_dir: Path,
    all_files: list[Path],
    decisions: dict[str, dict[str, Any]],
    analysis_version: str,
    fingerprint: str,
) -> None:
    fields = [
        "source_file",
        "article_id",
        "title",
        "authors",
        "year",
        "journal",
        "doi",
        "analysis_version",
        "is_programming_context",
        "content_summary_cn",
        "programming_context_definition_cn",
        *LIST_FIELDS,
        "research_method_cn",
        "situation_awareness_relation_type",
        "situation_awareness_relation_cn",
        "exclusion_reason_cn",
        "required_fields_complete",
        "normalization_warning_cn",
        "analysis_mode",
        "fulltext_chars",
    ]

    def write_csv(path: Path, rows: list[dict[str, Any]]) -> None:
        temp_path = path.with_suffix(".csv.tmp")
        with temp_path.open("w", encoding="utf-8-sig", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=fields)
            writer.writeheader()
            for item in sorted(rows, key=lambda row: str(row.get("source_file") or "")):
                row = dict(item)
                for field in LIST_FIELDS:
                    row[field] = json.dumps(row.get(field, []), ensure_ascii=False)
                writer.writerow({field: row.get(field, "") for field in fields})
        os.replace(temp_path, path)

    values = list(decisions.values())
    write_csv(output_dir / "decisions.csv", values)
    write_csv(
        output_dir / "programming_context_matches.csv",
        [row for row in values if row.get("is_programming_context") is True],
    )

    completed_files = {path.name for path in all_files} & set(decisions)
    matches = [row for row in values if row.get("is_programming_context") is True]
    summary = {
        "updated_at": utc_now(),
        "analysis_version": analysis_version,
        "prompt_fingerprint": fingerprint,
        "input_fulltext_files": len(all_files),
        "completed": len(completed_files),
        "pending": len(all_files) - len(completed_files),
        "programming_context_true": len(matches),
        "required_fields_incomplete": sum(
            row.get("required_fields_complete") is not True for row in matches
        ),
        "situation_awareness_relation_counts": {
            relation_type: sum(
                row.get("situation_awareness_relation_type") == relation_type
                for row in matches
            )
            for relation_type in sorted(SA_RELATION_TYPES)
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
                .replace("new_construct=", "programming_context=")
                .replace("objective=", "details_returned=")
                .replace("target_match=", "programming_context=")
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
