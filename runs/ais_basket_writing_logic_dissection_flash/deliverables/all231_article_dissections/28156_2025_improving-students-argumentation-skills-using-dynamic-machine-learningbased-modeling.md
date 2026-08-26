# Improving Students’ Argumentation Skills Using Dynamic Machine-Learning–Based Modeling

- 作者：Thiemo Wambsganss; Andreas Janson; Matthias Söllner; Ken Koedinger; Jan Marco Leimeister
- 年份 / 期刊：2025 / Information Systems Research
- DOI：10.1287/isre.2021.0615
- 源文件：28156_2025_improving-students-argumentation-skills-using-dynamic-machine-learningbased-modeling.md
- 论文主类型：theory_derived_artifact_experiment
- 主导写作弧线：problem_theory_design_test_return
- 置信度：0.85

## 文章级论证概况

- 核心问题：基于社会认知理论，动态机器学习建模（dynamic ML-based modeling）是否比脚本化建模、自适应支持和静态建模更能提高学生的论证写作能力，并且这种提升是否在复杂/简单任务、不同学习者经验水平以及三个月后的跨领域迁移中稳健存在？

- 制品与设计：作者构建了名为ArgueLearn的动态论证建模系统。系统采用服务导向架构，包括四个构件：论证标注方案、德文学生同行评审语料库、基于SVM的论证挖掘模块（识别claim/premise及支持关系）以及学生中心化界面。界面提供动态高亮、论证结构图、可读性/连贯性/说服力得分和按需分析反馈，而不是预先脚本化的输入结构或静态模型。

- 客观结果：Study 1中动态建模组客观论证质量5.08显著高于脚本建模组3.20（p<0.001），主观质量3.38显著高于2.79（p<0.05）；Study 2中动态建模在复杂任务（d=1.11）和简单任务（d=0.67）下客观质量均显著高于自适应支持，但主观质量大多不显著；Study 3中三个月动态建模组在迁移任务中客观质量4.04显著高于静态建模3.20（p=0.015）和无建模3.03（p=0.001），主观质量无显著差异。

- 核心贡献：作者声称，动态ML建模显著改善学习者的客观论证技能，且优于脚本化建模、传统自适应支持和静态建模；效果在复杂任务中更强，并适用于高低经验学习者；研究还表明社会认知理论可泛化到数学和科学之外的论证写作领域，为写作与技能支持系统设计提供了实证和设计知识。

- 整篇论证链：文章从论证技能在现代教育和职业中的重要性出发，指出现有大规模教学因缺乏个别化即时反馈而难以培养论证能力。作者将问题收缩为：已有技术辅助论证学习系统以脚本化建模和静态建模为主，新兴ML动态建模系统缺乏严格控制实验和长期现场检验。基于社会认知理论的行为建模和观察学习机制，作者提出动态建模系统ArgueLearn，并推导H1-H4。为了验证，作者先进行语料构建和算法技术评估，再通过试点设计和眼动研究优化界面，随后依次开展三项实证：与脚本化建模对比的实验室实验（Study 1）、与自适应支持及任务难度对比的2×2实验室实验（Study 2）、三个月真实课堂中的动态vs静态vs无建模现场实验（Study 3）。结果在客观论证质量上支持动态建模优势，且效果在简单/复杂任务中均存在、在复杂任务上更强，并跨论证领域迁移。讨论部分将结果回接到社会认知理论，主张动态ML建模构成新的行为建模类型，拓展了IS研究以往偏重静态建模的视角，同时用定性评论、专长后验分析和WEAT偏差分析保护贡献的边界。

## 类型与写作弧线判定

- 论文主类型判定：文章以社会认知理论为内核理论，将动态行为建模转化为系统设计特征，并据此提出H1-H4；随后通过三个实验直接比较动态建模与脚本化、自适应、静态/无建模之间的设计差异，属于理论推导制品差异并通过实验检验的典型写法。虽有设计科学元素，但占主导的是理论驱动的假设检验。

- 主导写作弧线判定：引言先建立论证技能重要性和规模化反馈缺口，随后引入社会认知理论并推导动态建模设计，再通过三个研究检验设计差异，最后在Discussion回到理论贡献、边界条件和未来研究，构成完整的问题—理论—设计—检验—返回理论弧线。

## 研究开展程序

- study_or_phase_count：7

- 研究阶段总序列：论文先完成系统构建和技术验证，再通过试点和眼动研究优化学习者中心设计，然后依次进行两个实验室实验和一个三个月现场实验，最后通过后验专长分析检验边界条件。阶段之间是累积关系：技术验证保证反馈可信，试点/眼动保证界面可用并处理错误预测威胁，Study 1证明优于脚本化基准，Study 2证明优于自适应支持并检验任务难度，Study 3证明长期跨领域学习优于静态/无建模，后验分析表明效应不受学习者先前专长影响。

### studies_or_phases

#### 1. 系统构建与技术构件验证

- order：1

- name_cn：系统构建与技术构件验证

- question_cn：能否为德文学生同行评审构建可靠的论证标注方案、语料库和ML论证挖掘模型，以支持动态论证建模？

- inputs_and_setting_cn：2012-2019年某西欧大学商业创新课程中约220名学生撰写的约7,000份同行评审；随机抽样1,000份构成标注语料；三位德语母语标注者；多种ML分类器。

- designed_or_compared_object_cn：新的论证标注方案、德文论证语料库、SVM分类器；比较了SVM、Logistic Regression、Random Forest、贝叶斯、BiLSTM-CRF、BERT等。

- baseline_control_or_counterfactual_cn：BERT和BiLSTM-CRF作为深度学习baseline；Stab和Gurevych在英文学生文本上的论证分类结果作为外部参照。

##### objective_metrics

1. 论证成分分类准确率65.4%

2. 论证关系分类准确率72.1%

3. BERT macro F1 73%

4. BiLSTM-CRF F1 57%

5. 人工标注一致性（指向Wambsganss et al. 2020b）

- analysis_method_cn：分层80/20训练测试划分、网格搜索、多组特征工程、技术实验比较、在真实未见学生数据上的鲁棒性检查。

- main_result_cn：最终选择特征工程SVM，认为在未见学生写作上比BERT更稳健；生成1,000篇德文同行评审语料，含7,996 claims和8,479 premises。

- argumentative_role_cn：为动态建模系统提供技术可信度：反馈背后的ML模型有可接受的准确率，并与更强深度学习模型比较过。

- remaining_uncertainty_cn：算法仍可能出错，准确率有限；没有学习者结果证据；尚未验证界面是否会引导学生采用错误预测。

- link_to_next_phase_cn：由于算法可能出错，需要先通过试点和眼动研究评估用户如何理解和使用动态建模反馈。

##### evidence_pointers

1. Implementation of a Theory-Driven Dynamic Argumentation Modeling System Based on ML段落

2. Dynamic Argumentation Modeling Based on NLP and ML段落

3. Wambsganss et al. (2020b)引用

#### 2. 试点设计评价

- order：2

- name_cn：试点设计评价

- question_cn：ArgueLearn的设计是否能达到其目的，用户需求是否被满足，哪些设计需要改进？

- inputs_and_setting_cn：46名不同用户，4轮评价系列，可点击mockup；观察、参与反馈和半结构化访谈。

- designed_or_compared_object_cn：动态建模系统的可点击原型；用户对论证写作目标、理论嵌入和学习目标的理解。

- baseline_control_or_counterfactual_cn：无对照组；按照Venable等人的设计科学人工评价框架进行迭代评价。

##### objective_metrics

1. 用户定性反馈

2. 观察记录

3. 改进需求数量

- analysis_method_cn：定性的迭代评价，采用Venable et al. (2012, 2016)的设计评价标准。

- main_result_cn：用户需要更透明的论证写作目标、理论嵌入和清晰的学习目标；作者据此在反馈系统中加入了目标、目的和方向指引。

- argumentative_role_cn：表明系统不是纯技术驱动，而是经过学习者中心设计迭代，满足用户需求。

- remaining_uncertainty_cn：试点只验证设计和可用性，未测学习效果；未解决错误ML预测问题。

- link_to_next_phase_cn：交互原型已改进，但还需用眼动研究进一步观察错误预测如何影响学习行为。

##### evidence_pointers

1. Experimental Design段落的pilot study描述

2. Venable et al. (2016)引用

#### 3. 眼动研究

- order：3

- name_cn：眼动研究

- question_cn：学生如何与错误预测的论证建模结构互动？错误高亮是否会影响学习或造成误导？

- inputs_and_setting_cn：13名学生使用迭代后的原型；眼动追踪和后续定性访谈。

- designed_or_compared_object_cn：学生对错误高亮的注意和使用；系统用非直接建议方式呈现错误。

- baseline_control_or_counterfactual_cn：无正式对照组；以眼动观察和访谈描述为主。

##### objective_metrics

1. 错误高亮被注意的人数（10/13）

2. 会因错误预测改变论证的人数（0/13）

3. 认为非直接高亮设计可避免过度强调错误的人数（9/13）

- analysis_method_cn：描述性统计和定性访谈整理。

