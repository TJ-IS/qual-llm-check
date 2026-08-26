# A collaborative decision support system for multi-criteria automatic clustering

- 作者：Mona Jabbari; Shaya Sheikh; Meysam Rabiee; Asil Oztekin
- 年份 / 期刊：2022 / Decision Support Systems
- DOI：10.1016/j.dss.2021.113671
- 源文件：19882_2022_a-collaborative-decision-support-system-for-multi-criteria-automatic-clustering.md
- 论文主类型：build_evaluate_design_science
- 主导写作弧线：performance_gap_artifact_benchmark_generalize
- 置信度：0.72

## 文章级论证概况

- 核心问题：在决策者对数据集和关注准则所知有限、同时存在多个可能冲突的聚类有效性指标时，如何构建一个可泛化的自动聚类决策支持系统，使多种进化算法协作、融入决策者偏好与质量阈值，并输出唯一的最终聚类划分？

- 制品与设计：一个六步协作式多准则自动聚类DSS：将MINLP模型与新提出的归一化乘积式聚合有效性指标结合；决策者可选择定量主VI与定性次VI、设定各VI质量阈值、选择GA/PSO/HS三种进化算法；算法离线共享最优VI值形成聚合函数；随后用非支配解筛选、输入导向CCR DEA模型得到有效解，并在多个有效解时用BWM和定性指标确定唯一最终聚类。

- 客观结果：在合成数据集（六中心480点）和PGATS高尔夫统计数据上，协作方法相比单个进化算法平均偏差改进0.75%到10.2%；生成16个非支配唯一解，DEA筛出6个有效解，BWM最终将10号聚类评为最优；敏感性分析显示BWM排序总体稳健但存在两个偏好条件会改变排序；阈值上升会减少可行解数量；与DBSCAN、Mean Shift、Affinity Propagation相比，进化算法在CS和SH上占优，在DB上合成数据占优但PGATS平均DB不如经典算法。

- 核心贡献：作者声称提出了首个具备主/次VI概念、VI阈值、协作式多进化算法、乘积式归一化聚合函数以及DEA/BWM最终评选的通用自动聚类DSS；贡献包括MINLP模型、新聚合VI、通用性与最小期望约束、协作进化算法，以及用DEA和BWM对划分进行MCDM排序。

- 整篇论证链：文章先指出自动聚类中簇数本身是决策变量，而现有有效性指标各预设几何结构、只能覆盖有限目标，难以应对多维、异质和重叠结构；接着综述多目标进化聚类选择最终解的三种路线，指出现有MOEA目标特殊、难以泛化。为了填补这一缺口，作者将问题形式化为NP-hard的MINLP，提出一个可纳入任意VI的归一化乘积式聚合目标，并设计六步DSS：选择VI与算法、设质量阈值、为各VI生成最优参数、离线协作构建聚合函数、用权重生成候选解、用DEA和BWM输出唯一解。实验先以合成数据演示完整流程，再用PGATS数据与阈值/偏好敏感性分析检验边界，最后通过与三种经典聚类算法比较说明协作进化方案的性能。结论部分回到引言的三类困境，声称框架能处理目的不匹配、信息缺乏和多准则并存，并把后续改进留作未来研究。

## 类型与写作弧线判定

- 论文主类型判定：论文的核心是开发一个DSS制品（六步协作框架与MINLP模型），并在合成数据和真实二手数据集上进行可行性演示、敏感性分析和与经典算法的比较；没有行为理论假设或现场因果实验，也没有以理论命题驱动的假设检验。因此最符合设计科学中的“需求—构建—评价—设计知识”模式。

- 主导写作弧线判定：全文从现有自动聚类有效性指标与MOEA选择方法缺乏通用性这一性能/能力缺口出发，构建协作式DSS制品，随后用合成数据、PGATS数据以及经典聚类算法对照进行benchmark式评价，最后把结果上升为可复用的框架设计知识；不是从行为理论命题推导设计，也不是以政策/机制仿真为主。

## 研究开展程序

- study_or_phase_count：5

- 研究阶段总序列：五个阶段形成累积论证：先建立正式数学模型，证明问题复杂性与模型表达力；再设计六步DSS流程，把模型变成可操作的决策支持步骤；继而在合成数据上执行完整流程，展示可行性和协作收益；随后用阈值与BWM敏感性分析划定边界；最后与经典聚类算法对比，进一步检验协作进化方案的性能边界并在结论中回到贡献主张。

### studies_or_phases

#### 1. 问题形式化与MINLP建模

- order：1

- name_cn：问题形式化与MINLP建模

- question_cn：如何把自动聚类中的多VI冲突、决策者质量期望和簇数变量统一表达为可优化模型？

- inputs_and_setting_cn：聚类问题形式化：数据集Y_I×J、簇数|K|为决策变量、可行解数量NFS公式、选定的DB/CS/SH三个VI；文献中的归一化方法NUI/NRU。

- designed_or_compared_object_cn：设计一个MINLP模型，包括新提出的归一化乘积式聚合目标函数Eq.16以及簇成员分配、激活簇数、VI阈值等约束。

- baseline_control_or_counterfactual_cn：没有直接对照模型；对比的是不同归一化方式NUI与NRU，以及传统用原始值而非归一化值的聚合思路。

##### objective_metrics

1. NFS公式体现搜索空间规模

2. 模型是否能把多个VI合并为单一可最大化分数

3. 约束是否完整表达DM质量阈值

- analysis_method_cn：数学规划建模，引用Brucker NP-hard结论，归一到0-1区间后构造乘积式目标。

- main_result_cn：得到一个可处理任意量纲VI的MINLP模型，以归一化VI的幂次乘积作为目标，并用阈值约束保证最终解不低于DM期望。

- argumentative_role_cn：为整个DSS提供形式化基础，表明问题本质是NP-hard，因此后续必须求助启发式/进化算法。

- remaining_uncertainty_cn：模型本身没有求解能力，也没有展示在可接受时间内得到实例解。

- link_to_next_phase_cn：NP-hard和大量非线性约束引出进化算法作为求解器，自然进入六步DSS设计。

##### evidence_pointers

1. Problem description开头段落与Eq.1

2. Section 2.2 NUI/NRU公式

3. Section 2.3 Eq.16与约束17-27

#### 2. 六步DSS方法论设计

- order：2

- name_cn：六步DSS方法论设计

- question_cn：如何将MINLP模型转化为一个决策者能实际使用的DSS工作流？

- inputs_and_setting_cn：DM选择的VI、距离度量、GA/PSO/HS参数、质量阈值、权重组合、定性VI（视觉紧凑度VC与视觉连通度VN）、DEA和BWM工具。

- designed_or_compared_object_cn：设计六步流程：1选VI/算法/解表示；2设质量阈值；3为聚合函数准备输入；4形成聚合函数；5准备DEA输入；6用DEA/BWM确定最终划分。

- baseline_control_or_counterfactual_cn：与引言中归纳的独立准则、膝部修剪、集成方法三类MOEA终选路线作概念对照，并用Table 2的Q1-Q7特征表证明只有本文具备全部能力。

##### objective_metrics

1. 六步流程完整性

2. 是否包含定量与定性VI、阈值、无专家依赖、Pareto前沿、聚合函数、唯一解、协作策略等七个特征

- analysis_method_cn：系统设计说明与文献对比；算法选择依据来自José-García与Gomez-Flores的调查以及GA/PSO/HS的机制描述。

- main_result_cn：形成了一套可由DM逐步执行的DSS；协作采用离线方式，各算法先单目标求解，再共享最优值构建聚合函数。

- argumentative_role_cn：把数学模型转成可操作制品，并以此支撑“框架可泛化”和“唯一解”的核心主张。

- remaining_uncertainty_cn：只是流程描述，尚无任何运行结果证明它能产出合理聚类。

- link_to_next_phase_cn：下一步必须用数据实例执行六步流程，展示每一步的输出。

