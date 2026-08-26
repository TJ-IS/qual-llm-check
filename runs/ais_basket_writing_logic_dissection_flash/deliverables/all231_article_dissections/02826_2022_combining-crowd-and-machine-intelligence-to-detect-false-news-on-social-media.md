# Combining Crowd and Machine Intelligence to Detect False News on Social Media

- 作者：Xuan Wei; Zhu Zhang; Mingyue Zhang; Weiyun Chen; Daniel Dajun Zeng
- 年份 / 期刊：2022 / MIS Quarterly
- DOI：10.25300/misq/2022/16526
- 源文件：02826_2022_combining-crowd-and-machine-intelligence-to-detect-false-news-on-social-media.md
- 论文主类型：build_evaluate_design_science
- 主导写作弧线：requirements_build_evaluate_design_principles
- 置信度：0.75

## 文章级论证概况

- 核心问题：如何利用社交媒体上可扩展的群体智慧（用户回应和举报）并将其与机器智能有效结合，以更准确、更可解释、更稳健地检测假新闻？

- 制品与设计：提出CAND框架，包含信息提取和结果聚合两阶段。信息提取阶段从新闻特征、用户回应和用户举报中分别得到机器判断、混合判断和人类判断；结果聚合阶段用无监督贝叶斯聚合模型CLNAM统一整合，其中辟谣行为用伯努利分布建模，举报数用泊松分布建模，分类器预测概率用逻辑斯蒂正态分布建模，并使用变分推断估计后验。

- 客观结果：在微博和推特数据集上，CAND显著优于特征型、端到端和聚合型基准；如微博IR=1:7时CAND-123的AUC为97.54%，而最佳基准BERT为91.62%。加入回应和举报能持续提升性能，CLNAM优于多数投票和二项聚合模型；在高度不平衡、早期检测、恶意操纵、新闻长度和类型变化等情形下均表现出稳健性。

- 核心贡献：作者声称，这项研究证明了可扩展群体判断（回应和举报）在假新闻检测中的价值，提出了可解释的混合人类-机器判断聚合框架，展示了人类与机器智能互补、可用于早期检测且对操纵具有稳健性，并扩展了群体智慧与混合智能文献。

- 整篇论证链：文章先以假新闻的社会危害和现有机器智能方法的局限建立问题紧迫性，指出可扩展的人类智能未被充分利用。通过在线去抑制效应和智慧众两个理论，论证社交媒体用户会通过回应和举报贡献真实性判断，并以微博真实案例说明该现象。随后将一般问题收缩为四个可研究问题：有哪些可扩展人类智能、价值多大、如何高效利用、如何与机器智能结合。作者据此设计CAND框架，先由深度学习/机器学习提取机器与混合判断，再以CLNAM贝叶斯模型同时建模人类与机器的可信度并聚合混合类型数据。评估阶段用微博和推特两个真实数据集，通过增量数据源、端到端/聚合基准、不平衡比变化、早期检测截止时间、模拟参数压力测试、新闻长度与类型敏感性、恶意回应操纵和多分类扩展等实验，证明CAND的性能、可解释性、稳健性和实际可用性。讨论与结论部分把这些局部性能差异上升为人类-机器互补、早期检测、抗操纵和可复用设计知识，并回应引言中的人类智能缺口。

## 类型与写作弧线判定

- 论文主类型判定：该文围绕社会问题提出设计需求，构建了CAND/CLNAM这一计算制品，并通过两个真实数据集、多个基准、消融与稳健性实验进行评价，最后提炼设计知识与实践启示，符合需求—构建—评价—设计知识的设计科学范式。

- 主导写作弧线判定：论文从可扩展群体智能利用不足出发，提出建模可信度与混合数据类型聚合等设计要求，构建CAND框架和CLNAM模型，评价性能与稳健性，最后形成可复用的设计知识，主线为要求—构建—评价—设计原则。

## 研究开展程序

- study_or_phase_count：8

- 研究阶段总序列：研究程序先建立理论/需求基础，然后进入两阶段制品构建（信息提取与贝叶斯聚合），接着进行跨平台主评价和复制验证，再通过早期检测、真实应用场景、互补性可视化、稳健性与敏感性分析将性能结果转化为设计知识，最后用多分类扩展和偏差讨论界定边界。

### studies_or_phases

#### 1. 信息提取阶段：T1与T2任务构建

- order：1

- name_cn：信息提取阶段：T1与T2任务构建

- question_cn：如何从新闻特征、用户回应和举报中提取可用于后续聚合的机器判断、混合判断和人类判断？

- inputs_and_setting_cn：微博（2,186条假新闻、9,455条真新闻）和推特（943条假新闻、1,007条真新闻）的新闻文本、上下文特征、用户回应；对回应进行辟谣与否的人工标注，Cohen's kappa为0.816。

- designed_or_compared_object_cn：T1使用SVM、CNN、LSTM、Bi-LSTM、BERT五个基分类器；T2使用双CNN模块预测单个回应是否为辟谣回应。

- baseline_control_or_counterfactual_cn：T1以五种特征型分类器互为基准；T2没有无人工标注的对照，但使用iBCC聚合标注者标签。

##### objective_metrics

1. T2标注一致性Cohen's kappa=0.816

2. 假新闻与真新闻的平均辟谣概率差异（微博0.263 vs 0.045；推特0.107 vs 0.083）

- analysis_method_cn：监督分类；用jieba分词、tf-idf、词嵌入、网格搜索调参；T2用CNN提取新闻与回应表示并拼接后softmax分类。

- main_result_cn：信息提取阶段产生三类判断输入：T1的五组机器概率、T2的辟谣概率、微博的举报数（部分模拟）；表2显示假新闻回应中辟谣概率显著更高，支撑群体判断有效性。

- argumentative_role_cn：为CLNAM提供输入，同时用辟谣概率差异为群体智慧假设提供初步经验证据。

- remaining_uncertainty_cn：T1/T2分类器本身可能有误判；举报数据在微博部分模拟，推特不可用。

- link_to_next_phase_cn：提取出的连续概率与离散计数进入下一阶段的贝叶斯聚合模型。

##### evidence_pointers

1. Emperical Evaluations: Datasets and Preprocessing

2. Table 1

3. Table 2

#### 2. CLNAM贝叶斯聚合模型构建与推断

- order：2

- name_cn：CLNAM贝叶斯聚合模型构建与推断

- question_cn：如何对低可信度的人和机器判断进行聚合以得到新闻真实性后验，并处理连续与离散混合数据类型？

- inputs_and_setting_cn：信息提取阶段输出的三类判断：T1概率、T2概率、举报计数；使用共轭先验（beta、NIG、gamma）。

- designed_or_compared_object_cn：CLNAM模型；以伯努利建模辟谣行为、泊松建模举报计数、逻辑斯蒂正态建模分类器预测概率；使用坐标上升平均场变分推断。

- baseline_control_or_counterfactual_cn：在后续评价中与二项聚合模型BAM（用两硬币假设替换逻辑斯蒂正态）和多数投票MV对照。

##### objective_metrics

1. ELBO收敛

2. 最终预测的PR AUC等（在后续阶段评估）

- analysis_method_cn：概率图模型、共轭先验、平均场变分推断、坐标上升算法；从验证集学习先验。

- main_result_cn：给出可操作的CLNAM生成过程和推断算法；由于完整条件分布属于指数族且先验共轭，坐标更新有闭式解。

- argumentative_role_cn：将设计约束转化为形式模型，是整个框架的核心技术贡献。

- remaining_uncertainty_cn：模型性能尚未评估；逻辑斯蒂正态假设的合理性需要经验验证。

- link_to_next_phase_cn：模型构建完成后进入经验评价阶段，与基准方法比较。

##### evidence_pointers

1. Crowd-Powered Framework section

2. CLNAM Model

3. Model Inference

4. Learning Prior Beliefs section

5. Figure 4

#### 3. 微博主评估：性能与增量价值

- order：3

- name_cn：微博主评估：性能与增量价值

- question_cn：CAND是否优于特征型、端到端和聚合型基准？加入回应和举报是否带来增量价值？CLNAM聚合模型是否优于简单/二项聚合？

- inputs_and_setting_cn：微博不平衡数据集，IR从1:1到1:100；测试集按60/20/20划分；CAND-1/12/123分别使用不同数据源组合。

- designed_or_compared_object_cn：CAND-1、CAND-12、CAND-123；对照SVM、CNN、LSTM、Bi-LSTM、BERT、Concat、HSA、MV、BAM。

- baseline_control_or_counterfactual_cn：无群体智能的特征型基准；有群体智能的端到端基准；同数据源下的聚合基准；增量加入数据源的消融。

##### objective_metrics

