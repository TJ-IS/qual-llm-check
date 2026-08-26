# Effectiveness of Location-Based Advertising and the Impact of Interface Design

- 作者：Dominik Molitor; Martin Spann; Anindya Ghose; Philipp Reichhart
- 年份 / 期刊：2020 / Journal of Management Information Systems
- DOI：10.1080/07421222.2020.1759922
- 源文件：01946_2020_effectiveness-of-location-based-advertising-and-the-impact-of-interface-design.md
- 论文主类型：field_intervention_or_platform_experiment
- 主导写作弧线：phenomenon_mechanism_intervention_field_test
- 置信度：0.86

## 文章级论证概况

- 核心问题：在位置型拉取式优惠券应用中，界面设计的选择架构——具体为是否提供距离信息和是否按距离排序——如何影响优惠券点击效果，以及这些效果如何随用户地理位置而不同？

- 制品与设计：被评价的数字制品是一个真实的位置型拉取式优惠券智能手机应用。核心设计包括一个2×2全因子现场实验操纵：距离排序/随机排序 × 提供距离信息/不提供距离信息，形成四个实验组。

- 客观结果：距离排序组的点击率显著高于随机排序组；距离排序且不显示距离信息的Group 3点击率最高；距离和展示排名都显著负向影响点击概率；随机排序会增强距离敏感度并减弱排名敏感度；用户所在城市、郊区、农村位置调节这些效应。

- 核心贡献：论文声称首次量化了位置型拉取式优惠券应用中界面选择架构的影响，将排名效应和距离效应文献扩展到拉取式移动优惠券情境，并用过度自信、权衡对比和情境依赖选择等行为理论解释异质性和偏离以往文献的结果。

- 整篇论证链：文章从移动广告和位置型优惠券的重要性出发，指出现有研究几乎只关注推送式优惠券，而拉取式优惠券在用户感知、互动方式和界面设计上存在根本差异，因而留下研究缺口。作者以选择架构理论、排名搜索成本、距离交通成本、过度自信和地理参考点为知识基础，将问题收缩到两个可操纵的界面设计维度，即距离信息提供和距离排序。随后，作者在真实应用中开展14周的大规模随机化现场实验，将4,364名新用户分配到2×2四组，并以399,913次展示为样本。先用模型无关的卡方检验比较组间点击率，发现距离排序最有效且距离信息反而可能降低效果；再按用户平均门店距离分成城市、郊区、农村三分位，发现位置调节效应；然后用分层贝叶斯logit模型估计距离和排名的主效应及与实验组的交互，发现随机排序增强距离敏感度并减弱排名敏感度。最后，通过稳健性检验和替代优惠券规格预测将结果提升为可复用的设计知识和管理建议，并回到排名、距离、过度自信和情境依赖理论。

## 类型与写作弧线判定

- 论文主类型判定：论文在真实运营的位置型优惠券App中，通过服务端随机分配对界面设计实施2×2现场实验操纵，并用点击率和模型估计评价用户行为响应，属于真实平台/产业环境中的数字设计实验。

- 主导写作弧线判定：文章先描述位置型拉取式优惠券的现象与独特特征，再引入排名、距离、过度自信和情境依赖等机制，随后实施界面设计现场干预，并用现场实验数据检验机制和边界条件，最后回到理论扩展。

## 研究开展程序

- study_or_phase_count：5

- 研究阶段总序列：先完成随机化现场实验设计和数据收集，为因果识别提供基础；然后用模型无关的组间比较回答RQ1前半部分；接着按地理区位细分回答RQ1后半部分；再用分层贝叶斯logit模型回答RQ2并量化效应；最后以稳健性检验和预测点击率收束，为理论和管理结论提供支撑。

### studies_or_phases

#### 1. 随机化现场实验设计与数据收集

- order：1

- name_cn：随机化现场实验设计与数据收集

- question_cn：在真实位置型优惠券应用中，如何随机分配用户到不同界面设计组合并形成可用于因果推断的数据？

- inputs_and_setting_cn：某欧洲大型电信公司旗下位置型拉取式优惠券App；德国2,392个ZIP区域；14周；4,364名首次下载应用的新用户；399,913次展示；3,499个优惠券推广；3,930家门店。

- designed_or_compared_object_cn：2×2全因子界面设计：距离排序/随机排序 × 有距离信息/无距离信息；Group 1为平台默认设计。

- baseline_control_or_counterfactual_cn：Group 1作为基准组；随机排序和删除距离信息分别构成反事实变体；同一用户固定在一个组，组间比较是核心反事实。

##### objective_metrics

1. 展示数

2. 点击数

3. 每用户会话数

4. 随机化完整性检验

- analysis_method_cn：服务端随机分配；首次登录用户；组间非实验变量对分配的解释力logit检验。

- main_result_cn：形成399,913条观察；四组样本分别为1,317、1,011、1,036、1,000；随机化完整，组间非实验变量不解释分配。

- argumentative_role_cn：建立现场实验的有效性前提，使后续点击率差异可以被归因于界面设计操纵。

- remaining_uncertainty_cn：尚未回答哪一界面设计更有效，也未控制用户、优惠券、时间等因素对点击的混淆影响。

- link_to_next_phase_cn：把数据带入模型无关的描述性组间比较，以回答RQ1的第一部分。

##### evidence_pointers

1. Randomized Field Experiment 节

2. Experimental Design 段

3. Note 7

#### 2. 模型无关的界面设计效果比较

- order：2

- name_cn：模型无关的界面设计效果比较

- question_cn：四种界面设计下，位置型拉取式优惠券的点击率是否存在显著差异？哪一种设计最有效？

- inputs_and_setting_cn：399,913次展示，四组用户，按总体、展示排名和产品类别分解。

- designed_or_compared_object_cn：比较总点击率、按排名的点击率分布、按产品类别的点击率。

- baseline_control_or_counterfactual_cn：Group 1为默认设计基准；Group 2缺失距离排序，Group 3缺失距离信息，Group 4同时缺失两者。

##### objective_metrics

1. 总体点击率

2. 各组点击率

3. 各排名位置点击率

4. 各产品类别点击率

5. 卡方检验统计量

- analysis_method_cn：模型无关的卡方显著性检验；图3、图4、图5描述性分析。

- main_result_cn：距离排序组点击率更高；Group 3（1.53%）显著高于Group 1（1.42%），也高于随机排序组；随机排序组的排名点击率接近均匀分布，距离排序组则呈指数式递减。

- argumentative_role_cn：提供RQ1最直接的证据：距离排序是最有效界面设计，并发现距离信息提供反而不是必要条件。

- remaining_uncertainty_cn：组间差异可能是用户异质性、时间、品类等协变量造成的，尚未被模型控制。

- link_to_next_phase_cn：引入地理区位细分，检验平均效果是否掩盖不同位置用户的异质性。

##### evidence_pointers

1. Effects of Interface Design 节

2. Figure 3

3. Figure 4

4. Figure 5

#### 3. 用户地理区位异质性分析

- order：3

- name_cn：用户地理区位异质性分析

- question_cn：界面设计有效性是否随用户所在城市、郊区或农村区域而变化？

- inputs_and_setting_cn：399,913次展示；按每次会话前25个展示的平均门店距离划分三分位：Urban（0.01–2.71 km）、Suburban（2.72–8.68 km）、Rural（8.69–50 km）。

- designed_or_compared_object_cn：比较四组界面设计在三种地理区位用户中的点击率。

