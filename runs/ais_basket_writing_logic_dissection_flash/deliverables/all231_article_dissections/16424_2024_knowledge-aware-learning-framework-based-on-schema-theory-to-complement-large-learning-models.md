# Knowledge-Aware Learning Framework Based on Schema Theory to Complement Large Learning Models

- 作者：Long Xia; Wenqi Shen; Weiguo Fan; G. Alan Wang
- 年份 / 期刊：2024 / Journal of Management Information Systems
- DOI：10.1080/07421222.2024.2340827
- 源文件：16424_2024_knowledge-aware-learning-framework-based-on-schema-theory-to-complement-large-learning-models.md
- 论文主类型：build_evaluate_design_science
- 主导写作弧线：requirements_build_evaluate_design_principles
- 置信度：0.84

## 文章级论证概况

- 核心问题：能否依据认知科学中的图式理论（schema theory）设计一种知识感知学习框架，使其仿照人类学习过程中知识的获取、表征、激活和利用方式，从而在不依赖大规模预训练语言模型（LLM）的情况下，达到可比的文本分析性能并提升学习效率与稳健性。

- 制品与设计：一个四组件知识感知深度学习框架：以ConceptNet作为人类长期记忆式大知识库；将知识三元组组织为结构化知识图谱/图式；用基于TF-IDF思想的任务相关边权重实现图式激活，构建上下文知识图谱；用两层GCN编码激活知识、双向LSTM编码焦点文本，并通过TransE生成概念与关系嵌入。

- 客观结果：在R52、Ohsumed、20-News、MR及NLI基准上与六类基线比较：在显式知识模型中领先（如MR上较Text GCN提升8.3个百分点），与依赖LLM的BertGCN、DeBERTa等达到可比性能；在20-News上达到最优；在10%训练数据下性能下降远小于基线；模型参数约为BertGCN的7.6%，训练时间更快；在知识图谱缺失和噪声情境下保持稳健；消融实验验证各组件的贡献；知识类型实验显示概念性知识是基础、情境性知识激活作用显著，并存在知识类型协同效应。

- 核心贡献：作者声称首次以图式理论为内核理论，通过设计科学研究方法构建了覆盖人类知识处理全过程的、具有认知合理性的知识感知学习框架；该框架以较小的参数、较少的数据和更快的训练实现与LLM可比的性能，并将认知科学引入可解释、可与人协作的AI设计。

- 整篇论证链：文章先建立人类与AI在学习有效性、效率和稳健性上的差距，指出根本差异在于人类拥有丰富先验知识而AI缺少常识性知识；随后将已有AI研究分为隐式编码知识的LLM和显式引入外部知识的知识感知模型，并分别批评前者把知识隐含在参数中、缺乏可解释性，后者要么用静态向量造成多义词问题、要么用GCN却忽视知识选择。接着引入图式理论，把人类学习拆解为知识获取、表征、激活、利用四个环节，由此形成ISDT中的内层理论、元需求、元设计和可检验假设。框架以ConceptNet模拟长期记忆，用知识三元组构造结构化图式，用TF-IDF启发式边权重完成任务相关激活，用bi-LSTM+GCN整合焦点文本与激活知识。五个实验依次支撑有效性、效率、稳健性、组件有效性和知识类型机制，最后在讨论中回到认知科学与设计科学，把局部性能结果提升为关于知识激活机制和设计知识的一般性主张。

## 类型与写作弧线判定

- 论文主类型判定：文章明确采用设计科学研究（DSR）和信息系统设计理论（ISDT），从图式理论推导元需求、元设计、可检验假设，构建完整知识感知学习框架，并以基准对比、效率比较、稳健性扰动、消融实验和知识类型实验进行系统评价。即使核心产物是计算制品，其写作和论证组织完全符合需求—构建—评价—设计知识的设计科学范式。

- 主导写作弧线判定：论证主线从图式理论作为内核理论出发，明确列出四条元需求，再将每条元需求转化为具体元设计组件，随后用H1-H4可检验假设驱动五个实验，最后在讨论中把实证结果转化为设计知识和理论启示，形成requirements-build-evaluate-design-principles的标准弧线。

## 研究开展程序

- study_or_phase_count：7

- 研究阶段总序列：阶段1是理论驱动的框架设计与实现，完成从图式理论到四组件设计的具体化；阶段2用全量基准数据集检验有效性，回答能否达到先进水平；阶段3通过缩小训练数据检验学习效率与泛化性；阶段4和阶段5分别以知识图谱缺失和噪声模拟外部知识不完美，检验稳健性；阶段6用消融实验把性能归因到三个关键设计组件；阶段7通过概念性、程序性和情境性知识的单用与组合检验知识机制。各阶段之间形成‘有效—高效—稳健—组件归因—机制解释’的逐步收束结构，每步为下一步提供新的待检验边界面。

### studies_or_phases

#### 1. 图式理论驱动的框架设计与实现

- order：1

- name_cn：图式理论驱动的框架设计与实现

- question_cn：能否将图式理论中的人类知识处理过程转化为可计算的知识感知学习框架？

- inputs_and_setting_cn：图式理论的四个知识过程、ConceptNet知识库、Wikipedia dump用于构建上下文背景频率、目标任务语料用于计算任务内共现频率。

- designed_or_compared_object_cn：四个元设计元素：大规模知识库、结构化知识图式、基于边权重的图式激活机制、bi-LSTM+GCN的整合学习模型。

- baseline_control_or_counterfactual_cn：无对照，本阶段是设计建构而非评价；对照出现在后续实验中。

##### objective_metrics

1. 设计组件的完整性与可追溯性

- analysis_method_cn：ISDT设计方法：内核理论→元需求→元设计→可检验假设

- main_result_cn：生成表1的四组件ISDT设计及图2完整框架。

- argumentative_role_cn：把抽象认知理论翻译成可实施的计算制品，为后续实验提供可实例化的对象。

- remaining_uncertainty_cn：设计是否真正有效、高效、稳健，以及每个组件是否都必要，尚不清楚。

- link_to_next_phase_cn：通过表1的H1-H4提出评价承诺，直接引出五个实验。

##### evidence_pointers

1. Table 1

2. Figure 2

3. Metadesign Element 1-4

#### 2. 实验1：学习框架的有效性基准测试

- order：2

- name_cn：实验1：学习框架的有效性基准测试

- question_cn：设计能否在标准文本分析和NLI任务上达到与现有知识感知模型和先进LLM相当的有效性？

- inputs_and_setting_cn：四个文本分类数据集R52、Ohsumed、20-News、MR，一个NLI数据集；同一框架实例；六种基线。

- designed_or_compared_object_cn：完整设计框架

- baseline_control_or_counterfactual_cn：显式知识基线Text GCN和KIM；隐式LLM基线BertGCN、MTL、EFL、DeBERTa；另附资源消耗对比BertGCN。

##### objective_metrics

1. F1（weighted）

2. 模型参数量

3. 训练时间

4. 外部数据规模

- analysis_method_cn：基准数据集上的对照实验，表4报告性能，表5报告20-News上的计算效率。

- main_result_cn：框架在全部任务上超过Text GCN和KIM，在20-News上超过所有基线，在其他任务上与LLM可比；模型参数8.36M vs BertGCN 109.6M，训练时间0.87小时 vs 2.39小时。

- argumentative_role_cn：回答RQ2，说明不依赖LLM也能达到可比性能；同时为后续效率实验提供全量数据下的表现基线。

- remaining_uncertainty_cn：有效性只在全量训练数据下检验，尚未检验少数据情境、外部知识不完美和组件必要性。

- link_to_next_phase_cn：表5的效率结果只是单点比较，实验2系统化地改变训练数据比例，将效率从资源比较扩展为学习曲线比较。

##### evidence_pointers

1. Table 4

2. Table 5

3. Experiment 1

#### 3. 实验2：学习效率与有限训练数据下的表现

- order：3

- name_cn：实验2：学习效率与有限训练数据下的表现

- question_cn：训练数据从100%缩减到1%时，框架是否比知识感知基线和LLM基线更稳健，从而体现更高学习效率？

- inputs_and_setting_cn：R52、20-News、Ohsumed以及新增ADE Detection和PubMed Classification；训练数据比例100%、60%、30%、10%、1%等；超参和测试集不变。

- designed_or_compared_object_cn：框架与Text GCN、BertGCN在相同数据缩减曲线下比较。

- baseline_control_or_counterfactual_cn：同一任务中缩减训练数据的反事实；Text GCN和BertGCN作为对照。

##### objective_metrics

1. F1随训练比例变化的曲线

2. 性能下降幅度

- analysis_method_cn：受控数据缩减实验，图5可视化多任务学习曲线。

- main_result_cn：例如R52从100%到10%数据时框架仅下降5.9%，Text GCN下降18.3个百分点、BertGCN下降33.2个百分点；低数据下Text GCN甚至超过BertGCN；框架在所有任务上都呈现更平缓的下降。

- argumentative_role_cn：直接支撑RQ3和H1的效率维度，并说明设计具有跨任务类型和领域的泛化性。

- remaining_uncertainty_cn：尚未考虑外部知识库本身不完整或包含错误关系的情况。