##### evidence_pointers

1. Section 3 Methodology六步标题

2. Step1 a-d、Step2-Step6

3. Fig. 2 DSS示意图

#### 3. 合成数据集上的DSS完整实施

- order：3

- name_cn：合成数据集上的DSS完整实施

- question_cn：在已知结构的合成数据上，六步DSS能否产出唯一且合理的最终聚类？

- inputs_and_setting_cn：480个合成点围绕6个已知中心生成；GA/PSO/HS各跑10次；16组均匀权重重复3次；PGATS作为第二个真实数据集进入后续比较。

- designed_or_compared_object_cn：比较三种进化算法在CS、DB、SH单目标上的结果；随后把16组权重和3组重复产生144个候选，去重去支配得到非支配解集，再用CCR DEA筛选，最后用BWM排名。

- baseline_control_or_counterfactual_cn：内部基准是三种进化算法各自的结果；控制条件是已知合成数据的6个簇中心；非支配解按标准帕累托支配定义判定。

##### objective_metrics

1. 各VI单目标最优值（CS最小0.656、DB最小0.546、SH最大0.722）

2. Table 6描述统计与置信区间

3. Table 7 VI间相关系数

4. Table 8协作相对各算法的平均偏差%

5. 非支配唯一解数量16

6. DEA有效解数量6

7. BWM最终排名

- analysis_method_cn：重复运行、置信区间、相关分析、平均偏差、非支配排序、输入导向CCR DEA、BWM与Eq.28加权评分。

- main_result_cn：HS在CS/SH上表现更好，PSO在DB上稳定最好；SH与CS/DB存在正相关因而目标冲突；协作相对各算法的平均偏差为0.75%-9.60%；最终从16个非支配解中由DEA筛出6个有效解，BWM把10号聚类排为最优。

- argumentative_role_cn：这是全文主要可行性证据，证明模型、协作、DEA和BWM能够串联成一个可运行系统并输出唯一解。

- remaining_uncertainty_cn：只在一个合成数据集和一个真实数据集上展示；没有真实DM参与主观评分；没有与其它聚合函数或DSS框架统计比较。

- link_to_next_phase_cn：合成数据成功之后，需要用敏感性分析回答“结果是否依赖DM偏好与阈值”，用经典算法对比回答“协作进化是否真的更优”。

##### evidence_pointers

1. Section 4.1 Steps 1-6

2. Tables 5-12

3. Appendix Tables A.1-A.6

4. Fig. 4六个有效聚类可视化

#### 4. BWM偏好与质量阈值的敏感性分析

- order：4

- name_cn：BWM偏好与质量阈值的敏感性分析

- question_cn：最终排序和候选解集合对DM偏好变化与质量阈值是否稳健？

- inputs_and_setting_cn：BWM中4个定量VI与2个定性VI的偏好排列和相对偏好值变化；阈值取0%、20%、40%、60%；合成数据与PGATS数据；NEA与NCA两个解计数。

- designed_or_compared_object_cn：操纵BWM准则排名与相对偏好；操纵质量阈值；对比协作进化算法与三个经典算法生成的非支配解数量。

- baseline_control_or_counterfactual_cn：无操纵的原始BWM排序作为基线；无阈值（0%）作为全解基线；经典算法作为解数量对照。

##### objective_metrics

1. 最终排名是否随BWM偏好改变

2. 不同阈值下NEA和NCA数量

3. 是否存在角点解影响稳健性

- analysis_method_cn：系统遍历偏好条件的变化；阈值扫描；表格比较。

- main_result_cn：BWM最终排序在大多数偏好变化下稳健，但DB与NOC分别作为最重要/最不重要、或DB与SH分别作为最重要/最不重要时，至少一个解的排序改变，7号解常受影响；阈值从0%到60%显著减少非支配解数量，且协作进化算法比经典算法在每个阈值下产生更多非支配解。

- argumentative_role_cn：划定框架的边界条件，说明最终唯一解在何种DM偏好下可能不稳定；同时展示质量阈值作为DM控制解的数量的机制是有效的。

- remaining_uncertainty_cn：敏感性分析只覆盖BWM偏好和阈值，没有系统改变DEA模型、距离度量或VI集合。

- link_to_next_phase_cn：既然阈值和偏好影响候选集，下一步需要检验“协作进化算法”本身是否比经典算法更值得用于生成候选解。

##### evidence_pointers

1. Section 4.2 Sensitivity analysis

2. Table 13阈值与非支配解数量比较

#### 5. 与经典聚类算法的效率对比

- order：5

- name_cn：与经典聚类算法的效率对比

- question_cn：协作进化算法相对DBSCAN、Mean Shift、Affinity Propagation是否在常用VI上更优，以及这种优势的边界在哪里？

- inputs_and_setting_cn：合成数据和PGATS数据；评价VI包括CS、DB、SH；算法组为GA/PSO/HS中的最优BEA和三个经典算法中的最优BCA。

- designed_or_compared_object_cn：比较BEA与BCA在三个数据集×三个VI上的平均值与最优值；并讨论质心编码/二进制编码对DB表现的影响。

- baseline_control_or_counterfactual_cn：经典算法Mean Shift、DBSCAN、Affinity Propagation作为外部基准。

##### objective_metrics

1. CS、DB、SH的Avg和Best

2. 每个数据集上的胜出算法

3. 不同编码表示下的表现差异

- analysis_method_cn：表格对比，定性解释性能差异的原因。

- main_result_cn：在CS和SH上，进化算法在所有数据集中都优于最佳经典算法；在DB上，合成数据集进化算法更优，但PGATS数据中经典算法的DB平均值反而更好；作者猜测是质心/簇数同时作为决策变量的表示方式所致，若改为二进制编码可能全面占优。

- argumentative_role_cn：用外部算法基准为协作进化DSS提供竞争有效性证据，同时诚实暴露一个不利边界，并将该边界转化为未来研究问题。

- remaining_uncertainty_cn：没有统计显著性检验；没有在更多真实数据集上验证；DB的边界只依赖一个数据集。

- link_to_next_phase_cn：性能边界与编码猜想被放入结论的future work，形成对全文贡献的保护性限定。

##### evidence_pointers

1. Section 4.3 Efficiency comparison

2. Table 14 BEA与BCA结果

## 各部分修辞架构

### abstract_moves

1. CONTEXT

2. LIMITATION

3. RQ_OR_OBJECTIVE

4. STUDY_OVERVIEW

5. RESULT

### introduction_moves

1. CONTEXT

2. PRACTICAL_STAKES

3. PHENOMENON

4. PRIOR_KNOWLEDGE

5. LIMITATION

6. TRANSITION

7. GAP

8. THEORY_INTRO

9. RQ_OR_OBJECTIVE

10. CONTRIBUTION

11. BENCHMARK_OR_CONTRAST

### theory_and_knowledge_moves

1. PRIOR_KNOWLEDGE

2. LIMITATION

3. THEORY_INTRO

4. THEORY_PROPOSITION

5. REQUIREMENT

6. DESIGN_FEATURE

### artifact_design_moves

1. REQUIREMENT

2. DESIGN_FEATURE

3. METHOD_JUSTIFICATION

4. STUDY_OVERVIEW

### evaluation_moves

1. METHOD_JUSTIFICATION

2. RESULT

3. BENCHMARK_OR_CONTRAST

4. ROBUSTNESS_OR_BOUNDARY_TEST

### discussion_and_contribution_moves

1. CONTRIBUTION

2. BOUNDARY_CONDITION

3. LIMITATION_AND_FUTURE

## 理论/知识到设计的翻译

### 知识/理论基础

1. 聚类有效性指标理论（内部指标：DB、CS、SH；外部与相对指标）

2. 归一化方法NUI与NRU

3. 多目标进化优化与GA/PSO/HS算法

4. Nash社会福利/乘积式优化思想（引Charkhgard等）

