# 本地可得全文子集：最终纳入与概念矩阵

本报告只覆盖能够在本地 13,910 篇全文库中按记录文件名或 DOI 解析出的论文。它不能代表其余缺失全文候选的最终结论。

## 流量

- 本地候选全文：31
- 全文最终纳入：30
- 全文排除：1

## 纳入构成

| 主体 | 数量 |
| --- | --- |
| human_only | 29 |
| human_ai | 1 |

| 程序制品 | 数量 |
| --- | --- |
| source_code | 14 |
| spreadsheet_logic | 9 |
| database_query | 6 |
| low_code_or_visual | 1 |

| 证据角色 | 数量 |
| --- | --- |
| primary_empirical | 27 |
| design_and_evaluation | 2 |
| secondary_review | 1 |

| 编程行动 | 数量 |
| --- | --- |
| write | 22 |
| debug_or_repair | 12 |
| test | 11 |
| inspect_or_review | 11 |
| understand | 10 |
| modify_or_refactor | 10 |
| generate | 4 |
| complete | 1 |

## 全文纳入论文

### 1. [Performance Outcomes of Test-Driven Development: An Experimental Investigation](fulltext_candidates_local/13262_2020_performance-outcomes-of-test-driven-development-an-experimental-investigation.md)
- 年份：2020；来源：Journal of the Association for Information Systems；DOI：10.17705/1jais.00628
- 证据角色：primary_empirical；主体：human_only；制品：source_code；行动：write；test；modify_or_refactor
- 编程情境定义：本文中的编程指根据需求规格说明，使用Java语言开发完整的面向对象应用程序，包括编写类、方法、测试用例，并通过控制台输出结果；任务要求实现具体的功能逻辑和输出，被明确视为编程任务。
- 任务与场景：受控实验室实验，参与者完成两个编程任务（热身任务和主任务），主任务为开发一个书店库存管理应用程序。两组分别使用传统的测试后开发方法和测试驱动开发（TDD）方法，在Eclipse IDE中编写Java代码。
- 方法与分析层级：随机化对照实验；individual
- 样本/数据：88名信息系统或计算机科学专业的本科及研究生参与，最终84人纳入分析，随机分为TDD组和测试后组各42人。平均年龄26.06岁，大部分具有小于2年的编程经验。
- 理论/框架：Goal Theory；Self-Determination Theory；Kolb's Experiential Learning Theory
- 自变量：开发方法（TDD vs. 测试后）
- 中介：无/未明示
- 调节：无/未明示
- 因变量：软件质量；任务满意度
- 主要发现：TDD组相比测试后组，软件质量显著更高，任务满意度也显著更高。同时TDD并未导致生产率下降。附加分析显示TDD组在理解水平上更高，但逐字回忆和问题解决能力无显著差异。
- 人—智能体关系：纯人类手动编程，比较两种软件开发方法，不涉及任何智能体或自动化工具（除IDE和JUnit框架外，工具本身不自主生成或修改代码）。
- 样本独立性：未提及复用其他研究样本，为独立样本。
- 质量/限制：使用学生样本且编程经验有限，可能影响外部效度；学习成果仅通过问卷即时测量，未采用纵向设计；任务为单一小型应用，可能限制生态效度。

### 2. [How Pair Programming Influences Team Performance: The Role of Backup Behavior, Shared Mental Models, and Task Novelty](fulltext_candidates_local/03656_2019_how-pair-programming-influences-team-performance-the-role-of-backup-behavior-shared-mental-model.md)
- 年份：2019；来源：Information Systems Research；DOI：10.1287/isre.2019.0856
- 证据角色：primary_empirical；主体：human_only；制品：source_code；行动：write；generate；complete；understand；inspect_or_review；debug_or_repair；modify_or_refactor；test
- 编程情境定义：在本文中，编程活动指两名软件开发人员结对使用一台电脑，共同进行软件代码的设计、编写、测试等任务。任务不涉及生成式AI或自主智能体，而是人类间的协作编程。
- 任务与场景：数据来自一家大型企业软件公司的62个Scrum团队，团队从事企业软件的开发、运营和维护，使用结对编程的程度不一。团队绩效由产品负责人评价。
- 方法与分析层级：定量实证研究，通过多来源问卷调查收集数据，采用OLS回归和自助法中介检验分析假设。；team
- 样本/数据：62个软件开发团队，377名软件开发人员，62名Scrum主管，34名产品负责人。数据收集于一家全球大型企业软件公司。
- 理论/框架：Team Adaptation Theory；Shared Mental Models；Backup Behavior
- 自变量：Pair Programming (PAIR)；Shared Mental Models (SHARED)；Backup Behavior (BACKUP)；Task Novelty (NOVELTY)；Interaction: BACKUP × NOVELTY
- 中介：Shared Mental Models
- 调节：Backup Behavior；Task Novelty
- 因变量：Team Performance (PERFORMANCE)
- 主要发现：结对编程通过增强共享心智模型促进团队备份行为；备份行为减弱了任务新颖性对团队绩效的负面影响，即在任务新颖性高时，拥有高备份行为的团队绩效更好。
- 人—智能体关系：本文研究人类开发者之间的结对编程实践，不涉及AI或智能体，故无人机关系。
- 样本独立性：未提及与其他研究共享样本，视为独立样本。
- 质量/限制：横截面数据，因果关系推断受限；单一组织背景，外部效度有限；自报告数据可能受共同方法偏差影响，但采用了多来源数据和控制手段。

### 3. [The Effects of Information Request Language and Template Usage on Query Formulation](fulltext_candidates_local/08748_2016_the-effects-of-information-request-language-and-template-usage-on-query-formulation.md)
- 年份：2016；来源：Journal of the Association for Information Systems；DOI：10.17705/1jais.00440
- 证据角色：primary_empirical；主体：human_only；制品：database_query；行动：write；test；debug_or_repair
- 编程情境定义：本研究中的编程定义为：参与者根据信息请求，使用SQL语言编写SELECT查询从关系数据库中检索数据。任务仅限于查询编写，不包括其他编程活动。
- 任务与场景：实验室实验，参与者依次完成八项SQL查询编写任务，每个任务有不同复杂度、请求语言和模板使用条件。
- 方法与分析层级：2×2×2重复测量因子实验设计，使用重复测量多元方差分析。；individual
- 样本/数据：63名计算机信息系统和计算机科学专业的三级学生（22名女性，65名男性，平均年龄18-25岁）。来自美国一所公立大学的两门数据库管理课程。
- 理论/框架：Cognitive Load Theory
- 自变量：request language (pseudo-SQL vs. manager English)；template usage (template vs. no template)；query complexity (low vs. high)
- 中介：无/未明示
- 调节：无/未明示
- 因变量：query accuracy；query writing time；number of query attempts；confidence
- 主要发现：请求语言和模板使用在不同情境下影响查询编写性能。伪SQL请求对低复杂度查询的准确性有显著正面影响，对高复杂度查询无影响。模板使用提高了高复杂度查询的性能，但对低复杂度查询有负面影响。查询复杂度显著负向影响所有性能指标。
- 人—智能体关系：人类参与者独立编写查询，没有自主智能体。工具（模板、请求语言）作为认知辅助，不涉及生成式或交互式智能体。
- 样本独立性：未提及与其他研究共用样本，但样本来自同一课程的两个部分，可能存在课程内关联。
- 质量/限制：局限性：使用学生样本，外部效度有限；样本量较小且部分参与者未完成所有任务导致删失；任务时间限制可能影响表现；伪SQL请求长度可能混淆其清晰度效果；未直接测量认知负荷类型。

### 4. [Is Query Reuse Potentially Harmful? Anchoring and Adjustment in Adapting Existing Database Queries](fulltext_candidates_local/09878_2010_is-query-reuse-potentially-harmful-anchoring-and-adjustment-in-adapting-existing-database-querie.md)
- 年份：2010；来源：Information Systems Research；DOI：10.1287/isre.1080.0189
- 证据角色：primary_empirical；主体：human_only；制品：database_query；行动：write；modify_or_refactor
- 编程情境定义：本文中的编程指使用SQL编写数据库查询以满足信息请求的活动，包括从零开始编写新查询和修改现有查询（查询重用）。任务不涉及数据库设计或架构变更。
- 任务与场景：实验任务：157名大学生在两个领域（熟悉和不熟悉的数据库模式）中分别为四个信息请求编写SQL查询。在每个领域中，两个请求提供样例查询可供修改重用，两个请求无样例。通过在线工具编写、执行并提交查询，并报告自信程度。
- 方法与分析层级：受控实验（被试内设计），随机分配样例查询条件，使用重复测量方差分析检验锚定与调整效应对查询正确性、时间、自信度等的影响。；individual
- 样本/数据：157名来自六所美国大学数据库管理课程的学生（查询新手），因课程学分参与。数据包括查询正确性（正确/错误）、花费时间（分钟）、自信度（五级李克特）、调整偏差正确调整百分比等。
- 理论/框架：Anchoring and Adjustment Heuristic；Effort-Accuracy Tradeoff
- 自变量：机会重用查询（有/无样例查询）；领域熟悉度（熟悉/不熟悉）；锚类型（表面结构/深层结构）
- 中介：无/未明示
- 调节：无/未明示
- 因变量：查询正确性；查询编写时间；自信度；自信与正确性关系（Mean Probability Score）；调整偏差（正确调整锚的百分比）；过度自信（Judgment Bias）
- 主要发现：重用样例查询导致更低的查询正确性、更快的完成时间、更高的过度自信，但总体自信度无显著差异。调整偏差在深层结构锚（如连接条件）上强于表面结构锚（如选择条件参数）。领域熟悉度对调整的影响取决于锚类型：熟悉领域促进深层结构调整，不熟悉领域促进表面结构调整。
- 人—智能体关系：无智能体介入，纯人类手动编写和修改查询。
- 样本独立性：未发现与其他研究复用样本的证据，应为一手数据。
- 质量/限制：样本为数据库课程学生，可能难以推广至有经验的从业者；实验任务与真实环境中从查询库中自主搜索和选择重用可能不同；自信测量为单题五级李克特，未能捕捉更精细的信心校准；领域熟悉度操作虽有效但熟悉度等级为中等，可能未捕捉高熟悉度情境。

