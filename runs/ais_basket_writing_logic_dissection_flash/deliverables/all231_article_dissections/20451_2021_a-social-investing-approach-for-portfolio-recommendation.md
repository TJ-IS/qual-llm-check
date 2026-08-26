# A social investing approach for portfolio recommendation

- 作者：Yung-Ming Li; Lien-Fa Lin; Chin-Yu Hsieh; Bo-Syun Huang
- 年份 / 期刊：2021 / Information & Management
- DOI：10.1016/j.im.2021.103536
- 源文件：20451_2021_a-social-investing-approach-for-portfolio-recommendation.md
- 论文主类型：build_evaluate_design_science
- 主导写作弧线：performance_gap_artifact_benchmark_generalize
- 置信度：0.84

## 文章级论证概况

- 核心问题：如何从社交投资平台上大量投资者生成的帖子中提取集体智慧，构建能够依据用户风险偏好推荐股票投资组合的决策支持机制，并使其在收益与风险调整绩效上优于市场指数和既有替代方法？

- 制品与设计：提出一个名为CIR的集体智慧投资组合推荐机制，包含特征词典构建、情感分析、知识分析、影响力分析、财务报表分析和投资组合构建六大模块；以帖子情感分数、作者领域分、关键词分、名人分、评分分和公司财务分加权聚合为帖子重要性，再按用户风险偏好配置股票权重。

- 客观结果：在eToro评论数据上的30日模拟交易中，标准风险组合CIR实现30.369%回报，而S&P 500为-0.806%，no-filter、knowledge-based、authority-based分别为-27.550%、16.180%、2.168%；Treynor比率和Jensen alpha也显示CIR优于其他方法；低风险与高风险定制组合中CIR也总体最好（高风险组合与authority-based持平）。

- 核心贡献：作者声称首次从系统开发、数据源、方法论、实践和金融五个层面贡献：构建了基于社交投资平台评论的投资决策支持系统；利用可追踪真实交易的投资者的帖子作为数据源；综合帖子、投资者、公司三维特征进行可信度评估；帮助初学者在信息过载中决策；通过集体智慧避免非理性行为并降低风险。

- 整篇论证链：文章以负利率和散户非理性行为导致平均股票基金投资者收益远低于市场指数为现实痛点，引入社交投资平台上的‘跟随/复制’投资现象和众包智慧证据，指出现有投资决策支持系统很少利用社交投资平台上的投资者评论。作者由此构建CIR机制，将帖子情感、作者领域知识、关键词相关度、社交影响力、点赞者绩效和公司财务指标统一成帖子和投资标的的评分，再通过beta将股票分成不同风险类型，按用户风险偏好生成定制组合。实验以eToro股票论坛927条帖子为输入，构建三类推荐列表，在30日模拟交易中与S&P 500以及no-filter、knowledge-based、authority-based三个层次化基准比较，用累计收益、Treynor比率和Jensen alpha证明CIR更好；随后按风险偏好生成低/中/高风险组合，再次比较得到CIR最优或持平。讨论部分把结果回接到引言中的信息过载和决策支持缺口，提出系统、数据、方法、实践和金融层面的贡献，并列出平台单一、标的集中于科技股、未考虑用户画像等边界条件。

## 类型与写作弧线判定

- 论文主类型判定：文章不是由正式理论推导假设并进行受控实验，而是围绕社会投资平台信息过载这一实际问题，提出一套多模块推荐制品，在真实平台数据上构建推荐列表，并用市场基准和消融式基准进行评价，最后总结为面向投资决策支持系统的贡献。

- 主导写作弧线判定：引言先构造散户绩效缺口（5.19%对9.85%），随后把社会平台海量信息处理能力缺乏作为性能痛点，提出CIR制品，再通过S&P500和分层基准的对比把制品价值一般化为设计知识；全文主线是性能缺口—制品—benchmark—一般化，而非从正式理论推出可检验命题。

## 研究开展程序

- study_or_phase_count：8

- 研究阶段总序列：文章按系统构建和评价的流水线展开：先对eToro帖子做清洗和特征抽取，再分别计算情感、作者知识、影响力和公司财务分，然后用PCA确定权重并生成推荐列表，最后进行30日组合绩效评价和按风险偏好的定制组合评价。各阶段不是独立实验，而是前一阶段输出作为后一阶段输入，最终以组合绩效检验整体制品。

### studies_or_phases

#### 1. 数据收集、预处理与特征抽取

- order：1

- name_cn：数据收集、预处理与特征抽取

- question_cn：如何把eToro股票论坛中嘈杂的英文帖子转化为可用于后续情感和知识分析的结构化特征？

- inputs_and_setting_cn：eToro.com上2016年12月至2017年3月期间收集的927条股票帖子；NLTK、Textblob、Porter stemming。

- designed_or_compared_object_cn：特征词典：去停用词、词干化、POS标注后，用TF-IDF对词排序并选取前500个关键词。

- baseline_control_or_counterfactual_cn：无；该阶段是描述性数据构建，不设对照。

##### objective_metrics

1. 句子数量

2. 名词/形容词/副词数量

3. TF-IDF词得分排序

4. 词典规模

- analysis_method_cn：停用词移除、Porter stemming、词性标注、TF-IDF特征选择。

- main_result_cn：共得到29,060个句子、58,863个名词、33,569个形容词和23,533个副词；从3,453个候选词中选出前500个作为特征关键词。

- argumentative_role_cn：为后续关键词分和情感分析提供统一词典与预处理文本，是制品能够处理非结构化评论的基础。

- remaining_uncertainty_cn：仅保留英文帖子可能遗漏非英语观点；未验证500个关键词是否充分代表投资者关注主题。

- link_to_next_phase_cn：预处理后的句子和词典直接作为情感分类和知识分析模块的输入。

##### evidence_pointers

1. Section 4.1

2. Tables 2-4

#### 2. 情感分类与情感分析

- order：2

- name_cn：情感分类与情感分析

- question_cn：如何度量每个帖子对投资标的的乐观或悲观程度？

- inputs_and_setting_cn：预处理后的eToro帖子；Loughran-McDonald情感词表；Textblob的Naive Bayes分类器。

- designed_or_compared_object_cn：帖子情感分数：将金融情感分数与Textblob审查情感分数平均。

- baseline_control_or_counterfactual_cn：并非严格对照；两个情感计算方法被平均以提升准确率。

##### objective_metrics

1. 正/负/中性词比例

2. financial_sentiment分数

3. review_sentiment分数

4. SentimentScore

- analysis_method_cn：基于情感词典的词级极性标注与基于Textblob的文档级情感分类。

- main_result_cn：每个帖子获得介于正负之间的综合情感分数，用于表达公众对投资标的的情绪。

- argumentative_role_cn：情感是CIR评分中最核心的意见信号，也是no-filter基准的基础。

- remaining_uncertainty_cn：Textblob基于电影评论训练，与金融话语存在领域偏移；仅用情感无法获得高回报。

- link_to_next_phase_cn：情感分数作为PostImportance中的乘数，与知识、影响力、财务分结合。

##### evidence_pointers

1. Section 3.2 Eq(1)-(2)

2. Section 4.2

#### 3. 知识分析与影响力分析

- order：3

- name_cn：知识分析与影响力分析

- question_cn：如何从作者的历史交易、帖子关键词、社交关系和点赞者绩效量化帖子可信度？

- inputs_and_setting_cn：eToro用户历史交易记录、帖子内容、关注关系、评论关系、点赞用户及其利润比率。

- designed_or_compared_object_cn：四个作者层面分数：领域分、关键词分、名人分、评分分。

- baseline_control_or_counterfactual_cn：无独立对照；但四个分数在后续基准中分别被用作knowledge-based和authority-based组合的成分。

##### objective_metrics

1. Domain Score

2. Keyword Score

3. Celebrity Score

4. Rating Score

- analysis_method_cn：历史交易类别集中度计算、帖子关键词句比例计算、显式/隐式链接归一化、按点赞者利润比率加权。

- main_result_cn：每个帖子获得四维可信度分数；文章给出部分帖子得分表示例子。

- argumentative_role_cn：这是CIR区别于纯情感推荐的关键：过滤并加权值得信任的投资者意见。

- remaining_uncertainty_cn：未单独检验各分数对最终绩效的独立贡献；权威分和知识分相对重要性不明确。

