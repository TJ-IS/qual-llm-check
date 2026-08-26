# A social recommendation approach for reward-based crowdfunding campaigns

- 作者：Yung-Ming Li; Jyh-Hwa Liou; Yi-Wen Li
- 年份 / 期刊：2020 / Information & Management
- DOI：10.1016/j.im.2019.103246
- 源文件：10158_2020_a-social-recommendation-approach-for-reward-based-crowdfunding-campaigns.md
- 论文主类型：build_evaluate_design_science
- 主导写作弧线：problem_theory_design_test_return
- 置信度：0.9

## 文章级论证概况

- 核心问题：如何利用社交网络数据设计一个阶段敏感的支持者推荐机制，帮助奖励型众筹项目在不同筹资阶段找到合适的支持者，从而提高众筹成功率？

- 制品与设计：提出的制品是一个阶段化众筹支持者推荐系统，由TypeTree构建模块、社会关系分析模块、用户偏好分析模块（含支持者偏好、个人偏好、经济能力）和众筹推荐引擎模块组成。系统整合Facebook社交数据和FlyingV/zeczec众筹平台数据，基于社会网络理论评估支持者与创建者的社会关系，通过活动数据推断偏好，利用AHP根据项目阶段和距离动态融合四因素（社会关系、个人偏好、支持者偏好、经济能力），生成不同阶段的候选支持者列表。

- 客观结果：实验结果显示，所提阶段化方法的点赞率为0.598、分享率为0.404，均高于内容型（0.338/0.266）、协同型（0.401/0.281）和社会型（0.454/0.356）基准；配对t检验显示点赞率差异显著；分享率相对于社会型基准不显著（T=0.66）。问卷结果显示所提模型在喜好、满意度和投资意愿上平均得分最高。

- 核心贡献：提出一个结合网络效应和社会资本理论的阶段化支持者推荐机制，通过动态整合社会关系、个人偏好、支持者偏好和经济能力，并根据项目阶段调整候选组，能够更有效地识别合适支持者，显著提高推荐效果，为众筹平台提供应用价值。

- 整篇论证链：文章首先指出现有众筹成功率低的现实问题，且学界对成功因素的研究只考虑偏好或社会关系的单一方面，未考虑筹资阶段。基于社会网络理论（强/弱连接、信任）和众筹动态文献（第一周家人/朋友支持、后期陌生人），设计了一个分为TypeTree构建、社会关系分析、用户偏好分析、经济能力分析、推荐引擎的五个模块的推荐系统。系统利用Facebook活动数据和两个台湾众筹平台项目数据，通过AHP计算四因素权重，依据项目阶段和距离选择候选组并生成推荐列表。实验以282名真实用户在59个项目上的行为指标（点赞、分享）和问卷（喜好、满意度、投资意愿）为因变量，与内容、协同、社会和随机基准比较，发现所提方法在大多数指标上显著更好。作者据此宣称贡献在于结合网络效应和社会资本理论，形成可复用的阶段化推荐设计知识，并强调实践价值。但实验未直接追踪项目实际成功率，存在一定过度主张。

## 类型与写作弧线判定

- 论文主类型判定：文章遵循设计科学范式：基于理论和实践需求设计了一个新的众筹推荐系统（制品），然后通过实验评估其性能，并总结贡献和设计知识。虽然也有benchmark对比，但核心是系统构建和评价，不是纯粹的算法benchmark。

- 主导写作弧线判定：文章开头从众筹成功率低这一现实问题出发，通过文献综述引出理论（社会网络理论、网络效应），然后设计推荐系统（理论到设计），并通过实验检验，最后在讨论中返回理论贡献和实践启示。

## 研究开展程序

- study_or_phase_count：4

- 研究阶段总序列：系统设计阶段（第3节）——实验设置与数据收集阶段（第4节）——行为结果评价阶段（第5.1节）——问卷结果评价阶段（第5.2节）。设计阶段基于理论构建了完整的推荐机制；实验阶段收集真实用户和项目数据，确定AHP权重和基准方法；随后通过行为指标和问卷指标验证机制有效性，并逐步建立从设计到证据的闭环。

### studies_or_phases

#### 1. 系统架构与模型构建

- order：1

- name_cn：系统架构与模型构建

- question_cn：如何设计一个能够利用社会关系和用户偏好、并适应不同筹资阶段的众筹支持者推荐机制？

- inputs_and_setting_cn：基于社会网络理论、众筹文献和推荐系统文献；无实验数据，主要设计阶段。

- designed_or_compared_object_cn：推荐系统的四个核心模块：TypeTree、社会关系分析、用户偏好分析、经济能力分析、众筹推荐引擎。

- baseline_control_or_counterfactual_cn：无（设计阶段）。

##### objective_metrics

（空）

- analysis_method_cn：概念设计、公式推导。

- main_result_cn：得到完整的推荐机制，包括公式（1）-（30）。

- argumentative_role_cn：建立明确的设计知识，支撑后续实现和评价。

- remaining_uncertainty_cn：该机制是否真的有效，需要实验验证。

- link_to_next_phase_cn：设计的系统需要在真实数据下实现并评测，因此进入实验阶段。

##### evidence_pointers

1. Section 3.1-3.5

2. Fig. 1

3. equations (1)-(30)

#### 2. 实验数据收集与权重计算

- order：2

- name_cn：实验数据收集与权重计算

- question_cn：在真实Facebook和众筹平台环境下，如何收集用户、项目数据，并确定AHP权重？

- inputs_and_setting_cn：通过Facebook众筹俱乐部邀请282名用户参与；从FlyingV和zeczec收集59个项目；使用Facebook Graph API获取用户数据；用户填写AHP问卷。

- designed_or_compared_object_cn：数据收集系统、TypeTree/ProjectTree、AHP权重问卷。

- baseline_control_or_counterfactual_cn：无（不涉及推荐策略比较）。

##### objective_metrics

（空）

- analysis_method_cn：数据收集、AHP方法计算准则权重。