1. PR AUC

2. F1 score

3. Recall

4. Precision

- analysis_method_cn：基准比较、增量消融、10次随机种子重复并报告SEM；在不同IR下重复。

- main_result_cn：CAND-123显著优于所有无群体智能基准，AUC从BERT的91.62%提升到97.54%；CAND-12仍优于全部特征型基准；CAND随数据源增加性能提升，而MV/BAM获益较少；CLNAM在所有数据源组合上优于MV和BAM；IR越高CAND优势越明显。

- argumentative_role_cn：提供核心证据支持框架有效、群体智能有价值、CLNAM优于替代聚合模型。

- remaining_uncertainty_cn：是否仅微博特有；是否受数据划分方式影响；举报数据的部分模拟是否影响结论。

- link_to_next_phase_cn：主结果后进入推特复制验证和稳健性检验。

##### evidence_pointers

1. False News Detection Performance: CAND vs. the Benchmark Methods

2. Figure 6a–6d

3. Figure 7

#### 4. 推特复制验证与划分稳健性

- order：4

- name_cn：推特复制验证与划分稳健性

- question_cn：在另一个平台和语言数据上，CAND是否仍优于基准？随机划分、时间划分、交叉验证是否改变结论？

- inputs_and_setting_cn：推特数据集，IR从1:1到1:2.5；无举报数据，因此仅评估CAND-1和CAND-12；补充时间切分、k折和留一验证。

- designed_or_compared_object_cn：CAND-1/CAND-12与特征型、端到端、聚合基准比较。

- baseline_control_or_counterfactual_cn：同微博的基准矩阵；CAND-12与CAND-1的增量比较。

##### objective_metrics

1. PR AUC

2. F1 score

3. Recall

4. Precision

- analysis_method_cn：跨数据集复制；与微博同样的实验流程；用不同划分方案检验稳健性。

- main_result_cn：推特结果与微博结论一致；随机划分、训练比例40%-90%、k折和LOOCV均不改变结论。

- argumentative_role_cn：增强外部有效性，说明框架不是微博特有产物。

- remaining_uncertainty_cn：推特缺少举报数据，无法检验CAND-123在推特的举报价值。

- link_to_next_phase_cn：核心性能证据确立后，进一步探讨早期检测、可解释性和稳健性。

##### evidence_pointers

1. Appendix B2

2. Appendix D1

#### 5. 早期检测截止时间分析

- order：5

- name_cn：早期检测截止时间分析

- question_cn：CAND需要等待多少回应才能有效检测假新闻？是否支持早期检测？

- inputs_and_setting_cn：CAND-12在微博IR=1:7与推特IR=1:1.5上，将响应收集最大时间从1分钟到4周变化。

- designed_or_compared_object_cn：不同响应截止时间下的CAND-12；以CAND-1作为参考线。

- baseline_control_or_counterfactual_cn：CAND-1（无回应）作为性能参考；不同截止时间互为对照。

##### objective_metrics

1. PR AUC

- analysis_method_cn：对时间截止点做性能曲线分析。

- main_result_cn：回应在最初几分钟即产生作用，性能在第一天内显著上升并随后稳定；约12小时到一天收集到代表性回应样本即可。

- argumentative_role_cn：把性能优势转化为实际可操作的早期检测能力。

- remaining_uncertainty_cn：无法用举报时间戳做同类分析；时间戳缺失。

- link_to_next_phase_cn：早期检测结果引出真实应用中‘等待vs实时’的权衡。

##### evidence_pointers

1. Analysis and Discussion: Early Detection

2. Figure 8

#### 6. 真实应用场景与可解释性分析

- order：6

- name_cn：真实应用场景与可解释性分析

- question_cn：CAND如何在真实平台上逐条处理帖子？聚合模型如何解释每个帖子的判断来源？

- inputs_and_setting_cn：将微博帖子按事件聚类；对CAND-123在IR=1:7下的单个帖子后验贡献进行可视化；提出新事件时间线。

- designed_or_compared_object_cn：解释真实应用流程；展示三类判断与先验对后验的相对贡献。

- baseline_control_or_counterfactual_cn：无直接反事实；以CAND-1作为实时检测替代方案。

##### objective_metrics

1. 相对贡献比例（可视化）

2. 可解释性描述

- analysis_method_cn：事件聚类流程说明、后验贡献分解、堆叠条形图可视化。

- main_result_cn：框架可以先聚类再等待约12小时预测；机器判断和混合判断贡献最多，但没有单一来源始终主导，互补性明显；模型对每个预测来源透明。

- argumentative_role_cn：连接benchmark结果与真实部署，同时展示可解释这一设计优势。

- remaining_uncertainty_cn：贡献比例是示例性而非统计检验；等待时间依赖于平台数据积累速度。

- link_to_next_phase_cn：可解释性优势引出对多个分类器价值的实际建议。

##### evidence_pointers

1. Real-World Application of CAND

2. Complementary Strengths of Humans and Machines

3. Figure 9

4. Figure 10

#### 7. 稳健性与敏感性测试套件

- order：7

- name_cn：稳健性与敏感性测试套件

- question_cn：CAND在举报模拟参数、新闻长度、新闻类型、恶意回应操纵和不同分类器数量下是否依然稳健有效？

- inputs_and_setting_cn：微博数据集（部分也用到推特）；模拟误报率0-0.6、假新闻举报率0.05-0.9；新闻最大长度5-2500；七类假新闻类型标注；六种恶意回应操控；不同分类器组合。

- designed_or_compared_object_cn：CAND-12/CAND-123/CAND-1在不同条件下的表现；对照不使用部分数据源或使用弱分类器的变体。

- baseline_control_or_counterfactual_cn：CAND-12作为无举报信息的参考；CAND-1作为无回应的参考；不同模拟参数互为反事实。

##### objective_metrics

1. PR AUC

2. F1 score

3. 性能下降/提高幅度

- analysis_method_cn：压力测试、敏感性分析、模拟操控、分类器组合枚举。

- main_result_cn：即使60%真新闻被误报或仅5%假新闻被举报，CAND-123仍优于CAND-12；CAND-12受新闻长度影响更小；不同假新闻类型上性能有差异但总体稳健；对六类模拟恶意回应操控不脆弱；增加分类器数量提高性能但边际递减，弱分类器无害。

- argumentative_role_cn：界定边界条件，回应数据不可用、操纵攻击和实际异质性等威胁。

- remaining_uncertainty_cn：恶意操纵是模拟而非真实攻击；新闻类型分析较初步；部分结果依赖在线附录。

- link_to_next_phase_cn：稳健性结果后进一步检验替代建模方案（多分类）和偏差问题。

##### evidence_pointers

1. Stress Testing of the Simulation Parameters

2. Sensitivity to News Characteristics

3. Robustness to Intentional Manipulation of Responses and Reports

4. Value of Multiple Feature-Based Classifiers

5. Figure 11

6. Figure 12

7. Figure 13

#### 8. 多分类扩展与数据集偏差讨论

- order：8

- name_cn：多分类扩展与数据集偏差讨论

- question_cn：将辟谣回应检测从二分类扩展为多分类是否会改善CAND？数据集偏差如何缓解？

- inputs_and_setting_cn：在微博数据集上扩展回应标签为多分类；设计CAM和E-CAM模型；讨论标注偏差与选择偏差的缓解方法。

- designed_or_compared_object_cn：CAM（完全利用多分类信息但无逻辑斯蒂正态）、E-CAM（部分利用多分类但保留逻辑斯蒂正态）与CAND比较。

- baseline_control_or_counterfactual_cn：CAND二分类作为主要对照；CAM作为多分类替代。

##### objective_metrics

1. PR AUC

2. 与CAND的性能差距

- analysis_method_cn：模型变体比较、在线补充实验、偏差缓解讨论。

- main_result_cn：E-CAM与CAND相当且都优于CAM，说明逻辑斯蒂正态假设重要，而多分类带来的边际收益有限；文章在附录中说明标注偏差和选择偏差的缓解。

- argumentative_role_cn：证明核心技术选择不是偶然，同时回应公平性关切。

- remaining_uncertainty_cn：多分类扩展的完整结果在在线附录；偏差分析不是定量因果检验。

- link_to_next_phase_cn：这些边界和扩展讨论进入结论，提炼贡献与局限。

##### evidence_pointers

1. Debunking Response Detection as a Multiclass Classification Problem

2. Dataset Bias

3. Appendix Section D5

4. Appendix Section D6

## 各部分修辞架构

### abstract_moves

1. CONTEXT: 假新闻泛滥及COVID-19信息疫情

2. LIMITATION: 机器智能成效有限、人类智能未被充分利用

