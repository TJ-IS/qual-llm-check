# A strategic decision-making architecture toward hybrid teams for dynamic competitive problems

- 作者：Alparslan Emrah Bayrak; Christopher McComb; Jonathan Cagan; Kenneth Kotovsky
- 年份 / 期刊：2021 / Decision Support Systems
- DOI：10.1016/j.dss.2020.113490
- 源文件：19688_2021_a-strategic-decision-making-architecture-toward-hybrid-teams-for-dynamic-competitive-problems.md
- 论文主类型：build_evaluate_design_science
- 主导写作弧线：requirements_build_evaluate_design_principles
- 置信度：0.82

## 文章级论证概况

- 核心问题：如何设计一种面向动态竞争问题的人机混合团队战略决策架构，让计算机从历史数据中学习目标与策略，为人类提供战略建议，并系统化地将任务划分给计算机团队以提升整体决策质量。

- 制品与设计：论文提出一个集成序列学习（LSTM）、模型预测控制（MPC）和博弈论的自适应决策架构。核心设计包括：将DCP表示为战略/操作双层问题；用状态空间微分方程描述战略时间尺度系统动态；用k-means识别策略簇；为每个策略簇训练LSTM奖励模型；采用“开局建议+微分博弈自适应建议”两阶段决策流程；并提出人工、无监督、有监督三种任务划分方法来分配计算机团队中的子问题。

- 客观结果：在StarCraft II人族对抗数据上，博弈论建议对低水平玩家更有利，对高水平玩家偏保守；在对手水平未知时给出安全但次优的建议；相比单一计算机的all-in-one方案，计算机团队通过非直觉任务划分能显著提高战略决策质量；有监督划分在总不匹配指标上优于无监督和人工划分。

- 核心贡献：作者声称的主要贡献是首次提出一种面向动态竞争问题的自适应决策架构，整合序列学习、模型预测控制和博弈论；该架构使用经验数据而不依赖显式问题公式，可帮助人类进行战略决策；同时给出数据驱动的计算机团队任务划分方法，填补了混合团队中高层次战略支持和分工方法缺失的缺口。

- 整篇论证链：作者从人机协作和动态竞争问题的重要性出发，指出现有自动化多用于定义良好的操作任务，缺乏支持高层战略决策的系统方法。随后将问题形式化为战略/操作双层表示，用StarCraft II作为复杂DCP的代表平台。先用状态空间方程建模并验证系统动态，再用k-means识别多种策略，用LSTM从胜负数据学习每个策略簇的奖励模型，然后提出两阶段决策流程：开局阶段由人类从数据提取的开局策略中选择目标，自适应阶段通过MPC和微分博弈求解纳什均衡建议。由于all-in-one求解困难，作者进一步提出任务划分方法，比较人工、无监督和有监督三种划分，证明计算机团队的分区求解优于单机方案。讨论部分将计算发现提升为若干可复用设计知识，并明确其边界条件与未来人机实验需求。

## 类型与写作弧线判定

- 论文主类型判定：论文的核心是提出一个决策支持架构和配套方法，并通过StarCraft II算例进行构建与评价，最后在讨论中提炼设计知识。它不是以理论假说检验为主的实验研究，也不是标准基准竞赛型计算文章，而是典型的“需求—构建—评价—设计知识”设计科学研究。

- 主导写作弧线判定：全文叙事围绕DCP的需求特征展开，逐步构建数学模型、奖励学习、两阶段决策和任务划分，随后用计算实验评价，并在讨论中给出多条take-aways式的设计原则，符合“要求—构建—评价—设计原则”的写作弧线。

## 研究开展程序

- study_or_phase_count：6

- 研究阶段总序列：共六个阶段，呈链式积累：第一阶段建立数学建模和变量系统；第二阶段从数据中发现策略簇；第三阶段学习每个簇的奖励模型；第四阶段生成开局策略；第五阶段用微分博弈/MPC求解自适应建议；第六阶段将战略问题分区给计算机团队并证明其优势。每一阶段的输出都成为下一阶段的输入或评价基础。

### studies_or_phases

#### 1. 动态竞争问题建模与战略/操作双层表示

- order：1

- name_cn：动态竞争问题建模与战略/操作双层表示

- question_cn：如何将复杂DCP形式化，使计算机能在战略时间尺度上建模和学习？

- inputs_and_setting_cn：StarCraft II公开replay数据，通过游戏API提取86个状态变量和85个行动变量；人族对人族对局。

- designed_or_compared_object_cn：战略/操作双层问题表示；线性状态空间微分方程Eq.(1)及其系统矩阵A、B。

- baseline_control_or_counterfactual_cn：以实际游戏replay中的状态轨迹为参照，对比模型预测值；另对比有无时延处理的分析。

##### objective_metrics

1. 状态方程预测值与实际replay状态的吻合程度

2. 忽略时延在不同分析时间步长下的影响

- analysis_method_cn：图形对比验证，使用单一样本游戏状态（如supply）展示模型吻合度和时延影响。

- main_result_cn：线性模型在战略时间尺度上与实际数据基本吻合；在较大时间步长下忽略时延不构成重大问题。

- argumentative_role_cn：为整个架构提供数学语言和变量基础，使后续策略聚类、奖励学习和博弈优化有统一的状态/行动表示。

- remaining_uncertainty_cn：线性模型是简化，且未覆盖操作层细节；时延在秒级分析中明显但战略层可忽略。

- link_to_next_phase_cn：状态和行动变量成为策略聚类和奖励模型训练的输入。

##### evidence_pointers

1. Section 2.1 Eq.(1)

2. Table 1

3. Fig. 2

#### 2. 策略聚类：从经验数据中识别竞争策略

- order：2

- name_cn：策略聚类：从经验数据中识别竞争策略

- question_cn：在存在多种赢法的DCP中，如何结构化地识别人类玩家采用的不同策略？

- inputs_and_setting_cn：StarCraft II人族对局中双方至50%游戏进程的累积单位训练行动，形成策略对的向量。

- designed_or_compared_object_cn：用k-means对策略二元组进行聚类，并选取五个策略簇。

- baseline_control_or_counterfactual_cn：以簇数增加到五个以上后产生相似簇作为内部判据；无外部baseline。

##### objective_metrics

1. 聚类簇数可解释性

2. 簇内策略差异（进攻型/防守型等）

- analysis_method_cn：k-means聚类和单位构成分布图观察。

- main_result_cn：识别出五个不同的策略簇，包含以Marines为主的进攻策略和以SCVs为主的防守策略等。

- argumentative_role_cn：体现DCP中不存在单一最优策略，为后续按策略簇分别建模和提供建议奠定基础。

- remaining_uncertainty_cn：簇数和表示方式依赖专家判断，且聚类只代表中期状态，胜负差异可能发生在后半程。

- link_to_next_phase_cn：每个策略簇将单独训练一个奖励模型，以适应不同策略的目标差异。

##### evidence_pointers

1. Section 2.2

2. Fig. 3

#### 3. 数据驱动奖励模型：LSTM学习目标函数

- order：3

- name_cn：数据驱动奖励模型：LSTM学习目标函数

- question_cn：当DCP没有显式目标函数时，如何从历史对局数据中学习可评估决策质量的奖励函数？

- inputs_and_setting_cn：归一化的状态变量和胜负标签；为处理平局加入合成数据；通过镜像数据强化零和对称性。

- designed_or_compared_object_cn：以指数反向传播函数Eq.(2)作为奖励参考；对每个策略簇训练LSTM网络；用两个LSTM输出的差构造严格对称的奖励Eq.(3)。

- baseline_control_or_counterfactual_cn：训练输出与胜负/平局三类标签对比；参考指数奖励曲线作为监督信号。

##### objective_metrics