- main_result_cn：大多数学生注意到错误高亮但不会据此改变论证；多数学生认为不主动建议修改的高亮设计降低了错误预测的负面影响。

- argumentative_role_cn：回应“ML反馈可能错误”这一效度威胁，并为之后将系统介绍为“正在学习的学生”提供依据。

- remaining_uncertainty_cn：样本量小，且只观察短期注意，未测长期错误反馈影响。

- link_to_next_phase_cn：确认系统可安全进入正式实验，并指导后续研究中的系统引入话术。

##### evidence_pointers

1. Experimental Design段落eye-tracking study描述

#### 4. Study 1：动态建模 vs 脚本化建模实验室实验

- order：4

- name_cn：Study 1：动态建模 vs 脚本化建模实验室实验

- question_cn：动态论证建模是否比脚本化论证建模更能提高说服性写作表现（H1）？

- inputs_and_setting_cn：54名大学生，实验室行为研究；先测问卷后写作再后测问卷；写作任务基于Flender等人关于“电视是否使学生暴力”的讨论。

- designed_or_compared_object_cn：处理组使用ArgueLearn接受动态建模反馈；对照组使用Fischer等人开发、以Toulmin模型为基础的脚本化输入工具。

- baseline_control_or_counterfactual_cn：脚本化论证建模作为当前大规模论证学习的已证实基准。

##### objective_metrics

1. 客观论证质量（按照Weinberger和Fischer方案计算支持性论点数量）

2. 主观论证质量（外部评分者五级评分）

3. 技术接受度问卷

- analysis_method_cn：线性回归/ANOVA，检查正态性和方差齐性；用前测三构念检验随机化；开放式问题定性分析。

- main_result_cn：动态建模组客观质量5.08显著高于脚本组3.20（t=-3.622, p<0.001）；主观质量3.38显著高于2.79（t=-2.654, p<0.05）。

- argumentative_role_cn：证明动态建模优于大规模学习中最常用的脚本化基准，确立了动态建模基础效果。

- remaining_uncertainty_cn：只是短期实验室效果；没有与自适应支持对比；没有检验任务难度和长期学习。

- link_to_next_phase_cn：既然优于脚本化，下一步需与更贴近“个性化”的自适应支持比较，并考虑任务难度。

##### evidence_pointers

1. Study 1: Evaluation of Dynamic Argumentation Modeling vs. Scripting in Laboratory Experiment

2. Table 4

#### 5. Study 2：动态建模 vs 自适应支持与任务难度2×2实验

- order：5

- name_cn：Study 2：动态建模 vs 自适应支持与任务难度2×2实验

- question_cn：动态建模是否优于自适应支持（H2）？与自适应支持相比，动态建模在复杂和简单任务上是否都更好（H3）？

- inputs_and_setting_cn：142名学生，沿用Study 1的实验室程序；四组为TG1动态/复杂、TG2动态/简单、TG3自适应/复杂、TG4自适应/简单。

- designed_or_compared_object_cn：操纵两个因素：支持方式（动态建模 vs 自适应支持）和任务难度（复杂 vs 简单）；自适应支持为预脚本化反馈消息和基于相似ML模型的仪表盘得分。

- baseline_control_or_counterfactual_cn：传统自适应支持作为baseline；复杂任务沿用Study 1任务，简单任务由两名专家通过简化句法和措辞生成，并由五名独立专家验证难度。

##### objective_metrics

1. 客观论证质量

2. 主观论证质量

3. Tukey HSD事后检验p值

4. Cohen's d效应量

- analysis_method_cn：ANOVA线性回归，Tukey事后检验，效应量计算，前测随机化检验。

- main_result_cn：复杂任务中动态组客观质量4.56显著高于自适应组2.87（p<0.001, d=1.1097）；简单任务中动态组3.70显著高于自适应组2.62（p=0.0216, d=0.6717）；主观质量大多不显著。

- argumentative_role_cn：证明动态建模优势不仅对脚本化成立，也对自适应支持成立；支持方式与任务难度的交互显示复杂任务下效果更强。

- remaining_uncertainty_cn：仍未测量长期技能；主观质量在简单任务中无显著差异，说明机制可能主要作用于形式结构。

- link_to_next_phase_cn：需要通过长期现场实验检验动态建模是否带来可迁移的论证技能，而非仅是单次任务表现。

##### evidence_pointers

1. Study 2: Evaluation of Dynamic vs. Adaptive Argumentation Modeling in a Laboratory Experiment

2. Tables 5–7

#### 6. Study 3：三个月现场实验

- order：6

- name_cn：Study 3：三个月现场实验

- question_cn：在三周重复论证任务中，动态建模是否比静态建模导致更好的论证技能学习（H4）？

- inputs_and_setting_cn：205名注册学生中124名完成三轮共九份同行评审和迁移后测；商业创新硕士课程；后测在另一论证领域写作。

- designed_or_compared_object_cn：TG1接受ArgueLearn动态建模；TG2接受基于Toulmin模型的静态建模文本和可视化；CG不接受建模；三组都可见相同写作指令。

- baseline_control_or_counterfactual_cn：静态建模和无建模作为对照；前测控制个人创新性、反馈寻求和主观论证能力。

##### objective_metrics

1. 迁移任务中的客观论证质量

2. 迁移任务中的主观论证质量

3. Tukey HSD p值

4. Cohen's d

- analysis_method_cn：ANOVA，Tukey事后检验，效应量，前测随机化检验，删去少于三句的无效回答。

- main_result_cn：动态组迁移任务客观质量4.04显著高于静态组3.20（p=0.015, d=0.6829）和无建模组3.03（p=0.001, d=0.7395）；主观质量三组无显著差异。

- argumentative_role_cn：证明动态建模的技能收益可持续三个月并迁移到另一论证领域，这是先前ML论证系统缺乏的证据。

- remaining_uncertainty_cn：只有客观质量显著；样本流失较多；只覆盖一个课程和一种迁移域；无法直接观察内在观察学习过程。

- link_to_next_phase_cn：既然核心效应已确立，需检查先前专长是否调节效果，以划定边界。

##### evidence_pointers

1. Study 3: Evaluation of Dynamic vs. Static Argumentation Modeling in a Field Experiment

2. Tables 8–9

#### 7. 后验学习者专长分析

- order：7

- name_cn：后验学习者专长分析

- question_cn：动态建模的效果是否受学习者先验论证专长影响？

- inputs_and_setting_cn：三项研究的前测数据；按“被动论证能力/主观论证能力”进行均值分割，比较不同专长组的学习结果。

- designed_or_compared_object_cn：高专长与低专长学习者之间的客观和主观论证质量。

- baseline_control_or_counterfactual_cn：无额外控制；在同一实验条件下做分割比较。

##### objective_metrics

1. 各研究客观论证质量p值

2. 各研究主观论证质量p值

- analysis_method_cn：均值分割后组间比较和显著性检验。

- main_result_cn：三项研究均未发现专长水平对客观或主观论证结果产生显著影响（如Study 1客观p=0.40376，主观p=0.91270；Study 2客观p=0.1473；Study 3客观p=0.6668）。

- argumentative_role_cn：表明动态建模对高、低专长学习者同样有效，支持其作为通用学习工具的边界主张。

- remaining_uncertainty_cn：均值分割可能丢失信息；样本量有限；未直接检验专长逆转效应。

- link_to_next_phase_cn：为讨论中的边界条件和未来人口统计差异研究提供分析基础。

##### evidence_pointers

1. Post Hoc Analysis of Learner Expertise

## 各部分修辞架构

### abstract_moves

1. CONTEXT: 论证是日常沟通和思维的基本元素，形成有说服力论证的能力重要。

2. PRACTICAL_STAKES: 缺乏个别化即时反馈，人工反馈不可扩展，阻碍技能培养。

3. RQ_OR_OBJECTIVE: 基于社会认知理论研究动态技术媒介论证建模是否提升短期和长期技能。

4. DESIGN_FEATURE: 构建动态ML建模系统，提供不依赖教师、时间、地点的逻辑论证错误反馈。

5. STUDY_OVERVIEW: 三项实证研究检验H1-H4。

6. RESULT: 动态模型显著改善客观论证技能，优于脚本化、自适应和静态建模。

7. CONTRIBUTION: 结果为教育和写作支持系统设计提供实证，并表明社会认知理论泛化到论证写作。

### introduction_moves

1. CONTEXT: 信息时代技能从记忆转向结构化、跨学科和创造任务。

2. PHENOMENON: 大课堂和MOOC中学生比例不利，缺乏个别互动。

3. PRACTICAL_STAKES: 缺乏个性化支持导致拖延、低学习结果、高辍学率和不满意。

4. PRIOR_KNOWLEDGE: IS几十年用于技术媒介学习，已有论证支持系统。

5. LIMITATION: 现有论证学习系统设计落后于NLP/ML发展，缺乏跨学科研究。

6. GAP: 缺少基于NLP/ML的全人中心论证学习系统的社会技术IS视角。

7. LIMITATION: 以往研究多关注一般系统设计而非实证检验，ML动态系统缺乏与脚本化、自适应基准的对比和长期现场实验。

