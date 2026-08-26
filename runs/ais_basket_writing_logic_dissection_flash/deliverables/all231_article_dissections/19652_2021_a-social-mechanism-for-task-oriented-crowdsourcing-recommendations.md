# A social mechanism for task-oriented crowdsourcing recommendations

- 作者：Yung-Ming Li; Chin-Yu Hsieh; Lien-Fa Lin; Chi-Hsuan Wei
- 年份 / 期刊：2021 / Decision Support Systems
- DOI：10.1016/j.dss.2020.113449
- 源文件：19652_2021_a-social-mechanism-for-task-oriented-crowdsourcing-recommendations.md
- 论文主类型：build_evaluate_design_science
- 主导写作弧线：requirements_build_evaluate_design_principles
- 置信度：0.78

## 文章级论证概况

- 核心问题：如何设计一个基于社交机制的任务型众包推荐系统，让请求者既能找到足够适合的贡献者，又能找到高意愿完成任务的人？

- 制品与设计：提出了SCT（Social Crowdsourcing Task）推荐机制，由类型树构建、贡献者池分析、社会影响分析、任务推荐四个模块构成；将贡献者偏好（兴趣、能力、动机）、贡献者历史（浏览/选择/完成/被验收记录）和社会影响（社会隶属、社会亲近度）量化为适合度评分，并用AHP确定三因子权重，最终生成推荐贡献者列表。

- 客观结果：在Facebook数据和Amazon Mechanical Turk/Taskcn任务类型背景下，以138名用户、39个任务进行实验；AHP加权的推荐准确率优于等权和默认权重；SCT模型在请求者满意度、贡献者任务适合度、喜爱度和接受意愿上均显著优于随机、内容、协同和一般平台四种基准。

- 核心贡献：从设计、方法、实证和实践四个角度宣称提出并验证了一个综合贡献者偏好、历史和社会影响的任务型众包社交推荐机制，能够降低搜索成本、提高匹配质量，并帮助请求者与贡献者建立长期合作关系。

- 整篇论证链：文章先指出众包任务平台高度分散、任务大量隐藏，贡献者搜索成本高，难以找到与个人偏好和能力匹配的任务，而现有内容过滤与协同过滤推荐系统无法解决该问题。接着引入社交网络信息作为新信号，认为贡献者的社交活动可推断其偏好，朋友影响和与请求者的社会亲近度可提高任务接受意愿。基于此，作者设计了包含类型树、贡献者偏好/历史分析、社会影响分析和推荐引擎的SCT机制，将三因子通过AHP加权聚合为贡献者适合度。实验实施为基于Facebook登录的Web系统，请求者上传任务、系统生成推荐列表、请求者邀请、贡献者反馈、请求者验收；通过与随机、内容、协同、一般平台模型的对比，在推荐准确率、满意度、任务适合度、喜爱度和接受意愿多项指标上验证SCT表现更好。讨论部分将这些结果重新连接回搜索成本和平台分散问题，宣称机制对请求者、贡献者和平台均有价值，并列出依赖Facebook、冷启动和小样本等边界条件。

## 类型与写作弧线判定

- 论文主类型判定：论文不是从理论命题推导可检验假设，而是基于文献需求设计了一套由类型树、贡献者分析、社会影响和推荐模块组成的推荐机制，再通过现场小规模实验和基准对比评价制品效果，最后总结为设计/方法/实证/实践贡献。这符合“需求—构建—评价—设计知识”的设计科学研究路径。

- 主导写作弧线判定：文章按“任务型众包与推荐系统的不足（需求）—四模块系统框架（构建）—实验与多指标评价（评价）—贡献与边界（设计知识）”组织；每个系统模块都来自可识别的偏好、历史和社会影响需求，并非从理论命题直接导出并验证。

## 研究开展程序

- study_or_phase_count：5

- 研究阶段总序列：第一阶段完成制品构建和适合度公式设计；第二阶段建立实验环境、收集数据并定义基准模型；第三阶段从请求者侧验证推荐被采用和质量被认可；第四、五阶段从贡献者侧验证主观适合度/喜爱度和实际接受意愿。各阶段依次回答“机制如何工作”“在哪里可检验”“对请求者是否有效”“对贡献者是否有效”“是否转化为接受行为”。

### studies_or_phases

#### 1. 机制构建与模块设计（系统框架阶段）

- order：1

- name_cn：机制构建与模块设计（系统框架阶段）

- question_cn：如何将贡献者偏好、历史表现与社会影响转换成可计算的任务-贡献者匹配得分？

- inputs_and_setting_cn：已有众包平台的任务分类、Facebook等社交数据概念、贡献者-任务历史记录、请求者与贡献者之间的社交路径

- designed_or_compared_object_cn：四模块SCT推荐机制：类型树构建、贡献者池分析、社会影响分析、任务推荐引擎

- baseline_control_or_counterfactual_cn：无；以文献中内容/协同过滤推荐的不足作为设计动因

##### objective_metrics

1. Suitability分数的可计算性

2. 各模块公式是否覆盖偏好、历史、社会影响

- analysis_method_cn：概念建模、类型树语义相似度、余弦相似度、0-4贡献者-任务矩阵、AHP多准则聚合

- main_result_cn：提出了包含ContributorPreference、ContributorHistory、SocialInfluence三因子的Suitability(C_i,T_j,R_k)公式，并设计了完整推荐流程

- argumentative_role_cn：产生可被后续实验检验的推荐制品，确立“三个因素同时纳入”的核心设计主张

- remaining_uncertainty_cn：公式与模块的真实推荐效果未知，尚需在真实数据上检验

- link_to_next_phase_cn：自然引出实验：要实现系统、收集社交数据并比较基准

##### evidence_pointers

1. Section 3, Fig.2

2. 3.1 Fig.3

3. 3.2 Equations (1)-(9)

4. 3.3 Equations (10)-(15)

5. 3.4 Equations (16)-(22)

#### 2. 实验环境与数据收集（系统实现、样本、任务、权重）

- order：2

- name_cn：实验环境与数据收集（系统实现、样本、任务、权重）

- question_cn：在哪里、用什么数据、以哪些基准来检验SCT机制？

- inputs_and_setting_cn：Facebook授权用户社交数据、138名参与者、39个任务/13个类型、Amazon Mechanical Turk与Taskcn的任务类型参考

- designed_or_compared_object_cn：基于Facebook登录的Web实验系统；五类推荐模型：随机、内容(CP+CH)、协同(CP+SI)、一般平台(CH+SI)、SCT(CP+CH+SI)

- baseline_control_or_counterfactual_cn：四种基准模型分别代表两两因子组合；三种权重方案（等权、默认、AHP）

##### objective_metrics

1. 样本量

2. 社交行为数据量（likes/tags/comments等）

3. AHP三准则权重

- analysis_method_cn：系统实现、问卷、AHP权重计算、描述性统计、任务类型分类

- main_result_cn：收集138名用户和大量社交行为数据；专业任务中偏好权重0.363最高，非专业任务中社会影响权重0.372最高

- argumentative_role_cn：创建可比较的评价场景，并通过AHP权重给出“为什么社会影响重要”的先验依据；同时定义基准模型为后续SCT对比做铺垫

- remaining_uncertainty_cn：尚不知道SCT是否真的优于基准，也未测贡献者端反应

- link_to_next_phase_cn：进入5.1-5.3的结果评价，先用推荐准确率与满意度检验请求者侧，再用任务邀请反馈检验贡献者侧

##### evidence_pointers

1. Section 4.1 Steps 1-5

2. Section 4.2.1 Table 1

3. Section 4.2.2 Table 2, Fig.6

4. Section 4.2.3 Table 3

5. Section 4.2.4 五个模型定义

#### 3. 请求者侧评价：推荐准确性与贡献满意度

