# Shedding light on blind spots – Developing a reference architecture to leverage video data for process mining

- 作者：Wolfgang Kratsch; Fabian König; Maximilian Röglinger
- 年份 / 期刊：2022 / Decision Support Systems
- DOI：10.1016/j.dss.2022.113794
- 源文件：16824_2022_shedding-light-on-blind-spots-developing-a-reference-architecture-to-leverage-video-data-for-pro.md
- 论文主类型：build_evaluate_design_science
- 主导写作弧线：requirements_build_evaluate_design_principles
- 置信度：0.78

## 文章级论证概况

- 核心问题：如何系统化利用视频数据来支持流程挖掘，即怎样从非结构化的视频数据中提取可用于流程挖掘的事件日志并形成可复用的架构方案。

- 制品与设计：ViProMiRA，一个桥接计算机视觉与流程挖掘的参考架构，包含Data Preprocessor、Information Extractor、Event Processor三个子系统层；通过颜色标识的实例化变体（蓝色、橙色、绿色）和可选组件，指导针对不同流程挖掘用例选择并组合计算机视觉能力；最终能以XES格式输出事件日志，并连接多种BPM应用。

- 客观结果：将参考架构的最复杂绿色变体实现为软件原型，并在Crêpe真实视频数据集上验证：自动提取出超过70%的流程相关事件；合并子活动后平均召回率69.70%、精确率82.36%；对提取日志做一致性检查得到fitness 79.81%，而真实日志为97.98%；流程发现得到的模型在fitness、precision等指标上可用。

- 核心贡献：作者声称ViProMiRA是首个系统性利用视频数据支持流程挖掘的参考架构，为基于视频的流程挖掘奠定了理论基础；原型是首个能够无侵入地提取多参与者并发案例的技术制品；同时提供了利用开源框架端到端实例化该架构的范例。

- 整篇论证链：文章从流程挖掘依赖结构化数据、导致人工活动成为分析盲点这一现实问题出发，指出非结构化视频数据蕴含流程信息但缺少系统化利用方案。通过文献调研与对照已有文本、传感器和视频相关方法，作者论证现有研究只解决领域特定问题，未能提供可推广的架构。据此从流程挖掘用例、事件日志提取和计算机视觉能力三个知识领域推导设计目标，构建包含预处理、信息提取和事件处理三个子系统的ViProMiRA参考架构。为证明其可行性，作者用逻辑推理、同行评审和软件原型进行多轮评价；最后在Crêpe数据集上实例化原型，通过召回率/精确率、一致性检查和流程发现三类评价说明该架构确实能把视频自动转为可用于流程挖掘的事件日志，并据此返回研究问题，宣称该架构填补了计算机视觉与流程挖掘之间的系统化空白。

## 类型与写作弧线判定

- 论文主类型判定：文章遵循Peffers等的设计科学研究流程，先定义设计目标，再构建参考架构ViProMiRA，并通过EVAL1至EVAL4多种评价活动（文献论证、逻辑推理、专家调查、原型演示、真实数据集应用）展示制品的有用性与适用性，最后提炼为可复用的设计知识。

- 主导写作弧线判定：全文主线是从文献与问题域提炼设计要求（DOs），据此构建参考架构，再通过多阶段评价验证DOs是否满足，并以参考架构和实例化路径作为可复用设计知识呈现。

## 研究开展程序

- study_or_phase_count：7

- 研究阶段总序列：研究按DSR生命周期展开：先识别问题并确认现有方案不足以解决（EVAL1），再从文献提炼设计目标；随后构建架构并用逻辑推理和研究者反馈评价设计规范（EVAL2）；接着实现最复杂绿色变体原型并测试内部一致性与适用性（EVAL3）；最后在真实视频数据集上应用原型，分别从事件日志准确性、一致性检查、流程发现三个方面评估（EVAL4）。这些阶段层层递进，从问题论证、需求生成、设计构建，到实例化验证，最终回到贡献声明。

### studies_or_phases

#### 1. 问题识别与文献调研（EVAL1）

- order：1

- name_cn：问题识别与文献调研（EVAL1）

- question_cn：现有流程挖掘研究是否已能为从视频数据中系统提取事件日志提供充分方案？

- inputs_and_setting_cn：半结构化文献搜索，以Mannhardt等的传感器活动识别与流程发现分类法为起点，向前后追溯流程挖掘与事件抽象、视频数据相关文献。

- designed_or_compared_object_cn：比较文本、传感器、视频等多类从非结构化数据提取事件的方法。

- baseline_control_or_counterfactual_cn：无独立baseline；以是否满足“通用事件提取、至少覆盖一个流程挖掘用例、有实现或实例化”三个标准来筛出候选方法。

##### objective_metrics

（空）

- analysis_method_cn：文献分析、筛选标准、人工逐篇比较。

- main_result_cn：最终保留五项工作；它们都只覆盖ex-post用例，大多不生成标准化XES日志，很多依赖多传感器且计算机视觉能力组合不能泛化，因此现有方法不能系统利用视频数据。

- argumentative_role_cn：为后续设计与开发提供合法性：说明需要一个新制品。

- remaining_uncertainty_cn：文献分析只能说明现有研究不足，还不能证明视频数据在真实流程挖掘场景中确实可提取并可分析。

- link_to_next_phase_cn：因此需要定义新制品应满足的设计目标并进入构建阶段。

##### evidence_pointers

1. Section 4 Table 1

2. Section 4 P3 selection criteria

3. Section 4 P4-P5 gap conclusion

#### 2. 设计目标定义

- order：2

- name_cn：设计目标定义

- question_cn：为系统化利用视频数据支持流程挖掘，制品应满足哪些功能性与非功能性要求？

- inputs_and_setting_cn：基于第2节流程挖掘、事件日志提取、事件抽象、计算机视觉等相关文献。

- designed_or_compared_object_cn：七条设计目标DO1.1至DO3.3，划分为用例导向、事件日志提取、计算机视觉能力三组。

- baseline_control_or_counterfactual_cn：无对照；设计目标作为后续构建和评价的规范性标准。

##### objective_metrics

（空）

- analysis_method_cn：文献综述与需求归纳。

- main_result_cn：确定制品必须支持ex-ante与ex-post用例、具备用例灵活性、输出XES、支持事件抽象、覆盖电脑视觉能力并指导选择与组合。

- argumentative_role_cn：把研究问题转换为可操作的架构需求，为设计提供依据。

- remaining_uncertainty_cn：目标是否可实现尚未验证。

- link_to_next_phase_cn：设计目标直接指导ViProMiRA的组件与变体设计。

##### evidence_pointers

1. Section 5 Table 2

#### 3. 设计与开发及设计规范评价（EVAL2）

- order：3

- name_cn：设计与开发及设计规范评价（EVAL2）

- question_cn：如何用参考架构形式满足设计目标？该设计规范是否有效、可理解并反映现实保真度？

- inputs_and_setting_cn：设计依据来自第2节的知识基础；采用Galster和Avgeriou的参考架构构建方法中的步骤I-V；评价采用逻辑推理和十位BPM研究者的七点Likert量表调查。

- designed_or_compared_object_cn：构建ViProMiRA的三层架构、颜色变体和可选组件；评价其与DOs的一致性和研究者感知。

- baseline_control_or_counterfactual_cn：DOs作为对照标准；调查没有对照条件。

##### objective_metrics

1. DOs符合性判断

2. 可理解性Likert均值6.3

3. 真实保真度Likert均值5.9

- analysis_method_cn：逻辑推理、研究者反馈调查、描述性统计。

- main_result_cn：逻辑推理认为ViProMiRA满足全部DOs；十位研究者均正面评价可理解性与真实保真度。

- argumentative_role_cn：在设计规范层面建立制品有效性。

- remaining_uncertainty_cn：研究者评价和逻辑推理不能证明实际运行可行性。

- link_to_next_phase_cn：下一步需要实例化为软件原型来验证内部一致性与实用性。

##### evidence_pointers

1. Section 6.2 Table 3

2. Section 6.2 Table 4

#### 4. 原型实现与演示（EVAL3）

- order：4

- name_cn：原型实现与演示（EVAL3）

- question_cn：ViProMiRA能否被实例化为可运行的软件原型？组件内部是否一致？

- inputs_and_setting_cn：参考架构中最广泛的绿色实例化变体；Python、PyTorch、SlowFast、Detectron2等开源框架；通过多次测试循环验证。

- designed_or_compared_object_cn：实现spatio-temporal activity recognition和Object Tracker组件，输出XES事件日志。

- baseline_control_or_counterfactual_cn：无对照；重点是内部一致性和运行可行性。

##### objective_metrics

1. 原型可运行性

2. XES日志导出能力

- analysis_method_cn：软件开发与测试循环。

- main_result_cn：原型能抽取业务事件并输出标准XES日志，可在ProM/PM4Py等工具中使用；仓库中提供演示视频。

- argumentative_role_cn：证明架构不是纸面制品，而是可实例化、可操作的技术方案。