- link_to_next_phase_cn：四个分数通过PCA进入最终帖子重要性公式，并构成knowledge-based与authority-based基准的评分。

##### evidence_pointers

1. Section 3.3-3.4

2. Section 4.3

3. Table 5

#### 4. 财务报表分析

- order：4

- name_cn：财务报表分析

- question_cn：如何将公司基本面的健康程度纳入投资标的评分？

- inputs_and_setting_cn：来自WRDS数据库的上市公司财务比率。

- designed_or_compared_object_cn：财务报告分数FSS：由盈利能力、营运能力、资本结构和流动性四类共八个比率平均得到。

- baseline_control_or_counterfactual_cn：无消融对照；FSS作为PostImportance中的乘数整体出现。

##### objective_metrics

1. ROTA

2. EPS

3. RTR

4. IT

5. DAR

6. LTFFA

7. CR

8. QR

9. FSS

- analysis_method_cn：对八个财务比率做归一化后取平均。

- main_result_cn：各标的获得0到1之间的FSS分数，例如Micron 0.402、Apple 0.349。

- argumentative_role_cn：把公司基本面作为目标质量信号，防止帖子情绪完全脱离企业真实状况。

- remaining_uncertainty_cn：没有单独检验FSS对推荐绩效的增量贡献；财务比率的权重均等也未被论证。

- link_to_next_phase_cn：FSS作为PostImportance公式中的最后一个乘数，影响所有帖子的加权重要性。

##### evidence_pointers

1. Section 3.5

2. Section 4.4

3. Table 6

#### 5. 风险偏好与Beta分析

- order：5

- name_cn：风险偏好与Beta分析

- question_cn：如何把股票按风险分类，以匹配不同用户的投资偏好？

- inputs_and_setting_cn：Yahoo Finance获取的个股与S&P500在2014/03/01至2017/03/01期间的日收盘价。

- designed_or_compared_object_cn：每股beta值及高风险/正常风险/低风险股票分组。

- baseline_control_or_counterfactual_cn：无对照；仅作为风险分类工具。

##### objective_metrics

1. Beta值

2. 高风险/正常风险/低风险分类

- analysis_method_cn：用个股日收益率与市场指数日收益率的协方差除以市场方差计算beta，并按1.25和0.75阈值分类。

- main_result_cn：Apple的beta为1.44，被归为高风险股票。

- argumentative_role_cn：支持投资组合构建模块根据风险偏好对推荐列表重新加权。

- remaining_uncertainty_cn：beta阈值1.25/0.75是主观设定；风险分类只依赖beta，未纳入用户年龄、收入等画像。

- link_to_next_phase_cn：分类结果用于Table 1中的风险权重，进而生成低/中/高风险推荐列表。

##### evidence_pointers

1. Section 3.6.1 Eq(10)-(11)

2. Section 4.5

3. Tables 7-8

#### 6. 推荐列表构建

- order：6

- name_cn：推荐列表构建

- question_cn：如何把情感、知识、影响力、财务分和风险偏好整合成最终股票推荐列表？

- inputs_and_setting_cn：前序阶段得到的各帖子情感分、四个可信度分数、FSS、时间衰减参数和PCA权重。

- designed_or_compared_object_cn：帖子重要性公式PostImportance；股票总评分；低/中/高风险三种推荐列表。

- baseline_control_or_counterfactual_cn：PCA确定四维可信度权重；Table 1中风险偏好权重决定组合内股票权重。

##### objective_metrics

1. Post Importance

2. 股票最终评分

3. PCA累计方差贡献

4. 推荐列表排名

- analysis_method_cn：用PCA把领域分、关键词分、名人分、评分分转化为权重；帖子重要性按时间衰减、情感、四维可信度、FSS相乘；最后按风险偏好加权排序。

- main_result_cn：生成三个推荐列表：正常风险列表为Mu、Wdc、Baba；低风险为Baba、Wdc、FB；高风险为Mu、Wdc、Appl。

- argumentative_role_cn：这是从多维信号到可执行投资组合的关节转换点，也是后续30日绩效评价的直接输入。

- remaining_uncertainty_cn：PCA权重和θ时间衰减参数在样本内确定，未做稳定性检验；没有验证最优性。

- link_to_next_phase_cn：推荐列表进入30日模拟交易并与市场指数和分层基准比较。

##### evidence_pointers

1. Section 3.6.2 Eq(13)

2. Section 4.6

3. Tables 9-12

#### 7. 30日组合绩效评价

- order：7

- name_cn：30日组合绩效评价

- question_cn：CIR推荐的组合是否在收益、风险调整收益和超额收益上优于市场指数及no-filter、knowledge-based、authority-based基准？

- inputs_and_setting_cn：推荐列表、30个交易日的每日回报、S&P500日回报、无风险国库券利率、各组合beta。

- designed_or_compared_object_cn：CIR组合与no-filter、knowledge-based、authority-based三种基准组合进行比较；外部参照为S&P500。

- baseline_control_or_counterfactual_cn：no-filter代表仅靠情感；knowledge-based代表仅用领域+关键词；authority-based代表仅用名人+评分；S&P500代表市场平均。

##### objective_metrics

1. 30日累计回报

2. 每日回报路径

3. Treynor比率

4. Jensen alpha

- analysis_method_cn：模拟交易30日计算组合收益；用Treynor公式评估单位市场风险的超额回报；用Jensen公式比较实际收益与CAPM预期收益。

- main_result_cn：标准风险下CIR回报30.369%，no-filter -27.550%、knowledge 16.180%、authority 2.168%，S&P500 -0.806%；CIR的Treynor和Jensen也最优，Jensen为正而其他为负。

- argumentative_role_cn：这是全文核心证据：证明整合多维可信度的集体智慧推荐优于单纯情感、单一知识、单一权威和市场指数。

- remaining_uncertainty_cn：只有单一30日窗口；无显著性检验；未考虑交易成本、滑点和流动性；部分收益可能来自特定市场窗口。

- link_to_next_phase_cn：为验证定制化决策支持，需要在不同风险偏好组合中重复同样的绩效比较。

##### evidence_pointers

1. Section 5.1

2. Table 13

3. Figs. 5-11

4. Eqs.(16)-(18)

#### 8. 定制化推荐列表评价

- order：8

- name_cn：定制化推荐列表评价

- question_cn：按用户风险偏好定制后的CIR组合是否仍然优于各类基准？

- inputs_and_setting_cn：低风险、正常风险、高风险三种推荐列表；Table 1中的风险权重；与阶段7相同的收益、Treynor、Jensen指标。

- designed_or_compared_object_cn：低、高、正常风险偏好下的CIR组合，与对应风险偏好下的no-filter、knowledge-based、authority-based组合比较。

- baseline_control_or_counterfactual_cn：同一风险加权方案下的三个基准组合。

##### objective_metrics

1. Return

2. Treynor

3. Jensen

- analysis_method_cn：按风险偏好对股票分数乘权重后重新排序成组合，再计算30日绩效三指标。

- main_result_cn：CIR在低风险和正常风险组合中三个指标均最好；高风险组合中CIR与authority-based表现相同；总体来看CIR在风险中性用户中最佳。

- argumentative_role_cn：把核心结论从单一组合扩展到个性化场景，强化决策支持系统的实用价值。

- remaining_uncertainty_cn：Table 15显示高风险组合CIR和authority-based完全相同，说明在该偏好下CIR没有增量优势；未纳入用户画像。

- link_to_next_phase_cn：定制化结果支撑讨论部分的贡献主张，并引出局限与未来研究。

##### evidence_pointers

1. Section 5.2

2. Tables 14-16

3. Figs. 12-14

## 各部分修辞架构

### abstract_moves

1. CONTEXT: 社交媒体成为个人投资经验分享渠道

2. PHENOMENON: 社交投资平台允许复制经验投资者的投资组合

3. RQ_OR_OBJECTIVE: 提出集体智慧机制提取并整合平台观点生成组合

4. RESULT: CIR跑赢市场指数和基准方法

### introduction_moves

1. CONTEXT: 负利率使人们从储蓄转向投资

2. PRACTICAL_STAKES: 散户平均收益低于市场指数

3. PHENOMENON: 买高和过度反应两种非理性行为

4. PRIOR_KNOWLEDGE: 70%用户信任陌生在线评论，众包投资提升收益

5. PHENOMENON: eToro等社交投资平台的复制策略

6. LIMITATION: 平台信息过载，跟随高绩效者并不能保证获利

