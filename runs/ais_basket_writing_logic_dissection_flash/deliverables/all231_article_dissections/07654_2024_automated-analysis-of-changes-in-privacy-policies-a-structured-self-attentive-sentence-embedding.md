# Automated Analysis of Changes in Privacy Policies: a Structured Self-Attentive Sentence Embedding Approach

- 作者：Fangyu Lin; Sagar Samtani; Hongyi Zhu; Laura Brandimarte; Hsinchun Chen
- 年份 / 期刊：2024 / MIS Quarterly
- DOI：10.25300/misq/2024/17115
- 源文件：07654_2024_automated-analysis-of-changes-in-privacy-policies-a-structured-self-attentive-sentence-embedding.md
- 论文主类型：build_evaluate_design_science
- 主导写作弧线：requirements_build_evaluate_design_principles
- 置信度：0.95

## 文章级论证概况

- 核心问题：如何利用深度学习方法自动分析隐私政策在监管出台前后的变化，具体地，如何设计一种能对长篇隐私政策段落进行多标签数据实践标注的模型，以便帮助企业和监管者识别政策变化和潜在合规问题。

- 制品与设计：提出一个隐私政策演化分析框架，核心是自注意力标注系统SAAS。SAAS包含行级自注意力嵌入（RSE）和多标签分类器：RSE基于BiGRU和多头自注意力，并引入行级注意力（RWA）对每个头学到的方面进行加权；多标签分类器同时预测10个数据实践类别，通过共享表示学习类别间的共同特征。

- 客观结果：在OPP-115数据集上，SAAS的micro-averaged F1达到0.758，显著优于全部传统ML（最高0.721）和DL基线（最高0.750）；消融实验证实RWA和多标签分类器各有贡献；自动分段实验显示SAAS对分段方式不敏感；Amazon案例研究揭示其GDPR后的隐私政策将cookies信息转移到独立文档，可能增加用户查找负担，违反GDPR的"easily accessible"透明度原则。

- 核心贡献：作者声称的贡献包括一个遵循计算设计科学范式的隐私政策演化分析框架和SAAS方法，以及两个可复用的设计原则：一是区分复杂长文本中不同词/短语集合的区分性权重，二是多标签分类中利用标签间共同特征并共享参数；这些原则可为电商、健康和隐私领域的IT工件设计提供指导。

- 整篇论证链：论文从隐私监管日益严格、隐私政策变得冗长且无统一格式的现实问题出发，指出IS隐私研究偏向行为/经济视角而缺乏对政策文本本身的分析；随后梳理隐私政策分析文献，指出传统ML的BOW表示和现有DL方法（MLP、CNN、BERT）分别存在无法捕捉长距离依赖、忽略标签相关性或依赖大量微调数据等问题。作者基于SSASE和注意力机制，引入行级自注意力权重重分方面重要程度，并构造共享参数的多标签分类器，形成SAAS。通过四个基准实验（对比传统ML、对比DL、消融、手工/自动分段）逐层证明SAAS的技术性能、组件贡献和鲁棒性，再以Amazon的GDPR前后政策为案例论证实际价值。最后将结果抽象为设计原则，并讨论对公司、监管者及后续IS研究的启示。

## 类型与写作弧线判定

- 论文主类型判定：论文明确采用计算设计科学范式（Rai, 2017），设计了一个新的IT工件（隐私政策演化分析框架及SAAS），通过基准实验、消融分析和案例研究进行严格评价，并最终以设计原则的形式向IS知识库贡献可复用的设计知识，符合'构建-评价-设计知识'的设计科学套路。

- 主导写作弧线判定：作者首先基于领域需求（隐私政策文本特点、多标签标注、监管要求）和设计科学准则提出设计要求，然后构建SAAS，接着通过一系列基准和消融实验评价工件，最后将结果提升为两条通用设计原则，并讨论跨领域应用。整条主线是要求→构建→评价→设计原则。

## 研究开展程序

- study_or_phase_count：6

- 研究阶段总序列：第1阶段通过领域需求和文献分析完成框架与SAAS设计；第2、3阶段通过两类基准实验确立SAAS相对现有方法的性能优势，并基于示例段解释机制；第4阶段消融实验隔离RWA和多标签分类器的各自贡献；第5阶段验证SAAS在自动分段下的稳健性；第6阶段通过Amazon案例研究展示框架在实际监管分析中的实用性。每个阶段解决上一阶段留下的不确定性问题，层层递进。

### studies_or_phases

#### 1. 需求分析与SAAS设计构建

- order：1

- name_cn：需求分析与SAAS设计构建

- question_cn：如何基于领域需求设计一个能自动标注隐私政策段落的深度学习方法？

- inputs_and_setting_cn：隐私政策分析文献、OPP-115数据集描述、SSASE和注意力机制文献、设计科学指南。

- designed_or_compared_object_cn：SAAS系统，包括RSE模块（BiGRU+multi-head attention+RWA）和多标签分类器。

- baseline_control_or_counterfactual_cn：无对照，设计阶段参考SSASE和注意力机制作为知识基础。

##### objective_metrics

（空）

- analysis_method_cn：需求分析、设计科学准则、架构设计（无定量评价）。

- main_result_cn：提出了完整的SAAS架构，明确了RWA和多标签分类器两个核心创新点。

- argumentative_role_cn：将领域需求和文献缺口转化为具体设计决策，为后续实验提供研究对象。

- remaining_uncertainty_cn：设计是否真的优于现有方法尚不明确。

- link_to_next_phase_cn：通过基准实验（实验1和2）检验SAAS相对于现有ML/DL模型的性能。

##### evidence_pointers

1. Section 'Proposed Privacy Policy Evolution Analytics Framework'

2. Figure 4

3. Figure 5

#### 2. 实验1：SAAS vs 传统机器学习模型

- order：2

- name_cn：实验1：SAAS vs 传统机器学习模型

- question_cn：SAAS是否优于基于Doc2Vec和TF-IDF表示的传统机器学习模型？

- inputs_and_setting_cn：OPP-115中3,749个段落，5×2交叉验证，使用迭代分层抽样。

- designed_or_compared_object_cn：SAAS vs 9个传统ML模型（LR, SVM, RF, NB, KNN × Doc2Vec/TF-IDF）。

- baseline_control_or_counterfactual_cn：Doc2Vec+LR/SVM/RF/KNN；TF-IDF+LR/SVM/RF/NB/KNN。

##### objective_metrics

1. micro-averaged precision

2. micro-averaged recall

3. micro-averaged F1-score

4. micro-averaged Hamming Loss

- analysis_method_cn：5×2交叉验证，配对t检验。

- main_result_cn：SAAS的micro-F1=0.758、micro-recall=0.714、micro-HL=0.058均显著优于所有传统ML基线（最高F1=0.721，TF-IDF+LR）。

- argumentative_role_cn：证明SAAS比被广泛使用的传统ML方法更有效，并指出这些方法因BOW表示而受限。

