# A dynamic shipment matching problem in hinterland synchromodal transportation

- 作者：Wenjing Guo; Bilge Atasoy; Wouter Beelaerts van Blokland; Rudy R. Negenborn
- 年份 / 期刊：2020 / Decision Support Systems
- DOI：10.1016/j.dss.2020.113289
- 源文件：01518_2020_a-dynamic-shipment-matching-problem-in-hinterland-synchromodal-transportation.md
- 论文主类型：computational_artifact_benchmark
- 主导写作弧线：performance_gap_artifact_benchmark_generalize
- 置信度：0.82

## 文章级论证概况

- 核心问题：在腹地同步联运背景下，如何为一个集中式在线匹配平台设计动态的货件与运输服务匹配机制，使得实时到达的合同和现货请求能够被及时、低成本地指派给驳船、火车或卡车服务？

- 制品与设计：一个在线同步联运匹配平台：采用滚动时域方法（RHA）定期对活跃请求进行再优化，仅在请求即将到期时才最终固定匹配决策；同时开发了基于路径预生成、可行匹配预生成和二进制整数规划的三阶段启发式算法，以在每个决策时刻快速给出匹配方案。

- 客观结果：启发式算法在中小规模实例上与精确解的总成本差距可达0.00%，计算时间不超过1秒；对700以上请求的大规模实例，精确算法内存不足，而启发式可在176秒内求得与更高路径长度设置相同的解。RHA在各种需求密度、动态程度、提前期和响应时间场景下均优于贪婪方法，且优势随动态性和不确定性的增加而扩大；优化区间过短不会继续提升性能，完整目标函数能实现总成本最低。

- 核心贡献：提出了动态货件匹配（DSM）问题的形式化MILP模型；设计了滚动时域框架和预处理启发式算法；通过系统性实验验证了算法的精度、效率和动态方法的实用价值；为在线同步联运匹配平台提供了可操作的决策支持方案。

- 整篇论证链：文章从同步联运和现货市场趋势切入，指出现有研究大多基于长期合同、聚合货物流或忽略转运，缺乏面向具体请求的动态匹配模型；由此定义DSM问题并给出MILP模型；由于精确算法难以应对实际规模，提出三阶段预处理启发式算法；实验首先证明启发式在解质量和计算时间上适用，然后将其嵌入滚动时域方法，并与实践中的贪婪方法比较，显示RHA在多种动态场景下显著降低成本；最后通过目标函数和优化区间敏感性分析揭示设计参数的影响，从而完成从问题建模、算法设计到决策支持主张的完整论证。

## 类型与写作弧线判定

- 论文主类型判定：文章核心是一个计算制品——动态货件匹配问题的数学模型与启发式算法，主要证据来自数值实验和基准对比（启发式 vs 精确、RHA vs GA），而非现场部署、实地数据或理论推导，因此符合计算制品benchmark类型。

- 主导写作弧线判定：文章首先指出现有精确方法在实际规模下的性能缺口，接着构建滚定时域和启发式算法作为制品，通过多个基准实验展示性能优势，最后将结果一般化为平台设计知识（如优化区间选择、目标函数构成的影响），符合性能缺口—制品—benchmark—一般化设计知识的写作弧线。

## 研究开展程序

- study_or_phase_count：6

- 研究阶段总序列：第一阶段将实际业务抽象为数学规划问题，建立精确MILP模型；第二阶段设计三阶段预处理启发式以解决大规模求解困难；第三阶段基于欧洲腹地网络生成可复现的测试实例族；第四阶段通过与精确算法对比验证启发式解质量与速度；第五阶段将启发式嵌入滚动时域RHA，与贪婪方法GA对比，揭示动态再优化价值及其边界条件；第六阶段分析目标函数构成和优化区间长度的影响，为参数选择提供依据，最终形成从建模、算法到设计知识的完整链条。

### studies_or_phases

#### 1. 动态货件匹配问题定义与MILP建模

- order：1

- name_cn：动态货件匹配问题定义与MILP建模

- question_cn：如何用数学规划刻画平台对合同和现货请求与多种运输服务之间的匹配决策，并表达时间依赖的卡车旅行时间？

- inputs_and_setting_cn：基于文献和实际背景定义的请求集合R（合同与现货）、运输服务集合S（驳船、火车、卡车）、终端网络；五条建模假设（集中式平台、不建模拒绝、不可拆分、响应时间、卡车容量无限、确定性旅行时间）。

- designed_or_compared_object_cn：混合整数线性规划模型：目标函数包含运输、转运、存储、延误和碳税成本；约束涵盖流量守恒、容量、时间传播和时变旅行时间线性化。

- baseline_control_or_counterfactual_cn：无，这是形式化和基准定义阶段。

##### objective_metrics

1. 模型完整性

2. 约束表达

3. 小规模可解性

- analysis_method_cn：MILP建模，使用CPLEX求解器作为精确算法基础。

- main_result_cn：构建了可求解的DSM问题MILP模型，并能对少量请求的实例求出精确解。

- argumentative_role_cn：为后续所有算法和实验提供了问题定义、目标函数和约束的标准形式，也作为启发式精确性对照的基准。

- remaining_uncertainty_cn：MILP模型在大规模实例（如700个请求）上无法在可接受时间内求得可行解，甚至内存不足。

- link_to_next_phase_cn：由于精确模型的局限，引出对启发式算法的需求。

##### evidence_pointers

1. Section 3 问题描述

2. Table 1 符号表

3. Section 5.1 模型方程(1)-(29)

#### 2. 预处理启发式算法设计

- order：2

- name_cn：预处理启发式算法设计

- question_cn：如何将大规模DSM问题压缩为可快速求解的二进制整数规划？

- inputs_and_setting_cn：静态服务网络、请求特征、路径最大服务数L；算法输入为服务集合和终端集合。

- designed_or_compared_object_cn：三阶段预处理启发式：路径预生成（Algorithm 1-3）、可行匹配生成（Algorithm 4-5）、二进制整数规划BIP求解；通过调节L形成Heuristic-1到4的变体。

- baseline_control_or_counterfactual_cn：不同路径长度限制L的消融比较，以及后续与精确算法的对比。

##### objective_metrics

1. 变量数

2. 约束数

3. 计算时间

4. 目标值gap

- analysis_method_cn：算法设计与描述；通过不同L的内部比较说明路径预生成的作用。

- main_result_cn：预处理大幅压缩变量和约束数量，Heuristic-3在后续实验中的解与Heuristic-4一致，且计算时间可控。

- argumentative_role_cn：提供了在线动态决策所需的快速求解引擎，是滚动时域方法能够实际运行的技术前提。

- remaining_uncertainty_cn：启发式依赖离线预生成的路径集合，若服务动态变化或出现新路径则需要重新生成；未处理实时旅行时间随机性。

- link_to_next_phase_cn：需要实验量化其解质量和速度，确认能否嵌入动态框架。

##### evidence_pointers

1. Section 5.2

2. Algorithms 1-5

3. Table 3 变量和约束数

#### 3. 基于欧洲腹地网络的实验实例生成

- order：3

- name_cn：基于欧洲腹地网络的实验实例生成

- question_cn：如何构造具有现实意义且可复制的测试场景来检验算法与动态方法？

- inputs_and_setting_cn：10个终端（3个海港、7个内陆）和116条服务（49驳船、33火车、34卡车）；参数来自van Riessen et al.和Li et al.；规划期为一周；生成EU-n1-n2实例族。

- designed_or_compared_object_cn：多个实例族：变化请求数量、到达频率、需求/供应比、动态程度DOD、提前期、响应时间。

- baseline_control_or_counterfactual_cn：不同实例族本身作为对照场景；无外部基准。

##### objective_metrics

1. 请求数量

2. 需求供给比

3. DOD

4. 提前期

5. 响应时间

- analysis_method_cn：参数化实例生成，并公开部分数据以支持复现。

- main_result_cn：产生了覆盖不同系统条件的大规模测试实例，为算法对比提供统一实验床。