### 5. [Revising the Panko–Halverson taxonomy of spreadsheet errors](fulltext_candidates_local/06890_2010_revising-the-pankohalverson-taxonomy-of-spreadsheet-errors.md)
- 年份：2010；来源：Decision Support Systems；DOI：10.1016/j.dss.2010.02.009
- 证据角色：design_and_evaluation；主体：human_only；制品：spreadsheet_logic；行动：write；generate；inspect_or_review；test
- 编程情境定义：本文中的编程活动指电子表格建模（分析需求、设计算法、输入公式和数据）和测试（检查电子表格错误）。不包括终端用户的日常数据录入或使用电子表格进行决策分析中的错误，尽管分类法也提及了这些阶段，但主要是为错误分类提供背景。
- 任务与场景：本文基于多个来源：以往实验室实验中大学生创建电子表格解决文字问题，以及现场审计操作电子表格。作者还进行了一项编码可靠性研究，使用学生开发的电子表格样本。
- 方法与分析层级：概念性分类法修订，基于文献综述和人类错误研究；附带编码者间可靠性研究以评估分类法。；code_artifact_or_agent
- 样本/数据：作者可靠性研究使用了40个有错误的电子表格，来自一项先前研究的74个电子表格语料库（大学生用Kooker任务开发）；此外回顾了多个以往研究的样本（如Panko和Halverson的实验、Powell等人的审计研究等）。
- 理论/框架：Reason's Human Error Taxonomy (mistakes, slips, lapses)；Norman's slip/lapse distinction；Allwood's error types；Flower and Hayes' writing process model
- 自变量：无/未明示
- 中介：无/未明示
- 调节：无/未明示
- 因变量：无/未明示
- 主要发现：修订分类法将错误分为故意违规和无辜错误；无辜错误进一步分为定性错误和定量错误；定量错误分为规划错误（领域规划和电子表格表达规划）和执行错误（滑倒和遗忘）。编码者间可靠性高（96.6%）。分析显示规划错误占大多数，暗示自动化检测工具可能效果有限。强调应更多关注定性错误和生命周期各阶段的错误。
- 人—智能体关系：本文仅涉及人类开发者的错误，无人工智能体参与。
- 样本独立性：作者自己的样本是独立收集的，但可能与其他已发表研究共享部分数据。可靠性研究使用的电子表格来自同一之前研究，但作者未明确说明是否在同一篇论文中复用。
- 质量/限制：文章主要限于分类法提出和初步的可靠性评估，样本小且限于特定任务和学生开发者，可能影响外部效度；未深入探讨定性错误和生命周期各阶段错误的具体分类；缺乏大规模实证验证。

### 6. [An Empirical Investigation of End-User Query Development: The Effects of Improved Model Expressiveness vs. Complexity](fulltext_candidates_local/15408_2009_an-empirical-investigation-of-end-user-query-development-the-effects-of-improved-model-expressiv.md)
- 年份：2009；来源：Information Systems Research；DOI：10.1287/isre.1080.0181
- 证据角色：primary_empirical；主体：human_only；制品：database_query；行动：write；understand；debug_or_repair
- 编程情境定义：本文中的编程活动定义为终端用户根据给定的信息请求，查看逻辑数据模型（ER图和数据字典），编写SQL查询以从数据库中检索信息。用户可以反复修改和执行查询，直到满意。研究聚焦于查询构建的语义正确性。
- 任务与场景：实验室实验，参与者为14个信息请求编写SQL查询，可查看数据模型，使用UNIX shell脚本记录全过程。任务限时2小时，每次提交后显示查询结果或语法错误，可重复修改。
- 方法与分析层级：受控实验室实验，采用组间设计，使用ANCOVA分析数据。；individual
- 样本/数据：81名高年级本科生和硕士生（分两年实验，第一年45人，第二年35人），具备SQL和商业知识。数据包括每个参与者的每次查询尝试的错误数、时间和信心评分。
- 理论/框架：Cognitive Fit Theory；Ontology (Wand and Weber)；Task Complexity Theory；Bounded Rationality
- 自变量：model_expressiveness
- 中介：无/未明示
- 调节：无/未明示
- 因变量：semantic_errors；time；confidence
- 主要发现：对于较大规模的数据模型，本体清晰的模型（表达性更高）导致更多语义错误、更长的时间和更低的信心，与较小模型结果相反，支持了有限理性和复杂度权衡的观点。
- 人—智能体关系：人仅使用传统DBMS工具，没有智能代理。
- 样本独立性：两年实验使用不同学生，无重复样本。
- 质量/限制：实验室实验，学生样本，特定数据模型和查询请求可能影响外部有效性；未控制转换过程中的差异；只分析了最终查询。但设计严谨，有统计分析。

### 7. [Are Two Heads Better than One for Software Development? The Productivity Paradox of Pair Programming1](fulltext_candidates_local/05946_2009_are-two-heads-better-than-one-for-software-development-the-productivity-paradox-of-pair-programm.md)
- 年份：2009；来源：MIS Quarterly；DOI：10.2307/20650280
- 证据角色：primary_empirical；主体：human_only；制品：source_code；行动：write；modify_or_refactor；debug_or_repair
- 编程情境定义：本研究中编程指在Java开发环境中完成指定的软件维护任务，参与者需修改已有的不完整程序，实现缺失的类方法、编写新功能并确保程序正确运行，涉及代码编写、编译和调试。
- 任务与场景：受控实验室实验，参与者使用装有Java JDK5、Java文档和记事本的笔记本电脑，在2小时内完成一个编程任务（低复杂度为修改两个类中5个方法，高复杂度为修改五个类中7个方法）。实验模拟软件维护场景。
- 方法与分析层级：采用2（编程设置：结对 vs 单独编程）×2（任务复杂度：高 vs 低）的受控实验室实验，通过随机分组，比较结对编程组与名义对（随机配对的独立程序员）中最佳和第二佳成员在软件质量、满意度和信心上的差异，使用MANCOVA和ANCOVA进行分析。；multiple
- 样本/数据：122名具有Java编程经验的大学信息系统的本科生和研究生，自愿参与。随机分配到结对条件（30对）和个体条件（60人），个体数据随机组合成30个名义对。数据通过编程任务提交的代码（由两名评分员独立评估软件质量）和自评问卷收集。
- 理论/框架：Distributed cognition；Social facilitation；Social loafing；Group information processing；Group task typology
- 自变量：programming setting (pair vs individual)；task complexity (high vs low)
- 中介：无/未明示
- 调节：task complexity
- 因变量：software quality；satisfaction；confidence in performance
- 主要发现：结对编程组的软件质量显著高于名义对中的第二佳成员（p<0.01），但与最佳成员无显著差异（p=0.16）；结对组满意度显著高于最佳和第二佳成员（p<0.05）；结对组信心显著高于第二佳成员（p<0.01），但与最佳成员差异不显著（p=0.15）。任务复杂度对编程设置与软件质量的关系无调节效应。
- 人—智能体关系：全部为人类程序员交互，结对组两人协作编程，遵循XP实践（轮流担任驾驶员和导航员），无任何智能体或AI参与。
- 样本独立性：实验分三个学期进行，但单因素方差分析显示学期之间在因变量上无显著差异（软件质量F=0.54, p=0.58；满意度F=0.46, p=0.63；信心F=1.01, p=0.37），且每学期均随机分配被试至各处理，无证据表明样本重叠。
- 质量/限制：使用学生样本可能限制对专业程序员的泛化性；GPA作为编程能力指标可能不够精确；未测量任务完成时间；实验任务为维护型编程，创造性较低，可能影响结对收益的推广；未模拟团队长期磨合效应。

### 8. [A Comparison of Pair Versus Solo Programming Under Different Objectives: An Analytical Approach](fulltext_candidates_local/14912_2008_a-comparison-of-pair-versus-solo-programming-under-different-objectives-an-analytical-approach.md)
- 年份：2008；来源：Information Systems Research；DOI：10.1287/isre.1070.0147
- 证据角色：design_and_evaluation；主体：human_only；制品：source_code；行动：write；inspect_or_review
- 编程情境定义：编程指软件开发中为模块编写源代码以及结对编程中导航员审查代码的活动，同时涉及将模块集成为工作系统的过程。
- 任务与场景：论文通过构建优化模型和遗传算法求解，比较结对编程与单独编程在最小化开发工作量或时间方面的表现，数值实验基于模拟项目实例，参数参考一个电信软件公司的真实计费系统。
- 方法与分析层级：分析建模（整数规划、NP-hard性证明）与数值仿真实验相结合，利用遗传算法求解大规模问题实例。；project_or_community
- 样本/数据：使用人工生成的问题实例，参数依据一个大型电信软件公司的计费系统设定，未采用真实项目数据。
- 理论/框架：无/未明示
- 自变量：development approach (pair vs solo)；pair development overhead；pair formation effort；knowledge sharing coefficient；link density；number of modules；project deadline；number of expert developers
- 中介：无/未明示
- 调节：无/未明示
- 因变量：total system development effort；project completion time
- 主要发现：当知识共享效率高或系统连接密度大时，结对编程更优；结对编程能更好地利用团队中的专家知识；当结对开发开销或结对形成努力高时，单独编程更合适；截止日期紧时单独编程有利，而截止日期宽时结对编程有利；混合开发模式仅在模块组间特性差异显著时优于纯模式。
- 人—智能体关系：本研究比较人类程序员的结对编程与单独编程方法，不涉及任何AI智能体。
- 样本独立性：所有实例通过模拟生成，不存在样本复用问题。
- 质量/限制：模型假设参数（如知识共享系数）在实际中难以精确估计；未考虑结对编程的社会心理收益；激励问题可能引发搭便车行为；以工作量或时间作为唯一优化准则，忽略代码质量等其他维度；实验基于模拟数据，外部有效性受限。

