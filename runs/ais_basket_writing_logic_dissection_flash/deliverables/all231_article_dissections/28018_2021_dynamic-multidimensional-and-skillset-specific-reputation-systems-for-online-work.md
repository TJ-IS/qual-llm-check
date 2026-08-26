# Dynamic, Multidimensional, and Skillset-Specific Reputation Systems for Online Work

- 作者：Marios Kokkodis
- 年份 / 期刊：2021 / Information Systems Research
- DOI：10.1287/isre.2020.0972
- 源文件：28018_2021_dynamic-multidimensional-and-skillset-specific-reputation-systems-for-online-work.md
- 论文主类型：build_evaluate_design_science
- 主导写作弧线：performance_gap_artifact_benchmark_generalize
- 置信度：0.72

## 文章级论证概况

- 核心问题：如何为在线劳动市场设计动态、多维、技能集特定的声誉系统，以克服声誉膨胀、声誉归因和声誉静态性三大缺陷？

- 制品与设计：提出HMM-W2V增强智能声誉框架。组件A用word embedding把任意技能集映射到10个潜在能力维度；组件B用带协变量转移/发射的hidden Markov models为每个能力维度估计动态质量；组件C按技能集权重聚合能力维度估计，生成技能集特定声誉分数。

- 客观结果：在58,459个完成任务的在线劳动市场数据上，HMM-W2V在排序相关、排序表现、lift、声誉分布接近正态程度、非完美工人识别和Open内申请者排序方面显著优于当前声誉系统及线性、LSTM、XGBoost、SVM-reg、WorkerRank等10个基准；在77,044条餐馆评论数据上验证了跨情境泛化，并优于推荐系统适配方案。

- 核心贡献：首次系统指出在线劳动市场声誉系统的三类缺陷，提出并实现三条设计原则（技能分解、动态能力特定质量评估、按需聚合），形成可复用的动态多维技能集声誉框架，并展示其与推荐系统协作提升交易效率的价值。

- 整篇论证链：作者先由在线劳动市场信任与声誉机制的重要性出发，指出现有声誉系统因统一平均评分而存在三方面缺陷：不能把声誉归属于具体技能、假设工人质量静态、评分过度膨胀。随后逐一排除人类/机器/混合型声誉系统、技能测试和推荐系统适配方案无法解决这些缺陷，从而把文献缺口定义为缺少同时处理三缺陷的声誉设计。作者据此提出三条设计原则，并将其转化为HMM-W2V框架的三个组件：W2V技能分解处理归因，HMM动态质量评估处理静态性，聚合处理技能集特定性与膨胀。模型无关证据先用数据展示三类现象确实存在，再通过网格搜索确定组件与超参，随后用10折交叉验证与当前系统、先进机器学习基准、WorkerRank及推荐系统适配进行多指标对比，证明排序、分布、非完美工人和Open内排序的优势，并用AUC协作实验展示下游价值。最后用餐馆评论数据复制主要结果，说明框架可泛化到其他动态多维且评分膨胀的在线平台，再将贡献上升为设计原则、方法论指南与未来工作含义。

## 类型与写作弧线判定

- 论文主类型判定：虽然评价方式是离线计算benchmark，但整篇文章以“设计原则—组件—评价—设计知识”组织，明确声称设计原则和可复制方法，因此归为设计科学；其核心证据是计算制品在基准上的表现，而非现场实验或形式机制。

- 主导写作弧线判定：文章以现有声誉系统三类性能缺口（膨胀、归因、静态性）为出发点，构建HMM-W2V，随后在线劳动市场与餐馆评论两类基准中证明优势，最后一般化为可复用设计原则；不是以迭代诊断—修正为主，也不是以形式模型/政策为主。

## 研究开展程序

- study_or_phase_count：7

- 研究阶段总序列：七阶段从现象证据到构建调参、主评价、替代方案排除、下游协作、附加预测性能和跨情境泛化，形成“发现缺陷—设计制品—基准证明—边界推广”的累积论证。

### studies_or_phases

#### 1. 模型无关证据阶段

- order：1

- name_cn：模型无关证据阶段

- question_cn：当前声誉系统是否在聚焦市场中真实表现出膨胀、归因和静态性？

- inputs_and_setting_cn：LaborBazaar（化名）真实在线劳动市场：662,423次申请、58,459个完成任务、13,510名工人、547个技能、17,563个技能集、141国、12个月。

- designed_or_compared_object_cn：无操纵，仅描述现有人工声誉系统的评分分布与工人任务序列。

- baseline_control_or_counterfactual_cn：无直接对照；以正态/代表性分布作为隐含参照。

##### objective_metrics

1. 反馈评分分布均值/中位数

2. 分技能评分均值/中位数

3. 连续任务技能集余弦相似度与潜在空间余弦相似度

4. 至少使用一个新技能的工人比例

5. 新技能后初始低分比例

6. 后续声誉回升趋势

- analysis_method_cn：描述性统计、余弦相似度、趋势观察。

- main_result_cn：评分高度膨胀（均值中位数0.86）；不同技能评分不同；连续任务技能集平均相似度仅0.33；约47%工人12个月内使用新技能，66%在新技能后初始低分但随后回升。

- argumentative_role_cn：用真实数据把三个抽象缺陷变成可观察现象，为后续设计原则提供经验理由。

- remaining_uncertainty_cn：现象描述不等于改进方案；未说明新框架能否克服这些问题。

- link_to_next_phase_cn：引出需要能够处理这些现象的框架设计，并确定输入变量。

##### evidence_pointers

1. Section 4.1

2. Figure 2(a)-(f)

3. Table 3

#### 2. 框架设计与超参数选择阶段

- order：2

- name_cn：框架设计与超参数选择阶段

- question_cn：在聚焦情境下，三个组件各应采用哪种建模选择和超参数？

- inputs_and_setting_cn：LaborBazaar数据；技能文本、任务反馈、工人历史变量。

- designed_or_compared_object_cn：框架的组件A（W2V vs D2V vs GMM）、组件B（HMM vs 线性/SVM/LSTM/XGBoost）、组件C（聚合方式）以及维度数与HMM参数。

- baseline_control_or_counterfactual_cn：同一数据上的替代建模选项；网格搜索比较。

##### objective_metrics

1. 声誉估计排序相关

2. 预测MAE/RMSE

3. 模型选择表现

- analysis_method_cn：网格搜索和10折交叉验证（按工人分fold）。

- main_result_cn：最终选择W2V、HMM结构、公式(8)聚合、10个能力维度、Beta发射、多项logit转移。

- argumentative_role_cn：确定最终制品配置，使后续基准比较建立在最有利的合理实现上。

- remaining_uncertainty_cn：虽有实现优势，但未证明相对外部声誉系统的整体优势。

- link_to_next_phase_cn：把调好的HMM-W2V与多种声誉系统进行正式基准比较。

##### evidence_pointers

1. Section 5.1

2. Online Appendix C

3. Figure 11

#### 3. 替代声誉系统基准评价阶段

- order：3

- name_cn：替代声誉系统基准评价阶段

- question_cn：HMM-W2V能否比现有和先进声誉系统提供更准确的工人声誉？

- inputs_and_setting_cn：LaborBazaar数据，10折工人级交叉验证。

- designed_or_compared_object_cn：HMM-W2V与当前声誉、线性模型、LSTM、XGBoost、SVM回归、WorkerRank。

- baseline_control_or_counterfactual_cn：当前声誉系统与5个先进替代模型。

##### objective_metrics

