# Applied machine learning for a zero defect tolerance system in the automated assembly of pharmaceutical devices

- 作者：Sebastian Dengler; Said Lahriri; Emanuel Trunzer; Birgit Vogel-Heuser
- 年份 / 期刊：2021 / Decision Support Systems
- DOI：10.1016/j.dss.2021.113540
- 源文件：19748_2021_applied-machine-learning-for-a-zero-defect-tolerance-system-in-the-automated-assembly-of-pharmac.md
- 论文主类型：build_evaluate_design_science
- 主导写作弧线：requirements_build_evaluate_design_principles
- 置信度：0.82

## 文章级论证概况

- 核心问题：如何在制药自动组装线上构建一个既能零漏检、又将误检控制在可接受范围，且能实时运行、可解释的ML质检系统？

- 制品与设计：多层QC系统：第一层k-means异常检测先剔除未知/可疑样本；第二层由DT+SVM+CNN组成的集成分类器区分正常与多类装配错误（DT用统计特征、SVM用标准化全序列、CNN用原始序列并配合Grad-CAM）；第三层投票方案（多数、veto、元分类器）产生最终二值质检结论和细粒度错误类别。

- 客观结果：预研和两个真实工业UC均实现FNR=0；FPR在预研、UC1、UC2分别为14.85%、9.04%、2.32%（不同投票/重采样条件下）；单样本或批量推理延迟远低于150ms和200ms；CAM可视化显示与类别相关的信号区域。

- 核心贡献：提出并评估了一个面向制药装配的、可零漏检、低误检、软实时、可解释的数据驱动QC系统；填补了ML用于制药行业成品QC的空白，并为预测性过程监控提供基础。

- 整篇论证链：从GMP的零缺陷质量要求和传统二值QC的局限出发，指出制药装配需要既能找出全部缺陷品又不产生过多误拒、还能给出拒绝原因的系统；作者组合已知ML方法构建异常检测+集成分类器+投票分层架构；先用试验台预研选择组件和投票方案，再用两个真实工业数据用例检验其在低/高频采样、不同物理过程下的表现；结果显示在有限批次中FNR均为0且延迟满足软实时约束，误检主要来自异常检测层；最后明确早期可行性定位与未来预测性监控方向。

## 类型与写作弧线判定

- 论文主类型判定：作者在方法学中对照Hevner七条设计科学准则，自述目标是创建ML制品和软件原型，并用两个真实工业用例和预研数据进行评价；不属于受控平台实验、形式优化或纯benchmark论文，因此判定为设计科学构建-评价型。

- 主导写作弧线判定：文章先由GMP零缺陷、低误拒、实时性等要求定义问题，随后构建多层ML质量控制系统，再用预研究和两个真实工业用例评价，最后以局限性、边界和未来路径收束；整体符合要求-构建-评价-设计知识弧线，尽管设计原则未以编号形式明确写出。

## 研究开展程序

- study_or_phase_count：5

- 研究阶段总序列：问题与需求界定→算法制品构建→预研试验台评估与设计选型→真实用例1评估→真实用例2评估。每个后面的阶段都承接前面阶段留下的不确定性：需求阶段确定FNR=0、FPR、实时性和可解释性约束；构建阶段据ML知识形成分层架构；预研验证可行性和投票方案；UC1检验真实低采样率场景；UC2检验高采样率场景的可迁移性。

### studies_or_phases

#### 1. 问题与需求界定

- order：1

- name_cn：问题与需求界定

- question_cn：制药自动组装线中，传统二值QC在零缺陷政策、低误拒、实时性、根因解释上的缺口是什么？

- inputs_and_setting_cn：GMP法规、真实制药装配线的流程结构、FMEA和领域专家知识、Gage R&R与装配公差知识。

- designed_or_compared_object_cn：不涉及具体实验对象；主要界定系统设计时应满足的约束，并将传统规则式QC作为问题化对象。

- baseline_control_or_counterfactual_cn：传统二值规则式QC，即超过阈值即报废的专家系统。

##### objective_metrics

1. FNR为0

2. FPR可接受

3. 实时性（150ms/200ms截止）

4. 错误根因可解释性

- analysis_method_cn：定性需求分析和文献对照，引用制药GMP要求和现有ML/时间序列分类研究。

- main_result_cn：得到系统设计必须支持的核心需求：不能漏掉任何缺陷品；误检只能造成经济损耗但可容忍；需要在产品离开工位前作出判断；需要区分多种错误类型以支持维护决策。

- argumentative_role_cn：为全文建立问题合法性和评价标准，说明为什么需要新的ML质检系统。

- remaining_uncertainty_cn：尚未有任何算法设计，也没有数据证明这些需求能否实现。

- link_to_next_phase_cn：需求直接转化为构件设计：零漏检→异常检测前置；可解释→DT和Grad-CAM；实时→选择低复杂度算法和批量推理。

##### evidence_pointers

1. Introduction P1-P4

2. Section 3 开头

3. Section 3.1 关于150ms

4. Section 3.2 关于200ms

#### 2. 算法制品构建

- order：2

- name_cn：算法制品构建

- question_cn：如何将零漏检要求和既有ML理论转化为一个可运行的QC系统？

- inputs_and_setting_cn：ML理论背景（DT、SVM、CNN、k-means、DTW、集成投票）、工业约束、Python/scikit-learn/Keras/tslearn。

- designed_or_compared_object_cn：构建对象为三层流水线：k-means异常检测、DT/SVM/CNN集成分类器、投票方案；同时定义了候选距离度量、特征设置和超参数搜索空间。

- baseline_control_or_counterfactual_cn：单一分类器、大多数投票、veto投票、元分类器，以及欧氏距离vs DTW。

##### objective_metrics

1. FNR

2. FPR

3. 训练/推理时间

4. 混淆矩阵

- analysis_method_cn：基于已知ML理论进行架构设计，并用网格搜索+5折分层交叉验证选择超参数。

- main_result_cn：形成异常检测→集成分类→投票决策的系统原型；各组件可独立优化；算法以Python实现并公开源代码。

- argumentative_role_cn：将抽象需求翻译成具体制品，说明每个设计选择对应哪个知识基础。

- remaining_uncertainty_cn：没有数据证明该组合在真实工业环境中的效果。

- link_to_next_phase_cn：制品需要在受控条件下先验证，因此进入预研试验台评估。

##### evidence_pointers

1. Section 4

2. Section 5

3. Fig. 5

4. Section 5.4

#### 3. 预研试验台评估与设计选型

- order：3

- name_cn：预研试验台评估与设计选型

- question_cn：在受控实验室数据上，系统能否实现FNR=0且FPR可接受？不同投票方案和组件的表现如何？

- inputs_and_setting_cn：试验台上的线性电机、夹爪、夹具、力传感器和两个待装配件；数据量2268条，含正常类和4个错误类。

- designed_or_compared_object_cn：对系统整体及组件进行消融式比较：AD、DT、SVM、CNN分别的误差；多数/veto/meta DT/meta SVM投票方案；二元QC输出与多类输出。

- baseline_control_or_counterfactual_cn：单一算法的二分类和多分类误差，以及不同投票方案的对比。

##### objective_metrics

1. FNR

2. FPR

3. 总体误差

4. 混淆矩阵

- analysis_method_cn：80/20训练测试切分、网格搜索交叉验证、混淆矩阵分析、误分类样本细查。

- main_result_cn：所有投票方案都实现FNR=0和FPR=14.85%；15个正常样本被AD层误判为坏件，但集成层本身可正确识别；meta DT整体最好；CAM能突出Error 3和Error 4的类别相关信号区域。

- argumentative_role_cn：证明系统在受控条件下可行，并由此固定后续使用的投票方案和关键组件。