### 9. [A critical review of the literature on spreadsheet errors](fulltext_candidates_local/10952_2008_a-critical-review-of-the-literature-on-spreadsheet-errors.md)
- 年份：2008；来源：Decision Support Systems；DOI：10.1016/j.dss.2008.06.001
- 证据角色：secondary_review；主体：human_only；制品：spreadsheet_logic；行动：write；inspect_or_review；debug_or_repair；test；modify_or_refactor
- 编程情境定义：本文中的“编程”指终端用户通过输入数据、编写公式和构建模型，在电子表格中创建可执行逻辑，以支持业务决策。任务涵盖电子表格错误的分类、影响、频率、产生与预防，以及检测。
- 任务与场景：任务是对关于电子表格错误的研究文献进行批判性综述，组织为错误分类、影响、频率、产生与预防、检测五个主题，并提出未来研究方向。
- 方法与分析层级：文献综述与批判性分析；multiple
- 样本/数据：综述纳入了多项已发表和未发表的研究，包括实验室实验、现场审计和访谈，涉及学生、专业人士、税务申报电子表格、大型工业电子表格等。
- 理论/框架：无/未明示
- 自变量：无/未明示
- 中介：无/未明示
- 调节：无/未明示
- 因变量：无/未明示
- 主要发现：文献显示，电子表格错误普遍且潜在成本高昂；现有错误分类法存在上下文依赖、定义模糊、未经验证等问题；关于错误影响的定量研究极少；错误频率的可靠估计因定义、检测方法和样本缺乏标准化而难以获得；关于错误产生和预防的实验室实验结论有限；有效的错误检测方法和工具研究严重不足。
- 人—智能体关系：本文综述的研究全部关于人类终端用户创建和审查电子表格，未涉及智能体或AI辅助编程。
- 样本独立性：不适用，本文为文献综述，不涉及样本独立性问题。
- 质量/限制：本文为文献综述，系统梳理了相关研究，并指出了现有研究的局限，如分类法缺乏标准化、现场审计方法不透明、缺少对错误影响的深入研究等。但综述本身未进行实证检验，其结论受限于所纳入研究的质量。

### 10. [An auditing protocol for spreadsheet models](fulltext_candidates_local/10446_2008_an-auditing-protocol-for-spreadsheet-models.md)
- 年份：2008；来源：Information & Management；DOI：10.1016/j.im.2008.03.004
- 证据角色：primary_empirical；主体：human_ai；制品：spreadsheet_logic；行动：inspect_or_review；debug_or_repair
- 编程情境定义：本文中的编程活动特指使用审计软件和人工检查来审查已有的操作型电子表格模型，以发现其中的逻辑、引用、硬编码、复制粘贴、数据输入和遗漏等错误。不包括编写或生成新电子表格。
- 任务与场景：任务是审计已完成的、从组织或网上收集的操作型电子表格，以发现各类错误。审计由受过训练的学生担任，使用两款商业审计软件（XL Analyst 和 Spreadsheet Professional），无开发者参与。
- 方法与分析层级：设计并实证测试了一个审计协议，对50个操作型电子表格进行审计，收集定量和定性数据，分析错误类型、发现方式、软件性能及审计时间。；code_artifact_or_agent
- 样本/数据：样本为50个来自不同组织（咨询公司、银行、学校、政府机构、能源公司等）的操作型电子表格，大小从25到63,731个公式不等。审计由经过10小时培训的本科生和研究生进行。数据包括电子表格大小、复杂度、函数使用、错误数量、发现方式、审计时间等。
- 理论/框架：无/未明示
- 自变量：无/未明示
- 中介：无/未明示
- 调节：无/未明示
- 因变量：错误实例数；错误单元格数；错误类型分布；发现方式分布；假阳性率；假阴性率；审计时间
- 主要发现：在47个电子表格中共发现483个错误实例（4855个错误单元格），公式错误率约1.79%。最有效的发现方法是地图分析（44.1%的错误实例）和Spreadsheet Professional计算测试（34.4%），代码检查只占18.2%。审计软件假阳性率达90%，但特定测试对特定错误类型有高阳性预测值（如“空白单元格被引用”与引用错误）。平均审计时间3.25小时。复杂公式和IF、VLOOKUP等函数易出错。
- 人—智能体关系：人类审计员使用审计软件作为工具，软件提供风险标记、可视化地图和计算测试结果，人类据此进行进一步检查并最终判定错误。人主导决策，软件辅助。
- 样本独立性：不清楚这些电子表格是否在多篇论文中被复用，本文仅报告了这50个样本的分析。
- 质量/限制：样本非随机，可能不具普遍性；审计员为学生，缺乏领域知识；未与开发者交互，可能遗漏部分错误；审计软件假阳性率高，可能影响效率；仅评估了协议发现某几类错误的能力，未衡量遗漏错误；审计时间受电子表格复杂度影响大。

### 11. [The Role of Visualization Tools in Spreadsheet Error Correction from a Cognitive Fit Perspective](fulltext_candidates_local/16148_2008_the-role-of-visualization-tools-in-spreadsheet-error-correction-from-a-cognitive-fit-perspective.md)
- 年份：2008；来源：Journal of the Association for Information Systems；DOI：10.17705/1jais.00162
- 证据角色：primary_empirical；主体：human_only；制品：spreadsheet_logic；行动：understand；inspect_or_review；debug_or_repair
- 编程情境定义：本文中的编程活动指终端用户在电子表格中检查并纠正公式错误，包括理解单元格间的引用关系，识别并修正错误的单元格引用（链接错误）或错误的运算符（非链接错误），从而调试和修复电子表格程序。
- 任务与场景：在实验室中，39名计算机科学/信息系统专业学生被随机分配至有无可视化工具组，在四个电子表格模型上完成错误纠正任务，每个模型包含两个链接错误和两个非链接错误，测量纠错时间和信心。
- 方法与分析层级：实验室实验，采用混合因子设计：工具类型（有无可视化工具）为被试间因子，错误类型（链接 vs. 非链接）为被试内因子。；individual
- 样本/数据：新加坡大学39名一、二年级计算机科学和信息系统专业学生，18人用工具，21人不用。每人纠正四个电子表格，每个含四个错误，共16个错误。数据包括纠错时间（分钟）和七点 Likert 信心评分。
- 理论/框架：Cognitive Fit Theory；Extended Cognitive Fit Model；Activity Framework (Ellis, 1989)
- 自变量：可视化工具（有/无）；错误类型（链接错误/非链接错误）
- 中介：无/未明示
- 调节：无/未明示
- 因变量：纠错时间（分钟）；信心（7点量表）
- 主要发现：有可视化工具时，纠正链接错误的速度显著快于无工具组，但信心无差异。有工具组纠正链接错误比非链接错误更快且信心更高。无工具组在两种错误类型上无显著差异。结果表明，可视化工具与任务需求匹配（认知匹配）时能提升性能，不匹配时可能产生干扰。
- 人—智能体关系：人类参与者使用内置可视化工具（箭头显示单元格引用关系）辅助理解电子表格结构并纠正公式错误，工具无自主决策能力，仅提供静态可视化支持。
- 样本独立性：实验使用独立样本，未提及数据复用。
- 质量/限制：学生样本限制外部效度；受试者首次使用工具，学习效应可能影响结果；工具特性特定，结论可能不适用于其他可视化工具；仅考察两种错误类型，未涵盖所有错误；实验室任务与真实纠错环境存在差异。

### 12. [Developing maintainable software: The Readable approach](fulltext_candidates_local/10622_2006_developing-maintainable-software-the-readable-approach.md)
- 年份：2006；来源：Decision Support Systems；DOI：10.1016/j.dss.2005.04.002
- 证据角色：primary_empirical；主体：human_only；制品：source_code；行动：understand
- 编程情境定义：本文中的编程活动指定为软件维护人员阅读和理解由他人编写的源代码，特别是理解程序组件之间的控制流，以促进软件维护。实验要求参与者阅读理解一个解决N皇后问题的Java程序，并回答关于控制流、数据流、程序状态和模块的真假问题。不直接涉及编写、修改或调试代码。
- 任务与场景：受控实验室实验，参与者被要求扮演维护人员，理解一个Java程序（N皇后问题），并完成20道真假题问卷，测量程序理解。实验组阅读采用Readable方法编写的程序，控制组阅读传统Java程序。
- 方法与分析层级：受控实验室实验；individual
- 样本/数据：美国公立大学信息系统专业学生81人，42人参与（实验组20人，控制组22人），随机分配。数据通过20项真/假问卷收集，每个构造（控制流、数据流、程序状态、模块）各5题，评分修正猜测。另有人口统计问卷。
- 理论/框架：Pennington's program understanding model
- 自变量：代码表示方法: Readable方法 vs. 传统Java
- 中介：无/未明示
- 调节：无/未明示
- 因变量：控制流理解得分；数据流理解得分；程序状态理解得分；模块理解得分
- 主要发现：Readable方法显著提高了参与者的控制流理解（H1得到支持，p=0.040），对程序状态理解有积极但不显著的趋势（H2 p=0.076），数据流和模块理解无显著差异（H3和H4不显著），表明该方法在改善程序理解的同时未产生负面影响。
- 人—智能体关系：无智能体参与；人类维护人员使用表格化静态表示（Readable方法）来理解程序源代码，实验比较了不同表示对理解的影响。
- 样本独立性：本研究样本独立，未发现与其他研究复用。
- 质量/限制：样本量小（每组20-22人），学生被试限制外部效度；仅测量程序理解而非实际维护行为；单一程序类型；Readable为原型环境；被试不熟悉Readable方法可能低估效果，但作者认为这加强了正向结果的说服力。

