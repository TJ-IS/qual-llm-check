# Timely, Granular, and Actionable: Designing a Social Listening Platform for Public Health 3.0

- 作者：Brent Kitchens; Jennifer L. Claggett; Ahmed Abbasi
- 年份 / 期刊：2024 / MIS Quarterly
- DOI：10.25300/misq/2023/17381
- 源文件：11292_2024_timely-granular-and-actionable-designing-a-social-listening-platform-for-public-health-3-0.md
- 论文主类型：build_evaluate_design_science
- 主导写作弧线：requirements_build_evaluate_design_principles
- 置信度：0.78

## 文章级论证概况

- 核心问题：如何设计一个能够为Public Health 3.0提供及时、细粒度、可行动数据的社交倾听平台，使公共卫生分析不再受限于零散、缺乏上下文和时效性不足的数据收集方式？

- 制品与设计：HealthSense，一个由活动理论扩展和情境信息质量维度共同指导的社会倾听平台。系统由三个模块组成：相关性评估模块（RAM）通过渠道特定的主题/情感分类器和图神经网络判断内容相关性；可信度评估模块（CAM）通过多层双向图传播和GNN判断内容可信度；景观评估模块（LAM）通过GNN评估URL是否可能引导至更多相关内容。三个模块结合GNN、图传播、双关系边增强节点嵌入，形成优先化抓取队列。

- 客观结果：在3700万URL测试床上，HealthSense在收集500万URL时即达到PMDS任务75.1%的相关内容召回率，约为最优比较方法HGAN的两倍多；在1000万URL时两个任务均达到99.9%召回率。消融分析显示与活动理论扩展相关的(i)、(j)设计元素贡献最大。现场用户实验中，使用HealthSense数据的分析师识别真阳性不良事件案例的精确率、召回率均显著高于GBS和BFS数据用户；在报告比值比（ROR）自动事件检测中，HealthSense数据使案例召回率比GBS数据高36%，信号精确率高81%。

- 核心贡献：作者声称的贡献包括：(1) 开发了由活动理论指导的社会倾听制品，将相关性、可信度和跨渠道景观评估结合；(2) 将活动理论扩展至在线平台上的多重交互关系网络，以解释信息不仅存在于个体传播活动中，也存在于活动之间的网络关系；(3) 提出两种GNN方法扩展，即图传播与GNN耦合以及双关系边增强节点嵌入；(4) 证明在动态、快速变化的环境中以人类中心理论和直觉指导的制品是自动化AI技术的重要补充；(5) 通过数据、用户和事件实验证明有效设计的制品可让公共卫生社会倾听变得可能、实用且有价值。

- 整篇论证链：作者从公共卫生数字化的现实背景出发，指出现有社交倾听平台在医疗领域效果不佳，Google Flu Trends的失败说明缺乏上下文、可信度和全渠道意识是根本问题。随后引入活动理论作为理解在线传播活动的社会学框架，并将其扩展为“多重关系网络”视角，提出信息的意义蕴含在作者、渠道、社区、内容之间复杂的交互网络中。与此同时，作者从情境信息质量文献中提取及时性、相关性、可信度、完整性四个元需求，将活动理论扩展具体映射为设计元素。基于这些要求构建HealthSense，用RAM、CAM、LAM三模块分别回应相关性、可信度和渠道景观导航问题。为了验证，作者构建了3700万URL的全量抓取测试床，用专家标注和黄金标准分类器定义两个公共卫生任务的相关内容，然后比较HealthSense与17种基线/基准方法的收集效率；数据实验获得大幅领先。消融分析进一步证明模块和理论派生的具体设计元素都不可缺失，尤其网络传播和交互关系元素贡献最大。最后，通过与一家大型制药公司的药物安全团队合作，作者用现场用户实验和ROR比例失衡分析证明HealthSense收集的数据能同时改善人工判定和自动信号检测的下游表现。讨论部分将结果回收到活动理论扩展与“理论引导制品是AI补充”的更高层贡献，从而把一次性性能优势升华为可复用的设计知识和理论贡献。

## 类型与写作弧线判定

- 论文主类型判定：文章以需求推导、制品构建、系统化评价、设计知识贡献为主线：先由活动理论和信息质量文献推导元需求与设计要素，再实现HealthSense制品，随后用大规模数据实验、消融分析、现场用户实验和事件检测实验评价，最终以设计知识、理论扩展和GNN方法贡献收尾。虽然包含计算benchmark和现场实验，但其整体论证结构是典型的设计科学研究范式。

- 主导写作弧线判定：论文按“Public Health 3.0信息质量要求→活动理论驱动的设计映射→HealthSense制品构建→数据/消融/现场评价→设计原则与理论贡献”展开，四个元需求构成章节骨架，Table 2直接把需求映射到设计元素，评价部分逐一验证这些设计元素，因此属于要求—构建—评价—设计原则弧线。

## 研究开展程序

- study_or_phase_count：6

- 研究阶段总序列：论文先通过动机案例和文献分析形成需求；然后构建大规模测试床作为评估基准；接着用数据实验比较HealthSense与现有方法的收集效率；再用消融分析证明理论派生的设计元素贡献；随后用现场用户实验检验人工决策价值；最后用比例失衡分析检验自动事件检测价值。各阶段层层递进：需求阶段提供设计依据，测试床阶段提供评价基础，数据实验阶段证明总体效能，消融阶段连接具体设计组件与性能，两类现场实验把性能差异转化为下游价值。

### studies_or_phases

#### 1. 需求与动机案例分析

- order：1

- name_cn：需求与动机案例分析

- question_cn：公共卫生社会倾听平台应满足哪些元需求，活动理论与信息质量维度如何转化为设计要求？

- inputs_and_setting_cn：Public Health 3.0文献、情境信息质量文献、活动理论；阿片类危机案例；对当地诊所项目主任、急救医生和急诊科医生的访谈；r/opiates和r/opiaterollcall数据；Comscore点击流数据。

- designed_or_compared_object_cn：四个元需求：及时性、相关性、可信度、完整性；以及它们与活动理论要素和设计元素的映射关系。

- baseline_control_or_counterfactual_cn：无定量对照；以Google Flu Trends失败和现有商业平台局限性作为反面参照。

##### objective_metrics

（空）

- analysis_method_cn：理论推演、案例描述、网络可视化分析（Reddit通信网络、Comscore网站图）。

- main_result_cn：得到Table 2的需求-设计映射，形成了HealthSense设计的理论依据。

- argumentative_role_cn：把宽泛的公共卫生数据缺口转化为可操作的设计元需求，为后续制品构建提供理论合法性。

- remaining_uncertainty_cn：这些需求是否真能带来性能提升尚不确定。

- link_to_next_phase_cn：需要构建制品并设计大规模测试床来检验需求映射的有效性。

##### evidence_pointers

1. Background部分活动理论小节

2. Requirements & Design部分及Table 1、Table 2

3. Motivating Case部分

4. Figure 3、Figure 4、Figure 5

#### 2. 测试床构建与黄金标准标注

- order：2

- name_cn：测试床构建与黄金标准标注

- question_cn：如何获得一个能够评估社会倾听平台收集效率的完整参照全集？

- inputs_and_setting_cn：从100个健康/药物相关种子URL出发，用简单爬虫抓取超过3700万个URL；两位领域专家标注16,000个页面；药物滥用本体和UMLS/SIDER等词表用于实体标注；用SVM构建仅用于离线评估的黄金标准分类器。

- designed_or_compared_object_cn：37,064,742个URL的任务相关性标签（PMDS和Opioid两个任务）。

- baseline_control_or_counterfactual_cn：理想化的简单爬虫全量抓取结果作为可收集内容的全集。

##### objective_metrics

1. 黄金标准分类器在12,000个测试页面上的准确率（PMDS 97.2%，Opioid 95.3%）

2. Cohen's kappa（PMDS 0.95，Opioid 0.93）

- analysis_method_cn：专家两阶段标注，结合实体存在性判断和情感极值判断；用信息增益筛选特征的SVM作为不可在线使用的黄金标准分类器。

- main_result_cn：获得全量测试床，并为每个URL打上两个任务的相关/不相关标签。

- argumentative_role_cn：为数据实验提供可计算精确召回的全集，使“收集到多少相关内容”“速度有多快”可以被客观度量。

- remaining_uncertainty_cn：测试床依赖于专家标注和黄金分类器，可能带有标注噪声；只有文本内容，未覆盖多媒体。

- link_to_next_phase_cn：该测试床是数据实验中各抓取方法性能比较的基础。

##### evidence_pointers

1. Applications and Evaluation部分Test Bed Construction

2. Table 4

#### 3. 数据实验：HealthSense与17种基线/基准方法比较

- order：3

- name_cn：数据实验：HealthSense与17种基线/基准方法比较

- question_cn：HealthSense是否比现有聚焦爬虫、图神经网络、节点嵌入等社会倾听方法更高效地收集任务相关内容？

- inputs_and_setting_cn：3700万URL测试床；每方法10次随机200种子URL运行；比较方法包括HGAN、HGNN、GAT、GraphSAGE、GCN、GBS、HFN、CGM、DeepWalk、Node2Vec、KW、VSM、NB、BERT、BFS、PageRank等。

- designed_or_compared_object_cn：HealthSense与各种基准方法的URL优先化策略。

- baseline_control_or_counterfactual_cn：BFS视为基线爬虫，PageRank作为链接分析基线；HGAN作为最强的GNN基准；还包含传统聚焦爬虫和BERT。

##### objective_metrics

1. 在5M和10M URL处的F-measure、Precision、Recall

2. F-measure曲线、Precision曲线、Recall曲线的AUC

- analysis_method_cn：多次运行平均表现，绘制收集曲线，比较不同渠道（网站、博客、论坛、社交网络）。

