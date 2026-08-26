# Mitigating Exposure Bias for Recommendations in Physical Spaces: An Unbiased Pairwise Ranking Approach Using Spatial Movement

- 作者：Jiangning He; Weikun Wu; Fan Zhang; Zhepeng (Lionel) Li
- 年份 / 期刊：2026 / Information Systems Research
- DOI：10.1287/isre.2023.0100
- 源文件：28582_2026_mitigating-exposure-bias-for-recommendations-in-physical-spaces-an-unbiased-pairwise-ranking-app.md
- 论文主类型：build_evaluate_design_science
- 主导写作弧线：requirements_build_evaluate_design_principles
- 置信度：0.74

## 文章级论证概况

- 核心问题：如何在实体空间中针对行人移动与空间布局造成的非均匀曝光设计无偏的下一POI推荐方法？

- 制品与设计：提出UMPR方法：(1) 无偏pairwise学习框架，通过把访问序列切分成阶段并引入可学习去偏组件，重写经典BPR式目标；(2) 运动感知推荐模型，将相关分数建模为偏好匹配收益减去移动成本，并基于空间网络、最短路径、视觉角等操作化曝光因子和移动因子；(3) 交替随机梯度上升算法，交替估计相关参数与去偏权重。

- 客观结果：在北京大型购物中心167,234条访问序列、1,276,791次门店惠顾数据上，UMPR在Recall@1/3/5和DCG@3/5上均优于所有基准；消融显示运动和去偏组件都显著贡献；收入模拟显示可产生可观增量收入，例如γ=0.75时约合1.03亿美元；公平性分析显示REO下降13.5%–66.7%，对低曝光组的性能改进更明显。

- 核心贡献：首次形式化P3M问题，识别实体空间中由行人移动与空间布局动态交互导致的曝光偏差，提出UMPR统一无偏pairwise学习和运动建模；通过理论命题、真实数据benchmark、消融、收入模拟和公平性分析，将该问题和方法上升为IS设计科学研究贡献。

- 整篇论证链：作者先用在线推荐成功和Cheetah Mobile、Amazon Dash Cart等实体场景解释离线推荐需求，提出P3M问题；随后指出实体空间中曝光偏差的独特来源是行人移动与空间布局的动态交互，而现有去偏文献以数字平台为主且模型去偏只支持pointwise学习。为填补该缺口，作者设计无偏pairwise目标，以阶段切分消除跨阶段过度断言误差，以去偏组件消除把未曝光但可能相关的POI误当负样本的有偏误差，并给出Proposition 1和2。为使该目标可计算，作者构建空间网络、最短路径和agent式移动假设，把曝光建模为Access、Visibility、Popularity的加权和，把相关分数建模为偏好匹配收益与移动成本之差，设计交替SGA算法。实证部分先用北京商场数据与多类基准比较，得到UMPR全面最优；再用消融把优势归因于运动和去偏组件；随后用收入模拟和公平性分析证明经济价值与多利益相关者价值；最后把贡献回收为P3M问题、无偏pairwise学习和行人移动建模三方面设计知识，并列出假设依赖和未来方向。

## 类型与写作弧线判定

- 论文主类型判定：文章以构建新型推荐制品UMPR为中心，先概念化问题和提出设计要求，再实现制品，随后通过理论命题、真实数据benchmark、消融、收入模拟和公平性分析完成多层面评价，最终提炼可复用设计知识，符合设计科学研究的基本论证弧线。

- 主导写作弧线判定：全文从P3M与曝光偏差的需求出发，把问题转成无偏pairwise学习和运动建模要求，构建UMPR，再以性能、消融、经济和公平性评价，最后回到设计原则和管理含义，属于要求—构建—评价—设计原则的弧线。

## 研究开展程序

- study_or_phase_count：8

- 研究阶段总序列：研究从问题概念化开始，依次经过无偏学习目标、运动感知模型、学习算法三个设计阶段，再进入主实验、消融、收入模拟和公平性分析四个评价阶段。设计阶段回答‘做什么和为什么’，评价阶段回答‘是否有效、为什么有效、有什么价值’。前一个阶段为后一个阶段提供输入或尚未解决的问题。

### studies_or_phases

#### 1. 问题形式化与曝光偏差概念化

- order：1

- name_cn：问题形式化与曝光偏差概念化

- question_cn：实体空间POI推荐的一般问题是什么，为什么曝光偏差是关键阻碍？

- inputs_and_setting_cn：在线推荐成功案例、Cheetah Mobile机器人、Amazon Dash Cart、商场楼层平面与顾客视觉范围示例、既有数字平台曝光偏差文献。

- designed_or_compared_object_cn：P3M问题的正式定义；数字平台与物理空间现场曝光的对照。

- baseline_control_or_counterfactual_cn：以数字平台页面级印象为对照，凸显物理空间路径级视觉接触。

##### objective_metrics

（空）

- analysis_method_cn：概念化与文献综合，用商场简化场景说明曝光概率随位置、方向、视觉范围变化。

- main_result_cn：给出P3M定义，把曝光偏差的独特来源定位为行人移动与空间布局的动态交互。

- argumentative_role_cn：建立全文研究目标和问题空间，让后续算法设计对应一个明确问题。

- remaining_uncertainty_cn：尚无可纠正该偏差的具体算法或可操作模型。

- link_to_next_phase_cn：问题缺口自然引向无偏pairwise学习目标的设计。

##### evidence_pointers

1. Introduction P1–P4

2. Definition 3

3. Figure 1

#### 2. 无偏pairwise学习框架与理论保证

- order：2

- name_cn：无偏pairwise学习框架与理论保证

- question_cn：如何把模型化去偏从pointwise学习推广到pairwise学习？

- inputs_and_setting_cn：经典BPR pairwise目标、隐式反馈数据生成过程、曝光与相关二分解。

- designed_or_compared_object_cn：阶段切分的训练集D与去偏组件P(i≻_{u,k}j|D)，对比传统负性假设下的D0。

- baseline_control_or_counterfactual_cn：经典pairwise learning即去偏权重恒为1的情况。

##### objective_metrics

1. 训练误差减少比例（过度断言误差、有偏误差）

- analysis_method_cn：形式化建模与概率推导，提出Proposition 1和Proposition 2并给出图示。

- main_result_cn：得到无偏pairwise目标式(5)，去偏组件式(8)，以及阶段切分和去偏对训练错误的保证。

- argumentative_role_cn：建立算法的统计基础，回应文献中‘模型去偏缺少pairwise框架’的缺口。

- remaining_uncertainty_cn：该框架需要具体化曝光和相关分数才能用于真实空间。

- link_to_next_phase_cn：下一步把曝光和相关分数翻译成可计算的空间移动模型。

##### evidence_pointers

1. Section 4.1.1 Equation (4)–(5)

2. Section 4.1.2 Equation (6)–(8)

3. Section 4.1.3 Proposition 1–2

4. Figure 3

#### 3. 行人移动系统与运动感知推荐模型

- order：3

- name_cn：行人移动系统与运动感知推荐模型

- question_cn：如何把行人移动建模成可操作的曝光和相关分数估计？

- inputs_and_setting_cn：楼层平面图、访问序列、行人移动文献中的最短路径和视觉范围概念。