- remaining_uncertainty_cn：试验台数据可能与真实生产线有差异；FPR仍偏高；样本是否真正代表目标错误行为存在不确定。

- link_to_next_phase_cn：将同一套系统应用到真实工业数据，检验其是否仍能维持FNR=0并降低FPR。

##### evidence_pointers

1. Section 5.2

2. Section 5.3

3. Fig. 8

4. Fig. 9

#### 4. 真实用例1评估

- order：4

- name_cn：真实用例1评估

- question_cn：在20线性电机的真实组装线上，系统是否能在150ms内零漏检并控制误检？对可变长度和损坏速度信号是否稳健？

- inputs_and_setting_cn：UC1：含20个线性电机的工位，40Hz采样，单条时间序列仅37-41个点；正常830条、Error 1=1180、Error 2=821、Error 3=1278，总计4109条；速度通道因PLC转换错误损坏。

- designed_or_compared_object_cn：比较三种输入预处理方案：重采样到38点、41点、38点并数值求导得到速度；比较多数/veto/meta投票。

- baseline_control_or_counterfactual_cn：不同重采样场景、不同投票方案、AD与集成组件误差比。

##### objective_metrics

1. FNR

2. FPR

3. 总体误差

4. 执行时间

- analysis_method_cn：离线训练和测试、混淆矩阵、组件误差贡献、10次随机样本的延迟测量和批量处理延迟测量。

- main_result_cn：所有条件下FNR=0；重采样到38点时民主投票和meta DT给出最佳FPR=9.04%；所有15个FP来自AD层，集成层达到完美分类；单样本处理平均3.109ms，20样本批量7.922ms，远低于150ms截止。

- argumentative_role_cn：证明系统在真实工业低采样率、信号损坏、时间长度不一致条件下仍满足零漏检和软实时要求。

- remaining_uncertainty_cn：仅一个真实过程；仍受限于有限批次；没有与旧QC并行运行；AD误检未被完全消除。

- link_to_next_phase_cn：需要第二个不同硬件和采样率的真实用例来检验系统是否可迁移。

##### evidence_pointers

1. Section 3.1

2. Table 1

3. Section 6.1

4. Fig. 10

#### 5. 真实用例2评估

- order：5

- name_cn：真实用例2评估

- question_cn：在高采样率PPU压装线上，系统的零漏检、低误检和软实时表现是否仍然成立，从而验证可迁移性？

- inputs_and_setting_cn：UC2：pick-and-place单元，2kHz采样，记录位置和力；正常9478条、Error 1=48、Error 2=1261、Error 3=1241，总计12028条；平均约1000个点。

- designed_or_compared_object_cn：比较降采样到100、200、500点；比较多数/veto/meta投票；比较AD与集成组件误差。

- baseline_control_or_counterfactual_cn：不同降采样选项、不同投票方案、组件误差贡献。

##### objective_metrics

1. FNR

2. FPR

3. 总体误差

4. 执行时间

- analysis_method_cn：离线训练和测试、混淆矩阵、组件误差贡献、延迟测量和批量处理延迟测量。

- main_result_cn：所有测试FNR=0；降采样到200点时最佳FPR=2.32%；AD的误分类明显多于集成层；集成层可能出现FN，但AD将其过滤；两个样本批量处理平均5.953ms，低于200ms截止。

- argumentative_role_cn：证明系统在完全不同采样频率和物理过程上仍有效，显著增强外部有效性。

- remaining_uncertainty_cn：仍仅两个真实UC和少量批次；没有覆盖batch-to-batch长期变异；没有做Gage R&R；错误标签可靠性和成本未评估。

- link_to_next_phase_cn：两个UC的结果共同进入讨论部分，用于声明边界条件和未来预测性监控方向。

##### evidence_pointers

1. Section 3.2

2. Table 1

3. Section 6.2

4. Fig. 11

## 各部分修辞架构

### abstract_moves

1. CONTEXT

2. LIMITATION

3. RQ_OR_OBJECTIVE

4. STUDY_OVERVIEW

5. RESULT

6. BOUNDARY_CONDITION

### introduction_moves

1. CONTEXT

2. PRACTICAL_STAKES

3. PRIOR_KNOWLEDGE

4. LIMITATION

5. GAP

6. WHY_GAP_MATTERS

7. RQ_OR_OBJECTIVE

8. CONTRIBUTION

9. BOUNDARY_CONDITION

10. STUDY_OVERVIEW

### theory_and_knowledge_moves

1. THEORY_INTRO

2. PRIOR_KNOWLEDGE

3. MECHANISM

4. REQUIREMENT

### artifact_design_moves

1. REQUIREMENT

2. DESIGN_FEATURE

3. METHOD_JUSTIFICATION

4. BENCHMARK_OR_CONTRAST

### evaluation_moves

1. STUDY_OVERVIEW

2. BENCHMARK_OR_CONTRAST

3. RESULT

4. ROBUSTNESS_OR_BOUNDARY_TEST

### discussion_and_contribution_moves

1. BOUNDARY_CONDITION

2. LIMITATION_AND_FUTURE

3. CONTRIBUTION

4. BOUNDARY_CONDITION

## 理论/知识到设计的翻译

### 知识/理论基础

1. GMP法规和零缺陷质量政策

2. 传统QC的阈值规则和Gage R&R/装配公差

3. FNR/FPR不对称性和质检指标

4. 决策树CART的可解释性与过拟合问题

5. SVM的最大间隔理论、核技巧和预测速度

6. CNN对网格状/时间序列数据的局部相关性建模

7. Grad-CAM类激活映射可解释性

8. k-means/1-NN异常检测和动态时间规整

9. 集成学习与投票/堆叠泛化

10. 软实时系统与PLC通信的时间约束

- 理论—设计耦合：partial

- 耦合判定理由：ML理论解释了各组件为什么适合问题，但最终制品选择大量依赖工业约束、网格搜索和实验比较；例如欧氏距离因运行时优势而非理论最优被选中，meta DT因实验结果优于其他投票方案而入选。因此知识基础前瞻性影响了架构，但未严格完全决定每个设计。

- 理论到设计翻译链：QC中FN绝对不可接受→异常检测前置+保守投票；DT可解释但易过拟合→用统计特征树并限制深度；SVM高维快速但黑箱→标准化全序列作为第二分类器；CNN适合时间序列但难解释→配合一维Grad-CAM；未知错误无法由训练类别覆盖→k-means在正常数据上聚类并设阈值；系统必须实时→舍弃DTW选欧氏距离并采用批量推理；单分类器危险→集成+投票。

### mapping_table

#### 1. 1

- theory_or_knowledge_claim_cn：在质检中FN会放行缺陷品，后果严重；FP只造成经济损失。

- mechanism_cn：分类器应对正常类设置严格条件，牺牲部分正常样本以避免漏检。

- design_requirement_cn：系统在结构上必须先保证FNR趋近于0，FPR尽量低。

- artifact_choice_cn：第一层k-means异常检测；第二层集成分类器；第三层多数/veto/元投票。

- evaluated_contrast_cn：AD vs 集成层；不同投票方案；二值输出 vs 多类输出。

- objective_result_cn：预研和两个真实UC均FNR=0；FPR分别为14.85%、9.04%、2.32%。

##### evidence_pointers

1. Section 4.1

2. Fig. 8-11

#### 2. 2

- theory_or_knowledge_claim_cn：决策树学习规则可被人理解，但容易过拟合。

- mechanism_cn：用少量统计特征并限制树深，可同时保留规则解释力和泛化性。

- design_requirement_cn：系统需要向操作者解释拒绝原因。

- artifact_choice_cn：DT只使用每个窗口的最小值/最大值/均值/标准差等简单统计特征，并通过最大深度控制。

