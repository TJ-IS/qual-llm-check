# Finding a Needle in the Haystack: 
Recommending Online Communities on Social Media Platforms Using Network and Design Science

- 作者：Srikar Velichety; Sudha Ram
- 年份 / 期刊：2021 / Journal of the Association for Information Systems
- DOI：10.17705/1jais.00694
- 源文件：14346_2021_finding-a-needle-in-the-haystack-recommending-online-communities-on-social-media-platforms-using.md
- 论文主类型：build_evaluate_design_science
- 主导写作弧线：problem_theory_design_test_return
- 置信度：0.76

## 文章级论证概况

- 核心问题：如何在社交媒体平台上为在线社区（以Twitter列表为背景）生成高质量的订阅推荐，尤其是如何利用用户与社区之间及不同用户之间形成的关系网络和社区一般统计特征来提高推荐质量？

- 制品与设计：一个基于设计科学和网络科学的方法（方法+特征提取过程）：构造三类网络（列表-列表、用户-用户、列表-用户）用于订阅与成员关系；提取网络特征（有向同配性、结构洞、中介/接近/特征向量中心性、局部聚类系数排名LCCR），提取一般社区特征（成员规模和订阅规模、重叠度），以内容主题特征作为基线；用神经网络模型融合三类特征并生成订阅推荐。

- 客观结果：在34,000个列表、1,600位策展人、6个月数据上，网络特征在首位推荐上优于一般特征与内容特征；网络+一般特征在首位推荐最优；三类特征联合在top-5/top-10最优；全文方法在多数指标上优于五个经典推荐算法以及List PageRank、CSD、BGEGM等最新方法；特征重要性和Shapley值显示网络/一般特征比纯内容特征贡献更大。

- 核心贡献：作者声称提出并验证了一个基于设计科学的大规模网络+一般社区特征+内容特征的社区订阅推荐方法，贡献了新网络特征（structural hole assortativity、LCCR）及其高效算法，扩展了设计科学中利用大数据进行预测/描述的框架，并为在Twitter及其他平台定制社区推荐提供了设计知识。

- 整篇论证链：作者先把在线社区订阅推荐界定为由于用户注意力稀缺和传统内容特征不足造成的实际问题，指出已有推荐方法主要依赖内容或简单用户关系，忽略社区和用户嵌入的关系网络结构。随后引入网络科学中的同配性、结构洞、连通性、小世界网络和随机游走等知识，把三类用户/社区关系网络转化为可计算的网络特征；同时从大规模数据探索中提出社区规模与重叠等一般特征，并以推文主题内容特征作为基线。通过在6个月Twitter列表数据集上构建神经网络推荐模型，作者系统比较单一特征、两两组合、三类组合以及若干baseline，证明网络特征在首位推荐和与一般特征组合时显著提升推荐质量，三类组合在top-5/top-10全面最优。最后作者将结果重新连接到设计科学框架，主张可复用的网络特征提取方法和对其他平台的可定制性，从而完成从问题、理论、设计、评价到设计知识的闭环。

## 类型与写作弧线判定

- 论文主类型判定：文章明确使用Peffers等的设计科学研究框架，将研究过程映射到问题识别、目标定义、设计开发、演示、评价与沟通等阶段；核心制品是结合网络与一般社区分析的特征提取方法与推荐模型；评价通过历史数据上的离线实验、baseline对比和解释性分析完成，不是纯计算benchmark或正式理论检验。因此属于构建-评价设计科学。

- 主导写作弧线判定：章节从现实问题与研究缺口出发，引入网络科学理论并将理论命题转译为网络/结构特征设计，随后用Twitter数据集构建和评估推荐模型，最后在结论部分回到设计科学理论贡献与可复用设计知识。整体符合“问题-理论-设计-检验-回到理论”的写作弧线。

## 研究开展程序

- study_or_phase_count：9

- 研究阶段总序列：数据采集与描述 → 识别并构建三类关系网络 → 同配性与结构洞分析 → 共同订阅/成员网络的LCCR特征设计 → 两模网络位置中心性分析 → 一般社区特征（规模与重叠）→ 内容主题基线提取 → 神经网络推荐模型与组合评价 → 稳健性/可解释性/外部baseline补充。前一阶段为后一阶段提供实体、网络、特征或比较基础，论证层层递进：先建立数据与网络对象，再从网络结构中提炼特征，再把三类特征放进统一模型比较，最后用可解释性和外部基线保护贡献。

### studies_or_phases

#### 1. 数据采集与描述

- order：1

- name_cn：数据采集与描述

- question_cn：需要什么样的Twitter列表数据来构建社区订阅推荐？

- inputs_and_setting_cn：Listorious随机列表，按NYT新闻分类关键词；1600位策展人；2014年9月至2015年2月共6个月；采集列表、成员、订阅者、关注关系和推文。

- designed_or_compared_object_cn：初始数据集与清洗流程

- baseline_control_or_counterfactual_cn：无

##### objective_metrics

1. 列表数

2. 成员数

3. 订阅数

4. 推文数

- analysis_method_cn：Python Tweepy模块、Twitter REST API、数据清洗（过滤停用用户和非英文推文）

- main_result_cn：共采集34,812个列表、1,656,991名成员、5,949,336条关注关系、19,115次订阅和506,700条推文。

- argumentative_role_cn：为后续所有网络构建和特征提取提供基础数据。

- remaining_uncertainty_cn：数据来自2014-15年且受限于Twitter API速率，无法代表全平台。

- link_to_next_phase_cn：基于这些实体，识别用户和列表之间可以构成哪些网络。

##### evidence_pointers

1. Table 1

2. Table 2

3. Section 4

#### 2. 网络构建与类型识别

- order：2

- name_cn：网络构建与类型识别

- question_cn：用户和社区之间存在哪些关系网络？

- inputs_and_setting_cn：用户（curators/members/subscribers）与列表（订阅/成员）的隶属关系。

- designed_or_compared_object_cn：三类网络：list-list、user-user、list-user；并区分membership与subscription两种关系。

- baseline_control_or_counterfactual_cn：无

##### objective_metrics

（空）

- analysis_method_cn：两模网络与单模网络建模；用策展人最大的列表作为其兴趣代表。

- main_result_cn：形成六个可能的网络组合，为特征提取提供输入。

- argumentative_role_cn：将研究问题转化为可计算网络对象。

- remaining_uncertainty_cn：用最大列表代表用户兴趣可能有损，多列表兴趣通过两模网络覆盖。

- link_to_next_phase_cn：分别分析这些网络以提取网络特征。

##### evidence_pointers

1. Section 5.1

2. Table 3

3. Figures 4-6

#### 3. 同配性与结构洞分析（用户订阅偏好量化）

- order：3

- name_cn：同配性与结构洞分析（用户订阅偏好量化）

- question_cn：用户偏好如何受网络同配结构影响？

- inputs_and_setting_cn：list-list订阅/成员网络，以及100个同度分布随机网络用于z-score检验。

- designed_or_compared_object_cn：四类有向同配性：degree、structural holes、betweenness centrality、closeness centrality。

- baseline_control_or_counterfactual_cn：同度分布的随机网络

##### objective_metrics

1. 同配性

2. ASP

3. Z-score

- analysis_method_cn：有向同配性计算、随机网络显著性检验

- main_result_cn：结构洞四个成分显著影响订阅；closeness centralities的in-in与out-in显著；betweenness不显著。

- argumentative_role_cn：说明列表周围网络结构能预测订阅，支持网络特征设计。

- remaining_uncertainty_cn：单靠同配性不能解释共同订阅模式。

- link_to_next_phase_cn：需要分析共同订阅网络。

##### evidence_pointers

1. Tables 4-5

2. Section 5.1.1

#### 4. 共同订阅/成员网络的LCCR特征设计

- order：4

