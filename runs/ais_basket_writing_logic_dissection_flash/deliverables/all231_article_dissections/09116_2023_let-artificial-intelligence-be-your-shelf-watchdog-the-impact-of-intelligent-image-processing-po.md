# Let Artificial Intelligence Be Your Shelf Watchdog: The Impact of Intelligent Image Processing-Powered Shelf Monitoring on Product Sales

- 作者：Yipu Deng; Jinyang Zheng; Liqiang Huang; Karthik Kannan
- 年份 / 期刊：2023 / MIS Quarterly
- DOI：10.25300/misq/2022/16813
- 源文件：09116_2023_let-artificial-intelligence-be-your-shelf-watchdog-the-impact-of-intelligent-image-processing-po.md
- 论文主类型：field_intervention_or_platform_experiment
- 主导写作弧线：phenomenon_mechanism_intervention_field_test
- 置信度：0.85

## 文章级论证概况

- 核心问题：在快速消费品零售场景中，由智能图像处理（IIP）驱动的货架监测系统是否、通过何种机制、以及在何种条件下能提升厂商产品销量，并且其效果能否在停止AI监测后持续？

- 制品与设计：IIP驱动的移动端货架监测系统：由厂商为业务代表配备手机应用，业务代表到店拍摄货架照片，系统通过计算机视觉识别焦点产品的SKU、陈列面数与货架位置，生成合规率报告，辅助业务代表进行货架合规监测；控制组仍采用传统人工监测。关键设计包括AI辅助而非替代、现场拍照加云端识别、终止组设计，以及仅拍照无AI报告的安慰剂对照。

- 客观结果：准实验约15%月销量提升；随机田野实验中继续监测组相比从未监测组销量显著更高，终止监测后销量约下降20%但仍高于从未监测组，表明部分持续效应；异质性分析显示效果主要集中于高合同异质性独立门店；零售商面对和位置合规率显著上升；仅拍照无效，AI报告带来0.243***销量提升；成本收益比约175.48。

- 核心贡献：作者声称首次以现场证据展示AI辅助型（而非替代型）监测在零售货架管理中的经济价值，发现“AI欣赏”、AI监测的行为持续性/人类学习、AI在处理异质合同实例时的可扩展性，并将货架管理研究扩展到制造商视角。

- 整篇论证链：作者以FMCG厂商在碎片化新兴市场中用传统人工监测难以扩展为现实问题，引入由AI图像识别辅助业务代表检查货架合规的IIP监测系统。先用厂商历史数据做PSM+DID准实验，获得销量提升的初步证据；再用随机田野实验从因果上确认启动效果，并通过“启动后终止”处理组检验效果持续性；随后从四个层面打开机制：按门店合同异质性检验AI可扩展性、用货架照片检验零售商合规率变化、用仅拍照无AI报告的额外实验排除拍照本身的安慰剂效应、以访谈补充定量因果链；最后用成本收益分析说明长期可行性，从而把局部销售效应上升为AI辅助监测的设计知识、机制主张和适用边界。

## 类型与写作弧线判定

- 论文主类型判定：论文的核心因果证据来自与真实FMCG厂商合作、在六城市数千家零售门店中实施的随机田野实验，包含监测启动与终止的处理臂；Stage 1的准实验和Stage 3的机制分析均围绕同一真实组织中的数字监测干预展开，而非构建新的计算制品或纯形式模型。

- 主导写作弧线判定：文章从新兴市场货架监测难扩展的现象出发，提出AI辅助监测的规模化、合规与学习机制，然后以准实验和田野实验对数字干预进行因果检验，再通过异质性、合规率、安慰剂和访谈逐层检验机制，最后返回经济价值与管理含义。

## 研究开展程序

- study_or_phase_count：7

- 研究阶段总序列：阶段顺序为：先用准实验建立效果存在的初步证据；再用随机田野实验确立因果并检验终止后的持续性；随后用四阶段机制分析解释效果来源（异质性、合规率、仅拍照安慰剂、访谈）；最后用成本收益分析判断长期经济可行性。每一阶段都解决上一阶段遗留的识别或机制问题。

### studies_or_phases

#### 1. Stage 1：准实验——IIP监测启动的增量效应

- order：1

- name_cn：Stage 1：准实验——IIP监测启动的增量效应

- question_cn：使用厂商已部署的IIP监测数据，IIP监测是否提高焦点产品销量？

- inputs_and_setting_cn：2017年1月至2019年8月42,097家门店月度销售与门店特征；2019年4月2,217家处理门店；货架照片级数据。

- designed_or_compared_object_cn：未由作者随机分配；比较已实施IIP监测的门店与继续人工监测的门店。

- baseline_control_or_counterfactual_cn：PSM配对后的未处理门店；相对时间模型中的治疗前时期；平行趋势。

##### objective_metrics

1. Log(Sales)

2. Monitoring系数

3. 相对时间系数

- analysis_method_cn：PSM最近邻1:1匹配+双向固定效应DID+相对时间模型。

- main_result_cn：Monitoring系数0.141***，约15%月销量提升；治疗后明显，治疗前无显著差异。

- argumentative_role_cn：提供初步增量效应证据，并验证可用的准实验识别。

- remaining_uncertainty_cn：非随机分配可能受未观测时变混杂影响。

- link_to_next_phase_cn：由于准实验不能保证因果识别，进入随机田野实验。

##### evidence_pointers

1. Stage 1 section

2. Table 4

3. Table 5

4. Figure 1

5. Appendix A

#### 2. Stage 2：随机田野实验——因果效应与终止后的持续性

- order：2

- name_cn：Stage 2：随机田野实验——因果效应与终止后的持续性

- question_cn：随机条件下，IIP监测启动是否提高销量，终止后是否仍有效果？

- inputs_and_setting_cn：3,808家门店，2019年5月至8月月销售；Group0=1,230，Group1=2,518，Group2=60；随机分配。

- designed_or_compared_object_cn：启动并持续IIP监测；启动后一个月终止IIP监测；对照从未启动。

- baseline_control_or_counterfactual_cn：Group0纯人工监测；Group1持续监测；Group2终止监测；随机化检验与组间t检验。

##### objective_metrics

1. Log(Sales)

2. Monitoring系数

3. RemoveMonitoring系数

4. 组间均值差

- analysis_method_cn：随机化检查，三组均值t检验，带门店/月份固定效应的回归（Equation 3和4）。

- main_result_cn：Group1销量显著高于Group0和Group2；RemoveMonitoring=-0.229***；终止后仍高于Group0（0.084**），说明部分持续效应。

- argumentative_role_cn：确立因果效应并检验行为的持续性/学习。

- remaining_uncertainty_cn：60家终止组样本较小；未直接观测人工学习行为。

- link_to_next_phase_cn：由效果存在转入为何存在、何时更强的机制分析。

##### evidence_pointers

1. Stage 2 section

2. Table 6

3. Table 7

4. Table 8

5. Table 9

6. Table 10

7. Table 11

8. Figure 2

#### 3. Stage 3机制分析之一：门店类型与合同异质性

- order：3

- name_cn：Stage 3机制分析之一：门店类型与合同异质性

- question_cn：AI的增量价值是否来自处理异质合同的可扩展性，即高合同异质性门店效果更强？

- inputs_and_setting_cn：Group0+Group1共3,748家门店，2017年1月至2019年8月，按厂商标准分为低、中、高合同异质性门店。

- designed_or_compared_object_cn：在DID中加入Monitoring×Middle和Monitoring×High交互。

- baseline_control_or_counterfactual_cn：低异质性门店/链式门店；纯人工监测对照组。

##### objective_metrics

1. Monitoring

2. Monitoring×Middle

3. Monitoring×High

- analysis_method_cn：DID交互模型（Equation 5）。

- main_result_cn：低异质性门店系数不显著（0.103），中异质性加0.163*，高异质性加0.302***；效果随异质性增加。

- argumentative_role_cn：把平均效应归因于AI对异质实例的规模化处理能力。