- argumentative_role_cn：支撑实验的可复现性和一定程度的外部有效性，使结果能推广到类似网络。

- remaining_uncertainty_cn：实例基于抽象网络和文献参数，并非特定公司的真实运营数据集。

- link_to_next_phase_cn：这些实例作为第四阶段及后续阶段实验的输入。

##### evidence_pointers

1. Section 6.1

2. Table 2 实验参数

3. Fig. 6 网络拓扑

4. 数据链接

#### 4. 启发式算法性能评估：与精确算法对比

- order：4

- name_cn：启发式算法性能评估：与精确算法对比

- question_cn：启发式算法相比精确算法在解质量和计算时间上表现如何？路径长度L的影响是什么？

- inputs_and_setting_cn：8组请求数量从5到1600的实例（EU-5-0到EU-1600-0）；精确算法用CPLEX；启发式用Heuristic-1到4。

- designed_or_compared_object_cn：Heuristic-L（L=1,2,3,4）与精确算法的对比；大实例中Heuristic-4作为替代基准。

- baseline_control_or_counterfactual_cn：精确算法提供最优解基准；Heuristic-4作为大实例中近似最优基准。

##### objective_metrics

1. 总成本Obj (€)

2. 计算时间CPU (s)

3. %gap

- analysis_method_cn：对比实验，计算相对gap；观察变量和约束数量缩减。

- main_result_cn：中小实例（≤30请求）精确算法可解但耗时最高5647s；Heuristic-3的gap为0.00%，CPU不超过1s；700及以上请求精确算法内存不足，Heuristic-3可在176.24s内求得与Heuristic-4相同的解。

- argumentative_role_cn：证明启发式在大规模实例上兼具精度与效率，为后续动态实验提供可信的求解器。

- remaining_uncertainty_cn：大规模实例没有真正的精确解作为对照，只能以Heuristic-4的结果为参照，无法完全排除启发式本身的系统性偏差。

- link_to_next_phase_cn：确认启发式可用后，下一步将其嵌入RHA并与实践中使用的GA比较。

##### evidence_pointers

1. Section 6.2

2. Table 3

3. Table 4

#### 5. 动态方法比较：RHA vs GA

- order：5

- name_cn：动态方法比较：RHA vs GA

- question_cn：滚动时域方法相比实践中的贪婪方法在不同动态场景下能否降低总成本？优势的边界条件是什么？

- inputs_and_setting_cn：使用Heuristic-3；优化区间h=1h；四组实验：需求密度40%-160%（EU-100-400至EU-400-1600）、DOD 25%-100%、提前期24/48/72h、响应时间1/12/24h；每组10个实例。

- designed_or_compared_object_cn：RHA与GA的对比；四个维度作为调节变量。

- baseline_control_or_counterfactual_cn：GA为实践基准。

##### objective_metrics

1. 总成本

- analysis_method_cn：分组比较并作图（Fig. 7），通过均值变化和方差观察表现。

- main_result_cn：RHA在所有组中总成本均低于GA；优势随需求密度、DOD、提前期和响应时间增大而增强；100%动态时RHA方差最大。

- argumentative_role_cn：证明动态再优化策略在在线匹配中的核心价值，同时揭示其在不同系统条件下的有效性边界。

- remaining_uncertainty_cn：只测试了h=1h，未检验不同优化区间对动态对比结论的影响；未纳入旅行时间不确定性。

- link_to_next_phase_cn：结果提出对优化区间长度和平台参数进一步分析的动机。

##### evidence_pointers

1. Section 6.3

2. Fig. 7(a)-(d)

#### 6. 目标函数与优化区间敏感性分析

- order：6

- name_cn：目标函数与优化区间敏感性分析

- question_cn：目标函数构成和RHA优化区间长度如何影响匹配决策、总成本和模式利用率？

- inputs_and_setting_cn：目标函数分析使用EU-1000-0实例，比较不同OF组合和碳税率（8、100、500、1000）；优化区间分析使用4个DOD实例（25%-100%），h从0.1到10h。

- designed_or_compared_object_cn：不同目标函数组合（仅OF1至完整总成本）；不同碳税率；不同优化区间h。

- baseline_control_or_counterfactual_cn：完整总成本目标作为默认；h=1h作为优化区间基准。

##### objective_metrics

1. 总成本

2. 各成本分量

3. 延迟TEU-h

4. 碳排放kg

5. 驳船/火车利用率

6. 卡车利用率

- analysis_method_cn：表格对比（Table 5）和折线图（Fig. 8）。

- main_result_cn：完整目标函数的总成本最低；只最小化转运/存储/延误成本会偏向卡车；碳税率提高会改变模式选择；优化区间过短（<1h）不再改善性能，高DOD下更需注意h的选取。

- argumentative_role_cn：将算法的技术优势转化为平台层面的设计知识，帮助决策者选择目标权重和再优化频率。

- remaining_uncertainty_cn：敏感性分析只在单一网络和确定性旅行时间下进行，碳税率对未来政策情景是假设性的。

- link_to_next_phase_cn：为结论中的实践建议提供依据，并指出未来在随机和动态环境下进一步验证的方向。

##### evidence_pointers

1. Section 6.4

2. Table 5

3. Fig. 8

## 各部分修辞架构

### abstract_moves

1. CONTEXT: 定义腹地多式联运与同步联运

2. PHENOMENON: 描述现货市场和数字化的趋势

3. RQ_OR_OBJECTIVE: 提出动态货件匹配问题

4. DESIGN_FEATURE: 提出滚动时域方法

5. DESIGN_FEATURE: 提出启发式算法

6. RESULT: 报告算法精度和效率，及RHA优于GA

### introduction_moves

1. CONTEXT: 介绍腹地多式联运及其复杂性

2. PRACTICAL_STAKES: 说明多式联运在成本、延误和排放上的重要性

3. PRIOR_KNOWLEDGE: 总结既有服务特征

4. CONTEXT: 引入同步联运扩展

5. PHENOMENON: 指出现货市场和数字化趋势

6. LIMITATION: 指出现有文献大多基于长期合同

7. GAP: 区分现货请求的实时性特征

8. WHY_GAP_MATTERS: 说明新趋势带来的决策复杂性

9. RQ_OR_OBJECTIVE: 提出DSM问题并说明平台

10. DESIGN_FEATURE: 描述平台角色和信息条件

11. MECHANISM: 解释容量受限导致前后决策关联

12. STUDY_OVERVIEW: 给出全文结构预告

### theory_and_knowledge_moves

1. PRIOR_KNOWLEDGE: 区分多式、同步等概念

2. PRIOR_KNOWLEDGE: 综述腹地多式联运战略和战术规划

3. PRIOR_KNOWLEDGE: 综述同步联运动态事件研究

4. LIMITATION: 指出已有同步模型忽略转运或基于聚合流

5. GAP: 提出从请求视角研究DSM问题

6. LIMITATION: 指出Mes和Iacob贪婪方法未考虑道路拥堵

7. PRIOR_KNOWLEDGE: 说明时间依赖旅行时间可纳入模型

8. LIMITATION: 对标Li et al.的receding horizon研究差距

### artifact_design_moves

1. DESIGN_FEATURE: 定义请求、服务、匹配等核心概念

2. REQUIREMENT: 给出五条建模假设

3. DESIGN_FEATURE: 描述贪婪方法流程图

4. DESIGN_FEATURE: 描述滚动时域方法流程图

5. DESIGN_FEATURE: 呈现MILP目标函数和约束

6. DESIGN_FEATURE: 解释启发式算法三阶段步骤

7. METHOD_JUSTIFICATION: 解释预处理是为了降低计算复杂度

8. DESIGN_FEATURE: 描述时间依赖旅行时间线性化技术

### evaluation_moves

1. STUDY_OVERVIEW: 预告实验部分结构

2. METHOD_JUSTIFICATION: 基于欧洲实际网络生成实例

3. BENCHMARK_OR_CONTRAST: 以精确算法和GA作为基准

4. RESULT: 报告启发式和精确算法对比结果

