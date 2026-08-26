# Does Social Influence Change with Other Information Sources? A Large-Scale Randomized Experiment in Medical Crowdfunding

- 作者：Yun Young Hur; Fujie Jin; Xitong Li; Yuan Cheng; Yu Jeffrey Hu
- 年份 / 期刊：2023 / Information Systems Research
- DOI：10.1287/isre.2022.1189
- 源文件：28560_2023_does-social-influence-change-with-other-information-sources-a-large-scale-randomized-experiment.md
- 论文主类型：field_intervention_or_platform_experiment
- 主导写作弧线：phenomenon_mechanism_intervention_field_test
- 置信度：0.88

## 文章级论证概况

- 核心问题：在医疗众筹情境中，当一个病例页面同时存在“好友捐赠信息”这一社交影响和其他病例属性信息时，社交影响对捐赠可能性的作用是否会随其他信息来源的信息价值而变化？

- 制品与设计：作者在一家领先的中国医疗众筹平台开展大规模捐赠者层面随机现场实验：用户在实验期内首次点击病例页面时被随机分入对照组或处理组，且分配固定；对照组看到病例标题、目标金额和文字描述，处理组额外看到“某好友捐赠了X元”这一行社交影响信息。为度量病例属性的信息价值，作者还设计了基于似然比思想的MTurk在线调查，比较不同属性取值在多大程度上让受访者感知到病例真实需要帮助。此外，作者利用平台实验期外数据训练模型，为每个病例构造综合信息性指数。

- 客观结果：全样本中，展示好友捐赠信息使捐赠概率显著提高约16.0%。当病例包含未成年患者、严重疾病、有商业保险等被调查判定为高信息价值的属性时，社交影响不显著；当病例没有这类高信息价值属性时，社交影响显著提高捐赠概率约18%–21%。当病例没有高信息价值属性但同时具有两个低信息价值属性时，社交影响再次变得不显著。使用信息性指数的聚合分析同样发现，社交影响对捐赠概率和捐赠金额的正向作用随信息性指数升高而下降。

- 核心贡献：作者声称是首批系统研究社交影响如何与多种其他信息源交互的论文之一；结果表明本研究情境中的社交影响主要是信息性的，即好友捐赠信息作为求助真实性的背书，其边际价值取决于病例本身已有信息的信息价值。因此，社交影响并不会仅仅让具有高信息价值属性的“强案例”获得更多的锁定式资源，反而可以把捐赠注意力引向缺乏高信息价值属性的“弱案例”，在整体上促进捐赠资源更平等的分布。

- 整篇论证链：论文从“社会影响无处不在但尚未系统研究其如何与其他信息源交互”的缺口出发，将问题置于医疗众筹这一信息不对称突出、求助需求真实性难以验证的真实场景。作者先用文献构建两类竞争预期：高信息价值属性可能使社交影响冗余，也可能形成锁定效应。随后通过MTurk调查将病例属性区分为高/低信息价值，再借助平台链接式分享产生的捐赠者层面随机实验，估计展示好友捐赠信息对捐赠概率的因果效应，并逐一比较含或不含高/低信息价值属性的子样本；结果支持“高信息价值弱化社交影响”的预期。为进一步证明边界条件，作者用实验期外数据构造信息性指数，验证整体信息价值越高社交影响越弱，并通过Tobit捐赠金额、分享/未分享样本对比、病例内匹配和固定效应检验排除替代解释。最后，作者把结论上升为“社交影响在本情境中主要是信息性的、并有助于更平等分配捐赠资源”的理论与实务贡献。

## 类型与写作弧线判定

- 论文主类型判定：论文核心证据来自真实医疗众筹平台上的大规模随机现场实验：作者在平台病例页面上实际操纵“是否展示好友捐赠信息”这一数字设计元素，并以真实捐赠行为作为结果变量。MTurk调查和离线数据建模是辅助性测量与稳健性工具，不改变论文以现场干预和因果识别为主的性质。

- 主导写作弧线判定：文章从社交影响与多种信息来源交互的经验现象出发，提出“信息价值决定社交影响边际效用”的机制假设，再通过现场实验对真实平台用户施加信息展示干预，并以随机分配和子样本比较进行因果检验，最后回到机制解释（信息性社会影响）与资源分配含义。整体符合“现象—机制—数字干预—现场因果检验”的弧线。

## 研究开展程序

- study_or_phase_count：6

- 研究阶段总序列：研究顺序是：先通过MTurk调查建立“病例属性信息价值”这一核心调节构念的操作化；然后在真实平台进行大规模捐赠者层面随机现场实验，估计社交影响的主效应及属性层面的异质性；接着用实验期外数据构造整体信息性指数，把属性逐一分析推广为聚合分析；最后用一系列稳健性检验处理替代结果变量、替代机制、样本不平衡和反射问题。六个阶段呈“构念测量—因果主效应—条件边界—聚合推广—替代解释排除”的累积关系。

### studies_or_phases

#### 1. MTurk调查：度量病例属性的信息价值

- order：1

- name_cn：MTurk调查：度量病例属性的信息价值

- question_cn：哪些病例属性更能够让捐赠者感知到病例真实需要帮助，因而具有较高的信息价值？

- inputs_and_setting_cn：195名美国MTurk受访者（通过注意检查后）；受访者先阅读医疗众筹介绍并回答理解题，随后针对患者年龄、疾病严重度、商业保险、患者性别、目标金额、描述长度、照片数量等属性的两个取值版本进行七点Likert同意度评价。

- designed_or_compared_object_cn：每个病例属性被设计成两个取值集，例如“未成年患者”与“成年患者”，随机向受访者展示两种比较方向之一，以衡量某一取值相对另一取值在多大程度上让案例显得真实需要帮助。

- baseline_control_or_counterfactual_cn：以“两个取值集在感知求助需要上没有差异”作为零假设；如果t检验显著为正或负，则认为相应取值具有高信息价值，否则为低信息价值。

##### objective_metrics

1. 反向编码后合并的均值

2. t统计量

3. 标准差

- analysis_method_cn：对两版本回答进行反向编码合并，用双尾t检验检验均值是否显著异于0。

- main_result_cn：未成年患者、严重疾病、有商业保险（负向）被识别为高信息价值属性；女性患者、较高目标金额、较多照片、较长描述被识别为低信息价值属性。

- argumentative_role_cn：为现场实验提供了病例属性分层和调节变量操作化的基础，使后续“高/低信息价值”的子样本比较有独立于实验数据的依据。

- remaining_uncertainty_cn：MTurk受访者来自美国，而现场实验平台用户在中国，属性感知可能存在文化或情境差异；调查测量的是自报感知而非真实捐赠行为。

- link_to_next_phase_cn：该调查的结果直接用于把现场实验数据按照“是否含有高信息价值属性”进行划分，从而检验社交影响的条件性。

##### evidence_pointers

1. Section 4.3

2. Table 3

3. Online Appendix A

#### 2. 大规模随机现场实验：社交影响主效应与高/低信息价值属性的异质性

- order：2

- name_cn：大规模随机现场实验：社交影响主效应与高/低信息价值属性的异质性

- question_cn：展示好友捐赠信息是否提高捐赠概率？该正向影响是否在含有高信息价值属性的病例中被削弱、在只含低信息价值属性的病例中仍显著？

- inputs_and_setting_cn：平台2017年12月7日至10日共四天产生的页面访问数据；最终样本为757,094个捐赠者-病例观测，来自722,179名访问者和15,768个病例，其中348,295名访问者分入对照组、373,884名分入处理组。

- designed_or_compared_object_cn：对捐赠者进行随机分组；处理组病例页面在筹款目标下方额外显示“某人捐赠了X元”，对照组不显示该行；每位用户首次点击病例链接时随机且之后固定。

- baseline_control_or_counterfactual_cn：对照组作为无社交影响的反事实；在不同属性子样本中，“不含该高信息价值属性”的病例作为“含该属性”病例的内部对照。

##### objective_metrics

1. Donation二元捐赠指标

2. 处理效应系数转换后的百分比变化

3. 稳健标准误下的t统计量

