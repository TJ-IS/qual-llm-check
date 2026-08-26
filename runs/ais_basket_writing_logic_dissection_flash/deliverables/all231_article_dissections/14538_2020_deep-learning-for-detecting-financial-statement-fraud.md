# Deep learning for detecting financial statement fraud

- 作者：Patricia Craja; Alisa Kim; Stefan Lessmann
- 年份 / 期刊：2020 / Decision Support Systems
- DOI：10.1016/j.dss.2020.113421
- 源文件：14538_2020_deep-learning-for-detecting-financial-statement-fraud.md
- 论文主类型：computational_artifact_benchmark
- 主导写作弧线：performance_gap_artifact_benchmark_generalize
- 置信度：0.72

## 文章级论证概况

- 核心问题：如何利用深度学习从年报MD&A文本中提取信息，并与财务比率结合，提高财务报表舞弊检测的预测性能和可解释性，从而为审计师提供决策支持？

- 制品与设计：提出基于层次注意力网络（HAN）的舞弊检测模型。HAN在词级和句子级分别使用双向LSTM编码和注意力机制，生成文档向量，并与47个财务比率拼接后经softmax输出舞弊概率；同时将词级和句级注意力权重转化为“红旗”指标，供审计人员定位需要重点审查的句子。

- 客观结果：在208起舞弊报告与7341份非舞弊报告的美国10-K年报数据集上，HAN在使用财务数据加全文文本（FIN+TXT）时达到最高AUC 92.64%和最高灵敏度90%，优于LR、SVM、RF、XGB、ANN、GPT-2等基准模型；文本特征与财务特征结合显著改善检测效果。

- 核心贡献：作者声称的主要贡献是：首次将深度学习文本表示应用于财务报表舞弊检测，证明MD&A文本的层次化、上下文敏感表示能够补充财务比率；提出可解释的“红旗”句子级指示器，为审计师提供可视化审计决策支持。

- 整篇论证链：作者首先用欺诈损失、审计师低检出率等现实问题建立研究紧迫性，然后通过文献表指出现有研究集中于财务变量或手工语言特征，缺少深度学习文本建模以及财务+文本的完整组合。接着提出三个研究问题：财务与文本数据是否互补、深度学习是否优于词袋、模型能否提供可解释信号。作者构建了AAER标注的10-K年报数据集，将HAN与多种机器学习基线在五种数据组合（FIN、LING、FIN+LING、TXT、FIN+TXT）上比较，发现HAN在FIN+TXT上表现最优。为了回答可解释性问题，又利用lime和HAN注意力分别提取词级“红旗”词表，并设计句级注意力权重高亮句子，形成两阶段审计决策支持。最后在讨论中回到上下文依赖的欺骗线索理论，将HAN的成功归因于其层次化注意力结构，并将句级解释视为更稳健、更不易被操纵的决策支持机制。

## 类型与写作弧线判定

- 论文主类型判定：文章的核心是构造HAN这一计算制品，以历史SEC年报数据集和多个基准模型比较为主要证据，没有实地部署、用户实验或现场干预；评价以离线分类性能、AUC/F2等指标和可解释性示例为主，属于计算制品加benchmark的研究范式。

- 主导写作弧线判定：文章从现有舞弊检测方法的性能缺口（审计师检出率低、词袋无法捕捉上下文）出发，引入HAN制品，通过系统benchmark证明性能优势，再将性能优势推广为可复用的决策支持设计知识（句级红旗指示、多数据源组合原则）。

## 研究开展程序

- study_or_phase_count：5

- 研究阶段总序列：五个阶段依次完成：数据构建与标注、模型与输入设计、比较评价实验、词级可解释性分析、句级决策支持演示。前三个阶段回答问题1和2，后两个阶段回答问题3。每个阶段为下一阶段提供必要输入：数据阶段提供实验语料；模型阶段提供可比较的基准和HAN；比较实验发现HAN在FIN+TXT最好，从而引出可解释性；词级分析暴露词级红旗不稳定，因而推进到句级分析；句级高亮展示最终决策支持应用。

### studies_or_phases

#### 1. 数据构建与标注阶段

- order：1

- name_cn：数据构建与标注阶段

- question_cn：如何获得足够大且可信的舞弊年报数据集，并处理类别不平衡？

- inputs_and_setting_cn：美国SEC EDGAR数据库的10-K年报文本、Compustat财务数据、1999–2019年AAER诉讼公告；最终样本包括208份舞弊报告和7341份非舞弊报告。

- designed_or_compared_object_cn：舞弊标注（AAER匹配）、财务比率集合（Dechow/Beneish公式）、文本预处理、缺失值插补、1:4欠采样平衡。

- baseline_control_or_counterfactual_cn：未平衡前的187869份年报和1:250自然比例作为背景参照；按年份和行业进行欠采样以避免年份和行业混淆。

##### objective_metrics

（空）

- analysis_method_cn：AAER文本规则筛选、Compustat比率提取、随机森林插补、按年份/行业分层欠采样。

- main_result_cn：形成7 757个企业-年度观测，其中208舞弊、7341非舞弊；平衡后1 163份报告，其中201舞弊、962非舞弊；2002–2004年舞弊集中，与SOX后监管加强一致。

- argumentative_role_cn：提供全文后续实验的核心数据基础，并利用AAER可信标签和最大文本数据集来支持结论的外部有效性。

- remaining_uncertainty_cn：AAER标签存在约三年时滞，只覆盖被SEC执法的案件，未区分无意错报与有意舞弊。

- link_to_next_phase_cn：为该数据集设计可比的输入表示（FIN、LING、TXT）和模型集合。

##### evidence_pointers

1. Section 5 全文

2. Section 5.1 Labeling

3. Section 5.4 Imbalance treatment

#### 2. 模型与输入设计阶段

- order：2

- name_cn：模型与输入设计阶段

- question_cn：如何选择文本表示和学习模型，使模型既能捕捉MD&A的层次结构又能输出可解释信号？

- inputs_and_setting_cn：MD&A全文、L&M词表等语言特征、47个财务比率、Google News预训练word2vec、GPT-2预训练嵌入；模型输入为词向量序列与财务比率拼接。

- designed_or_compared_object_cn：HAN（word2vec + 双向LSTM + 词/句注意力）与GPT-2+注意力、BOW/TF-IDF+LR/SVM/RF/XGB/ANN等基准；数据组合分为FIN、LING、FIN+LING、TXT、FIN+TXT。

- baseline_control_or_counterfactual_cn：传统BOW文本表示作为深度学习文本表示的对照；GPT-2+注意力作为另一个DL对照；单独财务数据作为数据组合的基线。

##### objective_metrics

（空）

- analysis_method_cn：基于性能选择嵌入；HAN训练采用批量32、17个epoch、dropout；FIN+TXT通过两阶段建模（文本概率作为输入）或直接拼接。

- main_result_cn：形成完整的7模型×5数据组合评价框架，并确定HAN使用300维Google News word2vec、LSTM 150神经元、文档向量200维、最后与47个财务比率拼接。

- argumentative_role_cn：将研究问题操作化为可复现的模型和数据组合矩阵，是后续所有结果的依赖框架。

- remaining_uncertainty_cn：没有对HAN内部各组件（如层次结构、注意力、预训练嵌入）进行系统消融，因此无法精确归因性能增益来源。

- link_to_next_phase_cn：在固定数据划分和评价协议下执行比较实验。

##### evidence_pointers

1. Section 4 Methodology

2. Section 4.3 Hierarchical Attention Network

3. Section 4.1 Neural Embeddings

#### 3. 比较评价实验阶段

- order：3

- name_cn：比较评价实验阶段

- question_cn：RQ1：财务和文本数据组合是否比单一数据更有信息量？RQ2：HAN能否在文本特征提取上胜过BOW？

- inputs_and_setting_cn：五种数据组合、七类模型、随机分层抽样形成的训练/验证/测试集；测试集分类结果。

- designed_or_compared_object_cn：各模型在FIN、LING、FIN+LING、TXT、FIN+TXT上的离线分类性能；关注AUC、灵敏度、特异度、F1、F2、准确率。

- baseline_control_or_counterfactual_cn：将多数类基线准确率0.8281作为最低参照；FIN和LING作为数据补充的delta比较；BOW模型作为DL文本建模的基础对照。

##### objective_metrics

1. AUC

2. Sensitivity/Recall

3. Specificity

4. F1-score

5. F2-score

6. Accuracy

- analysis_method_cn：五组数据组合×七种分类器的交叉比较；通过delta AUC/F1比较数据源增量；按F2和AUC解释成本不对称。

- main_result_cn：HAN在TXT上AUC 91.08%，在FIN+TXT上AUC 92.64%、灵敏度90%，均为最高；RF/ANN/XGB等在TXT或FIN+TXT上的AUC约为87–89%；文本数据一致优于手工语言特征；FIN+TXT相比FIN+LING带来明显AUC提升。