5. 数据包络分析CCR模型

6. Best-Worst Method多准则决策

- 理论—设计耦合：partial

- 耦合判定理由：文中没有可检验的行为或组织理论；设计主要来自聚类指数、归一化、进化优化和DEA/BWM等量化方法的技术知识。但这些知识确实实质性地决定了部分设计，例如归一化方法决定聚合函数、阈值约束体现DM期望、DEA/BWM决定终选流程，因此属于“知识基础部分决定设计”而非纯事后包装。

- 理论到设计翻译链：VI各自只假设某种几何结构且DM有多准则 → 需要把不同量纲VI归一化到0-1 → NUI/NRU提供归一化规则 → 引入乘积式聚合把归一化VI以权重为幂合并为单一目标 → 因为问题NP-hard且含非线性 → 用GA/PSO/HS求解 → 单算法可能有偏 → 离线信息共享建立全局OP/Max/Min参数 → DM对未来划分有最低期望 → 在MINLP中加阈值约束 → 多个权重组合产生大量候选解 → 使用非支配排序压缩 → DEA用输入NOC/DB/CS和输出SH识别有效解 → 多个有效解需要主观偏好与定性信息 → BWM与Eq.28确定唯一最终解。

### mapping_table

#### 1. 1

- theory_or_knowledge_claim_cn：不同VI各自衡量一种几何结构，单指标无法覆盖多维聚类质量

- mechanism_cn：多VI之间可能冲突，单一准则会忽视其他目标

- design_requirement_cn：需要一个能同时纳入多个VI的聚合函数

- artifact_choice_cn：Eq.16的归一化乘积式聚合目标，以各VI归一化值取权重幂次相乘

- evaluated_contrast_cn：16组不同的权重组合与3个算法重复

- objective_result_cn：生成144个候选，去重去支配后得到16个非支配唯一解

##### evidence_pointers

1. Section 2.3 Eq.16

2. Section 4.1 Steps 4-5

3. Table A.5

#### 2. 2

- theory_or_knowledge_claim_cn：不同VI量纲和方向不同，必须先归一化才能比较

- mechanism_cn：NUI与NRU能将VI转换成0-1无量纲值并统一优化方向

- design_requirement_cn：聚合函数必须使用归一化后的VI，而不是原始值

- artifact_choice_cn：DB和CS用NRU归一化，SH用NUI归一化，作为Eq.16输入

- evaluated_contrast_cn：单目标运行得到的OP/DB、OP/CS、Max-SH/Min-SH

- objective_result_cn：各VI进入同一目标函数，权重可以解释相对重要性

##### evidence_pointers

1. Section 2.2 Table 3

2. Section 2.3 Eqs.13-15

#### 3. 3

- theory_or_knowledge_claim_cn：自动聚类问题NP-hard，簇数也是决策变量

- mechanism_cn：精确求解在可行解空间爆炸时不可行

- design_requirement_cn：必须使用元启发式算法作为求解器

- artifact_choice_cn：选用GA、PSO、HS，并使用质心位置+激活层的两层实数编码

- evaluated_contrast_cn：三个算法各自10次单目标运行，以及与经典算法的比较

- objective_result_cn：三个算法在不同VI上各有优势，协作平均偏差0.75%-10.2%

##### evidence_pointers

1. Section 2问题描述

2. Section 3 Step1 c-d

3. Table 8

#### 4. 4

- theory_or_knowledge_claim_cn：单一进化算法可能提供有偏结果

- mechanism_cn：不同算法对簇中心和簇数搜索策略不同，会偏向不同VI

- design_requirement_cn：算法之间需要信息共享，以形成全局稳健的聚合参数

- artifact_choice_cn：离线协作：每个算法先分别求解VI，再共享全局最优OP/Max/Min

- evaluated_contrast_cn：协作方案结果与单个算法结果的百分比偏差

- objective_result_cn：合成数据上改善0.75%-9.60%，PGATS上改善1.13%-10.2%

##### evidence_pointers

1. Section 3 Step4

2. Table 8

#### 5. 5

- theory_or_knowledge_claim_cn：DM对聚类质量有主观最低期望

- mechanism_cn：若无阈值，最终解可能在一个DM不接受的VI上很差

- design_requirement_cn：把DM的质量期望转化为模型约束

- artifact_choice_cn：约束23-25，以及Step2中的0到1质量阈值

- evaluated_contrast_cn：阈值0%、20%、40%、60%下的非支配解数量

- objective_result_cn：阈值越高，可行非支配解越少，40%时PGATS只剩6个非支配解，60%时只剩1个

##### evidence_pointers

1. Section 2.3约束23-25

2. Section 3 Step2

3. Table 13

#### 6. 6

- theory_or_knowledge_claim_cn：DEA能无需预知权重即可在多输入多输出间识别有效单元

- mechanism_cn：把聚类候选看作DMU，输入为越小越好的指标，输出为越大越好的指标

- design_requirement_cn：用DEA从非支配解中识别有效划分

- artifact_choice_cn：输入导向CCR模型：输入NOC、DB、CS，输出SH

- evaluated_contrast_cn：16个非支配解输入DEA后的效率分数

- objective_result_cn：6个解效率分数为1，被识别为有效解

##### evidence_pointers

1. Section 3 Step5-Step6

2. Table 10

#### 7. 7

- theory_or_knowledge_claim_cn：当DEA产生多个有效解时，需要额外偏好信息来唯一化

- mechanism_cn：BWM通过最要与最不重要准则的比较生成权重，可纳入定性指标

- design_requirement_cn：用BWM对DEA有效解按定性VI排序

- artifact_choice_cn：BWM比较NOC/SH/DB/CS/VC/VN，用Eq.28以倒数和缩放后的BWM权重为指数评分

- evaluated_contrast_cn：BWM权重敏感性分析

- objective_result_cn：10号聚类被排为最优；排序总体稳健，但两个偏好条件下会改变

##### evidence_pointers

1. Section 3 Step6

2. Tables 11-12

3. Section 4.2敏感性分析

## 评价逻辑

### evaluation_modes

1. 单案例可行性演示（合成数据六步流程）

2. 内部算法比较（GA/PSO/HS与协作偏差）

3. 真实二手数据集复现（PGATS）

4. 敏感性分析（BWM偏好与质量阈值）

5. 外部算法benchmark（DBSCAN、Mean Shift、Affinity Propagation）

- why_these_evaluations_cn：因为论文主张是“可泛化的框架”而非单一算法性能，所以不能只在一个数据上展示；需要合成数据证明可控性，需要真实数据展示可迁移性；需要用阈值与偏好敏感性回答DM输入影响；需要与经典算法对比回答协作进化算法是否带来了真正收益。

- benchmark_and_contrast_chain_cn：评价参照逐级累积：先在合成数据内用三种进化算法互相对照，证明单算法有偏并引出协作；再用协作偏差表量化收益；然后引入经典算法作为外部基准，检验进化算法在所有VI上是否都更优；同时用BWM偏好和阈值扰动作为反事实检验。最终把“协作优于单算法”的局部结果提升为“框架能处理多准则自动聚类”的一般设计知识。

### claim_evidence_ledger

#### 1. 新聚合VI能把任意多个VI合并为单一分数

- claim_cn：新聚合VI能把任意多个VI合并为单一分数

- evidence_cn：给出Eq.16与NUI/NRU公式，并在实验中用DB/CS/SH三个VI运行

- gap_cn：未与其它聚合函数（如加权和）比较；只验证了三个内部VI

#### 2. 协作进化算法优于单一算法

- claim_cn：协作进化算法优于单一算法

- evidence_cn：Table 8平均偏差0.75%-10.2%

- gap_cn：该“协作基准”是由三个算法自身最优值构造的，缺少统计显著性检验

#### 3. 框架具有通用性

- claim_cn：框架具有通用性