- analysis_method_cn：使用逻辑回归模型估计Donation对Treatment的回归，控制病例与捐赠者层面变量及其与处理的交互；按病例聚类稳健标准误；对属性子样本分别估计处理效应。

- main_result_cn：全样本中社交影响使捐赠概率提高约16.0%（H1支持）。在含未成年患者、严重疾病、有商业保险的病例中，处理效应不显著；在相应不含这些属性的病例中，处理效应约为14.8%–18.4%且显著。在无任何高信息价值属性的子样本中，处理效应约20.9%；当只有一个低信息价值属性存在时，效应仍显著。

- argumentative_role_cn：这是整篇论文的核心因果证据：既建立了社交影响的正向主效应，又通过属性子样本比较直接检验H2的“高信息价值削弱社交影响”部分。

- remaining_uncertainty_cn：属性逐一分析未同时纳入所有属性的聚合信息；可能存在样本不平衡、炫耀动机、反射问题等替代解释；未识别好友身份和信息发送者特征。

- link_to_next_phase_cn：由于属性逐一分析只能说明单个属性的作用，下一阶段用整体信息性指数把调节作用推广到病例所有属性。

##### evidence_pointers

1. Section 4.1

2. Section 4.2

3. Section 5.1

4. Section 5.2

5. Table 4

6. Table 5

7. Figure 1

#### 3. 整体信息性指数的聚合分析

- order：3

- name_cn：整体信息性指数的聚合分析

- question_cn：当用所有病例属性综合成的信息性指数衡量信息价值时，社交影响是否随指数升高而减弱？

- inputs_and_setting_cn：实验期内的757,094个观测；另外从同一平台收集实验期外相近窗口的3,539个病例页面访问和捐赠数据，用于训练筹款成功概率模型。

- designed_or_compared_object_cn：用实验期外数据训练逻辑回归模型，预测每个实验病例的筹款成功概率，并将该预测概率定义为“信息性指数”；将该指数及其与Treatment的交互项加入主回归。

- baseline_control_or_counterfactual_cn：信息性指数接近0的病例作为低信息价值基线；指数高的病例作为高信息价值对照；Treatment×指数交互项为负则说明高信息价值削弱社交影响。

##### objective_metrics

1. Treatment主效应系数

2. Informativeness Index主效应系数

3. Treatment×Informativeness Index交互项系数

- analysis_method_cn：逻辑回归，控制捐赠者层面变量及交互项；以病例聚类稳健标准误。

- main_result_cn：Treatment系数正显著，Informativeness Index系数正显著，Treatment×Informativeness Index交互项负显著；说明病例整体信息价值越高，社交影响的正向作用越小。

- argumentative_role_cn：把前文的属性逐一分析升级为综合性的边界条件检验，证明“信息价值削弱社交影响”不是某个单一属性的偶然结果，而是病例整体信息环境的系统效应。

- remaining_uncertainty_cn：训练模型预测的是筹款成功，不一定等同于“感知信息价值”；模型依赖实验期外数据与实验期数据具有可比性；未直接测量捐赠者的信息处理心理过程。

- link_to_next_phase_cn：聚合分析之后需要排除替代结果变量、替代机制和因果识别问题，因此进入一系列稳健性检验。

##### evidence_pointers

1. Section 6.1

2. Table 7

3. Online Appendix C

#### 4. 替代结果变量与炫耀动机检验

- order：4

- name_cn：替代结果变量与炫耀动机检验

- question_cn：使用捐赠金额作为因变量时结果是否一致？展示好友捐赠信息导致的效果是否只是用户想在社交网络中“炫耀”的动机？

- inputs_and_setting_cn：同一实验数据；还将数据划分为“后续分享链接的捐赠者”和“未分享链接的捐赠者”两个子样本。

- designed_or_compared_object_cn：以log(Donation Amount+1)为因变量估计Tobit模型；比较分享与未分享子样本中的处理效应和交互项。

- baseline_control_or_counterfactual_cn：未分享子样本作为“不存在炫耀机会”的对照；主回归中二元捐赠结果作为结果变量选择的参照。

##### objective_metrics

1. Tobit模型中的处理效应和交互项

2. 分享/未分享样本系数差异的卡方检验

- analysis_method_cn：Tobit回归处理左删失0的捐赠金额；用χ²检验比较分享与未分享子样本的系数差异。

- main_result_cn：捐赠金额结果与二元捐赠结果一致：社交影响提高捐赠金额，信息性指数负向调节该效应。分享与未分享子样本的处理效应和交互项均无显著差异，说明炫耀动机不太可能是主要驱动。

- argumentative_role_cn：排除“社交可见性导致炫耀性捐赠”这一替代机制，同时证明结论不依赖于结果变量的测度方式。

- remaining_uncertainty_cn：分享行为是事后变量，可能受处理影响，分享子样本划分并非随机；其他动机（如利他、声誉、互惠）未被直接测量。

- link_to_next_phase_cn：继续用病例内匹配处理随机分组中的小不平衡，强化样本层面的内部效度。

##### evidence_pointers

1. Section 6.1

2. Section 6.2

3. Table 7

#### 5. 病例内倾向得分匹配

- order：5

- name_cn：病例内倾向得分匹配

- question_cn：在平衡性检查中目标金额和访问渠道存在微小显著差异时，匹配后样本是否仍能观察到相同结果？

- inputs_and_setting_cn：实验期全样本；按每个病例内部的处理组和对照组捐赠者进行倾向得分匹配。

- designed_or_compared_object_cn：在每个病例内，根据捐赠者层面控制变量（访问渠道、用户类型、地理位置、既往捐赠）对处理组与对照组进行匹配，生成匹配样本。

- baseline_control_or_counterfactual_cn：未匹配全样本作为参照；匹配后要求所有协变量在处理组和控制组之间无显著差异。

##### objective_metrics

1. 匹配样本中处理效应系数

2. 匹配样本中Treatment×Informativeness Index系数

3. 匹配后协变量平衡检验

- analysis_method_cn：病例内倾向得分匹配后，在匹配样本上重新估计逻辑回归。

- main_result_cn：匹配样本中处理效应和信息性指数交互项的结果与主分析一致，处理组与对照组在匹配样本中所有控制变量均值差异不显著。

- argumentative_role_cn：说明随机分组中少数变量的微小不平衡不会显著影响结论，增强实验的内部效度。

- remaining_uncertainty_cn：倾向得分匹配无法消除未观测混杂因素；它依赖可观测变量的正确建模。

- link_to_next_phase_cn：最后通过固定效应模型处理“反射问题”，排除群体层面共同因素导致的伪社会影响。

##### evidence_pointers

1. Section 6.3

2. Table 7 column 5

3. Table 2

#### 6. 反射问题固定效应检验

- order：6

- name_cn：反射问题固定效应检验

- question_cn：社交影响效应是否受到病例层面共同因素或捐赠者区域层面共同因素的干扰？

- inputs_and_setting_cn：实验期全样本；分别加入病例固定效应、捐赠者区域固定效应以及两者同时加入。

- designed_or_compared_object_cn：在线性概率模型中纳入病例固定效应（吸收病例层面外生效应）和捐赠者区域固定效应（吸收区域相关效应），以处理Manski反射问题中的外生效应和相关效应。

- baseline_control_or_counterfactual_cn：不含固定效应的主结果作为基准；反射问题框架中的内生效应是目标，外生和相关效应通过固定效应被吸收。

##### objective_metrics

1. Treatment系数

2. Treatment×Informativeness Index交互项系数

- analysis_method_cn：线性概率模型，按病例和捐赠者区域聚类稳健标准误。

- main_result_cn：加入病例固定效应、区域固定效应或两者后，处理效应仍正显著，交互项仍负显著。

- argumentative_role_cn：排除了“好友和焦点用户因共同案例特征或区域共同背景而行为相似”的反射问题解释，巩固社交影响的因果解释。

- remaining_uncertainty_cn：固定效应只控制可观测的区域内和病例内共同因素，不能排除更细粒度网络选择效应；小组层面的同群效应仍可能部分存在。

- link_to_next_phase_cn：稳健性链条完成后，进入讨论部分，将结果上升为机制贡献、理论贡献和管理含义。

##### evidence_pointers

1. Section 6.4

2. Table 8

## 各部分修辞架构

