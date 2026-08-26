# A new approximate belief rule base expert system for complex system modelling

- 作者：You Cao; Zhi Jie Zhou; Chang Hua Hu; Shuai Wen Tang; Jie Wang
- 年份 / 期刊：2021 / Decision Support Systems
- DOI：10.1016/j.dss.2021.113558
- 源文件：19766_2021_a-new-approximate-belief-rule-base-expert-system-for-complex-system-modelling.md
- 论文主类型：build_evaluate_design_science
- 主导写作弧线：performance_gap_artifact_benchmark_generalize
- 置信度：0.85

## 文章级论证概况

- 核心问题：如何设计一种既保留专家知识可解释性、又避免传统置信规则库(BRB)规则爆炸和弱可扩展性问题的专家系统，使其适用于复杂系统建模？

- 制品与设计：提出近似置信规则(ABR)，每个规则只包含单个属性，并通过独立因子对属性权重进行折扣来近似处理属性间的相关性；由这些ABR构成的ABRB模型使用ER方法推理，并提供属性、参考值和识别框架(FoD)的增量扩展机制。

- 客观结果：在锂电池容量健康状态估计案例中，优化后ABRB的MSE=1.04E-4，优于初始ABRB(1.51E-3)、FRB(1.67E-3)、ELM(1.09E-4)，接近BRB(1.06E-4)和BPNN(0.98E-4)，但ABRB只有11条规则而BRB有30条；在10%/30%小训练集下ABRB优于BPNN；新增Heating rate属性后MSE改善至1.01E-4，扩充识别框架后MSE升至2.6E-4但输出更细致。

- 核心贡献：开发了一个ABRB专家系统，通过单属性规则和独立因子解决规则爆炸和弱可扩展性，使专家知识能很好嵌入；理论上证明了ABRB与BRB具有相同的万能逼近能力；提出了针对属性、参考值和识别框架的扩展方法以保障长期有效性。

- 整篇论证链：作者首先指出BRB中的专家知识是可解释性的基础，但连接假设下的规则爆炸和弱可扩展性限制了专家知识利用。为解决这些问题，他们设计了基于单属性规则的ABR，通过独立因子折扣属性权重来处理属性相关性。他们证明ABRB同样具有万能逼近能力（使用Stone-Weierstrass定理），并分析了ABRB在属性、参考值、FoD方面的可扩展性。在锂电池健康状态估计案例中，ABRB用比BRB更紧致的规则集取得近似精度，在小样本场景下优于BPNN；新增属性时只需增加对应规则并更新独立因子，新增FoD元素时通过D-S规则重新分配信念。由此，论文提出一种兼顾可解释性、紧凑性和可扩展性的复杂系统建模专家系统，为未来构建大规模BRB提供了新思路。

## 类型与写作弧线判定

- 论文主类型判定：文章识别现有BRB制品的不足（规则爆炸、弱可扩展性），提出新制品ABRB，通过理论证明和案例研究评价其性能，并总结出可复用的扩展设计原则，符合设计科学“需求—构建—评价—设计知识”的套路。

- 主导写作弧线判定：论证从BRB的性能缺口（规则数量指数增长、重设计成本高）出发，提出ABRB制品，通过理论证明、案例benchmark对比、小样本分析和扩展验证，最终将紧凑性和可扩展性推广为一般化设计知识。

## 研究开展程序

- study_or_phase_count：6

- 研究阶段总序列：先形式化BRB的规则爆炸和弱可扩展性问题并提炼三个研究问题；然后设计ABRB模型（相关性处理、规则结构、推理、逼近证明、优化框架）；接着开发属性/参考值/FoD扩展方法；随后在LPB案例中构建并优化ABRB，验证实际可行性；再通过BRB/FRB/BPNN/ELM对比和小样本分析展示性能与紧凑性；最后演示扩展流程并总结可解释性。阶段之间通过“理论能力需实践验证”“实际性能需与基线对比”“可扩展性需案例演示”等递进逻辑连接。

### studies_or_phases

#### 1. 问题形式化与需求分析

- order：1

- name_cn：问题形式化与需求分析

- question_cn：传统BRB在连接假设下规则数量如何随属性增长？弱可扩展性如何阻碍知识更新？

- inputs_and_setting_cn：已有BRB建模公式、文献中的规则规模公式、感冒诊断示例

- designed_or_compared_object_cn：比较连接假设BRB（L1=∏Mi）与单属性规则模型（L2=∑Mi）的规模；分析增加属性时规则重设计示例

- baseline_control_or_counterfactual_cn：以传统BRB为baseline；单属性规则为替代

##### objective_metrics

1. 规则数量

2. 扩展所需重设计规则数

- analysis_method_cn：形式化计算和语义分析

- main_result_cn：L1随属性数指数增长，L2线性增长；增加一个属性时传统BRB需要重设全部规则，单属性规则只需增加新属性对应的规则

- argumentative_role_cn：确立规则爆炸和弱可扩展性是限制专家知识嵌入的关键缺口，为ABR提供动机

- remaining_uncertainty_cn：如何在不忽略属性相关性的前提下构建单属性规则？

- link_to_next_phase_cn：明确提出三个待解决问题（相关性处理、ABR构建、工程扩展），引向ABRB模型设计

##### evidence_pointers

1. Section 2.2 公式 L1、L2

2. 感冒诊断示例式(2-a)(2-b)(3)

#### 2. ABRB模型构建与理论逼近证明

- order：2

- name_cn：ABRB模型构建与理论逼近证明

- question_cn：如何定义基于单属性的近似规则ABR，并通过折扣权重处理属性相关性？ABRB是否具有与BRB相同的万能逼近能力？

- inputs_and_setting_cn：数据样本用于MMI计算；专家知识用于初始规则参数；数学证明环境

- designed_or_compared_object_cn：设计ABR规则（式10）、独立性因子定义（式6-9）、推理过程（式11-14）；与BRB的逼近能力作理论比较

- baseline_control_or_counterfactual_cn：以BRB的万能逼近性质为理论参照

##### objective_metrics

1. 规则形式是否单属性

2. 函数集是否满足Stone-Weierstrass条件

- analysis_method_cn：定义+解析公式+Stone-Weierstrass定理证明

