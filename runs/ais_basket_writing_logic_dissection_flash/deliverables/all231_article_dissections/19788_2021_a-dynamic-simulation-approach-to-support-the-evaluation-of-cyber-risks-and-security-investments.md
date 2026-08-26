# A dynamic simulation approach to support the evaluation of cyber risks and security investments in SMEs

- 作者：Stefano Armenia; Marco Angelini; Fabio Nonino; Giulia Palombi; Mario Francesco Schlitzer
- 年份 / 期刊：2021 / Decision Support Systems
- DOI：10.1016/j.dss.2021.113580
- 源文件：19788_2021_a-dynamic-simulation-approach-to-support-the-evaluation-of-cyber-risks-and-security-investments.md
- 论文主类型：build_evaluate_design_science
- 主导写作弧线：requirements_build_evaluate_design_principles
- 置信度：0.78

## 文章级论证概况

- 核心问题：如何为网络技能和资源有限的中小企业（SME）提供一种比静态框架更实用、更动态的网络风险评估与安全投资决策方法？

- 制品与设计：SMECRA工具：包含基于Cybersecurity Essential Controls的24题Snapshot Survey（输出覆盖率0-100%及四个子分数）和基于系统动力学的Powersim仿真模型（约50个方程，含声誉损害强化回路、攻击吸引力平衡回路、网络防御强化回路等；三个能力Prevention/Detection/Mitigation；支持Threat Level与Strategic Focus参数）。

- 客观结果：三个情景模拟显示：Alpha中等威胁下峰值损失16%、五年后4%；Alpha高威胁下峰值25%、五年后约11%；Beta高威胁下峰值约17%、五年后约11%，且Beta总成本（费用+损害）低于Alpha；配对t检验P=0.022；与每年€500常见支出相比，SMECRA导向的额外投资显著降低损害。

- 核心贡献：提出并演示了一个面向SME的动态、系统化的网络风险评估与投资决策支持方法/工具，弥补现有静态自评估框架无法捕捉组织变化和攻击动态的不足，并主张系统反馈视角优于线性/silo投资思维。

- 整篇论证链：论文从SME面临日益增长的网络威胁但缺乏相应技能和资源这一现实出发，指出现有网络风险管理框架和投资模型是静态或仅面向大企业，不能用跨类别动态关联支持SME决策；据此以NIST/意大利国家网络安全框架和系统动力学为知识基础，构建了由Snapshot Survey和SD仿真模型组成的SMECRA；通过设计三个受控情景（威胁环境与初始防御水平变化）进行模拟，展示工具能输出收入损失、防御能力和成本等动态结果；再通过Beta与Alpha的对照、配对t检验和与常见低投入做法比较，论证了初始防御和系统性投资的成本效益；最后将结果提升为系统性/动态框架优于线性silo方法的设计知识和管理启示。

## 类型与写作弧线判定

- 论文主类型判定：文章以需求（SME缺口）为导向，提出方法论和工具制品（SMECRA），通过三个模拟案例进行评价，并总结设计知识与决策树；没有使用真实组织的受控现场实验，也没有以基准数据集为主要证据的算法比较，因而最符合设计科学研究范式。

- 主导写作弧线判定：文章遵循需求识别（静态框架、SME缺口）→工具构建（Snapshot Survey + SD模型）→评价（三种情景模拟、统计检验、成本对比）→设计/管理含义（决策树、系统性方法结论）的写作弧线，属于要求—构建—评价—设计知识模式。

## 研究开展程序

- study_or_phase_count：6

- 研究阶段总序列：首先通过需求分析确定问题与目标，然后构建工具，接着设计受控案例，再运行模拟获取结果，随后用统计和成本对比验证，最后提炼战略含义和理论贡献；六个阶段依次累积，每一步都为下一步提供输入。

### studies_or_phases

#### 1. 需求分析与研究缺口

- order：1

- name_cn：需求分析与研究缺口

- question_cn：现有网络风险管理和投资方法的主要局限是什么？为什么需要为SME构建动态评估与投资决策工具？

- inputs_and_setting_cn：网络风险管理文献、NIST框架、意大利国家网络安全框架、System Dynamics用于信息安全投资的先前研究、Armenia et al. (2018) 的定性CLD模型，以及SME资源受限的背景。

- designed_or_compared_object_cn：研究目标与概念架构：将NIST类别投射到组织平面的双投影思路。

- baseline_control_or_counterfactual_cn：以静态框架和silo投资思维作为默认的现有方法。

##### objective_metrics

（空）

- analysis_method_cn：文献综述、缺口识别、系统思考概念推导。

- main_result_cn：确定两个核心缺口：现有方法缺乏动态/跨域整合；SME缺少实用易用的评估工具；确定以NIST/意大利框架和系统动力学为知识基础。

- argumentative_role_cn：赋予研究合法性和目标，说明为什么要做这个工具。

- remaining_uncertainty_cn：工具能否成功构建并产生有意义结果尚不确定。

- link_to_next_phase_cn：将需求转成具体设计与构建要求。

##### evidence_pointers

1. Section 2.1–2.3

2. Fig. 1

#### 2. SMECRA工具构建

- order：2

- name_cn：SMECRA工具构建

- question_cn：如何将NIST/意大利框架和定性CLD转化为可操作的量化评估与仿真工具？

- inputs_and_setting_cn：Cybersecurity Essential Controls、NIST五个功能、意大利框架的优先级/成熟度概念、Armenia et al. CLD、Powersim软件。

- designed_or_compared_object_cn：Snapshot Survey（24个问题、覆盖率与四个子分数）和SD仿真模型（>50条方程，七类资源分配，Prevention/Detection/Mitigation能力，RDRL/EDBL/CDRL反馈回路，Threat Level与Strategic Focus参数）。

- baseline_control_or_counterfactual_cn：没有正式baseline；以静态/线性投资逻辑为概念对照。

##### objective_metrics

1. Snapshot Survey覆盖率分数

2. 模型方程数量

3. 不同NIST类别到模型变量的映射

- analysis_method_cn：问卷设计、系统动力学建模、表格式变量映射。

- main_result_cn：完成了工具架构与变量映射；模型支持不同威胁环境和战略优先级的仿真。

- argumentative_role_cn：提供可复用的设计制品，说明工具如何回应静态框架不足。

- remaining_uncertainty_cn：模型参数设定、回路选择是否合理，以及输出是否可信尚未验证。

- link_to_next_phase_cn：需要案例和情景来演示工具使用。

##### evidence_pointers

1. Section 3.1–3.4

2. Fig. 2

3. Table 1

4. Table 2

5. Fig. 3–5

#### 3. 案例与情景设计

- order：3

- name_cn：案例与情景设计

- question_cn：如何设计受控案例来展示SMECRA在不同威胁环境和不同初始防御状态下的行为？

- inputs_and_setting_cn：两个虚构SME Alpha和Beta；三种情景（Alpha中等威胁、Alpha高威胁、Beta高威胁）；统一参数：5年仿真、1周时间步、SME年收入€1,300,000。

- designed_or_compared_object_cn：情景自变量：Threat Level（2或3）和Snapshot Survey初始得分（Alpha约38%，Beta约67.25%）。

- baseline_control_or_counterfactual_cn：Beta作为Alpha在高威胁环境下的防御准备对照；常见低支出（€500/年）作为外部成本基准。

##### objective_metrics

1. 峰值损失百分比

2. 第3年损失

3. 第5年损失

4. 到达平台时间