### 13. [Selecting optimal instantiations of data models—Theory and validation of an ex ante approach](fulltext_candidates_local/02594_2006_selecting-optimal-instantiations-of-data-modelstheory-and-validation-of-an-ex-ante-approach.md)
- 年份：2006；来源：Decision Support Systems；DOI：10.1016/j.dss.2005.10.002
- 证据角色：primary_empirical；主体：human_only；制品：database_query；行动：write；debug_or_repair
- 编程情境定义：编程行为在本研究中定义为最终用户根据给定的信息请求，使用SQL语言编写数据库查询。参与者需要理解请求，形成SQL语句，提交执行，并根据返回结果自行修正查询，直至认为正确满意。
- 任务与场景：实验室实验，59名学生参与者分别使用两种数据表示（3NF关系型或OOR对象关系型）为10个业务信息请求编写SQL查询。参与者可多次尝试每次请求，系统记录日志。收集了语义错误数、完成时间和信心评分。
- 方法与分析层级：受控实验室实验，受试者间设计，结合事后统计分析（MANCOVA等）比较两组在准确性、效率和信心上的差异。；individual
- 样本/数据：59名大学学生，均已接受SQL培训，按GPA排序后交替分入两组。实验在2小时内完成，数据来自系统日志和自评信心量表。
- 理论/框架：Sampling Theory；Halstead's Software Complexity Theory；Task Complexity Theory
- 自变量：Data representation type (3NF vs OOR)
- 中介：无/未明示
- 调节：无/未明示
- 因变量：Number of semantic errors；Time taken to complete query；Confidence in query correctness
- 主要发现：OOR实例化产生的查询复杂性更低，预测并验证了OOR用户比3NF用户产生显著更少的语义错误（p<0.0001）；在时间上OOR用户平均耗时更短但不显著；信心方面OOR用户反而低于3NF用户，与预期相反。结果支持根据加权平均查询复杂度事前评估最优数据表示的理论。
- 人—智能体关系：仅涉及人类参与者直接使用SQL查询数据库，无任何智能体或AI参与。
- 样本独立性：不清楚样本是否被其他研究复用，文中未提及。
- 质量/限制：局限：参与者为有基础培训的学生，非真实组织内最终用户；信息请求顺序非随机；未探讨其他复杂性度量；信心与准确性背离的原因有待进一步研究；外部效度有限。

### 14. [The Effects of State-Based and Event-Based Data Representation on User Performance in Query Formulation Tasks1,2](fulltext_candidates_local/01578_2006_the-effects-of-state-based-and-event-based-data-representation-on-user-performance-in-query-form.md)
- 年份：2006；来源：MIS Quarterly；DOI：10.2307/25148731
- 证据角色：primary_empirical；主体：human_only；制品：database_query；行动：write；test
- 编程情境定义：用户面对不同的实体关系图和关系模式，根据信息请求编写SQL查询，并可执行查询查看结果，属于即席查询编制任务。
- 任务与场景：被试通过互联网界面完成即席查询编制任务，每个被试随机分配到状态基、事件基或制品基的数据视图。先阅读业务描述、ER图和字段说明，然后编写7个SQL查询，可交互执行和修改。实验招募了北美和欧洲6所大学的342名信息系统学生，以额外学分作为激励。
- 方法与分析层级：受控实验（单因素被试间设计），通过互联网进行，测量查询准确性、信心和预测准确性，同时记录日志时间。；individual
- 样本/数据：342名信息系统背景的学生，随机分为三组处理。数据包括查询文本（经语义正确性评分）、五点信心自评、系统日志时间戳和人口学变量。
- 理论/框架：无/未明示
- 自变量：数据模型本体基础：状态基、事件基、制品基
- 中介：无/未明示
- 调节：E-R图阅读舒适度水平
- 因变量：查询准确性（语义正确性百分比）；信心（五点李克特自评）；预测准确性（平均预测得分）
- 主要发现：未发现处理对查询准确性和信心有显著主效应；事件基处理显著提高了预测准确性，尤其对于E-R图阅读舒适度低的被试；状态基处理在后期查询上花费的时间显著多于其他两种处理。
- 人—智能体关系：不适用（只有人参与）。
- 样本独立性：未提及与其他研究样本重叠，应为独立样本。
- 质量/限制：实验通过网络进行，缺乏实验室控制，可能存在干扰变量；样本为学生，可能影响外部效度；不同处理间的模型复杂度差异可能混淆结果；信息请求可能允许被试通过词汇映射而不深入理解语义。

### 15. [The Role of Cognitive Fit in the Relationship Between Software Comprehension and Modification1](fulltext_candidates_local/00546_2006_the-role-of-cognitive-fit-in-the-relationship-between-software-comprehension-and-modification1.md)
- 年份：2006；来源：MIS Quarterly；DOI：10.2307/25148716
- 证据角色：primary_empirical；主体：human_only；制品：source_code；行动：understand；modify_or_refactor
- 编程情境定义：本研究中编程是指专业软件维护人员理解现有COBOL源代码，并根据修改规范对程序进行增强性修改（添加功能或改变控制流），不包含从零编写程序，仅限于维护性修改。
- 任务与场景：实验室实验，24名有经验的COBOL程序员在控制条件下先学习程序（会计领域熟悉，水文领域不熟悉），然后根据书面修改说明完成功能修改或控制流修改任务，修改前后测量程序理解水平，并评估修改任务绩效。实验时间约4小时。
- 方法与分析层级：实验研究，2（应用领域熟悉度：熟悉/不熟悉）×2（修改任务类型：功能/控制流）混合设计，熟悉度为组内变量，任务类型为组间变量，同时纳入理解变化百分比作为连续预测变量，使用SAS PROC MIXED分析三阶交互。；individual
- 样本/数据：24名IT专业人员，平均10.7年经验，熟悉COBOL会计应用，来自多个组织。数据包括修改前后程序理解测验分数（百分比变化）、修改任务绩效评分（100分量表），以及操控的领域熟悉度和任务类型。
- 理论/框架：Cognitive Fit Theory；Dual-task interference；Distributed cognition；Pennington's program information types；von Mayrhauser and Vans' program comprehension model
- 自变量：application_domain_familiarity；modification_task_type；percent_change_in_comprehension
- 中介：无/未明示
- 调节：无/未明示
- 因变量：modification_task_performance
- 主要发现：认知匹配调节程序理解变化与修改绩效间的关系：当认知匹配存在时（熟悉领域+功能任务，或不熟悉领域+控制流任务），理解提升与修改绩效正相关；当认知不匹配时，理解提升与修改绩效负相关。表明高理解并不总能带来高修改绩效，认知不匹配时过度理解可能干扰修改。
- 人—智能体关系：只有人类参与者，无AI或智能体介入。人类程序员通过阅读和修改源代码完成维护任务。
- 样本独立性：每个参与者完成两个领域任务，观测值存在重复测量，分析时使用混合模型指定了组内和组间变量。
- 质量/限制：优势：使用IT专业人员，实验设计消除了个体差异和任务类型混淆，操控有效，分析考虑了重复测量和非正态性。局限：样本量较小（24人），但混合模型和稳健检验表明统计力足够；实验材料和任务虽经仔细匹配，外部效度受限于COBOL和特定维护类型；修改绩效评分虽有评分者信度，但仍存在主观成分；认知机制（如双任务干扰）通过绩效间接推断，未使用过程追踪。

### 16. [The role of spreadsheet knowledge in user-developed application success](fulltext_candidates_local/08484_2005_the-role-of-spreadsheet-knowledge-in-user-developed-application-success.md)
- 年份：2005；来源：Decision Support Systems；DOI：10.1016/j.dss.2004.01.002
- 证据角色：primary_empirical；主体：human_only；制品：spreadsheet_logic；行动：write；debug_or_repair；modify_or_refactor
- 编程情境定义：在本文中，编程是指终端用户使用电子表格软件（Microsoft Excel）开发电子表格应用程序，包括设计公式、布局和功能以解决具体问题（租车选择比较）。随后用户使用他人开发的电子表格时，允许进行修正和调整，这涉及修改和修复程序逻辑。
- 任务与场景：实验室实验，参与者首先开发一个电子表格解决租车公司选择问题，然后使用另一参与者开发的电子表格回答10个决策问题，最后填写问卷评价系统质量和满意度。
- 方法与分析层级：实验结合问卷，通过结构方程模型检验假设。使用验证的量表测量电子表格知识、系统质量（独立专家评估）、感知系统质量、用户满意度和个体影响（决策正确数）。；individual
- 样本/数据：159名志愿者（67.3%女性，平均年龄42.7，平均电子表格经验4.5年），每人开发一个电子表格并评价另一人的应用，共159个应用。
- 理论/框架：DeLone and McLean IS Success Model
- 自变量：开发者电子表格知识；用户电子表格知识
- 中介：系统质量；感知系统质量；用户满意度
- 调节：无/未明示
- 因变量：系统质量；感知系统质量；用户满意度；个体影响
- 主要发现：开发者电子表格知识显著正向预测系统质量，系统质量通过感知系统质量和用户满意度间接影响个体影响；用户电子表格知识对个体影响有显著直接正向效应，但不影响感知质量或满意度。用户满意度和用户知识独立且同等程度地影响个体影响。
- 人—智能体关系：无智能体参与，仅涉及人类开发者与用户。
- 样本独立性：unclear
- 质量/限制：便利样本可能限制外部效度；电子表格规模较小，结论未必适用于复杂应用；用自评知识和单一客观绩效指标；模型解释了部分方差，仍有其他因素未纳入。

