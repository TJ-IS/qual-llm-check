# OrdinoR: A framework for discovering, evaluating, and analyzing organizational models using event logs

- 作者：Jing Yang; Chun Ouyang; Wil M.P. van der Aalst; Arthur H.M. ter Hofstede; Yang Yu
- 年份 / 期刊：2022 / Decision Support Systems
- DOI：10.1016/j.dss.2022.113771
- 源文件：16575_2022_ordinor-a-framework-for-discovering-evaluating-and-analyzing-organizational-models-using-event-l.md
- 论文主类型：build_evaluate_design_science
- 主导写作弧线：requirements_build_evaluate_design_principles
- 置信度：0.8

## 文章级论证概况

- 核心问题：如何从事件日志中发现、评价并分析组织模型，使资源分组不仅呈现静态聚类，而且能与流程执行的多维上下文（案例类型、活动类型、时间类型）相连接，并能以事件日志本身为参照进行严格评价？

- 制品与设计：一个组织模型挖掘框架OrgMiner。核心制品是更丰富的组织模型定义OM=(RG,mem,cap)，其中cap将资源组与执行模式（case type, activity type, time type组合）相连；配套三阶段发现流程（执行模式学习、资源分组发现、执行模式分配）与符合度检查机制（fitness、precision、局部诊断）

- 客观结果：在WABO和BPIC17两个真实日志上共发现并评价24个组织模型；最佳模型的F1分别为0.696（WABO）和0.724（BPIC17）；多维度执行模式学习（尤其是trace clustering）和OverallScore分配方法优于ATonly和FullRecall；局部诊断可定位导致不精确的特定资源组和能力项。

- 核心贡献：提出将资源分组与流程执行知识耦合的组织模型形式化定义，并首次为组织模型引入以输入事件日志为参照的符合度检查（全局度量+局部诊断），从而既支持比较模型发现算法的质量，也支持定位资源分组的偏差和改进机会。

- 整篇论证链：作者先让读者接受动态组织对准确及时理解人力资源分组的现实需求，再指出事件日志提供了数据基础，但现有组织模型挖掘只偏向活动与工作交接维度，很少利用案例和时间维度，发现出的模型也不连接流程执行，且缺少以日志为参照的评价。为填这三个空，作者定义了执行模式和带cap的组织模型，把资源组与案例/活动/时间维度相连，并引入fitness、precision和四个局部诊断度量，构成框架；随后给出一个由三个可配置阶段组成的具体发现方法，实现OrgMiner工具，在WABO和BPIC17上开展全组合实验，用全局符合度比较方法差异，用局部诊断解释低精度模型的问题位置。最后一章将结果收回为框架级贡献，并把模型修复、扩展度量等问题列为未来工作。

## 类型与写作弧线判定

- 论文主类型判定：文章不是从行为理论推假设，而是先识别组织模型挖掘的三类缺口，提出概念框架和正式定义，再构造一个可执行的三阶段发现方法，并用真实事件日志进行评价；这符合设计要求—构建—评价—设计知识的典型设计科学研究弧线。

- 主导写作弧线判定：论文从组织模型挖掘应具备多维度、过程链接和日志可评价三项要求出发，构建了框架与具体方法，用真实日志评价，并提炼出可复用的设计选择（如执行模式桥接、OverallScore分配策略）和评价工具。

## 研究开展程序

- study_or_phase_count：5

- 研究阶段总序列：论文有五个承担不同论证任务的阶段：先做框架层面的概念化和符合度定义，这是后续所有工作的逻辑起点；再提出一个具体发现方法把框架实例化；随后实现软件提供可运行证据；然后在两个真实日志上做全局符合度实验，用对照组合检验方法差异；最后用局部诊断案例解释低精度模型的问题，形成从定义、构建、工具到评价和诊断的累积链条。

### studies_or_phases

#### 1. 框架概念化与符合度定义（Section 3）

- order：1

- name_cn：框架概念化与符合度定义（Section 3）

- question_cn：如何形式化地定义一个既能连接流程执行、又能被事件日志评价的组织模型？

- inputs_and_setting_cn：事件日志的最小属性（case、act、time、res）、流程执行三维度、已有组织模型挖掘概念

- designed_or_compared_object_cn：执行模式（execution mode）、资源日志、OM=(RG,mem,cap)、fitness/precision及四个局部诊断度量

- baseline_control_or_counterfactual_cn：现有组织模型只含资源分组和成员关系，缺少与流程执行模式的显式能力映射

##### objective_metrics

（空）

- analysis_method_cn：形式定义（Definition 1-16）、图例说明、小型示例日志的符合度计算

- main_result_cn：得到一个可表示资源组对案例/活动/时间类型能力的组织模型，以及全局和局部符合度度量

- argumentative_role_cn：确立论文的概念基础和RQ1-RQ3的理论答案，为后面方法和实验提供不可再分的定义框架

- remaining_uncertainty_cn：这些定义尚不能被自动发现，也没有在真实数据上说明性能

- link_to_next_phase_cn：框架的可行性需要一个具体发现方法来证明，因此进入三阶段发现方法

##### evidence_pointers

1. Def.1-Def.7

2. Fig.2-Fig.4

3. Def.8-Def.16

4. Sect.3.5.2局部诊断示例

#### 2. 组织模型发现方法（Section 4）

- order：2

- name_cn：组织模型发现方法（Section 4）

- question_cn：如何用可配置的步骤从事件日志自动发现满足框架定义的组织模型？

- inputs_and_setting_cn：事件日志；执行模式学习方法（ATonly、CT+AT+TT含case attribute和trace clustering）；分组方法（AHC、MOC）；分配方法（FullRecall、OverallScore）

- designed_or_compared_object_cn：三阶段流水线：学习执行模式→基于资源特征矩阵聚类→分配执行模式为组能力

- baseline_control_or_counterfactual_cn：ATonly与CT+AT+TT对照；FullRecall与OverallScore对照；支持重叠分组的MOC与非重叠AHC的机制差异

##### objective_metrics

1. 执行模式数量

2. 资源组数量

3. 概念上的fitness/precision预期

- analysis_method_cn：算法/方法设计、特征矩阵构造、基于现有聚类和社区发现技术的集成

- main_result_cn：提出一个可实例化框架的三阶段方法，并给出FullRecall和OverallScore两种分配策略

- argumentative_role_cn：证明框架不是纯概念，而是能落地为端到端发现过程

- remaining_uncertainty_cn：该方法在真实日志上会产生什么质量的模型，方法间取舍如何，尚未量化

- link_to_next_phase_cn：方法需要软件实现才能运行实验

##### evidence_pointers

1. Fig.6

2. Sect.4.1

3. Sect.4.2

4. Method FullRecall/OverallScore

5. Table 5-6

#### 3. 软件实现（Section 5）

- order：3

- name_cn：软件实现（Section 5）

- question_cn：如何把方法变成可复用、可配置、可扩展的开放工具以支持实验和未来研究？

- inputs_and_setting_cn：Python库OrgMiner、可视化工具

- designed_or_compared_object_cn：每个阶段提供可替换方法：三种执行模式学习、AHC/MOC分组、FullRecall/OverallScore分配

- baseline_control_or_counterfactual_cn：各阶段方法可独立配置，形成不同组合作为相互对照