5. 费用+损害总额

- analysis_method_cn：对照案例设计、模拟实验设计、控制混杂变量。

- main_result_cn：三组模拟输入确定，且Beta与Alpha的其他组织特征保持相同，以排除混淆因素。

- argumentative_role_cn：把工具应用变成可解释的对比证据。

- remaining_uncertainty_cn：结果差异是否统计显著和是否有经济意义尚待分析。

- link_to_next_phase_cn：进入实际仿真运行与结果分析。

##### evidence_pointers

1. Section 4 开头

2. Table 3

3. Table 4

#### 4. 模拟运行与动态结果

- order：4

- name_cn：模拟运行与动态结果

- question_cn：SMECRA在三个情景下产生哪些动态结果，尤其是不同威胁和初始防御带来的差异？

- inputs_and_setting_cn：Alpha/Beta的Snapshot Survey答案、Threat Level设置、默认理性资源分配、统一仿真参数。

- designed_or_compared_object_cn：比较三情景的收入随时间、损失百分比、防御能力随时间等输出。

- baseline_control_or_counterfactual_cn：情景1 vs 情景2（同一企业不同威胁）；情景2 vs 情景3（不同初始防御、相同威胁）。

##### objective_metrics

1. 收入损失百分比

2. 防御能力水平

3. 峰值损失

4. 平台时间

- analysis_method_cn：系统动力学仿真运行、图表演示。

- main_result_cn：Alpha中等威胁峰值16%且最终降至4%；Alpha高威胁峰值25%且五年后仍约11-12%；Beta高威胁峰值约17%且损失下降更快。防御能力图显示初始准备高使反馈回路强度受限。

- argumentative_role_cn：提供核心演示证据，展示工具能刻画动态行为和风险差异。

- remaining_uncertainty_cn：Beta优势是否统计显著；相比常见低投入做法是否更经济。

- link_to_next_phase_cn：通过统计检验和成本对比进一步确证。

##### evidence_pointers

1. Section 4.1–4.3

2. Fig. 7

3. Fig. 8

4. Table 5

#### 5. 统计验证与成本效益分析

- order：5

- name_cn：统计验证与成本效益分析

- question_cn：Beta相对Alpha的优势是否统计显著？SMECRA相比常见低投入做法是否具有成本效益？

- inputs_and_setting_cn：Scenario 2和Scenario 3每年的费用+损害数据；常见SME年网络安全支出低于€500的基准。

- designed_or_compared_object_cn：Alpha策略、Beta策略、基本approach（€500/年）三种成本结构。

- baseline_control_or_counterfactual_cn：基本approach作为最低投入对照；Beta策略作为高准备对照。

##### objective_metrics

1. 配对t检验P值

2. 总费用+损害

3. 网络支出与损害之比

- analysis_method_cn：配对t检验、表格成本对比、描述性解释。

- main_result_cn：配对t检验P=0.022，Beta优势在95%置信区间下显著；论文对比显示额外投入显著降低损害，Beta在成本与损害两个维度均优于Alpha。

- argumentative_role_cn：将模拟演示提升为具有统计和经济意义的证据。

- remaining_uncertainty_cn：t检验样本只有5个年度点；Table 6与Table 7存在数字不一致；未做敏感性分析。

- link_to_next_phase_cn：为战略和管理含义提供依据。

##### evidence_pointers

1. Section 5 前四段

2. Table 6

3. Table 7

4. Fig. 9

#### 6. 战略含义与理论贡献

- order：6

- name_cn：战略含义与理论贡献

- question_cn：这些结果对SME网络安全投资决策有什么关系？对研究有何理论意义？

- inputs_and_setting_cn：三情景结果、Beta vs Alpha对比、成本数据；决策树。

- designed_or_compared_object_cn：投资分配建议（Regulations, Accounts, Inventory, Protection Software, Network Protection, Damage Mitigation, HR Skill, Backups）和决策树。

- baseline_control_or_counterfactual_cn：静态/silo投资方法作为反面参照。

##### objective_metrics

（空）

- analysis_method_cn：管理推断、决策树构建、理论定位。

- main_result_cn：提出投资应关注七类变量；决策树指导先评估后模拟；主张系统性/动态框架优于线性方法，并扩展到银行/保险公司和未来领域。

- argumentative_role_cn：把结果上升为可复用设计知识和理论贡献，回应引言缺口。

- remaining_uncertainty_cn：推广到真实SME绩效和长期效果未经验证。

- link_to_next_phase_cn：收束全文，给出未来研究方向。

##### evidence_pointers

1. Section 5 后半段

2. Section 6

3. Fig. 10

## 各部分修辞架构

### abstract_moves

1. 背景：网络威胁增长，需要评估风险和规划投资

2. 指出NIST框架等自评估方法为静态，不能捕捉组织变化和攻击动态

3. 指出SME缺乏技能和资源

4. 提出方法：提出SMECRA（系统动力学+Snapshot Survey）

5. 说明用途：评估风险与投资影响、动态复杂性

6. 证据：三个案例研究

7. 目标受众：SME和保险公司

### introduction_moves

1. 数字化使SME也成为目标

2. 网络攻击影响关键基础设施；网络安全是多学科的

3. 需要合适的工具评估风险和投资

4. 现有方法缺乏跨域整合、动态和不确定性

5. 现有研究主要针对大企业和关键基础设施；SME受限

6. 提出SMECRA及NIST/意大利框架为基础

7. 路线图预告

### theory_and_knowledge_moves

1. 回顾网络安全风险管理的两组文献

2. 介绍NIST框架核心、层级、轮廓

3. 介绍意大利国家网络安全框架及其扩展概念（优先级、成熟度、情境化）

4. 引用Nazareth和Choi、Pate-Cornell等动态需求

5. 提出系统动力学与因果回路图方法

6. 基于Armenia et al. CLD模型，说明NIST类别在组织平面上的系统关联

### artifact_design_moves

1. 快照调查设计：基于Essential Controls，24个问题，覆盖率分数

2. 将调查答案映射到SD模型变量（Table 1）

3. 模型结构：stocks and flows、反馈回路（RDRL, EDBL, CDRL）

4. 能力变量：Prevention/Detection/Mitigation，带硬上限

5. 用户可控输入：Threat Level、Strategic Focus

### evaluation_moves

1. 三个情景：Alpha medium、Alpha high、Beta high

2. 控制Beta与Alpha除防御准备外完全相同，以提高信噪比

3. 关键结果：收入损失、防御能力、峰值损失、平台时间

4. 配对t检验验证Beta优势

5. 与常见低投入做法（€500/年）对比成本效益

### discussion_and_contribution_moves

1. 强调Beta在最初两年的抗毁优势

2. 竞争情景：Beta获得Alpha市场份额

3. 投入远低于损害；预防比事后补救有效

4. 决策树指导投资分配

5. 对比静态/silo方法，主张系统思维

6. 结论：SMECRA用于SME自身和第三方（银行保险公司）

7. 研究贡献：走向系统化和动态框架

## 理论/知识到设计的翻译

### 知识/理论基础

1. NIST Cybersecurity Framework

2. Italian National Cybersecurity Framework

3. Cybersecurity Essential Controls

4. Systems Thinking / System Dynamics

5. Armenia et al. (2018) qualitative CLD model

6. System Dynamics principles (structure influences behavior; simpler is better)

- 理论—设计耦合：partial

