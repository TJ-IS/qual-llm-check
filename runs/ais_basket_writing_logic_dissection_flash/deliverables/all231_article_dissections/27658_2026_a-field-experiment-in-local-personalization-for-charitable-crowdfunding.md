# A Field Experiment in Local Personalization for Charitable Crowdfunding

- 作者：Lauren Rhue; Atiya Avery; Jessica Clark
- 年份 / 期刊：2026 / MIS Quarterly
- DOI：10.25300/misq/2025/19044
- 源文件：27658_2026_a-field-experiment-in-local-personalization-for-charitable-crowdfunding.md
- 论文主类型：field_intervention_or_platform_experiment
- 主导写作弧线：phenomenon_mechanism_intervention_field_test
- 置信度：0.9

## 文章级论证概况

- 核心问题：在慈善众筹平台中，面向此前未支持本地项目的捐赠者，基于本地偏好的个性化推广能否比基于最近捐赠地点的默认个性化更有效地提升参与和捐赠，并产生何种分配公平后果？

- 制品与设计：以 DonorsChoose 为平台的邮件个性化推广：处理组使用账单所在地（本地个性化）推介项目，对照组使用最近捐赠学校所在地（默认个性化）；整个邮件主题、preheader、正文和落地页一致地指向该地点，其他内容保持恒定。

- 客观结果：开放率从27.7%升至28.2%，点击率从4.36%升至5.42%（+24%），捐赠率从0.209%升至0.285%（+36%）；有社会影响历史（经教师推荐链接首次捐赠）的捐赠者只提升点击率而不提升捐赠率；本地个性化使捐赠更集中在捐赠者所在高收入社区、高收入学校及人口统计相似地区。

- 核心贡献：通过大规模随机现场实验证明本地个性化能够激活潜在的本土偏好启发式，并揭示社会影响与本地偏好的层级关系、捐赠者可细分性，以及简单个性化策略可能加剧地理与教育资金不平等的问题。

- 整篇论证链：文章先指出慈善众筹平台有亲社会使命，但捐赠者自由选择导致善款分布未必符合社会需要；捐赠者依赖本土偏好和社会影响两类启发式，而既有文献分别研究、常假设二者一致，却很少比较冲突情境或用于平台个性化。作者由此提出三个研究问题：本地个性化对无本地捐赠历史的捐赠者是否有效、对社会影响型捐赠者是否不同、对长期分配公平有何影响。作者与 DonorsChoose 合作，把近16万名此前支持非本地项目的捐赠者随机分配到本地个性化邮件（账单所在地）或默认个性化邮件（最近捐赠地），利用开放、点击、捐赠、距离和推荐指标，依次用平衡检验、t检验、logistic回归、OLS、学校层面logistic和社区相似性分析，证明本地个性化总体上提升参与和捐赠，但社会影响历史会削弱从参与到捐赠的转换；本地个性化还使资金更集中到捐赠者自身高收入社区、高收入学校和人口相似地区，形成 rich-get-richer 效应。讨论部分把这些结果升华为启发式层级、捐赠者细分、个性化与社会公平的理论贡献，并提出轮换/组合个性化策略以平衡短期参与与长期使命。

## 类型与写作弧线判定

- 论文主类型判定：文章不是构建系统或离线benchmark，而是在真实慈善众筹平台DonorsChoose上对近16万真实捐赠者实施随机化邮件干预，记录真实行为结果；核心证据来自现场随机实验。

- 主导写作弧线判定：文章遵循：现象（慈善众筹中捐赠者的启发式使用与个性化推广）→机制（本土偏好与社会影响的比较与激活）→数字干预（本地个性化邮件）→现场因果检验（随机实验）→返回理论与社会公平含义。

## 研究开展程序

- study_or_phase_count：4

- 研究阶段总序列：阶段1验证随机化有效性；阶段2建立本地个性化对参与和捐赠的整体因果效应，并用距离交互排除‘与本地距离近’的替代解释；阶段3用推荐历史作为社会影响代理，检验异质性；阶段4从区域收入、学校收入、捐赠去向分布和社区相似性四个角度检验分配后果。四个阶段呈‘内部有效性→主效应→机制异质性→社会后果’的累积证据链。

### studies_or_phases

#### 1. 随机化与平衡性验证

- order：1

- name_cn：随机化与平衡性验证

- question_cn：本地个性化与默认个性化的随机分组是否成功，能否进行简单因果比较？

- inputs_and_setting_cn：DonorsChoose 2021年10月实验中的近160,000名此前支持非本地项目的捐赠者；匿名捐赠者ID、账单邮编、最近支持邮编、推荐指标、距离、邮编层面人口与收入数据。

- designed_or_compared_object_cn：处理组（本地个性化，账单所在地）与对照组（默认个性化，最近捐赠地）在预处理协变量上的分布比较。

- baseline_control_or_counterfactual_cn：对照组为平台当时的默认策略（最近捐赠地）；平衡检验比较两组协变量均值。

##### objective_metrics

（空）

- analysis_method_cn：t检验/均值平衡检验。

- main_result_cn：推荐率、距离、账单邮编收入、支持邮编收入、人口、BIPOC 80%+等变量均无显著差异，说明随机化有效。

- argumentative_role_cn：建立内部有效性，使后续简单t检验可被解读为因果效应。

- remaining_uncertainty_cn：平衡检验只说明可观测协变量平衡，不可观测动机差异仍可能存在。

- link_to_next_phase_cn：确认随机有效后，进入主效应分析。

##### evidence_pointers

1. Table 3

2. Randomization section

#### 2. 总体效应与距离交互（H1）

- order：2

- name_cn：总体效应与距离交互（H1）

- question_cn：对没有先前本地捐赠历史的非本地捐赠者，本地个性化是否提高开放、点击和捐赠率，且是否随捐赠者与之前捐赠地距离变化？

- inputs_and_setting_cn：同一现场实验中159,941名非本地捐赠者；开放、点击、捐赠行为变量，账单邮编与最近支持邮编之间的距离。

- designed_or_compared_object_cn：本地个性化邮件 vs 默认个性化邮件；本地个性化与距离的交互项。

- baseline_control_or_counterfactual_cn：对照组（默认个性化）；距离作为连续调节变量。

##### objective_metrics

1. open rate

2. click rate

3. donation rate

4. logistic regression coefficients

- analysis_method_cn：t检验比较条件均值；Logistic回归加入本地个性化、距离及交互项。

- main_result_cn：本地个性化显著提高开放率、点击率和捐赠率；距离主效应只在点击上显著，本地个性化×距离对点击和捐赠显著为正，说明对更远距离捐赠者的提升更大。

- argumentative_role_cn：证明本地个性化能在无先前本土偏好证据的捐赠者中激活本土偏好，支持H1a/H1b。

- remaining_uncertainty_cn：总体效应可能掩盖不同捐赠者类型的差异，尤其是有社会影响历史的捐赠者。

- link_to_next_phase_cn：由此转向社会影响历史的异质性检验。

##### evidence_pointers

1. Table 4

2. Table 5

3. Effects of Local Personalization on Engagement and Donations

#### 3. 社会影响历史的异质性（H2）

- order：3

- name_cn：社会影响历史的异质性（H2）

- question_cn：本地个性化的效果是否因捐赠者是否通过教师推荐链接获得首次捐赠而有差异？

- inputs_and_setting_cn：将样本分为推荐捐赠者（referred）与非推荐捐赠者（non-referred）；开放、点击、捐赠率按条件和子群分别统计。

- designed_or_compared_object_cn：推荐捐赠者 vs 非推荐捐赠者；每组内本地个性化 vs 默认个性化。

