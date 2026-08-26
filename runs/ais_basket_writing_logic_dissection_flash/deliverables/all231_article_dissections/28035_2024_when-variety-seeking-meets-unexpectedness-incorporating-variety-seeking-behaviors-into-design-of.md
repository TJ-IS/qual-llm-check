# When Variety Seeking Meets Unexpectedness: Incorporating Variety-Seeking Behaviors into Design of Unexpected Recommender Systems

- 作者：Pan Li; Alexander Tuzhilin
- 年份 / 期刊：2024 / Information Systems Research
- DOI：10.1287/isre.2021.0053
- 源文件：28035_2024_when-variety-seeking-meets-unexpectedness-incorporating-variety-seeking-behaviors-into-design-of.md
- 论文主类型：multi_method_or_multi_study_program
- 主导写作弧线：problem_theory_design_test_return
- 置信度：0.85

## 文章级论证概况

- 核心问题：如何把消费者追求多样性的行为（variety seeking）转化为可计算的度量，并用它来个性化地调节推荐系统中的unexpectedness，从而同时提升消费者满意度和平台业务指标？

- 制品与设计：提出一个variety-seeking测量框架（距离函数+时间衰减+平稳性汇总），并在推荐端提出Utility = Relevance + f(Variety_Seeking, Unexpectedness)的推荐框架；最优实现是DIN+Latent+Multiply，即用DIN算相关性、用潜在表示算unexpectedness、用乘法聚合variety seeking。

- 客观结果：问卷中Euclidean+Exponential+Mean与自报variety相关系数显著优于baseline；三个离线数据集上所有框架变体AUC/HR@10显著提升，平均约3.81%；线上A/B测试CTR+2.29%、视频观看完成率+4.56%、平均时长+39.2秒，公司最终部署该模型。

- 核心贡献：把营销领域的variety seeking引入推荐系统，提出测量与推荐两个框架，并用问卷、离线、线上多阶段证据证明其有效性和经济影响。

- 整篇论证链：作者先指出variety seeking是重要消费者行为但缺乏适合现代推荐系统的测量方法；然后按距离、时间衰减和稳恒性构建测量框架，用问卷验证“Euclidean+Exponential+Mean”能匹配用户自报多样性；接着论证variety seeking与unexpectedness互补，把测量结果代入效用函数自动确定unexpectedness权重；通过三个数据集离线实验证明显著优于多种baseline，再用一个大型视频平台A/B实验证明真实业务提升，并用异质性和稳健性检验支撑机制解释，最后以部署作为最终贡献锚点。

## 类型与写作弧线判定

- 论文主类型判定：文章没有局限在单一研究设计，而是依次完成框架构建、用户问卷验证、三个离线数据集benchmark、大规模线上对照实验、异质性与稳健性分析等多阶段证据闭环，属于多种方法或多个Study累积完成贡献。

- 主导写作弧线判定：文章从营销学variety seeking理论与数据挖掘unexpectedness概念切入，设计两个框架，然后通过问卷、离线实验和线上实验检验，并在结论中回到理论含义与部署，符合问题—理论—设计—检验—回到理论的写作弧线。

## 研究开展程序

- study_or_phase_count：5

- 研究阶段总序列：测量理论形式化 → 测量构念效度验证 → 推荐设计+离线效果验证 → 线上真实业务影响验证 → 异质性/长期性/稳健性分析。前一阶段解决测量是否可计算和可验证，后一阶段在本阶段留下的不确定点上继续推进。

### studies_or_phases

#### 1. 多样化测量框架的提出与平稳性检验

- order：1

- name_cn：多样化测量框架的提出与平稳性检验

- question_cn：如何从消费记录中度量消费者的variety-seeking水平？

- inputs_and_setting_cn：Yelp/MovieLens/Alibaba离线数据、线上视频平台数据；Company A用户行为的抽样数据。

- designed_or_compared_object_cn：由距离函数、时间衰减、平稳性三组件构成的Product_Variety和Variety_Seeking定义；不同组件组合。

- baseline_control_or_counterfactual_cn：无时间衰减变体；ADF单位根零假设；早期与后期观看行为的比较。

##### objective_metrics

1. ADF检验统计量

2. 产品多样性水平的均值和方差

- analysis_method_cn：描述性时序图；扩展Dickey–Fuller检验；组件消融对比。

- main_result_cn：有衰减的变体都拒绝单位根；无衰减不平稳；Euclidean+Exponential+Mean可作为后期采用。

- argumentative_role_cn：把marketing中的variety seeking概念转成可计算、可验证的推荐系统度量，为后续推荐框架提供输入。

- remaining_uncertainty_cn：尚未证明该度量能改善推荐性能和业务指标。

- link_to_next_phase_cn：需要用户问卷验证度量的外部效度，再进入推荐框架。

##### evidence_pointers

1. Table 1

2. Figure 2

#### 2. 用户问卷验证

- order：2

- name_cn：用户问卷验证

- question_cn：计算得到的variety-seeking度量是否与消费者自我报告一致？

- inputs_and_setting_cn：Alibaba 2401名消费者三周问卷；商品推荐反馈、CEI-II好奇心问卷。

- designed_or_compared_object_cn：计算Product_Variety和Variety_Seeking的多种变体。

- baseline_control_or_counterfactual_cn：APF和PAS两个营销baseline；去除时间衰减的变体。

##### objective_metrics

1. Pearson相关系数

- analysis_method_cn：相关分析；与baseline比较；显著性检验。

- main_result_cn：最优Euclidean+Exponential+Mean的相关显著最高，去除时间衰减后下降。

- argumentative_role_cn：建立测量构念效度，证明框架不只在理论上合理，也能对应消费者主观体验。

- remaining_uncertainty_cn：度量好不等于推荐好；需要在推荐任务中验证。

- link_to_next_phase_cn：进入推荐框架整合和离线实验。

##### evidence_pointers

1. Table 4

2. Section 3.5

3. online appendix part I/II

#### 3. 离线推荐实验

- order：3

- name_cn：离线推荐实验

- question_cn：将variety-seeking纳入unexpected推荐是否能提升推荐性能？

- inputs_and_setting_cn：Yelp, MovieLens, Alibaba三个工业数据集。

- designed_or_compared_object_cn：12个模型 = Relevance(NCF/DIN) × Unexpectedness(Feature/Latent) × Aggregation(Multiply/Exponential/Power)。

- baseline_control_or_counterfactual_cn：8个baseline：DIN, DeepFM, PURS, HOM-LIN, Re-Ranking, DPP, LinUCB, COFIBA；以及无variety seeking的固定α unexperted模型。

##### objective_metrics

1. AUC

2. Hit Rate@10

- analysis_method_cn：时间分层五折交叉验证；贝叶斯超参优化；显著性检验。

- main_result_cn：所有framework模型显著优于baselines；平均AUC和HR@10提升3.81%；最佳DIN+Latent+Multiply。

- argumentative_role_cn：证明框架的泛化性和相对baseline的有效性，排除‘只在单一场景有效’的顾虑。

- remaining_uncertainty_cn：离线指标不能证明真实业务价值。

- link_to_next_phase_cn：线上A/B检验。

##### evidence_pointers

1. Table 7

2. Figure 3

3. online appendix part VI

#### 4. 线上受控实验平均处理效应

- order：4

