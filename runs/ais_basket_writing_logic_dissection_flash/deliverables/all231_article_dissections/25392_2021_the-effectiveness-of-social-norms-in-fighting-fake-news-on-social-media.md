# The Effectiveness of Social Norms in Fighting Fake News on Social Media

- 作者：Henner Gimpel; Sebastian Heger; Christian Olenberger; Lena Utz
- 年份 / 期刊：2021 / Journal of Management Information Systems
- DOI：10.1080/07421222.2021.1870389
- 源文件：25392_2021_the-effectiveness-of-social-norms-in-fighting-fake-news-on-social-media.md
- 论文主类型：theory_derived_artifact_experiment
- 主导写作弧线：problem_theory_design_test_return
- 置信度：0.85

## 文章级论证概况

- 核心问题：作为社交媒体用户界面组成部分的injunctive和descriptive social norm messages能否改善用户举报假新闻的行为？

- 制品与设计：实验性新闻流界面中嵌入两种SN消息：injunctive message以新闻流顶部文本并要求点击确认；descriptive message在新闻帖上显示已有用户举报人数；分为control、injunctive、descriptive、combined四种处理；descriptive强度分5、25、125、625、3125五档；Study 2进一步区分正面（仅假新闻被标记）和负面（仅真新闻被标记）descriptive messages。

- 客观结果：injunctive message使假新闻举报几率较控制组提高96%且显著；descriptive单独不显著；combined提高295%且显著，并显著高于单独injunctive或descriptive；descriptive强度在625之前随强度增加提升举报几率，到3125时回落且与baseline无显著差异，呈倒U型；Study 2中positive与negative descriptive单独均无显著影响。

- 核心贡献：作者声称社会规范消息作为社交媒体界面设计特征能够正向影响用户举报假新闻行为，尤其是injunctive与descriptive结合最有效；这补充了IS领域关于假新闻的社会技术干预研究，并为平台提供实用工具；同时揭示descriptive norms的边界条件和潜在回火效应。

- 整篇论证链：先建立假新闻在社交媒体中传播且用户很少举报的现实矛盾，指出平台依赖用户举报作为事实核查前馈，进而引入社会心理学中的injunctive/descriptive norms和focus theory，推导四个假设：injunctive提高举报、descriptive提高举报、二者结合优于单独、descriptive强度呈倒U型；设计两个在线实验，在模拟Facebook的新闻流中操纵SN消息；Study 1的2x2实验支持H1、H3、H4但不支持H2，作者解释可能是descriptive消息混合了正负含义；Study 2拆分正负descriptive，证实descriptive单独仍无效果，并补充动机调查；讨论将结果带回理论贡献，说明社会规范可以作为社会技术干预手段，同时指出误报真实新闻的副作用和descriptive强度阈值。

## 类型与写作弧线判定

- 论文主类型判定：论文从社会心理学和焦点理论推导行为假设，将SN messages作为社交媒体界面中的设计特征进行操纵，并通过两个在线行为实验检验这些理论推导出的设计差异。

- 主导写作弧线判定：文章遵循从现实问题出发、引入理论、设计并实施实验、检验假设、最后回到理论贡献与边界条件的完整闭环；不是单纯的性能缺口或设计原则导向。

## 研究开展程序

- study_or_phase_count：4

- 研究阶段总序列：阶段顺序为：Study 1主实验检验四类处理对举报行为的影响及descriptive强度效应；在Study 1内部对H4进行帖子级强度后验分析；Study 2分离正负descriptive消息以解释H2的未支持结果；Study 2中补充举报动机与障碍调查。四阶段依次累积，前阶段的不确定性由后一阶段直接回应。

### studies_or_phases

#### 1. Study 1：不同社会规范消息条件下的举报行为实验

- order：1

- name_cn：Study 1：不同社会规范消息条件下的举报行为实验

- question_cn：四种处理（control、injunctive、descriptive、combined）对假新闻举报数量有何差异？descriptive强度对单帖举报概率影响如何？

- inputs_and_setting_cn：320名通过德国Facebook学生群招募的活跃社交媒体用户；自行开发的仿Facebook新闻流，含5条假新闻、5条真新闻、5条中性帖；进行自然交互浏览。

- designed_or_compared_object_cn：界面中的injunctive SN消息、descriptive SN消息（举报人数）的存在性及组合；descriptive强度5级。

- baseline_control_or_counterfactual_cn：无任何SN消息的control处理；以及以combined为baseline的rebase分析。

##### objective_metrics

1. 用户举报的假新闻数量（0-5）

2. 用户举报的真新闻数量（0-5）

3. 单条假新闻帖被举报的二元概率（H4）

4. odds ratio和效应量

- analysis_method_cn：有序logistic回归（Brant检验比例优势假设）；因子式强度logistic回归并使用Huber-White聚类稳健标准误；ANOVA和卡方检验结构等价性。

- main_result_cn：injunctive显著提高96%，descriptive单独不显著，combined显著提高295%且高于单用；强度到625递增、3125回落。

- argumentative_role_cn：为主要假设提供因果证据，同时暴露H2的异常并形成后续研究的理由。

- remaining_uncertainty_cn：descriptive messages可能同时包含正负特征，因为被标记的帖子可能为真也可能为假，无法分离。

- link_to_next_phase_cn：作者推断descriptive单独无效可能源于混杂的正负descriptive信息，因此设计Study 2专门分离。

##### evidence_pointers

1. Table 1

2. Table 2

3. H1-H4结果段

4. Study 1 Participants/Treatments

#### 2. Study 1中的descriptive强度后验分析

- order：2

- name_cn：Study 1中的descriptive强度后验分析

- question_cn：在combined处理中，descriptive强度是否对每个假新闻帖的举报概率产生倒U型影响？

- inputs_and_setting_cn：combined处理中82名参与者看到的410条假新闻帖子级观测；举报人数为5、25、125、625、3125五档，另有随机10%以内的抖动。

- designed_or_compared_object_cn：该帖被放置的举报人数级别。

- baseline_control_or_counterfactual_cn：举报人数为0（无descriptive信号）。

##### objective_metrics

1. 单帖是否被举报的二元结果

2. 各强度与baseline的odds ratio

- analysis_method_cn：logistic回归，strength作为有序因子，使用Huber-White聚类标准误。

- main_result_cn：从5到625举报几率显著递增（odds从2.06到3.69），3125时下降到1.77且与baseline差异不显著。

- argumentative_role_cn：专门验证H4，为descriptive规范强度设置阈值边界。

- remaining_uncertainty_cn：帖级特征（标题、来源）未控制；R²低，许多其他因素未建模。

- link_to_next_phase_cn：该结果支撑descriptive强度边界解释，同时提示过高强度会回火，但并未解决descriptive单独无效的问题。

