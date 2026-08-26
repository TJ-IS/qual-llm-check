#!/usr/bin/env python3
"""Build auditable CSV and Markdown summaries from the two metadata screens."""

from __future__ import annotations

import csv
import json
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any


RUN_DIR = Path(__file__).resolve().parent
MANIFEST_PATH = RUN_DIR / "input_manifest.csv"
STAGE1_PATH = RUN_DIR / "output_stage1_batch_v2" / "decisions.csv"
STAGE2_PATH = RUN_DIR / "output_stage2_batch_v2" / "decisions.csv"
AUDIT_PATH = RUN_DIR / "screening_audit.csv"
REPORT_PATH = RUN_DIR / "title_abstract_screening_results.md"
CANDIDATES_PATH = RUN_DIR / "title_abstract_candidates.md"


def read_csv(path: Path) -> list[dict[str, str]]:
    if not path.is_file():
        return []
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def json_list(value: str) -> list[str]:
    try:
        payload = json.loads(value or "[]")
    except json.JSONDecodeError:
        return []
    return [str(item) for item in payload] if isinstance(payload, list) else []


def markdown_table(headers: list[str], rows: list[list[Any]]) -> str:
    lines = [
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join("---" for _ in headers) + " |",
    ]
    for row in rows:
        lines.append(
            "| "
            + " | ".join(str(value).replace("|", "\\|").replace("\n", " ") for value in row)
            + " |"
        )
    return "\n".join(lines)


def year_group(value: str) -> str:
    try:
        year = int(value)
    except ValueError:
        return "unknown"
    if year >= 2021:
        return "2021–2026"
    if year >= 2011:
        return "2011–2020"
    if year >= 2001:
        return "2001–2010"
    return "≤2000"


