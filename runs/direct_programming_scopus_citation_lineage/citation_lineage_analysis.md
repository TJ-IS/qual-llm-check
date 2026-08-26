# 20 篇核心编程研究的 Scopus 施引文献脉络分析
## 核心结论
这 807 条记录并不主要来自 AIS eLibrary，也没有集中在某一个其他期刊类别。它们形成的是一个横跨信息系统、软件工程、计算机科学、HCI、计算教育、会计信息系统等领域的分散网络：
- Scopus 中 807 条记录的 EID 全部唯一，但其中包含 12 篇种子论文自身；剔除后是 795 条外部施引记录。
- 以 `Association for Information Systems` 为出版者的严格 AIS 记录只有 86 条（10.7%）。
- 把早期元数据中出版者缺失、但来源明确属于 ICIS、AMCIS、ECIS、PACIS、ACIS 的记录一并纳入，扩展 AIS 口径为 121 条（15.0%）。
- AIS Basket 11 期刊中有 137 条（17.0%）。扩展 AIS 与 Basket 11 重叠 27 条（均为 JAIS），两者取并集为 231 条（28.6%）；剩余 576 条（71.4%）在这两个体系之外。
- 807 条记录分散在 418 个来源名称中。第一大来源 JAIS 也只有 27 条（3.3%）；前 10 个来源合计 170 条（21.1%），前 20 个来源合计 259 条（32.1%），不存在单一期刊或单一出版体系占主导的情况。
因此，最准确的概括是：这是一条从 IS 中的认知匹配、程序理解、查询编写、电子表格与结对编程研究出发，向软件工程和计算机科学扩散的引用脉络，而不是 AIS eLibrary 内部的封闭脉络。
## 数据口径与去重
| 指标 | 结果 |
|---|---:|
| Scopus 导出记录 | 807 |
| 唯一 EID | 807 |
| 导出中再次出现的种子论文 | 12 |
| 外部施引记录 | 795 |
| 唯一 DOI | 656 |
| DOI 缺失 | 151 |
| 规范化后唯一标题 | 788 |
| 同题记录组 | 18 |
| 同题额外记录 | 19 |
同题记录主要是会议版与期刊扩展版、文章与书章再版，或 Scopus 对同一会议论文建立了两个记录。例如 *Analysis of Designer Emotions in Collaborative and Traditional Computer-Aided Design* 同时有 2019 年会议版与 2021 年期刊版。因而 807 是可靠的“唯一 Scopus 记录数”，但若把同题版本视为同一项研究，约为 788 个题名层面的研究对象。
组合 `REFEID` 检索还会返回“引用了其他种子的种子论文”。本次导出中有 12/20 篇种子满足这种关系，所以对外部扩散规模应使用 795，而不是 807。
## 来源体系：AIS、Basket 11 与其他领域
### AIS eLibrary/AIS 品牌来源
| 口径 | 数量 | 占 807 比例 |
|---|---:|---:|
| 出版者严格等于 Association for Information Systems | 86 | 10.7% |
| 加入明确的 ICIS/AMCIS/ECIS/PACIS/ACIS 老记录 | 121 | 15.0% |
| 其中会议论文 | 85 | 10.5% |
| 其中期刊文章 | 35 | 4.3% |
| 其中社论 | 1 | 0.1% |
扩展 AIS 的 36 条期刊/社论记录主要是 JAIS 27 条、CAIS 8 条、AIS Transactions on Human-Computer Interaction 1 条；其余 85 条主要是 AIS 各地区会议论文。因此，即使按宽口径，AIS 内容也只占约六分之一，而且以会议论文为主。
### AIS Basket 11
| 期刊 | 数量 |
|---|---:|
| Journal of the Association for Information Systems | 27 |
| Decision Support Systems | 24 |
| MIS Quarterly | 20 |
| Journal of Management Information Systems | 16 |
| Information Systems Research | 14 |
| Information & Management | 12 |
| European Journal of Information Systems | 12 |
| Information Systems Journal | 7 |
| Journal of Strategic Information Systems | 2 |
| Information and Organization | 2 |
| Journal of Information Technology | 1 |
| 合计 | 137 |
Basket 11 占 17.0%，说明这些种子的确有坚实的 IS 期刊延续，但仍不是全部施引文献的主体。扩展 AIS 与 Basket 11 合并、去除共同的 27 篇 JAIS 后为 231 条；换句话说，71.4% 的记录既不是明确的 AIS 来源，也不在 Basket 11 中。
### 其余来源在哪里
排除扩展 AIS 和 Basket 11 后还有 576 条，分布在 351 个来源中。数量较多的来源包括：
| 来源 | 数量 | 主要归属 |
|---|---:|---|
| HICSS Proceedings | 18 | 跨学科信息系统会议，主要由 IEEE 收录 |
| Information and Software Technology | 16 | 软件工程 |
| Lecture Notes in Business Information Processing | 11 | 商务信息处理/会议论文集 |
| Journal of Database Management | 11 | 数据库与 IS |
| Lecture Notes in Computer Science | 10 | 计算机科学会议论文集 |
| Journal of Systems and Software | 10 | 软件工程 |
| ICSE Proceedings | 9 | 软件工程 |
| Journal of Information Systems | 9 | 会计信息系统 |
| Empirical Software Engineering | 9 | 实证软件工程 |
| IEEE Transactions on Software Engineering | 9 | 软件工程 |
Scopus 的可重叠学科分类也支持这一判断：Computer Science 630 条（78.1%）、Business, Management and Accounting 252 条（31.2%）、Decision Sciences 192 条（23.8%）、Social Sciences 179 条（22.2%）、Engineering 104 条（12.9%）。这些类别会重叠，不能相加，但“计算机科学为最大覆盖面、IS/管理为重要次级覆盖面”的结构非常清楚。
## 出版形式
| 文献类型 | 数量 | 比例 |
|---|---:|---:|
| Article | 451 | 55.9% |
| Conference paper | 277 | 34.3% |
| Book chapter | 47 | 5.8% |
| Review | 18 | 2.2% |
| Book | 10 | 1.2% |
| Editorial | 4 | 0.5% |
约三分之一是会议论文，这与编程、软件工程、HCI 和计算机科学重视会议发表的传统一致，也解释了为什么不能只用 AIS 期刊或 Basket 11 来理解这条脉络。
## 年代：种子很老，但施引活动没有停止
20 篇种子的中位年份为 2003.5；18/20 发表于 2010 年及以前，14/20 发表于 2006 年及以前。因此“看起来普遍很老”首先是种子选择本身造成的。
| 年代 | 807 条原始记录 | 剔除种子后的外部施引记录 |
|---|---:|---:|
| 2021 年及以后 | 176 | 176 |
| 2016–2020 | 199 | 197 |
| 2006–2015 | 365 | 359 |
| 2005 年及以前 | 67 | 63 |
2016 年以来仍有 375/807 条（46.5%），2021 年以来有 176/807 条（21.8%）。所以这条脉络不是已经死亡，而是高峰集中在 2006–2015 年，之后持续扩散。2026 年数据仅截至 7 月 24 日，不能与完整年份直接比较。
## 哪些种子真正支撑了这条脉络
下表是种子 CSV 中的 Scopus `Cited by` 本地快照。它们相加为 932，但存在同一论文同时引用多篇种子的重叠，因此不能与 807 一一对应。
| 排名 | 种子论文 | 年份 | Cited by |
|---:|---|---:|---:|
| 1 | The Role of Cognitive Fit in the Relationship Between Software Comprehension and Modification | 2006 | 206 |
| 2 | Are Two Heads Better than One for Software Development? The Productivity Paradox of Pair Programming | 2009 | 154 |
| 3 | The Relevance of Application Domain Knowledge: The Case of Computer Program Comprehension | 1995 | 86 |
| 4 | Hitting the Wall: Errors in Developing and Code Inspecting a Simple Spreadsheet Model | 1998 | 60 |
| 5 | Applying Code Inspection to Spreadsheet Testing | 1999 | 55 |
| 6 | Is Query Reuse Potentially Harmful? | 2010 | 52 |
| 7 | State-Based and Event-Based Data Representation in Query Formulation | 2006 | 45 |
| 8 | Information Request Ambiguity and Construct Incongruence in Query Development | 2001 | 44 |
| 9 | Application Domain Knowledge and the Program Comprehension Process | 1998 | 39 |
| 10 | Why Is Programming (Sometimes) So Difficult? | 1997 | 39 |
前两篇占 932 次未去重种子引用的 38.6%，前五篇占 60.2%，前十篇占 83.7%。因此，807 篇并不是由 20 篇种子均匀产生的；真正的中心节点是“认知匹配—程序理解”和“结对编程”，随后才是领域知识、电子表格错误与查询编写。
## 主题脉络
以下是对题名、摘要、作者关键词和索引关键词进行可复现关键词匹配后的重叠计数，不是互斥分类，也不能把各行相加。
| 主题 | 全部命中 | 2021+ | 2016–2020 | 2006–2015 | ≤2005 |
|---|---:|---:|---:|---:|---:|
| 一般软件工程/软件开发 | 307 | 71 | 76 | 124 | 36 |
| 程序理解、认知与认知匹配 | 213 | 54 | 45 | 101 | 13 |
| 结对编程、敏捷、测试与质量 | 145 | 34 | 51 | 56 | 4 |
| 查询、数据库与概念建模 | 142 | 18 | 30 | 80 | 14 |
| 电子表格与终端用户编程 | 116 | 6 | 16 | 71 | 23 |
### 程序理解与认知匹配
这是最稳定、最容易迁移到今天的个人层面脉络。早期问题是领域知识、信息表示方式和认知匹配如何影响程序理解与修改；后续发展到代码阅读策略、眼动、心智模型、代码理解实验设计与开发者注意。2021 年以来仍有 54 条命中，是五个细分主题中延续最明显的一支。
### 结对编程、敏捷与测试
这条线的引用量很大，但发生了明显分叉。一支仍研究个人或二人编程行为，例如结对沟通、远程结对、TDD 与代码质量；另一支转向团队、项目、心理安全、工作满意度、离职倾向和组织敏捷。后者虽然引用了编程种子，却已经不再直接研究“人如何编程”。这也是 807 条不能整体视为编程情境文献的主要原因之一。
### 查询、数据库与概念建模
早期集中于 SQL/查询编写、信息请求语言、表示方式、模型复杂度和查询复用；后来扩展到概念建模、语义距离、ontology、数据探索与 SQL 教学。最新延续中已经出现 text-to-SQL/SPARQL/Cypher 与语言模型，但总体上与现代通用编程智能体的连接仍然有限。
### 电子表格与终端用户编程
这是一条成熟但明显收缩的分支：2006–2015 有 71 条命中，2021 年以来只有 6 条。当前主要表现为电子表格质量保证综述、错误检测、调试工具、产品度量和教学，不再是高速增长的研究前沿。
### 引用扩散而非直接继承
施引池中被引量最高的论文包括知识管理、Big Data 研究议程、设计科学理论发展、在线决策支持等。它们可能只是借用了认知匹配、领域知识或表示方式理论，并不研究编程。因此，“引用了 20 篇核心种子”只能证明文献关系，不能证明研究情境仍然是编程。
## 与现代 LLM/编程智能体的直接连接
本地题名、摘要和关键词规则在 2020 年以后命中 6 条 AI+编程候选。逐条阅读摘要后，4 条是直接研究编程或代码理解，1 条是相邻的软件需求工程，1 条是关键词造成的误命中。
### 直接相关的 4 篇
1. **Ivie: Lightweight Anchored Explanations of Just-Generated Code**（CHI 2024，Scopus cited by 43）。研究“生成代码后，程序员如何检查和理解代码”。Ivie 是 VS Code 分支，利用 LLM 把简短解释锚定在刚生成的代码旁；实验室研究显示它相较基线改善了生成代码理解，并被认为有用且干扰较低。这是旧程序理解研究与现代编程助手最直接的桥梁。
2. **Follow-Up Attention: An Empirical Study of Developer and Neural Model Code Exploration**（IEEE TSE 2024，cited by 2）。让 25 名开发者完成代码 sensemaking，形成 92 个带人工标注的眼动会话，并比较 CodeGen、InCoder、GPT-J 的注意信号与人的代码探索。提出的 follow-up attention 对下一行注视的预测准确率为 47%，高于 42.3% 的人类历史基线。这是“人的程序理解过程”与“模型如何处理代码”的直接连接。
3. **DevTales: A Tool for Providing Narrative Code Histories into Developer Workflows**（VL/HCC 2025，cited by 0）。在 VS Code 中整合细粒度子目标、网页查找活动、开发者笔记与 LLM 生成的代码历史叙事，通过三个混合方法用户研究考察调试、理解设计理由和代码复用。它延续的是程序理解、领域知识和开发过程外部记忆这条线。
4. **Evaluating Logical Structure in Computer Programs Using LLMs**（FLAIRS 2026，cited by 0）。比较 LLM 与人类专家对程序逻辑步骤及其代码块的标注，最高文本相似度为 64.4%。它直接把经典程序理解理论中的“识别程序逻辑步骤”改造成 LLM—人类对照任务。
### 相邻或不相关
- **Quest-RE**（2024）使用 GPT-4 生成问题以补全需求规格，属于需求工程，不是对编程活动本身的研究。
- **Determinants of Continuance Intention to Use Chatbots in Retail Settings**（2025）研究零售聊天机器人持续使用；摘要中的 “chatbot developers” 触发了宽松规则，实际与编程无关。
另有 **User Cognitive Fit in Human-AI Interaction**（Computers in Human Behavior，2026）使用六万余段人机对话，把认知匹配扩展为输入表示与生成输出复杂度之间的动态关系。它说明旧 IS 理论已经迁移到一般人机 AI 互动，但没有进入编程情境，因而不是编程智能体研究。
## 对“为什么普遍很老”的解释
你的直觉基本正确，但应拆成两层：
1. 种子层确实很老：18/20 在 2010 年及以前，核心理论节点来自 1990 年代到 2000 年代中期。
2. 后续引用并不老：近十年仍占约 46.5%，只是大量后续研究已经迁移到团队敏捷、一般认知匹配、概念建模、教育或软件质量，不再直接研究个人编程。
现代 coding agent/LLM 编程研究主要发表在 CHI、TSE、VL/HCC、ICSE 等 HCI/软件工程/计算机科学渠道，并不天然沿用 MISQ/ISR 的老编程文献。只从这 20 篇旧种子向前追引，会发现少量真正的现代桥梁，但会漏掉大量没有引用这些种子的当代编程智能体研究。
## 建议如何继续构建真正的现代编程研究脉络
如果目标是个人使用 Codex 一类编程智能体，最有效的下一步不是把 807 条全部视为候选，而是：
1. 以 Ivie、Follow-Up Attention、DevTales、Evaluating Logical Structure 四篇为第二代种子，继续查它们的施引文献。
2. 独立检索 coding agent、AI pair programmer、AI-assisted programming、generated-code comprehension、code verification、code sensemaking 等现代术语，避免“必须引用旧 IS 种子”造成的系统性漏检。
3. 只把直接观察编写、理解、调试、检查、修改或委托生成代码的研究纳入核心集；把团队敏捷、一般软件项目管理、需求工程和一般人机 AI 互动单列为邻近脉络。
## 限制
- 当前 Scopus CSV 没有导出逐篇参考文献列表，所以只能确认每条记录至少引用了 20 篇种子中的一篇，不能从该文件恢复“哪条记录具体引用了哪一篇种子”的边矩阵。若要精确网络，需要导出 References 字段，或分别运行 20 个单种子 `REFEID` 检索。
- 主题计数来自元数据关键词规则，用来描述总体结构；涉及现代 AI 的 6 条候选已经逐篇阅读摘要复核。
- Scopus 学科分类允许一篇文献同时属于多个领域，因此学科数量不能相加为 807。