- argumentative_role_cn：这是全文核心证据，直接回答RQ1和RQ2：证明财务+全文文本组合更有信息量，且HAN比BOW模型更优。

- remaining_uncertainty_cn：FN和FP的实际成本并未由真实审计流程校准；F2和阈值选择虽然反映成本偏好，但没有审计师行为数据验证。

- link_to_next_phase_cn：在性能优势基础上，作者转向解释HAN为何有效以及如何支持审计决策。

##### evidence_pointers

1. Section 6 Classification results

2. Table 2

3. Section 6.3 Modeling of text data

#### 4. 词级可解释性分析阶段

- order：4

- name_cn：词级可解释性分析阶段

- question_cn：RQ3的一部分：能否从模型中得到词级“红旗”指示，辅助审计？

- inputs_and_setting_cn：所有舞弊样本的MD&A文本；RF模型的lime局部解释；HAN注意力层的词权重。

- designed_or_compared_object_cn：比较RF（传统ML+可解释工具）和HAN注意力各自识别的“红旗”词表，并求交集。

- baseline_control_or_counterfactual_cn：RF的lime解释作为传统解释基准；HAN注意力作为深度学习内在解释。

##### objective_metrics

（空）

- analysis_method_cn：对每个舞弊文本用lime提取前10个词，聚合为红旗词表；对HAN提取注意力权重；计算两类词表的重叠。

- main_result_cn：RF和HAN分别给出大量不同词汇，仅15个重叠词，如government、certain、gross及月份词；词表含义模糊且易被操纵。

- argumentative_role_cn：展示模型可解释性，但同时暴露词级红旗的脆弱性，为句级方案做铺垫。

- remaining_uncertainty_cn：重叠词数量少且无统计检验；无法确认这些词是否具有稳定因果关系。

- link_to_next_phase_cn：词级分析的不稳定性直接引出句级注意力高亮作为更稳健的方案。

##### evidence_pointers

1. Section 7.1 Word-level

2. Figure 3

3. Figure 4

#### 5. 句级决策支持演示阶段

- order：5

- name_cn：句级决策支持演示阶段

- question_cn：RQ3的核心：能否利用HAN的句级注意力生成“红旗”句子，帮助审计师审查MD&A？

- inputs_and_setting_cn：200份被HAN预测为舞弊的报告；HAN句级注意力权重；MD&A文本页面可视化。

- designed_or_compared_object_cn：每个报告的句级注意力权重；根据权重将句子标记为“重要”和“额外重要”。

- baseline_control_or_counterfactual_cn：以句级注意力最高权重0.61和平均权重0.05作为规则阈值，标记审计关注句子；没有与人工审计标注比较。

##### objective_metrics

（空）

- analysis_method_cn：对舞弊报告提取句级注意力权重，每份报告取前10句，按阈值高亮；提出两阶段决策支持流程：先由HAN给出舞弊风险概率，再由高亮句指导审计。

- main_result_cn：句级红包句子可视化示例展示MD&A页面中的重点句子；作者声称这比词级标记更稳健、更能帮助审计师提高检测准确率。

- argumentative_role_cn：作为RQ3的关键回答，将HAN从预测工具升级为可操作的审计决策支持界面。

- remaining_uncertainty_cn：没有审计师对高亮句子的有用性、精确性进行实证评估，也没有检测实际审计效率提升。

- link_to_next_phase_cn：该演示支撑全文结论中关于可解释决策支持系统的贡献主张。

##### evidence_pointers

1. Section 7.2 Sentence-level

2. Figure 5

## 各部分修辞架构

### abstract_moves

1. CONTEXT：舞弊是投资者、审计公司和监管者关注的问题。

2. PHENOMENON：提出结合财务比率和年报MD&A文本进行舞弊检测。

3. DESIGN_FEATURE：使用HAN从MD&A提取文本特征，体现文档层次结构并包含词/句两级注意力。

4. CONTRIBUTION：模型捕获内容和上下文，提供可解释的红旗句子。

5. RESULT：HAN文本特征分类结果良好，并实质性增强财务指标。

### introduction_moves

1. CONTEXT：全球舞弊损失巨大且间接成本更高。

2. PRACTICAL_STAKES：审计师实际检出率低，利益相关者需要自动系统。

3. GAP：以往研究没有将深度学习文本建模用于舞弊检测，也没有结合FIN+TXT和可解释性。

4. RQ_OR_OBJECTIVE：提出三个RQ并声明贡献。

### theory_and_knowledge_moves

1. PRIOR_KNOWLEDGE：财务变量与语言特征都被用于舞弊检测，但语言特征多为词表/可读性。

2. LIMITATION：BOW忽略语法、上下文和结构。

3. THEORY_INTRO：欺骗心理学认为管理者语言线索可揭示认知过程，且相关线索依赖上下文。

4. MECHANISM：MD&A不受同等监管约束，管理层可能操纵或省略信息。

5. REQUIREMENT：需要上下文敏感的深度学习文本表示，而非预定词表。

### artifact_design_moves

1. METHOD_JUSTIFICATION：文本需要数值向量表示，BOW简单但有缺陷，因此选择预训练词向量。

2. DESIGN_FEATURE：HAN分层编码词、句并应用两级注意力。

3. DESIGN_FEATURE：文档向量与47个财务比率拼接进入softmax。

4. METHOD_JUSTIFICATION：采用F2-score和阈值选择以反映舞弊漏检的高成本。

### evaluation_moves

1. STUDY_OVERVIEW：比较7种分类器×5种数据组合。

2. BENCHMARK_OR_CONTRAST：FIN作为财务基线，LING作为语言基线，TXT代表全文输入，FIN+TXT为完整组合。

3. RESULT：HAN在FIN+TXT上AUC最高，达到92.64%，灵敏度90%。

4. ROBUSTNESS_OR_BOUNDARY_TEST：对比GPT-2+注意力，说明预训练嵌入选择会影响结果。

5. TRANSITION：从预测性能转向解释。

### discussion_and_contribution_moves

1. GAP：再次指出没有研究结合财务和文本数据。

2. RESULT：RF在BOW设置下最好，HAN在FIN+TXT设置下表现突出。

3. THEORY_RETURN：HAN的结果支持“欺骗检测需要上下文”的论点。

4. BOUNDARY_CONDITION：词级红旗易受操纵，句级标记更稳健。

5. CONTRIBUTION：提供句级红旗句子，为审计师决策支持。

## 理论/知识到设计的翻译

### 知识/理论基础

1. 舞弊侦查文献：财务比率与手工语言特征对舞弊的预测能力以及两者的互补性。

2. 欺骗心理学：管理者的认知和情绪状态可能通过语言线索泄露，识别欺骗需要上下文而非孤立词汇。

3. 自然语言处理：文档的层次结构（词-句-文档）、词向量与注意力的作用。

4. 审计决策支持：模型必须可解释，错误分类成本不对称，红旗比绿旗更难获得但更有用。

- 理论—设计耦合：partial

- 耦合判定理由：欺骗心理学和文本线索的上下文依赖问题为选择MD&A文本和注意力机制提供了动机，但HAN的具体架构来自NLP领域既有模型（Yang et al.），嵌入选择和财务比率拼接主要依赖工程经验与文献中的变量集，并非从理论严格推导；理论主要用于解释结果和包装贡献。

- 理论到设计翻译链：欺骗/上下文线索理论 -> 需要保留词序、语法、上下文和文档结构 -> 使用预训练词向量和层次注意力网络进行文本编码 -> 文档向量与财务比率拼接 -> 与BOW/手工语言特征对照 -> 通过AUC/F2验证 -> 注意力权重解释为红旗词/句，形成审计决策支持。

### mapping_table

#### 1. 1

- theory_or_knowledge_claim_cn：欺骗检测需要上下文和语境线索，而不只是孤立词表中的词。

- mechanism_cn：同一个词在不同句子中的重要性可能不同，管理层可通过适应词列表来掩盖舞弊，但更难操纵句子结构。

- design_requirement_cn：文本表示必须同时捕捉内容与上下文，并输出可解释的信号。

- artifact_choice_cn：HAN的双向LSTM和词/句两级注意力。

- evaluated_contrast_cn：HAN vs BOW/TF-IDF模型、HAN注意力 vs RF lime。

- objective_result_cn：HAN在TXT上AUC 91.08%，在FIN+TXT上AUC 92.64%；词级重叠词仅15个，句级注意力提供高亮句。

##### evidence_pointers

1. Section 4.3

2. Section 6.3

3. Section 7

#### 2. 2

- theory_or_knowledge_claim_cn：财务比率和文本线索是互补的，能发现彼此无法发现的舞弊类型。

- mechanism_cn：财务指标反映操纵结果，言语线索反映管理者的措辞和认知痕迹，两者相关性低。