1. Spearman rho和Kendall tau排序相关

2. Top-k排序表现

3. 平均lift

4. 总变差距离vs正态分布

5. 非完美工人子集排序相关

6. Open内Top-n被雇者平均表现

- analysis_method_cn：10折交叉验证、改进百分比、置信区间、分组分析。

- main_result_cn：HMM-W2V在排序相关上比当前系统高85%、比其他替代高20–60%；Top组表现高8%、lift高9%；分布距正态近37%；非完美工人子集显著更好；Open内排序优于大多数替代系统。

- argumentative_role_cn：核心证据：证明新制品在多项评价目标上优于所有竞争系统。

- remaining_uncertainty_cn：是否只是比声誉系统好，而推荐系统适配也能达到相似效果？下游是否真正受益？

- link_to_next_phase_cn：检验并排除推荐系统适配方案，再展示声誉与推荐系统协作的好处。

##### evidence_pointers

1. Section 5.3

2. Figures 3-7

#### 4. 推荐系统适配基准阶段

- order：4

- name_cn：推荐系统适配基准阶段

- question_cn：将推荐系统适配为工人声誉框架能否解决三类缺陷并与HMM-W2V竞争？

- inputs_and_setting_cn：把LaborBazaar数据改造成“技能集–工人–平均反馈”矩阵和技能集-评分序列。

- designed_or_compared_object_cn：kNN、SVD、slope one协同过滤，及CNN序列推荐系统。

- baseline_control_or_counterfactual_cn：HMM-W2V；同时以当前声誉作为隐含参照。

##### objective_metrics

1. Spearman rho和Kendall tau排序相关

- analysis_method_cn：网格搜索调参、10折交叉验证、改进百分比。

- main_result_cn：HMM-W2V显著优于所有推荐系统适配，改进20–60%；适配所需编码与物品假设伤害性能。

- argumentative_role_cn：排除推荐系统作为替代方案，证明需要情境适配的声誉框架。

- remaining_uncertainty_cn：推荐系统虽不能替代声誉，但声誉是否可以增强推荐系统？

- link_to_next_phase_cn：进入协作实验。

##### evidence_pointers

1. Section 5.4.1

2. Table 2

3. Figure 8

#### 5. 声誉与推荐系统协作验证阶段

- order：5

- name_cn：声誉与推荐系统协作验证阶段

- question_cn：把HMM-W2V声誉加入求职者推荐模型能否提升推荐性能？

- inputs_and_setting_cn：LaborBazaar申请/雇佣数据；在线附录G的预测特征。

- designed_or_compared_object_cn：求职者推荐分类器（logistic、贝叶斯网络、随机森林、梯度提升、神经网络）在用当前声誉、HMM-W2V声誉、原预测特征、原特征+HMM声誉四种特征设置下的表现。

- baseline_control_or_counterfactual_cn：同一分类器使用当前声誉或仅用预测特征。

##### objective_metrics

1. AUC

2. 相对AUC提升百分比

- analysis_method_cn：10折交叉验证，分模型计算改进。

- main_result_cn：相对当前声誉，HMM-W2V声誉带来2.4–10% AUC提升；在预测特征基础上加入HMM声誉再提升1.3–3.5%。

- argumentative_role_cn：证明声誉与推荐系统互补，并说明准确声誉的实际交易价值。

- remaining_uncertainty_cn：AUC提升与实际雇主决策质量、平台收入的关系尚未直接测量。

- link_to_next_phase_cn：转向附加预测性能与跨情境泛化，检验一般性。

##### evidence_pointers

1. Section 5.4.2

2. Figure 9

3. Online Appendix G

#### 6. 预测与解释性能补充评价阶段

- order：6

- name_cn：预测与解释性能补充评价阶段

- question_cn：HMM-W2V在预测误差和解释方差上是否也优于替代系统？

- inputs_and_setting_cn：LaborBazaar数据，10折交叉验证。

- designed_or_compared_object_cn：HMM-W2V与替代声誉系统的预测误差和线性解释力。

- baseline_control_or_counterfactual_cn：当前声誉、线性、LSTM、XGBoost、SVM-reg等。

##### objective_metrics

1. MAE

2. RMSE

3. 线性回归R²

- analysis_method_cn：预测误差比较、线性回归拟合。

- main_result_cn：HMM-W2V显著降低MAE/RMSE，并在线性规格中解释更多观察绩效方差。

- argumentative_role_cn：补充证据，说明优势不只在排序层面，也在校准和解释层面。

- remaining_uncertainty_cn：未测试其他情境的预测误差。

- link_to_next_phase_cn：进入餐馆评论情境的外部效度检验。

##### evidence_pointers

1. Section 5.5

2. Online Appendix D

3. Figure 13

4. Table 5

#### 7. 跨情境泛化验证阶段

- order：7

- name_cn：跨情境泛化验证阶段

- question_cn：框架能否泛化到另一个评分膨胀、质量多维且动态的在线声誉情境？

- inputs_and_setting_cn：77,044条餐馆评论，来自大型餐馆评论平台。

- designed_or_compared_object_cn：HMM-W2V与替代声誉系统和推荐系统适配；另与观察到的四维人工评分维度比较。

- baseline_control_or_counterfactual_cn：替代声誉系统、推荐系统适配、已有四维人工评分。

##### objective_metrics

1. 排序相关改进百分比

2. 与人工维度比较的改进

- analysis_method_cn：同前：10折交叉验证、网格搜索、显著性检验。

- main_result_cn：HMM-W2V显著优于替代声誉系统和推荐系统适配；其潜在能力维度包含与人工四维评分不同的信息。

- argumentative_role_cn：建立外部效度，并把贡献从一次性性能结果提升为可复用设计知识。

- remaining_uncertainty_cn：餐馆评分中的四维人工评分与潜在维度的差异未被近似；现场部署影响未测。

- link_to_next_phase_cn：回到讨论，把结果表述为设计原则、方法论指南和平台应用边界。

##### evidence_pointers

1. Section 5.5

2. Online Appendix E.3

3. Figures 14-16

## 各部分修辞架构

### abstract_moves

1. 情境：在线工作声誉系统对信任和交易效率重要。

2. 问题：现有系统未捕捉动态多维性质，存在声誉膨胀、归因、静态性。

3. 方案：提出HMM-W2V增强智能框架，三组件。

4. 证据：在线劳动市场58,459任务和77,044餐馆评论。

5. 结果：三类改进并泛化。

6. 类型声明：AI与人类输入增强决策。

### introduction_moves

1. 从市场增长和未来工作背景收束到声誉机制。

2. 由声誉机制价值转向三大缺陷：静态性、归因、膨胀。

3. 提出研究问题并预告三原则、三组件。

4. 用数据结果和泛化结果作为早期承诺。

5. 声明贡献与更广泛影响。

### theory_and_knowledge_moves

1. 综述在线信任、声誉系统类型与在线劳动市场研究。

2. 把现有系统分类为人类/机器/混合并逐一排除。

3. 引入推荐系统文献，说明映射与编码假设。

4. 用Schmidt-Hunter正常分布作为聚合原则依据。

### artifact_design_moves

1. 将三缺陷转成三条设计原则。

2. 组件A：W2V技能分解。

3. 组件B：HMM动态质量评估。

4. 组件C：聚合技能集声誉。

5. 用模型无关数据和变量定义来连接模型与现实。

### evaluation_moves

1. 描述数据和模型无关证据。

2. 网格搜索确定建模与超参。

