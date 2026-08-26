# Spoiled for Choice? Personalized Recommendation for Healthcare Decisions: A Multiarmed Bandit Approach

- 作者：Tongxin Zhou; Yingfei Wang; Lu (Lucy) Yan; Yong Tan
- 年份 / 期刊：2023 / Information Systems Research
- DOI：10.1287/isre.2022.1191
- 源文件：28562_2023_spoiled-for-choice-personalized-recommendation-for-healthcare-decisions-a-multiarmed-bandit-appr.md
- 论文主类型：build_evaluate_design_science
- 主导写作弧线：requirements_build_evaluate_design_principles
- 置信度：0.78

## 文章级论证概况

- 核心问题：如何为在线医疗平台设计一种能够实时适应个体动态偏好、同时按健康管理维度结构性分散推荐范围，从而提升用户持续参与的个性化干预推荐系统？

- 制品与设计：DLDE-MAB：基于Thompson sampling的上下文bandit，加入理论驱动的多样性约束；用户嵌入用wide-and-deep加增强LSTM（eLSTM）和注意力机制建模多序列健康上下文，并以健康结果作为辅助损失；干预嵌入用文本LSTM/FastText将标题与描述映射到SMART元属性。

- 客观结果：在真实减肥社区数据上，DLDE-MAB在Precision/Recall/nDCG/MAP、DR估计和模拟评估上优于多种batch、深度和bandit基准；消融显示每个设计组件有效；在偏好最动态的用户上精度相对变化更强；推荐多样性分布与真实选择的JSD最小；相对PMF有约97%的用户改进率；以体重下降为目标时平均期内体重下降率最高（top-5 72.75%，top-10 73.61%）。

- 核心贡献：作者声称贡献是一个融合深度表示学习和理论引导多样性增强bandit的医疗推荐设计科学制品，展示了prescriptive analytics与IT制品结合；并提出多序列健康上下文表示、SMART引导的干预表示和动态在线学习的设计知识。

- 整篇论证链：作者从在线健康平台中干预选择过载这一现实问题切入，指出用户缺乏评估能力导致持续参与下降；然后利用行为健康理论提炼动态在线适应的三条原则：适应不确定性、改进健康上下文表示、适应多样化健康需要。据此构建DLDE-MAB：用contextual bandit解决探索/利用，用TS处理优化；用SMART引导干预嵌入、用wide-and-deep加eLSTM和辅助损失学习用户多序列上下文，再用基于social cognitive theory的多样性约束保证推荐覆盖结果导向与行为导向维度。评估先用描述性数据确认动态和多样性，再通过benchmark、消融、动态用户集、多样性分布、用户改进率、健康结果仿真逐步证明整体有效性与每个组件贡献；最后讨论通过设计科学、方法论创新和实践含义回扣引言缺口，并给出边界与限制。

## 类型与写作弧线判定

- 论文主类型判定：文章明确遵循设计科学范式：第2节从行为健康理论提炼设计原则，第3节构建制品，第4-5节在真实数据上评价，第6节提炼设计知识与泛化边界。虽然评价依赖计算benchmark而非现场部署，但论证主线是需求/原则—构建—评价—设计知识。

- 主导写作弧线判定：作者没有从单一性能缺口直接跳到算法，而是先用理论建立动态在线适应原则，再将这些原则转化为多样性约束与深度表示组件，随后通过整体benchmark、消融和多个专项实验评价，最后在讨论中形成可复用的设计知识与边界条件。

## 研究开展程序

- study_or_phase_count：10

- 研究阶段总序列：第一阶段不产生数据，而从行为理论提炼设计原则；第二阶段把这些原则实例化为DLDE-MAB制品；第三到第四阶段收集并描述真实数据、确认动态性和多样性假设、验证嵌入的语义有效性；第五至第十阶段依次为整体benchmark、组件消融、动态用户专项、多样性分布、宏观用户改进率、健康结果扩展。每个后续实验解决前一实验留下的未回答问题，最终把局部性能优势上升为机制与设计知识。

### studies_or_phases

#### 1. 理论驱动的设计原则提炼

- order：1

- name_cn：理论驱动的设计原则提炼

- question_cn：在线医疗推荐需要满足哪些动态适应与多样性要求？

- inputs_and_setting_cn：行为健康理论文献（Johnson et al. 2002；Bandura 1991, 2004；Nahum-Shani et al. 2018；Doran 1981）和推荐系统文献

- designed_or_compared_object_cn：动态在线适应原则：适应不确定性、改进上下文表示、适应多样化健康需要

- baseline_control_or_counterfactual_cn：不适用；属于理论综合阶段

##### objective_metrics

（空）

- analysis_method_cn：文献综合与概念化

- main_result_cn：形成三条设计原则及表1中原则—缺口—组件映射

- argumentative_role_cn：把一般现实问题转成可计算的设计要求，为后续制品提供合法性

- remaining_uncertainty_cn：原则尚未落到具体算法结构，无法判断是否可实现

- link_to_next_phase_cn：第3节声称基于这些原则构建深度学习和多样性增强bandit框架

##### evidence_pointers

1. Section 2.2

2. Table 1

#### 2. DLDE-MAB制品构建

- order：2

- name_cn：DLDE-MAB制品构建

- question_cn：如何将设计原则翻译为上下文bandit、深度表示和多样性约束？

- inputs_and_setting_cn：用户属性特征、用户多序列历史、干预标题/描述、SMART元属性标注

- designed_or_compared_object_cn：DLDE-MAB框架：TS算法加多样性约束；用户嵌入wide-and-deep + eLSTM + attention + 健康结果辅助损失；干预嵌入LSTM/FastText映射SMART属性

- baseline_control_or_counterfactual_cn：算法论文中比较了完整RL、UCB、ε-greedy等方法作为方法选择参照

##### objective_metrics

（空）

- analysis_method_cn：随机优化/TS、深度神经网络、带约束的整数线性规划求解

- main_result_cn：得到完整可运行的推荐算法（Algorithm 1）和深度嵌入模型

- argumentative_role_cn：把原则实例化成可评价制品

- remaining_uncertainty_cn：尚无实证证据表明组件在真实数据上有效

- link_to_next_phase_cn：第4节引入真实数据集加以评价

##### evidence_pointers

1. Section 3

2. Algorithm 1

3. Figure 1

4. Figure 2

#### 3. 数据收集与描述性分析

- order：3

- name_cn：数据收集与描述性分析

- question_cn：真实减肥社区中用户干预偏好是否确实具有多样性和时间动态性？

- inputs_and_setting_cn：美国主要在线减肥社区2014年1月1日至4月30日数据；1,049名至少参与一次挑战的用户，165个挑战；周粒度

- designed_or_compared_object_cn：用户挑战选择类型（diet/exercise/weight loss）和相邻周选择向量重叠率

- baseline_control_or_counterfactual_cn：无干预对照

##### objective_metrics

1. 平均每周挑战数

2. 多挑战选择比例

3. 不同类型混合比例

4. 相邻选择向量重叠率0.37

- analysis_method_cn：描述性统计

- main_result_cn：用户约70%时间选择多个挑战，92%的多选时段覆盖超过两种类型，51%覆盖全部三种；重叠率0.37表明偏好动态明显

- argumentative_role_cn：为设计假设提供经验基础：多样性与动态性是真实存在的

- remaining_uncertainty_cn：描述性证据不等于推荐框架有效

- link_to_next_phase_cn：进入模型操作化和嵌入可视化，检验模型是否捕获这些模式

##### evidence_pointers

1. Section 4

2. Section 4.1

#### 4. 模型操作化与嵌入可视化验证

- order：4

- name_cn：模型操作化与嵌入可视化验证

- question_cn：深度嵌入是否有效捕获干预属性和用户健康行为序列？

- inputs_and_setting_cn：标注的挑战元属性、t-SNE投影的用户/干预嵌入

- designed_or_compared_object_cn：相同类型干预的聚集性；同强度干预的邻近性；同一用户随时间的轨迹连续性

- baseline_control_or_counterfactual_cn：无正式baseline，视觉比较

##### objective_metrics

1. t-SNE聚类形态与轨迹形态

- analysis_method_cn：t-SNE降维可视化

- main_result_cn：挑战嵌入按类型和强度聚集；用户嵌入按性别、年龄、体重变化状态聚集，同一用户轨迹连续