- evaluated_contrast_cn：DT在集成中的误差；meta DT与其他投票方案。

- objective_result_cn：meta DT在预研/UC中成绩最佳，能生成可用的最终混淆矩阵。

##### evidence_pointers

1. Section 4.2

2. Section 5.2.1

3. Section 5.3

4. Fig. 9

#### 3. 3

- theory_or_knowledge_claim_cn：SVM通过最大间隔超平面分类，核技巧可处理非线性，预测快但可解释性有限。

- mechanism_cn：对全时间序列标准化后交给SVM，可让算法自行利用高维时序信息。

- design_requirement_cn：需要准确且推理速度快的分类器，以支持实时QC。

- artifact_choice_cn：SVM作为集成第二分类器，使用标准化全序列信号。

- evaluated_contrast_cn：SVM在集成中的总体误差；不同核/超参数组合。

- objective_result_cn：SVM与其他分类器共同贡献集成决策，但不是最好组件。

##### evidence_pointers

1. Section 4.3

2. Section 5.2.2

3. Fig. 8b

#### 4. 4

- theory_or_knowledge_claim_cn：CNN擅长处理网格状数据，可捕捉相邻时间点的相关关系；Grad-CAM可定位决策依赖的区域。

- mechanism_cn：卷积和池化从时间序列中提取局部模式，反向梯度生成一维CAM。

- design_requirement_cn：既要高精度时序分类，又要让人理解模型依据。

- artifact_choice_cn：自定义CNN+一维Grad-CAM作为第三个分类器并输出解释图。

- evaluated_contrast_cn：CAM可视化正常、Error 3、Error 4；CNN在集成中的误差。

- objective_result_cn：CAM突出Error 3的高力尖峰和Error 4的后半段电机停滞/电流下降，支持操作者定位问题。

##### evidence_pointers

1. Section 4.4

2. Section 5.2.3

3. Fig. 7

#### 5. 5

- theory_or_knowledge_claim_cn：训练数据无法覆盖所有未知错误；传统分类器会把未知样本硬分到已知类别。

- mechanism_cn：在正常样本上做k-means聚类，用距离分布设定阈值，可先把未知/异常样本滤掉。

- design_requirement_cn：零缺陷政策要求未知错误也不能被放行。

- artifact_choice_cn：第一层使用k-means异常检测，阈值用Youden指数在ROC曲线上选取。

- evaluated_contrast_cn：不同k和距离度量（Euclidean vs DTW）；AD与集成层误分类。

- objective_result_cn：UC1中Euclidean因低FNR和O(n)复杂度被选用；AD是主要FP来源，但能够滤除未知样本。

##### evidence_pointers

1. Section 5.1

2. Table 2

3. Fig. 10b

4. Fig. 11b

#### 6. 6

- theory_or_knowledge_claim_cn：集成投票/堆叠可减少单一分类器风险，提高准确率。

- mechanism_cn：veto投票使单分类器阻止最终判定，降低FN；元分类器学习组合各模型输出。

- design_requirement_cn：最终质量判定必须稳健，不能因单个模型误判导致漏检。

- artifact_choice_cn：比较多数投票、veto投票、meta DT和meta SVM四种方案。

- evaluated_contrast_cn：各投票方案在预研、UC1、UC2上的FNR/FPR和组件误差。

- objective_result_cn：预研中所有投票方案FNR=0，民主投票可减少FP；meta DT整体最佳。

##### evidence_pointers

1. Section 5.3

2. Fig. 8a

3. Fig. 10a

4. Fig. 11a

#### 7. 7

- theory_or_knowledge_claim_cn：工业产线有明确周期和PLC通信截止时间，且信号长度可能不一致。

- mechanism_cn：对可变长信号重采样/降采样可统一输入形状；批量推理能显著降低平均延迟。

- design_requirement_cn：预测必须在产品离开工位前完成，且不能给PLC带来过大负载。

- artifact_choice_cn：UC1线性插值到38或41点，UC2降采样到100/200/500点；支持批量处理。

- evaluated_contrast_cn：不同重采样/降采样场景和单样本vs批量延迟。

- objective_result_cn：UC1最佳FPR=9.04%，UC2最佳FPR=2.32%；批量延迟7.922ms/5.953ms，低于150/200ms。

##### evidence_pointers

1. Section 6.1

2. Section 6.2

3. Fig. 10e

4. Fig. 11e

## 评价逻辑

### evaluation_modes

1. 离线有监督分类评估

2. 组件消融/内部对照

3. 不同重采样/降采样和数据预处理对照

4. 运行时性能测量

5. 可解释性可视化展示

6. 跨两个真实工业用例的外部验证

- why_these_evaluations_cn：因论文目标是设计科学制品，需要证明制品可实例化并满足工业要求：FNR=0对应零缺陷政策；FPR可接受对应经济代价；延迟低于150/200ms对应软实时；组件对照和投票方案比较对应架构合理性；两个不同采样率和物理过程的UC对应可迁移性；CAM对应可解释性。

- benchmark_and_contrast_chain_cn：没有外部基准数据集，而是建立内部对照链：预研先用80/20切分和交叉验证比较各算法与投票方案，选出meta DT；UC1再比较重采样场景和投票方案，揭示AD是FP来源；UC2再比较降采样场景和投票方案，证明同一架构在不同数据频率下仍成立。每层对比都在回答前一层留下的不确定性。

### claim_evidence_ledger

#### 1. 1

- claim：系统在两个真实UC上100%检测出缺陷品。

- evidence：UC1/UC2所有投票和重采样/降采样条件下FNR均0，混淆矩阵见Fig.10c/d和Fig.11c/d。

- supported：是

- caveat：仅基于有限批次历史数据，未经历真实在线生产中的未知批次变异。

#### 2. 2

- claim：多阶段架构（AD+集成+投票）实现了零漏检，且AD是关键过滤层。

- evidence：组件误差比显示AD是主要FP来源；预研中15个正常样本被AD滤掉，集成层却可正确分类；UC2中集成层可能FN但被AD过滤。

- supported：是

- caveat：未对完整架构做逐层移除的正式消融实验，证据来自内部误差分解。

#### 3. 3

- claim：欧氏距离优于DTW，兼顾低FNR和实时性。

- evidence：UC1异常检测表显示欧氏距离k=50/200有最低FNR；运行时264.63ms vs 0.60ms。

- supported：是

- caveat：该比较主要基于正常数据验证，且未在UC2重复展示距离度量比较。

#### 4. 4

- claim：CAM可帮助操作者理解错误原因。

- evidence：Fig.7显示正常、Error 3、Error 4的激活区域有明确差异。

- supported：partial

- caveat：未进行操作者用户研究，只展示了可视化能力，未证明实际维护决策改善。

#### 5. 5

- claim：系统可在软实时约束内执行。

- evidence：UC1单样本3.109ms、20样本批量7.922ms；UC2两样本批量5.953ms，均低于150/200ms。

- supported：是

- caveat：不包括PLC通信延迟，且未在真实PLC上验证端到端通信。

#### 6. 6

- claim：系统为预测性过程监控提供基础。

- evidence：仅在引言和讨论中提出这一方向，没有预测性监控实验。

- supported：否

- caveat：属于未来工作宣称，不是本文实证贡献。

- internal_validity_strategy_cn：在预研中使用80/20独立测试集；超参数通过网格搜索和5折分层交叉验证选择；对误分类样本逐一追踪来源（AD vs 集成）；使用相同FNR/FPR指标和混淆矩阵；在UC1/UC2中控制重采样/降采样和投票方案。但由于数据是历史批次而非随机实验，无法排除批次混淆。

