# Guided Diverse Concept Miner (GDCM): Uncovering Relevant Constructs for Managerial Insights from Text

- 作者：Dokyun “DK” Lee; Zhaoqi “ZQ” Cheng; Chengfeng Mao; Emaad Manzoor
- 年份 / 期刊：2025 / Information Systems Research
- DOI：10.1287/isre.2020.0494
- 源文件：27974_2025_guided-diverse-concept-miner-gdcm-uncovering-relevant-constructs-for-managerial-insights-from-te.md
- 论文主类型：build_evaluate_design_science
- 主导写作弧线：requirements_build_evaluate_design_principles
- 置信度：0.72

## 文章级论证概况

- 核心问题：如何在没有任何预定义概念或人工标注的情况下，从文本中自动、可解释地发现与管理者指定结果变量高度相关且多样、连贯的概念，并给出其相关重要性估计？

- 制品与设计：GDCM是一种可解释深度学习算法：将词、文档、概念嵌入到同一向量空间，概念向量对应原型；损失函数由嵌入损失、稀疏正则、概念两两差异正则和结果分类损失组成，同时优化可解释性、多样性与相关性。

- 客观结果：在在线零售商的评论阅读与转化数据上，GDCM的AUC为0.8885，超过所有可解释基线且接近CNN(0.9186)和XGB(0.9184)；人类判断Gini系数最高；coherence优于LDA；5次运行即可恢复多个基准50/150次运行无法恢复的Garvin概念；概念系数与Liu et al. (2019)的因果研究接近。

- 核心贡献：作者声称GDCM是一种“guided exploration”工具，能够按概念理论的可解释性、多样性和相关性要求，从文本中发现可能与管理者结果相关的新概念，并提供相关性重要性估计，为假设生成和后续因果研究提供起点；同时为监督概念挖掘提供了基于概念理论的设计知识。

- 整篇论证链：文章先指出企业文本分析需要将文本转化为管理者可理解且与结果相关的概念，但现有监督主题模型或黑箱模型要么缺少同一语义空间中的可解释性，要么缺少显式多样性控制。作者从哲学与认知科学的概念理论出发，尤其是原型理论，提炼出词汇化、概念连贯性、区分性与相关性四条标准，再转化为可解释性、多样性、相关性三个desiderata；据此构建GDCM：共享向量空间加概念原型、稀疏正则、概念向量两两相异正则、结果分类损失。评价分三层展开：MTurk与coherence证明可解释性；Garvin维度召回和未知概念覆盖证明多样性；预测AUC、概念系数与外部因果研究对比证明相关性。最后结合消融、Y敏感性以及TopicGPT比较，把GDCM定位为探索性、相关性假设生成工具，并声明其不能直接做因果推断。

## 类型与写作弧线判定

- 论文主类型判定：文章的核心是构建一个新算法制品GDCM，并从理论要求出发转化为设计原则（interpretability, diversity, relevance），再按这些desiderata进行系统评价，最后提炼可复用的设计知识和边界，符合“需求/原则—构建—评价—设计知识”的典型设计科学路径。虽然也使用benchmark，但其主导逻辑是设计要求的实现与验证，而非单纯追求性能纪录。

- 主导写作弧线判定：引言明确提出三个关键要求，第2节用概念理论支撑这些要求，第3节用数据挑战说明为什么现有方法不足，第4节把要求翻译成模型组件和损失函数，第5节按每个desideratum分别评价，第6节给出管理与研究含义和边界。整体写作弧线是要求—构建—评价—设计原则。

## 研究开展程序

- study_or_phase_count：11

- 研究阶段总序列：论文先从概念理论推出设计需求；然后在真实在线零售数据上构造成guided exploration任务；接着实现GDCM算法；之后按desiderata逐层评价：人类可解释性、算法coherence、多样性/召回、未知概念召回、预测相关性、概念重要性外部效度、Y敏感性与消融、LLM对比；最后总结贡献与边界。各阶段不是独立Study，而是累积地为同一个算法主张提供不同维度的证据。

### studies_or_phases

#### 1. 概念理论与设计需求推导

- order：1

- name_cn：概念理论与设计需求推导

- question_cn：什么样的概念定义适合作为文本探索工具的算法设计基础？

- inputs_and_setting_cn：哲学与认知科学文献：原型理论、经典概念理论、概念标准文献；无新数据。

- designed_or_compared_object_cn：概念的定义标准与三个desiderata；与经典概念理论对照。

- baseline_control_or_counterfactual_cn：古典概念理论与原型理论比较。

##### objective_metrics

1. 词汇化

2. 概念连贯性

3. 区分性

4. 相关性

- analysis_method_cn：概念分析与理论推导。

- main_result_cn：选定原型理论，提出GDCM应满足可解释性、多样性、相关性三个desiderata。

- argumentative_role_cn：给出算法的理论合法性和可评价标准。

- remaining_uncertainty_cn：尚未说明算法实现。

- link_to_next_phase_cn：引出数据任务与模型设计。

##### evidence_pointers

1. Section 1 P3/P5

2. Section 2.1 P1-P4

#### 2. 主数据与任务构造

- order：2

- name_cn：主数据与任务构造

- question_cn：如何构造一个管理者对相关概念一无所知的guided exploration真实场景？

- inputs_and_setting_cn：英国在线零售商数据，243,000消费者，2015年2-3月，电子产品和家庭园艺类，41个子类；含点击流、页面浏览、交易、评论阅读行为。

- designed_or_compared_object_cn：决策旅程：用户访问产品页、读评论、购买或放弃；样本为UserID-ProductID，含评论文本、结构化X、转化标签。

- baseline_control_or_counterfactual_cn：无明确反事实；以转化/放弃二元标签作为目标。

##### objective_metrics

1. 转化

- analysis_method_cn：数据构造和描述统计（Online Appendix B.1）。

- main_result_cn：得到可用于算法评价的journey级数据；转化作为管理结果Y。

- argumentative_role_cn：为所有后续评价提供共同的现实场景。

- remaining_uncertainty_cn：单一平台和品类；缺乏不同Y的对比。

- link_to_next_phase_cn：指出现有方法在如此任务中会产生不可用主题（Figure 3），引出算法。

##### evidence_pointers

1. Section 3.1 P1-P2

2. Online Appendix B.1

#### 3. GDCM算法构建

- order：3

- name_cn：GDCM算法构建

- question_cn：如何把原型理论和三个desiderata转成可训练的深度模型？

- inputs_and_setting_cn：上述journey数据的评论文本、X、Y。

- designed_or_compared_object_cn：GDCM的概念分配网络CAN、嵌入网络、线性分类器；L_neg、L_spr、L_div、L_clf。

- baseline_control_or_counterfactual_cn：无；之后与基准方法比较。

##### objective_metrics

1. 损失函数组成

2. 概念嵌入向量

3. 文档-概念分布

- analysis_method_cn：形式化模型推导。

- main_result_cn：GDCM在同一空间中表示词、文档和概念；稀疏、多样性、分类损失分别对应desiderata。

- argumentative_role_cn：提供可评价的制品。

- remaining_uncertainty_cn：理论上成立但需实证。

- link_to_next_phase_cn：进入Section 5评价。

##### evidence_pointers

1. Section 4.1.1-4.1.5

2. Table 4

#### 4. 人类判断可解释性评价

- order：4

- name_cn：人类判断可解释性评价

- question_cn：人类是否认为GDCM发现的概念或主题更清晰、更可解释？

- inputs_and_setting_cn：GDCM与LDA/HSTM/sDTM/sLDA的主题词；100名MTurk工人；Garvin维度描述；在线调查。

- designed_or_compared_object_cn：各算法主题；MTurk将主题匹配到Garvin维度。

- baseline_control_or_counterfactual_cn：LDA、HSTM、sDTM、sLDA等基准主题。

##### objective_metrics

1. Gini系数

- analysis_method_cn：Gini系数、bootstrap标准误；注意力检查和随机化。