- remaining_uncertainty_cn：原型在真实视频数据上的提取准确性未知。

- link_to_next_phase_cn：需要将原型应用于真实视频数据集以评估有用性。

##### evidence_pointers

1. Section 7 P1-P2

#### 5. 真实数据集应用与事件日志准确性评价（EVAL4-A）

- order：5

- name_cn：真实数据集应用与事件日志准确性评价（EVAL4-A）

- question_cn：原型从真实视频数据中提取的事件日志有多准确？与可观察真实行为相比召回率和精确率如何？

- inputs_and_setting_cn：Crêpe Dataset，90分钟、12个视频文件、1920x1080、模拟厨房场景，三个厨师和多个服务员，6个流程变体，9个活动类，53个case；训练41个case，评估12个case。

- designed_or_compared_object_cn：原型输出的Extracted_Log与基于视频标注生成的True_Log。

- baseline_control_or_counterfactual_cn：True_Log作为真实行为基准；另对比已知/未知资源的子集。

##### objective_metrics

1. 准确率69.70%

2. 召回率69.70%

3. 精确率82.36%

4. 已知资源子集准确率76.70%、精确率82.66%、召回率76.70%

- analysis_method_cn：事件实例级匹配、混淆矩阵、人工视频核查、合并连续子活动。

- main_result_cn：合并后107个检测活动实例，其中92个正确；六个人工核查补回标注缺失的活动；不同活动类别的表现与视觉显著性相关；未知资源上性能下降。

- argumentative_role_cn：量化证明原型能捕获大部分流程相关事件，且检测出的行为高概率正确。

- remaining_uncertainty_cn：准确性受标注质量、训练数据量和原型拆分活动的影响，尚未测试下游流程挖掘分析中的实际效果。

- link_to_next_phase_cn：所以需要继续用一致性检查和流程发现来评估对流程挖掘用例的有用性。

##### evidence_pointers

1. Section 8.1 Crêpe Dataset description

2. Section 8.2 Table 5

3. Section 8.2 Figure 6

#### 6. 一致性检查评价（EVAL4-B）

- order：6

- name_cn：一致性检查评价（EVAL4-B）

- question_cn：提取的事件日志与预定义流程模型的一致性如何？

- inputs_and_setting_cn：在ProM中导入True_Log与Extracted_Log，过滤complete事件并合并连续同活动事件，使用“Replay a Log on Petri Net for Conformance Analysis”插件。

- designed_or_compared_object_cn：True_Log和Extracted_Log在同一个Petri网模型上的fitness。

- baseline_control_or_counterfactual_cn：True_Log作为高一致性基线。

##### objective_metrics

1. True_Log fitness 97.98%

2. Extracted_Log fitness 79.81%

- analysis_method_cn：对齐重放、fitness计算、路径与异步移动分析。

- main_result_cn：真实日志高度一致；提取日志也达到较高fitness，大多数错误来自少数误检活动和未知资源相关case。

- argumentative_role_cn：显示原型输出可用于一致性检查这一经典流程挖掘用例。

- remaining_uncertainty_cn：只有一个数据集和一个流程模型，无法判断更复杂流程上的表现。

- link_to_next_phase_cn：需要再测试另一个流程挖掘用例——流程发现，以更全面证明有用性。

##### evidence_pointers

1. Section 8.3 P1-P4

2. Figure 7

#### 7. 流程发现评价（EVAL4-C）

- order：7

- name_cn：流程发现评价（EVAL4-C）

- question_cn：从提取日志中发现的流程模型是否接近真实过程？能否通过过滤低频率噪声改进质量？

- inputs_and_setting_cn：使用ProM的Inductive Miner-infrequent（IMf），改变分离阈值，分别用12个评估case和全部53个case计算fitness和precision。

- designed_or_compared_object_cn：从Extracted_Log发现的多个Petri网模型；以True_Log_12和True_Log_53为参照。

- baseline_control_or_counterfactual_cn：True_Log_12和True_Log_53作为代表性基准。

##### objective_metrics

1. 发现模型fitness

2. 基于对齐的precision

- analysis_method_cn：Inductive Miner-infrequent、对齐一致性、视觉比较。

- main_result_cn：模型6被认为表现最好；前三个活动与真实模型一致，但fold因检测缺失未成为所有路径的最终活动；过滤低频行为可以减轻误检影响。

- argumentative_role_cn：证明原型输出可支持流程发现，且对部分错误日志可通过算法处理得到可接受模型。

- remaining_uncertainty_cn：数据集简单、规模小、不是真实工业流程，流程发现结果不能直接泛化。

- link_to_next_phase_cn：由此转入结论，总结贡献并讨论局限与未来研究。

##### evidence_pointers

1. Section 8.4 P1-P4

2. Figure 8

## 各部分修辞架构

### abstract_moves

1. CONTEXT: 流程挖掘是BPM活跃研究方向

2. PHENOMENON: 结构化数据之外的盲点

3. GAP: 缺少从视频数据提取事件日志的标准化方法

4. RQ_OR_OBJECTIVE: 设计ViProMiRA参考架构

5. DESIGN_FEATURE: 灵活、用例驱动、情境相关实例化

6. RESULT: 原型自动提取超过70%的流程相关事件

### introduction_moves

1. CONTEXT: 流程挖掘及其商业价值

2. LIMITATION: 依赖结构化数据只覆盖10-20%数据

3. PHENOMENON: 人工活动构成盲点

4. PRACTICAL_STAKES: 人工观测不可扩展且Delphi研究强调非结构化数据优先级

5. PRIOR_KNOWLEDGE: NLP与传感器方法的优缺点

6. MECHANISM: 深度学习计算机视觉可把视频转为事件日志

7. GAP: 尚无整合计算机视觉到流程挖掘的指导体系

8. RQ_OR_OBJECTIVE: 提出研究问题并预告ViProMiRA

9. STUDY_OVERVIEW: 说明全文结构

### theory_and_knowledge_moves

1. PRIOR_KNOWLEDGE: ex-post与ex-ante流程挖掘用例

2. PRIOR_KNOWLEDGE: XES事件日志与事件抽取挑战

3. PRIOR_KNOWLEDGE: 事件抽象与复杂事件处理

4. PRIOR_KNOWLEDGE: 九种计算机视觉能力

5. REQUIREMENT: 把上述知识转化为DOs

### artifact_design_moves

1. DESIGN_FEATURE: 三层参考架构

2. DESIGN_FEATURE: Data Preprocessor的视频转帧与背景减除

3. DESIGN_FEATURE: Information Extractor的蓝/橙/绿实例化变体

4. DESIGN_FEATURE: Object Specifier子组件

5. DESIGN_FEATURE: Event Processor的事件聚合和XES导出

6. REQUIREMENT: 可选组件和变体满足DO1-DO3

7. METHOD_JUSTIFICATION: 采用Galster和Avgeriou的参考架构方法

### evaluation_moves

1. METHOD_JUSTIFICATION: EVAL1文献筛选

2. METHOD_JUSTIFICATION: EVAL2逻辑推理与研究者调查

3. METHOD_JUSTIFICATION: EVAL3原型实现与测试循环

4. METHOD_JUSTIFICATION: EVAL4真实数据集选择与日志对比

5. BENCHMARK_OR_CONTRAST: True_Log作为Extracted_Log的基准

6. RESULT: 召回率69.70%与精确率82.36%

7. RESULT: 一致性检查fitness对比

8. RESULT: 流程发现模型质量

9. ROBUSTNESS_OR_BOUNDARY_TEST: 已知资源与未知资源对比

### discussion_and_contribution_moves

1. CONTRIBUTION: 首个系统利用视频数据的参考架构

2. CONTRIBUTION: 首个支持多参与者并发案例的技术制品

3. CONTRIBUTION: 端到端开源实例化范例

4. LIMITATION_AND_FUTURE: 半具体描述、隐私、依赖监督学习、数据集局限

5. BOUNDARY_CONDITION: 视频只能部分填补盲点需结合其他数据

6. LIMITATION_AND_FUTURE: 未来研究无监督学习与更大数据集

## 理论/知识到设计的翻译

### 知识/理论基础

1. 流程挖掘用例知识：ex-post（discovery, conformance, enhancement）与ex-ante（predictive, prescriptive）

2. 事件日志抽取与标准：XES格式、事件抽象、复杂事件处理

3. 计算机视觉能力知识：背景减除、图像分类、目标检测、分割、姿态估计、跟踪、人脸识别、活动识别

4. 参考架构构建方法：Galster和Avgeriou的步骤，以及Angelov等的参考架构类型学

- 理论—设计耦合：partial

- 耦合判定理由：文章没有使用因果性或行为学理论来推导设计，而是从流程挖掘与计算机视觉文献归纳设计目标，再由目标映射到架构组件和实例化变体。计算机视觉组件的具体选择和技术实现（SlowFast、Detectron2）部分来自工程可用性与开源生态，而非严格理论演绎，因此知识基础显著影响了设计但并未完全决定技术制品选择。

