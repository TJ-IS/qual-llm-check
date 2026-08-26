# Task Characteristics and Incentives in Collaborative Problem Solving: Evidence from Three Field Experiments

- 作者：Jayarajan Samuel; Zhiqiang (Eric) Zheng; Vijay Mookerjee
- 年份 / 期刊：2024 / Information Systems Research
- DOI：10.1287/isre.2021.0118
- 源文件：28044_2024_task-characteristics-and-incentives-in-collaborative-problem-solving-evidence-from-three-field-e.md
- 论文主类型：field_intervention_or_platform_experiment
- 主导写作弧线：phenomenon_mechanism_intervention_field_test
- 置信度：0.9

## 文章级论证概况

- 核心问题：在知识密集型协作问题解决中，任务特征如何影响跨职能协作与正式交接的效率，以及部门级激励如何影响工程师遵循机器推荐进行协作的决策，如何校正激励以提高遵循率。

- 制品与设计：三个主要制品：1）新增协作选项的客户服务流程（实验一）；2）基于数据识别的任务-过程匹配规则（实验二）；3）提供何时协作或正式交接推荐的HRTech Analytics系统（实验三），以及激励校正措施（将评价指标改为总工时、移除周协作比例看板）。

- 客观结果：实验一：引入协作后平均案例周转时间下降25.7%，工程师工时下降13.6%，空闲时间下降31.8%；成本下降主要来自功能案例移向协作流程，而非正式交接移向协作。实验二：879个样例中，LTE高严重性任务协作降低37%总成本，LTE低严重性已知问题任务协作增加55%成本；验证研究确认干预方向。实验三：协作推荐平均遵守率0.7且高方差，当上周协作比例超过0.6时，本周遵守率显著下降0.371；激励校正后，上周比例不再影响遵守率。

- 核心贡献：识别任务特征（难度、不确定性、紧迫性）对跨职能协作成功的影响，填补任务特征如何塑造协作的空白；揭示并纠正部门级激励与公司目标不一致导致的协作回避问题；通过HRTech Analytics展示信息系统以两级支持（流程支持与工作流推荐）促进知识工作，并论证人机协作中激励设计的重要性。

- 整篇论证链：作者在引言建立两个缺口：任务特征如何影响协作未被研究，激励错位如何阻碍协作未被充分研究。实验一证明引入协作选项降低总成本，并确认主要来源是功能案例向协作流程的转移。实验二用HLM和聚类分析细分任务特征，发现高难度高紧急（LTE高严重性）任务适合协作，低紧急低不确定（LTE低严重性已知类型）任务协作反而有害，并通过验证研究确认因果关系。基于这些发现开发HRTech Analytics推荐系统，实验三引入机器推荐，发现工程师对协作推荐遵循率低且波动，原因是部门层面将协作视为依赖，通过断点回归识别出上周协作比例超过阈值导致本周自我纠正。最后实施激励校正（以总工时为评价指标并移除协作比例看板）后，遵循率恢复稳定，证明激励机制对齐的重要性，从而闭合两个初始缺口。

## 类型与写作弧线判定

- 论文主类型判定：文章主要证据来自三个在真实公司运营中进行的现场实验，操纵了数字协作流程和推荐系统，在真实组织中因果检验任务特征和激励对协作行为的影响，符合现场干预或平台实验的特征。

- 主导写作弧线判定：叙事线从现象（协作流程引入后成本降低）出发，通过实验二识别机制（任务特征），然后开发并部署干预（推荐系统），通过实验三现场因果检验，进一步发现激励问题并校正，最终回到理论贡献。

## 研究开展程序

- study_or_phase_count：5

- 研究阶段总序列：阶段顺序为：实验一建立总体效应和来源；实验二先探索性分析识别任务特征，再通过验证性现场干预确认因果；实验三先观察推荐遵循问题和识别激励错位，再通过激励校正检验解决方案。五个阶段逐步从总体价值到机制再到激励干预，形成完整论证链。

### studies_or_phases

#### 1. 实验一：协作流程价值评估与来源分解

- order：1

- name_cn：实验一：协作流程价值评估与来源分解

- question_cn：引入协作选项是否降低解决问题的平均成本？成本降低的来源是什么？

- inputs_and_setting_cn：10,556个案例；238个站点随机使用新流程，492个站点使用传统流程；T1（22个月）和T2（8个月）两个时期。

- designed_or_compared_object_cn：新协作流程 vs 传统流程；功能案例 vs 交叉功能案例。

- baseline_control_or_counterfactual_cn：对照组站点继续使用传统流程；正式交接作为协作的替换选项。

##### objective_metrics

1. CaseTAT

2. EngineerHours

3. CaseIdleTime

4. UsePSGResources

- analysis_method_cn：DID回归（等式1）；Logistic回归（等式2）；子样本DID比较功能案例和交叉功能案例。

- main_result_cn：引入协作后CaseTAT平均下降25.7%，EngineerHours下降13.6%，CaseIdleTime下降31.8%；寻求PSG帮助的几率增加13倍以上；功能案例转向协作池（功能案例工程师小时下降13.3%），但没有证据表明正式交接案例转向协作（总小时无显著变化）。

- argumentative_role_cn：确立协作选项整体有效，并定位成本降低主要来自功能工作向协作的转移，而非正式交接的替代，为后续识别任务特征提供动机。

- remaining_uncertainty_cn：哪种具体任务特征导致功能案例适合协作？为什么正式交接案例没有转移？

- link_to_next_phase_cn：实验一发现功能工作转移之谜促使实验二细分任务特征，寻找协作的适用条件。

##### evidence_pointers

1. Section 4.1-4.5

2. Table 3-7

3. Equation 1-2

#### 2. 实验二：任务特征的探索性分析

- order：2

- name_cn：实验二：任务特征的探索性分析

- question_cn：哪些任务特征（难度、不确定性、紧迫性）使协作比正式交接更有效或更无效？

- inputs_and_setting_cn：879个由CSG工程师选择协作或正式交接的交叉功能案例；收集CSGHours和PSGHours。

- designed_or_compared_object_cn：协作决策 vs 正式交接决策；按任务特征（域、严重性、问题类型）聚类比较。

- baseline_control_or_counterfactual_cn：正式交接作为基线；不同任务特征组合作为分组对照。

##### objective_metrics

1. EngineerHours

2. CSGHours

3. PSGHours

- analysis_method_cn：先计算ICC诊断工程师异质性，然后使用HLM模型（等式4）估计协作效应；K-means聚类将879个案例分为6簇，每簇内再进行HLM；最后用树结构划分特征域验证簇特征。

- main_result_cn：总体平均协作对总工时无显著影响；聚类4（LTE高严重，97%高严重）协作显著降低总成本37%；聚类5（LTE低严重已知问题）协作增加总成本55%；聚类2（LTE低严重未知问题）总成本不变但CSG/PSG负担转移。

- argumentative_role_cn：识别出任务特征与协作效果的匹配关系，为推荐系统提供可直接操作的规则，并说明协作的边界条件。

- remaining_uncertainty_cn：探索性聚类结果是否是因果关系？需要更受控制的干预验证。

- link_to_next_phase_cn：验证研究介入决策以确认聚类特征的因果效应。

##### evidence_pointers

1. Section 5.1-5.2

2. Table 8-11

3. Figure 3

#### 3. 实验二：验证性现场干预

- order：3

- name_cn：实验二：验证性现场干预

- question_cn：对聚类4和聚类5类型案例，强制改变协作/交接决策能否按预测方向降低成本？