- remaining_uncertainty_cn：门店类型只是合同异质性的代理，未直接测量每份合同差异。

- link_to_next_phase_cn：接着验证合规行为变化以补全因果链。

##### evidence_pointers

1. Stage 3 first subsection

2. Table 12

#### 4. Stage 3机制分析之二：零售商合规率变化

- order：4

- name_cn：Stage 3机制分析之二：零售商合规率变化

- question_cn：零售商合规率是否在IIP监测后改善，支持AI→监测→合规→销售链条？

- inputs_and_setting_cn：Group1 2,518家处理门店的AI货架照片与报告；厂商年度报告中人工监测下的总合规率0.75/0.84。

- designed_or_compared_object_cn：比较AI系统的面数合规率与位置合规率在治疗后月份、控制月份和治疗前总体水平之间的差异。

- baseline_control_or_counterfactual_cn：治疗前总体合规率；首个治疗月5月（照片反映初始状态）。

##### objective_metrics

1. facing compliance rate

2. position compliance rate

3. t检验

4. p-value

- analysis_method_cn：假设检验：每月平均合规率是否等于治疗前总体值。

- main_result_cn：5月无显著差异；6月起两种合规率显著提升（facing最高0.042，position最高0.061）。

- argumentative_role_cn：补全从监测到销售之间的行为机制证据。

- remaining_uncertainty_cn：合规率来自AI报告本身，需排除拍照/报告效应的混淆。

- link_to_next_phase_cn：接着排除“仅拍照”效应以证明AI部分是关键。

##### evidence_pointers

1. Change in Retailers’ Compliance subsection

2. Table 13

3. Figure B1

#### 5. Stage 3机制分析之三：仅拍照无AI报告的安慰剂实验

- order：5

- name_cn：Stage 3机制分析之三：仅拍照无AI报告的安慰剂实验

- question_cn：仅拍摄货架照片而不使用AI报告是否足以提升销量？

- inputs_and_setting_cn：2021年5月起888家门店的额外田野实验；Group0=772，Group1=60有照片+AI报告，Group2=56有照片无AI报告。

- designed_or_compared_object_cn：两个处理组都拍照，是否收到AI报告不同。

- baseline_control_or_counterfactual_cn：Group0人工监测；Group2仅拍照无AI报告。

##### objective_metrics

1. Photo系数

2. AI系数

- analysis_method_cn：带门店和月份固定效应的回归（Equation 6）。

- main_result_cn：Photo系数0.004不显著；AI系数0.243***；效果来自AI而非拍照。

- argumentative_role_cn：排除拍照记录的安慰剂/注意力效应，支持AI处理是核心。

- remaining_uncertainty_cn：该实验样本小、时间短，且2021年情境可能不同于2019年。

- link_to_next_phase_cn：访谈补充解释为什么AI能改善监测精度与零售商反应。

##### evidence_pointers

1. Effect of Taking Photos subsection

2. Table 14

3. Table 15

#### 6. Stage 3机制分析之四：业务代表与零售商访谈

- order：6

- name_cn：Stage 3机制分析之四：业务代表与零售商访谈

- question_cn：定性证据是否支持AI提高业务代表监测能力、零售商合规与异质性可扩展性的机制？

- inputs_and_setting_cn：28名业务代表电话访谈；112名零售商实地访谈；标准化问题与开放式回答。

- designed_or_compared_object_cn：半结构化访谈，围绕AI对监测难度、与厂商/门店关系、销量、异质性门店、反馈准确度等展开。

- baseline_control_or_counterfactual_cn：无严格对照组；依赖受访者自评与趋势描述。

##### objective_metrics

1. 回答比例：80%、90%、78%、85%等

- analysis_method_cn：描述性统计与主题归纳。

- main_result_cn：多数业务代表认为AI让检查更有效、改善与厂商和门店关系、更易识别不合规、对异质门店更有帮助；多数零售商感知反馈更准确、但拜访时间未增加、不觉得过度监测。

- argumentative_role_cn：为定量机制提供过程证据与参与者解释。

- remaining_uncertainty_cn：访谈样本非随机完整性受限，自报数据可能有偏差。

- link_to_next_phase_cn：结合定量与定性形成完整因果链，进入成本收益分析。

##### evidence_pointers

1. Interviews with Delegates subsection

2. Interviews with Retailers subsection

3. Table 16

4. Table 17

#### 7. 成本收益分析

- order：7

- name_cn：成本收益分析

- question_cn：从盈利角度，IIP监测系统的长期采纳是否值得？

- inputs_and_setting_cn：年度系统开发维护成本约155,000美元；2020年中国市场焦点产品总销售额约1.6亿美元；效应量17%。

- designed_or_compared_object_cn：成本-收益核算，用Table 11效应量外推年度收益。

- baseline_control_or_counterfactual_cn：无IIP监测的反事实情景。

##### objective_metrics

1. 年收益

2. 成本收益比

- analysis_method_cn：线性外推：17%×1.6亿=2,720万美元；比率≈175.48。

- main_result_cn：即使采用保守估计，成本收益比约175.48，项目盈利。

- argumentative_role_cn：回应长期可行性，把因果估计转成管理决策价值。

- remaining_uncertainty_cn：外推到其他市场/长期依赖不可检验假设；未计入劳动力成本调整。

- link_to_next_phase_cn：结论总结并给出边界与未来研究。

##### evidence_pointers

1. Cost-Benefit Analysis subsection

2. Table 11

## 各部分修辞架构

### abstract_moves

1. CONTEXT: 与领先FMCG厂商合作，用准实验和田野实验考察IIP货架监测对销售的影响。

2. RESULT: AI辅助显著且一致地提高产品销量。

3. MECHANISM: 零售商更可能合规；终止后效果部分持续表明学习；价值集中于独立零售商。

4. ROBUSTNESS_OR_BOUNDARY_TEST: 边际成本低，长期适用。

5. CONTRIBUTION: 对AI经济价值与AI辅助运营模式有贡献。

### introduction_moves

1. CONTEXT: 货架管理对FMCG制造商至关重要，陈列直接影响销售。

2. PHENOMENON: 新兴市场独立零售商多、货架条件高度异质，人工监测难扩展。

3. RQ_OR_OBJECTIVE: 提出效果、机制、长期成功三个问题。

4. STUDY_OVERVIEW: 预告三阶段：准实验、田野实验、机制分析。

5. RESULT: AI欣赏、异质性、持续性、因果链等主要发现。

6. CONTRIBUTION: 贡献到AI商业价值、算法态度、行为持续性、货架管理文献。

7. BOUNDARY_CONDITION: 管理启示以高异质性合同和分享经济为例。

### theory_and_knowledge_moves

1. PRIOR_KNOWLEDGE: IT促进供应链/需求/促销协作，但视觉营销/货架管理的IT研究稀缺。

2. GAP: AI辅助型模型相较AI替代型模型少受关注。

3. PRIOR_KNOWLEDGE: 人对算法既可能欣赏也可能厌恶。

4. HYPOTHESIS_OR_PROPOSITION: 若业务代表拒绝AI则销量不变，若接受则销量提升。

5. PRIOR_KNOWLEDGE: 监测普遍提高流程合规，但AI在自动化监测中的作用不清。

6. THEORY_PROPOSITION: 行为干预可能持续或消退；需检验IIP监测终止后的持久性。

7. GAP: 货架管理优化多从零售商视角，制造商如何管理零售商货架缺乏研究。

### artifact_design_moves

1. DESIGN_FEATURE: 移动应用+云端图像识别，自动检测产品SKU、面数与货架位置。

2. DESIGN_FEATURE: AI报告提供facing/position compliance rate。

3. REQUIREMENT: 提取面数与位置是因为二者是合同主要条款且被文献证明影响销售。

4. DESIGN_FEATURE: AI辅助业务代表而非完全替代人工；仅业务代表可拍照，无需CCTV。

5. DESIGN_FEATURE: 终止组设计使监测效果与行为持续性可分离。

### evaluation_moves

1. METHOD_JUSTIFICATION: 因处理组非随机，用PSM+双重差分控制选择偏差。

