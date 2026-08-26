# Social influence-based contrast language analysis framework for clinical decision support systems

- 作者：Xingwei Yang; Alexandra Joukova; Anteneh Ayanso; Morteza Zihayat
- 年份 / 期刊：2022 / Decision Support Systems
- DOI：10.1016/j.dss.2022.113813
- 源文件：19983_2022_social-influence-based-contrast-language-analysis-framework-for-clinical-decision-support-system.md
- 论文主类型：build_evaluate_design_science
- 主导写作弧线：problem_theory_design_test_return
- 置信度：0.42

## 文章级论证概况

- 核心问题：如何利用在线社交网络中的用户生成内容及其社会互动结构，提取能够区分抑郁与非抑郁用户语言使用差异的“社会影响对比语言特征”，从而增强临床决策支持系统（CDSS）在抑郁症早期检测、干预和治疗计划方面的功能与可解释性？

- 制品与设计：提出一个社会影响对比语言分析框架（Social influence-based contrast language analysis framework），包含三类特征提取流程：词项级对比特征（n-gram频率比率+p值显著性排序）、主题级对比特征（分别建立LDA主题模型并用软余弦相似度选取同语境中最判别主题）、网络级对比特征（基于抑郁症状态网络MSN、社交距离倒数影响分数与内容向量余弦相似度计算NBC值），并将框架嵌入数据驱动CDSS的组件交互。

- 客观结果：在1047名Facebook用户、197230条状态更新的真实数据集上，CART分类器在早期抑郁检测任务上达到69.05%准确率、76.19%精确率、66.67%召回率和71.11% F值；所提对比特征组合在多个实验设置下优于LIWC、SBERT、一般LDA主题特征和RFE特征选择基线。

- 核心贡献：作者声称的主要贡献是：提出并验证一个基于社会影响理论的对比语言分析框架，通过词项、主题和网络三个层面的可解释对比特征弥补模型准确性与可解释性之间的差距，并以此增强CDSS在早期诊断、早期干预和个性化治疗计划中的决策支持功能，同时保持用户匿名性。

- 整篇论证链：文章以抑郁症的普遍性和严重性为起点，指出现有CDSS依赖自报式调查与访谈数据，导致数据质量低、早期检测困难；随后说明虽然数据驱动CDSS和用户生成内容为检测提供了可能，但现有研究多孤立分析用户内容，忽略用户之间的社会互动，且预测模型缺乏可解释性。作者由此引入社会影响理论，论证个体的态度、语言和行为会受到网络中重要他人的影响，抑郁与非抑郁群体在在线社区会形成不同的语言规范，从而提出一个核心缺口：缺乏既能解释语言差异又能考虑社会影响的对比特征。围绕该缺口，文章设计了词项级、主题级和网络级三类对比特征，其中内容级特征（词项、主题）是网络级特征的输入，网络级特征以心理健康状态网络MSN为结构基础，结合距离倒数影响权重和内容向量相似度计算用户受不同群体影响的程度。在真实Facebook数据上，作者先展示三类特征的可解释性（词项聚类、主题对比、NBC与抑郁标签的关系），再用四种ML分类器和多个baseline（LIWC、GTF、RFE、SBERT）以及特征组合消融实验验证早期抑郁检测性能，证明所提特征能显著提升检测效果。讨论部分把结果重新连接到引言中的可解释性缺口，并声明该框架可推广到其他多群体语言对比场景，形成面向CDSS的可复用设计知识。

## 类型与写作弧线判定

- 论文主类型判定：文章的核心动作是先提出一个面向CDSS需求的分析框架（含数据处理、特征程序、CDSS组件交互），再通过真实数据集上的案例和用户研究进行评价；研究目标不仅是最优性能，更强调设计出的特征对临床决策的可解释性和可操作性。虽然包含计算实验和benchmark，但研究以“需求—构建—评价—设计知识”为主线，属于设计科学研究范式。

- 主导写作弧线判定：论证从现实问题（抑郁症早期检测难）出发，引入社会影响理论形成知识基础，据此推出一组设计要求并构建三类对比特征；随后以真实数据实验检验特征的有效性，最终在讨论部分回到理论缺口，将结果升华为对CDSS功能和知识库的贡献。该弧线符合“问题—理论—设计—检验—回到理论”。

## 研究开展程序

- study_or_phase_count：7

- 研究阶段总序列：研究包括概念设计、数据准备、三类特征提取方法、真实数据探索性分析、预测实验和特征重要性验证，共七个阶段。前四个阶段为构建阶段，后三个阶段为评价阶段；特征是累积的：内容级词项和主题特征为网络级特征提供内容向量输入，最后分类实验使用全部或子集特征进行验证。

### studies_or_phases

#### 1. 概念框架设计与CDSS集成规划

- order：1

- name_cn：概念框架设计与CDSS集成规划

- question_cn：什么样的分析框架能够同时考虑用户内容和社交网络结构，为CDSS提供可解释的抑郁检测支持？

- inputs_and_setting_cn：基于已有CDSS架构、在线社交平台、语音识别、案例推理、规则引擎、模型组件等概念组件。

- designed_or_compared_object_cn：设计整体社会影响对比语言分析框架及其与CDSS的交互接口。

- baseline_control_or_counterfactual_cn：对照传统CDSS依赖调查/访谈数据的模式。

##### objective_metrics

（空）

- analysis_method_cn：概念设计、系统架构推演、文献综合。

- main_result_cn：形成图1所示的集成了数据集成、特征提取、下游任务的CDSS框架蓝图。

- argumentative_role_cn：将问题转化为可实现的系统需求，界定研究边界和功能目标。

- remaining_uncertainty_cn：框架的实际数据处理和特征提取是否有效尚未验证。

- link_to_next_phase_cn：为后续的数据准备和特征提取程序提供设计蓝图。

##### evidence_pointers

1. Framework section, Fig. 1

2. Section 3.2 'Interactions with other data-driven components in a CDSS'

#### 2. 数据准备与抑郁标签构建

- order：2

- name_cn：数据准备与抑郁标签构建

- question_cn：如何将原始Facebook状态更新和CES-D问卷分数转换为可用的对比分析输入？

- inputs_and_setting_cn：Kosinski等提供的Facebook用户状态更新及CES-D心理问卷数据。

- designed_or_compared_object_cn：经过聚合、清洗、词形还原、停用词处理的用户语料；二元抑郁/非抑郁标签。

- baseline_control_or_counterfactual_cn：以CES-D阈值25作为抑郁判定的依据。

##### objective_metrics

1. 用户数1047

2. 状态更新数197230

3. 标签分布（569抑郁/478非抑郁）

- analysis_method_cn：SymSpell拼写检查、HTML去噪、词形还原、NLTK停用词、匿名ID聚合。

- main_result_cn：生成可以直接用于特征提取的两组用户语料和标签。

- argumentative_role_cn：确保后续特征差异可归因于用户群体差异而非文本噪声。

- remaining_uncertainty_cn：阈值25的临床适用性依赖文献，但不同人群可能不同。

- link_to_next_phase_cn：预处理后的语料被用于词项级和主题级特征发现。

##### evidence_pointers

1. Section 3.1 'Data preparation'

#### 3. 词项级和主题级内容对比特征方法设计

- order：3

- name_cn：词项级和主题级内容对比特征方法设计

- question_cn：如何从两个用户群体的语料中提取最能区分的词项和主题？

- inputs_and_setting_cn：预处理后的抑郁/非抑郁用户状态更新语料。

- designed_or_compared_object_cn：词项级对比特征（n-gram频率比率差值+p值排序）和主题级对比特征（独立LDA+软余弦相似度选同语境中最判别主题）。

- baseline_control_or_counterfactual_cn：与一般LDA主题模型、Rayson和Garside的关键词发现方法相对照。

##### objective_metrics

1. p值排名

2. 主题一致性分数

3. 软余弦相似度

- analysis_method_cn：公式(1)-(3)计算TF比率差；log-likelihood p值显著性检验；LDA+Mallet；软余弦相似度公式(4)；公式(5)-(8)选取最小μ主题。

- main_result_cn：形成两类可解释的内容级对比特征提取程序；Table 2给出示例词项，Fig 4给出主题选取示例。

- argumentative_role_cn：为网络级特征提供用户内容向量基础，同时被论证为能产生可解释的临床洞察。

- remaining_uncertainty_cn：这些特征在真实数据上是否呈现预期差异尚未验证。

- link_to_next_phase_cn：将内容对比特征向量作为网络级对比特征提取的输入。

