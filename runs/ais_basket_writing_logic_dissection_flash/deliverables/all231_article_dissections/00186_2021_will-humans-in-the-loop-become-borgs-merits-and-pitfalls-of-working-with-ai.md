# Will Humans-in-the-Loop Become Borgs? Merits and Pitfalls of Working with AI

- 作者：Andreas Fügener; Jörn Grahl; Alok Gupta; Wolfgang Ketter
- 年份 / 期刊：2021 / MIS Quarterly
- DOI：10.25300/misq/2021/16553
- 源文件：00186_2021_will-humans-in-the-loop-become-borgs-merits-and-pitfalls-of-working-with-ai.md
- 论文主类型：multi_method_or_multi_study_program
- 主导写作弧线：problem_theory_design_test_return
- 置信度：0.9

## 文章级论证概况

- 核心问题：在人类接收AI建议的决策环境中，AI建议如何影响人类个体准确率与独特人类知识（unique human knowledge）？这种变化对群体智慧（wisdom of crowds）有何后果？能否通过呈现AI置信度或个性化AI建议来缓解独特人类知识的损失？

- 制品与设计：研究围绕AI建议型人机决策环境展开，核心设计是四种条件：无AI建议、标准AI建议、AI建议附带AI置信度、个性化AI建议。实验使用GoogLeNet Inception v3对ImageNet图像进行分类，AI建议推荐最高置信度类别；个性化条件中，AI根据个体在错误建议上的伤害和正确建议上的收益计算临界比，只在临界比以上提供建议。

- 客观结果：AI建议使个体准确率从0.681提升到0.799（实验1），但独特人类知识从0.123降到0.073；呈现AI置信度使独特人类知识恢复至0.087，但未显著提升准确率。个性化AI建议在保持甚至略微提升准确率的同时，将独特人类知识从0.074提高到0.097。群体智慧仿真显示，AI建议在小组中有利，但随着群体增大，无AI建议的人类群体反超；个性化AI建议则在所有群体规模下均表现最好。

- 核心贡献：作者声称发现了一个此前被忽视的AI建议副作用：AI建议在提高个体准确率的同时会减少独特人类知识，使人类更像“Borgs”，即个体能力增强但个体性/互补性丧失；这种损失会损害群体智慧，而个性化AI建议可以同时保留个体绩效和人类多样性的好处。

- 整篇论证链：文章先指出现有AI建议文献主要追求绩效最大化，忽略AI建议对独特人类知识的影响；然后定义独特人类知识为AI错误而人类正确的任务实例，并用离散选择模型证明AI建议提高准确率的条件、降低UHK的机制、以及两种干预（AI置信度、个性化建议）何时有效；接着用三个实验分别检验AI建议和AI置信度、个体反应异质性、个性化建议对准确率和UHK的影响；然后用实验数据做Monte Carlo仿真，把个体层面损失转化为群体智慧后果，证明AI建议在群体增大时反而不利，而个性化建议可以缓解。整条论证从理论命题到个体实验再到群体仿真，最终回到人类-AI互补性、决策支持设计和Borgs隐喻。

## 类型与写作弧线判定

- 论文主类型判定：论文不是单一实验或纯benchmark，也不是传统设计科学构建新系统；它由解析模型、两个预注册确认性实验、一个探索性实验和基于实验数据的Monte Carlo仿真组成，每个研究阶段承担不同的论证任务：理论生成假设、个体层面检验、异质性探索、群体后果模拟，因此属于多方法/多Study累积完成贡献。

- 主导写作弧线判定：文章从人类与AI协作的现实问题和被忽视的独特知识切入，建立个体决策和群体智慧的理论模型，把理论转化为两个干预设计并做实验检验，最后回到互补性、决策支持和Borgs的一般化讨论；整体写作弧线是问题—理论—设计—检验—返回理论。

## 研究开展程序

- study_or_phase_count：7

- 研究阶段总序列：第一阶段用离散选择模型生成个体层面假设；第二阶段在群体智慧理论中推导群体假设并用数值示例展示AI建议从有益转向有害的群体规模；第三阶段用实验1检验AI建议和AI置信度对准确率与UHK的影响；第四阶段用探索性实验2显示个体对建议的收益/伤害存在显著异质性，为个性化建议提供动机；第五阶段用实验3检验个性化AI建议；第六、七阶段分别用实验1和实验3的数据进行群体智慧仿真，证明AI建议损害大群体、AI置信度只部分缓解、个性化建议能同时保住个体和群体表现。

### studies_or_phases

#### 1. 个体决策分析模型

- order：1

- name_cn：个体决策分析模型

- question_cn：在理性决策视角下，AI建议如何影响人类准确率和独特人类知识？AI置信度与个性化建议在什么条件下有效？

- inputs_and_setting_cn：离散选择任务的数学设定；人类选择正确项概率p_tc，AI建议a_tc，建议效应强度e_t，置信度缩放s_t，个性化决策d_th。

- designed_or_compared_object_cn：比较无建议、标准AI建议、带置信度建议、个性化建议四种情境的数学期望。

- baseline_control_or_counterfactual_cn：无AI建议作为基线，标准AI建议作为比较对象；个性化建议的反事实是同一任务若总是提供建议的结果。

##### objective_metrics

1. human accuracy

2. unique human knowledge (UHK)

3. unique AI knowledge (UAK)

4. relative unique human knowledge UHK/UAK

5. ΔAI

- analysis_method_cn：离散选择概率模型、代数推导、命题与可检验假设生成。

- main_result_cn：AI建议提高个体准确率，但除非人类能完美区分正确与错误建议，否则会降低UHK；正确建议与错误建议效果相对大小、相对UHK决定AI建议总体是否有利；置信度和个性化建议具有保留绩效并缓解UHK下降的条件。

- argumentative_role_cn：建立全部核心概念和假设，为后续实验的设计变量提供理论来源。

- remaining_uncertainty_cn：模型假设人类按概率响应建议，未证明真实人类会表现出同样的行为模式。

- link_to_next_phase_cn：由命题1-3推导出H1a-H3b，预告需要用受试者实验进行实证检验。

##### evidence_pointers

1. Theoretical Framework: Individual Decision Making

2. Equations (5)-(12)

3. Proposition 1, 2, 3

4. Hypotheses 1a-3b

#### 2. 群体智慧理论框架与数值探索

- order：2

- name_cn：群体智慧理论框架与数值探索

- question_cn：AI建议对众数聚合的群体决策何时从有益转为有害？

- inputs_and_setting_cn：多选任务中群组众数选择；二项/多项分布、Hoeffding不等式、数值示例（C=10，e=0.5，人类准确率0.2/0.5/0.8，AI准确率变化矩阵）。

- designed_or_compared_object_cn：比较不同组规模下无AI建议群体与有AI建议群体的群体准确率。

- baseline_control_or_counterfactual_cn：无AI建议人类群体为基线；有AI建议群体为处理。

##### objective_metrics

1. group accuracy

2. group size threshold

3. probability of modal choice

- analysis_method_cn：解析推导（命题4）与数值计算（Figure 1、Figure 2）。

- main_result_cn：只要正确选项被选概率高于其他选项，就存在一个组规模使无AI建议群体超过有AI建议群体；错误AI建议对群体非常有害，正确AI建议只在困难任务中对群组有明显帮助。

- argumentative_role_cn：将个体层面的UHK损失与群体智慧后果连接起来，生成H4a-H4c。

- remaining_uncertainty_cn：数值示例基于假设效应量，并非真实人类实验数据。

- link_to_next_phase_cn：提出需要用实验个体数据做群体仿真，检验真实条件下假设是否成立。

##### evidence_pointers

1. Theoretical Framework: Wisdom of Crowds

2. Proposition 4

3. Figure 1 and Figure 2

4. Hypotheses 4a-4c

#### 3. 实验1：AI建议与AI置信度

- order：3

- name_cn：实验1：AI建议与AI置信度

- question_cn：AI建议是否提高准确率并降低独特人类知识？额外呈现AI置信度能否缓解UHK下降并进一步提高准确率？

- inputs_and_setting_cn：458名MTurk受试者，100张ImageNet图像分类；三种组间条件：无AI（T1）、AI建议（T2）、AI建议+置信度（T3）；预注册、功率分析、随机分配、注意力检查。

- designed_or_compared_object_cn：在T2基础上增加AI置信度提示，用四点评分量表向受试者传达AI置信度。

- baseline_control_or_counterfactual_cn：T1为无建议基线，T2为标准AI建议，T3为置信度干预。

##### objective_metrics

1. human accuracy

2. unique human knowledge

3. image-level regression coefficients

4. trust questionnaire scores

- analysis_method_cn：Levene检验、异方差ANOVA、Tamhane T2/Tukey HSD事后比较、图像级随机效应回归。