- main_result_cn：获得282名用户行为数据和59个项目的状态；得到三个候选组的AHP权重（Table 5）；确定基准方法因素组合。

- argumentative_role_cn：为推荐系统实现提供输入，并为后续评估建立基准。

- remaining_uncertainty_cn：数据是否足以支持推荐效果差异？用户主观反馈未知。

- link_to_next_phase_cn：数据就绪和权重确定后，即可运行推荐系统并测量指标。

##### evidence_pointers

1. Section 4.1-4.3

2. Table 2-5

3. Fig. 3-10

#### 3. 行为结果评价：like与share率

- order：3

- name_cn：行为结果评价：like与share率

- question_cn：提出的phase-based推荐相比其他基准，在用户点赞和分享行为上是否更优？

- inputs_and_setting_cn：282位用户，通过系统邀请后记录点赞/分享行为，比较五种推荐方式（phase-based, content, collaborative, social, random）。

- designed_or_compared_object_cn：不同推荐策略的邀请列表（每个用户收到不同模型生成的邀请）。

- baseline_control_or_counterfactual_cn：content-based, collaborative-based, social-based, random。

##### objective_metrics

1. LikeRate

2. ShareRate

- analysis_method_cn：描述性统计，配对样本t检验（95%置信区间）。

- main_result_cn：phase-based的like率0.598，share率0.404，显著高于除social-based外的其他基准；t检验显示点赞率差异显著，分享率相对social-based不显著。

- argumentative_role_cn：证明设计的机制在行为层面优于现有方法。

- remaining_uncertainty_cn：like/share是否能代表真实投资意愿？用户主观感受如何？

- link_to_next_phase_cn：行为指标显示积极性，还需要问卷评估主观态度。

##### evidence_pointers

1. Section 5.1

2. Fig. 12-13

3. Table 7-8

#### 4. 问卷评估：喜好、满意度与投资意愿

- order：4

- name_cn：问卷评估：喜好、满意度与投资意愿

- question_cn：用户对phase-based生成的邀请内容的喜好、满意度和投资意愿是否高于其他基准？

- inputs_and_setting_cn：被邀请的backer填写1-5分的问卷，评估三方面；对不同模型和场景（scenario）比较。

- designed_or_compared_object_cn：不同推荐模型的邀请（在三个场景中评估）。

- baseline_control_or_counterfactual_cn：同上，包括random。

##### objective_metrics

1. Liking

2. Satisfaction

3. Willingness

- analysis_method_cn：平均分值比较（图表），未提及统计检验。

- main_result_cn：phase-based在三个指标上均最高，random最低；且发现social relationship在Scenario 1影响高，preference和economic在Scenario 3影响高。

- argumentative_role_cn：从用户主观角度补充证据，支持机制的有效性。

- remaining_uncertainty_cn：未进行显著性检验；没有追踪到真实投资行为。

- link_to_next_phase_cn：结果支持贡献主张，进入讨论。

##### evidence_pointers

1. Section 5.2

2. Fig. 14-16

## 各部分修辞架构

### abstract_moves

1. CONTEXT

2. PHENOMENON

3. GAP

4. RQ_OR_OBJECTIVE

5. RESULT

6. CONTRIBUTION

### introduction_moves

1. CONTEXT

2. PRACTICAL_STAKES

3. PHENOMENON

4. LIMITATION

5. GAP

6. RQ_OR_OBJECTIVE

7. THEORY_INTRO

8. STUDY_OVERVIEW

### theory_and_knowledge_moves

1. PRIOR_KNOWLEDGE

2. LIMITATION

3. THEORY_INTRO

4. THEORY_PROPOSITION

5. MECHANISM

### artifact_design_moves

1. THEORY_INTRO

2. DESIGN_FEATURE

3. METHOD_JUSTIFICATION

4. REQUIREMENT

5. HYPOTHESIS_OR_PROPOSITION

### evaluation_moves

1. METHOD_JUSTIFICATION

2. BENCHMARK_OR_CONTRAST

3. RESULT

4. ROBUSTNESS_OR_BOUNDARY_TEST

### discussion_and_contribution_moves

1. CONTRIBUTION

2. BOUNDARY_CONDITION

3. LIMITATION_AND_FUTURE

## 理论/知识到设计的翻译

### 知识/理论基础

1. 社会网络理论（强/弱连接、社会信任）

2. 社会资本理论

3. 众筹动态研究（Kuppuswamy & Bayus）

4. 推荐系统（内容、协同、社会）

5. 多准则决策AHP

- 理论—设计耦合：partial

- 耦合判定理由：社会网络理论直接决定了社会关系分析模块的设计（强/弱连接、信任），众筹动态研究决定了阶段化推荐。但用户偏好分析模块主要来自推荐系统文献中的内容/协同方法，经济能力分析则来自领域要求，AHP权重方法来自决策科学，因此整体属于理论影响了部分设计，而非完全理论推导。

- 理论到设计翻译链：社会网络理论：强连接导致更高信任 → 早期阶段注重社会关系 → 候选组1权重社会关系最高（表5）；众筹动态：第一周家人朋友是主要支持者 → 阶段划分 → 候选组1为强连接用户；AHP: 多准则决策 → 动态调整四因素权重；TypeTree: 分类学 → 偏好匹配。

### mapping_table

#### 1. 1

- theory_or_knowledge_claim_cn：强/弱连接理论：强连接的人之间信任更高，对高风险的众筹投资影响更大

- mechanism_cn：社会关系强度 → 信任 → 投资意愿

- design_requirement_cn：早期阶段应优先推荐强连接用户

- artifact_choice_cn：社会关系分析模块使用互动次数、共同朋友数、路径长度计算SocialRelationship，并按关系强度分为三组

- evaluated_contrast_cn：与content-based（无社会关系）和collaborative-based（无社会关系）对比

- objective_result_cn：phase-based在like/share率上显著更高，且问卷显示Scenario 1中social relationship影响最高

##### evidence_pointers

1. Section 3.3

2. Table 5

3. Fig 14-16

#### 2. 2

