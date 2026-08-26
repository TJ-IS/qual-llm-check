# Explainable Deep Learning for False Information Identification: An Argumentation Theory Approach

- 作者：Kyuhan Lee; Sudha Ram
- 年份 / 期刊：2024 / Information Systems Research
- DOI：10.1287/isre.2020.0097
- 源文件：27953_2024_explainable-deep-learning-for-false-information-identification-an-argumentation-theory-approach.md
- 论文主类型：theory_derived_artifact_experiment
- 主导写作弧线：problem_theory_design_test_return
- 置信度：0.86

## 文章级论证概况

- 核心问题：如何构建一个既能准确识别虚假信息、又能向人类用户解释决策的自动化FII系统？

- 制品与设计：提出G-FINDER，一个方法无关的框架。它在神经语言模型表示（input 1）之外，额外加入基于SBT的输入特征（input 2）：把claim和evidence分解为NE-V-N三元组，构造三节点词网络，利用GloVe词向量的语义相似度为边赋极性，计算结构平衡度，并将平衡度统计量（min/max/mean/top5/bottom5）作为特征。该设计用SBT作为Toulmin论证模型的计算隐喻，显式区分文本的句法与语义。

- 客观结果：Experiment I中，G-FINDER在PHEME Twitter数据上提升所有baseline的F1约1.3%–3.9%，最佳ELECTRA+G-FINDER的F1达82.92%；McNemar检验对MBiLSTM和BERT显著。Wikipedia数据上各baseline提升3.83%–21.71%且全部显著。Experiment II中，SBTX相比ATTNX、ATTNXL和无解释控制组显著提高任务准确率、对AI的信任和决策信心，而ATTNXL反而损害准确率。

- 核心贡献：作者声称在方法论上提出理论驱动的可解释FII框架，显式分离句法与语义；在可解释性上提供类似人类论证过程的SBTX解释并提升人机交互；在多场景中显示通用性；并补充IS领域自动化FII设计科学研究和理论驱动的文本分析研究。

- 整篇论证链：文章从虚假信息造成真实社会成本开始，指出内容审核与AI检测系统需要同时具备准确性和可解释性。现有深度学习方法把truth inference委托给神经网络黑箱，产生潜在表示句法语义纠缠、纳入无关文本、注意力解释不可靠等问题。作者引入Toulmin论证模型说明人类判断真伪时依赖claim、evidence和warrant，用SBT作为计算隐喻把warrant过程转化成词网络平衡性检验，并用Frege指称理论论证其合理性。据此形成设计原则并构建G-FINDER：输入1保留原有神经表示，输入2提供SBT平衡特征。第一个实验证明G-FINDER能在多种深度模型上提升分类性能并具有跨数据集稳健性；第二个实验证明基于SBT的解释SBTX比注意力解释更能提升人的任务表现、信任与信心。结论部分将这些改进重新解释为对IS领域FII设计知识、理论驱动文本分析和人机交互研究的贡献，同时承认证据检索、数据集和XAI泛化方面的局限。

## 类型与写作弧线判定

- 论文主类型判定：论文虽然采用设计科学措辞，但核心逻辑是从Toulmin论证模型、Frege指称理论和SBT推导出明确设计原则，再实现G-FINDER制品，并通过两个实验（性能benchmark和人类实验）检验理论预期。制品选择主要由理论/隐喻决定，而非工程调优或纯数据驱动。

- 主导写作弧线判定：文章按“现实问题→现有方法局限→理论引入→设计原则与制品→两类实验→回到理论贡献与设计知识”推进。理论与设计在前，实验在中间，结尾部分再次返回理论贡献和设计启示，形成完整的problem-theory-design-test-return弧线。

## 研究开展程序

- study_or_phase_count：5

- 研究阶段总序列：第一阶段建立问题与缺口，第二阶段把论证理论翻译为可计算设计原则，第三阶段实现G-FINDER计算制品，第四阶段用性能基准实验检验制品有效性，第五阶段用人类实验检验可解释性效果。整体呈“问题化→理论设计→制品构建→性能验证→人际交互验证”的累积关系，前一阶段的不确定性由后一阶段承接。

### studies_or_phases

#### 1. 问题化与文献缺口构建

- order：1

- name_cn：问题化与文献缺口构建

- question_cn：现有自动化FII方法在性能和可解释性上有什么不足？为何这些不足在现实中重要？

- inputs_and_setting_cn：社交媒体假信息案例、FII文献、Table 1的文献分类；无实验数据。

- designed_or_compared_object_cn：比较经典ML、DL和attention-based DL三类方法，对特征与可解释性进行归纳。

- baseline_control_or_counterfactual_cn：无；此阶段是叙述性文献比较。

##### objective_metrics

（空）

- analysis_method_cn：文献归纳和缺口论证。

- main_result_cn：识别出三个核心缺口：神经表示句法语义纠缠、注意力解释不可靠、既往人类评价实验规模小且控制不足。

- argumentative_role_cn：为理论引入和制品设计提供必要性；说明现有方法不能同时满足accuracy和explainability。

- remaining_uncertainty_cn：如何把人类论证过程转化为可计算算法尚不清楚。

- link_to_next_phase_cn：直接引出Toulmin模型与SBT设计隐喻，以填补该缺口。

##### evidence_pointers

1. Section 1 P5–P6

2. Section 2.1 Table 1之后的research gaps段

3. Section 2.1 解释性评价不足的段落

#### 2. 理论驱动的设计推理与设计原则形成

- order：2

- name_cn：理论驱动的设计推理与设计原则形成

- question_cn：如何用Toulmin模型、SBT和Frege指称理论将‘人类如何判断claim与evidence一致性’转成可计算设计原则？

- inputs_and_setting_cn：Toulmin论证模型、SBT理论、Frege指称理论、人脑句法/语义分离的神经心理学证据；无数据采集。

- designed_or_compared_object_cn：概念层面的三节点签名词网络、边极性推断规则和结构平衡判定逻辑。

- baseline_control_or_counterfactual_cn：与DL黑箱的语义相似度比较（JFK例子）。

##### objective_metrics

（空）

- analysis_method_cn：理论推导、类比推理和示例说明。

- main_result_cn：提出设计原则：在三词循环网络中，已知两条边真值的条件下，可由结构平衡状态推断第三条边真值。

- argumentative_role_cn：为G-FINDER的算法细节提供直接的规格源头。

- remaining_uncertainty_cn：理论原则是否能在真实文本和真实数据上产生性能增益尚未验证。

- link_to_next_phase_cn：原则需要被实现为具体NLP流水线和特征，因此进入制品构建。

##### evidence_pointers

1. Section 2.2 Argumentation Theory段落

2. Section 2.3 SBT定义与Figure 2说明

3. Section 2.3设计原则框

4. Section 2.3 Frege理论对应段

#### 3. G-FINDER计算制品构建

- order：3

- name_cn：G-FINDER计算制品构建

- question_cn：如何将设计原则实现为方法无关的FII输入特征生成器？

- inputs_and_setting_cn：claim/evidence文本，Spacy的NER/POS/lemmatization，coreference resolution，GloVe词向量，以及可选的神经网络输入向量。

- designed_or_compared_object_cn：G-FINDER的三部分架构：input1神经表示、input2 SBT特征、特征拼接后训练。

