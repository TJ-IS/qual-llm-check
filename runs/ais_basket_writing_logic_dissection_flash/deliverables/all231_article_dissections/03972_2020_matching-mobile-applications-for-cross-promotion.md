# Matching Mobile Applications for Cross-Promotion

- 作者：Gene Moo Lee; Shu He; Joowon Lee; Andrew B. Whinston
- 年份 / 期刊：2020 / Information Systems Research
- DOI：10.1287/isre.2020.0921
- 源文件：03972_2020_matching-mobile-applications-for-cross-promotion.md
- 论文主类型：multi_method_or_multi_study_program
- 主导写作弧线：problem_theory_design_test_return
- 置信度：0.74

## 文章级论证概况

- 核心问题：在移动应用交叉推广（CP）中，如何将源应用与目标应用进行匹配，从而同时改善用户下载与下载后使用两个维度的广告效果？

- 制品与设计：一个集中式的应用匹配平台：后端持续采集应用市场公开信息和应用分析数据，用LDA主题模型构造应用相似度；前端用机器学习模型（随机森林等）预测不同源-目标匹配在下载与下载后使用上的表现，并用广义延迟接受算法等多对多匹配算法生成每日匹配方案；系统通过模拟验证不同信息层级（公开、分析、个体）和匹配算法的边际价值。

- 客观结果：随机匹配实验41,294个CP活动显示，top 1%匹配的效果是平均水平的10倍；下载率与源-目标相似度呈倒U型（最优相似度0.4–0.5），下载后使用时长与相似度正相关；DID显示CP参与显著提升目标应用排名，尤其初始排名低的应用受益更多，源应用未受替代损害；机器学习模拟中，加入分析特征和个体用户特征后，最优匹配算法比随机匹配在下载、会话时间、连接数上分别提升78%、69%、68%。

- 核心贡献：首次对交叉推广框架进行大规模实证研究；揭示用户下载阶段的多样化寻求与下载后使用阶段的一致性寻求之行为分歧；提出并模拟验证了一个基于主题模型、机器学习和延迟接受算法的应用匹配系统，证明了应用分析能力和隐私数据在提升广告效果中的价值，以及由此带来的效用-隐私权衡。

- 整篇论证链：作者从移动应用市场搜索成本和赢家通吃现象出发，把交叉推广定位为缓解该问题的新型推广机制；利用韩国广告平台提供的随机匹配实验数据，先进行无模型分析证明CP匹配质量差异巨大；然后以LDA主题相似度为核心解释变量，用多元计量模型发现下载与使用行为对相似度的不同反应；接着用DID评估CP对参与应用及市场多样性的整体影响；最后基于这些经验规律设计集中式匹配平台，用机器学习预测和匹配算法仿真验证平台在提升广告效果上的价值，并将隐私成本纳入讨论。

## 类型与写作弧线判定

- 论文主类型判定：文章包含无模型描述性比较、多模型计量经济分析、DID市场效果评估、机器学习预测建模和匹配算法仿真等多个方法论阶段；各阶段承担不同论证任务并逐步累积，最终形成从行为机制到设计知识的完整链条，因此属于多方法或多Study研究项目。

- 主导写作弧线判定：文章从市场搜索成本和赢家通吃问题出发，引入消费者多样化/一致性寻求理论解释实证发现，再据此设计集中式匹配平台，用机器学习与匹配仿真检验该设计，最后回到隐私-效用权衡和文献贡献，形成问题-理论-设计-检验-返回理论的写作弧线。

## 研究开展程序

- study_or_phase_count：6

- 研究阶段总序列：阶段1用无模型分析证明CP匹配质量差异巨大，阶段2构造LDA相似度等关键变量，阶段3用计量模型识别相似度对下载与使用的影响，阶段4用DID评估CP的整体市场效应，阶段5构建机器学习预测模型并检验数据层级价值，阶段6用匹配算法仿真验证集中式平台的系统级提升；六个阶段依次回答‘现象是否重要-如何测量-行为机制是什么-市场后果如何-可否预测-能否设计优化’。

### studies_or_phases

#### 1. 无模型渠道比较与匹配异质性分析

- order：1

- name_cn：无模型渠道比较与匹配异质性分析

- question_cn：CP与其他获取渠道相比效果如何？不同源-目标匹配之间是否存在巨大效果差异？

- inputs_and_setting_cn：IGAWorks漏斗与使用数据；679个启用分析工具的应用，137个MDA应用，128个CP目标应用；下载量、会话时长、连接数。

- designed_or_compared_object_cn：比较organic、MDA、CP三种获取渠道，以及CP中top 1%、5%、10%的源-目标匹配与平均匹配。

- baseline_control_or_counterfactual_cn：organic下载和MDA作为渠道基准；平均CP匹配作为匹配质量基准。

##### objective_metrics

1. 总下载量

2. 每应用平均下载量

3. 每用户平均会话时间

4. 连接数

- analysis_method_cn：描述性统计与分位聚合：按渠道汇总下载/使用指标，再按目标应用对源应用取top分位并计算效果。

- main_result_cn：CP每应用下载10,469次，高于MDA的3,507次和organic的9,638次；但CP用户平均会话时间仅0.203小时，远低于organic的3.643小时；top 1%匹配的效果是平均匹配的10倍，top 5%匹配优于MDA。

- argumentative_role_cn：证明CP能带来大量安装但存在严重免费搭车问题，并通过匹配异质性说明优化匹配是提升CP效果的关键方向。

- remaining_uncertainty_cn：缺少广告曝光数据，无法计算转化率；描述性比较可能受应用自选择影响；匹配效果差异的来源尚不明确。

- link_to_next_phase_cn：由‘匹配质量差异大’引出对匹配决定因素（尤其源-目标相似度）的分析，进入变量构造与计量建模。

##### evidence_pointers

1. Section 3.2

2. Table 2

3. Endnote 19/20

#### 2. 应用相似度与变量构造（LDA主题模型）

- order：2

- name_cn：应用相似度与变量构造（LDA主题模型）

- question_cn：如何用文本描述构建可解释、可扩展的源-目标应用相似度度量，并定义CP广告效果变量？

- inputs_and_setting_cn：383,896个应用元数据；95,956个应用描述；韩国三个应用商店每日排名；CP活动与用户使用记录。

- designed_or_compared_object_cn：构建LDA主题模型（K=100）、话题向量的余弦相似度topic_ij、功能多样性entropy，以及一组公开/分析层控制变量。

- baseline_control_or_counterfactual_cn：替代文本相似度方法（TF-IDF、doc2vec）作为稳健性对比；无相似度模型作为计量基准。

##### objective_metrics

1. 话题可解释性

2. 交互主题相似度

3. topic_ij与topic_sq分布

- analysis_method_cn：LDA主题建模、超参数选择（10-200主题）、人工话题标注、余弦相似度计算。

- main_result_cn：100主题模型在定量和定性上表现良好，可生成具有音乐、社交、儿童、宗教、游戏、教育、电商、工具等可解释话题；相似度取值范围为0到1。

- argumentative_role_cn：提供贯穿全文的核心解释变量和匹配平台的核心文本分析组件，使应用相似性从离散类别变为连续可计算度量。

- remaining_uncertainty_cn：主题数选择依赖主观判断；文本描述可能与实际功能存在差距；相似度仅反映描述层面的水平差异化。

- link_to_next_phase_cn：构造好的topic_ij、topic_sq和熵变量被直接用于计量模型和机器学习预测。

##### evidence_pointers

1. Section 4.3

2. Table 3

3. Online Appendix B/E

#### 3. CP匹配效果的计量经济分析

- order：3

- name_cn：CP匹配效果的计量经济分析

- question_cn：源-目标相似度如何影响下载率和下载后使用行为？

- inputs_and_setting_cn：41,294个（源应用、目标应用、日）三层观察；127个源应用、128个目标应用、约400,000用户的CP活动；LDA相似度及控制变量。

- designed_or_compared_object_cn：比较线性固定效应、Tobit、Hurdle和两阶段Heckman样本选择模型；核心解释变量为topic_ij与topic_sq。

- baseline_control_or_counterfactual_cn：不含平方项的模型、不同固定效应结构、无相似度变量的朴素设定作为参照。

##### objective_metrics

1. 下载率dn_ratio_ijt

2. 下载后会话时长sess_ijt

3. 下载后连接数conn_ijt

4. 系数显著性与边际效应

- analysis_method_cn：面板固定效应线性回归、Tobit、Hurdle、聚合Heckman两阶段模型；边际效应与总体效应可视化。

- main_result_cn：下载率与相似度呈倒U型，最优相似度约为0.4–0.5；下载后使用时长与连接数随相似度上升而单调增加；显示广告对两个阶段均有正向作用；目标应用排名正向影响效果。

