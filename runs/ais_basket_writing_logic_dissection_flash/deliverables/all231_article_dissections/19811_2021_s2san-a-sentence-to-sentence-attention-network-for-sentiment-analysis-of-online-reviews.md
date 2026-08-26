# S2SAN: A sentence-to-sentence attention network for sentiment analysis of online reviews

- 作者：Ping Wang; Jiangnan Li; Jingrui Hou
- 年份 / 期刊：2021 / Decision Support Systems
- DOI：10.1016/j.dss.2021.113603
- 源文件：19811_2021_s2san-a-sentence-to-sentence-attention-network-for-sentiment-analysis-of-online-reviews.md
- 论文主类型：computational_artifact_benchmark
- 主导写作弧线：performance_gap_artifact_benchmark_generalize
- 置信度：0.82

## 文章级论证概况

- 核心问题：在在线评论情感分析中，如何设计一种句子级注意力机制，使每个句子按自身语义获得权重，同时避免HAN等模型将评论句子当作序列处理而引入不必要的顺序结构和计算复杂度。

- 制品与设计：提出S2SAN（sentence-to-sentence attention network）：词级用BI-GRU加词注意力得到句子向量，句子级用去除了位置编码的多头自注意力计算任意两个句子之间的关系权重，再通过全局平均池化得到文档表示，最后用softmax分类。

- 客观结果：在领域内情感分析中，S2SAN平均准确率0.788，优于HAN的0.776；在跨领域任务中12个子实验中7次最高，平均准确率0.646；在多领域任务中情感、领域、总体三项准确率均最高；将句子级注意力与CNN、RNN、LSTM等词编码器结合后准确率提升1.9%至8%，但MLP未提升；同时比HAN节省约25%训练时间。

- 核心贡献：作者声称首次用句子到句子注意力实现句子级注意力机制，避免句子位置信息并降低句子序列构建复杂度；面向在线评论在领域内、跨领域、多领域任务上取得更优结果；句子到句子注意力可作为独立框架提升CNN、RNN、LSTM等经典分类器。

- 整篇论证链：研究从在线评论数量激增和情感信息价值出发，指出现有注意力模型多聚焦词级注意力，而HAN等少数句子级注意力模型把句子当作序列，不符合评论中句子语义独立、关系多样的特点。作者据此提出以自注意力计算句子到句子关系的S2SAN。通过四组实验：领域内、跨领域、多领域以及不同词编码器兼容性实验，逐步验证模型在准确率、训练时间、跨域迁移和通用性上的优势，最后在讨论和结论中把这些结果上升为一种可复用的句子表示框架，并承认MLP失效、准确率提升有限等边界条件。

## 类型与写作弧线判定

- 论文主类型判定：论文核心是提出一个新的神经网络架构，并以多个真实评论数据集上的准确率、训练时间、混淆矩阵等benchmark结果作为主要证据；没有基于正式理论提出假设，也没有现场部署或人为干预实验，更接近计算制品+基准评价范式。

- 主导写作弧线判定：开头先构造性能/建模缺口：词级注意力忽略句子、HAN的句子级注意力错误假设句子序列关系；然后提出S2SAN制品；接着用领域内、跨领域、多领域和词编码器兼容性四组基准检验；最后将结论推广为适用于任意词编码器的句子级注意力框架。

## 研究开展程序

- study_or_phase_count：5

- 研究阶段总序列：研究先完成模型架构构建和复杂度分析，再用领域内任务检验基本有效性，用跨领域任务检验迁移能力，用多领域任务检验联合分类能力，最后用词编码器替换实验检验框架通用性。各阶段依次回答：能否设计出更合理的句子级注意力→是否比HAN更好→是否跨领域稳定→是否在多领域联合任务中仍有效→是否可搭配不同词编码器。

### studies_or_phases

#### 1. S2SAN架构构建与复杂度分析

- order：1

- name_cn：S2SAN架构构建与复杂度分析

- question_cn：如何构造一种不依赖句子位置与顺序的句子级注意力模型，并降低与HAN相比的句子编码复杂度？

- inputs_and_setting_cn：输入是既有HAN架构、BI-GRU-ATT词编码、Vaswani等提出的多头自注意力，以及在线评论中句子语义独立的经验观察；使用Yelp一条10句评论作为示例。

- designed_or_compared_object_cn：设计S2SAN的层次结构：词级BI-GRU+词注意力、句子级多头自注意力、全局平均池化、softmax分类器；与HAN的BI-GRU句子编码进行设计对比。

- baseline_control_or_counterfactual_cn：HAN作为主要对照；设计层面还比较了是否保留位置编码、是否使用序列模型编码句子。

##### objective_metrics

1. 模型复杂度O(n·d^2)+O(n^2·d) vs HAN O(n·d^2)+O(n·d^2)

2. 训练参数量

- analysis_method_cn：架构设计、公式推导、复杂度分析。

- main_result_cn：确立S2SAN架构，句子级复杂度为O(n^2·d)，由于句子数n远小于向量维度d，低于HAN的O(n·d^2)；移除位置编码以体现句子到句子关系。

- argumentative_role_cn：给出可验证的制品，并提前提供效率优势的理论依据。

- remaining_uncertainty_cn：设计是否真的能在准确率上超过HAN尚未验证。

- link_to_next_phase_cn：架构完成后自然进入实验评价，首先在领域内数据集上检验。

##### evidence_pointers

1. Section 3.1 Figure 1(a)(b)

2. Section 3.2.2 Equations (8)-(11)

3. Table 3

#### 2. 领域内情感分析实验

- order：2

- name_cn：领域内情感分析实验

- question_cn：在单一领域的在线评论上，S2SAN是否在准确率和训练时间上优于HAN及其他经典模型？

- inputs_and_setting_cn：四个数据集共120,000条评论：Amazon电子评论（英文）、Yelp餐饮评论（英文）、JD电子评论（中文）、Douban电影评论（中文）；5折交叉验证，训练测试8:2。

- designed_or_compared_object_cn：S2SAN与TextCNN、BI-GRU、BI-GRU-ATT、RCNN、Transformer、HAN比较。

- baseline_control_or_counterfactual_cn：所有基线统一嵌入维度400、优化器RMSProp、损失函数categorical cross-entropy、同一GPU环境。

##### objective_metrics

1. 分类准确率

2. 每epoch平均训练时间

- analysis_method_cn：5折交叉验证的均值与标准差比较；复杂度与训练时间对比。

- main_result_cn：S2SAN在Amazon、Yelp、Douban上最佳，JD上低于BI-GRU-ATT；平均准确率0.788，高于HAN的0.776；平均训练时间约322秒/epoch，约为HAN的75%。

- argumentative_role_cn：证明新架构在基本任务中有效，同时用训练时间支持效率主张。

- remaining_uncertainty_cn：领域内结果不能说明跨领域泛化能力，JD上的非最优也提示边界。

- link_to_next_phase_cn：为检验模型能否处理领域迁移，下一阶段做跨领域实验。

##### evidence_pointers

1. Table 2

2. Figure 5

3. Table 3

#### 3. 跨领域情感分析实验

- order：3

- name_cn：跨领域情感分析实验

- question_cn：在源领域训练、目标领域测试的跨领域设置中，S2SAN是否优于基线，并且句子级注意力是否比词级注意力更有利于迁移？

- inputs_and_setting_cn：Amazon四个领域：CDs and Vinyl、Cell Phones and Accessories、Clothing Shoes and Jewelry、Electronics；四个领域两两组对，正反各做一次，共12个源-目标子实验。