- argumentative_role_cn：验证表示学习的构念效度，为后续性能差异提供机制线索

- remaining_uncertainty_cn：可视化不能替代推荐性能指标

- link_to_next_phase_cn：第5节开始正式实验评价

##### evidence_pointers

1. Section 4.3

2. Figure 3

3. Figure 4

#### 5. Experiment 1：与state-of-the-art推荐系统比较

- order：5

- name_cn：Experiment 1：与state-of-the-art推荐系统比较

- question_cn：DLDE-MAB是否在整体推荐效果上优于多个batch、深度和bandit基准？

- inputs_and_setting_cn：真实数据前4周作为batch模型warm-up，评估周5-16；使用DR估计和omniscient模拟作为附加评价

- designed_or_compared_object_cn：DLDE-MAB vs CACF、SCF、PMF、CAMF、CB、hybrid_pure、hybrid_cacf、SLi-Rec、Caser、GRU4Rec、A2SVD、NextItNet、LSTUR、NPA、FAST、UCB、ε-greedy

- baseline_control_or_counterfactual_cn：所有benchmark模型；batch模型每周重训；bandit替代算法

##### objective_metrics

1. Precision@10

2. Recall@10

3. nDCG@10

4. MAP@10

5. DR@10

6. Simu@10

- analysis_method_cn：离线评估，30次运行t检验

- main_result_cn：DLDE-MAB在所有指标上最高，batch模型整体较差，且优于UCB/ε-greedy

- argumentative_role_cn：确立整体有效性并强调在线适应的重要性

- remaining_uncertainty_cn：整体领先无法说明哪个设计组件产生了贡献

- link_to_next_phase_cn：Experiment 2通过消融分解组件贡献

##### evidence_pointers

1. Section 5.1

2. Table 4

3. Online Appendix A9

#### 6. Experiment 2：模型组件消融分析

- order：6

- name_cn：Experiment 2：模型组件消融分析

- question_cn：多样性约束、用户嵌入、干预嵌入及深度结构是否各自有效？

- inputs_and_setting_cn：同一数据集，构造DLDE-MAB变体：去掉约束、去掉用户嵌入、去掉挑战嵌入、替换嵌入

- designed_or_compared_object_cn：完整模型 vs 去掉多样性约束/去掉用户嵌入/去掉挑战嵌入/不加嵌入/不加嵌入和约束；替代嵌入Collab_Filter、Tabular、BERT、FastText

- baseline_control_or_counterfactual_cn：完整DLDE-MAB为基准；各消融变体为对照

##### objective_metrics

1. Precision@10

2. Recall@10

3. nDCG@10

4. MAP@10

5. DR@10

6. Simu@10

- analysis_method_cn：消融比较

- main_result_cn：去掉多样性约束性能降约6.48%；去掉用户嵌入降约2.94%；去掉挑战嵌入降约12.16%；替代深度嵌入均不如原设计

- argumentative_role_cn：把整体性能归因到具体设计组件，支撑制品主张

- remaining_uncertainty_cn：动态偏好和多样性机制尚未直接展示

- link_to_next_phase_cn：Experiment 3和4分别考察动态适应和推荐多样性

##### evidence_pointers

1. Section 5.2

2. Table 5

3. Online Appendix A9

#### 7. Experiment 3：动态用户偏好适应

- order：7

- name_cn：Experiment 3：动态用户偏好适应

- question_cn：在偏好变化最剧烈的用户上，框架是否更能体现适应优势？

- inputs_and_setting_cn：从测试用户中按挑战嵌入方差选出30名偏好变化最大的用户

- designed_or_compared_object_cn：DLDE-MAB和各benchmark在动态用户子集上的表现，与原有全测试集结果比较

- baseline_control_or_counterfactual_cn：各模型在动态用户子集上的精度变化百分比

##### objective_metrics

1. Precision相对变化百分比

2. 附录中的评价指标

- analysis_method_cn：子集重跑，计算相对变化

- main_result_cn：DLDE-MAB在动态用户集上精度相对提升；UCB和ε-greedy表现不一；batch模型普遍下降

- argumentative_role_cn：直接展示在线学习对偏好动态的适应能力

- remaining_uncertainty_cn：仍未证明推荐组合的多样性是否匹配真实偏好结构

- link_to_next_phase_cn：Experiment 4用JSD比较推荐多样性分布

##### evidence_pointers

1. Section 5.3

2. Figure 5

3. Online Appendix A9.4

#### 8. Experiment 4：推荐多样性分布分析

- order：8

- name_cn：Experiment 4：推荐多样性分布分析

- question_cn：推荐框架是否能产生与用户真实偏好多样性一致的类型分布？

- inputs_and_setting_cn：各模型推荐类型频率分布与真实挑战选择类型频率分布

- designed_or_compared_object_cn：DLDE-MAB与各benchmark的多样性与真实分布差异

- baseline_control_or_counterfactual_cn：真实选择数据分布为参照

##### objective_metrics

1. Jensen-Shannon divergence（JSD）

- analysis_method_cn：分布相似度比较

- main_result_cn：DLDE-MAB的JSD最小（0.0456），最接近真实多样性

- argumentative_role_cn：证明多样性约束不仅存在，而且对齐用户真实需求

- remaining_uncertainty_cn：宏观分布相似不等于个体福利提高

- link_to_next_phase_cn：Experiment 5从用户层面计算改善比例

##### evidence_pointers

1. Section 5.4

2. Table 6

#### 9. Experiment 5：用户改进率宏观分析

- order：9

- name_cn：Experiment 5：用户改进率宏观分析

- question_cn：相对PMF基线，DLDE-MAB是否让更大比例用户获得更多偏好物品？

- inputs_and_setting_cn：以PMF为基线，比较各模型推荐集与用户历史选择偏好

- designed_or_compared_object_cn：各模型推荐结果；主要与PMF比较

- baseline_control_or_counterfactual_cn：PMF基线

##### objective_metrics

1. 用户改进率（获得更多偏好物品的用户百分比）

- analysis_method_cn：成对比较推荐集相对基线

- main_result_cn：DLDE-MAB用户改进率约97%，高于ε-greedy约93%、UCB约92%，远高于batch模型20%-80%

- argumentative_role_cn：把推荐性能提升翻译为平台层面的用户福利与可持续性含义

- remaining_uncertainty_cn：用户偏好物品不等于长期健康结果改善

- link_to_next_phase_cn：Experiment 6改变奖励信号，检验能否优化健康结果

##### evidence_pointers

1. Section 5.5

2. Figure 6

#### 10. Experiment 6：以健康结果为目标的反事实扩展

- order：10

- name_cn：Experiment 6：以健康结果为目标的反事实扩展

- question_cn：把推荐目标从参与率改为体重下降率后，框架是否仍能优于基准并保持灵活性？

- inputs_and_setting_cn：沿用DLDE-MAB，将奖励信号替换为期内体重下降率；使用挑战选择模拟器和体重结果模拟器生成反事实

- designed_or_compared_object_cn：DLDE-MAB与所有benchmark在体重下降奖励下的平均期内体重下降率

- baseline_control_or_counterfactual_cn：omniscient weight-loss simulator，扰动训练权重近似噪声

##### objective_metrics

1. 平均期内体重下降率（top-5和top-10）

- analysis_method_cn：反事实仿真，t检验比较

- main_result_cn：DLDE-MAB取得最高平均期内体重下降率（top-5 72.75%，top-10 73.61%）；深度batch推荐模型最差

- argumentative_role_cn：展示框架可适应不同目标函数，为政策和平台应用提供延伸

- remaining_uncertainty_cn：模拟健康结果不能替代真实因果健康结局；模型忽略干预对未来状态的影响

- link_to_next_phase_cn：引导讨论中的局限与未来RL方向

##### evidence_pointers

1. Section 5.6

2. Table 7

## 各部分修辞架构

### abstract_moves

1. CONTEXT: 在线平台提供多种健康干预项目；选择过多使个体难以决策。

2. PRACTICAL_STAKES: 选择过载可能阻碍持续健康管理参与。

3. RQ_OR_OBJECTIVE: 开发个性化医疗推荐框架帮助个体发现匹配干预。

4. DESIGN_FEATURE: 提出融合深度表示学习和理论引导多样性增强的在线学习框架。