- design_requirement_cn：分类模型应同时输入财务和文本数据，而非只使用单一数据源。

- artifact_choice_cn：FIN+TXT组合，HAN文档向量与47个财务比率拼接。

- evaluated_contrast_cn：FIN+TXT vs FIN、LING、FIN+LING；delta AUC/F1。

- objective_result_cn：HAN在FIN+TXT的AUC 92.64%，灵敏度90%，优于单独的FIN和LING。

##### evidence_pointers

1. Section 3.1

2. Section 5.3

3. Section 6.3

#### 3. 3

- theory_or_knowledge_claim_cn：BOW忽略词序、语法和上下文，无法充分捕捉文本语义。

- mechanism_cn：词袋表示将文档视为无序词集合，句法和上下文信息丢失，难以捕捉欺骗性文本的委婉表达。

- design_requirement_cn：使用预测式词嵌入和序列模型。

- artifact_choice_cn：word2vec预训练嵌入 + LSTM编码。

- evaluated_contrast_cn：ANN/BOW vs HAN/DL；GPT-2+注意力作为另一个DL对照。

- objective_result_cn：HAN的AUC和灵敏度高于BOW基准；GPT-2+注意力表现一般，说明嵌入选择影响结果。

##### evidence_pointers

1. Section 3.2

2. Section 4.1

3. Table 2

#### 4. 4

- theory_or_knowledge_claim_cn：舞弊漏检的成本高于误报，因此评价应偏向灵敏度。

- mechanism_cn：审计中漏掉真实舞弊可能导致更大损失，而错误警报虽增加工作量但成本较低。

- design_requirement_cn：使用F2-score、AUC并选择阈值最大化灵敏度与FPR差。

- artifact_choice_cn：F2-score评价、HAN阈值0.03。

- evaluated_contrast_cn：不同模型在灵敏度/F2上的排序。

- objective_result_cn：HAN灵敏度最高（90%），XGB在部分场景F2最高。

##### evidence_pointers

1. Section 4.4

2. Section 6

#### 5. 5

- theory_or_knowledge_claim_cn：审计决策支持要求模型可解释，红旗信号须能引导进一步审查。

- mechanism_cn：审计师需要知道哪句话触发了舞弊判断，从而快速定位风险片段。

- design_requirement_cn：从深度学习模型提取有形、可定位的解释信号。

- artifact_choice_cn：HAN注意力权重映射到红旗句子，形成两阶段审计决策流程。

- evaluated_contrast_cn：词级红旗 vs 句级红旗；RF lime vs HAN注意力。

- objective_result_cn：词级结果不稳定且易被操纵；句级注意力高亮示例可定位MD&A中高风险句子。

##### evidence_pointers

1. Section 7

## 评价逻辑

### evaluation_modes

1. 离线历史数据benchmark：在AAER标注的10-K年报上比较模型。

2. 数据组合消融型比较：FIN、LING、FIN+LING、TXT、FIN+TXT的逐级对比。

3. 模型对比：LR/SVM/RF/XGB/ANN/HAN/GPT-2在同一协议下比较。

4. 成本敏感指标评价：使用AUC、F2-score和阈值调整。

5. 可解释性演示：词级lime与注意力比较、句级注意力高亮。

- why_these_evaluations_cn：三个RQ分别要求验证数据组合价值、DL相对BOW的优势和可解释性，因此需要多模型、多数据组合的离线比较，再加解释分析；由于缺少部署环境，未做现场实验或用户研究。

- benchmark_and_contrast_chain_cn：以FIN为传统基线；LING展示手工语言特征的下限；FIN+LING观察手工语言与财务的结合；TXT引入全文文本；FIN+TXT作为最终完整设置。表格中的delta列帮助读者看到每一步数据源增加带来的AUC/F1变化，从而论证文本和财务的互补性。

### claim_evidence_ledger

#### 1. 财务+全文文本比单独财务或单独文本更有信息量。

- claim_cn：财务+全文文本比单独财务或单独文本更有信息量。

- evidence_cn：Table 2中最优HAN在FIN+TXT上的AUC 92.64%，高于FIN和TXT设置；多数模型在FIN+TXT上的AUC也高于FIN+LING。

- status_cn：supported

#### 2. HAN等深度学习文本表示优于BOW。

- claim_cn：HAN等深度学习文本表示优于BOW。

- evidence_cn：HAN的AUC和灵敏度超过TF-IDF+BOW基准；GPT-2+注意力虽不总是最好，但仍优于部分BOW模型。

- status_cn：partially supported

#### 3. HAN的层次结构和注意力是性能提升的原因。

- claim_cn：HAN的层次结构和注意力是性能提升的原因。

- evidence_cn：没有对层次、注意力、嵌入进行消融；与GPT-2+注意力比较显示嵌入选择对结果影响很大，因此不能唯一归因于HAN结构。

- status_cn：weakly supported

#### 4. 注意力权重能识别有意义的红旗词和红旗句。

- claim_cn：注意力权重能识别有意义的红旗词和红旗句。

- evidence_cn：展示了词级重叠词表和高亮句子示例，但没有审计师评估、精确率/召回率或与人工标注一致性。

- status_cn：partially supported

#### 5. 句级红旗比词级更稳健。

- claim_cn：句级红旗比词级更稳健。

- evidence_cn：作者主要用概念论证：句子更复杂、更难操纵；没有实证比较词级和句级在面对操纵时的存活率。

- status_cn：asserted, not directly tested

- internal_validity_strategy_cn：随机分层抽样划分训练/验证/测试集；按年度和行业进行欠采样，减少经济周期、法规变化和行业用词差异的混淆；固定数据划分与统一评价指标保证模型可比。

- external_validity_strategy_cn：使用公开SEC EDGAR和Compustat数据，样本量声称是带文本成分的最大舞弊数据集；AAER标签来自监管机构，具有一定可信度。

- what_is_not_actually_tested_cn：未测试真实审计师对红旗句子的接受度和使用效果；未测试模型在时间外推、跨期演化和主动应对操纵下的表现；未对HAN的层次和注意力组件进行消融；未检验词表中的词因操纵者适应性行为而失效的速度。

## 贡献闭环

- technical_claim_cn：HAN在财务+MD&A全文文本设置下达到AUC 92.64%和灵敏度90%，优于多个传统ML和DL基准。

- artifact_claim_cn：HAN的层次结构和词/句注意机制是提升文本特征提取能力和可解释性的关键，但缺乏严格消融。

- mechanism_claim_cn：MD&A文本线索依赖上下文和文档结构，HAN通过层次注意捕获了这些线索，从而强化模型区分真假报告的能力。

- boundary_claim_cn：结论基于美国上市公司10-K年报的MD&A文本、AAER标签和1:4平衡数据，适用于支持审计过程中的风险筛选，不适用于实时或非年报文本。

- reusable_design_knowledge_cn：文本数据不应只压缩为手工语言特征，全文MD&A加财务比率的组合更有效；深度学习文本表示能够直接输出句子级红旗，可供审计人员定位高风险内容；评价舞弊检测时应采用F2/AUC等对漏检敏感的指标。

- theoretical_contribution_cn：将“欺骗检测需要上下文”的心理学论点引入财务报表舞弊检测，用HAN的实证结果强化该观点，并指出注意力权重可作为理论到实践的解释接口。论文没有提出新的行为理论，而是连接了NLP机制与舞弊线索理论。

- how_discussion_closes_intro_gap_cn：讨论部分重新强调引言指出的两个缺口——无研究使用DL提取文本特征、极少研究结合财务+文本并注意可解释性——然后用HAN在FIN+TXT上的结果和红旗句子直接回应：新型DL文本特征能够提升检测，句级解释能缓解现有红绿旗研究的不足。

- overclaim_or_unsupported_leaps_cn：将HAN的性能优势主要归因于上下文/层次结构，但没有系统消融；将句级红旗标记描述为能提高审计准确度，但无审计师行为证据；将“红旗词集不稳定”推演为“句级更稳”，缺少直接对照证据。

## 句级写作动作图谱

### 1. Abstract P1 S1

- order：1

- section：Abstract

- locator：Abstract P1 S1

- move_code：CONTEXT

- paraphrase_cn：财务报表舞弊是投资者、审计公司和监管者非常关切的问题。

- rhetorical_function_cn：开篇点明研究领域和读者对象。

- depends_on_cn：无。

- sets_up_cn：为提出检测方法建立现实背景。

- evidence_pointer：Abstract first sentence

### 2. Abstract P1 S2

- order：2

- section：Abstract

- locator：Abstract P1 S2

- move_code：PHENOMENON

- paraphrase_cn：本文提出结合财务比率和年报MD&A管理评论进行舞弊检测。

- rhetorical_function_cn：一句话概括研究方案。

- depends_on_cn：舞弊问题背景。

