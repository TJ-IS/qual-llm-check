# Automating in High-Expertise, Low-Label Environments: Evidence-Based Medicine by Expert-Augmented Few-Shot Learning

- 作者：Rong Liu; Jingjing Li; Marko Zivkovic; Ahmed Abbasi
- 年份 / 期刊：2025 / MIS Quarterly
- DOI：10.25300/misq/2024/18573
- 源文件：13398_2025_automating-in-high-expertise-low-label-environments-evidence-based-medicine-by-expert-augmented.md
- 论文主类型：build_evaluate_design_science
- 主导写作弧线：requirements_build_evaluate_design_principles
- 置信度：0.85

## 文章级论证概况

- 核心问题：如何为高专家性、低标注数据的系统综述（SR）数据抽取任务设计一个既能最小化人工标注量、又能吸收医学专家意义建构知识的计算设计制品，从而自动化或增强证据医学中的PICO要素抽取过程？

- 制品与设计：提出FastSR，一个基于专家增强少样本学习（FSL）的端到端深度学习框架。其核心设计是在ProtoNet结构上扩展多种原型：用BioBERT+CNN生成句子的局部语义表示；用PubMed预训练的分层嵌入和pointer network生成句子全局章节背景表示；用全局注意力从支持集中提炼PICO文本片段表示；再用fragment-attended query表示和跨任务一致性正则化实现句子分类与序列标注的联合学习。

- 客观结果：在Wilson disease（WD）、COVID-19和公开EBM-NLP三个数据集上，FastSR在句子分类与PICO片段序列标注的P@3、R@3、F1@3和PRC指标上显著优于传统深度学习、半监督、LLM和FSL基准；消融实验表明全局上下文、注意力片段表示和联合学习均有显著贡献；下游SR报告与专家人工报告更接近；访谈获得积极反馈；时间成本估算显示相比人工SR可节省约65%时间和每项目约73,500美元。

- 核心贡献：面向高专家性、低标签流程自动化环境，提出四项设计需求DR1-DR4，构建理论指导的计算设计制品FastSR，并给出从任务复杂度到设计需求再到设计组件的映射；通过三数据集基准、消融、下游报告生成、专家访谈和时间成本分析形成多侧面评价；提出FastSR增强的SR半自动流程，为IS计算设计研究提供可复用的设计知识和评价模板。

- 整篇论证链：作者首先指出许多真实流程自动化环境具有高专家性和极少标注数据，而现有IS计算制品多聚焦于标注充足、任务定义良好的情境；他们选择系统综述（SR）数据抽取作为代表性问题，因为SR对EBM至关重要却极其耗时，且现有ML/NLP方案因标注稀缺、精度不足、没有充分模拟专家标注逻辑而受限。随后，通过SR流程文献回顾和专家访谈，提炼出数据抽取的四大任务复杂度，并借助组合性理论和sensemaking知识提出四项设计要求。FastSR作为满足这些要求的制品被构建：在少样本原型网络中加入局部语义、全局上下文、注意力片段语义和联合学习组件。为验证设计，作者在三数据集上开展句子分类和序列标注的全面基准评价，用消融检验每个组件，再通过真实SR公司的下游报告生成、专家访谈和时间成本估算展示实际价值，最后提出FastSR增强SR协议，并把成果回接到高专家性低标签环境下的计算设计研究贡献。

## 类型与写作弧线判定

- 论文主类型判定：文章明确遵循计算设计科学范式：从任务复杂度提炼设计需求，依据需求构建FastSR制品，然后用benchmarking、消融、下游案例和专家访谈进行多侧面评价，最终输出可复用的设计需求和增强流程，而不是仅以单一benchmark为主要贡献。

- 主导写作弧线判定：全文主干是：问题背景→任务复杂度→设计要求（DR1-DR4）→制品构建→多阶段评价→设计知识/协议输出。讨论部分也回到设计原则和理论，因此属于“要求—构建—评价—设计原则”的写作弧线。

## 研究开展程序

- study_or_phase_count：7

- 研究阶段总序列：第一阶段先做领域分析和需求提炼，定义DR1-DR4；第二阶段把需求实现为FastSR体系结构；第三和第四阶段分别在三个数据集上检验句子分类和序列标注，形成从“能否识别相关句子”到“能否抽取准确片段”的递进；第五阶段通过消融和样本敏感性证明组件因果贡献及边界；第六阶段跳出离线指标，进入真实SR工作流，考察报告质量、专家接受度和经济性；第七阶段把试验性结论上升为新的SR协议和可迁移设计知识。

### studies_or_phases

#### 1. 任务复杂度与设计要求提炼

- order：1

- name_cn：任务复杂度与设计要求提炼

- question_cn：SR数据抽取为什么难以自动化？需要满足哪些设计要求？

- inputs_and_setting_cn：SR方法学文献、SR自动化文献、SR专家访谈；Cochrane手册和PRISMA等作为领域知识来源。

- designed_or_compared_object_cn：把SR流程拆分为计划、检索、筛选、数据抽取和证据综合五步，识别最劳动密集且IT支持最弱的一步。

- baseline_control_or_counterfactual_cn：已有的SR自动化方案被归为传统分类器、半监督、LLM和FSL四类，并指出其各自局限。

##### objective_metrics

（空）

- analysis_method_cn：文献综述与专家咨询驱动的定性任务分析；从任务复杂度映射到设计需求（Table 1-3）。

- main_result_cn：数据抽取是SR中最耗时、支持最差的步骤；四个任务复杂度导致四项设计要求DR1-DR4。

- argumentative_role_cn：为整个制品构建提供“为什么需要FastSR”的问题基础，并把技术设计绑定到领域真实约束。

- remaining_uncertainty_cn：尚未证明这些设计要求是否真的能被FSL组件满足，也没有量化性能指标。

- link_to_next_phase_cn：四项设计要求成为下一阶段FastSR体系结构设计的功能规格。

##### evidence_pointers

1. Section 'SR Automation: Task Complexity, Design Requirements, and Related Literature'

2. Table 1-3

#### 2. FastSR体系结构设计与构建

- order：2

- name_cn：FastSR体系结构设计与构建

- question_cn：如何把DR1-DR4转化为具体的FSL网络组件和损失函数？

- inputs_and_setting_cn：少样本学习、BioBERT/SciBERT、CNN、hierarchical embedding、attention、MTL等NLP/ML技术基础；来自SR专家标注逻辑的PICO例示。

- designed_or_compared_object_cn：FastSR整体架构及四个关键模块：局部语义表示、全局上下文表示、注意力片段表示、混合联合学习。

- baseline_control_or_counterfactual_cn：以标准ProtoNet为基本对比形态，并指出MAML/matching net等替代FSL为何不适用。

##### objective_metrics

（空）

- analysis_method_cn：架构设计、公式化建模（Equations 1-19）和伪代码/实现描述。

- main_result_cn：形成可运行的FastSR模型：二路k-shot FSL、多原型距离、跨任务一致性损失。

- argumentative_role_cn：把设计需求翻译成可被后续实验检验的对象，即“哪些组件被加入/移除会产生差异”。

- remaining_uncertainty_cn：架构是否真的有效尚无证据，需要基准测试和消融。

- link_to_next_phase_cn：构建完成后自然进入三数据集上的句子分类基准测试。

##### evidence_pointers

1. Section 'FastSR: A Customized Few-Shot Deep Learning Framework'

2. Figure 1 and Equations (1)-(19)

#### 3. 三数据集句子分类基准评价

- order：3

- name_cn：三数据集句子分类基准评价

- question_cn：FastSR是否能在低标签高专长场景下比现有ML方案更准确地识别PICO要素相关句子？

- inputs_and_setting_cn：WD全文学术文章（私有SR项目）、COVID-19全文学术文章（CORD-19 + 专家标注）、EBM-NLP公开RCT摘要；训练集仅有数百句标注。

- designed_or_compared_object_cn：FastSR与Naïve Bayes、SVM、LSTM/CNN、VAT SSL、fine-tuned BioBERT、GPT-4 few-shot、MAML、FSL_DS、L2AC、Matching Net、ProtoNet等比较；同时比较BERT/SciBERT嵌入变体。

- baseline_control_or_counterfactual_cn：基准模型分组覆盖传统ML、半监督、LLM和FSL四类；另外用WD训练后的模型直接复用到COVID检验可迁移性。

##### objective_metrics

1. P@3

2. R@3

3. F1@3

4. PRC

- analysis_method_cn：逐篇文章扫描并取Top-3句子；显著性检验（t-test）比较F1和PRC差异；部分模型用作者原始实现。