- designed_or_compared_object_cn：S2SAN与相同基线比较；进一步分析不同情感极性下的准确率和混淆情况。

- baseline_control_or_counterfactual_cn：12个源-目标方向互为反事实；同时对比BI-GRU与BI-GRU-ATT以观察词级注意力的作用。

##### objective_metrics

1. 跨领域准确率

2. 分情感极性准确率

3. 混淆矩阵

- analysis_method_cn：成对方向比较、平均准确率比较、混淆矩阵与分极性错误率分析。

- main_result_cn：S2SAN在12个子实验中7次最高，平均准确率0.646，优于其他模型；正极性较易、中性最难；句子级注意力模型HAN和S2SAN整体优于仅词注意力的BI-GRU-ATT。

- argumentative_role_cn：验证模型在跨领域迁移中仍有效，并把优势归因于句子级注意力而不是词级注意力。

- remaining_uncertainty_cn：在部分子实验中RCNN或Transformer更优，说明跨领域迁移受源-目标方向影响显著。

- link_to_next_phase_cn：跨领域只处理情感分类，多领域任务需要同时预测领域和情感，因此进入多领域实验。

##### evidence_pointers

1. Table 4

2. Figure 6

3. Figure 7

#### 4. 多领域情感分析实验

- order：4

- name_cn：多领域情感分析实验

- question_cn：在训练集包含多个领域且测试时不知道领域信息的多领域任务中，S2SAN能否同时优化情感分类和领域分类？

- inputs_and_setting_cn：将Amazon四个领域与Yelp的Hotels、Arts、Shops、Restaurant四个领域合并，构成8领域数据。

- designed_or_compared_object_cn：S2SAN与相同基线比较，重点看情感准确率、领域准确率和总体联合准确率。

- baseline_control_or_counterfactual_cn：HAN作为层次结构对照；BI-GRU/Bi-GRU-ATT用于观察词注意力在多领域中的效果。

##### objective_metrics

1. sentiment accuracy

2. domain accuracy

3. overall accuracy

- analysis_method_cn：三类准确率对比；分领域、分极性的准确率表和混淆矩阵。

- main_result_cn：S2SAN在三项准确率上均最优：情感0.788、领域0.829、总体0.650；负极性最好，中性最差；同平台内领域之间更容易混淆。

- argumentative_role_cn：说明模型在更复杂的联合分类任务中仍保持优势，但总体准确率提升很小，且领域准确率与BI-GRU持平。

- remaining_uncertainty_cn：S2SAN对领域分类的优化不明显；总体准确率仅略高于HAN。

- link_to_next_phase_cn：上述实验都使用BI-GRU作词编码器，下一阶段检验框架是否兼容其他词编码器。

##### evidence_pointers

1. Table 5

2. Figure 8

3. Figure 9

#### 5. 词编码器兼容性实验

- order：5

- name_cn：词编码器兼容性实验

- question_cn：句子到句子注意力作为独立框架，是否能够提升MLP、CNN、RNN、LSTM等不同词编码器的准确率？

- inputs_and_setting_cn：Amazon数据集；选择MLP、CNN、RNN、LSTM作为词编码器，分别记为S2S-MLP、S2S-CNN、S2S-RNN、S2S-LSTM，与原始模型比较。

- designed_or_compared_object_cn：每个基础模型与其加上句子到句子注意力的变体比较，重点是最高准确率和收敛速度。

- baseline_control_or_counterfactual_cn：原始MLP/CNN/RNN/LSTM作为对照，是否加入S2S是唯一差异。

##### objective_metrics

1. 多轮训练中的最高测试准确率

2. 收敛速度/早期epoch表现

- analysis_method_cn：逐epoch准确率曲线比较，报告各模型最高准确率。

- main_result_cn：除MLP外，S2S-CNN、S2S-RNN、S2S-LSTM的最高准确率均高于基础模型，并在训练早期更快收敛；CNN从0.754到0.779，LSTM从0.733到0.792，RNN从0.665到0.735。

- argumentative_role_cn：证明句子到句子注意力是相对通用的框架，同时暴露MLP这一边界条件。

- remaining_uncertainty_cn：只在单一数据集上测试，未做超参数搜索；MLP为何不提升未深入解释。

- link_to_next_phase_cn：该边界结果进入讨论和结论，作为局限与未来方向。

##### evidence_pointers

1. Figure 10

2. Section 4.4.4

## 各部分修辞架构

### abstract_moves

1. CONTEXT: 在线评论情感分析中注意力模型现状

2. LIMITATION: 现有关注词级注意力、忽略句子重要性

3. LIMITATION: 已有句子级注意力沿用词级方法，带来序列结构和复杂度

4. DESIGN_FEATURE: 提出S2SAN，使用多头自注意力

5. RESULT: 多领域实验优于SOTA

6. CONTRIBUTION: 经典分类器加入句子到句子注意力后准确率提升

### introduction_moves

1. CONTEXT: 电商发展导致在线评论激增

2. PRACTICAL_STAKES: 评论对决策、商家改进、个性化推荐有价值

3. RQ_OR_OBJECTIVE: 需要能将评论情感信息转化为易理解形式的情感分析模型

4. PRIOR_KNOWLEDGE: 传统方法和深度学习方法的演进

5. THEORY_INTRO: 注意力机制模仿人类视觉注意力

6. MECHANISM: 注意力机制从大量输入中提取重要信息

7. LIMITATION: 现有注意力模型聚焦词级注意力

8. PHENOMENON: 评论中每个句子语义独立，应单独计算权重

9. LIMITATION: HAN虽考虑句子级注意力，但沿用词级处理方式

10. MECHANISM: 评论句子间不存在明显序列关系，用序列模型增加复杂度

11. DESIGN_FEATURE: 引入句子到句子自注意力结构

12. RQ_OR_OBJECTIVE: 提出三个研究目标

13. CONTRIBUTION: 列出三点贡献

14. STUDY_OVERVIEW: 给出全文结构

### theory_and_knowledge_moves

1. PRIOR_KNOWLEDGE: 领域特定情感分类、跨领域和多领域情感分析相关工作

2. PRIOR_KNOWLEDGE: 无监督情感分析方法的优势

3. PRIOR_KNOWLEDGE: 注意力机制在NLP中的发展脉络

4. PRIOR_KNOWLEDGE: HAN、Transformer、自注意力等关键架构

5. LIMITATION: 大多数注意力研究只计算词级注意力，句子级注意力少

6. GAP: 需要计算句子级注意力权重

### artifact_design_moves

1. MECHANISM: 评论句子间不是简单序列关系，而是平行、对抗、因果等关系

2. REQUIREMENT: 句子编码应忽略位置信息，关注句子间关系

3. DESIGN_FEATURE: 提出层次框架，词级到句子级、句子级到文档级

4. DESIGN_FEATURE: 词编码使用BI-GRU+词注意力

5. DESIGN_FEATURE: 句子编码使用多头自注意力并去掉位置编码

6. METHOD_JUSTIFICATION: BERT对短文本长度敏感，评论句子短，因此使用GRU

7. DESIGN_FEATURE: 文档表示通过全局平均池化得到

8. DESIGN_FEATURE: 最后接softmax分类器

### evaluation_moves

1. STUDY_OVERVIEW: 四组实验验证准确率和兼容性

2. BENCHMARK_OR_CONTRAST: 选择经典基线并说明HAN是层次对照