- 理论到设计翻译链：流程挖掘中ex-post与ex-ante用例需要不同数据类型和输出接口 → DO1要求支持两类用例且灵活 → 架构设置Event Log Exporter与Event Notifier两种输出接口，并用可选组件匹配用例。事件日志需要标准化XES和抽象层次 → DO2要求XES与事件抽象 → Event Processor中的Event Aggregator执行复杂事件处理，Event Log Exporter输出XES。计算机视觉可从视频提取结构化信息但能力多样 → DO3要求覆盖、选择、组合CV能力 → Information Extractor包含可训练组件，并以蓝/橙/绿变体指导按需组合；检测到的事件低层信息再由Event Aggregator提升为高层业务事件。

### mapping_table

#### 1. 1

- theory_or_knowledge_claim_cn：流程挖掘已从ex-post向后看扩展到ex-ante前瞻性用例，不同用例需要不同事件数据和输出方式。

- mechanism_cn：ex-post需要完整历史事件日志，ex-ante可基于事件通知或低层事件流。

- design_requirement_cn：DO1.1/DO1.2：必须同时支持两类用例，并能针对目标用例灵活配置。

- artifact_choice_cn：Event Processor同时提供Event Log Exporter（供ex-post）和Event Notifier（供ex-ante）；架构包含可选组件以适应不同用例。

- evaluated_contrast_cn：原型实现主要验证ex-post两类用例（conformance checking和process discovery）；ex-ante输出接口未被实例化评价。

- objective_result_cn：提取日志可用于ProM中的一致性检查和流程发现，fitness 79.81%，发现模型可接受。

##### evidence_pointers

1. Section 5 Table 2 DO1

2. Section 6.1 Event Processor

3. Section 8.3-8.4

#### 2. 2

- theory_or_knowledge_claim_cn：流程挖掘要求标准化扁平事件日志，XES是公认标准；从分布式原始数据抽取事件是挑战。

- mechanism_cn：只有标准化事件日志才能被现有流程挖掘工具直接处理。

- design_requirement_cn：DO2.1：必须考虑从视频数据提取XES格式事件日志。

- artifact_choice_cn：Event Processor包含Event Log Exporter，把高层业务事件转换为XES。

- evaluated_contrast_cn：原型输出Extracted_Log可导入ProM，与True_Log对比。

- objective_result_cn：提取日志直接导入ProM并完成一致性检查，证明XES兼容性。

##### evidence_pointers

1. Section 5 DO2.1

2. Section 7 P1

3. Section 8.3 P1

#### 3. 3

- theory_or_knowledge_claim_cn：视频流产生的是低层连续事件，必须通过事件抽象和复杂事件处理才能得到高层业务事件。

- mechanism_cn：低层事件经过过滤、聚合和抽象成为有意义的活动实例，并可与预定义活动映射。

- design_requirement_cn：DO2.2：制品必须具备抽象与泛化能力。

- artifact_choice_cn：Event Aggregator使用复杂事件处理把低层事件聚合为高层业务事件，并关联到流程活动；case关联留给现有流程挖掘方法。

- evaluated_contrast_cn：原型倾向于拆分连续活动，因此评价前合并子活动，比较Extracted_Log与True_Log的活动实例。

- objective_result_cn：合并后准确率69.70%，原型产生的活动可由人工映射到真实活动实例。

##### evidence_pointers

1. Section 5 DO2.2

2. Section 6.1 Event Processor

3. Section 8.2 Table 5

#### 4. 4

- theory_or_knowledge_claim_cn：计算机视觉领域有多种提取结构化信息的能力，不同能力从视频中提取的对象、轨迹、姿态、活动信息不同。

- mechanism_cn：目标检测提供位置框，跟踪提供轨迹ID，姿态估计改善活动识别，活动识别输出活动类别。

- design_requirement_cn：DO3.1/DO3.2/DO3.3：应覆盖相关能力、指导选择并指导组合实践。

- artifact_choice_cn：Information Extractor包含多个可训练组件，以蓝/橙/绿三种变体组合能力；Object Specifier包含姿态、跟踪、人脸识别和对象重识别。

- evaluated_contrast_cn：原型实现绿色变体（spatio-temporal activity recognition + object detection + object tracking），用于多资源并发场景。

- objective_result_cn：召回率69.70%、精确率82.36%；明显依赖视觉显著对象；未知资源性能下降。

##### evidence_pointers

1. Section 5 DO3

2. Section 6.1 Information Extractor

3. Section 7 P1

4. Section 8.2 Figure 6

#### 5. 5

- theory_or_knowledge_claim_cn：视频数据可能涉及隐私问题，必须遵守数据保护法规并保持透明。

- mechanism_cn：未经同意处理视频中个人身份信息会带来合规风险；盲传感器可在存储前过滤敏感的视觉信息。

- design_requirement_cn：架构设计必须考虑隐私与合规。

- artifact_choice_cn：Data Preprocessor部分讨论数据主体同意与透明性，并提及盲传感器作为符合数据保护法源的替代输入。

- evaluated_contrast_cn：没有在原型或EVAL4中实证评价隐私相关组件。

- objective_result_cn：无直接结果；在结论中作为边界与未来方向。

##### evidence_pointers

1. Section 6.1 Data Preprocessor

2. Section 9.2 limitation

## 评价逻辑

### evaluation_modes

1. 文献/问题识别评价（EVAL1）

2. 逻辑推理评价设计目标符合性（EVAL2）

3. 研究者反馈调查（EVAL2）

4. 原型实现与测试循环（EVAL3）

5. 真实数据集上的事件日志准确性分析（EVAL4-A）

6. 一致性检查（EVAL4-B）

7. 流程发现（EVAL4-C）

- why_these_evaluations_cn：由于ViProMiRA是设计制品，单靠构建无法证明其有效性。作者依次用文献调研证明问题缺口真实存在且现有方案不足；用逻辑推理证明设计规范满足DOs；用研究者调查补充可理解性与现实保真度；用原型实现证明架构可实例化；最后用真实视频数据集覆盖活动识别准确性、经典ex-post流程挖掘用例，最终从多个侧面建立技术与实用价值。

- benchmark_and_contrast_chain_cn：EVAL4的核心锚点是True_Log，即基于视频原始标注生成的理想日志。Extracted_Log与True_Log对比给出召回率/精确率；随后同一对日志在一致性检查中形成fitness高低对照；流程发现则以True_Log_12和True_Log_53作为衡量发现模型质量的代表性基准。这样事件级准确性、日志级一致性和模型级发现质量形成了递进的评价链。

### claim_evidence_ledger

#### 1. 原型能从真实视频中自动提取超过70%的流程相关事件。

- claim_type：技术主张

- claim_cn：原型能从真实视频中自动提取超过70%的流程相关事件。

- evidence_cn：Crêpe数据集12个评估case中，合并后107个检测活动实例，92个正确，准确率/召回率69.70%。

- support_level：强支持，但受单一数据集和合并后处理限制

#### 2. ViProMiRA的绿色实例化变体可以作为可运行原型并输出标准XES日志。

- claim_type：制品主张

- claim_cn：ViProMiRA的绿色实例化变体可以作为可运行原型并输出标准XES日志。

- evidence_cn：Section 7原型实现、XES日志导入ProM、一致性检查插件运行成功。

- support_level：支持，原型为单实例化，未覆盖其他变体

#### 3. 活动识别准确性受视觉显著性影响；已知资源的表现优于未知资源。

- claim_type：机制主张

- claim_cn：活动识别准确性受视觉显著性影响；已知资源的表现优于未知资源。

- evidence_cn：活动类别的召回率分析显示涉及明显工具（锅、木勺、刀等）的活动召回率高；未知资源三case的性能明显下降。

- support_level：部分支持，基于描述性观察，无统计检验

#### 4. ViProMiRA适用于多资源、并发运行的简单人工流程。

- claim_type：边界主张

- claim_cn：ViProMiRA适用于多资源、并发运行的简单人工流程。

- evidence_cn：Crêpe数据集为简化厨房场景，原型能处理多厨师并发。

- support_level：边界清晰，但未在真实工业流程中检验

#### 5. 参考架构的三层分解、颜色变体和可选组件可以指导未来视频流程挖掘实现。

- claim_type：可复用设计知识

- claim_cn：参考架构的三层分解、颜色变体和可选组件可以指导未来视频流程挖掘实现。

- evidence_cn：EVAL2和EVAL4综合说明变体与组件可实例化并可用。

- support_level：有证据支持，但“可复用”本身未跨项目验证

#### 6. ViProMiRA是首个系统性桥接计算机视觉与流程挖掘的参考架构。

- claim_type：理论贡献

- claim_cn：ViProMiRA是首个系统性桥接计算机视觉与流程挖掘的参考架构。

- evidence_cn：EVAL1文献调研未发现同等一般化的架构。

- support_level：受限于文献检索范围和“首个”的强声明