- argumentative_role_cn：识别出下载与使用两个阶段相反的行为机制，为匹配系统设定不同的优化目标提供经验基础。

- remaining_uncertainty_cn：观测数据、无个体曝光信息、聚合到应用对层面；两阶段模型依赖强分布假设；相似度与效果之间仍可能受遗漏变量影响。

- link_to_next_phase_cn：‘匹配至关重要’的结论推动作者进一步考察CP对整个市场的影响，为平台设计提供宏观动力。

##### evidence_pointers

1. Section 5.2

2. Tables 4-7

3. Figure 2

#### 4. CP参与对源/目标应用及市场分布影响的DID分析

- order：4

- name_cn：CP参与对源/目标应用及市场分布影响的DID分析

- question_cn：CP参与是否改善目标应用表现、损害源应用，并缓解移动应用市场的赢家通吃现象？

- inputs_and_setting_cn：679个启用分析工具的应用；643个目标应用、615个源应用；日排名、下载量、会话时长、连接数；CP参与前后时期。

- designed_or_compared_object_cn：交错DID设计，处理组为参与CP的源/目标应用，对照组为未参与CP的分析工具应用；比较Log_rank、Top 50、Tobit三种排名模型。

- baseline_control_or_counterfactual_cn：CP参与前的同一应用作为自身前测；非CP参与的分析工具应用作为时间趋势对照。

##### objective_metrics

1. 应用排名

2. 是否进入Top 50

3. 下载量

4. 会话时长

5. 连接数

- analysis_method_cn：交错DID+应用个体固定效应+时间固定效应；截断排名用Tobit；加入before-participation平均排名的交互项。

- main_result_cn：目标应用排名显著改善，且初始排名越低的应用受益越大；源应用排名未系统性变差，源应用用户使用时长甚至增加；CP参与显著提升目标应用下载与使用。

- argumentative_role_cn：将微观匹配效应提升到市场结构层面，说明CP有助于缓解需求集中，并给予源应用开发者参与激励。

- remaining_uncertainty_cn：对照组是自选择采用分析工具的应用；观测数据无法完全排除其他同时期政策；Top 50源应用系数只在10%显著。

- link_to_next_phase_cn：市场层面的正效应说明值得构建专门平台优化匹配，促进长期生态活力。

##### evidence_pointers

1. Section 6

2. Tables 8-9

3. Online Appendix A/F

#### 5. 机器学习预测模型构建

- order：5

- name_cn：机器学习预测模型构建

- question_cn：不同信息层级（公开、分析、个体）能否准确预测CP下载和下载后使用？

- inputs_and_setting_cn：1,318,980个下载预测观察（含人工生成负样本）；26,668个下载后使用观察；前一个月用户级特征与后一个月结果作为训练/验证/测试。

- designed_or_compared_object_cn：比较Logit、Lasso、KNN、SVC、随机森林、FFNN、CNN；特征组为public、public+analytics、public+analytics+individual。

- baseline_control_or_counterfactual_cn：无特征基准（Avg_Down、Rand_Down、Avg_Sess、Avg_Sess_Src）作为随机/均值预测对照。

##### objective_metrics

1. Precision

2. Recall

3. F1

4. AUROC

5. AUPRC

6. R²

7. MAE

8. RMSE

- analysis_method_cn：监督分类与回归，交叉验证与超参数调优；对类不平衡使用AUPRC作为调参目标；五折随机分割取平均测试性能。

- main_result_cn：随机森林在下载和下载后使用预测上均最优；下载预测AUPRC从public的21.44提升至全特征的52.77；下载后使用预测只有加入个体特征才能获得较好R²（会话0.22，连接0.39），仅公开或分析特征时R²接近0。

- argumentative_role_cn：证明匹配平台需要拥有应用分析数据和个体用户数据才能实现有效预测，尤其是预测长期使用行为；同时量化隐私数据的价值。

- remaining_uncertainty_cn：负样本来自10%日活用户曝光假设；没有真实曝光数据；个体特征和结果的时序划分虽明确但仍是观测数据。

- link_to_next_phase_cn：预测模型为匹配仿真提供效用值，从而比较不同匹配算法和信息条件下的系统效果。

##### evidence_pointers

1. Section 7.2

2. Tables 11-12

#### 6. 匹配算法仿真与平台效果评估

- order：6

- name_cn：匹配算法仿真与平台效果评估

- question_cn：集中式匹配算法能否依据预测效用显著提升CP广告效果？

- inputs_and_setting_cn：基于ML预测的偏好列表；最后30天数据；源/目标应用集合；下载最大化与使用最大化两种效用设定；源应用最多匹配7个目标应用。

- designed_or_compared_object_cn：比较random_match、greedy_match、源提议DA、目标提议DA；每种算法分别使用public、public+analytics、public+analytics+individual特征训练预测模型。

- baseline_control_or_counterfactual_cn：random_match作为无信息基准；仅用public特征模拟当前行业公开信息匹配现状；全特征预测模型作为评价器。

##### objective_metrics

1. 每日总下载量

2. 每日总会话时长

3. 每日总连接数

- analysis_method_cn：在预测效用基础上运行匹配算法，再用全特征RF模型对最终匹配进行评价；聚合到日层面报告30天平均。

- main_result_cn：全特征+目标提议DA最优；与random_match相比下载提升78%、会话提升69%、连接提升68%；仅用public特征时非随机算法在下载和连接上甚至劣于随机匹配；分析特征对下载的边际提升约39%，个体特征约28%。

- argumentative_role_cn：验证了集中式信息平台的制品价值，说明分析数据和个体数据是提升匹配效率的必要条件，并暴露隐私-效用权衡。

- remaining_uncertainty_cn：仿真而非现场部署；没有真实广告曝光；配额、分成比例、负样本抽取等假设可能影响绝对数值；算法在更大市场中的表现仅做可扩展性分析。

- link_to_next_phase_cn：仿真结果支撑结论中关于平台设计、管理启示和未来拍卖/现场实验的讨论。

##### evidence_pointers

1. Section 7.3

2. Table 13

3. Online Appendix G

## 各部分修辞架构

### abstract_moves

1. 建立背景：移动应用市场成功但搜索成本高。

2. 引入CP作为新推广框架并说明研究目标。

3. 概述数据：韩国大型随机匹配实验。

4. 报告实证发现：下载多样化、使用一致性。

5. 提出匹配系统并给出仿真提升。

6. 总结隐私与效用权衡含义。

### introduction_moves

1. 建立移动应用市场背景与双边平台属性。

2. 用赢家通吃统计制造问题紧迫感。

3. 将问题归因于市场设计缺失和搜索成本。

4. 介绍CP机制、业界应用和参与者动机。

5. 指出现有研究空白。

6. 介绍数据来源与随机实验特征。

7. 概述计量模型与核心发现。

8. 概述DID市场效应。

9. 概述匹配平台设计与仿真结果。

10. 声明学术/实践贡献。

11. 给出全文路线图。

### theory_and_knowledge_moves

1. 回顾移动应用市场与移动广告文献。

2. 将CP与交叉销售、产品捆绑、推荐系统对比，突出激励与顺序消费独特性。

3. 引入一致性寻求与多样化寻求理论，说明其在数字产品中的可迁移性。

4. 把本文定位为实证补充而非纯算法/纯理论。

### artifact_design_moves

1. 定义CP广告效果三指标。

2. 说明公开特征与分析特征的依赖层级。

3. 用LDA构建应用相似度并解释选择原因。

4. 设计集中式匹配平台信息架构（后端采集+前端匹配引擎）。

5. 构建多层特征ML预测模型。

6. 设计基于延迟接受算法的多对多匹配机制。

### evaluation_moves

1. 无模型渠道比较与top匹配异质性。

2. 线性、Tobit、Hurdle、两阶段选择模型。

3. 交错DID与排名/下载/使用结果。

4. 机器学习交叉验证与特征组对比。

5. 匹配算法仿真，含随机/贪心/DA与不同特征组合。

### discussion_and_contribution_moves

1. 重述搜索成本与CP解决路径。

2. 总结三个文献流贡献：移动生态、多产品促销、定向广告。

3. 给出开发者与平台管理者的可操作建议。

4. 将个体数据收益表述为隐私成本权衡。

5. 列出数据、模型、因果层面的限制并提出现场实验等未来方向。

## 理论/知识到设计的翻译

### 知识/理论基础

1. 双边市场与搜索成本理论（Rochet/Tirole, Evans等）

2. 行为经济学/营销中的一致性寻求与多样化寻求文献（McAlister, Simonson, Oliver等）

3. 多产品促销文献：交叉销售、捆绑、推荐系统

4. 主题模型/文本挖掘（LDA、TF-IDF、doc2vec）

5. 匹配市场与延迟接受算法（Gale-Shapley, Roth）

