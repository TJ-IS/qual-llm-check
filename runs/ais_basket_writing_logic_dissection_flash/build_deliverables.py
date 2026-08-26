#!/usr/bin/env python3
"""Validate analyses, render readable per-article files, and build evidence summaries."""

from __future__ import annotations

import csv
import json
import math
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


RUN_DIR = Path(__file__).resolve().parent
STAGE1_DIR = RUN_DIR / "output_stage1_all231"
STAGE2_DIR = RUN_DIR / "output_stage2_isr57"
DELIVERY_DIR = RUN_DIR / "deliverables"

LABELS = {
    "central_question_cn": "核心问题",
    "artifact_and_design_cn": "制品与设计",
    "objective_outcomes_cn": "客观结果",
    "core_contribution_cn": "核心贡献",
    "whole_argument_in_one_paragraph_cn": "整篇论证链",
    "paper_archetype_reason_cn": "论文主类型判定",
    "dominant_writing_arc_reason_cn": "主导写作弧线判定",
    "overall_sequence_cn": "研究阶段总序列",
    "knowledge_bases": "知识/理论基础",
    "theory_design_coupling": "理论—设计耦合",
    "coupling_reason_cn": "耦合判定理由",
    "translation_chain_cn": "理论到设计翻译链",
    "verified_macro_scaffold_cn": "核实后的宏观骨架",
    "single_sentence_description_of_isr_routine_cn": "本篇 ISR 套路的一句话概括",
    "limitations_cn": "分析限制",
}


