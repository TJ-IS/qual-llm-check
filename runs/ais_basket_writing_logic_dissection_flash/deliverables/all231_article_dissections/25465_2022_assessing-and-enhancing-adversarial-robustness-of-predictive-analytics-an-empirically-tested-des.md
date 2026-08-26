# Assessing and Enhancing Adversarial Robustness of Predictive Analytics: An Empirically Tested Design Framework

- 作者：Weifeng Li; Yidong Chai
- 年份 / 期刊：2022 / Journal of Management Information Systems
- DOI：10.1080/07421222.2022.2063549
- 源文件：25465_2022_assessing-and-enhancing-adversarial-robustness-of-predictive-analytics-an-empirically-tested-des.md
- 论文主类型：build_evaluate_design_science
- 主导写作弧线：requirements_build_evaluate_design_principles
- 置信度：0.7

## 文章级论证概况

- 核心问题：如何评估并增强预测分析应用对对抗性攻击（尤其是黑盒探索性攻击）的鲁棒性？

- 制品与设计：ARText系统：以技术威胁规避理论（TTAT）为内核理论，形成两个元需求——对抗鲁棒性评估（性能比率、性能-扰动曲线）和对抗鲁棒性增强（装袋集成学习、迭代对抗重训练），并实例化为文本分类系统。

- 客观结果：在垃圾评论与垃圾邮件两个测试床上，所有基线SML模型在对抗样本下性能显著下降；ARText的集成模型在所有性能比率和性能-扰动曲线AUC指标上优于基线；加入迭代对抗重训练后，包括ARText在内的所有模型鲁棒性均提升，ARText仍保持最优，尤其召回鲁棒性提升显著。

- 核心贡献：提出了一个以TTAT为内核理论、包含评估和增强两个元需求的设计框架，并通过ARText系统完成实例化与实验验证，从而扩展预测分析评估维度、回答黑盒对抗鲁棒性的评估与增强问题，并贡献于AI治理、预测分析文献和设计知识。

- 整篇论证链：文章从SML预测分析在关键决策中的普及和ERM分布假设在对抗输入下失效出发，指出IS文献忽略了预测模型安全威胁、评估仍以预测性能为主、已有防御局限于SVM白盒和理性代理假设，由此设置'如何评估'和'如何增强'两个研究问题。作者借用TTAT的威胁评估与威胁应对组件，转化出对抗鲁棒性评估与增强两个元需求；评估元需求进一步变成性能比率和性能-扰动曲线测量，增强元需求变成装袋集成学习和迭代对抗重训练。ARText作为框架实例化，在垃圾评论和垃圾邮件两个测试床上与九种基线模型进行两轮评估：第一轮证明基线模型脆弱且新指标能区分鲁棒性差异；第二轮证明集成学习和对抗重训练分别且联合提升鲁棒性。讨论和结论部分将实验结果上升为设计原则和可复用知识，回扣引言中提出的缺口，并给出AI治理、预测分析评估和设计框架三层贡献。

## 类型与写作弧线判定

- 论文主类型判定：文章遵循设计科学范式：从文献和TTAT推导元需求与设计原则，开发ARText制品，并用实验评估各组件效用与有效性。研究的主要贡献不是检验理论假设，而是提出并验证可复用的设计框架。

- 主导写作弧线判定：写作主线是TTAT风险应对逻辑生成两个元需求，将元需求转化为具体设计原则与系统特征，随后通过实验评价，最终在讨论中总结为面向预测分析的设计原则和边界条件。

## 研究开展程序

- study_or_phase_count：6

- 研究阶段总序列：研究先进行理论框架推导，再进行系统实例化，然后按组件分别评价：评估组件用两个实验证明基线脆弱并验证测量工具；增强组件用两个实验分别验证集成学习和对抗重训练。各阶段之间存在明确累积关系：框架给出结构，系统将结构具体化，评估实验为增强实验建立基线和问题重要性，增强实验反过来验证框架设计原则。

### studies_or_phases

#### 1. 框架推导阶段（TTAT元需求）

- order：1

- name_cn：框架推导阶段（TTAT元需求）

- question_cn：面对黑盒探索性攻击，预测分析应用应如何系统地评估和增强对抗鲁棒性？

- inputs_and_setting_cn：IS预测分析文献、对抗攻击与防御文献、TTAT理论

- designed_or_compared_object_cn：两个元需求：对抗鲁棒性评估与对抗鲁棒性增强

- baseline_control_or_counterfactual_cn：现有以预测性能为主评估、攻击特定防御、SVM白盒、理性代理假设

##### objective_metrics

（空）

- analysis_method_cn：理论演绎、设计科学元需求推导

- main_result_cn：提出以TTAT威胁评估/威胁应对映射的评估-增强框架

- argumentative_role_cn：为后续系统设计和评价提供总体结构

- remaining_uncertainty_cn：元需求尚未转化为可运行制品，也没有实证证据

- link_to_next_phase_cn：需要实例化和具体化评估测量与增强技术

##### evidence_pointers

1. Figure 1

2. Framework section

#### 2. ARText系统设计与构建阶段

- order：2

- name_cn：ARText系统设计与构建阶段

- question_cn：如何在文本分类任务中实现评估与增强两个元需求？

- inputs_and_setting_cn：文本分类应用、DeepWordBug生成器、常用文本分类模型、ERM与对抗重训练形式化

- designed_or_compared_object_cn：性能比率与性能-扰动曲线测量；装袋集成模型与迭代对抗重训练算法

- baseline_control_or_counterfactual_cn：无对抗重训练的单模型基线；仅用绝对预测性能的测量

##### objective_metrics

（空）

- analysis_method_cn：算法设计与形式化推导

- main_result_cn：构建ARText系统，包含评估模块和增强模块

- argumentative_role_cn：将抽象的元需求转成可评价的制品

- remaining_uncertainty_cn：系统的效用和有效性尚未经过数据验证

- link_to_next_phase_cn：需要用实验分别验证评估组件和增强组件

##### evidence_pointers

1. Figure 2

2. Figure 3

3. System Design section

#### 3. Evaluation 1 Experiment 1：性能比率鲁棒性测量

- order：3

- name_cn：Evaluation 1 Experiment 1：性能比率鲁棒性测量

- question_cn：性能比率指标能否揭示基线SML模型在对抗样本下的鲁棒性差异？

- inputs_and_setting_cn：均衡垃圾评论数据集（800/800）、非均衡垃圾邮件数据集（2500/500）；9个基线SML模型；DeepWordBug生成10%扰动幅度的对抗样本；5折交叉验证

- designed_or_compared_object_cn：非对抗测试集 vs 混合对抗测试集；不同基线模型的性能比率

- baseline_control_or_counterfactual_cn：非对抗原始测试集作为自身基线；各基线模型互比

##### objective_metrics

1. R_A

2. R_P

3. R_R

4. R_F

5. R_ROC

- analysis_method_cn：描述性对比和表格报告

- main_result_cn：所有基线模型在对抗样本下性能下降；没有模型天然鲁棒；NB在均衡垃圾评论上鲁棒性最高，10%扰动可削弱最佳性能4%-29%

- argumentative_role_cn：证明评估组件有用，同时说明预测分析部署面临实际风险

- remaining_uncertainty_cn：单一扰动范围无法反映跨扰动范围的鲁棒性

- link_to_next_phase_cn：引出Experiment 2用性能-扰动曲线覆盖多个扰动范围

##### evidence_pointers

1. Figure 4

2. Table 3

3. Experiment 1

#### 4. Evaluation 1 Experiment 2：性能-扰动曲线鲁棒性测量

- order：4

- name_cn：Evaluation 1 Experiment 2：性能-扰动曲线鲁棒性测量

- question_cn：性能-扰动曲线能否刻画预测模型在不同扰动范围下的鲁棒性？

- inputs_and_setting_cn：相同垃圾评论/垃圾邮件测试床和基线模型；扰动范围从0到1；对五个文本分类指标计算AUC