- 耦合判定理由：NIST/意大利框架和系统动力学提供了概念框架和建模方法，直接影响了调查题目、变量体系和模型结构；但大量具体实现选择（方程形式、反馈回路取舍、能力硬上限、仿真参数、案例设置）来自研究者判断和工程启发，评价未直接检验这些理论命题本身，而是展示工具在设想情景中的行为。

- 理论到设计翻译链：现实需求与缺口（SME动态风险与投资决策）→ NIST/意大利框架提供评估类别，Essential Controls提供SME化调查条目 → Snapshot Survey采集as-is状态 → 调查答案映射为SD模型变量和初始参数 → SD模型用因果回路和存流量结构表达类别间动态反馈 → Threat Level与Strategic Focus作为用户控制变量 → 三组情景模拟输出风险与成本动态 → 对比分析支持预防优先、系统分配优于silo的设计知识。

### mapping_table

#### 1. 1

- theory_or_knowledge_claim_cn：NIST框架的功能和子类别可以用于评估SME的网络安全防御状态。

- mechanism_cn：评估类别覆盖程度可量化企业防御弱点与总体态势。

- design_requirement_cn：需要能逐项采集SME对NIST相关控制的执行状态的轻量工具。

- artifact_choice_cn：基于Cybersecurity Essential Controls开发24题Snapshot Survey，输出总体覆盖率与四个子分数。

- evaluated_contrast_cn：Alpha和Beta在Snapshot Survey上的得分差异（38%对67.25%）。

- objective_result_cn：Beta防御准备高，模拟中峰值损失和总成本更低。

##### evidence_pointers

1. Section 3.3

2. Table 1

3. Table 4

4. Section 4.3

#### 2. 2

- theory_or_knowledge_claim_cn：意大利国家网络安全框架通过优先级、成熟度和情境化概念，使NIST框架适用于中小企业。

- mechanism_cn：不同优先级/成熟度影响防御措施的实施程度、成本与风险暴露。

- design_requirement_cn：工具应允许决策者按业务重点调整投资比例。

- artifact_choice_cn：在SD模型中设置Strategic Focus参数，允许增加/减少七个安全类别的支出。

- evaluated_contrast_cn：论文未系统比较Strategic Focus的不同设置，仅将其作为用户功能展示。

- objective_result_cn：工具能模拟不同战略重点，但该功能未被作为结果变量检验。

##### evidence_pointers

1. Section 3.4

2. Fig. 5

#### 3. 3

- theory_or_knowledge_claim_cn：系统动力学中，系统结构（反馈回路、存流量、时滞）决定系统行为。

- mechanism_cn：成功攻击→损害→脆弱性感知→吸引力→更多攻击；投资→缓解能力→阻止攻击→财务结果→更多投资。

- design_requirement_cn：模型需要包含跨NIST类别和组织变量的反馈回路，并支持动态仿真。

- artifact_choice_cn：用Powersim实现SD模型，含50多个方程、RDRL/EDBL/CDRL反馈回路、Poisson攻击率、三种能力及硬上限。

- evaluated_contrast_cn：同一企业不同威胁环境、不同初始防御企业的行为差异。

- objective_result_cn：高威胁环境下恢复慢、初始防御高则成本低。

##### evidence_pointers

1. Section 3.4

2. Fig. 3–8

3. Table 5

#### 4. 4

- theory_or_knowledge_claim_cn：系统动力学原则简单更好和结构影响行为意味着不需要包含全部理论反馈回路。

- mechanism_cn：主要反馈回路足以捕捉核心动态，过度复杂会损害可理解性。

- design_requirement_cn：模型应聚焦主要组织变量与NIST类别之间的关键关系。

- artifact_choice_cn：SMECRA只纳入主要相关回路，将其他子系统推迟到未来。

- evaluated_contrast_cn：没有直接对比不同复杂度模型，而是通过案例行为展示充分性。

- objective_result_cn：模型输出符合理论预期的动态行为，说明主要回路足够。

##### evidence_pointers

1. Section 2.3 后半段

2. Section 3.4 开头

## 评价逻辑

### evaluation_modes

1. 案例研究/scenario simulation

2. 对照案例设计（Alpha vs Beta）

3. 统计显著性检验（paired t-test）

4. 成本效益对比（standard approach）

5. 模型功能演示（不同威胁环境）

- why_these_evaluations_cn：由于是新的设计科学制品，需要展示工具在实际情境中的可用性、输出合理性及决策支持价值；通过受控情景对比将企业防御准备和威胁环境作为自变量，以揭示动态行为和成本差异；再用统计检验和与常见做法对比来支撑经济有效性。

- benchmark_and_contrast_chain_cn：第一步用Alpha中等威胁作为基线案例；第二步将威胁提高，形成环境冲击；第三步引入Beta作为防御准备更高的对照，在相同高威胁环境中比较；最后使用年支出€500的行业常见做法作为外部基准，衡量SMECRA导向策略的增量收益。

### claim_evidence_ledger

#### 1. SMECRA能评估SME当前网络风险并随时间动态显示风险

- claim_cn：SMECRA能评估SME当前网络风险并随时间动态显示风险

- evidence_cn：三组模拟的收入和防御能力图表（Fig.7/8, Table 5）

- supported_degree_cn：在模拟框架内支持；未与真实观测数据比对

#### 2. 初始防御准备越高，高威胁环境下的峰值损失和总成本越低

- claim_cn：初始防御准备越高，高威胁环境下的峰值损失和总成本越低

- evidence_cn：Scenario 2 vs 3结果、Table 6/7、配对t检验P=0.022

- supported_degree_cn：在模型生成数据上支持，但统计样本量极小

#### 3. 投资网络安全比不投资/低投入更具成本效益

- claim_cn：投资网络安全比不投资/低投入更具成本效益

- evidence_cn：Table 7中额外支出对应的损害减少

- supported_degree_cn：部分支持；论文表格数字存在不一致，削弱清晰性

#### 4. NIST类别之间通过组织关系系统关联，投资存在溢出效应

- claim_cn：NIST类别之间通过组织关系系统关联，投资存在溢出效应

- evidence_cn：CLD与SD模型中的反馈回路设计以及模拟行为

- supported_degree_cn：通过设计论证而非实证检验

- internal_validity_strategy_cn：通过使Alpha和Beta除网络准备外所有组织特征相同、统一仿真参数、使用相同的Snapshot Survey工具和模型，消除混杂因素；使用对照情景（威胁水平变化、防御水平变化）分离变量；最后用配对t检验确认差异不是偶然。

- external_validity_strategy_cn：采用意大利SME平均收入作为仿真参数；基于被广泛认可的NIST和意大利国家框架及Essential Controls；工具设计开源式呈现，便于在其他组织或国家适配；在结论中讨论对银行、保险公司和其他领域的可扩展性。

- what_is_not_actually_tested_cn：真实SME中的现场应用与用户接受度未测试；模型结果未与实际网络攻击损失数据校准；Strategic Focus参数的不同配置未做系统对比；Threat Level值的标定具有主观性；未做参数敏感性分析；统计检验只有5个年度合计点，且数据来自同一确定性模型，并非多次独立仿真。

## 贡献闭环

- technical_claim_cn：提出了一种基于系统动力学的SME网络风险评估与投资决策支持工具，能够动态模拟不同威胁和战略下的风险与费用。

- artifact_claim_cn：SMECRA的两个模块（Snapshot Survey与SD模型）共同实现了从现状评估到投资效果模拟的完整流程，其设计由NIST框架和Essential Controls转化而来。