- order：3

- name_cn：请求者侧评价：推荐准确性与贡献满意度

- question_cn：请求者是否采用系统推荐的贡献者，并对这些贡献者提交的工作感到满意？

- inputs_and_setting_cn：推荐列表、请求者实际pickup记录、请求者对贡献者工作的approve记录

- designed_or_compared_object_cn：AHP/Default/Equal三种权重；SCT与随机、内容、协同、一般平台四种基准

- baseline_control_or_counterfactual_cn：随机、内容(CP+CH)、协同(CP+SI)、一般平台(CH+SI)

##### objective_metrics

1. Accuracy = 推荐列表中被pickup人数 / 推荐列表人数

2. Satisfaction = 被pickup且approve人数 / 被pickup人数

- analysis_method_cn：比例计算、配对样本t检验、95%置信区间

- main_result_cn：AHP加权准确率显著高于等权和默认权重；SCT在贡献满意度上显著高于其他四种基准模型

- argumentative_role_cn：证明推荐机制对请求者具有实用价值：推荐的人不仅被选中，而且工作质量被接受

- remaining_uncertainty_cn：贡献者是否认为任务合适、是否愿意接受邀请仍未知

- link_to_next_phase_cn：转向贡献者视角：任务邀请的适合度、喜爱度和接受意愿

##### evidence_pointers

1. 5.1.1 Formula (23), Fig.7, Table 4

2. 5.1.2 Formula (24), Algorithm 1, Fig.8, Table 5

#### 4. 贡献者侧主观评价：任务邀请适合度与喜爱度

- order：4

- name_cn：贡献者侧主观评价：任务邀请适合度与喜爱度

- question_cn：被推荐的贡献者是否认为收到的任务邀请适合自己，并且喜欢该任务邀请？

- inputs_and_setting_cn：贡献者收到任务邀请后填写的问卷反馈，采用1-5量表

- designed_or_compared_object_cn：SCT与随机、内容、协同、一般平台四种基准

- baseline_control_or_counterfactual_cn：同上四种基准

##### objective_metrics

1. Fitness of task invitation（任务适合度）

2. Liking for task invitation（任务喜爱度）

- analysis_method_cn：问卷均值比较、配对样本t检验

- main_result_cn：SCT在任务适合度和喜爱度上均最高，随机模型最低，且差异显著

- argumentative_role_cn：从贡献者主观感受补充请求者侧证据，说明推荐结果不只是“完成任务”，而是真正匹配贡献者兴趣

- remaining_uncertainty_cn：主观喜欢不一定转化为接受邀请的行为

- link_to_next_phase_cn：测实际接受意愿，将主观态度转化为行为证据

##### evidence_pointers

1. 5.2.1 Fig.9, Table 6

2. 5.3.2 Fig.10, Table 7

#### 5. 贡献者侧行为评价：任务邀请接受意愿

- order：5

- name_cn：贡献者侧行为评价：任务邀请接受意愿

- question_cn：贡献者是否实际接受了系统推荐带来的任务邀请？

- inputs_and_setting_cn：任务邀请记录、贡献者接受/拒绝记录

- designed_or_compared_object_cn：SCT与随机、内容、协同、一般平台四种基准

- baseline_control_or_counterfactual_cn：同上四种基准

##### objective_metrics

1. Willingness = 接受的任务邀请数 / 收到的任务邀请数

- analysis_method_cn：接受率计算、配对样本t检验

- main_result_cn：SCT的任务邀请接受意愿显著高于其他模型

- argumentative_role_cn：将主观匹配转化为实际接受行为，闭合“请求者推荐准确—贡献者接受邀请”的匹配闭环

- remaining_uncertainty_cn：长期合作、平台收益、更大规模部署效果未测

- link_to_next_phase_cn：进入讨论与结论，总结贡献、边界与未来研究

##### evidence_pointers

1. 5.3.3 Formula (25), Fig.11, Table 8

## 各部分修辞架构

### abstract_moves

1. CONTEXT: 众包是利用互联网群体智慧解决人力密集型问题的趋势

2. PRACTICAL_STAKES: 众包平台分散、多数任务隐藏，贡献者难以找到匹配偏好与能力的任务

3. RQ_OR_OBJECTIVE: 目标是设计任务型众包推荐的社会机制，使请求者容易找到合适且愿意完成任务的贡献者

4. RESULT: 实验显示所提机制能有效识别不同类型任务型众包参与者的合适贡献者

### introduction_moves

1. CONTEXT: 众包源于外包/开放创新，产生多种商业模式，包含请求者与贡献者两类参与者

2. PHENOMENON: 贡献者通常只看任务列表前几页，搜索范围有限

3. PRACTICAL_STAKES: 高搜索成本损害众包效率和结果质量，请求者不满会离开平台

4. LIMITATION: 基于内容与协同过滤的既有推荐系统无法令人满意地解决众包特殊问题

5. RQ_OR_OBJECTIVE: 提出社交机制，并分解为“识别合适贡献者”和“提高完成意愿”两个研究问题

6. MECHANISM: 社交网络中的兴趣、能力和参与动机可用于推断贡献者偏好

7. MECHANISM: 朋友的任务兴趣和请求者-贡献者亲近度会提高贡献者接受任务的可能性

8. DESIGN_FEATURE: 机制同时考虑贡献者偏好、贡献者历史和社会影响三个因素

9. STUDY_OVERVIEW: 说明后续章节安排

### theory_and_knowledge_moves

1. PRIOR_KNOWLEDGE: 任务型众包包含请求者/贡献者，任务分专业和非专业

2. LIMITATION: 预算感知任务分配只考虑部分因素，主要关注偏好

3. PRIOR_KNOWLEDGE: 推荐系统分为内容过滤与协同过滤，协同过滤存在稀疏性、可扩展性和效率问题

4. PRIOR_KNOWLEDGE: 社交推荐系统利用社会关系和社会影响可提升推荐质量

5. THEORY_PROPOSITION: 相似兴趣与强关系关联，朋友的任务兴趣会传导给其他用户

6. THEORY_PROPOSITION: 贡献者与请求者关系越亲近，越可能帮助请求者完成任务

### artifact_design_moves

1. REQUIREMENT: 用类型树统一描述任务类型与贡献者偏好

2. DESIGN_FEATURE: 将签到、主页、点赞、评论等社交活动转换为兴趣信号，并用余弦相似度计算类型匹配

3. DESIGN_FEATURE: 用英文能力、教育背景、计算机能力衡量贡献者能力并归一化

4. DESIGN_FEATURE: 根据金钱、学习、娱乐动机调节贡献者偏好权重

5. DESIGN_FEATURE: 用0-4贡献者-任务矩阵记录浏览、选择、完成、被验收四层历史表现

6. MECHANISM: 社会隶属通过朋友的互动强度影响贡献者对任务的兴趣

7. DESIGN_FEATURE: 社会亲近度取贡献者-请求者路径上互动强度乘积最大值

8. DESIGN_FEATURE: 用AHP将请求者对偏好、历史、社会影响的成对比较转化为权重，并聚合为Suitability

### evaluation_moves

1. METHOD_JUSTIFICATION: 用Facebook收集社交信息，以Amazon Mechanical Turk和Taskcn作为任务型众包平台参考

2. STUDY_OVERVIEW: 设计五个实验步骤：系统实现、任务上传、分类与AHP、推荐/反馈、请求者验收

3. RESULT: 138名参与者及大规模社交行为数据被收集

4. RESULT: AHP权重显示专业任务偏好更重要，非专业任务社会影响更重要

5. BENCHMARK_OR_CONTRAST: 定义随机、内容(CP+CH)、协同(CP+SI)、一般平台(CH+SI)、SCT(CP+CH+SI)五个模型