6. 移动广告定向与隐私经济学（Rafieian & Yoganarasimhan, Marotta等）

- 理论—设计耦合：partial

- 耦合判定理由：行为理论显著影响核心假设（相似度对下载/使用的不同作用），但匹配平台的整体架构、特征分层、ML算法和延迟接受算法更多由数据可得性、工程可行性和匹配市场文献决定，并非由单一理论直接推导而来。

- 理论到设计翻译链：双边市场搜索成本理论 → CP作为降低搜索成本的市场设计 → 需要识别匹配决定因素 → 行为理论提出下载多样化/使用一致性假设 → LDA文本相似度作为操作化测量 → 计量结果揭示匹配目标冲突 → 设计集中式平台收集多层数据 → ML预测不同匹配结果 → 延迟接受算法以稳定方式实现匹配 → 仿真比较验证设计价值 → 返回隐私-效用权衡理论讨论。

### mapping_table

#### 1. 1

- theory_or_knowledge_claim_cn：消费者在同时/序列选择中会出现多样化寻求，但在实际消费中又存在一致性/惯性偏好。

- mechanism_cn：下载时对目标应用不确定性高，用户倾向于选择与源应用适度不同的应用以避免厌倦；下载后因实际体验，相似内容更符合既有偏好，故使用更久。

- design_requirement_cn：匹配目标不能只追求最大相似或最小相似；需要同时优化下载与使用两个目标。

- artifact_choice_cn：构造基于LDA的连续相似度topic_ij及其平方项，在两个结果方程中分别检验倒U和线性关系。

- evaluated_contrast_cn：topic_ij与topic_sq在下载率方程和下载后使用方程中的系数。

- objective_result_cn：下载率在相似度0.4–0.5处达到峰值；下载后使用时长/连接数随相似度上升而上升。

##### evidence_pointers

1. Section 5.2

2. Tables 4-7

3. Figure 2

#### 2. 2

- theory_or_knowledge_claim_cn：有效的匹配市场需要稳定、可执行的配对，否则参与者会偏离（Gale-Shapley/Roth）。

- mechanism_cn：若源或目标应用发现配对不稳定，可能拒绝参与或私下再匹配，损害平台长期运行。

- design_requirement_cn：匹配算法应产生稳定匹配，并考虑双方配额与偏好排序。

- artifact_choice_cn：采用广义延迟接受算法，同时提供源方提议和目标方提议版本；配额限制为每个源应用最多7个目标应用。

- evaluated_contrast_cn：random_match、greedy_match与src_da_match/tgt_da_match的仿真表现。

- objective_result_cn：目标提议DA在多数指标上略占优；与随机匹配相比全特征下提升显著。

##### evidence_pointers

1. Section 7.3.3-7.3.4

2. Table 13

#### 3. 3

- theory_or_knowledge_claim_cn：移动广告定向中，使用行为特征/用户历史数据可显著提升预测与投放效率（Rafieian & Yoganarasimhan等）。

- mechanism_cn：公开特征不足以刻画用户对目标应用的偏好；分析特征和应用内行为能捕捉使用模式，个体特征进一步异质化。

- design_requirement_cn：匹配平台应整合公开、分析、个体三层信息；同时需要权衡隐私成本。

- artifact_choice_cn：RF预测模型在public/public+analytics/public+analytics+individual三组特征上训练；仿真中用全特征模型作为评价器。

- evaluated_contrast_cn：三组特征的预测指标与匹配仿真结果。

- objective_result_cn：下载AUPRC从21.44提高到52.77；使用预测仅在含个体特征时有R²=0.22/0.39；匹配仿真中全特征DA比随机匹配提升78%下载、69%会话、68%连接。

##### evidence_pointers

1. Section 7.2

2. Tables 11-12

3. Section 7.3

4. Table 13

#### 4. 4

- theory_or_knowledge_claim_cn：文本描述可以表征产品功能与内容相似度；LDA可缓解稀疏性并提供可解释话题。

- mechanism_cn：应用描述中的词汇分布体现功能/使用场景；话题向量余弦相似度度量水平差异化。

- design_requirement_cn：需要可扩展、可解释、对稀疏文本稳健的相似度度量。

- artifact_choice_cn：用LDA在95,956个应用描述上训练K=100主题模型，构造cosine相似度topic_ij与功能多样性entropy。

- evaluated_contrast_cn：替代文本方法TF-IDF/doc2vec稳健性检验以及相似度平方项。

- objective_result_cn：相似度显著影响下载（倒U）和使用（正相关）；topic_sq显著。

##### evidence_pointers

1. Section 4.3

2. Online Appendix B/E

## 评价逻辑

### evaluation_modes

1. 无模型描述性比较

2. 固定效应线性、Tobit、Hurdle、两阶段选择模型

3. 交错DID

4. 机器学习交叉验证与超参数调优

5. 基于预测效用的匹配算法仿真

- why_these_evaluations_cn：先用描述性证据说明匹配重要性，再用计量模型识别相似度与效果的关联，用DID建立CP参与的整体后果，用ML评估预测可行性，最后用仿真比较不同算法和信息条件下的系统级效果。每一步回答前一步留下的未解决问题。

- benchmark_and_contrast_chain_cn：从渠道对比（organic/MDA/CP）、top匹配分位对比，到计量模型中的topic/平方项对比，到DID处理组/对照组对比，再到ML中naive/feature-group/algorithm对比；基准不断从描述性转向因果性再转向系统性设计评价。

### claim_evidence_ledger

#### 1. CP匹配质量差异大，top匹配远优于平均匹配。

- claim_cn：CP匹配质量差异大，top匹配远优于平均匹配。

- evidence_cn：top 1%匹配效果为平均的10倍，top 5%优于MDA；Table 2。

- evidence_strength_cn：描述性统计，无显著性检验但效应量巨大。

#### 2. 下载率与源-目标相似度呈倒U型。

- claim_cn：下载率与源-目标相似度呈倒U型。

- evidence_cn：线性、Tobit、Hurdle和两阶段模型均给出topic_ij正且topic_sq负，最优值0.4-0.5；Tables 4/7，Figure 2。

- evidence_strength_cn：跨模型稳健，但属观测关联。

#### 3. 下载后使用与源-目标相似度正相关。

- claim_cn：下载后使用与源-目标相似度正相关。

- evidence_cn：多个规格中topic_ij对会话时长和连接数正向显著；部分线性规格不显著但量级小；Tables 5-7。

- evidence_strength_cn：总体稳健，个别规格存在不显著负系数。

#### 4. CP参与显著提升目标应用排名，尤其低排名应用受益更大。

- claim_cn：CP参与显著提升目标应用排名，尤其低排名应用受益更大。

- evidence_cn：DID中after_jt显著负（Log_rank改善），after_rank_jt显著负；Table 8。

- evidence_strength_cn：DID加固定效应，但基于观测数据和自选择控制组。

#### 5. 源应用参与CP不会遭受替代损害，甚至使用增加。

- claim_cn：源应用参与CP不会遭受替代损害，甚至使用增加。

- evidence_cn：源应用排名无系统性恶化，会话时长和连接数增加；Tables 8-9。

- evidence_strength_cn：DID结果，Top50源应用系数仅在10%显著。

#### 6. 下载预测可通过公开/分析特征达到不错效果，个体特征进一步提升；下载后使用预测必须个体特征。

- claim_cn：下载预测可通过公开/分析特征达到不错效果，个体特征进一步提升；下载后使用预测必须个体特征。

- evidence_cn：下载AUPRC从21.44（public）到33.60（+analytics）到52.77（+individual）；使用预测R²仅在含个体特征时达0.22/0.39；Tables 11-12。

- evidence_strength_cn：交叉验证严格，但负样本为人工生成且无真实曝光。

#### 7. 集中式匹配算法能显著提升CP广告效果。

- claim_cn：集中式匹配算法能显著提升CP广告效果。

- evidence_cn：全特征DA比random提升78%/69%/68%下载/会话/连接；public-only时非随机算法劣于随机；Table 13。

- evidence_strength_cn：仿真证据，依赖预测模型和假设，非现场部署。

- internal_validity_strategy_cn：随机匹配实验由平台生成，减少源-目标选择性偏差；面板固定效应控制应用和时间不可观测因素；DID用非参与分析工具应用为对照，并用平行趋势检验（附录F）；两阶段模型处理下载选择对使用样本的截断。

- external_validity_strategy_cn：多个市场（Apple/Google/T Store）和大量应用/用户；与Tapjoy/AdMob平台实务类比；稳健性检验使用替代文本相似度；多种模型交叉验证；对高成本现场实验未做，用仿真探明边界。

- what_is_not_actually_tested_cn：实际的因果效应（非现场随机实验）；真实广告曝光数据下的个体层面行为；优化算法的真实部署效果；个体隐私数据泄露的经济成本没有直接实证；稳定匹配带来的长期平台参与变化未被检验。

