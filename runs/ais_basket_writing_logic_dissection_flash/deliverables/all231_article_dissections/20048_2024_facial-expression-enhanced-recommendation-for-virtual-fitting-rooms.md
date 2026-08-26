# Facial expression-enhanced recommendation for virtual fitting rooms

- 作者：Ying Xue; Jianshan Sun; Yezheng Liu; Xin Li; Kun Yuan
- 年份 / 期刊：2024 / Decision Support Systems
- DOI：10.1016/j.dss.2023.114082
- 源文件：20048_2024_facial-expression-enhanced-recommendation-for-virtual-fitting-rooms.md
- 论文主类型：build_evaluate_design_science
- 主导写作弧线：performance_gap_artifact_benchmark_generalize
- 置信度：0.74

## 文章级论证概况

- 核心问题：在虚拟试衣间/AR试妆场景中，能否以及如何利用用户与商品交互时产生的细粒度行为，尤其是面部表情，来改进个性化产品推荐？

- 制品与设计：FEERS：基于加权矩阵分解的推荐系统。设计上：用户正面表情视为强正向反馈（置信度1），负面表情视为负反馈（置信度0），中性表情根据交互行为数和驻留时间计算置信度；未点击商品则通过与用户已识别负面商品标题的文本相似度进行负反馈采样；再用ALS学习用户和商品隐向量，输出Top-K推荐。

- 客观结果：在81名女性学生用户的JD虚拟试妆实验中，FEERS的Precision=0.803、MAP=0.756，高于Popularity、AMAN、Average、BERS、DTERS等5个基准；Mann-Whitney U检验显示与各基准差异显著；并在不同用户类型和交互量分组中保持优势，在流行度和多样性方面也较好。

- 核心贡献：提出面向VFR场景的个性化推荐方法FEERS，把面部表情作为新的显式反馈，并结合交互行为、驻留时间、商品标题相似度构造加权矩阵分解模型；通过用户实验证明该方法优于使用传统行为信息的推荐方法，支持AR增强电子商务的价值。

- 整篇论证链：作者先说明AR/VFR已进入零售但现有推荐方法未利用其丰富行为信息，形成差距；随后以JD.com AR试妆为具体场景，把多源交互信号（点击、行为数、驻留时间、面部表情、商品标题）分别转化为推荐模型中的置信度与负采样权重；通过逐步加入信号构造FEERS并设计5个由弱到强的baseline；再用真实用户实验采集行为数据和用户自选商品作为金标准，比较Precision/MAP；不同用户类型、交互量、流行度/多样性和案例进一步支撑结论，最后回到VFR个性化推荐缺口，主张方法贡献和电商决策支持价值。

## 类型与写作弧线判定

- 论文主类型判定：论文从VFR推荐需求出发，设计并实现了一个推荐制品FEERS，通过用户实验与多组baseline进行评价，最后给出面向沉浸式购物环境的设计和实践启示，符合‘需求—构建—评价—设计知识’的设计科学套路，而非纯计算公开数据benchmark。

- 主导写作弧线判定：写作从‘现有推荐方法未利用VFR丰富行为’的性能/功能缺口出发，构建FEERS，用递增信息的baseline证明改进，并在结论/启示中一般化为AR增强电子商务支持。

## 研究开展程序

- study_or_phase_count：7

- 研究阶段总序列：阶段1界定VFR推荐问题与候选行为信号；阶段2把表情/行为/驻留时间转成正反馈置信度；阶段3用标题相似度处理负反馈；阶段4用加权矩阵分解和ALS生成推荐；阶段5设计用户实验采集真实交互数据和用户自选金标准；阶段6通过渐进baseline比较确认总体效果；阶段7通过用户类型、交互量、流行度/多样性和案例检验稳健性与边界。

### studies_or_phases

#### 1. 研究背景与需求界定

- order：1

- name_cn：研究背景与需求界定

- question_cn：VFR中用户与产品的多模态交互数据能否支撑偏好预测与个性化推荐？

- inputs_and_setting_cn：文献综述与JD.com AR试妆功能界面（图1、图4）。

- designed_or_compared_object_cn：定义候选信号：点击试装、拍照、进详情页、加购、驻留时间、面部表情、商品标题。

- baseline_control_or_counterfactual_cn：传统电商仅文本/图片信息，以及现有VFR仅做信息展示。

##### objective_metrics

（空）

- analysis_method_cn：文献梳理与系统使用场景描述。

- main_result_cn：VFR能够产生细粒度行为轨迹和表情信号，但现有推荐方法未充分利用。

- argumentative_role_cn：建立研究合法性和数据价值主张。

- remaining_uncertainty_cn：这些信号如何操作化为可计算推荐模型尚不清楚。

- link_to_next_phase_cn：引出FEERS的置信度设置与负反馈采样设计。

##### evidence_pointers

1. Introduction P2-P4

2. Section 3

3. Fig. 1

4. Fig. 4

#### 2. 正反馈置信度设置策略设计

- order：2

- name_cn：正反馈置信度设置策略设计

- question_cn：如何根据面部表情、行为数和驻留时间为已交互商品设置置信度？

- inputs_and_setting_cn：FAN表情识别结果、b_ui行为数、t_ui驻留时间。

- designed_or_compared_object_cn：r_ui与c_ui；正面表情c=1，负面c=0，中性按c=t'[0.5+α(b-1)]。

- baseline_control_or_counterfactual_cn：点击即喜欢/全部缺失为负（AMAN/AMAU）的简单假设。

##### objective_metrics

（空）

- analysis_method_cn：基于文献和启发式推导的置信度规则（公式1-3）。

- main_result_cn：形成基于表情三分类的置信度公式：正/负/中性。

- argumentative_role_cn：把“表情表达偏好”的领域知识转化为算法部件。

- remaining_uncertainty_cn：未点击商品仍无法处理，且置信度规则尚未实证检验。

- link_to_next_phase_cn：需要负反馈采样策略处理未点击记录。

##### evidence_pointers

1. Section 4.2.2

2. Equations (1)-(3)

3. Fig. 2

#### 3. 负反馈采样策略设计

- order：3

- name_cn：负反馈采样策略设计

- question_cn：如何为未点击商品分配负反馈置信度？

- inputs_and_setting_cn：用户由表情识别出的已知负例商品标题，以及所有未交互商品标题。

- designed_or_compared_object_cn：负反馈置信度c_ui = 平均TF-IDF余弦标题相似度。

- baseline_control_or_counterfactual_cn：AMAN全缺失为负和Average均匀采样。

##### objective_metrics

（空）

- analysis_method_cn：文本相似度计算与负例传播。

- main_result_cn：得到总体置信度公式（5），使未点击商品拥有与用户已知负例相似的置信度。

- argumentative_role_cn：解决交互矩阵缺失值问题，并为后续消融比较提供设计差异。

- remaining_uncertainty_cn：标题相似度是否有效提升推荐尚未验证。

- link_to_next_phase_cn：需要学习算法将置信度矩阵转化为推荐列表。

##### evidence_pointers

1. Section 4.2.3

