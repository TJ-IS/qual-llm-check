# sDTM: A Supervised Bayesian Deep Topic Model for Text Analytics：ISR 句段级微观图谱

- 作者：Yi Yang; Kunpeng Zhang; Yangyang Fan
- 年份：2023
- DOI：10.1287/isre.2022.1124
- 源文件：28460_2023_sdtm-a-supervised-bayesian-deep-topic-model-for-text-analytics.md
- 置信度：0.87

## 核实后的宏观骨架

文章属于设计科学型方法论文。全文线性结构为：以主题建模在IS研究中的广泛使用和两阶段分析范式为背景，指出其核心缺口是忽略文本伴随的辅助标签；文献综述分三段分别说明IS中的应用、已有监督主题模型的强分布假设限制、以及IS方法数据科学对测量误差和可解释性的关注；随后提出sDTM，用VAE式神经主题模型与双向GRU通过新的主题注意力层桥接，并用含标签似然的ELBO联合优化；评价分三个递进层次：模型拟合（困惑度与主题情感性）、实证价值（两个IS数据集上的回归与统计功效）、预测价值（端到端分类并与两阶段和深度基线比较）；讨论把贡献包装为可替换LDA的插件式方法，并给出会计金融等长文本的扩展设想和限制。

## 摘要逐句图谱

### 1. Abstract P1 S1

- order：1

- locator：Abstract P1 S1

- paraphrase_cn：主题建模方法如LDA是分析海量文本数据的有力工具。

- move_code：CONTEXT

- statement_status：prior_literature

- why_here_cn：开篇给出研究对象和方法在学术界的地位。

- inherits_from_previous_cn：无

- changes_argument_state_cn：确立主题建模是值得研究的方法领域。

- sets_up_next_cn：为指出被广泛使用却存在局限做铺垫。

- failure_if_removed_cn：缺少方法背景，后文的缺口批评失去对象。

- evidence_pointer：Abstract首句

### 2. Abstract P1 S2

- order：2

- locator：Abstract P1 S2

- paraphrase_cn：该方法在IS和商业研究中被广泛用于主题探索和派生新变量。

- move_code：CONTEXT

- statement_status：prior_literature

- why_here_cn：把主题建模定位为实证分析和特征工程流程的工具。

- inherits_from_previous_cn：承接LDA作为工具的地位。

- changes_argument_state_cn：说明主题向量会影响后续实证与预测。

- sets_up_next_cn：为批评无监督方法忽视元数据做铺垫。

- failure_if_removed_cn：读者无法理解为什么主题向量准确性重要。

- evidence_pointer：Abstract第二句

### 3. Abstract P1 S3

- order：3

- locator：Abstract P1 S3

- paraphrase_cn：现有主题建模大多无监督，只利用文本，忽略评论星级或论坛帖子类别等元数据。

- move_code：LIMITATION

- statement_status：author_inference

- why_here_cn：引入全文核心问题：辅助信息被忽略。

- inherits_from_previous_cn：继承工具地位并指出其使用方式有缺陷。

- changes_argument_state_cn：把对象从一般方法收窄到无监督假设。

- sets_up_next_cn：需要说明这种忽略会带来什么后果。

- failure_if_removed_cn：研究动机缺失，问题不成立。

- evidence_pointer：Abstract第三句

### 4. Abstract P1 S4

- order：4

- locator：Abstract P1 S4

- paraphrase_cn：由此识别的主题和派生变量可能不准确，导致实证估计错误和预测性能下降。

- move_code：CONSEQUENCE

- statement_status：author_inference

- why_here_cn：把方法缺陷转化为IS读者关心的实证和预测后果。

- inherits_from_previous_cn：承接无监督方法忽略标签的前提。

- changes_argument_state_cn：设定本文要解决的问题：不准确的主题造成下游损失。

- sets_up_next_cn：需要提出能利用标签的新模型。

- failure_if_removed_cn：研究价值不明确。

- evidence_pointer：Abstract第四句

### 5. Abstract P2 S1

- order：5

- locator：Abstract P2 S1

- paraphrase_cn：本文提出监督式深度主题模型sDTM，结合神经变分自编码器与循环神经网络。

- move_code：RQ_OR_OBJECTIVE

- statement_status：theory_claim

- why_here_cn：正式给出研究目标和制品名称。

- inherits_from_previous_cn：针对前文的后果提出解决方案。

- changes_argument_state_cn：从问题转入方案。

- sets_up_next_cn：需要解释sDTM如何利用辅助数据。

- failure_if_removed_cn：摘要缺少核心创新点。

- evidence_pointer：Abstract第二段首句

### 6. Abstract P2 S2

- order：6

- locator：Abstract P2 S2

- paraphrase_cn：sDTM利用文本伴随的辅助数据增强主题建模能力。

- move_code：MECHANISM

- statement_status：design_decision

- why_here_cn：明确创新机制：辅助数据进入主题推断。

- inherits_from_previous_cn：承接模型组件。

- changes_argument_state_cn：说明新模型与旧模型的关键差异。

- sets_up_next_cn：预告需要用数据验证。

- failure_if_removed_cn：创新点没有被表述。

- evidence_pointer：Abstract第二段第二句

### 7. Abstract P2 S3

- order：7

- locator：Abstract P2 S3

- paraphrase_cn：在一个在线消费者评论数据集和一个在线知识社区数据集上开展实证案例研究和预测分析。

- move_code：STUDY_OVERVIEW

- statement_status：method_decision

- why_here_cn：给出评价路径和IS相关数据场景。

- inherits_from_previous_cn：依赖模型已提出的前提。

- changes_argument_state_cn：把讨论引向实证评估。

- sets_up_next_cn：结果需要被概括。

- failure_if_removed_cn：缺少评估范围。

- evidence_pointer：Abstract第二段第三句

### 8. Abstract P2 S4

- order：8

- locator：Abstract P2 S4

- paraphrase_cn：实验结果表明，与基准方法相比，sDTM能同时提升实证估计和预测性能。

- move_code：RESULT

- statement_status：empirical_result

- why_here_cn：给出全局结果。

- inherits_from_previous_cn：承接两个数据集的评价。

- changes_argument_state_cn：从方案回到证据，证明方案有效。

- sets_up_next_cn：需要提炼贡献。

- failure_if_removed_cn：摘要没有结果支撑。

- evidence_pointer：Abstract第二段第四句

### 9. Abstract P2 S5

- order：9

- locator：Abstract P2 S5

- paraphrase_cn：sDTM对IS文献做出方法论贡献，并与使用文本分析的研究直接相关。

- move_code：CONTRIBUTION

- statement_status：contribution_claim

- why_here_cn：把结果升格为领域贡献。

- inherits_from_previous_cn：承接实证和预测改进结果。

- changes_argument_state_cn：将技术结果转成IS方法论价值。

- sets_up_next_cn：正文需要详细证明这一贡献。

- failure_if_removed_cn：贡献声明缺失，论文定位不清。

- evidence_pointer：Abstract末句

## 引言逐句图谱

### 1. Introduction P1 S1

- order：1

- locator：Introduction P1 S1

- paraphrase_cn：经济与社会交易的数字化和用户生成内容增长产生了海量非结构化文本，如评论和问答。

- move_code：CONTEXT

- statement_status：fact

- why_here_cn：建立宏观背景和问题域。

- inherits_from_previous_cn：无

- changes_argument_state_cn：进入文本分析领域。

- sets_up_next_cn：为引出计算方法需求做铺垫。

- failure_if_removed_cn：研究背景缺失。

- evidence_pointer：Introduction P1 S1

### 2. Introduction P1 S2

- order：2

- locator：Introduction P1 S2

- paraphrase_cn：探索和分析高容量文本为研究和实践提供前所未有的机会。

- move_code：CONTEXT

- statement_status：fact

- why_here_cn：说明文本分析的重要性。

- inherits_from_previous_cn：承接文本数据爆炸。

- changes_argument_state_cn：强调需求。

- sets_up_next_cn：需要有效计算方法。

- failure_if_removed_cn：读者不知道为何值得投入。

- evidence_pointer：Introduction P1 S2

### 3. Introduction P1 S3

- order：3

- locator：Introduction P1 S3

- paraphrase_cn：但这种探索需要有效计算方法，以借助大数据分析的力量。

- move_code：CONTEXT

- statement_status：fact

- why_here_cn：把背景转化为方法需求。

- inherits_from_previous_cn：承接机会。

- changes_argument_state_cn：从数据转向计算工具。

- sets_up_next_cn：引出主题建模。

- failure_if_removed_cn：方法的重要性没有建立。

- evidence_pointer：Introduction P1 S3

### 4. Introduction P1 S4

- order：4

- locator：Introduction P1 S4

- paraphrase_cn：主题建模已成为IS和商业研究者从文本中探索和提取洞察的主流工具。

- move_code：PRIOR_KNOWLEDGE

- statement_status：prior_literature

- why_here_cn：给出研究对象的具体工具。

- inherits_from_previous_cn：承接计算需求。

- changes_argument_state_cn：把主题建模置于中心。

- sets_up_next_cn：进一步介绍最常用的LDA。

- failure_if_removed_cn：论文主题不清晰。

- evidence_pointer：Introduction P1 S4

### 5. Introduction P1 S5

- order：5

- locator：Introduction P1 S5

- paraphrase_cn：最常用的LDA能自动发现潜在主题并提供概率解释。

- move_code：PRIOR_KNOWLEDGE

- statement_status：prior_literature

- why_here_cn：明确LDA的技术特征。

- inherits_from_previous_cn：承接主题建模主流地位。

- changes_argument_state_cn：为批评LDA的无监督性确定对象。

- sets_up_next_cn：转向LDA的两阶段应用。

- failure_if_removed_cn：后文说不清批评的对象。

- evidence_pointer：Introduction P1 S5

### 6. Introduction P2 S1

- order：6

- locator：Introduction P2 S1

- paraphrase_cn：主题建模的一个常见应用是理论生成，常与质性方法和实证方法结合。

- move_code：PRIOR_KNOWLEDGE

- statement_status：prior_literature

- why_here_cn：说明主题建模在IS研究中的主要角色。

- inherits_from_previous_cn：承接LDA作为工具。

- changes_argument_state_cn：把问题聚焦到研究流程。

- sets_up_next_cn：介绍两阶段框架。

- failure_if_removed_cn：IS相关性不够强。

- evidence_pointer：Introduction P2 S1

### 7. Introduction P2 S2

- order：7

- locator：Introduction P2 S2

- paraphrase_cn：研究者常先用LDA提取主题和文档主题分布，再将这些变量纳入计量模型。

- move_code：PRIOR_KNOWLEDGE

- statement_status：prior_literature

- why_here_cn：定义两阶段分析范式。

- inherits_from_previous_cn：承接理论生成应用。

- changes_argument_state_cn：确立批评的具体对象。

- sets_up_next_cn：给出实例。

- failure_if_removed_cn：后文的测量误差问题没有载体。

- evidence_pointer：Introduction P2 S2

### 8. Introduction P2 S3

- order：8

- locator：Introduction P2 S3

- paraphrase_cn：例如Khern-am-nuai等用LDA衡量平台提供金钱激励前后评论主题概率差异，再做回归。

- move_code：EXAMPLE

- statement_status：prior_literature

- why_here_cn：用已发表案例说明两阶段流程的具体形态。

- inherits_from_previous_cn：承接两阶段描述。

- changes_argument_state_cn：使范式具体可感。

- sets_up_next_cn：继续举预测场景。

- failure_if_removed_cn：两阶段范式还停留在抽象层面。

- evidence_pointer：Introduction P2 S3