- mechanism_claim_cn：通过反馈回路（声誉损害强化回路、资源获取平衡回路、网络防御强化回路）解释为什么初始防御薄弱会使企业在高威胁环境中持续受损、为什么预防性投资能降低长期成本。

- boundary_claim_cn：研究针对意大利SME情境，使用NIST/意大利框架和Essential Controls；不同国家、行业或大型企业可能需要定制；模型包含主要反馈回路而非全部。

- reusable_design_knowledge_cn：可复用经验：将NIST类别映射到组织变量、用Snapshot Survey采集现状、用SD模型表达类别间动态关联、允许Threat Level与Strategic Focus作为用户控制变量；决策树提供投资优先级指导。

- theoretical_contribution_cn：将系统和动态框架思想引入网络安全风险评估，论证静态框架中类别间的组织关联会导致投资溢出效应；扩展了用系统动力学研究信息安全投资的文献（如Nazareth和Choi）到SME情境。

- how_discussion_closes_intro_gap_cn：讨论部分用Beta vs Alpha的对比、t检验和标准approach对比，证明SMECRA能弥补静态框架的不足（动态、跨类别、可操作），并把结果提升为预防与系统分配优于事后响应的管理结论。

- overclaim_or_unsupported_leaps_cn：（1）Table 6与Table 7的总成本数字不一致（Table 6中Alpha五年总费用+损害为€1,728,200，Table 7中Alpha总费用+损害为€428,200），但论文未解释差异，可能影响成本效益论证；（2）配对t检验基于5个年度合计，样本量极小且数据来自同一模型，统计有效性有限；（3）将模拟情景结果表述为对真实企业的undeniable advantage略显过度；（4）从两个虚构案例推广到系统性方法优于线性方法缺乏实证基础。

## 句级写作动作图谱

### 1. P1 S1

- order：1

- section：Introduction

- locator：P1 S1

- move_code：CONTEXT

- paraphrase_cn：数字化使所有组织依赖信息系统，SME也成为潜在网络犯罪目标。

- rhetorical_function_cn：建立现实背景。

- depends_on_cn：无

- sets_up_cn：引出SME面临风险

- evidence_pointer：Introduction P1

### 2. P1 S2–S3

- order：2

- section：Introduction

- locator：P1 S2–S3

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：网络攻击可影响关键基础设施，网络安全涉及人为因素等跨学科问题。

- rhetorical_function_cn：说明问题重要性和多学科性。

- depends_on_cn：首句背景

- sets_up_cn：论证需要综合性工具

- evidence_pointer：Introduction P1

### 3. P2 S1

- order：3

- section：Introduction

- locator：P2 S1

- move_code：PRACTICAL_STAKES

- paraphrase_cn：信息不完整或企业规模有限时，仍需制定安全政策。

- rhetorical_function_cn：强调现实决策困境。

- depends_on_cn：前两句背景

- sets_up_cn：引出工具需求

- evidence_pointer：Introduction P2

### 4. P2 S2

- order：4

- section：Introduction

- locator：P2 S2

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：评估风险和规划投资的需要已被广泛认识，已有不少风险管理和预算分配研究。

- rhetorical_function_cn：展示学术关注。

- depends_on_cn：现实背景

- sets_up_cn：指出不足

- evidence_pointer：Introduction P2

### 5. P2 S3

- order：5

- section：Introduction

- locator：P2 S3

- move_code：LIMITATION

- paraphrase_cn：这些方法缺乏跨域整合和复杂性，且是静态的，不考虑因果依赖、攻击动态和不确定性。

- rhetorical_function_cn：明确技术和方法缺口。

- depends_on_cn：已有研究

- sets_up_cn：提出动态仿真方向

- evidence_pointer：Introduction P2

### 6. P2 S4

- order：6

- section：Introduction

- locator：P2 S4

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：Nazareth和Choi指出理解威胁动态是资源管理的前提，仿真适合处理动态关系。

- rhetorical_function_cn：用权威支持动态仿真。

- depends_on_cn：前述局限

- sets_up_cn：为系统动力学选择铺路

- evidence_pointer：Introduction P2

### 7. P3 S1

- order：7

- section：Introduction

- locator：P3 S1

- move_code：LIMITATION

- paraphrase_cn：另一局限是研究对象主要是大企业和关键基础设施。

- rhetorical_function_cn：明确情境缺口。

- depends_on_cn：已有文献范围

- sets_up_cn：SME焦点

- evidence_pointer：Introduction P3

### 8. P3 S2

- order：8

- section：Introduction

- locator：P3 S2

- move_code：PHENOMENON

- paraphrase_cn：SME遭受攻击增加，但因资源有限和技能短缺常无有效防御。

- rhetorical_function_cn：描述SME脆弱性的经验现象。

- depends_on_cn：情境缺口

- sets_up_cn：提出SME工具

- evidence_pointer：Introduction P3

### 9. P3 S3–S5

- order：9

- section：Introduction

- locator：P3 S3–S5

- move_code：RQ_OR_OBJECTIVE

- paraphrase_cn：因此提出SMECRA：基于系统动力学，以NIST框架为基线，先用Snapshot Survey采集初始风险，再模拟投资效果。

- rhetorical_function_cn：陈述研究目标和制品。

- depends_on_cn：前述所有缺口和需求

- sets_up_cn：后续方法论和案例

- evidence_pointer：Introduction P3

### 10. P3 S6

- order：10

- section：Introduction

- locator：P3 S6

- move_code：DESIGN_FEATURE

- paraphrase_cn：SMECRA允许设置不同战略优先级，比较不同投资选择的未来结果。

- rhetorical_function_cn：强调工具用户功能。

- depends_on_cn：目标陈述

- sets_up_cn：模型特性描述

- evidence_pointer：Introduction P3

### 11. P4

- order：11

- section：Introduction

- locator：P4

- move_code：STUDY_OVERVIEW

- paraphrase_cn：介绍文章结构：文献、方法、案例结果、讨论、结论。

- rhetorical_function_cn：预告路线。

- depends_on_cn：目标陈述

- sets_up_cn：后续章节顺序

- evidence_pointer：Introduction P4

### 12. P1

- order：12

- section：Section 2

- locator：P1

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：定义网络安全，并指出外部威胁和内部威胁（如恶意内部人员）都是重要主题。

- rhetorical_function_cn：建立网络安全知识基础。

- depends_on_cn：引言背景

- sets_up_cn：风险管理文献综述

- evidence_pointer：Section 2 P1

### 13. P1

- order：13

- section：Section 2.1

- locator：P1

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：文献中网络风险管理方法分为理论框架类和预算分配类。

- rhetorical_function_cn：给出文献分类框架。

- depends_on_cn：综述开始

- sets_up_cn：逐类讨论

- evidence_pointer：Section 2.1 P1

### 14. P3

- order：14

- section：Section 2.1

- locator：P3

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：NIST框架提供指南、最佳实践和标准，是多个国家框架的基础。

- rhetorical_function_cn：强调NIST的重要性。

- depends_on_cn：分类

- sets_up_cn：选择NIST作为基础

- evidence_pointer：Section 2.1 P3

### 15. P4

- order：15

- section：Section 2.1

- locator：P4

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：Nazareth和Choi用系统动力学模型评估不同安全管理策略，发现检测工具投资回报高于威慑工具。

- rhetorical_function_cn：显示SD在信息安全投资中的应用先例。

- depends_on_cn：预算分配类文献