6. RESULT: AHP加权准确率显著高于等权/默认

7. RESULT: SCT在贡献满意度上显著高于四种基准

8. RESULT: SCT在任务适合度、喜爱度、接受意愿上均最高且显著

9. ROBUSTNESS_OR_BOUNDARY_TEST: 分专业/非专业类型展示结果，并解释非专业满意度更高的原因

### discussion_and_contribution_moves

1. CONTRIBUTION: 总结机制由偏好、历史、社会影响三方面构成，实验结果证明优于基准

2. CONTRIBUTION: 实践层面：系统帮助请求者找到合适人力并建立长期合作

3. CONTRIBUTION: 方法层面：少有人提出基于社交的任务型众包推荐，三因素同时使用效果最好

4. CONTRIBUTION: 实证层面：整合社交与平台数据证明多指标改善

5. CONTRIBUTION: 实践层面：降低搜索成本，吸引更多请求者与贡献者进入平台

6. BOUNDARY_CONDITION: 依赖Facebook；新用户/社交活动少时性能受损；隐私限制能力信息；冷启动；样本量小于真实群体

7. LIMITATION_AND_FUTURE: 未来加入更多社交互动、Reactions情感分析、多平台集成、移动众包与情境/位置因素

## 理论/知识到设计的翻译

### 知识/理论基础

1. 任务型众包概念：请求者/贡献者、专业/非专业任务、预算感知任务分配

2. 行为经济学/众包动机：金钱、学习、休闲是主要参与动机

3. 推荐系统理论：内容过滤、协同过滤的局限和社交推荐的优势

4. 社会影响理论：社会隶属网络中的兴趣传导、社会亲近度影响助人意愿

5. 信息检索/分类：类型树、语义相似度、余弦相似度

6. 多准则决策：AHP用于请求者偏好/历史/社会影响的权重聚合

- 理论—设计耦合：partial

- 耦合判定理由：社会影响理论确实为“社会隶属+社会亲近度”模块提供了方向，众包动机知识也进入偏好权重；但具体公式（签到/点赞/主页/评论相加、互动强度求和、路径乘积等）主要是工程性操作化，且实验不检验理论命题本身，只对比整体机制优劣，因此属于部分耦合，而非理论前瞻决定设计。

- 理论到设计翻译链：众包平台分散与搜索成本问题 → 需要比内容/协同过滤更强的匹配信号 → 社交活动作为偏好代理 → 类型树将社交数据映射为任务类型兴趣 → 历史矩阵将过往表现作为能力代理 → 社会影响理论将朋友互动和请求者亲近度转化为参与意愿信号 → AHP将请求者偏好权重化 → 三因子聚合为Suitability → 生成推荐列表 → 实验用四类基准对比验证。

### mapping_table

#### 1. 1

- theory_or_knowledge_claim_cn：众包参与者有不同动机（金钱、学习、休闲），偏好和能力决定任务匹配

- mechanism_cn：贡献者的兴趣、能力、动机会影响其选择任务和完成任务质量

- design_requirement_cn：推荐机制必须估计贡献者偏好，并区分不同动机

- artifact_choice_cn：SocialInterest汇总签到/主页/点赞/评论；能力用英文/教育/计算机；动机向量调节权重

- evaluated_contrast_cn：内容基准模型只含偏好与历史(CP+CH)，SCT全含偏好/历史/社会影响

- objective_result_cn：SCT在请求者满意度和贡献者接受意愿等指标上最高；专业任务偏好权重0.363

##### evidence_pointers

1. 3.2.1 Equations (1)-(8)

2. 4.2.3 Table 3

3. 5.1.2 Fig.8

4. 5.3.3 Fig.11

#### 2. 2

- theory_or_knowledge_claim_cn：过去表现是未来表现的良好预测器；浏览、选择、完成、被验收反映兴趣与能力

- mechanism_cn：任务历史记录形成贡献者能力/兴趣的证据链

- design_requirement_cn：推荐应纳入贡献者历史而非只看静态偏好

- artifact_choice_cn：贡献者-任务矩阵0-4分，ContributorHistory按类型聚合

- evaluated_contrast_cn：一般平台基准模型只含历史与社会影响(CH+SI)，SCT同时包含偏好

- objective_result_cn：SCT在适合度、喜爱度、接受意愿上显著优于一般平台基准

##### evidence_pointers

1. 3.2.2 Fig.4

2. 4.2.4 benchmark定义

3. 5.2.1 Fig.9

4. 5.3.3 Fig.11

#### 3. 3

- theory_or_knowledge_claim_cn：强关系朋友之间兴趣相似，朋友的任务兴趣会传导；与请求者亲近会增加帮助意愿

- mechanism_cn：社交影响通过社会隶属影响兴趣，通过社会亲近度影响接受任务意愿

- design_requirement_cn：推荐机制必须量化社会隶属与社会亲近度

- artifact_choice_cn：Tag/Comment/Like/MutualFriend互动强度、SocialAffiliationInterest公式、路径乘积SocialCloseness、线性组合SocialInfluence

- evaluated_contrast_cn：协同过滤基准含偏好与社会影响(CP+SI)，一般平台含历史与社会影响(CH+SI)，SCT三因子齐全

- objective_result_cn：非专业任务社会影响权重0.372高于专业任务0.293；SCT任务接受意愿显著最高

##### evidence_pointers

1. 3.3.1 Equations (10)-(11)

2. 3.3.2 Equations (12)-(15)

3. 4.2.3 Table 3

4. 5.3.3 Fig.11

#### 4. 4

- theory_or_knowledge_claim_cn：内容过滤和协同过滤在稀疏性、可扩展性和显式偏好获取上有局限

- mechanism_cn：需要额外社交信号弥补用户显式偏好缺失

- design_requirement_cn：从社交平台整合用户生成内容作为偏好信号

- artifact_choice_cn：类型树+余弦相似度将社交活动关键词化为类型偏好

- evaluated_contrast_cn：内容基准(CP+CH)与协同基准(CP+SI)缺乏社交信号整合或历史信号

- objective_result_cn：SCT在满意度、适合度、喜爱度、接受意愿上均优于内容与协同基准

##### evidence_pointers

1. 2.2 推荐系统局限

2. 3.2.1 Formula (2)

3. 5.1.2 Table 5

4. 5.2.1 Table 6

#### 5. 5

- theory_or_knowledge_claim_cn：多准则决策中，不同请求者对匹配标准有不同偏好；AHP可整合成一致权重

- mechanism_cn：请求者的主观重要性判断转化为偏好/历史/社会影响的线性权重

- design_requirement_cn：最终适合度必须按请求者给定的权重聚合

- artifact_choice_cn：AHP成对比较矩阵、特征向量法求权重、Suitability公式

- evaluated_contrast_cn：等权、默认权重、AHP权重三种方案

- objective_result_cn：AHP加权准确率显著高于等权与默认

##### evidence_pointers

1. 3.4.2 Equations (18)-(22)

2. 4.2.3 Table 3

3. 5.1.1 Fig.7, Table 4

## 评价逻辑

### evaluation_modes

1. 现场小规模系统实验：真实Facebook授权数据、真实任务上传/邀请/验收流程

2. 基于两个大型众包平台任务类别的模拟任务池

3. 行为结果指标：推荐准确率、请求者满意度、贡献者接受意愿

4. 主观反馈指标：任务适合度、任务喜爱度

5. 统计检验：配对样本t检验

6. 基准对比：随机、内容(CP+CH)、协同(CP+SI)、一般平台(CH+SI)

- why_these_evaluations_cn：由于推荐机制同时面向请求者和贡献者，单一准确率不能证明双方都受益。因此先用准确率和满意度证明“请求者采纳且认可结果”，再用适合度、喜爱度和接受意愿证明“贡献者认为匹配且实际愿意接受”。评价指标从请求者侧延伸到贡献者侧，形成完整匹配验证。