8. THEORY_INTRO: 引入社会认知理论行为建模作为动态建模的理论基础。

9. RQ_OR_OBJECTIVE: 提出构建动态建模系统并验证其对论证技能的影响。

10. HYPOTHESIS_OR_PROPOSITION: 给出H1-H4。

11. METHOD_JUSTIFICATION: 用客观和主观论证质量以及三个月后跨领域迁移作为学习衡量。

12. CONTRIBUTION: 强调对比基准、跨领域泛化和设计知识贡献。

### theory_and_knowledge_moves

1. PRIOR_KNOWLEDGE: 人类论证能力普遍有缺陷，常混淆观点与事实。

2. THEORY_INTRO: 论证理论从亚里士多德到Toulmin模型强调逻辑结构。

3. THEORY_INTRO: Toulmin模型将论证分为claim和premise等成分。

4. PRIOR_KNOWLEDGE: 过去35年开发超过60种论证学习系统。

5. THEORY_INTRO: 按社会认知视角区分静态建模、脚本化建模和自适应支持。

6. BENCHMARK_OR_CONTRAST: 脚本化建模被证明是当前大规模论证学习的标准。

7. MECHANISM: 论证挖掘可建模期望行为，支持观察学习。

8. LIMITATION: NLP工具缺少教学场景和学习者中心设计，未做学习者评价。

9. THEORY_INTRO: 社会认知理论将学习定义为通过观察模型获取知识。

10. MECHANISM: 行为建模包括替代经验学习和亲历学习。

11. LIMITATION: 以往IS行为建模多采用静态模型。

12. GAP: 动态ML建模的行为建模和观察学习机制尚未被系统检验。

### artifact_design_moves

1. REQUIREMENT: 动态建模系统需提供透明、个别化、自适应反馈，基于逻辑论证错误。

2. DESIGN_FEATURE: 服务导向架构包含四个独立构件。

3. DESIGN_FEATURE: ArgueLearn界面提供文本输入、高亮、论证结构图、三个得分和按需分析。

4. METHOD_JUSTIFICATION: 用30个访谈形成需求，经过多轮设计科学评价。

5. REQUIREMENT: 为保证可扩展和跨领域，ML模型可不断使用新语料改进。

6. METHOD_JUSTIFICATION: 创建新德文论证标注方案和1,000篇语料以训练模型。

7. BENCHMARK_OR_CONTRAST: 比较SVM与BERT、BiLSTM-CRF，选择更鲁棒的SVM。

8. ROBUSTNESS_OR_BOUNDARY_TEST: 用眼动研究处理错误预测威胁，并以“训练中的学生”框架向用户介绍系统。

### evaluation_moves

1. STUDY_OVERVIEW: 概述试点、眼动和三项实验。

2. METHOD_JUSTIFICATION: 说明Study 1、2、3的设计分别对应H1、H2/H3、H4。

3. METHOD_JUSTIFICATION: 用前测控制随机化和论证能力。

4. METHOD_JUSTIFICATION: 客观质量用Weinberger和Fischer方案，主观质量用外部评分。

5. BENCHMARK_OR_CONTRAST: Study 1以脚本化建模为对照；Study 2以自适应支持为对照并操纵任务难度；Study 3以静态和无建模为对照。

6. RESULT: Study 1动态组客观和主观质量显著更高。

7. RESULT: Study 2动态组在复杂和简单任务下客观质量均显著更高，但主观质量大多不显著。

8. RESULT: Study 3动态组在迁移任务客观质量显著更高，主观质量不显著。

9. ROBUSTNESS_OR_BOUNDARY_TEST: 后验专长分析未发现调节效应。

10. ROBUSTNESS_OR_BOUNDARY_TEST: WEAT分析用于排除语料系统性偏差。

### discussion_and_contribution_moves

1. RESULT: 研究目标达成，动态建模在客观质量上优于脚本化、自适应、静态和无建模。

2. CONTRIBUTION: 将动态建模定位为IS行为建模从静态走向动态的推进。

3. THEORY_RETURN: 结果支持社会认知理论在非STEM写作领域的泛化。

4. BOUNDARY_CONDITION: 复杂任务下效果更强，简单任务也有中等效果。

5. BOUNDARY_CONDITION: 主观质量在跨领域迁移中未改善，可能因Toulmin只覆盖logos而忽视ethos和pathos。

6. BOUNDARY_CONDITION: 高低专长学习者均受益，未出现专长逆转。

7. LIMITATION_AND_FUTURE: 样本量、领域、伦理、错误反馈、AI素养和人口差异尚需研究。

8. CONTRIBUTION: 为未来类似技能支持系统的设计提供基础和方向。

## 理论/知识到设计的翻译

### 知识/理论基础

1. 社会认知理论（Bandura 1986, 2001）：行为建模、观察学习、替代经验、亲历学习

2. 论证理论（Toulmin 1984, 2003；亚里士多德说服三要素）

3. 技术媒介学习与IS设计（Gupta and Bostrom 2009, 2013）

4. 论证挖掘/NLP研究（Stab and Gurevych 2017b, Lawrence and Reed 2019）

5. 反馈与错误学习文献（Hattie and Timperley 2007, Metcalfe 2017）

6. 用户中心设计知识（30个访谈、试点、眼动研究）

- 理论—设计耦合：direct

- 耦合判定理由：社会认知理论的行为建模和观察学习命题直接定义了“动态建模”这一核心设计概念，并驱动H1-H4：动态建模应提供个性化、基于错误、可反复观察的反馈，从而优于脚本化、静态和简单自适应支持。虽然具体界面细节和技术实现受用户研究和ML工程影响，但被检验的核心设计差异正是由理论预期并直接比较的。

- 理论到设计翻译链：社会认知理论行为建模/观察学习 → 动态展示期望论证行为的反馈优于预先脚本或静态模板 → 系统需在写作中实时识别claim/premise及支持关系，并高亮、可视化、按需反馈 → ArgueLearn以SVM论证挖掘为核心，在界面中提供高亮、论证图和反馈细节 → 通过三个实验分别与脚本化、自适应、静态/无建模对比，检验理论预期。

### mapping_table

#### 1. 1

- theory_or_knowledge_claim_cn：行为建模中观察学习通过替代经验帮助学习者获得技能。

- mechanism_cn：动态模型提供期望论证行为的示范，学习者可观察、比较并修正自身论证。

- design_requirement_cn：系统应提供动态、个别化的论证行为模型，而非事先固定脚本。

- artifact_choice_cn：ArgueLearn在写作后按需分析文本并高亮claim/premise及支持关系。

- evaluated_contrast_cn：动态建模 vs 脚本化建模输入界面。

- objective_result_cn：动态组客观和主观论证质量显著高于脚本组。

##### evidence_pointers

1. Hypotheses Development H1

2. Study 1 Results

3. Table 4

#### 2. 2

- theory_or_knowledge_claim_cn：自适应反馈需要嵌入理论驱动的动态建模，而非仅提供文本消息或仪表盘。

- mechanism_cn：高亮、图形化结构和错误聚焦比单纯自适应反馈消息提供更丰富的观察学习资源。

- design_requirement_cn：界面需提供多层次反馈：高亮、论证图、得分、详细解释。

- artifact_choice_cn：ArgueLearn的F3-F7功能；对照为仅提供仪表盘和反馈消息的自适应系统。

- evaluated_contrast_cn：动态建模 vs 传统自适应支持。

- objective_result_cn：动态建模在复杂和简单任务中客观论证质量均更高。

##### evidence_pointers

1. Hypotheses Development H2/H3

2. Study 2 Results

3. Tables 5–7

#### 3. 3

- theory_or_knowledge_claim_cn：认知负荷理论认为复杂任务需要更强结构和动态支持。

- mechanism_cn：动态建模降低复杂论证结构的认知负荷，同时不影响简单任务中的学习。

- design_requirement_cn：反馈应适配任务复杂度。

- artifact_choice_cn：动态建模在所有任务难度下可用，提供图形和分层反馈。

- evaluated_contrast_cn：复杂任务 vs 简单任务 x 动态 vs 自适应。

- objective_result_cn：复杂任务大效应（d=1.11），简单任务中等效应（d=0.67）。

##### evidence_pointers

1. H3 Development

2. Study 2 Tables 5–7

#### 4. 4

- theory_or_knowledge_claim_cn：观察学习的四个子过程（注意、保持、产生、动机）在动态模型中比静态模型更充分。

- mechanism_cn：动态反馈个别化地突出相关特征、与自身行为紧密关联、提供情境化纠正、精确告知结果预期。

- design_requirement_cn：系统应在重复任务中持续根据个人行为更新反馈。

- artifact_choice_cn：三周内九次同行评审，动态组每次获得ArgueLearn反馈；静态组只获得固定Toulmin模型说明。

- evaluated_contrast_cn：动态建模 vs 静态建模 vs 无建模。

- objective_result_cn：三个月后迁移任务中动态组客观论证质量显著高于静态和无建模。

##### evidence_pointers

1. H4 Development

2. Study 3 Results

3. Tables 8–9

## 评价逻辑

### evaluation_modes