5. STUDY_OVERVIEW: 在真实减肥社区数据上评估。

6. RESULT: 证明推荐框架及各设计组件有效；贡献于prescriptive analytics与商业智能。

### introduction_moves

1. CONTEXT: 个人健康管理重要且依赖日常自我调节。

2. PHENOMENON: 在线平台提供太多干预选项，用户因选择过载难以决策。

3. MECHANISM: 缺乏健康管理经验导致用户无法评价选项，从而不参与。

4. PRACTICAL_STAKES: 不参与会损害健康管理结果。

5. RQ_OR_OBJECTIVE: 开发个性化医疗推荐系统，提供每个时刻的干预子集以提升参与。

6. LIMITATION: 医疗推荐面临时间动态、多维度需求和复杂上下文三大挑战。

7. GAP: 这些挑战是医疗推荐任务的主要障碍。

8. DESIGN_FEATURE: 提出bandit加深表示学习加多样性约束的框架。

9. STUDY_OVERVIEW: 计划用真实数据开展系列实验。

10. CONTRIBUTION: 提出设计科学制品并给出多元贡献。

### theory_and_knowledge_moves

1. PRIOR_KNOWLEDGE: 健康管理是动态过程，受健康轨迹、经历、自我监测和社交影响。

2. LIMITATION: batch推荐假设偏好不变，会固化历史推荐模式。

3. THEORY_INTRO: MAB通过exploitation/exploration平衡适应实时反馈。

4. GAP: 已有医疗推荐算法未考虑健康上下文序列；多样性只用随机化。

5. REQUIREMENT: 动态在线适应原则包括适应不确定性、改进上下文表示、适应多样化需求。

6. MECHANISM: 健康结果作为反馈强化健康行为。

7. REQUIREMENT: 干预表示应基于SMART目标维度。

8. THEORY_INTRO: social cognitive theory的自我调节周期给出结果导向与行为导向维度。

### artifact_design_moves

1. METHOD_JUSTIFICATION: 选择contextual bandit而非完整RL，因健康序列多外生且RL数据需求高。

2. DESIGN_FEATURE: 将推荐形式化为最大化累积参与、每期推荐K个干预的约束优化。

3. DESIGN_FEATURE: 用理论驱动的多样性约束保证推荐集覆盖结果与行为维度。

4. DESIGN_FEATURE: 设计TS算法结合约束优化求解。

5. DESIGN_FEATURE: 用户嵌入采用wide-and-deep加eLSTM和注意力，并加入健康结果辅助损失。

6. DESIGN_FEATURE: 干预嵌入用LSTM/FastText将标题描述映射到SMART元属性。

### evaluation_moves

1. STUDY_OVERVIEW: 第5节预告六类实验。

2. BENCHMARK_OR_CONTRAST: 对比batch、深度序列、内容推荐和bandit基准。

3. METHOD_JUSTIFICATION: 使用Precision/Recall/nDCG/MAP、DR与omniscient simulation，处理历史日志偏差。

4. RESULT: 整体benchmark中DLDE-MAB全面领先。

5. BENCHMARK_OR_CONTRAST: 消融设计隔离多样性约束和深度表示。

6. RESULT: 每个设计组件均有效，挑战嵌入贡献最大。

7. ROBUSTNESS_OR_BOUNDARY_TEST: 动态用户集、JSD多样性、用户改进率、健康结果仿真逐层验证。

### discussion_and_contribution_moves

1. CONTRIBUTION: 将研究定位为prescriptive analytics与设计科学制品的结合。

2. CONTRIBUTION: 方法论贡献包括TS加理论多样性、eLSTM多序列建模、健康结果辅助损失。

3. CONTRIBUTION: 实践含义覆盖用户、平台与政策制定者。

4. BOUNDARY_CONDITION: 设计可泛化到其他慢性病、移动健康和医疗文档。

5. LIMITATION_AND_FUTURE: bandit忽略未来状态依赖；未来可用完整RL，但需解决状态定义和数据需求。

## 理论/知识到设计的翻译

### 知识/理论基础

1. 行为健康动态过程理论（Johnson et al. 2002）

2. 社会认知理论与自我调节（Bandura 1991, 2004）

3. 即时自适应干预（JITAI）思想（Nahum-Shani et al. 2018）

4. SMART目标设定框架（Doran 1981; Ogbeiwi 2018）

5. 目标设定理论（Locke and Latham 1990）

6. 社会支持与健康行为（King et al. 2006; Yan and Tan 2014）

7. 多臂bandit在线学习（Auer et al. 2002; Chapelle and Li 2011）

8. 深度序列推荐方法（Tang and Wang 2018; Yuan et al. 2019）

- 理论—设计耦合：partial

- 耦合判定理由：行为健康理论明确决定了两个核心设计要求（多样性维度和健康结果反馈），并直接影响用户嵌入的目标函数与干预嵌入的SMART输出；但bandit架构、eLSTM、wide-and-deep、FastText/BERT等关键实现来自机器学习和推荐系统文献，理论未完全决定这些算法细节。因此是部分耦合而非完全直接推导。

- 理论到设计翻译链：行为理论（健康管理多维、结果反馈、自我调节）→ 设计原则（适应不确定性、改进上下文表示、适应多样需求）→ 设计要求（整合静态+动态多序列、纳入健康结果、结构化多样性覆盖结果/行为维度）→ 制品选择（eLSTM+注意力用户嵌入、健康结果辅助损失、SMART干预嵌入、TS加多样性约束）→ 被检验差异（整体框架 vs 无约束/无嵌入/替代嵌入）→ 客观结果（整体benchmark领先、消融性能下降、动态用户和多样性分布改善）。

### mapping_table

#### 1. 1

- theory_or_knowledge_claim_cn：社会认知理论认为健康管理需要同时自我调节健康结果与行为常规。

- mechanism_cn：只推荐单一类型会漏掉结果管理或行为管理需求，降低持续参与。

- design_requirement_cn：推荐组合需至少覆盖结果导向维度和行为导向维度。

- artifact_choice_cn：多样性约束D（式3）；实操为每期至少一个weight loss、diet、exercise挑战。

- evaluated_contrast_cn：有约束 vs 去掉约束。

- objective_result_cn：去掉约束使Precision@10从0.5311降至0.4967，约降6.48%。

##### evidence_pointers

1. Section 3.1.2

2. Section 4.2

3. Table 5

#### 2. 2

- theory_or_knowledge_claim_cn：健康管理是动态、情境依赖的过程，由健康轨迹、干预经历、自我监测和社交环境共同塑造。

- mechanism_cn：这些多序列信号共同决定用户偏好的变化，单一静态特征无法代表健康上下文。

- design_requirement_cn：用户表示应融合静态与动态多序列特征，并处理事件不规则性。

- artifact_choice_cn：wide-and-deep + eLSTM + attention的用户嵌入；输入包括体重记录、挑战历史、称重数、好友数和帖子。

- evaluated_contrast_cn：完整模型 vs 去掉用户嵌入或替换为Collab_Filter/Tabular。

- objective_result_cn：去掉用户嵌入使Precision@10约降2.94%；替代嵌入更差。

##### evidence_pointers

1. Section 3.2.1

2. Table 5

3. Figure 4

#### 3. 3

- theory_or_knowledge_claim_cn：健康行为动机理论认为健康结果作为反馈强化健康行为。

- mechanism_cn：用户看到正向健康结果会增强对相关干预的参与动机。

- design_requirement_cn：用户表示学习中应纳入健康结果信号。

- artifact_choice_cn：辅助损失head预测体重变化，结合MSE和交叉熵。

- evaluated_contrast_cn：该组件没有单独消融，作为用户嵌入整体被检验。

- objective_result_cn：用户嵌入整体有效，但辅助损失的单独贡献未被直接分离。

##### evidence_pointers

1. Section 3.2.1

2. Equation (13)

3. Table 5

#### 4. 4

- theory_or_knowledge_claim_cn：SMART目标框架指出高质量干预目标应具有具体、可测量、可实现、相关、时限等维度。

- mechanism_cn：干预的这些元属性影响用户能否判断干预价值，进而影响选择。

- design_requirement_cn：干预表示应生成并利用这些元属性。

- artifact_choice_cn：干预嵌入网络以标题/描述为输入，输出SMART属性加motivational/self-monitoring属性。

