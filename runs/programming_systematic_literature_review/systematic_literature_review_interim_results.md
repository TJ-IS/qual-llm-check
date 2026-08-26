# 人或智能体直接编程研究：系统文献综述阶段性结果

检索与筛选日期：2026-07-26

## 一、结论先行

本综述采用的是**有界权威来源系统综述 + 不限来源的种子施引扩展**，而不是仅搜索 AIS Basket，也不是宣称穷尽全球所有来源。

最重要的阶段性发现有三点：

1. **近期研究并不少。** 去重后的 5,642 条记录中有 2,105 条发表于 2021–2026；两轮题名—摘要判断一致保留的 2,136 条候选中，有 876 条发表于 2021–2026。
2. **“AIS 顶刊里近期很少”是发表场所迁移，不是研究主题消失。** 两轮一致候选中，MISQ、ISR、JAIS、JMIS 合计只有 17 条，2021 年以后只有 1 条；同期候选大量分布于 ICSE、TSE、CHI、EMSE、TOSEM、JSS、IST、VL/HCC 和计算机教育会议。
3. **人—AI 直接编程已形成明显的新文献流。** 题名—摘要两轮一致的 human–AI 候选有 214 条，其中 2024–2026 年有 116 条；最常见行动是调试/修复、编写、生成、理解、检查、重构和测试。但这 214 条仍是全文候选，不能直接当作最终纳入研究。

当前已经完成识别、去重、两阶段题录筛选和 31 篇本地可得全文的复核；尚缺 3,005 篇候选全文，因此本文件是**阶段性分析**，不是可以投稿时声称“全文筛选完毕”的最终 SLR。

## 二、研究问题与边界

研究关注个人或智能体直接：

- 编写、生成或补全程序；
- 理解、阅读或解释程序；
- 检查、审查、调试或修复程序；
- 修改、重构或测试程序。

程序包括源代码、可执行 SQL 查询、电子表格公式/脚本，以及低代码、可视化或终端用户编程产生的可执行逻辑。

核心纳入原则是“不可替换测试”：如果把程序员替换为一般知识工作者、把代码或可执行逻辑替换为一般工作产出后，研究问题、处理、主要测量和结论仍基本成立，则编程只是背景，不进入直接编程核心语料。

## 三、具体模仿了哪些权威文献

本项目没有笼统声称“遵循 AIS 规范”，而是从四本目标期刊的五篇原文中抽取了可核查的操作。完整逐项交叉表见 `method_reference_crosswalk.md`。

### 1. MIS Quarterly：Cram, D’Arcy, and Proudfoot (2019)

文献：*Seeing the Forest and the Trees: A Meta-Analysis of the Antecedents to Information Security Policy Compliance*，MIS Quarterly, 43(4)，DOI 10.25300/MISQ/2019/15117。

原文做法（本地全文第 102–126 行）：

- 预先报告检索截止日期、数据库、检索词和各阶段数量；
- 搜索 ABI/Inform、ACM DL、Business Source Premier、JSTOR，且不限制发表期刊；
- 额外搜索 AIS 会议、学位论文和未发表研究；
- 对初步合格文章做参考文献回溯和 Google Scholar 正向施引搜索；
- 最终从 1,698 篇期刊记录、158 篇会议记录、925 篇学位论文和 15 篇未发表记录中纳入 95 篇。

本项目准确采用：

- 冻结检索日期、Scopus 字段、完整检索式、来源清单和初始数量；
- 把重要 IS、SE、HCI 和 CS 教育会议纳入权威来源主检索；
- 对 20 篇人工确认核心种子执行不限来源的 Scopus 正向施引搜索；
- 保存各渠道、去重和筛选阶段的数量。

没有复制的部分：

- 本项目主数据库是 Scopus，不是原文的四个数据库；
- 尚未系统检索学位论文和未发表研究；
- 尚未对最终纳入集完成逐篇参考文献回溯。

### 2. Information Systems Research：Eisend (2019)

文献：*Explaining Digital Piracy: A Meta-Analysis*，Information Systems Research, 30(2)，DOI 10.1287/isre.2018.0821。

原文做法（本地全文第 188–198 行）：

- 从既有综述及其参考文献、所有施引文献出发，再做数据库关键词搜索；
- 每发现一篇研究就检查其参考文献；
- 明确排除不符合分析层级的国家聚合数据，保留个体层面研究；
- 区分 manuscript 与 independent sample；
- 两名编码者独立编码，初始一致率 93%，新类别一致率 95%，分歧通过讨论解决。

本项目准确采用：