7. GAP: 现有投资决策支持系统很少分析社交平台投资者评论

8. RQ_OR_OBJECTIVE: 提出基于社交平台集体智慧的股票组合推荐机制

9. STUDY_OVERVIEW: 预告全文结构

### theory_and_knowledge_moves

1. PRIOR_KNOWLEDGE: 集体智慧可预测股票回报并跑赢市场

2. PRIOR_KNOWLEDGE: 平台帖子情感与交易量、波动率、回报相关

3. THEORY_PROPOSITION: 正面观点将反映于未来股票表现

4. PRIOR_KNOWLEDGE: 现有DSS可用技术分析、财报、新闻，但较少使用社交投资平台评论

5. REQUIREMENT: 使用文本挖掘预处理步骤并构建特征词典

6. REQUIREMENT: 用情感分析和意见挖掘提取公众情绪

### artifact_design_moves

1. DESIGN_FEATURE: 四步流程涵盖风险偏好识别、集体智慧抽取、评分整合、定制推荐

2. DESIGN_FEATURE: 六模块系统架构

3. DESIGN_FEATURE: 特征词典构建

4. DESIGN_FEATURE: 情感分析模块的金融情感与Textblob平均

5. DESIGN_FEATURE: 知识分析中的领域分和关键词分

6. DESIGN_FEATURE: 影响力分析中的名人分和评分分

7. DESIGN_FEATURE: 财务报表分析的八比率FSS

8. DESIGN_FEATURE: 用beta和Table 1风险权重定制组合

### evaluation_moves

1. METHOD_JUSTIFICATION: 选择eToro实验平台并聚焦股票类别

2. METHOD_JUSTIFICATION: 用Loughran-McDonald加Textblob提升情感判断

3. METHOD_JUSTIFICATION: 用PCA确定四维可信度权重

4. BENCHMARK_OR_CONTRAST: 设立S&P500和no-filter/knowledge/authority三种基准

5. RESULT: CIR在累计收益上领先

6. RESULT: CIR在Treynor和Jensen上领先

7. RESULT: 定制化组合中CIR总体最好

### discussion_and_contribution_moves

1. TRANSITION: 重新概述机制和实验

2. CONTRIBUTION: 从系统开发、数据源、方法论、实践、金融五个方面声明贡献

3. BOUNDARY_CONDITION: eToro单平台、科技股、固定数据时间、未考虑用户画像

4. LIMITATION_AND_FUTURE: 增加特征选择方法、机器学习算法、移动交易、因果方向研究

## 理论/知识到设计的翻译

### 知识/理论基础

1. 行为金融学中的非理性投资行为

2. 集体智慧/众包预测

3. 投资决策支持系统文献

4. 文本挖掘与情感分析文献

5. 社会网络影响力分析

6. 财务报表分析

7. 投资组合理论与风险调整绩效衡量

- 理论—设计耦合：partial

- 耦合判定理由：集体智慧、情感预测、来源可信度等文献为系统架构提供了问题依据和模块方向，但关键设计选择（TF-IDF前500词、领域分/关键词分/名人分/评分分的操作化、PCA权重、beta阈值、Table 1风险权重）多为工程启发或数据驱动决定，没有从单一正式理论推导出来。

- 理论到设计翻译链：行为金融文献说明散户会因买高和过度反应而跑输市场，因此需要避免情绪化的决策支持；集体智慧文献说明大量投资者意见比单一专家更有效，因此应该利用社交投资平台帖子；情感分析和文本挖掘文献说明评论情绪可预测股价，因此需要把文本转为情感分数；社会影响和来源可信度文献说明意见价值取决于作者知识和权威，因此需要领域分、关键词分、名人分、评分分；财务报表文献说明标的自身质量也应纳入评分，因此加入FSS；投资组合理论和beta说明风险和偏好需要匹配，因此设置风险权重。所有环节最终汇总为PostImportance公式，用PCA加权生成推荐列表。

### mapping_table

#### 1. 1

- theory_or_knowledge_claim_cn：集体智慧能预测股票表现，众包组合可跑赢市场指数

- mechanism_cn：大量投资者独立意见汇聚后能抵消个体噪声，形成优于单一专家的判断

- design_requirement_cn：推荐机制必须从社交平台大量帖子中聚合意见而不是只跟随少数高绩效者

- artifact_choice_cn：以eToro帖子为数据源，按标的汇总所有帖子重要性分数生成组合

- evaluated_contrast_cn：CIR聚合全部帖子与单纯跟随市场、单纯跟随高绩效者相比

- objective_result_cn：CIR组合30日回报30.369%，远高于S&P500的-0.806%及authority-based的2.168%

##### evidence_pointers

1. Section 1 P4

2. Table 13

3. Section 5.1.1

#### 2. 2

- theory_or_knowledge_claim_cn：正面情绪预测未来股票回报

- mechanism_cn：乐观帖子反映投资者对标的未来现金流的积极预期，情绪信号会部分转化为价格变动

- design_requirement_cn：必须量化每条帖子对标的的正面或负面态度

- artifact_choice_cn：用Loughran-McDonald词表和Textblob计算综合情感分数

- evaluated_contrast_cn：no-filter基准只使用情感分数与加入可信度过滤的CIR比较

- objective_result_cn：纯情感no-filter亏损27.55%，而加入可信度过滤的CIR盈利30.369%

##### evidence_pointers

1. Section 2.4

2. Section 3.2

3. Table 13

#### 3. 3

- theory_or_knowledge_claim_cn：帖子的价值取决于作者的领域知识和内容专业性，而非单纯发帖数量

- mechanism_cn：有历史交易经验和帖子关键词相关性的作者更可能提供有效投资洞见

- design_requirement_cn：需要评估作者对标的类别的交易集中度和帖子关键词密度

- artifact_choice_cn：领域分用历史交易类别比例，关键词分用句子中含特征词典关键词的比例

- evaluated_contrast_cn：knowledge-based基准只用领域+关键词，与只用情感和只用权威比较

- objective_result_cn：knowledge-based回报16.18%，高于authority-based的2.168%和no-filter的-27.55%

##### evidence_pointers

1. Section 3.3

2. Section 5.1.1

3. Table 13

#### 4. 4

- theory_or_knowledge_claim_cn：社交网络上的权威和评分是信息可信度的重要来源

- mechanism_cn：被更多人关注、评论和点赞的作者更具社会影响力，其意见更可能被市场参与者采纳

- design_requirement_cn：需要计算显式社会链接和隐式评论链接，并让专家点赞权重更高

- artifact_choice_cn：名人分由关注者数和评论数归一化合成；评分分用点赞者的利润比率加权

- evaluated_contrast_cn：authority-based基准只用名人+评分，与no-filter/knowledge/CIR比较

- objective_result_cn：authority-based回报2.168%，优于no-filter但劣于knowledge-based和CIR

##### evidence_pointers

1. Section 3.4

2. Table 13

#### 5. 5

- theory_or_knowledge_claim_cn：基本面健康的公司更可能产生稳健回报

- mechanism_cn：盈利能力、营运效率、资本结构和流动性共同反映企业内在质量，可降低仅凭舆论带来的风险

- design_requirement_cn：投资标的评分必须纳入公司财务健康度

- artifact_choice_cn：用八个财务比率平均得到的FSS作为PostImportance的乘数

- evaluated_contrast_cn：没有单独做去掉FSS的消融，只在完整CIR中作为乘数

- objective_result_cn：CIR整体表现最佳，但无法分离FSS的具体增量贡献

##### evidence_pointers

1. Section 3.5

2. Section 4.4

3. Table 6

#### 6. 6

- theory_or_knowledge_claim_cn：投资者风险偏好应影响资产配置，高beta股票风险更高需更高权重匹配风险偏好

- mechanism_cn：beta衡量股票对市场波动的敏感度，按风险偏好加权可让组合与用户风险承受力一致

- design_requirement_cn：系统需要把股票分成风险组并为不同风险用户生成不同组合

- artifact_choice_cn：用beta阈值1.25/0.75分类股票；Table 1定义低/正常/高风险组合权重

- evaluated_contrast_cn：低风险、高风险、正常风险三类组合下比较CIR与基准

- objective_result_cn：CIR在低风险和正常风险组合绩效最好；高风险组合CIR与authority-based相同

##### evidence_pointers

1. Section 3.6.1

2. Tables 14-16

