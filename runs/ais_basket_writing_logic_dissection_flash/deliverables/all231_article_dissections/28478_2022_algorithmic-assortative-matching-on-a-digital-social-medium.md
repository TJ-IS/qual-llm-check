# Algorithmic Assortative Matching on a Digital Social Medium

- 作者：Kristian López Vargas; Julian Runge; Ruizhi Zhang
- 年份 / 期刊：2022 / Information Systems Research
- DOI：10.1287/isre.2022.1135
- 源文件：28478_2022_algorithmic-assortative-matching-on-a-digital-social-medium.md
- 论文主类型：field_intervention_or_platform_experiment
- 主导写作弧线：problem_theory_design_test_return
- 置信度：0.78

## 文章级论证概况

- 核心问题：在freemium数字社交环境中，算法辅助的正向类聚匹配（将高预期价值新用户推荐给高活跃团队）对用户参与、消费、社交和团队产出的因果影响是什么，其作用机制是什么？

- 制品与设计：一个基于机器学习的匹配系统：用户侧用XGBoost预测30天CLV并分为likely/unlikely payer；团队侧用多维活动分（活跃人数、团队任务、礼物、消息、收入）分为high/low activity；每天按供需阈值将高价值用户推荐到高活跃团队名单，保留用户自由选择具体团队。

- 客观结果：用户层面平均净效应：消息+13.2%、任务开始+10.1%、任务成功+9.2%、收入+2.7%、留存+0.9%；团队层面每个新用户转入类聚匹配带来收入/消息约+5%，任务开始+4.2%、成功+4.7%；低活跃团队接收低价值用户时受损；生产函数估计显示团队规模报酬递增与超模性，消息的中介作用显著。

- 核心贡献：第一次在真实数字环境中用田野实验外生操纵类聚匹配，给出用户-群体匹配而非用户-用户匹配的证据；刻画freemium环境的生产技术与超模性；指出算法促成类聚可能加剧数字社区极化。

- 整篇论证链：先从freemium应用用户留存低、社交体验重要的现实出发，指出新用户与既有社区的匹配方式可能决定参与和付费；鉴于环境具有互补性，作者设计高价值用户进高活跃团队的算法匹配系统；通过三开三关六周田野实验，证明系统对平均用户和团队有正向净效应；随后估计CES生产函数，发现团队层面递增规模报酬导致超模性，并证明社交行为（消息）是主要中介；最终把结果上升为对匹配理论、freemium平台设计和社交媒体极化的贡献，并警示低质量用户与低质量团队进一步隔离。

## 类型与写作弧线判定

- 论文主类型判定：论文在真实移动游戏App中部署了算法匹配系统，并通过时间维度上的on/off切换进行田野实验；核心证据来自对真实平台中数字设计的操纵和现场因果检验，而非实验室或纯benchmark研究。

- 主导写作弧线判定：文章首先提出freemium应用中用户匹配的现实问题，引入assortative matching与生产互补性理论，据此设计算法系统，再通过田野实验检验，最后通过生产函数估计和中介分析把结果返回并细化理论机制，形成完整闭环。

## 研究开展程序

- study_or_phase_count：9

- 研究阶段总序列：前四个阶段构成制品构建与预评价：环境刻画→团队分类→用户CLV模型→离线政策评估；第五阶段部署田野实验产生因果变异；第六、七阶段分别从用户和团队层面估计主效应；第八、九阶段转向机制，先估计生产技术再检验社交中介。各阶段依次收紧了从‘可能有效’到‘因果有效’再到‘为何有效’的论证。

### studies_or_phases

#### 1. 环境刻画与随机匹配基线

- order：1

- name_cn：环境刻画与随机匹配基线

- question_cn：研究所在的freemium社交游戏环境具有什么结构？用户如何加入团队？

- inputs_and_setting_cn：一个匿名合作方的移动解谜/角色扮演游戏，约9000个团队，团队上限30人；用户在达到资格后看到随机团队列表。

- designed_or_compared_object_cn：无需操纵，描述制度性基线：随机团队推荐、团队搜索成本高、玩家自由选择但信息有限。

- baseline_control_or_counterfactual_cn：随机团队列表作为后续处理的反事实基线。

##### objective_metrics

1. 游戏内行为描述

2. 团队规模

3. 进入团队资格时间

- analysis_method_cn：描述性统计和环境制度分析。

- main_result_cn：大多数新用户依赖随机推荐页加入团队；团队质量信息分散，选择近似随机。

- argumentative_role_cn：建立真实场景和‘随机匹配’基线，说明为什么匹配方式是可以被算法改进的管理决策。

- remaining_uncertainty_cn：尚未证明类聚匹配会带来何种因果后果。

- link_to_next_phase_cn：引出需要先构建用户和团队分类器，以便实施类聚匹配。

##### evidence_pointers

1. Section 3

2. Environment段落中team recommendation描述

#### 2. 团队活动分类模型构建与验证

- order：2

- name_cn：团队活动分类模型构建与验证

- question_cn：如何将团队分为high/low activity，并保证分类有经济意义？

- inputs_and_setting_cn：团队层面每日变量：活跃玩家数、团队任务数、礼物交换量、消息数、团队收入；14天移动平均；未来30天收入。

- designed_or_compared_object_cn：综合活动评分（几何平均），以30%分位作为高活跃阈值。

- baseline_control_or_counterfactual_cn：top 30%团队与其余团队在未来收入上的对比。

##### objective_metrics

1. 未来30天收入占比

2. 活动阈值命中率

- analysis_method_cn：产品经理协作构造评分，对任意日期排序并测量未来收入集中度。

- main_result_cn：top 30%团队捕获至少80%的下月收入，能代表最高产社交群体。

- argumentative_role_cn：为匹配系统提供团队侧‘高活跃’的可操作定义，保证推荐目标确实与收入和社会行为相关。

- remaining_uncertainty_cn：该分类只保证相关性，不证明把用户送入这些团队会带来因果收益。

- link_to_next_phase_cn：需要用户侧分类器来识别哪些新用户值得被推荐到高活跃团队。

##### evidence_pointers

1. Section 4.1

2. Team Classification验证段落

#### 3. 用户CLV预测模型构建与评价

- order：3

- name_cn：用户CLV预测模型构建与评价

- question_cn：在几乎没有购买历史且类别不平衡的情况下，能否用早期行为特征预测未来付费者？

- inputs_and_setting_cn：约52,000训练用户、约100,000时间独立holdout；人口统计和到资格前行为特征。

- designed_or_compared_object_cn：线性回归、随机森林、梯度提升、XGBoost，并结合SMOTE过采样。

- baseline_control_or_counterfactual_cn：随机猜测和传统CLV方法作为基准。

##### objective_metrics

1. hit rate

2. top 50%排名内捕获实际付费者比例

- analysis_method_cn：五折交叉验证、SMOTE、特征选择、超参调优、时间外验证。

- main_result_cn：XGBoost在top 50%预测排名中捕获约80%实际付费者，比随机猜测好60%。

- argumentative_role_cn：构建用户侧‘likely payer’分类器，使高价值用户识别具有可验证的预测性能。

- remaining_uncertainty_cn：预测性能不等于推荐给高活跃团队会产生因果效果。

- link_to_next_phase_cn：需要利用历史数据做离线政策评估，判断类聚推荐是否值得进入生产环境。

##### evidence_pointers

1. Section 4.2

2. Table 1

3. User Classification结果段落

#### 4. 离线政策评估

- order：4

- name_cn：离线政策评估

- question_cn：在真实部署前，类聚匹配对用户行为结果的预期影响是什么？

- inputs_and_setting_cn：历史随机匹配时期的数据；用户倾向得分和加入团队类型。

- designed_or_compared_object_cn：使用倾向得分匹配回归，比较具有相似高价值倾向但加入不同类型团队的用户。

- baseline_control_or_counterfactual_cn：历史加入低活跃团队的高/低价值用户作为对照。

##### objective_metrics

1. 消息发送

2. 任务开始

3. 任务成功

4. 收入

5. 留存

- analysis_method_cn：倾向得分匹配回归（在线附录A）。

- main_result_cn：likely payer加入高活跃团队显著增加消息和任务参与；unlikely payer多数结果不显著，但消息有正向效应。

- argumentative_role_cn：在低成本条件下预验证系统可能带来的净正向影响，支撑合作方授权生产部署。

- remaining_uncertainty_cn：历史数据存在自选择，倾向得分不能完全消除混淆。

- link_to_next_phase_cn：离线证据支持后，进入真实平台田野实验以获得因果估计。

##### evidence_pointers

1. Section 4.3末尾

2. Section A in online appendix

#### 5. 田野实验部署与操纵检验

- order：5

- name_cn：田野实验部署与操纵检验

- question_cn：算法系统是否在真实环境中按计划产生高-高、低-低匹配的分离路径？

