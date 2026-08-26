# 本地全文子集人工裁决

## 裁决范围

本地库只能解析到 31 篇候选全文。其中 20 篇是上一轮已经逐篇人工确认的“直接编程核心种子”，本轮继续保留；另外 11 篇是通过 DOI 在本地全文库中补配到的记录，需要重新执行“不可替换测试”：

- 如果把程序员替换成一般知识工作者、把代码或可执行逻辑替换成一般工作产出后，研究问题、关键处理、主要测量或结论仍基本成立，则不进入直接编程核心语料。
- 研究可以是个人、配对、团队、制品或智能体层级，也可以是经验、设计、分析建模或综述研究；但编程动作或程序制品必须是不可替换的研究对象，而不能只是组织、项目或团队理论的背景。
- 本表是人工裁决层，不覆盖 DeepSeek 原始输出。原始模型判断保存在 `output_fulltext_local_v1/decisions.csv`。

## 11 篇 DOI 补配全文的逐篇裁决

| 文献 | 人工裁决 | 在最终综合中的角色 | 依据 |
|---|---|---|---|
| How Pair Programming Influences Team Performance: The Role of Backup Behavior, Shared Mental Models, and Task Novelty (2019, ISR) | 不进入直接编程核心 | 编程团队情境背景 | 原文明说研究“shifting attention to the team-level effects”，主要数据是 62 个团队的多来源问卷；核心机制是 shared mental models、backup behavior、task novelty 与 team performance，而不是一次实际编程任务、代码过程或代码结果。 |
| Revising the Panko–Halverson Taxonomy of Spreadsheet Errors (2010, DSS) | 纳入 | 直接概念/分类与评价研究 | 分类对象是电子表格公式与建模/测试阶段中的程序错误；若替换成一般文档错误，分类法及其可靠性检验不再成立。 |
| A Comparison of Pair Versus Solo Programming Under Different Objectives: An Analytical Approach (2008, ISR) | 纳入 | 直接分析建模研究 | 数学模型直接比较结对与单人编程的模块—开发者分配、模块开发与系统集成成本，并从编程实验文献参数化；虽无参与者实验，但编程方法是模型不可替换的核心。 |
| A Critical Review of the Literature on Spreadsheet Errors (2008, DSS) | 纳入 | 直接二次综述 | 全文系统讨论电子表格公式开发、错误、测试、审计和修复；对象是可执行公式逻辑，不是一般电子表格使用。 |
| An Auditing Protocol for Spreadsheet Models (2008, Information & Management) | 纳入 | 直接设计与评价研究 | 对 50 个运营电子表格实施人工加审计软件的协议，核心证据是公式和模型错误的发现方式、类型及时间。 |
| The Role of Spreadsheet Knowledge in User-Developed Application Success (2005, DSS) | 纳入 | 直接人类经验研究 | 参与者实际开发和修正 Excel 应用，独立专家评估系统质量；电子表格公式和应用开发是处理与测量不可缺少的部分。 |
| Applications Development by End-Users: Can Quality Be Improved? (2000, DSS) | 纳入 | 直接人类实验 | 参与者实际创建电子表格应用，研究开发方法如何影响应用质量；不是仅调查一般使用态度。 |
| User-Developed Applications: An Empirical Study of Application Quality and Developer Productivity (1996, JMIS) | 纳入 | 直接人类实验 | 终端用户与代理专业人员成对开发完整 dBASE 应用，以缺陷、质量、功能点和代码行测量结果；编程制品和开发任务不可替换。 |
| Computer-Aided Model Construction (1993, DSS) | 排除 | 不相关 | “model construction”指决策/运筹模型构建，不是程序编写、生成、理解、检查、调试、修改或测试。 |
| Developing End-Users’ Systems Development Competence (1993, Information & Management) | 纳入 | 直接开发方法/行动研究 | 两个行动研究案例中，终端用户团队实际经历应用设计、生成、测试、批评与修改循环，并形成投入日常使用的应用；保留为团队层面的开发方法研究，不与个人任务实验混合。 |
| An Empirical Study of Users as Application Developers (1985, Information & Management) | 纳入 | 直接描述性研究 | 样本明确排除不开发应用的普通用户，研究对象是 272 名自行开发应用的非 DP 专业人员、其应用、开发时间、工具和支持条件；保留为编程实践描述证据，但不当作任务层面的因果实验。 |

## 裁决后数量

- 直接编程研究：29 篇（20 篇既有核心种子 + 9 篇 DOI 补配记录）。
- 编程团队情境背景：1 篇。
- 非编程含义：1 篇。

这 29 篇只是当前本地可获得全文的已裁决子集，不能替代对其余 3,005 篇候选全文的获取与复核，也不能作为整项系统综述的最终纳入数量。