- baseline_control_or_counterfactual_cn：各组内的默认个性化；推荐与非推荐群体作为对照。

##### objective_metrics

1. open rate

2. click rate

3. donation rate

4. p-value

- analysis_method_cn：子群t检验。

- main_result_cn：推荐捐赠者中本地个性化只显著提高点击率，不显著改变开放率或捐赠率；非推荐捐赠者中开放、点击、捐赠均显著提高；推荐捐赠者在两种条件下整体响应率更低。

- argumentative_role_cn：支持H2a（参与提升普遍存在）和H2b（捐赠提升仅出现在无社会影响历史的捐赠者），暗示社会影响是比地理位置更强的捐赠线索。

- remaining_uncertainty_cn：推荐指标只是社会影响的代理，无法直接测量捐赠者决策时的社会关系强度；也未解释推荐捐赠者整体低响应率的原因。

- link_to_next_phase_cn：在证明参与和捐赠差异后，进一步追问这些资金流向哪里，检验分配后果。

##### evidence_pointers

1. Table 6

2. Heterogeneous Effects by Social Influence

#### 4. 分配后果与rich-get-richer效应（H3）

- order：4

- name_cn：分配后果与rich-get-richer效应（H3）

- question_cn：本地个性化是否导致捐赠更集中到富裕地区、高收入学校以及和捐赠者人口统计相似但并非邻近的地区？

- inputs_and_setting_cn：通过实验邮件实际捐赠的395名捐赠者；捐赠学校邮编、接受学校免费/减价午餐比例、邮编层面收入与人口结构、社区属性向量。

- designed_or_compared_object_cn：本地个性化 vs 默认个性化；加入本地收入、推荐状态及其交互。

- baseline_control_or_counterfactual_cn：默认个性化捐赠者的受赠地区收入、学校收入、捐赠去向分布和相似度。

##### objective_metrics

1. median household income of donation zip

2. probability of donating to high-income school

3. share of donations to local/recent/other area

4. cosine similarity

5. Euclidean distance

- analysis_method_cn：OLS回归（受赠邮编中位收入）、Logistic回归（高收入学校）、描述性分布、社区属性向量的余弦相似性与欧氏距离比较。

- main_result_cn：本地个性化显著提高受赠地区中位收入，且与捐赠者本地收入交互显著；本地个性化使捐赠到高收入学校的概率提高67%-96%；本地个性化条件下41%的捐赠流向捐赠者本地社区，而对照组为22%；即使流向‘其他’地区，捐赠对象也与实验条件下所属社区属性显著更相似。

- argumentative_role_cn：支持H3，证明本地个性化在提高短期参与的同时强化了地理与教育资金的不平等。

- remaining_uncertainty_cn：没有直接检验缓解策略；没有测算对长期福利的净效应；‘相似性’不代表实际因果机制。

- link_to_next_phase_cn：结果进入讨论，把分配后果上升为理论贡献与平台设计启示。

##### evidence_pointers

1. Table 7

2. Table 8

3. Table 9

4. Table 10

5. Figure 2

## 各部分修辞架构

### abstract_moves

1. CONTEXT: 慈善众筹平台通过个性化推广驱动捐赠，并依赖本土偏好与社会影响等启发式。

2. LIMITATION: 两种启发式可能不一致，既有文献对二者如何交互缺乏洞见。

3. RQ_OR_OBJECTIVE: 用近16万捐赠者的随机现场实验填补这一缺口。

4. DESIGN_FEATURE: 实验对比本地个性化（账单所在地）与默认个性化（最近支持社区）。

5. RESULT: 本地个性化总体提高参与和捐赠，即使无先前本土偏好证据。

6. RESULT: 有社会影响历史的捐赠者只提升参与不提升捐赠。

7. RESULT: 本地个性化使资金流向富裕且人口统计相似的社区，形成富者愈富。

8. CONTRIBUTION: 强调简单个性化策略的行为力量与公平风险。

### introduction_moves

1. CONTEXT: 慈善众筹平台快速增长，具有亲社会使命。

2. PHENOMENON: 捐赠者自由选择导致个体偏好与社会需要错位。

3. PRIOR_KNOWLEDGE: 捐赠者依赖本土偏好与社会影响两种启发式。

4. GAP: 两种启发式如何比较和交互尚不清楚。

5. WHY_GAP_MATTERS: 平台需决定个性化策略，但无历史线索时无法判断哪种策略更有效。

6. RQ_OR_OBJECTIVE: 提出三个研究问题。

7. STUDY_OVERVIEW: 介绍与DonorsChoose合作的大规模随机实验。

8. RESULT: 预告本地个性化提升参与但存在异质性与公平代价。

9. CONTRIBUTION: 声明对IS、众筹、个性化文献的贡献。

10. TRANSITION: 给出全文路线图。

### theory_and_knowledge_moves

1. PRIOR_KNOWLEDGE: 众筹捐赠者面对信息过载，依赖System 1启发式。

2. THEORY_PROPOSITION: 本土偏好与社会影响分别提供熟悉、信任等决策捷径。

3. LIMITATION: 既有研究孤立分析两种启发式，缺乏竞争线索下的比较。

4. GAP: 个性化是否能主动激活未表现出来的本土偏好尚未检验。

5. PRACTICAL_STAKES: 基于地理的个性化可能加剧既有地理不平等。

### artifact_design_moves

1. STUDY_OVERVIEW: 平台已有邮件个性化基础设施，作者利用该基础设施开展随机实验。

2. DESIGN_FEATURE: 处理组邮件突出账单所在地项目，对照组突出最近捐赠地项目。

3. METHOD_JUSTIFICATION: 只保留账单邮编与最近支持邮编不同的非本地捐赠者，以隔离本地个性化效应。

4. DESIGN_FEATURE: 所有内容除地点外保持一致，确保依从。

5. METHOD_JUSTIFICATION: 用推荐指标作为社会影响代理，用距离作为本土偏好代理。

### evaluation_moves

1. ROBUSTNESS_OR_BOUNDARY_TEST: 随机化平衡检验证明两组可比较。

2. METHOD_JUSTIFICATION: 随机化且参与者不知情，因此用简单t检验即可识别因果效应。

3. BENCHMARK_OR_CONTRAST: 平台默认策略作为控制基准。

4. RESULT: 主效应表显示开放、点击、捐赠率显著提高。

5. RESULT: 距离交互显示对更远捐赠者提升更大。

6. RESULT: 推荐历史异质性显示只有无推荐历史的捐赠者发生捐赠转换。

7. RESULT: 收入、学校、去向分布和相似性四类证据共同支持rich-get-richer。

### discussion_and_contribution_moves

1. TRANSITION: 从结果回到三个研究问题。

2. CONTRIBUTION: 提出启发式层级：社会影响强于地理邻近。

3. CONTRIBUTION: 个性化与平台公平研究；最小个性化也能改变社会资源配置。

4. CONTRIBUTION: 静态地理位置可超越基于行为历史的个性化。

5. CONTRIBUTION: 平台可轮换或组合多种个性化策略以平衡公平。

6. LIMITATION_AND_FUTURE: 行为推断、聚合数据、未检验缓解策略。

7. CONTRIBUTION: 平台设计同时承担技术责任与道德责任。

## 理论/知识到设计的翻译

### 知识/理论基础

1. 双过程理论/System 1启发式

2. 本土偏好（home bias）

3. 社会影响（social influence）

4. 同质性（homophily）

5. 显示偏好逻辑（revealed preference）

6. 马太效应/富者愈富

- 理论—设计耦合：direct