- inputs_and_setting_cn：六周实验期，系统以三天间隔开关；新用户到达时间与开关状态近似独立。

- designed_or_compared_object_cn：处理期使用类聚匹配，控制期沿用随机团队列表；团队层面形成高活跃团队接收更多likely payer的分离。

- baseline_control_or_counterfactual_cn：off期间随机匹配作为处理的反事实。

##### objective_metrics

1. 高价值用户进入高活跃团队的比例

2. 高/低活跃团队接收不同类型用户数量

- analysis_method_cn：时间序列操纵检验、比例观察。

- main_result_cn：on期间接近100%的likely payer进入高活跃团队，off期间约等于随机比例；图1与图2显示分离路径。

- argumentative_role_cn：证明处理确实被实施，为后续因果估计提供外生变异。

- remaining_uncertainty_cn：时间式设计可能受周内/事件效应影响，尽管设计用三开三关缓解。

- link_to_next_phase_cn：操纵成功后才可解释用户和团队层面的回归结果。

##### evidence_pointers

1. Section 5

2. Figure 1

3. Figure 2

#### 6. 用户层面主回归

- order：6

- name_cn：用户层面主回归

- question_cn：类聚匹配对新用户的参与、消费、社交和留存有什么净效应？

- inputs_and_setting_cn：44,874名实验期间加入的新用户；14天结果窗口。

- designed_or_compared_object_cn：SystemON（on/off）和HighActivity（加入高/低活跃团队）两个二元处理。

- baseline_control_or_counterfactual_cn：off期加入的likely payer为参照；另检验unlikely payer和平均用户效应。

##### objective_metrics

1. Revenue

2. Messages

3. Retention

4. Mission starts

5. Mission successes

- analysis_method_cn：OLS回归（式1），交互项，事件和星期固定效应，设备组/渠道控制。

- main_result_cn：likely payer在社交和参与上显著受益，消息增加20%；unlikely payer在消息和任务开始上受损；平均用户净效应全部显著为正，消息最强。

- argumentative_role_cn：检验H1、H3、H5和H9，确立用户层面的因果效应及异质性。

- remaining_uncertainty_cn：14天短期效应不一定持久；收入效应弱。

- link_to_next_phase_cn：用户层面结果需要团队层面检验，确认对现有群体是否也产生净收益。

##### evidence_pointers

1. Section 6.1.1

2. Table 2

#### 7. 团队层面回归

- order：7

- name_cn：团队层面回归

- question_cn：类聚匹配对现有团队和团队整体产出的净效应是什么？

- inputs_and_setting_cn：4,635个团队；实验最后14天聚合结果；实验前控制变量。

- designed_or_compared_object_cn：团队接收的likely/unlikely payer数量及其与低活跃团队的交互。

- baseline_control_or_counterfactual_cn：高活跃团队且不加入新用户的情形为参照，并用组合t检验模拟随机→类聚的边际转移。

##### objective_metrics

1. Revenue

2. Messages

3. Mission starts

4. Mission successes

- analysis_method_cn：团队层面OLS回归（式2），含实验前结果控制。

- main_result_cn：每个payer加入高活跃团队带来收入2.4%、消息2.1%等正向影响；unlikely payer加入高活跃团队有负向影响；低活跃团队接收低价值用户受损；净效应每个新用户约+5%。

- argumentative_role_cn：检验H2、H4、H6，证明整体净效应为正且部分源于团队重组。

- remaining_uncertainty_cn：团队层面效应可能是行为变化、技术变化和重组的混合，无法直接分解。

- link_to_next_phase_cn：需要刻画生产技术以解释为什么重组产生正向净效应。

##### evidence_pointers

1. Section 6.1.2

2. Table 3

3. Equation (2)

#### 8. 生产技术估计与超模性分析

- order：8

- name_cn：生产技术估计与超模性分析

- question_cn：环境的生产技术是否具有超模性和规模报酬递增？它们如何解释类聚匹配的收益？

- inputs_and_setting_cn：实验前六周观测数据；个人投入（时间、游戏内支出、等级）与团队产出。

- designed_or_compared_object_cn：CES个人生产函数嵌套CES团队生产函数；分别估计高/低活跃团队及实验前后。

- baseline_control_or_counterfactual_cn：σ>ρ作为超模性条件；σ>1作为规模报酬递增。

##### objective_metrics

1. 参数δ, σ, ρ

2. σ/ρ比

3. 生产率因子

- analysis_method_cn：非线性最小二乘估计、delta method检验。

- main_result_cn：所有产出σ显著大于ρ，团队层面σ在1.04–1.75；消息的ρ约0.4，表现出最强超模性；规模报酬递增是超模性主要来源。

- argumentative_role_cn：检验H7，提供机制证据，说明高-高匹配因生产互补性而有效率。

- remaining_uncertainty_cn：生产函数把制度规则和交互行为混在一起；收入分布偏态导致估计不稳定。

- link_to_next_phase_cn：需要单独考察社交行为作为中介，以解释为何消息效应最大。

##### evidence_pointers

1. Section 6.2.1

2. Table 4

3. Section E in online appendix

#### 9. 社交性机制与中介分析

- order：9

- name_cn：社交性机制与中介分析

- question_cn：社交行为（消息）是否构成系统影响其他产出的中介机制？

- inputs_and_setting_cn：用户层面结果变量、高社交团队评分、消息作为中介变量。

- designed_or_compared_object_cn：用社交评分替代活动评分重新估计；加入社交与技术的交互；SEM中介分解。

- baseline_control_or_counterfactual_cn：高活动团队效应作为对照；低社交团队为参照。

##### objective_metrics

1. Revenue

2. Messages

3. Retention

4. Mission starts

5. Mission successes

6. 直接/间接效应

- analysis_method_cn：OLS替换变量、交互回归、结构方程中介模型。

- main_result_cn：按社交评分匹配的效果与按活动评分匹配相似；社交与技术评分呈替代关系；中介分析中间接效应显著，收入与任务成功的直接效应接近零。

- argumentative_role_cn：检验H8-H10，将主效应归于社会互动机制，支持‘社交是渠道’的理论解释。

- remaining_uncertainty_cn：中介分析依赖较强识别假设；并未直接测量极化或福利后果。

- link_to_next_phase_cn：机制确立后，结论部分把结果放回匹配理论与公平性讨论。

##### evidence_pointers

1. Section 6.2.2

2. Table 5

3. Section G/H in online appendix

## 各部分修辞架构

### abstract_moves

1. CONTEXT：数字环境与freemium应用普及。

2. PRACTICAL_STAKES：早期社交体验影响长期行为。

3. RQ_OR_OBJECTIVE：研究算法类聚匹配系统的影响。

4. DESIGN_FEATURE：ML系统识别高预期用户并推荐高活跃团队。

5. STUDY_OVERVIEW：在数字社交游戏中田野实验。

6. RESULT：显著提升参与、消费和社交。

7. BOUNDARY_CONDITION：低活跃团队受负面影响，环境更隔离。

8. MECHANISM：社交经验与群体社交行为是可能机制。

### introduction_moves

1. CONTEXT：移动设备使用时间和app经济规模。

2. PRACTICAL_STAKES：freemium定价驱动社交app的收入和时间占用。

3. PRIOR_KNOWLEDGE：已有文献确认社交体验对freemium参与和收入重要。

4. PHENOMENON：无进入壁垒导致大量异质用户，留存率极低。

5. PRACTICAL_STAKES：如何把新用户匹配到社区成为关键决策。

6. MECHANISM：互补性/替代性决定正/负类聚匹配方向。

7. GAP：事前正负类聚都可能成立，缺乏因果证据。

8. RQ_OR_OBJECTIVE：研究相对优劣及价值共创机制。

9. THEORY_INTRO：初步分析显示互补性，设计正向类聚系统。

10. DESIGN_FEATURE：用分析驱动系统推荐高价值用户到高活跃团队。

11. RESULT：田野实验显示净正向效应且低质量端受损。

12. MECHANISM：超模性与递增规模报酬，消息最突出。

13. CONTRIBUTION：freemium monetization、assortative matching、社交媒体极化。

14. LIMITATION_AND_FUTURE：算法透明与公平性问题。

15. STUDY_OVERVIEW：给出论文路线图。

### theory_and_knowledge_moves

1. THEORY_PROPOSITION：Becker提出可转移效用与技术互补下类聚匹配有效。

2. PRIOR_KNOWLEDGE：Kremer和实验室公共品实验支持类聚匹配提高贡献。

3. MECHANISM：条件合作者在类聚匹配中更少被搭便车者打击。

4. LIMITATION：数字平台中用户-群体匹配研究稀缺。

5. PRIOR_KNOWLEDGE：Hitsch等的在线约会研究是用户-用户匹配的代表。

6. PRIOR_KNOWLEDGE：Ahmadpoor和Jones提供团队生产技术估计框架。