- sets_up_cn：引出后续方法细节。

- evidence_pointer：Abstract second sentence

### 3. Abstract P1 S3-S5

- order：3

- section：Abstract

- locator：Abstract P1 S3-S5

- move_code：DESIGN_FEATURE

- paraphrase_cn：采用HAN提取MD&A文本特征，体现文档层次结构，并通过词级和句级注意力区分内容重要性。

- rhetorical_function_cn：突出模型两大特性：层次结构和注意力。

- depends_on_cn：前句提出的方案。

- sets_up_cn：为解释模型优势提供依据。

- evidence_pointer：Abstract third-fifth sentences

### 4. Abstract P1 S6

- order：4

- section：Abstract

- locator：Abstract P1 S6

- move_code：CONTRIBUTION

- paraphrase_cn：模型捕捉管理评论的内容和上下文，并提供红旗句子作为可解释信号。

- rhetorical_function_cn：声明可解释性贡献。

- depends_on_cn：HAN的双级注意力特性。

- sets_up_cn：引出全文的决策支持导向。

- evidence_pointer：Abstract final sentence

### 5. Introduction P1 S1-S2

- order：5

- section：Introduction

- locator：Introduction P1 S1-S2

- move_code：CONTEXT

- paraphrase_cn：舞弊是全球性问题，过去二十年造成的财务损失约5.127万亿美元且近十年增长56%。

- rhetorical_function_cn：用数字建立问题严重性。

- depends_on_cn：无。

- sets_up_cn：为自动检测需求提供动机。

- evidence_pointer：Introduction P1 S1-S2

### 6. Introduction P1 S3-S4

- order：6

- section：Introduction

- locator：Introduction P1 S3-S4

- move_code：PRACTICAL_STAKES

- paraphrase_cn：实际成本还包括投资者、债权人、员工信誉受损和业务减少，甚至导致破产。

- rhetorical_function_cn：扩展损失维度，说明舞弊不只是财务数字问题。

- depends_on_cn：前句的财务损失数据。

- sets_up_cn：强调研究舞弊检测的实践重要性。

- evidence_pointer：Introduction P1 S3-S4

### 7. Introduction P2 S1-S2

- order：7

- section：Introduction

- locator：Introduction P2 S1-S2

- move_code：PHENOMENON

- paraphrase_cn：ACFE将舞弊分为腐败、资产挪用和舞弊性报表三类；本研究聚焦财务报表舞弊。

- rhetorical_function_cn：界定研究对象，缩小范围。

- depends_on_cn：舞弊问题背景。

- sets_up_cn：为确定舞弊定义和后续标签方法做铺垫。

- evidence_pointer：Introduction P2 S1-S2

### 8. Introduction P2 S3

- order：8

- section：Introduction

- locator：Introduction P2 S3

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：采用Nguyen对财务报表舞弊的定义，即故意不按公认会计原则报告导致的重大遗漏或错报。

- rhetorical_function_cn：给出精确概念边界。

- depends_on_cn：前句聚焦舞弊报表。

- sets_up_cn：区分故意舞弊与无意错误，为AAER标签定义服务。

- evidence_pointer：Introduction P2 S3

### 9. Introduction P3 S1-S2

- order：9

- section：Introduction

- locator：Introduction P3 S1-S2

- move_code：PRACTICAL_STAKES

- paraphrase_cn：职业舞弊中位数损失12.5万美元且持续14个月，但财务报表舞弊中位损失95.4万美元且持续24个月，损害更严重。

- rhetorical_function_cn：用对比数据突出财务报表舞弊的特殊危害。

- depends_on_cn：ACFE报告。

- sets_up_cn：解释为何需要专门针对报表舞弊的检测系统。

- evidence_pointer：Introduction P3 S1-S2

### 10. Introduction P4 S1-S2

- order：10

- section：Introduction

- locator：Introduction P4 S1-S2

- move_code：PHENOMENON

- paraphrase_cn：管理层可能为个人利益、满足短期目标或隐瞒坏消息而舞弊，报表被操纵后与正常报表难以分辨。

- rhetorical_function_cn：描述舞弊行为特征，说明检测困难。

- depends_on_cn：前面关于舞弊危害。

- sets_up_cn：为引出文本线索和自动检测做铺垫。

- evidence_pointer：Introduction P4 S1-S2

### 11. Introduction P5 S1-S3

- order：11

- section：Introduction

- locator：Introduction P5 S1-S3

- move_code：PRACTICAL_STAKES

- paraphrase_cn：审计师发现舞弊的比例只有内部15%和外部4%，因此需要自动检测系统。

- rhetorical_function_cn：用审计师低检率建立对智能系统的需求。

- depends_on_cn：舞弊难检测的性质。

- sets_up_cn：引出下文对现有检测研究的评述。

- evidence_pointer：Introduction P5 S1-S3

### 12. Introduction P5 S4-S6

- order：12

- section：Introduction

- locator：Introduction P5 S4-S6

- move_code：GAP

- paraphrase_cn：已有研究考察财务和语言因素，但MD&A语言可能揭示管理层认知过程；不过还没有研究将最新深度学习用于文本特征提取，且很少研究财务+语言组合与可解释性。

- rhetorical_function_cn：同时建立两个缺口：DL文本建模缺席和解释性不足。

- depends_on_cn：审计师低检出率和MD&A文本价值。

- sets_up_cn：为三个RQ提供文献依据。

- evidence_pointer：Introduction P5 S4-S6

### 13. Introduction P6 S1

- order：13

- section：Introduction

- locator：Introduction P6 S1

- move_code：RQ_OR_OBJECTIVE

- paraphrase_cn：作者声称要弥合缺口，提出基于财务与文本数据的DL模型来筛查报告。

- rhetorical_function_cn：宣告研究目标。

- depends_on_cn：前句的缺口。

- sets_up_cn：列出贡献方向：预测性能、红旗指标、成本敏感评价。

- evidence_pointer：Introduction P6 S1

### 14. Section 2 P1 S1-S3

- order：14

- section：Research design and contributions

- locator：Section 2 P1 S1-S3

- move_code：RQ_OR_OBJECTIVE

- paraphrase_cn：提出三个研究问题：数据组合是否有信息增益、DL是否优于BOW、模型能否解释文本信号。

- rhetorical_function_cn：将目标正式化为可操作问题。

- depends_on_cn：引言中的缺口。

- sets_up_cn：确定后续实验设计。

- evidence_pointer：Section 2 P1 S1-S3

### 15. Section 2 P2 S1-S3

- order：15

- section：Research design and contributions

- locator：Section 2 P2 S1-S3

- move_code：STUDY_OVERVIEW

- paraphrase_cn：选择LR、SVM、RF以及XGB和ANN等模型，主要关注文本处理，并引入HAN。

- rhetorical_function_cn：预告模型集合，解释为何包含已建和未测试模型。

- depends_on_cn：三个RQ。

- sets_up_cn：为表2的模型矩阵搭建结构。

- evidence_pointer：Section 2 P2 S1-S3

### 16. Section 2 P3 S1-S3

- order：16

- section：Research design and contributions

- locator：Section 2 P3 S1-S3

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：所有模型都在FIN、LING、FIN+LING、TXT、FIN+TXT五种数据组合上训练，并用AUC、灵敏度、F1/F2等指标衡量。

- rhetorical_function_cn：说明评价协议，强调成本不对称指标。

- depends_on_cn：模型集合。

- sets_up_cn：支撑RQ1和RQ2的比较矩阵。

- evidence_pointer：Section 2 P3 S1-S3

### 17. Section 3 P1 and Table 1

- order：17

- section：Section 3

- locator：Section 3 P1 and Table 1

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：表1显示此前研究集中于财务变量，部分使用语言变量，分类器从LR到DL都有，但很少基于完整文本而非手工特征。

- rhetorical_function_cn：用文献表系统展示现状，便于读者定位缺口。

- depends_on_cn：引言中的研究目标。

- sets_up_cn：为批评现有文本处理的局限提供证据。

- evidence_pointer：Section 3 Table 1

### 18. Section 3 P1 S4-S6

- order：18

- section：Section 3

- locator：Section 3 P1 S4-S6

- move_code：LIMITATION

- paraphrase_cn：只有Hajek和Henriques结合了财务和语言数据，但未评价年报文本内容，也未使用BOW或DL等复杂文本挖掘技术。

- rhetorical_function_cn：指出最近相关工作仍存在的技术缺口。

- depends_on_cn：文献表。

- sets_up_cn：为本文“FIN+TXT+DL”组合提供切入点。

- evidence_pointer：Section 3 P1 S4-S6

### 19. Section 3 P1 S7-S9

- order：19

- section：Section 3

- locator：Section 3 P1 S7-S9

- move_code：GAP

- paraphrase_cn：多数研究忽视可解释性；Hajek和Henriques只能得到绿旗值，无法为舞弊样本得到红旗值。

