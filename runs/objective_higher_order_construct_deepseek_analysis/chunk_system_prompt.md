你正在读取一篇过长 IS 文章的一个连续全文分块。任务是提取“明确的理论 construct，其多个概念维度均被客观非问卷测量，并被实际聚合为该 construct 的上层值”的局部证据，供覆盖全篇的后续综合判断。只根据本分块输出有效 JSON，不要输出 Markdown，也不要因本块无证据就断言整篇没有证据。

注意：目标 X 必须被文章明确称为 `construct`，但作者不必称它 higher-order/second-order，也不必开发新 construct。不要把普通 index、预测分数、多个原始指标、并列回归变量或多通道神经网络输入误当作高阶 construct。

分别寻找：

1. 具名 X 与理论意义 `construct` 的明确联系；
2. X 与至少两个 dimension/facet/component/subconstruct 的组成关系；
3. 每个组成部分的非问卷测量方法与数据来源，以及问卷/评分等反证；
4. 本文实际从各部分生成 X 的一个上层值的公式、权重、因子/成分得分、指数或模型证据；
5. 只分别使用各维度、只说未来可聚合、或聚合结果并非 X 的边界证据。

返回：

{
  "construct_identity_candidates": [
    {"construct_name": "名称", "evidence": ["短引文或定位"]}
  ],
  "hierarchy_candidates": [
    {"construct_name": "名称", "components": ["部分名"], "explicit_higher_order_label": false, "evidence": ["短引文或定位"]}
  ],
  "component_measurement_candidates": [
    {"construct_name": "上层名称", "component_name": "部分名", "measurement_mode": "strict_objective | reproducible_behavioral_coding | rater_based_nonquestionnaire | questionnaire_self_report | mixed | unclear", "method_cn": "方法", "data_source_cn": "数据", "evidence": ["短引文或定位"]}
  ],
  "aggregation_candidates": [
    {"construct_name": "名称", "aggregation_output_type": "composite_index | single_numeric_score | latent_factor_score | other_single_value | no_aggregated_value | unclear", "method_cn": "聚合方法", "actually_computed_in_this_article": false, "same_construct_link": false, "evidence": ["短引文或定位"]}
  ],
  "negative_or_boundary_evidence": ["不满足条件的重要证据"],
  "limitations": ["OCR、缺页或本块限制"]
}