## 评价逻辑

### evaluation_modes

1. 30日模拟交易

2. 市场指数对照

3. 消融式基准对照

4. 风险调整绩效指标

5. 按风险偏好定制组合的重复比较

6. PCA权重确定

- why_these_evaluations_cn：作者需要同时回答三层问题：制品是否跑赢大盘、整合多维信息是否优于单一信息维度、按用户偏好定制是否仍然有效。因此不能只用准确率或单次收益，必须同时使用市场基准、成分消融式基准、风险调整指标和定制化场景。

- benchmark_and_contrast_chain_cn：基准链按信息复杂度递增：S&P500是外部市场底线；no-filter代表纯情感信号；knowledge-based增加作者领域和关键词；authority-based增加社交影响和评分；CIR把所有维度整合。这样从外到内逐步证明每个信息层面的增量作用，并最终表明只有完整CIR才能取得最优绩效。

### claim_evidence_ledger

#### 1. CIR组合在市场收益上优于S&P500和三个基准

- claim_cn：CIR组合在市场收益上优于S&P500和三个基准

- evidence_cn：Table 13中CIR 30日回报30.369%，S&P500为-0.806%，no-filter -27.550%，knowledge 16.180%，authority 2.168%

- status_cn：支持，但仅单一时段且无显著性检验

#### 2. 整合知识、权威和情感比单一维度更好

- claim_cn：整合知识、权威和情感比单一维度更好

- evidence_cn：CIR回报高于knowledge-based和authority-based；no-filter最差

- status_cn：支持，但属于聚合对照，未对四个维度做独立消融

#### 3. CIR在风险调整后仍优于其他方法

- claim_cn：CIR在风险调整后仍优于其他方法

- evidence_cn：Fig.10 Treynor和Fig.11 Jensen显示CIR最高，且Jensen为正，其他为负

- status_cn：支持，但缺少置信区间和统计检验

#### 4. 按风险偏好定制的组合依然保持优势

- claim_cn：按风险偏好定制的组合依然保持优势

- evidence_cn：Tables 14-16显示低风险和正常风险CIR三指标最优；高风险组合CIR与authority-based相同

- status_cn：部分支持；高风险组合没有增量优势

#### 5. 正面情绪能预测股票表现

- claim_cn：正面情绪能预测股票表现

- evidence_cn：no-filter纯情感基准亏损，而包含情感加权的CIR盈利

- status_cn：未被直接验证；情感信号只在组合中有效

#### 6. 财务报表分析改善了推荐

- claim_cn：财务报表分析改善了推荐

- evidence_cn：FSS被纳入PostImportance公式，但没有去掉FSS的对照实验

- status_cn：未被独立检验

#### 7. 该机制能帮助投资者避免非理性行为

- claim_cn：该机制能帮助投资者避免非理性行为

- evidence_cn：仅从机制设计上推断集体智慧可以减少情绪化决策

- status_cn：没有用户行为数据，属于概念性主张

- internal_validity_strategy_cn：通过在同一30日窗口、同一市场指数、同一数据源下比较CIR与多个层次化基准，构造了类似消融的逻辑；使用Treynor和Jensen控制市场风险；用PCA而非主观指定四维权重。但在统计上未做显著性检验，也未做滚动窗或交叉验证，因此内部有效性有限。

- external_validity_strategy_cn：使用真实社交投资平台eToro上的927条帖子、真实WRDS财务数据和Yahoo Finance市场价格，并覆盖低、正常、高三种风险偏好组合，增强了对现实决策场景的代表性；但作者自己也承认只选科技股、单一平台、固定时间窗口，限制了外推。

- what_is_not_actually_tested_cn：没有直接检验CIR与各组件之间的因果机制；没有验证FSS单独贡献；没有测试不同θ、不同PCA权重、不同风险加权表的稳健性；没有做样本外或多时期验证；没有考虑交易成本、滑点、流动性和用户行为；高风险组合中CIR与authority-based相同，说明并非在所有风险偏好下都有优势。

## 贡献闭环

- technical_claim_cn：提出的CIR方法在30日模拟交易中产生更高的绝对回报、Treynor比率和Jensen alpha，优于S&P500及no-filter、knowledge-based、authority-based方法。

- artifact_claim_cn：把帖子情感、作者领域知识、关键词相关性、社交权威、评分者绩效和公司财务指标整合进PostImportance公式，构造出可用的投资组合推荐制品；通过分层基准比较证明该制品的组合设计是绩效改善来源。

- mechanism_claim_cn：为什么CIR有效，是因为它在意见聚合中加入了投资者可信度过滤：知识比权威更能带来稳定收益，而完整多维融合优于单一维度；这使系统能在海量评论中找出有信息量的专家意见。

- boundary_claim_cn：机制在eToro平台、2016年12月至2017年3月、科技股和非英语评论被过滤的条件下有效；对不同风险偏好定制组合时，低风险和正常风险下CIR最优，高风险下与authority-based持平。

- reusable_design_knowledge_cn：投资推荐系统可以按‘帖子情感×作者可信度×标的财务质量×风险偏好’的评分框架设计；作者可信度应同时包含历史交易领域集中度、内容关键词密度、社交影响力和点赞者历史绩效；绩效评价需要同时报告市场回报、Treynor和Jensen。

- theoretical_contribution_cn：把集体智慧和来源可信度理论延伸到社交投资平台场景，利用可追踪真实交易记录的投资者的评论构造金融集体智慧，并整合多种文本和社交特征；不过文章没有修改或扩展正式理论模型，主要是应用型贡献。

- how_discussion_closes_intro_gap_cn：讨论开始重新引入负利率和收益焦虑，随后概述CIR流程并强调实验在收益、Treynor、Jensen上的优势；在贡献部分第一条直接回应引言中‘现有DSS很少分析社交平台投资者评论’的缺口，说明本系统首次使用可追踪真实交易的eToro评论来生成投资决策。

- overclaim_or_unsupported_leaps_cn：文章整体上存在几个跳跃：从单次30日绩效跳到‘更有利可图’；把组合绩效优势归因于集体智慧机制，但没有排除偶然市场窗口；Table 15显示高风险CIR与authority-based完全相同却仍宣称全面最好；FSS贡献无消融证据却纳入贡献；‘避免非理性行为’和‘降低风险’更多是概念性声明而非检验结果。

## 句级写作动作图谱

### 1. Abstract P1 S1-S2

- order：1

- section：Abstract

- locator：Abstract P1 S1-S2

- move_code：CONTEXT

- paraphrase_cn：现在人们更多通过社交媒体分享个人投资经验。

- rhetorical_function_cn：开篇建立社交平台作为投资信息源的现实背景。

- depends_on_cn：无。

- sets_up_cn：引出后续用户生成数据对组合构建有用的前提。

- evidence_pointer：Abstract第一句

### 2. Abstract P1 S3

- order：2

- section：Abstract

- locator：Abstract P1 S3

- move_code：PHENOMENON

- paraphrase_cn：允许投资者复制经验投资者组合的新型投资平台快速兴起。

- rhetorical_function_cn：把社交平台背景收窄到社交投资平台这一具体现象。

- depends_on_cn：依赖社交媒体分享经验的背景。

- sets_up_cn：为集体智慧机制提供应用场景。

- evidence_pointer：Abstract第二句

### 3. Abstract P1 S4

- order：3

- section：Abstract

- locator：Abstract P1 S4

- move_code：RQ_OR_OBJECTIVE

- paraphrase_cn：本研究提出一种集体智慧机制，通过分析投资平台上其他投资者的知识、权威和观点来生成合适的投资组合。

- rhetorical_function_cn：一句话概括核心研究目标和制品。

- depends_on_cn：依赖前两句提出的平台现象。

- sets_up_cn：为摘要中的实验结果做铺垫。

- evidence_pointer：Abstract第三句

### 4. Abstract P1 S5

- order：4

- section：Abstract

- locator：Abstract P1 S5

- move_code：RESULT

- paraphrase_cn：在eToro.com上的实验显示，提出机制推荐的组合在市场指数和多种基准方法上表现更好。

- rhetorical_function_cn：用实验结论支撑机制价值。

- depends_on_cn：依赖研究目标和实验数据。

- sets_up_cn：给读者留下制品有效的最初印象。

- evidence_pointer：Abstract末句

### 5. Introduction P1 S1-S3

- order：5

- section：Introduction