- rhetorical_function_cn：建立可解释性缺口。

- depends_on_cn：文献表。

- sets_up_cn：引出本文红旗词/句贡献。

- evidence_pointer：Section 3 P1 S7-S9

### 20. Section 3 P1 S10

- order：20

- section：Section 3

- locator：Section 3 P1 S10

- move_code：WHY_GAP_MATTERS

- paraphrase_cn：漏检舞弊成本高于错误标记正常报表，因此预警信号对审计效率至关重要。

- rhetorical_function_cn：从成本角度论证红旗研究的重要性。

- depends_on_cn：Hajek的成本估计。

- sets_up_cn：为F2-score和灵敏度导向评价提供依据。

- evidence_pointer：Section 3 P1 S10

### 21. Section 3.1 P1 S1-S3

- order：21

- section：Section 3.1

- locator：Section 3.1 P1 S1-S3

- move_code：CONTEXT

- paraphrase_cn：MD&A为投资者提供管理层对公司业绩和未来前景的看法，并包含主要风险和应对行动。

- rhetorical_function_cn：说明选择MD&A作为文本源的原因。

- depends_on_cn：对年报文本的总体定位。

- sets_up_cn：支撑“文本可揭示管理层认知”的机制。

- evidence_pointer：Section 3.1 P1 S1-S3

### 22. Section 3.1 P2 S1-S2

- order：22

- section：Section 3.1

- locator：Section 3.1 P2 S1-S2

- move_code：MECHANISM

- paraphrase_cn：MD&A受监管程度低于财务信息，管理层有更大操纵空间，可能为呈现有利形象而操纵或遗漏信息。

- rhetorical_function_cn：建立文本可用于舞弊检测的行为机制。

- depends_on_cn：MD&A内容描述。

- sets_up_cn：引出需要更强大的文本分析技术。

- evidence_pointer：Section 3.1 P2 S1-S2

### 23. Section 3.1 P2 S4-S5

- order：23

- section：Section 3.1

- locator：Section 3.1 P2 S4-S5

- move_code：THEORY_INTRO

- paraphrase_cn：社会心理学研究认为，想隐瞒真实情况的管理者的情绪和认知过程会体现在特定语言线索中。

- rhetorical_function_cn：引入理论依据，解释文本特征为何能预测舞弊。

- depends_on_cn：MD&A可被操纵这一现象。

- sets_up_cn：为后文L&M词表和深度学习上下文表示提供理论支撑。

- evidence_pointer：Section 3.1 P2 S4-S5

### 24. Section 3.1 P3 S1-S6

- order：24

- section：Section 3.1

- locator：Section 3.1 P3 S1-S6

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：年报语言研究有两种策略：预定词表（如L&M）和机器学习自动特征提取；L&M词表可作为DL方法的基准。

- rhetorical_function_cn：区分手工语言特征和自动文本特征。

- depends_on_cn：文本线索理论。

- sets_up_cn：将L&M词表作为LING数据来源，并让DL与BOW形成对照。

- evidence_pointer：Section 3.1 P3 S1-S6

### 25. Section 3.1 P4 S3-S4

- order：25

- section：Section 3.1

- locator：Section 3.1 P4 S3-S4

- move_code：MECHANISM

- paraphrase_cn：Purda和Skillicorn发现语言模型与财务模型低相关、能发现对方无法发现的舞弊类型，因此二者互补。

- rhetorical_function_cn：为财务+文本特征组合提供经验依据。

- depends_on_cn：前人的SVM语言模型和财务指标。

- sets_up_cn：支持FIN+TXT作为核心数据组合。

- evidence_pointer：Section 3.1 P4 S3-S4

### 26. Section 3.1 P5 S1

- order：26

- section：Section 3.1

- locator：Section 3.1 P5 S1

- move_code：LIMITATION

- paraphrase_cn：Hajek和Henriques的研究最接近本文，但其没有评估年报文本内容，也未使用现代NLP方法。

- rhetorical_function_cn：强调最近工作的缺口，确立本文推进方向。

- depends_on_cn：文献表中的Hajek和Henriques。

- sets_up_cn：为引入HAN和FIN+TXT做出铺垫。

- evidence_pointer：Section 3.1 P5 S1

### 27. Section 3.2 P1 S2-S4

- order：27

- section：Section 3.2

- locator：Section 3.2 P1 S2-S4

- move_code：LIMITATION

- paraphrase_cn：BOW将文档表示为词频向量，忽略语法、上下文和结构，可能无法理解文本真实含义。

- rhetorical_function_cn：批评传统文本表示。

- depends_on_cn：对NLP方法的已有知识。

- sets_up_cn：为DL方法的引入提供逻辑。

- evidence_pointer：Section 3.2 P1 S2-S4

### 28. Section 3.2 P1 S5-S7

- order：28

- section：Section 3.2

- locator：Section 3.2 P1 S5-S7

- move_code：THEORY_INTRO

- paraphrase_cn：深度ANN能自动从非结构化数据中提取高层特征，学习文本模式并解决BOW的问题。

- rhetorical_function_cn：介绍DL的机制优势。

- depends_on_cn：BOW缺陷。

- sets_up_cn：引出HAN架构。

- evidence_pointer：Section 3.2 P1 S5-S7

### 29. Section 3.2 P2 S3-S5

- order：29

- section：Section 3.2

- locator：Section 3.2 P2 S3-S5

- move_code：REQUIREMENT

- paraphrase_cn：用于实践的DL模型不仅应准确，还应可解释；但多数舞弊检测系统只追求准确率而忽略透明性。

- rhetorical_function_cn：把可解释性提升为系统的设计要求。

- depends_on_cn：DL可能成为黑箱的担忧。

- sets_up_cn：为RQ3和红旗句解释做铺垫。

- evidence_pointer：Section 3.2 P2 S3-S5

### 30. Section 4 P1 S1-S4

- order：30

- section：Section 4

- locator：Section 4 P1 S1-S4

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：文本必须转换成数值向量；BOW简单但会破坏词序，因此考虑预测式神经嵌入。

- rhetorical_function_cn：从文本表示的技术需求过渡到方法选择。

- depends_on_cn：BOW局限。

- sets_up_cn：具体介绍word2vec和HAN。

- evidence_pointer：Section 4 P1 S1-S4

### 31. Section 4.1 P1 S2-S5

- order：31

- section：Section 4.1

- locator：Section 4.1 P1 S2-S5

- move_code：DESIGN_FEATURE

- paraphrase_cn：word2vec生成低维稠密向量并保持语义和句法相似性；本文HAN使用Google News 300维词向量。

- rhetorical_function_cn：说明输入表示的选定。

- depends_on_cn：文本向量化的需要。

- sets_up_cn：支撑后续HAN性能的解释。

- evidence_pointer：Section 4.1 P1 S2-S5

### 32. Section 4.2 P2 S2-S4

- order：32

- section：Section 4.2

- locator：Section 4.2 P2 S2-S4

- move_code：DESIGN_FEATURE

- paraphrase_cn：LSTM的门结构使模型能选择性记住或遗忘信息，从而学习长期依赖。

- rhetorical_function_cn：解释为何用LSTM作为HAN编码器。

- depends_on_cn：文本序列建模需要。

- sets_up_cn：引入HAN的双向LSTM设定。

- evidence_pointer：Section 4.2 P2 S2-S4

### 33. Section 4.3 P1 S1-S4

- order：33

- section：Section 4.3

- locator：Section 4.3 P1 S1-S4

- move_code：THEORY_INTRO

- paraphrase_cn：语言的层次结构要求在词、句、文档上建模，HAN借此识别词在句中、句在文档中的重要性。

- rhetorical_function_cn：从语言结构理论过渡到模型设计原则。

- depends_on_cn：深度学习文本分类背景。

- sets_up_cn：详细描述HAN的词级和句级流程。

- evidence_pointer：Section 4.3 P1 S1-S4

### 34. Section 4.3 P3 S1-S3

- order：34

- section：Section 4.3

- locator：Section 4.3 P3 S1-S3

- move_code：DESIGN_FEATURE

- paraphrase_cn：先由双向LSTM生成词注释，再经注意力机制输出词重要性权重，加权求和得到句子向量。

- rhetorical_function_cn：具体展示词级编码和注意力操作。

- depends_on_cn：语言层次结构原则。

- sets_up_cn：为句子级编码和分类层提供组件。

- evidence_pointer：Section 4.3 Word Level/Word Attention

### 35. Section 4.3 Sentence Level and Sentence Encoder/Attention

- order：35

- section：Section 4.3

- locator：Section 4.3 Sentence Level and Sentence Encoder/Attention

- move_code：DESIGN_FEATURE

- paraphrase_cn：句子向量再输入双向LSTM，并通过句级注意力生成文档向量，最后经softmax输出舞弊概率。

