#!/usr/bin/env python3
"""Final full-text inclusion and concept-matrix coding for local candidates."""

from __future__ import annotations

import builtins
import csv
import importlib.util
import json
import os
import sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


RUN_DIR = Path(__file__).resolve().parent
ENGINE_PATH = (
    RUN_DIR.parent
    / "new_construct_objective_measurement_deepseek_analysis"
    / "analyze_fulltext.py"
)
SPEC = importlib.util.spec_from_file_location("programming_slr_fulltext_engine", ENGINE_PATH)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError(f"Cannot load shared engine from {ENGINE_PATH}")
ENGINE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = ENGINE
SPEC.loader.exec_module(ENGINE)

EVIDENCE_ROLES = {
    "primary_empirical",
    "design_and_evaluation",
    "conceptual",
    "secondary_review",
    "not_applicable",
}
ACTORS = {"human_only", "human_ai", "agent_only", "multiple", "unclear", "not_applicable"}
ARTIFACTS = {
    "source_code",
    "database_query",
    "spreadsheet_logic",
    "low_code_or_visual",
    "other_executable_logic",
    "multiple",
    "unclear",
    "not_applicable",
}
ACTIONS = {
    "write",
    "generate",
    "complete",
    "understand",
    "inspect_or_review",
    "debug_or_repair",
    "modify_or_refactor",
    "test",
}
UNITS = {
    "individual",
    "dyad",
    "team",
    "organization",
    "project_or_community",
    "code_artifact_or_agent",
    "multiple",
    "unclear",
    "not_applicable",
}


def clean(value: Any) -> str:
    return str(value or "").strip()


def list_of_strings(value: Any) -> list[str]:
    return [clean(item) for item in value] if isinstance(value, list) else []


def normalize_final(payload: dict[str, Any]) -> dict[str, Any]:
    final_include = payload.get("final_include")
    if not isinstance(final_include, bool):
        raise ValueError("final_include must be boolean")
    role = clean(payload.get("evidence_role")).lower()
    actor = clean(payload.get("actor_type")).lower()
    artifact = clean(payload.get("program_artifact")).lower()
    unit = clean(payload.get("unit_of_analysis")).lower()
    if role not in EVIDENCE_ROLES:
        raise ValueError(f"invalid evidence_role: {role!r}")
    if actor not in ACTORS:
        raise ValueError(f"invalid actor_type: {actor!r}")
    if artifact not in ARTIFACTS:
        raise ValueError(f"invalid program_artifact: {artifact!r}")
    if unit not in UNITS:
        raise ValueError(f"invalid unit_of_analysis: {unit!r}")
    actions = list(dict.fromkeys(item.lower() for item in list_of_strings(payload.get("programming_actions"))))
    if any(action not in ACTIONS for action in actions):
        raise ValueError(f"invalid programming_actions: {actions!r}")
    evidence = payload.get("fulltext_evidence")
    if not isinstance(evidence, list):
        evidence = []
    normalized_evidence = []
    for item in evidence:
        if isinstance(item, dict):
            normalized_evidence.append(
                {
                    "section": clean(item.get("section")),
                    "evidence": clean(item.get("evidence")),
                    "supports": clean(item.get("supports")),
                }
            )
    exclusion_reason = clean(payload.get("exclusion_reason_cn"))
    if not final_include and not exclusion_reason:
        raise ValueError("excluded records require exclusion_reason_cn")
    if final_include:
        required = [
            "programming_situation_definition_cn",
            "task_and_setting_cn",
            "research_method_cn",
            "main_findings_cn",
        ]
        missing = [key for key in required if not clean(payload.get(key))]
        if missing:
            raise ValueError(f"included record missing fields: {missing}")
        if len(normalized_evidence) < 2:
            raise ValueError("included record requires at least two evidence items")
    else:
        role = "not_applicable"
        actor = "not_applicable"
        artifact = "not_applicable"
        actions = []
        unit = "not_applicable"
    try:
        confidence = float(payload.get("confidence", 0.0))
    except (TypeError, ValueError):
        confidence = 0.0
    return {
        "final_include": final_include,
        "exclusion_reason_cn": exclusion_reason,
        "evidence_role": role,
        "actor_type": actor,
        "program_artifact": artifact,
        "programming_actions": actions,
        "programming_situation_definition_cn": clean(payload.get("programming_situation_definition_cn")),
        "task_and_setting_cn": clean(payload.get("task_and_setting_cn")),
        "research_method_cn": clean(payload.get("research_method_cn")),
        "unit_of_analysis": unit,
        "sample_and_data_cn": clean(payload.get("sample_and_data_cn")),
        "sample_independence_note_cn": clean(payload.get("sample_independence_note_cn")),
        "theory_or_framework_names": list_of_strings(payload.get("theory_or_framework_names")),
        "independent_variables": list_of_strings(payload.get("independent_variables")),
        "mediators": list_of_strings(payload.get("mediators")),
        "moderators": list_of_strings(payload.get("moderators")),
        "dependent_variables": list_of_strings(payload.get("dependent_variables")),
        "main_findings_cn": clean(payload.get("main_findings_cn")),
        "human_agent_relation_cn": clean(payload.get("human_agent_relation_cn")),
        "fulltext_evidence": normalized_evidence,
        "quality_and_limitations_cn": clean(payload.get("quality_and_limitations_cn")),
        "confidence": max(0.0, min(1.0, confidence)),
        # Compatibility aliases for shared progress output.
        "claims_new_construct_development": final_include,
        "objective_measurement_of_new_construct": final_include,
        "new_construct_with_objective_measurement": final_include,
    }


