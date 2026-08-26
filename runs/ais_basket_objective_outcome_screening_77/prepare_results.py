#!/usr/bin/env python3
"""Flatten objective-outcome decisions for audit and workbook generation."""

from __future__ import annotations

import json
from pathlib import Path


RUN_DIR = Path(__file__).resolve().parent
SOURCE = RUN_DIR / "output_v1" / "decisions.jsonl"
OUTPUT = RUN_DIR / "output_v1" / "decisions_flat.json"


def join_text(values: list[str]) -> str:
    return "；".join(str(value).strip() for value in values if str(value).strip())


rows = [json.loads(line) for line in SOURCE.read_text(encoding="utf-8").splitlines() if line.strip()]
flat: list[dict[str, object]] = []
for row in sorted(rows, key=lambda item: (int(item.get("year") or 0), str(item.get("title") or ""))):
    outcomes = row.get("objective_outcomes") or []
    route = row["inclusion_routes"]
    flat.append(
        {
            "record_id": row.get("record_id"),
            "title": row.get("title"),
            "authors": row.get("authors"),
            "year": int(row.get("year") or 0),
            "journal": row.get("journal"),
            "doi": row.get("doi"),
            "objective_outcome_match": bool(row.get("objective_outcome_match")),
            "objective_design_target": bool(route.get("objective_design_target")),
            "objectively_measured_outcome": bool(route.get("objectively_measured_outcome")),
            "outcome_count": len(outcomes),
            "outcome_names": join_text([str(outcome.get("outcome_name") or "") for outcome in outcomes]),
            "outcome_roles": join_text([str(outcome.get("outcome_role") or "") for outcome in outcomes]),
            "measurement_methods_cn": join_text([str(outcome.get("measurement_method_cn") or "") for outcome in outcomes]),
            "objectivity_bases_cn": join_text([str(outcome.get("objectivity_basis_cn") or "") for outcome in outcomes]),
            "evidence": join_text([evidence for outcome in outcomes for evidence in (outcome.get("evidence") or [])]),
            "subjective_focal_outcomes_cn": join_text(row.get("subjective_focal_outcomes_cn") or []),
            "artifact_outcome_link_cn": row.get("artifact_outcome_link_cn") or "",
            "decision_reason_cn": row.get("decision_reason_cn") or "",
            "confidence": float(row.get("confidence") or 0),
            "limitations_cn": row.get("limitations_cn") or "",
            "source_file": row.get("source_file"),
        }
    )

OUTPUT.write_text(json.dumps(flat, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"rows={len(flat)} matches={sum(bool(row['objective_outcome_match']) for row in flat)}")
print("nonmatches:")
for row in flat:
    if not row["objective_outcome_match"]:
        print(f"- {row['title']}")
print("target_only:")
for row in flat:
    if row["objective_design_target"] and not row["objectively_measured_outcome"]:
        print(f"- {row['title']}")