1. 技术基准比较：SVM vs BERT vs BiLSTM-CRF在德文论证语料上的准确率/F1

2. 设计科学试点评价：4轮46用户，定性评价

3. 眼动研究：13名用户，错误预测交互检验

4. 受控实验室实验：Study 1单因素，Study 2 2×2因子设计

5. 长期现场实验：Study 3三组三个月

6. 后验专长调节分析

7. WEAT偏差分析（在局限部分报告）

- why_these_evaluations_cn：每种评价解决不同论证缺口：技术基准保证ML反馈可信；试点和眼动保证学习者中心设计和错误反馈安全；受控实验建立相对基准的因果效果；现场实验将效果推广到真实长期学习环境并测量跨领域迁移；后验专长分析检验边界条件；WEAT分析排除语料偏见。

- benchmark_and_contrast_chain_cn：文章建立了一条递进的对照链：先以脚本化建模（当前大规模标准）为基准证明动态建模有效；再以传统自适应支持为更接近个性化教学的基准，同时加入任务难度；最后以静态建模和无建模为基准，在三个月现场环境中检验长期技能迁移。每一步的对照组都比上一步更贴近“动态建模要超越的现有技术”。

### claim_evidence_ledger

#### 1. SVM模型在德文论证成分和关系识别上可接受且比BERT更鲁棒。

- claim_cn：SVM模型在德文论证成分和关系识别上可接受且比BERT更鲁棒。

- evidence_cn：成分准确率65.4%，关系准确率72.1%；BERT macro F1 73%但在未见学生数据上不如SVM稳健。

- status_cn：支持

#### 2. 动态建模优于脚本化建模。

- claim_cn：动态建模优于脚本化建模。

- evidence_cn：Study 1客观和主观质量显著更高。

- status_cn：支持

#### 3. 动态建模优于自适应支持。

- claim_cn：动态建模优于自适应支持。

- evidence_cn：Study 2客观质量在复杂和简单任务中显著更高；主观质量大多不显著。

- status_cn：部分支持

#### 4. 动态建模在复杂和简单任务中都有效，且复杂任务效果更强。

- claim_cn：动态建模在复杂和简单任务中都有效，且复杂任务效果更强。

- evidence_cn：复杂任务d=1.1097，简单任务d=0.6717。

- status_cn：支持（基于客观质量）

#### 5. 动态建模在长期重复任务中导致更好的论证技能学习并跨领域迁移。

- claim_cn：动态建模在长期重复任务中导致更好的论证技能学习并跨领域迁移。

- evidence_cn：Study 3动态组迁移任务客观质量显著高于静态和无建模。

- status_cn：支持（客观质量）

#### 6. 动态建模提升主观说服质量。

- claim_cn：动态建模提升主观说服质量。

- evidence_cn：Study 1主观质量显著；Study 2中大多不显著；Study 3跨领域无显著差异。

- status_cn：不一致/仅短期支持

#### 7. 动态建模对高低专长学习者均有效。

- claim_cn：动态建模对高低专长学习者均有效。

- evidence_cn：三项研究的后验专长分析均不显著。

- status_cn：支持

#### 8. 社会认知理论在论证写作领域可泛化。

- claim_cn：社会认知理论在论证写作领域可泛化。

- evidence_cn：跨领域迁移和动态vs静态/无建模对比支持，但未直接测量观察学习过程。

- status_cn：部分支持

- internal_validity_strategy_cn：使用随机分配、前测控制构念检验、相同实验设备和程序、基于Toulmin的客观编码、两名标注者取均值、不同参与者不跨研究、用任务难度专家验证操纵、用眼动和用户访谈控制错误预测效应。

- external_validity_strategy_cn：三项研究覆盖受控实验室和大规模真实课堂；Study 3跨三个月、重复任务、另一论证领域迁移；后验分析覆盖不同专长；定性评论补充真实用户感受。

- what_is_not_actually_tested_cn：观察学习、替代经验、注意/保持/产生/动机等理论机制没有被直接测量，只能通过不同设计对比间接推断；主观说服质量在长期迁移中未改善；错误ML反馈的负面效果未在更大样本中严格量化；效果只在一个国家、一门课程、德文语料和同伴评审任务上得到验证。

## 贡献闭环

- technical_claim_cn：特征工程SVM在德文学生同行评审论证成分与关系识别上可达到可接受准确率，且比BERT更稳健，可作为动态论证建模的可行后端。

- artifact_claim_cn：ArgueLearn中的动态建模设计——按需分析、高亮、论证结构图、分层反馈——是导致客观论证质量提升的原因。

- mechanism_claim_cn：动态建模通过提供更丰富的观察学习机会和基于个人错误的反馈，促进了论证技能学习。

- boundary_claim_cn：动态建模的效果在复杂任务上强于简单任务，对高低专长学习者均成立，并在三个月后迁移到其他论证领域。

- reusable_design_knowledge_cn：可复用的是服务导向四构件架构、按需动态反馈模式、错误非直接呈现策略、将ML系统介绍为“正在学习的学生”以减少错误预测负面效应，以及多阶段学习者中心设计评价流程。

- theoretical_contribution_cn：将社会认知理论从静态行为建模扩展到动态ML建模，并证明该理论可用于论证写作这类非结构化写作技能；回应了IS研究中行为建模过于静态的问题。

- how_discussion_closes_intro_gap_cn：讨论部分重新回到引言提出的“ML动态论证系统缺乏严格实证”的缺口，以三项研究的结果和效应量回应，并说明动态建模为何优于脚本化、自适应和静态建模，从而声称填补了文献缺口。

- overclaim_or_unsupported_leaps_cn：摘要和结论有时用“across domains”和“all conditions”等强表述，但实际跨域迁移只有一个后测领域；H2/H3被作者自己称为“部分确认”，仍有主观质量不显著的结果；理论机制未被直接测量，仅靠设计对比间接推断。

## 句级写作动作图谱

### 1. P1 S1

- order：1

- section：Abstract

- locator：P1 S1

- move_code：CONTEXT

- paraphrase_cn：论证是日常沟通与思考中无处不在的基本元素。

- rhetorical_function_cn：开篇将论证技能置于普遍认知活动的位置。

- depends_on_cn：无。

- sets_up_cn：为后续论证技能值得支持奠定背景。

- evidence_pointer：Abstract P1

### 2. P1 S2-S3

- order：2

- section：Abstract

- locator：P1 S2-S3

- move_code：PRACTICAL_STAKES

- paraphrase_cn：形成说服性论证的能力对说服、决策、谈判和文明话语重要，但人类常因缺少个别即时反馈和人工反馈不可扩展而难以发展这种能力。

- rhetorical_function_cn：同时给出重要性和阻碍，形成实践痛点。

- depends_on_cn：论证的基本性。

- sets_up_cn：引出需要技术干预的理由。

- evidence_pointer：Abstract P1

### 3. P2

- order：3

- section：Abstract

- locator：P2

- move_code：RQ_OR_OBJECTIVE

- paraphrase_cn：基于社会认知理论，研究动态技术媒介论证建模是否在短期和长期提升学生论证技能。

- rhetorical_function_cn：明确研究问题和理论基础。

- depends_on_cn：实践痛点。

- sets_up_cn：决定以动态建模为核心概念。

- evidence_pointer：Abstract P2

### 4. P3

- order：4

- section：Abstract

- locator：P3

- move_code：DESIGN_FEATURE

- paraphrase_cn：构建了一个动态ML建模系统，提供基于逻辑论证错误的写作反馈，不受教师、时间和地点限制。

- rhetorical_function_cn：概要描述制品。

- depends_on_cn：研究目标。

- sets_up_cn：为实验比较提供对象。

- evidence_pointer：Abstract P3

### 5. P4

- order：5

- section：Abstract

- locator：P4

- move_code：STUDY_OVERVIEW

- paraphrase_cn：通过三个实证研究检验动态建模与脚本化建模、自适应支持、复杂与简单任务以及三月静态建模的比较。

- rhetorical_function_cn：预告研究结构和核心假设。

- depends_on_cn：制品描述。

- sets_up_cn：让读者期待后面的研究设计。

- evidence_pointer：Abstract P4

### 6. P5

- order：6

- section：Abstract

- locator：P5

- move_code：RESULT

- paraphrase_cn：结果发现动态行为建模显著改善学习者的客观论证技能，并超越脚本化、自适应和静态建模。

- rhetorical_function_cn：给出总体结论。

- depends_on_cn：研究实现。

- sets_up_cn：为贡献声明做准备。

- evidence_pointer：Abstract P5

### 7. P6

- order：7

- section：Abstract

- locator：P6

- move_code：CONTRIBUTION

- paraphrase_cn：工作提供关于动态建模和社会认知理论的实证发现，并表明该理论可泛化到论证写作领域。

- rhetorical_function_cn：声明理论贡献。

- depends_on_cn：结果。

- sets_up_cn：为全文贡献定位。

- evidence_pointer：Abstract P6

### 8. P1 S1-S3

- order：8

- section：Introduction

- locator：P1 S1-S3

- move_code：CONTEXT