- main_result_cn：FastSR在WD上F1@3约73%、PRC约72.6%，显著超过最强基准；在COVID复用和新训练场景均最佳；在EBM-NLP上仍领先，但与LLM差距因数据污染而缩小。

- argumentative_role_cn：证明FastSR作为整体制品在核心任务T1上的有效性，并展示跨疾病/文体/公开私有数据的可泛化性。

- remaining_uncertainty_cn：句子识别正确并不代表PICO片段边界正确，T2尚未被检验。

- link_to_next_phase_cn：在最好的句子分类器基础上耦合序列标签器，进入片段抽取评价。

##### evidence_pointers

1. Tables 7-9

2. Section 'Evaluation Results: Benchmarking: Sentence Classification'

#### 4. 三数据集序列标注基准评价

- order：4

- name_cn：三数据集序列标注基准评价

- question_cn：FastSR能否在正确句子基础上准确识别PICO文本片段，且语义对应优于词面匹配？

- inputs_and_setting_cn：WD、COVID、EBM-NLP的片段级标注；句子分类器输出的Top-3句子作为片段抽取输入。

- designed_or_compared_object_cn：FastSR的序列标签器与Linear/CRF/LSTM/LSTM+CRF、VAT上的Linear tagger、fine-tuned BioBERT、GPT-4 few-shot、ProtoNER、Nearest Neighbor比较。

- baseline_control_or_counterfactual_cn：传统标签器、半监督标签器、LLM标签器和FSL标签器四组对照；另用BERTScore作为语义相似度指标，与词面F1形成对比。

##### objective_metrics

1. F1_word@3

2. F1_BERT@3

3. PRC

- analysis_method_cn：在Top-3句子上计算词面F1和BERTScore F1；GPT模型因成本和句子性能原因未在WD/COVID上做标注。

- main_result_cn：FastSR在三个数据集上均取得最高F1_word、F1_BERT和PRC；在WD上F1_word@3约60.8%，比LSTM+CRF高约15%，比ProtoNER高约4%；在COVID复用和风险因子新类上也显著领先；EBM-NLP上GPT-4片段标注大幅落后。

- argumentative_role_cn：证明FastSR在T2上也有效，从而T1+T2构成的完整数据抽取能力得到验证。

- remaining_uncertainty_cn：离线指标仍不一定等于真实SR报告质量；未检验错误在完整流程中如何被专家修正。

- link_to_next_phase_cn：用消融检验“为什么FastSR有效”，再进入下游SR自动化应用。

##### evidence_pointers

1. Tables 10-12

2. Section 'Evaluation Results: Benchmarking: Sequence Tagging'

#### 5. 消融与稳健性分析

- order：5

- name_cn：消融与稳健性分析

- question_cn：FastSR的改进究竟来自哪些设计组件？在更少样本和更大样本条件下表现如何？

- inputs_and_setting_cn：WD、EBM-NLP数据集及FastSR全模型；对WD减少1/3训练样本并构造10个子集；EBM-NLP采样200/300/500训练样本。

- designed_or_compared_object_cn：移除全局上下文（M1）、移除注意力片段表示（M2）、移除联合学习（M3）、组合移除（M4-M6）；替代设计：层级MTL架构（M7）、图摘要全局上下文（M8）。

- baseline_control_or_counterfactual_cn：全模型为参照，消融模型和替代架构为对照；还对比了分层架构和替代全局上下文模块。

##### objective_metrics

1. F1@3

2. PRC

3. F1_word@3

4. F1_BERT@3

- analysis_method_cn：逐组件移除和双移除；替代组件测试；样本量敏感性测试；误差分析见Appendix H。

- main_result_cn：移除任意一个核心组件都会显著降低句子分类和片段抽取指标；替代全局上下文或层级MTL也较差；减少1/3样本仅造成约3-5%下降；样本量增加时FastSR与基准差距缩小，显示样本效率。

- argumentative_role_cn：把“整体性能好”上升为“每个设计组件都有因果贡献”，支撑DR1-DR4与设计组件的对应关系。

- remaining_uncertainty_cn：消融仅证明组件对当前数据集有用，不能完全证明组件是理论机制的唯一实现；EBM-NLP未启用全局上下文。

- link_to_next_phase_cn：组件贡献明确后，转向真实SR流程中FastSR能否带来端到端价值。

##### evidence_pointers

1. Tables 13-15

2. Section 'Evaluation Results: Ablation Analysis'

3. Figure 3

4. Appendix H

#### 6. SR自动化下游案例评价

- order：6

- name_cn：SR自动化下游案例评价

- question_cn：FastSR在真实SR项目中能否生成更接近专家结果的证据报告、被专家接受，并带来时间与经济节省？

- inputs_and_setting_cn：WD数据集对应的真实SR项目（GLS公司，1500小时，550篇文章）；SR专家参与验证和访谈；时间/成本估算基于110篇测试文章并外推到550篇。

- designed_or_compared_object_cn：FastSR生成的SR报告与ProtoNet报告、专家报告比较；FastSR增强流程与Manual SR、ProtoNet、CNN增强流程比较。

- baseline_control_or_counterfactual_cn：ProtoNet作为最强FSL基准、CNN作为最强传统DL基准、人工双筛查作为现状对照。

##### objective_metrics

1. 报告分布图与专家报告的一致性

2. 检索到的关键研究数量

3. 验证和修正假预测所需时间

4. 总项目时间节省百分比

5. 成本节省美元

6. 定性访谈反馈

- analysis_method_cn：四类对比图（WD表现、干预分布、中国样本量、Trientine研究类型）；专家半结构访谈；分步时间成本模型（标注、训练、验证、修正假预测）。

- main_result_cn：FastSR报告比ProtoNet更接近专家报告且不遗漏关键研究；访谈显示专家认为FastSR重要、可访问、适合时间敏感型SR，但建议增加界面和修订SR协议；时间成本估算显示FastSR相比人工SR节省约65%时间和约73,500美元/项目，相比基准模型节省20-25%。

- argumentative_role_cn：把离线指标优势转化为真实工作流程中的可用性证据，满足计算设计科学对“应用环境价值”的要求。

- remaining_uncertainty_cn：时间/成本是基于假设的估算而非随机对照实验；访谈样本有限；未在完整SR项目中长期部署。

- link_to_next_phase_cn：基于下游案例和访谈，讨论如何把FastSR制度化到SR协议中，由此提出FastSR增强流程。

##### evidence_pointers

1. Figure 4

2. Table 16

3. Appendix F1 qualitative feedback

4. Section 'SR Automation'

#### 7. FastSR增强SR协议与设计知识提炼

- order：7

- name_cn：FastSR增强SR协议与设计知识提炼

- question_cn：FastSR应如何嵌入SR流程？从该设计中可提炼哪些可复用的计算设计知识？

- inputs_and_setting_cn：前述六阶段的全部证据，加上PRISMA五阶段框架和专家访谈建议。

- designed_or_compared_object_cn：新的FastSR半自动SR协议：计划阶段标注少量样本→FastSR自动筛选和抽取→专家验证和修正。

- baseline_control_or_counterfactual_cn：与现行人工SR五阶段流程和已有ML增强思路比较。

##### objective_metrics

（空）

- analysis_method_cn：讨论形式的综合与概念整合；把DRs映射到设计知识，并总结边界条件。

- main_result_cn：提出FastSR增强SR协议，使筛选和抽取半自动化，专家认知负荷从机械抽取转向证据综合；讨论组合性理论、sensemaking和多侧面评价作为设计科学方法论贡献。

- argumentative_role_cn：把具体制品结果上升为可迁移的设计原则、边界条件和未来研究议程。

- remaining_uncertainty_cn：新协议未经完整现场随机检验；跨领域迁移、自动发现新PICO类、层级化PICO和LLM用于证据综合等仍未解决。

- link_to_next_phase_cn：无需下一阶段，直接收束到结论。

##### evidence_pointers

1. Figure 5

2. Section 'Discussion and Conclusion'

## 各部分修辞架构

### abstract_moves

1. CONTEXT

2. PRACTICAL_STAKES

3. LIMITATION

4. GAP

5. RQ_OR_OBJECTIVE

6. STUDY_OVERVIEW

7. CONTRIBUTION

### introduction_moves

1. CONTEXT

2. PRACTICAL_STAKES

3. PHENOMENON

4. PRIOR_KNOWLEDGE

5. LIMITATION

6. GAP

7. THEORY_INTRO

8. STUDY_OVERVIEW

9. CONTRIBUTION

### theory_and_knowledge_moves

1. THEORY_INTRO

2. THEORY_PROPOSITION

3. MECHANISM

4. REQUIREMENT

5. LIMITATION

6. PRIOR_KNOWLEDGE

### artifact_design_moves

1. REQUIREMENT