##### evidence_pointers

1. Section 3.3.1 'Content-based contrast features discovery'

2. Table 2, Fig. 2, Fig. 3, Fig. 4

#### 4. 网络级社会影响对比特征方法设计

- order：4

- name_cn：网络级社会影响对比特征方法设计

- question_cn：如何利用社交网络结构刻画抑郁/非抑郁朋友对用户语言和内容的影响差异？

- inputs_and_setting_cn：心理健康状态网络MSN（用户节点和抑郁症状态连接）；内容级对比特征生成的用户内容向量。

- designed_or_compared_object_cn：网络级对比特征NBC_d和NBC_nd：结合社交距离倒数影响分数与内容向量余弦相似度。

- baseline_control_or_counterfactual_cn：对照只使用内容特征而不考虑网络结构的做法。

##### objective_metrics

1. NBC_d

2. NBC_nd

3. 余弦相似度

4. 社交影响分数

- analysis_method_cn：公式(9)定义影响分数；公式(10)-(13)计算加权NBC；Algorithm 1给出伪代码。

- main_result_cn：形成可计算的网络级对比特征算法。

- argumentative_role_cn：将社会影响理论转化为可操作特征，体现框架对网络结构知识的利用。

- remaining_uncertainty_cn：NBC特征是否与实际抑郁状态相关尚未验证。

- link_to_next_phase_cn：为后续探索性分析和分类实验提供新的输入特征。

##### evidence_pointers

1. Section 3.3.2 'Network-based contrast features'

2. Fig. 5, Fig. 6, Algorithm 1

#### 5. 对比特征的探索性分析

- order：5

- name_cn：对比特征的探索性分析

- question_cn：所提出的三类对比特征在真实Facebook数据上是否表现出可解释的群体差异？

- inputs_and_setting_cn：1047名用户的状态更新、CES-D标签、MSN结构。

- designed_or_compared_object_cn：分析词项级对比特征分布、主题级对比内容、网络级NBC数值与标签的关系。

- baseline_control_or_counterfactual_cn：以文献中已有抑郁语言特征（如第一人称代词、负性词）作为内部参照。

##### objective_metrics

1. 词项频率差异

2. 主题词分布

3. NBC_d/NBC_nd数值比较

4. 聚类可视化

- analysis_method_cn：频率分布图、SBERT嵌入+PCA聚类、LDA主题词比较、散点图。

- main_result_cn：抑郁组明显更多第一人称和负性词；非抑郁组更多时间/事件词；主题对比显示抑郁主题负性情绪更强；NBC表显示抑郁用户NBC_d高于NBC_nd，非抑郁用户相反，且呈现负向趋势。

- argumentative_role_cn：证明特征具有面向上临床解释的可理解性和区分度，为后续预测实验提供机制性证据。

- remaining_uncertainty_cn：探索性观察未控制混淆变量，也没有评估预测性能。

- link_to_next_phase_cn：促使作者进入分类实验以量化特征的预测价值。

##### evidence_pointers

1. Section 4.1 'Exploratory analysis of network-based contrast features'

2. Section 4.2 'Exploratory analysis of content-based contrast features'

3. Table 3, Fig. 7, Fig. 8, Fig. 9, Fig. 10, Fig. 11

#### 6. 早期抑郁检测用户研究（分类实验）

- order：6

- name_cn：早期抑郁检测用户研究（分类实验）

- question_cn：包含词项、主题和网络级对比特征的特征集是否能在早期抑郁检测中优于常见基线和一般特征方法？

- inputs_and_setting_cn：同一Facebook数据集；特征集FS1-FS8；基线LIWC、GTF、RFE、SBERT；分类器LR、KNN、NN、CART。

- designed_or_compared_object_cn：对比特征组合与baseline特征；以及不同分类器性能。

- baseline_control_or_counterfactual_cn：LIWC、一般LDA主题特征（GTF）、RFE特征选择、SBERT嵌入基线；FS1-FS8内部组合用于分离各组件贡献。

##### objective_metrics

1. Accuracy

2. Precision

3. Recall

4. F-Score

- analysis_method_cn：80/20训练测试划分；四种监督ML算法；特征集消融比较。

- main_result_cn：CART性能最佳；大多数含对比特征的集合超过LIWC和SBERT；FS1优于GTF；FS4/FS8优于RFE；FS6-FS8单独对比特征也全部优于SBERT；但使用所有对比特征并非总是最优。

- argumentative_role_cn：为框架的有效性提供量化证据，并区分各特征组件对性能的贡献。

- remaining_uncertainty_cn：单一数据集、单一标签阈值、缺少与其他先进深度模型的比较；未控制问卷时间和状态更新时间之间的关系造成的选择偏差。

- link_to_next_phase_cn：进一步分析特征重要性以解释哪些特征驱动预测。

##### evidence_pointers

1. Section 4.3 'User study: early depression detection in mental status networks'

2. Fig. 12, Fig. 13, Table 5

#### 7. 特征重要性分析

- order：7

- name_cn：特征重要性分析

- question_cn：在所有特征中，哪些社会影响对比特征对早期抑郁检测最重要？

- inputs_and_setting_cn：用户研究中的最优模型CART和全部特征。

- designed_or_compared_object_cn：对比主题级、词项级和网络级特征的相对重要性。

- baseline_control_or_counterfactual_cn：不设置外部对照，只进行特征排名。

##### objective_metrics

1. 特征重要性排序

- analysis_method_cn：CART模型特征重要性（top-20）。

- main_result_cn：主题级对比特征最重要，其次是非抑郁组词项特征如“week”“last”“answer”和抑郁组词项特征如“sick”“heart”“alone”，网络级非抑郁特征也是关键驱动因素。

- argumentative_role_cn：将分类性能落实到具体可解释特征，进一步支持框架的可解释性主张。

- remaining_uncertainty_cn：特征重要性来自单一模型，泛化性未验证。

- link_to_next_phase_cn：讨论部分将特征重要性结果升华为临床可操作洞察和未来研究方向。

##### evidence_pointers

1. Section 4.3, Fig. 14

## 各部分修辞架构

### abstract_moves

1. 先确立问题严重性和社交网络作为补充信息源的潜力（CONTEXT/PHENOMENON）

2. 再提出框架目标和三类特征流程（RQ_OR_OBJECTIVE/STUDY_OVERVIEW）

3. 最后声明案例验证、方法论贡献和与CDSS的结合（RESULT/CONTRIBUTION）

### introduction_moves

1. 从全球抑郁负担和自杀后果建立现实急迫性

2. 指出传统CDSS依赖自报调查和访谈造成数据质量低和早期检测困难

3. 引入数据驱动CDSS和UGC的可行性，同时指出内容分析忽略互动特征

4. 引入社会影响理论说明网络互动影响语言和心理状态的机制

5. 将缺口定义为缺乏可解释的、考虑社会影响的对比语言特征

6. 提出框架目标并依次描述三类特征方向，预告论文结构

### theory_and_knowledge_moves

1. 文献综述先说明在线平台用于心理健康研究的既有成果

2. 再综述社会影响理论及其在信息系统和健康社区中的应用

3. 综述UGC分析方法（n-grams、LDA、LIWC）并小结其孤立内容文本的局限

4. 综述抑郁与非抑郁群体语言差异的实证发现（更多负性词、第一人称代词等）

5. 通过情绪感染文献论证需要将社会影响引入语言对比

6. 用表1比较现有研究与本文在语言/主题/网络/对比分析四个维度上的差异

### artifact_design_moves

1. 先给出框架概念图并集成到CDSS数据驱动接口

2. 描述数据准备和标签构建的具体做法

3. 提出词项级对比特征：频率比率差+p值排序

4. 提出主题级对比特征：独立LDA+软余弦相似度+同语境中最判别主题

5. 提出网络级对比特征：MSN定义、距离倒数影响分数、NBC公式

6. 说明框架与CDSS下游任务（早期检测、干预、治疗方案）的对接

### evaluation_moves

1. 用探索性分析展示词项聚类和主题对比的可解释性

2. 用NBC数值与抑郁标签的对应关系和散点趋势展示网络特征与标签的联系

3. 分类实验采用四种经典ML算法和四个基线

4. 设置FS1-FS8特征集以分离各组件贡献

5. 报告CART最优性能和各特征集对比结果

6. 用特征重要性排序解释模型驱动因素

### discussion_and_contribution_moves

1. 回到引言中的准确性与可解释性差距，声明本框架为此而设计