1. 模型对胜负/平局数据的区分能力

2. 连续输出能否表示期望获胜程度

- analysis_method_cn：LSTM回归训练，展示分类和回归趋势。

- main_result_cn：奖励模型能清晰区分胜者、败者和合成平局数据，并可输出连续的预期获胜程度。

- argumentative_role_cn：将经验数据转化为可优化的目标函数，是后续微分博弈问题的核心输入。

- remaining_uncertainty_cn：LSTM只是近似学习；合成平局和镜像对称只能改善而不能保证完全准确；未在真实时间上验证。

- link_to_next_phase_cn：奖励模型直接作为Eq.(4)中目标函数进入模型预测控制求解。

##### evidence_pointers

1. Section 2.3 Eq.(2)(3)

2. Fig. 4

#### 4. 开局策略提取：非自适应的初始建议阶段

- order：4

- name_cn：开局策略提取：非自适应的初始建议阶段

- question_cn：在对手信息不足的初始阶段，如何给人类提供可选择的、来自经验数据的开局战略建议？

- inputs_and_setting_cn：从策略簇聚类结果中按等间隔游戏进程采样累积决策，取每簇质心作为开局建议。

- designed_or_compared_object_cn：设计分阶段的目标建议序列，并指出建议需语义标签以便人类选择。

- baseline_control_or_counterfactual_cn：无直接对照；以策略簇质心作为经验基线，并讨论使用全行动向量的替代方案。

##### objective_metrics

1. 能否形成分阶段可执行的目标序列

2. 示例开局策略的可解释性

- analysis_method_cn：质心采样和阶段目标定义，仅做定性展示。

- main_result_cn：生成了如Strategy Cluster 2的分阶段目标建议，例如构建特定数量单位的阶段性目标。

- argumentative_role_cn：构成两阶段决策架构中的非自适应开局阶段，让人类在数据驱动的备选方案中做出初始选择。

- remaining_uncertainty_cn：没有人类被试验证；语义标签和认知负荷影响未测。

- link_to_next_phase_cn：开局目标完成后系统进入基于微分博弈的自适应建议阶段。

##### evidence_pointers

1. Section 3.1

2. Fig. 5

#### 5. 自适应博弈决策：模型预测控制与纳什均衡求解

- order：5

- name_cn：自适应博弈决策：模型预测控制与纳什均衡求解

- question_cn：在观察到对手状态后，如何用反馈控制方式给出博弈论战略建议？

- inputs_and_setting_cn：Strategy Cluster 2的实际对局数据；系统模型Eq.(1)和奖励模型；MPC预测窗口为3个时间步。

- designed_or_compared_object_cn：用Eq.(4)的微分博弈公式，通过迭代松弛和遗传算法求解纳什均衡；对比博弈建议与实际人类玩家决策。

- baseline_control_or_counterfactual_cn：同一game state下的人类实际决策和实际奖励；all-in-one非分区求解作为后续分区的总基线。

##### objective_metrics

1. 博弈建议奖励与实际玩家奖励的逐时间步比较

2. 胜者/败者获得的均衡奖励差异

3. 纳什均衡迭代收敛步数

- analysis_method_cn：模型预测控制滚动求解；遗传算法种群规模1000、250代、5次迭代收敛；图6展示均值和标准误。

- main_result_cn：均衡解在平均意义上比实际玩家奖励更平衡，对败者更高、对胜者更低；表明对高水平玩家可能过于保守，但对低水平玩家和未知对手情境提供安全建议。

- argumentative_role_cn：证明自适应建议机制能在经验数据基础上产生可解释、保守但合理的博弈论战略建议。

- remaining_uncertainty_cn：计算开销大，只能离线求解；没有真人跟随实验；均衡解依赖所学习奖励函数和有限预测窗口。

- link_to_next_phase_cn：all-in-one求解在大规模空间中的局限引出分区求解的必要性。

##### evidence_pointers

1. Section 3.2 Eq.(4)

2. Fig. 6

#### 6. 分区问题求解：计算机团队的任务划分与协调

- order：6

- name_cn：分区问题求解：计算机团队的任务划分与协调

- question_cn：当单一决策者无法高效求解大规模战略问题时，应如何在计算机团队中划分任务以最大化团队表现？

- inputs_and_setting_cn：每个策略簇内的行动/状态变量；经验数据；三种划分方法：人工语义划分、基于相关性的k-medoids无监督划分、基于奖励模型错位的有监督划分。

- designed_or_compared_object_cn：定义任务分区变量组；用顺序协调策略串联各子问题求解结果；构造总错位目标Eq.(5)并用PSO求解。

- baseline_control_or_counterfactual_cn：all-in-one非分区求解作为总体基线；人工语义划分作为分区基线；另比较无监督与有监督划分。

##### objective_metrics

1. 总错位（misalignment）

2. 胜者玩家的最优奖励

3. 不同分区方法的变量分布模式

- analysis_method_cn：优化问题求解与图8对比；在固定对手为Nash解的条件下检验分区方案提高胜者奖励的空间。

- main_result_cn：有监督分区在总错位上显著优于人工和无监督划分；无监督和有监督分区在决策质量上都优于all-in-one和人工划分；分区模式是非直观的。

- argumentative_role_cn：为混合团队中的计算机团队提供系统的分工方法，并将其优势归因于大规模空间中的更有效搜索。

- remaining_uncertainty_cn：协调策略简单顺序式，不保证全局最优；未测试人类任务划分；未做人机实时实验。

- link_to_next_phase_cn：结果为讨论部分“计算机团队优于单一元规划器”和“非直观任务划分”的设计知识提供直接证据。

##### evidence_pointers

1. Section 4 Eq.(5)

2. Fig. 7

3. Fig. 8a/b

## 各部分修辞架构

### abstract_moves

1. CONTEXT — 指出AI进步带来人机混合团队的新机会

2. RQ_OR_OBJECTIVE — 提出本文的决策架构目标

3. DESIGN_FEATURE — 描述集成方法和技术路线

4. STUDY_OVERVIEW — 说明在StarCraft II上的应用

5. RESULT — 报告低水平玩家受益、高水平玩家保守和安全建议等结果

6. CONTRIBUTION — 隐含人机协作架构与任务划分方法的贡献

### introduction_moves

1. CONTEXT — 建立人机协作和复杂问题背景

2. PRIOR_KNOWLEDGE — 回顾Fitts List和决策支持系统

3. LIMITATION — 指出传统自动化面向操作层、定义良好的任务

4. GAP — 指出高层战略决策支持与分工方法未被研究

5. PHENOMENON — 描述DCP的实例和属性

6. REQUIREMENT — 提出连续决策、对抗、适应性和双层表示等需求

7. THEORY_INTRO — 引入微分博弈、MPC、序列学习等方法

8. BOUNDARY_CONDITION — 说明不建模人类响应和未来真人实验

### theory_and_knowledge_moves

1. THEORY_INTRO — 微分博弈是控制与博弈论的结合

2. LIMITATION — LQR假设强、动态规划不可扩展

3. PRIOR_KNOWLEDGE — 人机团队可行性相关研究

4. GAP — 缺乏学习与适应能力的系统方法

5. THEORY_PROPOSITION — 正确设计的混合团队可产生更稳健决策

6. MECHANISM — 策略簇切换和状态反馈两种适应机制

### artifact_design_moves

1. REQUIREMENT — 战略/操作分离以管理复杂度

2. DESIGN_FEATURE — 状态空间微分方程模型

3. DESIGN_FEATURE — k-means策略聚类

4. DESIGN_FEATURE — LSTM奖励模型及合成/镜像数据

5. DESIGN_FEATURE — 两阶段决策流程

6. DESIGN_FEATURE — 三种任务划分方法和顺序协调