- sets_up_cn：支持本文使用SD

- evidence_pointer：Section 2.1 P4

### 16. P1–P3

- order：16

- section：Section 2.2

- locator：P1–P3

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：NIST框架由核心、层级和轮廓组成，核心有五个连续功能等。

- rhetorical_function_cn：介绍框架细节。

- depends_on_cn：NIST重要性

- sets_up_cn：意大利框架扩展

- evidence_pointer：Section 2.2 P1–P3

### 17. P4

- order：17

- section：Section 2.2

- locator：P4

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：意大利国家网络安全框架扩展NIST，适用于公共机构和SME，增加优先级、成熟度和情境化原型。

- rhetorical_function_cn：介绍本研究采用的本土化框架。

- depends_on_cn：NIST介绍

- sets_up_cn：模型变量来源

- evidence_pointer：Section 2.2 P4

### 18. P1

- order：18

- section：Section 2.3

- locator：P1

- move_code：GAP

- paraphrase_cn：上述模型虽有最佳实践，但缺乏跨域整合、不确定性与攻击动态，且应扩展至SME。

- rhetorical_function_cn：汇总研究缺口。

- depends_on_cn：文献综述

- sets_up_cn：明确本研究目标

- evidence_pointer：Section 2.3 P1

### 19. P2

- order：19

- section：Section 2.3

- locator：P2

- move_code：GAP

- paraphrase_cn：虽然有SD支持投资决策的系统，但没有实用、动态、易用且针对SME的风险评估模型。

- rhetorical_function_cn：形成最具体缺口。

- depends_on_cn：前述文献

- sets_up_cn：提出SMECRA

- evidence_pointer：Section 2.3 P2

### 20. P3

- order：20

- section：Section 2.3

- locator：P3

- move_code：RQ_OR_OBJECTIVE

- paraphrase_cn：研究目标是提出SMECRA方法论和工具，由Snapshot Survey和SD模型两模块组成。

- rhetorical_function_cn：陈述目标。

- depends_on_cn：缺口

- sets_up_cn：方法论章节

- evidence_pointer：Section 2.3 P3

### 21. P4

- order：21

- section：Section 2.3

- locator：P4

- move_code：PRACTICAL_STAKES

- paraphrase_cn：工具旨在帮助决策者理解投资HR、生产系统、信息/安全系统等如何提高网络韧性。

- rhetorical_function_cn：强调实践用途。

- depends_on_cn：目标

- sets_up_cn：投资分类相关设计

- evidence_pointer：Section 2.3 P4

### 22. P5

- order：22

- section：Section 2.3

- locator：P5

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：系统思维和SD在网络安全领域的价值已得到验证，还可用于网络战等。

- rhetorical_function_cn：为方法论提供知识支撑。

- depends_on_cn：前面文献

- sets_up_cn：方法选择

- evidence_pointer：Section 2.3 P5

### 23. P6

- order：23

- section：Section 2.3

- locator：P6

- move_code：THEORY_INTRO

- paraphrase_cn：SMECRA源自Armenia等人的定性CLD模型，该模型将意大利网络安全框架类别与SME组织结构关联。

- rhetorical_function_cn：说明模型理论来源。

- depends_on_cn：方法论需求

- sets_up_cn：设计原理

- evidence_pointer：Section 2.3 P6

### 24. P7

- order：24

- section：Section 2.3

- locator：P7

- move_code：THEORY_PROPOSITION

- paraphrase_cn：与组织方面系统关联意味着NIST类别之间通过组织关系也系统互连。

- rhetorical_function_cn：提出系统互连命题。

- depends_on_cn：CLD模型

- sets_up_cn：模型因果关系结构

- evidence_pointer：Section 2.3 P7

### 25. P8

- order：25

- section：Section 2.3

- locator：P8

- move_code：LIMITATION_AND_FUTURE

- paraphrase_cn：本文在先前假设基础上建立量化工具，只纳入主要反馈回路，其他子系统留待未来；遵循简单更好原则。

- rhetorical_function_cn：界定模型范围并预告未来工作。

- depends_on_cn：系统互连命题

- sets_up_cn：模型范围界定

- evidence_pointer：Section 2.3 P8

### 26. P1

- order：26

- section：Section 3.1

- locator：P1

- move_code：REQUIREMENT

- paraphrase_cn：为评估SME现状并支持投资决策，构建先分析后模拟的工具。

- rhetorical_function_cn：将目标转化为设计需求。

- depends_on_cn：研究目标

- sets_up_cn：工具架构

- evidence_pointer：Section 3.1 P1

### 27. P2

- order：27

- section：Section 3.1

- locator：P2

- move_code：REQUIREMENT

- paraphrase_cn：模型初始化参数来自初始as-is风险档案评估，将定性评估转化为核心参数。

- rhetorical_function_cn：说明数据输入机制。

- depends_on_cn：工具架构

- sets_up_cn：Snapshot Survey

- evidence_pointer：Section 3.1 P2

### 28. P3

- order：28

- section：Section 3.1

- locator：P3

- move_code：ROBUSTNESS_OR_BOUNDARY_TEST

- paraphrase_cn：多个初始化参数不会使模型失效，因为系统结构影响系统行为。

- rhetorical_function_cn：回应参数不确定性。

- depends_on_cn：模型架构

- sets_up_cn：模型可信性论证

- evidence_pointer：Section 3.1 P3

### 29. P1

- order：29

- section：Section 3.2

- locator：P1

- move_code：THEORY_INTRO

- paraphrase_cn：SD是迭代过程：定义动态假设、开发模型、检验政策。

- rhetorical_function_cn：介绍方法论框架。

- depends_on_cn：方法论选择

- sets_up_cn：建模步骤

- evidence_pointer：Section 3.2 P1

### 30. P2

- order：30

- section：Section 3.2

- locator：P2

- move_code：THEORY_INTRO

- paraphrase_cn：SD能处理非线性、信息反馈、时滞和动态复杂性。

- rhetorical_function_cn：论证为什么SD适合网络安全。

- depends_on_cn：SD定义

- sets_up_cn：设计特征

- evidence_pointer：Section 3.2 P2

### 31. P3–P4

- order：31

- section：Section 3.2

- locator：P3–P4

- move_code：THEORY_INTRO

- paraphrase_cn：CLD用于绘制因果关系和反馈回路，库存流量模型用来显示系统行为随时间变化。

- rhetorical_function_cn：介绍核心概念。

- depends_on_cn：SD理论

- sets_up_cn：模型描述

- evidence_pointer：Section 3.2 P3–P4

### 32. P1

- order：32

- section：Section 3.3

- locator：P1

- move_code：REQUIREMENT

- paraphrase_cn：为了建立基于参数的自我评估，需要数据采集工具；基于Essential Controls开发了24个问题的Snapshot Survey。

- rhetorical_function_cn：将需求转为调查工具。

- depends_on_cn：初始化需求

- sets_up_cn：调查内容

- evidence_pointer：Section 3.3 P1

### 33. P2

- order：33

- section：Section 3.3

- locator：P2

- move_code：DESIGN_FEATURE

- paraphrase_cn：调查结果是0-100%覆盖率分数和四个子分数，用于指出薄弱点。

- rhetorical_function_cn：描述调查输出。

- depends_on_cn：调查工具

- sets_up_cn：模型输入

- evidence_pointer：Section 3.3 P2

### 34. P3

- order：34

- section：Section 3.3

- locator：P3

- move_code：DESIGN_FEATURE