- name_cn：共同订阅/成员网络的LCCR特征设计

- question_cn：共同订阅的聚类结构及其时间演化如何量化？

- inputs_and_setting_cn：user-user订阅/成员网络，top-k和bottom-k边，六个月LCC值。

- designed_or_compared_object_cn：LCCR指标及其递归算法。

- baseline_control_or_counterfactual_cn：无

##### objective_metrics

1. LCC

2. 聚类数

3. LCC演化向量

4. 收敛迭代数

- analysis_method_cn：top-k分析、聚类、LCC演化向量、类似PageRank的递归计算

- main_result_cn：发现低/中/高三个LCC簇；LCC随时间交替增减；top-k大的边更稳定；定义LCCR并在30次迭代内收敛。

- argumentative_role_cn：提供量化用户兴趣多样性与演化的核心网络特征。

- remaining_uncertainty_cn：k的选择与聚类质量采用启发式评价；尚未与其他baseline对比。

- link_to_next_phase_cn：还需位置特征，故进行中心性分析。

##### evidence_pointers

1. Section 5.1.2

2. Formulas 2-4

3. Figure 7

#### 5. 位置特征与两模网络中心性

- order：5

- name_cn：位置特征与两模网络中心性

- question_cn：列表在整体网络中的位置是否影响订阅？

- inputs_and_setting_cn：list-user订阅/成员两模网络。

- designed_or_compared_object_cn：betweenness、closeness、eigenvector centrality与成员/订阅计数的相关。

- baseline_control_or_counterfactual_cn：无

##### objective_metrics

1. 相关系数

- analysis_method_cn：相关分析

- main_result_cn：订阅计数与betweenness相关较强（0.381）；成员计数与closeness相关较强（0.451）；eigenvector弱。

- argumentative_role_cn：支持将列表中心性纳入网络特征矩阵。

- remaining_uncertainty_cn：只测相关性，未做因果或预测贡献分离。

- link_to_next_phase_cn：与前面的网络特征共同形成NC_U和NC_L矩阵。

##### evidence_pointers

1. Table 6

2. Formula 5

#### 6. 一般社区特征：规模与重叠

- order：6

- name_cn：一般社区特征：规模与重叠

- question_cn：社区规模和重叠度能否帮助推荐订阅？

- inputs_and_setting_cn：列表成员和订阅者数量、curated/subscribed列表集合。

- designed_or_compared_object_cn：平均成员规模、平均订阅规模、成员重叠、订阅重叠。

- baseline_control_or_counterfactual_cn：无

##### objective_metrics

1. 均值

2. 标准差

3. 时间稳定性

- analysis_method_cn：描述性统计与纵向分析

- main_result_cn：列表规模分布存在异质性；重叠均值接近0但用户间差异明显；随时间稳定。

- argumentative_role_cn：为推荐模型补充非网络的一般特征。

- remaining_uncertainty_cn：没有说明这些特征单独推荐效果的好坏。

- link_to_next_phase_cn：需与网络、内容特征比较。

##### evidence_pointers

1. Section 5.2-5.4

2. Formulas 6-7

#### 7. 内容基线特征提取

- order：7

- name_cn：内容基线特征提取

- question_cn：如何从内容维度得到基线推荐特征？

- inputs_and_setting_cn：策展人推文与列表推文。

- designed_or_compared_object_cn：DDTM动态主题模型10个话题。

- baseline_control_or_counterfactual_cn：作为baseline的textual特征

##### objective_metrics

1. 话题分布

- analysis_method_cn：DDTM动态主题模型

- main_result_cn：每个用户与列表获得十维话题向量，乘法形成内容偏好矩阵。

- argumentative_role_cn：提供已有文献最常用的baseline，使比较有对照。

- remaining_uncertainty_cn：LDA短文本效果差，故用DDTM；内容基线不代表全部内容推荐法。

- link_to_next_phase_cn：三类特征进入同一模型框架比较。

##### evidence_pointers

1. Section 5.5-5.7

2. Formula 8

#### 8. 模型训练与评价

- order：8

- name_cn：模型训练与评价

- question_cn：网络、一般和内容特征单独及组合时，推荐质量如何？

- inputs_and_setting_cn：特征矩阵、六个月的订阅记录。

- designed_or_compared_object_cn：神经网络推荐模型 P(c,l)=αΔ+βμ+γΩ。

- baseline_control_or_counterfactual_cn：Textual only、General only、Network only、所有两两组合、三者组合；五个经典推荐算法；三个现有社区推荐方法。

##### objective_metrics

1. Precision@1/5/10

2. Recall@1/5/10

3. F-score@1/5/10

4. MRR

5. DCG

6. Overall accuracy

- analysis_method_cn：10折交叉验证、SMOTE、bootstrap标准误、神经网络、超参优化

- main_result_cn：Network top1 precision 0.8 vs Textual 0.7；Network+General top1 0.97；All features top5 0.94、top10 0.97；超越baseline与现有方法。

- argumentative_role_cn：直接检验三类特征对推荐质量的作用并比较组合效果。

- remaining_uncertainty_cn：只在一个平台的数据上离线评价；总体准确率下降因多数样本为负样本。

- link_to_next_phase_cn：需要解释特征贡献并检验稳健性。

##### evidence_pointers

1. Section 6.1-6.3

2. Table 7

3. Figure 8

#### 9. 稳健性、可解释性与基线对比补充

- order：9

- name_cn：稳健性、可解释性与基线对比补充

- question_cn：结果是否稳健、特征贡献是否真实、是否优于最新方法？

- inputs_and_setting_cn：同一数据集上的特征重要性/Shapley值，baseline结果。

- designed_or_compared_object_cn：特征排列重要性与Shapley值分析；与已有方法比较。

- baseline_control_or_counterfactual_cn：textual-only模型的特征贡献，以及state-of-art和现有方法。

##### objective_metrics

1. 分类错误率降低

2. Shapley值

3. 推荐指标

- analysis_method_cn：permutation importance、Shapley、汇总比较

- main_result_cn：网络+一般特征平均贡献高于内容；Textual+Network出现维度诅咒；全部方法优于现有baseline。

- argumentative_role_cn：保护核心贡献不被视为特征工程偶然事件并提供可解释性。

- remaining_uncertainty_cn：可解释性指标只解释模型内部，不替代行为实验。

- link_to_next_phase_cn：进入结论与设计知识归纳。

##### evidence_pointers

1. Section 6.3解释段

2. Appendix B

## 各部分修辞架构

### abstract_moves

1. CONTEXT: 指出在线社区推荐问题

2. METHOD: 基于网络科学与设计科学构建方法

3. RESULT: 网络特征和组合特征在推荐中的性能

4. CONTRIBUTION: 对在线社区推荐器设计的意义

### introduction_moves

1. CONTEXT: 定义在线社区与平台上的lists/groups/boards

2. PHENOMENON: Twitter列表比推文内容更代表兴趣，Pinterest boards改进搜索

3. PRACTICAL_STAKES: 社区可帮助广告主定位受众、减少无效投放

4. LIMITATION: 已有研究集中于内容和交互，忽略结构关系

5. GAP: 用户与社区及不同类型用户之间形成的关系网络未被用于推荐

6. WHY_GAP_MATTERS: 用户注意力稀缺，社区规模/重叠能帮助筛选

7. RQ_OR_OBJECTIVE: 提出三个研究问题

8. THEORY_INTRO: 引入网络科学中的small-world、weak ties、random surfer、connectivity

9. STUDY_OVERVIEW: 预告网络特征、一般特征、组合实验和baseline比较

10. ROBUSTNESS_OR_BOUNDARY_TEST: 声明处理数据泄漏并保证结果稳定

11. CONTRIBUTION: 提出可定制到其他平台的设计科学框架

### theory_and_knowledge_moves

1. THEORY_PROPOSITION: 用户和社区的隶属关系网络可量化订阅偏好