## 贡献闭环

- technical_claim_cn：基于LDA主题相似度和机器学习预测 + 延迟接受算法可显著提升CP广告效果。

- artifact_claim_cn：集中式匹配平台的设计（后端数据采集+前端匹配引擎）能比industry public-only匹配更优。

- mechanism_claim_cn：下载决策受多样化寻求驱动，下载后使用受一致性寻求驱动；相似度在两个阶段作用相反。

- boundary_claim_cn：效果依赖分析特征和个体数据；仅在公开数据下非随机算法可能劣于随机；个体数据提高使用预测但对下载预测的相对增益较小；结果基于韩国市场2013-14数据。

- reusable_design_knowledge_cn：匹配平台应采用多层信息（公开/分析/个体）预测广告效果，优先使用稳定匹配算法，并在设计时显式权衡隐私与投放效率。

- theoretical_contribution_cn：将多样化/一致性寻求理论扩展至移动应用下载与使用的两阶段决策；展示不同决策阶段行为偏好差异；将隐私效用权衡引入CP市场设计。

- how_discussion_closes_intro_gap_cn：结论部分重申引言中提出的搜索成本和赢家通吃问题，说明CP匹配平台通过降低搜索成本、提升低排名应用曝光和源应用参与激励来缓解问题，并指出未解决的隐私权衡作为限制与未来方向。

- overclaim_or_unsupported_leaps_cn：从随机匹配实验推断消费者偏好时缺乏真实曝光数据；负样本为人工生成；仿真评价使用全特征预测模型，可能放大算法表现；DID控制组为自选择采用分析工具的应用，仍可能有选择偏差；没有现场实验验证平台实际部署效果。

## 句级写作动作图谱

### 1. Abstract S1

- order：1

- section：Abstract

- locator：Abstract S1

- move_code：CONTEXT

- paraphrase_cn：移动应用市场是最成功的软件市场之一。

- rhetorical_function_cn：开篇建立行业重要性，为后续问题铺垫。

- depends_on_cn：无。

- sets_up_cn：引出平台快速增长与搜索成本问题。

- evidence_pointer：Abstract第一句

### 2. Abstract S2

- order：2

- section：Abstract

- locator：Abstract S2

- move_code：PRACTICAL_STAKES

- paraphrase_cn：应用数量达数百万、用户达数十亿，搜索成本急剧上升，开发者难以触达合适用户，用户难以找到合适应用。

- rhetorical_function_cn：用规模数字说明问题严重性。

- depends_on_cn：依赖移动市场成功背景。

- sets_up_cn：为CP作为解决方案铺垫。

- evidence_pointer：Abstract第二句

### 3. Abstract S3

- order：3

- section：Abstract

- locator：Abstract S3

- move_code：PHENOMENON

- paraphrase_cn：交叉推广CP被引入为一种新的应用推广框架：在源应用中为目标应用做广告。

- rhetorical_function_cn：定义核心研究对象。

- depends_on_cn：搜索成本问题。

- sets_up_cn：说明本文要研究CP。

- evidence_pointer：Abstract第三句

### 4. Abstract S4

- order：4

- section：Abstract

- locator：Abstract S4

- move_code：STUDY_OVERVIEW

- paraphrase_cn：本文对源应用用户在不同目标应用上的下载和使用行为建模，用LDA构造相似度并分析影响。

- rhetorical_function_cn：概述研究设计与测量方法。

- depends_on_cn：CP定义。

- sets_up_cn：为实证结果报告做铺垫。

- evidence_pointer：Abstract第四句

### 5. Abstract S5

- order：5

- section：Abstract

- locator：Abstract S5

- move_code：RESULT

- paraphrase_cn：实证显示消费者下载时更喜欢多样化应用，但使用时更偏好相似应用，与心理学多样化寻求文献一致。

- rhetorical_function_cn：提前给出核心发现，吸引读者。

- depends_on_cn：模型与分析。

- sets_up_cn：引出匹配系统设计与隐私讨论。

- evidence_pointer：Abstract第五句

### 6. Abstract S6

- order：6

- section：Abstract

- locator：Abstract S6

- move_code：CONTRIBUTION

- paraphrase_cn：提出基于ML和广义延迟接受的匹配系统；仿真显示分析能力重要，个体数据可提高匹配效果但牺牲隐私。

- rhetorical_function_cn：总结制品与核心权衡。

- depends_on_cn：实证发现。

- sets_up_cn：给出全文贡献定位。

- evidence_pointer：Abstract最后两句

### 7. Introduction P1 S1-S2

- order：7

- section：1. Introduction

- locator：Introduction P1 S1-S2

- move_code：CONTEXT

- paraphrase_cn：移动应用市场近年非常成功，iOS和Android等平台允许第三方开发者进入市场。

- rhetorical_function_cn：建立研究领域背景。

- depends_on_cn：无。

- sets_up_cn：引出平台规模和搜索成本。

- evidence_pointer：Introduction第1段

### 8. Introduction P1 S3-S5

- order：8

- section：1. Introduction

- locator：Introduction P1 S3-S5

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：应用市场已有数百万应用、数十亿用户，作为双边平台连接开发者和用户，App Store和Google Play等提供排名、评论、评分和关键词搜索来缓解信息不对称。

- rhetorical_function_cn：陈述已有市场结构和现有机制。

- depends_on_cn：移动市场背景。

- sets_up_cn：指出即使有现有工具仍存在市场失灵。

- evidence_pointer：Introduction第1段后半

### 9. Introduction P2 S1

- order：9

- section：1. Introduction

- locator：Introduction P2 S1

- move_code：LIMITATION

- paraphrase_cn：尽管有这些功能，双边移动应用市场在双方参与者规模巨大时，若缺乏高效市场设计，搜索成本仍可能上升。

- rhetorical_function_cn：指出现有机制不足以应对市场规模。

- depends_on_cn：现有排名/评论/搜索机制。

- sets_up_cn：引出赢家通吃证据。

- evidence_pointer：Introduction第2段第1句

### 10. Introduction P2 S2-S4

- order：10

- section：1. Introduction

- locator：Introduction P2 S2-S4

- move_code：PHENOMENON

- paraphrase_cn：测量研究显示移动应用市场存在赢家通吃现象，54%收入流向2%开发者，与视频流、拍卖、零售、图书等长尾市场形成鲜明对比。

- rhetorical_function_cn：用数据制造问题紧迫性。

- depends_on_cn：搜索成本论点。

- sets_up_cn：提出市场设计缺失的后果。

- evidence_pointer：Introduction第2段中间

### 11. Introduction P3 S1

- order：11

- section：1. Introduction

- locator：Introduction P3 S1

- move_code：MECHANISM

- paraphrase_cn：作者认为缺乏高效市场设计和随之上升的搜索成本可能是应用市场需求集中的原因。

- rhetorical_function_cn：把现象归因于市场设计。

- depends_on_cn：赢家通吃证据。

- sets_up_cn：为CP作为解决方案铺垫。

- evidence_pointer：Introduction第3段第1句

### 12. Introduction P3 S2-S4

- order：12

- section：1. Introduction

- locator：Introduction P3 S2-S4

- move_code：CONTEXT

- paraphrase_cn：开发者很难在数百万应用中突出新应用，可见性依赖应用商店内部排名，消费者主要接触排名靠前的应用，排名依赖会强化需求集中。

- rhetorical_function_cn：描述现状及其强化机制。

- depends_on_cn：市场设计问题。

- sets_up_cn：说明开发者需要新推广渠道。

- evidence_pointer：Introduction第3段

### 13. Introduction P4 S1

- order：13

- section：1. Introduction

- locator：Introduction P4 S1

- move_code：PHENOMENON

- paraphrase_cn：交叉推广CP被引入为新式定向广告，目标应用暴露给正在使用源应用的用户，消费者根据其应用使用行为被定向。

- rhetorical_function_cn：引入核心概念并定义。

- depends_on_cn：现有推广渠道不足。

- sets_up_cn：解释CP机制和参与者动机。

- evidence_pointer：Introduction第4段第1句

### 14. Introduction P4 S2

- order：14

- section：1. Introduction

- locator：Introduction P4 S2

- move_code：DESIGN_FEATURE

- paraphrase_cn：CP活动通过提供源应用内可使用的应用内奖励激励用户安装和使用目标应用。

- rhetorical_function_cn：指出CP的激励设计。

- depends_on_cn：CP定义。

- sets_up_cn：作为广告效果模型的背景。

- evidence_pointer：Introduction第4段第2句

### 15. Introduction P4 S3-S4

- order：15

- section：1. Introduction

- locator：Introduction P4 S3-S4

- move_code：PRACTICAL_STAKES

- paraphrase_cn：源应用开发者可通过应用内广告变现，目标应用开发者可通过选择合适源应用触达正确用户。