5. RESULT: 报告RHA vs GA四个维度结果

6. MECHANISM: 解释需求密度、DOD等对优势的影响

7. BOUNDARY_TEST: 100%动态时方差最大

8. RESULT: 目标函数敏感性表格结果

9. RESULT: 优化区间敏感性折线图结果

10. BOUNDARY_CONDITION: 优化区间低于1小时无进一步改善

### discussion_and_contribution_moves

1. CONTRIBUTION: 总结提出了问题、方法和验证

2. RESULT: 重申启发式效率和RHA优势

3. CONTRIBUTION: 将结果转化为决策支持含义

4. LIMITATION_AND_FUTURE: 指出卡车动态性、随机性、跨境网络、分布式协调等未来方向

## 理论/知识到设计的翻译

### 知识/理论基础

1. 同步联运与多式联运文献

2. 滚动时域/再优化方法（应用于拼车、包裹递送）

3. 时间依赖旅行时间建模

4. 活动基础碳排放核算

- 理论—设计耦合：none

- 耦合判定理由：文章没有从某个明确理论推导出设计假设；滚动时域方法和启发式主要来自运筹优化中的已有算法概念和问题本身的工程需求，而非理论命题驱动的设计选择。文献只用于定位缺口和解释结果，未构成前瞻性的理论到设计翻译。

- 理论到设计翻译链：由于缺乏理论指导，整体翻译链表现为：业务观察（现货市场、实时请求）→ 问题定义（DSM） → 性能缺口（精确算法不适用） → 方法选择（滚动时域和预处理启发式） → 设计实现（RHA的固定决策时点、启发式的路径预生成） → 实验对比（GA、exact） → 机制解释（RHA通过推迟决策利用未来信息）。

### mapping_table

#### 1. 1

- theory_or_knowledge_claim_cn：动态请求到达需要能够处理实时信息的在线规划方法

- mechanism_cn：周期性再优化可以推迟决策到必要时刻，利用最新信息更合理分配容量

- design_requirement_cn：需要一种能定期更新方案且不立即锁定请求的算法框架

- artifact_choice_cn：滚动时域方法RHA，仅在请求即将到期时固定决策

- evaluated_contrast_cn：RHA vs 贪婪方法GA（立即决策）

- objective_result_cn：RHA在多个动态场景下总成本更低，且优势随需求密度、DOD、提前期、响应时间增大

##### evidence_pointers

1. Section 4.2

2. Fig. 7(a)-(d)

#### 2. 2

- theory_or_knowledge_claim_cn：卡车旅行时间受道路交通拥堵影响呈现时变特征

- mechanism_cn：不同出发时间导致不同的旅行时间，影响匹配可行性和延误

- design_requirement_cn：模型必须显式表达卡车出发时间与旅行时间之间的关系

- artifact_choice_cn：对卡车服务采用分段线性时间依赖旅行时间函数，并用整数变量线性化

- evaluated_contrast_cn：作为模型内在约束，与不考虑拥堵的文献对比

- objective_result_cn：模型能够刻画拥堵影响，实验中影响匹配结果

##### evidence_pointers

1. Section 3 卡车服务描述

2. Fig. 2

3. 约束(18)-(25)

#### 3. 3

- theory_or_knowledge_claim_cn：碳排放可用活动基础方法按集装箱公里计算

- mechanism_cn：不同运输方式碳排放因子不同，碳税会改变模式选择

- design_requirement_cn：目标函数中包含碳税项以体现可持续性政策

- artifact_choice_cn：目标函数中加入ε_s q_r c^emission碳税项

- evaluated_contrast_cn：不同碳税率和不同目标函数组合的对比实验

- objective_result_cn：碳税率提高时，模型转向使用驳船/火车等低碳模式，但总成本增加

##### evidence_pointers

1. Section 5.1 目标函数

2. Table 5 案例12-14

## 评价逻辑

### evaluation_modes

1. 算法对比实验（启发式 vs 精确算法）

2. 动态方法对比实验（RHA vs GA）

3. 参数敏感性分析（目标函数构成、碳税率、优化区间长度）

- why_these_evaluations_cn：首先需要证明启发式解的质量和速度，因此与精确算法比较；其次要证明动态方法本身的价值，因此与实践中常用的贪婪方法比较；最后要检验平台设计参数的影响，因此进行目标函数和优化区间的敏感性分析，三者层层递进——只有解得快才能在动态环境下使用，只有动态再优化有效才能支持在线平台，只有参数影响可理解才能给出决策指导。

- benchmark_and_contrast_chain_cn：精确算法为启发式提供最优基准；Heuristic-4为大实例提供近似最优基准；GA为RHA提供实践基准；路径长度L的不同设置构成消融式对比；目标函数和优化区间实验则以内生比较为主。多条基准链相互衔接，使每个主张都有可参照的比较系。

### claim_evidence_ledger

#### 1. 1

- claim：启发式算法在中小实例上能达到精确解质量的0.00% gap

- evidence：Table 4，EU-5-0到EU-30-0实例，Heuristic-3的gap均为0.00%，CPU不超过1s

- status：supported

#### 2. 2

- claim：启发式算法能解决精确算法因内存不足而无法求解的大规模实例

- evidence：Table 3-4，EU-700-0及以上精确算法out of memory，Heuristic-3可在不超过176.24s内求解

- status：supported, 但大实例以Heuristic-4为参照而非最优解

#### 3. 3

- claim：RHA在总成本上优于GA

- evidence：Fig. 7(a)-(d)，所有场景组RHA均更低

- status：supported

#### 4. 4

- claim：RHA优势随需求密度、DOD、提前期、响应时间增大而增大

- evidence：Fig. 7(a)-(d)的组间趋势

- status：supported, 但未做统计显著性检验

#### 5. 5

- claim：完整目标函数能实现总成本最低

- evidence：Table 5，案例11总成本1,017,675低于其他组合

- status：supported

#### 6. 6

- claim：优化区间小于1h不会进一步改善性能

- evidence：Fig. 8，低于1h曲线趋于平缓，与最小响应时间约束有关

- status：supported, 解释合理

#### 7. 7

- claim：高碳税率会提高驳船/火车利用率

- evidence：Table 5，案例12-14从64.78%升至68.48%

- status：supported

#### 8. 8

- claim：RHA通过延迟决策更好分配稀缺容量

- evidence：Fig. 7(a)趋势及文中机制解释

- status：mechanism claim, 属合理推断而非直接观察

- internal_validity_strategy_cn：使用统一网络和参数生成实例；控制每组实例的规模、需求/供应比和DOD等变量；对每组使用10个实例以减少随机性；固定求解器、编译软件、计算环境以提高可比性。

- external_validity_strategy_cn：基于欧洲真实腹地网络拓扑（海港与内陆终端）以及文献中行业参数；生成不同需求密度、动态程度、提前期和响应时间的多组实例，覆盖多种运营条件；公开网络和数据链接以便复现。

- what_is_not_actually_tested_cn：未在真实运营平台或真实到达流上进行测试；未考虑旅行时间随机性、卡车容量动态性、多运营商博弈；假设请求不可拆分和决策集中化，这些均未在实验中被验证；大规模实例缺少真正的最优解参照。

## 贡献闭环

- technical_claim_cn：预处理启发式算法能够在保持与精确解几乎相同总成本的同时，大幅降低计算时间，使大规模实例变得可解。

- artifact_claim_cn：滚动时域方法作为一个平台决策机制，相比实践中常用的贪婪方法能显著降低总成本，且优势在动态性越高的环境中越明显。

- mechanism_claim_cn：RHA之所以更优，是因为它通过将决策推迟到请求即将到期前，利用后续到达的请求信息来更合理地分配驳船和火车等稀缺容量；而GA的即时固定决策会导致短视。

- boundary_claim_cn：该结论在需求密度高、动态程度高、提前期长、响应时间长的场景下更显著；优化区间存在一个有效下限（约1h），低于该值不会继续改善；目标函数中不同类型成本权重会改变模式选择，碳税率提高会促进低碳模式。