2. MECHANISM: 同配性、结构洞、共同订阅聚类和中心性影响用户订阅

3. REQUIREMENT: 需要将网络科学概念转变成可计算特征

4. THEORY_INTRO: 在文献综述中引用Newman、Burt、Freeman、Watts/Strogatz、Page等

5. MECHANISM: LCCR将随机surfer行为与共同订阅聚类结合

6. BENCHMARK_OR_CONTRAST: 以内容主题作为基线

### artifact_design_moves

1. DESIGN_FEATURE: 构造list-list、user-user、list-user三类网络

2. DESIGN_FEATURE: 定义有向同配性、结构洞、LCCR和中心性特征

3. DESIGN_FEATURE: 定义一般社区特征矩阵GC_C/GC_L

4. BENCHMARK_OR_CONTRAST: 用DDTM构造内容特征矩阵作为基线

5. METHOD_JUSTIFICATION: 用神经网络融合异质特征并解释黑箱

6. REQUIREMENT: 防止train-test和target leakage

### evaluation_moves

1. STUDY_OVERVIEW: 说明演示与评价阶段

2. METHOD_JUSTIFICATION: 选择神经网络并用交叉验证

3. BENCHMARK_OR_CONTRAST: 给出六种评价指标

4. RESULT: 报告单特征、组合特征和外部baseline的结果

5. ROBUSTNESS_OR_BOUNDARY_TEST: 使用bootstrap、SMOTE和特征重要性/Shapley

6. RESULT: 网络+一般特征在top1最好；三类特征在top5/10最好

### discussion_and_contribution_moves

1. CONTRIBUTION: 理论、方法、实践三层贡献

2. THEORY_INTRO: 将结果放入设计科学和大数据研究议程

3. BOUNDARY_CONDITION: 指出数据来自Twitter且受API限制

4. LIMITATION_AND_FUTURE: 未来研究二阶连接、跨平台、规模化和成员-订阅互动

5. CONTRIBUTION: 声称首次综合网络、内容和一般社区特征构建订阅推荐器

## 理论/知识到设计的翻译

### 知识/理论基础

1. 网络科学：偏好依附/同配性 (Newman 2002; Capocci et al. 2006)

2. 结构洞与弱连接 (Burt 2002, 2004)

3. 中心性与连通性 (Freeman 1977; Borgatti 2005)

4. 小世界网络与随机游走/PageRank (Watts & Strogatz 1998; Page et al. 1999)

5. 时间演化的用户兴趣 (Hong & Davison 2010; Rakesh et al. 2014)

6. 设计科学框架 (Peffers et al. 2007)

- 理论—设计耦合：partial

- 耦合判定理由：网络科学概念确实前置地指导了同配性、结构洞、LCCR和中心性特征的设计，但一般特征（规模、重叠）来自数据探索，模型选择（神经网络）来自工程比较，且没有正式理论命题被直接检验。因此是部分耦合，而非从理论命题直接推演出全部设计的“direct”。

- 理论到设计翻译链：网络科学中“同配性决定连接形成”与“结构洞描述ego网络稀疏性” → 用户对列表的订阅选择受网络邻居结构制约 → 需要量化用户偏好与列表位置关系的特征 → 设计有向同配性/结构洞/中心性特征矩阵NC_U×NC_L → 在神经网络中与内容、一般特征共同预测订阅，并与文本基线比较。小世界/随机游走“用户像随机surfer沿共同订阅者探索新社区” → 用LCCR捕捉共同订阅聚类及其时间演化 → 递归算法作为网络特征进入推荐模型。注意力稀缺下“社区规模和重叠帮助筛选社区” → 设计list_size、overlap特征矩阵GC_C×GC_L。内容主题作为已有baseline，通过TW_U×TW_L产生偏好。

### mapping_table

#### 1. 1

- theory_or_knowledge_claim_cn：同配性/偏好依附：节点倾向连接度属性相似的节点（Newman 2002）；结构洞：节点邻居之间的稀疏程度影响信息与控制收益（Burt 2004）。

- mechanism_cn：用户订阅列表的选择受其嵌入的邻里结构影响；邻居间连接紧密与稀疏会改变用户可见的新社区范围。

- design_requirement_cn：需要计算列表及其策展人的出/入度、结构洞、中介与接近中心性，以量化偏好。

- artifact_choice_cn：在list-list网络中计算四类有向同配性（degree、structural holes、betweenness、closeness）并使用ASP/z-score检验；将结果放入网络特征向量NC_U与NC_L。

- evaluated_contrast_cn：不加入网络特征仅用内容特征；只加网络特征；不同特征组合。

- objective_result_cn：网络特征在top1 precision (0.8)高于内容特征(0.7)；网络+一般特征top1最高(0.97)。

##### evidence_pointers

1. Tables 4-5

2. Table 7

#### 2. 2

- theory_or_knowledge_claim_cn：小世界网络/局部聚类系数：邻居接近完全图的程度（Watts & Strogatz 1998）；随机surfer模型：随机浏览者按链接结构传播重要性（Page et al. 1999）。

- mechanism_cn：拥有紧密共同订阅聚类的用户，其兴趣更多样且会随时间探索其他订阅社区；LCCR把这种聚类紧密性沿网络递归传递。

- design_requirement_cn：需要捕捉共同订阅/共同成员网络中用户聚类结构及其跨时间演化。

- artifact_choice_cn：定义LCCR，对top-k/bottom-k边计算LCC与成员/订阅比值，采用类似于PageRank的递归公式和算法。

- evaluated_contrast_cn：与文本特征比较，以及融合进网络特征组合。

- objective_result_cn：网络特征优于文本特征于首位推荐；LCCR是网络特征的一部分，整体网络特征组合带来显著提升。

##### evidence_pointers

1. Section 5.1.2

2. Formulas 2-4

3. Table 7

#### 3. 3

- theory_or_knowledge_claim_cn：中心性与连通性：节点在网络中占据桥接或接近位置影响信息流动（Freeman 1977; Borgatti 2005）。

- mechanism_cn：在列表-用户两模网络中，位置更中心的列表可能被更多用户看到和订阅。

- design_requirement_cn：需要计算列表在订阅和成员两模网络中的betweenness、closeness、eigenvector centrality。

- artifact_choice_cn：用相关系数检验中心性与成员/订阅计数；将显著相关的中心性置入NC_L，与NC_U相乘得偏好矩阵。

- evaluated_contrast_cn：中心性加入网络特征后与内容/一般特征比较。

- objective_result_cn：列表中心性相关性与特征组合带来高位推荐改善。

##### evidence_pointers

1. Table 6

2. Formula 5

3. Table 7

#### 4. 4

- theory_or_knowledge_claim_cn：注意力经济：用户注意有限，社区数量巨大（Davenport & Beck 2001; Bessi et al. 2014）。

- mechanism_cn：用户以简单可观察的社区统计线索（规模、重叠）快速判断是否订阅。

- design_requirement_cn：需要提取社区规模、订阅规模、成员重叠和订阅重叠作为一般特征。

- artifact_choice_cn：生成GC_C与GC_L矩阵，用乘法得到一般特征偏好矩阵Δ。

- evaluated_contrast_cn：一般特征单独、与网络组合、与内容组合。

- objective_result_cn：一般特征单独较差（top1 precision 0.3），但与网络组合时top1达到0.97。

##### evidence_pointers

1. Section 5.2-5.4

2. Table 7

#### 5. 5

- theory_or_knowledge_claim_cn：已有社区推荐主要使用内容特征（Kamath 2013; Yang 2015），但内容主题可能不如列表结构代表用户兴趣。

- mechanism_cn：将推文主题分布作为内容向量，与列表主题向量相乘产生内容偏好。

- design_requirement_cn：需要构造可比的内容基线特征。