- name_cn：线上受控实验平均处理效应

- question_cn：在真实平台用最佳模型替代生产系统是否提升业务指标？

- inputs_and_setting_cn：Company A视频平台，2020年9月，37,965,781条记录，444,765用户。

- designed_or_compared_object_cn：用户被随机分到treatment（DIN+Latent+Multiply）和control（生产系统）。

- baseline_control_or_counterfactual_cn：最新生产系统，即固定α的unexpectedness推荐模型。

##### objective_metrics

1. CTR

2. Video View

3. Time Spent

- analysis_method_cn：OLS回归Equation (4)；用户/视频特征和时间固定效应；稳健标准误。

- main_result_cn：CTR +2.29%, VV +4.56%, TS +39.219秒，均p<0.01。

- argumentative_role_cn：提供真实业务影响证据并导致部署。

- remaining_uncertainty_cn：平均效应可能掩盖不同消费者的差异；需要异质性分析。

- link_to_next_phase_cn：异质性、平行趋势和稳健性分析。

##### evidence_pointers

1. Table 9

2. Section 5.2

3. Figure 4

#### 5. 异质性、平行趋势与稳健性分析

- order：5

- name_cn：异质性、平行趋势与稳健性分析

- question_cn：提升是否对所有消费者一致？长期是否持续？结论是否稳健？

- inputs_and_setting_cn：同一线上实验数据。

- designed_or_compared_object_cn：按variety-seeking水平分20 bin；Treatment×Variety_Seeking交互；不同固定效应/模型设定/样本排除。

- baseline_control_or_counterfactual_cn：无交互效应；预处理期对照组/处理组差异。

##### objective_metrics

1. CTR

2. VV

3. TS

4. ATE系数

- analysis_method_cn：交互项回归；平行趋势图；logit/probit；排除样本；附录DID。

- main_result_cn：所有消费者正收益；高/低variety seeker获益更大；预处理无差异且长期显著；稳健。

- argumentative_role_cn：把平均效应转化为机制和边界知识，说明是heterogeneous desire驱动，而非简单的新奇效应。

- remaining_uncertainty_cn：机制仍是推断并非直接心理实验验证；边界限于视频平台。

- link_to_next_phase_cn：结论部分将异质性解释为个性化机制并指出未来方向。

##### evidence_pointers

1. Figure 5

2. Figure 6

3. online appendix part V/VII/VIII–X

## 各部分修辞架构

### abstract_moves

1. CONTEXT

2. GAP

3. RQ_OR_OBJECTIVE

4. DESIGN_FEATURE

5. STUDY_OVERVIEW

6. RESULT

7. CONTRIBUTION

### introduction_moves

1. CONTEXT

2. PRACTICAL_STAKES

3. GAP

4. LIMITATION

5. RQ_OR_OBJECTIVE

6. DESIGN_FEATURE

7. THEORY_INTRO

8. MECHANISM

9. HYPOTHESIS_OR_PROPOSITION

10. STUDY_OVERVIEW

11. CONTRIBUTION

### theory_and_knowledge_moves

1. PRIOR_KNOWLEDGE

2. THEORY_INTRO

3. THEORY_PROPOSITION

4. MECHANISM

5. LIMITATION

6. GAP

### artifact_design_moves

1. DESIGN_FEATURE

2. REQUIREMENT

3. METHOD_JUSTIFICATION

4. BENCHMARK_OR_CONTRAST

### evaluation_moves

1. STUDY_OVERVIEW

2. METHOD_JUSTIFICATION

3. BENCHMARK_OR_CONTRAST

4. RESULT

5. ROBUSTNESS_OR_BOUNDARY_TEST

### discussion_and_contribution_moves

1. RESULT

2. MECHANISM

3. CONTRIBUTION

4. PRACTICAL_STAKES

5. BOUNDARY_CONDITION

6. LIMITATION_AND_FUTURE

## 理论/知识到设计的翻译

### 知识/理论基础

1. 营销学variety seeking理论（McAlister & Pessemier；Hoyer & Ridgway；Van Trijp；Kim et al.）

2. 数据挖掘unexpectedness文献（Silberschatz & Tuzhilin；Adamopoulos & Tuzhilin；Li & Tuzhilin）

3. 深度学习推荐系统的表示学习实践（Covington et al.; He et al.; Zhang et al.; Zhou et al.）

4. 记忆与时间衰减的消费者行为研究（Helsen & Schmittlein；Braun & Moe）

- 理论—设计耦合：partial

- 耦合判定理由：测量框架的三个维度直接从营销学variety seeking理论出发生成，属于理论到设计的直接翻译；但具体深度学习嵌入、DIN、乘法聚合函数等关键技术选择来自计算机科学工程实践，且最终模型是从多个变体中挑出的最佳结果，因此整体是部分耦合。

- 理论到设计翻译链：营销理论中的探索动机与刺激需求 → 消费者比较当前与历史产品、记忆随时间衰减、个体差异长期稳定 → 定义为距离函数、时间衰减函数、平稳性汇总 → 用自编码器潜在空间计算产品距离、指数衰减、算术平均 → 与unexpectedness结合，将variety seeking作为效用函数中unexpectedness的个性化权重 → 在推荐模型中用DIN相关性+潜在unexpectedness+乘法函数实现。

### mapping_table

#### 1. 1

- theory_or_knowledge_claim_cn：消费者追求多样性的动机是探索新内容、避免重复消费。

- mechanism_cn：消费者会计算新产品与过去消费产品之间的差异，差异影响探索行为；记忆随时间衰退。

- design_requirement_cn：需要度量每个产品相对历史消费的差异，并随时间衰减。

- artifact_choice_cn：产品多样性函数 Product_Variety = Σ μ(t-t_k)*ρ(i_k,j)。

- evaluated_contrast_cn：不同距离函数（binary/feature/Euclidean等）× 不同时间衰减（exponential/hyperbolic/no decay）的变体与问卷自报多样性水平相关。

- objective_result_cn：Euclidean距离+Exponential衰减+Mean的相关最高 (0.775/0.618)，优于APF/PAS。

##### evidence_pointers

1. Section 3.1–3.5

2. Table 4

#### 2. 2

- theory_or_knowledge_claim_cn：variety seeking是长期稳定的个体特性。

- mechanism_cn：个体差异应保持稳定，可求均值。

- design_requirement_cn：用算术平均聚合产品多样性得到 Variety_Seeking(i)。

- artifact_choice_cn：Equation (2): Variety_Seeking(i) = (1/n) Σ Product_Variety。

- evaluated_contrast_cn：ADF test with different components; no decay fails stationarity。

- objective_result_cn：ADF统计量在有衰减时显著拒绝单位根，无衰减时不平稳。

##### evidence_pointers

1. Section 3.3

2. Table 1

#### 3. 3

- theory_or_knowledge_claim_cn：variety seeking和unexpectedness互补；消费者对刺激的需求可以通过提供多变/意外来满足。

- mechanism_cn：高variety seeker对意外推荐有更高偏好，低variety seeker更偏好熟悉。

- design_requirement_cn：utility中unexpectedness项的权重应由variety-seeking水平自动决定，而不是全局固定α。

- artifact_choice_cn：Utility = Relevance + f(Variety_Seeking(i), Unexpectedness(i,j))；aggregation functions multiply/exponential/power。

