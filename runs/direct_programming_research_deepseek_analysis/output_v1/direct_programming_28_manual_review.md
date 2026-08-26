# 28 篇直接编程研究：逐篇人工复核
## 先说结论
这 28 篇并不是 28 篇同质的“个人编程研究”。按研究真正观察的对象，可以分成三类：
- **核心人类编程研究（20 篇记录）**：参与者确实执行了写代码、写 SQL、读程序、修改程序、调试、代码检查或软件开发任务。这一组最值得用于界定“个人使用编程智能体”的研究情境。
- **真实开发行为，但研究落在项目/团队层（4 篇）**：使用提交记录、缺陷、团队问卷或项目面板研究项目健康、参与方式与协调。它们与软件开发有关，但不是个人在一次编程任务中如何使用工具。
- **纯代码制品、度量或工具研究（4 篇）**：研究源代码结构、复杂度、规模或静态/动态分析工具，没有研究人的编程行为。
此外，1995 年 ISR 的 *The Relevance of Application Domain Knowledge* 与 1998 年 JMIS 的同主题论文使用了同一批 24 名 COBOL 程序员、同一对会计/水文程序。后者扩展了分析问题，但不能当成两份独立样本。因此，20 篇核心记录大约对应 **19 个独立的实证设置**。
对个人 Codex/编程智能体研究最有启发的主线不是“软件项目绩效”，而是以下五类机制：
1. **智能体作为搭档**：可直接借鉴结对编程研究，但比较基准应包括个人独立完成、人与人结对、人与智能体协作。
2. **智能体建议造成锚定**：已有 SQL 的复用会使人更快但更容易错、还会过度自信，这几乎是 AI 代码建议依赖问题的直接前身。
3. **任务表述和表示方式**：请求语言、模板、数据库结构、程序表示和可视化都会改变准确率、时间、信心与校准。
4. **理解—修改之间的认知匹配**：理解代码不自动带来更好的修改表现；理解形成的心智表示必须与修改任务所需的信息匹配。
5. **检查、验证与元认知**：个人自查常漏错，团队检查的增益有时只是汇总个人发现；程序员也会对错误答案或复用结果过度自信。这为研究“智能体输出是否经过独立验证”提供了明确依据。
## 逐篇复核
### 1. [Atrophy in Aging Systems: Evidence, Dynamics, and Antidote](../../../database_fulltext_all/28664_2024_atrophy-in-aging-systems-evidence-dynamics-and-antidote.md)（2024）
- **定位：纯代码制品/项目层；对个人智能体研究较远。**
- **做了什么：** 对 1,354 个开源 Java 系统按季度重建约 25 年的源代码历史，分析约 1.9 亿行代码、900 万条依赖和 1,900 万次提交。作者把“系统萎缩”操作化为单位代码的圈复杂度随时间增加，并考察模块化、年龄和演化结果。
- **发现：** 大量系统会随年龄出现复杂度累积；模块化能够减缓这一过程，但保护作用会随系统老化而减弱。萎缩还与更多缺陷、更困难的演化以及较弱的采用/关注相关。
- **判断：** 它正经研究软件和代码，但主体是系统生命周期而不是程序员如何完成任务。可用于说明智能体长期生成代码可能带来的可维护性后果，不能充当个人使用 Codex 的行为理论。
### 2. [Performance Outcomes of Test-Driven Development: An Experimental Investigation](../../../database_fulltext_all/13262_2020_performance-outcomes-of-test-driven-development-an-experimental-investigation.md)（2020）
- **定位：核心人类编程实验；高度相关。**
- **做了什么：** 将 84 名学生随机分到测试驱动开发（TDD）与测试后开发，要求用 Java 完成书店应用；测量代码质量、完成时间、任务满意度，并事后分析问题理解、回忆和问题解决等学习结果。
- **发现：** TDD 组代码质量更高、任务满意度更高，而且没有显著增加开发时间；TDD 改善了问题理解，但对逐字回忆和一般问题解决能力没有显著优势。
- **判断：** 这篇的核心确实是“编程方法如何改变程序产出和人的体验”，不是把编程当背景。它可直接改造为“agent-first / human-first / test-first / test-last”等实验条件。
### 3. [The Effects of Information Request Language and Template Usage on Query Formulation](../../../database_fulltext_all/08748_2016_the-effects-of-information-request-language-and-template-usage-on-query-formulation.md)（2016）
- **定位：核心 SQL 编程实验；高度相关。**
- **做了什么：** 63 名学过 SQL 的学生完成 2×2×2 重复测量实验，操纵查询复杂度、需求表述语言（伪 SQL 或经理式英语）和是否提供查询模板，完成 8 个 SQL 编写任务；测量正确率、时间、尝试次数和信心。
- **发现：** 伪 SQL 表述主要帮助低复杂度查询；模板在高复杂度任务中改善准确率、尝试次数和信心，但在低复杂度任务上可能降低表现。辅助物的效果取决于任务复杂度，不是越多越好。
- **判断：** 可直接映射到编程智能体研究中的提示表述、任务规格、脚手架和计划模板。尤其适合检验智能体在不同复杂度下是减轻还是增加认知负荷。
### 4. [Performance implications of stage-wise lead user participation in software development problem solving](../../../database_fulltext_all/09798_2014_performance-implications-of-stage-wise-lead-user-participation-in-software-development-problem-s.md)（2014）
- **定位：真实软件开发，但属于项目面板研究；与个人智能体情境较远。**
- **做了什么：** 从 SourceForge 的 29 个 C# 项目构建 429 个项目—季度观测，使用 bug 报告、邮件讨论、补丁、代码度量和下载量，区分领先用户参与问题检测、分析和移除三个阶段。
- **发现：** 分析阶段投入与更好的代码质量相关，而检测和移除投入与较差的观测质量相关；三个阶段的参与均与较低开发生产力相关。较早修复问题的“前端加载”项目缺陷更少，但生产力也更低。这些是关联结果，存在问题严重程度反向影响参与量的解释空间。
- **判断：** 编程制品指标很实在，但研究问题是外部用户如何参与项目问题解决，不是个人如何编程。若研究个人 Codex，不应把它与受控编程任务论文放在同一证据层级。
### 5. [Is Query Reuse Potentially Harmful? Anchoring and Adjustment in Adapting Existing Database Queries](../../../database_fulltext_all/09878_2010_is-query-reuse-potentially-harmful-anchoring-and-adjustment-in-adapting-existing-database-querie.md)（2010）
- **定位：核心 SQL 编程与认知实验；对生成式编程智能体尤其重要。**
- **做了什么：** 157 名学生在熟悉或不熟悉的业务领域完成 12 个 SQL 需求，其中部分任务提供可复用的已有查询；研究复用样例是否形成锚点，并测量正确率、时间、信心和校准。
- **发现：** 获得样例查询的人完成得更快，却明显更不正确（约 29% 对 49%），而且对错误答案更自信；深层结构中的错误锚点比表层错误更难充分调整。领域熟悉度会改变这种关系。
- **判断：** 这是 28 篇中与 AI 代码补全/智能体建议最接近的机制之一：建议可节省时间，却可能让用户围绕错误初稿做不足调整，并产生过度信任。研究 Codex 时应同时测正确率、时间和 confidence calibration，不能只测效率。
### 6. [Exploring the Impact of Socio-Technical Core-Periphery Structures in Open Source Software Development](../../../database_fulltext_all/06398_2010_exploring-the-impact-of-soclo-technlcal-core-periphery-structures-in-open-source-software-develo.md)（2010）
- **定位：代码提交行为与项目健康；项目层边界文献。**
- **做了什么：** 开发 TESNA 工具，对 8 个 Java 开源项目的 SVN/CVS 日志和类依赖进行分析，用 DSM 聚类得到代码核心—外围位置，再根据开发者修改哪些模块计算平均核心—外围距离（CPDM）的时间变化。
- **发现：** 作者识别出稳定、持续远离核心和振荡等模式，并以案例方式认为远离核心或反复振荡可能预示项目不健康，稳定的核心关系更常见于健康项目。
- **判断：** 它确实基于真实的代码修改行为，所以严格筛选保留有道理；但因变量是项目健康，开发者只是日志中的节点，不是被研究的个人编程过程。对个人智能体研究最多提供仓库级协作/修改位置指标。
### 7. [An Empirical Investigation of End-User Query Development: The Effects of Improved Model Expressiveness vs. Complexity](../../../database_fulltext_all/15408_2009_an-empirical-investigation-of-end-user-query-development-the-effects-of-improved-model-expressiv.md)（2009）
- **定位：核心 SQL 编程实验；高度相关。**
- **做了什么：** 两个实验共约 80 名接受 SQL 训练的商科学生，在更简洁的传统模型与语义更丰富但更大的数据模型上完成 14 个查询需求，测量语义错误、时间和信心。
- **发现：** 更具表达力的模型并没有帮助，反而产生更多语义错误、更长时间和更低信心。其原因不是语义本身不好，而是额外实体和关系带来的协调复杂度超过了表达力收益。
- **判断：** 对 Codex 很有启发：提供更多上下文、更多抽象和更“聪明”的表示不一定改善表现，关键是用户必须协调多少信息。可用于研究上下文规模、工具输出复杂度和认知负荷。
### 8. [Role of collective ownership and coding standards in coordinating expertise in software project teams](../../../database_fulltext_all/12156_2009_role-of-collective-ownership-and-coding-standards-in-coordinating-expertise-in-software-project.md)（2009）
- **定位：软件团队协调研究；不是个人编程任务。**
- **做了什么：** 对一家大型软件公司的 56 个新项目团队、509 名开发者进行三波现场研究；用问卷测集体代码所有权、编码标准和专业知识协调，用项目结束时档案中的编码错误数作为客观结果。
- **发现：** 集体所有权和编码标准均与更少编码错误相关。集体所有权降低了“必须知道专家在哪里”的重要性，而编码标准反而增强了知识定位和知识运用对质量的作用。
- **判断：** 文章的结果确实落到编码错误，但理论和分析单位是团队协调。它适合多开发者/多智能体团队治理，不适合直接回答个人如何与 Codex 协作。
### 9. [Are Two Heads Better than One for Software Development? The Productivity Paradox of Pair Programming](../../../database_fulltext_all/05946_2009_are-two-heads-better-than-one-for-software-development-the-productivity-paradox-of-pair-programm.md)（2009）
- **定位：核心结对编程实验；与人—智能体协作最直接。**
- **做了什么：** 122 名学生完成 2×2 实验，比较结对与个人编程、低与高复杂度 Java 维护任务；把结对结果分别与组成该对的最佳个人和次佳个人比较，测代码质量、满意度和信心。
- **发现：** 结对优于“次佳个人”，却没有稳定超过“最佳个人”；结对提高满意度，对信心的提升同样主要是相对于次佳个人。任务复杂度没有表现出预期的调节作用。
- **判断：** 关键不是简单问“搭档是否有效”，而是选什么反事实基准。研究 Codex 时，如果只与平均个人比较会夸大增益；最好同时比较个人基线、人的最佳独立表现和人—agent 协作表现。
### 10. [The Role of Visualization Tools in Spreadsheet Error Correction from a Cognitive Fit Perspective](../../../database_fulltext_all/16148_2008_the-role-of-visualization-tools-in-spreadsheet-error-correction-from-a-cognitive-fit-perspective.md)（2008）
- **定位：核心终端用户编程/调试实验；高度相关。**
- **做了什么：** 39 名学生使用普通 Excel 或可视化箭头工具，在 4 个电子表格中纠正链接型和非链接型公式错误，测量纠错时间和信心。
- **发现：** 可视化对追踪单元格依赖的链接错误有帮助，但对非链接错误没有普遍优势，甚至可能干扰。工具只有在其表示方式与错误类型匹配时才有效。
- **判断：** 很适合转译为“智能体解释形式 × 调试任务类型”的研究。自然语言解释、调用图、差异视图或执行轨迹不应被假定具有统一效果。
### 11. [The Role of Cognitive Fit in the Relationship Between Software Comprehension and Modification](../../../database_fulltext_all/00546_2006_the-role-of-cognitive-fit-in-the-relationship-between-software-comprehension-and-modification1.md)（2006）
- **定位：核心程序理解与修改实验；高度相关。**
- **做了什么：** 24 名有经验的 COBOL 程序员在熟悉/不熟悉领域中执行功能型或控制流型修改，分别测量修改前后理解和客观修改绩效。
- **发现：** 当理解过程中形成的心智表示与修改任务需要的信息匹配时，理解增长与修改表现正相关；不匹配时关系可能转为负向，说明理解和修改会竞争认知资源，理解得“更多”不等于理解得“对任务有用”。
- **判断：** 这是研究编程智能体与 situation awareness 的关键文献。智能体可能提高用户对程序的总体解释感，却未必建立支持当前修改的任务特定心智模型。
### 12. [The Effects of State-Based and Event-Based Data Representation on User Performance in Query Formulation Tasks](../../../database_fulltext_all/01578_2006_the-effects-of-state-based-and-event-based-data-representation-on-user-performance-in-query-form.md)（2006）
- **定位：核心查询编写实验；中高相关。**
- **做了什么：** 342 名学生使用状态型、事件型或制品型数据表示完成 7 个 SQL 查询任务，测正确率、信心、校准和时间，并考虑其 E-R 模型熟悉程度。
- **发现：** 三种表示没有稳定改变总体正确率或信心；事件表示对 E-R 舒适度较低的人改善了校准，并缩短部分任务时间。表示效果依赖用户已有知识，而非绝对优劣。
- **判断：** 对 agent 界面很有价值：同一份数据库/程序信息可以按状态、事件或制品组织，研究应测用户能力与表示方式的交互，并保留校准指标。
### 13. [Selecting optimal instantiations of data models—Theory and validation of an ex ante approach](../../../database_fulltext_all/02594_2006_selecting-optimal-instantiations-of-data-modelstheory-and-validation-of-an-ex-ante-approach.md)（2006）
- **定位：核心 SQL 编写与数据模型选择实验；中高相关。**
- **做了什么：** 59 名受过 SQL 训练的学生在第三范式关系模式和对象—关系模式上完成 10 个查询需求；作者先用 Halstead 式复杂度预测查询难度，再用语义错误、时间和信心验证。
- **发现：** 对象—关系模式的预测查询复杂度更低，也产生更少语义错误；时间优势只是趋势而未显著。参与者却可能对表现较差的 3NF 模式更有信心，再次显示主观信心与实际正确性会分离。
- **判断：** 它说明编程环境/数据结构设计会先于用户努力决定任务难度，也提醒智能体研究不能只问“感觉是否容易”。
### 14. [Developing maintainable software: The Readable approach](../../../database_fulltext_all/10622_2006_developing-maintainable-software-the-readable-approach.md)（2006）
- **定位：核心程序表示与理解实验；高度相关。**
- **做了什么：** 提出一种可执行的表格化表示，把组件、控制和数据关系更显式地呈现；参与者随机使用 Readable 或传统 Java 表示理解 N-Queens 程序，并回答 20 个理解判断题。
- **发现：** Readable 主要改善控制流理解，同时没有明显损害其他类型理解。文章真正检验的是代码表示能否针对维护所需的信息降低理解难度。
- **判断：** 可直接用于研究智能体如何展示程序：仅生成更多文字不一定有效，结构化、可执行且与维护任务匹配的表示更可能改善理解。
### 15. [An exploratory study of object-oriented software component size determinants and the application of regression tree forecasting models](../../../database_fulltext_all/20163_2004_an-exploratory-study-of-object-oriented-software-component-size-determinants-and-the-application.md)（2004）
- **定位：纯代码制品/估算研究；对个人智能体研究较远。**
- **做了什么：** 分析 152 个真实 C++ 组件，用方法数、子类数、GUI 元素和事件等属性解释源代码行数，并比较回归、CART 和 CHAID 等预测方法。
- **发现：** 多种组件特征都与规模正相关，GUI 元素是很强的规模决定因素，组件类型也会改变关系；回归树可给出分段式规模预测规则。
- **判断：** 研究的是代码组件规模和预测，不涉及程序员的认知、协作或工具使用。除非要把代码规模作为智能体任务复杂度/产出控制变量，否则关联有限。
### 16. [The effects of information request ambiguity and construct incongruence on query development](../../../database_fulltext_all/20989_2001_the-effects-of-information-request-ambiguity-and-construct-incongruence-on-query-development.md)（2001）
- **定位：核心 SQL 编写实验；高度相关。**
- **做了什么：** 23 名研究生在 Oracle SQL 中处理高/低需求歧义、高/低表示构念不一致和不同复杂度的查询请求，测错误、时间、尝试次数和信心。
- **发现：** 需求歧义降低准确性和效率；用户需求概念与数据库表示不一致同样损害准确性、效率和信心；查询复杂度进一步恶化各项结果。
- **判断：** 这里的 construct incongruence 是“需求中的概念与数据模型表达方式不一致”，不是新 IS 构念开发。对智能体研究的价值在于：agent 能否澄清含糊需求并弥合用户概念与代码/数据结构之间的表示差距。
### 17. [The Moderating Effects of Structure on Volatility and Complexity in Software Enhancement](../../../database_fulltext_all/26371_2000_the-moderating-effects-of-structure-on-volatility-and-complexity-in-software-enhancement.md)（2000）
- **定位：软件制品与维护项目层研究；不是个人编程过程。**
- **做了什么：** 收集两家组织 64 个商业 COBOL 应用三年的功能点、Halstead 操作数、调用关系、增强次数、工时、成本和错误，检验软件结构如何调节复杂度/易变性对增强后果的影响。
- **发现：** 当应用更复杂或更频繁变化时，更高结构化程度与更低增强成本和更少错误的关系更强；经验上所需的最优结构水平会随复杂度和易变性增加。
- **判断：** 编程是必要背景，指标也来自代码，但分析单位是应用系统，研究的是结构属性而非人在一次修改中的行为。可作为代码库条件或维护任务难度背景，不宜归为个人 agent 使用研究。
### 18. [Using a structured design approach to reduce risks in end user spreadsheet development](../../../database_fulltext_all/22602_2000_using-a-structured-design-approach-to-reduce-risks-in-end-user-spreadsheet-development.md)（2000）
- **定位：核心终端用户编程/设计方法实验；高度相关。**
- **做了什么：** 两次实验分别有 61 和 88 名学生，比较先用数据流图进行结构化设计与直接、临时式开发；参与者建立含 10 个工作表、数十条跨表链接的电子表格。
- **发现：** 结构化设计减少了链接错误，但没有稳定减少概念错误、遗漏错误或开发时间。不同错误类型受设计方法的影响不同，个体与配置因素也很重要。
- **判断：** 很适合研究 agent 先规划再编码是否有效。结果提示“先生成计划”可能只改善与依赖结构有关的错误，而不会自动解决需求遗漏或错误概念化。
### 19. [Applying Code Inspection to Spreadsheet Testing](../../../database_fulltext_all/25049_1999_applying-code-inspection-to-spreadsheet-testing.md)（1999）
- **定位：核心代码检查实验；高度相关。**
- **做了什么：** 60 名 MIS 学生先个人检查一个植入 8 个错误的电子表格，再组成 20 个三人组检查；个人和小组各有 45 分钟。
- **发现：** 个人平均发现约 63% 错误，小组达到约 83%；但小组没有发现任何三位成员个人发现集合之外的真正新错误，增益基本来自汇总。遗漏和长公式错误更难发现，个人还表现出过度自信。
- **判断：** 对人—agent 审查很关键：团队/智能体提高召回可能只是合并彼此发现，而不是产生新的推理能力。实验应区分“集合增益”和“协同增益”，并测信心校准。
### 20. [The Relevance of Application Domain Knowledge: Characterizing the Computer Program Comprehension Process](../../../database_fulltext_all/24954_1998_the-relevance-of-application-domain-knowledge-characterizing-the-computer-program-comprehension.md)（1998）
- **定位：核心程序理解研究；高度相关，但与第 26 篇共用样本和任务。**
- **做了什么：** 24 名有经验的 COBOL 专业人员分别理解约 400 行的熟悉会计程序和不熟悉水文程序，限时阅读、出声思考并回答理解问题；协议被编码为假设/推论、高/低层级以及应用领域/编程领域知识引用。
- **发现：** 熟悉领域总体更容易触发自上而下、假设驱动的理解，不熟悉领域更多依赖自下而上的代码推论；但程序员还分为稳定自上而下、稳定自下而上和会随领域切换的灵活组，说明个体策略不能只由领域熟悉度解释。
- **判断：** 这篇比 1995 版更细地刻画知识类型、过程轨迹、策略分组及理解成效。对 Codex 的直接问题是：智能体提供领域知识后，用户是否真的形成了可验证的代码理解，还是只更快地产生高层假设。
### 21. [Hitting the wall: errors in developing and code inspecting a simple spreadsheet model](../../../database_fulltext_all/21491_1998_hitting-the-wall-errors-in-developing-and-code-inspecting-a-simple-spreadsheet-model.md)（1998）
- **定位：核心终端用户编程与自查研究；高度相关。**
- **做了什么：** 152 名学生开发一个表面简单的电子表格“墙体任务”，随后检查和修正自己的模型；作者分析成品错误类型、单元格错误率、自查效果及经验关系。
- **发现：** 约 35% 的模型有错，尽管单元格级错误率只有约 2%；遗漏和逻辑错误主导，经验并不能消除错误，自查只能修正很小一部分问题，参与者却容易相信模型正确。
- **判断：** 这篇说明“小错误率”不等于“任务成功率高”，也是 agent 评估中应同时报告文件/任务级正确率与局部代码指标的原因。自我检查弱还支持设置独立验证条件。
### 22. [Why Is Programming (Sometimes) So Difficult? Programming as Scientific Discovery in Multiple Problem Spaces](../../../database_fulltext_all/26760_1997_why-is-programming-sometimes-so-difficult-programming-as-scientific-discovery-in-multiple-proble.md)（1997）
- **定位：核心编程认知研究；理论相关性极高。**
- **做了什么：** 用三个受控实验让计算机专业学生从零编写 C++ 程序、理解现有程序以及复用程序解决新的同构问题；收集言语协议和程序产出，把行为编码为规则生成、心智模拟、表示构建与表示映射。
- **发现：** 编程困难不只来自写规则或测试实例，更来自必须发现或改变问题表示。初始表示不合适会造成僵局；成功复用者往往构造中间表示并完成多步映射，失败者则被旧表示束缚。
- **判断：** 这是理解编程智能体为何有时帮忙、有时使人更依赖错误框架的重要理论：agent 不只是给代码，还可能固定、改变或帮助搜索问题表示。非常适合与 situation awareness、problem framing 和认知卸载结合。
### 23. [An experimental investigation into the process of knowledge-based systems development](../../../database_fulltext_all/23206_1996_an-experimental-investigation-into-the-process-of-knowledge-based-systems-development.md)（1996）
- **定位：真实、较长周期的编程实验；中等相关。**
- **做了什么：** 24 名研究生在 7 周内用 CLIPS 独立开发 MBA 课程规划知识系统，2×2×2 操纵规则式/混合式知识表示、快速/结构化原型方法及程序员经验；记录设计和编码时间、LOC、版本间代码变更、异常、功能性和可用性。
- **发现：** 快速原型与规则表示组合的功能性最好，但快速原型与混合表示组合最差；结构化混合方案更稳健。经验更高的程序员编码生产率和可用性更好，说明方法与表示之间存在组合效应。
- **判断：** 文章确实把实际开发过程和制品作为核心，不是泛泛的系统采纳研究。它对现代 agent 的外部效度受 CLIPS、样本和七周课程情境限制，但“开发方法 × 知识表示 × 经验”的实验结构仍有用。
### 24. [The Influence of Database Structure Representation on Database System Learning and Use](../../../database_fulltext_all/24810_1996_the-influence-of-database-structure-representation-on-database-system-learning-and-use.md)（1996）
- **定位：核心 SQL 学习和编写实验；高度相关。**
- **做了什么：** 52 名商科研究生随机使用四种数据库结构表示，操纵实体/表格语义、图形/文本符号、关系显式/隐式；先学习数据库结构，再学习八类 SQL 查询并实际编写和判断查询。
- **发现：** 看起来更有助于理解现实实体的表示，未必更利于学习 SQL；表格语义和通过外键隐式表达关系反而更适合查询语言学习。贴近目标语言的表示可能比概念上更丰富的表示更有效。
- **判断：** 对 agent 的启示是区分“帮助理解业务世界”与“帮助生成正确代码”。自然语言或图形解释让用户觉得更懂领域，不必然改善其代码层操作。
### 25. [A software complexity model of object-oriented systems](../../../database_fulltext_all/17415_1995_a-software-complexity-model-of-object-oriented-systems.md)（1995）
- **定位：概念性代码度量模型；不是人类编程任务。**
- **做了什么：** 在变量、方法、对象和系统四层提出面向对象复杂度度量，涵盖耦合、凝聚、继承、多态、消息传递、扇入扇出等；另让 7 名学过面向对象课程的研究生列举复杂性来源，为模型分类提供感知支持。
- **发现：** 主要贡献是提出可从源代码静态表示计算的复杂度体系，而不是检验一种编程方法是否改善人的表现。小规模感知研究不能把它变成人类编程实验。
- **判断：** 可用于定义代码复杂度控制变量或 agent 任务难度，但不回答个人怎样使用智能体。
### 26. [Research Report—The Relevance of Application Domain Knowledge: The Case of Computer Program Comprehension](../../../database_fulltext_all/26710_1995_research-reportthe-relevance-of-application-domain-knowledge-the-case-of-computer-program-compre.md)（1995）
- **定位：核心程序理解研究；与第 20 篇共用同一实验材料和 24 名参与者。**
- **做了什么：** 让专业 COBOL 程序员分别理解熟悉的会计程序和不熟悉的水文程序并出声思考，将协议中的假设视为自上而下过程、推论视为自下而上过程，以两者差值构成过程分数。
- **发现：** 熟悉应用领域时，程序员相对更多使用自上而下、假设驱动的过程；不熟悉时更依赖从代码细节向上推断。它解决的是此前两种程序理解理论为何看似冲突。
- **判断：** 这是 1995 年 ISR 的较集中报告；1998 年 JMIS 文章基于相同材料扩展到知识引用层级、策略分组和理解效果。文献综述可同时引用，但做证据计数或元分析时必须视为依赖样本。
### 27. [On end-user computing productivity](../../../database_fulltext_all/18768_1991_on-end-user-computing-productivity.md)（1991）
- **定位：包含核心终端用户编程实验；中高相关。**
- **做了什么：** 文章含两个实验；与编程直接相关的是 83 名学生经培训后，用 BASIC 完成包含顺序、选择和循环的程序，比较流程图、伪代码、叙述式描述和直接编写四种开发方法，评价结构、正确性、总体质量、时间及质量/时间生产力。
- **发现：** 程序总体质量不高，四种方法在结构和正确性上没有显著差异；直接编写耗时最短，伪代码和直接编写在生产力指标上较好。对简单任务，正式前置表示的成本未必能由质量收益抵消。
- **判断：** 可作为“先让 agent 规划还是直接让 agent 编码”的早期类比，但其简单 BASIC 任务意味着不能外推为复杂任务下计划无用。
### 28. [COD — A dynamic data flow analysis system for Cobol](../../../database_fulltext_all/18351_1987_cod-a-dynamic-data-flow-analysis-system-for-cobol.md)（1987）
- **定位：编程工具设计与实现；没有用户实验。**
- **做了什么：** 构建 COBOL 动态数据流分析系统 COD，通过程序插桩监测变量的定义、引用、未定义、输入输出和文件开闭等动作，以状态转换图检测数据流异常，并处理 COBOL 的组项、表、REDEFINES、PERFORM、CALL 等语言特性。
- **发现：** 文章主要给出检测理论、系统架构、插桩实现和使用经验，认为该工具能够发现数据流异常及部分错误，越早用于开发越可能降低修复成本；没有人与工具对照实验支持行为效果。
- **判断：** 它属于“用于编程的技术”而非“人如何编程”的研究。可当静态/动态分析智能体的技术先例，但不能据此推断 agent 会改善人的正确性、理解或 situation awareness。
## 对 28 篇的最终取舍建议
如果下一步是为“个人使用 Codex 等编程智能体”建立紧凑的理论和实验设计库，建议优先保留以下 14 篇作为第一层：TDD、请求语言与模板、查询复用锚定、模型表达力与复杂度、结对编程、电子表格可视化、认知匹配下的理解—修改、状态/事件表示、数据模型实例化、Readable、需求歧义与表示不一致、结构化电子表格设计、电子表格代码检查、编程作为多问题空间发现。
第二层可保留 6 篇，用于扩充错误、自查、领域知识、学习和较长开发过程：Hitting the Wall、1995/1998 两篇领域知识论文（按一个样本处理）、知识系统开发、数据库结构表示、终端用户计算生产力。
其余 8 篇——系统萎缩、领先用户参与、开源核心—外围、集体所有权与编码标准、组件规模、软件增强结构、面向对象复杂度模型、COD——可以留在“软件/代码情境背景库”，但不应与个人编程智能体研究并列计算为直接的人类编程证据。