- evidence_cn：在合成数据和PGATS两个数据集上运行，且模型设计为可容纳任意VI

- gap_cn：只测试连续型数据和欧氏距离；未证明外部/相对VI、混合数据或高维数据

#### 4. DEA+BWM能提供唯一最终聚类

- claim_cn：DEA+BWM能提供唯一最终聚类

- evidence_cn：16个非支配解经DEA剩6个有效解，经BWM得唯一最优10号解

- gap_cn：BWM中的定性评分由作者本人给出，不是真实DM行为；没有比较替代MCDM方法

#### 5. 进化算法在多数VI上优于经典算法

- claim_cn：进化算法在多数VI上优于经典算法

- evidence_cn：Table 14显示CS/SH全面优于BCA，DB在合成数据上优于BCA

- gap_cn：PGATS的DB平均值不如经典算法，表明边界存在；无统计检验

#### 6. 阈值机制可控制候选解数量

- claim_cn：阈值机制可控制候选解数量

- evidence_cn：Table 13显示0%到60%阈值下非支配解数量递减，且NEA高于NCA

- gap_cn：没有分析阈值与最终解质量之间的关系

- internal_validity_strategy_cn：使用已知中心点的合成数据以确立基本事实；每个算法重复10次以获得分布信息；用置信区间和描述统计描述稳定性；用标准非支配定义去重去支配；用系统化的BWM偏好扫描检验排序对主观输入的敏感度。

- external_validity_strategy_cn：加入PGATS真实体育统计数据作为第二个数据集；使用三种不同原理的经典聚类算法作为外部基准；将框架设计为模块化步骤，以支持不同VI、算法和DM输入。

- what_is_not_actually_tested_cn：没有真实决策者实际操作DSS的主观评分；没有用外部真实类别标签验证聚类正确性；没有与其它自动聚类DSS或MOEA集成框架比较；没有大数据、高维或混合类型数据；没有统计显著性或效应量检验；DEA/BWM的具体计算细节在OCR版本中不完整。

## 贡献闭环

- technical_claim_cn：提出的归一化乘积式聚合函数与协作式多进化算法在合成数据和PGATS上能产生有效聚类，并在大多数比较中优于三个经典算法。

- artifact_claim_cn：六步DSS能够把DM的VI选择、质量阈值、权重和定性偏好整合为唯一划分；离线协作信息共享是提升结果的关键设计部分。

- mechanism_claim_cn：归一化使不同VI可比；幂次权重使DM偏好影响聚合值；离线协作避免单一算法偏差；DEA识别有效前沿；BWM在有效解中引入主观定性排序。

- boundary_claim_cn：框架适用于DM对数据集和准则信息不足、目的无法完全匹配现有方法、存在多个冲突准则的场景；但BWM最终排序在DB与NOC或DB与SH成为最重要/最不重要准则时可能不稳定；进化算法在DB上并非无条件优于经典算法。

- reusable_design_knowledge_cn：可复用要点包括：用NUI/NRU统一VI量纲；用乘积式聚合而非求和式聚合；用离线协作共享最优参数；用质量阈值作为DM控制解规模的旋钮；用DEA先筛有效解再用BWM处理多解唯一化。

- theoretical_contribution_cn：论文不修改经典理论，但提出了“主VI/次VI”概念、质量阈值约束和乘积式聚合VI，为自动聚类DSS研究提供了概念性设计知识。

- how_discussion_closes_intro_gap_cn：结论重申引言提出的三类困境：目的与算法不匹配、DM缺乏准则信息、多准则并存，并说明本框架通过阈值、主/次VI、协作算法和DEA/BWM统一处理这三类情况，从而宣称填补了“缺乏可泛化框架”的缺口。

- overclaim_or_unsupported_leaps_cn：“任意VI”“任何类型自动聚类问题”的通用性主张只基于形式化设计，缺乏跨VI类型、跨数据类型的实验支持；Table 2的“唯一具备全部特征”是作者自定义问题集下的判断；PGATS上DB表现不如经典算法说明“协作进化更优”并非全域结论；BWM定性评分由作者自己充当DM，外部效度有限。

## 句级写作动作图谱

### 1. Abstract P1 S1

- order：1

- section：Abstract

- locator：Abstract P1 S1

- move_code：CONTEXT

- paraphrase_cn：自动聚类在决策者不了解数据性质与关注准则时尤为困难。

- rhetorical_function_cn：开场将问题定位为有实际挑战性的聚类难题。

- depends_on_cn：默认读者知道聚类分析的一般背景。

- sets_up_cn：为后面提出DSS提供问题温度。

- evidence_pointer：Abstract第一句

### 2. Abstract P1 S2

- order：2

- section：Abstract

- locator：Abstract P1 S2

- move_code：LIMITATION

- paraphrase_cn：现有有效性指标各自只考虑有限目标，忽略其他验证层面，因而缺乏通用性。

- rhetorical_function_cn：指出现状缺陷，建立研究缺口。

- depends_on_cn：已说明自动聚类是困难问题。

- sets_up_cn：为“多准则聚合”方案做铺垫。

- evidence_pointer：Abstract第二句

### 3. Abstract P1 S3

- order：3

- section：Abstract

- locator：Abstract P1 S3

- move_code：RQ_OR_OBJECTIVE

- paraphrase_cn：提出在多个进化算法间协作的框架，并开发MINLP模型与六步DSS。

- rhetorical_function_cn：直接宣告本文贡献对象。

- depends_on_cn：缺口的建立使方案出现成为必要。

- sets_up_cn：为摘要后面的流程描述提供总纲。

- evidence_pointer：Abstract第三句

### 4. Abstract P2 S1-S3

- order：4

- section：Abstract

- locator：Abstract P2 S1-S3

- move_code：STUDY_OVERVIEW

- paraphrase_cn：决策者选择定量主VI和进化算法，可加入定性次VI，设定每个VI的阈值，分别运行算法；系统保存最优VI值以构造聚合函数，反复求解，最后用DEA和BWM确定最终聚类。

- rhetorical_function_cn：为读者提供整个DSS流程的路线图。

- depends_on_cn：已说明模型与框架存在。

- sets_up_cn：为正文第3、4节详细展开设定预期。

- evidence_pointer：Abstract第二段

### 5. Abstract P2 S4

- order：5

- section：Abstract

- locator：Abstract P2 S4

- move_code：RESULT

- paraphrase_cn：在合成数据集和两个二手数据集上验证了方法适用性，并逐步讨论结果。

- rhetorical_function_cn：提前给出评价证据，表明不只是概念提案。

- depends_on_cn：流程概述使结果有依托。

- sets_up_cn：为读者接受正文实验部分做准备。

- evidence_pointer：Abstract末句

### 6. Introduction P1 S1

- order：6

- section：Introduction

- locator：Introduction P1 S1

- move_code：CONTEXT

- paraphrase_cn：聚类是把数据分配到簇中的科学，簇内高相似、簇间高区别，所有聚类算法围绕凝聚与分离的权衡设计。

- rhetorical_function_cn：给出基本定义和聚类核心张力。

- depends_on_cn：无。

- sets_up_cn：为后续“VI衡量这两类准则”提供概念基础。

- evidence_pointer：Introduction首段

### 7. Introduction P1 S2

- order：7

- section：Introduction

- locator：Introduction P1 S2

- move_code：PRACTICAL_STAKES

- paraphrase_cn：聚类被用于推荐、电信、需求预测、银行信用、患者风险、疫苗网络、配送网络和保险定价等广泛领域。

- rhetorical_function_cn：用应用广度强调聚类问题的重要性。

- depends_on_cn：已定义聚类。

- sets_up_cn：说明研究自动聚类DSS具有现实价值。

- evidence_pointer：Introduction第1段文献[1-8]

### 8. Introduction P2 S1

- order：8

- section：Introduction

- locator：Introduction P2 S1

- move_code：PHENOMENON