- main_result_cn：GDCM的Gini系数最高。

- argumentative_role_cn：直接支持空间可解释性和概念连贯性。

- remaining_uncertainty_cn：依赖人标注和已知Garvin框架。

- link_to_next_phase_cn：用算法coherence做稳健性验证。

##### evidence_pointers

1. Section 5.1.1

2. Figure 4

3. Online Appendix B.2

#### 5. 算法coherence可解释性评价

- order：5

- name_cn：算法coherence可解释性评价

- question_cn：标准coherence指标是否确认GDCM的可解释性优势？

- inputs_and_setting_cn：各算法的top关键词；文档共现计数。

- designed_or_compared_object_cn：coherence得分；GDCM与benchmark对比。

- baseline_control_or_counterfactual_cn：LDA、HSTM、sDTM、sLDA、ETM等。

##### objective_metrics

1. Mimno-McCallum coherence

- analysis_method_cn：多次运行范围比较、统计显著性。

- main_result_cn：GDCM平均coherence为-1.86，LDA为-2.25，范围不重叠；HSTM更低；sDTM/sLDA更高但词重复。

- argumentative_role_cn：为可解释性提供不依赖人判断的补充证据，并说明高coherence可能被重复词虚高。

- remaining_uncertainty_cn：coherence单指标不足，需多样性/召回。

- link_to_next_phase_cn：转向多样性。

##### evidence_pointers

1. Section 5.1.2

2. Figure 3

3. Table 10

#### 6. 已知概念多样性与召回

- order：6

- name_cn：已知概念多样性与召回

- question_cn：GDCM是否能恢复多个已知高层质量概念，且概念之间更分散？

- inputs_and_setting_cn：Garvin的6个维度被两位专家操作化为词表；GDCM与benchmark输出top10词；MTurk分类结果。

- designed_or_compared_object_cn：各算法概念集与Garvin概念词表的重叠；人类分类向量的平均余弦距离。

- baseline_control_or_counterfactual_cn：LDA、HSTM、sDTM、sLDA、ETM、ProdLDA；不同重叠阈值和运行次数。

##### objective_metrics

1. 独特Garvin概念数量

2. 平均成对余弦距离

- analysis_method_cn：改变h_overlap阈值、多次运行、专家词表稳健性。

- main_result_cn：GDCM 5次运行可恢复5/4个概念，优于基准50/150次运行。

- argumentative_role_cn：支持多样性与区分性，且“召回已知理论概念”提供外部效度。

- remaining_uncertainty_cn：已知概念作为ground truth不代表真正未知发现。

- link_to_next_phase_cn：需要未知概念召回检验。

##### evidence_pointers

1. Section 5.2.1-5.2.2

2. Table 7

3. Table 8

#### 7. 未知概念相对召回

- order：7

- name_cn：未知概念相对召回

- question_cn：当真实概念未知时，GDCM是否比基准覆盖更多机器发现的概念？

- inputs_and_setting_cn：主数据上所有算法机器恢复的概念；将机器恢复概念作为伪ground truth（Online Appendix B.5）。

- designed_or_compared_object_cn：相对召回或覆盖率。

- baseline_control_or_counterfactual_cn：基准主题模型。

##### objective_metrics

1. relative recallability

2. coverage rate

- analysis_method_cn：在线附录B.5的覆盖分析。

- main_result_cn：GDCM相对召回率更高。

- argumentative_role_cn：把多样性主张从已知Garvin扩展到未知概念。

- remaining_uncertainty_cn：伪ground truth并不是真实理论新概念。

- link_to_next_phase_cn：转向相关性/预测。

##### evidence_pointers

1. Section 5.2.3

2. Online Appendix B.5

#### 8. 预测性能与相关性评价

- order：8

- name_cn：预测性能与相关性评价

- question_cn：GDCM发现的概念是否对转化结果相关，且预测表现是否可接受？

- inputs_and_setting_cn：主数据集的评论文本、X、转化标签；多个baseline。

- designed_or_compared_object_cn：GDCM与可解释/不可解释模型；topic model+LR/XGB。

- baseline_control_or_counterfactual_cn：LDA+LR、SeededLDA、HSTM、sDTM、BOW+LR、CNN、XGB等。

##### objective_metrics

1. Accuracy

2. Precision

3. Recall

4. F1

5. AUC

6. ROC

- analysis_method_cn：70/15/15划分，多参数配置训练，ROC/AUC比较。

- main_result_cn：GDCM AUC为0.8885；超过所有可解释基线；CNN 0.9186、XGB 0.9184略高。

- argumentative_role_cn：支持相关性desideratum，证明可解释模型仍具强预测能力。

- remaining_uncertainty_cn：非因果；黑箱模型略高；预测性能不是全部。

- link_to_next_phase_cn：继续检查概念系数是否在经济上有意义。

##### evidence_pointers

1. Section 5.3.1

2. Table 9

3. Table 10

4. Figure 7

#### 9. 概念重要性估计与外部因果对照

- order：9

- name_cn：概念重要性估计与外部因果对照

- question_cn：GDCM给出的概念相关重要性是否与已有因果/理论结果一致？

- inputs_and_setting_cn：GDCM估计系数；Liu et al. (2019)在类似数据上的因果估计。

- designed_or_compared_object_cn：Aesthetics、Conformance、Features、Value、Serviceability系数；价格、评分等X系数。

- baseline_control_or_counterfactual_cn：Liu et al. (2019)的系数作为外部对照。

##### objective_metrics

1. 系数符号

2. 系数大小排序

- analysis_method_cn：可视化估计系数并进行定性比较。

- main_result_cn：两者都显示Aesthetics正相关最高，Serviceability负相关最低；GDCM系数与Liu接近。

- argumentative_role_cn：外部效度：GDCM自动发现的概念在经济上并非一次性结果。

- remaining_uncertainty_cn：数据不完全相同，无法提供置信区间；不是因果证明。

- link_to_next_phase_cn：补充敏感性/消融来确认组分作用。

##### evidence_pointers

1. Section 5.3.2

2. Figure 8

#### 10. Y敏感性、消融与稳健性

- order：10

- name_cn：Y敏感性、消融与稳健性

- question_cn：GDCM对不同Y是否敏感；各超参数对可解释性和AUC的作用如何？

- inputs_and_setting_cn：DonorsChoose数据（多种Y）；主数据；超参数λ/η/ρ变化。

- designed_or_compared_object_cn：不同Y下的概念；不同超参数配置。

- baseline_control_or_counterfactual_cn：默认配置与其他参数设置。

##### objective_metrics

1. 概念内容变化

2. AUC

3. coherence

- analysis_method_cn：Y敏感性分析；消融实验（Online Appendices B.6/C）。

- main_result_cn：概念随Y发生合理变化；提高ρ提高AUC，提高η提高可解释性，提高λ降低AUC但不影响可解释性。

- argumentative_role_cn：表明GDCM灵活且组分可解释，保护artifact claim。

- remaining_uncertainty_cn：DonorsChoose细节在附录，未提供原始表。

- link_to_next_phase_cn：最后与LLM主题模型比较。

##### evidence_pointers

1. Section 5.3.3

2. Figure 9

3. Online Appendix C

#### 11. LLM主题模型对比（TopicGPT）

- order：11

- name_cn：LLM主题模型对比（TopicGPT）

- question_cn：新兴的prompt-based LLM主题模型是否对GDCM构成替代？

- inputs_and_setting_cn：TopicGPT（Llama2-7B）在主数据上的输出；seed/no-seed提示；三轮自纠正。

- designed_or_compared_object_cn：TopicGPT主题one-hot + XGB vs GDCM。

- baseline_control_or_counterfactual_cn：TopicGPT有/无种子、有/无自纠正；GDCM。

##### objective_metrics

1. Accuracy

2. Precision

3. Recall

4. F1

5. AUC

- analysis_method_cn：预测对比；样例幻觉检查。