##### evidence_pointers

1. Table 2

2. H4结果段

3. Online Supplemental Appendix I

#### 3. Study 2：正负descriptive消息的分离实验

- order：3

- name_cn：Study 2：正负descriptive消息的分离实验

- question_cn：排除混杂后，descriptive messages（正面或负面）是否单独影响假新闻举报行为？

- inputs_and_setting_cn：157名通过不同Facebook群招募的参与者；在Study 1基础上增强了假新闻与非假新闻的可区分度；新闻流与Study 1类似。

- designed_or_compared_object_cn：control（无descriptive消息）、positive descriptive（所有假新闻被标记）、negative descriptive（所有真新闻被标记）三种处理。

- baseline_control_or_counterfactual_cn：control组作为baseline；并与Study 1 control组进行可比性检验。

##### objective_metrics

1. 举报假新闻数量

2. 举报真新闻数量

- analysis_method_cn：有序logistic回归；卡方检验比较Study 1与Study 2的control组。

- main_result_cn：positive descriptive的odds增加36%但不显著，negative descriptive的odds仅增加1%且不显著；descriptive单独无效应得到重复。

- argumentative_role_cn：排除正负混杂解释，巩固H2不成立，并收集举报动机/障碍数据。

- remaining_uncertainty_cn：无更多关于descriptive单独效果的不确定性，但动机调查为探索性。

- link_to_next_phase_cn：结果与动机调查一起进入讨论，用于解释社会规范干预的条件和设计建议。

##### evidence_pointers

1. Table 3

2. Study 2 Results

3. 表4

#### 4. Study 2中的举报动机与障碍调查

- order：4

- name_cn：Study 2中的举报动机与障碍调查

- question_cn：用户举报或不举报假新闻的主要动机和障碍是什么？

- inputs_and_setting_cn：74名表示会举报的参与者和83名表示不会举报的参与者；5级李克特量表和自由文本。

- designed_or_compared_object_cn：预选的10项动机因子、9项障碍因子以及自由文本补充。

- baseline_control_or_counterfactual_cn：无对照组；描述性统计。

##### objective_metrics

1. 各因子均值、中位数、标准差

2. 自由文本出现的新障碍

- analysis_method_cn：描述性统计和自由文本归纳。

- main_result_cn：主要动机是避免负面后果、帮助他人形成正确观点、正确新闻景观；主要障碍是不相信举报有效、自认被动消费者；补充发现缺乏责任感和自身不确定性。

- argumentative_role_cn：为injunctive消息措辞和平台激励设计提供实证素材，解释为什么举报率低。

- remaining_uncertainty_cn：自我报告不能作为实际行为证据；未进入因果推断。

- link_to_next_phase_cn：在实践建议中用这些因子说明如何设计规范消息。

##### evidence_pointers

1. Table 4

2. Study 2 Procedures/Results

## 各部分修辞架构

### abstract_moves

1. CONTEXT

2. RQ_OR_OBJECTIVE

3. THEORY_INTRO

4. STUDY_OVERVIEW

5. RESULT

6. CONTRIBUTION

### introduction_moves

1. PHENOMENON

2. CONTEXT

3. PHENOMENON

4. RQ_OR_OBJECTIVE

5. THEORY_INTRO

6. LIMITATION

7. PRIOR_KNOWLEDGE

8. GAP

9. RQ_OR_OBJECTIVE

10. STUDY_OVERVIEW

11. RESULT

12. CONTRIBUTION

### theory_and_knowledge_moves

1. PRIOR_KNOWLEDGE

2. LIMITATION

3. CONTEXT

4. LIMITATION

5. PRIOR_KNOWLEDGE

6. THEORY_INTRO

7. THEORY_PROPOSITION

8. HYPOTHESIS_OR_PROPOSITION

9. MECHANISM

### artifact_design_moves

1. METHOD_JUSTIFICATION

2. DESIGN_FEATURE

3. DESIGN_FEATURE

4. DESIGN_FEATURE

5. REQUIREMENT

6. DESIGN_FEATURE

7. METHOD_JUSTIFICATION

8. BENCHMARK_OR_CONTRAST

### evaluation_moves

1. METHOD_JUSTIFICATION

2. BENCHMARK_OR_CONTRAST

3. RESULT

4. ROBUSTNESS_OR_BOUNDARY_TEST

5. TRANSITION

### discussion_and_contribution_moves

1. CONTRIBUTION

2. MECHANISM

3. BOUNDARY_CONDITION

4. LIMITATION_AND_FUTURE

5. CONTRIBUTION

## 理论/知识到设计的翻译

### 知识/理论基础

1. 社会规范理论：injunctive与descriptive norms（Cialdini等）

2. 规范性行为焦点理论（focus theory of normative conduct）

3. 旁观者效应与责任分散

4. 假新闻传播与IS干预研究

- 理论—设计耦合：direct

- 耦合判定理由：核心设计特征（inj message的放置与确认、descriptive message的举报人数、五级强度、组合条件）均由理论构念和焦点理论直接推导而来，并通过实验直接检验；仅少量实现细节如随机抖动和材料选择属于工程性处理。

- 理论到设计翻译链：社会规范理论定义injunctive和descriptive两类规范，并指出它们通过社会奖惩和启发式影响行为；焦点理论强调规范需处于注意力焦点且descriptive规范可将注意力引向injunctive规范；旁观者效应说明社交媒体环境中存在责任分散。这些理论命题被转化为界面设计要求：需要显示‘举报是值得做’的信息并确保用户注意、需要显示他人举报行为、需要两类消息并存、需要设置不同他人举报强度。最终形成实验中的四种处理组合和五级descriptive强度，并通过随机分配和行为测量检验对举报数量的影响。

### mapping_table

#### 1. 1

- theory_or_knowledge_claim_cn：Injunctive norms通过社会赞许/惩罚影响行为，且需要处于注意力焦点。

- mechanism_cn：用户意识到举报假新闻是社交环境赞许的行为，产生道德顺从动机。

- design_requirement_cn：界面需要一种明确传递‘应该举报’信息的机制，并确保用户看到。

- artifact_choice_cn：新闻流顶部显示injunctive SN message，必须点击确认才能继续。

- evaluated_contrast_cn：inj message存在 vs 不存在。

- objective_result_cn：举报假新闻odds提高96%，显著；支持H1。

##### evidence_pointers

1. Table 1 control vs injunctive regression

2. H1结果段

#### 2. 2

- theory_or_knowledge_claim_cn：Descriptive norms通过他人行为提供启发式，影响模糊情境下的决策。

- mechanism_cn：用户看到其他用户已经举报某帖，可能将其作为正确行为线索。