- rhetorical_function_cn：说明CP对双方的实际价值。

- depends_on_cn：CP机制。

- sets_up_cn：强调匹配的重要性。

- evidence_pointer：Introduction第4段后半

### 16. Introduction P5 S1-S2

- order：16

- section：1. Introduction

- locator：Introduction P5 S1-S2

- move_code：PHENOMENON

- paraphrase_cn：CP已在业界成功实现，例如Tapjoy有超过一万个应用和5.2亿月活用户，并已与Google AdMob集成。

- rhetorical_function_cn：用行业事实支撑CP的实践可行性。

- depends_on_cn：CP概念。

- sets_up_cn：说明CP增长但研究空白。

- evidence_pointer：Introduction第5段

### 17. Introduction P5 S3

- order：17

- section：1. Introduction

- locator：Introduction P5 S3

- move_code：GAP

- paraphrase_cn：尽管CP市场持续增长，但与其它应用营销策略相比，其机制和有效性在学术和行业中都尚未被充分理解。

- rhetorical_function_cn：明确指出研究空白。

- depends_on_cn：CP业界应用。

- sets_up_cn：引出本文研究目标。

- evidence_pointer：Introduction第5段最后一句

### 18. Introduction P6 S1

- order：18

- section：1. Introduction

- locator：Introduction P6 S1

- move_code：RQ_OR_OBJECTIVE

- paraphrase_cn：本文目标是通过分析韩国移动广告平台的大型实验数据，系统理解CP推广框架。

- rhetorical_function_cn：提出研究目标。

- depends_on_cn：研究空白。

- sets_up_cn：介绍数据来源与实验特征。

- evidence_pointer：Introduction第6段第1句

### 19. Introduction P6 S2-S3

- order：19

- section：1. Introduction

- locator：Introduction P6 S2-S3

- move_code：STUDY_OVERVIEW

- paraphrase_cn：实验平台与Tapjoy类似，2013年11月至2014年5月有41,294个CP活动，涉及215个应用和约40万用户，用户下载和使用行为被跟踪。

- rhetorical_function_cn：概述数据规模和平台。

- depends_on_cn：研究目标。

- sets_up_cn：强调随机匹配这一独特优势。

- evidence_pointer：Introduction第6段

### 20. Introduction P6 S4

- order：20

- section：1. Introduction

- locator：Introduction P6 S4

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：实验的独特之处在于源和目标应用被随机匹配，使作者能够探索用户对不同应用匹配的偏好并设计匹配平台。

- rhetorical_function_cn：论证数据可信度和研究可行性。

- depends_on_cn：数据概述。

- sets_up_cn：为计量模型和平台设计提供依据。

- evidence_pointer：Introduction第6段最后一句

### 21. Introduction P7 S1

- order：21

- section：1. Introduction

- locator：Introduction P7 S1

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：作者使用线性回归、Tobit、Hurdle和两阶段模型等多种计量模型，分析源应用用户对目标应用的下载和下载后使用决策。

- rhetorical_function_cn：说明方法论多样性以增强可信度。

- depends_on_cn：随机匹配数据。

- sets_up_cn：引出核心解释变量LDA相似度。

- evidence_pointer：Introduction第7段第1句

### 22. Introduction P7 S2

- order：22

- section：1. Introduction

- locator：Introduction P7 S2

- move_code：DESIGN_FEATURE

- paraphrase_cn：模型纳入基于主题建模的新颖应用相似度度量，并控制源/目标应用特征。

- rhetorical_function_cn：介绍核心测量创新。

- depends_on_cn：计量模型设定。

- sets_up_cn：为结果报告做准备。

- evidence_pointer：Introduction第7段第2句

### 23. Introduction P7 S3-S5

- order：23

- section：1. Introduction

- locator：Introduction P7 S3-S5

- move_code：RESULT

- paraphrase_cn：实证显示源-目标匹配对CP广告效果起关键作用；用户下载时偏好不同应用（多样化寻求），但使用时在相似应用上花费更多时间（一致性寻求），这与营销和行为经济学文献一致。

- rhetorical_function_cn：提前报告核心实证发现。

- depends_on_cn：计量模型结果。

- sets_up_cn：引出DID市场分析。

- evidence_pointer：Introduction第7段

### 24. Introduction P7 S6

- order：24

- section：1. Introduction

- locator：Introduction P7 S6

- move_code：RESULT

- paraphrase_cn：DID结果显示CP能显著改善目标应用表现，尤其是最初排名较低的应用，因而可能缓解需求集中。

- rhetorical_function_cn：报告市场层面结果。

- depends_on_cn：DID分析。

- sets_up_cn：为平台设计提供市场动机。

- evidence_pointer：Introduction第7段最后一句

### 25. Introduction P8 S1

- order：25

- section：1. Introduction

- locator：Introduction P8 S1

- move_code：RQ_OR_OBJECTIVE

- paraphrase_cn：基于实证洞察，作者提出基于预测模型和匹配算法的应用匹配系统。

- rhetorical_function_cn：引入设计科学部分。

- depends_on_cn：前文实证结果。

- sets_up_cn：说明行业实践不足并展示系统。

- evidence_pointer：Introduction第8段第1句

### 26. Introduction P8 S2-S3

- order：26

- section：1. Introduction

- locator：Introduction P8 S2-S3

- move_code：GAP

- paraphrase_cn：当前行业源-目标匹配主要基于应用商店的公开信息，作者认为这种匹配可能是次优的。

- rhetorical_function_cn：指出现有实践缺陷。

- depends_on_cn：CF平台背景。

- sets_up_cn：引出机器学习不同信息层级。

- evidence_pointer：Introduction第8段中间

### 27. Introduction P8 S4-S5

- order：27

- section：1. Introduction

- locator：Introduction P8 S4-S5

- move_code：RESULT

- paraphrase_cn：交叉验证显示，仅用保护隐私的应用特征即可构建准确下载预测，但准确的下载后使用预测需要个体用户特征；匹配仿真表明分析特征和个体数据可进一步改善广告效果。

- rhetorical_function_cn：预告核心设计与结果。

- depends_on_cn：ML和仿真。

- sets_up_cn：为隐私-效用权衡铺垫。

- evidence_pointer：Introduction第8段后半

### 28. Introduction P9 S1-S4

- order：28

- section：1. Introduction

- locator：Introduction P9 S1-S4

- move_code：CONTRIBUTION

- paraphrase_cn：本文是首个CP框架实证研究，贡献于移动应用市场、移动广告和多产品促销文献；实证显示数字产品多样化寻求行为差异；匹配平台有实践意义并可增强移动应用生态活力。

- rhetorical_function_cn：声明全文贡献。

- depends_on_cn：所有研究结果。

- sets_up_cn：为文献回顾和路线图做准备。

- evidence_pointer：Introduction第9段

### 29. Introduction P10

- order：29

- section：1. Introduction

- locator：Introduction P10

- move_code：STUDY_OVERVIEW

- paraphrase_cn：文章结构：第2节文献，第3-4节数据和变量，第5-6节实证，第7节匹配平台，第8节结论。

- rhetorical_function_cn：给出全文路线图。

- depends_on_cn：全文结构安排。

- sets_up_cn：引导读者预期。

- evidence_pointer：Introduction最后一段

### 30. Section 2.1 P1

- order：30

- section：2. Literature Review

- locator：Section 2.1 P1

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：移动应用市场文献已考察排名和特征对需求的影响，例如Carare（2012）、Ifrach & Johari（2014）、Ghose & Han（2014）、Lee & Raghu（2014）。

- rhetorical_function_cn：总结已有知识基础。

- depends_on_cn：引言中的市场背景。

- sets_up_cn：识别CP研究空白。

- evidence_pointer：Section 2.1第一段

### 31. Section 2.1 P2

- order：31

- section：2. Literature Review

- locator：Section 2.1 P2

- move_code：GAP

- paraphrase_cn：CP是相对较新的应用推广策略，尚未被实证研究；唯一相关分析论文是Guo等（2019）的奖励广告。

- rhetorical_function_cn：明确指出CP实证空白。

- depends_on_cn：已有促销文献。

- sets_up_cn：说明本文相对购买下载、搜索广告的差异。

- evidence_pointer：Section 2.1第二段

### 32. Section 2.1 P3

- order：32

- section：2. Literature Review

- locator：Section 2.1 P3

- move_code：WHY_GAP_MATTERS

- paraphrase_cn：移动定向广告文献研究位置、时间、天气、轨迹等，最近Rafieian & Yoganarasimhan研究行为特征对展示广告效果的提升；本文补上CP中不同信息层级的广告定向。

- rhetorical_function_cn：说明本文的定向广告文献增量。

- depends_on_cn：移动广告文献。

- sets_up_cn：为后文不同特征组预测提供理论框架。

