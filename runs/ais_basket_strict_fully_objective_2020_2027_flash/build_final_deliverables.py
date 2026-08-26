#!/usr/bin/env python3
"""Build validated deliverables and compare the strict rescreen with the prior 231-paper screen."""

from __future__ import annotations

import csv
import json
from collections import Counter
from pathlib import Path
from typing import Any


RUN_DIR = Path(__file__).resolve().parent
ROOT = RUN_DIR.parents[1]
OLD_JSONL = ROOT / "runs" / "ais_basket_objective_software_psych_theory_2020_2027_flash" / "output_v1" / "decisions.jsonl"
STAGE1_JSONL = RUN_DIR / "output_stage1" / "decisions.jsonl"
STAGE2_JSONL = RUN_DIR / "output_stage2" / "decisions.jsonl"
STAGE3_JSONL = RUN_DIR / "output_stage3" / "decisions.jsonl"
OUT = RUN_DIR / "deliverables"
ANCHORS = {
    "28352_2025_hypercars-using-hyperbolic-embeddings-for-generating-hierarchical-contextual-situations-in-conte.md": (True, True),
    "28480_2023_augmenting-social-bot-detection-with-crowd-generated-labels.md": (True, True),
    "28508_2023_pushing-yourself-harder-the-effects-of-mobile-touch-modes-on-users-self-regulation.md": (False, False),
    "28234_2022_achieving-a-balance-between-privacy-protection-and-data-collection-a-field-experimental-examinat.md": (False, False),
    "28156_2025_improving-students-argumentation-skills-using-dynamic-machine-learningbased-modeling.md": (False, False),
}


def load_latest(path: Path) -> tuple[dict[str, dict[str, Any]], int]:
    rows: dict[str, dict[str, Any]] = {}
    lines = 0
    with path.open("r", encoding="utf-8") as handle:
        for line in handle:
            if not line.strip():
                continue
            lines += 1
            row = json.loads(line)
            rows[str(row["source_file"])] = row
    return rows, lines