- designed_or_compared_object_cn：RF与CNN的召回-扰动曲线示例；所有基线的A/P AUC、P/P AUC、R/P AUC、F/P AUC、ROC/P AUC

- baseline_control_or_counterfactual_cn：扰动水平0作为无对抗状态；基线模型之间互比

##### objective_metrics

1. A/P AUC

2. P/P AUC

3. R/P AUC

4. F/P AUC

5. ROC/P AUC

- analysis_method_cn：曲线比较与AUC汇总

- main_result_cn：CNN在均衡垃圾评论上AUC最优；NB只在单点性能比率好但跨范围不强；各模型R/P AUC普遍低于P/P AUC，说明对抗样本主要引发第二类错误

- argumentative_role_cn：验证综合鲁棒性测量工具，进一步支持评估元需求

- remaining_uncertainty_cn：评估只是刻画脆弱性，尚未证明增强措施有效

- link_to_next_phase_cn：进入Evaluation 2测试增强组件

##### evidence_pointers

1. Figure 5

2. Table 4

3. Experiment 2

#### 5. Evaluation 2 Experiment 3：装袋集成学习的鲁棒性增强

- order：5

- name_cn：Evaluation 2 Experiment 3：装袋集成学习的鲁棒性增强

- question_cn：基于多样化策略的装袋集成能否提升文本分类模型对对抗攻击的鲁棒性？

- inputs_and_setting_cn：相同测试床、相同基线集合；ARText集成模型；对抗样本由与集成同构成的替代模型通过DeepWordBug生成

- designed_or_compared_object_cn：ARText集成模型 vs 9个基线单模型

- baseline_control_or_counterfactual_cn：单个传统和深度SML模型；与评估1相同的攻击设定

##### objective_metrics

1. 性能比率（R_A, R_P, R_R, R_F, R_ROC）

2. 性能-扰动曲线AUC（A/P AUC, P/P AUC, R/P AUC, F/P AUC, ROC/P AUC）

- analysis_method_cn：表格对比与结果解释

- main_result_cn：集成模型在两个测试床上所有性能比率和AUC指标上都优于基线；在垃圾评论上准确率鲁棒性提升0.071、F鲁棒性提升0.104、R/P AUC提升0.359

- argumentative_role_cn：验证增强元需求中的第一个设计原则

- remaining_uncertainty_cn：还需要验证训练过程的改进（对抗重训练）是否进一步有效

- link_to_next_phase_cn：Experiment 4在集成和基线上加入迭代对抗重训练

##### evidence_pointers

1. Table 5

2. Table 6

3. Experiment 3

#### 6. Evaluation 2 Experiment 4：迭代对抗重训练的鲁棒性增强

- order：6

- name_cn：Evaluation 2 Experiment 4：迭代对抗重训练的鲁棒性增强

- question_cn：迭代对抗重训练能否进一步提升鲁棒性？与集成学习联合是否最优？

- inputs_and_setting_cn：相同测试床；对ARText和所有基线模型应用迭代对抗重训练；每轮将DeepWordBug生成的对抗垃圾样本与原始垃圾样本混合；迭代上限100或提前收敛

- designed_or_compared_object_cn：各模型重训练前后；重训练后的ARText vs 重训练后的基线

- baseline_control_or_counterfactual_cn：各模型未重训练版本；以自身前后对比为主

##### objective_metrics

1. 性能比率改进百分比

2. 性能-扰动曲线AUC改进百分比

- analysis_method_cn：前后对比和跨模型对比

- main_result_cn：所有模型重训练后鲁棒性提升；ARText仍最高；垃圾评论召回鲁棒性提升29.11%，垃圾邮件提升26.27%；R/P AUC提升27%和82%，说明重训练显著降低第二类错误

- argumentative_role_cn：验证第二个设计原则，并证明集成学习可进一步增益对抗重训练

- remaining_uncertainty_cn：主文未详细报告在线附录中的迁移/查询攻击敏感性分析结果；未报告计算成本

- link_to_next_phase_cn：讨论和结论将实验结果上升为设计原则和贡献

##### evidence_pointers

1. Figure 6

2. Figure 7

3. Table 7

4. Table 8

5. Experiment 4

## 各部分修辞架构

### abstract_moves

1. CONTEXT: 预测分析在关键决策中广泛使用SML模型

2. PRACTICAL_STAKES: 对手有动力利用漏洞误导决策

3. GAP: 预测分析缺乏原则性的鲁棒性评估与增强技术

4. RQ_OR_OBJECTIVE: 以TTAT为内核提出框架并实例化ARText

5. STUDY_OVERVIEW: 在垃圾评论和垃圾邮件上评估系统

6. RESULT: 框架显著增强对抗鲁棒性

### introduction_moves

1. CONTEXT: 大数据和机器学习推动预测分析进入关键决策

2. PHENOMENON: 垃圾评论、垃圾邮件、欺诈、信用审批等具体应用场景

3. PRACTICAL_STAKES: 对抗攻击会造成声誉和财务损失

4. GAP: IS研究未充分认识威胁、评估局限于预测性能、部署脆弱

5. RQ_OR_OBJECTIVE: 提出两个研究问题

6. THEORY_INTRO: 引入TTAT作为内核理论

7. STUDY_OVERVIEW: 预告框架、ARText和两轮评价

### theory_and_knowledge_moves

1. THEORY_INTRO: 统计学习理论与ERM定义

2. MECHANISM: ERM的独立同分布假设在策略性输入下失效

3. PRIOR_KNOWLEDGE: 攻击分为causative和exploratory，exploratory更贴近应用

4. PRIOR_KNOWLEDGE: 白盒与黑盒攻击的具体分类

5. PRIOR_KNOWLEDGE: IS防御以principal-agent模型为主

6. GAP: 既有防御限于SVM、白盒和理性代理假设

7. THEORY_INTRO: TTAT威胁评估与威胁应对

8. REQUIREMENT: 威胁评估映射为鲁棒性评估元需求，威胁应对映射为鲁棒性增强元需求

### artifact_design_moves

1. DESIGN_FEATURE: ARText总体结构

2. METHOD_JUSTIFICATION: 用多样替代模型和DeepWordBug生成对抗文本

3. DESIGN_FEATURE: 性能比率采用相对性能而非绝对性能

4. DESIGN_FEATURE: 性能-扰动曲线捕捉扰动范围与性能的权衡

5. DESIGN_FEATURE: 装袋集成降低过拟合和攻击成功率

6. DESIGN_FEATURE: 迭代对抗重训练在目标函数中显式建模对抗风险

7. CONTRIBUTION: 技术新颖性三方面

### evaluation_moves

1. STUDY_OVERVIEW: 参照Hevner设计科学评价，分Evaluation1/2

2. BENCHMARK_OR_CONTRAST: 两个测试床、九种基线、5折交叉验证

3. METHOD_JUSTIFICATION: 对抗测试集由DeepWordBug生成

4. RESULT: 图4和图3显示基线全下降

5. RESULT: 表3和表4报告鲁棒性排名

6. METHOD_JUSTIFICATION: 集成模型用同构成替代模型生成对抗样本

7. RESULT: 表5/6显示集成全面领先

8. RESULT: 表7/8显示重训练前后改进

9. STUDY_OVERVIEW: 提到在线附录的迁移/查询攻击敏感性分析

### discussion_and_contribution_moves

1. RESULT: 总结两轮评价结果

2. CONTRIBUTION: 对抗鲁棒性应成为评估一部分

3. BOUNDARY_CONDITION: 性能比率适合固定扰动范围，曲线适合无界范围

4. CONTRIBUTION: 集成学习和对抗重训练是可复用设计原则

5. CONTRIBUTION: 对AI治理、预测分析文献和设计研究的三层贡献

6. LIMITATION_AND_FUTURE: 计算成本、特征工程、扰动度量局限

## 理论/知识到设计的翻译

### 知识/理论基础

1. Technology Threat Avoidance Theory (TTAT)

