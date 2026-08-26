# 方法模仿依据与逐项对应

本项目不是泛称“遵循系统综述规范”，而是把四篇发表于 MISQ、ISR、JAIS、JMIS 的原文做法拆成可核查的操作。下表区分“原文确实做了什么”“本项目照着做什么”和“本项目不得声称完全复制的差异”。

## 1. MIS Quarterly：Cram, D’Arcy, and Proudfoot (2019)

**文献：** W. Alec Cram, John D’Arcy, and Jeffrey G. Proudfoot. “Seeing the Forest and the Trees: A Meta-Analysis of the Antecedents to Information Security Policy Compliance.” *MIS Quarterly*, 43(4), 2019. DOI: 10.25300/MISQ/2019/15117。

**原文定位：** `Literature Search` 与 `Inclusion Criteria`。本地全文为 `database_fulltext_all/12802_2019_seeing-the-forest-i-and-i-the-trees-a-meta-analysis-of-the-antecedents-to-information-security-p.md`，重点见第 102–126 行。

**原文流量：** 1,698 篇期刊论文、最终 158 篇会议记录、925 篇学位论文和 15 篇未发表论文进入识别池；最终纳入 61 + 24 + 9 + 1 = 95 篇。

| 原文方法 | 本项目的准确模仿 | 差异与限制 |
|---|---|---|
| 预先说明检索截止时间、数据库、检索词、初始数量 | 冻结 2026-07-26 检索日期、Scopus 字段、完整检索式、来源范围和 4,981 条初始结果 | 原文用了 ABI/Inform、ACM DL、Business Source Premier、JSTOR；本项目主检索使用 Scopus，不声称数据库相同 |
| 期刊之外搜索 AIS 会议和学位论文以降低发表偏差 | 主检索纳入高质量 IS/SE/HCI/CS 教育会议；施引渠道不限制来源类型 | 当前未单独系统搜索学位论文，因此不能声称已经复制其灰色文献覆盖 |
| 对初始合格论文做 backward search，并用 Google Scholar 做 forward search | 对 20 篇人工确认核心种子做 Scopus 正向施引检索，得到 807 条记录；最终纳入后还要做参考文献回溯 | 当前正向检索平台是 Scopus，不是 Google Scholar；参考文献回溯将在全文纳入集上执行 |
| 明确列出纳入标准和分析层级 | 预先冻结“编程必须是不可替换的核心对象”、程序制品、行动、主体和排除项 | 本项目不限制为一种实证方法或一个层级，因为研究问题不同 |

## 2. Information Systems Research：Eisend (2019)

**文献：** Martin Eisend. “Explaining Digital Piracy: A Meta-Analysis.” *Information Systems Research*, 30(2), 2019, 636–664. DOI: 10.1287/isre.2018.0821。

**原文定位：** `Data Collection and Coding`。本地全文为 `database_fulltext_all/00350_2019_explaining-digital-piracy-a-meta-analysis.md`，重点见第 188–198 行。

**原文流量与一致性：** 初始得到 174 份可用 manuscript、185 个独立样本研究；最终综合 164 份 manuscript、174 个独立样本。两名编码者初始一致率 93%，新增类别的一致率 95%。

| 原文方法 | 本项目的准确模仿 | 差异与限制 |
|---|---|---|
| 从已有综述出发，查其参考文献和全部施引文献，再做数据库关键词检索 | 同时维护概念检索渠道、20 篇核心种子的施引渠道和本地种子渠道，合并后去重 | 本项目不是从一篇既有综述出发，而是从全文筛选确认的 20 篇核心种子出发 |
| 每识别一篇研究，再检查其参考文献 | 在全文确认纳入后，对其参考文献做回溯，新增记录重新走相同筛选 | 题录初筛阶段尚未完成这一轮 |
| 明确排除错误分析层级，并区分 manuscript 与 independent sample | 编码 individual/dyad/team/organization/project/artifact-agent 层级；最终综合时区分论文数与独立样本/研究数 | 题名摘要通常不足以识别复用样本，必须在全文阶段完成 |
| 两名编码者独立编码，初始一致率 93%，争议讨论解决 | 候选记录用两次相互独立的模型判断；冲突和不确定项由人工查全文裁决 | 这不是“两名人类编码者”，不得把模型复核等同于原文的双人编码，也不得虚报一致率 |

## 3. Journal of the Association for Information Systems：Diederich et al. (2022)

**文献：** Stephan Diederich, Alfred Benedikt Brendel, Stefan Morana, and Lutz Kolbe. “On the Design of and Interaction with Conversational Agents: An Organizing and Assessing Review of Human-Computer Interaction Research.” *Journal of the Association for Information Systems*, 23(1), 2022. DOI: 10.17705/1jais.00724。

**原文定位：** `Identification, Coding, and Analysis of CA Literature`。本地全文为 `database_fulltext_all/11232_2022_on-the-design-of-and-interaction-with-conversational-agents-an-organizing-and-assessing-review-o.md`，重点见第 111–127 行。

**原文流量：** 单一概念式返回 8,768 条；扫描题名、摘要和内容并做正反向搜索后保留 262 项。