- 组合概念检索、20 篇核心种子的施引检索和本地已知种子保障；
- 单独编码 individual、dyad、team、organization、project/community、code artifact/agent 等分析层级；
- 在全文综合中记录重复样本，例如 1995 ISR 与 1998 JMIS 的程序理解研究共用 24 名 COBOL 程序员和同一套任务。

没有复制的部分：

- 本项目的两次题录判断是两次相互独立的模型判断，不是两名人类编码者；
- 第一轮排除的 2,606 条没有再次进入第二轮，第二轮只复核第一轮保留的 3,036 条；
- 因此不得报告人类编码者一致率，也不得把模型一致性写成原文的 93%/95% 人际一致性。

### 3. Journal of the Association for Information Systems：Diederich et al. (2022)

文献：*On the Design of and Interaction with Conversational Agents: An Organizing and Assessing Review of Human-Computer Interaction Research*，JAIS, 23(1)，DOI 10.17705/1jais.00724。

这是本项目最主要的结构模板。原文做法（本地全文第 111–129 行）：

- 因主题横跨 IS 与 HCI/CS，目的性选择 Basket of Eight、四本 HCI 期刊、重要 IS 会议和 CHI；
- 维护一条简洁、稳定的概念检索式；
- 8,768 条结果经过题名、摘要、内容扫描及正反向搜索后保留 262 篇；
- 按研究方法、分析层级、理论基础和框架维度建立 concept matrix；
- 三名作者用 20 篇随机论文预试编码指南，讨论后修订，再由一名作者编码其余研究并讨论疑难项。

本项目准确采用：

- 用一条冻结的 TITLE-ABS-KEY 概念式，而不是维护许多彼此重叠的主检索式；
- 预先指定 IS、SE、HCI 和 CS 教育权威期刊/会议；
- 建立编程行动、主体、程序制品、研究方法、分析层级、理论、变量、结论和人—智能体关系的概念矩阵；
- 先用 20 篇人工确认核心文献和 8 篇边界文献校准筛选规则。

没有复制的部分：

- 原文还扫描正文内容，本项目的 Scopus 主检索严格使用用户指定的题名、摘要、关键词字段；
- 本项目的来源清单是按直接编程主题重新定义的，不能复制对话智能体综述的来源清单；
- 当前不机械复制原文的聚类分析，因为全文概念矩阵尚不完整。

### 4. JAIS 方法约束：Larsen et al. (2019)

文献：*Understanding the Elephant: The Discourse Approach to Boundary Identification and Corpus Construction for Theory Review Articles*，JAIS, 20(7)，DOI 10.17705/1jais.00556。

原文做法（本地全文第 39–67、195–207 行）：

- 严格区分 boundary identification 与 corpus construction；
- 明确批评用一组顶级期刊冒充整个研究领域的完整边界；
- 用基础文献、施引文献及其参考文献构成 citation ecosystem；
- 当领域太大时，可用机器学习或随机抽样构造具有代表性的分析语料。

本项目准确采用：

- 把 4,981 条权威来源检索定义为可枚举的 bounded outlet corpus，而非全球全集；
- 加入 807 条不限来源的核心种子施引记录扩展边界；
- 把模型筛选定位为大边界下的辅助 corpus construction；
- 在完整回溯未完成前，只声称“有界权威来源系统综述 + 引文扩展”。

### 5. Journal of Management Information Systems：Qahri-Saremi and Montazemi (2019)

文献：*Factors Affecting the Adoption of an Electronic Word of Mouth Message: A Meta-Analysis*，JMIS, 36(3)，DOI 10.1080/07421222.2019.1628936。

原文做法（本地全文第 161–170 行）：

- 采用经调整的 PRISMA 思路报告阶段流量；
- 先规定“研究目标、定量实证、具备效应量数据”三项 eligibility criteria；
- 两位作者分别评估 597 篇记录，讨论分歧并达成共识；
- 报告 597 → 167 → 137 → 79 → 87 个独立 primary studies 的筛选过程；
- 判断构念一致性时检查实际测量工具和内容，而不是只看作者标签。

本项目准确采用：

- 预先冻结对象、动作、程序制品、核心性和排除规则；
- 保留识别、去重、第一轮排除、第二轮冲突/不确定、全文可得性和全文排除理由；
- 判断“直接编程”时看实际任务、处理、测量和制品，不因标题出现 programmer、developer、code 就自动纳入；
- 保存两次模型输出，由人工全文裁决边界项。

没有复制的部分：

- 当前不是两位人类作者分别筛选全部记录；
- 本项目是组织与评价型综述，不进行效应量元分析；
- 3,005 篇全文尚未获得，故 PRISMA 式全文阶段尚未闭合。

## 四、冻结的检索设计

### 1. 主检索