2. BENCHMARK_OR_CONTRAST: 以相对时间模型检验平行趋势。

3. METHOD_JUSTIFICATION: 田野实验随机分配三组以精确因果识别。

4. BENCHMARK_OR_CONTRAST: Group2 vs Group1估计终止效应；Group2 vs Group0检验持久效应。

5. ROBUSTNESS_OR_BOUNDARY_TEST: 随机化检查、CEM附录、即时行为附录、过度监测附录。

6. RESULT: 异质性交互分析显示高合同异质性门店效果最强。

7. RESULT: 合规率在治疗后月份显著上升。

8. RESULT: 额外田野实验中Photo系数不显著、AI系数显著。

9. RESULT: 访谈比例为机制提供定性证据。

### discussion_and_contribution_moves

1. MECHANISM: 访谈补充AI→准确反馈→零售商合规→销量因果链。

2. RESULT: 成本收益分析给出约175.48的收益成本比。

3. CONTRIBUTION: AI辅助模型、算法欣赏、行为持续性、制造商面货架管理。

4. BOUNDARY_CONDITION: 效果集中于高合同异质性门店/新兴市场，外推需谨慎。

5. LIMITATION_AND_FUTURE: 未观测劳动力成本调整、缺少业务代表层面面板、样本量与外部效度限制。

## 理论/知识到设计的翻译

### 知识/理论基础

1. 货架管理/视觉营销文献：面数与位置影响销售

2. AI商业价值文献：AI适合处理图像/视频等大量感知任务，可增强人类任务

3. 人类对算法态度文献：算法欣赏/算法厌恶

4. 监测文献：监测提升流程合规；理性欺骗者模型

5. 行为持续性文献：干预停止后行为可能持续或消退

6. AI可扩展性观点：AI处理异质实例的边际成本低

- 理论—设计耦合：partial

- 耦合判定理由：厂家和作者共同开发/部署的移动IIP监测系统主要由图像识别技术约束和业务需求驱动；理论主要用来提出研究问题、选择核心变量（面数、位置合规率）、设计机制检验（合同异质性、合规率、拍照安慰剂、持久性）以及解释结果，而非从理论逐条推导出系统功能。因此属于部分耦合。

- 理论到设计翻译链：货架陈列决定销售→合同以面数和位置为核心条款→IIP系统提取面数与位置并生成合规报告→业务代表根据AI报告进行监测和反馈→零售商因监测更有效而提高合规率→销量提升；AI的预训练模型使异质合同的边际处理成本低→在高异质性独立门店效果更强；监测的持久性理论→田野实验设置终止组→部分持续性/学习。

### mapping_table

#### 1. 1

- theory_or_knowledge_claim_cn：货架空间与位置显著影响品牌销量，且是合同核心（Frank & Massy 1970; Nierop et al. 2008）

- mechanism_cn：产品面数和位置合规程度改变消费者可见性/可获得性，从而影响销量

- design_requirement_cn：监测系统必须量化合同中的面数和位置

- artifact_choice_cn：IIP识别每个SKU的facing数量和货架高度位置，生成facing/position compliance rate

- evaluated_contrast_cn：AI监测 vs 人工监测下的销量；AI报告 vs 仅拍照

- objective_result_cn：监测系数0.141***/0.166***；销量提升约15%-17%；AI系数0.243***，Photo不显著

##### evidence_pointers

1. Table 1

2. Role of AI section

3. Table 5

4. Table 11

5. Table 15

#### 2. 2

- theory_or_knowledge_claim_cn：监测提高合规，因为理性欺骗者会在监测不足时不履行合同（Nagin et al. 2002; Staats et al. 2016）

- mechanism_cn：AI增强业务代表监测能力，违规更容易被发现并留下记录，零售商因此提高合规

- design_requirement_cn：监测需要覆盖大量异质门店并产生可证明的合规记录

- artifact_choice_cn：移动应用拍照+AI报告作为业务代表的辅助监测工具

- evaluated_contrast_cn：治疗前后零售商合规率 vs 治疗前总体0.75/0.84；终止后销量 vs 对照组

- objective_result_cn：6月起facing/position合规率显著上升；终止后销量下降但仍高于基线

##### evidence_pointers

1. Table 13

2. Table 10

3. Table 11

4. Figure B1

#### 3. 3

- theory_or_knowledge_claim_cn：AI相对于人类更适合重复性强且实例异质的任务，边际处理成本低（Iansiti & Lakhani 2020; McKendrick 2018）

- mechanism_cn：人工监测异质合同的时间成本线性增长，AI预训练模型处理新合同边际成本低

- design_requirement_cn：系统应能应对不同门店布局，不需要针对每个合同重新人工编码

- artifact_choice_cn：云端图像识别模型直接输出各门店的SKU/面数/位置，无需逐店人工比对

- evaluated_contrast_cn：低/中/高合同异质性门店的监测效果差异

- objective_result_cn：Monitoring×High=0.302***，效果随异质性增大；链式门店不显著

##### evidence_pointers

1. Table 12

2. Stage 3 first subsection

#### 4. 4

- theory_or_knowledge_claim_cn：行为干预停止后可能因习惯形成而持续，也可能因内在动机被挤出而消退（Allcott & Rogers 2014; Staats et al. 2016）

- mechanism_cn：零售商意识到厂商有可靠监测能力并形成合规惯例，或业务代表从AI报告中学习，终止后效果部分保留

- design_requirement_cn：评估长期价值必须观察终止后的行为，而非只比较启动前后

- artifact_choice_cn：田野实验加入Group2：启动IIP监测一个月后终止，转为人工监测

- evaluated_contrast_cn：Group2终止后 vs Group1持续监测；Group2 vs Group0从未启动

- objective_result_cn：RemoveMonitoring=-0.229***，但与Group0比较仍为正0.084**，部分持续

##### evidence_pointers

1. Table 6

2. Table 10

3. Table 11

## 评价逻辑

### evaluation_modes

1. 准实验（PSM+DID）

2. 随机田野实验（三组启动/终止/对照）

3. 额外随机田野实验（仅拍照 vs 拍照+AI报告）

4. 合规率假设检验

5. 半结构化访谈

6. 成本收益分析

7. 稳健性检验（相对时间模型、CEM、即时行为、过度监测）

- why_these_evaluations_cn：因为需要从“是否有效”到“为什么有效”再到“能否长期采用”逐层回答：先用观察性数据获得初步增量证据，再用随机化排除选择偏差确认因果；加入终止组识别持久性；随后用合规率、仅拍照对照和访谈分别检验机制中的合规环节、AI信息处理环节和参与者行为逻辑；最后用成本收益把效果转成可持续性判断。

- benchmark_and_contrast_chain_cn：文章以人工监测为统一基线。Stage1中PSM匹配门店作为控制组；Stage2中Group0为纯人工监测，Group1为持续IIP监测，Group2为启动后终止，三者互为对照，使启动效果、终止效果和持久效果可以分离；Stage3用低/中/高合同异质性门店比较效果梯度；2021额外实验中Group2仅拍照无AI报告，与Group1拍照+AI报告对照，分离“AI处理”与“拍照行为”；访谈结果再为这些对照提供过程解释。

### claim_evidence_ledger

#### 1. 启动IIP监测提升月销量约15%（准实验）

- claim_cn：启动IIP监测提升月销量约15%（准实验）

- evidence_cn：PSM+DID Monitoring系数0.141***，平行趋势满足

- status_cn：有直接统计证据

#### 2. IIP监测对销量有因果效应

- claim_cn：IIP监测对销量有因果效应

- evidence_cn：随机田野实验，随机化检查通过，Group1显著高于Group0

- status_cn：有直接因果证据

#### 3. 终止监测后销量仍高于从未监测，效果部分持续

- claim_cn：终止监测后销量仍高于从未监测，效果部分持续

- evidence_cn：RemoveMonitoring在式(4)中0.084**，虽低于启动效应0.166***

- status_cn：有直接统计证据，但终止店样本仅60家