- design_requirement_cn：需要在帖子层面显示其他用户的举报行为。

- artifact_choice_cn：在新闻帖上增加‘已有X人举报’的消息，可选不同数量。

- evaluated_contrast_cn：descriptive message存在 vs 不存在。

- objective_result_cn：odds提高58%但不显著；Study 2正负descriptive均不显著；H2不支持。

##### evidence_pointers

1. Table 1

2. Table 3

#### 3. 3

- theory_or_knowledge_claim_cn：焦点理论认为descriptive norm可以将注意力指向injunctive norm，二者结合效应更强。

- mechanism_cn：descriptive message不断提醒injunctive message描述的理想行为。

- design_requirement_cn：需要在同一界面同时提供两种类型消息。

- artifact_choice_cn：combined treatment：既有顶部injunctive message，又有部分帖子带descriptive report count。

- evaluated_contrast_cn：combined vs control、vs单独injunctive、vs单独descriptive。

- objective_result_cn：odds比control高295%，比inj高101%，比desc高150%，均显著；支持H3。

##### evidence_pointers

1. Table 1 rebase模型

2. H3结果段

#### 4. 4

- theory_or_knowledge_claim_cn：Descriptive norm强度越大，行为示范越强；但Wong等指出举报行为动机依赖于感知收益，别人已大量举报可能降低自己行动的感知价值。

- mechanism_cn：强度提高先吸引注意力提高举报；超过阈值后感觉到‘已经有人处理’而减少举报。

- design_requirement_cn：需要设计不同强度的descriptive message，并测量对单帖举报概率的影响。

- artifact_choice_cn：将举报人数设为5、25、125、625、3125五个级别。

- evaluated_contrast_cn：各强度 vs 无descriptive（0）以及强度之间。

- objective_result_cn：从5到625显著递增，3125回落且与baseline无显著差异，倒U型；支持H4。

##### evidence_pointers

1. Table 2 post-level logistic回归

2. H4结果段

## 评价逻辑

### evaluation_modes

1. 在线行为实验（between-subject treatment manipulation）

2. post-level logistic回归分析 within-subject strength manipulation

3. 控制组对比与rebase分析

4. 补充问卷探索举报动机与障碍

5. 稳健性检查（参与者awareness控制）

- why_these_evaluations_cn：需要因果检验SN messages对举报行为的效果，因此采用随机分配和受控新闻流；由于举报数是离散计数且残差非正态，采用有序logistic回归；为了检验descriptive强度需要帖子级重复观测和聚类稳健标准误；为了排除H2不显著是因为正负混杂，需要Study 2加入正负descriptive分离条件；动机调查用于为平台设计提供解释性输入。

- benchmark_and_contrast_chain_cn：以control为baseline检验injunctive、descriptive、combined；再将combined重设为baseline比较与单用条件；Study 2以control为baseline比较positive和negative descriptive；还通过卡方检验确认Study 1与Study 2的control组行为可比。

### claim_evidence_ledger

#### 1. injunctive SN message增加假新闻举报。

- claim_cn：injunctive SN message增加假新闻举报。

- evidence_cn：Study 1有序logistic回归：odds ratio=1.962，p=.039，小效应。

- support_level_cn：支持

#### 2. descriptive SN message单独增加假新闻举报。

- claim_cn：descriptive SN message单独增加假新闻举报。

- evidence_cn：Study 1 odds ratio=1.578不显著；Study 2 positive odds=1.326不显著，negative odds=1.010不显著。

- support_level_cn：不支持

#### 3. combined比control和单用都提高举报。

- claim_cn：combined比control和单用都提高举报。

- evidence_cn：Study 1 combined odds vs control=3.947，rebase比较均显著。

- support_level_cn：支持

#### 4. descriptive强度影响举报概率呈倒U型。

- claim_cn：descriptive强度影响举报概率呈倒U型。

- evidence_cn：Table 2：5/25/125/625强度系数显著递增，3125不显著且低于625。

- support_level_cn：支持，但R²低且未控制帖级特征

#### 5. SNs会导致更多真实新闻被误报。

- claim_cn：SNs会导致更多真实新闻被误报。

- evidence_cn：Study 1 combined处理中真新闻报告显著增加；inj/desc不显著或边缘显著。

- support_level_cn：部分支持/有限证据

#### 6. SN messages可长期用于真实社交平台。

- claim_cn：SN messages可长期用于真实社交平台。

- evidence_cn：仅有受控在线实验，举报按钮已简化，非真实平台。

- support_level_cn：未直接检验

- internal_validity_strategy_cn：随机分配参与者到处理条件；对四组进行ANOVA和卡方结构等价检验；使用受控新闻流排除点赞、评论、分享等社会影响线索；随机化帖子顺序；教程确保参与者知道举报功能；Brant检验比例优势假设；H4使用聚类稳健标准误。

- external_validity_strategy_cn：采用Facebook风格新闻流增强界面生态效度；使用真实传播过的假新闻作为刺激；通过Facebook学生群招募活跃社交媒体用户；在线而非实验室；Study 2更新材料并增强真假差异；作者同时明确样本和材料对推广的限制。

- what_is_not_actually_tested_cn：真实平台上的实际举报流程、长期保持性、不同年龄/国家/平台用户的行为、descriptive强度在其他处理中的完整边界、真实误报成本、以及即时行为是否会转化为持续平台治理效果。

## 贡献闭环

- technical_claim_cn：无算法或技术性能主张；核心是行为干预的统计显著效应。

- artifact_claim_cn：特定SN消息设计（顶部injunctive message、帖级举报人数、组合呈现）能够增加用户举报假新闻的数量。

- mechanism_claim_cn：injunctive通过社会赞许/道德评价影响行为；descriptive通过注意力聚焦和启发式影响；combined中descriptive持续提醒injunctive；强度过高时感知收益下降导致回火。

- boundary_claim_cn：descriptive单独无效；在德国、年轻、学生为主且通过Facebook招募的用户样本中成立；descriptive强度超过某阈值后有利效果逆转；真实新闻误报风险存在但数量低于假新闻。

- reusable_design_knowledge_cn：平台界面可嵌入injunctive norm message并搭配descriptive report count；应避免过高举报人数展示；可考虑隐藏精确数字转用文章/来源评分；简化举报按钮可降低操作障碍；injunctive措辞可参考利他与避免负面后果等动机。

- theoretical_contribution_cn：将社会规范理论和焦点理论扩展到假新闻举报情境；显示descriptive norms在社交媒体举报场景中单独无效且存在倒U边界；补充了IS领域关于假新闻的社会技术干预研究，明确报告行为作为此前干预研究缺口的补充。