- theory_or_knowledge_claim_cn：众筹动态研究：支持者在第一周和最后一周贡献更多，家人/朋友在第一周出现

- mechanism_cn：阶段不同 → 有效支持者群体不同 → 需动态推荐

- design_requirement_cn：推荐系统应根据项目阶段和距离选择不同候选组

- artifact_choice_cn：crowdfunding recommendation engine使用ProjectPhase和ProjectDistance计算FundraisingStatus，选择候选组（公式19-25）

- evaluated_contrast_cn：与不划分阶段的基准相比

- objective_result_cn：phase-based优于其他基准

##### evidence_pointers

1. Section 3.5

2. Section 5.1.1

#### 3. 3

- theory_or_knowledge_claim_cn：推荐系统Literature：内容推荐基于用户历史偏好，协同基于相似用户，社会推荐基于社会关系

- mechanism_cn：单一因素不足，需多准则整合

- design_requirement_cn：整合社会关系、个人偏好、支持者偏好、经济能力

- artifact_choice_cn：Suitability公式（30）加权求和四因素，AHP确定权重

- evaluated_contrast_cn：与单一因素基准对比

- objective_result_cn：phase-based显著更高

##### evidence_pointers

1. Section 3.5.3

2. Section 4.4

3. Section 5

## 评价逻辑

### evaluation_modes

1. 行为指标（点赞率、分享率）

2. 问卷（喜好、满意度、投资意愿）

3. 配对t检验

4. 基准对比（content, collaborative, social, random）

- why_these_evaluations_cn：为了验证推荐机制的实际效果，需要从行为层面（用户是否互动）和主观层面（用户是否满意）进行测量，并与现有推荐方法对比，以证明其优越性。

- benchmark_and_contrast_chain_cn：先确定三个代表性基准（内容、协同、社会），分别对应不同推荐技术；为隔离因素效应，每个基准都包含经济能力因素，但缺少其他因素。然后通过配对设计比较本方法与各基准的行为和问卷得分。

### claim_evidence_ledger

#### 1. phase-based的like率显著高于其他基准

- claim_cn：phase-based的like率显著高于其他基准

- evidence_cn：Table 7配对t检验，Sig.均为0.00

- supported：是

#### 2. phase-based的share率显著高于所有基准

- claim_cn：phase-based的share率显著高于所有基准

- evidence_cn：Table 8中Phase-based vs Social-based的T=0.66，95%CI包含0，不显著；作者声称显著，证据不一致

- supported：否

#### 3. phase-based在问卷指标上优于其他

- claim_cn：phase-based在问卷指标上优于其他

- evidence_cn：Fig.14-16，无统计检验，仅为描述性平均值比较

- supported：是

#### 4. 机制能显著提高众筹成功率

- claim_cn：机制能显著提高众筹成功率

- evidence_cn：未直接测量项目成功率，使用like/share/问卷作为代理

- supported：否

- internal_validity_strategy_cn：使用配对样本设计（同一组用户接受所有模型条件），减少个体差异；通过t检验确定差异显著性。

- external_validity_strategy_cn：使用真实Facebook用户数据，两个众筹平台（FlyingV和zeczec），覆盖多种项目类型，模拟真实推荐场景。

- what_is_not_actually_tested_cn：实际的众筹项目成功率没有被直接追踪；推荐后是否真实投资没有被记录；仅在Facebook平台和台湾用户中验证；没有评估不同项目类型和规模的稳健性。

## 贡献闭环

- technical_claim_cn：所提出的阶段化推荐机制在点赞率、分享率、用户喜好、满意度和投资意愿上优于内容、协同、社会和随机基准。

- artifact_claim_cn：机制中的各模块（TypeTree, 社会关系, 偏好, 经济能力, AHP权重）协同工作导致性能提升。

- mechanism_claim_cn：通过根据项目阶段动态调整社会关系、个人偏好、支持者偏好和经济能力的权重，识别出不同阶段最合适的支持者群体，从而增强支持意愿。

- boundary_claim_cn：基于Facebook数据，在两个台湾众筹平台（FlyingV/zeczec）环境中验证；可能适用于类似文化和平台结构；受限于隐私政策等。

- reusable_design_knowledge_cn：阶段化众筹推荐的设计原则：使用TypeTree进行偏好映射，使用AHP结合多准则，根据项目阶段切换候选组，利用社交互动和共同朋友评估社会关系。

- theoretical_contribution_cn：结合网络效应和社会资本理论，提出了阶段化backer推荐机制；验证了社会关系在早期阶段的重要性，偏好在经济/晚期阶段的重要性。

- how_discussion_closes_intro_gap_cn：引言指出现有研究只考虑部分因素且忽视阶段，讨论中总结了所提机制通过动态整合四因素和阶段化推荐解决这一缺口，并强调理论贡献和实践影响。

- overclaim_or_unsupported_leaps_cn：声称显著提高了众筹成功率，但实验没有实际追踪项目结果；分享率与社交基准的比较中，t检验不显著（表8中Phase-based vs Social-based不显著），但作者声称显著；问卷没有显著性检验，但作者称“performs better”；此外，样本是自愿参与的Facebook用户，可能存在选择偏差。

## 句级写作动作图谱

### 1. P1 S1-S4

- order：1

- section：Abstract

- locator：P1 S1-S4

- move_code：CONTEXT

- paraphrase_cn：众筹作为一种新兴筹资方式逐渐出现，人们可以通过平台让大众支持创意项目。

- rhetorical_function_cn：建立研究背景，让读者进入众筹领域。

- depends_on_cn：无

- sets_up_cn：为后续指出成功率低的问题做铺垫。

- evidence_pointer：Abstract, first four sentences

### 2. P1 S5

- order：2

- section：Abstract

- locator：P1 S5

- move_code：PHENOMENON

- paraphrase_cn：尽管众筹带来巨大机会，但融资计划的成功率仍然很低。

- rhetorical_function_cn：点出关键现实问题，作为研究动机。

- depends_on_cn：前文众筹的发展

- sets_up_cn：引出解决方案的必要性。