- artifact_choice_cn：用DDTM对用户和列表推文建10维主题分布，生成内容偏好矩阵Ω。

- evaluated_contrast_cn：作为文本基线，与网络/一般特征单独及组合比较。

- objective_result_cn：单独的文本在top-5/10、MRR、DCG上优于单独网络，但在top1劣于网络；网络+一般全面优于文本。

##### evidence_pointers

1. Section 5.5-5.7

2. Table 7

## 评价逻辑

### evaluation_modes

1. 离线历史数据基准实验（large-scale dataset offline benchmark）

2. 特征集合的消融/组合比较（ablation by feature sets）

3. 与经典推荐算法baseline对比

4. 与最新社区推荐方法（List PageRank/CSD/BGEGM）对比

5. 可解释性/特征贡献分析（permutation importance, Shapley）

6. 稳健性（bootstrap、SMOTE、数据泄漏控制）

- why_these_evaluations_cn：因为核心主张不是单一性能数字，而是三类特征的相对价值和互补性；离线基准可控制数据泄漏并比较不同位置上的推荐质量；baselines用于证明不是单纯模型优势；可解释性用于证明网络/一般特征贡献真实且可解释；稳健性处理类别不平衡和不确定度。

- benchmark_and_contrast_chain_cn：先以内容特征为baseline，单独比较General、Network；然后比较两两组合与三者组合；接着以五个经典推荐算法和三个现有社区推荐方法作为外部基准；最后用特征重要性和Shapley值解释为何组合结果更优。链条从“自身特征优劣”延伸到“相对文献方法的优势”，再回到“特征贡献的真实性”。

### claim_evidence_ledger

#### 1. 网络特征优于内容特征在top1推荐。

- claim_cn：网络特征优于内容特征在top1推荐。

- evidence_cn：Table 7 Precision@1：Network 0.8 vs Textual 0.7。

- status_cn：数据集内支持

#### 2. Network+General在top1组合中最优。

- claim_cn：Network+General在top1组合中最优。

- evidence_cn：Table 7 Precision@1：Network+General 0.97，优于其他组合；附B可解释性指标支持。

- status_cn：数据集内支持

#### 3. 三类特征联合在top5/top10最优。

- claim_cn：三类特征联合在top5/top10最优。

- evidence_cn：Table 7 All：Precision@5=0.94、@10=0.97，MRR=0.95，DCG=3.967。

- status_cn：数据集内支持

#### 4. 全文方法优于state-of-art和最新社区推荐方法。

- claim_cn：全文方法优于state-of-art和最新社区推荐方法。

- evidence_cn：Table 7中与User-based、List-based、Dimensionality-reduction、GMM、Link-analysis以及List PageRank、CSD、BGEGM的对比。

- status_cn：限定于所用评价指标和历史数据，支持

#### 5. 提出了新特征与高效算法且可解释。

- claim_cn：提出了新特征与高效算法且可解释。

- evidence_cn：Section 5.1.2公式/算法与Appendix B特征重要性/Shapley值。

- status_cn：部分支持：指标在数据集上有效，跨平台和长期效应未验证

- internal_validity_strategy_cn：特征只在训练集上计算；训练与测试按时间分离；每个时间段单独训练以避免target leakage；使用SMOTE处理类别不平衡；用bootstrap估计标准误；通过10折交叉验证降低过拟合。

- external_validity_strategy_cn：使用覆盖政治、商业、科技、健康等多类主题的Twitter列表；指出Twitter是主流平台且其他平台有同构社区（groups/boards），从而主张特征与方法可迁移；但未进行跨平台现场验证。

- what_is_not_actually_tested_cn：用户对推荐的实际点击/订阅后的满意度、推荐结果在真实产品中的曝光效果、其他平台的泛化、二阶网络连接的影响、全平台大规模部署、长期动态推荐效果。

## 贡献闭环

- technical_claim_cn：网络特征和一般特征在Twitter列表订阅推荐上比纯内容特征更有效，尤其能提升首位推荐质量；三类特征联合在top5/top10最佳。

- artifact_claim_cn：提出了可复用的设计科学方法：识别三类用户-社区关系网络、提取网络与一般特征矩阵，并用神经网络构建订阅推荐模型。

- mechanism_claim_cn：结构上的多样性（structural hole assortativity）和时间演化的兴趣变化（LCCR）能够捕捉用户订阅偏好的潜在机制；普遍网络的中心性位置影响列表被订阅的可能性。

- boundary_claim_cn：结论主要适用于Twitter列表语境、一阶网络关系、当前六个月数据规模和API可及范围；推广到其他平台需要把list对应到board/group并重新构造网络。

- reusable_design_knowledge_cn：设计者可按以下方式复用：先识别平台中curator/member/subscriber三类角色和订阅/成员关系，再构造list-list、user-user、list-user三类网络，然后计算同配性/结构洞/LCCR/中心性/规模/重叠等特征，最后用组合特征训练推荐模型。

- theoretical_contribution_cn：扩展了设计科学中利用大数据的预测/描述方法；将网络科学的同配性、随机游走、小世界等概念转化为可用于研究订阅偏好和链接形成的可解释特征；为在线社区与社会媒体推荐提供了特征层面的理论化工具。

- how_discussion_closes_intro_gap_cn：引言指出已有研究忽视用户和社区之间的关系网络；结论用实验证据表明网络特征不仅在首位推荐上超过内容特征，而且与一般特征组合后全面超过内容基线，同时在三类特征联合时达到top5/10最优，从而直接回应了“结构特征是否可推荐社区”和“是否能补充内容特征”的问题。

- overclaim_or_unsupported_leaps_cn：“首次结合三类特征”的声明较难核实，且缺少对同时期其他特征融合工作的系统对照；将离线历史数据上的推荐性能直接表述为对广告主和营销者的实用价值，缺乏现场或成本证据；将网络特征解释为“兴趣多样性”和“演化”属于事后解释，没有测量潜在兴趣。

## 句级写作动作图谱

### 1. P1 S1

- order：1

- section：Introduction

- locator：P1 S1

- move_code：CONTEXT

- paraphrase_cn：在线社区被定义为一群围绕共同目标、兴趣或目的聚集的人。

- rhetorical_function_cn：为全文确定研究对象并给出可操作定义。

- depends_on_cn：无需前置。

- sets_up_cn：引出平台上的lists/groups/boards等具体形式。

- evidence_pointer：Introduction P1 S1

### 2. P1 S2

- order：2

- section：Introduction

- locator：P1 S2

- move_code：PHENOMENON

- paraphrase_cn：数百万用户在平台上围绕广泛主题创建或订阅社区。

- rhetorical_function_cn：强调现象普遍且重要。

- depends_on_cn：依赖于社区定义。

- sets_up_cn：说明需要推荐社区以减少信息过载。

- evidence_pointer：Introduction P1 S2

### 3. P2 S1

- order：3

- section：Introduction

- locator：P2 S1

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：已有研究发现Twitter列表比推文内容更能代表用户兴趣。

- rhetorical_function_cn：为选择列表作为研究对象提供依据。

- depends_on_cn：社区与列表的对应关系。

- sets_up_cn：说明列表是理想的研究载体。

- evidence_pointer：Introduction P2 S1

### 4. P2 S2

- order：4

- section：Introduction

- locator：P2 S2

- move_code：PHENOMENON

- paraphrase_cn：调查表明列表让用户能够追踪比直接关注更多的人。

- rhetorical_function_cn：进一步说明列表的实用价值。

- depends_on_cn：P2 S1的列表代表性。

- sets_up_cn：为列表订阅推荐的意义铺垫。

- evidence_pointer：Introduction P2 S2

### 5. P3 S1

- order：5

- section：Introduction

- locator：P3 S1

- move_code：PHENOMENON

- paraphrase_cn：给出一个名为“Security”的Twitter列表示例，包含策展人、成员和订阅者。