- how_discussion_closes_intro_gap_cn：引言质疑SNs是否适用于社交媒体及其净效应未知；讨论用两个实验回答：injunctive和combined有效，descriptive单独无效，并解释descriptive强度阈值与感知收益机制，从而闭合缺口并给出边界。

- overclaim_or_unsupported_leaps_cn：将combined中descriptive的附加效应完全归因于注意力聚焦可能超出直接证据；从简化举报按钮的人工实验推广到真实平台存在跳跃；认为整体净效应有利是基于误报数量较低，但未系统量化误报的社会成本。

## 句级写作动作图谱

### 1. 摘要第1段第1句

- order：1

- section：Abstract

- locator：摘要第1段第1句

- move_code：CONTEXT

- paraphrase_cn：指出假新闻为社会带来巨大威胁和严重负面后果。

- rhetorical_function_cn：立即确立研究紧迫性。

- depends_on_cn：无。

- sets_up_cn：引出提高用户举报行为的必要性。

- evidence_pointer：摘要首句

### 2. 摘要第1段第2句

- order：2

- section：Abstract

- locator：摘要第1段第2句

- move_code：RQ_OR_OBJECTIVE

- paraphrase_cn：研究如何鼓励人们举报假新闻并支持平台打击虚假信息。

- rhetorical_function_cn：明确研究意图。

- depends_on_cn：由威胁背景引出。

- sets_up_cn：为后文假设作铺垫。

- evidence_pointer：摘要第二句

### 3. 摘要第1段第3句

- order：3

- section：Abstract

- locator：摘要第1段第3句

- move_code：THEORY_INTRO

- paraphrase_cn：基于社会心理学提出假设：社会规范鼓励用户举报假新闻。

- rhetorical_function_cn：引入理论视角。

- depends_on_cn：需要解释如何激励用户。

- sets_up_cn：引入injunctive和descriptive norms概念。

- evidence_pointer：摘要第三句

### 4. 摘要第1段第4-5句

- order：4

- section：Abstract

- locator：摘要第1段第4-5句

- move_code：STUDY_OVERVIEW

- paraphrase_cn：通过两个实验，在同时包含真假新闻的新闻流中呈现两种规范消息。

- rhetorical_function_cn：预告实验设计。

- depends_on_cn：理论假设需要实验检验。

- sets_up_cn：为结果句铺垫。

- evidence_pointer：摘要第四、五句

### 5. 摘要第1段第6-8句

- order：5

- section：Abstract

- locator：摘要第1段第6-8句

- move_code：RESULT

- paraphrase_cn：结果显示injunctive规范提高举报率，descriptive单独无效果，组合效果最大。

- rhetorical_function_cn：预告核心发现。

- depends_on_cn：实验证据。

- sets_up_cn：强调社会规范是有前景的社会技术解药。

- evidence_pointer：摘要第六至八句

### 6. 引言第1段第1-3句

- order：6

- section：Introduction

- locator：引言第1段第1-3句

- move_code：PHENOMENON

- paraphrase_cn：用童话开篇说明假新闻不像童话那样标明虚假，却传播更广更快。

- rhetorical_function_cn：用比喻唤起现象直观。

- depends_on_cn：无。

- sets_up_cn：建立假新闻隐蔽而危险的背景。

- evidence_pointer：引言第一段

### 7. 引言第2段第1-4句

- order：7

- section：Introduction

- locator：引言第2段第1-4句

- move_code：CONTEXT

- paraphrase_cn：越来越多人在社交媒体获取新闻，社交媒体缺乏验证机制，诸多领域出现假新闻并影响观点与行动。

- rhetorical_function_cn：把假新闻提升为社会问题。

- depends_on_cn：第1段的流行性。

- sets_up_cn：说明为什么需要干预。

- evidence_pointer：引言第二段

### 8. 引言第3段第1-5句

- order：8

- section：Introduction

- locator：引言第3段第1-5句

- move_code：PHENOMENON

- paraphrase_cn：平台面临压力但用户极少使用举报功能，作者自己的调查也证实这一点。

- rhetorical_function_cn：将一般社会问题收缩到具体的低举报率。

- depends_on_cn：平台依赖用户举报作为机制。

- sets_up_cn：提出如何激励用户的问题。

- evidence_pointer：引言第三段

### 9. 引言第3段末句

- order：9

- section：Introduction

- locator：引言第3段末句

- move_code：RQ_OR_OBJECTIVE

- paraphrase_cn：问题自然出现：如何激励用户举报假新闻？

- rhetorical_function_cn：确立研究问题雏形。

- depends_on_cn：低举报率现象。

- sets_up_cn：为理论引入提供目标。

- evidence_pointer：引言第三段末句

### 10. 引言第4段第1-4句

- order：10

- section：Introduction

- locator：引言第4段第1-4句

- move_code：THEORY_INTRO

- paraphrase_cn：社会心理学认为社会规范强烈影响行为并分为injunctive和descriptive两类，先前研究也表明其在亲社会行为中有效。

- rhetorical_function_cn：引入社会规范作为潜在方案。

- depends_on_cn：需要解释行为来源。

- sets_up_cn：引出是否适用于社交媒体的疑问。

- evidence_pointer：引言第四段

### 11. 引言第5段第1-5句

- order：11

- section：Introduction

- locator：引言第5段第1-5句

- move_code：LIMITATION

- paraphrase_cn：但旁观者效应和规范消息回火可能使社会规范在社交媒体中失效甚至产生负效应，因此净效应未知。

- rhetorical_function_cn：划定研究缺口。

- depends_on_cn：理论背景和低举报率现象。

- sets_up_cn：说明为什么需要新研究。

- evidence_pointer：引言第五段

### 12. 引言第6段第1-4句

- order：12

- section：Introduction

- locator：引言第6段第1-4句

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：IS学者已研究界面微调能促使对假新闻反思，但尚未研究社会规范或举报行为本身。

- rhetorical_function_cn：定位与已有IS研究的区别。

- depends_on_cn：前文缺口。

- sets_up_cn：正式提出研究问题。

- evidence_pointer：引言第六段

### 13. 引言第6段末句

- order：13

- section：Introduction

- locator：引言第6段末句

- move_code：RQ_OR_OBJECTIVE

- paraphrase_cn：提出RQ：injunctive和descriptive social norm messages作为界面组成部分能否改善用户举报假新闻行为。

- rhetorical_function_cn：精确化研究问题。

- depends_on_cn：前文缺口。

- sets_up_cn：假设和实验设计。

- evidence_pointer：引言第六段末句

### 14. 引言第7段第1-3句

- order：14

- section：Introduction

- locator：引言第7段第1-3句

- move_code：STUDY_OVERVIEW

- paraphrase_cn：作者预告将推导假设、做两个在线实验，并提示descriptive单独无效的意外结果。

