# Simpler is better: Lifting interpretability-performance trade-off via automated feature engineering

- 作者：Alicja Gosiewska; Anna Kozak; Przemysław Biecek
- 年份 / 期刊：2021 / Decision Support Systems
- DOI：10.1016/j.dss.2021.113556
- 源文件：19762_2021_simpler-is-better-lifting-interpretability-performance-trade-off-via-automated-feature-engineeri.md
- 论文主类型：build_evaluate_design_science
- 主导写作弧线：requirements_build_evaluate_design_principles
- 置信度：0.75

## 文章级论证概况

- 核心问题：如何在无需牺牲预测性能的前提下，自动构建更简单、更可解释的决策支持模型，从而真正提升可解释性与性能之间的权衡？

- 制品与设计：提出SAFE ML框架：以任意复杂黑盒模型（如gbm、svm）作为监督模型，从其中提取变量变换知识；对连续变量用PDP/ALE曲线和PELT变点检测进行分箱，对分类变量用层次聚类合并类别；再基于原始变量加SAFE变换后的二元特征训练逻辑回归/线性回归等玻璃盒模型。

- 客观结果：在信用数据use case中，SAFE逻辑回归AUC 0.82，优于原版逻辑回归0.78，参数数从49降至25，且不低于调优gbm的0.80；在30个OpenML数据集的基准中，SAFE模型相对复杂监督模型AUC无显著下降，而可解释性显著提升，并在部分数据集上超过复杂监督模型。

- 核心贡献：作者声称：从复杂模型中自动提取特征工程知识可以训练出保持甚至提升性能的可解释玻璃盒模型；这质疑了“复杂模型一定优于简单模型”的常见信念；提出了满足高性能、可审计、可解释、自动化四项要求的可解释DSS构建框架。

- 整篇论证链：作者从高风险决策中黑盒模型引发信任问题出发，引Rudin观点说明准确率与可解释性的权衡可能是迷思，并归纳可信决策支持系统的四个要求。随后指出现有post-hoc解释不可靠且可解释模型构建成本高，特征工程又高度依赖领域专家，因此需要自动化方法。作者据此设计SAFE ML框架：用灵活黑盒监督模型捕捉非线性关系，通过PDP/ALE和PELT、层次聚类将它们转成可解释的二元特征，再训练简单玻璃盒模型。先用credit-g数据集进行use case，展示AUC与参数数量同时改善；再用30个OpenML数据集做大规模基准，比较原版逻辑回归、复杂监督模型和SAFE逻辑回归，以AUC和基于参数数量的可解释性指标评价，并用Wilcoxon检验证明性能无显著下降、可解释性显著提升。讨论部分将结果回扣到四项需求，并把“更简单的模型有时更优”作为一般设计知识提出，同时承认未处理高阶交互等边界。

## 类型与写作弧线判定

- 论文主类型判定：论文的核心是一套框架和算法制品（SAFE ML/SAFE），按照需求—构建—评价—设计知识的组织方式展开：先提出四项可信要求，再构建六步框架并形式化，然后用use case和30数据集基准评价，最后把结果归纳为可复用设计知识。虽以benchmark为主要证据，但论证重心是设计制品而非单纯的计算性能竞赛。

- 主导写作弧线判定：文章明确列出高性能、可审计、可解释、自动化四项要求，围绕这些要求构建SAFE ML框架，用use case和benchmark评价，并在讨论中逐条证明框架满足要求，最后提炼出关于可解释模型构建的设计知识。

## 研究开展程序

- study_or_phase_count：3

- 研究阶段总序列：第一阶段是概念与算法设计：建立SAFE ML框架并给出形式化目标；第二阶段是单一真实数据use case，证明框架在信用评分场景下有效且能生成可解释变换；第三阶段是30个OpenML数据集的大规模基准，把结论从单场景推广到多数据集，并用统计检验支撑绩效不下降、可解释性提升的主张。三个阶段形成从制品到示例再到泛化证据的累积论证链。

### studies_or_phases

#### 1. SAFE ML框架设计与形式化阶段

- order：1

- name_cn：SAFE ML框架设计与形式化阶段

- question_cn：如何从黑盒模型中自动提取可解释的特征变换，并形式化地训练简单玻璃盒模型？

- inputs_and_setting_cn：概念性输入：原始表格数据X、任意监督模型M、正则化惩罚λ；无经验数据。

- designed_or_compared_object_cn：设计SAFE ML六步流程、SAFE特征变换函数、Algorithm 1和Algorithm 2。

- baseline_control_or_counterfactual_cn：未设置实证对照；以“原版逻辑回归无法捕捉U形和非单调关系”作为隐式反事实。

##### objective_metrics

1. 损失函数L（准确性、交叉熵或RMSE）

2. 变换后特征的二元表示长度

3. 玻璃盒模型参数数量

- analysis_method_cn：数学形式化：定义transformer函数、partial dependence profile、glass box目标函数；用PELT和层次聚类作为具体变换算法。

- main_result_cn：得到可复现的六步框架和两个算法；SAFE变换把连续变量转成带变点的分段二元特征，把分类变量转成合并后的二元特征。

- argumentative_role_cn：建立制品本身，让后续经验评价有明确对象；也说明特征变换如何由监督模型自动学习。

- remaining_uncertainty_cn：尚无任何经验证据证明该框架真的能保持性能或提升可解释性。

- link_to_next_phase_cn：需要用真实数据演示框架运行和产出，因此进入credit-g use case。

##### evidence_pointers

1. Section 3.1 Fig. 1六步图

2. Section 3.2定义部分

3. Section 3.3 Algorithm 1和Algorithm 2

4. Fig. 2 SAFE方法图示

#### 2. 信用数据use case阶段

- order：2

- name_cn：信用数据use case阶段

- question_cn：在真实信用评分数据上，SAFE ML能否生成可解释变换，并让逻辑回归同时改善AUC和降低参数数量？

- inputs_and_setting_cn：credit-g/German Credit数据集，OpenML task 31的9:1训练测试划分；调优后的gbm监督模型。

- designed_or_compared_object_cn：SAFE变换特征；基于SAFE特征训练的逻辑回归；比较原版逻辑回归、gbm监督模型、SAFE逻辑回归。

- baseline_control_or_counterfactual_cn：原版逻辑回归作为基线；调优gbm作为复杂模型对照；仅用变换特征vs原始+变换特征。

##### objective_metrics

1. AUC

2. 模型参数数量

3. 可解释性=参数数量的倒数

- analysis_method_cn：可视化PDP和合并树；比较AUC和参数数量；用bias-variance解释gbm可能过拟合。

- main_result_cn：SAFE逻辑回归AUC 0.82，参数25；原版逻辑回归AUC 0.78，参数49；调优gbm AUC 0.80但参数约171,616；SAFE同时提升AUC和可解释性。

- argumentative_role_cn：作为可行性证明，说明框架能从复杂模型中提取有意义的非线性变换，并转化为更简单且更准确的线性模型。

- remaining_uncertainty_cn：单数据集结果可能只是偶然；没有检验多种监督模型和多种数据形态。

- link_to_next_phase_cn：需要多数据集基准来排除单数据集偶然性，并检验SAFE在不同监督模型下的稳健性。