- inputs_and_setting_cn：184个需要PSG帮助的案例：71个聚类4型（LTE高严重）和51个聚类5型（LTE低严重已知），研究持续3个月。

- designed_or_compared_object_cn：强制推荐协作 vs 工程师自选（正式交接/协作）；对聚类5强制推荐正式交接 vs 自选。

- baseline_control_or_counterfactual_cn：未被干预的工程师自选组作为对照。

##### objective_metrics

1. EngineerHours

- analysis_method_cn：t检验比较干预组（I）与非干预组（NI、FH、C）的均值。

- main_result_cn：聚类4型中，强制协作的平均工时13.86小时显著低于自选正式交接的35.63小时（下降61%）；聚类5型中，强制正式交接的15.13小时显著低于自选协作的33.83小时（下降55.3%）。

- argumentative_role_cn：从观察到因果的转折点，确认任务特征（LTE高紧急、LTE低紧急已知）与协作效果的关系，为系统设计提供可信依据。

- remaining_uncertainty_cn：实际部署推荐时，工程师是否遵循？即使推荐正确，激励是否影响行为？

- link_to_next_phase_cn：基于已验证的规则部署HRTech Analytics，进入实验三研究用户遵循行为。

##### evidence_pointers

1. Section 5.3

2. Figures 4-5

#### 4. 实验三：推荐系统合规研究

- order：4

- name_cn：实验三：推荐系统合规研究

- question_cn：工程师是否遵循机器推荐？如果不遵循，存在怎样的激励错位机制？

- inputs_and_setting_cn：HRTech Analytics部署后的29周数据，包括每周推荐协作/交接的案例数量和实际遵循数量；CSG工程师；每周看板显示协作比例。

- designed_or_compared_object_cn：协作推荐 vs 正式交接推荐的合规率；上周协作解决比例对本周合规的影响。

- baseline_control_or_counterfactual_cn：机器推荐作为基准；断点两侧数据形成自然对照。

##### objective_metrics

1. 协作合规比例

2. 正式交接合规比例

3. 上周协作比例

- analysis_method_cn：描述性图（图6、7），断点回归（RD）识别拐点，通过留一法选择带宽，局部线性回归估计局部平均处理效应（等式5）。

- main_result_cn：交接合规均值0.79、标准差0.006，协作合规均值0.7、标准差0.099；当上周协作解决案例比例超过0.6时，本周协作合规率显著下降0.371；访谈表明协作被视为依赖外部部门。

- argumentative_role_cn：揭示机器推荐在真实环境中面临的组织障碍——部门级激励与公司目标不一致，构成第二缺口的关键证据。

- remaining_uncertainty_cn：改变激励（如改为总工时评价并移除看板）能否消除自我纠正？

- link_to_next_phase_cn：激励校正步骤直接检验该不确定性，实现从问题到解决的闭环。

##### evidence_pointers

1. Section 6.1-6.2

2. Figures 6-8

3. Table 13

4. Equation 5

#### 5. 实验三：激励校正

- order：5

- name_cn：实验三：激励校正

- question_cn：将评价指标改为总工时并移除看板后，协作推荐合规是否变得稳定不再受上周比例影响？

- inputs_and_setting_cn：激励校正后12周数据；继续使用HRTech Analytics；每周采集与前期相同指标。

- designed_or_compared_object_cn：激励校正后的12周 vs 校正前的29周；回归上周协作比例对合规的影响。

- baseline_control_or_counterfactual_cn：校正前效应作为对照；校正后回归系数不显著即为成功。

##### objective_metrics

1. 协作合规比例

- analysis_method_cn：描述性图（图9）展示合规趋势；回归等式6估计校正后上周协作比例对合规的影响。

- main_result_cn：校正后协作合规均值0.786、标准差0.01，上周协作比例系数β1=-0.0142不显著，表明不再有自我纠正效应。

- argumentative_role_cn：证明激励对齐是推荐系统有效落地的关键，完成对第二个引言缺口的实证回答。

- remaining_uncertainty_cn：是否长期有效？是否可推广至其他组织？文章在讨论和结论中给出边界与未来方向。

- link_to_next_phase_cn：进入讨论，将发现整合为理论贡献和管理启示。

##### evidence_pointers

1. Section 6.3

2. Figure 9

3. Table 14

4. Equation 6

## 各部分修辞架构

### abstract_moves

1. CONTEXT
摘要开始提出研究主题：IT支持的协作问题解决在客户支持环境。

2. STUDY_OVERVIEW
预告三场顺序现场实验。

3. RESULT
转述每个实验的关键发现：成本降低并非协作总是优于交接；任务特征决定协作适用性；激励错位导致偏离推荐。

4. CONTRIBUTION
末尾声明实践启示：为企业开发和实施知识密集型任务支持系统提供启示。

### introduction_moves

1. CONTEXT
第1段建立跨职能协作重要性和管理挑战。

2. LIMITATION
指出现有文献关注团队构成等障碍，忽略任务特征。

3. GAP
明确任务特征如何塑造协作的空白。

4. RQ_OR_OBJECTIVE
首次提出研究问题：任务特征（复杂度、不确定性、紧急度）的作用。

5. GAP
第二缺口：激励错位如何阻碍协作。

6. RQ_OR_OBJECTIVE
第二次研究问题：提供纠正激励错位的策略。

7. PHENOMENON
描述公司环境中正式交接与协作两种求助方式。

8. STUDY_OVERVIEW
概述三个实验的顺序和主要发现。

9. CONTRIBUTION
列举两条主要贡献：任务特征与激励。

### theory_and_knowledge_moves

1. PRIOR_KNOWLEDGE
第2节总结协作的好处和团队组成文献。

2. LIMITATION
指出任务特征文献缺乏共识、数据不足。

3. PRIOR_KNOWLEDGE
引用Merton等关于个人激励和学术协作中奖励分配的早期工作。

4. THEORY_PROPOSITION
推断如果个人激励与公司目标不一致，知识工作者可能不会在必要时协作。

### artifact_design_moves

1. REQUIREMENT
第3.3节描述传统过程的低效在于求助方式，需要新的帮助方式。

2. DESIGN_FEATURE
第3.4节定义协作选项（同步工作）和正式交接（异步）。

3. MECHANISM
分析正式交接的文档开销导致成本上升，协作可减少空闲。

4. DESIGN_FEATURE
第6节介绍HRTech Analytics系统推荐协作或交接。

5. DESIGN_FEATURE
第6.3节描述激励校正：以总工时评价和移除看板。

### evaluation_moves

1. METHOD_JUSTIFICATION
第4.2节解释站点层面随机化而分析在案例层面，并承认限制。

2. BENCHMARK_OR_CONTRAST
第4.3节使用DiD，对照组和前期作为基准。

3. METHOD_JUSTIFICATION
第5.1节通过ICC诊断工程师异质性，采用HLM处理依赖。

4. BENCHMARK_OR_CONTRAST
第5.2节使用K-means聚类和树结构划分，定义子群对比。

5. BENCHMARK_OR_CONTRAST
第5.3节验证研究比较干预组与自选组。

6. METHOD_JUSTIFICATION
第6.2节用断点回归识别行为拐点，选择带宽。

7. ROBUSTNESS_OR_BOUNDARY_TEST
第6.3节激励校正后重复回归作为验证。

### discussion_and_contribution_moves

1. CONTRIBUTION
第7段第1段重述首个贡献：任务特征与协作结果的细化认知。

2. CONTRIBUTION
第二个贡献：非合规来源和激励设计。

3. CONTRIBUTION
第三个贡献：人机协作中的推荐系统正面案例。

