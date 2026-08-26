# Augmenting Social Bot Detection with Crowd-Generated Labels

- 作者：Victor Benjamin; T. S. Raghu
- 年份 / 期刊：2023 / Information Systems Research
- DOI：10.1287/isre.2022.1136
- 源文件：28480_2023_augmenting-social-bot-detection-with-crowd-generated-labels.md
- 论文主类型：build_evaluate_design_science
- 主导写作弧线：problem_theory_design_test_return
- 置信度：0.83

## 文章级论证概况

- 核心问题：如何利用真实社交媒体用户对疑似社交机器人的回复（众包标签），并借助言语行为理论衡量这些回复的可信度，从而增强传统社交机器人检测系统的性能？

- 制品与设计：作者构建了一个融合人类认知与机器计算的社交机器人检测框架：先从Reddit众包举报列表筛选高置信机器人账号，提取机器人与人类之间的回复关系；再用BERT等深度学习方法分别生成话题、情感、言语行为、语义和时间相似性特征；最后把众包反应特征与传统语义和时间相似性特征合并，训练多个分类器识别机器人账号。

- 客观结果：在Reddit真实数据集上，增强模型显著优于仅用传统特征的模型（随机森林宏F1从0.407提升到0.805）；消融实验显示去掉言语行为特征会使宏F1从0.805降至0.774；时间模拟显示增强模型在50条消息时检测率达81%，而传统模型为64%；在2019年新出现的机器人测试中，增强模型性能损失远小于传统模型。

- 核心贡献：作者声称这是首个在社交机器人检测中系统使用众包反应（人类回复）作为特征的研究，也是首次将言语行为理论用于评估众包标签的可信度；研究证明了众包反应能显著增强检测性能，而言语行为能够进一步带来适度提升，并提供了面向长文本平台和真实世界部署的设计知识。

- 整篇论证链：作者从社交机器人泛滥和人类用户能够识别机器人这一现实现象出发，指出现有检测文献几乎只分析机器人自身消息，忽略了对机器人消息的人类回复，而常用benchmark数据也缺少回复关系。为填补该缺口，他们以言语行为理论为知识基础，将用户回复按意图分类以衡量其识别机器人的确定性，并把这个理论构念转化为可计算的话题、情感、言语行为特征；随后在真实Reddit众包数据集上构建并评价了传统与增强两种检测模型。通过分类对比、消融、时间模拟、标签数量模拟和新时期机器人稳健性测试，作者证明众包反应可大幅提升检测性能，言语行为可适度增强性能。最后，作者把结果上升为可复用的设计知识：未来机器人检测应考虑加入众包反应，言语行为可作为评估众包标签确定性的机制，并指出部署与更新路径。

## 类型与写作弧线判定

- 论文主类型判定：文章的核心不是检验某个先验理论假设，而是提出一个融合众包反应与深度学习的社会机器人检测框架/系统，并在真实世界数据集上评价其性能、稳健性和实用性。作者在引言和讨论中明确援引设计科学研究呼吁，围绕需求、构建、评价、设计知识展开，符合设计科学制品—评价范式。

- 主导写作弧线判定：文章以现实问题（社交机器人操纵话语）开篇，引入言语行为理论作为衡量众包反应可信度的理论工具，再将其操作化为话题、情感、言语行为特征和最终分类器，通过多个实验检验设计，最后在讨论中回到理论贡献与可复用设计知识，形成问题—理论—设计—检验—回返理论的写作弧线。

## 研究开展程序

- study_or_phase_count：9

- 研究阶段总序列：研究依次完成：真实数据与回复关系的构建；三种人类认知特征分类器（话题、情感、言语行为）的独立开发与选择；传统机器检测特征的构建；最终增强分类器与传统分类器的对比及消融；部署相关的时间与标签数量模拟；面对更新机器人的稳健性测试；与既有文献的benchmark对照。每个阶段都建立在前一阶段产物之上：数据阶段提供语料，文本分类阶段提供特征，传统阶段提供基线，对比阶段提供核心证据，模拟与稳健性阶段把证据扩展到真实部署，benchmark阶段把结论嵌入文献脉络。

### studies_or_phases

#### 1. 数据收集与人机回复关系提取

- order：1

- name_cn：数据收集与人机回复关系提取

- question_cn：能否从真实社交媒体平台上的众包举报列表构建一个包含人类回复关系的高质量社交机器人检测测试场？

- inputs_and_setting_cn：Reddit平台、r/BotWatchman众包机器人列表、Reddit公共API；收集2016–2018年数据。

- designed_or_compared_object_cn：筛选出被举报10次以上的777个机器人账号作为ground truth；提取146,639条机器人消息、58,070条人类回复；按93.5%人类活动比例抽取195,291个非机器人账号及其消息，并收集对照回复。

- baseline_control_or_counterfactual_cn：非机器人账号消息和人类对非机器人消息的回复作为对照语料。

##### objective_metrics

1. 账号数

2. 消息数

3. 词长范围与均值

4. 举报次数阈值

- analysis_method_cn：公开API数据抓取、回复关系匹配、时间顺序80/20划分、防特征泄漏处理。

- main_result_cn：成功构建包含777个高置信机器人大账号和大量人类回复的Reddit数据集。

- argumentative_role_cn：为后续所有众包反应特征提供数据基础，把“用户会自然回复并指出机器人”这一现象转化为可计算的数据结构。

- remaining_uncertainty_cn：众包列表可能存在误报；假设机器人之间不互相回复；数据仅为Reddit平台。

- link_to_next_phase_cn：把回复语料交给话题、情感、言语行为分类器，生成人类认知特征。

##### evidence_pointers

1. Section 4.1

2. Table 3

3. Figure 2

#### 2. 话题分类：识别用户是否在指出机器人活动

- order：2

- name_cn：话题分类：识别用户是否在指出机器人活动

- question_cn：能否用监督文本分类判断人类回复是否在讨论/指出机器人活动？

- inputs_and_setting_cn：2,000条标注回复（1,000条相关、1,000条不相关），来自622个训练机器人账号收到的回复。

- designed_or_compared_object_cn：比较BERT、BiLSTM、LSTM、RNN、SVM五类模型。

- baseline_control_or_counterfactual_cn：SVM与传统RNN/LSTM作为弱基线。

##### objective_metrics

1. Precision

2. Recall

3. F1

4. AUC

5. Standard error

- analysis_method_cn：人工标注、平衡类训练、10折交叉验证。

- main_result_cn：BERT最优，F1=0.959。

- argumentative_role_cn：生成最终特征矩阵中的Bot Topic比例特征，即“多少回复明确指出机器人活动”。

- remaining_uncertainty_cn：训练类平衡但真实世界类不平衡；话题分类无法衡量回复者确定性。

- link_to_next_phase_cn：相同标注和BERT流程扩展到情感与言语行为分类。

##### evidence_pointers

1. Section 4.2.3

2. Table 4

#### 3. 情感分类：计算回复中的正/负/中性情感

- order：3

- name_cn：情感分类：计算回复中的正/负/中性情感

- question_cn：人类回复疑似机器人消息时的情感极性能否作为有效特征？

- inputs_and_setting_cn：3,000条标注回复，正/中/负各1,000条，只从已知机器人的回复中抽样。

- designed_or_compared_object_cn：比较BERT、BiLSTM、LSTM、RNN、SVM五类模型。

- baseline_control_or_counterfactual_cn：SVM与传统RNN/LSTM作为弱基线。

##### objective_metrics

1. Precision

2. Recall

3. F1

4. AUC

5. Standard error

- analysis_method_cn：人工标注、10折交叉验证、平衡训练。

- main_result_cn：BERT最优，F1=0.914。

- argumentative_role_cn：把人类对机器人的情感反应转化为正/负/中性比例特征，补充话题分类不能捕捉的情绪信号。

- remaining_uncertainty_cn：情感极性不等于可信度；消极情感可能来自正常争论而非机器人识别。

- link_to_next_phase_cn：言语行为分类进一步捕捉用户在回复中的意图和确定性。

##### evidence_pointers

1. Section 4.2.4

2. Table 4

#### 4. 言语行为分类：衡量众包反应的可信度

- order：4

- name_cn：言语行为分类：衡量众包反应的可信度

- question_cn：能否利用言语行为理论对用户回复进行分类，从而计算众包反应识别机器人的确定性？

- inputs_and_setting_cn：2,500条标注回复，覆盖Searle五类言语行为各500条，来自对已知机器人的回复。

- designed_or_compared_object_cn：比较BERT、BiLSTM、LSTM、RNN、SVM五类模型。

- baseline_control_or_counterfactual_cn：SVM与传统RNN/LSTM作为弱基线；另将识别出机器人的回复与未识别出机器人的回复进行言语行为分布比较。

##### objective_metrics

1. Precision

2. Recall

3. F1

4. AUC

5. Standard error

6. 言语行为分布

- analysis_method_cn：人工标注、10折交叉验证、BERT分类后对全量回复打标签。

- main_result_cn：BERT最优，F1=0.865；表达类最多，断言类其次；成功识别机器人的回复在言语行为分布上与普通回复显著不同。

- argumentative_role_cn：把Searle言语行为理论操作化为五个言语行为比例特征，作为众包反应可信度的代理。

- remaining_uncertainty_cn：言语行为特征是否真正提升最终机器人检测性能仍未验证。

- link_to_next_phase_cn：把话题、情感、言语行为三类人类认知特征并入最终特征矩阵。

##### evidence_pointers

1. Section 4.2.5

2. Table 4

3. Online Appendix A2

#### 5. 传统计算特征：语义与时间相似性基线