- main_result_cn：TopicGPT最佳AUC约0.7095，仍明显低于GDCM；抽样标签存在与原文无关的幻觉。

- argumentative_role_cn：回应最新benchmark，排除LLM方法作为直接替代。

- remaining_uncertainty_cn：LLM进展快，单一样例有限。

- link_to_next_phase_cn：进入总体结论。

##### evidence_pointers

1. Appendix A

2. Table A.2

3. Figure A.1

## 各部分修辞架构

### abstract_moves

1. OBJECTIVE: 提出GDCM的三个目标

2. METHOD: 同空间嵌入、多样性/相关性正则

3. RESULT: 在在线review数据上比基准更优，并恢复Garvin概念

4. VALIDITY: 与Liu et al.因果研究一致，用DonorsChoose证明Y敏感性

### introduction_moves

1. CONTEXT: 企业文本分析普及

2. PRACTICAL_STAKES: 文本量带来的认知挑战

3. REQUIREMENT: 概念需要可解释、多样、与结果相关

4. RQ_OR_OBJECTIVE: 提出GDCM

5. THEORY_INTRO: 用概念理论定义概念

6. LIMITATION: Quadrant II方法缺少显式多样性和理论根基

7. DESIGN_FEATURE: 三个desiderata及其实现

8. STUDY_OVERVIEW: 预览第5节评价

### theory_and_knowledge_moves

1. THEORY_INTRO: 原型理论比经典理论更适合计算化

2. THEORY_PROPOSITION: 概念=(A,d,p)三元组

3. REQUIREMENT: 把A/d/p映射到嵌入空间、相似度和概念向量

4. LIMITATION: LDA主题不在同一概念空间，嵌入主题模型缺距离度量

5. MECHANISM: 多样性和相关性共同提高未知概念的recall

### artifact_design_moves

1. REQUIREMENT: 可解释性、多样性、相关性对应四类loss

2. DESIGN_FEATURE: 词/文档/概念共享嵌入空间

3. DESIGN_FEATURE: 概念向量作为原型，文档为概念加权组合

4. DESIGN_FEATURE: 稀疏正则提升预测可解释性

5. DESIGN_FEATURE: 概念向量两两惩罚实现多样性

6. DESIGN_FEATURE: 分类交叉熵实现结果相关性

### evaluation_moves

1. METHOD_JUSTIFICATION: MTurk用Garvin维度测量人类可解释性

2. BENCHMARK_OR_CONTRAST: 用coherence、词重叠、AUC等对比多个基准

3. RESULT: GDCM在Gini、coherence、召回、AUC上均胜出或接近

4. ROBUSTNESS_OR_BOUNDARY_TEST: 消融、Y敏感性、未知概念召回、TopicGPT对比

5. RESULT: 系数与Liu et al.因果研究一致

### discussion_and_contribution_moves

1. CONTRIBUTION: GDCM是guided exploration工具

2. PRACTICAL_STAKES: 可动态监控反馈、识别内容偏差

3. BOUNDARY_CONDITION: 探索性、相关性而非因果性

4. LIMITATION_AND_FUTURE: 用户领域判断决定实际价值

## 理论/知识到设计的翻译

### 知识/理论基础

1. 原型理论（Osherson and Smith 1981）

2. 分布语义理论（Harris 1954; Mikolov et al. 2013）

3. 概念理论标准：lexicalization, conceptual coherence, differentiation, relevance

4. 可解释机器学习/XAI文献（Murdoch et al. 2019; Rudin 2019）

5. 主题模型文献（LDA, HSTM, sDTM, sLDA等）

- 理论—设计耦合：direct

- 耦合判定理由：概念理论不仅用于讨论，而是直接决定算法结构：原型理论的三元组(A,d,p)被逐一映射到共享嵌入空间、向量相似度和概念向量；lexicalization/coherence/differentiation/relevance四条标准分别对应嵌入损失、距离度量、多样性正则和分类损失。设计选择不是事后解释，而是从理论前瞻性推导出的。

- 理论到设计翻译链：原型理论把概念定义为(A,d,p)，GDCM把A实现为共享嵌入空间、d实现为向量相似性、p实现为概念向量；lexicalization和conceptual coherence通过词/概念同空间实现，differentiation通过惩罚概念向量点积实现，relevance通过分类交叉熵loss实现；预测可解释性通过线性权重θ实现；稀疏正则进一步服务于预测可解释性。

### mapping_table

#### 1. 1

- theory_or_knowledge_claim_cn：概念应可被语言表达（lexicalization）

- mechanism_cn：在共享语义空间中，靠近概念向量的词可用来解释概念

- design_requirement_cn：词、文档、概念必须在同一向量空间

- artifact_choice_cn：skip-gram负采样loss中同时注入pivot、context和document向量

- evaluated_contrast_cn：GDCM vs LDA/HSTM/sDTM/sLDA的概念词是否同空间、可解释

- objective_result_cn：MTurk Gini系数最高，coherence优于LDA

##### evidence_pointers

1. Section 4.1.1-4.1.2

2. Section 5.1.1-5.1.2

#### 2. 2

- theory_or_knowledge_claim_cn：概念成员应彼此相似（conceptual coherence）

- mechanism_cn：概念原型周围只包含语义相近的词，形成连通区域

- design_requirement_cn：以距离d界定概念成员

- artifact_choice_cn：用向量相似度定义概念成员和最近词

- evaluated_contrast_cn：各算法主题词的人类分类一致性

- objective_result_cn：GDCM主题更少歧义，Gini更高

##### evidence_pointers

1. Section 5.1.1

2. Figure 4

#### 3. 3

- theory_or_knowledge_claim_cn：概念之间应可区分（differentiation）

- mechanism_cn：概念向量彼此远离，避免主题重叠和概念扩散

- design_requirement_cn：显式惩罚概念嵌入的两两相似性

- artifact_choice_cn：L_div = η Σ log σ(E_c[i]·E_c[j])

- evaluated_contrast_cn：Garvin概念召回和主题间余弦距离

- objective_result_cn：GDCM 5次运行恢复更多Garvin概念，主题间更分散

##### evidence_pointers

1. Section 4.1.4

2. Section 5.2.1-5.2.2

3. Table 8

#### 4. 4

- theory_or_knowledge_claim_cn：概念应为预测现实提供最大信息（relevance）

- mechanism_cn：只保留与管理者结果Y高度相关的概念子空间

- design_requirement_cn：以分类损失引导概念发现

- artifact_choice_cn：L_clf = ρ cross-entropy(θ·p_d, y_d)

- evaluated_contrast_cn：转化预测AUC和概念系数

- objective_result_cn：AUC 0.8885，超过所有可解释基线；系数与外部因果研究接近

##### evidence_pointers

1. Section 4.1.5

2. Section 5.3.1-5.3.2

#### 5. 5

- theory_or_knowledge_claim_cn：预测关系应可理解（prediction interpretability）

- mechanism_cn：概念概率的线性组合直接映射到结果

- design_requirement_cn：使用线性预测层而不是黑箱预测层

- artifact_choice_cn：Equation (7)/(10)中的θ向量

- evaluated_contrast_cn：概念与X变量的系数报告

- objective_result_cn：可给出Aesthetics、Serviceability等概念的相关重要性

##### evidence_pointers

1. Section 4.1.5

2. Section 5.3.2

3. Figure 8

#### 6. 6

- theory_or_knowledge_claim_cn：每个文档应集中于少数概念（sparsity）

- mechanism_cn：稀疏文档-概念分布使解释聚焦于关键特征

- design_requirement_cn：加入稀疏正则

- artifact_choice_cn：L_spr = λ Σ log(p_d[c])

- evaluated_contrast_cn：消融实验中变化λ的影响

- objective_result_cn：λ提高会降低AUC，但不显著影响coherence

##### evidence_pointers

1. Section 4.1.3

2. Section 5.3.3.2

3. Figure 9

## 评价逻辑