- 耦合判定理由：作者从本土偏好和社会影响理论直接推导实验处理（本地个性化 vs 默认个性化）、调节变量（距离）、异质性分组（推荐历史）以及后果变量（捐赠地区收入、学校收入、社区相似性），并用随机实验直接检验这些理论命题。

- 理论到设计翻译链：本土偏好理论表明地理位置能通过熟悉、义务和信任触发捐赠 → 设计出‘账单所在地项目’的本地个性化邮件 → 与平台默认的‘最近捐赠地项目’邮件对比 → 检验开放、点击和捐赠率。社会影响理论表明捐赠者依赖推荐者的信任而非项目地理位置 → 用首次捐赠是否来自教师推荐区分捐赠者 → 检验参与和捐赠的转换差异。同质性与马太效应表明捐赠者偏好相似/富裕社区 → 在本地个性化条件下测量受赠地区收入、学校收入和社区向量相似性 → 支持富者愈富的分配后果。

### mapping_table

#### 1. 1

- theory_or_knowledge_claim_cn：捐赠者面对大量项目时会使用启发式；本土偏好使捐赠倾向于本地项目。

- mechanism_cn：地理位置唤起对社区的情感认同、义务感和信任，降低决策复杂度。

- design_requirement_cn：个性化邮件应突出与捐赠者地理位置相关的项目。

- artifact_choice_cn：处理组邮件使用账单邮编推荐当地项目。

- evaluated_contrast_cn：本地个性化 vs 默认个性化（最近捐赠地）。

- objective_result_cn：开放率、点击率、捐赠率均显著提升。

##### evidence_pointers

1. Table 4

#### 2. 2

- theory_or_knowledge_claim_cn：显示偏好假设过去捐赠预测未来偏好，但该假设在临时社会影响和平台约束下可能失效。

- mechanism_cn：过去选择不一定反映稳定偏好，可能受推荐关系或本地项目供给不足影响。

- design_requirement_cn：使用静态地理位置而非仅依据行为历史进行个性化。

- artifact_choice_cn：本地个性化使用账单邮编而非最近捐赠邮编。

- evaluated_contrast_cn：与平台默认的基于最近捐赠地的行为个性化对比。

- objective_result_cn：本地个性化在无本地捐赠历史的非本地捐赠者中仍然提高参与和捐赠。

##### evidence_pointers

1. Table 4

2. Table 5

#### 3. 3

- theory_or_knowledge_claim_cn：社会影响是独立启发式，捐赠者因信任推荐者而捐赠，不依赖项目位置。

- mechanism_cn：推荐关系提供信任信号，使地理位置线索对捐赠决策不够充分。

- design_requirement_cn：区分社会影响型捐赠者，预期其参与提升但捐赠转换有限。

- artifact_choice_cn：用首次捐赠是否来自教师推荐链接识别社会影响历史。

- evaluated_contrast_cn：推荐捐赠者 vs 非推荐捐赠者；每组内本地 vs 默认个性化。

- objective_result_cn：推荐捐赠者只显著提升点击率，非推荐捐赠者提升开放、点击和捐赠率。

##### evidence_pointers

1. Table 6

#### 4. 4

- theory_or_knowledge_claim_cn：同质性使捐赠者支持与自己社区相似的地区；马太效应使已有资源更多者获得更多。

- mechanism_cn：本土偏好把资金导向捐赠者所在的高收入社区，同质性则扩展到人口统计相似的地区。

- design_requirement_cn：本地个性化可能产生分配后果，需要检验受赠地区收入与学校特征。

- artifact_choice_cn：本地个性化邮件和落地页突出本地项目。

- evaluated_contrast_cn：本地个性化 vs 默认个性化的捐赠目的地收入、学校收入、地理分布。

- objective_result_cn：本地个性化显著提高受赠地区中位收入、捐赠到高收入学校的概率、本地社区捐赠比例。

##### evidence_pointers

1. Table 7

2. Table 8

3. Table 9

#### 5. 5

- theory_or_knowledge_claim_cn：同质性可通过社区属性相似性在非邻近地区中延续。

- mechanism_cn：本地个性化不止激活地理邻近，还激活与捐赠者社区相似的人口经济特征偏好。

- design_requirement_cn：除直接本地捐赠外，还需检验‘其他地区’捐赠是否与账单社区相似。

- artifact_choice_cn：用账单邮编、最近支持邮编和捐赠邮编构造社区属性向量。

- evaluated_contrast_cn：捐赠地区与账单地区/最近支持地区的余弦相似性和欧氏距离。

- objective_result_cn：捐赠去向与实验条件指向的地区在属性上显著更相似，且‘其他地区’子集也成立。

##### evidence_pointers

1. Table 10

## 评价逻辑

### evaluation_modes

1. 大规模随机现场实验

2. 随机化平衡检验

3. t检验

4. Logistic回归（距离交互）

5. 子群分析（推荐 vs 非推荐）

6. OLS回归（受赠地区收入）

7. Logistic回归（高收入学校）

8. 描述性捐赠去向分布

9. 社区属性向量的余弦相似性与欧氏距离比较

- why_these_evaluations_cn：平衡检验保障因果推断；t检验直接回答总体因果效果，因为随机化和捐赠者不知情消除了主要内生性；距离交互用于确认‘未表现本土偏好’并非因为实际地理距离近；推荐子群检验解释社会影响与本土偏好的交互；最后的收入、学校和相似性分析把短期行为效果扩展到长期分配后果。

- benchmark_and_contrast_chain_cn：主要benchmark是平台当时默认的‘最近捐赠地’个性化，它构成行为个性化基线；进一步以距离分层检验‘接近本地’的替代解释；以推荐历史作为社会影响对比；以‘高收入学校’与‘其他地区相似性’作为分配公平的额外对照。整个链条从单一总体均值差逐步细化到机制和边界。

### claim_evidence_ledger

#### 1. 本地个性化总体提高开放、点击和捐赠率。

- claim_cn：本地个性化总体提高开放、点击和捐赠率。

- evidence_cn：Table 4条件均值t检验：开放p<0.05，点击和捐赠p<0.001。

- support_level：强

#### 2. 本地个性化对更远距离的非本地捐赠者提升更大。

- claim_cn：本地个性化对更远距离的非本地捐赠者提升更大。

- evidence_cn：Table 5交互项：本地个性化×距离对点击和捐赠显著为正。

- support_level：中

#### 3. 本地个性化对无社会影响历史者提升捐赠，对有社会影响历史者只提升参与。

- claim_cn：本地个性化对无社会影响历史者提升捐赠，对有社会影响历史者只提升参与。

- evidence_cn：Table 6：非推荐者开放/点击/捐赠显著；推荐者仅点击显著，捐赠不显著。

- support_level：中

#### 4. 本地个性化导致资金流向更富裕地区和更高收入学校。

- claim_cn：本地个性化导致资金流向更富裕地区和更高收入学校。

- evidence_cn：Table 7 OLS受赠邮编中位收入显著提升；Table 8高收入学校概率显著提升67%-96%。

- support_level：中

#### 5. 本地个性化使捐赠流向本地和人口统计相似社区。

- claim_cn：本地个性化使捐赠流向本地和人口统计相似社区。

- evidence_cn：Table 9本地捐赠比例41% vs 22%；Table 10相似性指标显著指向实验条件地区，包括‘其他地区’子集。

- support_level：中

- internal_validity_strategy_cn：随机分配保证处理与对照在可观测协变量上平衡；捐赠者不知情减少期望偏差；所有邮件内容除位置外保持一致；分析只用随机分配变量进行意向处理式比较；结果在邮件打开前后均一致体现了处理位置，减少依从问题。