- evaluated_contrast_cn：完整模型 vs 去掉挑战嵌入或替换为BERT/FastText。

- objective_result_cn：去掉挑战嵌入使Precision@10约降12.16%，替代嵌入较差。

##### evidence_pointers

1. Section 3.2.2

2. Table 3

3. Table 5

#### 5. 5

- theory_or_knowledge_claim_cn：JITAI思想要求把合适的干预在合适时间带给合适的人，偏好会随时间漂移。

- mechanism_cn：静态batch学习会固化历史推荐模式，无法探索新偏好。

- design_requirement_cn：推荐策略应在线学习并在探索与利用间平衡。

- artifact_choice_cn：TS-based上下文bandit加上多样性约束，每期更新后验。

- evaluated_contrast_cn：DLDE-MAB vs UCB、ε-greedy和batch模型。

- objective_result_cn：DLDE-MAB在所有指标上优于这些基准；batch模型整体较差。

##### evidence_pointers

1. Section 2.2.2

2. Section 3.1

3. Table 4

## 评价逻辑

### evaluation_modes

1. 真实历史日志的离线benchmark

2. 消融分析

3. 动态用户子集测试

4. 推荐多样性分布对比（JSD）

5. 用户改进率宏观比较

6. DR离线估计与omniscient simulation

7. t-SNE表示可视化

8. 描述性统计

- why_these_evaluations_cn：由于无法在真实平台进行随机现场干预，作者利用历史日志加离线估计来近似反事实；用整体benchmark验证制品总效果，用消融把总效果归因到组件，用动态用户集验证动态适应机制，用JSD验证多样性机制，用用户改进率把推荐收益翻译成平台福利，用健康结果仿真展示目标可迁移性。

- benchmark_and_contrast_chain_cn：先从18个batch/deep/bandit基准模型比较确立整体优势；再通过消融把整体优势分解为多样性约束、用户嵌入和干预嵌入；随后在动态用户子集上检验动态适应；再用JSD检验推荐多样性分布对齐真实偏好；再用PMF基线计算用户改进率；最后改变奖励信号为体重下降，检验框架目标灵活性。各实验逐级回答上一实验无法回答的问题。

### claim_evidence_ledger

#### 1. 1

- claim：DLDE-MAB整体优于state-of-the-art推荐系统。

- evidence：Table 4显示在Precision/Recall/nDCG/MAP/DR/Simu六个指标上均最高，且多数基准显著更差。

- status：supported

#### 2. 2

- claim：多样性约束、用户嵌入和干预嵌入各自有效。

- evidence：Table 5消融显示去掉任一组件性能下降；替代嵌入也较差。

- status：supported；但用户嵌入中辅助损失和多序列机制的单独贡献未被分离

#### 3. 3

- claim：框架能适应偏好最动态的用户。

- evidence：Experiment 3在30名最动态用户上模型精度相对提升，batch模型下降。

- status：supported

#### 4. 4

- claim：推荐多样性分布符合用户真实偏好结构。

- evidence：Table 6中DLDE-MAB的JSD最小。

- status：supported

#### 5. 5

- claim：推荐能惠及更大用户群体。

- evidence：Experiment 5中相对PMF有约97%用户改进率。

- status：partially supported；改进率基于历史选择偏好而非真实长期参与

#### 6. 6

- claim：框架可用于改善健康结果。

- evidence：Experiment 6用体重结果模拟器显示最高平均期内体重下降率。

- status：partially supported；健康结果为反事实仿真，非真实随机实验

- internal_validity_strategy_cn：使用30次重复和t检验；采用DR估计处理历史日志的选择偏差；构建omniscient simulator生成反事实用户反馈；用消融隔离组件；对batch模型设置warm-up和每周重训以尽量公平。由于没有随机现场干预，内部有效性仍弱于A/B实验。

- external_validity_strategy_cn：选择减肥社区作为个人健康管理的代表性场景；在讨论中论证设计可泛化到糖尿病、心血管等慢性病；强调深度模型可处理不同健康数据、多样性约束可替换维度；并讨论可穿戴设备和移动健康推送。但只有一个平台、一个时间窗口，未做多环境现场验证。

- what_is_not_actually_tested_cn：没有真实用户看到推荐后的参与反馈；没有现场A/B测试；健康结果来自模拟器而非真实医疗结局；辅助损失、注意力和多序列建模的单独贡献未分别消融；SMART/motivational/self-monitoring属性的人工标注可靠性正文未展开；仅一个平台和一个时间段。

## 贡献闭环

- technical_claim_cn：提出的DLDE-MAB在真实离线数据上比多种batch、深度和bandit推荐算法取得更高推荐准确率和排名质量，并且对动态偏好用户与多样性目标都表现更好。

- artifact_claim_cn：理论驱动的多样性约束、深度用户嵌入和深度干预嵌入是性能提升的可识别设计组成部分；消融实验支持每个组件的独立贡献。

- mechanism_claim_cn：在线探索/利用平衡使框架能捕捉偏好漂移；多样性约束使推荐覆盖结果与行为维度；健康结果辅助损失和多序列建模改进用户上下文表示。

- boundary_claim_cn：该设计适用于需要调节多种健康和行为维度的个人健康管理场景（如减肥、糖尿病、心血管）；干预文本可采用相同嵌入方法；但bandit假设上下文独立同分布，忽略干预对未来状态的影响。

- reusable_design_knowledge_cn：可复用知识包括：将健康理论转化为多样性维度；用eLSTM处理多条健康/行为序列；用健康结果辅助损失增强用户表示；用SMART框架指导干预表示；用TS加约束解决带多样性的在线推荐。

- theoretical_contribution_cn：拓展了prescriptive analytics与设计科学文献；将行为健康理论与推荐系统设计连接起来，提出动态在线适应三原则；为多序列健康上下文表示提供了方法学增量。

- how_discussion_closes_intro_gap_cn：讨论首段重述系统能适应动态和多样化偏好；随后把贡献定位为prescriptive analytics/design science，直接回应引言中医疗推荐三大障碍；接着通过generalizability论证设计可迁移到其他健康场景；最后用限制说明bandit的边界，避免把结果说成通用RL。

- overclaim_or_unsupported_leaps_cn：将离线benchmark和模拟结果称为用户福利与平台可持续性的含义，存在证据跳跃；用户改进率基于历史偏好而非长期参与；健康结果实验使用simulated weight loss，不能等同于真实医疗效果；动态用户只选30名，可能放大模型优势；理论贡献更多是把既有行为理论转移到推荐设计，而非提出新理论。

## 句级写作动作图谱

### 1. P1 S1

- order：1

- section：Abstract

- locator：P1 S1

- move_code：CONTEXT

- paraphrase_cn：在线医疗平台向用户提供多种干预项目，以促进个人健康。

- rhetorical_function_cn：开篇给定应用场景。

- depends_on_cn：无

- sets_up_cn：为后面的选择过载问题提供背景。

- evidence_pointer：Abstract P1 S1

### 2. P1 S2

- order：2

- section：Abstract

- locator：P1 S2

- move_code：PRACTICAL_STAKES

- paraphrase_cn：选项很多且用户缺乏经验时，人们很难决定参加哪个干预，这会影响持续参与。

- rhetorical_function_cn：将背景转化为现实后果。

- depends_on_cn：上下文：在线平台提供很多干预。

- sets_up_cn：引出推荐框架的必要性。

- evidence_pointer：Abstract P1 S2

### 3. P1 S3

- order：3

- section：Abstract

- locator：P1 S3

- move_code：RQ_OR_OBJECTIVE

- paraphrase_cn：作者的目标是开发个性化医疗推荐框架，帮助个体发现适合自己的干预。

- rhetorical_function_cn：宣布研究目标。

- depends_on_cn：前两句的问题。

- sets_up_cn：预告后面的解决方案。

- evidence_pointer：Abstract P1 S3

### 4. P1 S4

- order：4

- section：Abstract

- locator：P1 S4

- move_code：DESIGN_FEATURE

- paraphrase_cn：提出一种融合深度表示学习和理论引导多样性提升的在线学习框架。

- rhetorical_function_cn：用一句话描述核心制品。

- depends_on_cn：研究目标。

- sets_up_cn：为正文第3节做预告。

- evidence_pointer：Abstract P1 S4