- remaining_uncertainty_cn：与深度学习方法相比性能如何？

- link_to_next_phase_cn：引出实验2与DL方法比较，检验SAAS相对更先进的模型是否仍有优势。

##### evidence_pointers

1. Table 7

2. Table 8

3. Section 'Experiment 1 Results'

#### 3. 实验2：SAAS vs 深度学习方法

- order：3

- name_cn：实验2：SAAS vs 深度学习方法

- question_cn：SAAS是否优于CNN、单向/双向RNN和SSASE等深度学习方法？

- inputs_and_setting_cn：OPP-115的3,749个段落，14个DL模型，5×2交叉验证。

- designed_or_compared_object_cn：SAAS vs CNN，LSTM/GRU（+Max/Mean pooling），BiLSTM/BiGRU（+Max/Mean pooling），10个独立SSASE和SSASE+多标签分类器。

- baseline_control_or_counterfactual_cn：10个深度模型基线，2个SSASE变体。

##### objective_metrics

1. micro-averaged precision

2. micro-averaged recall

3. micro-averaged F1-score

4. micro-averaged Hamming Loss

- analysis_method_cn：5×2交叉验证，配对t检验。

- main_result_cn：SAAS在micro-F1=0.758显著优于全部DL基线（CNN=0.745，BiLSTM+Max=0.742，SSASE+multi-label=0.750）。

- argumentative_role_cn：证明SAAS优于最具代表性的深度模型，尤其是两个SSASE变体，指向RWA和多标签分类器的价值。

- remaining_uncertainty_cn：RWA和多标签分类器各自起到多大作用？

- link_to_next_phase_cn：通过消融分析（实验3）分离各个组件的贡献。

##### evidence_pointers

1. Table 9

2. Table 10

3. Section 'Experiment 2 Results'

#### 4. 实验3：消融分析

- order：4

- name_cn：实验3：消融分析

- question_cn：RWA和多标签分类器对SAAS性能的贡献是什么？

- inputs_and_setting_cn：三个消融变体：SAAS without RWA，SAAS replacing RWA with MLP，10个独立SAAS（每个类别一个）。

- designed_or_compared_object_cn：SAAS vs 三个消融变体。

- baseline_control_or_counterfactual_cn：无RWA变体、MLP替代变体、独立二分类变体。

##### objective_metrics

1. micro-averaged precision

2. micro-averaged recall

3. micro-averaged F1-score

4. micro-averaged Hamming Loss

- analysis_method_cn：5×2交叉验证，配对t检验。

- main_result_cn：完整SAAS在micro-F1=0.758显著优于无RWA（0.750）、MLP替代（0.747）和10个独立SAAS（0.718）。

- argumentative_role_cn：验证RWA的动态加权与多标签分类器的共享表示学习都是性能提升的必要来源。

- remaining_uncertainty_cn：在自动分段的情况下，SAAS的性能是否会下降？

- link_to_next_phase_cn：实验4检验自动化分段对SAAS的鲁棒性，为大规模应用提供证据。

##### evidence_pointers

1. Table 11

2. Section 'Experiment 3 Results'

#### 5. 实验4：人工分段 vs 自动分段

- order：5

- name_cn：实验4：人工分段 vs 自动分段

- question_cn：SAAS使用ST-Ro自动分段时，性能是否显著劣于使用人工分段？

- inputs_and_setting_cn：OPP-115原始人工分段 vs ST-Ro自动分段，5×2交叉验证，测试序列用ST-Ro合并相邻句子。

- designed_or_compared_object_cn：两种分段输入下的SAAS性能。

- baseline_control_or_counterfactual_cn：ground truth分段 vs 自动分段。

##### objective_metrics

1. micro-averaged precision

2. micro-averaged recall

3. micro-averaged F1-score

- analysis_method_cn：配对t检验，比较F1差异。

- main_result_cn：micro-F1分别为74.6%与73.7%，差异不显著，表明SAAS对自动分段稳健。

- argumentative_role_cn：确保SAAS可以应用于缺乏人工标注段落的真实大规模政策分析。

- remaining_uncertainty_cn：SAAS在实际监管变化检测中的效用和产出是否具有实践价值？

- link_to_next_phase_cn：通过Amazon GDPR案例研究将技术性能转化为真实世界洞见。

##### evidence_pointers

1. Section 'Experiment 4 Results'

#### 6. 案例研究：GDPR对Amazon隐私政策的影响

- order：6

- name_cn：案例研究：GDPR对Amazon隐私政策的影响

- question_cn：SAAS能否帮助识别Amazon隐私政策在GDPR前后的变化，并检测出潜在合规问题？

- inputs_and_setting_cn：Amazon 2014年3月与2021年2月的隐私政策文本；使用ST-Ro自动分段；SAAS预先在OPP-115上训练对段落标注；分析FP类段及注意力权重。

- designed_or_compared_object_cn：GDPR前和后Amazon隐私政策中FP段的内容与呈现方式。

- baseline_control_or_counterfactual_cn：前后对比，无外部对照组。

##### objective_metrics

1. 定性的注意力权重分析

2. 政策文本对比

- analysis_method_cn：五步案例研究：收集政策→ST-Ro分段→SAAS标注→选择FP类别→可视化注意力权重。

- main_result_cn：后GDPR政策中与cookies相关的FP段的高权重方面指向"Cookies Notice"独立文档，说明Amazon将关键信息移出主政策，可能增加用户查找和理解负担，违反GDPR透明度原则。

- argumentative_role_cn：展示框架的实际应用价值，将SAAS的自动标注能力转化为监管者可以使用的合规洞察。

- remaining_uncertainty_cn：该发现是否可推广到其他公司和法规？是否真的构成法律违规未经法定裁决验证？

- link_to_next_phase_cn：进入讨论和结论，将案例结果与设计原则和管理启示相结合。

##### evidence_pointers

1. Section 'Regulation Impact Detection: A Case on GDPR'

2. Table 12

## 各部分修辞架构

### abstract_moves

1. CONTEXT

2. PHENOMENON

3. RQ_OR_OBJECTIVE

4. DESIGN_FEATURE

5. STUDY_OVERVIEW

6. RESULT

7. CONTRIBUTION

### introduction_moves

1. CONTEXT

2. PRACTICAL_STAKES

3. PHENOMENON

4. LIMITATION

5. GAP

6. RQ_OR_OBJECTIVE

7. DESIGN_FEATURE

8. STUDY_OVERVIEW

### theory_and_knowledge_moves

1. PRIOR_KNOWLEDGE

2. LIMITATION

3. MECHANISM

4. GAP

### artifact_design_moves

1. STUDY_OVERVIEW

2. METHOD_JUSTIFICATION

3. DESIGN_FEATURE

4. MECHANISM

### evaluation_moves

1. METHOD_JUSTIFICATION

2. BENCHMARK_OR_CONTRAST