### 17. [The effects of information request ambiguity and construct incongruence on query development](fulltext_candidates_local/20989_2001_the-effects-of-information-request-ambiguity-and-construct-incongruence-on-query-development.md)
- 年份：2001；来源：Decision Support Systems；DOI：10.1016/s0167-9236(01)00097-5
- 证据角色：primary_empirical；主体：human_only；制品：database_query；行动：write；understand
- 编程情境定义：本研究中，编程被定义为最终用户在交互式关系数据库查询语言中编写SQL查询。任务要求参与者根据给定的信息请求（自然语言或伪SQL）构建并执行Oracle SQL查询，以从数据库中检索指定数据。不包括数据库设计或修改，仅聚焦于查询编写。
- 任务与场景：实验室实验，参与者接收模拟的业务信息请求（分为模糊的“经理英语”和较不模糊的“伪SQL”两种形式），使用Oracle SQL编写查询，直到对查询结果满意为止。系统记录所有交互和时间戳。
- 方法与分析层级：2×2组内因子受控实验室实验，采用ANCOVA分析查询复杂性作为协变量。；individual
- 样本/数据：23名信息系统课程的商学研究生，具有SQL和ER图培训经验。分为两个等组，每组在模糊性和不一致性条件上交叉，共完成202个查询响应（每个参与者完成10个信息请求）。
- 理论/框架：Norman的用户查询性能模型（认知工程）；语义距离概念；任务技术匹配理论（Goodhue & Thompson, 1995）；认知负载理论
- 自变量：信息请求模糊性（模糊 vs. 不模糊）；构造不一致性（一致 vs. 不一致）
- 中介：无/未明示
- 调节：无/未明示
- 因变量：准确性（微观错误数、宏观错误数）；效率（总时间、查询尝试次数）；信心（自评7点 Likert量表）
- 主要发现：信息请求的模糊性显著增加了错误数量（微观和宏观）和尝试次数，但对时间和信心无显著影响。构造不一致性显著增加了所有错误类型，增加了尝试次数，并降低了信心。查询复杂性在所有绩效指标上均表现显著负效应。模糊性主要导致属性选择和SELECT子句错误；不一致性则广泛增加了各类错误。
- 人—智能体关系：仅有人类参与者直接编写SQL查询，无任何智能体介入。
- 样本独立性：虽然每个参与者完成了多个查询，但每个信息请求的版本仅分配给一组，因此不同条件下没有重复使用同一参与者同一请求的响应，数据点间相互独立。
- 质量/限制：样本量较小（23人），且为研究生，可能限制外部效度；组内设计可能产生疲劳或顺序效应；一致性条件中故意使一致请求的Halstead难度更高，可能引入混杂效应；仅依赖SQL查询，未考虑其他数据库交互方式；信心测量为主观自评，可能不够敏感。

### 18. [Applications development by end-users: can quality be improved?](fulltext_candidates_local/20843_2000_applications-development-by-end-users-can-quality-be-improved.md)
- 年份：2000；来源：Decision Support Systems；DOI：10.1016/s0167-9236(00)00068-3
- 证据角色：primary_empirical；主体：human_only；制品：spreadsheet_logic；行动：generate
- 编程情境定义：本文中，编程指最终用户使用电子表格软件（如Excel）创建满足特定业务需求的电子表格应用程序，包括输入数据、计算公式、生成输出和设计布局。任务不包括数据库查询、低代码或传统编程。
- 任务与场景：实验通过因特网进行，参与者为具有全职工作经验和电子表格使用经验的最终用户志愿者。实验包括前测（开发一个电子表格）、随机分配接受系统分析与设计培训（处理组）或无关培训（对照组）、后测（开发另一个电子表格）。测量电子表格的完整性、准确性、设计质量和用户满意度。
- 方法与分析层级：实验法；individual
- 样本/数据：样本为73名最终用户，通过电子邮件讨论组、专业组织等渠道招募；平均工作年限17.7年，84%男性，大多具有本科及以上学历。数据来自前测和后测的电子表格文件、在线问卷和用户满意度评分。
- 理论/框架：EUC Management Research Model
- 自变量：培训（系统分析与设计培训 vs. 无关培训）
- 中介：无/未明示
- 调节：无/未明示
- 因变量：完整性；准确性；设计质量；最终用户满意度
- 主要发现：接受系统分析与设计培训的最终用户开发的电子表格在设计质量上显著优于对照组，但在完整性、准确性和用户满意度上无显著差异。设计改进体现在模块化布局、文档和正确的单元格引用。高完整性和准确性可能由于任务简单且受试者技能熟练。
- 人—智能体关系：不适用，本研究不涉及智能体。
- 样本独立性：本研究样本为独立招募的最终用户志愿者，未见与其他研究复用的明确证据。
- 质量/限制：样本为志愿者而非随机样本，外部效度受限制；实验设计可能有人工性，任务较简单，可能影响准确性和完整性结果的变异性；培训内容为五分钟的多媒体培训，可能不足以产生全面改进。

### 19. [Using a structured design approach to reduce risks in end user spreadsheet development](fulltext_candidates_local/22602_2000_using-a-structured-design-approach-to-reduce-risks-in-end-user-spreadsheet-development.md)
- 年份：2000；来源：Information & Management；DOI：10.1016/s0378-7206(99)00029-4
- 证据角色：primary_empirical；主体：human_only；制品：spreadsheet_logic；行动：write；test
- 编程情境定义：本文中编程指开发包含多个链接工作表和公式的电子表格工作簿；参与者需根据预算问题建立可执行模型并进行情景分析，不包括一般的电子表格使用或数据分析。
- 任务与场景：两个实地实验。参与者为会计和工商管理专业学生，任务是根据预算问题开发一个包含10个工作表、51个链接（研究2为66个链接）的电子表格工作簿，并执行情景分析。研究1允许自行结对或单人，研究2要求单人完成。
- 方法与分析层级：现场实验，被试间设计，随机分配至结构化设计组（使用数据流图进行设计）和控制组（临时设计）。；individual
- 样本/数据：研究1：61名高年级和硕士阶段会计与工商管理专业学生，随机分两组。研究2：88名学生（会计和非会计专业），全部单人完成。数据来自预测试和后测试问卷、开发日志和提交的电子表格文件。
- 理论/框架：无/未明示
- 自变量：development_approach (structured vs ad hoc)；configuration (single vs pair) - Study 1 only；gender；domain_expertise (accounting vs other)；pre_test_excel_expertise；pre_test_dfd_expertise；pre_test_design_confidence
- 中介：无/未明示
- 调节：无/未明示
- 因变量：number_of_linking_errors；linking_error_percentage；number_of_conceptual_errors；number_of_oversight_errors；total_errors；development_time；post_test_spreadsheet_expertise；post_test_excel_expertise；post_test_design_confidence；post_test_coding_confidence；post_test_error_free_confidence
- 主要发现：结构化设计方法显著减少了链接错误（研究1：结构化组平均7% vs 控制组10%；研究2：8.37% vs 16.75%），但对概念性和疏忽性错误无影响。配置调节了方法效果：单人工作时方法效果显著，结对时优势减弱。预测试Excel专业知识是错误率和时间的重要预测因子。女性疏忽性错误显著更少，但报告更低的自评能力。领域专业知识（会计）增强设计信心。开发时间无显著差异。
- 人—智能体关系：无智能体参与，研究的是人类开发者使用结构化设计方法对电子表格开发质量的影响。
- 样本独立性：两次实验在不同时间进行，样本不同，独立。
- 质量/限制：样本为学生，外部效度受限；研究1中自行结对引入选择偏差；未测量结构化方法对可用性、可维护性、可审计性的影响；错误率与决策质量的关系未验证；未纳入学习设计方法的时间成本。

### 20. [Applying Code Inspection to Spreadsheet Testing](fulltext_candidates_local/25049_1999_applying-code-inspection-to-spreadsheet-testing.md)
- 年份：1999；来源：Journal of Management Information Systems；DOI：10.1080/07421222.1999.11518250
- 证据角色：primary_empirical；主体：human_only；制品：spreadsheet_logic；行动：inspect_or_review
- 编程情境定义：本文中的编程活动指对电子表格中的公式和数值进行代码检查（code inspection），以发现其中的错误。任务不包括编写、修改或执行电子表格，仅通过审查文档来发现错误。
- 任务与场景：实验要求被试对一份已植入8个错误的电子表格进行代码检查，先独自检查，再以三人小组重新检查。被试为60名MIS专业本科生，实验在课堂外进行，有时间限制，但强调不要仓促。
- 方法与分析层级：实验室内实验，采用单因素重复测量设计（个体阶段与群体阶段），并分析错误类型和公式长度的影响。；multiple
- 样本/数据：60名三、四年级MIS本科生，均修过电子表格课程。随机分配到20个三人小组。数据为每个被试和每组检测到的错误数量，以及估计的错误检测百分比。
- 理论/框架：无/未明示
- 自变量：检查方式（个体/群体）；错误类型（机械错误/遗漏错误）；公式长度（短/长）
- 中介：无/未明示
- 调节：无/未明示
- 因变量：错误检测百分比；估计错误检测百分比（过度自信）；检测到错误的数量
- 主要发现：个体代码检查平均发现63%的错误，三人小组检查发现83%，但小组并未发现新错误，仅汇集了个体的发现。小组对遗漏错误和长公式中的机械错误改进最大。被试存在过度自信，尤其当发现错误较少时。
- 人—智能体关系：此研究无智能体参与，仅涉及人类对电子表格的代码检查。
- 样本独立性：该样本可能与前人研究（如Panko and Sprague 1998）部分重叠，但本文明确指出不同时间进行，无直接证据表明复用样本。
- 质量/限制：样本量小（60人），被试为学生，可能缺乏外部有效性。实验材料简单，仅8个错误，存在天花板效应。缺乏真实工作场景的压力和反馈。没有测量长期效果或组织接受度。