### 5. P1 S5

- order：5

- section：Abstract

- locator：P1 S5

- move_code：STUDY_OVERVIEW

- paraphrase_cn：在真实世界在线减肥社区数据上评估方法。

- rhetorical_function_cn：给出研究设计类型。

- depends_on_cn：制品存在。

- sets_up_cn：暗示评价证据来自真实数据。

- evidence_pointer：Abstract P1 S5

### 6. P1 S6-S7

- order：6

- section：Abstract

- locator：P1 S6-S7

- move_code：RESULT

- paraphrase_cn：结果显示框架和每个设计组件都有效，并贡献于prescriptive analytics和商业智能研究。

- rhetorical_function_cn：报告主要结果并给出贡献定位。

- depends_on_cn：评价设计。

- sets_up_cn：为全文贡献声明定调。

- evidence_pointer：Abstract P1 S6-S7

### 7. P1 S1-S2

- order：7

- section：Introduction

- locator：P1 S1-S2

- move_code：CONTEXT

- paraphrase_cn：个人健康管理在慢病管理和疾病预防中日益重要，主要依赖个体日常自我调节。

- rhetorical_function_cn：建立健康管理的大背景。

- depends_on_cn：无

- sets_up_cn：把问题放在个人健康管理而非专业诊疗中。

- evidence_pointer：Introduction P1 S1-S2

### 8. P2 S1

- order：8

- section：Introduction

- locator：P2 S1

- move_code：PHENOMENON

- paraphrase_cn：在线平台提供大量干预选项，这可能带来选择过载，降低用户的决策表现。

- rhetorical_function_cn：引入具体经验现象。

- depends_on_cn：平台提供很多干预的背景。

- sets_up_cn：形成需求缺口。

- evidence_pointer：Introduction P2 S1

### 9. P2 S3-S4

- order：9

- section：Introduction

- locator：P2 S3-S4

- move_code：MECHANISM

- paraphrase_cn：大多数用户缺乏健康管理经验，难以评估干预选项，从而阻碍积极参与。

- rhetorical_function_cn：解释选择过载为何在医疗场景特别严重。

- depends_on_cn：选择过载现象。

- sets_up_cn：说明为什么需要推荐服务。

- evidence_pointer：Introduction P2 S3-S4

### 10. P2 S5

- order：10

- section：Introduction

- locator：P2 S5

- move_code：PRACTICAL_STAKES

- paraphrase_cn：难以决策导致用户不参加任何干预，从而损害健康管理表现。

- rhetorical_function_cn：强调不解决问题的现实后果。

- depends_on_cn：选择过载机制。

- sets_up_cn：为研究目标提供紧迫性。

- evidence_pointer：Introduction P2 S5

### 11. P3 S1-S3

- order：11

- section：Introduction

- locator：P3 S1-S3

- move_code：RQ_OR_OBJECTIVE

- paraphrase_cn：作者目标是开发个性化医疗推荐系统，为每个用户每期提供干预子集并提高参与率。

- rhetorical_function_cn：正式提出研究目标。

- depends_on_cn：前面的现实问题。

- sets_up_cn：为后续“为什么医疗推荐难”做铺垫。

- evidence_pointer：Introduction P3 S1-S3

### 12. P4 S1

- order：12

- section：Introduction

- locator：P4 S1

- move_code：LIMITATION

- paraphrase_cn：健康管理偏好具有强时间动态性，需要实时适应。

- rhetorical_function_cn：指出医疗推荐的第一大挑战。

- depends_on_cn：推荐目标。

- sets_up_cn：为选择在线学习/batch不足提供依据。

- evidence_pointer：Introduction P4 S1

### 13. P4 S3

- order：13

- section：Introduction

- locator：P4 S3

- move_code：LIMITATION

- paraphrase_cn：健康管理涉及多个结果和行为维度，理想推荐需覆盖多方面。

- rhetorical_function_cn：指出医疗推荐的第二大挑战：多样性。

- depends_on_cn：推荐目标。

- sets_up_cn：为理论驱动的多样性约束铺路。

- evidence_pointer：Introduction P4 S3

### 14. P4 S5-S6

- order：14

- section：Introduction

- locator：P4 S5-S6

- move_code：LIMITATION

- paraphrase_cn：用户健康管理上下文包含复杂序列相关和事件不规则性，以及多格式多内容数据。

- rhetorical_function_cn：指出医疗推荐第三大挑战：上下文表示。

- depends_on_cn：推荐目标。

- sets_up_cn：为深度表示学习提供理由。

- evidence_pointer：Introduction P4 S5-S6

### 15. P4 final sentence

- order：15

- section：Introduction

- locator：P4 final sentence

- move_code：GAP

- paraphrase_cn：这些挑战至今仍是医疗推荐任务的主要障碍。

- rhetorical_function_cn：把挑战明确为研究缺口。

- depends_on_cn：三大挑战。

- sets_up_cn：引出本文解决方案。

- evidence_pointer：Introduction P4 final sentence

### 16. P5 S1-S3

- order：16

- section：Introduction

- locator：P5 S1-S3

- move_code：DESIGN_FEATURE

- paraphrase_cn：采用bandit在线学习以快速适应动态偏好，并整合理论引导多样性和深度上下文表示。

- rhetorical_function_cn：给出总体技术路线。

- depends_on_cn：三大挑战。

- sets_up_cn：预告第3节的具体算法。

- evidence_pointer：Introduction P5 S1-S3

### 17. P5 S4

- order：17

- section：Introduction

- locator：P5 S4

- move_code：DESIGN_FEATURE

- paraphrase_cn：用理论驱动的多样性方案沿主要健康维度结构性地分散干预推荐。

- rhetorical_function_cn：突出与普通随机探索的区别。

- depends_on_cn：多维度需求挑战。

- sets_up_cn：为social cognitive theory应用埋下伏笔。

- evidence_pointer：Introduction P5 S4

### 18. P5 S5

- order：18

- section：Introduction

- locator：P5 S5

- move_code：DESIGN_FEATURE

- paraphrase_cn：用深度表示学习捕获静态属性和健康历史、行为路径中的复杂序列模式。

- rhetorical_function_cn：把上下文表示挑战具体到深度模型。

- depends_on_cn：复杂上下文挑战。

- sets_up_cn：为第3.2节用户/干预嵌入作预告。

- evidence_pointer：Introduction P5 S5

### 19. P6 S1

- order：19

- section：Introduction

- locator：P6 S1

- move_code：STUDY_OVERVIEW

- paraphrase_cn：通过真实数据集的一系列实验评估推荐框架。

- rhetorical_function_cn：预告评价设计。

- depends_on_cn：制品提出。

- sets_up_cn：为第4-5节评价铺路。

- evidence_pointer：Introduction P6 S1

### 20. P7 S1-S2

- order：20

- section：Introduction

- locator：P7 S1-S2

- move_code：CONTRIBUTION

- paraphrase_cn：提出医疗推荐框架，展示如何将prescriptive analytics整合进设计科学制品。

- rhetorical_function_cn：在引言末尾声明主要贡献。

- depends_on_cn：前面的问题和方案。

- sets_up_cn：为第6节详细贡献讨论留接口。

- evidence_pointer：Introduction P7 S1-S2

### 21. P4 final sentence

- order：21

- section：Section 2 intro

- locator：P4 final sentence

- move_code：REQUIREMENT

- paraphrase_cn：行为健康研究中的动态性和多样性证据促使作者在推荐设计中纳入动态和多样性考虑。

- rhetorical_function_cn：把文献证据转化为设计方向。

- depends_on_cn：前文健康行为动态与多样性的文献。

- sets_up_cn：引出2.1和2.2的设计理论。

- evidence_pointer：Section 2 intro final sentence

### 22. P2 S4

- order：22

- section：Section 2.1.1

- locator：P2 S4

- move_code：LIMITATION

- paraphrase_cn：batch推荐的基本假设是历史选择概率在推荐时不改变，因而无法捕捉动态偏好变化。

- rhetorical_function_cn：指出现有推荐技术一大缺陷。

- depends_on_cn：推荐文献概述。

- sets_up_cn：为引入MAB提供缺口。

- evidence_pointer：Section 2.1.1, paragraph on batch challenges

### 23. P3 S6

- order：23

- section：Section 2.1.1

- locator：P3 S6