4. BOUNDARY_CONDITION
讨论管理者如何根据任务特征分配。

5. BOUNDARY_CONDITION
讨论干预策略：仅在差异化结果时干预。

6. BOUNDARY_CONDITION
讨论激励对齐的一般性。

7. LIMITATION_AND_FUTURE
第8节列出未考虑满意度、学习、疫情远程等限制。

## 理论/知识到设计的翻译

### 知识/理论基础

1. 任务特征理论：Hackman (1968), Wood (1986), Campbell (1988) 关于任务难度与复杂性的分类。

2. 任务-协作匹配：Daley (1978) 指出不确定性高需要协作；Graesser等 (2018) 困难任务需要协作。

3. 激励理论：Merton (1968), Bikard等 (2015), Vakili等 (2021) 关于个体奖励与众创工作激励错位。

4. 人机协作：Fügener等 (2021, 2022) 关于人在环中协作与委托。

- 理论—设计耦合：partial

- 耦合判定理由：理论为任务特征选择（难度、不确定性、紧迫性）和激励概念提供了语言和变量定义，但具体的协作推荐规则并非从理论演绎而来，而是基于实验二数据中的聚类和统计分析挖掘发现（如LTE高严重适合协作，LTE低严重已知适合交接），属于数据驱动设计。

- 理论到设计翻译链：理论命题：任务复杂度和不确定性增加协作需求 → 机制假设：跨领域知识互补能降低成本 → 设计要求：识别高难度、高不确定、高紧急任务需要协作 → 制品选择：将LTE视为高难度、未知问题类型视为高不确定性、高严重视为高紧迫，作为推荐系统的规则变量 → 被检验差异：协作 vs 正式交接在不同特征组合上的成本差异 → 客观结果：在LTE高严重上协作降本，在LTE低严重已知上协作增本。激励理论：个体激励与组织目标不一致会阻碍协作 → 机制：部门对协作的负面感知（依赖外部）导致自我纠正 → 设计要求：以总工时为评价指标并移除看板 → 客观结果：合规稳定。

### mapping_table

#### 1. 1

- theory_or_knowledge_claim_cn：任务难度增加时协作需求上升（Hackman 1968; Autor et al. 2003; Graesser et al. 2018）

- mechanism_cn：困难任务需要跨领域知识，跨职能团队可整合知识。

- design_requirement_cn：识别高难度任务并推荐协作。

- artifact_choice_cn：将LTE（新兴技术）编码为高难度；系统对LTE任务倾向推荐协作。

- evaluated_contrast_cn：在LTE高严重案例中，协作 vs 正式交接的成本比较。

- objective_result_cn：协作降低总工时37%（聚类4）。

##### evidence_pointers

1. Section 5.2, Table 10 聚类4

#### 2. 2

- theory_or_knowledge_claim_cn：任务紧迫性提升协作需求（Daley 1978 虽未直接测紧迫，但时间约束影响协作）

- mechanism_cn：紧急任务由于时间压力需要同步合作避免信息传递延迟。

- design_requirement_cn：高严重性（时间紧迫）任务推荐协作。

- artifact_choice_cn：HRTech将高严重性作为协作推荐的加分项。

- evaluated_contrast_cn：LTE高严重（紧急） vs LTE低严重（不紧急）中协作的效果。

- objective_result_cn：LTE高严重中协作降本37%；LTE低严重中协作增本55%。

##### evidence_pointers

1. Section 5.2, Table 10 聚类4, 5

#### 3. 3

- theory_or_knowledge_claim_cn：不确定性任务可能增加协作（Daley 1978）

- mechanism_cn：未知问题需要更多调查和知识组合，但可能只是工作转移而非总成本下降。

- design_requirement_cn：需要区分不确定性与其他特征交互。

- artifact_choice_cn：系统将未知问题类型作为变量，但不单独推荐协作；必须结合紧急度。

- evaluated_contrast_cn：LTE低严重未知 vs LTE低严重已知：协作对总成本影响。

- objective_result_cn：两类均无总成本显著降低；未知类型产生工时从CSG向PSG转移（聚类2）。

##### evidence_pointers

1. Section 5.2, Table 10 聚类2

#### 4. 4

- theory_or_knowledge_claim_cn：个体激励与组织目标对齐是协作成功前提（Vakili et al. 2021; Merton 1968）

- mechanism_cn：部门级激励（看板上显示协作比例）传达出协作是依赖的负向信号，导致工程师自我纠正。

- design_requirement_cn：移除强化局部激励的看板，改为与公司总成本直接对齐的评价指标。

- artifact_choice_cn：激励校正：评价指标改为平均总工时（CSG+PSG），移除看板。

- evaluated_contrast_cn：校正前 vs 校正后，上周协作比例对本周合规的回归斜率。

- objective_result_cn：校正前β1=-0.371显著；校正后β1=-0.0142不显著。

##### evidence_pointers

1. Section 6.2, Table 13; Section 6.3, Table 14

## 评价逻辑

### evaluation_modes

1. 现场随机实验（站点层面随机化）

2. DID面板回归

3. 分层线性模型（HLM）

4. 探索性聚类分析

5. 受控干预验证（准实验）

6. 断点回归（RD）

7. 前后对照回归

- why_these_evaluations_cn：实验一需要总体因果效力，故用DID；实验二发现工程师异质性需要HLM；探索性聚类需要后续干预实验证明因果，故用验证研究；实验三要识别行为门槛和激励影响，故用断点回归；激励校正后再次回归检验充分性。每种方法对应论证链中的特定断言。

- benchmark_and_contrast_chain_cn：主要基线是传统过程和正式交接。实验一用对照组站点和时间先前时期作为DID基线，后面用正式交接作为协作的对比。实验二用同案例中正式交接结果作为协作基线；聚类和树结构提供不同特征组合间的对照。验证研究用工程师自选作为一种拟对照。实验三用机器推荐作为基准，并将校正前回归作为激励不对齐的基线，校正后回归作为对齐后的对比。整个链条从宏观（整体成本）到微观（特征分组）再到行为（合规与激励），逐层深化。

### claim_evidence_ledger

#### 1. 引入协作选项降低平均成本

- claim_cn：引入协作选项降低平均成本

- evidence_cn：DID回归β1负显著（CaseTAT -0.2977, EngineerHours -0.1470, IdleTime -0.3834），且模型固定效应控制站点/工程师和时间。

- supported：是

#### 2. 成本降低来自功能案例转向协作而非正式交接转向协作

- claim_cn：成本降低来自功能案例转向协作而非正式交接转向协作

- evidence_cn：功能案例子样本DID显示EngHours下降13.3%显著；交叉功能子样本DID显示EngHours -0.4116不显著。

- supported：是

#### 3. LTE高严重任务协作降低成本，LTE低严重已知任务协作增加成本

- claim_cn：LTE高严重任务协作降低成本，LTE低严重已知任务协作增加成本

- evidence_cn：聚类4β1=-0.4821***（总成本降37%），聚类5β1=0.4382***（总成本升55%）；验证研究强制干预显示显著降低。

- supported：是

#### 4. 部门激励导致工程师自我纠正偏离协作推荐

- claim_cn：部门激励导致工程师自我纠正偏离协作推荐

- evidence_cn：RD模型断点回归β1=-0.3708***，且在图7中呈现拐点；访谈支持机制。

- supported：是

#### 5. 激励校正消除自我纠正

- claim_cn：激励校正消除自我纠正

- evidence_cn：校正后回归β1=-0.0142不显著，合规均值提高且方差降低。