### 9. Introduction P2 S4

- order：9

- locator：Introduction P2 S4

- paraphrase_cn：LDA也是预测分析中常见的两阶段启发式：先估计主题向量，再交给监督预测模型。

- move_code：PRIOR_KNOWLEDGE

- statement_status：prior_literature

- why_here_cn：把问题扩展到预测场景。

- inherits_from_previous_cn：承接两阶段思想。

- changes_argument_state_cn：说明该范式不限于实证。

- sets_up_next_cn：强调主题向量准确性。

- failure_if_removed_cn：预测部分缺少前置。

- evidence_pointer：Introduction P2 S4

### 10. Introduction P2 S5

- order：10

- locator：Introduction P2 S5

- paraphrase_cn：在这些应用中主题向量必须准确，否则会产生测量误差、错误估计和差预测。

- move_code：WHY_GAP_MATTERS

- statement_status：author_inference

- why_here_cn：给出方法缺陷导致的后果。

- inherits_from_previous_cn：承接两种两阶段场景。

- changes_argument_state_cn：把工具问题变成影响研究质量的问题。

- sets_up_next_cn：解释为什么会不准确。

- failure_if_removed_cn：研究动机断裂。

- evidence_pointer：Introduction P2 S5

### 11. Introduction P3 S1

- order：11

- locator：Introduction P3 S1

- paraphrase_cn：传统统计主题模型如LDA是无监督的，只用文本训练。

- move_code：LIMITATION

- statement_status：fact

- why_here_cn：指出核心局限的性质。

- inherits_from_previous_cn：承接准确性要求。

- changes_argument_state_cn：定位问题根源。

- sets_up_next_cn：引入辅助元数据。

- failure_if_removed_cn：问题根源没有被指出。

- evidence_pointer：Introduction P3 S1

### 12. Introduction P3 S2

- order：12

- locator：Introduction P3 S2

- paraphrase_cn：但许多真实平台上的文本常伴随有用元数据，如评分、板块、新闻类别。

- move_code：PHENOMENON

- statement_status：fact

- why_here_cn：说明辅助信息普遍存在。

- inherits_from_previous_cn：承接无监督训练方式。

- changes_argument_state_cn：建立“应该利用而没有利用”的落差。

- sets_up_next_cn：说明为什么现有贝叶斯方法难以纳入。

- failure_if_removed_cn：标签的重要性无从谈起。

- evidence_pointer：Introduction P3 S2

### 13. Introduction P3 S3

- order：13

- locator：Introduction P3 S3

- paraphrase_cn：例如Yelp和Amazon有评分，知识社区有讨论板块，新闻有类别标签。

- move_code：EXAMPLE

- statement_status：fact

- why_here_cn：用IS读者熟悉的平台具体化元数据。

- inherits_from_previous_cn：承接元数据的普遍性。

- changes_argument_state_cn：证明该问题与IS数据高度相关。

- sets_up_next_cn：强化采纳标签的必要性。

- failure_if_removed_cn：元数据概念偏抽象。

- evidence_pointer：Introduction P3 S3

### 14. Introduction P3 S4

- order：14

- locator：Introduction P3 S4

- paraphrase_cn：尽管元数据可能是有用的监督信号，但无监督主题模型忽略了它们。

- move_code：LIMITATION

- statement_status：author_inference

- why_here_cn：明确无监督模型的忽略行为。

- inherits_from_previous_cn：承接元数据实例。

- changes_argument_state_cn：把事实转为批评。

- sets_up_next_cn：指出纳入的困难。

- failure_if_removed_cn：批评力度不足。

- evidence_pointer：Introduction P3 S4

### 15. Introduction P3 S5

- order：15

- locator：Introduction P3 S5

- paraphrase_cn：在贝叶斯主题建模中纳入辅助元数据很困难，因为需要显式定义辅助数据的生成过程。

- move_code：LIMITATION

- statement_status：prior_literature

- why_here_cn：说明已有方法为何难以解决。

- inherits_from_previous_cn：承接标签被忽略的批评。

- changes_argument_state_cn：指出贝叶斯建模的痛点。

- sets_up_next_cn：为深度学习方法留出空间。

- failure_if_removed_cn：无法解释为何需要新方法。

- evidence_pointer：Introduction P3 S5

### 16. Introduction P3 S6

- order：16

- locator：Introduction P3 S6

- paraphrase_cn：这会限制模型在复杂文本语义上的泛化，可能导致拟合差。

- move_code：CONSEQUENCE

- statement_status：author_inference

- why_here_cn：把技术困难转成性能后果。

- inherits_from_previous_cn：承接生成过程建模难题。

- changes_argument_state_cn：说明缺口需要被弥补。

- sets_up_next_cn：引出sDTM。

- failure_if_removed_cn：破而不立。

- evidence_pointer：Introduction P3 S6

### 17. Introduction P4 S1

- order：17

- locator：Introduction P4 S1

- paraphrase_cn：为克服这些挑战，本文提出基于深度学习的神经主题建模方法，利用评分或类别等辅助元数据。

- move_code：RQ_OR_OBJECTIVE

- statement_status：theory_claim

- why_here_cn：提出解决方案。

- inherits_from_previous_cn：承接贝叶斯纳入困难。

- changes_argument_state_cn：从问题转入方案。

- sets_up_next_cn：介绍模型组件。

- failure_if_removed_cn：文章没有核心提案。

- evidence_pointer：Introduction P4 S1

### 18. Introduction P4 S2

- order：18

- locator：Introduction P4 S2

- paraphrase_cn：sDTM把无监督神经主题建模与监督RNN结合在单一框架，用新颖的主题注意力层。

- move_code：MECHANISM

- statement_status：design_decision

- why_here_cn：具体说明模型架构。

- inherits_from_previous_cn：承接深度学习方案。

- changes_argument_state_cn：确定制品的核心技术选择。

- sets_up_next_cn：解释注意力层的作用。

- failure_if_removed_cn：技术贡献不明确。

- evidence_pointer：Introduction P4 S2

### 19. Introduction P4 S3

- order：19

- locator：Introduction P4 S3

- paraphrase_cn：sDTM用NTM学到的主题向量引导RNN把重要词与主题和标签关联起来。

- move_code：MECHANISM

- statement_status：design_decision

- why_here_cn：说明前向信息流。

- inherits_from_previous_cn：承接主题注意力层。

- changes_argument_state_cn：主题信息进入序列表示。

- sets_up_next_cn：用例子解释。

- failure_if_removed_cn：模型机制不清楚。

- evidence_pointer：Introduction P4 S3

### 20. Introduction P4 S4

- order：20

- locator：Introduction P4 S4

- paraphrase_cn：例如若NTM推断评论与价格和质量相关，则这些主题被用来给相关词更高权重，改善文档表示。

- move_code：EXAMPLE

- statement_status：author_inference

- why_here_cn：用直觉例子降低理解门槛。

- inherits_from_previous_cn：承接主题引导注意力机制。

- changes_argument_state_cn：机制变得可感。

- sets_up_next_cn：转向反向信息流。

- failure_if_removed_cn：读者难以理解设计价值。

- evidence_pointer：Introduction P4 S4

### 21. Introduction P4 S5

- order：21

- locator：Introduction P4 S5

- paraphrase_cn：同时，辅助标签可经RNN传播回NTM，向主题建模注入监督信号。

- move_code：MECHANISM

- statement_status：design_decision

- why_here_cn：说明后向信息流。

- inherits_from_previous_cn：承接前向机制。

- changes_argument_state_cn：形成双向信息流动。

- sets_up_next_cn：举标签实例。

- failure_if_removed_cn：监督性没有体现。

- evidence_pointer：Introduction P4 S5

### 22. Introduction P4 S6

- order：22

- locator：Introduction P4 S6

- paraphrase_cn：例如评分标签能帮助sDTM学到更具情感、价值导向的主题。

- move_code：EXAMPLE

- statement_status：author_inference

- why_here_cn：把监督信号与实际结果联系起来。

- inherits_from_previous_cn：承接反向传播。

- changes_argument_state_cn：说明标签对主题质量的贡献。

- sets_up_next_cn：总结合并优势。

- failure_if_removed_cn：标签价值不直观。

- evidence_pointer：Introduction P4 S6

### 23. Introduction P4 S7

- order：23

- locator：Introduction P4 S7

- paraphrase_cn：总之，sDTM结合监督深度学习和无监督主题建模的优点，有利于后续实证和预测。

- move_code：SUMMARY

- statement_status：theory_claim

- why_here_cn：总结模型的总体主张。

- inherits_from_previous_cn：承接双向机制的两个例子。

- changes_argument_state_cn：把组件级机制升格为整体价值。

- sets_up_next_cn：预告评估。

- failure_if_removed_cn：模型价值没有总括。

- evidence_pointer：Introduction P4 S7

### 24. Introduction P5 S1

- order：24

- locator：Introduction P5 S1

- paraphrase_cn：我们在Yelp消费者评论和Stack Exchange知识社区两个数据集上展示方法实用性。

- move_code：STUDY_OVERVIEW

- statement_status：method_decision

- why_here_cn：给出评价数据。

- inherits_from_previous_cn：承接模型总价值。

- changes_argument_state_cn：从方案转向证据。

- sets_up_next_cn：说明从三个角度展示。

- failure_if_removed_cn：评价范围缺失。

- evidence_pointer：Introduction P5 S1

### 25. Introduction P5 S2

- order：25

- locator：Introduction P5 S2

- paraphrase_cn：实用性从三个角度展示。

- move_code：STUDY_OVERVIEW

- statement_status：method_decision

- why_here_cn：给出评估结构。

- inherits_from_previous_cn：承接两个数据集。

- changes_argument_state_cn：为全文结构导航。

- sets_up_next_cn：逐一展开三点。

- failure_if_removed_cn：论文结构不清晰。

- evidence_pointer：Introduction P5 S2

### 26. Introduction P5 S3

- order：26

- locator：Introduction P5 S3

- paraphrase_cn：第一，作为概率主题模型，评估sDTM在留出数据上的模型拟合。

- move_code：STUDY_OVERVIEW

- statement_status：method_decision

- why_here_cn：给出第一评价维度。

- inherits_from_previous_cn：承接三角度声明。

- changes_argument_state_cn：确立离线拟合评估。

- sets_up_next_cn：给出具体结果预告。

- failure_if_removed_cn：第一维度缺失。

- evidence_pointer：Introduction P5 S3

### 27. Introduction P5 S4

- order：27

- locator：Introduction P5 S4

- paraphrase_cn：实验显示sDTM显著提升文本建模能力，Yelp上主题更连贯、可区分、更具情感导向。

- move_code：RESULT

- statement_status：empirical_result

- why_here_cn：预览模型拟合结果。

- inherits_from_previous_cn：承接模型拟合评估。

- changes_argument_state_cn：给出第一个证据。

- sets_up_next_cn：转入实证价值。

- failure_if_removed_cn：模型拟合结果缺失。

- evidence_pointer：Introduction P5 S4

### 28. Introduction P5 S5

- order：28

- locator：Introduction P5 S5

- paraphrase_cn：第二，进行两个实证案例研究展示sDTM在实证研究中的优势。

- move_code：STUDY_OVERVIEW

- statement_status：method_decision

- why_here_cn：给出第二评价维度。

- inherits_from_previous_cn：承接三角度声明。

- changes_argument_state_cn：从拟合转到实证。

- sets_up_next_cn：介绍两个案例。

- failure_if_removed_cn：实证维度缺失。

- evidence_pointer：Introduction P5 S5

### 29. Introduction P5 S6

- order：29