- reusable_design_knowledge_cn：在线同步联运匹配平台可遵循以下设计原则：使用周期性再优化延迟决策；通过离线路径预生成和可行匹配预生成来降低在线求解复杂度；优化区间设置应匹配请求的最小响应时间；目标函数应综合运输、转运、存储、延误和碳税以平衡多目标。

- theoretical_contribution_cn：该文不主要修正或扩展某个理论，但在运筹和决策支持层面将同步联运问题从聚合流推进到具体请求视角，并显式纳入转运、时变卡车旅行时间和碳税，为后续动态在线匹配研究提供了形式化基础。

- how_discussion_closes_intro_gap_cn：结论明确指出平台通过RHA和启发式解决了引言中提出的现货市场实时请求与多模式服务之间在线匹配的缺口；通过对网络实验的结果重述，说明所提出的方法在动态背景下有效，并呼应了引言对决策支持系统的需求。

- overclaim_or_unsupported_leaps_cn：大规模实例中启发式与Heuristic-4对比gap为0.00%，但Heuristic-4本身并非最优解，作者未讨论该参照是否可能同为局部最优；对机制（延迟决策带来的优势）的推断没有过程数据支持，属于合理的解释性推理；“优于实践中的贪婪方法”仅基于模拟中的固定参数，实践中的贪婪可能有不同的决策规则。

## 句级写作动作图谱

### 1. P1 S1

- order：1

- section：Abstract

- locator：P1 S1

- move_code：CONTEXT

- paraphrase_cn：腹地多式联运是指集装箱在深水港和内陆码头之间通过卡车、火车、驳船或组合方式运输。

- rhetorical_function_cn：建立领域背景，让不熟悉交通物流的读者理解研究对象。

- depends_on_cn：无，开篇定义。

- sets_up_cn：为随后引入同步联运和动态问题提供基线概念。

- evidence_pointer：Abstract第一句

### 2. P1 S2

- order：2

- section：Abstract

- locator：P1 S2

- move_code：CONTEXT

- paraphrase_cn：同步联运是多式联运的扩展，指利用实时信息动态更新运输计划。

- rhetorical_function_cn：给出同步联运的定义，突出动态信息这一关键要素。

- depends_on_cn：依赖前一句对多式联运的理解。

- sets_up_cn：引出文章的核心问题域——动态运输计划。

- evidence_pointer：Abstract第二句

### 3. P1 S3

- order：3

- section：Abstract

- locator：P1 S3

- move_code：PHENOMENON

- paraphrase_cn：现货市场和数字化趋势使得在线同步联运问题日益出现。

- rhetorical_function_cn：点明现实背景中的新变化，说明为什么现在需要研究动态匹配。

- depends_on_cn：基于同步联运的定义。

- sets_up_cn：为后面强调现有研究大多基于长期合同做铺垫。

- evidence_pointer：Abstract第三句

### 4. P1 S4

- order：4

- section：Abstract

- locator：P1 S4

- move_code：RQ_OR_OBJECTIVE

- paraphrase_cn：研究一个集中式平台对货件请求和运输服务进行在线匹配的动态匹配问题。

- rhetorical_function_cn：明确研究问题和平台角色。

- depends_on_cn：前文的背景和趋势。

- sets_up_cn：为后续方法简介给出问题框架。

- evidence_pointer：Abstract第四句

### 5. P1 S5

- order：5

- section：Abstract

- locator：P1 S5

- move_code：DESIGN_FEATURE

- paraphrase_cn：提出滚动时域方法处理新到达请求，并开发启发式算法在决策时刻快速生成方案。

- rhetorical_function_cn：预告论文的两个核心方法贡献。

- depends_on_cn：问题定义。

- sets_up_cn：结果陈述将围绕这两个方法展开。

- evidence_pointer：Abstract第五句

### 6. P1 S6

- order：6

- section：Abstract

- locator：P1 S6

- move_code：RESULT

- paraphrase_cn：实验表明启发式算法相比精确算法在解质量和计算效率上表现良好，滚动时域方法相比实践中的贪婪方法在多种场景下降低了总成本。

- rhetorical_function_cn：概括核心实证发现，让读者快速了解价值。

- depends_on_cn：方法设计。

- sets_up_cn：为正文详细结果作预告。

- evidence_pointer：Abstract最后一句

### 7. P1 S1

- order：7

- section：1. Introduction

- locator：P1 S1

- move_code：CONTEXT

- paraphrase_cn：腹地多式联运是集装箱在深水港与内陆终端之间使用多模式组合的运输。

- rhetorical_function_cn：与摘要类似，但更详细地引入研究领域。

- depends_on_cn：无。

- sets_up_cn：定义核心研究对象。

- evidence_pointer：Section 1 P1 S1

### 8. P1 S2

- order：8

- section：1. Introduction

- locator：P1 S2

- move_code：PRACTICAL_STAKES

- paraphrase_cn：相比单一模式，多式联运通过利用模式灵活性可在成本、延误和排放上表现更好。

- rhetorical_function_cn：说明研究多式联运的现实意义和收益。

- depends_on_cn：定义。

- sets_up_cn：为后文讨论同步联运和动态决策提供价值基础。

- evidence_pointer：Section 1 P1 S2

### 9. P1 S3

- order：9

- section：1. Introduction

- locator：P1 S3

- move_code：CONTEXT

- paraphrase_cn：由于使用多种模式，多式联运系统运行非常复杂。

- rhetorical_function_cn：引入复杂性，说明需要规划支持。

- depends_on_cn：前句强调好处。

- sets_up_cn：为后续提到时间兼容性和容量约束做铺垫。

- evidence_pointer：Section 1 P1 S3

### 10. P1 S4

- order：10

- section：1. Introduction

- locator：P1 S4

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：驳船和火车通常按固定时间表运行且自由容量有限，卡车则一般不排班且旅行时间受道路交通拥堵影响。

- rhetorical_function_cn：总结已有运输服务特征，是模型约束的基础。

- depends_on_cn：多式联运背景。

- sets_up_cn：引出时间兼容性和容量限制等规划约束。

- evidence_pointer：Section 1 P1 S4

### 11. P2 S1

- order：11

- section：1. Introduction

- locator：P2 S1

- move_code：CONTEXT

- paraphrase_cn：同步联运作为多式联运的扩展，指通过融合实时信息对计划进行动态更新。

- rhetorical_function_cn：正式引入同步联运概念。

- depends_on_cn：前文的多式联运定义。

- sets_up_cn：为动态问题提供概念框架。

- evidence_pointer：Section 1 P2 S1

### 12. P2 S2

- order：12

- section：1. Introduction

- locator：P2 S2

- move_code：PHENOMENON

- paraphrase_cn：现货市场和数字化趋势增加了对在线同步联运问题的需求。

- rhetorical_function_cn：引入环境变化，说明研究动机。

- depends_on_cn：同步联运的动态定义。

- sets_up_cn：为下一句指出现有文献的局限做铺垫。

- evidence_pointer：Section 1 P2 S2

### 13. P2 S3

- order：13

- section：1. Introduction

- locator：P2 S3

- move_code：LIMITATION

- paraphrase_cn：文献中大多数研究假设集装箱货物只来自基于长期合同的大货主，这些合同请求通常固定且在计划期内已知。

- rhetorical_function_cn：指出已有研究对请求类型假设的局限。

- depends_on_cn：前文趋势。

- sets_up_cn：形成与现货市场趋势的反差。

- evidence_pointer：Section 1 P2 S3

### 14. P2 S4

- order：14

- section：1. Introduction

- locator：P2 S4

- move_code：LIMITATION

- paraphrase_cn：与合同请求不同，现货请求实时到达并要求尽快得到运输方案。

- rhetorical_function_cn：具体刻画现货请求区别于合同请求的动态特征。

- depends_on_cn：前句的合同请求假设。

- sets_up_cn：构成需要在线决策的缺口。

- evidence_pointer：Section 1 P2 S4

### 15. P2 S5