- supported：是

- internal_validity_strategy_cn：站点随机化，案例级DID，固定效应吸收工程师/站点时间不变特征，ICC诊断并采用HLM处理工程师内相关，验证研究主动操纵决策排除选择偏差，RD断点提供局部因果辨识，激励校正前后同一系统设计比较增加可信度。

- external_validity_strategy_cn：使用真实公司全量案例，讨论覆盖类似票据式客户服务场景；验证研究在三个月内重复确认；从单一企业推广时作者明确限制并说明适用情境。

- what_is_not_actually_tested_cn：任务特征变量（LTE、问题类型、严重度）被作为客观代理，但未直接操纵任务难度和不确定性本身；长期学习效应未检验；激励校正的持续效应未超过12周；其他行业或非票据式流程未被直接证据覆盖。

## 贡献闭环

- technical_claim_cn：HRTech Analytics推荐系统基于任务特征（LTE、严重性、问题类型）能在成本上提供显著优于人类自主选择的结果（验证研究和合规分析支持）。

- artifact_claim_cn：协作选项和系统推荐是降低成本和改善合规的有效设计；具体可识别设计元素（推荐规则、评价指标、看板移除）导致了行为改变。

- mechanism_claim_cn：协作对任务特征的适用性源于同步知识整合对困难紧迫任务有效，而对低紧急已知任务造成冗余成本；激励错位通过部门对协作的负面归因（依赖外部）触发自我纠正。

- boundary_claim_cn：结果适用于面向票据的高科技客户服务环境；当任务可明确分类且团队结构清楚时；当利益机制存在部门可见性时。

- reusable_design_knowledge_cn：1) 应在推荐系统中编码任务特征（难度、紧急度、不确定性）作为流程选择依据；2) 推荐系统部署需审计既有激励，评估部门层面是否将推荐行为视为负面；3) 干预策略应仅在推荐能改变客观结果时采用，区分人机知识重叠与机器独有知识场景。

- theoretical_contribution_cn：扩展任务特征对协作成功的影响认识，用现场数据证明任务-流程匹配的重要性；将个人激励与组织目标错位引入协作问题解决研究，并展示纠正路径；人机协作文献获得一个推荐系统设计如何改善协作有效性的正面实例。

- how_discussion_closes_intro_gap_cn：讨论中第一、第二点直接对应引言两个缺口：第一点梳理任务特征对协作影响，填补文献空白；第二、三点针对激励错位，展示识别和解决过程，从而闭合缺口。

- overclaim_or_unsupported_leaps_cn：从单一企业、单一时期概化到各类服务流程有一定跳跃；验证研究样本有限；激励校正的必要性依赖未直接控制的潜在混淆（如同时变化的组织文化）；任务特征的代理变量过于粗糙（LTE→高难度）可能忽略语义。

## 句级写作动作图谱

### 1. Abstract P1 S1

- order：1

- section：Abstract

- locator：Abstract P1 S1

- move_code：CONTEXT

- paraphrase_cn：我们利用三个连续现场实验研究知识工作中IT支持的协作问题解决。

- rhetorical_function_cn：开门见山指出研究对象和方法组合。

- depends_on_cn：无，作为摘要起点。

- sets_up_cn：为摘要后续结果陈述提供背景。

- evidence_pointer：Abstract

### 2. Abstract P1 S2-S3

- order：2

- section：Abstract

- locator：Abstract P1 S2-S3

- move_code：STUDY_OVERVIEW

- paraphrase_cn：实验一检查新协作过程是否降低问题解决成本；实验二识别协作何时有效；实验三检验用户对推荐的反应。

- rhetorical_function_cn：概述研究三部曲，建立期待。

- depends_on_cn：上一句的研究背景。

- sets_up_cn：为读者提供全文总览。

- evidence_pointer：Abstract

### 3. Abstract P1 S4-S6

- order：3

- section：Abstract

- locator：Abstract P1 S4-S6

- move_code：RESULT

- paraphrase_cn：有趣的是，成本降低出现不是因为协作总是优于交接，而是因为内部支持工作向协作转移；任务新颖性和时间限制决定合适模式；部门级激励导致偏离推荐，而全局激励校准可提高遵循。

- rhetorical_function_cn：压缩三个实验的关键发现。

- depends_on_cn：研究阶段的摘要描述。

- sets_up_cn：突出‘有趣’和机制，吸引读者阅读正文。

- evidence_pointer：Abstract

### 4. Abstract P2 S1

- order：4

- section：Abstract

- locator：Abstract P2 S1

- move_code：CONTRIBUTION

- paraphrase_cn：研究为发展实施支持知识密集型任务的信息系统提供实践启示。

- rhetorical_function_cn：宣称对实践的贡献。

- depends_on_cn：所有已报告发现。

- sets_up_cn：暗示研究不仅学术更有应用价值。

- evidence_pointer：Abstract

### 5. Introduction P1 S1

- order：5

- section：Introduction

- locator：Introduction P1 S1

- move_code：CONTEXT

- paraphrase_cn：管理的一个关键目标是有效地组织群体协同工作，但创建和维持有效团队持续挑战公司。

- rhetorical_function_cn：将问题置于组织管理大背景，强调重要性。

- depends_on_cn：无。

- sets_up_cn：引出后续关于部门化与协作的张力。

- evidence_pointer：Introduction P1 S1

### 6. Introduction P1 S2-S3

- order：6

- section：Introduction

- locator：Introduction P1 S2-S3

- move_code：PHENOMENON

- paraphrase_cn：部门化带来专业化和规模经济，而跨职能协作带来新知识和视角，知识工作中团队协作成为常态。

- rhetorical_function_cn：描述组织内在矛盾，为协作重要性铺垫。

- depends_on_cn：上句关于管理目标。

- sets_up_cn：为后文指出文献关注团队构成而忽略任务特征做对比。

- evidence_pointer：Introduction P1 S2-S3

### 7. Introduction P2 S1

- order：7

- section：Introduction

- locator：Introduction P2 S1

- move_code：LIMITATION

- paraphrase_cn：尽管已有研究找出很多协作障碍如团队构成、搭便车、团队动态，但适宜跨职能团队的任务选择未得到所需关注。

- rhetorical_function_cn：指出现有文献的盲点。

- depends_on_cn：前文协作重要性论述。

- sets_up_cn：引出第一个研究缺口。

- evidence_pointer：Introduction P2 S1

### 8. Introduction P2 S2-S4

- order：8

- section：Introduction

- locator：Introduction P2 S2-S4

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：早期研究如Hackman显示任务难度增加协作需求，Daley调查显示团队协作用于高度不确定任务，最近工作表明复杂任务需要团队，但文献未系统研究任务特征如何塑造协作。

- rhetorical_function_cn：总结已有的零散认知，说明证据边际不清。

- depends_on_cn：上一句的缺口定位。

- sets_up_cn：强调现有文献的空白和理论重要性。

- evidence_pointer：Introduction P2 S2-S4

### 9. Introduction P2 S5

- order：9

- section：Introduction

- locator：Introduction P2 S5

- move_code：WHY_GAP_MATTERS

- paraphrase_cn：这是令人困惑的，因为任务分配在工业中重要，任务特征清晰存在，且任务管理工具普遍使用。

- rhetorical_function_cn：解释为什么该缺口值得研究。

- depends_on_cn：上文指出的文献空缺。

- sets_up_cn：引出第一个研究问题。

- evidence_pointer：Introduction P2 S5

### 10. Introduction P2 S6

- order：10

- section：Introduction

- locator：Introduction P2 S6