- order：5

- name_cn：传统计算特征：语义与时间相似性基线

- question_cn：不使用众包反应时，基于机器人自身消息的语义信息和时间重复性在Reddit长文本上能提供怎样的基线？

- inputs_and_setting_cn：已知777个机器人的消息与195,291个非机器人账号的消息。

- designed_or_compared_object_cn：账号级BERT语义嵌入；消息间平均余弦相似度作为时间相似性特征。

- baseline_control_or_counterfactual_cn：该模块构成传统检测模型的特征集。

##### objective_metrics

1. 无独立指标；由最终分类器输出Precision/Recall/F1/AUC

- analysis_method_cn：BERT账号级嵌入、余弦相似度计算。

- main_result_cn：形成传统机器人检测特征，作为与增强模型对比的基线。

- argumentative_role_cn：复现现有文献的主流检测思路，使后续“众包反应带来提升”的结论具有对照基础。

- remaining_uncertainty_cn：传统特征单独在Reddit上的性能很低，需要验证众包特征的增量价值。

- link_to_next_phase_cn：与传统特征和众包特征共同构成特征矩阵，运行传统 vs 增强分类实验。

##### evidence_pointers

1. Section 4.3

2. Section 4.4.1

3. Table 5

#### 6. 最终分类器对比与消融实验

- order：6

- name_cn：最终分类器对比与消融实验

- question_cn：加入众包反应特征后，机器人账号分类性能是否显著提升？言语行为特征是否贡献了额外性能？

- inputs_and_setting_cn：777个机器人与195,291个非机器人账号的特征矩阵；表5中的Bot Topic、情感、言语行为、时间相似性、BERT语义向量。

- designed_or_compared_object_cn：随机森林、决策树、逻辑回归、SVM、朴素贝叶斯五类分类器；比较传统模型与增强模型；对话题、情感、言语行为做消融。

- baseline_control_or_counterfactual_cn：仅用传统特征（语义+时间相似性）的模型；去掉话题/情感/言语行为的缩减模型。

##### objective_metrics

1. Precision(bot class)

2. Recall(bot class)

3. Macro-F1

4. Micro-F1

5. AUC

6. Standard error

- analysis_method_cn：特征矩阵构建、五类分类器训练、消融分析。

- main_result_cn：增强模型在所有分类器上大幅提升；随机森林宏F1从0.407提高到0.805；去掉言语行为使宏F1降到0.774，去掉话题降到0.745，去掉情感则几乎不变。

- argumentative_role_cn：提供核心证据：众包反应确实增强检测，言语行为带来适度但可观的增量。

- remaining_uncertainty_cn：平均指标无法回答“多快能检测”和“需要多少标签”。

- link_to_next_phase_cn：通过时间与标签数量模拟展示部署可行性。

##### evidence_pointers

1. Section 4.4.1

2. Table 6

3. Table 7

4. Online Appendix A3

#### 7. 时间-检测与标签数量模拟

- order：7

- name_cn：时间-检测与标签数量模拟

- question_cn：新机器人发布多少条消息或被多少用户标签后，系统能够检测出来？

- inputs_and_setting_cn：测试集中的机器人账号；按消息数量10/25/50阈值和众包标签数量1/5/10阈值触发评估。

- designed_or_compared_object_cn：传统模型与增强模型在同一触发条件下比较。

- baseline_control_or_counterfactual_cn：传统模型虽然同时被触发，但不把众包标签作为输入。

##### objective_metrics

1. 检测出的已知机器人百分比

- analysis_method_cn：模拟在线检测流程，在不同累积信息量下评估检测率。

- main_result_cn：增强模型在50条消息时检测81%，传统模型64%；在10个标签时检测78%，传统模型59%。

- argumentative_role_cn：把分类性能转化为真实世界中的早期检测能力，强化系统实用性和部署价值。

- remaining_uncertainty_cn：模拟仍基于历史数据，未做真实在线部署。

- link_to_next_phase_cn：用更晚出现的机器人检验系统是否会因机器人进化而过时。

##### evidence_pointers

1. Section 4.4.2

2. Table 8

3. Table 9

#### 8. 对更新/更高级机器人的稳健性测试

- order：8

- name_cn：对更新/更高级机器人的稳健性测试

- question_cn：面对2019年后出现、可能具有更强反检测能力的机器人，已训练模型是否仍然有效？

- inputs_and_setting_cn：2019年下半年创建的260个机器人，23,574条消息、5,592条回复；同时间窗口随机收集362,667条非机器人消息。

- designed_or_compared_object_cn：把主实验中训练好的传统模型与增强模型直接应用到新数据集上；比较精度/召回率相对变化。

- baseline_control_or_counterfactual_cn：主实验中的原始性能作为基准。

##### objective_metrics

1. Precision(bot class)

2. Recall(bot class)

3. Percentage change in precision

4. Percentage change in recall

- analysis_method_cn：复现相同特征矩阵构建流程，重新评估模型。

- main_result_cn：增强模型性能损失很小（随机森林精度-3.44%，召回-3.636%），传统模型损失更大（精度-8.78%，召回-11.299%）。

- argumentative_role_cn：提供边界与稳健性证据：众包反应可以帮助系统在机器人进化时保持检测力。

- remaining_uncertainty_cn：没有检验机器人故意发布虚假举报的策略；也没有通过重训练来进一步改进。

- link_to_next_phase_cn：通过文献benchmark把结果与已有方法对齐。

##### evidence_pointers

1. Section 4.4.3

2. Table 10

#### 9. 文献benchmark与可迁移性评估

- order：9

- name_cn：文献benchmark与可迁移性评估

- question_cn：本文方法与已有文献中的方法/基准数据集相比表现如何？

- inputs_and_setting_cn：Cresci et al. (2017) Twitter数据集；Garcia-Silva et al. (2019)报告的结果；Varol et al. (2017)特征列表。

- designed_or_compared_object_cn：用相同BERT配置比较；尝试加入时间相似性和话题检测后的增量；评估Varol特征在Reddit上的可移植性。

- baseline_control_or_counterfactual_cn：Garcia-Silva等人的BERT基线。

##### objective_metrics

1. F1

2. 特征可移植数量

- analysis_method_cn：在Cresci数据上运行BERT与传统特征；尝试部分实现Varol特征。

- main_result_cn：BERT基线与文献相当，加入两个可移植特征后略有提升；由于Cresci数据没有回复，无法benchmark众包反应特征；Varol的63类特征中仅约33类可在Reddit实现，因此放弃不完全对比。

- argumentative_role_cn：把本文方法嵌入现有文献，同时说明众包反应特征无法用旧benchmark评价的原因是旧数据缺少回复，反过来强化数据贡献。

- remaining_uncertainty_cn：没有在统一标准下与其他众包反应方法比较，因为不存在同类方法。

- link_to_next_phase_cn：进入讨论与结论，把局部性能上升为理论贡献和设计知识。

##### evidence_pointers

1. Section 4.4.4

2. Online Appendix A6

## 各部分修辞架构

### abstract_moves

1. CONTEXT: 社交平台面临社交机器人操纵在线话语

2. PHENOMENON: 一些用户能以不同程度信心识别社交机器人

3. THEORY_INTRO: 言语行为理论启发评估用户识别可信度的框架

4. REQUIREMENT: 并非所有用户反应对检测任务同等可信

5. DESIGN_FEATURE: 用深度学习方法操作化框架为计算系统

6. BENCHMARK_OR_CONTRAST: 在真实众包数据集上证明性能提升

7. RESULT: 考虑众包反应显著提升检测性能；言语行为可进一步适度提升

8. CONTRIBUTION: 为检测其他算法生成内容提供基础

### introduction_moves

1. CONTEXT: 社交媒体广泛覆盖吸引网络对手

2. PRACTICAL_STAKES: 机器人放大攻击并淹没真实用户声音

3. PHENOMENON: 越来越多用户能识别并指出机器人

4. LIMITATION: 现有文献缺少对这种人机互动的分析

5. GAP: 尚未利用人类回复中的认知信号增强检测

6. WHY_GAP_MATTERS: 机器人持续进化，需要新特征

7. RQ_OR_OBJECTIVE: 用真实用户反应增强传统检测

8. THEORY_INTRO: 用言语行为理论衡量用户反应可信度

9. CONTRIBUTION: 首次在检测中使用众包反应并评估其确定性

### theory_and_knowledge_moves

1. PRIOR_KNOWLEDGE: 社交机器人可占某些平台5%-8%用户并从事恶意行为

2. PRIOR_KNOWLEDGE: 现有检测主要依靠内容、网络和时间同步性特征

3. LIMITATION: 多数研究集中于Twitter/短文本并依赖Cresci数据集

4. GAP: Cresci数据缺少会话级回复，不能用于众包反应研究

5. THEORY_INTRO: Searle五类言语行为提供意图分类

6. MECHANISM: 断言/宣告类比提问/请求类具有更强确定性

7. LIMITATION: RSA等理论依赖听者解释，难以扩展到社交媒体大规模异质网络

### artifact_design_moves

1. REQUIREMENT: 需要判断用户回复是否在识别机器人

2. DESIGN_FEATURE: 话题分类生成Bot Topic比例

3. DESIGN_FEATURE: 情感分类生成正/负/中性比例

4. DESIGN_FEATURE: 言语行为分类生成五类意图比例

5. DESIGN_FEATURE: 传统模块使用BERT账号级语义嵌入和时间相似性

6. DESIGN_FEATURE: 最终特征矩阵合并所有特征