##### objective_metrics

（空）

- analysis_method_cn：开源原型开发、模块化设计

- main_result_cn：实现了包含全部方法的OrgMiner原型，使系统性实验和复现成为可能

- argumentative_role_cn：架起方法与实验之间的桥梁，体现设计科学的可执行性

- remaining_uncertainty_cn：工具本身不是贡献重点，方法的参数敏感性需在实验中处理

- link_to_next_phase_cn：实现之后便可在真实日志上运行全组合实验

##### evidence_pointers

1. Sect.5

2. OrgMiner模块说明

#### 4. 真实日志全局符合度实验（Section 6.1-6.3.1）

- order：4

- name_cn：真实日志全局符合度实验（Section 6.1-6.3.1）

- question_cn：不同方法选择如何影响所发现组织模型的全局符合度？

- inputs_and_setting_cn：WABO（荷兰建筑许可接收阶段）和BPIC17（荷兰金融机构贷款申请）两个公开真实日志；预处理后分别为1434/31509个案例、8577/475306个事件

- designed_or_compared_object_cn：执行模式学习方法、分组方法、分配方法的全部组合，共24个组织模型

- baseline_control_or_counterfactual_cn：每个日志以最优符合度模型为基准；逐阶段固定其他阶段方法进行比较；FullRecall可视为过度拟合的极端对照

##### objective_metrics

1. fitness

2. precision

3. F1-score

- analysis_method_cn：全组合实验、交叉验证确定组数、网格搜索OverallScore参数、阶段式对比、科学工作流自动化

- main_result_cn：最优模型分别为WABO配置CAT(tc)-MOC-OS（f=.876,p=.577,F1=.696）和BPIC17配置CAT(tc)-AHC-OS（f=.831,p=.641,F1=.724）；ATonly提高fitness但降低precision；trace clustering优于单案例属性；MOC因重叠提高fitness降低precision；FullRecall达到fitness=1但precision极低，类似过程挖掘中的flower model

- argumentative_role_cn：证明所提出的符合度指标能评价发现算法，并能产生可解释的方法选择知识

- remaining_uncertainty_cn：全局符合度只说明模型总体与日志偏离程度，不说明偏差具体发生在哪些组和能力上

- link_to_next_phase_cn：需要局部诊断来定位低精度模型的具体问题

##### evidence_pointers

1. Table 7-11

2. Sect.6.1

3. Sect.6.2

4. Sect.6.3.1

#### 5. 局部诊断分析（Section 6.3.2）

- order：5

- name_cn：局部诊断分析（Section 6.3.2）

- question_cn：如何利用局部诊断度量定位并解释组织模型中的不精确来源？

- inputs_and_setting_cn：从WABO实验中选出的极端低精度模型：CT+AT+TT(case attribute)-MOC-FullRecall，fitness=1.0，precision=0.036，F1=0.069

- designed_or_compared_object_cn：模型内每个group-mode对的RelFocus、RelStake、Coverage、MemContr得分，按排序识别风险能力项

- baseline_control_or_counterfactual_cn：以事件日志中实际发生的资源行为作为参照，而不是以先验组织知识为参照

##### objective_metrics

1. RelFocus

2. RelStake

3. Coverage

4. MemContr

- analysis_method_cn：单案例诊断、排序和可视化（图8-10）

- main_result_cn：在“Group 3”的133个能力执行模式中，只有46个的覆盖率超过0.5，许多能力只由一两个成员执行；部分能力虽然被模型赋予组，但组的相对份额低于5%，说明这些能力与实际日志不符

- argumentative_role_cn：展示局部诊断能定位模型哪里过度放宽、哪里偏离真实资源行为，从而闭合从全局评价到局部修复的分析链条

- remaining_uncertainty_cn：文章没有在实际流程中实施模型修复或验证修复后的效果；也未测试规范化模型下的干预意义

- link_to_next_phase_cn：诊断结果自然引出结论部分的未来工作：按诊断结果修复/改进组织模型

##### evidence_pointers

1. Sect.6.3.2

2. Fig.8-Fig.10

3. WABO低精度模型配置

## 各部分修辞架构

### abstract_moves

1. CONTEXT: 合理的人力资源结构可提升组织运营效率

2. PHENOMENON: 现代组织需要及时理解人力资源分组，但静态组织图不够

3. PRIOR_KNOWLEDGE: 过程挖掘可利用信息系统中的事件日志提取资源行为知识

4. GAP: 现有组织模型发现与过程执行上下文联系有限，且缺少以日志为参照的严格评价

5. RQ_OR_OBJECTIVE: 提出基于更丰富组织模型定义的框架

6. DESIGN_FEATURE: 引入组织模型符合度检查概念，支持模型的发现与评价

7. STUDY_OVERVIEW: 在真实事件日志上实施发现方法并开展实验

### introduction_moves

1. CONTEXT: 组织由雇员群体构成，流程导向的协作是组织目标实现方式

2. PRACTICAL_STAKES: 动态环境要求灵活的人力资源结构，静态组织图无法满足

3. PRIOR_KNOWLEDGE: 信息系统中的事件日志蕴含流程执行和资源参与信息

4. PHENOMENON: 过程挖掘中的组织模型挖掘旨在发现相似资源组

5. LIMITATION: 现有发现方法主要基于活动和交接关系，很少用案例与时间维度

6. LIMITATION: 发现出的模型只描述资源聚类，缺乏与流程执行动态的连接

7. LIMITATION: 评价依赖领域知识或技术指标，从未直接对照输入日志

8. RQ_OR_OBJECTIVE: 提出RQ1-RQ3，分别对应多维发现、过程连接、日志评价

9. STUDY_OVERVIEW: 预告框架、方法、实验与开源软件等贡献

### theory_and_knowledge_moves

1. PRIOR_KNOWLEDGE: 组织挖掘分为组织模型、社交网络、规则和行为画像四类

2. BENCHMARK_OR_CONTRAST: 从过程执行维度、过程链接、评价策略三个视角建立文献评价标准

3. LIMITATION: 多数方法仅用活动信息，案例和时间维度很少被利用

4. LIMITATION: 只有少数模型把资源组与过程活动相连接

5. LIMITATION: 三种既有评价策略均未以输入日志为直接参照

6. MECHANISM: 执行模式按案例类型、活动类型、时间类型把可能事件分块

7. MECHANISM: cap使资源组与执行模式相连，从而把组织结构与过程行为挂钩

8. MECHANISM: fitness衡量日志行为被模型允许的比例，precision衡量模型允许行为超出日志的程度

9. MECHANISM: 局部诊断通过相对焦点、相对份额、覆盖率、成员贡献定位偏差

### artifact_design_moves

1. REQUIREMENT: 事件日志至少有case,act,time三个强制属性，res为重要可选属性

2. DESIGN_FEATURE: 定义执行模式为三维组合，并在图2中用事件立方体可视化

3. DESIGN_FEATURE: 引入资源日志，把原始事件投影到资源×执行模式的多集

4. DESIGN_FEATURE: 组织模型由资源组、成员关系、执行模式能力三部分组成

5. REQUIREMENT: 发现执行模式时需考虑日志粒度与分析目的，因此提供ATonly和CT+AT+TT