- benchmark_and_contrast_chain_cn：四种基准模型分别代表不同两因子组合：内容基准=偏好+历史（缺社会影响），协同基准=偏好+社会影响（缺历史），一般平台=历史+社会影响（缺偏好），随机=无模型。SCT为三因子全模型；权重方案则对比等权、默认和AHP。每个结果小节重复“SCT vs 四基准”的t检验，使证据在多项指标上累积，也让三因子整合的必要性反复出现。

### claim_evidence_ledger

#### 1. 1

- claim：本文提出的SCT机制在多项推荐效果指标上优于随机、内容、协同和一般平台模型

- evidence：Fig.7-11和Table 4-8的均值比较与配对样本t检验

- assessment：在该小规模实验样本内有统计支持，但未在真实大型平台随机部署验证

#### 2. 2

- claim：AHP权重优于默认/等权权重

- evidence：5.1.1中AHP与等权、默认的配对t检验，Table 4

- assessment：统计上支持，但仅用于推荐准确率一个指标

#### 3. 3

- claim：同时纳入偏好、历史、社会影响三因子比任意两因子组合更有效

- evidence：基准模型分别省略一个因子，SCT全部包含并在满意度/适合度/喜爱度/意愿上均优于每个基准

- assessment：间接支持，但缺少正式的消融实验控制；基准模型可能还有其他工程差异

#### 4. 4

- claim：社会影响机制通过社会隶属和社会亲近度提高贡献者接受意愿

- evidence：非专业任务中社会影响权重更高；SCT接受意愿最高

- assessment：整体相关支持，但未对社会亲近度或社会隶属做中介/调节检验，机制路径未被直接证明

#### 5. 5

- claim：机制能建立长期合作并为平台创造价值

- evidence：讨论部分的推论，无纵向数据

- assessment：属于未来价值主张，未在实验中测量

- internal_validity_strategy_cn：使用配对样本t检验，使同一批用户/请求者在同一实验环境下面对不同推荐模型，减少个体差异；统一实验流程、问卷和系统实现保证条件一致；AHP问卷将请求者主观权重量化，减少随意等权。

- external_validity_strategy_cn：选取Facebook作为社交数据来源，以Amazon Mechanical Turk和Taskcn作为众包平台参考；任务覆盖专业/非专业13类；按专业/非专业分别报告结果；样本量高于部分同类实地研究。

- what_is_not_actually_tested_cn：未在真实大型众包平台上进行大规模部署；没有随机分配请求者/贡献者的严格现场因果设计；社会影响机制的社会隶属/社会亲近度路径未被直接中介检验；长期合作、平台收益、冷启动用户表现、多平台泛化均未直接测量。

## 贡献闭环

- technical_claim_cn：SCT机制在当前实验数据上比随机、内容、协同、一般平台模型获得更高准确率、满意度、任务适合度、喜爱度和接受意愿。

- artifact_claim_cn：同时纳入贡献者偏好、历史和社会影响的推荐制品优于只使用其中两因子的基准制品；AHP加权比等权/默认更准确。

- mechanism_claim_cn：社会影响通过社会隶属（朋友兴趣传导）和社会亲近度（与请求者的关系）提高贡献者的任务兴趣和接受意愿。

- boundary_claim_cn：机制适用于Facebook等社交数据可获取的环境、Amazon Mechanical Turk/Taskcn类任务型众包、专业/非专业两类任务；社交活动稀疏的新用户、隐私受限数据、小规模样本和冷启动条件下效果受限。

- reusable_design_knowledge_cn：类型树统一任务与偏好、社交行为关键词化、贡献者-任务历史0-4矩阵、社会隶属/亲近度计算、AHP多准则权重聚合，可作为任务型众包社交推荐的可复用设计构件。

- theoretical_contribution_cn：将社会影响理论引入任务型众包推荐，用社会隶属和社会亲近度作为贡献者意愿的操作化变量，扩展了社交推荐在crowdsourcing领域的应用。

- how_discussion_closes_intro_gap_cn：讨论开篇重述任务型众包趋势和搜索匹配成本问题，随后将实验优势归结为偏好/历史/社会影响的整合，直接回应引言中“内容/协同过滤不能解决”的缺口，并宣称该机制能为请求者、贡献者和平台创造价值。

- overclaim_or_unsupported_leaps_cn：从“显著高于基准”跳跃到“建立长期合作/平台利润”缺乏时间序列或平台收入证据；“三因子同时使用是perfect results”属于过度措辞；机制解释主要靠整体差异和非专业任务的权重差异，不是对中介机制的直接检验；某些公式和评价细节在预印本中有乱码，降低了可复现性强度。

## 句级写作动作图谱

### 1. Abstract P1 S1

- order：1

- section：Abstract

- locator：Abstract P1 S1

- move_code：CONTEXT

- paraphrase_cn：众包成为利用互联网群体智慧解决大量人力需求问题的新趋势。

- rhetorical_function_cn：首句将文章置于众包大背景，建立话题相关性。

- depends_on_cn：无需前置，直接引入

- sets_up_cn：为随后指出众包中的搜索和匹配问题提供背景

- evidence_pointer：Abstract

### 2. Abstract P1 S2-S3

- order：2

- section：Abstract

- locator：Abstract P1 S2-S3

- move_code：PRACTICAL_STAKES

- paraphrase_cn：众包平台众多但分散，多数任务隐藏，贡献者难以找到匹配个人偏好与能力的任务。

- rhetorical_function_cn：提出实际痛点，使研究有现实价值。

- depends_on_cn：前一句众包趋势

- sets_up_cn：引出推荐机制的必要性

- evidence_pointer：Abstract

### 3. Abstract P1 S4

- order：3

- section：Abstract

- locator：Abstract P1 S4

- move_code：RQ_OR_OBJECTIVE

- paraphrase_cn：本文目标是设计任务型众包推荐的社会机制，让请求者容易找到合适且愿意完成任务的贡献者。

- rhetorical_function_cn：明确研究目标。

- depends_on_cn：前两句的匹配痛点

- sets_up_cn：预告制品为社交推荐机制

- evidence_pointer：Abstract

### 4. Abstract P2 S1

- order：4

- section：Abstract

- locator：Abstract P2 S1

- move_code：RESULT

- paraphrase_cn：实验结果表明该机制能有效识别不同任务型众包参与者类型下的合适贡献者。

- rhetorical_function_cn：在摘要中给出实证结论。

- depends_on_cn：研究目标

- sets_up_cn：让读者预期后面有实验证据

- evidence_pointer：Abstract

### 5. Introduction P1 S1-S4

- order：5

- section：Introduction

- locator：Introduction P1 S1-S4

- move_code：CONTEXT

- paraphrase_cn：众包以群体智慧解决复杂问题，依托匿名社区和外包服务降低时间成本，产生多种商业模式。

- rhetorical_function_cn：从宽泛趋势过渡到具体任务型众包。

- depends_on_cn：众包概念

- sets_up_cn：引入请求者和贡献者两个角色

- evidence_pointer：Introduction

### 6. Introduction P1 S5

- order：6

- section：Introduction

- locator：Introduction P1 S5

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：任务型众包包含两类对象：公开发布任务的请求者和自愿贡献的贡献者。

- rhetorical_function_cn：给出核心术语定义，避免歧义。

- depends_on_cn：众包背景

- sets_up_cn：后文所有匹配问题围绕这两类主体

- evidence_pointer：Introduction P1

### 7. Introduction P2 S1-S2

- order：7

- section：Introduction

- locator：Introduction P2 S1-S2

- move_code：PHENOMENON

- paraphrase_cn：任务型众包平台分散，多数任务对大众隐藏，贡献者往往只看任务列表前几页就做选择。