7. GAP：freemium文献分别证明社交影响付费，但未处理多结果同时作用的净效应。

8. PRIOR_KNOWLEDGE：CLV预测从购买历史方法走向ML和SMOTE。

### artifact_design_moves

1. REQUIREMENT：环境存在互补性且随机列表搜索成本高，需要提高匹配价值。

2. METHOD_JUSTIFICATION：保留用户自由选择，避免内生群体形成影响。

3. DESIGN_FEATURE：用户/团队双分类，高价值用户进高活跃团队。

4. DESIGN_FEATURE：团队活动分用几何平均聚合五个维度。

5. RESULT：top 30%团队捕获至少80%未来收入。

6. DESIGN_FEATURE：用户CLV用XGBoost与SMOTE预测。

7. RESULT：分类器比随机猜测好60%。

8. DESIGN_FEATURE：每日更新阈值平衡高活跃团队空位与新用户供给。

9. RESULT：离线PSM评估支持系统预期正向效果。

### evaluation_moves

1. STUDY_OVERVIEW：时间式田野实验，三天开关持续六周。

2. METHOD_JUSTIFICATION：周内事件异质性和星期季节性在开关之间近似平衡。

3. METHOD_JUSTIFICATION：用户到达与开关状态独立，等价于用户级随机化；时间分离可识别团队效应。

4. HYPOTHESIS_OR_PROPOSITION：提出H1-H10，从个体/团队效应到净效应再到机制。

5. METHOD_JUSTIFICATION：用户级14天窗口，团队级实验最后14天窗口。

6. RESULT：用户层面SystemON与HighActivity回归表。

7. RESULT：团队层面NumPayers/NumUnlikelyPayers回归表。

8. RESULT：CES生产函数估计参数表。

9. RESULT：高社交评分替代活动评分估计。

10. RESULT：SEM中介分析。

11. ROBUSTNESS_OR_BOUNDARY_TEST：更长时窗、四分类、排除新成员的稳健性。

### discussion_and_contribution_moves

1. RESULT：总结平均净效应和团队效应。

2. MECHANISM：强调社交化是主要驱动。

3. BOUNDARY_CONDITION：适用于freemium数字产品、用户协作共创的在线社区。

4. CONTRIBUTION：首个数字环境类聚匹配田野实验，扩展Hitsch et al.。

5. CONTRIBUTION：刻画freemium生产技术的超模性。

6. CONTRIBUTION：管理意义——如何识别高价值用户并提供个性化社交体验。

7. BOUNDARY_CONDITION：低质量匹配造成团队分离和社区极化。

8. LIMITATION_AND_FUTURE：最优类聚程度、长期社区凝聚力、公平性。

## 理论/知识到设计的翻译

### 知识/理论基础

1. assortative matching theory (Becker 1973, Kremer 1993, Shimer and Smith 2000)

2. team production and supermodularity (Topkis 1998; Ahmadpoor and Jones 2019)

3. freemium平台中社交与同伴效应 (Oestreicher-Singer and Zalmanson 2013; Bapna and Umyarov 2015; Bapna et al. 2018)

4. CLV预测与机器学习 (Fader et al. 2005; Sifa et al. 2018; Vanderveld et al. 2016)

5. 条件合作者与内生群体形成 (Page et al. 2005; Carrell et al. 2013; Hitsch et al. 2010)

- 理论—设计耦合：partial

- 耦合判定理由：Becker式互补性理论决定了‘高-高匹配优于随机匹配’的核心方向，并把评价聚焦于超模性；但用户分类器的具体算法（XGBoost+SMOTE）、团队评分阈值、每日供需均衡等关键制品实现来自机器学习和产品管理经验，而非由理论直接导出。

- 理论到设计翻译链：理论命题（互补性→类聚匹配有效）→环境初步分析（潜在互补性）→设计需求（高价值用户进入高活跃团队）→制品选择（用户CLV分类器+团队活动评分+每日阈值分配）→实验对比（on/off随机vs类聚）→结果（净正向效应）→机制估计（CES超模性+社交中介）。

### mapping_table

#### 1. 1

- theory_or_knowledge_claim_cn：Becker/Kremer：若生产具有互补性，正向类聚匹配有效。

- mechanism_cn：高技能/高活跃成员相互提升产出，高价值用户对相似用户影响更大。

- design_requirement_cn：应该把likely payer推荐给high activity团队，而把unlikely payer留给低活跃团队。

- artifact_choice_cn：正类聚匹配系统：只在高活跃团队空位范围内，把最高预测收入用户推荐到高活跃团队。

- evaluated_contrast_cn：SystemON(类聚) vs off(随机)；HighActivity vs LowActivity。

- objective_result_cn：平均用户和团队净效应为正；表2、表3。

##### evidence_pointers

1. Section 4 Intro

2. Section 5.2 H1-H6

3. Table 2

4. Table 3

#### 2. 2

- theory_or_knowledge_claim_cn：生产团队中的超模性/递增规模报酬使团队规模与质量互补（Ahmadpoor and Jones, Topkis）。

- mechanism_cn：团队层面σ>ρ导致战略互补；规模报酬递增使更大/更高质量团队产生更高人均回报。

- design_requirement_cn：匹配系统应主动重组团队以利用递增规模报酬。

- artifact_choice_cn：以活动评分挑选高活跃团队并注入高价值用户。

- evaluated_contrast_cn：生产函数中σ与ρ比较；高/低活跃团队分别估计。

- objective_result_cn：σ在1.04-1.75，σ>ρ对所有产出成立；表4。

##### evidence_pointers

1. Section 6.2.1

2. Table 4

#### 3. 3

- theory_or_knowledge_claim_cn：freemium社交文献：社交参与和同伴付费转化正相关。

- mechanism_cn：社会化是影响参与和花钱的中间机制。

- design_requirement_cn：团队分类应反映社交行为而不仅是收入。

- artifact_choice_cn：团队活动分包含消息与礼物；社交分独立用于机制检验。

- evaluated_contrast_cn：HighSoc vs LowSoc；消息作为中介。

- objective_result_cn：高社交团队效应与高活动团队接近；中介间接效应显著。

##### evidence_pointers

1. Section 4.1

2. Section 6.2.2

3. Table 5

4. Section H

#### 4. 4

- theory_or_knowledge_claim_cn：CLV预测可用非购买行为特征和ML在无购买历史时预测付费（Sifa et al.）。

- mechanism_cn：早期行为痕迹携带用户异质性信息。

- design_requirement_cn：在用户进入资格时即时预测30天收入，处理类别不平衡。

- artifact_choice_cn：XGBoost + SMOTE，每日重训练。

- evaluated_contrast_cn：多种模型 vs 随机猜测。

- objective_result_cn：XGBoost在top50%捕获约80%实际付费者，比随机好60%。

##### evidence_pointers

1. Section 4.2

2. User Classification结果段落

#### 5. 5

- theory_or_knowledge_claim_cn：实验室公共品研究：类聚匹配提高条件合作者贡献。

- mechanism_cn：用户在与高活跃同伴互动时更愿意保持参与和贡献。

- design_requirement_cn：匹配应维持用户自由加入感知，避免内生群体形成效应污染。

- artifact_choice_cn：系统只改变推荐列表，不强制加入；用户仍选择具体团队。

- evaluated_contrast_cn：类聚推荐 vs 随机推荐，用户自由选择恒常。

- objective_result_cn：系统净正向且消息最强，说明自愿加入下机制成立。

##### evidence_pointers

1. Section 4 intro

2. Section 5.1

3. Table 2

## 评价逻辑

### evaluation_modes

1. 分类器离线评价：hit rate、时间独立holdout

2. 离线政策评估：倾向得分匹配回归

3. 田野实验：时间式on/off因果识别

4. 用户层面reduced-form OLS

5. 团队层面聚合OLS

6. 生产函数参数估计

7. 机制检验：社交评分替换、交互、SEM中介分析

8. 稳健性：更长时窗、四分类、排除新成员

- why_these_evaluations_cn：每一层评价解决前一层无法回答的问题：分类器只证明‘能预测’；离线评估证明‘可能有效’；田野实验证明‘因果有效’；生产函数与中介分析解释‘为什么有效’。评价从低成本到高成本、从预测到因果再到机制依次递进。

- benchmark_and_contrast_chain_cn：随机猜测→历史随机匹配→off期随机匹配→低活跃团队→低社交团队，逐步形成参照系；最后用70/30用户比例和80%收入团队比例构造团队净效应t检验，把局部估计加总为政策效应。

### claim_evidence_ledger

1. 用户分类器60%优于随机猜测：由时间独立holdout hit rate支持。

2. 类聚匹配对平均用户净正向：Table 2 panel A Net effect检验支持。

3. 加入高活跃团队对likely payer正向：Table 2 panel B HighAct系数支持。