- external_validity_strategy_cn：选择两个真实且不同的工业用例：UC1为20个线性电机、40Hz、短信号；UC2为PPU、2kHz、长信号。这套对比证明系统不依赖单一数据形态，但两个UC仍来自同一公司/领域，且样本批次有限。

- what_is_not_actually_tested_cn：没有与现有QC系统并行在线部署；没有经历长期batch-to-batch变异；没有实施Gage R&R；没有验证未知错误类别的真实到达率；没有评估错误标签噪声；没有用户研究证明CAM和DT解释确实提升操作员决策；没有计算误拒经济损失。

## 贡献闭环

- technical_claim_cn：提出一个组合AD、DT、SVM、CNN和投票方案的ML质检系统，在预研和两个真实制药工业UC上均实现FNR=0，FPR分别为14.85%、9.04%、2.32%，且延迟低于150/200ms。

- artifact_claim_cn：分层接受规则是系统实现零漏检的关键：AD层先剔除未知/可疑样本，集成层提供多类错误诊断，投票层生成最终二值质量结论；证据显示AD贡献了几乎全部FP，而集成层能够完美区分已知类别。

- mechanism_claim_cn：机制上，系统利用正常样本聚类的距离阈值制造“严格通过”条件；任何无法明确匹配已知类别的样本都被拒绝，从而避免FN；多分类器和投票进一步保证单个模型不会造成漏检。

- boundary_claim_cn：该结果当前只适用于两个使用例中的有限批次；缺乏batch-to-batch变异、Gage R&R、错误标签和成本数据；系统仍处于可行性/早期开发阶段，不能直接推广到所有制药装配线。

- reusable_design_knowledge_cn：可复用的设计知识包括：将零缺陷要求转化为前置异常检测和保守投票；用FNR/FPR而非accuracy评估工业质检；用二值输出+多类输出分离质量判断和根因判断；用重采样/降采样适配不同采样率；用批量推理满足实时约束；用DT和Grad-CAM实现可解释性。

- theoretical_contribution_cn：理论上主要是填补应用空白：为制药行业提供首个已知的ML成品QC可行性研究；将时间序列分类、异常检测、集成学习和可解释性方法组合到零缺陷场景；提出向预测性过程监控延伸的框架，但没有提出新形式模型或行为理论。

- how_discussion_closes_intro_gap_cn：引言指出传统二值QC无法给出拒绝原因且ML在制药QC中缺失；结论和讨论用真实UC证据回应这一缺口：系统能区分错误类型、解释信号区域、在软实时下运行，并明确将局限性限定在早期可行性阶段。

- overclaim_or_unsupported_leaps_cn：“100%检测”是基于有限批次的离线结果，易被读作永久性能保证；将CAM解释为改善维护决策未经验证；称系统为“zero defect tolerance system”依赖AD的保守接受，但未证明所有未知错误都可被AD捕获；预测性过程监控属于未来愿景而非本文证明。

## 句级写作动作图谱

### 1. Abstract P1

- order：1

- section：Abstract

- locator：Abstract P1

- move_code：CONTEXT

- paraphrase_cn：自动制造行业中，建立可靠且低误拒的质量控制系统是重大挑战。

- rhetorical_function_cn：开场即确立问题的一般性和重要性。

- depends_on_cn：无，是文章的总体背景。

- sets_up_cn：为后文提出制药行业的特殊性和现有QC局限做铺垫。

- evidence_pointer：Abstract P1

### 2. Abstract P1

- order：2

- section：Abstract

- locator：Abstract P1

- move_code：PRACTICAL_STAKES

- paraphrase_cn：制药行业为保障所有放行产品的完整性，可以接受大量误拒。

- rhetorical_function_cn：强调零缺陷政策带来的现实代价，使问题更紧迫。

- depends_on_cn：依赖前一句关于QC挑战的铺垫。

- sets_up_cn：为后文选择FNR/FPR作为核心指标提供依据。

- evidence_pointer：Abstract P1

### 3. Abstract P1

- order：3

- section：Abstract

- locator：Abstract P1

- move_code：LIMITATION

- paraphrase_cn：标准QC系统主要做二分类，大多不提供拒收原因，因此设备退化或参数设置错误等根因常被忽略。

- rhetorical_function_cn：指出现有系统功能缺口，特别是根因信息缺失。

- depends_on_cn：问题背景和制药行业特殊性。

- sets_up_cn：引出后续对“可解释、多类错误区分”系统的主张。

- evidence_pointer：Abstract P1

### 4. Abstract P2

- order：4

- section：Abstract

- locator：Abstract P2

- move_code：RQ_OR_OBJECTIVE

- paraphrase_cn：本文提出一种基于成熟机器学习方法、能区分医疗产品装配过程中多种错误类型的数据驱动QC系统。

- rhetorical_function_cn：给出文章核心研究对象。

- depends_on_cn：需要前面指出传统QC的缺陷。

- sets_up_cn：后文详细说明系统结构和评价。

- evidence_pointer：Abstract P2

### 5. Abstract P2

- order：5

- section：Abstract

- locator：Abstract P2

- move_code：STUDY_OVERVIEW

- paraphrase_cn：系统在预研究和两个真实工业用例中展示功能，并讨论应用差异。

- rhetorical_function_cn：预告文章的三段式证据安排。

- depends_on_cn：研究对象已提出。

- sets_up_cn：让读者预期后续实验章节。

- evidence_pointer：Abstract P2

### 6. Abstract P2

- order：6

- section：Abstract

- locator：Abstract P2

- move_code：RESULT

- paraphrase_cn：在两个UC和有限批次中，系统不仅检测出100%缺陷品，还将误拒控制在可接受范围，并可作为软实时系统运行。

- rhetorical_function_cn：提前报告最高层级结果，建立贡献。

- depends_on_cn：系统方法已提出。

- sets_up_cn：为正文的指标和延迟测量提供目标。

- evidence_pointer：Abstract P2

### 7. Introduction P1

- order：7

- section：Introduction

- locator：Introduction P1

- move_code：CONTEXT

- paraphrase_cn：GMP条例要求制药制造商在任何时候都需证明其处于受控状态，因此投入大量质量保证工作，包括对注射装置等附加产品的装配。

- rhetorical_function_cn：将问题锚定在法规要求上。

- depends_on_cn：无，是引言起点。

- sets_up_cn：解释为什么零缺陷在制药装配中不可妥协。

- evidence_pointer：Introduction P1

### 8. Introduction P1

- order：8

- section：Introduction

- locator：Introduction P1

- move_code：PRACTICAL_STAKES

- paraphrase_cn：装配线每个步骤都有经过验证的QC站，一旦发生错误，对应的笔必须报废。

- rhetorical_function_cn：说明实际后果，使系统改进具有经济意义。

- depends_on_cn：GMP背景。

- sets_up_cn：引出传统QC的缺陷和误拒代价。

- evidence_pointer：Introduction P1 and Fig.1

### 9. Introduction P2

- order：9

- section：Introduction

- locator：Introduction P2

- move_code：LIMITATION

- paraphrase_cn：传统QC大多不采用数据驱动算法，而是用专家系统检查阈值，产品只在规则违反时报废，进行二分类“好/坏”。

- rhetorical_function_cn：归纳现有系统的技术局限。

- depends_on_cn：装配流程已描述。

- sets_up_cn：为数据驱动ML替代方案制造缺口。

- evidence_pointer：Introduction P2

### 10. Introduction P2

- order：10

- section：Introduction

- locator：Introduction P2

- move_code：LIMITATION

- paraphrase_cn：二值保守QC导致大量误拒、更高报废率和OEE损失；现代设备虽产生大量数据，但现有QC只使用简单硬编码规则。

- rhetorical_function_cn：扩展局限说明，指出数据未被充分利用。