- evidence_pointer：Abstract, sentence 5

### 3. P1 S6

- order：3

- section：Abstract

- locator：P1 S6

- move_code：RQ_OR_OBJECTIVE

- paraphrase_cn：本研究提出一种基于阶段的backer推荐机制，融合众筹与社交网络信息，以帮助项目创建者在各阶段达成筹资目标。

- rhetorical_function_cn：概述研究目标和方法。

- depends_on_cn：问题陈述

- sets_up_cn：为后面的结果和贡献做摘要。

- evidence_pointer：Abstract, sentence 6

### 4. P1 S7-S8

- order：4

- section：Abstract

- locator：P1 S7-S8

- move_code：RESULT

- paraphrase_cn：实验结果显示所提机制在识别合适backer方面有效并显著提高成功率。

- rhetorical_function_cn：提前给出结论，吸引读者阅读。

- depends_on_cn：方法描述

- sets_up_cn：为正文详细介绍做保证。

- evidence_pointer：Abstract, last two sentences

### 5. P1 S1-S3

- order：5

- section：Introduction

- locator：P1 S1-S3

- move_code：CONTEXT

- paraphrase_cn：众筹是新式的公共筹资方式，是众包概念的延伸。

- rhetorical_function_cn：定义核心概念，并联系众包。

- depends_on_cn：无

- sets_up_cn：引入创作者和backer等术语。

- evidence_pointer：Introduction, paragraph 1

### 6. P1 S4-S6

- order：6

- section：Introduction

- locator：P1 S4-S6

- move_code：PRACTICAL_STAKES

- paraphrase_cn：众筹能帮助个人实现梦想，但有趣想法常因资金不足而失败；创作者在平台推广项目，若达成目标则获得资金并回馈支持者。

- rhetorical_function_cn：强调众筹的重要性和失败风险。

- depends_on_cn：众筹定义

- sets_up_cn：为后面讨论成功率低做伏笔。

- evidence_pointer：Introduction, paragraph 1, sentences 4-6

### 7. P2 S1-S2

- order：7

- section：Introduction

- locator：P2 S1-S2

- move_code：CONTEXT

- paraphrase_cn：众筹市场增长迅速，Kickstarter等平台有大量用户和资金。

- rhetorical_function_cn：展示众筹行业的规模。

- depends_on_cn：前文创作者/backer定义

- sets_up_cn：为说明问题普遍性提供背景。

- evidence_pointer：Introduction, paragraph 2

### 8. P3 S1-S2

- order：8

- section：Introduction

- locator：P3 S1-S2

- move_code：PHENOMENON

- paraphrase_cn：众筹项目只有按期达到目标才成功，若早期难以筹资并持续扩展，失败概率很高。

- rhetorical_function_cn：明确众筹项目的特殊约束和失败动态。

- depends_on_cn：众筹的all-or-nothing特性

- sets_up_cn：为阶段化推荐提供理论依据。

- evidence_pointer：Introduction, paragraph 3, first two sentences

### 9. P3 S3-S5

- order：9

- section：Introduction

- locator：P3 S3-S5

- move_code：PRACTICAL_STAKES

- paraphrase_cn：根据统计成功率从未超过50%；项目扩散太慢、创作者只能被动等待，网络效应导致初期缺乏支持时人们不愿投资。

- rhetorical_function_cn：强调问题的严重性并解释原因。

- depends_on_cn：众筹失败动态

- sets_up_cn：引出需要主动推荐机制。

- evidence_pointer：Introduction, paragraph 3, sentences 3-5

### 10. P4 S1-S2

- order：10

- section：Introduction

- locator：P4 S1-S2

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：近期研究从偏好或社会网络角度探究众筹成功因素。

- rhetorical_function_cn：概述已有研究领域。

- depends_on_cn：背景

- sets_up_cn：为指出不足做铺垫。

- evidence_pointer：Introduction, paragraph 4, first two sentences

### 11. P4 S3

- order：11

- section：Introduction

- locator：P4 S3

- move_code：LIMITATION

- paraphrase_cn：现有工作仅考虑偏好或社会方面的部分因素，而且社会推荐面临社交信息难以获取的问题。

- rhetorical_function_cn：指出已有研究的片面性。

- depends_on_cn：已有研究

- sets_up_cn：突出本研究的综合视角。

- evidence_pointer：Introduction, paragraph 4, sentence 3

### 12. P4 S4

- order：12

- section：Introduction

- locator：P4 S4

- move_code：GAP

- paraphrase_cn：现有研究主要研究社会关系对众筹的影响，但未考虑筹资状态；不同阶段的支持者群体特征不同，需要深入研究。

- rhetorical_function_cn：明确文献缺口：缺少分阶段研究。

- depends_on_cn：对现有研究的限制

- sets_up_cn：为研究问题提供空间。

- evidence_pointer：Introduction, paragraph 4, sentence 4

### 13. P4 S5-S6

- order：13

- section：Introduction

- locator：P4 S5-S6

- move_code：RQ_OR_OBJECTIVE

- paraphrase_cn：本研究通过动态结合社会关系和用户偏好，开发新推荐机制，识别与项目高度相关的合适backer，帮助创作者克服各阶段瓶颈。

- rhetorical_function_cn：提出研究目标和途径。

- depends_on_cn：缺口

- sets_up_cn：引出三个具体研究问题。

- evidence_pointer：Introduction, paragraph 4, final sentences

### 14. P5

- order：14

- section：Introduction

- locator：P5

- move_code：RQ_OR_OBJECTIVE

- paraphrase_cn：提出三个问题：如何从社交网络找到感兴趣的支持者；如何增强支持者信任和投资意愿；如何在不同筹资阶段利用社交网络力量提高成功率。

- rhetorical_function_cn：详细陈述研究问题，细化目标。

- depends_on_cn：总体目标

- sets_up_cn：引导后续系统设计。

- evidence_pointer：Introduction, paragraph 5 (the three questions)

### 15. P6 S1-S2

- order：15

- section：Introduction

- locator：P6 S1-S2

- move_code：STUDY_OVERVIEW