4. unlikely payer被类聚匹配伤害：Table 2 SystemON×UnlikelyPayer交互显著为负（消息/任务开始）。

5. 团队层面净效应约5%：Table 3组合t检验支持。

6. 生产函数超模性：Table 4 σ>ρ且σ>1，delta method显著。

7. 社交是机制：Table 5高社交团队效应相似、SEM中介间接效应显著。

8. 技术不随时间大幅变化：附录表10-12的支持，但文中提醒收入分布偏态。

- internal_validity_strategy_cn：利用用户到达时间与开关区间独立实现近似随机；三开三关平衡周内事件和星期；回归中加入事件、星期、设备组、渠道和实验前团队特征；团队层面用实验前结果控制。

- external_validity_strategy_cn：论证环境是头部社交手游，符合通用freemium+社区协作特征；结论外推到其他freemium数字产品和社交媒体，并借助与在线约会、极化文献的类比。

- what_is_not_actually_tested_cn：最优类聚程度没有被直接搜索；长期动态均衡、真实社交媒体的极化进程、福利后果和公平性损失未被直接测量；中介分析未在实验上操纵消息，因此因果中介识别较弱。

## 贡献闭环

- technical_claim_cn：提出的XGBoost+SMOTE用户分类器在早期稀疏行为数据上预测未来付费者表现显著优于随机猜测。

- artifact_claim_cn：可部署的正类聚匹配系统在真实环境中增加了用户参与、社交和消费；用户级净效应消息13.2%、任务开始10.1%、任务成功9.2%、收入2.7%、留存0.9%。

- mechanism_claim_cn：正向净效应源于团队层面递增规模报酬导致的超模性；社交行为（消息）是主要中介，消息的超模性也最强。

- boundary_claim_cn：适用于用户通过协作共创价值的freemium数字产品；对低活跃团队和低价值用户会产生负面外部性，导致社区隔离。

- reusable_design_knowledge_cn：识别高预期用户并推荐到高活跃团队可以提升聚合参与和收入；但应警惕低端用户匹配的负面效应；更细的用户/团队分类可能改善结果。

- theoretical_contribution_cn：扩展assortative matching到用户-群体匹配并在真实数字平台提供外生变化；用CES生产函数刻画freemium生产技术的超模性与递增规模报酬；连接社交媒体极化文献，暗示算法类聚可能是极化驱动因素。

- how_discussion_closes_intro_gap_cn：引言提出正负类聚事前皆可能、缺乏因果证据；结论用田野实验与机制估计明确回答正向类聚净收益为正，同时指出其分配性代价，从而同时满足管理设计与公平关注。

- overclaim_or_unsupported_leaps_cn：把单游戏环境推广到一般社交媒体可能过度；中介分析对消息的因果解释依赖较强假设；‘社交是机制’主要靠间接证据；关于极化的推断是外推而非直接测量。

## 句级写作动作图谱

### 1. Abstract P1 S1-S2

- order：1

- section：Abstract

- locator：Abstract P1 S1-S2

- move_code：CONTEXT

- paraphrase_cn：人类越来越多地在结构化数字环境中互动和生活，主要表现是各类app。

- rhetorical_function_cn：开篇给出宏观背景，把研究放在数字社会环境中。

- depends_on_cn：无。

- sets_up_cn：为freemium和社交app的重要性做铺垫。

- evidence_pointer：Abstract首句

### 2. Abstract P1 S3-S4

- order：2

- section：Abstract

- locator：Abstract P1 S3-S4

- move_code：PRACTICAL_STAKES

- paraphrase_cn：这些数字环境大多采用freemium定价，用户的早期社交体验对长期行为影响很大。

- rhetorical_function_cn：强调研究对象的现实重要性。

- depends_on_cn：背景句。

- sets_up_cn：引出匹配系统影响早期体验的问题。

- evidence_pointer：Abstract首段后半

### 3. Abstract P2 S1

- order：3

- section：Abstract

- locator：Abstract P2 S1

- move_code：RQ_OR_OBJECTIVE

- paraphrase_cn：在此基础上研究算法匹配系统把新用户以类聚方式匹配到既有社区的影响。

- rhetorical_function_cn：直接提出论文研究对象。

- depends_on_cn：背景和现实重要性。

- sets_up_cn：后文描述系统与实验。

- evidence_pointer：Abstract第二段首句

### 4. Abstract P2 S2

- order：4

- section：Abstract

- locator：Abstract P2 S2

- move_code：DESIGN_FEATURE

- paraphrase_cn：作者设计了基于机器学习的匹配系统，识别高预期价值用户，并把他们引导到高活跃高消费团队。

- rhetorical_function_cn：说明制品的核心机制。

- depends_on_cn：提出的研究对象。

- sets_up_cn：为实验发现做铺垫。

- evidence_pointer：Abstract第二段中句

### 5. Abstract P2 S3

- order：5

- section：Abstract

- locator：Abstract P2 S3

- move_code：STUDY_OVERVIEW

- paraphrase_cn：在数字社交游戏中实验部署该机制。

- rhetorical_function_cn：预告研究方法。

- depends_on_cn：制品描述。

- sets_up_cn：引向结果句。

- evidence_pointer：Abstract第二段末

### 6. Abstract P2 S4

- order：6

- section：Abstract

- locator：Abstract P2 S4

- move_code：RESULT

- paraphrase_cn：实验显著提高用户参与、消费和社交化。

- rhetorical_function_cn：给出核心实证结论。

- depends_on_cn：实验部署。

- sets_up_cn：为后续边界条件和机制总结提供主干。

- evidence_pointer：Abstract第三段首

### 7. Abstract P2 S5

- order：7

- section：Abstract

- locator：Abstract P2 S5

- move_code：BOUNDARY_CONDITION

- paraphrase_cn：该结论只在更活跃社区和总体层面成立；低活跃新用户匹配的低活跃团队受到负面影响，环境更隔离。

- rhetorical_function_cn：限定结果的适用边界并提示负面效应。

- depends_on_cn：正向主结果。

- sets_up_cn：为讨论极化与公平性做准备。

- evidence_pointer：Abstract第三段中后句

### 8. Abstract P2 S6

- order：8

- section：Abstract

- locator：Abstract P2 S6

- move_code：MECHANISM

- paraphrase_cn：作者认为社交经验和群体社交行为是驱动匹配系统影响的核心机制。

- rhetorical_function_cn：提前给出机制主张。

- depends_on_cn：主结果和负面结果。

- sets_up_cn：正文中用消息数据和中介分析支撑。

- evidence_pointer：Abstract末句

### 9. Introduction P1 S1-S3

- order：9

- section：Introduction

- locator：Introduction P1 S1-S3

- move_code：CONTEXT

- paraphrase_cn：人类在移动设备上花大量时间，app下载量和支出巨大。

- rhetorical_function_cn：建立宏观数字经济的现实背景。

- depends_on_cn：无。

- sets_up_cn：引入freemium定价模型。

- evidence_pointer：Intro第一段前句

### 10. Introduction P1 S4-S7

- order：10

- section：Introduction

- locator：Introduction P1 S4-S7

- move_code：PRACTICAL_STAKES

- paraphrase_cn：freemium定价使应用免费使用，通过内购和广告盈利，社交app尤其占据收入和时间。

- rhetorical_function_cn：说明数字平台商业化与社交化的实际重要性。

- depends_on_cn：宏观背景。

- sets_up_cn：引出社交体验对收入的作用。

- evidence_pointer：Intro第一段中后句

### 11. Introduction P1 S8

- order：11

- section：Introduction

- locator：Introduction P1 S8

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：已有文献表明社交体验对freemium环境的参与和收入很关键。

- rhetorical_function_cn：说明这不是全新问题，而是已有领域的重要决策。

- depends_on_cn：现实重要性。

- sets_up_cn：文献缺口将在后面出现。

- evidence_pointer：Intro第一段末

### 12. Introduction P2 S1-S3

- order：12

- section：Introduction

- locator：Introduction P2 S1-S3

- move_code：PHENOMENON

- paraphrase_cn：freemium没有进入门槛，大量用户进入后第一印象决定去留，留存率很低。

- rhetorical_function_cn：描述需要被管理的关键经验现象。

- depends_on_cn：freemium背景。

- sets_up_cn：把问题聚焦到新用户与社区的匹配。

- evidence_pointer：Intro第二段前句

### 13. Introduction P2 S4-S5

- order：13

- section：Introduction

- locator：Introduction P2 S4-S5

- move_code：PRACTICAL_STAKES

- paraphrase_cn：面对大量异质评价用户，厂商如何把新用户匹配进社区是最大化参与、留存、社区健康和消费的关键决策。

- rhetorical_function_cn：把经验现象转成厂商管理决策。

- depends_on_cn：低留存现象。

- sets_up_cn：匹配方法的重要性与理论方向。