| 原文方法 | 本项目的准确模仿 | 差异与限制 |
|---|---|---|
| 因主题横跨 IS 与 CS/HCI，目的性选择两个学科的权威期刊，并为新兴主题加入重要会议 | 权威来源主检索同时覆盖 Basket/核心 IS、SE、HCI、CS 教育期刊和重要会议 | 本项目所选来源集合按“个人或智能体直接编程”重新界定，不复制其会话智能体来源清单 |
| 维护一个简洁、稳定的概念检索式，而非许多不同形式的主检索式 | 只使用一条 TITLE-ABS-KEY 概念式；各术语是同一式中的同义/活动词，不作为不同方案分别运行 | 本项目因编程活动词汇比 CA 更分散，短语数量更多，但仍是一条冻结的主检索式 |
| 扫描 title、abstract、content，并做 forward/backward search | 题名摘要关键词初筛 → 候选全文复核 → 正反向引文补充 | Scopus 主检索严格限于 TITLE-ABS-KEY，这是用户要求；原文还扫描 content |
| 编码研究方法、分析单位和理论基础，并用 concept matrix 组织分析 | 输出行动、主体、程序制品、研究方法、分析单位、理论、变量和结论的概念矩阵 | 聚类只在资料规模和概念分布支持时使用，不机械复制原文的 cluster analysis |

### JAIS 的方法反例检查：Larsen et al. (2019)

**文献：** Kai R. Larsen, Zakariya Voronovich, Brian Cook, and Julia Pedro. “Understanding the Elephant: The Discourse Approach to Boundary Identification and Corpus Construction for Theory Review Articles.” *Journal of the Association for Information Systems*, 20(7), 2019. DOI: 10.17705/1jais.00556。

**原文定位：** 本地全文 `database_fulltext_all/12268_2019_understanding-the-elephant-the-discourse-approach-to-boundary-identification-and-corpus-construc.md`，重点见第 39–67、195–207 行。

这篇文章要求把 **boundary identification**（找出所有可能相关的研究边界）与 **corpus construction**（按纳入标准选出实际分析语料）分开，并明确警告：如果目标是声称覆盖整个研究领域，只搜索任意一组顶刊会产生系统偏差。它主张用基础文献、施引文献和这些文献的参考文献形成 citation ecosystem；当边界过大时，可用机器学习或随机抽样构造有代表性的语料。

本项目因此不能把 4,981 条“权威来源主检索”单独称为全领域穷尽检索。准确表述是：

1. 权威来源检索定义一个可完全枚举的 **bounded outlet corpus**，模仿 Diederich et al.；
2. 20 篇种子的 807 条不受来源限制的施引记录扩展边界，模仿 Larsen et al. 的 discourse/citation ecosystem 思路；
3. 目前尚未完成“每篇施引文献的全部参考文献”这一完整 ecosystem，因此最终报告只可声称“权威来源系统综述 + 引文扩展”，不能声称覆盖所有学科、所有来源的全球全集；
4. DeepSeek 题录分类承担大边界下的机器辅助 corpus construction，但所有冲突和最终纳入仍需人工全文裁决。

## 4. Journal of Management Information Systems：Qahri-Saremi and Montazemi (2019)

**文献：** Hamed Qahri-Saremi and Ali Reza Montazemi. “Factors Affecting the Adoption of an Electronic Word of Mouth Message: A Meta-Analysis.” *Journal of Management Information Systems*, 36(3), 2019, 969–1001. DOI: 10.1080/07421222.2019.1628936。

**原文定位：** 文献检索与选择部分。本地全文为 `database_fulltext_all/12278_2019_factors-affecting-the-adoption-of-an-electronic-word-of-mouth-message-a-meta-analysis.md`，重点见第 162–170 行。

**原文流量：** 597 篇 → 167 篇（研究目标）→ 137 篇（定量实证）→ 79 篇（可获得效应量）→ 87 个独立 primary studies（多样本拆分、重复样本合并）。

| 原文方法 | 本项目的准确模仿 | 差异与限制 |
|---|---|---|
| 改造 PRISMA，报告 597→167→137→79→87 independent studies 的逐阶段数量 | 保存识别、去重、题录排除、全文排除、引文新增和最终纳入数量，并给出排除理由 | 本项目是组织与评估型 SLR，不进行效应量元分析 |
| 预先建立三项 eligibility criteria | 预先建立对象、活动、程序制品、核心性和排除边界；所有渠道走同一套规则 | 具体标准按本项目研究问题重新定义 |
| 两位作者分别筛选，争议用 consensus 解决 | 两次独立模型筛选后对分歧项做人工全文裁决，并保留每次判断 | 只有一名人类研究者时，不声称“two authors separately assessed”；报告为 AI 辅助筛选加人工裁决 |
| 编码时检查实际测量工具和概念内容，而不只看作者标签 | 判断“编程是否为研究核心”时看实际任务、操纵、测量和制品，不因 programmer/developer/code 标签直接纳入 | 在题录阶段只能初判；内容一致性必须在全文阶段确认 |

## 5. 本项目最终采用的组合

本项目最接近 Diederich et al. (2022) 的“权威跨学科来源 + 一条稳定概念式 + concept matrix”总体架构；用 Cram et al. (2019) 与 Eisend (2019) 的正反向引文链补足检索词召回；用 Qahri-Saremi and Montazemi (2019) 的阶段流量、预设标准和共识裁决组织筛选；再用 Larsen et al. (2019) 约束覆盖范围的表述，避免把顶刊范围误称为整个学术领域。四篇期刊实证综述和一篇 JAIS 方法论文没有任何一篇单独等于本项目流程，因此报告必须称为“基于原文做法的组合与适配”，不能称为逐字复制某一篇。