- locator：Introduction P5 S6

- paraphrase_cn：第一个案例用Yelp研究评论复杂度与评论有用性的关系。

- move_code：STUDY_OVERVIEW

- statement_status：method_decision

- why_here_cn：给出案例1。

- inherits_from_previous_cn：承接实证维度。

- changes_argument_state_cn：明确案例1的IS问题。

- sets_up_next_cn：引出案例2。

- failure_if_removed_cn：案例1缺失。

- evidence_pointer：Introduction P5 S6

### 30. Introduction P5 S7

- order：30

- locator：Introduction P5 S7

- paraphrase_cn：第二个案例用Stack Exchange研究答案与问题的主题相似性与答案有用性的关系。

- move_code：STUDY_OVERVIEW

- statement_status：method_decision

- why_here_cn：给出案例2，形成跨场景验证。

- inherits_from_previous_cn：承接实证维度。

- changes_argument_state_cn：建立外部效度。

- sets_up_next_cn：总结两个案例的共同含义。

- failure_if_removed_cn：外部效度不足。

- evidence_pointer：Introduction P5 S7

### 31. Introduction P5 S8

- order：31

- locator：Introduction P5 S8

- paraphrase_cn：两个案例都说明sDTM能产生更有意义、理论上更合理的实证估计。

- move_code：RESULT

- statement_status：empirical_result

- why_here_cn：把两个案例共同结果提炼。

- inherits_from_previous_cn：承接两个案例。

- changes_argument_state_cn：从案例升至价值主张。

- sets_up_next_cn：解释机制。

- failure_if_removed_cn：实证价值不明确。

- evidence_pointer：Introduction P5 S8

### 32. Introduction P5 S9

- order：32

- locator：Introduction P5 S9

- paraphrase_cn：有了高质量主题模型，研究者可构造更准确的变量，缓解测量误差。

- move_code：MECHANISM

- statement_status：theory_claim

- why_here_cn：解释sDTM为何改善实证。

- inherits_from_previous_cn：承接实证改善结果。

- changes_argument_state_cn：把结果归因于主题向量质量。

- sets_up_next_cn：引出统计功效。

- failure_if_removed_cn：缺少机制解释。

- evidence_pointer：Introduction P5 S9

### 33. Introduction P5 S10

- order：33

- locator：Introduction P5 S10

- paraphrase_cn：此外，使用sDTM能降低不能拒绝零假设的发生率。

- move_code：RESULT

- statement_status：empirical_result

- why_here_cn：给出统计功效这一独特卖点。

- inherits_from_previous_cn：承接测量误差缓解。

- changes_argument_state_cn：把模型优势扩展到统计推断。

- sets_up_next_cn：转向预测。

- failure_if_removed_cn：统计功效贡献缺失。

- evidence_pointer：Introduction P5 S10

### 34. Introduction P5 S11

- order：34

- locator：Introduction P5 S11

- paraphrase_cn：第三，评估sDTM预测留出标签的能力。

- move_code：STUDY_OVERVIEW

- statement_status：method_decision

- why_here_cn：给出第三评价维度。

- inherits_from_previous_cn：承接三角度声明。

- changes_argument_state_cn：引入预测任务。

- sets_up_next_cn：给出预测结果。

- failure_if_removed_cn：预测维度缺失。

- evidence_pointer：Introduction P5 S11

### 35. Introduction P5 S12

- order：35

- locator：Introduction P5 S12

- paraphrase_cn：结果显示sDTM显著提高预测准确率，甚至接近或超过最先进的监督深度学习方法。

- move_code：RESULT

- statement_status：empirical_result

- why_here_cn：预览预测结果。

- inherits_from_previous_cn：承接预测任务。

- changes_argument_state_cn：给出第三个证据。

- sets_up_next_cn：进入贡献声明。

- failure_if_removed_cn：预测价值模糊。

- evidence_pointer：Introduction P5 S12

### 36. Introduction P6 S1

- order：36

- locator：Introduction P6 S1

- paraphrase_cn：本文以三种方式对IS文献做出贡献。

- move_code：CONTRIBUTION

- statement_status：contribution_claim

- why_here_cn：开始贡献声明。

- inherits_from_previous_cn：承接全部结果。

- changes_argument_state_cn：把结果升格为领域贡献。

- sets_up_next_cn：逐一说明。

- failure_if_removed_cn：论文缺少贡献聚焦。

- evidence_pointer：Introduction P6 S1

### 37. Introduction P6 S2

- order：37

- locator：Introduction P6 S2

- paraphrase_cn：第一，描述并提高对文本分析中辅助元数据普遍性的认识。

- move_code：CONTRIBUTION

- statement_status：contribution_claim

- why_here_cn：贡献一：认识层面。

- inherits_from_previous_cn：承接三贡献声明。

- changes_argument_state_cn：给出第一贡献。

- sets_up_next_cn：说明激励后果。

- failure_if_removed_cn：贡献一缺失。

- evidence_pointer：Introduction P6 S2

### 38. Introduction P6 S3

- order：38

- locator：Introduction P6 S3

- paraphrase_cn：把这些元数据纳入主题建模能显著增强潜在语义发现。

- move_code：CONTRIBUTION

- statement_status：contribution_claim

- why_here_cn：把认识转化为方法价值。

- inherits_from_previous_cn：承接贡献一。

- changes_argument_state_cn：说明为何值得关注。

- sets_up_next_cn：引出方法贡献。

- failure_if_removed_cn：贡献一缺价值判断。

- evidence_pointer：Introduction P6 S3

### 39. Introduction P6 S4

- order：39

- locator：Introduction P6 S4

- paraphrase_cn：受此激励，本文引入结合无监督神经主题建模和监督深度学习的监督主题建模方法，填补文献缺口。

- move_code：CONTRIBUTION

- statement_status：contribution_claim

- why_here_cn：给出方法层面的贡献。

- inherits_from_previous_cn：承接激励逻辑。

- changes_argument_state_cn：把认识创新与方法创新绑定。

- sets_up_next_cn：进入贡献二。

- failure_if_removed_cn：方法创新没有被表达。

- evidence_pointer：Introduction P6 S4

### 40. Introduction P6 S5

- order：40

- locator：Introduction P6 S5

- paraphrase_cn：第二，用两个高度IS相关的数据集展示sDTM的实用性。

- move_code：CONTRIBUTION

- statement_status：contribution_claim

- why_here_cn：给出贡献二。

- inherits_from_previous_cn：承接方法贡献。

- changes_argument_state_cn：把方法贡献落实为实证证据。

- sets_up_next_cn：说明展示内容。

- failure_if_removed_cn：实证效用贡献缺失。

- evidence_pointer：Introduction P6 S5

### 41. Introduction P6 S6

- order：41

- locator：Introduction P6 S6

- paraphrase_cn：我们展示sDTM产生高质量主题模型，强化后续实证和预测分析。

- move_code：CONTRIBUTION

- statement_status：contribution_claim

- why_here_cn：概括实证贡献内容。

- inherits_from_previous_cn：承接贡献二。

- changes_argument_state_cn：具体化展示结果。

- sets_up_next_cn：给出直接相关性结论。

- failure_if_removed_cn：贡献二内容空泛。

- evidence_pointer：Introduction P6 S6

### 42. Introduction P6 S7

- order：42

- locator：Introduction P6 S7

- paraphrase_cn：因此本文对IS和商业领域的研究者与实践者具有直接相关性和实用性。

- move_code：CONTRIBUTION

- statement_status：contribution_claim

- why_here_cn：给出贡献二的价值收尾。

- inherits_from_previous_cn：承接实证展示。

- changes_argument_state_cn：把证据转化为用户价值。

- sets_up_next_cn：进入贡献三。

- failure_if_removed_cn：贡献二缺应用对象。

- evidence_pointer：Introduction P6 S7

### 43. Introduction P6 S8

- order：43

- locator：Introduction P6 S8

- paraphrase_cn：第三，sDTM可直接替换LDA，无需研究者重构分析框架。

- move_code：CONTRIBUTION

- statement_status：contribution_claim

- why_here_cn：给出贡献三：低采用门槛。

- inherits_from_previous_cn：承接前两个贡献。

- changes_argument_state_cn：强调即插即用属性。

- sets_up_next_cn：提出开源。

- failure_if_removed_cn：可复用贡献缺失。

- evidence_pointer：Introduction P6 S8

### 44. Introduction P6 S9

- order：44

- locator：Introduction P6 S9

- paraphrase_cn：我们开源Python实现以最大化研究和实践影响。

- move_code：CONTRIBUTION

- statement_status：contribution_claim

- why_here_cn：用开源增强可复现性和采用可能性。

- inherits_from_previous_cn：承接即插即用。

- changes_argument_state_cn：把贡献落地为可用资源。

- sets_up_next_cn：正文进入文献综述。

- failure_if_removed_cn：可复制性主张缺支持。

- evidence_pointer：Introduction P6 S9

## 引言逐段图谱

### 1. Introduction P1

- locator：Introduction P1

- opening_move_cn：以数字化与用户生成内容爆炸开场。

- development_move_cn：逐步收窄到计算方法需求，再定位到主题建模与LDA。

- pivot_move_cn：从宏观数据机会转向具体技术工具。

- closing_move_cn：以LDA的自动发现能力收束，为下一段的两阶段应用提供对象。

- paragraph_job_cn：建立文章主题：主题建模是IS文本分析的支配性工具。

### 2. Introduction P2

- locator：Introduction P2

- opening_move_cn：从理论生成这一常见应用开始。

- development_move_cn：叙述两阶段流程，并用实证与预测两个例子说明。

- pivot_move_cn：从描述范式转向指出主题向量准确性的关键性。

- closing_move_cn：以测量误差和差预测的后果收束。

- paragraph_job_cn：把主题建模的普遍性转化为对主题向量质量的依赖。

### 3. Introduction P3

- locator：Introduction P3

- opening_move_cn：指出LDA是无监督模型。

- development_move_cn：展开元数据普遍性，并用平台实例具体化。

- pivot_move_cn：从“元数据存在”转到“现有贝叶斯方法难以纳入”。

- closing_move_cn：以泛化限制和低拟合结果收束。

- paragraph_job_cn：定义核心缺口：辅助标签存在但无法被传统方法利用。

### 4. Introduction P4

- locator：Introduction P4

- opening_move_cn：提出基于深度学习的新方法。

- development_move_cn：解释sDTM架构、主题注意力层和双向信息流，并用两个例子具体化。

- pivot_move_cn：从方案机制转向整体优势总结。

- closing_move_cn：以“结合两者优点”收束。

- paragraph_job_cn：给出解决缺口的技术方案。

### 5. Introduction P5

- locator：Introduction P5

- opening_move_cn：宣布在两个IS数据集上展示实用性。

- development_move_cn：按三个视角展开：模型拟合、实证案例、预测。

- pivot_move_cn：从每个视角的结果预览转向其对研究者的意义。

- closing_move_cn：以预测接近最先进方法收束。

- paragraph_job_cn：为全文的评估结构导航，并预告结果。

### 6. Introduction P6

- locator：Introduction P6

- opening_move_cn：宣布三种贡献。

- development_move_cn：依次展开认识贡献、实证贡献和即插即用贡献。

- pivot_move_cn：从研究贡献转向实践可复用性。

- closing_move_cn：以开源实现收束。

- paragraph_job_cn：把技术方案升格为对IS文献的贡献。

## 理论到设计逐句图谱

### 1. Section 2.1 P1 S1

- order：1

- locator：Section 2.1 P1 S1

- paraphrase_cn：主题建模在管理研究各领域广泛用于识别文本潜在主题。