- paraphrase_cn：我们开发新推荐机制，主要模块包括用户偏好和社会关系分析，筹资活动分为几个阶段。

- rhetorical_function_cn：预告机制组成和阶段划分。

- depends_on_cn：研究问题

- sets_up_cn：为系统框架章节做预览。

- evidence_pointer：Introduction, paragraph 6, sentences 1-2

### 16. P6 S3-S4

- order：16

- section：Introduction

- locator：P6 S3-S4

- move_code：DESIGN_FEATURE

- paraphrase_cn：初始阶段推荐给家人和朋友，中间阶段通过社交网络识别感兴趣的朋友，最终阶段达到目标；系统实现后实验显示优于其他基准。

- rhetorical_function_cn：概述阶段化推荐流程和初步结果。

- depends_on_cn：阶段划分

- sets_up_cn：为论文结构提供预览。

- evidence_pointer：Introduction, paragraph 6, sentences 3-4

### 17. P3 S1-S2

- order：17

- section：Section 2.1

- locator：P3 S1-S2

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：众筹分为奖励型、借贷型和股权型，本研究聚焦奖励型。

- rhetorical_function_cn：限定研究范围。

- depends_on_cn：众筹定义

- sets_up_cn：为后面的推荐设计提供特定场景。

- evidence_pointer：Section 2.1, paragraph 3

### 18. P4 S1

- order：18

- section：Section 2.1

- locator：P4 S1

- move_code：LIMITATION

- paraphrase_cn：少数研究尝试识别成功因素，但只考虑偏好或社会方面的部分因素。

- rhetorical_function_cn：在文献综述中重申缺口。

- depends_on_cn：已有研究

- sets_up_cn：强调本研究的综合方法。

- evidence_pointer：Section 2.1, paragraph 4, first sentence

### 19. P1 S1-P2 S1

- order：19

- section：Section 2.2

- locator：P1 S1-P2 S1

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：推荐系统分为内容型和协同型，各有优缺点。

- rhetorical_function_cn：介绍推荐系统的基本分类和问题。

- depends_on_cn：推荐系统文献

- sets_up_cn：为提出社会推荐做对照。

- evidence_pointer：Section 2.2, paragraphs 1-2

### 20. P3 S1-P4 S1

- order：20

- section：Section 2.2

- locator：P3 S1-P4 S1

- move_code：LIMITATION

- paraphrase_cn：社会推荐利用社会影响生成可信推荐，但难以获取社交信息；现有系统只考虑部分因素，不能有效应用于众筹。

- rhetorical_function_cn：指出现有推荐系统在众筹场景的不足。

- depends_on_cn：推荐系统综述

- sets_up_cn：为阶段化多准则系统提供动机。

- evidence_pointer：Section 2.2, paragraphs 3-4

### 21. P2 S1-S2

- order：21

- section：Section 2.3

- locator：P2 S1-S2

- move_code：THEORY_INTRO

- paraphrase_cn：社会网络中的连接分为强连接和弱连接，强连接表示关系密切、信任度高，通常发生在家人和亲密朋友之间。

- rhetorical_function_cn：引入社会网络理论的基本概念。

- depends_on_cn：社会网络文献

- sets_up_cn：用于设计社会关系分析模块。

- evidence_pointer：Section 2.3, paragraph 2

### 22. P2 S3-S4

- order：22

- section：Section 2.3

- locator：P2 S3-S4

- move_code：THEORY_PROPOSITION

- paraphrase_cn：强连接的朋友对用户选择高风险产品的影响更高，信任是购买决策的重要因素。

- rhetorical_function_cn：建立理论命题，即强连接影响高风险决策。

- depends_on_cn：社会网络理论

- sets_up_cn：支撑早期推荐给强连接朋友的设计。

- evidence_pointer：Section 2.3, paragraph 2

### 23. P3 S1-S3

- order：23

- section：Section 2.3

- locator：P3 S1-S3

- move_code：MECHANISM

- paraphrase_cn：众筹是从陌生人筹款的过程，社会关系通过信任影响支持行为；社会资本是早期成功的关键；因此应优先寻找有相似偏好的强连接朋友。

- rhetorical_function_cn：将社会网络理论应用到众筹场景，形成机制。

- depends_on_cn：强连接理论

- sets_up_cn：为系统设计中社会关系模块提供依据。

- evidence_pointer：Section 2.3, paragraph 3

### 24. P1 S1-S4

- order：24

- section：Section 3.1

- locator：P1 S1-S4

- move_code：THEORY_INTRO

- paraphrase_cn：利用社会网络理论，我们设计阶段化推荐机制；通过收集社交和众筹行为信息识别偏好，评估互动强度和接近度来度量社会关系。

- rhetorical_function_cn：说明系统设计的理论基础。

- depends_on_cn：前面文献中的理论

- sets_up_cn：引入系统架构。

- evidence_pointer：Section 3.1, first paragraph

### 25. P1 S5

- order：25

- section：Section 3.1

- locator：P1 S5

- move_code：THEORY_PROPOSITION

- paraphrase_cn：根据众筹动态研究，支持者在第一周和最后一周贡献更多，家人和朋友支持者往往出现在第一周。

- rhetorical_function_cn：引入阶段相关实证知识。

- depends_on_cn：众筹动态文献[23]

- sets_up_cn：为阶段划分和候选组提供依据。

- evidence_pointer：Section 3.1, sentence 5

### 26. P1 S6

- order：26

- section：Section 3.1

- locator：P1 S6

- move_code：DESIGN_FEATURE

- paraphrase_cn：根据项目进展（早、中、晚阶段），机制动态调整不同候选组的准则权重，并生成相关backer列表。

- rhetorical_function_cn：描述核心设计特征：动态阶段化。

- depends_on_cn：阶段知识

- sets_up_cn：引出系统框架图。

- evidence_pointer：Section 3.1, final sentence

### 27. P2 S1-S2

- order：27

- section：Section 3.2

- locator：P2 S1-S2

- move_code：DESIGN_FEATURE