- main_result_cn：H1a和H1b得到支持：AI建议显著提高准确率（0.799 vs 0.681）并降低UHK（0.073 vs 0.123）；H2a未获支持：置信度未显著提高准确率（0.801 vs 0.799）；H2b获支持：置信度显著提高UHK（0.087 vs 0.073）；回归显示置信度让人们减少对AI建议的遵从，尤其降低了在AI正确图像上的准确率。

- argumentative_role_cn：验证了理论模型最核心的两个个体效应，并第一次展示AI置信度对UHK的缓解作用。

- remaining_uncertainty_cn：为什么置信度提高UHK却没有提高准确率；个体反应是否存在系统性差异；群体层面后果未知。

- link_to_next_phase_cn：准确率与UHK的变化看起来与个体对建议的采纳差异有关，于是进入实验2探索收益/伤害异质性。

##### evidence_pointers

1. Experimental Studies: Individual Decision Making, Experiment 1

2. Table 2

3. Figure 5

4. Table 3

#### 4. 实验2：人类对AI建议反应的异质性

- order：4

- name_cn：实验2：人类对AI建议反应的异质性

- question_cn：正确AI建议的收益和错误AI建议的伤害是否在不同个体间存在足够大的异质性，从而支持个性化建议？

- inputs_and_setting_cn：99名MTurk受试者；同一批100张图像先无建议分类，再看到AI建议并允许修改；被试内设计；探索性，未预注册。

- designed_or_compared_object_cn：同一受试者在有无AI建议下分别决策，计算收益（正确AI建议使错改正）和伤害（错误AI建议使对改错）。

- baseline_control_or_counterfactual_cn：每个受试者自己的无AI准确率作为基线；AI建议后的准确率为处理。

##### objective_metrics

1. accuracy without AI

2. accuracy with AI

3. benefit of correct advice

4. harm of incorrect advice

- analysis_method_cn：描述性统计、个体收益-伤害散点图。

- main_result_cn：所有受试者都因AI建议而提高准确率，没有一个人整体受损；但收益和伤害的个体差异很大，且不能简单用AI遵从度解释。

- argumentative_role_cn：为个性化AI建议提供经验基础，表明按个体估计收益/伤害并选择性提供建议是可行方向。

- remaining_uncertainty_cn：探索性证据未检验个性化建议是否能真正奏效。

- link_to_next_phase_cn：异质性结论直接引出实验3的个性化建议设计。

##### evidence_pointers

1. Experimental Studies: Individual Decision Making, Experiment 2

2. Table 4

3. Figure 6

#### 5. 实验3：个性化AI建议

- order：5

- name_cn：实验3：个性化AI建议

- question_cn：个性化AI建议是否能保持个体准确率的同时显著提高独特人类知识？

- inputs_and_setting_cn：492名MTurk受试者；100张图像分成两组各50张，前50张供AI学习个体收益/伤害，后50张测试三种条件：无AI（T1'）、AI建议（T2'）、个性化AI建议（T3'）；预注册。

- designed_or_compared_object_cn：个性化条件中，只有当AI置信度超过受试者临界比时才提供建议，否则不提供。

- baseline_control_or_counterfactual_cn：T1'无建议和T2'永久建议作为基准；T3'为选择性建议。

##### objective_metrics

1. human accuracy

2. unique human knowledge

- analysis_method_cn：Levene检验、异方差ANOVA、Tamhane T2/Tukey HSD事后比较。

- main_result_cn：H3a获支持：个性化建议的准确率（0.795）不显著低于永久AI建议（0.773），并显著高于无建议（0.658）；H3b获支持：个性化建议的UHK（0.097）显著高于永久建议（0.074），且与无建议（0.108）差异不显著。

- argumentative_role_cn：证明第二种干预可以在个体层面同时保住AI带来的准确率收益和人类独特知识。

- remaining_uncertainty_cn：个性化建议在真实群体互动或组织环境中是否仍有效未知。

- link_to_next_phase_cn：既然个体层面UHK被保住，下一步用群体智慧仿真看个性化建议能否缓解群体层面损失。

##### evidence_pointers

1. Experimental Studies: Individual Decision Making, Experiment 3

2. Table 5

3. Figure 7

#### 6. 群体智慧仿真：基于实验1的AI建议与AI置信度

- order：6

- name_cn：群体智慧仿真：基于实验1的AI建议与AI置信度

- question_cn：AI建议是否随群体增大而损害群体智慧？AI置信度是否能恢复群体收益？

- inputs_and_setting_cn：以实验1三个处理组（T1/T2/T3）为样本总体，Monte Carlo随机抽样形成1到15人以及99、100人的群体，共1000次迭代，以众数为群体选择。

- designed_or_compared_object_cn：比较无AI、AI建议、AI建议+置信度三种条件下的群体准确率-组规模曲线。

- baseline_control_or_counterfactual_cn：无AI建议人类群体为真实基线；AI建议和置信度群体为处理；同群体规模下相互比较。

##### objective_metrics

1. group accuracy

2. group size interaction coefficients

- analysis_method_cn：Monte Carlo模拟、简单线性回归（群体准确率对组规模、AI建议、AI建议×组规模、AI置信度、AI置信度×组规模）。

- main_result_cn：AI建议×组规模交互显著为负，H4a获支持；AI置信度×组规模交互显著为正，H4b获支持；无AI群体从组规模约7开始超过仅AI建议群体，从约11开始超过AI建议+置信度群体。

- argumentative_role_cn：用个体实验数据展示UHK损失如何转化为群体智慧损害，是全文论证的关键桥接。

- remaining_uncertainty_cn：仿真基于抽样统计而非真实群体沟通/互动；AI置信度改善并不足以完全消除大群体劣势。

- link_to_next_phase_cn：需要检验个性化建议在同样的群体仿真中是否更有效，于是进入实验3的群体仿真。

##### evidence_pointers

1. Experimental Studies: Wisdom of Crowds, Simulation based on Experiment 1

2. Figure 8

3. Table 6 left column

#### 7. 群体智慧仿真：基于实验3的个性化AI建议

- order：7

- name_cn：群体智慧仿真：基于实验3的个性化AI建议

- question_cn：个性化AI建议能否在群体规模增大时同时保留AI建议的个体好处和人类群体多样性？

- inputs_and_setting_cn：以实验3三种条件（T1'/T2'/T3'）为样本总体，对后50张图像做同样的Monte Carlo抽样和众数聚合。

- designed_or_compared_object_cn：比较无AI、永久AI建议、个性化AI建议三种条件下的群体准确率-组规模曲线。

- baseline_control_or_counterfactual_cn：T1'无AI为基线，T2'永久建议为基准处理，T3'个性化建议为目标处理。

##### objective_metrics

1. group accuracy

2. personalization × group size interaction coefficient

- analysis_method_cn：Monte Carlo模拟、线性回归（用AI personalization替代AI certainty变量）。

- main_result_cn：再次发现AI建议×组规模显著为负（H4a获更多支持）；个性化建议×组规模显著为正（H4c获支持）；个性化AI建议在所有群体规模上都优于无AI和永久AI建议，甚至在100人群体中仍未被反超。

- argumentative_role_cn：证明第二项干预既能保持个体绩效又能避免群体智慧退化，给出全文的核心正面结论。

- remaining_uncertainty_cn：仿真群体并非真实团队；长期学习、组织动态和任务异质性未被检验。

- link_to_next_phase_cn：群体仿真结果直接进入讨论部分，转化为AI决策支持系统的设计含义。

##### evidence_pointers

1. Experimental Studies: Wisdom of Crowds, Simulation based on Experiment 3

2. Figure 9

3. Table 6 right column

## 各部分修辞架构

### abstract_moves

1. 以研究主题开场：AI建议如何影响人类与AI的互补性，尤其独特人类知识。

2. 报告主要发现：人类选择趋同、个体准确率提高但独特人类知识下降。

3. 引入Borgs隐喻作为贡献命名。

4. 指出群体后果：损害群体智慧。

5. 预告缓解技术并宣称它们既利于个体也利于群体。

### introduction_moves

1. 建立背景：AI改变工作场所，但完全自动化存在伦理/法律障碍；人类输出仍必要。

2. 界定研究领域：AI建议型人类决策。

3. 指出现有文献聚焦绩效最大化，忽略AI建议对独特人类知识的影响。

4. 说明独特人类知识对协作、创新和群体智慧的广泛重要性。

5. 提出三个研究问题：准确率与UHK、缓解方法、群体智慧后果。

6. 预告方法：解析模型、实验、仿真。

7. 概括关键洞见：即使个体绩效高于AI，UHK仍会下降。

8. 介绍两个干预：AI置信度、个性化建议。

9. 概述个体与群体结果。

10. 给出论文结构路标。

### theory_and_knowledge_moves

1. 回顾AI建议文献中关于绩效和AI置信度/心智模型的讨论。

2. 总结AI置信度效果在实验中的混合证据。