### abstract_moves

1. CONTEXT

2. GAP

3. RQ_OR_OBJECTIVE

4. METHOD_JUSTIFICATION

5. RESULT

6. CONTRIBUTION

7. BOUNDARY_CONDITION

### introduction_moves

1. CONTEXT

2. PRIOR_KNOWLEDGE

3. GAP

4. RQ_OR_OBJECTIVE

5. PRACTICAL_STAKES

6. PHENOMENON

7. LIMITATION

8. THEORY_PROPOSITION

9. METHOD_JUSTIFICATION

10. DESIGN_FEATURE

11. STUDY_OVERVIEW

12. RESULT

13. CONTRIBUTION

14. BOUNDARY_CONDITION

### theory_and_knowledge_moves

1. PRIOR_KNOWLEDGE

2. THEORY_INTRO

3. THEORY_PROPOSITION

4. MECHANISM

5. LIMITATION

6. GAP

7. HYPOTHESIS_OR_PROPOSITION

### artifact_design_moves

1. METHOD_JUSTIFICATION

2. DESIGN_FEATURE

3. BENCHMARK_OR_CONTRAST

4. REQUIREMENT

### evaluation_moves

1. STUDY_OVERVIEW

2. METHOD_JUSTIFICATION

3. BENCHMARK_OR_CONTRAST

4. RESULT

5. ROBUSTNESS_OR_BOUNDARY_TEST

### discussion_and_contribution_moves

1. RESULT

2. MECHANISM

3. CONTRIBUTION

4. BOUNDARY_CONDITION

5. LIMITATION_AND_FUTURE

6. PRACTICAL_STAKES

## 理论/知识到设计的翻译

### 知识/理论基础

1. 信息性社会影响理论（Deutsch & Gerard 1955; Burnkrant & Cousineau 1975; Cohen & Golden 1972）

2. 信号理论与信号优先级/显著性研究（Connelly et al. 2011; Morton & Podolny 2002; Higgins et al. 2011; Pollock et al. 2010）

3. 慈善捐赠与受助者属性文献（儿童脆弱性、性别差异）

4. 医疗众筹中的信息不对称研究（Kim et al. 2016; Young & Scheinberg 2017）

5. 似然比作为证据价值度量的方法论

- 理论—设计耦合：partial

- 耦合判定理由：理论确实前瞻性地提出了“社交影响是否被其他信息源削弱”的假设，并将“信息价值”机制与信号优先级理论相连；但关键的操作化——哪些属性具有高/低信息价值——并非纯理论推导，而是由MTurk调查的经验结果决定；现场实验中的具体处理（显示好友捐赠金额）来自社交影响文献，但属性分层高度依赖经验测量。因此属于理论影响问题与部分设计、但关键制品/变量操作化来自其他来源的“partial”耦合。

- 理论到设计翻译链：信息性社会影响理论说明个体把他人行为当作信息线索 → 在医疗众筹中，好友的捐赠可被视为对病例真实性的外部背书 → 设计上处理组显示“好友捐赠了X元”，对照组不显示 → 信号优先级理论预测高信息价值属性会成为更强信号 → 用MTurk调查识别高/低信息价值属性，再把数据按属性拆分为子样本比较处理效应 → 结果高信息价值属性存在时社交影响冗余，低信息价值属性存在时社交影响有用 → 用整体信息性指数验证同样逻辑。

### mapping_table

#### 1. 1

- theory_or_knowledge_claim_cn：个体的行为会被他人行为影响，且当个体缺少直接信息时，会把他人行为当作可信的信息线索。

- mechanism_cn：焦点用户看到好友已捐赠，推断好友拥有关于病例真实性的私有信息，从而将好友捐赠视为背书。

- design_requirement_cn：需要一个能独立操纵“好友捐赠信息可见性”的实验设计。

- artifact_choice_cn：在病例页筹款目标下方增加一行“某人捐赠了X元”，对照组不显示。

- evaluated_contrast_cn：处理组与对照组之间捐赠概率的差异，即社交影响主效应。

- objective_result_cn：处理组捐赠概率比对照组高约16.0%，效应显著。

##### evidence_pointers

1. Section 4.1

2. Section 5.1

3. Table 4

#### 2. 2

- theory_or_knowledge_claim_cn：当多个信号同时出现时，高优先级、高显著性的信号会压过低优先级信号，使后者变得冗余。

- mechanism_cn：高信息价值属性（如未成年患者、严重疾病）本身已足够让捐赠者相信病例真实需要帮助，因此好友捐赠信息不再提供额外信息。

- design_requirement_cn：需要对病例属性进行信息价值分层，并比较含与不含高信息价值属性的子样本。

- artifact_choice_cn：使用MTurk调查识别未成年患者、严重疾病、有商业保险（负向）为高信息价值属性；据此划分子样本。

- evaluated_contrast_cn：含高信息价值属性病例与不含该属性病例中处理效应的差异。

- objective_result_cn：含高信息价值属性的病例处理效应不显著；不含这些属性的病例处理效应显著为正。

##### evidence_pointers

1. Section 4.3

2. Section 5.1

3. Table 4

#### 3. 3

- theory_or_knowledge_claim_cn：低信息价值的单一信号不足以让个体下判断，但多个低信息价值信号可以互补并共同提供足够信息。

- mechanism_cn：当一个病例只有一个低信息价值属性（如女性患者）时，用户仍需好友捐赠信息作为补充线索；当两个低信息价值属性同时存在时，联合信息已经足以评估求助需要，社交影响的边际价值下降。

- design_requirement_cn：需要把分析限制在无高信息价值属性的病例中，并比较一个低信息价值属性与两个低信息价值属性组合下的处理效应。

- artifact_choice_cn：按低信息价值属性是否存在及其组合划分多个子样本。

- evaluated_contrast_cn：只含一个低信息价值属性 vs. 含两个低信息价值属性组合的处理效应。

- objective_result_cn：只含一个低信息价值属性时社交影响显著；含任意两个低信息价值属性组合时处理效应变得不显著。

##### evidence_pointers

1. Section 5.2

2. Section 5.3

3. Table 5

4. Table 6

#### 4. 4

- theory_or_knowledge_claim_cn：一个病例所有属性共同构成其整体信息价值，整体信息价值越高，外部信息线索的边际价值越低。

- mechanism_cn：综合信息性指数高的病例已经通过全部属性传达出较强的求助需要信号，因此好友捐赠信息对捐赠概率和金额的边际影响下降。

- design_requirement_cn：需要构造一个能够聚合所有属性信息价值的整体度量，并检验其与处理效应的交互。

- artifact_choice_cn：用实验期外数据训练逻辑回归预测筹款成功概率，将预测概率定义为信息性指数并加入交互项。

- evaluated_contrast_cn：信息性指数高与低的病例中处理效应的差异。

- objective_result_cn：Treatment×Informativeness Index交互项为负显著；信息性指数越高，社交影响越弱。

##### evidence_pointers

1. Section 6.1

2. Table 7

## 评价逻辑

### evaluation_modes

1. 捐赠者层面随机现场实验

2. MTurk调查作为调节变量的独立测量

3. 属性子样本的异质性分析

4. 实验期外数据训练的信息性指数聚合分析

5. Tobit模型替代结果变量检验

6. 分享/未分享子样本的替代机制检验

7. 病例内倾向得分匹配

8. 病例与区域固定效应反射问题检验

- why_these_evaluations_cn：需要一个干净的因果估计来证明社交影响确实改变真实捐赠行为，所以采用现场随机实验；需要一个独立于结果数据的构念测量来确定病例属性的信息价值，所以采用MTurk调查；只证明主效应还不够，需要用属性子样本检验边界条件；为了避免属性逐一分析的偶然性，需要聚合指数；为了让因果解释不被替代动机、样本不平衡和同群效应推翻，需要一系列稳健性检验。这些评价方法按“因果主效应—异质性边界—聚合推广—替代解释排除”的顺序相互衔接。