#### 4. AI比人工更适合高异质性合同

- claim_cn：AI比人工更适合高异质性合同

- evidence_cn：Monitoring×High=0.302***，效果随合同异质性增加

- status_cn：间接证据，用门店类型代理异质性

#### 5. 效果来自AI处理而非拍照

- claim_cn：效果来自AI处理而非拍照

- evidence_cn：Photo系数0.004不显著，AI系数0.243***

- status_cn：直接实验证据，但额外实验样本小

#### 6. 零售商合规率提高构成机制

- claim_cn：零售商合规率提高构成机制

- evidence_cn：治疗后月份facing/position合规率显著上升

- status_cn：直接证据，但合规率来自AI输出

#### 7. 业务代表和零售商行为机制成立

- claim_cn：业务代表和零售商行为机制成立

- evidence_cn：访谈多数受访者报告反馈更准、更易识别不合规、不觉得速度变化

- status_cn：定性自报证据，支持性而非决定性

- internal_validity_strategy_cn：随机分配与随机化检查；PSM与平行趋势检验；门店/月份固定效应控制未观测异质性；通过终止组清理持续性效应；通过仅拍照对照排除拍照的安慰剂渠道；使用货架照片合规率直接测量行为变化；附录用CEM、即时行为分析和过度监测检验补充稳健性。

- external_validity_strategy_cn：覆盖中国六个城市、数千家不同规模与类型门店；同时纳入独立店、区域连锁和全国连锁；将效果异质性与新兴市场零售结构联系；通过成本收益分析讨论向其他新兴市场与平台型异质实例管理场景的推广条件。

- what_is_not_actually_tested_cn：没有直接测量每个合同的异质性程度，而是用门店类型代理；没有业务代表层面面板来直接观察学习发生；终止组样本量小；成本收益外推依赖不可检验假设；未实际观测劳动力成本调整；仅拍照实验在2021年、且处理组较小，可能弱于主实验。

## 贡献闭环

- technical_claim_cn：在真实FMCG零售网络中，IIP监测使焦点产品月销量提高约14%-17%；终止后销量下降但残余高于人工监测基线。

- artifact_claim_cn：销量提升由AI生成的合规报告驱动，而非拍摄照片本身；报告使业务代表反馈更准确。

- mechanism_claim_cn：AI增强了业务代表的监测有效性与准确性，提高零售商对陈列合同的合规率；在合同异质性高时AI可扩展性带来更大效果；终止后部分效果持续表明零售商与业务代表发生学习。

- boundary_claim_cn：效果主要出现在独立门店/高合同异质性环境中；对链式门店/低异质性合同不显著；因而最适合新兴市场或分布碎片化的门店网络；长期价值依赖成本低于持续收益。

- reusable_design_knowledge_cn：可用AI辅助人类完成大量异质性实例的合规监测；监测系统应输出可核对的合规指标（面数、位置）；部署时应考虑干预终止后的残留效应；仅信息采集（拍照）不足以改变行为，AI生成的反馈才重要；成本收益需结合边际部署成本。

- theoretical_contribution_cn：将AI经济价值从AI替代扩展到AI辅助；在零售现场检验“AI欣赏”；将监测文献延伸到由AI辅助的合同合规；用终止组补充行为持续性理论；从制造商视角重访货架管理。

- how_discussion_closes_intro_gap_cn：结论部分逐条回答引言三问：确证销量提升、给出四层机制证据、通过终止组与成本收益说明长期可持续性；同时把异质性结果升华为AI可扩展性的边界条件。

- overclaim_or_unsupported_leaps_cn：把门店类型直接等同于合同异质性、把销量残余效果直接解释为人类学习、用2020年销售额和单市场短期系数外推长期收益成本比、认为效果将推广到Airbnb/Uber等异质实例管理，均属于较强外推；终止组和仅拍照实验样本量小，定量机制的因果完整性主要靠拼接而非单一实验。

## 句级写作动作图谱

### 1. Abstract S1

- order：1

- section：Abstract

- locator：Abstract S1

- move_code：CONTEXT

- paraphrase_cn：作者与一家领先FMCG厂商合作，用准实验和田野实验研究IIP货架监测对厂商货架管理的帮助。

- rhetorical_function_cn：开篇点明合作情境、对象和两种核心方法。

- depends_on_cn：无需前文。

- sets_up_cn：为摘要后续结果与贡献提供研究场景。

- evidence_pointer：Abstract

### 2. Abstract S2

- order：2

- section：Abstract

- locator：Abstract S2

- move_code：RESULT

- paraphrase_cn：作者发现AI辅助一致且显著地提高产品销量。

- rhetorical_function_cn：给出全文首要结论。

- depends_on_cn：承接合作情境。

- sets_up_cn：引出机制、边界和成本收益。

- evidence_pointer：Abstract

### 3. Abstract S3-S4

- order：3

- section：Abstract

- locator：Abstract S3-S4

- move_code：MECHANISM

- paraphrase_cn：作者将效果归因于零售商更高合规率、终止后部分持续说明人类学习，以及独立零售商而非连锁零售商。

- rhetorical_function_cn：列出三个核心机制发现，使结果具有解释力。

- depends_on_cn：基于验证后的主效应。

- sets_up_cn：为正文中机制分析作预告。

- evidence_pointer：Abstract

### 4. Abstract S5-S6

- order：4

- section：Abstract

- locator：Abstract S5-S6

- move_code：ROBUSTNESS_OR_BOUNDARY_TEST

- paraphrase_cn：作者指出实施IIP监测的边际成本低，表明长期适用和增量价值。

- rhetorical_function_cn：补充经济可行性以支持长期判断。

- depends_on_cn：前面机制与效应估计。

- sets_up_cn：引入成本收益分析。

- evidence_pointer：Abstract

### 5. Abstract S7

- order：5

- section：Abstract

- locator：Abstract S7

- move_code：CONTRIBUTION

- paraphrase_cn：作者声明对多支文献和管理实践有贡献。

- rhetorical_function_cn：定位文章理论贡献。

- depends_on_cn：全部发现。

- sets_up_cn：引导读者关注贡献主张。

- evidence_pointer：Abstract

### 6. Introduction P1 S1

- order：6

- section：Introduction

- locator：Introduction P1 S1

- move_code：CONTEXT

- paraphrase_cn：货架管理对FMCG制造商至关重要，因为陈列方式直接影响顾客选择和销量。

- rhetorical_function_cn：建立问题域的重要性。

- depends_on_cn：无。

- sets_up_cn：为后续合同、监测和AI方案做铺垫。

- evidence_pointer：Introduction P1

### 7. Introduction P1 S2-S3

- order：7

- section：Introduction

- locator：Introduction P1 S2-S3

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：标准零售合同规定货架位置、空间和展示数量，甚至眼平高度等约束；厂商派代表检查合规。

- rhetorical_function_cn：说明货架管理的制度安排。

- depends_on_cn：货架重要性的背景。

- sets_up_cn：为人工监测的局限作基础。

- evidence_pointer：Introduction P1

### 8. Introduction P1 S4-S5

- order：8

- section：Introduction

- locator：Introduction P1 S4-S5

- move_code：PHENOMENON

- paraphrase_cn：在进入全球市场时，厂商面对大量独立零售商和高度货架异质性，传统人工监测缺少扩展性。

- rhetorical_function_cn：引入新兴市场碎片化现象。

- depends_on_cn：前一合同安排。

- sets_up_cn：为AI方案制造张力。

- evidence_pointer：Introduction P1

### 9. Introduction P1 S5

- order：9

- section：Introduction

- locator：Introduction P1 S5

- move_code：LIMITATION

- paraphrase_cn：仅靠人工判断的常规货架管理正在过时。

- rhetorical_function_cn：明确指出旧方式不足以应对新现实。

- depends_on_cn：异质性监测挑战。

- sets_up_cn：引出AI/IIP方案。

- evidence_pointer：Introduction P1

### 10. Introduction P1 S6

- order：10

- section：Introduction