2. 将特征发现过程描述为从词项到主题再到网络的三层扩展

3. 将实用含义扩展为临床理解患者、引导面谈、识别高风险非抑郁用户

4. 将框架推广到其他精神障碍、金融情绪和电商双边评论等场景

5. 结论部分总结贡献并承认抑郁强度层次和个性化治疗方向的局限

## 理论/知识到设计的翻译

### 知识/理论基础

1. 社会影响理论（Kelman, 1958）

2. 社会学习理论（Bandura）

3. 虚拟社区参与和社会认同（Bagozzi等）

4. 情绪感染研究（Neumann & Strack）

5. 在线健康社区社会支持研究（Yan & Tan）

6. 对比语言和心理健康语言差异研究（Rude、Slonim、Nguyen等）

7. 社会网络影响力分析（Tang、Zhang等）

8. NLP/ML：LDA、软余弦相似度、SBERT、LIWC

- 理论—设计耦合：partial

- 耦合判定理由：社会影响理论提供了“个体受网络他人影响”的核心论证和网络级特征的设计动机，也解释了为什么需要对比语言特征；但词项级和主题级的具体技术选择（n-gram频率差、LDA+软余弦）主要来自NLP方法传统和对比语料库分析技术，而非由社会影响理论严格推导。网络级特征则更直接来自理论中的影响机制（距离、相似度）。因此理论对总体框架和网络特征是前瞻性指导，但部分技术细节来自其他知识源。

- 理论到设计翻译链：社会影响理论命题（人们的态度/语言受重要他人影响）→ 在线社区中抑郁和非抑郁用户形成不同语言规范 → 需要同时分析内容差异和互动影响 → 提取词项/主题内容向量 → 在MSN中以距离倒数定义影响分数 → 用内容向量相似度衡量影响方向 → 生成NBC对比特征 → 输入分类器实现早期抑郁检测。

### mapping_table

#### 1. 1

- theory_or_knowledge_claim_cn：社会影响理论：个体态度、信念和行为受重要他人影响

- mechanism_cn：用户的内容和情绪受其社交网络中朋友的内容影响，距离近则影响大

- design_requirement_cn：特征提取必须考虑网络结构，不能只看孤立文本

- artifact_choice_cn：MSN网络定义 + 距离倒数影响分数 + 内容向量相似度 → NBC_d/NBC_nd

- evaluated_contrast_cn：抑郁用户与非抑郁用户的NBC特征差异；与抑郁/非抑郁朋友内容的相似方向

- objective_result_cn：Table 3中抑郁用户NBC_d高于NBC_nd，非抑郁用户反之；Fig 7呈下降趋势

##### evidence_pointers

1. Section 4.1, Table 3, Fig. 7

#### 2. 2

- theory_or_knowledge_claim_cn：在线社区形成共享规范、行为和语言，包括术语和缩略语

- mechanism_cn：抑郁与非抑郁群体在语言风格和主题上发生分化，形成可观测的对比语言模式

- design_requirement_cn：需要识别群体间有判别力的词项和主题

- artifact_choice_cn：词项级对比特征（频率比率差+p值排序）+ 主题级对比特征（LDA+软余弦）

- evaluated_contrast_cn：抑郁与非抑郁组top-k词项和对比主题

- objective_result_cn：抑郁组更多第一人称和负性词；非抑郁组更多时间/事件词；对比主题负性情绪不同

##### evidence_pointers

1. Section 4.2, Table 2, Fig. 8, Fig. 9, Fig. 11

#### 3. 3

- theory_or_knowledge_claim_cn：情绪感染和坏心情可以通过社交互动从一个人传递到另一个人

- mechanism_cn：用户发布的内容会影响朋友的感受，因此朋友的抑郁/非抑郁状态内容可能影响目标用户的语言状态

- design_requirement_cn：内容相似性应与社会影响结合，量化朋友影响的方向和强度

- artifact_choice_cn：将词项/主题对比特征转为用户内容向量，计算与邻居内容的加权相似度

- evaluated_contrast_cn：NBC_d与NBC_nd的数值关系

- objective_result_cn：NBC_d与NBC_nd在不同用户组呈反向关系，支持影响方向假设

##### evidence_pointers

1. Section 3.3.2, Section 4.1

#### 4. 4

- theory_or_knowledge_claim_cn：现有研究发现抑郁患者使用更多负性词和第一人称代词

- mechanism_cn：语言特征可以直接反映用户的认知和情绪状态

- design_requirement_cn：对比特征应保留可解释的语言单位（词项/主题）而非黑盒表示

- artifact_choice_cn：词项级保留具体n-gram展示；主题级保留top词展示；用SBERT+PCA可视化聚类

- evaluated_contrast_cn：对比特征的聚类分布和主题词表

- objective_result_cn：词项聚类在嵌入空间中明显分开；抑郁主题含更多负性词

##### evidence_pointers

1. Section 4.2.1, Fig. 9; Section 4.2.2, Fig. 11

## 评价逻辑

### evaluation_modes

1. 探索性特征分析（词项聚类、主题对比、NBC与标签关系）

2. 监督分类实验（四种ML算法）

3. 多baseline对比（LIWC、GTF、RFE、SBERT）

4. 特征集消融（FS1-FS8）

5. 特征重要性分析

- why_these_evaluations_cn：首先通过探索性分析检验特征在真实语言数据上是否呈现可解释的群体差异，回答“特征看起来对吗”；再用分类实验量化特征是否对预测有效；通过baseline对比回答“比已有方法好吗”；通过特征集消融回答“每个组件贡献多少”；通过特征重要性回答“哪些特征最值得临床关注”。这种递进评价既覆盖了构建类工作的可解释性需求，又覆盖了计算性能需求。

- benchmark_and_contrast_chain_cn：基线设置从传统语言特征LIWC起步，再加入一般LDA主题模型GTF，说明对比主题优于一般主题；利用RFE特征选择说明“我们选择的判别特征”优于“通用递归消除特征”；用SBERT嵌入说明在相同原始文本上，对比特征优于通用深层语义向量；FS1-FS5与LIWC组合逐步加入topic/network/term组件；FS6-FS8只用对比特征不依赖LIWC。该链条逐步把性能差异归因于三组件的组合价值。

### claim_evidence_ledger

#### 1. 所提社会影响对比语言特征能有效检测早期抑郁

- claim_cn：所提社会影响对比语言特征能有效检测早期抑郁

- evidence_pointer：Fig 12, Fig 13, Section 4.3

- evaluation_cn：四种分类器中CART最优，且含对比特征的多数特征集超过LIWC和SBERT基线

- overclaim_check_cn：性能提升在特定数据集和特征子集上成立，并非所有组合一致最优；未与最新深度模型比较

#### 2. 词项、主题和网络三个层面特征各自具有贡献

- claim_cn：词项、主题和网络三个层面特征各自具有贡献

- evidence_pointer：FS1-FS8对比结果和Fig 14特征重要性

- evaluation_cn：FS1优于GTF说明主题级对比特征优于一般主题；FS4/FS8优于RFE说明选择方法有效；NBC特征被列为重要特征

- overclaim_check_cn：FS2（仅network）和FS1（仅topic）的直接对比信息不足；没有进行所有组件的严格正交消融

#### 3. 抑郁和非抑郁朋友对用户有对比影响

- claim_cn：抑郁和非抑郁朋友对用户有对比影响

- evidence_pointer：Table 3, Fig 7

- evaluation_cn：示例用户NBC_d/NBC_nd与标签匹配，散点呈下降趋势

- overclaim_check_cn：这是探索性相关性证据，非因果；样本量小，未控制用户自身内容对朋友影响的逆因果

#### 4. 框架能解决模型准确性与可解释性的差距并提供临床决策支持

- claim_cn：框架能解决模型准确性与可解释性的差距并提供临床决策支持

- evidence_pointer：Section 5.1, Fig 8-11, Fig 14

- evaluation_cn：特征以词项、主题和网络数值形式呈现，能够被解释并用于临床洞察

- overclaim_check_cn：没有与真实临床医生进行有用性评估；可解释性来自研究者叙述而非临床工作者测试

#### 5. 框架可推广到其他领域和多群体场景

- claim_cn：框架可推广到其他领域和多群体场景

- evidence_pointer：Section 5.2

- evaluation_cn：概念性论述，无实证支持

- overclaim_check_cn：属于前瞻性声明，未经跨场景验证