6. DESIGN_FEATURE: 基于资源特征矩阵做聚类/社区发现，形成资源组

7. DESIGN_FEATURE: FullRecall简单但易过度泛化，OverallScore用相对份额与覆盖率加权筛选能力

8. DESIGN_FEATURE: 原型OrgMiner支持各阶段方法可配置和扩展

### evaluation_moves

1. BENCHMARK_OR_CONTRAST: 选择WABO和BPIC17两个公开真实日志作为实验数据

2. METHOD_JUSTIFICATION: 测试所有方法组合以系统评价各阶段影响

3. BENCHMARK_OR_CONTRAST: 每个日志以最优符合度模型为基准，逐阶段比较

4. RESULT: 最优配置来自trace clustering与OverallScore

5. RESULT: ATonly因模式更粗而fitness高、precision低

6. RESULT: MOC因重叠组而比AHC更灵活，fitness更高但precision更低

7. RESULT: FullRecall像flower model，fitness=1但precision极低

8. RESULT: 局部诊断发现低精度模型的许多能力覆盖率低或组相对份额低

### discussion_and_contribution_moves

1. CONTRIBUTION: 组织模型定义覆盖结构（成员）和行为（能力），连接了资源分析与流程分析

2. CONTRIBUTION: 符合度检查能同时做程度度量与原因诊断，区分于只评价发现算法

3. CONTRIBUTION: 实验展示了符合度工具可用于发现方法比较和偏差分析

4. BOUNDARY_CONDITION: 模型解释取决于描述性还是规范性目的

5. LIMITATION_AND_FUTURE: 未来可发展更有效的发现方法、扩展符合度度量、根据局部诊断修复模型

6. LIMITATION_AND_FUTURE: 标准三类过程挖掘均可针对组织模型扩展

## 理论/知识到设计的翻译

### 知识/理论基础

1. 过程挖掘中的组织模型挖掘（Song & van der Aalst等）

2. 过程立方体/多维事件数据分析（van der Aalst）

3. 过程模型符合度检查中的fitness/precision思想

4. 业务流程管理中的资源类概念：组内成员可互换执行相似工作

5. 数据挖掘中的聚类分析、社区发现、交叉验证和网格搜索

- 理论—设计耦合：partial

- 耦合判定理由：文章没有从行为理论或组织理论推出假设，设计主要来自过程挖掘领域概念、工程启发式和现有技术集成；但领域知识（资源类、过程立方体、过程符合度）确实塑造了核心定义和评价方法，因此属于部分耦合。

- 理论到设计翻译链：现有组织模型只解释活动维度→需要多维度过程执行抽象→设计执行模式（案例类型×活动类型×时间类型）→把事件日志投影为资源日志→资源组通过cap与执行模式相连→用fitness检查日志行为是否被模型允许；用precision检查模型是否允许过多候选资源；用局部诊断定位具体偏差。

### mapping_table

#### 1. 1

- theory_or_knowledge_claim_cn：资源类是指组内成员在流程执行中可互换完成相似工作的资源集合

- mechanism_cn：资源行为相似性可由他们执行过的执行模式体现

- design_requirement_cn：需要把资源的历史参与抽象成特征向量

- artifact_choice_cn：构建资源×执行模式频率矩阵

- evaluated_contrast_cn：AHC（非重叠）与MOC（重叠）两种分组方法

- objective_result_cn：在真实日志上MOC模型通常fitness更高、precision更低

##### evidence_pointers

1. Sect.4.2

2. Table 5

3. Table 10

#### 2. 2

- theory_or_knowledge_claim_cn：事件日志可从案例、活动、时间三个维度切片、切块和上卷

- mechanism_cn：相同事件执行模式可在三维空间形成事件立方体

- design_requirement_cn：组织模型发现应能利用案例和时间维度，而不只是活动维度

- artifact_choice_cn：执行模式(ct,at,tt)和资源日志

- evaluated_contrast_cn：ATonly vs CT+AT+TT（case attribute vs trace clustering）

- objective_result_cn：ATonly获得更高fitness但更低precision；trace clustering通常比单案例属性更均衡

##### evidence_pointers

1. Sect.3.2

2. Sect.4.1

3. Table 9

#### 3. 3

- theory_or_knowledge_claim_cn：过程模型符合度检查用fitness和precision对比模型行为与日志行为

- mechanism_cn：fitness看日志中事件是否被模型允许；precision看模型是否允许过多未在日志中发生的行为

- design_requirement_cn：组织模型也需要与输入日志进行逐事件对比

- artifact_choice_cn：conforming event、candidate resource、fitness、precision

- evaluated_contrast_cn：不同发现方法组合在WABO和BPIC17上的fitness/precision/F1

- objective_result_cn：指标能区分方法差异并可生成合理配置建议

##### evidence_pointers

1. Sect.3.5.1

2. Table 8-11

#### 4. 4

- theory_or_knowledge_claim_cn：仅有全局符合度无法告诉偏差在哪里，过程挖掘常用局部诊断回放日志

- mechanism_cn：对每个资源组和动作模式计算参与强度、覆盖程度和成员贡献

- design_requirement_cn：需要可在模型上定位偏差的局部度量

- artifact_choice_cn：RelFocus、RelStake、Coverage、MemContr

- evaluated_contrast_cn：对WABO低精度模型的高覆盖组与低份额组进行诊断

- objective_result_cn：识别出大量能力项只有一两名成员实际执行或组贡献极小

##### evidence_pointers

1. Sect.3.5.2

2. Sect.6.3.2

3. Fig.8-10

## 评价逻辑

### evaluation_modes

1. 形式定义+小型示例验证

2. 真实事件日志上的系统实验

3. 全组合方法对照

4. 单案例局部诊断分析

- why_these_evaluations_cn：形式示例说明概念可计算；真实日志实验说明框架在非合成数据上可行；阶段式对照使每个方法选择的贡献可分离；局部诊断说明评价不限于得到一个总分，还能定位问题。

- benchmark_and_contrast_chain_cn：先用每个日志的最优模型作基准（Table 8），再逐阶段固定其他因素比较ATonly/CT+AT+TT、MOC/AHC、OverallScore/FullRecall（Table 9-11）。这些比较不断用fitness/precision/F1解释机制，随后选一个极端低精度模型进行局部诊断，把偏差落实到具体group-mode对。

### claim_evidence_ledger

#### 1. 新定义的组织模型能连接资源组与流程执行模式

- claim_cn：新定义的组织模型能连接资源组与流程执行模式

- evidence_cn：Def.7、Fig.3、Fig.4示例；真实日志发现模型中包含cap信息

- status_cn：有证据支持，但属于表示能力而非外部有效性

#### 2. 符合度检查能评价发现出来的组织模型

- claim_cn：符合度检查能评价发现出来的组织模型

- evidence_cn：Table 8-11的fitness/precision/F1结果及阶段比较

- status_cn：有证据支持，尚未与组织真实结构对照

#### 3. ATonly因模式更粗糙而fitness高、precision低

- claim_cn：ATonly因模式更粗糙而fitness高、precision低

- evidence_cn：Table 9显示ATonly的fitness高于CT+AT+TT但precision更低，且模式数远少

- status_cn：有证据且提供机制解释

#### 4. MOC的重叠会导致fitness高、precision低