2. DESIGN_FEATURE

3. METHOD_JUSTIFICATION

4. MECHANISM

### evaluation_moves

1. METHOD_JUSTIFICATION

2. BENCHMARK_OR_CONTRAST

3. STUDY_OVERVIEW

4. RESULT

5. ROBUSTNESS_OR_BOUNDARY_TEST

6. TRANSITION

### discussion_and_contribution_moves

1. CONTRIBUTION

2. THEORY_RETURN

3. BOUNDARY_CONDITION

4. LIMITATION_AND_FUTURE

5. CONTRIBUTION

## 理论/知识到设计的翻译

### 知识/理论基础

1. 组合性理论（compositionality theory）

2. sensemaking文献

3. SR领域过程/标注逻辑

4. 少样本学习文献

5. Biomedical NLP/LLM与预训练模型

- 理论—设计耦合：direct

- 耦合判定理由：文章明确提出用组合性理论和sensemaking指导设计：从理论视角把高专家性低标签环境的任务复杂度抽象为四项设计要求，每一项要求都对应FastSR中的具体组件，并通过整体benchmarking和逐组件ablation被直接检验；因此理论与设计、评价形成完整链条。

- 理论到设计翻译链：组合性理论（复杂含义由简单部件及其关系构成）→人可少样本学习→用FSL缓解标签稀缺→DR1需要最小标注；sensemaking（局部/全局背景、语义对应、迭代综合）→DR2-DR4→FastSR增加多重原型、注意力片段表示和联合学习→三数据集基准和消融检验→下游SR自动化评价→设计原则/协议输出。

### mapping_table

#### 1. 1

- theory_or_knowledge_claim_cn：组合性理论：人类能从少数例子中通过组合和对比简单部件来高效学习复杂概念。

- mechanism_cn：在少样本设置中，用支持集构造类原型，把预测转化为查询与原型间的距离比较，可在每类极少标注下工作。

- design_requirement_cn：DR1：ML自动化方案应只需最少标注投入。

- artifact_choice_cn：采用基于ProtoNet的二路k-shot FSL，并以one-vs-rest处理多标签；用BioBERT嵌入增强医学语义。

- evaluated_contrast_cn：与fine-tuned BioBERT、GPT-4 few-shot、VAT SSL、MAML、Matching Net等基准对比。

- objective_result_cn：FastSR在WD/COVID/EBM-NLP句子分类F1@3和PRC均最高；减少1/3训练样本仅轻微下降。

##### evidence_pointers

1. Table 7-9

2. Table 13 M9

3. Figure 3

#### 2. 2

- theory_or_knowledge_claim_cn：sensemaking要求同时考虑句子局部语义和所在章节的全局背景。

- mechanism_cn：局部上下文帮助理解词语意义（如prevalence对应研究设计），全局上下文帮助判断句子是否属于PICO所在章节。

- design_requirement_cn：DR2：模型应同时考虑句子的local和global context。

- artifact_choice_cn：BioBERT+CNN生成局部语义原型；用PubMed预训练的分层嵌入做章节分类，再用pointer network选择最匹配的全局上下文原型。

- evaluated_contrast_cn：消融移除全局上下文（M1）、用图摘要替代全局上下文（M8）、层级MTL替代（M7）。

- objective_result_cn：移除全局上下文使WD句子F1@3降低3.64%、片段F1降低3.41%；替代方案也下降。

##### evidence_pointers

1. Table 13 M1/M8/M7

2. Table 14 M1/M8

#### 3. 3

- theory_or_knowledge_claim_cn：人类专家对PICO片段进行语义对应而非单纯词面匹配。

- mechanism_cn：通过抽象和消歧，专家能够接受“patients under 14”与“pediatric patients”表达同一核心概念；模型需要用注意力聚焦核心片段词。

- design_requirement_cn：DR3：语义对应优先于词面匹配。

- artifact_choice_cn：全局注意力机制生成attention-based fragment表示；引入BERTScore作为语义评价指标；在query侧用word-to-word attention构造fragment-attended query。

- evaluated_contrast_cn：与ProtoNER、Nearest Neighbor、无注意力消融（M2）比较；使用F1_word与F1_BERT两种指标。

- objective_result_cn：FastSR在WD片段F1_word@3约60.8%、F1_BERT@3约67.2%；移除注意力使F1_word下降5.18%；F1_BERT普遍高于F1_word，说明语义匹配确实发生。

##### evidence_pointers

1. Table 10

2. Table 13 M2

3. Table 14 M2

#### 4. 4

- theory_or_knowledge_claim_cn：组合性理论强调部件间关系；sensemaking涉及迭代的、相互依赖的句子和片段识别。

- mechanism_cn：句子分类和片段标注共享知识可减少误差传播；一个词被标为PICO片段，则该句更应被分类为PICO相关。

- design_requirement_cn：DR4：应在FSL框架内联合识别句子和片段并共享语义、上下文、医学知识。

- artifact_choice_cn：共享片段原型，通过fragment-attended query把T2知识用于T1；在总损失中加入LR一致性正则化。

- evaluated_contrast_cn：与分离的两阶段流程、层级MTL架构（M7）、移除联合学习（M3）比较。

- objective_result_cn：移除联合学习使WD句子F1@3下降4.74%、片段F1_word下降3.76%；层级MTL也低于模块化联合设计。

##### evidence_pointers

1. Table 13 M3/M7

2. Table 14 M3/M7

## 评价逻辑

### evaluation_modes

1. 三数据集句子分类benchmarking

2. 三数据集序列标注benchmarking

3. 组件消融与替代设计检验

4. 样本量敏感性分析

5. 下游SR报告生成对比

6. 专家定性访谈

7. 时间/成本经济性建模

8. 误差分析

- why_these_evaluations_cn：计算设计科学制品必须同时回答“是否有效、哪个组件有效、是否可泛化、对真实流程是否有价值”。仅benchmark不足以证明设计需求被满足，因此加入消融、替代架构、样本敏感性；仅离线指标不足以证明高专家性环境下的适用性，因此加入真实SR报告、访谈和经济估算。

- benchmark_and_contrast_chain_cn：句子分类阶段先用四类基准模型确立FastSR整体优势，再在COVID上检验可迁移性，在EBM-NLP上检验公共数据泛化；序列标注阶段把最好的句子分类器与标签器组合，检验错误传播后的端到端片段抽取；消融阶段逐一删除全局上下文、注意力和联合学习，并测试替代组件；最后在真实SR流程中用报告图、访谈和成本模型把离线优势转成下游价值。

### claim_evidence_ledger

#### 1. FastSR在句子分类上显著优于现有ML/LLM/FSL方案。

- claim_cn：FastSR在句子分类上显著优于现有ML/LLM/FSL方案。

- evidence_cn：WD、COVID、EBM-NLP三个数据集的F1@3和PRC表格及显著性检验。

- status_cn：充分支持

#### 2. FastSR在PICO片段抽取上显著优于现有序列标注器。

- claim_cn：FastSR在PICO片段抽取上显著优于现有序列标注器。

- evidence_cn：三个数据集上的F1_word、F1_BERT和PRC结果。

- status_cn：充分支持

#### 3. 每个设计组件（全局上下文、注意力片段、联合学习）独立贡献性能。

- claim_cn：每个设计组件（全局上下文、注意力片段、联合学习）独立贡献性能。

- evidence_cn：WD和EBM-NLP上的消融表M1-M9及替代设计比较。

- status_cn：充分支持，但限于所测数据集和实现方式

#### 4. FastSR具有样本效率，在更少标注下仍稳健。

- claim_cn：FastSR具有样本效率，在更少标注下仍稳健。

- evidence_cn：WD减少1/3样本仅3-5%下降；EBM-NLP样本量增大时差距缩小。

- status_cn：支持，但边界条件是样本量不太大

#### 5. FastSR生成的SR报告更接近专家人工报告。

- claim_cn：FastSR生成的SR报告更接近专家人工报告。

- evidence_cn：四类对比图显示FastSR检索到关键研究，基准方法遗漏重要文献。

- status_cn：支持，但仅基于WD项目案例

#### 6. FastSR能节省SR时间和成本。

- claim_cn：FastSR能节省SR时间和成本。

- evidence_cn：分步时间成本模型估算65%时间节省和73,500美元/项目节省。

- status_cn：部分支持；该估算依赖专家人工筛查、单筛查等假设

#### 7. 专家认为FastSR具有实用性。

- claim_cn：专家认为FastSR具有实用性。

- evidence_cn：半结构访谈引用（重要性、可访问性、适合性）。

- status_cn：支持，但样本小且非随机