- designed_or_compared_object_cn：空间网络、移动路径、移动状态、曝光因子AC/VS/PO与移动因子DS/LD/DD/IV/DT。

- baseline_control_or_counterfactual_cn：以仅用地理距离的POI推荐和忽略移动成本的偏好匹配为对照。

##### objective_metrics

1. 曝光分数、相关分数的可计算性

- analysis_method_cn：基于图网络与agent模拟假设，给出式(9)–(17)的操作化公式。

- main_result_cn：得到运动感知推荐模型：相关分数=全局偏好+局部兴趣−移动成本，曝光分数依赖可达性和可见性。

- argumentative_role_cn：把理论去偏目标落地为可估计的制品，是UMPR区别于纯序列模型的核心。

- remaining_uncertainty_cn：模型参数无法用闭式解得到，需要设计学习算法。

- link_to_next_phase_cn：相关参数与去偏权重相互依赖，引出交替学习算法。

##### evidence_pointers

1. Section 4.2.1–4.2.4

2. Equations (9)–(17)

3. Assumptions 1 and 2

4. Figures 4 and 5

#### 4. 交替学习算法

- order：4

- name_cn：交替学习算法

- question_cn：去偏组件和推荐模型参数如何联合优化？

- inputs_and_setting_cn：无偏目标式(18)、点wise辅助目标式(20)、随机梯度上升。

- designed_or_compared_object_cn：Relevance_Params_Learner、Debiasing_Weight_Corrector、UMPR-ASGA交替算法。

- baseline_control_or_counterfactual_cn：用SGA直接学习但固定去偏权重的设定。

##### objective_metrics

1. 收敛条件

2. 参数更新方向

- analysis_method_cn：算法设计与交替优化。

- main_result_cn：Algorithm 1–3实现了相关参数和去偏权重的互相增强。

- argumentative_role_cn：解决模型学习可行性问题，使后续实证评价成为可能。

- remaining_uncertainty_cn：真实数据上的推荐性能尚不清楚。

- link_to_next_phase_cn：进入真实商场数据评价。

##### evidence_pointers

1. Section 4.3

2. Algorithm 1

3. Algorithm 2

4. Algorithm 3

#### 5. 主实验benchmark评价

- order：5

- name_cn：主实验benchmark评价

- question_cn：UMPR是否比现有推荐方法在P3M上更准确？

- inputs_and_setting_cn：北京某大型购物中心2019年9月1日至11月23日数据，共167,234条序列、175家店、1,276,791次惠顾。

- designed_or_compared_object_cn：UMPR与11个基准方法比较，包括UserKNN、ItemKNN、BPR-MF、FPMC、CoFiSet、Context-BPR、GRU4Rec、JODIE、SSE-PT、Cat-MPR、Dist-MPR和Random。

- baseline_control_or_counterfactual_cn：Random非个性化基线；不同方法家族；受控变体Cat-MPR和Dist-MPR。

##### objective_metrics

1. Recall@1

2. Recall@3

3. Recall@5

4. DCG@3

5. DCG@5

- analysis_method_cn：leave-one-out评估、网格搜索调参、配对t检验。

- main_result_cn：UMPR在所有指标上最优，相对每个基准的提升均显著；例如Recall@3相对JODIE提升9.2%，相对SSE-PT提升16.9%。

- argumentative_role_cn：证明UMPR技术优越性，并暗示显式建模移动与模型去偏的价值。

- remaining_uncertainty_cn：整体性能优势无法说明具体哪个设计组件导致。

- link_to_next_phase_cn：通过消融把性能归因到组件。

##### evidence_pointers

1. Section 5.1

2. Section 5.2

3. Table 3

4. Table 4

#### 6. 消融研究

- order：6

- name_cn：消融研究

- question_cn：运动和去偏两个组件各自对最终性能贡献多少？

- inputs_and_setting_cn：与主实验相同的数据和评估流程。

- designed_or_compared_object_cn：UMPR、移除运动组件的UMPR-M、移除去偏组件的UMPR-U。

- baseline_control_or_counterfactual_cn：UMPR-M将移动成本置零；UMPR-U将去偏权重设为1。

##### objective_metrics

1. Recall@1

2. Recall@3

3. Recall@5

4. DCG@3

5. DCG@5

- analysis_method_cn：受控变体比较。

- main_result_cn：两个组件都显著且互补；运动组件在短列表优势更明显，去偏组件在长列表优势更大。

- argumentative_role_cn：把算法性能进一步拆解为可识别的制品设计属性，支撑制品主张。

- remaining_uncertainty_cn：性能提升是否转化为经济价值和社会价值仍未知。

- link_to_next_phase_cn：用收入模拟和公平性分析考察价值外溢。

##### evidence_pointers

1. Section 5.3

2. Table 5

#### 7. 增量收入模拟

- order：7

- name_cn：增量收入模拟

- question_cn：更高的推荐精度能否转化为购物中心的增量收入？

- inputs_and_setting_cn：UMPR与各方法家族的best benchmark；推荐列表、曝光门店识别、访问概率衰减γ、人均消费约1.26美元。

- designed_or_compared_object_cn：四步模拟流程：生成推荐列表、识别沿途曝光门店、模拟访问概率、估计增量收入。

- baseline_control_or_counterfactual_cn：JODIE、Dist-MPR、FPMC、UserKNN等benchmark的模拟收入。

##### objective_metrics

1. 平均每条推荐增量收入

2. 相对收入改进百分比

- analysis_method_cn：100次并行模拟取平均，γ取值变化进行敏感性分析。

- main_result_cn：UMPR在所有γ下收入均最高；γ=0.75时每条推荐增量收入0.405美元，折算全商场年增量约1.03亿美元，占2019年总收入的32.2%。

- argumentative_role_cn：证明技术优势可以转化为货币价值，强化实践相关性。

- remaining_uncertainty_cn：收入依赖模拟假设，且未考察对不同门店群体的分配公平性。

- link_to_next_phase_cn：转向公平性分析考察对高低曝光组的影响。

##### evidence_pointers

1. Section 5.4

2. Figure 6

#### 8. 公平性分析

- order：8

- name_cn：公平性分析

- question_cn：去偏是否改善不同曝光水平门店之间的推荐公平？

- inputs_and_setting_cn：测试集中的ground-truth门店按Access、Visibility、Popularity分成高曝光和低曝光组。

- designed_or_compared_object_cn：UMPR与UMPR-U在每组的性能、REO和PI。

- baseline_control_or_counterfactual_cn：UMPR-U作为未去偏的对照。

##### objective_metrics

1. REO@5

2. Performance Improvement (PI) at Recall@5

- analysis_method_cn：分组比较和REO指标。

- main_result_cn：UMPR比UMPR-U的REO降低13.5%–66.7%；debiasing对低曝光组的性能提升更显著。

- argumentative_role_cn：证明方法缓解马太效应、促进多利益相关者公平，扩大贡献边界。

- remaining_uncertainty_cn：公平性来自离线指标，未测量真实顾客探索行为或门店长期收益。

- link_to_next_phase_cn：结论部分把经济和公平结果汇总为理论与设计贡献。

##### evidence_pointers

1. Section 5.5

2. Table 6

3. Figure 7