- benchmark_and_contrast_chain_cn：论文构建了多层对照链条：① 对照组 vs 处理组估计社交影响主效应；② 含高信息价值属性 vs 不含该属性的病例子样本估计信息价值对社交影响的调节作用；③ 无高信息价值属性病例中，一个低信息价值属性 vs 两个低信息价值属性组合进一步刻画联合信息价值；④ 实验期外模型生成的信息性指数从连续维度验证同样的调节逻辑；⑤ 分享/未分享、匹配/未匹配、加固定效应/不加固定效应等稳健性对照排除替代解释。

### claim_evidence_ledger

#### 1. 社交影响显著提高捐赠概率

- claim_cn：社交影响显著提高捐赠概率

- evidence_cn：全样本逻辑回归处理效应0.148，换算为16.0%，p<0.001

- strength_cn：强，来自大规模随机现场实验

#### 2. 高信息价值属性削弱社交影响

- claim_cn：高信息价值属性削弱社交影响

- evidence_cn：未成年、严重疾病、有商业保险子样本处理效应不显著；不含这些属性的子样本效应显著

- strength_cn：强，子样本内随机分配仍成立；但属性差异非随机分配

#### 3. 两个低信息价值属性组合足以削弱社交影响

- claim_cn：两个低信息价值属性组合足以削弱社交影响

- evidence_cn：六种两两组合子样本中处理效应均不显著

- strength_cn：中等，各组合样本量不同且部分t值接近0.05水平

#### 4. 整体信息性指数越高社交影响越弱

- claim_cn：整体信息性指数越高社交影响越弱

- evidence_cn：Treatment×Informativeness Index交互项在逻辑回归和Tobit中均显著为负

- strength_cn：强，但信息性指数来自筹款成功预测模型，非直接测量感知信息价值

#### 5. 炫耀动机不是主要驱动

- claim_cn：炫耀动机不是主要驱动

- evidence_cn：分享与未分享子样本的处理效应和交互项无显著差异

- strength_cn：中等，分享行为是事后变量，非随机

#### 6. 社交影响主要来自信息性而非规范性

- claim_cn：社交影响主要来自信息性而非规范性

- evidence_cn：如果规范性支配，效应不应随信息价值变化；但观察到的效应随信息价值变化而被削弱

- strength_cn：间接证据，未直接测量规范性社会影响

- internal_validity_strategy_cn：采用捐赠者层面随机分配且分配固定，保证个体层面可比性；通过平衡性检查确认两组在病例和捐赠者变量上总体平衡；用病例内倾向得分匹配处理微小不平衡；用病例和区域固定效应处理反射问题；实验时间避开节假日和特殊事件；只纳入好友分享链接产生的访问，排除平台推广消息；按病例聚类标准误。

- external_validity_strategy_cn：平台规模大（超过4亿活跃用户，2019年筹集106亿元），样本来自真实捐赠者而非实验室被试；处理是真实页面上的信息展示；作者将结论一般化到其他医疗众筹、点对点平台和亲社会活动，但强调在非利他、强成本收益分析的场景中信息处理投入可能更强。

- what_is_not_actually_tested_cn：文中没有直接测量捐赠者的心理过程，因此“信息性而非规范性”是从调节模式推断的；没有检验发送链接的好友身份、社会关系强度、捐赠金额锚定效应；没有检测捐赠者匿名性变化的影响；没有直接测量社交影响对分享行为本身的作用；也没有检验社交影响是否真正提高总福利，只根据熵值讨论了资源分布更平等。

## 贡献闭环

- technical_claim_cn：在医疗众筹平台上展示好友捐赠信息会提高真实捐赠概率和捐赠金额，且该效应随病例整体信息价值提高而下降。

- artifact_claim_cn：页面上额外显示的“好友捐赠了X元”这一设计元素是导致处理组捐赠率升高的可识别设计组成部分；其效果受病例属性信息价值调节。

- mechanism_claim_cn：本研究中的社交影响主要来自信息性社会影响：好友捐赠作为病例真实性的外部信号，其边际价值取决于病例本身是否已有足够信息价值的属性。

- boundary_claim_cn：该效应边界是医疗众筹等以非金钱动机为主、信息不对称和不确定性较高的情境；在用户更强进行成本收益分析的场景中，可能观察到更强或不同的信息源交互。

- reusable_design_knowledge_cn：平台或筹款者不应把社交影响视为普遍有效工具；应先评估病例或产品已有信息源的信息价值。若已有高信息价值信号，社交影响冗余；若信息价值不足，社交影响可有效补充；多个弱信号组合也能替代社交影响。

- theoretical_contribution_cn：把社会影响研究从“是否存在、强度如何”推进到“如何与其他信息源交互”；为医疗众筹和慈善捐赠文献提供了捐赠者层面的因果证据；用信息价值调节模式区分信息性与规范性社会影响。

- how_discussion_closes_intro_gap_cn：引言提出的缺口是“没有研究系统检验社交影响如何与多种其他信息来源交互”；讨论部分直接以“本文是最早系统研究这一交互的研究之一”回应，并用“信息价值决定社交影响边际价值”贯通引言中的两种竞争可能性：不是锁定效应，而是信息性社交影响让低信息价值病例获得更多帮助。

- overclaim_or_unsupported_leaps_cn：从“处理效应随信息价值下降”推断“社交影响主要是信息性”属于间接推断；MTurk调查在美国样本上界定的信息价值被直接用于解释中国平台行为，存在文化迁移风险；熵值下降被解读为“更平等”，但未检验捐赠者福利、患者结果或资金配置效率；信息性指数基于筹款成功而非真实感知信息价值，可能混入其他因素。

## 句级写作动作图谱

### 1. Introduction P1 S1

- order：1

- section：Introduction

- locator：Introduction P1 S1

- move_code：CONTEXT

- paraphrase_cn：指出在日益相互联系的世界中，用户行为会受到线上和线下其他人行为的影响。

- rhetorical_function_cn：开篇建立社会影响具有广泛重要性的背景。

- depends_on_cn：无需前置。

- sets_up_cn：为引出“还需研究社会影响与其他信息来源如何交互”做铺垫。

- evidence_pointer：Introduction P1

### 2. Introduction P1 S2

- order：2

- section：Introduction

- locator：Introduction P1 S2

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：已有研究考察了社会影响是否存在以及其影响在不同条件下如何变化。

- rhetorical_function_cn：总结既有知识，为紧接着指出缺口服务。

- depends_on_cn：建立在第1句背景之上。

- sets_up_cn：让读者预期下一步会指出尚未被研究的方面。

- evidence_pointer：Introduction P1

### 3. Introduction P1 S3

- order：3

- section：Introduction

- locator：Introduction P1 S3

- move_code：GAP

- paraphrase_cn：但没有研究系统地检验社会影响如何与多种其他信息来源交互。

- rhetorical_function_cn：明确研究缺口，这是全文的问题来源。

- depends_on_cn：依赖第2句对已有研究的概括。

- sets_up_cn：直接引出本文目标，使研究有明确位置。

- evidence_pointer：Introduction P1

### 4. Introduction P1 S4

- order：4

- section：Introduction

- locator：Introduction P1 S4

- move_code：RQ_OR_OBJECTIVE

- paraphrase_cn：本文旨在填补该空白，通过医疗众筹现场实验考察社会影响如何随病例属性的信息价值变化。

- rhetorical_function_cn：提出研究问题与研究场景。

- depends_on_cn：承接第3句的缺口。

- sets_up_cn：预告后文情境、实验和方法。

- evidence_pointer：Introduction P1

### 5. Introduction P2 S1–S2

- order：5

- section：Introduction

- locator：Introduction P2 S1–S2

- move_code：CONTEXT

- paraphrase_cn：医疗众筹是捐赠式众筹的一种主要类型，近年来规模和受欢迎程度迅速增长。

- rhetorical_function_cn：为研究提供具体领域背景，并强调现实重要性。

- depends_on_cn：承接第4句提到的医疗众筹情境。

- sets_up_cn：为后面讨论不同病例获得资源不平等做铺垫。

- evidence_pointer：Introduction P2

### 6. Introduction P2 S3

- order：6

- section：Introduction

- locator：Introduction P2 S3

- move_code：PHENOMENON

- paraphrase_cn：并非所有筹款者都能成功说服捐赠者，不同病例获得关注和支持的差异很大。

- rhetorical_function_cn：描述现实经验现象，说明问题普遍。