- internal_validity_strategy_cn：使用多数据集、专家标注一致性kappa（WD 0.85，COVID 0.87）、固定Top-N评估协议、显著性检验、消融和替代架构控制，使性能归因更清晰。

- external_validity_strategy_cn：覆盖私有WD全文学术文章、开放COVID全文学术文章、公开EBM-NLP摘要；跨领域重训和复用；同时使用词面和语义指标。

- what_is_not_actually_tested_cn：未在非医学领域检验；新PICO类自动发现未实现；PICO层级结构未纳入原型；LLM在证据综合阶段的价值未测试；FastSR增强SR协议未在完整随机现场试验中验证；时间/成本节省仍是模型估计而非受控实测。

## 贡献闭环

- technical_claim_cn：FastSR在三个医疗SR数据集上的句子分类和PICO片段抽取指标显著优于传统DL、SSL、LLM和FSL基准。

- artifact_claim_cn：全局上下文原型、注意力片段原型和联合学习模块是FastSR性能提升的来源，消融实验证明了每个组件的独立贡献。

- mechanism_claim_cn：FastSR通过多原型结构模拟专家sensemaking：局部语义和全局章节背景决定句子相关性，语义注意力决定片段对应，共享片段原型和一致性正则化减少T1/T2误差传播。

- boundary_claim_cn：FastSR在低标签高专家性医疗SR语境中有效；样本量增加时优势缩小；GPT类LLM在开放域可能因数据污染而虚高，在封闭域表现差；在抽象数据集上全局上下文模块可不启用。

- reusable_design_knowledge_cn：从任务复杂度到设计需求DR1-DR4的映射表；FastSR的多原型少样本设计模板；FastSR增强SR半自动协议；多侧面评价策略（benchmark + ablation + 下游工作流 + 访谈 + 成本模型）。

- theoretical_contribution_cn：将组合性理论和sensemaking引入FSL制品设计，展示如何用理论把高专家性低标签环境的任务复杂度转译为可计算的设计需求；延伸关于AI人机协同和设计科学的IS讨论。

- how_discussion_closes_intro_gap_cn：引言指出高专家性低标签是IS计算设计未充分覆盖的问题；讨论部分明确回应这一缺口，强调FastSR证明了理论引导领域适配和定制评价策略的价值，并提出新的SR协议；同时用边界条件避免把结果夸大为通用万能方案。

- overclaim_or_unsupported_leaps_cn：最明显的跳跃是把时间成本模型当作事实性的65%节省；该估算依赖单筛查、专家每小时100美元等假定。另一个跳跃是把“专家访谈认为有用”等同于“实际部署成功”。此外，GPT-4的低绩效部分由数据污染和成本解释，但不足以断言所有ALM都在此类任务上结构性劣势。

## 句级写作动作图谱

### 1. P1 S1-S2

- order：1

- section：Introduction

- locator：P1 S1-S2

- move_code：CONTEXT

- paraphrase_cn：IS领域近年越来越重视用计算设计制品自动化/增强人工密集型流程，但以往作品多面向标注充足、任务定义清晰的场景。

- rhetorical_function_cn：开篇确立计算设计研究的一般兴趣，并立即划出本文要进入的空白地带。

- depends_on_cn：无，是全文起点。

- sets_up_cn：为后面突出“高专家性、低标签”特殊性做铺垫。

- evidence_pointer：Introduction P1

### 2. P1 S3

- order：2

- section：Introduction

- locator：P1 S3

- move_code：GAP

- paraphrase_cn：本文研究的是SR这一对证据医学至关重要、标注数据稀缺且常规ML难以表征高专家性任务的计算制品设计问题。

- rhetorical_function_cn：把一般IS兴趣收缩到具体代表性环境。

- depends_on_cn：上一句指出IS主流多聚焦标签充足场景。

- sets_up_cn：提出SR与EBM作为核心申请场景。

- evidence_pointer：Introduction P1

### 3. P2 S1-S2

- order：3

- section：Introduction

- locator：P2 S1-S2

- move_code：PRACTICAL_STAKES

- paraphrase_cn：SR是可重复、减少偏倚的证据抽取与综合过程，是EBM的重要支柱，对临床决策和新冠疫情等公共健康问题有重大影响。

- rhetorical_function_cn：说明研究对象为何值得关注，提升现实重要性。

- depends_on_cn：承接上一段引入SR。

- sets_up_cn：为后续“SR慢、成本高”的痛点提供价值背景。

- evidence_pointer：Introduction P2

### 4. P2 S4

- order：4

- section：Introduction

- locator：P2 S4

- move_code：PRACTICAL_STAKES

- paraphrase_cn：有估计称SR支撑的EBM可预防至多三分一死亡并降低至少30%医疗开支。

- rhetorical_function_cn：用数量级后果把SR的重要性推至极点。

- depends_on_cn：前面定义SR和EBM。

- sets_up_cn：为“必须自动化”提供理由。

- evidence_pointer：Introduction P2

### 5. P3 S1-S3

- order：5

- section：Introduction

- locator：P3 S1-S3

- move_code：PHENOMENON

- paraphrase_cn：SR通常由多位专家手工执行，需要从文章中抽取高度细粒度、疾病特异、不断变化的PICO要素，例如单个疾病可能有上百个不同结局元素。

- rhetorical_function_cn：描述经验现象，说明数据抽取为何困难。

- depends_on_cn：上一段说明SR的重要性。

- sets_up_cn：为任务复杂度分析提供具体领域事实。

- evidence_pointer：Introduction P3

### 6. P3 S4-S5

- order：6

- section：Introduction

- locator：P3 S4-S5

- move_code：PRACTICAL_STAKES

- paraphrase_cn：PICO要素疾病特异且快速变化，无法标准化数据库；人工SR平均耗时67.3周，许多综述发表时已过时。

- rhetorical_function_cn：量化当前SR低效性和过时风险。

- depends_on_cn：前一句说明PICO多样性。

- sets_up_cn：建立“需要ML代替/辅助”的迫切性。

- evidence_pointer：Introduction P3

### 7. P4 S1

- order：7

- section：Introduction

- locator：P4 S1

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：已有ML/NLP方案通常把SR数据抽取拆为句子分类和序列标注两个监督任务。

- rhetorical_function_cn：总结已有技术路径，让读者知道现状是什么。

- depends_on_cn：前面已说明SR步骤。

- sets_up_cn：为后续指出这些方案的局限作铺垫。

- evidence_pointer：Introduction P4

### 8. P4 S2-S3

- order：8

- section：Introduction

- locator：P4 S2-S3

- move_code：LIMITATION

- paraphrase_cn：由于PICO要素数量多、每类标注样本需求大，ML SR的标注成本几乎与人工SR一样高；现有方案只能限制抽取元素数量、限定RCT或抽取摘要，而且因未充分纳入人类专家使用的语义、上下文和医学知识而表现不佳。

- rhetorical_function_cn：指出已有制品在标注效率、覆盖范围和性能上的三重短板。

- depends_on_cn：基于上一句对任务步骤的说明。

- sets_up_cn：引出FastSR要解决的两大障碍：标注量大、专家知识缺失。

- evidence_pointer：Introduction P4

### 9. P5 S1-S2

- order：9

- section：Introduction

- locator：P5 S1-S2

- move_code：RQ_OR_OBJECTIVE

- paraphrase_cn：为了应对这些问题，本文提出FastSR，一个基于组合性理论指导的通用FSL框架，专门处理SR数据抽取的标注稀缺和专家意义建构挑战。

- rhetorical_function_cn：首次给出本文研究目标和制品名称。

- depends_on_cn：前段识别出的两大问题。

- sets_up_cn：告诉读者答案即将出现，并预告三个设计扩展。

- evidence_pointer：Introduction P5

### 10. P5 S3-S4

- order：10

- section：Introduction

- locator：P5 S3-S4

- move_code：THEORY_INTRO

- paraphrase_cn：FastSR采用FSL，并依据组合性理论扩展FSL：人类能通过简单部件及其关系高效从有限样例学习；对应地加入句子、片段多种表示、注意力和共享表示的联合学习。

- rhetorical_function_cn：引入理论并桥接到具体设计组件。

- depends_on_cn：上一句提出FastSR。

- sets_up_cn：为第二节的任务复杂度/设计需求正式讨论做预告。

- evidence_pointer：Introduction P5

### 11. P6

- order：11

- section：Introduction

- locator：P6

- move_code：STUDY_OVERVIEW

- paraphrase_cn：FastSR在WD、COVID和EBM-NLP三个测试床上实例化与评估，其中WD来自1500小时真实SR项目，COVID来自开放挑战，EBM-NLP是公开专家标注RCT摘要。

- rhetorical_function_cn：预告数据集范围和证据来源。

- depends_on_cn：前面说明了制品。