- link_to_next_phase_cn：既然外部知识库是关键依赖，实验3转向知识图谱不完整和噪声带来的稳健性检验。

##### evidence_pointers

1. Figure 5

2. Experiment 2

#### 4. 实验3a：对知识图谱不完整性的稳健性

- order：4

- name_cn：实验3a：对知识图谱不完整性的稳健性

- question_cn：当ConceptNet随机缺失10%、50%、90%三元组时，框架性能会下降多少？

- inputs_and_setting_cn：五个任务R52、20-News、Ohsumed、PubMed_20K、ADE；在知识激活前随机删除ConceptNet中的知识三元组。

- designed_or_compared_object_cn：完整知识图谱vs删除10%、50%、90%知识三元组后的框架。

- baseline_control_or_counterfactual_cn：不含外部知识的模型基线；完整知识图谱作为100%性能参照。

##### objective_metrics

1. F1

2. 保留的性能改进百分比

3. 统计显著性

- analysis_method_cn：随机缺失多轮运行（每个比例10次）取均值，比较性能改进的保留量。

- main_result_cn：删除10%时下降微不足道且多不显著；删除50%时仍保留80%以上的性能改进；删除90%时保留约40%-51%的改进，但所有下降显著。

- argumentative_role_cn：支撑H2，说明框架在常见知识库不完整程度下仍能维持学习能力。

- remaining_uncertainty_cn：只处理缺失，尚未处理错误关系。

- link_to_next_phase_cn：由缺失转到噪声，检验错误关系是否同样不影响性能。

##### evidence_pointers

1. Table 6

2. Resilience to Knowledge Graph Incompleteness

#### 5. 实验3b：对知识图谱噪声的稳健性

- order：5

- name_cn：实验3b：对知识图谱噪声的稳健性

- question_cn：当ConceptNet中1%或5%的关系被随机替换为错误关系时，框架性能是否依然稳定？

- inputs_and_setting_cn：五个任务；随机选取1%或5%三元组并赋予错误关系。

- designed_or_compared_object_cn：完整知识图谱vs含1%和5%噪声知识图谱的框架。

- baseline_control_or_counterfactual_cn：无知识基线；完整知识图谱作为参照。

##### objective_metrics

1. F1

2. 性能改进保留百分比

- analysis_method_cn：每种噪声水平10次随机运行取平均，与完整KG比较。

- main_result_cn：1%和5%噪声下性能下降均微小且统计上不显著，知识改进百分比多保持在90%以上。

- argumentative_role_cn：进一步支撑H2，说明当前知识图谱约95%-99%准确率已足以支撑该框架。

- remaining_uncertainty_cn：稳健性检验未解释哪些组件真正导致性能差异。

- link_to_next_phase_cn：实验4用消融实验把稳健性能归因到三个核心设计组件。

##### evidence_pointers

1. Table 7

2. Resilience to Noise in the Knowledge Graph

#### 6. 实验4：组件消融研究

- order：6

- name_cn：实验4：组件消融研究

- question_cn：GCN、bi-LSTM编码器和知识激活机制各自对完整框架的性能贡献是多少？

- inputs_and_setting_cn：R52、20-News、Ohsumed、MR四个任务；每次移除一个核心组件。

- designed_or_compared_object_cn：完整设计 vs 不含GCN vs 不含bi-LSTM vs 无知识激活（随机选择K个三元组）

- baseline_control_or_counterfactual_cn：完整设计为参照；无知识激活作为知识选择机制的反事实。

##### objective_metrics

1. F1

- analysis_method_cn：逐一删组件的消融比较，表8记录性能。

- main_result_cn：任一组件删除均导致性能下降，例：20-News从89.6%降到84.2%-87.5%。

- argumentative_role_cn：支撑H3，将性能改进从整体设计归因到具体设计元素。

- remaining_uncertainty_cn：消融只说明组件必要性，未说明不同知识类型在认知机制中的角色。

- link_to_next_phase_cn：实验5进一步放开知识类型，考察概念性、程序性、情境性知识的作用。

##### evidence_pointers

1. Table 8

2. Experiment 4

#### 7. 实验5：知识类型与知识机制

- order：7

- name_cn：实验5：知识类型与知识机制

- question_cn：概念性、程序性、情境性知识在单用与组合时如何影响学习性能，是否存在协同效应？

- inputs_and_setting_cn：R52、20-News、Ohsumed、PubMed_20K、ADE；按认知科学分类对知识三元组分组；为隔离知识作用，移除文本表示部分。

- designed_or_compared_object_cn：使用概念性、程序性、情境性知识及其组合的框架变体。

- baseline_control_or_counterfactual_cn：不引入任何外部知识的模型作为基线；完整三类知识组合作为100%改进参照。

##### objective_metrics

1. F1

2. 相对基线的改进百分比

- analysis_method_cn：分组组合比较，表9报告改进百分比；语义上判断是否存在协同效应（组合改进大于单独改进之和）。

- main_result_cn：概念性知识通常比程序性知识贡献更大；情境性知识单独使用时在医学任务上贡献显著；概念+程序+情境的组合改进超过三者和。例如R52单独改进合计80.5%，组合达到100%。

- argumentative_role_cn：支撑H4，把计算实验结果回接到认知科学关于知识类型关系的理论，并以情境性知识激活机制解释框架的工作方式。

- remaining_uncertainty_cn：只测试了有限领域；概念性和程序性知识的反向关系未得到证据；未检验动态知识。

- link_to_next_phase_cn：讨论部分把知识类型证据提升为对认知科学和AI研究的意义，并指出局限。

##### evidence_pointers

1. Table 9

2. Experiment 5

3. Online Supplemental Appendices 2 and 3

## 各部分修辞架构

### abstract_moves

1. CONTEXT

2. GAP

3. THEORY_INTRO

4. DESIGN_FEATURE

5. RESULT

6. CONTRIBUTION

### introduction_moves

1. CONTEXT

2. PRACTICAL_STAKES

3. PHENOMENON

4. MECHANISM

5. THEORY_INTRO

6. GAP

7. WHY_GAP_MATTERS

8. RQ_OR_OBJECTIVE

9. STUDY_OVERVIEW

10. CONTRIBUTION

### theory_and_knowledge_moves

1. PRIOR_KNOWLEDGE

2. THEORY_INTRO

3. THEORY_PROPOSITION

4. MECHANISM

5. LIMITATION

6. GAP

### artifact_design_moves

1. METHOD_JUSTIFICATION

2. REQUIREMENT

3. DESIGN_FEATURE

4. MECHANISM

5. STUDY_OVERVIEW

### evaluation_moves

1. HYPOTHESIS_OR_PROPOSITION

2. METHOD_JUSTIFICATION

3. BENCHMARK_OR_CONTRAST

4. RESULT

5. ROBUSTNESS_OR_BOUNDARY_TEST

### discussion_and_contribution_moves

1. CONTRIBUTION

2. BOUNDARY_CONDITION

3. THEORY_RETURN

4. LIMITATION_AND_FUTURE

## 理论/知识到设计的翻译

### 知识/理论基础

1. 图式理论（schema theory）：知识结构、图式激活、知识获取/表征/激活/利用

2. 认知科学知识分类：概念性知识、程序性知识、情境性知识

3. 外部知识资源：ConceptNet

4. 信息检索启发式：TF-IDF

5. 深度学习技术知识：bi-LSTM、GCN、TransE

- 理论—设计耦合：direct

- 耦合判定理由：作者明确采用ISDT，把图式理论作为内核理论，并由其推导四条元需求，再逐条映射到四个元设计组件。虽然具体技术手段（GCN、bi-LSTM、TF-IDF）来自工程工具箱，但框架的整体结构、组件分解和评价假设均由图式理论前瞻性决定，且评价直接检验包含/不包含这些理论要素的差异。

- 理论到设计翻译链：图式理论认为人类学习包含知识获取、知识表征、知识激活与知识利用四个过程→ISDT元需求要求设计包含大知识库、结构化图式、激活机制、整合模型→元设计分别采用ConceptNet作为大知识库、把知识三元组组织成知识图谱、用任务相关边权重实现图式激活、用bi-LSTM+GCN完成整合→四个可检验假设H1-H4分别评价有效性/效率、稳健性、组件贡献、知识类型关系→实验结果显示完整设计有效、高效、稳健，并且每个组件和知识类型均有可识别作用。

### mapping_table

#### 1. 1

- theory_or_knowledge_claim_cn：人类通过长期经验形成海量先验知识，并存储于长期记忆中

- mechanism_cn：丰富的背景知识为后续学习提供支撑

- design_requirement_cn：设计应包含大规模知识库以模拟长期记忆（元需求1）

- artifact_choice_cn：选用ConceptNet作为外部知识库

- evaluated_contrast_cn：有外部知识 vs 无外部知识基线；不完整和噪声知识图谱

- objective_result_cn：完整框架优于无知识基线；删除10%-50%知识仍保留大部分性能；1%-5%噪声影响不显著

##### evidence_pointers

1. Table 6

2. Table 7

3. Table 9 baseline

#### 2. 2

- theory_or_knowledge_claim_cn：人类知识不是孤立事实，而是以概念和关系组成的结构性图式存在