### evaluation_modes

1. 人类主观评价（MTurk + Garvin维度匹配）

2. 算法coherence指标

3. 已知概念词重叠召回（Garvin ground truth）

4. 未知概念相对召回（机器恢复概念作为伪ground truth）

5. 预测性能benchmark（多个可解释和不可解释基线）

6. 系数与外部因果研究对照

7. Y敏感性分析（DonorsChoose）

8. 消融分析（λ、η、ρ）

9. 新兴LLM主题模型对比（TopicGPT）

- why_these_evaluations_cn：因为作者主张的不是单一性能优势，而是三个desiderata同时成立。因此需要为每个desideratum分别设计证据：可解释性需要人类判断和coherence；多样性需要概念区分度和对已知/未知概念的召回；相关性需要预测表现和概念重要性。外部因果对照则是为了证明GDCM发现的概念不是偶然，而是与经济理论一致。

- benchmark_and_contrast_chain_cn：先用人判断和coherence建立可解释性基准；再用Garvin词表召回建立已知概念基准；再用机器恢复概念建立未知概念基准；然后用预测AUC与多类baseline比较建立相关性基准；最后用Liu et al. (2019)的因果估计作为经济含义的外部锚。各层基准互相补充，但由不同证据支撑。

### claim_evidence_ledger

1. 技术主张：GDCM能同时实现高可解释性、多样性和相关性；证据：Gini、coherence、Garvin召回、AUC、消融；支持程度：较强，但部分依赖在线附录。

2. 制品主张：显式多样性正则和分类损失等设计组分带来改进；证据：消融显示η提高可解释性、ρ提高AUC；支持程度：中等，消融只单独变化单个超参数，未系统检验交互。

3. 机制主张：因为概念在同一空间，向量化后才可能惩罚概念距离；多样性约束在相关性约束下提高recall；证据：4.2.3的论证与多样性/召回结果；支持程度：论证加间接证据，缺乏过程归因证据。

4. 边界主张：GDCM是探索性、相关性工具，不能用于因果推断；证据：作者在6.2明确声明，且系数只是线性相关；支持程度：主张与设计一致。

5. 理论贡献：将原型理论实现为文本概念挖掘算法，提供计算化概念工具；证据：理论到损失函数的映射表；支持程度：较强，但仍是算法实现而非新理论命题。

- internal_validity_strategy_cn：多轮超参数搜索、多次运行范围比较、MTurk注意力检查与随机呈现、bootstrap标准误、专家词表稳健性、不同h_overlap阈值、大量baseline和消融分析。

- external_validity_strategy_cn：以Garvin维度作为已知理论构念检验概念召回；与Liu et al. (2019)在类似数据上的因果估计对比；用DonorsChoose的不同Y变量检验敏感性；用TopicGPT等新方法补充；多个基准方法对比。

- what_is_not_actually_tested_cn：没有在多种真实行业现场做因果验证；没有检验GDCM在实际管理者使用中的决策效果；概念重要性没有置信区间；未知概念发现用机器恢复概念作为伪ground truth，不等于真实理论新发现；DonorsChoose实验细节在附录中，无法从主文本核对。

## 贡献闭环

- technical_claim_cn：GDCM作为guided exploration算法，能够同时取得高可解释性、高概念多样性和结果相关性，预测表现优于所有可解释基线并接近黑箱模型。

- artifact_claim_cn：GDCM的具体设计组件——共享嵌入空间、显式多样性正则、稀疏正则、分类损失——共同带来上述改进；其中不同参数对AUC和coherence有可分离的影响。

- mechanism_claim_cn：概念向量化使得概念之间可以显式计算距离并惩罚相似性；在相关性分类损失的约束下，多样性正则通过扩大候选概念空间来提高对相关概念的recall。

- boundary_claim_cn：GDCM是非因果的探索性工具，结果受用户领域判断约束；它适合生成假设，不适合直接产生因果结论。

- reusable_design_knowledge_cn：文本概念挖掘应同时优化三个desiderata：共享语义空间实现空间和预测可解释性；显式多样性正则缓解主题重叠；分类损失保证与管理者结果相关。这些要求可复用于其他文本挖掘任务。

- theoretical_contribution_cn：将原型理论从认知科学带入计算文本分析，使概念原型、概念域和距离度量被具体实现为可训练向量、嵌入空间和相似度函数，为监督主题模型提供了理论驱动的设计模板。

- how_discussion_closes_intro_gap_cn：讨论部分重新连接引言中提出的三个要求：第6节说明GDCM通过可解释概念恢复理论概念、通过多样性发现未知内容、通过相关性提供经济重要性，并把局限明确为探索性与相关性，从而把贡献稳定在“假设生成工具”而非因果或纯预测工具。

- overclaim_or_unsupported_leaps_cn：作者将GDCM系数与Liu et al. (2019)比较并称“closely match”，但两者数据并不完全相同且无统计检验；用Garvin维度作为ground truth可能对GDCM有利；未知概念召回使用伪ground truth也不能等同于真实科学发现；将“高diversity+高recall”解释为“增加发现新概念的可能性”仍是一个推断而非直接证据。

## 句级写作动作图谱

### 1. P1 S1

- order：1

- section：Introduction

- locator：P1 S1

- move_code：CONTEXT

- paraphrase_cn：企业越来越依赖文本数据来支持战略决策。

- rhetorical_function_cn：建立文本分析重要性的现实背景。

- depends_on_cn：无

- sets_up_cn：为后面提出文本概念挖掘需求作铺垫。

- evidence_pointer：Section 1 P1

### 2. P1 S2

- order：2

- section：Introduction

- locator：P1 S2

- move_code：PRACTICAL_STAKES

- paraphrase_cn：文本数据的庞大规模带来认知负担，需要计算化地转换成管理者可理解的概念。

- rhetorical_function_cn：说明文本数据利用中的实际困难。

- depends_on_cn：第1句

- sets_up_cn：引出概念提取的必要性。

- evidence_pointer：Section 1 P1

### 3. P1 S3

- order：3

- section：Introduction

- locator：P1 S3

- move_code：REQUIREMENT

- paraphrase_cn：提取出的概念必须与相关管理结果变量强相关。

- rhetorical_function_cn：提出第一个需求：相关性。

- depends_on_cn：第2句

- sets_up_cn：为GDCM的relevance设计作准备。

- evidence_pointer：Section 1 P1

### 4. P1 S4

- order：4

- section：Introduction

- locator：P1 S4

- move_code：REQUIREMENT

- paraphrase_cn：概念多样性对发现未知构念和生成创新假设至关重要。

- rhetorical_function_cn：提出第二个需求：多样性。

- depends_on_cn：第2句

- sets_up_cn：为GDCM的diversity设计作准备。

- evidence_pointer：Section 1 P1

### 5. P2 S1

- order：5

- section：Introduction

- locator：P2 S1

- move_code：RQ_OR_OBJECTIVE

- paraphrase_cn：本文提出一个名为GDCM的新型文本探索算法。

- rhetorical_function_cn：引入论文核心制品和目标。

- depends_on_cn：前面的背景和需求

- sets_up_cn：给出文章主贡献对象。

- evidence_pointer：Section 1 P2

### 6. P2 S2

- order：6

- section：Introduction

- locator：P2 S2

- move_code：REQUIREMENT

- paraphrase_cn：GDCM围绕三个关键要求：可解释性、多样性和对管理结果的相关性。

- rhetorical_function_cn：明确算法的三个设计要求。

- depends_on_cn：第5句

- sets_up_cn：按这三个要求组织全文和评价。

- evidence_pointer：Section 1 P2

### 7. P3 S1

- order：7

- section：Introduction

- locator：P3 S1

- move_code：THEORY_INTRO

- paraphrase_cn：为了明确文本洞察的目标，作者把“概念”理解为概念理论中的目标构念。

- rhetorical_function_cn：引入理论视角为概念下定义。

- depends_on_cn：第6句