- internal_validity_strategy_cn：使用True_Log作为真实行为锚点，明确活动实例匹配规则，合并连续子活动以消除原型事件拆分偏差，并对不一致处进行人工视频核查；训练集与评估集分离，评估集包含所有流程变体和多个资源；使用混淆矩阵和精确率/召回率。

- external_validity_strategy_cn：选择公开、包含并发多资源和多活动类的Crêpe数据集；同时用12个case和全量53个case验证发现模型的代表性；结论部分将适用范围限制到监督学习、简单流程、90分钟视频，并承认现实应用需要更多真实数据。

- what_is_not_actually_tested_cn：未检验蓝、橙两种实例化变体；未检验Event Notifier和ex-ante预测/处方用例；未检验隐私和盲传感器组件；未在真实组织流程中部署；未做跨数据集泛化；统计显著性和误差来源分析不足；case关联仍超出架构范围。

## 贡献闭环

- technical_claim_cn：使用计算机视觉与流程挖掘工具链，可以从真实视频中自动提取过程相关事件并生成可用XES日志。

- artifact_claim_cn：ViProMiRA作为参考架构能够被实例化，其最复杂绿色变体是首个支持无侵入提取多参与者并发案例视频日志的技术原型。

- mechanism_claim_cn：低层视频信息经目标检测、活动识别、对象跟踪和事件聚合后被抽象为高层业务事件，从而与流程挖掘活动映射。

- boundary_claim_cn：在监督学习条件下，对包含多资源和并发案例的简单人工厨房流程有效；未知资源会降低性能；更复杂流程、真实工业和隐私敏感环境仍需验证。

- reusable_design_knowledge_cn：按Data Preprocessor-Information Extractor-Event Processor分层、用实例化变体组合计算机视觉能力、以Event Aggregator实现复杂事件处理、用Event Log Exporter/Event Notifier匹配ex-post/ex-ante用例，这套结构可作为未来视频流程挖掘系统的参考蓝图。

- theoretical_contribution_cn：在流程挖掘与计算机视觉之间建立可复用的参考架构，为基于非结构化视频数据的流程挖掘研究提供理论化基础设施；明确以设计科学方式连接两个领域。

- how_discussion_closes_intro_gap_cn：引言指出缺少把计算机视觉能力系统整合进流程挖掘的指南；结论通过ViProMiRA的三层架构和变体明确回应了这个缺口，并声称这是首次系统性方案，从而把评价结果从单点原型提升到参考架构层面。

- overclaim_or_unsupported_leaps_cn：“首个系统性参考架构”和“首个技术制品”较强，但EVAL1只是文献检索而非全面系统综述；从单数据集原型推广到架构有效，在逻辑上仍有跳跃；架构中大量组件（如人脸识别、实例分割、Event Notifier）没有被实例化或测试，却宣称架构整体有效。

## 句级写作动作图谱

### 1. Abstract S1

- order：1

- section：Abstract

- locator：Abstract S1

- move_code：CONTEXT

- paraphrase_cn：流程挖掘是BPM中活跃的研究流，许多方法用于分析结构化流程数据。

- rhetorical_function_cn：开头给出领域背景，确定研究在流程挖掘知识体系中的位置。

- depends_on_cn：无需前置。

- sets_up_cn：为后面指出结构化数据之外的问题提供对比。

- evidence_pointer：Abstract 第1句

### 2. Abstract S2

- order：2

- section：Abstract

- locator：Abstract S2

- move_code：PHENOMENON

- paraphrase_cn：案例中只有数字化部分被流程系统直接捕获，人工活动常留下盲点。

- rhetorical_function_cn：引出具体经验现象，解释为何现有流程挖掘有覆盖缺口。

- depends_on_cn：依赖流程挖掘背景。

- sets_up_cn：为视频数据作为补充来源做铺垫。

- evidence_pointer：Abstract 第2句

### 3. Abstract S3

- order：3

- section：Abstract

- locator：Abstract S3

- move_code：GAP

- paraphrase_cn：视频数据含有流程相关信息，但缺少从非结构化视频提取事件日志的标准化方法。

- rhetorical_function_cn：明确研究空白。

- depends_on_cn：依赖盲点现象。

- sets_up_cn：为研究问题和制品引入提供逻辑依据。

- evidence_pointer：Abstract 第3句

### 4. Abstract S4

- order：4

- section：Abstract

- locator：Abstract S4

- move_code：RQ_OR_OBJECTIVE

- paraphrase_cn：为解决该问题设计了ViProMiRA参考架构，桥接计算机视觉与流程挖掘。

- rhetorical_function_cn：陈述核心回答——设计制品。

- depends_on_cn：依赖GAP。

- sets_up_cn：为摘要后续的评价结果做主体准备。

- evidence_pointer：Abstract S4

### 5. Abstract S5

- order：5

- section：Abstract

- locator：Abstract S5

- move_code：DESIGN_FEATURE

- paraphrase_cn：参考架构支持灵活、用例驱动、情境特定的实例化。

- rhetorical_function_cn：概括制品的关键设计属性。

- depends_on_cn：ViProMiRA提出后自然导出。

- sets_up_cn：为评价活动的设计提供标准。

- evidence_pointer：Abstract S5

### 6. Abstract S6

- order：6

- section：Abstract

- locator：Abstract S6

- move_code：RESULT

- paraphrase_cn：原型在真实视频数据集和监督学习场景中自动提取超过70%的流程相关事件。

- rhetorical_function_cn：用定量结果证明制品有用。

- depends_on_cn：依赖制品与评价设置。

- sets_up_cn：预告正文中EVAL4的结果。

- evidence_pointer：Abstract S6

### 7. Intro P1 S1-S3

- order：7

- section：Introduction

- locator：Intro P1 S1-S3

- move_code：CONTEXT

- paraphrase_cn：流程挖掘从事件日志中发现、监控和改进流程，已成为活跃领域，有学术会议和巨大商业前景。

- rhetorical_function_cn：建立问题重要性，说明该领域值得研究。

- depends_on_cn：无。

- sets_up_cn：为“现有流程挖掘只覆盖结构化数据”的批评提供领域基础。

- evidence_pointer：Introduction P1

### 8. Intro P2 S1-S3

- order：8

- section：Introduction

- locator：Intro P2 S1-S3

- move_code：LIMITATION

- paraphrase_cn：当前流程挖掘依赖结构化业务数据，而80-90%数据是非结构化，流程分析只能覆盖10-20%的数据，因此难以端到端分析含有未被信息系统跟踪的人工活动。

- rhetorical_function_cn：指出现有流程挖掘的核心限制。

- depends_on_cn：流程挖掘背景。

- sets_up_cn：引出盲点概念和非结构化数据机会。

- evidence_pointer：Introduction P2

### 9. Intro P3 S1-S2

- order：9

- section：Introduction

- locator：Intro P3 S1-S2

- move_code：PHENOMENON

- paraphrase_cn：文章把流程中无法被事件日志捕获的部分称为盲点；人工观察填补盲点耗时且不可扩展。

- rhetorical_function_cn：概念化问题现象，使抽象问题可操作。

- depends_on_cn：依赖上一段数据覆盖缺口。

- sets_up_cn：提出非结构化数据作为可行补救方向。

- evidence_pointer：Introduction P3 S1-S2

### 10. Intro P3 S3-S4

- order：10

- section：Introduction

- locator：Intro P3 S3-S4

- move_code：PRACTICAL_STAKES

- paraphrase_cn：大量非结构化数据如媒体文件和文本文档可用，Delphi研究中专家认为BPM应优先探索非结构化数据。

- rhetorical_function_cn：说明解决盲点问题的现实紧迫性。

- depends_on_cn：盲点概念。

- sets_up_cn：为视频数据成为研究对象提供优先级依据。

- evidence_pointer：Introduction P3 S3-S4

### 11. Intro P4 S1-S3

- order：11

- section：Introduction

- locator：Intro P4 S1-S3

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：已有NLP和传感器方法尝试利用非结构化数据，但传感器部署不可扩展且依赖位置，NLP易泛化但只覆盖信息系统内活动。

- rhetorical_function_cn：总结两种现有路线的优缺点。

- depends_on_cn：非结构化数据使用背景。

- sets_up_cn：说明视频数据作为替代/补充来源的动机。

- evidence_pointer：Introduction P4 S1-S3

### 12. Intro P4 S4

- order：12

- section：Introduction

- locator：Intro P4 S4

- move_code：TRANSITION

- paraphrase_cn：在注意隐私合规的前提下，常用摄像头视频有潜力使盲点流程可观察。

- rhetorical_function_cn：把问题从NLP/传感器转移到视频。

- depends_on_cn：已有方法局限性。

- sets_up_cn：为计算机视觉引入做铺垫。

- evidence_pointer：Introduction P4 S4

### 13. Intro P5 S1-S3

- order：13

- section：Introduction

- locator：Intro P5 S1-S3

- move_code：MECHANISM

- paraphrase_cn：深度学习的计算机视觉在特定场景已能识别对象和活动；若迁移到流程挖掘，从视频提取的事件和参与者可喂入结构化事件日志。