- baseline_control_or_counterfactual_cn：没有直接对照；与现有baseline的输入特征相对照。

##### objective_metrics

（空）

- analysis_method_cn：NLP流水线、图构建、余弦相似度和结构平衡公式。

- main_result_cn：实现从文本到NE-V-N三元组、可比对三元组、三节点词网络、边极性推断、连续结构平衡度sb值以及input2统计量的完整管道。

- argumentative_role_cn：证明理论设计原则可在工程上落地，并成为可输入任意ML/DL模型的特征。

- remaining_uncertainty_cn：构建出的特征是否真的改进预测性能和人类理解，需要系统评价。

- link_to_next_phase_cn：性能实验利用该特征在多个baseline上检验增益。

##### evidence_pointers

1. Section 3.2 G-FINDER架构段

2. Section 3.2 decomposition and triple extraction段落

3. Section 3.2 Figure 4/Figure 5相关段落

4. Section 3.2 sb公式段落

#### 4. Experiment I：模型性能基准与稳健性

- order：4

- name_cn：Experiment I：模型性能基准与稳健性

- question_cn：G-FINDER输入特征能否在不同数据、不同baseline上稳定提升FII性能？

- inputs_and_setting_cn：PHEME Twitter数据（5,802条，1,972 rumor/3,830 nonrumor），每条claim手动匹配新闻证据；Wikipedia众包事实核查数据作为辅助；自动证据检索模型；带噪声证据的稳健性检验。

- designed_or_compared_object_cn：六类baseline（Riedel、MBiLSTM、Attention、BERT、RoBERTa、ELECTRA）的vanilla版与各自+G-FINDER版。

- baseline_control_or_counterfactual_cn：每个baseline的无G-FINDER版本；Wikipedia数据作为外部数据集；noisy evidence作为反事实稳健性。

##### objective_metrics

1. Precision

2. Recall

3. F1 score

4. AUC

5. Accuracy

6. McNemar statistics

- analysis_method_cn：嵌套交叉验证、McNemar检验、与baseline对比、噪声稳健性分析。

- main_result_cn：G-FINDER在所有baseline上提升F1（BERT提升3.97%，Riedel 1.92%，MBiLSTM 1.85%，Attention 1.89%，RoBERTa 1.31%，ELECTRA 1.57%），MBiLSTM和BERT的McNemar检验显著；Wikipedia实验中全部配对显著；噪声下稳健性更好。

- argumentative_role_cn：直接检验设计原则的有效性，说明理论驱动的输入特征不仅不损害神经模型，反而补足其缺陷。

- remaining_uncertainty_cn：性能提升并不等于解释被人类接受或改善人类决策，因此需要第二个实验。

- link_to_next_phase_cn：由性能验证转向SBTX解释对人类行为的影响。

##### evidence_pointers

1. Section 4.1.1 Data段

2. Section 4.1.2 Baselines段

3. Section 4.1.3 Results段

4. Table 2

5. Online Appendices C and F

#### 5. Experiment II：模型可解释性的人类实验

- order：5

- name_cn：Experiment II：模型可解释性的人类实验

- question_cn：基于结构平衡的解释SBTX相比注意力解释（ATTNX、ATTNXL）和无解释场景，能否改善人机交互？

- inputs_and_setting_cn：280名MTurk美国成年人，排除26名后254名有效；五道FII题目；四组受试者：control、ATTNX、ATTNXL、SBTX。

- designed_or_compared_object_cn：四种解释条件：无解释、完整注意力热图、简版注意力高亮、SBTX三元组分数表。

- baseline_control_or_counterfactual_cn：control组（无解释）作为基线；ATTNX和ATTNXL作为对照解释方式；AI推荐准确率固定为80%。

##### objective_metrics

1. 任务准确率（accuracy）

2. 任务完成时间

3. 对AI推荐的信任

4. 决策信心

- analysis_method_cn：随机分组、多元线性回归，控制性别、年龄、教育、对在线新闻和AI的一般信任；组间系数差异检验。

- main_result_cn：SBTX显著提高任务准确率（β=0.361, p<0.01）、信任（β=1.152, p<0.001）和决策信心（β=0.369, p<0.1）；ATTNXL准确率显著为负（β=-0.338, p<0.05）；SBTX在信任上显著强于其他解释，准确率显著强于ATTNXL但与ATTNX差异不显著。

- argumentative_role_cn：表明G-FINDER不只改进机器性能，其解释方式确实符合人类论证过程并带来人际交互收益，支撑可解释贡献。

- remaining_uncertainty_cn：仅测试了两类解释变体；未测试LIME/SHAP等其他解释；实验为受控任务而非真实内容审核平台；样本为MTurk。

- link_to_next_phase_cn：结论部分将这些结果升级为IS领域的理论贡献、设计知识和实践启示。

##### evidence_pointers

1. Section 4.2.1 Method段

2. Section 4.2.2 Results段

3. Table 3

4. Figure 6

5. Online Appendices I and J

## 各部分修辞架构

### abstract_moves

1. CONTEXT: 在线信息爆炸与真假判断难题

2. PHENOMENON: 大量虚假声明可用于学习特征

3. LIMITATION: 现有ML忽略人类论证，黑箱决策产生多个问题

4. THEORY_INTRO: 引入Toulmin论证模型

5. DESIGN_FEATURE: 词网络→签名词网络→结构平衡度→作为ML输入

6. STUDY_OVERVIEW: 两个实验分别测试性能与可解释性

7. RESULT: 性能超过前沿方法，SBTX提升人类任务表现、信任与信心

8. CONTRIBUTION: 为自动化FII研究提供新方向

### introduction_moves

1. CONTEXT: 现实虚假信息社会成本（Bitcoin April Fool）

2. PRACTICAL_STAKES: 社交媒体放大假信息影响

3. REQUIREMENT: AI系统应既是过滤器又支持人工审核

4. PRIOR_KNOWLEDGE: DL与注意力机制是主流方案

5. LIMITATION: 黑箱、表示纠缠、注意力不可靠

6. GAP: 忽视人类论证过程

7. RQ_OR_OBJECTIVE: 提出Toulmin+SBT计算框架

8. CONTRIBUTION: 方法论、可解释性、通用性、IS贡献

9. STUDY_OVERVIEW: 论文路线图

### theory_and_knowledge_moves

1. PRIOR_KNOWLEDGE: FII文献三分类与特征归纳

2. LIMITATION: 神经表示句法语义纠缠

3. GAP: 过去可解释性评价不足

4. THEORY_INTRO: 论证理论和Toulmin模型组件

5. THEORY_PROPOSITION: 符合Toulmin的解释更可能带来信任

6. MECHANISM: warrant可操作化为claim与evidence的一致性判断

7. MECHANISM: Frege指称理论解释同主语下的谓词真值关系

8. REQUIREMENT: 用SBT作为计算隐喻，把一致性转化为网络平衡性

### artifact_design_moves

1. REQUIREMENT: 区分句法与语义并判断一致性

2. DESIGN_FEATURE: NE-V-N三元组抽取

3. DESIGN_FEATURE: 词网络三节点与边极性

4. DESIGN_FEATURE: sb公式与统计特征

5. DESIGN_FEATURE: 与input1拼接并喂给任意ML/DL模型

### evaluation_moves

1. BENCHMARK_OR_CONTRAST: 六个baseline，每个对比有无G-FINDER