- locator：Introduction P1 S6

- move_code：DESIGN_FEATURE

- paraphrase_cn：自然解决方案是使用AI/ML方法如IIP来突破限制。

- rhetorical_function_cn：提出解决方案方向。

- depends_on_cn：人工监测局限。

- sets_up_cn：引出三研究问题。

- evidence_pointer：Introduction P1

### 11. Introduction P1 S7

- order：11

- section：Introduction

- locator：Introduction P1 S7

- move_code：RQ_OR_OBJECTIVE

- paraphrase_cn：作者提出三个问题：IIP监测是否改善货架管理与销量、机制为何、长期效果如何。

- rhetorical_function_cn：正式给出研究问题。

- depends_on_cn：方案方向。

- sets_up_cn：预告三阶段研究。

- evidence_pointer：Introduction P1

### 12. Introduction P2 S1

- order：12

- section：Introduction

- locator：Introduction P2 S1

- move_code：STUDY_OVERVIEW

- paraphrase_cn：作者说明与厂商合作并开展系统性分析实验的三个阶段。

- rhetorical_function_cn：给出全文路线图。

- depends_on_cn：三研究问题。

- sets_up_cn：为后续章节提供导航。

- evidence_pointer：Introduction P2

### 13. Introduction P2 S2

- order：13

- section：Introduction

- locator：Introduction P2 S2

- move_code：STUDY_OVERVIEW

- paraphrase_cn：Stage 1用准实验方案分析观测数据，估计启动IIP监测的增量影响。

- rhetorical_function_cn：介绍第一阶段任务。

- depends_on_cn：总路线图。

- sets_up_cn：说明第一阶段证据形式。

- evidence_pointer：Introduction P2

### 14. Introduction P2 S3

- order：14

- section：Introduction

- locator：Introduction P2 S3

- move_code：STUDY_OVERVIEW

- paraphrase_cn：Stage 2用随机田野实验更精确识别因果效应，并设置终止AI辅助的处理组以研究持续性。

- rhetorical_function_cn：介绍第二阶段的识别升级与持续性设计。

- depends_on_cn：准实验局限。

- sets_up_cn：引出持久性和学习分析。

- evidence_pointer：Introduction P2

### 15. Introduction P2 S4

- order：15

- section：Introduction

- locator：Introduction P2 S4

- move_code：STUDY_OVERVIEW

- paraphrase_cn：Stage 3分四部分拆解机制：异质性、合规率、拍照效应和访谈。

- rhetorical_function_cn：介绍机制分析结构。

- depends_on_cn：主效应的存在。

- sets_up_cn：为Stage 3节铺垫。

- evidence_pointer：Introduction P2

### 16. Introduction P3 S1

- order：16

- section：Introduction

- locator：Introduction P3 S1

- move_code：RESULT

- paraphrase_cn：所有分析一致显示“AI欣赏”，实施IIP监测的门店销量提升。

- rhetorical_function_cn：给出首要经验结果。

- depends_on_cn：三阶段分析。

- sets_up_cn：引向异质性结果。

- evidence_pointer：Introduction P3

### 17. Introduction P3 S2

- order：17

- section：Introduction

- locator：Introduction P3 S2

- move_code：RESULT

- paraphrase_cn：销量提升主要来自独立零售店，对合同更同质的连锁店不显著。

- rhetorical_function_cn：报告关键的异质性发现。

- depends_on_cn：平均效果。

- sets_up_cn：支撑AI可扩展性论点。

- evidence_pointer：Introduction P3

### 18. Introduction P3 S3

- order：18

- section：Introduction

- locator：Introduction P3 S3

- move_code：MECHANISM

- paraphrase_cn：该发现支持AI的可扩展性，能处理通常对人类更困难的异质实例重复任务。

- rhetorical_function_cn：把异质性结果转成机制解释。

- depends_on_cn：异质性结果。

- sets_up_cn：为Stage 3异质性检验做预告。

- evidence_pointer：Introduction P3

### 19. Introduction P3 S4

- order：19

- section：Introduction

- locator：Introduction P3 S4

- move_code：RESULT

- paraphrase_cn：程序结束后销售增量下降，但处理店仍高于从未采用的人工监测店，表明部分持续与学习。

- rhetorical_function_cn：报告行为的持续性发现。

- depends_on_cn：终止组设计。

- sets_up_cn：引出学习机制。

- evidence_pointer：Introduction P3

### 20. Introduction P4 S1

- order：20

- section：Introduction

- locator：Introduction P4 S1

- move_code：MECHANISM

- paraphrase_cn：作者给出AI帮助更有效监测、监测带来更好合规、合规改善销量的因果链，并说明仅拍照的安慰剂不会提升销量。

- rhetorical_function_cn：压缩式呈现机制链条。

- depends_on_cn：量化与质性证据。

- sets_up_cn：为Stage 3四部分机制铺路。

- evidence_pointer：Introduction P4

### 21. Introduction P4 S2-S5

- order：21

- section：Introduction

- locator：Introduction P4 S2-S5

- move_code：CONTRIBUTION

- paraphrase_cn：作者列出对AI辅助模型、算法态度、行为持续性、AI适用业务情境和货架管理制造商视角的贡献。

- rhetorical_function_cn：定位文献贡献。

- depends_on_cn：全部发现。

- sets_up_cn：为Discussion中的贡献复述做准备。

- evidence_pointer：Introduction P4

### 22. Introduction P5

- order：22

- section：Introduction

- locator：Introduction P5

- move_code：BOUNDARY_CONDITION

- paraphrase_cn：管理启示强调高合同异质性场景，并推广到Airbnb/Uber等管理大量异质实例的分享经济。

- rhetorical_function_cn：扩展结论的适用边界。

- depends_on_cn：前沿发现。

- sets_up_cn：塑造一般化设计知识。

- evidence_pointer：Introduction P5

### 23. Literature Review section around AI and Retailer Management

- order：23

- section：Literature Review

- locator：Literature Review section around AI and Retailer Management

- move_code：GAP

- paraphrase_cn：作者指出AI替代任务的研究较多，AI辅助任务的实证影响较少。

- rhetorical_function_cn：构建AI辅助研究缺口。

- depends_on_cn：先前AI文献。

- sets_up_cn：为本文AI辅助模型贡献定位。

- evidence_pointer：Literature Review, AI and Retailer Management

### 24. Literature Review, Retailer Management and AI paragraph

- order：24

- section：Literature Review

- locator：Literature Review, Retailer Management and AI paragraph

- move_code：LIMITATION

- paraphrase_cn：已有IT帮助供应链、需求计划和促销协作，但视觉营销/货架管理中的IT作用研究稀少。

- rhetorical_function_cn：指出零售商管理文献中的具体盲区。

- depends_on_cn：McKinsey分类。

- sets_up_cn：说明AI可改变该领域。

- evidence_pointer：Literature Review, Retailer Management and AI

### 25. Literature Review, Retailer Management and AI near end

- order：25

- section：Literature Review

- locator：Literature Review, Retailer Management and AI near end

- move_code：DESIGN_FEATURE

- paraphrase_cn：作者跟随Luo等人的工作，与厂商共同开发并实验AI-人类监测组合体，以检查零售商货架合规。

- rhetorical_function_cn：明确AI系统的定位是辅助人，而非替代人。

- depends_on_cn：AI适合图像处理的观点。

- sets_up_cn：为Role of AI中的系统描述提供依据。

- evidence_pointer：Literature Review, Retailer Management and AI

### 26. Literature Review, Human Attitudes Toward AI first paragraph

- order：26

- section：Literature Review

- locator：Literature Review, Human Attitudes Toward AI first paragraph

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：文献记录了算法厌恶与算法欣赏两种相反态度。

- rhetorical_function_cn：建立关于人机态度的两难知识。

- depends_on_cn：行为决策文献。

- sets_up_cn：为业务代表是否使用AI的假设作基础。

- evidence_pointer：Literature Review, Human Attitudes Toward AI

### 27. Literature Review, Human Attitudes Toward AI last paragraph