3. METHOD_JUSTIFICATION: 统一实验环境、优化器、嵌入维度

4. RESULT: 领域内S2SAN平均准确率最高

5. RESULT: 训练时间与复杂度低于HAN

6. RESULT: 跨领域S2SAN在7/12子实验最高

7. MECHANISM: 句子级注意力有助于跨领域信息提取

8. RESULT: 多领域S2SAN在三个指标上均最优

9. RESULT: S2S变体提升CNN/RNN/LSTM但非MLP

### discussion_and_contribution_moves

1. RESULT: 重述四组实验的结论

2. CONTRIBUTION: 句子到句子结构学习多子空间句子语义关系、降低训练时间

3. BOUNDARY_CONDITION: 准确率提升有限、跨领域和多领域准确率不高、MLP无优化

4. CONTRIBUTION: 填补句子语义独立而非序列的研究缺口

5. CONTRIBUTION: 理论意义是句子表示新视角、低复杂度、更多句子依赖关系

6. PRACTICAL_STAKES: 可快速分析大规模评论，帮助商家和平台理解用户态度

7. LIMITATION_AND_FUTURE: 未来包括aspect级、更长文本、预训练模型结合

## 理论/知识到设计的翻译

### 知识/理论基础

1. 注意力机制是对人类视觉注意力的模拟

2. 层次文本表示：文档由句子构成、句子由词构成

3. HAN使用BI-GRU-ATT同时编码词和句子

4. Vaswani等的Transformer多头自注意力

5. BOW思想：忽略词序、关注词袋关系

6. BERT对短文本长度敏感这一经验观察

- 理论—设计耦合：partial

- 耦合判定理由：注意力机制和层次文本表示知识确实影响了问题定位和设计方向，但关键技术选择主要来自Transformer工程经验和作者对评论语料的观察，没有从正式理论推导出可检验假设，也没有用理论解释所有设计参数。

- 理论到设计翻译链：注意力机制能表示实体重要性 → 句子也应作为实体获得注意力权重 → 现有HAN把句子当序列处理，与评论中句子语义独立矛盾 → 设计应忽略句子位置、直接计算句子两两关系 → 使用多头自注意力构造句子到句子注意力 → 通过领域内、跨领域、多领域和词编码器替换实验检验该设计。

### mapping_table

#### 1. 1

- theory_or_knowledge_claim_cn：评论中句子语义独立，句子间不存在严格顺序关系，而存在平行、因果、对抗等多种关系。

- mechanism_cn：用BI-GRU等序列模型编码句子会强加顺序依赖，增加无效复杂度和训练时间。

- design_requirement_cn：句子级编码应不依赖句子位置信息。

- artifact_choice_cn：移除位置编码，用自注意力直接计算任意两个句子间的关系矩阵。

- evaluated_contrast_cn：HAN的BI-GRU句子编码 vs S2SAN的多头自注意力句子编码。

- objective_result_cn：领域内平均准确率0.788 vs 0.776；每epoch平均训练时间约322秒 vs 427秒。

##### evidence_pointers

1. Section 3.1 Figure 2

2. Table 2

3. Table 3

4. Figure 5

#### 2. 2

- theory_or_knowledge_claim_cn：自注意力机制可以表示序列中任何两个实体之间的关系。

- mechanism_cn：多头结构让模型从多个子空间捕获句子间语义关系，增强文档表示。

- design_requirement_cn：句子到句子注意力应采用多头自注意力并保留全局池化以得到定长文档向量。

- artifact_choice_cn：MultiHead(Q,K,V) + 全局平均池化 + softmax。

- evaluated_contrast_cn：与HAN的句子级注意力比较；在跨领域和多领域任务中比较。

- objective_result_cn：跨领域平均0.646；多领域情感/领域/总体准确率0.788/0.829/0.650，均优于HAN。

##### evidence_pointers

1. Section 3.2.2 Equations (8)-(11)

2. Table 4

3. Table 5

#### 3. 3

- theory_or_knowledge_claim_cn：注意力机制可以给不同实体分配不同重要性权重。

- mechanism_cn：词级注意力突出关键词，句子级注意力突出关键句子。

- design_requirement_cn：层次结构中词级和句子级应分别计算注意力。

- artifact_choice_cn：BI-GRU+词注意力生成句子向量，再进入句子到句子注意力。

- evaluated_contrast_cn：拥有句子级注意力的HAN/S2SAN vs 仅词注意力的BI-GRU-ATT。

- objective_result_cn：在跨领域任务中，HAN和S2SAN整体优于BI-GRU-ATT，说明句子级注意力有额外收益。

##### evidence_pointers

1. Section 3.2.1 Equations (5)-(7)

2. Table 4

#### 4. 4

- theory_or_knowledge_claim_cn：预训练模型BERT对短文本敏感，评论句子平均长度明显小于50词。

- mechanism_cn：短文本输入可能导致BERT准确率下降，而评论句子较短，不适合直接套用BERT。

- design_requirement_cn：词编码器应选择对短句稳健的模型。

- artifact_choice_cn：采用GRU/BI-GRU作为词编码器。

- evaluated_contrast_cn：没有直接对比GRU与BERT，而是用GRU作为架构默认词编码器。

- objective_result_cn：以BI-GRU为词编码器的S2SAN在领域内、跨领域、多领域任务中取得最佳或接近最佳结果。

##### evidence_pointers

1. Section 3.2.1

2. Table 2

3. Table 4

4. Table 5

#### 5. 5

- theory_or_knowledge_claim_cn：句子到句子注意力应独立于底层词编码器。

- mechanism_cn：一旦得到句子向量，句子到句子注意力只需处理句子向量序列，不关心向量由哪种词编码器产生。

- design_requirement_cn：框架应能插入不同词编码器。

- artifact_choice_cn：构造S2S-MLP、S2S-CNN、S2S-RNN、S2S-LSTM。

- evaluated_contrast_cn：各基础模型 vs 加入句子到句子注意力后的变体。

- objective_result_cn：CNN、RNN、LSTM提升1.9%-8%，MLP未提升。

##### evidence_pointers

1. Section 4.4.4

2. Figure 10

## 评价逻辑

### evaluation_modes

1. 领域内情感分类基准对比

2. 跨领域迁移基准对比

3. 多领域联合分类基准对比

4. 词编码器替换实验

5. 模型复杂度与训练时间对比

- why_these_evaluations_cn：领域内实验检验基本分类能力；跨领域实验检验模型泛化而非记忆领域特征；多领域实验检验联合预测领域和情感的复杂任务；词编码器替换实验检验句子到句子注意力作为独立框架的通用性；复杂度与训练时间对比则支持效率主张，防止贡献只停留在准确率上。

- benchmark_and_contrast_chain_cn：先以HAN为主要对照，因为HAN是唯一使用句子级注意力的层次模型；再用与传统flat模型对比显示整体竞争力；加入跨领域、多领域后，HAN和S2SAN被反复对比，逐步排除词级注意力解释，突出句子到句子注意力的贡献；最后用同一词编码器加不加S2S的对照，建立直接消融式比较。

### claim_evidence_ledger

#### 1. S2SAN在领域内、跨领域、多领域任务上取得比基线更高的平均准确率。

- claim_type：技术主张

- claim_cn：S2SAN在领域内、跨领域、多领域任务上取得比基线更高的平均准确率。

- evidence_cn：Table 2平均0.788最高；Table 4平均0.646最高；Table 5三项指标均最高。