- move_code：PRIOR_KNOWLEDGE

- statement_status：prior_literature

- why_here_cn：文献综述开头建立LDA的支配地位。

- inherits_from_previous_cn：承接引言中的LDA主流地位。

- changes_argument_state_cn：把引言论断落实为文献证据。

- sets_up_next_cn：列出应用实例。

- failure_if_removed_cn：文献基础不牢。

- evidence_pointer：Section 2.1 P1

### 2. Section 2.1 P1 S2-S4

- order：2

- locator：Section 2.1 P1 S2-S4

- paraphrase_cn：IS学者大量用LDA分析评论、回复、酒店体验、产品缺陷等，如Tirunillai/Tellis、Lappas等、Mankad等。

- move_code：PRIOR_KNOWLEDGE

- statement_status：prior_literature

- why_here_cn：用实例证明LDA在IS实证研究中的普遍性。

- inherits_from_previous_cn：承接主题建模主流地位。

- changes_argument_state_cn：说明大量研究依赖LDA派生变量。

- sets_up_next_cn：继续补充其他文本类型。

- failure_if_removed_cn：IS相关性证据不足。

- evidence_pointer：Section 2.1 P1

### 3. Section 2.1 P2

- order：3

- locator：Section 2.1 P2

- paraphrase_cn：LDA还被用于搜索查询、App信息、综述、专利、创意、推文、公司描述、博客、公司报告和分析师报告等。

- move_code：PRIOR_KNOWLEDGE

- statement_status：prior_literature

- why_here_cn：进一步扩大LDA应用范围。

- inherits_from_previous_cn：承接评论领域实例。

- changes_argument_state_cn：说明LDA是跨IS子领域的通用工具。

- sets_up_next_cn：为指出所有应用都忽略标签做铺垫。

- failure_if_removed_cn：普遍性证据不够。

- evidence_pointer：Section 2.1 P2

### 4. Section 2.1 P3

- order：4

- locator：Section 2.1 P3

- paraphrase_cn：现有研究直接应用LDA，忽略文本伴随的标签、类别或评分等辅助信息；本文是最早强调并纳入这些信息的研究之一。

- move_code：GAP

- statement_status：author_inference

- why_here_cn：在文献综述末尾明确研究缺口。

- inherits_from_previous_cn：承接LDA应用清单。

- changes_argument_state_cn：把文献综述收束为本文的机会。

- sets_up_next_cn：转向监督主题模型综述。

- failure_if_removed_cn：文献综述缺少缺口。

- evidence_pointer：Section 2.1末段

### 5. Section 2.2 P1 S1-S2

- order：5

- locator：Section 2.2 P1 S1-S2

- paraphrase_cn：LDA无监督，不利用文档辅助信息；元数据可作为监督信号，因此出现了sLDA等贝叶斯监督模型，用线性或softmax建模标签。

- move_code：PRIOR_KNOWLEDGE

- statement_status：prior_literature

- why_here_cn：介绍已有监督主题模型。

- inherits_from_previous_cn：承接辅助标签的价值。

- changes_argument_state_cn：说明前人也想用标签，但有假设限制。

- sets_up_next_cn：列出变种。

- failure_if_removed_cn：已有工作脉络缺失。

- evidence_pointer：Section 2.2 P1

### 6. Section 2.2 P1 S3-S4

- order：6

- locator：Section 2.2 P1 S3-S4

- paraphrase_cn：sLDA有许多变种，如DiscLDA、MedLDA、BP-sLDA、谱LDA，另有基于矩阵分解或神经网络的非贝叶斯监督主题模型。

- move_code：PRIOR_KNOWLEDGE

- statement_status：prior_literature

- why_here_cn：展示监督主题建模的已有谱系。

- inherits_from_previous_cn：承接sLDA基础。

- changes_argument_state_cn：说明本文需要与多个基线比较。

- sets_up_next_cn：批评其共同缺陷。

- failure_if_removed_cn：基线选择失去依据。

- evidence_pointer：Section 2.2 P1

### 7. Section 2.2 P2

- order：7

- locator：Section 2.2 P2

- paraphrase_cn：这些监督模型对潜变量分布做强假设，限制泛化，易导致低拟合和次优预测。

- move_code：LIMITATION

- statement_status：author_inference

- why_here_cn：指出已有监督主题模型的共同缺陷。

- inherits_from_previous_cn：承接监督模型谱系。

- changes_argument_state_cn：为深度学习方案制造空间。

- sets_up_next_cn：介绍深度主题模型。

- failure_if_removed_cn：不知道为何需要新方法。

- evidence_pointer：Section 2.2 P2

### 8. Section 2.2 P3 S1-S2

- order：8

- locator：Section 2.2 P3 S1-S2

- paraphrase_cn：深度学习进展催生了TopicRNN和Chai-Li等结合神经网络与主题模型的尝试。

- move_code：PRIOR_KNOWLEDGE

- statement_status：prior_literature

- why_here_cn：介绍最接近本文的深度主题模型。

- inherits_from_previous_cn：承接深度学习方法需求。

- changes_argument_state_cn：说明深度主题建模已有基础。

- sets_up_next_cn：指出其仍无监督。

- failure_if_removed_cn：深度主题建模脉络缺失。

- evidence_pointer：Section 2.2 P3

### 9. Section 2.2 P3 S3-S4

- order：9

- locator：Section 2.2 P3 S3-S4

- paraphrase_cn：但这两个工作本质无监督，深度学习组件只建模词序，标签不参与反向传播，不影响主题推断。

- move_code：LIMITATION

- statement_status：author_inference

- why_here_cn：指出最接近工作的仍未解决监督问题。

- inherits_from_previous_cn：承接深度主题模型。

- changes_argument_state_cn：定位出真正的技术缺口。

- sets_up_next_cn：提出本文填补。

- failure_if_removed_cn：创新点没有对照。

- evidence_pointer：Section 2.2 P3

### 10. Section 2.2 P3 S5

- order：10

- locator：Section 2.2 P3 S5

- paraphrase_cn：尚不清楚如何把监督深度学习和无监督主题建模联合学习；本文通过注意力层桥接VAE式NTM和序列网络。

- move_code：THEORY_PROPOSITION

- statement_status：theory_claim

- why_here_cn：正式提出研究问题和解决方案。

- inherits_from_previous_cn：承接技术缺口。

- changes_argument_state_cn：从缺口转向设计方向。

- sets_up_next_cn：为设计部分铺垫。

- failure_if_removed_cn：本文定位不明。

- evidence_pointer：Section 2.2 P3末

### 11. Section 2.2 P4

- order：11

- locator：Section 2.2 P4

- paraphrase_cn：Table 1显示LDA类监督模型预定义潜变量分布且标签是主题的线性关系，本文则用深度学习的主题注意力层建模标签。

- move_code：THEORY_PROPOSITION

- statement_status：author_inference

- why_here_cn：用表格对比固化已有模型与本文差异。

- inherits_from_previous_cn：承接全部综述。

- changes_argument_state_cn：把文字缺口变成可比较的表格。

- sets_up_next_cn：进入IS方法数据科学综述。

- failure_if_removed_cn：差异对比不够系统。

- evidence_pointer：Section 2.2 Table 1

### 12. Section 2.3 P1

- order：12

- locator：Section 2.3 P1

- paraphrase_cn：IS方法数据科学研究强调大样本p值问题、ML生成变量测量误差、预测模型可解释性；本文受其启发，旨在提升主题建模工具的实用与预测效用。

- move_code：PRIOR_KNOWLEDGE

- statement_status：prior_literature

- why_here_cn：把本文放入IS方法数据科学脉络。

- inherits_from_previous_cn：承接文献综述三分类。

- changes_argument_state_cn：说明本文不只是一个CS算法论文。

- sets_up_next_cn：进入方法设计。

- failure_if_removed_cn：IS定位削弱。

- evidence_pointer：Section 2.3

### 13. Section 3.1 P1 S1-S3

- order：13

- locator：Section 3.1 P1 S1-S3

- paraphrase_cn：以手机评论为例，正负情感词会与电池词共现，无监督LDA会学到正负混合的电池主题；评分可分离出干净的正负电池主题。

- move_code：THEORY_PROPOSITION

- statement_status：author_inference

- why_here_cn：在方法开始前用直觉例子证明标签价值。

- inherits_from_previous_cn：承接辅助标签重要性。

- changes_argument_state_cn：把监督信号的价值具体化为可想象的主题分离。

- sets_up_next_cn：扩展到知识社区类别。

- failure_if_removed_cn：设计动机没有直观基础。

- evidence_pointer：Section 3.1 P1

### 14. Section 3.1 P1 S4

- order：14

- locator：Section 3.1 P1 S4

- paraphrase_cn：在线知识社区中帖子分属不同板块，类别标签可提供主题指导并增强主题建模。

- move_code：THEORY_PROPOSITION

- statement_status：author_inference

- why_here_cn：把标签价值从评论扩展到知识社区。

- inherits_from_previous_cn：承接评论例子。

- changes_argument_state_cn：说明标签价值是领域一般的。

- sets_up_next_cn：给出常见数据源表。

- failure_if_removed_cn：第二个数据集的设计动机缺失。

- evidence_pointer：Section 3.1 P1

### 15. Section 3.1 P2

- order：15

- locator：Section 3.1 P2

- paraphrase_cn：Figure 1对比当前研究的两阶段P1/P2与本文sDTM的P3/P4：传统两阶段中标签只用于第二阶段，sDTM使标签直接影响主题推断。

- move_code：THEORY_PROPOSITION

- statement_status：author_inference

- why_here_cn：用图示区分本文与现有范式的本质差异。

- inherits_from_previous_cn：承接设计动机。

- changes_argument_state_cn：把“标签价值”转化为“架构路径差异”。

- sets_up_next_cn：随后进入NTM背景。

- failure_if_removed_cn：设计创新缺乏范式对照。

- evidence_pointer：Section 3.1 Figure 1

### 16. Section 3.2 P1

- order：16

- locator：Section 3.2 P1

- paraphrase_cn：贝叶斯主题建模如LDA假设文档由潜在主题混合生成；深度主题模型因表达力强能生成更准确的文档模型。

- move_code：PRIOR_KNOWLEDGE

- statement_status：prior_literature

- why_here_cn：提供主题建模与NTM的背景。

- inherits_from_previous_cn：承接设计框架。

- changes_argument_state_cn：确定本文的基础组件NTM。

- sets_up_next_cn：描述NTM的VAE机制。

- failure_if_removed_cn：方法细节缺少基础。

- evidence_pointer：Section 3.2 P1

### 17. Section 3.2 P2-P4

- order：17

- locator：Section 3.2 P2-P4

- paraphrase_cn：NTM用VAE近似后验，编码器把文档映射为高斯参数，解码器用β重建词，目标为ELBO。

- move_code：PRIOR_KNOWLEDGE

- statement_status：prior_literature

- why_here_cn：解释NTM的内部结构，为后续修改β和ELBO做准备。

- inherits_from_previous_cn：承接深度主题模型背景。

- changes_argument_state_cn：提供设计可操作的语言。

- sets_up_next_cn：进入监督式扩展。

- failure_if_removed_cn：后续β分解和ELBO无法理解。

- evidence_pointer：Section 3.2 P2-P4

### 18. Section 3.3 P1

- order：18

- locator：Section 3.3 P1

- paraphrase_cn：NTM无监督，但文档伴随标签时，标签很可能提供有用信息提高主题向量质量，因此需要监督式深度主题模型。

- move_code：THEORY_PROPOSITION

- statement_status：theory_claim

- why_here_cn：把文献缺口转成具体设计需求。

