# Attending to Customer Attention: A Novel Deep Learning Method for Leveraging Multimodal Online Reviews to Enhance Sales Prediction

- 作者：Gang Chen; Lihua Huang; Shuaiyong Xiao; Chenghong Zhang; Huimin Zhao
- 年份 / 期刊：2024 / Information Systems Research
- DOI：10.1287/isre.2021.0292
- 源文件：28706_2024_attending-to-customer-attention-a-novel-deep-learning-method-for-leveraging-multimodal-online-re.md
- 论文主类型：build_evaluate_design_science
- 主导写作弧线：problem_theory_design_test_return
- 置信度：0.76

## 文章级论证概况

- 核心问题：如何概念化并利用顾客对多模态在线评论的注意力，从而更有效地提升基于多模态评论的销售预测？

- 制品与设计：提出一个多模态深度学习方法DTV-AMI，其中DTV包含语义多样性、时效性和投票意识三种注意力机制，AMI用于文本与图像的自适应交互注意力；设计基础是过程-粒度框架，将顾客注意力分解为评论集合、评论子集、单条评论和评论元素四个粒度层次，并导出四个内容无关的注意力指标。

- 客观结果：在案例研究中预测酒店月度入住率，基于2685家酒店、125万条评论文本和19.7万张评论图片，DTV-AMI在预测性能和多模态表征学习性能上均优于基准和八种先进基准方法；集成历史销售、评论表征与月份指标后，最佳模型（DTV-AMI-mh的XGBoost，半年时间窗）达到5.32% RMSE，比仅用历史销售的ARIMA最佳结果改进24.4%。

- 核心贡献：作者声称四方面贡献：将顾客注意力概念化为多个粒度层次并导出四个指标；提出DTV-AMI这一设计科学制品；基于大规模真实案例展示其预测和表征优势；深化对顾客注意力随时间、语义多样性、投票和图文交互变化的认识。

- 整篇论证链：文章从“评论有帮助性不一定等于预测有用”的缺口出发，先指出现有帮助性指标是评论层面的量化指标，未捕捉顾客在接收阶段的选择性注意。作者用信息处理/信息学习理论、双加工理论、选择效应和精细加工可能性模型，把顾客注意力分解为时间性、语义多样性、投票意识和多模态交互四个指标，并把这些指标翻译成四种神经网络注意力机制，进而构成DTV-AMI。实证部分用酒店入住率预测案例依次完成端到端预测性能比较、表征学习性能比较、历史销售时间序列基准、集成特征预测、注意力权重的探索性分析和消融分析，最终把预测性能优势上升为对顾客注意力机制的理论解释和可复用设计知识。

## 类型与写作弧线判定

- 论文主类型判定：文章明确将自己定位在设计科学范式（引用Hevner et al. 2004和Gregor & Hevner 2013），强调设计理由（design rationale）是制品设计与评价的基础；核心工作是先导出顾客注意力指标作为设计要求，再构建DTV-AMI制品，最后用真实数据评价制品，并提出设计科学贡献。

- 主导写作弧线判定：文章从现实问题与文献缺口出发，引入过程-粒度框架和多个理论，将其转化为四个设计指标和四个注意力机制，经过多轮实验验证，最后通过探索性注意力权重分析和贡献讨论回到理论，回答RQ1和RQ2。

## 研究开展程序

- study_or_phase_count：8

- 研究阶段总序列：全文不是简单的一个实验，而是从理论设计到制品构建再到多级评价的累积链条。第一阶段是设计理由构建：把顾客注意力理论化为过程-粒度框架并导出四个指标；第二阶段是制品构建：把指标翻译成DTV-AMI的注意力机制；第三至第六阶段是四组实证实验，依次回答端到端预测、表征质量、时间序列基准和集成价值；第七阶段用训练得到的注意力权重做探索性分析回馈RQ1；第八阶段用消融分析确认每个设计成分的贡献。

### studies_or_phases

#### 1. 设计理由构建：过程-粒度框架与四个顾客注意力指标

- order：1

- name_cn：设计理由构建：过程-粒度框架与四个顾客注意力指标

- question_cn：如何从顾客信息处理过程和多粒度浏览行为中，导出能指导销售预测设计的顾客注意力指标？

- inputs_and_setting_cn：理论输入：信息处理理论、信息学习理论、双加工理论、选择效应/差异化效应、精细加工可能性模型；没有实证数据。

- designed_or_compared_object_cn：过程-粒度框架、四个注意力指标及其与粒度层次的对应关系。

- baseline_control_or_counterfactual_cn：对照是现有基于内容的帮助性指标（如长度、情感、客观性），文章认为这些只覆盖yielding阶段而未覆盖reception阶段。

##### objective_metrics

（空）

- analysis_method_cn：理论演绎和概念分析，将已有行为/心理理论转化为内容无关的注意力维度。

- main_result_cn：提出四个注意力指标：时效性、语义多样性、投票意识、多模态交互的自适应注意力，并分别对应理论理由、方法论挑战和解决方案（Table 1）。

- argumentative_role_cn：建立整个设计科学论证的‘设计理由’，使后续制品不是工程启发式的堆砌，而是理论推导的结果。

- remaining_uncertainty_cn：这些理论指标是否真的能改善销售预测，以及如何用神经网络实现，尚未解决。

- link_to_next_phase_cn：每个指标对应一个方法论挑战，自然引出第四节DTV和AMI两种注意力机制。

##### evidence_pointers

1. Section 3 Figure 1

2. Section 3 Table 1

#### 2. 制品构建：DTV-AMI模型

- order：2

- name_cn：制品构建：DTV-AMI模型

- question_cn：怎样把四个顾客注意力指标转化为可训练的神经网络注意力机制？

- inputs_and_setting_cn：多模态评论序列：文本、图片、发布日期、投票数；预训练嵌入模型BERT和VGG-16；GRU作为基础序列模型。

- designed_or_compared_object_cn：DTV中的语义多样性注意力、时效性注意力、投票意识注意力，AMI中的自适应文本-图像交互注意力，以及双层序列padding mask和事后融合策略。

- baseline_control_or_counterfactual_cn：没有正式baseline，但隐含对照是现有亲和力式自注意力机制（相似度/点积兼容函数）。

##### objective_metrics

（空）

- analysis_method_cn：算法设计、公式推导和架构构建。

- main_result_cn：得到一个多模态深度学习方法DTV-AMI，能够运用L2范数逆匹配、指数时间衰减、指数投票项和自适应权重大小结合文本与图像。

- argumentative_role_cn：将理论指标落地为可检验的计算制品。

- remaining_uncertainty_cn：模型是否真正优于现有注意力与多模态融合方法，以及每个组件是否都被需要，尚未回答。

- link_to_next_phase_cn：第五节用四组实验对这一设计制品进行系统评价。

##### evidence_pointers

1. Section 4.1 Figure 2

2. Section 4.2–4.4 Equations (1)–(8)

#### 3. 实验1：端到端销售预测性能比较

- order：3

- name_cn：实验1：端到端销售预测性能比较

- question_cn：DTV-AMI在直接预测酒店月度入住率时，是否优于现有注意力增强GRU和多模态深度学习方法？

- inputs_and_setting_cn：2685家酒店，1252158条有效文本评论、197584张评论图片，三种时间窗（季度、半年、年），酒店-月为预测实例。

- designed_or_compared_object_cn：DTV-AMI-self和DTV-AMI-mh与GRU、MPL-self/mh、AC-self/mh、DIIA、CEN、MDL-CW、MCL进行比较；分别使用文本、图片和图文多模态三种输入。

- baseline_control_or_counterfactual_cn：GRU为基础；八个基准分别覆盖两种兼容函数乘自注意力/多头注意力，以及四种先进多模态融合方法。

##### objective_metrics

1. RMSE

2. MAE（正文见表2，MAE见在线附录E）

- analysis_method_cn：5次独立运行×10折交叉验证，共50个估计；Tukey-Kramer事后两两比较（在线附录G）。

- main_result_cn：DTV-AMI在所有时间窗和输入类型下均优于baseline和benchmarks，差异在0.001水平显著；半年窗口通常最好；图片评论与文本评论性能相当；多模态加上AMI后超过单一模态。

- argumentative_role_cn：提供核心技术水平证据：在端到端预测任务上，基于顾客注意力的注意力机制优于通用注意力和多模态融合方法。

- remaining_uncertainty_cn：性能提升可能只来自最终预测头，而不一定说明学到的表征更好。