- main_result_cn：ABRB函数集对加法、乘法、数乘封闭，可区分不同输入，故具有与BRB相同的万能逼近能力

- argumentative_role_cn：提供ABRB的理论合法性，说明其建模能力不低于BRB

- remaining_uncertainty_cn：理论证明未考虑真实数据噪声和参数优化效果

- link_to_next_phase_cn：提出优化问题，并进入可扩展性方法设计

##### evidence_pointers

1. Section 3.1 式(6)-(9)

2. Section 3.2 式(10)-(14)

3. Section 3.3 定理1、2及证明

#### 3. 可扩展性方法开发（属性/参考值/FoD）

- order：3

- name_cn：可扩展性方法开发（属性/参考值/FoD）

- question_cn：在增加或删除属性、参考值和识别框架元素时，如何更新ABRB而不重设计整个模型？

- inputs_and_setting_cn：LPB退化过程的先验知识；新状态加入时专家提供的γ概率；D-S规则

- designed_or_compared_object_cn：提出属性/参考值扩展公式（式20）；FoD新增元素时信念重分配公式（式22-a~d）；FoD删除元素时重分配公式（式24-a~c）

- baseline_control_or_counterfactual_cn：以传统BRB的全局重设计为对照

##### objective_metrics

1. 是否只需局部更新

2. 是否保持原有规则参数不变

- analysis_method_cn：数学推导与D-S证据理论

- main_result_cn：ABRB扩展只需增加/删除对应规则组并更新独立因子；FoD变化可通过D-S规则重分配信念度

- argumentative_role_cn：支撑ABRB长期有效性的关键设计，为后续案例扩展验证提供方法

- remaining_uncertainty_cn：扩展导致的误差累积程度未知，需案例验证

- link_to_next_phase_cn：在案例研究中用LPB数据验证ABRB构建、训练、扩展全流程

##### evidence_pointers

1. Section 4.1 式(20)

2. Section 4.2 式(22-a)~(22-d), (24-a)~(24-c)

3. Remark 3, 4

#### 4. 案例研究：ABRB构建与优化

- order：4

- name_cn：案例研究：ABRB构建与优化

- question_cn：ABRB能否在实际LPB健康状态估计中取得满意精度并保持可解释性？

- inputs_and_setting_cn：NASA LPB 145个循环数据；Time-CC、Time-CV两个特征；专家初始信念分布（表4）；P-CMA-ES算法

- designed_or_compared_object_cn：构建初始ABRB（表4）并优化成优化ABRB（表5）；约束ID_i,m（式26）

- baseline_control_or_counterfactual_cn：以初始ABRB为baseline

##### objective_metrics

1. MSE

- analysis_method_cn：训练-测试（50%随机训练，全数据测试），P-CMA-ES优化，可解释性约束

- main_result_cn：优化后ABRB MSE=1.04E-4，较初始降低93.11%，信念分布贴近初始且符合约束

- argumentative_role_cn：证明ABRB在实际工程数据上的可行性、可训练性和可解释性

- remaining_uncertainty_cn：与现有主流模型相比性能如何？小样本场景下是否仍有优势？

- link_to_next_phase_cn：引入与BRB、FRB、BPNN、ELM的对比研究

##### evidence_pointers

1. Section 5.1 表1-表4

2. Section 5.2 图3-图5, 表5, 式(26)

#### 5. 对比研究：性能、紧凑性与小样本优势

- order：5

- name_cn：对比研究：性能、紧凑性与小样本优势

- question_cn：ABRB与原始BRB、FRB、BPNN、ELM相比，在精度、模型规模和小训练集表现上如何？

- inputs_and_setting_cn：同一LPB数据集；BRB（30条规则）、FRB、BPNN、ELM；不同训练比例（10%、30%、50%、60%）

- designed_or_compared_object_cn：比较各模型MSE和规则数；另做独立训练/测试50%/50%的再比较

- baseline_control_or_counterfactual_cn：以BRB为算法基准，以BPNN为数据驱动黑箱基准

##### objective_metrics

1. MSE

2. 规则数量

- analysis_method_cn：随机训练测试划分，多模型重复比较

- main_result_cn：ABRB以11条规则达到与30条规则BRB几乎一致的MSE；在10%/30%训练数据下ABRB优于BPNN；在50%/50%独立划分下ABRB MSE=1.08E-4，BPNN=1.05E-4，但ABRB泛化更好

- argumentative_role_cn：展示ABRB在保持类似精度的同时更紧凑，专家知识带来小样本优势

- remaining_uncertainty_cn：扩展性在真实运行中是否如预期工作？

- link_to_next_phase_cn：进行新增属性和FoD的扩展演示

##### evidence_pointers

1. Section 5.3 表6、表7

2. Remark 6 式(27-a)~(27-c)

#### 6. 扩展验证与可解释性总结

- order：6

- name_cn：扩展验证与可解释性总结

- question_cn：ABRB能否通过局部更新添加新属性（Heating rate）和新识别框架元素（CF）？全模型可解释性体现在哪些方面？

- inputs_and_setting_cn：新增Heating rate特征数据；专家为新增规则提供初始信念（表9）；新状态CF对应的γ概率（表11）；原有的Time-CC、Time-CV规则和优化后Heating规则（表10）

- designed_or_compared_object_cn：扩展后的ABRB（表12），比较扩展前后MSE和信念分布输出

- baseline_control_or_counterfactual_cn：以扩展前优化ABRB为baseline；也对比初始ABRB

##### objective_metrics

1. MSE

2. 信念分布形状

3. 输出可解释性

- analysis_method_cn：局部优化新增规则，D-S规则重分配FoD，图6-7分析

- main_result_cn：添加Heating rate后MSE改善至1.01E-4；扩充FoD（加入CF）后MSE为2.6E-4，但输出能更精细描述健康状态，且信念分布斜率可解释状态迁移过程

- argumentative_role_cn：验证ABRB可扩展性设计；总结可解释性四方面（建立、优化、扩展、输出）

- remaining_uncertainty_cn：复杂扩展场景误差增大，仍需一般性扩展方法；进一步验证需要更多实验

- link_to_next_phase_cn：结论部分总结贡献和未来方向