- claim_cn：MOC的重叠会导致fitness高、precision低

- evidence_cn：Table 10中WABO和BPIC17的MOC相对AHC结果

- status_cn：有证据，但两个日志上模式不完全一致，解释合理

#### 5. FullRecall会产生fitness=1但precision极差的过灵活模型

- claim_cn：FullRecall会产生fitness=1但precision极差的过灵活模型

- evidence_cn：Table 11，两个日志上FullRecall的fitness均为1.0，precision分别为0.067和0.169

- status_cn：强证据支持

#### 6. 局部诊断能定位模型不精确的具体来源

- claim_cn：局部诊断能定位模型不精确的具体来源

- evidence_cn：WABO低精度模型中Group 3的133个能力只有46个覆盖率>0.5；部分能力组相对份额<5%

- status_cn：有证据，但仅基于一个低精度模型案例

- internal_validity_strategy_cn：通过逐阶段固定其他变量的比较分离方法效果；使用交叉验证选择资源组数；对OverallScore做网格搜索；预处理去除重复事件以统一计数。

- external_validity_strategy_cn：使用两个不同领域、规模差异大的公开真实日志（市政许可和金融贷款）来增加一般性；同时开源实现便于复现和扩展。

- what_is_not_actually_tested_cn：没有测试发现模型是否匹配组织真实结构；没有测试规范模型下干预资源行为的管理效果；没有实施模型修复并验证修复后是否符合度提高；也没有检验不同执行模式定义对下游管理决策的影响。

## 贡献闭环

- technical_claim_cn：提出了可用于事件日志的组织模型符合度检查技术，包括事件级fitness、候选资源precision和四个局部诊断度量。

- artifact_claim_cn：新增cap组件并定义执行模式的组织模型OM=(RG,mem,cap)使资源组可与案例/活动/时间维度相连，是发现与分析可计算的基础。

- mechanism_claim_cn：执行模式越粗，越容易fit日志但会放大候选资源集从而降低precision；重叠组提升灵活性而牺牲precision；低覆盖或低相对份额的能力项是模型不精确的主要来源。

- boundary_claim_cn：演示范围是两个真实事件日志；fitness只考虑有资源信息的事件；precision定义依赖候选资源集合；模型解释和修复建议取决于模型是描述性还是规范性。

- reusable_design_knowledge_cn：用执行模式作为事件日志与资源分组之间的桥接层；用fitness/precision双指标比较不同发现方法；用局部诊断把全局偏差落到资源组和能力项。

- theoretical_contribution_cn：将组织模型从单纯的结构聚类扩展为结构+行为联合表示，并把过程挖掘中的符合度思想移植到组织视角，从而连接组织模型挖掘与过程模型挖掘。

- how_discussion_closes_intro_gap_cn：结论部分直接回应引言的三类缺口：cap对应RQ2和过程连接，多维执行模式对应RQ1，符合度检查对应RQ3；实验部分则展示这些缺口被填补后的用途（方法比较和偏差分析）。

- overclaim_or_unsupported_leaps_cn：“严格评价”可能被高估，因为fitness/precision只说明与日志的一致性，不等于组织有效性；局部诊断只展示一个案例，却外推为通用改进路径；将trace clustering优于单案例属性的结论建立于两个日志的具体属性选择之上，泛化需要更多证据。

## 句级写作动作图谱

### 1. P1 S1-S2

- order：1

- section：Introduction

- locator：P1 S1-S2

- move_code：CONTEXT

- paraphrase_cn：现代组织由多个员工群体构成，通常通过端到端业务流程协作来交付价值。

- rhetorical_function_cn：把组织、流程、人力资源三个主题放在同一个现实场景中。

- depends_on_cn：不需要前文，是文章自然的起点。

- sets_up_cn：为组织资源分组的重要性作铺垫。

- evidence_pointer：Introduction P1

### 2. P1 S3-S5

- order：2

- section：Introduction

- locator：P1 S3-S5

- move_code：PRACTICAL_STAKES

- paraphrase_cn：动态环境要求组织不断调整人力资源结构，灵活合理的资源分组有助于应对挑战，因此需要准确及时地理解资源分组。

- rhetorical_function_cn：说明该研究主题的现实后果，使问题不再只是技术兴趣。

- depends_on_cn：承接组织依赖流程协作的背景。

- sets_up_cn：推出静态组织图不能满足需求的判断。

- evidence_pointer：Introduction P1

### 3. P2 S1-S4

- order：3

- section：Introduction

- locator：P2 S1-S4

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：信息系统中的事件日志记录活动、时间戳、流程实例和资源，可反映员工如何参与流程。

- rhetorical_function_cn：引入数据基础，说明解决动态理解问题的可能路径。

- depends_on_cn：从需求转向可用数据。

- sets_up_cn：为过程挖掘和组织模型挖掘登场提供依据。

- evidence_pointer：Introduction P2

### 4. P3 S1-S2

- order：4

- section：Introduction

- locator：P3 S1-S2

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：过程挖掘提供大量分析事件日志的方法；其中组织模型挖掘关注从日志中发现相似资源组。

- rhetorical_function_cn：界定本文所在研究分支。

- depends_on_cn：建立在日志数据可用之上。

- sets_up_cn：随后指出该分支的现有不足。

- evidence_pointer：Introduction P3

### 5. P4 开头至Fig.1前

- order：5

- section：Introduction

- locator：P4 开头至Fig.1前

- move_code：GAP

- paraphrase_cn：现有组织模型发现主要依据资源的活动相似性和活动间工作交接，案例与时间维度很少被考虑。

- rhetorical_function_cn：构造第一个研究缺口。

- depends_on_cn：对现有方法分类判断。

- sets_up_cn：指向RQ1关于多维发现的问题。

- evidence_pointer：Introduction P4

### 6. P4 中段

- order：6

- section：Introduction

- locator：P4 中段

- move_code：GAP

- paraphrase_cn：发现出的组织模型通常只是资源聚类，缺少资源组与流程执行动态之间的连接，因而难以进行后续行为与绩效分析。

- rhetorical_function_cn：构造第二个研究缺口。

- depends_on_cn：前一缺口的补充。

- sets_up_cn：指向RQ2关于过程连接的问题。

- evidence_pointer：Introduction P4

### 7. P4 末尾

- order：7

- section：Introduction

- locator：P4 末尾

- move_code：GAP

- paraphrase_cn：发现结果评价要么依赖领域知识，要么依赖算法特有指标，没有将模型与输入事件日志进行对比。

- rhetorical_function_cn：构造第三个研究缺口。

- depends_on_cn：对文献评价策略的概括。

- sets_up_cn：指向RQ3关于日志作为参照的问题。

- evidence_pointer：Introduction P4

### 8. P4 末RQ列表

- order：8

- section：Introduction

- locator：P4 末RQ列表

- move_code：RQ_OR_OBJECTIVE

- paraphrase_cn：提出RQ1如何多维发现、RQ2如何连接资源组与流程执行、RQ3如何以日志评价模型。

- rhetorical_function_cn：把三个缺口压缩成可操作的研究问题。

- depends_on_cn：三个缺口描述。

- sets_up_cn：决定全文框架和评价结构。

- evidence_pointer：Introduction RQ1-RQ3

### 9. P5

- order：9