- rhetorical_function_cn：描述经验现象，说明搜索局限。

- depends_on_cn：平台分散的现实

- sets_up_cn：为搜索成本高、效率受损做铺垫

- evidence_pointer：Introduction P2

### 8. Introduction P2 S3-S4

- order：8

- section：Introduction

- locator：Introduction P2 S3-S4

- move_code：PRACTICAL_STAKES

- paraphrase_cn：在MTurk等市场，任务页面数量很大；高搜索成本会降低众包效率和结果质量，请求者不满可能离开，平台损失收入与未来机会。

- rhetorical_function_cn：把现象后果放大为平台与请求者均受损。

- depends_on_cn：上一句搜索范围有限

- sets_up_cn：说明推荐机制具有经济和平台价值

- evidence_pointer：Introduction P2

### 9. Introduction P2 S5

- order：9

- section：Introduction

- locator：Introduction P2 S5

- move_code：LIMITATION

- paraphrase_cn：已有研究指出贡献者很难找到匹配偏好与能力的任务，即使平台提供一些选择机制。

- rhetorical_function_cn：指出既有平台/研究的不足。

- depends_on_cn：搜索成本问题

- sets_up_cn：为引入推荐系统作铺垫

- evidence_pointer：Introduction P2

### 10. Introduction P3 S1-S2

- order：10

- section：Introduction

- locator：Introduction P3 S1-S2

- move_code：RQ_OR_OBJECTIVE

- paraphrase_cn：有效推荐机制可以解决该问题，但众包特性使内容过滤和协同过滤均不能令人满意，因此本文设计社交机制。

- rhetorical_function_cn：将一般问题收缩为推荐技术缺口，并预告解决方案。

- depends_on_cn：搜索成本与既有推荐不足

- sets_up_cn：引出社交网络作为新信息源

- evidence_pointer：Introduction P3

### 11. Introduction P3 S3

- order：11

- section：Introduction

- locator：Introduction P3 S3

- move_code：RQ_OR_OBJECTIVE

- paraphrase_cn：利用社交网络实现众包推荐需要解决两个问题：如何识别合适且感兴趣的贡献者，如何用社会影响提高完成意愿。

- rhetorical_function_cn：把研究目标拆解成两个可处理的问题。

- depends_on_cn：社交机制方案

- sets_up_cn：后文分别对应偏好分析和社交影响模块

- evidence_pointer：Introduction P3

### 12. Introduction P4 S1-S3

- order：12

- section：Introduction

- locator：Introduction P4 S1-S3

- move_code：MECHANISM

- paraphrase_cn：贡献者偏好并非显式给出，但社交活动以及搜索/表现历史可推断其兴趣、能力和参与动机。

- rhetorical_function_cn：解释为什么社交数据能补足偏好信号。

- depends_on_cn：偏好是推荐主要因素

- sets_up_cn：为贡献者池分析模块提供依据

- evidence_pointer：Introduction P4

### 13. Introduction P5 S1-S3

- order：13

- section：Introduction

- locator：Introduction P5 S1-S3

- move_code：MECHANISM

- paraphrase_cn：众包是向陌生人征集贡献，但如果贡献者的朋友对某类任务有兴趣或有经验，贡献者也会更可能感兴趣；与请求者关系更近会提高接受任务的可能性。

- rhetorical_function_cn：说明社交影响如何作用于贡献者意愿。

- depends_on_cn：社交网络中的强关系影响

- sets_up_cn：为社交影响力模块提供理论依据

- evidence_pointer：Introduction P5

### 14. Introduction P6 S1

- order：14

- section：Introduction

- locator：Introduction P6 S1

- move_code：DESIGN_FEATURE

- paraphrase_cn：拟议机制考虑三个因素：贡献者偏好、贡献者历史、社会影响。

- rhetorical_function_cn：给出制品的核心设计摘要。

- depends_on_cn：两个研究问题的解决途径

- sets_up_cn：后文系统框架的三条分析主线

- evidence_pointer：Introduction P6

### 15. Introduction P6 S2-S3

- order：15

- section：Introduction

- locator：Introduction P6 S2-S3

- move_code：PRACTICAL_STAKES

- paraphrase_cn：该机制可降低搜索成本、提升贡献者参与动机，并为请求者、贡献者和平台创造长期合作价值。

- rhetorical_function_cn：在提出机制后立刻给出更高层面的收益。

- depends_on_cn：三因子机制

- sets_up_cn：讨论部分关于平台价值的表述

- evidence_pointer：Introduction P6

### 16. Introduction P7 S1

- order：16

- section：Introduction

- locator：Introduction P7 S1

- move_code：STUDY_OVERVIEW

- paraphrase_cn：说明后续章节安排：文献、系统框架、实验、结果、讨论。

- rhetorical_function_cn：为读者提供阅读路线图。

- depends_on_cn：论文整体结构

- sets_up_cn：无后续实质内容，仅结构预告

- evidence_pointer：Introduction P7

### 17. 2.1 P1

- order：17

- section：Related literature 2.1

- locator：2.1 P1

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：众包是把传统由指定执行者完成的任务通过公开呼叫外包给不确定大群体的行为，来源包括开放创新。

- rhetorical_function_cn：定义核心概念并建立文献基础。

- depends_on_cn：众包趋势

- sets_up_cn：区分任务型众包和请求者/贡献者角色

- evidence_pointer：Section 2.1

### 18. 2.1 P2

- order：18

- section：Related literature 2.1

- locator：2.1 P2

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：众包任务分为需要专业技能的专业任务和可拆分给劳动力完成的大规模非专业任务。

- rhetorical_function_cn：为后文类型树和专业/非专业权重差异提供分类框架。

- depends_on_cn：任务型众包定义

- sets_up_cn：实验任务分类和AHP权重分析

- evidence_pointer：Section 2.1

### 19. 2.1 P3

- order：19

- section：Related literature 2.1

- locator：2.1 P3

- move_code：LIMITATION

- paraphrase_cn：预算感知任务分配等已有研究只考虑部分因素且侧重偏好，本文结合偏好和社会因素推荐高适配贡献者。

- rhetorical_function_cn：指出既有任务分配工作的缺口。

- depends_on_cn：对已有众包研究的回顾

- sets_up_cn：说明本文新增社会因素

- evidence_pointer：Section 2.1

### 20. 2.2 P1

- order：20

- section：Related literature 2.2

- locator：2.2 P1

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：推荐系统分为内容过滤和协同过滤；协同过滤存在评分稀疏、可扩展性和效率限制。

- rhetorical_function_cn：建立既有推荐方法及其缺陷的知识背景。

- depends_on_cn：推荐系统文献

- sets_up_cn：后文说明为什么需要社交机制

- evidence_pointer：Section 2.2

### 21. 2.2 P2

- order：21

- section：Related literature 2.2

- locator：2.2 P2

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：社交推荐系统分析社会关系并利用社会影响提升推荐质量，已被证明能显著改善推荐。

- rhetorical_function_cn：为本文做法提供已有成功证据。

- depends_on_cn：社交网络发展

- sets_up_cn：将社交机制用于众包推荐

- evidence_pointer：Section 2.2

### 22. 2.2 P3

- order：22

- section：Related literature 2.2

- locator：2.2 P3

- move_code：GAP

- paraphrase_cn：任务众包的成功取决于任务类型、贡献者偏好/能力和社会关系，因此本文开发社交机制支持任务众包推荐。

- rhetorical_function_cn：将一般社交推荐推进到任务型众包场景，构造缺口。

- depends_on_cn：推荐系统和社会推荐知识

- sets_up_cn：系统框架的设计目标

- evidence_pointer：Section 2.2

### 23. 2.3 P2

- order：23

- section：Related literature 2.3

- locator：2.3 P2