- move_code：RQ_OR_OBJECTIVE

- paraphrase_cn：因此研究问题一：任务特征（复杂度、不确定性、紧迫性）在跨职能团队协作解决问题成功中的作用。

- rhetorical_function_cn：明确第一研究问题。

- depends_on_cn：缺口重要性判断。

- sets_up_cn：全文核心问题之一。

- evidence_pointer：Introduction P2 S6

### 11. Introduction P3 S1-S2

- order：11

- section：Introduction

- locator：Introduction P3 S1-S2

- move_code：MECHANISM

- paraphrase_cn：个人是否协作受组织利益和个人奖励共同驱动，若两者不一致，知识工作者可能应协作时不协作。

- rhetorical_function_cn：提出激励错位的潜在机制。

- depends_on_cn：前文关于协作重要性的论述。

- sets_up_cn：引出第二个缺口。

- evidence_pointer：Introduction P3 S1-S2

### 12. Introduction P3 S3

- order：12

- section：Introduction

- locator：Introduction P3 S3

- move_code：GAP

- paraphrase_cn：尽管重要，激励错位如何阻碍工业环境中的协作以及如何对齐个人与公司激励未被文献充分关注。

- rhetorical_function_cn：定位第二个空白。

- depends_on_cn：前句机制逻辑。

- sets_up_cn：引出研究问题二。

- evidence_pointer：Introduction P3 S3

### 13. Introduction P3 S4

- order：13

- section：Introduction

- locator：Introduction P3 S4

- move_code：RQ_OR_OBJECTIVE

- paraphrase_cn：研究问题二旨在通过提供纠正激励错位的策略来维持跨职能协作，为此做出贡献。

- rhetorical_function_cn：明确第二研究问题。

- depends_on_cn：缺口界定。

- sets_up_cn：全文第二目标。

- evidence_pointer：Introduction P3 S4

### 14. Introduction P4 S1-S2

- order：14

- section：Introduction

- locator：Introduction P4 S1-S2

- move_code：CONTEXT

- paraphrase_cn：这些缺口存在部分因为缺乏细粒度数据，但IT能收集个体和任务级数据；我们的数据来自全球领先的高科技ICT公司。

- rhetorical_function_cn：说明采用现场数据的原因，介绍数据条件。

- depends_on_cn：缺口描述。

- sets_up_cn：引出具体问题情境。

- evidence_pointer：Introduction P4 S1-S2

### 15. Introduction P5 S1-S3

- order：15

- section：Introduction

- locator：Introduction P5 S1-S3

- move_code：PHENOMENON

- paraphrase_cn：工程师收到客户故障单，可在收到的部门内解决，或寻求产品专家帮助；求助方式有两种：正式交接或协作。

- rhetorical_function_cn：生动描述实际决策情境。

- depends_on_cn：研究情境介绍。

- sets_up_cn：为实验定义两个求助方式。

- evidence_pointer：Introduction P5 S1-S3

### 16. Introduction P6 S1-S3

- order：16

- section：Introduction

- locator：Introduction P6 S1-S3

- move_code：RESULT

- paraphrase_cn：实验一显示新工作形式降低成本；实验二揭示利益来源和利于协作的任务特征，并说明某些困难任务非紧急时协作反而有害。

- rhetorical_function_cn：提前总结前两个实验的结果。

- depends_on_cn：研究情境。

- sets_up_cn：为推荐系统开发做铺垫。

- evidence_pointer：Introduction P6 S1-S3

### 17. Introduction P7 S1-S4

- order：17

- section：Introduction

- locator：Introduction P7 S1-S4

- move_code：STUDY_OVERVIEW

- paraphrase_cn：公司实施助手系统HRTech Analytics指导何时协作或交接；实验三提供推荐并发现部门激励影响遵循；校正激励后工程师基于公司利益决策。

- rhetorical_function_cn：概述实验三和最终解决方案。

- depends_on_cn：实验二成果。

- sets_up_cn：引出贡献声明。

- evidence_pointer：Introduction P7 S1-S4

### 18. Introduction P8 S1-S2

- order：18

- section：Introduction

- locator：Introduction P8 S1-S2

- move_code：CONTRIBUTION

- paraphrase_cn：第一项贡献：发现任务特征对协作有利或有害的证据，连接任务特征与团队协作需求。

- rhetorical_function_cn：声明任务特征贡献。

- depends_on_cn：所有实验发现。

- sets_up_cn：与引言中第一缺口呼应。

- evidence_pointer：Introduction P8 S1-S2

### 19. Introduction P9 S1-S2

- order：19

- section：Introduction

- locator：Introduction P9 S1-S2

- move_code：CONTRIBUTION

- paraphrase_cn：第二项贡献：识别激励在推荐系统成功实施中的作用，展示激励错位会阻止协作，并提供管理意义。

- rhetorical_function_cn：声明激励贡献。

- depends_on_cn：实验三发现。

- sets_up_cn：呼应第二缺口。

- evidence_pointer：Introduction P9 S1-S2

### 20. Prior Work P1 S1-S3

- order：20

- section：Prior Work

- locator：Prior Work P1 S1-S3

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：协作提高生产力、创新、好创意概率，但先前工作主要关注团队构成。

- rhetorical_function_cn：总结文献收益和集中点。

- depends_on_cn：引言贡献定位。

- sets_up_cn：指出任务特征被忽略。

- evidence_pointer：Prior Work P1 S1-S3

### 21. Prior Work P2 S1-S2

- order：21

- section：Prior Work

- locator：Prior Work P2 S1-S2

- move_code：GAP

- paraphrase_cn：任务特征对协作成败的影响文献稀薄，原因在于特征定义无共识和缺少细粒度数据。

- rhetorical_function_cn：深入解释任务特征空白的原因。

- depends_on_cn：上文协作收益综述。

- sets_up_cn：为细粒度数据研究提供依据。

- evidence_pointer：Prior Work P2 S1-S2

### 22. Prior Work P2 S3

- order：22

- section：Prior Work

- locator：Prior Work P2 S3

- move_code：CONTRIBUTION

- paraphrase_cn：据我们所知，本研究首次实证建立细粒度任务特征（难度、不确定性、紧迫性）在成功协作中的作用。

- rhetorical_function_cn：声明研究的新颖性。

- depends_on_cn：前述空白。

- sets_up_cn：强化实证贡献。

- evidence_pointer：Prior Work P2 S3

### 23. Prior Work P3 S1-S4

- order：23

- section：Prior Work

- locator：Prior Work P3 S1-S4

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：协作也有成本：社会惰化、协调成本、冲突；个体可能因联合工作而报酬不成比例，早期科学中的奖励不平等。

- rhetorical_function_cn：平衡讨论协作成本。

- depends_on_cn：无。

- sets_up_cn：引入激励错位概念。

- evidence_pointer：Prior Work P3 S1-S4

### 24. Prior Work P4 S1-S4

- order：24

- section：Prior Work

- locator：Prior Work P4 S1-S4

- move_code：THEORY_PROPOSITION

- paraphrase_cn：个体选择协作若收益超过成本；在学术研究中作者在个体归因更多时增加协作。但工业中激励错位未被报告。我们假设如果个人激励与公司目标不一致，个体可能不选择应选的协作。

- rhetorical_function_cn：将学术协作激励文献延伸到工业情境。

- depends_on_cn：协作成本和收益综述。

- sets_up_cn：立起第二研究支柱。

- evidence_pointer：Prior Work P4 S1-S4

### 25. Section 3.3 Motivation P1-S2

- order：25

- section：Research Context