- link_to_next_phase_cn：实验2直接检验表征学习性能，把不同方法学到的多模态表示送入下游预测模型。

##### evidence_pointers

1. Section 5.2 Experiment 1

2. Section 5.3.1 Table 2

#### 4. 实验2：多模态表征学习性能比较

- order：4

- name_cn：实验2：多模态表征学习性能比较

- question_cn：DTV-AMI学到的多模态评论表征是否能更好地支持下游预测模型？

- inputs_and_setting_cn：由DTV-AMI、baseline和基准方法产生的多模态表示特征，分别输入SVM、随机森林和XGBoost；用Lasso做特征选择。

- designed_or_compared_object_cn：表征来源：GRU、MPL-self/mh、AC-self/mh、DIIA、CEN、MDL-CW、MCL、DTV-AMI-self/mh；下游模型：SVM、RF、XGBoost。

- baseline_control_or_counterfactual_cn：同样以GRU和八个基准方法的表征作为对照。

##### objective_metrics

1. RMSE（MAE见附录E）

- analysis_method_cn：5次×10折CV；平均池化多步表示；Lasso特征选择；Tukey-Kramer事后比较。

- main_result_cn：DTV-AMI产生的表征在所有下游模型和所有时间窗内最好；SVM整体最佳；DTV的反向匹配兼容函数优于激活和乘法兼容函数。

- argumentative_role_cn：排除‘只是预测头更好’的替代解释，说明DTV-AMI确实提升多模态表示质量；同时突出语义多样性注意力的作用。

- remaining_uncertainty_cn：评论表征预测虽好，但传统历史销售时间序列在表4中更强，说明需要检验评论信息的增量价值。

- link_to_next_phase_cn：实验3先给出历史销售时间序列的基准表现，作为实验4集成模型的下界参照。

##### evidence_pointers

1. Section 5.2 Experiment 2

2. Section 5.3.2 Table 3

#### 5. 实验3：基于历史销售时间序列的预测

- order：5

- name_cn：实验3：基于历史销售时间序列的预测

- question_cn：不利用评论，仅用历史销售时间序列预测入住率能达到什么水平？

- inputs_and_setting_cn：酒店历史月度入住率，按季度、半年、年三个时间跨度构造时间序列。

- designed_or_compared_object_cn：GRU与ARIMA两种时间序列模型。

- baseline_control_or_counterfactual_cn：没有额外baseline；这是传统销售预测的强参照。

##### objective_metrics

1. RMSE

- analysis_method_cn：与实验1/2相同的CV协议。

- main_result_cn：年窗口ARIMA取得最佳7.04% RMSE，优于仅用评论的预测结果。

- argumentative_role_cn：证明历史销售是强有力的传统特征，为使评论价值可比较提供基准。

- remaining_uncertainty_cn：历史销售忽略了市场需求波动和顾客需求信息，评论能否补充它尚待验证。

- link_to_next_phase_cn：实验4将历史销售表征、评论表征和月份指标整合。

##### evidence_pointers

1. Section 5.2 Experiment 3

2. Section 5.3.3 Table 4

#### 6. 实验4：集成特征预测

- order：6

- name_cn：实验4：集成特征预测

- question_cn：将DTV-AMI的评论表征与历史销售时间序列、月份指标整合后，能否进一步改善销售预测？

- inputs_and_setting_cn：整合特征集：GRU历史销售隐特征、DTV-AMI或基准方法的多模态评论表征、月份指标。

- designed_or_compared_object_cn：与使用不同评论表征来源的集成模型比较；下游模型SVM、RF、XGBoost。

- baseline_control_or_counterfactual_cn：不用评论的纯历史销售模型（实验3）和仅用评论表征的模型（实验2）作为对照。

##### objective_metrics

1. RMSE

- analysis_method_cn：5次×10折CV；XGBoost/SVM/RF。

- main_result_cn：最佳模型为半年窗口、DTV-AMI-mh表征+XGBoost，RMSE 5.32%，比ARIMA最佳结果改进24.4%，比单独评论表征最佳结果改进18.5%。

- argumentative_role_cn：证明评论在传统特征之上增加显著价值，同时说明DTV-AMI的评论表征在这一集成中依然优于其他方法。

- remaining_uncertainty_cn：整体预测性能好，但仍不清楚四个注意力成分各自的贡献。

- link_to_next_phase_cn：第五节后半部分用探索性分析和消融分析来回答RQ1并归因RQ2的设计成分。

##### evidence_pointers

1. Section 5.2 Experiment 4

2. Section 5.3.4 Table 5

#### 7. 探索性分析：检验注意力机制是否符合顾客注意力

- order：7

- name_cn：探索性分析：检验注意力机制是否符合顾客注意力

- question_cn：训练好的DTV-AMI中，各注意力机制的权重变化是否显示顾客确实更关注及时、多样、被投票和图文权重交替的评论？

- inputs_and_setting_cn：训练集上DTV-AMI的注意力权重，按时间序、冗余度/多样性、投票数排序，以及各时间步的ξ值。

- designed_or_compared_object_cn：DTV-AMI设计的注意力权重 vs 自注意力权重；不同时间窗。

- baseline_control_or_counterfactual_cn：自注意力作为对照。

##### objective_metrics

1. 注意力权重分布

2. ξ值的时间步变化

- analysis_method_cn：将训练集权重平均、排序、可视化。

- main_result_cn：权重倾向于高时效、低冗余、高投票评论；ξ随时间步明显变化，文本和图像交替主导。

- argumentative_role_cn：把预测性能优势与理论机制连接起来，为RQ1提供证据，说明模型学到的注意力与理论上的顾客注意力一致。

- remaining_uncertainty_cn：模型权重只能作为顾客注意力的代理，不是直接观测到的顾客行为。

- link_to_next_phase_cn：还需要消融分析确认每个机制对预测都有贡献，而不只是权重可视化好看。

##### evidence_pointers

1. Section 5.4 Figures 4–7

#### 8. 消融与稳健性/补充分析

- order：8

- name_cn：消融与稳健性/补充分析

- question_cn：四个注意力成分中，每个成分对预测性能的边际贡献是什么？

- inputs_and_setting_cn：DTV-AMI-mh用于多模态评论；四个变体TV-AMI、DV-AMI、DT-AMI、DTV分别移除语义多样性、时效性、投票意识、AMI。

- designed_or_compared_object_cn：完整DTV-AMI vs 四个去除单一成分的变体。

- baseline_control_or_counterfactual_cn：完整模型为对照，每次移除一个成分。

##### objective_metrics

1. RMSE（正文说明结果见在线附录I）

- analysis_method_cn：消融比较；结合Tukey-Kramer和在线附录中的补充分析。

- main_result_cn：作者报告各成分移除后性能下降，具体数值在Online Appendix I；四个部件均有贡献。

- argumentative_role_cn：将性能优势归因于顾客注意力指标对应的具体设计，而不是整体模型复杂度。

- remaining_uncertainty_cn：没有在正文展示消融数值；泛化性仍需其他领域验证；注意力指标参数需按领域调节。

- link_to_next_phase_cn：贡献与局限性部分据此概括可复用设计知识和未来方向。

##### evidence_pointers

1. Section 5.5

2. Online Appendix I

## 各部分修辞架构

### abstract_moves

1. CONTEXT: 评论帮助性已被广泛研究，但通常用评论层面的量化指标测量。

2. LIMITATION: 简单帮助性指标未必带来准确销售预测。

3. MECHANISM: 更高顾客注意力的评论对购买意向和销量更有影响力。

4. RQ_OR_OBJECTIVE: 从四个粒度层次概念化顾客注意力并导出四个指标。

5. DESIGN_FEATURE: 提出DTV-AMI，将指标嵌入神经网络注意力机制。

6. RESULT: 大型酒店数据集上预测和表征性能均超过基准方法。

### introduction_moves

1. CONTEXT: 在线评论是连接顾客与产品的重要信息渠道，且影响购买决策。

2. PRACTICAL_STAKES: 销售预测对零售商运营和业务价值重要。

3. LIMITATION: 加入所有评论会带来预测偏差，因为只有少数评论被真正感知。

4. LIMITATION: 已有评论销售预测常用量化方式处理非结构化评论，文本语义和图像信息利用不足。

5. MECHANISM: 顾客更可能受仔细阅读的评论影响，吸引大量注意力的评论预测力更强。

6. PHENOMENON: 面对海量评论，顾客不会逐一评估，而是只关注一个子集。

