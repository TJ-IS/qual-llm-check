#!/usr/bin/env python3
"""Create compact, readable views of the series-mimic screening results."""

from __future__ import annotations

import json
from collections import Counter
from pathlib import Path


RUN_DIR = Path(__file__).resolve().parent
source = RUN_DIR / "output_v1" / "decisions.jsonl"
rows = [json.loads(line) for line in source.read_text(encoding="utf-8").splitlines() if line.strip()]

compact = []
for row in sorted(rows, key=lambda item: ({"high": 0, "medium": 1, "low": 2, "reject": 3}.get(item["mimic_priority"], 9), item["title"])):
    source_pattern = row["source_pattern"]
    series = row["series_value"]
    compact.append(
        {
            "record_id": row["record_id"],
            "title": row["title"],
            "year": row["year"],
            "journal": row["journal"],
            "doi": row["doi"],
            "mimic_candidate": row["mimic_candidate"],
            "mimic_priority": row["mimic_priority"],
            "conditions": row["essential_conditions"],
            "design_delta_cn": source_pattern.get("design_delta_cn", ""),
            "comparison_logic_cn": source_pattern.get("comparison_logic_cn", ""),
            "objective_outcomes": source_pattern.get("objective_outcomes", []),
            "theory_to_design_chain": source_pattern.get("theory_to_design_chain", []),
            "method_template_cn": source_pattern.get("method_template_cn", ""),
            "resource_requirements_cn": source_pattern.get("resource_requirements_cn", ""),
            "source_outcome_structure_cn": series.get("source_outcome_structure_cn", ""),
            "coding_agent_analogue_outcome_cn": series.get("coding_agent_analogue_outcome_cn", ""),
            "coding_agent_stage_or_dimension_cn": series.get("coding_agent_stage_or_dimension_cn", ""),
            "coding_agent_specificity_cn": series.get("coding_agent_specificity_cn", ""),
            "what_to_copy_cn": series.get("what_to_copy_cn", ""),
            "what_not_to_copy_cn": series.get("what_not_to_copy_cn", ""),
            "decision_reason_cn": row.get("decision_reason_cn", ""),
            "confidence": row.get("confidence"),
            "source_file": row.get("source_file"),
        }
    )

(RUN_DIR / "output_v1" / "compact_results.json").write_text(
    json.dumps(compact, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
)

print(f"rows={len(rows)} priorities={dict(Counter(row['mimic_priority'] for row in rows))}")
for row in compact:
    if row["mimic_priority"] == "high":
        print(f"\n[{row['record_id']}] {row['title']}")
        print(f"stage: {row['coding_agent_stage_or_dimension_cn']}")
        print(f"analogue: {row['coding_agent_analogue_outcome_cn']}")
        print(f"copy: {row['what_to_copy_cn']}")