- baseline_control_or_counterfactual_cn：同一实验组在不同地理区位的反事实对比，以及同一区位下四组间对比。

##### objective_metrics

1. 各区位×组的点击率

2. 卡方检验统计量

- analysis_method_cn：平均门店距离三分位分组；分组卡方显著性检验。

- main_result_cn：三个区位内的组间差异均显著；默认Group 1在城市效果相对差；郊区/农村用户对距离排序组反应更好，且看起来对距离不那么敏感。

- argumentative_role_cn：回答RQ1的后半部分，将平均效应限定为有边界条件的效应，并支持地理参考点机制。

- remaining_uncertainty_cn：区位是观察变量而非随机分配；仍未分离距离和排名各自的数量效应。

- link_to_next_phase_cn：激励使用分层贝叶斯logit模型估计主效应和界面设计交互效应。

##### evidence_pointers

1. Effects of Interface Design and Location-Specific Heterogeneity 节

2. Figure 6

#### 4. 分层贝叶斯Logit模型估计

- order：4

- name_cn：分层贝叶斯Logit模型估计

- question_cn：距离和展示排名对点击概率的效应有多大？这些效应是否因不同界面设计而不同？

- inputs_and_setting_cn：399,913条展示-点击面板；用户、优惠券、位置、时间等协变量。

- designed_or_compared_object_cn：估计Distance和Display_Rank主效应及其与Group 2/3/4的交互，对照组为Group 1。

- baseline_control_or_counterfactual_cn：Group 1的主效应作为基准，交互项识别其他实验组相对基准的差异。

##### objective_metrics

1. 后验均值

2. 标准差

3. 95%后验区间

4. 偏差（Deviance）

- analysis_method_cn：层次贝叶斯混合效应logit；MCMC Gibbs采样；25,000次迭代，保留后20,000次， thinning=20；用户层随机效应。

- main_result_cn：距离（β=-0.183）和展示排名（β=-0.354）均显著负向影响点击；随机排序组的距离负效应显著更强（Distance×Group2=-0.330，Distance×Group4=-0.276），排名负效应显著更弱（Rank×Group2=0.239，Rank×Group4=0.225）。

- argumentative_role_cn：回答RQ2，提供控制协变量后的量化效应，并把界面设计差异转化为距离敏感度和排名敏感度的变化。

- remaining_uncertainty_cn：点击不等于线下兑换；Group 3的距离和排名交互不显著；用户组别效应因个体内时不变无法估计。

- link_to_next_phase_cn：通过稳健性检验检验主变量是否稳定，并用模型预测替代优惠券规格的点击率。

##### evidence_pointers

1. Econometric Analysis 节

2. Estimation Results 表3

3. Note 15

#### 5. 稳健性检验与替代优惠券规格预测

- order：5

- name_cn：稳健性检验与替代优惠券规格预测

- question_cn：主结果在首登用户、不同使用强度、首页展示等条件下是否稳健？模型能否预测不同折扣、品类和过期日的点击率？

- inputs_and_setting_cn：在线补充附录中的额外分析：每用户首次登录、前15%高使用强度用户对比、控制首屏出现、分组单独估计；以及基准点击率预测。

- designed_or_compared_object_cn：与主模型比较系数符号和显著性；预测不同折扣深度、产品类别下的点击率。

- baseline_control_or_counterfactual_cn：主模型估计结果作为稳健性检验基准；预测时固定其他变量。

##### objective_metrics

1. 系数符号与显著性是否稳定

2. 预测点击率

- analysis_method_cn：基于同一现场实验数据的补充回归；模型预测反算点击概率。

- main_result_cn：距离和展示排名的符号与显著性基本保持；预测基期点击率1.23%，50%折扣升至1.42%，杂货类别1.70%，教育文化类别0.61%。

- argumentative_role_cn：保护核心因果结论免受样本选择、展示位置和使用强度等替代解释影响，并展示模型的管理预测价值。

- remaining_uncertainty_cn：预测基于观察到的优惠券配置；长期学习、重复曝光与过期日的随机分离、折扣深度的实验操纵仍未直接检验。

- link_to_next_phase_cn：收束到理论讨论、管理启示、局限与未来研究。

##### evidence_pointers

1. Estimation Results 末尾

2. Click Rate Predictions of Alternative Coupon Specifications 节

3. Online Supplemental Appendix

4. 表4

## 各部分修辞架构

### abstract_moves

1. CONTEXT: 线下零售商日益使用位置型优惠券实时接触附近消费者。

2. PHENOMENON: 位置距离提升相关性和有效性，但界面设计中的距离信息与距离排序是关键。

3. RQ_OR_OBJECTIVE: 研究并量化这两个界面设计维度对位置型优惠券效果的影响。

4. STUDY_OVERVIEW: 开展包含399,913次观察的随机化现场实验。

5. RESULT: 距离排序是最有效界面设计，距离和排名效应因界面设计与地理区位而异。

6. CONTRIBUTION: 增进了对位置型广告消费者行为响应的理解，并为界面设计提供启示。

### introduction_moves

1. CONTEXT: 移动广告是最大数字广告渠道，位置型优惠券是关键应用。

2. PHENOMENON: 位置型优惠券可分为推送式和拉取式。

3. LIMITATION: 以往研究几乎只关注推送式优惠券。

4. GAP: 拉取式优惠券在用户感知、互动和界面设计上不同，文献缺少对其界面设计的研究。

5. WHY_GAP_MATTERS: 企业需要了解界面设计如何优化位置型优惠券活动。

6. RQ_OR_OBJECTIVE: 提出两个研究问题：最有效界面设计以及距离/排名效应的大小如何随设计变化。

7. STUDY_OVERVIEW: 预告大规模随机化现场实验和模型分析。

### theory_and_knowledge_moves

1. THEORY_INTRO: 引入选择架构理论，说明界面设计影响用户决策。

2. PRIOR_KNOWLEDGE: 总结排名效应文献，强调高排名降低搜索成本并获得更多注意。

3. MECHANISM: 手机屏幕小导致更高认知搜索成本，因此排名效应更强。

4. PRIOR_KNOWLEDGE: 距离增加降低线下商店选择概率，移动情境下距离更重要。

5. THEORY_PROPOSITION: 距离信息提升交通成本显著性，但缺失时可能因过度自信而被低估。

6. THEORY_PROPOSITION: 地理区位形成参考点，远程用户对距离边际变化更不敏感。

### artifact_design_moves

1. DESIGN_FEATURE: 应用展示按实时GPS距离排序的新闻流式优惠券列表。

2. DESIGN_FEATURE: 优惠券档案包含价值、距离和简短信息；点击作为偏好显示。

3. DESIGN_FEATURE: 2×2实验操纵距离信息提供和排序机制。

4. BENCHMARK_OR_CONTRAST: Group 1为平台默认设计，其他组形成距离信息与排序的分解对照。

5. METHOD_JUSTIFICATION: 仅随机分配新用户以避免先前经验效应，服务端分配避免自选择。

### evaluation_moves

1. METHOD_JUSTIFICATION: 模型无关卡方检验回答RQ1的组间差异。

2. RESULT: 距离排序组点击率高于随机排序组，Group 3最高。

3. RESULT: 距离排序组的排名点击率呈指数递减，随机排序组近均匀。

4. METHOD_JUSTIFICATION: 分层贝叶斯logit控制个体异质性并估计交互效应。

5. RESULT: 距离和排名显著负向；随机排序增强距离敏感度、减弱排名敏感度。