## 各部分修辞架构

### abstract_moves

1. CONTEXT

2. GAP

3. RQ_OR_OBJECTIVE

4. DESIGN_FEATURE

5. RESULT

6. BOUNDARY_CONDITION

### introduction_moves

1. CONTEXT

2. PRACTICAL_STAKES

3. PHENOMENON

4. MECHANISM

5. REQUIREMENT

6. LIMITATION

7. GAP

8. RQ_OR_OBJECTIVE

9. CONTRIBUTION

### theory_and_knowledge_moves

1. THEORY_INTRO

2. MECHANISM

3. LIMITATION

4. GAP

5. REQUIREMENT

6. DESIGN_FEATURE

7. PRIOR_KNOWLEDGE

### artifact_design_moves

1. DESIGN_FEATURE

2. THEORY_PROPOSITION

3. MECHANISM

4. METHOD_JUSTIFICATION

5. HYPOTHESIS_OR_PROPOSITION

### evaluation_moves

1. METHOD_JUSTIFICATION

2. BENCHMARK_OR_CONTRAST

3. STUDY_OVERVIEW

4. RESULT

5. ROBUSTNESS_OR_BOUNDARY_TEST

### discussion_and_contribution_moves

1. CONTRIBUTION

2. PRACTICAL_STAKES

3. BOUNDARY_CONDITION

4. LIMITATION_AND_FUTURE

## 理论/知识到设计的翻译

### 知识/理论基础

1. 隐式反馈推荐与BPR pairwise learning

2. 曝光偏差与missing-not-at-random文献

3. 营销文献中的事前曝光与现场曝光概念

4. 行人移动建模、空间句法与agent模拟

5. POI推荐中的地理距离与空间影响

- 理论—设计耦合：partial

- 耦合判定理由：设计高度依赖多支知识领域，尤其是数据生成过程、曝光两阶段理论和行人移动文献；但最终技术选择如具体曝光因子、视觉角、最短路径假设等来自领域工程和现有计算方法的组合，并非单一理论前瞻性推导，因此属于部分耦合。

- 理论到设计翻译链：隐式反馈数据生成中的曝光/相关分解 → 未观测不等于负样本 → 去偏组件作为未访问POI为负的概率 → 无偏pairwise目标；营销曝光两阶段 → 物理现场曝光由可达性和可见性决定 → Access和Visibility曝光因子 → 曝光分数；行人移动成本文献 → 距离、方向改变、不确定性和视觉干扰构成移动成本 → 移动因子 → 相关分数=偏好匹配收益−移动成本。

### mapping_table

#### 1. 1

- theory_or_knowledge_claim_cn：隐式反馈的生成可分解为曝光O和相关R，Y=O×R。

- mechanism_cn：未观测交互可能是未曝光或相关但未访问，不能一律视为负样本。

- design_requirement_cn：需要估计未访问POI确实为负的概率。

- artifact_choice_cn：去偏组件P(i≻_{u,k}j|D)=P(R=0|Y=0)并作为权重加入pairwise目标。

- evaluated_contrast_cn：UMPR vs UMPR-U（去偏权重设为1）。

- objective_result_cn：UMPR在Recall@5较UMPR-U提升8.9%–11.8%，DCG@5提升10.6%。

##### evidence_pointers

1. Section 4.1.2 Equations (6)–(8)

2. Section 5.3 Table 5

#### 2. 2

- theory_or_knowledge_claim_cn：曝光分为事前曝光与现场曝光；数字平台是页面级印象，物理空间是路径级视觉接触。

- mechanism_cn：行人在路径上的可达性和视觉可见性决定现场曝光；流行度决定事前曝光。

- design_requirement_cn：曝光分数需同时包含Access、Visibility和Popularity。

- artifact_choice_cn：曝光因子向量x=[AC,VS,PO]以及o=ρ^T[1;x]。

- evaluated_contrast_cn：UMPR与基于距离启发式去偏的Dist-MPR、以及按类别抽样的Cat-MPR比较。

- objective_result_cn：UMPR在Recall@3相对Dist-MPR提升14.1%，相对Cat-MPR提升15.0%。

##### evidence_pointers

1. Section 2.1 Table 1

2. Section 4.2.3

3. Section 5.2 Table 4

#### 3. 3

- theory_or_knowledge_claim_cn：行人移动成本包括距离、方向改变、不确定性和干扰，影响路径选择。

- mechanism_cn：顾客评估相关店时会权衡偏好匹配收益与移动到该店的成本。

- design_requirement_cn：相关分数应建模为收益减成本。

- artifact_choice_cn：r=b−c；b=p^T q+z_l^T q；c=ω^T m，其中m含DS、LD、DD、IV、DT。

- evaluated_contrast_cn：UMPR vs UMPR-M（移动成本置零）。

- objective_result_cn：UMPR在Recall@1提升16.3%，DCG@5提升8.3%。

##### evidence_pointers

1. Section 4.2.2 Equations (11)–(13)

2. Section 4.2.4

3. Section 5.3 Table 5

#### 4. 4

- theory_or_knowledge_claim_cn：顾客在一次购物中会因多目的而改变意图，跨阶段偏好比较会产生错误标签。

- mechanism_cn：在不同访问之间构建pair可能把‘后来访问但因目的变化’的店错误当作负样本。

- design_requirement_cn：应在相邻访问构成的阶段内构建pairwise关系。

- artifact_choice_cn：阶段化训练集D={(u,k,i,j)}。

- evaluated_contrast_cn：理论Proposition 1刻画与不切分训练集的误差差异。

- objective_result_cn：Proposition 1给出可消除的过度断言误差比例下界，并随偏好变化概率和序列长度增加而增加。

##### evidence_pointers

1. Section 4.1.1 Equation (4)

2. Section 4.1.3 Proposition 1

3. Figure 3(a)

#### 5. 5

- theory_or_knowledge_claim_cn：pairwise学习比pointwise学习更适合隐式反馈排序。

- mechanism_cn：pairwise直接优化正负项分数差，而非二分类概率。

- design_requirement_cn：去偏框架需要保持pairwise形式，而不是退回pointwise。

- artifact_choice_cn：无偏pairwise目标L=Σ P(i≻_j|D)lnσ(r_i−r_j)。

- evaluated_contrast_cn：UMPR与BPR-MF、FPMC等pairwise基准及pointwise变体比较。

- objective_result_cn：UMPR在Recall@3相对BPR-MF提升110.4%，相对FPMC提升19.3%。

##### evidence_pointers

1. Section 3.2

2. Section 4.1.1 Equation (5)

3. Table 4

#### 6. 6

- theory_or_knowledge_claim_cn：实体空间曝光由移动路径和视觉范围动态决定，现有POI推荐主要只考虑地理距离。

- mechanism_cn：忽略位置、方向和视觉范围会漏掉大量曝光变化，进而错误标记负样本。

- design_requirement_cn：需要空间网络、移动路径和agent式移动状态建模。

- artifact_choice_cn：行人移动系统（空间网络+最短路径+移动状态）及多维移动因子。

- evaluated_contrast_cn：UMPR与深度序列模型GRU4Rec/JODIE/SSE-PT以及距离式Dist-MPR比较。