- verified：是

- note_cn：差异幅度较小，且未提供统计显著性检验。

#### 2. 用句子到句子注意力替换HAN的句子序列编码带来准确率提升和训练时间下降。

- claim_type：制品主张

- claim_cn：用句子到句子注意力替换HAN的句子序列编码带来准确率提升和训练时间下降。

- evidence_cn：Table 2、Table 3显示准确率提升1.2%，训练时间约为HAN的75%。

- verified：是

- note_cn：准确率提升并非每个数据集都成立，JD数据集上S2SAN低于BI-GRU-ATT。

#### 3. 句子级注意力比词级注意力更有助于跨领域情感信息提取。

- claim_type：机制主张

- claim_cn：句子级注意力比词级注意力更有助于跨领域情感信息提取。

- evidence_cn：跨领域实验中BI-GRU-ATT平均低于BI-GRU，而HAN/S2SAN更高。

- verified：是

- note_cn：这是观察性解释，未直接操纵句子级注意力进行严格消融。

#### 4. 句子到句子注意力对CNN、RNN、LSTM有效，但对MLP无优化。

- claim_type：边界主张

- claim_cn：句子到句子注意力对CNN、RNN、LSTM有效，但对MLP无优化。

- evidence_cn：Figure 10显示除MLP外其他S2S变体最高准确率均超过基础模型。

- verified：是

- note_cn：仅在一个数据集上验证，MLP失败原因未解释。

#### 5. 句子到句子注意力是独立于词编码器的句子表示框架。

- claim_type：可复用设计知识

- claim_cn：句子到句子注意力是独立于词编码器的句子表示框架。

- evidence_cn：S2S-CNN、S2S-RNN、S2S-LSTM均有效。

- verified：是

- note_cn：没有给出超参数选择和不同数据规模下的稳定性。

#### 6. 提供句子表示新视角，降低复杂度并学习更多句子依赖关系。

- claim_type：理论贡献

- claim_cn：提供句子表示新视角，降低复杂度并学习更多句子依赖关系。

- evidence_cn：模型复杂度分析和多场景实验。

- verified：否

- note_cn：这句话更多是讨论中的定位，未形成可复用的正式理论命题。

- internal_validity_strategy_cn：使用5折交叉验证、统一嵌入维度和优化器、相同GPU硬件、同一框架实现基线与S2SAN；跨领域实验用源-目标方向互换形成反事实；词编码器兼容实验中，基础模型与S2S变体只差是否加入句子到句子注意力。

- external_validity_strategy_cn：使用两种语言（英文、中文）、四个平台（Amazon、Yelp、JD、Douban）、多种领域（电子产品、餐饮、电影、酒店、艺术、商店等）以及三种任务设置；通过跨领域和多领域实验扩大结论覆盖范围。

- what_is_not_actually_tested_cn：没有进行统计显著性检验；没有对注意力头数、维度、dropout等超参数做敏感性分析；没有真正消融位置编码是否存在；没有检验BERT/ELMo等预训练词编码器；也没有在更长文本、新闻或科学文献上验证；MLP失效的机制没有解释。

## 贡献闭环

- technical_claim_cn：S2SAN在多个在线评论情感分析基准上优于当前state-of-the-art模型。

- artifact_claim_cn：句子到句子注意力（而非序列型句子编码）是带来准确率和训练时间改进的可识别设计部分。

- mechanism_claim_cn：评论句子语义独立且关系多样，自注意力能够在多个子空间捕获句子间依赖，从而得到更好的文档表示；跨领域任务中句子级注意力比词级注意力更有效。

- boundary_claim_cn：适用于在线评论类短文本；对CNN/RNN/LSTM词编码器有效但对MLP无效；跨领域和多领域准确率整体仍不高，中性情感最难。

- reusable_design_knowledge_cn：句子到句子注意力可以作为独立于词编码器的句子表示框架，使用时可以去除位置编码，并结合多词编码器提升性能。

- theoretical_contribution_cn：提出一种新的句子表示视角：句子的语义权重不应依赖位置顺序而应依赖句子间语义关系；这一视角扩展了注意力机制在层次文本建模中的应用。

- how_discussion_closes_intro_gap_cn：讨论和结论明确指出“句子语义是个体性而非顺序性”这一引言缺口，并把S2SAN描述为填补该缺口的模型；同时用准确率、训练时间和兼容性实验回应引言中的三个目标，再以理论/实践意义收束。

- overclaim_or_unsupported_leaps_cn：“首次使用句子到句子注意力”这类首创性表述缺少系统性文献证据；只凭平均准确率提升0.8%-2.1%就宣称SOTA，未做显著性检验；把多场景结果解释为“句子级注意力有效”但未隔离句子级注意力的贡献；MLP作为反例被列为局限，却未深入解释为何失效；训练时间比较未说明early stopping标准是否完全一致。

## 句级写作动作图谱

### 1. Abstract P1 S1

- order：1

- section：Abstract

- locator：Abstract P1 S1

- move_code：LIMITATION

- paraphrase_cn：现有基于注意力的深度情感分析方法多关注词，把整篇评论当作词序列。

- rhetorical_function_cn：开头直接限定问题域，指出已有方法的基本假设。

- depends_on_cn：无需前置内容。

- sets_up_cn：为引出句子重要性被忽略做铺垫。

- evidence_pointer：Abstract

### 2. Abstract P1 S2

- order：2

- section：Abstract

- locator：Abstract P1 S2

- move_code：LIMITATION

- paraphrase_cn：这种做法忽略每个句子对整个文本重要性的差异。

- rhetorical_function_cn：把上句的词级焦点转化为缺陷。

- depends_on_cn：依赖上句对现有方法的概括。

- sets_up_cn：引出需要句子级注意力。

- evidence_pointer：Abstract

### 3. Abstract P1 S3-S4

- order：3

- section：Abstract

- locator：Abstract P1 S3-S4

- move_code：LIMITATION

- paraphrase_cn：已有句子级注意力工作只是把词级注意力方法照搬到句子编码，导致不必要的序列结构和复杂度。

- rhetorical_function_cn：把句子级注意力已有尝试也标记为不充分，形成双重缺口。

- depends_on_cn：承接前两句。

- sets_up_cn：为提出替代方案提供理由。

- evidence_pointer：Abstract

### 4. Abstract P1 S5

- order：4

- section：Abstract

- locator：Abstract P1 S5

- move_code：DESIGN_FEATURE

- paraphrase_cn：因此提出使用多头自注意力的句子到句子注意力网络S2SAN。

- rhetorical_function_cn：在摘要中点出核心制品。

- depends_on_cn：依赖前两句的缺口。

- sets_up_cn：为后面报告实验和贡献做预备。

- evidence_pointer：Abstract

### 5. Abstract P1 S6-S7

- order：5

- section：Abstract

- locator：Abstract P1 S6-S7

- move_code：RESULT

- paraphrase_cn：在多个真实数据集上进行了领域内、跨领域和多领域实验，结果显示S2SAN优于其他模型。

- rhetorical_function_cn：给出最直接的证据概括。

- depends_on_cn：依赖制品提出。

- sets_up_cn：引出贡献句。

- evidence_pointer：Abstract

### 6. Abstract P2

- order：6

- section：Abstract

- locator：Abstract P2

- move_code：CONTRIBUTION

- paraphrase_cn：经典模型如CNN、RNN、LSTM重构为包含句子到句子注意力后准确率提升。