3. RQ_OR_OBJECTIVE: 提出将回应与举报两类可扩展群体判断与机器智能结合

4. DESIGN_FEATURE: 概述CAND框架与无监督贝叶斯聚合

5. RESULT: 微博和推特数据集上的性能优势

6. CONTRIBUTION: 互补价值、早期检测、抗操纵及文献贡献

### introduction_moves

1. CONTEXT: 假新闻成为全球性问题

2. PRACTICAL_STAKES: 经济、信任与公共健康后果

3. PRIOR_KNOWLEDGE: 业界的举报/人工核查与机器学习措施

4. PRIOR_KNOWLEDGE: 学术界基于内容和社交特征的计算检测

5. LIMITATION: 人类智能受成本和可扩展性限制

6. GAP: 可扩展人类智能未被充分利用

7. RQ_OR_OBJECTIVE: 提出四个关于可扩展人类智能的研究问题

8. THEORY_INTRO: 引入在线去抑制效应与智慧众

9. MECHANISM: 用户会通过评论/举报表达异议，聚合可受益

10. PHENOMENON: 微博台风山竹案例

11. LIMITATION: 群体判断可能不可靠

12. DESIGN_FEATURE: CAND两阶段框架

13. STUDY_OVERVIEW: 预告评测、洞察与贡献

### theory_and_knowledge_moves

1. THEORY_INTRO: 在线去抑制效应和智慧众

2. THEORY_PROPOSITION: 用户在线更坦诚表达异议

3. PRIOR_KNOWLEDGE: 智慧众在众包、预测市场等场景的IS应用

4. MECHANISM: 聚合后真假新闻呈现不同辟谣/举报模式

5. PRIOR_KNOWLEDGE: 现有计算检测的内容/社交情境分类

6. LIMITATION: 回应和举报被用作黑箱特征或分开研究

7. GAP: 缺乏可解释结合两类群体智能的方法

8. PRIOR_KNOWLEDGE: 信息聚合的分类器组合与众包答案聚合文献

9. GAP: 现有聚合只涉及单一人类或机器来源

### artifact_design_moves

1. REQUIREMENT: 人类和机器都可能不可靠，需要建模可信度

2. REQUIREMENT: 需要聚合连续概率与离散计数等混合类型

3. DESIGN_FEATURE: 信息提取阶段T1/T2与举报数

4. DESIGN_FEATURE: 伯努利、泊松、逻辑斯蒂正态分布组合

5. METHOD_JUSTIFICATION: 逻辑斯蒂正态比两硬币模型保留更多预测信息

6. DESIGN_FEATURE: CLNAM生成过程与共轭先验

7. METHOD_JUSTIFICATION: 使用平均场变分推断处理不可处理后验

8. DESIGN_FEATURE: 从验证集数据学习先验

### evaluation_moves

1. METHOD_JUSTIFICATION: 使用微博/推特和不同IR模拟真实不平衡

2. METHOD_JUSTIFICATION: 标注一致性、辟谣概率差异

3. BENCHMARK_OR_CONTRAST: 设计端到端与聚合基准矩阵

4. METHOD_JUSTIFICATION: 以PR AUC为主要指标并优先召回

5. METHOD_JUSTIFICATION: 统一调参、多次随机重复、控制响应收集窗口

6. RESULT: 主性能对比与增量消融

7. ROBUSTNESS_OR_BOUNDARY_TEST: IR变化、切分稳健性、早期检测、压力测试、敏感性、操纵模拟

8. TRANSITION: 从核心性能转向实际应用和边界条件

### discussion_and_contribution_moves

1. RESULT: 早期检测时间窗口分析

2. BOUNDARY_CONDITION: 真实应用等待约12小时、可退化为CAND-1实时模式

3. RESULT: 互补贡献可视化与可解释性

4. RESULT: 多分类器数量与弱分类器价值

5. ROBUSTNESS_OR_BOUNDARY_TEST: 压力测试与操纵模拟

6. CONTRIBUTION: 性能、可解释性、灵活性三大优势

7. CONTRIBUTION: 群体判断价值与混合智能可信度建模

8. PRACTICAL_STAKES: 平台与用户建议

9. LIMITATION_AND_FUTURE: 真新闻选取、隐含真实效应、用户加权、扩展数据源

## 理论/知识到设计的翻译

### 知识/理论基础

1. 在线去抑制效应（Suler, 2004）

2. 智慧众/集体智慧（Surowiecki, 2005）

3. 混合人类-机器智能（Kamar, 2016; Demartini et al., 2017）

4. 信息聚合/分类器组合/众包答案聚合（Dawid & Skene, 1979; Kim & Ghahramani, 2012）

5. 贝叶斯生成建模与变分推断（Blei et al., 2017）

- 理论—设计耦合：partial

- 耦合判定理由：智慧众和在线去抑制效应决定了使用用户回应与举报作为可扩展人类智能来源，并提出聚合不可靠判断的设计方向；但CLNAM的具体组件（逻辑斯蒂正态、泊松分布、共轭先验、变分推断）以及深度学习信息提取主要来自统计建模和工程经验，并通过benchmark而非严格理论假设检验来验证。

- 理论到设计翻译链：假新闻检测问题 → 观察到回应/举报作为可扩展群体行为 → 在线去抑制效应解释行为来源、智慧众解释聚合价值 → 设计要求：建模人类和机器可信度并处理混合数据 → 贝叶斯生成模型CLNAM → 信息提取阶段供给三类判断 → 跨平台不平衡基准评价 → 稳健性/边界分析 → 设计知识与理论贡献。

### mapping_table

#### 1. 1

- theory_or_knowledge_claim_cn：在线去抑制效应使社交媒体用户更愿意在线表达异议，包括评论辟谣和举报。

- mechanism_cn：用户读到与自己信念相悖的新闻时，由于网络匿名/异步环境约束减少，更可能公开表达不认同。

- design_requirement_cn：应利用自愿涌现的回应和举报作为可扩展人类判断来源。

- artifact_choice_cn：CAND将T2回应辟谣检测和举报计数作为两类群体判断输入。

- evaluated_contrast_cn：CAND-12/CAND-123与不使用回应/举报的CAND-1及特征型基准比较。

- objective_result_cn：加入回应和举报后性能显著提升；辟谣概率差异显著。

##### evidence_pointers

1. Figure 6b

2. Table 2

3. Introduction P5

#### 2. 2

- theory_or_knowledge_claim_cn：智慧众认为大量个体的聚合判断可超越单个或专家判断。

- mechanism_cn：个体判断有噪声，但聚合后真/假新闻展现出不同的辟谣与举报模式。

- design_requirement_cn：不能依赖单条判断，需要显式建模每个判断源的可信度并进行概率聚合。

- artifact_choice_cn：CLNAM用伯努利、泊松和逻辑斯蒂正态分布联合建模群体与机器行为。

- evaluated_contrast_cn：CLNAM与多数投票MV、二项聚合BAM比较。

- objective_result_cn：CLNAM在所有数据源组合上优于MV和BAM。

##### evidence_pointers

1. Figure 6b

2. Figure B1

#### 3. 3

- theory_or_knowledge_claim_cn：人类和机器具有互补的问题解决能力。

- mechanism_cn：机器擅长大规模模式学习，但依赖训练数据；人类更擅长上下文理解并能更新知识。

- design_requirement_cn：应同时整合机器判断、人类回应判断和人类举报判断。

- artifact_choice_cn：设计CAND-123整合三类判断，保持可解释结构。

- evaluated_contrast_cn：CAND-1→CAND-12→CAND-123增量比较；CAND与端到端黑箱模型比较。

- objective_result_cn：增量加入人类判断带来性能提升；CAND优于端到端基准，且贡献可视化显示来源互补。

##### evidence_pointers

1. Figure 6a–6d

2. Figure 10

#### 4. 4

- theory_or_knowledge_claim_cn：信息聚合文献中，结果聚合可通过多数投票、加权或贝叶斯可信度建模实现。

- mechanism_cn：贝叶斯方法通过生成过程解释观测判断与隐式真值之间的关系，从而对不可靠来源降权。

- design_requirement_cn：需要针对人类-机器混合判断和混合数据类型设计专门的聚合模型。

- artifact_choice_cn：CLNAM采用共轭先验和平均场变分推断。

- evaluated_contrast_cn：与只使用单一来源的传统聚合模型（MV/BAM）对比。

- objective_result_cn：混合场景下CLNAM优于简单聚合和传统二项假设。

##### evidence_pointers

1. Information Aggregation section

2. Figure 6b

#### 5. 5

- theory_or_knowledge_claim_cn：分类器输出的连续概率比二元预测承载更多信息。

- mechanism_cn：将概率阈值化会丢失0.51与1之间的差异；逻辑斯蒂正态分布能描述logit空间的分布。