- main_result_cn：PMDS任务在5M URL时HealthSense达到75.1%召回率，高于HGAN的36.7%；在10M URL时达到99.9%召回率，而HGAN仅66.3%。Opioid任务效果类似，HealthSense在10M时99.9%，HGAN为53.8%。

- argumentative_role_cn：证明HealthSense在收集效率上显著优于现有方法，为后续下游价值主张提供前端性能基础。

- remaining_uncertainty_cn：总体性能优势还没有归因到具体设计组件；也不知道这种优势是否能转化为实际分析人员的决策改善或自动事件检测改善。

- link_to_next_phase_cn：数据实验后立即进行消融分析，以把性能优势追溯到理论指导的设计元素。

##### evidence_pointers

1. Data Experiment部分

2. Table 5

3. Table 6

4. Figures 7 and 8

#### 4. 消融分析

- order：4

- name_cn：消融分析

- question_cn：HealthSense的性能优势中，哪些由活动理论扩展和信息质量需求派生的具体设计元素贡献？

- inputs_and_setting_cn：同一3700万URL测试床；按Table 7定义的模块级和组件级消融设置（a-j）。

- designed_or_compared_object_cn：从完整HealthSense中移除一个模块/组件后的性能退化。

- baseline_control_or_counterfactual_cn：完整HealthSense作为对照。

##### objective_metrics

1. 移除组件后的F1、Precision、Recall退化百分比

2. F1/Precision/Recall曲线AUC的退化百分比

- analysis_method_cn：leave-out分析；配对t检验。

- main_result_cn：移除CAM和LAM会导致显著性能退化；组件层面，(i)双向关系和作者/站点图以及(j)图传播和图嵌入影响最大，这对应活动理论扩展的多重交互关系和信息传播元素。

- argumentative_role_cn：把系统级性能优势与理论设计要求建立因果联系，证明理论指导不是事后包装，而是实际性能来源。

- remaining_uncertainty_cn：消融是离线指标，没有直接展示下游用户决策或自动检测中的价值。

- link_to_next_phase_cn：消融后需要用现场研究证明这些性能改进确实转化为组织和决策价值。

##### evidence_pointers

1. Data Experiment中Ablation Analysis段落

2. Table 7

3. Table 8

#### 5. 现场用户实验：PharmCo药物安全团队人工案例核查

- order：5

- name_cn：现场用户实验：PharmCo药物安全团队人工案例核查

- question_cn：使用HealthSense收集的数据，是否能让药物安全分析师更准确地判断报告的药品不良事件是否为真阳性？

- inputs_and_setting_cn：一家美国大型制药公司（PharmCo）全球药物安全部门的77名成员；由5名专家事先审查100个案例并确定21个真阳性；从其中选取20个案例（10真10假）；参与者随机分配到HealthSense、GBS、BFS三组；三组使用相同的Tableau仪表盘，仅数据来源不同。

- designed_or_compared_object_cn：不同社会倾听数据源（HealthSense与两种对照方法）作为用户判断的信息基础。

- baseline_control_or_counterfactual_cn：GBS（情感导向聚焦爬虫）和BFS（广度优先爬虫）数据用户组。

##### objective_metrics

1. 真阳性案例判断的Precision、Recall、F-measure

2. 假阳性案例判断的Precision、Recall、F-measure

- analysis_method_cn：随机化实验；专家核查参与者提供的证据；单因素ANOVA检查人口学无差异。

- main_result_cn：HealthSense组真阳性判断的精确率85.34、召回率81.54，显著高于GBS组的70.24、65.00和BFS组的63.32、63.08；对假阳性案例的判断同样显著更优。

- argumentative_role_cn：证明HealthSense的收集效率优势可转化为人工分析决策的准确性和效率提升，回应“及时、细粒度、可行动”中“可行动”的要求。

- remaining_uncertainty_cn：仅在一个公司、一个任务、20个案例上检验；没有直接测量实际工作时间或成本节省，只是用精确率和召回率推断。

- link_to_next_phase_cn：现场用户实验检验人工判断，还需检验自动分析场景是否能同样受益。

##### evidence_pointers

1. Field Study部分User Experiment

2. Table 9

3. Table 10

#### 6. 比例失衡分析：自动不良事件信号检测

- order：6

- name_cn：比例失衡分析：自动不良事件信号检测

- question_cn：使用HealthSense收集的数据，是否能提高基于报告比值比（ROR）的自动药物不良事件信号检测的准确度？

- inputs_and_setting_cn：PharmCo专家界定的21个真阳性案例；HealthSense、GBS、BFS在5M URL阈值下收集的PMDS数据。

- designed_or_compared_object_cn：三种数据源输入同样的ROR自动检测流程。

- baseline_control_or_counterfactual_cn：GBS数据和BFS数据作为对照。

##### objective_metrics

1. 检出的唯一事件案例数

2. 真阳性信号数

3. 假阳性信号数

4. 案例召回率（case recall）

5. 信号精确率（signal precision）

- analysis_method_cn：在文档内计算药物-反应二元组的共现，使用报告比值比及95%置信区间>=1作为阳性信号判定。

- main_result_cn：HealthSense数据实现案例召回率71.43%、信号精确率46.94%；GBS数据为52.38%、25.93%；BFS数据为47.62%、22.22%。相比GBS，召回率提高36%，精确率提高81%。

- argumentative_role_cn：证明HealthSense不仅能改善人工判断，也能改善自动分析，补全下游价值链的两种典型使用方式。

- remaining_uncertainty_cn：ROR只是常用启发式信号检测方法；结果基于一个公司案例集；未做多中心、多药品、多时间窗口的重复验证。

- link_to_next_phase_cn：数据实验、消融、用户实验和事件检测共同支撑Discussion中的五大贡献陈述。

##### evidence_pointers

1. Field Study部分Disproportionality Analysis Case Study

2. Table 11

## 各部分修辞架构

### abstract_moves

1. CONTEXT：在线患者生成海量健康内容；公共健康需要及时、细粒度、可行动数据。

2. PRACTICAL_STAKES：公共卫生3.0呼吁社会倾听平台。

3. GAP：先前医疗社会倾听结果参差不齐，根源是缺乏上下文。

4. DESIGN_FEATURE：用活动理论指导HealthSense，结合图传播与GNN。

5. STUDY_OVERVIEW：两个公共健康任务展示价值。

6. RESULT：数据、用户、事件实验均证明改进。

7. CONTRIBUTION：扩展活动理论到多重交互网络。

### introduction_moves

1. CONTEXT/PRIOR_KNOWLEDGE：从个体健康收益转向公共健康潜力的广阔空间。

2. GAP：现有平台无法有效支持公共卫生信息学。

3. LIMITATION：Google Flu Trends失败，商业平台渠道有限。

4. PHENOMENON：HHS缺乏相关合作，CDC只列商业工具。

5. REQUIREMENT：需要从社会技术视角设计平台。

6. THEORY_INTRO：引入活动理论并预告扩展。

7. STUDY_OVERVIEW：介绍HealthSense及实验概览。

8. CONTRIBUTION：提前列出五项贡献。

### theory_and_knowledge_moves

1. PRIOR_KNOWLEDGE：社会倾听研究多依赖预收集数据或单一API。

2. LIMITATION：现有聚焦爬虫主要基于词法，缺少整体上下文。

3. THEORY_INTRO：活动理论提供理解人类传播活动的框架。

4. THEORY_PROPOSITION：活动是主体、客体、工具、共同体之间的交互。

5. THEORY_PROPOSITION：在线传播信息存在于多重关系网络中。

6. GAP：活动理论研究和全渠道研究都只覆盖少数关系子集。

7. REQUIREMENT：需要纳入完整的多重交互关系。

### artifact_design_moves

1. REQUIREMENT：从信息质量文献提炼及时性、相关性、可信度、完整性四大主题。

2. DESIGN_FEATURE：RAM用渠道特定主题/情感分类器和GNN。

3. DESIGN_FEATURE：CAM用多层双向图传播和GNN可信度分类器。

4. DESIGN_FEATURE：LAM用GNN评估链接景观的隧道潜力。

5. METHOD_JUSTIFICATION：用公式化的关系图卷积和边条件节点嵌入实现GNN。

6. DESIGN_FEATURE：优先化收集公式结合CAM、RAM、LAM得分。

### evaluation_moves

1. METHOD_JUSTIFICATION：构建全量测试床作为可计算全集。

2. BENCHMARK_OR_CONTRAST：与GNN、图爬虫、节点嵌入、链接上下文、基线爬虫等17种方法比较。

3. RESULT：HealthSense在5M/10M节点处大幅领先。

4. ROBUSTNESS_OR_BOUNDARY_TEST：消融分析检验模块和组件贡献。

5. TRANSITION：从离线性能转向现场下游价值。

6. RESULT：用户实验中HealthSense数据组判断更准确。

7. RESULT：比例失衡分析中HealthSense数据信号检测更优。

### discussion_and_contribution_moves

1. CONTRIBUTION：理论引导的制品可同时评估相关性、可信度、景观。

2. CONTRIBUTION：扩展活动理论到多重交互关系，并经验证明其价值。

3. CONTRIBUTION：提出两种GNN扩展。

4. CONTRIBUTION：人类中心理论和直觉是AI技术的必要补充。

5. CONTRIBUTION：数据、用户、事件实验构成下游价值链条。

6. BOUNDARY_CONDITION：可推广到数字营销、危机识别等非公共卫生领域。

7. LIMITATION_AND_FUTURE：模型不能覆盖全部在线复杂性，需要初始训练数据，仅处理文本。

## 理论/知识到设计的翻译

### 知识/理论基础

1. 活动理论（Activity Theory）

