#!/usr/bin/env python3
"""High-recall title/abstract screening for the programming SLR."""

from __future__ import annotations

import builtins
import csv
import importlib.util
import json
import os
import re
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
SPEC = importlib.util.spec_from_file_location("programming_slr_screen_engine", ENGINE_PATH)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError(f"Cannot load shared batch engine from {ENGINE_PATH}")
ENGINE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = ENGINE
SPEC.loader.exec_module(ENGINE)

LABELS = {"include_candidate", "uncertain", "exclude"}
CENTRALITY = {
    "programming_core",
    "programming_as_context",
    "not_programming",
    "unclear",
}
ACTOR_TYPES = {"human_only", "human_ai", "agent_only", "unclear", "not_applicable"}
ARTIFACT_TYPES = {
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
ACTION_ALIASES = {
    "coding": "write",
    "program": "write",
    "programming": "write",
    "generation": "generate",
    "code_generation": "generate",
    "completion": "complete",
    "code_completion": "complete",
    "read": "understand",
    "comprehend": "understand",
    "comprehension": "understand",
    "explain": "understand",
    "inspect": "inspect_or_review",
    "review": "inspect_or_review",
    "check": "inspect_or_review",
    "verify": "inspect_or_review",
    "debug": "debug_or_repair",
    "repair": "debug_or_repair",
    "fix": "debug_or_repair",
    "modify": "modify_or_refactor",
    "refactor": "modify_or_refactor",
    "maintenance": "modify_or_refactor",
    "testing": "test",
}
STUDY_TYPES = {
    "empirical_human",
    "empirical_artifact_or_agent",
    "tool_design_and_evaluation",
    "secondary_review",
    "conceptual",
    "unclear",
    "not_applicable",
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


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def clean(value: Any) -> str:
    return str(value or "").strip()


def normalize_final(payload: dict[str, Any]) -> dict[str, Any]:
    label = clean(payload.get("screening_label")).lower()
    centrality = clean(payload.get("programming_centrality")).lower()
    if centrality in {"not_applicable", "n/a", "none"}:
        centrality = "not_programming" if label == "exclude" else "unclear"
    actor = clean(payload.get("actor_type")).lower()
    artifact = clean(payload.get("program_artifact")).lower()
    if re.search(r"[|,;/]", artifact):
        artifact = "multiple"
    study_type = clean(payload.get("study_type")).lower()
    unit = clean(payload.get("unit_of_analysis")).lower()
    if label not in LABELS:
        raise ValueError(f"invalid screening_label: {label!r}")
    if centrality not in CENTRALITY:
        raise ValueError(f"invalid programming_centrality: {centrality!r}")
    if actor not in ACTOR_TYPES:
        raise ValueError(f"invalid actor_type: {actor!r}")
    if artifact not in ARTIFACT_TYPES:
        raise ValueError(f"invalid program_artifact: {artifact!r}")
    if study_type not in STUDY_TYPES:
        raise ValueError(f"invalid study_type: {study_type!r}")
    if unit not in UNITS:
        raise ValueError(f"invalid unit_of_analysis: {unit!r}")
    raw_actions = payload.get("programming_actions")
    actions = []
    for value in (raw_actions if isinstance(raw_actions, list) else []):
        for raw_action in re.split(r"[|,;/]+", clean(value).lower()):
            action = raw_action.strip()
            if action in {"", "none", "not_applicable", "n/a"}:
                continue
            actions.append(ACTION_ALIASES.get(action, action))
    if label == "exclude":
        actions = []
    if any(action not in ACTIONS for action in actions):
        raise ValueError(f"invalid programming_actions: {actions!r}")
    actions = list(dict.fromkeys(actions))
    summary = clean(payload.get("research_summary_cn"))
    reason = clean(payload.get("decision_reason_cn"))
    evidence = clean(payload.get("metadata_evidence_cn"))
    if not reason or not evidence:
        raise ValueError("decision_reason_cn and metadata_evidence_cn are required")
    if label != "exclude" and not summary:
        raise ValueError("research_summary_cn is required for candidates")
    if label == "exclude":
        actor = "not_applicable"
        artifact = "not_applicable"
        actions = []
        study_type = "not_applicable"
        unit = "not_applicable"
        summary = ""
    try:
        confidence = float(payload.get("confidence", 0.0))
    except (TypeError, ValueError):
        confidence = 0.0
    candidate = label != "exclude"
    return {
        "screening_label": label,
        "programming_centrality": centrality,
        "actor_type": actor,
        "program_artifact": artifact,
        "programming_actions": actions,
        "study_type": study_type,
        "unit_of_analysis": unit,
        "theory_or_framework_names": [
            clean(value)
            for value in (
                payload.get("theory_or_framework_names")
                if isinstance(payload.get("theory_or_framework_names"), list)
                else []
            )
            if clean(value)
        ],
        "research_summary_cn": summary,
        "decision_reason_cn": reason,
        "metadata_evidence_cn": evidence,
        "confidence": max(0.0, min(1.0, confidence)),
        # Compatibility aliases expected by the shared engine.
        "claims_new_construct_development": candidate,
        "objective_measurement_of_new_construct": label == "include_candidate",
        "new_construct_with_objective_measurement": candidate,
    }


FIELDS = [
    "source_file",
    "article_id",
    "title",
    "authors",
    "year",
    "journal",
    "doi",
    "analysis_version",
    "screening_label",
    "programming_centrality",
    "actor_type",
    "program_artifact",
    "programming_actions",
    "study_type",
    "unit_of_analysis",
    "theory_or_framework_names",
    "research_summary_cn",
    "decision_reason_cn",
    "metadata_evidence_cn",
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
            for field in ("programming_actions", "theory_or_framework_names"):
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
    write_csv(
        output_dir / "candidates.csv",
        [row for row in rows if row.get("screening_label") != "exclude"],
    )
    summary = {
        "updated_at": utc_now(),
        "analysis_version": analysis_version,
        "prompt_fingerprint": fingerprint,
        "input_records": len(all_files),
        "completed": len(rows),
        "pending": len(all_files) - len({path.name for path in all_files} & set(decisions)),
        "screening_label_counts": dict(
            Counter(str(row.get("screening_label") or "") for row in rows)
        ),
        "candidate_centrality_counts": dict(
            Counter(
                str(row.get("programming_centrality") or "")
                for row in rows
                if row.get("screening_label") != "exclude"
            )
        ),
        "candidate_actor_counts": dict(
            Counter(
                str(row.get("actor_type") or "")
                for row in rows
                if row.get("screening_label") != "exclude"
            )
        ),
        "candidate_study_type_counts": dict(
            Counter(
                str(row.get("study_type") or "")
                for row in rows
                if row.get("screening_label") != "exclude"
            )
        ),
        "usage": {
            key: sum(int((row.get("usage") or {}).get(key, 0)) for row in rows)
            for key in ("prompt_tokens", "completion_tokens", "total_tokens")
        },
    }
    temp = (output_dir / "summary.json").with_suffix(".json.tmp")
    temp.write_text(
        json.dumps(summary, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    os.replace(temp, output_dir / "summary.json")


def main(config_name: str = "config.json") -> int:
    def task_print(*args: Any, **kwargs: Any) -> None:
        if args and isinstance(args[0], str):
            first = (
                args[0]
                .replace("new_construct=", "candidate=")
                .replace("objective=", "include_candidate=")
                .replace("target_match=", "candidate=")
            )
            args = (first, *args[1:])
        builtins.print(*args, **kwargs)

    ENGINE.RUN_DIR = RUN_DIR
    ENGINE.CONFIG_PATH = RUN_DIR / config_name
    ENGINE.normalize_final = normalize_final
    ENGINE.write_reports = write_reports
    ENGINE.print = task_print
    return int(ENGINE.main())


if __name__ == "__main__":
    sys.exit(main())