- order：15

- section：1. Introduction

- locator：P2 S5

- move_code：PHENOMENON

- paraphrase_cn：最近一些研究指出集装箱运输正出现现货市场趋势。

- rhetorical_function_cn：为现货请求的真实性提供文献支撑。

- depends_on_cn：无。

- sets_up_cn：进一步佐证引入动态问题的必要性。

- evidence_pointer：Section 1 P2 S5

### 16. P2 S6

- order：16

- section：1. Introduction

- locator：P2 S6

- move_code：WHY_GAP_MATTERS

- paraphrase_cn：这些新趋势给多式联运规划带来复杂性，凸显了对适应动态环境的决策支持系统的需求。

- rhetorical_function_cn：说明现有方法无法处理新趋势，缺口重要。

- depends_on_cn：前几句的对比。

- sets_up_cn：为本文提出动态匹配问题提供动机。

- evidence_pointer：Section 1 P2 S6

### 17. P3 S1

- order：17

- section：1. Introduction

- locator：P3 S1

- move_code：RQ_OR_OBJECTIVE

- paraphrase_cn：本文研究一个平台提供在线匹配的动态货件匹配（DSM）问题。

- rhetorical_function_cn：正式提出研究问题。

- depends_on_cn：所有前序背景和缺口。

- sets_up_cn：定义平台和问题范围。

- evidence_pointer：Section 1 P3 S1

### 18. P3 S2

- order：18

- section：1. Introduction

- locator：P3 S2

- move_code：DESIGN_FEATURE

- paraphrase_cn：考虑一个在线同步联运匹配平台，它从货主接收合同和现货请求，从承运商接收运输服务。

- rhetorical_function_cn：描述平台的角色和数据流。

- depends_on_cn：问题定义。

- sets_up_cn：为后续形式化建模提供实体关系。

- evidence_pointer：Section 1 P3 S2

### 19. P3 S3

- order：19

- section：1. Introduction

- locator：P3 S3

- move_code：DESIGN_FEATURE

- paraphrase_cn：货主是寻找运输服务的实体，承运商是提供服务的实体，网络运营商是平台所有者。

- rhetorical_function_cn：明确各参与方角色，消除歧义。

- depends_on_cn：平台描述。

- sets_up_cn：为假设中的集中式模型做铺垫。

- evidence_pointer：Section 1 P3 S3

### 20. P4 S1

- order：20

- section：1. Introduction

- locator：P4 S1

- move_code：RQ_OR_OBJECTIVE

- paraphrase_cn：平台目标是在给定计划期内最小化匹配货件请求与运输服务的总成本。

- rhetorical_function_cn：给出优化目标。

- depends_on_cn：问题描述。

- sets_up_cn：为后文目标函数建立依据。

- evidence_pointer：Section 1 P4 S1

### 21. P4 S2

- order：21

- section：1. Introduction

- locator：P4 S2

- move_code：MECHANISM

- paraphrase_cn：由于驳船和火车容量有限，当前请求的决策可能影响未来请求的决策，因此需要动态方法生成在线匹配决策。

- rhetorical_function_cn：解释为什么必须考虑动态，而非简单逐请求决策。

- depends_on_cn：容量约束。

- sets_up_cn：引出滚动时域方法。

- evidence_pointer：Section 1 P4 S2

### 22. P4 S3

- order：22

- section：1. Introduction

- locator：P4 S3

- move_code：DESIGN_FEATURE

- paraphrase_cn：设计滚动时域方法处理动态请求，并开发启发式算法以高效求解。

- rhetorical_function_cn：概述技术方案。

- depends_on_cn：动态需求。

- sets_up_cn：为第4、5节叙述做预告。

- evidence_pointer：Section 1 P4 S3

### 23. P5

- order：23

- section：1. Introduction

- locator：P5

- move_code：STUDY_OVERVIEW

- paraphrase_cn：预告后续章节结构：文献、问题描述、动态方法、优化算法、实验、结论。

- rhetorical_function_cn：提供全文路线图。

- depends_on_cn：无。

- sets_up_cn：引导读者阅读。

- evidence_pointer：Section 1 P5

### 24. P1 S1

- order：24

- section：2. Literature review

- locator：P1 S1

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：过去几十年出现了多式、同步等多种货运概念，它们之间有细微差别。

- rhetorical_function_cn：界定相关概念，避免混淆。

- depends_on_cn：背景。

- sets_up_cn：为文献分类奠定基础。

- evidence_pointer：Section 2 P1 S1

### 25. 2.1 末尾附近

- order：25

- section：2. Literature review

- locator：2.1 末尾附近

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：战术规划研究涵盖服务网络设计、容量分配、行程和频率等。

- rhetorical_function_cn：总结腹地多式联运战术规划的代表性工作。

- depends_on_cn：战略/战术分类。

- sets_up_cn：表明现有研究多为离线规划。

- evidence_pointer：Section 2.1

### 26. 2.2 P1

- order：26

- section：2. Literature review

- locator：2.2 P1

- move_code：GAP

- paraphrase_cn：多式联运侧重于离线规划，同步联运强调在线规划利用实时信息处理动态事件，如新请求到达。

- rhetorical_function_cn：将同步联运与离线规划区别开来，指出动态事件的处理是未被充分研究的部分。

- depends_on_cn：概念区分。

- sets_up_cn：为后续综述同步动态方法做铺垫。

- evidence_pointer：Section 2.2 P1

### 27. 2.2 综述后

- order：27

- section：2. Literature review

- locator：2.2 综述后

- move_code：LIMITATION

- paraphrase_cn：上述考虑多种模式的研究都没有纳入不同服务之间的转运作业。

- rhetorical_function_cn：指出已有同步联运研究的一个具体缺口。

- depends_on_cn：对多篇文献的总结。

- sets_up_cn：为提出考虑转运的请求视角模型铺垫。

- evidence_pointer：Section 2.2

### 28. 2.2 紧接

- order：28

- section：2. Literature review

- locator：2.2 紧接

- move_code：LIMITATION

- paraphrase_cn：建模转运的研究通常面向聚合集装箱流，而实践中货主希望整批货物一起运输。

- rhetorical_function_cn：进一步缩小缺口：聚合流模型不符合不拆分请求的业务需求。

- depends_on_cn：前句的转运缺口的延伸。

- sets_up_cn：为以请求为决策单位的二进制变量建模做铺垫。

- evidence_pointer：Section 2.2

### 29. 2.2 结论句

- order：29

- section：2. Literature review

- locator：2.2 结论句

- move_code：GAP

- paraphrase_cn：因此，本文从货件请求的视角研究DSM问题，决策变量指示具体请求被分配给具体服务。

- rhetorical_function_cn：明确本文的切入点。

- depends_on_cn：前两个LIMITATION。

- sets_up_cn：直接对应该文贡献。

- evidence_pointer：Section 2.2

### 30. 2.2 末尾

- order：30

- section：2. Literature review

- locator：2.2 末尾

- move_code：LIMITATION

- paraphrase_cn：Mes和Iacob提出的贪婪方法为动态请求选择最便宜的服务，但没有考虑道路交通拥堵。

- rhetorical_function_cn：点出与本文最接近的实践方法及其缺陷。

- depends_on_cn：对贪婪方法的综述。

- sets_up_cn：为本文引入时变卡车旅行时间并作为基准做铺垫。

- evidence_pointer：Section 2.2

### 31. 2.3 P1

- order：31

- section：2. Literature review

- locator：2.3 P1

- move_code：LIMITATION

- paraphrase_cn：与本文最相似的工作Li et al.采用滚动时域方法控制集装箱流，但它关注聚合流而非带时间窗的具体请求，并使用时间价值而非延误成本。

- rhetorical_function_cn：明确与最相似工作的差异，进一步界定本文贡献。

- depends_on_cn：对Li et al.的综述。

- sets_up_cn：为贡献列表提供背景。

- evidence_pointer：Section 2.3

### 32. 2.3 贡献列表

- order：32

- section：2. Literature review