- design_requirement_cn：建模分类器可信度时应充分利用连续预测概率。

- artifact_choice_cn：采用逻辑斯蒂正态分布而非两硬币模型。

- evaluated_contrast_cn：CAND与BAM比较；CAM/E-CAM的多分类扩展比较；图3经验分布。

- objective_result_cn：CAND优于BAM，E-CAM优于CAM，说明逻辑斯蒂正态假设更有效。

##### evidence_pointers

1. Technical Insights

2. Figure 3

3. Multiclass extension

## 评价逻辑

### evaluation_modes

1. dataset_benchmark_comparison

2. incremental_ablation

3. cross_platform_replication

4. cutoff_time_analysis

5. stress_testing_and_robustness_simulation

6. sensitivity_analysis

7. interpretability_visualization

8. model_variant_comparison

- why_these_evaluations_cn：主benchmark用于确立整体性能优势；增量消融用于证明群体智能和每个数据源的贡献；跨平台复制用于外部有效性；截止时间分析用于早期检测实际价值；压力测试和敏感性分析用于应对数据模拟、平台差异和恶意操纵等威胁；可解释性分析用于支撑设计知识；模型变体比较用于验证关键分布假设。

- benchmark_and_contrast_chain_cn：先从无群体智能的特征型基准（SVM/CNN/LSTM/Bi-LSTM/BERT）建立基线，确定CAND聚合的价值；再用端到端基准（Concat/HSA）证明CAND优于黑箱多源融合；最后通过聚合基准（MV/BAM）证明CLNAM优于已有聚合思路。与此同时，CAND-1、CAND-12、CAND-123的增量对比把性能差异归因到回应和举报；IR变化将不平衡性作为压力条件；早期检测、压力测试、敏感性分析和操纵模拟进一步把性能优势转化为边界条件和实用知识。

### claim_evidence_ledger

#### 1. CAND框架优于特征型/端到端基准方法

- claim_cn：CAND框架优于特征型/端到端基准方法

- evidence_cn：微博IR=1:7时CAND-123的AUC为97.54%，最优基准BERT为91.62%；推特结果一致

- support_cn：强

#### 2. 加入回应和举报能提升假新闻检测性能

- claim_cn：加入回应和举报能提升假新闻检测性能

- evidence_cn：CAND-1到CAND-12到CAND-123性能递增；图6b显示F1从94.02%到95.57%到97.54%

- support_cn：强

#### 3. CLNAM聚合模型优于MV和BAM

- claim_cn：CLNAM聚合模型优于MV和BAM

- evidence_cn：在相同数据源组合下CAND均优于MV/BAM；与BAM的差距归因于逻辑斯蒂正态假设

- support_cn：强

#### 4. 逻辑斯蒂正态假设优于伯努利两硬币假设

- claim_cn：逻辑斯蒂正态假设优于伯努利两硬币假设

- evidence_cn：CAND vs BAM性能优势；图3经验分布拟合；E-CAM优于CAM

- support_cn：中

#### 5. 群体智能可支持早期检测

- claim_cn：群体智能可支持早期检测

- evidence_cn：图8显示响应在几分钟内开始生效，12小时到一天足以稳定性能

- support_cn：强

#### 6. 方法对人为操纵稳健

- claim_cn：方法对人为操纵稳健

- evidence_cn：图12压力测试与在线附录D4的六类模拟恶意回应操控

- support_cn：中（基于模拟而非真实攻击）

#### 7. 人类与机器智能互补

- claim_cn：人类与机器智能互补

- evidence_cn：图10贡献可视化显示没有单一来源始终主导

- support_cn：中（视觉证据，无显著性检验）

- internal_validity_strategy_cn：使用多种数据划分（随机、时间切分、k折、LOOCV）；统一超参数网格搜索；10次随机种子重复并报告SEM；T2标注用多人标注与Cohen's kappa；通过增量消融和模型变体比较控制数据组合与假设差异；对模拟参数进行压力测试。

- external_validity_strategy_cn：使用微博和推特两个平台、不同语言和情境的数据；设置多种不平衡比；跨平台复制；对新闻长度、新闻类型、分类器数量、响应截止时间和操纵比例进行敏感性分析；在附录中补充Twitter图表和在线补充实验。

- what_is_not_actually_tested_cn：在线去抑制效应和智慧众的心理机制没有被直接测量；人类用户行为数据来自观察而非实验；微博举报数据部分为模拟且无举报时间戳；没有真实平台部署或A/B测试；对恶意操纵的稳健性来自模拟而非真实攻击；多分类与偏差讨论依赖在线补充材料；没有对真实用户在真实时间线中的使用进行现场验证。

## 贡献闭环

- technical_claim_cn：CAND/CLNAM在假新闻检测上优于特征型、端到端和聚合型基准，尤其在高不平衡数据下更稳定。

- artifact_claim_cn：可识别的设计部分——加入回应/举报数据和CLNAM的可信度建模——带来了改进；特别是逻辑斯蒂正态假设相对于伯努利假设的增量价值。

- mechanism_claim_cn：社交媒体用户的在线去抑制效应促使他们通过评论辟谣和举报表达对新闻真实性的判断；聚合后假新闻与真新闻呈现不同模式，因而群体判断可作为机器判断的互补信号。

- boundary_claim_cn：在需要等待约12小时到一天收集群体回应时有效；在缺乏举报数据的平台上仍可用回应信号；对数据不平衡、部分模拟误报/漏报、新闻长度变化和模拟性恶意操纵具有稳健性；但依赖用户自愿产生回应和举报。

- reusable_design_knowledge_cn：可复用设计原则包括：利用自愿且可扩展的群体行为作为智能源；显式建模人类和机器判断源的可信度；对连续分类器概率使用保留完整信息的分布而非二元化；用生成式贝叶斯模型聚合混合数据类型；从验证集学习先验；构建可解释的贡献分解以支持决策。

- theoretical_contribution_cn：将智慧众和在线去抑制效应引入假新闻检测，实证支持人类与机器智能互补；提出在混合人类-机器系统中建模两类来源可信度的概率方法；对混合智能和群体智能文献有扩展意义。

- how_discussion_closes_intro_gap_cn：引言指出可扩展人类智能未被充分利用；讨论和结论通过CAND-12/CAND-123的增量性能、跨平台复制、早期检测、互补贡献可视化和抗操纵测试，直接证明回应与举报这两类可扩展群体判断不仅可用，而且能显著提升机器检测并形成设计知识。

- overclaim_or_unsupported_leaps_cn：将‘人类与机器互补’主要由可视化贡献图支撑，缺乏统计检验；‘抗操纵’基于模拟操纵而非真实恶意账户；举报数据部分模拟却用于支持CAND-123的强结论；在线去抑制效应作为机制未被直接验证；多分类和偏差缓解的完整证据放在在线附录，正文无法完全核验。

## 句级写作动作图谱

### 1. Abstract S1

- order：1

- section：Abstract

- locator：Abstract S1

- move_code：CONTEXT

- paraphrase_cn：假新闻在社交媒体上的爆炸式传播，尤其在COVID-19信息疫情背景下，严重影响新闻生态、政治、经济和公众信任。

- rhetorical_function_cn：开篇确立问题的重要性和紧迫性。

- depends_on_cn：无前置依赖。

- sets_up_cn：为后文提出检测需求提供背景。

- evidence_pointer：Abstract P1

### 2. Abstract S2

- order：2

- section：Abstract

- locator：Abstract S2

- move_code：LIMITATION

- paraphrase_cn：机器智能在检测和遏制假新闻方面成效有限，而人类知识/智能极具补充潜力，但现有研究仍缺乏高效利用方式。

- rhetorical_function_cn：指出现有技术路径的不足，形成缺口。

- depends_on_cn：上一篇确立问题严重性。

- sets_up_cn：为引入群体智能方向作铺垫。

- evidence_pointer：Abstract P2

### 3. Abstract S3

- order：3

- section：Abstract

- locator：Abstract S3

- move_code：RQ_OR_OBJECTIVE

- paraphrase_cn：观察到用户通过发布回应或举报来对新闻真实性做出判断，提出将这两类可扩展群体判断与机器智能结合。

- rhetorical_function_cn：从观察到的主张过渡到研究目标。

- depends_on_cn：人类智能可扩展性缺口。

- sets_up_cn：引出CAND框架。

- evidence_pointer：Abstract S3

### 4. Abstract S4

- order：4

- section：Abstract

- locator：Abstract S4

- move_code：DESIGN_FEATURE

- paraphrase_cn：设计CAND框架，从新闻特征和可扩展群体智能中提取相关人类/机器判断，再用无监督贝叶斯聚合模型整合。