- locator：Introduction P1 S1-S3

- move_code：CONTEXT

- paraphrase_cn：过去人们把闲置资金存入银行赚利息，但现在负利率政策使储蓄失去吸引力。

- rhetorical_function_cn：建立宏观金融环境变化，说明投资需求上升。

- depends_on_cn：无。

- sets_up_cn：引出散户投资行为问题的现实重要性。

- evidence_pointer：Introduction第一段

### 6. Introduction P1 S4-S6

- order：6

- section：Introduction

- locator：Introduction P1 S4-S6

- move_code：PRACTICAL_STAKES

- paraphrase_cn：尽管S&P500近20年年均回报9.85%，普通股票型基金投资者仅获得5.19%，投资者行为常受情绪影响。

- rhetorical_function_cn：用收益差距说明非理性行为导致巨大现实损失。

- depends_on_cn：依赖负利率背景下投资重要性。

- sets_up_cn：为决策支持系统的必要性提供问题基础。

- evidence_pointer：Introduction第一段后半

### 7. Introduction P2 S1-S3

- order：7

- section：Introduction

- locator：Introduction P2 S1-S3

- move_code：PHENOMENON

- paraphrase_cn：导致投资者跑输市场的两种行为是买高和过度反应。

- rhetorical_function_cn：具体化非理性行为机制。

- depends_on_cn：依赖上一句投资者平均收益低的现实。

- sets_up_cn：说明需要技术工具避免情绪化决策。

- evidence_pointer：Introduction第二段

### 8. Introduction P3 S1-S5

- order：8

- section：Introduction

- locator：Introduction P3 S1-S5

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：Web2.0使更多人用社交平台表达经验；Nielsen调查显示70%的人信任陌生人在线评论。

- rhetorical_function_cn：引入在线评论作为可靠信息源。

- depends_on_cn：前面非理性问题需要信息解决方案。

- sets_up_cn：为社交投资平台的意见挖掘提供依据。

- evidence_pointer：Introduction第三段

### 9. Introduction P4 S1-S4

- order：9

- section：Introduction

- locator：Introduction P4 S1-S4

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：麻省理工研究表明众包投资提升回报，且已有基于群众智慧的ETF。

- rhetorical_function_cn：用具体研究和产品说明集体智慧投资可行。

- depends_on_cn：依赖在线评论可信这一前提。

- sets_up_cn：为使用社交平台帖子构建推荐机制提供合法性。

- evidence_pointer：Introduction第四段

### 10. Introduction P5 S1-S6

- order：10

- section：Introduction

- locator：Introduction P5 S1-S6

- move_code：PHENOMENON

- paraphrase_cn：社交投资平台如eToro允许用户复制经验投资者，OpenBook有450万交易者社区。

- rhetorical_function_cn：描述现实可用的数据平台和跟投现象。

- depends_on_cn：依赖众包智慧投资可行。

- sets_up_cn：引出eToro作为实验平台。

- evidence_pointer：Introduction第五段

### 11. Introduction P6 S1-S3

- order：11

- section：Introduction

- locator：Introduction P6 S1-S3

- move_code：LIMITATION

- paraphrase_cn：平台信息太多，新手难以理解；跟随受欢迎投资者也可能亏损，因为高绩效者也有非理性行为。

- rhetorical_function_cn：否定简单跟投和人工浏览的解决方案。

- depends_on_cn：依赖eToro平台丰富但庞杂的信息环境。

- sets_up_cn：为自动集体智慧机制创造缺口。

- evidence_pointer：Introduction第六段

### 12. Introduction P7 S1-S3

- order：12

- section：Introduction

- locator：Introduction P7 S1-S3

- move_code：GAP

- paraphrase_cn：投资决策支持系统范围很广，但很少有系统分析社交投资平台上的投资者评论来产生投资决策，而研究显示这类评论有洞见价值。

- rhetorical_function_cn：明确指出文献和制品缺口。

- depends_on_cn：依赖前面对社交平台评论价值的论证。

- sets_up_cn：直接支撑本文研究目标。

- evidence_pointer：Introduction第七段

### 13. Introduction P7 S4

- order：13

- section：Introduction

- locator：Introduction P7 S4

- move_code：RQ_OR_OBJECTIVE

- paraphrase_cn：因此本文提出基于社交平台集体智慧的股票组合推荐机制。

- rhetorical_function_cn：正式提出研究问题和制品。

- depends_on_cn：依赖缺口句。

- sets_up_cn：为后文系统框架提供方向。

- evidence_pointer：Introduction第七段中

### 14. Introduction P8

- order：14

- section：Introduction

- locator：Introduction P8

- move_code：STUDY_OVERVIEW

- paraphrase_cn：预告论文结构：文献、系统框架、数据与实验、结果讨论、贡献与局限。

- rhetorical_function_cn：提供全文路标。

- depends_on_cn：无。

- sets_up_cn：组织读者预期。

- evidence_pointer：Introduction末尾

### 15. Section 2.1 P1-P2

- order：15

- section：Related Literature

- locator：Section 2.1 P1-P2

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：已有研究显示众包选股和CAPS组合能跑赢市场指数。

- rhetorical_function_cn：建立集体智慧的预测可信度。

- depends_on_cn：引言中众包投资证据。

- sets_up_cn：为用社交平台帖子做集体智慧抽取提供文献支持。

- evidence_pointer：Section 2.1

### 16. Section 2.1 P3

- order：16

- section：Related Literature

- locator：Section 2.1 P3

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：平台数据研究显示社交媒体意见能预测股票回报和收益意外。

- rhetorical_function_cn：把集体智慧从选股系统延伸到社交媒体文本。

- depends_on_cn：依赖众包预测可靠。

- sets_up_cn：为情感分析模块提供依据。

- evidence_pointer：Section 2.1后半

### 17. Section 2.1末尾

- order：17

- section：Related Literature

- locator：Section 2.1末尾

- move_code：REQUIREMENT

- paraphrase_cn：因此本研究从投资平台目标论坛的帖子中提取集体情绪状态，为不同风险偏好投资者构建组合。

- rhetorical_function_cn：把文献知识转化为制品的数据源和功能需求。

- depends_on_cn：依赖社交文本预测股票回报的证据。

- sets_up_cn：引出系统框架中的情感和论坛数据处理。

- evidence_pointer：Section 2.1最后一句

### 18. Section 2.2 P1-P3

- order：18

- section：Related Literature

- locator：Section 2.2 P1-P3

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：文献中有遗传算法、神经网络、多代理等投资DSS，但通常使用市场信息、公司财务和新闻评论。

- rhetorical_function_cn：总结投资DSS现状，为缺口做铺垫。

- depends_on_cn：前面集体智慧讨论。

- sets_up_cn：指出社交投资平台评论作为数据源未被充分使用。

- evidence_pointer：Section 2.2

### 19. Section 2.2末尾

- order：19

- section：Related Literature

- locator：Section 2.2末尾

- move_code：GAP

- paraphrase_cn：本研究使用文本挖掘和集体智慧，从社交投资平台帖子及重要投资者行为中提炼建议，以解决组合选择问题。

- rhetorical_function_cn：把DSS文献缺口和本文方法对接。

- depends_on_cn：依赖前面对现有DSS数据源的局限。

- sets_up_cn：为系统框架中的模块选择提供理由。

- evidence_pointer：Section 2.2末句

### 20. Section 2.3 P1-P3

- order：20

- section：Related Literature

- locator：Section 2.3 P1-P3

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：文本挖掘通常包括市场数据收集、预处理和机器学习算法；预处理包含特征选择、降维和特征表示。

- rhetorical_function_cn：为后续预处理和词典构建提供标准流程。

- depends_on_cn：无。

- sets_up_cn：支撑系统框架中的特征词典构建模块。

- evidence_pointer：Section 2.3

### 21. Section 2.3末尾

- order：21

- section：Related Literature

- locator：Section 2.3末尾

- move_code：REQUIREMENT

- paraphrase_cn：本研究将实施特征选择、降维和特征表示的预处理步骤来分析投资者帖子。

- rhetorical_function_cn：把文本挖掘流程转化为制品实现要求。

- depends_on_cn：依赖前面对文本挖掘流程的总结。

- sets_up_cn：为4.1节具体预处理操作铺垫。

- evidence_pointer：Section 2.3末

### 22. Section 2.4 P1

- order：22

- section：Related Literature