- rhetorical_function_cn：用具体例子把抽象概念落地。

- depends_on_cn：前述列表定义。

- sets_up_cn：解释成员、订阅者的区别，并引出商业价值。

- evidence_pointer：Figure 1前一段

### 6. P3 S2

- order：6

- section：Introduction

- locator：P3 S2

- move_code：PRACTICAL_STAKES

- paraphrase_cn：该列表可用于向关注信息安全产品的企业提供广告线索。

- rhetorical_function_cn：强调研究对广告主的现实价值。

- depends_on_cn：示例中列表的成员和订阅者属性。

- sets_up_cn：说明错误推荐的代价，从而强化研究动机。

- evidence_pointer：Introduction P3 S2

### 7. P4 S1

- order：7

- section：Introduction

- locator：P4 S1

- move_code：LIMITATION

- paraphrase_cn：已有工作多使用内容和交互来推荐社区，很少关注用户与社区之间的关系结构。

- rhetorical_function_cn：建立文献缺口。

- depends_on_cn：前文关于社区类型和价值的背景。

- sets_up_cn：引出网络结构特征的核心主题。

- evidence_pointer：Introduction P4 S1

### 8. P4 S2

- order：8

- section：Introduction

- locator：P4 S2

- move_code：GAP

- paraphrase_cn：在线社区是社会结构，用户嵌入在社区与用户的关系网络中，因此可以利用这些关系来构建订阅推荐。

- rhetorical_function_cn：从“被忽视”转向“可利用”，形成核心缺口。

- depends_on_cn：P4 S1的局限。

- sets_up_cn：为三个研究问题提供前提。

- evidence_pointer：Introduction P4 S2

### 9. P4 S3

- order：9

- section：Introduction

- locator：P4 S3

- move_code：WHY_GAP_MATTERS

- paraphrase_cn：鉴于用户注意力稀缺，社区规模和重叠等一般特征也能帮助推荐订阅。

- rhetorical_function_cn：解释为何这一缺口重要且需要网络与非网络特征。

- depends_on_cn：P4 S2的网络嵌入观点。

- sets_up_cn：引出研究问题中的一般特征部分。

- evidence_pointer：Introduction P4 S3

### 10. P4 S4

- order：10

- section：Introduction

- locator：P4 S4

- move_code：RQ_OR_OBJECTIVE

- paraphrase_cn：提出三个研究问题：关系特征、一般特征、以及与内容特征的比较和补充。

- rhetorical_function_cn：明确研究任务，作为全文路线图。

- depends_on_cn：前四段的缺口与动机。

- sets_up_cn：后续方法、设计与评价均围绕这三问展开。

- evidence_pointer：Introduction P4 S4

### 11. P5 S1

- order：11

- section：Introduction

- locator：P5 S1

- move_code：THEORY_INTRO

- paraphrase_cn：使用网络科学中的小世界、弱连接、随机surfer模型和连通性来设计并提取特征。

- rhetorical_function_cn：引入理论工具包。

- depends_on_cn：研究问题。

- sets_up_cn：解释后续特征的具体知识来源。

- evidence_pointer：Introduction P5 S1

### 12. P5 S2

- order：12

- section：Introduction

- locator：P5 S2

- move_code：STUDY_OVERVIEW

- paraphrase_cn：构建了模型，发现网络特征在首位推荐最优、网络+一般特征首位最优、三类特征整体最优。

- rhetorical_function_cn：提前给出核心结果摘要。

- depends_on_cn：理论与特征设计。

- sets_up_cn：为结论部分的关键主张埋下伏笔。

- evidence_pointer：Introduction P5 S2

### 13. P5 S3

- order：13

- section：Introduction

- locator：P5 S3

- move_code：ROBUSTNESS_OR_BOUNDARY_TEST

- paraphrase_cn：特征构建和模型考虑了数据泄漏，并证明结果稳定显著。

- rhetorical_function_cn：预先防御对数据泄漏的质疑。

- depends_on_cn：方法与评价设计。

- sets_up_cn：后续评价中的稳健性安排。

- evidence_pointer：Introduction P5 S3

### 14. P6 S1

- order：14

- section：Introduction

- locator：P6 S1

- move_code：CONTRIBUTION

- paraphrase_cn：使用Peffers设计科学框架，提出可定制到其他平台的社区推荐设计方法。

- rhetorical_function_cn：把工程工作提升为设计科学贡献。

- depends_on_cn：前面整个研究概述。

- sets_up_cn：第3节框架与第7节贡献的呼应。

- evidence_pointer：Introduction P6 S1

### 15. P1 S1

- order：15

- section：Literature Review

- locator：P1 S1

- move_code：GAP

- paraphrase_cn：虽然有研究用社区推断用户兴趣和演化，但很少研究如何推荐社区给用户。

- rhetorical_function_cn：从已有文献转向不足。

- depends_on_cn：引言中的问题。

- sets_up_cn：为下一段内容推荐工作的综述做衬托。

- evidence_pointer：Section 2 P1 S1

### 16. P2 S1

- order：16

- section：Literature Review

- locator：P2 S1

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：最早的工作使用社区发布的内容构建推荐器，例如Ronen和Kamath。

- rhetorical_function_cn：综述已有内容方法。

- depends_on_cn：P1提出的推荐缺口。

- sets_up_cn：指出这些方法只依赖内容。

- evidence_pointer：Section 2 P2 S1

### 17. P2 S3

- order：17

- section：Literature Review

- locator：P2 S3

- move_code：LIMITATION

- paraphrase_cn：这些研究都只使用内容，没有使用相关社交网络特征。

- rhetorical_function_cn：明确内容方法的局限性。

- depends_on_cn：P2 S1-S2的综述。

- sets_up_cn：引入以网络为基础的方法。

- evidence_pointer：Section 2 P2 S3

### 18. P3 S1

- order：18

- section：Literature Review

- locator：P3 S1

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：后续方法如Rakesh、Han、Xiao、Yin分别使用列表订阅、相似度、公平性和深度学习。

- rhetorical_function_cn：综述最新工作，建立baseline。

- depends_on_cn：前面对早期内容方法的梳理。

- sets_up_cn：指出这些方法仍未考虑结构/位置特征。

- evidence_pointer：Section 2 P3 S1

### 19. P3 S2

- order：19

- section：Literature Review

- locator：P3 S2

- move_code：LIMITATION

- paraphrase_cn：这些方法没有考虑社区和用户嵌入网络中的结构性和位置性特征。

- rhetorical_function_cn：将缺口精确到结构/位置特征。

- depends_on_cn：P3 S1的最新方法综述。

- sets_up_cn：为本文基于网络科学设计特征作铺垫。

- evidence_pointer：Section 2 P3 S2

### 20. P4 S1

- order：20

- section：Literature Review

- locator：P4 S1

- move_code：THEORY_PROPOSITION

- paraphrase_cn：因为用户消费多个社区内容，用户与社区的隶属网络可以量化订阅偏好。

- rhetorical_function_cn：提出本文的基本理论命题。

- depends_on_cn：P3指出的结构特征缺口。

- sets_up_cn：引出同配性和LCCR特征设计。

- evidence_pointer：Section 2 P4 S1

### 21. P4 S2

- order：21

- section：Literature Review

- locator：P4 S2

- move_code：MECHANISM

- paraphrase_cn：结合偏好依附和弱连接文献，设计出用户偏好的同配性特征。

- rhetorical_function_cn：解释网络特征背后的机制。

- depends_on_cn：P4 S1的理论命题。

- sets_up_cn：为5.1.1的同配性分析提供理论解释。

- evidence_pointer：Section 2 P4 S2

### 22. P4 S3

- order：22

- section：Literature Review

- locator：P4 S3

- move_code：MECHANISM