- move_code：LIMITATION

- paraphrase_cn：即使频繁重训，batch模型仍强化历史推荐模式，没有机会探索更好选项。

- rhetorical_function_cn：强化batch方法的探索缺失。

- depends_on_cn：batch学习形式化。

- sets_up_cn：引出MAB的探索价值。

- evidence_pointer：Section 2.1.1, paragraph end

### 24. P4 S1

- order：24

- section：Section 2.1.1

- locator：P4 S1

- move_code：THEORY_INTRO

- paraphrase_cn：MAB通过顺序决策平衡exploitation和exploration，能适应实时反馈。

- rhetorical_function_cn：引入在线学习机制。

- depends_on_cn：batch限制。

- sets_up_cn：为bandit作为核心框架作理论准备。

- evidence_pointer：Section 2.1.1, MAB paragraph

### 25. P2 S4

- order：25

- section：Section 2.1.2

- locator：P2 S4

- move_code：GAP

- paraphrase_cn：已有医疗推荐研究较少考虑用户健康管理上下文，也没有纳入个体健康行为序列。

- rhetorical_function_cn：点明医疗推荐中的上下文表示缺口。

- depends_on_cn：医疗推荐文献。

- sets_up_cn：为深度序列表示组件提供依据。

- evidence_pointer：Section 2.1.2, healthcare recommendation gaps

### 26. P2 S5-S6

- order：26

- section：Section 2.1.2

- locator：P2 S5-S6

- move_code：GAP

- paraphrase_cn：已有多样性方法主要增加随机性，不保证覆盖主要健康管理需求。

- rhetorical_function_cn：点明多样性缺口。

- depends_on_cn：医疗推荐文献。

- sets_up_cn：为理论驱动多样性约束做铺垫。

- evidence_pointer：Section 2.1.2, diversification discussion

### 27. P1 S1

- order：27

- section：Section 2.2

- locator：P1 S1

- move_code：REQUIREMENT

- paraphrase_cn：作者提出动态在线适应原则，包括适应不确定性、适应观测到的动态、适应多样化健康需求。

- rhetorical_function_cn：把文献缺口上升为设计要求。

- depends_on_cn：文献综述。

- sets_up_cn：组织第2.2节剩余小节。

- evidence_pointer：Section 2.2 P1 S1

### 28. P1 S2-S4

- order：28

- section：Section 2.2.2

- locator：P1 S2-S4

- move_code：REQUIREMENT

- paraphrase_cn：推荐应在不确定性下通过在线学习同时利用历史数据并探索未知偏好。

- rhetorical_function_cn：解释为什么要在线学习。

- depends_on_cn：动态适应原则。

- sets_up_cn：为bandit算法提供设计依据。

- evidence_pointer：Section 2.2.2 P1 S2-S4

### 29. P1 S1

- order：29

- section：Section 2.2.3.1

- locator：P1 S1

- move_code：REQUIREMENT

- paraphrase_cn：健康管理上下文应同时整合静态用户特征和动态序列特征。

- rhetorical_function_cn：提出第一个上下文表示要求。

- depends_on_cn：动态上下文原则。

- sets_up_cn：为wide-and-deep用户嵌入铺垫。

- evidence_pointer：Section 2.2.3.1 P1 S1

### 30. P1 S5-S6

- order：30

- section：Section 2.2.3.2

- locator：P1 S5-S6

- move_code：REQUIREMENT

- paraphrase_cn：多序列健康数据应被联合处理以捕捉序列内和序列间相关及事件不规则性。

- rhetorical_function_cn：提出多序列联合建模要求。

- depends_on_cn：动态上下文原则。

- sets_up_cn：为eLSTM设计和注意力机制提供依据。

- evidence_pointer：Section 2.2.3.2 P1 S5-S6

### 31. P1 S3

- order：31

- section：Section 2.2.3.3

- locator：P1 S3

- move_code：MECHANISM

- paraphrase_cn：用户以健康结果作为反馈来强化或调整健康行为，所以参与偏好在个人口味之外还受目标健康结果驱动。

- rhetorical_function_cn：解释健康结果为什么应进入用户表示。

- depends_on_cn：行为动机理论。

- sets_up_cn：为辅助损失设计提供机制理由。

- evidence_pointer：Section 2.2.3.3 P1 S3

### 32. P2 S4

- order：32

- section：Section 2.2.3.3

- locator：P2 S4

- move_code：REQUIREMENT

- paraphrase_cn：干预目标质量可用SMART五维度评价，因此干预表示学习应以此为引导。

- rhetorical_function_cn：把干预表示学习锚定到领域知识。

- depends_on_cn：目标设定理论。

- sets_up_cn：为第3.2.2干预嵌入输出SMART属性铺垫。

- evidence_pointer：Section 2.2.3.3 P2 S4

### 33. P1 S1

- order：33

- section：Section 2.2.4

- locator：P1 S1

- move_code：THEORY_INTRO

- paraphrase_cn：社会认知理论的自我调节概念指出用户需同时管理健康结果与行为常规。

- rhetorical_function_cn：引入多样性设计的核心理论。

- depends_on_cn：动态适应原则中的多样性维度。

- sets_up_cn：为结果导向/行为导向两类维度提供理论来源。

- evidence_pointer：Section 2.2.4 P1 S1

### 34. Table 1附近的总结段

- order：34

- section：Section 2.2.5

- locator：Table 1附近的总结段

- move_code：REQUIREMENT

- paraphrase_cn：表1将设计原则、研究缺口和设计组件对应起来。

- rhetorical_function_cn：把理论到设计的映射可视化为表格。

- depends_on_cn：第2.2节各原则。

- sets_up_cn：为第3节制品实现提供蓝图。

- evidence_pointer：Section 2.2.5, Table 1

### 35. P1 S3

- order：35

- section：Section 3 intro

- locator：P1 S3

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：选择contextual bandit而非完整RL，因为RL需要大量数据和系统动态知识，而健康行为序列多外生。

- rhetorical_function_cn：为算法选择辩护。

- depends_on_cn：医疗推荐环境特点。

- sets_up_cn：限定本文建模范围。

- evidence_pointer：Section 3 intro P1 S3

### 36. P1 S1

- order：36

- section：Section 3.1.1

- locator：P1 S1

- move_code：DESIGN_FEATURE

- paraphrase_cn：把推荐问题形式化为每期给每个用户推荐K个干预，以最大化整个推荐期的累计参与。

- rhetorical_function_cn：定义目标函数。

- depends_on_cn：设计目标部分。

- sets_up_cn：为TS优化和约束设置提供数学基础。

- evidence_pointer：Section 3.1.1 P1 S1

### 37. P1 S4

- order：37

- section：Section 3.1.2

- locator：P1 S4

- move_code：DESIGN_FEATURE

- paraphrase_cn：将社会认知理论转化为结构化的多样性约束，要求推荐集中每个结果/行为维度至少有一个干预。

- rhetorical_function_cn：把理论命题变成算法约束。

- depends_on_cn：社会认知理论。

- sets_up_cn：进入TS带约束优化算法。

- evidence_pointer：Section 3.1.2, Equation (3)

### 38. Algorithm 1后说明段

- order：38

- section：Section 3.1.2

- locator：Algorithm 1后说明段

- move_code：DESIGN_FEATURE

- paraphrase_cn：TS变体先生成后验参数样本，再在多样性约束下求解整数优化，选择K个推荐并由反馈更新后验。

- rhetorical_function_cn：描述制品核心算法。

- depends_on_cn：问题形式化和多样性约束。

- sets_up_cn：为后续深度表示如何嵌入上下文做铺垫。

- evidence_pointer：Section 3.1.2, Algorithm 1

### 39. P1 S1

- order：39

- section：Section 3.2.1

- locator：P1 S1

- move_code：DESIGN_FEATURE

- paraphrase_cn：用户嵌入模型采用wide-and-deep网络，结合静态属性和动态序列特征。

- rhetorical_function_cn：提出用户表示的整体架构。

- depends_on_cn：上下文表示原则。

- sets_up_cn：为eLSTM、注意力和辅助损失作为子模块展开。

- evidence_pointer：Section 3.2.1 P1 S1

### 40. P5 S2-S4

- order：40

- section：Section 3.2.1

- locator：P5 S2-S4

- move_code：DESIGN_FEATURE