- mechanism_cn：结构化知识支持有组织地检索和应用

- design_requirement_cn：设计应将获取的知识组织成结构化图式（元需求2）

- artifact_choice_cn：把ConceptNet知识三元组重构成以概念为节点、关系为边的知识图

- evaluated_contrast_cn：完整设计 vs 移除GCN的消融；与Text GCN等结构化方法对比

- objective_result_cn：移除GCN导致性能下降；完整框架超过Text GCN，如MR F1 84.4% vs 76.1%

##### evidence_pointers

1. Table 8

2. Table 4

#### 3. 3

- theory_or_knowledge_claim_cn：学习中只有与当前任务相关的知识应从长期记忆中被激活

- mechanism_cn：任务嵌入线索指示搜索方向，激活相关图式

- design_requirement_cn：设计应包含图式激活机制（元需求3）

- artifact_choice_cn：用TF-IDF启发式计算任务相关边权重，构造上下文知识图谱，按权重做top-K激活

- evaluated_contrast_cn：有知识激活 vs 随机挑选K个三元组（无知识激活消融）；噪声与缺失扰动下激活稳定性

- objective_result_cn：无激活时性能下降，例如20-News从89.6%降到86.9%；激活机制在噪声和缺失下仍稳健

##### evidence_pointers

1. Table 8

2. Table 6

3. Table 7

#### 4. 4

- theory_or_knowledge_claim_cn：学习是交互过程，需将激活的图式与当前任务信息整合

- mechanism_cn：局部文本线索与外部知识共同决定输出

- design_requirement_cn：设计应包含整合激活图式与焦点信息的预测模型（元需求4）

- artifact_choice_cn：bi-LSTM编码焦点文本，GCN编码激活知识图，TransE生成概念/关系嵌入

- evaluated_contrast_cn：完整设计 vs 移除bi-LSTM；完整设计 vs 移除GCN

- objective_result_cn：两种移除均导致性能显著下降，说明文本与知识两种表征都必要

##### evidence_pointers

1. Table 8

#### 5. 5

- theory_or_knowledge_claim_cn：认知科学区分概念性、程序性和情境性知识，情境性知识指导相关图式激活

- mechanism_cn：情境性知识帮助选择与任务相关的概念性和程序性图式；概念性知识为程序性知识提供基础

- design_requirement_cn：虽未进入四条元需求，但成为H4和实验5的设计性追问

- artifact_choice_cn：将知识三元组按概念性/程序性/情境性分类并构造单用与组合的实验变体

- evaluated_contrast_cn：每种知识单独使用 vs 组合使用；全部组合 vs 无知识基线

- objective_result_cn：概念性知识贡献通常大于程序性知识，情境性知识在医学任务中单独贡献最高，三类组合表现出超加性协同

##### evidence_pointers

1. Table 9

## 评价逻辑

### evaluation_modes

1. 多任务基准对照：文本分类与NLI基准上的性能比较

2. 计算资源对比：模型参数量、训练时间、外部数据规模

3. 训练数据缩减实验：不同训练比例下的学习曲线

4. 知识图谱扰动：随机删除或错误化知识三元组

5. 组件消融：移除GCN、bi-LSTM、知识激活机制

6. 知识类型因子比较：概念性/程序性/情境性知识单用与组合

- why_these_evaluations_cn：设计科学需要同时回答制品是否有效、是否高效、是否稳健、哪些组件起作用、以及背后的理论机制是否成立。仅做benchmark不足以证明设计知识，因为性能可能来自整体模型而不是理论映射；仅做消融又无法回答是否达到先进水平。因此作者用表4建立有效性、图5建立效率、表6-7建立稳健性、表8建立组件归因、表9建立知识机制，五类证据相互补足，共同支撑H1-H4。

- benchmark_and_contrast_chain_cn：实验1同时纳入显式知识模型（Text GCN、KIM）和隐式知识LLM（BertGCN、MTL、EFL、DeBERTa），构成‘与旧知识感知方法相比更好’和‘与LLM相比可比但更轻量’的双重基准。表5把性能优势转化为资源效率证据；实验2进一步把这一效率优势泛化到训练数据规模维度，形成对LLM数据密集性的系统回应；实验3则说明即使外部知识不完美，框架仍保持改进；实验4和实验5分别把整体性能拆回组件与知识类型，最终使benchmark结果上升为可复用的设计知识。

### claim_evidence_ledger

#### 1. 框架在文本分析任务上优于现有显式知识感知模型

- claim_cn：框架在文本分析任务上优于现有显式知识感知模型

- evidence_cn：表4显示框架在R52、Ohsumed、20-News、MR、NLI上全面超过Text GCN和KIM

- status_cn：由直接对照证据支持

#### 2. 框架在不依赖LLM的情况下达到与LLM相当的性能

- claim_cn：框架在不依赖LLM的情况下达到与LLM相当的性能

- evidence_cn：表4显示与BertGCN、DeBERTa接近，仅在20-News上最优；并非全面超越

- status_cn：以‘可比’措辞谨慎支持

#### 3. 框架具有更高学习效率，参数量更小、训练更快

- claim_cn：框架具有更高学习效率，参数量更小、训练更快

- evidence_cn：表5在20-News上比较8.36M vs 109.6M参数和0.87h vs 2.39h；图5显示低数据下性能下降更小

- status_cn：支持，但效率计算基于有限数据集和单次对比

#### 4. 框架对知识图谱不完整和噪声具有稳健性

- claim_cn：框架对知识图谱不完整和噪声具有稳健性

- evidence_cn：表6和表7显示10%缺失、1%/5%噪声下影响不显著，50%缺失仍保留大部分改进

- status_cn：支持，90%缺失仍显著下降，边界清晰

#### 5. GCN、bi-LSTM和知识激活机制都是关键设计组件

- claim_cn：GCN、bi-LSTM和知识激活机制都是关键设计组件

- evidence_cn：表8消融实验显示移除任一组件均导致性能下降

- status_cn：支持

#### 6. 概念性、程序性和情境性知识具有不同作用并存在协同效应

- claim_cn：概念性、程序性和情境性知识具有不同作用并存在协同效应

- evidence_cn：表9显示概念性知识贡献通常大于程序性知识，情境性知识单独贡献在医学任务上突出，组合改进超过单独改进之和

- status_cn：部分支持，统计检验细节在在线附录中

#### 7. 框架模仿了人类知识处理过程，因此具有认知合理性

- claim_cn：框架模仿了人类知识处理过程，因此具有认知合理性

- evidence_cn：设计上与图式理论四个过程对应，但没有测量认知过程，也没有人类对照实验

- status_cn：属于理论定位主张，而非直接实证支持

- internal_validity_strategy_cn：使用预先定义的ISDT假设将评价限定在H1-H4；通过消融实验隔离设计组件；通过固定超参数、相同数据集、多轮随机运行平均来控制实验条件；在实验5中刻意剔除文本表示组件，以孤立知识类型效应；使用统计显著性标记判断性能差异是否可靠。

- external_validity_strategy_cn：选取多个文本分析任务（文档、句子、词级分类）和多个领域（新闻、医学、电影情感）以扩大任务类型和领域覆盖面；同时纳入NLI任务；与当前最强的LLM基线并列比较；通过低数据实验展示泛化潜力；通过资源对比说明不是依赖大规模算力获得性能。

- what_is_not_actually_tested_cn：没有直接测量或操纵人类认知过程，所谓‘认知合理性’和‘像人一样激活知识’只是设计映射而非行为证据；没有跨任务类别的形式化迁移测试；没有在真实企业中部署或做现场实验；‘comparable performance’仅在有限数据集上成立，且并非每个任务都达到最优；只使用静态ConceptNet，时间动态知识未被检验；知识类型关系只在计算设置中验证，未做人类被试实验。

## 贡献闭环

- technical_claim_cn：提出的知识感知学习框架在文本分类和NLI任务上达到与先进LLM相当且优于现有显式知识感知模型的性能，同时参数更少、数据需求更低、训练更快。

- artifact_claim_cn：框架的性能改进可归因于三个核心设计元素：GCN结构编码、bi-LSTM文本编码、基于上下文权重的知识激活机制；不激活或移除组件均导致性能下降。

- mechanism_claim_cn：基于TF-IDF思想的任务相关边权重能够激活与当前学习任务最相关的知识图式，类似于图式理论描述的人类知识激活；情境性知识起到控制相关图式激活的作用，概念性知识为程序性知识提供基础。

- boundary_claim_cn：框架在文本分类和NLI任务范围内、在新闻/医学/情感等领域的文档/句子/词级任务上有效；对外部知识库10%-50%的缺失和1%-5%的噪声稳健；在训练数据降至10%时仍保持较高性能；但当90%知识缺失时性能显著下降，且未覆盖动态知识和其他专门领域。

- reusable_design_knowledge_cn：知识感知学习框架可按照知识获取、知识表征、知识激活、知识利用四个环节组织；大规模外部知识库宜配合结构化图式组织与任务相关激活；文本局部信息与外部激活知识的双通道融合是有效方案；在设计科学中使用内核理论到元需求再到元设计的过程能将认知理论转化为AI制品。