3. RESULT

4. ROBUSTNESS_OR_BOUNDARY_TEST

### discussion_and_contribution_moves

1. CONTEXT

2. CONTRIBUTION

3. BOUNDARY_CONDITION

4. LIMITATION_AND_FUTURE

## 理论/知识到设计的翻译

### 知识/理论基础

1. Structured Self-Attentive Sentence Embedding (SSASE)

2. Attention mechanisms

3. Multi-label classification (binary relevance and multi-task learning)

4. Computational design science guidelines

5. Privacy policy analysis domain knowledge (OPP-115, data practice categories)

- 理论—设计耦合：direct

- 耦合判定理由：作者从SSASE和注意力机制的已知属性直接推导出SAAS的设计：SSASE将所有方面等权重，因此设计RWA来区分方面重要性；binary relevance忽略标签相关性，因此设计共享参数的多标签分类器。这些设计选择随后通过消融实验和与SSASE变体的直接对比得到检验，属于前瞻性知识对设计的直接决定。

- 理论到设计翻译链：首先，SSASE的multi-head self-attention生成多个方面向量，但SSASE将这些方面等同对待，而隐私政策段落中某些方面（如“share”）对预测TP更具区分性，因此需要RWA按照方面对分类的贡献动态加权；其次，multi-label分类若按binary relevance独立预测每个类别会丢失类别间的相关性（如FP与TP频繁共现），因此需要共享参数的多标签分类器，同时优化10个二元任务并共同调整表示。将这两个设计整合到SAAS中，形成RSE+multi-label classifier的架构。

### mapping_table

#### 1. 1

- theory_or_knowledge_claim_cn：SSASE的多头注意力能捕捉段落的多个方面，但所有方面被等同对待；一些方面（如表示收集、共享的短语）对不同数据实践的区分性不同。

- mechanism_cn：方面级别的重要性差异：某些词/短语集合（方面）对特定类别标签的预测更有指示性，同等对待这些方面会稀释关键信号。

- design_requirement_cn：需要一种机制学习每个方面在分类中的贡献权重。

- artifact_choice_cn：设计行级注意力RWA：对segment embedding的每一行（方面）计算softmax权重，并用于加权矩阵的行。

- evaluated_contrast_cn：SAAS vs 无RWA的SSASE（消融）和替代RWA的MLP变体。

- objective_result_cn：SAAS的micro-F1=0.758显著高于无RWA（0.750）和MLP替代（0.747），p<0.001。

##### evidence_pointers

1. Table 11

#### 2. 2

- theory_or_knowledge_claim_cn：Binary relevance将多标签任务分解为独立二分类器，忽略标签间相关性；而隐私政策中的数据实践类别（如FP和TP）在段落中经常同时出现，存在语义和主题上的关联。

- mechanism_cn：标签相关性与共享表示：同时预测多个类别可以通过共享隐藏层正则化模型，避免过拟合低频类别并利用类别之间的共同语义。

- design_requirement_cn：需要让模型同时感知全部标签，并在训练中共享参数。

- artifact_choice_cn：在多标签分类器中，将扁平化后的加权段表示输入共享全连接层，输出10个sigmoid概率，并用binary cross entropy联合优化。

- evaluated_contrast_cn：SAAS vs 10个独立SAAS（每个类别一个）；SAAS vs SSASE+multi-label classifier（未加RWA）。

- objective_result_cn：SAAS的micro-F1=0.758显著高于10个独立SAAS（0.718）和SSASE+multi-label（0.750），p<0.001。

##### evidence_pointers

1. Table 9

2. Table 11

#### 3. 3

- theory_or_knowledge_claim_cn：BiRNN能捕捉长距离顺序依赖，而自注意力能捕捉非顺序全局依赖；两者结合（SSASE）在多类文本分类中有效，但在多标签数据实践标注中应用不足。

- mechanism_cn：长距离语义依赖和全局语义交互：隐私政策段落混合多个类别，需要同时理解局部短语的上下文和全局依赖性。

- design_requirement_cn：保留SSASE的双向递归和自注意力机制，并针对多标签任务适配。

- artifact_choice_cn：RSE选择BiGRU（比BiLSTM收敛更快），保留multi-head attention生成段嵌入，再叠加RWA。

- evaluated_contrast_cn：SAAS vs CNN、单向RNN、双向RNN池化方法及SSASE变体。

- objective_result_cn：SAAS在micro-F1=0.758显著高于CNN（0.745）、BiLSTM+Max（0.742）和SSASE变体（0.749/0.750）。

##### evidence_pointers

1. Table 9

## 评价逻辑

### evaluation_modes

1. offline benchmark experiments

2. ablation analysis

3. robustness test with automated segmentation

4. interpretive case study with attention weights

- why_these_evaluations_cn：需要先证明SAAS相对现有基线的整体性能（实验1/2），再隔离每个设计组件对性能的贡献（实验3），接着验证在接近真实应用条件下（自动分段）的鲁棒性（实验4），最后用案例研究展示工具在监管分析中的实践价值。多种评价模式共同构成从技术性能到实践效用的证据链。

- benchmark_and_contrast_chain_cn：实验1和实验2分别建立SAAS对传统ML和DL基线的优势；实验3通过消融证明优势来自RWA和多标签分类器；实验4通过更换分段方式检验鲁棒性；案例研究则把模型输出（注意力权重）转译成监管相关发现。每一步的对照组都逐步向真实应用条件靠近。

### claim_evidence_ledger

#### 1. SAAS的技术性能优于传统ML和DL基线。

- claim_cn：SAAS的技术性能优于传统ML和DL基线。

- evidence_cn：实验1表7和实验2表9显示在OPP-115上micro-F1=0.758，显著高于所有基线（p<0.05到0.001）。

##### evidence_pointers

1. Table 7

2. Table 9

#### 2. RWA是性能提升的必要组件。

- claim_cn：RWA是性能提升的必要组件。

- evidence_cn：消融实验表11显示去除RWA或替换为MLP后micro-F1显著下降（0.750/0.747 vs 0.758）。

##### evidence_pointers

1. Table 11

#### 3. 多标签分类器比独立二分类器更好。

- claim_cn：多标签分类器比独立二分类器更好。

- evidence_cn：10个独立SAAS的micro-F1=0.718，显著低于完整SAAS的0.758（表11）。

##### evidence_pointers

1. Table 11

#### 4. SAAS能识别被基线漏掉的复合标签实例。

- claim_cn：SAAS能识别被基线漏掉的复合标签实例。

- evidence_cn：表10展示了一个FP+TP段被SSASE只预测为FP，SAAS正确预测FP+TP，并在287个测试段中发现类似模式。

##### evidence_pointers

1. Table 10

#### 5. SAAS对自动分段具有外部效度。

- claim_cn：SAAS对自动分段具有外部效度。