- internal_validity_strategy_cn：使用固定分类器CART进行特征集比较以降低模型差异影响；采用多个baseline和特征子集以隔离组件贡献；报告多个性能指标避免单一指标偏差；使用CES-D阈值和早期检测的时间窗口定义以减少预测目标模糊。

- external_validity_strategy_cn：使用真实Facebook数据和标准心理量表标签；强调框架适用于任何在线社交网络；通过引用已有文献语言差异发现作为交叉验证。

- what_is_not_actually_tested_cn：未进行现场临床使用评估；未检验临床医生是否认为特征可操作；未测试不同平台、不同抑郁严重度、不同年龄段/文化群体；网络影响的因果方向未验证；隐私保护机制只是声明引用，未进行安全性验证。

## 贡献闭环

- technical_claim_cn：提出一个新的三层次对比特征提取方法，其中主题级对比特征采用独立LDA+软余弦相似度选择同语境中最判别主题，网络级对比特征采用距离倒数影响分数与内容相似度组合，在抑郁症检测任务上取得优于LIWC、GTF、RFE、SBERT的性能。

- artifact_claim_cn：构建了一个可嵌入CDSS的社会影响对比语言分析框架；词项、主题和网络三类特征在不同程度上提高了早期抑郁检测的准确率、精确率、召回率和F值。

- mechanism_claim_cn：抑郁/非抑郁朋友在MSN中的内容对目标用户有对比影响；用户受影响的方向可通过NBC特征反映，且用户更容易与同类状态朋友产生内容相似。

- boundary_claim_cn：框架适用于包含在线社交互动的数据场景，可扩展到多类用户对比和心理健康之外的领域；但内容级对比特征需要用户产生足够的文本，网络级特征需要可获取的朋友状态标签。

- reusable_design_knowledge_cn：可复用知识包括：对比特征设计原则（先词项/主题内容特征，再叠加网络结构特征）、主题对比选择程序（同语境中最判别主题）、影响权重设计（距离倒数）、评价流程（探索性分析+分类实验+特征重要性）。

- theoretical_contribution_cn：将社会影响理论引入CDSS和抑郁语言对比分析，把“群体语言差异”从静态内容特征扩展为动态网络影响特征；但理论本身并未被修正或扩展，更多是为特征设计提供合理性依据。

- how_discussion_closes_intro_gap_cn：讨论部分回顾引言中提出的“缺乏可解释性”和“忽略社会互动”两个缺口，重申本框架提供的三类可解释对比特征能够填补准确性-可解释性差距，并通过网络级特征把社会影响理论转化为可操作的临床决策支持。

- overclaim_or_unsupported_leaps_cn：从NBC相关模式推导“影响方向”存在因果跳跃；从单一Facebook数据集和CART模型概括到所有CDSS场景过于宽泛；“隐私保护”只引用文献并未实际设计新机制；可扩展到其他心理障碍和电商场景属于概念性声明。

## 句级写作动作图谱

### 1. P1 S1

- order：1

- section：Abstract

- locator：P1 S1

- move_code：CONTEXT

- paraphrase_cn：抑郁是全球主要心理健康问题，影响3亿人。

- rhetorical_function_cn：开篇建立问题的严重性和规模。

- depends_on_cn：不依赖前文。

- sets_up_cn：为后续提出数字解决方案提供现实紧迫性。

- evidence_pointer：Abstract P1

### 2. P1 S2

- order：2

- section：Abstract

- locator：P1 S2

- move_code：PHENOMENON

- paraphrase_cn：社交网络为心理健康专业人员提供了患者补充信息的巨大潜力。

- rhetorical_function_cn：建立从社交网络数据入手的切入现象。

- depends_on_cn：依赖抑郁问题严重性。

- sets_up_cn：引出本研究的数据来源方向。

- evidence_pointer：Abstract P1

### 3. P2 S1

- order：3

- section：Abstract

- locator：P2 S1

- move_code：RQ_OR_OBJECTIVE

- paraphrase_cn：本研究提出一种用于CDSS的方法框架，通过分析社交网络数据区分有早期抑郁迹象用户的语言使用，即对比语言分析。

- rhetorical_function_cn：明确研究问题与目标制品。

- depends_on_cn：依赖前两句建立的现实和数据潜力。

- sets_up_cn：为摘要剩余部分的特征流程预告做铺垫。

- evidence_pointer：Abstract P2

### 4. P3 S1-S3

- order：4

- section：Abstract

- locator：P3 S1-S3

- move_code：STUDY_OVERVIEW

- paraphrase_cn：先通过词项百分比差异发现对比词，再构建主题模型获得主题级对比特征，最后考虑网络结构发现网络级对比特征。

- rhetorical_function_cn：预告三类特征的有序发现过程。

- depends_on_cn：依赖研究目标的提出。

- sets_up_cn：让读者预期本文的方法结构。

- evidence_pointer：Abstract P3

### 5. P4 S1-S2

- order：5

- section：Abstract

- locator：P4 S1-S2

- move_code：CONTRIBUTION

- paraphrase_cn：用真实数据集案例研究展示有效性；在方法论上增强CDSS功能，并以低成本和数据分析补充传统调查与访谈。

- rhetorical_function_cn：在摘要中先声明贡献与证据。

- depends_on_cn：依赖特征流程的设计框架。

- sets_up_cn：为正文引言中的贡献论证提供浓缩版。

- evidence_pointer：Abstract P4

### 6. P1 S1-S4

- order：6

- section：Introduction

- locator：P1 S1-S4

- move_code：CONTEXT

- paraphrase_cn：抑郁是残疾主因且社会成本快速增长，并可能造成工作、学校、关系受损，甚至导致15-29岁人群第二大死因自杀。

- rhetorical_function_cn：用数据描述全球抑郁负担。

- depends_on_cn：不依赖前文。

- sets_up_cn：为论证CDSS必要性提供现实背景。

- evidence_pointer：Introduction P1

### 7. P1 S5-S7

- order：7

- section：Introduction

- locator：P1 S5-S7

- move_code：LIMITATION

- paraphrase_cn：传统CDSS主要依赖调查和访谈，资源消耗大且一对一接触，数据自报、受心理状态影响，质量低，因此很难早期发现高风险抑郁患者。

- rhetorical_function_cn：指出现有系统在数据源层面的核心限制。

- depends_on_cn：依赖抑郁问题严重性作为背景。

- sets_up_cn：为引入数据驱动CDSS和UGC替代方案做铺垫。

- evidence_pointer：Introduction P1

### 8. P2 S1-S4

- order：8

- section：Introduction

- locator：P2 S1-S4

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：随着EHR部署，数据驱动CDSS成为可行替代，功能不仅依赖结构化临床数据，还依赖患者交互产生的用户生成内容。

- rhetorical_function_cn：导入已有知识和最新技术背景。

- depends_on_cn：针对传统CDSS限制提出替代路径。

- sets_up_cn：为引入语言特征作为UGC基础做铺垫。

- evidence_pointer：Introduction P2

### 9. P2 S4

- order：9

- section：Introduction

- locator：P2 S4

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：在心理健康领域，语言是心理状态和情绪的最强反映，因此用户生成内容中的语言特征成为以往方法发掘信息词和主题的基础组件。

- rhetorical_function_cn：把语言特征定位为抑郁检测的关键。

- depends_on_cn：依赖UGC作为数据源的可行性论证。

- sets_up_cn：为后文指出内容分析忽略互动特征做对比。

- evidence_pointer：Introduction P2

### 10. P3 S1

- order：10

- section：Introduction

- locator：P3 S1

- move_code：LIMITATION

- paraphrase_cn：虽然内容分析能理解心理状态，但底层用户互动特征如患者之间、医患之间互动大多被忽略。

- rhetorical_function_cn：给出内容分析方法的主要缺口。

- depends_on_cn：承认内容分析的价值但指出其局限性。

- sets_up_cn：引入社会影响理论。

- evidence_pointer：Introduction P3

### 11. P3 S2-S4

- order：11

- section：Introduction

- locator：P3 S2-S4

- move_code：THEORY_INTRO

- paraphrase_cn：社会影响理论认为个体态度、信念和行为受重要他人影响；在线社交互动是参与语境中的有意社会行动；用户会形成群体规范和社会凝聚力，包括使用术语或缩略语的共享语言。

- rhetorical_function_cn：为社会影响特征提供理论合法化。

- depends_on_cn：基于对内容分析局限的指认。

- sets_up_cn：为后续将网络结构和语言对比结合提供理论基础。

- evidence_pointer：Introduction P3