2. Equations (4)-(5)

#### 4. 模型训练与推荐生成

- order：4

- name_cn：模型训练与推荐生成

- question_cn：如何基于置信度矩阵学习用户/商品隐向量并生成Top-K推荐？

- inputs_and_setting_cn：置信度矩阵C、交互矩阵R、正则参数λ、隐因子维度k。

- designed_or_compared_object_cn：加权矩阵分解目标函数与ALS交替最小二乘求解。

- baseline_control_or_counterfactual_cn：不适用，本阶段是模型实现。

##### objective_metrics

（空）

- analysis_method_cn：ALS隐因子分解，Algorithm 1。

- main_result_cn：模型可求出X和Y，按内积预测r_ui并排序得到Top-K推荐。

- argumentative_role_cn：把置信度设计转化为可计算推荐流程。

- remaining_uncertainty_cn：整体算法在真实用户偏好上的性能未知。

- link_to_next_phase_cn：需要用户实验采集数据并设置基准对比。

##### evidence_pointers

1. Section 4.3

2. Algorithm 1

3. Equations (6)-(8)

#### 5. 用户实验与金标准采集

- order：5

- name_cn：用户实验与金标准采集

- question_cn：如何获得用户在VFR中的真实交互数据和用户真正偏好的商品？

- inputs_and_setting_cn：82名付费女性学生，JD VFR平台，自带手机，固定教室和时间，屏幕录制。

- designed_or_compared_object_cn：实验流程：问卷、自由试妆、录屏、按商品切分交互、邮件反馈推荐列表。

- baseline_control_or_counterfactual_cn：无算法操控，只采集自然行为作为后续统一评测数据。

##### objective_metrics

1. 交互行为数

2. 驻留时间

3. 表情类别

4. 用户自选商品

- analysis_method_cn：录屏人工分割与标注，形成user-product-interaction数据。

- main_result_cn：81名有效用户，交互372个商品，总记录2816条，平均每个用户约35个商品，平均驻留3.5秒。

- argumentative_role_cn：为后续评测提供唯一数据来源和真实偏好金标准。

- remaining_uncertainty_cn：数据规模小、样本单一，可能影响泛化。

- link_to_next_phase_cn：提供数据输入给FEERS和baseline进行对比评价。

##### evidence_pointers

1. Section 5.1

2. Fig. 5

3. Fig. 6

4. Section 5.1.3

#### 6. 总体性能与渐进式基准比较

- order：6

- name_cn：总体性能与渐进式基准比较

- question_cn：FEERS是否优于传统行为信息推荐，并且每个新增信号是否有效？

- inputs_and_setting_cn：用户实验数据、FEERS、Popularity、AMAN、Average、BERS、DTERS。

- designed_or_compared_object_cn：不同算法生成的推荐列表；各取Top-2去重后形成混合列表。

- baseline_control_or_counterfactual_cn：Popularity为无个性化基准；AMAN/Average为传统隐反馈基准；BERS加入行为数；DTERS再加入驻留时间；FEERS再加入表情和标题相似度。

##### objective_metrics

1. Precision

2. MAP

- analysis_method_cn：用户反馈金标准对照，描述性比较。

- main_result_cn：FEERS Precision=0.803、MAP=0.756，均最高；DTERS和BERS其次；AMAN和Average最差。

- argumentative_role_cn：核心性能证据，展示整体方法优于传统方法，并隔离各信息源贡献。

- remaining_uncertainty_cn：未证明在所有用户群体和数据量下都稳定。

- link_to_next_phase_cn：需要分组稳健性分析和统计检验。

##### evidence_pointers

1. Section 5.2

2. Section 6.1

3. Table 3

#### 7. 稳健性、边界与案例检验

- order：7

- name_cn：稳健性、边界与案例检验

- question_cn：FEERS的优势在不同用户类型、交互量、流行度/多样性以及具体案例中是否仍然成立？

- inputs_and_setting_cn：问卷分组信息、交互量分组信息、推荐列表流行度/多样性、第3位用户案例。

- designed_or_compared_object_cn：不同用户组下的Precision/MAP，平均流行度与Hamming diversity，FEERS与DTERS的推荐列表对比。

- baseline_control_or_counterfactual_cn：同类baseline在各分组下的表现。

##### objective_metrics

1. 分组Precision

2. 分组MAP

3. 平均商品流行度

4. Hamming diversity

5. 用户反馈命中

- analysis_method_cn：分组统计、Mann-Whitney U检验、Hamming距离、个案分析。

- main_result_cn：FEERS在不同用户类型和交互量分组中基本最优；流行度最低0.072、多样性0.628仅次于DTERS；案例显示FEERS推荐与用户真实选择重合。

- argumentative_role_cn：把总体性能结果上升为稳健的设计知识，并回应精度之外的质量问题。

- remaining_uncertainty_cn：统计检验基于小样本和短推荐列表；仍缺乏真实线上长期购买行为验证。

- link_to_next_phase_cn：以稳健性结果为结论和未来研究提供依据。

##### evidence_pointers

1. Section 6.2

2. Fig. 7-9

3. Table 4

4. Section 6.3

5. Table 5

6. Section 6.4

7. Table 6

## 各部分修辞架构

### abstract_moves

1. CONTEXT

2. PHENOMENON

3. RQ_OR_OBJECTIVE

4. DESIGN_FEATURE

5. STUDY_OVERVIEW

6. RESULT

7. CONTRIBUTION

### introduction_moves

1. CONTEXT

2. PHENOMENON

3. PRIOR_KNOWLEDGE

4. LIMITATION

5. GAP

6. WHY_GAP_MATTERS

7. RQ_OR_OBJECTIVE

8. DESIGN_FEATURE

9. CONTRIBUTION

### theory_and_knowledge_moves

1. PRIOR_KNOWLEDGE

2. MECHANISM

3. THEORY_PROPOSITION

4. LIMITATION

5. GAP

6. REQUIREMENT

### artifact_design_moves

1. REQUIREMENT

2. DESIGN_FEATURE

3. MECHANISM

4. THEORY_PROPOSITION

5. METHOD_JUSTIFICATION

### evaluation_moves

1. STUDY_OVERVIEW

2. METHOD_JUSTIFICATION

3. BENCHMARK_OR_CONTRAST

4. RESULT

5. ROBUSTNESS_OR_BOUNDARY_TEST

6. TRANSITION

### discussion_and_contribution_moves

1. GAP

2. CONTRIBUTION

3. PRACTICAL_STAKES

4. BOUNDARY_CONDITION

5. LIMITATION_AND_FUTURE

## 理论/知识到设计的翻译

### 知识/理论基础

1. 面部表情/情绪与用户偏好关系：表情是用户对商品的直观反应，可表达偏好。

2. 隐反馈推荐文献：矩阵分解、AMAN/AMAU、按驻留时间设置置信度、负反馈采样。

3. 用户行为/驻留时间文献：驻留时间是参与和满意度的指标。

4. 商品标题文本信息：品牌、类型、适用人群等特征可辅助购买决策。

