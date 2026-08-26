#!/usr/bin/env python3
"""Describe the deduplicated identification pool before relevance screening."""

from __future__ import annotations

import csv
import json
from collections import Counter
from pathlib import Path


RUN_DIR = Path(__file__).resolve().parent
MANIFEST = RUN_DIR / "input_manifest.csv"
PREPARATION = RUN_DIR / "input_preparation_summary.json"
OUTPUT = RUN_DIR / "identification_pool_analysis.md"


def table(headers: list[str], rows: list[list[object]]) -> str:
    lines = [
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join("---" for _ in headers) + " |",
    ]
    lines.extend(
        "| " + " | ".join(str(value).replace("|", "\\|") for value in row) + " |"
        for row in rows
    )
    return "\n".join(lines)


def main() -> None:
    with MANIFEST.open("r", encoding="utf-8-sig", newline="") as handle:
        rows = list(csv.DictReader(handle))
    preparation = json.loads(PREPARATION.read_text(encoding="utf-8"))
    years = Counter(row["year"] or "(missing)" for row in rows)
    sources = Counter(row["source_title"] or "(missing)" for row in rows)
    documents_by_channel_combo = Counter(
        row["retrieval_channels"].replace(";", " + ") for row in rows
    )
    recent = sum((row["year"].isdigit() and int(row["year"]) >= 2021) for row in rows)
    lines = [
        "# 识别池分析",
        "",
        "## 流量与完整性",
        "",
        f"- 原始输入行：{sum(preparation['source_rows'].values()):,}（各渠道相加，含重叠）",
        f"- 去重后题录：{len(rows):,}",
        f"- 具有摘要：{preparation['records_with_abstract']:,}",
        f"- 缺摘要：{preparation['records_without_abstract']:,}",
        f"- 2021–2026：{recent:,}",
        "",
        table(
            ["原始渠道", "输入行"],
            [[key, value] for key, value in preparation["source_rows"].items()],
        ),
        "",
        "## 渠道重叠",
        "",
        table(
            ["去重后渠道组合", "记录数"],
            [[key, value] for key, value in documents_by_channel_combo.most_common()],
        ),
        "",
        "## 年份（前 20 个高频年份）",
        "",
        table(
            ["年份", "题录数"],
            [[key, value] for key, value in years.most_common(20)],
        ),
        "",
        "## 来源（前 30）",
        "",
        table(
            ["来源", "题录数"],
            [[key, value] for key, value in sources.most_common(30)],
        ),
        "",
        "## 解释",
        "",
        "识别池不是相关文献集。权威来源概念检索会包含大量因短语多义、技术工具或项目背景造成的噪声；施引记录也只证明引用关系。所有 5,642 条必须走同一 eligibility criteria。",
    ]
    OUTPUT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(OUTPUT)


if __name__ == "__main__":
    main()