- section：Introduction

- locator：P5

- move_code：STUDY_OVERVIEW

- paraphrase_cn：论文将提出包含多维定义与符合度检查的框架、一个具体发现方法、真实日志实验和开源软件。

- rhetorical_function_cn：预告整体研究动作。

- depends_on_cn：研究问题列表。

- sets_up_cn：让读者知道每个RQ由哪些章节支撑。

- evidence_pointer：Introduction P5

### 10. P6

- order：10

- section：Introduction

- locator：P6

- move_code：TRANSITION

- paraphrase_cn：说明后续章节如何组织：相关工作、框架、方法、实现、评价、结论。

- rhetorical_function_cn：提供全文导航。

- depends_on_cn：贡献预告。

- sets_up_cn：为Section 2的文献审查做引导。

- evidence_pointer：Introduction P6

### 11. Sect.2 P1

- order：11

- section：Related Work

- locator：Sect.2 P1

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：组织挖掘可分为组织模型、社交网络、规则和行为画像四类。

- rhetorical_function_cn：界定文献位置，指出本文聚焦第一类。

- depends_on_cn：过程挖掘研究背景。

- sets_up_cn：根据研究方向设定评述框架。

- evidence_pointer：Sect.2 P1

### 12. Sect.2 P2

- order：12

- section：Related Work

- locator：Sect.2 P2

- move_code：BENCHMARK_OR_CONTRAST

- paraphrase_cn：作者从过程执行维度、过程链接、评价策略三个视角建立文献评价标准。

- rhetorical_function_cn：为Table 1的系统性对照提供透明标准。

- depends_on_cn：三个研究问题。

- sets_up_cn：导出的三个缺口有了可比较的文献证据。

- evidence_pointer：Sect.2 P2

### 13. Sect.2 问题1讨论

- order：13

- section：Related Work

- locator：Sect.2 问题1讨论

- move_code：LIMITATION

- paraphrase_cn：多数现有方法只用活动信息，案例和时间维度很少被利用，因此发现不了按案例或班次分组的模式。

- rhetorical_function_cn：用文献证据支持第一个缺口。

- depends_on_cn：Table 1的维度列。

- sets_up_cn：支撑RQ1。

- evidence_pointer：Sect.2 Q1段落

### 14. Sect.2 问题2讨论

- order：14

- section：Related Work

- locator：Sect.2 问题2讨论

- move_code：LIMITATION

- paraphrase_cn：虽然少数工作把资源组与活动相连，但把组放在完整流程执行情境中的问题仍未解决。

- rhetorical_function_cn：用文献证据支持第二个缺口。

- depends_on_cn：Table 1的链接列。

- sets_up_cn：支撑RQ2。

- evidence_pointer：Sect.2 Q2段落

### 15. Sect.2 问题3讨论

- order：15

- section：Related Work

- locator：Sect.2 问题3讨论

- move_code：LIMITATION

- paraphrase_cn：现有一类评价用领域知识，另一类用技术指标，还有一类只做可行性验证；没有研究用输入日志直接评价发现模型。

- rhetorical_function_cn：第三个缺口得到文献梳理支持。

- depends_on_cn：Table 1的评价列。

- sets_up_cn：支撑RQ3。

- evidence_pointer：Sect.2 Q3段落

### 16. Sect.2 末尾

- order：16

- section：Related Work

- locator：Sect.2 末尾

- move_code：TRANSITION

- paraphrase_cn：本文针对这三个开放问题提出框架与符合度检查概念。

- rhetorical_function_cn：把评述收束为本文任务，并引出下一节。

- depends_on_cn：三个缺口。

- sets_up_cn：开启Section 3框架。

- evidence_pointer：Sect.2最后一段

### 17. Sect.3 opener P1

- order：17

- section：Framework

- locator：Sect.3 opener P1

- move_code：THEORY_INTRO

- paraphrase_cn：业务流程由一组活动构成，案例是流程的一次执行，相似案例可形成案例类型。

- rhetorical_function_cn：建立后续定义的业务语言。

- depends_on_cn：过程挖掘的基本概念。

- sets_up_cn：为执行模式和案例类型定义提供术语。

- evidence_pointer：Sect.3开头

### 18. Sect.3 opener P2

- order：18

- section：Framework

- locator：Sect.3 opener P2

- move_code：RQ_OR_OBJECTIVE

- paraphrase_cn：本节将引入把资源组链接到活动、案例类型和时间段的更丰富组织模型，并建立基于日志的符合度评价。

- rhetorical_function_cn：以总结句进入框架细节。

- depends_on_cn：引言中的RQ1-RQ3。

- sets_up_cn：引导读者从定义到符合度框架。

- evidence_pointer：Sect.3 opening P2

### 19. Sect.3.1 Def.1-Def.2

- order：19

- section：Framework

- locator：Sect.3.1 Def.1-Def.2

- move_code：DESIGN_FEATURE

- paraphrase_cn：事件日志被形式化为事件、属性和属性取值函数；case、act、time为强制属性，res为可选属性。

- rhetorical_function_cn：给日志数据一个可计算的形式基础。

- depends_on_cn：过程挖掘日志标准。

- sets_up_cn：支持后面执行模式与资源日志的定义。

- evidence_pointer：Def.1-Def.2

### 20. Sect.3.2 Def.3-Def.4 及Fig.2

- order：20

- section：Framework

- locator：Sect.3.2 Def.3-Def.4 及Fig.2

- move_code：DESIGN_FEATURE

- paraphrase_cn：案例类型、活动类型、时间类型各自划分对应论域，三者组合成为执行模式，把事件空间切成事件立方体。

- rhetorical_function_cn：将多维流程信息转化为可计算的分组单元。

- depends_on_cn：case/act/time属性的正式定义。

- sets_up_cn：为资源日志和cap提供维度。

- evidence_pointer：Def.3-Def.4, Fig.2

### 21. Sect.3.3 Def.5-Def.6 与Table 3

- order：21

- section：Framework

- locator：Sect.3.3 Def.5-Def.6 与Table 3

- move_code：DESIGN_FEATURE

- paraphrase_cn：资源日志是资源事件的multiset，由事件日志和预先定义的执行模式派生而来。

- rhetorical_function_cn：把原始日志转换到资源视角，便于资源聚类。

- depends_on_cn：执行模式定义。

- sets_up_cn：特征矩阵的输入。

- evidence_pointer：Def.5-Def.6, Table 3

### 22. Sect.3.4 Def.7与Fig.3

- order：22

- section：Framework

- locator：Sect.3.4 Def.7与Fig.3

- move_code：DESIGN_FEATURE

- paraphrase_cn：组织模型定义为一个三元组RG、mem、cap，其中cap把资源组映射到它们可执行的执行模式集合。

- rhetorical_function_cn：这是全文最核心的制品定义。

- depends_on_cn：资源和执行模式概念。

- sets_up_cn：cap使资源组与流程执行挂钩，并使符合度检查可定义。

- evidence_pointer：Def.7, Fig.3

### 23. Sect.3.4解释段

- order：23

- section：Framework

- locator：Sect.3.4解释段

- move_code：REQUIREMENT

- paraphrase_cn：cap之所以必要，是因为它捕获与资源分组相关的过程执行知识，建立组织模型与流程之间的连接。