5. VFR/AR零售文献：沉浸式环境产生丰富行为轨迹，个性化在虚拟购物环境中重要。

- 理论—设计耦合：partial

- 耦合判定理由：文章没有建立并检验正式理论命题；它主要用以往经验知识（表情表达偏好、驻留时间表征参与、点击不等于喜欢）作为启发式，把行为信号翻译为置信度与负采样权重。这些知识影响了变量选择和算法部件，但模型形态（矩阵分解、ALS、标题相似度、α=0.4）来自推荐工程和文献惯例，不是严格理论推导。

- 理论到设计翻译链：表情反映偏好 → 情绪三分类决定基础偏好方向；点击≠喜欢/未点击≠不喜欢 → 使用行为数和驻留时间设置正向置信度；驻留时间越长偏好越强 → 归一化驻留时间进入置信度；标题包含商品特征且用户负面商品可传播 → 用TF-IDF余弦相似度设置负反馈置信度；所有信号最终折算为置信度矩阵 → 输入加权矩阵分解+ALS，输出Top-K推荐。

### mapping_table

#### 1. 1

- theory_or_knowledge_claim_cn：面部表情能表达用户偏好。

- mechanism_cn：积极表情表示真实喜欢，消极表情表示不喜欢，中性表情无法直接判断。

- design_requirement_cn：表情类别必须进入交互矩阵的置信度设置。

- artifact_choice_cn：正面表情→r=1,c=1；负面表情→r=0,c=0；中性表情→结合行为数和驻留时间计算。

- evaluated_contrast_cn：FEERS vs DTERS/BERS：后两者不使用表情信号。

- objective_result_cn：FEERS Precision=0.803、MAP=0.756，显著高于不使用表情的基准。

##### evidence_pointers

1. Section 4.2.2(2) equations (1)-(3)

2. Table 3

3. Table 4

#### 2. 2

- theory_or_knowledge_claim_cn：点击不等于喜欢，未点击不等于不喜欢（AMAN不准确）。

- mechanism_cn：用户可能点击查看后不喜欢；未点击可能因为没看到商品。

- design_requirement_cn：不能只按是否点击设置0/1，需要对正反馈置信度加权。

- artifact_choice_cn：用行为数b和驻留时间t构造置信度c=t'[0.5+α(b-1)]。

- evaluated_contrast_cn：BERS/DTERS逐步加入行为数和驻留时间，优于AMAN/Average。

- objective_result_cn：BERS=0.698/0.664，DTERS=0.704/0.630，均高于AMAN/Average的0.636/0.580。

##### evidence_pointers

1. Section 4.2.2(2) equations (1)-(3)

2. Table 3

#### 3. 3

- theory_or_knowledge_claim_cn：驻留时间是用户参与和满意度的指标。

- mechanism_cn：在商品上停留越久，偏好概率越高。

- design_requirement_cn：置信度应与驻留时间正相关，并进行用户级归一化。

- artifact_choice_cn：采用log空间z-score归一化的驻留时间乘到基础置信度。

- evaluated_contrast_cn：DTERS使用驻留时间，BERS不使用。

- objective_result_cn：DTERS Precision=0.704，高于BERS Precision=0.698。

##### evidence_pointers

1. Section 4.2.2(2) formula (2)

2. Table 3

#### 4. 4

- theory_or_knowledge_claim_cn：商品标题包含品牌、类型、适用人群等特征信息。

- mechanism_cn：用户不喜欢的商品可以通过标题文本相似度传递到未交互商品。

- design_requirement_cn：未点击商品不能一律视为负例或统一置信度，应按与已知负例的相似度分配负反馈权重。

- artifact_choice_cn：用TF-IDF+cosine相似度计算未交互商品与用户表情识别负例标题的平均相似度，作为负样本置信度。

- evaluated_contrast_cn：FEERS同时使用表情和标题相似度，优于仅用行为的BERS/DTERS。

- objective_result_cn：FEERS Precision/MAP均最高。

##### evidence_pointers

1. Section 4.2.3 formula (4)-(5)

2. Table 3

#### 5. 5

- theory_or_knowledge_claim_cn：虚拟环境产生细粒度行为轨迹，可用于推荐。

- mechanism_cn：VFR中点击试穿、拍照、进详情、加购、表情、驻留时间构成多源反馈。

- design_requirement_cn：推荐算法需把多源交互汇总为统一偏好矩阵。

- artifact_choice_cn：将所有信号折算成置信度矩阵后，用带权矩阵分解+ALS学习隐向量并生成Top-K。

- evaluated_contrast_cn：用户实验把推荐列表反馈给用户形成金标准，用Precision/MAP评估。

- objective_result_cn：FEERS在所有总体指标和多数分组上均最优。

##### evidence_pointers

1. Section 4.2.1 framework

2. Section 4.3

3. Section 5.1

4. Tables 3-5

## 评价逻辑

### evaluation_modes

1. 用户实验室实验

2. 多baseline对比

3. 渐进式信息源消融对比（BERS→DTERS→FEERS）

4. Mann-Whitney U统计检验

5. 用户类型/交互量分组稳健性分析

6. 推荐流行度与多样性评估

7. 案例研究

- why_these_evaluations_cn：因为没有公开VFR推荐数据集，作者需要自建真实用户实验来提供行为数据和用户偏好金标准；为证明FEERS不是简单换算法，设置从无个性化到逐步加入行为、驻留时间、表情/负采样的baseline；为保护结论不过度依赖单一总体指标，增加分组、统计检验、beyond-accuracy和个案分析。

- benchmark_and_contrast_chain_cn：Popularity（无个性化）→ AMAN/Average（传统点击隐反馈）→ BERS（加交互行为数）→ DTERS（加驻留时间）→ FEERS（加面部表情和标题相似度负采样）。每个新增信号都对应一个可比较的算法变体，使Table 3的指标差异可被理解为新增信息源的贡献。

### claim_evidence_ledger

1. 技术主张：FEERS在当前VFR数据集上Precision/MAP最高。证据：Table 3、Table 4。

2. 制品主张：表情、行为、驻留时间、标题相似度等部件带来提升。证据：BERS/DTERS/FEERS递进对比。

3. 机制主张：表情直接表达偏好、行为数/驻留时间表征偏好强度、标题相似度传播负偏好。证据：公式推导与对比结果，但没有过程性心理或行为机制检验。

4. 边界主张：不同用户类型和交互量下仍有效。证据：Fig.7-9分组结果。

5. 设计知识：VFR推荐可把多模态AR交互转成置信度矩阵。证据：FEERS整体设计及其成功评价。

6. 理论贡献：扩展VFR/AR增强电子商务的推荐研究，未提出新形式理论。证据：结论论述。

- internal_validity_strategy_cn：固定实验时间和教室灯光、独立空间避免相互影响；屏幕录制完整保留操作和面部影像；用户自选商品作为金标准；用Mann-Whitney U检验显著性；用渐进baseline隔离信息源。

- external_validity_strategy_cn：使用真实JD VFR平台、真实商品、用户自带手机和自由操作，接近实际使用；但样本限定为女性学生、化妆品类目，外部推广需要更广泛样本。