- depends_on_cn：传统QC的阈值机制。

- sets_up_cn：引出ML利用已有数据的机会。

- evidence_pointer：Introduction P2

### 11. Introduction P3

- order：11

- section：Introduction

- locator：Introduction P3

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：研究和工业界已证明ML可用于质量控制和错误恢复；制药领域也有ML决策支持系统，但主要用于过程规划/优化而非实时质检；作者未发现制药行业ML成品QC先例。

- rhetorical_function_cn：综述文献并明确指出空白。

- depends_on_cn：前面对传统QC局限的讨论。

- sets_up_cn：用“已知研究”和“制药QC空白”构成双缺口。

- evidence_pointer：Introduction P3

### 12. Introduction P3

- order：12

- section：Introduction

- locator：Introduction P3

- move_code：LIMITATION

- paraphrase_cn：已有时间序列分类方法计算复杂度过高，不适合实时运行，且不区分FN和FP，可解释性差。

- rhetorical_function_cn：排除直接套用现有分类器方案的可行性。

- depends_on_cn：对ML相关工作的综述。

- sets_up_cn：为系统设计提出实时性、FN/FP权衡和可解释性要求。

- evidence_pointer：Introduction P3

### 13. Introduction P4

- order：13

- section：Introduction

- locator：Introduction P4

- move_code：WHY_GAP_MATTERS

- paraphrase_cn：在制药装配中使用ML可提取区分正常和不同错误类型的规则，即时反馈产线事件，支持更有依据的故障排查。

- rhetorical_function_cn：说明填补缺口会使谁受益、何种价值。

- depends_on_cn：前一句文献局限。

- sets_up_cn：引出论文贡献清单。

- evidence_pointer：Introduction P4

### 14. Introduction P5

- order：14

- section：Introduction

- locator：Introduction P5

- move_code：CONTRIBUTION

- paraphrase_cn：本文贡献是提出数据驱动的智能QC系统，作为实时DSS在150ms内提供当前失败的具体反馈，并用两个真实制药应用进行工业评价。

- rhetorical_function_cn：集中宣布三个贡献：系统、实时DSS、工业评估。

- depends_on_cn：前面对缺口和价值的论证。

- sets_up_cn：后文所有章节围绕这三点展开。

- evidence_pointer：Introduction P5

### 15. Introduction P6

- order：15

- section：Introduction

- locator：Introduction P6

- move_code：BOUNDARY_CONDITION

- paraphrase_cn：作者定位本工作为基础研究和可行性研究，更广视角是提供预测性过程监控的潜在框架。

- rhetorical_function_cn：降低读者对理论深度的期待，同时抬高未来意义。

- depends_on_cn：贡献声明。

- sets_up_cn：为讨论中的局限和未来研究方向埋下伏笔。

- evidence_pointer：Introduction P6

### 16. Introduction P7

- order：16

- section：Introduction

- locator：Introduction P7

- move_code：STUDY_OVERVIEW

- paraphrase_cn：说明文章剩余结构：方法学、UC、理论背景、系统构成、评价、局限和总结。

- rhetorical_function_cn：给出全文路线图。

- depends_on_cn：文章主体已计划好。

- sets_up_cn：读者按此顺序阅读。

- evidence_pointer：Introduction P7

### 17. Section 2 P1

- order：17

- section：Section 2 Research methodology

- locator：Section 2 P1

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：作者用Hevner等提出的IS设计科学研究指南来定位自己的工作，并逐条对照指南。

- rhetorical_function_cn：将工程制品论文框定为IS设计科学贡献。

- depends_on_cn：论文整体目标。

- sets_up_cn：让读者用设计科学标准评价后续构建与评估。

- evidence_pointer：Section 2 P1

### 18. Section 3 intro P1

- order：18

- section：Section 3 Industrial use cases

- locator：Section 3 intro P1

- move_code：REQUIREMENT

- paraphrase_cn：两个UC在过程中不同，但共同点是制药领域的质量目标：必须检测所有缺陷品，并将测量系统不确定性和批次变异纳入验收阈值。

- rhetorical_function_cn：强调领域需求，而非工艺本身，是该问题的共同约束。

- depends_on_cn：引言中GMP要求。

- sets_up_cn：为后续选择FNR/FPR指标提供领域依据。

- evidence_pointer：Section 3 intro P1

### 19. Section 3.1 P1

- order：19

- section：Section 3.1 UC1

- locator：Section 3.1 P1

- move_code：REQUIREMENT

- paraphrase_cn：UC1机器周期4秒，实际装配约1秒，因此质量预测必须在产品转到下一工位前完成，可用时间约150ms。

- rhetorical_function_cn：定量说明软实时要求。

- depends_on_cn：前面对QC目标的要求。

- sets_up_cn：后文延迟测量以150ms为基准。

- evidence_pointer：Section 3.1 P1

### 20. Section 3.1 P2

- order：20

- section：Section 3.1 UC1

- locator：Section 3.1 P2

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：作者搭建试验台，用相同硬件模拟装配过程，加装力传感器测量反力；通过FMEA和咨询制造者/操作者/领域专家确定典型失败场景。

- rhetorical_function_cn：解释训练数据为何可信、错误类别从何而来。

- depends_on_cn：需要真实系统但又不便直接大规模制造缺陷。

- sets_up_cn：为预研数据集和错误类别分类提供合法来源。

- evidence_pointer：Section 3.1 P2 and Fig.3

### 21. Section 3.1 P2

- order：21

- section：Section 3.1 UC1

- locator：Section 3.1 P2

- move_code：BOUNDARY_CONDITION

- paraphrase_cn：尽管力信号提供更多细节，但生产线上每工位加装力传感器可能不可行，因此分析限定于电机自身记录的数据。

- rhetorical_function_cn：预先设定系统适用边界：强调工业可实施性优先于信号丰富度。

- depends_on_cn：试验台信号分析结果。

- sets_up_cn：影响后续输入特征选择和UC1评价。

- evidence_pointer：Section 3.1 P2

### 22. Section 3.1 P3

- order：22

- section：Section 3.1 UC1

- locator：Section 3.1 P3

- move_code：LIMITATION

- paraphrase_cn：在真实机器上复现了三种失败类型；采集到的信号每条仅37-41个点，且速度反馈因PLC转换错误损坏。

- rhetorical_function_cn：暴露真实数据的限制，说明后续需要重采样和缺失通道处理。

- depends_on_cn：试验台后的真实机器实验。

- sets_up_cn：为UC1评价中的不同重采样场景提供理由。

- evidence_pointer：Section 3.1 P3 and Table 1

### 23. Section 3.2 P1

- order：23

- section：Section 3.2 UC2

- locator：Section 3.2 P1

- move_code：REQUIREMENT

- paraphrase_cn：UC2的装夹单元同时装配两个产品，机器周期2.4秒，装配约1.4秒，质量预测截止时间为200ms。

- rhetorical_function_cn：与UC1一样提供硬实时边界，形成跨场景对比。

- depends_on_cn：前面对制药质量目标的强调。

- sets_up_cn：后续以200ms作为延迟基准。

- evidence_pointer：Section 3.2 P1

### 24. Section 3.3 P1

- order：24

- section：Section 3.3 Differences between use cases

- locator：Section 3.3 P1

- move_code：CONTEXT

- paraphrase_cn：两个UC的主要差异是采样率和数据类型：UC1为40Hz，仅37-41点；UC2为2kHz，因独立采集系统而获得高分辨率。

- rhetorical_function_cn：概括两个评价场景的区别，为后续可迁移性做铺垫。

- depends_on_cn：两个UC介绍。

- sets_up_cn：后文分别使用重采样和降采样适应数据差异。

- evidence_pointer：Section 3.3 P1

### 25. Section 4.1 P1