3. 指出没有研究讨论AI建议对UHK的影响。

4. 引入群体智慧、多样性预测定理和群体多样性下降的文献。

5. 建立离散选择模型并定义UHK、UAK。

6. 推导AI建议对准确率和UHK影响的命题与假设。

7. 推导AI置信度和个性化建议的条件与假设。

8. 在群体智慧模型中推导组规模阈值并生成H4a-H4c。

### artifact_design_moves

1. 选择图像分类作为通用任务并说明三点理由。

2. 使用GoogLeNet Inception v3作为AI建议来源。

3. 设计无AI、AI建议、AI建议+置信度三种基础条件。

4. 将AI置信度映射到人类同样使用的四点评分量表。

5. 根据理论模型定义UHK与准确率测量。

6. 在实验3中实现个性化临界比规则：前50张学习个体收益/伤害，后50张选择性提供建议。

7. 通过预注册、功率分析、MTurk流程强化设计可信度。

### evaluation_moves

1. 用实验1检验H1a/H1b/H2a/H2b，使用ANOVA和事后比较。

2. 用图像级回归解释H2a未获支持的原因。

3. 用实验2测量个体收益/伤害异质性。

4. 用实验3检验H3a/H3b。

5. 用Monte Carlo仿真把实验个体数据聚合成群体智慧结果。

6. 用回归检验组规模与AI建议/置信度/个性化的交互效应。

7. 以无AI条件作为贯穿始终的基线和外部锚点。

### discussion_and_contribution_moves

1. 回到两个主要效应：个体绩效提升与UHK损失。

2. 说明个体提升依赖于互补性和区分正确/错误建议的能力。

3. 说明UHK损失对群体智慧的影响，并引用技能-多样性讨论。

4. 提出AI决策支持系统的三个设计含义。

5. 强调不能把AI建议视为“一刀切”方案。

6. 列举三点未来研究方向。

7. 以Borgs问题收束，将结果转化为关于人类长期价值和多样性的讨论。

## 理论/知识到设计的翻译

### 知识/理论基础

1. AI建议型人类决策与心智模型/错误边界（Bansal et al. 2019a, 2019b）

2. 建议采纳与人类区分正确/错误建议能力（Bonaccio and Dalal 2006）

3. 独特人类知识与人类-AI互补性（Krishnan et al. 1997; Tan et al. 2018; Zhang et al. 2020）

4. 群体智慧与多样性预测定理（Surowiecki 2004; Page 2008; Hong et al. 2016）

5. 现代AI能估计自身不确定性并能学习个体行为（Zhang et al. 2020）

- 理论—设计耦合：direct

- 耦合判定理由：两个干预并非单纯的工程启发：AI置信度介入被建模为s_t对建议效果e_t的缩放，个性化建议被建模为按个体临界比r_h决定是否提供建议；实验设计直接比较这些理论设计变量与标准建议、无建议的差异，因此理论实质决定了设计并被评价直接检验。

- 理论到设计翻译链：知识命题（人类与AI在结构上互补，存在UHK/UAK）→ 机制（AI建议改变选择概率，正确建议产生收益、错误建议产生伤害）→ 设计要求（应让人类更好区分正确/错误建议，或让AI按个体临界比选择要不要给建议）→ 制品选择（呈现AI置信度；个性化阈值规则）→ 被比较的设计差异（无建议 vs 标准建议 vs 标准建议+置信度 vs 个性化建议）→ 客观结果（准确率、UHK、群体准确率）。

### mapping_table

#### 1. 1

- theory_or_knowledge_claim_cn：人类选择概率与AI建议之间存在结构互补性，存在UHK和UAK；AI建议按效果强度e_t改变人类选择概率。

- mechanism_cn：正确AI建议会将错误答案引向正确，错误AI建议会将正确答案引向错误；总体效果取决于正确/错误建议的相对效应和相对UHK。

- design_requirement_cn：只有当正确建议的潜在收益超过错误建议的潜在伤害时，系统才应提供建议。

- artifact_choice_cn：标准AI建议界面；个性化建议的临界比规则。

- evaluated_contrast_cn：无建议 vs AI建议（实验1的T1/T2；实验3的T1'/T2'）。

- objective_result_cn：AI建议显著提高准确率并降低UHK；H1a/H1b获支持。

##### evidence_pointers

1. Experiment 1, Table 2

2. Experiment 3, Table 5

#### 2. 2

- theory_or_knowledge_claim_cn：人类若能更好判断AI的错误边界，就能区分正确与错误建议。

- mechanism_cn：呈现AI置信度可改变人类对建议的采纳：对低置信度错误建议减少遵从，对高置信度正确建议增加遵从。

- design_requirement_cn：把AI置信度转化为人类能理解并对照自身确信度的信息。

- artifact_choice_cn：在与人类相同的四点评分尺度上呈现AI置信度。

- evaluated_contrast_cn：AI建议 vs AI建议+置信度（T2 vs T3）。

- objective_result_cn：准确率无显著提升（0.801 vs 0.799），UHK显著提高（0.087 vs 0.073）；H2a未获支持、H2b获支持。

##### evidence_pointers

1. Experiment 1, Table 2 and Table 3

#### 3. 3

- theory_or_knowledge_claim_cn：不同人类对正确建议的收益和错误建议的伤害存在异质性。

- mechanism_cn：AI可估计每个个体的临界比r_h=harm/(harm+benefit)，当AI置信度低于临界比时撤回建议。

- design_requirement_cn：建议系统应个性化，而不是一视同仁地给所有用户同样的建议。

- artifact_choice_cn：前50张图像学习个体收益/伤害，后50张按是否超过临界比选择性显示AI建议。

- evaluated_contrast_cn：永久AI建议 vs 个性化AI建议（T2' vs T3'）。

- objective_result_cn：准确率不下降（0.795 vs 0.773），UHK显著提高（0.097 vs 0.074）；H3a/H3b获支持。

##### evidence_pointers

1. Experiment 3, Table 5

#### 4. 4

- theory_or_knowledge_claim_cn：群体智慧取决于个体准确率与预测多样性的平衡；AI建议提高前者但降低后者。

- mechanism_cn：随群体增大，正确建议的边际价值递减，而错误建议会促使大量个体选择同一错误选项，使众数选择变坏。

- design_requirement_cn：在群体决策环境中不能默认“一人一刀切”的AI建议，需要保护独特人类知识。

- artifact_choice_cn：用群体智慧仿真作为后果检验场景；将AI置信度和个性化建议作为缓解机制。

- evaluated_contrast_cn：无AI群体 vs AI建议群体 vs AI建议+置信度群体 vs 个性化AI建议群体。

- objective_result_cn：AI建议×组规模交互显著为负；AI置信度×组规模和个性化×组规模交互显著为正；个性化建议在所有规模下最优。

##### evidence_pointers

1. Wisdom of Crowds simulations, Figure 8-9, Table 6

#### 5. 5

- theory_or_knowledge_claim_cn：现代AI基于历史数据训练，其决策规则与人类不同，因此结构性互补会随人类盲目追随AI而消失。

- mechanism_cn：同质化决策使人类个体知识不再独立，多样性下降。

- design_requirement_cn：应让AI识别何时自己可能错误，并允许人类保留自己的判断。

- artifact_choice_cn：置信度提示和个性化建议都旨在让人类在不该听从AI时仍保留自身知识。

- evaluated_contrast_cn：对AI正确/错误图像分别考察置信度提示的影响。

- objective_result_cn：置信度提示增加了人类在AI错误图像上的准确率，但降低了在AI正确图像上的遵从度，导致总准确率未提升。

##### evidence_pointers

1. Experiment 1, Table 3 regression models

## 评价逻辑

### evaluation_modes

1. 解析模型与命题推导

2. 预注册的组间确认性实验（实验1、实验3）

3. 探索性被试内实验（实验2）

4. 图像级随机效应回归

5. 基于实验数据的Monte Carlo群体智慧仿真

6. 群体准确率回归分析

- why_these_evaluations_cn：个体层面的假设需要受试者实验来检验真实行为；实验2需要用被试内设计揭示收益/伤害异质性以便设计个性化规则；群体后果很难在实验室直接做大群体互动，因此作者用个体实验数据构造Monte Carlo群体仿真，把UHK损失转化为群体智慧效果。

- benchmark_and_contrast_chain_cn：无AI条件始终作为人类基线；实验1加入标准AI建议，再叠加AI置信度形成三条件阶梯；实验2用被试内无AI作为自己的基线；实验3用无AI和永久AI建议作为两个基准，检验个性化建议；群体仿真把三种处理群体放回同一抽样框架，按组规模累积对比，从而把个体差异转化为群体差异。

### claim_evidence_ledger

1. AI建议提升个体准确率：由实验1 T2 vs T1、实验3 T2' vs T1'支持。

2. AI建议降低独特人类知识：由实验1 T2 vs T1、实验3 T2' vs T1'支持。