2. Statistical learning theory / empirical risk minimization (ERM)

3. Adversarial machine learning (causative vs exploratory; white-box vs black-box; transferability and query-based attacks)

4. Performance-based and perturbation-based adversarial robustness measures

5. Ensemble learning / diversification

6. Adversarial retraining / adversarial risk

- 理论—设计耦合：partial

- 耦合判定理由：TTAT为框架提供了总体的二分类元需求结构（威胁评估→鲁棒性评估，威胁应对→鲁棒性增强），但具体测量公式、集成方法、对抗重训练算法和DeepWordBug选择主要来自机器学习安全文献和工程实践，并非由TTAT演绎而来。文章也没有检验TTAT的理论命题。

- 理论到设计翻译链：TTAT威胁评估组件 → 元需求1：对抗鲁棒性评估 → 评估两步法（对抗样本生成+鲁棒性测量） → 性能比率和性能-扰动曲线；TTAT威胁应对组件 → 元需求2：对抗鲁棒性增强 → 设计原则1装袋集成（多样化策略）与设计原则2迭代对抗重训练（显式建模对抗风险） → ARText系统实现。同时，ERM分布假设在策略性输入下失效构成整个翻译过程的逻辑底座：评估用于揭示该失效，增强用于弥补该失效。

### mapping_table

#### 1. 1

- theory_or_knowledge_claim_cn：TTAT威胁评估主张系统易感性和负面后果需要被评估

- mechanism_cn：通过量化对抗攻击造成的性能损失来判断模型脆弱性

- design_requirement_cn：预测分析应用应实施对抗鲁棒性评估

- artifact_choice_cn：两步评估：DeepWordBug生成对抗样本；性能比率和性能-扰动曲线测量

- evaluated_contrast_cn：非对抗测试集 vs 混合对抗测试集；基线模型之间互比

- objective_result_cn：所有基线模型在对抗样本下性能下降，NB/CNN等鲁棒性排名不同，确认评估有用

##### evidence_pointers

1. Figure 4

2. Table 3

3. Table 4

#### 2. 2

- theory_or_knowledge_claim_cn：TTAT威胁应对主张需要采取措施规避IT威胁

- mechanism_cn：多样化降低相关性失败风险，使对抗样本必须同时欺骗多数模型

- design_requirement_cn：预测分析应用应增强底层SML模型的韧性

- artifact_choice_cn：装袋集成学习（Bagging ensemble）

- evaluated_contrast_cn：ARText集成模型 vs 9个基线单模型

- objective_result_cn：集成模型在两个测试床上所有鲁棒性指标均优于基线

##### evidence_pointers

1. Table 5

2. Table 6

3. Experiment 3

#### 3. 3

- theory_or_knowledge_claim_cn：对抗重训练将对抗风险显式加入ERM目标函数

- mechanism_cn：训练集中的对抗样本对应目标函数中的对抗损失项，可权衡预测性能与鲁棒性

- design_requirement_cn：在训练过程中引入对抗样本而不是只改变模型结构

- artifact_choice_cn：迭代对抗重训练算法（Figure 3）

- evaluated_contrast_cn：各模型重训练前后；ARText与重训练后的基线

- objective_result_cn：所有模型鲁棒性提升，ARText仍最优，召回类AUC提升尤其显著

##### evidence_pointers

1. Figure 3

2. Figure 6

3. Figure 7

4. Table 7

5. Table 8

#### 4. 4

- theory_or_knowledge_claim_cn：黑盒转移性攻击显示对抗样本可以在替代模型和目标模型间迁移

- mechanism_cn：攻击者用替代模型近似目标模型，生成对抗样本再攻击目标

- design_requirement_cn：评估和增强需要模拟黑盒攻击，并提高对替代模型迁移的抵抗

- artifact_choice_cn：ARText在评估与重训练中使用由多种文本分类器组成的替代模型集合和DeepWordBug

- evaluated_contrast_cn：同一攻击设定下ARText与基线的对比；在线附录补充迁移/查询攻击

- objective_result_cn：ARText在主评价中全面优于基线；补充分析用于展示跨攻击类型稳健性

##### evidence_pointers

1. System Design section

2. Evaluation 2 introduction

3. Online Supplemental Appendices

## 评价逻辑

### evaluation_modes

1. 非对抗 vs 混合对抗测试集对比

2. 单点扰动范围性能比率测量

3. 跨扰动范围性能-扰动曲线与AUC

4. 集成学习 vs 单基线的同条件对照

5. 迭代对抗重训练前后自身对照

6. 重训练后ARText vs 重训练后基线对照

7. 在线附录中的迁移/查询攻击敏感性分析

- why_these_evaluations_cn：文章需要同时验证框架的两个元需求：评估组件需要证明所提测量能暴露模型脆弱性并区分不同模型；增强组件需要证明设计原则确实带来鲁棒性提升。因此先做评估实验建立基线和威胁严重性，再做增强实验；每个实验都设置了能隔离对应设计贡献的对照，如非对抗/混合数据集、单模型/集成、重训练前/后。

- benchmark_and_contrast_chain_cn：所有实验共享同一组九种基线模型和两个测试床，形成统一比较框架。评估1用非对抗和混合对抗测试集的性能差异说明基线脆弱；评估2将ARText与同一组基线对比，证明集成有效；随后在自身模型上叠加迭代重训练，以before-after对照证明重训练有效，并进一步显示ARText在重训练后仍优于重训练后的基线，从而将两个设计原则连接起来。攻击生成器固定为DeepWordBug，扰动范围与已有文献保持一致，增强了可比性。

### claim_evidence_ledger

#### 1. 技术主张：ARText在对抗鲁棒性指标上优于现有基线模型

- claim_cn：技术主张：ARText在对抗鲁棒性指标上优于现有基线模型

- evidence_cn：性能比率表（Table 5）和性能-扰动曲线AUC表（Table 6）显示ARText集成模型在两个测试床上全面优于9个基线

#### 2. 制品主张：集成学习和对抗重训练各自是有效的鲁棒性增强设计

- claim_cn：制品主张：集成学习和对抗重训练各自是有效的鲁棒性增强设计

- evidence_cn：Experiment 3对比集成与单基线；Experiment 4对所有模型进行重训练前后对比，表7/8显示改进

#### 3. 机制主张：多样化使攻击者必须同时欺骗多数模型，重训练显式建模对抗风险

- claim_cn：机制主张：多样化使攻击者必须同时欺骗多数模型，重训练显式建模对抗风险

- evidence_cn：实验结果是支持性证据，但文章没有直接观测攻击者替代模型的搜索过程，机制主要来自理论解释

#### 4. 边界主张：框架对黑盒探索性攻击、对文本分类任务有效

- claim_cn：边界主张：框架对黑盒探索性攻击、对文本分类任务有效

- evidence_cn：两个文本测试床（均衡和非均衡）以及主评价中的模型内可迁移性攻击；在线附录补充迁移/查询攻击

#### 5. 设计知识：两个元需求和两个设计原则可复用于预测分析应用

- claim_cn：设计知识：两个元需求和两个设计原则可复用于预测分析应用

- evidence_cn：通过TTAT映射和ARText实例化获得；单个实例不支持强泛化，文章以设计科学范式呈现

#### 6. 理论贡献：扩展TTAT到AI/ML安全，并补足预测分析评估维度

- claim_cn：理论贡献：扩展TTAT到AI/ML安全，并补足预测分析评估维度

- evidence_cn：讨论和结论部分回扣文献缺口，属于理论定位而非直接实证检验

- internal_validity_strategy_cn：统一攻击生成器（DeepWordBug）、固定10%扰动与文献一致、5折交叉验证、同样的基线和测试床；混合测试集中加入非对抗样本以隔离扰动效应；重训练前后对比控制模型身份；集成模型与替代模型使用同构成，确保攻击强度可比。

