# TheoryOn: A Design Framework and System for Unlocking Behavioral Knowledge Through Ontology Learning

- 作者：Jingjing Li; Kai Larsen; Ahmed Abbasi
- 年份 / 期刊：2020 / MIS Quarterly
- DOI：10.25300/misq/2020/15323
- 源文件：12584_2020_theoryon-a-design-framework-and-system-for-unlocking-behavioral-knowledge-through-ontology-learn.md
- 论文主类型：build_evaluate_design_science
- 主导写作弧线：requirements_build_evaluate_design_principles
- 置信度：0.92

## 文章级论证概况

- 核心问题：如何设计并实现一个能从大规模行为研究文献中自动抽取行为知识（假设、构念、理论关系、同义关系）的IT制品，从而缓解行为研究中的“知识不可及”问题，并提升学者在信息检索处理阶段的准确性与效率？

- 制品与设计：论文提出两个设计制品：BOLT行为本体学习设计框架和TheoryOn搜索引擎。BOLT将行为知识定义为假设（terms）、构念（concepts）、理论关系（non-taxonomic relations）、同义关系（taxonomic relations）四个本体学习层蛋糕输出，并规定四项任务：假设抽取、变量抽取、理论关系抽取、同义关系识别。TheoryOn按照BOLT实现，假设抽取采用规则与深度学习混合分类器，变量与关系抽取采用DLMTCK（深度学习增强的多阶段树复合核SVM），并以定制LSA加Lucene关键词实现构念检索、构念对检索、前因后果检索和理论整合可视化。

- 客观结果：方法比较中，假设抽取F1为95.25%，变量抽取F1为76.61%，关系抽取F1为84.54%，均优于各类baseline；系统比较中，TheoryOn变量抽取F1为70.84%，关系抽取F1为69.17%，高于CRCTOL、OntoGain、Text-To-Onto、TextStorm等通用本体学习系统；随机用户实验中，TheoryOn在四项信息检索任务的F-measure比EBSCOhost和Google Scholar高37%至121%，可减少最高158%的假阴性；适用性检查得到学者正面定性支持。

- 核心贡献：作者声称的贡献有三：提出BOLT设计框架以指导行为知识抽取系统开发；将框架实例化为TheoryOn，并嵌入深度学习与复合核SVM；通过数据挖掘实验、随机用户实验和适用性检查积累关于NLP、数据-理论-ML交叉设计、信息检索行为与知识不可及的实证和定性知识。

- 整篇论证链：作者从行为研究文献急剧膨胀但研究者只能检索到极少有价值文章的现象出发，提出“知识不可及”问题并说明其四方面危害；随后用信息检索三阶段模型把问题定位到processing phase，指出现有全文搜索引擎只支持searching阶段，因缺乏行为知识抽取而产生假阳性和放大确认偏误。基于Weber/Bunge的本体论文、Baron和Kenny的关系分类、Larsen和Bong的构念相似性以及Buitelaar的本体学习层蛋糕，作者推出BOLT框架，将行为文献中的知识转化为可计算的四类本体输出，并给出每类任务的混合技术处方。按照BOLT实现TheoryOn后，作者通过方法比较、系统比较、随机用户实验和适用性检查逐层验证框架处方、系统抽取能力、用户信息检索结果和实际可用性；讨论部分将结果升华为概念中心视角、复杂NLP方法以及数据-理论-ML制品需要整体评价的设计知识，并回到引言中的知识不可及问题，说明其对减少重复研究、建立累积传统、提升研究敏捷和产生社会效益的意义。

## 类型与写作弧线判定

- 论文主类型判定：论文以设计科学研究为主：提出BOLT设计框架（kernel theories、meta-requirements、meta-design、testable hypotheses），实例化为TheoryOn，然后通过方法比较、系统比较、随机用户实验和适用性检查进行多层面评价，最终输出设计知识和可复用原则。虽然包含随机实验，但整个论证结构是“要求—构建—评价—设计原则”，而非单纯的理论推导制品实验。

- 主导写作弧线判定：正文严格按照设计理论四件套组织：从知识不可及问题提出meta-requirements，再给出BOLT的meta-design，随后构建TheoryOn实例，最后用四类评价检验测试假设并提炼设计原则。作者在Discussion中直接按BOLT框架、TheoryOn系统、多元评价、通用性四层汇报设计知识，符合requirements—build—evaluate—design principles路径。

## 研究开展程序

- study_or_phase_count：6

- 研究阶段总序列：研究分为六个相互累积的阶段：第一阶段用行为/本体理论形成BOLT设计框架；第二阶段按框架构建TheoryOn；第三阶段在孤立任务上比较理论处方规定的抽取技术与baseline；第四阶段在完整系统管线上与通用本体学习系统比较；第五阶段用随机用户实验比较TheoryOn与传统全文搜索引擎的信息检索结果和感知效用；第六阶段用适用性检查获得学者定性反馈和场景边界。前两阶段建立制品，后四阶段形成“算法性能→系统管线→用户结果→领域适用性”的证据链。

### studies_or_phases

#### 1. BOLT设计框架构建

- order：1

- name_cn：BOLT设计框架构建

- question_cn：行为知识应该如何界定？支持行为知识抽取的系统应具备什么能力？需要哪些任务和技术？

- inputs_and_setting_cn：输入为多个行为研究与本体学习知识源：Weber的理论本体论、Baron和Kenny的调节/中介关系、Larsen和Bong的构念相似性、Buitelaar等人本体学习层蛋糕，以及设计科学中Walls et al.的框架结构。

- designed_or_compared_object_cn：设计对象是BOLT设计框架，包括kernel theories、meta-requirements、meta-design和testable hypotheses，具体推出假设抽取、变量抽取、理论关系抽取、同义关系识别四项任务。

- baseline_control_or_counterfactual_cn：没有形式化baseline；对照是现有全文搜索引擎、元数据型学术系统、生物医学文本挖掘方法均不能支持processing阶段。

##### objective_metrics

（空）

- analysis_method_cn：概念综合与理论推导，将本体学习层蛋糕映射到行为知识，并识别最佳支持技术类别。

- main_result_cn：行为知识被形式化为四类有序本体输出；meta-design给出四类任务，并以语言学和统计/ML两类技术作为支持。

- argumentative_role_cn：奠定全篇的设计理论基础，把“知识不可及”转化为可计算的抽取问题。

- remaining_uncertainty_cn：框架中的技术处方尚未经过经验检验，也未实例化。

- link_to_next_phase_cn：需要构建一个遵循BOLT的系统来验证框架的可行性，从而进入TheoryOn实例化阶段。

##### evidence_pointers

1. Design Framework for Disembedding Behavioral Knowledge

2. Figure 1. BOLT Framework

#### 2. TheoryOn系统实例化

- order：2

- name_cn：TheoryOn系统实例化

- question_cn：BOLT框架能否被实例化为一个可运行的行为知识搜索系统？

- inputs_and_setting_cn：输入是行为研究文章中的假设文本，以及规则模板、word2vec、深度学习模型、SVM树核、语义词典等NLP/ML资源；开发过程中使用后续标注数据的一部分进行模型设计。

- designed_or_compared_object_cn：设计对象是TheoryOn系统，包含混合假设分类器、DLMTCK变量/关系抽取器、理论网络构建、基于LSA+Lucene的搜索与可视化界面。

- baseline_control_or_counterfactual_cn：此时没有正式对照；系统实现严格遵循BOLT以保持instantiation validity。

##### objective_metrics

（空）

- analysis_method_cn：系统架构与算法设计；将调节/中介的三元关系分解为二元关系再组装。

- main_result_cn：实现了四类功能：构念搜索、构念对搜索、前因后果搜索、理论整合。

- argumentative_role_cn：作为设计框架的proof-of-concept实例，使BOLT的抽象处方变成可评价的具体系统。

- remaining_uncertainty_cn：系统抽取质量未知，用户价值未知，需要系统化评价。

- link_to_next_phase_cn：先用方法比较和系统比较检验抽取能力，再用随机用户实验和适用性检查检验用户价值。

##### evidence_pointers

1. TheoryOn: An Instantiation of the Proposed Design Framework

2. Figure 2. TheoryOn System Diagram

#### 3. 方法比较实验

- order：3

- name_cn：方法比较实验

- question_cn：BOLT规定的假设、变量、关系抽取技术是否优于替代技术？

- inputs_and_setting_cn：286篇期刊文章（MIS Quarterly 69篇、Information Systems Research 72篇、Journal of Applied Psychology 145篇，1980–2009），两位资深标注者标注，Cohen's kappa分别为0.98、0.75、0.82；最终1,913条假设、6,020个变量实例、3,135条关系；训练/开发/测试集60/20/20。