2. METHOD_JUSTIFICATION: 使用PHEME和Wikipedia以覆盖真实与实验室场景

3. ROBUSTNESS_OR_BOUNDARY_TEST: 自动证据检索与noisy evidence检验

4. METHOD_JUSTIFICATION: 人类实验的随机分组、控制变量和固定AI准确率

5. RESULT: Table 2和Table 3量化提升

6. RESULT: SBTX正向效果与ATTNXL负向效果的解释

### discussion_and_contribution_moves

1. CONTRIBUTION: 理论驱动的设计贡献

2. CONTRIBUTION: 方法论挑战的回应

3. CONTRIBUTION: 内容审核实践意义

4. BOUNDARY_CONDITION: 需要evidence输入，适合早期检测

5. LIMITATION_AND_FUTURE: 证据检索、数据集、机器生成假信息、XAI其他方法、复杂场景

## 理论/知识到设计的翻译

### 知识/理论基础

1. Toulmin's model of argumentation

2. Structural balance theory (SBT)

3. Frege's theory of reference

4. Distributional hypothesis

5. Neuropsychology of syntax/semantics dissociation

6. Human-AI interaction and trust-assuring argumentation literature

- 理论—设计耦合：direct

- 耦合判定理由：G-FINDER的核心设计原则直接由Toulmin模型、Frege指称理论和SBT推导而来；边极性规则、结构平衡度特征和SBTX解释形式均由理论决定。神经网络输入部分虽来自工程惯例，但作为被补充的input1而非核心贡献。评价也直接检验理论预设：结构平衡特征提升性能，SBTX改善人机交互。

- 理论到设计翻译链：人类判断真伪依赖claim-evidence-warrant（Toulmin）→ warrant可表示为claim与evidence的信息一致性 → 一致性判断需要分离句法和语义并比较谓词/名词指称（Frege）→ SBT将一致性转化为三节点网络是否平衡 → 实现为NE-V-N三元组词网络与边极性推断 → 结构平衡度sb值构成input2特征 → 该特征同时生成SBTX解释 → 实验I检验性能，实验II检验人类可解释性。

### mapping_table

#### 1. 1

- theory_or_knowledge_claim_cn：Toulmin模型：论证由claim、evidence和warrant构成，warrant连接claim与evidence。

- mechanism_cn：FII需要显式建立claim与evidence之间的warrant；warrant可操作化为信息一致性判断。

- design_requirement_cn：算法应计算claim与evidence的语义一致性，而不只是把两者编码为黑箱向量。

- artifact_choice_cn：把claim/evidence分解为可比较的NE-V-N三元组，构造包含共享实体与两个名词/动词的词网络。

- evaluated_contrast_cn：含G-FINDER的模型与不含G-FINDER的baseline对比；SBTX与ATTNX/ATTNXL对比。

- objective_result_cn：G-FINDER使各baseline的F1提升1.31%–3.97%；SBTX在人类实验中提高准确率和信任。

##### evidence_pointers

1. Section 2.2 Toulmin模型段

2. Section 3.2 三元组与网络构建段

3. Table 2

4. Table 3

#### 2. 2

- theory_or_knowledge_claim_cn：SBT：三实体网络中偶数条负边为平衡，奇数条负边为不平衡；不平衡会产生改变关系的压力。

- mechanism_cn：claim和evidence可看作通过共享实体连接的两个词关系；若网络平衡则claim与evidence一致，否则不一致。

- design_requirement_cn：用结构平衡状态作为claim真伪的代理度量。

- artifact_choice_cn：给证据边赋正号，用GloVe余弦相似度推断claim边和名词边的符号，计算结构平衡度。

- evaluated_contrast_cn：连续sb值特征（min/max/mean/top5/bottom5）与不使用该特征。

- objective_result_cn：加入sb特征提升分类性能；SBTX展示最高/最低一致性三元组。

##### evidence_pointers

1. Section 2.3 SBT定义段

2. Section 3.2 sb公式段

3. Figure 5(c)

#### 3. 3

- theory_or_knowledge_claim_cn：Frege指称理论：谓词可看作以主语为输入且输出真值的函数；同一对象输入给同一语义的谓词应产生相同真值。

- mechanism_cn：若claim和evidence共享主语，但谓词语义相近而宾语指称不同，则两条关系不可能同时为真；已知evidence为真时claim必假。

- design_requirement_cn：当claim动词与evidence动词语义相近、而两个宾语语义不同时，claim边应被判定为不一致。

- artifact_choice_cn：通过v1与v2的余弦相似性决定claim动词边极性，通过n1与n2的余弦相似性决定名词边极性。

- evaluated_contrast_cn：不平衡网络的claim被判为假，平衡网络判为真；由平衡计算隐式实现Frege规则。

- objective_result_cn：实验I中分类准确率和F1提升，说明该规则在真实数据上有效。

##### evidence_pointers

1. Section 2.3 Frege段

2. Section 3.2 edge polarity步

3. Figure 2(3)

#### 4. 4

- theory_or_knowledge_claim_cn：人机交互文献：计算机提供的解释若类似真实人际沟通（如Toulmin式论证），更能促进信任、信心和接受。

- mechanism_cn：SBTX以claim-evidence三元组和一致性分数呈现判断理由，符合人类如何论证，因此提升人的理解。

- design_requirement_cn：FII解释不应只是注意力热图，而应显示claim与evidence之间哪些部分支持或反驳结论。

- artifact_choice_cn：SBTX显示top5最高或最低SBT分数对应的claim/evidence三元组。

- evaluated_contrast_cn：SBTX vs ATTNX、ATTNXL、无解释；AI准确率固定80%。

- objective_result_cn：SBTX显著提高任务准确率、信任和信心；ATTNXL显著降低准确率。

##### evidence_pointers

1. Section 2.2 Gregor and Jones引用段

2. Section 4.2.1 treatment III描述

3. Figure 6(c)

4. Table 3

## 评价逻辑

### evaluation_modes

1. 离线benchmark实验：PHEME Twitter数据上的多baseline对比

2. 外部数据验证：Wikipedia事实核查数据

3. 稳健性检验：noisy evidence和自动证据检索

4. 受控人类实验：MTurk随机分组、四种解释条件

5. 统计检验：McNemar、线性回归、系数差异检验

- why_these_evaluations_cn：文章同时提出性能和可解释性两类主张，因此需要两类评价。性能主张通过规范benchmark和多种baseline对比来检验；可解释性主张不能仅靠离线度量，必须通过人类实验检验人对解释的反应。两个实验分别对应FII系统的两个核心实际要求。

- benchmark_and_contrast_chain_cn：第一层对照是G-FINDER作为附加特征与六种baseline的vanilla版本对比，检验通用提升能力；第二层对照是Wikipedia数据集，检验跨场景稳定性；第三层是noisy evidence，检验对证据质量的稳健性；第四层是人类实验中SBTX与两种注意力解释及无解释对照，检验可解释性有效性。每层都回应前一层无法回答的问题。

### claim_evidence_ledger

#### 1. G-FINDER显著提升FII模型性能

- claim_cn：G-FINDER显著提升FII模型性能

- evidence_cn：Table 2显示所有baseline的F1都有提升，BERT+3.97%，ELECTRA+1.57%；MBiLSTM和BERT的McNemar检验p<0.05。