- external_validity_strategy_cn：使用均衡垃圾评论和非均衡垃圾邮件两个不同任务领域；测量覆盖五种文本分类指标；框架层面用TTAT元需求为通用设计知识；在线附录对迁移性和查询型攻击做敏感性分析。

- what_is_not_actually_tested_cn：没有真实攻击者行为、没有白盒攻击主评价、没有causative/poisoning攻击、没有除文本外的其他模态、没有特征工程攻击、没有统计显著性检验、没有计算成本/组织部署评估；在线附录中的迁移/查询攻击敏感性分析在主文中未报告具体结果。

## 贡献闭环

- technical_claim_cn：在文本分类任务上，ARText的对抗鲁棒性评估与增强技术优于现有基线，尤其是性能比率和性能-扰动曲线能更好刻画鲁棒性。

- artifact_claim_cn：装袋集成学习和迭代对抗重训练是可识别且有效的设计组成；前者提供架构性防护，后者提供训练过程防护，二者联合增益最大。

- mechanism_claim_cn：集成通过多样化降低转移攻击成功率并扩大替代模型搜索空间；对抗重训练通过在目标函数中加入对抗风险项、并迭代加入成功对抗样本，降低第二类错误。机制主张主要由实验结果间接支持。

- boundary_claim_cn：框架针对黑盒探索性攻击、文本分类预测分析，尤其是输入由决策受影响个体提供的领域（垃圾评论、垃圾邮件、信用审批、招聘等）；测量可通过替换领域指标推广到其他预测分析任务。

- reusable_design_knowledge_cn：预测分析应用应把对抗鲁棒性纳入评估；评估应采用相对性能比率和扰动-性能权衡曲线；增强应优先考虑多样化集成和对抗重训练，且这些措施可叠加到已有SML模型上，不必重建系统。

- theoretical_contribution_cn：将TTAT的威胁评估/威胁应对逻辑移植到ML安全设计，为AI治理提供安全视角；同时扩展预测分析文献，把鲁棒性维度补充到传统预测性能评估中。

- how_discussion_closes_intro_gap_cn：Discussion第一条对应引言第二点缺口（评估只重预测性能），用实验中的性能下降和鲁棒性指标论证应将鲁棒性纳入评估；第二条对应如何评估（RQ1），说明两个测量各自的适用场景；第三条对应如何增强（RQ2），说明集成和重训练是可操作设计原则；结论进一步把设计结果上升到AI治理和预测分析文献贡献。

- overclaim_or_unsupported_leaps_cn：标题和摘要中的“显著增强”没有报告统计检验，属于描述性对比；从两个测试床推广到多个应用领域略显过度；声称性能比率“剔除预测性能”可能不完全成立，因为比率仍受非对抗性能水平影响；CNN鲁棒性归因于Lipschitz性质属于推测；对“首批系统”的表述难以核验。

## 句级写作动作图谱

### 1. P1 S1

- order：1

- section：Abstract

- locator：P1 S1

- move_code：CONTEXT

- paraphrase_cn：预测分析越来越依赖监督机器学习模型来支持关键决策

- rhetorical_function_cn：为全文建立应用背景

- depends_on_cn：无

- sets_up_cn：引出攻击威胁

- evidence_pointer：Abstract first sentence

### 2. P1 S2

- order：2

- section：Abstract

- locator：P1 S2

- move_code：PRACTICAL_STAKES

- paraphrase_cn：对手有动机利用SML模型的漏洞误导预测分析作出错误决策

- rhetorical_function_cn：把背景转为安全利害

- depends_on_cn：第1句

- sets_up_cn：为研究缺口提供现实理由

- evidence_pointer：Abstract second sentence

### 3. P2 S1

- order：3

- section：Abstract

- locator：P2 S1

- move_code：GAP

- paraphrase_cn：由于对这种对抗攻击的理解和认知有限，预测分析需要原则性的鲁棒性评估与增强技术

- rhetorical_function_cn：指出知识与应用缺口

- depends_on_cn：第2句

- sets_up_cn：引出TTAT框架

- evidence_pointer：Abstract continuation

### 4. P2 S2-P3

- order：4

- section：Abstract

- locator：P2 S2-P3

- move_code：STUDY_OVERVIEW

- paraphrase_cn：本文以TTAT为内核理论提出框架，并开发ARText系统进行实验评估

- rhetorical_function_cn：预告研究贡献和方法

- depends_on_cn：第3句

- sets_up_cn：给出全文路线图

- evidence_pointer：Abstract final part

### 5. P1 S1

- order：5

- section：Introduction

- locator：P1 S1

- move_code：CONTEXT

- paraphrase_cn：机器学习进展和大数据推动组织将预测分析用于关键决策

- rhetorical_function_cn：引入研究背景

- depends_on_cn：无

- sets_up_cn：列举应用领域

- evidence_pointer：Introduction P1 S1

### 6. P1 S2-S5

- order：6

- section：Introduction

- locator：P1 S2-S5

- move_code：PHENOMENON

- paraphrase_cn：评论平台、邮箱服务、移动应用、金融、HR、医疗等都在用SML做预测

- rhetorical_function_cn：展示预测分析应用的广度和现实性

- depends_on_cn：第5句

- sets_up_cn：表明攻击面非常广

- evidence_pointer：Introduction P1 examples

### 7. P2 S1-S3

- order：7

- section：Introduction

- locator：P2 S1-S3

- move_code：PRACTICAL_STAKES

- paraphrase_cn：对抗攻击通过微扰输入诱导错误决策，可能带来声誉和财务损失

- rhetorical_function_cn：从应用背景转入威胁后果

- depends_on_cn：第6句

- sets_up_cn：提出核心现象和研究动机

- evidence_pointer：Introduction P2

### 8. P2 S4-S5

- order：8

- section：Introduction

- locator：P2 S4-S5

- move_code：PHENOMENON

- paraphrase_cn：垃圾评论可被修改以绕过检测，垃圾邮件可被设计以欺骗过滤系统

- rhetorical_function_cn：把威胁落到后续实验任务上

- depends_on_cn：第7句

- sets_up_cn：为垃圾评论/邮件testbeds埋伏笔

- evidence_pointer：Introduction P2

### 9. P3 S1

- order：9

- section：Introduction

- locator：P3 S1

- move_code：GAP

- paraphrase_cn：漏洞虽已受关注，但预测分析新兴应用仍需从三个原因深入研究

- rhetorical_function_cn：设置三个层次的缺口

- depends_on_cn：第7句

- sets_up_cn：展开IS文献缺口

- evidence_pointer：Introduction P3

### 10. P3 S2

- order：10

- section：Introduction

- locator：P3 S2

- move_code：LIMITATION

- paraphrase_cn：IS预测分析文献没有充分承认SML模型面临的潜在安全威胁，缺少处理不可靠输入的指南

- rhetorical_function_cn：第一个缺口：文献意识不足

- depends_on_cn：第9句

- sets_up_cn：强调需要在IS研究中处理

- evidence_pointer：Introduction P3 reason 1

### 11. P3 S3

- order：11

- section：Introduction

- locator：P3 S3

- move_code：LIMITATION

- paraphrase_cn：IS文献主要评估预测性能如准确率，系统评估对抗鲁棒性被忽视

- rhetorical_function_cn：第二个缺口：评估维度缺失

- depends_on_cn：第9句

- sets_up_cn：引出鲁棒性评估技术需求

- evidence_pointer：Introduction P3 reason 2

### 12. P3 S4

- order：12

- section：Introduction

- locator：P3 S4

- move_code：PRACTICAL_STAKES

- paraphrase_cn：认知不足和缺乏评估导致部署的应用可能被利用，造成财务和声誉损失

- rhetorical_function_cn：第三个缺口：部署脆弱性

- depends_on_cn：第10-11句

- sets_up_cn：引出鲁棒性增强需求

- evidence_pointer：Introduction P3 reason 3

### 13. P4 S1

- order：13

- section：Introduction

- locator：P4 S1

- move_code：RQ_OR_OBJECTIVE