- designed_or_compared_object_cn：比较对象为各抽取任务的方法：假设抽取中混合分类器 vs 规则、最大熵、CNN、LSTM、BiLSTM-CNN；变量抽取中DLMTCK vs CRF、HMM、BiLSTM+CRF、CharCNN+BiLSTM+CRF、DRM、C/NC、npTFIDF、BPLex；关系抽取中DLMTCK vs 线性SVM、动词规则、关联规则、LexSynPatt。

- baseline_control_or_counterfactual_cn：以现有SOTA深度学习方法、经典序列标注方法和通用本体学习方法为baseline。

##### objective_metrics

1. Precision

2. Recall

3. F1-measure

- analysis_method_cn：在固定训练/开发/测试划分上比较分类和序列标注性能。

- main_result_cn：混合假设分类器F1=95.25%，DLMTCK变量抽取F1=76.61%，关系抽取F1=84.54%，均优于比较方法。

- argumentative_role_cn：验证BOLT meta-design中技术处方的有效性，支持“框架规定的技术确实适合行为知识抽取”。

- remaining_uncertainty_cn：孤立任务表现好不等同于完整管线好，也不等同用户检索结果好。

- link_to_next_phase_cn：需要系统比较来检验完整管线中的误差传播和端到端性能。

##### evidence_pointers

1. Evaluation: Experiments to Examine Behavioral Knowledge Extraction Performance

2. Table 1. Method Comparison Results

#### 4. 系统比较实验

- order：4

- name_cn：系统比较实验

- question_cn：TheoryOn作为遵循BOLT的完整管线，是否优于现有文本本体学习系统？

- inputs_and_setting_cn：使用与阶段三相同的标注数据，但评价对象是完整抽取管线；基线系统包括CRCTOL、OntoGain、Text-To-Onto、TextStorm；因通用系统无假设抽取，所有系统从已抽取假设出发比较变量和关系抽取。

- designed_or_compared_object_cn：比较TheoryOn与四个通用文本本体学习系统的变量/关系抽取管线性能。

- baseline_control_or_counterfactual_cn：按Park et al.评价标准筛选可比较的通用本体学习系统。

##### objective_metrics

1. Precision

2. Recall

3. F1-measure

- analysis_method_cn：端到端管线评价，观察阶段间误差传播效应。

- main_result_cn：TheoryOn变量抽取F1=70.84%，关系抽取F1=69.17%，显著高于四个通用系统；但整体低于孤立方法结果，说明存在误差传播。

- argumentative_role_cn：证明通用本体学习系统无法胜任行为知识抽取，BOLT指导的实例化是必要的。

- remaining_uncertainty_cn：抽取能力好仍不能说明用户搜索任务变好；需要用户级实验。

- link_to_next_phase_cn：转入随机用户实验，评估TheoryOn对信息检索结果和感知效用的影响。

##### evidence_pointers

1. System Comparison Experiments and Results

2. Table 2. System Comparison Results

#### 5. 随机用户实验

- order：5

- name_cn：随机用户实验

- question_cn：相比EBSCOhost和Google Scholar，TheoryOn是否能在行为研究者的信息检索任务中带来更好的客观性能和感知效用？

- inputs_and_setting_cn：52名全球IS与组织行为学博士生随机分配到TheoryOn、EBSCOhost、Google Scholar三组；面向TAM设计四项任务：同义构念搜索、构念对搜索、前因/后果搜索、理论整合；gold standard由资深教师、博士生和研究助理团队构建；三组均在相同期刊和年份范围（1990–2009）内搜索。

- designed_or_compared_object_cn：比较对象是TheoryOn与两个全文搜索引擎的系统界面、检索能力和可视化。

- baseline_control_or_counterfactual_cn：EBSCOhost和Google Scholar为baseline；TAM刻意选择高认知度理论以给全文搜索引擎最好的发挥条件。

##### objective_metrics

1. Precision

2. Recall

3. F1-measure

4. Perceived usefulness

5. Perceived ease of use

6. Behavioral intention

- analysis_method_cn：随机化检查（ANOVA）、组间t检验比较客观绩效与感知用量表。

- main_result_cn：TheoryOn在所有任务的F-measure比baseline高37%至121%；假阴性最多减少158%；感知有用性和易用性显著更高，行为意向边际显著。

- argumentative_role_cn：将系统抽取能力转化为用户在真实检索任务中的信息检索绩效，证明TheoryOn能缓解知识不可及。

- remaining_uncertainty_cn：任务是人工设定的TAM场景，用户不能自由切换工具，系统当时不公开，无法判断真实长期工作流价值。

- link_to_next_phase_cn：需要适用性检查补充“何时、对谁、如何有用”的定性理解。

##### evidence_pointers

1. Evaluation: User Experiments to Examine Information-Seeking Outcomes

2. Table 3. Percentage Retrieval Performance by Task

3. Table 4. Perceived Usefulness Comparison

#### 6. 适用性检查

- order：6

- name_cn：适用性检查

- question_cn：行为研究学者在真实研究流程中认为TheoryOn是否重要、可访问、适合，并用于哪些步骤？

- inputs_and_setting_cn：10名助理/副教授/正教授通过学术listserv招募，平均17.4年学术经验；经历预调查、两轮名义小组技术（NGT）会议、视频/上手任务和后续调查。

- designed_or_compared_object_cn：评估TheoryOn的importance、accessibility、suitability；识别学者信息检索的14个步骤。

- baseline_control_or_counterfactual_cn：没有对照系统；方法是Rosemann和Vessey的applicability check。

##### objective_metrics

（空）

- analysis_method_cn：NGT定性方法，会议转录、编码、引语归纳。

- main_result_cn：学者确认三阶段信息检索流程，认为TheoryOn在processing阶段特别有价值，可补充Google Scholar等搜索工具；对新手、资深学者和评审均有潜在帮助。

- argumentative_role_cn：提供生态效度和定性支持，划定TheoryOn适用的边界条件。

- remaining_uncertainty_cn：样本小且自选，定性反馈不能证明因果，系统未修改迭代。

- link_to_next_phase_cn：连同前几阶段证据进入Discussion，将局部结果上升为设计知识。

##### evidence_pointers

1. Applicability Check

2. Applicability Check Step 4: Modified Nominal Group Technique Applicability Check

3. Table 5. Information-Seeking Behaviors

## 各部分修辞架构

### abstract_moves

1. CONTEXT: 学者信息检索包含searching、accessing、processing三阶段

2. GAP: 现有Google Scholar等支持前两阶段，但processing阶段造成知识不可及

3. RQ_OR_OBJECTIVE: 提出BOLT框架和TheoryOn系统

4. STUDY_OVERVIEW: 数据挖掘实验、随机用户实验、适用性检查

5. RESULT: 数据挖掘实验支持BOLT，用户实验显示F1提高37%–121%，适用性检查定性支持

6. CONTRIBUTION: 设计制品共同解决行为文献知识不可及问题

### introduction_moves

1. CONTEXT: 行为研究依赖理论，部分理论引用超过七万

2. PRACTICAL_STAKES: 文献规模已经大到研究者无法掌握，概念中心视角下检索完整性低

3. PHENOMENON: 知识不可及被定义，并列举四类负面影响

4. WHY_GAP_MATTERS: 会造成重复研究、阻碍累积传统、降低研究敏捷并产生社会成本

5. MECHANISM: 行为理论语言可塑，需要构念中心视角；信息检索分为三阶段

6. LIMITATION: 全文搜索引擎适合searching但不适合processing，假阳性和确认偏误严重

7. RQ_OR_OBJECTIVE: 提出BOLT与TheoryOn，并声明这是exaptation

### theory_and_knowledge_moves

1. THEORY_INTRO: 设计科学框架包含kernel theories、meta-requirements、meta-design、testable hypotheses

2. THEORY_PROPOSITION: 理论实例是Bunge式专门本体，核心是构念、关系、状态

3. THEORY_PROPOSITION: 行为知识对应本体学习层蛋糕中的terms/concepts/non-taxonomic/taxonomic relations

4. REQUIREMENT: 四项BOLT任务被确定为假设抽取、变量抽取、理论关系抽取、同义关系识别

5. DESIGN_FEATURE: 使用语言学加统计/ML两类技术，并强调深度学习的潜力

### artifact_design_moves

1. DESIGN_FEATURE: TheoryOn按BOLT实现混合假设分类器

2. DESIGN_FEATURE: DLMTCK将变量抽取与关系抽取耦合，使用深度学习和树复合核SVM

3. DESIGN_FEATURE: 三元调节/中介关系被分解为二元关系再组装

4. DESIGN_FEATURE: 理论网络用共享变量和最小编辑距离聚合

5. DESIGN_FEATURE: 搜索结合定制LSA和Lucene关键词检索，提供四种功能

### evaluation_moves

1. STUDY_OVERVIEW: 四个评价阶段被预告

2. METHOD_JUSTIFICATION: 使用跨学科期刊与高信度标注建立测试床

3. BENCHMARK_OR_CONTRAST: 方法比较覆盖规则、特征、深度学习和通用本体学习方法