7. THEORY_INTRO: 信息处理理论和信息学习理论将评论处理分为reception和yielding两阶段。

8. RQ_OR_OBJECTIVE: 提出RQ1，不同粒度层次上顾客注意力指向何种评论。

9. THEORY_PROPOSITION: 用双加工理论、选择效应、帮助性投票和ELM分别推出四个注意力指标。

10. RQ_OR_OBJECTIVE: 提出RQ2，如何利用顾客注意力增强多模态评论销售预测。

11. STUDY_OVERVIEW: 预告DTV-AMI和酒店案例实验结果。

### theory_and_knowledge_moves

1. PRIOR_KNOWLEDGE: 文献综述回顾评论对销售的影响、帮助性研究、基于评论的销售预测和深度学习注意力机制。

2. LIMITATION: 现有帮助性研究集中在内容相关指标和yielding阶段，未充分捕捉reception阶段。

3. GAP: 非结构化文本和图像评论的预测能力未充分研究，现有模型无法区分评论。

4. GAP: 现有注意力兼容函数与顾客注意力指标不兼容。

5. WHY_GAP_MATTERS: 不解决这些方法要求，评论信息在销售预测中的价值难以发挥。

6. THEORY_INTRO: 引入过程-粒度框架、双加工理论、选择效应、ELM作为设计理由。

7. REQUIREMENT: 从每个理论推出一个设计指标和一个对应的方法论挑战。

8. METHOD_JUSTIFICATION: 采用设计科学范式，强调设计理由对制品贡献的重要性。

### artifact_design_moves

1. DESIGN_FEATURE: 用BERT和VGG-16提取文本/图像嵌入，用双GRU捕捉流式评论。

2. DESIGN_FEATURE: 双层序列padding mask处理单模态缺失和不等长实例。

3. DESIGN_FEATURE: 语义多样性注意力用L2范数逆匹配和冗余度调节。

4. DESIGN_FEATURE: 时效性注意力用指数衰减项和参数η。

5. DESIGN_FEATURE: 投票意识注意力用指数投票项和参数γ。

6. DESIGN_FEATURE: AMI在每个时间步用自适应权重ξ折中文本和图像。

7. MECHANISM: 事后融合所有时间步预测，契合顾客陆续到达和任意评论作为起点的浏览行为。

### evaluation_moves

1. STUDY_OVERVIEW: 预告四组实验。

2. BENCHMARK_OR_CONTRAST: 选取GRU、两种兼容函数×自注意力/多头注意力、四种多模态深度学习方法作为基准。

3. METHOD_JUSTIFICATION: 用RMSE和MAE，5次×10折CV。

4. RESULT: 表2显示预测性能全面领先。

5. RESULT: 表3显示表征学习性能全面领先。

6. RESULT: 表4显示历史销售时间序列更强。

7. TRANSITION: 历史销售虽强但忽略顾客需求，因此需要集成。

8. RESULT: 表5显示集成后效果最佳。

9. MECHANISM: 探索性分析用注意力权重回答RQ1。

10. ROBUSTNESS_OR_BOUNDARY_TEST: 消融分析分离每个成分贡献。

### discussion_and_contribution_moves

1. CONTRIBUTION: 概念化顾客注意力并扩展到多粒度层次。

2. CONTRIBUTION: 提出DTV-AMI作为设计科学制品。

3. CONTRIBUTION: 通过大规模案例提供关于注意力如何变化的经验知识。

4. BOUNDARY_CONDITION: 方法需要足够的评论跨度、投票和多模态评论。

5. LIMITATION_AND_FUTURE: 未纳入竞争者评论。

6. BOUNDARY_CONDITION: 参数λ、η、γ、ξ需按领域调整。

7. LIMITATION_AND_FUTURE: 固定词级嵌入，未来可探索词级和图像区域级注意力。

## 理论/知识到设计的翻译

### 知识/理论基础

1. 信息学习理论（Riley 1954）和信息处理理论（McGuire 1968）

2. 双加工理论（Groves and Thompson 1970）

3. 选择效应/差异化效应（Li and Hitt 2008; Moe and Schweidel 2012）

4. 精细加工可能性模型ELM（Petty and Cacioppo 1986）

5. 评论帮助性文献（Mudambi and Schuff 2010; Kuan et al. 2015）

6. 神经网络注意力机制与全连接兼容函数文献（Vaswani et al. 2017）

7. 多模态评论与图像价值文献（Ma et al. 2018; Li and Xie 2020）

- 理论—设计耦合：direct

- 耦合判定理由：四个顾客注意力指标都是直接从理论推导而来，再被翻译成四个神经网络注意力机制；每个机制都在实验和消融中被直接检验，因此是前瞻性理论到设计的直接耦合。

- 理论到设计翻译链：信息处理/信息学习理论先划分reception和yielding两阶段，确定研究应关注reception阶段的内容无关注意力；过程-粒度框架把reception阶段的注意力划分为集合、子集、单条评论、元素四层；随后每个粒度用相应理论导出指标：集合层用双加工理论推出时效性，子集层用选择效应推出语义多样性，单条评论层用帮助性文献推出投票意识，元素层用ELM推出文本-图像自适应交互；每个指标再转化为DTV和AMI中的具体注意力操作。

### mapping_table

#### 1. 1

- theory_or_knowledge_claim_cn：双加工理论认为顾客决策由快速自动过程和慢速审慎过程共同完成，过时评论更可能被自动过程处理，最新评论更受关注。

- mechanism_cn：评论的效用随时间衰减，顾客更关注新评论。

- design_requirement_cn：预测模型应对更近的评论赋予更大权重，并允许每个评论位置都作为潜在起点。

- artifact_choice_cn：在注意力权重中加入基于发布时间的指数衰减项exp(Δt_j/Δt_max)，并用参数η调节。

- evaluated_contrast_cn：DTV-AMI vs GRU/其他注意力基准；探索性分析中时效性注意力权重 vs 自注意力权重；消融中移除时效性（DV-AMI）。

- objective_result_cn：DTV-AMI预测性能领先；训练权重显示越新评论权重越高，出现长尾效应。

##### evidence_pointers

1. Section 4.4.2 Equation (6)

2. Figure 4

3. Table 2

4. Online Appendix I

#### 2. 2

- theory_or_knowledge_claim_cn：选择效应和差异化效应表明顾客偏好异质，会关注在语义上互补、非冗余的评论集。

- mechanism_cn：顾客从同类评论中看到的是冗余信息，而语义多样的评论共同提供全面评估。

- design_requirement_cn：注意力应突出与目标query互补、且彼此不冗余的评论，而不仅仅是与query高度相关的评论。

- artifact_choice_cn：用L2范数逆匹配兼容函数和平均冗余度r_j构造语义多样性注意力。

- evaluated_contrast_cn：DTV vs 缩放乘性/激活兼容函数；探索性中多样性权重 vs 自注意力；消融中移除语义多样性（TV-AMI）。

- objective_result_cn：DTV-AMI在表2和表3中优于基于亲和力的注意力；权重视觉化显示低冗余评论获得更高权重。

##### evidence_pointers

1. Section 4.4.1 Equations (4)–(5)

2. Figure 5

3. Tables 2–3

4. Online Appendix I

#### 3. 3

- theory_or_knowledge_claim_cn：帮助性投票是最普遍的单条评论帮助性信号，被投票的评论会吸引更多顾客注意力并在yielding阶段更有说服力。

- mechanism_cn：顾客看到投票数高时更愿意注意和采纳该评论。

- design_requirement_cn：注意力应给投票更多的评论更高权重，并且允许投票与时效相互作用。

- artifact_choice_cn：在注意力权重中增加指数项γexp(s_j/s_max)。

- evaluated_contrast_cn：DTV vs 自注意力；探索性中投票意识权重 vs 自注意力；消融中移除投票意识（DT-AMI）。

- objective_result_cn：预测性能领先；训练权重显示投票数越高权重越高。

##### evidence_pointers

1. Section 4.4.3 Equation (7)

2. Figure 6

3. Table 2

4. Online Appendix I

#### 4. 4

- theory_or_knowledge_claim_cn：精细加工可能性模型认为顾客可能走中央或边缘路线处理评论，文本和图像在不同评论中的相对重要性不同。

- mechanism_cn：文本和图像之间存在替代或互补效应，顾客对文本和图像的偏好因评论而异。

- design_requirement_cn：在每个评论点应根据该评论内容对文本和图像权重做自适应折中，且折中权重随评论变化。