7. METHOD_JUSTIFICATION: 用BERT而非RNN处理长文本以避免梯度消失

### evaluation_moves

1. BENCHMARK_OR_CONTRAST: 传统模型 vs 增强模型

2. BENCHMARK_OR_CONTRAST: 多分类器对比

3. ROBUSTNESS_OR_BOUNDARY_TEST: 消融话题/情感/言语行为

4. ROBUSTNESS_OR_BOUNDARY_TEST: 时间-检测模拟

5. ROBUSTNESS_OR_BOUNDARY_TEST: 标签数量模拟

6. ROBUSTNESS_OR_BOUNDARY_TEST: 对新时期机器人测试

7. BENCHMARK_OR_CONTRAST: 与Cresci/Garcia-Silva基准对比

### discussion_and_contribution_moves

1. CONTRIBUTION: 众包反应与言语行为首次结合

2. CONTRIBUTION: 系统易于部署到现有平台

3. PRACTICAL_STAKES: 机器人问题与虚假信息、平台责任相关

4. LIMITATION_AND_FUTURE: 延迟检测、无法检测未被人类识别的机器人

5. LIMITATION_AND_FUTURE: 个性偏差与虚假举报策略

6. BOUNDARY_CONDITION: 适用于用户能够识别的机器人；依赖众包标签质量

7. CONTRIBUTION: 为未来研究提供新数据集和新方向

## 理论/知识到设计的翻译

### 知识/理论基础

1. 言语行为理论（Searle 1969）：语言用于完成特定行为，可分类为断言、承诺、宣告、指令、表达

2. 社交机器人检测文献：机器人表现出高频、同步、重复行为，内容分析可识别

3. 社交媒体分析/NLP：话题分析和情感分析可量化文本内容，BERT等预训练模型适合长文本

4. 众包标注文献：众包标签可显式或隐式生成，但不同标签可信度不同

- 理论—设计耦合：partial

- 耦合判定理由：言语行为理论直接影响了“众包反应可信度”这一核心问题的定义，并决定了最终特征矩阵中加入五类言语行为比例特征；但系统的大部分技术选择（BERT、账号级语义嵌入、时间相似性、话题与情感分类）来自NLP与机器人检测文献的工程启发，而非言语行为理论推导。消融实验也表明言语行为不是性能提升的必要条件，因此属于理论部分影响设计。

- 理论到设计翻译链：言语行为理论主张每条话语都在执行某种行为→用户回复机器人时，其意图可能是断言、宣告、指令、表达或承诺→不同意图暗示不同确定性→需要把回复按言语行为分类并加权→设计出话题/情感/言语行为三类人类认知特征→与语义和时间相似性传统特征合并成特征矩阵→通过传统vs增强、消融、时间模拟等实验检验。

### mapping_table

#### 1. 1

- theory_or_knowledge_claim_cn：Searle言语行为理论：语言表达可依据说话者意图分为断言、承诺、宣告、指令、表达五类；不同言语行为承载不同程度的确定性与行动意图。

- mechanism_cn：用户在回复疑似机器人时，宣告式“这是机器人”比指令式/疑问式“这是机器人吗？”表达更强确定性；表达式和指令式可能置信度较低。

- design_requirement_cn：不能把所有用户回复等同视为标签，需要按言语行为量化可信度并把可信度输入检测模型。

- artifact_choice_cn：训练BERT言语行为分类器，把每条回复归入五类之一；最终以每类所占比例作为账号特征SA1-SA5。

- evaluated_contrast_cn：完整增强模型 vs 去掉言语行为特征的增强模型；以及每个言语行为分别作为特征的表现。

- objective_result_cn：去掉言语行为使随机森林宏F1从0.805降至0.774；言语行为提供适度但一致的增量提升。

##### evidence_pointers

1. Section 4.2.5

2. Section 4.4.1

3. Table 7

4. Online Appendix A3

#### 2. 2

- theory_or_knowledge_claim_cn：社交机器人往往高同步、重复地发布相似内容，因此消息间时间相似性可作为检测信号。

- mechanism_cn：机器人账号内容重复度高，人类账号内容多样；平均余弦相似度可量化这种差异。

- design_requirement_cn：传统检测模块应捕捉账号内容的时间重复性。

- artifact_choice_cn：对同一账号消息两两计算余弦相似度并取平均，作为时间相似性特征。

- evaluated_contrast_cn：传统模型（语义+时间相似性） vs 增强模型（加入众包反应）。

- objective_result_cn：仅用传统特征时随机森林宏F1为0.407；增强后为0.805。

##### evidence_pointers

1. Section 4.3.2

2. Table 6

#### 3. 3

- theory_or_knowledge_claim_cn：众包标签已有成功应用，且可以通过观察自然使用系统而隐式产生。

- mechanism_cn：社交媒体用户自然回复疑似机器人时，其内容本身就是一种隐式众包标签；不同用户识别能力不同，因此标签可信度各异。

- design_requirement_cn：把自然发生的用户回复作为弱标签，并用话题、情感、言语行为等多维特征衡量其质量。

- artifact_choice_cn：从回复语料中提取“Bot Topic”比例、情感比例和言语行为比例，替代显式众包标注。

- evaluated_contrast_cn：传统模型 vs 增强模型；不同众包标签数量阈值。

- objective_result_cn：增强模型大幅提升；标签从1个增至10个时检测率从53%升至78%，而传统模型仅从48%升至59%。

##### evidence_pointers

1. Section 2.1

2. Section 4.4.1

3. Table 9

#### 4. 4

- theory_or_knowledge_claim_cn：BERT等Transformer适合长文本，不会像RNN一样因梯度消失而丢失前文信息。

- mechanism_cn：Reddit消息可远长于Twitter，RNN处理长序列会性能下降；BERT可以处理更长输入。

- design_requirement_cn：文本表征模型应选择支持长输入的深度学习架构。

- artifact_choice_cn：采用HuggingFace BERT作为所有文本分类和语义嵌入的骨干模型。

- evaluated_contrast_cn：BERT vs BiLSTM/LSTM/RNN/SVM在话题、情感、言语行为三类分类任务上的表现。

- objective_result_cn：BERT在三类任务上F1均最高（0.959、0.914、0.865）。

##### evidence_pointers

1. Section 4.2.2

2. Table 4

## 评价逻辑

### evaluation_modes

1. 多分类器对比：在同一特征矩阵上比较随机森林、决策树、逻辑回归、SVM、朴素贝叶斯，避免结论依赖单一模型

2. 增量对比：传统特征 vs 传统+众包反应特征

3. 消融分析：分别去掉话题、情感、言语行为特征，检验每个特征集的贡献

4. 时间-检测模拟：在新机器人累积10/25/50条消息时触发检测，评估早期检测率

5. 标签数量模拟：在新机器人获得1/5/10个众包标签时触发检测，评估标签数量效应

6. 时间外稳健性测试：用2019年新出现的机器人测试既有模型，评估性能退化

7. 文献benchmark：在Cresci数据集上对比Garcia-Silva等结果，验证基础模型与可移植特征

- why_these_evaluations_cn：单一分类准确率不足以支持“众包反应增强检测”的贡献，还需要证明增量来自众包反应、言语行为是否必要、系统能否早期部署、面对进化机器人是否稳健，以及结果与既有文献的可比性。因此作者用传统vs增强回答核心问题，用消融回答机制来源，用模拟回答实用性，用新数据回答稳健性，用benchmark回答外部效度。

- benchmark_and_contrast_chain_cn：作者先以传统语义和时间相似性模型作为弱基线；再加入众包反应形成增强模型，显示大幅提升；随后通过消融把提升拆解为话题、情感和言语行为各自的贡献；接着把静态分类提升转化为消息数/标签数维度的检测率；再用2019年新机器人作为时间外数据验证稳健性；最后尝试与Cresci/Garcia-Silva基准对比，说明众包反应特征因旧数据缺少回复而无法直接benchmark，从而把缺少回复的数据集重新定义为文献缺口。

### claim_evidence_ledger

#### 1. 众包反应能显著提升机器人检测性能。

- claim_cn：众包反应能显著提升机器人检测性能。

- evidence_cn：Table 6：增强随机森林宏F1=0.805，传统=0.407；五个分类器均一致提升。

#### 2. 言语行为可作为评估众包反应确定性的机制并带来增量提升。

- claim_cn：言语行为可作为评估众包反应确定性的机制并带来增量提升。

- evidence_cn：Table 7：去掉言语行为后宏F1从0.805降至0.774；附录A3提供逐言语行为分析。

#### 3. 系统能够在机器人早期活动时检测，且标签越多检测率越高。

- claim_cn：系统能够在机器人早期活动时检测，且标签越多检测率越高。

- evidence_cn：Table 8：50条消息时增强模型81% vs 传统64%；Table 9：10个标签时78% vs 59%。

#### 4. 系统对更新/更高级的机器人仍稳健。

- claim_cn：系统对更新/更高级的机器人仍稳健。

- evidence_cn：Table 10：增强随机森林精度仅下降3.44%，传统模型下降8.78%。

#### 5. 现有常用基准数据集缺少回复数据，无法直接支持众包反应研究。

- claim_cn：现有常用基准数据集缺少回复数据，无法直接支持众包反应研究。

- evidence_cn：Section 4.4.4：Cresci数据集无回复，无法benchmark众包特征；Varol特征大部分无法迁移到Reddit。

#### 6. BERT是三类文本分类任务的最佳模型。

- claim_cn：BERT是三类文本分类任务的最佳模型。

- evidence_cn：Table 4：话题F1=0.959，情感F1=0.914，言语行为F1=0.865，均优于RNN/SVM。

