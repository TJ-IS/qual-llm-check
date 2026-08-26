# 识别池分析

## 流量与完整性

- 原始输入行：5,816（各渠道相加，含重叠）
- 去重后题录：5,642
- 具有摘要：5,642
- 缺摘要：0
- 2021–2026：2,105

| 原始渠道 | 输入行 |
| --- | --- |
| authoritative_outlet_search | 4981 |
| forward_citation_of_20_seeds | 807 |
| local_fulltext_seed_28 | 28 |

## 渠道重叠

| 去重后渠道组合 | 记录数 |
| --- | --- |
| authoritative_outlet_search | 4839 |
| forward_citation_of_20_seeds | 732 |
| authoritative_outlet_search + forward_citation_of_20_seeds | 43 |
| authoritative_outlet_search + forward_citation_of_20_seeds + local_fulltext_seed_28 | 11 |
| local_fulltext_seed_28 | 9 |
| authoritative_outlet_search + local_fulltext_seed_28 | 6 |
| forward_citation_of_20_seeds + local_fulltext_seed_28 | 2 |

## 年份（前 20 个高频年份）

| 年份 | 题录数 |
| --- | --- |
| 2024 | 417 |
| 2025 | 412 |
| 2023 | 398 |
| 2022 | 374 |
| 2021 | 279 |
| 2018 | 275 |
| 2020 | 269 |
| 2019 | 253 |
| 2026 | 225 |
| 2017 | 188 |
| 2014 | 185 |
| 2015 | 182 |
| 2011 | 173 |
| 2013 | 171 |
| 2016 | 162 |
| 2008 | 160 |
| 2010 | 154 |
| 2012 | 151 |
| 2006 | 122 |
| 2009 | 115 |

## 来源（前 30）

| 来源 | 题录数 |
| --- | --- |
| Proceedings - International Conference on Software Engineering | 1098 |
| IEEE Transactions on Software Engineering | 601 |
| Empirical Software Engineering | 384 |
| Journal of Systems and Software | 342 |
| Conference on Human Factors in Computing Systems - Proceedings | 281 |
| Information and Software Technology | 273 |
| ACM Transactions on Software Engineering and Methodology | 238 |
| Proceedings of IEEE Symposium on Visual Languages and Human-Centric Computing, VL/HCC | 148 |
| Annual Conference on Innovation and Technology in Computer Science Education, ITiCSE | 143 |
| International Symposium on Empirical Software Engineering and Measurement | 97 |
| Software Quality Journal | 73 |
| Proceedings of the International Conference on Software Engineering and Knowledge Engineering, SEKE | 72 |
| SIGCSE TS 2025 - Proceedings of the 56th ACM Technical Symposium on Computer Science Education | 41 |
| The Journal of Systems and Software | 39 |
| SIGCSE Bulletin (Association for Computing Machinery, Special Interest Group on Computer Science Education) | 36 |
| Computer Science Education | 33 |
| Decision Support Systems | 33 |
| Proceedings of the Conference on Integrating Technology into Computer Science Education, ITiCSE | 33 |
| Journal of the Association for Information Systems | 29 |
| International Journal of Human Computer Studies | 28 |
| SIGCSE 2024 - Proceedings of the 55th ACM Technical Symposium on Computer Science Education | 26 |
| 36th International Conference on Software Engineering, ICSE Companion 2014 - Proceedings | 24 |
| Information Systems Research | 23 |
| MIS Quarterly: Management Information Systems | 22 |
| Proceedings - 2017 IEEE/ACM 39th International Conference on Software Engineering Companion, ICSE-C 2017 | 21 |
| Information and Management | 20 |
| Journal of Management Information Systems | 20 |
| Proceedings - 2020 ACM/IEEE 42nd International Conference on Software Engineering: Companion, ICSE-Companion 2020 | 20 |
| SIGCSE 2015 - Proceedings of the 46th ACM Technical Symposium on Computer Science Education | 20 |
| Proceedings - 2004 IEEE Symposium on Visual Languages and Human Centric Computing | 20 |

## 解释

识别池不是相关文献集。权威来源概念检索会包含大量因短语多义、技术工具或项目背景造成的噪声；施引记录也只证明引用关系。所有 5,642 条必须走同一 eligibility criteria。