- external_validity_strategy_cn：真实慈善众筹平台、近16万捐赠者、真实邮件渠道和真实捐赠行为；基线与行业邮件营销基准比较；使用多个层级和多个结果变量以增加稳健性；讨论中谨慎限定于DonorsChoose和非本地捐赠者子样本。

- what_is_not_actually_tested_cn：未直接测量捐赠者认知过程或自报动机；‘社会影响历史’只是首次捐赠是否来自教师推荐链接的代理；未检验长期动态或算法个性化版本；未检验缓解策略；无法在个体层面按种族、年龄等人口特征分析；‘rich-get-richer’的社会福利净效应未直接测算。

## 贡献闭环

- technical_claim_cn：在DonorsChoose环境中，本地个性化邮件相对于平台默认的最近捐赠地邮件显著提高了开放率、点击率和捐赠率，且对点击和捐赠的提升在越远离之前捐赠地的捐赠者中越明显。

- artifact_claim_cn：邮件中一致呈现的账单所在地项目（而非最近捐赠地项目）是效果来源，因为两组除位置外内容完全一致。

- mechanism_claim_cn：本地个性化激活了潜在的本土偏好启发式，通过熟悉、义务和信任增加参与；但当捐赠者有社会影响历史时，推荐关系驱动的信任更强，因此参与提升没有转化为捐赠。

- boundary_claim_cn：效果出现在此前支持非本地项目的捐赠者中；有社会影响历史的捐赠者只提升点击不提升捐赠；捐赠流向更集中在富裕和高收入学校地区；结论受DonorsChoose、2021年10月、邮件渠道和一周观测窗口限制。

- reusable_design_knowledge_cn：静态地理位置属性可以超越基于行为历史的个性化；平台应参考捐赠者是否依赖社会影响来细分受众；应通过轮换或组合地理、社会、文化相似性等策略减少单一启发式引发的分配不公。

- theoretical_contribution_cn：为本土偏好与社会影响的比较提供因果证据，提出启发式层级（社会影响强于地理邻近）；把个性化研究延伸到分配公平，表明简单个性化也能触发马太效应和同质性驱动的资源配置。

- how_discussion_closes_intro_gap_cn：讨论直接回到三个研究问题：本地个性化对无本地历史的捐赠者有效；社会影响历史改变从参与到捐赠的转换；分配后果揭示短期参与与长期使命之间的张力，从而回应引言中‘启发式未对齐’和‘平台应如何个性化’的缺口。

- overclaim_or_unsupported_leaps_cn：从行为结果推断‘潜在启发式激活’具有一定跳跃，因为没有认知测量；用首次捐赠推荐链接代表社会影响较粗；‘社会影响强于地理邻近’是基于推荐群体中捐赠转换缺失的间接推断，并非直接比较同一个人面对两种提示的决策；rich-get-richer的公平性判断依赖于收入/学校代理，未直接测算社会总福利。

## 句级写作动作图谱

### 1. P1 S1

- order：1

- section：Abstract

- locator：P1 S1

- move_code：CONTEXT

- paraphrase_cn：慈善众筹平台使用个性化推广来吸引捐赠者并增加捐款，通常利用本土偏好和社会影响等认知启发式。

- rhetorical_function_cn：开篇点出研究对象和关键机制，让读者进入具体平台行为情境。

- depends_on_cn：无。

- sets_up_cn：为后文‘二者可能冲突’的缺口做铺垫。

- evidence_pointer：Abstract P1

### 2. P1 S2

- order：2

- section：Abstract

- locator：P1 S2

- move_code：LIMITATION

- paraphrase_cn：两种启发式都能影响捐赠，但未必一致，既有文献对它们如何交互或谁主导缺乏洞见。

- rhetorical_function_cn：在摘要中快速制造研究缺口。

- depends_on_cn：依赖前句对两类启发式的引入。

- sets_up_cn：引出本文的目的和实验设计。

- evidence_pointer：Abstract P1

### 3. P2 S1

- order：3

- section：Abstract

- locator：P2 S1

- move_code：RQ_OR_OBJECTIVE

- paraphrase_cn：作者通过一个近16万捐赠者的随机现场实验来回答该缺口。

- rhetorical_function_cn：宣布方法和规模，强化可信度。

- depends_on_cn：缺口确立后，自然转向解决方案。

- sets_up_cn：引出实验条件和主要结果。

- evidence_pointer：Abstract P2

### 4. P2 S2

- order：4

- section：Abstract

- locator：P2 S2

- move_code：DESIGN_FEATURE

- paraphrase_cn：此前支持非本地项目的捐赠者被随机分配到本地个性化邮件或默认个性化邮件。

- rhetorical_function_cn：说明实验干预的具体构造。

- depends_on_cn：研究目标需要两组对比。

- sets_up_cn：后文结果按这两组比较。

- evidence_pointer：Abstract P2

### 5. P3 S1

- order：5

- section：Abstract

- locator：P3 S1

- move_code：RESULT

- paraphrase_cn：本地个性化总体提高了参与和捐赠，即使捐赠者没有先前本土偏好证据。

- rhetorical_function_cn：给出核心正面发现。

- depends_on_cn：实验设计建立后报告结果。

- sets_up_cn：与下一句的异质性结果形成对比。

- evidence_pointer：Abstract P3

### 6. P3 S2

- order：6

- section：Abstract

- locator：P3 S2

- move_code：RESULT

- paraphrase_cn：有社会影响历史的捐赠者在本地个性化下参与提高但捐赠可能性未提高。

- rhetorical_function_cn：报告关键调节效应。

- depends_on_cn：总体效应已经给出；现在细分。

- sets_up_cn：为理论上的启发式层级和捐赠者细分做铺垫。

- evidence_pointer：Abstract P3

### 7. P3 S3

- order：7

- section：Abstract

- locator：P3 S3

- move_code：RESULT

- paraphrase_cn：本地个性化把资金不成比例地引向富裕且与捐赠者人口统计相似的社区，强化富者愈富。

- rhetorical_function_cn：报告分配后果。

- depends_on_cn：前面结果说明行为变化；现在转向资源配置。

- sets_up_cn：支撑文末关于公平风险的贡献。

- evidence_pointer：Abstract P3

### 8. P4 S1

- order：8

- section：Abstract

- locator：P4 S1

- move_code：CONTRIBUTION

- paraphrase_cn：这些发现凸显简单个性化策略的行为力量与公平风险，对平台设计和启发式负责任使用具有启示。

- rhetorical_function_cn：收束摘要，定位贡献。

- depends_on_cn：所有结果已呈现。

- sets_up_cn：无需再铺垫，直接进入正文。

- evidence_pointer：Abstract P4

### 9. P1 S1

- order：9

- section：Introduction

- locator：P1 S1

- move_code：CONTEXT

- paraphrase_cn：慈善众筹平台允许个人直接支持解决教育、健康或灾害等社会需求的项目，并已大幅增长。

- rhetorical_function_cn：建立研究领域的重要性。

- depends_on_cn：无。

- sets_up_cn：为‘使命与捐赠模式冲突’提供背景。

- evidence_pointer：Introduction P1

### 10. P2 S1

- order：10

- section：Introduction

- locator：P2 S1

- move_code：PHENOMENON

- paraphrase_cn：因为捐赠者自行决定资金去向，平台的亲社会使命可能与实际捐赠分布不一致。

- rhetorical_function_cn：提出一个值得研究的平台现象。

- depends_on_cn：需要平台快速增长且捐赠者自由选择这一背景。

- sets_up_cn：引出捐赠者依赖启发式的解释。

- evidence_pointer：Introduction P2

### 11. P3 S1

- order：11

- section：Introduction