- evidence_cn：实验4中与原OPP-115分段相比，ST-Ro自动分段下micro-F1差异不显著（74.6% vs 73.7%）。

##### evidence_pointers

1. Section 'Experiment 4 Results'

#### 6. 框架能检测隐私政策改变中的潜在合规问题。

- claim_cn：框架能检测隐私政策改变中的潜在合规问题。

- evidence_cn：Amazon案例中，SAAS的注意力权重指出post-GDPR政策将cookies信息放到外部文档，并引用GDPR Recitals 39和58支持结论（Table 12）。

##### evidence_pointers

1. Table 12

- internal_validity_strategy_cn：使用5×2交叉验证和配对t检验控制随机划分差异；采用迭代分层抽样处理多标签不平衡；在同一硬件和框架下运行所有模型；固定超参数进行消融，只改变目标组件；自动化分段实验使用同一训练协议。

- external_validity_strategy_cn：选择OPP-115这一在隐私政策分析中被广泛采用的数据集；对比模型涵盖经典ML、CNN、RNN和SSASE等主流方法；通过自动分段实验模拟大规模未分段政策；案例研究使用真实公司的前后政策文本，并向监管者与公司推广使用场景。

- what_is_not_actually_tested_cn：SAAS尚未在真实监管工作流中接受大范围部署测试；案例研究未获得法律裁决或监管机构对"违规"的正式认定，"可能违反"仅基于文本分析和GDPR条款；设计原则在电商、健康等其他领域的适用性只是理论推演，没有跨领域实验；低样本类别（如DR、PC、DNT）上SAAS未表现出统一优势，部分类别甚至不如TF-IDF基线。

## 贡献闭环

- technical_claim_cn：SAAS在OPP-115上micro-F1=0.758，比所有传统ML和DL基线高出统计显著幅度，尤其优于CNN和SSASE变体。

- artifact_claim_cn：SAAS中的RWA和多标签分类器是性能提升的核心设计组件，消融分析确认两者缺一不可。

- mechanism_claim_cn：RWA通过动态加权不同方面提高关键区分信号的权重；多标签分类器通过共享参数利用类别间相关性并正则化模型；BiGRU+attention则提供了长距离和全局语义捕捉。

- boundary_claim_cn：SAAS对自动分段稳健；在OPP-115上对FP、TP、UCC、UAED、DS、O等类别提升明显，但在数据样本极少的DR、PC、DNT上可能不优于TF-IDF基线；案例研究仅适用于类似Amazon的单一公司文本，不能直接断言普遍合规。

- reusable_design_knowledge_cn：两个设计原则：①在复杂长文本中差异化处理不同词/短语集合的区分性，减少等权方面对预测的干扰；②多标签分类中共享参数、联合优化所有标签，利用标签间共同特征提高低资源类别的泛化能力。

- theoretical_contribution_cn：将SSASE从单一多类分类扩展为多标签分类，并引入行级注意力作为方面级加权机制；为注意力机制在IS文本分析任务中的设计提供了基于多标签场景的实例和边界。

- how_discussion_closes_intro_gap_cn：引言指出IS隐私研究缺乏分析政策文本的技术工具，讨论部分将SAAS定位为填补这一空白的IT工件，并将案例结果与GDPR合规联系起来；同时将SAAS的技术特征抽象为设计原则，回应了引言中"需要新IT工具"的号召。

- overclaim_or_unsupported_leaps_cn：作者在摘要和结论中称Amazon后GDPR政策"potentially violates"，但案例分析中缺乏对具体法律解释的量化证明，"增加用户负担"的推断主要基于注意力权重和文本重定向信息，没有进行用户行为实验；设计原则的跨领域价值没有实证支撑，属于理论延伸。

## 句级写作动作图谱

### 1. P1 S1

- order：1

- section：Abstract

- locator：P1 S1

- move_code：CONTEXT

- paraphrase_cn：消费者信息隐私的社会关注增强，推动全球隐私监管执行。

- rhetorical_function_cn：开篇建立宏观背景，引出隐私话题的重要性。

- depends_on_cn：

- sets_up_cn：为后文提到监管导致隐私政策变化做铺垫。

- evidence_pointer：Abstract P1 S1

### 2. P1 S2

- order：2

- section：Abstract

- locator：P1 S2

- move_code：PHENOMENON

- paraphrase_cn：为遵守GDPR等法规，许多公司的隐私政策越来越冗长和复杂。

- rhetorical_function_cn：指出具体现象：法规驱动政策膨胀。

- depends_on_cn：依赖监管背景（S1）。

- sets_up_cn：引出自动分析的需求。

- evidence_pointer：Abstract P1 S2

### 3. P1 S3

- order：3

- section：Abstract

- locator：P1 S3

- move_code：RQ_OR_OBJECTIVE

- paraphrase_cn：本研究采用计算设计科学范式设计隐私政策演化分析框架。

- rhetorical_function_cn：明确研究范式和方法论。

- depends_on_cn：基于现象和研究背景。

- sets_up_cn：引出框架和SAAS。

- evidence_pointer：Abstract P1 S3

### 4. P1 S4

- order：4

- section：Abstract

- locator：P1 S4

- move_code：DESIGN_FEATURE

- paraphrase_cn：框架包括SAAS系统，能自动标注隐私政策段落的数据实践类别。

- rhetorical_function_cn：介绍核心工件。

- depends_on_cn：研究目标。

- sets_up_cn：为后续评价内容提供对象。

- evidence_pointer：Abstract P1 S4

### 5. P1 S5

- order：5

- section：Abstract

- locator：P1 S5

- move_code：STUDY_OVERVIEW

- paraphrase_cn：我们在OPP-115数据集上严格评估SAAS，并与最新ML和DL方法比较。

- rhetorical_function_cn：预告评估方式。

- depends_on_cn：SAAS设计。

- sets_up_cn：报告实验结果。

- evidence_pointer：Abstract P1 S5

### 6. P1 S6

- order：6

- section：Abstract

- locator：P1 S6

- move_code：RESULT

- paraphrase_cn：SAAS在F1指标上显著优于传统ML和DL模型。

- rhetorical_function_cn：给出核心实验结果。

- depends_on_cn：评价协议。

- sets_up_cn：支持贡献声明。

- evidence_pointer：Abstract P1 S6

### 7. P1 S7

- order：7

- section：Abstract

- locator：P1 S7

- move_code：STUDY_OVERVIEW

- paraphrase_cn：通过Amazon在GDPR前后的隐私政策案例展示框架的实践效用。

- rhetorical_function_cn：介绍第二个评价环节——案例研究。

- depends_on_cn：实验评价。

- sets_up_cn：引出案例结果。

- evidence_pointer：Abstract P1 S7

### 8. P1 S8

- order：8

- section：Abstract

- locator：P1 S8

- move_code：RESULT

- paraphrase_cn：案例显示Amazon后GDPR政策可能导致消费者更费力查找第一方数据收集信息，可能违反GDPR原则。