- artifact_choice_cn：AMI在每个时间步引入自适应权重ξ_i，用ξ_i z_text + (1−ξ_i) z_image融合。

- evaluated_contrast_cn：DTV-AMI vs 其他多模态融合方法；探索性中ξ的时间步波动；消融中移除AMI（DTV）。

- objective_result_cn：多模态评论预测优于单一模态；ξ随时间步明显变化，文本和图像交替主导。

##### evidence_pointers

1. Section 4.4.4 Equation (8)

2. Figure 7

3. Tables 2–3

4. Online Appendix I

## 评价逻辑

### evaluation_modes

1. 端到端预测性能比较：与GRU、标准注意力GRU、先进多模态深度学习方法比较。

2. 多模态表征学习性能比较：将不同方法的表征输入SVM、随机森林、XGBoost。

3. 传统时间序列基准：GRU和ARIMA基于历史销售。

4. 集成特征预测：历史销售表征+评论表征+月份指标。

5. 探索性注意力权重可视化：检查四个注意力机制是否符合顾客注意力。

6. 消融分析：移除四个成分的变体比较。

7. 稳健性补充：5次×10折CV、Tukey-Kramer事后检验、MAE和在线附录中的额外分析。

- why_these_evaluations_cn：单一预测对比不足以说明STV-AMI的价值，因为可能只是最终预测头更好，也可能只是增加模型复杂度。于是第二组实验单独检验表征；第三组实验提供传统强基准，证明评论在历史销售之外的增量价值；第四组实验模拟实际预测场景，把评论特征与传统特征结合；探索性分析把预测优势与理论机制联系起来；消融分析把优势归因到具体设计成分。

- benchmark_and_contrast_chain_cn：基准链从基础GRU开始，加入两种注意力兼容函数与自注意力/多头注意力组合，再加入四种多模态融合方法；这同一个benchmark集合在实验1、2、4中反复使用，形成累积比较。实验3引入ARIMA/GRU历史销售时间序列作为更强的应用基准；实验4又把实验2和实验3的特征放在同一集成框架下比较。探索性分析用自注意力作为对照，消融分析用完整模型作为对照。

### claim_evidence_ledger

#### 1. DTV-AMI在端到端销售预测中优于现有注意力与多模态方法。

- claim_cn：DTV-AMI在端到端销售预测中优于现有注意力与多模态方法。

- evidence_cn：表2中所有时间窗和输入类型下RMSE最低，Tukey-Kramer事后检验在0.001水平显著。

- status_cn：有直接证据

#### 2. DTV-AMI学到的多模态表征更有效。

- claim_cn：DTV-AMI学到的多模态表征更有效。

- evidence_cn：表3中三种下游模型全部取得最低RMSE。

- status_cn：有直接证据

#### 3. 多模态评论在历史销售之外有增量价值。

- claim_cn：多模态评论在历史销售之外有增量价值。

- evidence_cn：表5中最优集成模型比表4最优ARIMA改进24.4%，比表3评论特征单独最优改进18.5%。

- status_cn：有直接证据

#### 4. 四个注意力机制确实模仿顾客注意力。

- claim_cn：四个注意力机制确实模仿顾客注意力。

- evidence_cn：图4–7显示权重更关注时效、多样、投票评论，且ξ随时间步变化。

- status_cn：间接证据；模型权重是顾客注意力的代理，不是直接观测

#### 5. 每个设计成分都有贡献。

- claim_cn：每个设计成分都有贡献。

- evidence_cn：消融分析移除每个成分后性能下降（作者陈述，具体在Online Appendix I）。

- status_cn：依赖附录，正文未展示数值

#### 6. 方法具有普适性。

- claim_cn：方法具有普适性。

- evidence_cn：仅在酒店行业验证；作者在贡献和局限中承认需扩展。

- status_cn：未检验，属于边界主张

- internal_validity_strategy_cn：使用固定预处理流程、五种随机初始化×10折交叉验证、重复50次估计、统一RMSE/MAE指标、用Lasso控制高维特征、在同一数据与架构下比较不同注意力机制、用消融分离组件、用探索性权重确认识别模式，以降低随机性和成分混淆。

- external_validity_strategy_cn：采用真实酒店集团的大规模多模态数据，包含不同时间窗口、不同下游模型、文本/图片/多模态三种输入，以及历史销售集成场景；通过多个域内设置展示稳健性，并在局限中承认需要跨领域验证。

- what_is_not_actually_tested_cn：顾客注意力没有被直接测量（没有点击、眼动或调查），模型注意力权重只是代理；没有检验竞争酒店评论的影响；没有在酒店行业之外验证；没有直接因果识别评论对销售的因果效应；消融具体数值只在在线附录，未完全纳入正文论证。

## 贡献闭环

- technical_claim_cn：DTV-AMI在月入住率预测的RMSE和MAE上显著优于GRU、标准注意力GRU和四种多模态深度学习方法，并产生更适合下游模型的多模态表征。

- artifact_claim_cn：四个针对顾客注意力指标设计的注意力机制（语义多样性、时效性、投票意识、多模态交互自适应）共同构成性能优势，消融分析支持每个组件的贡献。

- mechanism_claim_cn：注意力权重模式显示模型更关注及时、语义多样、被投票的评论，并在不同评论上动态调节文本与图像权重，这与理论上的顾客注意力一致。

- boundary_claim_cn：方法需要足够的评论跨度、评论中应有投票信息、需要一定数量的图文评论；λ、η、γ、ξ等参数需要按领域调整；目前仅在酒店行业验证。

- reusable_design_knowledge_cn：过程-粒度框架可作为设计神经网络注意力机制的结构化方法；内容无关的reception阶段注意力应先于内容相关帮助性指标；时间衰减、非冗余互补、投票加权、自适应模态折中是四个可迁移的注意力设计原则。

- theoretical_contribution_cn：把评论帮助性研究从单条评论的量化指标扩展到多粒度层次的顾客注意力；用信息处理理论区分reception和yielding，指出现有内容指标只覆盖yielding，为评论影响力研究补充了接收阶段的机制；同时为多模态图文交互提供了模型层面的证据。

- how_discussion_closes_intro_gap_cn：讨论部分直接回到开头的“帮助性评论未必最影响购买决策”缺口，主张只有吸引顾客注意力的评论才更有预测力；四个指标的提出和DTV-AMI的验证共同回应了RQ1和RQ2，并把性能结果升华为概念化和设计科学贡献。

- overclaim_or_unsupported_leaps_cn：从模型注意力权重推论“顾客真实注意力”存在跳跃；作者自己假设‘更好的预测结果可以关联更多底层顾客注意力’，这是理论层面的推断而非直接证据；贡献部分说‘扩大帮助性到多个粒度’较抽象；消融数值仅指向在线附录，正文没有给出具体下降幅度，因此‘每个组件都有贡献’的证据强度有限。

## 句级写作动作图谱

### 1. P1 S1–S2

- order：1

- section：Abstract

- locator：P1 S1–S2

- move_code：CONTEXT

- paraphrase_cn：评论帮助性已被广泛研究，但通常用评论层面的量化指标测量；这类简单指标可能无法保证准确的销售预测。

- rhetorical_function_cn：在摘要开头建立领域共识，并立刻指出共识的局限。

- depends_on_cn：无；独立定位。

- sets_up_cn：为‘顾客注意力’替代‘简单帮助性指标’铺路。

- evidence_pointer：Abstract P1 S1–S2

### 2. P2 S1–S2

- order：2

- section：Abstract

- locator：P2 S1–S2

- move_code：RQ_OR_OBJECTIVE

- paraphrase_cn：假设高顾客注意力的评论对购买意图和销售更有影响，从四个粒度层次概念化注意力并导出四个指标，提出DTV-AMI方法。

- rhetorical_function_cn：在摘要中压缩了理论到设计再到评价的全文主线。

- depends_on_cn：依赖前面帮助性指标不足的判断。

- sets_up_cn：预告文章的方法、概念框架和实证结论。

- evidence_pointer：Abstract P2 S1–S2

### 3. P1 S1–S3

- order：3

- section：Introduction

- locator：P1 S1–S3

- move_code：CONTEXT

- paraphrase_cn：在线评论是连接顾客与产品的重要信息渠道，影响购买意向，也具备揭示未来销售的潜力。

- rhetorical_function_cn：建立研究背景和现实重要性。

- depends_on_cn：无。

- sets_up_cn：提出销售预测问题，并说明评论是新的预测视角。

- evidence_pointer：Section 1 P1 S1–S3

### 4. P2 S1

