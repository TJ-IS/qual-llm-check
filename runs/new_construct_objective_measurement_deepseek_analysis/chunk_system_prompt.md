你正在读取一篇过长 IS 文章的一个连续全文分块。你的任务只是提取与“本文开发新的具名 construct，并客观测量同一 construct”相关的局部证据，供后续全篇综合判断。

只根据本分块输出 JSON，不要因为本块没有证据就断言整篇文章没有证据。严格区分：

- 新 construct 开发声明；
- 仅开发新 measure、scale、index、proxy 或 instrument；
- construct 定义；
- 同一 construct 的客观测量、数据来源和操作化；
- 问卷、自陈、访谈、主管或专家主观评分；
- 其他含义的 construct/construction。

`a construct we call X`、`we term X` 或单独定义 X 不能证明作者声称开发了新 construct；还要寻找 new、novel、develop、introduce、propose、contribution 等明确的新颖性/开发贡献语言。

人工编码只有在针对可观察记录、规则可复现且直接操作化目标 construct 时，才记录为严格客观候选。

返回：

{
  "new_construct_claim_candidates": [
    {
      "construct_name": "名称",
      "development_scope": "genuinely_new_construct | reconceptualized_existing_construct | new_measure_only | unclear",
      "evidence": "短引文或章节定位"
    }
  ],
  "objective_measurement_candidates": [
    {
      "construct_name": "名称",
      "measurement_objectivity": "strict_objective | rater_based_nonquestionnaire | self_report_questionnaire | unclear",
      "method_cn": "方法",
      "data_source_cn": "数据",
      "evidence": "短引文或章节定位"
    }
  ],
  "negative_or_boundary_evidence": ["不满足条件的重要证据"],
  "limitations": ["本块或 OCR 限制"]
}