- paraphrase_cn：本文提出两个研究问题：如何评估预测分析的对抗鲁棒性？如何提高对抗鲁棒性？

- rhetorical_function_cn：明确研究问题

- depends_on_cn：第10-12句

- sets_up_cn：组织全文结构

- evidence_pointer：Introduction P4 S1

### 14. P4 S2

- order：14

- section：Introduction

- locator：P4 S2

- move_code：THEORY_INTRO

- paraphrase_cn：基于技术威胁规避理论提出评估和增强框架

- rhetorical_function_cn：引入内核理论

- depends_on_cn：第13句

- sets_up_cn：Framework section

- evidence_pointer：Introduction P4 S2

### 15. P4 S3-S5

- order：15

- section：Introduction

- locator：P4 S3-S5

- move_code：STUDY_OVERVIEW

- paraphrase_cn：框架包含评估模型和增强设计原则；实例化为ARText，利用集成学习和对抗重训练，并在垃圾评论和垃圾邮件上做两组评价

- rhetorical_function_cn：预告系统与实验

- depends_on_cn：第14句

- sets_up_cn：读者预期设计和评价

- evidence_pointer：Introduction P4 final

### 16. P1 S2-S3

- order：16

- section：Research Background: Predictive Analytics in IS

- locator：P1 S2-S3

- move_code：THEORY_INTRO

- paraphrase_cn：多数预测分析基于统计学习理论，将任务形式化为f:X→Y并采用经验风险最小化

- rhetorical_function_cn：为后续ERM假设缺陷提供技术基础

- depends_on_cn：无

- sets_up_cn：ERM分布假设

- evidence_pointer：Research Background first paragraphs

### 17. P2 S1-S2

- order：17

- section：Research Background: Predictive Analytics in IS

- locator：P2 S1-S2

- move_code：MECHANISM

- paraphrase_cn：ERM假设输入独立同分布，但当输入由受决策影响者提供时，对手可策略性操纵输入，该假设失效

- rhetorical_function_cn：建立技术机制层面的脆弱性

- depends_on_cn：第16句

- sets_up_cn：为什么需要对抗鲁棒性

- evidence_pointer：Research Background P2

### 18. P3 S1-S3

- order：18

- section：Research Background: Predictive Analytics in IS

- locator：P3 S1-S3

- move_code：LIMITATION

- paraphrase_cn：现有评估主要用准确率、精确率、召回率、F1、ROC等预测性能指标，不能直接度量鲁棒性

- rhetorical_function_cn：方法论缺口

- depends_on_cn：第17句

- sets_up_cn：新的评估模型

- evidence_pointer：Research Background P3

### 19. P1 S1-S2

- order：19

- section：Research Background: Adversarial Attacks against SML Models

- locator：P1 S1-S2

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：攻击分为causative（投毒）和exploratory（逃避），exploratory通过微扰欺骗已训练模型

- rhetorical_function_cn：引入攻击分类

- depends_on_cn：第17句

- sets_up_cn：黑盒exploratory攻击设定

- evidence_pointer：Research Background Attacks P1

### 20. P1 S4

- order：20

- section：Research Background: Adversarial Attacks against SML Models

- locator：P1 S4

- move_code：PHENOMENON

- paraphrase_cn：例如虚假负面评论可通过替换词语、引入typo绕过检测系统

- rhetorical_function_cn：让攻击概念落到文本域

- depends_on_cn：第19句

- sets_up_cn：ARText使用文本对抗样本

- evidence_pointer：Research Background Attacks P1

### 21. P2-P3

- order：21

- section：Research Background: Adversarial Attacks against SML Models

- locator：P2-P3

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：白盒攻击分最大损失和最小扰动；黑盒攻击通过迁移性或查询近似目标模型

- rhetorical_function_cn：整理攻击技术谱系

- depends_on_cn：第19句

- sets_up_cn：解释为何聚焦黑盒

- evidence_pointer：Table 1 taxonomy

### 22. P1 S1-S2

- order：22

- section：Research Background: Defense against Adversarial Attacks

- locator：P1 S1-S2

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：IS文献从principal-agent模型出发，通过混合整数规划解Nash均衡来防御SVM等模型

- rhetorical_function_cn：总结既有防御

- depends_on_cn：第17句

- sets_up_cn：识别其局限

- evidence_pointer：Research Background Defense P1

### 23. P2 S1

- order：23

- section：Research Background: Defense against Adversarial Attacks

- locator：P2 S1

- move_code：GAP

- paraphrase_cn：既有研究针对SVM并依赖解析解，不清楚能否推广到非线性判别函数的其他模型

- rhetorical_function_cn：第一缺口：模型类型局限

- depends_on_cn：第22句

- sets_up_cn：需要广义增强方法

- evidence_pointer：Research Background Defense P2

### 24. P3 S1

- order：24

- section：Research Background: Defense against Adversarial Attacks

- locator：P3 S1

- move_code：GAP

- paraphrase_cn：过去文献多为白盒攻击；本文转向黑盒攻击，因为真实领域如欺诈、垃圾、信用审批中攻击者常只有输出访问权

- rhetorical_function_cn：第二缺口：攻击假设局限

- depends_on_cn：第21-22句

- sets_up_cn：设定黑盒探索性攻击研究范围

- evidence_pointer：Research Background Defense P3

### 25. P4 S1

- order：25

- section：Research Background: Defense against Adversarial Attacks

- locator：P4 S1

- move_code：BOUNDARY_CONDITION

- paraphrase_cn：既有principal-agent假设所有个体理性且有操纵动机；本文允许真实报告数据的良性agent

- rhetorical_function_cn：划清研究边界和适用场景

- depends_on_cn：第22句

- sets_up_cn：贴近在线评论等非全欺诈场景

- evidence_pointer：Research Background Defense P4

### 26. P5 S1

- order：26

- section：Research Background: Defense against Adversarial Attacks

- locator：P5 S1

- move_code：RQ_OR_OBJECTIVE

- paraphrase_cn：总结研究问题设定：预测分析根据个人提供的数据决策，攻击者反复访问输出但有限知道模型规格

- rhetorical_function_cn：明确研究对象约束

- depends_on_cn：第23-25句

- sets_up_cn：引出框架设计

- evidence_pointer：Research Background Defense P5

### 27. P1 S1

- order：27

- section：Framework for Adversarial Robustness Assessment and Enhancement

- locator：P1 S1

- move_code：THEORY_INTRO

- paraphrase_cn：有效对抗措施需要IS安全理论提供设计指南，TTAT是合适的kernel theory

- rhetorical_function_cn：为理论选择辩护

- depends_on_cn：第26句

- sets_up_cn：TTAT的两个组件

- evidence_pointer：Framework P1

### 28. P1 S2

- order：28

- section：Framework for Adversarial Robustness Assessment and Enhancement

- locator：P1 S2

- move_code：THEORY_PROPOSITION

- paraphrase_cn：TTAT包含威胁评估和威胁应对两部分

- rhetorical_function_cn：陈述理论命题

- depends_on_cn：第27句

- sets_up_cn：映射到元需求

- evidence_pointer：Framework P1

### 29. P1 S3-S4

- order：29

- section：Framework for Adversarial Robustness Assessment and Enhancement

- locator：P1 S3-S4

- move_code：REQUIREMENT

- paraphrase_cn：防御黑盒攻击需要同时评估威胁和应对威胁，因此框架包含两个元需求：鲁棒性评估和鲁棒性增强

- rhetorical_function_cn：从理论到设计要求的翻译

- depends_on_cn：第28句

- sets_up_cn：图1框架

- evidence_pointer：Framework P1 + Figure 1

### 30. P1 S1

- order：30

- section：Framework: Adversarial Robustness Assessment

- locator：P1 S1

- move_code：REQUIREMENT

- paraphrase_cn：提出通过实证分析量化鲁棒性，包含对抗样本生成和鲁棒性测量两步

- rhetorical_function_cn：具体化评估元需求

- depends_on_cn：第29句

