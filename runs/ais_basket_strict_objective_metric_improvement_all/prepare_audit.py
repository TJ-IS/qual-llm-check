#!/usr/bin/env python3
"""Create a deterministic stratified audit sample from the current screening decisions."""

from __future__ import annotations

import json
import random
from collections import defaultdict
from pathlib import Path


RUN_DIR = Path(__file__).resolve().parent
DECISIONS = RUN_DIR / "output_v1" / "decisions.jsonl"
AUDIT_DIR = RUN_DIR / "audit_v1"
SEED = 20260806


def load_rows() -> list[dict]:
    rows: dict[str, dict] = {}
    with DECISIONS.open("r", encoding="utf-8") as handle:
        for line in handle:
            if line.strip():
                row = json.loads(line)
                rows[str(row["source_file"])] = row
    return list(rows.values())


def compact(row: dict, audit_group: str) -> dict:
    return {
        "audit_group": audit_group,
        "record_id": row.get("record_id"),
        "source_file": row.get("source_file"),
        "title": row.get("title"),
        "year": row.get("year"),
        "journal": row.get("journal"),
        "doi": row.get("doi"),
        "strict_match": row.get("strict_objective_improvement_match"),
        "gates": row.get("gates"),
        "centrality": row.get("objective_metric_centrality"),
        "solution_layer": row.get("solution_layer"),
        "research_paradigms": row.get("research_paradigms"),
        "objective_metrics": row.get("objective_metrics"),
        "knowledge_and_design_basis": row.get("knowledge_and_design_basis"),
        "research_logic": row.get("research_logic"),
        "decision_reason_cn": row.get("decision_reason_cn"),
        "confidence": row.get("confidence"),
    }


def main() -> None:
    rows = load_rows()
    rng = random.Random(SEED)
    selected: list[dict] = []
    used: set[str] = set()

    by_layer: dict[str, list[dict]] = defaultdict(list)
    for row in rows:
        if row.get("strict_objective_improvement_match") is True:
            by_layer[str(row.get("solution_layer"))].append(row)
    for layer in sorted(by_layer):
        pool = sorted(by_layer[layer], key=lambda item: str(item.get("source_file")))
        for row in rng.sample(pool, min(2, len(pool))):
            selected.append(compact(row, f"retained_layer:{layer}"))
            used.add(str(row["source_file"]))

    theory_pool = [
        row for row in rows
        if row.get("strict_objective_improvement_match") is True
        and "theory_driven_artifact_experiment" in (row.get("research_paradigms") or [])
        and str(row.get("source_file")) not in used
    ]
    for row in rng.sample(sorted(theory_pool, key=lambda item: str(item.get("source_file"))), min(4, len(theory_pool))):
        selected.append(compact(row, "retained_theory_driven"))
        used.add(str(row["source_file"]))

    near_pool = []
    for row in rows:
        if row.get("strict_objective_improvement_match") is True:
            continue
        gates = row.get("gates") or {}
        passed = sum(bool(value) for value in gates.values())
        if passed == 3 and row.get("objective_metric_centrality") in {"exclusive", "dominant", "mixed"}:
            near_pool.append(row)
    for row in rng.sample(sorted(near_pool, key=lambda item: str(item.get("source_file"))), min(8, len(near_pool))):
        selected.append(compact(row, "near_miss_three_gates"))
        used.add(str(row["source_file"]))

    objective_without_design = [
        row for row in rows
        if row.get("strict_objective_improvement_match") is False
        and bool((row.get("gates") or {}).get("objective_metric_is_primary_target"))
        and not bool((row.get("gates") or {}).get("purposeful_solution_design"))
        and str(row.get("source_file")) not in used
    ]
    for row in rng.sample(sorted(objective_without_design, key=lambda item: str(item.get("source_file"))), min(4, len(objective_without_design))):
        selected.append(compact(row, "excluded_objective_without_design"))

    AUDIT_DIR.mkdir(parents=True, exist_ok=True)
    (AUDIT_DIR / "sample_manifest.json").write_text(
        json.dumps({"seed": SEED, "screened_available": len(rows), "sample_size": len(selected), "records": selected}, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    lines = ["# Stratified audit sample", "", f"Screened decisions available: {len(rows)}", f"Sample size: {len(selected)}", f"Seed: {SEED}", ""]
    for index, row in enumerate(selected, start=1):
        lines.extend([
            f"## {index}. {row['title']}", "",
            f"- Audit group: {row['audit_group']}",
            f"- Source file: `{row['source_file']}`",
            f"- Year/journal: {row['year']} / {row['journal']}",
            f"- Decision: {row['strict_match']} / {row['centrality']} / {row['solution_layer']}",
            f"- Gates: `{json.dumps(row['gates'], ensure_ascii=False)}`",
            f"- Model reason: {row['decision_reason_cn']}",
            "- Manual audit: pending",
            "",
        ])
    (AUDIT_DIR / "sample_report.md").write_text("\n".join(lines), encoding="utf-8")
    print(json.dumps({"screened_available": len(rows), "sample_size": len(selected), "audit_dir": str(AUDIT_DIR)}, ensure_ascii=False))


if __name__ == "__main__":
    main()