- rhetorical_function_cn：给出案例研究所产生的领域洞见。

- depends_on_cn：SAAS标注和注意力权重。

- sets_up_cn：说明框架的现实意义。

- evidence_pointer：Abstract P1 S8

### 9. P1 S9

- order：9

- section：Abstract

- locator：P1 S9

- move_code：BOUNDARY_CONDITION

- paraphrase_cn：鉴于消费者隐私的重要性，框架对监管者和公司有重要启示。

- rhetorical_function_cn：扩展影响范围，强调实践相关性。

- depends_on_cn：结果。

- sets_up_cn：提出设计原则。

- evidence_pointer：Abstract P1 S9

### 10. P1 S1

- order：10

- section：Introduction

- locator：P1 S1

- move_code：CONTEXT

- paraphrase_cn：电商和社交媒体的爆发使大量消费者在线分享个人信息。

- rhetorical_function_cn：奠定技术和社会背景。

- depends_on_cn：

- sets_up_cn：引出隐私问题。

- evidence_pointer：Introduction P1 S1

### 11. P1 S2

- order：11

- section：Introduction

- locator：P1 S2

- move_code：PRACTICAL_STAKES

- paraphrase_cn：消费者信息隐私已成为重要的社会问题。

- rhetorical_function_cn：提高现实紧迫性。

- depends_on_cn：背景。

- sets_up_cn：说明研究为什么重要。

- evidence_pointer：Introduction P1 S2

### 12. P2 S1

- order：12

- section：Introduction

- locator：P2 S1

- move_code：PHENOMENON

- paraphrase_cn：法规深远影响导致许多公司修改隐私政策以包含数据实践细节。

- rhetorical_function_cn：描述问题中的行为现象。

- depends_on_cn：法规背景。

- sets_up_cn：过渡到政策变得冗长。

- evidence_pointer：Introduction P2 S1

### 13. P2 S4

- order：13

- section：Introduction

- locator：P2 S4

- move_code：PHENOMENON

- paraphrase_cn：政策更新频繁和长度增长迅速，2009至2019年平均长度翻倍。

- rhetorical_function_cn：用数据佐证政策长度增加现象。

- depends_on_cn：政策更新现象。

- sets_up_cn：为引出分析困难做铺垫。

- evidence_pointer：Introduction P2 S4

### 14. P3 S2

- order：14

- section：Introduction

- locator：P3 S2

- move_code：PRACTICAL_STAKES

- paraphrase_cn：立法者担忧公司以合规名义起草政策但对提高用户理解无益。

- rhetorical_function_cn：指出政策复杂性的危害。

- depends_on_cn：政策长度增长例子。

- sets_up_cn：说明需要自动分析工具。

- evidence_pointer：Introduction P3 S2

### 15. P4 S1

- order：15

- section：Introduction

- locator：P4 S1

- move_code：LIMITATION

- paraphrase_cn：IS隐私研究从行为与经济视角关注关切、控制和风险，但没有分析隐私政策文本的方法。

- rhetorical_function_cn：指出现有IS研究的空白。

- depends_on_cn：问题背景。

- sets_up_cn：为提出IT工件缺口作铺垫。

- evidence_pointer：Introduction P4 S1

### 16. P4 S2

- order：16

- section：Introduction

- locator：P4 S2

- move_code：GAP

- paraphrase_cn：因此需要一个配备新ML/DL文本分析方法的IT工件来识别隐私政策如何变化。

- rhetorical_function_cn：明确提出工件缺口。

- depends_on_cn：IS文献局限。

- sets_up_cn：引出研究目标和SAAS。

- evidence_pointer：Introduction P4 S2

### 17. P5 S1

- order：17

- section：Introduction

- locator：P5 S1

- move_code：RQ_OR_OBJECTIVE

- paraphrase_cn：本研究采用计算设计科学范式，设计隐私政策演化分析框架。

- rhetorical_function_cn：正式宣布研究目标和范式。

- depends_on_cn：缺口。

- sets_up_cn：介绍框架细节。

- evidence_pointer：Introduction P5 S1

### 18. P5 S3

- order：18

- section：Introduction

- locator：P5 S3

- move_code：DESIGN_FEATURE

- paraphrase_cn：SAAS设计有两个新颖之处：RWA识别关键词组方面，多标签分类器共享参数产生正则化。

- rhetorical_function_cn：列出SAAS的两个核心创新。

- depends_on_cn：框架提出。

- sets_up_cn：后续实验检验这些创新。

- evidence_pointer：Introduction P5 S3

### 19. IS privacy paragraph

- order：19

- section：Literature Review

- locator：IS privacy paragraph

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：IS隐私研究已分为关切、控制和风险三大类，多采用行为理论或计量模型。

- rhetorical_function_cn：总结已有IS隐私研究的知识领域。

- depends_on_cn：文献综述目标。

- sets_up_cn：指出方法上的局限。

- evidence_pointer：Literature Review, 'IS Information Privacy Research'

### 20. Privacy policy analysis, step description

- order：20

- section：Literature Review

- locator：Privacy policy analysis, step description

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：现有隐私政策分析过程分为三步：分段、用ML算法标注、分析标注段落。

- rhetorical_function_cn：描述领域标准流程，为后续定位研究贡献。

- depends_on_cn：领域定义。

- sets_up_cn：引出当前方法的不足。

- evidence_pointer：Literature Review, 'Privacy Policy Analysis' Step 1-3

### 21. Privacy policy analysis, after step 3

- order：21

- section：Literature Review

- locator：Privacy policy analysis, after step 3

- move_code：LIMITATION

- paraphrase_cn：传统ML方法依赖BOW表示，假设同一类别的段共享相似词分布，实际却常因词多样性产生漏标或错标。

- rhetorical_function_cn：点明传统方法在表示上的缺陷。

- depends_on_cn：已有流程。

- sets_up_cn：为DL方法引入做铺垫。

- evidence_pointer：Literature Review, paragraph after Step 3

### 22. Privacy policy analysis, DL paragraph

- order：22

- section：Literature Review

- locator：Privacy policy analysis, DL paragraph

- move_code：LIMITATION

- paraphrase_cn：DL方法（如MLP、CNN、BERT）分别有丢失序列信息、忽视长程依赖、需要大量微调数据等问题。

- rhetorical_function_cn：列举现有DL方法的不足。

- depends_on_cn：传统ML局限。

- sets_up_cn：引出SSASE作为可行方案。

- evidence_pointer：Literature Review, paragraph on DL-based methods

### 23. SSASE section, last paragraph

- order：23

- section：Literature Review

- locator：SSASE section, last paragraph

- move_code：GAP

- paraphrase_cn：很少有人研究SSASE在多标签分类任务（如数据实践段标注）上的表现。

- rhetorical_function_cn：识别技术空白。

- depends_on_cn：SSASE介绍。

- sets_up_cn：引出对SSASE的多标签扩展。