### evaluation_moves

1. BENCHMARK_OR_CONTRAST — 实际replay验证模型

2. RESULT — LSTM区分胜负/平局

3. RESULT — 博弈建议对败者/胜者的奖励差异

4. BENCHMARK_OR_CONTRAST — all-in-one与人工划分为基线

5. RESULT — 分区方法在错位和胜者奖励上优于基线

### discussion_and_contribution_moves

1. CONTRIBUTION — 战略/操作分离有利于复杂问题管理

2. MECHANISM — 两类适应机制

3. CONTRIBUTION — 架构缓解博弈论保守性

4. CONTRIBUTION — 计算机团队优于单一计算机

5. DESIGN_KNOWLEDGE — 计算机团队偏好非直觉任务划分

6. BOUNDARY_CONDITION — 数据质量、策略多样性和领域可迁移性

## 理论/知识到设计的翻译

### 知识/理论基础

1. 微分博弈理论（differential games）

2. 模型预测控制（MPC）

3. 序列学习（LSTM/RNN）

4. 博弈论与纳什均衡

5. 运筹学/系统工程中的多时间尺度决策分层

6. 分解式设计优化与任务分配（DSM/functional dependency）

7. 人机功能分配与自动化文献（Fitts List）

- 理论—设计耦合：direct

- 耦合判定理由：架构的核心元素直接由微分博弈、模型预测控制和序列学习等知识基础决定：双层表示来自多时间尺度决策文献，奖励模型来自序列学习，博弈建议来自MPC和微分博弈，任务划分来自分解式设计优化。评价也直接检验这些设计元素的计算效果。

- 理论到设计翻译链：DCP的连续动态与对抗特征 → 用双层表示和状态空间方程建模；缺乏显式目标 → 用LSTM从胜负数据学习奖励函数；竞争均衡 → 用微分博弈/MPC求解纳什均衡建议；大规模求解困难 → 用任务划分和顺序协调组织计算机团队。

### mapping_table

#### 1. 1

- theory_or_knowledge_claim_cn：微分博弈理论认为竞争动态系统的均衡可在连续时间动态背景下求解，但经典解析方法受限于简单系统。

- mechanism_cn：将对抗决策建模为双方动态博弈；用有限时域滚动优化逼近均衡。

- design_requirement_cn：需要在战略时间尺度上有可预测的状态空间模型和一个可优化的目标函数。

- artifact_choice_cn：Eq.(1)线性状态空间模型；Eq.(4)微分博弈MPC公式；迭代松弛+遗传算法求解。

- evaluated_contrast_cn：在相同game state下，博弈建议奖励与实际人类玩家奖励对比。

- objective_result_cn：均衡解在平均意义上更平衡：对败者奖励更高、对胜者奖励更低；对高水平玩家保守。

##### evidence_pointers

1. Section 3.2

2. Fig. 6

#### 2. 2

- theory_or_knowledge_claim_cn：序列学习模型能捕捉时间序列中的长期依赖；逆强化学习的“数据最优”假设在包含非专家的数据中不成立。

- mechanism_cn：从历史胜负序列中学习状态到期望收益的非线性映射，并用指数反向传播塑形。

- design_requirement_cn：在无显式目标时，需要用经验数据构建可作为优化目标的奖励函数。

- artifact_choice_cn：每策略簇LSTM奖励模型；指数反向传播Eq.(2)；合成平局数据；镜像对称Eq.(3)。

- evaluated_contrast_cn：训练输出与胜负/平局类别标签和参考指数曲线对比。

- objective_result_cn：模型能区分三类数据，并输出连续期望获胜程度。

##### evidence_pointers

1. Section 2.3

2. Fig. 4

#### 3. 3

- theory_or_knowledge_claim_cn：在零和博弈中，Nash均衡要求任何一方都不能单方面改进。

- mechanism_cn：用min-max嵌套优化表达一方最优响应依赖对方最优响应，实现保守最优。

- design_requirement_cn：建议应当考虑对手做出最优决策的可能性，而非假设对手非理性。

- artifact_choice_cn：Eq.(4)中的嵌套优化和迭代松弛方法。

- evaluated_contrast_cn：Nash解与实际非理性玩家决策对比。

- objective_result_cn：对低水平玩家提供更高奖励路径，对高水平玩家过于保守；在未知对手情形下提供安全建议。

##### evidence_pointers

1. Section 3.2

2. Fig. 6

#### 4. 4

- theory_or_knowledge_claim_cn：分解式设计优化和任务分配文献认为，问题划分和协调策略会影响整体性能；但现有方法针对显式目标函数。

- mechanism_cn：将耦合决策变量分组，分组后顺序协调，可在大规模空间中更高效搜索。

- design_requirement_cn：黑箱目标下仍需系统化、可优化的问题划分。

- artifact_choice_cn：人工语义划分、基于相关性的无监督k-medoids划分、基于错位目标的有监督划分；顺序协调。

- evaluated_contrast_cn：三种分区方案与all-in-one及人工划分基线对比。

- objective_result_cn：有监督划分最小化总错位；无监督和有监督分区均显著提升胜者奖励，且划分模式非直观。

##### evidence_pointers

1. Section 4

2. Fig. 7

3. Fig. 8a/b

#### 5. 5

- theory_or_knowledge_claim_cn：人机功能分配理论（Fitts List）认为人和机器具有互补能力。

- mechanism_cn：计算机负责战略层建议，人类保留最终决策权并负责操作层执行。

- design_requirement_cn：建议应可被人类接受或忽略，而非自动执行。

- artifact_choice_cn：两阶段建议架构：开局策略选择和微分博弈自适应建议。

- evaluated_contrast_cn：当前仅在计算层验证，无真人参与者对比。

- objective_result_cn：计算结果显示建议安全但保守，讨论中主张最终决策应由人类评估。

##### evidence_pointers

1. Section 1.2-1.3

2. Section 3

3. Section 5

## 评价逻辑

### evaluation_modes

1. 状态空间模型的replay数据验证

2. k-means策略聚类的可解释性评估

3. LSTM奖励模型的训练与预测对比

4. 微分博弈Nash解与人类实际决策的计算对比

5. 任务划分方法与all-in-one/manual基线的对比

- why_these_evaluations_cn：由于文章没有真人参与实验，作者采用逐层计算验证来建立可信度：先确保数学模型与数据一致，再确保策略识别和奖励学习有效，再比较博弈建议与真实决策，最后比较分区方案与基线。每一层都为下一层提供可信输入。

- benchmark_and_contrast_chain_cn：先从实际replay验证系统模型；然后以胜负/平局标签验证奖励模型；再用同一game state下的人类实际决策作为博弈建议的参照；最后以all-in-one为总体基线和人工语义划分为分区基线，依次展示无监督和有监督分区的优势。

### claim_evidence_ledger

#### 1. 架构能从经验数据中学习战略目标。

- claim_cn：架构能从经验数据中学习战略目标。

- evidence_cn：Section 2.3 LSTM训练结果，Fig. 4。

- assessment_cn：支持：模型能区分胜负/平局，并输出连续预期获胜程度。

#### 2. 博弈论建议对低水平玩家更有利、对高水平玩家保守。

- claim_cn：博弈论建议对低水平玩家更有利、对高水平玩家保守。

- evidence_cn：Section 3.2 Fig. 6中的平均奖励对比。

- assessment_cn：部分支持：该结论基于计算对比，而非实际人类水平测验。

#### 3. 任务划分显著提升决策质量，优于all-in-one。

- claim_cn：任务划分显著提升决策质量，优于all-in-one。

- evidence_cn：Section 4 Fig. 8b的胜者奖励对比。

- assessment_cn：支持：但仅在固定对手为Nash解、顺序协调和特定策略簇条件下验证。