- evidence_pointer：Intro第二段中句

### 14. Introduction P2 S6-S8

- order：14

- section：Introduction

- locator：Introduction P2 S6-S8

- move_code：MECHANISM

- paraphrase_cn：匹配方法取决于用户与社区是互补还是替代，决定应正向还是负向类聚；事前两种策略都可能合理。

- rhetorical_function_cn：提出两种机制方向，显示问题的open nature。

- depends_on_cn：匹配决策的现实重要性。

- sets_up_cn：为论文‘比较两种思路’的目标服务。

- evidence_pointer：Intro第二段后句

### 15. Introduction P3 S1

- order：15

- section：Introduction

- locator：Introduction P3 S1

- move_code：RQ_OR_OBJECTIVE

- paraphrase_cn：论文主旨在研究两种匹配方法的相对优劣，并理解用户为厂商共创价值的机制。

- rhetorical_function_cn：清晰声明研究目标和问题。

- depends_on_cn：事前两种可能的张力。

- sets_up_cn：后续提到初步分析和系统设计。

- evidence_pointer：Intro第三段首句

### 16. Introduction P3 S2-S3

- order：16

- section：Introduction

- locator：Introduction P3 S2-S3

- move_code：DESIGN_FEATURE

- paraphrase_cn：基于初步分析发现环境有潜在互补性，作者设计分析驱动的正向类聚匹配系统。

- rhetorical_function_cn：从研究问题转向制品设计。

- depends_on_cn：互补性判断。

- sets_up_cn：为实验部署做准备。

- evidence_pointer：Intro第三段中句

### 17. Introduction P3 S4

- order：17

- section：Introduction

- locator：Introduction P3 S4

- move_code：STUDY_OVERVIEW

- paraphrase_cn：系统在社交游戏app中进行大规模田野实验。

- rhetorical_function_cn：预告实证策略。

- depends_on_cn：制品描述。

- sets_up_cn：引出摘要中的结果。

- evidence_pointer：Intro第三段末

### 18. Introduction P4-P5

- order：18

- section：Introduction

- locator：Introduction P4-P5

- move_code：RESULT

- paraphrase_cn：田野实验显示正向类聚系统对参与和产出有净正向影响；高价值用户更愿意玩、留存更长、花更多钱；匹配到低质量用户和团队产生负效应。

- rhetorical_function_cn：在引言中给出主要实证发现。

- depends_on_cn：实验设计。

- sets_up_cn：为机制解释和贡献声明做铺垫。

- evidence_pointer：Intro第四、五段

### 19. Introduction P6 S1

- order：19

- section：Introduction

- locator：Introduction P6 S1

- move_code：MECHANISM

- paraphrase_cn：正净效应产生是因为生产技术的超模性，而超模性主要由团队层面递增规模报酬驱动。

- rhetorical_function_cn：把结果从‘有效’提升到‘为何有效’。

- depends_on_cn：主结果。

- sets_up_cn：后续生产技术估计。

- evidence_pointer：Intro第六段首句

### 20. Introduction P6 S2-S4

- order：20

- section：Introduction

- locator：Introduction P6 S2-S4

- move_code：MECHANISM

- paraphrase_cn：社交行为、尤其消息，在reduced-form中最强，超模性也更强；基于社交评分匹配可带来全面正向效果；中介分析支持消息是中介。

- rhetorical_function_cn：提前给出社交机制的完整证据链摘要。

- depends_on_cn：主结果和生产函数。

- sets_up_cn：为机制部分提供预告。

- evidence_pointer：Intro第六段后句

### 21. Introduction P7 S1-S2

- order：21

- section：Introduction

- locator：Introduction P7 S1-S2

- move_code：CONTRIBUTION

- paraphrase_cn：贡献首先在于freemium货币化中的社交和同伴效应，其次在于数字环境中用户-群体类聚匹配。

- rhetorical_function_cn：定位理论贡献。

- depends_on_cn：主要发现。

- sets_up_cn：为结论部分反复强调。

- evidence_pointer：Intro第七段前句

### 22. Introduction P7 S3

- order：22

- section：Introduction

- locator：Introduction P7 S3

- move_code：CONTRIBUTION

- paraphrase_cn：研究还说明算法促成的类聚可加剧社交媒体极化。

- rhetorical_function_cn：把研究连接到更大社会问题。

- depends_on_cn：负向匹配结果。

- sets_up_cn：为伦理讨论做铺垫。

- evidence_pointer：Intro第七段中句

### 23. Introduction P7 S4-S6

- order：23

- section：Introduction

- locator：Introduction P7 S4-S6

- move_code：BOUNDARY_CONDITION

- paraphrase_cn：算法类聚可提高总体社区参与和利润，但对边缘用户有害，引发算法透明和伦理担忧。

- rhetorical_function_cn：明确结果的管理与伦理边界。

- depends_on_cn：正面与负面效应的并存。

- sets_up_cn：结论中扩展为公平性呼吁。

- evidence_pointer：Intro第七段末

### 24. Introduction P8

- order：24

- section：Introduction

- locator：Introduction P8

- move_code：STUDY_OVERVIEW

- paraphrase_cn：说明后续章节结构。

- rhetorical_function_cn：给读者路线图。

- depends_on_cn：全文框架。

- sets_up_cn：方便读者按序阅读。

- evidence_pointer：Intro最后一段

### 25. Section 2 P1

- order：25

- section：Related Literature

- locator：Section 2 P1

- move_code：THEORY_PROPOSITION

- paraphrase_cn：Becker证明在效用可转移且技术互补时类聚匹配是有效率的。

- rhetorical_function_cn：引入本研究的核心理论基石。

- depends_on_cn：研究问题。

- sets_up_cn：为正向类聚的合理性提供基础。

- evidence_pointer：Related Literature第一段

### 26. Section 2 P2

- order：26

- section：Related Literature

- locator：Section 2 P2

- move_code：MECHANISM

- paraphrase_cn：实验室公共品实验发现类聚匹配提高平均贡献，条件合作者因较少遇到搭便车者而维持更高贡献。

- rhetorical_function_cn：给出类聚为什么影响行为的微观机制。

- depends_on_cn：Becker理论。

- sets_up_cn：解释本文系统的行为基础。

- evidence_pointer：Related Literature第二段

### 27. Section 2 P3

- order：27

- section：Related Literature

- locator：Section 2 P3

- move_code：LIMITATION

- paraphrase_cn：数字平台上类聚匹配研究很少，例外是Hitsch等的在线约会，但那是用户-用户匹配。

- rhetorical_function_cn：指出现有文献在用户-群体和数字平台上的缺口。

- depends_on_cn：之前文献总结。

- sets_up_cn：为本文用户-群体匹配贡献定位。

- evidence_pointer：Related Literature第三段

### 28. Section 2 P3末

- order：28

- section：Related Literature

- locator：Section 2 P3末

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：Ahmadpoor和Jones提出可以将团队产出分解为个人贡献的技术，强调战略互补与超模性。

- rhetorical_function_cn：提供本文生产函数估计的直接方法基础。

- depends_on_cn：团队生产文献。

- sets_up_cn：为机制部分CES函数架桥。

- evidence_pointer：Related Literature第三段末

### 29. Section 2 P4

- order：29

- section：Related Literature

- locator：Section 2 P4

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：本文通过悄悄操纵推荐团队列表实现用户-群体匹配，保留用户自由选择并固定搜索摩擦。

- rhetorical_function_cn：说明实验操纵与现有文献的差异和优势。

- depends_on_cn：Hitsch和Carrell的搜索/内生群体问题。

- sets_up_cn：为实验设计辩护。

- evidence_pointer：Related Literature第四段

### 30. Section 2 P5-P7

- order：30

- section：Related Literature

- locator：Section 2 P5-P7

- move_code：GAP

- paraphrase_cn：freemium文献分别证明社交参与提升付费和付费提升社交，但不清楚这些效应如何同时作用形成收入、留存和货币化。

- rhetorical_function_cn：指出现有文献缺乏对多结果同时净效应的研究。

- depends_on_cn：社交/同伴效应文献。

- sets_up_cn：本文用整体系统实验填补。

- evidence_pointer：Related Literature第五至七段

### 31. Section 2 P8

- order：31

- section：Related Literature

- locator：Section 2 P8

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：CLV预测从购买历史统计模型发展到基于行为数据的ML方法，RF和XGBoost在freemium中表现良好。

- rhetorical_function_cn：为用户分类器提供技术文献依据。

- depends_on_cn：CLV文献。

- sets_up_cn：为4.2的XGBoost选择。

- evidence_pointer：Related Literature第八段

### 32. Section 3 P2

- order：32

- section：Environment

- locator：Section 3 P2

- move_code：CONTEXT

- paraphrase_cn：游戏是社交解谜/角色扮演游戏，团队协作对体验至关重要，且在畅销榜前100。