##### evidence_pointers

1. Section 4.1

2. Fig. 3

3. Fig. 4

4. Table 2

#### 3. OpenML 30数据集基准阶段

- order：3

- name_cn：OpenML 30数据集基准阶段

- question_cn：在更广泛的数据集上，SAFE特征工程是否普遍保持复杂模型性能且显著提升可解释性？复杂模型是否总是优于简单模型？

- inputs_and_setting_cn：OpenML100中30个无缺失值二分类数据集；每个任务10个train/test splits；默认svm、默认gbm、调优gbm作为监督模型。

- designed_or_compared_object_cn：原版逻辑回归、默认svm、默认gbm、调优gbm、SAFE gbm default、SAFE gbm tuned、SAFE svm。

- baseline_control_or_counterfactual_cn：原版逻辑回归作为基线；复杂模型作为监督模型；SAFE模型作为处理；以10次固定split重复控制划分变异。

##### objective_metrics

1. AUC

2. 模型参数数量

3. 可解释性=参数数量的倒数

4. Wilcoxon秩和检验p值

- analysis_method_cn：三元图展示三模型相对排序；灰色箭头图展示可解释性-性能位移；Wilcoxon秩和检验比较AUC和可解释性差异。

- main_result_cn：SAFE模型与各监督模型相比AUC均无显著下降（p>0.05），可解释性显著提升（p<0.001）；部分数据集上SAFE逻辑回归超过复杂监督模型，进入三元图红区，说明“复杂模型未必优于简单模型”。

- argumentative_role_cn：把use case的单一证据扩展为一般性结论，提供外部效度；同时识别出SAFE并非总能超越原版逻辑回归的边界条件。

- remaining_uncertainty_cn：只测试了二分类表格数据、逻辑回归作为玻璃盒、未处理高阶交互；没有真实用户或组织部署的证据。

- link_to_next_phase_cn：在讨论部分把这些证据回扣到四项需求，并在未来工作提出处理交互特征的扩展方向。

##### evidence_pointers

1. Section 4.2

2. Table 3

3. Table 4

4. Fig. 5

5. Fig. 6

6. Table 5

## 各部分修辞架构

### abstract_moves

1. CONTEXT：ML能产生有用预测模型并可支持决策，AutoML使复杂模型容易构建。

2. PRACTICAL_STAKES：复杂模型在高风险决策中造成有害、不公平或错误决策。

3. RQ_OR_OBJECTIVE：在保持性能的同时简化复杂模型，提升透明度。

4. STUDY_OVERVIEW：提出基于弹性黑盒监督模型的SAFE ML框架，以合成特征训练玻璃盒模型；用OpenML大规模基准和信用真实数据应用，报告三个主要结果。

### introduction_moves

1. CONTEXT：模型信任成为关键问题，复杂模型影响贷款、治疗、警务等决定。

2. PRACTICAL_STAKES：盲目使用ML引发事故、歧视、错误预测，导致尤其金融等监管行业抵触复杂模型。

3. PRIOR_KNOWLEDGE：Rudin指出准确率与可解释性权衡是迷思；可解释模型简单且易验证但构建成本高。

4. REQUIREMENT：提出可信系统的四项要求：高性能、可审计、可解释、自动化。

5. RQ_OR_OBJECTIVE：介绍SAFE ML框架，用复杂监督模型学习可解释特征工程，最终训练透明玻璃盒模型。

6. STUDY_OVERVIEW：说明全文结构。

### theory_and_knowledge_moves

1. PRIOR_KNOWLEDGE：GDPR和可信AI伦理指南使可解释性成为设计系统的一部分。

2. PRIOR_KNOWLEDGE：post-hoc解释方法包括规则、树、PDP、ALE、LIME、SHAP、BreakDown。

3. LIMITATION：post-hoc解释是模型简化，可能不准确且缺乏统一保真度度量。

4. LIMITATION：可解释模型虽然结构已知，但参数过多时也会变得不透明。

5. PRIOR_KNOWLEDGE：特征工程在金融、保险、医疗等领域很关键，但成熟领域主要依赖领域知识。

6. LIMITATION：已有自动数据变换方法耗时且常不如人工，且生成特征难以解释。

7. GAP：需要一种能自动从复杂黑盒中提取可解释特征并用于简单模型的方法。

### artifact_design_moves

1. STUDY_OVERVIEW：提出六步SAFE ML框架。

2. DESIGN_FEATURE：第一步接受原始表格数据，无需预处理。

3. DESIGN_FEATURE：第二步训练任意复杂监督模型，目的是提取特征知识。

4. DESIGN_FEATURE：第三步用PDP/ALE变点检测和层次聚类生成SAFE变换。

5. DESIGN_FEATURE：第四步可选特征选择，第五步拟合逻辑回归/线性模型，第六步给出直接解释。

6. MECHANISM：分箱连续变量可把非线性关系带入线性模型，合并分类水平可减少参数。

### evaluation_moves

1. METHOD_JUSTIFICATION：用AUC作为性能度量，用参数数量的倒数作为可解释性度量。

2. BENCHMARK_OR_CONTRAST：选择credit-g use case和30个OpenML二分类数据集。

3. BENCHMARK_OR_CONTRAST：对比原版逻辑回归、默认svm、默认gbm、调优gbm和对应SAFE模型。

4. RESULT：use case中SAFE逻辑回归AUC和可解释性同时提升。

5. RESULT：基准中SAFE相对复杂监督模型AUC无显著下降、可解释性显著提升。

6. BOUNDARY_CONDITION：部分数据集中SAFE未能超越原版逻辑回归，且复杂监督模型并非总优于逻辑回归。

7. ROBUSTNESS_OR_BOUNDARY_TEST：Wilcoxon检验支持主要主张。

### discussion_and_contribution_moves

1. TRANSITION：从“信任或不用”两难回到研究目标。

2. CONTRIBUTION：SAFE ML框架满足四项要求。

3. CONTRIBUTION：use case说明金融等监管领域可用可解释模型替代黑盒。

4. CONTRIBUTION：基准表明自动特征工程可让线性模型达到甚至超过复杂模型。

5. BOUNDARY_CONDITION：SAFE只处理单个特征，尚未捕捉高阶交互。

6. LIMITATION_AND_FUTURE：未来工作可针对随机森林/xgboost等模型提取交互特征。

7. OTHER：软件和复现资源。

## 理论/知识到设计的翻译

### 知识/理论基础

1. 可解释机器学习中的glass box与black box概念

2. Rudin关于可解释性与性能权衡是迷思的论断

3. post-hoc解释的保真度问题

4. 特征工程和数据变换文献

5. partial dependence profile和ALE方法

6. 变点检测PELT算法

7. 层次聚类

8. bias-variance tradeoff

9. 用参数数量反向衡量可解释性的做法

- 理论—设计耦合：partial

- 耦合判定理由：Rudin论点、bias-variance等一般性知识影响了问题定位、评价维度和事后解释，但SAFE的具体算法选择（PELT、层次聚类、PDP/ALE）主要来自已有工程方法和技术文献，而非由某个形式理论前瞻性推导。因此是部分耦合而非直接理论驱动，也不是完全无理论关联。