2. 情境化信息质量文献（Context-based Information Quality）

3. 聚焦爬虫与社会倾听研究

4. 图神经网络与节点嵌入技术文献

- 理论—设计耦合：direct

- 耦合判定理由：论文不是事后用理论解释结果，而是先由活动理论和信息质量维度明确推导出元需求和设计元素，形成Table 2的逐格映射，并且消融分析逐项检验这些理论派生元素对性能的贡献。GNN等技术选择也是为了实现理论要求而引入，因此属于直接耦合。

- 理论到设计翻译链：Public Health 3.0数据要求→情境信息质量四大主题（及时性、相关性、可信度、完整性）→与活动理论要素（作者、渠道、社区、内容、传播网络）交叉→Table 2中的设计元素（a-j）→HealthSense三人模块（RAM/CAM/LAM）→GNN+图传播+双关系边嵌入的具体实现→数据实验和消融分析检验各设计元素→现场实验检验下游价值。

### mapping_table

#### 1. 1

- theory_or_knowledge_claim_cn：公共卫生任务具有高度时间敏感性，数据需要在内容被删除或局势升级前收集；信息分散在多种渠道且来源易消失。

- mechanism_cn：时效性要求决定了爬虫必须在有限时间内优先收集任务相关内容，而不是慢慢抓取全量网页。

- design_requirement_cn：MR0：从多种在线平台及时收集数据，支持时间敏感分析。

- artifact_choice_cn：优先化抓取队列：所有候选URL先经CAM过滤，再按RAM相关性排序，低相关性URL可因LAM隧道潜力被提升；随着新节点加入不断更新分数。

- evaluated_contrast_cn：HealthSense与BFS、PageRank及其他需要更多抓取才能达到同等召回率的方法比较。

- objective_result_cn：在5M URL时HealthSense达到75.1%（PMDS）和67.9%（Opioid）召回率；10M时两任务均99.9%。

##### evidence_pointers

1. Meta-Requirement 0

2. 优先化收集公式

3. Table 6

#### 2. 2

- theory_or_knowledge_claim_cn：相关性不能仅靠词面相似判断；社区黑话、作者角色和渠道规范决定内容意义。

- mechanism_cn：同样的词汇在不同社区含义不同；作者在社区中的角色决定其发布内容是否与毒品获取、风险提示、情感支持等相关。

- design_requirement_cn：MR1：评估内容与任务的相关性。

- artifact_choice_cn：RAM模块：八种渠道特定的主题/情感分类器，结合词、POS、语义实体标签、情感标签和作者特征；GNN使用边条件节点嵌入。

- evaluated_contrast_cn：消融中移除作者内容特征、渠道特定分类器、语义实体标签、主题/情感分类器；与BERT、关键词方法比较。

- objective_result_cn：基础数据集实验HealthSense大幅优于BERT等；消融使F1退化约6-20%。

##### evidence_pointers

1. Meta-Requirement 1

2. RAM模块

3. Table 8

#### 3. 3

- theory_or_knowledge_claim_cn：在线医疗内容存在大量垃圾、诈骗和错误信息；可信度需要由来源声誉和社区规范共同推断。

- mechanism_cn：可信度可以通过链接关系传播：可信网站更少链接不可信内容；社区用“bad friend”等暗语标记欺诈者。

- design_requirement_cn：MR2：评估内容可信度，避免收集虚假信号。

- artifact_choice_cn：CAM模块：基于医疗认证数据库种子，使用站点、文档、作者三层双向图传播计算可信度，再输入GNN分类器；低于阈值者置为最低优先级。

- evaluated_contrast_cn：消融中移除CAM、用随机种子替代可信度种子、去掉图传播。

- objective_result_cn：移除CAM后PMDS任务@5M F1从73.8降至48.5；种子可信度被破坏导致21-39%退化。

##### evidence_pointers

1. Meta-Requirement 2

2. CAM模块

3. Table 8

#### 4. 4

- theory_or_knowledge_claim_cn：在线健康内容碎片化，相关节点可能在链接稀疏的“口袋”中；只按内容相关性爬取会陷入局部最优。

- mechanism_cn：一些看似不相关的中间站点（如BitcoinTalk）充当相关社区之间的桥；必须预测“隧道”潜力。

- design_requirement_cn：MR3：导航复杂渠道景观，实现完整性。

- artifact_choice_cn：LAM模块：用GNN对子图训练“是否在y跳内导向相关页面”的标签；对低相关性URL额外赋予L(v)分数。

- evaluated_contrast_cn：消融中移除LAM；与不测隧道潜力的聚焦爬虫和GNN方法比较。

- objective_result_cn：移除LAM后PMDS @5M F1降至37.4；完整系统在稀疏链接下仍能到达相关节点。

##### evidence_pointers

1. Meta-Requirement 3

2. LAM模块

3. Figure 5

4. Table 8

#### 5. 5

- theory_or_knowledge_claim_cn：活动理论的延伸命题：信息不仅存在于单个传播活动中，也存在于作者、渠道、社区、内容之间的多重交互关系中，并随信息传播形成网络。

- mechanism_cn：作者-作者、作者-社区、渠道-渠道、文档-文档链接及方向性承载了上下文；双向和多层图可以捕捉这些关系。

- design_requirement_cn：设计元素(h)(i)(j)：纳入作者/站点关系、双向边关系、图和传播信息。

- artifact_choice_cn：GNN中使用双向关系边条件节点嵌入；CAM/LAM使用作者、站点、文档多层图；CAM使用图传播；GNN使用图嵌入聚合。

- evaluated_contrast_cn：消融(i1)双向关系、(i2)作者和站点图、(i3)两者结合、(j1)图传播、(j2)图嵌入、(j3)两者结合。

- objective_result_cn：在PMDS任务，(i3)导致F1退化25.0% @5M和30.9% @10M；(j3)导致30.5% @5M和30.1% @10M；Opioid任务退化更大，(j3)达47.3% @5M。这些是消融中影响最大的组件。

##### evidence_pointers

1. Background活动理论小节

2. HealthSense Artifact技术描述

3. Table 8

## 评价逻辑

### evaluation_modes

1. 大规模数据实验（crawler benchmark）

2. 消融分析（ablation）

3. 现场随机化用户实验（user experiment）

4. 比例失衡分析案例研究（disproportionality analysis）

- why_these_evaluations_cn：单一性能比较只能说明系统总量更好，不能说明为什么更好，也不能说明实际价值。因此作者先使用全量测试床进行可复现的收集效率比较；然后用消融分析把性能差异归因到具体理论派生设计元素；再用现场用户实验证明数据质量能改善人工决策；最后用比例失衡分析证明同一数据也能改善自动信号检测。四种评价分别对应技术性能、设计原理、人机协同价值、自动化分析价值。

- benchmark_and_contrast_chain_cn：测试床构建创造了可计算的“全集”，使 recall 成为可解释指标。数据实验建立端到端性能优势，并覆盖GNN、聚焦爬虫、节点嵌入、链接上下文、BERT和基线爬虫等竞争方法。消融分析将整体优势拆解到CAM/LAM模块和理论派生的(a)-(j)组件，从而建立“性能差异→设计要素差异”的链条。现场研究以GBS和BFS数据作为对照，把上游收集性能差异转化为下游人工和自动分析差异。

### claim_evidence_ledger

#### 1. HealthSense比现有社会倾听工具更能及时收集相关内容。

- claim_cn：HealthSense比现有社会倾听工具更能及时收集相关内容。

- evidence_cn：Table 6数据实验：5M URL时PMDS召回率75.1%，10M时99.9%；Opioid任务同样领先。

- status_cn：强支持

#### 2. 性能优势来自活动理论扩展所派生的设计元素。

- claim_cn：性能优势来自活动理论扩展所派生的设计元素。

- evidence_cn：Table 8消融分析：移除双向关系、作者/站点图、图传播和图嵌入导致最大的性能退化；配对t检验显著。

- status_cn：强支持（但属于离线性能代理）

#### 3. HealthSense收集的数据让分析师更准确、更高效地判断不良事件。

- claim_cn：HealthSense收集的数据让分析师更准确、更高效地判断不良事件。

- evidence_cn：Table 10用户实验：HealthSense数据用户的真阳性判断精确率85.34、召回率81.54，显著高于GBS和BFS组。

- status_cn：强支持（随机化但仅一个企业案例）

#### 4. HealthSense收集的数据能提高自动不良事件信号检测。

- claim_cn：HealthSense收集的数据能提高自动不良事件信号检测。

- evidence_cn：Table 11比例失衡分析：案例召回率71.43% vs GBS 52.38%，信号精确率46.94% vs 25.93%。

- status_cn：中等支持（单一ROR方法、单一数据集）

#### 5. 活动理论需要扩展至多重交互关系才能解释现代在线传播。

- claim_cn：活动理论需要扩展至多重交互关系才能解释现代在线传播。

- evidence_cn：消融分析中最具影响力的组件正是对应活动理论扩展的交互关系和传播元素，且Comscore/Reddit网络图提供现象支持。

- status_cn：中等支持（通过设计验证而非理论假设检验）

- internal_validity_strategy_cn：使用固定全量测试床避免选择偏差；10次随机种子运行平均降低种子敏感性；消融分析以完整系统为对照并做配对t检验；用户实验中随机分配参与者到三种数据条件，检查人口统计无显著差异，且由不参与实验的专家核查证据。

- external_validity_strategy_cn：覆盖两个公共卫生任务（PMDS和Opioid）；数据来自多种渠道（网站、博客、论坛、社交网络）；现场实验在真实制药公司药物安全团队进行；讨论中将应用场景推广到营销和危机响应。