def write_csv(path: Path, rows: list[dict[str, Any]], fields: list[str]) -> None:
    with path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def metric_names(row: dict[str, Any]) -> str:
    result = []
    for metric in row.get("qualifying_metrics") or []:
        if isinstance(metric, dict) and metric.get("name"):
            result.append(str(metric["name"]))
    return " | ".join(result)


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    old, old_lines = load_latest(OLD_JSONL)
    stage1, stage1_lines = load_latest(STAGE1_JSONL)
    stage2, stage2_lines = load_latest(STAGE2_JSONL)
    stage3, stage3_lines = load_latest(STAGE3_JSONL)

    old_set = {source for source, row in old.items() if row.get("base_match") is True}
    s1_set = {source for source, row in stage1.items() if row.get("strict_match") is True}
    objective_final_set = {source for source, row in stage2.items() if row.get("confirmed_strict_match") is True}
    artifact_old_pass_set = {
        source for source, row in old.items()
        if bool((row.get("software_artifact") or {}).get("pass"))
    }
    artifact_reconciled_set = {source for source, row in stage3.items() if row.get("artifact_confirmed") is True}
    final_set = objective_final_set & (artifact_old_pass_set | artifact_reconciled_set)
    removed_old = old_set - final_set
    added_new = final_set - old_set
    retained_old = old_set & final_set
    stage2_removed = s1_set - objective_final_set
    stage3_removed = objective_final_set - final_set

    anchor_checks = {}
    for source, (expected_s1, expected_final) in ANCHORS.items():
        actual_s1 = bool(stage1.get(source, {}).get("strict_match"))
        actual_final = source in final_set
        anchor_checks[source] = {
            "expected_stage1": expected_s1,
            "actual_stage1": actual_s1,
            "expected_final": expected_final,
            "actual_final": actual_final,
            "pass": actual_s1 == expected_s1 and actual_final == expected_final,
        }

    final_rows = []
    for source in sorted(final_set, key=lambda item: (str(stage2[item].get("year")), str(stage2[item].get("journal")), str(stage2[item].get("title")))):
        row = stage2[source]
        final_rows.append({
            "record_id": row.get("record_id"),
            "source_file": source,
            "title": row.get("title"),
            "authors": row.get("authors"),
            "year": row.get("year"),
            "journal": row.get("journal"),
            "doi": row.get("doi"),
            "objective_status": row.get("objective_status"),
            "core_role": row.get("core_role"),
            "confidence": row.get("confidence"),
            "qualifying_metrics": metric_names(row),
            "software_artifact_cn": row.get("software_artifact_cn"),
            "audit_reason_cn": row.get("audit_reason_cn"),
            "old_base_match": source in old_set,
        })
    write_csv(
        OUT / f"final_strict_{len(final_set)}_articles.csv",
        final_rows,
        ["record_id", "source_file", "title", "authors", "year", "journal", "doi", "objective_status", "core_role", "confidence", "qualifying_metrics", "software_artifact_cn", "audit_reason_cn", "old_base_match"],
    )

    audit_removed_rows = []
    for source in sorted(stage2_removed):
        row = stage2[source]
        failed_gates = [key for key, value in (row.get("gates") or {}).items() if value is False]
        audit_removed_rows.append({
            "record_id": row.get("record_id"),
            "source_file": source,
            "title": row.get("title"),
            "year": row.get("year"),
            "journal": row.get("journal"),
            "objective_status": row.get("objective_status"),
            "core_role": row.get("core_role"),
            "failed_gates": " | ".join(failed_gates),
            "audit_reason_cn": row.get("audit_reason_cn"),
        })
    write_csv(
        OUT / f"stage2_removed_{len(stage2_removed)}_articles.csv",
        audit_removed_rows,
        ["record_id", "source_file", "title", "year", "journal", "objective_status", "core_role", "failed_gates", "audit_reason_cn"],
    )

    stage3_removed_rows = []
    for source in sorted(stage3_removed):
        row = stage3[source]
        failed_gates = [key for key, value in (row.get("gates") or {}).items() if value is False]
        stage3_removed_rows.append({
            "record_id": row.get("record_id"),
            "source_file": source,
            "title": row.get("title"),
            "year": row.get("year"),
            "journal": row.get("journal"),
            "artifact_status": row.get("artifact_status"),
            "failed_gates": " | ".join(failed_gates),
            "audit_reason_cn": row.get("audit_reason_cn"),
        })
    write_csv(
        OUT / f"stage3_artifact_removed_{len(stage3_removed)}_articles.csv",
        stage3_removed_rows,
        ["record_id", "source_file", "title", "year", "journal", "artifact_status", "failed_gates", "audit_reason_cn"],
    )

    union = sorted(old_set | final_set)
    comparison_rows = []
    for source in union:
        row = stage2.get(source) or stage1.get(source) or old[source]
        old_match = source in old_set
        final_match = source in final_set
        transition = "retained" if old_match and final_match else "removed_from_old" if old_match else "newly_added"
        comparison_rows.append({
            "record_id": row.get("record_id"),
            "source_file": source,
            "title": row.get("title"),
            "year": row.get("year"),
            "journal": row.get("journal"),
            "old_base_match": old_match,
            "new_stage1_match": source in s1_set,
            "new_final_match": final_match,
            "transition": transition,
            "new_objective_status": stage2.get(source, stage1.get(source, {})).get("objective_status"),
            "new_reason_cn": stage2.get(source, {}).get("audit_reason_cn") or stage1.get(source, {}).get("decision_reason_cn") or "",
        })
    write_csv(
        OUT / f"old231_vs_new{len(final_set)}_comparison.csv",
        comparison_rows,
        ["record_id", "source_file", "title", "year", "journal", "old_base_match", "new_stage1_match", "new_final_match", "transition", "new_objective_status", "new_reason_cn"],
    )

    stage2_removed_status = Counter(str(stage2[source].get("objective_status")) for source in stage2_removed)
    failed_gate_counts = Counter()
    for source in stage2_removed:
        for key, value in (stage2[source].get("gates") or {}).items():
            if value is False:
                failed_gate_counts[key] += 1

    summary = {
        "input_articles": len(stage1),
        "stage1_matches": len(s1_set),
        "stage2_audited": len(stage2),
        "objective_measurement_matches_after_stage2": len(objective_final_set),
        "stage3_artifact_conflicts_audited": len(stage3),
        "stage3_artifact_conflicts_confirmed": len(artifact_reconciled_set),
        "stage3_artifact_conflicts_removed": len(stage3_removed),
        "final_matches": len(final_set),
        "stage2_removed": len(stage2_removed),
        "prior_matches": len(old_set),
        "retained_from_prior": len(retained_old),
        "removed_from_prior": len(removed_old),
        "newly_added_vs_prior": len(added_new),
        "final_year_counts": dict(sorted(Counter(str(stage2[source].get("year")) for source in final_set).items())),
        "final_journal_counts": dict(sorted(Counter(str(stage2[source].get("journal")) for source in final_set).items())),
        "final_objective_status_counts": dict(sorted(Counter(str(stage2[source].get("objective_status")) for source in final_set).items())),
        "stage2_removed_status_counts": dict(sorted(stage2_removed_status.items())),
        "stage2_failed_gate_counts": dict(sorted(failed_gate_counts.items())),
        "stage3_artifact_status_counts": dict(sorted(Counter(str(row.get("artifact_status")) for row in stage3.values()).items())),
        "anchor_checks": anchor_checks,
        "validation": {
            "old_jsonl_lines": old_lines,
            "old_unique_articles": len(old),
            "stage1_jsonl_lines": stage1_lines,
            "stage1_unique_articles": len(stage1),
            "stage2_jsonl_lines": stage2_lines,
            "stage2_unique_articles": len(stage2),
            "stage3_jsonl_lines": stage3_lines,
            "stage3_unique_articles": len(stage3),
            "stage2_is_exactly_stage1_positive_set": set(stage2) == s1_set,
            "stage3_is_exactly_artifact_disagreement_set": set(stage3) == (objective_final_set - artifact_old_pass_set),
            "final_is_subset_of_stage1": final_set <= s1_set,
            "final_all_pass_objective_audit": final_set <= objective_final_set,
            "final_all_pass_artifact_evidence": final_set <= (artifact_old_pass_set | artifact_reconciled_set),
            "all_anchor_checks_pass": all(value["pass"] for value in anchor_checks.values()),
        },
    }
    (OUT / "comparison_summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    lines = [
        "# 2020–2027 完全客观指标严格重筛结果",
        "",
        "## 最终结果",
        "",
        f"- 本地全文输入：{len(stage1):,} 篇。",
        f"- 第一阶段严格初筛：{len(s1_set)} 篇。",
        f"- 第二阶段客观测量反向审计：确认 {len(objective_final_set)} 篇，推翻 {len(stage2_removed)} 篇。",
        f"- 第三阶段对 {len(stage3)} 个新旧制品边界冲突项仲裁：确认 {len(artifact_reconciled_set)} 篇，排除 {len(stage3_removed)} 篇纯算法/方法。",
        f"- 最终同时满足严格客观测量与明确软件制品要求：{len(final_set)} 篇。",
        f"- 旧版 231 篇与新最终清单交集：{len(retained_old)} 篇；旧版删除：{len(removed_old)} 篇；全量重筛新补入：{len(added_new)} 篇。",
        "",
        f"## 最终 {len(final_set)} 篇按期刊",
        "",
    ]
    for journal, count in summary["final_journal_counts"].items():
        lines.append(f"- {journal}: {count}")
    lines.extend(["", f"## 最终 {len(final_set)} 篇按年份", ""])
    for year, count in summary["final_year_counts"].items():
        lines.append(f"- {year}: {count}")
    lines.extend(["", "## 二审推翻原因概况", ""])
    for status, count in summary["stage2_removed_status_counts"].items():
        lines.append(f"- {status}: {count}")
    lines.extend(["", "## 校准检查", ""])
    for source, check in anchor_checks.items():
        lines.append(f"- {source}: {'PASS' if check['pass'] else 'FAIL'}")
    lines.extend([
        "",
        "## 交付文件",
        "",
        f"- `final_strict_{len(final_set)}_articles.csv`: 最终严格清单及逐篇指标、制品和审计理由。",
        f"- `stage2_removed_{len(stage2_removed)}_articles.csv`: 客观测量二审推翻文章与具体失败门槛。",
        f"- `stage3_artifact_removed_{len(stage3_removed)}_articles.csv`: 制品边界仲裁排除的纯算法/方法文章。",
        f"- `old231_vs_new{len(final_set)}_comparison.csv`: 旧 231 与新最终集合的逐篇变化。",
        "- `comparison_summary.json`: 统计与机器可读验证结果。",
    ])
    (OUT / "final_report_cn.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