- 理论到设计翻译链：可解释性与性能存在提升空间的信念 + post-hoc解释不可靠 + 现有特征工程依赖专家 → 需求是自动化地生成可解释特征 → 利用黑盒模型能够捕捉非线性关系这一经验知识 → 设计从监督模型的PDP/ALE中提取变点并分箱、从模型响应聚类中合并类别 → 生成二元特征供线性模型使用 → 用AUC证明性能不下降、用参数数量证明可解释性提升 → 用bias-variance解释简单模型可能优于复杂模型。

### mapping_table

#### 1. 1

- theory_or_knowledge_claim_cn：Rudin：准确率与可解释性之间的权衡常常是迷思，可解释模型不必然损失性能。

- mechanism_cn：如果简单模型拥有更好的特征表示，则同样或更高性能可在更少参数下实现。

- design_requirement_cn：框架应生成能携带黑盒模型非线性知识的特征，供简单模型使用。

- artifact_choice_cn：以黑盒监督模型提取变换特征，再训练逻辑回归玻璃盒。

- evaluated_contrast_cn：原版逻辑回归 vs SAFE逻辑回归 vs 复杂监督模型。

- objective_result_cn：use case中AUC从0.78升至0.82，参数从49降至25；基准中AUC无显著下降、可解释性显著提升。

##### evidence_pointers

1. Fig. 4

2. Table 5

#### 2. 2

- theory_or_knowledge_claim_cn：复杂模型的高性能部分来自良好的数据表示，特别是非线性关系。

- mechanism_cn：如果把这些非线性以分段常数/二元特征显式表示，线性模型也能拟合该非线性。

- design_requirement_cn：连续变量应按照模型响应曲率分箱，使分段内的响应近似恒定。

- artifact_choice_cn：使用PDP/ALE曲线和PELT变点检测对连续变量自动分箱。

- evaluated_contrast_cn：不分箱的线性模型 vs SAFE分箱后的线性模型。

- objective_result_cn：SAFE变换能表达credit amount的非单调关系，并提升逻辑回归AUC。

##### evidence_pointers

1. Fig. 3

2. Fig. 4

#### 3. 3

- theory_or_knowledge_claim_cn：分类变量的某些水平对预测响应相似时可以安全合并。

- mechanism_cn：合并相似响应水平减少参数数量，且不丢失预测信息；层次聚类可根据模型响应合并类别。

- design_requirement_cn：分类变量应基于监督模型响应进行水平合并。

- artifact_choice_cn：对每个分类变量计算不同水平下的模型响应，用层次聚类合并水平。

- evaluated_contrast_cn：原始信用历史5个水平 vs SAFE合并后2个水平。

- objective_result_cn：参数数量下降，同时AUC提升。

##### evidence_pointers

1. Fig. 3

2. Table 2

#### 4. 4

- theory_or_knowledge_claim_cn：post-hoc解释是黑盒模型的简化，可能不准确且无统一保真度度量。

- mechanism_cn：与其事后解释黑盒，不如直接训练一个结构已知的透明模型，使解释来自模型本身。

- design_requirement_cn：最终模型应是玻璃盒，能给出系数级解释。

- artifact_choice_cn：用逻辑回归/线性模型作为最终玻璃盒，SAFE变换后的二元特征使预测可加性解释。

- evaluated_contrast_cn：SAFE最终模型 vs 黑盒监督模型（可解释性水平对比）。

- objective_result_cn：SAFE模型可解释性显著高于监督模型。

##### evidence_pointers

1. Fig. 6

2. Table 5

#### 5. 5

- theory_or_knowledge_claim_cn：bias-variance权衡：模型复杂度增加可能导致方差增大和过拟合。

- mechanism_cn：更少参数的简单模型在特征足够好时可能比复杂模型泛化更好。

- design_requirement_cn：在性能相近时优先选择更少参数的模型。

- artifact_choice_cn：通过SAFE生成少量变换特征，减少逻辑回归参数。

- evaluated_contrast_cn：调优gbm监督模型 vs SAFE逻辑回归。

- objective_result_cn：use case中gbm AUC 0.80但参数极多，SAFE逻辑回归AUC 0.82且参数极少；benchmark中出现简单模型优于监督模型的数据集。

##### evidence_pointers

1. Fig. 4

2. Fig. 5红区

## 评价逻辑

### evaluation_modes

1. 概念framework的形式化论证

2. 真实数据use case（credit-g）

3. 30个OpenML数据集的大规模基准

4. 基于参数数量的可解释性度量

5. 统计显著性检验（Wilcoxon rank sum test）

6. 可视化分析（三元图、箭头图）

- why_these_evaluations_cn：框架先需要形式化确保可计算；use case用于演示可解释变换和端到端可行性；大规模基准用于回答“是否普遍成立”并检验三种监督模型下的稳健性；AUC提供性能证据，参数数量提供可解释性证据；Wilcoxon检验避免只凭均值判断，可视化帮助读者感知trade-off位移。

- benchmark_and_contrast_chain_cn：先以原版逻辑回归为基线，然后加入默认svm、默认gbm、调优gbm作为复杂监督模型，再对每个监督模型应用SAFE得到SAFE svm、SAFE gbm default、SAFE gbm tuned。每个数据集10个固定split，逐split计算AUC，再以三元图比较三种角色（基线、监督、SAFE）的排序，以箭头图比较性能-可解释性位移，最后用Wilcoxon检验汇聚为无显著性能下降、显著可解释性提升的结论。

### claim_evidence_ledger

#### 1. SAFE特征工程能提高简单模型性能。

- claim_cn：SAFE特征工程能提高简单模型性能。

- evidence_cn：credit-g use case中AUC从0.78升至0.82；基准左半区显示多数数据集SAFE优于原版逻辑回归。

- status_cn：在展示的数据集上支持，但不是全部数据集。

#### 2. SAFE模型性能与复杂监督模型无显著差异。

- claim_cn：SAFE模型性能与复杂监督模型无显著差异。

- evidence_cn：Table 5中gbm default/tuned/svm vs SAFE的AUC Wilcoxon p值均大于0.05。

- status_cn：统计支持。

#### 3. SAFE模型可解释性显著高于复杂监督模型。

- claim_cn：SAFE模型可解释性显著高于复杂监督模型。

- evidence_cn：Table 5中可解释性Wilcoxon p值均小于0.001；Fig. 6显示箭头上移。

- status_cn：统计支持，但可解释性度量仅以参数数量近似。

#### 4. 复杂模型并不总是优于简单模型。

- claim_cn：复杂模型并不总是优于简单模型。

- evidence_cn：三元图红区出现SAFE模型在部分数据集中成为最好的情况；use case中SAFE逻辑回归AUC高于gbm。

- status_cn：有案例支持，但属于对既有一般信念的质疑，不是对所有复杂模型的全称否定。

#### 5. SAFE变换反映了监督模型学习到的非线性关系。

- claim_cn：SAFE变换反映了监督模型学习到的非线性关系。

- evidence_cn：Fig. 3展示credit amount的PDP呈非单调，SAFE分箱后水平均值随区间变化。

- status_cn：可视化支持机制，但未做消融或因果检验。