3. AI置信度提升UHK但不提升准确率：由实验1 T3 vs T2、图像级回归支持。

4. 个性化建议不降低准确率并提高UHK：由实验3 T3' vs T2'支持。

5. AI建议在大群体中损害群体智慧：由两组群体仿真回归的AI advice × group size负交互支持。

6. AI置信度能部分恢复群体收益：由第一组仿真中AI certainty × group size正交互支持。

7. 个性化建议能同时保持个体和群体绩效：由第二组仿真中personalization × group size正交互及所有组规模最优支持。

8. Borgs和长期创新损失：属于理论性外推，缺乏长期追踪或组织层面直接证据。

- internal_validity_strategy_cn：预注册、先验功率分析、随机分配、注意力检查、人口统计学控制变量、Levene/异方差ANOVA、图像级随机效应模型控制图像和受试者异质性；实验2用被试内设计让同一人先后比较有无建议；群体仿真通过随机抽样和固定随机种子/迭代控制组规模比较。

- external_validity_strategy_cn：选择不需要专业训练的通用图像分类任务，宣称结果更易迁移；使用ImageNet和当时性能最强的GoogLeNet Inception v3，使AI具有代表性；用群体智慧作为“概念验证”，避免在真实组织中做昂贵随机实验；实验招募MTurk大面积人群。

- what_is_not_actually_tested_cn：没有真实团队互动或组织现场部署；没有长期追踪UHK损失是否影响学习和创新；个性化建议是离线阈值规则而非真正持续自适应的算法；AI置信度提示的准确率假设（H2a）未获支持；群体后果完全基于仿真而非真实人群协商；独特人类知识的操作化只是“AI错误而人类正确”的图像数，未直接触及知识/创新本质。

## 贡献闭环

- technical_claim_cn：AI建议可以通过标准界面提升个体图像分类准确率，但只提供AI自身置信度并不必然提升总准确率；个性化阈值规则能在不降低准确率的情况下保留更多独特人类知识。

- artifact_claim_cn：具体造成改进的可识别设计是：个性化AI建议——当AI估计置信度低于个体临界比时不显示建议；这一设计同时影响准确率和UHK。

- mechanism_claim_cn：机制是人类对AI建议的选择概率改变：正确建议带来收益，错误建议带来伤害；若人类/系统不能区分二者，就会损失UHK；个性化建议通过撤回高风险建议来保护UHK。

- boundary_claim_cn：结果适用于人类正确概率高于随机水平、AI建议具有可估计置信度、任务以离散分类形式呈现、群体以众数聚合的智慧众包环境；在更大的真实团队、不同任务类型和长期交互中可能不成立。

- reusable_design_knowledge_cn：AI建议系统不应默认把所有建议显示给所有人；可以估计个体对建议的收益/伤害，并用简单阈值规则决定何时给建议；在群体决策中更应避免“一刀切”建议，因为它会降低答案多样性。

- theoretical_contribution_cn：将AI建议文献从“能否提升绩效”扩展到“是否消耗人类互补性”；用多样性预测定理把个体UHK损失与群体智慧连接起来；为“损失多样性”机制提供了一个正式概率模型和实验证据。

- how_discussion_closes_intro_gap_cn：讨论部分重新回到引言中提出的被忽视UHK问题：AI建议确实提升个体绩效，但降低UHK和互补性，并对群体智慧造成严重损害；作者将实验中期未得到支持的H2a解释为置信度降低了对正确AI建议的遵从，并用个性化建议作为替代方案，从而闭合了“能否缓解”的缺口。

- overclaim_or_unsupported_leaps_cn：从图片分类实验中UHK下降外推到“长期创新受损”“人类变成Borgs”属于修辞性跳跃，缺少长期/组织证据；H2a未获支持，却在讨论和建议中仍强调置信度作为缓解工具；群体结果依赖Monte Carlo仿真，未用真实互动群体检验；个性化建议虽然在个体和大群体仿真中都有效，但未检验真实组织中的算法适配和用户接受。

## 句级写作动作图谱

### 1. Abstract, first paragraph

- order：1

- section：Abstract

- locator：Abstract, first paragraph

- move_code：STUDY_OVERVIEW

- paraphrase_cn：作者宣告研究分析AI建议如何影响人机互补性，尤其是人类独有而AI没有的知识。

- rhetorical_function_cn：开篇直接给出研究对象，明确“UHK”为贯穿全文的核心概念。

- depends_on_cn：无。

- sets_up_cn：为摘要后半部分的发现和贡献做铺垫。

- evidence_pointer：Abstract P1

### 2. Abstract, first paragraph

- order：2

- section：Abstract

- locator：Abstract, first paragraph

- move_code：RESULT

- paraphrase_cn：主要发现是人类选择向相似回答收敛，个体准确率提升，但个体UHK下降。

- rhetorical_function_cn：在摘要层面先给出核心实证结果，制造张力：个体变好但独特性变差。

- depends_on_cn：依赖上一句对UHK的定义。

- sets_up_cn：为“Borgs”隐喻和群体后果提供证据基础。

- evidence_pointer：Abstract P1

### 3. Abstract, first paragraph

- order：3

- section：Abstract

- locator：Abstract, first paragraph

- move_code：CONTRIBUTION

- paraphrase_cn：作者把与AI交互的人类比作Borgs，即个体绩效强但人类个性消失的生化人。

- rhetorical_function_cn：用有冲击力的标签概括发现，使抽象损失具象化。

- depends_on_cn：依赖前面对趋同结果的描述。

- sets_up_cn：为讨论部分的Borgs隐喻和多样性价值埋下伏笔。

- evidence_pointer：Abstract P1

### 4. Abstract, second paragraph

- order：4

- section：Abstract

- locator：Abstract, second paragraph

- move_code：RESULT

- paraphrase_cn：作者说这种UHK损失会导致多种不良后果，并用仿真证明AI协助群体比无AI群体更不有效。

- rhetorical_function_cn：把个体损失升级到群体后果，强调研究不只是心理测量。

- depends_on_cn：依赖“Borgs”概念和群体智慧设想。

- sets_up_cn：为“需要缓解技术”的论述做铺垫。

- evidence_pointer：Abstract P2

### 5. Abstract, second paragraph

- order：5

- section：Abstract

- locator：Abstract, second paragraph

- move_code：CONTRIBUTION

- paraphrase_cn：作者提出个性化AI建议等缓解技术，并称它们在个体和群体智慧上都表现良好。

- rhetorical_function_cn：摘要以正面解决方案收尾，暗示设计贡献。

- depends_on_cn：依赖前面识别出的群体损害问题。

- sets_up_cn：为正文中两个干预的测试提供预告。

- evidence_pointer：Abstract P2

### 6. Introduction, first paragraph

- order：6

- section：Introduction

- locator：Introduction, first paragraph

- move_code：CONTEXT

- paraphrase_cn：AI将如何改变工作场所充满期望与不确定性，许多过去被认为不可自动化的任务现在由机器完成。

- rhetorical_function_cn：建立宽泛现实背景，说明AI议题重要。

- depends_on_cn：无。

- sets_up_cn：引出“人类仍会留在回路中”的前提。

- evidence_pointer：Introduction P1

### 7. Introduction, first paragraph

- order：7

- section：Introduction

- locator：Introduction, first paragraph

- move_code：PRACTICAL_STAKES

- paraphrase_cn：即使完全自动化在技术上可行，伦理和法律问题仍使许多任务依赖人类输入；人类还能补充算法。

- rhetorical_function_cn：说明研究人类与AI协作不是过渡问题，而是长期结构性现实。

- depends_on_cn：依赖背景段对自动化的描述。

- sets_up_cn：为人机互补性研究提供合理性。

- evidence_pointer：Introduction P1

### 8. Introduction, second paragraph

- order：8

- section：Introduction

- locator：Introduction, second paragraph

- move_code：CONTEXT

- paraphrase_cn：作者进入AI建议型人类决策领域，说明典型应用包括医疗和法律支持。

- rhetorical_function_cn：将研究嵌入具体文献流，同时限定研究范围。

- depends_on_cn：依赖前面对人机协作的背景。

- sets_up_cn：为随后指出现有文献只关心绩效做铺垫。

- evidence_pointer：Introduction P2

### 9. Introduction, second paragraph

- order：9

- section：Introduction

- locator：Introduction, second paragraph

- move_code：LIMITATION

- paraphrase_cn：该文献流的重点是把绩效最大化，作者则关注被忽视的AI建议对UHK的影响。

- rhetorical_function_cn：构造“文献缺陷”，确立本文差异化位置。

- depends_on_cn：依赖上一句对AI建议研究领域的介绍。

- sets_up_cn：引出UHK及后续群体智慧证明。

- evidence_pointer：Introduction P2

### 10. Introduction, third paragraph

- order：10

- section：Introduction