- what_is_not_actually_tested_cn：未直接检验系统对真实公共卫生干预结果的影响（如急救车是否真的准备更多纳洛酮）；未检验多媒体内容；未检验除PMDS/Opioid之外的公共卫生任务；未检验HealthSense在完全冷启动、无初始任务知识场景下的表现；活动理论扩展是通过设计验证而非独立理论假设检验。

## 贡献闭环

- technical_claim_cn：图传播与GNN耦合、双关系边增强节点嵌入这两种GNN扩展能显著提升图上的信息收集效率，尤其适用于标签稀疏和异构网络环境。

- artifact_claim_cn：HealthSense结合相关性、可信度和景观评估三模块后，能够以较低抓取成本收集高比例任务相关内容，是一个有效、高效的社会倾听制品。

- mechanism_claim_cn：在线传播信息的上下文存在于作者、渠道、社区、内容之间的多重交互关系及传播路径中；利用这些关系可以更准确地推断相关性、可信度和隧道潜力。

- boundary_claim_cn：HealthSense特别适用于时间为关键、信息分散在多种渠道、内容动态易消失的公共卫生场景；在稳定任务和既有领域知识条件下收益最大，在探索性任务或缺少初始训练数据时可能受限；研究还指出当前仅覆盖文本内容。

- reusable_design_knowledge_cn：可复用的设计知识包括：活动理论要素可作为健康社会倾听的上下文来源；信息质量维度可转化为社会倾听系统的元需求；图传播可解决GNN标签稀疏问题；双向/多层图可捕捉渠道间交互关系；需要设置“隧道”机制避免聚焦爬虫陷入局部最优点；评价时需要用全量测试床+消融+下游现场实验形成完整证据链。

- theoretical_contribution_cn：将活动理论从描述单个传播活动扩展为描述在线平台中传播活动之间的多重交互关系网络，提出信息不仅存在于个体活动中，也存在于活动之间；并通过设计实验经验证明这种扩展对现代平台上的社会倾听有价值。

- how_discussion_closes_intro_gap_cn：引言指出现有社会倾听缺乏上下文、可信度和全渠道意识，导致GFT失败和公共健康应用受限。讨论部分回到活动理论扩展和“理论引导制品是AI补充”的命题，说明HealthSense正是通过引入上下文多重关系来解决该缺口；同时用现场实验把引言中“让社会倾听变得可能、实用、有价值”从口号转化为可观察的下游改善。

- overclaim_or_unsupported_leaps_cn：存在以下潜在跳跃：将系统性能优势直接称为“公共健康结果改善”，但研究测量的是中间指标（数据收集、案例判断、信号检测）而非最终健康结果；活动理论扩展仅通过单个制品设计验证，缺少独立理论检验；将结果推广到公共卫生之外时只有推测性讨论，没有实证；ROR分析中的“信号精确率”计算依赖专家界定真阳性，可能高估或低估实际表现。

## 句级写作动作图谱

### 1. P1 S1

- order：1

- section：Abstract

- locator：P1 S1

- move_code：CONTEXT

- paraphrase_cn：患者每天通过多种渠道获取和生成在线健康内容，形成不断扩大的数字数据海洋。

- rhetorical_function_cn：开篇建立数据和公共卫生交汇的现实背景。

- depends_on_cn：无需依赖前文。

- sets_up_cn：为引出“需要社会倾听平台”提供前提。

- evidence_pointer：Abstract P1

### 2. P1 S2

- order：2

- section：Abstract

- locator：P1 S2

- move_code：PRACTICAL_STAKES

- paraphrase_cn：公共卫生倡导者呼吁及时、细粒度、可行动的数据，强调需要能识别和汇集这些数据的社会倾听平台。

- rhetorical_function_cn：把数据海洋问题上升到公共卫生政策层面的现实需求。

- depends_on_cn：依赖前一句的数据背景。

- sets_up_cn：为本文设计目标提供政策性理由。

- evidence_pointer：Abstract P1

### 3. P1 S3

- order：3

- section：Abstract

- locator：P1 S3

- move_code：GAP

- paraphrase_cn：此前医疗领域的社会倾听尝试结果参差不齐，主要原因是未能纳入足够上下文来理解要分析的通信。

- rhetorical_function_cn：点明现有方案失败的共同根源。

- depends_on_cn：需要前文说明社会倾听的价值。

- sets_up_cn：引出活动理论作为上下文来源。

- evidence_pointer：Abstract P1

### 4. P2 S1

- order：4

- section：Abstract

- locator：P2 S1

- move_code：DESIGN_FEATURE

- paraphrase_cn：在活动理论指导下设计HealthSense，用于高效感知和收集网络数据以支持实时公共卫生分析。

- rhetorical_function_cn：预告本文解决方案的名称和理论基础。

- depends_on_cn：依赖前文指出的上下文缺失问题。

- sets_up_cn：为后文详细设计模块做总述。

- evidence_pointer：Abstract P2

### 5. P2 S2

- order：5

- section：Abstract

- locator：P2 S2

- move_code：DESIGN_FEATURE

- paraphrase_cn：HealthSense将理论指导的内容分析与图传播、图神经网络相结合，以评估相关性和可信度并智能导航在线渠道景观。

- rhetorical_function_cn：从技术层面说明制品如何实现上下文感知。

- depends_on_cn：依赖活动理论指导的总体设计。

- sets_up_cn：为后续RAM/CAM/LAM模块描述做铺垫。

- evidence_pointer：Abstract P2

### 6. P3 S1

- order：6

- section：Abstract

- locator：P3 S1

- move_code：STUDY_OVERVIEW

- paraphrase_cn：通过两个公共卫生任务展示制品价值：药品上市后不良反应监测和合成阿片类药物危机监测。

- rhetorical_function_cn：明确评价场景，让读者知道应用范围。

- depends_on_cn：需要前一设计句说明系统能力。

- sets_up_cn：引出下文数据实验和现场实验。

- evidence_pointer：Abstract P3

### 7. P3 S2

- order：7

- section：Abstract

- locator：P3 S2

- move_code：RESULT

- paraphrase_cn：数据、用户和事件实验表明有效设计可以让自动化决策和人工决策都得到改善。

- rhetorical_function_cn：提前宣告证据类型和结论范围。

- depends_on_cn：依赖两个任务介绍。

- sets_up_cn：支持摘要末尾的贡献声称。

- evidence_pointer：Abstract P3

### 8. P4 S1

- order：8

- section：Abstract

- locator：P4 S1

- move_code：CONTRIBUTION

- paraphrase_cn：设计过程将活动理论扩展到现代在线平台的复杂性，信息不仅存在于个体通信活动中，也存在于它们的交互网络。

- rhetorical_function_cn：把数据结果上升为理论贡献。

- depends_on_cn：依赖前文所有主张。

- sets_up_cn：为Discussion中的理论贡献段落做定位。

- evidence_pointer：Abstract P4

### 9. P1 S1

- order：9

- section：Introduction

- locator：P1 S1

- move_code：CONTEXT

- paraphrase_cn：用户通过在线健康社区、患者门户、Twitter、Reddit等多种平台获取和生成健康信息。

- rhetorical_function_cn：建立平台多样性和数据体量背景。

- depends_on_cn：无。

- sets_up_cn：为后文强调全渠道社会倾听挑战做铺垫。

- evidence_pointer：Introduction P1

### 10. P1 S3

- order：10

- section：Introduction

- locator：P1 S3

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：过去研究主要关注在线资源对个体健康结果的益处，如慢性病管理、患者教育、情感支持和临床决策支持。

- rhetorical_function_cn：总结已有文献关注点，显示个体层面成果丰富。

- depends_on_cn：依赖平台列举。

- sets_up_cn：形成转向公共健康层面潜力的对照。

- evidence_pointer：Introduction P1

### 11. P2 S1

- order：11

- section：Introduction

- locator：P2 S1

- move_code：GAP

- paraphrase_cn：利用这些数字通信解决更大公共健康问题的潜力巨大但尚未实现。

- rhetorical_function_cn：明确个体健康之外的研究缺口。

- depends_on_cn：依赖前段个体收益总结。

- sets_up_cn：列出多个公共健康应用场景。

- evidence_pointer：Introduction P2

### 12. P2 S3

- order：12

- section：Introduction

- locator：P2 S3

- move_code：LIMITATION

- paraphrase_cn：现有社会倾听平台存在重大局限，无法有效支持公共卫生信息学。

- rhetorical_function_cn：直接否定现有工具能力。

- depends_on_cn：依赖上一句公共健康应用场景。

- sets_up_cn：为设计新平台提供理由。

- evidence_pointer：Introduction P2

### 13. P3 S2

- order：13

- section：Introduction

- locator：P3 S2

- move_code：PHENOMENON

- paraphrase_cn：除公共移动数据外，美国卫生与公众服务部没有利用在线平台数据的合作或举措；CDC仅列出数据源有限的商业工具。

- rhetorical_function_cn：用机构现状说明真实世界尚未采纳先进社会倾听。

- depends_on_cn：依赖前句COVID-19暴露公共卫生数据需求。

- sets_up_cn：强化现有方案不足和机会。

- evidence_pointer：Introduction P3

### 14. P4 S2

- order：14

- section：Introduction

- locator：P4 S2

- move_code：LIMITATION

- paraphrase_cn：Google Flu Trends是失败例子，因为其狭窄视角忽略了上下文、可信度和线上交互内在的全渠道特性。

- rhetorical_function_cn：用一个著名失败案例证明技术中心方案的局限。

- depends_on_cn：依赖前句提到社会倾听在医疗领域的极端复杂性。

- sets_up_cn：引出社会技术视角的要求。

- evidence_pointer：Introduction P4

### 15. P4 S5

- order：15

- section：Introduction

- locator：P4 S5

- move_code：REQUIREMENT

