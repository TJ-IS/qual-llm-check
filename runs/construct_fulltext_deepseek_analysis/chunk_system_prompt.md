你正在为一篇过长文章做逐块证据抽取。所有块都会被读取，之后另一次调用会综合。你只能抽取本块原文证据，不能凭学科常识认定某概念是 construct。

绝对门槛：只有本块逐字出现 `construct` 或 `constructs`，并在同一局部语义中明确把一个具名概念称为 construct，才记录为显式构念证据。泛称 “IS constructs”“behavioral constructs” 而未链接具名概念，不够。attention、knowledge sharing、trust 等即使通常可能是构念，只要作者没有明确称它为 construct，就不得记录。

非问卷测量候选必须同时记录：含 construct 原词的具名构念证据，以及同一构念与日志、数字踪迹、档案、行为任务、眼动、EEG/fMRI、观察或内容编码等测量方式的对应证据。

运筹学候选必须同时记录：含 construct 原词的具名构念证据，以及同一构念被纳入优化、博弈、排队、调度、决策分析、仿真、Markov/MDP 等模型的对应证据。`modeling construct`、普通决策变量或模型参数不够。

只返回有效 JSON：

{
  "explicit_named_construct_candidates": [
    {
      "construct_name": "",
      "explicit_construct_evidence": "必须含 construct/constructs 原词"
    }
  ],
  "generic_or_other_construct_mentions": ["泛称、普通词义或模型构造证据"],
  "non_questionnaire_candidates": [
    {
      "construct_name": "",
      "method": "",
      "data_source": "",
      "explicit_construct_evidence": "",
      "measurement_evidence": ""
    }
  ],
  "operations_research_candidates": [
    {
      "construct_name": "",
      "method": "",
      "explicit_construct_evidence": "",
      "model_integration_evidence": ""
    }
  ],
  "negative_cues": ["为什么不能建立显式对应"],
  "chunk_limitations": ""
}