- paraphrase_cn：在信息易得的世界，记忆能力不再是重点，结构化处理知识的能力更重要，职业向跨学科、模糊和创造任务转变。

- rhetorical_function_cn：建立时代和教育背景。

- depends_on_cn：无。

- sets_up_cn：说明技能教育的必要性。

- evidence_pointer：Introduction P1

### 9. P2 S1-S3

- order：9

- section：Introduction

- locator：P2 S1-S3

- move_code：PHENOMENON

- paraphrase_cn：课堂和MOOC规模扩大导致教育者与学习者比例不利，妨碍个体互动和个性化学习体验。

- rhetorical_function_cn：描述现实经验现象。

- depends_on_cn：技能重要性。

- sets_up_cn：引出规模化反馈缺口。

- evidence_pointer：Introduction P2

### 10. P2 S4

- order：10

- section：Introduction

- locator：P2 S4

- move_code：PRACTICAL_STAKES

- paraphrase_cn：研究显示缺乏个性化支持导致拖延、低学习成果、高辍学率和学习不满。

- rhetorical_function_cn：把现象后果化。

- depends_on_cn：学习者规模问题。

- sets_up_cn：强调需要技术解决方案。

- evidence_pointer：Introduction P2

### 11. P3 S1-S3

- order：11

- section：Introduction

- locator：P3 S1-S3

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：IS已被用于技术媒介学习多年，并已开发出支持在线辩论、协作学习和自适应论证反馈的系统。

- rhetorical_function_cn：总结已有技术尝试。

- depends_on_cn：技术需求。

- sets_up_cn：说明技术解决方案不是没有，但有局限。

- evidence_pointer：Introduction P3

### 12. P3 S4-S5

- order：12

- section：Introduction

- locator：P3 S4-S5

- move_code：LIMITATION

- paraphrase_cn：当前论证学习系统的设计和采用落后于NLP/ML进展，缺少检验自动化动态建模对论证技能影响的跨学科文献。

- rhetorical_function_cn：指出文献与技术的脱节。

- depends_on_cn：已有系统概述。

- sets_up_cn：构建研究缺口。

- evidence_pointer：Introduction P3

### 13. P3 S6

- order：13

- section：Introduction

- locator：P3 S6

- move_code：GAP

- paraphrase_cn：缺少基于NLP和ML的、以学习者为中心并通过行为建模反馈支持自我监控的论证学习系统的社会技术IS视角。

- rhetorical_function_cn：明确提出缺口。

- depends_on_cn：前句局限。

- sets_up_cn：将研究定位为IS视角。

- evidence_pointer：Introduction P3

### 14. P4 S1-S4

- order：14

- section：Introduction

- locator：P4 S1-S4

- move_code：LIMITATION

- paraphrase_cn：已有动态建模系统研究常缺少真实学习环境中的实验，未与脚本化建模和自适应支持基准比较，也没有长期现场实验。

- rhetorical_function_cn：把缺口具体化为评价缺失。

- depends_on_cn：前面关于动态建模系统的论点。

- sets_up_cn：为三项研究的设计提供理由。

- evidence_pointer：Introduction P4

### 15. P5 S1-S2

- order：15

- section：Introduction

- locator：P5 S1-S2

- move_code：THEORY_INTRO

- paraphrase_cn：基于社会认知理论提出理论驱动的动态ML论证建模系统，以透明、个体化和自适应反馈呈现逻辑论证错误。

- rhetorical_function_cn：引入理论并命名方案。

- depends_on_cn：缺口。

- sets_up_cn：为设计特征和假设提供理论锚点。

- evidence_pointer：Introduction P5

### 16. P6 S1-S2

- order：16

- section：Introduction

- locator：P6 S1-S2

- move_code：HYPOTHESIS_OR_PROPOSITION

- paraphrase_cn：基于行为建模，动态建模反馈应能提高论证能力，作者因而开展三个实证研究检验H1-H4。

- rhetorical_function_cn：给出核心预测和研究路线。

- depends_on_cn：社会认知理论。

- sets_up_cn：预告后续研究和结果。

- evidence_pointer：Introduction P6

### 17. P7 S1-S3

- order：17

- section：Introduction

- locator：P7 S1-S3

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：用Toulmin模型评估客观论证质量并辅以外评分，三个月后在其他领域测说服写作表现以代表技能学习。

- rhetorical_function_cn：说明因变量和迁移测量逻辑。

- depends_on_cn：论证理论。

- sets_up_cn：让读者知道如何判断结果。

- evidence_pointer：Introduction P7

### 18. P8 S1-S4

- order：18

- section：Introduction

- locator：P8 S1-S4

- move_code：CONTRIBUTION

- paraphrase_cn：作者声称首次严格比较动态ML建模与三个基准，并证明社会认知理论可泛化到论证写作。

- rhetorical_function_cn：声明新意和理论贡献。

- depends_on_cn：整个研究设计。

- sets_up_cn：为Discussion的贡献展开做准备。

- evidence_pointer：Introduction P8

### 19. Argumentation Skills P1 S3

- order：19

- section：Related Work

- locator：Argumentation Skills P1 S3

- move_code：PHENOMENON

- paraphrase_cn：多个领域研究发现人类通常不擅于论证，常把观点与事实主张混淆，不会反驳对方而坚持己见。

- rhetorical_function_cn：为训练论证技能的必要性提供实证基础。

- depends_on_cn：无。

- sets_up_cn：支持开发论证支持系统。

- evidence_pointer：Related Work, Argumentation Skills

### 20. Argumentation Skills P2

- order：20

- section：Related Work

- locator：Argumentation Skills P2

- move_code：THEORY_INTRO

- paraphrase_cn：亚里士多德区分logos、ethos和pathos三个说服原则。

- rhetorical_function_cn：引入论证理论的历史基础。

- depends_on_cn：论证重要性。

- sets_up_cn：为后来Toulmin模型和后续对主观质量差异的解释提供背景。

- evidence_pointer：Related Work, Argumentation Skills

### 21. Argumentation Skills P3-P4

- order：21

- section：Related Work

- locator：Argumentation Skills P3-P4

- move_code：THEORY_INTRO

- paraphrase_cn：Toulmin模型是最著名的形式论证模型，论证由claim和premise等成分组成。

- rhetorical_function_cn：确定本文评价论证质量的正式标准。

- depends_on_cn：论证理论历史。

- sets_up_cn：为标注方案、系统反馈和结果测量提供共同框架。

- evidence_pointer：Related Work, Argumentation Skills; Figure 1

### 22. Tech-Mediated Systems P1

- order：22

- section：Related Work

- locator：Tech-Mediated Systems P1

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：35年来已开发超过60种论证支持系统，涵盖创建、编辑、解释或评审论证。

- rhetorical_function_cn：说明大量已有工作。

- depends_on_cn：论证理论。

- sets_up_cn：为分类和缺口提供前提。

- evidence_pointer：Related Work, Technology-Mediated Argumentation Learning Systems

### 23. Tech-Mediated Systems P2-P3

- order：23

- section：Related Work

- locator：Tech-Mediated Systems P2-P3

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：按社会认知视角可区分静态建模、脚本化建模和自适应支持三类系统。

- rhetorical_function_cn：建立系统分类学。

- depends_on_cn：对已有系统的综述。

- sets_up_cn：为动态建模定位为新的子类。

- evidence_pointer：Related Work; Table 1

### 24. Tech-Mediated Systems P3 S3

- order：24

- section：Related Work

- locator：Tech-Mediated Systems P3 S3

- move_code：BENCHMARK_OR_CONTRAST

- paraphrase_cn：脚本化建模因为领域无关、可扩展和有效，已成为大规模论证学习标准。

- rhetorical_function_cn：把脚本化建模设立为基准。

- depends_on_cn：系统分类。

- sets_up_cn：为H1比较动态建模与脚本化建模铺路。

- evidence_pointer：Related Work, Tech-Mediated Systems

### 25. Tech-Mediated Systems P4

- order：25

- section：Related Work

- locator：Tech-Mediated Systems P4

- move_code：DESIGN_FEATURE

- paraphrase_cn：作者提出基于社会认知理论、利用ML的动态论证建模系统，并将其视为自适应支持的一个子类。

- rhetorical_function_cn：给出本文系统在分类中的位置。

- depends_on_cn：三分类体系。

- sets_up_cn：说明动态建模比传统自适应支持更智能和个性化。

- evidence_pointer：Related Work, Tech-Mediated Systems

### 26. Tech-Mediated Systems P5-P6

- order：26

- section：Related Work

- locator：Tech-Mediated Systems P5-P6

- move_code：MECHANISM

- paraphrase_cn：论证挖掘能从文本中识别claim和premise，从而为观察学习建立期望行为模型。

- rhetorical_function_cn：解释技术如何支撑学习机制。

- depends_on_cn：ML任务定义。

- sets_up_cn：支撑动态建模优于静态/脚本的机制论证。

- evidence_pointer：Related Work, Tech-Mediated Systems

### 27. Tech-Mediated Systems P7

- order：27

- section：Related Work

- locator：Tech-Mediated Systems P7

- move_code：LIMITATION