- order：4

- section：Introduction

- locator：P2 S1

- move_code：LIMITATION

- paraphrase_cn：直接把产品所有评论文本和量化指标塞进预测模型会引入预测偏差，因为顾客往往只感知和消化少量评论。

- rhetorical_function_cn：指出‘用全部评论’这一朴素做法的根本缺陷。

- depends_on_cn：建立在评论影响销售这一文献共识上。

- sets_up_cn：引出卖家注意力作为更合理的过滤机制。

- evidence_pointer：Section 1 P2 S1

### 5. P2 S2–S3

- order：5

- section：Introduction

- locator：P2 S2–S3

- move_code：LIMITATION

- paraphrase_cn：已有评论销售预测工作常用量化方式处理文本，文本语义和图像信息价值未被充分利用，模型也没有对原评论做有效区分。

- rhetorical_function_cn：明确研究缺口的两方面：数据模态和模型区分度。

- depends_on_cn：对已有文献的简短回顾。

- sets_up_cn：为RQ2需要新方法提供理由。

- evidence_pointer：Section 1 P2 S2–S3

### 6. P3 S1–S2

- order：6

- section：Introduction

- locator：P3 S1–S2

- move_code：MECHANISM

- paraphrase_cn：销售来自购买意向，购买意向又受顾客仔细阅读的评论影响；因此被顾客充分注意的评论应更有预测力。

- rhetorical_function_cn：提出全文核心机制：顾客注意力中介评论对销售的影响。

- depends_on_cn：依赖评论影响购买决策的文献和有限注意力的常识。

- sets_up_cn：引出研究哪种评论吸引关注，并奠定RQ1。

- evidence_pointer：Section 1 P3 S1–S2

### 7. P4 S1–S2

- order：7

- section：Introduction

- locator：P4 S1–S2

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：文献用信息质量、论证质量和帮助性衡量评论价值，通常认为帮助性高的评论更影响购买意向，但内容式帮助性指标不能稳定代表群体购买意向，因为顾客偏好异质。

- rhetorical_function_cn：总结帮助性研究并制造‘共识内部有冲突’的张力。

- depends_on_cn：引用Filieri、Yin、Moe等的实证结果。

- sets_up_cn：为内容无关的顾客注意力指标腾出空间。

- evidence_pointer：Section 1 P4 S1–S2

### 8. P5 S1–S2

- order：8

- section：Introduction

- locator：P5 S1–S2

- move_code：THEORY_INTRO

- paraphrase_cn：依据信息学习和信息处理理论，顾客处理评论分reception和yielding两个阶段；现有内容式帮助性指标只覆盖yielding阶段，没有捕捉顾客在reception阶段的初步注意。

- rhetorical_function_cn：引入理论区分，并把文章的研究视角从yielding转向reception。

- depends_on_cn：依赖Riley、McGuire和Kuan等的理论线索。

- sets_up_cn：为过程-粒度框架提供过程维度的理论基础。

- evidence_pointer：Section 1 P5 S1–S2

### 9. P6 S1–S2

- order：9

- section：Introduction

- locator：P6 S1–S2

- move_code：PHENOMENON

- paraphrase_cn：顾客浏览评论会沿自上而下或自下而上的路径，从整体评论集合钻取到评论元素；由此可以把注意力分为集合、子集、单条评论、元素四个粒度。

- rhetorical_function_cn：引入过程-粒度框架的空间维度，解释四种粒度从何而来。

- depends_on_cn：依赖前面对浏览行为的经验观察。

- sets_up_cn：直接引出RQ1。

- evidence_pointer：Section 1 P6 S1–S2

### 10. P6 S3

- order：10

- section：Introduction

- locator：P6 S3

- move_code：RQ_OR_OBJECTIVE

- paraphrase_cn：提出RQ1：在购买决策过程中，不同粒度层次上什么评论符合顾客注意力？

- rhetorical_function_cn：明确第一个研究问题。

- depends_on_cn：依赖过程-粒度框架。

- sets_up_cn：后面探索性分析回答RQ1。

- evidence_pointer：Section 1 P6 S3

### 11. P7 S1–S2

- order：11

- section：Introduction

- locator：P7 S1–S2

- move_code：THEORY_PROPOSITION

- paraphrase_cn：分别在四个粒度上，用双加工理论、选择效应、帮助性投票和ELM提出时效性、语义多样性、投票意识和图文交互四类注意力。

- rhetorical_function_cn：用多个理论支撑四个指标，建立理论到设计的桥梁。

- depends_on_cn：依赖Section 3详细理论展开。

- sets_up_cn：为DTV-AMI的设计特征提供预期。

- evidence_pointer：Section 1 P7 S1–S2

### 12. P7 S3

- order：12

- section：Introduction

- locator：P7 S3

- move_code：RQ_OR_OBJECTIVE

- paraphrase_cn：提出RQ2：如何利用顾客注意力提升多模态评论销售预测的效果？

- rhetorical_function_cn：给出第二个研究问题，与RQ1形成‘是什么’和‘怎么做’的互补。

- depends_on_cn：依赖四个指标的提出。

- sets_up_cn：引出DTV-AMI。

- evidence_pointer：Section 1 P7 S3

### 13. P8 S1–S2

- order：13

- section：Introduction

- locator：P8 S1–S2

- move_code：DESIGN_FEATURE

- paraphrase_cn：介绍DTV-AMI：DTV包含语义多样性、时效性和投票意识注意力，AMI自适应处理图文交互；模型递归地把每条评论作为潜在起点，并动态提升及时、多样、被投票评论的权重。

- rhetorical_function_cn：在引言中预告制品的两个核心组件及其与顾客注意力指标的对应关系。

- depends_on_cn：依赖RQ2和四个指标。

- sets_up_cn：为第四节详细算法做摘要式预览。

- evidence_pointer：Section 1 P8 S1–S2

### 14. P9 S1

- order：14

- section：Introduction

- locator：P9 S1

- move_code：STUDY_OVERVIEW

- paraphrase_cn：预告案例研究结果：2685家酒店、125万条文本和19.7万张图像的实验显示DTV-AMI优于基准深度学习方法。

- rhetorical_function_cn：给出结果预告，增加文章吸引力和方向感。

- depends_on_cn：依赖DTV-AMI的设计。

- sets_up_cn：为第五节实证结果设置期待。

- evidence_pointer：Section 1 P9 S1

### 15. P1–P4

- order：15

- section：Literature Review 2.1

- locator：P1–P4

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：文献综述回顾评论如何通过帮助性影响销售，文本评论、图像评论和混合评论分别提供信息与诊断价值。

- rhetorical_function_cn：建立已有知识基础，同时暴露现有工作对图像和深层语义利用不足。

- depends_on_cn：引用大范围实证文献。

- sets_up_cn：为Research Gaps提供依据。

- evidence_pointer：Section 2.1 P1–P4

### 16. P1–P3

- order：16

- section：Literature Review 2.2

- locator：P1–P3

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：已有基于评论的销售预测主要使用文本情感、量化指标和时间序列方法，虽然取得进展，但多模态图像信息基本未进入预测模型。

- rhetorical_function_cn：总结预测方法现状，突出模态缺口。

- depends_on_cn：引用Yu、Archak、van Nguyen等。

- sets_up_cn：使‘多模态评论销售预测仍开放’成为合理缺口。

- evidence_pointer：Section 2.2 P1–P3

### 17. P1–P2

- order：17

- section：Literature Review 2.3

- locator：P1–P2

- move_code：THEORY_INTRO

- paraphrase_cn：注意力机制是神经网络的重要组件，能让模型搜索与任务相关的输入，并带来可解释性优势。

- rhetorical_function_cn：引入深度学习中的注意力机制作为实现工具。

- depends_on_cn：依赖Vaswani、Bahdanau、Xu等。

- sets_up_cn：说明为什么用神经注意力机制实现顾客注意力。

- evidence_pointer：Section 2.3 P1–P2

### 18. P1–P3

- order：18

- section：Literature Review 2.4

- locator：P1–P3

- move_code：GAP

- paraphrase_cn：指出三类缺口：多模态评论预测未充分研究、现有预测方法不能有效区分评论、现有注意力兼容函数与顾客注意力指标不兼容。

- rhetorical_function_cn：集中陈述研究方法缺口，把文献回顾导向本文设计。

- depends_on_cn：依赖前三小节的文献回顾。

- sets_up_cn：为DTV-AMI的贡献定位。

- evidence_pointer：Section 2.4 P1–P3