- rhetorical_function_cn：增加贡献点：框架通用性。

- depends_on_cn：依赖实验结果。

- sets_up_cn：吸引读者关注可复用性。

- evidence_pointer：Abstract

### 7. Introduction P1 S1-S2

- order：7

- section：Introduction

- locator：Introduction P1 S1-S2

- move_code：CONTEXT

- paraphrase_cn：电商发展改变了商家与消费者之间的商业模式，在线评论数量激增。

- rhetorical_function_cn：建立研究的宏观背景。

- depends_on_cn：无需前置。

- sets_up_cn：为说明评论价值做铺垫。

- evidence_pointer：Introduction P1

### 8. Introduction P1 S3-S5

- order：8

- section：Introduction

- locator：Introduction P1 S3-S5

- move_code：PRACTICAL_STAKES

- paraphrase_cn：Amazon和京东等平台使消费者分享评价，评论中包含正负中性的丰富情感信息。

- rhetorical_function_cn：说明研究对象和现实数据来源。

- depends_on_cn：依赖电商背景。

- sets_up_cn：为情感分析任务的价值作准备。

- evidence_pointer：Introduction P1

### 9. Introduction P1 S6-S10

- order：9

- section：Introduction

- locator：Introduction P1 S6-S10

- move_code：PRACTICAL_STAKES

- paraphrase_cn：电子口碑影响决策，评论也帮助商家改进产品服务，并为个性化推荐提供参考。

- rhetorical_function_cn：把评论价值具体化到决策、商家和推荐三个层面。

- depends_on_cn：依赖评论数据存在的前提。

- sets_up_cn：解释为什么要做情感分析。

- evidence_pointer：Introduction P1

### 10. Introduction P1 S11-S12

- order：10

- section：Introduction

- locator：Introduction P1 S11-S12

- move_code：PRACTICAL_STAKES

- paraphrase_cn：在线评论数量巨大，用户和商家难以全面提取和分析公众意见。

- rhetorical_function_cn：引入现实痛点，说明自动情感分析的必要性。

- depends_on_cn：依赖评论价值论述。

- sets_up_cn：引出需要情感分析模型。

- evidence_pointer：Introduction P1

### 11. Introduction P2 S1-S4

- order：11

- section：Introduction

- locator：Introduction P2 S1-S4

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：传统情感分析包括标注语料、情感词典和领域分类器，为研究打下基础。

- rhetorical_function_cn：简要梳理已有方法谱系。

- depends_on_cn：与评论情感分析问题直接相关。

- sets_up_cn：为区分深度学习方法的优势提供对照。

- evidence_pointer：Introduction P2

### 12. Introduction P2 S5-S7

- order：12

- section：Introduction

- locator：Introduction P2 S5-S7

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：深度学习和语言模型方法成为主流，在文本表示和深层语义理解上优于传统机器学习。

- rhetorical_function_cn：说明技术演进的当前位置。

- depends_on_cn：依赖传统方法介绍。

- sets_up_cn：为注意力机制的引入做铺垫。

- evidence_pointer：Introduction P2

### 13. Introduction P3 S1-S3

- order：13

- section：Introduction

- locator：Introduction P3 S1-S3

- move_code：THEORY_INTRO

- paraphrase_cn：注意力机制是对人类视觉注意力的模拟，人类会忽略无关信息并分配更多注意力给重要信息。

- rhetorical_function_cn：引入理论基础，强调注意力机制的合理性。

- depends_on_cn：承接深度学习方法。

- sets_up_cn：为句子级注意力观点提供依据。

- evidence_pointer：Introduction P3

### 14. Introduction P3 S4-S6

- order：14

- section：Introduction

- locator：Introduction P3 S4-S6

- move_code：MECHANISM

- paraphrase_cn：注意力机制通过从大量输入中提取有用信息并分配更大权重来提升模型鲁棒性。

- rhetorical_function_cn：解释注意力为什么有效。

- depends_on_cn：依赖视觉注意力类比。

- sets_up_cn：说明任何实体序列都可用注意力，包括句子。

- evidence_pointer：Introduction P3

### 15. Introduction P4 S1-S3

- order：15

- section：Introduction

- locator：Introduction P4 S1-S3

- move_code：LIMITATION

- paraphrase_cn：现有注意力模型基本以词为单位，把整个文本表示为词序列。

- rhetorical_function_cn：指出主流方法的主要假设。

- depends_on_cn：依赖注意力机制介绍。

- sets_up_cn：为提出句子重要性差异做反衬。

- evidence_pointer：Introduction P4

### 16. Introduction P4 S4-S5

- order：16

- section：Introduction

- locator：Introduction P4 S4-S5

- move_code：PHENOMENON

- paraphrase_cn：评论中每个句子表达独特语义，因此不同句子的注意力权重应分别计算。

- rhetorical_function_cn：提出作者对评论语料的经验观察和核心主张。

- depends_on_cn：依赖上一句的缺陷陈述。

- sets_up_cn：引出HAN的不足。

- evidence_pointer：Introduction P4

### 17. Introduction P4 S6-S7

- order：17

- section：Introduction

- locator：Introduction P4 S6-S7

- move_code：LIMITATION

- paraphrase_cn：HAN虽考虑了句子级注意力，但大多数研究用与词级相同的方式计算句子级注意力。

- rhetorical_function_cn：指出已有句子级注意力尝试的不足。

- depends_on_cn：依赖句子重要性主张。

- sets_up_cn：为词级方法不能直接移植作论证。

- evidence_pointer：Introduction P4

### 18. Introduction P4 S8-S9

- order：18

- section：Introduction

- locator：Introduction P4 S8-S9

- move_code：MECHANISM

- paraphrase_cn：评论句子之间没有明显序列结构关系，用序列模型表示句子会带来不必要的复杂度。

- rhetorical_function_cn：从数据结构上解释为什么现有方法不适合评论。

- depends_on_cn：依赖HAN不足。

- sets_up_cn：为使用自注意力替代序列编码提供理由。

- evidence_pointer：Introduction P4

### 19. Introduction P4 S10-S11

- order：19

- section：Introduction

- locator：Introduction P4 S10-S11

- move_code：DESIGN_FEATURE

- paraphrase_cn：引入句子到句子结构，利用自注意力计算任意两个句子的关系权重。

- rhetorical_function_cn：给出解决方案的核心。

- depends_on_cn：依赖上句的机理分析。

- sets_up_cn：引出三个研究目标。

- evidence_pointer：Introduction P4

### 20. Introduction P5 S1-S5

- order：20

- section：Introduction

- locator：Introduction P5 S1-S5

- move_code：RQ_OR_OBJECTIVE

- paraphrase_cn：研究目标有三个：设计S2SAN并选择合适词/句编码器；验证其在领域内、跨领域、多领域任务中优于HAN；验证其与不同词编码器兼容。

- rhetorical_function_cn：明确研究问题并预告实验方向。

- depends_on_cn：依赖前面的设计主张。

- sets_up_cn：直接对应后面四组实验。

- evidence_pointer：Introduction P5

### 21. Introduction P6

- order：21

- section：Introduction

- locator：Introduction P6

- move_code：CONTRIBUTION

- paraphrase_cn：贡献包括首次用句子到句子注意力实现句子级注意力、相比HAN提高准确率并降低训练时间、提升经典分类器准确率。

- rhetorical_function_cn：以列表形式声明理论、实验和通用性贡献。

- depends_on_cn：依赖研究目标。