- internal_validity_strategy_cn：使用OpenML任务预定义的10个独立train/test splits；对gbm进行随机搜索调优并固定范围；所有SAFE变换只在训练数据上生成再应用到测试数据；用Wilcoxon检验而非仅描述均值；统一使用AUC指标和参数数量定义可解释性。

- external_validity_strategy_cn：使用30个来自OpenML100的二分类表格数据集，覆盖不同领域和规模；使用三种不同类型的监督模型（svm、默认gbm、调优gbm）；给出的软件包和GitHub代码支持复现。

- what_is_not_actually_tested_cn：没有进行真实用户或领域专家的可解释性评估；没有在真实组织决策流程中部署；没有测试回归任务、多分类、深度学习监督模型或除逻辑回归外的其他玻璃盒模型；没有系统消融PELT与层次聚类各自贡献；没有检验高阶交互特征。

## 贡献闭环

- technical_claim_cn：SAFE方法作为一种自动特征工程技术，在30个数据集上让逻辑回归模型保持复杂监督模型的AUC水平，同时显著降低参数数量。

- artifact_claim_cn：被识别为导致改进的设计部分是：从监督模型PDP/ALE中提取变点进行分箱、基于模型响应合并分类水平，以及最终用二元特征训练线性玻璃盒。

- mechanism_claim_cn：机制是：复杂模型能够捕捉变量与目标之间的非单调/非线性关系，SAFE将这些关系编码为分箱或合并后的可解释二元特征，从而使线性模型也能表达此类关系；同时因参数减少，模型方差更小，可能优于过拟合的复杂模型。

- boundary_claim_cn：该框架适用于二分类表格数据、以逻辑回归为玻璃盒、以gbm/svm为监督模型；并非所有数据集上SAFE都超越原版逻辑回归；当监督模型本身不能捕捉有效信息时，SAFE可能不提升性能；不处理高阶交互。

- reusable_design_knowledge_cn：可复用设计知识包括：利用黑盒模型的边际响应曲线自动生成可解释分箱；基于模型响应合并分类水平以降低复杂度；特征变换自动化和领域专家检查可结合；评估可解释性时可使用参数数量的倒数作为代理指标。

- theoretical_contribution_cn：从经验上支持并强化Rudin的观点：可解释性与性能的权衡不是必然，通过合适的自动特征工程可以同时获得性能和可解释性；同时以案例质疑“复杂模型恒优于简单模型”的信念。

- how_discussion_closes_intro_gap_cn：讨论部分逐条把SAFE ML框架与引言提出的四项要求对应：玻璃盒满足可解释，线性模型诊断工具多满足可审计，基准显示性能不下降满足高性能，自动特征变换满足自动化；从而回应了引言中“缺乏自动化可解释DSS”的缺口，并把use case和benchmark的证据统一为框架级贡献。

- overclaim_or_unsupported_leaps_cn：将“参数数量倒数”直接等同于真实可解释性是一种简化，可能过度；从benchmark的“部分数据集简单模型更好”上升到“质疑复杂模型优于简单模型的迷思”有一定跳跃，因为这是案例证据而非系统性证明；机制解释（bias-variance、非线性编码）没有被严格消融验证。

## 句级写作动作图谱

### 1. Abstract P1 S1-S3

- order：1

- section：Abstract

- locator：Abstract P1 S1-S3

- move_code：CONTEXT

- paraphrase_cn：机器学习已能生成有用的预测模型，AutoML工具使构建复杂模型变得容易。

- rhetorical_function_cn：开场承认ML能支持决策，为后文“但复杂性成问题”铺垫。

- depends_on_cn：无。

- sets_up_cn：引出复杂性在应用中的障碍。

- evidence_pointer：Abstract

### 2. Abstract P1 S4-S5

- order：2

- section：Abstract

- locator：Abstract P1 S4-S5

- move_code：PRACTICAL_STAKES

- paraphrase_cn：黑盒模型在高风险决策中常导致有害、不公平或错误决策。

- rhetorical_function_cn：把问题从效率上升到社会后果，制造研究紧迫感。

- depends_on_cn：前句说明模型复杂化。

- sets_up_cn：提出需要简化模型并保持性能。

- evidence_pointer：Abstract

### 3. Abstract P2 S1-S2

- order：3

- section：Abstract

- locator：Abstract P2 S1-S2

- move_code：RQ_OR_OBJECTIVE

- paraphrase_cn：本文提出用弹性黑盒作为监督模型来创建更简单、更不透明但准确可解释的玻璃盒模型。

- rhetorical_function_cn：明确论文的核心方案和贡献方向。

- depends_on_cn：前文已建立黑盒问题。

- sets_up_cn：为摘要后文列出三个主要结果。

- evidence_pointer：Abstract

### 4. Abstract P2 S3-S6

- order：4

- section：Abstract

- locator：Abstract P2 S3-S6

- move_code：STUDY_OVERVIEW

- paraphrase_cn：用OpenML多个表格数据集做大规模基准，并报告三个结果：提取信息提升简单模型、复杂模型未必优于简单模型、真实应用。

- rhetorical_function_cn：预先告诉读者评价方式和贡献清单。

- depends_on_cn：方案已提出。

- sets_up_cn：引导读者按这三个结果阅读正文。

- evidence_pointer：Abstract

### 5. Intro P1 S1-S3

- order：5

- section：Introduction

- locator：Intro P1 S1-S3

- move_code：CONTEXT

- paraphrase_cn：模型信任成为关键问题；复杂模型用于金融、医疗、安全等领域，影响贷款、治疗和警务决定。

- rhetorical_function_cn：建立模型决策无处不在的背景。

- depends_on_cn：无。

- sets_up_cn：为后文高风险场景中的信任问题做铺垫。

- evidence_pointer：Intro P1

### 6. Intro P1 S4-S8

- order：6

- section：Introduction

- locator：Intro P1 S4-S8

- move_code：PRACTICAL_STAKES

- paraphrase_cn：算法性能提升的同时复杂度增加；不批判地使用ML导致手术机器人事故、刑事司法问题、空气质量误报等，使金融等严格监管领域宁愿牺牲性能也不用复杂模型。

- rhetorical_function_cn：用真实负面案例说明黑盒模型的社会代价。

- depends_on_cn：前句说明模型应用广泛。

- sets_up_cn：论证需要可解释DSS。

- evidence_pointer：Intro P1

### 7. Intro P2 S1-S3

- order：7

- section：Introduction

- locator：Intro P2 S1-S3

- move_code：RQ_OR_OBJECTIVE

- paraphrase_cn：作者认为主要挑战是开发可解释AI决策支持系统，并引用Rudin表明准确率与可解释性权衡是迷思。

- rhetorical_function_cn：提出本文要解决的核心挑战，并引入理论支持点。

- depends_on_cn：前文现实问题。

- sets_up_cn：为“可解释模型不必然损失性能”提供知识基础。

- evidence_pointer：Intro P2

### 8. Intro P2 S4-S6

- order：8

- section：Introduction

- locator：Intro P2 S4-S6

- move_code：LIMITATION

- paraphrase_cn：可解释模型大多简单且容易验证，但构建它们需要大量计算和领域知识。

- rhetorical_function_cn：说明已有可解释模型虽好但不够自动化。