- paraphrase_cn：有效的健康社会倾听平台必须从社会技术视角设计，因为在线交流是人类过程。

- rhetorical_function_cn：从失败案例推导出本文设计原则。

- depends_on_cn：依赖GFT失败分析。

- sets_up_cn：为活动理论引入提供逻辑入口。

- evidence_pointer：Introduction P4

### 16. P5 S1

- order：16

- section：Introduction

- locator：P5 S1

- move_code：GAP

- paraphrase_cn：现有平台要么聚焦少数精选来源，要么缓慢抓取数据仓库式快照，无法满足时效性。

- rhetorical_function_cn：进一步细化现有平台的具体缺口。

- depends_on_cn：依赖社会技术视角要求。

- sets_up_cn：说明本文设计目标：效率与广度兼得。

- evidence_pointer：Introduction P5

### 17. P5 S3

- order：17

- section：Introduction

- locator：P5 S3

- move_code：THEORY_INTRO

- paraphrase_cn：作者利用并扩展活动理论，赋予平台数字通信上下文，以高效识别和收集相关平台信息。

- rhetorical_function_cn：引出理论工具。

- depends_on_cn：依赖前文指出需要社会技术视角和时效性。

- sets_up_cn：为活动理论扩展埋下伏笔。

- evidence_pointer：Introduction P5

### 18. P5 S5

- order：18

- section：Introduction

- locator：P5 S5

- move_code：THEORY_PROPOSITION

- paraphrase_cn：信息不仅存在于这些传播活动中，而且（通常更重要）存在于它们之间。

- rhetorical_function_cn：提出文章理论核心命题。

- depends_on_cn：依赖活动理论引入。

- sets_up_cn：为后文“多重关系网络”扩展和消融分析提供靶心。

- evidence_pointer：Introduction P5

### 19. P6 S1

- order：19

- section：Introduction

- locator：P6 S1

- move_code：STUDY_OVERVIEW

- paraphrase_cn：采用计算设计研究方法提出HealthSense，用于收集支持Public Health 3.0分析的数据。

- rhetorical_function_cn：将理论命题转化为设计研究项目。

- depends_on_cn：依赖前面的理论和缺口。

- sets_up_cn：为后续制品描述和实验概述做准备。

- evidence_pointer：Introduction P6

### 20. P6 S4

- order：20

- section：Introduction

- locator：P6 S4

- move_code：RESULT

- paraphrase_cn：数据实验表明HealthSense仅分析20%的数据就能识别超过90%的任务相关内容，快于包括SOTA深度学习在内的比较方法。

- rhetorical_function_cn：在引言阶段给出核心量化结果，吸引读者继续阅读。

- depends_on_cn：依赖测试床和实验段落。

- sets_up_cn：为后文详细数据实验做预告。

- evidence_pointer：Introduction P6

### 21. P6 S5

- order：21

- section：Introduction

- locator：P6 S5

- move_code：RESULT

- paraphrase_cn：用户和事件实验证明HealthSense帮助药物安全团队在不良事件相关决策中更准确。

- rhetorical_function_cn：提前宣告现场研究价值。

- depends_on_cn：依赖数据实验结果。

- sets_up_cn：为现场实验段落做铺垫。

- evidence_pointer：Introduction P6

### 22. P7 S1

- order：22

- section：Introduction

- locator：P7 S1

- move_code：CONTRIBUTION

- paraphrase_cn：作者列出五项贡献：新制品、活动理论扩展、GNN延伸、理论引导制品与AI互补、跨层评价。

- rhetorical_function_cn：在文章开头就声明贡献清单，让审稿人和读者快速判断增量。

- depends_on_cn：依赖前文摘要级描述。

- sets_up_cn：与Discussion末尾的贡献段落形成呼应。

- evidence_pointer：Introduction P7

### 23. P1 S4

- order：23

- section：Background: State of Social Listening Research

- locator：P1 S4

- move_code：LIMITATION

- paraphrase_cn：大多数研究把数据获取视为给定条件，依赖预收集数据或单一API来源。

- rhetorical_function_cn：概括文献中普遍忽视数据收集环节。

- depends_on_cn：依赖前文对多个使用场景的罗列。

- sets_up_cn：为将社会倾听作为研究焦点提供依据。

- evidence_pointer：Background State of Social Listening Research P1

### 24. P2 S3

- order：24

- section：Background: State of Social Listening Research

- locator：P2 S3

- move_code：LIMITATION

- paraphrase_cn：聚焦爬虫虽有主题相关性，但多数只考虑词法特征，且效率不足以支持时间敏感分析。

- rhetorical_function_cn：评价现有聚焦爬虫方法的两大不足。

- depends_on_cn：依赖前面对普通爬虫和聚焦爬虫的介绍。

- sets_up_cn：为下文提出需要“整体且高效考虑上下文”的平台做铺垫。

- evidence_pointer：Background State of Social Listening Research P2

### 25. P2 S1

- order：25

- section：Background: Node Embeddings and GNNs

- locator：P2 S1

- move_code：THEORY_INTRO

- paraphrase_cn：图神经网络通过消息传递端到端学习节点嵌入，适合图上的下游分类任务。

- rhetorical_function_cn：介绍本文技术基础。

- depends_on_cn：依赖前面对节点嵌入的说明。

- sets_up_cn：为后文提出GNN局限和扩展做背景。

- evidence_pointer：Background Node Embeddings and GNNs P2

### 26. P3 S1

- order：26

- section：Background: Node Embeddings and GNNs

- locator：P3 S1

- move_code：REQUIREMENT

- paraphrase_cn：对于社会倾听平台，GNN提供了结合丰富领域适配图表示的机会，本文提出一种融合图传播的新型嵌入。

- rhetorical_function_cn：把技术文献从介绍转向本文设计贡献。

- depends_on_cn：依赖GNN技术介绍。

- sets_up_cn：为HealthSense的GNN方法细节做预告。

- evidence_pointer：Background Node Embeddings and GNNs P3

### 27. P1 S1

- order：27

- section：Background: An Activity Theoretic Perspective

- locator：P1 S1

- move_code：THEORY_INTRO

- paraphrase_cn：数字通信是人类过程，只有从社会技术角度考虑支持意义建构的上下文才能真正理解。

- rhetorical_function_cn：从背景技术转向理论视角。

- depends_on_cn：依赖前文社会技术视角要求。

- sets_up_cn：为引入活动理论提供认知理由。

- evidence_pointer：Background Activity P1

### 28. P2 S1

- order：28

- section：Background: An Activity Theoretic Perspective

- locator：P2 S1

- move_code：THEORY_PROPOSITION

- paraphrase_cn：活动理论不是预测理论，而是引导观察者理解复杂现实问题的框架。

- rhetorical_function_cn：界定活动理论的元理论地位，避免被误认为可检验假设理论。

- depends_on_cn：依赖活动理论基本概念。

- sets_up_cn：说明本文将“解释”活动理论以适应新环境。

- evidence_pointer：Background Activity P2

### 29. P3 S1

- order：29

- section：Background: An Activity Theoretic Perspective

- locator：P3 S1

- move_code：THEORY_PROPOSITION

- paraphrase_cn：在本文情境中，发布内容的用户是主体，在线渠道是工具，在线社区提供规范、黑话和隐形规则等上下文。

- rhetorical_function_cn：将活动理论的抽象概念映射到在线健康内容场景。

- depends_on_cn：依赖活动理论框架。

- sets_up_cn：为Table 2的活动理论要素列提供具体含义。

- evidence_pointer：Background Activity P3

### 30. P4 S1

- order：30

- section：Background: An Activity Theoretic Perspective

- locator：P4 S1

- move_code：THEORY_PROPOSITION

- paraphrase_cn：信息通过传播活动在平台内部和平台之间流动，这些活动不仅直接连接，还通过其组成成分之间的多重关系形成复杂网络。

- rhetorical_function_cn：提出本文对活动理论的核心扩展命题。

- depends_on_cn：依赖前面对活动组成部分的映射。

- sets_up_cn：为Figure 2和多重关系网络设计做理论基础。

- evidence_pointer：Background Activity P4

### 31. P5 S2

- order：31

- section：Background: An Activity Theoretic Perspective

- locator：P5 S2

- move_code：GAP

- paraphrase_cn：活动理论研究大多只考察成对活动过程；全渠道研究也只关注用户与多个渠道交互的有限子集。

- rhetorical_function_cn：指出现有理论对多重交互关系覆盖面不足。

- depends_on_cn：依赖前文“多重关系”命题。

- sets_up_cn：为本文的完整交互关系补全提供缺口论证。

- evidence_pointer：Background Activity P5

### 32. P5 S4

- order：32

- section：Background: An Activity Theoretic Perspective

- locator：P5 S4

- move_code：REQUIREMENT

- paraphrase_cn：纳入完备的多重交互关系对于从大量在线传播活动中提取信息至关重要。

- rhetorical_function_cn：把理论缺口转化为设计必要要求。

- depends_on_cn：依赖前一句的有限子集判断。

- sets_up_cn：为Table 2中设计元素(h)(i)(j)提供来源。

- evidence_pointer：Background Activity P5

### 33. P6 S1

- order：33

- section：Background: An Activity Theoretic Perspective

- locator：P6 S1

- move_code：DESIGN_FEATURE

- paraphrase_cn：这一活动理论扩展构成核心元设计信息，并与情境信息质量文献结合以满足公共卫生社会倾听需求。

- rhetorical_function_cn：把理论扩展与信息质量要求并列，预示Table 2结构。

- depends_on_cn：依赖前文理论扩展和信息质量文献引入。

- sets_up_cn：为Requirements & Design部分的双源映射做总结。

- evidence_pointer：Background Activity P6

### 34. P1 S3

- order：34

- section：Requirements & Design

- locator：P1 S3