- locator：2.3 贡献列表

- move_code：CONTRIBUTION

- paraphrase_cn：主要贡献：提出滚动时域方法处理新请求；开发启发式算法高效求解；通过实验评估算法性能并与实践中的贪婪方法比较。

- rhetorical_function_cn：正式列出论文贡献。

- depends_on_cn：所有文献缺口。

- sets_up_cn：为后续章节的方法和实验提供承诺。

- evidence_pointer：Section 2.3

### 33. P1-P2

- order：33

- section：3. Problem description

- locator：P1-P2

- move_code：DESIGN_FEATURE

- paraphrase_cn：每个请求包含公告时间、释放时间、起讫点、体积和延误成本，分为合同和现货两类。

- rhetorical_function_cn：形式化定义请求实体，为建模提供参数集。

- depends_on_cn：问题定义。

- sets_up_cn：对应后续约束中的时间参数。

- evidence_pointer：Section 3 请求定义

### 34. P3-P4

- order：34

- section：3. Problem description

- locator：P3-P4

- move_code：DESIGN_FEATURE

- paraphrase_cn：服务分为固定时间表的驳船/火车和出发时间灵活的卡车，卡车具有时变旅行时间。

- rhetorical_function_cn：刻画服务实体及其关键特征。

- depends_on_cn：服务集定义。

- sets_up_cn：为容量、时间窗口、时变旅行时间约束提供依据。

- evidence_pointer：Section 3 服务定义

### 35. P5

- order：35

- section：3. Problem description

- locator：P5

- move_code：REQUIREMENT

- paraphrase_cn：给出五条建模假设：集中式平台、不考虑拒绝请求、货物不可拆分、决策需在释放时间前给出、卡车容量无限、旅行时间确定性。

- rhetorical_function_cn：明确模型边界，避免不必要的复杂性。

- depends_on_cn：前面对实体和匹配的定义。

- sets_up_cn：定义了可解问题的范围，后续所有实验都在这些假设下进行。

- evidence_pointer：Section 3 假设列表

### 36. P1

- order：36

- section：4. Dynamic approaches

- locator：P1

- move_code：RQ_OR_OBJECTIVE

- paraphrase_cn：为处理动态请求，需要设计能基于动态信息更新决策的方法，本文提出RHA并以GA为基准。

- rhetorical_function_cn：设置第4节的研究子问题。

- depends_on_cn：引言中的动态需求。

- sets_up_cn：为下一段两个方法的对比定义。

- evidence_pointer：Section 4 P1

### 37. 4.1

- order：37

- section：4. Dynamic approaches

- locator：4.1

- move_code：BENCHMARK_OR_CONTRAST

- paraphrase_cn：贪婪方法是一种简单直观、在请求到达时即分配最便宜可行服务的算法，作为实践基准。

- rhetorical_function_cn：定义基准方法的决策逻辑。

- depends_on_cn：实践文献中的常用方法。

- sets_up_cn：与RHA的延迟决策形成对比。

- evidence_pointer：Section 4.1

### 38. 4.2 P1

- order：38

- section：4. Dynamic approaches

- locator：4.2 P1

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：滚动时域方法是一种周期性再优化方法，已应用于拼车和包裹递送等领域。

- rhetorical_function_cn：说明RHA不是新概念，但本研究将其应用到DSM问题。

- depends_on_cn：动态方法背景。

- sets_up_cn：为RHA在本问题的具体实现提供方法学来源。

- evidence_pointer：Section 4.2 P1

### 39. 4.2 P2

- order：39

- section：4. Dynamic approaches

- locator：4.2 P2

- move_code：MECHANISM

- paraphrase_cn：RHA在计划期内利用所有已知信息制定计划，但决策仅在必须确定时才最终固定，通过再优化纳入最新信息。

- rhetorical_function_cn：解释RHA的核心机制——延迟决策。

- depends_on_cn：RHA定义。

- sets_up_cn：为实验结果中的优势提供机制解释。

- evidence_pointer：Section 4.2 P2

### 40. 4.2 图5后

- order：40

- section：4. Dynamic approaches

- locator：4.2 图5后

- move_code：DESIGN_FEATURE

- paraphrase_cn：在每个决策时点，系统为所有活跃请求确定匹配，只有当请求的释放时间早于下一决策时点时才固定其匹配计划。

- rhetorical_function_cn：给出RHA在DSM中的具体操作规则。

- depends_on_cn：活跃请求定义。

- sets_up_cn：为实验中的优化区间参数设定做铺垫。

- evidence_pointer：Section 4.2 图5后续

### 41. 5.1 目标函数前

- order：41

- section：5. Optimization algorithms

- locator：5.1 目标函数前

- move_code：DESIGN_FEATURE

- paraphrase_cn：提出MILP模型，目标函数最小化运输、转运、存储、延误和碳税成本。

- rhetorical_function_cn：给出精确优化模型的核心。

- depends_on_cn：问题描述的符号。

- sets_up_cn：后文将比较启发式与它。

- evidence_pointer：Section 5.1

### 42. 5.1 约束解释后

- order：42

- section：5. Optimization algorithms

- locator：5.1 约束解释后

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：对碳排采用活动基础方法，因为更复杂的排放模型所需数据经常不可得。

- rhetorical_function_cn：说明选择活动碳排模型的可行性理由。

- depends_on_cn：目标函数中的碳税项。

- sets_up_cn：为实验中的碳税参数和敏感性分析提供依据。

- evidence_pointer：Section 5.1

### 43. P1

- order：43

- section：5.2

- locator：P1

- move_code：GAP

- paraphrase_cn：由于匹配问题的计算复杂度，精确算法无法为现实规模实例生成可行解。

- rhetorical_function_cn：指出需要启发式的直接原因。

- depends_on_cn：实验中发现的计算限制。

- sets_up_cn：引入预处理启发式算法。

- evidence_pointer：Section 5.2 P1

### 44. P1 后

- order：44

- section：5.2

- locator：P1 后

- move_code：DESIGN_FEATURE

- paraphrase_cn：启发式包括三步：不考虑请求特性的路径预生成、考虑请求特性的可行匹配预生成、以及二进制整数规划求最优。

- rhetorical_function_cn：概述启发式算法结构。

- depends_on_cn：计算复杂度的判断。

- sets_up_cn：为后续算法描述和实验中的L参数做铺垫。

- evidence_pointer：Section 5.2 P1

### 45. P1

- order：45

- section：6. Numerical experiments

- locator：P1

- move_code：STUDY_OVERVIEW

- paraphrase_cn：本节先评估优化算法性能，比较GA与RHA，然后研究目标函数和优化区间的影响。

- rhetorical_function_cn：预告实验部分的三层结构。

- depends_on_cn：方法部分。

- sets_up_cn：组织实验结果叙述。

- evidence_pointer：Section 6 P1

### 46. 网络描述

- order：46

- section：6.1

- locator：网络描述

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：考虑一个欧洲腹地多式联运网络，包含三个海港终端和七个内陆终端以及116条服务，以展示模型应用。

- rhetorical_function_cn：说明实验场景的来源和现实参照。

- depends_on_cn：实例生成需求。

- sets_up_cn：为后续所有实验提供统一的网络基础。

- evidence_pointer：Section 6.1 网络描述

### 47. 实例命名规则

- order：47

- section：6.1

- locator：实例命名规则

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：使用EU-n1-n2表示有n1个合同请求和n2个现货请求的实例，并通过不同到达频率生成不同规模。

- rhetorical_function_cn：说明实例族的命名和构造逻辑。

- depends_on_cn：网络和参数设置。

- sets_up_cn：为算法对比和动态实验提供实例集合。

- evidence_pointer：Section 6.1 实例命名

### 48. P1

- order：48

- section：6.2

- locator：P1

- move_code：BENCHMARK_OR_CONTRAST

- paraphrase_cn：为比较启发式与精确算法，生成8个不同请求数量的DSM实例。

- rhetorical_function_cn：建立算法对比实验的输入。

- depends_on_cn：实例生成。