3. 设定10个替代声誉系统和多项指标。

4. 分层展示结果：排序、分布、非完美工人、Open内排序。

5. 对推荐系统适配进行基准并展示协作。

6. 用餐馆评论做泛化测试。

### discussion_and_contribution_moves

1. 重述缺陷与框架对应关系。

2. 声明研究、方法论贡献。

3. 把适用范围扩大到Yelp/Uber/LinkedIn等平台。

4. 讨论离散状态、降级转移、W2V/D2V选择边界和未来状态空间模型。

5. 总结对工人、雇主、企业和未来工作的启示。

## 理论/知识到设计的翻译

### 知识/理论基础

1. 在线市场信任与声誉系统文献

2. 在线劳动市场中的声誉转移、雇佣选择与收入研究

3. 声誉膨胀文献及正常分布个体差异研究（Schmidt and Hunter 1983）

4. 分布式词汇表示/词嵌入（Mikolov et al. 2013）

5. 隐马尔可夫模型与序列建模

6. 推荐系统与序列感知推荐文献

- 理论—设计耦合：partial

- 耦合判定理由：设计原则明确来源于对三个缺陷的经验归纳和对人类能力正态分布的引用，因此知识基础影响了问题界定与整体架构；但W2V/HMM这些核心算法选择并非来自某个行为理论，而是通过网格搜索与其他ML模型比较后被保留。推荐系统适配、性能指标也来自工程文献。因此属于部分耦合。

- 理论到设计翻译链：文章没有严格的形式理论，而是从市场微观现象和既有实证规律出发。核心链条是：声誉系统的制度作用→现有系统三种可命名缺陷（膨胀、归因、静态性）→每条缺陷对应一条设计原则→三条原则分别决定W2V、HMM和聚合三组件→评价指标把“准确声誉”操作化为排序、分布、子群体与Open内表现→结果返回设计原则，提出可复用的设计知识。

### mapping_table

#### 1. 1

- theory_or_knowledge_claim_cn：声誉系统应通过减少信息不对称来促进在线劳动市场交易；现有一维平均评分不能刻画多技能工人的真实质量。

- mechanism_cn：Inflated uniform scores fail to differentiate workers; heterogeneous skillsets require decomposition; worker quality evolves, so static averages become stale.

- design_requirement_cn：声誉框架必须支持技能集特定的、动态更新的、具有区分能力的评分。

- artifact_choice_cn：三组件HMM-W2V框架：W2V技能分解、HMM动态质量评估、按需聚合。

- evaluated_contrast_cn：HMM-W2V vs 当前声誉、线性、LSTM、XGBoost、SVM-reg、WorkerRank。

- objective_result_cn：排序相关、排序表现、lift和分布接近正态等指标显著更优。

##### evidence_pointers

1. Section 5.3

2. Figures 3-7

#### 2. 2

- theory_or_knowledge_claim_cn：人类能力差异接近正态分布（Schmidt and Hunter 1983）。

- mechanism_cn：如果声誉评分准确反映能力，则总体分布应接近正态；当前正偏态表示膨胀和区分不足。

- design_requirement_cn：技能集特定声誉分布应接近正态并促进工人区分。

- artifact_choice_cn：Component C在能力维上聚合多个连续估计，生成细腻的连续分数。

- evaluated_contrast_cn：总变差距离与正态分布比较，HMM-W2V vs 替代声誉系统。

- objective_result_cn：HMM-W2V分布比替代系统近正态最多37%。

##### evidence_pointers

1. Section 5.3

2. Figure 5

#### 3. 3

- theory_or_knowledge_claim_cn：在线工人持续学习新技能并获得经验，质量动态演化。

- mechanism_cn：Uniform past averages cannot update quickly; latent quality states with stochastic transitions can revise estimates as new evidence arrives.

- design_requirement_cn：每个能力维度需要动态、可更新且允许向下修正的质量模型。

- artifact_choice_cn：Component B采用hidden Markov model，用工人历史变量影响转移概率，用观察特征影响发射分布。

- evaluated_contrast_cn：HMM vs 线性、SVM、LSTM、XGBoost等替代建模。

- objective_result_cn：HMM显著更优，尤其在非完美工人预测和排序相关上。

##### evidence_pointers

1. Section 3.2

2. Section 5.1

3. Figure 3

4. Figure 6

5. Online Appendix C

#### 4. 4

- theory_or_knowledge_claim_cn：技能集数量庞大且存在相关性；一维评分无法归属到技能。

- mechanism_cn：将技能视为词、技能集视为文档，通过W2V把任意技能组合投影到有限能力维，从而利用语义/技能相似性。

- design_requirement_cn：声誉框架必须可扩展到任意技能数，且无需为每个技能单独测试。

- artifact_choice_cn：Component A用W2V将技能映射到10维能力空间，并softmax归一化技能集权重。

- evaluated_contrast_cn：W2V vs D2V vs GMM；以及推荐系统适配中的技能集-物品映射。

- objective_result_cn：W2V在劳动市场情境中更优；推荐系统适配因映射假设而显著较差。

##### evidence_pointers

1. Section 3.1

2. Section 5.4.1

3. Figure 8

4. Online Appendix C

## 评价逻辑

### evaluation_modes

1. 离线benchmark on observational transaction data

2. 10-fold worker-level cross-validation

3. multiple advanced baseline models

4. nonperfect worker subset analysis

5. within-opening ranking analysis

6. recommender adaptation benchmark

7. downstream recommender AUC integration test

8. external context generalizability test

- why_these_evaluations_cn：由于无法在真实平台进行现场操纵，作者用离线交易数据在固定评估协议下证明制品预测质量；同时用多个基准确立优势，用推荐系统适配排除替代方案，用AUC协作实验展示下游价值，再用第二情境复制证明泛化，使离线benchmark承担多种论证任务。

- benchmark_and_contrast_chain_cn：先与当前声誉系统和先进ML模型比较，确立主优势；再与推荐系统适配比较，排除另一个候选方案；再展示声誉作为推荐系统特征可提升AUC，说明协作价值；最后在餐馆评论数据中复制主比较，形成“当前系统→先进系统→推荐系统→外部情境”的逐渐收紧和扩展链条。

### claim_evidence_ledger

#### 1. 1

- claim：HMM-W2V生成更准确、更适合区分工人的声誉排序。

- evidence：10折交叉验证中排序相关显著高于当前系统85%及替代系统20–60%；排序表现和lift也更高。

- assessment：充分：多指标、多基准、置信区间。避免单一指标。但排序相关均为离线指标。

#### 2. 2

- claim：HMM-W2V生成接近正态的声誉分布，缓解通胀。

- evidence：与正态分布的总变差距离比替代系统近37%。

- assessment：较充分：用正态分布作为理论参照，但正态分布是否必然等同于最优区分仍有假设成分。

#### 3. 3

- claim：HMM-W2V特别擅长识别非完美工人。

- evidence：在至少一次非完美反馈的子集中排序相关显著优于所有替代。

- assessment：充分：子群体分析避免整体准确率被多数完美工人掩盖。

#### 4. 4

- claim：HMM-W2V改善Open内申请者排序。

- evidence：Top-n被雇者平均表现优于几乎所有替代，仅对WorkerRank/XGB部分显著性较弱。

- assessment：部分充分：优势方向一致，但对最强基线仅部分显著，需谨慎表述。

#### 5. 5

- claim：推荐系统适配不足以提供声誉。

- evidence：kNN/SVD/slope one/CNN序列推荐适配后显著差于HMM-W2V，改进20–60%。