#### 4. 计算机团队偏好非直观任务划分。

- claim_cn：计算机团队偏好非直观任务划分。

- evidence_cn：Section 4 Fig. 7中无监督和有监督划分模式与语义划分明显不同，且绩效更好。

- assessment_cn：间接支持：模式差异与绩效提升相关，但未系统解释机制。

#### 5. 人机混合团队可行。

- claim_cn：人机混合团队可行。

- evidence_cn：没有真人参与实验，仅有架构描述和计算演示。

- assessment_cn：未直接验证：作者也承认human-in-the-loop留待未来工作。

- internal_validity_strategy_cn：通过输入归一化、合成平局数据、镜像对称、统一时间步长、固定对手为Nash解的比较设计、遗传算法种子继承等方式，减少外部变量和求解随机性对结论的干扰。

- external_validity_strategy_cn：采用StarCraft II作为复杂DCP代表，强调方法层面不依赖具体游戏机制，因此可迁移到军事、工程管理等领域；但未做跨域验证。

- what_is_not_actually_tested_cn：未测试真人决策者是否遵循建议；未测试实际实时性能；未测试认知负荷和信任等人因变量；未在StarCraft II之外的其他DCP上验证泛化性；未系统检验不同协调策略下的分区优势。

## 贡献闭环

- technical_claim_cn：构建了一个整合LSTM、MPC和博弈论的自适应战略决策架构，能够从历史对局数据中学习目标函数并产生战略建议；同时提出数据驱动的任务划分方法。

- artifact_claim_cn：架构中的各设计元素——策略聚类、奖励模型、开局策略、自适应博弈建议和任务划分——均在计算实验中产生可检验的效果，尤其是分区求解比all-in-one更优。

- mechanism_claim_cn：计算机通过按策略簇切换奖励模型和状态反馈的微分博弈求解来适应对手策略变化；博弈论最优响应假设使建议具有保守但安全的特性；任务划分通过更有效的搜索空间遍历提升团队绩效。

- boundary_claim_cn：方法对低水平玩家提供有效指导，对高水平玩家可能过于保守；在对手水平未知时提供安全但次优建议；在战略/操作可分离且历史数据可获得的问题中适用。

- reusable_design_knowledge_cn：可复用知识包括：多时间尺度分离以管理复杂性；按策略簇学习奖励；采用“开局策略+自适应博弈”两阶段决策；对大问题使用计算机团队而非单一元规划器；任务划分应先尝试无监督方法，不满意再用有监督方法；计算机团队可能偏好非直观任务划分。

- theoretical_contribution_cn：将微分博弈、模型预测控制和序列学习整合到人机协作决策支持中，并以经验数据替代显式目标函数；扩展了自动化支持从操作层到战略层的讨论；未提出新的行为理论，而是建立了方法框架。

- how_discussion_closes_intro_gap_cn：讨论部分的五个主要take-aways分别回应引言中“缺乏高层战略支持”、“缺乏学习/适应能力”、“缺乏划分系统方法”等缺口：战略/操作分离、两类适应机制、架构缓解博弈论局限、计算机团队优于单机、非直观划分。

- overclaim_or_unsupported_leaps_cn：人机协作的实际价值在无人被试情况下主要由架构推断；低水平/高水平玩家的结论来自计算数据而非真实玩家表现；分区优势可能依赖顺序协调和Nash固定对手等特定条件；将StarCraft II结果推广到其他DCP仍需更多验证。

## 句级写作动作图谱

### 1. Abstract P1

- order：1

- section：Abstract

- locator：Abstract P1

- move_code：CONTEXT

- paraphrase_cn：AI进步为计算机在混合团队中作为同伴支持人类解决复杂问题创造了新机会。

- rhetorical_function_cn：开篇建立研究背景和现实意义。

- depends_on_cn：无

- sets_up_cn：为提出本文架构提供动机。

- evidence_pointer：Abstract P1

### 2. Abstract P2

- order：2

- section：Abstract

- locator：Abstract P2

- move_code：RQ_OR_OBJECTIVE

- paraphrase_cn：本文提出一个用于动态环境中大规模竞争问题的人机协作自适应决策架构。

- rhetorical_function_cn：明确本文目标。

- depends_on_cn：背景句

- sets_up_cn：引出集成方法和技术路线。

- evidence_pointer：Abstract P2

### 3. Abstract P3

- order：3

- section：Abstract

- locator：Abstract P3

- move_code：DESIGN_FEATURE

- paraphrase_cn：架构整合序列学习、模型预测控制和博弈论，并包含数据驱动的计算机团队任务划分方法。

- rhetorical_function_cn：概括核心设计要素。

- depends_on_cn：目标句

- sets_up_cn：为后续各章结构提供预览。

- evidence_pointer：Abstract P3

### 4. Abstract P4

- order：4

- section：Abstract

- locator：Abstract P4

- move_code：STUDY_OVERVIEW

- paraphrase_cn：该通用方法在即时战略游戏StarCraft II上进行说明。

- rhetorical_function_cn：说明应用平台和评价场景。

- depends_on_cn：方法叙述

- sets_up_cn：为结果句提供领域背景。

- evidence_pointer：Abstract P4

### 5. Abstract P5-P6

- order：5

- section：Abstract

- locator：Abstract P5-P6

- move_code：RESULT

- paraphrase_cn：结果显示低水平玩家可以从博弈论支持中受益，高水平玩家可能觉得建议过于保守；面对未知水平对手时建议安全但次优；计算机团队的非直觉任务划分显著提升决策质量。

- rhetorical_function_cn：报告核心发现。

- depends_on_cn：方法与应用平台

- sets_up_cn：为读者提供本文价值主张。

- evidence_pointer：Abstract P5-P6

### 6. Introduction P1 S1

- order：6

- section：Introduction

- locator：Introduction P1 S1

- move_code：CONTEXT

- paraphrase_cn：人机协作因能扩展人类决策者处理复杂工程系统管理和军事行动等问题的能力而受到关注。

- rhetorical_function_cn：建立广泛现实背景。

- depends_on_cn：无

- sets_up_cn：引出团队协作和自动化支持的主题。

- evidence_pointer：Introduction P1 S1

### 7. Introduction P1 S2-S3

- order：7

- section：Introduction

- locator：Introduction P1 S2-S3

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：有效团队协作对超出单个决策者能力的大规模问题至关重要；自动支持人类决策可追溯到1950年代的Fitts List。

- rhetorical_function_cn：回顾人机功能分配的历史知识。

- depends_on_cn：背景句

- sets_up_cn：说明人机协作不是新问题，但存在新的ML机会。

- evidence_pointer：Introduction P1 S2-S3

### 8. Introduction P1 S4-S5

- order：8

- section：Introduction

- locator：Introduction P1 S4-S5

- move_code：CONTEXT

- paraphrase_cn：机器学习使计算机能从大数据中提取知识，这是早期自动化系统缺乏的能力，因此可以增强人类在开放和病态定义问题中的直觉。

- rhetorical_function_cn：强调新时代条件变化。

- depends_on_cn：Fitts List背景

- sets_up_cn：为“高层战略支持”新视角做铺垫。

- evidence_pointer：Introduction P1 S4-S5

### 9. Introduction P2 S1

- order：9

- section：Introduction

- locator：Introduction P2 S1

- move_code：HYPOTHESIS_OR_PROPOSITION

- paraphrase_cn：作者提出，设计良好的混合团队可以比人或计算机单独做出更稳健的决策。

- rhetorical_function_cn：给出全文的核心假设/命题。

- depends_on_cn：ML能力背景

- sets_up_cn：后面所有设计都服务于这个命题。

- evidence_pointer：Introduction P2 S1

### 10. Introduction P2 S2-S3