- paraphrase_cn：构建TypeTree层次结构，将众筹项目类型与Facebook偏好分类关联，用于分析用户偏好和项目相关性。

- rhetorical_function_cn：设计工具模块。

- depends_on_cn：分类学需求

- sets_up_cn：为偏好分析提供基础。

- evidence_pointer：Section 3.2, paragraph 2

### 28. P1 S1

- order：28

- section：Section 3.3

- locator：P1 S1

- move_code：REQUIREMENT

- paraphrase_cn：构建创作者社交网络以评估与潜在支持者的社会关系，并将其分类到三个候选组。

- rhetorical_function_cn：将社会关系理论转成具体需求。

- depends_on_cn：社会网络理论

- sets_up_cn：定义社会关系计算。

- evidence_pointer：Section 3.3, first sentence

### 29. P1 S1-P2 S1

- order：29

- section：Section 3.3.1

- locator：P1 S1-P2 S1

- move_code：DESIGN_FEATURE

- paraphrase_cn：社会互动强度由标记、评论、点赞、共同俱乐部数计算，并通过min-max归一化处理。

- rhetorical_function_cn：具体化社会关系计算。

- depends_on_cn：社会关系研究

- sets_up_cn：用于社会接近度。

- evidence_pointer：Section 3.3.1, equations (1)-(2)

### 30. P1 S1-P2 S3

- order：30

- section：Section 3.3.2

- locator：P1 S1-P2 S3

- move_code：DESIGN_FEATURE

- paraphrase_cn：社会接近度由共同朋友数量和互动强度组合，并考虑多路径计算最终社会关系。

- rhetorical_function_cn：定义社会关系的综合测度。

- depends_on_cn：互动强度

- sets_up_cn：用于排序和分组。

- evidence_pointer：Section 3.3.2, equations (3)-(5)

### 31. P1 S1-P2 S2

- order：31

- section：Section 3.4.1

- locator：P1 S1-P2 S2

- move_code：DESIGN_FEATURE

- paraphrase_cn：支持者偏好通过共享次数和类型偏好计算，类型偏好基于投资次数和金额。

- rhetorical_function_cn：设计支持者偏好模块。

- depends_on_cn：众筹活动数据

- sets_up_cn：补充用户偏好信息。

- evidence_pointer：Section 3.4.1, equations (8)-(9)

### 32. P2 S1

- order：32

- section：Section 3.4.1

- locator：P2 S1

- move_code：REQUIREMENT

- paraphrase_cn：对于没有众筹历史的新用户，偏好设为零；为避免冷启动问题，增加个人偏好分析。

- rhetorical_function_cn：解决数据稀疏。

- depends_on_cn：支持者偏好模块

- sets_up_cn：引入个人偏好模块。

- evidence_pointer：Section 3.4.1, final paragraph

### 33. P1 S1-P3 S1

- order：33

- section：Section 3.4.2

- locator：P1 S1-P3 S1

- move_code：DESIGN_FEATURE

- paraphrase_cn：个人偏好基于社交媒体上的签到、页面、点赞、评论，并使用TypeTree计算相似度。

- rhetorical_function_cn：设计个人偏好模块。

- depends_on_cn：TypeTree

- sets_up_cn：为推荐引擎提供偏好维度。

- evidence_pointer：Section 3.4.2, equations (10)-(12)

### 34. P1 S1-S2

- order：34

- section：Section 3.4.3

- locator：P1 S1-S2

- move_code：DESIGN_FEATURE

- paraphrase_cn：经济能力由年龄、教育、工作经验、收入四个层面评估。

- rhetorical_function_cn：设计经济能力模块。

- depends_on_cn：领域常识

- sets_up_cn：形成四因素之一。

- evidence_pointer：Section 3.4.3, equations (13)-(17)

### 35. P1 S1

- order：35

- section：Section 3.5

- locator：P1 S1

- move_code：DESIGN_FEATURE

- paraphrase_cn：阶段定义为第一周、中段和最后一周，不同阶段采用不同权重分布。

- rhetorical_function_cn：定义阶段规则。

- depends_on_cn：众筹动态研究

- sets_up_cn：为推荐引擎设置输入。

- evidence_pointer：Section 3.5, first sentence

### 36. P1 S1-P3 S1

- order：36

- section：Section 3.5.1

- locator：P1 S1-P3 S1

- move_code：DESIGN_FEATURE

- paraphrase_cn：计算项目阶段（PPhase）和项目距离（PDistance），用于确定推荐候选组。

- rhetorical_function_cn：描述状态计算。

- depends_on_cn：阶段和距离阈值

- sets_up_cn：为候选组选择做准备。

- evidence_pointer：Section 3.5.1, equations (18)-(23)

### 37. P1 S1-P2 S3

- order：37

- section：Section 3.5.2

- locator：P1 S1-P2 S3

- move_code：DESIGN_FEATURE

- paraphrase_cn：综合项目阶段和距离得到FundraisingStatus，然后根据阈值选择候选组。

- rhetorical_function_cn：建立状态到候选组的映射。

- depends_on_cn：PPhase和PDistance

- sets_up_cn：为权重调整提供基础。

- evidence_pointer：Section 3.5.2, equations (24)-(25)

### 38. P1 S1-P3 S3

- order：38

- section：Section 3.5.3

- locator：P1 S1-P3 S3

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：使用AHP方法确定社会关系、个人偏好、支持者偏好、经济能力四项准则的相对权重，通过问卷收集配对比较，并采用平均归一化列计算权重。

- rhetorical_function_cn：解释为什么使用AHP以及如何实施。

- depends_on_cn：多准则决策需求

- sets_up_cn：为推荐评分公式（30）提供权重。

- evidence_pointer：Section 3.5.3, equations (26)-(29)

### 39. P1 S1-S2

- order：39

- section：Section 3.5.4

- locator：P1 S1-S2

- move_code：DESIGN_FEATURE

- paraphrase_cn：最终生成推荐列表，包含项目信息和候选支持者的社会关系、偏好、联系方式等。