- rhetorical_function_cn：预告研究路径和关键发现。

- depends_on_cn：RQ。

- sets_up_cn：结果和贡献。

- evidence_pointer：引言第七段

### 15. 引言第8段第1句

- order：15

- section：Introduction

- locator：引言第8段第1句

- move_code：CONTRIBUTION

- paraphrase_cn：声明对研究与实践的双重贡献，尤其响应社会技术干预假新闻的呼吁。

- rhetorical_function_cn：提前定位贡献。

- depends_on_cn：结果。

- sets_up_cn：全文贡献主张。

- evidence_pointer：引言第八段

### 16. 第一段第1-4句

- order：16

- section：Theoretical Background, Fake News section

- locator：第一段第1-4句

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：定义假新闻为故意且可验证的虚假信息，具有不真实性和欺骗性。

- rhetorical_function_cn：确立概念边界。

- depends_on_cn：引言中的RQ。

- sets_up_cn：讨论其危害和干预必要性。

- evidence_pointer：理论与假设发展部分第一段

### 17. 第三段第1-4句

- order：17

- section：Theoretical Background, Fake News section

- locator：第三段第1-4句

- move_code：LIMITATION

- paraphrase_cn：纠正错误信息难以改变信念，重复会因熟悉度偏见强化相信。

- rhetorical_function_cn：解释为什么遏制传播比纠正更重要。

- depends_on_cn：假新闻影响。

- sets_up_cn：为举报干预提供理由。

- evidence_pointer：假新闻小节第三段

### 18. 第一段第1-6句

- order：18

- section：Theoretical Background, Fake News in Social Media section

- locator：第一段第1-6句

- move_code：CONTEXT

- paraphrase_cn：社交媒体通过广泛受众、低门槛、高速传播和缺乏权威验证四个特征加剧假新闻传播。

- rhetorical_function_cn：解释平台为何脆弱。

- depends_on_cn：假新闻定义。

- sets_up_cn：为界面干预提供背景。

- evidence_pointer：假新闻与社交媒体小节第一段

### 19. 第三段第1-4句

- order：19

- section：Theoretical Background, Fake News in Social Media section

- locator：第三段第1-4句

- move_code：LIMITATION

- paraphrase_cn：用户判断真实性存在弱点，确认偏误和认知失调导致难以客观处理信息。

- rhetorical_function_cn：说明不能只靠用户辨别。

- depends_on_cn：平台脆弱性。

- sets_up_cn：需要额外机制。

- evidence_pointer：同一小节第三段

### 20. 第四段第1-4句

- order：20

- section：Theoretical Background, Fake News in Social Media section

- locator：第四段第1-4句

- move_code：LIMITATION

- paraphrase_cn：旁观者效应和在线责任分散会降低举报意愿，因此必须让用户看到举报是值得的。

- rhetorical_function_cn：为社会规范干预提供行为学缺口。

- depends_on_cn：之前描述的用户弱点。

- sets_up_cn：与社会规范理论对接。

- evidence_pointer：同一小节第四段

### 21. 第一段第1-4句

- order：21

- section：Theoretical Background, Countermeasures section

- locator：第一段第1-4句

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：新兴IS研究通过来源展示、来源评分和反思评价改善用户对假新闻的认知参与。

- rhetorical_function_cn：总结已有干预路径。

- depends_on_cn：说明已有进展。

- sets_up_cn：指出未涉及举报行为。

- evidence_pointer：对策小节第一段

### 22. 第三至五段

- order：22

- section：Theoretical Background, Countermeasures section

- locator：第三至五段

- move_code：LIMITATION

- paraphrase_cn：现有自动检测和事实核查依赖预选，平台需要用户举报作为触发；但用户举报数据缺乏。

- rhetorical_function_cn：建立以用户举报为焦点的必要性。

- depends_on_cn：治理机制描述。

- sets_up_cn：为假设选择举报行为作依据。

- evidence_pointer：对策小节第三至五段

### 23. 第一段第1-5句

- order：23

- section：Theoretical Background, Social Norms section

- locator：第一段第1-5句

- move_code：THEORY_INTRO

- paraphrase_cn：定义社会规范为个体对情境中典型和认可行为的信念，分为injunctive（应该做什么）和descriptive（别人做什么）。

- rhetorical_function_cn：介绍核心理论构念。

- depends_on_cn：需要理论工具。

- sets_up_cn：推导H1。

- evidence_pointer：社会规范小节第一段

### 24. 第一段第6-8句

- order：24

- section：Theoretical Background, Social Norms section

- locator：第一段第6-8句

- move_code：THEORY_PROPOSITION

- paraphrase_cn：Injunctive norms通过社会奖惩和道德评价影响行为；当注意力聚焦于规范时更可能遵循。

- rhetorical_function_cn：提供injunctive机制。

- depends_on_cn：焦点理论。

- sets_up_cn：H1。

- evidence_pointer：同一段后半

### 25. H1条文

- order：25

- section：Theoretical Background, Social Norms section

- locator：H1条文

- move_code：HYPOTHESIS_OR_PROPOSITION

- paraphrase_cn：H1：injunctive message存在会增加假新闻举报数量。

- rhetorical_function_cn：提出第一个可检验假设。

- depends_on_cn：理论推导。

- sets_up_cn：Study 1检验。

- evidence_pointer：H1条文

### 26. 第二段第1-4句

- order：26

- section：Theoretical Background, Social Norms section

- locator：第二段第1-4句

- move_code：THEORY_PROPOSITION

- paraphrase_cn：Descriptive norms提供启发式，在不确定情境中帮助决策；先前在减少乱扔垃圾等领域有效。

- rhetorical_function_cn：为descriptive效果提供机制和先例。

- depends_on_cn：社会规范理论。

- sets_up_cn：H2。

- evidence_pointer：社会规范小节第二段

### 27. H2条文

- order：27

- section：Theoretical Background, Social Norms section

- locator：H2条文

- move_code：HYPOTHESIS_OR_PROPOSITION

- paraphrase_cn：H2：descriptive message存在会增加假新闻举报数量。

- rhetorical_function_cn：提出第二个假设。

- depends_on_cn：理论推导。

- sets_up_cn：实验验证。

- evidence_pointer：H2条文

### 28. 第三段第1-4句

- order：28

- section：Theoretical Background, Social Norms section

- locator：第三段第1-4句

- move_code：MECHANISM

- paraphrase_cn：以往回收和毛巾重用研究表明联合使用两类规范效果最强，因为descriptive可聚焦注意力到injunctive。

- rhetorical_function_cn：为组合假设提供机制。

- depends_on_cn：焦点理论。

- sets_up_cn：H3。

- evidence_pointer：社会规范小节第三段

### 29. H3条文