- status_cn：支持

#### 2. G-FINDER具有跨数据集通用性

- claim_cn：G-FINDER具有跨数据集通用性

- evidence_cn：Wikipedia数据上所有模型对均显著提升，准确率提升3.83%–21.71%（Online Appendix C）。

- status_cn：作者报告支持；因附录未在正文中提供，无法独立核验

#### 3. G-FINDER可早期识别谣言

- claim_cn：G-FINDER可早期识别谣言

- evidence_cn：悉尼人质案中使用的证据文章在事件发生4小时后发布，早于以往研究的20小时阈值。

- status_cn：部分支持；属于说明性证据而非系统性时间对比

#### 4. SBTX改善人类任务准确率

- claim_cn：SBTX改善人类任务准确率

- evidence_cn：Table 3中SBTX系数为0.361（p<0.01），且显著大于ATTNXL系数（p<0.001），但与ATTNX差异不显著（p=0.139）。

- status_cn：支持但需限定：对ATTNX的优势主要体现在信任而非准确率

#### 5. SBTX提高对AI的信任

- claim_cn：SBTX提高对AI的信任

- evidence_cn：SBTX系数1.152（p<0.001），显著高于ATTNX和ATTNXL。

- status_cn：支持

#### 6. SBTX提高决策信心

- claim_cn：SBTX提高决策信心

- evidence_cn：SBTX系数0.369（p<0.1），且与ATTNX、ATTNXL差异分别达到0.001和0.1水平。

- status_cn：支持（显著性较弱）

#### 7. SBTX解释符合人类论证过程

- claim_cn：SBTX解释符合人类论证过程

- evidence_cn：作者通过Toulmin和Frege理论论证并据其设计解释格式；但实验没有直接测量解释是否被认为“像人类论证”。

- status_cn：理论推断支持，直接经验证据不足

- internal_validity_strategy_cn：人类实验采用随机分组、固定AI推荐准确率在80%、设置control/ATTNX/ATTNXL/SBTX四组、控制人口学变量和一般信任、剔除完成时间过短或过长的被试。性能实验采用嵌套交叉验证和McNemar检验，并区分同一模型有无G-FINDER，减少结构差异混淆。

- external_validity_strategy_cn：使用PHEME真实Twitter事件数据和众包Wikipedia数据，覆盖真实谣言与实验室事实核查场景；人工收集的新闻证据贴近早期谣言传播；MTurk被试在年龄、教育上多样化。

- what_is_not_actually_tested_cn：自动证据检索模型虽然构建并报告F1=97.90%，但未在主评价中替代人工证据，因此完全自动化pipeline的实际效果未被直接测试；SBTX未与LIME、SHAP等公认XAI方法比较；对机器生成虚假信息、无ground-truth证据、证据随时间演化等情形只作为未来方向；人类实验是单次任务，而非真实内容审核平台中的持续性使用。

## 贡献闭环

- technical_claim_cn：G-FINDER作为附加特征能够在多个深度学习方法上提升FII的F1、AUC和准确率，并在多个数据集上稳定有效。

- artifact_claim_cn：SBT平衡特征及其与神经表示的拼接是性能提升的来源；SBTX解释形式是改善人机交互的来源。

- mechanism_claim_cn：G-FINDER之所以有效，是因为它模仿人类判断论证一致性的方式，把claim与evidence之间的关系显式建立为warrant；SBTX之所以有效，是因为它向人展示论证中支持或反驳claim的关键部分。

- boundary_claim_cn：本方法适用于有evidence输入、且可提取NE-V-N三元组的基于事实的FII；能在事件发生后数小时内早期检测；对evidence噪声有稳健性。

- reusable_design_knowledge_cn：设计原则：在三词循环网络中，若已知两条边的真值，可由结构平衡推断未知边真值；设计者可将理论中的论证结构转译为图上的签名边与平衡度特征，再把特征作为可解释输入注入任意ML/DL模型。

- theoretical_contribution_cn：把Toulmin论证模型、Frege指称理论和SBT引入IS的自动FII设计；为理论驱动文本分析提供新例；将可解释AI研究从“热图”扩展为基于论证结构的解释，并与信任/信心建立联系。

- how_discussion_closes_intro_gap_cn：结尾直接回应引言中提出的三个缺陷：通过显式分离句法与语义回应“表示纠缠”，通过SBTX回应“注意力解释不可靠/不像人类交流”，通过人类实验回应“过去文献忽视解释对人类行为的影响”；同时用性能提升回应“初始过滤器”的实用要求。

- overclaim_or_unsupported_leaps_cn：作者从G-FINDER的性能和SBTX实验结果跳到“解释符合人类论证过程”的理论解释，但缺乏直接过程证据；将“attention解释有问题”的文献争议处理得较单向；从两个数据集宣称generalizability略强；SBTX对准确率的优势与ATTNX差异并不显著，却在结论中使用更强措辞；噪音证据稳健性只以附录形式报告，无法判断其规模与强度。

## 句级写作动作图谱

### 1. P1 S1–S3

- order：1

- section：Introduction

- locator：P1 S1–S3

- move_code：PHENOMENON

- paraphrase_cn：欺骗无处不在，并以Bitcoin因愚人节玩笑而上涨为例说明假信息可造成实际市场后果。

- rhetorical_function_cn：用一个具体事件把假信息问题从抽象概念变成有社会成本的现实问题。

- depends_on_cn：无；文章开头直接设景。

- sets_up_cn：为后续说明“必须自动检测假信息”提供现实驱动力。

- evidence_pointer：Introduction P1

### 2. P2 S1–S3

- order：2

- section：Introduction

- locator：P2 S1–S3

- move_code：PRACTICAL_STAKES

- paraphrase_cn：社交媒体让每个人都能传播未经核实的观点，假信息比真信息扩散更快。

- rhetorical_function_cn：将问题聚焦到社交媒体假信息，并强调其规模与危害。

- depends_on_cn：承接Bitcoin案例，说明这不是偶发现象。

- sets_up_cn：引出平台需要内容审核与自动化检测。

- evidence_pointer：Introduction P2

### 3. P3 S1–S4

- order：3

- section：Introduction

- locator：P3 S1–S4

- move_code：REQUIREMENT

- paraphrase_cn：人工审核成本高，AI检测系统应既自动化过滤假信息，又向人类审核员解释为何某内容被判定为假。

- rhetorical_function_cn：提出对理想FII系统的双重实际要求：accuracy和explainability。

- depends_on_cn：基于社交媒体假信息规模。

- sets_up_cn：为后文将可解释性作为核心评价维度提供依据。

- evidence_pointer：Introduction P3

### 4. P4 S1–S3

- order：4

- section：Introduction

- locator：P4 S1–S3

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：深度学习和注意力机制被广泛用于文本真伪判断，注意力权重也常被当作解释工具。

- rhetorical_function_cn：概述当前主流技术路径。

- depends_on_cn：上一段提到AI系统需求。

- sets_up_cn：为随后的技术批评设置对象。

- evidence_pointer：Introduction P4

### 5. P5 S1–S4

- order：5

- section：Introduction

- locator：P5 S1–S4

- move_code：LIMITATION

- paraphrase_cn：但这些方法未理解人类论证的本性，把真值推断完全交给神经网络黑箱，导致潜在表示句法语义纠缠、纳入无关词、注意力不能可靠指向重要词。