在 Scopus 的 TITLE-ABS-KEY 字段运行一条冻结概念式，覆盖 program/code comprehension、code review/inspection、debugging/repair、modification/refactoring、testing/completion、pair programming、TDD、query formulation/development/reuse、end-user programming、spreadsheet development/error/testing、AI-assisted programming、AI coding assistant 和 coding agent 等直接编程活动。

完整检索式与全部来源名称见 `search_protocol_v2.md`。

### 2. 来源范围

- AIS/IS：MISQ、ISR、JAIS、JMIS、Basket 其他期刊及 DSS、I&M 等；
- 软件工程：TSE、TOSEM、EMSE、JSS、IST、Software Quality Journal、ICSE 等；
- HCI：TOCHI、CHI、IJHCS、VL/HCC 等；
- CS 教育：Computer Science Education、Computers & Education、SIGCSE、ITiCSE 等。

### 3. 补充渠道

- 20 篇人工确认核心种子的 Scopus 正向施引检索：807 条；
- 本地 28 条直接或边界种子保障；
- 最终全文纳入集的逐篇参考文献回溯：尚待完成。

## 五、检索与筛选流量

| 阶段 | 数量 |
|---|---:|
| 权威来源主检索 | 4,981 |
| 20 篇种子的不限来源施引记录 | 807 |
| 本地种子保障 | 28 |
| 原始渠道记录合计（含重叠） | 5,816 |
| 去重后记录 | 5,642 |
| 具有摘要 | 5,642 |
| 第一轮排除 | 2,606 |
| 第一轮保留进入第二轮 | 3,036 |
| 两轮一致保留 | 2,136 |
| 第一轮保留、第二轮排除，需全文裁决 | 765 |
| 第二轮不确定，需全文裁决 | 135 |
| 本地解析到候选全文 | 31 |
| 尚缺候选全文 | 3,005 |
| 本地全文人工裁决为直接编程 | 29 |
| 本地全文裁决为团队情境背景 | 1 |
| 本地全文裁决为非编程含义 | 1 |

第一轮曾有 160 条记录位于失败批次，第二轮曾有 16 条记录位于失败批次；所有记录后来均重试成功，当前未解决错误为 0。

## 六、检索召回审计

### 1. 已知 28 篇本地记录

- 权威来源主检索找回 17 条；
- 种子施引渠道找回 13 条；
- 三个渠道合并后找回 28/28。

主检索没有独立找回的记录不全是缺关键词：部分不在预设来源，部分老记录的题名摘要不用当前术语。这证明单独依赖一条数据库式并不够。

### 2. 近期施引验证集

- 30 条 `likely_direct` 近期施引候选：主检索找回 11，施引渠道找回 30，合并找回 30/30；
- 加上 3 条 `possible_direct` 后：主检索找回 11，合并找回 33/33。

这个审计只能证明渠道对已知验证集的召回，不能证明对全部 Scopus 或全球文献达到 100% 召回。尤其是完全不引用旧种子的 Copilot、Codex 和 coding-agent 研究主要依靠概念检索发现。

## 七、题名—摘要阶段的实质结果

### 1. 年代

两轮一致保留的 2,136 条候选中：

| 年代 | 数量 |
|---|---:|
| 2021–2026 | 876 |
| 2011–2020 | 731 |
| 2001–2010 | 371 |
| 2000 及以前 | 158 |

因此，“直接编程研究普遍很老”只适用于传统 AIS 顶刊子集，不适用于跨学科研究边界。

### 2. 发表场所迁移

两轮一致候选最多的来源为：

| 来源 | 候选数 |
|---|---:|
| ICSE | 408 |
| IEEE Transactions on Software Engineering | 205 |
| CHI | 150 |
| Empirical Software Engineering | 132 |
| VL/HCC | 101 |
| ITiCSE | 94 |
| Journal of Systems and Software | 93 |
| ACM TOSEM | 93 |
| Information and Software Technology | 83 |

MISQ、ISR、JAIS、JMIS 合计只有 17 条两轮一致候选，且 2021 年以后只有 JMIS 2023 的 *Leveraging Low Code Development of Smart Personal Assistants*。这意味着如果综述只看四本 AIS 顶刊，会系统性漏掉生成式 AI 编程、代码补全、智能体工作流、编程教育与开发者工具的近期主流研究。

### 3. 研究主体

| 主体 | 两轮一致候选数 |
|---|---:|
| human_only | 1,390 |
| agent_only | 492 |
| human_ai | 214 |
| unclear | 39 |
| not_applicable | 1 |

`agent_only` 多是工具或模型评测，`human_ai` 才更接近个人使用 Codex/Copilot/编程智能体的行为研究；两者不能混合解释。

### 4. 程序制品与行动