- order：27

- section：Literature Review

- locator：Literature Review, Human Attitudes Toward AI last paragraph

- move_code：HYPOTHESIS_OR_PROPOSITION

- paraphrase_cn：如果业务代表拒绝AI，销量不会有变化；如果他们拥抱AI，销量可能大增。

- rhetorical_function_cn：把态度文献转化为可检验命题。

- depends_on_cn：算法欣赏/厌恶文献。

- sets_up_cn：解释为何田野实验可检验态度。

- evidence_pointer：Literature Review, Human Attitudes Toward AI

### 28. Literature Review, Monitoring section

- order：28

- section：Literature Review

- locator：Literature Review, Monitoring section

- move_code：GAP

- paraphrase_cn：监测文献大多显示监测提高合规，但AI在自动化监测中的作用仍不清楚。

- rhetorical_function_cn：在监测文献中构造AI角色缺口。

- depends_on_cn：监测实证文献。

- sets_up_cn：引出IIP监测的增量价值主张。

- evidence_pointer：Literature Review, Monitoring

### 29. Literature Review, Monitoring persistence paragraph

- order：29

- section：Literature Review

- locator：Literature Review, Monitoring persistence paragraph

- move_code：THEORY_PROPOSITION

- paraphrase_cn：行为干预停止后可能持续或消退，实际和理论都要求检验IIP监测的长期可持续性。

- rhetorical_function_cn：引入行为持续性理论作为研究设计依据。

- depends_on_cn：行为干预文献。

- sets_up_cn：为终止组设计和持久性结果提供框架。

- evidence_pointer：Literature Review, Monitoring

### 30. Literature Review, Shelf Management section near end

- order：30

- section：Literature Review

- locator：Literature Review, Shelf Management section near end

- move_code：GAP

- paraphrase_cn：货架管理优化多从零售商视角，制造商如何有效管理零售商货架仍待研究。

- rhetorical_function_cn：在货架管理文献中建立制造商视角缺口。

- depends_on_cn：零售商侧优化文献。

- sets_up_cn：为IIP监测系统提供应用领域。

- evidence_pointer：Literature Review, Shelf Management

### 31. Research Context Background P2

- order：31

- section：Research Context

- locator：Research Context Background P2

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：厂商与每家零售商签订货架空间租赁合同，明确规定展示数量、租用货架部分和违约处罚。

- rhetorical_function_cn：说明制度性基础。

- depends_on_cn：前文零售网络描述。

- sets_up_cn：使监测和合规成为具体问题。

- evidence_pointer：Research Context, Background

### 32. Research Context Background P3

- order：32

- section：Research Context

- locator：Research Context Background P3

- move_code：CONTEXT

- paraphrase_cn：业务代表每人负责约150家门店，并负责拜访、送货、下单和反馈等职责。

- rhetorical_function_cn：说明人工监测的时间约束。

- depends_on_cn：合同制度。

- sets_up_cn：为后续时间成本线性增长论点奠基。

- evidence_pointer：Research Context, Background

### 33. Research Context Background P4

- order：33

- section：Research Context

- locator：Research Context Background P4

- move_code：PHENOMENON

- paraphrase_cn：新兴市场零售结构碎片化，独立店货架条件异质性高，合同需逐店单独签订。

- rhetorical_function_cn：描述研究现场的现象特征。

- depends_on_cn：成熟市场与新兴市场对比。

- sets_up_cn：引出扩展性理论。

- evidence_pointer：Research Context, Background

### 34. Research Context Background P5

- order：34

- section：Research Context

- locator：Research Context Background P5

- move_code：MECHANISM

- paraphrase_cn：合同异质性使人工检查的时间成本随门店数线性增长，难以扩展。

- rhetorical_function_cn：从时间成本角度解释人工监测瓶颈。

- depends_on_cn：异质性现象。

- sets_up_cn：为AI可扩展性做反衬。

- evidence_pointer：Research Context, Background

### 35. Research Context Background P6

- order：35

- section：Research Context

- locator：Research Context Background P6

- move_code：THEORY_PROPOSITION

- paraphrase_cn：监测不足时，理性零售商可能因成本与效用差异而不合规，且违规易被忽视。

- rhetorical_function_cn：引入理性欺骗者行为模型。

- depends_on_cn：监测不足。

- sets_up_cn：为合规率机制提供了为什么监测有效。

- evidence_pointer：Research Context, Background

### 36. Research Context Background P7

- order：36

- section：Research Context

- locator：Research Context Background P7

- move_code：DESIGN_FEATURE

- paraphrase_cn：厂商采用基于移动应用的IIP监测：业务代表拍照上传云端，AI识别产品并输出合规信息。

- rhetorical_function_cn：刻画系统核心功能。

- depends_on_cn：AI方案方向。

- sets_up_cn：说明该系统的信息输入输出。

- evidence_pointer：Research Context, Background

### 37. Role of AI first paragraph

- order：37

- section：Role of AI

- locator：Role of AI first paragraph

- move_code：REQUIREMENT

- paraphrase_cn：因为面数和位置是合同两大方面并被文献证明影响销售，所以IIP系统提取这两个指标。

- rhetorical_function_cn：从领域知识推导出系统度量要求。

- depends_on_cn：货架管理文献。

- sets_up_cn：解释AI报告为何包含facing和position compliance rate。

- evidence_pointer：Role of AI section

### 38. Stage 1 Identification Strategy P1

- order：38

- section：Stage 1

- locator：Stage 1 Identification Strategy P1

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：由于处理店选择非随机，作者使用PSM构造拟随机样本并配合DID。

- rhetorical_function_cn：解释准实验识别策略。

- depends_on_cn：Stage 1数据。

- sets_up_cn：为Stage 1回归结果提供合法性。

- evidence_pointer：Stage 1, Identification Strategy

### 39. Stage 1 Difference-in-Differences first paragraph

- order：39

- section：Stage 1

- locator：Stage 1 Difference-in-Differences first paragraph

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：DID比较处理组与对照组随时间变化，并纳入门店和时间固定效应。

- rhetorical_function_cn：给出主回归模型。

- depends_on_cn：PSM匹配。

- sets_up_cn：为相对时间模型作对照。

- evidence_pointer：Stage 1, Difference-in-Differences

### 40. Stage 1 Relative Time Model first paragraph

- order：40

- section：Stage 1

- locator：Stage 1 Relative Time Model first paragraph

- move_code：BENCHMARK_OR_CONTRAST

- paraphrase_cn：作者用相对时间模型加入治疗前后虚拟变量，检验平行趋势和动态效应。

- rhetorical_function_cn：建立DID有效性的前提证据。

- depends_on_cn：DID模型。

- sets_up_cn：支持用DID系数解释因果。

- evidence_pointer：Stage 1, Relative Time Model

### 41. Stage 1 Results, Relative Time Model paragraph

- order：41

- section：Stage 1

- locator：Stage 1 Results, Relative Time Model paragraph

- move_code：ROBUSTNESS_OR_BOUNDARY_TEST

- paraphrase_cn：治疗前各组虚拟变量都不显著，说明匹配后平行趋势成立。

- rhetorical_function_cn：为主识别假设提供证据。

- depends_on_cn：相对时间模型回归。

- sets_up_cn：使后续主效应可以被因果解读。

- evidence_pointer：Table 4

### 42. Stage 1 Results, Effect of Launching paragraph

- order：42

- section：Stage 1

- locator：Stage 1 Results, Effect of Launching paragraph

- move_code：RESULT

- paraphrase_cn：IIP监测使处理店月销量约增加15%，对应系数0.141***。

- rhetorical_function_cn：报告Stage 1核心结果。

- depends_on_cn：PSM+DID。

- sets_up_cn：为Stage 2因果检验做铺垫。

- evidence_pointer：Table 5

### 43. Stage 2 first paragraph

- order：43

- section：Stage 2

- locator：Stage 2 first paragraph

- move_code：LIMITATION

- paraphrase_cn：准实验虽有推断力，但因缺少随机分配仍可能受混杂偏误影响。