- rhetorical_function_cn：完成由词到文档的层次表示。

- depends_on_cn：词级注意力输出。

- sets_up_cn：说明文档向量如何用于分类和注意力解释。

- evidence_pointer：Section 4.3 Sentence Level

### 36. Section 4.3 final P2-S1

- order：36

- section：Section 4.3

- locator：Section 4.3 final P2-S1

- move_code：DESIGN_FEATURE

- paraphrase_cn：HAN的200维文档向量与47个财务比率拼接后输入稠密层，再经softmax输出舞弊概率。

- rhetorical_function_cn：描述FIN+TXT的模型输入融合方式。

- depends_on_cn：文档向量和财务比率数据。

- sets_up_cn：直接支撑RQ1的数据组合实验。

- evidence_pointer：Section 4.3 final paragraph

### 37. Section 4.4 P2 S1-S3

- order：37

- section：Section 4.4

- locator：Section 4.4 P2 S1-S3

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：以往研究强调灵敏度优于特异度，因为漏检与误报的成本不同；F2-score比F1更重视灵敏度。

- rhetorical_function_cn：解释指标选择的成本逻辑。

- depends_on_cn：Hajek的成本估计。

- sets_up_cn：使后文结果以F2和AUC为主要讨论对象。

- evidence_pointer：Section 4.4 P2 S1-S3

### 38. Section 4.4 P3 S1-S3

- order：38

- section：Section 4.4

- locator：Section 4.4 P3 S1-S3

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：选择最大化灵敏度与假正率之差的阈值；HAN最优阈值约0.03。

- rhetorical_function_cn：提供可复现的决策规则。

- depends_on_cn：成本不对称和F2指标。

- sets_up_cn：为预测概率转化为审计行动提供依据。

- evidence_pointer：Section 4.4 P3 S1-S3

### 39. Section 5 P1 S1-S3

- order：39

- section：Section 5

- locator：Section 5 P1 S1-S3

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：舞弊数据存在严重类别不平衡，SEC年报中舞弊与非舞弊比例约为1:250；本文使用208舞弊与7341非舞弊，是带文本成分的最大数据集。

- rhetorical_function_cn：用数据规模证明研究的数据贡献。

- depends_on_cn：表1中的样本量对比。

- sets_up_cn：说明数据构建和欠采样的必要性。

- evidence_pointer：Section 5 P1 S1-S3

### 40. Section 5.1 P1 S1-S4

- order：40

- section：Section 5.1

- locator：Section 5.1 P1 S1-S4

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：基于AAER诉讼文件标注舞弊，方法简单、可复制，并避免主观分类偏差。

- rhetorical_function_cn：为标签可信度提供辩护。

- depends_on_cn：SEC执法文件。

- sets_up_cn：为数据集的外部有效性提供依据。

- evidence_pointer：Section 5.1 P1 S1-S4

### 41. Section 5.1 P1 S5-S6

- order：41

- section：Section 5.1

- locator：Section 5.1 P1 S5-S6

- move_code：PHENOMENON

- paraphrase_cn：作者筛选1999–2019年AAER中涉及舞弊和10-K的案例，并采用二元舞弊分类。

- rhetorical_function_cn：描述具体标注规则。

- depends_on_cn：AAER作为标签源。

- sets_up_cn：得到最终样本量。

- evidence_pointer：Section 5.1 P1 S5-S6

### 42. Section 5.2 P1 S1-S4

- order：42

- section：Section 5.2

- locator：Section 5.2 P1 S1-S4

- move_code：DESIGN_FEATURE

- paraphrase_cn：语言特征包括否定词、认知不确定性、积极/消极情绪、可读性指数和句子长度等先验线索。

- rhetorical_function_cn：说明LING数据集的构成。

- depends_on_cn：文本线索文献。

- sets_up_cn：为LING数据作为传统基线提供定义。

- evidence_pointer：Section 5.2 P1 S1-S4

### 43. Section 5.3 P1 S1-S4

- order：43

- section：Section 5.3

- locator：Section 5.3 P1 S1-S4

- move_code：DESIGN_FEATURE

- paraphrase_cn：使用基于Dechow和Beneish公式的47个财务预测变量，捕捉财务困境和管理层错报动机。

- rhetorical_function_cn：说明财务特征来源。

- depends_on_cn：财务舞弊文献。

- sets_up_cn：作为FIN基线及FIN+TXT组合的财务部分。

- evidence_pointer：Section 5.3 P1 S1-S4

### 44. Section 5.4 P1 S1-S4

- order：44

- section：Section 5.4

- locator：Section 5.4 P1 S1-S4

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：按1:4比例欠采样平衡正负类，并按年份和行业分层，以控制经济条件、法规和行业差异。

- rhetorical_function_cn：说明平衡策略及其合理性。

- depends_on_cn：数据严重不平衡。

- sets_up_cn：为分类比较提供公平样本。

- evidence_pointer：Section 5.4 P1 S1-S4

### 45. Section 6 P1 S1-S2

- order：45

- section：Section 6

- locator：Section 6 P1 S1-S2

- move_code：STUDY_OVERVIEW

- paraphrase_cn：通过实证分析回答RQ1和RQ2，比较分类模型在财务、语言、全文及组合数据上的表现。

- rhetorical_function_cn：开始呈现主体实验结果。

- depends_on_cn：模型与数据设计。

- sets_up_cn：引出表2结果。

- evidence_pointer：Section 6 P1 S1-S2

### 46. Section 6.1 P1 S2-S3

- order：46

- section：Section 6.1

- locator：Section 6.1 P1 S2-S3

- move_code：RESULT

- paraphrase_cn：在财务数据上，RF和XGB等树模型在AUC和准确率上表现突出。

- rhetorical_function_cn：报告财务基线结果。

- depends_on_cn：表2的FIN列。

- sets_up_cn：与后续文本模型比较。

- evidence_pointer：Section 6.1 P1 S2-S3

### 47. Section 6.1 P1 S8-S10

- order：47

- section：Section 6.1

- locator：Section 6.1 P1 S8-S10

- move_code：RESULT

- paraphrase_cn：F1/F2显示XGB优于其他模型，且XGB是此前舞弊检测未使用的方法。

- rhetorical_function_cn：突出新引入模型的价值。

- depends_on_cn：表2的F2列。

- sets_up_cn：为后续对先进ML方法的讨论做铺垫。

- evidence_pointer：Section 6.1 P1 S8-S10

### 48. Section 6.2 P1 S5-S7

- order：48

- section：Section 6.2

- locator：Section 6.2 P1 S5-S7

- move_code：RESULT

- paraphrase_cn：单独语言特征上，模型表现弱于财务数据，但差距不大，说明语言与舞弊行为存在强关联。

- rhetorical_function_cn：报告LING结果并解释意义。

- depends_on_cn：表2的LING列。

- sets_up_cn：为FIN+LING组合的结果做参照。

- evidence_pointer：Section 6.2 P1 S5-S7

### 49. Section 6.2 P2 S1-S3

- order：49

- section：Section 6.2

- locator：Section 6.2 P2 S1-S3

- move_code：RESULT

- paraphrase_cn：FIN+LING使多数分类器AUC提升，但准确率略有下降，说明两类数据可能向分类器提供冲突信号，总体仍是改进。

- rhetorical_function_cn：解读组合数据的非单调效果。

- depends_on_cn：表2的FIN+LING列。

- sets_up_cn：为FIN+TXT中更复杂的信息融合做铺垫。

- evidence_pointer：Section 6.2 P2 S1-S3

### 50. Section 6.3 P2 S1-S6

- order：50

- section：Section 6.3

- locator：Section 6.3 P2 S1-S6

- move_code：RESULT

- paraphrase_cn：全文文本TXT比LING显著提升所有模型，尤其ANN在准确率和F2上表现良好，说明全文内容比手工语言特征更丰富。

- rhetorical_function_cn：报告TXT阶段结果并解释提升来源。

- depends_on_cn：表2的TXT列。

- sets_up_cn：为HAN的出现提供对比基础。

- evidence_pointer：Section 6.3 P2 S1-S6

### 51. Section 6.3 P2 S9-S11

- order：51

- section：Section 6.3

- locator：Section 6.3 P2 S9-S11

- move_code：RESULT

- paraphrase_cn：HAN在TXT设置下灵敏度仅次于SVM，且其优异表现可归因于提取文档内上下文相似性的能力。

- rhetorical_function_cn：突出HAN在TXT上的竞争力。

- depends_on_cn：表2的TXT HAN行。

- sets_up_cn：引出FIN+TXT核心结果。

- evidence_pointer：Section 6.3 P2 S9-S11

### 52. Section 6.3 P3 S1-S3

- order：52

- section：Section 6.3