- move_code：MECHANISM

- paraphrase_cn：如果用户对某任务有兴趣，强联系朋友更可能同样感兴趣；贡献者与请求者关系越近，越可能帮助完成任务。

- rhetorical_function_cn：明确社会影响理论在众包场景中的因果机制。

- depends_on_cn：社会影响理论

- sets_up_cn：社会隶属/社会亲近度两大计算方向

- evidence_pointer：Section 2.3

### 24. 2.3 P3

- order：24

- section：Related literature 2.3

- locator：2.3 P3

- move_code：THEORY_PROPOSITION

- paraphrase_cn：本文使用前述理论计算贡献者与请求者之间的社会关系，以纳入社会隶属和社会亲近度。

- rhetorical_function_cn：将文献理论收束为本文设计原则。

- depends_on_cn：社会影响理论

- sets_up_cn：系统框架的社交影响分析模块

- evidence_pointer：Section 2.3

### 25. Section 3 intro

- order：25

- section：System framework

- locator：Section 3 intro

- move_code：DESIGN_FEATURE

- paraphrase_cn：开发的社会推荐机制分析贡献者偏好、历史表现和社会影响，帮助双方找长期伙伴并提升平台盈利能力。

- rhetorical_function_cn：总起系统框架并重复价值主张。

- depends_on_cn：引言的机制设想

- sets_up_cn：引出四个模块和四个流程步骤

- evidence_pointer：Section 3, Fig.1

### 26. Section 3 process list

- order：26

- section：System framework

- locator：Section 3 process list

- move_code：REQUIREMENT

- paraphrase_cn：流程为：请求者提交并分类任务、系统测量贡献者适合度、生成推荐列表、请求者选择并邀请。

- rhetorical_function_cn：说明推荐机制的实际操作流程。

- depends_on_cn：总体机制设计

- sets_up_cn：实验步骤与之一一对应

- evidence_pointer：Section 3, Fig.1

### 27. Section 3 module overview

- order：27

- section：System framework

- locator：Section 3 module overview

- move_code：DESIGN_FEATURE

- paraphrase_cn：系统由四个模块组成：类型树构建、贡献者池分析、社会影响分析、任务推荐引擎。

- rhetorical_function_cn：给读者系统结构地图。

- depends_on_cn：综合需求

- sets_up_cn：按模块详细展开

- evidence_pointer：Section 3, Fig.2

### 28. 3.1 P1

- order：28

- section：System framework 3.1

- locator：3.1 P1

- move_code：REQUIREMENT

- paraphrase_cn：用分层树结构对任务和贡献者偏好分类，越靠近叶节点越具体，并参考产品分类和语义相似性研究。

- rhetorical_function_cn：为统一任务类型和偏好提供一个稳定分类结构。

- depends_on_cn：专业/非专业任务分类

- sets_up_cn：后续语义相似度计算的基础

- evidence_pointer：Section 3.1, Fig.3

### 29. 3.2.1 interests

- order：29

- section：System framework 3.2.1

- locator：3.2.1 interests

- move_code：MECHANISM

- paraphrase_cn：贡献者兴趣可从签到、主页、点赞和评论等社交活动推断。

- rhetorical_function_cn：说明社交数据成为兴趣代理。

- depends_on_cn：贡献者偏好作为关键因子

- sets_up_cn：SocialInterest计算公式

- evidence_pointer：Section 3.2.1, Equation (1)

### 30. 3.2.1 similarity

- order：30

- section：System framework 3.2.1

- locator：3.2.1 similarity

- move_code：DESIGN_FEATURE

- paraphrase_cn：将社交数据映射到类型树，用余弦相似度计算贡献者与任务类型的相似度，并给出Design与C向量示例。

- rhetorical_function_cn：把原始社交行为转化为可计算偏好相似度。

- depends_on_cn：类型树结构

- sets_up_cn：兴趣得分 = 社交兴趣 × 相似度

- evidence_pointer：Section 3.2.1, Equation (2), Fig.4-5

### 31. 3.2.1 capacity

- order：31

- section：System framework 3.2.1

- locator：3.2.1 capacity

- move_code：DESIGN_FEATURE

- paraphrase_cn：能力用英文、教育、计算机三项分级打分并归一化，能力不足的贡献者不作推荐。

- rhetorical_function_cn：将贡献者能力操作化为可量化资格过滤条件。

- depends_on_cn：贡献者偏好包含能力维度

- sets_up_cn：偏好得分中加入能力项

- evidence_pointer：Section 3.2.1, Equations (4)-(7)

### 32. 3.2.1 motivation

- order：32

- section：System framework 3.2.1

- locator：3.2.1 motivation

- move_code：THEORY_PROPOSITION

- paraphrase_cn：贡献者的主要参与动机是金钱，还包括学习和休闲，不同动机应赋予不同权重。

- rhetorical_function_cn：引入动机理论来区分贡献者偏好权重。

- depends_on_cn：众包动机文献

- sets_up_cn：贡献者偏好对任务价值的加权

- evidence_pointer：Section 3.2.1, Equation (8)

### 33. 3.2.2

- order：33

- section：System framework 3.2.2

- locator：3.2.2

- move_code：MECHANISM

- paraphrase_cn：浏览、选择、完成、被验收四层历史分别反映兴趣、偏好、完成能力和产出质量，用0-4矩阵记录。

- rhetorical_function_cn：把平台行为历史转换为能力/兴趣证据。

- depends_on_cn：过去表现预测未来表现

- sets_up_cn：ContributorHistory聚合公式

- evidence_pointer：Section 3.2.2, Fig.4, Equation (9)

### 34. 3.3.1 affiliation

- order：34

- section：System framework 3.3.1

- locator：3.3.1 affiliation

- move_code：MECHANISM

- paraphrase_cn：朋友之间互动越强，社交影响越大；如果朋友喜欢并分享任务，贡献者也会产生兴趣。

- rhetorical_function_cn：说明社会隶属网络为什么能够传导兴趣。

- depends_on_cn：社会影响理论

- sets_up_cn：互动强度和社交隶属公式

- evidence_pointer：Section 3.3.1, Fig.5

### 35. 3.3.1 interaction

- order：35

- section：System framework 3.3.1

- locator：3.3.1 interaction

- move_code：DESIGN_FEATURE

- paraphrase_cn：用Tag、Comment、Like、MutualFriend四类行为计算互动强度，并用Jaccard相似度标准化。

- rhetorical_function_cn：将强关系概念操作化为可计算指标。

- depends_on_cn：社会隶属例子

- sets_up_cn：社交隶属兴趣公式中的互动权重

- evidence_pointer：Section 3.3.1, Equation (10)

### 36. 3.3.1 affiliation interest

- order：36

- section：System framework 3.3.1

- locator：3.3.1 affiliation interest

- move_code：DESIGN_FEATURE

- paraphrase_cn：社交隶属兴趣=朋友工作数量×互动强度加权的归一化值，与自身浏览行为加权平均。

- rhetorical_function_cn：把朋友兴趣传导过程变成可用于匹配的分数。

- depends_on_cn：互动强度

- sets_up_cn：社会影响总评分中的隶属部分

- evidence_pointer：Section 3.3.1, Equation (11)

### 37. 3.3.2 closeness

- order：37

- section：System framework 3.3.2

- locator：3.3.2 closeness

- move_code：MECHANISM

- paraphrase_cn：贡献者与请求者之间存在越短/越强的社会路径，就越可能接受任务邀请。

- rhetorical_function_cn：提出社会亲近度影响意愿的机制。

- depends_on_cn：社会影响理论

- sets_up_cn：路径乘积计算

- evidence_pointer：Section 3.3.2

### 38. 3.3.2 equation

- order：38

- section：System framework 3.3.2

- locator：3.3.2 equation

