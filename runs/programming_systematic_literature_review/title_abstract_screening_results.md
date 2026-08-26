# 题名—摘要—关键词筛选结果

本报告是可重复生成的阶段性结果。题录筛选只决定是否进入全文复核，不能替代最终纳入判断。

## 流量

- 去重后的输入记录：5,642
- 第一轮已完成：5,642
- 第一轮候选（include + uncertain）：3,036
- 第一轮排除：2,606
- 第二轮已完成：3,036
- 两轮均纳入：2,136
- 第一轮保留、第二轮排除（需全文裁决）：765
- 第二轮不确定（需全文裁决）：135

| 第一轮标签 | 数量 |
| --- | --- |
| include_candidate | 2799 |
| exclude | 2606 |
| uncertain | 237 |

| 第二轮标签（只对第一轮候选） | 数量 |
| --- | --- |
| include_candidate | 2136 |
| exclude | 765 |
| uncertain | 135 |

## 检索渠道覆盖

| 渠道 | 去重后涉及记录数 |
| --- | --- |
| authoritative_outlet_search | 4899 |
| forward_citation_of_20_seeds | 788 |
| local_fulltext_seed_28 | 28 |

## 两轮一致纳入记录的题录概览

### 主体

| 主体 | 数量 |
| --- | --- |
| human_only | 1390 |
| agent_only | 492 |
| human_ai | 214 |
| unclear | 39 |
| not_applicable | 1 |

### 程序制品

| 制品 | 数量 |
| --- | --- |
| source_code | 1792 |
| low_code_or_visual | 131 |
| spreadsheet_logic | 87 |
| database_query | 55 |
| other_executable_logic | 50 |
| unclear | 21 |

### 编程行动

| 行动 | 数量 |
| --- | --- |
| debug_or_repair | 671 |
| write | 645 |
| understand | 559 |
| inspect_or_review | 268 |
| test | 244 |
| modify_or_refactor | 228 |
| generate | 176 |
| complete | 82 |

### 研究类型

| 研究类型 | 数量 |
| --- | --- |
| unclear | 2116 |
| empirical_human | 11 |
| tool_design_and_evaluation | 5 |
| empirical_artifact_or_agent | 4 |

### 分析层级

| 层级 | 数量 |
| --- | --- |
| unclear | 2116 |
| individual | 14 |
| code_artifact_or_agent | 5 |
| not_applicable | 1 |

### 年代

| 年代 | 数量 |
| --- | --- |
| 2021–2026 | 876 |
| 2011–2020 | 731 |
| 2001–2010 | 371 |
| ≤2000 | 158 |

### 候选最多的来源（前 25）

| 来源 | 数量 |
| --- | --- |
| Proceedings - International Conference on Software Engineering | 408 |
| IEEE Transactions on Software Engineering | 205 |
| Conference on Human Factors in Computing Systems - Proceedings | 150 |
| Empirical Software Engineering | 132 |
| Proceedings of IEEE Symposium on Visual Languages and Human-Centric Computing, VL/HCC | 101 |
| Annual Conference on Innovation and Technology in Computer Science Education, ITiCSE | 94 |
| Journal of Systems and Software | 93 |
| ACM Transactions on Software Engineering and Methodology | 93 |
| Information and Software Technology | 83 |
| International Symposium on Empirical Software Engineering and Measurement | 30 |
| Software Quality Journal | 27 |
| SIGCSE TS 2025 - Proceedings of the 56th ACM Technical Symposium on Computer Science Education | 24 |
| Proceedings of the Conference on Integrating Technology into Computer Science Education, ITiCSE | 22 |
| Proceedings of the International Conference on Software Engineering and Knowledge Engineering, SEKE | 21 |
| International Journal of Human Computer Studies | 21 |
| Computer Science Education | 18 |
| SIGCSE 2024 - Proceedings of the 55th ACM Technical Symposium on Computer Science Education | 18 |
| SIGCSE 2015 - Proceedings of the 46th ACM Technical Symposium on Computer Science Education | 17 |
| SIGCSE 2021 - Proceedings of the 52nd ACM Technical Symposium on Computer Science Education | 13 |
| SIGCSE 2019 - Proceedings of the 50th ACM Technical Symposium on Computer Science Education | 12 |
| Proceedings - 2011 IEEE Symposium on Visual Languages and Human Centric Computing, VL/HCC 2011 | 12 |
| SIGCSE Bulletin (Association for Computing Machinery, Special Interest Group on Computer Science Education) | 12 |
| SIGCSE'08 - Proceedings of the 39th ACM Technical Symposium on Computer Science Education | 11 |
| SIGCSE TS 2026 - Proceedings of the 57th ACM Technical Symposium on Computer Science Education V.1 | 10 |
| Proceedings - 2020 ACM/IEEE 42nd International Conference on Software Engineering: Companion, ICSE-Companion 2020 | 10 |

## 解释限制

- 这是题录阶段的高召回结果；主体、方法、层级和理论均可能因摘要信息不足而在全文阶段修正。
- `agent_only` 技术评测、`human_ai` 交互研究与 `human_only` 认知/行为研究将在综合时分层，不直接合并。
- 第一轮与第二轮冲突项不会自动排除，而进入全文裁决。