- what_is_not_actually_tested_cn：没有检验FAN表情识别错误对推荐结果的影响；没有与深度学习方法或真实线上推荐系统对比；没有检验AMAU、user-oriented/item-oriented采样；没有做不同α/超参数敏感性；结论的‘统计显著’基于每个用户推荐列表很短且只有一次选择性反馈；男性、服装类目和长时间真实购买行为未检验。

## 贡献闭环

- technical_claim_cn：FEERS在当前VFR数据集上的Precision=0.803、MAP=0.756，显著高于5个baseline。

- artifact_claim_cn：表情三分类、行为数/驻留时间置信度、标题相似度负采样这些可识别设计部件共同导致改进；DTERS/BERS逐步对比支持这一点。

- mechanism_claim_cn：面部表情直接反映用户偏好，行为数和驻留时间反映偏好强度，标题相似度把已知负偏好传播到未交互商品。

- boundary_claim_cn：在不同教育水平、VFR经验、产品熟悉度和交互数据量分组中，FEERS基本保持最优；在流行度与多样性方面也较好。

- reusable_design_knowledge_cn：在VFR类沉浸式购物环境中，推荐系统可把AR交互中的表情、行为数、驻留时间和商品文本相似度转化为置信度矩阵，从而利用隐性/显式多模态反馈。

- theoretical_contribution_cn：不是提出新理论，而是把AR/VFR产生的细粒度交互和表情作为推荐信息源引入偏好建模，扩展了VFR推荐和AR增强电商的相关研究。

- how_discussion_closes_intro_gap_cn：引言指出‘现有推荐方法未充分利用VFR行为信息’，结论重新声明‘VFR已广泛使用但缺乏适配推荐方法’，然后以FEERS的构建和实验结果表明该缺口被补齐，并引申出对商家决策支持和管理意义。

- overclaim_or_unsupported_leaps_cn：作者称面部表情是‘新的显式反馈’，但实际只是把表情映射为0/1/中间置信度，没有直接验证表情标签与真实偏好的因果关系；Mann-Whitney U检验基于很小样本和很短的推荐列表；结论中‘显著优于’更多是统计意义而非实际购买转化意义；DTERS的MAP低于BERS但作者仍说DTERS排第二，解释并不完全一致。

## 句级写作动作图谱

### 1. P1 S1

- order：1

- section：Abstract

- locator：P1 S1

- move_code：CONTEXT

- paraphrase_cn：AR技术发展使虚拟试衣间被视为提升电商体验的增强手段。

- rhetorical_function_cn：开篇将研究置于AR零售与电商增强的背景。

- depends_on_cn：无。

- sets_up_cn：引出VFR作为研究对象。

- evidence_pointer：Abstract P1

### 2. P1 S2-S3

- order：2

- section：Abstract

- locator：P1 S2-S3

- move_code：PHENOMENON

- paraphrase_cn：VFR让用户更直观看到产品，也使商家获得更多偏好信息，可用来增强推荐。

- rhetorical_function_cn：点出VFR同时具有体验与数据价值。

- depends_on_cn：承接AR/VFR背景。

- sets_up_cn：为使用推荐算法利用VFR信息做铺垫。

- evidence_pointer：Abstract P1

### 3. P2 S1

- order：3

- section：Abstract

- locator：P2 S1

- move_code：DESIGN_FEATURE

- paraphrase_cn：提出基于置信度设置、负反馈采样和矩阵分解的推荐算法。

- rhetorical_function_cn：概括制品FEERS的三大技术部件。

- depends_on_cn：前面建立VFR数据价值。

- sets_up_cn：后续实验以该算法为核心。

- evidence_pointer：Abstract P2

### 4. P2 S2-S3

- order：4

- section：Abstract

- locator：P2 S2-S3

- move_code：RESULT

- paraphrase_cn：81名被试实验显示所提方法优于传统行为信息方法，支持AR增强电商价值。

- rhetorical_function_cn：预告主要结果与贡献。

- depends_on_cn：算法设计已完成。

- sets_up_cn：让读者期待实验证据。

- evidence_pointer：Abstract P2

### 5. P1 S1

- order：5

- section：Introduction

- locator：P1 S1

- move_code：CONTEXT

- paraphrase_cn：AR把虚拟信息与现实结合，已在导航、艺术、社交和营销中应用。

- rhetorical_function_cn：从技术背景进入主题。

- depends_on_cn：无。

- sets_up_cn：定义VFR是AR在商业中的具体应用。

- evidence_pointer：Introduction P1

### 6. P2 S1-S2

- order：6

- section：Introduction

- locator：P2 S1-S2

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：传统上用户通过文本和图片了解商品；VFR能让用户看到商品在真实场景中的三维效果。

- rhetorical_function_cn：对比旧信息获取方式与VFR优势。

- depends_on_cn：AR/VFR定义。

- sets_up_cn：解释VFR为何产生更丰富交互。

- evidence_pointer：Introduction P2

### 7. P3 S1-S2

- order：7

- section：Introduction

- locator：P3 S1-S2

- move_code：PHENOMENON

- paraphrase_cn：VFR还留下详细行为轨迹，点击、调整等行为结合眼动和表情能刻画消费者注意和偏好。

- rhetorical_function_cn：提出VFR可生成细粒度行为数据这一现象。

- depends_on_cn：前面VFR交互体验描述。

- sets_up_cn：指出这些数据可增强推荐系统。

- evidence_pointer：Introduction P3

### 8. P3 S3

- order：8

- section：Introduction

- locator：P3 S3

- move_code：LIMITATION

- paraphrase_cn：然而现有推荐方法没有充分捕获和利用这类AR相关信息。

- rhetorical_function_cn：建立问题缺口。

- depends_on_cn：描述VFR数据丰富性之后。

- sets_up_cn：引出全文要解决的问题。

- evidence_pointer：Introduction P3

### 9. P4 S1-S2

- order：9

- section：Introduction

- locator：P4 S1-S2

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：VFR在电商中虽快速发展，但现有应用主要是展示商品，研究多关注其对体验和决策的影响。

- rhetorical_function_cn：总结VFR研究现状。

- depends_on_cn：前面已说明VFR价值。

- sets_up_cn：为“研究空白”提供文献背景。

- evidence_pointer：Introduction P4

### 10. P4 S3

- order：10

- section：Introduction

- locator：P4 S3

- move_code：GAP

- paraphrase_cn：很少有研究把VFR交互整合进推荐算法。

- rhetorical_function_cn：明确具体研究空白。

- depends_on_cn：相关研究只关注体验与决策而非推荐。

- sets_up_cn：说明推荐算法研究缺失。

- evidence_pointer：Introduction P4

### 11. P4 S4

- order：11

- section：Introduction

- locator：P4 S4

- move_code：WHY_GAP_MATTERS

- paraphrase_cn：用户身体特征可支撑更好的VFR推荐，这被视为高影响力方向。

- rhetorical_function_cn：说明该缺口值得研究。

- depends_on_cn：缺口已明确。