- rhetorical_function_cn：指出上一阶段识别局限。

- depends_on_cn：Stage 1结果。

- sets_up_cn：证明为何需要随机田野实验。

- evidence_pointer：Stage 2, first paragraph

### 44. Stage 2 setup paragraph

- order：44

- section：Stage 2

- locator：Stage 2 setup paragraph

- move_code：STUDY_OVERVIEW

- paraphrase_cn：田野实验随机分配3,808家门店到对照组、持续处理组和终止处理组。

- rhetorical_function_cn：描述实验设计。

- depends_on_cn：前一阶段遗留问题。

- sets_up_cn：给出持久性检验的具体结构。

- evidence_pointer：Table 6

### 45. Stage 2 Results, randomization check paragraph

- order：45

- section：Stage 2

- locator：Stage 2 Results, randomization check paragraph

- move_code：ROBUSTNESS_OR_BOUNDARY_TEST

- paraphrase_cn：三组在门店面积、收银台数、POS系统和购物篮等协变量上无明显差异。

- rhetorical_function_cn：验证随机化成功。

- depends_on_cn：随机分配。

- sets_up_cn：使组间对比可作因果解释。

- evidence_pointer：Table 8

### 46. Stage 2 Results, mean comparison paragraph

- order：46

- section：Stage 2

- locator：Stage 2 Results, mean comparison paragraph

- move_code：RESULT

- paraphrase_cn：继续监测组销量显著高于终止组和对照组；终止组显著低于继续组但高于对照组。

- rhetorical_function_cn：给出三组均值对比结果。

- depends_on_cn：随机化检查。

- sets_up_cn：引出回归估计的精确效应量。

- evidence_pointer：Table 9

### 47. Stage 2 Results, Table 10 paragraph

- order：47

- section：Stage 2

- locator：Stage 2 Results, Table 10 paragraph

- move_code：RESULT

- paraphrase_cn：终止IIP监测使销量约下降20%，说明零售商在监测移除后放松合规。

- rhetorical_function_cn：量化终止效应。

- depends_on_cn：三组实验。

- sets_up_cn：为部分持久性结果提供对照。

- evidence_pointer：Table 10

### 48. Stage 2 Results, Table 11 paragraph

- order：48

- section：Stage 2

- locator：Stage 2 Results, Table 11 paragraph

- move_code：RESULT

- paraphrase_cn：终止组相对从未监测的对照组仍保留正向销量效应，说明效果部分持续。

- rhetorical_function_cn：给出持久性回归证据。

- depends_on_cn：式(4)模型。

- sets_up_cn：支持人类学习解释。

- evidence_pointer：Table 11

### 49. Stage 3 opening paragraph

- order：49

- section：Stage 3

- locator：Stage 3 opening paragraph

- move_code：TRANSITION

- paraphrase_cn：前述分析尚未解释为何销量会增加，因此需要打开机制。

- rhetorical_function_cn：明确从效应转向机制。

- depends_on_cn：Stage 1和2结果。

- sets_up_cn：引入四阶段机制分析。

- evidence_pointer：Stage 3, first paragraph

### 50. Stage 3, Effect by Types of Retail Stores, second paragraph

- order：50

- section：Stage 3

- locator：Stage 3, Effect by Types of Retail Stores, second paragraph

- move_code：THEORY_PROPOSITION

- paraphrase_cn：AI具有超强工作记忆和计算速度，擅长处理重复且异质的任务。

- rhetorical_function_cn：为异质性机制提供理论基础。

- depends_on_cn：AI能力文献。

- sets_up_cn：推导出高异质性门店效果更强。

- evidence_pointer：Stage 3, Effect by Types of Retail Stores

### 51. Stage 3, Effect by Types of Retail Stores, hypothesis paragraph

- order：51

- section：Stage 3

- locator：Stage 3, Effect by Types of Retail Stores, hypothesis paragraph

- move_code：HYPOTHESIS_OR_PROPOSITION

- paraphrase_cn：面对时间约束和异质合同，AI应比人工更有效地完成货架监测，因而高异质性门店受益更大。

- rhetorical_function_cn：将理论转成可检验差异化预测。

- depends_on_cn：AI可扩展性理论。

- sets_up_cn：引出交互模型。

- evidence_pointer：Stage 3, Effect by Types of Retail Stores

### 52. Stage 3, Effect by Types of Retail Stores, results paragraph

- order：52

- section：Stage 3

- locator：Stage 3, Effect by Types of Retail Stores, results paragraph

- move_code：RESULT

- paraphrase_cn：低异质性门店提升不显著，中高异质性交互项显著且系数递增。

- rhetorical_function_cn：用异质性交互支持AI可扩展性。

- depends_on_cn：交互DID模型。

- sets_up_cn：为独立店/链店差异提供证据。

- evidence_pointer：Table 12

### 53. Stage 3, Change in Retailers’ Compliance, method paragraph

- order：53

- section：Stage 3

- locator：Stage 3, Change in Retailers’ Compliance, method paragraph

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：作者用AI系统输出的货架照片与报告测量面数合规率和位置合规率。

- rhetorical_function_cn：说明合规率数据的来源。

- depends_on_cn：Role of AI中的指标定义。

- sets_up_cn：检验AI→合规机制。

- evidence_pointer：Stage 3, Change in Retailers’ Compliance

### 54. Stage 3, Change in Retailers’ Compliance, results paragraph

- order：54

- section：Stage 3

- locator：Stage 3, Change in Retailers’ Compliance, results paragraph

- move_code：RESULT

- paraphrase_cn：首个治疗月无差异，随后月份两种合规率显著提升。

- rhetorical_function_cn：证明合规率在时间上跟随AI监测而上升。

- depends_on_cn：合规率数据结构。

- sets_up_cn：支持从监测到销售的因果链。

- evidence_pointer：Table 13

### 55. Stage 3, Effect of Taking Photos, setup paragraph

- order：55

- section：Stage 3

- locator：Stage 3, Effect of Taking Photos, setup paragraph

- move_code：STUDY_OVERVIEW

- paraphrase_cn：作者另设随机实验，一组拍照并收AI报告，另一组拍照但不收AI报告。

- rhetorical_function_cn：设计安慰剂对照以分离AI处理。

- depends_on_cn：需要排除拍照效应。

- sets_up_cn：为Photo和AI双变量模型作准备。

- evidence_pointer：Stage 3, Effect of Taking Photos

### 56. Stage 3, Effect of Taking Photos, results paragraph

- order：56

- section：Stage 3

- locator：Stage 3, Effect of Taking Photos, results paragraph

- move_code：RESULT

- paraphrase_cn：拍照系数不显著，AI系数显著为正，说明效果来自AI处理而非拍照。

- rhetorical_function_cn：排除替代解释。

- depends_on_cn：额外田野实验。

- sets_up_cn：把机制收敛到AI信息处理。

- evidence_pointer：Table 15

### 57. Stage 3, Interviews with Delegates, results paragraph

- order：57

- section：Stage 3

- locator：Stage 3, Interviews with Delegates, results paragraph

- move_code：RESULT

- paraphrase_cn：多数业务代表报告AI让检查更有效、提高反馈准确性、加强门店管理，并在异质性门店更有帮助。

- rhetorical_function_cn：用定性数据支持AI辅助监测机制。

- depends_on_cn：访谈程序。

- sets_up_cn：补充定量机制的参与者视角。

- evidence_pointer：Stage 3, Interviews with Delegates

### 58. Stage 3, Interviews with Retailers, results paragraph

- order：58

- section：Stage 3

- locator：Stage 3, Interviews with Retailers, results paragraph

- move_code：RESULT

- paraphrase_cn：零售商感知拜访时间未增加但反馈准确性提高，且多数不觉得过度监测。

- rhetorical_function_cn：从被监测方视角验证机制并回应过度监测担忧。

- depends_on_cn：零售商访谈。

- sets_up_cn：为过度监测附录提供依据。

- evidence_pointer：Stage 3, Interviews with Retailers

### 59. Discussion first paragraph