- theoretical_contribution_cn：将图式理论引入知识感知AI设计，提供了计算证据表明情境性知识在知识激活中的先行作用、概念性知识与程序性知识的协同而非独立关系，并回应用了Samtani等关于深层学习研究中理论引导和认知合理性的呼吁。

- how_discussion_closes_intro_gap_cn：讨论部分明确回答三个RQ：RQ1由ISDT设计框架证明能够设计认知理论引导的四阶段框架；RQ2由表4的实验证据证明不依赖LLM也可获得可比性能；RQ3由图5和表5证明学习效率提升。随后将结果返回认知科学和设计科学，说明这弥补了引言指出的‘现有知识感知模型缺乏理论基础、知识处理方式与人类不一致’的缺口。

- overclaim_or_unsupported_leaps_cn：最明显的跳跃是从计算性能与设计映射直接推断‘认知合理性’和‘模仿人类知识处理’；没有行为数据或心理物理证据支撑。另一个跳跃是把20-News上的单次计算效率推广为普遍结论；‘comparable performance’也没有在所有数据集上逐项显著检验。知识类型的‘协同效应’基于改进百分比的算术比较，未给出组合与单独效应的推断统计。

## 句级写作动作图谱

### 1. Abstract P1 S1

- order：1

- section：Abstract

- locator：Abstract P1 S1

- move_code：CONTEXT

- paraphrase_cn：尽管AI近期取得显著进展，但在学习有效性和效率上仍不及人类。

- rhetorical_function_cn：开篇建立AI表现的宏大背景与人类学习差距

- depends_on_cn：没有前置，直接锚定研究主题

- sets_up_cn：为引出人的先验知识与AI缺乏常识的缺口作铺垫

- evidence_pointer：Abstract

### 2. Abstract P1 S2

- order：2

- section：Abstract

- locator：Abstract P1 S2

- move_code：GAP

- paraphrase_cn：根本差异在于人类拥有丰富先验知识，而AI缺少完成学习所需的基本常识知识。

- rhetorical_function_cn：提出全文核心差距：知识拥有量的不对称

- depends_on_cn：依赖前句对AI差距的设定

- sets_up_cn：为知识感知框架提供必要性

- evidence_pointer：Abstract

### 3. Abstract P1 S3

- order：3

- section：Abstract

- locator：Abstract P1 S3

- move_code：THEORY_INTRO

- paraphrase_cn：作者以图式理论为指导，采用设计科学研究方法提出新框架。

- rhetorical_function_cn：引入理论和方法论双重支柱

- depends_on_cn：承接知识差距，说明应对路径

- sets_up_cn：预示框架会从认知理论推导

- evidence_pointer：Abstract

### 4. Abstract P1 S4

- order：4

- section：Abstract

- locator：Abstract P1 S4

- move_code：DESIGN_FEATURE

- paraphrase_cn：框架紧密模拟人类获取、表征、激活和利用知识的过程，不同于现有LLM和知识感知方法。

- rhetorical_function_cn：一句话概括晶体设计特征与既有方法的差异

- depends_on_cn：基于图式理论四过程

- sets_up_cn：为摘要中的结果和贡献做设计铺垫

- evidence_pointer：Abstract

### 5. Abstract P1 S5

- order：5

- section：Abstract

- locator：Abstract P1 S5

- move_code：RESULT

- paraphrase_cn：文本分析任务上的广泛评价显示其达到与先进LLM相当的性能，并提升泛化性和学习效率。

- rhetorical_function_cn：在摘要中给出最强结果定位

- depends_on_cn：依赖框架设计描述的成立

- sets_up_cn：引出对认知科学与AI研究的意义

- evidence_pointer：Abstract

### 6. Abstract P1 S6

- order：6

- section：Abstract

- locator：Abstract P1 S6

- move_code：CONTRIBUTION

- paraphrase_cn：本研究向前推进了将认知科学引入可认知合理AI和人机协作研究。

- rhetorical_function_cn：声明学科层面贡献

- depends_on_cn：结果支持后才合法

- sets_up_cn：为讨论部分学科定位埋伏笔

- evidence_pointer：Abstract

### 7. Introduction P1 S1

- order：7

- section：Introduction

- locator：Introduction P1 S1

- move_code：CONTEXT

- paraphrase_cn：深度学习在NLP多个任务上带来表现突出的AI系统。

- rhetorical_function_cn：建立技术繁荣背景

- depends_on_cn：无前置，直接进入背景

- sets_up_cn：随后用ChatGPT案例强化当前进展

- evidence_pointer：Introduction P1

### 8. Introduction P1 S2

- order：8

- section：Introduction

- locator：Introduction P1 S2

- move_code：PRACTICAL_STAKES

- paraphrase_cn：ChatGPT受到广泛关注，但Sam Altman呼吁停止单纯扩大模型，转而提升学习能力、减少参数并发展类人认知AI。

- rhetorical_function_cn：用行业领袖观点赋予问题现实重要性

- depends_on_cn：依赖前一S对AI进展的描述

- sets_up_cn：引出效率与认知合理性主题

- evidence_pointer：Introduction P1

### 9. Introduction P2 S1

- order：9

- section：Introduction

- locator：Introduction P2 S1

- move_code：PHENOMENON

- paraphrase_cn：人类能从单个样例学习新概念，AI却需要成千上万样例，且巨型模型成本高昂却仍犯事实和逻辑错误。

- rhetorical_function_cn：用具体现象展示人类与AI学习效率的鲜明反差

- depends_on_cn：延续P1中AI差距的铺垫

- sets_up_cn：为‘学习过程未准确镜像人类’提供诱因

- evidence_pointer：Introduction P2

### 10. Introduction P2 S2

- order：10

- section：Introduction

- locator：Introduction P2 S2

- move_code：MECHANISM

- paraphrase_cn：当前AI只是松散地受大脑结构启发，并未准确反映人类学习过程，因此开发认知合理AI是逼近人类水平的有希望路径。

- rhetorical_function_cn：把现象归因到机制：缺少对认知过程的模拟

- depends_on_cn：基于P2 S1中的对比

- sets_up_cn：为引入认知合理性概念铺垫

- evidence_pointer：Introduction P2

### 11. Introduction P3 S1

- order：11

- section：Introduction

- locator：Introduction P3 S1

- move_code：THEORY_INTRO

- paraphrase_cn：认知合理性的定义是计算模型能在何种程度上模仿人类认知过程。

- rhetorical_function_cn：正式引入理论术语并界定范围

- depends_on_cn：承接P2中‘认知合理AI’

- sets_up_cn：后续将知识差异视为认知合理性核心

- evidence_pointer：Introduction P3

### 12. Introduction P3 S2

- order：12

- section：Introduction

- locator：Introduction P3 S2

- move_code：GAP

- paraphrase_cn：普遍观点认为人类有大量先验知识，而AI缺少帮助学习的常识知识。

- rhetorical_function_cn：把认知合理性问题聚焦到知识层面

- depends_on_cn：依赖认知合理性定义

- sets_up_cn：为‘知识感知模型’主题做知识性缺口铺垫

- evidence_pointer：Introduction P3

### 13. Introduction P4 S1

- order：13

- section：Introduction

- locator：Introduction P4 S1

- move_code：RQ_OR_OBJECTIVE

- paraphrase_cn：由此研究焦点转向开发知识感知模型，这是AI研究最活跃领域之一。

- rhetorical_function_cn：把一般缺口收缩为具体研究领域

- depends_on_cn：前面知识缺口论证

- sets_up_cn：随后定义和评估知识感知模型

- evidence_pointer：Introduction P4

### 14. Introduction P5 S1

- order：14

- section：Introduction

- locator：Introduction P5 S1

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：引用Ji等人定义，知识感知模型是在学习过程中显式整合外部知识的计算模型。

- rhetorical_function_cn：为术语提供明确操作定义

- depends_on_cn：确认研究焦点为知识感知模型

- sets_up_cn：后续用该定义评价现有模型

- evidence_pointer：Introduction P5

### 15. Introduction P5 S2

- order：15

- section：Introduction

- locator：Introduction P5 S2

- move_code：LIMITATION

- paraphrase_cn：某些知识感知模型把外部知识作为额外词嵌入，但词嵌入是静态向量，导致多义词问题和缺乏上下文特异。

- rhetorical_function_cn：指出第一类现有方法的缺陷

- depends_on_cn：知识感知模型定义

- sets_up_cn：为图式理论的结构化知识方案制造空白

- evidence_pointer：Introduction P5

### 16. Introduction P6 S1

- order：16

- section：Introduction

- locator：Introduction P6 S1

- move_code：LIMITATION

- paraphrase_cn：另外一些模型用GCN利用外部知识结构关系，但知识选择常被忽视或采用临时方法，无法捕捉人类从长期记忆中检索知识的方式。

- rhetorical_function_cn：指出第二类方法的缺陷：缺乏知识选择

- depends_on_cn：延续对知识感知模型分类的讨论

- sets_up_cn：为激活机制提供问题空间

- evidence_pointer：Introduction P6

### 17. Introduction P7 S1

- order：17

- section：Introduction

- locator：Introduction P7 S1

- move_code：GAP