- sets_up_cn：为全文评价标准定调。

- evidence_pointer：Introduction P6

### 22. Introduction P7

- order：22

- section：Introduction

- locator：Introduction P7

- move_code：STUDY_OVERVIEW

- paraphrase_cn：说明后续章节安排：相关工作、模型、实验、讨论、结论。

- rhetorical_function_cn：给出全文路线图。

- depends_on_cn：贡献声明后。

- sets_up_cn：引导读者按结构阅读。

- evidence_pointer：Introduction P7

### 23. Section 2.1 P1-P4

- order：23

- section：Related Works

- locator：Section 2.1 P1-P4

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：领域特定情感分类、跨领域和多领域情感分类已有众多方法，包括机器学习、词典适应、注意力网络和领域适应模型。

- rhetorical_function_cn：建立文献基础，展示问题已被多角度研究。

- depends_on_cn：引言已确定研究对象。

- sets_up_cn：为后续注意力机制综述和缺口陈述做铺垫。

- evidence_pointer：Section 2.1

### 24. Section 2.2 P1-P4

- order：24

- section：Related Works

- locator：Section 2.2 P1-P4

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：注意力机制从图像识别扩展到语音、视频、机器翻译、阅读理解、文档分类等任务。

- rhetorical_function_cn：说明注意力机制在NLP中的广泛适用性。

- depends_on_cn：领域情感分析文献。

- sets_up_cn：引出HAN和Transformer作为直接相关基础。

- evidence_pointer：Section 2.2

### 25. Section 2.2 P5-P6

- order：25

- section：Related Works

- locator：Section 2.2 P5-P6

- move_code：GAP

- paraphrase_cn：注意力研究大多聚焦词的注意力权重，很少有研究计算句子的注意力权重。

- rhetorical_function_cn：指出文献缺口。

- depends_on_cn：依赖注意力综述。

- sets_up_cn：为论文的句子级注意力工作提供空间。

- evidence_pointer：Section 2.2末尾

### 26. Section 3.1 P1-P2

- order：26

- section：Proposed Approach

- locator：Section 3.1 P1-P2

- move_code：MECHANISM

- paraphrase_cn：文档中句子间没有明显序列关系，尤其口语化在线评论中，BI-GRU编码句子会强加无效顺序并增加复杂度。

- rhetorical_function_cn：从数据特性解释为什么不能照搬HAN。

- depends_on_cn：依赖相关工作中HAN与自注意力介绍。

- sets_up_cn：为提出自注意力句子编码提供机理依据。

- evidence_pointer：Section 3.1, Figure 2

### 27. Section 3.1 P3

- order：27

- section：Proposed Approach

- locator：Section 3.1 P3

- move_code：REQUIREMENT

- paraphrase_cn：受到BOW启发，决定忽略句子位置信息，重点考虑句子在文档向量空间中的关系。

- rhetorical_function_cn：把经验观察转化为设计约束。

- depends_on_cn：依赖上一段的机理分析。

- sets_up_cn：引出层次注意力框架。

- evidence_pointer：Section 3.1 P3

### 28. Section 3.1 P4

- order：28

- section：Proposed Approach

- locator：Section 3.1 P4

- move_code：DESIGN_FEATURE

- paraphrase_cn：提出层次注意力框架：词到句子、句子到文档，句子向量由自注意力而不是BI-GRU-ATT计算，最后用全局平均池化。

- rhetorical_function_cn：正式给出制品框架。

- depends_on_cn：依赖设计约束。

- sets_up_cn：为下一节具体网络结构作总述。

- evidence_pointer：Section 3.1 P4, Figure 1(b)

### 29. Section 3.2 P1

- order：29

- section：Proposed Approach

- locator：Section 3.2 P1

- move_code：DESIGN_FEATURE

- paraphrase_cn：S2SAN用BI-GRU-ATT编码词得到句子表示，用多头自注意力编码句子得到文档表示。

- rhetorical_function_cn：描述默认配置。

- depends_on_cn：依赖框架总述。

- sets_up_cn：为词编码和句子编码分别说明。

- evidence_pointer：Section 3.2 P1

### 30. Section 3.2.1 P1

- order：30

- section：Proposed Approach

- locator：Section 3.2.1 P1

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：BERT等预训练模型对长度敏感，短文本准确率低，而评论句子平均长度远低于50，因此选择更稳健的GRU。

- rhetorical_function_cn：为词编码器选择提供依据。

- depends_on_cn：依赖文档表示框架。

- sets_up_cn：引出BI-GRU词编码细节。

- evidence_pointer：Section 3.2.1 P1

### 31. Section 3.2.1 Equations (1)-(4)

- order：31

- section：Proposed Approach

- locator：Section 3.2.1 Equations (1)-(4)

- move_code：DESIGN_FEATURE

- paraphrase_cn：将评论表示为句子-词层次结构，词向量经过前后向GRU得到隐状态表示。

- rhetorical_function_cn：用公式固化词编码过程。

- depends_on_cn：依赖GRU选择。

- sets_up_cn：为词注意力层提供输入。

- evidence_pointer：Section 3.2.1 Equations (1)-(4)

### 32. Section 3.2.1 Equations (5)-(7)

- order：32

- section：Proposed Approach

- locator：Section 3.2.1 Equations (5)-(7)

- move_code：DESIGN_FEATURE

- paraphrase_cn：通过词注意力层计算每个词的权重，加权求和得到句子向量。

- rhetorical_function_cn：描述句子表示生成方式。

- depends_on_cn：依赖BI-GRU输出。

- sets_up_cn：为句子到句子注意力提供输入向量。

- evidence_pointer：Section 3.2.1 Equations (5)-(7)

### 33. Section 3.2.2 P1

- order：33

- section：Proposed Approach

- locator：Section 3.2.2 P1

- move_code：DESIGN_FEATURE

- paraphrase_cn：文档表示采用Vaswani等提出的多头自注意力，与RNN相比更擅长解决长距离依赖。

- rhetorical_function_cn：引入关键句子编码器。

- depends_on_cn：依赖句子向量生成。

- sets_up_cn：解释多头子空间的作用。

- evidence_pointer：Section 3.2.2 P1

### 34. Section 3.2.2 P1

- order：34

- section：Proposed Approach

- locator：Section 3.2.2 P1

- move_code：MECHANISM

- paraphrase_cn：每个注意力头是一个子空间，拼接多头输出可以使文档表示从不同子空间学习语义信息。

- rhetorical_function_cn：说明多头设计的机制收益。

- depends_on_cn：依赖多头自注意力引入。

- sets_up_cn：为去掉位置编码的设计做支撑。

- evidence_pointer：Section 3.2.2 P1

### 35. Section 3.2.2 P1-S2

- order：35

- section：Proposed Approach

- locator：Section 3.2.2 P1-S2

- move_code：DESIGN_FEATURE

- paraphrase_cn：与原始Transformer相比，移除了位置嵌入层，使模型更贴合句子到句子注意力。

- rhetorical_function_cn：突出设计差异点。

- depends_on_cn：依赖多头自注意力说明。

- sets_up_cn：为后面实验中的HAN对照提供设计差异依据。

- evidence_pointer：Section 3.2.2 P1

### 36. Section 3.2.2 Equations (8)-(11)

- order：36

- section：Proposed Approach

- locator：Section 3.2.2 Equations (8)-(11)

- move_code：DESIGN_FEATURE

- paraphrase_cn：文档表示由多头注意力输出经全局平均池化得到，再输入softmax分类。