6. ROBUSTNESS_OR_BOUNDARY_TEST: 附录中的首登、使用强度、首屏控制等检验保持主变量稳健。

### discussion_and_contribution_moves

1. CONTRIBUTION: 量化界面选择架构对位置型拉取式优惠券效果的影响。

2. MECHANISM: 过度自信解释无距离信息时点击率更高。

3. BOUNDARY_CONDITION: 郊区/农村用户对位置型优惠券反应更好。

4. CONTRIBUTION: 将排名和距离效应文献扩展到拉取式优惠券，并连接过度自信、权衡对比和情境依赖选择。

5. DESIGN_KNOWLEDGE: 管理建议包括距离桶拍卖、动态定价和首屏位置溢价。

6. LIMITATION_AND_FUTURE: 缺乏线下兑换数据、折扣深度未操纵、长期效应和重定向/过期分离留待未来。

## 理论/知识到设计的翻译

### 知识/理论基础

1. 选择架构理论：Johnson et al. 2012; Thaler et al. 2010

2. 排名效应与搜索成本：Ghose et al. 2014; Ursu 2018; Ghose et al. 2013; Mantonakis et al. 2009

3. 距离与交通成本：Bell et al. 1998; Ghose et al. 2013; Molitor et al. 2016; Forman et al. 2009

4. 过度自信：DellaVigna 2009; Buehler et al. 1994

5. 情境依赖选择与权衡对比：Simonson & Tversky 1992; Choi & Bell 2011

- 理论—设计耦合：direct

- 耦合判定理由：界面设计的两个操纵维度——距离信息提供和距离排序——直接来自排名效应、距离效应和过度自信等理论命题；这些命题不仅决定实验条件，还被模型交互项直接检验。

- 理论到设计翻译链：理论命题（高排名减少搜索成本、距离增加交通成本、距离信息缺失诱发过度自信、地理参考点影响边际敏感度）→ 行为机制（搜索成本、交通成本、成本显著性、参考点）→ 设计要求（界面应提供排序机制、可显示或不显示距离、应按距离排序）→ 具体制品选择（2×2现场实验四组）→ 被比较的设计差异（距离排序 vs 随机、有距离信息 vs 无）→ 客观结果（点击率差异、距离和排名系数差异）。

### mapping_table

#### 1. 1

- theory_or_knowledge_claim_cn：排序影响搜索成本，高排位选项更易被发现和选择，存在首因效应。

- mechanism_cn：手机屏幕小，低排位需要更多滚动和认知努力；高排位降低搜索成本并增加注意。

- design_requirement_cn：位置型优惠券界面需要有明确的排序机制，并可用距离作为相关性信号。

- artifact_choice_cn：将优惠券按距离升序排序（Group 1/3），对比随机排序（Group 2/4）。

- evaluated_contrast_cn：距离排序 vs 随机排序的点击率；展示排名系数的组间交互。

- objective_result_cn：距离排序组点击率更高；随机排序组排名负效应显著减弱（Rank×Group2=0.239，Rank×Group4=0.225）。

##### evidence_pointers

1. Figure 3

2. Table 3 Rank×Group2/4

#### 2. 2

- theory_or_knowledge_claim_cn：距离增加意味着交通成本增加，降低线下商店选择概率。

- mechanism_cn：用户需要到店兑换，距离越远，交通成本越高，吸引力越低。

- design_requirement_cn：界面应以距离作为相关性的核心维度，并可向用户展示具体距离。

- artifact_choice_cn：提供距离信息（Group 1/2） vs 不提供距离信息（Group 3/4）。

- evaluated_contrast_cn：Distance主效应；Distance×Group2/4交互，即随机排序下的距离敏感度。

- objective_result_cn：距离主效应显著为负（β=-0.183）；随机排序组的距离负效应显著更强（-0.330、-0.276）。

##### evidence_pointers

1. Table 3 Distance

2. Distance×Group2/4

#### 3. 3

- theory_or_knowledge_claim_cn：消费者对距离知识过度自信，没有距离信息时会低估到店所需时间或交通成本。

- mechanism_cn：距离信息缺失使交通成本不显著，用户高估自己对本地门店位置的了解，低估到达成本。

- design_requirement_cn：距离信息的提供并非总是有利，其成本显著性会改变选择。

- artifact_choice_cn：在距离排序基础上删除距离显示（Group 3 vs Group 1）。

- evaluated_contrast_cn：有距离信息 vs 无距离信息，在同样距离排序下的点击率。

- objective_result_cn：Group 3点击率1.53%，显著高于Group 1的1.42%。

##### evidence_pointers

1. Figure 3

2. Effects of Interface Design 第二段

#### 4. 4

- theory_or_knowledge_claim_cn：地理区位构成选择参考点，基础交通成本不同导致边际距离敏感度不同。

- mechanism_cn：城市门店密集、平均距离低，边际距离更敏感；农村平均距离高，边际距离较不敏感。

- design_requirement_cn：评估界面设计效果时应区分用户地理区位，而非只看平均效应。

- artifact_choice_cn：按会话平均门店距离三分位划分城市/郊区/农村，再比较四组。

- evaluated_contrast_cn：同一界面设计在不同区位用户中的点击率；区位内四组间差异。

- objective_result_cn：三区位组间差异均显著；默认Group 1在城市表现差，郊区和农村更偏好距离排序组。

##### evidence_pointers

1. Figure 6

2. Effects of Interface Design and Location-Specific Heterogeneity 节

#### 5. 5

- theory_or_knowledge_claim_cn：选择情境中的权衡对比影响评估，相邻选项距离差异越大，对比越突出。

- mechanism_cn：随机排序使相邻优惠券的距离差被放大（如100 m vs 1 km），近距离选项的相对吸引力更高。

- design_requirement_cn：排序机制会影响用户感知到的距离差异结构。

- artifact_choice_cn：随机排序组（Group 2/4）使距离不再作为排序信号。

- evaluated_contrast_cn：随机排序且有距离信息 vs 距离排序且有距离信息；随机排序时距离敏感度。

- objective_result_cn：Distance×Group2显著为负；注释报告随机排序组相邻距离差中位数是距离排序组的3.55倍。

##### evidence_pointers

1. Table 3 Distance×Group2

2. Note 16

## 评价逻辑

### evaluation_modes

1. 随机化现场实验：2×2全因子组间设计，真实App内服务端随机分配

2. 模型无关描述性检验：组间点击率卡方检验

3. 按展示排名和产品类别的分解分析

4. 按地理区位三分位的子组分析

5. 分层贝叶斯混合效应logit模型与MCMC估计

6. 稳健性检验：首登用户、高使用强度用户、首屏控制、分组单独估计

7. 反事实点击率预测：替代折扣深度、产品类别、过期日等规格

- why_these_evaluations_cn：RQ1需要随机化下的模型无关组间比较来回答哪种界面设计最有效；RQ2需要模型化估计距离和排名主效应及实验组交互，以控制用户异质性和协变量；地理区位分析回答边界条件；稳健性检验排除替代解释；预测为管理决策提供可操作价值。

- benchmark_and_contrast_chain_cn：以Group 1（平台默认设计：距离排序且有距离信息）为基准，Group 2孤立随机排序影响，Group 3孤立距离信息影响，Group 4综合两种缺失；描述性分析用组间总体、排名位置和品类分解累积证据；模型估计用Group 1主效应为基准，交互项量化其他组相对变化；区位分析在同组内比较城市/郊区/农村；预测部分把模型输出的点击率与总体基准点击率1.23%比较。