- evidence_pointer：Section 2.1第三段

### 33. Section 2.2 开头和Table 1附近

- order：33

- section：2. Literature Review

- locator：Section 2.2 开头和Table 1附近

- move_code：GAP

- paraphrase_cn：CP与交叉销售、产品捆绑和推荐系统的不同在于两个独有特征：激励和顺序消费；表1总结了这些差异。

- rhetorical_function_cn：用表格建立CP相对其他多产品促销的独特性。

- depends_on_cn：多产品促销文献。

- sets_up_cn：为后续与各文献的对比提供结构。

- evidence_pointer：Section 2.2开头及Table 1

### 34. Section 2.2 交叉销售段

- order：34

- section：2. Literature Review

- locator：Section 2.2 交叉销售段

- move_code：GAP

- paraphrase_cn：交叉销售主要在同一公司内进行，CP允许多个应用发布者向他人客户推广，激励相容成为关键；且应用数量巨大，需要用文本挖掘度量相似度以解决可扩展性。

- rhetorical_function_cn：对比交叉销售并引出文本挖掘设计。

- depends_on_cn：多产品促销文献。

- sets_up_cn：为LDA相似度提供动机。

- evidence_pointer：Section 2.2交叉销售段

### 35. Section 2.2 产品捆绑段

- order：35

- section：2. Literature Review

- locator：Section 2.2 产品捆绑段

- move_code：GAP

- paraphrase_cn：CP与捆绑不同：消费者不会同时安装两个应用，得到的利益是源应用内的in-app奖励而非价格折扣。

- rhetorical_function_cn：对比捆绑，强调CP激励机制。

- depends_on_cn：捆绑文献。

- sets_up_cn：突出CP的独特价值。

- evidence_pointer：Section 2.2产品捆绑段

### 36. Section 2.2 推荐系统段

- order：36

- section：2. Literature Review

- locator：Section 2.2 推荐系统段

- move_code：GAP

- paraphrase_cn：CP与推荐系统共享内容过滤和用户行为思想，但CP存在开发者之间的合同，推荐系统中没有。

- rhetorical_function_cn：对比推荐系统，强调市场设计维度。

- depends_on_cn：推荐系统文献。

- sets_up_cn：为后文匹配算法奠定基础。

- evidence_pointer：Section 2.2推荐系统段

### 37. Section 2.3 P1

- order：37

- section：2. Literature Review

- locator：Section 2.3 P1

- move_code：THEORY_INTRO

- paraphrase_cn：营销和行为经济学文献发现消费者存在一致性和多样化两种相反行为；用户通常对产品或品牌有忠诚和稳定偏好。

- rhetorical_function_cn：引入行为理论。

- depends_on_cn：移动应用消费场景。

- sets_up_cn：为两种相反假设提供理论依据。

- evidence_pointer：Section 2.3第一段

### 38. Section 2.3 P2

- order：38

- section：2. Literature Review

- locator：Section 2.3 P2

- move_code：THEORY_INTRO

- paraphrase_cn：另一支文献显示人们受多样化动机驱动，实验室实验证明序列选择中偏好更多样化；数字商品的多样化寻求行为也被研究。

- rhetorical_function_cn：引入对立理论机制。

- depends_on_cn：上一段一致性理论。

- sets_up_cn：为下载阶段多样化假设提供依据。

- evidence_pointer：Section 2.3第二段

### 39. Section 2.3 P3

- order：39

- section：2. Literature Review

- locator：Section 2.3 P3

- move_code：GAP

- paraphrase_cn：移动应用可视为耐用品，本文贡献在于提供移动应用情境下一致性和多样化寻求存在的经验证据。

- rhetorical_function_cn：将理论文献与本文贡献连接。

- depends_on_cn：两类行为理论。

- sets_up_cn：为实证分析提供假设方向。

- evidence_pointer：Section 2.3第三段

### 40. Section 3.1 P1

- order：40

- section：3. Data

- locator：Section 3.1 P1

- move_code：CONTEXT

- paraphrase_cn：数据来自韩国领先移动广告平台IGAWorks，其产品包括Adbrix分析工具和CP/MDA变现平台。

- rhetorical_function_cn：介绍数据提供方和工具。

- depends_on_cn：研究目标。

- sets_up_cn：描述三类数据。

- evidence_pointer：Section 3.1第一段

### 41. Section 3.1 P2

- order：41

- section：3. Data

- locator：Section 3.1 P2

- move_code：STUDY_OVERVIEW

- paraphrase_cn：数据由三部分组成：383,896个应用元数据、CP/MDA漏斗数据和110万用户的详细使用数据。

- rhetorical_function_cn：概述数据结构。

- depends_on_cn：数据来源。

- sets_up_cn：说明后续变量测量基础。

- evidence_pointer：Section 3.1第二段

### 42. Section 3.2 P1-P2

- order：42

- section：3. Data

- locator：Section 3.2 P1-P2

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：作者比较organic、MDA和CP三组用户的下载和使用效果；但由于缺少广告曝光数据，无法测量转化率，只能用安装量和人均使用时间。

- rhetorical_function_cn：说明渠道比较方法及数据限制。

- depends_on_cn：数据定义。

- sets_up_cn：报告结果显示CP下载多但使用低。

- evidence_pointer：Section 3.2前两段

### 43. Section 3.2 P3

- order：43

- section：3. Data

- locator：Section 3.2 P3

- move_code：RESULT

- paraphrase_cn：CP每应用平均下载10,469次，约是MDA的3倍，甚至超过organic下载；但CP用户平均使用时长仅0.203小时，远低于organic的3.643小时，与免费搭车问题一致。

- rhetorical_function_cn：报告渠道对比核心结果。

- depends_on_cn：渠道比较方法。

- sets_up_cn：引出匹配优化必要性。

- evidence_pointer：Section 3.2及Table 2

### 44. Section 3.2 P4-P5

- order：44

- section：3. Data

- locator：Section 3.2 P4-P5

- move_code：RESULT

- paraphrase_cn：对每个目标应用按源应用划分用户，计算平均下载后使用，发现top 1%匹配比平均有效10倍，top 5%匹配优于MDA。

- rhetorical_function_cn：展示匹配质量异质性。

- depends_on_cn：CP数据。

- sets_up_cn：为研究匹配决定因素提供动力。

- evidence_pointer：Section 3.2最后两段

### 45. Section 4 引言

- order：45

- section：4. Variable Construction

- locator：Section 4 引言

- move_code：STUDY_OVERVIEW

- paraphrase_cn：本节定义广告效果因变量，并区分公开可得的应用特征和需分析工具构造的特征。

- rhetorical_function_cn：预告变量分类。

- depends_on_cn：数据结构。

- sets_up_cn：为指标和控制变量列表铺垫。

- evidence_pointer：Section 4引言和Table 3

### 46. Section 4.1

- order：46

- section：4. Variable Construction

- locator：Section 4.1

- move_code：REQUIREMENT

- paraphrase_cn：广告效果需同时考虑下载数和下载后使用，因为源应用希望下载量，目标应用希望下载和长期使用，平台也要在短期成本与长期效果间权衡。

- rhetorical_function_cn：解释为什么需要多个因变量。

- depends_on_cn：CP平台利益结构。

- sets_up_cn：为后续分别建模下载和使用做铺垫。

- evidence_pointer：Section 4.1

### 47. Section 4.3 P1

- order：47

- section：4. Variable Construction

- locator：Section 4.3 P1

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：使用应用描述比应用类别更细致，作者选择LDA而非TF-IDF或doc2vec，因为LDA克服数据稀疏、话题可解释且被广泛接受。

- rhetorical_function_cn：为文本测量选择辩护。

- depends_on_cn：文本挖掘文献。

- sets_up_cn：描述LDA训练细节。

- evidence_pointer：Section 4.3第一段

### 48. Section 4.3 P2-P5

- order：48

- section：4. Variable Construction

- locator：Section 4.3 P2-P5

- move_code：DESIGN_FEATURE

- paraphrase_cn：在95,956个应用描述上训练LDA，K=100；用话题向量余弦相似度定义topic_ij，并加入平方项以捕捉非线性。

- rhetorical_function_cn：具体说明相似度变量的构造。

- depends_on_cn：LDA方法选择。

- sets_up_cn：为计量模型中的核心解释变量提供定义。

- evidence_pointer：Section 4.3中间至结尾

### 49. Section 5 引言

- order：49

- section：5. Empirical Analysis

- locator：Section 5 引言

- move_code：RQ_OR_OBJECTIVE

- paraphrase_cn：本节用多种模型估计应用匹配和相似度对CP广告效果的影响。

- rhetorical_function_cn：交代实证分析目标。

- depends_on_cn：变量构造。

- sets_up_cn：引出模型设定。

- evidence_pointer：Section 5引言