- rhetorical_function_cn：简要介绍制品核心设计。

- depends_on_cn：提出结合方向。

- sets_up_cn：为后续评估做铺垫。

- evidence_pointer：Abstract S4

### 5. Abstract S5

- order：5

- section：Abstract

- locator：Abstract S5

- move_code：RESULT

- paraphrase_cn：基于微博和推特数据集评估，证明群体智能有效且CAND框架优于基准方法。

- rhetorical_function_cn：给出核心经验证据。

- depends_on_cn：制品设计完成。

- sets_up_cn：为贡献陈述作准备。

- evidence_pointer：Abstract S5

### 6. Abstract S6

- order：6

- section：Abstract

- locator：Abstract S6

- move_code：CONTRIBUTION

- paraphrase_cn：结果带来互补价值、早期检测和抗操纵等洞察，研究贡献于假新闻检测与群体智能文献。

- rhetorical_function_cn：概括理论/实践贡献。

- depends_on_cn：经验结果。

- sets_up_cn：帮助读者把握全文贡献。

- evidence_pointer：Abstract S6

### 7. Introduction P1 S1–S2

- order：7

- section：Introduction

- locator：Introduction P1 S1–S2

- move_code：CONTEXT

- paraphrase_cn：假新闻被视作全球性最大关切之一，大量调查受访者暴露于假新闻，社交媒体加剧了其传播。

- rhetorical_function_cn：从社会现实切入，建立话题重要性。

- depends_on_cn：无。

- sets_up_cn：为现实危害提供证据。

- evidence_pointer：Introduction P1

### 8. Introduction P1 S4–S5

- order：8

- section：Introduction

- locator：Introduction P1 S4–S5

- move_code：PRACTICAL_STAKES

- paraphrase_cn：假新闻降低新闻信任、影响电子商务和投资，例如一条假推文曾让股市蒸发1300亿美元。

- rhetorical_function_cn：说明问题不解决的经济与社会代价。

- depends_on_cn：假新闻背景。

- sets_up_cn：证明该问题值得IS研究。

- evidence_pointer：Introduction P1

### 9. Introduction P2 S1–S2

- order：9

- section：Introduction

- locator：Introduction P2 S1–S2

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：Facebook等公司允许用户标记可疑新闻并交给第三方核查，新浪微博也允许举报，机器学习算法已被用来识别假新闻。

- rhetorical_function_cn：展示业界已有应对措施。

- depends_on_cn：问题严重性。

- sets_up_cn：为后文指出这些措施仍依赖机器人工核查留下缺口。

- evidence_pointer：Introduction P2

### 10. Introduction P3 S1–S3

- order：10

- section：Introduction

- locator：Introduction P3 S1–S3

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：学术界主要使用新闻内容和社交情境两类数据源，提取特征后输入机器学习算法，总体上严重依赖机器智能。

- rhetorical_function_cn：总结学术现状。

- depends_on_cn：业界现状。

- sets_up_cn：为人类智能缺口铺垫。

- evidence_pointer：Introduction P3

### 11. Introduction P3 S4

- order：11

- section：Introduction

- locator：Introduction P3 S4

- move_code：LIMITATION

- paraphrase_cn：人类智能是高成本且受限的资源，专家导向和众包导向的事实核查难以大规模应用，因此当前仍被低估。

- rhetorical_function_cn：指出现有研究中的可扩展性限制。

- depends_on_cn：学术现状。

- sets_up_cn：引出可扩展群体智能问题。

- evidence_pointer：Introduction P3

### 12. Introduction P3 S5

- order：12

- section：Introduction

- locator：Introduction P3 S5

- move_code：RQ_OR_OBJECTIVE

- paraphrase_cn：提出四个研究问题：何种可扩展人类智能可用、价值多大、如何高效利用、如何与机器智能共生结合。

- rhetorical_function_cn：把一般限制转化为明确研究问题。

- depends_on_cn：人类智能缺口。

- sets_up_cn：为研究设计建立目标。

- evidence_pointer：Introduction P3

### 13. Introduction P4 S1

- order：13

- section：Introduction

- locator：Introduction P4 S1

- move_code：THEORY_INTRO

- paraphrase_cn：以智慧众和网络去抑制效应作为提出方法的理论基础。

- rhetorical_function_cn：引入理论支柱。

- depends_on_cn：研究问题。

- sets_up_cn：为使用回应/举报提供理论依据。

- evidence_pointer：Introduction P4

### 14. Introduction P4 S2–S4

- order：14

- section：Introduction

- locator：Introduction P4 S2–S4

- move_code：MECHANISM

- paraphrase_cn：网络去抑制效应表明用户在网上更开放地表达不同意；聚合这些意见可以受益于智慧众。

- rhetorical_function_cn：解释为什么群体判断会出现并有效。

- depends_on_cn：理论基础。

- sets_up_cn：为选择回应和举报数据作铺垫。

- evidence_pointer：Introduction P4

### 15. Introduction P5 S1–S3

- order：15

- section：Introduction

- locator：Introduction P5 S1–S3

- move_code：PHENOMENON

- paraphrase_cn：以微博台风“山竹”新闻为例，展示用户通过举报按钮和辟谣回应贡献真实性判断。

- rhetorical_function_cn：用真实例子使抽象机制具体化。

- depends_on_cn：机制解释。

- sets_up_cn：引出该现象的可靠性和局限性讨论。

- evidence_pointer：Introduction P5/Figure 1

### 16. Introduction P5 S7–S8

- order：16

- section：Introduction

- locator：Introduction P5 S7–S8

- move_code：LIMITATION

- paraphrase_cn：并非每个读者都会举报或发表辟谣评论，也可能误报误评，因此单靠群体判断不可靠。

- rhetorical_function_cn：指出真实现象中的噪声。

- depends_on_cn：真实例子。

- sets_up_cn：为结合机器智能和聚合建模提供原因。

- evidence_pointer：Introduction P5

### 17. Introduction P6 S1–S4

- order：17

- section：Introduction

- locator：Introduction P6 S1–S4

- move_code：DESIGN_FEATURE

- paraphrase_cn：介绍CAND框架：提取机器、人类与混合判断，用无监督贝叶斯聚合模型得到最终预测。

- rhetorical_function_cn：正式提出制品。

- depends_on_cn：问题与局限。

- sets_up_cn：为评估设计做预告。

- evidence_pointer：Introduction P6

### 18. Introduction P6 S5–S6

- order：18

- section：Introduction

- locator：Introduction P6 S5–S6

- move_code：STUDY_OVERVIEW

- paraphrase_cn：预告将在微博和推特上验证框架，并报告互补性、早期检测和抗操纵等洞察。

- rhetorical_function_cn：设定全文研究步骤和读者预期。

- depends_on_cn：制品提出。

- sets_up_cn：为后续章节的评估与分析作路标。

- evidence_pointer：Introduction P6

### 19. Theoretical Foundations P1

- order：19

- section：Related Work: Theoretical Foundations

- locator：Theoretical Foundations P1

- move_code：THEORY_PROPOSITION

- paraphrase_cn：网络去抑制效应意味着至少部分用户会在相反信念时诚实评论或举报，而面对面时可能不表态。

- rhetorical_function_cn：将心理学理论转化为社交媒体行为命题。

- depends_on_cn：理论引入。

- sets_up_cn：支撑群体判断数据来源的合理性。

- evidence_pointer：Related Work: Theoretical Foundations P1

### 20. Theoretical Foundations P2

- order：20

- section：Related Work: Theoretical Foundations

- locator：Theoretical Foundations P2

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：智慧众在众包市场、众筹、用户生成内容和IS研究中已被广泛应用。

- rhetorical_function_cn：说明理论有经验基础。

- depends_on_cn：理论命题。

- sets_up_cn：支持聚合群体判断有效。

- evidence_pointer：Related Work: Theoretical Foundations P2

### 21. Theoretical Foundations P2 last sentence

- order：21

- section：Related Work: Theoretical Foundations

- locator：Theoretical Foundations P2 last sentence

- move_code：MECHANISM

- paraphrase_cn：单个用户可能不可靠，但聚合后真假新闻会呈现不同的辟谣和举报模式。

- rhetorical_function_cn：从个体不可靠走向群体可靠的机制桥。

- depends_on_cn：智慧众文献。

- sets_up_cn：为贝叶斯模型假设不同分布提供前提。

- evidence_pointer：Related Work: Theoretical Foundations P2

### 22. Computational detection P1–P5

- order：22

- section：Related Work: Computational False News Detection

- locator：Computational detection P1–P5

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：现有计算检测分为基于新闻内容和基于社交情境两类，前者包括知识、风格和深度学习方法，后者包括用户、帖子、网络和标记特征。