- rhetorical_function_cn：完成从句子到文档再到分类的建模。

- depends_on_cn：依赖多头自注意力公式。

- sets_up_cn：为实验部分提供可运行模型。

- evidence_pointer：Section 3.2.2 Equations (8)-(11)

### 37. Section 4 P1

- order：37

- section：Experiments

- locator：Section 4 P1

- move_code：STUDY_OVERVIEW

- paraphrase_cn：进行四组实验验证S2SAN在领域内、跨领域、多领域中的准确率以及与主流词编码器的兼容性。

- rhetorical_function_cn：预告实验结构。

- depends_on_cn：依赖模型构建。

- sets_up_cn：为后续小节顺序提供路线图。

- evidence_pointer：Section 4 P1

### 38. Section 4.1

- order：38

- section：Experiments

- locator：Section 4.1

- move_code：BENCHMARK_OR_CONTRAST

- paraphrase_cn：选择HAN、TextCNN、BI-GRU、BI-GRU-ATT、RCNN、Transformer作为基线，其中HAN是层次模型，其余是flat结构。

- rhetorical_function_cn：建立评价参照系。

- depends_on_cn：依赖引言中的研究目标。

- sets_up_cn：为实验结果表格设定比较对象。

- evidence_pointer：Section 4.1

### 39. Section 4.2

- order：39

- section：Experiments

- locator：Section 4.2

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：实验统一在GPU服务器上运行，使用TensorFlow和Keras，5折交叉验证，嵌入维度400，RMSProp优化器和categorical cross-entropy损失。

- rhetorical_function_cn：说明实验条件受控，提升可比性。

- depends_on_cn：依赖基线选择。

- sets_up_cn：为结果可信度提供方法保障。

- evidence_pointer：Section 4.2

### 40. Section 4.4.1 P2-P3

- order：40

- section：Experiments

- locator：Section 4.4.1 P2-P3

- move_code：RESULT

- paraphrase_cn：S2SAN在四个领域数据集中除JD外均取得最高准确率，平均准确率0.788，高于HAN的0.776。

- rhetorical_function_cn：报告领域内实验主要结果。

- depends_on_cn：依赖实验设置。

- sets_up_cn：为训练时间和复杂度分析提供对比基础。

- evidence_pointer：Table 2

### 41. Section 4.4.1 P4-P5

- order：41

- section：Experiments

- locator：Section 4.4.1 P4-P5

- move_code：RESULT

- paraphrase_cn：S2SAN和HAN都比非层次模型训练时间短，且S2SAN只消耗HAN约75%的训练时间；复杂度分析显示句子级S2SAN为O(n^2d)，低于HAN的O(nd^2)。

- rhetorical_function_cn：用第二指标支持效率主张。

- depends_on_cn：依赖准确率结果。

- sets_up_cn：为贡献中“降低训练时间”提供证据。

- evidence_pointer：Figure 5, Table 3

### 42. Section 4.4.2 P2-S3

- order：42

- section：Experiments

- locator：Section 4.4.2 P2-S3

- move_code：RESULT

- paraphrase_cn：在12个跨领域子实验中，S2SAN在7个任务上最高，平均准确率0.646。

- rhetorical_function_cn：报告跨领域主要结果。

- depends_on_cn：依赖跨领域设计。

- sets_up_cn：为句子级注意力在跨域中的机制解释提供依据。

- evidence_pointer：Table 4

### 43. Section 4.4.2 P3

- order：43

- section：Experiments

- locator：Section 4.4.2 P3

- move_code：MECHANISM

- paraphrase_cn：BI-GRU-ATT在跨领域中反而低于BI-GRU，而HAN和S2SAN更好，说明句子级注意力有助于提取跨领域信息。

- rhetorical_function_cn：把跨领域结果上升为机制解释。

- depends_on_cn：依赖跨领域准确率表。

- sets_up_cn：为讨论部分的核心贡献提供论证。

- evidence_pointer：Section 4.4.2 P3

### 44. Section 4.4.2 P4

- order：44

- section：Experiments

- locator：Section 4.4.2 P4

- move_code：RESULT

- paraphrase_cn：分极性分析显示正极性准确率最高、中性最差，且中性与正负之间的误判比例较高。

- rhetorical_function_cn：补充模型行为细节。

- depends_on_cn：依赖跨领域准确率结果。

- sets_up_cn：为讨论中的边界条件提供材料。

- evidence_pointer：Figure 6, Figure 7

### 45. Section 4.4.3 P2

- order：45

- section：Experiments

- locator：Section 4.4.3 P2

- move_code：RESULT

- paraphrase_cn：多领域实验中S2SAN在情感、领域和总体准确率上都最优，分别为0.788、0.829和0.650。

- rhetorical_function_cn：报告多领域主要结果。

- depends_on_cn：依赖多领域数据构造。

- sets_up_cn：为论证S2SAN在联合任务中的有效性。

- evidence_pointer：Table 5

### 46. Section 4.4.3 P3-P5

- order：46

- section：Experiments

- locator：Section 4.4.3 P3-P5

- move_code：RESULT

- paraphrase_cn：在多领域中词注意力不像跨领域中那样有害，但句子级注意力仍带来情感和总体准确率提升，领域准确率没有明显提升。

- rhetorical_function_cn：细化各注意力层在不同任务中的贡献。

- depends_on_cn：依赖多领域结果。

- sets_up_cn：为讨论中的边界条件铺垫。

- evidence_pointer：Section 4.4.3 P3-P5

### 47. Section 4.4.4 P1-P2

- order：47

- section：Experiments

- locator：Section 4.4.4 P1-P2

- move_code：RESULT

- paraphrase_cn：除MLP外，S2S-CNN、S2S-RNN、S2S-LSTM最高准确率均超过基础模型，且收敛更快。

- rhetorical_function_cn：报告词编码器兼容性实验结果。

- depends_on_cn：依赖框架独立性假设。

- sets_up_cn：为贡献中的通用性主张提供证据。

- evidence_pointer：Figure 10

### 48. Section 5 P1

- order：48

- section：Discussion

- locator：Section 5 P1

- move_code：RESULT

- paraphrase_cn：总结四组实验：S2SAN在领域内提升准确率和训练时间，跨领域平均最高，多领域三项指标最好，词编码器替换中除MLP外均有效。

- rhetorical_function_cn：以连贯段落重述全部实验结果。

- depends_on_cn：依赖前文所有实验。

- sets_up_cn：为抽象出的设计结论提供基础。

- evidence_pointer：Section 5 P1

### 49. Section 5 P2

- order：49

- section：Discussion

- locator：Section 5 P2

- move_code：CONTRIBUTION

- paraphrase_cn：S2SAN用句子到句子结构替代序列结构，在多子空间学习句子语义关系并获得更好文本表示，同时降低训练时间。

- rhetorical_function_cn：把实验结果转译为模型设计贡献。

- depends_on_cn：依赖实验总结。

- sets_up_cn：为结论中的理论意义做准备。

- evidence_pointer：Section 5 P2

### 50. Section 5 P2末尾

- order：50

- section：Discussion

- locator：Section 5 P2末尾

- move_code：BOUNDARY_CONDITION

- paraphrase_cn：模型仍有局限：准确率提升有限，跨领域和多领域准确率不高，MLP优化效果不佳。

- rhetorical_function_cn：主动列出边界条件，防止贡献被高估。

- depends_on_cn：依赖实验结果中的非最优项。