- evidence_pointer：SSASE section, last paragraph

### 24. SSASE section, BR limitation

- order：24

- section：Literature Review

- locator：SSASE section, BR limitation

- move_code：MECHANISM

- paraphrase_cn：Binary relevance在标签相关性弱时表现良好，但数据实践类别之间存在相互依赖，共享参数的多任务学习能带来正则化。

- rhetorical_function_cn：解释标签间相关性的机制和应对方法。

- depends_on_cn：多标签分类已有知识。

- sets_up_cn：为多标签分类器设计提供依据。

- evidence_pointer：SSASE section, paragraph on multi-label classification

### 25. SSASE section, equal aspects

- order：25

- section：Literature Review

- locator：SSASE section, equal aspects

- move_code：GAP

- paraphrase_cn：SSASE将所有方面等同看待，但一些方面比其他方面更具区分性。

- rhetorical_function_cn：指出SSASE的另一个局限。

- depends_on_cn：SSASE机制理解。

- sets_up_cn：引出RWA设计的需要。

- evidence_pointer：SSASE section, paragraph after multi-label

### 26. P1 S1

- order：26

- section：Research Gaps and Questions

- locator：P1 S1

- move_code：GAP

- paraphrase_cn：文献回顾确定了几个研究缺口：IS方法不能分析复杂政策文本，传统ML方法有BOW缺陷，DL方法遗漏长依赖，SSASE未用于多标签。

- rhetorical_function_cn：汇总所有缺口，形成研究动机。

- depends_on_cn：文献综述。

- sets_up_cn：提出研究问题。

- evidence_pointer：Research Gaps and Questions P1 S1

### 27. RQ1

- order：27

- section：Research Gaps and Questions

- locator：RQ1

- move_code：RQ_OR_OBJECTIVE

- paraphrase_cn：RQ1：如何增强SSASE的多头自注意力以识别关键区分性方面，改善多标签数据实践段标注？

- rhetorical_function_cn：正式提出第一个研究问题。

- depends_on_cn：缺口总结。

- sets_up_cn：指导SAAS设计。

- evidence_pointer：Research Gaps and Questions RQ1

### 28. RQ2

- order：28

- section：Research Gaps and Questions

- locator：RQ2

- move_code：RQ_OR_OBJECTIVE

- paraphrase_cn：RQ2：增强后的标注系统如何帮助分析隐私政策在法规执行后的演化？

- rhetorical_function_cn：提出第二个研究问题，聚焦实际应用。

- depends_on_cn：RQ1。

- sets_up_cn：引出案例研究。

- evidence_pointer：Research Gaps and Questions RQ2

### 29. Framework overview

- order：29

- section：Proposed Framework

- locator：Framework overview

- move_code：STUDY_OVERVIEW

- paraphrase_cn：提出的框架包括四个组件：测试床、SAAS、基准实验、GDPR案例。

- rhetorical_function_cn：预告框架结构。

- depends_on_cn：RQ1和RQ2。

- sets_up_cn：分小节详述。

- evidence_pointer：'Proposed Privacy Policy Evolution Analytics Framework' first paragraph

### 30. SAAS description

- order：30

- section：SAAS

- locator：SAAS description

- move_code：DESIGN_FEATURE

- paraphrase_cn：SAAS由行级自注意力嵌入RSE和多标签分类器组成。

- rhetorical_function_cn：定义SAAS的总体构成。

- depends_on_cn：框架介绍。

- sets_up_cn：分别解释RSE和分类器。

- evidence_pointer：SAAS section, paragraph 'Recognizing the key limitations...'

### 31. RSE, RWA formula paragraph

- order：31

- section：RSE

- locator：RSE, RWA formula paragraph

- move_code：DESIGN_FEATURE

- paraphrase_cn：RWA通过softmax权重向量对segment embedding的每一行（方面）进行加权，得到加权段表示。

- rhetorical_function_cn：具体描述RWA的数学操作。

- depends_on_cn：SSASE的缺点。

- sets_up_cn：为后续消融实验提供可检验的设计。

- evidence_pointer：RSE subsection, formula (1)-(2)

### 32. RWA regularizer sentence

- order：32

- section：RSE

- locator：RWA regularizer sentence

- move_code：MECHANISM

- paraphrase_cn：RWA充当标签预测中的正则化器，如果一个方面对预测有用，该方面的所有元素都有用，应获得更高权重。

- rhetorical_function_cn：解释RWA为何有效。

- depends_on_cn：RWA定义。

- sets_up_cn：为实验结果解释提供理论机制。

- evidence_pointer：RSE subsection, sentence 'RWA is a regularizer...'

### 33. Classifier overview

- order：33

- section：Multi-Label Classifier

- locator：Classifier overview

- move_code：DESIGN_FEATURE

- paraphrase_cn：多标签分类器在一个模型中包含10个二元分类任务，输出10个概率。

- rhetorical_function_cn：说明分类器结构。

- depends_on_cn：RSE输出。

- sets_up_cn：解释联合优化和损失函数。

- evidence_pointer：Multi-Label Classifier subsection, first paragraph

### 34. BCE joint loss explanation

- order：34

- section：Multi-Label Classifier

- locator：BCE joint loss explanation

- move_code：MECHANISM

- paraphrase_cn：通过同时最小化10个类别的损失，模型能学习类别间的共同特征，减少过拟合。

- rhetorical_function_cn：解释多任务联合训练的好处。

- depends_on_cn：分类器结构。

- sets_up_cn：作为消融对比中独立模型的表现依据。

- evidence_pointer：Multi-Label Classifier subsection, last sentence

### 35. Intro to benchmarks

- order：35

- section：Benchmark Experiments

- locator：Intro to benchmarks

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：按计算设计科学范式，我们设计了四个基准实验来严格评估SAAS。

- rhetorical_function_cn：论证评估方法符合范式要求。

- depends_on_cn：设计科学指南。

- sets_up_cn：介绍实验细节。

- evidence_pointer：'Benchmark Experiments' section, first paragraph

### 36. 5x2 cross-validation paragraph

- order：36

- section：Benchmark Experiments

- locator：5x2 cross-validation paragraph

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：采用5×2交叉验证和配对t检验，以避免方差低估和Type I error升高。

- rhetorical_function_cn：说明统计协议的选择原因。

- depends_on_cn：对比算法评估传统。

- sets_up_cn：让后续显著性结论有依据。

- evidence_pointer：Benchmark Experiments, paragraph '5 times 2-fold cross-validation...'

### 37. Main finding

- order：37

- section：Experiment 1 Results

- locator：Main finding

- move_code：RESULT

- paraphrase_cn：SAAS在micro-recall、F1和HL上显著优于所有传统ML模型。

- rhetorical_function_cn：报告实验1的核心结果。

- depends_on_cn：评估协议。

- sets_up_cn：解释SAAS为何更强。

- evidence_pointer：Experiment 1 Results, first paragraph