- move_code：REQUIREMENT

- paraphrase_cn：Public Health 3.0对“及时、细粒度、可行动数据”的呼吁与情境化信息质量定义一致。

- rhetorical_function_cn：把政策口号与学术信息质量文献对接。

- depends_on_cn：依赖前文公共卫生3.0背景。

- sets_up_cn：为四大元需求提供文献基础。

- evidence_pointer：Requirements & Design P1

### 35. P1 S6

- order：35

- section：Requirements & Design

- locator：P1 S6

- move_code：REQUIREMENT

- paraphrase_cn：从信息质量维度中识别出四个高层主题：及时性、相关性、可信度和完整性。

- rhetorical_function_cn：概括需求框架。

- depends_on_cn：依赖Table 1文献汇总。

- sets_up_cn：为后续MR0-MR3各小节组织文章。

- evidence_pointer：Requirements & Design P1

### 36. P2 S1

- order：36

- section：Motivating Case: Opioid Epidemic

- locator：P2 S1

- move_code：PHENOMENON

- paraphrase_cn：经销商有动力制造危险批次，因为用户寻求高纯度；社交媒体上过量报道会刺激对该批药物兴趣。

- rhetorical_function_cn：用具体现象说明为何及时监测高风险阿片批次对挽救生命重要。

- depends_on_cn：依赖前文阿片过量的统计。

- sets_up_cn：为引出“24-72小时响应窗口”和患者结局改善提供案例。

- evidence_pointer：Motivating Case P2

### 37. P5 S1

- order：37

- section：Motivating Case: Opioid Epidemic

- locator：P5 S1

- move_code：REQUIREMENT

- paraphrase_cn：作者提出社会倾听平台可以提供及时、细粒度、可行动信息，帮助地方急救人员准备应对强效阿片批次。

- rhetorical_function_cn：把现象案例提升为系统需求目标。

- depends_on_cn：依赖前面对急救和急诊医生访谈。

- sets_up_cn：为Table 2需求-设计映射做情境锚定。

- evidence_pointer：Motivating Case P5

### 38. P2 S3

- order：38

- section：Meta-Requirement 0: Timeliness

- locator：P2 S3

- move_code：REQUIREMENT

- paraphrase_cn：时效性由公共卫生问题紧迫性驱动，同时需要打破数据孤岛、实现广泛互操作。

- rhetorical_function_cn：解释为什么及时性不是操作性指标，而是贯穿设计的主轴。

- depends_on_cn：依赖前文Public Health 3.0数据呼吁。

- sets_up_cn：引出跨渠道收集和内容消失问题。

- evidence_pointer：MR0 P2

### 39. P3 S1

- order：39

- section：Meta-Requirement 0: Timeliness

- locator：P3 S1

- move_code：PHENOMENON

- paraphrase_cn：阿片相关信息源高度动态且短暂，网站和帖子可能很快被删除；历史数据中8.1%帖子被删除或移除。

- rhetorical_function_cn：给出时效性约束的具体数据证据。

- depends_on_cn：依赖前一句跨渠道必要性。

- sets_up_cn：强化优先化抓取的紧迫性。

- evidence_pointer：MR0 P3

### 40. P2 S1

- order：40

- section：Meta-Requirement 1: Evaluate Relevance

- locator：P2 S1

- move_code：REQUIREMENT

- paraphrase_cn：相关性评估需要理解渠道和社区特有的语义特征，如俚语、缩写、表情符号。

- rhetorical_function_cn：说明为什么简单词法相关性不够。

- depends_on_cn：依赖前文相关性定义。

- sets_up_cn：为RAM模块的渠道特定分类器提供理由。

- evidence_pointer：MR1 P2

### 41. P3 S1

- order：41

- section：Meta-Requirement 1: Evaluate Relevance

- locator：P3 S1

- move_code：MECHANISM

- paraphrase_cn：作者在在线社区中扮演多种社会角色；作者关系网络中的传播信息能帮助解释内容相关性。

- rhetorical_function_cn：把活动理论中的作者关系转化为相关性信号。

- depends_on_cn：依赖前文社区黑话和作者角色描述。

- sets_up_cn：为后文作者特征和图传播用于RAM做设计铺垫。

- evidence_pointer：MR1 P3

### 42. P3 S1

- order：42

- section：Meta-Requirement 2: Evaluate Credibility

- locator：P3 S1

- move_code：MECHANISM

- paraphrase_cn：可信或权威的作者不太可能链接到不可信内容，因此链接关系可用于推断可信度；社区规范可提供种子信号，如“bad friend”警告。

- rhetorical_function_cn：设计CAM的可信度推断机制。

- depends_on_cn：依赖前文非可信内容问题严重性。

- sets_up_cn：为CAM的TrustRank式图传播提供原理。

- evidence_pointer：MR2 P3

### 43. P2 S1

- order：43

- section：Meta-Requirement 3: Navigate Channel Landscape

- locator：P2 S1

- move_code：MECHANISM

- paraphrase_cn：相关在线内容可能位于稀疏链接的口袋中，平台间竞争或规避执法导致直接链接很少；需要穿越看似不相关的中间站点。

- rhetorical_function_cn：解释为何需要“隧道”机制。

- depends_on_cn：依赖前文完整性定义和碎片化现象。

- sets_up_cn：引出LAM模块和优先化公式。

- evidence_pointer：MR3 P2

### 44. P3 S2

- order：44

- section：Meta-Requirement 3: Navigate Channel Landscape

- locator：P3 S2

- move_code：MECHANISM

- paraphrase_cn：Comscore数据显示BitcoinTalk是连接多个毒品相关网站的最中心节点；如果仅看内容相关性，社会倾听平台可能难以穿越该图并陷入局部最优。

- rhetorical_function_cn：用真实网络证据支持隧道机制的必要性。

- depends_on_cn：依赖前面对稀疏连接的描述。

- sets_up_cn：为LAM的隧道潜力评分提供实证依据。

- evidence_pointer：MR3 P3

### 45. P1 S1

- order：45

- section：The HealthSense Artifact

- locator：P1 S1

- move_code：DESIGN_FEATURE

- paraphrase_cn：HealthSense包含三个模块，分别处理相关性、可信度和导航渠道景观，全部基于最新GNN构建。

- rhetorical_function_cn：总述系统架构与元需求对应关系。

- depends_on_cn：依赖前文元需求和设计元素。

- sets_up_cn：为下面对各模块的详细说明提供结构。

- evidence_pointer：The HealthSense Artifact P1

### 46. P3 S1

- order：46

- section：The HealthSense Artifact

- locator：P3 S1

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：GNN能简约地考虑节点、边、特征和层级图结构，与活动理论扩展的多重交互关系信息传播相对应。

- rhetorical_function_cn：为选择GNN作为实现技术提供理论匹配理由。

- depends_on_cn：依赖前文GNN概述和活动理论扩展。

- sets_up_cn：引出两个方法论贡献：图传播+GNN和双关系边增强节点嵌入。

- evidence_pointer：The HealthSense Artifact P3

### 47. P4 S1

- order：47

- section：The HealthSense Artifact

- locator：P4 S1

- move_code：DESIGN_FEATURE

- paraphrase_cn：RAM评估内容主题和情感，结合作者潜在倾向、社区词典和渠道模式。

- rhetorical_function_cn：具体描述相关性模块输入。

- depends_on_cn：依赖MR1需求。

- sets_up_cn：为后文RAM技术细节做摘要。

- evidence_pointer：The HealthSense Artifact P4

### 48. P4 S2

- order：48

- section：The HealthSense Artifact

- locator：P4 S2

- move_code：DESIGN_FEATURE

- paraphrase_cn：CAM使用类似TrustRank的图传播特征，结合站点、文档、作者级图进行可信度评估，并用社区规范作为可信度种子。

- rhetorical_function_cn：具体描述可信度模块。

- depends_on_cn：依赖MR2需求。

- sets_up_cn：为后文CAM公式和图传播细节做铺垫。

- evidence_pointer：The HealthSense Artifact P4

### 49. P5 S1

- order：49

- section：The HealthSense Artifact

- locator：P5 S1

- move_code：DESIGN_FEATURE

- paraphrase_cn：LAM评估链接能否导向进一步相关内容，以平衡RAM和CAM对直接相关内容的过度聚焦。

- rhetorical_function_cn：具体描述景观模块的必要性。

- depends_on_cn：依赖MR3需求。

- sets_up_cn：为后文LAM的图嵌入和优先级公式做铺垫。

- evidence_pointer：The HealthSense Artifact P5

### 50. P6 S2

- order：50

- section：The HealthSense Artifact

- locator：P6 S2

- move_code：DESIGN_FEATURE

- paraphrase_cn：系统以CAM过滤、RAM排序、LAM补充低相关性URL的方式优先抓取候选URL，并随着新URL加入实时更新分数。

- rhetorical_function_cn：说明三模块如何整合为统一抓取流程。

- depends_on_cn：依赖三模块各自描述。

- sets_up_cn：为评价部分测试“效率”提供系统行为基础。

- evidence_pointer：The HealthSense Artifact P6

### 51. P2 S1

- order：51

- section：The HealthSense Artifact - RAM

- locator：P2 S1

- move_code：DESIGN_FEATURE

- paraphrase_cn：RAM使用按渠道分开训练的主题和情感分类器，共八个二分类器。

- rhetorical_function_cn：将MR1的渠道差异要求落到具体分类器设计。

- depends_on_cn：依赖渠道特定语言模式讨论。

- sets_up_cn：为Table 3特征列表提供上下文。

- evidence_pointer：RAM Module P2

### 52. P1 S1

- order：52

- section：The HealthSense Artifact - CAM

- locator：P1 S1

- move_code：DESIGN_FEATURE