- locator：Section 2.4 P1

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：情感分析或意见挖掘常被用于收集和分析在线评论以辅助决策。

- rhetorical_function_cn：把情感分析引入系统工具集。

- depends_on_cn：无。

- sets_up_cn：引出情感分析模块。

- evidence_pointer：Section 2.4第一句

### 23. Section 2.4末尾

- order：23

- section：Related Literature

- locator：Section 2.4末尾

- move_code：HYPOTHESIS_OR_PROPOSITION

- paraphrase_cn：根据以往研究，积极观点将乐观地反映在未来股票表现上。

- rhetorical_function_cn：提出可操作假设支撑情感分数进入最终评分。

- depends_on_cn：依赖Twitter/Yahoo情感预测研究。

- sets_up_cn：为情感分数作为PostImportance乘数提供依据。

- evidence_pointer：Section 2.4末

### 24. Section 3 Step 1

- order：24

- section：System Framework

- locator：Section 3 Step 1

- move_code：DESIGN_FEATURE

- paraphrase_cn：系统第一步要求投资者根据风险偏好选择投资标的，偏好被分为风险偏好者、风险中性和风险厌恶者。

- rhetorical_function_cn：说明系统面向个性化使用的起点。

- depends_on_cn：依赖文献中风险偏好对投资的重要性。

- sets_up_cn：为后面beta分类和Table 1权重埋下伏笔。

- evidence_pointer：Section 3 Step1

### 25. Section 3 Step2-Step4

- order：25

- section：System Framework

- locator：Section 3 Step2-Step4

- move_code：STUDY_OVERVIEW

- paraphrase_cn：系统从平台帖子和历史数据中提取集体智慧，整合各标的评分并构建不同类型的投资组合，最后按风险偏好定制。

- rhetorical_function_cn：用四步流程总览制品运行逻辑。

- depends_on_cn：依赖前面提出的研究目标。

- sets_up_cn：为六大模块详细介绍提供框架。

- evidence_pointer：Section 3 Steps 2-4

### 26. Section 3 module (1)

- order：26

- section：System Framework

- locator：Section 3 module (1)

- move_code：DESIGN_FEATURE

- paraphrase_cn：特征词典构建模块从eToro各标的论坛收集帖子并构建重要词词典，用于评估帖子知识相关性。

- rhetorical_function_cn：说明系统第一个模块的数据流。

- depends_on_cn：依赖文本挖掘预处理流程。

- sets_up_cn：为关键词分提供词典。

- evidence_pointer：Section 3模块1

### 27. Section 3 module (2) & 3.2

- order：27

- section：System Framework

- locator：Section 3 module (2) & 3.2

- move_code：DESIGN_FEATURE

- paraphrase_cn：情感分析模块用Loughran-McDonald词表和Textblob识别帖子乐观或悲观。

- rhetorical_function_cn：说明如何操作化公众意见。

- depends_on_cn：依赖情感预测文献。

- sets_up_cn：为情感分数公式提供具体实现。

- evidence_pointer：Section 3模块2

### 28. Section 3 module (3) & 3.3

- order：28

- section：System Framework

- locator：Section 3 module (3) & 3.3

- move_code：DESIGN_FEATURE

- paraphrase_cn：知识分析模块用领域分和关键词分评估作者对投资目标的知识可信度。

- rhetorical_function_cn：说明权威可信度如何被操作化为两个分数。

- depends_on_cn：依赖经验投资者更有知识的假设。

- sets_up_cn：为knowledge-based基准提供成分。

- evidence_pointer：Section 3模块3

### 29. Section 3 module (4) & 3.4

- order：29

- section：System Framework

- locator：Section 3 module (4) & 3.4

- move_code：DESIGN_FEATURE

- paraphrase_cn：影响力分析模块用名人分和评分分衡量作者权威。

- rhetorical_function_cn：说明社交权威如何被纳入评分。

- depends_on_cn：依赖社交网络影响力理论。

- sets_up_cn：为authority-based基准提供成分。

- evidence_pointer：Section 3模块4

### 30. Section 3 module (5)

- order：30

- section：System Framework

- locator：Section 3 module (5)

- move_code：DESIGN_FEATURE

- paraphrase_cn：财务报表分析模块用盈利能力、营运能力、资本结构和流动性指标评估投资标的价值。

- rhetorical_function_cn：在社交媒体信号之外加入基本面信号。

- depends_on_cn：依赖财务分析作为投资决策的经典依据。

- sets_up_cn：为FSS公式提供指标范围。

- evidence_pointer：Section 3模块5

### 31. Section 3 module (6)

- order：31

- section：System Framework

- locator：Section 3 module (6)

- move_code：DESIGN_FEATURE

- paraphrase_cn：投资组合构建模块聚合评论观点，根据用户风险偏好生成定制推荐列表。

- rhetorical_function_cn：把各模块输出汇聚为最终制品。

- depends_on_cn：依赖前五个模块的输出。

- sets_up_cn：为3.6节的投资组合构建公式做预告。

- evidence_pointer：Section 3模块6

### 32. Section 3.1

- order：32

- section：System Framework

- locator：Section 3.1

- move_code：DESIGN_FEATURE

- paraphrase_cn：特征词典通过停用词移除、词干化和POS标注后，用TF-IDF选取重要词。

- rhetorical_function_cn：描述词典构建的具体文本处理步骤。

- depends_on_cn：依赖文本挖掘文献中的bag-of-words和TF-IDF。

- sets_up_cn：为4.1节的预处理结果提供设计蓝图。

- evidence_pointer：Section 3.1

### 33. Section 3.2 Eq(1)-(2)

- order：33

- section：System Framework

- locator：Section 3.2 Eq(1)-(2)

- move_code：DESIGN_FEATURE

- paraphrase_cn：帖子情感分数由金融情感分数与Textblob评论情感分数平均得到。

- rhetorical_function_cn：给出情感模块的可计算公式。

- depends_on_cn：依赖情感词典和Textblob工具。

- sets_up_cn：为情感分数进入最终公式建立输入。

- evidence_pointer：Section 3.2

### 34. Section 3.3.1

- order：34

- section：System Framework

- locator：Section 3.3.1

- move_code：REQUIREMENT

- paraphrase_cn：领域分根据作者历史交易中属于目标类别的比例来计算，反映其在特定领域的经验。

- rhetorical_function_cn：说明知识可信度的一种操作化方式。

- depends_on_cn：依赖交易历史可获取的平台功能。

- sets_up_cn：为领域分在实验中的计算细节铺垫。

- evidence_pointer：Section 3.3.1

### 35. Section 3.3.2

- order：35

- section：System Framework

- locator：Section 3.3.2

- move_code：MECHANISM

- paraphrase_cn：关键词分统计包含特征词典关键词的句子比例，避免仅按发帖数衡量专家度而受无意义帖子干扰。

- rhetorical_function_cn：解释为什么用内容而非数量来测知识。

- depends_on_cn：依赖特征词典模块。

- sets_up_cn：强化知识分数的内容相关性。

- evidence_pointer：Section 3.3.2

### 36. Section 3.4.1 Eq(5)-(7)

- order：36

- section：System Framework

- locator：Section 3.4.1 Eq(5)-(7)

- move_code：DESIGN_FEATURE

- paraphrase_cn：名人分由显式链接（关注者数）和隐式链接（帖子收到的评论数）加权合成。

- rhetorical_function_cn：说明社交影响力如何被数值化。

- depends_on_cn：依赖社交网络数据。

- sets_up_cn：为权威基准的celebrity score提供公式。

- evidence_pointer：Section 3.4.1

### 37. Section 3.4.2 Eq(8)

- order：37

- section：System Framework

- locator：Section 3.4.2 Eq(8)

- move_code：DESIGN_FEATURE

- paraphrase_cn：评分分用给帖子点赞的用户的利润比率来加权，认为专家点赞更有价值。

- rhetorical_function_cn：说明评价的权威性如何被历史绩效加权。

- depends_on_cn：依赖平台可追踪真实交易绩效。

- sets_up_cn：为authority-based基准提供rating score成分。

- evidence_pointer：Section 3.4.2

### 38. Section 3.6.1 Eq(10)-(11)

- order：38

- section：System Framework

- locator：Section 3.6.1 Eq(10)-(11)

- move_code：DESIGN_FEATURE

- paraphrase_cn：用beta值将股票分为高风险、正常风险和低风险三组，用于匹配用户风险偏好。