- locator：Introduction, third paragraph

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：独特人类知识普遍被AI建议文献视为人机互补性的来源，并被认为对协作环境有正面作用。

- rhetorical_function_cn：引用已有文献证明UHK概念并非作者编造，而是被广泛接受。

- depends_on_cn：依赖前面对UHK的引入。

- sets_up_cn：为“失去UHK很危险”的论点提供理论依据。

- evidence_pointer：Introduction P3

### 11. Introduction, third paragraph

- order：11

- section：Introduction

- locator：Introduction, third paragraph

- move_code：PRACTICAL_STAKES

- paraphrase_cn：与AI协作的人类若失去独特知识，会对长期绩效、持续改进和创新极其不利。

- rhetorical_function_cn：提示即使个体短期获益，长期系统代价可能巨大。

- depends_on_cn：依赖UHK重要性的文献。

- sets_up_cn：为研究问题“如何缓解损失”提供紧迫性。

- evidence_pointer：Introduction P3

### 12. Introduction, fourth paragraph

- order：12

- section：Introduction

- locator：Introduction, fourth paragraph

- move_code：MECHANISM

- paraphrase_cn：现代AI基于数据训练，与人类决策规则不同，因此存在结构性互补；UHK是AI没有而人类有的知识。

- rhetorical_function_cn：用结构性互补解释UHK为什么存在，并说明AI与人类决策规则差异。

- depends_on_cn：依赖前面关于UHK的讨论。

- sets_up_cn：为模型定义UHK/UAK和后续推导提供概念架构。

- evidence_pointer：Introduction P4

### 13. Introduction, fifth paragraph

- order：13

- section：Introduction

- locator：Introduction, fifth paragraph

- move_code：RQ_OR_OBJECTIVE

- paraphrase_cn：作者明确提出三个研究问题：AI建议如何影响准确率和UHK、如何缓解UHK损失、UHK损失对群体智慧有什么后果。

- rhetorical_function_cn：把背景转化为可研究的三个具体问题，构成全文组织骨架。

- depends_on_cn：依赖文献缺口和UHK概念。

- sets_up_cn：为分析模型、实验和群体仿真提供目标清单。

- evidence_pointer：Introduction P5

### 14. Introduction, fifth paragraph

- order：14

- section：Introduction

- locator：Introduction, fifth paragraph

- move_code：STUDY_OVERVIEW

- paraphrase_cn：作者预告用解析模型发展并支持假设，再用系列实验验证理论洞见。

- rhetorical_function_cn：提前说明多方法设计，让读者知道后续章节。

- depends_on_cn：依赖三个研究问题。

- sets_up_cn：为论文的方法逐层展开做路标。

- evidence_pointer：Introduction P5

### 15. Introduction, sixth paragraph

- order：15

- section：Introduction

- locator：Introduction, sixth paragraph

- move_code：CONTRIBUTION

- paraphrase_cn：关键洞见是即使AI建议成功把个体抬到优于AI的表现，也会减少人类相对AI的独特知识。

- rhetorical_function_cn：以最浓缩形式宣告全文核心发现，制造反直觉张力。

- depends_on_cn：依赖前面的理论推导预告。

- sets_up_cn：为两个干预实验和群体后果的讨论确定焦点。

- evidence_pointer：Introduction P6

### 16. Introduction, seventh paragraph

- order：16

- section：Introduction

- locator：Introduction, seventh paragraph

- move_code：DESIGN_FEATURE

- paraphrase_cn：作者描述两个干预：呈现AI自身置信度，以及提供个性化AI建议。

- rhetorical_function_cn：把研究问题转化为具体可测设计变量。

- depends_on_cn：依赖模型中对建议效果e_t和个体临界比的概念。

- sets_up_cn：为实验1和实验3的设计做预告。

- evidence_pointer：Introduction P7

### 17. Introduction, ninth paragraph

- order：17

- section：Introduction

- locator：Introduction, ninth paragraph

- move_code：RESULT

- paraphrase_cn：作者宣告群体智慧恶果：AI建议改善个体和小群体，但显著损害较大群体；置信度缓解不彻底，个性化建议表现良好。

- rhetorical_function_cn：把个体层面结果延伸到群体层面，提前给出全文主要结论。

- depends_on_cn：依赖两个干预的设计描述。

- sets_up_cn：为群体智慧仿真章节定了结论导向。

- evidence_pointer：Introduction P9

### 18. Literature Review, first paragraph

- order：18

- section：Literature Review

- locator：Literature Review, first paragraph

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：从Huber和Leidner/Elam开始，早期信息技术决策支持研究已识别组织智能和信息源等互补性。

- rhetorical_function_cn：把研究放在更长的IS传统中，说明问题有历史渊源。

- depends_on_cn：无需前文。

- sets_up_cn：为“但没有人讨论建议对任务层面互补性的影响”做铺垫。

- evidence_pointer：Literature Review P1

### 19. Literature Review, second paragraph

- order：19

- section：Literature Review

- locator：Literature Review, second paragraph

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：综述AI建议文献，特别是提供AI置信度和说明对人类绩效的影响。

- rhetorical_function_cn：概括现有知识，让读者看到AI建议研究的主流问题。

- depends_on_cn：依赖对AI建议领域的界定。

- sets_up_cn：为指出置信度效果不一致的文献缺口做准备。

- evidence_pointer：Literature Review P2

### 20. Literature Review, second paragraph

- order：20

- section：Literature Review

- locator：Literature Review, second paragraph

- move_code：LIMITATION

- paraphrase_cn：作者总结AI置信度或解释性信息的效果在实验中是不一致的，有些研究增加遵从但没有准确率提升。

- rhetorical_function_cn：指出文献中关于置信度干预的经验结论混杂。

- depends_on_cn：依赖上一句对相关研究的列举。

- sets_up_cn：为作者自己在H2a上的未支持结果提供上下文。

- evidence_pointer：Literature Review P2

### 21. Literature Review, second paragraph

- order：21

- section：Literature Review

- locator：Literature Review, second paragraph

- move_code：GAP

- paraphrase_cn：作者强调据其所知，没有研究讨论AI建议对独特人类知识的影响。

- rhetorical_function_cn：明确本文的核心文献缺口。

- depends_on_cn：依赖前面对AI建议文献的综述。

- sets_up_cn：为全文以UHK为中心的理论模型和实验做铺垫。

- evidence_pointer：Literature Review P2

### 22. Literature Review, third paragraph

- order：22

- section：Literature Review

- locator：Literature Review, third paragraph

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：综述群体智慧、Galton称牛实验、多样性预测定理以及群体多样性下降的研究。

- rhetorical_function_cn：为群体智慧后果提供既有理论支撑。

- depends_on_cn：无直接依赖，但承接缺少群体视角的缺口。

- sets_up_cn：为H4a-H4c和群体仿真建立基础。

- evidence_pointer：Literature Review P3

### 23. Literature Review, third paragraph

- order：23

- section：Literature Review

- locator：Literature Review, third paragraph

- move_code：GAP

- paraphrase_cn：虽然群体智慧研究指出多样性下降会降低群体表现，但没有研究测试个体AI建议对群体多样性和表现的影响。

- rhetorical_function_cn：将两个文献流（AI建议和群体智慧）合并，形成交叉缺口。

- depends_on_cn：依赖前面对群体智慧文献的总结。

- sets_up_cn：为群体智慧理论框架和实验仿真做预告。

- evidence_pointer：Literature Review P3

### 24. Theoretical Framework, opening paragraph

- order：24

- section：Theoretical Framework: Individual Decision Making

- locator：Theoretical Framework, opening paragraph

- move_code：THEORY_INTRO

- paraphrase_cn：作者提出一个简单的离散选择模型，用来计算人类准确率、AI准确率、UHK和UAK。

- rhetorical_function_cn：用最小模型定义全部关键变量。

- depends_on_cn：依赖引言中的UHK概念。

- sets_up_cn：为后续所有命题和假设提供数学语言。

- evidence_pointer：Theoretical Framework: Individual Decision Making, opening

### 25. Effect of AI Advice on Performance, after Equation (5)

- order：25

- section：Theoretical Framework: Individual Decision Making

- locator：Effect of AI Advice on Performance, after Equation (5)

- move_code：MECHANISM

- paraphrase_cn：AI建议以e_t强度提高被推荐选项的选择概率，因此正确建议带来收益、错误建议带来伤害。

- rhetorical_function_cn：用概率模型解释AI建议为何既可能帮助也可能伤害个体。

- depends_on_cn：依赖式(5)对p_tc^AI的定义。

- sets_up_cn：为命题1和H1a准备条件。

- evidence_pointer：Effect of AI Advice on Performance, Equations (5)-(7)

### 26. Effect of AI Advice on Performance, Proposition 1

- order：26

- section：Theoretical Framework: Individual Decision Making

- locator：Effect of AI Advice on Performance, Proposition 1