- paraphrase_cn：上述讨论表明研究缺口：现有知识感知模型使用知识嵌入或图，但知识往往与多种语义混淆且不针对学习任务。

- rhetorical_function_cn：综合两个缺陷，正式宣告研究缺口

- depends_on_cn：依赖前面对两类模型的批评

- sets_up_cn：为三个研究问题提供直接依据

- evidence_pointer：Introduction P7

### 18. Introduction P7 S2

- order：18

- section：Introduction

- locator：Introduction P7 S2

- move_code：WHY_GAP_MATTERS

- paraphrase_cn：人类完成特定任务时只会从长期记忆中提取相关部分，而现有模型没有做到这一点。

- rhetorical_function_cn：说明缺口的理论后果：偏离人类认知

- depends_on_cn：架构在‘相关知识检索’的常识上

- sets_up_cn：把缺口提升为认知合理性问题

- evidence_pointer：Introduction P7

### 19. Introduction P7 S3

- order：19

- section：Introduction

- locator：Introduction P7 S3

- move_code：RQ_OR_OBJECTIVE

- paraphrase_cn：三个研究问题：能否设计认知理论引导的知识感知框架、不依赖LLM能否满意性能、能否提升学习效率。

- rhetorical_function_cn：用RQ形式精确划定研究任务

- depends_on_cn：前面缺口和知识差异论证

- sets_up_cn：为后文实验和回答提供清单

- evidence_pointer：Introduction P7

### 20. Introduction P8 S1

- order：20

- section：Introduction

- locator：Introduction P8 S1

- move_code：STUDY_OVERVIEW

- paraphrase_cn：采用DSR和Schema Theory构建框架，实验结果以仅7.6%的LLM参数、10%的训练数据、近3倍更快的训练速度达到可比性能。

- rhetorical_function_cn：预告方法与核心数字，增强可读性

- depends_on_cn：三个RQ的提出

- sets_up_cn：把读者注意力引向后续设计细节

- evidence_pointer：Introduction P8

### 21. Introduction P8 S2

- order：21

- section：Introduction

- locator：Introduction P8 S2

- move_code：CONTRIBUTION

- paraphrase_cn：框架同时改善有效性、效率和稳健性，推动AI接近人类学习，并贡献给知识感知AI研究。

- rhetorical_function_cn：在引言末尾完成贡献预告

- depends_on_cn：摘要和前面实验预告

- sets_up_cn：为讨论部分详细展开学科意义铺设框架

- evidence_pointer：Introduction P8

### 22. Research Background P1 S1

- order：22

- section：Research Background

- locator：Research Background P1 S1

- move_code：TRANSITION

- paraphrase_cn：本节将已有研究按是否显式整合外部知识分为LLM和知识感知模型两类进行综述。

- rhetorical_function_cn：提供文献综述的分类路线图

- depends_on_cn：引言聚焦知识感知模型

- sets_up_cn：后续两小节分别批评两类方法

- evidence_pointer：Research Background

### 23. Pre-trained LLMs P1 S1

- order：23

- section：Pre-trained LLMs: Encoding Knowledge Implicitly

- locator：Pre-trained LLMs P1 S1

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：LLM通过在大规模文本上预训练，将知识隐式编码在亿级参数中。

- rhetorical_function_cn：描述LLM的知识处理方式

- depends_on_cn：前一小节分类

- sets_up_cn：为批评隐式知识黑箱作铺垫

- evidence_pointer：Pre-trained LLMs P1

### 24. Pre-trained LLMs P2 S1

- order：24

- section：Pre-trained LLMs: Encoding Knowledge Implicitly

- locator：Pre-trained LLMs P2 S1

- move_code：LIMITATION

- paraphrase_cn：LLM需要大量训练数据、计算成本高，知识以隐式非符号形式存在，导致黑箱且不符合以人为中心的目标，因此仅将其作为benchmark。

- rhetorical_function_cn：把LLM限定为评价基准而非设计组件

- depends_on_cn：对LLM知识编码方式的描述

- sets_up_cn：确立实验中的对照逻辑

- evidence_pointer：Pre-trained LLMs P2

### 25. Knowledge-Aware Models P1 S1

- order：25

- section：Knowledge-Aware Models: Incorporating Explicit External Knowledge

- locator：Knowledge-Aware Models P1 S1

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：人类知识通常是符号化和显式的，知识图以三元组形式组织概念与关系，类似人类存储知识。

- rhetorical_function_cn：为知识图引入认知对应物

- depends_on_cn：前面对隐式知识的批评

- sets_up_cn：解释为何知识图是显式知识载体

- evidence_pointer：Knowledge-Aware Models P1

### 26. Knowledge-Aware Models P2 S1

- order：26

- section：Knowledge-Aware Models: Incorporating Explicit External Knowledge

- locator：Knowledge-Aware Models P2 S1

- move_code：PHENOMENON

- paraphrase_cn：举例：判断“Tim Cook发布新产品”是否属于科技新闻，人类会调用长期记忆中的(Tim Cook, CEO of, Apple)和(Apple, IsA, Technology Company)。

- rhetorical_function_cn：用简单例子展示外部知识为何必要

- depends_on_cn：知识图三元组概念

- sets_up_cn：为知识感知模型的价值提供直观依据

- evidence_pointer：Knowledge-Aware Models P2

### 27. Knowledge-Aware Models P3 S1

- order：27

- section：Knowledge-Aware Models: Incorporating Explicit External Knowledge

- locator：Knowledge-Aware Models P3 S1

- move_code：LIMITATION

- paraphrase_cn：第一类知识感知模型把知识作为附加词嵌入，静态向量引发一词多义，无法捕捉结构性关系。

- rhetorical_function_cn：在综述中同步批判方法，强化缺口

- depends_on_cn：现象例子说明知识重要

- sets_up_cn：为图式理论的结构化设计铺垫

- evidence_pointer：Knowledge-Aware Models P3

### 28. Knowledge-Aware Models P4 S1

- order：28

- section：Knowledge-Aware Models: Incorporating Explicit External Knowledge

- locator：Knowledge-Aware Models P4 S1

- move_code：LIMITATION

- paraphrase_cn：第二类GCN模型能建模结构关系，但忽略或临时性处理知识选择，外部知识保持通用而非针对任务。

- rhetorical_function_cn：继续补足第二类方法的缺口

- depends_on_cn：知识选择在人类学习中的重要性

- sets_up_cn：引出激活机制的设计需求

- evidence_pointer：Knowledge-Aware Models P4

### 29. Schema Theory P1 S1

- order：29

- section：Schema Theory

- locator：Schema Theory P1 S1

- move_code：THEORY_INTRO

- paraphrase_cn：图式理论提供理解人类学习的综合框架，认为学习围绕图式的创建与应用展开。

- rhetorical_function_cn：正式引入全文核心理论

- depends_on_cn：前面知识缺口需要理论来补足

- sets_up_cn：后文将定义图式与知识结构

- evidence_pointer：Schema Theory P1

### 30. Schema Theory P1 S2

- order：30

- section：Schema Theory

- locator：Schema Theory P1 S2

- move_code：THEORY_PROPOSITION

- paraphrase_cn：图式被定义为表示组成部分之间关系的知识结构，多个图式构成长期记忆中的背景知识。

- rhetorical_function_cn：给出精确的理论构念

- depends_on_cn：图式理论引入

- sets_up_cn：为“知识结构”与知识图谱的对应提供依据

- evidence_pointer：Schema Theory P1

### 31. Knowledge Acquisition and Representation P1 S1

- order：31

- section：Schema Theory: Knowledge Acquisition and Representation

- locator：Knowledge Acquisition and Representation P1 S1

- move_code：THEORY_PROPOSITION

- paraphrase_cn：知识并非天生，而是通过与世界互动，形成概念与关系并逐步补充到既有图式中。

- rhetorical_function_cn：解释人类知识获取的认知机制

- depends_on_cn：图式定义

- sets_up_cn：为元需求1大知识库和元需求2结构化表示提供依据

- evidence_pointer：Knowledge Acquisition and Representation P1

### 32. Knowledge Acquisition and Representation P2 S1

- order：32

- section：Schema Theory: Knowledge Acquisition and Representation

- locator：Knowledge Acquisition and Representation P2 S1

- move_code：MECHANISM

- paraphrase_cn：知识结构意味着知识不是孤立事实，而是决定知识何时适用的结构框架；零散知识无法独立存在。

- rhetorical_function_cn：强调结构性是知识表征的关键

- depends_on_cn：知识获取过程

- sets_up_cn：直接映射到将三元组组织成知识图谱

- evidence_pointer：Knowledge Acquisition and Representation P2

### 33. Knowledge Activation and Utilization P1 S1

- order：33

- section：Schema Theory: Knowledge Activation and Utilization

- locator：Knowledge Activation and Utilization P1 S1

- move_code：THEORY_PROPOSITION

- paraphrase_cn：长期记忆中只有部分知识适用于当前任务，任务中的刺激决定搜索方向并激活相关图式。

- rhetorical_function_cn：给出图式激活的操作定义

- depends_on_cn：知识表征完成后的问题

- sets_up_cn：为元需求3激活机制提供理论依据

- evidence_pointer：Knowledge Activation and Utilization P1