- assessment：充分：直接检验了表2中的映射假设，并显示其性能损失。

#### 6. 6

- claim：框架可泛化到其他动态多维且膨胀的情境。

- evidence：77,044餐馆评论复制实验显著优于替代声誉/推荐系统，且潜在维度不同于人工四维评分。

- assessment：较充分：一个外部情境复制可证明可行性，但不足以证明所有此类平台均适用。

- internal_validity_strategy_cn：按工人划分10折，避免同一工人历史跨折导致的信息泄漏；所有基准在同一评估协议下比较；对每个结果报告置信区间和显著性；用非完美工人子集和Open内排序等细粒度分析避免总体指标掩盖差异；用组件级网格搜索和替代建模比较支撑设计选择。

- external_validity_strategy_cn：在同一市场内用10折交叉验证实现样本外预测；在另一个情境（77,044餐馆评论）中复制主要实验；与人工四维评分维度比较，说明潜在维度包含额外信息；最后讨论W2V与D2V在不同文本结构下的适用边界。

- what_is_not_actually_tested_cn：未部署到真实平台，不测量雇主实际决策、交易结果、长期收入或工人行为反应；未进行随机化现场干预；没有对“AUC提升会转化为平台收益”做直接检验；餐馆评论泛化只是另一观察数据集，不是其他市场现场数据；推荐系统协作只是离线AUC，不是端到端交易结果。

## 贡献闭环

- technical_claim_cn：在排序相关、分布、非完美工人和Open内排序等指标上，HMM-W2V显著优于10个替代声誉系统和推荐系统适配。

- artifact_claim_cn：框架的三个组件共同导致了优势：W2V处理归因、HMM处理静态性、聚合处理技能集特定性和膨胀；组件替换实验和网格搜索支持每个组件贡献。

- mechanism_claim_cn：作者主张机制是：把声誉分解到潜在能力维度、用状态转移捕捉动态演化、用聚合产生正态分布来区分工人；还主张降级转移允许新证据修正估计。

- boundary_claim_cn：框架适用于评分膨胀、服务质量多维且动态的在线平台，如在线劳动市场、餐馆评论、共享出行、职业网络；W2V更适用于结构化技能词项情境，D2V更适合非结构化文本情境。

- reusable_design_knowledge_cn：三条设计原则：任意技能组合分解到有限能力维度、动态能力特定质量评估、按需聚合生成技能集声誉；以及可复用的HMM变量选择、似然估计和网格搜索评价流程。

- theoretical_contribution_cn：扩展了在线声誉文献：首次把声誉静态性/归因明确概念化，并在人类能力正态分布规律与聚合设计之间建立连接；也为增强智能（IA）系统提供人机评分融合的基线。

- how_discussion_closes_intro_gap_cn：讨论重述引言中的三大缺陷，逐一说明框架组件对应关系，并用两个数据集的结果把缺陷从问题转化为可解决的设计缺口，进而提出设计原则与平台应用建议。

- overclaim_or_unsupported_leaps_cn：从离线指标到“提高交易效率/收入”的因果跳跃；“首次”主张依赖文献覆盖；正态分布作为最优目标未经验证；AUC提升对实际雇主选择的影响未测；非完美工人子集结果与整体排序结果有重叠；餐馆泛化只证明单一替代情境。

## 句级写作动作图谱

### 1. P1 S1-S2

- order：1

- section：Introduction

- locator：P1 S1-S2

- move_code：CONTEXT

- paraphrase_cn：在线劳动市场促进全球短期合同和自由职业工作。

- rhetorical_function_cn：建立研究发生的制度与市场背景。

- depends_on_cn：无。

- sets_up_cn：为后文声誉机制的重要性提供场景。

- evidence_pointer：Section 1

### 2. P1 S3-S4

- order：2

- section：Introduction

- locator：P1 S3-S4

- move_code：CONTEXT

- paraphrase_cn：在线劳动市场过去十年指数增长，自动化与共享经济将加速这一趋势。

- rhetorical_function_cn：强调问题的重要性和时效性。

- depends_on_cn：场景建立。

- sets_up_cn：支持后文“准确声誉影响未来工作”的论断。

- evidence_pointer：Section 1

### 3. P2 S1

- order：3

- section：Introduction

- locator：P2 S1

- move_code：PRACTICAL_STAKES

- paraphrase_cn：在线劳动市场成功的一个决定因素是平台在雇主和工人之间建立的中间信任。

- rhetorical_function_cn：把话题从市场增长收束到信任机制。

- depends_on_cn：市场背景。

- sets_up_cn：引出声誉系统作为信任机制。

- evidence_pointer：Section 1

### 4. P2 S2

- order：4

- section：Introduction

- locator：P2 S2

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：声誉系统是平台用来增加信任、减少信息不对称的标准机制。

- rhetorical_function_cn：引入核心研究对象与既有知识。

- depends_on_cn：信任机制论断。

- sets_up_cn：为后续指出声誉系统缺陷埋下伏笔。

- evidence_pointer：Section 1

### 5. P2 S3-S6

- order：5

- section：Introduction

- locator：P2 S3-S6

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：反馈评分积累为工人在线简历，衡量预期服务质量，增加雇主信任并影响工人定价。

- rhetorical_function_cn：说明声誉系统为什么重要。

- depends_on_cn：声誉系统作为标准机制。

- sets_up_cn：让后文的“设计缺陷”具有严重后果。

- evidence_pointer：Section 1

### 6. P3 S1

- order：6

- section：Introduction

- locator：P3 S1

- move_code：LIMITATION

- paraphrase_cn：尽管有这些好处，当前声誉系统设计没有捕捉在线工作的动态和多维本质。

- rhetorical_function_cn：从已有收益转向问题。

- depends_on_cn：前文声誉重要性。

- sets_up_cn：开启三类缺陷的讨论。

- evidence_pointer：Section 1

### 7. P3 S2-S5

- order：7

- section：Introduction

- locator：P3 S2-S5

- move_code：LIMITATION

- paraphrase_cn：系统统一平均所有历史反馈，隐含假设工人质量不随时间变化，但技能更替速度加快，工人必须持续再学习。

- rhetorical_function_cn：指出静态性缺陷及其现实原因。

- depends_on_cn：声誉系统统一平均的特征。

- sets_up_cn：为动态质量评估组件提供依据。

- evidence_pointer：Section 1

### 8. P3 S6-S9

- order：8

- section：Introduction

- locator：P3 S6-S9

- move_code：LIMITATION

- paraphrase_cn：声誉分数是一维且与技能集无关，但数字工作场所资质高度异质，工人常完成需要不同技能集合的任务。

- rhetorical_function_cn：指出归因缺陷及市场异质性。

- depends_on_cn：一维评分机制。

- sets_up_cn：为技能分解组件提供依据。

- evidence_pointer：Section 1

### 9. P3 S10-S13

- order：9

- section：Introduction

- locator：P3 S10-S13

- move_code：LIMITATION

- paraphrase_cn：与其他平台类似，在线劳动市场声誉分数过度正向，许多工人被评得“好于平均”，无法有效区分。

- rhetorical_function_cn：指出膨胀缺陷及其后果。

- depends_on_cn：一维平均和反馈偏差。

- sets_up_cn：为聚合产生正态分布的设计提供依据。

- evidence_pointer：Section 1

### 10. P4 S1

- order：10

- section：Introduction

- locator：P4 S1

- move_code：RQ_OR_OBJECTIVE