### claim_evidence_ledger

#### 1. 距离排序是最有效的界面设计

- claim_cn：距离排序是最有效的界面设计

- evidence_cn：图3显示距离排序组点击率更高，卡方检验显著；表3中排名交互效应支持排序机制重要性。

#### 2. 距离信息的提供在距离排序下反而不利

- claim_cn：距离信息的提供在距离排序下反而不利

- evidence_cn：Group 3点击率显著高于Group 1；表3中Distance×Group3不显著，说明删除距离信息没有显著增加距离负效应。

#### 3. 距离显著负向影响优惠券点击

- claim_cn：距离显著负向影响优惠券点击

- evidence_cn：表3 Distance系数为-0.183，95%后验区间不含0。

#### 4. 展示排名显著负向影响点击

- claim_cn：展示排名显著负向影响点击

- evidence_cn：表3 Display_Rank系数为-0.354，95%后验区间不含0。

#### 5. 随机排序增强距离敏感度并减弱排名敏感度

- claim_cn：随机排序增强距离敏感度并减弱排名敏感度

- evidence_cn：表3 Distance×Group2/4显著为负，Rank×Group2/4显著为正。

#### 6. 用户地理位置调节界面设计效果

- claim_cn：用户地理位置调节界面设计效果

- evidence_cn：图6三个区位内的组间差异均显著；Group 1在城市效果差，距离排序在郊区和农村更有效。

#### 7. 主结果在多种子样本和稳健性检验中保持

- claim_cn：主结果在多种子样本和稳健性检验中保持

- evidence_cn：正文报告首登、使用强度、首屏控制等附录分析中，距离和展示排名的符号与显著性保持。

- internal_validity_strategy_cn：采用服务端随机分配，避免用户自选择；仅纳入首次下载应用的新用户，减少先前经验干扰；用户不知道其他组存在；组间设计避免污染；用logit检验随机化完整性；在模型中控制时间、品类、使用强度等协变量；报告展示排名与距离相关性低以及VIF以排除共线性；附录中首登和首屏控制进一步支持因果解释。

- external_validity_strategy_cn：数据覆盖德国2,392个ZIP区域、3,930家门店、13个产品类别，空间广度远超以往单城研究；应用形态与Yelp、Foursquare、TripAdvisor、Groupon等距离排序应用相似；产品类别分布与Groupon数据比较以支持推广；通过对城市/郊区/农村三分位显示效应适用范围；同时承认单一国家、单一App、14周和点击而非兑换的限制。

- what_is_not_actually_tested_cn：未直接检验线下兑换或购买；未实验操纵折扣深度；未随机分离重复曝光/重定向与过期日期；未测量用户的过度自信或感知距离的心理变量；地理区位是观察划分而非随机分配；未覆盖其他操作系统、应用设计和所有位置型广告情境。

## 贡献闭环

- technical_claim_cn：分层贝叶斯混合效应logit模型能够在控制用户异质性后估计距离和展示排名对点击概率的影响，并识别不同界面设计下这些效应的差异。

- artifact_claim_cn：距离排序是位置型拉取式优惠券最有效的界面设计；提供距离信息在距离排序下并不必要，甚至可以降低点击率；随机排序会改变距离和排名的相对重要性。

- mechanism_claim_cn：排序通过搜索成本影响选择；距离通过交通成本影响吸引力；距离信息缺失使交通成本不显著并诱发过度自信；随机排序通过距离对比效应增强近距离优惠券的吸引力；地理区位作为参考点调节边际距离敏感度。

- boundary_claim_cn：界面设计效果受用户地理区位调节：城市用户对距离和排序更敏感，郊区/农村用户更接受距离排序且对距离较不敏感；结果主要适用于位置型拉取式优惠券情境，而非所有位置型广告。

- reusable_design_knowledge_cn：位置型优惠券应用应默认采用距离排序；距离显示可考虑按距离桶提供；在距离桶内可引入拍卖机制分配顶部排名；可根据用户实时距离、屏幕排名和地理区位动态定价；首屏顶部位置具有溢价价值。

- theoretical_contribution_cn：将排名效应和距离效应文献从推送式广告和搜索引擎扩展到位置型拉取式优惠券；用过度自信解释距离信息提供的反直觉效应；用权衡对比和情境依赖选择解释随机排序下距离敏感度增强；用地理参考点解释用户异质性。

- how_discussion_closes_intro_gap_cn：讨论部分重新回到引言提出的推送-拉取差异和研究缺口，明确宣称本文首次在真实随机化现场实验中量化拉取式位置型优惠券的界面选择架构，并用行为理论解释为何结果不同于基于推送式广告的既有文献，从而闭合缺口。

- overclaim_or_unsupported_leaps_cn：点击率被当作显示偏好，但不等同于兑换或购买；将Group 3高于Group 1解释为过度自信，缺少对过度自信的直接测量；地理区位是从观察性距离分布派生，不能完全排除区位选择的内生性；权衡对比机制仅由注释中相邻距离差的描述性统计支持，未纳入同一模型的正式检验；Group 2/3/4主效应不显著却强调实验组差异，主要是通过交互项识别。

## 句级写作动作图谱

### 1. P1 S1

- order：1

- section：Introduction

- locator：P1 S1

- move_code：CONTEXT

- paraphrase_cn：移动广告已占美国数字广告支出75%以上，位置型优惠券是其关键应用之一。

- rhetorical_function_cn：开篇强调研究领域的商业重要性。

- depends_on_cn：无，建立宏观背景。

- sets_up_cn：为后续聚焦位置型优惠券和广告有效性做铺垫。

- evidence_pointer：Introduction 第一段

### 2. P1 S2

- order：2

- section：Introduction

- locator：P1 S2

- move_code：PHENOMENON

- paraphrase_cn：位置型优惠券既可通过推送通知发送，也可由用户在应用内主动浏览获取，后者即拉取式。

- rhetorical_function_cn：界定本文研究对象与推送式区别。

- depends_on_cn：依赖位置型优惠券这一背景。

- sets_up_cn：为区分推送与拉取奠定概念基础。

- evidence_pointer：Introduction 第一段后半

### 3. P2 S1

- order：3

- section：Introduction

- locator：P2 S1

- move_code：LIMITATION

- paraphrase_cn：以往研究几乎只研究移动推送优惠券的用户响应。

- rhetorical_function_cn：指出研究重点是推送，未覆盖拉取。

- depends_on_cn：已区分推送/拉取。

- sets_up_cn：为文献缺口提供前提。

- evidence_pointer：Introduction 第二段

### 4. P2 S3

- order：4

- section：Introduction

- locator：P2 S3

- move_code：GAP

- paraphrase_cn：与以往研究推送优惠券不同，本文分析位置型拉取式优惠券应用。

- rhetorical_function_cn：直接声明研究对象转移。

- depends_on_cn：基于对既有推送文献的限制判断。

- sets_up_cn：提出尚未研究的情境。

- evidence_pointer：Introduction 第二段末尾

### 5. P3 S1

- order：5

- section：Introduction

- locator：P3 S1

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：移动拉取在用户感知、互动方式和界面设计三个方面与推送不同。

- rhetorical_function_cn：系统化说明拉取式差异。

- depends_on_cn：建立在研究对象转移之上。

- sets_up_cn：为界面设计作为核心机制提供分类框架。

- evidence_pointer：Introduction 第三段

### 6. P3 S3

- order：6

- section：Introduction

- locator：P3 S3

- move_code：MECHANISM

