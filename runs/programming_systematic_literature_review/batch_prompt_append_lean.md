## 本次调用的批量初筛输出

用户消息会提供多篇彼此独立的题名—摘要—关键词记录。本阶段只做相关性初筛，不抽取方法、变量、层级、理论或完整概要；这些内容留到全文编码。

只返回：

{
  "results": [
    {
      "record_id": "原样复制输入的 record_id",
      "screening_label": "include_candidate|uncertain|exclude",
      "programming_centrality": "programming_core|programming_as_context|not_programming|unclear",
      "actor_type": "human_only|human_ai|agent_only|unclear|not_applicable",
      "program_artifact": "source_code|database_query|spreadsheet_logic|low_code_or_visual|other_executable_logic|unclear|not_applicable",
      "programming_actions": ["write|generate|complete|understand|inspect_or_review|debug_or_repair|modify_or_refactor|test"],
      "decision_reason_cn": "不超过35个汉字",
      "metadata_evidence_cn": "不超过35个汉字",
      "confidence": 0.0
    }
  ]
}

硬性要求：

1. `results` 数量必须与输入数量相同；
2. 每个输入 `record_id` 必须原样、恰好返回一次；
3. 每篇只依据自己的元数据，不混入其他记录；
4. 理由和证据各写一个短句，不展开讨论；
5. 信息不足时用 `uncertain`，不要用长篇推理弥补摘要缺失。