- paraphrase_cn：CAM使用加权多层双向图传播为每个节点计算可信度值，作为可信度GNN的输入特征。

- rhetorical_function_cn：将MR2要求转化为具体计算方法。

- depends_on_cn：依赖前文可信度种子来源。

- sets_up_cn：为后文公式(6)和图传播细节做铺垫。

- evidence_pointer：CAM Module P1

### 53. P1 S1

- order：53

- section：The HealthSense Artifact - LAM

- locator：P1 S1

- move_code：DESIGN_FEATURE

- paraphrase_cn：LAM通过在有标签的图中分析文档节点是否在y跳内导向相关页面，学习预测候选URL的语境分数。

- rhetorical_function_cn：将MR3隧道需求转化为ML任务。

- depends_on_cn：依赖前文LAM总述。

- sets_up_cn：为优先化公式中L(v)的使用提供依据。

- evidence_pointer：LAM Module P1

### 54. P1 S1

- order：54

- section：Applications and Evaluation

- locator：P1 S1

- move_code：STUDY_OVERVIEW

- paraphrase_cn：作者构建大型测试床，探索两个公共卫生任务：上市后药物警戒和合成阿片类批次监测。

- rhetorical_function_cn：把设计章节转向评价章节。

- depends_on_cn：依赖前文HealthSense系统。

- sets_up_cn：为Test Bed Construction和后续实验做引子。

- evidence_pointer：Applications and Evaluation P1

### 55. P1 S1

- order：55

- section：Test Bed Construction

- locator：P1 S1

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：开发了一个由简单爬虫在无限时间下可收集全部信息构成的测试床，以评估HealthSense在收集任务相关信息上的效率和有效性。

- rhetorical_function_cn：解释为何需要全量测试床。

- depends_on_cn：依赖前文效率目标。

- sets_up_cn：为黄金标准分类器和recall计算提供逻辑基础。

- evidence_pointer：Test Bed Construction P1

### 56. P1 S1

- order：56

- section：Data Experiment

- locator：P1 S1

- move_code：BENCHMARK_OR_CONTRAST

- paraphrase_cn：HealthSense与一系列基线和领先benchmarks比较，每次运行使用随机种子子集以保证对种子不敏感。

- rhetorical_function_cn：交代比较方法和随机化设置。

- depends_on_cn：依赖测试床构建。

- sets_up_cn：为Table 5列表和Table 6结果做准备。

- evidence_pointer：Data Experiment P1

### 57. P4 S1

- order：57

- section：Data Experiment

- locator：P4 S1

- move_code：RESULT

- paraphrase_cn：PMDS任务中HealthSense在500万URL内获得75.1%相关页面，精确率72.6%，数字是最好比较方法HGAN的两倍多。

- rhetorical_function_cn：给出第一个核心量化结果。

- depends_on_cn：依赖Table 6。

- sets_up_cn：为后文10M结果和渠道一致性提供部分图景。

- evidence_pointer：Data Experiment P4

### 58. P5 S1

- order：58

- section：Data Experiment

- locator：P5 S1

- move_code：RESULT

- paraphrase_cn：在1000万URL时HealthSense在两个任务中均识别99.9%相关页面，HGAN仅53%-67%。

- rhetorical_function_cn：强调高召回率最终可达，但HGAN差距巨大。

- depends_on_cn：依赖前一个5M结果。

- sets_up_cn：支持“效率提升”核心主张。

- evidence_pointer：Data Experiment P5

### 59. P6 S1

- order：59

- section：Data Experiment

- locator：P6 S1

- move_code：BENCHMARK_OR_CONTRAST

- paraphrase_cn：收集时间主要是服务器响应瓶颈，算法运行时间显著短于页面等待时间，因此收集时间与性能曲线呈线性关系。

- rhetorical_function_cn：把URL数量转换为时间含义。

- depends_on_cn：依赖前面收集性能结果。

- sets_up_cn：为“更及时”提供可解释的操作性度量。

- evidence_pointer：Data Experiment P6

### 60. P7 S1

- order：60

- section：Data Experiment

- locator：P7 S1

- move_code：TRANSITION

- paraphrase_cn：为展示理论指导的设计元素如何影响整体性能，作者进行消融分析。

- rhetorical_function_cn：从整体性能转向内部归因。

- depends_on_cn：依赖前文整体结果。

- sets_up_cn：为Table 7和Table 8做引导。

- evidence_pointer：Data Experiment P7

### 61. P1 S1

- order：61

- section：Ablation Analysis

- locator：P1 S1

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：在模块和组件两个层级进行leave-out分析，对应Table 2中整列或单个设计元素的排除。

- rhetorical_function_cn：说明消融设计如何与理论映射对应。

- depends_on_cn：依赖Table 2和Table 7。

- sets_up_cn：为解读Table 8的退化百分比提供方法学基础。

- evidence_pointer：Ablation Analysis P1

### 62. P2 S2

- order：62

- section：Ablation Analysis

- locator：P2 S2

- move_code：RESULT

- paraphrase_cn：影响最大的设计元素是(i)和(j)，与活动理论扩展的多重交互关系和信息传播相关。

- rhetorical_function_cn：把最大性能贡献指向理论扩展。

- depends_on_cn：依赖Table 8数据。

- sets_up_cn：为Discussion中的理论贡献提供经验证据。

- evidence_pointer：Ablation Analysis P2

### 63. P1 S1

- order：63

- section：Field Study

- locator：P1 S1

- move_code：TRANSITION

- paraphrase_cn：为展示前述收集效率收益的下游价值主张，作者在一家大型美国制药公司进行PMDS任务的现场研究。

- rhetorical_function_cn：从实验室评价转向实用价值评价。

- depends_on_cn：依赖数据实验和消融分析。

- sets_up_cn：为用户实验和比例失衡分析提供导语。

- evidence_pointer：Field Study P1

### 64. P2 S1

- order：64

- section：User Experiment

- locator：P2 S1

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：参与者随机分配到三组，每组使用由不同社会倾听方法收集的数据加载同一Tableau仪表盘。

- rhetorical_function_cn：保证唯一差异是数据来源。

- depends_on_cn：依赖测试床和5M阈值数据。

- sets_up_cn：为Table 10结果提供因果有效性说明。

- evidence_pointer：User Experiment P2

### 65. P4 S2

- order：65

- section：User Experiment

- locator：P4 S2

- move_code：RESULT

- paraphrase_cn：使用HealthSense数据的参与者识别真阳性案例的精确率和召回率显著更高，同时也能更好地识别假阳性案例。

- rhetorical_function_cn：报告用户实验核心结果。

- depends_on_cn：依赖Table 10。

- sets_up_cn：支持“数据可行动性”和“降低调查成本”主张。

- evidence_pointer：User Experiment P4

### 66. P2 S1

- order：66

- section：Disproportionality Analysis

- locator：P2 S1

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：使用报告比值比ROR及95%置信区间>=1来识别药物-反应对。

- rhetorical_function_cn：说明自动事件检测的数量方法。

- depends_on_cn：依赖比例失衡分析概念。

- sets_up_cn：为Table 11结果提供测量方式。

- evidence_pointer：Disproportionality Analysis P2

### 67. P3 S2

- order：67

- section：Disproportionality Analysis

- locator：P3 S2

- move_code：RESULT

- paraphrase_cn：相比GBS数据，HealthSense数据使案例召回率提高36%，信号精确率提高81%。

- rhetorical_function_cn：量化自动检测的下游增益。

- depends_on_cn：依赖Table 11。

- sets_up_cn：为Discussion中“下游价值链条”贡献提供实例。

- evidence_pointer：Disproportionality Analysis P3

### 68. P2 S1

- order：68

- section：Discussion and Conclusion

- locator：P2 S1

- move_code：CONTRIBUTION

- paraphrase_cn：理论引导的社会倾听制品可以无缝结合相关性、可信度和跨渠道景观评估，实现明显更好的公共卫生感知能力。

- rhetorical_function_cn：概括第一项贡献。

- depends_on_cn：依赖所有实验结果。

- sets_up_cn：引出后文理论扩展和GNN扩展。

- evidence_pointer：Discussion P2

### 69. P3 S1

- order：69

- section：Discussion and Conclusion

- locator：P3 S1

- move_code：CONTRIBUTION

- paraphrase_cn：通过设计过程提出对活动理论的扩展，并经验证明这些多重交互关系机制大幅改善制品能力。

- rhetorical_function_cn：把消融最大贡献组件与理论扩展连接。

- depends_on_cn：依赖Table 8消融结果。

- sets_up_cn：回扣引言中“信息存在于活动之间”的核心命题。

- evidence_pointer：Discussion P3

### 70. P4 S1

- order：70

- section：Discussion and Conclusion

- locator：P4 S1

- move_code：CONTRIBUTION

- paraphrase_cn：提出两种GNN方法扩展：图传播与GNN耦合，以及双关系边增强节点嵌入。

- rhetorical_function_cn：确立方法贡献。

- depends_on_cn：依赖HealthSense技术章节。

- sets_up_cn：为“人类中心理论与AI互补”的更高层贡献做铺垫。

- evidence_pointer：Discussion P4

### 71. P5 S1

- order：71

- section：Discussion and Conclusion

- locator：P5 S1

- move_code：CONTRIBUTION

- paraphrase_cn：在动态环境中，由人类中心理论和直觉指导的制品仍然是自动化AI技术的关键补充。

- rhetorical_function_cn：把具体技术贡献上升为设计科学方法论启示。

- depends_on_cn：依赖前几项贡献。

- sets_up_cn：为将结果推广到更广泛AI时代提供修辞支撑。

- evidence_pointer：Discussion P5

### 72. P6 S1

- order：72

- section：Discussion and Conclusion

- locator：P6 S1