- locator：Section 6.3 P3 S1-S3

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：FIN+TXT的输入设置有两种：基准模型直接拼接向量，HAN和GPT-2采用两阶段建模，即先用文本模型输出概率，再与财务数据合并。

- rhetorical_function_cn：说明不同DL模型的融合方式不同。

- depends_on_cn：模型架构差异。

- sets_up_cn：帮助解释HAN表现和GPT-2表现差异。

- evidence_pointer：Section 6.3 P3 S1-S3

### 53. Section 6.3 P5 S1-S4

- order：53

- section：Section 6.3

- locator：Section 6.3 P5 S1-S4

- move_code：RESULT

- paraphrase_cn：HAN在FIN+TXT上取得最高AUC 92.64%和最高灵敏度90%，成为推荐的舞弊检测方案；GPT-2加财务数据提升不大，说明预训练嵌入选择很重要。

- rhetorical_function_cn：报告核心结果并指出嵌入选择的影响。

- depends_on_cn：表2的FIN+TXT列。

- sets_up_cn：为下一节解释HAN的注意力机制提供性能基础。

- evidence_pointer：Section 6.3 P5 S1-S4

### 54. Section 6.3 P6 S1-S2

- order：54

- section：Section 6.3

- locator：Section 6.3 P6 S1-S2

- move_code：TRANSITION

- paraphrase_cn：HAN的结果回答了RQ1和RQ2，并能提供解释，下一节将深入探索。

- rhetorical_function_cn：把预测结果引向可解释性。

- depends_on_cn：HAN的性能优势。

- sets_up_cn：引导读者进入解释和决策支持部分。

- evidence_pointer：Section 6.3 P6 S1-S2

### 55. Section 7 P1 S3-S5

- order：55

- section：Section 7

- locator：Section 7 P1 S3-S5

- move_code：CONTEXT

- paraphrase_cn：SOX要求MD&A充分披露关键会计估计和政策，但研究显示MD&A长度增加而信息内容或语言风格并未变化。

- rhetorical_function_cn：说明MD&A审查监管背景下文本分析仍未充分发挥作用。

- depends_on_cn：SOX和MD&A政策背景。

- sets_up_cn：为红旗句子的实用价值提供背景。

- evidence_pointer：Section 7 P1 S3-S5

### 56. Section 7 P1 S8-S10

- order：56

- section：Section 7

- locator：Section 7 P1 S8-S10

- move_code：GAP

- paraphrase_cn：Hajek和Henriques只能生成绿旗值而无法得到红旗值，本文提出用文本元素作为红旗，并在词级和句级上实现。

- rhetorical_function_cn：明确可解释性贡献的独特之处。

- depends_on_cn：前文的可解释性缺口。

- sets_up_cn：为词级和句级分析做铺垫。

- evidence_pointer：Section 7 P1 S8-S10

### 57. Section 7 P2 S1-S2

- order：57

- section：Section 7

- locator：Section 7 P2 S1-S2

- move_code：MECHANISM

- paraphrase_cn：舞弊者可操纵内容使文字接近真实，因此只凭内容词可能过度简单；句级指标因复杂而不易被操纵。

- rhetorical_function_cn：论证句级红旗优于词级红旗。

- depends_on_cn：词级红旗可能失效的担忧。

- sets_up_cn：支撑7.2节句级分析。

- evidence_pointer：Section 7 P2 S1-S2

### 58. Section 7.1 P1 S1-S4

- order：58

- section：Section 7.1

- locator：Section 7.1 P1 S1-S4

- move_code：STUDY_OVERVIEW

- paraphrase_cn：用lime解释RF词级作用，并提取HAN注意力词权重，比较两类红旗词表。

- rhetorical_function_cn：介绍词级可解释性分析。

- depends_on_cn：HAN注意力可提取词权重。

- sets_up_cn：报告词级结果。

- evidence_pointer：Section 7.1 P1 S1-S4

### 59. Section 7.1 P3 S1-S3

- order：59

- section：Section 7.1

- locator：Section 7.1 P3 S1-S3

- move_code：RESULT

- paraphrase_cn：RF和HAN各有不同的红旗词，仅15个重叠词，且词表含义模糊、易被快速适应和规避。

- rhetorical_function_cn：报告词级结果并指出其局限性。

- depends_on_cn：词级分析结果。

- sets_up_cn：为转向句级分析提供理由。

- evidence_pointer：Section 7.1 P3 S1-S3

### 60. Section 7.2 P1 S2-S3

- order：60

- section：Section 7.2

- locator：Section 7.2 P1 S2-S3

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：提取200份舞弊报告的句级注意力权重，每份取前10句，并以平均权重0.05和最大0.61作为标记规则。

- rhetorical_function_cn：说明句级红旗的生成方法。

- depends_on_cn：HAN句级注意力。

- sets_up_cn：展示句级高亮图。

- evidence_pointer：Section 7.2 P1 S2-S3

### 61. Section 7.2 P2 S1-S4

- order：61

- section：Section 7.2

- locator：Section 7.2 P2 S1-S4

- move_code：REQUIREMENT

- paraphrase_cn：建议两阶段决策支持：先用HAN概率判断舞弊风险，再用高亮句子指导审计。

- rhetorical_function_cn：把技术输出转化为审计流程要求。

- depends_on_cn：HAN预测和高亮句子。

- sets_up_cn：支撑结论中的决策支持贡献。

- evidence_pointer：Section 7.2 P2 S1-S4

### 62. Section 7.2 P2 S5

- order：62

- section：Section 7.2

- locator：Section 7.2 P2 S5

- move_code：BOUNDARY_CONDITION

- paraphrase_cn：鉴于MD&A很长且人工精力有限，可视化指导能提高舞弊检测准确性。

- rhetorical_function_cn：为应用场景和边界作说明。

- depends_on_cn：审计工作量大这一现实。

- sets_up_cn：为贡献声明提供务实理由。

- evidence_pointer：Section 7.2 P2 S5

### 63. Section 8 P1 S1

- order：63

- section：Section 8

- locator：Section 8 P1 S1

- move_code：GAP

- paraphrase_cn：文献中HJ和Throckmorton等曾结合财务和语言数据，但没有发现结合财务和全文文本的研究。

- rhetorical_function_cn：在讨论开头重新强调研究空白。

- depends_on_cn：文献综述和实验结果。

- sets_up_cn：将结果置于填补空白的叙事中。

- evidence_pointer：Section 8 P1 S1

### 64. Section 8 P2 S1-S3

- order：64

- section：Section 8

- locator：Section 8 P2 S1-S3

- move_code：RESULT

- paraphrase_cn：SVM在多数设置表现良好，RF在BOW上最佳，但只有HAN在FIN+TXT中表现出独特的提取能力。

- rhetorical_function_cn：总结不同模型的相对位置。

- depends_on_cn：表2结果。

- sets_up_cn：为HAN贡献定位。

- evidence_pointer：Section 8 P2 S1-S3

### 65. Section 8 P2 S4

- order：65

- section：Section 8

- locator：Section 8 P2 S4

- move_code：THEORY_RETURN

- paraphrase_cn：HAN的高检出率支持Zhou等关于文本欺骗检测需要上下文信息的论点。

- rhetorical_function_cn：将结果回接到先前理论，提升理论意义。

- depends_on_cn：HAN的实验结果。

- sets_up_cn：构成机制贡献。

- evidence_pointer：Section 8 P2 S4

### 66. Section 8 P3 S1

- order：66

- section：Section 8

- locator：Section 8 P3 S1

- move_code：RESULT

- paraphrase_cn：HAN提取的语言变量与TF-IDF文本变量在结合财务比率时显著增加检测价值。

- rhetorical_function_cn：用简洁结论重申RQ1答案。

- depends_on_cn：AUC比较结果。

- sets_up_cn：支撑数据组合贡献。

- evidence_pointer：Section 8 P3 S1

### 67. Section 8 P3 S2-S3

- order：67

- section：Section 8

- locator：Section 8 P3 S2-S3

- move_code：BOUNDARY_CONDITION

- paraphrase_cn：不同模型在不同数据上的性能变化说明模型捕捉不同信号，集成多种模型可能比选择单一模型更合适。

- rhetorical_function_cn：提出边界条件：不存在在所有数据组合上的统治模型。

- depends_on_cn：表2的异质性。

- sets_up_cn：为实践建议提供细化。

- evidence_pointer：Section 8 P3 S2-S3

### 68. Section 8 P4 S1-S3

- order：68

- section：Section 8

- locator：Section 8 P4 S1-S3

- move_code：RESULT

- paraphrase_cn：词级红旗大多被两种模型识别为不同词，脱离上下文可能误导；句级标记因更高复杂性而更稳健。

- rhetorical_function_cn：总结可解释性分析并强调句级价值。

- depends_on_cn：词级和句级分析。

- sets_up_cn：为结论中的决策支持贡献做铺垫。