- paraphrase_cn：经典聚类预置簇数，自动聚类把簇数作为决策变量；高维、密度/大小/形状差异和簇重叠都会使确定簇数更难。

- rhetorical_function_cn：界定研究对象为自动聚类，并指出核心困难。

- depends_on_cn：基于聚类定义展开。

- sets_up_cn：为后文把簇数作为DEA输入之一提供依据。

- evidence_pointer：Introduction第2段

### 9. Introduction P2 S2

- order：9

- section：Introduction

- locator：Introduction P2 S2

- move_code：CONTEXT

- paraphrase_cn：聚类还需处理模仿生命体行为和主观性的问题。

- rhetorical_function_cn：把题目引向DSS中的主观性维度。

- depends_on_cn：自动聚类困难清单。

- sets_up_cn：为主/次VI和DM偏好埋下伏笔。

- evidence_pointer：Introduction第2段末

### 10. Introduction P3 S1

- order：10

- section：Introduction

- locator：Introduction P3 S1

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：自动聚类输出簇数与划分，有效性指标可分为外部、内部和相对三类。

- rhetorical_function_cn：给出VI的分类体系。

- depends_on_cn：自动聚类输出定义。

- sets_up_cn：后续2.1节展开VI局限。

- evidence_pointer：Introduction第3段

### 11. Introduction P3 S2

- order：11

- section：Introduction

- locator：Introduction P3 S2

- move_code：LIMITATION

- paraphrase_cn：每个VI按预设几何结构衡量拟合优度，当簇结构多样且DM有多个目标时，多数算法和VI会失败。

- rhetorical_function_cn：建立VI层面的性能缺口。

- depends_on_cn：VI分类知识。

- sets_up_cn：为需要多VI聚合提供理由。

- evidence_pointer：Introduction第3段末

### 12. Introduction P4 S1

- order：12

- section：Introduction

- locator：Introduction P4 S1

- move_code：TRANSITION

- paraphrase_cn：作者把MOEA最终解选择归纳为独立准则、膝部修剪和集成方法三类。

- rhetorical_function_cn：用分类法组织文献，为定位本文做铺垫。

- depends_on_cn：多目标进化聚类背景。

- sets_up_cn：随后逐一评述三类方法并指出缺点。

- evidence_pointer：Introduction第4段

### 13. Introduction P4 S2-S8

- order：13

- section：Introduction

- locator：Introduction P4 S2-S8

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：评述独立准则方法的代表工作，包括用误分类VI、NSGA-II、Pareto排序、九个VI等，并指出各自局限如只能处理球形簇或非均匀分布不佳。

- rhetorical_function_cn：提供证据说明独立准则方法各有特定适用范围。

- depends_on_cn：三类方法框架。

- sets_up_cn：支持“现有MOEA方法难以泛化”的缺口。

- evidence_pointer：Introduction第4段文献[9,14-16]等

### 14. Introduction P5 S1

- order：14

- section：Introduction

- locator：Introduction P5 S1

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：膝部修剪选择改变一个目标值时对另一目标影响最大的解，但处理重叠簇和大数据有困难。

- rhetorical_function_cn：覆盖第二类终选方法并指出局限。

- depends_on_cn：三类方法框架。

- sets_up_cn：继续累积现有方法不通用性。

- evidence_pointer：Introduction第5段

### 15. Introduction P6 S1

- order：15

- section：Introduction

- locator：Introduction P6 S1

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：集成方法通过合并多个VI信息得到单一聚类，已有MCDM排名、显隐知识集成、模糊集成和粒子群等尝试。

- rhetorical_function_cn：覆盖第三类方法并展示已有集成思路。

- depends_on_cn：三类方法框架。

- sets_up_cn：让读者看到本文集成式DSS与它们的区别。

- evidence_pointer：Introduction第6段文献[11,12,34,41]

### 16. Introduction P6 S2

- order：16

- section：Introduction

- locator：Introduction P6 S2

- move_code：GAP

- paraphrase_cn：被引MOEA文章目标特殊，难以推广到所有多目标聚类方法；本文框架试图填补这一缺口。

- rhetorical_function_cn：明确文献缺口。

- depends_on_cn：三类方法局限归纳。

- sets_up_cn：为贡献列表提供靶子。

- evidence_pointer：Introduction第6段末

### 17. Introduction P7 S1

- order：17

- section：Introduction

- locator：Introduction P7 S1

- move_code：THEORY_INTRO

- paraphrase_cn：MCDM帮助决策者定义问题、识别最重要准则和偏好并推荐排序；DEA测量DMU相对效率并预处理数据。

- rhetorical_function_cn：为后文DEA/BWM工具引入知识背景。

- depends_on_cn：已提出缺口。

- sets_up_cn：为DSS最后两步提供方法合法化。

- evidence_pointer：Introduction第7段

### 18. Introduction P8 S1-S2

- order：18

- section：Introduction

- locator：Introduction P8 S1-S2

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：聚类输出可被用作其它决策支持方法的输入，例如流量作弊分类和共享住宿评论数量研究。

- rhetorical_function_cn：说明聚类DSS不是孤立优化，而是决策链的一环。

- depends_on_cn：DEA/MCDM上下文。

- sets_up_cn：为“DSS”这一期刊定位服务。

- evidence_pointer：Introduction第8段文献[44,45]

### 19. Introduction P9 S1

- order：19

- section：Introduction

- locator：Introduction P9 S1

- move_code：GAP

- paraphrase_cn：就作者所知，缺少能反映DM考虑的可泛化自动聚类框架；因此选择四个VI并让三个进化算法协作。

- rhetorical_function_cn：把文献缺口转化为本文研究目标。

- depends_on_cn：前面三类方法不足。

- sets_up_cn：引出四VI和三算法的具体设计。

- evidence_pointer：Introduction第9段

### 20. Introduction P9 S2

- order：20

- section：Introduction

- locator：Introduction P9 S2

- move_code：CONTRIBUTION

- paraphrase_cn：贡献包括MINLP模型、新的归一化乘积式聚合VI、通用性、最小期望阈值、协作DSS、主/次VI概念和DEA-BWM排名框架。

- rhetorical_function_cn：密集列出贡献清单，让审稿人快速看到边际贡献。

- depends_on_cn：缺口声明。

- sets_up_cn：为Table 2特征对比做内容清单。

- evidence_pointer：Introduction贡献列表

### 21. Introduction Table 2前一段与表格

- order：21

- section：Introduction

- locator：Introduction Table 2前一段与表格

- move_code：BENCHMARK_OR_CONTRAST

- paraphrase_cn：通过七个问题与既有MOEA论文逐项对比，只有本文包含全部特征：定量/定性VI、VI阈值、无专家依赖、多于两个VI的Pareto前沿、聚合函数、唯一解和协作策略。

- rhetorical_function_cn：用特征表把本文置于文献对照的制高点。

- depends_on_cn：贡献清单。

- sets_up_cn：强化新颖性主张，也暗示后面的评价要支撑这些特征。

- evidence_pointer：Introduction Table 2

### 22. Section 2 P1

- order：22

- section：Problem description

- locator：Section 2 P1

- move_code：LIMITATION

- paraphrase_cn：自动聚类可行解数随数据点增多而爆炸，且Brucker证明簇数大于三时聚类问题NP-hard。

- rhetorical_function_cn：从计算复杂性说明精确求解不可行。

- depends_on_cn：自动聚类定义。

- sets_up_cn：为选择进化算法提供正当理由。

- evidence_pointer：Section 2开头与Eq.1

### 23. Section 2 P1末

- order：23

- section：Problem description

- locator：Section 2 P1末

- move_code：RQ_OR_OBJECTIVE

- paraphrase_cn：因此开发DSS，用协作式多准则进化方法把任意VI集合并为单一分数。

- rhetorical_function_cn：把复杂性结论转为本文目标。

- depends_on_cn：NP-hard结论。