- sets_up_cn：为表3表4的结果作准备。

- evidence_pointer：Section 6.2 P1

### 49. 结果总结

- order：49

- section：6.2

- locator：结果总结

- move_code：RESULT

- paraphrase_cn：小实例精确算法可解但耗时剧增；将路径最大服务数L从1增至3后，启发式与精确解差距降到0.00%，计算时间不超过1秒。

- rhetorical_function_cn：报告启发式vs精确的核心定量结果。

- depends_on_cn：实验数据。

- sets_up_cn：支撑启发式的适用性论证。

- evidence_pointer：Section 6.2 Table 4

### 50. 大实例结果

- order：50

- section：6.2

- locator：大实例结果

- move_code：RESULT

- paraphrase_cn：对于700以上请求的实例，精确算法因内存不足无法求解，而Heuristic-3能在176秒内求解，且与Heuristic-4的差距为0.00%。

- rhetorical_function_cn：报告大规模实例下启发式的可行性。

- depends_on_cn：实验数据。

- sets_up_cn：进一步证明启发式是动态环境下唯一可行的求解选项。

- evidence_pointer：Section 6.2 Table 4

### 51. 需求密度实验描述

- order：51

- section：6.3

- locator：需求密度实验描述

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：生成了需求/供应比分别为40%、80%、120%、160%的四组实例，每组包含10个实例。

- rhetorical_function_cn：说明动态对比实验的第一组设计。

- depends_on_cn：实例生成逻辑。

- sets_up_cn：为图7(a)的结果提供支撑。

- evidence_pointer：Section 6.3 需求密度

### 52. 图7(a)后

- order：52

- section：6.3

- locator：图7(a)后

- move_code：RESULT

- paraphrase_cn：RHA在所有需求密度组中均比GA总成本低，且成本降低随需求密度增加而增加。

- rhetorical_function_cn：报告第一个动态对比结果。

- depends_on_cn：数据。

- sets_up_cn：触发机制解释。

- evidence_pointer：Fig. 7(a)

### 53. 图7(a)解释

- order：53

- section：6.3

- locator：图7(a)解释

- move_code：MECHANISM

- paraphrase_cn：需求/供应比越高，请求间对有限容量竞争越激烈，RHA能更好地将稀缺的驳船和火车容量分配给可能更合适的、较晚到达的请求。

- rhetorical_function_cn：解释RHA优势来源。

- depends_on_cn：前句结果。

- sets_up_cn：为后文DOD等其他维度的结果提供一致的机制语言。

- evidence_pointer：Section 6.3 图7(a)后

### 54. DOD实验

- order：54

- section：6.3

- locator：DOD实验

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：定义动态程度DOD为现货集装箱数占总数之比，构造25%到100%的四组实例。

- rhetorical_function_cn：说明第二个实验维度的定义和取值。

- depends_on_cn：动态场景设计。

- sets_up_cn：为图7(b)结果做铺垫。

- evidence_pointer：Section 6.3 DOD

### 55. 图7(b)后

- order：55

- section：6.3

- locator：图7(b)后

- move_code：RESULT

- paraphrase_cn：RHA在所有DOD组中均优于GA，改进幅度随DOD增大而增大；完全动态时RHA的表现方差最大。

- rhetorical_function_cn：报告DOD维度结果，同时引入方差观察。

- depends_on_cn：数据。

- sets_up_cn：引出对不确定性条件下RHA表现的讨论。

- evidence_pointer：Fig. 7(b)

### 56. 提前期实验

- order：56

- section：6.3

- locator：提前期实验

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：生成提前期分别为24、48、72小时的三组实例，考察提前期对算法差异的影响。

- rhetorical_function_cn：说明第三个实验维度的构造。

- depends_on_cn：实验设计。

- sets_up_cn：为图7(c)结果做铺垫。

- evidence_pointer：Section 6.3 提前期

### 57. 图7(c)后

- order：57

- section：6.3

- locator：图7(c)后

- move_code：RESULT

- paraphrase_cn：RHA在所有提前期组均优于GA，提前期越长，成本改善越大，因为RHA有更多再优化机会。

- rhetorical_function_cn：报告提前期维度的结果和机制。

- depends_on_cn：数据。

- sets_up_cn：支持延迟决策的理论解释。

- evidence_pointer：Fig. 7(c)

### 58. 响应时间实验

- order：58

- section：6.3

- locator：响应时间实验

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：将响应时间从1小时变化到24小时，生成三组实例。

- rhetorical_function_cn：说明第四个实验维度。

- depends_on_cn：实验设计。

- sets_up_cn：为图7(d)结果做铺垫。

- evidence_pointer：Section 6.3 响应时间

### 59. 图7(d)后

- order：59

- section：6.3

- locator：图7(d)后

- move_code：RESULT

- paraphrase_cn：响应时间越长，RHA的总成本改善越好，因为它有更多时间在请求释放前更新决策。

- rhetorical_function_cn：报告响应时间维度结果。

- depends_on_cn：数据。

- sets_up_cn：为优化区间分析做铺垫，因为响应时间决定了RHA有效区间上限。

- evidence_pointer：Fig. 7(d)

### 60. 目标函数分析

- order：60

- section：6.4.1

- locator：目标函数分析

- move_code：STUDY_OVERVIEW

- paraphrase_cn：本节使用RHA和Heuristic-3研究不同目标函数和优化区间长度的影响。

- rhetorical_function_cn：预告敏感性分析的具体内容。

- depends_on_cn：动态方法验证完成。

- sets_up_cn：为平台参数设计提供建议。

- evidence_pointer：Section 6.4

### 61. Table 5后

- order：61

- section：6.4.1

- locator：Table 5后

- move_code：RESULT

- paraphrase_cn：比较不同目标函数时，总成本在包含所有要素时最低；仅最小化转运、存储或延误成本会偏向使用卡车。

- rhetorical_function_cn：报告目标函数构成的量化结果。

- depends_on_cn：表格数据。

- sets_up_cn：引出不同目标之间的权衡讨论。

- evidence_pointer：Table 5

### 62. 碳税讨论

- order：62

- section：6.4.1

- locator：碳税讨论

- move_code：RESULT

- paraphrase_cn：碳税率提高会改变匹配决策，使驳船和火车利用率上升，同时总成本增加。

- rhetorical_function_cn：报告碳税敏感性结果。

- depends_on_cn：Table 5案例12-14。

- sets_up_cn：强调碳税在可持续决策中的潜在影响。

- evidence_pointer：Table 5

### 63. 优化区间分析

- order：63

- section：6.4.2

- locator：优化区间分析

- move_code：STUDY_OVERVIEW

- paraphrase_cn：为测试优化区间长度的影响，使用4个不同DOD的实例并将h从0.1变到10小时。

- rhetorical_function_cn：引入第二个敏感性实验。

- depends_on_cn：前文动态实验。

- sets_up_cn：为Fig. 8结果做铺垫。

- evidence_pointer：Section 6.4.2

### 64. Fig. 8后

- order：64

- section：6.4.2

- locator：Fig. 8后

- move_code：RESULT

- paraphrase_cn：缩小h能让系统更快响应新信息从而改进解，尤其在高DOD时；但低于1小时不再带来收益。

- rhetorical_function_cn：报告优化区间长度的影响结果和边界。

- depends_on_cn：数据。

- sets_up_cn：为决策者提供h选择建议。

- evidence_pointer：Fig. 8

### 65. P1

- order：65

- section：7. Conclusion

- locator：P1

- move_code：CONTRIBUTION

- paraphrase_cn：本文提出并验证了在线同步联运匹配平台中的滚动时域方法和启发式算法，并在欧洲网络实验中证明其有效性。

- rhetorical_function_cn：总结论文贡献。

- depends_on_cn：全文。

- sets_up_cn：给出决策支持含义。

- evidence_pointer：Section 7 P1

### 66. P2

- order：66

- section：7. Conclusion

- locator：P2

- move_code：CONTRIBUTION