- sets_up_cn：支撑本文研究必要性。

- evidence_pointer：Introduction P4

### 12. P5 S1

- order：12

- section：Introduction

- locator：P5 S1

- move_code：RQ_OR_OBJECTIVE

- paraphrase_cn：VFR中的交互是否有助于偏好预测与推荐，以及如何使用这些行为进行推荐，是需要研究的问题。

- rhetorical_function_cn：正式提出研究问题。

- depends_on_cn：文献缺口和高影响力判断。

- sets_up_cn：预告本文方法方案。

- evidence_pointer：Introduction P5

### 13. P5 S2-S3

- order：13

- section：Introduction

- locator：P5 S2-S3

- move_code：DESIGN_FEATURE

- paraphrase_cn：本文提出基于矩阵分解的个性化推荐方法，并认为用户与商品互动时的表情信息能帮助预测偏好。

- rhetorical_function_cn：给出解决方案摘要。

- depends_on_cn：研究问题。

- sets_up_cn：说明方法核心：交互行为+表情+矩阵分解。

- evidence_pointer：Introduction P5

### 14. P6 S1-S3

- order：14

- section：Introduction

- locator：P6 S1-S3

- move_code：CONTRIBUTION

- paraphrase_cn：贡献有三：VFR多交互行为推荐方法、用面部表情作为新的显式反馈、数据收集与用户实验验证。

- rhetorical_function_cn：以贡献列表收束引言。

- depends_on_cn：问题与方法概述。

- sets_up_cn：后续章节按此展开。

- evidence_pointer：Introduction P6

### 15. 2.1 P1 S1-S2

- order：15

- section：Related work

- locator：2.1 P1 S1-S2

- move_code：CONTEXT

- paraphrase_cn：VR和AR技术越来越多用于实体与线上零售，提供虚拟购物环境以改善体验。

- rhetorical_function_cn：为相关文献分类开篇。

- depends_on_cn：引言中的AR/VFR背景。

- sets_up_cn：综述虚拟环境对消费行为的影响。

- evidence_pointer：Section 2.1 P1

### 16. 2.1 P3 S1

- order：16

- section：Related work

- locator：2.1 P3 S1

- move_code：MECHANISM

- paraphrase_cn：AR对消费者体验和情绪感知的影响改变购物态度与满意度，进而影响购买意愿。

- rhetorical_function_cn：概括虚拟环境影响购买决策的机制。

- depends_on_cn：沉浸感与临场感研究。

- sets_up_cn：解释为什么个性化推荐与用户状态密切相关。

- evidence_pointer：Section 2.1 P3

### 17. 2.1 P4 S1-S2

- order：17

- section：Related work

- locator：2.1 P4 S1-S2

- move_code：WHY_GAP_MATTERS

- paraphrase_cn：虚拟购物体验受性别、参与度和经验等个体差异影响，因此个性化很有必要。

- rhetorical_function_cn：说明虚拟环境中的个性化需求。

- depends_on_cn：前面综述AR体验与购买意愿关系。

- sets_up_cn：为推荐方法研究提供管理学动机。

- evidence_pointer：Section 2.1 P4

### 18. 2.2 P4 S1

- order：18

- section：Related work

- locator：2.2 P4 S1

- move_code：LIMITATION

- paraphrase_cn：大多数现有研究把虚拟环境当作数据采集和信息显示工具，没有充分考虑用户在其中的交互行为及意义，尤其是购物场景。

- rhetorical_function_cn：批判现有VFR推荐研究不足。

- depends_on_cn：对现有虚拟环境推荐研究的回顾。

- sets_up_cn：形成本文研究空间。

- evidence_pointer：Section 2.2 P4

### 19. 2.2 P5 S1-S3

- order：19

- section：Related work

- locator：2.2 P5 S1-S3

- move_code：DESIGN_FEATURE

- paraphrase_cn：已有研究显示表情可作为隐反馈提升搜索/视频推荐，本文利用表情识别偏好并与其他交互行为结合进行商品推荐。

- rhetorical_function_cn：指出表情信号在推荐中的可行性。

- depends_on_cn：虚拟环境推荐文献缺口。

- sets_up_cn：为FEERS的表情模块提供依据。

- evidence_pointer：Section 2.2 P5

### 20. P2 S1-S2

- order：20

- section：Research context

- locator：P2 S1-S2

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：研究基于京东AR试妆功能，该平台允许用户在虚拟试衣间试用不同美妆产品。

- rhetorical_function_cn：说明研究场景来自真实商业平台。

- depends_on_cn：VFR推荐问题界定。

- sets_up_cn：为后续用户实验和界面行为定义提供具体环境。

- evidence_pointer：Section 3 P2

### 21. P1 S1

- order：21

- section：Preliminaries

- locator：P1 S1

- move_code：OTHER

- paraphrase_cn：给出用户-商品交互矩阵、行为数、驻留时间、表情、置信度、标题相似度等符号。

- rhetorical_function_cn：统一模型记法。

- depends_on_cn：VFR场景描述。

- sets_up_cn：供4.2节公式使用。

- evidence_pointer：Section 4.1, Table 1

### 22. 4.2.1 P2 S1-S4

- order：22

- section：Recommendation model

- locator：4.2.1 P2 S1-S4

- move_code：LIMITATION

- paraphrase_cn：最常用的r_ui是按是否点击，AMAN把所有缺失当负例、AMAU当未知，但点击不等于喜欢，未点击也不一定不喜欢，因此这两种策略不准确。

- rhetorical_function_cn：批评简单点击反馈假设。

- depends_on_cn：交互矩阵概念。

- sets_up_cn：为置信度加权和负采样提供理由。

- evidence_pointer：Section 4.2.1 P2

### 23. 4.2.1 P3 S1-S4

- order：23

- section：Recommendation model

- locator：4.2.1 P3 S1-S4

- move_code：REQUIREMENT

- paraphrase_cn：不同行为对预测效果不同；VFR能收集表情，表情包含可直接指示偏好的信息，因此需要把表情和其他行为用于完成交互矩阵。

- rhetorical_function_cn：从文献知识转向设计需求。

- depends_on_cn：点击反馈局限。

- sets_up_cn：引出置信度设置与表情识别。

- evidence_pointer：Section 4.2.1 P3

### 24. 4.2.2(1) P1 S1-S2

- order：24

- section：Recommendation model

- locator：4.2.2(1) P1 S1-S2

- move_code：THEORY_PROPOSITION

- paraphrase_cn：面部情绪是最直观的反应，能很好表达用户对商品的好恶，并且可在VFR中直接观测。

- rhetorical_function_cn：提出表情与偏好关系的知识命题。

- depends_on_cn：VFR行为信号分析。

- sets_up_cn：说明为何用表情作为反馈。

- evidence_pointer：Section 4.2.2(1)

### 25. 4.2.2(1) P2 S1-S3

- order：25

- section：Recommendation model

- locator：4.2.2(1) P2 S1-S3

- move_code：DESIGN_FEATURE

- paraphrase_cn：采用FAN表情识别模型，用深度CNN和帧注意力从视频中识别每帧情绪及概率，最终得到用户试妆表情。