### 34. Knowledge Activation and Utilization P2 S1

- order：34

- section：Schema Theory: Knowledge Activation and Utilization

- locator：Knowledge Activation and Utilization P2 S1

- move_code：MECHANISM

- paraphrase_cn：最后一步是将激活的图式与任务信息整合，并赋予概念和命题不同价值，形成全局语义关联。

- rhetorical_function_cn：解释知识利用环节

- depends_on_cn：图式激活

- sets_up_cn：为bi-LSTM+GCN整合模型奠基

- evidence_pointer：Knowledge Activation and Utilization P2

### 35. Research Gaps and Our Work P1 S1

- order：35

- section：Research Gaps and Our Work

- locator：Research Gaps and Our Work P1 S1

- move_code：GAP

- paraphrase_cn：基于图式理论的审视发现，现有模型设计缺乏理论根基，不能以认知上可信的方式封装人类知识处理过程。

- rhetorical_function_cn：把之前所有批评上升为正式研究缺口

- depends_on_cn：综述两类模型与图式理论

- sets_up_cn：引入具体工作的必要性

- evidence_pointer：Research Gaps and Our Work P1

### 36. Research Gaps and Our Work P2 S1

- order：36

- section：Research Gaps and Our Work

- locator：Research Gaps and Our Work P2 S1

- move_code：LIMITATION

- paraphrase_cn：最接近的Wang等人模型缺乏结构关系、只检索IsA关系、知识选择不符合人类线索激活，根本问题是缺乏理论。

- rhetorical_function_cn：用最近似工作衬托本文设计的差异

- depends_on_cn：前面综述中已提及Wang等人

- sets_up_cn：让本文四个设计组件具备排他性

- evidence_pointer：Research Gaps and Our Work P2

### 37. Research Gaps and Our Work P3 S1

- order：37

- section：Research Gaps and Our Work

- locator：Research Gaps and Our Work P3 S1

- move_code：RQ_OR_OBJECTIVE

- paraphrase_cn：因此本文引入图式理论引导的知识感知学习框架，覆盖知识获取、表征、激活和利用全过程。

- rhetorical_function_cn：直接回填研究缺口并预告设计

- depends_on_cn：缺口的具体化

- sets_up_cn：为下一节详细设计做承接

- evidence_pointer：Research Gaps and Our Work P3

### 38. Framework P1 S1

- order：38

- section：Schema Theory Guided Knowledge-Aware Learning Framework

- locator：Framework P1 S1

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：采用信息系统设计理论（ISDT）来形式化设计过程，确保与设计科学一致并有效可行。

- rhetorical_function_cn：为设计方法提供合理性声明

- depends_on_cn：上一节的缺口需用设计科学解决

- sets_up_cn：引出四个ISDT组件

- evidence_pointer：Framework P1

### 39. Kernel Theory P1 S1

- order：39

- section：Kernel Theory

- locator：Kernel Theory P1 S1

- move_code：THEORY_PROPOSITION

- paraphrase_cn：内核理论是图式理论：人类学习是获取、表征、激活、利用知识的过程。

- rhetorical_function_cn：把理论压缩为设计可依据的四阶段

- depends_on_cn：ISDT框架组件

- sets_up_cn：表1的四条元需求由此而生

- evidence_pointer：Kernel Theory P1

### 40. Kernel Theory P2 S1

- order：40

- section：Kernel Theory

- locator：Kernel Theory P2 S1

- move_code：MECHANISM

- paraphrase_cn：某些词具有启发性质可激活图式，但单一刺激可能激活多个图式，需要额外线索才能确定最合适图式。

- rhetorical_function_cn：解释为何激活需要任务相关权重而非简单匹配

- depends_on_cn：图式激活理论

- sets_up_cn：为TF-IDF式上下文权重设计提供认知理由

- evidence_pointer：Kernel Theory P2

### 41. Metarequirements P1 S1

- order：41

- section：Metarequirements

- locator：Metarequirements P1 S1

- move_code：REQUIREMENT

- paraphrase_cn：四条元需求：大知识库、结构化图式、图式激活机制、整合模型。

- rhetorical_function_cn：将理论翻译成设计目标

- depends_on_cn：前面图式四过程

- sets_up_cn：表1的元需求列

- evidence_pointer：Metarequirements P1

### 42. Metadesign Complete Design P1 S1

- order：42

- section：Metadesign: Complete Design

- locator：Metadesign Complete Design P1 S1

- move_code：DESIGN_FEATURE

- paraphrase_cn：完整设计是：ConceptNet作知识库、知识三元组构成结构图式、边权重激活机制、bi-LSTM+GCN整合模型。

- rhetorical_function_cn：把四条元需求实例化为四个元设计组件

- depends_on_cn：元需求列表

- sets_up_cn：后四小节逐一详细解释组件

- evidence_pointer：Metadesign Complete Design, Figure 2

### 43. Metadesign Element 1 P1 S1

- order：43

- section：Metadesign Element 1

- locator：Metadesign Element 1 P1 S1

- move_code：DESIGN_FEATURE

- paraphrase_cn：选择ConceptNet是因为它整合多知识库、规模大、关系类型丰富，堪比人类长期记忆。

- rhetorical_function_cn：为知识库选型提供理由

- depends_on_cn：元需求1

- sets_up_cn：后续元素2用其三元组组织结构

- evidence_pointer：Metadesign Element 1

### 44. Metadesign Element 2 P1 S1

- order：44

- section：Metadesign Element 2

- locator：Metadesign Element 2 P1 S1

- move_code：DESIGN_FEATURE

- paraphrase_cn：将ConceptNet原始三元组转为以概念为节点、关系为边的知识结构，以模拟人类图式表征。

- rhetorical_function_cn：说明结构化表示的实现方式

- depends_on_cn：图式理论强调知识结构

- sets_up_cn：为图式激活提供可操作图对象

- evidence_pointer：Metadesign Element 2, Figure 1

### 45. Metadesign Element 3 P1 S1

- order：45

- section：Metadesign Element 3

- locator：Metadesign Element 3 P1 S1

- move_code：MECHANISM

- paraphrase_cn：未加权的图式把所有知识平等对待，无法激活像(Apple,IsA,Technology Company)这样的任务相关关系，因此需要权重。

- rhetorical_function_cn：构造问题：现有知识图缺少选择性

- depends_on_cn：图式激活理论

- sets_up_cn：引出TF-IDF启发式权重

- evidence_pointer：Metadesign Element 3, Figure 3

### 46. Metadesign Element 3 P2 S1

- order：46

- section：Metadesign Element 3

- locator：Metadesign Element 3 P2 S1

- move_code：DESIGN_FEATURE

- paraphrase_cn：受TF-IDF启发，权重等于概念对在任务语料中的频率除以在Wikipedia通用语料中的频率加一。

- rhetorical_function_cn：给出知识激活机制的具体公式和来源

- depends_on_cn：需要区分任务相关与通用知识

- sets_up_cn：随后示例说明如何激活技术公司关系

- evidence_pointer：Metadesign Element 3, Equation 1

### 47. Metadesign Element 3 P3 S1

- order：47

- section：Metadesign Element 3

- locator：Metadesign Element 3 P3 S1

- move_code：RESULT

- paraphrase_cn：示例中(Apple,Technology Company)权重0.12，而(Apple,Fruit)权重0.001，因此前者被激活。

- rhetorical_function_cn：用数字示例让激活机制直观可感

- depends_on_cn：权重公式

- sets_up_cn：说明权重确实能选择任务相关关系

- evidence_pointer：Metadesign Element 3

### 48. Metadesign Element 3 P4 S1

- order：48

- section：Metadesign Element 3

- locator：Metadesign Element 3 P4 S1

- move_code：MECHANISM

- paraphrase_cn：高权重的概念对捕捉目标领域相对于通用领域的独特特征，并与图式理论中激活任务相关图式一致。

- rhetorical_function_cn：将工程启发式重新绑定到认知理论

- depends_on_cn：公式与示例

- sets_up_cn：为公式的认知合理性辩护

- evidence_pointer：Metadesign Element 3

### 49. Metadesign Element 3 P5 S1

- order：49

- section：Metadesign Element 3

- locator：Metadesign Element 3 P5 S1

- move_code：DESIGN_FEATURE

- paraphrase_cn：实现上对给定文档做拓扑展开，检索一阶邻居关系，按权重取top K；不足时扩展到二阶。

- rhetorical_function_cn：将激活机制转化为可执行算法

- depends_on_cn：上下文知识图谱权重

- sets_up_cn：让实验可以固定K超参数

- evidence_pointer：Metadesign Element 3

### 50. Metadesign Element 4 P1 S1

- order：50

- section：Metadesign Element 4

- locator：Metadesign Element 4 P1 S1

- move_code：DESIGN_FEATURE

- paraphrase_cn：学习模型由文本表示和知识图表示双通道构成：bi-LSTM编码目标文本，GCN编码激活知识图。

- rhetorical_function_cn：把知识利用环节实例化为模型结构

- depends_on_cn：图式理论强调激活图式与任务信息整合

- sets_up_cn：后文用GCN/bi-LSTM超参数表支撑实验复现