- sets_up_cn：为future work铺垫。

- evidence_pointer：Section 5 P2

### 51. Section 6 P1-P2

- order：51

- section：Conclusions

- locator：Section 6 P1-P2

- move_code：CONTRIBUTION

- paraphrase_cn：在线评论情感分析中，句子语义是个体性的而非顺序性的，已有句子级注意力工作很少；本文提出S2SAN填补缺口，并可用任意词编码器。

- rhetorical_function_cn：在结论中重新连接引言缺口并声明贡献。

- depends_on_cn：依赖整个研究和讨论。

- sets_up_cn：为理论/实践意义和future work定位。

- evidence_pointer：Section 6 P1-P2

### 52. Section 6 P3-P4

- order：52

- section：Conclusions

- locator：Section 6 P3-P4

- move_code：BOUNDARY_CONDITION

- paraphrase_cn：理论上提供句子表示新视角、更低复杂度和更多句子依赖关系；实践上可快速分析大规模无标注评论，帮助商家和平台理解用户态度。

- rhetorical_function_cn：把结果上升为理论与实践意义。

- depends_on_cn：依赖贡献声明。

- sets_up_cn：为未来研究方向提供背景。

- evidence_pointer：Section 6 P3-P4

### 53. Section 6 P5

- order：53

- section：Conclusions

- locator：Section 6 P5

- move_code：LIMITATION_AND_FUTURE

- paraphrase_cn：未来计划包括aspect级情感分析、更长更逻辑化的文本如新闻和科技文献，以及结合BERT/ELMo等预训练模型。

- rhetorical_function_cn：指明未验证场景，为后续工作留空间。

- depends_on_cn：依赖全文边界条件。

- sets_up_cn：结束全文。

- evidence_pointer：Section 6 P5

## 写作技术

- gap_construction_cn：采用双重缺口构造：先指出主流的词级注意力忽略句子；再指出已有句子级注意力HAN只是把词级方法搬到句子上，造成序列假设错误和复杂度增加。用“评论句子语义独立”这一语料观察把技术缺陷变成建模假设缺陷。

- signposting_cn：在引言用三个研究目标预告全文；用贡献列表强化重点；每节开头用“In this section”、“Next”、“Further分析”等提醒读者当前论证位置；论文结构段明确各节功能。

- transition_logic_cn：领域内实验后说“进一步分析跨领域”；跨领域实验后说“接下来做多领域”；多领域实验后回溯“第3节曾提到框架独立于词编码器，因此继续验证”。每个过渡都以尚未解决的问题为动力。

- claim_evidence_rhythm_cn：每个实验结果段先给表格/图，再给最高值或平均值，然后补充例外（如JD非最优），最后给机制解释。讨论部分又按四组实验重述，使证据与主张节奏一致。

- benchmark_narrative_cn：基线被包装为“不同时期达到state-of-the-art的经典模型”，HAN被单独强调为层次结构对照；在跨领域和多领域中还引入BI-GRU-ATT vs BI-GRU的比较，以分离词级注意力和句子级注意力的作用。

- theory_return_cn：讨论和结论把实验结果返回到“句子语义个体性而非顺序性”这一起始命题，声称句子到句子注意力提供句子表示新视角，并把低复杂度和多子空间关系学习作为理论意义。

- contribution_positioning_cn：贡献被定位为“首次”的方法创新、与HAN相比的准确率和时间收益、以及可插拔框架对不同词编码器的提升；通过多场景实验和词编码器实验把贡献从单一算法扩展为通用设计。

- novelty_protection_cn：作者用多组实验场景、训练时间与复杂度分析、词编码器兼容性实验共同防止贡献被看成一次性性能结果；但“首次”表述和缺少显著性检验使其保护力度有限。

## 可复用研究与写作程序

### structure_steps

#### 1. 1

- step：1

- writing_job_cn：建立领域重要性：描述在线评论数量、价值和决策影响。

- research_job_cn：确定目标领域和实际痛点。

- required_evidence_cn：平台和评论数据的基本事实或引用。

- transition_to_next_cn：从现实需求引向技术需求。

#### 2. 2

- step：2

- writing_job_cn：综述现有方法并构造缺口：指出主流方法忽略某结构或假设错误。

- research_job_cn：系统梳理方法谱系，找到可替代的建模假设。

- required_evidence_cn：代表性文献和可观察语料特征。

- transition_to_next_cn：缺口指向新设计。

#### 3. 3

- step：3

- writing_job_cn：描述制品：分模块介绍架构、公式和图，说明每个设计选择。

- research_job_cn：实现模型，进行复杂度分析。

- required_evidence_cn：可运行的架构和复杂度对比。

- transition_to_next_cn：模型需要实验验证。

#### 4. 4

- step：4

- writing_job_cn：建立评价框架：说明数据集、基线、指标和实验环境。

- research_job_cn：收集或构造多场景数据集，实现基线。

- required_evidence_cn：数据集统计、基线定义、环境说明。

- transition_to_next_cn：进入结果报告。

#### 5. 5

- step：5

- writing_job_cn：报告核心结果：按任务类型分节，先给表再解释，并指出例外。

- research_job_cn：执行领域内、跨领域、多领域实验。

- required_evidence_cn：准确率表、训练时间、混淆矩阵。

- transition_to_next_cn：核心结果之后检验通用性。

#### 6. 6

- step：6

- writing_job_cn：检验通用性和边界：更换组件或场景，报告哪些情况有效、哪些无效。

- research_job_cn：设计组件替换实验，如不同词编码器。

- required_evidence_cn：对照组和替换实验曲线。

- transition_to_next_cn：结果回收到讨论。

#### 7. 7

- step：7

- writing_job_cn：讨论与贡献：重述结果、提炼设计知识、列出边界和未来。

- research_job_cn：把结果与初始缺口连接，形成可复用主张。

- required_evidence_cn：实验结果与限制列表。

- transition_to_next_cn：结束全文。

### most_transferable_moves_cn

1. 用层次模型作为直接对照，而不是只与最新模型比较

2. 在结果中主动报告非最优数据集和失败组件

3. 增加训练时间和复杂度作为第二评价维度

4. 用组件替换实验证明框架通用性

5. 在讨论和结论中把技术改进重新连接到开头的建模缺口

### resource_intensive_or_nonstandard_parts_cn

1. 四组实验需要两个语言、四个平台、120,000条评论数据

2. 跨领域实验需要12个源-目标方向的训练和测试，计算开销大

3. 需要GPU服务器和多个基线模型的稳定复现

4. 领域内、跨领域、多领域三种任务需要不同评价指标和数据处理

### what_not_to_copy_superficially_cn

1. 没有显著性检验时不要宣称“SOTA”或“明显更优”

2. “首次提出”需要全面文献检索支撑，不能仅靠自我声明

3. 训练时间比较需要保证early stopping和超参数策略一致

4. 如果组件替换实验有失败案例，不能只说成功并忽略失败机制

5. 不能只复制“句子语义独立”这种经验断言而不提供语料示例或定量证据

- single_best_description_of_the_routine_cn：识别性能或建模缺口，提出一个可插拔的计算制品，用多场景基准逐个验证准确率、效率和通用性，最后通过边界条件和未来工作保护贡献不过度泛化。

## 分析边界

本文基于提供全文和表格进行分析；部分图以占位图形式出现，无法从图像读取除图题外的全部数值；文章没有页码，因此位置证据使用章节、段落、表图编号表示；未获得附录或补充材料。