- paraphrase_cn：覆盖率分数衡量每个控制覆盖程度，低于70%或50%表示有重要缺失或不合规。

- rhetorical_function_cn：定义分数解读方法。

- depends_on_cn：调查输出

- sets_up_cn：案例解释

- evidence_pointer：Section 3.3 P3

### 35. P4

- order：35

- section：Section 3.3

- locator：P4

- move_code：DESIGN_FEATURE

- paraphrase_cn：加权系统确保一个类别总分为100，避免偏向。

- rhetorical_function_cn：说明调查权重设计。

- depends_on_cn：调查输出

- sets_up_cn：分数可靠性

- evidence_pointer：Section 3.3 P4

### 36. P5

- order：36

- section：Section 3.3

- locator：P5

- move_code：TRANSITION

- paraphrase_cn：调查数据映射到SD模型的变量和参数。

- rhetorical_function_cn：连接调查与模型。

- depends_on_cn：调查输出和模型变量

- sets_up_cn：模型描述

- evidence_pointer：Section 3.3 P5

### 37. P1

- order：37

- section：Section 3.4

- locator：P1

- move_code：DESIGN_FEATURE

- paraphrase_cn：SMECRA模型用Powersim开发，以Snapshot Survey作为初始状态输入。

- rhetorical_function_cn：说明工具实现。

- depends_on_cn：调查映射

- sets_up_cn：方程和环路

- evidence_pointer：Section 3.4 P1

### 38. P2

- order：38

- section：Section 3.4

- locator：P2

- move_code：DESIGN_FEATURE

- paraphrase_cn：模型包含50多个方程，表2给出备份相关方程示例。

- rhetorical_function_cn：展示模型量化程度。

- depends_on_cn：模型架构

- sets_up_cn：方程细节

- evidence_pointer：Section 3.4 P2

### 39. P3

- order：39

- section：Section 3.4

- locator：P3

- move_code：MECHANISM

- paraphrase_cn：没有防御的企业会陷入声誉损害强化回路：成功攻击→损害→脆弱性感知→吸引力→更多攻击。

- rhetorical_function_cn：解释负面动态。

- depends_on_cn：CLD模型

- sets_up_cn：模型行为解释

- evidence_pointer：Section 3.4 P3

### 40. P4

- order：40

- section：Section 3.4

- locator：P4

- move_code：MECHANISM

- paraphrase_cn：损害过大时企业吸引力下降从而减少外部攻击，但同时也意味着经营已严重受损。

- rhetorical_function_cn：解释平衡回路或极端情况。

- depends_on_cn：负面动态

- sets_up_cn：高威胁情景结果

- evidence_pointer：Section 3.4 P4

### 41. P5

- order：41

- section：Section 3.4

- locator：P5

- move_code：MECHANISM

- paraphrase_cn：网络防御强化回路：投资→缓解能力→阻止攻击→减少损害→提高财务结果→更多投资。

- rhetorical_function_cn：解释积极反馈。

- depends_on_cn：负面回路解释

- sets_up_cn：投资效果

- evidence_pointer：Section 3.4 P5

### 42. P6–P7

- order：42

- section：Section 3.4

- locator：P6–P7

- move_code：MECHANISM

- paraphrase_cn：攻击率由Poisson分布决定，受威胁水平和吸引力影响；攻击经过检测和缓解两个关口，未阻止的攻击增加损害。

- rhetorical_function_cn：描述攻击流程机制。

- depends_on_cn：SD结构

- sets_up_cn：能力和结果变量

- evidence_pointer：Section 3.4 P6–P7

### 43. P8

- order：43

- section：Section 3.4

- locator：P8

- move_code：MECHANISM

- paraphrase_cn：损害增加既减少财务结果又提高脆弱性感知，管理层面临投资压力但资源减少。

- rhetorical_function_cn：解释资源约束的矛盾。

- depends_on_cn：攻击流程

- sets_up_cn：投资决策动态

- evidence_pointer：Section 3.4 P8

### 44. P9

- order：44

- section：Section 3.4

- locator：P9

- move_code：DESIGN_FEATURE

- paraphrase_cn：资源库存通过七个流出分配到Regulations、Accounts、Inventory等安全变量，再转化为能力。

- rhetorical_function_cn：描述资源分配结构。

- depends_on_cn：SD结构

- sets_up_cn：Strategic Focus

- evidence_pointer：Section 3.4 P9

### 45. P10

- order：45

- section：Section 3.4

- locator：P10

- move_code：DESIGN_FEATURE

- paraphrase_cn：用户可控制Threat Level（低/中/高）和Strategic Focus，模拟不同环境和不同投资策略。

- rhetorical_function_cn：说明用户可调参数。

- depends_on_cn：模型结构

- sets_up_cn：案例情景

- evidence_pointer：Section 3.4 P10

### 46. P11

- order：46

- section：Section 3.4

- locator：P11

- move_code：BOUNDARY_CONDITION

- paraphrase_cn：三种能力从0到1，但设硬上限，因为没有完美防御。

- rhetorical_function_cn：承认模型边界。

- depends_on_cn：能力结构

- sets_up_cn：结果解读

- evidence_pointer：Section 3.4 P11

### 47. P1

- order：47

- section：Section 4

- locator：P1

- move_code：STUDY_OVERVIEW

- paraphrase_cn：为展示工具在现实情景中的行为，选择Alpha和Beta两个SME，设计了三个情景。

- rhetorical_function_cn：引入评价部分。

- depends_on_cn：工具描述

- sets_up_cn：案例细节

- evidence_pointer：Section 4 P1

### 48. P2

- order：48

- section：Section 4

- locator：P2

- move_code：BENCHMARK_OR_CONTRAST

- paraphrase_cn：统一5年、周步长和收入；Beta与Alpha除防御准备外完全相同，以提高信噪比。

- rhetorical_function_cn：建立对照逻辑。

- depends_on_cn：案例选择

- sets_up_cn：结果可比性

- evidence_pointer：Section 4 P2

### 49. P3

- order：49

- section：Section 4

- locator：P3

- move_code：BENCHMARK_OR_CONTRAST

- paraphrase_cn：情景展示不同威胁环境对无防御企业的影响、投资如何通过避免损失自我买单、防御优势可用来抢占市场份额。

- rhetorical_function_cn：明确情景对比的目的。

- depends_on_cn：对照逻辑

- sets_up_cn：结果讨论

- evidence_pointer：Section 4 P3

### 50. P1

- order：50

- section：Section 4.1

- locator：P1

- move_code：CONTEXT

- paraphrase_cn：Alpha是典型不关注网络安全的SME，总体Snapshot Survey得分38%。

- rhetorical_function_cn：描述案例基线。

- depends_on_cn：情景设计

- sets_up_cn：情景1结果

- evidence_pointer：Section 4.1 P1

### 51. P2

- order：51

- section：Section 4.1

- locator：P2

- move_code：RESULT

- paraphrase_cn：模拟开始后Alpha很快成为目标，6个月损失超16%收入。

- rhetorical_function_cn：报告情景1早期结果。

- depends_on_cn：案例基线

- sets_up_cn：投资干预效果

- evidence_pointer：Section 4.1 P2

### 52. P3

- order：52

- section：Section 4.1

- locator：P3

- move_code：RESULT

- paraphrase_cn：第二学期后情况改善，第四年损失明显减少；峰值投资约4%，稳定后低于2%。

- rhetorical_function_cn：报告情景1完整动态。