- sets_up_cn：ARText评估模块

- evidence_pointer：Framework Assessment first paragraph

### 31. P2-P3

- order：31

- section：Framework: Adversarial Robustness Assessment

- locator：P2-P3

- move_code：LIMITATION

- paraphrase_cn：现有性能型测量混入预测性能且测试床只含对抗样本，扰动型测量用简单统计无法刻画权衡

- rhetorical_function_cn：批评既有测量

- depends_on_cn：第30句

- sets_up_cn：提出新测量

- evidence_pointer：Table 2 and following paragraphs

### 32. P3 S1-S3

- order：32

- section：Framework: Adversarial Robustness Assessment

- locator：P3 S1-S3

- move_code：DESIGN_FEATURE

- paraphrase_cn：提出用相对性能比率并结合非对抗/对抗混合测试集；用性能-扰动曲线捕捉扰动范围与性能的权衡

- rhetorical_function_cn：提出评估设计原则

- depends_on_cn：第31句

- sets_up_cn：ARText的性能比率和曲线公式

- evidence_pointer：Framework Assessment final paragraphs

### 33. P1 S1-S2

- order：33

- section：Framework: Adversarial Robustness Enhancement

- locator：P1 S1-S2

- move_code：DESIGN_FEATURE

- paraphrase_cn：攻击特定防御不适用于未知攻击类型，因此提出集成学习和对抗重训练两个设计原则

- rhetorical_function_cn：从缺口到增强设计

- depends_on_cn：第29句

- sets_up_cn：ARText增强模块

- evidence_pointer：Framework Enhancement first paragraph

### 34. P2 S1

- order：34

- section：Framework: Adversarial Robustness Enhancement

- locator：P2 S1

- move_code：MECHANISM

- paraphrase_cn：集成学习通过多样化降低相关失败风险，并扩大攻击者搜索替代模型的功能空间，使攻击更难成功

- rhetorical_function_cn：解释集成的机制

- depends_on_cn：第33句

- sets_up_cn：装袋集成设计

- evidence_pointer：Framework Enhancement P2

### 35. P3 S1-S3

- order：35

- section：Framework: Adversarial Robustness Enhancement

- locator：P3 S1-S3

- move_code：MECHANISM

- paraphrase_cn：对抗重训练把对抗样本加入训练集，等价于在目标函数中显式建模对抗风险，并可调节权重以权衡预测性能与鲁棒性

- rhetorical_function_cn：用形式化解释重训练机制

- depends_on_cn：第33句

- sets_up_cn：迭代对抗重训练算法

- evidence_pointer：Framework Enhancement P3

### 36. P1 S1-S2

- order：36

- section：System Design: The ARText System

- locator：P1 S1-S2

- move_code：DESIGN_FEATURE

- paraphrase_cn：基于文本分类的广泛应用，开发ARText作为框架实例化，集成了对抗样本生成、鲁棒性测量、装袋集成和迭代重训练

- rhetorical_function_cn：进入系统设计

- depends_on_cn：第32、35句

- sets_up_cn：系统各模块详细说明

- evidence_pointer：System Design P1 + Figure 2

### 37. P1 S1-S2

- order：37

- section：System Design: Adversarial Robustness Assessment using Adversarial Textual Samples

- locator：P1 S1-S2

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：ARText模拟黑盒攻击：先训练多种替代模型，再使用DeepWordBug生成对抗文本；多种模型可扩大对抗样本多样性

- rhetorical_function_cn：说明评估模块技术选择

- depends_on_cn：第36句

- sets_up_cn：评估测量的可操作性

- evidence_pointer：System Design Assessment P1

### 38. P1-P2

- order：38

- section：System Design: Adversarial Robustness Measurement

- locator：P1-P2

- move_code：DESIGN_FEATURE

- paraphrase_cn：提出性能比率和性能-扰动曲线，并扩展到accuracy、precision、recall、F1、ROC五个文本分类指标

- rhetorical_function_cn：给出具体测量定义

- depends_on_cn：第37句

- sets_up_cn：Evaluation 1的指标

- evidence_pointer：System Design Measurement

### 39. P2 S1

- order：39

- section：System Design: Adversarial Robustness Measurement

- locator：P2 S1

- move_code：DESIGN_FEATURE

- paraphrase_cn：性能比率比较模型在非对抗数据集和混合对抗/非对抗数据集上的性能，使变化可归因于对抗扰动

- rhetorical_function_cn：解释指标合理性

- depends_on_cn：第38句

- sets_up_cn：Experiment 1

- evidence_pointer：System Design Measurement P2

### 40. P4 S1-S2

- order：40

- section：System Design: Adversarial Robustness Measurement

- locator：P4 S1-S2

- move_code：DESIGN_FEATURE

- paraphrase_cn：性能-扰动曲线以预测性能为纵轴、扰动范围为横轴，曲线越高越鲁棒，AUC为综合鲁棒性分数

- rhetorical_function_cn：解释曲线测量

- depends_on_cn：第38句

- sets_up_cn：Experiment 2

- evidence_pointer：System Design Measurement P4

### 41. P1 S1-S4

- order：41

- section：System Design: Ensemble Learning

- locator：P1 S1-S4

- move_code：DESIGN_FEATURE

- paraphrase_cn：采用bagging集成：自举训练子样本、分别训练、投票决策；减少过拟合并迫使对抗样本欺骗多数模型

- rhetorical_function_cn：说明增强模块架构

- depends_on_cn：第34句

- sets_up_cn：Experiment 3

- evidence_pointer：System Design Ensemble Learning

### 42. P1 S1-S3

- order：42

- section：System Design: Adversarial Retraining

- locator：P1 S1-S3

- move_code：DESIGN_FEATURE

- paraphrase_cn：提出迭代对抗重训练算法：每轮攻击当前模型，将成功对抗样本加入训练集重训，并用鲁棒性指标判断收敛

- rhetorical_function_cn：实现训练过程增强

- depends_on_cn：第35句

- sets_up_cn：Experiment 4

- evidence_pointer：Figure 3

### 43. P1 S1-S3

- order：43

- section：System Design: Technical Novelties

- locator：P1 S1-S3

- move_code：CONTRIBUTION

- paraphrase_cn：技术新颖性包括新测量、将bagging加入迭代对抗重训练、文本预测分析鲁棒性系统的首批之一

- rhetorical_function_cn：明示系统层面的贡献

- depends_on_cn：第36-42句

- sets_up_cn：读者对实验的预期

- evidence_pointer：System Design Technical Novelties

### 44. P1 S1-S2

- order：44

- section：Experimental Evaluation

- locator：P1 S1-S2

- move_code：STUDY_OVERVIEW

- paraphrase_cn：参照Hevner设计科学评价，Evaluation1评估评估组件，Evaluation2评估增强组件，使用垃圾评论和垃圾邮件测试床

- rhetorical_function_cn：给出评价总体结构

- depends_on_cn：第43句

- sets_up_cn：Experiment 1-4

- evidence_pointer：Experimental Evaluation P1

### 45. P1 S3-S6

- order：45

- section：Experimental Evaluation

- locator：P1 S3-S6

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：测试床包括800/800均衡垃圾评论和非均衡2500/500垃圾邮件；基线覆盖传统与深度模型；采用5折交叉验证

- rhetorical_function_cn：建立公平比较的数据和基线

- depends_on_cn：第44句

- sets_up_cn：实验结果的可靠性

- evidence_pointer：Experimental Evaluation P1

### 46. P1 S1-S2

- order：46

- section：Evaluation 1: Adversarial Robustness Assessment

- locator：P1 S1-S2

- move_code：RQ_OR_OBJECTIVE

- paraphrase_cn：第一组评价验证评估组件：用性能比率和曲线测量基线在模型内可迁移性攻击下的鲁棒性，对抗测试集由DeepWordBug生成

- rhetorical_function_cn：明确第一轮评价目标

- depends_on_cn：第44句

- sets_up_cn：Experiment 1和2