- inherits_from_previous_cn：承接NTM无监督背景。

- changes_argument_state_cn：开启sDTM设计。

- sets_up_next_cn：选择序列编码器。

- failure_if_removed_cn：设计动机断裂。

- evidence_pointer：Section 3.3 P1

### 19. Section 3.3 P2

- order：19

- locator：Section 3.3 P2

- paraphrase_cn：选择双向GRU作为序列编码器，其广泛用于文本分类并能捕获前后上下文。

- move_code：DESIGN_FEATURE

- statement_status：design_decision

- why_here_cn：给出序列网络的具体选择与理由。

- inherits_from_previous_cn：承接结合NTM与深度学习的需求。

- changes_argument_state_cn：确定RNN组件。

- sets_up_next_cn：需要桥接NTM和GRU。

- failure_if_removed_cn：RNN组件没有依据。

- evidence_pointer：Section 3.3 P2

### 20. Section 3.3 P3

- order：20

- locator：Section 3.3 P3

- paraphrase_cn：把NTM与RNN结合是本文的方法贡献：通过主题注意力层桥接两者；反向传播时标签影响主题嵌入，前向时主题嵌入进入文档表示。

- move_code：DESIGN_FEATURE

- statement_status：design_decision

- why_here_cn：给出核心设计创新和双向信息流机制。

- inherits_from_previous_cn：承接桥接两个组件的挑战。

- changes_argument_state_cn：确定主题注意力层为制品核心。

- sets_up_next_cn：给出β分解细节。

- failure_if_removed_cn：技术贡献核心缺失。

- evidence_pointer：Section 3.3 P3

### 21. Section 3.3 P4

- order：21

- locator：Section 3.3 P4

- paraphrase_cn：把主题词分布β分解为softmax(VF^T)，得到主题嵌入；L取100是效率与表达力的折中。

- move_code：DESIGN_FEATURE

- statement_status：design_decision

- why_here_cn：说明主题嵌入的构造和维度选择。

- inherits_from_previous_cn：承接注意力层需要主题嵌入。

- changes_argument_state_cn：为注意力公式提供对象。

- sets_up_next_cn：用主题嵌入作为上下文向量。

- failure_if_removed_cn：注意力层没有操作对象。

- evidence_pointer：Section 3.3 P4

### 22. Section 3.3 P5

- order：22

- locator：Section 3.3 P5

- paraphrase_cn：与标准注意力层用单一随机初始化上下文向量不同，sDTM用NTM主题嵌入作为上下文向量，使RNN关注全局主题信息。

- move_code：DESIGN_FEATURE

- statement_status：design_decision

- why_here_cn：突出与标准注意力方法的差异。

- inherits_from_previous_cn：承接主题嵌入。

- changes_argument_state_cn：把主题嵌入定义为查询向量。

- sets_up_next_cn：引入shifted topic proportion。

- failure_if_removed_cn：方法创新性被削弱。

- evidence_pointer：Section 3.3 P5

### 23. Section 3.3 P6

- order：23

- locator：Section 3.3 P6

- paraphrase_cn：注意力权重经softmax计算后按shifted topic proportion平均；δ使不同主题的梯度方向分离，增强主题区分度。

- move_code：DESIGN_FEATURE

- statement_status：design_decision

- why_here_cn：说明注意力加权和δ的机制理由。

- inherits_from_previous_cn：承接注意力权重公式。

- changes_argument_state_cn：给出文档表示生成方法。

- sets_up_next_cn：引出最终表示和输出。

- failure_if_removed_cn：注意力设计不完整。

- evidence_pointer：Section 3.3 P6

### 24. Section 3.4 P1-P3

- order：24

- locator：Section 3.4 P1-P3

- paraphrase_cn：目标是最大化联合边际似然p(l,d|β)；标签独立于词袋、依赖RNN输入和主题混合；直接积分不可解，用ELBO变分推断。

- move_code：THEORY_PROPOSITION

- statement_status：method_decision

- why_here_cn：把网络设计变成可优化的概率目标。

- inherits_from_previous_cn：承接模型组件。

- changes_argument_state_cn：建立联合训练目标。

- sets_up_next_cn：分解ELBO。

- failure_if_removed_cn：模型无法训练。

- evidence_pointer：Section 3.4 P1-P3

### 25. Section 3.4 P4-P6

- order：25

- locator：Section 3.4 P4-P6

- paraphrase_cn：ELBO由数据对数似然、标签对数似然和KL散度构成；分类标签用softmax/sigmoid，数值标签用高斯似然。

- move_code：METHOD_JUSTIFICATION

- statement_status：method_decision

- why_here_cn：说明目标函数的可操作分解和标签类型处理。

- inherits_from_previous_cn：承接ELBO。

- changes_argument_state_cn：使联合训练可计算。

- sets_up_next_cn：给出优化方法。

- failure_if_removed_cn：没有可计算的损失函数。

- evidence_pointer：Section 3.4 P4-P6

### 26. Section 3.4 P7

- order：26

- locator：Section 3.4 P7

- paraphrase_cn：用随机梯度上升联合更新所有参数；对Φ用重参数化估计梯度。

- move_code：METHOD_JUSTIFICATION

- statement_status：method_decision

- why_here_cn：给出参数更新方案。

- inherits_from_previous_cn：承接ELBO分解。

- changes_argument_state_cn：说明联合学习可实现。

- sets_up_next_cn：进入数据与实验。

- failure_if_removed_cn：训练可行性不清楚。

- evidence_pointer：Section 3.4 P7

## 制品设计理由逐句图谱

### 1. Section 3.3 P2

- locator：Section 3.3 P2

- paraphrase_cn：选择双向GRU而非普通RNN，是因为它广泛用于文本分类且能同时捕获前向与后向上下文。

- why_cn：序列组件需要捕获局部上下文，双向GRU是低风险、高普适的选择。

- design_tradeoff_cn：牺牲部分实现复杂度，换取稳定且可比的序列表示。

- evidence_pointer：Section 3.3 P2

### 2. Section 3.3 P3

- locator：Section 3.3 P3

- paraphrase_cn：主题注意力层使标签在反向传播时更新主题嵌入，在前向时把主题信息并入RNN表示。

- why_cn：单一组件同时实现监督信号注入和无监督主题信息的利用。

- design_tradeoff_cn：比简单拼接NTM与RNN更耦合，需要公式推导保证可微。

- evidence_pointer：Section 3.3 P3

### 3. Section 3.3 P4

- locator：Section 3.3 P4

- paraphrase_cn：将β分解为softmax(VF^T)以得到低维主题嵌入，并选择L=100。

- why_cn：直接使用高维β会让注意力层参数过多且不灵活，折中维度平衡效率与表达力。

- design_tradeoff_cn：L过大会增加计算成本，过小会限制主题表达。

- evidence_pointer：Section 3.3 P4

### 4. Section 3.3 P5

- locator：Section 3.3 P5

- paraphrase_cn：用NTM主题嵌入作为注意力上下文向量，替代标准注意力中的单一随机初始化向量。

- why_cn：使RNN能看全局主题信息，弥补监督深度学习主要关注局部上下文的不足。

- design_tradeoff_cn：放弃标准注意力的通用性，换取主题与序列的互信息传递。

- evidence_pointer：Section 3.3 P5

### 5. Section 3.3 P6

- locator：Section 3.3 P6

- paraphrase_cn：用shifted topic proportion平均注意力权重，δ使梯度对不同主题有不同符号。

- why_cn：δ的偏移让高概率主题与低概率主题在梯度中反向移动，增强主题区分度。

- design_tradeoff_cn：增加一个需要调参的超参数，但能解决注意力权重退化问题。

- evidence_pointer：Section 3.3 P6

### 6. Section 3.4 P1-P2

- locator：Section 3.4 P1-P2

- paraphrase_cn：假设标签独立于词袋表示，依赖RNN输入和主题混合，从而分解联合边际似然。

- why_cn：这个条件独立性使标签似然可以单独写出并纳入ELBO。

- design_tradeoff_cn：忽略标签与词袋之间的直接依赖，换来解决联合生成的复杂度。

- evidence_pointer：Section 3.4 P1-P2

### 7. Section 3.4 P3

- locator：Section 3.4 P3

- paraphrase_cn：用ELBO替代不可解的积分最大化联合似然。

- why_cn：变分推断是贝叶斯深度主题模型的标准解法，使所有组件可端到端训练。

- design_tradeoff_cn：ELBO是真实似然的下界，存在近似误差，但可扩展到大规模数据。

- evidence_pointer：Section 3.4 P3

### 8. Section 3.4 P4-P6

- locator：Section 3.4 P4-P6

- paraphrase_cn：分类标签用softmax/sigmoid，数值标签用高斯似然。

- why_cn：标签类型决定输出层的分布假设，使模型能同时处理Yelp评分二分类和Stack Exchange类别多分类。

- design_tradeoff_cn：对数值标签引入方差超参数σ_l，需在应用中设置。

- evidence_pointer：Section 3.4 P4-P6

### 9. Section 4预处理

- locator：Section 4预处理

- paraphrase_cn：两个数据集都保留词频最高的2000词作为主题词表，并随机80/20分割。

- why_cn：控制词表规模以稳定NTM训练，并给出留出集评估。

- design_tradeoff_cn：小词表提高效率但可能丢失低频语义。

- evidence_pointer：Section 4末尾

### 10. Section 5.1超参数

- locator：Section 5.1超参数

- paraphrase_cn：RNN序列长度按95百分位设为300和500，δ与K用网格搜索。

- why_cn：使模型能覆盖绝大多数文档，同时避免过长序列的计算浪费。

- design_tradeoff_cn：网格搜索增加调参成本，但能报告稳健性。

- evidence_pointer：Section 5.1

## Study开头、过渡与收束图谱

### 1. Section 4 opening

- locator：Section 4 opening

- role：opening

- paraphrase_cn：在评估前先描述两个数据集，均与IS研究高度相关。

- function_cn：为评价提供数据背景和IS相关性。

- evidence_pointer：Section 4首段

### 2. Section 4.1 opening

- locator：Section 4.1 opening

- role：opening

- paraphrase_cn：Yelp评论广泛用于IS研究，评分可作为辅助标签。

- function_cn：说明案例1的现实基础和标签可利用性。

- evidence_pointer：Section 4.1 P1

### 3. Section 4.2 opening

- locator：Section 4.2 opening

- role：opening

- paraphrase_cn：Stack Exchange知识社区也是IS常用场景，帖子类别可作为辅助标签。

- function_cn：说明案例2的现实基础和标签可利用性。

- evidence_pointer：Section 4.2 P1

### 4. Section 4 closing

- locator：Section 4 closing

- role：closure

- paraphrase_cn：两个数据集统一预处理，80/20分割，Table 3给出摘要统计。

- function_cn：固定数据格式，为后续所有实验提供共同基础。

- evidence_pointer：Section 4末段

### 5. Section 5 opening

- locator：Section 5 opening

- role：opening

- paraphrase_cn：概率主题模型的常见评价是留出集上的拟合度，本文用困惑度衡量。

- function_cn：建立第一层评价指标并解释其重要性。

- evidence_pointer：Section 5 P1

### 6. Section 5.1 baselines

- locator：Section 5.1 baselines

- role：method

- paraphrase_cn：列出无监督基线LDA/NTM和监督基线sLDA/MedLDA/BP-sLDA/sNNTM，并说明公平调参和附录中的稳健性检验。

- function_cn：定义对比对象与评价公平性。

- evidence_pointer：Section 5.1

### 7. Section 5 result perplexity

- locator：Section 5 result perplexity