- order：25

- section：Section 4.1 Process error classification

- locator：Section 4.1 P1

- move_code：MECHANISM

- paraphrase_cn：分类器可能犯两种错误：FP仅是经济损失，而FN意味着放行缺陷品，必须严格避免，因此用FNR和FPR作为主要评价指标。

- rhetorical_function_cn：建立评价指标的理论依据。

- depends_on_cn：制药质量控制需求。

- sets_up_cn：指导后续异常检测阈值和投票方案设计。

- evidence_pointer：Section 4.1 P1 and Eq.(1)-(2)

### 26. Section 4.2 P1

- order：26

- section：Section 4.2 Decision trees

- locator：Section 4.2 P1

- move_code：THEORY_INTRO

- paraphrase_cn：决策树通过分裂规则减小不纯度，生成的步骤列表易于理解，可向人类用户展示知识；但容易过拟合，需剪枝或限制深度。

- rhetorical_function_cn：说明为什么选择DT作为可解释组件。

- depends_on_cn：前面提出的可解释性需求。

- sets_up_cn：后文DT使用简单统计特征和最大深度限制。

- evidence_pointer：Section 4.2 P1

### 27. Section 4.3 P1

- order：27

- section：Section 4.3 Support vector machines

- locator：Section 4.3 P1

- move_code：THEORY_INTRO

- paraphrase_cn：SVM通过最大间隔超平面分离样本，核技巧解决非线性问题，预测阶段快，但数学函数导致可解释性有限。

- rhetorical_function_cn：为选择SVM作为第二分类器提供理论理由。

- depends_on_cn：实时和鲁棒性需求。

- sets_up_cn：后文SVM使用标准化全序列并与其他模型集成。

- evidence_pointer：Section 4.3 P1

### 28. Section 4.4 P1

- order：28

- section：Section 4.4 Convolutional neural networks

- locator：Section 4.4 P1

- move_code：THEORY_INTRO

- paraphrase_cn：CNN尤其适合处理图像或时间序列这类网格状数据，通过卷积核移动提取局部模式，池化提高对噪声的鲁棒性。

- rhetorical_function_cn：为选择CNN作为时间序列分类器提供依据。

- depends_on_cn：时间序列信号特性。

- sets_up_cn：后文自定义CNN用于集成。

- evidence_pointer：Section 4.4 P1

### 29. Section 4.4 P2-P3

- order：29

- section：Section 4.4 Convolutional neural networks

- locator：Section 4.4 P2-P3

- move_code：THEORY_INTRO

- paraphrase_cn：Grad-CAM通过梯度池化得到类别权重并生成类激活图，可定位输入区域对预测的影响；方法可扩展至一维数据。

- rhetorical_function_cn：说明CNN黑箱如何被打开。

- depends_on_cn：CNN选择。

- sets_up_cn：后文用CAM展示错误类别的信号区域。

- evidence_pointer：Section 4.4 P2-P3 and Eq.(3)-(4)

### 30. Section 5 intro P1

- order：30

- section：Section 5 Structure of the proposed algorithm

- locator：Section 5 intro P1

- move_code：REQUIREMENT

- paraphrase_cn：系统必须将样本分入多个类别，但对正常类设置更严格条件，因为正常类误判会带来严重后果；这一要求被嵌入算法结构。

- rhetorical_function_cn：把零漏检需求转成结构约束。

- depends_on_cn：Section 4.1的错误类型论述。

- sets_up_cn：引出多层过滤架构。

- evidence_pointer：Section 5 intro P1 and Fig.5

### 31. Section 5 intro P1

- order：31

- section：Section 5 Structure of the proposed algorithm

- locator：Section 5 intro P1

- move_code：DESIGN_FEATURE

- paraphrase_cn：新样本经过多个阶段评估，每一层都可筛出样本；各层单独优化，因为全局参数空间过大。

- rhetorical_function_cn：说明架构的可组合性和工程可行性。

- depends_on_cn：上一句的结构约束。

- sets_up_cn：后文依次介绍AD、集成、投票。

- evidence_pointer：Section 5 intro P1 and Fig.5

### 32. Section 5.1 P1

- order：32

- section：Section 5.1 Anomaly detection

- locator：Section 5.1 P1

- move_code：DESIGN_FEATURE

- paraphrase_cn：训练数据之外几乎必然出现未知错误；普通分类器会把未知样本归入已知类，因此先对正常数据做k-means聚类，用距离阈值把异常样本排除。

- rhetorical_function_cn：为AD层提供操作机制。

- depends_on_cn：零缺陷政策要求。

- sets_up_cn：解释AD为何是本系统FNR控制的关键。

- evidence_pointer：Section 5.1 P1

### 33. Section 5.1 P2-P3

- order：33

- section：Section 5.1 Anomaly detection

- locator：Section 5.1 P2-P3

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：AD的阈值用ROC曲线和Youden指数确定，并比较欧氏距离与DTW；UC1中欧氏距离因低FNR和O(n)复杂度而入选。

- rhetorical_function_cn：为距离度量和阈值选择提供数据和复杂度依据。

- depends_on_cn：AD机制。

- sets_up_cn：展示具体优化示例和表2结果。

- evidence_pointer：Section 5.1 P2-P3, Fig.6, Table 2

### 34. Section 5.1 P3

- order：34

- section：Section 5.1 Anomaly detection

- locator：Section 5.1 P3

- move_code：RESULT

- paraphrase_cn：DTW在k=100时整体最优，但欧氏距离k=50和k=200有最低FNR；欧氏距离运行时间为0.60ms，DTW为264.63ms，因此只考虑欧氏距离。

- rhetorical_function_cn：报告选择结论，强调实时性压倒细微准确率差异。

- depends_on_cn：表2和运行时间测量。

- sets_up_cn：固定AD参数，进入集成分类器设计。

- evidence_pointer：Section 5.1 P3, Table 2

### 35. Section 5.2 P1

- order：35

- section：Section 5.2 Ensemble classifier

- locator：Section 5.2 P1

- move_code：DESIGN_FEATURE

- paraphrase_cn：集成步骤对已被AD判定为故障的样本仍应用，以获取拒收原因；使用多个分类器而非单一分类器，并用网格搜索和5折交叉验证优化超参数。

- rhetorical_function_cn：解释为什么需要集成和如何选择模型。

- depends_on_cn：AD层已提出。

- sets_up_cn：随后逐个介绍DT、SVM、CNN。

- evidence_pointer：Section 5.2 P1

### 36. Section 5.2.1 P1

- order：36

- section：Section 5.2.1 Decision tree

- locator：Section 5.2.1 P1

- move_code：DESIGN_FEATURE

- paraphrase_cn：DT不直接使用全时间序列，而是对每个变量和窗口计算六个简单统计特征，以最大化可解释性。

- rhetorical_function_cn：说明可解释树的具体设计选择。

- depends_on_cn：DT理论中的可解释性优势。

- sets_up_cn：后文将DT与其他模型集成。

- evidence_pointer：Section 5.2.1 P1

### 37. Section 5.2.2 P1

- order：37

- section：Section 5.2.2 Support vector machine

- locator：Section 5.2.2 P1

- move_code：DESIGN_FEATURE

- paraphrase_cn：SVM适合高维数据，因此训练在全时间序列上；由于输入尺度敏感，需标准化，使所有变量被同等对待。

- rhetorical_function_cn：说明SVM输入设计和预处理原因。

- depends_on_cn：SVM理论中的核/尺度敏感性。

- sets_up_cn：后文SVM作为集成第二个估计器。

- evidence_pointer：Section 5.2.2 P1

### 38. Section 5.2.3 P1-P2

- order：38

- section：Section 5.2.3 Convolutional neural network