- rhetorical_function_cn：解释新组件不是锦上添花，而是为RQ2服务。

- depends_on_cn：Def.7。

- sets_up_cn：联系引言中的第二个缺口。

- evidence_pointer：Sect.3.4

### 24. Sect.3.5.1 Def.8-Def.9

- order：24

- section：Framework

- locator：Sect.3.5.1 Def.8-Def.9

- move_code：MECHANISM

- paraphrase_cn：fitness定义为事件日志中符合模型允许的资源执行的事件数占所有有资源事件数的比例。

- rhetorical_function_cn：把“模型能否解释日志”转化为可计算的全局指标。

- depends_on_cn：cap定义和事件日志。

- sets_up_cn：与precision形成互补的全局符合度。

- evidence_pointer：Def.8-Def.9

### 25. Sect.3.5.1 Def.10-Def.12

- order：25

- section：Framework

- locator：Sect.3.5.1 Def.10-Def.12

- move_code：MECHANISM

- paraphrase_cn：precision通过候选资源集衡量模型是否允许太多未被日志观察到的资源行为。

- rhetorical_function_cn：弥补fitness只看“够不够”而不管“多不多”的缺陷。

- depends_on_cn：candidate resource和allowed event定义。

- sets_up_cn：全局F1评估和后续方法比较。

- evidence_pointer：Def.10-Def.12

### 26. Sect.3.5.2 Def.13-Def.16

- order：26

- section：Framework

- locator：Sect.3.5.2 Def.13-Def.16

- move_code：MECHANISM

- paraphrase_cn：四个局部度量分别衡量组对某类工作的相对焦点、相对份额、组内成员覆盖率和成员贡献。

- rhetorical_function_cn：将偏差从总体分数下沉到组和模式层面。

- depends_on_cn：资源和执行模式概念。

- sets_up_cn：为局部诊断实验提供工具。

- evidence_pointer：Def.13-Def.16

### 27. Sect.3.5末尾

- order：27

- section：Framework

- locator：Sect.3.5末尾

- move_code：BOUNDARY_CONDITION

- paraphrase_cn：符合度结果的解释取决于模型是描述性还是规范性：描述性模型需要修改以贴合日志，规范性模型则提示绩效问题。

- rhetorical_function_cn：界定指标的使用边界，防止把日志一致性直接等同于组织正确性。

- depends_on_cn：局部诊断示例。

- sets_up_cn：为结论部分的未来工作和边界说明提供理论依据。

- evidence_pointer：Sect.3.5末尾

### 28. Sect.3.6 Fig.5

- order：28

- section：Framework

- locator：Sect.3.6 Fig.5

- move_code：STUDY_OVERVIEW

- paraphrase_cn：框架以事件日志为输入，支持发现、符合度检查和扩展分析，并可用符合度结果修订模型或做What-if分析。

- rhetorical_function_cn：把前面的定义集成为一个可操作的研究框架。

- depends_on_cn：组织模型和符合度定义。

- sets_up_cn：限定本论文只深化发现和符合度两步。

- evidence_pointer：Fig.5, Sect.3.6

### 29. Sect.4 opener Fig.6

- order：29

- section：Approach

- locator：Sect.4 opener Fig.6

- move_code：DESIGN_FEATURE

- paraphrase_cn：方法分成学习执行模式、发现资源分组、分配执行模式三个阶段，最终输出组织模型。

- rhetorical_function_cn：把框架落实为可实现的流水线。

- depends_on_cn：框架步骤(1a)-(1c)。

- sets_up_cn：后面各小节详细说明每个阶段。

- evidence_pointer：Fig.6, Sect.4 opener

### 30. Sect.4.1

- order：30

- section：Approach

- locator：Sect.4.1

- move_code：REQUIREMENT

- paraphrase_cn：学习执行模式受日志信息粒度和分析目的约束；文中给出ATonly和CT+AT+TT两种示例方法。

- rhetorical_function_cn：承认执行模式学习没有通用解，用两个可操作方法表达设计空间。

- depends_on_cn：执行模式定义。

- sets_up_cn：为实验中的方法组合提供变量。

- evidence_pointer：Sect.4.1, Table 4

### 31. Sect.4.2

- order：31

- section：Approach

- locator：Sect.4.2

- move_code：DESIGN_FEATURE

- paraphrase_cn：资源分组通过资源特征矩阵实现，矩阵灵感来自performer-by-activity矩阵，行是资源，列是不同执行模式的频率。

- rhetorical_function_cn：说明如何把资源行为数字化并接入聚类技术。

- depends_on_cn：资源日志。

- sets_up_cn：AHC和MOC等分组算法有了输入。

- evidence_pointer：Sect.4.2, Table 5

### 32. Sect.4.2末段

- order：32

- section：Approach

- locator：Sect.4.2末段

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：是否允许组重叠取决于现代组织中一人多角色的事实，因此需要重叠聚类或重叠社区发现。

- rhetorical_function_cn：为MOC的引入提供组织依据，也为后面的precision差异埋下伏笔。

- depends_on_cn：资源分组方法选择。

- sets_up_cn：解释实验里MOC与AHC的对比。

- evidence_pointer：Sect.4.2末尾

### 33. Sect.4.3 FullRecall

- order：33

- section：Approach

- locator：Sect.4.3 FullRecall

- move_code：DESIGN_FEATURE

- paraphrase_cn：FullRecall把任一成员执行过的执行模式都赋给该组作为能力，确保覆盖日志中所有已观察行为。

- rhetorical_function_cn：提供一个简单但有明显缺陷的基线策略。

- depends_on_cn：资源分组输出。

- sets_up_cn：引出OverallScore及其权衡参数。

- evidence_pointer：Method FullRecall

### 34. Sect.4.3 OverallScore

- order：34

- section：Approach

- locator：Sect.4.3 OverallScore

- move_code：REQUIREMENT

- paraphrase_cn：为避免FullRecall把少数成员做过的工作当成全组共享，需要只看组参与度较高且覆盖多数成员的执行模式。

- rhetorical_function_cn：用两个诊断量反向生成设计要求。

- depends_on_cn：RelStake和Coverage定义。

- sets_up_cn：OverallScore的加权阈值公式。

- evidence_pointer：Sect.4.3 OverallScore前段

### 35. Sect.4.3 Method OverallScore

- order：35

- section：Approach

- locator：Sect.4.3 Method OverallScore

- move_code：DESIGN_FEATURE

- paraphrase_cn：OverallScore用相对份额和覆盖率的加权平均值是否达到阈值来决定cap(rg)。

- rhetorical_function_cn：把设计需求变成参数化方法。

- depends_on_cn：RelStake/Coverage。

- sets_up_cn：实验中网格搜索ω和λ。

- evidence_pointer：Method OverallScore, Table 6

### 36. Sect.5 P1

- order：36

- section：Implementation

- locator：Sect.5 P1

- move_code：DESIGN_FEATURE

- paraphrase_cn：开发了Python库OrgMiner和可视化工具，实现发现方法和符合度检查。

- rhetorical_function_cn：把算法变成可运行资产。

- depends_on_cn：方法定义。

- sets_up_cn：为全组合实验提供执行环境。

- evidence_pointer：Sect.5

### 37. Sect.5 方法列表

- order：37