- rhetorical_function_cn：指出现有深度学习方法的核心技术缺陷。

- depends_on_cn：建立在P4对主流方法的描述之上。

- sets_up_cn：为理论驱动的替代设计制造缺口。

- evidence_pointer：Introduction P5

### 6. P6 S1–S3

- order：6

- section：Introduction

- locator：P6 S1–S3

- move_code：LIMITATION

- paraphrase_cn：把解释完全交给神经网络还会产生不像人际交流的说明，注意力图甚至误导用户。

- rhetorical_function_cn：补充第二个缺口：可解释性不只是技术问题，也是人际交互问题。

- depends_on_cn：承接P5中注意力不可靠的讨论。

- sets_up_cn：强调需要像人类论证方式的解释。

- evidence_pointer：Introduction P6

### 7. P7 S1–S3

- order：7

- section：Introduction

- locator：P7 S1–S3

- move_code：RQ_OR_OBJECTIVE

- paraphrase_cn：为应对这些问题，作者按设计科学路径提出以Toulmin模型为理论基础、以SBT为设计隐喻的DL框架。

- rhetorical_function_cn：第一次明确论文的核心回应方案。

- depends_on_cn：依赖于P5–P6所建构的双重缺口。

- sets_up_cn：引出后续理论说明和方法设计。

- evidence_pointer：Introduction P7

### 8. P8 S1–S6

- order：8

- section：Introduction

- locator：P8 S1–S6

- move_code：CONTRIBUTION

- paraphrase_cn：作者列出六项贡献：方法论、可解释性、通用性、IS设计科学、ML文本分析、人机交互。

- rhetorical_function_cn：提前声明贡献，为读者提供评价框架。

- depends_on_cn：由P7的方案自然延展。

- sets_up_cn：为后文实验和结论提供钩子。

- evidence_pointer：Introduction P8

### 9. P9 S1–S3

- order：9

- section：Introduction

- locator：P9 S1–S3

- move_code：STUDY_OVERVIEW

- paraphrase_cn：给出论文结构：文献、论证理论、计算方法、两个实验及讨论。

- rhetorical_function_cn：提供路线图。

- depends_on_cn：无关键技术依赖。

- sets_up_cn：使读者预期后续章节。

- evidence_pointer：Introduction P9

### 10. Section 2.1 Table 1前段

- order：10

- section：Related Work

- locator：Section 2.1 Table 1前段

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：用Table 1把FII研究按领域、方法、特征和可解释性分类，说明DL和attention-based DL已成为主流。

- rhetorical_function_cn：系统化已有文献，为缺口定位提供坐标。

- depends_on_cn：衔接引言中的技术路径概览。

- sets_up_cn：随后指出这些方法共同的不足。

- evidence_pointer：Section 2.1 Table 1前段

### 11. Section 2.1 research gap第一段

- order：11

- section：Related Work

- locator：Section 2.1 research gap第一段

- move_code：LIMITATION

- paraphrase_cn：神经嵌入把句法和语义混在一起，且扫描全文会产生无关信息，导致相似度判断不可靠。

- rhetorical_function_cn：精确化第一个技术缺口。

- depends_on_cn：建立在Table 1对方法特征的归纳上。

- sets_up_cn：为SBT区分句法/语义的设计提供理由。

- evidence_pointer：Section 2.1 research gap第一段

### 12. Section 2.1 research gap第二段

- order：12

- section：Related Work

- locator：Section 2.1 research gap第二段

- move_code：GAP

- paraphrase_cn：大多数研究忽视模型解释对人类行为的影响，少数考虑人的研究样本小、指标单一或缺少混淆变量控制。

- rhetorical_function_cn：指出可解释性评价的研究空白。

- depends_on_cn：与上一个技术缺口并列，形成双重缺口。

- sets_up_cn：为Experiment II设计和解释评价指标提供依据。

- evidence_pointer：Section 2.1 research gap第二段

### 13. Section 2.1最后一段

- order：13

- section：Related Work

- locator：Section 2.1最后一段

- move_code：RQ_OR_OBJECTIVE

- paraphrase_cn：作者提出用Toulmin模型和SBT设计FII框架，先测性能再测解释。

- rhetorical_function_cn：在文献综述结尾重新聚焦研究设计。

- depends_on_cn：依赖前两个缺口。

- sets_up_cn：自然过渡到2.2理论介绍。

- evidence_pointer：Section 2.1最后一段

### 14. Section 2.2第一段

- order：14

- section：Related Work

- locator：Section 2.2第一段

- move_code：THEORY_INTRO

- paraphrase_cn：论证理论批评形式逻辑不适用于现实论证，Toulmin模型包含claim、evidence、warrant三个核心组件及qualifier等可选组件。

- rhetorical_function_cn：正式引入理论框架。

- depends_on_cn：缺口需要理论来填补。

- sets_up_cn：后续把warrant作为FII的关键机制。

- evidence_pointer：Section 2.2第一段

### 15. Section 2.2第二段

- order：15

- section：Related Work

- locator：Section 2.2第二段

- move_code：THEORY_PROPOSITION

- paraphrase_cn：Toulmin模型给出构建高效可解释FII模型的指导，符合该模型的解释应更具说服力并带来更多信任与满意。

- rhetorical_function_cn：说明理论对FII设计和人机交互的承诺。

- depends_on_cn：Toulmin模型定义。

- sets_up_cn：为SBTX解释的心理效果提供理论预期。

- evidence_pointer：Section 2.2第二段

### 16. Section 2.2第三段

- order：16

- section：Related Work

- locator：Section 2.2第三段

- move_code：GAP

- paraphrase_cn：现有DL把warrant、backing、qualifier、rebuttal全委托给黑箱，而论证模型本身没有给出可计算设计指南。

- rhetorical_function_cn：点出从理论到算法的断层。

- depends_on_cn：Toulmin模型介绍和DL缺陷。

- sets_up_cn：引出作者用Frege和SBT补足这个断层。

- evidence_pointer：Section 2.2第三段

### 17. Section 2.2第四段

- order：17

- section：Related Work

- locator：Section 2.2第四段

- move_code：RQ_OR_OBJECTIVE

- paraphrase_cn：作者提出基于Frege指称理论和SBT设计隐喻的计算方案。

- rhetorical_function_cn：第一次在理论层把缺口转成设计目标。

- depends_on_cn：依赖第三段的计算断层。

- sets_up_cn：为2.3的设计原则做铺垫。

- evidence_pointer：Section 2.2第四段

### 18. Section 2.3第一段

- order：18

- section：Design Principle

- locator：Section 2.3第一段

- move_code：THEORY_INTRO

- paraphrase_cn：ML历史中好的隐喻带来创新设计，SBT是理解和解释人类论证过程的合适隐喻。

- rhetorical_function_cn：为选择SBT提供学术正当性。

- depends_on_cn：前一节提出的SBT作为设计隐喻。

- sets_up_cn：随后定义SBT并说明其与FII的对应。

- evidence_pointer：Section 2.3第一段

### 19. Section 2.3第二段

- order：19

- section：Design Principle

- locator：Section 2.3第二段

- move_code：THEORY_PROPOSITION

- paraphrase_cn：SBT描述三人网络中偶数条负边为平衡，奇数条负边为不平衡，不平衡会产生改变关系的压力。