- evaluated_contrast_cn：与现有unexpectedness推荐模型（α固定）、纯relevance、diversity、bandit baselines比较。

- objective_result_cn：Table 7：proposed models显著优于baselines；最佳DIN+Latent+Multiply。

##### evidence_pointers

1. Section 4

2. Table 7

#### 4. 4

- theory_or_knowledge_claim_cn：真实平台业务指标与点击、观看和时长相关，个性化推荐应提升这些指标。

- mechanism_cn：为variety seeker提供更多意外推荐、为consistency seeker提供更熟悉推荐，减少不匹配。

- design_requirement_cn：将最好模型部署到真实平台并做A/B检验。

- artifact_choice_cn：Company A上比较treatment DIN+Latent+Multiply vs 生产系统。

- evaluated_contrast_cn：CTR, VV, time spent；heterogeneous effect。

- objective_result_cn：CTR +2.29%, VV +4.56%, time +39.219s；U-shape heterogeneity；部署。

##### evidence_pointers

1. Section 5

2. Table 9

3. Figure 5

## 评价逻辑

### evaluation_modes

1. User questionnaire correlation validation

2. ADF stationarity test

3. Off-line click-through prediction benchmark on three datasets

4. Large-scale online controlled experiment (A/B test on Company A)

5. Heterogeneous treatment effect analysis

6. Parallel trend analysis

7. Robustness checks with alternative models/specifications/samples

- why_these_evaluations_cn：先验证测量构念是否有效，再验证推荐设计是否在可复现的离线benchmark上优于基线，最后用真实平台随机实验证明业务价值；每个环节都回应上一环节留下的不确定性问题。

- benchmark_and_contrast_chain_cn：测量阶段用APF/PAS和“无时间衰减”变体作为对照；推荐阶段用8个baselines（relevance、unexpectedness、diversity、bandit）作为对照；线上阶段用最新生产系统作为对照；异质性阶段用低/中/高variety seeker子组作为对照；长期性用预处理期和posttreatment期作对照。

### claim_evidence_ledger

#### 1. 1

- claim：提出的variety-seeking度量与消费者自报variety水平相关

- evidence：Alibaba问卷调查Table 4相关显著，且优于APF/PAS

- support_quality：强，直接测量构念效度

#### 2. 2

- claim：Euclidean+Exponential+Mean measure captures variety seeking best

- evidence：问卷相关最高且ADF平稳

- support_quality：强，但局限于Alibaba问卷和三个离线数据集的背景

#### 3. 3

- claim：所有推荐框架变体都优于已有推荐模型

- evidence：Table 7三个数据集上的AUC和HR@10

- support_quality：强，但离线指标只能代理真实用户反应

#### 4. 4

- claim：variety-seeking水平应作为unexpectedness的个性化权重

- evidence：离线模型显著优于固定α模型；线上best model显著优于生产系统

- support_quality：较强，但机制解释是推断而非直接中介检验

#### 5. 5

- claim：线上模型带来真实经济影响

- evidence：Table 9的CTR/VV/TS显著提升，公司部署

- support_quality：强，但有赖于公司合作和单一视频平台

#### 6. 6

- claim：模型对高和低variety seeker获益最大

- evidence：Figure 5的Treatment×Variety_Seeking交互

- support_quality：中强，U型效应是统计模式，未直接测量消费者满意

- internal_validity_strategy_cn：线上实验用二进制哈希随机分流；检查倾向值分布平衡；用户不知分组；控制用户和视频特征及时间固定效应；使用平行趋势检验；多个稳健性设定（logit/probit、排除自有内容、排除新地区等）。

- external_validity_strategy_cn：测量阶段使用Alibaba真实用户问卷；推荐阶段使用Yelp、MovieLens、Alibaba三个不同行业数据集；线上实验使用大型视频平台；展示不同业务场景、稀疏度和variety seeker分布下的可重复结果。

- what_is_not_actually_tested_cn：没有直接检验‘更多意外推荐导致variety seeker满意度提高’的中介机制；消费者满意度只由点击、观看、时长这些行为指标代理；自我报告测量只在Alibaba食品杂货平台完成，而非视频平台；stationarity假设未在更长时间跨度或非娱乐产品上验证；没有对模型中各组件做严格的逐一因果消融，baseline比较是整体模型间的比较。

## 贡献闭环

- technical_claim_cn：提出的variety-seeking测量框架在问卷和ADF检验上优于现有测量方法；结合DIN+Latent+Multiply的推荐模型在离线AUC/HR@10和线上CTR/VV/TS上显著优于baselines。

- artifact_claim_cn：Euclidean+Exponential+Mean是最优测量变体；DIN+Latent+Multiply是最优推荐模型，且已被公司部署。

- mechanism_claim_cn：variety seeking与unexpectedness互补，variety-seeking水平决定unexpectedness权重，从而为variety seeker提供更多意外推荐、为consistency seeker提供更熟悉推荐。

- boundary_claim_cn：该结论主要适用于高消费率的水平品种寻求（horizontal variety），尤其是娱乐/视频类内容；垂直差异化variety seeking和其他平台尚未验证。

- reusable_design_knowledge_cn：测量variety seeking应包含三个组件：距离函数、时间衰减函数、满足平稳性的汇总统计；推荐设计应让unexpectedness的权重随variety-seeking水平个性化，而非使用全局固定α。

- theoretical_contribution_cn：将营销学的variety seeking概念操作化并引入推荐系统，补充了unexpectedness推荐研究忽略的消费者异质性维度；用大规模数据验证了时间衰减和stationarity的重要性，并用线上实验将行为理论与技术设计连接起来。

- how_discussion_closes_intro_gap_cn：结论明确指出variety seeking在推荐中被忽略，本文通过测量与推荐两个框架以及问卷、离线、线上实验填补这一缺口，并以部署结果强化贡献的现实意义。

- overclaim_or_unsupported_leaps_cn：“潜在额外3000万美元收入”基于2.29% CTR提升与平台收入的直接比例假设，未做严格归因；heterogeneous effect的U型解释是事后机制解释，没有直接测量心理过程；‘所有消费者都受益’来自总体正效应，个别细分可能不明显；单一公司部署不能直接外推到整个视频推荐行业。

## 句级写作动作图谱

### 1. Abstract P1

- order：1

- section：Abstract

- locator：Abstract P1

- move_code：CONTEXT

- paraphrase_cn：介绍variety seeker是什么：容易厌倦已购产品、偏好新鲜内容。

- rhetorical_function_cn：开篇界定核心用户群体。

- depends_on_cn：无。

- sets_up_cn：为后续说明该群体未被推荐系统研究做好准备。

- evidence_pointer：Abstract

### 2. Abstract P2

- order：2

- section：Abstract

- locator：Abstract P2

- move_code：GAP

- paraphrase_cn：尽管这一行为普遍，但由于现有测量方法的局限，在推荐应用中被很少研究。

- rhetorical_function_cn：在摘要中直接点出研究缺口。

- depends_on_cn：依赖前句对variety seeker重要性的设定。

- sets_up_cn：引出本文要填的缺口。

- evidence_pointer：Abstract

### 3. Abstract P3

- order：3

- section：Abstract

- locator：Abstract P3

- move_code：RQ_OR_OBJECTIVE

- paraphrase_cn：为填补缺口，提出基于消费记录的variety-seeking框架。