- paraphrase_cn：NLP社区开发的工具缺乏教学场景、学习者中心视角和技术媒介学习评价。

- rhetorical_function_cn：指出已有动态工具的评价缺失。

- depends_on_cn：对NLP工具的描述。

- sets_up_cn：证明IS视角的实验评价有价值。

- evidence_pointer：Related Work, Tech-Mediated Systems

### 28. Social Cognitive View P1 S1-S3

- order：28

- section：Related Work

- locator：Social Cognitive View P1 S1-S3

- move_code：THEORY_INTRO

- paraphrase_cn：社会认知理论认为学习是通过观察模型获得知识，行为建模包括替代学习和亲历学习。

- rhetorical_function_cn：引入核心机制。

- depends_on_cn：Bandura理论。

- sets_up_cn：为动态建模的优越性提供理论解释。

- evidence_pointer：Related Work, Social Cognitive View

### 29. Social Cognitive View P1 S4-S5

- order：29

- section：Related Work

- locator：Social Cognitive View P1 S4-S5

- move_code：LIMITATION

- paraphrase_cn：过去IS研究主要提供静态模型，如视频或示例，缺乏动态行为建模。

- rhetorical_function_cn：建立IS文献内的缺口。

- depends_on_cn：社会认知理论。

- sets_up_cn：为H4比较动态与静态提供动机。

- evidence_pointer：Related Work, Social Cognitive View

### 30. Intro paragraph

- order：30

- section：Hypotheses Development

- locator：Intro paragraph

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：假设基于技能学习、论证理论、技术媒介学习、论证挖掘和教育工具设计文献推导。

- rhetorical_function_cn：说明理论来源的多元性。

- depends_on_cn：相关文献。

- sets_up_cn：使假设看起来有据可依。

- evidence_pointer：Hypotheses Development

### 31. H1 P1

- order：31

- section：Hypotheses Development

- locator：H1 P1

- move_code：GAP

- paraphrase_cn：脚本化建模与动态建模依赖不同机制，现有研究无法给出它们在商业领域论证学习中的明确结论。

- rhetorical_function_cn：制造假设检验的必要性。

- depends_on_cn：系统分类。

- sets_up_cn：H1。

- evidence_pointer：H1 section

### 32. H1 P2

- order：32

- section：Hypotheses Development

- locator：H1 P2

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：Fischer等人的脚本理论表明预结构化论证输入可改善客观论证质量。

- rhetorical_function_cn：承认脚本化建模的证据基础。

- depends_on_cn：脚本理论文献。

- sets_up_cn：使H1的比较有意义的强基准。

- evidence_pointer：H1 section

### 33. H1 P3

- order：33

- section：Hypotheses Development

- locator：H1 P3

- move_code：MECHANISM

- paraphrase_cn：过度脚本化可能抑制自主性，而观察学习和替代经验在开放任务中可能更有效。

- rhetorical_function_cn：给出动态建模优越性的机制理由。

- depends_on_cn：社会认知理论。

- sets_up_cn：直接引出H1。

- evidence_pointer：H1 section

### 34. H1 P4

- order：34

- section：Hypotheses Development

- locator：H1 P4

- move_code：REQUIREMENT

- paraphrase_cn：动态监控和建模应定义目标、监控进展并识别达成目标的活动。

- rhetorical_function_cn：将机制转化为系统功能要求。

- depends_on_cn：反馈文献。

- sets_up_cn：指导系统实现。

- evidence_pointer：H1 section

### 35. H1 P5

- order：35

- section：Hypotheses Development

- locator：H1 P5

- move_code：MECHANISM

- paraphrase_cn：犯错和接受反馈能增强记忆与正确反应生成，透明高亮反馈有效。

- rhetorical_function_cn：用错误学习文献支持动态反馈。

- depends_on_cn：认知心理学研究。

- sets_up_cn：为系统高亮设计提供理由。

- evidence_pointer：H1 section

### 36. H1 final

- order：36

- section：Hypotheses Development

- locator：H1 final

- move_code：HYPOTHESIS_OR_PROPOSITION

- paraphrase_cn：H1：动态论证建模比脚本化论证建模更能提高说服性写作表现。

- rhetorical_function_cn：正式提出第一个假设。

- depends_on_cn：机制论证。

- sets_up_cn：Study 1。

- evidence_pointer：H1 section

### 37. H2 P1-P2

- order：37

- section：Hypotheses Development

- locator：H2 P1-P2

- move_code：REQUIREMENT

- paraphrase_cn：自适应支持常见于文本反馈和仪表盘，但应考虑动态高亮、图形结构和错误聚焦的嵌入。

- rhetorical_function_cn：区分本文动态建模与传统自适应支持。

- depends_on_cn：自适应支持文献。

- sets_up_cn：H2。

- evidence_pointer：H2 section

### 38. H2 final

- order：38

- section：Hypotheses Development

- locator：H2 final

- move_code：HYPOTHESIS_OR_PROPOSITION

- paraphrase_cn：H2：动态论证建模比自适应支持更能提高说服性写作表现。

- rhetorical_function_cn：正式提出第二个假设。

- depends_on_cn：与自适应支持的区别。

- sets_up_cn：Study 2。

- evidence_pointer：H2 section

### 39. H3 P1

- order：39

- section：Hypotheses Development

- locator：H3 P1

- move_code：MECHANISM

- paraphrase_cn：任务难度与工作记忆容量和元素交互性有关，复杂论证需要更精细动态建模。

- rhetorical_function_cn：引入任务难度作为调节机制。

- depends_on_cn：认知负荷理论。

- sets_up_cn：H3。

- evidence_pointer：H3 section

### 40. H3 final

- order：40

- section：Hypotheses Development

- locator：H3 final

- move_code：HYPOTHESIS_OR_PROPOSITION

- paraphrase_cn：H3：与自适应支持相比，动态建模在复杂和简单任务上都带来更好写作表现。

- rhetorical_function_cn：正式提出第三个假设。

- depends_on_cn：任务难度机制。

- sets_up_cn：Study 2的因子设计。

- evidence_pointer：H3 section

### 41. H4 P1-P4

- order：41

- section：Hypotheses Development

- locator：H4 P1-P4

- move_code：MECHANISM

- paraphrase_cn：动态ML建模通过注意、保持、产生和动机四个观察学习过程优于静态模型。

- rhetorical_function_cn：展开长期优势的理论机制。

- depends_on_cn：Bandura四个过程。

- sets_up_cn：H4。

- evidence_pointer：H4 section

### 42. H4 P5

- order：42

- section：Hypotheses Development

- locator：H4 P5

- move_code：GAP

- paraphrase_cn：尚无研究在长期现场实验中检验动态论证反馈对技能的影响，也没有跨领域迁移证据。

- rhetorical_function_cn：指出长期现场证据缺失。

- depends_on_cn：IS静态建模主导。

- sets_up_cn：H4和Study 3。

- evidence_pointer：H4 section

### 43. H4 final

- order：43

- section：Hypotheses Development

- locator：H4 final

- move_code：HYPOTHESIS_OR_PROPOSITION

- paraphrase_cn：H4：三个月重复任务中动态建模比静态建模导致更好学习。

- rhetorical_function_cn：正式提出第四个假设。

- depends_on_cn：观察学习机制。

- sets_up_cn：Study 3。

- evidence_pointer：H4 section

### 44. Introduction P1

- order：44

- section：Experimental Studies

- locator：Introduction P1

- move_code：STUDY_OVERVIEW

- paraphrase_cn：为检验四个假设，设计了三个实验并操纵不同论证建模方式。

- rhetorical_function_cn：总起实验部分。

- depends_on_cn：假设。

- sets_up_cn：后续各Study细节。

- evidence_pointer：Experimental Studies opening

### 45. P1

- order：45

- section：Implementation

- locator：P1

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：系统设计依据技能学习、论证理论、技术媒介学习、论证挖掘和工具设计文献。

- rhetorical_function_cn：强调设计有理论依据。

- depends_on_cn：文献综述。

- sets_up_cn：使系统不是随意的技术演示。

- evidence_pointer：Implementation of a Theory-Driven Dynamic Argumentation Modeling System Based on ML

### 46. P2

- order：46

- section：Implementation

- locator：P2

- move_code：DESIGN_FEATURE

- paraphrase_cn：系统采用服务导向架构，四个构件可独立更新，有利于跨领域重用。

- rhetorical_function_cn：描述制品的顶层架构。

- depends_on_cn：设计科学方法。

- sets_up_cn：为后续可复用设计知识服务。

- evidence_pointer：Implementation section; Figure 2

### 47. P3-P4

- order：47

- section：Implementation

- locator：P3-P4

- move_code：DESIGN_FEATURE

- paraphrase_cn：ArgueLearn界面提供文本输入、按需分析、高亮、个人仪表盘、得分和论证图。

- rhetorical_function_cn：呈现具体界面功能。

- depends_on_cn：服务架构。

- sets_up_cn：为后续评价中的功能引用提供基础。

- evidence_pointer：User Interface Design; Figure 3

### 48. NLP/ML P1-P3

- order：48

- section：Implementation