- evidence_pointer：Metadesign Element 4, Table 2

### 51. Metadesign Element 4 P2 S1

- order：51

- section：Metadesign Element 4

- locator：Metadesign Element 4 P2 S1

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：选择TransE生成概念和关系嵌入，因为它简单、可解释、高效且具竞争力。

- rhetorical_function_cn：解释知识嵌入方法选型的工程理由

- depends_on_cn：需要将三元组向量化

- sets_up_cn：排除其他嵌入方法的比较必要性

- evidence_pointer：Metadesign Element 4

### 52. Design Summary P1 S1

- order：52

- section：Design Summary

- locator：Design Summary P1 S1

- move_code：STUDY_OVERVIEW

- paraphrase_cn：总结框架：ConceptNet表示知识获取，知识三元组结构化表示知识表征，权重激活表示知识激活，bi-LSTM+GCN表示知识利用；这是首次完整复刻人类知识处理过程的框架。

- rhetorical_function_cn：阶段性总结并声明设计新颖性

- depends_on_cn：四个元设计子节

- sets_up_cn：为下节可检验假设提供设计完整性

- evidence_pointer：Design Summary

### 53. Testable Hypotheses P1 S1

- order：53

- section：Testable Hypotheses

- locator：Testable Hypotheses P1 S1

- move_code：HYPOTHESIS_OR_PROPOSITION

- paraphrase_cn：提出H1-H4：完整设计有效性/效率、稳健性、组件有效性、知识类型关系。

- rhetorical_function_cn：把设计要求转化为可评价命题

- depends_on_cn：ISDT元设计

- sets_up_cn：为五个实验提供论证结构

- evidence_pointer：Table 1

### 54. Experiments intro P1 S1

- order：54

- section：Experiments and Results

- locator：Experiments intro P1 S1

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：选择文本分类和NLI两个任务，因为它们在商业决策中有应用潜力且已有充分基线和基准。

- rhetorical_function_cn：为评价情境的可行性辩护

- depends_on_cn：需要实例化设计

- sets_up_cn：引出表3基线选择

- evidence_pointer：Experiments intro

### 55. Experiment 1 P1 S1

- order：55

- section：Experiment 1

- locator：Experiment 1 P1 S1

- move_code：BENCHMARK_OR_CONTRAST

- paraphrase_cn：两个任务都纳入知识感知模型和先进预训练LLM作为baseline。

- rhetorical_function_cn：确立双重评价参照

- depends_on_cn：表3模型选型

- sets_up_cn：为表4的比较结果设定坐标系

- evidence_pointer：Table 3

### 56. Experiment 1 P2 S1

- order：56

- section：Experiment 1

- locator：Experiment 1 P2 S1

- move_code：RESULT

- paraphrase_cn：框架在所有任务上一致优于显式知识模型，例如MR F1从76.1%提升到84.4%；与LLM模型可比，仅在20-News上最优。

- rhetorical_function_cn：报告对照实验核心结果

- depends_on_cn：表4结果

- sets_up_cn：为证明不依赖LLM也可达到先进水平提供证据

- evidence_pointer：Table 4

### 57. Experiment 1 P2 S2

- order：57

- section：Experiment 1

- locator：Experiment 1 P2 S2

- move_code：RESULT

- paraphrase_cn：表5显示框架模型远小于BertGCN，训练时间更短，不需要昂贵的预训练或微调。

- rhetorical_function_cn：把性能可比性转化为效率优势

- depends_on_cn：表4性能结果

- sets_up_cn：为RQ3效率声明提供具体证据

- evidence_pointer：Table 5

### 58. Experiment 2 P1 S1

- order：58

- section：Experiment 2

- locator：Experiment 2 P1 S1

- move_code：STUDY_OVERVIEW

- paraphrase_cn：实验2将MR和NLI替换为ADE和PubMed，使测试床覆盖不同任务类型和领域，并将训练数据从100%逐步减到1%。

- rhetorical_function_cn：说明实验2的设计改变及其目的

- depends_on_cn：实验1只测全量数据

- sets_up_cn：为图5的学习曲线结果作准备

- evidence_pointer：Experiment 2, Figure 5

### 59. Experiment 2 P2 S1

- order：59

- section：Experiment 2

- locator：Experiment 2 P2 S1

- move_code：RESULT

- paraphrase_cn：R52从100%数据到10%数据时框架仅下降5.9%，而Text GCN和BertGCN分别下降18.3和33.2个百分点。

- rhetorical_function_cn：用单个任务数据展示框架的低数据优势

- depends_on_cn：图5结果

- sets_up_cn：为学习效率结论提供关键证据

- evidence_pointer：Figure 5

### 60. Experiment 2 P3 S1

- order：60

- section：Experiment 2

- locator：Experiment 2 P3 S1

- move_code：RESULT

- paraphrase_cn：在极低训练数据下Text GCN超过BertGCN，说明LLM微调依赖大量数据。

- rhetorical_function_cn：解释低数据下基线反转，强化框架优势

- depends_on_cn：图5观察

- sets_up_cn：暴露LLM数据密集性局限

- evidence_pointer：Experiment 2

### 61. Experiment 2 P4 S1

- order：61

- section：Experiment 2

- locator：Experiment 2 P4 S1

- move_code：RESULT

- paraphrase_cn：跨任务类型和领域都观察到一致的效率提升，说明框架具有泛化性。

- rhetorical_function_cn：把效率从单例推广到多个任务

- depends_on_cn：图5整体曲线

- sets_up_cn：为讨论中‘接近人类泛化学习’提供依据

- evidence_pointer：Figure 5

### 62. Experiment 3 intro P1 S1

- order：62

- section：Experiment 3

- locator：Experiment 3 intro P1 S1

- move_code：ROBUSTNESS_OR_BOUNDARY_TEST

- paraphrase_cn：由于外部知识库普遍存在错误和缺失，框架依赖知识库，因此有必要评估不完整和噪声知识下的稳健性。

- rhetorical_function_cn：说明稳健性实验的必要性

- depends_on_cn：实验1和2确认有效与高效

- sets_up_cn：为表6和表7的扰动实验提供理由

- evidence_pointer：Experiment 3

### 63. KG Incompleteness P1 S1

- order：63

- section：Resilience to Knowledge Graph Incompleteness

- locator：KG Incompleteness P1 S1

- move_code：RESULT

- paraphrase_cn：缺失10%知识时性能下降不显著；缺失50%仍保留超80%改进；缺失90%时保留约40%-51%但下降显著。

- rhetorical_function_cn：报告不完整性实验结果并给出边界

- depends_on_cn：表6数据

- sets_up_cn：支撑H2的同时明确极端缺失的边界

- evidence_pointer：Table 6

### 64. KG Noise P1 S1

- order：64

- section：Resilience to Noise in the Knowledge Graph

- locator：KG Noise P1 S1

- move_code：RESULT

- paraphrase_cn：1%和5%噪声下性能下降均微小且统计不显著，说明当前知识图谱数据质量足以支撑框架。

- rhetorical_function_cn：报告噪声实验结果并链接实践可用性

- depends_on_cn：表7数据

- sets_up_cn：增强框架鲁棒性和实际部署可信度

- evidence_pointer：Table 7

### 65. Experiment 4 P1 S1

- order：65

- section：Experiment 4

- locator：Experiment 4 P1 S1

- move_code：RESULT

- paraphrase_cn：消融实验显示GCN、bi-LSTM和知识激活机制三个组件被移除后性能均下降，例如20-News从89.6%降至87.5%或更低。

- rhetorical_function_cn：报告消融结果，支撑组件归因

- depends_on_cn：表8结果

- sets_up_cn：确保性能不是仅靠整体模型规模

- evidence_pointer：Table 8

### 66. Experiment 5 P1 S1

- order：66

- section：Experiment 5

- locator：Experiment 5 P1 S1

- move_code：STUDY_OVERVIEW

- paraphrase_cn：实验5检验概念性、程序性和情境性知识在单独和组合时的作用。

- rhetorical_function_cn：预告实验5的机制考察目标

- depends_on_cn：认知科学知识分类

- sets_up_cn：为表9的知识类型结果作准备

- evidence_pointer：Experiment 5

### 67. Experiment 5 P2 S1

- order：67

- section：Experiment 5

- locator：Experiment 5 P2 S1

- move_code：RESULT

- paraphrase_cn：概念性知识贡献大于程序性知识，情境性知识单独使用在医学任务中贡献突出，三类知识的组合改进超过单独改进之和。

- rhetorical_function_cn：报告知识类型与协同效应的核心发现

- depends_on_cn：表9结果

- sets_up_cn：为认知科学讨论提供计算证据

- evidence_pointer：Table 9

### 68. Discussions P1 S1

- order：68

- section：Discussions

- locator：Discussions P1 S1

- move_code：CONTRIBUTION

- paraphrase_cn：研究通过DSR和Schema Theory回答了RQ1-RQ3，框架与人类知识处理过程对齐且无需LLM。

- rhetorical_function_cn：开头即闭合引言RQ清单

- depends_on_cn：全部实验结果

- sets_up_cn：随后分学科展开贡献讨论

- evidence_pointer：Discussions P1

### 69. Implications for Cognitive Science P1 S1