- rhetorical_function_cn：声明研究目标。

- depends_on_cn：需要上一句缺口。

- sets_up_cn：说明本文的测量贡献。

- evidence_pointer：Abstract

### 4. Abstract P4

- order：4

- section：Abstract

- locator：Abstract P4

- move_code：STUDY_OVERVIEW

- paraphrase_cn：通过阿里巴巴用户问卷验证测量与消费者自报variety seeking一致。

- rhetorical_function_cn：预告第一个验证证据。

- depends_on_cn：measurement framework存在后才能被验证。

- sets_up_cn：为推荐框架的经济效果证据铺垫。

- evidence_pointer：Abstract

### 5. Abstract P5

- order：5

- section：Abstract

- locator：Abstract P5

- move_code：DESIGN_FEATURE

- paraphrase_cn：提出把识别出的variety seeking水平与unexpected recommendation结合，向variety seeker提供更多意外推荐。

- rhetorical_function_cn：说明核心设计思想。

- depends_on_cn：基于variety seeking测量框架。

- sets_up_cn：引出离线与线上实验。

- evidence_pointer：Abstract

### 6. Abstract P5

- order：6

- section：Abstract

- locator：Abstract P5

- move_code：RESULT

- paraphrase_cn：离线实验覆盖三类推荐场景，线上受控实验显示业务指标显著提升。

- rhetorical_function_cn：给出主要证据和结果。

- depends_on_cn：前句框架存在。

- sets_up_cn：为贡献和部署声明作准备。

- evidence_pointer：Abstract

### 7. Abstract P6

- order：7

- section：Abstract

- locator：Abstract P6

- move_code：CONTRIBUTION

- paraphrase_cn：最佳模型已被公司部署到整个视频平台。

- rhetorical_function_cn：用部署作为最终贡献锚点。

- depends_on_cn：前一句线上实验结果。

- sets_up_cn：强调现实影响。

- evidence_pointer：Abstract

### 8. Introduction P1 S1

- order：8

- section：Introduction

- locator：Introduction P1 S1

- move_code：CONTEXT

- paraphrase_cn：variety seeking描述消费者厌倦既有产品后探索新产品的动机。

- rhetorical_function_cn：给出一般性定义和例子。

- depends_on_cn：无。

- sets_up_cn：构建消费者行为的重要现实。

- evidence_pointer：Introduction P1

### 9. Introduction P1 最后一句

- order：9

- section：Introduction

- locator：Introduction P1 最后一句

- move_code：PRACTICAL_STAKES

- paraphrase_cn：variety seeker增加消费量、对促销更开放，是营销中的重要细分。

- rhetorical_function_cn：说明忽略variety seeking的现实代价。

- depends_on_cn：variety seeking定义。

- sets_up_cn：使缺口具有商业重要性。

- evidence_pointer：Introduction P1

### 10. Introduction P2 第一句

- order：10

- section：Introduction

- locator：Introduction P2 第一句

- move_code：GAP

- paraphrase_cn：variety seeking在营销中被广泛研究，但在推荐系统中明显不足。

- rhetorical_function_cn：明确领域间的不平衡。

- depends_on_cn：前段强调variety seeking重要性。

- sets_up_cn：随后列举三个具体限制。

- evidence_pointer：Introduction P2

### 11. Introduction P2 限制一

- order：11

- section：Introduction

- locator：Introduction P2 限制一

- move_code：LIMITATION

- paraphrase_cn：现有测量只在品类或品牌层运作，不能在现代推荐的细粒度产品水平和潜在表示空间工作。

- rhetorical_function_cn：指出技术可扩展性问题。

- depends_on_cn：推荐系统使用嵌入表示的背景。

- sets_up_cn：本文选择潜在空间距离函数。

- evidence_pointer：Introduction P2

### 12. Introduction P2 限制二

- order：12

- section：Introduction

- locator：Introduction P2 限制二

- move_code：LIMITATION

- paraphrase_cn：现有variety seeking模型没有考虑购买之间的dwell time。

- rhetorical_function_cn：指出时间维度缺失。

- depends_on_cn：消费决策中的时间因子。

- sets_up_cn：本文加入时间衰减函数。

- evidence_pointer：Introduction P2

### 13. Introduction P2 限制三

- order：13

- section：Introduction

- locator：Introduction P2 限制三

- move_code：LIMITATION

- paraphrase_cn：现有营销方法很少研究variety seeking的长期稳定属性，如stationarity。

- rhetorical_function_cn：指出缺乏可泛化的行为规律。

- depends_on_cn：variety seeking作为个体特征的假设。

- sets_up_cn：本文提出stationarity假设和检验。

- evidence_pointer：Introduction P2

### 14. Introduction P3 前两句

- order：14

- section：Introduction

- locator：Introduction P3 前两句

- move_code：RQ_OR_OBJECTIVE

- paraphrase_cn：为解决这些问题，提出一个仅基于消费记录的variety-seeking框架。

- rhetorical_function_cn：从缺口转为目标。

- depends_on_cn：上一段三个限制。

- sets_up_cn：描述三个组件。

- evidence_pointer：Introduction P3

### 15. Introduction P3 组件句

- order：15

- section：Introduction

- locator：Introduction P3 组件句

- move_code：DESIGN_FEATURE

- paraphrase_cn：框架由距离函数、时间衰减函数和stationarity三部分组成。

- rhetorical_function_cn：预告测量框架的结构。

- depends_on_cn：前一句提出框架。

- sets_up_cn：第四节将详细定义每个组件。

- evidence_pointer：Introduction P3

### 16. Introduction P4 第一句

- order：16

- section：Introduction

- locator：Introduction P4 第一句

- move_code：THEORY_INTRO

- paraphrase_cn：本文把consumers的variety seeking与unexpected recommender systems连接起来。

- rhetorical_function_cn：引入第二个知识基础。

- depends_on_cn：measurement framework已经提出。

- sets_up_cn：引出unexpectedness与variety seeking互补的观点。

- evidence_pointer：Introduction P4

### 17. Introduction P4 互补句

- order：17

- section：Introduction

- locator：Introduction P4 互补句

- move_code：MECHANISM

- paraphrase_cn：unexpectedness是产品中心的概念，variety seeking是消费者中心的概念，二者互补。

- rhetorical_function_cn：建立两个构念的逻辑关系。

- depends_on_cn：先前对两个概念的文献定义。

- sets_up_cn：提出本文的核心假设。

- evidence_pointer：Introduction P4

### 18. Introduction P4 假设句

- order：18

- section：Introduction

- locator：Introduction P4 假设句

- move_code：HYPOTHESIS_OR_PROPOSITION

- paraphrase_cn：假设高variety seeker偏好更多意外产品，因此应根据其variety水平提高unexpectedness，反之亦然。

- rhetorical_function_cn：给出可检验的设计命题。

- depends_on_cn：互补性论证。

- sets_up_cn：为推荐框架的效用函数设计提供依据。

- evidence_pointer：Introduction P4

### 19. Introduction P4 提出推荐框架句

- order：19

- section：Introduction

- locator：Introduction P4 提出推荐框架句

- move_code：REQUIREMENT

- paraphrase_cn：因此提出一个按每个消费者variety水平自动调整unexpectedness程度的推荐框架。