4. BENCHMARK_OR_CONTRAST: 系统比较使用CRCTOL、OntoGain、Text-To-Onto、TextStorm

5. RESULT: 方法/系统比较均显示TheoryOn优势

6. BENCHMARK_OR_CONTRAST: 随机实验以EBSCOhost和Google Scholar为baseline

7. RESULT: 用户实验F1领先37%–121%，假阴性减少158%

8. METHOD_JUSTIFICATION: 适用性检查采用NGT和Rosemann/Vessey框架

### discussion_and_contribution_moves

1. CONTRIBUTION: BOLT框架证明概念中心视角可行

2. CONTRIBUTION: TheoryOn系统是有效的proof-of-concept

3. CONTRIBUTION: 智能文本分析可缓解知识不可及，应同时关注precision和recall

4. CONTRIBUTION: 提供BOLT系统可能、实用且有价值的第一手证据

5. BOUNDARY_CONDITION: 推广到概念中心视角、复杂NLP和多元评价

6. CONTRIBUTION: 三方面贡献总结，并给出未来自动化综述展望

## 理论/知识到设计的翻译

### 知识/理论基础

1. Weber/Bunge的理论实例作为专门本体

2. Baron和Kenny的主效应、调节、中介关系分类

3. Larsen和Bong的构念相似性/同义关系算法

4. Buitelaar等的本体学习层蛋糕与ontology learning from text文献

5. Wong等的语言学与统计/ML技术分类

6. NLP/深度学习方法：word2vec、CNN、Bi-LSTM、CRF、SVM、树核

7. Meho和Tibbo的信息检索三阶段模型

8. 确认偏误研究（Nickerson、White等）

- 理论—设计耦合：direct

- 耦合判定理由：知识基础不是事后解释，而是前瞻性地决定了框架与系统设计：行为理论的本体观直接转化为meta-requirements，Buitelaar层蛋糕直接映射出四项任务，NLP/ML技术直接规定TheoryOn的算法选择；随后通过testable hypotheses和四类评价直接检验这些设计选择。因此属于直接耦合。

- 理论到设计翻译链：行为研究采用构念中心视角 + 理论实例是专门本体 → 行为知识核心部分为假设、构念、理论关系、同义关系 → 对应本体学习层蛋糕中的terms/concepts/non-taxonomic/taxonomic relations → 形成四项BOLT任务 → 从NLP文献选择语言学+统计/ML混合技术 → TheoryOn实例具体采用规则+深度学习假设分类器、DLMTCK变量/关系抽取器、LSA+Lucene同义构念检索 → 方法/系统/用户/适用性四类评价检验各环节。

### mapping_table

#### 1. 1

- theory_or_knowledge_claim_cn：理论实例是专门本体，其核心部分是构念和关系（Weber/Bunge）

- mechanism_cn：行为文献中的知识以假设、变量和关系的形式嵌入句子中，需要被抽取出来

- design_requirement_cn：系统应能抽取假设、变量、理论关系和同义关系

- artifact_choice_cn：BOLT四项任务；TheoryOn按此顺序构建抽取管线

- evaluated_contrast_cn：方法比较中混合假设抽取、DLMTCK变量/关系抽取 vs 通用/替代方法

- objective_result_cn：假设抽取F1=95.25%，变量抽取F1=76.61%，关系抽取F1=84.54%

##### evidence_pointers

1. Kernel Theories

2. Meta-Requirements

3. Table 1

#### 2. 2

- theory_or_knowledge_claim_cn：理论关系分为主效应、调节、中介（Baron和Kenny）

- mechanism_cn：调节和中介涉及三元变量，关系抽取不能只处理二元主效应

- design_requirement_cn：关系抽取应能识别三类关系并支持三元结构

- artifact_choice_cn：DLMTCK将三元调节/中介分解为多个二元关系，用复合核SVM分类后组装

- evaluated_contrast_cn：关系抽取DLMTCK vs 线性SVM、动词规则、关联规则、LexSynPatt

- objective_result_cn：关系抽取F1=84.54%，优于线性SVM的80.73%

##### evidence_pointers

1. Theoretical Relationship Extraction

2. TheoryOn Stage 2

3. Table 1

#### 3. 3

- theory_or_knowledge_claim_cn：同义构念可通过语义词典和潜在语义分析识别（Larsen和Bong）

- mechanism_cn：不同文章用不同名称表达同一构念，导致关键词检索漏检

- design_requirement_cn：搜索应能返回同义构念所在文章

- artifact_choice_cn：TheoryOn使用定制LSA + Lucene关键词搜索，支持同义构念检索

- evaluated_contrast_cn：随机用户实验中同义构念搜索任务 vs EBSCOhost/Google Scholar

- objective_result_cn：同义构念搜索F1=40.1%，高于EBSCOhost的26.4%和Google Scholar的28.5%

##### evidence_pointers

1. Synonymous Relationship Identification

2. TheoryOn Search and Visualization

3. Table 3

#### 4. 4

- theory_or_knowledge_claim_cn：本体学习层蛋糕输出是有序的，terms/relations逐层依赖（Buitelaar等）

- mechanism_cn：抽取变量依赖假设，关系依赖变量，错误会沿管线传播

- design_requirement_cn：系统应按层依次处理，并对误差传播有所认识

- artifact_choice_cn：TheoryOn管线为假设抽取→变量抽取→关系抽取→理论网络构建

- evaluated_contrast_cn：系统比较中TheoryOn完整管线 vs CRCTOL/OntoGain/Text-To-Onto/TextStorm

- objective_result_cn：变量抽取F1=70.84%，关系抽取F1=69.17%，高于通用系统；但低于孤立方法，显示误差传播

##### evidence_pointers

1. Meta-Requirements

2. System Comparison Experiments and Results

3. Table 2

#### 5. 5

- theory_or_knowledge_claim_cn：信息检索分为searching、accessing、processing三阶段，processing最需要跨文章综合（Meho和Tibbo）

- mechanism_cn：全文搜索引擎的关键词匹配和引用排序会导致假阳性和确认偏误

- design_requirement_cn：新系统应直接支持processing阶段的构念提取和关系可视化

- artifact_choice_cn：TheoryOn的构念搜索、构念对搜索、前因后果搜索和理论整合功能

- evaluated_contrast_cn：随机用户实验四项任务 vs EBSCOhost/Google Scholar

- objective_result_cn：所有任务F1比baseline高37%–121%，假阴性最多减少158%

##### evidence_pointers

1. Background: Limitations of Existing Search Engines

2. Randomized User Experiment

3. Table 3

#### 6. 6

- theory_or_knowledge_claim_cn：确认偏误会因关键词检索和流行度排序被放大（Nickerson、White等）

- mechanism_cn：搜索者倾向用已知构念名检索，漏掉同义不同名的文献

- design_requirement_cn：系统应减少假阴性，直接返回构念及理论关系而非仅含关键词的文档

- artifact_choice_cn：TheoryOn用抽取出的理论网络作为索引单元，按变量检索相关文章

- evaluated_contrast_cn：用户实验中理论整合和构念对搜索的召回表现

- objective_result_cn：TheoryOn回归/召回显著更高，理论整合F1=34.6%，远高于Google Scholar的15.6%

##### evidence_pointers

1. Introduction P4

2. Randomized User Experiment

3. Table 3

## 评价逻辑

### evaluation_modes

1. 数据挖掘方法比较实验

2. 数据挖掘系统比较实验

3. 随机用户实验

4. 适用性检查（NGT定性）

5. 系统使用统计（事后补充，非受控）

- why_these_evaluations_cn：BOLT提出两个可检验假设：一是抽取行为知识的能力，二是增强信息检索结果的能力。前者需要在受控数据上比较方法和系统；后者需要随机用户实验测量检索绩效和感知效用；适用性检查则回答何时、对谁、如何有价值。四个模式覆盖从算法到生态的完整证据链。

- benchmark_and_contrast_chain_cn：首先在孤立方法上对照SOTA深度学习和通用本体学习方法，证明框架处方有效；再与完整通用本体学习系统比较，证明端到端管线优于通用方案并暴露误差传播；随后将用户级baseline换为EBSCOhost和Google Scholar，证明在行为研究者实际检索任务中TheoryOn更优；最后通过适用性检查补充定性生态证据。该链条把“算法更好”逐步提升到“系统更好”和“用户检索更好”。

### claim_evidence_ledger

#### 1. BOLT规定的抽取技术优于替代技术

- claim_cn：BOLT规定的抽取技术优于替代技术

- evidence_cn：Table 1中假设、变量、关系抽取的F1全面领先

- verdict_cn：在孤立任务上有充分证据支持

#### 2. 遵循BOLT的完整系统优于通用本体学习系统

- claim_cn：遵循BOLT的完整系统优于通用本体学习系统

- evidence_cn：Table 2中TheoryOn变量/关系抽取F1高于CRCTOL等四个系统