- section：Implementation

- locator：Sect.5 方法列表

- move_code：DESIGN_FEATURE

- paraphrase_cn：执行模式学习有三种方法，分组有AHC和MOC，分配有FullRecall和OverallScore，均可独立配置。

- rhetorical_function_cn：明确工具的可配置空间。

- depends_on_cn：实现设计。

- sets_up_cn：确定实验中方法组合总数。

- evidence_pointer：Sect.5

### 38. Sect.6.1

- order：38

- section：Evaluation

- locator：Sect.6.1

- move_code：BENCHMARK_OR_CONTRAST

- paraphrase_cn：选用CoSeLoG项目的WABO和BPIC17两个公开真实日志，覆盖市政许可和金融贷款两个领域。

- rhetorical_function_cn：建立外部有效性基础。

- depends_on_cn：日志需满足四个基本属性。

- sets_up_cn：为Table 7的描述统计和后续实验提供数据。

- evidence_pointer：Sect.6.1, Table 7

### 39. Sect.6.2 P1-P2

- order：39

- section：Evaluation

- locator：Sect.6.2 P1-P2

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：实验中测试三个阶段的全部组合，并用科学工作流自动化实验过程。

- rhetorical_function_cn：说明实验设计的系统性和可复现性。

- depends_on_cn：OrgMiner工具。

- sets_up_cn：后续四个比较表的产生方式。

- evidence_pointer：Sect.6.2

### 40. Sect.6.2 参数设置

- order：40

- section：Evaluation

- locator：Sect.6.2 参数设置

- move_code：BENCHMARK_OR_CONTRAST

- paraphrase_cn：用交叉验证确定组数；对OverallScore做网格搜索，选择能使符合度最优的参数。

- rhetorical_function_cn：减少参数选择对方法比较的污染。

- depends_on_cn：实验设计。

- sets_up_cn：保证不同方法的比较相对公平。

- evidence_pointer：Sect.6.2

### 41. Sect.6.3 Table 8前

- order：41

- section：Evaluation

- locator：Sect.6.3 Table 8前

- move_code：RESULT

- paraphrase_cn：共发现并评价24个组织模型，两个日志的最优模型分别来自trace clustering与OverallScore组合。

- rhetorical_function_cn：给出全文的总体实验结果。

- depends_on_cn：全组合实验。

- sets_up_cn：作为后续逐阶段比较的基准。

- evidence_pointer：Sect.6.3, Table 8

### 42. Sect.6.3.1 Table 9

- order：42

- section：Evaluation

- locator：Sect.6.3.1 Table 9

- move_code：RESULT

- paraphrase_cn：ATonly的fitness更高但precision更低，因为模式更粗、候选资源更多；trace clustering优于单案例属性。

- rhetorical_function_cn：解释执行模式学习方法间的取舍。

- depends_on_cn：Table 9数据。

- sets_up_cn：为选择多维模式学习提供证据。

- evidence_pointer：Table 9及随附段落

### 43. Sect.6.3.1 Table 10

- order：43

- section：Evaluation

- locator：Sect.6.3.1 Table 10

- move_code：RESULT

- paraphrase_cn：MOC产生的重叠组增加灵活性，因此fitness更高而precision更低；AHC模型更严格但不够fit。

- rhetorical_function_cn：把分组技术差异转化为符合度机制解释。

- depends_on_cn：Table 10数据。

- sets_up_cn：说明设计选择不能只看fitness或precision单指标。

- evidence_pointer：Table 10及随附段落

### 44. Sect.6.3.1 Table 11

- order：44

- section：Evaluation

- locator：Sect.6.3.1 Table 11

- move_code：RESULT

- paraphrase_cn：FullRecall在两个日志上都是fitness=1但precision极低，类似flower model；OverallScore在保持中等fitness的同时大幅提升precision。

- rhetorical_function_cn：验证cap分配策略的核心权衡。

- depends_on_cn：Table 11数据。

- sets_up_cn：说明所提指标能识别过灵活模型。

- evidence_pointer：Table 11

### 45. Sect.6.3.1末段

- order：45

- section：Evaluation

- locator：Sect.6.3.1末段

- move_code：CONTRIBUTION

- paraphrase_cn：这些比较展示符合度检查可用于评价发现算法、配置方法，从而扩展组织模型挖掘文献。

- rhetorical_function_cn：把局部实验结果上升为方法贡献。

- depends_on_cn：Table 9-11结果。

- sets_up_cn：承接局部诊断的必要性。

- evidence_pointer：Sect.6.3.1末段

### 46. Sect.6.3.2 Fig.8

- order：46

- section：Evaluation

- locator：Sect.6.3.2 Fig.8

- move_code：RESULT

- paraphrase_cn：低精度WABO模型中Group 3被允许133个执行模式，但只有46个覆盖率超过0.5，许多能力只由一两个成员执行。

- rhetorical_function_cn：用具体案例展示局部诊断的定位能力。

- depends_on_cn：选出的低精度模型和Coverage度量。

- sets_up_cn：支撑低覆盖率作为不精确来源。

- evidence_pointer：Sect.6.3.2, Fig.8

### 47. Sect.6.3.2 Fig.9-Fig.10

- order：47

- section：Evaluation

- locator：Sect.6.3.2 Fig.9-Fig.10

- move_code：RESULT

- paraphrase_cn：某些被列为能力的高频执行模式，该组实际完成的相对份额不足5%，说明能力项与日志行为不一致。

- rhetorical_function_cn：展示低相对份额也能识别偏差。

- depends_on_cn：RelStake度量。

- sets_up_cn：说明需要结合多个局部诊断量。

- evidence_pointer：Fig.9-Fig.10

### 48. Sect.6.3.2末段

- order：48

- section：Evaluation

- locator：Sect.6.3.2末段

- move_code：TRANSITION

- paraphrase_cn：局部诊断结果可以指导改进发现方法，避免把关系不大的执行模式赋为组能力。

- rhetorical_function_cn：把诊断结果连接到模型改进和未来工作。

- depends_on_cn：诊断案例。

- sets_up_cn：进入结论部分。

- evidence_pointer：Sect.6.3.2末段

### 49. Sect.7 P1

- order：49

- section：Conclusion

- locator：Sect.7 P1

- move_code：CONTRIBUTION

- paraphrase_cn：本文贡献是提出基于更丰富组织模型定义的框架，模型同时覆盖结构（成员）和行为（能力），连接资源分析与流程分析。

- rhetorical_function_cn：用一句话重述核心贡献。

- depends_on_cn：全文定义和实验。

- sets_up_cn：与引言RQ1/RQ2呼应。

- evidence_pointer：Sect.7 P1

### 50. Sect.7 P1后半

- order：50

- section：Conclusion

- locator：Sect.7 P1后半

- move_code：CONTRIBUTION

- paraphrase_cn：符合度检查使模型不仅能被评价，还能诊断共性与差异的原因，这区别于只评价发现算法有效性的现有工作。

- rhetorical_function_cn：强调RQ3的贡献定位。

- depends_on_cn：符合度定义。

- sets_up_cn：说明为什么该工作不是一次性方法报告。

- evidence_pointer：Sect.7 P1

### 51. Sect.7 P2

- order：51

- section：Conclusion

- locator：Sect.7 P2