##### evidence_pointers

1. Section 5.4 表8-表12, 图6

2. Section 5.5 图7

## 各部分修辞架构

### abstract_moves

1. CONTEXT

2. LIMITATION

3. RQ_OR_OBJECTIVE

4. DESIGN_FEATURE

5. THEORY_PROPOSITION

6. REQUIREMENT

### introduction_moves

1. PRIOR_KNOWLEDGE

2. CONTEXT

3. PRIOR_KNOWLEDGE

4. LIMITATION

5. REQUIREMENT

6. PRIOR_KNOWLEDGE

7. RQ_OR_OBJECTIVE

8. CONTRIBUTION

9. STUDY_OVERVIEW

### theory_and_knowledge_moves

1. PRIOR_KNOWLEDGE

2. METHOD_JUSTIFICATION

3. THEORY_PROPOSITION

4. DESIGN_FEATURE

5. THEORY_INTRO

6. HYPOTHESIS_OR_PROPOSITION

7. RESULT

### artifact_design_moves

1. DESIGN_FEATURE

2. DESIGN_FEATURE

3. BOUNDARY_CONDITION

4. DESIGN_FEATURE

5. MECHANISM

6. DESIGN_FEATURE

### evaluation_moves

1. PRACTICAL_STAKES

2. RQ_OR_OBJECTIVE

3. METHOD

4. RESULT

5. BENCHMARK_OR_CONTRAST

6. RESULT

7. LIMITATION_AND_FUTURE

8. METHOD

9. LIMITATION

### discussion_and_contribution_moves

1. CONTRIBUTION

2. CONTRIBUTION

3. LIMITATION_AND_FUTURE

## 理论/知识到设计的翻译

### 知识/理论基础

1. BRB/RIMER理论 (Yang et al., 2006)

2. 属性相关性度量方法 (Pearson, Spearman, Kendall, mutual information, MMI)

3. Stone-Weierstrass定理

4. Dempster-Shafer证据理论

5. 可扩展性/变革性概念 (Ross et al., 2008)

6. 先前单属性信念规则研究 (Chen et al., 2015; Li et al., 2019)

7. P-CMA-ES优化算法

- 理论—设计耦合：partial

- 耦合判定理由：ABR单属性结构主要来源于已有单属性规则和工程可解释性需求，而非从某个基础理论推演；独立因子和折扣权重来自现有相关文献；Stone-Weierstrass定理只用于事后验证逼近能力，未在设计初始指导规则形式；优化和可解释性约束来自应用需求。因此关键制品选择原理上由领域知识和经验启发，理论更多用于论证和解释。

- 理论到设计翻译链：传统BRB连接假设导致规则爆炸和重设计 → 需要线性规模且易扩展的规则结构 → 采用单属性规则；属性相关性不应被忽略 → 用互信息度量相关性并定义独立因子 → 用独立因子折扣属性权重；近似模型需保证能力不损失 → 用Stone-Weierstrass定理验证ABRB函数类的逼近能力；长期运行需要扩展 → 设计局部更新方法和D-S重分配方法。

### mapping_table

#### 1. 1

- theory_or_knowledge_claim_cn：BRB规则数在连接假设下随属性指数增长（L1=∏Mi）

- mechanism_cn：横向组合参考值导致组合爆炸

- design_requirement_cn：规则库规模应线性增长，且单个规则简单

- artifact_choice_cn：每个属性独立建立一系列单输入规则（ABR）

- evaluated_contrast_cn：对比ABRB（11规则）和BRB（30规则）的MSE

- objective_result_cn：ABRB MSE=1.04E-4，BRB=1.06E-4，规则数大幅减少

##### evidence_pointers

1. Section 2.2 L1/L2公式

2. Table 6

#### 2. 2

- theory_or_knowledge_claim_cn：属性相关性普遍存在，忽略会降低建模精度，强相关可去除，弱相关应降低影响

- mechanism_cn：弱相关信息冗余和噪声会干扰权重

- design_requirement_cn：在每个属性的权重中应包含独立因子以折扣相关性影响

- artifact_choice_cn：定义基于MMI的独立因子φ_ij，将属性权重更新为δ_i'=∏φ_ij δ_i

- evaluated_contrast_cn：在添加新属性时更新独立因子矩阵后，扩展ABRB MSE改善；但未单独做消融实验对比是否折扣

- objective_result_cn：增加Heating rate并更新独立因子后，MSE从1.04E-4降至1.01E-4

##### evidence_pointers

1. Section 3.1 式(6)-(9)

2. Section 5.4 式(28), Table 10

#### 3. 3

- theory_or_knowledge_claim_cn：万能逼近性要求函数集对代数运算封闭且能区分点

- mechanism_cn：满足Stone-Weierstrass条件即可逼近任意连续函数

- design_requirement_cn：ABRB输出函数f(x) 应满足封闭性和点分离

- artifact_choice_cn：使用解析ER公式定义输出，通过证明ABRB规则集的ζ函数和权重函数满足条件

- evaluated_contrast_cn：证明而非数值对比；理论等价于BRB

- objective_result_cn：ABRB满足定理条件，具有与BRB相同的万能逼近能力

##### evidence_pointers

1. Section 3.3 Theorem 1, 2 和证明

#### 4. 4

- theory_or_knowledge_claim_cn：长期使用中属性、参考值、识别框架需要更新，且不希望重设计整个模型

- mechanism_cn：系统知识随实践积累，扩展应该是增量的

- design_requirement_cn：扩展时应保持原参数和结构不变，只做局部更新

- artifact_choice_cn：每个属性对应独立规则组，新增属性等于添加新规则组并更新独立因子；FoD变化用D-S规则重分配信念

- evaluated_contrast_cn：案例中分别增加属性Heating rate和FoD元素CF，与扩展前ABRB比较

- objective_result_cn：属性扩展后MSE降到1.01E-4；FoD扩展后MSE升至2.6E-4但输出更细致

##### evidence_pointers

1. Section 4.1-4.2

2. Section 5.4 Table 8-12, Fig.6

#### 5. 5

- theory_or_knowledge_claim_cn：专家知识应作为初始约束，优化不应破坏参数含义