### 21. [Hitting the wall: errors in developing and code inspecting a `simple' spreadsheet model](fulltext_candidates_local/21491_1998_hitting-the-wall-errors-in-developing-and-code-inspecting-a-simple-spreadsheet-model.md)
- 年份：1998；来源：Decision Support Systems；DOI：10.1016/s0167-9236(97)00038-9
- 证据角色：primary_empirical；主体：human_only；制品：spreadsheet_logic；行动：write；inspect_or_review
- 编程情境定义：编程是指根据给定的文字问题，在电子表格中建立模型，输入公式和数值以计算出结果；代码审查是指检查电子表格中的公式和引用，以发现错误。不包括纯粹的数据录入或格式化操作。
- 任务与场景：受试者在家打开密封信封，根据“Wall Task”问题在空白电子表格中构建模型，时间为45分钟；之后部分本科生接受代码审查训练，审查自己之前构建的模型。
- 方法与分析层级：实验（开发阶段和代码审查阶段）；individual
- 样本/数据：152名夏威夷大学学生：102名高年级MIS专业本科生，50名MBA学生。MBA中26人为无经验者（≤100小时），17人为有经验者（≥250小时）。数据来自电子表格文件和事后问卷。
- 理论/框架：无/未明示
- 自变量：参与者组别（本科生 vs MBA）；电子表格经验水平（无经验 vs 有经验）
- 中介：无/未明示
- 调节：无/未明示
- 因变量：模型包含错误的百分比；每个模型的错误数；单元格错误率；错误类型百分比；代码审查纠正错误百分比
- 主要发现：35%的模型至少包含一个错误；CER为2.0%；本科生与MBA之间错误率无显著差异；即使在250小时以上经验的MBA中，仍有24%模型有错误；错误类型主要是遗漏错误(54%)和逻辑错误(43%)；代码审查仅纠正了18%的错误；人工检查自己的模型效果很差。
- 人—智能体关系：纯粹人类活动，没有智能体参与。人类作为开发者构建电子表格，然后作为审查者检查自己的电子表格。
- 样本独立性：unclear
- 质量/限制：任务简单，外部效度可能有限；代码审查阶段样本较小且仅限本科生；在家完成可能引入环境差异；机械错误极少，可能与任务简单有关；事后问卷测量自我报告，可能存在偏差。

### 22. [The Relevance of Application Domain Knowledge: Characterizing the Computer Program Comprehension Process](fulltext_candidates_local/24954_1998_the-relevance-of-application-domain-knowledge-characterizing-the-computer-program-comprehension.md)
- 年份：1998；来源：Journal of Management Information Systems；DOI：10.1080/07421222.1998.11518196
- 证据角色：primary_empirical；主体：human_only；制品：source_code；行动：understand
- 编程情境定义：本文研究的编程活动是专业程序员对现有 COBOL 程序进行阅读理解，以回答理解问题，不包括编写或修改代码。
- 任务与场景：参与者在实验室中分别研究一个熟悉的会计工资程序和一个陌生的水文学程序，每个程序限时 15 分钟，之后回答 10 道是/非理解问题。研究采用并发口头协议采集认知过程。
- 方法与分析层级：实验室实验，采用 2（应用领域熟悉度：熟悉 vs. 陌生）× 3（理解过程组：自上而下、自下而上、灵活）混合设计，并借助并发口头协议分析进行过程追踪。；individual
- 样本/数据：24 名信息系统专业人员，平均 36.5 岁，平均 10.7 年 IS 经验，熟练 COBOL。口头协议数据经转录后编码为假设/推论、知识类型（应用域/编程域）、细节层次；并收集理解问题正确率。
- 理论/框架：Brooks' top-down theory of program comprehension；Pennington's bottom-up theory of program comprehension；Letovsky's knowledge-based understander model；metacognition theory (Flavell)
- 自变量：application_domain_familiarity (familiar vs. unfamiliar, within-subject)；comprehension_process_group (top-down, bottom-up, flexible, between-subject)
- 中介：无/未明示
- 调节：无/未明示
- 因变量：process_score (hypotheses minus inferences)；number of application domain references；number of programming domain references；level of application references (high vs. low)；level of programming references (high vs. low)；comprehension question accuracy (%)
- 主要发现：程序员在熟悉应用领域中多使用自上而下理解过程，在陌生领域多使用自下而上过程。被试可分为三类稳定的过程组：自上而下组、自下而上组和灵活组（随领域切换过程）。灵活组的理解正确率显著最高（71%），自下而上组次之（61%），自上而下组最低（50%）。自上而下组在熟悉域中产生更多且更高层次的应用域引用；灵活组在编程域引用总数少于其他两组，且应用域引用的层次低于自上而下组。元认知问卷显示程序员自我报告的过程与实际观察到的并不一致，可能存在社会期望偏差；灵活组更年轻，经验较少，可能避免了拘泥于固定过程的“定势效应”。
- 人—智能体关系：无智能体参与，仅研究人类程序员的理解过程。
- 样本独立性：样本可能复用自 Shaft & Vessey (1995) 的研究，但本文侧重过程组划分与元认知等新分析，若进行证据合成需注意样本重叠。
- 质量/限制：优点：使用专业程序员、正式的协议编码、重复测量设计。局限：样本量较小（N=24），但符合过程追踪研究惯例；程序规模仅约 400 行，且为 COBOL，可能限制外部推演力；元认知测量依赖事后自我报告，可能受社会期望偏差影响；过程组的划分基于中位数切分，可能损失信息。

### 23. [Why Is Programming (Sometimes) So Difficult? Programming as Scientific Discovery in Multiple Problem Spaces](fulltext_candidates_local/26760_1997_why-is-programming-sometimes-so-difficult-programming-as-scientific-discovery-in-multiple-proble.md)
- 年份：1997；来源：Information Systems Research；DOI：10.1287/isre.8.1.25
- 证据角色：primary_empirical；主体：human_only；制品：source_code；行动：write；understand；modify_or_refactor
- 编程情境定义：编程被定义为在规则空间、实例空间和表征空间中的搜索过程。具体编程任务包括：从零开始编写面向对象程序解决汉诺塔同构问题，理解给定程序如何解决问题，以及重用旧程序解决新问题。编程活动涉及编写新代码、理解现有代码和修改代码。
- 任务与场景：实验室实验，被试为卡内基梅隆大学数学/计算机科学专业高年级本科生，有面向对象编程经验。实验1：编写C++程序解决3怪物变换（MC）或3怪物转移（MT）问题；实验2：理解给定程序并运行测试用例；实验3：重用旧程序解决新问题（5个怪物）。每次实验均使用了问题和程序同构体来控制表征。口头协议被录音并转录。
- 方法与分析层级：控制实验结合口头协议分析。开发了编码方案对认知操作（规则开发、心理模拟、表征构建/映射）进行分类，构建问题行为图，比较代表组和对照组在认知过程和产出上的差异。；individual
- 样本/数据：实验1：8名被试（每组4人）；实验2：24名被试（每组12人）；实验3：12名被试（9名代表组，3名对照组）。均从同一门软件工程课程招募，但各实验被试不同。数据包括口语协议录音文字记录、书面程序、测试答案和完成时间。总共分析约38.5小时的口语协议。
- 理论/框架：Programming as scientific discovery in multiple problem spaces；Dual space search model of scientific discovery
- 自变量：problem_isomorph_type
- 中介：无/未明示
- 调节：无/未明示
- 因变量：time_spent；program_generality；number_of_mental_simulations；comprehension_score；reuse_success
- 主要发现：当编程任务需要表征改变时，认知难度显著增加。实验1中，代表组产生特定程序而非通用程序；实验2中，代表组需要更多时间和心理模拟来理解程序；实验3中，仅33%的代表组被试成功重用程序，成功者通过引入中间表征完成映射。总体表明，编程作为一种多空间搜索，表征改变是导致困难的关键因素。
- 人—智能体关系：本研究不涉及智能体，仅研究人类程序员个体在不使用AI辅助下的编程认知过程。
- 样本独立性：三个实验使用了不同的受试者，未发现重复参与。
- 质量/限制：研究采用小规模程序、特定问题同构体和学生样本，限制了外部效度。但严格控制的实验设计和详细的口头协议分析提供了高内部效度和深入认知过程洞察。局限于面向对象编程，且无法完全排除表征改变时的言语缺失导致的编码困难。