- order：29

- section：Theoretical Background, Social Norms section

- locator：H3条文

- move_code：HYPOTHESIS_OR_PROPOSITION

- paraphrase_cn：H3：inj和desc同时存在比只用一种导致更多举报。

- rhetorical_function_cn：提出第三个假设。

- depends_on_cn：先前理论。

- sets_up_cn：实验检验。

- evidence_pointer：H3条文

### 30. 第四段第1-5句

- order：30

- section：Theoretical Background, Social Norms section

- locator：第四段第1-5句

- move_code：MECHANISM

- paraphrase_cn：descriptive norm强度越高越被感知为标准行为，但与injunctive结合时，过高强度可能让人觉得自己的举报不再有额外收益，产生反向作用。

- rhetorical_function_cn：引入非单调效应。

- depends_on_cn：知觉收益机制。

- sets_up_cn：H4。

- evidence_pointer：社会规范小节第四段

### 31. H4条文

- order：31

- section：Theoretical Background, Social Norms section

- locator：H4条文

- move_code：HYPOTHESIS_OR_PROPOSITION

- paraphrase_cn：H4：在injunctive存在时，descriptive强度对举报概率呈倒U型影响。

- rhetorical_function_cn：提出第四个假设。

- depends_on_cn：理论。

- sets_up_cn：Study 1 strength分析。

- evidence_pointer：H4条文

### 32. 末段

- order：32

- section：Theoretical Background, Social Norms section

- locator：末段

- move_code：LIMITATION

- paraphrase_cn：作者声明研究重点不是真实新闻被误报，但仍会将此副作用纳入分析。

- rhetorical_function_cn：预先界定负效应并设置检验。

- depends_on_cn：举报机制具有误报副作用。

- sets_up_cn：为后续by-catch结果铺路。

- evidence_pointer：社会规范小节末段

### 33. Participants段

- order：33

- section：Study 1

- locator：Participants段

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：通过Facebook学生群招募活跃用户，在线实验被视为提升生态效度的选择。

- rhetorical_function_cn：说明样本和情境选择理由。

- depends_on_cn：需要对比实验。

- sets_up_cn：描述样本特征。

- evidence_pointer：Study 1 Participants段

### 34. Task段

- order：34

- section：Study 1

- locator：Task段

- move_code：DESIGN_FEATURE

- paraphrase_cn：自研新闻流模仿Facebook，排除点赞评论分享等社会线索，并添加简化举报按钮。

- rhetorical_function_cn：设计可控而逼真的实验环境。

- depends_on_cn：需要操纵SN消息而排除其他社会影响。

- sets_up_cn：描述新闻帖子结构。

- evidence_pointer：Study 1 Task段

### 35. Task段后部

- order：35

- section：Study 1

- locator：Task段后部

- move_code：DESIGN_FEATURE

- paraphrase_cn：新闻流包含5条假新闻、5条真新闻和5条中性帖，并以随机顺序展示。

- rhetorical_function_cn：建立标准化刺激集。

- depends_on_cn：真实主义需求。

- sets_up_cn：操纵和指标定义。

- evidence_pointer：Study 1 Task段后部

### 36. Treatments段

- order：36

- section：Study 1

- locator：Treatments段

- move_code：DESIGN_FEATURE

- paraphrase_cn：采用2x2被试间设计：control、injunctive、descriptive、combined；descriptive条件内部有5级强度。

- rhetorical_function_cn：生成H1-H4所需的条件比较。

- depends_on_cn：理论假设。

- sets_up_cn：统计比较。

- evidence_pointer：Treatments段

### 37. Independent Variables段

- order：37

- section：Study 1

- locator：Independent Variables段

- move_code：REQUIREMENT

- paraphrase_cn：为确保SNs被感知和可信，injunctive message放在新闻流开头并要求点击确认，descriptive message显示举报人数。

- rhetorical_function_cn：将注意力聚焦要求操作化为具体功能。

- depends_on_cn：焦点理论和可信性要求。

- sets_up_cn：对差异的效应估计。

- evidence_pointer：Independent Variables段

### 38. Independent Variables段

- order：38

- section：Study 1

- locator：Independent Variables段

- move_code：DESIGN_FEATURE

- paraphrase_cn：descriptive强度设为5、25、125、625、3125，并加入随机10%以内的波动以避免被识破模式。

- rhetorical_function_cn：实现强度操纵并防止参与者猜出实验意图。

- depends_on_cn：需要覆盖宽谱。

- sets_up_cn：H4检验。

- evidence_pointer：Independent Variables段

### 39. Dependent Variables段

- order：39

- section：Study 1

- locator：Dependent Variables段

- move_code：DESIGN_FEATURE

- paraphrase_cn：主要因变量为报告假新闻数量，次要为报告真新闻数量。

- rhetorical_function_cn：既测目标行为又测误报副作用。

- depends_on_cn：研究目标。

- sets_up_cn：回归分析。

- evidence_pointer：Dependent Variables段

### 40. Procedures段

- order：40

- section：Study 1

- locator：Procedures段

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：先教程说明举报功能，再让参与者在自然交互run中自由浏览，最后fake assessment run检查其能否区分真假。

- rhetorical_function_cn：确保行为测量不是因不知道功能而失败。

- depends_on_cn：需要真实的交互行为。

- sets_up_cn：区分注意与能力解释。

- evidence_pointer：Procedures段

### 41. Results第一段

- order：41

- section：Study 1

- locator：Results第一段

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：由于举报数是0-5的整数且残差非正态，采用有序logistic回归并做Brant检验。

- rhetorical_function_cn：说明统计模型选择。

- depends_on_cn：数据特征。

- sets_up_cn：表1结果。

- evidence_pointer：Results第一段

### 42. Results第一段附近

- order：42

- section：Study 1

- locator：Results第一段附近

- move_code：BENCHMARK_OR_CONTRAST

- paraphrase_cn：使用control作为baseline，并通过对combined的rebase来比较combined与单独injunctive/descriptive。

- rhetorical_function_cn：建立条件间相对比较的基准。

- depends_on_cn：有序logistic回归。

- sets_up_cn：H1/H2/H3的效应估计。

- evidence_pointer：Results第一段及表1

### 43. H1结果段

- order：43

- section：Study 1

- locator：H1结果段

- move_code：RESULT

- paraphrase_cn：inj message显著提高举报假新闻odds约96%，支持H1。

- rhetorical_function_cn：给出第一个假设结论。

- depends_on_cn：表1回归。

- sets_up_cn：验证理论有效性。

- evidence_pointer：H1结果段

### 44. H2结果段

- order：44

- section：Study 1

- locator：H2结果段

- move_code：RESULT