- objective_result_cn：UMPR在Recall@3相对GRU4Rec提升16.4%，相对JODIE提升9.2%，相对SSE-PT提升16.9%。

##### evidence_pointers

1. Section 2.3

2. Section 4.2.1

3. Section 5.2 Table 4

## 评价逻辑

### evaluation_modes

1. 真实数据benchmark比较

2. 受控变体消融

3. 理论命题证明

4. 增量收入模拟

5. 公平性分组分析

- why_these_evaluations_cn：单一benchmark只能证明整体有效；消融用于把效果归因到具体组件；理论命题处理‘为什么能去偏’；收入模拟证明经济价值；公平性分析证明社会价值和边界。五类评价形成递进链条，每一环都回答前一个评价留下的未决问题。

- benchmark_and_contrast_chain_cn：先用Random建立最低参照，再按方法家族放置UserKNN/ItemKNN、BPR-MF/FPMC/CoFiSet/Context-BPR、GRU4Rec/JODIE/SSE-PT，并设计Cat-MPR和Dist-MPR作为与UMPR共享相关模型但使用启发式去偏的受控对照。Table 4证明整体优势；Table 5用UMPR-M和UMPR-U把优势归因到组件；Figure 6用收入模拟把优势转化为金额；Figure 7用REO把优势转化为公平性。

### claim_evidence_ledger

#### 1. UMPR在推荐准确性上优于SOTA与经典方法。

- claim_cn：UMPR在推荐准确性上优于SOTA与经典方法。

- evidence_cn：Table 4中所有指标全面最高，配对t检验p<0.001。

- strength_cn：高

#### 2. 运动组件和去偏组件都显著贡献性能。

- claim_cn：运动组件和去偏组件都显著贡献性能。

- evidence_cn：Table 5中UMPR分别比UMPR-M和UMPR-U显著提升，且两组件在不同N下优势不同。

- strength_cn：高

#### 3. 显式建模行人移动优于仅依赖隐式序列的深度模型。

- claim_cn：显式建模行人移动优于仅依赖隐式序列的深度模型。

- evidence_cn：UMPR相对GRU4Rec、JODIE、SSE-PT的Recall@3提升9.2%–16.9%。

- strength_cn：中高

#### 4. 模型化去偏优于启发式去偏。

- claim_cn：模型化去偏优于启发式去偏。

- evidence_cn：在相同相关模型下，UMPR相对Cat-MPR和Dist-MPR均有显著提升。

- strength_cn：高

#### 5. 阶段切分和去偏组件能减少训练误差。

- claim_cn：阶段切分和去偏组件能减少训练误差。

- evidence_cn：Proposition 1和2给出理论下界和比例表达式。

- strength_cn：中，因为依赖偏好变化概率τ和暴露相关假设

#### 6. 方法可带来显著增量收入。

- claim_cn：方法可带来显著增量收入。

- evidence_cn：Figure 6的模拟在多种γ下一致优于基准，γ=0.75时约合1.03亿美元年增量。

- strength_cn：中，因为收入来自模拟而非真实部署

#### 7. 去偏能促进低曝光组的公平。

- claim_cn：去偏能促进低曝光组的公平。

- evidence_cn：Figure 7显示UMPR的REO低于UMPR-U，且PI在低曝光组更高。

- strength_cn：中，离线公平指标，未测真实顾客探索行为

- internal_validity_strategy_cn：采用LOO策略避免随机划分泄漏；用再切分的验证集做网格搜索调参；通过UMPR-M、UMPR-U、Cat-MPR、Dist-MPR等受控变体隔离组件效应；使用配对t检验；收入模拟执行100次取平均；公平性分组依据明确操作化定义。

- external_validity_strategy_cn：选择跨方法家族基准以覆盖广泛推荐范式；在线附录进行序列切分、替代路径策略、流行度口径等稳健性检查；结论将方法推广到超市、商业街、世博会等物理空间；公平性分析覆盖顾客、门店和商场多个利益相关者。

- what_is_not_actually_tested_cn：未进行现场实验，未观察真实用户对推荐的反应；没有真实完整移动轨迹，移动路径依赖最短路径假设；曝光没有被直接测量，而是用AC/VS/PO近似；增量收入完全来自模拟；推荐结果显示带来的新型曝光偏差未被处理；所有观测访问均被当作正反馈的假设未被检验。

## 贡献闭环

- technical_claim_cn：UMPR在P3M任务上的推荐准确率显著优于多个经典和最新方法，且能降低理论训练误差。

- artifact_claim_cn：无偏pairwise学习中的去偏组件和运动感知模型中的移动成本组件分别且互补地贡献了性能提升。

- mechanism_claim_cn：实体空间曝光偏差来自路径级视觉接触，去偏组件通过估计未访问POI为负的概率纠正负样本标签；相关分数中加入移动成本能更准确反映行人决策。

- boundary_claim_cn：方法适用于以行人移动和空间布局为特征的P3M场景，在中等至大型实体空间尤其有价值；效果受最短路径、视觉角、观测访问为正等假设约束。

- reusable_design_knowledge_cn：应将物理空间表示为空间网络并动态建模位置、方向和视觉范围；模型化去偏应尽量与pairwise学习统一；相关分数应包含偏好匹配收益与移动成本的权衡。

- theoretical_contribution_cn：把曝光偏差研究从数字平台扩展到物理空间，首次形式化P3M；提出无偏pairwise学习框架，填补模型去偏与pairwise学习的交叉空白；以Proposition 1和2给出训练误差减少的理论保证。

- how_discussion_closes_intro_gap_cn：结论逐条回应引言的两大缺口：一是模型去偏缺少pairwise框架，二是物理空间动态移动建模被忽视；随后把方法贡献表述为P3M问题、无偏pairwise学习和运动建模三方面，并给出与曝光偏差、马太效应等引言概念的连接。

- overclaim_or_unsupported_leaps_cn：收入测算依赖模拟假设却以“1.03亿美元”作营销式陈述；公平性只来自离线REO，却宣称能创造探索体验和平衡客流；理论命题依赖τ_u和b_uk等不可观测量，实证中未直接估计；把‘性能提升’外推为‘设计知识’需要更多跨场景证据。

## 句级写作动作图谱

### 1. Abstract P1

- order：1

- section：Abstract

- locator：Abstract P1

- move_code：CONTEXT

- paraphrase_cn：在线个性化推荐的成功激发了将其扩展到物理空间的兴趣。

- rhetorical_function_cn：建立背景并引出离线推荐的总问题。

- depends_on_cn：无，全文开头。

- sets_up_cn：为引入P3M问题做铺垫。

- evidence_pointer：Abstract

### 2. Abstract P2

- order：2

- section：Abstract

- locator：Abstract P2

- move_code：GAP

- paraphrase_cn：P3M中的一个关键但研究不足的问题是曝光偏差。

- rhetorical_function_cn：迅速点出核心问题。

- depends_on_cn：前一句建立的应用背景。

- sets_up_cn：说明全文要解决的问题。

- evidence_pointer：Abstract

### 3. Abstract P2 S2

- order：3

- section：Abstract

- locator：Abstract P2 S2

- move_code：MECHANISM

- paraphrase_cn：与数字平台不同，这里曝光偏差源于行人移动与空间布局的动态交互。