- rhetorical_function_cn：把假设转化为设计需要。

- depends_on_cn：前一句假设。

- sets_up_cn：后续用多组模型实例化该框架。

- evidence_pointer：Introduction P4

### 20. Introduction P4 证据预览句

- order：20

- section：Introduction

- locator：Introduction P4 证据预览句

- move_code：STUDY_OVERVIEW

- paraphrase_cn：在Yelp、MovieLens和Alibaba上做离线实验，并在中国大型视频平台做线上受控实验。

- rhetorical_function_cn：预告验证方案。

- depends_on_cn：推荐框架提出。

- sets_up_cn：为摘要和结论提供结果来源。

- evidence_pointer：Introduction P4

### 21. Introduction P5 最后句

- order：21

- section：Introduction

- locator：Introduction P5 最后句

- move_code：CONTRIBUTION

- paraphrase_cn：模型已部署到平台，带来显著经济影响。

- rhetorical_function_cn：提前声明最强贡献。

- depends_on_cn：线上实验结果。

- sets_up_cn：强调现实落地。

- evidence_pointer：Introduction P5

### 22. Section 2.1 P3 第一句

- order：22

- section：Section 2.1

- locator：Section 2.1 P3 第一句

- move_code：GAP

- paraphrase_cn：variety seeking在推荐系统中仍未充分研究，导致忽略消费者的多样化欲望。

- rhetorical_function_cn：重新强调领域缺口。

- depends_on_cn：前面文献中variety seeking的多种应用。

- sets_up_cn：说明本文要识别测量维度。

- evidence_pointer：Section 2.1

### 23. Section 2.1 P3 动机句

- order：23

- section：Section 2.1

- locator：Section 2.1 P3 动机句

- move_code：THEORY_INTRO

- paraphrase_cn：方法受Hoyer和Ridgway理论模型启发，把purchase exploration视为个体特征与产品特征交互。

- rhetorical_function_cn：连接营销理论基础。

- depends_on_cn：已有variety seeking研究。

- sets_up_cn：将交互聚焦到variety seeking与unexpectedness。

- evidence_pointer：Section 2.1

### 24. Section 2.1 P3 试验扩展句

- order：24

- section：Section 2.1

- locator：Section 2.1 P3 试验扩展句

- move_code：THEORY_INTRO

- paraphrase_cn：实验室研究发现通过提供更多variety可以满足刺激需求，本文将其扩展到个性化unexpectedness推荐。

- rhetorical_function_cn：把行为实验结论转化为推荐设计动机。

- depends_on_cn：Menon & Kahn、Maimaran & Wheeler的实验室结果。

- sets_up_cn：支持向variety seeker提供更多意外推荐的思路。

- evidence_pointer：Section 2.1

### 25. Section 2.2 P1 限制句

- order：25

- section：Section 2.2

- locator：Section 2.2 P1 限制句

- move_code：LIMITATION

- paraphrase_cn：传统方法只推荐相似产品，忽略偏好分散，导致over-specialization和用户厌倦。

- rhetorical_function_cn：指出unexpectedness要解决的问题。

- depends_on_cn：推荐系统典型设计。

- sets_up_cn：引出unexpectedness概念。

- evidence_pointer：Section 2.2

### 26. Section 2.2 P1 固定α句

- order：26

- section：Section 2.2

- locator：Section 2.2 P1 固定α句

- move_code：LIMITATION

- paraphrase_cn：现有unexpectedness方法把α设为对所有消费者相同的固定值，未考虑异质性。

- rhetorical_function_cn：定位本文要克服的弱点。

- depends_on_cn：unexpectedness utility function的文献。

- sets_up_cn：提出用variety seeking自动决定α。

- evidence_pointer：Section 2.2

### 27. Section 2.2 P2 第二句

- order：27

- section：Section 2.2

- locator：Section 2.2 P2 第二句

- move_code：RQ_OR_OBJECTIVE

- paraphrase_cn：本文聚焦于把variety seeking和unexpectedness一起建模。

- rhetorical_function_cn：重申本文目标。

- depends_on_cn：前文gap和limitations。

- sets_up_cn：进入测量框架。

- evidence_pointer：Section 2.2

### 28. Section 3 P1 时间衰减句

- order：28

- section：Section 3

- locator：Section 3 P1 时间衰减句

- move_code：THEORY_PROPOSITION

- paraphrase_cn：产品间差异会随消费时间间隔增大而变得不那么重要，因为记忆会淡忘。

- rhetorical_function_cn：说明时间衰减是测量variety seeking的基本假设。

- depends_on_cn：消费者记忆文献。

- sets_up_cn：定义时间衰减函数μ。

- evidence_pointer：Section 3 P1

### 29. Section 3 P1 平稳性句

- order：29

- section：Section 3

- locator：Section 3 P1 平稳性句

- move_code：THEORY_PROPOSITION

- paraphrase_cn：variety seeking倾向长期稳定，因此过程应具有stationarity。

- rhetorical_function_cn：说明stationarity是另一基本假设。

- depends_on_cn：variety seeking作为内在特质的理论。

- sets_up_cn：定义汇总统计和ADF检验。

- evidence_pointer：Section 3 P1

### 30. Section 3 公式后总结句

- order：30

- section：Section 3

- locator：Section 3 公式后总结句

- move_code：DESIGN_FEATURE

- paraphrase_cn：框架由距离函数、时间衰减、stationarity三部分组成，具体假设决定具体测量模型。

- rhetorical_function_cn：把抽象假设转成可操作框架。

- depends_on_cn：前两条基本假设。

- sets_up_cn：分别讨论三个组件。

- evidence_pointer：Section 3 equations

### 31. Section 3.1 P3

- order：31

- section：Section 3.1

- locator：Section 3.1 P3

- move_code：DESIGN_FEATURE

- paraphrase_cn：提出在潜在空间用深度学习表示计算产品距离，比特征空间更细致。

- rhetorical_function_cn：引入具体距离函数选择。

- depends_on_cn：之前binary和feature-based距离的局限。

- sets_up_cn：说明选择autoencoder的理由。

- evidence_pointer：Section 3.1

### 32. Section 3.1 P4

- order：32

- section：Section 3.1

- locator：Section 3.1 P4

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：选用autoencoding模型因为它可扩展、高效，且在工业平台广泛部署。

- rhetorical_function_cn：为技术选型辩护。

- depends_on_cn：距离函数需要在潜在空间计算。

- sets_up_cn：将其应用到variety seeking。

- evidence_pointer：Section 3.1

### 33. Section 3.2 P1

- order：33

- section：Section 3.2

- locator：Section 3.2 P1

- move_code：DESIGN_FEATURE

- paraphrase_cn：引入时间衰减函数，指数衰减是最常用的选择。

- rhetorical_function_cn：将时间维度形式化。

- depends_on_cn：时间衰减假设。

- sets_up_cn：后续在问卷和ADF中验证其必要性。

- evidence_pointer：Section 3.2

### 34. Section 3.2 P2

- order：34

- section：Section 3.2

- locator：Section 3.2 P2

- move_code：LIMITATION

- paraphrase_cn：已有variety seeking模型没有纳入时间因素，但dwell time在推荐中很重要。

- rhetorical_function_cn：再次指出文献缺口。

- depends_on_cn：时间对消费决策重要性的文献。