- depends_on_cn：依赖第5句对众筹规模的描述。

- sets_up_cn：引出病例属性影响捐赠的研究必要性。

- evidence_pointer：Introduction P2

### 7. Introduction P2 S4–S5

- order：7

- section：Introduction

- locator：Introduction P2 S4–S5

- move_code：PRACTICAL_STAKES

- paraphrase_cn：筹款者需要知道不同属性如何影响捐赠意愿以及社交影响是否与之交互；盲目使用社交影响可能无效甚至有害。

- rhetorical_function_cn：把现象转化为实际管理后果。

- depends_on_cn：基于第6句的不平等现象。

- sets_up_cn：解释为什么研究交互机制有直接实践价值。

- evidence_pointer：Introduction P2

### 8. Introduction P3 S1

- order：8

- section：Introduction

- locator：Introduction P3 S1

- move_code：LIMITATION

- paraphrase_cn：已有研究没有详细考察社交影响如何随其他来源提供的信息价值而变化。

- rhetorical_function_cn：再次指出文献局限，把缺口具体化。

- depends_on_cn：承接第3句的一般缺口。

- sets_up_cn：为下一句提出两种竞争预期作铺垫。

- evidence_pointer：Introduction P3

### 9. Introduction P3 S2–S3

- order：9

- section：Introduction

- locator：Introduction P3 S2–S3

- move_code：THEORY_PROPOSITION

- paraphrase_cn：一种可能是社交影响在高信息价值病例中更明显，因为社会连接会造成锁定效应；另一种可能是高信息价值属性使社交影响的信息作用被削弱，因为人们会关注更显著或优先级更高的信号。

- rhetorical_function_cn：呈现两种竞争的理论预期，突出研究张力。

- depends_on_cn：基于第8句提到的文献局限。

- sets_up_cn：让实证结果能够区分两种解释。

- evidence_pointer：Introduction P3

### 10. Introduction P3 S4

- order：10

- section：Introduction

- locator：Introduction P3 S4

- move_code：RQ_OR_OBJECTIVE

- paraphrase_cn：本文旨在填补空白，系统考察社交影响如何随其他信息来源的信息价值改变。

- rhetorical_function_cn：在理论张力之后重申研究目标。

- depends_on_cn：依赖第8、9句的缺口和预期。

- sets_up_cn：预告后文的方法选择。

- evidence_pointer：Introduction P3

### 11. Introduction P4 S1

- order：11

- section：Introduction

- locator：Introduction P4 S1

- move_code：STUDY_OVERVIEW

- paraphrase_cn：作者在中国领先医疗众筹平台开展涉及超过70万捐赠者的大规模捐赠者层面随机现场实验。

- rhetorical_function_cn：预告主要实证方法。

- depends_on_cn：回应第10句的研究目标。

- sets_up_cn：说明实验规模和数据基础。

- evidence_pointer：Introduction P4

### 12. Introduction P4 S2–S3

- order：12

- section：Introduction

- locator：Introduction P4 S2–S3

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：该平台病例信息完全靠用户通过社交链接分享传播，捐赠者只能点击分享链接访问页面，不能搜索或浏览，因此适合干净地研究社交影响。

- rhetorical_function_cn：解释为什么选择这个平台作为实验现场。

- depends_on_cn：承接第11句的实验场景。

- sets_up_cn：为随机化设计和排除搜索排名等混淆提供依据。

- evidence_pointer：Introduction P4

### 13. Introduction P4 S4–S5

- order：13

- section：Introduction

- locator：Introduction P4 S4–S5

- move_code：DESIGN_FEATURE

- paraphrase_cn：用户在实验期内首次点击病例页时随机分入处理组或对照组，分配固定；处理组页面显示发来链接的好友捐赠金额，对照组不显示。

- rhetorical_function_cn：描述实验核心操纵。

- depends_on_cn：继承第12句的平台背景。

- sets_up_cn：为后文估计社交影响的因果效应提供基础。

- evidence_pointer：Introduction P4

### 14. Introduction P5 S1–S2

- order：14

- section：Introduction

- locator：Introduction P5 S1–S2

- move_code：RESULT

- paraphrase_cn：同时用MTurk调查评估病例属性的信息价值，发现患者年龄、严重疾病和有商业保险具有高信息价值，其他属性较弱。

- rhetorical_function_cn：在引言中提前报告调查结果，让读者知道属性分层的依据。

- depends_on_cn：依赖第13句介绍的实验。

- sets_up_cn：为后文将实验数据按属性分层做铺垫。

- evidence_pointer：Introduction P5

### 15. Introduction P5 S3

- order：15

- section：Introduction

- locator：Introduction P5 S3

- move_code：STUDY_OVERVIEW

- paraphrase_cn：作者据此考察社交影响如何因不同病例属性的信息价值而不同。

- rhetorical_function_cn：提示接下来分析框架的核心比较。

- depends_on_cn：基于第14句的调查结果。

- sets_up_cn：引导读者关注“信息价值”作为调节变量。

- evidence_pointer：Introduction P5

### 16. Introduction P6 S1–S3

- order：16

- section：Introduction

- locator：Introduction P6 S1–S3

- move_code：RESULT

- paraphrase_cn：高信息价值属性存在时社交影响不显著；只有低信息价值属性时社交影响显著为正；多个低信息价值属性组合会削弱社交影响。

- rhetorical_function_cn：概括核心实证结果。

- depends_on_cn：依赖第13、14句所述实验和调查。

- sets_up_cn：为贡献和理论解释提供结果支撑。

- evidence_pointer：Introduction P6

### 17. Introduction P6 S4

- order：17

- section：Introduction

- locator：Introduction P6 S4

- move_code：RESULT

- paraphrase_cn：用实验期外数据训练模型计算信息性指数后，发现社交影响提高捐赠概率和金额，但该作用在信息性指数更高时减弱。

- rhetorical_function_cn：在引言中预告聚合分析的一致性结果。

- depends_on_cn：承接第16句核心结果。

- sets_up_cn：强调结果不是单一属性的偶然现象。

- evidence_pointer：Introduction P6

### 18. Introduction P7 S1

- order：18

- section：Introduction

- locator：Introduction P7 S1

- move_code：CONTRIBUTION

- paraphrase_cn：这些发现为医疗众筹平台和筹款者提供了关于社交影响与病例信息价值如何共同驱动捐赠的洞见。

- rhetorical_function_cn：开始陈述贡献。

- depends_on_cn：依赖第16、17句结果。

- sets_up_cn：为后文管理含义和理论贡献铺垫。

- evidence_pointer：Introduction P7

### 19. Introduction P7 S2

- order：19

- section：Introduction

- locator：Introduction P7 S2

- move_code：BOUNDARY_CONDITION

- paraphrase_cn：作者认为发现可以推广到其他点对点平台和亲社会活动。

- rhetorical_function_cn：界定贡献的适用范围。

- depends_on_cn：基于第18句的贡献。

- sets_up_cn：提示读者不要只把结果理解为单一平台。

- evidence_pointer：Introduction P7

### 20. Introduction P7 S3

- order：20

- section：Introduction

- locator：Introduction P7 S3

- move_code：STUDY_OVERVIEW

- paraphrase_cn：文末说明后文结构：文献、假设、方法、结果、稳健性、讨论。

- rhetorical_function_cn：给读者路径图。

- depends_on_cn：无需前置。

- sets_up_cn：为全文结构立下路标。

- evidence_pointer：Introduction P7

### 21. Section 2.1 P1

- order：21

- section：Section 2.1

- locator：Section 2.1 P1

- move_code：CONTEXT

- paraphrase_cn：医疗众筹面临的核心挑战是信息不对称：捐赠者难以确认患者病情是否真实、是否没有其他资源。

- rhetorical_function_cn：建立研究情境的理论基础。

- depends_on_cn：承接引言中的现实问题。

- sets_up_cn：说明为什么信息线索对捐赠决策重要。

- evidence_pointer：Section 2.1

### 22. Section 2.1 P2

- order：22

- section：Section 2.1

- locator：Section 2.1 P2

- move_code：LIMITATION