- locator：Section 5.2.3 P1-P2

- move_code：DESIGN_FEATURE

- paraphrase_cn：CNN不仅看单个输入值，还考虑相邻点关系，适合时序数据；作者设计自定义CNN，并使用一维Grad-CAM展示类别定位。

- rhetorical_function_cn：说明CNN为何入选及可解释性如何实现。

- depends_on_cn：CNN/Grad-CAM理论背景。

- sets_up_cn：后文用CAM图说明错误类别的识别区域。

- evidence_pointer：Section 5.2.3 P1-P2 and Fig.7

### 39. Section 5.3 P1-P2

- order：39

- section：Section 5.3 Voting scheme

- locator：Section 5.3 P1-P2

- move_code：DESIGN_FEATURE

- paraphrase_cn：比较多数投票、veto投票和元分类器；veto方案中单个分类器可阻止最终判定，保守但系统准确度受最差分类器限制；堆叠可提高准确率。

- rhetorical_function_cn：列出并解释三种投票机制。

- depends_on_cn：集成分类器已构建。

- sets_up_cn：后文预研中的投票比较实验。

- evidence_pointer：Section 5.3 P1-P2

### 40. Section 5.3 P3

- order：40

- section：Section 5.3 Voting scheme

- locator：Section 5.3 P3

- move_code：RESULT

- paraphrase_cn：预研测试中所有投票方案都得到FNR=0和FPR=14.85%；15个正常样本被AD层误判，但集成层能正确识别；这些样本可能与错误类曲线相似，系统因不确定而将其剔除。

- rhetorical_function_cn：报告预研最核心结果，并解释FP来源。

- depends_on_cn：预研数据切分和训练。

- sets_up_cn：为系统同时输出二值和多类预测提供证据。

- evidence_pointer：Section 5.3 P3 and Fig.8

### 41. Section 5.3 P4

- order：41

- section：Section 5.3 Voting scheme

- locator：Section 5.3 P4

- move_code：DESIGN_FEATURE

- paraphrase_cn：系统生成两个预测：用于实际QC的二值分类和提供错误模式可能原因的多类分类；meta DT的混淆矩阵展示了最终结果。

- rhetorical_function_cn：说明系统输出结构。

- depends_on_cn：投票方案比较。

- sets_up_cn：读者接下来会在UC评价看到类似混淆矩阵。

- evidence_pointer：Section 5.3 P4 and Fig.9

### 42. Section 5.3 P5

- order：42

- section：Section 5.3 Voting scheme

- locator：Section 5.3 P5

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：为控制FP，作者在异常检测阈值和网格搜索中关注总体准确率而非严格零FN策略；不同投票方案的比较表明，某些情况下veto甚至不是达到零FN所必需的，民主投票可能FP更少。

- rhetorical_function_cn：解释设计权衡，防止读者误以为所有阈值都取零FN。

- depends_on_cn：预研投票结果。

- sets_up_cn：为UC评价中选择非零FN被牺牲的设计留下说明。

- evidence_pointer：Section 5.3 P5

### 43. Section 6.1 P1

- order：43

- section：Section 6.1 UC1 evaluation

- locator：Section 6.1 P1

- move_code：RESULT

- paraphrase_cn：UC1中重采样到38点效果最好；民主投票和meta DT给出最佳FPR=9.04%；添加数值求导速度仅在meta SVM时改善。

- rhetorical_function_cn：报告第一个真实UC的主要分类性能。

- depends_on_cn：系统训练和重采样方案。

- sets_up_cn：随后拆解FP来源和延迟。

- evidence_pointer：Section 6.1 P1 and Fig.10a

### 44. Section 6.1 P2

- order：44

- section：Section 6.1 UC1 evaluation

- locator：Section 6.1 P2

- move_code：RESULT

- paraphrase_cn：AD层是UC1中所有15个FP的来源；使用民主投票时集成层达到完美分类。

- rhetorical_function_cn：通过组件误差分解，明确系统哪一部分产生误检。

- depends_on_cn：图10b/c/d。

- sets_up_cn：为讨论AD的改进方向提供证据。

- evidence_pointer：Section 6.1 P2 and Fig.10b-d

### 45. Section 6.1 P3

- order：45

- section：Section 6.1 UC1 evaluation

- locator：Section 6.1 P3

- move_code：RESULT

- paraphrase_cn：延迟测量显示单样本平均3.109ms，20样本批量处理7.922ms，远低于150ms截止。

- rhetorical_function_cn：证明软实时可行性。

- depends_on_cn：100次时间测量。

- sets_up_cn：UC2将重复相同测量以确认可迁移。

- evidence_pointer：Section 6.1 P3 and Fig.10e

### 46. Section 6.2 P1

- order：46

- section：Section 6.2 UC2 evaluation

- locator：Section 6.2 P1

- move_code：RESULT

- paraphrase_cn：UC2中所有测试FNR=0；降采样到200点时FPR最优为2.32%；veto方案在100点时略差。

- rhetorical_function_cn：报告第二个真实UC的核心性能。

- depends_on_cn：系统在UC2数据上的训练/测试。

- sets_up_cn：随后拆解组件误差和延迟。

- evidence_pointer：Section 6.2 P1 and Fig.11a

### 47. Section 6.2 P2

- order：47

- section：Section 6.2 UC2 evaluation

- locator：Section 6.2 P2

- move_code：RESULT

- paraphrase_cn：AD比集成层产生更多误分类；尽管集成层可能做出FN预测，最终结果中FN不存在，因为AD将其过滤。

- rhetorical_function_cn：强化AD层在零漏检中的必要作用。

- depends_on_cn：组件误差分解和混淆矩阵。

- sets_up_cn：说明系统级FN保护来自层间组合，而非单独模型。

- evidence_pointer：Section 6.2 P2 and Fig.11b-d

### 48. Section 6.2 P3

- order：48

- section：Section 6.2 UC2 evaluation

- locator：Section 6.2 P3

- move_code：RESULT

- paraphrase_cn：延迟测量显示两个样本批量处理平均5.953ms，低于200ms截止。

- rhetorical_function_cn：证明高采样率场景下仍然满足软实时。

- depends_on_cn：100次时间测量。

- sets_up_cn：支持跨UC的实时性结论。

- evidence_pointer：Section 6.2 P3 and Fig.11e

### 49. Section 7 P1

- order：49

- section：Section 7 Discussion

- locator：Section 7 P1

- move_code：LIMITATION_AND_FUTURE

- paraphrase_cn：系统仍处早期开发阶段：错误聚类基于FMEA；应加入长期生产中的batch-to-batch变异并开展Gage R&R；当前可作为监控和针对性故障排查工具，未来可支持预测性过程监控。

- rhetorical_function_cn：明确结果边界并指向未来方向。

- depends_on_cn：两UC评价结果。

- sets_up_cn：保护贡献不被视为成熟可推广系统。

- evidence_pointer：Section 7 P1

### 50. Section 7 P1

- order：50

- section：Section 7 Discussion

- locator：Section 7 P1

- move_code：BOUNDARY_CONDITION

- paraphrase_cn：错误标记的样本可能显著增加误拒，因为模型有意表现保守；误拒产品的成本也未纳入本概念验证。

- rhetorical_function_cn：补充两个额外边界：标签质量和经济成本。

- depends_on_cn：系统保守设计。

- sets_up_cn：为未来数据清洗和成本建模留空间。

- evidence_pointer：Section 7 P1

### 51. Section 8 P1-P2

- order：51

- section：Section 8 Conclusions

- locator：Section 8 P1-P2

- move_code：CONTRIBUTION

- paraphrase_cn：作者总结开发并评价了制药自动化装配线的ML QC系统：与传统系统不同，它能区分多种失败并提供额外见解；多层设计旨在防止缺陷件被误判为正常；AD、集成和投票组成最终系统，且推理可被人理解。