### 12. P3 S5-S7

- order：12

- section：Introduction

- locator：P3 S5-S7

- move_code：GAP

- paraphrase_cn：网络社会过程有潜力增强CDSS，但现有方法性能虽好却缺乏可解释性，无法解释抑郁与非抑郁用户的语言和内容差异；高患病率、数据获取障碍和缺乏可解释性导致大量未确诊患者。

- rhetorical_function_cn：整合多个缺口形成研究必要性的高峰。

- depends_on_cn：依赖社会影响理论的引入。

- sets_up_cn：为提出研究目标和框架做铺垫。

- evidence_pointer：Introduction P3

### 13. P4 S1-S2

- order：13

- section：Introduction

- locator：P4 S1-S2

- move_code：RQ_OR_OBJECTIVE

- paraphrase_cn：本研究旨在通过提出社会影响对比语言分析框架来增强CDSS的功能与决策支持，该框架结合NLP和ML，检测抑郁并可能提供早期干预和定制治疗计划的主动建议。

- rhetorical_function_cn：明确提出研究目标。

- depends_on_cn：依赖前文缺口论证。

- sets_up_cn：为框架的具体特征描述做引导。

- evidence_pointer：Introduction P4

### 14. P4 S3-S4

- order：14

- section：Introduction

- locator：P4 S3-S4

- move_code：DESIGN_FEATURE

- paraphrase_cn：框架提取‘社会影响对比语言模式’，即区分抑郁和非抑郁用户在情绪表达及对他人影响方面的语言特征；例如抑郁用户可能更多用‘sad’等负面词，非抑郁用户则更多用正面词，并认为朋友内容的情绪极性可能影响用户情绪。

- rhetorical_function_cn：具体化框架将要提取的特征类型。

- depends_on_cn：基于社会影响理论和研究目标。

- sets_up_cn：让读者理解三类特征背后想表达的对比模式。

- evidence_pointer：Introduction P4

### 15. P4 S5-S6

- order：15

- section：Introduction

- locator：P4 S5-S6

- move_code：CONTRIBUTION

- paraphrase_cn：除了方法论贡献，框架解决了准确性与可解释性之间的差距，为临床提供可操作的洞察，并通过隐私保护机制缓解隐私疑虑。

- rhetorical_function_cn：声明多层次的贡献。

- depends_on_cn：依赖框架设计描述。

- sets_up_cn：为讨论部分贡献主张提供早期预告。

- evidence_pointer：Introduction P4

### 16. P5 S1

- order：16

- section：Introduction

- locator：P5 S1

- move_code：TRANSITION

- paraphrase_cn：预告后续章节结构：理论综述、框架、实验、讨论和结论。

- rhetorical_function_cn：提供阅读地图。

- depends_on_cn：不依赖具体论证。

- sets_up_cn：为读者建立结构预期。

- evidence_pointer：Introduction P5

### 17. P1 S1-S6

- order：17

- section：Literature Review 2.1

- locator：P1 S1-S6

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：在线社交平台研究心理健康已成为热点，多个研究用状态更新、微博、Twitter数据识别抑郁症状、自杀污名、情绪变化和意见领袖影响力。

- rhetorical_function_cn：梳理已有证据显示社交媒体可用于心理健康分析。

- depends_on_cn：不依赖前文，是文献综述起点。

- sets_up_cn：为后续点出这些研究大多孤立分析内容做铺垫。

- evidence_pointer：Section 2.1 P1

### 18. P2 S1-S6

- order：18

- section：Literature Review 2.1

- locator：P2 S1-S6

- move_code：THEORY_INTRO

- paraphrase_cn：社会影响理论指出个体态度行为通过顺从、认同、内化机制受他人影响；社会学习发生在与信任朋友的交流中；相关研究考察知识管理使用、Facebook参与、患者支持交换和戒烟社区等。

- rhetorical_function_cn：扩展社会影响理论在不同信息系统场景中的应用证据。

- depends_on_cn：与引言中理论引入相呼应。

- sets_up_cn：为框架中网络结构特征提供理论支持。

- evidence_pointer：Section 2.1 P2

### 19. P1 S1-S5

- order：19

- section：Literature Review 2.2

- locator：P1 S1-S5

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：UGC语言分析主要使用n-gram和LDA主题模型，但大多数研究集中在寻找最具预测力的特征，将UGC视为独立于社交互动的数据源。

- rhetorical_function_cn：总结方法现状并指出其孤立内容分析的倾向。

- depends_on_cn：承接上一节社会影响讨论。

- sets_up_cn：为本文对比特征方法提供比较对象和缺口。

- evidence_pointer：Section 2.2 P1

### 20. P1 S6-S10

- order：20

- section：Literature Review 2.2

- locator：P1 S6-S10

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：列举Resnik、Shen&Rudzicz、Saha、Schwartz、Tadesse等研究，都用n-gram、LDA、LIWC等从Twitter、Reddit、LiveJournal、Facebook检测抑郁或焦虑。

- rhetorical_function_cn：证明既有大量方法但都依赖孤立UGC特征。

- depends_on_cn：延续对方法现状的说明。

- sets_up_cn：为后文宣称本研究是首个同时考虑影响和对比特征提供对比依据。

- evidence_pointer：Section 2.2 P1

### 21. P1 S1-S9

- order：21

- section：Literature Review 2.3

- locator：P1 S1-S9

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：不同用户组语言风格不同，抑郁用户更多负性自我暴露和第一人称代词；Rude等发现当前抑郁学生比从未抑郁者使用更多负性词和‘I’；Nguyen和Rissola等比较在线抑郁社区与其他社区的内容差异。

- rhetorical_function_cn：汇总对比语言和心理语言学的既有发现。

- depends_on_cn：作为语言对比的证据基础。

- sets_up_cn：引出社交影响而非仅内容的分析视角。

- evidence_pointer：Section 2.3 P1

### 22. P1 S10-S11

- order：22

- section：Literature Review 2.3

- locator：P1 S10-S11

- move_code：MECHANISM

- paraphrase_cn：在线用户发布的内容会影响朋友；坏心情可通过社交互动传递，因此需要基于社会影响的特征来研究语言差异和影响。

- rhetorical_function_cn：在语言差异文献后加入社会传播机制，形成本文的理论连贯性。

- depends_on_cn：依赖情绪感染文献和对比语言发现。

- sets_up_cn：为网络级对比特征提供直接依据。

- evidence_pointer：Section 2.3 P1

### 23. P2 S1-S5

- order：23

- section：Literature Review 2.3

- locator：P2 S1-S5

- move_code：GAP

- paraphrase_cn：Nguyen和Rissola只做内容分析，未考察社会影响；Yang等人虽用语言特征和意图建模/最短路径考虑社会影响，但未考虑主题级特征；本文同时考虑语言学和主题特征，并扩展了Yang等人的网络对比特征。

- rhetorical_function_cn：明确本研究相对具体前作的缺口和扩展点。

- depends_on_cn：依赖前文对相关研究的总结。

- sets_up_cn：为表1的对比框架和贡献声明提供基础。

- evidence_pointer：Section 2.3 P2

### 24. P2 S6-S7

- order：24

- section：Literature Review 2.3

- locator：P2 S6-S7

- move_code：CONTRIBUTION

- paraphrase_cn：据我们所知，本研究是第一个在使用UGC数据时同时考虑用户内容影响并提出区分抑郁/非抑郁用户特征的框架。

- rhetorical_function_cn：声明新颖性。

- depends_on_cn：依赖缺口定位和表1的文献比较。

- sets_up_cn：支撑全文的核心贡献主张。

- evidence_pointer：Section 2.3 P2, Table 1

### 25. P3 S1-S4

- order：25

- section：Literature Review 2.3

- locator：P3 S1-S4

- move_code：BOUNDARY_CONDITION

- paraphrase_cn：Contractor和DeChurch的SIP框架整合网络结构和影响机制，并指出可扩展到抑郁症检测之外；本文框架也可扩展到其他问题场景。

- rhetorical_function_cn：将社会影响理论定位为可推广的一般性视角。

- depends_on_cn：依赖于对SIP框架的引用。

- sets_up_cn：为后文讨论部分的应用扩展做铺垫。

- evidence_pointer：Section 2.3 P3

### 26. P1 S1-S4

- order：26

- section：Framework

- locator：P1 S1-S4

- move_code：DESIGN_FEATURE

