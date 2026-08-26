#!/usr/bin/env python3
"""Screen recent papers citing the 20 programming seeds using Scopus metadata."""

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
SPEC = importlib.util.spec_from_file_location(
    "recent_citation_metadata_batch_engine", ENGINE_PATH
)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError(f"Cannot load shared batch engine from {ENGINE_PATH}")
ENGINE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = ENGINE
SPEC.loader.exec_module(ENGINE)

LABELS = {"likely_direct", "possible_direct", "not_direct"}
ACTOR_TYPES = {"human_only", "human_ai", "agent_only", "unclear", "not_applicable"}
ARTIFACT_TYPES = {
    "source_code",
    "database_query",
    "spreadsheet_logic",
    "low_code_or_visual",
    "other",
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


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def clean_text(value: Any) -> str:
    return str(value or "").strip()


def normalize_final(payload: dict[str, Any]) -> dict[str, Any]:
    label = clean_text(payload.get("screening_label")).lower()
    actor_type = clean_text(payload.get("actor_type")).lower()
    artifact = clean_text(payload.get("program_artifact")).lower()
    if label not in LABELS:
        raise ValueError(f"invalid screening_label: {label!r}")
    if actor_type not in ACTOR_TYPES:
        raise ValueError(f"invalid actor_type: {actor_type!r}")
    if artifact not in ARTIFACT_TYPES:
        raise ValueError(f"invalid program_artifact: {artifact!r}")
    raw_actions = payload.get("programming_actions")
    actions = [
        clean_text(value).lower()
        for value in (raw_actions if isinstance(raw_actions, list) else [])
    ]
    if any(action not in ACTIONS for action in actions):
        raise ValueError(f"invalid programming_actions: {actions!r}")
    actions = list(dict.fromkeys(actions))
    summary = clean_text(payload.get("research_summary_cn"))
    reason = clean_text(payload.get("decision_reason_cn"))
    evidence = clean_text(payload.get("metadata_evidence_cn"))
    if not reason or not evidence:
        raise ValueError("decision_reason_cn and metadata_evidence_cn are required")
    if label != "not_direct" and not summary:
        raise ValueError("research_summary_cn is required for candidate records")
    if label == "not_direct":
        actor_type = "not_applicable"
        artifact = "not_applicable"
        actions = []
        summary = ""
    try:
        confidence = float(payload.get("confidence", 0.0))
    except (TypeError, ValueError):
        confidence = 0.0
    candidate = label != "not_direct"
    return {
        "screening_label": label,
        "actor_type": actor_type,
        "program_artifact": artifact,
        "programming_actions": actions,
        "research_summary_cn": summary,
        "decision_reason_cn": reason,
        "metadata_evidence_cn": evidence,
        "confidence": max(0.0, min(1.0, confidence)),
        # Compatibility aliases used by the shared engine's progress output.
        "claims_new_construct_development": candidate,
        "objective_measurement_of_new_construct": label == "likely_direct",
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
    "actor_type",
    "program_artifact",
    "programming_actions",
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
            row["programming_actions"] = json.dumps(
                row.get("programming_actions", []), ensure_ascii=False
            )
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
        [row for row in rows if row.get("screening_label") != "not_direct"],
    )
    counts = Counter(str(row.get("screening_label") or "") for row in rows)
    actor_counts = Counter(
        str(row.get("actor_type") or "")
        for row in rows
        if row.get("screening_label") != "not_direct"
    )
    action_counts: Counter[str] = Counter()
    for row in rows:
        if row.get("screening_label") == "not_direct":
            continue
        action_counts.update(row.get("programming_actions") or [])
    summary = {
        "updated_at": utc_now(),
        "analysis_version": analysis_version,
        "prompt_fingerprint": fingerprint,
        "input_records": len(all_files),
        "completed": len(rows),
        "pending": len(all_files) - len({path.name for path in all_files} & set(decisions)),
        "screening_label_counts": dict(counts),
        "candidate_actor_counts": dict(actor_counts),
        "candidate_action_counts": dict(action_counts),
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


def main() -> int:
    def task_print(*args: Any, **kwargs: Any) -> None:
        if args and isinstance(args[0], str):
            first = (
                args[0]
                .replace("new_construct=", "candidate=")
                .replace("objective=", "likely_direct=")
                .replace("target_match=", "candidate=")
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