- paraphrase_cn：用增强LSTM把多条序列特征变换成元序列，并用自注意机制处理事件间隔和顺序模式。

- rhetorical_function_cn：针对多序列相关和事件不规则性设计具体模块。

- depends_on_cn：多序列联合处理原则。

- sets_up_cn：在后续t-SNE中验证用户轨迹连续。

- evidence_pointer：Section 3.2.1, eLSTM and attention description

### 41. P8 S1-S3

- order：41

- section：Section 3.2.1

- locator：P8 S1-S3

- move_code：DESIGN_FEATURE

- paraphrase_cn：加入健康结果辅助损失，既能反映健康结果对偏好的影响，也帮助主模型在有限数据下提取序列信号。

- rhetorical_function_cn：把健康结果反馈理论落实到损失函数。

- depends_on_cn：健康结果反馈机制。

- sets_up_cn：在Experiment 6中表现为对体重下降目标的适应。

- evidence_pointer：Section 3.2.1, auxiliary loss paragraph

### 42. P1 S1

- order：42

- section：Section 3.2.2

- locator：P1 S1

- move_code：DESIGN_FEATURE

- paraphrase_cn：干预嵌入模型以标题和描述为输入，用LSTM与平均token嵌入学习文本语义。

- rhetorical_function_cn：提出干预表示基础架构。

- depends_on_cn：干预文本结构。

- sets_up_cn：转入SMART元属性输出。

- evidence_pointer：Section 3.2.2 P1 S1

### 43. P2 S3

- order：43

- section：Section 3.2.2

- locator：P2 S3

- move_code：DESIGN_FEATURE

- paraphrase_cn：干预嵌入输出映射到SMART元属性以及动机和自我监测等亚属性。

- rhetorical_function_cn：把领域知识作为监督信号注入干预表示。

- depends_on_cn：SMART指标。

- sets_up_cn：为第4.2节标注和表3提供对应。

- evidence_pointer：Section 3.2.2, output attributes description

### 44. P1 S3-S5

- order：44

- section：Section 4.1

- locator：P1 S3-S5

- move_code：RESULT

- paraphrase_cn：用户平均每周约选2个挑战，约70%的周会选多个挑战；多选时92%覆盖超过两种类型，51%覆盖全部三种类型。

- rhetorical_function_cn：用描述统计证实干预偏好多样性。

- depends_on_cn：数据集收集与分类。

- sets_up_cn：支撑多样性设计的现实必要性。

- evidence_pointer：Section 4.1 P1 S3-S5

### 45. P2 final sentence

- order：45

- section：Section 4.1

- locator：P2 final sentence

- move_code：RESULT

- paraphrase_cn：相邻周选择向量重叠率平均为0.37，说明用户偏好在时间上变化明显。

- rhetorical_function_cn：用描述统计证实偏好动态性。

- depends_on_cn：选择向量操作化。

- sets_up_cn：支撑在线适应设计的现实必要性。

- evidence_pointer：Section 4.1 P2 final sentence

### 46. P3 S1-S2

- order：46

- section：Section 4.2

- locator：P3 S1-S2

- move_code：BENCHMARK_OR_CONTRAST

- paraphrase_cn：将多样性约束操作化为推荐集至少包含一个weight loss、diet、exercise挑战。

- rhetorical_function_cn：把理论维度落到具体实验变量。

- depends_on_cn：理论多样性维度。

- sets_up_cn：让消融测试可以比较有约束和无约束。

- evidence_pointer：Section 4.2 P3 S1-S2

### 47. P1-P2 总结段

- order：47

- section：Section 4.3

- locator：P1-P2 总结段

- move_code：RESULT

- paraphrase_cn：t-SNE显示干预嵌入按类型和强度聚类，用户嵌入按性别、年龄和体重变化状态聚类且同一用户轨迹连续。

- rhetorical_function_cn：提供表示质量的构念效度证据。

- depends_on_cn：用户与干预嵌入模型。

- sets_up_cn：为后续性能差异提供机制解释。

- evidence_pointer：Section 4.3, Figures 3 and 4

### 48. P1 S1

- order：48

- section：Section 5.1

- locator：P1 S1

- move_code：BENCHMARK_OR_CONTRAST

- paraphrase_cn：为了证明整体有效性，与多种batch、深度序列、内容推荐和bandit算法比较。

- rhetorical_function_cn：为第一个实验建立对照。

- depends_on_cn：制品构建完成。

- sets_up_cn：给出表4的结果。

- evidence_pointer：Section 5.1 P1 S1

### 49. P3 S1-S4

- order：49

- section：Section 5.1

- locator：P3 S1-S4

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：除常规指标外，使用DR估计处理离线数据选择偏差，并用omniscient simulation生成反事实反馈。

- rhetorical_function_cn：为离线评价的因果性辩护。

- depends_on_cn：历史日志只能观测被选择动作的奖励。

- sets_up_cn：增强后续结果的可信度。

- evidence_pointer：Section 5.1, evaluation methods paragraph

### 50. P4 S1-S4

- order：50

- section：Section 5.1

- locator：P4 S1-S4

- move_code：RESULT

- paraphrase_cn：DLDE-MAB在全部指标上最高；batch模型整体较差，且优于UCB和ε-greedy。

- rhetorical_function_cn：报告整体benchmark结果。

- depends_on_cn：基准模型表。

- sets_up_cn：提出需要消融解释为什么领先。

- evidence_pointer：Section 5.1, Table 4

### 51. P1 S1

- order：51

- section：Section 5.2

- locator：P1 S1

- move_code：BENCHMARK_OR_CONTRAST

- paraphrase_cn：通过消融，逐一关闭或替换设计组件，检验每个组件贡献。

- rhetorical_function_cn：把整体性能分解为组件效应。

- depends_on_cn：整体benchmark结果。

- sets_up_cn：给出表5消融结果。

- evidence_pointer：Section 5.2 P1 S1

### 52. P2 S2-S4

- order：52

- section：Section 5.2

- locator：P2 S2-S4

- move_code：RESULT

- paraphrase_cn：去掉多样性约束约降6.48%，去掉用户嵌入约降2.94%，去掉挑战嵌入约降12.16%，替换嵌入也普遍更差。

- rhetorical_function_cn：定量报告每个组件的必要性。

- depends_on_cn：消融设计。

- sets_up_cn：支撑制品主张和理论到设计映射。

- evidence_pointer：Section 5.2, Table 5

### 53. P2 结果段

- order：53

- section：Section 5.3

- locator：P2 结果段

- move_code：RESULT

- paraphrase_cn：在偏好变化最大的30名用户上，DLDE-MAB精度相对提升，UCB和ε-greedy表现不稳定，batch模型普遍下降。

- rhetorical_function_cn：展示模型对动态偏好的适应优势。

- depends_on_cn：动态用户子集选择。

- sets_up_cn：与多样性分布实验一起支持机制主张。

- evidence_pointer：Section 5.3, Figure 5

### 54. P1 结果段

- order：54

- section：Section 5.4

- locator：P1 结果段

- move_code：RESULT

- paraphrase_cn：DLDE-MAB推荐类型分布的JSD最小，说明与真实选择多样性最接近。

- rhetorical_function_cn：验证多样性约束产生的分布是否匹配真实需求。

- depends_on_cn：多样性约束。

- sets_up_cn：把性能优势延伸到结构与机制层面。

- evidence_pointer：Section 5.4, Table 6

### 55. P1 结果段

- order：55

- section：Section 5.5

- locator：P1 结果段

- move_code：RESULT

- paraphrase_cn：相对PMF，DLDE-MAB约97%的用户获得更多偏好物品，高于UCB和ε-greedy，更远高于batch模型。

- rhetorical_function_cn：把推荐效果转化为用户层面福利。

- depends_on_cn：PMF基线设定。

- sets_up_cn：为平台可持续性含义提供依据。

- evidence_pointer：Section 5.5, Figure 6

### 56. P2 结果段

- order：56

- section：Section 5.6

- locator：P2 结果段

- move_code：ROBUSTNESS_OR_BOUNDARY_TEST

- paraphrase_cn：将奖励改为体重下降后，DLDE-MAB仍取得最高平均期内体重下降率，而依赖选择历史的深度batch模型最差。

- rhetorical_function_cn：展示同一框架可适配不同目标，也测试健康结果导向的边界。