- paraphrase_cn：定义社会影响对比语言分析框架：提取在在线社交中区分抑郁与非抑郁用户情绪表达的语言特征，并揭示歧视过程以支持CDSS的抑郁检测、治疗方案推荐和早期预防。

- rhetorical_function_cn：正式介绍框架定义和功能目标。

- depends_on_cn：依赖引言和文献综述建立的问题与理论。

- sets_up_cn：为图1的CDSS集成和后续特征发现细节做铺垫。

- evidence_pointer：Framework section, Fig. 1

### 27. P2 S1-S5

- order：27

- section：Framework

- locator：P2 S1-S5

- move_code：REQUIREMENT

- paraphrase_cn：框架集成到数据驱动CDSS中，数据可来自医院/诊所/患者等，预处理信息可进入不同组件以生成可视化、解释和知识库，最终输出EHR、建议、转诊或早期干预决策。

- rhetorical_function_cn：说明框架在CDSS环境中的部署方式和对数据质量的要求。

- depends_on_cn：依赖框架的整体定义。

- sets_up_cn：为3.2节讨论与其他组件交互提供上下文。

- evidence_pointer：Framework P2, Fig. 1

### 28. P1 S1-S4

- order：28

- section：Data Preparation 3.1

- locator：P1 S1-S4

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：使用Kosinski等的数据集，其中包含用户心理问卷反应和Facebook状态更新；CES-D 20题量表用于测评抑郁程度，阈值25以上标记为抑郁。

- rhetorical_function_cn：给出数据来源和标签生成的依据。

- depends_on_cn：需要框架有明确输入输出。

- sets_up_cn：保证后续对比特征是在可信标签下提取。

- evidence_pointer：Section 3.1

### 29. P2 S1-S2

- order：29

- section：Data Preparation 3.1

- locator：P2 S1-S2

- move_code：REQUIREMENT

- paraphrase_cn：将所有用户状态更新按匿名ID聚合，进行拼写纠正、去HTML/特殊字符、扩展缩写、词形还原和停用词过滤，但保留人称代词，因为文献表明‘I’与心理健康相关。

- rhetorical_function_cn：说明预处理保留哪些语言特征及原因。

- depends_on_cn：依赖CES-D标签构建。

- sets_up_cn：为词项级和主题级特征提取提供干净的语料输入。

- evidence_pointer：Section 3.1

### 30. P1

- order：30

- section：Framework 3.2

- locator：P1

- move_code：DESIGN_FEATURE

- paraphrase_cn：框架可与语音识别、案例推理、规则引擎、模型组件和自主决策组件交互；特征生成后可用于病例检索、规则生成或深度学习预测。

- rhetorical_function_cn：将框架置于CDSS组件生态中，强化其现实集成性。

- depends_on_cn：依赖图1的CDSS架构概念。

- sets_up_cn：为后文实验中的‘与模型组件交互’提供佐证。

- evidence_pointer：Section 3.2

### 31. P1

- order：31

- section：Framework 3.3

- locator：P1

- move_code：STUDY_OVERVIEW

- paraphrase_cn：特征发现分为词项级、主题级和网络级；前两类属内容级，网络级考虑网络结构并将内容特征作为输入。

- rhetorical_function_cn：介绍三类特征并说明其从属和依赖关系。

- depends_on_cn：依赖框架整体定义。

- sets_up_cn：为3.3.1和3.3.2的详细程序建立顺序。

- evidence_pointer：Section 3.3

### 32. P1-P2

- order：32

- section：Term-level features 3.3.1.1.1

- locator：P1-P2

- move_code：MECHANISM

- paraphrase_cn：文档内容可由特定词的频率和比例表示；词频在两个用户组中的差异可标识判别词项；因此过滤极高/极低频n-gram，用公式计算相对词频和比率差。

- rhetorical_function_cn：解释词项特征为什么具有判别力并描述计算步骤。

- depends_on_cn：需要预处理后的语料。

- sets_up_cn：为后续p值排序形成词项级对比特征做铺垫。

- evidence_pointer：Section 3.3.1.1.1, Eqs. (1)-(3)

### 33. P3-P4

- order：33

- section：Term-level features 3.3.1.1.1

- locator：P3-P4

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：用log-likelihood p值评估词频差异的统计显著性，取p值最小的top-k词作为各组对比特征；Table 2展示UNI-gram的示例结果。

- rhetorical_function_cn：说明显著性排序和特征选择标准。

- depends_on_cn：依赖频率比率差计算。

- sets_up_cn：为实验部分具体对比词展示提供方法依据。

- evidence_pointer：Section 3.3.1.1.1, Table 2

### 34. P1

- order：34

- section：Term-level visualization 3.3.1.1.2

- locator：P1

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：单纯列表不足以支持决策，因此用SBERT嵌入将top词转成向量，用PCA降到两维并进行聚类可视化，以便观察两组词在语义空间中的分布。

- rhetorical_function_cn：引入可视化方法以增强可解释性。

- depends_on_cn：依赖词项级对比特征结果。

- sets_up_cn：为Fig 9的聚类图提供方法解释。

- evidence_pointer：Section 3.3.1.1.2, Fig. 2

### 35. P1-P2

- order：35

- section：Topic-level features 3.3.1.2

- locator：P1-P2

- move_code：LIMITATION

- paraphrase_cn：已有主题建模通常构建统一主题模型并用主题向量表示群体，无法有效指示最判别主题；因此需要新方法来提取对比主题。

- rhetorical_function_cn：指出主流主题建模方法在对比分析中的不足。

- depends_on_cn：依赖前文对LDA主题建模的综述。

- sets_up_cn：为独立运行LDA和软余弦相似度方法做铺垫。

- evidence_pointer：Section 3.3.1.2 P1-P2

### 36. P3-P5

- order：36

- section：Topic-level features 3.3.1.2

- locator：P3-P5

- move_code：DESIGN_FEATURE

- paraphrase_cn：分别对抑郁和非抑郁语料运行LDA，用coherence选择主题数；因两个语料词典不同，采用基于Levenshtein距离矩阵的软余弦相似度比较主题，并选取在同语境下最相似但差异最大的主题作为对比主题。

- rhetorical_function_cn：描述主题级对比特征的具体技术选择。

- depends_on_cn：依赖对一般主题建模局限的批判。

- sets_up_cn：为探索性分析中的主题对比表和Fig 4示例提供指令。

- evidence_pointer：Section 3.3.1.2, Eqs. (4)-(8), Fig. 3, Fig. 4

### 37. P8

- order：37

- section：Topic-level features 3.3.1.2

- locator：P8

- move_code：CONTRIBUTION

- paraphrase_cn：与Rayson和Garside只找一组关键词的语料库比较方法不同，本方法为抑郁和非抑郁组分别产生词项和主题两套对比特征。

- rhetorical_function_cn：强调方法相对于既有语料库语言学工具的增量贡献。

- depends_on_cn：依赖前文对关键词发现方法Rayson的引用。

- sets_up_cn：为框架整体新颖性提供一条具体证据。

- evidence_pointer：Section 3.3.1.2 P8

### 38. P1-P2

- order：38

- section：Network-based features 3.3.2

- locator：P1-P2

- move_code：THEORY_INTRO

- paraphrase_cn：个体心理状态受家人朋友影响；社交网络分析是捕捉社会影响的主要方式；Tang等证明用户影响取决于主题分布和社交关系；由此定义心理健康状态网络MSN。

- rhetorical_function_cn：用既有社会网络影响研究支撑网络级特征设计。

- depends_on_cn：依赖社会影响理论综述。

- sets_up_cn：为MSN定义和NBC公式做理论铺垫。

- evidence_pointer：Section 3.3.2 P1-P2, Definition 1

### 39. P3-P4

- order：39

- section：Network-based features 3.3.2

- locator：P3-P4

- move_code：DESIGN_FEATURE

- paraphrase_cn：用距离倒数定义用户对目标用户的社会影响分数；以内容向量余弦相似度衡量目标用户与邻居内容的相似程度；加权组合得到NBC_d和NBC_nd。

- rhetorical_function_cn：将理论机制转化为数学公式和特征。

- depends_on_cn：依赖内容级特征生成的用户内容向量。

- sets_up_cn：为Algorithm 1和实验中的NBC分析提供实现细节。

- evidence_pointer：Section 3.3.2, Eqs. (9)-(13), Fig. 5, Fig. 6, Algorithm 1

### 40. P1

- order：40

- section：Downstream tasks 3.4

- locator：P1

- move_code：REQUIREMENT