- mechanism_cn：先验知识缩小搜索空间，并保持局部搜索

- design_requirement_cn：优化中应加入可解释性约束，初始值贴近最优

- artifact_choice_cn：使用可解释性约束ID_i,m（信念分布不应冲突），采用P-CMA-ES局部优化

- evaluated_contrast_cn：优化前后信念分布对比，观察是否保持接近

- objective_result_cn：优化后信念分布与初始接近，符合约束

##### evidence_pointers

1. Section 5.2 图3, 式(26)

## 评价逻辑

### evaluation_modes

1. 理论证明

2. 案例研究

3. 基准对比

4. 小样本分析

5. 扩展验证

6. 可解释性分析

- why_these_evaluations_cn：理论证明用于保证建模能力的理论下界；案例研究验证实际可行性；基准对比展示与既有方法相比的优势；小样本分析凸显专家知识价值；扩展验证检验可扩展性设计；可解释性分析支持专家系统性质。

- benchmark_and_contrast_chain_cn：先用初始ABRB作为自身基准评估优化效果；再与BRB/FRB/BPNN/ELM对比；随后用不同训练集规模对比ABRB与BPNN；最后用扩展前后ABRB对比验证扩展能力。对照阶梯从自身到外部，从静态到扩展。

### claim_evidence_ledger

1. 技术主张：ABRB具有与BRB相同的万能逼近能力；证据：Stone-Weierstrass定理证明（Section 3.3）。

2. 制品主张：ABRB在紧凑规则数下达到与BRB相当精度；证据：表6中ABRB 11规则MSE=1.04E-4，BRB 30规则MSE=1.06E-4。

3. 机制主张：独立因子折扣属性权重能处理弱相关；证据：扩展Heating rate时更新独立因子，MSE下降；但缺少与不折扣对照。

4. 边界主张：ABRB在小样本下优于BPNN；证据：表7中10%/30%训练数据ABRB MSE低于BPNN。

5. 设计知识：ABRB能局部扩展；证据：案例中新增属性和FoD只需添加规则并重分配信念，无需重设计原规则。

6. 可解释性主张：ABRB输出可解释性强；证据：信念分布图和斜率分析展示状态迁移，但无量化对比。

- internal_validity_strategy_cn：使用同一数据集、相同训练/测试划分比较各模型；随机选取训练集；使用解释性约束限制参数空间；优化算法固定；通过初始值贴近最优实现局部搜索；承认随机划分可能带来偏置，并解释其公平性。

- external_validity_strategy_cn：使用NASA真实LPB实验数据，贴近航天应用；案例覆盖模型构建、优化、扩展、解释等多个环节；但仅一个数据集，外部有效性有限。

- what_is_not_actually_tested_cn：未对独立因子必要性进行消融实验；未测试ABRB在更多真实复杂系统上的表现；未对比与其他属性相关性处理方法的差异；未验证强相关未消除时模型行为；FoD扩展的误差未做小样本优化验证。

## 贡献闭环

- technical_claim_cn：提出了ABRB，一种基于单属性规则和独立因子的BRB变体，具有与BRB相当的逼近能力和更紧凑的规则结构。

- artifact_claim_cn：ABR、独立因子折扣权重、以及局部扩展机制共同实现了线性规模规则库和无需重设计的增量更新。

- mechanism_claim_cn：独立因子通过归一化互信息度量属性相关性，并以权重折扣方式降低弱相关性的影响；FoD扩展通过D-S规则将未区分状态的概率重分配。

- boundary_claim_cn：适用于强相关已被前两种方法消除、仅剩弱相关性的工程场景；扩展方法在简单扩展中有效，复杂扩展会导致误差增大。

- reusable_design_knowledge_cn：设计单属性规则库时可利用独立因子折扣权重处理相关性；扩展新属性时只需创建独立规则组并更新独立因子；扩展FoD时可用D-S规则进行信念重分配。

- theoretical_contribution_cn：证明ABRB函数类满足Stone-Weierstrass定理条件，从而具有与BRB相同的万能逼近能力；但未修改或扩展基础理论。

- how_discussion_closes_intro_gap_cn：结论重新强调了规则爆炸和弱可扩展性对专家知识利用的限制，指出ABRB通过单属性规则和折扣权重解决该问题，并声称通过理论和案例验证；最后承认局限并展望未来。

- overclaim_or_unsupported_leaps_cn：宣称ABRB具有更好可解释性和长期有效性，但可解释性只是定性分析，未与BRB做定量对比；FoD扩展后MSE升高但被解释为提供更多信息，未证明其在决策中的实际优势；ABRB小样本优势仅与BPNN比较；通用扩展研究不足。

## 句级写作动作图谱

### 1. P1 S1

- order：1

- section：Abstract

- locator：P1 S1

- move_code：CONTEXT

- paraphrase_cn：专家知识是BRB可解释性的基础。

- rhetorical_function_cn：建立背景和核心价值

- depends_on_cn：无

- sets_up_cn：为后文规则爆炸限制专家知识作铺垫

- evidence_pointer：Abstract P1 S1

### 2. P1 S2

- order：2

- section：Abstract

- locator：P1 S2

- move_code：LIMITATION

- paraphrase_cn：然而规则爆炸和弱可扩展性限制了专家知识的利用。

- rhetorical_function_cn：指出问题

- depends_on_cn：句1

- sets_up_cn：为提出ABRB设动机

- evidence_pointer：Abstract P1 S2

### 3. P1 S3

- order：3

- section：Abstract

- locator：P1 S3

- move_code：RQ_OR_OBJECTIVE

- paraphrase_cn：为解决此问题，提出一种带单属性的新近似置信规则，并构建ABRB系统。

- rhetorical_function_cn：给出解决方向

- depends_on_cn：句2

- sets_up_cn：为摘要后续贡献作铺垫

- evidence_pointer：Abstract P1 S3

### 4. P1 S4

- order：4

- section：Abstract

- locator：P1 S4

- move_code：DESIGN_FEATURE

- paraphrase_cn：新规则中，属性间的相关性由独立因子进行折扣。

- rhetorical_function_cn：描述核心设计

- depends_on_cn：句3

- sets_up_cn：为理论证明和案例铺垫