- paraphrase_cn：在这些缺陷下，如何设计动态、多维、技能集特定的声誉框架？

- rhetorical_function_cn：提出核心研究问题。

- depends_on_cn：三类缺陷。

- sets_up_cn：引出解决方案的简短预告。

- evidence_pointer：Section 1

### 11. P4 S2

- order：11

- section：Introduction

- locator：P4 S2

- move_code：STUDY_OVERVIEW

- paraphrase_cn：提出一个增强智能系统，依赖三条设计原则：技能分解、动态能力特定质量评估、聚合。

- rhetorical_function_cn：预告整体方案和设计原则。

- depends_on_cn：研究问题。

- sets_up_cn：为后文组件A/B/C提供预览。

- evidence_pointer：Section 1

### 12. P4 S3-S5

- order：12

- section：Introduction

- locator：P4 S3-S5

- move_code：MECHANISM

- paraphrase_cn：技能分解解决归因，动态评估解决静态性，聚合产生正态分布并促进工人区分。

- rhetorical_function_cn：把原则与缺陷对应，让设计看似必然。

- depends_on_cn：三条设计原则。

- sets_up_cn：为评价指标中的分布与排序提供逻辑。

- evidence_pointer：Section 1

### 13. P5 S1-S2

- order：13

- section：Introduction

- locator：P5 S1-S2

- move_code：RESULT

- paraphrase_cn：58,459个完成任务的分析显示，新方法显著优于10个替代声誉系统，并在排序、非完美工人识别和Open内排序三方面更好。

- rhetorical_function_cn：在引言中给出核心实证结果。

- depends_on_cn：框架设计。

- sets_up_cn：让读者预期后文的详细评估。

- evidence_pointer：Section 1, 摘要

### 14. P5 S3

- order：14

- section：Introduction

- locator：P5 S3

- move_code：RESULT

- paraphrase_cn：77,044条餐馆评论进一步显示框架能泛化到其他反馈过度正向、质量多维且动态的情境。

- rhetorical_function_cn：提供外部效度的早期承诺。

- depends_on_cn：劳动市场结果。

- sets_up_cn：为后文第二情境复制做准备。

- evidence_pointer：Section 1

### 15. P6 S1-S2

- order：15

- section：Introduction

- locator：P6 S1-S2

- move_code：CONTRIBUTION

- paraphrase_cn：本文首次指出当前声誉系统缺陷并提出未来系统应具备的设计原则。

- rhetorical_function_cn：声明理论/文献贡献。

- depends_on_cn：三类缺陷与设计原则。

- sets_up_cn：为讨论中的研究贡献提供定位。

- evidence_pointer：Section 1

### 16. P6 S3-S5

- order：16

- section：Introduction

- locator：P6 S3-S5

- move_code：CONTRIBUTION

- paraphrase_cn：准确声誉帮助工人区分、帮助雇主快速知情决策、帮助市场改进推荐算法并理解供应分布。

- rhetorical_function_cn：把技术结果提升为管理价值。

- depends_on_cn：准确声誉。

- sets_up_cn：为讨论的平台含义提供基础。

- evidence_pointer：Section 1

### 17. P7 S1-S4

- order：17

- section：Introduction

- locator：P7 S1-S4

- move_code：CONTRIBUTION

- paraphrase_cn：该IA框架展示人类输入与机器学习结合可增强智能，并通过工人区分与供应再分配影响未来工作。

- rhetorical_function_cn：把论文接入增强智能和未来工作的宏大议题。

- depends_on_cn：框架与结果。

- sets_up_cn：呼应期刊专刊主题。

- evidence_pointer：Section 1

### 18. 段落开头

- order：18

- section：2.2.1

- locator：段落开头

- move_code：LIMITATION

- paraphrase_cn：在线劳动市场声誉系统不完美，经历声誉膨胀、归因和静态性三个缺陷。

- rhetorical_function_cn：把引言中的三个问题正式命名为研究框架。

- depends_on_cn：引言问题。

- sets_up_cn：为第2.2.2节的替代方案排除提供分类框架。

- evidence_pointer：Section 2.2.1

### 19. Reputation Inflation段

- order：19

- section：2.2.1

- locator：Reputation Inflation段

- move_code：MECHANISM

- paraphrase_cn：低分工人难以再被雇佣因而退出市场，雇主又感受同伴压力给好评，导致评分正向偏斜。

- rhetorical_function_cn：解释膨胀的微观机制。

- depends_on_cn：三类缺陷框架。

- sets_up_cn：说明为什么膨胀会削弱区分能力。

- evidence_pointer：Section 2.2.1

### 20. Reputation Attribution段

- order：20

- section：2.2.1

- locator：Reputation Attribution段

- move_code：PHENOMENON

- paraphrase_cn：一维总体评分无法回答IT任务中网络、C和Python各自的服务质量是多少。

- rhetorical_function_cn：用具体例子展示归因缺陷。

- depends_on_cn：异质技能环境。

- sets_up_cn：支持技能分解的必要性。

- evidence_pointer：Section 2.2.1

### 21. Reputation Staticity段

- order：21

- section：2.2.1

- locator：Reputation Staticity段

- move_code：MECHANISM

- paraphrase_cn：工人通过经验和学习新技能演化，但当前系统把服务者当作静态商品来平均评分。

- rhetorical_function_cn：解释静态性的机制和误导性。

- depends_on_cn：技能演化现象。

- sets_up_cn：支持动态质量评估的必要性。

- evidence_pointer：Section 2.2.1

### 22. 段尾

- order：22

- section：2.2.1

- locator：段尾

- move_code：GAP

- paraphrase_cn：这些缺陷使质量估计往往不能预测未来表现，因此需要探索替代声誉系统。

- rhetorical_function_cn：把缺陷转化为研究缺口和行动需要。

- depends_on_cn：三类缺陷。

- sets_up_cn：引出对现有替代系统的检验。

- evidence_pointer：Section 2.2.1

### 23. 开篇段

- order：23

- section：2.2.2

- locator：开篇段

- move_code：LIMITATION

- paraphrase_cn：商业人类声誉系统有膨胀和部分归因/静态性问题；机器与混合系统在适用性或目标上不适合在线劳动市场。

- rhetorical_function_cn：逐类排除现有系统。

- depends_on_cn：三类缺陷分类。

- sets_up_cn：使文献缺口更清晰。

- evidence_pointer：Section 2.2.2

### 24. 技能测试段

- order：24

- section：2.2.2

- locator：技能测试段

- move_code：LIMITATION

- paraphrase_cn：基于项目反应理论的技能测试成本高、不能扩展、且工人可只展示正向认证。

- rhetorical_function_cn：排除用测试解决归因的思路。

- depends_on_cn：在线劳动市场特殊性。

- sets_up_cn：强调需要无需测试的自动分解方案。

- evidence_pointer：Section 2.2.2

### 25. WorkerRank段

- order：25

- section：2.2.2

- locator：WorkerRank段

- move_code：LIMITATION

- paraphrase_cn：WorkerRank通过雇主隐含判断的链接分析排序工人，但并没有解决归因和静态性，只是可能隐含缓解膨胀。

- rhetorical_function_cn：排除最接近的在线劳动市场声誉方法。

- depends_on_cn：链接分析方法。

- sets_up_cn：为后文与其直接比较提供理由。

- evidence_pointer：Section 2.2.2

### 26. 设计动态声誉系统段

- order：26

- section：2.2.3

- locator：设计动态声誉系统段

- move_code：REQUIREMENT