- rhetorical_function_cn：系统总结基准文献。

- depends_on_cn：问题背景。

- sets_up_cn：为后续基准选择提供基础。

- evidence_pointer：Related Work: Computational False News Detection

### 23. Computational detection P6

- order：23

- section：Related Work: Computational False News Detection

- locator：Computational detection P6

- move_code：GAP

- paraphrase_cn：现有文献把回应和举报主要用作黑箱方法特征，或分开研究，缺乏结合两类群体智能并利用可解释结构的方法。

- rhetorical_function_cn：精准指出文献空白。

- depends_on_cn：文献综述。

- sets_up_cn：为CAND的可解释结构定位。

- evidence_pointer：Related Work: Computational False News Detection P6

### 24. Information Aggregation P1–P3

- order：24

- section：Related Work: Information Aggregation

- locator：Information Aggregation P1–P3

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：分类器组合和众包答案聚合已有大量方法，包括多数投票、iBCC、DS模型，但通常只处理人类或机器单一来源。

- rhetorical_function_cn：总结聚合方法学基础。

- depends_on_cn：需要聚合判断。

- sets_up_cn：说明为什么需要新模型。

- evidence_pointer：Related Work: Information Aggregation

### 25. Information Aggregation P4

- order：25

- section：Related Work: Information Aggregation

- locator：Information Aggregation P4

- move_code：GAP

- paraphrase_cn：本场景需要同时聚合人类和机器的混合判断，与现有只涉及单一来源的文献不同，需要专门设计模型。

- rhetorical_function_cn：点出技术缺口。

- depends_on_cn：文献基础。

- sets_up_cn：引出CLNAM。

- evidence_pointer：Related Work: Information Aggregation P4

### 26. Framework P1

- order：26

- section：Crowd-Powered Framework

- locator：Framework P1

- move_code：DESIGN_FEATURE

- paraphrase_cn：提出CAND框架，包含信息提取和结果聚合两阶段，并给出新闻内容/上下文特征定义。

- rhetorical_function_cn：开始设计章节。

- depends_on_cn：缺口和技术需要。

- sets_up_cn：为后续技术细节提供框架。

- evidence_pointer：Crowd-Powered Framework section P1/Figure 2

### 27. Information Extraction subsection

- order：27

- section：Crowd-Powered Framework

- locator：Information Extraction subsection

- move_code：DESIGN_FEATURE

- paraphrase_cn：将信息提取任务分为T1基于特征检测假新闻和T2检测辟谣回应；举报数直接作为人类判断输入。

- rhetorical_function_cn：细化信息提取阶段。

- depends_on_cn：框架顶层。

- sets_up_cn：为CLNAM提供三类输入。

- evidence_pointer：Information Extraction subsection

### 28. Challenges P1

- order：28

- section：Crowd-Powered Framework: CLNAM

- locator：Challenges P1

- move_code：REQUIREMENT

- paraphrase_cn：人类和机器都可能不可靠：分类器会犯错，用户可能不辟谣、误辟谣、误举报，因此聚合必须建模可信度。

- rhetorical_function_cn：提出设计约束。

- depends_on_cn：提取结果。

- sets_up_cn：证明简单聚合不够。

- evidence_pointer：CLNAM: Challenges P1

### 29. Challenges P2

- order：29

- section：Crowd-Powered Framework: CLNAM

- locator：Challenges P2

- move_code：REQUIREMENT

- paraphrase_cn：待聚合数据包括连续概率和离散计数，现有聚合文献未处理这种混合类型，需要新模型。

- rhetorical_function_cn：提出第二个设计约束。

- depends_on_cn：混合判断特征。

- sets_up_cn：为贝叶斯生成模型做铺垫。

- evidence_pointer：CLNAM: Challenges P2

### 30. Technical Insights P1

- order：30

- section：Crowd-Powered Framework: CLNAM

- locator：Technical Insights P1

- move_code：DESIGN_FEATURE

- paraphrase_cn：用伯努利分布建模辟谣行为、泊松分布建模举报次数、逻辑斯蒂正态分布建模分类器预测概率。

- rhetorical_function_cn：给出模型组件选择。

- depends_on_cn：设计约束。

- sets_up_cn：形成CLNAM生成过程。

- evidence_pointer：CLNAM: Technical Insights P1

### 31. Technical Insights P2

- order：31

- section：Crowd-Powered Framework: CLNAM

- locator：Technical Insights P2

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：相比两硬币模型的伯努利假设，逻辑斯蒂正态保留更多预测概率信息，并用图3的经验分布作为证据。

- rhetorical_function_cn：为关键技术选择辩护。

- depends_on_cn：模型组件选择。

- sets_up_cn：解释与BAM的差异来源。

- evidence_pointer：CLNAM Technical Insights P2/Figure 3

### 32. CLNAM Model paragraph

- order：32

- section：Crowd-Powered Framework: CLNAM

- locator：CLNAM Model paragraph

- move_code：DESIGN_FEATURE

- paraphrase_cn：形式化定义生成过程：从先验、真实标签到三类判断的分布及共轭先验；图4为图模型。

- rhetorical_function_cn：完整搭建模型。

- depends_on_cn：技术洞察。

- sets_up_cn：为推断算法提供对象。

- evidence_pointer：CLNAM Model/Figure 4

### 33. Model Inference paragraph

- order：33

- section：Crowd-Powered Framework: CLNAM

- locator：Model Inference paragraph

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：由于后验难以精确计算，采用坐标上升平均场变分推断，可扩展到大规模数据并保证收敛到局部最优。

- rhetorical_function_cn：解释推断选择。

- depends_on_cn：生成模型。

- sets_up_cn：为算法实现和后续评估提供依据。

- evidence_pointer：Model Inference subsection

### 34. Learning Prior Beliefs paragraph

- order：34

- section：Crowd-Powered Framework: CLNAM

- locator：Learning Prior Beliefs paragraph

- move_code：DESIGN_FEATURE

- paraphrase_cn：利用两阶段特性从验证集行为学习先验，以减轻贝叶斯模型对先验的敏感性。

- rhetorical_function_cn：补充实用设计。

- depends_on_cn：贝叶斯模型。

- sets_up_cn：增强模型稳健性。

- evidence_pointer：Learning Prior Beliefs subsection

### 35. Datasets and Preprocessing P1–P2

- order：35

- section：Emperical Evaluations

- locator：Datasets and Preprocessing P1–P2

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：使用微博和推特两个真实数据集，微博包含举报信息，推特无举报；为贴近现实使用不同不平衡比。

- rhetorical_function_cn：说明数据来源和评估场景。

- depends_on_cn：框架需要两类群体数据。

- sets_up_cn：为结果的外部有效性做设计。

- evidence_pointer：Emperical Evaluations: Datasets and Preprocessing

### 36. Datasets and Preprocessing P3

- order：36

- section：Emperical Evaluations

- locator：Datasets and Preprocessing P3

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：对回应进行标注，Cohen's kappa为0.816；表2显示假新闻的辟谣概率显著更高，支撑群体智能假设。

- rhetorical_function_cn：说明T2标注质量和人群判断差异。

- depends_on_cn：数据准备。

- sets_up_cn：为CAND有效性提供前提证据。

- evidence_pointer：Emperical Evaluations Table 1/2

### 37. Baseline Methods and Evaluation Metrics

- order：37

- section：Emperical Evaluations

- locator：Baseline Methods and Evaluation Metrics

- move_code：BENCHMARK_OR_CONTRAST

- paraphrase_cn：由于没有使用完全相同的输入组合的基准，设计端到端（Concat、HSA）和聚合（MV、BAM）两类基准，并按数据源逐步加入。

- rhetorical_function_cn：建立公平比较矩阵。

- depends_on_cn：框架创新点。

- sets_up_cn：让性能比较有依据。

- evidence_pointer：Baseline Methods and Evaluation Metrics

### 38. Evaluation Metrics paragraph

- order：38

- section：Emperical Evaluations

- locator：Evaluation Metrics paragraph

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：在不平衡数据下采用PR AUC为主指标，并更重视召回，因为实际场景中宁可牺牲部分精确率也要找出更多假新闻。

- rhetorical_function_cn：解释指标选择。

- depends_on_cn：不平衡评估。

- sets_up_cn：支撑后续结果解读。

- evidence_pointer：Evaluation Metrics paragraph

### 39. Experimental Procedure

- order：39

- section：Emperical Evaluations

- locator：Experimental Procedure

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：统一超参数调优、10次随机种子运行，控制响应收集一天，举报数截断20，用于早期检测评估。

- rhetorical_function_cn：描述实验控制。

- depends_on_cn：评估设计。

- sets_up_cn：保证结果可复现并衔接早期检测分析。