- rhetorical_function_cn：限定问题的独特机制，与既有文献区分。

- depends_on_cn：曝光偏差概念。

- sets_up_cn：为方法需要运动建模提供理据。

- evidence_pointer：Abstract

### 4. Abstract P3

- order：4

- section：Abstract

- locator：Abstract P3

- move_code：RQ_OR_OBJECTIVE

- paraphrase_cn：为此提出UMPR，包括无偏pairwise学习、运动感知模型和交替学习算法。

- rhetorical_function_cn：预告制品的三个组成部分。

- depends_on_cn：第二句的缺口。

- sets_up_cn：为正文Section 4的组织提供路标。

- evidence_pointer：Abstract

### 5. Abstract P4

- order：5

- section：Abstract

- locator：Abstract P4

- move_code：RESULT

- paraphrase_cn：真实商场数据证明方法优于SOTA基准。

- rhetorical_function_cn：给出主要实证结论。

- depends_on_cn：UMPR设计。

- sets_up_cn：为摘要中的价值声明提供证据锚。

- evidence_pointer：Abstract

### 6. Abstract P5

- order：6

- section：Abstract

- locator：Abstract P5

- move_code：BOUNDARY_CONDITION

- paraphrase_cn：进一步研究显示性能提升可转化为货币价值并保持对顾客和租户的公平。

- rhetorical_function_cn：把技术结果扩展为多维价值承诺。

- depends_on_cn：主结果。

- sets_up_cn：引出后文的收入模拟与公平性分析。

- evidence_pointer：Abstract

### 7. Introduction P1

- order：7

- section：Introduction

- locator：Introduction P1

- move_code：PRACTICAL_STAKES

- paraphrase_cn：实体零售正寻求把在线个性化推荐转移到线下，Cheetah Mobile和Amazon Dash Cart等例子显示可提高销售与转化。

- rhetorical_function_cn：说明研究主题的商业重要性。

- depends_on_cn：在线推荐成功这一背景。

- sets_up_cn：为P3M问题提供真实场景。

- evidence_pointer：Introduction P1

### 8. Introduction P2

- order：8

- section：Introduction

- locator：Introduction P2

- move_code：PHENOMENON

- paraphrase_cn：P3M包含多样化POI、特定的空间布局和行人移动三个特征，目标是基于访问序列推荐下一个POI。

- rhetorical_function_cn：正式化研究对象。

- depends_on_cn：离线推荐应用背景。

- sets_up_cn：让算法设计对应明确的输入输出。

- evidence_pointer：Introduction P2

### 9. Introduction P3

- order：9

- section：Introduction

- locator：Introduction P3

- move_code：GAP

- paraphrase_cn：曝光偏差在物理空间中尤为明显，受流行度、空间布局和移动路径影响，但现有研究未充分探索。

- rhetorical_function_cn：把一般偏差问题聚焦到物理空间的特殊来源。

- depends_on_cn：前一句的P3M三特征。

- sets_up_cn：为后文‘动态交互是主因’做铺垫。

- evidence_pointer：Introduction P3

### 10. Introduction P4 example

- order：10

- section：Introduction

- locator：Introduction P4 example

- move_code：PHENOMENON

- paraphrase_cn：用商场例子说明顾客位于某店外时，视觉范围内的店更可能被曝光，移动时曝光集合会变化。

- rhetorical_function_cn：用具体场景让抽象机制可见。

- depends_on_cn：曝光偏差概念。

- sets_up_cn：说明必须模拟移动状态。

- evidence_pointer：Introduction P4, Figure 1

### 11. Introduction P4 last

- order：11

- section：Introduction

- locator：Introduction P4 last

- move_code：MECHANISM

- paraphrase_cn：把未访问店一律当负样本会严重偏差学习，加剧马太效应并损害探索体验。

- rhetorical_function_cn：解释偏差的后果。

- depends_on_cn：商场曝光例子。

- sets_up_cn：支持必须纠正曝光偏差的主张。

- evidence_pointer：Introduction P4

### 12. Introduction P4 final sentence

- order：12

- section：Introduction

- locator：Introduction P4 final sentence

- move_code：REQUIREMENT

- paraphrase_cn：因此需要动态建模物理空间中的行人移动并将其纳入无偏推荐。

- rhetorical_function_cn：从机制转换为设计要求。

- depends_on_cn：偏差后果。

- sets_up_cn：引出UMPR的方法方向。

- evidence_pointer：Introduction P4

### 13. Introduction P5 first gap

- order：13

- section：Introduction

- locator：Introduction P5 first gap

- move_code：LIMITATION

- paraphrase_cn：启发式去偏因去偏与学习脱节而次优；模型去偏多为pointwise，缺pairwise去偏框架。

- rhetorical_function_cn：通过文献局限制造方法缺口。

- depends_on_cn：前文曝光偏差问题。

- sets_up_cn：这是贡献一。

- evidence_pointer：Introduction P5

### 14. Introduction P5 second gap

- order：14

- section：Introduction

- locator：Introduction P5 second gap

- move_code：LIMITATION

- paraphrase_cn：现有研究主要处理数字平台页面级曝光，物理空间中的移动与布局交互未得到充分关注。

- rhetorical_function_cn：指出第二类文献缺口。

- depends_on_cn：曝光机制对比。

- sets_up_cn：这是贡献二。

- evidence_pointer：Introduction P5

### 15. Introduction P6

- order：15

- section：Introduction

- locator：Introduction P6

- move_code：RQ_OR_OBJECTIVE

- paraphrase_cn：我们率先处理物理推荐中由行人移动引起的曝光偏差，提出UMPR。

- rhetorical_function_cn：从缺口跳转到本文目标。

- depends_on_cn：两个gap。

- sets_up_cn：概括方法并预告 Figure 2。

- evidence_pointer：Introduction P6

### 16. Section 2.1 paragraph 1

- order：16

- section：Related Work

- locator：Section 2.1 paragraph 1

- move_code：THEORY_INTRO

- paraphrase_cn：基于营销文献把曝光分为事前曝光和现场曝光。

- rhetorical_function_cn：为曝光因素选择提供理论名目。

- depends_on_cn：曝光偏差定义。

- sets_up_cn：支持Later AC/VS/PO的选择。

- evidence_pointer：Section 2.1

### 17. Section 2.1 digital vs physical

- order：17

- section：Related Work

- locator：Section 2.1 digital vs physical

- move_code：MECHANISM

- paraphrase_cn：数字平台是页面级印象，由算法展示决定；物理空间是路径级视觉接触，由行人移动与布局决定。

- rhetorical_function_cn：通过对比揭示物理空间曝光偏差的特殊机制。

- depends_on_cn：事前/现场曝光划分。

- sets_up_cn：为Table 1和后续method设计提供依据。

- evidence_pointer：Section 2.1, Table 1

### 18. Section 2.1 last

- order：18

- section：Related Work

- locator：Section 2.1 last

- move_code：REQUIREMENT

- paraphrase_cn：因此需要引入行人移动系统和曝光因子来捕获物理空间中的曝光。

- rhetorical_function_cn：从机制转换为设计要求。

- depends_on_cn：路径级视觉接触概念。

- sets_up_cn：为空间网络与AC/VS/PO操作化铺路。