- rhetorical_function_cn：说明环境代表头部社交手机应用。

- depends_on_cn：前面文献。

- sets_up_cn：使实验结果具有代表性。

- evidence_pointer：Section 3环境描述

### 33. Section 3 P5-P6

- order：33

- section：Environment

- locator：Section 3 P5-P6

- move_code：PHENOMENON

- paraphrase_cn：用户达到资格后看到从活跃团队中随机抽取的团队列表，绝大多数依赖推荐页而非主动搜索。

- rhetorical_function_cn：描述随机匹配基线。

- depends_on_cn：环境规则。

- sets_up_cn：说明类聚系统可以在此替代随机列表。

- evidence_pointer：Section 3团队加入段落

### 34. Section 3末段

- order：34

- section：Environment

- locator：Section 3末段

- move_code：LIMITATION

- paraphrase_cn：平台不主动促进正向类聚；团队质量信息有限且搜索成本高，所以新用户选择近似随机。

- rhetorical_function_cn：指出平台现有的匹配缺陷。

- depends_on_cn：随机推荐规则。

- sets_up_cn：为匹配系统设计提供空间。

- evidence_pointer：Section 3末段

### 35. Section 4 P1

- order：35

- section：Matching System

- locator：Section 4 P1

- move_code：REQUIREMENT

- paraphrase_cn：初步分析显示环境有潜在互补性，而随机列表造成高搜索成本和低匹配价值，应该用类聚方式推荐团队。

- rhetorical_function_cn：从环境缺陷导出设计需求。

- depends_on_cn：理论互补性。

- sets_up_cn：引出系统的高-高匹配。

- evidence_pointer：Section 4首段

### 36. Section 4 P2

- order：36

- section：Matching System

- locator：Section 4 P2

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：系统只改变推荐列表，用户仍自由选择，保持自我选择与内生群体形成的感知，避免影响团队生产。

- rhetorical_function_cn：保护实验操纵的纯粹性。

- depends_on_cn：Carrell等内生群体文献。

- sets_up_cn：解释为什么制度设计保留了用户选择。

- evidence_pointer：Section 4 P2

### 37. Section 4 P3

- order：37

- section：Matching System

- locator：Section 4 P3

- move_code：DESIGN_FEATURE

- paraphrase_cn：机制分解为用户和团队两个分类问题：likely payer进high activity团队。

- rhetorical_function_cn：给出制品的骨架。

- depends_on_cn：设计需求。

- sets_up_cn：随后两小节分别描述分类器。

- evidence_pointer：Section 4 P3

### 38. Section 4.1 P1-P2

- order：38

- section：Matching System

- locator：Section 4.1 P1-P2

- move_code：DESIGN_FEATURE

- paraphrase_cn：团队分类使用产品经理经验构造的几何平均活动分，包含活跃人数、任务、礼物、消息和收入。

- rhetorical_function_cn：说明团队活动评分的构成。

- depends_on_cn：设计骨架。

- sets_up_cn：验证评分与未来收入的关系。

- evidence_pointer：Section 4.1

### 39. Section 4.1 P3

- order：39

- section：Matching System

- locator：Section 4.1 P3

- move_code：RESULT

- paraphrase_cn：验证发现top 30%团队捕获至少80%下月收入，故以30%分位为高活跃阈值。

- rhetorical_function_cn：提供团队分类的预测有效性证据。

- depends_on_cn：活动评分。

- sets_up_cn：为系统供给侧限定空位比例。

- evidence_pointer：Section 4.1验证段

### 40. Section 4.2 P1-P2

- order：40

- section：Matching System

- locator：Section 4.2 P1-P2

- move_code：REQUIREMENT

- paraphrase_cn：用户资格阶段几乎没有购买历史，类别不平衡，需要用能接受非购买数据的ML和SMOTE处理。

- rhetorical_function_cn：说明用户分类器的技术需求和选择。

- depends_on_cn：CLV文献。

- sets_up_cn：为XGBoost+SMOTE结果做铺垫。

- evidence_pointer：Section 4.2

### 41. Section 4.2 P4

- order：41

- section：Matching System

- locator：Section 4.2 P4

- move_code：RESULT

- paraphrase_cn：XGBoost在top 50%预测排名中捕获约80%实际付费者，比随机猜测好60%。

- rhetorical_function_cn：给出用户分类器的核心性能证据。

- depends_on_cn：训练和holdout评估。

- sets_up_cn：支撑用户侧可用性。

- evidence_pointer：Section 4.2末段

### 42. Section 4.3 P1-P4

- order：42

- section：Matching System

- locator：Section 4.3 P1-P4

- move_code：DESIGN_FEATURE

- paraphrase_cn：系统每日用前一天需求和空位数据设定payer阈值，夜里重训练模型，确保市场出清且适应波动。

- rhetorical_function_cn：说明算法在真实生产中的可持续实现。

- depends_on_cn：两个分类器。

- sets_up_cn：为实验的on/off设计提供实现细节。

- evidence_pointer：Section 4.3 Implementation

### 43. Section 4.3末段

- order：43

- section：Matching System

- locator：Section 4.3末段

- move_code：RESULT

- paraphrase_cn：离线PSM评估显示likely payer加入高活跃团队显著增加消息和任务参与，预计总体正向。

- rhetorical_function_cn：在生产部署前提供预期效果证据。

- depends_on_cn：历史随机匹配数据。

- sets_up_cn：支持合作方授权实验。

- evidence_pointer：Section 4.3末段

### 44. Section 5 P1

- order：44

- section：Experiment Design

- locator：Section 5 P1

- move_code：STUDY_OVERVIEW

- paraphrase_cn：采用时间式实验：系统每三天开关一次，持续六周。

- rhetorical_function_cn：描述实验设计。

- depends_on_cn：离线评估通过。

- sets_up_cn：为因果识别辩护。

- evidence_pointer：Section 5 P1

### 45. Section 5 P2

- order：45

- section：Experiment Design

- locator：Section 5 P2

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：三开三关能平衡每周事件和时间季节性；用户到达与开关独立，等价于用户级随机化，且时间分离能识别团队效应。

- rhetorical_function_cn：解释为什么采用时间式而非用户级随机。

- depends_on_cn：实验环境特点。

- sets_up_cn：说明后续因果估计的有效性。

- evidence_pointer：Section 5 P2

### 46. Section 5.1

- order：46

- section：Experiment Design

- locator：Section 5.1

- move_code：OTHER

- paraphrase_cn：列出五个结果变量：收入、消息数、周赛任务开始、周赛任务成功、14天留存。

- rhetorical_function_cn：明确结果构念和测量。

- depends_on_cn：环境中的活动单位。

- sets_up_cn：服务于后续回归解释。

- evidence_pointer：Section 5.1 Outcomes

### 47. Section 5.2 H1-H6

- order：47

- section：Experiment Design

- locator：Section 5.2 H1-H6

- move_code：HYPOTHESIS_OR_PROPOSITION

- paraphrase_cn：假设1-4认为团队质量影响新玩家，新玩家质量影响团队；假设5-6认为系统整体净效应为正。

- rhetorical_function_cn：把理论预期转成可检验命题。

- depends_on_cn：正向类聚理论。

- sets_up_cn：为用户和团队回归提供检验对象。

- evidence_pointer：Section 5.2

### 48. Section 5.2 H7

- order：48

- section：Experiment Design

- locator：Section 5.2 H7

- move_code：HYPOTHESIS_OR_PROPOSITION

- paraphrase_cn：假设7预期生产函数同时存在战略/技术互补与规模报酬。

- rhetorical_function_cn：为机制估计设定目标。

- depends_on_cn：超模性理论。

- sets_up_cn：引出6.2.1生产函数估计。

- evidence_pointer：Section 5.2 H7

### 49. Section 5.2 H8-H10

- order：49

- section：Experiment Design

- locator：Section 5.2 H8-H10

- move_code：HYPOTHESIS_OR_PROPOSITION

- paraphrase_cn：假设8-10认为社交是重要机制：高社交团队与高活跃团队效应相同、消息影响最大、消息中介其他结果。

- rhetorical_function_cn：把机制预期转化为可检验的中介命题。

- depends_on_cn：社交体验文献。

- sets_up_cn：引出6.2.2社交性分析。

- evidence_pointer：Section 5.2 H8-H10

### 50. Section 6 P1

- order：50

- section：Results

- locator：Section 6 P1

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：用户分析使用加入团队后14天结果，团队分析使用实验最后14天结果，均用对数变换。

- rhetorical_function_cn：说明估计窗口和变换。

- depends_on_cn：结果变量定义。

- sets_up_cn：明确主结果时窗。

- evidence_pointer：Section 6开头

### 51. Section 6.1.1 P1

- order：51

- section：Results