- move_code：THEORY_PROPOSITION

- paraphrase_cn：当正确建议相对错误的缩放因子大于相对UHK时，AI建议的总绩效效应为正。

- rhetorical_function_cn：给出AI建议有益的精确条件，使假设可检验。

- depends_on_cn：依赖式(8)关于ΔAI与UAK/UHK的关系。

- sets_up_cn：为H1a提供理论依据。

- evidence_pointer：Proposition 1

### 27. Effect of AI Advice on Performance, before Hypothesis 1a

- order：27

- section：Theoretical Framework: Individual Decision Making

- locator：Effect of AI Advice on Performance, before Hypothesis 1a

- move_code：HYPOTHESIS_OR_PROPOSITION

- paraphrase_cn：作者给出三条件假设：存在互补性、AI准确率至少不劣于人类、人类能区分正确与错误建议，于是预测AI建议提升准确率。

- rhetorical_function_cn：把模型条件转成可实证检验的H1a。

- depends_on_cn：依赖命题1和三组常用假设。

- sets_up_cn：为实验1的T1/T2比较提供目标。

- evidence_pointer：Hypothesis 1a

### 28. Effect of AI Advice on Unique Human Knowledge, after Equation (12)

- order：28

- section：Theoretical Framework: Individual Decision Making

- locator：Effect of AI Advice on Unique Human Knowledge, after Equation (12)

- move_code：MECHANISM

- paraphrase_cn：只要人类在错误AI建议上赋予任何权重，AI建议就会降低UHK。

- rhetorical_function_cn：推出反直觉核心机制：即使个体准确率提升，UHK必然下降。

- depends_on_cn：依赖式(11)-(12)对ΔUHK^AI的推导。

- sets_up_cn：为H1b和全文核心贡献提供理论。

- evidence_pointer：Equations (10)-(12), Hypothesis 1b

### 29. Providing AI’s Certainty, Proposition 2

- order：29

- section：Theoretical Framework: Individual Decision Making

- locator：Providing AI’s Certainty, Proposition 2

- move_code：THEORY_PROPOSITION

- paraphrase_cn：命题2给出呈现AI置信度能提升总体绩效的三种条件，核心是让人类在错误建议上减少遵从、在正确建议上增加遵从。

- rhetorical_function_cn：把“如何缓解UHK损失”的第一个设计翻译成精确命题。

- depends_on_cn：依赖s_t和δ_s的模型。

- sets_up_cn：为H2a/H2b提供条件。

- evidence_pointer：Providing AI’s Certainty, Proposition 2

### 30. Providing AI’s Certainty, before Hypothesis 2a

- order：30

- section：Theoretical Framework: Individual Decision Making

- locator：Providing AI’s Certainty, before Hypothesis 2a

- move_code：HYPOTHESIS_OR_PROPOSITION

- paraphrase_cn：作者假设提供AI置信度会提升准确率，因为人类能更好判断AI何时犯错。

- rhetorical_function_cn：将命题2转化为实验可检验假设。

- depends_on_cn：依赖Bansal等关于错误边界的心智模型文献。

- sets_up_cn：为实验1的T3条件提供预期。

- evidence_pointer：Hypothesis 2a

### 31. Providing AI’s Certainty, after Equation (21)

- order：31

- section：Theoretical Framework: Individual Decision Making

- locator：Providing AI’s Certainty, after Equation (21)

- move_code：HYPOTHESIS_OR_PROPOSITION

- paraphrase_cn：作者假设提供AI置信度能增加UHK，因为置信度可以让人类减少对错误建议的遵从。

- rhetorical_function_cn：把第二个干预与核心结果变量UHK连接。

- depends_on_cn：依赖式(20)-(21)对ΔUHK^cert的推导。

- sets_up_cn：为实验1的UHK结果提供预期。

- evidence_pointer：Hypothesis 2b

### 32. Personalized Suggestions, after Equation (25)

- order：32

- section：Theoretical Framework: Individual Decision Making

- locator：Personalized Suggestions, after Equation (25)

- move_code：MECHANISM

- paraphrase_cn：AI根据个体收益/伤害的临界比决定是否提供建议；若置信度低于临界比则撤回建议。

- rhetorical_function_cn：说明个性化建议的可操作规则来自模型中的期望收益/伤害比较。

- depends_on_cn：依赖d_th、e_th和临界比r_h的定义。

- sets_up_cn：为实验3的个性化算法提供理论公式。

- evidence_pointer：Personalized Suggestions, Equations (22)-(25)

### 33. Personalized Suggestions, Proposition 3

- order：33

- section：Theoretical Framework: Individual Decision Making

- locator：Personalized Suggestions, Proposition 3

- move_code：THEORY_PROPOSITION

- paraphrase_cn：当正确建议相对效果的个体缩放因子小于相对UHK变化时，个性化建议总体有益。

- rhetorical_function_cn：给出第二个干预有效的理论条件。

- depends_on_cn：依赖式(26)-(27)对Δper_h的推导。

- sets_up_cn：为H3a/H3b提供支持。

- evidence_pointer：Proposition 3

### 34. Personalized Suggestions, before Hypothesis 3a

- order：34

- section：Theoretical Framework: Individual Decision Making

- locator：Personalized Suggestions, before Hypothesis 3a

- move_code：HYPOTHESIS_OR_PROPOSITION

- paraphrase_cn：作者保守假设个性化建议不会使准确率下降，并会增加UHK。

- rhetorical_function_cn：把命题3转成两个可检验假设。

- depends_on_cn：依赖个性化建议的收益-伤害逻辑。

- sets_up_cn：为实验3的T2'/T3'比较提供预期。

- evidence_pointer：Hypotheses 3a-3b

### 35. Illustrative Example, before Proposition 4

- order：35

- section：Theoretical Framework: Wisdom of Crowds

- locator：Illustrative Example, before Proposition 4

- move_code：THEORY_INTRO

- paraphrase_cn：用两个选项、三个人的简单例子说明：所有人类都跟随AI时，群体准确率等于AI准确率，而不跟随AI的独立群体通过多数投票可以超过AI。

- rhetorical_function_cn：用最小例子让读者直观看到多样性损失的代价。

- depends_on_cn：依赖个体层模型中的p_t1和AI准确率。

- sets_up_cn：为命题4和群体阈值提供论证。

- evidence_pointer：Theoretical Framework: Wisdom of Crowds, Illustrative Example

### 36. Illustrative Example, Proposition 4

- order：36

- section：Theoretical Framework: Wisdom of Crowds

- locator：Illustrative Example, Proposition 4

- move_code：THEORY_PROPOSITION

- paraphrase_cn：在二选一且正确选项概率较高的情境中，存在足够大的群体，使群体准确率超过任何低于1的阈值。

- rhetorical_function_cn：用Hoeffding不等式证明“大群体无AI也能非常准”。

- depends_on_cn：依赖式(29)-(30)的概率上界。

- sets_up_cn：为H4a关于AI建议在群体中边际效益递减提供理论基础。

- evidence_pointer：Proposition 4

### 37. Effect of AI Advice on Wisdom of Crowds’ Performance, after Figures 1-2

- order：37

- section：Theoretical Framework: Wisdom of Crowds

- locator：Effect of AI Advice on Wisdom of Crowds’ Performance, after Figures 1-2

- move_code：MECHANISM

- paraphrase_cn：正确建议加速群体收敛，但错误建议则使群体走向错误众数；在较大群体中无AI人类群体的优势出现。

- rhetorical_function_cn：解释数值仿真结果背后的机制，为群体假设做铺垫。

- depends_on_cn：依赖图1和图2的计算结果。

- sets_up_cn：为H4a-H4c提供机制理由。

- evidence_pointer：Theoretical Framework: Wisdom of Crowds, Effect of AI Advice, Figures 1-2

### 38. General Experimental Design, first paragraph

- order：38

- section：Experimental Studies: Individual Decision Making

- locator：General Experimental Design, first paragraph

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：作者选择图像分类作为实验任务，因为它是通用任务、现代AI表现好、且AI与人类使用的分类方法不同，因此能产生UHK。

- rhetorical_function_cn：为实验任务选择提供方法论辩护，增强结论可推广性。

- depends_on_cn：依赖本文对UHK的定义。

- sets_up_cn：为后续图像实验的细节介绍做准备。

- evidence_pointer：Experimental Studies: Individual Decision Making, General Experimental Design

### 39. General Experimental Design, after Table 1

- order：39

- section：Experimental Studies: Individual Decision Making

- locator：General Experimental Design, after Table 1

- move_code：DESIGN_FEATURE

- paraphrase_cn：所有研究包含无AI和AI建议两种主条件，AI建议来自GoogLeNet Inception v3，并以最高置信度类别作为推荐。

- rhetorical_function_cn：说明AI制品的来源和基础条件设置。

- depends_on_cn：依赖图像分类任务选择。