- evidence_pointer：Abstract P1 S4

### 5. P1 S5

- order：5

- section：Abstract

- locator：P1 S5

- move_code：THEORY_PROPOSITION

- paraphrase_cn：为说明ABRB与BRB相似的建模能力，理论上证明了ABRB的万能逼近能力。

- rhetorical_function_cn：预告理论贡献

- depends_on_cn：句3

- sets_up_cn：为Section3.3铺垫

- evidence_pointer：Abstract P1 S5

### 6. P1 S6

- order：6

- section：Abstract

- locator：P1 S6

- move_code：REQUIREMENT

- paraphrase_cn：在ABRB中，属性、参考值和识别框架等关键组件可被扩展，以保障长期实践的有效性。

- rhetorical_function_cn：强调可扩展性要求

- depends_on_cn：句3

- sets_up_cn：为Section4铺垫

- evidence_pointer：Abstract P1 S6

### 7. P1 S1

- order：7

- section：Introduction

- locator：P1 S1

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：回顾Yang等人通过将信念结构嵌入模糊规则库提出BRB的过程。

- rhetorical_function_cn：回顾BRB起源

- depends_on_cn：无

- sets_up_cn：为后续讨论BRB性质铺垫

- evidence_pointer：Introduction P1 S1

### 8. P2 S1

- order：8

- section：Introduction

- locator：P2 S1

- move_code：CONTEXT

- paraphrase_cn：BRB的应用分为两类：作为通用逼近器（黑盒）或作为专家系统（强调可解释性和内部机制）。

- rhetorical_function_cn：区分BRB两种用途，定位本文关注专家系统

- depends_on_cn：句7

- sets_up_cn：为强调专家知识作用铺垫

- evidence_pointer：Introduction P2 S1

### 9. P3 S1

- order：9

- section：Introduction

- locator：P3 S1

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：专家知识在BRB专家系统中对保证准确性和可解释性起关键作用。

- rhetorical_function_cn：建立专家知识重要性的前提

- depends_on_cn：句8

- sets_up_cn：为三种情况铺垫

- evidence_pointer：Introduction P3 S1

### 10. P5 S2

- order：10

- section：Introduction

- locator：P5 S2

- move_code：LIMITATION

- paraphrase_cn：不幸的是，在连接假设下，这个过程可能受限于BRB模型，导致规则爆炸问题。

- rhetorical_function_cn：点出核心问题

- depends_on_cn：句9

- sets_up_cn：为提出ABR动机

- evidence_pointer：Introduction P5 S2

### 11. P5 S4

- order：11

- section：Introduction

- locator：P5 S4

- move_code：REQUIREMENT

- paraphrase_cn：本文中可扩展性指专家系统在不改变原参数和结构的情况下进行扩展的能力。

- rhetorical_function_cn：给出可扩展性定义

- depends_on_cn：句10

- sets_up_cn：为第4节定义扩展方法铺垫

- evidence_pointer：Introduction P5 S4

### 12. P7 S1

- order：12

- section：Introduction

- locator：P7 S1

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：没有参考值组合的单属性规则在可读性和可扩展性方面表现良好。

- rhetorical_function_cn：指出单属性规则优势

- depends_on_cn：句10-11

- sets_up_cn：为提出ABR作铺垫

- evidence_pointer：Introduction P7 S1

### 13. P7 S7

- order：13

- section：Introduction

- locator：P7 S7

- move_code：RQ_OR_OBJECTIVE

- paraphrase_cn：为处理属性相关性，本文提出一种新的单属性信念规则，其中使用独立因子描述并降低属性相关性的影响。

- rhetorical_function_cn：提出本文化解方案

- depends_on_cn：句12

- sets_up_cn：为方法章节铺路

- evidence_pointer：Introduction P7 S7

### 14. P8 S1

- order：14

- section：Introduction

- locator：P8 S1

- move_code：CONTRIBUTION

- paraphrase_cn：本文主要贡献是开发用于复杂系统建模的ABRB专家系统。

- rhetorical_function_cn：声明主要贡献

- depends_on_cn：句13

- sets_up_cn：为摘要/结论呼应

- evidence_pointer：Introduction P8 S1

### 15. P9 S1

- order：15

- section：Introduction

- locator：P9 S1

- move_code：STUDY_OVERVIEW

- paraphrase_cn：本文余下部分组织如下：第2节介绍BRB及其问题，第3节提出ABRB，第4节分析扩展性，第5节案例研究，第6节结论。

- rhetorical_function_cn：预告结构

- depends_on_cn：句14

- sets_up_cn：为读者导航

- evidence_pointer：Introduction P9 S1

### 16. P1 S2

- order：16

- section：Section 2.2

- locator：P1 S2

- move_code：LIMITATION

- paraphrase_cn：对于连接假设下的BRB，规则爆炸和弱可扩展性使专家难以直观理解和确定所有规则。

- rhetorical_function_cn：重申问题

- depends_on_cn：Section 2.1

- sets_up_cn：为规模公式铺垫

- evidence_pointer：Section 2.2 P1 S2

### 17. P2 S1

- order：17

- section：Section 2.2

- locator：P2 S1

- move_code：RESULT

- paraphrase_cn：根据现有研究，连接假设下BRB的规模为L1=∏Mi，随属性数和参考值数指数增长。

- rhetorical_function_cn：用公式证明规则爆炸

- depends_on_cn：句16

- sets_up_cn：为对比单属性规则规模铺垫

- evidence_pointer：Section 2.2 P2 S1

### 18. P3 S4

- order：18

- section：Section 2.2

- locator：P3 S4

- move_code：PHENOMENON

- paraphrase_cn：以感冒诊断为例，当增加一个新条件（喉咙痛）时，整个规则库需要重设，所有信念度都要重新设计。

- rhetorical_function_cn：用示例展示BRB扩展代价

- depends_on_cn：感冒示例

- sets_up_cn：为ABR的优势铺垫

- evidence_pointer：Section 2.2 P3 S4

### 19. P4 S4

- order：19

- section：Section 2.2

- locator：P4 S4

- move_code：RQ_OR_OBJECTIVE

- paraphrase_cn：因此待解决的问题是：如何处理属性相关性，如何构建ABR，以及如何在工程中扩展ABRB。