- evidence_pointer：Section 8 P4 S1-S3

### 69. Section 9 P1 S1-S3

- order：69

- section：Section 9

- locator：Section 9 P1 S1-S3

- move_code：GAP

- paraphrase_cn：结论重申：很少研究结合财务和语言信息，没有发现使用DL文本表示检测报表舞弊的研究。

- rhetorical_function_cn：再次框定全文贡献对象。

- depends_on_cn：全文工作。

- sets_up_cn：引出最终贡献陈述。

- evidence_pointer：Section 9 P1 S1-S3

### 70. Section 9 P2 S1-S3

- order：70

- section：Section 9

- locator：Section 9 P2 S1-S3

- move_code：CONTRIBUTION

- paraphrase_cn：结果证明HAN在AUC上显著提升，适合识别舞弊案例，而多数ML模型在正确识别非舞弊上更好但会漏掉更多舞弊。

- rhetorical_function_cn：把技术结果转化为论文贡献。

- depends_on_cn：表2结果。

- sets_up_cn：引导出对审计和利益相关者的价值。

- evidence_pointer：Section 9 P2 S1-S3

### 71. Section 9 P2 S4-S5

- order：71

- section：Section 9

- locator：Section 9 P2 S4-S5

- move_code：CONTRIBUTION

- paraphrase_cn：MD&A文本经HAN提取增强预测准确性，尤其是产生红旗信号；句级指示能让审计师快速定位触发舞弊判断的文本片段。

- rhetorical_function_cn：总结全文核心贡献。

- depends_on_cn：实证结果和解释分析。

- sets_up_cn：形成论文收束。

- evidence_pointer：Section 9 P2 S4-S5

## 写作技术

- gap_construction_cn：作者用文献表（Table 1）展示现状，明确指出两个层面缺口：技术层面没有DL文本建模用于舞弊检测；证据层面没有将完整文本与财务数据结合，且缺乏可解释的红旗信号。这一缺口不是“没人研究”，而是“现有方法无法处理MD&A全文的上下文结构”和“可解释性未解决”。

- signposting_cn：在研究设计节明确列出RQ1/RQ2/RQ3；在评价节反复预告“下一节将解释”；在结论中再次回指RQ。全文用“这回答了RQ1和RQ2”和“将深入探索”等方式为读者导航。

- transition_logic_cn：从预测结果到可解释性使用“尽管性能优异，但实践需要解释”的过渡；从词级到句级使用“词级不稳定易操纵”的过渡；从数据组合到模型性能使用“先基准后增量”的逐步引导。

- claim_evidence_rhythm_cn：每个实验段落先报结果，再用一至两句解释其意义，接着回指表2或文献。例如6.3节先报告TXT提升，再解释提升来自全文内容，最后与HAN/GPT-2关联。结论部分的贡献声明都依赖于表2和解释示例，但部分解释性声明缺少直接证据。

- benchmark_narrative_cn：benchmark不是简单罗列，而是以FIN为起点，逐步加入LING、TXT和财务组合；每一列都给出与前一列的delta A UC/F1，使读者看到每一步信息源增加带来的边际价值。HN和GPT-2作为DL代表嵌入到TXT和FIN+TXT中，与BOW模型形成对照。

- theory_return_cn：作者在讨论中把HAN的性能优势归结为上下文依赖的欺骗线索，引用Zhou等强化这一观点；同时用句级红旗的稳健性回应“内容可被操纵”的担忧，使技术结果回接到心理学理论。

- contribution_positioning_cn：贡献被定位为：方法新颖（首次用HAN查舞弊）、数据组合完整（FIN+TXT）、可解释的审计决策支持（红旗句子）。每个贡献都对应一个RQ，避免贡献泛化。

- novelty_protection_cn：作者通过多模型、多数据组合的全面比较，让HAN的AUC优势看起来不是偶然；通过引入GPT-2对照说明并非所有DL都有效，从而突出HAN架构；通过从词级到句级的递进，把一次性性能结果升华为可复用的设计原则（上下文敏感文本特征+句级可解释输出）。

## 可复用研究与写作程序

### structure_steps

#### 1. 1

- step：1

- writing_job_cn：用损失金额、审计师低检出率等现实数据建立问题严重性，并定义术语。

- research_job_cn：选择明确的舞弊定义和检测场景。

- required_evidence_cn：权威报告或统计数字，能显示现有检测的不足。

- transition_to_next_cn：从实践需求转向“已有方法能否满足”的文献评述。

#### 2. 2

- step：2

- writing_job_cn：用文献表归纳现有方法的维度（数据、模型、指标、国家），指出技术缺口和证据缺口。

- research_job_cn：系统检索和分类前人研究，尤其是最近工作。

- required_evidence_cn：能证明“现有方法未处理完整文本/未使用DL/未结合多数据源/未给出红旗”的具体引用。

- transition_to_next_cn：由缺口引出研究问题和贡献点。

#### 3. 3

- step：3

- writing_job_cn：将缺口转化为可回答的RQ，并预告模型、数据和评价指标。

- research_job_cn：确定要比较的数据组合和模型集合，选定成本敏感指标。

- required_evidence_cn：每个RQ有后续实验结果可以直接回答。

- transition_to_next_cn：介绍方法论和数据集。

#### 4. 4

- step：4

- writing_job_cn：说明数据来源、标注规则、不平衡处理方法，并强调数据规模或外部可信性。

- research_job_cn：构建检测数据集，做好标签和样本划分。

- required_evidence_cn：数据规模、标注来源、平衡前后统计。

- transition_to_next_cn：转入模型设计。

#### 5. 5

- step：5

- writing_job_cn：说明文本表示选择、DL架构、融合方式和超参数。

- research_job_cn：实现HAN、基准DL和传统ML模型。

- required_evidence_cn：模型可运行且能输出概率用于阈值和注意力解释。

- transition_to_next_cn：呈现分类比较结果。

#### 6. 6

- step：6

- writing_job_cn：以表格报告多模型×多数据组合的指标，并逐节解读FIN、LING、TXT、组合数据的边际贡献。

- research_job_cn：执行离线比较，记录AUC/F1/F2等。

- required_evidence_cn：测试集结果和一个明确的最优模型。

- transition_to_next_cn：由最优模型引出可解释性。

#### 7. 7

- step：7

- writing_job_cn：用可解释工具或注意力权重呈现红旗信号，并说明其如何嵌入审计流程。

- research_job_cn：提取词级/句级解释，构造决策支持示例。

- required_evidence_cn：能展示具体红旗词/句的示例，并论证比替代方案更稳健。

- transition_to_next_cn：在讨论中回到理论和实践边界。

#### 8. 8

- step：8

- writing_job_cn：在讨论中重新闭合引言缺口，重述RQ答案，声明贡献，并列出限制。

- research_job_cn：检验哪些贡献有直接证据，哪些只是解释性延展。

- required_evidence_cn：与引言缺口对应的明确结果。

- transition_to_next_cn：结束。

### most_transferable_moves_cn

1. 用逐级数据组合（FIN->LING->FIN+LING->TXT->FIN+TXT）展示信息源边际价值。

2. 将RQ拆成数据/模型/解释三维，评价设计直接跟随RQ。

3. 用成本不对称论证F2和灵敏度优先评价。

4. 将解释性从词级推进到句级，避免一词一义陷阱。

5. 使用“上下文依赖欺骗线索”理论解释结果，而不用发明新模型机制。

### resource_intensive_or_nonstandard_parts_cn

1. AAER标注的多年SEC年报整理需要法律文本匹配和人工核实，难以低成本复制。

2. Compustat财务数据需要商业数据库许可。

3. HAN训练与超参数调整需要DL算力和NLP工程经验。

4. 句级解释演示需要人工可视化MD&A页面并与审计场景结合。

### what_not_to_copy_superficially_cn

1. 不能只声称“深度学习优于词袋”而不做多模型、多数据组合的对照。

2. 不能把词级红旗列表当作稳定规则，而需验证其对抗操纵的稳健性。

3. 不能把HAN的成功完全归因于注意力和层次结构，除非做消融或机制对照。

4. 不能把句级红旗说成能提高审计准确率，除非有审计师行为实验。

- single_best_description_of_the_routine_cn：用大规模历史年报数据，把一个NLP中的成熟架构（HAN）迁移到舞弊检测任务，通过多维数据组合和多模型benchmark证明其有效性，再借注意力输出构建可操作的审计红旗工具，最后用“上下文依赖欺骗线索”这一理论把技术结果包装成可推广的设计知识。

## 分析边界

输入全文存在OCR噪声和明显文字错乱（如abstract中乱码、某些段落句子断裂、表格公式显示不全），可能影响某些段落释义；缺少页码和附录细节；文中引用的在线附录不可见；无法从本文确认精确的页级位置。因此所有位置证据基于章节/段落/图表名，而非页码。