- depends_on_cn：Rudin观点。

- sets_up_cn：为四项要求中的自动性作铺垫。

- evidence_pointer：Intro P2

### 9. Intro P2 S7

- order：9

- section：Introduction

- locator：Intro P2 S7

- move_code：REQUIREMENT

- paraphrase_cn：据此提出可信且可访问系统必须满足四项要求：高性能、可审计、可解释、自动化。

- rhetorical_function_cn：把问题转化为设计标准。

- depends_on_cn：前文对现有模型的限制。

- sets_up_cn：后文SAFE ML框架将逐条对应这些要求。

- evidence_pointer：Intro P2

### 10. Intro P3-P6

- order：10

- section：Introduction

- locator：Intro P3-P6

- move_code：REQUIREMENT

- paraphrase_cn：逐条解释四项要求：黑盒性能高但不可解释；简单玻璃盒更易诊断；模型推理应透明；AutoML使建模自动化日益重要。

- rhetorical_function_cn：让四项要求成为可操作的框架目标。

- depends_on_cn：四项要求提出。

- sets_up_cn：为SAFE ML框架的设计评价提供标准。

- evidence_pointer：Intro P3-P6

### 11. Intro P7 S1-S3

- order：11

- section：Introduction

- locator：Intro P7 S1-S3

- move_code：RQ_OR_OBJECTIVE

- paraphrase_cn：本文介绍SAFE ML框架，用复杂监督模型学习可解释特征工程，然后训练透明玻璃盒模型。

- rhetorical_function_cn：正式提出论文制品。

- depends_on_cn：四项要求。

- sets_up_cn：为后面框架详细描述做预告。

- evidence_pointer：Intro P7

### 12. Intro P8

- order：12

- section：Introduction

- locator：Intro P8

- move_code：STUDY_OVERVIEW

- paraphrase_cn：说明论文组织：相关工作、框架、真实数据use case和benchmark、结论。

- rhetorical_function_cn：给出阅读地图。

- depends_on_cn：框架已提出。

- sets_up_cn：让读者预期经验证据位置。

- evidence_pointer：Intro P8

### 13. Section 2 opening

- order：13

- section：Related work

- locator：Section 2 opening

- move_code：TRANSITION

- paraphrase_cn：文献综述分为两部分：表格数据的可解释AI与DSS，以及数据工程方法。

- rhetorical_function_cn：组织文献结构。

- depends_on_cn：引言提出的问题。

- sets_up_cn：分别建立post-hoc解释不足与特征工程不足两个缺口。

- evidence_pointer：Section 2

### 14. Section 2.1 P1

- order：14

- section：Related work

- locator：Section 2.1 P1

- move_code：CONTEXT

- paraphrase_cn：GDPR的“解释权”和可信AI伦理指南使可解释性成为系统设计的一部分。

- rhetorical_function_cn：用法规和伦理标准提升可解释性问题的合法性。

- depends_on_cn：引言中的监管背景。

- sets_up_cn：引出对解释方法的文献回顾。

- evidence_pointer：Section 2.1

### 15. Section 2.1 P2

- order：15

- section：Related work

- locator：Section 2.1 P2

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：post-hoc解释方法包括规则约简、决策树、PDP、ALE、LIME、SHAP和BreakDown等。

- rhetorical_function_cn：概述现有解释工具箱。

- depends_on_cn：可解释性成为需求。

- sets_up_cn：为下一段指出这些方法的不足。

- evidence_pointer：Section 2.1 P2

### 16. Section 2.1 P3

- order：16

- section：Related work

- locator：Section 2.1 P3

- move_code：LIMITATION

- paraphrase_cn：但这些解释是模型的简化，可能不准确，而且缺少统一保真度度量，因而可能误导或有害。

- rhetorical_function_cn：建立对post-hoc解释的怀疑。

- depends_on_cn：前段解释方法。

- sets_up_cn：为“应训练透明模型而非解释黑盒”提供理由。

- evidence_pointer：Section 2.1 P3

### 17. Section 2.1 P4

- order：17

- section：Related work

- locator：Section 2.1 P4

- move_code：LIMITATION

- paraphrase_cn：可解释模型结构已知，但即使线性模型有数百个系数和交互也会变得不透明。

- rhetorical_function_cn：防止“线性模型一定可解释”的简单化。

- depends_on_cn：前段讨论透明模型。

- sets_up_cn：为简化参数数量作为可解释性指标埋下伏笔。

- evidence_pointer：Section 2.1 P4

### 18. Section 2.2 P1

- order：18

- section：Related work

- locator：Section 2.2 P1

- move_code：CONTEXT

- paraphrase_cn：数据准备和变换是数据分析核心，算法质量既依赖复杂度也依赖特征工程，领域知识在金融、保险、医学中很关键。

- rhetorical_function_cn：给出特征工程的重要性背景。

- depends_on_cn：可解释模型讨论。

- sets_up_cn：引出特征工程自动化缺口。

- evidence_pointer：Section 2.2 P1

### 19. Section 2.2 P2

- order：19

- section：Related work

- locator：Section 2.2 P2

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：信用评分等成熟领域已有基于领域知识的分箱方法，如极值、均值、标准差和基于树的离散化，但通常需要专家参与。

- rhetorical_function_cn：说明领域特征工程成熟但依赖专家。

- depends_on_cn：特征工程背景。

- sets_up_cn：为自动化需求做对照。

- evidence_pointer：Section 2.2 P2

### 20. Section 2.2 P3

- order：20

- section：Related work

- locator：Section 2.2 P3

- move_code：LIMITATION

- paraphrase_cn：自动数据变换方法虽然发展，但往往耗时且不如人工，而且生成的新特征难以解释。

- rhetorical_function_cn：指出自动化的现状缺口。

- depends_on_cn：前段专家依赖。

- sets_up_cn：为SAFE ML的“可解释自动特征工程”定位。

- evidence_pointer：Section 2.2 P3

### 21. Section 2.2 P4

- order：21

- section：Related work

- locator：Section 2.2 P4

- move_code：GAP

- paraphrase_cn：已有可扩展自动特征生成框架（Shi等），但SAFE ML的独特点是直接从复杂黑盒模型中提取特征并用它们训练简单可解释模型。

- rhetorical_function_cn：明确本文相对已有自动特征工程的方法差异。

- depends_on_cn：自动特征工程限制。

- sets_up_cn：引向SAFE ML框架。

- evidence_pointer：Section 2.2 P4

### 22. Section 3 opening

- order：22

- section：SAFE ML

- locator：Section 3 opening

- move_code：STUDY_OVERVIEW

- paraphrase_cn：本节描述六步SAFE ML框架，从原始数据到可解释模型完全自动。

- rhetorical_function_cn：宣布框架设计的开始。

- depends_on_cn：前文缺口。

- sets_up_cn：详细步骤将逐条展开。

- evidence_pointer：Section 3 opening

### 23. Section 3.1 Step 2

- order：23

- section：SAFE ML

- locator：Section 3.1 Step 2

- move_code：DESIGN_FEATURE

- paraphrase_cn：用原始数据训练任意复杂监督模型，该模型不需要可解释，只用来提取特征知识，因此应尽量高绩效。

