from __future__ import annotations

import json
from collections import Counter, defaultdict
from pathlib import Path


RUN_DIR = Path(__file__).resolve().parent
AUDIT_DIR = RUN_DIR / "audit_v1"
MANIFEST = AUDIT_DIR / "sample_manifest.json"
RESULTS_JSON = AUDIT_DIR / "manual_audit_results.json"
REPORT_MD = AUDIT_DIR / "manual_audit_report.md"


NOTES = {
    "8364": "确认纳入。全文提出多源 eWOM 排名算法及原型，以相对多种基线和消融版本的 Spearman 排名相关改进作为核心成功证据。",
    "6616": "确认纳入。blob-centric 图像检索组织与索引方案是明确制品，查询响应时间和 I/O 成本相对 naive 方案的改进构成全文评价核心。",
    "8542": "确认纳入。组合交易所定价机制及投标语言属于可实施的平台机制设计，贸易利得、效率损失和计算性能均有明确最优参照。",
    "7344": "确认纳入。按时段匹配产品价值诉求是可实施的移动定向规则，随机实地实验以实际购买率相对行业默认策略的提升为主要结果。",
    "764": "确认纳入。众包标注质量保障算法围绕误分类成本与标签成本设计，并通过模拟、真实数据和现场实验与多种基准比较。",
    "15986": "确认纳入。混合可再生能源规划 DSS 和随机优化/启发式方法以期望总成本和最优差距作为排他性评价标准。",
    "12792": "确认纳入。作者构建不同导航结构的网站版本，核心问题就是哪种界面结构提高客观任务完成表现；感知测量不是成功判据。",
    "9894": "确认纳入。awareness display 的信息粒度是被设计的界面属性，两轮实验用中断时机、任务正确率/时间和目标绩效进行客观比较。",
    "16308": "确认纳入。CABG 结局预测模型体系以测试集准确率、敏感度和特异度比较算法，客观预测表现是全文核心。",
    "950": "确认纳入。作者构建不同临床阶段的 LOS 预测模型并以线性回归为基准，MAE/MRE 的跨模型、跨阶段比较贯穿全文。",
    "13306": "确认纳入（边界较宽）。论文给出可求解的软件专利政策决策规则，并以社会福利相对自由市场和替代政策的解析/数值比较为唯一成功标准；符合提示词对 formal prescriptive policy 的明确允许。",
    "7286": "确认纳入。可中断负荷采购随机规划以 CVaR 与期望利润为目标，并明确比较无该方案的基准情形。",
    "10622": "确认纳入。Readable 是实际构建的程序表示与执行环境，正确答案评分的程序理解测试相对 Java 对照构成主要评价。",
    "11228": "确认纳入。社交购物路线推荐制品以推荐路线和真实访问路线的客观重叠率为核心，满意度仅为补充。",
    "13598": "确认纳入。会话式仪表盘和 onboarding 是理论导出的界面制品；transparent interaction 用最短路径比率、效率用时间、有效性用正确任务数进行行为化测量并与六种制品条件比较。",
    "6360": "确认纳入。概念建模中的 part-whole 表示是被设计的信息表示方式，答案正确率是主导结果，时间和感知易用性为辅助。",
    "1090": "确认纳入。可分享性与稀缺性组合成数字促销机制，field/online experiments 以购买、成功推荐、净收入和 CLV 相对对照的改善为主。",
    "4378": "确认纳入。WISS 是实际 Web 干预支持制品，随机对照以药物停用率和阶段迁移等客观健康行为结果判断成效。",
    "10408": "确认排除。虽有三种咨询工具和客观 decision quality，但文章以 empowerment 理论及 DMS、DMT、SoC、PPR、GSPI 等感知构念形成并列核心，客观改进不占支配地位。",
    "4164": "确认排除。结构模型的主要贡献是估计 TNC 功能价值、司机学习和促销效应；优化促销政策只在主分析之后作为应用，不能反向代表全文的主要成功标准。",
    "11476": "确认排除。理论特征被用于 churn prediction 且报告测试集 AUC，但没有把所提特征/模型与不含这些特征的明确基线作性能增量比较；绝对 AUC 与重复抽样不满足 Gate 3。",
    "5836": "改判纳入。CAPS 不只是抽象框架：作者按该框架连续构建 context-aware predictive artifacts，以 Croston 为显式基线，用 forecasting-error cost 证明 phase-out 版本改善 4%、sensor activity 版本改善 20%。全文把框架归为 DSR improvement contribution，客观改进是评价其能否产生更好制品的主导证据；专家/情境反思用于迭代和边界说明，不是并列的主观成功指标。",
    "3102": "确认排除。ECCO 同时追求可迁移的模型选择、完整分析流程和 actionable insight；准确率基准只验证其中的 sentiment-modeling 模块，后半部分洞察能力主要以案例展示，故客观改进不是整个框架的支配性成功标准。",
    "8946": "确认排除。研究操纵的是既有 GDSS 外部的人工 facilitation 角色，而非作者设计或实质修改的数字制品；客观共识结果不能弥补 Gate 1。",
    "1082": "确认排除。平台功能是研究场景中已经发生的自然整合，作者利用准实验解释其效果，没有提出或实施该制品改造。",
    "9906": "改判纳入。文章给出可实施的在线随机 last-minute sales 定价/供给决策规则，解析求解不同参数下的最优策略，并把利润同确定性销售及其他策略类别直接比较。提示词明确允许 prescriptive model、decision rule 和 digital policy，因此不应仅因它不是软件界面而判 Gate 1 失败。",
    "13262": "确认排除。文章比较已有 TDD 与 test-last 开发实践，不设计软件制品；且软件质量与任务满意度是并列结果。",
    "256": "确认排除。干预是系统外的纸质 self-regulatory learning scripts，而非 e-learning 系统功能或数字制品改造。",
    "15010": "确认排除。WBT 是现成商业产品，作者比较的是培训/协作教学安排；知识测试与自我效能、满意度并列，既不满足 Gate 1 也不满足 Gate 4。",
    "4338": "确认排除。self-prophecy 提问是行为实验操纵，不是 IS 制品；处理相对控制也未证明任务正确率改善。",
}