- locator：NLP/ML P1-P3

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：创建了德文论证标注方案和1,000篇同行评审语料，并使用SVM识别成分和关系。

- rhetorical_function_cn：说明ML后端的数据基础。

- depends_on_cn：Toulmin模型。

- sets_up_cn：为技术评价和准确率报告提供依据。

- evidence_pointer：Dynamic Argumentation Modeling Based on NLP and ML

### 49. NLP/ML P4

- order：49

- section：Implementation

- locator：NLP/ML P4

- move_code：BENCHMARK_OR_CONTRAST

- paraphrase_cn：SVM与BERT和BiLSTM-CRF比较后被认为更稳健，因此被选入最终系统。

- rhetorical_function_cn：用技术对比证明模型选择。

- depends_on_cn：语料与评价。

- sets_up_cn：降低对ML反馈准确性的质疑。

- evidence_pointer：Dynamic Argumentation Modeling Based on NLP and ML

### 50. P2

- order：50

- section：Experimental Design

- locator：P2

- move_code：STUDY_OVERVIEW

- paraphrase_cn：三项研究分别对应H1、H2/H3和H4，并用试点和眼动研究为正式实验做准备。

- rhetorical_function_cn：明确研究阶段划分。

- depends_on_cn：全部假设。

- sets_up_cn：引导读者阅读不同Study。

- evidence_pointer：Experimental Design

### 51. Pilot paragraph

- order：51

- section：Experimental Design

- locator：Pilot paragraph

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：试点研究用人工评价框架检查效用、价值、弱点和改进请求。

- rhetorical_function_cn：说明为什么先做试点。

- depends_on_cn：制品已完成初版。

- sets_up_cn：为界面需求说明提供依据。

- evidence_pointer：Experimental Design pilot study

### 52. Pilot result + eye-tracking

- order：52

- section：Experimental Design

- locator：Pilot result + eye-tracking

- move_code：ROBUSTNESS_OR_BOUNDARY_TEST

- paraphrase_cn：试点发现需要更透明的学习目标；眼动研究发现错误高亮会被注意但不会导致学生改变论证。

- rhetorical_function_cn：证明错误预测风险被控制。

- depends_on_cn：试点和眼动数据。

- sets_up_cn：支持将系统介绍为‘训练中的学生’以减少错误反馈担忧。

- evidence_pointer：Experimental Design pilot/eye-tracking

### 53. P1

- order：53

- section：Study 1

- locator：P1

- move_code：STUDY_OVERVIEW

- paraphrase_cn：Study 1实验室实验比较动态建模与脚本化建模。

- rhetorical_function_cn：聚焦H1。

- depends_on_cn：H1。

- sets_up_cn：描述被试、流程和结果。

- evidence_pointer：Study 1 section

### 54. Procedure P1-P3

- order：54

- section：Study 1

- locator：Procedure P1-P3

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：前测控制随机化和论证能力，写作阶段分别使用ArgueLearn或脚本化工具，后测测量接受度和定性反馈。

- rhetorical_function_cn：说明实验程序如何保证内部有效性。

- depends_on_cn：研究设计总述。

- sets_up_cn：支撑结果解释。

- evidence_pointer：Study 1 procedure; Figure 4

### 55. P1-P2

- order：55

- section：Study 2

- locator：P1-P2

- move_code：STUDY_OVERVIEW

- paraphrase_cn：Study 2采用2×2设计，同时操纵支持方式与任务难度。

- rhetorical_function_cn：聚焦H2/H3。

- depends_on_cn：H2/H3。

- sets_up_cn：描述四组设置和任务难度操作。

- evidence_pointer：Study 2 section; Figure 5; Table 2

### 56. Task difficulty paragraph

- order：56

- section：Study 2

- locator：Task difficulty paragraph

- move_code：BENCHMARK_OR_CONTRAST

- paraphrase_cn：简单任务通过简化句法和措辞生成，并由五位专家验证复杂度差异。

- rhetorical_function_cn：提供操纵检验。

- depends_on_cn：Shehab和Nussbaum理论。

- sets_up_cn：保证任务难度操纵有效。

- evidence_pointer：Study 2 task difficulty validation

### 57. P1-P2

- order：57

- section：Study 3

- locator：P1-P2

- move_code：STUDY_OVERVIEW

- paraphrase_cn：Study 3在真实课堂中设置动态、静态和无建模三组，检验三个月后的技能迁移。

- rhetorical_function_cn：聚焦H4。

- depends_on_cn：H4。

- sets_up_cn：描述现有课程和九次同行评审任务。

- evidence_pointer：Study 3 section; Figure 6

### 58. Posttest paragraph

- order：58

- section：Study 3

- locator：Posttest paragraph

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：后测使用另一论证领域任务判断是否形成可迁移技能而非仅是学写了更 persuasive 的 peer review。

- rhetorical_function_cn：说明迁移测量的必要性。

- depends_on_cn：Toulmin模型和Flender量表。

- sets_up_cn：支撑技能学习而非任务表现的结论。

- evidence_pointer：Study 3 postsurvey phase

### 59. P1-P3

- order：59

- section：Measurement

- locator：P1-P3

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：客观质量根据Toulmin模型和Weinberger/Fischer方案编码，主观质量由外部评分者五级评定。

- rhetorical_function_cn：给出因变量的定义和测量方法。

- depends_on_cn：论证理论。

- sets_up_cn：让结果表格中的数字有明确定义。

- evidence_pointer：Measurement of Persuasive Writing Performance

### 60. H1 Results

- order：60

- section：Results

- locator：H1 Results

- move_code：RESULT

- paraphrase_cn：动态建模组客观和主观论证质量均显著高于脚本建模组。

- rhetorical_function_cn：给出Study 1核心结果。

- depends_on_cn：Study 1设计。

- sets_up_cn：支持H1。

- evidence_pointer：Table 4

### 61. H2/H3 Results

- order：61

- section：Results

- locator：H2/H3 Results

- move_code：RESULT

- paraphrase_cn：动态建模在复杂和简单任务中客观质量均显著高于自适应支持，效应量分别为大和中等；主观质量未达显著。

- rhetorical_function_cn：报告支持/部分支持H2/H3的证据。

- depends_on_cn：Study 2设计。

- sets_up_cn：为讨论部分关于任务难度的解释提供数据。

- evidence_pointer：Tables 5–7

### 62. H4 Results

- order：62

- section：Results

- locator：H4 Results

- move_code：RESULT

- paraphrase_cn：动态建模组在迁移任务中客观质量显著高于静态组和无建模组，但主观质量无显著差异。

- rhetorical_function_cn：报告Study 3核心结果。

- depends_on_cn：Study 3设计。

- sets_up_cn：支持H4并提示主观质量边界。

- evidence_pointer：Tables 8–9

### 63. Post Hoc Analysis

- order：63

- section：Results

- locator：Post Hoc Analysis

- move_code：ROBUSTNESS_OR_BOUNDARY_TEST

- paraphrase_cn：按先前专长均值分割后，三项研究中高低专长组的客观和主观结果均无显著差异。

- rhetorical_function_cn：检验专长边界。

- depends_on_cn：前测数据。

- sets_up_cn：在讨论中强调普适性。

- evidence_pointer：Post Hoc Analysis of Learner Expertise

### 64. Discussion of Findings P1-P3

- order：64

- section：Discussion

- locator：Discussion of Findings P1-P3

- move_code：RESULT

- paraphrase_cn：研究结果显示动态建模在客观论证质量上优于脚本化、自适应、静态和无建模，并支持任务复杂度和专长边界。

- rhetorical_function_cn：汇总研究发现。

- depends_on_cn：全部结果。

- sets_up_cn：为理论贡献和局限做铺垫。

- evidence_pointer：Discussion and Implications, Discussion of Findings

### 65. Theoretical Contributions P1-P3

- order：65

- section：Discussion

- locator：Theoretical Contributions P1-P3

- move_code：CONTRIBUTION

- paraphrase_cn：本文填补了ML动态建模系统缺乏受控实验和长期现场评价的缺口，并将动态建模定位为IS行为建模的推进。

- rhetorical_function_cn：声明理论贡献。

- depends_on_cn：与相关文献对比。

- sets_up_cn：后续具体机制解释和边界。

- evidence_pointer：Discussion, Theoretical Contributions and Practical Implications

### 66. Theoretical Contributions P4-P6

- order：66

- section：Discussion

- locator：Theoretical Contributions P4-P6

- move_code：THEORY_RETURN

- paraphrase_cn：研究结果被解释为支持社会认知理论对复杂任务和观察学习的预测，并扩展该理论到论证写作。

- rhetorical_function_cn：用结果回馈理论。

- depends_on_cn：Study 2/3结果。

- sets_up_cn：为结论中的泛化主张服务。

- evidence_pointer：Discussion, Theory paragraphs

### 67. Theoretical Contributions P7-P9

- order：67

- section：Discussion

- locator：Theoretical Contributions P7-P9

- move_code：BOUNDARY_CONDITION

- paraphrase_cn：主观质量没有一致提高，作者以Toulmin侧重logos而忽视ethos和pathos来解释。