- rhetorical_function_cn：提炼三个研究问题

- depends_on_cn：句18

- sets_up_cn：为后文三小节导航

- evidence_pointer：Section 2.2 P4 S4

### 20. P1 S1

- order：20

- section：Section 3.1

- locator：P1 S1

- move_code：CONTEXT

- paraphrase_cn：两个属性之间的相关性在工程中是普遍的。

- rhetorical_function_cn：建立相关性普遍性

- depends_on_cn：无

- sets_up_cn：为相关性处理必要性铺垫

- evidence_pointer：Section 3.1 P1 S1

### 21. P5 S3

- order：21

- section：Section 3.1

- locator：P5 S3

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：根据文献，基于互信息的方法被认为具有更好的普遍性和公平性，可用于各种类型的变量。

- rhetorical_function_cn：论证选择MMI的原因

- depends_on_cn：句20

- sets_up_cn：为独立因子定义铺垫

- evidence_pointer：Section 3.1 P5 S3

### 22. Definition 1

- order：22

- section：Section 3.1

- locator：Definition 1

- move_code：THEORY_PROPOSITION

- paraphrase_cn：定义两个属性之间的相关度ψ(Xi,Xj)为归一化互信息的函数。

- rhetorical_function_cn：定义相关性度

- depends_on_cn：MMI

- sets_up_cn：为独立因子定义铺垫

- evidence_pointer：Section 3.1, after Eq.(6), Definition 1

### 23. Definition 2

- order：23

- section：Section 3.1

- locator：Definition 2

- move_code：DESIGN_FEATURE

- paraphrase_cn：定义Xi对Xj的独立因子φ_i,j为1减去相关度对熵的加权调整。

- rhetorical_function_cn：给出独立因子

- depends_on_cn：Definition 1

- sets_up_cn：为权重折扣铺垫

- evidence_pointer：Section 3.1, after Eq.(7), Definition 2

### 24. Eq.(9-a)前一句

- order：24

- section：Section 3.1

- locator：Eq.(9-a)前一句

- move_code：DESIGN_FEATURE

- paraphrase_cn：为降低Xi与Xj的弱相关性，可用独立因子对Xi的属性权重进行折扣。

- rhetorical_function_cn：具体折扣机制

- depends_on_cn：Definition 2

- sets_up_cn：为ABR中权重更新铺垫

- evidence_pointer：Section 3.1, Eq.(9-a)前一句

### 25. P1 S1

- order：25

- section：Section 3.2

- locator：P1 S1

- move_code：DESIGN_FEATURE

- paraphrase_cn：假设有T个属性，每个属性有M_i个参考值，则第i个属性的第m条ABR规则形式为“若Xi是A_i,m，则结果信念分布...，带有规则权重和折扣属性权重”。

- rhetorical_function_cn：正式定义ABR规则结构

- depends_on_cn：相关性处理

- sets_up_cn：为推理过程铺垫

- evidence_pointer：Section 3.2, Eq.(10)

### 26. P2 S1

- order：26

- section：Section 3.2

- locator：P2 S1

- move_code：DESIGN_FEATURE

- paraphrase_cn：输入数据Xi先转化为信念分布，再计算与规则的匹配度，其中使用归一化折扣属性权重。

- rhetorical_function_cn：描述输入转换和匹配度计算

- depends_on_cn：ABR定义

- sets_up_cn：为ER推理铺垫

- evidence_pointer：Section 3.2, after Eq.(10)

### 27. Remark 1

- order：27

- section：Section 3.2

- locator：Remark 1

- move_code：BOUNDARY_CONDITION

- paraphrase_cn：ABR实际上是单输入规则，是原始信念规则的特例；ABR不旨在替代原始规则，而是复杂系统建模的一种备选。

- rhetorical_function_cn：澄清ABR定位

- depends_on_cn：ABR定义

- sets_up_cn：防止误解

- evidence_pointer：Section 3.2, Remark 1

### 28. Theorem 1

- order：28

- section：Section 3.3

- locator：Theorem 1

- move_code：HYPOTHESIS_OR_PROPOSITION

- paraphrase_cn：万能逼近定理：对任意连续函数和任意ε>0，存在ABRB模型使误差上界不超过ε。

- rhetorical_function_cn：提出待证性质

- depends_on_cn：ABRB输出函数形式

- sets_up_cn：为证明搭建框架

- evidence_pointer：Section 3.3, Theorem 1

### 29. Theorem 2

- order：29

- section：Section 3.3

- locator：Theorem 2

- move_code：THEORY_INTRO

- paraphrase_cn：Stone-Weierstrass定理给出紧致域上连续函数集合的充分条件。

- rhetorical_function_cn：引入证明工具

- depends_on_cn：Theorem 1

- sets_up_cn：用于证明Theorem 1

- evidence_pointer：Section 3.3, Theorem 2

### 30. 末尾

- order：30

- section：Section 3.3

- locator：末尾

- move_code：RESULT

- paraphrase_cn：基于上述分析，可得出结论：ABRB模型与BRB模型具有相同的万能逼近能力。

- rhetorical_function_cn：报告理论结果

- depends_on_cn：证明过程

- sets_up_cn：为后续实际性能评价提供理论前提

- evidence_pointer：Section 3.3末尾

### 31. P1 S1

- order：31

- section：Section 3.4

- locator：P1 S1

- move_code：CONTEXT

- paraphrase_cn：由于专家知识有限，ABRB初始参数应使用观测数据进一步微调。

- rhetorical_function_cn：引出优化必要性

- depends_on_cn：实际应用需求

- sets_up_cn：为优化方程铺垫

- evidence_pointer：Section 3.4 P1 S1

### 32. P1 S1

- order：32

- section：Section 4

- locator：P1 S1

- move_code：CONTEXT

- paraphrase_cn：真实系统的先验知识在长期实践中逐步积累。

- rhetorical_function_cn：说明扩展需求背景

- depends_on_cn：长期应用

- sets_up_cn：为扩展方法铺垫

- evidence_pointer：Section 4 P1 S1

### 33. P3 S1

- order：33

- section：Section 4.1

- locator：P3 S1

- move_code：MECHANISM