- verdict_cn：有证据支持，但只比较了变量/关系抽取，未比较假设抽取

#### 3. TheoryOn能改善行为研究者信息检索结果

- claim_cn：TheoryOn能改善行为研究者信息检索结果

- evidence_cn：Table 3中四项任务F1均显著更高，假阴性减少158%

- verdict_cn：在受控TAM任务中有强支持；需注意任务为研究者人工设定

#### 4. 用户感知TheoryOn更有用且容易使用

- claim_cn：用户感知TheoryOn更有用且容易使用

- evidence_cn：Table 4中PU/EU显著更高，BI边际显著

- verdict_cn：大部分支持，BI不显著被归因于系统未公开

#### 5. TheoryOn在处理阶段对学者重要、可访问、适合

- claim_cn：TheoryOn在处理阶段对学者重要、可访问、适合

- evidence_cn：10名教授的适用性检查和NGT引语，确认processing阶段价值

- verdict_cn：定性支持，但样本小且自选，不能替代因果证据

- internal_validity_strategy_cn：随机分配用户并进行ANOVA人口统计检验；标注采用Cohen's kappa评估信度；金标准由经验团队独立构建；统一限定期刊与年份范围；对每个系统提供视频教程；选择高知名度TAM作为任务主题，被认为给全文搜索引擎创造有利条件；任务时长受限；适用性检查使用独立预调查、多轮NGT和转录编码。

- external_validity_strategy_cn：训练数据覆盖MISQ、ISR、JAP三个不同行为研究学科期刊；用户来自全球多个博士项目；适用性检查招募10名不同职称学者；作者在讨论中把结论推广到行为医学、心理学、教育、经济学等领域；还补充了TheoryOn上线后通过口碑获得的4000+用户、459个机构、125个国家等使用统计。

- what_is_not_actually_tested_cn：没有进行真实长期工作流中的随机对照试验；用户实验不允许自由切换或组合工具，无法识别TheoryOn在混合检索流程中的边际作用；未直接检验对理论整合质量的专家级深层判断；BOLT框架留待未来抽取theory state，因此行为知识的完整性未被完全测试；适用性检查反馈属于定性意见；系统使用统计缺乏对照组；用户实验中的搜索recall低于方法抽取recall，系统瓶颈仍未被完全建模。

## 贡献闭环

- technical_claim_cn：提出的混合假设分类器和DLMTCK在假设、变量、关系抽取上优于现有SOTA及传统本体学习方法；TheoryOn作为完整系统在变量/关系抽取上优于通用文本本体学习系统。

- artifact_claim_cn：BOLT框架的meta-design是抽取性能提升的原因；TheoryOn是该框架的成功实例化，证明了框架可行。

- mechanism_claim_cn：TheoryOn自动抽取并可视化假设、构念和关系，将研究者的认知带宽从人工提取释放到信息质量评估，从而减少假阳性和假阴性（即“带宽释放”机制）。

- boundary_claim_cn：适用对象是采用构念化、假设化语言的行为/社会科学文献；对刚进入新领域的新手研究者尤其有用，也可帮助资深研究者验证理解、更新领域知识和支持评审；应与Google Scholar等全文引擎互补使用而非替代。

- reusable_design_knowledge_cn：可复用的设计知识包括：采取概念中心视角；把行为知识映射到本体学习层蛋糕；以假设作为terms起点；采用语言学+统计/ML混合技术；用深度学习做变量抽取并用复合核SVM处理复杂关系；对数据-理论-ML交叉制品采用“方法—系统—用户—适用性”多层评价。

- theoretical_contribution_cn：将Bunge/Weber的本体理论、信息检索三阶段模型和本体学习连接起来，形式化定义了“行为知识不可及”问题；为信息检索processing阶段可由IT制品支持提供了理论和实证基础；扩展了IS领域NLP研究的问题类型，从简单分类推进到复杂行为知识抽取。

- how_discussion_closes_intro_gap_cn：Discussion中直接回到引言提出的四类危害：高召回高精度减少重复研究、错误gap spotting和边缘研究；支撑累积传统；提升研究话题敏捷性；扩展到多学科可能产生经济与社会效益。作者用用户实验中高F1、适用性检查中“Google Scholar给覆盖但TheoryOn给精度”等引语，逐一回应知识不可及的负面后果。

- overclaim_or_unsupported_leaps_cn：存在若干跳跃：将系统级抽取性能直接解释为用户recall降低的原因属于推测而非直接测量；以适用性检查的积极引语作为制品有效性证据较软；使用统计“4000+用户”无对照组，只能说明扩散不能证明效果；从抽取能力外推至“未来自动文献综述、自动meta-analysis”属于远景展望；用户实验任务集中于TAM，且传统全文搜索引擎未被设计成构念检索，因此比较可能放大效果。

## 句级写作动作图谱

### 1. P1 S1–S3

- order：1

- section：Abstract

- locator：P1 S1–S3

- move_code：CONTEXT

- paraphrase_cn：学者检索行为研究文献的过程分为搜索、获取和处理三阶段；谷歌学术等现有工具只解决了前两阶段，导致知识不可及问题。

- rhetorical_function_cn：在摘要开头用三阶段模型为全文设置核心问题框架。

- depends_on_cn：无

- sets_up_cn：引出后文对处理阶段不足的讨论和BOLT方案。

- evidence_pointer：Abstract P1

### 2. P1 S4

- order：2

- section：Abstract

- locator：P1 S4

- move_code：RQ_OR_OBJECTIVE

- paraphrase_cn：提出BOLT设计框架和TheoryOn搜索引擎，用于支持研究者处理行为知识。

- rhetorical_function_cn：明确文章的研究目标和两个设计制品。

- depends_on_cn：前面的知识不可及问题

- sets_up_cn：为摘要中的评价与贡献提供对象。

- evidence_pointer：Abstract P1

### 3. P1 S5

- order：3

- section：Abstract

- locator：P1 S5

- move_code：STUDY_OVERVIEW

- paraphrase_cn：研究通过数据挖掘实验、随机用户实验和适用性检查来评价框架和系统。

- rhetorical_function_cn：预告多阶段评价方案，体现设计科学的严谨性。

- depends_on_cn：制品的提出

- sets_up_cn：后文按此顺序展开评价。

- evidence_pointer：Abstract P1

### 4. P1 S6–S7

- order：4

- section：Abstract

- locator：P1 S6–S7

- move_code：RESULT

- paraphrase_cn：数据挖掘实验支持BOLT设计原则；用户实验中TheoryOn比EBSCOhost和Google Scholar更好地降低假阳性和假阴性。

- rhetorical_function_cn：给出最有说服力的量化结果摘要。

- depends_on_cn：评价方案预告

- sets_up_cn：为贡献声明提供证据基础。

- evidence_pointer：Abstract P1

### 5. P1 S8

- order：5

- section：Abstract

- locator：P1 S8

- move_code：CONTRIBUTION

- paraphrase_cn：适用性检查提供定性支持，总体证明设计制品对知识不可及问题的价值。

- rhetorical_function_cn：把技术结果提升到问题层面的贡献声明。

- depends_on_cn：前面的定量和定性评价

- sets_up_cn：对应Discussion中的综合贡献。

- evidence_pointer：Abstract P1

### 6. P1 S1–S2

- order：6

- section：Introduction

- locator：P1 S1–S2

- move_code：CONTEXT

- paraphrase_cn：行为研究者持续寻找和发展理论，例如计划行为理论被引超过七万次。

- rhetorical_function_cn：建立行为研究对理论依赖的背景。

- depends_on_cn：无

- sets_up_cn：为“文献规模巨大但研究者难以掌握”的悖论作铺垫。

- evidence_pointer：Introduction P1

### 7. P1 S3

- order：7

- section：Introduction

- locator：P1 S3

- move_code：PRACTICAL_STAKES

- paraphrase_cn：行为文献已扩大到无法完全掌握的程度，由于采用构念中心视角，文献检索完整性常以找到多少相关构念衡量；专家甚至在小规模全文集中也只能找到不到10%的有价值文章。

- rhetorical_function_cn：强调问题严重性，说明理论繁荣反而带来不可知。

- depends_on_cn：理论引用规模的背景

- sets_up_cn：引出“知识不可及”定义。

- evidence_pointer：Introduction P1

### 8. P2 S1

- order：8

- section：Introduction

- locator：P2 S1

- move_code：PHENOMENON

- paraphrase_cn：将知识不可及定义为行为知识嵌入大规模文献但研究者无法全面准确获取。

- rhetorical_function_cn：正式定义核心现象，限定研究对象。

- depends_on_cn：前段检索失败例证

- sets_up_cn：列出四方面负面影响。

- evidence_pointer：Introduction P2

### 9. P2 S2–S4

- order：9

- section：Introduction

- locator：P2 S2–S4

- move_code：WHY_GAP_MATTERS