- role：result

- paraphrase_cn：Table 4显示sDTM两个数据集所有K下困惑度显著最低；sLDA优于LDA也说明利用标签的益处。

- function_cn：给出第一层核心证据：模型拟合更强。

- evidence_pointer：Section 5 Table 4后

### 8. Section 5 topic quality

- locator：Section 5 topic quality

- role：result

- paraphrase_cn：sDTM能学到带情感极性的主题，如负面服务主题，而LDA/NTM缺乏这种极性。

- function_cn：用主题词例展示监督标签带来主题语义改善。

- evidence_pointer：Section 5 Tables 6-7

### 9. Section 5 valence quantitative

- locator：Section 5 valence quantitative

- role：result

- paraphrase_cn：用VADER量化主题极性，sDTM产生更多正负值和更高标准差，NTM在附录也表现中性。

- function_cn：把主题质量从定性升级为定量。

- evidence_pointer：Section 5 Table 5

### 10. Section 5 closing transition

- locator：Section 5 closing transition

- role：transition

- paraphrase_cn：模型拟合和主题词示例验证了sDTM的改进，但能否帮研究者构造更准确变量和预测模型仍未知，因此转向实证和预测。

- function_cn：桥接离线拟合与下游应用。

- evidence_pointer：Section 5末段

### 11. Section 6 opening

- locator：Section 6 opening

- role：opening

- paraphrase_cn：变量测量质量影响实证估计，因此准确的主题建模能派生更好变量；本节用两个实证研究检验sDTM。

- function_cn：解释实证评价的逻辑。

- evidence_pointer：Section 6首段

### 12. Section 6.1 opening

- locator：Section 6.1 opening

- role：opening

- paraphrase_cn：案例1在Yelp检验评论主题熵与有用性的关系，引述Ghose等和Gong等的复杂度预期。

- function_cn：设定假设和变量构造方式。

- evidence_pointer：Section 6.1 P1-P2

### 13. Section 6.1 results

- locator：Section 6.1 results

- role：result

- paraphrase_cn：TopicEntropy_sDTM显著负向，LDA/NTM不显著；子样本重复1000次中sDTM显著次数远多于LDA。

- function_cn：证明sDTM派生变量在实证回归中的有效性和统计功效优势。

- evidence_pointer：Section 6.1 Tables 8-9

### 14. Section 6.2 opening

- locator：Section 6.2 opening

- role：opening

- paraphrase_cn：案例2在Stack Exchange检验问答主题相似性与答案有用性，引述Peng等的语义一致性预期。

- function_cn：设定第二个跨场景假设。

- evidence_pointer：Section 6.2 P1-P2

### 15. Section 6.2 results

- locator：Section 6.2 results

- role：result

- paraphrase_cn：QASimilarity_sDTM显著正相关，LDA/NTM不显著，且变量自动生成、无需人工标注。

- function_cn：证明sDTM在另一类IS场景中的外部效度。

- evidence_pointer：Section 6.2 Table 10

### 16. Section 7 opening

- locator：Section 7 opening

- role：opening

- paraphrase_cn：IS研究者也常把主题模型用于预测，通常先LDA提取特征再送入分类器，因此需要评估sDTM预测能力。

- function_cn：从实证引入预测评价。

- evidence_pointer：Section 7 P1

### 17. Section 7.1 baselines

- locator：Section 7.1 baselines

- role：method

- paraphrase_cn：基线分为无监督主题模型两阶段、监督主题模型、监督PCA、以及RNN attention/Bi-LSTM/DistilBERT/BERT；RNN attention作为消融组件。

- function_cn：定义预测评价的对比谱系和消融设计。

- evidence_pointer：Section 7.1

### 18. Section 7.2 metrics and results

- locator：Section 7.2 metrics and results

- role：result

- paraphrase_cn：Yelp用AUROC，Stack Exchange用准确率；Table 11显示sDTM显著优于主题模型基线和RNN attention，并与BERT可比。

- function_cn：给出预测证据并解释主题信息带来的增量。

- evidence_pointer：Section 7.2 Table 11

### 19. Section 7 closing

- locator：Section 7 closing

- role：closure

- paraphrase_cn：sDTM虽本质是主题模型，但能像标准主题模型一样总结文档，便于实证使用，这是黑箱BERT难以实现的。

- function_cn：把预测优势转向可解释性优势，为讨论铺垫。

- evidence_pointer：Section 7末段

## 讨论与贡献逐句图谱

### 1. Discussion P1 S1

- order：1

- locator：Discussion P1 S1

- paraphrase_cn：文献综述表明主题建模是IS和管理研究中使用越来越多的强大工具。

- move_code：CONTRIBUTION

- statement_status：contribution_claim

- why_here_cn：讨论开头重述引言背景，形成闭环。

- inherits_from_previous_cn：承接全文问题。

- changes_argument_state_cn：把技术结果放回领域背景。

- sets_up_next_cn：指出标签未被利用。

- failure_if_removed_cn：讨论脱离引言问题。

- evidence_pointer：Discussion P1 S1

### 2. Discussion P1 S2

- order：2

- locator：Discussion P1 S2

- paraphrase_cn：许多真实文本数据带有辅助信息，但传统LDA未纳入，可能导致主题分析表现差。

- move_code：CONTRIBUTION

- statement_status：contribution_claim

- why_here_cn：重申核心缺口。

- inherits_from_previous_cn：承接第一句。

- changes_argument_state_cn：把方法价值与已识别缺口绑定。

- sets_up_next_cn：引出后果。

- failure_if_removed_cn：贡献没有针对的问题。

- evidence_pointer：Discussion P1 S2

### 3. Discussion P1 S3

- order：3

- locator：Discussion P1 S3

- paraphrase_cn：这可能进一步导致实证估计不准确或预测性能差。

- move_code：CONTRIBUTION

- statement_status：contribution_claim

- why_here_cn：把缺口后果再陈述一遍。

- inherits_from_previous_cn：承接缺口。

- changes_argument_state_cn：强化解决问题的紧迫性。

- sets_up_next_cn：引出sDTM方案。

- failure_if_removed_cn：解决问题的重要性不足。

- evidence_pointer：Discussion P1 S3

### 4. Discussion P1 S4

- order：4

- locator：Discussion P1 S4

- paraphrase_cn：因此本文提出并评估纳入辅助标签的监督式深度主题建模方法。

- move_code：CONTRIBUTION

- statement_status：contribution_claim

- why_here_cn：给出研究交付物。

- inherits_from_previous_cn：承接问题与后果。

- changes_argument_state_cn：完成问题到方案的闭环。

- sets_up_next_cn：总结方法结果。

- failure_if_removed_cn：讨论缺解决方案。

- evidence_pointer：Discussion P1 S4

### 5. Discussion P2 S1

- order：5

- locator：Discussion P2 S1

- paraphrase_cn：本文的监督式深度主题建模结合无监督神经主题建模与监督RNN。

- move_code：CONTRIBUTION

- statement_status：contribution_claim

- why_here_cn：重述技术方案。

- inherits_from_previous_cn：承接方案提出。

- changes_argument_state_cn：强调方法创新。

- sets_up_next_cn：给实验结果总结。

- failure_if_removed_cn：方法创新没有被归纳。

- evidence_pointer：Discussion P2 S1

### 6. Discussion P2 S2

- order：6

- locator：Discussion P2 S2

- paraphrase_cn：两个IS数据集上的实验显示sDTM从多个方面显著提升主题模型质量。

- move_code：CONTRIBUTION

- statement_status：empirical_result

- why_here_cn：把实验证据再提炼。

- inherits_from_previous_cn：承接方法描述。

- changes_argument_state_cn：结果支持贡献。

- sets_up_next_cn：说明对实证与预测的意义。

- failure_if_removed_cn：贡献缺乏证据。

- evidence_pointer：Discussion P2 S2

### 7. Discussion P2 S3

- order：7

- locator：Discussion P2 S3

- paraphrase_cn：方法既能缓解ML模型不准确导致的测量误差，又能提高预测准确率。

- move_code：CONTRIBUTION

- statement_status：contribution_claim

- why_here_cn：概括两大价值：实证与预测。

- inherits_from_previous_cn：承接实验总结。

- changes_argument_state_cn：把结果转成IS关心的收益。

- sets_up_next_cn：给出主要启示。

- failure_if_removed_cn：用户价值不明确。

- evidence_pointer：Discussion P2 S3

### 8. Discussion P2 S4

- order：8

- locator：Discussion P2 S4

- paraphrase_cn：主要启示是研究者可利用辅助标签实现高质量主题建模。

- move_code：CONTRIBUTION

- statement_status：contribution_claim

- why_here_cn：给出可操作的关键信息。

- inherits_from_previous_cn：承接两大价值。

- changes_argument_state_cn：把方法贡献简化为一句话。

- sets_up_next_cn：引出即插即用声明。

- failure_if_removed_cn：核心启示缺失。

- evidence_pointer：Discussion P2 S4

### 9. Discussion P2 S5

- order：9

- locator：Discussion P2 S5

- paraphrase_cn：IS和商业学者可以直接把sDTM作为即插即用工具，无需大幅改造文本分析流程。

- move_code：CONTRIBUTION

- statement_status：contribution_claim

- why_here_cn：强化低采用门槛。

- inherits_from_previous_cn：承接主要启示。

- changes_argument_state_cn：把贡献包装为替换工具。

- sets_up_next_cn：扩展到其他领域。

- failure_if_removed_cn：可复用贡献不完整。

- evidence_pointer：Discussion P2 S5

### 10. Discussion P3 S1

- order：10

- locator：Discussion P3 S1

- paraphrase_cn：实证和预测评价显示sDTM能推进IS文本分析，在会计金融等其他学科也有用。

- move_code：BOUNDARY

- statement_status：author_inference

- why_here_cn：把贡献扩展到相邻领域。

- inherits_from_previous_cn：承接两个数据集结果。

- changes_argument_state_cn：提出边界外应用。

- sets_up_next_cn：给出长文本具体场景。

- failure_if_removed_cn：外部性缺失。

- evidence_pointer：Discussion P3 S1

### 11. Discussion P3 S2

- order：11

- locator：Discussion P3 S2

- paraphrase_cn：会计金融研究已用主题建模分析公司披露，如10-K和电话会议记录。

- move_code：BOUNDARY

- statement_status：prior_literature

- why_here_cn：用文献证明拓展场景的真实性。

- inherits_from_previous_cn：承接拓展声明。

- changes_argument_state_cn：把拓展落地为具体数据类型。

- sets_up_next_cn：指出transformer局限。

- failure_if_removed_cn：拓展场景无事实依据。

- evidence_pointer：Discussion P3 S2

### 12. Discussion P3 S3

- order：12

- locator：Discussion P3 S3

- paraphrase_cn：这些披露很长，transformer模型受序列长度限制，而sDTM本质是降维方法，可缓解该问题。

- move_code：BOUNDARY

- statement_status：author_inference

- why_here_cn：给出sDTM在该场景的技术优势。

- inherits_from_previous_cn：承接长文本披露。

- changes_argument_state_cn：把架构特性转为边界优势。

- sets_up_next_cn：指出可用的辅助标签。

- failure_if_removed_cn：拓展优势不具体。

- evidence_pointer：Discussion P3 S3

### 13. Discussion P3 S4

- order：13

- locator：Discussion P3 S4

- paraphrase_cn：在公司披露情境中，行业代码可作为辅助标签。

- move_code：BOUNDARY

- statement_status：author_inference

- why_here_cn：给出具体标签设计。

- inherits_from_previous_cn：承接优势。