- paraphrase_cn：少数研究医疗众筹可信度的研究主要依赖聚合数据或访谈，难以识别具体病例属性对捐赠的影响。

- rhetorical_function_cn：指出方法学上的空缺。

- depends_on_cn：基于第21句的信息不对称背景。

- sets_up_cn：为本文捐赠者级随机实验提供定位。

- evidence_pointer：Section 2.1

### 23. Section 2.1 P3

- order：23

- section：Section 2.1

- locator：Section 2.1 P3

- move_code：GAP

- paraphrase_cn：据作者所知，没有研究在医疗众筹情境中探索社交影响和不同信息来源如何影响捐赠。

- rhetorical_function_cn：再次明确缺口。

- depends_on_cn：继承第22句对现有研究的批评。

- sets_up_cn：为本文的贡献声明铺路。

- evidence_pointer：Section 2.1

### 24. Section 2.2 P1

- order：24

- section：Section 2.2

- locator：Section 2.2 P1

- move_code：LIMITATION

- paraphrase_cn：既有慈善捐赠研究大多关注捐赠者属性，且通常把筹款者当作同质群体，没有考察筹款者属性如何改变捐赠意愿。

- rhetorical_function_cn：指出慈善捐赠文献的盲点。

- depends_on_cn：不需要前文太多。

- sets_up_cn：引出医疗众筹中患者属性变异的价值。

- evidence_pointer：Section 2.2

### 25. Section 2.2 P2

- order：25

- section：Section 2.2

- locator：Section 2.2 P2

- move_code：THEORY_PROPOSITION

- paraphrase_cn：儿童被视为需要关怀的脆弱群体，儿童慈善在捐赠者中尤其受欢迎，因此年轻患者年龄可能具有高信息价值。

- rhetorical_function_cn：从已有知识推导属性信息价值。

- depends_on_cn：基于慈善文献。

- sets_up_cn：为MTurk调查中“未成年患者=高信息价值”提供理论预期。

- evidence_pointer：Section 2.2

### 26. Section 2.2 P3

- order：26

- section：Section 2.2

- locator：Section 2.2 P3

- move_code：THEORY_PROPOSITION

- paraphrase_cn：关于性别与健康结果的研究证据混杂，因此患者性别可能只有低信息价值。

- rhetorical_function_cn：从矛盾文献推导低信息价值。

- depends_on_cn：依赖医疗性别差异文献。

- sets_up_cn：为调查中“女性患者=低信息价值”提供理论解释。

- evidence_pointer：Section 2.2

### 27. Section 2.2 P4

- order：27

- section：Section 2.2

- locator：Section 2.2 P4

- move_code：GAP

- paraphrase_cn：没有研究跨属性比较信息价值，也没有系统考察它们如何调节社交影响。

- rhetorical_function_cn：把缺口从单一文献扩展到跨属性比较。

- depends_on_cn：基于第25、26句的零散知识。

- sets_up_cn：为本文的调查设计和交互分析提供依据。

- evidence_pointer：Section 2.2

### 28. Section 2.3 P1

- order：28

- section：Section 2.3

- locator：Section 2.3 P1

- move_code：THEORY_INTRO

- paraphrase_cn：信息性社会影响指个体从他人行为中推断信息以减少不确定性，把他人行为当作可信信息源。

- rhetorical_function_cn：引入核心理论构念。

- depends_on_cn：基于社会影响文献。

- sets_up_cn：为假设1的机制提供理论工具。

- evidence_pointer：Section 2.3

### 29. Section 2.3 P2

- order：29

- section：Section 2.3

- locator：Section 2.3 P2

- move_code：GAP

- paraphrase_cn：但没有研究考察社会影响如何因多种信息源的存在而变化。

- rhetorical_function_cn：在社会影响文献内再次标记缺口。

- depends_on_cn：依赖第28句的理论介绍。

- sets_up_cn：直接引出后文的假设。

- evidence_pointer：Section 2.3

### 30. Section 3 P1

- order：30

- section：Section 3

- locator：Section 3 P1

- move_code：MECHANISM

- paraphrase_cn：感知求助需要是捐赠的主要动机；由于信息不对称，捐赠者会依赖病例属性推断真实性；好友的捐赠因其可能有私有医学知识或与患者有联系而被视为背书。

- rhetorical_function_cn：解释为什么展示好友捐赠信息会产生信息性社会影响。

- depends_on_cn：依赖第28句的信息性社会影响理论。

- sets_up_cn：为假设1提供因果链条。

- evidence_pointer：Section 3

### 31. Section 3 H1

- order：31

- section：Section 3

- locator：Section 3 H1

- move_code：HYPOTHESIS_OR_PROPOSITION

- paraphrase_cn：假设1：社会影响提高焦点用户向病例捐赠的可能性。

- rhetorical_function_cn：给出第一个可检验假设。

- depends_on_cn：依靠第30句的机制。

- sets_up_cn：由实验结果第一个验证。

- evidence_pointer：Section 3

### 32. Section 3 P2

- order：32

- section：Section 3

- locator：Section 3 P2

- move_code：MECHANISM

- paraphrase_cn：社会影响的边际价值取决于病例属性提供的替代信息的多少。

- rhetorical_function_cn：把调节机制概括为“边际价值取决于替代信息”。

- depends_on_cn：承接第30句的机制。

- sets_up_cn：为假设2提供逻辑基础。

- evidence_pointer：Section 3

### 33. Section 3 P2

- order：33

- section：Section 3

- locator：Section 3 P2

- move_code：THEORY_PROPOSITION

- paraphrase_cn：当多个信号并存时，高优先级信号会取代或贬低低优先级信号；若底层质量已被更直接的信号捕获，原信号的信息作用变冗余。

- rhetorical_function_cn：从信号理论引入信号替代逻辑。

- depends_on_cn：依赖信号优先级文献。

- sets_up_cn：说明高信息价值属性为何让好友捐赠信息冗余。

- evidence_pointer：Section 3

### 34. Section 3 P3

- order：34

- section：Section 3

- locator：Section 3 P3

- move_code：MECHANISM

- paraphrase_cn：当一个病例没有高信息价值属性时，多个低信息价值属性可以提供独特且互补的信息，整体上提高信息价值并削弱社会影响的边际作用。

- rhetorical_function_cn：为低信息价值属性组合的调节作用提供机制。

- depends_on_cn：依赖信号互补文献。

- sets_up_cn：为假设2的延伸部分提供依据。

- evidence_pointer：Section 3

### 35. Section 3 H2

- order：35

- section：Section 3

- locator：Section 3 H2

- move_code：HYPOTHESIS_OR_PROPOSITION

- paraphrase_cn：假设2：病例属性的信息价值越高，社会影响对捐赠概率的正向作用越弱。

- rhetorical_function_cn：给出核心调节假设。

- depends_on_cn：依赖第32–34句。

- sets_up_cn：为第4、5节的子样本分析提供目标。

- evidence_pointer：Section 3

### 36. Section 4.1 P1

- order：36

- section：Section 4.1

- locator：Section 4.1 P1

- move_code：CONTEXT

- paraphrase_cn：平台采用“留全即得”模型、不收费、有七天反欺诈审查期，规模庞大。

- rhetorical_function_cn：介绍实验平台背景，说明其代表性。

- depends_on_cn：不需要前置。

- sets_up_cn：为后文实验设计提供合理性。

- evidence_pointer：Section 4.1

### 37. Section 4.1 P2–P3

- order：37

- section：Section 4.1

- locator：Section 4.1 P2–P3

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：平台几乎完全依靠用户通过第三方社交媒体链接分享来传播病例，捐赠者不能搜索或浏览平台，只能点击链接进入。

- rhetorical_function_cn：说明为什么该平台能干净地识别社交影响而不会受搜索排名和内容推荐混淆。

- depends_on_cn：承接第36句平台介绍。

- sets_up_cn：为随机分组和“好友捐赠信息”与“发链接好友”的匹配提供条件。

- evidence_pointer：Section 4.1

### 38. Section 4.1 P4–P5

- order：38

- section：Section 4.1

- locator：Section 4.1 P4–P5

- move_code：DESIGN_FEATURE

- paraphrase_cn：实验为期四天，用户在首次点击病例链接时被随机分入处理或对照组且固定；处理组额外显示好友捐赠信息。

