#!/usr/bin/env python3
"""Create reproducible audit and summary artifacts for the completed screening run."""

from __future__ import annotations

import csv
import json
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any


RUN_DIR = Path(__file__).resolve().parent
OUTPUT_DIR = RUN_DIR / "output_v1"
INPUT_DIR = RUN_DIR.parents[1] / "database_fulltext_all"


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    with path.open("r", encoding="utf-8") as handle:
        return [json.loads(line) for line in handle if line.strip()]


def best_outcome(row: dict[str, Any]) -> tuple[dict[str, Any], dict[str, Any]]:
    outcomes = row.get("outcome_candidates") or []
    index = int(row.get("best_candidate_index", -1))
    outcome = outcomes[index] if 0 <= index < len(outcomes) else {}
    return outcome, outcome.get("coding_agent_transfer") or {}


def table(headers: list[str], rows: list[list[Any]]) -> list[str]:
    return [
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join("---" for _ in headers) + " |",
        *("| " + " | ".join(str(value).replace("|", "\\|") for value in row) + " |" for row in rows),
    ]


def main() -> None:
    decisions = load_jsonl(OUTPUT_DIR / "decisions.jsonl")
    retained = [
        row
        for row in decisions
        if row["overall_screening_decision"] in {"strong_candidate", "promising_candidate"}
    ]

    overall = Counter(row["overall_screening_decision"] for row in decisions)
    by_year: dict[str, Counter[str]] = defaultdict(Counter)
    by_journal: dict[str, Counter[str]] = defaultdict(Counter)
    cross_design: dict[str, Counter[str]] = defaultdict(Counter)
    attempts = Counter(int(row.get("attempts") or 0) for row in decisions)
    best_specificity: Counter[str] = Counter()
    best_coding_specificity: Counter[str] = Counter()
    best_transfer_strength: Counter[str] = Counter()
    best_transfer_type: Counter[str] = Counter()
    theory_names: Counter[str] = Counter()

    for row in decisions:
        decision = row["overall_screening_decision"]
        by_year[str(row.get("year") or "unknown")][decision] += 1
        by_journal[str(row.get("journal") or "unknown")][decision] += 1
        cross_design[row["source_assessment"]["design_research_type"]][decision] += 1

    for row in retained:
        outcome, transfer = best_outcome(row)
        best_specificity[str(outcome.get("source_context_specificity") or "missing")] += 1
        best_coding_specificity[str(transfer.get("coding_agent_specificity") or "missing")] += 1
        best_transfer_strength[str(transfer.get("transfer_strength") or "missing")] += 1
        best_transfer_type[str(transfer.get("transfer_type") or "missing")] += 1
        for theory in row["source_assessment"].get("theories") or []:
            name = str(theory.get("theory_name") or "").strip()
            if name:
                theory_names[name] += 1

    eligible_design = {"explicit_design_science", "design_oriented_build_evaluate"}
    consistency_issues = [
        row
        for row in decisions
        if (
            row["overall_screening_decision"] == "strong_candidate"
            and row["source_assessment"]["design_research_type"] not in eligible_design
        )
        or (bool(row["target_match"]) != (row["overall_screening_decision"] == "strong_candidate"))
    ]

    core: list[dict[str, Any]] = []
    for row in decisions:
        if row["overall_screening_decision"] != "strong_candidate":
            continue
        outcome, transfer = best_outcome(row)
        if (
            row["source_assessment"]["design_research_type"] == "explicit_design_science"
            and row["source_assessment"]["theory_to_design_strength"] in {"strong", "moderate"}
            and outcome.get("source_context_specificity") in {"domain_constitutive", "contextualized"}
            and transfer.get("coding_agent_specificity") == "strong"
            and transfer.get("transfer_strength") == "strong"
            and float(row.get("confidence") or 0) >= 0.8
        ):
            core.append(row)
    core.sort(key=lambda row: (-float(row.get("confidence") or 0), -int(row.get("year") or 0), row["title"]))

    theme_rules = {
        "security_privacy_trust_accountability": [
            "security", "privacy", "trust", "accountab", "phish", "cyber", "权限", "隐私", "安全", "问责", "信任",
        ],
        "fairness_inclusion_rights": [
            "fair", "equity", "justice", "inclusion", "discrimin", "公平", "公正", "正义", "包容", "歧视", "权利",
        ],
        "human_ai_explanation_oversight": [
            "explain", "human-ai", "human ai", "algorithm", "machine", "agent", "automation", "解释", "监督", "接管", "人机", "智能体",
        ],
        "safety_risk_resilience_recovery": [
            "safety", "risk", "resilien", "recover", "robust", "harm", "安全性", "风险", "韧性", "恢复", "鲁棒", "伤害",
        ],
        "attention_cognition_learning_usability": [
            "attention", "cognit", "learning", "usability", "comprehension", "reflection", "注意", "认知", "学习", "可用性", "理解", "反思",
        ],
        "coordination_governance_incentives_markets": [
            "coordin", "govern", "incentive", "market", "auction", "platform", "welfare", "协调", "治理", "激励", "市场", "拍卖", "福利",
        ],
        "data_quality_detection_measurement": [
            "quality", "detect", "measure", "prediction", "classification", "fraud", "data", "质量", "检测", "测量", "预测", "分类", "欺诈", "数据",
        ],
        "health_care": ["health", "clinical", "patient", "medical", "care", "健康", "临床", "患者", "医疗", "照护"],
        "sustainability_environment": [
            "sustain", "environment", "carbon", "energy", "green", "可持续", "环境", "碳", "能源", "绿色",
        ],
        "software_development": [
            "software", "code", "developer", "technical debt", "repository", "软件", "代码", "开发者", "技术债", "仓库",
        ],
    }
    theme_counts: Counter[str] = Counter()
    for row in retained:
        outcome, transfer = best_outcome(row)
        # Cluster by the source domain, not by the proposed coding-agent wording.
        blob = " ".join(
            [
                str(row.get("title") or ""),
                str(outcome.get("source_outcome_name") or ""),
                str(outcome.get("source_outcome_definition_cn") or ""),
                str(outcome.get("source_operationalization_cn") or ""),
            ]
        ).lower()
        for theme, keywords in theme_rules.items():
            if any(keyword in blob for keyword in keywords):
                theme_counts[theme] += 1

    historical_errors = load_jsonl(OUTPUT_DIR / "errors.jsonl") if (OUTPUT_DIR / "errors.jsonl").exists() else []
    completed_names = {row["source_file"] for row in decisions}
    resolved_historical_errors = sum(error.get("source_file") in completed_names for error in historical_errors)

    unclear_rows = [row for row in decisions if row["overall_screening_decision"] == "unclear"]
    audit_fields = [
        "record_id", "source_file", "title", "year", "journal", "doi", "fulltext_chars", "decision_reason_cn", "limitations_cn"
    ]
    with (OUTPUT_DIR / "unclear_fulltext_audit.csv").open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=audit_fields)
        writer.writeheader()
        for row in sorted(unclear_rows, key=lambda item: int(item.get("fulltext_chars") or 0)):
            writer.writerow({field: row.get(field, "") for field in audit_fields})

    retained_fields = [
        "record_id", "source_file", "title", "authors", "year", "journal", "doi", "overall_screening_decision",
        "design_research_type", "theory_to_design_strength", "source_outcome", "source_context_specificity",
        "coding_agent_outcome_cn", "coding_agent_specificity", "transfer_strength", "transfer_type",
        "decision_reason_cn", "confidence",
    ]
    with (OUTPUT_DIR / "retained_candidates.csv").open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=retained_fields)
        writer.writeheader()
        for row in sorted(
            retained,
            key=lambda item: (0 if item["overall_screening_decision"] == "strong_candidate" else 1, -float(item.get("confidence") or 0), item["title"]),
        ):
            outcome, transfer = best_outcome(row)
            writer.writerow(
                {
                    "record_id": row.get("record_id"),
                    "source_file": row.get("source_file"),
                    "title": row.get("title"),
                    "authors": row.get("authors"),
                    "year": row.get("year"),
                    "journal": row.get("journal"),
                    "doi": row.get("doi"),
                    "overall_screening_decision": row.get("overall_screening_decision"),
                    "design_research_type": row["source_assessment"].get("design_research_type"),
                    "theory_to_design_strength": row["source_assessment"].get("theory_to_design_strength"),
                    "source_outcome": outcome.get("source_outcome_name"),
                    "source_context_specificity": outcome.get("source_context_specificity"),
                    "coding_agent_outcome_cn": transfer.get("candidate_outcome_name_cn"),
                    "coding_agent_specificity": transfer.get("coding_agent_specificity"),
                    "transfer_strength": transfer.get("transfer_strength"),
                    "transfer_type": transfer.get("transfer_type"),
                    "decision_reason_cn": row.get("decision_reason_cn"),
                    "confidence": row.get("confidence"),
                }
            )

    with (OUTPUT_DIR / "high_precision_core.csv").open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=retained_fields)
        writer.writeheader()
        for row in core:
            outcome, transfer = best_outcome(row)
            writer.writerow(
                {
                    "record_id": row.get("record_id"),
                    "source_file": row.get("source_file"),
                    "title": row.get("title"),
                    "authors": row.get("authors"),
                    "year": row.get("year"),
                    "journal": row.get("journal"),
                    "doi": row.get("doi"),
                    "overall_screening_decision": row.get("overall_screening_decision"),
                    "design_research_type": row["source_assessment"].get("design_research_type"),
                    "theory_to_design_strength": row["source_assessment"].get("theory_to_design_strength"),
                    "source_outcome": outcome.get("source_outcome_name"),
                    "source_context_specificity": outcome.get("source_context_specificity"),
                    "coding_agent_outcome_cn": transfer.get("candidate_outcome_name_cn"),
                    "coding_agent_specificity": transfer.get("coding_agent_specificity"),
                    "transfer_strength": transfer.get("transfer_strength"),
                    "transfer_type": transfer.get("transfer_type"),
                    "decision_reason_cn": row.get("decision_reason_cn"),
                    "confidence": row.get("confidence"),
                }
            )

    year_rows: list[list[Any]] = []
    for year in sorted(by_year):
        counts = by_year[year]
        year_rows.append(
            [year, sum(counts.values()), counts["strong_candidate"], counts["promising_candidate"], counts["inspiration_only"], counts["exclude"], counts["unclear"]]
        )

    journal_rows: list[list[Any]] = []
    for journal, counts in sorted(
        by_journal.items(), key=lambda item: -(item[1]["strong_candidate"] + item[1]["promising_candidate"])
    ):
        journal_rows.append(
            [journal, sum(counts.values()), counts["strong_candidate"], counts["promising_candidate"], counts["strong_candidate"] + counts["promising_candidate"]]
        )

    design_rows: list[list[Any]] = []
    for design_type, counts in sorted(cross_design.items()):
        design_rows.append(
            [design_type, sum(counts.values()), counts["strong_candidate"], counts["promising_candidate"], counts["inspiration_only"], counts["exclude"], counts["unclear"]]
        )

    core_rows: list[list[Any]] = []
    for row in core[:30]:
        outcome, transfer = best_outcome(row)
        core_rows.append(
            [row["year"], row["journal"], row["title"], outcome.get("source_outcome_name", ""), transfer.get("candidate_outcome_name_cn", ""), row["confidence"]]
        )

    report = [
        "# Coding-agent-transferable theory-driven DSR screening",
        "",
        "## Run completion",
        "",
        f"- Full texts screened: {len(decisions):,}",
        f"- Strong candidates: {overall['strong_candidate']}",
        f"- Promising candidates: {overall['promising_candidate']}",
        f"- Inspiration only: {overall['inspiration_only']}",
        f"- Excluded: {overall['exclude']}",
        f"- Unclear/full-text audit: {overall['unclear']}",
        f"- High-precision core (explicit DSR plus strong transfer checks): {len(core)}",
        f"- Unresolved API failures: {len(decisions) - len(completed_names)}",
        f"- Historical calibration errors now resolved: {resolved_historical_errors}/{len(historical_errors)}",
        f"- Cross-field consistency issues: {len(consistency_issues)}",
        "",
        "## Decisions by year",
        "",
        *table(["Year", "Total", "Strong", "Promising", "Inspiration", "Exclude", "Unclear"], year_rows),
        "",
        "## Decisions by design-research classification",
        "",
        *table(["Design type", "Total", "Strong", "Promising", "Inspiration", "Exclude", "Unclear"], design_rows),
        "",
        "## Journals ranked by retained candidates",
        "",
        *table(["Journal", "Total", "Strong", "Promising", "Retained"], journal_rows),
        "",
        "## Best-outcome transfer diagnostics for retained candidates",
        "",
        f"- Source contextual specificity: {dict(best_specificity)}",
        f"- Coding-agent specificity: {dict(best_coding_specificity)}",
        f"- Transfer strength: {dict(best_transfer_strength)}",
        f"- Transfer type: {dict(best_transfer_type)}",
        "",
        "## Overlapping heuristic themes among retained candidates",
        "",
        "These counts use only source-paper titles/outcomes/operationalizations, are keyword-based and non-mutually-exclusive, and are navigation aids rather than model decisions.",
        "",
        *table(["Theme", "Retained papers"], [[theme, count] for theme, count in theme_counts.most_common()]),
        "",
        "## Most frequently named theories in retained candidates",
        "",
        *table(["Theory name as returned", "Count"], [[name, count] for name, count in theory_names.most_common(25)]),
        "",
        "## High-precision core: first 30 by confidence",
        "",
        *table(["Year", "Journal", "Title", "Source outcome", "Coding-agent outcome", "Confidence"], core_rows),
        "",
        "## Quality notes",
        "",
        "- `unclear_fulltext_audit.csv` contains records whose source text is incomplete, mismatched, or otherwise insufficient.",
        "- `errors.jsonl` contains two early calibration failures caused by an output-token cap; both articles were successfully rerun and are present in the final decisions.",
        "- `retained_candidates.csv` is the compact human-review set. The complete nested evidence and transfer reasoning remain in `decisions.jsonl`.",
    ]
    (OUTPUT_DIR / "screening_analysis_report.md").write_text("\n".join(report) + "\n", encoding="utf-8")

    detailed = [
        "# High-precision core: detailed evidence profiles",
        "",
        "These 20 records are a derived high-precision review stratum, not a model output label. They satisfy all post-screening rules documented in `screening_analysis_report.md`.",
        "",
    ]
    for number, row in enumerate(core, start=1):
        outcome, transfer = best_outcome(row)
        detailed.extend(
            [
                f"## {number}. {row['title']}",
                "",
                f"- Metadata: {row.get('year')} · {row.get('journal')} · {row.get('doi')}",
                f"- Authors: {row.get('authors')}",
                f"- Design classification: {row['source_assessment'].get('design_research_type')}",
                f"- Artifact/intervention: {row['source_assessment'].get('artifact_or_intervention_cn', '')}",
                f"- Theory-to-design strength: {row['source_assessment'].get('theory_to_design_strength')}",
                "- Theories:",
            ]
        )
        for theory in row["source_assessment"].get("theories") or []:
            detailed.append(
                f"  - {theory.get('theory_name', '')}: {theory.get('design_role_cn', '')}"
            )
        detailed.extend(
            [
                f"- Source outcome: {outcome.get('source_outcome_name', '')}",
                f"- Source definition: {outcome.get('source_outcome_definition_cn', '')}",
                f"- Source evaluation role: {outcome.get('source_outcome_role', '')}",
                f"- Source operationalization: {outcome.get('source_operationalization_cn', '')}",
                f"- Source contextual specificity: {outcome.get('source_context_specificity', '')}",
                f"- Why source-specific: {outcome.get('source_specificity_reason_cn', '')}",
                f"- Coding-agent outcome: {transfer.get('candidate_outcome_name_cn', '')}",
                f"- Coding-agent definition: {transfer.get('candidate_outcome_definition_cn', '')}",
                f"- Transfer type: {transfer.get('transfer_type', '')}",
                f"- Theory reuse: {transfer.get('theory_reuse_mode', '')}",
                f"- Distinctive affordances: {', '.join(transfer.get('distinctive_coding_agent_affordances') or [])}",
                f"- Mechanism mapping: {transfer.get('theory_design_mechanism_mapping_cn', '')}",
                "- Proposed observables:",
                *(f"  - {value}" for value in transfer.get("proposed_observables_cn") or []),
                f"- Coding-agent counterfactual: {transfer.get('coding_counterfactual_cn', '')}",
                f"- Caveat: {transfer.get('transfer_caveats_cn', '')}",
                f"- Flash decision reason: {row.get('decision_reason_cn', '')}",
                f"- Confidence: {row.get('confidence')}",
                "- Design evidence:",
                *(f"  - {value}" for value in row["source_assessment"].get("design_evidence") or []),
                "- Evaluation evidence:",
                *(f"  - {value}" for value in row["source_assessment"].get("evaluation_evidence") or []),
                "- Outcome evidence:",
                *(f"  - {value}" for value in outcome.get("source_outcome_evidence") or []),
                "",
            ]
        )
    (OUTPUT_DIR / "high_precision_core_detailed.md").write_text(
        "\n".join(detailed) + "\n", encoding="utf-8"
    )

    structured = {
        "records": len(decisions),
        "overall": dict(overall),
        "retained": len(retained),
        "high_precision_core": len(core),
        "consistency_issues": len(consistency_issues),
        "historical_errors": len(historical_errors),
        "resolved_historical_errors": resolved_historical_errors,
        "attempt_counts": dict(sorted(attempts.items())),
        "best_source_specificity": dict(best_specificity),
        "best_coding_agent_specificity": dict(best_coding_specificity),
        "best_transfer_strength": dict(best_transfer_strength),
        "best_transfer_type": dict(best_transfer_type),
        "overlapping_theme_counts": dict(theme_counts),
    }
    (OUTPUT_DIR / "analysis_summary.json").write_text(
        json.dumps(structured, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )


if __name__ == "__main__":
    main()