- order：10

- section：Introduction

- locator：Introduction P2 S2-S3

- move_code：GAP

- paraphrase_cn：以往研究多让计算机执行定义良好的重复性操作任务；本文提出一个文献中尚未研究的新视角：让计算机在更高层战略决策中与人类协作。

- rhetorical_function_cn：构造研究缺口。

- depends_on_cn：现有自动化文献

- sets_up_cn：引出本文独特贡献。

- evidence_pointer：Introduction P2 S2-S3

### 11. Introduction P3 S1

- order：11

- section：Introduction

- locator：Introduction P3 S1

- move_code：PHENOMENON

- paraphrase_cn：本文聚焦于高复杂度的动态竞争问题，实例包括生命周期内的工程系统运营管理和军事小队对抗决策。

- rhetorical_function_cn：定义问题类别并给出现实事例。

- depends_on_cn：研究缺口句

- sets_up_cn：为形式化DCP提供现象基础。

- evidence_pointer：Introduction P3 S1

### 12. Introduction P3 S2

- order：12

- section：Introduction

- locator：Introduction P3 S2

- move_code：REQUIREMENT

- paraphrase_cn：DCP具有两个特征：环境动态变化下的连续决策，以及面对对手的竞争。

- rhetorical_function_cn：提炼DCP的必要条件。

- depends_on_cn：现象句

- sets_up_cn：推理出适应性和对抗性需求。

- evidence_pointer：Introduction P3 S2

### 13. Introduction P3 S3

- order：13

- section：Introduction

- locator：Introduction P3 S3

- move_code：MECHANISM

- paraphrase_cn：有效反击对手策略并适应问题变化是成功决策的关键。

- rhetorical_function_cn：说明为什么DCP需要适应机制。

- depends_on_cn：DCP属性

- sets_up_cn：为两阶段适应架构提供理由。

- evidence_pointer：Introduction P3 S3

### 14. Introduction P3 S4

- order：14

- section：Introduction

- locator：Introduction P3 S4

- move_code：LIMITATION

- paraphrase_cn：问题不确定性、目标不明确、决策空间高维和时变特征使DCP难以被单一数学模型和现有AI处理。

- rhetorical_function_cn：指出问题困难所在。

- depends_on_cn：DCP属性

- sets_up_cn：引出双层表示和混合团队的必要性。

- evidence_pointer：Introduction P3 S4

### 15. Introduction P4 S1

- order：15

- section：Introduction

- locator：Introduction P4 S1

- move_code：REQUIREMENT

- paraphrase_cn：本文通过分离短期操作决策和长期战略决策的双层问题表示来应对这些挑战。

- rhetorical_function_cn：提出解决问题的总体设计原则。

- depends_on_cn：DCP困难

- sets_up_cn：为后续建模和架构提供主线。

- evidence_pointer：Introduction P4 S1

### 16. Introduction P5 S1

- order：16

- section：Introduction

- locator：Introduction P5 S1

- move_code：DESIGN_FEATURE

- paraphrase_cn：本文提出一个自适应决策过程，整合序列学习、模型预测控制和博弈论。

- rhetorical_function_cn：点明架构的方法组合。

- depends_on_cn：双层表示原则

- sets_up_cn：为后面具体模块提供方法地图。

- evidence_pointer：Introduction P5 S1

### 17. Introduction P6 S1

- order：17

- section：Introduction

- locator：Introduction P6 S1

- move_code：BOUNDARY_CONDITION

- paraphrase_cn：本文不假设人类会遵循计算机所有建议，真人参与验证留待未来。

- rhetorical_function_cn：限定研究边界。

- depends_on_cn：混合团队视角

- sets_up_cn：防止读者将计算演示误认为真人实验结论。

- evidence_pointer：Introduction P6 S1

### 18. Section 1.1 P1

- order：18

- section：Introduction 1.1

- locator：Section 1.1 P1

- move_code：THEORY_INTRO

- paraphrase_cn：微分博弈将控制理论与博弈论结合，用于分析动态系统中的对抗和均衡。

- rhetorical_function_cn：引入理论基础。

- depends_on_cn：DCP需求

- sets_up_cn：为自适应建议阶段提供形式化工具。

- evidence_pointer：Section 1.1 P1

### 19. Section 1.1 P2

- order：19

- section：Introduction 1.1

- locator：Section 1.1 P2

- move_code：LIMITATION

- paraphrase_cn：既有规范方法使用线性二次调节器和动态规划，前者假设过强，后者难以扩展到高维系统。

- rhetorical_function_cn：指出经典微分博弈求解方法的不足。

- depends_on_cn：微分博弈理论

- sets_up_cn：为本文采用MPC和序列学习提供动机。

- evidence_pointer：Section 1.1 P2

### 20. Section 1.2 P1

- order：20

- section：Introduction 1.2

- locator：Section 1.2 P1

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：已有研究表明可以用计算机模拟人类问题解决过程，也可以用计算机代理替换无人机协调中的人类成员。

- rhetorical_function_cn：说明人机团队可行性。

- depends_on_cn：人机协作背景

- sets_up_cn：将讨论推进到“缺乏学习/适应”缺口。

- evidence_pointer：Section 1.2 P1

### 21. Section 1.2 P2

- order：21

- section：Introduction 1.2

- locator：Section 1.2 P2

- move_code：GAP

- paraphrase_cn：现有文献多关注自动化而忽略ML带来的学习与适应能力；在动态竞争和长短周期决策中，系统化开发自适应计算机代理和分工方法仍未研究。

- rhetorical_function_cn：明确双重研究缺口。

- depends_on_cn：人机协作文献回顾

- sets_up_cn：为贡献陈述提供靶心。

- evidence_pointer：Section 1.2 P2

### 22. Section 1.3 P1

- order：22

- section：Introduction 1.3

- locator：Section 1.3 P1

- move_code：CONTRIBUTION

- paraphrase_cn：主要贡献是提出基于序列学习、MPC和博弈论的自适应决策架构，支持DCP中的人机协作，并用StarCraft II演示。

- rhetorical_function_cn：正式声明贡献。

- depends_on_cn：GAP句

- sets_up_cn：为整篇论文的章节安排提供纲领。

- evidence_pointer：Section 1.3 P1

### 23. Section 2 P1

- order：23

- section：Section 2

- locator：Section 2 P1

- move_code：REQUIREMENT

- paraphrase_cn：DCP需要基于系统整体动态和对手潜在决策做出自适应决策。

- rhetorical_function_cn：从模型层面重申问题需求。

- depends_on_cn：Introduction中的DCP定义

- sets_up_cn：引出状态空间建模。

- evidence_pointer：Section 2 P1

### 24. Section 2 P2

- order：24

- section：Section 2

- locator：Section 2 P2

- move_code：LIMITATION

- paraphrase_cn：DCP不能像棋类那样离散化为决策树，因为所有各方都必须连续决策。

- rhetorical_function_cn：排除经典博弈建模路径。

- depends_on_cn：DCP连续动态属性

- sets_up_cn：为微分博弈和MPC腾出空间。

- evidence_pointer：Section 2 P2

### 25. Section 2 P4

- order：25

- section：Section 2

- locator：Section 2 P4

- move_code：STUDY_OVERVIEW

- paraphrase_cn：本文用StarCraft II作为复杂DCP应用平台，研究对称零和动态竞争。

- rhetorical_function_cn：引入应用平台并说明选择理由。

- depends_on_cn：DCP建模需求

- sets_up_cn：为数据、变量和后续实验限定场景。

- evidence_pointer：Section 2 P4

### 26. Section 2 P6

- order：26

- section：Section 2

- locator：Section 2 P6

- move_code：LIMITATION