- locator：P3 S1

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：捐赠者经常依赖两类启发式：本土偏好和社会影响，二者分别通过地理亲近和社交推荐简化决策。

- rhetorical_function_cn：引入核心理论概念。

- depends_on_cn：平台复杂性导致认知局限，需要启发式。

- sets_up_cn：随后指出这两类启发式未被充分比较。

- evidence_pointer：Introduction P3

### 12. P3 S4

- order：12

- section：Introduction

- locator：P3 S4

- move_code：GAP

- paraphrase_cn：哪种启发式更能推动参与和捐赠，尤其在它们指向不同选择或捐赠者过去没有明显使用痕迹时，仍不清楚。

- rhetorical_function_cn：把已有知识收缩成明确缺口。

- depends_on_cn：需要前句对两类启发式的定义。

- sets_up_cn：说明平台个性化需要回答的问题。

- evidence_pointer：Introduction P3

### 13. P4 S1

- order：13

- section：Introduction

- locator：P4 S1

- move_code：WHY_GAP_MATTERS

- paraphrase_cn：这个缺口对平台优化捐赠者推广非常重要，因为平台不知道在没有历史线索时应采用哪种策略，也可能面临富者愈富风险。

- rhetorical_function_cn：证明缺口不只是理论兴趣，而是实践决策问题。

- depends_on_cn：前文已说明启发式可被平台个性化利用。

- sets_up_cn：引出三个具体研究问题。

- evidence_pointer：Introduction P4

### 14. P5 S1

- order：14

- section：Introduction

- locator：P5 S1

- move_code：RQ_OR_OBJECTIVE

- paraphrase_cn：作者提出三个问题：本地个性化对无本地捐赠历史的捐赠者是否有效；对社会影响型捐赠者是否不同；对捐赠模式和长期使命有何影响。

- rhetorical_function_cn：给出研究问题清单，使论文结构清晰。

- depends_on_cn：缺口的实践意义已建立。

- sets_up_cn：后文实验和研究设计直接对应这三个问题。

- evidence_pointer：Introduction P5

### 15. P5 S4

- order：15

- section：Introduction

- locator：P5 S4

- move_code：STUDY_OVERVIEW

- paraphrase_cn：作者与DonorsChoose合作，对近16万此前支持非本地项目的捐赠者随机发送基于居住地或之前捐赠地的个性化邮件。

- rhetorical_function_cn：预告实验设计。

- depends_on_cn：研究问题需要随机对照。

- sets_up_cn：为结果和贡献的呈现提供框架。

- evidence_pointer：Introduction P5

### 16. P6 S1

- order：16

- section：Introduction

- locator：P6 S1

- move_code：RESULT

- paraphrase_cn：本地个性化显著提升参与和捐赠率，但对有社会影响历史的捐赠者效果较弱，并使资金集中在更富裕地区。

- rhetorical_function_cn：提前告知核心发现。

- depends_on_cn：实验概述后给出结果摘要。

- sets_up_cn：为贡献声明提供依据。

- evidence_pointer：Introduction P6

### 17. P7 S1

- order：17

- section：Introduction

- locator：P7 S1

- move_code：CONTRIBUTION

- paraphrase_cn：本文为数字平台、慈善众筹和个性化文献提供新见解：本土偏好可被激活，社会影响调节其效果，并可能加剧地理资金差距。

- rhetorical_function_cn：声明文献贡献。

- depends_on_cn：结果摘要已给出。

- sets_up_cn：说明论文在IS领域的位置。

- evidence_pointer：Introduction P7

### 18. P8 S1

- order：18

- section：Introduction

- locator：P8 S1

- move_code：TRANSITION

- paraphrase_cn：下一节介绍理论背景，随后依次是数据、实证分析和结果，最后是讨论与局限。

- rhetorical_function_cn：提供全文路线图。

- depends_on_cn：引言已完成问题与贡献陈述。

- sets_up_cn：引导读者进入相关文献。

- evidence_pointer：Introduction P8

### 19. P1 S1

- order：19

- section：Related Literature

- locator：P1 S1

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：慈善众筹平台以亲社会为目标，捐赠者不追求财务回报，而从给予中获得非经济价值。

- rhetorical_function_cn：界定慈善众筹不同于商业众筹的关键特征。

- depends_on_cn：引言已把平台作为背景。

- sets_up_cn：为启发式在捐赠决策中的作用做铺垫。

- evidence_pointer：Related Literature P1

### 20. P2 S1

- order：20

- section：Related Literature

- locator：P2 S1

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：捐赠者评估项目时依据更新数、目标、语言、情绪、图像等多维属性，但信息过载使系统评价不可行。

- rhetorical_function_cn：说明捐赠决策的复杂性来源。

- depends_on_cn：慈善众筹的捐赠者自主选择。

- sets_up_cn：引出启发式作为简化机制。

- evidence_pointer：Related Literature P2

### 21. P3 S1

- order：21

- section：Related Literature

- locator：P3 S1

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：启发式源于双过程理论，本土偏好和社会影响分别通过社区认同和信任线索减少评估负担。

- rhetorical_function_cn：正式引入理论基础。

- depends_on_cn：需要说明信息过载背景。

- sets_up_cn：为后文假设提供概念定义。

- evidence_pointer：Related Literature P3

### 22. P4 S3

- order：22

- section：Related Literature

- locator：P4 S3

- move_code：LIMITATION

- paraphrase_cn：过去研究分别证明两种启发式的作用，但很少研究它们如何交互，尤其是当它们提供竞争性线索时。

- rhetorical_function_cn：指出现有文献空白。

- depends_on_cn：两种启发式定义已建立。

- sets_up_cn：为本文比较二者提供理论动机。

- evidence_pointer：Related Literature P4

### 23. P5 S1

- order：23

- section：Related Literature

- locator：P5 S1

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：个性化指根据行为或人口数据定制内容，已被证明能增加注意和参与，尤其在与用户偏好或身份一致时。

- rhetorical_function_cn：引入个性化文献。

- depends_on_cn：已说明捐赠者依赖启发式。

- sets_up_cn：质疑个性化是否必须建立在过往行为基础上。

- evidence_pointer：Related Literature P5

### 24. P5 S3

- order：24

- section：Related Literature

- locator：P5 S3

- move_code：GAP

- paraphrase_cn：尚不清楚基于本土偏好的个性化是否对没有先前本土偏好的捐赠者仍然有效。

- rhetorical_function_cn：把个性化文献缺口具体化。

- depends_on_cn：需要个性化增加参与的已有证据。

- sets_up_cn：为H1a/H1b铺垫。

- evidence_pointer：Related Literature P5

### 25. P6 S1

- order：25

- section：Related Literature

- locator：P6 S1

- move_code：PRACTICAL_STAKES

- paraphrase_cn：个性化可能带来意外后果，因为富区捐赠者捐赠更多，地理位置导向的个性化可能加剧地理不公平。

- rhetorical_function_cn：引入公平风险。

- depends_on_cn：需要平台个性化广泛存在且捐赠者有地域特征。

- sets_up_cn：为H3和分配后果分析做铺垫。

- evidence_pointer：Related Literature P6

### 26. P7 S1

- order：26

- section：Related Literature

- locator：P7 S1

- move_code：GAP

- paraphrase_cn：现有研究孤立分析启发式、多用观测数据、很少关注平台推广策略，因此缺乏对启发式交互、策略激活和公平影响的系统性理解。

- rhetorical_function_cn：总结并放大研究缺口。

- depends_on_cn：前几节分别讨论启发式与个性化。

- sets_up_cn：为假设发展提供整体动机。

- evidence_pointer：Related Literature P7