- rhetorical_function_cn：选择具体表情识别工具。

- depends_on_cn：表情作为偏好的知识命题。

- sets_up_cn：输出七类情绪并映射为正/中/负。

- evidence_pointer：Section 4.2.2(1)

### 26. 4.2.2(1) P4 S1

- order：26

- section：Recommendation model

- locator：4.2.2(1) P4 S1

- move_code：DESIGN_FEATURE

- paraphrase_cn：将七种表情输出编码为：happy→positive，neutral→neutral，其余→negative。

- rhetorical_function_cn：定义表情类别到偏好的翻译。

- depends_on_cn：FAN输出。

- sets_up_cn：支持后续置信度规则。

- evidence_pointer：Section 4.2.2(1)

### 27. 4.2.2(2) P1-P2

- order：27

- section：Recommendation model

- locator：4.2.2(2) P1-P2

- move_code：DESIGN_FEATURE

- paraphrase_cn：积极表情时r为正且c=1；消极表情时r为负且c=0；中性表情需进一步设置置信度。

- rhetorical_function_cn：把表情类别映射为初始置信度。

- depends_on_cn：表情编码规则。

- sets_up_cn：中性情形需要行为数和驻留时间补充。

- evidence_pointer：Section 4.2.2(2)

### 28. 4.2.2(2) P3 S1-S4

- order：28

- section：Recommendation model

- locator：4.2.2(2) P3 S1-S4

- move_code：MECHANISM

- paraphrase_cn：用户可进详情、加购、拍照等，交互越多说明喜欢的可能性越大。

- rhetorical_function_cn：为行为数进入置信度提供行为机制。

- depends_on_cn：中性表情需要进一步判断。

- sets_up_cn：引出公式(1)。

- evidence_pointer：Section 4.2.2(2)

### 29. 4.2.2(2) P3 S5-S7

- order：29

- section：Recommendation model

- locator：4.2.2(2) P3 S5-S7

- move_code：DESIGN_FEATURE

- paraphrase_cn：设置c=0.5+α(b-1)，其中0.5表示点击后有50%喜欢可能，α=0.4参考隐反馈文献。

- rhetorical_function_cn：给出行为数置信度公式。

- depends_on_cn：行为数越多偏好越强的机制。

- sets_up_cn：后面加入驻留时间形成完整公式。

- evidence_pointer：Section 4.2.2(2), Equation (1)

### 30. 4.2.2(2) P4 S1-S3

- order：30

- section：Recommendation model

- locator：4.2.2(2) P4 S1-S3

- move_code：DESIGN_FEATURE

- paraphrase_cn：驻留时间也是偏好指标，因此用归一化驻留时间乘以行为数置信度得到c=t'[0.5+α(b-1)]。

- rhetorical_function_cn：把驻留时间纳入置信度。

- depends_on_cn：驻留时间反映参与/满意度的文献。

- sets_up_cn：最终形成公式(3)。

- evidence_pointer：Section 4.2.2(2), Equation (2)

### 31. 4.2.3 P1 S1-S3

- order：31

- section：Recommendation model

- locator：4.2.3 P1 S1-S3

- move_code：REQUIREMENT

- paraphrase_cn：未点击缺失值需要采样填充；商品标题包含品牌、类型、适用人群等丰富特征，可用于负反馈采样。

- rhetorical_function_cn：为负采样策略引入文本相似度。

- depends_on_cn：正反馈置信度已设计。

- sets_up_cn：定义标题相似度负采样公式。

- evidence_pointer：Section 4.2.3 P1

### 32. 4.2.3 P2 S1-S3

- order：32

- section：Recommendation model

- locator：4.2.3 P2 S1-S3

- move_code：DESIGN_FEATURE

- paraphrase_cn：用用户已由表情识别的负例商品，对未交互商品按标题平均相似度设置负反馈置信度。

- rhetorical_function_cn：给出负反馈置信度规则。

- depends_on_cn：负例可由表情找到的前提。

- sets_up_cn：形成总体置信度公式(5)。

- evidence_pointer：Section 4.2.3, Equation (4)

### 33. 4.2.3 P3 S1

- order：33

- section：Recommendation model

- locator：4.2.3 P3 S1

- move_code：DESIGN_FEATURE

- paraphrase_cn：总体置信度按四种情况组合：正表情c=1、负表情c=0、中性表情结合行为/驻留时间、未点击用标题相似度。

- rhetorical_function_cn：汇总完整置信度策略。

- depends_on_cn：正反馈和负采样设计。

- sets_up_cn：进入矩阵分解损失函数和ALS。

- evidence_pointer：Section 4.2.3, Equation (5)

### 34. 4.3 P1 S1

- order：34

- section：Recommendation model

- locator：4.3 P1 S1

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：模型用隐式反馈的ALS方法训练。

- rhetorical_function_cn：选择可求解加权矩阵分解的方法。

- depends_on_cn：置信度矩阵和损失函数。

- sets_up_cn：算法伪代码和Top-K推荐。

- evidence_pointer：Section 4.3

### 35. 5 P1 S1

- order：35

- section：Experiment

- locator：5 P1 S1

- move_code：STUDY_OVERVIEW

- paraphrase_cn：基于实验设计方法设计实验，收集数据并验证用户交互行为能否帮助个性化推荐。

- rhetorical_function_cn：预告实验目的与方法论。

- depends_on_cn：FEERS模型完成。

- sets_up_cn：进入用户实验细节。

- evidence_pointer：Section 5 P1

### 36. 5.1.1 P3 S1-S2

- order：36

- section：Experiment

- locator：5.1.1 P3 S1-S2

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：用手机屏幕录制记录从进入VFR到退出的全部操作和面部信息，之后按商品切分并手工处理成交互数据。

- rhetorical_function_cn：说明数据采集方式。

- depends_on_cn：实验场景和参与者招募。

- sets_up_cn：生成可供推荐算法使用的用户-商品-交互数据。

- evidence_pointer：Section 5.1.1

### 37. 5.1.2 P1 S1-S3

- order：37

- section：Experiment

- locator：5.1.2 P1 S1-S3

- move_code：BENCHMARK_OR_CONTRAST

- paraphrase_cn：用处理后的数据运行FEERS和各baseline，各取Top-2去重后形成推荐列表，发给用户让其选择偏好商品作为金标准。

- rhetorical_function_cn：设计推荐结果反馈与金标准流程。

- depends_on_cn：用户交互数据。

- sets_up_cn：后续Precision/MAP评价。

- evidence_pointer：Section 5.1.2

### 38. 5.1.3 P2

- order：38

- section：Experiment

- locator：5.1.3 P2

- move_code：RESULT

- paraphrase_cn：处理后数据有81名用户、372个商品、约2816条交互记录，平均每个用户交互约35个商品，平均驻留时间3.5秒。

- rhetorical_function_cn：报告实验数据规模。

- depends_on_cn：录屏标注过程。

- sets_up_cn：让读者理解数据集规模和稀疏性。

- evidence_pointer：Section 5.1.3