- rhetorical_function_cn：描述随机化操作细节。

- depends_on_cn：基于第37句的平台传播机制。

- sets_up_cn：为平衡性检验和因果识别做好交代。

- evidence_pointer：Section 4.1

### 39. Section 4.2 P1

- order：39

- section：Section 4.2

- locator：Section 4.2 P1

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：作者清理数据：剔除未通过平台评价、性别特异性疾病、平台主动推送等观测，最终聚合到捐赠者-病例层。

- rhetorical_function_cn：解释样本构建过程，减少噪音和权重偏差。

- depends_on_cn：基于第38句的实验设计。

- sets_up_cn：为最终样本量757,094和统计模型提供数据基础。

- evidence_pointer：Section 4.2

### 40. Section 4.3 P1–P2

- order：40

- section：Section 4.3

- locator：Section 4.3 P1–P2

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：作者借鉴似然比概念设计在线调查，通过比较一个取值集相对另一取值集在多大程度上让受访者认为病例真实需要帮助，来评价属性的信息价值。

- rhetorical_function_cn：为信息价值的测量提供方法论依据。

- depends_on_cn：不需要前文。

- sets_up_cn：解释表3结果是如何产生的。

- evidence_pointer：Section 4.3

### 41. Section 4.3 P4

- order：41

- section：Section 4.3

- locator：Section 4.3 P4

- move_code：RESULT

- paraphrase_cn：调查结果识别出高信息价值属性为未成年患者、严重疾病和有商业保险（负向），低信息价值属性为患者性别、目标金额、照片数量和描述长度。

- rhetorical_function_cn：给出现测构念的结果，作为后续分层变量。

- depends_on_cn：依赖第40句的调查设计。

- sets_up_cn：为第5节按属性拆分子样本提供直接依据。

- evidence_pointer：Section 4.3, Table 3

### 42. Section 4.4 P1

- order：42

- section：Section 4.4

- locator：Section 4.4 P1

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：作者把数据按是否含有高/低信息价值属性划分成子样本，并用逻辑回归估计处理效应，同时加入控制变量及其与处理的交互。

- rhetorical_function_cn：说明主分析框架如何在随机实验中做异质性分析。

- depends_on_cn：依赖第39、41句的数据和属性分层。

- sets_up_cn：为第5节结果表格提供方法依据。

- evidence_pointer：Section 4.4

### 43. Section 5 intro P1

- order：43

- section：Section 5

- locator：Section 5 intro P1

- move_code：STUDY_OVERVIEW

- paraphrase_cn：作者预告将分四步报告结果：先逐个比较高信息价值属性；再在无高信息价值属性病例中逐个考察低信息价值属性；再分析两个低信息价值属性组合；最后用整体信息性指数。

- rhetorical_function_cn：为复杂的异质性分析提供清晰路线图。

- depends_on_cn：依赖第42句的分析框架。

- sets_up_cn：让读者预期第5.1至5.3和6.1节的逻辑顺序。

- evidence_pointer：Section 5

### 44. Section 5.1 P1

- order：44

- section：Section 5.1

- locator：Section 5.1 P1

- move_code：RESULT

- paraphrase_cn：全样本结果显示社交影响使捐赠概率增加约16.0%，统计显著，假设1得到支持。

- rhetorical_function_cn：报告主效应并直接对照假设1。

- depends_on_cn：依赖第39、42句数据和分析。

- sets_up_cn：为后续调节效应提供基线。

- evidence_pointer：Section 5.1, Table 4

### 45. Section 5.1 P2–P4

- order：45

- section：Section 5.1

- locator：Section 5.1 P2–P4

- move_code：RESULT

- paraphrase_cn：在未成年患者、严重疾病和有商业保险的病例中，处理效应不显著；在不含相应属性的病例中，处理效应显著为正。

- rhetorical_function_cn：用三组对照证据支持高信息价值削弱社交影响。

- depends_on_cn：依赖第41句调查对高信息价值属性的识别。

- sets_up_cn：形成对假设2的第一部分支持。

- evidence_pointer：Section 5.1, Table 4

### 46. Section 5.2 P1–P2

- order：46

- section：Section 5.2

- locator：Section 5.2 P1–P2

- move_code：RESULT

- paraphrase_cn：在无高信息价值属性的病例中，社交影响显著提升捐赠概率约20.9%；在只存在女性患者、较多照片、较长描述或较高目标金额等单个低信息价值属性时，社交影响仍显著。

- rhetorical_function_cn：证明单低信息价值属性不足以让社交影响失效。

- depends_on_cn：依赖第45句的高信息价值对照。

- sets_up_cn：引出第5.3节的两个低信息价值属性组合分析。

- evidence_pointer：Section 5.2, Table 5

### 47. Section 5.3 P1

- order：47

- section：Section 5.3

- locator：Section 5.3 P1

- move_code：RESULT

- paraphrase_cn：在无高信息价值属性且同时含有任意两个低信息价值属性组合的病例中，社交影响变得不显著。

- rhetorical_function_cn：验证低信息价值属性的联合信息可以替代社交影响。

- depends_on_cn：依赖第46句单个低信息价值的显著结果。

- sets_up_cn：为聚合信息性指数提出更一般的版本。

- evidence_pointer：Section 5.3, Table 6

### 48. Section 6.1 P1–P2

- order：48

- section：Section 6.1

- locator：Section 6.1 P1–P2

- move_code：RESULT

- paraphrase_cn：用实验期外数据训练的模型生成信息性指数后，处理效应仍正显著，信息性指数主效应正显著，二者交互项负显著。

- rhetorical_function_cn：从属性逐一分析推广到整体信息价值。

- depends_on_cn：依赖第47句的组合逻辑和第40、41句的信息价值概念。

- sets_up_cn：为随后稳健性检验提供聚合层面证据。

- evidence_pointer：Section 6.1, Table 7

### 49. Section 6.2–6.4

- order：49

- section：Section 6.2–6.4

- locator：Section 6.2–6.4

- move_code：ROBUSTNESS_OR_BOUNDARY_TEST

- paraphrase_cn：作者进行了多组稳健性检验：Tobit捐赠金额结果一致；分享与未分享子样本中处理效应无显著差异，排除炫耀动机；病例内匹配样本结果一致；加入病例和区域固定效应后交互项仍负显著，排除反射问题。

- rhetorical_function_cn：打包报告稳健性结果，证明核心结论不依赖特定测度、替代机制或识别假设。

- depends_on_cn：依赖第48句的聚合指数分析。

- sets_up_cn：让讨论部分的机制解释更有说服力。

- evidence_pointer：Section 6.2–6.4, Tables 7 and 8

### 50. Section 7.1 P1–P2

- order：50

- section：Section 7.1

- locator：Section 7.1 P1–P2

- move_code：CONTRIBUTION

- paraphrase_cn：作者总结核心发现，并指出结果意味着本情境中的社交影响主要是信息性的，而非规范性的。

- rhetorical_function_cn：把实证结果上升为理论机制贡献。

- depends_on_cn：依赖第49句稳健性结果。

- sets_up_cn：为后文理论贡献和管理含义定调。

- evidence_pointer：Section 7.1

### 51. Section 7.1 P3

- order：51

- section：Section 7.1

- locator：Section 7.1 P3

- move_code：CONTRIBUTION

- paraphrase_cn：作者说明本文对社会影响文献、医疗众筹文献和慈善捐赠文献的理论贡献。

- rhetorical_function_cn：明确贡献对象和文献定位。

- depends_on_cn：基于第50句的机制结论。

- sets_up_cn：回应引言中提出的研究缺口。

- evidence_pointer：Section 7.1

### 52. Section 7.2 P1–P4

- order：52

- section：Section 7.2

- locator：Section 7.2 P1–P4

- move_code：LIMITATION_AND_FUTURE

- paraphrase_cn：作者承认无法直接测量心理过程、缺少好友身份和社会网络信息、匿名性不明确、未检验捐赠金额锚定效应，并提出未来研究方向。

- rhetorical_function_cn：通过承认数据限制来界定贡献范围。

- depends_on_cn：依赖全文结果的解释边界。