- rhetorical_function_cn：说明组合定制中如何把风险数量化。

- depends_on_cn：依赖beta作为市场波动度量。

- sets_up_cn：为Table 1风险权重和三类推荐列表做基础。

- evidence_pointer：Section 3.6.1

### 39. Section 3.6.2 Eq(13)

- order：39

- section：System Framework

- locator：Section 3.6.2 Eq(13)

- move_code：DESIGN_FEATURE

- paraphrase_cn：帖子重要性等于时间衰减后的情感分数乘以知识分、权威分、评分的加权组合，再乘以公司FSS。

- rhetorical_function_cn：给出整个制品的核心融合公式。

- depends_on_cn：依赖所有模块的输出。

- sets_up_cn：为4.6节PCA权重和推荐列表提供计算核心。

- evidence_pointer：Section 3.6.2 Eq(13)

### 40. Section 4 P1 & 4.1 Data collection

- order：40

- section：Experiments

- locator：Section 4 P1 & 4.1 Data collection

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：选择eToro作为实验平台并聚焦股票，因为股票类别多且帖子数量多；收集2016年12月至2017年3月共927条帖子。

- rhetorical_function_cn：说明数据来源和采样选择。

- depends_on_cn：需要eToro平台结构。

- sets_up_cn：为后续所有实验提供数据集。

- evidence_pointer：Section 4开头与4.1

### 41. Section 4.1 Preprocessing & Feature extraction

- order：41

- section：Experiments

- locator：Section 4.1 Preprocessing & Feature extraction

- move_code：RESULT

- paraphrase_cn：预处理后得到29,060个句子、58,863个名词、33,569个形容词和23,533个副词，并从前3,453个词中选出500个关键词。

- rhetorical_function_cn：用具体数字证明处理管道可行。

- depends_on_cn：依赖NLTK、Porter、TF-IDF实现。

- sets_up_cn：为后续词典和分数计算提供物质基础。

- evidence_pointer：Section 4.1

### 42. Section 4.2

- order：42

- section：Experiments

- locator：Section 4.2

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：为提高情感极性准确度，结合Loughran-McDonald词表和Textblob两种方法并取平均。

- rhetorical_function_cn：说明情感分数的稳健性来源。

- depends_on_cn：依赖两种情感计算工具。

- sets_up_cn：为Eq(2)在数据上的应用提供理由。

- evidence_pointer：Section 4.2

### 43. Section 4.3

- order：43

- section：Experiments

- locator：Section 4.3

- move_code：DESIGN_FEATURE

- paraphrase_cn：实验按前文公式计算每个帖子的领域分、关键词分、名人分和评分分。

- rhetorical_function_cn：把设计公式转换成实验数据计算。

- depends_on_cn：依赖3.3和3.4的公式。

- sets_up_cn：为PCA权重和推荐列表表5提供输入。

- evidence_pointer：Section 4.3

### 44. Section 4.4

- order：44

- section：Experiments

- locator：Section 4.4

- move_code：DESIGN_FEATURE

- paraphrase_cn：财务数据来自WRDS数据库，并计算八个财务比率得到FSS。

- rhetorical_function_cn：说明FSS的数据来源和计算方式。

- depends_on_cn：依赖3.5财务模块定义。

- sets_up_cn：为Table 6提供实际财务分。

- evidence_pointer：Section 4.4

### 45. Section 4.5

- order：45

- section：Experiments

- locator：Section 4.5

- move_code：DESIGN_FEATURE

- paraphrase_cn：用Yahoo Finance取得Apple和S&P500数据，计算Apple beta为1.44，属于高风险。

- rhetorical_function_cn：示范beta计算在单个股票上的结果。

- depends_on_cn：依赖3.6.1 beta公式。

- sets_up_cn：为Table 8和风险列表提供实例。

- evidence_pointer：Section 4.5

### 46. Section 4.6

- order：46

- section：Experiments

- locator：Section 4.6

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：使用主成分分析确定领域、关键词、名人、评分四个因素的权重。

- rhetorical_function_cn：用数据驱动方法替代主观权重。

- depends_on_cn：依赖四个可信度分数已有。

- sets_up_cn：为最终推荐列表的生成提供权重。

- evidence_pointer：Section 4.6 Table 9

### 47. Section 4.6末尾 Tables 10-12

- order：47

- section：Experiments

- locator：Section 4.6末尾 Tables 10-12

- move_code：RESULT

- paraphrase_cn：最终生成正常风险、低风险和高风险三张推荐列表，首选股票分别为Mu/Wdc/Baba、Baba/Wdc/FB、Mu/Wdc/Appl。

- rhetorical_function_cn：展示制品输出。

- depends_on_cn：依赖PCA权重和风险权重。

- sets_up_cn：作为30日绩效评价的输入。

- evidence_pointer：Tables 10-12

### 48. Section 5开头

- order：48

- section：Results and Evaluation

- locator：Section 5开头

- move_code：BENCHMARK_OR_CONTRAST

- paraphrase_cn：选择S&P500作为市场指数，并选择no-filter、knowledge-based、authority-based作为基准方法，分别对应纯情感、知识、权威三类推荐逻辑。

- rhetorical_function_cn：建立外部市场和内部消融的对比框架。

- depends_on_cn：依赖文献中已有情感、知识、权威预测方法。

- sets_up_cn：为实验结论提供参照系。

- evidence_pointer：Section 5第一段

### 49. Section 5.1.1 Table 13

- order：49

- section：Results and Evaluation

- locator：Section 5.1.1 Table 13

- move_code：RESULT

- paraphrase_cn：30日累计回报显示CIR为30.369%，远高于S&P500的-0.806%、no-filter的-27.550%、knowledge的16.180%和authority的2.168%。

- rhetorical_function_cn：给出核心绩效证据。

- depends_on_cn：依赖30日模拟交易和基准链。

- sets_up_cn：支撑后文风险调整指标的讨论。

- evidence_pointer：Table 13

### 50. Section 5.1.1 Fig.5-9之后

- order：50

- section：Results and Evaluation

- locator：Section 5.1.1 Fig.5-9之后

- move_code：MECHANISM

- paraphrase_cn：作者解释知识型基准优于权威型基准，是因为更多领域知识代表投资者是相应领域专家，更可能分享更好的投资策略。

- rhetorical_function_cn：为绩效差异提供机制解释。

- depends_on_cn：依赖knowledge和authority的结果差异。

- sets_up_cn：强调内容知识比社交权威更重要。

- evidence_pointer：Section 5.1.1

### 51. Section 5.1.2 Fig.10

- order：51

- section：Results and Evaluation

- locator：Section 5.1.2 Fig.10

- move_code：RESULT

- paraphrase_cn：Treynor比率结果表明no-filter最差，CIR明显优于其他方法。

- rhetorical_function_cn：用风险调整收益复核绩效优势。

- depends_on_cn：依赖Treynor公式和30日组合beta。

- sets_up_cn：为Jensen alpha的比较提供一致性。

- evidence_pointer：Fig.10

### 52. Section 5.1.3 Fig.11

- order：52

- section：Results and Evaluation

- locator：Section 5.1.3 Fig.11

- move_code：RESULT

- paraphrase_cn：Jensen alpha显示CIR为正，其他方法为负，说明CIR获得异常正收益。

- rhetorical_function_cn：用CAPM超额收益概念强化经济价值。

- depends_on_cn：依赖Jensen公式和组合beta。

- sets_up_cn：为贡献部分‘更有利可图’提供依据。

- evidence_pointer：Fig.11

### 53. Section 5.2

- order：53

- section：Results and Evaluation

- locator：Section 5.2

- move_code：RESULT

- paraphrase_cn：按低、高、正常风险偏好定制的组合中，CIR在多数指标和多数组合中仍是最好的，其中风险中性投资者表现最佳。

- rhetorical_function_cn：把核心结论扩展到个性化定制场景。

- depends_on_cn：依赖Table 1风险权重和30日绩效。

- sets_up_cn：为讨论部分的实用贡献提供证据。

- evidence_pointer：Section 5.2 Tables 14-16

### 54. Discussion P1-P2

- order：54

- section：Discussion and Conclusion

- locator：Discussion P1-P2

- move_code：TRANSITION

- paraphrase_cn：面对负利率时代，本文提出基于社交平台集体智慧的组合推荐机制，并用实验证明其在收益、Treynor和Jensen上持续优于基准。