- paraphrase_cn：常见AI方法将StarCraft拆成子问题，但缺乏集成方法时无法解决整体问题；现有AI最多达到业余水平。

- rhetorical_function_cn：指出替代技术路线的不足。

- depends_on_cn：StarCraft复杂度描述

- sets_up_cn：为“与人类协作”而非替代人类提供动机。

- evidence_pointer：Section 2 P6

### 27. Section 2 P7

- order：27

- section：Section 2

- locator：Section 2 P7

- move_code：RQ_OR_OBJECTIVE

- paraphrase_cn：本文不试图用计算机替代人类，而是开发计算机协作决策过程。

- rhetorical_function_cn：明确研究取向。

- depends_on_cn：AI方法局限

- sets_up_cn：引出战略/操作分离和混合团队架构。

- evidence_pointer：Section 2 P7

### 28. Section 2.1 P4-P5

- order：28

- section：Section 2.1

- locator：Section 2.1 P4-P5

- move_code：DESIGN_FEATURE

- paraphrase_cn：StarCraft II中战略行动分为四类：采集资源、建造单位/建筑、升级、派兵进攻/防守；相应状态变量表示资源量、单位/建筑数、升级状态和进攻/防守单位数。

- rhetorical_function_cn：将抽象战略/操作分离映射到具体变量。

- depends_on_cn：战略/操作双层表示

- sets_up_cn：为状态空间方程提供变量。

- evidence_pointer：Section 2.1 P4-P5

### 29. Section 2.1 P6-P7

- order：29

- section：Section 2.1

- locator：Section 2.1 P6-P7

- move_code：DESIGN_FEATURE

- paraphrase_cn：系统动态用线性状态空间微分方程Eq.(1)表示，系统矩阵A和B由游戏机制构建。

- rhetorical_function_cn：给出核心数学模型。

- depends_on_cn：变量定义

- sets_up_cn：该模型成为后续MPC问题约束。

- evidence_pointer：Section 2.1 Eq.(1)

### 30. Section 2.1 P10

- order：30

- section：Section 2.1

- locator：Section 2.1 P10

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：使用公开游戏数据验证系统模型，并通过后处理提取状态/行动变量，对时间和变量做归一化。

- rhetorical_function_cn：说明数据来源和预处理合理性。

- depends_on_cn：状态空间模型

- sets_up_cn：为图2模型验证提供方法和数据。

- evidence_pointer：Section 2.1 P10

### 31. Fig. 2附近段落

- order：31

- section：Section 2.1

- locator：Fig. 2附近段落

- move_code：RESULT

- paraphrase_cn：模型预测的供应状态与实际游戏数据一致；忽略时延在战略时间尺度上影响很小。

- rhetorical_function_cn：展示建模有效性。

- depends_on_cn：模型和数据

- sets_up_cn：为后续使用该模型求解提供信心。

- evidence_pointer：Fig. 2

### 32. Section 2.2 P1

- order：32

- section：Section 2.2

- locator：Section 2.2 P1

- move_code：REQUIREMENT

- paraphrase_cn：现实中单一策略很难击败所有对手，识别多种策略是竞争问题成功的关键。

- rhetorical_function_cn：引出策略聚类需求。

- depends_on_cn：DCP多策略现实

- sets_up_cn：为k-means聚类提供逻辑。

- evidence_pointer：Section 2.2 P1

### 33. Section 2.2 P3

- order：33

- section：Section 2.2

- locator：Section 2.2 P3

- move_code：DESIGN_FEATURE

- paraphrase_cn：用50%游戏进程前的累积单位行动进行k-means聚类，识别出五个策略簇。

- rhetorical_function_cn：给出具体聚类设计。

- depends_on_cn：策略多样性需求

- sets_up_cn：为每个策略簇训练奖励模型。

- evidence_pointer：Section 2.2 P3, Fig. 3

### 34. Section 2.3 P1

- order：34

- section：Section 2.3

- locator：Section 2.3 P1

- move_code：REQUIREMENT

- paraphrase_cn：DCP需要奖励函数来评估潜在决策，但许多现实问题没有显式目标。

- rhetorical_function_cn：说明构造奖励模型的必要性。

- depends_on_cn：DCP目标不明确

- sets_up_cn：引出数据驱动奖励学习。

- evidence_pointer：Section 2.3 P1

### 35. Section 2.3 P2

- order：35

- section：Section 2.3

- locator：Section 2.3 P2

- move_code：DESIGN_FEATURE

- paraphrase_cn：以胜负为1/-1并用指数函数向开局方向反传，形成随游戏进程变化的奖励函数。

- rhetorical_function_cn：给出奖励塑形设计。

- depends_on_cn：无显式目标问题

- sets_up_cn：为LSTM训练提供监督信号。

- evidence_pointer：Section 2.3 Eq.(2)

### 36. Section 2.3 P3

- order：36

- section：Section 2.3

- locator：Section 2.3 P3

- move_code：LIMITATION

- paraphrase_cn：逆强化学习假设人类数据最优，但本数据包含专家和非专家，该假设不适用。

- rhetorical_function_cn：排除替代方法并说明理由。

- depends_on_cn：奖励模型需求

- sets_up_cn：为自定义指数反向传播提供合理性。

- evidence_pointer：Section 2.3 P3

### 37. Section 2.3 P5

- order：37

- section：Section 2.3

- locator：Section 2.3 P5

- move_code：DESIGN_FEATURE

- paraphrase_cn：对每个策略簇训练独立的LSTM网络来估计奖励，因为策略簇内部时间依赖不同。

- rhetorical_function_cn：将序列学习用于奖励建模。

- depends_on_cn：策略聚类结果

- sets_up_cn：为每个簇建立差异化目标函数。

- evidence_pointer：Section 2.3 P5

### 38. Section 2.3 P8-P9

- order：38

- section：Section 2.3

- locator：Section 2.3 P8-P9

- move_code：DESIGN_FEATURE

- paraphrase_cn：加入合成平局数据并用镜像翻转数据强制零和对称性，最终奖励取两个LSTM输出的平均差。

- rhetorical_function_cn：处理数据标签稀疏和对称性约束。

- depends_on_cn：原始胜负数据

- sets_up_cn：提高奖励模型在相似状态和角色互换下的合理性。

- evidence_pointer：Section 2.3 P8-P9, Eq.(3)

### 39. Fig. 4附近

- order：39

- section：Section 2.3

- locator：Fig. 4附近

- move_code：RESULT

- paraphrase_cn：LSTM训练结果表明模型能清楚区分胜者、败者和合成平局，并输出连续预期获胜程度。

- rhetorical_function_cn：验证奖励模型有效性。

- depends_on_cn：LSTM训练设计和数据

- sets_up_cn：为将其用作Eq.(4)目标函数提供依据。

- evidence_pointer：Fig. 4

### 40. Section 3 intro P1

- order：40

- section：Section 3

- locator：Section 3 intro P1

- move_code：STUDY_OVERVIEW

- paraphrase_cn：提出两阶段人机协作框架：开局非自适应阶段和后续自适应反馈阶段。

- rhetorical_function_cn：预览第三章内容。

- depends_on_cn：模型与奖励

- sets_up_cn：分别展开两个阶段。

- evidence_pointer：Section 3 intro P1

### 41. Section 3.1 P1

- order：41

- section：Section 3.1

- locator：Section 3.1 P1

- move_code：DESIGN_FEATURE

- paraphrase_cn：开局阶段从经验数据提取成功开局策略，以分阶段目标建议呈现给人类选择。

- rhetorical_function_cn：描述开局阶段的设计。

- depends_on_cn：策略聚类结果

- sets_up_cn：为图5示例提供说明。

- evidence_pointer：Section 3.1 P1

### 42. Section 3.2 P1

- order：42

- section：Section 3.2