- paraphrase_cn：拉取式给用户更多控制权，用户出于不同动机主动搜索产品或服务。

- rhetorical_function_cn：解释拉取行为背后的用户主动机制。

- depends_on_cn：依赖拉取-推送差异。

- sets_up_cn：说明界面设计为何重要，因为用户主动浏览。

- evidence_pointer：Introduction 第三段

### 7. P4 S1

- order：7

- section：Introduction

- locator：P4 S1

- move_code：THEORY_INTRO

- paraphrase_cn：从理论看，不同优惠券选项的选择取决于界面呈现方式，即选择架构。

- rhetorical_function_cn：引入选择架构理论作为总框架。

- depends_on_cn：前面已把界面设计确认为关键差异。

- sets_up_cn：为两个设计变量提供理论锚点。

- evidence_pointer：Introduction 第四段

### 8. P4 S2

- order：8

- section：Introduction

- locator：P4 S2

- move_code：REQUIREMENT

- paraphrase_cn：影响展示优惠券相关性的两个关键变量是排序机制和距离信息提供。

- rhetorical_function_cn：从理论中提炼出两个可操纵的设计维度。

- depends_on_cn：依赖选择架构概念。

- sets_up_cn：直接对应后续2×2实验设计。

- evidence_pointer：Introduction 第四段

### 9. P4 S3-S4

- order：9

- section：Introduction

- locator：P4 S3-S4

- move_code：MECHANISM

- paraphrase_cn：用户选择受距离型交通成本和排名型搜索成本影响；距离信息使交通成本透明，排名搜索成本源于智能手机屏幕小。

- rhetorical_function_cn：解释两个设计变量为何影响用户选择。

- depends_on_cn：依赖排序和距离信息作为关键变量。

- sets_up_cn：为文献综述和理论背景提供机制菜单。

- evidence_pointer：Introduction 第四段后半

### 10. P6 S3

- order：10

- section：Introduction

- locator：P6 S3

- move_code：LIMITATION

- paraphrase_cn：大多数推送通知由操作系统标准化，且很少包含多个优惠券，因此不需要排序机制。

- rhetorical_function_cn：解释推送研究为何无法处理界面排序问题。

- depends_on_cn：对推送式广告的描述。

- sets_up_cn：强化拉取式界面设计研究的必要性。

- evidence_pointer：Introduction 第六段

### 11. P7 S1

- order：11

- section：Introduction

- locator：P7 S1

- move_code：GAP

- paraphrase_cn：因此，关于位置型拉取式优惠券与距离信息、距离排序界面设计互动的研究存在缺口。

- rhetorical_function_cn：正式明确文献缺口。

- depends_on_cn：综合推送标准化和拉取差异的论证。

- sets_up_cn：为研究问题和贡献定位。

- evidence_pointer：Introduction 第七段

### 12. P7 S2

- order：12

- section：Introduction

- locator：P7 S2

- move_code：WHY_GAP_MATTERS

- paraphrase_cn：企业需要了解如何通过界面设计优化位置型优惠券活动的行为效果。

- rhetorical_function_cn：说明缺口对实践的重要性。

- depends_on_cn：缺口叙述。

- sets_up_cn：为研究意义铺路。

- evidence_pointer：Introduction 第七段末尾

### 13. P8 S1-S3

- order：13

- section：Introduction

- locator：P8 S1-S3

- move_code：RQ_OR_OBJECTIVE

- paraphrase_cn：本文目标是量化距离排序和距离信息对位置型优惠券效果的影响，并提出两个研究问题。

- rhetorical_function_cn：正式设定研究问题和目标。

- depends_on_cn：基于识别出的缺口。

- sets_up_cn：确定后续实验和模型的结构。

- evidence_pointer：Introduction 第八段

### 14. P9 S1-S2

- order：14

- section：Introduction

- locator：P9 S1-S2

- move_code：STUDY_OVERVIEW

- paraphrase_cn：为回答问题，开展大规模随机化现场实验，并用模型无关检验和分层贝叶斯模型分别分析RQ1和RQ2。

- rhetorical_function_cn：预告方法和证据层次。

- depends_on_cn：依赖两个研究问题。

- sets_up_cn：为全文的结构做路标。

- evidence_pointer：Introduction 第九段

### 15. P10 S1-S2

- order：15

- section：Introduction

- locator：P10 S1-S2

- move_code：DESIGN_FEATURE

- paraphrase_cn：研究情境是一个真实的位置型拉取式优惠券应用，展示按距离实时排序的新闻流列表，并通过现场实验操纵界面设计。

- rhetorical_function_cn：说明实验情境和操纵方式。

- depends_on_cn：研究问题和方法预告。

- sets_up_cn：为实验设计细节做准备。

- evidence_pointer：Introduction 第十段

### 16. P2 S1

- order：16

- section：Literature Review

- locator：P2 S1

- move_code：CONTRAST

- paraphrase_cn：与以往研究相反，本文用包含广泛品类、门店和地理范围的大型随机化现场实验测量拉取式位置优惠券。

- rhetorical_function_cn：在文献对比中突出本研究的差异化定位。

- depends_on_cn：表1中对已有推送研究的总结。

- sets_up_cn：为贡献声明提供文献坐标。

- evidence_pointer：Literature Review 末段

### 17. P1 S2

- order：17

- section：Theoretical Background

- locator：P1 S2

- move_code：THEORY_PROPOSITION

- paraphrase_cn：拉取式用户可主动搜索和选择多种优惠券，因此用户选择强烈依赖优惠券信息的呈现方式。

- rhetorical_function_cn：从拉取交互特点推出选择架构的重要性。

- depends_on_cn：前面关于拉取式主动搜索的描述。

- sets_up_cn：引出排序和距离两个设计维度。

- evidence_pointer：Theoretical Background 第一段

### 18. Ranking Effects, P1

- order：18

- section：Theoretical Background

- locator：Ranking Effects, P1

- move_code：THEORY_PROPOSITION

- paraphrase_cn：相关性排序通过让用户更快找到产品来降低搜索成本。

- rhetorical_function_cn：引入排名效应的核心理论命题。

- depends_on_cn：选择架构框架。

- sets_up_cn：为距离排序作为设计选项提供理论依据。

- evidence_pointer：Theoretical Background Ranking Effects

### 19. Ranking Effects, P3

- order：19

- section：Theoretical Background

- locator：Ranking Effects, P3

- move_code：MECHANISM

- paraphrase_cn：排名效应在移动用户中比PC用户更强，因为小屏幕需要更高认知努力和搜索成本。

- rhetorical_function_cn：说明排名效应在智能手机情境下尤其重要。

- depends_on_cn：通用排名效应文献。

- sets_up_cn：解释为什么界面设计对移动端拉取式优惠券关键。

- evidence_pointer：Theoretical Background Ranking Effects

### 20. Ranking Effects, P4

- order：20

- section：Theoretical Background

- locator：Ranking Effects, P4

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：排名效应可能内生，因此需要用随机化实验检验排名效应。

- rhetorical_function_cn：为现场实验设计提供方法上的正当性。

- depends_on_cn：排名效应内生性讨论。

- sets_up_cn：说明为什么采用随机实验而非观察数据。

- evidence_pointer：Theoretical Background Ranking Effects 末段

### 21. Distance Effects, P1

- order：21

- section：Theoretical Background

- locator：Distance Effects, P1

- move_code：THEORY_PROPOSITION

- paraphrase_cn：距离是位置型应用排序的自然候选，附近门店的优惠券应被视为更相关并排得更高。