- rhetorical_function_cn：提供核心机制假说：视频→低层事件→结构化日志→流程挖掘。

- depends_on_cn：视频数据潜力。

- sets_up_cn：为研究问题中的“系统化利用”提供技术可能性。

- evidence_pointer：Introduction P5

### 14. Intro P6 S1

- order：14

- section：Introduction

- locator：Intro P6 S1

- move_code：GAP

- paraphrase_cn：计算机视觉与流程挖掘交叉的早期研究结果令人鼓舞，但目前缺乏如何整体集成计算机视觉能力到流程挖掘中的可靠指南。

- rhetorical_function_cn：明确文献空白。

- depends_on_cn：前面已有初期交叉研究。

- sets_up_cn：直接引出研究问题。

- evidence_pointer：Introduction P6 S1

### 15. Intro P6 S2

- order：15

- section：Introduction

- locator：Intro P6 S2

- move_code：RQ_OR_OBJECTIVE

- paraphrase_cn：由此提出研究问题：如何系统化地利用视频数据支持流程挖掘？

- rhetorical_function_cn：把空白转化为可回答的研究问题。

- depends_on_cn：GAP句。

- sets_up_cn：为全文定义中心目标。

- evidence_pointer：Introduction P6 S2

### 16. Intro P7 S1-S5

- order：16

- section：Introduction

- locator：Intro P7 S1-S5

- move_code：STUDY_OVERVIEW

- paraphrase_cn：提出ViProMiRA来回答问题，采用设计科学方法并做多种评价；概述全文按DSR流程组织。

- rhetorical_function_cn：预告制品、研究范式和论文结构。

- depends_on_cn：研究问题。

- sets_up_cn：为后续理论背景和DSR阶段提供导航。

- evidence_pointer：Introduction P7

### 17. Section 2.1 P1

- order：17

- section：Theory Background 2.1

- locator：Section 2.1 P1

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：流程挖掘最初定义discovery、conformance、enhancement三类用例，并可按数据来源和用途划分为ex-post与ex-ante。

- rhetorical_function_cn：引入DO1所需的核心分类知识。

- depends_on_cn：流程挖掘背景。

- sets_up_cn：为设计目标DO1.1/1.2提供知识基础。

- evidence_pointer：Section 2.1 P1

### 18. Section 2.1 P2

- order：18

- section：Theory Background 2.1

- locator：Section 2.1 P2

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：近年流程挖掘扩展到预测和处方分析等ex-ante用例，从历史数据预测剩余时间、结果或下一步动作。

- rhetorical_function_cn：补充用例分类的当代演化。

- depends_on_cn：ex-post/ex-ante分类。

- sets_up_cn：支持DO1.1要求支持ex-ante和ex-post。

- evidence_pointer：Section 2.1 P2

### 19. Section 2.2 P1-P2

- order：19

- section：Theory Background 2.2

- locator：Section 2.2 P1-P2

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：流程挖掘需要标准化的XES扁平日志；从原始数据中提取事件是挑战，现有研究多关注合成日志，较少处理真实世界数据抽取。

- rhetorical_function_cn：引出事件日志提取的知识基础及其缺口。

- depends_on_cn：流程挖掘用例。

- sets_up_cn：支持DO2.1关于XES的设定。

- evidence_pointer：Section 2.2 P1-P2

### 20. Section 2.2 P3

- order：20

- section：Theory Background 2.2

- locator：Section 2.2 P3

- move_code：MECHANISM

- paraphrase_cn：由于信息系统只覆盖现实世界一小部分，需要用补充数据源扩展日志；从视频等非结构化数据得到高层业务事件必须经过事件抽象，复杂事件处理可从低层事件流实时生成高层复杂事件。

- rhetorical_function_cn：说明视频低层事件如何变成可分析的高层事件。

- depends_on_cn：事件日志提取挑战。

- sets_up_cn：支持DO2.2和Event Aggregator设计。

- evidence_pointer：Section 2.2 P3

### 21. Section 2.3 P1

- order：21

- section：Theory Background 2.3

- locator：Section 2.3 P1

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：计算机视觉旨在从视觉数据中实现类似人类甚至超过人类的感知解释能力，但本文聚焦提取结构化信息的RGB能力，而非修改视觉数据的能力。

- rhetorical_function_cn：界定计算机视觉知识的范围。

- depends_on_cn：非结构化数据利用背景。

- sets_up_cn：为列出九种计算机视觉能力限定范围。

- evidence_pointer：Section 2.3 P1

### 22. Section 2.3 P2

- order：22

- section：Theory Background 2.3

- locator：Section 2.3 P2

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：基于相关研究综述识别出九种相关计算机视觉能力，包括背景减除、图像分类、目标检测、分割、姿态估计、目标跟踪、重识别、人脸识别和活动识别。

- rhetorical_function_cn：建立计算机视觉能力清单。

- depends_on_cn：计算机视觉范围。

- sets_up_cn：支持DO3.1和Information Extractor组件设计。

- evidence_pointer：Section 2.3 P2

### 23. Section 3 P1

- order：23

- section：Research Design

- locator：Section 3 P1

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：由于ViProMiRA是模型型设计制品，所以采用设计科学范式并遵循Peffers等的六阶段DSR流程。

- rhetorical_function_cn：说明总体研究范式选择。

- depends_on_cn：研究问题需要人工制品。

- sets_up_cn：为后文的阶段划分提供框架。

- evidence_pointer：Section 3 P1

### 24. Section 3 P2

- order：24

- section：Research Design

- locator：Section 3 P2

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：通用DSR未提供参考架构设计指南，因此补充Galster和Avgeriou的参考架构方法，并设置EVAL1-EVAL4连续评价活动。

- rhetorical_function_cn：说明采用补充方法和多阶段评价的原因。

- depends_on_cn：制品类型为参考架构。

- sets_up_cn：为EVAL1-EVAL4的编排提供蓝图。

- evidence_pointer：Section 3 P2

### 25. Section 3 P3-P5

- order：25

- section：Research Design

- locator：Section 3 P3-P5

- move_code：STUDY_OVERVIEW

- paraphrase_cn：概述各阶段：问题识别、设计目标、设计开发、演示、评价和沟通，并说明哪些Galster步骤被选用。

- rhetorical_function_cn：让读者预知每一阶段及其论证任务。

- depends_on_cn：DSR流程。

- sets_up_cn：为第4-8节每章建立阅读预期。

- evidence_pointer：Section 3 P3-P5

### 26. Section 4 P1

- order：26

- section：Problem Identification (EVAL1)

- locator：Section 4 P1

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：用半结构化文献搜索和前后向引用搜索识别从非结构化数据提取事件的相关方法。

- rhetorical_function_cn：为问题缺口提供文献证据。

- depends_on_cn：引言中的GAP。

- sets_up_cn：为表1和选择标准做方法说明。

- evidence_pointer：Section 4 P1

### 27. Section 4 P2

- order：27

- section：Problem Identification (EVAL1)

- locator：Section 4 P2

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：表1列出文本、传感器和视频等方法的类型、覆盖用例和抽象层次，多数方法与流程挖掘只是远亲关系。

- rhetorical_function_cn：系统呈现现有方法全貌。

- depends_on_cn：文献搜索。

- sets_up_cn：为后续筛选和分析提供对象。

- evidence_pointer：Section 4 Table 1

### 28. Section 4 P3

- order：28

- section：Problem Identification (EVAL1)

- locator：Section 4 P3

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：用三个标准筛选最可能解决问题的五项工作：通用方案、至少一个流程挖掘用例、有实现或实例化。

- rhetorical_function_cn：说明为何只深入分析部分文献。

- depends_on_cn：表1方法集合。

- sets_up_cn：为详细比较现有方案能力边界做准备。

- evidence_pointer：Section 4 P3

### 29. Section 4 P4

- order：29

- section：Problem Identification (EVAL1)

- locator：Section 4 P4

- move_code：LIMITATION

- paraphrase_cn：现有方法都不覆盖ex-ante用例，只有少数生成XES日志，且除个别工作外没有将多种计算机视觉能力以可泛化方式组合。

- rhetorical_function_cn：逐条指出候选方法不能满足系统利用视频数据的要求。

- depends_on_cn：筛选结果。

- sets_up_cn：为GAP结论提供具体支撑。

- evidence_pointer：Section 4 P4

### 30. Section 4 P5

- order：30

- section：Problem Identification (EVAL1)

- locator：Section 4 P5

- move_code：GAP

- paraphrase_cn：因此已有方法只在各自领域有价值，不能系统开发视频数据在流程挖掘中的潜力，需要扩展知识库的新制品。

- rhetorical_function_cn：收敛文献分析为明确空白。

- depends_on_cn：上一句的LIMITATION。

- sets_up_cn：为设计目标定义做过渡。

- evidence_pointer：Section 4 P5

### 31. Section 5 P1

- order：31

- section：Definition of Design Objectives

