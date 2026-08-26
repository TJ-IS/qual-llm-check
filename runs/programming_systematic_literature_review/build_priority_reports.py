#!/usr/bin/env python3
"""Create focused reports for the human-AI, recent-human, and agent-only branches."""

from __future__ import annotations

import csv
from pathlib import Path


RUN_DIR = Path(__file__).resolve().parent
AUDIT = RUN_DIR / "screening_audit.csv"


def read_rows() -> list[dict[str, str]]:
    with AUDIT.open("r", encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def write_group(name: str, title: str, rows: list[dict[str, str]]) -> None:
    rows.sort(
        key=lambda row: (
            -int(row["year"]) if row["year"].isdigit() else 0,
            row["title"].casefold(),
        )
    )
    fields = list(rows[0]) if rows else []
    csv_path = RUN_DIR / f"{name}.csv"
    with csv_path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)
    lines = [
        f"# {title}",
        "",
        f"共 {len(rows)} 条；均为两轮题名—摘要—关键词判断一致纳入，尚不等于最终全文纳入。",
    ]
    for index, row in enumerate(rows, start=1):
        lines.extend(
            [
                "",
                f"## {index}. {row['title']}",
                f"- 年份：{row['year']}；来源：{row['source_title']}；DOI：{row['doi'] or '无'}",
                f"- 主体：{row['actor_type']}；制品：{row['program_artifact']}；行动：{row['programming_actions']}",
                f"- 第二轮理由：{row['stage2_reason_cn']}",
                f"- 第二轮证据：{row['stage2_evidence_cn']}",
            ]
        )
    (RUN_DIR / f"{name}.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    rows = read_rows()
    two_pass = [
        row for row in rows if row["screening_status"] == "two_pass_include"
    ]
    human_ai = [row for row in two_pass if row["actor_type"] == "human_ai"]
    recent_human = [
        row
        for row in two_pass
        if row["actor_type"] == "human_only"
        and row["year"].isdigit()
        and int(row["year"]) >= 2021
    ]
    agent_only = [row for row in two_pass if row["actor_type"] == "agent_only"]
    write_group(
        "two_pass_human_ai",
        "两轮一致的 human–AI 直接编程候选",
        human_ai,
    )
    write_group(
        "two_pass_recent_human",
        "2021–2026 两轮一致的人类直接编程候选",
        recent_human,
    )
    write_group(
        "two_pass_agent_only",
        "两轮一致的 agent-only 直接编程候选",
        agent_only,
    )
    print(
        {
            "human_ai": len(human_ai),
            "recent_human_only": len(recent_human),
            "agent_only": len(agent_only),
        }
    )


if __name__ == "__main__":
    main()