- evidence_pointer：Section 2.1 last paragraph

### 19. Section 2.2.1

- order：19

- section：Related Work

- locator：Section 2.2.1

- move_code：LIMITATION

- paraphrase_cn：启发式加权或抽样的去偏阶段与模型学习阶段脱节，难以保证效果。

- rhetorical_function_cn：批评一类已有方法。

- depends_on_cn：文献分类。

- sets_up_cn：为模型化去偏铺路。

- evidence_pointer：Section 2.2.1

### 20. Section 2.2.2

- order：20

- section：Related Work

- locator：Section 2.2.2

- move_code：GAP

- paraphrase_cn：现有模型化去偏主要面向pointwise学习，如何与pairwise学习整合仍未被研究。

- rhetorical_function_cn：精确定位空白格。

- depends_on_cn：启发式与模型化去偏的分类。

- sets_up_cn：引向无偏pairwise学习这一核心贡献。

- evidence_pointer：Section 2.2.2

### 21. Section 2.3.2

- order：21

- section：Related Work

- locator：Section 2.3.2

- move_code：LIMITATION

- paraphrase_cn：POI推荐文献大多只利用地理距离，缺乏对位置、方向和视觉范围等动态空间交互的刻画。

- rhetorical_function_cn：界定空间建模上的缺口。

- depends_on_cn：POI推荐综述。

- sets_up_cn：支持多维运动建模的必要性。

- evidence_pointer：Section 2.3.2

### 22. Section 3.1

- order：22

- section：Preliminaries

- locator：Section 3.1

- move_code：RQ_OR_OBJECTIVE

- paraphrase_cn：形式化定义访问序列、楼层平面图和P3M问题。

- rhetorical_function_cn：把问题变成可计算定义。

- depends_on_cn：引言中的P3M描述。

- sets_up_cn：为pairwise目标提供数学对象。

- evidence_pointer：Section 3.1, Definitions 1–3

### 23. Section 3.2

- order：23

- section：Preliminaries

- locator：Section 3.2

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：pairwise学习直接优化排序且适合隐式反馈，因此被选为方法框架。

- rhetorical_function_cn：为框架选择提供文献理由。

- depends_on_cn：P3M属于隐式反馈。

- sets_up_cn：引出BPR目标以及后续改良。

- evidence_pointer：Section 3.2

### 24. Section 3.2 limitation one

- order：24

- section：Preliminaries

- locator：Section 3.2 limitation one

- move_code：LIMITATION

- paraphrase_cn：负性假设把所有未访问POI当负样本，但其中混合了真正负样本和可能正样本。

- rhetorical_function_cn：指出经典BPR在P3M中的严重缺陷。

- depends_on_cn：pairwise训练数据定义。

- sets_up_cn：为去偏组件提供动机。

- evidence_pointer：Section 3.2

### 25. Section 3.2 limitation two

- order：25

- section：Preliminaries

- locator：Section 3.2 limitation two

- move_code：LIMITATION

- paraphrase_cn：经典模型只做偏好匹配，忽视行人移动的物理成本。

- rhetorical_function_cn：指出第二类缺陷。

- depends_on_cn：BPR-MF相关分数定义。

- sets_up_cn：为运动成本项提供动机。

- evidence_pointer：Section 3.2

### 26. Section 4.1.1 stage segmentation

- order：26

- section：UMPR Method

- locator：Section 4.1.1 stage segmentation

- move_code：DESIGN_FEATURE

- paraphrase_cn：把访问序列切成相邻访问之间的多个阶段，并给出三条好处。

- rhetorical_function_cn：介绍第一大设计策略。

- depends_on_cn：Preliminaries中的序列定义。

- sets_up_cn：为Proposition 1提供对象。

- evidence_pointer：Section 4.1.1

### 27. Section 4.1.1 debiasing component

- order：27

- section：UMPR Method

- locator：Section 4.1.1 debiasing component

- move_code：DESIGN_FEATURE

- paraphrase_cn：引入P(i≻_{u,k}j|D)作为无偏权重，重写经典pairwise目标。

- rhetorical_function_cn：介绍第二大设计策略。

- depends_on_cn：阶段化训练集D。

- sets_up_cn：为后续概率推导提供目标函数。

- evidence_pointer：Section 4.1.1, Equation (5)

### 28. Section 4.1.2

- order：28

- section：UMPR Method

- locator：Section 4.1.2

- move_code：THEORY_PROPOSITION

- paraphrase_cn：假设观测行为由曝光和相关两个过程相乘生成，Y=O×R。

- rhetorical_function_cn：给出去偏权重的数据生成基础。

- depends_on_cn：隐式反馈文献。

- sets_up_cn：导出未访问POI为负的概率公式。

- evidence_pointer：Section 4.1.2, Equation (6)

### 29. Section 4.1.2 interpretation

- order：29

- section：UMPR Method

- locator：Section 4.1.2 interpretation

- move_code：MECHANISM

- paraphrase_cn：去偏组件等于未访问POI为负的概率，能同时利用曝光和相关概率。

- rhetorical_function_cn：把公式翻译成去偏机制。

- depends_on_cn：式(7)–(8)推导。

- sets_up_cn：说明方法在曝光估计不完整时仍能工作。

- evidence_pointer：Section 4.1.2

### 30. Section 4.1.3 Proposition 1

- order：30

- section：UMPR Method

- locator：Section 4.1.3 Proposition 1

- move_code：HYPOTHESIS_OR_PROPOSITION

- paraphrase_cn：Proposition 1给出阶段切分至少可消除多少过度断言误差。

- rhetorical_function_cn：把设计策略转化为可验证的理论保证。

- depends_on_cn：定义4与阶段切分。

- sets_up_cn：证明策略有效，为后文benchmark提供理论背书。

- evidence_pointer：Section 4.1.3, Proposition 1, Figure 3(a)

### 31. Section 4.1.3 Proposition 2

- order：31

- section：UMPR Method

- locator：Section 4.1.3 Proposition 2

- move_code：HYPOTHESIS_OR_PROPOSITION

- paraphrase_cn：Proposition 2给出去偏组件可消除有偏误差的比例。

- rhetorical_function_cn：证明去偏策略有效。

- depends_on_cn：定义5与式(8)。

- sets_up_cn：说明在POI数较少时去偏仍重要。

- evidence_pointer：Section 4.1.3, Proposition 2, Figure 3(b)

### 32. Section 4.2.1

- order：32

- section：UMPR Method

- locator：Section 4.2.1

- move_code：DESIGN_FEATURE

- paraphrase_cn：基于楼层平面图构建空间网络，节点为POI和锚点，边为同层与跨层通道。

- rhetorical_function_cn：把楼层平面图变成算法可用图结构。

- depends_on_cn：Definition 2中的floor plan。

- sets_up_cn：用于生成移动路径。

- evidence_pointer：Section 4.2.1

### 33. Section 4.2.1 Assumption 1

- order：33

- section：UMPR Method

- locator：Section 4.2.1 Assumption 1

- move_code：THEORY_PROPOSITION

- paraphrase_cn：假定行人在两次访问之间走最短路径。

- rhetorical_function_cn：用可计算假设替代不可观测的真实路径。

- depends_on_cn：空间网络。