- paraphrase_cn：descriptive仅提高58% odds但不显著，H2未获支持，且真实新闻误报有边缘性增加。

- rhetorical_function_cn：报告未支持的假设。

- depends_on_cn：表1。

- sets_up_cn：引出对descriptive实现方式的分析。

- evidence_pointer：H2结果段

### 45. H2结果段末

- order：45

- section：Study 1

- locator：H2结果段末

- move_code：TRANSITION

- paraphrase_cn：作者推测是因为descriptive随机标记真假新闻，对多数参与者产生混杂的正负descriptive信息，因此需要Study 2分离。

- rhetorical_function_cn：为后续研究铺设理由。

- depends_on_cn：H2不显著。

- sets_up_cn：Study 2设计。

- evidence_pointer：H2结果段末

### 46. H3结果段

- order：46

- section：Study 1

- locator：H3结果段

- move_code：RESULT

- paraphrase_cn：combined相对control提高295%且显著，同时显著高于单独inj和desc，支持H3；但也显著增加真实新闻误报。

- rhetorical_function_cn：验证组合效应和副作用。

- depends_on_cn：表1 rebase。

- sets_up_cn：讨论整体净效应。

- evidence_pointer：H3结果段

### 47. H4结果段

- order：47

- section：Study 1

- locator：H4结果段

- move_code：RESULT

- paraphrase_cn：post-level logistic显示descriptive强度到625为止递增，3125时回落且与baseline无显著差异，支持倒U型H4。

- rhetorical_function_cn：验证强度边界。

- depends_on_cn：表2。

- sets_up_cn：讨论阈值机制。

- evidence_pointer：H4结果段

### 48. Study 1末段

- order：48

- section：Study 1

- locator：Study 1末段

- move_code：TRANSITION

- paraphrase_cn：总结Study 1支持H1/H3/H4，未支持H2，因此需要Study 2继续测试H2。

- rhetorical_function_cn：明确阶段间累积关系。

- depends_on_cn：全部Study 1结果。

- sets_up_cn：Study 2。

- evidence_pointer：Study 1末段

### 49. Treatments段

- order：49

- section：Study 2

- locator：Treatments段

- move_code：DESIGN_FEATURE

- paraphrase_cn：将descriptive分为positive（只有假新闻被标记）和negative（只有真新闻被标记）两个处理，与control比较。

- rhetorical_function_cn：消除Study 1中正负混合的混淆。

- depends_on_cn：H2失败原因分析。

- sets_up_cn：再次检验H2。

- evidence_pointer：Study 2 Treatments段

### 50. Procedures段

- order：50

- section：Study 2

- locator：Procedures段

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：除相同流程外，增加了参与者对每条新闻的造假感知评分和举报动机障碍问卷。

- rhetorical_function_cn：扩展测量以解释行为。

- depends_on_cn：需要补充主观证据。

- sets_up_cn：表4结果。

- evidence_pointer：Study 2 Procedures段

### 51. Results段

- order：51

- section：Study 2

- locator：Results段

- move_code：RESULT

- paraphrase_cn：positive descriptive仅提高36% odds且不显著，negative几乎无变化；结论是descriptive单独无法改善举报。

- rhetorical_function_cn：再次验证H2不成立并排除正负解释。

- depends_on_cn：表3。

- sets_up_cn：讨论descriptive规范的边界。

- evidence_pointer：Study 2 Results段

### 52. Results段和表4

- order：52

- section：Study 2

- locator：Results段和表4

- move_code：RESULT

- paraphrase_cn：动机因子主要是内在利他和避免负面后果，障碍主要是不相信举报有效、仅作为消费者；自由文本补充缺乏责任感和自身不确定性。

- rhetorical_function_cn：为平台设计injunctive消息提供实际内容输入。

- depends_on_cn：问卷数据。

- sets_up_cn：实践建议。

- evidence_pointer：Table 4

### 53. 第1-2段

- order：53

- section：Discussion

- locator：第1-2段

- move_code：CONTRIBUTION

- paraphrase_cn：文章回应了假新闻社会技术干预的研究呼吁，证明SN消息能影响举报行为，但需注意真新闻作为副产品被误报。

- rhetorical_function_cn：将结果抽象为领域贡献并指出副作用。

- depends_on_cn：两个Study的结果。

- sets_up_cn：与已有研究比较。

- evidence_pointer：Discussion开头两段

### 54. 第4-5段

- order：54

- section：Discussion

- locator：第4-5段

- move_code：MECHANISM

- paraphrase_cn：组合效应最好，且descriptive message能持续提醒injunctive规范，因此同时更实用。

- rhetorical_function_cn：给组合结果提供机制解释并连接实际可用性。

- depends_on_cn：H3结果。

- sets_up_cn：descriptive强度阈值讨论。

- evidence_pointer：Discussion第四、五段

### 55. 第6段

- order：55

- section：Discussion

- locator：第6段

- move_code：BOUNDARY_CONDITION

- paraphrase_cn：descriptive强度阈值与感知收益下降有关，这与在线购物等场景的正相关存在边界。

- rhetorical_function_cn：界定descriptive规范在举报情境中的边界。

- depends_on_cn：H4结果。

- sets_up_cn：为未来研究指定阈值条件。

- evidence_pointer：Discussion第六段

### 56. 第一段

- order：56

- section：Contribution to Theory

- locator：第一段

- move_code：CONTRIBUTION

- paraphrase_cn：理论贡献一：SN messages作为界面引导有效但不总是有效；injunctive有效、descriptive单独无效、组合最强。

- rhetorical_function_cn：明确理论增量。

- depends_on_cn：两个Study。

- sets_up_cn：第二、第三贡献。

- evidence_pointer：Contribution to Theory第一段

### 57. 第二段

- order：57

- section：Contribution to Theory

- locator：第二段

- move_code：BOUNDARY_CONDITION

- paraphrase_cn：理论贡献二：overly strong descriptive SNs会回火，降低举报动机。

- rhetorical_function_cn：强调边界条件。

- depends_on_cn：H4。

- sets_up_cn：建议实践避免过高强度。

- evidence_pointer：Contribution to Theory第二段

### 58. 第三段

- order：58

- section：Contribution to Theory

- locator：第三段

- move_code：LIMITATION_AND_FUTURE

- paraphrase_cn：理论贡献三：未发现SNs对真新闻误报的显著总体负效应，但无法排除强descriptive下的误报。

- rhetorical_function_cn：诚实报告副作用的不确定性。

- depends_on_cn：by-catch分析。

- sets_up_cn：未来研究。

- evidence_pointer：Contribution to Theory第三段

### 59. 比较段

- order：59

- section：Contribution to Theory

- locator：比较段

- move_code：CONTRIBUTION