- sets_up_cn：为评价部分建立预期。

- evidence_pointer：Introduction P6

### 12. P7

- order：12

- section：Introduction

- locator：P7

- move_code：STUDY_OVERVIEW

- paraphrase_cn：本文还与SR公司合作把FastSR和替代模型嵌入真实人工SR工作流，比较报告质量、时间节省，并通过专家访谈验证可用性。

- rhetorical_function_cn：预告论文不只有离线benchmark，还有下游应用评价。

- depends_on_cn：上一段已谈离线数据集。

- sets_up_cn：为SR Automation节埋下伏笔。

- evidence_pointer：Introduction P7

### 13. P8

- order：13

- section：Introduction

- locator：P8

- move_code：CONTRIBUTION

- paraphrase_cn：研究贡献包括：面向AI场景的设计研究路径、理论引导的设计抽象、四项设计需求、FastSR制品及三数据集证据、节约65%时间和73,500美元/项目的增强SR流程。

- rhetorical_function_cn：集中宣布贡献，让审稿人和读者快速知道论文价值。

- depends_on_cn：前面全部问题与方案介绍。

- sets_up_cn：为讨论部分回收贡献做准备。

- evidence_pointer：Introduction P8

### 14. P1 and Table 1

- order：14

- section：SR Automation: Task Complexity

- locator：P1 and Table 1

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：通过对SR关键步骤的文献综述发现，数据抽取是最劳动密集且现有IT制品支持最少的一步。

- rhetorical_function_cn：从整体流程中选中研究焦点。

- depends_on_cn：引言已经提出SR难题。

- sets_up_cn：说明本文只自动化数据抽取步骤。

- evidence_pointer：Section 'SR Automation', Table 1

### 15. P2

- order：15

- section：SR Automation: Task Complexity

- locator：P2

- move_code：MECHANISM

- paraphrase_cn：结合SR自动化文献和专家咨询，数据抽取复杂度来自四方面：PICO要素量巨大、需要局部与全局上下文、片段语义对应、迭代过程中需要多元知识联合运用。

- rhetorical_function_cn：从领域经验中提炼出抽象的任务复杂度。

- depends_on_cn：上一句选取数据抽取为焦点。

- sets_up_cn：四项复杂度分别导向DR1-DR4。

- evidence_pointer：Section 'SR Automation', P2

### 16. P3

- order：16

- section：SR Automation: Task Complexity

- locator：P3

- move_code：THEORY_INTRO

- paraphrase_cn：引入组合性理论：复杂表达的意义由部件和组成规则决定，丰富概念可从简单原语组合而来，因此可从少量例子学习；sensemaking则是为回答任务问题而搜索表示并把数据编码到该表示的过程。

- rhetorical_function_cn：把领域复杂度与认知理论连接起来，为设计提供理论语言。

- depends_on_cn：前句列出四个任务复杂度。

- sets_up_cn：为“理论指导设计”提供依据。

- evidence_pointer：Section 'SR Automation', P3

### 17. P1

- order：17

- section：Task Complexity 1

- locator：P1

- move_code：REQUIREMENT

- paraphrase_cn：因为标准SR可能有数百个PICO类、标注高度专业且不可复用，所以提出DR1：模型应尽量少标注。

- rhetorical_function_cn：从复杂度1明确产生第一条设计要求。

- depends_on_cn：前一节列出复杂度1。

- sets_up_cn：为FSL组件选择提供依据。

- evidence_pointer：Section 'Task Complexity 1'

### 18. Related literature paragraphs

- order：18

- section：Task Complexity 1

- locator：Related literature paragraphs

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：现有低标注方案包括LLM微调/few-shot、半监督学习和FSL；但它们分别受限于标注需求、分布不对齐和任务多样性。

- rhetorical_function_cn：综述候选技术并指出其各自适用边界。

- depends_on_cn：DR1已提出。

- sets_up_cn：为选择FSL特别是ProtoNet做铺垫。

- evidence_pointer：Section 'Task Complexity 1', 'Related literature'

### 19. FSL paragraphs

- order：19

- section：Task Complexity 1

- locator：FSL paragraphs

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：在FSL内部，优化式方法依赖任务共享初始化，但SR各PICO类标签词重叠很少；度量式方法更合适；ProtoNet相比matching net更高效、原型能更好表示多维知识，因此选择ProtoNet。

- rhetorical_function_cn：解释为什么最终选择ProtoNet而非其他FSL。

- depends_on_cn：前面讨论FSL类别。

- sets_up_cn：为FastSR整体结构选择提供技术理由。

- evidence_pointer：Section 'Task Complexity 1', 'Related literature', Table 4

### 20. P1

- order：20

- section：Task Complexity 2

- locator：P1

- move_code：REQUIREMENT

- paraphrase_cn：因为SR专家既看句子的局部意思，也看句子在文章中的位置，因此提出DR2：模型应同时考虑局部和全局上下文。

- rhetorical_function_cn：从复杂度2产生第二条设计要求。

- depends_on_cn：前一节列出复杂度2。

- sets_up_cn：为局部语义和全局上下文两个模块提供规格。

- evidence_pointer：Section 'Task Complexity 2'

### 21. Related literature paragraphs

- order：21

- section：Task Complexity 2

- locator：Related literature paragraphs

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：BioBERT能捕捉医学词义，CNN适合抓取局部关键短语；全局上下文因标注少无法直接训练，因此用PubMed预训练分层嵌入做迁移，并用pointer network处理同一PICO类出现在多个章节的情况。

- rhetorical_function_cn：说明局部/全局模块各自的技术选型理由。

- depends_on_cn：DR2提出。

- sets_up_cn：对应FastSR中的表示与原型公式。

- evidence_pointer：Section 'Task Complexity 2'

### 22. P1

- order：22

- section：Task Complexity 3

- locator：P1

- move_code：REQUIREMENT

- paraphrase_cn：因为专家看重片段与PICO核心概念的语义对应而非词面一致，提出DR3：模型应优先语义对应。

- rhetorical_function_cn：从复杂度3产生第三条设计要求。

- depends_on_cn：前一节列出复杂度3。

- sets_up_cn：为注意力片段表示和BERTScore评价做准备。

- evidence_pointer：Section 'Task Complexity 3'

### 23. Related literature paragraphs

- order：23

- section：Task Complexity 3

- locator：Related literature paragraphs

- move_code：LIMITATION

- paraphrase_cn：传统IOB序列标注依赖词面匹配，无法处理“pediatric patients”与“patients under 14”的语义等价；为此需要全局注意力把词与核心PICO概念对齐，并用BERTScore补充评价。

- rhetorical_function_cn：指出已有序列标注器的不足，并引出FastSR的语义组件。

- depends_on_cn：DR3形成。

- sets_up_cn：为fragment representation模块和BERTScore提供动机。

- evidence_pointer：Section 'Task Complexity 3'

### 24. P1

- order：24

- section：Task Complexity 4

- locator：P1

- move_code：REQUIREMENT

- paraphrase_cn：因为专家在迭代标注中同时使用语义、上下文和医学知识来确定句子与片段，提出DR4：模型应在FSL中联合识别句子和片段、共享知识。

- rhetorical_function_cn：从复杂度4产生第四条设计要求。

- depends_on_cn：前面三个DR都关于单一知识，这里强调联合。

- sets_up_cn：为共享片段原型和跨任务正则化提供依据。

- evidence_pointer：Section 'Task Complexity 4'

### 25. Related literature paragraphs

- order：25

- section：Task Complexity 4

- locator：Related literature paragraphs

- move_code：LIMITATION

- paraphrase_cn：已有方案把T1和T2分开处理，T1错误会传播到T2；MTL虽有帮助，但需小心调节任务相关性和架构；模块化架构优于顺序层级架构。

- rhetorical_function_cn：指出分离式流程的误差传播并说明MTL设计取向。

- depends_on_cn：DR4提出。

- sets_up_cn：为FastSR的联合学习损失设计做铺垫。

- evidence_pointer：Section 'Task Complexity 4'

### 26. P1-P2

- order：26

- section：FastSR: Problem Definition

- locator：P1-P2

- move_code：DESIGN_FEATURE

- paraphrase_cn：由于一个句子可含多个PICO类，FastSR用one-vs-rest把多标签分类转化为多个二路k-shot FSL任务。

- rhetorical_function_cn：说明制品如何从问题定义上应对多标签现实。

- depends_on_cn：前面DR1-FSL选择。

- sets_up_cn：为后文Query与Support Set的构造提供形式化基础。

- evidence_pointer：Section 'Problem Definition and Overall Architecture'

### 27. Figure 1e paragraphs

- order：27

- section：FastSR: Overall Architecture