- changes_argument_state_cn：使方法可迁移性更具体。

- sets_up_next_cn：描述潜在收益。

- failure_if_removed_cn：迁移应用缺可操作标签。

- evidence_pointer：Discussion P3 S4

### 14. Discussion P3 S5

- order：14

- locator：Discussion P3 S5

- paraphrase_cn：其前景是学到更好的披露表示，并构造更准确的变量，如披露与分析师报告相似性、风险主题、创新指标。

- move_code：BOUNDARY

- statement_status：author_inference

- why_here_cn：用具体变量类型说明潜在贡献。

- inherits_from_previous_cn：承接行业代码标签。

- changes_argument_state_cn：把边界扩展转为研究议程。

- sets_up_next_cn：转向实践者价值。

- failure_if_removed_cn：拓展价值空洞。

- evidence_pointer：Discussion P3 S5

### 15. Discussion P4 S1

- order：15

- locator：Discussion P4 S1

- paraphrase_cn：实践者也能受益于sDTM。

- move_code：CONTRIBUTION

- statement_status：contribution_claim

- why_here_cn：引入实践者视角。

- inherits_from_previous_cn：承接研究者应用。

- changes_argument_state_cn：扩大受众。

- sets_up_next_cn：举趋势实例。

- failure_if_removed_cn：实践价值缺失。

- evidence_pointer：Discussion P4 S1

### 16. Discussion P4 S2

- order：16

- locator：Discussion P4 S2

- paraphrase_cn：深度学习主题模型在文档理解上比传统LDA更有效，云平台已开始提供VAE式神经主题建模。

- move_code：CONTEXT

- statement_status：prior_literature

- why_here_cn：用工业趋势佐证方法方向的可行性。

- inherits_from_previous_cn：承接实践者价值。

- changes_argument_state_cn：说明市场已接受该方向。

- sets_up_next_cn：给出本文的工具定位。

- failure_if_removed_cn：实践趋势证据不足。

- evidence_pointer：Discussion P4 S2

### 17. Discussion P4 S3

- order：17

- locator：Discussion P4 S3

- paraphrase_cn：本文开源方法可成为实践者文本分析流程中准确方便的工具。

- move_code：CONTRIBUTION

- statement_status：contribution_claim

- why_here_cn：把方法定位为可落地工具。

- inherits_from_previous_cn：承接云平台趋势。

- changes_argument_state_cn：完成实践贡献。

- sets_up_next_cn：转入限制。

- failure_if_removed_cn：实践贡献没有落脚点。

- evidence_pointer：Discussion P4 S3

### 18. Discussion P5 S1

- order：18

- locator：Discussion P5 S1

- paraphrase_cn：局限之一是只验证两个数据集；虽有电影和Wikipedia附录检验，会计等其他领域仍待未来验证。

- move_code：LIMITATION

- statement_status：author_inference

- why_here_cn：坦诚边界，避免过度推广。

- inherits_from_previous_cn：承接全部贡献。

- changes_argument_state_cn：设定可信的边界。

- sets_up_next_cn：引出第二点限制。

- failure_if_removed_cn：推广声明显得无根据。

- evidence_pointer：Discussion P5 S1

### 19. Discussion P5 S2

- order：19

- locator：Discussion P5 S2

- paraphrase_cn：局限之二是与其他ML方法一样需要超参数调优，未来可探索更省成本的训练方法。

- move_code：LIMITATION

- statement_status：author_inference

- why_here_cn：承认实用性障碍。

- inherits_from_previous_cn：承接第一点限制。

- changes_argument_state_cn：给出未来研究方向。

- sets_up_next_cn：进入最终呼吁。

- failure_if_removed_cn：限制讨论不完整。

- evidence_pointer：Discussion P5 S2

### 20. Discussion P6 S1

- order：20

- locator：Discussion P6 S1

- paraphrase_cn：IS研究需要有效计算方法来利用大数据分析的力量，希望sDTM能帮助学者和实践者从非结构化文本中获得洞察。

- move_code：CLOSING

- statement_status：contribution_claim

- why_here_cn：呼应引言开篇，完成全文闭环。

- inherits_from_previous_cn：承接全部贡献与限制。

- changes_argument_state_cn：把文章定位为对IS计算方法的回应。

- sets_up_next_cn：以开源落款。

- failure_if_removed_cn：全文缺少收束。

- evidence_pointer：Discussion P6 S1

### 21. Discussion P6 S2

- order：21

- locator：Discussion P6 S2

- paraphrase_cn：开源Python实现以最大化研究和实践影响。

- move_code：CLOSING

- statement_status：contribution_claim

- why_here_cn：以可复现性收尾。

- inherits_from_previous_cn：承接最终呼吁。

- changes_argument_state_cn：把贡献落到可获取资源。

- sets_up_next_cn：无

- failure_if_removed_cn：开源承诺缺失。

- evidence_pointer：Discussion P6 S2

## Study累积逻辑

### 1. 1

- study_or_phase：问题识别与文献缺口

- evidence_job_cn：证明现有无监督主题模型忽略辅助标签这一缺口的普遍性和重要性。

- what_it_establishes_cn：LDA广泛用于IS的两阶段分析，且忽略标签会造成测量误差。

- what_it_cannot_establish_cn：不能证明存在可以改进的设计。

- why_next_phase_is_needed_cn：需要提出具体方法。

- transition_wording_function_cn：以“为克服挑战我们提出sDTM”进入设计。

### 2. 2

- study_or_phase：sDTM设计与推导

- evidence_job_cn：证明存在可实现的统一监督深度主题模型。

- what_it_establishes_cn：NTM加双向GRU可按主题注意力层桥接，ELBO可联合优化。

- what_it_cannot_establish_cn：不能证明该设计在真实数据上有效。

- why_next_phase_is_needed_cn：需要数据和实验验证。

- transition_wording_function_cn：“接下来描述两个数据集”进入实验。

### 3. 3

- study_or_phase：数据收集与预处理

- evidence_job_cn：提供两个IS相关数据集及可用标签，并确立可复现的预处理和分割。

- what_it_establishes_cn：Yelp有评分，Stack Exchange有类别，均适合验证方法。

- what_it_cannot_establish_cn：不能证明模型在这些数据上有效。

- why_next_phase_is_needed_cn：需要模型拟合比较。

- transition_wording_function_cn：“首先评估模型拟合”进入第一层评价。

### 4. 4

- study_or_phase：模型拟合评估

- evidence_job_cn：证明sDTM作为主题模型的基本质量和泛化能力。

- what_it_establishes_cn：困惑度显著低于多类基线，主题更具情感极性。

- what_it_cannot_establish_cn：不能证明这些改进转化为实证或预测收益。

- why_next_phase_is_needed_cn：需要检验下游应用的实用价值。

- transition_wording_function_cn：“改进能否帮研究者构造更准确变量仍未知，因此转向实证和预测”。

### 5. 5

- study_or_phase：实证案例1：主题熵与评论有用性

- evidence_job_cn：证明sDTM派生变量在实证回归中比LDA/NTM更显著，并提高统计功效。

- what_it_establishes_cn：同一变量由sDTM派生时效应显著且方向符合文献。

- what_it_cannot_establish_cn：不能证明在其他IS场景中同样成立。

- why_next_phase_is_needed_cn：需要第二个场景增强外部效度。

- transition_wording_function_cn：“在第二个研究中转向在线知识社区”。

### 6. 6

- study_or_phase：实证案例2：问答相似性与答案有用性

- evidence_job_cn：证明sDTM在另一类IS文本中的外部效度。

- what_it_establishes_cn：sDTM派生的QA相似性变量显著解释答案有用性，基线不显著。

- what_it_cannot_establish_cn：不能证明在端到端预测任务中的优势。

- why_next_phase_is_needed_cn：需要预测任务验证监督学习的实际使用方式。

- transition_wording_function_cn：“除实证外，IS研究者也在预测分析中使用主题模型”。

### 7. 7

- study_or_phase：预测研究

- evidence_job_cn：证明sDTM在监督预测中优于两阶段方法和监督主题模型，并通过消融说明主题组件贡献。

- what_it_establishes_cn：Yelp AUROC和Stack Exchange准确率显著提升，接近BERT。

- what_it_cannot_establish_cn：不能证明在更长文档或数值标签上的表现，以及主题注意力层的内部机制。

- why_next_phase_is_needed_cn：需要讨论贡献、边界和未来。

- transition_wording_function_cn：预测研究末段把性能优势转为可解释性优势，进入讨论。

## 主张—证据台账

### 1. sDTM在两个数据集、多种主题数下困惑度显著低于所有主题模型基线。

- claim_cn：sDTM在两个数据集、多种主题数下困惑度显著低于所有主题模型基线。

- claim_level：technical

- supporting_evidence_cn：Table 4中sDTM全部比较均显著低于NTM等基线。

- support_strength：direct

- where_claim_is_made：Section 5 Table 4后

- where_evidence_is_provided：Table 4

### 2. sDTM比LDA/NTM学到更多情感极性主题。

- claim_cn：sDTM比LDA/NTM学到更多情感极性主题。

- claim_level：artifact

- supporting_evidence_cn：Table 5-7显示sDTM有18个极性主题，LDA仅7个；主题词含情感词。

- support_strength：direct

- where_claim_is_made：Section 5主题质量段

- where_evidence_is_provided：Tables 5-7

### 3. sDTM派生变量在实证回归中更显著且方向符合理论。

- claim_cn：sDTM派生变量在实证回归中更显著且方向符合理论。

- claim_level：artifact

- supporting_evidence_cn：Tables 8和10中sDTM变量显著，LDA/NTM不显著或弱显著。

- support_strength：direct

- where_claim_is_made：Section 6.1和6.2结果段

- where_evidence_is_provided：Tables 8和10

### 4. sDTM能降低错误接受零假设的概率，提高统计功效。

- claim_cn：sDTM能降低错误接受零假设的概率，提高统计功效。

- claim_level：design_knowledge

- supporting_evidence_cn：Table 9的1000次子样本分析中sDTM在5%水平显著744次，LDA仅147次。

- support_strength：direct

- where_claim_is_made：Section 6.1子样本段

- where_evidence_is_provided：Table 9

### 5. sDTM预测显著优于主题模型基线和RNN attention。

- claim_cn：sDTM预测显著优于主题模型基线和RNN attention。

- claim_level：technical

- supporting_evidence_cn：Table 11中sDTM的AUROC和准确率显著高于所有主题模型基线，并优于消融RNN attention。

- support_strength：direct

- where_claim_is_made：Section 7.2结果段

- where_evidence_is_provided：Table 11

### 6. sDTM性能与BERT相当甚至更好。

- claim_cn：sDTM性能与BERT相当甚至更好。

- claim_level：technical

- supporting_evidence_cn：sDTM Yelp AUROC 0.948 vs BERT 0.954，Stack Exchange 0.918 vs 0.920，实际略低但称为comparable或better；未报告与BERT的显著性检验。

- support_strength：partial

- where_claim_is_made：摘要和Section 7.2

- where_evidence_is_provided：Table 11

### 7. 主题注意力层是性能提升的关键来源。

- claim_cn：主题注意力层是性能提升的关键来源。

- claim_level：mechanism

- supporting_evidence_cn：sDTM显著优于其监督组件RNN attention，说明加入NTM/主题注意力带来增量。

- support_strength：partial

- where_claim_is_made：Section 3.3和7.2

- where_evidence_is_provided：Table 11中RNN attention对比

### 8. sDTM可直接替换LDA且无需重构分析流程。

- claim_cn：sDTM可直接替换LDA且无需重构分析流程。

- claim_level：design_knowledge