- rhetorical_function_cn：给出SBT的核心判定规则。

- depends_on_cn：SBT作为隐喻被接受。

- sets_up_cn：为词网络的平衡/不平衡判定提供数学规则。

- evidence_pointer：Section 2.3第二段

### 20. Section 2.3第三段

- order：20

- section：Design Principle

- locator：Section 2.3第三段

- move_code：MECHANISM

- paraphrase_cn：人类判断claim与evidence一致性时同时使用句法和语义；JFK例子说明DL可能把两个句式和语义都不同的句子误判为相似。

- rhetorical_function_cn：展示从理论命题到知识机制的桥梁。

- depends_on_cn：神经心理学句法/语义分离证据。

- sets_up_cn：说明为何SBT网络表示比纯嵌入更适合一致性判断。

- evidence_pointer：Section 2.3第三段

### 21. Section 2.3第四段

- order：21

- section：Design Principle

- locator：Section 2.3第四段

- move_code：REQUIREMENT

- paraphrase_cn：SBT方法把句子句法表示成词网络，用句子语义为边赋极性，再测网络平衡度作为claim与evidence的一致性。

- rhetorical_function_cn：把理论观察转成功能要求。

- depends_on_cn：JFK例子和大脑句法/语义分离。

- sets_up_cn：为Figure 2的详细实现提供概览。

- evidence_pointer：Section 2.3第四段

### 22. Section 2.3第五段与Figure 2

- order：22

- section：Design Principle

- locator：Section 2.3第五段与Figure 2

- move_code：DESIGN_FEATURE

- paraphrase_cn：claim和evidence分解为主谓宾三元组；共享主语形成三节点网络；证据边视为正，claim动词边与名词边用语义相似度赋极性，平衡与否决定claim真假。

- rhetorical_function_cn：给出具体可操作的设计细节。

- depends_on_cn：前一段的功能要求。

- sets_up_cn：为设计原则的正式表述做准备。

- evidence_pointer：Section 2.3第五段、Figure 2

### 23. Section 2.3第六段

- order：23

- section：Design Principle

- locator：Section 2.3第六段

- move_code：MECHANISM

- paraphrase_cn：Frege指称理论说明：同一主语输入给两个语义相近的谓词，若宾语指称不同，则两条关系不可能同时为真；证据为真时claim必假。

- rhetorical_function_cn：为edge polarity规则提供语言哲学基础。

- depends_on_cn：前一段的极性与真值判定。

- sets_up_cn：使网络平衡判定具有理论合法性。

- evidence_pointer：Section 2.3第六段

### 24. Section 2.3设计原则框

- order：24

- section：Design Principle

- locator：Section 2.3设计原则框

- move_code：REQUIREMENT

- paraphrase_cn：在三词循环网络中，已知两条边真值时，可由网络平衡状态推断未知边的真值，这是本方法的设计原则。

- rhetorical_function_cn：用一句规范语句概括全部理论推导。

- depends_on_cn：SBT定义与Frege规则。

- sets_up_cn：直接作为G-FINDER算法的规格。

- evidence_pointer：Section 2.3设计原则框

### 25. Section 2.3最后一段

- order：25

- section：Design Principle

- locator：Section 2.3最后一段

- move_code：TRANSITION

- paraphrase_cn：实现该设计原则将同时提升FII性能和解释的沟通效率。

- rhetorical_function_cn：结束理论段并预告方法实现。

- depends_on_cn：设计原则。

- sets_up_cn：进入Methodology。

- evidence_pointer：Section 2.3最后一段

### 26. Section 3.1 Problem Definition

- order：26

- section：Methodology

- locator：Section 3.1 Problem Definition

- move_code：RQ_OR_OBJECTIVE

- paraphrase_cn：把两个研究问题形式化为：找到并解释一个函数f(c,e)->{0,1}，其中0为真、1为假。

- rhetorical_function_cn：将设计任务转化为可计算问题。

- depends_on_cn：前面所有理论推导。

- sets_up_cn：为G-FINDER的输入输出定义边界。

- evidence_pointer：Section 3.1

### 27. Section 3.2第一段

- order：27

- section：Methodology

- locator：Section 3.2第一段

- move_code：DESIGN_FEATURE

- paraphrase_cn：G-FINDER由三部分组成：神经语言模型表示作为input1，SBT词网络平衡特征作为input2，拼接后训练任意ML/DL模型。

- rhetorical_function_cn：给出制品整体架构。

- depends_on_cn：设计原则与问题定义。

- sets_up_cn：后续细节都是对这三部分的展开。

- evidence_pointer：Section 3.2第一段

### 28. Section 3.2 decomposition段

- order：28

- section：Methodology

- locator：Section 3.2 decomposition段

- move_code：DESIGN_FEATURE

- paraphrase_cn：用从句拆分、词形还原、NER、POS标注和共指消解把句子分解为NE-V-N三元组集合。

- rhetorical_function_cn：说明从自然语言文本到理论构念的工程映射。

- depends_on_cn：G-FINDER三部分架构。

- sets_up_cn：为后续词网络构建提供输入。

- evidence_pointer：Section 3.2 decomposition段

### 29. Section 3.2 Beatles例子

- order：29

- section：Methodology

- locator：Section 3.2 Beatles例子

- move_code：DESIGN_FEATURE

- paraphrase_cn：用“The Beatles被提名音乐奖，证据称The Beatles和Louis Armstrong获格莱美”展示三元组产出。

- rhetorical_function_cn：用具体例子降低NLP流程的抽象性。

- depends_on_cn：三元组分解方法。

- sets_up_cn：为Figure 5的网络构建提供实例。

- evidence_pointer：Section 3.2 Beatles例子

### 30. Section 3.2 word network段

- order：30

- section：Methodology

- locator：Section 3.2 word network段

- move_code：DESIGN_FEATURE

- paraphrase_cn：只有共享命名实体的claim三元组与evidence三元组才可比，由共享实体、两个名词和两个动词构成三节点网络。

- rhetorical_function_cn：定义可比性规则，控制网络规模。

- depends_on_cn：三元组集合。

- sets_up_cn：为边极性推断和平衡判定提供图结构。

- evidence_pointer：Section 3.2 word network段

### 31. Section 3.2 edge polarity段

- order：31

- section：Methodology

- locator：Section 3.2 edge polarity段

- move_code：DESIGN_FEATURE

- paraphrase_cn：证据边恒为正，claim动词边和两个名词边分别用GloVe余弦相似度判断符号，再统计负边数量判定平衡或失衡。

- rhetorical_function_cn：实现设计原则中的边极性规则。

- depends_on_cn：SBT和Frege规则。

- sets_up_cn：为该规则从离散阈值改进为连续sb分数做铺垫。

- evidence_pointer：Section 3.2 edge polarity段

### 32. Section 3.2 sb formula段

- order：32

- section：Methodology

- locator：Section 3.2 sb formula段

- move_code：DESIGN_FEATURE

- paraphrase_cn：阈值法不理想，作者改用动词余弦相似度与名词余弦相似度之差的绝对值得到连续sb值，并取min、max、mean、top5、bottom5作为13维输入。

- rhetorical_function_cn：把离散平衡计数转化为更平滑、更信息丰富的特征。

- depends_on_cn：对阈值法的测试失败经验。