- sets_up_cn：强调本文时间衰减贡献。

- evidence_pointer：Section 3.2

### 35. Section 3.3 P1

- order：35

- section：Section 3.3

- locator：Section 3.3 P1

- move_code：THEORY_PROPOSITION

- paraphrase_cn：variety seeking是消费者的内在属性，因此测量需要stationarity。

- rhetorical_function_cn：强调第三个组件。

- depends_on_cn：个体特征稳定性理论。

- sets_up_cn：引入stationarity假设和均值汇总。

- evidence_pointer：Section 3.3

### 36. Section 3.3 P2

- order：36

- section：Section 3.3

- locator：Section 3.3 P2

- move_code：HYPOTHESIS_OR_PROPOSITION

- paraphrase_cn：提出variety seeking行为在长期是平稳时间序列的假设。

- rhetorical_function_cn：把stationarity表述为可检验假设。

- depends_on_cn：stationarity作为内在属性。

- sets_up_cn：用动态图和ADF检验。

- evidence_pointer：Section 3.3

### 37. Section 3.3 P3

- order：37

- section：Section 3.3

- locator：Section 3.3 P3

- move_code：RESULT

- paraphrase_cn：视频平台数据上variety水平方差很小；前50个视频有波动，但最近10个视频已经收敛。

- rhetorical_function_cn：用描述性数据支持stationarity。

- depends_on_cn：stationarity假设。

- sets_up_cn：为ADF检验做铺垫。

- evidence_pointer：Figure 2

### 38. Section 3.3 P4

- order：38

- section：Section 3.3

- locator：Section 3.3 P4

- move_code：RESULT

- paraphrase_cn：ADF检验表明有衰减的variety measure平稳，无衰减则不平稳。

- rhetorical_function_cn：用正式检验确认stationarity。

- depends_on_cn：ADF检验设定。

- sets_up_cn：说明时间衰减是stationarity的必要组件。

- evidence_pointer：Table 1

### 39. Section 3.4 组件清单

- order：39

- section：Section 3.4

- locator：Section 3.4 组件清单

- move_code：DESIGN_FEATURE

- paraphrase_cn：距离函数可以是binary/feature/latent，时间衰减可以是指数/双曲等，stationarity需要汇总统计满足平稳性。

- rhetorical_function_cn：把框架的选择空间清晰化。

- depends_on_cn：三个组件的讨论。

- sets_up_cn：为后续模型变体和实验提供矩阵。

- evidence_pointer：Table 2

### 40. Section 3.4 最后一段

- order：40

- section：Section 3.4

- locator：Section 3.4 最后一段

- move_code：CONTRIBUTION

- paraphrase_cn：该框架从三个角度推进了现有variety seeking文献：多函数支持、时间衰减、stationarity验证。

- rhetorical_function_cn：将框架贡献定位在文献层面。

- depends_on_cn：框架内容和验证预告。

- sets_up_cn：引导进入推荐框架。

- evidence_pointer：Section 3.4

### 41. Section 3.5 P1

- order：41

- section：Section 3.5

- locator：Section 3.5 P1

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：遵循营销研究标准，用Alibaba用户问卷进行消费者问卷分析。

- rhetorical_function_cn：解释为何使用问卷验证。

- depends_on_cn：framework需要构念效度。

- sets_up_cn：描述问卷实施细节。

- evidence_pointer：Section 3.5

### 42. Section 3.5 P4 方法句

- order：42

- section：Section 3.5

- locator：Section 3.5 P4 方法句

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：将问卷报告的产品variety和variety seeking水平与Equation (1)(2)计算的指标做相关比较，并用APF/PAS做baseline。

- rhetorical_function_cn：界定验证方式。

- depends_on_cn：问卷数据。

- sets_up_cn：报告相关结果。

- evidence_pointer：Section 3.5 P4

### 43. Section 3.5 P4 结果句

- order：43

- section：Section 3.5

- locator：Section 3.5 P4 结果句

- move_code：RESULT

- paraphrase_cn：框架下各度量与消费者自报水平的相关显著高于APF和PAS。

- rhetorical_function_cn：给出度量效度的核心证据。

- depends_on_cn：问卷与计算指标。

- sets_up_cn：进一步指出最优变体。

- evidence_pointer：Table 4

### 44. Section 3.5 P4 最优模型句

- order：44

- section：Section 3.5

- locator：Section 3.5 P4 最优模型句

- move_code：RESULT

- paraphrase_cn：Euclidean距离+Exponential时间衰减+均值统计是最好的variety seeking measure。

- rhetorical_function_cn：从所有变体中选出最优。

- depends_on_cn：相关系数结果。

- sets_up_cn：后续推荐实验直接采用该measure。

- evidence_pointer：Table 4

### 45. Section 3.5 P4 去除衰减句

- order：45

- section：Section 3.5

- locator：Section 3.5 P4 去除衰减句

- move_code：ROBUSTNESS_OR_BOUNDARY_TEST

- paraphrase_cn：去掉时间衰减函数的variety measure效果显著变差，显示时间因子不可或缺。

- rhetorical_function_cn：用消融证明组件必要性。

- depends_on_cn：Table 4对比。

- sets_up_cn：支持框架三组件都有价值。

- evidence_pointer：Table 4

### 46. Section 4.1 P1 经典效用句

- order：46

- section：Section 4.1

- locator：Section 4.1 P1 经典效用句

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：经典推荐系统中效用只由相关性决定，目标是找最相关产品。

- rhetorical_function_cn：给出传统模式的基线。

- depends_on_cn：推荐系统文献。

- sets_up_cn：指出其不能满足novelty需求。

- evidence_pointer：Section 4.1

### 47. Section 4.1 P1 However句

- order：47

- section：Section 4.1

- locator：Section 4.1 P1 However句

- move_code：LIMITATION

- paraphrase_cn：只做相关性会忽略消费者对新颖内容的需求，且unexpectedness的α固定对所有消费者都一样。

- rhetorical_function_cn：指出已有unexpectedness模型的局限。

- depends_on_cn：经典效用函数。

- sets_up_cn：提出用variety seeking动态决定α。

- evidence_pointer：Section 4.1

### 48. Section 4.1 P1 互补句

- order：48

- section：Section 4.1

- locator：Section 4.1 P1 互补句

- move_code：MECHANISM

- paraphrase_cn：不同消费者variety seeking水平差异很大，因此可以用它决定unexpectedness程度，向高variety seeker提供更多意外推荐。

- rhetorical_function_cn：建立从测量到设计的行为机制。

- depends_on_cn：variety seeking测量框架。

- sets_up_cn：写出Equation (3)。

- evidence_pointer：Section 4.1

### 49. Section 4.1 Equation (3)

- order：49

- section：Section 4.1

- locator：Section 4.1 Equation (3)

- move_code：DESIGN_FEATURE

- paraphrase_cn：效用函数写作相关性加上variety seeking和unexpectedness的聚合函数。

- rhetorical_function_cn：把设计思想形式化。

- depends_on_cn：互补性论证。

- sets_up_cn：为模型变体提供统一框架。

- evidence_pointer：Equation (3)

### 50. Section 4.1 P2 Table 5

- order：50

- section：Section 4.1

- locator：Section 4.1 P2 Table 5

- move_code：DESIGN_FEATURE