- move_code：CONTRIBUTION

- paraphrase_cn：数据、用户和事件实验共同展示有效设计的社会倾听制品的下游价值链。

- rhetorical_function_cn：汇总证据来源。

- depends_on_cn：依赖Table 6、Table 10、Table 11。

- sets_up_cn：为最终“公共卫生结果可能性”做收官。

- evidence_pointer：Discussion P6

### 73. P7 S1

- order：73

- section：Discussion and Conclusion

- locator：P7 S1

- move_code：BOUNDARY_CONDITION

- paraphrase_cn：该系统也适用于公共卫生之外的领域，如数字营销中的全渠道用户行为监控和危机识别响应。

- rhetorical_function_cn：界定系统的潜在适用边界，扩大一般性。

- depends_on_cn：依赖前文系统特征。

- sets_up_cn：为未来研究留下方向。

- evidence_pointer：Discussion P7

### 74. P8 S1

- order：74

- section：Discussion and Conclusion

- locator：P8 S1

- move_code：LIMITATION_AND_FUTURE

- paraphrase_cn：模型只覆盖在线通信复杂性的一小部分；需要初始任务相关训练集；仅处理文本内容。

- rhetorical_function_cn：列出研究限制，防止过度一般化。

- depends_on_cn：依赖前文所有贡献。

- sets_up_cn：为未来研究预留边界条件。

- evidence_pointer：Discussion P8

## 写作技术

- gap_construction_cn：先用“患者生成海量数据+公共卫生3.0数据呼吁”建立机会，再用Google Flu Trends失败和商业平台渠道局限说明现有产品无法抓住机会；再用HHS/CDC的现状增强紧迫感；最后把问题归结为“缺乏上下文”这一可解决的理论缺口。

- signposting_cn：在摘要和引言提前列出五项贡献；在Requirements部分预告Table 2映射；在每个元需求小节开头用“第一个主题是……”“下一个主题是……”；在数据实验末预告消融；在消融末预告现场研究。

- transition_logic_cn：每个研究阶段都以前一阶段留下的问题开头：测试床回答“如何测量”，数据实验回答“是否更好”，消融回答“为什么更好”，现场用户实验回答“对人是否有用”，比例失衡分析回答“对机器是否有用”。段末常用“As we later demonstrate”“In order to demonstrate”等指引。

- claim_evidence_rhythm_cn：先陈述总体性能数字，再展示图表；先用数据实验建立整体优势，再用消融把优势拆解到组件，最后用现场实验把性能优势翻译成用户和自动分析结果。主张逐步放大，证据也逐步多元。

- benchmark_narrative_cn：benchmark不是孤立技术对比，而是按类别组织（GNN、图爬虫、节点嵌入、链接上下文、基线），让读者看到HealthSense在与自己最接近的SOTA HGAN上领先2倍多，同时与经典方法也拉开差距；Table 5的说明把基准差异变成“技术选择差异”的叙事。

- theory_return_cn：消融分析中最大贡献组件(i)(j)被回溯到活动理论扩展；讨论部分紧跟着把这些实证结果表述为“经验证明扩展理论有效”，从而避免理论贡献只停留在概念层面。

- contribution_positioning_cn：贡献分多层：制品层、理论层、方法层、设计科学层、实证价值层；每项贡献都有对应证据（制品→数据实验；理论→消融；方法→技术描述+消融；设计科学→讨论；实证价值→现场实验）。

- novelty_protection_cn：通过消融分析把端到端性能差异归因到理论派生组件，避免被看作“又一个新的GNN应用”；通过现场用户和事件实验把性能数字升华为“人工分析成本降低”“自动事件发现更准”，防止贡献退化为一次性benchmark结果；讨论中主动承认边界，防止过度声称。

## 可复用研究与写作程序

### structure_steps

#### 1. 1

- step：1

- writing_job_cn：在引言建立现实数据海洋与公共卫生政策需求，然后用一个失败案例（GFT）指出现有技术中心方案的缺口，最后提出“需要社会技术视角和上下文”的设计原则。

- research_job_cn：识别一个有政策紧迫性、有失败先例、有多渠道数据现象的公共卫生问题；初步收集领域证据（文献、机构访谈、示例数据）。

- required_evidence_cn：需要证明现有方案确实不足，且存在可观察的真实世界后果；至少要有政策文件、失败案例或机构现状作为佐证。

- transition_to_next_cn：缺口句末尾自然引出“因此我们使用/扩展某理论”作为解决方案的起点。

#### 2. 2

- step：2

- writing_job_cn：用理论+已有文献推导元需求，制作需求-设计映射表，把抽象理论元素对应到具体设计元素，并为每个元需求提供真实案例说明。

- research_job_cn：选择与问题匹配的kernel theory和信息质量框架；通过访谈、历史数据或网络可视化展示每个元需求的现实意义。

- required_evidence_cn：需要每个元需求至少有一个真实案例或数据现象（如帖子删除率、网络图中心性、社区暗语）作为支撑。

- transition_to_next_cn：映射表最后一列预告“在后续消融中验证每个设计元素”，把设计章节引向制品实现。

#### 3. 3

- step：3

- writing_job_cn：按模块描述制品，每个模块明确对应一个元需求；在技术公式和架构图附近说明设计选择与理论的对应关系；末尾用优先化/流程说明模块如何整合。

- research_job_cn：实现制品；设计时记录每个组件的理论来源和可替换性，为消融分析做准备。

- required_evidence_cn：需要可用系统/组件或可重复实现的技术规格；至少需要说明输入、输出、损失函数和模块交互。

- transition_to_next_cn：模块整合后自然转入“如何证明它有效”，即构建测试床和评价。

#### 4. 4

- step：4

- writing_job_cn：先构建可计算全量测试床和黄金标准，再安排数据实验比较端到端性能；报告曲线和关键里程碑指标；随后安排消融分析把性能归因到组件。

- research_job_cn：收集/标注或模拟完整参照集；选择有代表性的baseline和benchmark；设计leave-out消融；运行多次避免种子偏差。

- required_evidence_cn：需要测试床的规模、标注信度、黄金标准准确率；需要各方法在相同条件下的性能表；消融需要配对显著性检验。

- transition_to_next_cn：在消融段落末尾说明“离线性能仍然只是代理，需要下游验证”，引出现场或用户研究。

#### 5. 5

- step：5

- writing_job_cn：设计一个能直接转换性能优势为组织价值的现场研究；用随机分配或内部控制保证比较公平；报告精确率、召回率等决策指标。

- research_job_cn：找到愿意合作的企业/机构；构建专家判定的真实案例集；用不同数据源作为唯一差异，记录参与者决策表现。

- required_evidence_cn：需要真实组织、真实任务、专家共识标签、随机分配或相应控制；最好有任务时间/决策准确率等可量化结果。

- transition_to_next_cn：人工决策验证后，立即补充自动化分析验证，使价值证据覆盖人和机器两条路径。

#### 6. 6

- step：6

- writing_job_cn：在Discussion按贡献层级总结：制品贡献、理论贡献、方法贡献、设计科学贡献、实证价值贡献；并明确边界条件与限制。

- research_job_cn：把各实验结果对应到贡献声明；识别真正被证据支持的边界与未被检验的隐含假设。

- required_evidence_cn：每个贡献声明必须至少有一条实验证据链；限制部分需要诚实地列出数据、场景和方法边界。

- transition_to_next_cn：用边界条件和未来研究收尾，使贡献看起来可扩展而非一次性。

### most_transferable_moves_cn

1. 用政策/官方机构现状（如HHS/CDC）作为“现实缺口”证据，比纯文献引用更有说服力。

2. 把理论构念与设计元素制作成显式映射表，后文用消融表回应这个映射，形成闭环。

3. 先用全量测试床确保可计算recall，再用消融分析将性能优势归因到理论组件。

4. 在数据实验与现场研究之间设置明确过渡：“离线性能优势是否转化为下游价值？”

5. 用“同一仪表盘、不同数据源”的随机化实验隔离数据质量对用户决策的影响。

6. 将人工判断实验与自动算法实验并列，证明价值不依赖于单一路径。

### resource_intensive_or_nonstandard_parts_cn

1. 3700万URL的大型测试床构建和数十万页专家标注成本极高，不是所有研究都能复制。

2. 需要与真实制药公司安全团队建立合作关系并获取内部专家判断，涉及隐私和准入限制。

3. Comscore点击流数据是付费商业数据；Reddit和访谈数据相对可获取但也不完全开放。

4. 需要较强的工程能力实现三个GNN模块和图传播系统。

### what_not_to_copy_superficially_cn

1. 不能只在讨论中宣称“扩展了活动理论”，而没有消融分析证明理论派生组件带来性能差异。

2. 不能只报告端到端准确率就声称“社会倾听有价值”，需要用用户/事件实验展示下游改善。

3. 不能用“平台多样性”泛泛而谈，必须有不同渠道上的指标表现。

4. 不能把系统性能直接等同于公共卫生最终健康结果；若无最终结局数据，措辞应限定为中间指标改善。

- single_best_description_of_the_routine_cn：先用政策和失败案例制造一个“缺乏上下文导致社会倾听不可用”的缺口，再用活动理论+信息质量生成显式需求-设计映射并构建HealthSense，接着用全量测试床、消融、现场用户实验和自动事件检测四层证据把“性能好”升级为“理论对、组件对、对人有用、对机器有用”。

## 分析边界

文章全文和图表可读，但原始文件没有期刊页码，定位只能精确到章节、段落和表/图编号；OCR对公式和部分图注可能有细微符号失真；摘要与正文重复度较高，因此句子级动作编码在摘要和引言部分偶尔覆盖相似表述；未访问附录或在线补充材料，可能存在未展示的补充分析。