- sets_up_cn：形成方法可复用的特征工程。

- evidence_pointer：Section 3.2 sb formula段

### 33. Section 3.2最后一段

- order：33

- section：Methodology

- locator：Section 3.2最后一段

- move_code：DESIGN_FEATURE

- paraphrase_cn：SBT分数反映claim被evidence支撑的程度，因此也可用于向人解释模型决策。

- rhetorical_function_cn：把性能特征与可解释性机制连接起来。

- depends_on_cn：SBT作为warrant计算的思想。

- sets_up_cn：为Experiment II中的SBTX做伏笔。

- evidence_pointer：Section 3.2最后一段

### 34. Section 4开头

- order：34

- section：Experiment

- locator：Section 4开头

- move_code：STUDY_OVERVIEW

- paraphrase_cn：作者预告两个实验：一个测模型性能，另一个测解释对用户的影响。

- rhetorical_function_cn：明确评价结构。

- depends_on_cn：方法构建完成。

- sets_up_cn：分别展开Experiment I和II。

- evidence_pointer：Section 4开头

### 35. Section 4.1.1 Data段

- order：35

- section：Experiment I

- locator：Section 4.1.1 Data段

- move_code：BENCHMARK_OR_CONTRAST

- paraphrase_cn：使用PHEME Twitter数据并人工为每条claim匹配早期新闻证据，使任务接近真实谣言检测；Wikipedia数据作为补充。

- rhetorical_function_cn：交代benchmark场景和数据来源。

- depends_on_cn：需要claim和evidence成对输入的方法。

- sets_up_cn：为结果的可推广性提供基础。

- evidence_pointer：Section 4.1.1

### 36. Section 4.1.1 robustness段

- order：36

- section：Experiment I

- locator：Section 4.1.1 robustness段

- move_code：ROBUSTNESS_OR_BOUNDARY_TEST

- paraphrase_cn：针对证据质量问题，作者设计自动证据检索模型并对噪声证据做稳健性测试，结果显示G-FINDER提高噪声下的鲁棒性。

- rhetorical_function_cn：回应“证据不可靠”这一实际部署风险。

- depends_on_cn：人工证据选择的局限性。

- sets_up_cn：增强G-FINDER在真实环境中的可信度。

- evidence_pointer：Section 4.1.1

### 37. Section 4.1.2 Baselines段

- order：37

- section：Experiment I

- locator：Section 4.1.2 Baselines段

- move_code：BENCHMARK_OR_CONTRAST

- paraphrase_cn：选取六类baseline并分别为每个baseline训练vanilla版和+G-FINDER版，用嵌套交叉验证调参，报告precision、recall、F1、AUC和accuracy。

- rhetorical_function_cn：建立严格对照，保证性能提升可归因于G-FINDER。

- depends_on_cn：G-FINDER方法无关的设计。

- sets_up_cn：为Table 2的结果提供框架。

- evidence_pointer：Section 4.1.2

### 38. Section 4.1.3 Results段

- order：38

- section：Experiment I

- locator：Section 4.1.3 Results段

- move_code：RESULT

- paraphrase_cn：Table 2显示G-FINDER在全部baseline上提升F1，BERT、MBiLSTM等模型的提升在McNemar检验中显著。

- rhetorical_function_cn：报告核心性能结果。

- depends_on_cn：baseline与评价协议。

- sets_up_cn：支持“设计原则有效”的结论。

- evidence_pointer：Section 4.1.3、Table 2

### 39. Section 4.1.3 additional advantages段

- order：39

- section：Experiment I

- locator：Section 4.1.3 additional advantages段

- move_code：RESULT

- paraphrase_cn：作者补充说明G-FINDER只需要claim与evidence文本，不需要用户行为或回复等额外数据，并能在事件后4小时内检测谣言。

- rhetorical_function_cn：扩展结果的意义，不只讲准确率。

- depends_on_cn：PHEME实验设置。

- sets_up_cn：为实践价值部分提供素材。

- evidence_pointer：Section 4.1.3

### 40. Section 4.2开头段

- order：40

- section：Experiment II

- locator：Section 4.2开头段

- move_code：RQ_OR_OBJECTIVE

- paraphrase_cn：自动FII系统实际由人类使用，因此需要检验解释对任务表现、时间、信任和信心的影响。

- rhetorical_function_cn：说明为何需要第二个实验以及要测哪些指标。

- depends_on_cn：前文关于可解释性缺口的讨论。

- sets_up_cn：为人类实验设计提供逻辑。

- evidence_pointer：Section 4.2开头段

### 41. Section 4.2.1 Method段

- order：41

- section：Experiment II

- locator：Section 4.2.1 Method段

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：在MTurk招募280人并随机分到control、ATTNX、ATTNXL、SBTX四组，控制AI准确率与人口学变量，用多元回归分析处理。

- rhetorical_function_cn：说明实验设计如何保证组间可比并减少混淆。

- depends_on_cn：需检验多个解释条件。

- sets_up_cn：使Table 3结果具有可信度。

- evidence_pointer：Section 4.2.1

### 42. Section 4.2.2 Results accuracy段

- order：42

- section：Experiment II

- locator：Section 4.2.2 Results accuracy段

- move_code：RESULT

- paraphrase_cn：SBTX显著提高任务准确率，ATTNXL显著降低准确率；作者猜测ATTNXL让人只关注被高亮词而忽略全文。

- rhetorical_function_cn：报告核心对比结果并给出解释机制。

- depends_on_cn：Table 3回归模型。

- sets_up_cn：引出解释简洁性与注意力付出的权衡。

- evidence_pointer：Section 4.2.2

### 43. Section 4.2.2 Results trust/confidence段

- order：43

- section：Experiment II

- locator：Section 4.2.2 Results trust/confidence段

- move_code：RESULT

- paraphrase_cn：SBTX在信任和信心上都显著优于对照组并强于两种注意力解释，带来心理层面的额外收益。

- rhetorical_function_cn：佐证SBTX的人际交互优势。

- depends_on_cn：Table 3结果。

- sets_up_cn：为结论中的HCI贡献提供支持。

- evidence_pointer：Section 4.2.2

### 44. Section 5第一段

- order：44

- section：Concluding Remarks

- locator：Section 5第一段

- move_code：CONTRIBUTION

- paraphrase_cn：作者重新声明：基于Toulmin和SBT设计的FII模型性能更强且解释更好，是首批把语言学与心理学理论用于FII设计的研究之一。

- rhetorical_function_cn：在结论开头重申核心贡献并提升到跨学科层面。

- depends_on_cn：两个实验结果。

- sets_up_cn：统一全篇理论贡献。

- evidence_pointer：Section 5第一段

### 45. Section 5第二段

- order：45

- section：Concluding Remarks

- locator：Section 5第二段

- move_code：CONTRIBUTION

- paraphrase_cn：作者称方法解决神经语言模型不能分离句法与语义的问题，并在多个指标上超越前沿baseline，还能在4小时内检测谣言。

- rhetorical_function_cn：直接回应引言中的技术缺口。

- depends_on_cn：Experiment I结果。

- sets_up_cn：为随后实践意义铺路。

- evidence_pointer：Section 5第二段

### 46. Section 5第三段

- order：46

- section：Concluding Remarks

- locator：Section 5第三段