### 39. 5.2 P1

- order：39

- section：Experiment

- locator：5.2 P1

- move_code：BENCHMARK_OR_CONTRAST

- paraphrase_cn：设置5个baseline：Popularity、AMAN、Average、BERS、DTERS。

- rhetorical_function_cn：建立对比参照系。

- depends_on_cn：实验数据。

- sets_up_cn：通过逐步添加信息源解释FEERS优势。

- evidence_pointer：Section 5.2

### 40. 5.3 P1-P2

- order：40

- section：Experiment

- locator：5.3 P1-P2

- move_code：BENCHMARK_OR_CONTRAST

- paraphrase_cn：采用Precision和MAP两个指标，分别衡量正确预测比例和推荐排序质量。

- rhetorical_function_cn：明确评价指标。

- depends_on_cn：用户金标准反馈。

- sets_up_cn：呈现结果表。

- evidence_pointer：Section 5.3

### 41. 6.1 P1 S1-S3

- order：41

- section：Result

- locator：6.1 P1 S1-S3

- move_code：RESULT

- paraphrase_cn：Table 3显示FEERS在Precision和MAP上都最好，显著超过前三个基准，也优于后两个加入行为/驻留时间的方法。

- rhetorical_function_cn：报告总体性能结论。

- depends_on_cn：baseline和指标设定。

- sets_up_cn：后续解释各信号贡献。

- evidence_pointer：Section 6.1, Table 3

### 42. 6.1 P2 S1-S2

- order：42

- section：Result

- locator：6.1 P2 S1-S2

- move_code：OTHER

- paraphrase_cn：AMAN和Average结果相同，作者认为是因为样本量小，均匀采样影响有限。

- rhetorical_function_cn：解释baseline之间出现相同结果的原因。

- depends_on_cn：Table 3中的相同数值。

- sets_up_cn：说明数据规模对方法比较的潜在限制。

- evidence_pointer：Section 6.1 P2

### 43. 6.2 P1 S1

- order：43

- section：Result

- locator：6.2 P1 S1

- move_code：ROBUSTNESS_OR_BOUNDARY_TEST

- paraphrase_cn：为继续验证方法有效性，进一步分析不同用户类型下的推荐表现。

- rhetorical_function_cn：引入稳健性分析。

- depends_on_cn：总体性能结果。

- sets_up_cn：下面的分组图表。

- evidence_pointer：Section 6.2 P1

### 44. 6.2 P3 S1-S2

- order：44

- section：Result

- locator：6.2 P3 S1-S2

- move_code：RESULT

- paraphrase_cn：在不同教育、VFR经验、产品熟悉度分组下，FEERS在Precision和MAP上都基本最优，说明用户熟悉度不影响方法表现。

- rhetorical_function_cn：报告分组稳健性结果。

- depends_on_cn：问卷分组数据。

- sets_up_cn：支持边界主张。

- evidence_pointer：Section 6.2, Fig. 8

### 45. 6.2 P6 S1-S3

- order：45

- section：Result

- locator：6.2 P6 S1-S3

- move_code：RESULT

- paraphrase_cn：Mann-Whitney U检验显示FEERS的Precision显著高于其他方法。

- rhetorical_function_cn：给出统计显著性证据。

- depends_on_cn：分组和总体结果。

- sets_up_cn：强化“显著优于”结论。

- evidence_pointer：Section 6.2, Table 4

### 46. 6.3 P1 S1-S2

- order：46

- section：Result

- locator：6.3 P1 S1-S2

- move_code：ROBUSTNESS_OR_BOUNDARY_TEST

- paraphrase_cn：只追求准确率可能导致多样性和信息茧房问题，因此进一步计算推荐列表的流行度和多样性。

- rhetorical_function_cn：引入beyond-accuracy评价。

- depends_on_cn：准确率结果。

- sets_up_cn：报告流行度/多样性表。

- evidence_pointer：Section 6.3 P1

### 47. 6.3 P3 S1-S2

- order：47

- section：Result

- locator：6.3 P3 S1-S2

- move_code：RESULT

- paraphrase_cn：FEERS的推荐平均流行度最低（0.072），多样性0.628仅次于DTERS；作者认为准确率提高会牺牲部分多样性，但FEERS仍保持较好的多样性。

- rhetorical_function_cn：报告beyond-accuracy结果。

- depends_on_cn：流行度与Hamming距离指标。

- sets_up_cn：说明方法不只优化准确率。

- evidence_pointer：Section 6.3, Table 5

### 48. 6.4 P3 S1-S3

- order：48

- section：Result

- locator：6.4 P3 S1-S3

- move_code：RESULT

- paraphrase_cn：以第3位用户为例，FEERS推荐的前两项是Armani口红，而DTERS前两项是其他类目；说明FEERS能利用表情捕捉偏好。

- rhetorical_function_cn：用个案展示机制解释。

- depends_on_cn：推荐列表和用户交互品牌分布。

- sets_up_cn：引导结论中的意义。

- evidence_pointer：Section 6.4, Table 6

### 49. 6.4 P4 S1-S2

- order：49

- section：Result

- locator：6.4 P4 S1-S2

- move_code：RESULT

- paraphrase_cn：用户3最终选择的5个偏好商品中，有两个正对应FEERS推荐列表前两项，案例直观展示推荐准确性和多样性。

- rhetorical_function_cn：用用户反馈金标准验证案例。

- depends_on_cn：用户返回的偏好商品列表。

- sets_up_cn：收束实验结果。

- evidence_pointer：Section 6.4 P4

### 50. P1 S1-S2

- order：50

- section：Conclusion

- locator：P1 S1-S2

- move_code：CONTRIBUTION

- paraphrase_cn：VFR已广泛用于电商但缺少适配的推荐方法，本文提出FEERS，用VFR中的交互行为尤其表情来分析预测偏好。

- rhetorical_function_cn：重新连接引言缺口并宣告贡献。

- depends_on_cn：整个模型和实验结果。

- sets_up_cn：随后说明方法如何解决隐反馈问题。

- evidence_pointer：Section 7 P1

### 51. P2 S1-S3

- order：51

- section：Conclusion

- locator：P2 S1-S3

- move_code：PRACTICAL_STAKES

- paraphrase_cn：商家可通过表情和交互行为更直接理解用户真实偏好；个性化营销降低搜索成本、辅助决策并提高收益。

- rhetorical_function_cn：强调实践意义。

- depends_on_cn：实验验证结果。

- sets_up_cn：把方法贡献转化为决策支持价值。

- evidence_pointer：Section 7 P2

### 52. P3 S1-S3

- order：52

- section：Conclusion

- locator：P3 S1-S3

- move_code：LIMITATION_AND_FUTURE

- paraphrase_cn：局限包括缺少公开数据集、数据量限制使用传统矩阵分解、未利用外部商品信息；未来将扩大数据、加入外部信息并采用深度学习方法。

- rhetorical_function_cn：提供边界条件和未来方向。

- depends_on_cn：自建数据实验。

- sets_up_cn：让贡献表达更谦逊并指出后续研究。