### 24. [An experimental investigation into the process of knowledge-based systems development](fulltext_candidates_local/23206_1996_an-experimental-investigation-into-the-process-of-knowledge-based-systems-development.md)
- 年份：1996；来源：European Journal of Information Systems；DOI：10.1057/ejis.1996.29
- 证据角色：primary_empirical；主体：human_only；制品：source_code；行动：write；debug_or_repair；modify_or_refactor；test
- 编程情境定义：参与者使用CLIPS工具，通过编写规则和对象（混合表示），开发一个交互式MBA课程规划专家系统。编程活动包括知识的形式化表达、编写可执行规则与对象代码、迭代修改原型、测试和修复异常，直至系统达到要求的功能性和可用性。
- 任务与场景：在研究生课程的7周实验中，24名学生独立开发一个MBA课程规划专家系统。系统需根据用户偏好生成4个学期的个性化课程表。他们利用CLIPS开发，分为规则与混合表示、快速与结构化原型、经验与新手程序员共8种条件。
- 方法与分析层级：实验法（2x2x2因子设计）；individual
- 样本/数据：24名信息系统专业研究生（剔除2名未完成者），按编程经验分为两组，随机分配到四种处理组合。收集了时间日志、提交的代码原型（包括中间版本和最终产品），以及作者对最终产品功能性和可用性的Likert量表评分。
- 理论/框架：Cognitive fit theory
- 自变量：Knowledge representation type；Development methodology；Programmer quality
- 中介：无/未明示
- 调节：无/未明示
- 因变量：Internal quality: number of anomalies；External quality: functionality score；External quality: usability score；Process: product size (LOC)；Process: design time；Process: coding time；Process: coding productivity；Process: project productivity；Process: changed lines of code
- 主要发现：快速原型与规则表示结合产生最高的功能性和可用性，但与混合表示结合则导致最差的可用性。结构化原型与混合表示组合较为稳健。程序员经验显著提高编码生产率，进而提升可用性，但对功能性的影响不显著。内部质量（异常数量）与可用性正相关，而与功能性无关。
- 人—智能体关系：无智能体参与，人类程序员独立使用KBS开发工具CLIPS完成编程任务。
- 样本独立性：未见与其他论文复用样本的证据，但参与者来自同一班级，可能通过非正式交流相互影响，但作者通过统一信息发布和随机分配加以控制。
- 质量/限制：优点：严格的因子实验设计，随机分配，多种过程和内容指标，统计方法适当。局限：学生样本可能限制外部普适性；任务规模较小；时间报告依赖自我记录可能存在偏差；开发者同时也是评分者可能引入主观性，但通过双人独立评分并协商一致加以控制。

### 25. [The Influence of Database Structure Representation on Database System Learning and Use](fulltext_candidates_local/24810_1996_the-influence-of-database-structure-representation-on-database-system-learning-and-use.md)
- 年份：1996；来源：Journal of Management Information Systems；DOI：10.1080/07421222.1996.11518106
- 证据角色：primary_empirical；主体：human_only；制品：source_code；行动：write；understand；inspect_or_review
- 编程情境定义：本文中的编程活动是指学习和使用标准SQL查询语言，从关系数据库中检索数据，包括编写SQL查询、解释查询语义、生成查询解决问题以及评估给定查询是否可基于数据库执行。数据库结构表示是理解和编写查询的基础，编程任务涵盖查询编写、阅读、问题解决和评估。
- 任务与场景：受控实验室实验，52名研究生首先学习阅读四种数据库结构表示之一（LDS、Table、Table/arrows、Table/text），随后学习八种标准SQL查询类型，最后完成基于新数据库的查询编写、查询阅读、问题解决和查询评估任务。所有指令和反馈通过计算机程序呈现，数据自动记录。
- 方法与分析层级：随机分组受控实验，采用4（数据库表示）×2（阶段：表示学习、查询语言学习）混合设计，通过ANOVA和事前对比分析处理效应。；individual
- 样本/数据：52名研究生（多数拥有商业经验），随机分配至4种数据库表示处理组，每组13人。收集数据包括学习阶段阅读时间、练习时间、各项任务正确数及反应时，以及两个数据库上的记忆回忆、问题生成和问题/查询评估得分。
- 理论/框架：无/未明示
- 自变量：{'name': '数据库表示语义', 'description': '实体语义（LDS）vs 表格语义（Table、Table/arrows、Table/text）', 'type': 'categorical'}；{'name': '数据库表示符号', 'description': '图形与文本结合（LDS、Table、Table/arrows）vs 纯文本（Table/text）', 'type': 'categorical'}；{'name': '关系表示方式', 'description': '显式关系表示（LDS、Table/arrows）vs 隐式关系表示（Table、Table/text）', 'type': 'categorical'}
- 中介：无/未明示
- 调节：无/未明示
- 因变量：{'name': '表示学习总时间', 'description': '阅读材料时间 + 达到正确回答标准所需练习时间'}；{'name': '表示学习练习时间', 'description': '在表示理解练习中达到每概念连续3题正确的总时间'}；{'name': '表示要素回忆数量', 'description': '记忆任务中正确回忆的实体/表、属性/列、关系/外键总数'}；{'name': '查询语言学习总时间', 'description': '阅读SQL说明时间 + 达到每个查询类型2/3正确率的练习时间'}；{'name': '查询语言练习时间', 'description': '在SQL练习中达到各查询类型标准的练习时间'}；{'name': '正确编写查询数', 'description': '查询编写任务中生成的正确SQL语句数'}；{'name': '正确查询评估数', 'description': '判断给定SQL语句是否可执行正确的数量'}；{'name': '有效问题/查询生成数', 'description': '问题解决任务中生成的可用数据库回答的有效问题或查询数'}
- 主要发现：实体语义（LDS）显著缩短表示学习练习时间，增加实体和关系记忆数，但在SQL学习上显著增加了练习时间，并导致查询编写和评估正确数降低。图形符号对表示学习无显著影响，但图形组在SQL学习上花费更多练习时间。显式关系表示缩短了表示练习时间，却延长了SQL学习时间并减低了查询评估正确数。这些相反效果表明，有助于理解数据库内容的表示特征可能阻碍特定查询语言（SQL）的学习和使用。
- 人—智能体关系：研究不涉及任何智能体，参与者为人类，仅使用数据库管理系统和SQL查询语言。
- 样本独立性：未提及复用其他研究样本，视为独立样本。
- 质量/限制：样本较小（52人）且仅限于研究生，可能限制对实际终端用户的推广。实验耗时较长（每阶段3-6小时），可能引起疲劳效应。仅使用SQL作为查询语言，可能存在表示偏向，削弱了实体语义的优势。部分任务（如问题生成）未产生显著差异，可能因测量不够敏感。缺乏对长期记忆保持或真实工作场景的检验。

### 26. [User-Developed Applications: An Empirical Study of Application Quality and Developer Productivity](fulltext_candidates_local/24828_1996_user-developed-applications-an-empirical-study-of-application-quality-and-developer-productivity.md)
- 年份：1996；来源：Journal of Management Information Systems；DOI：10.1080/07421222.1996.11518117
- 证据角色：primary_empirical；主体：human_only；制品：source_code；行动：write；test；debug_or_repair；inspect_or_review
- 编程情境定义：本文中的编程是指使用dBASE语言编写、测试和调试完整的数据库应用程序，包括数据录入、更新、查询、报表和菜单等功能，属于事务处理系统开发。分析、设计、文档等系统开发生命周期活动虽不直接是编写代码，但作为开发任务的一部分被计入时间。
- 任务与场景：在课堂实验中，由5组MBA学生（终端用户）和5组CIS本科生（代用IS专业人员）分别开发5个真实业务人员提出的数据库应用系统，使用dBASE完成编码、测试和文档，周期6周。终端用户组可咨询扮演信息中心顾问的教师，两组都可使用实验室支持。
- 方法与分析层级：实验室实验，配对团队间比较。；team
- 样本/数据：10个开发团队，每组3人，分别来自一所大学的MBA班（代表终端用户）和CIS本科班（代表代用IS专业人员）。每个MBA团队有至少2年相关业务经验，CIS团队平均修过5门CIS课程。收集数据包括时间日志、代码行数、功能点、缺陷数和主观质量评分。
- 理论/框架：无/未明示
- 自变量：developer_type
- 中介：无/未明示
- 调节：无/未明示
- 因变量：productivity_LOC_per_hour；productivity_FP_per_hour；quality_defect_per_FP；quality_attribute_score
- 主要发现：代用IS专业人员的生产率（按功能点/小时和代码行/小时）显著高于终端用户；其应用质量也显著更高，缺陷密度更低且质量属性评分更优。终端用户开发的应用存在严重的数据完整性和设计缺陷。
- 人—智能体关系：无智能体参与，完全由人类手动编写和测试程序。
- 样本独立性：5个应用各自独立开发，配对团队间无交叉，未发现复用样本。
- 质量/限制：主要局限：小样本量（仅5个应用），使用学生代用而非有经验的IS专业人员，可能低估实际差异；实验室环境降低了外部效度；终端用户组没有与IS代用组强制沟通，可能夸大分析时间差异。信度尚可，效度中等。