### 50. Section 5.1

- order：50

- section：5. Empirical Analysis

- locator：Section 5.1

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：由于下载后使用变量有大量零值且下载决定和使用决定紧密相关，作者使用线性、Tobit、Hurdle和两阶段Hellman样本选择模型。

- rhetorical_function_cn：解释为什么采用四类模型。

- depends_on_cn：因变量分布和决策顺序。

- sets_up_cn：为结果表编号和解读铺路。

- evidence_pointer：Section 5.1

### 51. Section 5.2 P1

- order：51

- section：5. Empirical Analysis

- locator：Section 5.2 P1

- move_code：RESULT

- paraphrase_cn：下载率与相似度在所有规格中呈倒U型，最优值约0.4-0.5，表明用户希望下载与正在使用应用既不完全相同也不太不同的新应用。

- rhetorical_function_cn：报告下载行为核心发现。

- depends_on_cn：计量模型结果。

- sets_up_cn：将其解释为多样化寻求。

- evidence_pointer：Section 5.2及Tables 4/7

### 52. Section 5.2 P2

- order：52

- section：5. Empirical Analysis

- locator：Section 5.2 P2

- move_code：RESULT

- paraphrase_cn：下载后使用与相似度呈严格正相关，说明下载后面临确定性时，一致性寻求占主导。

- rhetorical_function_cn：报告使用行为核心发现。

- depends_on_cn：下载后使用模型结果。

- sets_up_cn：连接行为理论解释。

- evidence_pointer：Section 5.2及Tables 5-6

### 53. Section 5.2 P3 and Figure 2

- order：53

- section：5. Empirical Analysis

- locator：Section 5.2 P3 and Figure 2

- move_code：ROBUSTNESS_OR_BOUNDARY_TEST

- paraphrase_cn：通过边际效应和总体效应图，作者进一步展示相似度对下载的倒U影响和对使用时间的单调正影响。

- rhetorical_function_cn：用可视化增强结果直观性。

- depends_on_cn：回归系数。

- sets_up_cn：为后文设计匹配系统提供直观依据。

- evidence_pointer：Section 5.2和Figure 2

### 54. Section 5.3 P1

- order：54

- section：5. Empirical Analysis

- locator：Section 5.3 P1

- move_code：RESULT

- paraphrase_cn：控制变量显示，显示广告正向影响下载和使用；经验丰富的源应用开发者反而带来更低的下载和使用。

- rhetorical_function_cn：报告重要控制变量结果。

- depends_on_cn：完整模型估计。

- sets_up_cn：为排名影响解释做准备。

- evidence_pointer：Section 5.3第一段

### 55. Section 5.3 P2-P3

- order：55

- section：5. Empirical Analysis

- locator：Section 5.3 P2-P3

- move_code：ROBUSTNESS_OR_BOUNDARY_TEST

- paraphrase_cn：目标应用排名正向影响CP效果，源应用排名影响不一致，作者用活跃用户已受控和双向效应解释。

- rhetorical_function_cn：处理排名变量的不一致发现。

- depends_on_cn：控制变量结果。

- sets_up_cn：保护核心结论不被排名混淆。

- evidence_pointer：Section 5.3后两段

### 56. Section 6 P1

- order：56

- section：6. Impact on Source Apps and Market Demand Distribution

- locator：Section 6 P1

- move_code：RQ_OR_OBJECTIVE

- paraphrase_cn：作者进一步考察CP是否缓解赢家通吃，以及源应用是否承受替代损害。

- rhetorical_function_cn：提出市场层面研究问题。

- depends_on_cn：前文匹配效果。

- sets_up_cn：介绍DID设计。

- evidence_pointer：Section 6第一段

### 57. Section 6 P2

- order：57

- section：6. Impact on Source Apps and Market Demand Distribution

- locator：Section 6 P2

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：使用交错DID，以未参与CP的分析工具应用为对照，用Log_rank、Top50和Tobit处理排名上限问题，并加入事前排名交互项。

- rhetorical_function_cn：说明识别策略和处理截断的方法。

- depends_on_cn：市场层面问题。

- sets_up_cn：报告排名影响结果。

- evidence_pointer：Section 6第二段

### 58. Section 6 P3

- order：58

- section：6. Impact on Source Apps and Market Demand Distribution

- locator：Section 6 P3

- move_code：RESULT

- paraphrase_cn：目标应用参与CP后排名显著改善，初始排名低的应用受益更大；源应用排名未系统性变化；因此CP可能缓解赢家通吃。

- rhetorical_function_cn：报告市场结构核心结果。

- depends_on_cn：DID估计。

- sets_up_cn：为源应用参与提供依据。

- evidence_pointer：Section 6第三段和Table 8

### 59. Section 6 P4

- order：59

- section：6. Impact on Source Apps and Market Demand Distribution

- locator：Section 6 P4

- move_code：RESULT

- paraphrase_cn：源应用参与CP不损害其新用户获取，反而提升会话时长和连接数；目标应用下载和使用显著增加。

- rhetorical_function_cn：报告下载/使用DID结果。

- depends_on_cn：下载/使用DID估计。

- sets_up_cn：为平台双方参与激励提供证据。

- evidence_pointer：Section 6第四段和Table 9

### 60. Section 7 P1

- order：60

- section：7. Matching Platform Design

- locator：Section 7 P1

- move_code：REQUIREMENT

- paraphrase_cn：因为个体开发者缺少详细应用和用户级数据，作者提出由CP平台集中收集分析数据并集中匹配，而不是依赖实时竞价。

- rhetorical_function_cn：解释为何需要集中式平台。

- depends_on_cn：前面预测需求。

- sets_up_cn：描述平台信息架构。

- evidence_pointer：Section 7第一段

### 61. Section 7.1

- order：61

- section：7. Matching Platform Design

- locator：Section 7.1

- move_code：DESIGN_FEATURE

- paraphrase_cn：平台分为后端和前端：后端采集公开数据和分析数据并训练主题模型与ML模型，前端用延迟接受算法生成每日匹配。

- rhetorical_function_cn：给出制品架构。

- depends_on_cn：集中式平台论证。

- sets_up_cn：为ML预测和匹配仿真做准备。

- evidence_pointer：Section 7.1和Figure 3

### 62. Section 7.2.1-7.2.2

- order：62

- section：7. Matching Platform Design

- locator：Section 7.2.1-7.2.2

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：预测单位是用户-源应用-目标应用-日；因无曝光数据，用10%日活用户随机抽样生成负样本；特征被分为公开、分析和个体三类。

- rhetorical_function_cn：说明ML设置与数据构造。

- depends_on_cn：平台设计需求。

- sets_up_cn：为预测性能比较提供基础。

- evidence_pointer：Section 7.2.1-7.2.2

### 63. Section 7.2.3

- order：63

- section：7. Matching Platform Design

- locator：Section 7.2.3

- move_code：RESULT

- paraphrase_cn：随机森林在下载预测上表现最优；加入分析和个体特征使AUPRC分别提升12%和19%。

- rhetorical_function_cn：报告下载预测关键结果。

- depends_on_cn：ML训练。

- sets_up_cn：强调分析数据价值。

- evidence_pointer：Section 7.2.3和Table 11

### 64. Section 7.2.4

- order：64

- section：7. Matching Platform Design

- locator：Section 7.2.4

- move_code：RESULT

- paraphrase_cn：下载后使用预测只有加入个体特征时才有较好R²（会话0.22、连接0.39）；公开和分析特征几乎无法预测使用。

- rhetorical_function_cn：报告使用预测关键结果。

- depends_on_cn：使用回归训练。

- sets_up_cn：讨论隐私-效用权衡。

- evidence_pointer：Section 7.2.4和Table 12

### 65. Section 7.3.1-7.3.2

- order：65

- section：7. Matching Platform Design

- locator：Section 7.3.1-7.3.2

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：仿真以预测效用构造偏好列表，考虑固定价格和收益分成两种合约，并比较不同特征组的预测模型对匹配结果的影响。

- rhetorical_function_cn：说明匹配仿真设定。

- depends_on_cn：ML预测模型。

- sets_up_cn：为算法比较提供背景。

- evidence_pointer：Section 7.3.1-7.3.2

### 66. Section 7.3.3

- order：66

- section：7. Matching Platform Design

- locator：Section 7.3.3

- move_code：BENCHMARK_OR_CONTRAST

- paraphrase_cn：使用随机匹配和贪心匹配作为基准，与源提议/目标提议的广义延迟接受算法比较。

- rhetorical_function_cn：建立仿真基准。

- depends_on_cn：效用估计。

- sets_up_cn：报告算法效果差异。

- evidence_pointer：Section 7.3.3

### 67. Section 7.3.4

- order：67

- section：7. Matching Platform Design

- locator：Section 7.3.4

- move_code：RESULT