- sets_up_cn：为后续原型理论作铺垫。

- evidence_pointer：Section 1 P3

### 8. P3 S2

- order：8

- section：Introduction

- locator：P3 S2

- move_code：THEORY_PROPOSITION

- paraphrase_cn：概念是思想的积木，是知识和行动的基础。

- rhetorical_function_cn：引用理论命题说明概念的重要性。

- depends_on_cn：第7句

- sets_up_cn：说明GDCM为何从概念理论出发。

- evidence_pointer：Section 1 P3

### 9. P3 S3

- order：9

- section：Introduction

- locator：P3 S3

- move_code：RQ_OR_OBJECTIVE

- paraphrase_cn：GDCM从头设计为识别符合概念理论定义的表征。

- rhetorical_function_cn：强调理论驱动的设计目标。

- depends_on_cn：第8句

- sets_up_cn：预告算法与理论标准的对应。

- evidence_pointer：Section 1 P3

### 10. P4 S1

- order：10

- section：Introduction

- locator：P4 S1

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：图1按探索与提取、引导与非引导两个维度对现有概念挖掘方法分类。

- rhetorical_function_cn：构建方法分类框架，定位现有技术。

- depends_on_cn：第5句

- sets_up_cn：为识别Quadrant II空白提供结构。

- evidence_pointer：Section 1 P4 and Figure 1

### 11. P4 S2-S4

- order：11

- section：Introduction

- locator：P4 S2-S4

- move_code：PHENOMENON

- paraphrase_cn：管理者可能需要验证预定概念、大批量提取已知概念，或在新领域中探索与特定结果相关的概念。

- rhetorical_function_cn：描述管理现实中的不同文本分析任务。

- depends_on_cn：第10句

- sets_up_cn：说明哪些任务已有方法覆盖，哪些存在缺口。

- evidence_pointer：Section 1 P4

### 12. P4 S5

- order：12

- section：Introduction

- locator：P4 S5

- move_code：LIMITATION

- paraphrase_cn：Quadrant II现有方法要么优先预测而牺牲可解释性，要么没有显式优化主题多样性和连贯性。

- rhetorical_function_cn：指出现有guided exploration方法的不足。

- depends_on_cn：第10-11句

- sets_up_cn：为GDCM的定位制造缺口。

- evidence_pointer：Section 1 P4

### 13. P5 S1

- order：13

- section：Introduction

- locator：P5 S1

- move_code：DESIGN_FEATURE

- paraphrase_cn：GDCM属于图1第二象限的可解释深度学习算法。

- rhetorical_function_cn：给出GDCM的技术定位。

- depends_on_cn：第12句

- sets_up_cn：说明GDCM要填补的正是Quadrant II空白。

- evidence_pointer：Section 1 P5

### 14. P5 S2

- order：14

- section：Introduction

- locator：P5 S2

- move_code：THEORY_INTRO

- paraphrase_cn：GDCM依据哲学和认知科学的概念理论设计。

- rhetorical_function_cn：声明理论根基。

- depends_on_cn：第13句

- sets_up_cn：引出四条概念标准。

- evidence_pointer：Section 1 P5

### 15. P5 S3

- order：15

- section：Introduction

- locator：P5 S3

- move_code：THEORY_PROPOSITION

- paraphrase_cn：从理论中提炼出词汇化、概念连贯性、区分性和相关性四条标准。

- rhetorical_function_cn：把理论转化为可操作的标准列表。

- depends_on_cn：第14句

- sets_up_cn：这些标准成为设计的底层原则。

- evidence_pointer：Section 1 P5

### 16. P6 S1

- order：16

- section：Introduction

- locator：P6 S1

- move_code：DESIGN_FEATURE

- paraphrase_cn：GDCM通过定制架构和训练目标满足上述四条标准。

- rhetorical_function_cn：连接理论标准与算法实现。

- depends_on_cn：第15句

- sets_up_cn：进入具体desiderata说明。

- evidence_pointer：Section 1 P6

### 17. P6 S2

- order：17

- section：Introduction

- locator：P6 S2

- move_code：DESIGN_FEATURE

- paraphrase_cn：与Quadrant II其他方法相比，GDCM突出特点是显式增强多样性。

- rhetorical_function_cn：强调算法的新颖性。

- depends_on_cn：第16句

- sets_up_cn：多样性成为后续评价的重点之一。

- evidence_pointer：Section 1 P6

### 18. P6 S3

- order：18

- section：Introduction

- locator：P6 S3

- move_code：MECHANISM

- paraphrase_cn：不同且多样的概念会增加新发现的可能性，这是科学探索的基础。

- rhetorical_function_cn：解释多样性如何带来价值。

- depends_on_cn：第17句

- sets_up_cn：把多样性从工程指标提升为科学发现条件。

- evidence_pointer：Section 1 P6

### 19. P6 bullet 1

- order：19

- section：Introduction

- locator：P6 bullet 1

- move_code：DESIGN_FEATURE

- paraphrase_cn：空间可解释性通过把词、概念、文档嵌入同一多维空间实现，概念可用邻近词解释。

- rhetorical_function_cn：说明空间可解释性的具体机制。

- depends_on_cn：第16句

- sets_up_cn：为4.1的嵌入设计铺路。

- evidence_pointer：Section 1 P6, Figure 2

### 20. P6 bullet 2

- order：20

- section：Introduction

- locator：P6 bullet 2

- move_code：DESIGN_FEATURE

- paraphrase_cn：预测可解释性通过内在线性模型实现，概念与结果关系由权重描述。

- rhetorical_function_cn：说明预测层设计。

- depends_on_cn：第16句

- sets_up_cn：为分类损失和系数报告作准备。

- evidence_pointer：Section 1 P6

### 21. P6 bullet 3

- order：21

- section：Introduction

- locator：P6 bullet 3

- move_code：DESIGN_FEATURE

- paraphrase_cn：多样性通过迫使概念在概念空间中彼此远离实现，从而提高潜在概念召回。

- rhetorical_function_cn：说明多样性正则的设计。

- depends_on_cn：第19句

- sets_up_cn：为L_div损失作铺垫。

- evidence_pointer：Section 1 P6

### 22. P6 bullet 4

- order：22

- section：Introduction

- locator：P6 bullet 4

- move_code：DESIGN_FEATURE

- paraphrase_cn：相关性通过把概念集中于与结果高度相关的概念空间子区域实现。

- rhetorical_function_cn：说明相关性正则的设计。

- depends_on_cn：第19-20句

- sets_up_cn：为L_clf分类损失作铺垫。

- evidence_pointer：Section 1 P6

### 23. P7 S1

- order：23

- section：Introduction

- locator：P7 S1

- move_code：MECHANISM

- paraphrase_cn：三个desiderata缺一不可，缺少任何一个都会显著削弱模型有效性。

- rhetorical_function_cn：解释三个要求的互补性。

- depends_on_cn：第21-22句

- sets_up_cn：说明为什么需要联合优化而不是单一指标。

- evidence_pointer：Section 1 P7

### 24. P8 S1

- order：24

- section：Introduction

- locator：P8 S1

- move_code：STUDY_OVERVIEW

- paraphrase_cn：第5节将在电子商务评论与转化的场景中展示GDCM在这些标准上的表现。

- rhetorical_function_cn：预告后续评价结构。

- depends_on_cn：第23句

- sets_up_cn：为评价章节提供路标。

- evidence_pointer：Section 1 P8

### 25. P1 S1

- order：25

- section：Section 2.1

- locator：P1 S1

- move_code：THEORY_INTRO

- paraphrase_cn：古典概念理论要求严格定义标准，而原型理论与现代认知科学更契合。

- rhetorical_function_cn：在多种理论中选择原型理论。

- depends_on_cn：第15句

- sets_up_cn：为(A,d,p)形式化作准备。

- evidence_pointer：Section 2.1 P1

### 26. P1 S2

- order：26

- section：Section 2.1