- internal_validity_strategy_cn：使用时间顺序80/20划分避免特征泄漏；删除训练账号在测试期收到的回复；用10折交叉验证训练文本分类器；用多分类器交叉验证避免单模型偶然性；用消融分离特征贡献；对机器人账号采用10次以上举报的阈值提高ground truth可信度。

- external_validity_strategy_cn：使用真实Reddit众包举报数据而非人工实验；收集2016-2018整段会话；用2019年新创建的机器人作为时间外验证；尝试与Cresci/Garcia-Silva等文献基准对比；选取多个分类器以展示方法稳健性。

- what_is_not_actually_tested_cn：没有真实在线部署；没有检验机器人故意发布虚假举报的策略；没有直接测试最先进、完全不被人类识别的机器人；没有对言语行为与性能之间的因果机制做更细粒度实验；没有在Twitter等其他平台验证众包反应特征的通用性；Cresci基准上无法对众包特征本身做benchmark。

## 贡献闭环

- technical_claim_cn：在Reddit长文本平台，BERT为基础的众包反应增强模型显著优于仅使用语义和时间相似性的传统模型，且比文献中Twitter短期模型更具长文本适应性。

- artifact_claim_cn：可识别的设计部分“人类认知特征”（话题、情感、言语行为）导致了性能提升；其中去掉话题特征下降最明显，去掉言语行为下降适度，去掉情感几乎不变。

- mechanism_claim_cn：用户对疑似机器人的自然回复可被视为隐式众包标签，言语行为分类能帮助区分高确定性与低确定性的标签，从而改善模型学习。

- boundary_claim_cn：该方法适用于“用户能够识别并公开回应”的社交机器人；对完全不被人类察觉的最先进机器人无效；检测存在延迟；言语行为的效果可能受个体人格影响。

- reusable_design_knowledge_cn：未来机器人检测系统应显式收集并利用消息回复作为众包反应；需要以话题分类识别“指出机器人”的回复；言语行为可作为衡量回复确定性的特征；系统可部署到已有检测流程中，并需要定期用系统发现和外部数据重新训练。

- theoretical_contribution_cn：将言语行为理论从对话理解和文本意义建构延伸到众包标签可信度评估与安全信息学；构建了“言语行为→确定性→众包标签权重”的理论应用链条，并提供了实证证据。

- how_discussion_closes_intro_gap_cn：引言指出现有检测忽略人类回复且缺少长文本与会话级数据；讨论部分明确声称这是首个引入众包反应和言语行为的社交机器人检测工作，并指出Cresci等基准因缺少回复而无法支持这类研究，从而把数据缺口转化为本文的数据贡献和后续研究议程。

- overclaim_or_unsupported_leaps_cn：作者承认言语行为并非必要，但在摘要和贡献中仍强调其作为评估确定性的机制，实测增益较小；从“分类性能提升”到“系统可部署”之间存在跨度，因为没有真实在线部署；从“众包标签帮助检测”推断“用户更早识别恶意机器人”也需要更多现场证据；面对2019新机器人的测试只覆盖约一年后的数据，不能说明长期抗进化能力。

## 句级写作动作图谱

### 1. P1 S1

- order：1

- section：Introduction

- locator：P1 S1

- move_code：CONTEXT

- paraphrase_cn：社交媒体广泛受众吸引网络对手操纵在线话语。

- rhetorical_function_cn：建立问题所在的现实场景。

- depends_on_cn：无。

- sets_up_cn：引出社交机器人作为放大攻击的工具。

- evidence_pointer：Introduction P1 S1

### 2. P1 S2-S3

- order：2

- section：Introduction

- locator：P1 S2-S3

- move_code：PRACTICAL_STAKES

- paraphrase_cn：网络对手越来越多用机器人自动化并扩大攻击，例如FCC公众评论被机器人垃圾评论淹没。

- rhetorical_function_cn：说明问题具有真实世界后果。

- depends_on_cn：建立在社交机器人泛滥的背景上。

- sets_up_cn：为研究必要性提供动机。

- evidence_pointer：Introduction P1 S2-S3

### 3. P1 S4-S5

- order：3

- section：Introduction

- locator：P1 S4-S5

- move_code：PHENOMENON

- paraphrase_cn：尽管机器人能欺骗许多人，但越来越多用户能识别并公开指出机器人活动。

- rhetorical_function_cn：引入论文核心经验现象：自然人会对机器人做出反应。

- depends_on_cn：前面提到机器人泛滥且用户被欺骗。

- sets_up_cn：为利用众包反应提供经验基础。

- evidence_pointer：Introduction P1 S4-S5

### 4. P1 S6

- order：4

- section：Introduction

- locator：P1 S6

- move_code：LIMITATION

- paraphrase_cn：现有文献对人类与机器人互动的分析有限。

- rhetorical_function_cn：指出现有研究盲区。

- depends_on_cn：现象已建立。

- sets_up_cn：定义研究缺口。

- evidence_pointer：Introduction P1 S6

### 5. P1 S7

- order：5

- section：Introduction

- locator：P1 S7

- move_code：GAP

- paraphrase_cn：本文要解决这个缺口：用真实用户对疑似机器人的反应构建特征，增强传统检测。

- rhetorical_function_cn：明确研究目的。

- depends_on_cn：前述局限性。

- sets_up_cn：引出言语行为理论作为可信度框架。

- evidence_pointer：Introduction P1 S7

### 6. P1 S8

- order：6

- section：Introduction

- locator：P1 S8

- move_code：THEORY_INTRO

- paraphrase_cn：由于用户识别机器人的能力不同，需要以言语行为理论为基础构建框架来区分不同类型用户反应的优先级。

- rhetorical_function_cn：引入理论工具。

- depends_on_cn：缺口需要衡量用户反应可信度。

- sets_up_cn：为研究框架和特征设计提供理论来源。

- evidence_pointer：Introduction P1 S8

### 7. P2 S1

- order：7

- section：Introduction

- locator：P2 S1

- move_code：PRACTICAL_STAKES

- paraphrase_cn：社交机器人泛滥带来严重的伦理与实践挑战，值得研究。

- rhetorical_function_cn：再次强调问题重要性。

- depends_on_cn：引言开头的问题背景。

- sets_up_cn：引出已有检测与对抗升级。

- evidence_pointer：Introduction P2 S1

### 8. P2 S2-S3

- order：8

- section：Introduction

- locator：P2 S2-S3

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：已有研究主要用启发式方法检测机器人高度同步的非人类行为模式，但机器人也在发展反检测能力。

- rhetorical_function_cn：总结现有检测能力与局限。

- depends_on_cn：问题重要性。

- sets_up_cn：说明需要新特征和新方法。

- evidence_pointer：Introduction P2 S2-S3

### 9. P2 S4-S5

- order：9

- section：Introduction

- locator：P2 S4-S5

- move_code：WHY_GAP_MATTERS

- paraphrase_cn：对抗升级促使学界和业界呼吁更多抑制机器人影响的研究，以及设计新特征。

- rhetorical_function_cn：解释为什么需要填补缺口。

- depends_on_cn：机器人反检测能力不断提高。

- sets_up_cn：支撑本文提出新特征的合理性。

- evidence_pointer：Introduction P2 S4-S5

### 10. P3 S1-S2

- order：10

- section：Introduction

- locator：P3 S1-S2

- move_code：PHENOMENON

- paraphrase_cn：媒体曝光和机器人的现实影响使用户变得警觉，并会在遇到可疑内容时留言提醒他人。

- rhetorical_function_cn：进一步确认用户反应是真实存在的现象。

- depends_on_cn：用户能识别机器人这一现象。

- sets_up_cn：为众包反应作为数据来源提供基础。

- evidence_pointer：Introduction P3 S1-S2

### 11. P3 S3

- order：11

- section：Introduction

- locator：P3 S3

- move_code：GAP

- paraphrase_cn：尽管机器人研究很多，但没有研究考虑将用户消息中蕴含的人类认知能力纳入机器人内容检测，众包标签也未被使用。

- rhetorical_function_cn：突出文献空白。

- depends_on_cn：现象存在但未被利用。

- sets_up_cn：引出本文核心缺口。

- evidence_pointer：Introduction P3 S3

### 12. P4 S1-S5

- order：12

- section：Introduction

- locator：P4 S1-S5

- move_code：WHY_GAP_MATTERS

- paraphrase_cn：使用众包标签并不简单，因为两个用户都说发现机器人时，一个可能非常确定，另一个可能只是怀疑，这要求系统化地权衡不同回复。

- rhetorical_function_cn：说明为什么简单加入用户回复不够，需要可信度评估。

- depends_on_cn：用户能力不同这一现象。

- sets_up_cn：为言语行为理论引入提供逻辑必然性。

- evidence_pointer：Introduction P4 S1-S5

### 13. P5 S1-S2

- order：13

- section：Introduction

- locator：P5 S1-S2

- move_code：THEORY_INTRO

- paraphrase_cn：本文用言语行为理论来衡量和加权不同用户的回复，通过判断回复试图完成的行为来评估其意义。

- rhetorical_function_cn：把理论应用到具体问题。

- depends_on_cn：需要用系统方式评价回复可信度。

- sets_up_cn：为言语行为分类特征奠定基础。

- evidence_pointer：Introduction P5 S1-S2

### 14. P5 S3

- order：14

- section：Introduction

- locator：P5 S3

- move_code：HYPOTHESIS_OR_PROPOSITION

- paraphrase_cn：作者断言这种将用户回复纳入机器人检测的视角比传统模型性能更优。