- supporting_evidence_cn：架构上以文档主题分布和预测输出对接下游，且开源实现；但没有在多种异构两阶段流程中验证无缝替换。

- support_strength：asserted

- where_claim_is_made：Introduction P6与Discussion P2

- where_evidence_is_provided：全文架构与实验设计

### 9. sDTM能推广到会计金融等长文本场景。

- claim_cn：sDTM能推广到会计金融等长文本场景。

- claim_level：boundary

- supporting_evidence_cn：仅给出行业代码标签和长文本降维优势的论证，辅以Wikipedia和电影数据集附录。

- support_strength：asserted

- where_claim_is_made：Discussion P3

- where_evidence_is_provided：Discussion P3与Online Appendices D/E

## ISR定位逻辑

- constitutive_is_problem_cn：文本数据与实证、预测研究流程相互构成：IS研究者把主题模型当两阶段分析的特征工程工具，因此主题向量质量直接决定后续变量准确性和预测性能；文章把算法问题变成IS研究中的测量误差问题。

- technology_behavior_or_market_entanglement_cn：技术设计不是随意替换的工具，因为真实平台的文本总是伴随评分、板块、类别等平台制度性元数据；这些元数据既来自平台行为，又能反过来改善主题建模，形成数据环境、用户生成内容与算法之间的纠缠。

- role_of_benchmark_or_objective_evidence_cn：困惑度、VADER极性、回归系数、子样本功效和AUROC等客观证据被用来支持“减少测量误差、提高实证检验功效、改善预测”这些IS主张，而不是仅仅证明分数优势。

- theory_in_design_cn：没有正式组织理论进入设计；设计主要受“辅助标签监督信号能提高主题判别性”这一知识驱动。理论只出现在下游案例（评论复杂度、问答语义一致性）用于验证派生变量有效性，属于结果效度层面，而非设计层面。

- technical_vs_is_contribution_balance_cn：技术细节约占全文一半，但贡献声明和讨论集中在IS实证和预测效用上；作者用两个IS数据集、测量误差文献和可解释性把技术贡献包装成可替换LDA的研究工具。

- beyond_transient_performance_cn：文章通过三层次证据超越一次性分数优势：模型拟合证明基础能力，实证案例证明派生变量在经济关系中的效度与统计功效，预测任务加消融证明主题组件的增量贡献；最后以开源和插件式定位强化可复用性。

## 段落级仿写模板

### abstract_steps

1. 先确立工具地位：主题建模是文本分析的有力工具。

2. 指出工具在IS中的具体使用方式：主题探索和特征工程。

3. 指出共同局限：无监督、忽略辅助标签。

4. 给出后果：主题不准确影响实证和预测。

5. 提出制品：命名模型并给出关键组件。

6. 说明机制：利用辅助数据增强主题建模。

7. 说明评价数据与任务：两个IS数据集上的实证与预测。

8. 给出结果：优于基准、提升实证与预测。

9. 给出贡献：方法论贡献和直接相关性。

### introduction_paragraph_steps

1. 首段从数字化数据浪潮进入主题建模。

2. 第二段聚焦两阶段分析范式并给出实例，指出主题向量准确性关键。

3. 第三段指出无监督局限与元数据普遍性，说明贝叶斯纳入困难。

4. 第四段提出模型、机制和直觉例子。

5. 第五段按模型拟合、实证、预测三点预告评价。

6. 第六段给出三条贡献并以开源收束。

### theory_to_design_steps

1. 文献综述分三步：应用现状、已有监督模型及其缺陷、IS方法数据科学关切。

2. 用表格固定已有模型与本文差异。

3. 设计开始时用直观例子说明为什么标签重要。

4. 用范式路径图对比两阶段与单阶段。

5. 先引入基础组件NTM，再引入序列编码器。

6. 用主题注意力层桥接并解释双向信息流。

7. 给出β分解、注意力公式、δ偏移等关键设计。

8. 用联合ELBO把设计变成可优化目标。

### method_and_study_sequence_steps

1. 数据段先说明数据集的IS相关性，再说明标签可用性。

2. 模型拟合段先解释困惑度指标，再列出所有基线。

3. 先报告表格中的整体结果，再用主题词示例和情感性量化补充。

4. 段末用“拟合好是否能转化为实际价值未知”过渡。

5. 实证段先说明测量质量影响估计，再逐案例给假设、变量、回归、子样本功效。

6. 案例2选择不同数据源以建立外部效度。

7. 预测段先描述两阶段范式，再列分组基线并设消融对照。

### results_reporting_steps

1. 每一层结果先定义指标和为什么用该指标。

2. 表格前说明对比对象，表格后写“我们做几个观察”。

3. 观察按主结果、监督效应、定性例子、定量补充排序。

4. 每个结果后回接研究问题。

5. 在节末用未解决问题过渡到下一层。

### discussion_and_contribution_steps

1. 第一段重述引言缺口。

2. 第二段总结方法、实验和核心启示。

3. 第三段给出相邻领域的边界应用，并指定可用标签。

4. 第四段说明实践者价值。

5. 第五段列出限制和未来。

6. 第六段呼应IS对计算方法的呼吁并以开源收尾。

## 可执行写作算法

### 1. 1

- step：1

- rhetorical_job_cn：建立研究背景和工具地位。

- research_evidence_required_cn：需要证明主题建模在目标领域被广泛使用的文献证据。

- sentence_pattern_function_cn：从数字数据现象出发，逐句收窄到工具。

- transition_condition_cn：当读者接受LDA是主流工具后进入下一步。

### 2. 2

- step：2

- rhetorical_job_cn：介绍两阶段使用范式并指出其准确性依赖。

- research_evidence_required_cn：需要已发表的两阶段应用实例。

- sentence_pattern_function_cn：先描述通用流程，再给实例，最后指出关键假设。

- transition_condition_cn：当读者理解主题向量准确性的关键性后进入下一步。

### 3. 3

- step：3

- rhetorical_job_cn：定义核心缺口：无监督方法忽略辅助标签，且纳入困难。

- research_evidence_required_cn：需要现实平台中标签存在的实例和已有模型局限的文献。

- sentence_pattern_function_cn：先指出无监督，再列元数据实例，再讲贝叶斯纳入困难。

- transition_condition_cn：当缺口和后果清楚后进入方案。

### 4. 4

- step：4

- rhetorical_job_cn：提出制品并解释机制。

- research_evidence_required_cn：需要可实现的架构、明确的机制和直觉例子。

- sentence_pattern_function_cn：先给方案名称和组件，再分别解释前向与后向信息流，搭配小例子。

- transition_condition_cn：当读者能想象模型如何工作时进入评价预告。

### 5. 5

- step：5

- rhetorical_job_cn：预告三层次评价。

- research_evidence_required_cn：需要各层次确实准备的数据、基线和指标。

- sentence_pattern_function_cn：用“从三个角度展示”做导航，每个角度给结果预览。

- transition_condition_cn：当评价范围和预期结果清楚后进入详细方法。

### 6. 6

- step：6

- rhetorical_job_cn：选择两个IS相关数据集并说明标签。

- research_evidence_required_cn：需要真实数据集、预处理方式和标签。

- sentence_pattern_function_cn：每个数据集先引用IS文献，再说明标签可作为辅助信息。

- transition_condition_cn：当数据可比且可复现后进入第一层实验。

### 7. 7

- step：7

- rhetorical_job_cn：用离线拟合证明基础能力。

- research_evidence_required_cn：需要困惑度、主题词和情感性量化等多重证据。

- sentence_pattern_function_cn：先指标定义，再基线，再表格，再主题示例，再量化。

- transition_condition_cn：当基础拟合优势确立后，用“能否转化为实际价值未知”过渡。

### 8. 8

- step：8

- rhetorical_job_cn：用两个实证案例证明变量的下游效度和统计功效。

- research_evidence_required_cn：需要每个案例有明确假设、同一变量由不同模型派生、回归对照和子样本功效分析。

- sentence_pattern_function_cn：每个案例从文献假设出发，构造变量，报告回归，再强调显著性差异。

- transition_condition_cn：当两种场景都支持sDTM后进入预测任务。

### 9. 9

- step：9

- rhetorical_job_cn：用预测任务证明端到端监督学习价值并做消融。

- research_evidence_required_cn：需要两阶段基线、监督主题模型、深度学习基线和消融组件。

- sentence_pattern_function_cn：先描述两阶段预测范式，再按组列基线，报告指标和表格，解释提升来源。

- transition_condition_cn：当预测结果与消融证据都到位后进入讨论。

### 10. 10

- step：10

- rhetorical_job_cn：把结果转成贡献、边界和未来研究。

- research_evidence_required_cn：需要明确的可替换定位、相邻领域的具体标签设想和诚实限制。

- sentence_pattern_function_cn：重述缺口、总结证据、扩展领域、给出标签、列出限制、以开放资源收尾。

- transition_condition_cn：当全文形成问题-方案-证据-贡献的闭环后结束。

## 应模仿的高价值动作

1. 在方法设计前用手机电池评论例子让‘标签能分离正负情感主题’这一机制变得直观。

2. 用Figure 1的P1-P4路径图把两阶段旧范式与单阶段新范式并置，清晰展示标签参与推断的位置差异。

3. 在实证案例中让LDA、NTM、sDTM派生同一个变量进入同一回归，形成最直接的变量质量对照。

4. 用1000次随机子样本分析把sDTM的优势从系数显著性升级为统计功效论断。

5. 把消融组件（RNN attention）作为预测基线，同时验证机制和性能增量。

6. 把模型贡献定位为‘可直接替换LDA’并开源，降低IS研究者的采用门槛。

7. 在讨论中为其他学科给出具体的辅助标签（行业代码）和具体变量类型（披露相似性、风险主题、创新指标），使边界扩展不只是口号。

## 不要只复制的表面动作

1. 没有完整的拟合-实证-预测三层证据链就宣称‘优于LDA’。

2. 没有做同一变量的多模型对照就声称派生变量更准确。

3. 没有消融实验就断言注意力层是提升来源。

4. 没有在两个以上场景验证就声称广泛适用。

5. 没有开源实现就宣称即插即用。

6. 只报表格星星而不解释统计功效和效应方向是否与理论一致。

## 证据薄弱或跳跃的动作

1. 摘要和正文称性能‘与BERT相当或更好’，但表中的数值略低于BERT且未对BERT差异做显著性检验。

2. ‘可直接替换LDA’更多是架构层面的推论，没有在多种异构分析流程中做替换实验。

3. 会计金融等长文本的适用性是推断，主要靠附录的Wikipedia和电影数据支撑，且未在真实披露文本上验证。

4. 主题注意力层的双向信息流机制未被中介分析直接检验，只能通过消融和主题情感性间接推断。

5. 子样本功效分析只对比了sDTM与LDA，没有对比NTM。

## 一句话套路

本文的ISR套路是：把一个在IS文本分析中被广泛使用但忽略平台元数据的工具（LDA）定义为核心缺口，构建一个能利用辅助标签的深度主题模型，通过拟合→实证→预测三层递进证据把算法性能转译为测量误差缓解、统计功效提高和可解释预测能力，最后以可直接替换LDA的插件式方法定位贡献。

## 分析边界

全文为OCR/Markdown转录，个别公式和表格可能有字符错乱；第一阶段分析中有几处表格编号与正文不完全一致（如Table 5的GSM应为NTM，部分Online Appendix编号顺序与正文引述不完全对应）；附录A-E未在正文给出，故对长文档和数值标签的稳健性分析只能依据正文引用推断；段落位置依据可见标题和内容近似编码，若遇到图表切分可能有偏离。