- order：59

- section：Discussion

- locator：Discussion first paragraph

- move_code：MECHANISM

- paraphrase_cn：访谈补充定量证据，支持AI帮助准确反馈、监测有效性提高、零售商合规和销量提升的因果链。

- rhetorical_function_cn：综合定量与定性为机制结论收束。

- depends_on_cn：Stage 3各机制证据。

- sets_up_cn：进入成本收益和结论。

- evidence_pointer：Discussion

### 60. Cost-Benefit Analysis paragraph

- order：60

- section：Cost-Benefit Analysis

- locator：Cost-Benefit Analysis paragraph

- move_code：RESULT

- paraphrase_cn：年成本约15.5万美元，年收益约2,720万美元，成本收益比约175.48。

- rhetorical_function_cn：给出经济可行性判断。

- depends_on_cn：Table 11效应量与2020年销售数据。

- sets_up_cn：支持长期采纳建议。

- evidence_pointer：Cost-Benefit Analysis section

### 61. Conclusion first paragraph

- order：61

- section：Conclusion

- locator：Conclusion first paragraph

- move_code：RESULT

- paraphrase_cn：作者总结三阶段研究，结论是IIP监测带来14%-17%销量提升，效果集中于高合同异质性门店，且终止后部分持续。

- rhetorical_function_cn：用一段话复述核心经验发现。

- depends_on_cn：所有阶段结果。

- sets_up_cn：为贡献和局限收尾。

- evidence_pointer：Conclusion

### 62. Conclusion limitations paragraph

- order：62

- section：Conclusion

- locator：Conclusion limitations paragraph

- move_code：LIMITATION_AND_FUTURE

- paraphrase_cn：作者承认未观察劳动力成本调整、缺少业务代表层面面板，访谈样本有限。

- rhetorical_function_cn：说明研究边界。

- depends_on_cn：全部分析。

- sets_up_cn：为未来研究留出空间。

- evidence_pointer：Conclusion

### 63. Appendix C final model

- order：63

- section：Appendix C

- locator：Appendix C final model

- move_code：ROBUSTNESS_OR_BOUNDARY_TEST

- paraphrase_cn：门店访问次数与销量正相关，未发现过度监测的递减回报。

- rhetorical_function_cn：用附加数据排除过度监测担忧。

- depends_on_cn：访问频率数据。

- sets_up_cn：强化监测效果的外部有效性。

- evidence_pointer：Appendix C, Table C1

## 写作技术

- gap_construction_cn：先用业务现实（新兴市场碎片化零售、人工监测不具扩展性）制造必须解决的问题；再指出AI替代模型研究多、AI辅助模型证据少；最后在货架管理文献中指出零售商视角优化多、制造商如何管理零售商货架少。三层缺口都指向同一个可执行研究。

- signposting_cn：引言明确写出三个研究问题和三阶段路线；Research Stages和每节开头用“Stage 1/2/3”和“four phases”做路标；每阶段末尾预告下一个阶段；表格和回归编号让论证可追踪。

- transition_logic_cn：每阶段开头先说明上一阶段留下的不确定性（如准实验非随机→田野实验；平均效应→机制；销售变化→合规变化→拍照安慰剂→定性解释），再说明本阶段如何解决该不确定性。

- claim_evidence_rhythm_cn：先给结果数字，再给经济解释，再给机制假设，逐步升级；每个主效应后都配一个相对时间模型/随机化检查/对照实验作为证据栅栏；定性访谈置于定量之后提供三角验证。

- benchmark_narrative_cn：人工监测作为全程基线；用Group1/Group2/Group0三组和仅拍照组形成多维对照组，使“AI”“人工”“拍照”“持续监测”“终止监测”可分离；成本收益以无AI情景为反事实。

- theory_return_cn：异质性结果被返回AI可扩展性理论；终止组结果被返回行为持续性理论；合规率与访谈结果被返回监测/理性欺骗者理论；最终在结论中把具体效果概括为AI辅助监测的一般适用条件。

- contribution_positioning_cn：作者把自己放在“AI辅助而非替代”“现场实验而非实验室”“制造商视角而非零售商视角”“异质实例可扩展性”“行为持续性”五个定位上，与已有AI商业价值和监测文献形成差异化。

- novelty_protection_cn：用多个独立设计互相印证：准实验给趋势、田野实验给因果、终止组给持久性、仅拍照对照排除无聊解释、访谈揭示参与者机制、成本收益给长期价值，因此贡献不易被视为一次性性能结果。

## 可复用研究与写作程序

### structure_steps

#### 1. 1

- step：1

- writing_job_cn：建立实际业务问题：货架管理重要但人工监测在异质市场不可扩展。

- research_job_cn：找到愿意合作的厂商/平台，获得部署、销售和门店特征数据。

- required_evidence_cn：证明存在合同合规约束和异质性零售网络，且有可获得的销售数据。

- transition_to_next_cn：提出效果、机制、长期三个问题，引出研究设计。

#### 2. 2

- step：2

- writing_job_cn：用准实验/现成数据先给初步证据。

- research_job_cn：收集部署前后销售面板和门店特征，做PSM+DID和相对时间模型。

- required_evidence_cn：需要平行趋势和显著主效应。

- transition_to_next_cn：说明非随机局限，预告随机实验。

#### 3. 3

- step：3

- writing_job_cn：做随机田野实验，包含启动和终止组。

- research_job_cn：与厂商合作随机分配门店，追踪销量，设置终止组。

- required_evidence_cn：需要随机化检查、两两比较和回归结果。

- transition_to_next_cn：从“是否有效”转入“为什么有效”。

#### 4. 4

- step：4

- writing_job_cn：拆解机制：异质性、合规率、安慰剂对照、访谈。

- research_job_cn：用同一数据做交互、用照片做合规率、另设最小实验、做访谈。

- required_evidence_cn：每部分都有统计或定性证据。

- transition_to_next_cn：把各环节拼接成因果链。

#### 5. 5

- step：5

- writing_job_cn：做成本收益/长期分析。

- research_job_cn：收集系统成本与市场规模数据，用效应量估算收益。

- required_evidence_cn：需要成本、销售基数和效应系数。

- transition_to_next_cn：把效果转成可持续性判断。

#### 6. 6

- step：6

- writing_job_cn：写贡献和边界。

- research_job_cn：梳理与文献的关系，明确适用条件。

- required_evidence_cn：需要说明外推假设。

- transition_to_next_cn：回到引言问题收束。

### most_transferable_moves_cn

1. 三阶段递进：准实验→随机田野实验→机制分析。

2. 在真实合作场景中把准实验作为证据预演、随机实验作为因果核心、机制实验排除替代解释。

3. 每个效应都配合对照和检查，如随机化检查、平行趋势、安慰剂组。

4. 用访谈补充参与者机制，量化结果与质性解释互相印证。

5. 用成本收益把因果估计转成管理利润含义。

### resource_intensive_or_nonstandard_parts_cn

1. 与大型FMCG厂商的长期合作。

2. 数千家门店随机分配和终止组指令。

3. 2021年额外现场实验。

4. 厂商内部照片、合规率和销售面板数据。

5. 大量业务代表和零售商的访谈渠道。

### what_not_to_copy_superficially_cn

1. 不可以只写“AI提升销售”而不做随机化。

2. 不能把门店类型差异直接说成异质性机制而无合规率或照片证据。

3. 不能把终止后仍高于基线直接说成学习而没有定性/过程证据。

4. 不能对单一市场短期效应做长期外推而忽视不可检验假设。

- single_best_description_of_the_routine_cn：用真实零售田野实验，把“AI辅助监测是否有效”变成可检验的因果问题，再以终止组和机制对照逐步打开“为什么有效”，最后用成本收益证明“值得长期用”的写作套路。

## 分析边界

提供文本缺少脚注内容（如脚注2、3、4、7、8、9、10、11、12），部分细节（如NDA处理和特定定义）依赖正文推断；附录A-C完整。实际页码不存在，位置证据使用段落与表格编号。