- sets_up_cn：支持移动路径和曝光/移动因子提取。

- evidence_pointer：Section 4.2.1, Assumption 1

### 34. Section 4.2.1 Assumption 2

- order：34

- section：UMPR Method

- locator：Section 4.2.1 Assumption 2

- move_code：THEORY_PROPOSITION

- paraphrase_cn：假定行人沿网络边移动，移动方向与边一致，视觉范围为方向两侧各ϑ/2。

- rhetorical_function_cn：把视觉范围变为可计算参数。

- depends_on_cn：space syntax agent模拟文献。

- sets_up_cn：定义Visibility和Invisibility等因子。

- evidence_pointer：Section 4.2.1, Assumption 2

### 35. Section 4.2.2

- order：35

- section：UMPR Method

- locator：Section 4.2.2

- move_code：DESIGN_FEATURE

- paraphrase_cn：曝光分数建模为曝光因子的线性加权，相关分数建模为偏好匹配收益减移动成本。

- rhetorical_function_cn：给出模型核心公式。

- depends_on_cn：Pedestrian movement system。

- sets_up_cn：把无偏目标中的概率替换为可学习分数。

- evidence_pointer：Section 4.2.2, Equations (9)–(11)

### 36. Section 4.2.3

- order：36

- section：UMPR Method

- locator：Section 4.2.3

- move_code：DESIGN_FEATURE

- paraphrase_cn：曝光因子包括Access、Visibility和Popularity，分别刻画可达、视觉和事前曝光。

- rhetorical_function_cn：将概念转化为具体操作化变量。

- depends_on_cn：曝光两阶段概念。

- sets_up_cn：用于估计曝光概率。

- evidence_pointer：Section 4.2.3, Equations following 10

### 37. Section 4.2.4

- order：37

- section：UMPR Method

- locator：Section 4.2.4

- move_code：DESIGN_FEATURE

- paraphrase_cn：移动因子包括距离、楼层差、方向差、不可见性和分心，共同构成移动成本。

- rhetorical_function_cn：把移动成本多维操作化。

- depends_on_cn：行人移动文献。

- sets_up_cn：用于计算相关分数中的成本项。

- evidence_pointer：Section 4.2.4, Equations (14)–(17)

### 38. Section 4.3

- order：38

- section：UMPR Method

- locator：Section 4.3

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：由于相关参数与去偏权重互相依赖，设计交替SGA算法。

- rhetorical_function_cn：解释算法设计的必要性。

- depends_on_cn：目标式(18)和式(20)。

- sets_up_cn：给出完整可训练流程。

- evidence_pointer：Section 4.3, Algorithm 3

### 39. Section 5.1

- order：39

- section：Empirical Evaluation

- locator：Section 5.1

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：使用北京大型商场真实访客视频追踪数据，并按LOO策略划分训练与测试。

- rhetorical_function_cn：说明数据来源和评估方式的合理性。

- depends_on_cn：P3M问题中的实际场景。

- sets_up_cn：让Table 4的对比可复现。

- evidence_pointer：Section 5.1

### 40. Section 5.2

- order：40

- section：Empirical Evaluation

- locator：Section 5.2

- move_code：BENCHMARK_OR_CONTRAST

- paraphrase_cn：选择多个经典与SOTA方法，并设计Cat-MPR和Dist-MPR作为受控去偏变体。

- rhetorical_function_cn：建立评价参照系。

- depends_on_cn：推荐方法分类。

- sets_up_cn：支撑主实验结论。

- evidence_pointer：Section 5.2, Table 3

### 41. Section 5.2 Table 4 result

- order：41

- section：Empirical Evaluation

- locator：Section 5.2 Table 4 result

- move_code：RESULT

- paraphrase_cn：UMPR在所有指标上最佳并显著优于每个基准。

- rhetorical_function_cn：给出核心实证证据。

- depends_on_cn：benchmark设置。

- sets_up_cn：支持后续消融和价值分析。

- evidence_pointer：Section 5.2, Table 4

### 42. Section 5.2 interpretation

- order：42

- section：Empirical Evaluation

- locator：Section 5.2 interpretation

- move_code：MECHANISM

- paraphrase_cn：与深度序列模型比，优势来自显式建模移动；与启发式变体比，优势来自模型化去偏。

- rhetorical_function_cn：把结果解释为机制，而非单纯调参。

- depends_on_cn：Table 4相对提升。

- sets_up_cn：引出消融和组件归因。

- evidence_pointer：Section 5.2

### 43. Section 5.3

- order：43

- section：Empirical Evaluation

- locator：Section 5.3

- move_code：STUDY_OVERVIEW

- paraphrase_cn：通过去掉运动组件或去偏组件构建UMPR-M和UMPR-U两个对照。

- rhetorical_function_cn：预告消融研究方法。

- depends_on_cn：前文组件定义。

- sets_up_cn：为Table 5结果提供设计。

- evidence_pointer：Section 5.3

### 44. Section 5.3 results

- order：44

- section：Empirical Evaluation

- locator：Section 5.3 results

- move_code：RESULT

- paraphrase_cn：两个组件都显著贡献，且在不同推荐列表长度下各有优势。

- rhetorical_function_cn：证明组件级因果归因。

- depends_on_cn：Table 5。

- sets_up_cn：说明UMPR不是单一技巧带来的改进。

- evidence_pointer：Section 5.3, Table 5

### 45. Section 5.4 motivation

- order：45

- section：Empirical Evaluation

- locator：Section 5.4 motivation

- move_code：PRACTICAL_STAKES

- paraphrase_cn：行人接受推荐需要实际移动，移动途中可能被其他推荐店吸引，从而产生增量购买。

- rhetorical_function_cn：说明为什么推荐精度可转化为收入。

- depends_on_cn：P3M的物理移动属性。

- sets_up_cn：引出增量收入模拟。

- evidence_pointer：Section 5.4

### 46. Section 5.4 results

- order：46

- section：Empirical Evaluation

- locator：Section 5.4 results

- move_code：RESULT

- paraphrase_cn：模拟显示UMPR在多个衰减率下均产生最高增量收入，可折算为可观的年度额外收入。

- rhetorical_function_cn：把技术性能转化为经济证据。

- depends_on_cn：模拟流程和best benchmark选择。

- sets_up_cn：支持结论中的managerial implications。

- evidence_pointer：Section 5.4, Figure 6

### 47. Section 5.5

- order：47

- section：Empirical Evaluation

- locator：Section 5.5

- move_code：STUDY_OVERVIEW

- paraphrase_cn：按曝光因子把ground-truth门店分成高低曝光组，用REO衡量公平。

- rhetorical_function_cn：说明公平性评价的设计。

- depends_on_cn：曝光因子定义。

- sets_up_cn：为Figure 7结果做铺垫。

- evidence_pointer：Section 5.5, Table 6

### 48. Section 5.5 results

- order：48

- section：Empirical Evaluation

- locator：Section 5.5 results

- move_code：RESULT

- paraphrase_cn：UMPR比UMPR-U的REO更低，且对低曝光组的性能提升更显著。

- rhetorical_function_cn：证明去偏促进公平。

- depends_on_cn：REO和PI指标。

- sets_up_cn：引出结论中关于马太效应和探索体验的讨论。