- locator：P1 S2

- move_code：THEORY_PROPOSITION

- paraphrase_cn：原型理论中，概念可表示为(A,d,p)，p是原型，d是成员到原型的距离。

- rhetorical_function_cn：给出可数学化的概念定义。

- depends_on_cn：第25句

- sets_up_cn：之后GDCM直接操作这个三元组。

- evidence_pointer：Section 2.1 P1

### 27. P2 S1

- order：27

- section：Section 2.1

- locator：P2 S1

- move_code：REQUIREMENT

- paraphrase_cn：在GDCM中，概念域A对应共享嵌入空间，距离d对应向量相似度，原型p对应概念嵌入。

- rhetorical_function_cn：把理论概念翻译成算法组件。

- depends_on_cn：第26句

- sets_up_cn：为具体网络设计提供映射。

- evidence_pointer：Section 2.1 P2

### 28. P3 S1

- order：28

- section：Section 2.1

- locator：P3 S1

- move_code：DESIGN_FEATURE

- paraphrase_cn：词汇化通过词嵌入实现，概念原型用最近的词解释。

- rhetorical_function_cn：说明词汇化如何在设计中实现。

- depends_on_cn：第27句

- sets_up_cn：给出空间可解释性的具体机制。

- evidence_pointer：Section 2.1 P3

### 29. P3 S3

- order：29

- section：Section 2.1

- locator：P3 S3

- move_code：DESIGN_FEATURE

- paraphrase_cn：区分性通过惩罚概念嵌入之间的相似性实现。

- rhetorical_function_cn：说明区分性设计。

- depends_on_cn：第27句

- sets_up_cn：对应L_div损失。

- evidence_pointer：Section 2.1 P3

### 30. P4 S1

- order：30

- section：Section 2.1

- locator：P4 S1

- move_code：CONTRIBUTION

- paraphrase_cn：GDCM在统一语义空间中实现概念原型和成员，并用损失函数优化多样性和相关性。

- rhetorical_function_cn：小结理论到设计的完成。

- depends_on_cn：第28-29句

- sets_up_cn：为第4节模型细节作总结。

- evidence_pointer：Section 2.1 P4

### 31. P5 S1

- order：31

- section：Section 2.1

- locator：P5 S1

- move_code：LIMITATION

- paraphrase_cn：LDA及其变体的主题可粗看为原型，但主题与成员不在同一空间，违反原型理论要求。

- rhetorical_function_cn：指出传统主题模型的理论缺陷。

- depends_on_cn：第26句

- sets_up_cn：说明为什么GDCM把概念和词放在同一空间。

- evidence_pointer：Section 2.1 P5

### 32. P3 S3

- order：32

- section：Section 2.2

- locator：P3 S3

- move_code：LIMITATION

- paraphrase_cn：无监督主题模型找出的主题常缺少概念的desiderata，出现intrusion和diffusion。

- rhetorical_function_cn：概括现有主题模型在概念质量上的问题。

- depends_on_cn：第31句

- sets_up_cn：为GDCM的coherence和differentiation目标提供动机。

- evidence_pointer：Section 2.2 P3

### 33. P5 S2

- order：33

- section：Section 2.2

- locator：P5 S2

- move_code：GAP

- paraphrase_cn：现有guided exploration方法也缺少概念理论根基，因此作者设计GDCM来填补Quadrant II的缺口。

- rhetorical_function_cn：直接声明文献缺口。

- depends_on_cn：第32句

- sets_up_cn：把GDCM的提出框定为必要填充。

- evidence_pointer：Section 2.2 P5

### 34. P1 S1

- order：34

- section：Section 2.3

- locator：P1 S1

- move_code：PRACTICAL_STAKES

- paraphrase_cn：高性能黑箱算法难以给出预测理由，造成审计、责任和隐私等高风险问题。

- rhetorical_function_cn：说明可解释性的实际重要性。

- depends_on_cn：无

- sets_up_cn：为GDCM强调可解释性提供背景。

- evidence_pointer：Section 2.3 P1

### 35. P6 S1

- order：35

- section：Section 2.3

- locator：P6 S1

- move_code：RQ_OR_OBJECTIVE

- paraphrase_cn：本文在guided exploration任务中谨慎设计可解释ML，并用coherence和人类判断测量可解释性。

- rhetorical_function_cn：声明本文在可解释文献中的具体做法。

- depends_on_cn：第34句和第33句

- sets_up_cn：为后续评价指标选择铺路。

- evidence_pointer：Section 2.3 P6

### 36. P2 S1

- order：36

- section：Section 3.1

- locator：P2 S1

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：作者用浏览和评论阅读数据构造购买或放弃的决策旅程。

- rhetorical_function_cn：说明评价所用数据的构造逻辑。

- depends_on_cn：第35句

- sets_up_cn：定义后面的UserID-ProductID分析单位。

- evidence_pointer：Section 3.1 P2

### 37. P1 S1

- order：37

- section：Section 3.2

- locator：P1 S1

- move_code：PHENOMENON

- paraphrase_cn：管理者可以利用转化率、辅助数据和产品评论来识别与转化相关的概念。

- rhetorical_function_cn：描述GDCM目标使用场景。

- depends_on_cn：第36句

- sets_up_cn：说明任务是从数据中找出管理者不知道但相关的概念。

- evidence_pointer：Section 3.2 P1

### 38. P2 S1

- order：38

- section：Section 3.2

- locator：P2 S1

- move_code：LIMITATION

- paraphrase_cn：现有guided exploration方法只部分实现目标，尤其缺少多样性正则，导致主题重叠和重要因素遗漏。

- rhetorical_function_cn：再次确认缺口并具体化为多样性缺失。

- depends_on_cn：第33句

- sets_up_cn：引出GDCM以多样性为核心改进。

- evidence_pointer：Section 3.2 P2

### 39. P3 S1

- order：39

- section：Section 3.2

- locator：P3 S1

- move_code：RESULT

- paraphrase_cn：图3显示LDA生成的主题词既有词入侵又有概念扩散，管理者难以直接使用。

- rhetorical_function_cn：用具体输出展示现有方法的失败。

- depends_on_cn：第38句

- sets_up_cn：为GDCM改进点提供可视化证据。

- evidence_pointer：Section 3.2 P3 and Figure 3

### 40. P1 S1

- order：40

- section：Section 4.1

- locator：P1 S1

- move_code：DESIGN_FEATURE

- paraphrase_cn：GDCM由概念分配网络、嵌入网络和分类器三部分组成，损失函数包含嵌入、稀疏、多样性和分类四项。

- rhetorical_function_cn：给出算法总体结构。

- depends_on_cn：第27句

- sets_up_cn：后续逐项解释每个loss。

- evidence_pointer：Section 4.1 P1

### 41. P4 S1

- order：41

- section：Section 4.1.2

- locator：P4 S1

- move_code：DESIGN_FEATURE

- paraphrase_cn：文档嵌入被表示为概念嵌入的加权线性组合。

- rhetorical_function_cn：说明文档与概念的包含关系。

- depends_on_cn：第40句

- sets_up_cn：使文档和概念处于同一空间。

- evidence_pointer：Section 4.1.2 P4

### 42. P1 S1

- order：42

- section：Section 4.1.3

- locator：P1 S1

- move_code：REQUIREMENT

- paraphrase_cn：GDCM希望每个文档主要表现少量概念，稀疏性可提升预测可解释性。

- rhetorical_function_cn：说明稀疏正则的必要性。

- depends_on_cn：第40句

- sets_up_cn：引入L_spr。

- evidence_pointer：Section 4.1.3 P1

### 43. P1 S2

- order：43

- section：Section 4.1.4

- locator：P1 S2

- move_code：DESIGN_FEATURE

- paraphrase_cn：为提升概念多样性，GDCM惩罚每对概念嵌入之间的点积相似度。

- rhetorical_function_cn：说明多样性正则的具体形式。

- depends_on_cn：第40句