### 27. P1 S1

- order：27

- section：Hypothesis Development

- locator：P1 S1

- move_code：LIMITATION

- paraphrase_cn：过去的捐赠可能不反映稳定偏好，而受临时情境、平台设计或社会影响塑造。

- rhetorical_function_cn：质疑显示偏好逻辑。

- depends_on_cn：个性化文献中的行为定向假设。

- sets_up_cn：引出本地个性化可能触发新启发式的假设。

- evidence_pointer：Hypothesis Development P1

### 28. Local Personalization P1 S2

- order：28

- section：Hypothesis Development

- locator：Local Personalization P1 S2

- move_code：MECHANISM

- paraphrase_cn：显示偏好假设不总是成立，过去非本地捐赠可能是临时的社会连接或平台本地项目供给不足所致。

- rhetorical_function_cn：解释为什么行为个性化可能失败。

- depends_on_cn：显示偏好文献。

- sets_up_cn：支持本地个性化激活潜在本土偏好的逻辑。

- evidence_pointer：H1 development

### 29. Local Personalization P2 S1

- order：29

- section：Hypothesis Development

- locator：Local Personalization P2 S1

- move_code：MECHANISM

- paraphrase_cn：本地个性化可通过情感认同、邻里义务或道德责任感激活本土偏好启发式，因此提高参与和捐赠。

- rhetorical_function_cn：给出主效应的心理机制。

- depends_on_cn：需要本土偏好定义。

- sets_up_cn：推导H1a/H1b。

- evidence_pointer：H1 development

### 30. H1a/H1b

- order：30

- section：Hypothesis Development

- locator：H1a/H1b

- move_code：HYPOTHESIS_OR_PROPOSITION

- paraphrase_cn：假设本地个性化提高此前支持非本地项目捐赠者的参与度（H1a）和捐赠可能性（H1b）。

- rhetorical_function_cn：将机制转化为可检验假设。

- depends_on_cn：前文机制推导。

- sets_up_cn：实验主效应分析检验此假设。

- evidence_pointer：H1a/H1b

### 31. Social Influence P1 S1

- order：31

- section：Hypothesis Development

- locator：Social Influence P1 S1

- move_code：MECHANISM

- paraphrase_cn：社会影响是独立启发式，核心是捐赠者与推荐者的关系，而非项目位置；当数字网络跨越地理边界时，社会影响与本土偏好常不一致。

- rhetorical_function_cn：解释为何社会影响型捐赠者可能不受地理线索驱动。

- depends_on_cn：需要社会影响定义。

- sets_up_cn：推导H2a/H2b。

- evidence_pointer：H2 development

### 32. H2a/H2b

- order：32

- section：Hypothesis Development

- locator：H2a/H2b

- move_code：HYPOTHESIS_OR_PROPOSITION

- paraphrase_cn：假设本地个性化提高所有非本地捐赠者的参与（H2a），但捐赠可能性的提升仅发生在没有先前社会影响证据的捐赠者中（H2b）。

- rhetorical_function_cn：将异质性社会影响机制转化为假设。

- depends_on_cn：社会影响机制推导。

- sets_up_cn：子群分析检验这一差异。

- evidence_pointer：H2a/H2b

### 33. Consequences P1 S1

- order：33

- section：Hypothesis Development

- locator：Consequences P1 S1

- move_code：PRACTICAL_STAKES

- paraphrase_cn：本地个性化虽能提高参与，但捐赠者多来自富裕地区，激活本土偏好可能把资金集中到已受惠社区，与平台使命冲突。

- rhetorical_function_cn：提出道德与实践后果。

- depends_on_cn：已有研究表明富裕者捐赠更多。

- sets_up_cn：引向马太效应和H3。

- evidence_pointer：H3 development

### 34. H3

- order：34

- section：Hypothesis Development

- locator：H3

- move_code：HYPOTHESIS_OR_PROPOSITION

- paraphrase_cn：假设本地个性化导致富者愈富，把捐赠集中到更富裕地区。

- rhetorical_function_cn：把分配后果形式化。

- depends_on_cn：马太效应和捐赠者富裕特征。

- sets_up_cn：后续收入、学校和相似性分析。

- evidence_pointer：H3

### 35. Study Context P1 S1

- order：35

- section：Experiment

- locator：Study Context P1 S1

- move_code：CONTEXT

- paraphrase_cn：DonorsChoose是帮助美国公立学校教师筹资的慈善众筹平台，已筹集超15亿美元，覆盖多数公立学校。

- rhetorical_function_cn：介绍实验现场。

- depends_on_cn：研究问题需要合适的实地平台。

- sets_up_cn：让实验设计有具体背景。

- evidence_pointer：Study Context

### 36. Experimental Design P1 S1

- order：36

- section：Experiment

- locator：Experimental Design P1 S1

- move_code：STUDY_OVERVIEW

- paraphrase_cn：作者利用平台现有邮件个性化基础设施，于2021年10月对近16万此前捐赠者实施大规模随机现场实验。

- rhetorical_function_cn：说明实验总体安排。

- depends_on_cn：平台背景已介绍。

- sets_up_cn：随后说明条件定义和样本选择。

- evidence_pointer：Experimental Design

### 37. Experimental Design P2 S1

- order：37

- section：Experiment

- locator：Experimental Design P2 S1

- move_code：DESIGN_FEATURE

- paraphrase_cn：处理组邮件突出账单邮编周边项目，对照组突出最近支持项目的学校邮编周边项目；地点信息在主题、预header、正文和落地页保持一致。

- rhetorical_function_cn：定义实验干预物。

- depends_on_cn：需要平台邮件基础设施。

- sets_up_cn：使随后结果可归因于本地位置线索。

- evidence_pointer：Table 1

### 38. Experimental Design P3 S1

- order：38

- section：Experiment

- locator：Experimental Design P3 S1

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：主分析只保留账单邮编与最近支持邮编不同的捐赠者，以隔离本地个性化对非本地捐赠者的效应。

- rhetorical_function_cn：说明样本筛选逻辑。

- depends_on_cn：研究问题聚焦无本地历史捐赠者。

- sets_up_cn：后续所有表格都面向该子样本。

- evidence_pointer：Experimental Design P3

### 39. Measures P1 S1

- order：39

- section：Experiment

- locator：Measures P1 S1

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：作者用匿名捐赠者级数据构造开放、点击、捐赠、距离和推荐指标，并用人口普查邮编数据补充地区属性。

- rhetorical_function_cn：说明变量来源和构造。

- depends_on_cn：实验平台必须提供日志数据。

- sets_up_cn：为随机化检验和回归分析提供变量。

- evidence_pointer：Table 2

### 40. Randomization P1 S1

- order：40

- section：Experiment

- locator：Randomization P1 S1

- move_code：ROBUSTNESS_OR_BOUNDARY_TEST

- paraphrase_cn：随机化平衡检验显示处理组与对照组在社会影响、距离、收入、人口和BIPOC高占比地区等协变量上没有显著差异。

- rhetorical_function_cn：验证实验内部有效性。

- depends_on_cn：需要测量协变量。

- sets_up_cn：让后续简单t检验可作为因果解释。

- evidence_pointer：Table 3

### 41. Experimental Results Intro S1

- order：41

- section：Experiment

- locator：Experimental Results Intro S1

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：由于随机分配且捐赠者不知情，内生性和观察者偏差被最小化，简单t检验足以评估因果效果。

- rhetorical_function_cn：说明为什么不需要复杂因果识别。

- depends_on_cn：平衡检验已确认随机化。

- sets_up_cn：主效应表可直接解释为因果效应。

- evidence_pointer：Experimental Results intro