- paraphrase_cn：对比特征可支持三个下游任务：早期抑郁检测、早期干预和个性化治疗计划。

- rhetorical_function_cn：将特征设计与CDSS的最终功能目标挂钩。

- depends_on_cn：依赖三类特征设计完成。

- sets_up_cn：为实验设计提供应用导向。

- evidence_pointer：Section 3.4

### 41. P1

- order：41

- section：Experiment 4

- locator：P1

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：使用197230条Facebook状态更新和1047个用户的CES-D问卷分数，569名抑郁和478名非抑郁，来评估框架并展示逐步分析。

- rhetorical_function_cn：给出实验数据集和规模。

- depends_on_cn：依赖数据准备阶段的标签。

- sets_up_cn：为探索性分析和分类实验提供数据基础。

- evidence_pointer：Section 4

### 42. P1-P2

- order：42

- section：Experiment 4.1

- locator：P1-P2

- move_code：RESULT

- paraphrase_cn：NBC计算示例显示抑郁用户u1/u2的NBC_d高于NBC_nd，非抑郁用户u3/u4相反；散点图显示NBC_d和NBC_nd呈下降趋势，表明两类用户群体在网络上对用户有对比影响。

- rhetorical_function_cn：用示例和可视化展示网络级特征的区分力。

- depends_on_cn：依赖NBC公式实现。

- sets_up_cn：说明网络特征可用于衡量用户心理健康倾向。

- evidence_pointer：Section 4.1, Table 3, Fig. 7

### 43. P1-P2

- order：43

- section：Experiment 4.2.1

- locator：P1-P2

- move_code：RESULT

- paraphrase_cn：词项级对比特征分布显示抑郁组常使用第一人称和负性情绪词，非抑郁组更多使用时间、事件和活动词汇；聚类图进一步显示两组词在语义空间中分离。

- rhetorical_function_cn：展示词项级特征的可解释性和与文献的一致性。

- depends_on_cn：依赖词项对比特征提取方法。

- sets_up_cn：响应框架关于可解释性的主张。

- evidence_pointer：Section 4.2.1, Fig. 8, Fig. 9

### 44. P1-P3

- order：44

- section：Experiment 4.2.2

- locator：P1-P3

- move_code：RESULT

- paraphrase_cn：通过coherence选择各组最优主题数为10；主题词比较显示抑郁主题包含更多负性词，抑郁组对比主题含‘hate’‘fear’等，可用于新用户主题概率作为抑郁指标。

- rhetorical_function_cn：展示主题级对比特征的发现和临床可用性。

- depends_on_cn：依赖主题级特征提取方法。

- sets_up_cn：为特征重要性分析中主题重要性最高做铺垫。

- evidence_pointer：Section 4.2.2, Fig. 10, Table 4, Fig. 11

### 45. P1-P3

- order：45

- section：Experiment 4.3

- locator：P1-P3

- move_code：STUDY_OVERVIEW

- paraphrase_cn：设计早期抑郁检测用户研究，使用LR、KNN、NN、CART四种ML算法，用80%训练20%测试，比较准确率、精确率、召回率和F-score，并只统计问卷日期在最后发帖之后的预测。

- rhetorical_function_cn：介绍分类实验的设置和早期检测定义。

- depends_on_cn：依赖特征提取框架的输出。

- sets_up_cn：为基线比较和特征子集实验做铺垫。

- evidence_pointer：Section 4.3 P1-P3

### 46. P4

- order：46

- section：Experiment 4.3

- locator：P4

- move_code：BENCHMARK_OR_CONTRAST

- paraphrase_cn：设置四大基线：LIWC文本分析特征、GTF（LIWC+一般LDA主题）、RFE（递归特征消除选择非对比特征）和SBERT嵌入特征。

- rhetorical_function_cn：定义用于证明对比特征价值的参照系。

- depends_on_cn：依赖分类实验整体设计。

- sets_up_cn：为后续图13的对比结果提供对应项。

- evidence_pointer：Section 4.3 P4, Table 5

### 47. P5

- order：47

- section：Experiment 4.3

- locator：P5

- move_code：BENCHMARK_OR_CONTRAST

- paraphrase_cn：定义特征集FS1-FS8，通过LIWC与不同对比特征组合以及纯对比特征组合，分离词项、主题和网络特征的贡献。

- rhetorical_function_cn：构造消融式的特征组合设计。

- depends_on_cn：依赖基线定义。

- sets_up_cn：为结果中判断各组件价值提供结构。

- evidence_pointer：Section 4.3 P5, Table 5

### 48. P6

- order：48

- section：Experiment 4.3

- locator：P6

- move_code：RESULT

- paraphrase_cn：结果显示CART性能最佳；含对比特征的FS1-FS5大多超过LIWC和SBERT；FS1优于GTF；FS4/FS8优于RFE；FS6-FS8纯对比特征也全部优于SBERT。

- rhetorical_function_cn：报告核心性能对比结果并支持框架有效性。

- depends_on_cn：依赖特征集和基线定义。

- sets_up_cn：为讨论部分的贡献主张提供量化证据。

- evidence_pointer：Section 4.3, Fig. 12, Fig. 13

### 49. P7

- order：49

- section：Experiment 4.3

- locator：P7

- move_code：ROBUSTNESS_OR_BOUNDARY_TEST

- paraphrase_cn：使用所有对比特征并不总是最佳；FS7比FS6在准确率/精确率/F值更高，FS8在召回率更高，说明某些特征组合比‘全部包含’更好。

- rhetorical_function_cn：对‘特征越多越好’的直觉作边界约束。

- depends_on_cn：依赖FS1-FS8结果。

- sets_up_cn：提醒读者框架需要按任务选择特征子集。

- evidence_pointer：Section 4.3 P7

### 50. P8

- order：50

- section：Experiment 4.3

- locator：P8

- move_code：RESULT

- paraphrase_cn：特征重要性显示所有主题级对比特征最重要，其次是非抑郁组词项特征如‘week’‘last’‘answer’和抑郁组词项特征如‘sick’‘heart’‘alone’，网络级非抑郁特征也是重要驱动因素。

- rhetorical_function_cn：将预测性能落实到具体可解释特征。

- depends_on_cn：依赖CART分类模型和全部特征。

- sets_up_cn：为讨论中临床可操作特征主张提供细节。

- evidence_pointer：Section 4.3, Fig. 14

### 51. P1

- order：51

- section：Discussion 5.1

- locator：P1

- move_code：CONTRIBUTION

- paraphrase_cn：语言是心理状态最强反映；现有ML抑郁检测研究侧重数据驱动特征，缺乏可解释性；本框架通过社会影响对比特征解决准确性与可解释性之间的缺口。

- rhetorical_function_cn：将讨论与引言中的缺口直接闭合。

- depends_on_cn：依赖实验结果的支撑。

- sets_up_cn：为后文对三类特征的总结和扩展做铺垫。

- evidence_pointer：Section 5.1

### 52. P2

- order：52

- section：Discussion 5.1

- locator：P2

- move_code：CONTRIBUTION

- paraphrase_cn：框架从社会网络结构学习网络级对比特征，词项级、主题级和网络级特征形成完整链条，为临床医生提供更深入的心理健康理解和可解释知识。

- rhetorical_function_cn：总结框架的完整贡献链。

- depends_on_cn：依赖方法章节的三类特征设计。

- sets_up_cn：支撑实践含义和应用扩展的论述。

- evidence_pointer：Section 5.1 P2

### 53. P1-P2

- order：53

- section：Discussion 5.2

- locator：P1-P2

- move_code：BOUNDARY_CONDITION

- paraphrase_cn：框架可构建基于心理健康状态网络的预测模型，也可用于其他多类用户问题；在临床场景中能帮助专业人员理解患者、引导面谈、识别高风险非抑郁用户。

- rhetorical_function_cn：扩展框架的适用边界和实用价值。

- depends_on_cn：依赖讨论部分的贡献总结。

- sets_up_cn：为结论和未来研究方向提供桥梁。

- evidence_pointer：Section 5.2

### 54. P3

- order：54

- section：Discussion 5.2

- locator：P3

- move_code：BOUNDARY_CONDITION

- paraphrase_cn：框架可扩展到其他心理健康亚群体识别、投资者情绪与投资决策、电商双边评论与交易预测等场景。

- rhetorical_function_cn：进一步扩大框架适用范围。

- depends_on_cn：依赖框架对对比语言的通用性主张。

- sets_up_cn：为结论中的未来研究方向铺垫。

- evidence_pointer：Section 5.2 P3