### 38. Interpretation sentence

- order：38

- section：Experiment 1 Results

- locator：Interpretation sentence

- move_code：MECHANISM

- paraphrase_cn：SAAS性能可归因于它能捕捉关键词、利用上下文语义和处理高维特征。

- rhetorical_function_cn：为结果提供机制解释。

- depends_on_cn：结果。

- sets_up_cn：用示例段说明。

- evidence_pointer：Experiment 1 Results, paragraph after result tables

### 39. Main finding

- order：39

- section：Experiment 2 Results

- locator：Main finding

- move_code：RESULT

- paraphrase_cn：SAAS在precision、F1、HL上显著优于所有DL基线。

- rhetorical_function_cn：报告实验2核心结果。

- depends_on_cn：DL基线协议。

- sets_up_cn：比较具体架构并解释。

- evidence_pointer：Experiment 2 Results, first paragraph

### 40. Comparison to SSASE variants

- order：40

- section：Experiment 2 Results

- locator：Comparison to SSASE variants

- move_code：RESULT

- paraphrase_cn：SAAS优于10个独立SSASE和SSASE加多标签分类器。

- rhetorical_function_cn：强调SAAS相对SSASE方案的优势。

- depends_on_cn：F1结果。

- sets_up_cn：引出RWA和关系学习的机制主张。

- evidence_pointer：Experiment 2 Results, second paragraph

### 41. Example segment discussion

- order：41

- section：Experiment 2 Results

- locator：Example segment discussion

- move_code：MECHANISM

- paraphrase_cn：SAAS能利用区分性方面和类别间关系识别FP和TP，而SSASE只识别FP。

- rhetorical_function_cn：用具体实例说明机制的实践意义。

- depends_on_cn：表10结果。

- sets_up_cn：指出防止漏检标签的监管价值。

- evidence_pointer：Experiment 2 Results, paragraph after Table 10

### 42. Main finding

- order：42

- section：Experiment 3 Results

- locator：Main finding

- move_code：RESULT

- paraphrase_cn：完整SAAS优于所有消融变体，证明RWA和多标签分类器的必要性。

- rhetorical_function_cn：报告消融实验结论。

- depends_on_cn：消融设计。

- sets_up_cn：为设计原则提供证据。

- evidence_pointer：Experiment 3 Results, first paragraph

### 43. RWA vs MLP explanation

- order：43

- section：Experiment 3 Results

- locator：RWA vs MLP explanation

- move_code：MECHANISM

- paraphrase_cn：MLP学固定权重矩阵而RWA能根据输入段动态更新权重。

- rhetorical_function_cn：解释RWA优于MLP替代的原因。

- depends_on_cn：消融结果。

- sets_up_cn：说明为何动态权重更适合长而复杂的段落。

- evidence_pointer：Experiment 3 Results, paragraph after Table 11

### 44. Main finding

- order：44

- section：Experiment 4 Results

- locator：Main finding

- move_code：RESULT

- paraphrase_cn：自动分段与手工分段的F1差异不显著。

- rhetorical_function_cn：报告鲁棒性测试结果。

- depends_on_cn：ST-Ro分段。

- sets_up_cn：扩展SAAS的应用场景。

- evidence_pointer：Experiment 4 Results, last paragraph

### 45. Step 3 description

- order：45

- section：Case Study

- locator：Step 3 description

- move_code：STUDY_OVERVIEW

- paraphrase_cn：我们收集Amazon前后政策，用ST-Ro分段，用SAAS标注，然后选择FP类段，并用注意力权重可视化。

- rhetorical_function_cn：介绍案例研究五步流程。

- depends_on_cn：SAAS框架。

- sets_up_cn：报告案例结果。

- evidence_pointer：Case Study section, steps 1-5

### 46. Result section

- order：46

- section：Case Study

- locator：Result section

- move_code：RESULT

- paraphrase_cn：后GDPR段的高注意力比重指向cookies notice重定向，用户需打开独立文档。

- rhetorical_function_cn：报告案例中的关键发现。

- depends_on_cn：注意力权重输出。

- sets_up_cn：结合GDPR条款进行解释。

- evidence_pointer：Case Study section, paragraph after Table 12

### 47. GDPR Recitals interpretation

- order：47

- section：Case Study

- locator：GDPR Recitals interpretation

- move_code：MECHANISM

- paraphrase_cn：GDPR要求信息易于访问和理解，但Amazon将信息隐藏在不同文档，增加用户负担。

- rhetorical_function_cn：将结果连接到法律原则，形成合规判断。

- depends_on_cn：案例观测。

- sets_up_cn：支持监管启示。

- evidence_pointer：Case Study section, after result

### 48. First paragraph

- order：48

- section：Discussion

- locator：First paragraph

- move_code：CONTRIBUTION

- paraphrase_cn：本研究通过计算设计科学范式设计、实现并评估了隐私政策演化分析框架。

- rhetorical_function_cn：总结贡献。

- depends_on_cn：全部前文。

- sets_up_cn：细分贡献类别。

- evidence_pointer：Discussion and Contributions, first paragraph

### 49. Design principles

- order：49

- section：Discussion

- locator：Design principles

- move_code：CONTRIBUTION

- paraphrase_cn：框架遵循两个超越隐私政策的设计原则：区分复杂文本中的方面重要性，以及多标签分类中共享特征。

- rhetorical_function_cn：明确提出可复用的设计知识。

- depends_on_cn：实验结果。

- sets_up_cn：讨论跨领域应用。

- evidence_pointer：Discussion, 'Contributions to the IS Knowledge Base'

### 50. Managerial implications

- order：50

- section：Discussion

- locator：Managerial implications

- move_code：BOUNDARY_CONDITION

- paraphrase_cn：框架可帮助监管者改进合规测试，帮助公司审查潜在违规。

- rhetorical_function_cn：说明实践受众。

- depends_on_cn：贡献声明。

- sets_up_cn：为未来方向做过渡。

- evidence_pointer：Discussion, 'Managerial and Practical Implications'

### 51. Future directions

- order：51

- section：Conclusion

- locator：Future directions

- move_code：LIMITATION_AND_FUTURE

- paraphrase_cn：未来可开发多语言框架和面向用户的SAAS辅助系统。

- rhetorical_function_cn：指出后续研究方向。

- depends_on_cn：当前框架的边界。

- sets_up_cn：结束全文。

- evidence_pointer：Conclusion and Future Directions, last paragraph

## 写作技术

- gap_construction_cn：通过三类缺口的叠加来制造研究的必要性：一是IS隐私研究缺乏文本分析方法的领域缺口；二是现有隐私政策分析技术（传统ML、CNN、BERT等）各自存在表示或数据需求的性能缺口；三是SSASE本身未针对多标签和方面区分的问题。三个缺口层层收窄，最后对准SAAS的设计空间。