- locator：Section 5 P1

- move_code：REQUIREMENT

- paraphrase_cn：从第2节流程挖掘与计算机视觉文献中推导设计目标，用于指导开发和评价。

- rhetorical_function_cn：说明DOs来源与用途。

- depends_on_cn：理论背景与GAP。

- sets_up_cn：引出表2各条DO。

- evidence_pointer：Section 5 P1

### 32. Section 5 Table 2 DO1.1

- order：32

- section：Definition of Design Objectives

- locator：Section 5 Table 2 DO1.1

- move_code：REQUIREMENT

- paraphrase_cn：制品必须同时支持ex-ante和ex-post流程挖掘用例，因为流程挖掘已经从回顾性扩展到了前瞻性。

- rhetorical_function_cn：把用例知识转成明确要求。

- depends_on_cn：Section 2.1。

- sets_up_cn：影响Event Processor输出接口设计。

- evidence_pointer：Section 5 Table 2 DO1.1

### 33. Section 5 Table 2 DO1.2

- order：33

- section：Definition of Design Objectives

- locator：Section 5 Table 2 DO1.2

- move_code：REQUIREMENT

- paraphrase_cn：制品必须灵活支持目标流程挖掘用例，因为不同用例可能不需要完整结构化日志。

- rhetorical_function_cn：强调配置灵活性要求。

- depends_on_cn：用例差异知识。

- sets_up_cn：驱动架构中可选组件与实例化变体。

- evidence_pointer：Section 5 Table 2 DO1.2

### 34. Section 5 Table 2 DO2.1

- order：34

- section：Definition of Design Objectives

- locator：Section 5 Table 2 DO2.1

- move_code：REQUIREMENT

- paraphrase_cn：制品必须考虑从视频数据提取XES格式事件日志，以确保与现有工具互操作。

- rhetorical_function_cn：把标准知识转成输出要求。

- depends_on_cn：Section 2.2。

- sets_up_cn：促使Event Log Exporter组件出现。

- evidence_pointer：Section 5 Table 2 DO2.1

### 35. Section 5 Table 2 DO2.2

- order：35

- section：Definition of Design Objectives

- locator：Section 5 Table 2 DO2.2

- move_code：REQUIREMENT

- paraphrase_cn：制品必须具备抽象和泛化能力，以从非结构化视频事件流导出有意义的业务活动层事件。

- rhetorical_function_cn：把事件抽象知识转成能力要求。

- depends_on_cn：Section 2.2 event abstraction。

- sets_up_cn：引导Event Aggregator组件。

- evidence_pointer：Section 5 Table 2 DO2.2

### 36. Section 5 Table 2 DO3.1-DO3.3

- order：36

- section：Definition of Design Objectives

- locator：Section 5 Table 2 DO3.1-DO3.3

- move_code：REQUIREMENT

- paraphrase_cn：制品必须覆盖相关计算机视觉能力、指导按用例选择合适能力，并指导如何组合实践。

- rhetorical_function_cn：将计算机视觉知识转成设计约束。

- depends_on_cn：Section 2.3。

- sets_up_cn：为Information Extractor组件和颜色变体提供依据。

- evidence_pointer：Section 5 Table 2 DO3

### 37. Section 6.1 P1

- order：37

- section：Design and Development

- locator：Section 6.1 P1

- move_code：DESIGN_FEATURE

- paraphrase_cn：ViProMiRA包含Data Preprocessor、Information Extractor、Event Processor三个子系统层，并以颜色变体和可选组件提供实例化指导。

- rhetorical_function_cn：总体展示制品结构。

- depends_on_cn：DOs。

- sets_up_cn：为各层细节介绍设框架。

- evidence_pointer：Section 6.1 Figure 3

### 38. Section 6.1 Data Preprocessor

- order：38

- section：Design and Development

- locator：Section 6.1 Data Preprocessor

- move_code：DESIGN_FEATURE

- paraphrase_cn：Data Preprocessor负责视频转帧、帧率同步、分辨率调整，并可在静态镜头下用背景减除，同时考虑隐私合规。

- rhetorical_function_cn：描述架构输入层的组件。

- depends_on_cn：ViProMiRA总体架构。

- sets_up_cn：为后续信息提取提供标准化帧输入。

- evidence_pointer：Section 6.1 Data Preprocessor段落

### 39. Section 6.1 Information Extractor P1

- order：39

- section：Design and Development

- locator：Section 6.1 Information Extractor P1

- move_code：DESIGN_FEATURE

- paraphrase_cn：Information Extractor接收预处理后的帧序列，组合可训练计算机视觉组件，以分层方式提取有意义信息。

- rhetorical_function_cn：说明核心提取层的通用机制。

- depends_on_cn：DO3。

- sets_up_cn：引出蓝、橙、绿三种变体。

- evidence_pointer：Section 6.1 Information Extractor段落

### 40. Section 6.1 Information Extractor P2

- order：40

- section：Design and Development

- locator：Section 6.1 Information Extractor P2

- move_code：DESIGN_FEATURE

- paraphrase_cn：蓝色变体仅用Image Classifier处理简单分类；橙色变体用Temporal Activity Recognizer处理单执行者顺序活动；绿色变体结合Object Detector与Spatio-temporal Activity Recognizer处理多资源并发活动。

- rhetorical_function_cn：说明不同变体适配不同流程情境。

- depends_on_cn：九种计算机视觉能力。

- sets_up_cn：为原型选择绿色变体做铺垫。

- evidence_pointer：Section 6.1 Information Extractor段落

### 41. Section 6.1 Information Extractor P3

- order：41

- section：Design and Development

- locator：Section 6.1 Information Extractor P3

- move_code：DESIGN_FEATURE

- paraphrase_cn：Object Specifier包含姿态估计、对象跟踪、人脸识别和对象重识别四个子组件，分别用于增强活动识别、短时区分资源、稳定识别已知人员和跨镜头重识别。

- rhetorical_function_cn：详细描述复杂变体中的附加能力。

- depends_on_cn：多参与者场景需求。

- sets_up_cn：为EVAL3原型实现组件选择提供依据。

- evidence_pointer：Section 6.1 Object Specifier段落

### 42. Section 6.1 Event Processor P1

- order：42

- section：Design and Development

- locator：Section 6.1 Event Processor P1

- move_code：DESIGN_FEATURE

- paraphrase_cn：Event Processor中的Event Aggregator从低层事件排除噪声，使用复杂事件处理导出高层业务事件流，并可关联到预定义流程活动。

- rhetorical_function_cn：说明低层视觉事件如何变成业务事件。

- depends_on_cn：DO2.2和事件抽象知识。

- sets_up_cn：为事件日志导出和通知输出做铺垫。

- evidence_pointer：Section 6.1 Event Processor + Figure 4

### 43. Section 6.1 Event Processor P2

- order：43

- section：Design and Development

- locator：Section 6.1 Event Processor P2

- move_code：DESIGN_FEATURE

- paraphrase_cn：Event Log Exporter把聚合事件转成流程挖掘兼容格式，支持ex-post用例；Event Notifier转发事件通知，支持ex-ante用例。

- rhetorical_function_cn：说明两个输出接口如何覆盖不同用例。

- depends_on_cn：DO1.1。

- sets_up_cn：为EVAL4只测ex-post用例留下边界说明。

- evidence_pointer：Section 6.1 Event Processor倒数段

### 44. Section 6.2 P1

- order：44

- section：Design and Development (EVAL2)

- locator：Section 6.2 P1

- move_code：RESULT

- paraphrase_cn：通过逻辑推理逐条验证ViProMiRA符合所有设计目标，并以表3给出合著者的一致判断。

- rhetorical_function_cn：在构建后立即建立设计规范性证据。

- depends_on_cn：前文设计规范。

- sets_up_cn：为后续原型测试提供有效性基线。

- evidence_pointer：Section 6.2 Table 3

### 45. Section 6.2 P2-P3

- order：45

- section：Design and Development (EVAL2)

- locator：Section 6.2 P2-P3

- move_code：RESULT

- paraphrase_cn：十位BPM研究者在讨论后通过匿名问卷正面评价了可理解性和真实保真度。

- rhetorical_function_cn：用外部研究者感知补充逻辑推理。

- depends_on_cn：设计规范。

- sets_up_cn：强化架构设计阶段的有效性。

- evidence_pointer：Section 6.2 Table 4

### 46. Section 7 P1

- order：46

- section：Demonstration (EVAL3)

- locator：Section 7 P1

- move_code：DESIGN_FEATURE

- paraphrase_cn：实现最广泛的绿色实例化变体为软件原型，支持时空活动识别与对象跟踪，并输出XES日志。

- rhetorical_function_cn：说明原型覆盖架构的哪些部分。

- depends_on_cn：绿色变体设计。

- sets_up_cn：为EVAL4使用原型提供技术说明。

- evidence_pointer：Section 7 P1

### 47. Section 7 P2

- order：47

- section：Demonstration (EVAL3)