- paraphrase_cn：表1显示文献未同时解决三类缺陷，从而提出三条设计原则：技能分解、动态估计、按需聚合。

- rhetorical_function_cn：把缺口转成设计要求。

- depends_on_cn：表1的文献比较。

- sets_up_cn：定义后续框架的组件结构。

- evidence_pointer：Table 1

### 27. 开篇

- order：27

- section：2.3

- locator：开篇

- move_code：RQ_OR_OBJECTIVE

- paraphrase_cn：推荐系统也解决信息不对称，那么它们能否解决三类缺陷并提供技能集声誉？

- rhetorical_function_cn：提出一个竞争性替代框架。

- depends_on_cn：声誉与推荐系统具有相似功能。

- sets_up_cn：为后文推荐系统适配实验铺垫。

- evidence_pointer：Section 2.3

### 28. 差异段

- order：28

- section：2.3.1

- locator：差异段

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：声誉系统范围更广，可生成排名、影响估值、提供反馈；推荐系统往往服务单一目标。

- rhetorical_function_cn：区分两个概念和功能。

- depends_on_cn：推荐系统文献。

- sets_up_cn：解释为什么不能简单用推荐系统替代。

- evidence_pointer：Section 2.3.1

### 29. 映射段

- order：29

- section：2.3.2

- locator：映射段

- move_code：REQUIREMENT

- paraphrase_cn：把推荐系统用于声誉时，需要将工人映射为用户、技能集映射为物品、平均反馈映射为评分。

- rhetorical_function_cn：定义推荐系统适配所需的映射。

- depends_on_cn：推荐系统形式化。

- sets_up_cn：为后文说明该映射的弱点做准备。

- evidence_pointer：Section 2.3.2

### 30. 序列感知推荐段

- order：30

- section：2.3.2

- locator：序列感知推荐段

- move_code：LIMITATION

- paraphrase_cn：序列感知推荐系统主要基于隐式反馈并忽略显式评分，需要大量编码假设才能提供技能集声誉。

- rhetorical_function_cn：预告推荐系统适配的先天不足。

- depends_on_cn：推荐系统映射。

- sets_up_cn：为5.4.1的实证失败埋下伏笔。

- evidence_pointer：Section 2.3.2

### 31. 开篇段

- order：31

- section：3

- locator：开篇段

- move_code：DESIGN_FEATURE

- paraphrase_cn：根据三条设计原则，构建由技能分解、动态质量评估和聚合组成的三组件HMM-W2V框架。

- rhetorical_function_cn：启动制品设计。

- depends_on_cn：设计原则。

- sets_up_cn：逐个描述组件。

- evidence_pointer：Section 3, Figure 1

### 32. 直接估计缺陷段

- order：32

- section：3.1

- locator：直接估计缺陷段

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：直接估计每个技能集的声誉会造成数据稀疏、忽略技能集相关性和新技能需要重训三个问题。

- rhetorical_function_cn：为技能分解方法提供必要性论证。

- depends_on_cn：技能集规模。

- sets_up_cn：引入W2V作为解决方案。

- evidence_pointer：Section 3.1

### 33. W2V设计段

- order：33

- section：3.1

- locator：W2V设计段

- move_code：DESIGN_FEATURE

- paraphrase_cn：使用W2V把技能视为词、技能集视为文档，把任意技能集投影到D维能力空间。

- rhetorical_function_cn：选择并描述组件A的核心算法。

- depends_on_cn：对直接估计的批判。

- sets_up_cn：给出公式(1)(2)的技能集表示。

- evidence_pointer：Section 3.1

### 34. 替代方法段

- order：34

- section：3.1

- locator：替代方法段

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：D2V、聚类等替代映射方法也在附录中被讨论和比较。

- rhetorical_function_cn：说明组件选择并非随意，而会经验比较。

- depends_on_cn：W2V选择。

- sets_up_cn：为后文网格搜索和附录C提供依据。

- evidence_pointer：Section 3.1, Online Appendix C

### 35. HMM结构段

- order：35

- section：3.2

- locator：HMM结构段

- move_code：MECHANISM

- paraphrase_cn：工人每个能力维度的质量是潜在且动态的，HMM用潜在状态、状态转移和观测发射刻画这种演化。

- rhetorical_function_cn：描述组件B的核心机制。

- depends_on_cn：动态质量假设。

- sets_up_cn：为转移/发射变量设计提供框架。

- evidence_pointer：Section 3.2

### 36. 初始状态与转移/发射段

- order：36

- section：3.2

- locator：初始状态与转移/发射段

- move_code：DESIGN_FEATURE

- paraphrase_cn：新工人落入初始状态，历史信号向量影响状态转移概率，工人特征向量影响观测发射分布。

- rhetorical_function_cn：把HMM一般结构实例化到声誉情境。

- depends_on_cn：HMM机制。

- sets_up_cn：为第4.2节变量选择做准备。

- evidence_pointer：Section 3.2, 公式(3)-(6)

### 37. 聚合段

- order：37

- section：3.3

- locator：聚合段

- move_code：DESIGN_FEATURE

- paraphrase_cn：组件C对各能力维度的当前质量估计求和，得到任意技能集下的当前声誉。

- rhetorical_function_cn：描述组件C的聚合方式。

- depends_on_cn：组件A和B的输出。

- sets_up_cn：为评价中的技能集特定声誉奠定操作定义。

- evidence_pointer：Section 3.3, Equation (8)

### 38. 数据段

- order：38

- section：4

- locator：数据段

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：用LaborBazaar真实交易数据构建和评估框架，包含58,459个完成任务、17,563个技能集、12个月追踪。

- rhetorical_function_cn：交代数据来源和规模。

- depends_on_cn：框架需要真实反馈数据。

- sets_up_cn：为模型无关证据和后续评价提供数据基础。

- evidence_pointer：Section 4, Table 3

### 39. 模型无关证据段

- order：39

- section：4.1

- locator：模型无关证据段

- move_code：PHENOMENON

- paraphrase_cn：图2显示评分分布膨胀、不同技能评分差异大、连续任务技能集异构、工人学新技能后先低分后回升。

- rhetorical_function_cn：在建模前用描述性证据证明三类缺陷真实存在。

- depends_on_cn：数据。

- sets_up_cn：让框架设计拥有经验基础。

- evidence_pointer：Section 4.1, Figure 2(a)-(f)

### 40. 变量段

- order：40

- section：4.2

- locator：变量段

- move_code：DESIGN_FEATURE

- paraphrase_cn：选择累计声誉、总收入、完成工作数、工时、雇佣率作为转移变量；当前声誉和小时费率作为发射变量。

- rhetorical_function_cn：操作化HMM的转移和发射输入。

- depends_on_cn：HMM机制。

- sets_up_cn：为第5.1节网格搜索提供变量清单。

- evidence_pointer：Section 4.2, Table 4

### 41. 开篇

- order：41

- section：5

- locator：开篇

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：将数据按工人分成10折，每个工人的完整历史只出现在一折中，用10折交叉验证进行评估。

- rhetorical_function_cn：建立评估协议，避免信息泄漏。

- depends_on_cn：数据。

- sets_up_cn：为所有基准比较提供统一方法。

- evidence_pointer：Section 5

### 42. 设计选择段

- order：42

- section：5.1

- locator：设计选择段

- move_code：RESULT

- paraphrase_cn：网格搜索发现W2V优于D2V和GMM，HMM优于线性/SVM/LSTM/XGBoost，公式(8)聚合最优，D=10，采用Beta发射和多项logit转移。

