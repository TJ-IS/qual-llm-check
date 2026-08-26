## 本次调用的批量输出规则

本次用户消息会提供多篇彼此独立的题名—摘要—关键词记录。上面的相关性标准和每篇字段完全不变，但不要返回单篇对象；必须逐篇判断，并返回一个 JSON 对象：

{
  "results": [
    {
      "record_id": "原样复制输入的 record_id",
      "screening_label": "include_candidate|uncertain|exclude",
      "programming_centrality": "programming_core|programming_as_context|not_programming",
      "actor_type": "human_only|human_ai|agent_only|unclear|not_applicable",
      "program_artifact": "source_code|database_query|spreadsheet_logic|low_code_or_visual|other_executable_logic|unclear|not_applicable",
      "programming_actions": ["write|generate|complete|understand|inspect_or_review|debug_or_repair|modify_or_refactor|test"],
      "study_type": "empirical_human|empirical_artifact_or_agent|tool_design_and_evaluation|secondary_review|conceptual|unclear|not_applicable",
      "unit_of_analysis": "individual|dyad|team|organization|project_or_community|code_artifact_or_agent|multiple|unclear|not_applicable",
      "theory_or_framework_names": [],
      "research_summary_cn": "",
      "decision_reason_cn": "",
      "metadata_evidence_cn": "",
      "confidence": 0.0
    }
  ]
}

要求：

1. `results` 的数量必须与输入记录数量完全相同；
2. 每个输入 `record_id` 必须恰好出现一次，不能改写、遗漏或重复；
3. 每篇只依据自己的元数据判断，不得把其他记录的信息混入；
4. 保持说明简洁，候选记录概要一至两句，理由和证据各一至两句。