- locator：Section 6.1.1 P1

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：对用户层面，加入on/off期间的差异对用户不可知且与到达时间独立，因此可视为近似随机。

- rhetorical_function_cn：论证用户层面因果识别。

- depends_on_cn：时间式实验。

- sets_up_cn：建立回归方程的可解释性。

- evidence_pointer：Section 6.1.1 P1

### 52. Section 6.1.1 Equation (1)附近

- order：52

- section：Results

- locator：Section 6.1.1 Equation (1)附近

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：回归把SystemON、UnlikelyPayer及其交互放入模型，同时控制用户和事件固定效应，以估计不同质量用户的处理效应和平均净效应。

- rhetorical_function_cn：提供主回归的规格说明。

- depends_on_cn：识别假设。

- sets_up_cn：为表2结果做方法准备。

- evidence_pointer：Section 6.1.1方程(1)

### 53. Table 2 panel A

- order：53

- section：Results

- locator：Table 2 panel A

- move_code：RESULT

- paraphrase_cn：面板A显示likely payer在消息和任务上大幅正向；unlikely payer在消息和任务开始时负向；平均用户净效应全部显著为正，消息最强。

- rhetorical_function_cn：给出用户层面主结果。

- depends_on_cn：用户回归。

- sets_up_cn：为面板B和机制分析提供对比。

- evidence_pointer：Table 2 panel A

### 54. Table 2 panel B

- order：54

- section：Results

- locator：Table 2 panel B

- move_code：RESULT

- paraphrase_cn：面板B显示从低活跃到高活跃团队对likely payer有显著正向效应，消息29%；对unlikely payer不显著。

- rhetorical_function_cn：区分系统开启效应与团队质量效应。

- depends_on_cn：HighActivity规格。

- sets_up_cn：说明系统收益主要由高活跃团队效应驱动。

- evidence_pointer：Table 2 panel B

### 55. Section 6.1.1较长时窗段

- order：55

- section：Results

- locator：Section 6.1.1较长时窗段

- move_code：ROBUSTNESS_OR_BOUNDARY_TEST

- paraphrase_cn：15-30天窗口显示效应仍在但变小；收入与留存不再显著，消息降幅相对更明显。

- rhetorical_function_cn：检验主结果的时间持续性。

- depends_on_cn：14天主结果。

- sets_up_cn：说明社交短期效应有长期产出后果。

- evidence_pointer：Section 6.1.1末段，Tables 7-8 online appendix

### 56. Section 6.1.2 P1及Figure 1/2

- order：56

- section：Results

- locator：Section 6.1.2 P1及Figure 1/2

- move_code：RESULT

- paraphrase_cn：操纵检验显示on期几乎100% likely payer进入高活跃团队，off期则接近随机；实验进程形成高、低活跃团队的分离路径。

- rhetorical_function_cn：证明团队层面处理实施成功。

- depends_on_cn：时间式实验。

- sets_up_cn：使团队回归结果可信。

- evidence_pointer：Section 6.1.2和Figure 1/2

### 57. Section 6.1.2 Equation (2)附近

- order：57

- section：Results

- locator：Section 6.1.2 Equation (2)附近

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：团队回归用接收的payer/unlikely payer数量及与低活跃团队交互预测团队结果，并控制实验前特征。

- rhetorical_function_cn：给出团队层面识别策略。

- depends_on_cn：分离路径和数量变化。

- sets_up_cn：解释表3系数和t检验。

- evidence_pointer：Section 6.1.2方程(2)

### 58. Table 3

- order：58

- section：Results

- locator：Table 3

- move_code：RESULT

- paraphrase_cn：每个payer加入高活跃团队带来收入/消息/任务正效应；unlikely payer加入高活跃团队显著负向；净效应每新用户约+5%。

- rhetorical_function_cn：给出团队层面核心结果。

- depends_on_cn：团队回归。

- sets_up_cn：为净效应和政策含义做基础。

- evidence_pointer：Table 3

### 59. Table 3后段及Section D

- order：59

- section：Results

- locator：Table 3后段及Section D

- move_code：ROBUSTNESS_OR_BOUNDARY_TEST

- paraphrase_cn：排除实验期间新加入成员的稳健性分析显示主要效应仍存在。

- rhetorical_function_cn：证明团队效应不是仅由新成员自身产出驱动。

- depends_on_cn：团队主结果。

- sets_up_cn：支持系统对现有团队的因果解释。

- evidence_pointer：Table 3后段，Table 9 online appendix

### 60. Section 6.2.1 P1-P2

- order：60

- section：Results

- locator：Section 6.2.1 P1-P2

- move_code：MECHANISM

- paraphrase_cn：正净效应可能来自规模报酬或技术互补，需要通过CES生产函数估计区分。

- rhetorical_function_cn：引入机制分析方法。

- depends_on_cn：主结果。

- sets_up_cn：为超模性估计做理论准备。

- evidence_pointer：Section 6.2.1

### 61. Section 6.2.1 Equation (3)及Table 4

- order：61

- section：Results

- locator：Section 6.2.1 Equation (3)及Table 4

- move_code：RESULT

- paraphrase_cn：CES估计显示σ>ρ对所有产出成立，团队规模报酬递增，消息的ρ≈0.4，说明消息生产有最强的超模性。

- rhetorical_function_cn：提供生产技术层面的机制证据。

- depends_on_cn：CES模型。

- sets_up_cn：解释为什么类聚匹配有效。

- evidence_pointer：Section 6.2.1和Table 4

### 62. Section 6.2.1估计差异段

- order：62

- section：Results

- locator：Section 6.2.1估计差异段

- move_code：ROBUSTNESS_OR_BOUNDARY_TEST

- paraphrase_cn：分高/低活跃团队和实验前后估计发现，低活跃团队在收入和消息上并非稳定递增规模报酬；但除收入外超模性基本存在，消息的超模性始终最强。

- rhetorical_function_cn：检验生产函数的异质性和时间不变性。

- depends_on_cn：总体CES估计。

- sets_up_cn：提醒低质量团队可能无法从类聚中受益。

- evidence_pointer：Section 6.2.1和Tables 10-12 online appendix

### 63. Section 6.2.1重组归因段

- order：63

- section：Results

- locator：Section 6.2.1重组归因段

- move_code：MECHANISM

- paraphrase_cn：因为个人输入对同伴行为敏感度低，且切换系统不改变个人输入，净收益主要来自重组本身，而重组收益由超模技术放大。

- rhetorical_function_cn：排除‘行为改变’这一替代机制。

- depends_on_cn：附录F的peer effect和输入回归。

- sets_up_cn：把机制锁定到技术互补和重组。

- evidence_pointer：Section 6.2.1末段，Section F online appendix

### 64. Section 6.2.2 P1-P2及Table 5

- order：64

- section：Results

- locator：Section 6.2.2 P1-P2及Table 5

- move_code：RESULT

- paraphrase_cn：用社交评分代替活动评分后，高社交团队的效果与高活跃团队非常相似，消息增幅尤其是29%。

- rhetorical_function_cn：论证社交分量足以解释主效应。

- depends_on_cn：用户层面回归。

- sets_up_cn：为中介分析做铺垫。

- evidence_pointer：Section 6.2.2和Table 5

### 65. Section 6.2.2交互段

- order：65

- section：Results

- locator：Section 6.2.2交互段

- move_code：RESULT

- paraphrase_cn：社交与技术评分呈强替代：团队在技术分量上已强时，再提高社交性甚至可能降低likely payer支出。

- rhetorical_function_cn：细化机制边界。

- depends_on_cn：社交评分回归。

- sets_up_cn：说明简单高-高匹配并非越强越好。

- evidence_pointer：Section 6.2.2和Table 15 online appendix

### 66. Section 6.2.2中介分析段

- order：66

- section：Results

- locator：Section 6.2.2中介分析段

- move_code：RESULT

- paraphrase_cn：结构方程中介分析显示消息的间接效应显著，对收入和任务成功而言直接效应接近零，对任务开始直接效应不足一半。

- rhetorical_function_cn：提供社交作为中介的直接统计证据。

- depends_on_cn：SEM模型。

- sets_up_cn：支持H10。

- evidence_pointer：Section 6.2.2和Section H online appendix

### 67. Section 7 P1-P2

- order：67

- section：Conclusion

- locator：Section 7 P1-P2

- move_code：RESULT

- paraphrase_cn：总结系统、预测性能和主要效应数字。

- rhetorical_function_cn：带读者回顾完整证据。

- depends_on_cn：全文。

- sets_up_cn：进入贡献讨论。

- evidence_pointer：Section 7 P1-P2

### 68. Section 7 P3

- order：68

- section：Conclusion

- locator：Section 7 P3

- move_code：BOUNDARY_CONDITION

- paraphrase_cn：研究适用于用户协作共创价值的freemium数字产品和社交类app。

- rhetorical_function_cn：限制外推范围。