- paraphrase_cn：共同订阅网络的特性结合随机surfer模型和小世界网络，形成LCCR特征。

- rhetorical_function_cn：解释第二个核心网络特征的来源。

- depends_on_cn：P4 S1和P4 S2。

- sets_up_cn：为5.1.2的LCCR设计铺垫。

- evidence_pointer：Section 2 P4 S3

### 23. P5 S1

- order：23

- section：Literature Review

- locator：P5 S1

- move_code：REQUIREMENT

- paraphrase_cn：位置网络特征可以解决协同过滤在社区推荐中的操作问题，一般社区特征也有价值。

- rhetorical_function_cn：说明为什么需要位置特征和一般特征。

- depends_on_cn：P4的理论命题。

- sets_up_cn：为5.1.3和5.2-5.4的特征设计提供依据。

- evidence_pointer：Section 2 P5 S1

### 24. Section 3 P1

- order：24

- section：Research Design and Process

- locator：Section 3 P1

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：采用Peffers等的设计科学名义过程模型来组织研究阶段。

- rhetorical_function_cn：用方法论框架为文章结构提供合法性。

- depends_on_cn：引言中提出的设计科学定位。

- sets_up_cn：后续Framework图及各阶段描述。

- evidence_pointer：Section 3 P1

### 25. Section 3 P2

- order：25

- section：Research Design and Process

- locator：Section 3 P2

- move_code：STUDY_OVERVIEW

- paraphrase_cn：设计阶段确定了三类网络，并用网络科学和时间变化识别特征，同时修正数据泄漏。

- rhetorical_function_cn：概述设计阶段的内容。

- depends_on_cn：设计科学框架。

- sets_up_cn：为第5节详细设计做预告。

- evidence_pointer：Section 3 P2

### 26. Section 3 P3

- order：26

- section：Research Design and Process

- locator：Section 3 P3

- move_code：ARTIFACT

- paraphrase_cn：制品是由方法、特征提取流程和评价过程组成的整体。

- rhetorical_function_cn：定义本文的artifact并援引Hevner等人。

- depends_on_cn：设计科学框架。

- sets_up_cn：强调方法和流程都是贡献。

- evidence_pointer：Section 3 P3

### 27. Section 4 P1

- order：27

- section：Data Description

- locator：Section 4 P1

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：用Listorious和NYT关键词生成随机列表，采集策展人及其列表、成员、订阅者和推文，连续六个月。

- rhetorical_function_cn：说明数据来源和采集方式，使结果可复现。

- depends_on_cn：研究问题需要大规模真实数据。

- sets_up_cn：提供后续网络和特征分析的数据基础。

- evidence_pointer：Section 4 P1

### 28. Section 4 P2

- order：28

- section：Data Description

- locator：Section 4 P2

- move_code：RESULT

- paraphrase_cn：给出数据集描述性统计，包括列表、成员、关注、订阅和推文数量。

- rhetorical_function_cn：证明数据集规模足够。

- depends_on_cn：P1的数据采集。

- sets_up_cn：为后续特征计算的可行性和代表性提供证据。

- evidence_pointer：Table 2

### 29. Section 5.1 P1

- order：29

- section：Design

- locator：Section 5.1 P1

- move_code：DESIGN_FEATURE

- paraphrase_cn：用两类实体和三种关系构造list-list、user-user、list-user网络。

- rhetorical_function_cn：给出网络设计的总体思路。

- depends_on_cn：数据中的用户和列表角色。

- sets_up_cn：为具体网络定义提供框架。

- evidence_pointer：Section 5.1

### 30. Section 5.1 P2

- order：30

- section：Design

- locator：Section 5.1 P2

- move_code：DESIGN_FEATURE

- paraphrase_cn：分别定义成员关系和订阅关系下的三个网络，并说明节点和链接含义。

- rhetorical_function_cn：把研究问题转成可计算的图对象。

- depends_on_cn：前一网络设计思路。

- sets_up_cn：为同配性等特征计算提供输入。

- evidence_pointer：Table 3, Figures 4-6

### 31. Section 5.1 P3

- order：31

- section：Design

- locator：Section 5.1 P3

- move_code：REQUIREMENT

- paraphrase_cn：为避免数据泄漏，所有特征只在训练集上计算，并按时间段分别训练。

- rhetorical_function_cn：建立内部有效性防线。

- depends_on_cn：对时间序列数据的认识。

- sets_up_cn：第6节评价的可靠性。

- evidence_pointer：Section 5.1末段

### 32. Section 5.1.1 P1

- order：32

- section：Design

- locator：Section 5.1.1 P1

- move_code：MECHANISM

- paraphrase_cn：列表成员关系和订阅关系反映用户追踪他人活动的意图，因此用有向同配性进行量化。

- rhetorical_function_cn：解释为什么同配性能量化用户偏好。

- depends_on_cn：list-list网络。

- sets_up_cn：引出四类同配性的具体计算。

- evidence_pointer：Section 5.1.1 P1

### 33. Section 5.1.1 P2

- order：33

- section：Design

- locator：Section 5.1.1 P2

- move_code：MECHANISM

- paraphrase_cn：同配性只反映ego与alters的直接连接，需用结构洞和中心性描述ego嵌入的更广社区。

- rhetorical_function_cn：说明为何需要更多网络特征。

- depends_on_cn：同配性的局限。

- sets_up_cn：为structural holes、betweenness、closeness分析铺垫。

- evidence_pointer：Section 5.1.1 P2

### 34. Section 5.1.1 P3

- order：34

- section：Design

- locator：Section 5.1.1 P3

- move_code：RESULT

- paraphrase_cn：结构洞的四个成分显著，betweenness不显著，closeness的in-in和out-in显著。

- rhetorical_function_cn：用统计检验结果支撑“结构影响订阅”的命题。

- depends_on_cn：列联表和显著性检验。

- sets_up_cn：表明网络特征有信息量，进而研究共同订阅。

- evidence_pointer：Tables 4-5

### 35. Section 5.1.1 P4

- order：35

- section：Design

- locator：Section 5.1.1 P4

- move_code：TRANSITION

- paraphrase_cn：单个列表周围的同配性不能覆盖多列表共同订阅模式，需进一步分析用户间的共同订阅网络。

- rhetorical_function_cn：从同配性过渡到LCCR。

- depends_on_cn：同配性的结果与限制。

- sets_up_cn：引出5.1.2。

- evidence_pointer：Section 5.1.1 P4

### 36. Section 5.1.2 P1

- order：36

- section：Design

- locator：Section 5.1.2 P1

- move_code：MECHANISM

- paraphrase_cn：两个用户共同订阅说明兴趣相似，但这些相似关系会形成聚类并随时间变化。

- rhetorical_function_cn：建立共同订阅网络分析的必要性。

- depends_on_cn：用户多样化的订阅行为。

- sets_up_cn：引出LCC和LCCR定义。

- evidence_pointer：Section 5.1.2 P1

### 37. Section 5.1.2 P2

- order：37

- section：Design

- locator：Section 5.1.2 P2

- move_code：THEORY_PROPOSITION

- paraphrase_cn：LCCR的直觉是嵌入紧密共同订阅网络的用户应获得更高排名，这类似随机surfer沿社区探索。

- rhetorical_function_cn：用PageRank类比解释新特征机制。

- depends_on_cn：共同订阅聚类现象。

- sets_up_cn：为LCCR公式和算法提供理论解释。

- evidence_pointer：Section 5.1.2 P2

### 38. Section 5.1.2 P3

- order：38

- section：Design

- locator：Section 5.1.2 P3

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：用top-k分析和演化向量来确定用户的相似邻居及其时间变化。

- rhetorical_function_cn：说明LCCR计算前的关键预处理。

- depends_on_cn：需要定义邻域和演化。

- sets_up_cn：给出聚类和演化向量结果。

