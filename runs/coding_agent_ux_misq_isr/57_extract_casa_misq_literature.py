"""Extract a traceable Top-11 literature evidence matrix for the CASA manuscript."""

from __future__ import annotations

import csv
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / "database" / "ALL_AIS_Basket_11.csv"
OUT_DIR = Path(__file__).resolve().parent
OUT_CSV = OUT_DIR / "57_casa_misq_literature_evidence.csv"
OUT_MD = OUT_DIR / "57_casa_misq_literature_evidence.md"


# The list is deliberately curated. Broad keyword hits such as "AI" or "control"
# produce hundreds of substantively unrelated records in the source database.
EVIDENCE_MAP = {
    "Development of an instrument to measure the perceptions of adopting an information technology innovation": (
        "construct_method",
        "Shows how weak definitions and measures impede cumulative research and demonstrates iterative item sorting, construct redefinition, and independent field tests.",
        "Does not justify CASA's substantive domain or proposed dimensions.",
    ),
    "Understanding information systems continuance: An expectation-confirmation model": (
        "outcome_chain",
        "Provides the established individual-level link from satisfaction to continuance intention.",
        "Does not establish CASA as an antecedent of satisfaction.",
    ),
    "Explanations from intelligent systems: Theoretical foundations and implications for practice": (
        "interface_antecedent",
        "Shows that context-specific explanations can support performance, learning, satisfaction, acceptance, and trust, while excessive effort can suppress explanation use.",
        "Explanation quality and explanation use are not situation awareness.",
    ),
    "A methodology for construct development in MIS research": (
        "construct_method",
        "Defines domain specification, instrument construction, and measurement-property evaluation as distinct stages of MIS construct development.",
        "Provides process guidance rather than evidence that a new CASA construct exists.",
    ),
    "Reconceptualizing system usage: An approach and empirical test": (
        "contextualization",
        "Demonstrates that an individual-level IS construct must be defined around the focal user, system, task, and nomological context rather than measured generically.",
        "Concerns system use and should not be treated as CASA's parent construct.",
    ),
    "Construct measurement and validation procedures in MIS and behavioral research: Integrating new and existing techniques": (
        "construct_method",
        "Provides the principal MIS guidance for conceptual definition, measurement-model specification, content validity, and multi-stage validation.",
        "Cannot supply CASA content before qualitative evidence is collected.",
    ),
    "From use to effective use: A representation theory perspective": (
        "outcome_boundary",
        "Explains why effective interaction depends on users obtaining faithful representations of system-relevant states and goals.",
        "Effective use is a broader outcome-oriented construct, not CASA.",
    ),
    "A framework and guidelines for context-specific theorizing in information systems research": (
        "contextualization",
        "Establishes that context can reveal direct and interacting mechanisms hidden by general constructs and supplies criteria for context-specific theorizing.",
        "Context alone does not warrant renaming or duplicating an existing construct.",
    ),
    "The nature and consequences of trade-off transparency in the context of recommendation agents": (
        "interface_antecedent",
        "Shows that a concrete interface transparency feature can change diagnosticity, enjoyment, decision quality, and effort, including nonlinear effects.",
        "Trade-off transparency concerns disclosed product trade-offs and is neither general transparency nor CASA.",
    ),
    "Mobile application usability: Conceptualization and instrument development": (
        "contextualization",
        "Provides an MIS precedent for deriving a technology-specific individual-level construct and instrument when established measures omit interaction-specific content.",
        "Usability is not CASA and must not be used as CASA's parent construct.",
    ),
    "The effect of interactive analytical dashboard features on situation awareness and task performance": (
        "sa_is_evidence",
        "Shows that interface functionality can increase task performance while reducing individual situation awareness, supporting CASA's distinction from performance.",
        "The dashboard task does not contain delegated action or mutable software artifacts.",
    ),
    "Research perspectives: The rise of human machines: How cognitive computing systems challenge assumptions of user-system interaction": (
        "agentic_context",
        "Argues that learning and adaptive systems challenge assumptions inherited from interactions with passive information systems.",
        "Does not define or measure coding-agent situation awareness.",
    ),
    "Eyes wide open: The role of situational information security awareness for security-related behaviour": (
        "sa_is_evidence",
        "Provides an individual-level IS precedent for contextualizing situation awareness and linking person and system antecedents to appraisal and behavior.",
        "Its focal state is a phishing threat, not agent action or software change.",
    ),
    "Failures of fairness in automation require a deeper understanding of human–ml augmentation": (
        "agentic_context",
        "Distinguishes forms of human oversight and argues that machine-learning artifacts can invalidate assumptions embedded in traditional IS concepts.",
        "Its analysis is organized around fairness and augmentation, not users' subjective task-state awareness.",
    ),
    "The next generation of research on is use: A theoretical framework of delegation to and from agentic is artifacts": (
        "agentic_context",
        "Establishes delegation in a human-agentic-IS dyad and identifies appraisal, distribution, and coordination as mechanisms when artifacts initiate action under uncertainty.",
        "Delegation is the interaction structure that motivates CASA, not CASA's measurement domain.",
    ),
    "Cognitive Challenges in Human–Artificial Intelligence Collaboration: Investigating the Path Toward Productive Delegation": (
        "agentic_context",
        "Shows that productive human-to-AI delegation can fail because people lack metaknowledge even when algorithm aversion is absent.",
        "Classification delegation does not directly represent users' awareness of an evolving coding task.",
    ),
    "On the Design of and Interaction with Conversational Agents: An Organizing and Assessing Review of Human-Computer Interaction Research": (
        "adjacent_ux",
        "Documents that agent design, interaction, perceptions, and outcomes form distinct elements of the human-agent research space.",
        "Conversational-agent findings cannot be assumed to cover tool-using coding agents.",
    ),
    "AI Agents as Team Members: Effects on Satisfaction, Conflict, Trustworthiness, and Willingness to Work With": (
        "outcome_boundary",
        "Demonstrates that AI participation can affect process satisfaction independently of trustworthiness and willingness to work with the agent.",
        "The study is a virtual-team experiment and does not measure CASA.",
    ),
    "Expl(AI)ned: The Impact of Explainable Artificial Intelligence on Users' Information Processing": (
        "interface_antecedent",
        "Shows that explanations reshape situational information weighting and mental models and may also preserve misconceptions.",
        "An explanation or mental-model adjustment is not evidence that users accurately or subjectively grasp an agentic coding task.",
    ),
    "Prejudiced against the Machine? Implicit Associations and the Transience of Algorithm Aversion": (
        "boundary_construct",
        "Shows that reliance preferences can arise from implicit bias and accessible performance information, providing a competing account distinct from task-state awareness.",
        "Algorithm aversion is a preference between human and algorithmic advice, not CASA.",
    ),
    "AN INTEGRATIVE PERSPECTIVE ON ALGORITHM AVERSION AND APPRECIATION IN DECISION-MAKING": (
        "boundary_construct",
        "Clarifies the definition and measurement of algorithm aversion and appreciation across decision configurations.",
        "Preference for human versus algorithmic advice does not measure awareness of task state.",
    ),
}