- evidence_pointer：Evaluation 1 intro

### 47. P1 S1-S2

- order：47

- section：Experiment 1

- locator：P1 S1-S2

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：性能比率实验比较非对抗和混合对抗测试集，对抗垃圾评论按10%扰动范围生成并与文献一致

- rhetorical_function_cn：说明实验操作

- depends_on_cn：第46句

- sets_up_cn：图4和表3结果

- evidence_pointer：Experiment 1 first paragraph

### 48. P2 S1-S3

- order：48

- section：Experiment 1

- locator：P2 S1-S3

- move_code：RESULT

- paraphrase_cn：图4显示所有基线模型在所有指标上性能下降，没有模型天然鲁棒；某些原始性能好的模型下降更严重

- rhetorical_function_cn：报告核心现象

- depends_on_cn：第47句

- sets_up_cn：性能比率量化

- evidence_pointer：Figure 4

### 49. P3 S1-S3

- order：49

- section：Experiment 1

- locator：P3 S1-S3

- move_code：RESULT

- paraphrase_cn：表3显示在均衡垃圾评论上NB鲁棒性最高，各模型差异明显；10%扰动可削弱最佳性能4%-29%

- rhetorical_function_cn：给出可操作结论

- depends_on_cn：第48句

- sets_up_cn：需要更全面的曲线测量

- evidence_pointer：Table 3

### 50. P1 S1

- order：50

- section：Experiment 2

- locator：P1 S1

- move_code：BOUNDARY_CONDITION

- paraphrase_cn：性能比率适合固定扰动范围的场景，当扰动范围难以控制时，性能-扰动曲线更合适

- rhetorical_function_cn：划定两种指标适用边界

- depends_on_cn：第49句

- sets_up_cn：Experiment 2设计

- evidence_pointer：Experiment 2 first paragraph

### 51. P2 S1

- order：51

- section：Experiment 2

- locator：P2 S1

- move_code：RESULT

- paraphrase_cn：图5显示RF在10%扰动时召回略高，但CNN在10%-86%区间更鲁棒，AUC显示CNN整体更好

- rhetorical_function_cn：用曲线示例说明跨范围比较价值

- depends_on_cn：第50句

- sets_up_cn：表4的AUC汇总

- evidence_pointer：Figure 5

### 52. P3 S1-S2

- order：52

- section：Experiment 2

- locator：P3 S1-S2

- move_code：RESULT

- paraphrase_cn：表4显示CNN在均衡数据集AUC最优；所有模型R/P AUC低于P/P AUC，说明攻击主要引发第二类错误；CNN的Lipschitz性质可能是原因

- rhetorical_function_cn：报告曲线测量结果并提供机制解释

- depends_on_cn：第51句

- sets_up_cn：进入增强评价

- evidence_pointer：Table 4

### 53. P1 S1

- order：53

- section：Evaluation 2: Adversarial Robustness Enhancement

- locator：P1 S1

- move_code：STUDY_OVERVIEW

- paraphrase_cn：第二组评价检验增强组件：Experiment3测集成学习，Experiment4测对抗重训练，另在在线附录做迁移/查询攻击敏感性分析

- rhetorical_function_cn：预告第二组实验

- depends_on_cn：第44句

- sets_up_cn：Experiment 3和4

- evidence_pointer：Evaluation 2 intro

### 54. P1 S1

- order：54

- section：Experiment 3

- locator：P1 S1

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：集成模型与基线比较，其对抗样本由与集成同构成的替代模型生成

- rhetorical_function_cn：保证攻击强度可比

- depends_on_cn：第53句

- sets_up_cn：表5/6结果

- evidence_pointer：Experiment 3 first paragraph

### 55. P2 S1

- order：55

- section：Experiment 3

- locator：P2 S1

- move_code：RESULT

- paraphrase_cn：表5显示在10%扰动下集成模型在所有性能比率指标上优于所有基线；垃圾评论上准确率鲁棒性提升0.071、F鲁棒性提升0.104

- rhetorical_function_cn：报告集成收益

- depends_on_cn：第54句

- sets_up_cn：更广的AUC指标

- evidence_pointer：Table 5

### 56. P3 S1-S2

- order：56

- section：Experiment 3

- locator：P3 S1-S2

- move_code：RESULT

- paraphrase_cn：表6显示集成模型在性能-扰动曲线AUC上也全面优于基线，验证多样化策略增加攻击难度

- rhetorical_function_cn：补充综合指标证据

- depends_on_cn：第55句

- sets_up_cn：加入重训练

- evidence_pointer：Table 6

### 57. P1 S1-S2

- order：57

- section：Experiment 4

- locator：P1 S1-S2

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：对集成和基线都应用迭代对抗重训练，每轮将DeepWordBug生成的对抗垃圾与原始垃圾混合重训，迭代上限100或提前收敛

- rhetorical_function_cn：说明重训练实验协议

- depends_on_cn：第53句

- sets_up_cn：前后对比结果

- evidence_pointer：Experiment 4 first paragraph

### 58. P2 S1

- order：58

- section：Experiment 4

- locator：P2 S1

- move_code：RESULT

- paraphrase_cn：图6/表7显示重训练后所有模型鲁棒性提升；ARText最高，垃圾评论召回鲁棒性提高29.11%，垃圾邮件提高26.27%

- rhetorical_function_cn：报告重训练收益

- depends_on_cn：第57句

- sets_up_cn：各类模型普适性

- evidence_pointer：Figure 6 + Table 7

### 59. P3 S1-S3

- order：59

- section：Experiment 4

- locator：P3 S1-S3

- move_code：RESULT

- paraphrase_cn：图7/表8显示重训练提升大多数AUC指标，R/P AUC提升27%（垃圾评论）和82%（垃圾邮件），说明重训练降低第二类错误；ARText仍优于重训练后的基线，说明集成进一步增益重训练

- rhetorical_function_cn：报告联合效应

- depends_on_cn：第58句

- sets_up_cn：讨论中的设计原则

- evidence_pointer：Figure 7 + Table 8

### 60. P1 S1

- order：60

- section：Discussion

- locator：P1 S1

- move_code：RESULT

- paraphrase_cn：实验结果验证ARText及其元设计：第一组证明评估效用，第二组证明增强有效

- rhetorical_function_cn：总结实证环节

- depends_on_cn：第44-59句

- sets_up_cn：三点主要启示

- evidence_pointer：Discussion first paragraph

### 61. P2 S1-S4

- order：61

- section：Discussion

- locator：P2 S1-S4

- move_code：CONTRIBUTION

- paraphrase_cn：第一点：对抗鲁棒性应成为预测分析评估的一部分；10%扰动可扭曲3%精确率和28%召回率；ERM脆弱性使其可推广到多领域

- rhetorical_function_cn：把结果提升为评估原则

- depends_on_cn：第60句

- sets_up_cn：组织实践建议

- evidence_pointer：Discussion first takeaway

### 62. P3 S1-S4

- order：62

- section：Discussion

- locator：P3 S1-S4

- move_code：BOUNDARY_CONDITION

- paraphrase_cn：第二点：性能比率适合固定扰动范围，性能-扰动曲线适合无界范围；可通过替换领域指标推广到其他预测分析任务

- rhetorical_function_cn：界定测量方法的适用范围

- depends_on_cn：第60句

- sets_up_cn：通用的测量设计知识

- evidence_pointer：Discussion second takeaway

### 63. P4 S1-S4

- order：63

- section：Discussion

- locator：P4 S1-S4

- move_code：CONTRIBUTION

- paraphrase_cn：第三点：集成学习和对抗重训练是有效的设计原则，前者用多样化降低风险，后者缓解ERM分布假设，且可应用于已有系统而不需重大修改

- rhetorical_function_cn：把增强结果上升为设计原则

- depends_on_cn：第60句

- sets_up_cn：结论中的贡献声明

- evidence_pointer：Discussion third takeaway

### 64. P1 S1

- order：64

- section：Conclusions