- locator：Figure 1e paragraphs

- move_code：DESIGN_FEATURE

- paraphrase_cn：FastSR整体采用ProtoNet结构，但不再只有一个类原型，而是包含局部语义、全局上下文和片段三类原型，并让两类任务共享片段原型。

- rhetorical_function_cn：一句话概括FastSR架构的核心创新。

- depends_on_cn：四个DR共同作用。

- sets_up_cn：随后各小节分别展开三种表示和联合学习。

- evidence_pointer：Figure 1e附近

### 28. P1

- order：28

- section：Sentence Contextualized Semantic Representations

- locator：P1

- move_code：DESIGN_FEATURE

- paraphrase_cn：局部语义表示用BioBERT做上下文词嵌入，再用CNN生成句子表示，支持集内句子表示取平均作为语义原型。

- rhetorical_function_cn：实现DR2的局部上下文组件。

- depends_on_cn：第二节局部上下文技术选择。

- sets_up_cn：供Equation (1)和后续距离计算使用。

- evidence_pointer：Equation (1)

### 29. P1-P2

- order：29

- section：Sentence Global Context Representations

- locator：P1-P2

- move_code：DESIGN_FEATURE

- paraphrase_cn：全局上下文用PubMed训练的hierarchical embedding章节分类器产生13类章节概率；由于同一PICO类可出现在多个章节，用pointer network选择与query最匹配的支持句上下文作为上下文原型。

- rhetorical_function_cn：实现DR2的全局上下文组件。

- depends_on_cn：第二节全局上下文技术选择。

- sets_up_cn：证明全局上下文不使用简单平均而用pointer network的原因。

- evidence_pointer：Equations (2)-(3)

### 30. P1-P2

- order：30

- section：PICO Text Fragment Representations

- locator：P1-P2

- move_code：DESIGN_FEATURE

- paraphrase_cn：片段表示用全局注意力对支持集中的片段词加权，使模型聚焦于PICO核心概念；支持集内片段表示平均后形成片段原型。

- rhetorical_function_cn：实现DR3的语义对应组件。

- depends_on_cn：Task Complexity 3对语义对应的讨论。

- sets_up_cn：这个片段原型将在T1和T2间共享。

- evidence_pointer：Equations (4)-(7)

### 31. P1-P2

- order：31

- section：Fragment-Attended Query Representations

- locator：P1-P2

- move_code：DESIGN_FEATURE

- paraphrase_cn：为了把片段知识用于句子分类，FastSR用word-to-word attention计算query词与支持集片段词的对齐，生成fragment-attended query表示，并同时输出词是否属于片段的发射概率β_t。

- rhetorical_function_cn：实现DR4中T2到T1的知识共享。

- depends_on_cn：片段原型已建立。

- sets_up_cn：为联合损失中的LS、LT、LR提供输入。

- evidence_pointer：Equations (8)-(11)

### 32. P1-P3

- order：32

- section：Joint Learning via Representation Integration

- locator：P1-P3

- move_code：DESIGN_FEATURE

- paraphrase_cn：句子分类用语义、上下文和片段注意力三种原型距离的加权和；片段标注用词与片段原型的距离并乘以β_t；总损失包含分类损失、标注损失和跨任务一致性正则化。

- rhetorical_function_cn：汇总FastSR的推理与学习目标，完成DR4的联合学习设计。

- depends_on_cn：前面三种表示和query表示。

- sets_up_cn：为后续训练与消融提供可操作公式。

- evidence_pointer：Equations (12)-(19)

### 33. P1

- order：33

- section：Evaluation Strategy

- locator：P1

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：计算设计科学需要多侧面评价：基准比较、消融分析和下游价值缺一不可。

- rhetorical_function_cn：为整章评价策略提供方法论辩护。

- depends_on_cn：设计科学文献和本文Design Science定位。

- sets_up_cn：后续三大部分评价（分类、标注、SR自动化）都有合法性。

- evidence_pointer：Section 'Evaluation Strategy and Datasets'

### 34. P2-P3

- order：34

- section：Evaluation Tasks

- locator：P2-P3

- move_code：BENCHMARK_OR_CONTRAST

- paraphrase_cn：句子分类采用P@N/R@N/F1@N和PRC；片段标注额外采用词面F1和BERTScore语义F1；所有这些指标都基于每个文章的Top-3预测句子。

- rhetorical_function_cn：规定评价指标与Top-N协议，使结果可比。

- depends_on_cn：SR自动化文献已有Top-N指标。

- sets_up_cn：为表格中的一致数字格式做准备。

- evidence_pointer：Section 'Evaluation Tasks', Appendix D

### 35. WD dataset paragraph

- order：35

- section：Datasets

- locator：WD dataset paragraph

- move_code：DESIGN_FEATURE

- paraphrase_cn：WD数据集来自药企委托的1500小时真实SR项目，共137个PICO元素，本研究仅使用其中六类并限制每类标注不超过100句，以模拟低标注约束。

- rhetorical_function_cn：说明主测试床的私有性和高专家性。

- depends_on_cn：评价策略已设定。

- sets_up_cn：为后续报告生成和时间成本分析提供来源。

- evidence_pointer：Section 'Datasets and Model Implementation', Table 6

### 36. COVID dataset paragraph

- order：36

- section：Datasets

- locator：COVID dataset paragraph

- move_code：DESIGN_FEATURE

- paraphrase_cn：COVID数据用于检验可迁移性：一方面把WD训练好的模型直接复用到population/sample size/country三类，另一方面新训练risk factor类来测试新领域新类。

- rhetorical_function_cn：引入跨领域迁移设计。

- depends_on_cn：WD模型已训练。

- sets_up_cn：为COVID reuse与新类结果做铺垫。

- evidence_pointer：Section 'Datasets and Model Implementation', Table 6

### 37. EBM-NLP paragraph

- order：37

- section：Datasets

- locator：EBM-NLP paragraph

- move_code：DESIGN_FEATURE

- paraphrase_cn：EBM-NLP公开数据集提供200篇专家标注摘要和17个PICO元素三类，但只有摘要，所以FastSR的全局上下文模块被禁用。

- rhetorical_function_cn：给出公开基准数据及相应模型配置变化。

- depends_on_cn：评价策略和WD/COVID设置。

- sets_up_cn：为EBM-NLP上的泛化性解释提供前提。

- evidence_pointer：Section 'Datasets and Model Implementation', Table 6

### 38. WD result paragraphs after Table 7

- order：38

- section：Evaluation Results: Sentence Classification

- locator：WD result paragraphs after Table 7

- move_code：RESULT

- paraphrase_cn：在WD上CNN是传统模型中最强；VAT提升有限；fine-tuned BioBERT受限于样本量；GPT-4 few-shot明显落后；FSL中ProtoNet最强；FastSR F1@3约73%，比ProtoNet高约7%，比GPT-4高约34%。

- rhetorical_function_cn：报告主数据集句子分类结果并解释各基准为何受限。

- depends_on_cn：表7结果。

- sets_up_cn：为COVID和EBM-NLP结果提供对照。

- evidence_pointer：Table 7

### 39. COVID result paragraphs after Table 8

- order：39

- section：Evaluation Results: Sentence Classification

- locator：COVID result paragraphs after Table 8

- move_code：RESULT

- paraphrase_cn：在COVID上FSL模型的reusability优于CNN和fine-tuned BioBERT；FastSR在复用和新训练风险因子类上都最好。

- rhetorical_function_cn：证明WD训练出的模型可迁移到COVID。

- depends_on_cn：WD结果已建立。

- sets_up_cn：为序列标注中的reuse测试做预告。

- evidence_pointer：Table 8

### 40. EBM-NLP result paragraphs after Table 9

- order：40

- section：Evaluation Results: Sentence Classification

- locator：EBM-NLP result paragraphs after Table 9

- move_code：RESULT

- paraphrase_cn：由于只有摘要、片段粒度更粗，所有模型在EBM-NLP上表现更好；FastSR仍最佳，但与GPT-4的差距缩小约20%，很可能因为开放域数据污染。

- rhetorical_function_cn：报告公开数据集结果并解释LLM差距缩小的原因。

- depends_on_cn：WD/COVID结果。

- sets_up_cn：为后续GPT-4参与序列标注提供理由。

- evidence_pointer：Table 9

### 41. WD result paragraph after Table 10

- order：41

- section：Evaluation Results: Sequence Tagging

- locator：WD result paragraph after Table 10

- move_code：RESULT

- paraphrase_cn：WD片段抽取中FSL标签器优于传统标签器；FastSR的F1_word@3约61%，比LSTM+CRF高约15%，比ProtoNER高约4%；BERTScore显著高于词面F1，说明语义对应确实存在。