- paraphrase_cn：框架沿relevance、unexpectedness、aggregation三个维度提供多种配置，如NCF/DIN、feature/latent、multiply/exponential/power。

- rhetorical_function_cn：明确可实例化的模型矩阵。

- depends_on_cn：Equation (3)。

- sets_up_cn：离线实验将测试这些配置。

- evidence_pointer：Table 5

### 51. Section 4.2 P1

- order：51

- section：Section 4.2

- locator：Section 4.2 P1

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：选择点击率预测任务，因为其与平台收入最相关。

- rhetorical_function_cn：为离线实验的任务选择辩护。

- depends_on_cn：推荐平台业务知识。

- sets_up_cn：介绍三个数据集和评价指标。

- evidence_pointer：Section 4.2

### 52. Section 4.2 P2

- order：52

- section：Section 4.2

- locator：Section 4.2 P2

- move_code：BENCHMARK_OR_CONTRAST

- paraphrase_cn：与四组八个state-of-the-art baselines比较，包括relevance、unexpectedness、diversity和bandit。

- rhetorical_function_cn：建立全面的评价参照。

- depends_on_cn：已有推荐算法分类。

- sets_up_cn：确保比较公平和全面。

- evidence_pointer：Section 4.2 P2

### 53. Section 4.3 P1

- order：53

- section：Section 4.3

- locator：Section 4.3 P1

- move_code：RESULT

- paraphrase_cn：提出的所有模型在三个数据集上都显著优于所有baseline。

- rhetorical_function_cn：报告离线实验核心结果。

- depends_on_cn：模型矩阵和baseline设置。

- sets_up_cn：给出平均提升和最佳模型。

- evidence_pointer：Table 7

### 54. Section 4.3 P1 平均提升句

- order：54

- section：Section 4.3

- locator：Section 4.3 P1 平均提升句

- move_code：RESULT

- paraphrase_cn：相对于第二好baseline，平均AUC和HR@10都提升3.81%。

- rhetorical_function_cn：量化整体增益。

- depends_on_cn：Table 7数据。

- sets_up_cn：强调增益在行业实践中是实质性的。

- evidence_pointer：Table 7

### 55. Section 4.3 P2

- order：55

- section：Section 4.3

- locator：Section 4.3 P2

- move_code：CONTRIBUTION

- paraphrase_cn：三个数据集代表不同行业和稀疏度，因此结果支持框架的泛化性和外部效度。

- rhetorical_function_cn：把离线结果提升为一般性结论。

- depends_on_cn：多个数据集结果。

- sets_up_cn：为线上实验做铺垫。

- evidence_pointer：Section 4.3

### 56. Section 5.1 P1

- order：56

- section：Section 5.1

- locator：Section 5.1 P1

- move_code：STUDY_OVERVIEW

- paraphrase_cn：为证明经济收益，在大型视频平台进行大规模线上受控实验。

- rhetorical_function_cn：从离线证据转入现场证据。

- depends_on_cn：离线实验结果。

- sets_up_cn：描述平台背景和实验规模。

- evidence_pointer：Section 5.1

### 57. Section 5.1 P1 自选择句

- order：57

- section：Section 5.1

- locator：Section 5.1 P1 自选择句

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：平台用户无法关注、搜索或共享，只能接受推荐，因此减少自选择偏差，便于估计ATE。

- rhetorical_function_cn：为实验平台的识别优势辩护。

- depends_on_cn：平台功能背景。

- sets_up_cn：介绍随机分流策略。

- evidence_pointer：Section 5.1

### 58. Section 5.2 P1

- order：58

- section：Section 5.2

- locator：Section 5.2 P1

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：通过user ID的二进制哈希随机分流到treatment/control，并检查倾向值平衡。

- rhetorical_function_cn：说明随机化操作。

- depends_on_cn：平台用户分流标准。

- sets_up_cn：回归识别策略。

- evidence_pointer：Section 5.2

### 59. Section 5.2 P2

- order：59

- section：Section 5.2

- locator：Section 5.2 P2

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：使用带用户/视频特征和时间固定效应的OLS回归估计ATE，见Equation (4)。

- rhetorical_function_cn：给出正式因果识别模型。

- depends_on_cn：随机分流。

- sets_up_cn：报告ATE结果。

- evidence_pointer：Equation (4)

### 60. Section 5.3 P1

- order：60

- section：Section 5.3

- locator：Section 5.3 P1

- move_code：RESULT

- paraphrase_cn：处理组比对照组CTR提高2.29%，VV提高4.56%，平均观看时长提高39.219秒。

- rhetorical_function_cn：报告线上核心结果。

- depends_on_cn：Equation (4)回归。

- sets_up_cn：讨论经济意义和部署。

- evidence_pointer：Table 9

### 61. Section 5.3 P2 机制句

- order：61

- section：Section 5.3

- locator：Section 5.3 P2 机制句

- move_code：MECHANISM

- paraphrase_cn：改进不意外，因为模型根据variety level个性化地平衡unexpectedness，避免了固定α导致的错配。

- rhetorical_function_cn：把统计效应解释为机制。

- depends_on_cn：ATE结果。

- sets_up_cn：引出经济影响声明。

- evidence_pointer：Section 5.3

### 62. Section 5.3 P2 经济句

- order：62

- section：Section 5.3

- locator：Section 5.3 P2 经济句

- move_code：PRACTICAL_STAKES

- paraphrase_cn：按CTR提升推算，模型可能给平台带来约3000万美元额外收入，且延迟和内存成本很小。

- rhetorical_function_cn：把结果转化为商业价值。

- depends_on_cn：CTR提升和平台收入。

- sets_up_cn：为部署声明提供依据。

- evidence_pointer：Section 5.3

### 63. Section 5.4 P1

- order：63

- section：Section 5.4

- locator：Section 5.4 P1

- move_code：RESULT

- paraphrase_cn：处理效应不是均匀的：高variety seeker和强烈反对variety的消费者获益最大，中等消费者获益较小。

- rhetorical_function_cn：揭示异质性。

- depends_on_cn：Treatment×Variety_Seeking交互。

- sets_up_cn：用个性化机制解释U型模式。

- evidence_pointer：Figure 5

### 64. Section 5.4 P1 解释句

- order：64

- section：Section 5.4

- locator：Section 5.4 P1 解释句

- move_code：MECHANISM

- paraphrase_cn：模型给variety seeker更多意外、给consistency seeker更多熟悉推荐，避免两类错配。

- rhetorical_function_cn：把异质性结果回接到核心机制。

- depends_on_cn：Figure 5的U型结果。

- sets_up_cn：为结论中的理论意义铺路。

- evidence_pointer：Section 5.4

### 65. Section 5.5 P1

- order：65

- section：Section 5.5

- locator：Section 5.5 P1

- move_code：RESULT

- paraphrase_cn：平行趋势显示预处理无差异，posttreatment期处理组持续显著优于对照组。

- rhetorical_function_cn：排除预先存在的趋势。

- depends_on_cn：日度CTR时间序列。

- sets_up_cn：说明长期有效而非短暂新奇。

- evidence_pointer：Figure 6

### 66. Section 5.6 P1

- order：66

- section：Section 5.6

- locator：Section 5.6 P1

- move_code：ROBUSTNESS_OR_BOUNDARY_TEST