- sets_up_cn：为管理含义提供更谨慎的边界。

- evidence_pointer：Section 7.2

### 53. Section 7.3 P1

- order：53

- section：Section 7.3

- locator：Section 7.3 P1

- move_code：PRACTICAL_STAKES

- paraphrase_cn：作者指出社交影响能显著帮助缺乏高信息价值属性的病例，并通过处理组熵值更低说明捐赠分布更均匀。

- rhetorical_function_cn：把结果转化为资源分配的实践含义。

- depends_on_cn：依赖核心结果和熵值描述。

- sets_up_cn：引导平台和筹款者将社交影响用于弱信息案例。

- evidence_pointer：Section 7.3

### 54. Section 7.3 P2

- order：54

- section：Section 7.3

- locator：Section 7.3 P2

- move_code：BOUNDARY_CONDITION

- paraphrase_cn：作者强调社交影响不是所有说服问题的普遍解，需要先评估具体情境中其他信息源的质量。

- rhetorical_function_cn：为实践建议设置适用条件。

- depends_on_cn：基于第53句的管理含义。

- sets_up_cn：防止读者把结论过度推广到所有平台和情境。

- evidence_pointer：Section 7.3

## 写作技术

- gap_construction_cn：作者使用多重缺口的叠加：先是“没有研究系统研究社交影响与多种信息源交互”，再在医疗众筹文献中补一个“捐赠者级随机实验缺失”，在慈善捐赠文献中补一个“筹款者属性异质性缺失”，最后在社会影响文献中补一个“条件性缺失”。每一层缺口都与前文相连，形成越来越具体的空白。

- signposting_cn：引言最后给出全文结构；第5节开头提前用“四步走”预告结果分析顺序；每个小节的标题和段首句都直接说明要检验哪个假设或哪类属性。

- transition_logic_cn：每个阶段结尾都留下一个“尚未完成”的问题：调查结果引出属性分层；主效应引出调节分析；单一属性引出组合；组合引出聚合指数；聚合分析引出稳健性；稳健性引出讨论。过渡句如“我们接下来检验社交影响如何与……”“这促使我们考察……”直接连接相邻阶段。

- claim_evidence_rhythm_cn：论文遵循“假设→回归表格→系数解释→对假设的判定”的节奏。每个结果段先报告具体系数和百分数，再解释该数字对假设意味着什么，因此读者始终知道证据支持程度。

- benchmark_narrative_cn：benchmark和对照不是独立的性能比较，而是嵌入概念的“有无信息价值”层级：对照组提供社交影响基线；高/低属性子样本提供调节对照；两个低信息属性组合提供联合信号对照；信息性指数提供连续维度的整体对照。

- theory_return_cn：在讨论部分，作者把“结果随信息价值下降”回译为“信息性社会影响占主导”，并重提引言中的锁定效应与信号替代两种可能，用数据决策支持后者；随后把这种机制回接到社会影响、医疗众筹和慈善文献中。

- contribution_positioning_cn：贡献陈述采用“本文是第一批……”“我们补充/扩展了……”的句式，将贡献挂在既有文献的具体节点上，而不是泛泛说“有实践意义”。

- novelty_protection_cn：作者用大规模真实平台数据、随机分配、多重稳健性、聚合指数和理论机制共同保护贡献：即使某个单一属性效应不够强，聚合指数和多个组合仍能说明系统规律；即使存在替代机制，分享/未分享样本和固定效应也能削弱其解释力。

## 可复用研究与写作程序

### structure_steps

#### 1. 1

- step：1

- writing_job_cn：开篇用“已有研究虽多，但未系统检验X与Y交互”的方式制造缺口。

- research_job_cn：找到真实场景中两个理论构念的交互问题，并确定研究场景。

- required_evidence_cn：需要一组能说明现实重要性的现象或数据，例如众筹规模、不均衡结果。

- transition_to_next_cn：缺口必须是“如果填补，会有实践或理论后果”，从而导向研究问题。

#### 2. 2

- step：2

- writing_job_cn：分别从三个文献流回顾，每个文献流末尾都指出与本文相关的局限。

- research_job_cn：把问题放入社会影响、慈善捐赠、众筹等文献脉络。

- required_evidence_cn：需要与机制相关的既有理论和经验证据。

- transition_to_next_cn：把文献空白压缩成可检验假设。

#### 3. 3

- step：3

- writing_job_cn：用机制链解释为什么自变量影响因变量，并写出可检验假设。

- research_job_cn：提出具体因果机制（如信息性社会影响、信号替代）。

- required_evidence_cn：需要至少一个可操作的中介/调节变量（如信息价值）。

- transition_to_next_cn：假设要求设计能够构造或测量该变量的研究。

#### 4. 4

- step：4

- writing_job_cn：描述实验平台、随机化、处理组对照组的差别；说明为什么该平台适合因果识别。

- research_job_cn：在真实平台实施随机干预，或者在可访问的实地环境中操纵数字设计。

- required_evidence_cn：需要随机分配记录、平衡性检验、样本量。

- transition_to_next_cn：用独立测量（如调查、外部模型）为调节变量提供操作化。

#### 5. 5

- step：5

- writing_job_cn：先报告主效应，再按调节变量拆分子样本，逐个检验假设。

- research_job_cn：估计主效应和异质性效应；使用稳健标准误和控制变量。

- required_evidence_cn：主效应显著；子样本效应差异清晰。

- transition_to_next_cn：从单一调节变量升级到聚合度量或组合效应。

#### 6. 6

- step：6

- writing_job_cn：用额外数据构造聚合指标，把属性级结果推广到整体层面。

- research_job_cn：寻找外部数据或模型来验证调节变量的连续度量。

- required_evidence_cn：交互项符号和显著性在聚合层面上同样成立。

- transition_to_next_cn：用稳健性检验排除替代结果变量、替代机制、样本偏差和识别问题。

#### 7. 7

- step：7

- writing_job_cn：最后回到理论机制，讨论贡献、边界、限制和管理含义。

- research_job_cn：挑出结果中最强的模式，说明它支持哪种机制，并指出不能支持哪种机制。

- required_evidence_cn：有至少一个机制推断可由调节模式支撑；有限制声明。

- transition_to_next_cn：讨论中强调“社交影响不是普遍工具”，使贡献避免被看成一次性结果。

### most_transferable_moves_cn

1. 用多个文献流反复制造并收窄缺口

2. 在假设前用“信号优先级”“边际价值”等理论语言解释为什么调节方向可能是这样

3. 用调查或外部数据独立测量调节变量，与实验数据分离

4. 按“主效应—单属性调节—组合调节—聚合指数”的顺序展示证据

5. 用一组稳健性检验分别对应一种替代解释

### resource_intensive_or_nonstandard_parts_cn

1. 与大型真实平台合作并获得超过70万用户的随机分组，需要极高的平台访问权限和信任

2. 平台采用“仅链接分享”的独特传播机制，为干净识别社交影响创造了条件，这类平台背景难以复制

3. 实验期外另收集3,539个病例数据训练信息性指数，需要平台持续提供数据

4. MTurk调查虽相对便宜，但美国受访者与中国捐赠者之间的文化差异可能造成测量偏差

### what_not_to_copy_superficially_cn

1. 不能只写“社交影响是信息性的”而不直接测量信息处理过程；本文也是推断性的

2. 不能把MTurk调查得到的属性信息价值直接套到不同国家或不同平台，而不做验证

3. 不能把处理效应随信息价值下降就解释为“资源更平等”，需要额外证据，如熵值或福利指标

4. 不能在没有随机分配或固定效应控制的情况下复制子样本比较，否则容易把属性选择效应误当因果调节

- single_best_description_of_the_routine_cn：先用一个现场随机实验建立自变量主效应，再用独立调查测出一个调节变量，然后通过“子样本拆分—组合—聚合指数”的递进展示，把主效应证明为一个有边界条件、可一般化的机制命题。

## 分析边界

本文基于提供的PDF文本进行分析；图1的具体快照、表2中的某些符号和表3中部分字符在转换中可能有残缺；Online Appendix A/B/C内容未随正文提供，文中对附录的引用无法具体核对；全文没有给出标准页码，因此locator使用章节、段落和表格编号定位。