- locator：Section 7 P2

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：原型基于Python、PyTorch、SlowFast和Detectron2等开源框架实现，以一秒间隔进行活动识别；测试循环确认内部一致性与可用性。

- rhetorical_function_cn：说明技术实现细节与验证方式。

- depends_on_cn：绿色变体。

- sets_up_cn：为真实数据集评价中的训练与预测参数做解释。

- evidence_pointer：Section 7 P2

### 48. Section 8.1 P1-P2

- order：48

- section：Evaluation (EVAL4)

- locator：Section 8.1 P1-P2

- move_code：BENCHMARK_OR_CONTRAST

- paraphrase_cn：选择Crêpe数据集是因为其公开、具有连续视频的空间时间标注，并包含多活动、多资源与并发案例，共6个变体、9个活动类和53个case。

- rhetorical_function_cn：说明数据集为何适合作为基准。

- depends_on_cn：原型需要多资源并发场景。

- sets_up_cn：为后续训练/评估划分和日志构造奠定基础。

- evidence_pointer：Section 8.1 P1-P2

### 49. Section 8.1 P3-P4

- order：49

- section：Evaluation (EVAL4)

- locator：Section 8.1 P3-P4

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：按原始帧标注自动生成一秒间隔标签，把无关活动归为undefined；将41个case用于训练，12个case用于评估。

- rhetorical_function_cn：说明监督训练和评估集划分。

- depends_on_cn：数据集的带有帧标注。

- sets_up_cn：为Extracted_Log与True_Log定义做准备。

- evidence_pointer：Section 8.1 P3-P4

### 50. Section 8.1 P5-P6

- order：50

- section：Evaluation (EVAL4)

- locator：Section 8.1 P5-P6

- move_code：BENCHMARK_OR_CONTRAST

- paraphrase_cn：将原型输出记为Extracted_Log，将基于标注的可观察事件记为True_Log，二者用于对比。

- rhetorical_function_cn：建立评价中的基准与处理对象。

- depends_on_cn：数据集划分。

- sets_up_cn：为第8.2节精度/召回率分析提供两个日志。

- evidence_pointer：Section 8.1 P5-P6

### 51. Section 8.2 P1

- order：51

- section：Evaluation (EVAL4)

- locator：Section 8.2 P1

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：在事件实例级别比较Extracted_Log与True_Log，分别回答召回率和精确率两个问题。

- rhetorical_function_cn：明确准确性评价的两个指标及其含义。

- depends_on_cn：两个日志。

- sets_up_cn：为匹配规则和混淆矩阵做方法基础。

- evidence_pointer：Section 8.2 P1

### 52. Section 8.2 P2-P3

- order：52

- section：Evaluation (EVAL4)

- locator：Section 8.2 P2-P3

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：定义匹配规则：检测活动需落在真实活动的时间边界内且类别相同；合并连续同类子活动后再比较。

- rhetorical_function_cn：说明如何公正处理原型的事件拆分行为。

- depends_on_cn：事件实例级比较。

- sets_up_cn：为表5和混淆矩阵数字提供口径。

- evidence_pointer：Section 8.2 P2-P3

### 53. Section 8.2 Table 5

- order：53

- section：Evaluation (EVAL4)

- locator：Section 8.2 Table 5

- move_code：RESULT

- paraphrase_cn：合并后续同类事件后，Extracted_Log从136个活动实例降为107个，True_Log保持114个。

- rhetorical_function_cn：展示预处理后的日志属性。

- depends_on_cn：匹配规则。

- sets_up_cn：为召回率/精确率计算提供最终数据。

- evidence_pointer：Section 8.2 Table 5

### 54. Section 8.2 P4-P5

- order：54

- section：Evaluation (EVAL4)

- locator：Section 8.2 P4-P5

- move_code：RESULT

- paraphrase_cn：混淆矩阵显示共有92个正确检测，对应69.70%准确率；人工核查还发现六个标注缺失但被原型正确检测到的活动。

- rhetorical_function_cn：给出核心定量结果。

- depends_on_cn：匹配后的日志。

- sets_up_cn：为后续按活动类别分析错误模式提供总览。

- evidence_pointer：Section 8.2 Figure 6

### 55. Section 8.2 P6-P8

- order：55

- section：Evaluation (EVAL4)

- locator：Section 8.2 P6-P8

- move_code：ROBUSTNESS_OR_BOUNDARY_TEST

- paraphrase_cn：涉及明显视觉对象的活动召回率高，fold、grate、transfer较低；未知资源上的12个case中性能显著下降。

- rhetorical_function_cn：探索活动类别和资源类型对性能的边界影响。

- depends_on_cn：混淆矩阵结果。

- sets_up_cn：为结论部分的外部边界和泛化限制提供证据。

- evidence_pointer：Section 8.2 P6-P8

### 56. Section 8.3 P1-P2

- order：56

- section：Evaluation (EVAL4)

- locator：Section 8.3 P1-P2

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：用ProM对两个日志做一致性检查，过滤complete事件并合并连续事件后，使用对齐重放插件计算fitness。

- rhetorical_function_cn：说明第二个流程挖掘用例的评价方法。

- depends_on_cn：XES日志。

- sets_up_cn：为fitness对比提供计算依据。

- evidence_pointer：Section 8.3 P1-P2

### 57. Section 8.3 P3-P4

- order：57

- section：Evaluation (EVAL4)

- locator：Section 8.3 P3-P4

- move_code：RESULT

- paraphrase_cn：True_Log的fitness为97.98%，Extracted_Log为79.81%，前者高度合规，后者也可接受。

- rhetorical_function_cn：对比两个日志的一致性表现。

- depends_on_cn：一致性检查插件。

- sets_up_cn：说明原型输出可用于一致性检查。

- evidence_pointer：Section 8.3 P3-P4

### 58. Section 8.3 P5

- order：58

- section：Evaluation (EVAL4)

- locator：Section 8.3 P5

- move_code：RESULT

- paraphrase_cn：提取日志的多数fitness损失来自少量错误活动实例，但原型仍然成功捕捉了大部分可观察行为。

- rhetorical_function_cn：解释fitness差异来源，弱化误差影响。

- depends_on_cn：两个fitness值。

- sets_up_cn：为流程发现中过滤低频行为提供理由。

- evidence_pointer：Section 8.3 P5

### 59. Section 8.4 P1-P2

- order：59

- section：Evaluation (EVAL4)

- locator：Section 8.4 P1-P2

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：采用Inductive Miner-infrequent进行流程发现，并以True_Log_12和True_Log_53作为发现模型质量基准，同时计算fitness和precision。

- rhetorical_function_cn：说明流程发现评价的技术路线。

- depends_on_cn：提取日志。

- sets_up_cn：为模型6结果做解释。

- evidence_pointer：Section 8.4 P1-P2

### 60. Section 8.4 P3-P4

- order：60

- section：Evaluation (EVAL4)

- locator：Section 8.4 P3-P4

- move_code：RESULT

- paraphrase_cn：模型6被认为最佳：前三个活动顺序与真实模型一致，但fold未能成为所有路径的最终活动；模型在四种质量准则间取得较好平衡。

- rhetorical_function_cn：给出流程发现的核心结果。

- depends_on_cn：IMf和阈值变化。

- sets_up_cn：说明过滤低频行为可作为部分错误日志的处理策略。

- evidence_pointer：Section 8.4 Figure 8

### 61. Section 8.4 P5

- order：61

- section：Evaluation (EVAL4)

- locator：Section 8.4 P5

- move_code：TRANSITION

- paraphrase_cn：EVAL4总体上证明了原型和ViProMiRA在流程挖掘中的适用性与有用性，即使是部分错误的事件日志也仍具潜力。

- rhetorical_function_cn：总结评价阶段，连接结论。

- depends_on_cn：前三个子评价。

- sets_up_cn：为结论部分贡献声明和未来研究铺垫。

- evidence_pointer：Section 8.4 P5

### 62. Section 9.1 P1-P3

- order：62

- section：Conclusion

- locator：Section 9.1 P1-P3

- move_code：CONTRIBUTION

- paraphrase_cn：在非结构化数据快速增长背景下，本研究用ViProMiRA回答了如何系统利用视频数据支持流程挖掘，并通过多阶段评价证明其价值。

- rhetorical_function_cn：重申研究问题、制品和评价链，形成闭环。

- depends_on_cn：全部前文。

- sets_up_cn：为后续具体贡献声明做总起。

- evidence_pointer：Section 9.1 P1-P3

### 63. Section 9.1 P4

- order：63

- section：Conclusion

- locator：Section 9.1 P4

- move_code：CONTRIBUTION

- paraphrase_cn：这是首个系统利用视频数据支持流程挖掘的参考架构，也是首个支持多参与者并发案例提取的技术制品。

- rhetorical_function_cn：提出核心新颖性声明。

- depends_on_cn：EVAL1和EVAL4结果。

- sets_up_cn：提升贡献层级到理论化基础设施。

- evidence_pointer：Section 9.1 P4