- locator：Section 3.3 Motivation P1-S2

- move_code：LIMITATION

- paraphrase_cn：传统过程的问题不在于CSG工程师求助，而在于正式交接需大量文档工作，可能提高总工时，因此提供协作选项有望降低成本。

- rhetorical_function_cn：指出传统过程低效的具体原因。

- depends_on_cn：前面描述的传统流程。

- sets_up_cn：为新过程设计提供动机。

- evidence_pointer：Section 3.3, paragraph beginning with 'In its existing business process'

### 26. Section 3.4 New Process P1-S5

- order：26

- section：Research Context

- locator：Section 3.4 New Process P1-S5

- move_code：DESIGN_FEATURE

- paraphrase_cn：新过程在传统正式交接外加上了协作选项，CSG工程师可同步求助PSG工程师，由此产生四类案例：功能、交叉交接、交叉协作。

- rhetorical_function_cn：明确定义制品设计的关键特征。

- depends_on_cn：传统过程描述。

- sets_up_cn：为实验一变量定义做准备。

- evidence_pointer：Section 3.4

### 27. Section 4 P1 S1-S2

- order：27

- section：Experiment One

- locator：Section 4 P1 S1-S2

- move_code：RQ_OR_OBJECTIVE

- paraphrase_cn：实验一的问题是协作是否降低平均问题解决成本，以及所有交叉功能任务是否都受益还是仅某些功能工作受益。

- rhetorical_function_cn：设置实验一的研究问题。

- depends_on_cn：引言铺垫。

- sets_up_cn：引导后续DID分析。

- evidence_pointer：Section 4, opening paragraph

### 28. Section 4.2 Experiment Design P3

- order：28

- section：Experiment One

- locator：Section 4.2 Experiment Design P3

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：随机化在站点层面而非案例层面，因为客户感知，分析在案例层面进行。

- rhetorical_function_cn：说明随机化单位的合理性及局限。

- depends_on_cn：研究设计需求。

- sets_up_cn：承认潜在设计限制，为DID方法使用辩护。

- evidence_pointer：Section 4.2 P3

### 29. Section 4.3 Econometric Model P1-S4

- order：29

- section：Experiment One

- locator：Section 4.3 Econometric Model P1-S4

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：使用DID比较处理与对照组在实验前后的变化，检验交互项β1是否为零。

- rhetorical_function_cn：阐述识别策略。

- depends_on_cn：随机化设计。

- sets_up_cn：为回归结果解释提供基础。

- evidence_pointer：Section 4.3

### 30. Section 4.4 Results P1-S2

- order：30

- section：Experiment One

- locator：Section 4.4 Results P1-S2

- move_code：RESULT

- paraphrase_cn：回归显示引入协作后案例周转时间下降25.7%，工程师工时下降13.6%，空闲时间下降31.8%，总体有益。

- rhetorical_function_cn：报告实验一第一组结果。

- depends_on_cn：DID模型。

- sets_up_cn：随后分解利益来源。

- evidence_pointer：Section 4.4, Table 4

### 31. Section 4.5 Isolating Source P1-S1

- order：31

- section：Experiment One

- locator：Section 4.5 Isolating Source P1-S1

- move_code：HYPOTHESIS_OR_PROPOSITION

- paraphrase_cn：由于增加帮助方式，寻求PSG帮助的倾向必然弱增；我们据此两步分离来源。

- rhetorical_function_cn：提出一个可检验逻辑前提。

- depends_on_cn：新过程设计。

- sets_up_cn：指导后续两个证据步骤。

- evidence_pointer：Section 4.5 P1

### 32. Section 4.5 Isolating Source P2

- order：32

- section：Experiment One

- locator：Section 4.5 Isolating Source P2

- move_code：RESULT

- paraphrase_cn：Logit回归表明寻求PSG帮助的几率增加13倍。

- rhetorical_function_cn：支撑前提。

- depends_on_cn：式2回归。

- sets_up_cn：引出子样本分析。

- evidence_pointer：Section 4.5, Table 5

### 33. Section 4.5 P4-P5

- order：33

- section：Experiment One

- locator：Section 4.5 P4-P5

- move_code：RESULT

- paraphrase_cn：功能案例的子样本显示工程师小时下降13.3%，而正式交接案例的工程师小时无显著变化，所以利益来自功能工作转向协作。

- rhetorical_function_cn：说明来源分解的具体结果。

- depends_on_cn：子样本DID。

- sets_up_cn：为实验二任务特征研究提供动机。

- evidence_pointer：Section 4.5, Tables 6-7

### 34. Section 5 P1-S1-S3

- order：34

- section：Experiment Two

- locator：Section 5 P1-S1-S3

- move_code：TRANSITION

- paraphrase_cn：基于实验一发现协作利益源于功能案例，实验二转向研究哪些任务特征使协作有利。

- rhetorical_function_cn：连接实验一与实验二。

- depends_on_cn：实验一结果。

- sets_up_cn：定义实验二目标。

- evidence_pointer：Section 5, paragraph beginning with 'The primary outcome'

### 35. Section 5.1 P1-S3

- order：35

- section：Experiment Two

- locator：Section 5.1 P1-S3

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：因为同一工程师处理多个案例，结果可能相关，OLS不适用，需检验IC并采用HLM。

- rhetorical_function_cn：论证模型选择。

- depends_on_cn：数据面板结构。

- sets_up_cn：引入HLM模型。

- evidence_pointer：Section 5.1

### 36. Section 5.1 Table 8

- order：36

- section：Experiment Two

- locator：Section 5.1 Table 8

- move_code：RESULT

- paraphrase_cn：所有结果变量的ICC在0.59到0.64且显著，确认工程师异质性大，需采用HLM。

- rhetorical_function_cn：实证辩护HLM。

- depends_on_cn：ICC诊断。

- sets_up_cn：使用模型4。

- evidence_pointer：Section 5.1 Table 8

### 37. Section 5.1 Table 9

- order：37

- section：Experiment Two

- locator：Section 5.1 Table 9

- move_code：RESULT

- paraphrase_cn：全体879案例中协作对总工时无显著影响，但显著增加PSG工时减少CSG工时。

- rhetorical_function_cn：报告平均值无效应，为后续聚类异质性铺垫。

- depends_on_cn：HLM估计。

- sets_up_cn：推动探索性聚类。

- evidence_pointer：Section 5.1 Table 9

### 38. Section 5.2 Exploratory Custer P1-S1

- order：38

- section：Experiment Two

- locator：Section 5.2 Exploratory Custer P1-S1

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：因为平均值掩盖异质性，我们用K-means将案例分为六簇并分别估计协作效应。

- rhetorical_function_cn：解释为何聚类。

- depends_on_cn：平均效应不显著。

- sets_up_cn：展示分簇效应表。

- evidence_pointer：Section 5.2 P1

### 39. Section 5.2 P2-P5

- order：39

- section：Experiment Two

- locator：Section 5.2 P2-P5

- move_code：RESULT

- paraphrase_cn：协作在簇4（LTE高严重）显著降本37%，在簇5（LTE低严重已知）显著增本55%，在簇2（LTE低严重未知）总成本不变但成本转移。

- rhetorical_function_cn：产出核心实证规律。

- depends_on_cn：分簇HLM。

- sets_up_cn：为推荐规则和验证研究提供具体标签。

- evidence_pointer：Section 5.2 Table 10

### 40. Section 5.3 Validation Study P1-S2

- order：40

- section：Experiment Two