- rhetorical_function_cn：从结果返回整体问题，重新叙述文章主线。

- depends_on_cn：依赖实验结论。

- sets_up_cn：引出贡献和局限。

- evidence_pointer：Section 6开头

### 55. Section 6.1

- order：55

- section：Discussion and Conclusion

- locator：Section 6.1

- move_code：CONTRIBUTION

- paraphrase_cn：从系统开发、数据源、方法论、实践和金融五个方面声明贡献，包括首个基于社交投资平台评论的投资DSS、可追踪真实交易的投资者数据、五维可信度整合、帮助新手处理信息过载、避免非理性行为。

- rhetorical_function_cn：集中回应引言中的缺口并放大贡献。

- depends_on_cn：依赖实验证据和系统设计。

- sets_up_cn：为后续局限与未来研究做铺垫。

- evidence_pointer：Section 6.1

### 56. Section 6.2-6.3

- order：56

- section：Discussion and Conclusion

- locator：Section 6.2-6.3

- move_code：LIMITATION_AND_FUTURE

- paraphrase_cn：局限包括只用eToro、集中科技股、固定时间数据、未考虑用户基本画像；未来可探索其他特征选择、机器学习算法、移动交易和舆论与价格波动因果方向。

- rhetorical_function_cn：划定边界并保持学术克制。

- depends_on_cn：依赖本文实验设计。

- sets_up_cn：为后续研究留下空间。

- evidence_pointer：Section 6.2-6.3

## 写作技术

- gap_construction_cn：文章用三层嵌套构造缺口：先给宏观绩效缺口（散户跑输市场），再给平台数据潜力（众包智慧有效），最后给制品缺口（现有DSS很少分析社交投资平台评论）。缺口的最终形式是‘现有制品不能充分利用可追踪真实交易投资者的社交平台评论’。

- signposting_cn：引言末有全文结构预告；系统框架用四步流程和六大模块编号指引；每个实验小节标题本身就是状态标签；评价部分明确列出基准名单和三个绩效指标，帮助读者追踪。

- transition_logic_cn：每个模块都会在末尾说明输出给下一模块；每个实验结果之后用一句话解释为什么会有这种差异；Discussion重新回到引言中的负利率和绩效缺口。

- claim_evidence_rhythm_cn：先给出公式和模块设计作为‘如何做’，再在实验部分以数据表和图表作为‘效果如何’，最后在贡献部分把结果提升为‘为什么有价值’；在结果段落中频繁使用表格数值和图形指认。

- benchmark_narrative_cn：benchmark被设计成逐步增加信息维度的故事：no-filter代表最原始情感，knowledge增加内容知识，authority增加社交影响，CIR代表完整集体智慧；读者可以从CIR与每个基准的差距中感知每个维度的贡献。

- theory_return_cn：文章在结果解释中使用‘知识型专家分享更好洞见’来连接集体智慧和知识管理；在贡献部分回引‘集体智慧’和‘避免非理性行为’，使数据结果从单纯绩效变成对集体智慧理念的支持。

- contribution_positioning_cn：贡献被拆成五个视角（系统、数据、方法、实践、金融），每个视角都对应一个具体设计选择或实验发现，再用引言中的缺口做锚点，从而避免贡献退化为‘我们做了个系统并且效果不错’。

- novelty_protection_cn：通过分层基准和风险调整指标，把CIR与纯情感、纯知识、纯权威拉开差距；通过在3.6.2中整合四维分数和FSS，强调是组合设计产生了优势；在讨论中反复强调可追踪真实交易的社交投资平台这一独特数据源，防止文章被读成普通文本情绪选股。

## 可复用研究与写作程序

### structure_steps

#### 1. 1

- step：1

- writing_job_cn：建立现实投资绩效缺口：引用负利率、散户平均收益和市场指数收益差。

- research_job_cn：找到可用统计数据支撑‘投资者决策需要帮助’的问题。

- required_evidence_cn：至少一个市场收益对照数据和行为金融依据。

- transition_to_next_cn：用‘尽管有社交平台，但信息过载’过渡到新数据机会。

#### 2. 2

- step：2

- writing_job_cn：介绍社交投资平台现象和众包智慧证据，说明平台上有大量可挖掘的投资者经验。

- research_job_cn：收集平台规模、用户行为研究或众包预测证据。

- required_evidence_cn：平台存在性和集体智慧有效性的文献或调查。

- transition_to_next_cn：用‘但平台信息太多、跟随高手并不够’制造新缺口。

#### 3. 3

- step：3

- writing_job_cn：以‘现有DSS很少使用社交投资平台评论’作为研究缺口，并给出研究目标。

- research_job_cn：检索投资DSS文献，确认没有或很少采用该数据源。

- required_evidence_cn：文献综述能显示数据源空白。

- transition_to_next_cn：用‘因此我们提出机制’切换到系统设计。

#### 4. 4

- step：4

- writing_job_cn：按模块描述制品：文本处理、情感、知识、权威、财务、组合构建。

- research_job_cn：实现每个模块的关键公式，并说明输入输出。

- required_evidence_cn：公式可计算、模块间数据流清晰。

- transition_to_next_cn：用‘为了验证机制，我们用eToro数据实验’转向评价。

#### 5. 5

- step：5

- writing_job_cn：描述数据收集、预处理、特征提取和基准设置。

- research_job_cn：采集真实平台数据，计算各分项得分和推荐列表。

- required_evidence_cn：数据量、预处理结果表和推荐列表。

- transition_to_next_cn：用‘我们交易30日并观察日收益变化’进入绩效评价。

#### 6. 6

- step：6

- writing_job_cn：使用市场基准和消融式基准报告收益、Treynor和Jensen，并按风险偏好重复比较。

- research_job_cn：运行模拟交易和风险调整指标计算。

- required_evidence_cn：多指标绩效对照表。

- transition_to_next_cn：用‘结果证明CIR更好’回到贡献和局限。

#### 7. 7

- step：7

- writing_job_cn：在Discussion中重新连接引言缺口，分条列出贡献并明确边界与未来工作。

- research_job_cn：从证据中提炼可复用设计知识，诚实列出未验证部分。

- required_evidence_cn：贡献与实验证据对应，局限真实。

- transition_to_next_cn：未来工作自然从局限中产生。

### most_transferable_moves_cn

1. 用真实市场数据制造绩效缺口再引入新数据源

2. 用模块化系统框架把多维信号组织为可计算流程

3. 使用no-filter/knowledge/authority/CIR的分层基准模拟消融

4. 同时报告绝对收益、Treynor和Jensen以强化稳健性

5. 把推荐列表按风险偏好拆成低/中/高三组，扩展适用场景

6. 在贡献部分按系统、数据、方法、实践、金融逐层声明价值

### resource_intensive_or_nonstandard_parts_cn

1. 需要接入eToro这类社交投资平台的用户帖子、历史交易、关注关系、评论关系、点赞者和点赞者利润比率，普通研究者难以获得同等数据

2. 需要WRDS数据库获取公司财务比率

3. 需要Yahoo Finance等历史价格数据并计算beta

4. 平台用户真实交易记录和利润比率是文章中评分分和领域分的关键，无法仅凭公开帖子复制

5. 30日模拟交易虽不需要真实资金，但需要一套完整的市场数据管道

### what_not_to_copy_superficially_cn

1. 不能只套用‘集体智慧’和‘情感+知识+权威’术语而不提供分层基准

2. 不能只报告累计收益而不报告Treynor和Jensen，否则无法支撑风险调整优势

3. 不能用PCA权重却不说清四维分数的含义和数据来源

4. 不能在高风险组合CIR与authority-based相同的情况下仍声称全面显著更优

5. 没有真实交易可追踪数据时，不能照搬评分分用利润比率加权的设计

- single_best_description_of_the_routine_cn：以投资绩效缺口为起点，用社交投资平台上的帖子作为数据源，把情感、作者知识、影响力和公司基本面组合成一个可解释的推荐评分，再通过去掉成分的基准对照和风险调整指标证明组合优于单一维度与市场。

## 分析边界

本文基于用户提供的Markdown全文进行分析，部分公式和图（如Eq.9附近、Fig.1/Fig.2）在转换中可能存在排版断裂或细节缺失；所有位置证据来自章节标题、公式编号和表图编号，未对照PDF原始页码；未访问原始数据，因此无法验证实验数值的统计显著性。