def main() -> None:
    manifest = {row["source_file"]: row for row in read_csv(MANIFEST_PATH)}
    stage1 = read_csv(STAGE1_PATH)
    stage2 = {row["source_file"]: row for row in read_csv(STAGE2_PATH)}
    if not stage1:
        raise RuntimeError(f"No completed stage-one report at {STAGE1_PATH}")

    audit_rows: list[dict[str, str]] = []
    for first in stage1:
        source_file = first["source_file"]
        meta = manifest.get(source_file, {})
        second = stage2.get(source_file, {})
        label1 = first.get("screening_label", "")
        label2 = second.get("screening_label", "")
        if label1 == "exclude":
            status = "stage1_exclude"
        elif not label2:
            status = "awaiting_stage2"
        elif label2 == "include_candidate":
            status = "two_pass_include"
        elif label2 == "uncertain":
            status = "stage2_uncertain_fulltext_required"
        else:
            status = "screening_disagreement_fulltext_required"
        audit_rows.append(
            {
                "source_file": source_file,
                "record_id": meta.get("record_id", first.get("article_id", "")),
                "eid": meta.get("eid", ""),
                "doi": meta.get("doi", first.get("doi", "")),
                "title": first.get("title", ""),
                "year": first.get("year", ""),
                "source_title": first.get("journal", ""),
                "retrieval_channels": meta.get("retrieval_channels", ""),
                "local_fulltext_files": meta.get("local_fulltext_files", ""),
                "stage1_label": label1,
                "stage2_label": label2,
                "screening_status": status,
                "actor_type": second.get("actor_type") or first.get("actor_type", ""),
                "program_artifact": second.get("program_artifact")
                or first.get("program_artifact", ""),
                "programming_actions": second.get("programming_actions")
                or first.get("programming_actions", ""),
                "study_type": second.get("study_type") or first.get("study_type", ""),
                "unit_of_analysis": second.get("unit_of_analysis")
                or first.get("unit_of_analysis", ""),
                "theory_or_framework_names": second.get("theory_or_framework_names")
                or first.get("theory_or_framework_names", ""),
                "research_summary_cn": second.get("research_summary_cn")
                or first.get("research_summary_cn", ""),
                "stage1_reason_cn": first.get("decision_reason_cn", ""),
                "stage2_reason_cn": second.get("decision_reason_cn", ""),
                "stage1_evidence_cn": first.get("metadata_evidence_cn", ""),
                "stage2_evidence_cn": second.get("metadata_evidence_cn", ""),
                "stage1_confidence": first.get("confidence", ""),
                "stage2_confidence": second.get("confidence", ""),
            }
        )

    fields = list(audit_rows[0])
    with AUDIT_PATH.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(audit_rows)

    candidates = [row for row in audit_rows if row["stage1_label"] != "exclude"]
    two_pass = [
        row for row in audit_rows if row["screening_status"] == "two_pass_include"
    ]
    label_counts = Counter(row["stage1_label"] for row in audit_rows)
    stage2_counts = Counter(row["stage2_label"] for row in candidates)
    status_counts = Counter(row["screening_status"] for row in audit_rows)
    actor_counts = Counter(row["actor_type"] for row in two_pass)
    artifact_counts = Counter(row["program_artifact"] for row in two_pass)
    study_counts = Counter(row["study_type"] for row in two_pass)
    unit_counts = Counter(row["unit_of_analysis"] for row in two_pass)
    period_counts = Counter(year_group(row["year"]) for row in two_pass)
    action_counts: Counter[str] = Counter()
    for row in two_pass:
        action_counts.update(json_list(row["programming_actions"]))
    source_counts = Counter(row["source_title"] for row in two_pass)
    channel_counts: Counter[str] = Counter()
    for row in audit_rows:
        channel_counts.update(
            value for value in row["retrieval_channels"].split(";") if value
        )

    report = [
        "# 题名—摘要—关键词筛选结果",
        "",
        "本报告是可重复生成的阶段性结果。题录筛选只决定是否进入全文复核，不能替代最终纳入判断。",
        "",
        "## 流量",
        "",
        f"- 去重后的输入记录：{len(manifest):,}",
        f"- 第一轮已完成：{len(audit_rows):,}",
        f"- 第一轮候选（include + uncertain）：{len(candidates):,}",
        f"- 第一轮排除：{label_counts.get('exclude', 0):,}",
        f"- 第二轮已完成：{len(stage2):,}",
        f"- 两轮均纳入：{len(two_pass):,}",
        f"- 第一轮保留、第二轮排除（需全文裁决）：{status_counts.get('screening_disagreement_fulltext_required', 0):,}",
        f"- 第二轮不确定（需全文裁决）：{status_counts.get('stage2_uncertain_fulltext_required', 0):,}",
        "",
        markdown_table(
            ["第一轮标签", "数量"],
            [[key, value] for key, value in label_counts.most_common()],
        ),
        "",
        markdown_table(
            ["第二轮标签（只对第一轮候选）", "数量"],
            [[key, value] for key, value in stage2_counts.most_common()],
        ),
        "",
        "## 检索渠道覆盖",
        "",
        markdown_table(
            ["渠道", "去重后涉及记录数"],
            [[key, value] for key, value in channel_counts.most_common()],
        ),
        "",
        "## 两轮一致纳入记录的题录概览",
        "",
        "### 主体",
        "",
        markdown_table(
            ["主体", "数量"], [[key, value] for key, value in actor_counts.most_common()]
        ),
        "",
        "### 程序制品",
        "",
        markdown_table(
            ["制品", "数量"], [[key, value] for key, value in artifact_counts.most_common()]
        ),
        "",
        "### 编程行动",
        "",
        markdown_table(
            ["行动", "数量"], [[key, value] for key, value in action_counts.most_common()]
        ),
        "",
        "### 研究类型",
        "",
        markdown_table(
            ["研究类型", "数量"], [[key, value] for key, value in study_counts.most_common()]
        ),
        "",
        "### 分析层级",
        "",
        markdown_table(
            ["层级", "数量"], [[key, value] for key, value in unit_counts.most_common()]
        ),
        "",
        "### 年代",
        "",
        markdown_table(
            ["年代", "数量"], [[key, value] for key, value in period_counts.most_common()]
        ),
        "",
        "### 候选最多的来源（前 25）",
        "",
        markdown_table(
            ["来源", "数量"],
            [[key or "(missing)", value] for key, value in source_counts.most_common(25)],
        ),
        "",
        "## 解释限制",
        "",
        "- 这是题录阶段的高召回结果；主体、方法、层级和理论均可能因摘要信息不足而在全文阶段修正。",
        "- `agent_only` 技术评测、`human_ai` 交互研究与 `human_only` 认知/行为研究将在综合时分层，不直接合并。",
        "- 第一轮与第二轮冲突项不会自动排除，而进入全文裁决。",
    ]
    REPORT_PATH.write_text("\n".join(report) + "\n", encoding="utf-8")

    grouped: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in candidates:
        grouped[row["actor_type"] or "unclear"].append(row)
    candidate_lines = [
        "# 全部题录候选",
        "",
        "以下记录尚未经过最终全文纳入判断。",
    ]
    actor_order = ["human_ai", "human_only", "agent_only", "unclear"]
    for actor in actor_order + sorted(set(grouped) - set(actor_order)):
        rows = sorted(
            grouped.get(actor, []),
            key=lambda row: (
                -int(row["year"]) if row["year"].isdigit() else 0,
                row["title"].casefold(),
            ),
        )
        if not rows:
            continue
        candidate_lines.extend(["", f"## {actor}（{len(rows)}）"])
        for index, row in enumerate(rows, start=1):
            actions = "、".join(json_list(row["programming_actions"])) or "未明"
            candidate_lines.extend(
                [
                    "",
                    f"### {index}. {row['title']}",
                    f"- 年份：{row['year']}；来源：{row['source_title']}；DOI：{row['doi'] or '无'}",
                    f"- 行动：{actions}；制品：{row['program_artifact']}；研究类型：{row['study_type']}；层级：{row['unit_of_analysis']}",
                    f"- 题录概要：{row['research_summary_cn']}",
                    f"- 筛选状态：{row['screening_status']}",
                ]
            )
    CANDIDATES_PATH.write_text("\n".join(candidate_lines) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "audit_rows": len(audit_rows),
                "stage1_candidates": len(candidates),
                "stage2_rows": len(stage2),
                "audit_csv": str(AUDIT_PATH),
                "report": str(REPORT_PATH),
                "candidates": str(CANDIDATES_PATH),
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