- rhetorical_function_cn：将距离与排序机制连接。

- depends_on_cn：排名搜索成本理论。

- sets_up_cn：为距离排序设计提供理论期望。

- evidence_pointer：Theoretical Background Distance Effects

### 22. Distance Effects, P5

- order：22

- section：Theoretical Background

- locator：Distance Effects, P5

- move_code：MECHANISM

- paraphrase_cn：同一优惠券在提供精确距离信息后可能被认为吸引力下降，因为距离显著性使交通成本透明，削弱了过度自信。

- rhetorical_function_cn：引入过度自信解释距离信息缺失可能更有利的反直觉预测。

- depends_on_cn：交通成本与过度自信文献。

- sets_up_cn：为Group 3结果提供理论预测。

- evidence_pointer：Theoretical Background Distance Effects

### 23. Moderating the Role of Geography, P1-P2

- order：23

- section：Theoretical Background

- locator：Moderating the Role of Geography, P1-P2

- move_code：THEORY_PROPOSITION

- paraphrase_cn：地理位置构成参考点；城市的平均距离低，农村的平均距离高，因此远程用户对边际距离更不敏感。

- rhetorical_function_cn：预测地理区位会调节距离效应。

- depends_on_cn：情境依赖选择与参考点文献。

- sets_up_cn：支撑随后的城市/郊区/农村三分位分析。

- evidence_pointer：Theoretical Background Moderating the Role of Geography

### 24. Location-Based Coupon Service, P1

- order：24

- section：Randomized Field Experiment

- locator：Location-Based Coupon Service, P1

- move_code：DESIGN_FEATURE

- paraphrase_cn：应用基于GPS展示按距离排序的优惠券新闻流，用户通过滚动浏览。

- rhetorical_function_cn：描述实验平台的核心功能。

- depends_on_cn：前述研究方法概述。

- sets_up_cn：说明平台具备位置型拉取式应用的关键特征。

- evidence_pointer：Randomized Field Experiment 节 Location-Based Coupon Service

### 25. Experimental Design, P1

- order：25

- section：Randomized Field Experiment

- locator：Experimental Design, P1

- move_code：DESIGN_FEATURE

- paraphrase_cn：实验操纵距离信息提供和排序机制，并将首次下载应用的新用户随机分配到四个实验组。

- rhetorical_function_cn：描述实验设计核心要素。

- depends_on_cn：理论背景中的两个设计维度。

- sets_up_cn：为2×2组间比较提供设计说明。

- evidence_pointer：Randomized Field Experiment Experimental Design

### 26. Experimental Design, P2

- order：26

- section：Randomized Field Experiment

- locator：Experimental Design, P2

- move_code：BENCHMARK_OR_CONTRAST

- paraphrase_cn：Group 1为距离排序且有距离信息；Group 2为随机排序且有距离信息；Group 3为距离排序但无距离信息；Group 4为随机排序且无距离信息。

- rhetorical_function_cn：建立四种设计的组合对照。

- depends_on_cn：实验操纵变量。

- sets_up_cn：作为后续所有比较的分析框架。

- evidence_pointer：Randomized Field Experiment Experimental Design 第二段

### 27. P1 S1-S2

- order：27

- section：Effects of Interface Design

- locator：P1 S1-S2

- move_code：RESULT

- paraphrase_cn：四组点击率总体差异显著，距离排序组高于随机排序组，Group 3最高。

- rhetorical_function_cn：报告RQ1最核心的描述性结果。

- depends_on_cn：实验设计和点击数据。

- sets_up_cn：支撑距离排序是最有效设计的结论。

- evidence_pointer：Effects of Interface Design 第一段，Figure 3

### 28. P1 后半

- order：28

- section：Effects of Interface Design

- locator：P1 后半

- move_code：BENCHMARK_OR_CONTRAST

- paraphrase_cn：将拉取式优惠券点击率与移动横幅广告0.33%的点击率比较，说明本文情境点击率较高。

- rhetorical_function_cn：提供行业基准，突出效果规模。

- depends_on_cn：已报告点击率结果。

- sets_up_cn：增强结果的外部参照意义。

- evidence_pointer：Effects of Interface Design 第一段末尾

### 29. P2 前半

- order：29

- section：Effects of Interface Design

- locator：P2 前半

- move_code：RESULT

- paraphrase_cn：即使没有距离信息，随机排序仍比距离排序点击率低，说明用户能察觉排序相关性。

- rhetorical_function_cn：解释距离排序与随机排序差异的机制。

- depends_on_cn：组间点击率比较。

- sets_up_cn：支持用户具有当地门店位置常识的解释。

- evidence_pointer：Effects of Interface Design 第二段

### 30. P2 后半

- order：30

- section：Effects of Interface Design

- locator：P2 后半

- move_code：RESULT

- paraphrase_cn：有距离信息且距离排序的Group 1点击率低于无距离信息的Group 3，可能反映过度自信导致低估距离。

- rhetorical_function_cn：报告反直觉结果并连接理论。

- depends_on_cn：理论背景中的过度自信命题。

- sets_up_cn：为后续模型和讨论中的过度自信解释做准备。

- evidence_pointer：Effects of Interface Design 第二段

### 31. Figure 4前一段

- order：31

- section：Effects of Interface Design

- locator：Figure 4前一段

- move_code：RESULT

- paraphrase_cn：按展示排名看，距离排序组点击率随排名指数下降，随机排序组几乎均匀。

- rhetorical_function_cn：通过排名位置分布补充总体结果。

- depends_on_cn：图3总体组间比较。

- sets_up_cn：说明距离和排名相对重要性依赖于排序设计。

- evidence_pointer：Effects of Interface Design 第三段，Figure 4

### 32. Figure 5前一段

- order：32

- section：Effects of Interface Design

- locator：Figure 5前一段

- move_code：ROBUSTNESS_OR_BOUNDARY_TEST

- paraphrase_cn：距离排序组点击率较高的模式在多个产品类别中成立，多个类别组间差异显著。

- rhetorical_function_cn：检验主结果是否仅由少数品类驱动。

- depends_on_cn：图3总体结果。

- sets_up_cn：增强结果稳健性。

- evidence_pointer：Effects of Interface Design 第四段，Figure 5

### 33. P1 后半

- order：33

- section：Effects of Interface Design and Location-Specific Heterogeneity

- locator：P1 后半

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：将每次会话前25个展示的平均门店距离分成三分位，近似城市、郊区、农村。

- rhetorical_function_cn：说明地理区位的操作化方法。

- depends_on_cn：地理参考点理论。

- sets_up_cn：为区位异质性结果提供方法。

- evidence_pointer：Effects of Interface Design and Location-Specific Heterogeneity 第一段

### 34. P2 前半

- order：34

- section：Effects of Interface Design and Location-Specific Heterogeneity

- locator：P2 前半

- move_code：RESULT

- paraphrase_cn：城市区位的默认Group 1效果较差，而郊区和农村区位中距离排序组更有效。

- rhetorical_function_cn：报告地理边界条件。

- depends_on_cn：三分位划分。

- sets_up_cn：支持参考点机制。

- evidence_pointer：Effects of Interface Design and Location-Specific Heterogeneity 第二段，Figure 6

### 35. P2 后半

- order：35

- section：Effects of Interface Design and Location-Specific Heterogeneity

- locator：P2 后半

- move_code：MECHANISM

- paraphrase_cn：远程用户因平均到店距离较高而更接受交通成本，因此对距离较不敏感。