- paraphrase_cn：全特征目标提议DA比随机匹配在下载、会话、连接上分别提升78%、69%、68%；仅公开特征时非随机算法甚至不如随机。

- rhetorical_function_cn：报告仿真核心结果。

- depends_on_cn：匹配仿真执行。

- sets_up_cn：支撑平台设计价值与数据需求。

- evidence_pointer：Section 7.3.4和Table 13

### 68. Section 8 P1

- order：68

- section：8. Concluding Remarks

- locator：Section 8 P1

- move_code：CONTRIBUTION

- paraphrase_cn：作者总结了从搜索成本、CP机制、实证行为机制到匹配平台和仿真的完整工作。

- rhetorical_function_cn：概括全文贡献链条。

- depends_on_cn：全部研究结果。

- sets_up_cn：进入学术与管理启示。

- evidence_pointer：Section 8第一段

### 69. Section 8 P2

- order：69

- section：8. Concluding Remarks

- locator：Section 8 P2

- move_code：CONTRIBUTION

- paraphrase_cn：论文贡献于移动生态、多产品促销和定向广告三个文献流，并突出CP的顺序购买、跨公司和激励特征。

- rhetorical_function_cn：正式陈述学术贡献。

- depends_on_cn：文献回顾和结果。

- sets_up_cn：为管理启示做铺垫。

- evidence_pointer：Section 8第二段

### 70. Section 8 P3

- order：70

- section：8. Concluding Remarks

- locator：Section 8 P3

- move_code：BOUNDARY_CONDITION

- paraphrase_cn：管理启示包括开发者应选择合适伙伴、平台应使用分析数据和ML改善效果，并指出隐私成本与市场效率的权衡。

- rhetorical_function_cn：把结果转化为实践指导并界定边界。

- depends_on_cn：实证与仿真结果。

- sets_up_cn：为限制与未来研究提供语境。

- evidence_pointer：Section 8第三段

### 71. Section 8 P4-P6

- order：71

- section：8. Concluding Remarks

- locator：Section 8 P4-P6

- move_code：LIMITATION_AND_FUTURE

- paraphrase_cn：限制包括缺少广告曝光数据、假设固定价格或分成、基于观测数据；未来可收集曝光数据、采用拍卖模型、开展随机现场实验。

- rhetorical_function_cn：诚实列出边界并给出后续方向。

- depends_on_cn：全文证据。

- sets_up_cn：为读者和后续研究划定适用区间。

- evidence_pointer：Section 8最后三段

## 写作技术

- gap_construction_cn：先用市场规模和赢家通吃数据制造现实紧迫性，接着指出CP已在业界大规模使用但学术空白，再通过表1将CP与交叉销售/捆绑/推荐系统比较，突出其激励+顺序消费的组合未被研究。

- signposting_cn：引言末尾给出全文路线图；每节开头说明本节目标；例如第7节开头说明‘基于实证洞察设计平台’；表1位置预告研究贡献。

- transition_logic_cn：从渠道比较到top匹配异质性，引出相似度变量；从计量结果中‘匹配至关重要’过渡到DID市场影响；从实证结论‘下载与使用偏好不同’过渡到预测模型和匹配算法。

- claim_evidence_rhythm_cn：每个主要主张常先给结果再解释机制，并在下一段补充控制变量或稳健性；例如倒U结果后立即引心理学文献；在仿真结果后解释‘仅公开特征时非随机算法不如随机’的现象。

- benchmark_narrative_cn：benchmark不只是技术指标，而是嵌入故事：用随机匹配作为无信息基准，用公开特征模拟行业现状，用DID的对照组提供信度，用naive ML模型说明特征增益。

- theory_return_cn：在结果解释处引用行为理论，在讨论中把个体数据的效果与隐私权衡联系回Rafieian/Yoganarasimhan和Marotta等的定向广告文献，从而把工程仿真上升为经济学权衡。

- contribution_positioning_cn：作者称‘首次对CP的实证研究’，同时把自己放入移动广告、多产品促销和消费者行为三个文献流，突出每个流的增量。

- novelty_protection_cn：用随机实验、多种计量规格、替代相似度、DID和仿真共同保证结果不是一次性；在最弱点（个体数据）用仿真展示边际价值并将隐私成本作为边界条件。

## 可复用研究与写作程序

### structure_steps

#### 1. 1

- step：1

- writing_job_cn：建立现实问题与市场失灵背景，用统计数据和行业案例说明紧迫性。

- research_job_cn：寻找独特数据源和随机/自然实验机会，收集市场集中度与渠道效果描述性证据。

- required_evidence_cn：市场集中度统计、行业报告、至少描述性证据显示新机制已大规模使用且匹配效果差异大。

- transition_to_next_cn：从现象到数据：说明‘要理解机制，需要大规模随机匹配数据’。

#### 2. 2

- step：2

- writing_job_cn：描述数据来源、时间、参与方；构造关键测量（如LDA相似度）与控制变量；进行无模型比较。

- research_job_cn：清洗二级数据、训练主题模型、验证构造有效性、展示匹配异质性。

- required_evidence_cn：变量分布、渠道对比表、top匹配异质性。

- transition_to_next_cn：从测量到因果/关联分析：说明需要计量模型估计相似度效应。

#### 3. 3

- step：3

- writing_job_cn：说明模型选择动机（零膨胀、选择偏差）；报告结果；连接行为理论。

- research_job_cn：估计线性/Tobit/Hurdle/两阶段模型，可视化边际效应。

- required_evidence_cn：显著且稳定的核心系数和正确的函数形状。

- transition_to_next_cn：从个体行为到市场后果：评估CP是否整体缓解需求集中。

#### 4. 4

- step：4

- writing_job_cn：建立DID设计；解释排名模型；为源应用参与提供激励理由。

- research_job_cn：交错DID、平行趋势检验、稳健性。

- required_evidence_cn：目标排名改善、低排名交互项、源应用不受损。

- transition_to_next_cn：从经验规律到系统设计：利用预测模型和算法实现匹配优化。

#### 5. 5

- step：5

- writing_job_cn：给出信息架构（后端/前端）；说明特征分层；完成ML基准。

- research_job_cn：构建特征、生成负样本、交叉验证、调参。

- required_evidence_cn：预测指标随特征组增益；个体数据对使用预测必要。

- transition_to_next_cn：从预测到匹配：把预测作为偏好效用输入。

#### 6. 6

- step：6

- writing_job_cn：定义效用函数、匹配算法、配额；报告与随机/贪心对比。

- research_job_cn：实现延迟接受算法，运行仿真，评估聚合效果。

- required_evidence_cn：仿真指标提升；隐私权衡数值。

- transition_to_next_cn：从仿真到结论：回到理论贡献和边界。

#### 7. 7

- step：7

- writing_job_cn：将结果提升为文献贡献和管理含义；诚实列出限制。

- research_job_cn：反思未检验的因果、缺失数据、扩展方向。

- required_evidence_cn：每个贡献与前述证据闭环。

- transition_to_next_cn：结束或提出后续现场实验。

### most_transferable_moves_cn

1. 用随机/自然实验数据构造‘匹配异质性’叙事

2. 用表1把新机制与已有促销机制作维度对比

3. 将行为理论嵌入两阶段决策（下载 vs 使用）

4. 用特征分层（公开/分析/个体）表达隐私-效用权衡

5. 用多个模型/基准让对方相信结果不是偶然

### resource_intensive_or_nonstandard_parts_cn

1. 来自IGAWorks的约40万用户、679应用的大规模二级数据

2. 41,294个随机匹配CP活动

3. 应用商店排名和元数据的长期爬取

4. 韩国市场与平台合作关系难以复制

5. 机器学习调参计算资源（RF/FFNN/CNN训练数小时）

### what_not_to_copy_superficially_cn

1. 如果只有公开特征，仿真表明非随机算法反而可能劣于随机匹配，因此不能在不具备分析/个体数据时宣称算法一定更优

2. 没有真实曝光数据的‘下载率’结果依赖负样本生成假设，直接复制会误导

3. DID控制组的平行趋势没有表内证据，需要额外附录检验

4. 隐私权衡不能被写成已实证的因果成本

- single_best_description_of_the_routine_cn：从真实平台随机实验出发，先描述匹配效果差异，再计量识别消费者行为机制，进而设计一个数据驱动的匹配平台，用预测+稳定匹配仿真证明其价值，最后把隐私和因果边界作为理论贡献的一部分。

## 分析边界

全文完整，但Online Appendices（A-G）和嵌入图片中的部分文字无法直接读取，精确页码未提供；LDA主题表、平行趋势检验、算法细节等在附录中，分析只能依赖正文描述；论文的某些假设（负样本生成、10%曝光率、固定分成比例）在正文中有说明但未提供额外验证，因此对仿真结果解释需谨慎。