- rhetorical_function_cn：划清效果边界。

- depends_on_cn：Study 2/3主观质量结果。

- sets_up_cn：避免过度声称主观说服提升。

- evidence_pointer：Discussion, subjective argumentation paragraph

### 68. Theoretical Contributions P10-P12

- order：68

- section：Discussion

- locator：Theoretical Contributions P10-P12

- move_code：BOUNDARY_CONDITION

- paraphrase_cn：专长分析没有发现专长逆转，说明动态建模对高低经验学习者同样有效。

- rhetorical_function_cn：进一步界定边界。

- depends_on_cn：后验专长分析。

- sets_up_cn：支持普适性主张。

- evidence_pointer：Discussion, expertise paragraph

### 69. Limitations P1-P2

- order：69

- section：Discussion

- locator：Limitations P1-P2

- move_code：LIMITATION_AND_FUTURE

- paraphrase_cn：研究样本局限于高等教育德文场景，效应可能无法直接迁移到其他领域。

- rhetorical_function_cn：承认外部有效性限制。

- depends_on_cn：研究设计。

- sets_up_cn：未来研究建议。

- evidence_pointer：Limitations, Future Research, and Conclusion

### 70. Limitations P3-P5

- order：70

- section：Discussion

- locator：Limitations P3-P5

- move_code：LIMITATION_AND_FUTURE

- paraphrase_cn：作者讨论伦理、数据隐私、错误反馈和AI素养等问题，并报告WEAT偏差分析。

- rhetorical_function_cn：补充研究的稳健性防护和未来方向。

- depends_on_cn：系统设计伦理。

- sets_up_cn：为该领域后续研究提供议程。

- evidence_pointer：Limitations, Future Research, and Conclusion

### 71. Conclusion paragraph

- order：71

- section：Discussion

- locator：Conclusion paragraph

- move_code：CONTRIBUTION

- paraphrase_cn：研究为基于智能算法的教育反馈应用提供了实证和设计知识，并呼吁未来设计更多智能反馈系统。

- rhetorical_function_cn：以更广泛贡献收束。

- depends_on_cn：全部结果和边界。

- sets_up_cn：无。

- evidence_pointer：Limitations, Future Research, and Conclusion, final paragraph

## 写作技术

- gap_construction_cn：文章采用三层缺口构造：先建立实践缺口（大规模课堂无法提供个别化论证反馈），再建立系统空缺（现有系统以脚本化和静态建模为主，NLP工具缺乏教学评价），最后建立证据缺口（ML动态系统没有被与脚本化、自适应和静态基准在受控与长期现场条件下比较）。

- signposting_cn：摘要预告H1-H4和三项研究；每节开始用‘In study X, our aim was to...’明确目标；表3提供全部研究总览；假设部分在每段末尾以H1-H4收束。

- transition_logic_cn：从实用问题转向IS与NLP的技术可能，再转向理论机制，再转向假设；每个Study以‘既然上一研究确立了X，下一步需要检验Y’的逻辑连接。

- claim_evidence_rhythm：每个假设先给机制论证，再描述对应研究，再展示表格和统计结果，再在讨论中解释边界；结果部分保持克制，讨论部分才提升为理论贡献。

- benchmark_narrative_cn：脚本化建模被先定位为‘大规模标准’，自适应支持被定位为‘更接近个性化但不够动态’，静态/无建模被定位为‘现有IS主流或空白’，动态建模则逐步超越它们。

- theory_return_cn：Discussion将Study 2的任务难度效应回接到社会认知理论对挑战性学习的预测，将Study 3的跨域迁移解释为观察学习四个子过程的实现，并将整个研究定位为SCT从STEM到论证写作的泛化。

- contribution_positioning_cn：贡献被定位为‘首次严格比较动态ML建模与现有基准’、‘证明SCT可泛化’和‘为设计写作技能支持系统提供基础’，而不是单纯说‘我们的系统更好’。

- novelty_protection_cn：通过多重基准、受控+现场实验、跨域迁移测量、效应量、专长边界分析和WEAT偏差分析，把结果提升为设计知识和理论泛化，避免被看作一次性性能报告。

## 可复用研究与写作程序

### structure_steps

#### 1. 1

- step：1

- writing_job_cn：在引言先建立技能的时代重要性和大规模反馈不可扩展的现实痛点。

- research_job_cn：收集技能重要性的政策和市场证据，并描述学习场景中的具体痛点。

- required_evidence_cn：引用技能框架、MOOC规模和辍学统计。

- transition_to_next_cn：从‘需要技能’过渡到‘为什么现有技术不够’。

#### 2. 2

- step：2

- writing_job_cn：综述已有系统并建立分类，指出动态ML系统缺少严谨实验。

- research_job_cn：系统梳理已有论证支持系统，区分静态、脚本化和自适应。

- required_evidence_cn：现有系统列表、各自结果和局限。

- transition_to_next_cn：用‘虽然已有系统，但...’引出理论与假设。

#### 3. 3

- step：3

- writing_job_cn：引入内核理论并推导若干可检验假设。

- research_job_cn：将理论机制翻译为具体设计特征和比较条件。

- required_evidence_cn：理论命题和前人研究支持每个假设。

- transition_to_next_cn：假设结束后自然进入系统实现。

#### 4. 4

- step：4

- writing_job_cn：描述系统架构、界面和ML后端，并提供技术验证。

- research_job_cn：构建系统，准备语料，训练模型，并与强baseline比较。

- required_evidence_cn：任务数据、模型准确率/鲁棒性证据。

- transition_to_next_cn：技术可行后说明需要先做设计评价。

#### 5. 5

- step：5

- writing_job_cn：报告试点和眼动等设计评价，处理错误预测等效度威胁。

- research_job_cn：用用户研究和界面迭代检验可用性，明确错误反馈的边界。

- required_evidence_cn：用户定性反馈、眼动结果、改进措施。

- transition_to_next_cn：系统成熟后进入正式实验。

#### 6. 6

- step：6

- writing_job_cn：用受控实验依次与更接近的基准比较，并加入调节变量。

- research_job_cn：设计随机实验，控制前测变量，测量客观与主观结果。

- required_evidence_cn：组间差异显著性和效应量。

- transition_to_next_cn：若实验室证据成立，则进一步做长期现场检验。

#### 7. 7

- step：7

- writing_job_cn：用长期现场实验和迁移任务证明技能学习，并进行后验边界分析。

- research_job_cn：在真实课程中实施多轮任务，测量另一领域的迁移，检查专长等调节变量。

- required_evidence_cn：长期跟踪数据、组间差异、迁移效果、无显著调节。

- transition_to_next_cn：结果稳定后进入理论贡献和局限。

#### 8. 8

- step：8

- writing_job_cn：回接引言的缺口，声明理论贡献，并坦诚边界和未来研究。

- research_job_cn：将结果提升为设计知识和理论泛化，同时报告偏差分析和局限。

- required_evidence_cn：无明显过度声称，对不一致结果给出解释。

- transition_to_next_cn：无。

### most_transferable_moves_cn

1. 先把脚本化/静态标杆定位为‘现有标准或主流’，再要求新系统与之比较。

2. 每个假设都从理论机制推到可观察结果，避免只罗列H。

3. 技术评价与学习者评价分开报告：先证明‘模型可靠’，再证明‘系统有效’。

4. 以迁移任务测量技能而非单次任务表现。

5. 在结果与讨论之间用效应量、边界条件和定性引语共同保护贡献。

### resource_intensive_or_nonstandard_parts_cn

1. 七年间从真实课堂收集约7,000份学生同行评审并人工标注1,000篇，需要长期课程合作和标注团队。

2. 30个用户访谈和13次眼动研究需要行为实验室和伦理审查。

3. 三个月现场实验需要课程老师配合、系统嵌入教学流程以及处理流失率。

4. SVM、BERT、BiLSTM等多模型比较需要NLP工程投入。

5. 作者团队跨IS、HCI、教育心理学和NLP，非单一研究者可轻易复制。

### what_not_to_copy_superficially_cn

1. 不能只宣称‘动态建模更好’而不提供可运行的模型、语料和对照实验。

2. 不能在主观质量不显著时仍过度声称‘更 persuasive’。

3. 不能把H2/H3写成完全确认，除非所有因变量都显著。

4. 不能把‘跨领域’建立在只有一个迁移任务上。

5. 不能省略错误反馈和算法偏见等效度威胁的讨论。

- single_best_description_of_the_routine_cn：用一个能动态识别论证结构并提供反馈的ML系统，以社会认知理论为内核，通过逐步替换基准（脚本化→自适应→静态/无建模）证明动态建模对论证技能短期与长期、跨领域和不同任务难度的稳健效果。

## 分析边界

全文被完整提供，但缺少在线附录，部分表格的图像信息可能未被完整捕获；Study 3结果文字中的TG编号与表8表头存在不一致（文中一处将动态组写为TG2而表格标为TG1），分析以表格和摘要为准；眼动研究和试点数据只有概述，没有细粒度统计；部分引用如Wambsganss et al. (2020b)的详细标注一致性没有在本文中复述，因此相关技术证据依赖外部文献。