def load_articles(directory: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for path in sorted((directory / "articles").glob("*.json")):
        row = json.loads(path.read_text(encoding="utf-8"))
        row["_article_json"] = str(path)
        rows.append(row)
    return rows


def scalar(value: Any) -> str:
    if value is None:
        return ""
    if isinstance(value, bool):
        return "是" if value else "否"
    return str(value)


def render_generic(value: Any, level: int = 3) -> list[str]:
    lines: list[str] = []
    if isinstance(value, dict):
        for key, item in value.items():
            label = LABELS.get(key, key)
            if isinstance(item, (dict, list)):
                lines.extend([f"{'#' * min(level, 6)} {label}", ""])
                lines.extend(render_generic(item, level + 1))
            else:
                lines.extend([f"- {label}：{scalar(item)}", ""])
    elif isinstance(value, list):
        if not value:
            lines.extend(["（空）", ""])
        for index, item in enumerate(value, start=1):
            if isinstance(item, dict):
                title = item.get("locator") or item.get("name_cn") or item.get("claim_cn") or item.get("step") or index
                lines.extend([f"{'#' * min(level, 6)} {index}. {title}", ""])
                lines.extend(render_generic(item, level + 1))
            else:
                lines.extend([f"{index}. {scalar(item)}", ""])
    else:
        lines.extend([scalar(value), ""])
    return lines


def render_stage1(row: dict[str, Any]) -> str:
    lines = [
        f"# {row.get('title')}", "",
        f"- 作者：{row.get('authors')}",
        f"- 年份 / 期刊：{row.get('year')} / {row.get('journal')}",
        f"- DOI：{row.get('doi')}",
        f"- 源文件：{row.get('source_file')}",
        f"- 论文主类型：{row.get('paper_archetype')}",
        f"- 主导写作弧线：{row.get('dominant_writing_arc')}",
        f"- 置信度：{row.get('confidence')}", "",
        "## 文章级论证概况", "",
    ]
    lines.extend(render_generic(row.get("article_level_summary") or {}, 3))
    lines.extend(["## 类型与写作弧线判定", ""])
    lines.extend(render_generic({
        "paper_archetype_reason_cn": row.get("paper_archetype_reason_cn"),
        "dominant_writing_arc_reason_cn": row.get("dominant_writing_arc_reason_cn"),
    }, 3))
    sections = [
        ("研究开展程序", "research_program"),
        ("各部分修辞架构", "rhetorical_architecture"),
        ("理论/知识到设计的翻译", "theory_to_design_trace"),
        ("评价逻辑", "evaluation_logic"),
        ("贡献闭环", "contribution_logic"),
        ("句级写作动作图谱", "sentence_level_move_map"),
        ("写作技术", "writing_techniques"),
        ("可复用研究与写作程序", "reusable_blueprint"),
    ]
    for title, key in sections:
        lines.extend([f"## {title}", ""])
        lines.extend(render_generic(row.get(key) or ([] if key == "sentence_level_move_map" else {}), 3))
    lines.extend(["## 分析边界", "", f"{row.get('limitations_cn') or '无特别说明。'}", ""])
    return "\n".join(lines)


def render_stage2(row: dict[str, Any]) -> str:
    lines = [
        f"# {row.get('title')}：ISR 句段级微观图谱", "",
        f"- 作者：{row.get('authors')}",
        f"- 年份：{row.get('year')}",
        f"- DOI：{row.get('doi')}",
        f"- 源文件：{row.get('source_file')}",
        f"- 置信度：{row.get('confidence')}", "",
        "## 核实后的宏观骨架", "",
        scalar(row.get("verified_macro_scaffold_cn")), "",
    ]
    sections = [
        ("摘要逐句图谱", "abstract_sentence_map"),
        ("引言逐句图谱", "introduction_sentence_map"),
        ("引言逐段图谱", "introduction_paragraph_map"),
        ("理论到设计逐句图谱", "theory_to_design_sentence_map"),
        ("制品设计理由逐句图谱", "artifact_rationale_sentence_map"),
        ("Study开头、过渡与收束图谱", "study_opening_transition_and_closure_map"),
        ("讨论与贡献逐句图谱", "discussion_and_contribution_sentence_map"),
        ("Study累积逻辑", "study_accumulation_logic"),
        ("主张—证据台账", "claim_evidence_ledger"),
        ("ISR定位逻辑", "isr_positioning_logic"),
        ("段落级仿写模板", "paragraph_level_mimicry_template"),
        ("可执行写作算法", "writing_algorithm"),
        ("应模仿的高价值动作", "high_value_moves_to_mimic_cn"),
        ("不要只复制的表面动作", "superficial_moves_not_to_copy_cn"),
        ("证据薄弱或跳跃的动作", "unsupported_or_fragile_moves_cn"),
    ]
    for title, key in sections:
        lines.extend([f"## {title}", ""])
        lines.extend(render_generic(row.get(key) or ([] if isinstance(row.get(key), list) else {}), 3))
    lines.extend([
        "## 一句话套路", "", scalar(row.get("single_sentence_description_of_isr_routine_cn")), "",
        "## 分析边界", "", scalar(row.get("limitations_cn") or "无特别说明。"), "",
    ])
    return "\n".join(lines)


def write_csv(path: Path, rows: list[dict[str, Any]], fields: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def crosstab(rows: list[dict[str, Any]], left: str, right: str) -> list[dict[str, Any]]:
    left_values = sorted({str(row.get(left) or "") for row in rows})
    right_values = sorted({str(row.get(right) or "") for row in rows})
    counts = Counter((str(row.get(left) or ""), str(row.get(right) or "")) for row in rows)
    return [
        {left: lv, **{rv: counts[(lv, rv)] for rv in right_values}, "total": sum(counts[(lv, rv)] for rv in right_values)}
        for lv in left_values
    ]


def mean(values: list[int]) -> float:
    return round(sum(values) / len(values), 2) if values else 0.0


def score(row: dict[str, Any], stage2_sources: set[str]) -> float:
    sentence_units = len(row.get("sentence_level_move_map") or [])
    phases = int((row.get("research_program") or {}).get("study_or_phase_count") or 0)
    mappings = len((row.get("theory_to_design_trace") or {}).get("mapping_table") or [])
    return (
        float(row.get("confidence") or 0) * 10
        + min(sentence_units, 100) / 40
        + min(phases, 10) / 5
        + min(mappings, 10) / 5
        + (1.0 if row.get("source_file") in stage2_sources else 0.0)
        + (0.5 if row.get("source_theory_guided_subset_match") else 0.0)
    )


def build() -> None:
    stage1 = load_articles(STAGE1_DIR)
    stage2 = load_articles(STAGE2_DIR)
    if len(stage1) != 231 or len({row["source_file"] for row in stage1}) != 231:
        raise ValueError("Stage 1 must contain 231 unique article files")
    if len(stage2) != 57 or len({row["source_file"] for row in stage2}) != 57:
        raise ValueError("Stage 2 must contain 57 unique article files")
    if any(row.get("journal") != "Information Systems Research" for row in stage2):
        raise ValueError("Stage 2 contains a non-ISR article")
    if any(row.get("finish_reason") != "stop" for row in stage1 + stage2):
        raise ValueError("one or more analyses did not finish naturally")
    if any(not row.get("sentence_level_move_map") for row in stage1):
        raise ValueError("Stage 1 contains an empty sentence map")
    if any(not row.get("introduction_sentence_map") for row in stage2):
        raise ValueError("Stage 2 contains an empty introduction sentence map")

    stage1_md_dir = DELIVERY_DIR / "all231_article_dissections"
    stage2_md_dir = DELIVERY_DIR / "isr57_micro_dissections"
    stage1_md_dir.mkdir(parents=True, exist_ok=True)
    stage2_md_dir.mkdir(parents=True, exist_ok=True)
    for row in stage1:
        (stage1_md_dir / (Path(row["source_file"]).stem + ".md")).write_text(
            render_stage1(row), encoding="utf-8"
        )
    for row in stage2:
        (stage2_md_dir / (Path(row["source_file"]).stem + ".md")).write_text(
            render_stage2(row), encoding="utf-8"
        )

    stage1_index = ["# 231篇逐篇研究与写作逻辑解剖", ""]
    for row in sorted(stage1, key=lambda item: (str(item.get("journal")), str(item.get("year")), str(item.get("title")))):
        name = Path(row["source_file"]).stem + ".md"
        stage1_index.append(
            f"- {row.get('journal')} · {row.get('year')} · [{row.get('title')}](all231_article_dissections/{name})"
        )
    (DELIVERY_DIR / "all231_index.md").write_text("\n".join(stage1_index) + "\n", encoding="utf-8")
    stage2_index = ["# ISR 57篇句段级微观解剖", ""]
    for row in sorted(stage2, key=lambda item: (str(item.get("year")), str(item.get("title")))):
        name = Path(row["source_file"]).stem + ".md"
        stage2_index.append(
            f"- {row.get('year')} · [{row.get('title')}](isr57_micro_dissections/{name})"
        )
    (DELIVERY_DIR / "isr57_index.md").write_text("\n".join(stage2_index) + "\n", encoding="utf-8")

    move_counts = Counter(
        str(item.get("move_code") or "")
        for row in stage1
        for item in (row.get("sentence_level_move_map") or [])
    )
    coupling_counts = Counter(
        str((row.get("theory_to_design_trace") or {}).get("theory_design_coupling") or "")
        for row in stage1
    )
    stage2_fields = [
        "abstract_sentence_map", "introduction_sentence_map", "introduction_paragraph_map",
        "theory_to_design_sentence_map", "artifact_rationale_sentence_map",
        "study_opening_transition_and_closure_map", "discussion_and_contribution_sentence_map",
        "study_accumulation_logic", "claim_evidence_ledger", "writing_algorithm",
    ]
    stage2_coverage: list[dict[str, Any]] = []
    for row in stage2:
        coverage = {
            "source_file": row["source_file"], "title": row.get("title"), "year": row.get("year"),
            "source_theory_guided_subset_match": row.get("source_theory_guided_subset_match"),
            "confidence": row.get("confidence"), "completion_tokens": (row.get("usage") or {}).get("completion_tokens"),
        }
        coverage.update({field: len(row.get(field) or []) for field in stage2_fields})
        coverage["sentence_units_total"] = sum(
            coverage[field]
            for field in stage2_fields[:2] + stage2_fields[3:7]
        )
        stage2_coverage.append(coverage)
    write_csv(DELIVERY_DIR / "isr57_coverage.csv", stage2_coverage, list(stage2_coverage[0]))

    tables_dir = DELIVERY_DIR / "tables"
    for left, right, filename in (
        ("paper_archetype", "dominant_writing_arc", "archetype_by_arc.csv"),
        ("paper_archetype", "journal", "archetype_by_journal.csv"),
        ("dominant_writing_arc", "journal", "arc_by_journal.csv"),
    ):
        table = crosstab(stage1, left, right)
        write_csv(tables_dir / filename, table, list(table[0]))
    coupling_rows = []
    for row in stage1:
        coupling_rows.append({
            **row,
            "theory_design_coupling": (row.get("theory_to_design_trace") or {}).get("theory_design_coupling"),
            "source_subset": "theory_subset" if row.get("source_theory_guided_subset_match") else "other",
        })
    table = crosstab(coupling_rows, "theory_design_coupling", "source_subset")
    write_csv(tables_dir / "coupling_by_source_subset.csv", table, list(table[0]))

    stage2_sources = {row["source_file"] for row in stage2}
    groups: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in stage1:
        groups[f"archetype::{row.get('paper_archetype')}"] .append(row)
        groups[f"arc::{row.get('dominant_writing_arc')}"] .append(row)
        groups[f"coupling::{(row.get('theory_to_design_trace') or {}).get('theory_design_coupling')}"] .append(row)
    representatives: dict[str, list[dict[str, Any]]] = {}
    for group, rows in sorted(groups.items()):
        selected = sorted(rows, key=lambda row: (-score(row, stage2_sources), str(row.get("title"))))[:5]
        representatives[group] = [
            {
                "source_file": row["source_file"], "title": row.get("title"), "year": row.get("year"),
                "journal": row.get("journal"), "confidence": row.get("confidence"),
                "paper_archetype": row.get("paper_archetype"), "dominant_writing_arc": row.get("dominant_writing_arc"),
                "theory_design_coupling": (row.get("theory_to_design_trace") or {}).get("theory_design_coupling"),
                "study_or_phase_count": (row.get("research_program") or {}).get("study_or_phase_count"),
                "sentence_units": len(row.get("sentence_level_move_map") or []),
                "isr_micro_available": row["source_file"] in stage2_sources,
                "routine_cn": (row.get("reusable_blueprint") or {}).get("single_best_description_of_the_routine_cn"),
            }
            for row in selected
        ]
    (DELIVERY_DIR / "representative_articles.json").write_text(
        json.dumps(representatives, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )

    cards = ["# 跨文章套路证据卡", ""]
    for arc in sorted({str(row.get("dominant_writing_arc")) for row in stage1}):
        selected = sorted(
            [row for row in stage1 if row.get("dominant_writing_arc") == arc],
            key=lambda row: (-score(row, stage2_sources), str(row.get("title"))),
        )[:12]
        cards.extend([f"## {arc}（{sum(row.get('dominant_writing_arc') == arc for row in stage1)}篇）", ""])
        for row in selected:
            summary = row.get("article_level_summary") or {}
            technique = row.get("writing_techniques") or {}
            blueprint = row.get("reusable_blueprint") or {}
            cards.extend([
                f"### {row.get('title')}", "",
                f"- 年份/期刊：{row.get('year')} / {row.get('journal')}",
                f"- 类型：{row.get('paper_archetype')}；耦合：{(row.get('theory_to_design_trace') or {}).get('theory_design_coupling')}",
                f"- 完整论证：{summary.get('whole_argument_in_one_paragraph_cn')}",
                f"- 阶段序列：{(row.get('research_program') or {}).get('overall_sequence_cn')}",
                f"- 缺口制造：{technique.get('gap_construction_cn')}",
                f"- benchmark叙事：{technique.get('benchmark_narrative_cn')}",
                f"- 理论返回：{technique.get('theory_return_cn')}",
                f"- 防止贡献过时：{technique.get('novelty_protection_cn')}",
                f"- 一句话套路：{blueprint.get('single_best_description_of_the_routine_cn')}", "",
            ])
    (DELIVERY_DIR / "cross_article_routine_evidence_cards.md").write_text(
        "\n".join(cards) + "\n", encoding="utf-8"
    )

    isr_cards = ["# ISR 57篇微观写作证据卡", ""]
    for row in sorted(stage2, key=lambda item: (str(item.get("year")), str(item.get("title")))):
        isr = row.get("isr_positioning_logic") or {}
        isr_cards.extend([
            f"## {row.get('title')}", "",
            f"- 年份：{row.get('year')}；理论子集：{row.get('source_theory_guided_subset_match')}",
            f"- 宏观骨架：{row.get('verified_macro_scaffold_cn')}",
            f"- ISR问题构成：{isr.get('constitutive_is_problem_cn')}",
            f"- 技术与行为/市场纠缠：{isr.get('technology_behavior_or_market_entanglement_cn')}",
            f"- 客观证据角色：{isr.get('role_of_benchmark_or_objective_evidence_cn')}",
            f"- 理论进入设计：{isr.get('theory_in_design_cn')}",
            f"- 技术与IS贡献平衡：{isr.get('technical_vs_is_contribution_balance_cn')}",
            f"- 超越暂时性能：{isr.get('beyond_transient_performance_cn')}",
            f"- 一句话ISR套路：{row.get('single_sentence_description_of_isr_routine_cn')}",
            "- 高价值动作：",
            *[f"  - {item}" for item in row.get("high_value_moves_to_mimic_cn") or []],
            "- 不应表面复制：",
            *[f"  - {item}" for item in row.get("superficial_moves_not_to_copy_cn") or []],
            "",
        ])
    (DELIVERY_DIR / "isr57_micro_evidence_cards.md").write_text(
        "\n".join(isr_cards) + "\n", encoding="utf-8"
    )

    stage1_units = [len(row.get("sentence_level_move_map") or []) for row in stage1]
    stage1_phases = [int((row.get("research_program") or {}).get("study_or_phase_count") or 0) for row in stage1]
    stage2_units = [int(row["sentence_units_total"]) for row in stage2_coverage]
    stage2_intro = [int(row["introduction_sentence_map"]) for row in stage2_coverage]
    validation = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "stage1": {
            "articles": len(stage1), "unique_sources": len({row["source_file"] for row in stage1}),
            "natural_stop": sum(row.get("finish_reason") == "stop" for row in stage1),
            "theory_subset": sum(row.get("source_theory_guided_subset_match") is True for row in stage1),
            "isr_articles": sum(row.get("journal") == "Information Systems Research" for row in stage1),
            "sentence_units_total": sum(stage1_units), "sentence_units_min": min(stage1_units),
            "sentence_units_max": max(stage1_units), "sentence_units_mean": mean(stage1_units),
            "study_phases_total": sum(stage1_phases), "study_phases_min": min(stage1_phases),
            "study_phases_max": max(stage1_phases), "study_phases_mean": mean(stage1_phases),
            "move_counts": dict(sorted(move_counts.items())),
            "coupling_counts": dict(sorted(coupling_counts.items())),
        },
        "stage2": {
            "articles": len(stage2), "unique_sources": len({row["source_file"] for row in stage2}),
            "natural_stop": sum(row.get("finish_reason") == "stop" for row in stage2),
            "sentence_units_total": sum(stage2_units), "sentence_units_min": min(stage2_units),
            "sentence_units_max": max(stage2_units), "sentence_units_mean": mean(stage2_units),
            "introduction_sentence_units_total": sum(stage2_intro),
            "introduction_sentence_units_min": min(stage2_intro),
            "introduction_sentence_units_max": max(stage2_intro),
            "introduction_sentence_units_mean": mean(stage2_intro),
        },
        "files": {
            "stage1_markdown": len(list(stage1_md_dir.glob("*.md"))),
            "stage2_markdown": len(list(stage2_md_dir.glob("*.md"))),
        },
    }
    (DELIVERY_DIR / "validation_and_statistics.json").write_text(
        json.dumps(validation, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(validation, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    build()