- rhetorical_function_cn：描述系统输出。

- depends_on_cn：所有分析模块

- sets_up_cn：为实验提供可操作界面。

- evidence_pointer：Section 3.5.4

### 40. P1 S1

- order：40

- section：Section 4

- locator：P1 S1

- move_code：STUDY_OVERVIEW

- paraphrase_cn：为验证机制，我们在两个众筹平台FlyingV和zeczec及Facebook上开展实验。

- rhetorical_function_cn：说明实验场景。

- depends_on_cn：系统设计

- sets_up_cn：介绍数据来源。

- evidence_pointer：Section 4, first sentence

### 41. Step 1

- order：41

- section：Section 4.1

- locator：Step 1

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：开发web系统，邀请用户登录Facebook并填写AHP问卷以计算准则权重。

- rhetorical_function_cn：说明实验操作步骤。

- depends_on_cn：系统实现

- sets_up_cn：确定数据收集方式。

- evidence_pointer：Section 4.1, Step 1

### 42. Step 2

- order：42

- section：Section 4.1

- locator：Step 2

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：创作者输入项目信息，包括未正式启动的项目概念。

- rhetorical_function_cn：描述项目数据输入。

- depends_on_cn：创作者参与

- sets_up_cn：为推荐测试提供项目样本。

- evidence_pointer：Section 4.1, Step 2

### 43. Step 3-4

- order：43

- section：Section 4.1

- locator：Step 3-4

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：系统计算项目阶段和距离，生成推荐列表；创作者邀请支持者，同时用户提供反馈。

- rhetorical_function_cn：描述匹配和反馈流程。

- depends_on_cn：推荐引擎

- sets_up_cn：为后续行为指标收集做铺垫。

- evidence_pointer：Section 4.1, Steps 3-4

### 44. P1 S1-S2

- order：44

- section：Section 4.2.1

- locator：P1 S1-S2

- move_code：RESULT

- paraphrase_cn：实验有282名用户参与，收集了大量Facebook活动数据。

- rhetorical_function_cn：报告样本规模和数据规模。

- depends_on_cn：数据收集

- sets_up_cn：说明实验数据基础。

- evidence_pointer：Section 4.2.1, Table 2

### 45. P1 S1-S4

- order：45

- section：Section 4.2.2

- locator：P1 S1-S4

- move_code：RESULT

- paraphrase_cn：共收集59个项目，覆盖16种类型和所有阶段/距离状态。

- rhetorical_function_cn：报告项目样本覆盖性。

- depends_on_cn：数据收集

- sets_up_cn：用于评价机制的适用性。

- evidence_pointer：Section 4.2.2, Table 3

### 46. P2

- order：46

- section：Section 4.3

- locator：P2

- move_code：RESULT

- paraphrase_cn：AHP结果显示社会关系在Phase1最重要，个人偏好在Phase3最重要。

- rhetorical_function_cn：报告权重计算结果，验证理论预期。

- depends_on_cn：AHP问卷

- sets_up_cn：为推荐引擎的动态权重提供依据。

- evidence_pointer：Section 4.3, Table 5

### 47. P1-P4

- order：47

- section：Section 4.4

- locator：P1-P4

- move_code：BENCHMARK_OR_CONTRAST

- paraphrase_cn：定义四种基准：内容型、协同型、社会型和随机，每种使用部分因素组合。

- rhetorical_function_cn：建立评价参照系。

- depends_on_cn：现有推荐方法

- sets_up_cn：用于对比实验。

- evidence_pointer：Section 4.4, Table 6

### 48. P2-P3

- order：48

- section：Section 5.1.1

- locator：P2-P3

- move_code：RESULT

- paraphrase_cn：点赞率结果：phase-based 0.598，其他基准较低；配对t检验显示差异显著。

- rhetorical_function_cn：报告主要行为指标结果。

- depends_on_cn：实验数据

- sets_up_cn：支撑方法效果核心主张。

- evidence_pointer：Section 5.1.1, Fig.12, Table 7

### 49. P2-P3

- order：49

- section：Section 5.1.2

- locator：P2-P3

- move_code：RESULT

- paraphrase_cn：分享率结果：phase-based 0.404，其他较低；配对t检验声称显著，但相对social-based不显著。

- rhetorical_function_cn：报告行为指标，注意与文本不一致。

- depends_on_cn：实验数据

- sets_up_cn：为讨论增加数据细节。

- evidence_pointer：Section 5.1.2, Fig.13, Table 8

### 50. P1

- order：50

- section：Section 5.2

- locator：P1

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：使用问卷测量用户对邀请的喜爱、满意度和投资意愿，采用1-5分。

- rhetorical_function_cn：解释主观测量方式。

- depends_on_cn：需要主观反馈

- sets_up_cn：为主观结果铺垫。

- evidence_pointer：Section 5.2

### 51. P1

- order：51

- section：Section 5.2.1-5.2.3

- locator：P1

- move_code：RESULT

- paraphrase_cn：三张图显示phase-based在喜好、满意度和投资意愿上平均分最高，random最低。

- rhetorical_function_cn：报告主观评价结果。

- depends_on_cn：问卷数据

- sets_up_cn：支持机制有效性主张。

- evidence_pointer：Section 5.2.1-5.2.3, Fig.14-16

### 52. P1

- order：52

- section：Section 6

- locator：P1

- move_code：CONTRIBUTION

- paraphrase_cn：研究提出阶段化backer推荐机制，整合社会关系、偏好和经济能力，通过AHP动态调整，以持续寻找合适支持者。

- rhetorical_function_cn：总结论文贡献。

- depends_on_cn：全部研究

- sets_up_cn：为详细贡献声明做铺垫。

- evidence_pointer：Section 6, first paragraph

### 53. P1

- order：53

- section：Section 6.1

- locator：P1

- move_code：CONTRIBUTION

- paraphrase_cn：理论贡献：结合网络效应和社会资本理论，提出阶段化推荐机制，并根据阶段分类支持者群体。

- rhetorical_function_cn：明确理论层面的贡献。