- rhetorical_function_cn：定义监督模型角色。

- depends_on_cn：框架思想。

- sets_up_cn：说明为什么需要复杂模型作为信息源。

- evidence_pointer：Section 3.1 Step 2

### 24. Section 3.1 Step 3

- order：24

- section：SAFE ML

- locator：Section 3.1 Step 3

- move_code：DESIGN_FEATURE

- paraphrase_cn：SAFE方法对连续模型用期望预测函数找变点分箱，对分类变量用聚类合并水平；变换在训练数据上生成再应用到训练和测试数据。

- rhetorical_function_cn：给出核心特征工程技术。

- depends_on_cn：监督模型训练完成。

- sets_up_cn：为后文算法和实验建立操作定义。

- evidence_pointer：Section 3.1 Step 3

### 25. Section 3.1 Step 4-5

- order：25

- section：SAFE ML

- locator：Section 3.1 Step 4-5

- move_code：DESIGN_FEATURE

- paraphrase_cn：新特征集合包含原始特征和SAFE变换特征，可做特征选择；然后拟合逻辑回归或线性模型。

- rhetorical_function_cn：说明玻璃盒模型如何建立。

- depends_on_cn：SAFE变换生成。

- sets_up_cn：为最终模型可解释性铺路。

- evidence_pointer：Section 3.1 Step 4-5

### 26. Section 3.1 Step 6

- order：26

- section：SAFE ML

- locator：Section 3.1 Step 6

- move_code：DESIGN_FEATURE

- paraphrase_cn：简单模型保证系数能直接解释每个变量对预测的贡献，终端用户可基于预测和解释做决策。

- rhetorical_function_cn：把制品设计与决策支持目标连接。

- depends_on_cn：玻璃盒模型已训练。

- sets_up_cn：为use case中系数表的意义做预备。

- evidence_pointer：Section 3.1 Step 6

### 27. Section 3.2

- order：27

- section：SAFE ML

- locator：Section 3.2

- move_code：MECHANISM

- paraphrase_cn：形式化目标是在变换类H和模型类G中最小化损失，得到玻璃盒g(h(x))。

- rhetorical_function_cn：把框架翻译成优化问题。

- depends_on_cn：六步流程。

- sets_up_cn：为SAFE方法的具体变换函数提供数学语境。

- evidence_pointer：Section 3.2

### 28. Section 3.2.1

- order：28

- section：SAFE ML

- locator：Section 3.2.1

- move_code：DESIGN_FEATURE

- paraphrase_cn：SAFE变换函数把数值变量转成由PDP或ALE变点决定的二元分箱向量，把分类变量转成由层次聚类决定的新水平二元向量。

- rhetorical_function_cn：给出SAFE特征变换的具体形式。

- depends_on_cn：形式化定义。

- sets_up_cn：为Algorithm 1的伪代码提供依据。

- evidence_pointer：Section 3.2.1

### 29. Section 3.2.1 Definition 3.1附近

- order：29

- section：SAFE ML

- locator：Section 3.2.1 Definition 3.1附近

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：引入PDP定义：固定目标变量，在其余变量上取期望得到模型响应曲线。

- rhetorical_function_cn：为后续变点检测定义输入。

- depends_on_cn：SAFE变换需要响应曲线。

- sets_up_cn：解释PDP如何被用于分箱。

- evidence_pointer：Section 3.2.1 Definition 3.1

### 30. Section 3.3

- order：30

- section：SAFE ML

- locator：Section 3.3

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：用PELT变点检测把连续变量按PDP最大变异性处分箱，惩罚由MBIC决定；层次聚类用于分类水平合并。

- rhetorical_function_cn：具体化算法组件。

- depends_on_cn：PDP/ALE曲线。

- sets_up_cn：算法1和算法2的具体操作。

- evidence_pointer：Section 3.3

### 31. Section 3.3 PELT段落

- order：31

- section：SAFE ML

- locator：Section 3.3 PELT段落

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：经验结果显示PELT精度高于Binary Segmentation，且计算成本小一个数量级，因此选择PELT。

- rhetorical_function_cn：为PELT选择提供技术合理性。

- depends_on_cn：变点检测需求。

- sets_up_cn：提高算法选择的可信度。

- evidence_pointer：Section 3.3

### 32. Section 4 opening

- order：32

- section：Empirical study

- locator：Section 4 opening

- move_code：STUDY_OVERVIEW

- paraphrase_cn：实证研究分两部分：credit-g use case和OpenML100基准。

- rhetorical_function_cn：预告评价结构。

- depends_on_cn：框架已定义。

- sets_up_cn：分别承接可行性和泛化性。

- evidence_pointer：Section 4

### 33. Section 4.1 P1

- order：33

- section：Empirical study

- locator：Section 4.1 P1

- move_code：BENCHMARK_OR_CONTRAST

- paraphrase_cn：使用credit-g德国信用数据集，按OpenML task 31的9:1划分训练测试，并用调优gbm作为监督模型。

- rhetorical_function_cn：定义use case的实例设置。

- depends_on_cn：框架步骤1和2。

- sets_up_cn：为结果比较提供语境。

- evidence_pointer：Section 4.1

### 34. Section 4.1 Fig.3附近

- order：34

- section：Empirical study

- locator：Section 4.1 Fig.3附近

- move_code：RESULT

- paraphrase_cn：SAFE把credit amount变成5个箱子，并捕捉非单调平均预测；把credit history从5个水平合并成2个直觉性水平。

- rhetorical_function_cn：展示SAFE变换产物并说明其可解释意义。

- depends_on_cn：调优gbm。

- sets_up_cn：为逻辑回归系数解释提供例子。

- evidence_pointer：Fig. 3

### 35. Section 4.1 PARAMS段落

- order：35

- section：Empirical study

- locator：Section 4.1 PARAMS段落

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：用参数数量的倒数度量可解释性；对gbm，参数数等于树数乘交互深度及相关节点和权重。

- rhetorical_function_cn：建立可解释性可量化度量。

- depends_on_cn：需要同时评估性能和可解释性。

- sets_up_cn：为Fig.4和Fig.6二维可视化做铺垫。

- evidence_pointer：Section 4.1

### 36. Section 4.1 Fig.4附近

- order：36

- section：Empirical study

- locator：Section 4.1 Fig.4附近

- move_code：RESULT

- paraphrase_cn：use case中SAFE变换同时提升AUC和可解释性；原版逻辑回归AUC 0.78/49参数，SAFE逻辑回归AUC 0.82/25参数，调优gbm AUC 0.80但参数极多。

- rhetorical_function_cn：给出核心use case证据。

- depends_on_cn：SAFE特征生成和逻辑回归训练。

- sets_up_cn：作为后续benchmark的初步信号。

- evidence_pointer：Fig. 4

### 37. Section 4.1 bias-variance段落

- order：37

- section：Empirical study

- locator：Section 4.1 bias-variance段落

- move_code：MECHANISM

- paraphrase_cn：作者用bias-variance解释SAFE逻辑回归优于gbm：更少复杂度降低方差，gbm可能过拟合。

- rhetorical_function_cn：对意外结果提供机制解释。

- depends_on_cn：AUC结果。