- paraphrase_cn：在ABRB中每个属性对应一系列ABR，每个参考值对应一条ABR，因此调整属性或参考值数量可视为调整规则数量。

- rhetorical_function_cn：解释ABRB可扩展的机制

- depends_on_cn：ABR结构

- sets_up_cn：为扩展公式铺垫

- evidence_pointer：Section 4.1 P3 S1

### 34. P5 S1

- order：34

- section：Section 4.2

- locator：P5 S1

- move_code：DESIGN_FEATURE

- paraphrase_cn：因此可基于传统D-S规则开发信念重分配方法。

- rhetorical_function_cn：给出FoD扩展方法

- depends_on_cn：前一句FoD新状态含义

- sets_up_cn：为Belief重分配公式铺垫

- evidence_pointer：Section 4.2 P5 S1

### 35. P1 S1

- order：35

- section：Section 5

- locator：P1 S1

- move_code：PRACTICAL_STAKES

- paraphrase_cn：锂电池是航天器电源系统的关键部件，其健康状态直接影响航天器运行。

- rhetorical_function_cn：说明案例重要性

- depends_on_cn：无

- sets_up_cn：为案例引入动机

- evidence_pointer：Section 5 P1 S1

### 36. P4 S3

- order：36

- section：Section 5

- locator：P4 S3

- move_code：RQ_OR_OBJECTIVE

- paraphrase_cn：因此有必要建立观测特征与容量之间的可解释关系。

- rhetorical_function_cn：提出案例具体目标

- depends_on_cn：LPB观测限制

- sets_up_cn：为ABRB应用铺垫

- evidence_pointer：Section 5 P4 S3

### 37. P3 S1

- order：37

- section：Section 5.1

- locator：P3 S1

- move_code：DESIGN_FEATURE

- paraphrase_cn：根据工程应用，容量高于98%为完全安全(CS)，降到85%为安全(S)，75%为较差(LB)，60%为很差(VB)需更换。

- rhetorical_function_cn：定义识别框架

- depends_on_cn：专家知识

- sets_up_cn：为初始规则表4铺垫

- evidence_pointer：Section 5.1 P3 S1

### 38. P3 S5

- order：38

- section：Section 5.2

- locator：P3 S5

- move_code：RESULT

- paraphrase_cn：优化后ABRB的信念分布与初始ABRB接近，表明参数是局部优化。

- rhetorical_function_cn：报告优化局部性

- depends_on_cn：图3

- sets_up_cn：为可解释性主张铺垫

- evidence_pointer：Section 5.2 P3 S5

### 39. P4 S1

- order：39

- section：Section 5.2

- locator：P4 S1

- move_code：RESULT

- paraphrase_cn：优化后ABRB的MSE为1.04E-4，满足工程精度要求。

- rhetorical_function_cn：报告核心精度结果

- depends_on_cn：训练

- sets_up_cn：为后续对比铺垫

- evidence_pointer：Section 5.2 P4 S1

### 40. P1 S1

- order：40

- section：Section 5.3

- locator：P1 S1

- move_code：BENCHMARK_OR_CONTRAST

- paraphrase_cn：为验证ABRB有效性，实施了与BRB、BPNN、ELM、FRB的对比研究。

- rhetorical_function_cn：建立基准比较

- depends_on_cn：之前的ABRB结果

- sets_up_cn：为展示相对优势铺垫

- evidence_pointer：Section 5.3 P1 S1

### 41. P2 S4

- order：41

- section：Section 5.3

- locator：P2 S4

- move_code：RESULT

- paraphrase_cn：在有限数据样本下，ABRB在复杂系统建模方面的性能优于BPNN。

- rhetorical_function_cn：报告小样本优势

- depends_on_cn：表7

- sets_up_cn：为专家知识价值铺垫

- evidence_pointer：Section 5.3 P2 S4

### 42. Remark 6

- order：42

- section：Section 5.3

- locator：Remark 6

- move_code：LIMITATION_AND_FUTURE

- paraphrase_cn：训练集随机选自全数据集可能导致对ABRB的有偏评估，但该划分对所有模型公平。

- rhetorical_function_cn：承认评估偏置

- depends_on_cn：训练测试设计

- sets_up_cn：为补充分析铺垫

- evidence_pointer：Section 5.3, Remark 6

### 43. P4 S1

- order：43

- section：Section 5.4

- locator：P4 S1

- move_code：METHOD

- paraphrase_cn：在ABRB中，新增规则可单独使用P-CMA-ES优化。

- rhetorical_function_cn：描述扩展训练方式

- depends_on_cn：ABR结构

- sets_up_cn：为扩展结果铺垫

- evidence_pointer：Section 5.4 P4 S1

### 44. P6 S1

- order：44

- section：Section 5.4

- locator：P6 S1

- move_code：LIMITATION

- paraphrase_cn：但扩展后的ABRB MSE为2.6E-4，大于优化ABRB但小于初始ABRB，这表明扩展是二次处理并引入了误差。

- rhetorical_function_cn：报告扩展代价

- depends_on_cn：表12

- sets_up_cn：为复杂扩展未来研究铺垫

- evidence_pointer：Section 5.4 P6 S1

### 45. P1 S1

- order：45

- section：Section 5.5

- locator：P1 S1

- move_code：CONTRIBUTION

- paraphrase_cn：ABRB模型的可解释性体现在建立、优化、扩展和输出四个方面。

- rhetorical_function_cn：总结可解释性

- depends_on_cn：前文所有结果

- sets_up_cn：为结论贡献铺垫

- evidence_pointer：Section 5.5 P1 S1

### 46. P2 S1

- order：46

- section：Conclusion

- locator：P2 S1

- move_code：CONTRIBUTION

- paraphrase_cn：主要贡献有三：提出近似置信规则并通过折扣权重处理相关性，证明ABRB的万能逼近能力，提出关键组件的扩展方法。

- rhetorical_function_cn：列出贡献

- depends_on_cn：全文

- sets_up_cn：为未来研究铺垫

- evidence_pointer：Conclusion P2 S1

### 47. P3 S4

- order：47

- section：Conclusion

- locator：P3 S4

- move_code：LIMITATION_AND_FUTURE