OVERRIDES = {
    "5836": {
        "manual_strict_match": True,
        "manual_centrality": "dominant",
        "manual_solution_layer": "hybrid",
        "manual_gates": {
            "purposeful_solution_design": True,
            "objective_metric_is_primary_target": True,
            "comparative_improvement_demonstrated": True,
            "objective_improvement_is_the_success_basis": True,
        },
        "error_type": "false_negative_overstrict_centrality",
    },
    "9906": {
        "manual_strict_match": True,
        "manual_centrality": "exclusive",
        "manual_solution_layer": "prescriptive_model_or_optimization",
        "manual_gates": {
            "purposeful_solution_design": True,
            "objective_metric_is_primary_target": True,
            "comparative_improvement_demonstrated": True,
            "objective_improvement_is_the_success_basis": True,
        },
        "error_type": "false_negative_overstrict_solution_boundary",
    },
}


def main() -> None:
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    audited = []
    for index, record in enumerate(manifest["records"], 1):
        record_id = record["record_id"]
        override = OVERRIDES.get(record_id)
        manual_match = override["manual_strict_match"] if override else record["strict_match"]
        item = {
            "audit_id": index,
            "audit_group": record["audit_group"],
            "record_id": record_id,
            "source_file": record["source_file"],
            "title": record["title"],
            "year": record["year"],
            "journal": record["journal"],
            "model_strict_match": record["strict_match"],
            "manual_strict_match": manual_match,
            "manual_outcome": (
                "confirmed_inclusion"
                if record["strict_match"] and manual_match
                else "confirmed_exclusion"
                if not record["strict_match"] and not manual_match
                else "false_negative"
                if not record["strict_match"] and manual_match
                else "false_positive"
            ),
            "model_gates": record["gates"],
            "manual_gates": override["manual_gates"] if override else record["gates"],
            "model_centrality": record["centrality"],
            "manual_centrality": override["manual_centrality"] if override else record["centrality"],
            "model_solution_layer": record["solution_layer"],
            "manual_solution_layer": override["manual_solution_layer"] if override else record["solution_layer"],
            "error_type": override["error_type"] if override else "none",
            "manual_reason_cn": NOTES[record_id],
        }
        audited.append(item)

    outcomes = Counter(item["manual_outcome"] for item in audited)
    by_group: dict[str, Counter] = defaultdict(Counter)
    for item in audited:
        by_group[item["audit_group"]][item["manual_outcome"]] += 1

    sampled_model_inclusions = sum(item["model_strict_match"] for item in audited)
    sampled_model_exclusions = len(audited) - sampled_model_inclusions
    summary = {
        "sample_design": "fixed deterministic stratified audit; not a simple random sample",
        "seed": manifest["seed"],
        "screened_available_when_sampled": manifest["screened_available"],
        "sample_size": len(audited),
        "model_inclusions_sampled": sampled_model_inclusions,
        "model_exclusions_sampled": sampled_model_exclusions,
        "confirmed_inclusions": outcomes["confirmed_inclusion"],
        "confirmed_exclusions": outcomes["confirmed_exclusion"],
        "false_positives": outcomes["false_positive"],
        "false_negatives": outcomes["false_negative"],
        "raw_agreement_count": outcomes["confirmed_inclusion"] + outcomes["confirmed_exclusion"],
        "raw_agreement_rate": round(
            (outcomes["confirmed_inclusion"] + outcomes["confirmed_exclusion"]) / len(audited), 4
        ),
        "observed_precision_within_stratified_inclusion_sample": round(
            outcomes["confirmed_inclusion"] / sampled_model_inclusions, 4
        ),
        "warning": "Because inclusion layers and boundary cases were intentionally oversampled, these rates must not be projected directly to all screened articles.",
        "error_taxonomy": {
            "false_negative_overstrict_centrality": 1,
            "false_negative_overstrict_solution_boundary": 1,
        },
        "by_group": {group: dict(counts) for group, counts in sorted(by_group.items())},
    }
    RESULTS_JSON.write_text(
        json.dumps({"summary": summary, "records": audited}, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    lines = [
        "# Manual stratified audit report",
        "",
        "## Outcome",
        "",
        f"- Fixed sample: {len(audited)} articles (seed `{manifest['seed']}`; sampled after {manifest['screened_available']} decisions were available)",
        f"- Model inclusions audited: {sampled_model_inclusions}; confirmed: {outcomes['confirmed_inclusion']}; false positives: {outcomes['false_positive']}",
        f"- Model exclusions audited: {sampled_model_exclusions}; confirmed: {outcomes['confirmed_exclusion']}; false negatives: {outcomes['false_negative']}",
        f"- Raw agreement: {summary['raw_agreement_count']}/{len(audited)} ({summary['raw_agreement_rate']:.1%})",
        "- Important: this is a deliberately stratified boundary audit, not a prevalence sample. Do not extrapolate its rates to the corpus.",
        "",
        "## Corrections",
        "",
    ]
    for item in audited:
        if item["manual_outcome"] in {"false_negative", "false_positive"}:
            lines.extend(
                [
                    f"### {item['title']}",
                    "",
                    f"- Model -> manual: `{item['model_strict_match']}` -> `{item['manual_strict_match']}`",
                    f"- Error type: `{item['error_type']}`",
                    f"- Reason: {item['manual_reason_cn']}",
                    "",
                ]
            )
    lines.extend(
        [
            "## Boundary interpretation",
            "",
            "The inclusion sample showed no obvious false positive in this audit. The two observed disagreements were both conservative exclusions:",
            "",
            "1. A DSR process/framework paper can still be objective-improvement dominant when the framework is evaluated by building multiple artifacts and the central evidence is benchmark improvement. Qualitative reflection used to refine the framework does not automatically make the success criteria mixed.",
            "2. A formal e-commerce policy can satisfy purposeful solution design when it yields a concrete, implementable decision rule and objective comparison. Requiring a graphical interface or deployed software would contradict the prompt's explicit allowance for prescriptive models and digital policies.",
            "",
            "## Article-level judgments",
            "",
        ]
    )
    for item in audited:
        lines.extend(
            [
                f"### {item['audit_id']:02d}. {item['title']}",
                "",
                f"- Group: `{item['audit_group']}`",
                f"- Outcome: `{item['manual_outcome']}`",
                f"- Model/manual decision: `{item['model_strict_match']}` / `{item['manual_strict_match']}`",
                f"- Manual reason: {item['manual_reason_cn']}",
                "",
            ]
        )
    REPORT_MD.write_text("\n".join(lines), encoding="utf-8")
    print(json.dumps(summary, ensure_ascii=False))


if __name__ == "__main__":
    main()