### 19. P3 S3

- order：19

- section：Literature Review 2.4

- locator：P3 S3

- move_code：WHY_GAP_MATTERS

- paraphrase_cn：语义多样性要求非冗余键，时效性和投票意识要求关注及时被投票的键，自适应图文交互要求动态权衡文本图像；解决这些要求就是DTV-AMI的贡献。

- rhetorical_function_cn：把抽象缺口具体化为可工程化的要求，并预告贡献。

- depends_on_cn：依赖前面对现有兼容函数的批评。

- sets_up_cn：为第四节设计机制设置清单。

- evidence_pointer：Section 2.4 P3 S3

### 20. P1

- order：20

- section：Section 3 Design Rationales

- locator：P1

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：本研究属于设计科学范式，设计理由对制品贡献至关重要；四个顾客注意力指标构成注意力机制的设计理由。

- rhetorical_function_cn：明确研究范式，并为后续理论推导提供合法性。

- depends_on_cn：依赖Gregor和Hevner的设计科学框架。

- sets_up_cn：引出过程-粒度框架作为设计理由的来源。

- evidence_pointer：Section 3 P1

### 21. P2

- order：21

- section：Section 3 Design Rationales

- locator：P2

- move_code：THEORY_PROPOSITION

- paraphrase_cn：顾客处理评论分两个阶段：reception阶段决定注意哪些评论，yielding阶段评估是否接受；reception阶段的注意力是释放有影响力评论预测价值的基础。

- rhetorical_function_cn：确立过程维度的核心理论主张。

- depends_on_cn：依赖Riley、McGuire的信息处理理论。

- sets_up_cn：为内容无关指标选择提供理论依据。

- evidence_pointer：Section 3 P2

### 22. P3

- order：22

- section：Section 3 Design Rationales

- locator：P3

- move_code：MECHANISM

- paraphrase_cn：从整体评论集合到最近评论子集、主题子集、单条评论和元素，顾客的浏览路径逐层下钻；这些步骤发生具体内容被仔细阅读之前，因此吸引的是内容无关的注意力。

- rhetorical_function_cn：用平台交互场景解释为什么四个粒度都是内容无关的。

- depends_on_cn：依赖产品页面展示逻辑和浏览行为。

- sets_up_cn：为每个粒度指标提供经验基础。

- evidence_pointer：Section 3 P3 and Figure 1

### 23. Paragraph starting 'The timeliness attention of customers...'

- order：23

- section：Section 3 Timeliness Attention

- locator：Paragraph starting 'The timeliness attention of customers...'

- move_code：REQUIREMENT

- paraphrase_cn：顾客不总从最新评论开始，每条评论都可能成为起点，因此需要全局注意力；同时时效性意味着时间衰减效应，需要按时间序加权。

- rhetorical_function_cn：把双加工理论转化为具体设计需求。

- depends_on_cn：依赖双加工理论命题。

- sets_up_cn：为4.4.2时效性注意力的公式设计提供理由。

- evidence_pointer：Section 3 Timeliness paragraph

### 24. Paragraph starting 'The semantic diversity attention of customers...'

- order：24

- section：Section 3 Semantic Diversity Attention

- locator：Paragraph starting 'The semantic diversity attention of customers...'

- move_code：REQUIREMENT

- paraphrase_cn：现有亲和力式兼容函数会让模型关注彼此相关的评论，导致语义冗余；语义多样性注意力要求模型关注与query互补、彼此不冗余的评论。

- rhetorical_function_cn：把选择效应转化为操作层面的‘反冗余注意力’需求。

- depends_on_cn：依赖选择效应/差异化效应。

- sets_up_cn：为4.4.1的L2逆匹配设计提供理由。

- evidence_pointer：Section 3 Semantic Diversity paragraph

### 25. Paragraph starting 'The voting awareness attention of customers...'

- order：25

- section：Section 3 Voting Awareness Attention

- locator：Paragraph starting 'The voting awareness attention of customers...'

- move_code：REQUIREMENT

- paraphrase_cn：投票数是最普遍的单条评论帮助性信号，投票意识的顾客注意力要求更多票的评论获得更高权重。

- rhetorical_function_cn：把帮助性文献转化为简单的权重要求。

- depends_on_cn：依赖Mudambi、Kuan等关于投票的结论。

- sets_up_cn：为4.4.3投票意识注意力提供理由。

- evidence_pointer：Section 3 Voting Awareness paragraph

### 26. Paragraph starting 'The varying attention for text-image interaction...'

- order：26

- section：Section 3 Varying Attention for Text-Image Interaction

- locator：Paragraph starting 'The varying attention for text-image interaction...'

- move_code：REQUIREMENT

- paraphrase_cn：文本和图像在不同评论中的相对重要性阈值会持续变化，因此需要跨评论自适应分配文本和图像权重。

- rhetorical_function_cn：把ELM和图文互补/替代效应转化为自适应融合需求。

- depends_on_cn：依赖ELM和图文交互文献。

- sets_up_cn：为4.4.4 AMI设计提供理由。

- evidence_pointer：Section 3 Text-Image paragraph

### 27. Table 1

- order：27

- section：Section 3 Table 1

- locator：Table 1

- move_code：REQUIREMENT

- paraphrase_cn：表格汇总四个注意力指标对应的理论根据、方法论挑战和解决方案。

- rhetorical_function_cn：把理论推导压缩为可阅读的对照表，便于读者快速把握设计理由。

- depends_on_cn：依赖前四个指标的详细论述。

- sets_up_cn：作为第四节方法设计的索引。

- evidence_pointer：Section 3 Table 1

### 28. P1–P2

- order：28

- section：Section 4.1 Overview

- locator：P1–P2

- move_code：DESIGN_FEATURE

- paraphrase_cn：DTV-AMI先用预训练网络提取多模态嵌入，再用两个并行GRU生成文本和图像序列表示，最后加入DTV和AMI机制。

- rhetorical_function_cn：给出模型整体架构的鸟瞰图。

- depends_on_cn：依赖前文四个指标。

- sets_up_cn：为后面的嵌入、padding和公式细节做铺垫。

- evidence_pointer：Section 4.1 Figure 2

### 29. P1–P2

- order：29

- section：Section 4.2 Data and Preprocessing

- locator：P1–P2

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：在案例研究中按酒店-月把前一段时间内的有效评论按时间排序形成评论序列；过滤短评论和不足十个评论的实例。

- rhetorical_function_cn：说明数据构造方式如何匹配流式评论预测任务。

- depends_on_cn：依赖酒店合作方提供的数据。

- sets_up_cn：为后面双层padding mask和嵌入提取定义输入格式。

- evidence_pointer：Section 4.2.1

### 30. P5

- order：30

- section：Section 4.2.2 Bilevel Sequence Padding Mask

- locator：P5

- move_code：DESIGN_FEATURE

- paraphrase_cn：在单条评论层处理纯文本或纯图片造成的模态缺失，在酒店-月层处理不等长序列。

- rhetorical_function_cn：解决多模态序列建模的两个实际工程难题。

- depends_on_cn：依赖标准padding mask技术。

- sets_up_cn：使文本和图像序列能在GRU中同步训练。

- evidence_pointer：Section 4.2.2

### 31. Equation (4)–(5) paragraph

- order：31

- section：Section 4.4.1 Semantic Diversity Attention

- locator：Equation (4)–(5) paragraph

- move_code：DESIGN_FEATURE

- paraphrase_cn：用键间的平均冗余度和L2范数逆匹配兼容函数，使候选键既与query互补又彼此不冗余时获得更大权重。

- rhetorical_function_cn：把语义多样性需求实现为具体的注意力公式。

- depends_on_cn：依赖L2距离和软最大化。

- sets_up_cn：为后续时效和投票权重的乘法调整提供基础。

- evidence_pointer：Section 4.4.1 Equations (4)–(5)

### 32. Equation (6) paragraph

- order：32

- section：Section 4.4.2 Timeliness Attention

- locator：Equation (6) paragraph

- move_code：DESIGN_FEATURE

- paraphrase_cn：在多样性权重上乘一个指数时间衰减项，使越新的评论权重越大，并随时间呈现衰减。

- rhetorical_function_cn：将时效性要求实现为指数衰减机制。

- depends_on_cn：依赖前一步多样性权重。

- sets_up_cn：为投票项加入提供结构。

- evidence_pointer：Section 4.4.2 Equation (6)

### 33. Equation (7) paragraph

- order：33

- section：Section 4.4.3 Voting Awareness Attention