- evidence_pointer：Experimental Procedure

### 40. Figure 6a paragraph

- order：40

- section：False News Detection Performance

- locator：Figure 6a paragraph

- move_code：RESULT

- paraphrase_cn：CAND-123显著优于无群体智能的端到端基准，AUC从BERT的91.62%提高到97.54%；CAND-12仍优于全部基准。

- rhetorical_function_cn：提供核心性能主张。

- depends_on_cn：提取+聚合完成。

- sets_up_cn：证明群体智能价值。

- evidence_pointer：False News Detection Performance, Figure 6a

### 41. Figure 6b paragraph

- order：41

- section：False News Detection Performance

- locator：Figure 6b paragraph

- move_code：RESULT

- paraphrase_cn：CAND随数据源增加性能上升，而MV/BAM收益更小；CLNAM在所有数据源组合上优于聚合基准；与BAM的差距归因于逻辑斯蒂正态假设。

- rhetorical_function_cn：报告增量消融与聚合模型对比。

- depends_on_cn：基准矩阵。

- sets_up_cn：说明聚合模型和假设有效。

- evidence_pointer：Figure 6b

### 42. Figure 6c/6d paragraph

- order：42

- section：False News Detection Performance

- locator：Figure 6c/6d paragraph

- move_code：RESULT

- paraphrase_cn：在IR=1:7时HSA与CAND相当，但在IR=1:50时端到端模型精确率高但召回低，CAND全面胜出。

- rhetorical_function_cn：证明极端不平衡情形下的优势。

- depends_on_cn：基准结果。

- sets_up_cn：强化实用性。

- evidence_pointer：Figure 6c/6d

### 43. Figure 7 paragraph

- order：43

- section：False News Detection Performance

- locator：Figure 7 paragraph

- move_code：ROBUSTNESS_OR_BOUNDARY_TEST

- paraphrase_cn：随IR增大，CAND性能下降幅度更小、SEM更小，比基准更稳定。

- rhetorical_function_cn：检验不平衡条件下的稳健性。

- depends_on_cn：主结果。

- sets_up_cn：支持真实世界不平衡性下的适用性。

- evidence_pointer：Figure 7

### 44. Twitter results and split robustness paragraph

- order：44

- section：Appendix B2 and Robustness Checks

- locator：Twitter results and split robustness paragraph

- move_code：RESULT

- paraphrase_cn：推特数据集得到相同结论；随机/时间切分和k折/留一验证不改变结论。

- rhetorical_function_cn：跨平台复制与评估方案稳健性检验。

- depends_on_cn：微博结果。

- sets_up_cn：增强外部有效性。

- evidence_pointer：Appendix B2 and Section D1

### 45. Early Detection paragraph

- order：45

- section：Analysis and Discussion

- locator：Early Detection paragraph

- move_code：RESULT

- paraphrase_cn：以不同响应收集截止时间评估，CAND-12在最初几分钟已开始受益，一天内显著提升并稳定；约12小时到一天足够。

- rhetorical_function_cn：回答实际应用中的时效问题。

- depends_on_cn：框架需要群体数据。

- sets_up_cn：提出等待时间权衡和实时模式。

- evidence_pointer：Analysis and Discussion: Early Detection/Figure 8

### 46. Real-World Application paragraph

- order：46

- section：Analysis and Discussion

- locator：Real-World Application paragraph

- move_code：BOUNDARY_CONDITION

- paraphrase_cn：CAND不对新闻事件即时核实，而是等待一段时间收集群体智能；约12小时是必要取舍，也支持退化为CAND-1的实时检测。

- rhetorical_function_cn：界定实际使用条件。

- depends_on_cn：早期检测结果。

- sets_up_cn：让框架落地并防止误用。

- evidence_pointer：Real-World Application of CAND/Figure 9

### 47. Complementary Strengths paragraph

- order：47

- section：Analysis and Discussion

- locator：Complementary Strengths paragraph

- move_code：RESULT

- paraphrase_cn：单个判断源不总是主导，而是互补；可视化显示贝叶斯模型对每个帖子预测来源透明可解释。

- rhetorical_function_cn：支持人类-机器互补主张。

- depends_on_cn：聚合输出。

- sets_up_cn：展示可解释设计知识。

- evidence_pointer：Complementary Strengths of Humans and Machines/Figure 10

### 48. Value of Multiple Feature-Based Classifiers paragraph

- order：48

- section：Analysis and Discussion

- locator：Value of Multiple Feature-Based Classifiers paragraph

- move_code：RESULT

- paraphrase_cn：增加特征分类器数量提高CAND-12性能但边际递减；弱分类器不影响性能，因为模型会估计可信度并降低权重。

- rhetorical_function_cn：回答工程实用性问题。

- depends_on_cn：可信度建模。

- sets_up_cn：指导分类器数量选择。

- evidence_pointer：Value of Multiple Feature-Based Classifiers/Figure 11

### 49. Stress Testing paragraph

- order：49

- section：Analysis and Discussion

- locator：Stress Testing paragraph

- move_code：ROBUSTNESS_OR_BOUNDARY_TEST

- paraphrase_cn：即使误报率高达60%或假新闻举报率仅5%，CAND-123仍优于CAND-12，说明举报信息价值稳健。

- rhetorical_function_cn：检验部分模拟数据带来的不确定性。

- depends_on_cn：主结果的前置局限。

- sets_up_cn：回应用户举报可能受操纵的担忧。

- evidence_pointer：Stress Testing of Simulation Parameters/Figure 12

### 50. Sensitivity to News Characteristics paragraph

- order：50

- section：Analysis and Discussion

- locator：Sensitivity to News Characteristics paragraph

- move_code：ROBUSTNESS_OR_BOUNDARY_TEST

- paraphrase_cn：新闻长度增加提高性能，但包含群体智慧的CAND-12受长度影响更小；不同假新闻类型上模型表现有差异。

- rhetorical_function_cn：界定边界条件。

- depends_on_cn：检测性能。

- sets_up_cn：说明群体智慧降低对内容特征的依赖并提示类型敏感。

- evidence_pointer：Sensitivity to News Characteristics/Figure 13

### 51. Robustness to Intentional Manipulation paragraph

- order：51

- section：Analysis and Discussion

- locator：Robustness to Intentional Manipulation paragraph

- move_code：ROBUSTNESS_OR_BOUNDARY_TEST

- paraphrase_cn：模拟六种恶意用户操控回应，CAND-12相比CAND-1不脆弱，整合回应至少不损害检测；举报操纵也在合理范围内稳健。

- rhetorical_function_cn：应对对抗攻击。

- depends_on_cn：系统威胁。

- sets_up_cn：强化抗操纵主张。

- evidence_pointer：Robustness to Intentional Manipulation

### 52. Multiclass Classification paragraph

- order：52

- section：Analysis and Discussion

- locator：Multiclass Classification paragraph

- move_code：ROBUSTNESS_OR_BOUNDARY_TEST

- paraphrase_cn：将辟谣回应检测扩展为多分类时，E-CAM与CAND相当且优于CAM，说明逻辑斯蒂正态假设重要，多分类收益有限。

- rhetorical_function_cn：检验替代建模选择。

- depends_on_cn：核心模型。

- sets_up_cn：证明模型选择不是随意。

- evidence_pointer：Debunking Response Detection as a Multiclass Classification Problem

### 53. Dataset Bias paragraph

- order：53

- section：Analysis and Discussion

- locator：Dataset Bias paragraph

- move_code：CONTRIBUTION

- paraphrase_cn：讨论标注偏差和选择偏差，并在在线附录中说明缓解措施。

- rhetorical_function_cn：回应公平性议题。

- depends_on_cn：数据构建。

- sets_up_cn：保护贡献不被偏差质疑。

- evidence_pointer：Dataset Bias

### 54. Conclusion P1

- order：54

- section：Conclusion

- locator：Conclusion P1

- move_code：CONTRIBUTION

- paraphrase_cn：相比黑箱端到端模型，CAND性能更好、更可解释、能产生多种技术洞察且易于扩展。

- rhetorical_function_cn：总结三大优势。

- depends_on_cn：全文证据。

- sets_up_cn：回应引言中的缺口。

- evidence_pointer：Conclusion P1

### 55. Conclusion P2

- order：55

- section：Conclusion

- locator：Conclusion P2

- move_code：CONTRIBUTION

- paraphrase_cn：理论贡献在于展示可扩展群体判断的价值和人类-机器互补，并为混合系统中人类和机器可信度建模。

- rhetorical_function_cn：上升到理论贡献。

- depends_on_cn：经验结果。

- sets_up_cn：为混合智能文献提供一般化结论。

- evidence_pointer：Conclusion P2