- rhetorical_function_cn：提出待检验的核心主张。

- depends_on_cn：理论框架。

- sets_up_cn：后续实验检验这一主张。

- evidence_pointer：Introduction P5 S3

### 15. P6 S1

- order：15

- section：Introduction

- locator：P6 S1

- move_code：CONTRIBUTION

- paraphrase_cn：主要贡献是探索评估人群反应的机器人检测策略。

- rhetorical_function_cn：提前声明贡献。

- depends_on_cn：前面的缺口。

- sets_up_cn：为后文贡献讨论做准备。

- evidence_pointer：Introduction P6 S1

### 16. P6 S2-S3

- order：16

- section：Introduction

- locator：P6 S2-S3

- move_code：LIMITATION

- paraphrase_cn：现有基准数据集只包含机器人消息，没有回复；言语行为理论未曾在众包标签或安全信息学中使用。

- rhetorical_function_cn：强化已有制品的缺口。

- depends_on_cn：核心贡献声明。

- sets_up_cn：说明本文的独特位置。

- evidence_pointer：Introduction P6 S2-S3

### 17. P6 S4-S5

- order：17

- section：Introduction

- locator：P6 S4-S5

- move_code：CONTRIBUTION

- paraphrase_cn：研究结果是未来检测应纳入众包反应，且言语行为可能作为衡量众包反应确定性的机制。

- rhetorical_function_cn：把贡献具体化为可引用的知识。

- depends_on_cn：理论应用与待检验主张。

- sets_up_cn：为摘要和讨论中的贡献表述提供模板。

- evidence_pointer：Introduction P6 S4-S5

### 18. P7 S1-S3

- order：18

- section：Introduction

- locator：P7 S1-S3

- move_code：WHY_GAP_MATTERS

- paraphrase_cn：该工作处于人类与机器认知能力结合点，回应了IS领域对更多设计科学计算研究的呼吁。

- rhetorical_function_cn：把问题提升到IS学科相关性。

- depends_on_cn：贡献声明。

- sets_up_cn：证明该研究不只是技术性能问题。

- evidence_pointer：Introduction P7 S1-S3

### 19. P8 S1

- order：19

- section：Introduction

- locator：P8 S1

- move_code：STUDY_OVERVIEW

- paraphrase_cn：论文结构预告：先综述背景，再介绍研究框架，然后描述数据、实验和评价，最后讨论贡献。

- rhetorical_function_cn：为读者提供阅读路径。

- depends_on_cn：全文结构。

- sets_up_cn：引导进入Background。

- evidence_pointer：Introduction P8 S1

### 20. Section 2 intro S1

- order：20

- section：Background

- locator：Section 2 intro S1

- move_code：STUDY_OVERVIEW

- paraphrase_cn：作者将回顾三条文献：社交机器人、社交媒体分析、言语行为理论。

- rhetorical_function_cn：说明文献选择结构。

- depends_on_cn：研究问题。

- sets_up_cn：为每节文献分别服务。

- evidence_pointer：Section 2 intro S1

### 21. Section 2.1.1 S1-S2

- order：21

- section：Background

- locator：Section 2.1.1 S1-S2

- move_code：CONTEXT

- paraphrase_cn：社交机器人约占热门平台5%-8%用户，常发布垃圾、虚假信息和恶意软件。

- rhetorical_function_cn：量化问题的普遍性与危害。

- depends_on_cn：引言背景。

- sets_up_cn：论证检测研究的紧迫性。

- evidence_pointer：Section 2.1.1 S1-S2

### 22. Section 2.1.1 S3-S4

- order：22

- section：Background

- locator：Section 2.1.1 S3-S4

- move_code：MECHANISM

- paraphrase_cn：机器人影响信息扩散、增加垃圾与虚假社交请求，降低用户体验并导致用户流失和平台损失。

- rhetorical_function_cn：解释机器人为什么会产生平台级伤害。

- depends_on_cn：机器人普遍存在。

- sets_up_cn：为平台管理者采取行动提供动机。

- evidence_pointer：Section 2.1.1 S3-S4

### 23. Section 2.1.3 S1-S2

- order：23

- section：Background

- locator：Section 2.1.3 S1-S2

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：已有机器人研究在ground truth、特征开发、建模技术和评估程序上高度相似。

- rhetorical_function_cn：总结领域共同范式。

- depends_on_cn：前面的机器人类型讨论。

- sets_up_cn：引出该范式的局限。

- evidence_pointer：Section 2.1.3 S1-S2

### 24. Section 2.1.3 S3

- order：24

- section：Background

- locator：Section 2.1.3 S3

- move_code：LIMITATION

- paraphrase_cn：建立ground truth是常见难题，开放的带验证标签数据集很少。

- rhetorical_function_cn：指出数据瓶颈。

- depends_on_cn：领域范式。

- sets_up_cn：为众包ground truth的合理性做铺垫。

- evidence_pointer：Section 2.1.3 S3

### 25. Section 2.1.3 S4-S5

- order：25

- section：Background

- locator：Section 2.1.3 S4-S5

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：常见ground truth方法包括蜜罐、公开数据集、众包数据、专家标注，各有权衡。

- rhetorical_function_cn：显示方法多样性并承认无统一最优。

- depends_on_cn：ground truth难题。

- sets_up_cn：解释本文选择众包列表的理由。

- evidence_pointer：Section 2.1.3 S4-S5

### 26. Section 2.1.3 S6-S7

- order：26

- section：Background

- locator：Section 2.1.3 S6-S7

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：特征生成与模型选择紧密相连，内容分析、网络分析各有特征，且平台决定可用特征。

- rhetorical_function_cn：说明现有方法的平台依赖性。

- depends_on_cn：检测方法总结。

- sets_up_cn：为长文本平台研究缺口提供依据。

- evidence_pointer：Section 2.1.3 S6-S7

### 27. Table 1前的段落

- order：27

- section：Background

- locator：Table 1前的段落

- move_code：LIMITATION

- paraphrase_cn：大多数文本机器人检测研究聚焦Twitter短文本，长文本平台如Reddit的应用效果未知，相关研究稀缺。

- rhetorical_function_cn：指出平台代表性不足。

- depends_on_cn：平台特征总结。

- sets_up_cn：为选择Reddit作数据平台提供理由。

- evidence_pointer：Section 2.1.3，Table 1前一段

### 28. Table 1后讨论Cresci数据的段落

- order：28

- section：Background

- locator：Table 1后讨论Cresci数据的段落

- move_code：LIMITATION

- paraphrase_cn：Cresci数据只有消息级粒度，无法重建会话和回复关系，且该局限延续到许多后续研究。

- rhetorical_function_cn：把常见基准数据集的缺陷上升为领域缺口。

- depends_on_cn：对现有数据集的回顾。

- sets_up_cn：为众包回复数据贡献铺路。

- evidence_pointer：Section 2.1.3，Table 1后

### 29. Section 2.1末尾

- order：29

- section：Background

- locator：Section 2.1末尾

- move_code：GAP

- paraphrase_cn：现有机器人检测只评估机器人消息，不利用包含人类判断的众包反应。

- rhetorical_function_cn：明确核心文献缺口。

- depends_on_cn：Cresci数据局限和用户意识现象。

- sets_up_cn：引出研究问题1。

- evidence_pointer：Section 2.1末尾

### 30. Section 2.1末尾后两段

- order：30

- section：Background

- locator：Section 2.1末尾后两段

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：众包标签已在其他领域使用，可以是显式任务标签或隐式系统使用信号。

- rhetorical_function_cn：为众包反应构建合法性。

- depends_on_cn：众包反应未用于机器人检测的缺口。

- sets_up_cn：将社交媒体自然回复视为隐式众包标签。

- evidence_pointer：Section 2.1末尾后两段

### 31. Section 2.1末尾研究问题处

- order：31

- section：Background

- locator：Section 2.1末尾研究问题处

- move_code：RQ_OR_OBJECTIVE

- paraphrase_cn：研究问题1：分析众包反应会对机器人检测任务产生什么影响？

- rhetorical_function_cn：正式提出第一个研究问题。

- depends_on_cn：核心缺口。

- sets_up_cn：框架设计的第一个目标。

- evidence_pointer：Section 2.1末尾，Research Question 1

### 32. Section 2.2倒数第二段

- order：32

- section：Background

- locator：Section 2.2倒数第二段

- move_code：LIMITATION

- paraphrase_cn：话题和情感分析不足以完全操作化一个用人类智能增强机器学习的方法，因为用户识别机器人的确定性不同。

- rhetorical_function_cn：说明现有文本分析工具不足。

- depends_on_cn：社交媒体分析综述。

- sets_up_cn：引出研究问题2。

- evidence_pointer：Section 2.2倒数第二段

### 33. Section 2.2研究问题处

- order：33

- section：Background

- locator：Section 2.2研究问题处

- move_code：RQ_OR_OBJECTIVE

- paraphrase_cn：研究问题2：如何用计算方式评估众包反应对潜在机器人的确定性？

- rhetorical_function_cn：提出第二个研究问题。

- depends_on_cn：话题/情感分析局限。

- sets_up_cn：为引入言语行为理论做铺垫。

- evidence_pointer：Section 2.2，Research Question 2

### 34. Section 2.3.1 S1-S2

- order：34

- section：Background

- locator：Section 2.3.1 S1-S2

- move_code：THEORY_INTRO

- paraphrase_cn：言语行为视角评估说话者想完成的行为，是理解个体间沟通意图的工具。

- rhetorical_function_cn：介绍言语行为理论核心思想。

- depends_on_cn：需要一个衡量语言意图的理论。