- depends_on_cn：反事实体重结果模拟器。

- sets_up_cn：为讨论中灵活性和局限提供证据。

- evidence_pointer：Section 5.6, Table 7

### 57. P1-P2

- order：57

- section：Section 6

- locator：P1-P2

- move_code：CONTRIBUTION

- paraphrase_cn：作者总结推荐系统有效，并将贡献定位为prescriptive analytics与设计科学制品的结合。

- rhetorical_function_cn：把实验结果升维到学科贡献。

- depends_on_cn：全部实验。

- sets_up_cn：引出方法论与实践含义。

- evidence_pointer：Section 6 P1-P2

### 58. P1 S1

- order：58

- section：Section 6.1

- locator：P1 S1

- move_code：BOUNDARY_CONDITION

- paraphrase_cn：该设计是通用的，可应用于其他需要类似健康和行为维度的慢病管理场景。

- rhetorical_function_cn：限定并扩展适用范围。

- depends_on_cn：设计组件与具体维度解耦。

- sets_up_cn：防止贡献退化为单一数据集的一次性结果。

- evidence_pointer：Section 6.1 P1 S1

### 59. P1 S4-S6

- order：59

- section：Section 6.2

- locator：P1 S4-S6

- move_code：LIMITATION_AND_FUTURE

- paraphrase_cn：bandit模型假设上下文独立同分布，忽略干预对用户未来状态的影响；完整RL是严格推广但需要大量数据和状态定义。

- rhetorical_function_cn：承认模型边界并给出未来方向。

- depends_on_cn：对健康动态的讨论。

- sets_up_cn：为后续研究留下接口，同时保护当前贡献不被误认为全RL解。

- evidence_pointer：Section 6.2 P1 S4-S6

## 写作技术

- gap_construction_cn：先铺陈个人健康管理的现实重要性，然后用选择过载与用户低参与建立实践后果；接着指出医疗推荐不是e-commerce推荐的简单迁移，存在动态、多样、复杂上下文三大障碍；再通过文献综述指出batch推荐静态且无探索、已有医疗推荐缺乏健康上下文和理论引导多样性，从而形成三层缺口。

- signposting_cn：引言最后预告贡献；第2节开头说明先综述后给设计理论；第3节开头声明基于设计原则构建框架；第5节开头列出六个实验；每个实验段都先交代目的再给结果，读者始终知道当前论证位置。

- transition_logic_cn：从整体benchmark到消隐实验用“整体领先应由组件解释”过渡；从消融到动态用户实验用“是否适应动态”过渡；从动态到多样性用“是否匹配真实多样性”过渡；从多样性到用户改进用“用户层面是否更好”过渡；从用户改进到健康结果用“目标能否迁移”过渡。

- claim_evidence_rhythm_cn：每个设计主张后面紧跟对应实验表格或图：整体有效性用表4，组件有效用表5，动态适应用图5，多样性用表6，用户改进用图6，健康结果用表7。结果报告中先用数字，再给解释，再回扣机制。

- benchmark_narrative_cn：benchmark不是简单罗列，而是按论证需要分组：batch模型用于证明静态不足，深度推荐用于证明需序列建模但缺健康上下文，UCB/ε-greedy用于证明TS和多样性约束的价值；DR和omniscient simulation用于回应历史日志偏误，使benchmark更可信。

- theory_return_cn：结果没有停在指标上，而是在讨论中把性能优势重新解释为动态在线适应三原则的实例化；把用户嵌入和干预嵌入的消融结果映射回Johnson、Bandura和SMART理论，使局部实验成为设计知识。

- contribution_positioning_cn：不把贡献写成“我们建了一个更好算法”，而是写成设计科学制品加方法论创新：TS加理论多样性、eLSTM多序列建模、健康结果辅助损失；再面向用户、平台、政策三类利益相关者给出实践含义。

- novelty_protection_cn：通过消融证明不是整体式黑箱提升；通过动态用户和JSD证明优势有明确机制来源；通过健康目标实验证明框架可迁移而非一次性性能结果；最后用generalizability和limitations划定边界，防止被解读为过宽主张。

## 可复用研究与写作程序

### structure_steps

#### 1. 1

- step：1

- writing_job_cn：用一个具体现实问题开场，说明若不解决会有哪些实践后果。

- research_job_cn：收集在线健康平台选择过载、参与率低等现象证据和相关文献。

- required_evidence_cn：至少引入官方报告、既有实证研究或平台数据统计，证明问题真实存在。

- transition_to_next_cn：“因此我们开发推荐系统”引入研究目标。

#### 2. 2

- step：2

- writing_job_cn：把一般问题收缩为可研究的技术挑战，并总结现有研究的不足。

- research_job_cn：对比batch推荐与在线MAB，突出医疗场景的动态性、多样性和复杂上下文。

- required_evidence_cn：文献中的限制必须有具体机制，而非“缺乏研究”。

- transition_to_next_cn：“我们提出动态在线适应原则”进入设计理论。

#### 3. 3

- step：3

- writing_job_cn：从行为理论或领域知识提炼设计原则，用表格映射原则—缺口—组件。

- research_job_cn：找到能真正约束设计选择的理论，而不是事后贴标签。

- required_evidence_cn：必须能说明每个理论命题如何变成一种设计要求。

- transition_to_next_cn：“基于这些原则，我们构建框架”进入制品。

#### 4. 4

- step：4

- writing_job_cn：清晰描述制品：问题形式化、算法、网络结构、损失函数和约束。

- research_job_cn：实现算法并把每个设计原则落到可执行模块。

- required_evidence_cn：必须有可复现的算法或伪代码，以及可解释的组件。

- transition_to_next_cn：“我们在真实数据上评价”进入实证。

#### 5. 5

- step：5

- writing_job_cn：先用描述性数据验证设计假设，再用benchmark和消融提供整体与组件证据。

- research_job_cn：选择合适数据集，构造基准和消融，使用稳健离线评估。

- required_evidence_cn：整体benchmark要有多指标和统计检验；消融要能分离组件贡献。

- transition_to_next_cn：“为了深入验证机制，我们进行专项实验”进入机制验证。

#### 6. 6

- step：6

- writing_job_cn：用专项实验展示机制边界，再在讨论中回扣理论和贡献。

- research_job_cn：检验动态用户、多样性分布、用户福利、目标迁移等。

- required_evidence_cn：专项实验必须回答上一实验留下的不确定性。

- transition_to_next_cn：“局限与未来”把边界说清楚，防止过度声称。

### most_transferable_moves_cn

1. 把现实问题转化为多个具体技术挑战的结构化方法

2. 用设计原则表把理论、缺口和组件对应起来

3. 整体benchmark后紧跟消隐，防止黑箱式贡献

4. 用专项实验逐一验证机制，而非只报告平均性能

5. 用DR和模拟器等离线性评估增强可信度

6. 在讨论中显式泛化并给定边界

### resource_intensive_or_nonstandard_parts_cn

1. 真实在线健康社区用户日志与干预文本数据

2. 对干预目标进行人工SMART属性标注

3. 复杂深度模型训练（eLSTM、attention、BERT/FastText）

4. DR估计与omniscient simulation的设计和实现

5. 多轮benchmark与消融的算力和时间成本

6. 需要行为健康理论深度参与设计而非事后解释

### what_not_to_copy_superficially_cn

1. 不能只创建“多样性约束”而不用领域理论确定维度

2. 不能只堆LSTM/注意力而不说明这些组件对应哪些健康机制

3. 不能把模拟健康结果写成真实健康改善

4. 不能只报告整体指标而不做消融，否则组件贡献无法归因

5. 不能忽略bandit与RL的边界，否则贡献会被过度解释

6. 不能在没有真实用户反馈的情况下声称平台福利得到改善

- single_best_description_of_the_routine_cn：从现实健康选择困境出发，用行为理论提炼设计原则，再把这些原则编码成深度bandit制品，再用真实数据和消融实验逐项证明每个设计选择，最后回到设计科学与实践含义。

## 分析边界

OCR将部分公式和图表转为图片/占位符；表4-7和算法主体可读，但Online Appendix A1-A9未提供，无法核验DR估计、omniscient simulation、超参数和人工标注细节；全文无页码，只能以章节和段落标识位置；图1-6部分未在文本中完全复现。