- paraphrase_cn：通过不同特征组合、logit/probit、排除平台自有内容和新增地区等检验，结论仍然成立。

- rhetorical_function_cn：提供稳健性证据。

- depends_on_cn：线上回归结果。

- sets_up_cn：强化ATE的可靠性。

- evidence_pointer：Section 5.6, online appendix part VII

### 67. Conclusions P1

- order：67

- section：Conclusions

- locator：Conclusions P1

- move_code：CONTEXT

- paraphrase_cn：variety seeking在理解消费者意图和行为中很重要，推荐需要回应该需求。

- rhetorical_function_cn：重述研究的重要性。

- depends_on_cn：全文论证。

- sets_up_cn：总结两个框架和实验。

- evidence_pointer：Conclusions

### 68. Conclusions P3

- order：68

- section：Conclusions

- locator：Conclusions P3

- move_code：LIMITATION_AND_FUTURE

- paraphrase_cn：本文主要关注高消费率娱乐产品中的水平variety seeking，未来计划研究垂直差异化、其他平台和动态measure。

- rhetorical_function_cn：界定边界和未来方向。

- depends_on_cn：已有经验的边界。

- sets_up_cn：保护贡献不被过度泛化。

- evidence_pointer：Conclusions P3

## 写作技术

- gap_construction_cn：不是简单说‘没人研究’，而是列出三个技术性局限：不能处理细粒度产品嵌入、忽略dwell time、缺乏stationarity；同时把推荐系统的现有unexpectedness方法也暴露为‘固定α、忽略消费者异质性’，使两个缺口互相咬合。

- signposting_cn：频繁使用‘To summarize’‘In this paper’‘In Section 3.5’‘Note that’等路标；每节结束都有小结，把读者从测量框架推到推荐框架再推到实验。

- transition_logic_cn：测量框架验证后，用‘基于这个框架，我们转向推荐框架’过渡；离线实验后，用‘为证明经济收益’过渡到线上；线上ATE后用‘但是平均效应可能掩盖异质性’进入heterogeneous analysis。

- claim_evidence_rhythm_cn：每个主要声明后紧跟表格或图：测量效度→Table 4；stationarity→Table 1；离线性能→Table 7；线上ATE→Table 9；异质性→Figure 5；长期性→Figure 6。证据紧贴声明。

- benchmark_narrative_cn：不是只与一个baseline比，而是按四类方法建起‘全面对抗阵营’，再说明公平的hyperparameter tuning，最后用‘所有模型显著优于所有baseline’强化说服力。

- theory_return_cn：在结论和异质性分析中，用‘为variety seeker提供更多意外、为consistency seeker提供更熟悉’的机制解释结果，把统计效应重新绑定到营销理论和刺激需求理论。

- contribution_positioning_cn：在引言中列出First/Second/Final的贡献序列，在摘要中重复，在线下/线上实验后不断回指‘本文框架’，并以公司部署作为最终现实贡献锚点。

- novelty_protection_cn：通过三数据集泛化、多组件变体、线上大规模验证、异质性U型效应和长期平行趋势，把结果从‘一次性性能提升’提升为‘理论驱动的个性化设计知识’；即使某些变体不是最佳，也表明整个框架连续成立。

## 可复用研究与写作程序

### structure_steps

#### 1. 1

- step：1

- writing_job_cn：用一段话建立构念的现实重要性，给出可观察现象和商业后果。

- research_job_cn：确定要引入的消费者/用户行为构念，并找出现有文献中该构念未被技术领域处理的原因。

- required_evidence_cn：构念定义、已有营销/行为研究、推荐系统中的具体局限。

- transition_to_next_cn：'虽在A领域广泛研究，但在B系统中不足，因为具体限制1/2/3'。

#### 2. 2

- step：2

- writing_job_cn：把理论构念形式化为组件化框架，给出清晰公式和组件清单。

- research_job_cn：将构念拆成可计算维度，并设计可替换的函数/参数空间。

- required_evidence_cn：每个组件有理论或文献依据，能组合出多个具体测量模型。

- transition_to_next_cn：'当我们对三个组件做具体假设时，就得到相应measure；下面用问卷/ADF验证。'

#### 3. 3

- step：3

- writing_job_cn：用独立用户调查验证测量构念效度，并与已有measure比较。

- research_job_cn：设计问卷或用户报告题项，计算指标与自报指标的相关。

- required_evidence_cn：问卷数据、baseline指标、相关表、显著性检验。

- transition_to_next_cn：'测量指标有效后，把它嵌入下游系统设计。'

#### 4. 4

- step：4

- writing_job_cn：把测量指标作为设计输入，给出包含多个组件/操作化的推荐或决策框架。

- research_job_cn：定义新的utility/决策函数，列出可配置维度，并构造一组具体模型。

- required_evidence_cn：框架公式、组件选项表、至少一个理论上最优的候选。

- transition_to_next_cn：'下面用离线benchmark检验所有配置。'

#### 5. 5

- step：5

- writing_job_cn：在多数据集离线实验中与多类baseline比较，并报告最佳模型。

- research_job_cn：收集代表性数据集，设置公平超参优化，选择与业务相关的指标。

- required_evidence_cn：多个数据集、多个baseline、表格化结果、显著性标记。

- transition_to_next_cn：'离线不足以证明真实价值，因此进行大规模线上实验。'

#### 6. 6

- step：6

- writing_job_cn：用线上受控实验证明业务影响，再通过异质性、平行趋势和稳健性分析回护机制。

- research_job_cn：与平台合作随机分流，采集业务指标，做ATE、异质性和长期分析。

- required_evidence_cn：随机化平衡、回归结果、长期趋势、多项稳健性检验。

- transition_to_next_cn：'结果支持设计知识，最后总结边界和未来。'

### most_transferable_moves_cn

1. 把抽象行为构念拆成可计算组件并给出公式化框架

2. 用问卷自报数据验证测量效度

3. 将测量结果作为下游系统的个性化参数

4. 用多数据集和多类baseline构建全面benchmark

5. 以线上A/B实验和公司部署作为贡献锚点

6. 用异质性分析连接统计效应与理论机制

### resource_intensive_or_nonstandard_parts_cn

1. 与大型互联网平台的长期合作和线上A/B测试

2. 海量真实用户观看记录（37,965,781条）

3. Alibaba用户问卷和CEI-II心理测量

4. 多个工业级数据集的获取与处理

### what_not_to_copy_superficially_cn

1. 不能只把variety seeking乘进utility就声称框架有效，必须系统检验距离、时间衰减、stationarity三组件

2. 不能只依赖离线指标就声称业务影响，必须做随机化线上实验

3. 不能只做平均ATE就宣称机制成立，需要异质性和稳健性

4. 不能只列出baseline而不说明公平的超参优化

5. 没有真实部署时不应把‘公司已部署’作为贡献

- single_best_description_of_the_routine_cn：先构建可操作化测量框架并用问卷验证构念效度，再把构念嵌入推荐效用函数，用离线多场景benchmark确立相对优势，用大规模线上随机实验证明真实业务价值，最后用异质性/稳健性回护机制解释。

## 分析边界

分析基于全文主要章节和表格，未包含在线附录全部细节（如part I–X的具体问卷题目、DID细节、更多稳健性表）；图表只能依赖OCR和文字叙述判断，个别数字可能有OCR误差，但不影响整体结构判断。