- sets_up_cn：进入2.1节VI和2.2节归一化。

- evidence_pointer：Section 2末句

### 24. Section 2.1 P1

- order：24

- section：Section 2.1

- locator：Section 2.1 P1

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：VI通过簇内凝聚与簇间分离来检验聚类，三类指标分别按预设几何结构计算。

- rhetorical_function_cn：系统介绍VI的判定逻辑。

- depends_on_cn：第2段定义。

- sets_up_cn：解释为什么单一VI不足。

- evidence_pointer：Section 2.1首段

### 25. Section 2.1 P2

- order：25

- section：Section 2.1

- locator：Section 2.1 P2

- move_code：LIMITATION

- paraphrase_cn：当聚类目的不能匹配某方法、DM缺乏准则信息、或存在多个准则时，需要进一步研究。

- rhetorical_function_cn：把VI的通用局限转成三个可操作条件。

- depends_on_cn：VI分类。

- sets_up_cn：这三个条件在结论中再次出现形成闭环。

- evidence_pointer：Section 2.1三类情形列表

### 26. Section 2.1 P3

- order：26

- section：Section 2.1

- locator：Section 2.1 P3

- move_code：RQ_OR_OBJECTIVE

- paraphrase_cn：本文框架被设计来解决上述三类情况。

- rhetorical_function_cn：把问题清单收束为框架目标。

- depends_on_cn：三类情形。

- sets_up_cn：引入归一化和数学模型。

- evidence_pointer：Section 2.1末段

### 27. Section 2.2 Table 3前后

- order：27

- section：Section 2.2

- locator：Section 2.2 Table 3前后

- move_code：THEORY_INTRO

- paraphrase_cn：归一化使不同量纲VI可比较，NUI和NRU能把任意VI转换为0-1单位。

- rhetorical_function_cn：说明聚合前的必要预处理。

- depends_on_cn：多VI不可直接比较的局限。

- sets_up_cn：为Eq.16的归一化聚合函数提供输入工具。

- evidence_pointer：Section 2.2与Table 3

### 28. Section 2.3 Eq.16前后

- order：28

- section：Section 2.3

- locator：Section 2.3 Eq.16前后

- move_code：DESIGN_FEATURE

- paraphrase_cn：MINLP目标函数采用归一化VI以权重为幂的乘积形式，DB和CS用NRU，SH用NUI；较大的权重使对应VI在目标中更受重视。

- rhetorical_function_cn：将归一化知识落实为核心制品设计。

- depends_on_cn：归一化公式与乘积式思想。

- sets_up_cn：为实验中的16组权重组合提供模型基础。

- evidence_pointer：Section 2.3 Eq.16

### 29. Section 2.3约束23-25

- order：29

- section：Section 2.3

- locator：Section 2.3约束23-25

- move_code：DESIGN_FEATURE

- paraphrase_cn：模型加入DB、CS、SH分别不低于/高于DM阈值约束，把决策者最低期望转化为可行域限制。

- rhetorical_function_cn：把“最小期望”从概念变成可执行约束。

- depends_on_cn：归一化阈值可用性。

- sets_up_cn：为Step2阈值设定提供数学依据。

- evidence_pointer：Section 2.3约束23-25

### 30. Section 3开头

- order：30

- section：Methodology

- locator：Section 3开头

- move_code：STUDY_OVERVIEW

- paraphrase_cn：开发框架包含六个步骤。

- rhetorical_function_cn：预告方法论结构，降低阅读复杂度。

- depends_on_cn：数学模型建立。

- sets_up_cn：后面Step1-Step6逐一展开。

- evidence_pointer：Section 3第一句

### 31. Section 3 Step 1 a-d

- order：31

- section：Methodology Step 1

- locator：Section 3 Step 1 a-d

- move_code：DESIGN_FEATURE

- paraphrase_cn：决策者选择与聚类目标和数据类型匹配的VI，可加入定性VI作为次要目标；同时选择GA/PSO/HS算法，采用质心位置加激活层的实数编码。

- rhetorical_function_cn：说明用户如何进入系统以及解如何表示。

- depends_on_cn：DM角色和算法选择需求。

- sets_up_cn：为主/次VI概念和后续Solution representation提供具体操作。

- evidence_pointer：Section 3 Step 1与Fig.1

### 32. Section 3 Step 1 c

- order：32

- section：Methodology Step 1 c

- locator：Section 3 Step 1 c

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：由于MINLP含大量非线性方程且为多目标，作者依据文献调查选择GA、PSO和HS。

- rhetorical_function_cn：解释算法选择不是任意的，而是基于问题性质和文献流行度。

- depends_on_cn：NP-hard与非线性模型。

- sets_up_cn：为后面运行实验中的算法参数表A.6提供理由。

- evidence_pointer：Section 3 Step1 c

### 33. Section 3 Step 2

- order：33

- section：Methodology Step 2

- locator：Section 3 Step 2

- move_code：REQUIREMENT

- paraphrase_cn：决策者为每个VI设定0到1的质量阈值，若解空间为空则放宽，阈值与可行解数量成反比。

- rhetorical_function_cn：把DM期望转成DSS可控参数。

- depends_on_cn：模型约束23-25。

- sets_up_cn：为Table 13阈值分析提供意义。

- evidence_pointer：Section 3 Step2

### 34. Section 3 Step 3

- order：34

- section：Methodology Step 3

- locator：Section 3 Step 3

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：对每个VI分别用三种算法各跑十次，获得最优值或最大/最小值，作为聚合函数的输入。

- rhetorical_function_cn：说明聚合函数输入参数的实证来源。

- depends_on_cn：归一化需要Max/Min/OP。

- sets_up_cn：为附录A.2-A.4的单目标结果表提供来源。

- evidence_pointer：Section 3 Step3

### 35. Section 3 Step 4

- order：35

- section：Methodology Step 4

- locator：Section 3 Step 4

- move_code：DESIGN_FEATURE

- paraphrase_cn：三种算法离线共享信息，统一设置全局OP/Max/Min值，并据此形成乘积式聚合目标。

- rhetorical_function_cn：定义“协作”的精确机制。

- depends_on_cn：Step3单目标运行结果。

- sets_up_cn：为Table 8协作收益评估提供设计依据。

- evidence_pointer：Section 3 Step4

### 36. Section 3 Step 5

- order：36

- section：Methodology Step 5

- locator：Section 3 Step 5

- move_code：DESIGN_FEATURE

- paraphrase_cn：决策者选择权重组合，记录每个算法最终簇数与SH/DB/CS；SH作DEA输出，DB/CS/NOC作DEA输入。

- rhetorical_function_cn：为DEA模型定义输入输出。

- depends_on_cn：聚合函数运行后的候选集。

- sets_up_cn：为Step6 DEA筛选做准备。

- evidence_pointer：Section 3 Step5

### 37. Section 3 Step 6

- order：37

- section：Methodology Step 6

- locator：Section 3 Step 6

- move_code：DESIGN_FEATURE

- paraphrase_cn：DEA返回效率分数后，若存在多个有效解，用BWM结合定性指标排序，并以Eq.28计算最终排名。

- rhetorical_function_cn：完成从有效解到唯一解的决策闭环。

- depends_on_cn：DEA有效解集。

- sets_up_cn：为实验部分的Table 10-12提供方法。

- evidence_pointer：Section 3 Step6与Eq.28

### 38. Section 4 P1

- order：38

- section：Experiment results

- locator：Section 4 P1

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：用合成数据和PGATS高尔夫统计检验框架在不同数据类型的鲁棒性。

- rhetorical_function_cn：说明实验数据选择目的。

- depends_on_cn：框架六步设计。

- sets_up_cn：引出4.1合成数据实施和4.2敏感分析。

- evidence_pointer：Section 4开头

### 39. Section 4.1 Steps 1-2

- order：39

- section：Experiment results