- paraphrase_cn：知识不可及导致文献碎片化、重复研究和边缘研究，妨碍累积传统，降低研究敏捷性，并因多学科跨度带来巨大经济与社会成本。

- rhetorical_function_cn：说明该问题值得IS研究，不只是检索不便。

- depends_on_cn：知识不可及定义

- sets_up_cn：让后文提出IT制品具有现实必要性。

- evidence_pointer：Introduction P2

### 10. P3 S1–S2

- order：10

- section：Introduction

- locator：P3 S1–S2

- move_code：MECHANISM

- paraphrase_cn：行为理论不像自然科学那样使用严格普遍语言，因此需要构念中心观点，并在信息检索中澄清和综合构念关系。

- rhetorical_function_cn：解释为什么行为知识抽取需要专门设计。

- depends_on_cn：行为研究概念中心视角

- sets_up_cn：为BOLT采用本体学习提供合理性。

- evidence_pointer：Introduction P3

### 11. P4 S1–S3

- order：11

- section：Introduction

- locator：P4 S1–S3

- move_code：LIMITATION

- paraphrase_cn：全文搜索引擎擅长搜索阶段但不支持处理阶段；大量假阳性会让研究者过早结束检索。

- rhetorical_function_cn：指出现有制品的核心缺口。

- depends_on_cn：三阶段信息检索模型

- sets_up_cn：说明需要能抽取行为知识的新制品。

- evidence_pointer：Introduction P4

### 12. P4 S4

- order：12

- section：Introduction

- locator：P4 S4

- move_code：MECHANISM

- paraphrase_cn：关键词匹配和引用排序会放大研究者与领域的确认偏误，造成假阴性。

- rhetorical_function_cn：解释为什么现有搜索引擎不仅漏检还会系统性强化偏见。

- depends_on_cn：全文搜索引擎特征

- sets_up_cn：引出“抽取+构念检索”作为缓解机制。

- evidence_pointer：Introduction P4

### 13. P5 S1

- order：13

- section：Introduction

- locator：P5 S1

- move_code：RQ_OR_OBJECTIVE

- paraphrase_cn：为缓解知识不可及，论文提出BOLT设计框架和TheoryOn搜索引擎，以从大规模出版文献抽取行为知识。

- rhetorical_function_cn：提出全文的核心目标和两个制品。

- depends_on_cn：前面的缺口与机制

- sets_up_cn：后文框架、系统与评价全部围绕此展开。

- evidence_pointer：Introduction P5

### 14. P1 S1

- order：14

- section：Background

- locator：P1 S1

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：信息检索行为可分成搜索、获取、处理三个阶段，处理阶段包含跨文章的概念综合与分析。

- rhetorical_function_cn：引入支撑全文的基础模型。

- depends_on_cn：相关文献

- sets_up_cn：用于定位现有搜索引擎的局限。

- evidence_pointer：Background P1

### 15. P2 S1–S2

- order：15

- section：Background

- locator：P2 S1–S2

- move_code：LIMITATION

- paraphrase_cn：谷歌学术和EBSCOhost适合搜索初期和快速浏览，但不适合处理阶段，假阳性和假阴性会影响综合活动。

- rhetorical_function_cn：明确工具适用边界。

- depends_on_cn：三阶段模型

- sets_up_cn：后文用实例说明假阳性和假阴性。

- evidence_pointer：Background P2

### 16. P3 S1

- order：16

- section：Background

- locator：P3 S1

- move_code：LIMITATION

- paraphrase_cn：全文搜索引擎不抽取构念等行为知识元数据，导致构念搜索产生大量假阳性；例如“perceived usefulness”在谷歌学术返回9万多结果，很多不是目标构念。

- rhetorical_function_cn：用具体例子证明假阳性问题。

- depends_on_cn：对全文搜索引擎的一般批评

- sets_up_cn：为构念级索引提供动机。

- evidence_pointer：Background P3

### 17. P4 S1

- order：17

- section：Background

- locator：P4 S1

- move_code：LIMITATION

- paraphrase_cn：关键词匹配和引用/使用排序可能造成严重假阴性，并放大研究者和领域层面的确认偏误，例如同义不同名的social factors或image可能完全漏检。

- rhetorical_function_cn：说明与假阳性并列的另一问题。

- depends_on_cn：确认偏误文献

- sets_up_cn：提出同义构念检索的必要性。

- evidence_pointer：Background P4

### 18. P5 S1

- order：18

- section：Background

- locator：P5 S1

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：已有一些学术支持工具能抽取作者、引用、领域等元数据，但均未抽取假设、构念和关系。

- rhetorical_function_cn：避免读者认为作者不知道相关领域。

- depends_on_cn：文献调研

- sets_up_cn：指出元数据检索不足以解决行为知识不可及。

- evidence_pointer：Background P5

### 19. P6 S1

- order：19

- section：Background

- locator：P6 S1

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：生物医学文本挖掘虽抽取基因、蛋白质等实体关系，但由于基因命名规范化而行为构念语言易变，方法不能直接迁移。

- rhetorical_function_cn：排除最接近的替代技术来源。

- depends_on_cn：生物医学文本挖掘文献

- sets_up_cn：说明需要专门的行为本体学习框架。

- evidence_pointer：Background P6

### 20. P1 S1

- order：20

- section：Design Framework for Disembedding Behavioral Knowledge

- locator：P1 S1

- move_code：GAP

- paraphrase_cn：由于行为知识定义本身存在分歧，系统应具备哪些能力、任务和技术都缺乏清晰共识。

- rhetorical_function_cn：指出缺乏设计指南，为提出BOLT提供缺口。

- depends_on_cn：前面对现有制品不充分的论证

- sets_up_cn：引入设计框架。

- evidence_pointer：Design Framework section P1

### 21. P2 S1–S2

- order：21

- section：Design Framework for Disembedding Behavioral Knowledge

- locator：P2 S1–S2

- move_code：THEORY_INTRO

- paraphrase_cn：按设计科学范式，提出BOLT框架，由kernel theories、meta-requirements、meta-design和testable hypotheses构成。

- rhetorical_function_cn：建立设计理论结构作为本文骨架。

- depends_on_cn：设计科学文献

- sets_up_cn：后文各小节按这四个组件组织。

- evidence_pointer：Design Framework section P2

### 22. P2 S3

- order：22

- section：Design Framework for Disembedding Behavioral Knowledge

- locator：P2 S3

- move_code：THEORY_PROPOSITION

- paraphrase_cn：基于多个行为研究提供的kernel theories，行为知识可被视为理论实例集合，每个理论实例是专门本体，核心部分包括构念和关系。

- rhetorical_function_cn：把“行为知识”从模糊概念变成可操作的本体构念。

- depends_on_cn：Weber/Bunge理论

- sets_up_cn：为meta-requirements提供依据。

- evidence_pointer：Design Framework section P2

### 23. P2 S4

- order：23

- section：Design Framework for Disembedding Behavioral Knowledge

- locator：P2 S4

- move_code：REQUIREMENT

- paraphrase_cn：由此引出meta-requirements：行为知识抽取需支持假设（terms）、变量（concepts）、理论关系（non-taxonomic）和同义关系（taxonomic）的抽取。

- rhetorical_function_cn：把本体论映射到系统需求。

- depends_on_cn：理论实例作为专门本体

- sets_up_cn：后文四项BOLT任务直接对应这些需求。

- evidence_pointer：Design Framework section P2

### 24. P2 S5

- order：24

- section：Design Framework for Disembedding Behavioral Knowledge

- locator：P2 S5

- move_code：DESIGN_FEATURE

- paraphrase_cn：meta-design将语言学与统计/机器学习技术组织起来，为每一项BOLT任务提供可选技术。

- rhetorical_function_cn：界定系统构建的技术空间。

- depends_on_cn：本体学习文献

- sets_up_cn：使后续TheoryOn算法选择有所依据。

- evidence_pointer：Design Framework section P2

### 25. P2 S6

- order：25

- section：Design Framework for Disembedding Behavioral Knowledge

- locator：P2 S6

- move_code：HYPOTHESIS_OR_PROPOSITION

- paraphrase_cn：提出可检验假设：BOLT meta-design应既能抽取行为知识，又能增强信息检索结果，因此需要多元评价。

- rhetorical_function_cn：从构建转向评价，预告全文的评价结构。

- depends_on_cn：meta-requirements和meta-design

- sets_up_cn：为方法/系统/用户/适用性四类评价提供逻辑。

- evidence_pointer：Design Framework section P2

### 26. P1 S1

- order：26

- section：Kernel Theories

- locator：P1 S1

- move_code：THEORY_PROPOSITION

- paraphrase_cn：理论是行为研究最重要的知识类型，理论实例包括源起论文、重要扩展和所有采用该理论的文章。

- rhetorical_function_cn：明确行为知识的载体单位。

- depends_on_cn：Larsen et al.和Weber

- sets_up_cn：为“文章是专门本体”提供依据。

- evidence_pointer：Kernel Theories section P1