### 42. Effects H1 P1 S1

- order：42

- section：Experiment

- locator：Effects H1 P1 S1

- move_code：RESULT

- paraphrase_cn：本地个性化组的开放率、点击率和捐赠率均显著高于默认个性化组，支持H1a和H1b。

- rhetorical_function_cn：给出主效应结果。

- depends_on_cn：实验设计和t检验方法。

- sets_up_cn：作为后面异质性和后果分析的基础。

- evidence_pointer：Table 4

### 43. Effects H1 P2 S1

- order：43

- section：Experiment

- locator：Effects H1 P2 S1

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：为探讨效应是否随先前非本地捐赠距离变化，作者估计包含本地个性化与距离交互项的Logistic回归。

- rhetorical_function_cn：引入更精细的调节分析。

- depends_on_cn：主效应已经显著。

- sets_up_cn：检验‘潜在本土偏好’而非‘本就离得近’的解释。

- evidence_pointer：Table 5

### 44. Effects H1 P3 S1

- order：44

- section：Experiment

- locator：Effects H1 P3 S1

- move_code：RESULT

- paraphrase_cn：本地个性化主效应显著，且本地个性化×距离对点击和捐赠显著为正，说明越远离先前捐赠地，本地个性化提升越大。

- rhetorical_function_cn：报告调节结果。

- depends_on_cn：需要距离交互模型。

- sets_up_cn：强化‘激活潜在本土偏好’的解读。

- evidence_pointer：Table 5 Columns 6, 9

### 45. Heterogeneous Effects P1 S1

- order：45

- section：Experiment

- locator：Heterogeneous Effects P1 S1

- move_code：TRANSITION

- paraphrase_cn：作者接下来检查本地个性化的影响是否随捐赠者是否通过推荐链接首次捐赠而变化。

- rhetorical_function_cn：从主效应转向异质性。

- depends_on_cn：主效应已建立。

- sets_up_cn：为H2检验铺路。

- evidence_pointer：Heterogeneous Effects section

### 46. Heterogeneous Effects P2 S1

- order：46

- section：Experiment

- locator：Heterogeneous Effects P2 S1

- move_code：RESULT

- paraphrase_cn：推荐捐赠者中本地个性化只显著提高点击率；非推荐捐赠者中开放、点击和捐赠率均显著提高。

- rhetorical_function_cn：报告子群差异。

- depends_on_cn：需要将样本按推荐历史拆分。

- sets_up_cn：支持H2a部分和H2b。

- evidence_pointer：Table 6

### 47. Heterogeneous Effects P3 S1

- order：47

- section：Experiment

- locator：Heterogeneous Effects P3 S1

- move_code：RESULT

- paraphrase_cn：结果显示本地个性化普遍提高参与，但捐赠转换只发生在没有社会影响历史的捐赠者中，推荐捐赠者总体上响应率更低。

- rhetorical_function_cn：解释子群结果的理论意义。

- depends_on_cn：Table 6的结果。

- sets_up_cn：为讨论中启发式层级观点提供基础。

- evidence_pointer：Heterogeneous Effects P3

### 48. Consequences H3 P1 S1

- order：48

- section：Experiment

- locator：Consequences H3 P1 S1

- move_code：STUDY_OVERVIEW

- paraphrase_cn：最后作者检验H3，把样本限制在通过实验邮件捐赠的395名捐赠者，分析受赠地区收入与学校特征。

- rhetorical_function_cn：从行为结果转向分配后果。

- depends_on_cn：前文已证明主效应和异质性。

- sets_up_cn：用收入、学校和地理分布检验富者愈富。

- evidence_pointer：Consequences H3

### 49. Consequences H3 P2 S1

- order：49

- section：Experiment

- locator：Consequences H3 P2 S1

- move_code：RESULT

- paraphrase_cn：本地个性化显著提高受赠地区中位收入，并与捐赠者本地收入显著正交互，说明高收入捐赠者更倾向支持富裕地区。

- rhetorical_function_cn：报告收入层面证据。

- depends_on_cn：OLS模型设定。

- sets_up_cn：为H3提供直接支撑。

- evidence_pointer：Table 7

### 50. Consequences H3 P3 S1

- order：50

- section：Experiment

- locator：Consequences H3 P3 S1

- move_code：RESULT

- paraphrase_cn：本地个性化使捐赠到低低收入学生比例少的高收入学校的概率增加67%-96%。

- rhetorical_function_cn：从地区收入下沉到学校层面。

- depends_on_cn：需要学校免费/减价午餐数据。

- sets_up_cn：进一步支持教育资金不平等。

- evidence_pointer：Table 8

### 51. Consequences H3 P4 S1

- order：51

- section：Experiment

- locator：Consequences H3 P4 S1

- move_code：RESULT

- paraphrase_cn：本地个性化条件下41%的捐赠流向捐赠者本地社区，而对照组为22%；对照组更多流向最近支持地区。

- rhetorical_function_cn：报告地理分布差异。

- depends_on_cn：需要捐赠目的地数据。

- sets_up_cn：说明资金向富裕本地社区集中。

- evidence_pointer：Table 9

### 52. Consequences H3 P5 S1

- order：52

- section：Experiment

- locator：Consequences H3 P5 S1

- move_code：RESULT

- paraphrase_cn：社区属性向量分析显示，捐赠去向与实验条件地区在人口经济特征上显著更相似，即使流向‘其他’地区也如此。

- rhetorical_function_cn：把效应延伸到间接同质性机制。

- depends_on_cn：需要构造社区属性向量。

- sets_up_cn：为同质性而非单纯邻近提供证据。

- evidence_pointer：Table 10

### 53. Consequences H3 P6 S1

- order：53

- section：Experiment

- locator：Consequences H3 P6 S1

- move_code：RESULT

- paraphrase_cn：综合收入、学校、分布和相似性四类证据，本地个性化确实产生富者愈富效应。

- rhetorical_function_cn：总结分配后果。

- depends_on_cn：Table 7-10的结果。

- sets_up_cn：为讨论部分的理论和伦理意义提供结论。

- evidence_pointer：Consequences H3 P6

### 54. P1 S1

- order：54

- section：Discussion

- locator：P1 S1

- move_code：RESULT

- paraphrase_cn：作者总结：本地个性化提升参与和捐赠（H1）、社会影响历史改变捐赠转换（H2）、分配后果强化不平等（H3）。

- rhetorical_function_cn：把实证结果集中呈现为三个洞察。

- depends_on_cn：实验结果部分。

- sets_up_cn：随后转入理论和实践意义。

- evidence_pointer：Discussion P1

### 55. Theoretical Implications P2 S1

- order：55

- section：Discussion

- locator：Theoretical Implications P2 S1

- move_code：CONTRIBUTION

- paraphrase_cn：本文为启发式与个人化IS文献提供比较证据，提出社会影响的信任驱动强于地理邻近的层级。

- rhetorical_function_cn：把结果升华为理论贡献。

- depends_on_cn：H1-H3的结果。

- sets_up_cn：将贡献从技术效果提升到机制理解。

- evidence_pointer：Theoretical Implications

### 56. Theoretical Implications P3 S1

- order：56

- section：Discussion

- locator：Theoretical Implications P3 S1

- move_code：CONTRIBUTION

- paraphrase_cn：作者把研究置于个性化与平台公平的交汇点，证明即使最简单的个性化也会产生富者愈富的再分配效应。

- rhetorical_function_cn：扩展IS文献中的社会公平视角。

- depends_on_cn：H3的分配后果。

- sets_up_cn：为实践建议做铺垫。

- evidence_pointer：Theoretical Implications