- depends_on_cn：情景1运行

- sets_up_cn：高威胁对比

- evidence_pointer：Section 4.1 P3

### 53. P1

- order：53

- section：Section 4.2

- locator：P1

- move_code：RESULT

- paraphrase_cn：同一Alpha在高威胁环境下几个月损失近25%，五年后仍损失约12%，可能倒闭。

- rhetorical_function_cn：报告威胁升级后果。

- depends_on_cn：情景1结果

- sets_up_cn：高威胁对比

- evidence_pointer：Section 4.2 P1

### 54. P2

- order：54

- section：Section 4.2

- locator：P2

- move_code：MECHANISM

- paraphrase_cn：高威胁下经济与声誉损害的负反馈回路太强，影响持续数年。

- rhetorical_function_cn：解释为什么恢复缓慢。

- depends_on_cn：情景2结果

- sets_up_cn：预防优先论点

- evidence_pointer：Section 4.2 P2

### 55. P3

- order：55

- section：Section 4.2

- locator：P3

- move_code：RESULT

- paraphrase_cn：管理层增加约40%投资并很快达到上限，但结果仍不佳，说明延迟和回路使事后弥补无效；预防优于接受损害。

- rhetorical_function_cn：强化预防论点。

- depends_on_cn：情景2结果

- sets_up_cn：Beta对比

- evidence_pointer：Section 4.2 P3

### 56. P1

- order：56

- section：Section 4.3

- locator：P1

- move_code：CONTEXT

- paraphrase_cn：Beta与Alpha几乎相同但防御准备更高，总体得分67.25%，几乎是Alpha两倍。

- rhetorical_function_cn：描述对照案例。

- depends_on_cn：情景3设计

- sets_up_cn：情景3结果

- evidence_pointer：Section 4.3 P1

### 57. P2

- order：57

- section：Section 4.3

- locator：P2

- move_code：RESULT

- paraphrase_cn：Beta在高威胁下峰值损失约17%，随后损失快速下降至情景2的约60%。

- rhetorical_function_cn：报告Beta优势。

- depends_on_cn：Beta基线

- sets_up_cn：机制解释

- evidence_pointer：Section 4.3 P2

### 58. P3

- order：58

- section：Section 4.3

- locator：P3

- move_code：MECHANISM

- paraphrase_cn：因为Beta已有较好防御，能防止有害反馈回路获得强度，更好控制局面。

- rhetorical_function_cn：解释Beta优势原因。

- depends_on_cn：情景3结果

- sets_up_cn：统计验证

- evidence_pointer：Section 4.3 P3

### 59. P1

- order：59

- section：Section 5

- locator：P1

- move_code：RESULT

- paraphrase_cn：表5和图9显示Beta在前两年关键期抵抗攻击波更好；即使最终结果接近，Alpha可能因脆弱性倒闭。

- rhetorical_function_cn：总结模拟比较。

- depends_on_cn：三情景结果

- sets_up_cn：竞争战略含义

- evidence_pointer：Section 5 P1

### 60. P1b

- order：60

- section：Section 5

- locator：P1b

- move_code：PRACTICAL_STAKES

- paraphrase_cn：若两者竞争，Beta会获得Alpha市场份额，只因及时关注网络安全。

- rhetorical_function_cn：把结果转化为战略利益。

- depends_on_cn：情景比较

- sets_up_cn：投资重要性

- evidence_pointer：Section 5 P1

### 61. P2

- order：61

- section：Section 5

- locator：P2

- move_code：RESULT

- paraphrase_cn：图9a显示企业即使在遭受攻击时网络安全支出仍很低，且投资通常不到损害金额的25%。

- rhetorical_function_cn：指出实际投资不足现象。

- depends_on_cn：模型输出

- sets_up_cn：成本效益论证

- evidence_pointer：Section 5 P2

### 62. P3

- order：62

- section：Section 5

- locator：P3

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：进一步列出每年现金流出，包括初始措施成本、年度缓解成本和攻击损害，以比较不同策略。

- rhetorical_function_cn：说明成本对比方法。

- depends_on_cn：模型输出

- sets_up_cn：经济验证

- evidence_pointer：Section 5 P3

### 63. P4

- order：63

- section：Section 5

- locator：P4

- move_code：ROBUSTNESS_OR_BOUNDARY_TEST

- paraphrase_cn：配对t检验P=0.022，95%置信水平下Beta优势统计显著。

- rhetorical_function_cn：提供统计有效性证据。

- depends_on_cn：成本数据

- sets_up_cn：结论可信度

- evidence_pointer：Section 5 P4

### 64. P5

- order：64

- section：Section 5

- locator：P5

- move_code：BENCHMARK_OR_CONTRAST

- paraphrase_cn：与常见SME每年不足€500支出相比，SMECRA导向策略优势更明显，额外支出带来更大损害减少。

- rhetorical_function_cn：建立外部基准。

- depends_on_cn：统计验证

- sets_up_cn：成本效益结论

- evidence_pointer：Section 5 P5

### 65. P6

- order：65

- section：Section 5

- locator：P6

- move_code：RESULT

- paraphrase_cn：即使Alpha的基本approach，额外€115,700支出对应约€1,318,000损害减少；Beta在费用和损害两方面均优于Alpha。

- rhetorical_function_cn：报告关键成本效益数字。

- depends_on_cn：外部基准

- sets_up_cn：系统方法价值

- evidence_pointer：Section 5 P6

### 66. P7

- order：66

- section：Section 5

- locator：P7

- move_code：CONTRIBUTION

- paraphrase_cn：这些模拟不仅展示工具能力，也强调预防和意识对SME的重要性。

- rhetorical_function_cn：提炼管理含义。

- depends_on_cn：全部结果

- sets_up_cn：决策树

- evidence_pointer：Section 5 P7

### 67. P8

- order：67

- section：Section 5

- locator：P8

- move_code：CONTRIBUTION

- paraphrase_cn：SME要在数字化世界获得竞争优势，必须评估并决定网络安全投资，投资要经济可持续并最小化投资+损害总和。

- rhetorical_function_cn：提出投资决策准则。

- depends_on_cn：成本效益结果

- sets_up_cn：决策树功能

- evidence_pointer：Section 5 P8

### 68. P10

- order：68

- section：Section 5

- locator：P10

- move_code：CONTRIBUTION

- paraphrase_cn：决策树说明如何使用SMECRA支持投资分配，关键变量是Regulations, Accounts, Inventory等。

- rhetorical_function_cn：提供可操作指导。

- depends_on_cn：决策准则

- sets_up_cn：结论

- evidence_pointer：Section 5 P10, Fig. 10

### 69. P1

- order：69

- section：Section 6

- locator：P1

- move_code：CONTRIBUTION

- paraphrase_cn：本文引入SMECRA，通过Snapshot Survey和SD模型评估SME当前风险和投资系统影响。

- rhetorical_function_cn：重述贡献。

- depends_on_cn：全文

- sets_up_cn：总结

- evidence_pointer：Section 6 P1

### 70. P2

- order：70

- section：Section 6

- locator：P2

- move_code：CONTRIBUTION

- paraphrase_cn：SMECRA基于系统性视角，优势在于用反馈动态克服线性投资政策的局限。

- rhetorical_function_cn：强调核心创新。

- depends_on_cn：全文结果

- sets_up_cn：与静态方法对比

- evidence_pointer：Section 6 P2

### 71. P3

- order：71

- section：Section 6

- locator：P3