- paraphrase_cn：与已有IS干预互补，Moravec研究评估行为，本研究关注如何触发评估和举报行为。

- rhetorical_function_cn：定位本文独特贡献。

- depends_on_cn：IS文献。

- sets_up_cn：实践建议。

- evidence_pointer：Contribution to Theory比较段

### 60. 整段

- order：60

- section：Practical Implications

- locator：整段

- move_code：CONTRIBUTION

- paraphrase_cn：给平台建议：显示injunctive message、组合descriptive message、避免过高举报计数并考虑隐藏计数或显示评分。

- rhetorical_function_cn：将理论结果转化为设计知识。

- depends_on_cn：H1/H3/H4。

- sets_up_cn：结论。

- evidence_pointer：Practical Implications段

### 61. 整段

- order：61

- section：Limitations

- locator：整段

- move_code：LIMITATION_AND_FUTURE

- paraphrase_cn：承认样本、材料、平台和现实按钮简化带来的局限，并列出六个未来研究方向。

- rhetorical_function_cn：保护贡献不被过度一般化。

- depends_on_cn：研究证据范围。

- sets_up_cn：结论。

- evidence_pointer：Limitations段

### 62. 整段

- order：62

- section：Conclusion

- locator：整段

- move_code：CONTRIBUTION

- paraphrase_cn：总结：社会规范能引导用户举报假新闻，且只需在现有平台中加入SN消息，是以低成本对抗假新闻的可行工具。

- rhetorical_function_cn：最终贡献主张。

- depends_on_cn：全文。

- sets_up_cn：结束。

- evidence_pointer：Conclusion段

## 写作技术

- gap_construction_cn：先陈述假新闻在社交媒体的严重性，再叠加平台依赖用户举报但用户几乎不举报的实践矛盾，最后指出IS研究未探索社会规范或举报行为，从而形成明确而具体的研究缺口。

- signposting_cn：在Abstract、Introduction和每段假设前明确列出H1-H4；在每次结果后直接写‘supports H1/H3/H4’或‘not supported’；在Study 1末尾和Study 2开头间设置显式过渡。

- transition_logic_cn：段落间从宏观现象到平台机制再到IS对策，最后转入理论；Study间用‘由于H2未支持且可能的混杂正负descriptive信息’作为逻辑桥；讨论部分从实验结果返回理论主张和边界。

- claim_evidence_rhythm_cn：每段假设检验先给出理论推导，再报告数据结果与效应量，紧接着说明支持或不支持，最后解释可能机制；未支持的假设会在随后的Study或讨论中重新解释。

- benchmark_narrative_cn：将control作为无干预基准，使每个处理效果都能通过odds ratio直观呈现；对combined采用rebase作为基准以比较‘组合优于单用’；Study 2又用control作为基准，并通过control组可比性检验串联两个Study。

- theory_return_cn：讨论将descriptive单独无效、combined最有效和强度倒U分别归因于机制（道德评价、注意力聚焦、感知收益），从而把实验结果升华为理论命题而非一次性数据。

- contribution_positioning_cn：将贡献定位为‘响应IS研究假新闻社会技术干预的呼吁’，并与Moravec等评估行为研究互补，强调本文关注触发举报行为。

- novelty_protection_cn：通过同时报告descriptive无效和真实新闻误报副效应，展示研究诚实度；通过明确样本、材料和简化按钮局限，防止贡献被误读为普遍真理；通过提出阈值和边界条件，使结果具有可检验的结构而非一次性性能发现。

## 可复用研究与写作程序

### structure_steps

#### 1. 1

- step：1

- writing_job_cn：用具体现象建立现实问题，描述低举报率并要求激励。

- research_job_cn：收集假新闻危害、平台举报机制、现有干预的证据。

- required_evidence_cn：假新闻传播数据和举报机制证据。

- transition_to_next_cn：引出‘如何激励用户’的问题。

#### 2. 2

- step：2

- writing_job_cn：从社会心理学引入规范理论，定义构念、机制并推导假设。

- research_job_cn：选择合适理论构念、明确机制、写出可检验假设。

- required_evidence_cn：先前规范研究基础和本情境可迁移性。

- transition_to_next_cn：假设需要实验检验。

#### 3. 3

- step：3

- writing_job_cn：描述实验界面、消息实现、条件设计。

- research_job_cn：构建模拟新闻流和操作化SN消息。

- required_evidence_cn：操纵必须与理论构念对应且能被感知。

- transition_to_next_cn：报告实验实施和统计结果。

#### 4. 4

- step：4

- writing_job_cn：描述样本、程序、统计模型，报告假设检验结果。

- research_job_cn：随机分配、收集数据、回归建模。

- required_evidence_cn：样本特征、模型假设、结果表。

- transition_to_next_cn：不支持的假设需要解释并设计后续研究。

#### 5. 5

- step：5

- writing_job_cn：用新Study分离混淆，补充调查，验证并解释前阶段的未支持结果。

- research_job_cn：调整条件、重新实验、加入量表。

- required_evidence_cn：前阶段缺失的证据；控制组可比性。

- transition_to_next_cn：利用结果返回理论讨论和边界。

#### 6. 6

- step：6

- writing_job_cn：将结果抽象为理论贡献、实践建议和边界、局限。

- research_job_cn：区分支持/不支持、副作用、可推广范围。

- required_evidence_cn：各假设的证据等级和局限。

- transition_to_next_cn：收束全文。

### most_transferable_moves_cn

1. 把现实低参与率塑造成研究问题

2. 用规范理论推导具体假设

3. 操作化界面消息并确保注意力

4. 利用第二个Study解释第一个Study的未支持假设

5. 区分行为效果和边界条件

6. 在讨论中把实验结果提升为界面设计知识

### resource_intensive_or_nonstandard_parts_cn

1. 获取并改编真实假新闻帖子

2. 开发与Facebook相似新闻流

3. 招募两个样本的参与者

4. 在线实验的工程和问卷系统

5. 现场平台实验成本更高

### what_not_to_copy_superficially_cn

1. 只写社会规范有效而缺乏随机操纵和对照

2. 把descriptive单独无效当成普遍结论而不考虑情境

3. 忽略误报真实新闻和descriptive强度阈值

4. 声称可直接移植到真实平台而无现场验证

5. 把自报动机当作实际行为证据

- single_best_description_of_the_routine_cn：以低举报率这一现实缺口为起点，从社会心理学推导四个界面消息假设，通过两个在线实验逐项检验，并用第二个实验排除冲突解释，最终把行为效应升华为可复用的社会技术设计知识并明确其边界。

## 分析边界

OCR文本中存在少量拼写不一致（如efect等）及图表未完全可解析；无法提供精确页码，仅按章节/段落定位；附录信息只可推断，无法核验其具体内容。