- sets_up_cn：为理论操作化打基础。

- evidence_pointer：Section 2.3.1 S1-S2

### 35. Section 2.3.1 Searle分类部分

- order：35

- section：Background

- locator：Section 2.3.1 Searle分类部分

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：Searle提出断言、承诺、宣告、指令、表达五类言语行为，是许多计算工作基础。

- rhetorical_function_cn：选择本文采用的理论分类体系。

- depends_on_cn：理论综述。

- sets_up_cn：为言语行为分类器和特征定义提供标签体系。

- evidence_pointer：Section 2.3.1，Table 2

### 36. Section 2.3.1 RSA段落

- order：36

- section：Background

- locator：Section 2.3.1 RSA段落

- move_code：LIMITATION

- paraphrase_cn：RSA理论依赖听者主观解释，难以扩展到社交媒体中互不相识的大规模网络。

- rhetorical_function_cn：排除不适合的理论，保留Searle式分类。

- depends_on_cn：理论选项比较。

- sets_up_cn：为使用Searle分类提供理由。

- evidence_pointer：Section 2.3.1 RSA段落

### 37. Section 2.3.2 S1-S2

- order：37

- section：Background

- locator：Section 2.3.2 S1-S2

- move_code：GAP

- paraphrase_cn：言语行为分类尚未用于社交机器人检测，但现有文本分析管线可扩展至言语行为分类。

- rhetorical_function_cn：识别理论与机器人检测之间的空白。

- depends_on_cn：言语行为理论综述。

- sets_up_cn：把言语行为变成可执行分类任务。

- evidence_pointer：Section 2.3.2 S1-S2

### 38. Section 2.3.2 S4-S5

- order：38

- section：Background

- locator：Section 2.3.2 S4-S5

- move_code：MECHANISM

- paraphrase_cn：众包数据集可扩展构建ground truth，但用户不确定时不会报告，因此不同众包反应的确定性不同，选择高质量数据会提高性能。

- rhetorical_function_cn：解释为什么需要按可信度筛选标签。

- depends_on_cn：众包ground truth的可行性。

- sets_up_cn：引出研究问题3。

- evidence_pointer：Section 2.3.2 S4-S5

### 39. Section 2.3.2研究问题处

- order：39

- section：Background

- locator：Section 2.3.2研究问题处

- move_code：RQ_OR_OBJECTIVE

- paraphrase_cn：研究问题3：言语行为能否用于计算评估众包反应识别潜在机器人的确定性？

- rhetorical_function_cn：正式提出第三个研究问题。

- depends_on_cn：言语行为理论。

- sets_up_cn：为实验设计确定目标。

- evidence_pointer：Section 2.3.2，Research Question 3

### 40. Section 3 S1-S3

- order：40

- section：Research Approach

- locator：Section 3 S1-S3

- move_code：GAP

- paraphrase_cn：机器人与平台正在军备竞赛，众包反应未被利用；需要研究如何加权反应以及言语行为是否适用。

- rhetorical_function_cn：把三个研究问题整合进研究框架。

- depends_on_cn：Background各缺口。

- sets_up_cn：引出研究方法与框架图。

- evidence_pointer：Section 3 S1-S3

### 41. Section 3 S4-S5

- order：41

- section：Research Approach

- locator：Section 3 S4-S5

- move_code：PRACTICAL_STAKES

- paraphrase_cn：作者还关注测量社交机器人的真实影响并支持管理者决策。

- rhetorical_function_cn：增加研究的实践意义。

- depends_on_cn：核心问题。

- sets_up_cn：为后续描述性统计和平台部署建议提供动机。

- evidence_pointer：Section 3 S4-S5

### 42. Section 4.1.1 S2-S3

- order：42

- section：Data Collection

- locator：Section 4.1.1 S2-S3

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：选择Reddit是因为能观察自然发生的真实人机互动，而非受控设置。

- rhetorical_function_cn：解释平台选择的生态效度。

- depends_on_cn：研究框架需要真实互动数据。

- sets_up_cn：为数据收集和ground truth来源作辩护。

- evidence_pointer：Section 4.1.1 S2-S3

### 43. Section 4.1.2 S2-S3

- order：43

- section：Data Collection

- locator：Section 4.1.2 S2-S3

- move_code：DESIGN_FEATURE

- paraphrase_cn：只保留被举报10次以上的机器人账号，得到777个高置信ground truth账号。

- rhetorical_function_cn：设计ground truth过滤规则。

- depends_on_cn：众包列表可能有误报。

- sets_up_cn：为后续特征提取提供可信样本。

- evidence_pointer：Section 4.1.2 S2-S3

### 44. Section 4.1.3 S1-S3

- order：44

- section：Data Collection

- locator：Section 4.1.3 S1-S3

- move_code：DESIGN_FEATURE

- paraphrase_cn：将对话拆解为人机回复关系，只收集机器人消息和直接回复；假定没有机器人回复机器人。

- rhetorical_function_cn：定义众包反应的数据结构。

- depends_on_cn：Reddit线程的回复关系。

- sets_up_cn：为人类认知特征计算提供回复语料。

- evidence_pointer：Section 4.1.3 S1-S3

### 45. Section 4.1.3 S4-S7

- order：45

- section：Data Collection

- locator：Section 4.1.3 S4-S7

- move_code：BENCHMARK_OR_CONTRAST

- paraphrase_cn：额外收集非机器人账号消息和人类消息的回复，以构造传统Bot/非Bot比较测试床；按时间顺序80/20划分并删除训练账号在测试期的回复，防止特征泄漏。

- rhetorical_function_cn：建立比较所需的非机器人对照与时间划分。

- depends_on_cn：机器人数据。

- sets_up_cn：确保最终分类实验具有对照和时间有效性。

- evidence_pointer：Section 4.1.3 S4-S7

### 46. Section 4.2.2 S1-S2

- order：46

- section：Human-Cognitive Power

- locator：Section 4.2.2 S1-S2

- move_code：DESIGN_FEATURE

- paraphrase_cn：采用Transformer（BERT），因为能处理长序列且不会像RNN那样消失梯度，适合Reddit长文本。

- rhetorical_function_cn：为系统选择核心深度学习架构。

- depends_on_cn：长文本平台特征。

- sets_up_cn：支撑后续所有BERT特征生成。

- evidence_pointer：Section 4.2.2 S1-S2

### 47. Section 4.2.3 S1-S2

- order：47

- section：Human-Cognitive Power

- locator：Section 4.2.3 S1-S2

- move_code：REQUIREMENT

- paraphrase_cn：需要判断人类回复是否在指出机器人活动，因此建立二分类话题模型。

- rhetorical_function_cn：把研究问题转化为分类任务。

- depends_on_cn：众包反应需要识别有效性。

- sets_up_cn：构建Bot Topic特征。

- evidence_pointer：Section 4.2.3 S1-S2

### 48. Section 4.2.3 S3-S4

- order：48

- section：Human-Cognitive Power

- locator：Section 4.2.3 S3-S4

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：模型用平衡类训练但会面对真实不平衡数据；采用过采样等文献建议的做法。

- rhetorical_function_cn：解释训练/测试类分布差异的处理。

- depends_on_cn：话题分类任务。

- sets_up_cn：为分类性能报告提供方法依据。

- evidence_pointer：Section 4.2.3 S3-S4

### 49. Section 4.2.3 S5

- order：49

- section：Human-Cognitive Power

- locator：Section 4.2.3 S5

- move_code：RESULT

- paraphrase_cn：BERT在话题分类中表现最佳，很可能因为长序列处理能力。

- rhetorical_function_cn：报告并解释模型选择结果。

- depends_on_cn：五模型对比。

- sets_up_cn：为后续所有特征统一采用BERT。

- evidence_pointer：Section 4.2.3 S5，Table 4

### 50. Section 4.2.4 S1-S2

- order：50

- section：Human-Cognitive Power

- locator：Section 4.2.4 S1-S2

- move_code：MECHANISM

- paraphrase_cn：用户对疑似机器人的回复可能情绪两极化，负情绪有助于揭示试图误导用户的机器人。

- rhetorical_function_cn：论证情感特征的有效性。

- depends_on_cn：话题特征。

- sets_up_cn：构建情感特征。

- evidence_pointer：Section 4.2.4 S1-S2

### 51. Section 4.2.5 S1-S3

- order：51

- section：Human-Cognitive Power

- locator：Section 4.2.5 S1-S3

- move_code：MECHANISM

- paraphrase_cn：言语行为可揭示用户判断机器人的确定性，因此不应平权对待所有回复。

- rhetorical_function_cn：把言语行为理论与机器学习特征连接。

- depends_on_cn：研究问题3。

- sets_up_cn：构建SA1-SA5特征并解释消融预期。

- evidence_pointer：Section 4.2.5 S1-S3

### 52. Section 4.2.5 S5

- order：52

- section：Human-Cognitive Power

- locator：Section 4.2.5 S5

- move_code：RESULT

- paraphrase_cn：BERT在言语行为分类中最佳；表达类占比超过一半；成功识别机器人的回复与普通回复的言语行为分布显著不同。

- rhetorical_function_cn：报告言语行为分类结果及初步分布证据。

- depends_on_cn：言语行为分类器。

- sets_up_cn：为言语行为特征进入最终模型提供支撑。

- evidence_pointer：Section 4.2.5 S5，Table 4

### 53. Section 4.3.1 S1-S2

- order：53

- section：Traditional Computational Approach

- locator：Section 4.3.1 S1-S2

- move_code：DESIGN_FEATURE