### 27. [Research Report—The Relevance of Application Domain Knowledge: The Case of Computer Program Comprehension](fulltext_candidates_local/26710_1995_research-reportthe-relevance-of-application-domain-knowledge-the-case-of-computer-program-compre.md)
- 年份：1995；来源：Information Systems Research；DOI：10.1287/isre.6.3.286
- 证据角色：primary_empirical；主体：human_only；制品：source_code；行动：understand；inspect_or_review
- 编程情境定义：本文中，编程指理解现有程序代码（comprehension），即程序员通过阅读代码、形成和验证假设或基于代码细节做出推断来建立对程序功能和结构的心理表征。任务不涉及编写、修改、测试或调试代码。
- 任务与场景：在实验室环境中，24名专业COBOL程序员分别在15分钟内理解两个程序：一个来自熟悉的应用领域（会计），另一个来自不熟悉的领域（水利），并要求出声思维。研究者比较了两个条件下假设和推断的数量。
- 方法与分析层级：受试内设计，过程追踪研究，并发口头协议分析。假设和推断由两名评定者根据编码手册独立编码，计算过程得分（假设数减推断数），使用配对t检验。；individual
- 样本/数据：24名信息系统专业人员，平均年龄36.5岁，平均10.7年行业经验，多为男性，具有会计应用开发经验，无水利领域知识。每人产生两个口头协议（熟悉和不熟悉领域），共48个协议。
- 理论/框架：Brooks' top-down comprehension theory；Pennington's bottom-up comprehension theory；Letovsky's knowledge-based understander model
- 自变量：application domain familiarity
- 中介：无/未明示
- 调节：无/未明示
- 因变量：program comprehension process (process score: hypotheses minus inferences)；number of hypotheses；number of inferences
- 主要发现：程序员在熟悉的应用领域中比在不熟悉的应用领域中使用了更自上而下的理解过程，表现为熟悉领域的平均过程得分更高（t=2.10, p<0.024）。这说明应用领域知识促使程序员更依赖假设驱动的理解策略。
- 人—智能体关系：仅人类参与者，无智能体介入；研究聚焦于程序员凭借自身知识和经验理解程序。
- 样本独立性：unclear
- 质量/限制：使用专业程序员作为参与者，口头协议经正式编码且评分者信度良好（Kappa=0.66）。局限：样本量较小（但为协议分析常见规模）；实验程序规模中等（但仍大于多数前代研究）；仅考察两个应用领域，未平衡会计和水利的熟悉度，可能限制推广性。

### 28. [Developing end-users' systems development competence](fulltext_candidates_local/19004_1993_developing-end-users-systems-development-competence.md)
- 年份：1993；来源：Information & Management；DOI：10.1016/0378-7206(93)90079-9
- 证据角色：primary_empirical；主体：human_only；制品：source_code；行动：write；generate；modify_or_refactor；test
- 编程情境定义：本文中，编程是指最终用户使用 iCASE 工具进行业务应用程序的原型设计、生成、测试和修改，最终构建可执行的信息系统，包括需求分析、概念建模、代码生成与迭代改进等活动。
- 任务与场景：在一个大型企业的零售部门，两个志愿者团队分别开发订单处理系统和分发管理信息系统，使用协作行动学习方法结合 iCASE 环境进行实际系统开发。
- 方法与分析层级：行动研究，通过两个案例研究探索 CAL 方法对最终用户系统开发能力的影响。；team
- 样本/数据：两个项目团队，每队 8 名志愿者（来自目录销售部门），共 16 人；数据来源于参与者日记、音频记录及会议记录。
- 理论/框架：Holographic Organization Theory；Action Learning Theory；Communicative Action Theory
- 自变量：无/未明示
- 中介：无/未明示
- 调节：无/未明示
- 因变量：无/未明示
- 主要发现：CAL 方法通过行动学习、沟通行动和自我组织团队结构，使最终用户在真实系统开发中发展了系统开发能力，尤其在克服技术沟通障碍、承担自主责任和掌握开发过程方面效果显著；用户普遍认为实际开发经验比传统案例学习更有效，协作结构和角色轮换加速了技能获取和组织学习。
- 人—智能体关系：无智能体参与，人类最终用户使用 iCASE 工具进行开发，工具仅作为辅助，无自主决策能力。
- 样本独立性：两个案例来自同一组织同一部门，但项目任务和团队成员独立，无证据表明样本重叠。
- 质量/限制：探索性案例研究，样本规模小且来自单一组织，结论的普遍性有限；数据主要基于参与者主观报告，缺少客观的编程能力或产品质量度量。

### 29. [On end-user computing productivity](fulltext_candidates_local/18768_1991_on-end-user-computing-productivity.md)
- 年份：1991；来源：Information & Management；DOI：10.1016/0378-7206(91)90067-c
- 证据角色：primary_empirical；主体：human_only；制品：source_code；行动：write
- 编程情境定义：该研究包含两个实验，其中编程实验要求参与者使用 BASIC 语言编写一个小程序，完成任务需使用顺序、选择和迭代三种基本结构。编程活动仅限于手工编写代码，不涉及测试或调试环节。数据库实验则针对命令级用户，不涉及编程，故不纳入编程行为。
- 任务与场景：受控实验在入门计算机/MIS课程的课堂中进行，参与者为商科学生，共83人。他们被随机分为四组，分别采用四种程序开发方法（流程图、伪代码、叙述性描述、直接编写）完成一个相同的编程任务，最终提交手写程序。
- 方法与分析层级：对照实验（controlled experiment），使用 ANOVA 比较组间差异。；individual
- 样本/数据：编程实验：83名被试，多为高年级商科学生，平均 GPA 2.65，平均修过 1.96 门计算机课程，多数有工作经验，具体人口统计学特征见表 1。数据收集包括程序质量评分、完成时间和人口统计学问卷。
- 理论/框架：无/未明示
- 自变量：program development method (flowchart, pseudocode, narrative, direct)
- 中介：无/未明示
- 调节：无/未明示
- 因变量：program accuracy；program structure；overall program quality；task completion time；productivity (quality/time)
- 主要发现：终端用户编写的程序质量普遍较低（平均正确率 2.27/5，结构度 2.17/5）。四种开发方法在程序正确性、结构性和整体质量上无统计显著差异。直接编写程序耗时最短（13.9 分钟），流程图耗时最长（18.9 分钟）。在生产力（质量/时间）上，伪代码和直接编写法显著优于其他两种方法。建议终端用户在处理小型程序时可采用伪代码以平衡质量与效率。
- 人—智能体关系：纯人类，无智能代理参与。
- 样本独立性：unclear
- 质量/限制：内部效度较高（对照实验），但外部效度有限：被试为学生，虽与目标终端用户特征相似，但任务规模小且为 BASIC 语言，推广至真实复杂场景需谨慎。评分存在主观性，已通过双人评分和仲裁缓解。研究发表于 1991 年，技术环境过时。

### 30. [An empirical study of users as application developers](fulltext_candidates_local/18163_1985_an-empirical-study-of-users-as-application-developers.md)
- 年份：1985；来源：Information & Management；DOI：10.1016/0378-7206(85)90037-0
- 证据角色：primary_empirical；主体：human_only；制品：low_code_or_visual；行动：write；debug_or_repair；test
- 编程情境定义：本文研究非DP专业人员（用户）使用第四代语言、应用生成器等工具自行开发行政型计算机应用（UDA）的活动。编程指用户亲自设计、编写、测试和调试可执行的应用程序。
- 任务与场景：在十家大型加拿大企业中，通过访谈和问卷调查，研究用户开发应用程序的特征、时间分配、技术背景、感知的优势与劣势、满意度等。任务涉及用户亲自开发小型管理应用，如报表、模型分析、事务处理等。
- 方法与分析层级：混合方法：首先通过结构化与非结构化访谈进行探索性研究，然后通过自编问卷对1074名用户进行调查，回收272份有效问卷。数据分析使用了判别分析、方差分析、描述性统计和重要性-满意度矩阵分析。；individual
- 样本/数据：来自10家大型加拿大企业的272名非DP专业人员（用户开发应用者），覆盖会计、财务、营销、工程等多个职能，职位包括分析师、主管、经理等。同时收集了DP经理的访谈资料。
- 理论/框架：无/未明示
- 自变量：user_type
- 中介：无/未明示
- 调节：无/未明示
- 因变量：productivity_improvement；perceived_advantages；satisfaction_with_UDA_aspects；time_spent_on_UDA_activities；application_development_time；user_background；disadvantages
- 主要发现：1. 根据开发原因和使用模式将用户分为三类：微型DP部门用户、参谋分析员和机会寻求者，他们在经验、时间分配和开发模式上存在显著差异。2. 用户开发的应用主要是报表准备（耗时最多）、简单查询、模型分析、事务处理、数据分析和图形。3. 用户认为UDA最大的优点是缩短了开发周期（及时性），其次是自己专业知识的直接运用和独立性；主要缺点是缺乏编程经验和软件工具使用困难。4. 满意度分析显示：用户对工具易用性、及时性、控制感和信息有用性高度满意且认为重要；对DP提供的咨询支持、响应时间、培训等方面既觉得重要又不满意。5. 生产率平均提高约5-6倍，但用户技能的局限、工具效率和控制问题仍是挑战。
- 人—智能体关系：无/不适用
- 样本独立性：未提及与其他研究复用样本，应为独立样本。
- 质量/限制：优点：多方法、多来源数据，提供了当时用户编程的全面图景。局限性：样本局限于大型加拿大公司，结果可能不适用于中小企业或其他文化背景；数据基于自我报告，可能存在回忆偏差；问卷回收率较低（40%响应，可用25%），虽经无响应偏差检验，但仍可能影响代表性。

## 全文排除论文

1. [Computer-aided model construction](fulltext_candidates_local/17316_1993_computer-aided-model-construction.md)（1993）：本文研究的是数学模型（尤其是数学规划模型）的计算机辅助构建，涉及建模语言（如GAMS、ASCEND）和知识基模型构建系统，但不涉及程序（如源代码、SQL查询、电子表格公式/脚本）的编写、生成、补全、理解、检查、调试、修改或测试。文中讨论的“模型构建”是指建立数学抽象和公式，而不是生成可执行程序。根据纳入标准，若把程序员和程序替换成一般知识工作者和一般工作产出后实际任务、操纵、测量和结论仍基本不变，则编程只是背景，应排除。本文核心是数学建模支持，不符合编程相关任务范围。