- evidence_pointer：Section 5.5, Figure 7

### 49. Section 6 contributions

- order：49

- section：Conclusion

- locator：Section 6 contributions

- move_code：CONTRIBUTION

- paraphrase_cn：总结三点贡献：P3M问题、无偏pairwise学习框架、运动感知模型。

- rhetorical_function_cn：把全文工作抽象为研究贡献。

- depends_on_cn：方法、理论命题、实证结果。

- sets_up_cn：为后续设计科学定位和managerial implications提供结构。

- evidence_pointer：Section 6

### 50. Section 6 limitations

- order：50

- section：Conclusion

- locator：Section 6 limitations

- move_code：LIMITATION_AND_FUTURE

- paraphrase_cn：方法依赖多项假设，缺少现场实验，未来可放宽正反馈假设、获取真实轨迹、扩展到3D和其他空间。

- rhetorical_function_cn：限定贡献边界并提出后续问题。

- depends_on_cn：方法中所作假设。

- sets_up_cn：保护贡献不被过度泛化。

- evidence_pointer：Section 6 last paragraph

## 写作技术

- gap_construction_cn：先在Related Work中建立两类文献的维度表，把‘模型去偏×pairwise学习’和‘物理空间×动态移动’做成空白格；再用‘under-investigated’和‘remains underexplored’反复定位；同时用商场视觉范围的具体例子让缺口在现象层面可感知。

- signposting_cn：Abstract和Introduction结尾都对UMPR三组件做了显式路标；Section 5开头列出四种评价目标；Conclusion以贡献编号重述全文。Figures 1–7在叙述中被提前调用，增强空间感。

- transition_logic_cn：每个方法小节末尾用‘因此需要/为了…’连接到下一阶段；实证小节末尾常用‘Having demonstrated… we further…’把benchmark推进到消融、收入、公平；理论小节末尾把命题与Figure 3相连后立即转回模型学习。

- claim_evidence_rhythm_cn：先给总体结论，再给表/图，再逐条解释‘First/Second/Third’；每个数值后紧跟相对提升百分比和t检验；解释时把结果回收到具体机制，而不是停在统计显著性。

- benchmark_narrative_cn：benchmark不是单纯罗列，而按方法家族分组，并加入Cat-MPR和Dist-MPR两个受控变体，使得‘模型去偏优于启发去偏’和‘explicit movement优于implicit sequence’两类主张都能从同一张表中读出。

- theory_return_cn：Proposition 1和2在方法部分证明误差减少，消融在实证部分对应验证实际误差减少；结论把这些命题与P3M问题重新绑定，使结果不是一次性精度，而是‘无偏pairwise学习有效’的理论知识。

- contribution_positioning_cn：贡献分三层：问题贡献、方法贡献、建模贡献，分别对应引言两个gap和空间建模缺口；在IS设计科学语境中使用‘design artifacts’和‘design insights’提升一般性。

- novelty_protection_cn：通过Table 2中的空白格、两个Proposition、受控变体消融、经济模拟和公平性分析，把UMPR定位成‘不仅在这个数据集上更好’，而是‘填补了文献交叉空白且具有机制保证的设计知识’，避免被读作一次性调参结果。

## 可复用研究与写作程序

### structure_steps

#### 1. 1

- step：1

- writing_job_cn：用一到两段把在线背景、现实例子和商业后果写清楚，提出一般化问题并给正式定义。

- research_job_cn：识别真实物理环境中可形式化的推荐问题，并找到关键机制型阻碍。

- required_evidence_cn：有可复现的应用案例或领域机制；问题定义能对应明确输入输出。

- transition_to_next_cn：一般化问题必须指出一个具体偏差/阻碍，从而进入文献缺口。

#### 2. 2

- step：2

- writing_job_cn：用文献分类表把现有方法归类，显式指出一个空白格。

- research_job_cn：系统梳理相关文献并确定未被满足的方法需求。

- required_evidence_cn：文献分类与每类代表作品；空白格的‘缺什么’要可操作。

- transition_to_next_cn：缺口应自然映射到方法目标的三个组件。

#### 3. 3

- step：3

- writing_job_cn：先给学习目标、数据生成过程和命题，再给可学习模型。

- research_job_cn：把问题形式化为优化目标，并用理论命题保证目标设计合理。

- required_evidence_cn：推导完整；命题有界或可计算；假设有文献支持。

- transition_to_next_cn：理论目标需要可计算参数，因此进入制品实现。

#### 4. 4

- step：4

- writing_job_cn：把每个理论构件翻译成可操作因子、公式和算法，包括假设说明。

- research_job_cn：构建空间网络、因子提取、模型结构和学习算法。

- required_evidence_cn：每个因子有操作化公式和对应用途；算法有收敛设定。

- transition_to_next_cn：制品完成后需要说明数据来源和评价协议。

#### 5. 5

- step：5

- writing_job_cn：在同一数据集上做多家族基准、受控变体消融、价值与公平分析。

- research_job_cn：设计对照，使性能提升可归因于设计组件，并扩展价值主张。

- required_evidence_cn：主结果显著；消融能分离组件；价值模拟有透明假设。

- transition_to_next_cn：评价结果需回收为研究贡献和边界条件。

#### 6. 6

- step：6

- writing_job_cn：结论部分按问题、方法、建模三层重述贡献，并列出假设与未来方向。

- research_job_cn：把局部结果上升为可复用设计知识和适用范围。

- required_evidence_cn：贡献声明要与引言gap一一对应；局限性要指向未验证假设。

- transition_to_next_cn：结束全文，同时为后续研究留下明确入口。

### most_transferable_moves_cn

1. 问题定义+现象示例两步法把抽象问题变成可研究对象

2. 文献分类表+空白格定位贡献

3. 从数据生成过程导出目标函数后再设计模型

4. 用受控变体把性能优势归因到设计属性

5. 用理论命题保护方法非一次性

6. 用经济与公平分析把算法评价升级为多利益相关者价值

### resource_intensive_or_nonstandard_parts_cn

1. 真实大型商场细粒度访客追踪数据

2. 楼层平面图到空间网络和视觉角的工程实现

3. 收入模拟依赖商场财务数据与人均消费数据

4. 附录中的多项稳健性分析缺失时会影响审稿信任

5. 长期多轮审稿修改与补充实验

### what_not_to_copy_superficially_cn

1. 不能只给公式和benchmark而缺少P3M问题概念化

2. 不能用‘首次’代替文献定位和空白格论证

3. 不能把模拟收入当作现场实验证据

4. 不能忽略正反馈、最短路径等假设而把结果过度泛化

5. 不能在没有消融的情况下声称组件贡献

- single_best_description_of_the_routine_cn：把实体场景中的一个‘偏差机制’概念化为可数学化的去偏目标，再用空间与行为数据构造可操作因子，最后通过benchmark、消融和利益相关者价值分析把算法成果包装为IS设计知识。

## 分析边界

正文OCR提供了完整主体结构和图表位置，但Online Appendices A–O只有引用标记，部分推导细节、稳健性检验、购物模式分析和系统实现细节无法从正文直接核实；句子级位置使用章节与段落标识而非出版社页码；收入与公平性部分依赖作者对图的文字描述，个别图表数值无法逐点复核。