JSON_FIELDS = [
    "programming_actions",
    "theory_or_framework_names",
    "independent_variables",
    "mediators",
    "moderators",
    "dependent_variables",
    "fulltext_evidence",
]
FIELDS = [
    "source_file",
    "article_id",
    "title",
    "authors",
    "year",
    "journal",
    "doi",
    "analysis_version",
    "final_include",
    "exclusion_reason_cn",
    "evidence_role",
    "actor_type",
    "program_artifact",
    "programming_actions",
    "programming_situation_definition_cn",
    "task_and_setting_cn",
    "research_method_cn",
    "unit_of_analysis",
    "sample_and_data_cn",
    "sample_independence_note_cn",
    "theory_or_framework_names",
    "independent_variables",
    "mediators",
    "moderators",
    "dependent_variables",
    "main_findings_cn",
    "human_agent_relation_cn",
    "fulltext_evidence",
    "quality_and_limitations_cn",
    "confidence",
    "analysis_mode",
    "fulltext_chars",
]


def write_csv(path: Path, rows: list[dict[str, Any]]) -> None:
    temp = path.with_suffix(path.suffix + ".tmp")
    with temp.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDS)
        writer.writeheader()
        for source in rows:
            row = dict(source)
            for field in JSON_FIELDS:
                row[field] = json.dumps(row.get(field, []), ensure_ascii=False)
            writer.writerow({field: row.get(field, "") for field in FIELDS})
    os.replace(temp, path)


def write_reports(
    output_dir: Path,
    all_files: list[Path],
    decisions: dict[str, dict[str, Any]],
    analysis_version: str,
    fingerprint: str,
) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    rows = [decisions[name] for name in sorted(decisions)]
    write_csv(output_dir / "decisions.csv", rows)
    write_csv(output_dir / "included.csv", [row for row in rows if row.get("final_include") is True])
    summary = {
        "updated_at": datetime.now(timezone.utc).isoformat(),
        "analysis_version": analysis_version,
        "prompt_fingerprint": fingerprint,
        "input_fulltexts": len(all_files),
        "completed": len(rows),
        "pending": len(all_files) - len({path.name for path in all_files} & set(decisions)),
        "final_include_true": sum(row.get("final_include") is True for row in rows),
        "evidence_role_counts": dict(Counter(row.get("evidence_role", "") for row in rows if row.get("final_include") is True)),
        "actor_counts": dict(Counter(row.get("actor_type", "") for row in rows if row.get("final_include") is True)),
        "artifact_counts": dict(Counter(row.get("program_artifact", "") for row in rows if row.get("final_include") is True)),
    }
    temp = (output_dir / "summary.json").with_suffix(".json.tmp")
    temp.write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    os.replace(temp, output_dir / "summary.json")


def main() -> int:
    def task_print(*args: Any, **kwargs: Any) -> None:
        if args and isinstance(args[0], str):
            first = (
                args[0]
                .replace("new_construct=", "final_include=")
                .replace("objective=", "final_include=")
                .replace("target_match=", "final_include=")
            )
            args = (first, *args[1:])
        builtins.print(*args, **kwargs)

    ENGINE.RUN_DIR = RUN_DIR
    ENGINE.CONFIG_PATH = RUN_DIR / "config_fulltext.json"
    ENGINE.normalize_final = normalize_final
    ENGINE.write_reports = write_reports
    ENGINE.print = task_print
    return int(ENGINE.main())


if __name__ == "__main__":
    sys.exit(main())