- move_code：DESIGN_FEATURE

- paraphrase_cn：社会亲近度取所有路径中逐段互动强度乘积的最大值，社会影响由社会隶属和社会亲近度线性组合。

- rhetorical_function_cn：把社会亲近度操作化为路径上的最强连接；把两维度合并为一个社会影响力。

- depends_on_cn：社交路径和互动强度

- sets_up_cn：推荐模块中的SocialInfluence项

- evidence_pointer：Section 3.3.2, Equations (12)-(15)

### 39. 3.4.1 task value

- order：39

- section：System framework 3.4.1

- locator：3.4.1 task value

- move_code：DESIGN_FEATURE

- paraphrase_cn：用任务价值和执行时间构成的TaskValue吸引财务动机的贡献者，贡献者偏好由兴趣、能力、任务价值按动机加权。

- rhetorical_function_cn：将动机理论引入最终匹配分数。

- depends_on_cn：动机类型

- sets_up_cn：适合度公式中的偏好项

- evidence_pointer：Section 3.4.1, Equations (16)-(17)

### 40. 3.4.2 AHP

- order：40

- section：System framework 3.4.2

- locator：3.4.2 AHP

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：采用AHP将请求者对偏好、历史、社会影响的成对比较转化为三准则权重，避免简单等权。

- rhetorical_function_cn：说明为什么需要AHP而非固定权重。

- depends_on_cn：多准则决策需求

- sets_up_cn：Suitability加权聚合

- evidence_pointer：Section 3.4.2, Equations (18)-(21)

### 41. 3.4.2 suitability

- order：41

- section：System framework 3.4.2

- locator：3.4.2 suitability

- move_code：DESIGN_FEATURE

- paraphrase_cn：适合度=偏好权重×偏好分+历史权重×历史分+社会影响权重×社会影响分，据此排序。

- rhetorical_function_cn：将三个模块整合为一个排序分数，生成推荐列表。

- depends_on_cn：AHP权重和三个因子

- sets_up_cn：实验中的推荐结果生成

- evidence_pointer：Section 3.4.2, Equation (22)

### 42. Section 4 intro

- order：42

- section：Experiment 4

- locator：Section 4 intro

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：实验用Facebook收集社交信息，以Amazon Mechanical Turk和Taskcn作为任务型众包平台参考。

- rhetorical_function_cn：说明数据来源和平台代表性的选择。

- depends_on_cn：系统框架的数据需求

- sets_up_cn：数据收集和任务分类

- evidence_pointer：Section 4

### 43. 4.1 Steps 1-5

- order：43

- section：Experiment 4.1

- locator：4.1 Steps 1-5

- move_code：STUDY_OVERVIEW

- paraphrase_cn：实验分五步：实现系统并招募Facebook俱乐部用户；请求者上传任务；系统分类并AHP计算适合度；生成推荐并邀请，收集反馈；请求者评估贡献是否被接受。

- rhetorical_function_cn：完整描述评价流程，说明证据如何产生。

- depends_on_cn：推荐机制流程

- sets_up_cn：数据统计和结果评价

- evidence_pointer：Section 4.1

### 44. 4.2.1

- order：44

- section：Experiment 4.2.1

- locator：4.2.1

- move_code：RESULT

- paraphrase_cn：138名参与者提供大量签到、标签、点赞、评论和粉丝页数据；用雪球抽样，样本量高于同类实地研究平均水平。

- rhetorical_function_cn：展示样本规模和社交数据丰富度，增强结果可信度。

- depends_on_cn：实验流程

- sets_up_cn：后续推荐效果的可推广性论述

- evidence_pointer：Section 4.2.1, Table 1

### 45. 4.2.3

- order：45

- section：Experiment 4.2.3

- locator：4.2.3

- move_code：RESULT

- paraphrase_cn：AHP权重显示专业任务中贡献者偏好更重要(0.363)，非专业任务中社会影响更重要(0.372)，与假设一致。

- rhetorical_function_cn：在结果前先给出权重差异，作为社会影响机制的先验证据。

- depends_on_cn：AHP问卷数据

- sets_up_cn：解释后文为什么非专业任务满意度更高

- evidence_pointer：Section 4.2.3, Table 3

### 46. 4.2.4

- order：46

- section：Experiment 4.2.4

- locator：4.2.4

- move_code：BENCHMARK_OR_CONTRAST

- paraphrase_cn：设置随机、内容(CP+CH)、协同(CP+SI)、一般平台(CH+SI)、SCT(CP+CH+SI)五个模型，分别代表不同因子组合。

- rhetorical_function_cn：建立评价参照，使SCT的三因子整合可被对比。

- depends_on_cn：三因子机制

- sets_up_cn：所有结果小节中的模型比较

- evidence_pointer：Section 4.2.4

### 47. 5.1.1

- order：47

- section：Results 5.1.1

- locator：5.1.1

- move_code：RESULT

- paraphrase_cn：AHP加权的推荐准确率优于等权和默认权重，配对t检验显示显著差异。

- rhetorical_function_cn：先验证权重方案，说明AHP作为聚合方法有效。

- depends_on_cn：AHP问卷与准确率定义

- sets_up_cn：后续SCT模型统一使用AHP权重

- evidence_pointer：5.1.1, Fig.7, Table 4

### 48. 5.1.2

- order：48

- section：Results 5.1.2

- locator：5.1.2

- move_code：RESULT

- paraphrase_cn：SCT在贡献满意度上显著高于四种基准模型，非专业任务的满意度普遍更高。

- rhetorical_function_cn：证明请求者端效果，并解释任务类型差异。

- depends_on_cn：五模型对比和满意度定义

- sets_up_cn：转向贡献者端任务邀请评价

- evidence_pointer：5.1.2, Fig.8, Table 5

### 49. 5.2.1

- order：49

- section：Results 5.2.1

- locator：5.2.1

- move_code：RESULT

- paraphrase_cn：SCT的任务邀请适合度最高，显著优于其他模型。

- rhetorical_function_cn：从贡献者视角补充匹配质量证据。

- depends_on_cn：五模型对比

- sets_up_cn：继续检验贡献者对邀请的喜爱度

- evidence_pointer：5.2.1, Fig.9, Table 6

### 50. 5.3.2

- order：50

- section：Results 5.3.2

- locator：5.3.2

- move_code：RESULT

- paraphrase_cn：SCT的任务邀请喜爱度最高，随机模型最低，差异显著。

- rhetorical_function_cn：将匹配从“适合”延伸到“主观喜欢”。

- depends_on_cn：五模型对比

- sets_up_cn：用实际接受意愿验证态度是否转化为行为

- evidence_pointer：5.3.2, Fig.10, Table 7

### 51. 5.3.3

- order：51

- section：Results 5.3.3

- locator：5.3.3

- move_code：RESULT

- paraphrase_cn：SCT的任务邀请接受意愿最高，显著高于其他模型。

- rhetorical_function_cn：用行为指标闭合推荐匹配链条。

- depends_on_cn：五模型对比

- sets_up_cn：讨论部分总结全部实验贡献

- evidence_pointer：5.3.3, Fig.11, Table 8

### 52. 6 intro

- order：52

- section：Discussion 6

- locator：6 intro

- move_code：CONTRIBUTION

- paraphrase_cn：总结所提机制基于偏好、历史和社会影响三方面，用AHP加权，实验结果证明优于基准。

- rhetorical_function_cn：重新包装前文结果，使其成为论文中心主张。

- depends_on_cn：全部实验结果

- sets_up_cn：展开具体贡献条目

- evidence_pointer：Section 6

### 53. 6.1

- order：53

- section：Discussion 6.1

- locator：6.1

- move_code：CONTRIBUTION