- locator：Section 4.1 Steps 1-2

- move_code：RESULT

- paraphrase_cn：对每个VI三种算法各跑10次，得到30个解并选全局最优，设置协作参数。

- rhetorical_function_cn：示范协作DSS的离线执行。

- depends_on_cn：Step3-4方法。

- sets_up_cn：为后续聚合函数提供输入。

- evidence_pointer：Section 4.1 Steps1-2

### 40. Section 4.1 合成数据生成段

- order：40

- section：Experiment results

- locator：Section 4.1 合成数据生成段

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：围绕6个已知中心生成480个点，以可控结构测试算法是否能识别不同簇结构。

- rhetorical_function_cn：说明合成数据的内部有效性设计。

- depends_on_cn：需要已知真值的数据。

- sets_up_cn：为六步流程提供实例。

- evidence_pointer：Section 4.1合成数据段与Table 5

### 41. Section 4.1 Step 3

- order：41

- section：Experiment results

- locator：Section 4.1 Step 3

- move_code：RESULT

- paraphrase_cn：单目标结果显示HS在CS/SH上更好，PSO在DB上稳定达到最低，算法间存在VI偏好差异。

- rhetorical_function_cn：证明单一算法可能偏向特定VI。

- depends_on_cn：附录A.2-A.4运行数据。

- sets_up_cn：为协作方法提供必要性。

- evidence_pointer：Section 4.1 Step3与Fig.3

### 42. Section 4.1 Step 3 Table 7

- order：42

- section：Experiment results

- locator：Section 4.1 Step 3 Table 7

- move_code：RESULT

- paraphrase_cn：SH与CS、SH与DB存在正相关，说明最大化SH与最小化CS/DB存在冲突。

- rhetorical_function_cn：用相关性说明多目标必要性。

- depends_on_cn：单目标运行值。

- sets_up_cn：为DEA中SH作输出、DB/CS作输入提供依据。

- evidence_pointer：Table 7

### 43. Section 4.1 Step 3 Table 8

- order：43

- section：Experiment results

- locator：Section 4.1 Step 3 Table 8

- move_code：RESULT

- paraphrase_cn：协作方法相对单一算法的平均偏差在合成数据上0.75%-9.60%，PGATS上1.13%-10.2%。

- rhetorical_function_cn：直接量化协作收益。

- depends_on_cn：协作参数设定。

- sets_up_cn：为“协作优于孤立”的核心主张提供证据。

- evidence_pointer：Table 8

### 44. Section 4.1 Steps 4-5

- order：44

- section：Experiment results

- locator：Section 4.1 Steps 4-5

- move_code：RESULT

- paraphrase_cn：16组权重重复三次得到144个候选解，去重去支配后剩16个非支配唯一解。

- rhetorical_function_cn：展示候选生成与Pareto压缩。

- depends_on_cn：Table A.1权重与单目标结果。

- sets_up_cn：为DEA输入准备候选集。

- evidence_pointer：Section 4.1 Steps4-5与Table 9

### 45. Section 4.1 Step 6

- order：45

- section：Experiment results

- locator：Section 4.1 Step 6

- move_code：RESULT

- paraphrase_cn：输入导向CCR DEA在16个非支配解中识别出6个有效解。

- rhetorical_function_cn：显示DEA如何进一步压缩候选。

- depends_on_cn：非支配解集。

- sets_up_cn：为BWM多准则排序提供输入。

- evidence_pointer：Section 4.1 Step6与Table 10

### 46. Section 4.1 Step 6 Table 11-12

- order：46

- section：Experiment results

- locator：Section 4.1 Step 6 Table 11-12

- move_code：RESULT

- paraphrase_cn：BWM结合定性VC/VN和定量VI后，10号聚类被排为最终最优。

- rhetorical_function_cn：演示如何在多解情况下输出唯一答案。

- depends_on_cn：DEA有效解与DM定性评分。

- sets_up_cn：为敏感性分析提供基准排序。

- evidence_pointer：Tables 11-12与Fig.4

### 47. Section 4.2第一段

- order：47

- section：Section 4.2

- locator：Section 4.2第一段

- move_code：ROBUSTNESS_OR_BOUNDARY_TEST

- paraphrase_cn：BWM敏感性分析显示最终排名总体稳健，但两种偏好条件（DB与NOC、DB与SH分别成为最重要/最不重要）会改变至少一个解的排名，角点解可能是原因。

- rhetorical_function_cn：承认框架对DM偏好存在边界，避免过度泛化。

- depends_on_cn：Table 10-12排序。

- sets_up_cn：为结论部分的适用边界提供证据。

- evidence_pointer：Section 4.2 Changes on relative preference values

### 48. Section 4.2 Table 13

- order：48

- section：Section 4.2

- locator：Section 4.2 Table 13

- move_code：ROBUSTNESS_OR_BOUNDARY_TEST

- paraphrase_cn：阈值从0%到60%时，协作进化算法产生的非支配解数量显著高于经典算法；更高阈值减少候选解数量。

- rhetorical_function_cn：展示阈值作为DM控制机制的稳健效果。

- depends_on_cn：质量阈值约束。

- sets_up_cn：为“框架能适应DM期望”提供证据。

- evidence_pointer：Table 13

### 49. Section 4.3开头

- order：49

- section：Section 4.3

- locator：Section 4.3开头

- move_code：BENCHMARK_OR_CONTRAST

- paraphrase_cn：将GA/PSO/HS与DBSCAN、Mean Shift、Affinity Propagation在CS/DB/SH上比较。

- rhetorical_function_cn：引入外部算法基准来检验协作进化算法的竞争力。

- depends_on_cn：已有合成和PGATS数据。

- sets_up_cn：为Table 14的性能结论搭建框架。

- evidence_pointer：Section 4.3

### 50. Section 4.3 Table 14后

- order：50

- section：Section 4.3

- locator：Section 4.3 Table 14后

- move_code：RESULT

- paraphrase_cn：CS和SH上进化算法在所有数据集均优于最佳经典算法；DB上合成数据进化算法更优，但PGATS中经典算法DB平均值更好。

- rhetorical_function_cn：给出外部对比结果并暴露不一致边界。

- depends_on_cn：Table 14数据。

- sets_up_cn：引出二进制编码的未来研究方向。

- evidence_pointer：Table 14

### 51. Section 4.3最后一段

- order：51

- section：Section 4.3

- locator：Section 4.3最后一段

- move_code：LIMITATION_AND_FUTURE

- paraphrase_cn：若把质心和簇数表示改为二进制编码，作者推测进化算法可能在所有VI上全面胜出，留待未来研究。

- rhetorical_function_cn：把不利结果转化为可检验的后续假设。

- depends_on_cn：DB在PGATS上的反例。

- sets_up_cn：为结论部分的future work铺垫。

- evidence_pointer：Section 4.3末

### 52. Section 5 P1

- order：52

- section：Conclusions

- locator：Section 5 P1

- move_code：CONTRIBUTION

- paraphrase_cn：单一准则聚类算法不适合非线性可分和冲突目标；本文提供带质量阈值的MINLP模型和新的聚合VI。

- rhetorical_function_cn：返回开头缺陷并重申贡献。

- depends_on_cn：全文模型与实验。

- sets_up_cn：为随后的三类适用情形做结论闭环。

- evidence_pointer：Section 5第一段

### 53. Section 5 P2

- order：53

- section：Conclusions

- locator：Section 5 P2

- move_code：BOUNDARY_CONDITION

- paraphrase_cn：框架适用于目的与算法不匹配、DM信息少、存在多准则三种情况；主/次VI、信息共享、DEA和BWM保证唯一聚类结果。

- rhetorical_function_cn：直接对接引言三类缺口，形成贡献闭环。

- depends_on_cn：引言三类情形和六步DSS。

- sets_up_cn：为未来研究限定范围。

- evidence_pointer：Section 5第二段

### 54. Section 5 P3