- locator：Section 3.2 P1

- move_code：DESIGN_FEATURE

- paraphrase_cn：自适应阶段使用反馈控制架构，识别最近的策略簇并求解微分博弈给出建议；人类可选择是否遵循。

- rhetorical_function_cn：描述自适应阶段设计。

- depends_on_cn：奖励模型和MPC

- sets_up_cn：引入微分博弈公式。

- evidence_pointer：Section 3.2 P1

### 43. Section 3.2 P2

- order：43

- section：Section 3.2

- locator：Section 3.2 P2

- move_code：DESIGN_FEATURE

- paraphrase_cn：将DCP形式化为Eq.(4)的微分博弈，包含系统约束、状态/行动界、可行性约束和整数约束。

- rhetorical_function_cn：给出优化问题的完整表述。

- depends_on_cn：状态空间模型和奖励模型

- sets_up_cn：为算法求解提供对象。

- evidence_pointer：Section 3.2 Eq.(4)

### 44. Section 3.2 P4-P5

- order：44

- section：Section 3.2

- locator：Section 3.2 P4-P5

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：用MPC在有限预测窗口中迭代求解纳什均衡，并在每个时间步用实际game state进行独立求解以实现公平比较。

- rhetorical_function_cn：解释求解策略和比较逻辑。

- depends_on_cn：微分博弈公式

- sets_up_cn：为图6博弈解与人类数据对比提供方法。

- evidence_pointer：Section 3.2 P4-P5

### 45. Fig. 6附近

- order：45

- section：Section 3.2

- locator：Fig. 6附近

- move_code：RESULT

- paraphrase_cn：均衡解在平均意义上比实际玩家奖励更平衡，对败者更高、对胜者更低。

- rhetorical_function_cn：展示核心计算发现。

- depends_on_cn：MPC求解结果

- sets_up_cn：引出对保守性和适用人群的讨论。

- evidence_pointer：Fig. 6

### 46. Section 3.2 P7

- order：46

- section：Section 3.2

- locator：Section 3.2 P7

- move_code：BOUNDARY_CONDITION

- paraphrase_cn：博弈建议对低水平玩家提供合理指导，对高水平玩家可能过于保守；在对手水平未知时提供安全但次优建议。

- rhetorical_function_cn：界定建议适用的用户和情境。

- depends_on_cn：图6结果

- sets_up_cn：为讨论部分“人类最终评估”提供基础。

- evidence_pointer：Section 3.2 P7

### 47. Section 3.2 P8

- order：47

- section：Section 3.2

- locator：Section 3.2 P8

- move_code：LIMITATION_AND_FUTURE

- paraphrase_cn：当前方法计算代价高，需离线求解；实时实现可通过响应面近似，但人机实时实验留待未来。

- rhetorical_function_cn：表明计算限制和未来方向。

- depends_on_cn：求解实验

- sets_up_cn：为第四章分区求解提供动机。

- evidence_pointer：Section 3.2 P8

### 48. Section 4 intro P1-P3

- order：48

- section：Section 4

- locator：Section 4 intro P1-P3

- move_code：GAP

- paraphrase_cn：all-in-one求解可能不高效；现有设计结构矩阵和功能依赖表等方法不适用于黑箱目标问题。

- rhetorical_function_cn：构造分区求解的研究缺口。

- depends_on_cn：第三章all-in-one局限

- sets_up_cn：引出三种任务划分方法。

- evidence_pointer：Section 4 intro P1-P3

### 49. Section 4 intro P4

- order：49

- section：Section 4

- locator：Section 4 intro P4

- move_code：DESIGN_FEATURE

- paraphrase_cn：采用顺序协调策略，依次求解各子问题并传递最优解。

- rhetorical_function_cn：说明分区后如何协调。

- depends_on_cn：分区问题定义

- sets_up_cn：为后续三种划分方法提供统一求解框架。

- evidence_pointer：Section 4 intro P4

### 50. Section 4.1 P1

- order：50

- section：Section 4.1

- locator：Section 4.1 P1

- move_code：BENCHMARK_OR_CONTRAST

- paraphrase_cn：人工语义划分作为基线，按变量含义手工分成四个子问题。

- rhetorical_function_cn：建立分区比较的baseline。

- depends_on_cn：分区需求

- sets_up_cn：为无监督/有监督划分提供参照。

- evidence_pointer：Section 4.1, Table 2

### 51. Section 4.2 P1-P2

- order：51

- section：Section 4.2

- locator：Section 4.2 P1-P2

- move_code：DESIGN_FEATURE

- paraphrase_cn：无监督划分用k-medoids和Pearson相关作为距离，把高相关变量分到同一子问题。

- rhetorical_function_cn：描述无监督划分方法。

- depends_on_cn：经验数据

- sets_up_cn：为图7中非语义划分模式提供来源。

- evidence_pointer：Section 4.2 P1-P2

### 52. Section 4.3 P1-P2

- order：52

- section：Section 4.3

- locator：Section 4.3 P1-P2

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：有监督划分利用奖励函数训练个体目标，以个体目标与团队目标的错位之和作为划分优化目标，从而避免嵌套Nash求解的高开销。

- rhetorical_function_cn：解释有监督划分为何有效且可计算。

- depends_on_cn：奖励模型

- sets_up_cn：为Eq.(5)优化问题提供逻辑。

- evidence_pointer：Section 4.3 P1-P2

### 53. Section 4.3 P3-P4

- order：53

- section：Section 4.3

- locator：Section 4.3 P3-P4

- move_code：DESIGN_FEATURE

- paraphrase_cn：将状态变量划分为N个子问题并最小化总错位；用粒子群优化连续松弛求解整数划分问题。

- rhetorical_function_cn：给出有监督划分的数学形式和求解方法。

- depends_on_cn：错位目标

- sets_up_cn：为图8a结果提供算法。

- evidence_pointer：Section 4.3 Eq.(5), P4

### 54. Fig. 8附近

- order：54

- section：Section 4.3

- locator：Fig. 8附近

- move_code：RESULT

- paraphrase_cn：有监督划分显著降低总错位；无监督和有监督划分在胜者奖励上均优于all-in-one和人工划分。

- rhetorical_function_cn：报告分区方法的核心结果。

- depends_on_cn：三种划分方法和求解

- sets_up_cn：为讨论中“计算机团队优于单一计算机”提供证据。

- evidence_pointer：Fig. 8a/b

### 55. Section 5 P1

- order：55

- section：Section 5

- locator：Section 5 P1

- move_code：BOUNDARY_CONDITION

- paraphrase_cn：方法论适用于存在或可收集历史决策数据的工程问题，但解的质量依赖数据的多样性、规模和特征质量。

- rhetorical_function_cn：限定方法适用条件。

- depends_on_cn：前文所有计算实验

- sets_up_cn：引出主要take-aways。

- evidence_pointer：Section 5 P1

### 56. Take-away 1

- order：56

- section：Section 5

- locator：Take-away 1

- move_code：CONTRIBUTION

- paraphrase_cn：战略/操作分离能有效管理问题复杂度，使战略问题规模不随军队规模变化。

- rhetorical_function_cn：把结果提升为设计知识。

- depends_on_cn：建模和实验

- sets_up_cn：为其他DCP应用提供一般原则。

- evidence_pointer：Section 5 Take-away 1

### 57. Take-away 2

- order：57

- section：Section 5

- locator：Take-away 2

- move_code：MECHANISM

- paraphrase_cn：方法通过两个机制适应对手策略：策略簇切换提供大调整，簇内状态反馈提供小调整。

- rhetorical_function_cn：解释适应机制。

- depends_on_cn：策略聚类和自适应博弈

- sets_up_cn：说明架构如何应对动态竞争。

- evidence_pointer：Section 5 Take-away 2