- locator：Equation (7) paragraph

- move_code：DESIGN_FEATURE

- paraphrase_cn：在时间衰减项上增加指数投票项，使投票更多的评论获得更高注意力，并允许时效与投票交互。

- rhetorical_function_cn：将单条评论层面的投票意识引入注意力计算。

- depends_on_cn：依赖时效项结构。

- sets_up_cn：形成综合的DTV评分，再交给AMI融合模态。

- evidence_pointer：Section 4.4.3 Equation (7)

### 34. Equation (8) paragraph

- order：34

- section：Section 4.4.4 Adaptive AMI

- locator：Equation (8) paragraph

- move_code：DESIGN_FEATURE

- paraphrase_cn：在每个时间步使用自适应权重ξ_i折中文本和图像表示，并把各时间步的预测平均作为最终预测。

- rhetorical_function_cn：把顾客对图文的自适应注意力实现为参数化融合。

- depends_on_cn：依赖前一步DTV得到的文本和图像序列表示。

- sets_up_cn：为后续“事后融合优于事前融合”的解释提供依据。

- evidence_pointer：Section 4.4.4 Equation (8)

### 35. P1

- order：35

- section：Section 5.1 Data

- locator：P1

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：用于评价的数据来自2,685家酒店，125万条文本和19.7万张图片，预测目标是提前一个月的月度入住率。

- rhetorical_function_cn：给出数据集规模、预测目标和时间窗口，说明案例研究的实际基础。

- depends_on_cn：依赖第四节数据处理流程。

- sets_up_cn：为实验1–4提供可复现的数据描述。

- evidence_pointer：Section 5.1

### 36. P1–P2

- order：36

- section：Section 5.2 Main Experiments

- locator：P1–P2

- move_code：STUDY_OVERVIEW

- paraphrase_cn：预告四组实验：预测性能、表征学习、历史销售时间序列、集成特征预测；并说明使用RMSE和MAE、5次×10折CV的评估协议。

- rhetorical_function_cn：给实证部分提供清晰的路线图。

- depends_on_cn：依赖DTV-AMI模型和数据。

- sets_up_cn：使读者知道后面四个小节分别回答什么问题。

- evidence_pointer：Section 5.2 P1–P2

### 37. P3–P5

- order：37

- section：Section 5.2 Main Experiments

- locator：P3–P5

- move_code：BENCHMARK_OR_CONTRAST

- paraphrase_cn：构造九个对照：GRU、缩放乘性自/多头注意力、激活自/多头注意力、DIIA、CEN、MDL-CW、MCL，并规定多模态输入下的融合策略。

- rhetorical_function_cn：为实验建立系统而可比较的基准集。

- depends_on_cn：依赖文献中已有的注意力与多模态方法。

- sets_up_cn：让表2–5的比较结果具有可信度。

- evidence_pointer：Section 5.2 P3–P5

### 38. P1–P3

- order：38

- section：Section 5.3.1 Experiment 1

- locator：P1–P3

- move_code：RESULT

- paraphrase_cn：DTV-AMI在所有时间窗和所有输入类型下优于基线和八个基准，差异显著；多头注意力通常略优于自注意力；半年窗口通常最好；图片评论与文本评论性能相当，图文结合在AMI帮助下进一步改善。

- rhetorical_function_cn：报告第一组核心证据，并解释性能模式的可能机制。

- depends_on_cn：依赖表2数据。

- sets_up_cn：促使实验2检验表征质量。

- evidence_pointer：Section 5.3.1 Table 2

### 39. P1–P3

- order：39

- section：Section 5.3.2 Experiment 2

- locator：P1–P3

- move_code：RESULT

- paraphrase_cn：DTV-AMI生成的多模态表征在SVM、随机森林和XGBoost上均取得最低RMSE；逆匹配兼容函数优于激活和乘法函数。

- rhetorical_function_cn：证明DTV-AMI的表征质量而非仅预测头更好。

- depends_on_cn：依赖表3数据。

- sets_up_cn：支持‘语义多样性注意力对表征学习重要’的论断。

- evidence_pointer：Section 5.3.2 Table 3

### 40. P1

- order：40

- section：Section 5.3.3 Experiment 3

- locator：P1

- move_code：RESULT

- paraphrase_cn：历史销售时间序列最好结果（年窗口ARIMA约7.04%）超过仅用评论的预测，说明历史销售是必要基准。

- rhetorical_function_cn：引入传统强基线，避免读者误以为评论是唯一可用信息。

- depends_on_cn：依赖表4。

- sets_up_cn：引出实验4整合评论与历史销售。

- evidence_pointer：Section 5.3.3 Table 4

### 41. P1 last sentence

- order：41

- section：Section 5.3.3 Experiment 3

- locator：P1 last sentence

- move_code：TRANSITION

- paraphrase_cn：历史销售只靠时间序列依赖，忽略市场需求扰动，而评论直接反映顾客需求，因此需要把评论补充进去。

- rhetorical_function_cn：在实验3和实验4之间建立逻辑过渡。

- depends_on_cn：依赖表4结果。

- sets_up_cn：为实验4的集成特征设计提供理由。

- evidence_pointer：Section 5.3.3 P1 last sentence

### 42. P1

- order：42

- section：Section 5.3.4 Experiment 4

- locator：P1

- move_code：RESULT

- paraphrase_cn：集成历史销售表征、DTV-AMI评论表征和月份指标后，XGBoost在半年窗口达到5.32% RMSE，比ARIMA改进24.4%，比评论表征单独改进18.5%。

- rhetorical_function_cn：给出全文最重要的应用结果，说明评论和DTV-AMI的增量价值。

- depends_on_cn：依赖表5以及实验2、3的最佳值。

- sets_up_cn：为随后探索性分析和贡献总结提供事实基础。

- evidence_pointer：Section 5.3.4 Table 5

### 43. P1–P2

- order：43

- section：Section 5.4 Exploratory Analysis

- locator：P1–P2

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：训练后的注意力参数可以帮助理解顾客在不同粒度的注意力；将注意力权重按时间、多样性、投票排序并平均。

- rhetorical_function_cn：说明为什么要看注意力权重，并交代可视化方法。

- depends_on_cn：依赖训练好的DTV-AMI。

- sets_up_cn：为图4–7的证据做方法准备。

- evidence_pointer：Section 5.4 P1–P2

### 44. Figures 4–7 headings and text

- order：44

- section：Section 5.4.1–5.4.4

- locator：Figures 4–7 headings and text

- move_code：RESULT

- paraphrase_cn：四个探索性分析分别显示：模型给高时效、低冗余、高投票评论更高权重，且图文交互权重ξ随时间步明显变化。

- rhetorical_function_cn：把预测性能升华为对RQ1的实证回答。

- depends_on_cn：依赖图4–7。

- sets_up_cn：为贡献部分说‘加深对顾客注意力的理解’提供证据。

- evidence_pointer：Section 5.4.1–5.4.4 Figures 4–7

### 45. P1

- order：45

- section：Section 5.5 Ablation Analysis

- locator：P1

- move_code：ROBUSTNESS_OR_BOUNDARY_TEST

- paraphrase_cn：通过移除语义多样性、时效性、投票意识或AMI形成四个变体，检验每个机制的独立贡献。

- rhetorical_function_cn：把综合模型的性能优势归因到具体设计，排除整体复杂度解释。

- depends_on_cn：依赖完整DTV-AMI和表2结果。

- sets_up_cn：为贡献部分‘机制有效’提供证据。

- evidence_pointer：Section 5.5 and Online Appendix I

### 46. P1

- order：46

- section：Section 6 Contributions and Implications

- locator：P1

- move_code：CONTRIBUTION

- paraphrase_cn：贡献包括概念化顾客注意力、提出DTV-AMI方法、以及提供关于顾客注意力变化和图文交互的经验发现。

- rhetorical_function_cn：把全文结果归纳为理论、方法和实证三类贡献。

- depends_on_cn：依赖全部理论和实验结果。

- sets_up_cn：为结论和局限部分做铺垫。

- evidence_pointer：Section 6 P1

### 47. P2

- order：47

- section：Section 6 Practical Implications

- locator：P2

- move_code：BOUNDARY_CONDITION

- paraphrase_cn：方法在酒店行业评价，但可扩展到其他多模态评论场景，并为第三方评论平台提供评论高亮优化方案。

- rhetorical_function_cn：扩展制品的应用边界和实际价值。

- depends_on_cn：依赖DTV-AMI在大案例上的成功。