- sets_up_cn：为实验1中的三个处理条件提供基础。

- evidence_pointer：General Experimental Design, Figures 3-4

### 40. Experiment 1, Hypotheses and Study Design

- order：40

- section：Experimental Studies: Individual Decision Making

- locator：Experiment 1, Hypotheses and Study Design

- move_code：HYPOTHESIS_OR_PROPOSITION

- paraphrase_cn：作者把实验1要检验的四个假设写出：AI建议提升准确率、降低UHK；AI置信度进一步提升准确率、提升UHK。

- rhetorical_function_cn：把理论假设直接绑定到T1/T2/T3比较。

- depends_on_cn：依赖理论框架中的H1-H2。

- sets_up_cn：为结果部分的统计检验提供清晰预期。

- evidence_pointer：Experiment 1, Hypotheses and Study Design

### 41. Experiment 1, Study Protocol

- order：41

- section：Experimental Studies: Individual Decision Making

- locator：Experiment 1, Study Protocol

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：作者说明实验遵循预注册、功率分析、MTurk筛选、注意力检查和稳健性控制人口学变量。

- rhetorical_function_cn：增强确认性实验的内部效度和可信度。

- depends_on_cn：依赖对假设的预注册要求。

- sets_up_cn：为结果部分的ANOVA和回归解读提供方法保障。

- evidence_pointer：Experiment 1, Study Protocol

### 42. Experiment 1, Results

- order：42

- section：Experimental Studies: Individual Decision Making

- locator：Experiment 1, Results

- move_code：RESULT

- paraphrase_cn：统计结果支持H1a和H1b；H2a不支持，H2b支持；额外发现AI建议后的准确率显著超过AI本身。

- rhetorical_function_cn：给出实验1对理论假设的检验结果，区分支持与未支持。

- depends_on_cn：依赖实验1的三个处理条件。

- sets_up_cn：为图像级回归解释H2a未支持以及实验2的异质性研究做衔接。

- evidence_pointer：Experiment 1, Results, Table 2, Figure 5

### 43. Experiment 1, Results, regression discussion

- order：43

- section：Experimental Studies: Individual Decision Making

- locator：Experiment 1, Results, regression discussion

- move_code：ROBUSTNESS_OR_BOUNDARY_TEST

- paraphrase_cn：图像级回归显示置信度提高了AI错误图像上的准确率，却降低了AI正确图像上的准确率，说明置信度让人类总体减少对AI的遵从。

- rhetorical_function_cn：解释为什么总准确率没有提升，为H2a的未支持结果提供机制性解释。

- depends_on_cn：依赖表3的回归结果。

- sets_up_cn：为后面“置信度只能部分缓解”的结论和个性化建议的转向铺垫。

- evidence_pointer：Experiment 1, Results, Table 3

### 44. Experiment 2, Study Design

- order：44

- section：Experimental Studies: Individual Decision Making

- locator：Experiment 2, Study Design

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：作者用被试内设计让每位受试者先无建议再看到AI建议，以测量个体层面的收益和伤害，并称该实验是探索性的。

- rhetorical_function_cn：说明实验2的定位不是假设检验，而是为个性化建议提供异质性证据。

- depends_on_cn：依赖实验1提出的个体反应差异问题。

- sets_up_cn：为实验3个性化算法提供经验理由。

- evidence_pointer：Experiment 2, Study Design

### 45. Experiment 2, Results

- order：45

- section：Experimental Studies: Individual Decision Making

- locator：Experiment 2, Results

- move_code：RESULT

- paraphrase_cn：所有受试者都从AI建议中获益，但个体收益和伤害的变异性非常大，且不能简单归因于遵从度。

- rhetorical_function_cn：证明个性化建议有存在空间。

- depends_on_cn：依赖表4和图6的数据。

- sets_up_cn：为实验3的个性化设计提供直接依据。

- evidence_pointer：Experiment 2, Results, Table 4, Figure 6

### 46. Experiment 3, Hypotheses and Study Design

- order：46

- section：Experimental Studies: Individual Decision Making

- locator：Experiment 3, Hypotheses and Study Design

- move_code：DESIGN_FEATURE

- paraphrase_cn：作者把AI建议个性化实现为：前50张图像估计个体收益和伤害，计算临界比，后50张只在AI置信度超过临界比时显示建议。

- rhetorical_function_cn：把理论中的临界比规则变成一个可执行的实验设计。

- depends_on_cn：依赖实验2的异质性发现和理论式(25)。

- sets_up_cn：为实验3的T3'条件和H3a/H3b检验做准备。

- evidence_pointer：Experiment 3, Hypotheses and Study Design

### 47. Experiment 3, Results

- order：47

- section：Experimental Studies: Individual Decision Making

- locator：Experiment 3, Results

- move_code：RESULT

- paraphrase_cn：个性化建议的准确率不显著低于永久建议，且显著高于无建议；UHK显著高于永久建议，与无建议无显著差异。

- rhetorical_function_cn：支持H3a和H3b，证明个性化设计同时保住了准确率和UHK。

- depends_on_cn：依赖实验3的三个条件和表5数据。

- sets_up_cn：为群体智慧仿真提供可用于比较的实验总体。

- evidence_pointer：Experiment 3, Results, Table 5, Figure 7

### 48. Simulation Setup and Hypotheses

- order：48

- section：Experimental Studies: Wisdom of Crowds

- locator：Simulation Setup and Hypotheses

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：作者用实验处理组作为总体，随机抽样不同规模群体，以众数聚合、随机平局处理，进行Monte Carlo模拟。

- rhetorical_function_cn：说明群体后果如何由个体实验数据构造出来，而不需要真实大群体实验。

- depends_on_cn：依赖实验1和实验3产生的处理组样本。

- sets_up_cn：为H4a-H4c的仿真检验提供方法。

- evidence_pointer：Experimental Studies: Wisdom of Crowds, Simulation Setup

### 49. Wisdom of Crowds: Experiment 1, Results

- order：49

- section：Experimental Studies: Wisdom of Crowds

- locator：Wisdom of Crowds: Experiment 1, Results

- move_code：RESULT

- paraphrase_cn：无AI群体从组规模约7起超过仅AI建议群体，从约11起超过AI建议+置信度群体；回归中AI建议×组规模为负，AI置信度×组规模为正。

- rhetorical_function_cn：用仿真和回归支持H4a与H4b，并量化阈值。

- depends_on_cn：依赖图8和表6左侧回归。

- sets_up_cn：引出“UHK损失在群体中很重要”的结论。

- evidence_pointer：Figure 8, Table 6 left column

### 50. Wisdom of Crowds: Experiment 3, Results

- order：50

- section：Experimental Studies: Wisdom of Crowds

- locator：Wisdom of Crowds: Experiment 3, Results

- move_code：RESULT

- paraphrase_cn：个性化AI建议在所有群体规模上都优于无AI和永久AI建议，回归显示个性化×组规模交互为正。

- rhetorical_function_cn：支持H4c，证明第二个干预能解决群体智慧损害。

- depends_on_cn：依赖图9和表6右侧回归。

- sets_up_cn：为讨论部分的决策支持系统建议提供正面证据。

- evidence_pointer：Figure 9, Table 6 right column

### 51. Insights in Human-AI Collaboration

- order：51

- section：Discussion and Conclusions

- locator：Insights in Human-AI Collaboration

- move_code：CONTRIBUTION

- paraphrase_cn：作者重申研究揭示两个效应：个体准确率提升和独特人类知识下降，并说明后者影响人机及人与人之间的互补性。

- rhetorical_function_cn：把实证结果回收到引言提出的缺口，完成回答。

- depends_on_cn：依赖所有实验和仿真结果。

- sets_up_cn：为AI决策支持系统设计含义铺路。

- evidence_pointer：Discussion, Insights in Human-AI Collaboration

### 52. Implications for AI-Based Decision Support Systems

- order：52

- section：Discussion and Conclusions

- locator：Implications for AI-Based Decision Support Systems

- move_code：CONTRIBUTION

- paraphrase_cn：作者提出三个设计含义：简单建议界面能实现人机互补；给群体提供同样的AI建议有严重缺点；现代AI可用置信度和个体学习来克服这一缺点。

- rhetorical_function_cn：把文章结果转化为可操作的设计知识，提升实践相关性。

- depends_on_cn：依赖实验3和仿真中个性化建议的成功。

- sets_up_cn：为未来研究和Borgs讨论建立落点。

- evidence_pointer：Discussion, Implications for AI-Based Decision Support Systems

### 53. Limitations and Future Research

- order：53

- section：Discussion and Conclusions

- locator：Limitations and Future Research

- move_code：LIMITATION_AND_FUTURE

- paraphrase_cn：作者列出三类局限：可能有其他更好的AI协助设计；真实团队行为可能依赖任务类型；未来应研究更复杂的人机交互设置和长期效应。