- paraphrase_cn：用BERT生成账号级语义嵌入，将账号所有消息拼接成一个输入。

- rhetorical_function_cn：实现传统内容语义特征。

- depends_on_cn：BERT长输入能力。

- sets_up_cn：作为传统模型特征之一。

- evidence_pointer：Section 4.3.1 S1-S2

### 54. Section 4.3.2 S1-S3

- order：54

- section：Traditional Computational Approach

- locator：Section 4.3.2 S1-S3

- move_code：DESIGN_FEATURE

- paraphrase_cn：通过账号消息对之间的平均余弦相似度衡量时间相似性，高相似度表明机器人式重复。

- rhetorical_function_cn：实现传统行为时间特征。

- depends_on_cn：机器人重复行为文献。

- sets_up_cn：作为传统模型第二部分特征。

- evidence_pointer：Section 4.3.2 S1-S3

### 55. Section 4.4.1 S1-S3

- order：55

- section：Human-Machine Symbiosis

- locator：Section 4.4.1 S1-S3

- move_code：DESIGN_FEATURE

- paraphrase_cn：特征矩阵合并众包反应特征（Bot Topic、情感、言语行为）与传统特征（时间相似性、BERT语义向量）。

- rhetorical_function_cn：实现人机认知融合的最终制品。

- depends_on_cn：前几阶段所有特征模块。

- sets_up_cn：为分类对比和消融提供输入。

- evidence_pointer：Section 4.4.1，Table 5

### 56. Section 4.4.1 S4-S6

- order：56

- section：Human-Machine Symbiosis

- locator：Section 4.4.1 S4-S6

- move_code：BENCHMARK_OR_CONTRAST

- paraphrase_cn：实验分两种配置：仅传统特征 vs 传统+众包反应特征，用五类分类器做机器人/非机器人分类。

- rhetorical_function_cn：建立核心对比设计。

- depends_on_cn：特征矩阵。

- sets_up_cn：为核心性能结果提供结构。

- evidence_pointer：Section 4.4.1 S4-S6

### 57. Section 4.4.1 S7

- order：57

- section：Human-Machine Symbiosis

- locator：Section 4.4.1 S7

- move_code：RESULT

- paraphrase_cn：增强模型在所有分类器上都显著提升，随机森林最优，并降低假阴性。

- rhetorical_function_cn：报告核心验证结果。

- depends_on_cn：分类对比。

- sets_up_cn：为消融实验提出待分解问题。

- evidence_pointer：Section 4.4.1 S7，Table 6

### 58. Section 4.4.1 S8

- order：58

- section：Human-Machine Symbiosis

- locator：Section 4.4.1 S8

- move_code：TRANSITION

- paraphrase_cn：性能提升来自回复消息本身还是言语行为尚不清楚，需要用缩减特征集检验。

- rhetorical_function_cn：引出消融实验。

- depends_on_cn：核心结果。

- sets_up_cn：为言语行为增量证据做准备。

- evidence_pointer：Section 4.4.1 S8

### 59. Section 4.4.1 S9

- order：59

- section：Human-Machine Symbiosis

- locator：Section 4.4.1 S9

- move_code：RESULT

- paraphrase_cn：消融显示言语行为带来适度提升；在每天数百万条消息的平台上，小幅提升也能转化为大量被检测出的机器人。

- rhetorical_function_cn：报告消融结果并赋予实际意义。

- depends_on_cn：消融表。

- sets_up_cn：为言语行为贡献的边界做铺垫。

- evidence_pointer：Section 4.4.1 S9，Table 7

### 60. Section 4.4.2 S1-S2

- order：60

- section：Time-to-Detection

- locator：Section 4.4.2 S1-S2

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：利用已有时间划分，模拟当测试账号发布10、25、50条消息时触发检测，以评估系统响应速度。

- rhetorical_function_cn：从静态分类转向部署相关动态评估。

- depends_on_cn：时间序列数据划分。

- sets_up_cn：报告早期检测率。

- evidence_pointer：Section 4.4.2 S1-S2

### 61. Section 4.4.2 S3

- order：61

- section：Time-to-Detection

- locator：Section 4.4.2 S3

- move_code：RESULT

- paraphrase_cn：增强模型在消息数增加后检测率明显上升，50条消息时达81% vs 传统模型64%。

- rhetorical_function_cn：证明增强模型具有早期检测实用性。

- depends_on_cn：时间模拟。

- sets_up_cn：为标签数量模拟作铺垫。

- evidence_pointer：Section 4.4.2，Table 8

### 62. Section 4.4.2 S4-S5

- order：62

- section：Time-to-Detection

- locator：Section 4.4.2 S4-S5

- move_code：BENCHMARK_OR_CONTRAST

- paraphrase_cn：进一步按1、5、10个众包标签触发检测，传统模型同时触发但不使用标签。

- rhetorical_function_cn：把性能与标签数量挂钩，展示众包信息的累积价值。

- depends_on_cn：检测模拟框架。

- sets_up_cn：报告标签数量效应。

- evidence_pointer：Section 4.4.2 S4-S5，Table 9

### 63. Section 4.4.3 S1-S2

- order：63

- section：Advancing Bots

- locator：Section 4.4.3 S1-S2

- move_code：ROBUSTNESS_OR_BOUNDARY_TEST

- paraphrase_cn：为应对机器人持续进化，用2019年新识别出的机器人测试既有模型。

- rhetorical_function_cn：引入时间外稳健性检验。

- depends_on_cn：主实验结果。

- sets_up_cn：说明新数据集构建。

- evidence_pointer：Section 4.4.3 S1-S2

### 64. Section 4.4.3 S5-S6

- order：64

- section：Advancing Bots

- locator：Section 4.4.3 S5-S6

- move_code：RESULT

- paraphrase_cn：增强模型在2019新机器人上性能损失很小，传统模型损失更大；众包反应有助于防止性能随时间退化。

- rhetorical_function_cn：报告稳健性结果并解释原因。

- depends_on_cn：2019数据集实验。

- sets_up_cn：为讨论中的边界条件做准备。

- evidence_pointer：Section 4.4.3，Table 10

### 65. Section 4.4.4 S1-S3

- order：65

- section：Other Benchmarks

- locator：Section 4.4.4 S1-S3

- move_code：BENCHMARK_OR_CONTRAST

- paraphrase_cn：尝试与Garcia-Silva在Cresci数据上的BERT结果对比；旧数据没有回复，无法benchmark众包特征，只能验证基础特征。

- rhetorical_function_cn：把结果锚定到现有benchmark。

- depends_on_cn：已有文献。

- sets_up_cn：论证旧基准数据无法支持众包反应研究。

- evidence_pointer：Section 4.4.4 S1-S3

### 66. Section 4.4.4 S4-S5

- order：66

- section：Other Benchmarks

- locator：Section 4.4.4 S4-S5

- move_code：LIMITATION

- paraphrase_cn：Varol等特征因Reddit缺乏follow/retweet等无法完全迁移，只实现约33/63类，因此放弃不完全对比。

- rhetorical_function_cn：说明跨平台benchmark的根本限制。

- depends_on_cn：Reddit平台特征。

- sets_up_cn：为讨论中的平台普适性边界提供依据。

- evidence_pointer：Section 4.4.4 S4-S5

### 67. Section 5.1 S1-S3

- order：67

- section：Discussion and Conclusion

- locator：Section 5.1 S1-S3

- move_code：CONTRIBUTION

- paraphrase_cn：本文开发了用众包标签和众包反应检测机器人的框架，将计算方法与语言理论结合；识别用户回复并按言语行为分类是全新做法。

- rhetorical_function_cn：总结核心贡献。

- depends_on_cn：全部实验结果。

- sets_up_cn：为后续部署与边界讨论提供主题。

- evidence_pointer：Section 5.1 S1-S3

### 68. Section 5.1 S4-S6

- order：68

- section：Discussion and Conclusion

- locator：Section 5.1 S4-S6

- move_code：CONTRIBUTION

- paraphrase_cn：框架可部署到真实世界，是现有检测系统的自然扩展，也可从零构建。

- rhetorical_function_cn：强调实用性和可复用性。

- depends_on_cn：系统设计与模拟结果。

- sets_up_cn：为实践洞察提供基础。

- evidence_pointer：Section 5.1 S4-S6

### 69. Section 5.1 S7-S8

- order：69

- section：Discussion and Conclusion

- locator：Section 5.1 S7-S8

- move_code：PRACTICAL_STAKES

- paraphrase_cn：社交机器人问题与虚假信息、平台内容审核责任和Section 230等政策议题相关。

- rhetorical_function_cn：把技术贡献连接到社会与政策影响。

- depends_on_cn：问题重要性。

- sets_up_cn：增强研究现实意义。

- evidence_pointer：Section 5.1 S7-S8

### 70. Section 5.2 S1-S3

- order：70

- section：Discussion and Conclusion

- locator：Section 5.2 S1-S3

- move_code：LIMITATION_AND_FUTURE

- paraphrase_cn：依赖众包标签意味着检测是延迟反应；机器人可能在发现前造成伤害，但没有方法能100%提前检测。

- rhetorical_function_cn：坦诚界定方法边界。

- depends_on_cn：系统本质。

- sets_up_cn：维护贡献的同时避免过度宣称。

- evidence_pointer：Section 5.2 S1-S3

### 71. Section 5.2 S4-S6

- order：71

- section：Discussion and Conclusion

- locator：Section 5.2 S4-S6

- move_code：BOUNDARY_CONDITION

- paraphrase_cn：方法依赖用户能识别的机器人；无法检测完全不被发现的机器人；可能对某些机器人类型有偏；言语行为可能受人格影响。