def norm(text: str) -> str:
    return " ".join((text or "").lower().replace("–", "-").split())


def main() -> None:
    keyed = {norm(title): (title, *meta) for title, meta in EVIDENCE_MAP.items()}
    selected: list[dict[str, str]] = []
    situation_awareness: list[dict[str, str]] = []

    with SOURCE.open("r", encoding="utf-8-sig", newline="") as handle:
        for row in csv.DictReader(handle):
            title_key = norm(row.get("Title", ""))
            if "situation awareness" in norm(" ".join([
                row.get("Title", ""), row.get("Abstract", ""),
                row.get("Author Keywords", ""), row.get("Index Keywords", ""),
            ])) or "situational awareness" in norm(" ".join([
                row.get("Title", ""), row.get("Abstract", ""),
                row.get("Author Keywords", ""), row.get("Index Keywords", ""),
            ])):
                situation_awareness.append(row)

            if title_key not in keyed:
                continue
            canonical, category, use, limit = keyed[title_key]
            selected.append({
                "category": category,
                "canonical_title": canonical,
                "authors": row.get("Authors", ""),
                "year": row.get("Year", ""),
                "source_title": row.get("Source title", ""),
                "cited_by": row.get("Cited by", ""),
                "doi": row.get("DOI", ""),
                "abstract": row.get("Abstract", ""),
                "evidentiary_use": use,
                "claim_limit": limit,
            })

    found = {norm(item["canonical_title"]) for item in selected}
    missing = [title for title in EVIDENCE_MAP if norm(title) not in found]
    if missing:
        raise RuntimeError("Curated titles not found in database: " + "; ".join(missing))

    fields = [
        "category", "canonical_title", "authors", "year", "source_title",
        "cited_by", "doi", "abstract", "evidentiary_use", "claim_limit",
    ]
    selected.sort(key=lambda row: (row["category"], -int(row["cited_by"] or 0)))
    with OUT_CSV.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(selected)

    grouped: dict[str, list[dict[str, str]]] = defaultdict(list)
    for item in selected:
        grouped[item["category"]].append(item)

    lines = [
        "# CASA 构念开发的 Top 11 文献证据矩阵",
        "",
        f"> 数据源：`{SOURCE}`。本脚本采用精确题名筛选，避免广义 AI、控制或透明度关键词带来的大量误收。数据库被引次数仅用于辨识经典程度，不作为理论适配性的判断标准。",
        "",
        "## 抽取概况",
        "",
        f"- 精确纳入的核心记录：{len(selected)} 篇。",
        f"- 数据库中提及 situation awareness 或 situational awareness 的记录：{len(situation_awareness)} 篇。",
        "- 每篇记录同时标注可支持的论证和不可越过的证据边界。",
        "",
    ]
    labels = {
        "agentic_context": "编程智能体作为代理行动情境",
        "sa_is_evidence": "个体态势感知的 IS 证据",
        "contextualization": "情境化构念的理论依据",
        "construct_method": "构念与量表开发方法",
        "interface_antecedent": "界面与信息呈现前因",
        "adjacent_ux": "相邻的人机交互研究",
        "boundary_construct": "相邻构念边界",
        "outcome_boundary": "结果链与边界",
        "outcome_chain": "个体使用结果链",
    }
    for category in labels:
        items = grouped.get(category, [])
        if not items:
            continue
        lines.extend([f"## {labels[category]}", ""])
        for item in items:
            lines.extend([
                f"### {item['canonical_title']}",
                "",
                f"- 题录：{item['authors']}（{item['year']}），*{item['source_title']}*；数据库被引 {item['cited_by'] or '0'} 次；DOI：{item['doi']}。",
                f"- 数据库摘要：{item['abstract']}",
                f"- 可支持：{item['evidentiary_use']}",
                f"- 证据边界：{item['claim_limit']}",
                "",
            ])

    lines.extend([
        "## 使用规则",
        "",
        "1. 编程智能体的代理行动特征由 Baird 与 Maruping（2021）等文献建立，但 CASA 的内容仍只能由态势感知理论与后续经验材料界定。",
        "2. Hong 等（2014）、Hoehle 与 Venkatesh（2015）只证明情境化理论与测量可以成立，不能单凭情境新颖性证明 CASA 必须成为新构念。",
        "3. 透明度、解释、信任、感知控制、满意度和持续使用仅用于边界、前因或后果；不得拼入 CASA 定义。",
        "4. 个体态势感知文献可以支持 CASA 的理论起点和法则网络，但不能预先替代 Reddit 数据识别其情境特定内容。",
        "",
    ])
    OUT_MD.write_text("\n".join(lines), encoding="utf-8-sig")

    print(f"Wrote {OUT_CSV}")
    print(f"Wrote {OUT_MD}")
    print(f"Selected records: {len(selected)}; SA records in database: {len(situation_awareness)}")


if __name__ == "__main__":
    main()