### 64. Section 9.1 P4-P5

- order：64

- section：Conclusion

- locator：Section 9.1 P4-P5

- move_code：CONTRIBUTION

- paraphrase_cn：还提供一个端到端开源实现范例，可以指导未来系统实现。

- rhetorical_function_cn：增加可复用实践贡献。

- depends_on_cn：EVAL3原型实现。

- sets_up_cn：为局限与未来研究做铺垫。

- evidence_pointer：Section 9.1 P5

### 65. Section 9.2 P1-P3

- order：65

- section：Conclusion

- locator：Section 9.2 P1-P3

- move_code：LIMITATION_AND_FUTURE

- paraphrase_cn：半具体架构不能直接作为完整实现方案；视频隐私需严格合规；依赖高质量摄像头和深度学习硬件。

- rhetorical_function_cn：对制品本身的技术和合规边界作出限制。

- depends_on_cn：架构设计和实现经验。

- sets_up_cn：为未来改进方向提供直接线索。

- evidence_pointer：Section 9.2 P1-P3

### 66. Section 9.2 P4-P6

- order：66

- section：Conclusion

- locator：Section 9.2 P4-P6

- move_code：LIMITATION_AND_FUTURE

- paraphrase_cn：视频只能部分填补盲点，需与其他数据源结合；原型依赖监督学习；Crêpe数据集不是真实工业流程且只有90分钟。

- rhetorical_function_cn：界定评价证据的适用范围。

- depends_on_cn：EVAL4设置。

- sets_up_cn：引出未来研究建议。

- evidence_pointer：Section 9.2 P4-P6

### 67. Section 9.2 P7

- order：67

- section：Conclusion

- locator：Section 9.2 P7

- move_code：LIMITATION_AND_FUTURE

- paraphrase_cn：未来研究应探索无监督学习、更大规模数据集、盲传感器、更复杂流程、多模态数据，并持续更新架构。

- rhetorical_function_cn：为后续研究提供路线图，同时承认当前贡献的边界。

- depends_on_cn：所有局限。

- sets_up_cn：以开放问题收尾。

- evidence_pointer：Section 9.2 P7

## 写作技术

- gap_construction_cn：先用数据量悬殊强调流程挖掘只覆盖结构化数据的一小部分，再把人工活动定义为盲点，然后逐个否定文本和传感器路线的可扩展性，最后指出虽有视频+流程挖掘早期交叉研究，但缺少一般化的参考架构，于是自然形成缺口。

- signposting_cn：在引言末用一段列出章节安排；在第三节研究设计中提前标注EVAL1至EVAL4；每章开头经常重述当前DSR阶段，使读者始终知道论证位置。

- transition_logic_cn：每个评价阶段的结束都会留下未解决问题并引出下一阶段：EVAL1确认缺口→定义DOs；EVAL2确认设计规范→EVAL3实例化；EVAL3验证可运行→EVAL4验证真实数据；EVAL4事件级准确性→一致性检查→流程发现，逐层加码。

- claim_evidence_rhythm_cn：每提出一个设计组件后，后文几乎都有对应证据：DOs由文献支撑，组件由EVAL2逻辑推理支撑，变体选择由原型实现支撑，提取效果由混淆矩阵支撑，流程挖掘适用性由fitness和过程模型支撑。

- benchmark_narrative_cn：True_Log不是外部公开benchmark，而是由视频标注构造的“真实日志”；文章反复以True_Log为锚点评价Extracted_Log，形成“自动提取 vs 可观察真相”的叙事；对流程挖掘模型又以全量53个case作为代表性参照。

- theory_return_cn：文末并未发展新理论，而是把架构放到桥接计算机视觉与流程挖掘的理论化位置，声称参考架构和实例化路径可以作为未来研究的理论基础，从而把单点原型结果提升为领域基础设施。

- contribution_positioning_cn：用“首个”强调原创性，同时用EVAL1的系统性文献比较支持“尚无一般化方案”的断言；把技术原型的具体结果限定为对架构的“有用性和适用性证明”，避免只声称单一benchmark性能。

- novelty_protection_cn：通过补做原型评价的两个经典用例、对比已知/未知资源、展示开源实现路径、说明合并子活动和人工核查细节，把结果放在“系统化架构+可复现实现”上，而不仅是70%召回率这一数字，从而减少被贬为一次性实验结果。

## 可复用研究与写作程序

### structure_steps

#### 1. 1

- step：1

- writing_job_cn：用具体现象和行业数据建立问题重要性，提出盲点等可操作概念。

- research_job_cn：识别研究领域的主要数据缺口，并把一般问题收缩为可研究的具体矛盾。

- required_evidence_cn：领域权威数据、行业案例、专家调查或标准引用。

- transition_to_next_cn：从问题缺口过渡到“现有方法为何不够”。

#### 2. 2

- step：2

- writing_job_cn：系统梳理已有方法的类别，逐类说明它们为何不能解决问题。

- research_job_cn：做文献搜索，用明确标准筛选最接近的候选方案，并比较其能力边界。

- required_evidence_cn：候选文献列表、筛选标准、逐个缺点说明。

- transition_to_next_cn：由文献空白过渡到需要新制品。

#### 3. 3

- step：3

- writing_job_cn：从知识基础中抽取出可验证的设计目标（DOs），并以表格列出。

- research_job_cn：综合多个相关领域知识，把问题转化为制品必须满足的需求。

- required_evidence_cn：每条DO都需有文献依据或领域标准支撑。

- transition_to_next_cn：DOs直接指导制品设计。

#### 4. 4

- step：4

- writing_job_cn：描述制品总体结构、组件、变体、可选部分及使用选择逻辑。

- research_job_cn：采用适合制品类型的设计方法构建制品，并考虑变体与实例化空间。

- required_evidence_cn：设计图、组件职责说明、DOs到组件的映射关系。

- transition_to_next_cn：先通过逻辑推理证明设计规范符合DOs，再进入实例化。

#### 5. 5

- step：5

- writing_job_cn：说明如何把架构的某一部分实例化为可运行原型。

- research_job_cn：实现原型，测试内部一致性和基本功能，确保后续评价可用。

- required_evidence_cn：技术栈、原型功能、输出格式、测试结果。

- transition_to_next_cn：原型需要在真实数据上评价。

#### 6. 6

- step：6

- writing_job_cn：选择合适数据集，清晰定义基准和评价指标，报告核心定量结果。

- research_job_cn：构造事件级对比、领域标准指标、下游代表性用例等分层评价。

- required_evidence_cn：数据集说明、基准日志、指标（recall/precision/fitness等）、误差分析。

- transition_to_next_cn：评价结果用于回答研究问题和贡献声明。

#### 7. 7

- step：7

- writing_job_cn：把评价结果提升为跨数据集、跨项目可复用的设计知识，并诚实说明边界。

- research_job_cn：归纳制品主张、边界条件和未来研究方向，避免把单次结果过度泛化。

- required_evidence_cn：与引言缺口回应的显著对照、局限性说明、未来可检验问题。

- transition_to_next_cn：全文结束。

### most_transferable_moves_cn

1. 用一个形象概念（如blind spot）把数据覆盖问题压缩成鲜明研究缺口。

2. 先逐一否定现有路线，再指出目标数据源的特殊潜力。

3. 用设计目标表格把文献知识转化为可操作制品要求。

4. 用“文献评价+逻辑推理+研究者反馈+原型演示+真实数据用途评价”的多层评价链。

5. 用真实/理想日志作为基准，先做事件级准确性，再做流程级一致性检查和发现。

6. 在结论中把单点原型结果放回参考架构和理论化基础设施的高度。

### resource_intensive_or_nonstandard_parts_cn

1. 构建完整的视频训练和事件日志提取原型需要大量标注视频数据、深度学习和标注人工成本。

2. Crêpe数据集虽公开但不是常见流程挖掘benchmark，依赖带空间时间标注的视频数据集本身稀缺。

3. 以十位研究者进行设计评审调查并非所有研究都能复制。

4. 使用多个ProM插件完成一致性检查和流程发现的复现路径较复杂。

### what_not_to_copy_superficially_cn

1. 不能只复制“参考架构+颜色变体”的外壳，而没有逐条DOs到组件的映射。

2. 不能只报告recall/precision而不给匹配规则、日志合并操作和人工核查过程。

3. 不能只声称“首个”而不做EVAL1式的系统文献筛选和限制性比较。

4. 不能把单一数据集上的原型指标当作架构整体的普适有效性。

- single_best_description_of_the_routine_cn：先证明现有路线的碎片化，再以设计目标统摄多领域知识构建参考架构，最后用理想日志为锚逐层评价事件级准确性和流程挖掘用例，最终把单原型结果上升为可复用设计基础设施。

## 分析边界

文章全文完整，但补充材料A-D、附录表格和部分图表细节未能全部阅读；对EVAL2研究者调查的具体问卷内容只能依据正文描述；句子级位置使用段落和节点标识而非精确页码，可能存在轻度定位偏差。