- move_code：RESULT

- paraphrase_cn：实验证明框架可发现组织模型，并展示符合度工具可用于方法比较与偏差分析。

- rhetorical_function_cn：把实验结果回收到贡献声明。

- depends_on_cn：Section 6实验。

- sets_up_cn：后续未来工作讨论。

- evidence_pointer：Sect.7 P2

### 52. Sect.7 P3

- order：52

- section：Conclusion

- locator：Sect.7 P3

- move_code：LIMITATION_AND_FUTURE

- paraphrase_cn：未来工作包括更有效的发现方法、扩展符合度维度、以及按局部诊断结果修复组织模型。

- rhetorical_function_cn：给出研究边界和可继承方向。

- depends_on_cn：全文框架和局部诊断。

- sets_up_cn：为其他研究者留下入口。

- evidence_pointer：Sect.7 P3

## 写作技术

- gap_construction_cn：不是泛泛说没人研究，而是用Table 1从三个事先定义好的视角统一编码已有工作，让“缺案例/时间维度、缺过程连接、缺日志参照评价”三个缺口同时具备文献证据和结构对称性。

- signposting_cn：引言明确列出RQ1-RQ3；相关工作结尾说“we target these three open issues”；框架开头预告“richer organizational model + conformance checking”；方法开头说明三个阶段；实验部分先全局后局部。

- transition_logic_cn：每个大节结束都指向下一节任务：相关工作末尾指向框架；框架末尾只深化发现和符合度；方法后需要实现；实现后需要真实日志评价；全局评价后需要局部诊断解释。

- claim_evidence_rhythm_cn：每提出一个设计选择或机制，都先用定义或例子说明，再在实验部分用对照表呈现数值，最后用一两句话解释为什么数值符合机制预测（如模式越粗→候选资源越多→precision下降）。

- benchmark_narrative_cn：benchmark不是单一数据集上的SOTA比较，而是把真实日志上每个方法组合当作发现策略的对照；先立最优模型为基准，再逐阶段扰动一个变量，使每个表都回答一个具体的“如果换成某方法会怎样”问题。

- theory_return_cn：结果不是停在“我们的方法更好”，而是回到过程挖掘的语言：把FullRecall比作flower model、把precision/fitness解释为模型灵活性与日志拟合的权衡、把局部诊断与过程模型回放对齐。

- contribution_positioning_cn：强调贡献不在某个具体分组算法，而在于“更丰富定义”和“独立于发现技术的评价”，因此即使未来算法替换，框架仍成立。

- novelty_protection_cn：通过开源实现、可配置方法、未来扩展方向，以及明确区分描述性/规范性模型，防止贡献被看成固定数据上的一次性调参结果。

## 可复用研究与写作程序

### structure_steps

#### 1. 1

- step：1

- writing_job_cn：用可比较的文献编码表指出缺口，而不是罗列文献

- research_job_cn：确定3个左右的研究缺口，并确认每个缺口都有现有工作可支撑

- required_evidence_cn：每个缺口至少有两篇以上代表性的现有研究作为反例

- transition_to_next_cn：把每个缺口写成RQ，让全文结构由RQ驱动

#### 2. 2

- step：2

- writing_job_cn：为“缺失的链接”设计形式化概念，并说明为什么新组件必要

- research_job_cn：定义核心对象（如执行模式、cap），用图表示概念关系

- required_evidence_cn：小型示例能手工计算，证明概念可操作

- transition_to_next_cn：概念定义完成后，需要一套发现流程来生成这种对象

#### 3. 3

- step：3

- writing_job_cn：把评价问题从“算法指标”转向“与输入数据的符合度”

- research_job_cn：定义全局和局部评价度量，并解释度量背后的机制

- required_evidence_cn：每个度量有明确公式，且能在示例上得到有意义的数值

- transition_to_next_cn：有了评价工具，才谈得上比较不同发现方法

#### 4. 4

- step：4

- writing_job_cn：用一个端到端方法把框架实例化，并给出多个可选策略

- research_job_cn：设计流水线，保证每个阶段有至少两种可选方案以形成对照

- required_evidence_cn：能在一个小型日志上跑通输出示例

- transition_to_next_cn：方法需要软件化，否则无法系统实验

#### 5. 5

- step：5

- writing_job_cn：介绍实现，强调模块化和可配置性

- research_job_cn：把方法写成库/工具，支持自动批处理

- required_evidence_cn：能运行实验并生成结果表

- transition_to_next_cn：工具准备好了就进入真实数据评价

#### 6. 6

- step：6

- writing_job_cn：在真实数据上做全组合或因子式实验，逐阶段解释差异

- research_job_cn：选择两个或以上真实日志，固定其他变量比较单一阶段方法

- required_evidence_cn：每个比较表都配有一个机制解释，而不仅是数值

- transition_to_next_cn：全局指标说明总体情况，还需要定位问题

#### 7. 7

- step：7

- writing_job_cn：用局部诊断案例展示评价不止于总分

- research_job_cn：选一个低质量模型，用局部度量找出具体问题项

- required_evidence_cn：能清晰展示某个具体模型/组/模式是偏差来源

- transition_to_next_cn：诊断结果自然引出修复和改进的未来工作

#### 8. 8

- step：8

- writing_job_cn：结论重述RQ如何被回答，并把边界和未来方向写清楚

- research_job_cn：确认所有RQ都有对应的概念、方法或实验结果

- required_evidence_cn：贡献声明能与引言的缺口一一对应

- transition_to_next_cn：结束研究并留下可扩展空间

### most_transferable_moves_cn

1. 用文献编码表让缺口有结构化证据

2. 每个RQ都对应一个形式化对象和一个评价指标

3. 先立最优基准，再逐阶段扰动一个变量

4. 把结果现象翻译成机制语言（如粗粒度→高fitness低precision）

5. 用局部诊断把全局指标落到具体对象上

6. 强调框架/评价独立于具体算法以保护贡献

### resource_intensive_or_nonstandard_parts_cn

1. 真实事件日志的获取和预处理需要领域数据，WABO和BPIC17来自公开数据平台

2. 实现OrgMiner并支持多方法可配置需要较多工程投入

3. trace clustering参数和网格搜索需要一定计算资源

4. 图8-10的组织模型可视化部分高度依赖具体工具，OCR中也出现严重表格损坏

### what_not_to_copy_superficially_cn

1. 不要只写“我们提出更丰富定义”却没有可计算的公式或示例

2. 不要只比较两个方法就声称“严格评价”，需要机制解释和逐阶段对照

3. 不要把日志符合度直接说成组织正确性，必须说明描述性与规范性边界

4. 不要在没有真实日志和开源工具的情况下模仿“框架+方法+实验”的表面结构

- single_best_description_of_the_routine_cn：先系统化制造缺口，再用一个形式化模型和一套评价工具把缺口变成RQ，最后用可配置方法+真实日志全组合实验+局部诊断案例证明框架价值。

## 分析边界

源文件标题与正文标题不一致（记录名为OrdinoR，正文首行为OrgMining 2.0），可能反映版本差异；OCR导致图8-10以及部分超大表格内容严重损坏，分析主要依赖正文文字描述；文中未提供真实组织结构的ground truth比较，因此“评价模型质量”只能从符合度角度理解。