- order：69

- section：Implications for Cognitive Science

- locator：Implications for Cognitive Science P1 S1

- move_code：THEORY_RETURN

- paraphrase_cn：计算证据显示情境性知识在需要时控制任务相关知识激活，支持概念性知识先于程序性知识的观点并揭示两者协同。

- rhetorical_function_cn：把实验结果返回并推进认知科学理论

- depends_on_cn：实验5表9结果

- sets_up_cn：为设计科学和实践意义提供理论高度

- evidence_pointer：Implications for Cognitive Science, Figure 6

### 70. Implications for Design Science P1 S1

- order：70

- section：Implications for Design Science and Technical IS Research

- locator：Implications for Design Science P1 S1

- move_code：CONTRIBUTION

- paraphrase_cn：研究以学习层级的新颖性回应Samtani等人的呼吁，通过上下文知识图谱实现认知合理知识激活机制，展现出将抽象认知理论转化为学习模型的设计创新。

- rhetorical_function_cn：把贡献嵌入IS深度学习研究议程

- depends_on_cn：设计组件与稳健结果

- sets_up_cn：为实践影响和局限提供IS学科视角

- evidence_pointer：Implications for Design Science

### 71. Implications for Practice P1 S1

- order：71

- section：Implications for Practice

- locator：Implications for Practice P1 S1

- move_code：BOUNDARY_CONDITION

- paraphrase_cn：框架在少数据下仍能保持高准确率，适合数据受限场景，且其通用性可超越文本分类和NLI。

- rhetorical_function_cn：界定实践适用边界的正向表述

- depends_on_cn：实验2低数据结果和实验1任务多样性

- sets_up_cn：引出实践领域扩展建议

- evidence_pointer：Implications for Practice

### 72. Limitations P1 S1

- order：72

- section：Limitations

- locator：Limitations P1 S1

- move_code：LIMITATION_AND_FUTURE

- paraphrase_cn：研究依赖外部知识库质量，知识库可能不完善且随时间变化，未来可改进知识库质量和采用动态知识库。

- rhetorical_function_cn：诚实地限定贡献边界并指明后续方向

- depends_on_cn：实验对ConceptNet的依赖

- sets_up_cn：为结论提供审慎收束

- evidence_pointer：Limitations

## 写作技术

- gap_construction_cn：先建立人类与AI的性能与知识不对称，再把现有AI按知识处理方式分成隐式LLM和显式知识感知两类，分别以‘静态向量导致多义词’和‘知识选择缺失/临时化’批评它们，最后用图式理论把这些缺点重新定义为‘不具认知合理性’，从而形成理论缺口而非普通技术缺口。

- signposting_cn：引言用三个RQ定向；文献综述开头说明分类方式；框架部分用ISDT四组件和Table 1给出路线图；设计各小节以‘元需求—元设计’重复路标；实验部分在每段开头声明要回答的假设；讨论开头直接回应RQ。

- transition_logic_cn：每类文献评述都以缺陷收尾，下一节立即给出‘然而，图式理论显示…’的结构；元需求从理论四过程逐条翻译；每个实验的最后一句话往往点出下一个不确定问题，自然引出下一实验。

- claim_evidence_rhythm_cn：大主张被拆为多个可检验假设，每个假设对应一个实验；每个实验先说明问题、再展示表/图、然后以‘关键洞见’总结；语言上使用‘可比’而非‘超越’来保持精确，用‘our design consistently outperformed’修饰显式知识基线，用‘comparable’修饰LLM对比。

- benchmark_narrative_cn：LLM被先批评为黑箱和低效，再被用作基准；这种‘批判性认可’让基准对照既体现严谨性又不损害框架定位。知识感知基线Text GCN和KIM被选为同类对照，使实验能回答‘即使不用LLM，也比同类显式知识方法好’的问题。

- theory_return_cn：实验5的知识类型结果直接返回图式理论和认知科学的争论：情境性知识激活相关图式、概念性知识是程序性知识的基础、知识间存在协同而非独立；讨论中的Figure 6把四种理论观点与实证结果对接，使结果不只停留在准确率。

- contribution_positioning_cn：贡献被定位为‘首次将图式理论完整用于知识感知框架设计’，通过DSR/ISDT与IS社区对话，并通过Samtani等人的深度学习议程强调技术IS相关性，避免仅被视作NLP技巧。

- novelty_protection_cn：作者用多实验链保护贡献：有效性证明可达先进水平，效率证明不是靠算力，稳健性证明不是依赖完美知识库，消融证明不是整体模型幻觉，知识类型实验证明机制不只是一次性性能提升。同时在报告中使用‘可比’而非‘全面超越’，并给出明确的边界和局限，防止贡献被简化为单一benchmark结果。

## 可复用研究与写作程序

### structure_steps

#### 1. 1

- step：1

- writing_job_cn：用高张力现象（人类单样本学习 vs AI大规模数据）建立现实问题，并把差距归于知识层面

- research_job_cn：界定研究对象为知识感知模型，概述LLM和知识感知两类现有方案

- required_evidence_cn：需要有说服力的现象数据或业界引用，以及一组代表性的现有知识处理模型

- transition_to_next_cn：指出两类现有方案各自的本质缺陷，使其共同指向‘缺乏认知理论’的空白

#### 2. 2

- step：2

- writing_job_cn：引入一个可提供过程级解释的认知理论，拆解为知识获取、表征、激活、利用四个阶段

- research_job_cn：从该理论推导出四条对应元需求

- required_evidence_cn：理论构念需可操作化为数据、结构和算法组件

- transition_to_next_cn：用ISDT表把元需求映射到元设计组件

#### 3. 3

- step：3

- writing_job_cn：逐一描述元设计组件，每个组件都回指元需求，并给出实现细节

- research_job_cn：构建可用系统，确定知识库、图谱构建、激活规则、学习模型和超参数

- required_evidence_cn：需要有一个实际可运行的实现和超参数表，供后续实验复现

- transition_to_next_cn：从设计组件转化为H1-H4可检验假设

#### 4. 4

- step：4

- writing_job_cn：把评价拆成若干可检验假设，覆盖有效、高效、稳健、组件、机制

- research_job_cn：规划多实验序列，并选择合适的任务、基线、指标和扰动方式

- required_evidence_cn：需要标准数据集和至少两类基线：同类旧制品与当前强基线

- transition_to_next_cn：先做有效性，再做后续边界探索

#### 5. 5

- step：5

- writing_job_cn：按假设顺序组织实验：有效性→效率→稳健→消融→机制

- research_job_cn：执行对照、数据缩减、知识扰动、隔离组件、知识类型组合，并记录F1与资源数据

- required_evidence_cn：每一实验都需给出表/图和解释性数字，并明确统计或边界意义

- transition_to_next_cn：把所有实验结果汇总，回到最初的理论缺口

#### 6. 6

- step：6

- writing_job_cn：在讨论中逐一回答RQ，并把结果提升为对理论、设计方法和实践的含义

- research_job_cn：把机制实验结果与认知理论对接，并诚实地列出局限

- required_evidence_cn：需要有可回指的理论观点（如知识类型争论）和清晰的边界条件

- transition_to_next_cn：结论处重申贡献并保持审慎

### most_transferable_moves_cn

1. 用‘人类长期记忆—图式—知识三元组’的类比把认知理论落实为系统组件

2. 用ISDT表把理论命题翻译成元需求、元设计和可检验假设

3. 在benchmark中同时放入旧知识感知模型与当前LLM，形成双重参照

4. 先用完整数据验证有效，再用数据缩减证明效率，避免效率和有效性混谈

5. 用消融实验把整体性能归因到各设计组件

6. 用知识类型组合实验使性能结果反哺认知理论

### resource_intensive_or_nonstandard_parts_cn

1. 需要大型知识库ConceptNet和Wikipedia dump做背景频率统计

2. 需要较强GPU、较长CPU时间（Wikipedia处理4.5小时）

3. 需要运行多个LLM基线（BertGCN、MTL、EFL、DeBERTa）并进行资源对照

4. Online Supplemental Appendices中的知识分组和额外实验结果未在正文中完全展开

5. 图5的可视化细节依赖OCR，部分无法从文本完全还原

### what_not_to_copy_superficially_cn

1. 不要在没有理论映射的情况下声称‘图式理论引导’，否则ISDT表格会成为空壳

2. 不要在没有运行先进LLM基线的情况下声称‘与LLM可比’

3. 不要在没有消融的情况下把整体性能归因于某个组件

4. 不要在没有知识扰动实验的情况下宣称‘稳健’

5. 不要在没有知识类型证据的情况下讨论认知科学含义

- single_best_description_of_the_routine_cn：用一个认知理论把人类知识处理拆成四阶段，再通过ISDT把四阶段翻译成四个系统组件，最后用从有效性到效率、稳健、消融和知识机制的实验序列把性能提升升华为设计知识。

## 分析边界

分析基于全文文本，但部分实现细节和实验数据在Online Supplemental Appendices 1-3中，当前未读取；图片中Figure 5和部分表格的具体数值只能依赖文本转述，无法完全OCR还原；无法获得真实页码，只能使用章节、段落、表/图序号作为位置证据。