- evidence_pointer：Section 5.1.2 P3

### 39. Section 5.1.2 P4

- order：39

- section：Design

- locator：Section 5.1.2 P4

- move_code：RESULT

- paraphrase_cn：每月都出现低、中、高三个LCC簇，且LCC随k增加而增加；共同订阅的演化呈交替增减。

- rhetorical_function_cn：用数据说明聚类结构和时间变化确实存在。

- depends_on_cn：top-k与演化向量计算。

- sets_up_cn：为LCCR的递归公式提供实证基础。

- evidence_pointer：Figure 7, Formula 3

### 40. Section 5.1.2 P5

- order：40

- section：Design

- locator：Section 5.1.2 P5

- move_code：DESIGN_FEATURE

- paraphrase_cn：正式定义LCCR递归公式，并给出可收敛的算法；每个策展人得到一个9维网络特征向量。

- rhetorical_function_cn：把理论机制变成可计算特征。

- depends_on_cn：前述LCC演化结果。

- sets_up_cn：为进入矩阵乘法与推荐模型做准备。

- evidence_pointer：Formula 4, Algorithm

### 41. Section 5.1.3 P1

- order：41

- section：Design

- locator：Section 5.1.3 P1

- move_code：RESULT

- paraphrase_cn：列表中心性与成员/订阅计数存在可观察的相关：订阅与betweenness相关，成员与closeness相关。

- rhetorical_function_cn：支持“位置影响订阅”的假设。

- depends_on_cn：两模网络中心性计算。

- sets_up_cn：将中心性纳入NC_L矩阵。

- evidence_pointer：Table 6

### 42. Section 5.1.3 P2

- order：42

- section：Design

- locator：Section 5.1.3 P2

- move_code：DESIGN_FEATURE

- paraphrase_cn：构造列表网络特征列向量NC_L，并与用户网络特征矩阵NC_U相乘得到偏好矩阵。

- rhetorical_function_cn：将网络特征统一成用户-列表偏好表达。

- depends_on_cn：中心性相关结果。

- sets_up_cn：为推荐模型中的network component提供输入。

- evidence_pointer：Formula 5

### 43. Section 5.2-5.4 P1

- order：43

- section：Design

- locator：Section 5.2-5.4 P1

- move_code：THEORY_PROPOSITION

- paraphrase_cn：注意力稀缺使得简单的一般社区属性如规模和重叠，能帮助用户决定订阅哪些社区。

- rhetorical_function_cn：为一般特征提供理论依据。

- depends_on_cn：引言中的注意力经济问题。

- sets_up_cn：引出规模与重叠的具体分析。

- evidence_pointer：Section 5.2

### 44. Section 5.4 P2

- order：44

- section：Design

- locator：Section 5.4 P2

- move_code：RESULT

- paraphrase_cn：成员和订阅重叠均值接近零，但标准差较大且随时间稳定，说明用户间存在可用的异质性。

- rhetorical_function_cn：把一般特征从描述性观察提升为预测特征。

- depends_on_cn：重叠度计算公式。

- sets_up_cn：形成GC_C和GC_L矩阵。

- evidence_pointer：Section 5.4 P2

### 45. Section 5.4 P3

- order：45

- section：Design

- locator：Section 5.4 P3

- move_code：DESIGN_FEATURE

- paraphrase_cn：将策展人和列表的规模/重叠特征组织成矩阵并相乘得到用户偏好矩阵Δ。

- rhetorical_function_cn：形式化一般特征输入。

- depends_on_cn：规模与重叠分析。

- sets_up_cn：为推荐模型中的general component提供输入。

- evidence_pointer：Formula 7

### 46. Section 5.5-5.7 P1

- order：46

- section：Design

- locator：Section 5.5-5.7 P1

- move_code：BENCHMARK_OR_CONTRAST

- paraphrase_cn：使用推文主题作为基线特征，并说明简单LDA对短文本效果差，采用DDTM。

- rhetorical_function_cn：建立后续比较的content baseline。

- depends_on_cn：已有内容推荐文献。

- sets_up_cn：为TW_U×TW_L矩阵和模型比较做准备。

- evidence_pointer：Section 5.6

### 47. Section 6.1 P1

- order：47

- section：Evaluation

- locator：Section 6.1 P1

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：采用神经网络融合三类特征并用交叉验证及超参优化；用可解释AI指标弥补黑箱。

- rhetorical_function_cn：解释模型选择并防御黑箱批评。

- depends_on_cn：多类特征需要进行非线性融合。

- sets_up_cn：为特征重要性和Shapley分析提供理由。

- evidence_pointer：Section 6.1

### 48. Section 6.2 P1

- order：48

- section：Evaluation

- locator：Section 6.2 P1

- move_code：BENCHMARK_OR_CONTRAST

- paraphrase_cn：给出六个评价指标：accuracy、precision@k、recall@k、F-score@k、MRR、DCG。

- rhetorical_function_cn：建立系统评价框架。

- depends_on_cn：推荐系统评估标准。

- sets_up_cn：为结果表提供指标列。

- evidence_pointer：Section 6.2

### 49. Section 6.3 P1

- order：49

- section：Evaluation

- locator：Section 6.3 P1

- move_code：RESULT

- paraphrase_cn：网络特征在top1超过一般和内容特征；网络+一般组合在top1达到最高。

- rhetorical_function_cn：报告核心结果之一。

- depends_on_cn：模型训练和指标计算。

- sets_up_cn：解释网络特征的价值。

- evidence_pointer：Table 7

### 50. Section 6.3 P2

- order：50

- section：Evaluation

- locator：Section 6.3 P2

- move_code：RESULT

- paraphrase_cn：单独内容特征在top5/10、MRR和DCG上优于单独网络特征，但网络+一般组合在所有指标上超过纯内容。

- rhetorical_function_cn：在承认内容优势的同时强调网络+一般的整体优势。

- depends_on_cn：Table 7结果。

- sets_up_cn：为特征互补性主张提供证据。

- evidence_pointer：Table 7, Figure 8

### 51. Section 6.3 P3

- order：51

- section：Evaluation

- locator：Section 6.3 P3

- move_code：ROBUSTNESS_OR_BOUNDARY_TEST

- paraphrase_cn：特征重要性和Shapley值显示，网络+一般特征的平均贡献高于纯文本特征。

- rhetorical_function_cn：用可解释性分析补充性能差异。

- depends_on_cn：模型解释工具。

- sets_up_cn：强化“参与网络结构确实有用”的机制主张。

- evidence_pointer：Figures B1-B4

### 52. Section 6.3 P4

- order：52

- section：Evaluation

- locator：Section 6.3 P4

- move_code：RESULT

- paraphrase_cn：Textual+Network出现维度诅咒，网络特征在该组合中未降低错误率；三类特征联合在top5/10上表现最好。

- rhetorical_function_cn：报告组合实验中的反直觉发现与总体最优组合。

- depends_on_cn：特征组合实验。

- sets_up_cn：为实践建议（按目标选择不同组合）提供依据。

- evidence_pointer：Section 6.3 P4

### 53. Section 6.3 P5

- order：53

- section：Evaluation

- locator：Section 6.3 P5

- move_code：BENCHMARK_OR_CONTRAST

- paraphrase_cn：与经典推荐算法及现有列表推荐方法相比，本文方法在多数指标上明显更好。

- rhetorical_function_cn：将贡献从内部特征比较扩展到外部文献比较。

- depends_on_cn：baseline实现与指标。

- sets_up_cn：为结论中的“优于最新工作”提供证据。

- evidence_pointer：Table 7后半部分

### 54. Section 6.3 P6

- order：54

- section：Evaluation

- locator：Section 6.3 P6

- move_code：TRANSITION

- paraphrase_cn：根据目标不同，推荐网络+一般特征用于首位高质量推荐，或三类组合用于整体top10推荐。