### 27. P1 S2–S5

- order：27

- section：Kernel Theories

- locator：P1 S2–S5

- move_code：THEORY_PROPOSITION

- paraphrase_cn：理论实例可视为Bunge式专门本体，核心部分是构念、构念关系和状态空间；构念关系包括主效应、调节、中介以及同义关系。

- rhetorical_function_cn：提供行为知识本体论的细粒度定义。

- depends_on_cn：Weber/Bunge/Baron & Kenny

- sets_up_cn：后文meta-requirements直接复用这些术语。

- evidence_pointer：Kernel Theories section P1

### 28. P2 S1

- order：28

- section：Meta-Requirements

- locator：P2 S1

- move_code：THEORY_PROPOSITION

- paraphrase_cn：本体学习的目标是从大量文本中抽取本体组件，这正好对应行为知识不可及的缓解目标。

- rhetorical_function_cn：把本体学习方法论引入问题。

- depends_on_cn：Buitelaar等人

- sets_up_cn：为层蛋糕映射做铺垫。

- evidence_pointer：Meta-Requirements section P2

### 29. P2 S2–P3 S1

- order：29

- section：Meta-Requirements

- locator：P2 S2–P3 S1

- move_code：REQUIREMENT

- paraphrase_cn：本体学习层蛋糕中的terms、concepts、taxonomic relations、non-taxonomic relations被分别映射为行为知识中的假设、构念、同义关系和理论关系。

- rhetorical_function_cn：给出从通用本体学习到行为知识的具体映射规则。

- depends_on_cn：层蛋糕概念与行为知识定义

- sets_up_cn：形成四项有序的meta-requirements。

- evidence_pointer：Meta-Requirements section

### 30. P1 S1

- order：30

- section：Meta-Design

- locator：P1 S1

- move_code：DESIGN_FEATURE

- paraphrase_cn：meta-design把上述需求转化为四项任务，并确定语言学与统计/ML两类技术类别。

- rhetorical_function_cn：将需求变成可执行任务。

- depends_on_cn：meta-requirements

- sets_up_cn：后续各抽取任务节的顺序。

- evidence_pointer：Meta-Design section

### 31. P1 S1–S4

- order：31

- section：Hypothesis Extraction

- locator：P1 S1–S4

- move_code：DESIGN_FEATURE

- paraphrase_cn：假设有格式化与非格式化两种形态，因此最好用规则法和机器学习结合来抽取。

- rhetorical_function_cn：为TheoryOn的混合分类器提供设计理由。

- depends_on_cn：假设格式示例

- sets_up_cn：后面实现中的规则+深度学习分类器。

- evidence_pointer：Hypothesis Extraction section

### 32. P1 S1–S3

- order：32

- section：Variable Extraction

- locator：P1 S1–S3

- move_code：DESIGN_FEATURE

- paraphrase_cn：变量抽取被视为序列标注问题，可使用CRF、Bi-LSTM和字符CNN等深度学习方法。

- rhetorical_function_cn：选择变量抽取的核心技术路径。

- depends_on_cn：IOB标注与NLP文献

- sets_up_cn：TheoryOn中DLMTCK第一阶段的深度结构。

- evidence_pointer：Variable Extraction section

### 33. P1 S1–S4

- order：33

- section：Theoretical Relationship Extraction

- locator：P1 S1–S4

- move_code：DESIGN_FEATURE

- paraphrase_cn：理论关系抽取依赖句法特征，复杂领域关系需要多阶段方法，SVM是强基线。

- rhetorical_function_cn：为TheoryOn选择SVM与树核提供依据。

- depends_on_cn：主效应/调节/中介示例

- sets_up_cn：后文复合核SVM设计。

- evidence_pointer：Theoretical Relationship Extraction section

### 34. P1 S1–S3

- order：34

- section：Synonymous Relationship Identification

- locator：P1 S1–S3

- move_code：DESIGN_FEATURE

- paraphrase_cn：同义关系识别融合词汇相似度、LSA和语义词典，并可使用Larsen和Bong的构念相似性算法。

- rhetorical_function_cn：为同义构念搜索提供技术选择。

- depends_on_cn：语义资源文献

- sets_up_cn：TheoryOn的LSA+Lucene搜索。

- evidence_pointer：Synonymous Relationship Identification section

### 35. P1 S1

- order：35

- section：Testable Hypotheses

- locator：P1 S1

- move_code：HYPOTHESIS_OR_PROPOSITION

- paraphrase_cn：框架需要两类测试：抽取行为知识的能力和增强信息检索结果的能力，并且都需要一个实例化系统作为评价基础。

- rhetorical_function_cn：把设计框架的验证条件正式陈述出来。

- depends_on_cn：BOLT四组件

- sets_up_cn：进入TheoryOn系统章节。

- evidence_pointer：Testable Hypotheses section

### 36. P1 S1

- order：36

- section：TheoryOn: An Instantiation of the Proposed Design Framework

- locator：P1 S1

- move_code：DESIGN_FEATURE

- paraphrase_cn：TheoryOn严格按BOLT框架中的技术处方实现各抽取步骤，并组装理论网络和搜索应用。

- rhetorical_function_cn：说明系统与框架的对应关系，保证instantiation validity。

- depends_on_cn：BOLT框架

- sets_up_cn：后续系统技术细节。

- evidence_pointer：TheoryOn section P1

### 37. P1 S1–S4

- order：37

- section：TheoryOn: Hypothesis Extraction

- locator：P1 S1–S4

- move_code：DESIGN_FEATURE

- paraphrase_cn：TheoryOn使用规则加深度学习的混合句分类器：word2vec、Bi-LSTM、规则特征和句序特征拼接后分类假设句。

- rhetorical_function_cn：给出具体实现，展示BOLT处方的落地。

- depends_on_cn：BOLT假设抽取任务

- sets_up_cn：后面的方法比较实验评价该分类器。

- evidence_pointer：TheoryOn Hypothesis Extraction subsection

### 38. P1 S1

- order：38

- section：TheoryOn: Variable and Theoretical Relationship Extraction

- locator：P1 S1

- move_code：DESIGN_FEATURE

- paraphrase_cn：变量和关系抽取被合并为DLMTCK两阶段模型：第一阶段用深度学习抽取变量并生成变元增强子树，第二阶段用复合核SVM分类关系。

- rhetorical_function_cn：提出本文的核心技术贡献。

- depends_on_cn：BOLT变量/关系任务、NLP深度学习方法

- sets_up_cn：后文方法/系统比较中的DLMTCK。

- evidence_pointer：TheoryOn Variable and Theoretical Relationship Extraction subsection

### 39. P1 S1

- order：39

- section：TheoryOn: Stage 2: Classification With Multiple Kernel Functions

- locator：P1 S1

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：SVM用最大间隔找到超平面；复合核将线性核与子树核线性组合，纳入丰富的句法信息同时降低过拟合。

- rhetorical_function_cn：解释为什么选取复合核SVM。

- depends_on_cn：统计学习理论

- sets_up_cn：附件C中的核函数细节。

- evidence_pointer：TheoryOn Stage 2 subsection

### 40. P1 S1–S2

- order：40

- section：TheoryOn: Theoretical Network Construction

- locator：P1 S1–S2

- move_code：DESIGN_FEATURE

- paraphrase_cn：系统按共享变量将假设连接成理论网络，并通过语义词典和最小编辑距离把同义变量归组。

- rhetorical_function_cn：说明从抽取结果到可视化理论网络的构建逻辑。

- depends_on_cn：变量/关系抽取结果

- sets_up_cn：支撑前因后果和理论整合功能。

- evidence_pointer：Theoretical Network Construction subsection

### 41. P1 S1–S3

- order：41

- section：TheoryOn: TheoryOn Search and Visualization

- locator：P1 S1–S3

- move_code：DESIGN_FEATURE

- paraphrase_cn：同义关系识别后，用户输入构念可返回相关理论网络；系统用定制LSA加Lucene关键词同时支持语义检索和关键词检索。

- rhetorical_function_cn：连接后端抽取与前端搜索功能。

- depends_on_cn：同义关系识别

- sets_up_cn：下一节四个系统功能描述。

- evidence_pointer：TheoryOn Search and Visualization subsection

### 42. P1 S1

- order：42

- section：Evaluation: Experiments to Examine Behavioral Knowledge Extraction Performance

- locator：P1 S1

- move_code：STUDY_OVERVIEW

- paraphrase_cn：为验证BOLT设计指南和提出的抽取方法，论文将框架指导的技术与替代方法进行benchmark比较。

- rhetorical_function_cn：开启评价章节，并说明评价目的。

- depends_on_cn：testable hypotheses

- sets_up_cn：随后说明数据和方法。

- evidence_pointer：Evaluation section P1

### 43. P1 S2–S3

- order：43

- section：Evaluation: Experiments to Examine Behavioral Knowledge Extraction Performance