### 56. Conclusion P3

- order：56

- section：Conclusion

- locator：Conclusion P3

- move_code：PRACTICAL_STAKES

- paraphrase_cn：为平台和用户提供可行建议，包括鼓励用户举报/回应、为不支持举报的平台设计该功能。

- rhetorical_function_cn：转化实践含义。

- depends_on_cn：贡献总结。

- sets_up_cn：说明设计知识可用于实践。

- evidence_pointer：Conclusion P3

### 57. Conclusion P4

- order：57

- section：Conclusion

- locator：Conclusion P4

- move_code：LIMITATION_AND_FUTURE

- paraphrase_cn：局限包括未报告帖子可能包含漏检假新闻、微博警告标签造成隐含真实效应、未按用户可靠性加权、仅使用两类群体智能。

- rhetorical_function_cn：诚实地限制贡献范围。

- depends_on_cn：全文方法。

- sets_up_cn：为未来研究留出空间。

- evidence_pointer：Conclusion P4

## 写作技术

- gap_construction_cn：先承认机器智能的有限性，再指出人类智能在可扩展性上的瓶颈，并用‘回应与举报未被高效利用’与‘现有聚合模型只处理单一来源’两个技术缺口共同构造研究空间；同时用一个真实微博例子把抽象缺口具象化。

- signposting_cn：摘要直接预告框架与结果；引言末尾给出全文组织；每节开头用综述句或‘Recall that’等路标；结果部分反复以图表编号指示证据位置；在分析部分用单独小标题标记每个稳健性问题。

- transition_logic_cn：从社会问题进入理论与相关工作的综述，再由文献限制过渡到框架设计；框架内部从提取到聚合到推断逐层深入；结果部分从主性能转向不平衡稳健性，再进入实际应用与边界条件，最后到结论；每个分析小问题都由前面遗留的不确定性或实际需求触发。

- claim_evidence_rhythm_cn：每提出一个性能或设计主张，紧接引用图表的具体数值或对比；增量消融和基准矩阵用同一组指标反复收敛；稳健性主张放在主结果之后，用压力测试和模拟操控提供证据；贡献段落再回扣这些证据。

- benchmark_narrative_cn：将基准方法按数据源和方法类型组织成表格（Table 3），先说明不存在完全相同的基准，再设计端到端和聚合两类对照；通过逐步加入数据源和不同IR把benchmark变成可解释的消融与压力叙事。

- theory_return_cn：结果不是停留在‘我们更好’，而是回到在线去抑制与智慧众：辟谣概率差异、互补贡献图、早期检测和抗操纵都被解释为群体智慧在混合系统中的具体表现；逻辑斯蒂正态假设也用经验分布和与BAM的对比重新辩护。

- contribution_positioning_cn：以‘不同于黑箱特征处理’和‘现有聚合只涉及单一来源’来定位新意；贡献分层为方法性能、可解释结构、混合可信度建模和设计原则，避免只宣称性能提升。

- novelty_protection_cn：通过跨平台复制、多种IR、时间切分/交叉验证、压力测试、操纵模拟、敏感性和多分类扩展，把可能被看作一次性性能优势的结果转译为稳健的边界条件和设计知识；同时在限制中承认数据模拟等弱点，防止过度主张被击穿。

## 可复用研究与写作程序

### structure_steps

#### 1. 1

- step：1

- writing_job_cn：用现实危害数据打开问题，说明不解决的社会/经济后果。

- research_job_cn：明确目标问题域，并收集可信的宏观证据。

- required_evidence_cn：至少有一条可靠的现实后果或统计事实。

- transition_to_next_cn：从‘问题严重’过渡到‘现有方法不足’。

#### 2. 2

- step：2

- writing_job_cn：综述现有技术/学术应对，突出对某一类可获取但未充分利用信息的忽视。

- research_job_cn：识别特定数据源或能力缺口，最好配一个真实例子。

- required_evidence_cn：能展示缺口存在且实际可观察的案例或文献对比。

- transition_to_next_cn：从缺口引出研究问题。

#### 3. 3

- step：3

- writing_job_cn：把一般缺口转化为可研究的问题，并引入支撑理论或知识基础。

- research_job_cn：选择能解释数据来源行为机制的理论（如智慧众、心理学效应），并说明如何从个体行为到聚合价值。

- required_evidence_cn：理论命题与所用数据现象之间有可辩护的逻辑链。

- transition_to_next_cn：从理论命题走向设计需求。

#### 4. 4

- step：4

- writing_job_cn：将理论命题转化为设计要求和具体制品特征。

- research_job_cn：设计信息提取/聚合的整体架构，并说明每个组件应对哪个挑战。

- required_evidence_cn：每个设计选择能对应一个明确挑战或需求。

- transition_to_next_cn：从架构进入模型形式化。

#### 5. 5

- step：5

- writing_job_cn：描述模型/算法的生成过程、推断方式和先验/超参数处理。

- research_job_cn：实现可计算的模型，选择可扩展高效的推断算法。

- required_evidence_cn：模型可运行并能输出最终预测；若有关键假设，应有初步经验证据。

- transition_to_next_cn：从构建进入评价设计。

#### 6. 6

- step：6

- writing_job_cn：设计评价矩阵：数据集、基准、指标、对照和消融。

- research_job_cn：确定能证明数据源增量和聚合模型价值的基准组合与指标。

- required_evidence_cn：有多个维度（如端到端/聚合）和增量数据源组合；指标适合不平衡场景。

- transition_to_next_cn：从评价设计到主结果呈现。

#### 7. 7

- step：7

- writing_job_cn：报告主结果和稳健性/边界分析，逐一回应可能威胁。

- research_job_cn：执行跨数据集、不平衡比、早期时间窗口、压力测试、敏感性、操纵模拟等额外分析。

- required_evidence_cn：至少有一种稳健性检验覆盖数据、时间、参数或对抗威胁。

- transition_to_next_cn：从具体结果上升到贡献和设计知识。

#### 8. 8

- step：8

- writing_job_cn：在结论中回扣引言缺口，分层声明贡献并诚实列出局限。

- research_job_cn：提炼可复用设计知识、理论贡献和实践建议。

- required_evidence_cn：结论中的每一类贡献都能在前文找到对应证据。

- transition_to_next_cn：结束全文并指出未来研究方向。

### most_transferable_moves_cn

1. 用宏观危害数据开篇，快速建立现实紧迫性

2. 以一个真实平台例子把抽象数据源具象化

3. 将理论命题直接映射为数据源选择与聚合要求

4. 设计‘基础分类器—端到端融合—聚合模型’的分层基准矩阵

5. 用增量加入数据源的消融把性能提升归因到具体设计

6. 用不平衡比、截止时间、压力测试、敏感性、操纵模拟组成稳健性叙事

7. 可解释贡献可视化把‘性能好’转化为‘设计知识’

8. 结论中分层声明技术、制品、机制、边界和理论贡献

### resource_intensive_or_nonstandard_parts_cn

1. 需要真实社交平台上的假/真新闻语料、回应和举报数据，且举报数据在部分平台不可得

2. 微博举报数据在论文中部分模拟，无法轻易获得完整真实举报带时间戳数据

3. T2辟谣回应检测需要人工标注，标注成本和一致性管理较高

4. 训练SVM/CNN/LSTM/Bi-LSTM/BERT等多种深度模型并进行网格搜索需要较大计算资源

5. 跨平台数据（微博和推特）的获取、清洗、事件聚类和字段对齐极为耗时

6. 对恶意操纵的模拟、多分类扩展和偏差缓解依赖大量在线补充实验

### what_not_to_copy_superficially_cn

1. 不要在没有群体判断数据时宣称使用了群体智慧

2. 不要在未做增量消融时把性能优势归因于人类智能

3. 不要轻易采用逻辑斯蒂正态假设而没有经验分布或与二项假设的对照

4. 不要用模拟举报数据直接宣称真实举报价值，必须做压力测试并承认局限

5. 不要把‘可解释’停留在口头，应有贡献分解或机制可视化

6. 不要宣称抗操纵却只给主benchmark，缺乏操纵模拟

- single_best_description_of_the_routine_cn：用真实平台可观察的群体行为作为可扩展智能源，通过可解释贝叶斯聚合把人类与机器判断融合，再用跨平台、不平衡、渐进式与对抗式评价把一次性性能提升转化为设计知识。

## 分析边界

全文主体可读，但许多附录（B1/B2、C、D等）和在线补充细节未完整提供，多分类、偏差缓解和部分稳健性分析依赖这些附录；文章没有页码，位置以段落和图表为据；正文中部分公式符号因OCR可能不完整；无法核验附录中隐含的统计显著性和全部实验设置。