- rhetorical_function_cn：把结果转化为可操作建议，并转向结论。

- depends_on_cn：所有实验结果。

- sets_up_cn：结论部分的贡献总结。

- evidence_pointer：Section 6.3末段

### 55. Section 7 P1

- order：55

- section：Conclusion

- locator：Section 7 P1

- move_code：CONTRIBUTION

- paraphrase_cn：提出设计科学方法，用网络、内容和一般社区特征构建订阅推荐器，并声称是首个结合三类特征的推荐器。

- rhetorical_function_cn：用最高层声明概括贡献。

- depends_on_cn：全文结果。

- sets_up_cn：后续理论/方法/实践贡献的分层展开。

- evidence_pointer：Section 7 P1

### 56. Section 7.1

- order：56

- section：Conclusion

- locator：Section 7.1

- move_code：CONTRIBUTION

- paraphrase_cn：贡献扩展到设计科学大数据框架：在缺少现成社会/经济理论时，可从大规模行为数据中提取特征并用于推荐。

- rhetorical_function_cn：将实证工作关联到设计科学理论。

- depends_on_cn：结论开篇的贡献声明。

- sets_up_cn：为未来大数据设计科学研究提供路线。

- evidence_pointer：Section 7.1

### 57. Section 7.2

- order：57

- section：Conclusion

- locator：Section 7.2

- move_code：CONTRIBUTION

- paraphrase_cn：方法论贡献包括新网络特征与高效算法，可迁移到其他平台的boards/groups网络。

- rhetorical_function_cn：强调可复用的方法内容。

- depends_on_cn：网络特征设计章节。

- sets_up_cn：为实践者采用提供具体清单。

- evidence_pointer：Section 7.2

### 58. Section 7.3

- order：58

- section：Conclusion

- locator：Section 7.3

- move_code：PRACTICAL_STAKES

- paraphrase_cn：实际贡献在于为在线社区推荐系统提供新特征和新方法，帮助广告主和平台定位受众。

- rhetorical_function_cn：回扣引言中的广告价值。

- depends_on_cn：性能结果。

- sets_up_cn：说明结果不只是学术指标，而有商业含义。

- evidence_pointer：Section 7.3

### 59. Section 8 P1

- order：59

- section：Limitations

- locator：Section 8 P1

- move_code：LIMITATION_AND_FUTURE

- paraphrase_cn：研究只使用一阶连接，可扩展至二阶连接；成员与订阅行为的交互尚未深入；API速率限制影响规模；未来可在其他平台验证。

- rhetorical_function_cn：诚实界定边界并给出未来方向。

- depends_on_cn：全文方法与结果。

- sets_up_cn：保护贡献不被过度泛化。

- evidence_pointer：Section 8

## 写作技术

- gap_construction_cn：先承认已有推荐多基于内容或简单交互，再指出用户与社区嵌入的关系网络未被充分利用；把缺口表达为既有方法对结构/位置特征的系统性忽视，并以注意力经济说明缺口重要。

- signposting_cn：使用三个研究问题作为路线图；在文献与设计部分反复提示下一小节要回答的问题；用设计科学框架显式预告demonstration/evaluation/communication阶段。

- transition_logic_cn：每完成一类网络分析后，以‘这是否足够’引出下一类分析（如同配性→共同订阅→位置特征）；在特征提取后自然转到模型评价；评价后又用可解释性补强结果。

- claim_evidence_rhythm_cn：在每个特征小节先给理论机制，再做统计检验或描述性结果，最后形成矩阵特征；结果部分先报告推荐指标，再用特征重要性解释，最后用外部baseline扩大对照。

- benchmark_narrative_cn：将文本内容特征定义为基线，逐步加入一般和网络特征；再连接经典推荐算法和最新社区推荐工作，使benchmark不仅证明性能，也承担“弥补文献缺口的证据”功能。

- theory_return_cn：结论部分把网络科学概念（LCCR、同配性）升华为可复用的设计科学方法，并声称对研究链接形成、网络嵌入和平台推荐的理论贡献。

- contribution_positioning_cn：按理论、方法、实践三层分别声明贡献，并强调‘首次结合三类特征’和‘可定制到其他平台’，同时以设计科学框架命名使贡献进入特定研究传统。

- novelty_protection_cn：通过组合多个网络科学概念构造新指标（structural hole assortativity、LCCR），提供高效算法和可解释性分析；用数据泄漏控制和稳健性检验防止结果被归为偶然/过拟合；用外部baseline证明不是普通分类器优势。

## 可复用研究与写作程序

### structure_steps

#### 1. 1

- step：1

- writing_job_cn：用现实案例和已有研究定义推荐缺口

- research_job_cn：收集领域文献和案例证据

- required_evidence_cn：不同方法之间的系统对比证据

- transition_to_next_cn：提出研究问题

#### 2. 2

- step：2

- writing_job_cn：引入理论/知识基础并将知识转译成可计算网络对象

- research_job_cn：识别实体和关系网络

- required_evidence_cn：存在可提取的关系网络

- transition_to_next_cn：进行特征推导

#### 3. 3

- step：3

- writing_job_cn：设计新特征/指标，通过统计检验/描述分析支撑

- research_job_cn：在大样本中计算指标并验证差异

- required_evidence_cn：指标与目标行为有系统关联

- transition_to_next_cn：形成特征矩阵

#### 4. 4

- step：4

- writing_job_cn：建立baseline和多个比较对象

- research_job_cn：构建模型和评价框架

- required_evidence_cn：baseline可运行并产生可比结果

- transition_to_next_cn：运行多个特征组合

#### 5. 5

- step：5

- writing_job_cn：用消融/组合实验证明特征相对价值

- research_job_cn：对所有组合进行评价

- required_evidence_cn：稳健的性能差异

- transition_to_next_cn：解释特征贡献

#### 6. 6

- step：6

- writing_job_cn：用可解释性和稳健性检验保护贡献

- research_job_cn：特征重要性、bootstrap、防泄漏措施

- required_evidence_cn：贡献不是偶然

- transition_to_next_cn：归纳设计知识

#### 7. 7

- step：7

- writing_job_cn：回到理论/设计科学框架表述贡献与边界

- research_job_cn：明确适用条件与局限

- required_evidence_cn：对应用条件和未检验部分的说明

- transition_to_next_cn：完成贡献声明

### most_transferable_moves_cn

1. 用大标题式研究问题控制文章结构

2. 把网络科学概念转译成可计算指标并在表格中展示显著性

3. 建立内容特征为第一基线，用组合实验展示互补性

4. 在结果后增加可解释性分析保护黑箱模型

5. 以设计科学框架把工程性工作命名为理论/方法贡献

### resource_intensive_or_nonstandard_parts_cn

1. 收集6个月的Twitter多类型数据（列表、成员、订阅、关注、推文）并清洗

2. Listorious等多源数据获取

3. 大规模网络特征计算与神经网络超参优化

4. 第三方平台API速率限制和伦理/隐私问题

### what_not_to_copy_superficially_cn

1. 只给LCCR公式而不说明为什么它能代表随机surfer机制

2. 在没有数据泄漏控制的情况下宣称网络特征优于内容

3. 没有足够baseline就声称outperform

4. 用‘首次’声明贡献而没有对已有方法全面比较

5. 将单一平台离线结果直接推广到其他平台

- single_best_description_of_the_routine_cn：先让读者相信‘结构一直被忽视’，再把网络科学概念做成可计算特征矩阵，用消融实验证明结构特征本身和与其他特征组合的价值，最后用设计科学框架把这些工程步骤包装成可复用方法。

## 分析边界

全文可读，但个别公式字符和附录图片无法完全校验；研究阶段划分与句子级动作标记依赖对章节的逐段阅读，非OCR页码；论文未提供实际推荐界面或现场部署证据，因此外部效度判断受限。