- signposting_cn：摘要和引言末尾明确列出论文剩余结构；每个章节开头都有'First...Second...Third...'式的路标；每个实验小节开头说明该实验的目的和对照组；案例研究部分用Step 1-Step 5列出流程，使读者始终知道当前所处位置。

- transition_logic_cn：实验1证明优于传统ML后，自然过渡到'但需要与更先进的DL模型比较'；实验2的SSASE基线性能接近SAAS，自然引出消融分析来分离RWA和分类器贡献；消融确认设计有效后，下一步检查在自动分段下的实际可用性；鲁棒性验证后，进入案例研究展示价值。每个Study结尾的'remaining uncertainty'成为下一Study的动机。

- claim_evidence_rhythm_cn：在结果部分采用总-分-总的模式：先给出宏观统计结果（表7/9/11的显著差异），然后用一个具体示例段和注意力权重解释机制，最后量化这种模式在测试集中出现的次数（如75/1872、287/1872），使案例具有代表性和数量感。

- benchmark_narrative_cn：基准不是简单罗列，而是按从弱到强的顺序组织：传统ML→CNN/RNN→双向RNN→SSASE变体。每一级baseline都对应一个特定的技术限制（BOW、局部特征、单向、缺少方面区分），SAAS每胜一级就补充一项论据。最终归因到RWA和multi-label classifier。

- theory_return_cn：在结果和讨论中反复将性能差异归因到RWA的动态方面加权和多标签分类器的共享参数，再在贡献部分将这两项抽象为设计原则，并推广到电商、健康和隐私，完成从具体结果到一般知识的上升。

- contribution_positioning_cn：贡献分三层：技术层（SAAS模型）、应用层（隐私政策变化分析用例）、知识层（设计原则）。每层都直接回应引言中的相应缺口，且用表13将设计原则与不同IS文献领域对应，增强知识的可迁移性。

- novelty_protection_cn：通过消融实验和与SSASE变体的对比，明确宣称性能提升来自RWA和multi-label classifier，防止贡献被看作仅仅是调参的结果；用自动分段实验证明实用鲁棒性；用案例研究展示除了指标外还有真实世界影响，使贡献不限于一次性性能比较。

## 可复用研究与写作程序

### structure_steps

#### 1. 1

- step：1

- writing_job_cn：建立现实背景：社会责任、法规压力和隐私政策的实际变化。

- research_job_cn：收集法规案例和隐私政策长度变化数据。

- required_evidence_cn：至少一个可视化示例（如Amazon政策前后对比）展示问题严重性。

- transition_to_next_cn：指出现有IS文献缺乏处理该问题的工具，引出技术缺口。

#### 2. 2

- step：2

- writing_job_cn：综述相关领域，明确已有方法和限制。

- research_job_cn：系统梳理IS隐私研究、隐私政策分析、SSASE和注意力机制文献。

- required_evidence_cn：用表格总结关键文献，并明确指出每个方法的具体限制。

- transition_to_next_cn：将限制综合为研究缺口，提出RQ。

#### 3. 3

- step：3

- writing_job_cn：设计IT工件：给出框架图和算法细节。

- research_job_cn：将RQs转换为设计需求，选择合适的技术基础进行扩展。

- required_evidence_cn：清晰的框架图和与知识基础对应的创新点描述。

- transition_to_next_cn：说明为评价工件而设计的多组实验。

#### 4. 4

- step：4

- writing_job_cn：选择基准和实验协议。

- research_job_cn：选择公认数据集、多类baseline、交叉验证和统计检验。

- required_evidence_cn：合理的评估指标（micro-F1, HL等）和baseline集合。

- transition_to_next_cn：按从弱到强顺序报告实验结果。

#### 5. 5

- step：5

- writing_job_cn：报告实验并解释机制。

- research_job_cn：在统计结果之外，提供具体示例和注意力可视化来说明模型为什么有效。

- required_evidence_cn：至少一个代表性错误分析或成功案例，并统计类似案例频次。

- transition_to_next_cn：通过消融或鲁棒性检验进一步支持设计声称。

#### 6. 6

- step：6

- writing_job_cn：消融和稳健性分析。

- research_job_cn：移除/替换关键组件，或在更真实条件下测试。

- required_evidence_cn：对比完整模型与变体，证明每个设计成分的必要性。

- transition_to_next_cn：引入实际案例研究展示价值。

#### 7. 7

- step：7

- writing_job_cn：案例研究连接现实影响。

- research_job_cn：选择有代表性的真实对象（如Amazon和GDPR），展示模型输出如何转化为领域洞见。

- required_evidence_cn：与法规条款或实际事件相关的具体发现，而不是泛泛的定性描述。

- transition_to_next_cn：在讨论中把技术结果上升为设计原则。

#### 8. 8

- step：8

- writing_job_cn：讨论贡献、设计原则和未来方向。

- research_job_cn：将实验结果抽象为可复用的知识，并说明对研究者、监管者和企业的启示。

- required_evidence_cn：设计原则应与实验结果正面呼应，避免无证据扩展。

- transition_to_next_cn：以未来方向收尾。

### most_transferable_moves_cn

1. 用表格总结文献并逐条指出限制，使缺口一目了然

2. 将实验按从弱到强的baseline层层递进，每层建立新论据

3. 在结果中穿插具体示例和注意力可视化，用数量统计说明代表性

4. 在消融实验中逐一验证设计组件，保护核心贡献不被稀释

5. 用案例研究将technical结果转换为领域术语和现实意义

6. 将核心创新抽象为两条短语级设计原则，并映射到不同应用领域

### resource_intensive_or_nonstandard_parts_cn

1. 需要人工标注数据集（如OPP-115）作为测试床，构建此类数据成本高

2. 案例研究需要选择具有监管争议的企业和前后政策文本，需领域知识支撑

3. 与法律条款（如GDPR Recitals）结合的解释需要跨学科团队

4. 深度模型的训练需要GPU、大规模调参和较长时间

### what_not_to_copy_superficially_cn

1. 如果没有消融实验，不能声称某一组件是必要的

2. 如果没有与SSASE变体对比，不能把SAAS的改进全部归因于RWA

3. 案例研究只是案例，不能单靠单个公司推出普遍合规结论

4. 不能只复制设计原则措辞而没有对应的实验结果支撑

5. 不应将注意力权重直接等同于法律判决依据

- single_best_description_of_the_routine_cn：以一个现实问题为牵引，系统指出现有技术最贴近的知识基础（SSASE）的缺陷，然后通过两个针对性设计改动填补缺陷，用一套逐层递进的基准实验、消融和案例将改动验证为必要且有用，最终把改动抽象为两条可迁移设计原则。

## 分析边界

文章图片和部分公式因OCR存在少量噪声，但文本内容完整；本文只提供了正文和附录的部分表格，未包含全部附录（如Appendix B的完整表格已给出，但个别细节如超参数之外的训练细节略有省略）；基于提供的全文，分析覆盖了主要论证链。