- rhetorical_function_cn：报告主数据集片段抽取结果，证明T2有效。

- depends_on_cn：句子分类器已选出Top-3句子。

- sets_up_cn：为COVID/EBM-NLP片段结果和消融做铺垫。

- evidence_pointer：Table 10

### 42. COVID result paragraph after Table 11

- order：42

- section：Evaluation Results: Sequence Tagging

- locator：COVID result paragraph after Table 11

- move_code：RESULT

- paraphrase_cn：在COVID上复用WD模型的FastSR仍比最强基准高出8-28%；新训练risk factor类同样大幅领先。

- rhetorical_function_cn：证明片段抽取模块也可跨域迁移。

- depends_on_cn：WD片段模型和COVID句子结果。

- sets_up_cn：进一步强化跨领域泛化证据。

- evidence_pointer：Table 11

### 43. EBM-NLP result paragraph after Table 12

- order：43

- section：Evaluation Results: Sequence Tagging

- locator：EBM-NLP result paragraph after Table 12

- move_code：RESULT

- paraphrase_cn：在EBM-NLP上FastSR在全部指标上最高；GPT-4在片段标注上比句子分类退化更严重，fine-tuned BioBERT与FastSR的差距保持稳定，显示双向上下文对精确抽取更关键。

- rhetorical_function_cn：报告公开数据集片段结果，并解释GPT-4为何在精确任务上失败。

- depends_on_cn：EBM-NLP句子分类结果和WD/COVID片段结果。

- sets_up_cn：为讨论LLM局限和FSL优越性提供证据。

- evidence_pointer：Table 12

### 44. WD ablation paragraphs after Table 13

- order：44

- section：Evaluation Results: Ablation Analysis

- locator：WD ablation paragraphs after Table 13

- move_code：RESULT

- paraphrase_cn：在WD上移除全局上下文、注意力和联合学习分别使句子F1@3下降3.64%、4.30%和4.74%；双移除进一步下降；替代的层级MTL和图摘要全局上下文也都不如原设计；减少1/3样本仍较稳健。

- rhetorical_function_cn：把整体性能优势分解为具体组件的贡献。

- depends_on_cn：完整FastSR结果和表13。

- sets_up_cn：为EBM-NLP消融和样本敏感性分析做铺垫。

- evidence_pointer：Tables 13-14

### 45. EBM-NLP ablation paragraphs after Table 15

- order：45

- section：Evaluation Results: Ablation Analysis

- locator：EBM-NLP ablation paragraphs after Table 15

- move_code：RESULT

- paraphrase_cn：在EBM-NLP上移除注意力使句子F1下降1-2%、片段F1下降3%；移除联合学习使句子F1下降约2%、片段F1下降约5%；趋势与WD一致。

- rhetorical_function_cn：证明WD上的消融结论在公开摘要数据上可复现。

- depends_on_cn：WD消融结果。

- sets_up_cn：强化核心组件因果贡献的外部效度。

- evidence_pointer：Table 15

### 46. Figure 3 paragraph

- order：46

- section：Evaluation Results: Sample Sensitivity

- locator：Figure 3 paragraph

- move_code：ROBUSTNESS_OR_BOUNDARY_TEST

- paraphrase_cn：在EBM-NLP上增大训练样本到200、300、500后，FastSR仍领先，但与基准的差距缩小，说明其优势主要体现在低标签区域。

- rhetorical_function_cn：刻画FastSR有效性的边界条件。

- depends_on_cn：消融和WD样本减少测试。

- sets_up_cn：讨论部分关于边界条件的表述。

- evidence_pointer：Figure 3

### 47. Figure 4 paragraphs

- order：47

- section：SR Automation: Report Generation

- locator：Figure 4 paragraphs

- move_code：RESULT

- paraphrase_cn：在WD报告生成中，FastSR的PICO要素分布图比ProtoNet更贴近专家报告；ProtoNet遗漏多篇关键文章，例如中国样本量图中漏掉691人研究，Trientine图中漏掉最高质量临床试验。

- rhetorical_function_cn：用具体报告可视化展示下游价值差异。

- depends_on_cn：离线性能差异。

- sets_up_cn：为“FastSR更接近专家结果”提供直观证据。

- evidence_pointer：Figure 4

### 48. Appendix F1 and paragraphs

- order：48

- section：SR Automation: Qualitative Feedback

- locator：Appendix F1 and paragraphs

- move_code：RESULT

- paraphrase_cn：SR专家访谈认为FastSR重要且有用，能找出浓缩摘要中可能被忽略的句子，节省PICO抽取时间后可聚焦于证据综合；也建议增加用户界面并修订SR协议。

- rhetorical_function_cn：用定性证据验证实际工作流程中的可用性。

- depends_on_cn：报告生成结果。

- sets_up_cn：为FastSR增强SR协议和结论提供用户视角。

- evidence_pointer：Appendix F1, Section 'Qualitative feedback'

### 49. Table 16 paragraphs

- order：49

- section：SR Automation: Economic Benefits

- locator：Table 16 paragraphs

- move_code：RESULT

- paraphrase_cn：基于550篇文章的项目模型，FastSR通过更少的唯一句数、更高的P@1/R@1降低验证和假预测修正时间，相比人工SR节省约65%时间和约73,500美元；相比ProtoNet/CNN节省20-25%。

- rhetorical_function_cn：把性能优势转化为经济成本节省。

- depends_on_cn：WD项目的真实时间投入和模型指标。

- sets_up_cn：支持论文标题中“Automating in high-expertise, low-label environments”的实际价值主张。

- evidence_pointer：Table 16

### 50. Figure 5 paragraphs

- order：50

- section：SR Automation: Implications on SR Guidelines

- locator：Figure 5 paragraphs

- move_code：CONTRIBUTION

- paraphrase_cn：作者提出FastSR增强的SR流程：计划阶段专家标注少量样本，FastSR半自动完成摘要筛选和全文PICO抽取，专家只需验证和修正，从而把工作重心转向证据综合。

- rhetorical_function_cn：把实证结果转成可操作的新流程建议。

- depends_on_cn：报告生成、访谈和成本分析。

- sets_up_cn：为Discussion中的设计知识做铺垫。

- evidence_pointer：Figure 5

### 51. P2

- order：51

- section：Discussion

- locator：P2

- move_code：CONTRIBUTION

- paraphrase_cn：作者主张在高专家性低标签环境中做计算设计，先深入理解应用环境再用理论指导设计，该路径可作为IS设计科学研究的模板。

- rhetorical_function_cn：第一项讨论贡献：方法论路径。

- depends_on_cn：全文设计过程。

- sets_up_cn：为后续理论回接和评价策略讨论定调。

- evidence_pointer：Discussion, first subsection

### 52. P3

- order：52

- section：Discussion

- locator：P3

- move_code：THEORY_RETURN

- paraphrase_cn：人类sensemaking通过组合简单部件形成语义；FastSR用组合性理论识别部件与关系，用多原型FSL实现类似的人类式学习，产生多个组件协同的效果。

- rhetorical_function_cn：把结果回接到组合性理论，使贡献不局限于工程性能。

- depends_on_cn：消融证明组件协同。

- sets_up_cn：为AI人机协同设计含义做铺垫。

- evidence_pointer：Discussion, 'Making machines learn like humans'

### 53. P4

- order：53

- section：Discussion

- locator：P4

- move_code：CONTRIBUTION

- paraphrase_cn：作者提出针对复杂社会技术环境的制品需要定制化多侧面评价策略，包括基准、消融、下游案例、访谈和边界条件评估。

- rhetorical_function_cn：第二项讨论贡献：评价方法。

- depends_on_cn：前文评价部分全部证据。

- sets_up_cn：为未来AI/ML设计研究提供方法论建议。

- evidence_pointer：Discussion, 'Customized evaluation strategy'

### 54. P5

- order：54

- section：Discussion

- locator：P5

- move_code：LIMITATION_AND_FUTURE

- paraphrase_cn：作者列出五项局限：仅限医学SR领域；PICO类由专家预定义；PICO层级未利用；ALM虽在抽取中落后但可用于证据综合；具体ML组件可随新技术替换。

- rhetorical_function_cn：限定贡献边界并指向未来研究。

- depends_on_cn：前文结果和边界条件。

- sets_up_cn：为结论中的“问题驱动框架稳定、组件可替换”做铺垫。

- evidence_pointer：Discussion, limitations paragraph

### 55. P6

- order：55

- section：Discussion

- locator：P6

- move_code：BOUNDARY_CONDITION

- paraphrase_cn：作者指出设计框架面向高专家性低标签问题保持稳定，但单个组件可随技术迭代更换，隐含FastSR不是一次性模型而是可演进设计。