- rhetorical_function_cn：防止贡献被理解为最终答案，同时开启后续研究空间。

- depends_on_cn：依赖全文结果的边界意识。

- sets_up_cn：为最后Borgs段落提供平衡。

- evidence_pointer：Discussion, Limitations and Future Research

### 54. Will Humans Become Borgs?

- order：54

- section：Discussion and Conclusions

- locator：Will Humans Become Borgs?

- move_code：CONTRIBUTION

- paraphrase_cn：作者用Borgs问题收尾：人类因AI而进步，但行为趋同并失去互补性；多样性是长期超越AI的关键，而个性化建议可缓解这种损失。

- rhetorical_function_cn：用命题式标题重新包装全文贡献，使论文在理论讨论之外有记忆点。

- depends_on_cn：依赖所有个体和群体层面的结果。

- sets_up_cn：为读者留下关于人类长期价值的思考。

- evidence_pointer：Discussion, Will Humans Become Borgs? 

## 写作技术

- gap_construction_cn：作者不是简单说“没人研究AI建议与独特知识”，而是先承认AI建议文献很成熟，再指出其主流目标只是最大化绩效；同时指出群体智慧文献已经知道多样性下降有害，但没有考虑到“每个个体都接同一个外部AI信号”这一来源。于是缺口出现在两个文献流的交叉处。

- signposting_cn：引言末尾明确预告“个体模型→实验→群体仿真→结论”；每个理论小节以“Next, we derive conditions for...”等表述推进；实验部分用Table 1总览三个实验的目的，并在每段实验结束后说明为什么要进入下一个实验。

- transition_logic_cn：实验1结果中置信度未提升准确率，转而用图像级回归解释，再引出实验2探讨异质性；实验2发现异质性后直接提出“因此个性化建议可能是有效方向”；个体实验结束后用“作为概念验证，我们扩展群体智慧模型并仿真”的过渡进入群体部分。

- claim_evidence_rhythm_cn：每个理论命题后紧跟可检验假设；每个实验先给假设，再给统计结果，最后解释支持或不支持的机制；关键处使用“我们并未发现足够支持”而不是只报正结果，增强可信度。

- benchmark_narrative_cn：无AI条件始终作为人类基线，逐步叠加AI建议、AI置信度、个性化建议，构成递进式比较；群体仿真中使用同一样本重新抽样，使不同处理在相同组规模下可比，形成清晰的阈值叙事（组规模约7和11开始反超）。

- theory_return_cn：讨论部分不是重复结果，而是用“个体准确率提升”“UHK下降”“群体智慧受损”“个性化可缓解”四层结果返回到互补性和多样性预测定理，并用Borgs隐喻把理论贡献上升为关于人类长期价值的命题。

- contribution_positioning_cn：作者把贡献定位为“被忽视的副作用”而不是“更好的AI”；每一次贡献声明都强调UHK是连接人机互补性与群体智慧的关键变量，从而避免被视为一次性实验结果。

- novelty_protection_cn：通过解析模型先证明UHK下降是结构性的，而不仅是数据偶然；用预注册和功率分析减少事后解释嫌疑；用图像级回归解释未支持假设；用仿真说明群体后果不是因为实验任务特殊；最后用第二个干预的成功说明损失可被设计修复。

## 可复用研究与写作程序

### structure_steps

#### 1. 1

- step：1

- writing_job_cn：把一个看似常识的协作问题（人机协作）聚焦到一个被忽视的构念（独特人类知识），并说明其现实后果。

- research_job_cn：定义核心构念，找到已有文献承认但未系统研究的知识点。

- required_evidence_cn：需要文献证据表明该构念在多个领域重要，且现有AI建议文献未将其作为结果变量。

- transition_to_next_cn：“既然没人研究UHK，我们需要一个能度量UHK的框架”引出理论模型。

#### 2. 2

- step：2

- writing_job_cn：用形式化模型定义变量、推导核心效应和干预条件，并把命题转成假设。

- research_job_cn：建立最小但足够精确的概率模型，计算AI建议的收益/伤害与UHK变化。

- required_evidence_cn：数学推导需要能产生反直觉结论（个体更好但独特性更差），并且能区分两种干预。

- transition_to_next_cn：“理论需要被真实人类行为检验”引出预注册实验。

#### 3. 3

- step：3

- writing_job_cn：设计确认性实验检验理论假设，同时在实验内部嵌入机制探索（回归/调查）来解释未支持假设。

- research_job_cn：选择通用任务和现有高质量AI，设置无AI/AI建议/干预的组间对比，并做功率分析、随机化和预注册。

- required_evidence_cn：需要观察到个体准确率和UHK的显著变化，并能说明未预期结果不是随机噪声。

- transition_to_next_cn：若主假设只有部分被支持，用探索性实验检查机制细节。

#### 4. 4

- step：4

- writing_job_cn：用探索性研究揭示个体异质性，把“平均效应”拆成“收益/伤害”分布。

- research_job_cn：采用被试内设计测量每位受试者的收益和伤害，证明不同人需要不同帮助。

- required_evidence_cn：需要显示变异足够大且不能用简单遵从度解释，为个性化干预提供必要性。

- transition_to_next_cn：“既然个体差异大，下一步设计个性化规则”引出干预实验。

#### 5. 5

- step：5

- writing_job_cn：把理论中的干预规则实作成可执行设计，并用第二轮预注册实验检验。

- research_job_cn：实现个性化阈值算法，在训练/测试两阶段上比较个性化与永久建议。

- required_evidence_cn：需要证明干预不降低准确率并显著恢复UHK。

- transition_to_next_cn：“个体层面成功，但群体中是否有意义”引出群体仿真。

#### 6. 6

- step：6

- writing_job_cn：用个体实验数据构造群体仿真，把个体结果升级为群体后果，并用回归检验交互效应。

- research_job_cn：设计Monte Carlo抽样、众数聚合、随机平局处理，计算组规模阈值和交互系数。

- required_evidence_cn：需要得到组规模×AI建议显著为负、组规模×干预显著为正的结果。

- transition_to_next_cn：“结果支持了理论预测”进入讨论，回到理论和设计含义。

#### 7. 7

- step：7

- writing_job_cn：在讨论中把个体/群体结果重新组织为对理论缺口和设计原则的回应，并用一个隐喻（Borgs）保护贡献。

- research_job_cn：总结哪些主张有直接证据、哪些属于外推，明确提出边界条件和未来研究。

- required_evidence_cn：需要能从结果推出可复用的设计含义，同时承认未检验的长期/组织因素。

- transition_to_next_cn：无，论文结束。

### most_transferable_moves_cn

1. 用“Borgs”这类隐喻命名抽象结果，增加记忆点。

2. 用解析模型把“知识多样性”转化为可计算的UHK/UAK。

3. 用预注册和功率分析保护确认性实验。

4. 用同一个AI处理的不同条件构成递进式benchmark：No AI → AI advice → AI advice + certainty → personalized AI advice。

5. 用个体实验数据进行Monte Carlo群体仿真，以小数据模拟大群体后果。

6. 把未支持的假设转化为图像级回归和机制解释，而不是直接跳过。

### resource_intensive_or_nonstandard_parts_cn

1. 需要运行大规模MTurk受试者招募（实验1 458人，实验3 492人，实验2 99人）。

2. 需要ImageNet图像集和GoogLeNet Inception v3的预测置信度作为AI建议来源。

3. 预注册和功率分析增加了研究设计成本。

4. 实验3需要两阶段设计：前50张图像学习个体收益/伤害，后50张检验；这依赖个体在同样任务集上多次决策。

5. 群体智慧仿真虽然计算量不大，但依赖来自多个实验条件的完整个体选择数据。

### what_not_to_copy_superficially_cn

1. 不能只在文字里声称“AI导致同质化/多样化损失”，必须用AI正确/错误交叉定义UHK并测量。

2. 不能只报告准确率提升，而忽略UHK下降；否则群体验证会缺少关键变量。

3. 不能把置信度提示包装成被支持的绩效提升，因为实验并未支持H2a。

4. 不能把Borgs隐喻说成实证结论；原文也只是有意夸张的讨论。

5. 不能宣称“个性化AI建议在所有环境下都有效”，因为只在图片分类和模拟群体中被支持。

6. 不能把Monte Carlo仿真等同于真实团队行为。

- single_best_description_of_the_routine_cn：先用形式化模型把一个被忽视的互补性损失变成可测量的UHK，再用预注册实验和图像级回归证明个体层面的“收益-代价”结构，最后用探索性异质性、第二轮干预实验以及Monte Carlo群体仿真证明该损失会外溢到群体智慧，并可用个性化建议同时保住个体绩效与人类多样性。

## 分析边界

全文为完整文本，无需OCR；但个别公式符号在文本转换中有瑕疵，例如式(5)的p_tc^AI分子可能缺少下标c，附录部分公式显示不完整；这些不影响主要论证结构识别。