- depends_on_cn：引言缺口和文献

- sets_up_cn：突出学术价值。

- evidence_pointer：Section 6.1, first paragraph

### 54. P2

- order：54

- section：Section 6.1

- locator：P2

- move_code：CONTRIBUTION

- paraphrase_cn：实践贡献：系统帮助创作者找到潜在支持者，提高投资意愿，为众筹平台带来商业价值。

- rhetorical_function_cn：强调应用价值。

- depends_on_cn：实验结果

- sets_up_cn：吸引实践者。

- evidence_pointer：Section 6.1, second paragraph

### 55. P1

- order：55

- section：Section 6.2

- locator：P1

- move_code：LIMITATION_AND_FUTURE

- paraphrase_cn：局限性：仅使用Facebook数据，社交媒体不能完全反映现实，无法追踪实际投融资活动。

- rhetorical_function_cn：坦诚研究边界。

- depends_on_cn：数据和方法

- sets_up_cn：为未来工作提供方向。

- evidence_pointer：Section 6.2

### 56. P1

- order：56

- section：Section 6.3

- locator：P1

- move_code：LIMITATION_AND_FUTURE

- paraphrase_cn：未来工作：整合更多平台、更多活动维度，扩展至股权众筹，考虑地理距离和法律问题。

- rhetorical_function_cn：描述后续研究方向。

- depends_on_cn：局限性

- sets_up_cn：给出延续性研究课题。

- evidence_pointer：Section 6.3

## 写作技术

- gap_construction_cn：先说明众筹成功率低的实践痛点，然后指出现有研究只考虑偏好或社会关系的单一方面，且未考虑项目阶段，从而构造出“缺乏动态多因素阶段化推荐”的研究缺口。

- signposting_cn：文章开头预告三个研究问题，系统设计章节按模块组织，实验和结果用分段标题，便于读者追踪。

- transition_logic_cn：从问题到文献，再到系统设计，用“因此我们开发…”“本研究提出…”等表述承接。实验与结果之间通过“为验证机制…”过渡。

- claim_evidence_rhythm_cn：先提出机制，然后描述实验，再呈现数据和统计检验，最后在讨论中重申贡献。但有些主张（如成功率提高）缺乏直接证据，节奏略显跳跃。

- benchmark_narrative_cn：将基准设置为内容、协同、社会三类，并说明每类选择的因素组合，使对比有据可依。

- theory_return_cn：在讨论中回到社会网络理论，解释为什么阶段化权重有效（早期社会关系重要，后期偏好重要），用实验结果支持理论命题。

- contribution_positioning_cn：将贡献定位为结合网络效应和社会资本理论的新型推荐机制，而非单纯工程系统。

- novelty_protection_cn：通过强调“动态”和“阶段化”特征，对比现有静态推荐，并展示用户行为改善，避免被视为一次性的benchmark结果。

## 可复用研究与写作程序

### structure_steps

#### 1. 1

- step：1

- writing_job_cn：在引言中建立众筹成功率和现有推荐系统的双重不足。

- research_job_cn：明确研究对象和问题领域，收集市场数据。

- required_evidence_cn：成功率统计数据、平台规模、现有研究缺口陈述。

- transition_to_next_cn：说明需要新机制，引出研究问题。

#### 2. 2

- step：2

- writing_job_cn：综述相关文献，提炼可用的理论（社会网络、推荐系统、众筹动态）。

- research_job_cn：梳理文献，确认理论架构。

- required_evidence_cn：权威文献引用，理论概念明确。

- transition_to_next_cn：理论导出的设计需求作为系统框架的基础。

#### 3. 3

- step：3

- writing_job_cn：描述系统架构和每个模块的公式。

- research_job_cn：将理论转化为可计算的设计，编写伪代码或公式。

- required_evidence_cn：模块定义、数据输入输出说明、公式推导。

- transition_to_next_cn：展示系统实现后，说明需要实验验证。

#### 4. 4

- step：4

- writing_job_cn：说明实验设置：数据来源、参与用户、基准方法。

- research_job_cn：实施系统，收集真实数据，进行实验。

- required_evidence_cn：数据描述、实验步骤、基准定义。

- transition_to_next_cn：准备汇报结果。

#### 5. 5

- step：5

- writing_job_cn：呈现行为指标和统计检验结果，然后辅以问卷。

- research_job_cn：计算指标，执行t检验，分析问卷。

- required_evidence_cn：精确数值和p值，图表。

- transition_to_next_cn：结果支持贡献，进入讨论。

#### 6. 6

- step：6

- writing_job_cn：总结贡献，区别理论与实务，列出局限性。

- research_job_cn：反思研究边界和未来方向。

- required_evidence_cn：对引言的回应，限制说明。

- transition_to_next_cn：论文结束。

### most_transferable_moves_cn

1. 从现实问题出发，逐步缩小到具体缺口

2. 用理论指导设计要素

3. 设置包含部分因素的基准以隔离效应

4. 同时使用行为指标和问卷以三角验证

5. 在讨论中把结果上升到理论命题

### resource_intensive_or_nonstandard_parts_cn

1. 需要获取真实Facebook用户数据并访问Graph API，涉及隐私授权

2. 需要多个众筹平台的项目数据

3. 需要设计并实施AHP问卷

4. 需要进行现场部署和问卷收集

### what_not_to_copy_superficially_cn

1. 不要只声称“提高了成功率”而没有直接实测项目结果

2. 不要在分享率与社交基准不显著的情况下宣称“显著优于所有基准”

3. 不要忽略问卷数据缺乏显著性检验的问题

- single_best_description_of_the_routine_cn：从现实痛点出发，用理论构造需求，构建系统，以行为与问卷双指标与多基准比较，最后回到理论贡献的结构化设计科学套路。

## 分析边界

由于是PDF转换，部分公式符号缺失（如“?????????”），可能影响对具体参数的精确理解；表8中Phase-based vs Social-based的p值缺失，但文本声称显著，对解读有影响。此外，文章未提供完整的AHP问卷内容和随机基准的具体数字，限制了复现。