- evidence_pointer：Section 7 P3

## 写作技术

- gap_construction_cn：先用VFR的沉浸体验和丰富行为数据制造“数据价值”期待，再用“现有推荐方法没有充分利用”“很少研究把VFR交互纳入推荐”双重否定直接构造缺口；把缺口定性为缺少适合VFR的推荐制品，而不是理论不足。

- signposting_cn：引言末尾用三点贡献预告全文；方法部分用“firstly/此外/综上所述”组织；实验部分用“5.1用户实验设计—5.2 baselines—5.3评估指标”线性推进；结果部分用“总体—不同类型—流行度多样性—案例”逐层展开。

- transition_logic_cn：段间常用“However”“Therefore”“In this paper”等连接；从文献缺口跳到研究问题，从框架图跳到置信度公式，从模型构建跳到实验验证，从总体结果跳到稳健性分析，最后回到引言缺口。

- claim_evidence_rhythm_cn：每个核心主张都紧跟一张表/图或一个公式：贡献声明后是实验；总体最优后是Table 3；稳健性后是Fig.7-9和Table 4；beyond-accuracy后是Table 5；案例后是Table 6。总体是“主张—证据—解释”的循环。

- benchmark_narrative_cn：baseline被设计成信息源从少到多的阶梯，使FEERS的优势不仅是对某个固定基准的胜利，还被读作“越充分利用VFR信号，推荐越好”的累积证据；AMAN/Average最差则强化传统点击反馈不可靠。

- theory_return_cn：文章没有回扣形式理论，而是在最后把实验结果提升为“面部表情和交互行为可帮助偏好预测”的一般性断言，并给出商家决策支持意义；理论返回比较弱。

- contribution_positioning_cn：贡献定位为“新场景中的新方法+新反馈源+真实数据验证”，强调VFR环境适配性和表情信号的新颖性，而不是算法复杂度的前沿。

- novelty_protection_cn：通过渐进baseline说明不是简单替换矩阵分解，而是表情和多种行为信号带来的增益；通过分组、流行度/多样性和案例说明贡献不是一次性指标噪声；最后用局限和未来工作降低过度承诺风险。

## 可复用研究与写作程序

### structure_steps

#### 1. 1

- step：1

- writing_job_cn：建立AR/VFR的现实价值，描述平台和用户交互。

- research_job_cn：选定真实场景，识别VFR中有哪些可观测行为信号。

- required_evidence_cn：平台界面、操作细节、行为类型、用户数据可用性。

- transition_to_next_cn：用‘然而现有推荐方法未利用这些信息’引出缺口。

#### 2. 2

- step：2

- writing_job_cn：综述虚拟环境与推荐研究并标出缺口。

- research_job_cn：定位现有研究只关注体验而不关注推荐算法的证据。

- required_evidence_cn：至少几篇代表性文献和明确的缺口陈述。

- transition_to_next_cn：提出研究问题并给出总体方法。

#### 3. 3

- step：3

- writing_job_cn：把行为/表情信号翻译成推荐模型构件。

- research_job_cn：设计置信度规则、负采样策略和矩阵分解目标函数。

- required_evidence_cn：每个公式的文献或逻辑理由。

- transition_to_next_cn：说明这些构件需要真实用户数据检验。

#### 4. 4

- step：4

- writing_job_cn：设计用户实验过程和数据采集规范。

- research_job_cn：招募被试、控制环境、录制屏幕、形成用户商品交互数据和金标准。

- required_evidence_cn：样本量、有效人数、交互记录规模、行为分布。

- transition_to_next_cn：准备baseline和评价指标。

#### 5. 5

- step：5

- writing_job_cn：设置递增信息量的baseline。

- research_job_cn：构造从无个性化到逐步加入行为、驻留时间、表情/标题相似度的对比算法。

- required_evidence_cn：每个baseline的定义、参数和数据输入。

- transition_to_next_cn：呈现总体性能表。

#### 6. 6

- step：6

- writing_job_cn：报告总体性能并解释差异来源。

- research_job_cn：计算Precision/MAP，与baseline比较，解释为什么新方法更好。

- required_evidence_cn：总指标表，必要时统计检验。

- transition_to_next_cn：进入稳健性分析。

#### 7. 7

- step：7

- writing_job_cn：加入分组、beyond-accuracy和案例检验。

- research_job_cn：按用户类型/交互量分组，计算流行度/多样性，选择典型案例解释。

- required_evidence_cn：分组图和表、多样性度量、用户反馈命中案例。

- transition_to_next_cn：收束到结论和实践意义。

#### 8. 8

- step：8

- writing_job_cn：结论重构缺口闭合，提出贡献、实践意义和局限。

- research_job_cn：总结方法适用场景，说明未检验的边界。

- required_evidence_cn：实验结果概括和与引言的呼应。

- transition_to_next_cn：结束全文。

### most_transferable_moves_cn

1. 用真实平台界面定义研究场景，让算法设计有具体锚点。

2. 指出点击不是偏好的充分条件，为置信度加权提供理由。

3. 把表情、行为数、驻留时间、标题相似度逐步折算成统一置信度矩阵。

4. 设计从弱到强的baseline阶梯，使比较结果可解释为信息源贡献。

5. 用真实用户反馈作为金标准，而不是仅用历史行为代理评分。

6. 在总体精度之后增加用户分组、流行度/多样性和案例检验。

7. 最后用实践意义和局限把单次实验结果包装成可复用设计知识。

### resource_intensive_or_nonstandard_parts_cn

1. 真实VFR平台部署（JD.com AR试妆）与81名付费女性学生招募。

2. 手机屏幕录制和面部视频采集，涉及隐私和实验控制。

3. 录屏人工按商品切分并标注为用户-商品-交互数据，成本高。

4. FAN表情识别需要视频帧处理和时间成本。

5. 通过邮件发放推荐列表并回收用户偏好反馈，过程依赖用户配合。

6. 固定教室、固定时间段、独立空间等实验条件并非一般研究者随手可得。

### what_not_to_copy_superficially_cn

1. 不能只写‘面部表情增强推荐’而在没有真实表情识别和用户偏好金标准的情况下宣称效果。

2. 不能只罗列baseline而不说明每个baseline对应哪些信号，否则比较无法解释。

3. 不能把小样本、一次选择反馈包装成大规模统计显著结论。

4. 不能把‘表情映射为0/1’称作‘显式反馈’而不讨论表情识别误差和用户个体差异。

5. 不能只复制‘AR增强电商价值’的口号，必须有实验数据支撑。

- single_best_description_of_the_routine_cn：以真实VFR场景中的细粒度交互（尤其面部表情）为信息源，通过把行为信号渐进式转化为置信度和负样本权重，构造加权矩阵分解推荐器，并用真实用户偏好作金标准的对照实验来支撑设计知识。

## 分析边界

文章来自排版文本，没有连续页码，位置证据使用原文章节和图表编号；个别OCR表述可能不完整（如Data statistics中2816后缺单位、'facial veiling'含义不明）；作者在招募82人与有效81人之间表述不完全一致。