- rhetorical_function_cn：补充适用范围与潜在偏误。

- depends_on_cn：众包数据本质。

- sets_up_cn：为未来研究确定方向。

- evidence_pointer：Section 5.2 S4-S6

### 72. Section 5.2 S7-S8

- order：72

- section：Discussion and Conclusion

- locator：Section 5.2 S7-S8

- move_code：LIMITATION_AND_FUTURE

- paraphrase_cn：机器人可能协同互动或故意发布虚假举报，本文没有检验这些对抗策略。

- rhetorical_function_cn：承认对抗式未来的不确定性。

- depends_on_cn：高级机器人能力。

- sets_up_cn：为后续稳健性研究留空间。

- evidence_pointer：Section 5.2 S7-S8

### 73. Section 5.3 S3-S6

- order：73

- section：Discussion and Conclusion

- locator：Section 5.3 S3-S6

- move_code：CONTRIBUTION

- paraphrase_cn：平台可以先用本文数据或自标数据训练初始模型，再部署并定期用系统发现和外部数据重训练。

- rhetorical_function_cn：把系统转化为可执行的部署建议。

- depends_on_cn：系统设计。

- sets_up_cn：强化设计知识的可复用性。

- evidence_pointer：Section 5.3 S3-S6

### 74. Section 5.4 S1-S5

- order：74

- section：Discussion and Conclusion

- locator：Section 5.4 S1-S5

- move_code：CONTRIBUTION

- paraphrase_cn：多数机器人检测研究集中在Twitter短文本且不用众包反应；本文的Reddit数据和言语行为评估是首次尝试，为未来研究奠定基础。

- rhetorical_function_cn：把结论回扣到引言缺口。

- depends_on_cn：文献综述与实验结果。

- sets_up_cn：论文收束在学科贡献层面。

- evidence_pointer：Section 5.4 S1-S5

## 写作技术

- gap_construction_cn：作者采用多重复合缺口：一是指出现有检测只分析机器人自身消息、忽略人类回复；二是批评常用Cresci基准缺乏会话/回复关系；三是指出长文本平台Reddit检测缺失；四是言语行为理论从未用于众包标签可信度评估。缺口不是“没人做过”的简单陈述，而是用数据缺陷、平台偏差和理论空白共同支撑。

- signposting_cn：摘要和引言末尾都预告论文结构；背景部分用三小节显式说明三条文献流；每节开头用“首先/其次/最后”串起；每个研究问题都放在文献缺口之后，并配有编号“Research Question 1/2/3”，形成清晰路标。

- transition_logic_cn：段落之间的过渡通常先总结当前状态，再指出“但/然而”的局限，最后给出下一步。例如：话题和情感分析虽有用但不足以衡量确定性→引出研究问题2和言语行为；核心分类提升后立即说“不清楚提升来自回复还是言语行为”→引出消融；静态性能报告后说“还需要展示真实世界实用性”→引出时间模拟。

- claim_evidence_rhythm_cn：每个贡献声明都紧跟或紧跟一个具体实验证据。例如先断言“用户回复提供有用特征”，随后用Table 6显示增强模型大幅提升；先问“言语行为是否必要”，随后用Table 7消融回答。结果段落不是单纯报告数字，而是解释数字如何对应缺口。

- benchmark_narrative_cn：作者把benchmark嵌入论证而不是单独堆指标：先用传统模型作为内部基线，再用消融拆解特征贡献，随后用时间/标签模拟把指标翻译为部署效果，最后用Cresci/Garcia-Silva对照说明旧基准无法包含回复数据。因此benchmark同时承担验证、消融、实用性展示和数据缺口证实的多重功能。

- theory_return_cn：在讨论部分，作者把“分类性能提升”回译为“言语行为可作为评估众包反应确定性的机制”，并呼吁未来检测应纳入众包反应；这样实验证据不是停留在性能数字，而是回到理论主张和设计知识。

- contribution_positioning_cn：贡献声明既强调技术性能（增强模型显著优于传统），也强调制品特征（众包反应、言语行为特征可部署），还强调理论应用（言语行为首次用于安全信息学和众包标签），并通过“首次”“尚未有文献”等表述把贡献定位在交叉空白处。

- novelty_protection_cn：作者把性能提升的一部分归因于言语行为的适度增量，但明确承认言语行为并非观察性能提升的必要条件，从而避免过度宣称；同时用“旧数据集没有回复”解释为什么无法与主流benchmark直接比较，把看似弱点的事实转化为数据贡献；并用2019新机器人实验证明方法不是一次性结果。

## 可复用研究与写作程序

### structure_steps

#### 1. 1

- step：1

- writing_job_cn：建立现实问题与可观察现象：先描述安全威胁，再点出“用户已经会自然回复机器人”这一现象，说明现有文献没有利用该现象。

- research_job_cn：收集或确认真实世界中有价值的待检测对象和可观察的人类反应。

- required_evidence_cn：需要至少一个现实案例或数据事实表明问题严重，且用户反应真实存在。

- transition_to_next_cn：从“现象存在但未被利用”进入“需要新特征/新方法”的缺口。

#### 2. 2

- step：2

- writing_job_cn：把一般问题收缩为明确研究问题，并用文献综述结构化支撑缺口：现有方法、常用数据集的不足、平台偏差、理论空白。

- research_job_cn：做焦点文献综述，识别主流数据集/方法无法回答的问题。

- required_evidence_cn：需要具体文献和benchmark缺陷说明，例如基准缺少某个关键数据维度。

- transition_to_next_cn：从缺口过渡到理论工具：某种理论可填补“如何评估”“如何建模”的方法空位。

#### 3. 3

- step：3

- writing_job_cn：引入理论并直接定义可计算变量：说明理论构念如何变成分类标签或特征。

- research_job_cn：建立理论到特征的翻译，例如用言语行为五分类作为用户确定性特征。

- required_evidence_cn：需要有标注数据或领域知识支撑每个理论类别可被人工/算法识别。

- transition_to_next_cn：从“可以计算的特征”进入“如何收集数据并生成特征”的研究设计。

#### 4. 4

- step：4

- writing_job_cn：描述数据收集、特征生成和系统架构；说明每个模块解决什么问题。

- research_job_cn：构建数据集与计算管线：ground truth、回复关系、文本分类、传统基线、特征矩阵。

- required_evidence_cn：需要具体的账号/消息统计、ground truth过滤规则、防泄漏时间划分。

- transition_to_next_cn：从系统构建进入实验评价，用“传统 vs 增强”“消融”回答问题。

#### 5. 5

- step：5

- writing_job_cn：设计多阶段评价：先比较总体性能，再消融特征，再做部署模拟和稳健性测试。

- research_job_cn：运行分类对比、消融、时间/标签阈值模拟、时间外数据验证。

- required_evidence_cn：需要每个实验有明确指标和基线；消融需能分离核心特征贡献。

- transition_to_next_cn：从实验结果进入讨论，把性能数字转化为机制和设计知识。

#### 6. 6

- step：6

- writing_job_cn：用讨论回扣缺口：重述贡献、局限、部署建议和未来方向；避免把结果包装成一次性性能提升。

- research_job_cn：反思方法的边界条件，提出可复用的设计知识。

- required_evidence_cn：需要有边界证据或诚实声明，说明哪些条件未测试。

- transition_to_next_cn：论文以贡献和未来研究收束。

### most_transferable_moves_cn

1. 把现实场景中用户自然产生的行为数据重新定义为“隐式众包标签”，并用多特征衡量其质量

2. 用“传统基线 vs 增强配置+消融”三步骤把性能提升归因到具体特征

3. 在静态分类后增加时间/阈值模拟，把模型指标转化为部署可理解的早期检测率

4. 用“现有benchmark缺少某类数据”解释为什么不能直接比较，并把数据本身作为贡献

5. 用真实世界的新时期数据做时间外稳健性测试，防止贡献停留在单一时点

### resource_intensive_or_nonstandard_parts_cn

1. 从Reddit公开API获取完整会话与回复关系，需要长时间数据收集和较大存储

2. 使用众包社区维护的机器人举报列表作为ground truth，依赖社区活跃度和举报质量

3. 需要大量人工标注：话题2000条、情感3000条、言语行为2500条，且需要较高inter-rater reliability

4. BERT类大模型训练和推理需要GPU资源

5. 2019新机器人集的自建与过滤也依赖后续众包举报，不能完全自动化复制

### what_not_to_copy_superficially_cn

1. 不能只声明“用户回复能增强检测”而不构建回复关系数据集

2. 不能只引入言语行为标签而不做消融，否则无法说明标签贡献

3. 不能声称“系统可部署”而没有时间/标签数量模拟或部署可行性讨论

4. 不能把与旧benchmark不可比表述为优势，而应像作者一样用数据缺陷解释并补充基础模型验证

5. 不能把所有性能提升都归因于理论，作者也用消融承认言语行为只是适度增量

- single_best_description_of_the_routine_cn：找到一个自然产生的、未被利用的数据信号，用一种语言学理论把它变成可信度特征，再用“传统基线+增强模型+消融+时间模拟+时间外测试”的组合证据，把该特征从数据集性能上升为可复用的设计知识。

## 分析边界

本文献为文本全文导入，但图片（研究框架、示例截图）和多个在线附录未包含，因此对Figure 1/2和附录A1-A6的内容只能依据正文推断；文中个别章节编号存在跳号（如4.1出现在3.1之后），但不影响论证结构判断；部分表格性能数值受OCR影响可能有格式误差，分析以总体趋势与作者叙述为准。