- rhetorical_function_cn：解释区位异质性的机制。

- depends_on_cn：地理参考点理论。

- sets_up_cn：为讨论中的边界条件铺路。

- evidence_pointer：Effects of Interface Design and Location-Specific Heterogeneity 第二段末尾

### 36. Model 第一段

- order：36

- section：Econometric Analysis

- locator：Model 第一段

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：采用分层贝叶斯logit模型控制用户个体异质性。

- rhetorical_function_cn：说明模型选择原因。

- depends_on_cn：RQ2需要控制异质性。

- sets_up_cn：引入效用模型和估计方法。

- evidence_pointer：Econometric Analysis Model 第一段

### 37. Estimation 第一段

- order：37

- section：Econometric Analysis

- locator：Estimation 第一段

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：用MCMC Gibbs算法从后验分布抽样，并报告后验均值、标准差和95%后验区间。

- rhetorical_function_cn：说明统计推断程序。

- depends_on_cn：分层贝叶斯模型设定。

- sets_up_cn：为表3结果提供可信性。

- evidence_pointer：Econometric Analysis Estimation

### 38. Estimation Results 第一段

- order：38

- section：Econometric Analysis

- locator：Estimation Results 第一段

- move_code：RESULT

- paraphrase_cn：地理距离显著负向影响优惠券选择概率。

- rhetorical_function_cn：报告距离主效应。

- depends_on_cn：模型估计表3。

- sets_up_cn：支持交通成本机制。

- evidence_pointer：Estimation Results 表3 Distance

### 39. Estimation Results 第二段

- order：39

- section：Econometric Analysis

- locator：Estimation Results 第二段

- move_code：RESULT

- paraphrase_cn：展示排名显著负向影响点击概率，排名越靠后点击概率越低。

- rhetorical_function_cn：报告排名主效应。

- depends_on_cn：表3 Display_Rank。

- sets_up_cn：支持搜索成本机制。

- evidence_pointer：Estimation Results 第二段，表3 Display_Rank

### 40. Estimation Results 交互段

- order：40

- section：Econometric Analysis

- locator：Estimation Results 交互段

- move_code：RESULT

- paraphrase_cn：随机排序组中距离负效应显著更强。

- rhetorical_function_cn：报告界面设计对距离敏感度的调节。

- depends_on_cn：表3 Distance×Group2/4。

- sets_up_cn：支持随机排序下的距离对比效应。

- evidence_pointer：Estimation Results 第三、四段，表3 Distance×Group2/4

### 41. Estimation Results 排名交互段

- order：41

- section：Econometric Analysis

- locator：Estimation Results 排名交互段

- move_code：RESULT

- paraphrase_cn：随机排序组中排名负效应显著更弱，用户愿意为地理近距离的更低排名优惠券承担更多搜索成本。

- rhetorical_function_cn：报告界面设计对排名敏感度的调节。

- depends_on_cn：表3 Rank×Group2/4。

- sets_up_cn：说明距离比排名更重要。

- evidence_pointer：Estimation Results 第五段，表3 Rank×Group2/4

### 42. Estimation Results 控制变量段

- order：42

- section：Econometric Analysis

- locator：Estimation Results 控制变量段

- move_code：RESULT

- paraphrase_cn：折扣深度正向影响点击，但促销券无金额折扣也受欢迎；会话印象数、先前点击数、过期时间等控制变量均显著。

- rhetorical_function_cn：报告控制变量的结果，排除替代解释。

- depends_on_cn：完整模型估计。

- sets_up_cn：支持后续预测和管理建议。

- evidence_pointer：Estimation Results 第六至八段

### 43. Estimation Results 品类段

- order：43

- section：Econometric Analysis

- locator：Estimation Results 品类段

- move_code：RESULT

- paraphrase_cn：产品类别之间存在显著点击偏好差异，例如杂货和多媒体高于理发店，教育文化低于理发店。

- rhetorical_function_cn：报告品类控制变量。

- depends_on_cn：模型中包含品类固定效应。

- sets_up_cn：展示品类异质性，并与Groupon研究可比。

- evidence_pointer：Estimation Results 品类段，表3

### 44. Estimation Results 末尾

- order：44

- section：Econometric Analysis

- locator：Estimation Results 末尾

- move_code：ROBUSTNESS_OR_BOUNDARY_TEST

- paraphrase_cn：在线附录中的首登用户、使用强度、首屏控制等稳健性分析中，距离和展示排名主变量在符号和显著性上保持稳定。

- rhetorical_function_cn：报告稳健性检验结论。

- depends_on_cn：主模型结果。

- sets_up_cn：增强全文核心结论的可信度。

- evidence_pointer：Estimation Results 末尾，Online Supplemental Appendix

### 45. P1-P2

- order：45

- section：Click Rate Predictions of Alternative Coupon Specifications

- locator：P1-P2

- move_code：RESULT

- paraphrase_cn：模型预测总体点击率1.23%，50%折扣提升至1.42%，杂货类别1.70%，教育文化0.61%。

- rhetorical_function_cn：展示模型的反事实预测能力。

- depends_on_cn：分层贝叶斯logit模型。

- sets_up_cn：为动态定价和品类策略提供量化工具。

- evidence_pointer：Click Rate Predictions of Alternative Coupon Specifications

### 46. RQ1讨论段

- order：46

- section：Concluding Discussion

- locator：RQ1讨论段

- move_code：CONTRIBUTION

- paraphrase_cn：距离排序是最有效的界面设计，而距离信息在距离排序下不必要；过度自信可解释无距离信息时更高的点击率。

- rhetorical_function_cn：将RQ1结果上升为理论性贡献。

- depends_on_cn：描述性结果和模型结果。

- sets_up_cn：与引言中的界面设计缺口闭合。

- evidence_pointer：Concluding Discussion and Managerial Interpretation

### 47. RQ2讨论段

- order：47

- section：Concluding Discussion

- locator：RQ2讨论段

- move_code：CONTRIBUTION

- paraphrase_cn：距离效应和排名效应并非恒定，而是依赖排序设计；随机排序时排名负效应减弱、距离负效应增强，可用权衡对比解释。

- rhetorical_function_cn：将RQ2结果转化为对既有文献的修正。

- depends_on_cn：贝叶斯模型交互项。

- sets_up_cn：为后续理论扩展和管理启示奠基。

- evidence_pointer：Concluding Discussion RQ2段

### 48. 总结段

- order：48

- section：Concluding Discussion

- locator：总结段

- move_code：CONTRIBUTION

- paraphrase_cn：本文延伸排名和距离效应文献，并应用过度自信、权衡对比和情境依赖选择理论。

- rhetorical_function_cn：明确宣称理论贡献。

- depends_on_cn：前文全部结果和讨论。

- sets_up_cn：收束全文的理论定位。

- evidence_pointer：Concluding Discussion 末段

### 49. 第一条与第二条

- order：49

- section：Managerial Implications

- locator：第一条与第二条

- move_code：DESIGN_KNOWLEDGE

- paraphrase_cn：企业可在距离桶内拍卖排名、根据实时距离和屏幕排名动态定价。

- rhetorical_function_cn：把结果转化为可操作的设计原则。

- depends_on_cn：距离和排名效应量化结果。

- sets_up_cn：说明研究对优惠券平台和商家的商业价值。

- evidence_pointer：Managerial Implications 第一、二段

### 50. P1-S1

- order：50

- section：Limitations and Future Research

- locator：P1-S1

- move_code：LIMITATION_AND_FUTURE