- locator：Section 5.3 Validation Study P1-S2

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：为了验证聚类结果，我们在三个月内对184个需要PSG帮助的案例进行干预，强制部分工程师采用协作或交接，比较结果。

- rhetorical_function_cn：说明验证研究设计。

- depends_on_cn：聚类发现。

- sets_up_cn：提供因果证据。

- evidence_pointer：Section 5.3

### 41. Section 5.3 P4-P6

- order：41

- section：Experiment Two

- locator：Section 5.3 P4-P6

- move_code：RESULT

- paraphrase_cn：簇4型案例强制协作的工程师小时显著低于自选交接；簇5型案例强制交接显著低于自选协作，确认了聚类方向的因果作用。

- rhetorical_function_cn：报告验证结果。

- depends_on_cn：t检验。

- sets_up_cn：确定推荐规则可信。

- evidence_pointer：Section 5.3 Figures 4-5

### 42. Section 6 P1-S1

- order：42

- section：Experiment Three

- locator：Section 6 P1-S1

- move_code：RQ_OR_OBJECTIVE

- paraphrase_cn：实验三目标研究激励在成功协作中的作用，检查工程师是否遵循机器推荐，并探究偏离原因。

- rhetorical_function_cn：设定实验三研究问题。

- depends_on_cn：实验二已验证的推荐规则。

- sets_up_cn：部署推荐系统。

- evidence_pointer：Section 6 P1

### 43. Section 6.1 Compliance P1-S2

- order：43

- section：Experiment Three

- locator：Section 6.1 Compliance P1-S2

- move_code：RESULT

- paraphrase_cn：29周数据中正式交接推荐合规稳定在0.79，协作推荐合规较低0.7且方差高。

- rhetorical_function_cn：报告机器推荐应用中的基本发现。

- depends_on_cn：数据收集。

- sets_up_cn：引出原因调查。

- evidence_pointer：Section 6.1 Figures 6

### 44. Section 6.1 P3

- order：44

- section：Experiment Three

- locator：Section 6.1 P3

- move_code：MECHANISM

- paraphrase_cn：访谈揭示低协作合规由于CSG部门将协作视为对外部部门的依赖，缺乏自豪感；正式交接不视为依赖因为控制权保留在CSG。

- rhetorical_function_cn：揭示行为背后的心理机制。

- depends_on_cn：访谈和观察。

- sets_up_cn：为断点回归假设提供内容。

- evidence_pointer：Section 6.1 P3

### 45. Section 6.1 P5

- order：45

- section：Experiment Three

- locator：Section 6.1 P5

- move_code：HYPOTHESIS_OR_PROPOSITION

- paraphrase_cn：我们推测较低合规是部门激励与公司目标错位的体现；若上周协作比例过高，工程师本周会自我纠正减少协作。

- rhetorical_function_cn：提出可检验假设。

- depends_on_cn：目标函数错位逻辑。

- sets_up_cn：驱动断点回归。

- evidence_pointer：Section 6.1 P5

### 46. Section 6.2 Root Cause P1

- order：46

- section：Experiment Three

- locator：Section 6.2 Root Cause P1

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：我们模拟断点回归，用不同断点回归识别拐点，并选R2最高的点作为断点。

- rhetorical_function_cn：说明RD断点识别方法。

- depends_on_cn：图7显示拐点。

- sets_up_cn：正式估计效应。

- evidence_pointer：Section 6.2 P1

### 47. Section 6.2 Table 13

- order：47

- section：Experiment Three

- locator：Section 6.2 Table 13

- move_code：RESULT

- paraphrase_cn：回归结果显示上周协作比例越过断点时，本周合规下降0.371，支持自我纠正假设。

- rhetorical_function_cn：报告核心结果。

- depends_on_cn：RD回归。

- sets_up_cn：论证激励错位存在。

- evidence_pointer：Section 6.2 Table 13

### 48. Section 6.3 Incentive Correction P1-S2

- order：48

- section：Experiment Three

- locator：Section 6.3 Incentive Correction P1-S2

- move_code：DESIGN_FEATURE

- paraphrase_cn：为校正激励，我们改变工程师评价指标为平均总工时，并移除每周协作比例看板。

- rhetorical_function_cn：描述干预设计。

- depends_on_cn：根因分析。

- sets_up_cn：评价干预效果。

- evidence_pointer：Section 6.3

### 49. Section 6.3 P3-P4

- order：49

- section：Experiment Three

- locator：Section 6.3 P3-P4

- move_code：RESULT

- paraphrase_cn：校正后12周合规均值0.786，回归显示上周比例系数不显著，表明自我纠正消失。

- rhetorical_function_cn：报告干预验证结果。

- depends_on_cn：回归等式6。

- sets_up_cn：证明激励对齐效果。

- evidence_pointer：Section 6.3 Figure 9, Table 14

### 50. Section 7 P1 S1-S2

- order：50

- section：Discussion

- locator：Section 7 P1 S1-S2

- move_code：CONTRIBUTION

- paraphrase_cn：这篇论文是首次实验研究任务特征和激励对齐在协作问题解决中的作用，大型现场实验使我们观察到最粒度的任务和工程师行为。

- rhetorical_function_cn：放大研究独特性。

- depends_on_cn：全文证据。

- sets_up_cn：进入贡献性讨论。

- evidence_pointer：Section 7 P1

### 51. Section 7 P1 S3-S5

- order：51

- section：Discussion

- locator：Section 7 P1 S3-S5

- move_code：CONTRIBUTION

- paraphrase_cn：第一，我们精细认知任务特征如何影响协作结果；第二，我们指出推荐不合规和激励失谐的重要性；第三，我们增加人机协作的正面案例。

- rhetorical_function_cn：逐条列出三点贡献。

- depends_on_cn：前文分析。

- sets_up_cn：对应引言缺口。

- evidence_pointer：Section 7 P1 S3-S5

### 52. Section 7 P2 S1-S3

- order：52

- section：Discussion

- locator：Section 7 P2 S1-S3

- move_code：BOUNDARY_CONDITION

- paraphrase_cn：管理者应将正确任务分配给协作；LTE高严重此类任务最适协作，而低优先级已知问题则协作有害；不确定非紧急任务仅是工时转移。

- rhetorical_function_cn：将结果转化为可操作边界。

- depends_on_cn：实验二结果。

- sets_up_cn：说明实践边界。

- evidence_pointer：Section 7 P2

### 53. Section 7 P3 S1-S6

- order：53

- section：Discussion

- locator：Section 7 P3 S1-S6

- move_code：BOUNDARY_CONDITION

- paraphrase_cn：推荐干预应区分三种情境：人类有独特信息、人机知识重叠、机器有独特信息；只有后两种才值得干预。

- rhetorical_function_cn：提炼可泛化的人机干预原则。

- depends_on_cn：实验二/三发现。

- sets_up_cn：为未来系统设计提供框架。

- evidence_pointer：Section 7 P3

### 54. Section 7 P4

- order：54

- section：Discussion

- locator：Section 7 P4

- move_code：BOUNDARY_CONDITION

- paraphrase_cn：第三个实践意义是激励对齐，引入协作时需评估阻碍协作的现有激励，并可能需要改变个人文化。

- rhetorical_function_cn：强调激励对齐的一般性边界。

- depends_on_cn：实验三结果。

- sets_up_cn：导向结论。

- evidence_pointer：Section 7 P4

### 55. Section 8 P1 S1-S3

- order：55

- section：Conclusion

- locator：Section 8 P1 S1-S3

- move_code：CONTRIBUTION

- paraphrase_cn：我们通过三个现场实验发现适合跨职能团队的任务被有效筛选，并将任务特征纳入推荐系统后分析工程师不愿协作的根源，改变激励后展示协作益处。