- sets_up_cn：为“简单模型可能更好”的一般主张提供理论支持。

- evidence_pointer：Section 4.1

### 38. Section 4.1 Table 2附近

- order：38

- section：Empirical study

- locator：Section 4.1 Table 2附近

- move_code：RESULT

- paraphrase_cn：SAFE逻辑回归系数表显示每个箱子/合并类别的贡献，例如某credit amount区间使坏概率logit增加0.0051。

- rhetorical_function_cn：展示玻璃盒模型的直接解释能力。

- depends_on_cn：SAFE变换后的特征。

- sets_up_cn：支撑可解释性主张。

- evidence_pointer：Table 2

### 39. Section 4.2 P1

- order：39

- section：Empirical study

- locator：Section 4.2 P1

- move_code：BENCHMARK_OR_CONTRAST

- paraphrase_cn：从OpenML100选择30个无缺失二分类数据集，每个任务有10个train/test splits。

- rhetorical_function_cn：定义基准规模和数据来源。

- depends_on_cn：use case成功。

- sets_up_cn：为多种模型比较设定范围。

- evidence_pointer：Section 4.2 P1

### 40. Section 4.2 P2

- order：40

- section：Empirical study

- locator：Section 4.2 P2

- move_code：BENCHMARK_OR_CONTRAST

- paraphrase_cn：对每个split训练原版逻辑回归、默认svm、默认gbm、调优gbm，并分别用SAFE生成对应的三个SAFE逻辑回归模型。

- rhetorical_function_cn：设置对照模型和处理模型。

- depends_on_cn：OpenML任务。

- sets_up_cn：为三元图和箭头图提供数据点。

- evidence_pointer：Section 4.2 P2

### 41. Section 4.2 三元图说明

- order：41

- section：Empirical study

- locator：Section 4.2 三元图说明

- move_code：BENCHMARK_OR_CONTRAST

- paraphrase_cn：三元图中每个点对应一个数据集上原版逻辑回归、监督模型、SAFE模型三者AUC排序后计分的位置。

- rhetorical_function_cn：说明可视化如何编码三模型比较。

- depends_on_cn：30数据集AUC。

- sets_up_cn：识别左/右区域、红/蓝/绿区域的含义。

- evidence_pointer：Fig. 5

### 42. Section 4.2 左半区解释

- order：42

- section：Empirical study

- locator：Section 4.2 左半区解释

- move_code：RESULT

- paraphrase_cn：左半边数据集上SAFE平均优于原版逻辑回归；红区表示SAFE模型优于复杂监督模型，说明合适特征工程使简单模型超过复杂模型，质疑了复杂模型恒优于线性模型的迷思。

- rhetorical_function_cn：给出主要结果并直接连接到贡献主张。

- depends_on_cn：三元图数据。

- sets_up_cn：为讨论中的“复杂模型未必胜出”提供证据。

- evidence_pointer：Fig. 5

### 43. Section 4.2 右半区解释

- order：43

- section：Empirical study

- locator：Section 4.2 右半区解释

- move_code：BOUNDARY_CONDITION

- paraphrase_cn：右半边数据集中原版逻辑回归优于SAFE；蓝区显示某些监督模型也差于逻辑回归，说明SAFE并非万能，且调优gbm也未必总优于逻辑回归。

- rhetorical_function_cn：诚实呈现边界条件，防止过度概括。

- depends_on_cn：三元图数据。

- sets_up_cn：为讨论和未来工作限定适用范围。

- evidence_pointer：Fig. 5

### 44. Section 4.2 Fig.6附近

- order：44

- section：Empirical study

- locator：Section 4.2 Fig.6附近

- move_code：RESULT

- paraphrase_cn：灰色箭头显示SAFE使模型从复杂监督位置向高可解释、相似AUC位置移动；中位数箭头表明整体trade-off被抬升。

- rhetorical_function_cn：把散点结果压缩成可解释性-性能位移的视觉论证。

- depends_on_cn：AUC和参数数量。

- sets_up_cn：为Wilcoxon检验提供可视化先导。

- evidence_pointer：Fig. 6

### 45. Section 4.2 Wilcoxon段

- order：45

- section：Empirical study

- locator：Section 4.2 Wilcoxon段

- move_code：ROBUSTNESS_OR_BOUNDARY_TEST

- paraphrase_cn：Wilcoxon检验表明SAFE相对各监督模型AUC无显著下降，但可解释性显著提升。

- rhetorical_function_cn：为性能保持和可解释性提升提供统计证据。

- depends_on_cn：30数据集AUC和参数数。

- sets_up_cn：支撑讨论部分关于四项要求中高性能和可解释性的结论。

- evidence_pointer：Table 5

### 46. Section 4.2 末尾段落

- order：46

- section：Empirical study

- locator：Section 4.2 末尾段落

- move_code：MECHANISM

- paraphrase_cn：SAFE模型泛化了监督模型捕获的关系；没有复杂监督模型就不可能得到这些特征；即使黑盒略好，玻璃盒仍值得用于透明、可解释和可审计。

- rhetorical_function_cn：解释SAFE为何有效，并给出最终推荐。

- depends_on_cn：基准结果。

- sets_up_cn：为讨论部分框架需求映射做准备。

- evidence_pointer：Section 4.2末段

### 47. Section 5 P1

- order：47

- section：Discussion

- locator：Section 5 P1

- move_code：CONTEXT

- paraphrase_cn：ML越来越多用于决策支持，决策者面临盲目信任黑盒或完全不用的两难。

- rhetorical_function_cn：回到文章开头的问题。

- depends_on_cn：引言中的信任问题。

- sets_up_cn：引出SAFE ML作为破解两难的方法。

- evidence_pointer：Section 5 P1

### 48. Section 5 P2-P3

- order：48

- section：Discussion

- locator：Section 5 P2-P3

- move_code：CONTRIBUTION

- paraphrase_cn：SAFE ML框架用监督模型自动化特征变换并训练玻璃盒，因此能逐条满足四项要求：可解释、可审计、高性能、自动化。

- rhetorical_function_cn：把经验证据回扣到引言的需求清单。

- depends_on_cn：前三节框架和实验。

- sets_up_cn：正式声明框架级贡献。

- evidence_pointer：Section 5 P2-P3

### 49. Section 5 P4

- order：49

- section：Discussion

- locator：Section 5 P4

- move_code：CONTRIBUTION

- paraphrase_cn：use case表明在高度监管的金融领域，SAFE可以生成完全可解释的线性模型并达到复杂gbm的性能。

- rhetorical_function_cn：突出在严格监管场景中的适用性。

- depends_on_cn：credit-g结果。

- sets_up_cn：强化DSS应用价值。

- evidence_pointer：Section 5 P4

### 50. Section 5 P5

- order：50

- section：Discussion

- locator：Section 5 P5

- move_code：CONTRIBUTION

- paraphrase_cn：30数据集基准确认SAFE生成特征可训练准确透明模型，且部分数据集上线性模型达到或超过复杂模型。

- rhetorical_function_cn：把benchmark结果升华为一般知识。

- depends_on_cn：基准证据。

- sets_up_cn：为未来工作和边界条件作收束。

- evidence_pointer：Section 5 P5

### 51. Section 5.1