- depends_on_cn：结果。

- sets_up_cn：为管理启示和伦理讨论提供范围。

- evidence_pointer：Section 7 P3

### 69. Section 7 P4

- order：69

- section：Conclusion

- locator：Section 7 P4

- move_code：CONTRIBUTION

- paraphrase_cn：本文是首个数字环境中类聚匹配田野实验，扩展Hitsch等的用户-用户匹配到用户-群体匹配。

- rhetorical_function_cn：明确对标文献并声明贡献。

- depends_on_cn：已有文献。

- sets_up_cn：与freemium货币化贡献并列。

- evidence_pointer：Section 7 P4

### 70. Section 7 P5

- order：70

- section：Conclusion

- locator：Section 7 P5

- move_code：CONTRIBUTION

- paraphrase_cn：论文刻画freemium平台的生产技术，证明团队生产超模，因此类聚匹配能提高参与和货币化。

- rhetorical_function_cn：把机制发现转化为理论贡献。

- depends_on_cn：生产函数估计。

- sets_up_cn：支撑管理含义。

- evidence_pointer：Section 7 P5

### 71. Section 7 P6

- order：71

- section：Conclusion

- locator：Section 7 P6

- move_code：BOUNDARY_CONDITION

- paraphrase_cn：算法类聚虽然盈利，却使高、低质量团队分离，低质量团队受到进一步负面冲击，可能导致社区极化。

- rhetorical_function_cn：揭示结果的分配性边界。

- depends_on_cn：负向匹配结果。

- sets_up_cn：引出公平性讨论。

- evidence_pointer：Section 7 P6

### 72. Section 7 P7

- order：72

- section：Conclusion

- locator：Section 7 P7

- move_code：LIMITATION_AND_FUTURE

- paraphrase_cn：未来可研究最优类聚程度、长期社区凝聚力，并与利润最大化政策对比；公平性应成为ML匹配研究重点。

- rhetorical_function_cn：指出局限和未来方向。

- depends_on_cn：全文结论。

- sets_up_cn：收尾并发出社会警示。

- evidence_pointer：Section 7末段

## 写作技术

- gap_construction_cn：先承认已有文献分别证明社交提升付费和付费提升社交，然后指出‘多结果如何同时互动形成企业相关产出’并不清楚；再指出assortative matching文献在数字平台和用户-群体匹配上稀缺；两个缺口被同一套田野实验同时填补。

- signposting_cn：引言末给出路线图；每节开头用独立段总结该节目的；机制部分开始时明确‘先看直接效应，再探索机制’；假设部分先写个体/团队效应再写净效应和机制，形成递进路标。

- transition_logic_cn：从离线分类器到离线政策评估再用‘基于积极结果合作方授权部署’过渡到实验；从用户层面到团队层面用‘需要确认对现有群体的影响’连接；从主结果到生产函数用‘正净效应可能来自超模性，需要刻画技术’过渡；从生产技术到社交中介用‘消息最强提示社交是渠道’衔接。

- claim_evidence_rhythm_cn：每个主要主张后紧跟估计表或t检验，表注中明确参照组和原假设；先报告SystemON效应，再报告HighActivity效应，再用组合t检验报告平均净效应；机制部分用CES参数和中介系数回应假设。

- benchmark_narrative_cn：随机猜测和传统CLV作为分类器基准；off期随机匹配作为处理基准；低活跃团队作为高活跃团队参照；低社交团队作为高社交团队参照；最后用70/30用户比例和80%收入团队比例构造政策相关净效应检验。

- theory_return_cn：将实验净效应反推到生产技术参数，用σ>ρ证明超模性；然后发现消息的超模性最强，再返回社交媒体文献解释算法类聚可能带来极化；理论在结论中重新出现并承担规范性含义。

- contribution_positioning_cn：论文把贡献对准三个清晰目录：freemium货币化文献、assortative matching理论、社交媒体生产与消费；同时用‘首个田野实验’‘用户-群体匹配’‘外生变异’等短语建立新颖性。

- novelty_protection_cn：不仅报告总体正向结果，还展示负面效应和机制边界；用生产函数、中介分析、稳健性检验把一次性实验结果升华为可复用的设计知识和理论主张；最后通过伦理讨论防止结果被简单解读为‘算法总是好’的性能故事。

## 可复用研究与写作程序

### structure_steps

#### 1. 1

- step：1

- writing_job_cn：用现实数据和文献建立freemium社交应用的用户匹配问题，说明为什么值得研究。

- research_job_cn：选择可获得的真实平台，确认用户匹配现状（随机列表、搜索成本）。

- required_evidence_cn：环境数据显示用户留存低、社交参与重要、当前匹配近似随机。

- transition_to_next_cn：引入理论和文献，指出需要比较正负类聚方向。

#### 2. 2

- step：2

- writing_job_cn：综述assortative matching、freemium社交和CLV文献，定位缺口。

- research_job_cn：梳理可借用的理论机制与估计方法。

- required_evidence_cn：能证明用户-群体数字环境中的类聚匹配和净效应未充分研究。

- transition_to_next_cn：进入环境描述，说明为什么这个游戏适合做实验。

#### 3. 3

- step：3

- writing_job_cn：描述环境规则、团队加入流程和随机推荐基线。

- research_job_cn：采集环境结构和基线数据，说明平台未主动进行类聚匹配。

- required_evidence_cn：用户进入资格时间、随机团队列表、搜索成本高的事实。

- transition_to_next_cn：转向匹配系统设计。

#### 4. 4

- step：4

- writing_job_cn：把设计需求转成用户/团队分类器和匹配算法。

- research_job_cn：构建团队活动评分、用户CLV预测模型，做离线验证。

- required_evidence_cn：分类器有可验证的预测性能；团队top30%能捕获主要收入。

- transition_to_next_cn：通过离线政策评估证明预期效果后才部署实验。

#### 5. 5

- step：5

- writing_job_cn：设计田野实验并把处理随机化/时间化。

- research_job_cn：在真实平台部署系统，收集on/off比较数据。

- required_evidence_cn：操纵检验显示处理确实改变了匹配比例。

- transition_to_next_cn：用回归估计用户和团队层面的因果效应。

#### 6. 6

- step：6

- writing_job_cn：提出假设、展示主回归和净效应检验。

- research_job_cn：用户层和团队层分别估计，并做异质性和稳健性分析。

- required_evidence_cn：处理效应在主要结果上显著，负效应在低端出现，净效应可检验。

- transition_to_next_cn：解释为什么会有净正向效应，进入机制。

#### 7. 7

- step：7

- writing_job_cn：用生产函数和中介分析解释机制。

- research_job_cn：估计生产技术参数，检验社交作为中介。

- required_evidence_cn：超模性条件成立；中介效应显著。

- transition_to_next_cn：回到理论和贡献。

#### 8. 8

- step：8

- writing_job_cn：总结发现、边界和伦理含义，避免一次性性能故事。

- research_job_cn：把结果放到更广泛设计知识和公平性讨论中。

- required_evidence_cn：结论不超出实验能支持的边界。

- transition_to_next_cn：无下一步。

### most_transferable_moves_cn

1. 先在环境中验证‘当前是随机/低效率’再提出算法替代；

2. 用离线预测评估+离线政策评估作为田野实验的前置门槛；

3. 在实验设计部分预先辩护时间式开关为何近似随机；

4. 把主效应分成用户层和团队层，并用组合t检验构造净效应；

5. 用生产函数参数和中介分析把‘有效’转化为‘为什么有效’。

### resource_intensive_or_nonstandard_parts_cn

1. 需要真实数字平台和产品团队合作，无法在实验室/单纯数据集复制；

2. 需要每日重训练的ML基础设施和生产系统；

3. 需要六周的真实用户流量和随机开关时段；

4. 需要匿名游戏的大量用户和团队面板数据；

5. 在线附录包含PSM、CES、中介等大量统计细节，普通论文难以复制。

### what_not_to_copy_superficially_cn

1. 不能只写‘我们部署了ML匹配系统’而没有分类器离线验证和操纵检验；

2. 不能只报告总体正效应而忽略unlikely payer和低活跃团队的负效应；

3. 不能把相关中介分析直接当作因果中介叙述；

4. 不能把单个平台结果外推到所有社交媒体而不给出边界条件。

- single_best_description_of_the_routine_cn：用真实平台做因果干预，先用分类器+离线评估证明‘能识别、可能有效’，再用田野实验证明‘有效’，最后用生产函数与中介分析证明‘为何有效’，并在贡献中同时给出正向净效应与对低端用户的负面警示。

## 分析边界

全文正文完整，但多个关键的附录分析（Section A-H，Tables 7-16）只被引用，未在给定文本中提供完整细节，因此对离线PSM、生产函数异质性、交互和中介分析的核验依赖文章自身叙述；无法提供精确页码，位置证据基于章节与表编号。