- paraphrase_cn：所提平台能帮助决策者在运输成本、延误和碳排放之间权衡，更有效地管理驳船、火车和卡车使用。

- rhetorical_function_cn：将技术结果提升为管理含义。

- depends_on_cn：实验结果。

- sets_up_cn：为未来研究过渡。

- evidence_pointer：Section 7 P2

### 67. P3

- order：67

- section：7. Conclusion

- locator：P3

- move_code：LIMITATION_AND_FUTURE

- paraphrase_cn：未来可考虑卡车服务动态性、随机旅行时间、国际和内陆综合网络、多运营商协调机制等方向。

- rhetorical_function_cn：承认局限并提出扩展方向。

- depends_on_cn：本文假设和发现。

- sets_up_cn：为后来研究提供路线图。

- evidence_pointer：Section 7 P3

## 写作技术

- gap_construction_cn：先建立两个概念层级：多式联运的离线规划与同步联运的在线规划；再通过三个逐层收窄的缺口：现有研究聚焦长期合同→缺少现货请求处理→即便考虑同步也常忽略转运或使用聚合流；最后以具体请求视角和时变卡车旅行时间作为本文独特切入点，同时将最相似的Li et al.工作作为对照凸显差异。

- signposting_cn：摘要最后一句预告实验结果；引言最后一段给出全文结构；每节开头用'In this section'说明任务；实验部分用'We first... Then...'组织三个阶段。

- transition_logic_cn：从背景到文献用'Nevertheless/However'转折；从缺口到本文贡献用'Therefore, in this paper'；从精确算法到启发式用'Due to computational complexity... Therefore'；从静态求解到动态比较用'Both of them work with Heuristic-3'；从动态比较到敏感性分析用'In this section... investigate impact'，形成明确推进。

- claim_evidence_rhythm_cn：每个核心主张先以一句话陈述，随后立即给出表格/图或具体数值；在数值后附加机制解释（如'The reason is...'），形成'主张—证据—机制'三步循环。

- benchmark_narrative_cn：通过两套基准构建论证：精确算法作为最优性基准，用于证明启发式解质量；贪婪方法作为实践基准，用于证明动态框架增量价值；同时用Heuristic-4作为大实例的近似最优基准补足缺失的对照。

- theory_return_cn：文章没有传统意义上的理论假设，但在讨论中将结果回归到平台设计知识（如优化区间与响应时间匹配）和同步联运文献中的动态概念，使结果具有超出单次实验的普遍含义。

- contribution_positioning_cn：在文献综述末尾明确列出三点贡献：问题模型、滚动时域+启发式方法论、实验验证；结论部分通过'设计、操作化和验证在线匹配平台'将贡献凝练为一个完整决策支持系统。

- novelty_protection_cn：通过与最相似工作Li et al.的差异（聚合流vs具体请求、时间价值vs延误成本）界定新颖性；通过多维度实验（需求密度、DOD、提前期、响应时间）展示通用性；通过目标函数和优化区间分析展示参数可控性，避免贡献退化为一次性性能结果。

## 可复用研究与写作程序

### structure_steps

#### 1. 1

- step：1

- writing_job_cn：在引言中描述行业趋势和现实需求，指出传统方法的静态假设局限。

- research_job_cn：从实际业务或文献中识别新现象（如现货市场）和具体痛点（实时请求无法处理）。

- required_evidence_cn：需要至少一个可验证的趋势文献或行业事实，以及现有模型无法处理的明确例子。

- transition_to_next_cn：用'因此本文研究...'引出研究问题。

#### 2. 2

- step：2

- writing_job_cn：撰写文献综述，按两个相关分支分类，并在每个分支末尾指出不足。

- research_job_cn：系统检索并总结邻近工作，找出可量化的缺口（如忽略转运、聚合流）。

- required_evidence_cn：需要覆盖主要相关文献，并明确指出至少一个未被处理的维度。

- transition_to_next_cn：用'与本文最相似的工作是...，然而...'缩小范围并引出贡献。

#### 3. 3

- step：3

- writing_job_cn：形式化定义问题：实体、参数、假设和数学规划模型。

- research_job_cn：将业务问题转化为精确定义的输入输出和约束，确保模型可实施。

- required_evidence_cn：需要完整符号表和假设列表，使后续实验可复现。

- transition_to_next_cn：用'由于问题的计算复杂度...'引出求解方法。

#### 4. 4

- step：4

- writing_job_cn：先提出精确/基准方法（如MILP），再设计高效算法并解释技术选择。

- research_job_cn：开发至少一个可求解大实例的算法，并证明其在理论或结构上的合理性。

- required_evidence_cn：需要算法伪代码和与基准方法的结构对比（如变量数、约束数）。

- transition_to_next_cn：用'为了检验...在实验中比较...'过渡到实验。

#### 5. 5

- step：5

- writing_job_cn：基于真实或现实网络生成测试实例，并说明参数来源。

- research_job_cn：构造覆盖不同条件（规模、动态度、需求密度）的实例族。

- required_evidence_cn：需要网络拓扑、参数表和实例命名规则。

- transition_to_next_cn：用'首先评估算法性能...然后比较动态方法...'预告实验结构。

#### 6. 6

- step：6

- writing_job_cn：执行算法对比实验，用gap、CPU时间等指标报告结果，并解释机制。

- research_job_cn：系统运行实验并收集性能数据；使用基准或消融对照。

- required_evidence_cn：需要可对比的quantitative结果和至少一个机制解释。

- transition_to_next_cn：用'然后，我们比较动态方法...'进入下一阶段。

#### 7. 7

- step：7

- writing_job_cn：进行参数敏感性或边界条件分析，回答'何时有效'和'如何设置参数'。

- research_job_cn：变动关键参数（目标权重、优化区间等）观察结果变化。

- required_evidence_cn：需要不同参数下的对比数据，并提炼设计规则。

- transition_to_next_cn：用'结论...未来研究...'收尾。

#### 8. 8

- step：8

- writing_job_cn：在结论中重述贡献、实践含义和局限，列出未来方向。

- research_job_cn：将技术发现上升为决策支持知识，并诚实列出未验证的部分。

- required_evidence_cn：需要与引言缺口呼应的总结，以及基于假设的边界说明。

- transition_to_next_cn：无。

### most_transferable_moves_cn

1. 从文献分类中提炼具体缺口：先综述，再逐一点出不足，最后用'因此本文...'收束

2. 双基准策略：用精确算法证明解质量，用实践基线证明增量价值

3. 分层实验设计：先验证求解器，再验证动态框架，最后检验参数敏感性

4. 机制解释放回结果处：每个quantitative结果后紧跟一个'The reason is...'，使读者理解因果

### resource_intensive_or_nonstandard_parts_cn

1. 需要真实或高保真的网络拓扑与服务数据（如欧洲网络的116条服务）

2. 需要商业求解器CPLEX和较强计算环境（8GB RAM以上用于大规模实例）

3. 实验中的大规模实例需大量运行时间和内存，尤其是精确算法对比

4. 数据公开链接和可复现实验需要额外维护

### what_not_to_copy_superficially_cn

1. 不能仅说'我们提出了RHA和启发式'而不展示与精确解或实践基线的数值对比

2. 不能忽略假设条件而宣称普适有效；大规模实例若没有真实最优解参照，需像文中那样使用Heuristic-4作为近似基准并承认

3. 不能只在讨论中宣称机制优势而不在实验设置中改变动态度或需求密度等变量

4. 碳税和优化区间的敏感性结论依赖于具体网络参数，随意套用可能误导

- single_best_description_of_the_routine_cn：从现实趋势中识别缺口→把缺口转化为精确数学模型→设计快速算法→用双基准把算法价值一步步证明出来→再通过敏感性分析把结果扩展成可操作的设计知识。

## 分析边界

全文OCR基本完整，但部分公式和算法伪代码可能存在转写错误（如部分上标下标），未获得附录或数据链接的实际内容；实验数据基于文本报告，未运行原始代码验证；对写作动作的判断基于个人对论文结构的方法论解读，可能存在不同理解。