### 57. Practical Implications P1 S1

- order：57

- section：Discussion

- locator：Practical Implications P1 S1

- move_code：CONTRIBUTION

- paraphrase_cn：作者指出静态地理位置属性可以超越基于行为历史的个性化，但同一策略也可能加剧不平等。

- rhetorical_function_cn：把结果转化为平台设计启示。

- depends_on_cn：主效应和分配后果。

- sets_up_cn：提出轮换/组合个性化建议。

- evidence_pointer：Practical Implications

### 58. Limitations P1 S1

- order：58

- section：Discussion

- locator：Limitations P1 S1

- move_code：LIMITATION_AND_FUTURE

- paraphrase_cn：研究限制包括从行为推断启发式、未纳入其他启发式、邮编层面聚合数据、未直接评估缓解策略等。

- rhetorical_function_cn：保护贡献免受过度一般化。

- depends_on_cn：全文已作出主要贡献。

- sets_up_cn：为未来研究指明方向。

- evidence_pointer：Limitations

### 59. P1 S1

- order：59

- section：Conclusion

- locator：P1 S1

- move_code：CONTRIBUTION

- paraphrase_cn：结论强调本地个性化提供因果证据并揭示其放大社会经济差距的风险，平台设计兼具技术责任与道德责任。

- rhetorical_function_cn：以更宏大的平台责任收尾。

- depends_on_cn：全部理论、实证和讨论。

- sets_up_cn：结束文章，强化贡献意义。

- evidence_pointer：Conclusion

## 写作技术

- gap_construction_cn：文章不采用‘没人研究’式缺口，而是强调既有研究分别证明两种启发式、常假设它们一致，却缺少竞争情境比较和平台推广层面的检验；因此缺口是‘解释不足’与‘策略未检验’的结合。

- signposting_cn：摘要直接列出发现；引言列出三个研究问题；结尾给出路线图；假设用H1a/H1b/H2a/H2b/H3明确标记；每个分析段落以‘我们检验/我们接下来/最后’等方式预告。

- transition_logic_cn：从平衡检验到主效应，从主效应到距离交互，从主效应到‘我们接下来检查社会影响’，再到‘最后测试H3’，每一步都是‘已有证据—新问题—新分析’。

- claim_evidence_rhythm_cn：先提假设→描述实验→平衡检验→简单t检验→回归→子群→分配后果；每个结果段先给核心系数或均值，再解释对应假设，再给机制说明。

- benchmark_narrative_cn：平台默认的‘最近捐赠地’个性化作为自然控制条件，使benchmark不是虚构基线而是真实业务策略；随后用距离分层、推荐历史分层、学校收入和社区相似度扩大对照范围。

- theory_return_cn：讨论部分把‘本地提高参与但推荐者不转化’解释为社会影响强于地理邻近的层级，把收入与相似性结果解释为同质性和马太效应的体现，重新连接到开头理论。

- contribution_positioning_cn：贡献不是‘我们提升了点击率’，而是‘证明启发式可被激活、存在可细分的捐赠者层级、简单个性化影响公平’，把论文放在IS的平台与社会公平脉络中。

- novelty_protection_cn：通过大规模真实随机实验、非本地捐赠者样本、距离交互、推荐异质性和分配后果四重证据，避免论文退化为一次性邮件效果报告；同时坦诚未测认知机制和缓解策略，使贡献范围清晰。

## 可复用研究与写作程序

### structure_steps

#### 1. 1

- step：1

- writing_job_cn：建立平台背景与现象，指出使命与行为错位。

- research_job_cn：识别平台关键决策（个性化推广）和核心行为（捐赠者启发式）。

- required_evidence_cn：平台规模、捐赠者自由选择、行业或文献证据表明启发式普遍存在。

- transition_to_next_cn：从现象推到‘两种启发式如何交互’的文献缺口。

#### 2. 2

- step：2

- writing_job_cn：用理论机制推导可检验假设。

- research_job_cn：界定本土偏好与社会影响的机制，预测主效应、异质性和分配后果。

- required_evidence_cn：文献能支持机制路径；假设必须能被随机实验操纵和测量。

- transition_to_next_cn：‘为检验这些假设，我们开展随机现场实验’。

#### 3. 3

- step：3

- writing_job_cn：描述实验设计、变量、样本和随机化验证。

- research_job_cn：与平台合作生成处理与对照邮件，获取行为日志和邮编数据，检查平衡性。

- required_evidence_cn：随机化平衡表；清晰的实验条件差异。

- transition_to_next_cn：‘随机化有效，因此可进行简单因果比较’。

#### 4. 4

- step：4

- writing_job_cn：循序报告主效应、调节效应和异质性。

- research_job_cn：使用t检验、回归和子群分析检验H1/H2。

- required_evidence_cn：显著的总体结果；关键调节变量能推进机制而非只是细分。

- transition_to_next_cn：‘既然行为改变了，再看资源流向何处’。

#### 5. 5

- step：5

- writing_job_cn：检验分配后果并上升到理论含义。

- research_job_cn：用受赠地区收入、学校特征、地理分布和相似性分析支持公平后果主张。

- required_evidence_cn：后果指标确实受处理影响；能从机制上解释，而非仅事后相关。

- transition_to_next_cn：结果返回理论层级和平台责任。

#### 6. 6

- step：6

- writing_job_cn：总结贡献、实践建议、局限与未来研究。

- research_job_cn：把实证结果重构为可复用设计知识和理论边界。

- required_evidence_cn：讨论中的每项贡献都能索引到前面的具体结果。

- transition_to_next_cn：以平台责任收束全文。

### most_transferable_moves_cn

1. 把真实平台默认策略作为对照，避免虚构baseline。

2. 用随机化平衡表建立内部有效性，使后续分析可因果解释。

3. 先报告总体主效应，再用距离和推荐历史等可测量变量做调节与异质性。

4. 把行为结果延伸到分配结果（地区收入、学校特征、目的地相似性），将性能提升变成社会后果。

5. 在讨论中用‘启发式层级’和‘个性化与公平’重述贡献，而不是只讲点击率提升。

### resource_intensive_or_nonstandard_parts_cn

1. 与大型慈善众筹平台建立正式合作并获取近16万真实捐赠者样本。

2. 平台具备成熟邮件个性化引擎和开放/点击/捐赠追踪能力。

3. 需要账单邮编、最近支持学校邮编、捐赠学校邮编、教师推荐链接等平台内部数据。

4. 需要与美国人口普查及ZipCodeR邮编数据对接，计算距离和社区属性相似度。

5. 随机化实验需在固定时间窗口（2021年10月）内完成，数据期限和平台合规成本高。

### what_not_to_copy_superficially_cn

1. 不能只复制‘本地化邮件’的措辞而不设置真正随机对照组，否则无法声称因果。

2. 不能在没有推荐链接历史时使用‘社会影响历史’变量。

3. 不能在没有受赠地区收入、学校午餐比例和邮编社区属性时声称rich-get-richer。

4. 不能仅凭行为结果宣称‘潜在启发式激活’，必须承认缺少认知测量。

5. 不能把DonorsChoose单平台结果推广到全部众筹平台而不加边界条件。

- single_best_description_of_the_routine_cn：用现实平台的随机邮件实验把两个启发式的比较与激活问题变成可检验的因果设计，并沿‘主效应—异质性—分配后果’的证据链把技术有效性上升为理论层级与平台伦理贡献。

## 分析边界

文章无印刷页码，位置以章节/段落/表格编号表示；未提供在线附录或实验材料原文；表格数值依据文中呈现的表格，潜在OCR风险较低但无法独立核验；分析未重运行作者代码。