- rhetorical_function_cn：报告最终配置选择。

- depends_on_cn：组件级替代方案。

- sets_up_cn：确定后续使用的HMM-W2V版本。

- evidence_pointer：Section 5.1, Online Appendix C

### 43. 替代声誉系统列表段

- order：43

- section：5.2

- locator：替代声誉系统列表段

- move_code：BENCHMARK_OR_CONTRAST

- paraphrase_cn：实现当前声誉、线性模型、LSTM、XGBoost、SVM回归和WorkerRank作为替代声誉系统。

- rhetorical_function_cn：定义基准集合。

- depends_on_cn：声誉系统分类。

- sets_up_cn：为5.3多指标比较提供对手。

- evidence_pointer：Section 5.2

### 44. Ranking Workers段首

- order：44

- section：5.3

- locator：Ranking Workers段首

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：声誉系统的最终目标是按预期服务质量排名工人，因此用排序相关、排序表现和lift衡量。

- rhetorical_function_cn：把评价目标与核心功能连接起来。

- depends_on_cn：声誉系统功能。

- sets_up_cn：为图3和图4的结果做方法论准备。

- evidence_pointer：Section 5.3

### 45. Ranking Workers结果段

- order：45

- section：5.3

- locator：Ranking Workers结果段

- move_code：RESULT

- paraphrase_cn：HMM-W2V在排序相关上比当前声誉平均高85%，比所有替代系统显著高20–60%。

- rhetorical_function_cn：报告第一个核心结果。

- depends_on_cn：排序指标。

- sets_up_cn：建立整体排序优势。

- evidence_pointer：Figure 3

### 46. Reputation Distribution段

- order：46

- section：5.3

- locator：Reputation Distribution段

- move_code：RESULT

- paraphrase_cn：新方法的声誉分布与正态分布的总变差距离比替代系统近最多37%。

- rhetorical_function_cn：报告分布层面的通胀缓解证据。

- depends_on_cn：正态分布参照。

- sets_up_cn：支持聚合可以提升区分能力的论断。

- evidence_pointer：Figure 5

### 47. Nonperfect Workers段

- order：47

- section：5.3

- locator：Nonperfect Workers段

- move_code：RESULT

- paraphrase_cn：在至少收到一次非完美反馈的工人子集中，HMM-W2V显著优于所有替代系统。

- rhetorical_function_cn：证明方法在更难预测且更可能造成损失的群体上更优。

- depends_on_cn：整体排序结果。

- sets_up_cn：支撑早期预警和干预的管理含义。

- evidence_pointer：Figure 6

### 48. Within-Opening Rankings段

- order：48

- section：5.3

- locator：Within-Opening Rankings段

- move_code：RESULT

- paraphrase_cn：在Open内Top-n排序中，HMM-W2V优于除WorkerRank和XGBoost之外的所有系统，对这两个最强基线也有部分显著优势。

- rhetorical_function_cn：报告决策情境下的排序结果。

- depends_on_cn：Open内排序指标。

- sets_up_cn：说明优势可转化到实际雇佣选择。

- evidence_pointer：Figure 7

### 49. 推荐系统适配结果段

- order：49

- section：5.4.1

- locator：推荐系统适配结果段

- move_code：RESULT

- paraphrase_cn：HMM-W2V显著优于kNN、SVD、slope one和CNN序列推荐系统，改进20–60%。

- rhetorical_function_cn：实证排除推荐系统适配方案。

- depends_on_cn：映射与编码假设。

- sets_up_cn：支持“需要情境化声誉框架”的核心论断。

- evidence_pointer：Figure 8

### 50. 协作结果段

- order：50

- section：5.4.2

- locator：协作结果段

- move_code：RESULT

- paraphrase_cn：把HMM-W2V声誉加入求职者推荐模型后，AUC比使用当前声誉高2.4–10%，比仅使用原预测特征高1.3–3.5%。

- rhetorical_function_cn：展示声誉与推荐系统的下游互补价值。

- depends_on_cn：求职者推荐模型。

- sets_up_cn：为平台部署和交易效率结论提供依据。

- evidence_pointer：Figure 9

### 51. Generalizability段

- order：51

- section：5.5

- locator：Generalizability段

- move_code：ROBUSTNESS_OR_BOUNDARY_TEST

- paraphrase_cn：在77,044条餐馆评论上，HMM-W2V显著优于替代声誉系统和推荐系统适配；其潜在维度不同于人工四维评分。

- rhetorical_function_cn：在第二情境中复制主要结果，建立外部效度。

- depends_on_cn：劳动市场主评价。

- sets_up_cn：支持把贡献从一次性性能提升上升为设计知识。

- evidence_pointer：Section 5.5, Online Appendix E.3, Figures 14-16

### 52. Discussion开篇

- order：52

- section：6

- locator：Discussion开篇

- move_code：CONTRIBUTION

- paraphrase_cn：重述三类缺陷以及HMM-W2V如何逐一解决，并总结四类实证改进。

- rhetorical_function_cn：把结果重新接回引言中的问题。

- depends_on_cn：所有实证结果。

- sets_up_cn：进入贡献和边界讨论。

- evidence_pointer：Section 6

### 53. Research Contributions段

- order：53

- section：6.1

- locator：Research Contributions段

- move_code：CONTRIBUTION

- paraphrase_cn：本文首次明确声誉静态性和归因，并提供可泛化到任意技能集的解决方案。

- rhetorical_function_cn：声明研究贡献。

- depends_on_cn：三类缺陷和框架。

- sets_up_cn：为后续设计贡献和方法论贡献划分层次。

- evidence_pointer：Section 6.1

### 54. Methodological Contributions段

- order：54

- section：6.2

- locator：Methodological Contributions段

- move_code：CONTRIBUTION

- paraphrase_cn：方法论贡献包括技能集分解、HMM结构、参数估计以及设计选择和评价指南。

- rhetorical_function_cn：把技术方案提炼为可复用方法。

- depends_on_cn：三组件设计。

- sets_up_cn：声明方法论贡献可迁移到其他情境。

- evidence_pointer：Section 6.2

### 55. 可泛化平台段

- order：55

- section：6.2

- locator：可泛化平台段

- move_code：BOUNDARY_CONDITION

- paraphrase_cn：该框架可调整到Yelp、TripAdvisor、Uber、Lyft、LinkedIn等经历三类缺陷的在线平台。

- rhetorical_function_cn：界定适用范围并推广到其他情境。

- depends_on_cn：通用设计原则。

- sets_up_cn：支持未来应用的想象。

- evidence_pointer：Section 6.2

### 56. 平台和交易段

- order：56

- section：6.3

- locator：平台和交易段

- move_code：CONTRIBUTION

- paraphrase_cn：准确的声誉分数帮助工人区分、雇主决策、市场改进推荐算法；预测非完美工人可支持提前干预。

- rhetorical_function_cn：把技术改进转化为平台和参与者价值。

- depends_on_cn：评价结果。

- sets_up_cn：为结论中的未来工作含义铺垫。

- evidence_pointer：Section 6.3

### 57. 离散状态讨论段

- order：57

- section：6.4

- locator：离散状态讨论段

- move_code：LIMITATION_AND_FUTURE

- paraphrase_cn：框架假设隐藏状态离散，但输出连续分数；连续状态空间模型不保证更好，也可能增加管理解释难度。

- rhetorical_function_cn：承认建模假设的局限并给出理由。

- depends_on_cn：HMM设计。

- sets_up_cn：为未来研究提出方向。