| 程序制品 | 数量 |
|---|---:|
| 源代码 | 1,792 |
| 低代码/可视化程序 | 131 |
| 电子表格逻辑 | 87 |
| 数据库查询 | 55 |
| 其他可执行逻辑 | 50 |
| 不清楚 | 21 |

| 编程行动 | 数量 |
|---|---:|
| 调试/修复 | 671 |
| 编写 | 645 |
| 理解 | 559 |
| 检查/审查 | 268 |
| 测试 | 244 |
| 修改/重构 | 228 |
| 生成 | 176 |
| 补全 | 82 |

这些数字是多标签计数，不能相加为论文数。

### 5. 人—AI 直接编程候选

214 条 human–AI 候选的时间分布明显集中于生成式 AI 之后：

- 2024：34 条；
- 2025：49 条；
- 2026（截至检索日）：33 条；
- 三年合计：116 条。

其高频行动为调试/修复 71、编写 70、生成 66、理解 38、检查/审查 30、修改/重构 28、补全 25、测试 19。主要来源是 CHI、ICSE、VL/HCC、TSE、EMSE、TOSEM、JSS、SIGCSE 和 ITiCSE。

这批候选已经出现与研究个人使用编程智能体高度贴近的方向：控制 AI 自动化程度、AI 辅助重构、生成式 AI 下的代码理解、AI 代码采纳、LLM 辅助代码审查、智能体式调试、眼动测量的 Copilot 依赖、非程序员借助 AI 编程等。完整候选清单见 `two_pass_human_ai.md`。

## 八、本地 31 篇全文的人工裁决

DeepSeek 全文编码原始结果为 30 篇纳入、1 篇排除。人工复核后作出一项关键纠正：

- 2019 ISR 的 *How Pair Programming Influences Team Performance* 不进入直接编程核心。原文主动把重点从个人/配对任务转到团队层面，研究的是 shared mental models、backup behavior、task novelty 和 team performance，数据为 62 个软件团队的多来源问卷。它只能作为编程团队情境背景。

另一篇 *Computer-Aided Model Construction* 的 model construction 是决策/运筹模型构建，不是程序编写，维持排除。

裁决后：

- 29 篇直接编程研究；
- 1 篇编程团队情境背景；
- 1 篇非编程含义。

11 篇新补配全文的逐篇裁决和依据见 `local_fulltext_human_adjudication.md`；原始模型输出保留在 `output_fulltext_local_v1/decisions.csv`。

## 九、目前能够与不能够得出的结论

### 可以得出

- 一条稳定概念式与种子施引渠道明显互补；
- 传统 AIS 顶刊中的直接编程研究确实较少且偏旧；
- 近期直接编程研究已经大量迁移到软件工程、HCI 和 CS 教育期刊/会议；
- human–AI 直接编程研究在 2024–2026 明显增长，并覆盖编写、生成、理解、重构、调试、审查和测试；
- 只使用 Basket 或四本 AIS 顶刊不能形成对当前编程智能体研究的充分覆盖。

### 不能得出

- 2,136 条两轮一致候选就是最终纳入数量；
- 214 条 human–AI 候选都经过全文确认；
- 当前检索穷尽了所有学科、所有数据库和灰色文献；
- 当前模型筛选等同于两名人类作者独立筛选；
- 当前已经完成投稿所需的全文排除流量、质量评价、独立样本识别和最终参考文献回溯。

## 十、下一步

投稿级 SLR 还需：

1. 获取 3,005 篇候选全文，优先顺序为 214 篇 human–AI、900 篇两轮冲突/不确定、其余 1,922 篇两轮一致人类/智能体候选；
2. 按同一全文 codebook 人工裁决直接性、研究层级、方法、理论、变量与独立样本；
3. 对最终纳入研究逐篇做参考文献回溯，并让新增记录走相同筛选流程；
4. 报告全文排除理由、质量评价和最终 concept matrix；
5. 如果要宣称比“有界权威来源”更广的覆盖，还需补充至少一个跨数据库检索和灰色文献渠道。

## 十一、可复核文件

- 完整方法交叉表：`method_reference_crosswalk.md`
- 冻结检索协议与检索式：`search_protocol_v2.md`
- 来源选择依据：`source_scope_rationale.md`
- 识别池分析：`identification_pool_analysis.md`
- 召回审计：`search_recall_audit.md`
- 题名—摘要筛选结果：`title_abstract_screening_results.md`
- 全部 5,642 条筛选审计：`screening_audit.csv`
- 214 条 human–AI 候选：`two_pass_human_ai.csv`、`two_pass_human_ai.md`
- 本地全文人工裁决：`local_fulltext_human_adjudication.md`
- 31 篇模型全文编码：`output_fulltext_local_v1/decisions.csv`
- 错误与重试审计：`error_resolution_audit.json`