- paraphrase_cn：没有线下购买数据，无法验证实际兑换；点击只能作为显示偏好。

- rhetorical_function_cn：诚实界定研究局限。

- depends_on_cn：数据来源。

- sets_up_cn：为未来研究提供方向。

- evidence_pointer：Limitations and Future Research 第一句

### 51. 末段

- order：51

- section：Conclusions

- locator：末段

- move_code：BOUNDARY_CONDITION

- paraphrase_cn：结果不一定推广到所有位置型广告情境，但为企业和后续研究提供了关键基线。

- rhetorical_function_cn：限定外部效度并保护贡献。

- depends_on_cn：全文结论。

- sets_up_cn：防止读者过度一般化。

- evidence_pointer：Conclusions 末段

## 写作技术

- gap_construction_cn：先承认现有文献几乎全聚焦推送式优惠券，然后论证拉取式在感知、互动和界面设计三个维度与推送本质不同，最后指出推送通知的标准化和单优惠券特征使排序问题无法在推送研究中出现，从而构造出拉取式界面设计缺口。

- signposting_cn：引言明确预告两个研究问题和使用模型无关检验+分层贝叶斯模型；在理论背景中以Ranking Effects、Distance Effects、Moderating the Role of Geography分层设标；每个分析小节末尾连接下一阶段。

- transition_logic_cn：从总体组间比较过渡到按排名和品类分解，再过渡到地理区位异质性，再到计量模型；每次过渡都基于前一阶段留下的未解决问题，例如“描述性差异需要控制协变量后验证”。

- claim_evidence_rhythm_cn：每个重要主张几乎都同时给出描述性图/表和推断性表3；先用低价门槛的卡方检验给出直觉证据，再用后验区间给出量化证据，最后用稳健性检验保护证据。

- benchmark_narrative_cn：将Group 1设为平台正常设计作为内部基准，把2×2组间差异作为主benchmark；还将拉取式点击率与移动横幅广告点击率比较，形成外部绩效参照；模型预测点击率又提供管理上的反事实benchmark。

- theory_return_cn：结果不是在讨论中才提出理论，而是理论背景中先预设了过度自信、交通成本、搜索成本和参考点，结果段和讨论段反复用这些概念解释Group 3高于Group 1、随机排序组距离敏感度更高、农村用户更接受距离。

- contribution_positioning_cn：将贡献放在“首次研究拉取式位置优惠券界面设计”和“扩展排名/距离效应文献”两个层面，避免只宣称一个App的实验效果；管理层建议进一步把贡献物化为可操作的界面和定价知识。

- novelty_protection_cn：用随机化现场实验的支持来防止结果被视为一次性性能差异；通过大地理范围、多品类和平台默认设计对比，强调结果不是特定数据集偶然；通过理论机制解释“为什么”而不是只报告“是什么”，避免贡献退化为单一点击率数字。

## 可复用研究与写作程序

### structure_steps

#### 1. 1

- step：1

- writing_job_cn：引言：从行业重要性切入，界定研究对象（拉取 vs 推送），明确指出既有文献缺口和研究问题。

- research_job_cn：找到现有文献没有覆盖的真实数字设计问题，并确认存在可操纵的设计维度。

- required_evidence_cn：需要证明研究对象在现实中的重要性，以及既有研究确实集中在另一机制上。

- transition_to_next_cn：用两个研究问题预告研究阶段。

#### 2. 2

- step：2

- writing_job_cn：理论背景：将两个设计维度与选择架构、搜索成本、交通成本、过度自信、参考点等机制连接。

- research_job_cn：把待检验的界面差异转化成有理论含义的对比。

- required_evidence_cn：需要已有文献支持每个机制与结果之间的因果关系。

- transition_to_next_cn：以理论命题导出实验设计的具体操纵。

#### 3. 3

- step：3

- writing_job_cn：实验设计：描述平台、操纵变量、分组、随机化方式和数据。

- research_job_cn：在真实平台实施随机分配，建立干净反事实。

- required_evidence_cn：需要平台数据、随机化过程和组间可比性证据。

- transition_to_next_cn：进入描述性结果。

#### 4. 4

- step：4

- writing_job_cn：模型无关结果：用组间比较、按排名/品类分解和地理子组给出直观证据。

- research_job_cn：先不让模型假设干扰证据，直接检验平均差异和异质性。

- required_evidence_cn：需要足够大的样本和统计检验，使组间差异可被直接观察。

- transition_to_next_cn：指出描述性差异需要用模型控制协变量并量化效应。

#### 5. 5

- step：5

- writing_job_cn：计量模型：设定效用模型，说明分层贝叶斯方法和估计细节，报告主效应与交互。

- research_job_cn：用模型估计效应大小、显著性及设计依赖的交互项。

- required_evidence_cn：需要面板数据和合理先验/估计算法。

- transition_to_next_cn：用稳健性检验和预测把模型结果推回结论。

#### 6. 6

- step：6

- writing_job_cn：稳健性与预测：报告子样本/首登/首屏检验，并给出替代规格的预测点击率。

- research_job_cn：排除替代解释，展示结果的可推广性和管理用途。

- required_evidence_cn：需要额外的样本拆分或辅助数据。

- transition_to_next_cn：进入讨论、管理启示和局限。

#### 7. 7

- step：7

- writing_job_cn：讨论与贡献：回到引言缺口，用行为理论解释结果，提炼设计知识和边界条件。

- research_job_cn：把具体点击率差异提升为可复用的设计原则和理论贡献。

- required_evidence_cn：需要结果与理论机制一致，并明确限制条件。

- transition_to_next_cn：以局限和未来研究结束。

### most_transferable_moves_cn

1. 用2×2全因子设计把抽象界面维度分解为可直接比较的实验条件

2. 以平台默认设计作为基准组，使结果对实践者有意义

3. 先做模型无关描述性检验，再做异质性分析，最后用贝叶斯模型控制个体异质性

4. 用交互项量化设计条件对主要效应的调节，而不仅报告主效应

5. 通过地理区位三分位寻找边界条件

6. 将点击率预测转化为动态定价和排名拍卖建议

### resource_intensive_or_nonstandard_parts_cn

1. 与大型电信公司旗下真实App合作，开展14周现场实验

2. 服务端随机分配4,364名新用户，覆盖399,913次展示

3. 数据覆盖2,392个ZIP区域和3,930家门店，普通学术项目难以轻易复制

4. 在线补充附录中的额外稳健性分析依赖原始平台数据和用户级点击记录

5. 移动App的产品更新和运营条件不能在实验室完全模拟

### what_not_to_copy_superficially_cn

1. 不能只写“距离排序最重要”而不实际操纵排序机制

2. 不能把点击率当作兑换率或购买率而不加说明

3. 不能在没有随机分配的地理区位数据时声称因果性的区位调节

4. 不能把城市/郊区/农村三分位说成随机实验处理

5. 不能在没有过度自信测量时把点击率差异直接归因于过度自信

- single_best_description_of_the_routine_cn：先把真实应用界面拆成两个可操纵的设计维度并随机分配给用户，然后用模型无关检验找到最有效设计，再用分层贝叶斯模型量化距离和排名效应及其设计依赖，最后用行为理论解释为何违反直觉并转化为管理设计知识。

## 分析边界

文章全文可读，但供分析的图多为正文引用而非逐像素可读；在线补充附录的具体表格未包含在文本中，因此稳健性检验细节主要依据正文描述，无法对附录内部数字进行独立核对。
