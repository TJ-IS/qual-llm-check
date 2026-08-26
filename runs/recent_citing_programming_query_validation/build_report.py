#!/usr/bin/env python3
"""Build the Markdown report for recent citing-paper query validation."""

from __future__ import annotations

import csv
import json
from collections import Counter
from pathlib import Path


RUN_DIR = Path(__file__).resolve().parent
CANDIDATES_CSV = RUN_DIR / "output_v1" / "candidates.csv"
EVALUATION_JSON = RUN_DIR / "query_recall_evaluation.json"
REPORT_MD = RUN_DIR / "recent_citing_query_validation_report.md"


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def clean_cell(value: str) -> str:
    return (value or "").replace("|", "\\|").replace("\r", " ").replace("\n", " ")


def main() -> None:
    rows = read_csv(CANDIDATES_CSV)
    evaluation = json.loads(EVALUATION_JSON.read_text(encoding="utf-8"))
    likely = sorted(
        [row for row in rows if row["screening_label"] == "likely_direct"],
        key=lambda row: (-int(row["year"]), row["title"].casefold()),
    )
    possible = sorted(
        [row for row in rows if row["screening_label"] == "possible_direct"],
        key=lambda row: (-int(row["year"]), row["title"].casefold()),
    )
    year_counts = Counter(row["year"] for row in likely)
    actor_counts = Counter(row["actor_type"] for row in likely)

    lines = [
        "# 20 篇种子论文的近期施引文献与检索式召回验证",
        "",
        "## 结论",
        "",
        "- 807 条 Scopus 施引记录中有 176 篇发表于 2021–2026，且全部具有摘要。",
        "- DeepSeek V4 Pro 根据题名、摘要和关键词筛出 30 篇 `likely_direct` 和 3 篇 `possible_direct`；这些是全文复核候选，不等同于最终全文纳入。",
        "- 30 篇明确候选中没有一篇来自 Basket 11。近期研究主要迁移到软件工程、人本编程、HCI、计算机教育和少量 AI/NLP 来源。",
        "- 旧扩展检索式召回 25/30（83.3%）；改进后的跨领域高召回检索式召回 30/30（100%），并召回 3 篇不确定项中的 2 篇。",
        "- 唯一没有被高召回式命中的不确定项是一本只写 `software review`、未明确说明是否审查代码的书。为找回它而加入宽泛的 `software review` 会产生大量噪声，适合由引文追踪补充。",
        "- 该验证集来自种子论文施引链，不能证明检索式对整个 Scopus 的绝对召回率；它能证明检索式没有漏掉这批已知的近期知识后继。",
        "",
        "## 近期候选构成",
        "",
        f"- 年份：{'; '.join(f'{year}={year_counts[year]}' for year in sorted(year_counts, reverse=True))}。",
        f"- 行动者：human_only={actor_counts['human_only']}；human_ai={actor_counts['human_ai']}；agent_only={actor_counts['agent_only']}。",
        "- 模型抽取的活动计数：理解 17、编写 14、调试/修复 7、检查/审查 5、生成 3、测试 2、修改/重构 2；一篇可包含多种活动。",
        "",
        "代表性的新近分支包括：",
        "",
        "- OpenAI 生成测试骨架，再由学生补全、验证与修复；",
        "- Ivie 为编程助手刚生成的代码提供定位解释，支持程序员理解与检查；",
        "- 比较开发者与神经代码模型在代码探索中的注意力；",
        "- LLM 识别和解释程序逻辑结构；",
        "- T5 模型生成 SQL、SPARQL 与 Cypher 查询；",
        "- 代码注释、算法标签、眼动模式和执行日志对程序理解或调试的影响；",
        "- 低代码开发、SQL 学习、TDD、结对编程和电子表格调试。",
        "",
        "## 检索式回测",
        "",
        "| 检索式 | 807 条中命中 | 近期 176 条中命中 | 明确候选召回 | 不确定候选召回 | 近期非直接命中 |",
        "|---|---:|---:|---:|---:|---:|",
    ]
    labels = {
        "Q1_title_high_precision": "Q1 标题高精度",
        "Q1_title_abstract_keywords": "Q1 题名摘要关键词",
        "Q2_legacy_expanded": "Q2 旧扩展式",
        "Q8_ais_professional_refined": "Q8 AIS 专业词式",
        "Q3_modern_agent_supplement": "Q3 现代智能体补充式",
        "Q9_cross_domain_high_recall": "Q9 跨领域高召回式",
    }
    for key, value in evaluation["variants"].items():
        lines.append(
            f"| {labels[key]} | {value['all_807_hits']} | "
            f"{value['recent_176_hits']} | "
            f"{value['likely_direct_30_hits']}/30 "
            f"({value['likely_direct_recall']:.1%}) | "
            f"{value['possible_direct_3_hits']}/3 | "
            f"{value['recent_not_direct_hits']} |"
        )

    lines.extend(
        [
            "",
            "高召回式在 176 篇近期记录中命中 55 篇，其中 30 篇明确相关、2 篇不确定、23 篇非直接相关。它的作用是生成可控的全文筛选池，而不是直接给出最终文献集。",
            "",
            "## 推荐的 Scopus 分块检索式",
            "",
            "建议四个词块分别运行、分别保存命中数，最后按 EID、DOI 和题名去重。这样比一条巨型表达式更容易审计。",
            "",
            "### A. 编写、理解与编程任务",
            "",
            "```text",
            "TITLE-ABS-KEY(",
            '  "program comprehension" OR "code comprehension" OR',
            '  "software comprehension" OR "program understanding" OR',
            '  "code understanding" OR "code reading" OR "reading source code" OR',
            '  "code exploration" OR',
            '  "programming task*" OR "coding task*" OR',
            '  "programming performance" OR "programmer performance" OR',
            '  "programming productivity" OR "programming practice*" OR',
            '  "programming pattern*" OR "programming environment*" OR',
            '  "introductory programming" OR "programming education" OR',
            '  "novice programmer*" OR "pair programming" OR',
            '  "test-driven development" OR "execution log*"',
            ")",
            "```",
            "",
            "### B. 检查、调试、修复、修改与测试",
            "",
            "```text",
            "TITLE-ABS-KEY(",
            '  "code review" OR "code inspection" OR "code inspecting" OR',
            '  "program debugging" OR "code debugging" OR "source code debugging" OR',
            '  (debug* W/5 (program* OR code OR software)) OR',
            '  "bug fixing" OR "fault localization" OR "fault localisation" OR',
            '  "program repair" OR "test generation" OR "test skeleton*" OR',
            '  "unit test generation" OR "code modification" OR',
            '  "program modification" OR "code refactoring"',
            ")",
            "```",
            "",
            "### C. 查询、电子表格、终端用户与低代码编程",
            "",
            "```text",
            "TITLE-ABS-KEY(",
            '  "query formulation" OR "query development" OR "query reuse" OR',
            '  "query complexity" OR "structured query language*" OR',
            '  "text-to-SQL" OR "text to SQL" OR "text-to-SPARQL" OR',
            '  "text-to-Cypher" OR',
            '  (SQL W/8 (query OR learn* OR teach* OR error* OR debug* OR',
            '             writ* OR formulat* OR skill*)) OR',
            '  "spreadsheet error*" OR "spreadsheet testing" OR',
            '  "spreadsheet development" OR "spreadsheet debugging" OR',
            '  "spreadsheet programming" OR "spreadsheet formula*" OR',
            '  "end-user programming" OR "low-code" OR "low code" OR',
            '  "visual programming"',
            ")",
            "```",
            "",
            "### D. 代码生成、补全与编程智能体",
            "",
            "```text",
            "TITLE-ABS-KEY(",
            '  "code generation" OR "generate code" OR "generating code" OR',
            '  "generated code" OR "just-generated code" OR',
            '  "code completion" OR "code autocomplete" OR',
            '  "code autocompletion" OR "code suggestion*" OR',
            '  "AI-assisted programming" OR "AI-assisted coding" OR',
            '  "AI-assisted software development" OR "AI pair programmer*" OR',
            '  "coding agent*" OR "programming agent*" OR',
            '  "coding assistant*" OR "programming assistant*" OR',
            '  "code assistant*" OR "GitHub Copilot" OR "OpenAI Codex" OR',
            '  (("large language model*" OR LLM* OR ChatGPT OR "generative AI")',
            '   W/15',
            '   (programming OR coding OR "source code" OR "code generation" OR',
            '    "code completion" OR "program comprehension" OR',
            '    "program repair" OR "test generation" OR SQL))',
            ")",
            "```",
            "",
            "用于近期综述时，可在每个词块后追加 `AND PUBYEAR > 2015`。识别阶段不建议先限制来源或文献类型；来源和文献类型应作为筛选字段保留，而不是检索前硬删除。",
            "",
            "## 为什么仅靠施引检索仍然不够",
            "",
            "807 条施引记录中：",
            "",
            "- 没有出现字面短语 `code completion`、`code autocomplete` 或 `code autocompletion`；",
            "- 没有出现 `GitHub Copilot`，只有 Ivie 的元数据出现一般的 `Copilot`；",
            "- 只有 5 篇被现代智能体补充词块捕捉。",
            "",
            "因此，前向追引能发现程序理解、TDD、查询、低代码和部分 LLM 桥接研究，但不能替代 D 词块对代码补全、Copilot、Codex 和 coding agents 的独立全库检索。",
            "",
            "## 30 篇摘要明确相关的近期施引文献",
            "",
            "| 年份 | 标题 | 来源 | 行动者 | 摘要判断概括 |",
            "|---:|---|---|---|---|",
        ]
    )
    for row in likely:
        lines.append(
            f"| {row['year']} | {clean_cell(row['title'])} | "
            f"{clean_cell(row['journal'])} | {row['actor_type']} | "
            f"{clean_cell(row['research_summary_cn'])} |"
        )

    lines.extend(
        [
            "",
            "## 3 篇需要全文确认的边界文献",
            "",
            "| 年份 | 标题 | 来源 | 为什么不确定 |",
            "|---:|---|---|---|",
        ]
    )
    for row in possible:
        lines.append(
            f"| {row['year']} | {clean_cell(row['title'])} | "
            f"{clean_cell(row['journal'])} | "
            f"{clean_cell(row['decision_reason_cn'])} |"
        )

    lines.extend(
        [
            "",
            "## 解释边界",
            "",
            "这次 30/30 是对“20 篇旧种子的近期施引后继”的回溯性召回，不是对全体近期编程文献的绝对召回证明。更可靠的正式流程应是：",
            "",
            "1. 用 A–D 四个词块在 Scopus 全库独立检索；",
            "2. 用 20 篇种子的前向与后向引文补充；",
            "3. 对全库检索新增而施引链未发现的代码补全/智能体论文建立第二个验证集；",
            "4. 用 DeepSeek 做题名摘要高召回筛选，再全文确认；",
            "5. 报告各轨新增文献数以及每条轨道独有的最终纳入文献。",
            "",
        ]
    )
    REPORT_MD.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {REPORT_MD} with {len(likely)} likely and {len(possible)} possible records")


if __name__ == "__main__":
    main()