- move_code：CONTRIBUTION

- paraphrase_cn：在实践中，自动FII系统既要可靠又要引导积极的人机交互，本方法同时满足这两个条件。

- rhetorical_function_cn：把技术性能与人类实验共同整合为实践价值。

- depends_on_cn：两个实验的综合。

- sets_up_cn：随后转入局限。

- evidence_pointer：Section 5第三段

### 47. Section 5 limitations段

- order：47

- section：Concluding Remarks

- locator：Section 5 limitations段

- move_code：LIMITATION_AND_FUTURE

- paraphrase_cn：作者承认方法依赖证据检索、需要更多数据集、未处理机器生成假信息、XAI实验需与其他解释方法比较、复杂与动态证据场景尚未测试。

- rhetorical_function_cn：界定贡献边界并指明未来方向。

- depends_on_cn：整篇方法设计。

- sets_up_cn：没有后续阶段，用于保护主张不被过度解释。

- evidence_pointer：Section 5第四段

## 写作技术

- gap_construction_cn：采用“现实需求—技术现状—三重缺陷—理论断层”的叠层缺口：先说明FII系统必须准确且可解释，再指出深度学习的三个具体技术问题，再指出论证模型难以算法化，最后指出可解释性人类评价的空白。

- signposting_cn：在引言末尾给出路线图；每个大节开始用一两句预告该节内容；Experiment开头明确“两个实验”；每个实验内部先讲数据/方法再讲结果。

- transition_logic_cn：用“然而”“尽管”“为了填补这些缺口”“因此”等连接词把现实问题引向文献、文献引向理论、理论引向设计、设计引向实验、实验引向贡献。段与段之间经常以“在下一节中”收束。

- claim_evidence_rhythm_cn：先提出理论主张，再给出设计原则，然后用Table 2/3的具体数字证明；在结果后立即用作者自己的机制解释（如ATTNXL的注意力牺牲）把数字转化为可理解的叙事。

- benchmark_narrative_cn：benchmark不单独存在，而是嵌入“每个baseline的vanilla vs +G-FINDER”结构，让G-FINDER始终是唯一可解释变量；Wikipedia作为外部场景补充，noise作为边界测试。

- theory_return_cn：在结论中把G-FINDER的性能重新表述为“实现了Toulmin模型的warrant过程”，把SBTX的人类实验效果重新表述为“符合人际交流的解释更值得信任”，回到开头的理论主张。

- contribution_positioning_cn：把贡献分层：方法论（算法设计）、机制（句法/语义分离）、设计知识（设计原则）、领域填补（IS设计科学）、交叉学科（理论驱动文本分析）、人机交互（可解释性）。

- novelty_protection_cn：通过强调理论驱动而非工程调优、用SBT作为“设计隐喻”并给出正式设计原则，将贡献从一次性性能提升提升为可复用知识；同时用实验II证明性能之外的人机交互价值，防止论文被理解为纯benchmark改进。

## 可复用研究与写作程序

### structure_steps

#### 1. 1

- step：1

- writing_job_cn：用具体事件引出真实问题，说明系统需要两个不可拆分的需求（准确性+可解释性）。

- research_job_cn：收集真实案例或统计证据，展示现有解决方案的隐性成本。

- required_evidence_cn：能说明问题重要的经验材料。

- transition_to_next_cn：转到当前主流技术及其不足。

#### 2. 2

- step：2

- writing_job_cn：把现有技术路径归类并逐一指出缺陷，形成“性能缺陷”和“解释缺陷”双缺口。

- research_job_cn：系统综述FII文献，归纳方法、特征、可解释性三个维度。

- required_evidence_cn：文献分类表足够覆盖主流方法，且能支撑每个缺陷主张。

- transition_to_next_cn：缺口需要理论来回答，引入目标理论。

#### 3. 3

- step：3

- writing_job_cn：介绍理论并明确其关键组件；说明理论如何对应到人工任务的动作。

- research_job_cn：选择与问题机制匹配的理论，提取核心命题。

- required_evidence_cn：理论文献和已有经验研究支持“该理论对任务有解释力”。

- transition_to_next_cn：说明理论本身不能直接算法化，需要设计隐喻或计算表示。

#### 4. 4

- step：4

- writing_job_cn：用规范语句写出设计原则，再用图示给出从文本到特征的具体步骤。

- research_job_cn：把理论命题翻译为计算约束，确定数据表示和算法步骤。

- required_evidence_cn：能展示该原则确实由理论推导且可被工程实现。

- transition_to_next_cn：用该方法无关性说明可适配任意ML/DL模型。

#### 5. 5

- step：5

- writing_job_cn：设计两个层次分明的评价：离线benchmark检验性能，人类实验检验解释与交互。

- research_job_cn：选定数据集、baseline、对照条件、统计检验和控制变量。

- required_evidence_cn：每个结论都有可观察指标；同一模型有无该特征的对比能隔离贡献。

- transition_to_next_cn：从性能结果转向解释结果，说明为何还需要第二个实验。

#### 6. 6

- step：6

- writing_job_cn：在结论中重新阐述设计原则、机制贡献和边界，回应用人机交互与理论缺口。

- research_job_cn：把实验结果归纳为可复用设计知识和理论贡献，承认未验证场景。

- required_evidence_cn：能够把实验数字映射回具体理论命题；能够说明哪些情况不适合该方法。

- transition_to_next_cn：以局限和未来方向收尾。

### most_transferable_moves_cn

1. 用“理想系统需要两个需求”把性能与可解释性绑定，使两种实验都有必要。

2. 把理论组件映射为图结构（Toulmin的warrant → SBT的边平衡），从而让理论直接决定设计。

3. 把每个baseline同时训练vanilla和+G-FINDER版本，使方法贡献可以被统计检验隔离。

4. 用同一套SBT分数既做分类特征又做人类解释，形成“性能”与“可解释”共享同一机制的设计。

5. 在人类实验中固定AI准确率，避免因模型性能差异污染解释效果判断。

### resource_intensive_or_nonstandard_parts_cn

1. PHEME数据需要人工为每条claim匹配早期新闻证据，工作量较大且依赖领域知识。

2. 自动证据检索模型和noise robustness实验只在附录中报告，主文未给出完整pipeline评价。

3. MTurk实验需要足够样本、质量控制（master、时长过滤）和多组随机分配。

4. G-FINDER涉及NER、POS、coreference、GloVe、多个transformer baseline等大量工程与算力。

### what_not_to_copy_superficially_cn

1. 不能只写“我们使用Toulmin/SBT”而缺少可操作的设计原则和具体算法映射。

2. 不能只报告性能提升而不做同一baseline的with/without对照和统计检验。

3. 不能只宣称“解释像人类论证”而没有人类实验结果。

4. 不能把针对两个数据集的改进扩展为无条件generalizability，必须说明evidence依赖和任务边界。

- single_best_description_of_the_routine_cn：用理论把人工任务的内在结构翻译成一个可计算图或特征，然后证明这个特征既能让机器涨点，又能让人类看懂。

## 分析边界

全文基于提供的正文；Online Appendix A–J仅被作者引用，未包含在输入中，因此Wikipedia性能、noise robustness、自动证据检索、实验问卷材料等只能依赖作者表述，无法独立核验。正文中个别图表与公式的OCR排版可能影响对网络极性符号的精确理解。