### 58. Take-away 3

- order：58

- section：Section 5

- locator：Take-away 3

- move_code：CONTRIBUTION

- paraphrase_cn：人机协作架构可缓解博弈论的局限：人类可结合AI建议和自身对对手行为的判断做最终决策。

- rhetorical_function_cn：把架构定位为人机互补而非替代。

- depends_on_cn：博弈建议保守性结果

- sets_up_cn：回扣引言中混合团队命题。

- evidence_pointer：Section 5 Take-away 3

### 59. Take-away 4-5

- order：59

- section：Section 5

- locator：Take-away 4-5

- move_code：CONTRIBUTION

- paraphrase_cn：大规模DCP推荐使用计算机咨询团队而非单一元规划器；计算机团队偏好非直观任务划分。

- rhetorical_function_cn：提炼任务分工的设计知识。

- depends_on_cn：分区实验结果

- sets_up_cn：为未来混合团队设计提出明确建议。

- evidence_pointer：Section 5 Take-away 4-5

### 60. Section 6 P2

- order：60

- section：Conclusion

- locator：Section 6 P2

- move_code：CONTRIBUTION

- paraphrase_cn：总结结果：博弈论建议对高水平玩家保守但可为非专家和安全建议提供支持；分区后的计算机团队优于all-in-one，尤其在大型复杂问题中。

- rhetorical_function_cn：收束全文贡献。

- depends_on_cn：全部研究阶段

- sets_up_cn：结束论证并指向未来工作。

- evidence_pointer：Section 6 P2

## 写作技术

- gap_construction_cn：作者先承认自动化支持人类决策的历史（Fitts List），再指出既有自动化多用于定义良好的操作任务，随后提出“高层战略决策支持”和“混合团队分工方法”两个未被研究的缺口；同时在1.1中通过LQR和动态规划的数学局限构造方法论缺口。

- signposting_cn：在摘要和贡献部分直接列出技术要素；在引言末尾预告各章内容；在每个方法小节开头说明该模块将如何被使用；反复使用“本节/以下小节”进行预告。

- transition_logic_cn：每个阶段末尾都留下供下一阶段使用的输出：模型验证后过渡到聚类；聚类后过渡到奖励模型；奖励模型后过渡到决策架构；all-in-one计算昂贵后过渡到分区求解；分区结果后过渡到设计知识提炼。

- claim_evidence_rhythm：方法陈述后紧接图表验证：“建模—图2”、“聚类—图3”、“奖励—图4”、“博弈—图6”、“分区—图7/8”；讨论部分再把图内结果提炼成take-aways。

- benchmark_narrative_cn：将all-in-one作为总基线，将人工语义划分作为分区基线；在分区比较中固定对手为Nash解，保证分区改进不是来自对手变化；通过无监督/有监督的梯度展示方法谱系从ad hoc到objective。

- theory_return_cn：讨论部分没有停留在性能数字，而是返回博弈论和混合团队理论：用“保守均衡”说明人类最终判断的必要性，用“非直观划分”说明人类和计算机任务偏好可能不同。

- contribution_positioning_cn：在Introduction明确“primary contribution”是架构而非单点性能；在讨论中以“take-aways”形式把结果写成可复用设计知识；在结论中重复架构价值但标注未来人机实验。

- novelty_protection_cn：通过强调“文献尚未研究”“系统性方法缺失”多次防止贡献被简化为“在StarCraft上跑赢了”；通过显示分区优于all-in-one和非直观划分，使贡献从单一性能比较上升为团队分工设计知识。

## 可复用研究与写作程序

### structure_steps

#### 1. 1

- step：1

- writing_job_cn：建立问题类别（如DCP）和现实例子，指出传统方法不足。

- research_job_cn：提炼问题特征：连续决策、对抗性、高复杂度、目标不明确等。

- required_evidence_cn：能说明问题复杂性和现有方法缺口的文献与案例。

- transition_to_next_cn：引出“需要形式化表示”作为下一步。

#### 2. 2

- step：2

- writing_job_cn：描述数学建模和变量定义，说明分层/简化逻辑。

- research_job_cn：建立状态空间方程并验证其与实际数据的一致性。

- required_evidence_cn：模型预测值与经验数据对比，尤其在目标时间尺度上的吻合。

- transition_to_next_cn：模型提供变量，下一步需要识别问题中的策略模式。

#### 3. 3

- step：3

- writing_job_cn：说明从数据中发现策略模式的必要性和方法。

- research_job_cn：用聚类等方法识别多个策略簇并解释其含义。

- required_evidence_cn：簇数选择依据和簇的可解释性。

- transition_to_next_cn：每个策略簇需要独立的目标函数，引出奖励学习。

#### 4. 4

- step：4

- writing_job_cn：描述如何在没有显式目标时构造奖励模型。

- research_job_cn：训练序列学习模型，处理数据不平衡和对称性。

- required_evidence_cn：模型能区分不同结果类别并输出连续价值估计。

- transition_to_next_cn：奖励模型成为后续决策优化的目标函数。

#### 5. 5

- step：5

- writing_job_cn：描述两阶段决策流程：非自适应的开局阶段和自适应博弈阶段。

- research_job_cn：实现并使用MPC/博弈论求解建议，与实际人类决策对比。

- required_evidence_cn：建议与实际数据的对比、保守性分析、计算复杂度说明。

- transition_to_next_cn：如果单机求解昂贵或低效，引出分区求解。

#### 6. 6

- step：6

- writing_job_cn：描述任务划分方法和协调机制，设置baseline。

- research_job_cn：实现人工/无监督/有监督划分并评估团队性能。

- required_evidence_cn：分区方法相比all-in-one和baseline的性能改进。

- transition_to_next_cn：用结果提炼一般化设计知识。

#### 7. 7

- step：7

- writing_job_cn：在讨论中把计算发现转为take-aways和边界条件。

- research_job_cn：总结哪些结论可复用、依赖什么条件、哪些没测。

- required_evidence_cn：对方法和数据的局限性有明确说明。

- transition_to_next_cn：结论中重申贡献并列出未来工作。

### most_transferable_moves_cn

1. 在引言中用“已有方法A→局限→本文新视角B”制造缺口

2. 用“每阶段输出是下一阶段输入”的链式段落组织方法

3. 每个设计元素后立即配图和验证结果

4. 把黑箱目标问题转化为数据驱动的奖励学习

5. 用all-in-one和语义划分作为双层baseline

6. 在讨论中把计算现象提炼为可操作的设计原则

### resource_intensive_or_nonstandard_parts_cn

1. StarCraft II replay数据及API后处理管道

2. 大规模高维LSTM训练和合成数据构造

3. 每次Nash均衡求解需要遗传算法大种群和迭代

4. 有监督分区需要反复训练多个LSTM子目标

5. 领域专家对策略簇数和语义标签的判断

### what_not_to_copy_superficially_cn

1. 不能只在文字上声明“人机混合团队”而没有human-in-the-loop证据

2. 不能把“对高手保守”当作普适结论，因为文中只有计算对比

3. 不能把“分区优于all-in-one”推广到所有协调策略和所有问题规模

4. 不能忽视数据质量、策略多样性和特征选择等前提条件

5. 不能把StarCraft上的实现直接当作其他DCP的成熟系统

- single_best_description_of_the_routine_cn：先定义一类复杂问题，再用数据驱动建模把无目标问题变成可优化问题，用控制与博弈方法给出保守建议，最后用分区计算证明“多计算机团队比单机更优”并提炼成设计原则。

## 分析边界

未提供真实页码，所有位置证据来自章节、段落、表和图；全文图表转换中有部分图片缺失或仅有占位，不影响主要文字逻辑；未提供附录和代码。结论基于对全文文本的分析者判断。