- locator：P1 S1

- move_code：CONTRIBUTION

- paraphrase_cn：贡献于AI治理：即使AI在良性设置中有效，其算法漏洞可被攻击利用，安全是human-AI hybrid开发的关键

- rhetorical_function_cn：理论贡献定位

- depends_on_cn：第61-63句

- sets_up_cn：第二、三层贡献

- evidence_pointer：Conclusions first paragraph

### 65. P1 S2

- order：65

- section：Conclusions

- locator：P1 S2

- move_code：CONTRIBUTION

- paraphrase_cn：扩展预测分析文献，把对抗鲁棒性评估纳入评估体系

- rhetorical_function_cn：文献贡献

- depends_on_cn：第64句

- sets_up_cn：设计贡献

- evidence_pointer：Conclusions first paragraph

### 66. P1 S3

- order：66

- section：Conclusions

- locator：P1 S3

- move_code：CONTRIBUTION

- paraphrase_cn：提出基于TTAT的设计框架，并通过ARText实例化与系列实验展示可行性

- rhetorical_function_cn：设计贡献

- depends_on_cn：第65句

- sets_up_cn：实践意义

- evidence_pointer：Conclusions first paragraph

### 67. P3 S1-S3

- order：67

- section：Conclusions

- locator：P3 S1-S3

- move_code：LIMITATION_AND_FUTURE

- paraphrase_cn：局限：计算成本、特征工程也可能被攻击、文本扰动量化较粗糙；未来可研究更高效率、特征工程攻防和更细粒度扰动度量

- rhetorical_function_cn：保护贡献不过度泛化

- depends_on_cn：第64-66句

- sets_up_cn：后续研究 agenda

- evidence_pointer：Conclusions limitations

## 写作技术

- gap_construction_cn：采用三重缺口构造：第一重是IS预测分析文献未承认安全威胁、评估仍以预测性能为主；第二重是防御文献局限于SVM、白盒攻击和理性代理假设；第三重是现实部署因缺少评估而脆弱。文章通过ERM分布假设与对抗输入现实之间的冲突，把这些经验现象转化为理论和方法论缺口。

- signposting_cn：开头直接列出两个研究问题；研究背景末尾总结研究设定；Framework用图1显示元需求；Evaluation部分明确Evaluation1/2和Experiment1-4；每个实验段落先说明目标再给结果；Discussion用三点takeaways收束。

- transition_logic_cn：先建立“需要评估+需要增强”的框架，再按组件实现；评估实验先证明基线脆弱，增强实验再证明设计原则有效；Experiment1到2从单点扰动范围拓宽到全域曲线；Experiment3到4从静态架构增强转向训练过程增强。

- claim_evidence_rhythm_cn：每提出一个设计声明，随后给出公式、算法或系统组件；每个实验结果先写方法，再用图/表展示数据，再做机制解释；讨论用“实验结果表明”把数字转化为设计原则。

- benchmark_narrative_cn：用同一组九种基线模型、相同DeepWordBug攻击生成器、固定10%扰动范围和两个不同平衡性的测试床建立可比性；评估1用非对抗/混合对抗对比；评估2先用同构成替代模型攻击集成，再加入重训练前后对照，使benchmark服务于论证链而非孤立性能比较。

- theory_return_cn：结果不仅报告ARText更好，还在Discussion中把ERM脆弱性、TTAT元需求、多样化和对抗风险等机制重新连接；结论部分把设计框架上升到AI治理和预测分析评估文献，完成从实验数字到理论知识的返回。

- contribution_positioning_cn：贡献分三层：AI治理（理论）、预测分析评估（文献）、设计框架和ARText（设计科学）。每层都对应引言中的某个缺口，并在结论中明确回应。

- novelty_protection_cn：强调性能比率“剔除”预测性能、性能-扰动曲线“刻画权衡”，并把ARText定位为“首批文本预测分析鲁棒性系统”；用全面基线对照、重训练前后对照、两个testbeds和补充敏感性分析防止贡献被解读为一次性性能结果。

## 可复用研究与写作程序

### structure_steps

#### 1. 1

- step：1

- writing_job_cn：写出现实应用背景和技术基础（SML、ERM、攻击威胁）

- research_job_cn：收集应用场景、攻击分类和ERM假设相关文献

- required_evidence_cn：能说明预测分析应用广泛且ERM假设会被策略性输入破坏的文献与实例

- transition_to_next_cn：由技术机制缺陷引出IS文献缺口

#### 2. 2

- step：2

- writing_job_cn：构建具体缺口：评估维度缺失、防御假设局限、部署脆弱

- research_job_cn：比较IS预测分析评估指标和现有防御研究

- required_evidence_cn：证明现有评估以预测性能为主、防御集中在SVM/白盒/理性代理

- transition_to_next_cn：提出两个研究问题和基本研究范围

#### 3. 3

- step：3

- writing_job_cn：选择内核理论，把理论组件翻译成元需求和设计原则

- research_job_cn：寻找理论概念与设计要求的映射关系

- required_evidence_cn：理论定义可对应到要解决的系统问题（如威胁评估/应对）

- transition_to_next_cn：说明需要具体实例化

#### 4. 4

- step：4

- writing_job_cn：描述制品设计：测量模块、增强模块、算法与公式

- research_job_cn：选择并改造现有算法、实现可运行系统

- required_evidence_cn：系统可运行、有明确输入输出和算法流程

- transition_to_next_cn：说明需要实验评价

#### 5. 5

- step：5

- writing_job_cn：设计分组件评价：评估组件用脆弱性揭示，增强组件用对照实验

- research_job_cn：选择测试床、基线、攻击生成器和评价指标，执行实验

- required_evidence_cn：结果表/图能支持每个组件的效用和有效性

- transition_to_next_cn：将实验效果上升为设计原则

#### 6. 6

- step：6

- writing_job_cn：讨论设计知识、边界条件和贡献，并回扣引言缺口

- research_job_cn：解释机制、识别适用场景、讨论局限

- required_evidence_cn：实验结果能支撑泛化论述和边界判断

- transition_to_next_cn：形成完整的设计科学论证闭环

### most_transferable_moves_cn

1. 用技术机制缺陷（ERM假设失效）把现实威胁转化为学术缺口

2. 用内核理论组件映射到元需求，再逐步细化到可运行设计

3. 把评估组件和增强组件分开评价，使每个元需求都有直接证据

4. 在统一基线和攻击设定下构建从脆弱性评估到增强验证的递进实验链

5. 在Discussion中用设计原则而非单一性能数字收束结论

### resource_intensive_or_nonstandard_parts_cn

1. 需要训练多种传统和深度文本分类模型作为基线和替代模型

2. DeepWordBug或其他对抗文本生成器需要工程实现与调参

3. 迭代对抗重训练的计算成本高，迭代上限和收敛判断需要设计

4. 均衡和非均衡测试床的数据获取与预处理可能依赖外部语料

5. 在线补充的迁移/查询攻击敏感性分析需要额外攻击实现

### what_not_to_copy_superficially_cn

1. 不要在没有统计检验或足够对照时使用“显著增强”

2. 不要只做表面TTAT标签而不建立理论组件到设计要求的真实映射

3. 不要声称“首批系统”而不进行相关文献审计

4. 不要把单点性能比率结果当作通用鲁棒性证据，需要跨扰动范围曲线

5. 不要让机制解释超出实验结果（如Lipschitz解释是推测）

- single_best_description_of_the_routine_cn：用IS安全理论把“需要评估+需要增强”变成元需求，再以当前最优攻击/防御技术实例化成系统，最终用两个测试床和同一批基线把技术改进解释为可复用的设计原则。

## 分析边界

全文以OCR形式提供，图片内容无法直接读取，只能依据图标题和正文引用理解；在线补充附录中关于迁移/查询攻击的敏感性分析在主文中未展开具体数据，因此无法评价其证据强度；表8跨页时标题出现OCR截断，但不影响主要表格内容识别。