- sets_up_cn：引入L_div。

- evidence_pointer：Section 4.1.4 P1-S2

### 44. P2 S1

- order：44

- section：Section 4.1.5

- locator：P2 S1

- move_code：DESIGN_FEATURE

- paraphrase_cn：GDCM加入分类损失，用概念的线性组合来预测管理结果Y。

- rhetorical_function_cn：说明相关性loss的作用机制。

- depends_on_cn：第40句

- sets_up_cn：引入L_clf和可比较的系数。

- evidence_pointer：Section 4.1.5 P2

### 45. P2 S1

- order：45

- section：Section 4.2.3

- locator：P2 S1

- move_code：MECHANISM

- paraphrase_cn：由于在guided exploration中不知道真正要发现的概念，无法直接优化recall，于是先优化多样性；相关性约束限定假设空间，多样性正则则在这个空间内提高recall。

- rhetorical_function_cn：解释GDCM为何用多样性作为recall代理。

- depends_on_cn：第43-44句

- sets_up_cn：使后面用多样性评价recall成为合理的推理。

- evidence_pointer：Section 4.2.3 P2

### 46. Table 5前一句

- order：46

- section：Section 5

- locator：Table 5前一句

- move_code：STUDY_OVERVIEW

- paraphrase_cn：表5列出后续实验，分别对应可解释性、多样性和相关性三个评价维度。

- rhetorical_function_cn：预告整个评价章节的结构。

- depends_on_cn：第45句

- sets_up_cn：让读者知道每个实验分别检验什么。

- evidence_pointer：Section 5 intro and Table 5

### 47. P1 S1

- order：47

- section：Section 5.1.1

- locator：P1 S1

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：作者用Amazon MTurk调查来评估GDCM和若干主题模型的可解释性。

- rhetorical_function_cn：引入人类判断作为可解释性证据。

- depends_on_cn：第46句

- sets_up_cn：描述评价语料和任务。

- evidence_pointer：Section 5.1.1 P1

### 48. P2 S1

- order：48

- section：Section 5.1.1

- locator：P2 S1

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：采用Gini系数衡量MTurk工人对每个主题所属Garvin维度的一致性，Gini越高说明主题越清晰可解释。

- rhetorical_function_cn：给出人类可解释性的量化指标。

- depends_on_cn：第47句

- sets_up_cn：提供图4的统计基础。

- evidence_pointer：Section 5.1.1 P2

### 49. P4 S1

- order：49

- section：Section 5.1.1

- locator：P4 S1

- move_code：RESULT

- paraphrase_cn：GDCM在Gini系数上最高，说明MTurk工人对GDCM主题的概念共识更强。

- rhetorical_function_cn：报告可解释性的人类判断结果。

- depends_on_cn：第48句

- sets_up_cn：为可解释性主张提供核心证据之一。

- evidence_pointer：Section 5.1.1 and Figure 4

### 50. P2 S1

- order：50

- section：Section 5.1.2

- locator：P2 S1

- move_code：RESULT

- paraphrase_cn：GDCM平均coherence为-1.86，高于LDA的-2.25，且多轮运行范围不重叠。

- rhetorical_function_cn：报告算法coherence结果，增强可解释性证据的稳健性。

- depends_on_cn：第49句

- sets_up_cn：同时指出sDTM/sLDA高coherence可能是词重复导致的。

- evidence_pointer：Section 5.1.2 and Table 10

### 51. P1 S1

- order：51

- section：Section 5.2.1

- locator：P1 S1

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：作者用MTurk分类向量计算主题间的平均成对余弦距离来测多样性，并用unique top Garvin维度计数测召回。

- rhetorical_function_cn：定义多样性的量化方法。

- depends_on_cn：第46句

- sets_up_cn：为图5和图6提供方法。

- evidence_pointer：Section 5.2.1

### 52. P2 S1

- order：52

- section：Section 5.2.1

- locator：P2 S1

- move_code：RESULT

- paraphrase_cn：GDCM识别出更多不同的Garvin维度并恢复更多独特Garvin维度。

- rhetorical_function_cn：报告多样性/召回的人类判断结果。

- depends_on_cn：第51句

- sets_up_cn：支持GDCM比现有方法更分散且召回更高。

- evidence_pointer：Section 5.2.1 and Figure 5

### 53. P1 S1

- order：53

- section：Section 5.2.2

- locator：P1 S1

- move_code：BENCHMARK_OR_CONTRAST

- paraphrase_cn：作者以Garvin维度作为ground truth，用词重叠阈值计算各算法对已知概念的召回。

- rhetorical_function_cn：建立可量化的已知概念基准。

- depends_on_cn：第52句

- sets_up_cn：为表8的对比提供逻辑。

- evidence_pointer：Section 5.2.2 and Table 7/8

### 54. P2 S2

- order：54

- section：Section 5.2.2

- locator：P2 S2

- move_code：RESULT

- paraphrase_cn：GDCM仅用5次运行就能恢复比基准方法50或150次运行更多的ground truth概念。

- rhetorical_function_cn：报告已知概念召回的最强对比结果。

- depends_on_cn：第53句

- sets_up_cn：支持GDCM高效发现已知理论概念。

- evidence_pointer：Section 5.2.2 and Table 8

### 55. P1 S1

- order：55

- section：Section 5.3.1

- locator：P1 S1

- move_code：BENCHMARK_OR_CONTRAST

- paraphrase_cn：作者把GDCM与一组可解释基线和一组不可解释预测模型比较预测表现。

- rhetorical_function_cn：为相关性维度建立预测基准。

- depends_on_cn：第46句

- sets_up_cn：报告AUC和ROC结果。

- evidence_pointer：Section 5.3.1 and Table 9

### 56. P4 S2

- order：56

- section：Section 5.3.1

- locator：P4 S2

- move_code：RESULT

- paraphrase_cn：GDCM AUC为0.8885，超过所有可解释基线，仅略低于CNN和XGB。

- rhetorical_function_cn：报告预测相关性结果。

- depends_on_cn：第55句

- sets_up_cn：支撑GDCM在保持可解释的同时接近黑箱预测性能。

- evidence_pointer：Section 5.3.1 and Table 10

### 57. P1 S1

- order：57

- section：Section 5.3.2

- locator：P1 S1

- move_code：DESIGN_FEATURE

- paraphrase_cn：GDCM可输出挖掘概念相对用户指定X的相关重要性。

- rhetorical_function_cn：说明GDCM的管理者输出形式。

- depends_on_cn：第44句

- sets_up_cn：为系数分析提供基础。

- evidence_pointer：Section 5.3.2 P1

### 58. P3 S2

- order：58

- section：Section 5.3.2

- locator：P3 S2

- move_code：RESULT

- paraphrase_cn：美学概念对转化的正相关最高，服务性与退换相关概念最低，且与Liu et al. (2019)的系数接近。

- rhetorical_function_cn：报告系数和外部对照。

- depends_on_cn：第57句

- sets_up_cn：作为外部效度证据。

- evidence_pointer：Section 5.3.2 and Figure 8

### 59. P1 S1

- order：59

- section：Section 5.3.3.2

- locator：P1 S1

- move_code：ROBUSTNESS_OR_BOUNDARY_TEST

- paraphrase_cn：消融分析显示提高分类损失权重会提高AUC，提高多样性权重会提高可解释性，提高稀疏权重会降低AUC。

- rhetorical_function_cn：检验每个设计组分的直接作用。

- depends_on_cn：第56句

- sets_up_cn：为artifact claim提供组分级证据。

- evidence_pointer：Section 5.3.3.2 and Figure 9

### 60. P2 S1

- order：60

- section：Section 5.4

- locator：P2 S1

- move_code：CONTRIBUTION

- paraphrase_cn：在未知概念场景中，LDA多次运行无法恢复多数Garvin概念，而GDCM五次运行即可恢复，说明GDCM对文本洞察的潜在价值。