- locator：P1 S2–S3

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：标注数据来自三个跨学科期刊1980–2009年的286篇文章，两位资深标注者标注；Kappa值显示信度高；最终得到1,913条假设、6,020个变量实例、3,135条关系。

- rhetorical_function_cn：说明评价数据的来源、规模和质量。

- depends_on_cn：抽取任务

- sets_up_cn：为方法/系统比较提供受控测试床。

- evidence_pointer：Evaluation section P1

### 44. Table 1前一段至结果段

- order：44

- section：Method Comparison Experiments and Results

- locator：Table 1前一段至结果段

- move_code：BENCHMARK_OR_CONTRAST

- paraphrase_cn：方法比较覆盖规则、特征分类器、深度学习和通用本体学习方法等替代技术。

- rhetorical_function_cn：建立全面的基准对照矩阵。

- depends_on_cn：testbed

- sets_up_cn：用Table 1结果证明BOLT技术优势。

- evidence_pointer：Method Comparison Experiments and Results

### 45. Table 1后结果段

- order：45

- section：Method Comparison Experiments and Results

- locator：Table 1后结果段

- move_code：RESULT

- paraphrase_cn：混合假设分类器、DLMTCK变量抽取和关系抽取分别在假设、变量和关系任务上达到最高F1。

- rhetorical_function_cn：报告方法层级的核心结果。

- depends_on_cn：方法比较

- sets_up_cn：为系统比较提供基准性能。

- evidence_pointer：Table 1

### 46. P1–P3

- order：46

- section：System Comparison Experiments and Results

- locator：P1–P3

- move_code：BENCHMARK_OR_CONTRAST

- paraphrase_cn：按Park等标准筛选四个通用本体学习系统与TheoryOn比较完整管线，从已抽取假设开始比较变量和关系抽取。

- rhetorical_function_cn：解释系统比较的对照选择与范围限制。

- depends_on_cn：通用ontology learning文献

- sets_up_cn：Table 2结果将显示通用系统不足。

- evidence_pointer：System Comparison Experiments and Results

### 47. Table 2后结果段

- order：47

- section：System Comparison Experiments and Results

- locator：Table 2后结果段

- move_code：RESULT

- paraphrase_cn：TheoryOn在变量和关系抽取上的F1显著高于四个通用系统；同时整体性能低于孤立方法，说明存在误差传播。

- rhetorical_function_cn：展示端到端效果并坦诚指出管线误差。

- depends_on_cn：系统比较实验

- sets_up_cn：为后续用户实验提供动机：抽取提升必须转化为用户效益。

- evidence_pointer：Table 2

### 48. 最后一段

- order：48

- section：System Comparison Experiments and Results

- locator：最后一段

- move_code：TRANSITION

- paraphrase_cn：在展示抽取能力后，需要用户实验和适用性检查来证明下游实用价值。

- rhetorical_function_cn：把论证从技术系统转向用户和任务。

- depends_on_cn：系统比较结果

- sets_up_cn：随机用户实验章节。

- evidence_pointer：System Comparison section final paragraph

### 49. P1 S1

- order：49

- section：Evaluation: User Experiments to Examine Information-Seeking Outcomes

- locator：P1 S1

- move_code：STUDY_OVERVIEW

- paraphrase_cn：研究包含两个用户研究：随机用户实验和适用性检查，分别定性与定量评价TheoryOn的信息检索结果。

- rhetorical_function_cn：预告用户层级评价。

- depends_on_cn：testable hypotheses中的第二方面

- sets_up_cn：分别展开两个研究。

- evidence_pointer：User Experiments section

### 50. P1–P2

- order：50

- section：Randomized User Experiment

- locator：P1–P2

- move_code：BENCHMARK_OR_CONTRAST

- paraphrase_cn：52名博士生被随机分配到TheoryOn、EBSCOhost、Google Scholar三组；四项任务围绕TAM设计，以高知名度TAM给传统全文搜索引擎最佳表现机会。

- rhetorical_function_cn：确定用户实验的对照设计并试图对baseline有利。

- depends_on_cn：信息检索任务

- sets_up_cn：客观precision/recall和感知效用比较。

- evidence_pointer：Randomized User Experiment section

### 51. P2 S2

- order：51

- section：Randomized User Experiment

- locator：P2 S2

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：金标准由经验丰富的教师、博士生和研究助理团队构建；评价同时采用客观检索性能与感知效用。

- rhetorical_function_cn：说明用户实验测量工具与金标准来源。

- depends_on_cn：评价任务设计

- sets_up_cn：Table 3和Table 4的结果。

- evidence_pointer：Randomized User Experiment section P2

### 52. P1 S1

- order：52

- section：Construct and Theory Retrieval Performance

- locator：P1 S1

- move_code：RESULT

- paraphrase_cn：TheoryOn用户的F-measure在四项任务上比EBSCOhost和Google Scholar高37%到121%，假阴性最多减少158%。

- rhetorical_function_cn：给出用户层最核心的量化证据。

- depends_on_cn：随机用户实验

- sets_up_cn：讨论中关于知识不可及缓解的主张。

- evidence_pointer：Construct and Theory Retrieval Performance

### 53. P2

- order：53

- section：Construct and Theory Retrieval Performance

- locator：P2

- move_code：ROBUSTNESS_OR_BOUNDARY_TEST

- paraphrase_cn：错误分析显示，用户搜索recall低于方法抽取recall可能因为时间有限未检查全部结果；用户precision高于方法精度则是由于用户能人工过滤部分假阳性。

- rhetorical_function_cn：解释系统性能与用户绩效之间的差异，增加结论透明度。

- depends_on_cn：Table 3与Table 1对比

- sets_up_cn：指出未来可研究工具组合场景。

- evidence_pointer：Construct and Theory Retrieval Performance P2

### 54. P1 S1

- order：54

- section：Perceived Utility

- locator：P1 S1

- move_code：RESULT

- paraphrase_cn：四项任务的感知有用性均显著优于两个baseline，系统级易用性和有用性也显著更高，行为意向只是边际显著。

- rhetorical_function_cn：补充用户主观接受度证据。

- depends_on_cn：感知量表

- sets_up_cn：解释BI边际显著是由于系统未公开。

- evidence_pointer：Perceived Utility section

### 55. P1 S1

- order：55

- section：Applicability Check

- locator：P1 S1

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：适用性检查采用Rosemann和Vessey框架，请10名助理至正教授通过NGT会议评价TheoryOn的重要性、可访问性和适合性。

- rhetorical_function_cn：说明第三个评价环节的方法来源。

- depends_on_cn：设计科学适用性检查文献

- sets_up_cn：后续14步信息检索流程和定性引语。

- evidence_pointer：Applicability Check section

### 56. 结果段

- order：56

- section：Applicability Check

- locator：结果段

- move_code：RESULT

- paraphrase_cn：学者确认了信息检索三阶段，认为TheoryOn在处理阶段最有价值，能补充Google Scholar，也让新手更快进入新领域。

- rhetorical_function_cn：提供生态和定性支持，并给出适用场景。

- depends_on_cn：NGT会议结果

- sets_up_cn：Discussion中“何时、对谁、如何有用”的结论。

- evidence_pointer：Applicability Check results

### 57. BOLT Framework段

- order：57

- section：Discussion

- locator：BOLT Framework段

- move_code：CONTRIBUTION

- paraphrase_cn：方法评价结果证明BOLT meta-design处方有效，并说明采用概念中心视角抽取行为知识是可行的。

- rhetorical_function_cn：把方法结果上升为框架层面的贡献。

- depends_on_cn：方法比较实验

- sets_up_cn：随后讨论系统贡献。

- evidence_pointer：Discussion BOLT Framework paragraph

### 58. TheoryOn System段

- order：58

- section：Discussion

- locator：TheoryOn System段

- move_code：CONTRIBUTION

- paraphrase_cn：TheoryOn作为BOLT实例，在用户实验中表现优于EBSCOhost和Google Scholar，适用性检查也提供支持，说明BOLT指导的系统能抽取知识并改善信息检索。

- rhetorical_function_cn：把系统实例与用户结果绑定为整体贡献。

- depends_on_cn：用户实验和适用性检查

- sets_up_cn：进入多元评价的贡献讨论。

- evidence_pointer：Discussion TheoryOn System paragraph

### 59. Multifaceted Evaluation段

- order：59

- section：Discussion

- locator：Multifaceted Evaluation段

- move_code：CONTRIBUTION

- paraphrase_cn：多元评价贡献之一是：智能文本分析可以缓解知识不可及，且precision和recall都应成为设计考虑。

- rhetorical_function_cn：从结果提炼可复用的设计知识。

- depends_on_cn：用户实验中的precision/recall差异

- sets_up_cn：下一条关于BOLT系统价值的主张。

- evidence_pointer：Discussion Multifaceted Evaluation (1)

### 60. Multifaceted Evaluation段

- order：60

- section：Discussion