- order：54

- section：Conclusions

- locator：Section 5 P3

- move_code：LIMITATION_AND_FUTURE

- paraphrase_cn：文章重点是框架开发，未来需设计更高效算法、探索更多VI组合、不同距离度量和真实DM视角。

- rhetorical_function_cn：诚实限定贡献并开放研究议程。

- depends_on_cn：实验中的性能边界。

- sets_up_cn：为DSS自动聚类文献留下扩展空间。

- evidence_pointer：Section 5未来工作段

## 写作技术

- gap_construction_cn：作者先建立自动聚类固有困难，再指出VI各有几何假设，接着把MOEA终选方法分为三类并逐一列举失败条件，最后用“不能轻易泛化”将缺口具体化；同时用Table 2的七问特征表把本文置于唯一满足所有特征的制高点。

- signposting_cn：摘要给出六步流程；引言末段说明剩余部分组织；方法论开头直接“六步”；每一步都按Step编号标题化，使复杂流程容易被追踪。

- transition_logic_cn：从“问题NP-hard”过渡到“需要进化算法”；从“归一化”过渡到“聚合函数”；从“单算法有偏”过渡到“协作”；从“多个DEA有效解”过渡到“BWM唯一化”；从“性能反例”过渡到“未来研究”。

- claim_evidence_rhythm_cn：每个主要设计主张后都立即跟随对应实验证据：提出聚合函数后给出权重扫描；提出协作后给出Table 8偏差；提出DEA/BWM后给出有效解数量与最终排名；提出阈值后给出Table 13。

- benchmark_narrative_cn：benchmark不是简单罗列，而是嵌入论证：先用合成数据内部对照证明单算法偏颇，再引入经典算法作为外部基准回答“协作进化是否值得”；同时把不利结果解释为编码表示问题，保留进一步研究空间。

- theory_return_cn：论文不依赖行为理论，但在结论用“三类困境”与引言形成镜像，把DSS设计特征（阈值、主/次VI、协作、DEA/BWM）逐个映射回当初的缺口，让贡献显得完整。

- contribution_positioning_cn：贡献通过四层定位：数学新模型、DSS流程新特征、主/次VI概念、DEA/BWM组合；再用Table 2七问对比把当前论文定位为唯一全覆盖。

- novelty_protection_cn：作者用“首次”“唯一”“通用”等强表述，同时用敏感性分析、经典算法对照和未来工作来防止贡献退化为一次性结果；即使在PGATS DB上不如经典算法，也通过“二进制编码猜想”把反例转化为未来方向，而不是放弃核心主张。

## 可复用研究与写作程序

### structure_steps

#### 1. 1

- step：1

- writing_job_cn：用现实应用说明聚类重要性，把自动聚类簇数未知和多VI冲突定义为挑战。

- research_job_cn：形式化问题，定义数据集、决策变量和可行解空间，引用NP-hard结论。

- required_evidence_cn：能说明问题规模爆炸且现有方法不通用。

- transition_to_next_cn：从“问题难解”转向“需要新模型/方法”。

#### 2. 2

- step：2

- writing_job_cn：提炼现有VI分类和局限，指出单一指标无法应对多目标。

- research_job_cn：选择一组代表性VI并说明其公式和优化方向。

- required_evidence_cn：能够演示多个VI之间方向或几何假设不一致。

- transition_to_next_cn：从“VI局限”转向“需要归一化与聚合”。

#### 3. 3

- step：3

- writing_job_cn：推导归一化方法和聚合目标函数，给出模型约束。

- research_job_cn：选择归一化规则，设计可解释的聚合函数，把DM最低期望写成阈值约束。

- required_evidence_cn：模型在数学上能把任意VI转为可比分数并包含DM偏好。

- transition_to_next_cn：从“模型”转向“由于NP-hard需要启发式求解”。

#### 4. 4

- step：4

- writing_job_cn：说明为何选择特定进化算法，并描述解表示。

- research_job_cn：实现算法，定义与目标函数一致的编码和算子。

- required_evidence_cn：算法能针对每个单VI生成稳定合理的解。

- transition_to_next_cn：从“单算法实现”转向“多个算法需要协作”。

#### 5. 5

- step：5

- writing_job_cn：定义DSS工作流，把用户输入与算法执行串联成步骤。

- research_job_cn：设计决策者在哪一步选VI、设阈值、给权重，以及系统如何把候选集传给下游模型。

- required_evidence_cn：工作流能够从用户输入一直走到唯一输出。

- transition_to_next_cn：从“流程设计”转向“用数据实例演示”。

#### 6. 6

- step：6

- writing_job_cn：用合成数据完整跑通流程，报告每一步的关键表和候选数量。

- research_job_cn：设计生成数据或选择真实数据，执行单目标运行、权重扫描、非支配筛选、DEA和BWM。

- required_evidence_cn：每一步都有输出且最终得到唯一解。

- transition_to_next_cn：从“可行性演示”转向“稳健性”与“外部对照”。

#### 7. 7

- step：7

- writing_job_cn：做参数敏感性分析，并选择外部基准算法进行比较。

- research_job_cn：扰动DM偏好和阈值，运行经典算法，记录性能表格。

- required_evidence_cn：能说明结果在何种条件下稳健、在何种条件下不稳健。

- transition_to_next_cn：从“边界探索”转向“结论中的贡献与未来”。

#### 8. 8

- step：8

- writing_job_cn：在结论中回到引言缺口，逐条匹配框架特征，并列出边界和未来方向。

- research_job_cn：审查证据是否支持每个贡献主张，诚实标注未实现部分。

- required_evidence_cn：每个贡献主张至少对应一个数据表或模型公式。

- transition_to_next_cn：结束全文并为后续研究留接口。

### most_transferable_moves_cn

1. 用文献分类法（三类终选方法）压缩复杂文献并制造缺口

2. 用特征对比表（Q1-Q7）快速定位本文独特性

3. 把用户期望转成数学约束（阈值）

4. 用“离线协作”概念把多个已有算法包装成新DSS特征

5. 先DEA筛有效解、再用BWM做主观唯一化

6. 敏感性分析为排序结果提供稳健性证据

7. 把反例解释为未来编码方向

### resource_intensive_or_nonstandard_parts_cn

1. 需要设计并运行GA/PSO/HS各多次的完整实验，计算成本较高

2. BWM定性评分需要真实DM判断，本文中由作者代替，难以简单复制

3. PGATS等真实数据集需要可访问来源

4. 多数据集、多VI组合、多算法比较会产生大量附录表，需要较多编辑篇幅

5. DEA和BWM的详细计算在OCR版本不完整，复现依赖附录与代码

### what_not_to_copy_superficially_cn

1. 不能只在引言说“缺乏通用框架”而不给文献分类表

2. 不能把“首次”或“唯一”建立在自定义特征表上，需更全面的文献覆盖

3. 不能跳过敏感性分析却声称BWM结果稳健

4. 不能在经典算法反例存在时仍宣称全面优于经典算法

5. 不能把“模型可容纳任意VI”等同于“已测试任意VI”，需在结论区分设计主张与实证主张

6. 不能在没有真实DM参与的情况下把主观评分当作有效外部效度

- single_best_description_of_the_routine_cn：先用形式化模型把多目标聚类的多个有效性指标压缩为带权重幂次的归一化乘积式单目标，再用多个进化算法离线协作生成候选解集，随后用DEA识别有效解、用BWM引入主观偏好得到唯一解，最后用敏感性分析和经典算法对比划定边界，并在结论中把框架特征回扣到引言的三类缺口。

## 分析边界

全文以OCR文本形式提供，部分公式（尤其Eq.28）、DEA计算细节和图像内容可能不完整；补充附录A中有部分表格被截断，可能影响对单目标结果和DEA/BWM计算细节的精确重建；对研究阶段的划分基于章节标题和实验叙述，存在一定主观判断。