- move_code：CONTRIBUTION

- paraphrase_cn：与常见silo投资思维不同，类别间因组织依赖系统关联，系统方法可能用更少投入达到相同目标，或发现线性投入不足。

- rhetorical_function_cn：提出设计和管理命题。

- depends_on_cn：系统互连命题

- sets_up_cn：研究意义

- evidence_pointer：Section 6 P3

### 72. P4

- order：72

- section：Section 6

- locator：P4

- move_code：BOUNDARY_CONDITION

- paraphrase_cn：SMECRA也可用于其他组织或银行/保险公司评估残余风险。

- rhetorical_function_cn：扩展受众和适用边界。

- depends_on_cn：工具能力

- sets_up_cn：未来应用

- evidence_pointer：Section 6 P4

### 73. P5

- order：73

- section：Section 6

- locator：P5

- move_code：CONTRIBUTION

- paraphrase_cn：研究贡献是建立系统和动态框架评价新视角，模型可定制到其他领域。

- rhetorical_function_cn：理论定位。

- depends_on_cn：全文

- sets_up_cn：结论句

- evidence_pointer：Section 6 P5

### 74. P6

- order：74

- section：Section 6

- locator：P6

- move_code：CONTRIBUTION

- paraphrase_cn：最后总结SMECRA在定义实际/目标风险档案、模拟不同情景和维持可持续方面的价值；系统思维和SD是关键。

- rhetorical_function_cn：收束全文。

- depends_on_cn：全文

- sets_up_cn：无

- evidence_pointer：Section 6 P6

## 写作技术

- gap_construction_cn：先承认现有框架有价值，再指出其静态、无跨域整合、面向大企业等三层次不足；引用权威文献强化动态必要性；最后提出针对SME的具体缺口。

- signposting_cn：摘要末尾和引言末尾给出路线图；每个主要章节以目的句开头；在方法论中预告Snapshot Survey将映射到模型；在情景前说明对照逻辑。

- transition_logic_cn：从缺口（2.3）直接转向因此本文提出SMECRA；从工具描述（第3节）转向需要案例展示（第4节）；从模拟结果（4.3）转向讨论和战略含义（第5节）；从讨论再转向结论（第6节）。

- claim_evidence_rhythm_cn：每个结果段先给图或表数据，再用一两句解释其机制（反馈回路），最后给出管理含义；统计检验放在成本对比之前作为合法性支撑。

- benchmark_narrative_cn：不是用传统性能基准，而是通过情景设计（威胁环境、初始防御）和外部成本基准（€500/年）来建立比较；表5汇总三情景关键指标，表7进行成本效益对照。

- theory_return_cn：在结论中把模拟结果重新连接到系统和动态框架理论视角，并批评线性/silo手段；讨论将可复用设计知识表达为对静态框架的替代。

- contribution_positioning_cn：强调这是针对SME的、实用且易于使用的方法/工具；在管理启示中把贡献扩展到保险和银行等第三方；在研究启示中把贡献置于更广泛动态框架议程。

- novelty_protection_cn：通过三种方式防止退化为一次性性能结果：一是明确指出这是对先前定性CLD的量化扩展，而不是从零开始的模型；二是强调工具可定制和可扩展到其他领域；三是将结果与常见行业做法对比，强调不是又一个模拟而是可操作决策支持。

## 可复用研究与写作程序

### structure_steps

#### 1. 1

- step：1

- writing_job_cn：写引言：从宏观背景收缩到具体用户（SME）和具体方法缺口。

- research_job_cn：完成文献综述，识别现有方法的静态、跨域缺失与情境缺失。

- required_evidence_cn：一组清晰且被引用的缺口陈述；目标用户（SME）的困境数据或权威背景。

- transition_to_next_cn：以因此本文提出直接引出目标和方法。

#### 2. 2

- step：2

- writing_job_cn：在方法章节说明知识基础（框架/理论）如何转化为工具需求。

- research_job_cn：选择或建立基础框架；设计数据采集工具（如调查）、模型变量映射和系统动力学模型。

- required_evidence_cn：能展示知识基础到设计特征的具体映射（如NIST类别→调查题目→模型变量）。

- transition_to_next_cn：以为了演示工具使用过渡到评价设计。

#### 3. 3

- step：3

- writing_job_cn：设计评价：说明案例/情景选择理由，并控制混杂变量。

- research_job_cn：确定情景自变量（威胁环境、初始状态）、统一参数、对照案例。

- required_evidence_cn：情景差异对应研究问题；对照能隔离感兴趣的变量。

- transition_to_next_cn：用预期对比逻辑引出结果。

#### 4. 4

- step：4

- writing_job_cn：报告结果：先给关键图/表，再解释机制（反馈回路），再给出管理含义。

- research_job_cn：运行模型，收集可量化输出；必要时做统计检验。

- required_evidence_cn：结果数据、可能的多情景比较、可识别的模式。

- transition_to_next_cn：用为了进一步确证引入统计/成本对比。

#### 5. 5

- step：5

- writing_job_cn：讨论中把结果提升为设计知识和理论贡献，并与常见做法对比。

- research_job_cn：做外部基准比较、统计显著性检验、成本效益分析；提炼决策规则。

- required_evidence_cn：足够的统计或成本证据；与外部基准的对比数字。

- transition_to_next_cn：用决策树或管理建议向实践转化。

#### 6. 6

- step：6

- writing_job_cn：结论中回到引言缺口，陈述贡献边界和未来工作。

- research_job_cn：明确设计知识可扩展到哪些领域、哪些主张未经验证。

- required_evidence_cn：对缺口闭合的清楚说明；对局限的诚实声明。

- transition_to_next_cn：无。

### most_transferable_moves_cn

1. 先承认现有方法优点再指出多层缺口的修辞

2. 将规范框架转化为调查与模型变量的映射表

3. 用对照案例设计（除关键自变量外全部相同）来提升模拟结果可解释性

4. 在结果后立即用机制（反馈回路）解释，再用统计/成本对比证实

5. 把具体工具结果提升为可复用设计知识（系统性视角优于silo）

### resource_intensive_or_nonstandard_parts_cn

1. 构建完整系统动力学模型（Powersim方程、多个反馈回路）需要系统动力学专长

2. 获得NIST/意大利框架和Essential Controls等专业知识是前提

3. 如果要做真实案例，需要访问真实SME和长期数据；本文只用了虚构案例

4. 配对t检验基于模型生成的数据而非真实观测，统计推断的资源需求较低但外部效度受限

### what_not_to_copy_superficially_cn

1. 不要只复制动态、系统化措辞而没有实际反馈回路和存流量模型

2. 不要在没有对照设计的情况下宣称某个策略优于另一个

3. 不要用单个模拟情景就声称统计显著；还需说明样本量与数据来源

4. 不要照搬简单更好原则而省略关键回路或敏感性讨论

5. 不要忽略表格数字一致性；应核对Table 6/7等汇总数据

- single_best_description_of_the_routine_cn：用规范框架和系统动力学工具构建一个看起来可操作的风险评估与投资模拟器，再通过巧妙设计的对照情景和一个小统计检验把它包装成对SME决策有普遍指导意义的方法。

## 分析边界

全文可读但存在Table 6与Table 7总成本数字不一致，以及文中€1,318,000损害减少与表中数字不完全吻合；缺少附录和模型完整方程，无法验证全部模型细节；三个情景均为作者构建的虚构SME，未见真实数据校准；t检验样本极小且来源单一。