- paraphrase_cn：本文仍有局限：需研究更多降低属性相关性的技术，复杂情况下的ABRB扩展也应进一步研究。

- rhetorical_function_cn：承认局限并展望

- depends_on_cn：本文边界

- sets_up_cn：为未来工作铺垫

- evidence_pointer：Conclusion P3 S4

## 写作技术

- gap_construction_cn：先确立专家知识是BRB可解释性的核心，随后指出连接假设导致规则爆炸和弱可扩展性会阻断专家知识利用；然后分析已有解法的不足，特别是单属性规则忽略相关性，最终在“需要相关性处理”和“需要单属性结构”之间制造缺口，提出ABR。

- signposting_cn：引言末尾预告章节安排；每节开头明确小节任务（如2.1简介、2.2问题形式化）；在3.2明确“本节分为三小节”；案例部分有清晰的子节标题。文末用Remark补充边界。

- transition_logic_cn：先由BRB问题形式化引出三个待解决问题；再逐节解决；每个Study之间通过“尚未解决的问题”过渡：理论后接优化，优化后接扩展，扩展后接案例，案例内部先初建再对比再扩展。

- claim_evidence_rhythm_cn：在提出主张后立即用公式、定理、表格或图佐证。例如，规则爆炸用L1公式；逼近能力用SW证明；实际性能用MSE表和曲线；扩展性用表12和图6。在结果后附解释（“The reason may be...”）来连接结果和机制。

- benchmark_narrative_cn：将BRB作为主要基线，因为ABRB是其变体；FRB作为传统模糊系统，BPNN/ELM作为数据驱动黑箱代表；小样本对比用于展示专家知识带来的优势；扩展前后对比展示可扩展设计。

- theory_return_cn：证明ABRB满足SW定理后，在结论中又回到BRB理论：“具有相同万能逼近能力”，并将可扩展性提升为“长期价值维持”的一般议题。

- contribution_positioning_cn：在引言、结论和摘要中重复主要贡献三点：ABR规则设计、万能逼近证明、扩展方法；并强调这是构造大规模可解释专家系统的新思路。

- novelty_protection_cn：通过理论证明将ABRB与成熟BRB的能力绑定，避免被认为只是一个工程简化；同时强调紧凑性和可扩展性是BRB无法实现的，用案例和扩展演示证明其额外价值；用Remark 1澄清ABR不是替代而是备选，降低攻击面。

## 可复用研究与写作程序

### structure_steps

#### 1. 1

- step：1

- writing_job_cn：建立问题域和知识基础：说明现有专家系统（BRB）的价值和局限。

- research_job_cn：形式化规则爆炸和弱可扩展性。

- required_evidence_cn：公式或示例展示指数增长和重设计成本。

- transition_to_next_cn：指出解决单属性规则时忽略相关性的缺口，引出新规则。

#### 2. 2

- step：2

- writing_job_cn：设计制品核心机制：定义新规则和相关性处理机制。

- research_job_cn：提出ABR规则、独立因子、推理流程。

- required_evidence_cn：清晰规则定义和公式。

- transition_to_next_cn：需要证明新制品不损失能力，从而引入理论。

#### 3. 3

- step：3

- writing_job_cn：理论验证：证明新制品与baseline在能力上等价。

- research_job_cn：运用Stone-Weierstrass定理证明万能逼近。

- required_evidence_cn：严格的定理和证明。

- transition_to_next_cn：理论能力不等于实际性能，需要案例。

#### 4. 4

- step：4

- writing_job_cn：讨论扩展性设计：说明如何随时间扩展。

- research_job_cn：设计属性/参考值/FoD扩展公式。

- required_evidence_cn：公式和机制。

- transition_to_next_cn：用案例验证扩展方法。

#### 5. 5

- step：5

- writing_job_cn：案例实施与评价：构建实际应用场景，展示构建、优化、对比、扩展全过程。

- research_job_cn：在真实数据集上训练ABRB并比较。

- required_evidence_cn：数据集、表格、图、MSE。

- transition_to_next_cn：结果解释和可解释性总结。

#### 6. 6

- step：6

- writing_job_cn：总结贡献和边界：重申解决缺口和贡献，指出局限。

- research_job_cn：提炼设计知识和未来方向。

- required_evidence_cn：验证结果。

- transition_to_next_cn：强调长期价值和未来研究。

### most_transferable_moves_cn

1. 从核心问题（规则爆炸/可扩展性）出发，给出形式化规模公式（L1=∏Mi vs L2=∑Mi）

2. 在提出新规则后立即用理论证明其等价能力

3. 用案例和对比实验展示紧凑性和小样本优势

4. 在扩展中演示“无需重设计”的增量机制

5. 用Remark标明边界条件（如强/弱相关性、扩展误差）

### resource_intensive_or_nonstandard_parts_cn

1. 需要特定领域数据（NASA LPB实验数据）和领域知识来设定初始规则

2. 需要专家提供初始信念度、参考值、γ概率等，非公开数据不可轻易复制

3. 优化依赖P-CMA-ES等算法和人工设定迭代次数

4. 需要用Stone-Weierstrass定理进行严格证明，需要数学背景

5. 案例中的扩展验证依赖长期实践知识（如LPB退化模式），无法通用化

### what_not_to_copy_superficially_cn

1. 不能只模仿“单属性规则”表面结构而忽略独立因子和相关性处理，否则精度可能下降

2. 不能只写“可扩展”而不提供局部更新公式和验证，否则沦为口号

3. 不能只宣称“可解释”而没有信念分布/图/约束等实证

4. 不能把万能逼近证明当作工程性能保证，证明没有考虑有限数据和噪声

5. 不能照搬“随机选取50%训练并全数据测试”的分割方式而不讨论偏置

- single_best_description_of_the_routine_cn：用单属性规则加独立因子构建紧凑可扩展的专家系统，并用万能逼近理论、真实案例和增长性扩展演示证明其能力不降、知识可利用、长期可维护。

## 分析边界

文章为PDF文本转换，部分数学符号和图片标记可能不完整，但结构和关键信息基本清晰；案例研究仅一个数据集，可能限制外部有效性判断；本文未阅读附录（如果有），但基于正文分析。