- locator：Multifaceted Evaluation段

- move_code：CONTRIBUTION

- paraphrase_cn：贡献之二是提供首个关于BOLT系统可能、实用且有价值的广泛实证和定性研究。

- rhetorical_function_cn：强调研究的首创性和证据覆盖范围。

- depends_on_cn：随机用户实验与适用性检查

- sets_up_cn：一般化讨论。

- evidence_pointer：Discussion Multifaceted Evaluation (2)

### 61. Generalizability段

- order：61

- section：Discussion

- locator：Generalizability段

- move_code：BOUNDARY_CONDITION

- paraphrase_cn：设计制品可推广到多学科；概念中心视角可扩展到哲学、法律等场景，深度学习方法可应对更复杂NLP问题，多元评价适合数据-理论-ML交叉制品。

- rhetorical_function_cn：将单个设计实例结果提升为一般设计知识。

- depends_on_cn：BOLT、TheoryOn和评价结果

- sets_up_cn：最后讨论对知识不可及的影响。

- evidence_pointer：Discussion Generalizability section

### 62. P1 S1–S3

- order：62

- section：Conclusions and Future Directions

- locator：P1 S1–S3

- move_code：CONTRIBUTION

- paraphrase_cn：总结三个贡献：BOLT框架、TheoryOn实例、以及通过数据挖掘实验、随机用户实验和适用性检查获得的多方面见解。

- rhetorical_function_cn：收束全文贡献。

- depends_on_cn：全文证据链

- sets_up_cn：未来方向与使用统计。

- evidence_pointer：Conclusions and Future Directions

### 63. P3–P4

- order：63

- section：Conclusions and Future Directions

- locator：P3–P4

- move_code：OTHER

- paraphrase_cn：作者补充了TheoryOn上线后12个月仅靠口碑获得的用户规模、行动次数、搜索次数和覆盖国家等使用统计。

- rhetorical_function_cn：用真实使用数据增强外部有效性和未来可行性。

- depends_on_cn：系统已上线

- sets_up_cn：展望自动文献综述和自动meta-analysis。

- evidence_pointer：Conclusions and Future Directions P3

## 写作技术

- gap_construction_cn：作者不是简单说“没人研究”，而是先给出“文献规模大但专家只能找到<10%”的经验现象，再用信息检索三阶段模型把缺口定位在processing phase，并指出现有谷歌学术/EBSCO、元数据系统、生物医学挖掘三类工具都无法抽取行为知识。缺口因此被塑造成“现有制品不能实现一个对IS重要的目标”，而非“文献空白”。

- signposting_cn：标题直接给出设计框架名（BOLT）和系统名（TheoryOn）；正文按设计理论四组件命名小标题；Evaluation部分明确区分“抽取性能”和“信息检索结果”；Discussion分为BOLT Framework、TheoryOn System、Multifaceted Evaluation、Generalizability、Impact五个层级，读者始终知道当前论证位置。

- transition_logic_cn：每个阶段结尾都会留下一个尚未回答的问题：框架需要实例化→系统需要评价→孤立方法需要验证管线→管线需要用户实验→用户实验需要定性场景→最后进入讨论；主要用“未满足用户价值”“误差传播”“下游价值”等过渡。

- claim_evidence_rhythm_cn：总是先提出需求/设计，再给出实现，然后用表格数据结果紧跟主张；例如先列出BOLT四项任务，再给TheoryOn实现，最后Table 1/2/3逐层交付证据；讨论部分再引用这些表格数据回扣主张。

- benchmark_narrative_cn：benchmark不是堆砌，而是按“替代方法→通用系统→全文搜索引擎→实际适用性”四层叙事逐步升级；每一层都说明为什么选择该baseline（如TAM高认知有利于baseline；系统比较选择相关组件以保证公平），读者会被引导接受每层比较的合理性。

- theory_return_cn：结果不是停留在“TheoryOn更好”，而是在Discussion中把用户实验结果回扣到知识不可及的四类危害，再抽象成概念中心视角、复杂NLP、整体评价三条一般化知识，并声明这是对信息检索processing阶段的理论支持。

- contribution_positioning_cn：开头把工作定位为“将本体学习方案exaptation到行为知识抽取”；结尾则把贡献分成框架、系统、评价三个层次，并把IS定位为设计科学、行为方法和NLP的自然交叉点。

- novelty_protection_cn：作者用三阶段证据链保护贡献不被看作一次性性能结果：method comparison说明技术好，system comparison说明完整系统好，randomized user experiment说明用户检索结果好，applicability check说明真实有用；讨论部分又把结果从具体任务提升为概念中心视角和多重评价设计知识。

## 可复用研究与写作程序

### structure_steps

#### 1. 1

- step：1

- writing_job_cn：写作任务：定义领域现实问题，给出可量化的现象（如专家检索率<10%）和后果。

- research_job_cn：研究任务：梳理目标用户的工作流程阶段，找到现有制品未覆盖的关键阶段。

- required_evidence_cn：需要来自领域数据的现象证据或已有研究中的量化指标。

- transition_to_next_cn：从“问题在该阶段凸显”过渡到“需要新制品”。

#### 2. 2

- step：2

- writing_job_cn：写作任务：引入kernel theories，把问题中的关键概念转成本体/理论构念。

- research_job_cn：研究任务：选择能定义知识结构的基础理论，并与目标领域概念逐一对齐。

- required_evidence_cn：需要理论文献支持核心概念的定义与分解。

- transition_to_next_cn：从知识结构转换为系统要求。

#### 3. 3

- step：3

- writing_job_cn：写作任务：按设计理论四件套组织框架（kernel theories、meta-requirements、meta-design、testable hypotheses）。

- research_job_cn：研究任务：明确需求、任务、技术类别，并提出与需求对应的可检验假设。

- required_evidence_cn：需要能说明每项任务为何必要、技术为何可行的文献依据。

- transition_to_next_cn：从抽象框架转向具体实例系统。

#### 4. 4

- step：4

- writing_job_cn：写作任务：描述实例系统如何遵循框架，给出关键算法和系统功能。

- research_job_cn：研究任务：实际构建系统或原型，并保证设计选择能追溯到框架要求。

- required_evidence_cn：需要能运行的系统或原型，并最好有图示和功能说明。

- transition_to_next_cn：从构建转向评价，说明为什么需要多层次评价。

#### 5. 5

- step：5

- writing_job_cn：写作任务：用方法/系统/用户/适用性四个层面组织评价，每层设明确baseline。

- research_job_cn：研究任务：先在受控数据上比较组件和管线，再用用户实验和定性检查证明实践价值。

- required_evidence_cn：需要标注数据、基准系统、用户样本和金标准。

- transition_to_next_cn：从评价结果转向设计与理论贡献。

#### 6. 6

- step：6

- writing_job_cn：写作任务：在讨论中把具体结果上升为可复用设计知识，并回扣开头问题。

- research_job_cn：研究任务：提炼一般化原则、边界条件和未来扩展。

- required_evidence_cn：需要能够从实验数据中抽象出跨场景主张的证据链。

- transition_to_next_cn：收束为贡献总结。

### most_transferable_moves_cn

1. 用阶段模型（三阶段信息检索）定位现有工具盲区

2. 用设计科学四件套（kernel theories、meta-requirements、meta-design、testable hypotheses）组织研究

3. 用ontology layer cake建立“领域知识→可计算输出”的映射

4. 把复杂关系分解为二元子问题再组装，降低技术难度

5. 采用“方法→系统→用户→适用性”四层评价，逐级增强证据

6. 在讨论中按制品、评价、一般化、影响分层贡献

### resource_intensive_or_nonstandard_parts_cn

1. 286篇跨学科文献的人工标注需要资深研究者长时间投入

2. 随机用户实验需招募52名全球博士生并构造专家金标准

3. 适用性检查需要10名教授参与多轮NGT与上手任务，成本高

4. TheoryOn系统本身需要大量NLP/ML开发资源和持续维护

5. 结论中的使用统计依赖系统真实上线和口碑扩散，普通项目难以复制

### what_not_to_copy_superficially_cn

1. 不能只写“我们提出框架”而没有kernel theory到meta-requirements的推导

2. 不能只用方法比较就声称解决实践问题；用户层证据是必要的

3. 不能把适用性检查中的积极引语当因果证据

4. 不能忽略baseline选择理由；每个对照都应有明确选择标准

5. 不能把“未来可实现自动综述”当作已验证贡献

- single_best_description_of_the_routine_cn：先用设计理论四件套把现实问题翻译成本体学习任务，再实例化成系统，再用算法—系统—用户—适用性四层证据逐级证明从抽取性能到信息检索价值的完整链条。

## 分析边界

全文完整，但输入文本来自PDF转换，少量表格符号（如+、^、±）和附录编号可能存在OCR痕迹；没有独立页码，位置只能使用章节、段落和表格定位；无法访问TheoryOn系统复现使用统计与界面功能。