### 55. P1-P2

- order：55

- section：Conclusion

- locator：P1-P2

- move_code：CONTRIBUTION

- paraphrase_cn：总结提出数据驱动分析框架，结合NLP/ML提取内容与网络对比特征；用户研究显示框架有效检测抑郁并优于基线。

- rhetorical_function_cn：压缩全文贡献和证据。

- depends_on_cn：依赖全文框架和实验。

- sets_up_cn：为后续限制和未来研究提供收束。

- evidence_pointer：Conclusion P1-P2

### 56. P3

- order：56

- section：Conclusion

- locator：P3

- move_code：LIMITATION_AND_FUTURE

- paraphrase_cn：研究未考虑抑郁强度不同阶段的语言差异；未来可构建基于案例的推荐系统，并需要与医疗专业合作开展现场研究来设计治疗计划。

- rhetorical_function_cn：承认主要限制并规划未来方向。

- depends_on_cn：依赖全文贡献声明。

- sets_up_cn：结束整篇文章。

- evidence_pointer：Conclusion P3

## 写作技术

- gap_construction_cn：作者采用多步堆叠缺口法：先指出现实问题（抑郁高发、自报数据差），再指出数据驱动CDSS的可行但受限（忽略互动，可解释性差），然后用社会影响理论把‘忽略互动’升华为理论性问题，最终将缺口定义为‘缺乏同时考虑内容差异和社会影响的、可解释的对比特征’。每一步缺口都由文献或引言中的证据支撑。

- signposting_cn：在引言结尾给出完整章节地图；在第3节开头说明三类特征的逻辑关系；在3.3节开头声明‘先内容特征后网络特征’的依赖；在实验开始时预告‘先探索性分析再分类实验’。多次使用‘First…Second…Finally’和‘as shown in Table/Fig’。

- transition_logic_cn：从数据准备到特征发现通过‘预处理信息可馈入组件’过渡；从内容特征到网络特征通过‘内容特征是网络特征的输入’过渡；从探索性分析到分类实验通过‘特征具有可区别性，因此需要量化预测力’过渡；从实验到讨论通过‘性能提升需要解释什么特征驱动’过渡。

- claim_evidence_rhythm_cn：每个主要主张都紧跟证据：先提出特征定义，随即用公式和表/图示例；先宣称可解释性，随后用聚类图和主题词表；先宣称预测有效性，随后用分类性能图；先宣称特征重要性，随后用特征重要性图。文章在结果段大量使用‘according to Fig/Table’句式。

- benchmark_narrative_cn：Benchmark设计不是随意列举，而是服务三大论证：LIWC代表传统心理语言学特征，GTF代表一般主题建模，RFE代表通用特征选择，SBERT代表通用深度语义表示；通过对比证明‘对比特征’在三个维度上均有增量价值；消融FS系列则将增量归因到具体组件。

- theory_return_cn：讨论部分开篇重述社会影响理论并断言‘现有研究无法解释用户如何在社会影响下用不同语言交流’；随后把三类特征解释为对该理论的操作化；最后在5.2节把理论推广到其他领域，使结果从‘检测抑郁’上升为‘对比语言模式可作为CDSS通用机制’。

- contribution_positioning_cn：作者从三个位置强化贡献：引言预告（解决准确性与可解释性矛盾）、表1文献矩阵定位新颖性（第一个同时考虑影响力、网络结构和对比分析）、讨论5.1总结并承诺临床可操作性。贡献类型强调‘功能增强’而非‘理论突破’。

- novelty_protection_cn：为避免结果被视为一次性性能报告，作者通过三招保护：一是强调特征的可解释性和面临床可用性，使性能与临床洞察绑定；二是将方法设计成框架而非单一分类器，可嵌入CDSS多种组件；三是用大量表图和算法细节展示方法可复制、可组合、可扩展；四是在讨论和结论中反复声明框架可推广到其他精神疾病和多类群体场景。

## 可复用研究与写作程序

### structure_steps

#### 1. 1

- step：1

- writing_job_cn：建立现实问题并指出现有系统的数据源和可解释性双重不足

- research_job_cn：收集领域数据（如健康统计、系统局限文献）并明确目标系统类型（如CDSS）

- required_evidence_cn：领域报告或权威文献显示问题规模和现有方法的局限

- transition_to_next_cn：通过‘虽然数据驱动系统可行，但缺少X’转向知识缺口

#### 2. 2

- step：2

- writing_job_cn：引入理论或知识基础，解释为何现有方法忽略的维度重要

- research_job_cn：选择与现象匹配的理论（如社会影响理论），梳理该理论在相关IS/健康研究中的应用

- required_evidence_cn：理论原文和至少几篇在类似场景中应用该理论的文献

- transition_to_next_cn：将理论命题转为‘因此需要提取某类特征’的设计要求

#### 3. 3

- step：3

- writing_job_cn：将理论/知识基础转化为具体的特征或组件设计，描述每个组件的输入输出和算法

- research_job_cn：实现特征提取程序（如n-gram频率、LDA、软余弦、网络公式），并用公式和伪代码表达

- required_evidence_cn：可运行的算法描述或原型；初步示例输出

- transition_to_next_cn：说明组件之间的依赖关系并指向评价

#### 4. 4

- step：4

- writing_job_cn：用真实数据展示每个组件的输出是否可解释、是否符合预期

- research_job_cn：选定真实数据集，进行数据清洗、标签构建，并产出表/图展示中间结果

- required_evidence_cn：表/图/示例数值显示输出具有判别性或差异性

- transition_to_next_cn：从‘看起来有区别’引向‘量化预测价值’

#### 5. 5

- step：5

- writing_job_cn：设计分类实验和基线对比，证明所提出的特征或系统能提升目标任务性能

- research_job_cn：实现至少一个可比较的基线集合和特征消融组合，运行多个评价指标

- required_evidence_cn：分类性能表/图显示在多数组合上优于基线

- transition_to_next_cn：用特征重要性或误差分析解释性能来自哪里

#### 6. 6

- step：6

- writing_job_cn：回到引言缺口，声明贡献和可推广边界，并承认未测部分

- research_job_cn：把结果重新连接到理论/知识缺口，讨论哪些场景可迁移、哪些不能

- required_evidence_cn：讨论中引用前言缺口句子；用限制和未来研究对冲过度主张

- transition_to_next_cn：结论部分以简短总结收束

### most_transferable_moves_cn

1. 多步缺口堆叠：现实问题→系统局限→理论视角→具体缺口→研究目标

2. 用文献对比表（表1）快速定位自己的新颖性坐标

3. 特征设计时先说明现有方法不足，再用公式和算法展示新程序

4. 评价时同时做可解释性探索和预测性能验证，兼顾设计科学与计算实验

5. 特征集消融设计（FS1-FS8）把整体性能分解到组件，增强说服力

6. 讨论部分主动把结果推广到其他领域，保护贡献不过度窄化

### resource_intensive_or_nonstandard_parts_cn

1. 需要包含用户心理量表标签和社交网络结构的真实数据集（如Kosinski数据）

2. 网络级特征依赖可获取的朋友状态和标签，普通研究者难以获得类似MSN数据

3. 需要较长的文本预处理和主题模型调优过程

4. 实验对医疗数据隐私和伦理要求较高，不能随意复制

### what_not_to_copy_superficially_cn

1. 不能只写‘我们提出对比框架’而没有三类特征的具体公式和伪代码

2. 不能只宣称‘可解释’而没有词项聚类图、主题词表和特征重要性结果

3. 不能只给出性能数字而不设置LIWC/GTF/RFE/SBERT等基线

4. 不能把探索性NBC相关模式说成因果影响，需要实验或因果识别设计

5. 不能在没有跨场景数据时声称框架可推广到电商双向评论等无关领域

- single_best_description_of_the_routine_cn：先堆叠现实与文献缺口，再借一个社会/行为理论把缺口理论化，随后把理论翻译成一组可计算的分层特征，用真实数据先展示特征的可解释性，再用分类实验和基线消融证明其预测价值，最后回到理论宣称对目标系统的功能增强和可推广性。

## 分析边界

分析基于提供的全文OCR文本；部分图表（如Fig 4、Fig 7坐标、Table 4格式）在文本提取中不完整，可能影响对某些结果描述的细微理解；没有附录且参考文献中个别条目不完整，可能影响对既有工作对比的完整把握；p值、公式和算法伪代码可能存在OCR转录误差，因此对技术细节的解释应辅以原始PDF验证。