- rhetorical_function_cn：重述核心贡献和系统闭环。

- depends_on_cn：全文方法和结果。

- sets_up_cn：为最终局限和未来实施步骤收尾。

- evidence_pointer：Section 8 P1-P2

### 52. Section 8 P3

- order：52

- section：Section 8 Conclusions

- locator：Section 8 P3

- move_code：BOUNDARY_CONDITION

- paraphrase_cn：在两个工业应用中，基于少量测试批次训练时系统能100%识别缺陷品；目前处于早期开发，需更多反映生产环境变异的数据；但执行时间远低于最大可接受延迟，具备软实时控制潜力。

- rhetorical_function_cn：在贡献声明后立即限定范围。

- depends_on_cn：两UC结果。

- sets_up_cn：避免读者过度推广。

- evidence_pointer：Section 8 P3

### 53. Section 8 P4

- order：53

- section：Section 8 Conclusions

- locator：Section 8 P4

- move_code：LIMITATION_AND_FUTURE

- paraphrase_cn：真实产线实施的第一步是与现有QC并行运行，待新系统充分训练并展示质量判断能力后再完全替换旧系统。

- rhetorical_function_cn：给出从研究到部署的路径。

- depends_on_cn：前面所有可行性证据。

- sets_up_cn：以务实实施计划结束全文。

- evidence_pointer：Section 8 P4

## 写作技术

- gap_construction_cn：先立法规和行业现实（GMP、零缺陷、误拒成本），再指出传统QC的二值/阈值局限，随后用文献说明ML在其他行业可行但制药QC空缺、时间序列分类虽先进却不适于实时和FN/FP权衡，由此形成“现实需要+技术可行+专有空白”的三重缺口。

- signposting_cn：摘要直接用“贡献是…”，引言末尾预告全文结构；方法学用Hevner指南作为评审框架；第3、4、5、6、7节分别以明确功能词开头（UC、理论背景、算法结构、评价、讨论），使读者始终知道每个部分承担什么论证任务。

- transition_logic_cn：从一般问题到需求再到数据/UC；从理论到每个算法组件；从组件到集成投票；从预研到UC1再UC2，每个转变句都回答上一个阶段留下的不确定性问题。

- claim_evidence_rhythm_cn：每次提出一个设计选择（如AD、SVM标准化、欧氏距离、投票方案），随后立即给出评价指标或对比表；主要结论用混淆矩阵、FNR/FPR和延迟测量承接，不在讨论中空泛重复。

- benchmark_narrative_cn：没有外部benchmark，而是把内部组件和参数变体作为对照链：预研比较投票和算法；UC1比较重采样和投票；UC2比较降采样和投票。每个对照都嵌入系统评价，使“选哪个”成为论证的一部分。

- theory_return_cn：理论主要用于设计推导而非解释结果；讨论和结论将结果回接到“可行性研究”“预测性过程监控框架”等引言中的更大愿景，说明本研究是长期研究计划的第一步。

- contribution_positioning_cn：将贡献定位为“数据驱动的QC系统+两个真实工业应用评价+允许市场批准的GMP设计”，同时强调是地基性/可行性研究，避免宣称完整理论或正式设计原则。

- novelty_protection_cn：通过“小批次”“早期开发”“需更多变异数据”“未考虑成本”等边界声明，把结果框定为特定条件下的证明；同时用“与现有QC并行测试”作为未来计划，使贡献不会退化为一次性性能报告。

## 可复用研究与写作程序

### structure_steps

#### 1. 1

- step：1

- writing_job_cn：用管制要求和产线流程建立问题背景，说明误拒/漏检的后果。

- research_job_cn：收集行业标准、真实装配流程、当前QC实现方式及领域专家输入。

- required_evidence_cn：可引用的监管要求、真实流程描述和传统QC的具体限制。

- transition_to_next_cn：从“现有系统做不到什么”转向“系统应该满足什么需求”。

#### 2. 2

- step：2

- writing_job_cn：把零缺陷、低误拒、实时性和根因信息转换成系统需求。

- research_job_cn：通过FMEA/专家访谈确定错误类别和可用信号，量化时间预算。

- required_evidence_cn：至少一个真实或受控数据源能区分正常和若干错误类；明确的延迟上限。

- transition_to_next_cn：需求条目逐项对应算法组件。

#### 3. 3

- step：3

- writing_job_cn：简述所用ML理论，并说明每个理论如何映射到一个组件或设计选择。

- research_job_cn：实现候选算法，设计特征/标准化/网络结构，定义FNR/FPR和延迟指标。

- required_evidence_cn：每个组件有理论依据；至少有一个方案可权衡（如距离度量）。

- transition_to_next_cn：进入受控预研对设计选项做初筛。

#### 4. 4

- step：4

- writing_job_cn：报告预研数据集、训练/测试切分、投票比较、组件误差、ROC/Youden阈值和可解释性图。

- research_job_cn：在试验台或小样本上执行离线实验、交叉验证、误分类样本追踪。

- required_evidence_cn：FNR=0且FPR可接受；至少确定一个关键设计选项（如meta DT）。

- transition_to_next_cn：把选定的系统迁移到第一个真实工业数据。

#### 5. 5

- step：5

- writing_job_cn：逐UC描述数据形态、预处理选项、投票方案、混淆矩阵、FNR/FPR和延迟。

- research_job_cn：在真实历史数据上重采样/降采样训练测试，并做运行时测量。

- required_evidence_cn：两个UC都满足FNR=0、FPR可接受和软实时；最好有一个UC间差异。

- transition_to_next_cn：两个UC结果合并进入局限与泛化讨论。

#### 6. 6

- step：6

- writing_job_cn：明确小批量、缺少长期变异、标签噪声、未考虑成本等边界，并提出未来部署/预测性监控方向。

- research_job_cn：梳理数据收集和验证场景的限制，设计下一步并线验证。

- required_evidence_cn：诚实的边界声明和可被执行的下一个实验。

- transition_to_next_cn：完成从具体结果到可复用设计知识的收束。

### most_transferable_moves_cn

1. 用FNR/FPR而非accuracy作为制造质检主指标

2. 需求-组件-评价一一对应

3. 预研选型+两个真实用例验证的阶梯式证据

4. 异常检测前置处理未知错误

5. 二值与多类双输出兼顾质量判断与根因解释

6. 延迟测量证明软实时可行

7. 明确可行性研究的边界

### resource_intensive_or_nonstandard_parts_cn

1. 真实的制药装配线数据和PLC/DCS集成，通常来自企业保密协议

2. 试验台改造和力传感器标定

3. FMEA和领域专家访谈

4. 两个不同工厂/产线的错误样本获取

5. 在真实机器上人为复现失败类型

6. 与产线PLC通信的端到端集成验证

### what_not_to_copy_superficially_cn

1. 没有真实错误标签和多类样本，不能宣称FNR=0

2. 没有逐一检验AD/集成/投票，不能把100%检测归因于架构

3. 没有测量延迟，不能声称软实时

4. 没有两个不同UC或批次外数据，不能泛化

5. 只写Hevner列表而无系统构建/评价，不是设计科学贡献

- single_best_description_of_the_routine_cn：把一个严格质检场景的规则缺陷转成零漏检+可接受误检+可解释+软实时的多层机器学习制品，并先用实验室数据确定组件，再用两个真实工业用例证明其可行与边界。

## 分析边界

解析以OCR全文为基础，部分图片和表内数字无法逐格读取（尤其混淆矩阵中FPR具体数值），因此位置标识为章节级近似；对工程术语解释可能有简化；未复制原文长句，全部采用中文转述。