- order：51

- section：Discussion

- locator：Section 5.1

- move_code：LIMITATION_AND_FUTURE

- paraphrase_cn：SAFE目前只变换单个特征，未来可以从随机森林或xgboost中提取交互特征。

- rhetorical_function_cn：明确未覆盖的高阶交互边界并给出扩展路线。

- depends_on_cn：框架当前设计。

- sets_up_cn：防止读者误以为框架已经处理全部复杂关系。

- evidence_pointer：Section 5.1

### 52. Section 5.2

- order：52

- section：Discussion

- locator：Section 5.2

- move_code：OTHER

- paraphrase_cn：提供R包rSAFE、Python库SafeTransformer和实验代码仓库。

- rhetorical_function_cn：支持可复现性和工具落地。

- depends_on_cn：框架和实验。

- sets_up_cn：让读者能自行验证。

- evidence_pointer：Section 5.2

## 写作技术

- gap_construction_cn：先建立高风险黑盒决策的实践问题，再指出post-hoc解释不可靠，最后强调已有特征工程依赖专家且自动生成特征难解释；两层缺口交汇出“需要自动可解释特征工程”的位置。

- signposting_cn：在摘要和引言末尾预告三结果，第二章开头说明综述的两部分，第三章开头预告六步框架，第四章开头预告use case和benchmark；每个阶段都先给地图再展开。

- transition_logic_cn：从黑盒问题过渡到四项要求，再从四项要求过渡到SAFE ML框架；框架后以“需要实证”过渡到use case；use case后以“单数据集不足”过渡到多数据集基准；基准后以“结果回扣要求”过渡到讨论。

- claim_evidence_rhythm_cn：每次提出大主张后紧跟局部证据：提出SAFE能提升性能，马上用credit-g的AUC和参数数说明；提出总体不降性能，马上用Wilcoxon p值说明；同时用红/蓝区域主动限定反例。

- benchmark_narrative_cn：不是简单列成绩，而是用三元图把三种模型的相对排序空间可视化，再用箭头图把“可解释性-性能位移”呈现为整体趋势；benchmark被嵌入“trade-off是否被抬升”的论证而非单独的性能竞赛。

- theory_return_cn：在use case中用bias-variance解释为什么简单模型可能超过复杂模型；在讨论中把Rudin的“trade-off是迷思”重新表述为“适当特征工程可以同时获得性能和可解释性”，让数据结果返回并强化引言知识。

- contribution_positioning_cn：贡献被定位为：框架方法、实证证据、对常见信念的质疑、满足DSS四项要求；没有把贡献说成“打败所有黑盒”，而是限定在表格二分类和自动特征工程。

- novelty_protection_cn：通过大规模多数据集和统计检验防止结果被视为单案例；通过对比多种监督模型防止方法依赖特定黑盒；通过公开软件和代码增强可复现；通过明确边界（不处理交互、不保证所有数据集更好）防止被一次性性能结果击穿。

## 可复用研究与写作程序

### structure_steps

#### 1. 1

- step：1

- writing_job_cn：用高风险决策例子建立黑盒模型不可信的实践问题，并给出法规或权威观点。

- research_job_cn：识别应用领域中的失败案例和用户信任障碍。

- required_evidence_cn：需要具体负面案例或监管要求，说明问题不是虚构。

- transition_to_next_cn：从问题提炼出若干系统要求，如性能、可审计、可解释、自动化。

#### 2. 2

- step：2

- writing_job_cn：把问题转化为明确的设计需求，并预告解决方案。

- research_job_cn：定义制品要满足的标准。

- required_evidence_cn：需求应可操作并与后续评价指标对应。

- transition_to_next_cn：用“现有方法不足”说明为什么需要新框架。

#### 3. 3

- step：3

- writing_job_cn：综述相关方法并指出现有post-hoc解释和特征工程的缺口。

- research_job_cn：梳理可解释方法与特征工程方法的能力边界。

- required_evidence_cn：至少一个明确缺口：现有解释不可靠或特征工程依赖专家。

- transition_to_next_cn：缺口直接引出本文制品的核心思路。

#### 4. 4

- step：4

- writing_job_cn：详细描述框架/算法，给出步骤、形式化定义和伪代码。

- research_job_cn：设计算法并确保可复现。

- required_evidence_cn：算法输入输出明确，最好有图示说明变换过程。

- transition_to_next_cn：框架需要实证演示，于是进入use case。

#### 5. 5

- step：5

- writing_job_cn：先用一个真实数据集做use case，展示变换的可解释性和结果改进。

- research_job_cn：运行端到端流程，报告性能与复杂度指标。

- required_evidence_cn：AUC或类似指标，以及参数数量或可视化变换。

- transition_to_next_cn：以“单案例不足”引出大规模基准。

#### 6. 6

- step：6

- writing_job_cn：用多数据集基准评价框架，设置多种baseline和监督模型，进行统计检验。

- research_job_cn：选择公开数据集、多种对照组、多次划分，并运行统计检验。

- required_evidence_cn：足够多的数据集、重复划分、显著性检验和可视化结果。

- transition_to_next_cn：把统计结果回扣到引言需求。

#### 7. 7

- step：7

- writing_job_cn：讨论中逐条证明框架满足需求，并声明贡献、边界和未来工作。

- research_job_cn：检查结果是否支持所有需求；识别未覆盖场景。

- required_evidence_cn：能够对应需求表逐项引用证据。

- transition_to_next_cn：给出软件和复现资源，结束。

### most_transferable_moves_cn

1. 用四项需求作为设计和评价的锚点，使所有实验都回流到需求。

2. 先use case展示直观效果，再大基准提供统计支持。

3. 用参数数量倒数做可解释性代理指标，使性能-可解释性trade-off可可视化。

4. 用三元图和箭头图把复杂多维比较压缩为读者容易理解的位移图。

5. 用Wilcoxon检验支持“性能不下降，可解释性提升”的联合主张。

### resource_intensive_or_nonstandard_parts_cn

1. 30个OpenML数据集和每个任务10个固定split需要较大计算量和数据管理。

2. 调优gbm的随机搜索需要额外计算预算。

3. 三元图和复杂度计算需要自己定义参数数量公式。

4. use case中的领域解释（信用历史合并）依赖对信用数据的背景知识。

### what_not_to_copy_superficially_cn

1. 如果没有大规模多数据集基准，就不能声称“复杂模型不必然优于简单模型”。

2. 如果没有统计检验，仅靠均值差异不能支撑“性能无显著下降”。

3. 如果只用参数数量代替可解释性，应说明这是代理指标，不能直接等同于用户理解。

4. 如果框架没有处理交互，就不能暗示它解决了所有非线性问题。

- single_best_description_of_the_routine_cn：先把可信DSS拆成四项要求，再构建一个用黑盒监督模型自动生成可解释特征、用玻璃盒做最终决策的框架，最后用单案例展示、多数据集基准和统计检验证明性能不下降且可解释性提升。

## 分析边界

原文没有提供精确分页，所有位置证据使用章节、段落、图、表标识；Fig.3和Fig.4的部分细节只能依据正文描述重建；benchmark表内若干数字受OCR排版影响可能有微小误差，但不影响整体结论。