- rhetorical_function_cn：把各评价汇总为整体贡献。

- depends_on_cn：第54句和第59句

- sets_up_cn：进入管理与研究含义。

- evidence_pointer：Section 5.4

### 61. P1 S1

- order：61

- section：Section 6.2

- locator：P1 S1

- move_code：BOUNDARY_CONDITION

- paraphrase_cn：GDCM是探索性、相关性的非因果工具，只能帮助生成假设和构建理论，需要用户用领域知识判断。

- rhetorical_function_cn：明确方法边界，防止贡献被误读为因果。

- depends_on_cn：第60句

- sets_up_cn：为未来使用提供约束。

- evidence_pointer：Section 6.2

### 62. P1 S1

- order：62

- section：Section 7

- locator：P1 S1

- move_code：CONTRIBUTION

- paraphrase_cn：作者总结GDCM由管理结果变量引导，对文本进行探索、组织和信息提取。

- rhetorical_function_cn：用一句话完成结论。

- depends_on_cn：第61句

- sets_up_cn：无，文章结束。

- evidence_pointer：Section 7

### 63. Figure A.1后

- order：63

- section：Appendix A

- locator：Figure A.1后

- move_code：RESULT

- paraphrase_cn：TopicGPT虽然能捕捉部分正确概念，但也产生与原文无关的幻觉标签。

- rhetorical_function_cn：展示LLM主题模型在解释上的缺陷。

- depends_on_cn：第56句

- sets_up_cn：为LLM基线性能不足提供视觉证据。

- evidence_pointer：Appendix A and Figure A.1

### 64. Table A.2后

- order：64

- section：Appendix A

- locator：Table A.2后

- move_code：LIMITATION

- paraphrase_cn：TopicGPT即使加入种子和自我纠正，最佳版本仍明显低于GDCM。

- rhetorical_function_cn：报告LLM对比结果并限制其替代性。

- depends_on_cn：第63句

- sets_up_cn：排除LLM方法作为主要竞争者。

- evidence_pointer：Appendix A and Table A.2

## 写作技术

- gap_construction_cn：先用2x2图把方法分类，指出Quadrant II现有方法要么黑箱、要么缺少显式多样性和理论根基；再用图3展示具体词的入侵和扩散，造成“即使有guidance也得到不可用输出”的直观缺口。

- signposting_cn：开篇列出三个requirements，Table 5把后续实验映射到desiderata，每节标题和Table 2重复对应关系；常用“We benchmark...”“Table 5 lists...”等路标句。

- transition_logic_cn：从理论到模型用“operationalization”衔接；每个评价小节先声明desideratum，再给基准和证据，最后以“尚缺另一维度”引出下一节；从相关性到外部效度用“Lastly, we highlight...”推进。

- claim_evidence_rhythm_cn：先给总体命题（如“GDCM excels...”），再列图表数据，再解释与基准的关系或限制；结果段落常以粗体或对比句收束。

- benchmark_narrative_cn：benchmark不是单一大榜，而是按desideratum分层：可解释性用MTurk+coherence，多样性用Garvin召回和未知概念覆盖，相关性用AUC和外部因果对照；每层都有独立的对比集。

- theory_return_cn：在4.2和6.2将loss对应回概念理论；用外部因果研究和Garvin维度证明GDCM发现的概念具有理论/经济意义；在局限中说明非因果性，避免过度推广。

- contribution_positioning_cn：强调GDCM是“guided exploration”工具而非预测模型；贡献是发现概念和生成假设，不是替代因果研究；同时给出管理与研究双侧含义。

- novelty_protection_cn：通过“explicit diversity + shared embedding + classification loss”三合一同时优化，并且用少量运行恢复已知概念和匹配因果研究，证明不是一次性性能结果；用消融和Y敏感性证明组分有效且可调节。

## 可复用研究与写作程序

### structure_steps

#### 1. 1

- step：1

- writing_job_cn：建立核心构念的严格定义，并从理论中提炼标准。

- research_job_cn：选择一种可形式化的理论（如原型理论），提炼可操作的标准。

- required_evidence_cn：能说明为什么该理论比竞争者更适合计算化。

- transition_to_next_cn：把标准转化为算法需要满足的要求。

#### 2. 2

- step：2

- writing_job_cn：用表格或图示对照现有方法，指出它们在哪些desiderata上缺失。

- research_job_cn：对已有方法进行结构化分类，定位空白。

- required_evidence_cn：能具体指出缺失维度，最好有样例输出。

- transition_to_next_cn：从缺口引出新算法/设计。

#### 3. 3

- step：3

- writing_job_cn：呈现算法总体结构并逐项说明每个设计如何对应要求。

- research_job_cn：实现每个desideratum对应的模型组件或损失。

- required_evidence_cn：形式化loss和结构图，以及理论映射表。

- transition_to_next_cn：说明评价所用的数据与任务。

#### 4. 4

- step：4

- writing_job_cn：描述评价场景、数据来源和构造逻辑。

- research_job_cn：找到同时有文本、管理结果Y和辅助X的现实数据集。

- required_evidence_cn：数据构造细节、描述统计、分析单位定义。

- transition_to_next_cn：进入分维度评价。

#### 5. 5

- step：5

- writing_job_cn：按每个desideratum分别设计评价并报告结果。

- research_job_cn：使用人类判断、算法指标、基准比较、外部效度等多种证据。

- required_evidence_cn：每个desideratum都有至少一个直接指标。

- transition_to_next_cn：每个小节末尾说明该维度证据的局限并引到下个维度。

#### 6. 6

- step：6

- writing_job_cn：做稳健性检验，包括消融和场景敏感性。

- research_job_cn：变化关键超参数、改变Y、增加新benchmark。

- required_evidence_cn：证明设计和结论不是偶然，并揭示组分作用。

- transition_to_next_cn：总结整体证据。

#### 7. 7

- step：7

- writing_job_cn：在讨论中声明贡献和边界，尤其区分相关性与因果。

- research_job_cn：把结果放回理论，同时给出用户/研究者使用限制。

- required_evidence_cn：能够回指理论映射，并明确未检验内容。

- transition_to_next_cn：与引言中的缺口闭合。

### most_transferable_moves_cn

1. 用理论定义核心构念并直接作为算法设计依据

2. 用2x2分类定位自己的算法并制造缺口

3. 把评价分解成多个desiderata而不是单一性能指标

4. 用人类判断和算法指标双重验证可解释性

5. 用已知理论构念和外部因果研究作为效度锚点

6. 在贡献中老实降级为探索性/相关性工具

### resource_intensive_or_nonstandard_parts_cn

1. 在线零售商的真实点击流、评论阅读时长和转化数据不易获得

2. MTurk人类标注实验和Garvin专家词表需要人力成本

3. 大规模深度学习模型训练依赖GPU资源（作者致谢Nvidia）

4. Liu et al. (2019)同类因果估计数据无法随意复制

5. DonorsChoose和未知概念召回细节放在在线附录，需额外资源验证

### what_not_to_copy_superficially_cn

1. 如果模型没有概念向量化，就不能声称“多样性通过向量距离”

2. 如果没有人类判断、召回或因果对照，不能只报告AUC

3. 不要把自己的黑箱模型称为可解释，除非有线性层和同空间嵌入

4. 不要在没有类似ground truth或因果对照时宣称“发现理论概念”

5. 不要在相关证据不足时宣称因果或普适边界

- single_best_description_of_the_routine_cn：以理论定义概念，把理论标准转成可训练的loss，再按每个desideratum分别构造mini-evaluation，最后用已知理论/因果研究做外部锚定，同时声明探索性边界。

## 分析边界

仅提供主文本；Online Appendix B.1/B.2/B.5/B.6/C未提供，部分结果只能引用而无法核对；部分图以图片形式存在，无法解析精确数值；全文没有页码，句子位置基于章节段落估计；TopicGPT和DonorsChoose实验细节在附录中，无法从主文本充分验证。