- rhetorical_function_cn：保护贡献避免被具体模型版本取代。

- depends_on_cn：前面局限和讨论。

- sets_up_cn：为结论收束和未来组件升级留下空间。

- evidence_pointer：Discussion, final paragraph before conclusion

### 56. Final paragraph

- order：56

- section：Conclusion

- locator：Final paragraph

- move_code：CONTRIBUTION

- paraphrase_cn：结论重申FastSR是把人类标注逻辑融入少样本框架的定制FSL，多侧面评价支持其在数据抽取和SR自动化上的价值，对高专家性低标签环境制品设计有重要意义。

- rhetorical_function_cn：以贡献重申和一般化收束全文。

- depends_on_cn：全文证据链。

- sets_up_cn：无后续；是终点。

- evidence_pointer：Conclusion

## 写作技术

- gap_construction_cn：先承认IS计算设计关注自动化，但指出主流场景是标注充足；随后用SR具体现象说明现有ML方案在标注成本、覆盖范围和性能三方面的不足，从而形成“高专家性、低标签环境下需要新制品”的缺口。

- signposting_cn：引言结尾列出贡献清单；第二节用Table 2把任务复杂度、设计需求、文献、基准和设计组件并列；每个Task Complexity小节都以“Task complexity→设计需求→相关文献→评价基准”的统一结构推进；评价部分明确说分为句子分类、序列标注和SR自动化三部分。

- transition_logic_cn：Task Complexity一节末尾用“Hence, we propose DRx”过渡到下一需求；FastSR各模块小节以“This component aims to represent...”起始；评价部分从“句子分类有效”过渡到“但还需检查片段抽取”，再到“还需知道组件为什么有效”，最后到“还需知道真实流程是否受益”。

- claim_evidence_rhythm_cn：每个主要声明后面都紧跟表格或图：例如性能声明→Table 7-12；组件贡献声明→Table 13-15；下游价值声明→Figure 4/Table 16；文本段落负责解释，表格提供精确数字。

- benchmark_narrative_cn：benchmark不是孤立堆模型，而是围绕四类已有方案（传统、SSL、LLM、FSL）组织，并解释每类为何不足以解决SR问题；随后用消融把模型比较升级为组件归因；再通过COVID复用和EBM-NLP公开数据把结论推向泛化。

- theory_return_cn：讨论部分不是简单重复结果，而是把FastSR的三种原型和联合学习重新放到组合性理论和sensemaking语言下，说明“各设计组件协同产生运营效用”，使理论看起来是设计而非事后包装。

- contribution_positioning_cn：贡献被放在AI设计研究、理论指导抽象、可复用设计需求、实际增强协议和评价策略五个层面，避免只申报“我们做出了一个更准的模型”。

- novelty_protection_cn：通过消融证明每个组件不可删；通过基准模型覆盖传统、SSL、LLM、FSL四类说明不是靠单一baseline；通过WD/COVID/EBM-NLP三数据集和reuse实验说明不是单点过拟合；通过GPT数据污染解释LLM差距，避免被“换更大LLM”简单推翻；最后强调组件可替换、框架稳定。

## 可复用研究与写作程序

### structure_steps

#### 1. 1

- step：1

- writing_job_cn：写清楚现实流程的痛点、现实后果和为什么现有IS制品不匹配；把一般自动化兴趣收窄到特定高专家性低标签流程。

- research_job_cn：选定一个真实、劳动密集、依赖专家且标注昂贵的过程；收集其平均耗时、成本或失败案例。

- required_evidence_cn：能证明该流程重要、慢、难标注的数据或文档；现有ML/NLP方案在该流程上的明确局限。

- transition_to_next_cn：用“为了解决这些问题，本文提出...”切入制品。

#### 2. 2

- step：2

- writing_job_cn：把目标流程拆成子步骤，找出最劳动密集且IT支持最弱的一步；把该步拆成若干任务复杂度。

- research_job_cn：查看领域手册、流程标准和专家操作；访谈专家确认。

- required_evidence_cn：子步骤表（劳动强度+现有支持）；每个复杂度有具体领域例子。

- transition_to_next_cn：把每个任务复杂度压缩成“Hence, DRx”。

#### 3. 3

- step：3

- writing_job_cn：引入一个认知/组织/技术理论，解释为什么人类专家能在少样本下工作；用该理论把复杂度转成设计需求。

- research_job_cn：选择与专家行为机制匹配的理论；确保理论能给出“部件、关系、表示”等可设计语言。

- required_evidence_cn：至少能够从理论命题推出一个可操作设计要求。

- transition_to_next_cn：用需求清单引导下一节架构设计。

#### 4. 4

- step：4

- writing_job_cn：把每条设计要求翻译成具体算法/架构组件；用公式或图展示组件如何交互；同时预告未来评价将如何检验每个组件。

- research_job_cn：实现模型，确定输入表示、损失函数、训练策略，并准备消融入口。

- required_evidence_cn：可以运行的代码或伪代码；能清晰指出哪些模块可被独立关闭。

- transition_to_next_cn：“接下来评估是否满足设计需求”引出评价。

#### 5. 5

- step：5

- writing_job_cn：设置多层评价：全局基准给出整体优势；消融给出组件归因；替代设计排除“换一种实现也差不多”的质疑。

- research_job_cn：建baseline组，覆盖现有主流方法；设计消融开关；准备多个数据集或情境。

- required_evidence_cn：有显著差异的表格；消融显示关键组件贡献；样本或域变化下边界清晰。

- transition_to_next_cn：离线指标后转移到真实流程价值。

#### 6. 6

- step：6

- writing_job_cn：用下游用例证明“不仅更准，还有用”：可以是可视化报告、专家反馈、决策质量、时间成本或用户采纳。

- research_job_cn：寻找合作机构/专家；构建能展示实际产出的材料；做访谈或时间成本模型。

- required_evidence_cn：真实报告对比图、引用级定性反馈、按真实项目规模计算的时间和成本数字。

- transition_to_next_cn：讨论边界、局限和设计知识。

#### 7. 7

- step：7

- writing_job_cn：把结果回接到理论，提炼可复用设计原则和边界条件；明确哪些组件会随技术变化，哪些框架性知识稳定。

- research_job_cn：将设计需求、实现、证据和局限整理成可迁移的“设计知识”；对照引言缺口说明贡献。

- required_evidence_cn：对适用边界的正面和反面证据；未来研究需要解决的具体空白。

- transition_to_next_cn：结论一句话重申制品、证据和领域含义。

### most_transferable_moves_cn

1. 先定位流程中最耗时且支持最弱的步骤

2. 用专家访谈和领域手册把复杂度显式化

3. 用理论给出“部分-组合-关系”的设计语言

4. 用Table 2把复杂度/需求/文献/基准/组件并列，提前埋下评价点

5. 通过消融把整体模型比较转成组件因果归因

6. 用三数据集+reuse实验证明泛化而非单点过拟合

7. 用下游报告/访谈/成本模型把性能数字转成真实价值

8. 在讨论中强调“框架稳定、组件可替换”以保护贡献生命周期

### resource_intensive_or_nonstandard_parts_cn

1. WD私有数据集来自真实药企SR项目，需要多年行业合作关系

2. COVID专家标注由具有30年医学经验的团队完成，标注成本高

3. GPT API实验费用高（文中提约4,660美元），且对封闭域仍表现差

4. 真实SR公司合作和专家访谈不是一般研究者容易获得的资源

5. 对三数据集的逐句专家验证和kappa计算需要医学专家长期参与

### what_not_to_copy_superficially_cn

1. 不能只照搬“我们提出X框架，基准更好”而没有设计需求与组件消融

2. 不能把时间节省宣称建立在未经验证的假设上，必须有真实项目参数和敏感性说明

3. 不能把GPT低绩效简单归因于架构，而应做开放域/封闭域区分和数据污染分析

4. 不能只在讨论中声称“受组合性理论指导”，而需在设计需求、组件和消融中有可追踪映射

- single_best_description_of_the_routine_cn：先通过领域分析和专家访谈定位高专家性低标签流程中最痛的一步，用理论把任务复杂度转成设计需求，再构建设计制品并用三数据集基准、消融和下游真实工作流证据逐步证明“为什么有效、何处有效、值多少”。

## 分析边界

由于原文以网页/PDF转换文本呈现，没有稳定页码，所有位置证据只能使用段落、表格、图和公式编号；文中在WD训练句数上存在不一致（正文提到222句，Table 6各列合计为418句，Appendix F2显示660句含NA），分析中按研究阶段描述而未纠结具体数字；附录G/H是补充材料，但系统提示只要求对全文结构判断，不影响主证据链。