- rhetorical_function_cn：概括研究旅程。

- depends_on_cn：所有实验。

- sets_up_cn：总结贡献。

- evidence_pointer：Section 8 P1

### 56. Section 8 P2 S1-S3

- order：56

- section：Conclusion

- locator：Section 8 P2 S1-S3

- move_code：CONTRIBUTION

- paraphrase_cn：我们填充了两个文献空白：成功协作还需任务分配正确，且即使任务和团队正确，若激励错位协作也会适得其反；我们展示了如何对齐激励。

- rhetorical_function_cn：逐点对应引言缺口。

- depends_on_cn：全文证据。

- sets_up_cn：形成闭环。

- evidence_pointer：Section 8 P2

### 57. Section 8 P3 S1-S3

- order：57

- section：Conclusion

- locator：Section 8 P3 S1-S3

- move_code：BOUNDARY_CONDITION

- paraphrase_cn：尽管目标在ICT行业，结果适用于更广泛的服务交付场景，如保修、客户关怀、项目管理和业务流程管理。

- rhetorical_function_cn：声明外推合理性。

- depends_on_cn：机制普遍性。

- sets_up_cn：为未来研究拓展。

- evidence_pointer：Section 8 P3

### 58. Section 8 P4 S1-S6

- order：58

- section：Conclusion

- locator：Section 8 P4 S1-S6

- move_code：LIMITATION_AND_FUTURE

- paraphrase_cn：研究限制：只关注生产力和成本；未考虑员工学习；现场为面授办公环境；未来可在远程工作和其他情境研究。

- rhetorical_function_cn：诚实承认边界和未来方向。

- depends_on_cn：研究设计。

- sets_up_cn：结束全文。

- evidence_pointer：Section 8 P4

## 写作技术

- gap_construction_cn：先从管理重要性和文献综述中凸显两个具体空白（任务特征、激励错位），并解释为什么数据不足造成了这些空白，然后用自己的现场数据优势填补。

- signposting_cn：在引言提前综述三个实验发现；各实验开头明确研究问题；使用“下一步”、“我们接下来”等过渡引导；摘要给出完整顺序。

- transition_logic_cn：实验一结果中的“功能案例转移”直接引发“什么任务适合协作”的问题；实验二聚类结果中的“某些簇显著”直接引出“强制推荐是否因果”的验证研究；实验二的验证结果直接支持“开发推荐系统”；实验三的合规失败直接引出“激励校正是解决方案”。

- claim_evidence_rhythm_cn：每个实验先提出研究问题，然后描述设计（随机化、模型），再给出基准对比结果，最后解释机制或来源，形成均匀的“主张-证据-解释”循环。

- benchmark_narrative_cn：正式交接作为主要基准反复出现；实验一对比传统过程，实验二对比交接决策，实验三以机器推荐作为遵循基准；通过逐层对比使“协作优于或不优于交接”的叙事随条件细化而丰富。

- theory_return_cn：讨论部分将实证发现纳入理论：任务特征与协作匹配扩展了Hackman/Daley；激励错位扩展了Bikard/Vakili；人机协作扩展了Fügener等。

- contribution_positioning_cn：贡献在引言和结论中以两点列出，并放置到现有文献的具体研究领域（协作问题解决、激励设计、人机协作），通过“首次”“重要贡献”等措辞加强地位。

- novelty_protection_cn：作者通过多实验三角设计、验证研究、断点回归和激励前后对比，将单一结果链接到机制和边界；并未声称协作普通有效，而是强调任务匹配和激励对齐，避免贡献退化为“协作有用”的一次性结果。

## 可复用研究与写作程序

### structure_steps

#### 1. 1

- step：1

- writing_job_cn：建立知识缺口：综述现有协作文献，指出任务特征和激励对齐未被研究。

- research_job_cn：找出组织情境中的两个具体问题，并确保有细粒度数据通道。

- required_evidence_cn：引用文献明确空白，并展示可获得的数据能支撑案例级分析。

- transition_to_next_cn：从缺口提出研究问题，导向现场实验设计。

#### 2. 2

- step：2

- writing_job_cn：设计实验一：整体价值评估，使用DID和来源分解。

- research_job_cn：在真实组织部署新流程（如协作选项），随机分配站点/单元，收集前后期数据。

- required_evidence_cn：平均处理效应显著，并能分解主要来源（功能转移而非交接替代）。

- transition_to_next_cn：用“成本降低来源不明确”引出任务特征分析。

#### 3. 3

- step：3

- writing_job_cn：实验二探索性分析：利用现有数据分层建模和聚类。

- research_job_cn：收集协变量和小时分解，建立工程师异质模型，按任务特征聚簇并估计异质性效应。

- required_evidence_cn：聚类间效应方向相反，表现为某些簇协作有正/负影响。

- transition_to_next_cn：用“因果性”疑问引出验证研究。

#### 4. 4

- step：4

- writing_job_cn：实验二验证：设计小规模干预实验，强制推荐反事实路径。

- research_job_cn：对关键簇案例进行随机干预，比较强制推荐与自选结果。

- required_evidence_cn：干预组显著优于自选基线，确认预测方向。

- transition_to_next_cn：用“已验证规则”过渡到系统实施。

#### 5. 5

- step：5

- writing_job_cn：实验三：部署推荐系统，观察人类遵循行为。

- research_job_cn：将规则编码为系统，现场运行并记录推荐和实际选择；收集访谈和情绪证据。

- required_evidence_cn：发现明显不合规模式，并有机制解释（如部门自豪感）。

- transition_to_next_cn：用“激励错位”导入校正步骤。

#### 6. 6

- step：6

- writing_job_cn：实验三激励校正：修改评价指标和控制信息展示，重复测量。

- research_job_cn：实施激励变换，收集后续周期数据，用回归验证原解释消失。

- required_evidence_cn：行为变化显著，旧回归系数不再显著。

- transition_to_next_cn：用“缺口闭合”进入讨论和贡献。

### most_transferable_moves_cn

1. 利用现场协作选项的自然变异构建DID

2. 用聚类和子样本揭示平均效应中的异质性

3. 在探索性发现后进行验证性干预以提升因果可信度

4. 部署系统后利用行为数据+访谈+断点回归识别机制

5. 通过改变激励和测量行为来验证机制解释

6. 讨论部分将具体结果提升为人机干预原则

### resource_intensive_or_nonstandard_parts_cn

1. 获得企业许可进行站点级随机化长期现场实验

2. 获取细粒度日志（工时、决策、推荐）

3. 实施干预（强制推荐）并允许后续调整

4. 访谈调动部门管理层参与

5. 实际修改公司激励制度并观察后续效果

### what_not_to_copy_superficially_cn

1. 若没有真实任务分类和细粒度工时，不能把LTE/严重度作为任务特征代理

2. 若未随机化或不控制工程师异质性，不能使用DID/HLM声称因果

3. 若没有断点回归设计，不能将合规下降归因于激励错位

4. 若没有激励改变后的后续观测，不能声称校正有效

- single_best_description_of_the_routine_cn：真实场景中介入协作选项，用现场数据识别任务特征，部署推荐系统，再用激励干预完善系统，形成从价值证明到机制到干预到验证的完整闭环。

## 分析边界

文章全文可读，但未提供在线附录具体内容，部分图表细节依赖OCR可能不完全准确；阶段划分和句子编号基于常识推断，在个别边界段落可能有错位；单篇文章解读为主观判断，但仍忠实于原文结构。