- evidence_pointer：Section 6.4

### 58. 降级转移段

- order：58

- section：6.4

- locator：降级转移段

- move_code：MECHANISM

- paraphrase_cn：允许工人转移到更低质量状态看似不合理，但用新反馈修正早期高估是必要的。

- rhetorical_function_cn：解释一个反直觉设计选择。

- depends_on_cn：多项logit转移函数。

- sets_up_cn：为开放式状态转移设计提供辩护。

- evidence_pointer：Section 6.4, Online Appendix I

### 59. W2V vs D2V边界段

- order：59

- section：6.4

- locator：W2V vs D2V边界段

- move_code：BOUNDARY_CONDITION

- paraphrase_cn：W2V更适合结构化且每个词项信息重要的情境，D2V更适合非结构化文本情境。

- rhetorical_function_cn：界定组件选择的适用条件。

- depends_on_cn：劳动市场和餐馆情境的结果差异。

- sets_up_cn：避免让读者误以为W2V总是更好。

- evidence_pointer：Section 6.4

### 60. Conclusion段

- order：60

- section：6.5

- locator：Conclusion段

- move_code：CONTRIBUTION

- paraphrase_cn：总结IA框架解决三类缺陷，在两个情境中提供准确服务评估，可能对工人、雇主、企业和未来工作产生重要影响。

- rhetorical_function_cn：为全文收束。

- depends_on_cn：全部研究。

- sets_up_cn：强化文章的整体贡献。

- evidence_pointer：Section 6.5

## 写作技术

- gap_construction_cn：不是简单说“没人研究”，而是命名三个具体缺陷（膨胀、归因、静态性），并用表1/表2对所有现有系统逐项打叉，使缺口可见；再用模型无关证据证明缺陷真实存在于数据中。

- signposting_cn：引言末尾预告三原则和三组件；每节标题用标签化术语（Component A/B/C）；5.3按四个评价目标分小段；5.4明确说“先检验适配，再展示协作”；讨论中重复三原则并逐项对应。

- transition_logic_cn：从研究背景到设计：“这些缺陷需要替代系统”；从设计到数据：“为了构建和评价，先用数据证明缺陷”；从主基准到推荐系统：“如果只是替代声誉系统呢？推荐系统能否解决？”；从评价到讨论：“结果如何返回设计原则”。

- claim_evidence_rhythm_cn：每个小标题先提出评价目标，再给指标定义，然后呈现图和显著性，最后一句话把结果拉回原缺陷；重要结果在摘要、引言、结果和讨论中多次重复但逐级加深。

- benchmark_narrative_cn：把基准嵌入论证：先定义三类现有系统，再逐一排除；表1/2作为“缺口的可视化”；第5节先选最优配置，再与多个先进ML和WorkerRank比较，再与推荐系统适配比较，最后在第二数据集中复制，使benchmark不只是性能表而是论证环节。

- theory_return_cn：讨论段重复“三缺陷→三组件→四表现”的结构，将实证结果重述为设计原则、方法论指南和边界条件，并把正态分布及IA概念作为理论锚点。

- contribution_positioning_cn：用“首次”、“基线”、“可推广到其他情境”三类措辞，把贡献放在设计知识和方法论指南层面，而不是单一算法性能。

- novelty_protection_cn：通过多组件消融/网格搜索、多指标、与最强替代（WorkerRank/XGB）直接比较、推荐系统适配实验和跨情境复制，防止贡献被解释为一次性调参或数据集特例；并明确边界条件（W2V vs D2V）进一步限制过度泛化。

## 可复用研究与写作程序

### structure_steps

#### 1. 1

- step：1

- writing_job_cn：建立在线市场或平台的重要性，把声誉/信任机制设为研究对象。

- research_job_cn：选择真实平台与可观测反馈数据。

- required_evidence_cn：平台规模、交易量、反馈数据可得。

- transition_to_next_cn：由机制重要性转向机制缺陷。

#### 2. 2

- step：2

- writing_job_cn：命名并分类现有系统的具体缺陷（如膨胀、归因、静态性），并用示例说明。

- research_job_cn：从数据中找模型无关证据。

- required_evidence_cn：评分分布、分技能评分差异、纵向技能获取与绩效变化。

- transition_to_next_cn：缺陷成立后，追问“现有系统是否已解决”。

#### 3. 3

- step：3

- writing_job_cn：用表格/文献综述逐项排除现有系统的适用性，切割缺口。

- research_job_cn：系统检索人类/机器/混合声誉系统、推荐系统适配。

- required_evidence_cn：能够显示“哪些系统解决/未解决哪些缺陷”的比较表。

- transition_to_next_cn：缺口清晰后，提出设计原则。

#### 4. 4

- step：4

- writing_job_cn：把每条缺陷翻译成一条设计原则，并映射到一个可实现的组件。

- research_job_cn：为每个组件选择可计算的方法并进行组件级比较。

- required_evidence_cn：组件级网格搜索或消融结果，证明所选方法优于替代。

- transition_to_next_cn：组件确定后，进入整体基准评价。

#### 5. 5

- step：5

- writing_job_cn：用多指标、多基准确立整体优势，并加入子群体与下游任务。

- research_job_cn：在固定评估协议下比较所有候选系统；训练/评估分离；报告显著性。

- required_evidence_cn：交叉验证下的排序/分布/子群体/Open内结果；与最强基线差异。

- transition_to_next_cn：主结果稳健后，测试另一个情境或下游价值。

#### 6. 6

- step：6

- writing_job_cn：讨论中把结果返回设计原则，声明设计知识、边界和未来研究。

- research_job_cn：在第二个情境复制主要实验；记录边界条件。

- required_evidence_cn：跨情境复制结果或对失败条件的讨论；明确限制适用范围。

- transition_to_next_cn：结束。

### most_transferable_moves_cn

1. 缺陷命名法：用三个可记忆标签把模糊问题变成可检验缺口

2. 缺口表：用表格逐项对照文献/系统是否解决每个缺陷

3. 模型无关证据：在建模前先用描述性图表证明现象存在

4. 组件级消融/网格搜索：证明每个设计选择都有依据

5. 多基准+子群体+下游任务：不只报告总体精度

6. 第二情境复制：用不同数据证明一般化

### resource_intensive_or_nonstandard_parts_cn

1. 私有在线劳动市场全量交易快照（58,459任务）及长期工人面板

2. 77,044条餐馆评论外部数据

3. 多个深度学习/机器学习模型的大规模网格搜索和10折交叉验证计算开销

4. HMM似然估计与参数推导（附录B/C）需要较深度建模知识

5. 在线附录中的大量补充分析

### what_not_to_copy_superficially_cn

1. 只使用“动态/多维/技能集”等词汇但没有纵向数据与技能归属映射

2. 声称“首次”但没有完整比较表或充分文献覆盖

3. 把正态分布作为设计目标但未报告分布接近程度

4. 只做总体精度提升而不做子群体与下游任务验证

5. 把离线AUC/排序提升直接写成平台收益

- single_best_description_of_the_routine_cn：把对手系统在三个命名缺陷上打靶，把缺陷翻译成三条设计原则，把原则落地成组件，用多基准、多指标、子群体、下游任务和跨领域复制证明制品更优。

## 分析边界

正文完整可读，但Online Appendices A–I只有引用没有正文内容，参数推导、附加图和具体调节表格无法直接核对；表格中的脚注部分被OCR截断；因此对附录支撑的细节判断以正文引用和图表标题为准。
