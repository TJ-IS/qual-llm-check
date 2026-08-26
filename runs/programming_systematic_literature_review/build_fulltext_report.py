#!/usr/bin/env python3
"""Build a readable synthesis of the locally available full-text subset."""

from __future__ import annotations

import csv
import json
from collections import Counter
from pathlib import Path


RUN_DIR = Path(__file__).resolve().parent
DECISIONS = RUN_DIR / "output_fulltext_local_v1" / "decisions.csv"
OUTPUT = RUN_DIR / "local_fulltext_synthesis.md"


def as_list(value: str) -> list[object]:
    try:
        payload = json.loads(value or "[]")
    except json.JSONDecodeError:
        return []
    return payload if isinstance(payload, list) else []


def join_list(value: str) -> str:
    return "；".join(str(item) for item in as_list(value)) or "无/未明示"


def table(headers: list[str], rows: list[list[object]]) -> str:
    lines = [
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join("---" for _ in headers) + " |",
    ]
    lines.extend(
        "| "
        + " | ".join(str(value).replace("|", "\\|").replace("\n", " ") for value in row)
        + " |"
        for row in rows
    )
    return "\n".join(lines)


def main() -> None:
    with DECISIONS.open("r", encoding="utf-8-sig", newline="") as handle:
        rows = list(csv.DictReader(handle))
    included = [row for row in rows if row["final_include"].lower() == "true"]
    excluded = [row for row in rows if row["final_include"].lower() != "true"]
    actor_counts = Counter(row["actor_type"] for row in included)
    artifact_counts = Counter(row["program_artifact"] for row in included)
    role_counts = Counter(row["evidence_role"] for row in included)
    action_counts: Counter[str] = Counter()
    for row in included:
        action_counts.update(str(value) for value in as_list(row["programming_actions"]))

    lines = [
        "# 本地可得全文子集：最终纳入与概念矩阵",
        "",
        "本报告只覆盖能够在本地 13,910 篇全文库中按记录文件名或 DOI 解析出的论文。它不能代表其余缺失全文候选的最终结论。",
        "",
        "## 流量",
        "",
        f"- 本地候选全文：{len(rows)}",
        f"- 全文最终纳入：{len(included)}",
        f"- 全文排除：{len(excluded)}",
        "",
        "## 纳入构成",
        "",
        table(["主体", "数量"], [[key, value] for key, value in actor_counts.most_common()]),
        "",
        table(["程序制品", "数量"], [[key, value] for key, value in artifact_counts.most_common()]),
        "",
        table(["证据角色", "数量"], [[key, value] for key, value in role_counts.most_common()]),
        "",
        table(["编程行动", "数量"], [[key, value] for key, value in action_counts.most_common()]),
        "",
        "## 全文纳入论文",
    ]
    included.sort(
        key=lambda row: (
            -int(row["year"]) if row["year"].isdigit() else 0,
            row["title"].casefold(),
        )
    )
    for index, row in enumerate(included, start=1):
        lines.extend(
            [
                "",
                f"### {index}. [{row['title']}](fulltext_candidates_local/{row['source_file']})",
                f"- 年份：{row['year']}；来源：{row['journal']}；DOI：{row['doi'] or '无'}",
                f"- 证据角色：{row['evidence_role']}；主体：{row['actor_type']}；制品：{row['program_artifact']}；行动：{join_list(row['programming_actions'])}",
                f"- 编程情境定义：{row['programming_situation_definition_cn']}",
                f"- 任务与场景：{row['task_and_setting_cn']}",
                f"- 方法与分析层级：{row['research_method_cn']}；{row['unit_of_analysis']}",
                f"- 样本/数据：{row['sample_and_data_cn']}",
                f"- 理论/框架：{join_list(row['theory_or_framework_names'])}",
                f"- 自变量：{join_list(row['independent_variables'])}",
                f"- 中介：{join_list(row['mediators'])}",
                f"- 调节：{join_list(row['moderators'])}",
                f"- 因变量：{join_list(row['dependent_variables'])}",
                f"- 主要发现：{row['main_findings_cn']}",
                f"- 人—智能体关系：{row['human_agent_relation_cn'] or '无/不适用'}",
                f"- 样本独立性：{row['sample_independence_note_cn'] or '未发现明确复用证据'}",
                f"- 质量/限制：{row['quality_and_limitations_cn']}",
            ]
        )
    lines.extend(["", "## 全文排除论文"])
    for index, row in enumerate(excluded, start=1):
        lines.extend(
            [
                "",
                f"{index}. [{row['title']}](fulltext_candidates_local/{row['source_file']})（{row['year']}）：{row['exclusion_reason_cn']}",
            ]
        )
    OUTPUT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(
        {
            "local_fulltexts": len(rows),
            "included": len(included),
            "excluded": len(excluded),
            "report": str(OUTPUT),
        }
    )


if __name__ == "__main__":
    main()