- sets_up_cn：为未来应用提供方向。

- evidence_pointer：Section 6 P2

### 48. P1–P2

- order：48

- section：Section 7 Conclusion

- locator：P1–P2

- move_code：LIMITATION_AND_FUTURE

- paraphrase_cn：局限包括：只在酒店验证、未纳入竞争者评论、指标参数需要按领域调整、固定嵌入无法获得词级和图像区域级注意力。

- rhetorical_function_cn：保护贡献不因过度泛化而被攻击，同时为未来研究留出空间。

- depends_on_cn：依赖对全文方法的反思。

- sets_up_cn：结束全文。

- evidence_pointer：Section 7 P1–P2

## 写作技术

- gap_construction_cn：先建立‘帮助性=评论价值’的文献共识，再用反例（负向评论双向效果、长度帮助性结论矛盾）削弱内容式帮助性指标的稳定性；随后用reception/yielding两阶段区分，指出内容指标只覆盖yielding；最后把技术缺口聚焦到现有注意力兼容函数与顾客注意力不兼容，使缺口从‘数据没用好’升级为‘设计哲学不对’。

- signposting_cn：在引言明确给出RQ1和RQ2；Section 3开头列出三个基本问题；Section 5.2明确预告四组实验；每个组件描述都以‘…guides our design…’方式重复指标到设计的关系；贡献部分用First/Second/Third列出。

- transition_logic_cn：从概念到方法的过渡靠‘每个指标产生一个方法论挑战’；从实验1到实验2靠‘是否只因为最终预测头更好’的疑问；从实验3到实验4靠‘历史销售虽强但忽视顾客需求’的论证；从主实验到探索性靠‘更好预测可关联更多顾客注意力’的假设；从探索性到消融靠‘权重模式是否真的来自每个机制’的检验需要。

- claim_evidence_rhythm_cn：每个注意力指标都按‘理论命题→机制→设计需求→公式→实验证据→消融/探索证据’的节奏展开；结果部分先报表，再解释模式，再给出机制解释；贡献部分不重复数字，而是把数字上升为概念和方法贡献。

- benchmark_narrative_cn：基准不是随机堆砌，而是从基础GRU、标准兼容函数×自/多头、多模态融合方法三个层次构造，并用同一基准集在实验1、2、4中反复出现；这让读者看到相同的对照在不同评价层次上都被DTV-AMI超越，形成累积说服力。

- theory_return_cn：实验1/2/4提供预测优势，探索性分析用训练权重把这种优势带回到理论构念（时效性、多样性、投票、图文交互），消融分析再把这些构念对应到具体机制，最后贡献部分声称深化了对顾客注意力的理解。

- contribution_positioning_cn：将论文同时定位为概念化贡献、设计科学制品贡献和经验贡献；用Online Appendix A和B的表格说明与相关研究的区别，避免与通用注意力/多模态学习文献混淆。

- novelty_protection_cn：通过在端点预测之外增加表征学习评价，说明不是预测头功劳；通过消融实验说明不是模型复杂度功劳；通过探索性权重说明不是纯黑箱性能；通过在线附录的补充分析和显著性检验说明不是单次随机结果。

## 可复用研究与写作程序

### structure_steps

#### 1. 1

- step：1

- writing_job_cn：建立领域问题与优先缺口：评论帮助性虽重要但不足以支持销售预测。

- research_job_cn：系统回顾评论、帮助性、销售预测、深度注意力文献。

- required_evidence_cn：需要若干篇显示帮助性指标与销售/行为关系不稳定的文献，以及现有预测方法未用图像/深层语义的证据。

- transition_to_next_cn：从‘内容指标不充分’过渡到‘需要捕捉顾客接收阶段注意力’。

#### 2. 2

- step：2

- writing_job_cn：构建过程-粒度框架，导出多个内容无关的注意力指标。

- research_job_cn：用行为和心理学理论（信息处理、双加工、选择效应、ELM）把注意力分解为不同粒度。

- required_evidence_cn：需要理论命题能转化为可操作化的设计需求；每个指标要有独立理论来源。

- transition_to_next_cn：每个指标的‘方法论挑战’直接对应一个神经网络设计任务。

#### 3. 3

- step：3

- writing_job_cn：写出模型设计和数学公式，展示指标如何嵌入注意力机制。

- research_job_cn：实现DTV和AMI，包括嵌入、padding、GRU、注意力兼容函数、融合方式。

- required_evidence_cn：需要模型代码和初步仿真确认机制可训练、无NaN/性能不崩溃。

- transition_to_next_cn：用‘设计科学’框架说明制品已按要求构建，转入评价。

#### 4. 4

- step：4

- writing_job_cn：报告评价数据、实验设置、基准和指标。

- research_job_cn：获得真实多模态评论数据和销售标签，构造酒店-月实例，清洗和预处理。

- required_evidence_cn：需要足够大的数据集、明确预测目标（入住率）、三个时间窗和可计算的RMSE/MAE。

- transition_to_next_cn：从数据设定进入多组对照实验。

#### 5. 5

- step：5

- writing_job_cn：执行并报告四层实验：端到端、表征、时序基线、集成。

- research_job_cn：对同一基准集做预测/表征/集成三级比较；加入历史销售基线。

- required_evidence_cn：需要5次×10折CV、统计显著性检验、三种下游模型、ARIMA/GRU基线和集成结果。

- transition_to_next_cn：用‘为什么性能更好’进入机制解释。

#### 6. 6

- step：6

- writing_job_cn：进行探索性注意力权重分析和消融分析。

- research_job_cn：从训练模型提取权重可视化；移除每个组件形成变体并比较。

- required_evidence_cn：需要注意力权重按理论维度排序时呈现预期模式；消融移除后性能下降。

- transition_to_next_cn：用这些证据把经验结果升华为理论贡献与设计原则。

#### 7. 7

- step：7

- writing_job_cn：在贡献与局限部分连接引言缺口，声明适用范围。

- research_job_cn：总结概念化、方法、机制和可持续应用边界。

- required_evidence_cn：需要明确哪些结果只在酒店领域获得、哪些是代理变量、哪些参数需调整。

- transition_to_next_cn：收束全文并列出未来方向。

### most_transferable_moves_cn

1. 用‘理论命题→设计需求→模型组件→证据’四步链组织每个设计元素。

2. 把研究问题分成RQ1（概念/机制）和RQ2（方法与工具）双轨。

3. 用一组固定基准在多层次实验中反复比较，形成累积证据。

4. 用传统强基准（历史销售）作为边界，再用集成实验展示增量价值。

5. 用训练后的注意力权重回答概念性问题，避免概念只停留在理论。

6. 用消融分析对应设计成分，防止‘整体性能好’被归因于复杂度。

### resource_intensive_or_nonstandard_parts_cn

1. 需要与合作酒店集团共处获得真实的月度入住率、多模态评论和投票信息；这种长期字段数据和高访问权限难以复制。

2. 数据规模要求高：125万评论文本、19.7万图片、2685家酒店，加上BERT/VGG-16嵌入和50次×10折CV，计算成本大。

3. 多模态数据需要同时有文本和图片，且评论需要有时间戳和投票数，否则时效和投票机制无法实现。

4. 在线附录中的表格和图片需要补充提供，正文只给出结果摘要。

### what_not_to_copy_superficially_cn

1. 不能只复制‘注意力机制+指数衰减+投票项’的公式，而不说明每个公式对应的理论指标和顾客行为机制，否则会沦为工程堆积。

2. 不能把训练模型产生的注意力权重直接等同于顾客注意力，必须有行为数据或至少承认代理性。

3. 不能在只有单一领域数据时就宣称通用，需要有跨领域验证或明确限定边界。

4. 不能把消融结果放在附录而不在正文解释，否则组件归因证据显得薄弱。

5. 不能把预测改进直接讲成理论贡献，需要像本文一样用探索性分析和概念化框架把它接回理论。

- single_best_description_of_the_routine_cn：先用‘过程-粒度框架’把顾客注意力拆成四个内容无关的指标，再把每个指标翻译成对应的神经网络注意力机制，最后用预测、表征、时序基准、集成、探索和消融六级证据证明‘指标和机制同时有效’。

## 分析边界

本文分析基于OCR全文，缺少在线附录A–I的具体表格和图片细节，尤其是消融分析结果正文只指向Online Appendix I，因此对消融效果的具体幅度和显著性只能依赖作者叙述；图1–3与图4–7等图片内容无法完整OCR，正文位置主要以章节和表格索引为准。