- paraphrase_cn：从设计、方法、实证和实践四角度说明贡献：设计有效系统、提出少有的社交众包推荐、整合用户行为数据证明多指标提升、降低搜索成本并吸引更多合作。

- rhetorical_function_cn：把结果转化为可引用的贡献陈述。

- depends_on_cn：实验结果

- sets_up_cn：随后列出限制，保护主张不过度泛化

- evidence_pointer：Section 6.1

### 54. 6.2

- order：54

- section：Discussion 6.2

- locator：6.2

- move_code：BOUNDARY_CONDITION

- paraphrase_cn：限制包括只使用Facebook、新用户社交活动少时性能下降、隐私导致能力信息缺失、冷启动问题、实验样本小于真实众包群体。

- rhetorical_function_cn：划定结论适用边界，避免被批评为无条件有效。

- depends_on_cn：实验环境与数据

- sets_up_cn：未来研究方向的直接来源

- evidence_pointer：Section 6.2

### 55. 6.3

- order：55

- section：Discussion 6.3

- locator：6.3

- move_code：LIMITATION_AND_FUTURE

- paraphrase_cn：未来可加入更多社交互动、Reactions情感分析、多平台数据整合、移动众包以及情境/位置因素。

- rhetorical_function_cn：提出扩展方向，暗示当前机制可继续演进。

- depends_on_cn：当前限制

- sets_up_cn：论文结尾，无后续

- evidence_pointer：Section 6.3

## 写作技术

- gap_construction_cn：首先用“平台分散、任务隐藏、搜索成本高、效率和结果质量受损”制造现实痛点，接着断言内容过滤和协同过滤因众包特性不能解决，最后将社交网络信息包装成未被充分利用的资源，从而形成“现有推荐系统不足—需要社交机制—需要偏好/历史/社会影响三因子”的递进缺口。

- signposting_cn：摘要在开头给出目标，引言末尾给出章节路线图，系统框架开篇用四模块列表预告结构，实验部分用“五步”清晰安排流程，结果部分用“两个部分”预告请求者侧与贡献者侧评价。

- transition_logic_cn：从引言的问题到相关文献用“因此/然而”连接；从文献到系统框架用“为解决问题，我们提出”；从系统到实验用“为了验证所提机制，本节描述实验过程”；从请求者结果到贡献者结果用“此外/同样地”转向。各模块之间也采用“下个模块”的显式转场。

- claim_evidence_rhythm_cn：每个结果小节都遵循“指标定义—公式—图示—基准比较—配对t检验”节奏。先给计算公式和算法，再放柱状图展示均值，然后用t检验表格证明显著性，最后用一句解释性推理说明为什么该结果在理论上合理。

- benchmark_narrative_cn：四个基准不是随意选取，而是分别对应缺少社会影响、缺少历史、缺少偏好的两因子组合，从而在叙事上把SCT的“三因子全包含”塑造成性能优势的必要条件；权重方案对比则说明AHP并非可有可无的聚合工具。

- theory_return_cn：讨论部分把高贡献者意愿归因于社会隶属与社会亲近度，用AHP权重中非专业任务社会影响更高来解释结果；同时还引用“过去表现预测未来表现”和“朋友兴趣传导”来使偏好/历史因子的设计显得有理论支持。

- contribution_positioning_cn：不把贡献局限在算法性能上，而是分成“设计/方法/实证/实践”四类，分别对应制品、社交推荐稀缺性、数据验证和平台价值，使贡献具有多层面可引用性。

- novelty_protection_cn：反复强调“少有人提出任务型众包社交推荐机制”，并用五个不同评价指标（准确率、满意度、适合度、喜爱度、意愿）展示优势，避免贡献被归结为单一benchmark上的偶然性能。

## 可复用研究与写作程序

### structure_steps

#### 1. 1

- step：1

- writing_job_cn：在引言中建立众包趋势、参与者和搜索成本痛点

- research_job_cn：识别现存平台/推荐系统的匹配失败证据

- required_evidence_cn：至少需要任务隐藏、搜索成本、贡献者偏好不可得等可引用现象

- transition_to_next_cn：用“现有推荐不能解决”过渡到“需要社交机制”

#### 2. 2

- step：2

- writing_job_cn：在文献部分界定任务型众包、推荐系统和社交影响

- research_job_cn：找出众包偏好/历史/社会关系作为推荐因子的理论依据

- required_evidence_cn：文献中关于动机、绩效预测、社交影响和推荐局限的支撑

- transition_to_next_cn：从理论/知识缺口转到系统设计需求

#### 3. 3

- step：3

- writing_job_cn：构建系统框架，把需求翻译成模块和公式

- research_job_cn：设计类型树、偏好/历史分析、社会影响分析、最终推荐聚合方法

- required_evidence_cn：每个模块必须有可计算的操作化公式和数据来源说明

- transition_to_next_cn：用“为验证机制，进行实验”进入评价

#### 4. 4

- step：4

- writing_job_cn：描述实验环境和数据收集，定义基准模型

- research_job_cn：实现系统、招募样本、收集社交数据、确定任务、计算权重、建立对照

- required_evidence_cn：样本量、数据量、任务分类、AHP权重、四类基准定义

- transition_to_next_cn：用排序/满意度/接受意愿等结果指标呈现验证

#### 5. 5

- step：5

- writing_job_cn：报告多个结果指标，并配对t检验证明优势

- research_job_cn：从请求者侧和贡献者侧分别采集行为或问卷数据

- required_evidence_cn：每项指标都有公式、图和统计检验表

- transition_to_next_cn：用“结果证明有效”转入讨论

#### 6. 6

- step：6

- writing_job_cn：在讨论中重述缺口、总结贡献、列出边界和未来

- research_job_cn：把结果抽象为设计知识，并诚实说明限制

- required_evidence_cn：至少要有边界条件和未来研究清单支撑主张的可信度

- transition_to_next_cn：全文结束

### most_transferable_moves_cn

1. 把现实痛点（搜索成本高）拆解为可计算的匹配问题

2. 用基准模型代表不同因子组合进行消融式叙事

3. 同一批用户/请求者上做配对比较，并用t检验增强统计说服力

4. 从请求者侧和贡献者侧双向评价，使推荐机制不只有单边准确率

5. 讨论部分按设计/方法/实证/实践四类贡献组织

### resource_intensive_or_nonstandard_parts_cn

1. 基于Facebook授权收集真实社交关系数据需要平台权限和用户同意

2. 138用户、大量签到/点赞/标签等数据需要长时间招募和清洗

3. 真实请求者创建任务、邀请贡献者、等待贡献、验收结果的闭环实验周期较长

4. 使用AHP问卷获取每个请求者的三准则权重并非标准推荐系统能直接获得

5. 四类基准模型都需要在同一个系统上重新生成推荐列表并采集反馈

### what_not_to_copy_superficially_cn

1. 不要只写“偏好+历史+社会影响”而不给出可复现的计算公式和数据来源

2. 不要把整体性能优势直接说成社会影响机制成立，需要中介或过程证据

3. 不要在样本量较小且未平台部署的情况下宣称长期关系和平台利润

4. 不要复制“AHP权重合理”的断言而没有实际请求者问卷数据

5. 不要在公式存在乱码/模糊的情况下假装方法完全可复现

- single_best_description_of_the_routine_cn：先构造一个搜索匹配失败的实际痛点，再把偏好、历史、社会关系翻译成可计算因子，构建推荐机制，用现场小规模实验与四类基准做全面比较，用t检验证明整体优势，最后把结果包装为多角度贡献。

## 分析边界

本文所用源文件为Journal Pre-proof，PDF中部分公式符号和编号存在OCR乱码，无法逐字精确重建所有公式；图表仅保留图片引用，无法从OCR中抽取具体数值；实际页码未知，因此位置证据使用章节/段落/图/表/公式编号标识。
