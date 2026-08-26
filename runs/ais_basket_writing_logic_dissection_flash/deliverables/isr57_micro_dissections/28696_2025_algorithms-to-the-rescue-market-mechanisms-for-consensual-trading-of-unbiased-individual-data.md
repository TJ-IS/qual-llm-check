# Algorithms to the Rescue: Market Mechanisms for Consensual Trading of Unbiased Individual Data：ISR 句段级微观图谱

- 作者：Brian Birkhead; Ashkan Eshghi; Ram D. Gopal; Hooman Hidaji; Raymond A. Patterson
- 年份：2025
- DOI：10.1287/isre.2024.1115
- 源文件：28696_2025_algorithms-to-the-rescue-market-mechanisms-for-consensual-trading-of-unbiased-individual-data.md
- 置信度：0.72

## 核实后的宏观骨架

全文采用'问题-文献缺口-机制设计-最坏情形理论分析-仿真与真实数据验证-部分信息比较-结论'的论证结构。摘要先给出背景与现有平台两类机制缺陷，再提出算法化市场机制RSP，随后给出比固定补偿和集中优化更优的核心结果，并预告偏差-成本、样本量和匿名性洞见。引言从现实场景出发，用互联网规模、第三方追踪、隐私工具偏差、监管变化建立问题紧迫性，接着介绍新兴数据市场与现有固定补偿/集中优化缺陷，再概述本文机制、合作企业、理论比较路线和贡献。文献综述在定价端、集中优化端、差分隐私端、联合补偿-估计端分别划界，最终把独特贡献定位为'产生无偏样本而非无偏估计'。第3节建立平台、数据主体效用、k-anonymity和隐私成本模型；第4节依次设计第二补偿拍卖、排序相邻配对采样、RSP市场机制；第5节在最坏情形（完全相关）下推导SRS、FCH/FCL、RSP的偏差、总补偿、排除率、不平等指标和闭式结果，并给出RSP支配固定补偿、总成本优势、样本量影响等命题；第6节用完美相关仿真、TOST检验、不完美相关扫描、beta分布稳健性、真实企业调查数据验证；第7节把平台部分信息建模为区间不确定性，证明现实人口规模下平台应放弃部分信息估计而直接使用RSP；第8节重述问题、贡献、实践含义、边界和未来研究。

## 摘要逐句图谱

### 1. Abstract P1 S1

- order：1

- locator：Abstract P1 S1

- paraphrase_cn：在线经济长期依赖收集和变现用户个人数据，以换取工具和服务。

- move_code：CONTEXT

- statement_status：fact

- why_here_cn：开篇把研究置于一个读者熟悉且规模巨大的现实背景中，避免从抽象机制开始。

- inherits_from_previous_cn：摘要首句，不需要承接。

- changes_argument_state_cn：建立数据市场的存在与基本交换逻辑。

- sets_up_next_cn：为下一句指出现有交换逻辑的缺陷提供背景。

- failure_if_removed_cn：缺少后读者不知道论文为何要讨论个人数据交易。

- evidence_pointer：Abstract P1 S1

### 2. Abstract P1 S2

- order：2

- locator：Abstract P1 S2

- paraphrase_cn：不透明和缺少适当补偿机制已逐渐侵蚀该市场的数据质量，催生新一代平台中介数据市场，明确向数据主体报销其数据。

- move_code：LIMITATION

- statement_status：author_inference

- why_here_cn：把背景转成需要解决的问题，并引出本文针对的平台类型。

- inherits_from_previous_cn：承接在线经济依赖个人数据的前提。

- changes_argument_state_cn：指出现状失败，并聚焦到平台中介数据市场。

- sets_up_next_cn：为下一句扩展这些平台的应用场景。

- failure_if_removed_cn：缺少后论文问题动机不完整，RSP机制缺乏要解决的问题。

- evidence_pointer：Abstract P1 S2

### 3. Abstract P1 S3

- order：3

- locator：Abstract P1 S3

- paraphrase_cn：这些平台还可创建从用户直接收集数据的数据市场，用于调查和医疗研究等场景。

- move_code：CONTEXT

- statement_status：fact

- why_here_cn：扩大机制适用场景，说明问题不限于广告数据经纪。

- inherits_from_previous_cn：承接平台中介数据市场这一概念。

- changes_argument_state_cn：把应用场景扩展到直接数据收集。

- sets_up_next_cn：为下一句指出这些平台仍使用两类缺陷机制。

- failure_if_removed_cn：缺少后会显得问题仅限在线广告，削弱ISR相关性和贡献宽度。

- evidence_pointer：Abstract P1 S3

### 4. Abstract P1 S4

- order：4

- locator：Abstract P1 S4

- paraphrase_cn：这类平台使用集中优化或固定补偿机制，导致数据买方面对昂贵和/或有偏的样本。

- move_code：LIMITATION

- statement_status：author_inference

- why_here_cn：直接给出本文要超越的两类现成机制及其失败后果。

- inherits_from_previous_cn：依赖前面指出的平台类型。

- changes_argument_state_cn：建立现有技术的双缺陷：贵或偏。

- sets_up_next_cn：为提出本文机制创造差额。

- failure_if_removed_cn：缺少后本文机制没有明确的竞争对象。

- evidence_pointer：Abstract P1 S4

### 5. Abstract P1 S5

- order：5

- locator：Abstract P1 S5

- paraphrase_cn：本文提出一种算法化市场机制，将激励相容补偿机制与新型采样方法结合，使平台能向买方提供低成本无偏样本，同时适当补偿数据主体的隐私损失。

- move_code：RQ_OR_OBJECTIVE

- statement_status：author_inference

- why_here_cn：摘要核心句，宣告制品、方法组合和三个目标。

- inherits_from_previous_cn：依赖固定补偿/集中优化的双缺陷。

- changes_argument_state_cn：从指出现状缺陷转向给出本文方案。

- sets_up_next_cn：为下面性能结果提供主语。

- failure_if_removed_cn：缺少后摘要没有研究主张，后续结果句无对象。

- evidence_pointer：Abstract P1 S5

### 6. Abstract P2 S1

- order：6

- locator：Abstract P2 S1

- paraphrase_cn：我们展示该市场机制相对当前方法的优越性能。

- move_code：RESULT

- statement_status：empirical_result

- why_here_cn：以概括句开启结果部分，提示下面给出具体优势。

- inherits_from_previous_cn：承接所提出的机制。

- changes_argument_state_cn：把研究从设计转向证据。

- sets_up_next_cn：为紧随其后的两个具体结果句做引导。

- failure_if_removed_cn：缺少后摘要结果部分缺乏过渡。

- evidence_pointer：Abstract P2 S1

### 7. Abstract P2 S2

- order：7

- locator：Abstract P2 S2

- paraphrase_cn：我们发现本文方法优于固定补偿；即使平台拥有数据主体隐私顾虑的部分信息，实践上也应放弃该信息而采用本文方法。

- move_code：RESULT

- statement_status：empirical_result

- why_here_cn：摘要最强结果，同时覆盖固定补偿和集中优化两个对手，并给出反直觉建议。

- inherits_from_previous_cn：继承上一句的优越性能声明。

- changes_argument_state_cn：把'优越'具体化为两个可比较的对手。

- sets_up_next_cn：为结论和正文第7节埋下伏笔。

- failure_if_removed_cn：缺少后摘要失去最强卖点，也削弱实践贡献。

- evidence_pointer：Abstract P2 S2

### 8. Abstract P2 S3

- order：8

- locator：Abstract P2 S3

- paraphrase_cn：最后我们提供关于样本中偏差与成本权衡、以及样本量和匿名性影响的洞见。

- move_code：RESULT

- statement_status：author_inference

- why_here_cn：列出辅助贡献，拓宽论文的理论价值。

- inherits_from_previous_cn：依赖机制设计和比较分析。

- changes_argument_state_cn：从两个直接比较结果扩展为一般性洞见。

- sets_up_next_cn：为正文中样本量、k-anonymity和Proposition 4做预告。

- failure_if_removed_cn：缺少后摘要只强调赢过对手，显得像算法竞赛而非IS知识贡献。

- evidence_pointer：Abstract P2 S3

## 引言逐句图谱

### 1. Introduction P1 S1

- order：1

- locator：Introduction P1 S1

- paraphrase_cn：在定向广告以及调查和医疗研究等涉及个体数据收集的应用中，需要同意且透明的代表性用户数据收集。

- move_code：CONTEXT

- statement_status：fact

- why_here_cn：引言首句把问题定义为跨应用的一般需求，而非单一平台问题。

- inherits_from_previous_cn：引言起点，不承接摘要。

- changes_argument_state_cn：建立研究想要满足的规范性条件：同意、透明、代表性。

- sets_up_next_cn：为提出算法化市场机制做铺垫。

- failure_if_removed_cn：缺少后论文没有明确需求起点，后面所有缺陷无靶心。

- evidence_pointer：Introduction P1 S1

### 2. Introduction P1 S2

- order：2

- locator：Introduction P1 S2

- paraphrase_cn：我们提出一种算法化市场机制方法，以低成本实现这一目标。

- move_code：RQ_OR_OBJECTIVE

- statement_status：author_inference

- why_here_cn：在一句话内先给出论文方案，随后再回头讲现状缺陷，形成先扬后抑结构。

- inherits_from_previous_cn：承接对同意、透明、代表性数据的需求。

- changes_argument_state_cn：直接宣布本文解决方案。

- sets_up_next_cn：为下一句转向当前方法的缺点做转折。

- failure_if_removed_cn：缺少后引言开头没有研究主张。

- evidence_pointer：Introduction P1 S2

### 3. Introduction P1 S3

- order：3

- locator：Introduction P1 S3

- paraphrase_cn：我们首先描述当前数据收集方法的缺点。

- move_code：ROADMAP

- statement_status：author_inference

- why_here_cn：给读者阅读路线，使P1-P5的现状批评有明确目的。

- inherits_from_previous_cn：承接本文方案。

- changes_argument_state_cn：把写作组织为'先说缺陷再说方案'。

- sets_up_next_cn：引导下面数据规模和第三方追踪的段落。

- failure_if_removed_cn：缺少后读者会困惑为何大段介绍现状。

- evidence_pointer：Introduction P1 S3

### 4. Introduction P2 S1

- order：4

- locator：Introduction P2 S1

- paraphrase_cn：当前在线经济很大程度上建立在用户愿意以个人数据交换在线服务的基础上。

- move_code：CONTEXT

- statement_status：fact

- why_here_cn：建立数据供应的基本制度性事实。

- inherits_from_previous_cn：承接摘要和引言开头的数据需求。

- changes_argument_state_cn：为市场规模和问题严重性提供基础。

- sets_up_next_cn：为接下来的互联网用户数和数据量数据做铺垫。

- failure_if_removed_cn：缺少后数据市场规模叙述缺少起点。

- evidence_pointer：Introduction P2 S1

### 5. Introduction P2 S2

- order：5

- locator：Introduction P2 S2

- paraphrase_cn：互联网的广泛使用为公司在线上收集用户数据创造了大量机会。

- move_code：CONTEXT

- statement_status：fact

- why_here_cn：把数据收集从个别服务扩展为普遍企业行为。

- inherits_from_previous_cn：承接用户用数据换服务的模型。

- changes_argument_state_cn：说明数据收集的普遍性和规模。

- sets_up_next_cn：为具体统计数字做铺垫。

- failure_if_removed_cn：缺少后市场规模数据显得突兀。

- evidence_pointer：Introduction P2 S2

### 6. Introduction P2 S3

- order：6

- locator：Introduction P2 S3

- paraphrase_cn：2020年全球约有49亿活跃互联网用户，创造了约64泽字节数据。

- move_code：CONTEXT

- statement_status：fact

- why_here_cn：用硬数据建立问题量级。

- inherits_from_previous_cn：依赖互联网广泛使用。

- changes_argument_state_cn：把个人数据从常识性话题变成统计级现象。

- sets_up_next_cn：为定义'个体数据'提供事实基础。

- failure_if_removed_cn：缺少后市场规模论述缺乏可信度。

- evidence_pointer：Introduction P2 S3

### 7. Introduction P2 S4

- order：7

- locator：Introduction P2 S4

- paraphrase_cn：这些数据被称为个体数据，包括人口统计、偏好、在线行为、购买模式和位置等信息，用户被称为数据主体。

- move_code：DEFINITION

- statement_status：fact

- why_here_cn：在规模数据之后给出全文核心术语的精确定义。

- inherits_from_previous_cn：承接前述海量数据。

- changes_argument_state_cn：界定研究对象为个体级数据而非聚合统计。

- sets_up_next_cn：为说明这些数据对企业价值做铺垫。

- failure_if_removed_cn：缺少后术语'个体数据'和'数据主体'缺乏根基。

- evidence_pointer：Introduction P2 S4

### 8. Introduction P2 S5

- order：8

- locator：Introduction P2 S5

- paraphrase_cn：这些数据对企业具有巨大潜在价值，用于瞄准和触达潜在客户、获取新客户、建立忠诚、预测需求和开发个性化产品。

- move_code：CONTEXT

- statement_status：fact

- why_here_cn：解释需求端为什么愿意为数据付费。

- inherits_from_previous_cn：依赖个体数据定义。

- changes_argument_state_cn：建立数据市场的经济价值端。

- sets_up_next_cn：为市场价值数字做铺垫。

- failure_if_removed_cn：缺少后数据市场价值缺少需求端解释。

- evidence_pointer：Introduction P2 S5

### 9. Introduction P2 S6

- order：9

- locator：Introduction P2 S6

- paraphrase_cn：这导致对个体数据的需求激增，2024年该市场价值约2700亿美元。

- move_code：CONTEXT

- statement_status：fact

- why_here_cn：用市场价值证明问题重要性，为ISR读者建立商业利害关系。

- inherits_from_previous_cn：承接企业数据价值论述。

- changes_argument_state_cn：把数据收集问题提升为千亿美元级市场问题。

- sets_up_next_cn：引出第三方经纪人的收集行为。

- failure_if_removed_cn：缺少后论文问题的重要性不够突出。

- evidence_pointer：Introduction P2 S6

### 10. Introduction P3 S1

- order：10

- locator：Introduction P3 S1

- paraphrase_cn：个体数据收集主要由第三方经纪商完成，它们跨网站、应用、社交媒体和电商平台追踪用户浏览行为，在用户缺乏真实且明确知情同意的情况下收集数据。

- move_code：PHENOMENON

- statement_status：fact

- why_here_cn：指出现实中最主要的数据收集方式是隐蔽的，构成论文第一个问题。

- inherits_from_previous_cn：承接数据市场巨大需求。

- changes_argument_state_cn：把需求引向不透明收集实践。

- sets_up_next_cn：为引用文献说明收集过程浑浊。

- failure_if_removed_cn：缺少后论文没有第三方经纪人这一现实靶子。

- evidence_pointer：Introduction P3 S1

### 11. Introduction P3 S2

- order：11

- locator：Introduction P3 S2

- paraphrase_cn：已有研究表明第三方数据收集过程至多算是浑浊不清的。

- move_code：PRIOR_LITERATURE

- statement_status：prior_literature

- why_here_cn：用IS文献支撑隐蔽收集的判断，避免自说自话。

- inherits_from_previous_cn：承接第三方追踪描述。

- changes_argument_state_cn：把一个现象判断升级为文献共识。

- sets_up_next_cn：为数据被用于算法产品做铺垫。

- failure_if_removed_cn：缺少后隐蔽收集只是作者断言，缺乏学理支持。

- evidence_pointer：Introduction P3 S2

### 12. Introduction P3 S3

- order：12

- locator：Introduction P3 S3

- paraphrase_cn：这种暗中收集的数据常被输入机器学习算法，用于消费者画像、市场细分、受众定向和定制市场洞察等产品。

- move_code：CONTEXT

- statement_status：fact

- why_here_cn：说明问题数据最终进入经济决策，扩大后果。

- inherits_from_previous_cn：依赖文献支持的收集过程。

- changes_argument_state_cn：把数据质量问题与下游商业应用连接。

- sets_up_next_cn：为数据主体未获补偿做铺垫。

- failure_if_removed_cn：缺少后数据收集问题与商业后果脱节。

- evidence_pointer：Introduction P3 S3

### 13. Introduction P3 S4

- order：13

- locator：Introduction P3 S4

- paraphrase_cn：数据主体很少因其数据被使用或因隐私损失获得补偿。

- move_code：LIMITATION

- statement_status：fact

- why_here_cn：直接指出现行机制的补偿缺失，是论文要解决的核心缺口之一。

- inherits_from_previous_cn：依赖数据被收集和出售的事实。

- changes_argument_state_cn：引入补偿不公这一规范性维度。

- sets_up_next_cn：为数据主体使用隐私工具提供动机。

- failure_if_removed_cn：缺少后论文缺少从'不透明'到'无激励'的关键链接。

- evidence_pointer：Introduction P3 S4

### 14. Introduction P3 S5

- order：14

- locator：Introduction P3 S5

- paraphrase_cn：引用多个文献说明数据主体很少因数据使用或隐私损失获得补偿。

- move_code：PRIOR_LITERATURE

- statement_status：prior_literature

- why_here_cn：把补偿缺失从断言变成有文献支持的事实。

- inherits_from_previous_cn：承接上一句的补偿缺失主张。

- changes_argument_state_cn：提升补偿缺失的学术可信度。

- sets_up_next_cn：为下一段数据主体觉醒做铺垫。

- failure_if_removed_cn：缺少后补偿缺失缺乏权威支撑。

- evidence_pointer：Introduction P3 S5

### 15. Introduction P4 S1

- order：15

- locator：Introduction P4 S1

- paraphrase_cn：历史上数据主体愿意无直接补偿交出私人信息，但现在正迅速意识到共享信息的隐私风险。

- move_code：CONTEXT

- statement_status：fact

- why_here_cn：用时间对比解释用户行为为何开始变化。

- inherits_from_previous_cn：承接补偿缺失。

- changes_argument_state_cn：从静态问题转向动态用户觉醒。

- sets_up_next_cn：为数据主体使用隐私工具做心理动机铺垫。

- failure_if_removed_cn：缺少后隐私工具使用缺乏行为动机。

- evidence_pointer：Introduction P4 S1

### 16. Introduction P4 S2

- order：16

- locator：Introduction P4 S2

- paraphrase_cn：缺乏适当补偿促使隐私敏感的数据主体通过隐私工具保护数据。

- move_code：MECHANISM

- statement_status：author_inference

- why_here_cn：把'缺乏补偿'与'隐私工具使用'建立因果链。

- inherits_from_previous_cn：依赖数据主体对隐私风险的觉醒。

- changes_argument_state_cn：引入隐私工具作为中间机制。

- sets_up_next_cn：为隐私工具使用统计做铺垫。

- failure_if_removed_cn：缺少后从风险意识到工具使用缺因果桥梁。

- evidence_pointer：Introduction P4 S2

### 17. Introduction P4 S3

- order：17

- locator：Introduction P4 S3

- paraphrase_cn：Cisco 2021报告86%在线用户在意数据隐私，79%愿意行动，47%实际采取行动保护隐私。

- move_code：FACT

- statement_status：fact

- why_here_cn：用行业调查量化隐私关注和行动，建立现象普遍性。

- inherits_from_previous_cn：承接隐私工具使用主张。

- changes_argument_state_cn：把隐私行动从假设变为大规模事实。

- sets_up_next_cn：为VPN和广告拦截的具体使用数据做铺垫。

- failure_if_removed_cn：缺少后数据主体行动只是估计。

- evidence_pointer：Introduction P4 S3

### 18. Introduction P4 S4

- order：18

- locator：Introduction P4 S4

- paraphrase_cn：另外来源称1.05亿美国成年网民使用VPN，近47%网民使用广告拦截器。

- move_code：FACT

- statement_status：fact

- why_here_cn：提供具体工具使用规模，说明隐私工具不是边缘行为。

- inherits_from_previous_cn：承接用户行动数据。

- changes_argument_state_cn：把隐私行动具体化为VPN和广告拦截。

- sets_up_next_cn：为隐私工具造成样本偏差做铺垫。

- failure_if_removed_cn：缺少后隐私工具使用缺乏可感规模。

- evidence_pointer：Introduction P4 S4

### 19. Introduction P4 S5

- order：19

- locator：Introduction P4 S5

- paraphrase_cn：隐私工具的使用如同过滤器限制数据经纪商触达，给数据集引入显著偏差，隐私不敏感者被过度代表。

- move_code：MECHANISM

- statement_status：author_inference

- why_here_cn：这是从用户行为到数据质量的关键因果机制，解释隐私工具为何造成市场问题。

- inherits_from_previous_cn：依赖隐私工具使用规模。

- changes_argument_state_cn：把隐私工具使用转化为样本偏差机制。

- sets_up_next_cn：为相关性导致代表性缺失做铺垫。

- failure_if_removed_cn：缺少后论文无法建立隐私态度与样本偏差的联系。

- evidence_pointer：Introduction P4 S5

### 20. Introduction P4 S6

- order：20

- locator：Introduction P4 S6

- paraphrase_cn：由于隐私敏感性与个体数据相关，隐私敏感者不参与导致数据缺乏代表性。

- move_code：MECHANISM

- statement_status：author_inference

- why_here_cn：把样本偏差与数据内容本身连接，说明偏差不是随机的而会影响代表性和价值。

- inherits_from_previous_cn：依赖隐私工具过滤器机制。

- changes_argument_state_cn：引入隐私与数据相关性，为后文机制设计核心假设奠基。

- sets_up_next_cn：为广告ROI负面证据做铺垫。

- failure_if_removed_cn：缺少后相关系的理论和模型基础不存在。

- evidence_pointer：Introduction P4 S6

### 21. Introduction P4 S7

- order：21

- locator：Introduction P4 S7

- paraphrase_cn：Neumann 2019表明在线广告投资回报率常为负，主要原因就是依赖根本性差且不准确的数据。

- move_code：FACT

- statement_status：fact

- why_here_cn：用下游经济后果证明偏差问题有真实商业成本。

- inherits_from_previous_cn：承接代表性缺失。

- changes_argument_state_cn：把偏差从统计问题升级为经济问题。

- sets_up_next_cn：为法规变化作为另一重压力做铺垫。

- failure_if_removed_cn：缺少后数据质量问题的商业严重性不足。

- evidence_pointer：Introduction P4 S7

### 22. Introduction P5 S1

- order：22

- locator：Introduction P5 S1

- paraphrase_cn：除上述缺陷外，现行市场结构难以适应全球各地严格的数据获取和使用监管，如GDPR和CCPA。

- move_code：LIMITATION

- statement_status：fact

- why_here_cn：引入制度压力，使问题不仅是市场效率而且是合规。

- inherits_from_previous_cn：承接前面对数据质量问题的论述。

- changes_argument_state_cn：把个人数据市场问题从经济层扩展到法律层。

- sets_up_next_cn：为监管要求同意做铺垫。

- failure_if_removed_cn：缺少后本文的同意和透明贡献失去制度背景。

- evidence_pointer：Introduction P5 S1

### 23. Introduction P5 S2

- order：23

- locator：Introduction P5 S2

- paraphrase_cn：此类监管要求在收集个体数据前获得数据主体直接同意，并对使用、存储和共享有明确限制，使现行范式更加混乱。

- move_code：LIMITATION

- statement_status：fact

- why_here_cn：解释监管为何无法被现有隐蔽收集模式满足。

- inherits_from_previous_cn：依赖GDPR/CCPA引入。

- changes_argument_state_cn：把合规要求具体化为同意和使用限制。

- sets_up_next_cn：为第三方cookie限制做铺垫。

- failure_if_removed_cn：缺少后监管压力变得空泛。

- evidence_pointer：Introduction P5 S2

### 24. Introduction P5 S3

- order：24

- locator：Introduction P5 S3

- paraphrase_cn：再加上第三方追踪cookie限制即将实施，个人数据市场的运作方式显然需要根本性变革。

- move_code：TRANSITION

- statement_status：fact

- why_here_cn：把五个问题段落收束为一个变革需求，为数据市场平台和本文机制过渡。

- inherits_from_previous_cn：依赖监管和cookie限制。

- changes_argument_state_cn：结束问题描述，开启方案部分。

- sets_up_next_cn：引出1.1节新兴数据市场。

- failure_if_removed_cn：缺少后引言从问题直接跳到方案，缺乏转折。

- evidence_pointer：Introduction P5 S3

### 25. Introduction 1.1 P1 S1

- order：25

- locator：Introduction 1.1 P1 S1

- paraphrase_cn：针对上述问题，一个新市场已出现，旨在同意地收集个体数据并适当补偿数据主体。

- move_code：PHENOMENON

- statement_status：fact

- why_here_cn：说明论文不是讨论空想平台，而是已有现实中介。

- inherits_from_previous_cn：依赖根本变革需要。

- changes_argument_state_cn：从市场缺陷转向新兴对策。

- sets_up_next_cn：为列举平台类型做铺垫。

- failure_if_removed_cn：缺少后数据市场平台没有现实出处。

- evidence_pointer：Introduction 1.1 P1 S1

### 26. Introduction 1.1 P1 S2

- order：26

- locator：Introduction 1.1 P1 S2

- paraphrase_cn：这一新兴市场中，平台以数据可携等主要服务附带付费补偿，如mydex、digi.me、meeco、dataswift。

- move_code：PHENOMENON

- statement_status：fact

- why_here_cn：给出第一类平台案例。

- inherits_from_previous_cn：承接新兴市场出现。

- changes_argument_state_cn：区分补偿为次要活动的平台类型。

- sets_up_next_cn：为第二类直接付费平台做对照。

- failure_if_removed_cn：缺少后数据市场经济类型不完整。

- evidence_pointer：Introduction 1.1 P1 S2

### 27. Introduction 1.1 P1 S3

- order：27

- locator：Introduction 1.1 P1 S3

- paraphrase_cn：其他平台如Reklaim、citizenme、BIGtoken、getmyslice创建数字市场，用户数据被售出时直接获补偿。

- move_code：PHENOMENON

- statement_status：fact

- why_here_cn：给出第二类直接补偿平台案例，是本文机制的最近实践形态。

- inherits_from_previous_cn：承接新兴市场。

- changes_argument_state_cn：建立直接向用户付费的平台类型。

- sets_up_next_cn：为买方构成做铺垫。

- failure_if_removed_cn：缺少后固定补偿机制缺少现实载体。

- evidence_pointer：Introduction 1.1 P1 S3

### 28. Introduction 1.1 P1 S4

- order：28

- locator：Introduction 1.1 P1 S4

- paraphrase_cn：买方通常是广告商和营销商，提供B2B数据增强、合规、跨设备身份管理等服务。

- move_code：CONTEXT

- statement_status：fact

- why_here_cn：说明买方是谁，为后文买方样本需求提供角色。

- inherits_from_previous_cn：依赖平台类型。

- changes_argument_state_cn：界定数据市场的需求端。

- sets_up_next_cn：为平台应用场景做补充。

- failure_if_removed_cn：缺少后买方目标不清晰。

- evidence_pointer：Introduction 1.1 P1 S4

### 29. Introduction 1.1 P1 S5

- order：29

- locator：Introduction 1.1 P1 S5

- paraphrase_cn：这些平台还用于网红活动和优惠券定向活动。

- move_code：CONTEXT

- statement_status：fact

- why_here_cn：进一步扩展平台应用场景。

- inherits_from_previous_cn：依赖买方服务类型。

- changes_argument_state_cn：提示机制用途广泛。

- sets_up_next_cn：为下一句总结现有机制缺陷做铺垫。

- failure_if_removed_cn：缺少后平台场景稍显狭窄。

- evidence_pointer：Introduction 1.1 P1 S5

### 30. Introduction 1.1 P1 S6

- order：30

- locator：Introduction 1.1 P1 S6

- paraphrase_cn：该领域公司依赖固定价格补偿机制或基于数据主体隐私顾虑部分信息的集中优化。

- move_code：LIMITATION

- statement_status：fact

- why_here_cn：一句话把当前平台归入两类机制，直接对应后文基准。

- inherits_from_previous_cn：依赖全部平台案例。

- changes_argument_state_cn：把现实做法抽象为固定补偿和集中优化。

- sets_up_next_cn：为1.1节继续扩展调查和医疗场景做铺垫。

- failure_if_removed_cn：缺少后论文缺少从现实平台到机制模型的桥梁。

- evidence_pointer：Introduction 1.1 P1 S6

### 31. Introduction 1.1 P2 S1

- order：31

- locator：Introduction 1.1 P2 S1

- paraphrase_cn：低成本无偏数据收集的挑战不限于在线广告，还延伸到直接向用户收集数据。

- move_code：CONTEXT

- statement_status：fact

- why_here_cn：把机制适用范围从广告扩展到调查和医疗。

- inherits_from_previous_cn：依赖前面对数据市场平台的描述。

- changes_argument_state_cn：扩大问题覆盖面。

- sets_up_next_cn：为调查平台例子做铺垫。

- failure_if_removed_cn：缺少后问题显得仅限广告经纪。

- evidence_pointer：Introduction 1.1 P2 S1

### 32. Introduction 1.1 P2 S2

- order：32

- locator：Introduction 1.1 P2 S2

- paraphrase_cn：例如在调查数据收集中，受访者因数据和回答得到报酬，如Google Opinion Rewards、Branded Surveys、Swagbucks等。

- move_code：PHENOMENON

- statement_status：fact

- why_here_cn：给出调查场景的固定补偿现实。

- inherits_from_previous_cn：承接直接数据收集挑战。

- changes_argument_state_cn：建立调查平台的支付实践。

- sets_up_next_cn：为说明这些公司代买方收集数据做铺垫。

- failure_if_removed_cn：缺少后调查场景缺乏具体实例。

- evidence_pointer：Introduction 1.1 P2 S2

### 33. Introduction 1.1 P2 S3

- order：33

- locator：Introduction 1.1 P2 S3

- paraphrase_cn：这些公司代买方收集数据，通过付费让用户完成调查并分享数据。

- move_code：CONTEXT

- statement_status：fact

- why_here_cn：解释调查平台的数据流和支付关系。

- inherits_from_previous_cn：依赖调查平台例子。

- changes_argument_state_cn：把调查平台纳入数据市场框架。

- sets_up_next_cn：为数据代表性和成本关键性做铺垫。

- failure_if_removed_cn：缺少后调查平台与买方需求脱节。

- evidence_pointer：Introduction 1.1 P2 S3

### 34. Introduction 1.1 P2 S4

- order：34

- locator：Introduction 1.1 P2 S4

- paraphrase_cn：数据代表性和成本是关键。当前获取个体数据的方法是为每个用户支付固定金额。

- move_code：LIMITATION

- statement_status：fact

- why_here_cn：指出调查平台使用的正是固定补偿。

- inherits_from_previous_cn：依赖调查平台数据流。

- changes_argument_state_cn：把调查和广告场景统一到固定补偿机制。

- sets_up_next_cn：为医疗平台例子做铺垫。

- failure_if_removed_cn：缺少后调查平台的机制缺陷不明确。

- evidence_pointer：Introduction 1.1 P2 S4

### 35. Introduction 1.1 P2 S5

- order：35

- locator：Introduction 1.1 P2 S5

- paraphrase_cn：医疗领域也有类似平台如Hu-manity、Nebula Genomics、DeHealth允许出售个人健康记录，但设定补偿时不考虑用户隐私顾虑，只用固定补偿或集中优化。

- move_code：PHENOMENON

- statement_status：fact

- why_here_cn：把固定补偿/集中优化问题扩展到高度敏感的医疗数据。

- inherits_from_previous_cn：承接调查平台机制缺陷。

- changes_argument_state_cn：扩大机制缺陷的后果严重性。

- sets_up_next_cn：为1.1节总结两类缺陷做铺垫。

- failure_if_removed_cn：缺少后会削弱'同意和透明'在医疗等敏感场景的紧迫性。

- evidence_pointer：Introduction 1.1 P2 S5

### 36. Introduction 1.1 P3 S1

- order：36

- locator：Introduction 1.1 P3 S1

- paraphrase_cn：本文直接针对固定补偿和基于部分信息的集中优化这两种当前方法的缺陷。

- move_code：LIMITATION

- statement_status：author_inference

- why_here_cn：把前文现实平台统一收束到论文要解决的两类机制。

- inherits_from_previous_cn：依赖全部平台案例。

- changes_argument_state_cn：从现象转向机制层面。

- sets_up_next_cn：为固定补偿缺陷的详细分析做铺垫。

- failure_if_removed_cn：缺少后1.1节没有明确总结。

- evidence_pointer：Introduction 1.1 P3 S1

### 37. Introduction 1.1 P3 S2

- order：37

- locator：Introduction 1.1 P3 S2

- paraphrase_cn：固定补偿是对所有数据主体支付固定金额，虽简单但会使隐私成本或保留价高于固定价格的数据主体不参与。

- move_code：MECHANISM

- statement_status：author_inference

- why_here_cn：精确解释固定补偿的自选择机制。

- inherits_from_previous_cn：承接两类缺陷总结。

- changes_argument_state_cn：把固定补偿的缺陷归因于保留价筛选。

- sets_up_next_cn：为自选择偏差做铺垫。

- failure_if_removed_cn：缺少后固定补偿为何有偏缺乏解释。

- evidence_pointer：Introduction 1.1 P3 S2

### 38. Introduction 1.1 P3 S3

- order：38

- locator：Introduction 1.1 P3 S3

- paraphrase_cn：这种对隐私不敏感端的自选择，在隐私顾虑与数据主体特征相关时会造成数据集显著偏差。

- move_code：MECHANISM

- statement_status：author_inference

- why_here_cn：由固定补偿筛选推出偏差结论，是论文核心机制。

- inherits_from_previous_cn：依赖保留价筛选。

- changes_argument_state_cn：建立固定补偿→偏差的因果链。

- sets_up_next_cn：为引用相关性文献做铺垫。

- failure_if_removed_cn：缺少后固定补偿缺陷缺少机制解释。

- evidence_pointer：Introduction 1.1 P3 S3

### 39. Introduction 1.1 P3 S4

- order：39

- locator：Introduction 1.1 P3 S4

- paraphrase_cn：这种相关性在数据市场文献中已被确立，如Fleischer和Lyu、Roth和Schoenebeck、Ghosh和Roth、Hwang。

- move_code：PRIOR_LITERATURE

- statement_status：prior_literature

- why_here_cn：用文献支撑相关性假设，防止机制设计被指为特例。

- inherits_from_previous_cn：承接相关性导致偏差。

- changes_argument_state_cn：把相关性的重要性从作者判断升级为文献共识。

- sets_up_next_cn：为代表性数据集的昂贵性做铺垫。

- failure_if_removed_cn：缺少后相关性假设缺乏理论根基。

- evidence_pointer：Introduction 1.1 P3 S4

### 40. Introduction 1.1 P3 S5

- order：40

- locator：Introduction 1.1 P3 S5

- paraphrase_cn：因此，要创建代表性数据集，必须把固定价格设在最高个体隐私成本之上，这使样本贵得令人却步。

- move_code：LIMITATION

- statement_status：author_inference

- why_here_cn：从固定补偿偏差推出'无偏则贵'的结论，确立偏差-成本权衡。

- inherits_from_previous_cn：依赖固定补偿筛选机制。

- changes_argument_state_cn：把固定补偿问题定位为昂贵或有偏。

- sets_up_next_cn：为集中优化的介绍做对照。

- failure_if_removed_cn：缺少后固定补偿失败的经济性不完整。

- evidence_pointer：Introduction 1.1 P3 S5

### 41. Introduction 1.1 P3 S6

- order：41

- locator：Introduction 1.1 P3 S6

- paraphrase_cn：集中优化方法利用优化和部分数据主体信息设置报酬，可能适用于拥有行为数据的平台，但在广告、调查和医疗等平台无信息时无法使用。

- move_code：LIMITATION

- statement_status：author_inference

- why_here_cn：介绍第二个对手并指出其适用性限制。

- inherits_from_previous_cn：承接固定补偿缺陷。

- changes_argument_state_cn：把集中优化限定于有信息平台。

- sets_up_next_cn：为'即使有部分信息也未必最优'做铺垫。

- failure_if_removed_cn：缺少后集中优化这条竞争路线未被介绍。

- evidence_pointer：Introduction 1.1 P3 S6

### 42. Introduction 1.1 P3 S7

- order：42

- locator：Introduction 1.1 P3 S7

- paraphrase_cn：更重要的是，即使有部分信息，集中方法也可能不是最佳数据获取方案。

- move_code：LIMITATION

- statement_status：author_inference

- why_here_cn：为后文第7节的'放弃部分信息'主张埋下伏笔。

- inherits_from_previous_cn：依赖集中优化介绍。

- changes_argument_state_cn：把集中优化的缺陷扩展为'信息未必有价值'。

- sets_up_next_cn：为1.2节提出替代机制做铺垫。

- failure_if_removed_cn：缺少后本文最强反直觉结论缺少铺垫。

- evidence_pointer：Introduction 1.1 P3 S7

### 43. Introduction 1.2 P1 S1

- order：43

- locator：Introduction 1.2 P1 S1

- paraphrase_cn：本文为这类数据市场提出一种替代补偿机制，既产生无偏样本，又对买方低成本。

- move_code：RQ_OR_OBJECTIVE

- statement_status：author_inference

- why_here_cn：在对手缺陷讲完后正式提出本文方案。

- inherits_from_previous_cn：依赖固定补偿和集中优化缺陷。

- changes_argument_state_cn：进入论文贡献段落。

- sets_up_next_cn：为与Numerous合作开发做铺垫。

- failure_if_removed_cn：缺少后1.2节没有核心主张。

- evidence_pointer：Introduction 1.2 P1 S1

### 44. Introduction 1.2 P1 S2

- order：44

- locator：Introduction 1.2 P1 S2

- paraphrase_cn：我们与初创公司Numerous Limited合作，开发了鼓励数据主体参与并获补偿的机制。

- move_code：CONTEXT

- statement_status：fact

- why_here_cn：用产业合作增强机制的现实可行性。

- inherits_from_previous_cn：承接替代机制提议。

- changes_argument_state_cn：引入产业伙伴，为后文真实数据埋下伏笔。

- sets_up_next_cn：为透明同意隐私顾虑补偿目标做铺垫。

- failure_if_removed_cn：缺少后真实数据验证缺少来源说明。

- evidence_pointer：Introduction 1.2 P1 S2

### 45. Introduction 1.2 P1 S3

- order：45

- locator：Introduction 1.2 P1 S3

- paraphrase_cn：也就是说，我们设计了克服透明度、同意、数据主体隐私顾虑与合理补偿期望等问题的市场机制。

- move_code：RQ_OR_OBJECTIVE

- statement_status：author_inference

- why_here_cn：把机制目标与引言开头的同意透明需求明确连接。

- inherits_from_previous_cn：依赖Numerous合作开发。

- changes_argument_state_cn：把技术方案上升为满足多重规范目标。

- sets_up_next_cn：为采样算法和拍卖机制做铺垫。

- failure_if_removed_cn：缺少后方案与引言需求脱节。

- evidence_pointer：Introduction 1.2 P1 S3

### 46. Introduction 1.2 P1 S4

- order：46

- locator：Introduction 1.2 P1 S4

- paraphrase_cn：我们的方法将新型采样算法与激励相容拍卖机制作为补偿方案结合。

- move_code：DESIGN_FEATURE

- statement_status：author_inference

- why_here_cn：一句话预告本文制品的两个构件。

- inherits_from_previous_cn：承接市场机制设计目标。

- changes_argument_state_cn：把抽象目标落实到'采样算法+拍卖'。

- sets_up_next_cn：为三个同时目标做铺垫。

- failure_if_removed_cn：缺少后制品的组成不明确。

- evidence_pointer：Introduction 1.2 P1 S4

### 47. Introduction 1.2 P1 S5

- order：47

- locator：Introduction 1.2 P1 S5

- paraphrase_cn：我们展示该方法能让平台同时诱导真实报告隐私顾虑、补偿隐私损失、提供无偏低成本样本。

- move_code：DESIGN_FEATURE

- statement_status：author_inference

- why_here_cn：列出机制三个功能，是全文分析的评价标准。

- inherits_from_previous_cn：依赖采样+拍卖。

- changes_argument_state_cn：建立机制的多重目标清单。

- sets_up_next_cn：为1.2节继续解释现有实践与本文差异做铺垫。

- failure_if_removed_cn：缺少后机制目标不清，后文评价指标失去对象。

- evidence_pointer：Introduction 1.2 P1 S5

### 48. Introduction 1.2 P2 S1

- order：48

- locator：Introduction 1.2 P2 S1

- paraphrase_cn：当前从数据主体购买数据的实践主要针对特定上下文或业务的查询。

- move_code：CONTEXT

- statement_status：fact

- why_here_cn：引入当前实践的对比基准。

- inherits_from_previous_cn：承接机制目标。

- changes_argument_state_cn：建立当前实践是'按查询购买'。

- sets_up_next_cn：为本文数据先期收集做对照。

- failure_if_removed_cn：缺少后本文与当前实践的差异不明确。

- evidence_pointer：Introduction 1.2 P2 S1

### 49. Introduction 1.2 P2 S2

- order：49

- locator：Introduction 1.2 P2 S2

- paraphrase_cn：在本文方法中，数据从数据主体预先收集，买方购买时自动支付补偿。

- move_code：DESIGN_FEATURE

- statement_status：author_inference

- why_here_cn：说明本文机制与查询式购买的关键差异。

- inherits_from_previous_cn：依赖当前实践描述。

- changes_argument_state_cn：引入平台自动交易的时间结构。

- sets_up_next_cn：为按隐私偏好补偿做铺垫。

- failure_if_removed_cn：缺少后自动市场机制缺乏时间结构。

- evidence_pointer：Introduction 1.2 P2 S2

### 50. Introduction 1.2 P2 S3

- order：50

- locator：Introduction 1.2 P2 S3

- paraphrase_cn：每个数据主体按隐私偏好获得补偿，使所收集数据能代表数据主体群体。

- move_code：DESIGN_FEATURE

- statement_status：author_inference

- why_here_cn：把个性化补偿与代表性连接。

- inherits_from_previous_cn：依赖自动补偿机制。

- changes_argument_state_cn：确立补偿与代表性和平共处的原则。

- sets_up_next_cn：为激励相容防止虚报做铺垫。

- failure_if_removed_cn：缺少后'按隐私偏好补偿'的目标不明确。

- evidence_pointer：Introduction 1.2 P2 S3

### 51. Introduction 1.2 P2 S4

- order：51

- locator：Introduction 1.2 P2 S4

- paraphrase_cn：激励相容机制能防止用户虚报隐私偏好来增加补偿。

- move_code：DESIGN_FEATURE

- statement_status：author_inference

- why_here_cn：预告拍卖机制的核心性质，防止个性化补偿被策略性利用。

- inherits_from_previous_cn：依赖按隐私偏好补偿。

- changes_argument_state_cn：引入策略性报告问题。

- sets_up_next_cn：为高层直觉解释做铺垫。

- failure_if_removed_cn：缺少后个性化补偿缺乏防操纵机制。

- evidence_pointer：Introduction 1.2 P2 S4

### 52. Introduction 1.2 P2 S5

- order：52

- locator：Introduction 1.2 P2 S5

- paraphrase_cn：高层直觉是如果数据主体虚报隐私偏好，其期望补偿会下降。

- move_code：MECHANISM

- statement_status：author_inference

- why_here_cn：用一句话给出激励相容为何成立的直觉。

- inherits_from_previous_cn：依赖虚报问题提出。

- changes_argument_state_cn：为Proposition 1提供读者能懂的前瞻解释。

- sets_up_next_cn：为真实报告结论做铺垫。

- failure_if_removed_cn：缺少后激励相容缺乏直观理解。

- evidence_pointer：Introduction 1.2 P2 S5

### 53. Introduction 1.2 P2 S6

- order：53

- locator：Introduction 1.2 P2 S6

- paraphrase_cn：换言之，数据主体真实报告隐私偏好符合自身利益。

- move_code：MECHANISM

- statement_status：author_inference

- why_here_cn：把上一句的负向表述转成正向结论。

- inherits_from_previous_cn：依赖虚报降低期望补偿。

- changes_argument_state_cn：确立真实报告的激励方向。

- sets_up_next_cn：为中介平台必要性做铺垫。

- failure_if_removed_cn：缺少后机制目标与后文Proposition 1的联系减弱。

- evidence_pointer：Introduction 1.2 P2 S6

### 54. Introduction 1.2 P3 S1

- order：54

- locator：Introduction 1.2 P3 S1

- paraphrase_cn：使用中介平台来收集和销售数据对聚合代表性数据至关重要，因为它实现规模经济。

- move_code：REQUIREMENT

- statement_status：author_inference

- why_here_cn：解释为何本文强调平台中介而非点对点交易。

- inherits_from_previous_cn：承接机制设计目标。

- changes_argument_state_cn：把平台定位为市场组织者。

- sets_up_next_cn：为数据主体一次设置做铺垫。

- failure_if_removed_cn：缺少后平台在机制中的角色不明确。

- evidence_pointer：Introduction 1.2 P3 S1

### 55. Introduction 1.2 P3 S2

- order：55

- locator：Introduction 1.2 P3 S2

- paraphrase_cn：数据主体无需为每个买方完成在线资料或问卷，只需在平台设置一次。

- move_code：REQUIREMENT

- statement_status：author_inference

- why_here_cn：说明平台如何降低数据主体参与成本。

- inherits_from_previous_cn：依赖规模经济论点。

- changes_argument_state_cn：把一次设置作为平台可实施性的关键。

- sets_up_next_cn：为自动交易做铺垫。

- failure_if_removed_cn：缺少后数据主体参与负担问题不受处理。

- evidence_pointer：Introduction 1.2 P3 S2

### 56. Introduction 1.2 P3 S3

- order：56

- locator：Introduction 1.2 P3 S3

- paraphrase_cn：平台通过基于数据主体偏好的自动交易实现大规模销售并为每笔交易补偿数据主体。

- move_code：REQUIREMENT

- statement_status：author_inference

- why_here_cn：给出平台自动市场的运行方式。

- inherits_from_previous_cn：依赖一次设置。

- changes_argument_state_cn：确立交易的自动化机制。

- sets_up_next_cn：为当前缺乏此类平台的判断做铺垫。

- failure_if_removed_cn：缺少后平台运行逻辑不完整。

- evidence_pointer：Introduction 1.2 P3 S3

### 57. Introduction 1.2 P3 S4

- order：57

- locator：Introduction 1.2 P3 S4

- paraphrase_cn：由于目前缺乏稳健平台执行该任务，这种数据收集还不普遍。

- move_code：GAP

- statement_status：author_inference

- why_here_cn：说明本文所设计的市场机制有现实空白。

- inherits_from_previous_cn：依赖平台功能设想。

- changes_argument_state_cn：把平台缺失定义为实践空白。

- sets_up_next_cn：为平台一旦存在可广泛采用做铺垫。

- failure_if_removed_cn：缺少后本文机制与现状差距不明显。

- evidence_pointer：Introduction 1.2 P3 S4

### 58. Introduction 1.2 P3 S5

- order：58

- locator：Introduction 1.2 P3 S5

- paraphrase_cn：一旦此类平台存在，就能促成数据主体和买方广泛采用。

- move_code：GAP

- statement_status：author_inference

- why_here_cn：给出建立平台的价值承诺。

- inherits_from_previous_cn：依赖平台缺失。

- changes_argument_state_cn：把平台建设升华为市场形成条件。

- sets_up_next_cn：为理论比较预告做铺垫。

- failure_if_removed_cn：缺少后平台必要性论证不完整。

- evidence_pointer：Introduction 1.2 P3 S5

### 59. Introduction 1.2 P4 S1

- order：59

- locator：Introduction 1.2 P4 S1

- paraphrase_cn：我们提供本文方法与固定补偿、集中优化及最佳基准的理论比较。

- move_code：STUDY_OVERVIEW

- statement_status：author_inference

- why_here_cn：预告第5章比较结构，让读者知道评估路线。

- inherits_from_previous_cn：承接机制设计完成。

- changes_argument_state_cn：从设计转向评估。

- sets_up_next_cn：为代表性样本和近最优成本结果做铺垫。

- failure_if_removed_cn：缺少后理论与仿真章节缺乏预告。

- evidence_pointer：Introduction 1.2 P4 S1

### 60. Introduction 1.2 P4 S2

- order：60

- locator：Introduction 1.2 P4 S2

- paraphrase_cn：我们证明市场机制产生代表性样本且成本近最优。

- move_code：RESULT

- statement_status：author_inference

- why_here_cn：在引言直接给出核心结果。

- inherits_from_previous_cn：依赖比较结构。

- changes_argument_state_cn：提前兑现机制目标。

- sets_up_next_cn：为稳健性预告做铺垫。

- failure_if_removed_cn：缺少后引言没有结果卖点。

- evidence_pointer：Introduction 1.2 P4 S2

### 61. Introduction 1.2 P4 S3

- order：61

- locator：Introduction 1.2 P4 S3

- paraphrase_cn：最后我们通过大量仿真确认结果稳健性。

- move_code：STUDY_OVERVIEW

- statement_status：author_inference

- why_here_cn：预告第6章仿真证据。

- inherits_from_previous_cn：依赖理论比较与结果。

- changes_argument_state_cn：把证据范围扩展到仿真。

- sets_up_next_cn：为下面更具体的性能声明做铺垫。

- failure_if_removed_cn：缺少后仿真章节缺少预告。

- evidence_pointer：Introduction 1.2 P4 S3

### 62. Introduction 1.2 P5 S1

- order：62

- locator：Introduction 1.2 P5 S1

- paraphrase_cn：结果表明方法能达到理论最佳偏差零，为买方提供代表性样本。

- move_code：RESULT

- statement_status：author_inference

- why_here_cn：把代表性结果具体化为偏差零。

- inherits_from_previous_cn：依赖代表性样本结论。

- changes_argument_state_cn：用可度量指标定义成功。

- sets_up_next_cn：为成本接近基准做铺垫。

- failure_if_removed_cn：缺少后核心卖点不量化。

- evidence_pointer：Introduction 1.2 P5 S1

### 63. Introduction 1.2 P5 S2

- order：63

- locator：Introduction 1.2 P5 S2

- paraphrase_cn：样本成本接近最佳基准。

- move_code：RESULT

- statement_status：author_inference

- why_here_cn：把成本优势与理论基准建立联系。

- inherits_from_previous_cn：依赖偏差零结果。

- changes_argument_state_cn：同时满足无偏和低成本。

- sets_up_next_cn：为支配固定补偿做铺垫。

- failure_if_removed_cn：缺少后机制只无偏但成本未知。

- evidence_pointer：Introduction 1.2 P5 S2

### 64. Introduction 1.2 P5 S3

- order：64

- locator：Introduction 1.2 P5 S3

- paraphrase_cn：机制不仅支配固定补偿，在大多数实际设置下还优于拥有部分隐私顾虑信息的集中优化。

- move_code：RESULT

- statement_status：author_inference

- why_here_cn：同时覆盖两个对手，把性能声明推向最强。

- inherits_from_previous_cn：依赖成本接近基准。

- changes_argument_state_cn：把机制置于两种现状之上。

- sets_up_next_cn：为放弃部分信息的反直觉结论做铺垫。

- failure_if_removed_cn：缺少后引言性能声明不完整。

- evidence_pointer：Introduction 1.2 P5 S3

### 65. Introduction 1.2 P5 S4

- order：65

- locator：Introduction 1.2 P5 S4

- paraphrase_cn：有趣的是，即使平台能通过观察行为估计隐私顾虑，最好也放弃该信息。

- move_code：BOUNDARY_CONDITION

- statement_status：author_inference

- why_here_cn：把集中优化被超越升级为'信息无价值'的反直觉管理建议。

- inherits_from_previous_cn：依赖优于集中优化。

- changes_argument_state_cn：从性能比较转向设计原则。

- sets_up_next_cn：为第7节部分信息比较做预告。

- failure_if_removed_cn：缺少后本文最独特洞见缺失。

- evidence_pointer：Introduction 1.2 P5 S4

### 66. Introduction 1.2 P5 S5

- order：66

- locator：Introduction 1.2 P5 S5

- paraphrase_cn：平台利用本文市场机制在数据主体和买方之间创造市场会得到更好结果。

- move_code：BOUNDARY_CONDITION

- statement_status：author_inference

- why_here_cn：给出替代行动方案，把'放弃信息'转化为'采用RSP'。

- inherits_from_previous_cn：依赖放弃信息结论。

- changes_argument_state_cn：把消极建议转为积极机制采用。

- sets_up_next_cn：为平等和包容测量做铺垫。

- failure_if_removed_cn：缺少后放弃信息的建议没有替代方案。

- evidence_pointer：Introduction 1.2 P5 S5

### 67. Introduction 1.2 P5 S6

- order：67

- locator：Introduction 1.2 P5 S6

- paraphrase_cn：此外我们的机制在平等和包容测量上接近最佳基准。

- move_code：RESULT

- statement_status：author_inference

- why_here_cn：引入排除率和不平等维度，扩大机制优势面。

- inherits_from_previous_cn：依赖市场机制价值。

- changes_argument_state_cn：把评价从偏差成本扩展到公平。

- sets_up_next_cn：为样本量和匿名性洞见做铺垫。

- failure_if_removed_cn：缺少后Vp和Gini指标没有引言预告。

- evidence_pointer：Introduction 1.2 P5 S6

### 68. Introduction 1.2 P5 S7

- order：68

- locator：Introduction 1.2 P5 S7

- paraphrase_cn：除主要发现外，我们还提供样本量和匿名性对不同机制性能影响的洞见。

- move_code：RESULT

- statement_status：author_inference

- why_here_cn：预告第5.6节和α弹性分析。

- inherits_from_previous_cn：依赖主要发现。

- changes_argument_state_cn：扩展贡献至机制设计参数。

- sets_up_next_cn：为理论贡献段落做铺垫。

- failure_if_removed_cn：缺少后样本量和匿名性分析缺少引言预告。

- evidence_pointer：Introduction 1.2 P5 S7

### 69. Introduction 1.2 P6 S1

- order：69

- locator：Introduction 1.2 P6 S1

- paraphrase_cn：本研究对理论和实践都有贡献。

- move_code：CONTRIBUTION

- statement_status：contribution_claim

- why_here_cn：开启贡献声明段落。

- inherits_from_previous_cn：依赖全部结果。

- changes_argument_state_cn：把研究结果转为贡献陈述。

- sets_up_next_cn：为理论贡献具体化做铺垫。

- failure_if_removed_cn：缺少后贡献声明没有总起句。

- evidence_pointer：Introduction 1.2 P6 S1

### 70. Introduction 1.2 P6 S2

- order：70

- locator：Introduction 1.2 P6 S2

- paraphrase_cn：理论上，我们提出结合采样算法与拍卖机制的算法化市场机制，创造个体理性且激励相容、以近最优成本提供真实数据无偏样本的机制。

- move_code：CONTRIBUTION

- statement_status：contribution_claim

- why_here_cn：把机制设计成果总结为理论贡献。

- inherits_from_previous_cn：依赖研究总体贡献。

- changes_argument_state_cn：确立制品的理论属性。

- sets_up_next_cn：为与估计文献区分做铺垫。

- failure_if_removed_cn：缺少后理论贡献不具体。

- evidence_pointer：Introduction 1.2 P6 S2

### 71. Introduction 1.2 P6 S3

- order：71

- locator：Introduction 1.2 P6 S3

- paraphrase_cn：与先前用机制设计和估计从有偏样本得到无偏估计不同，本文产生无偏样本，是根本性方法变化。

- move_code：CONTRIBUTION

- statement_status：contribution_claim

- why_here_cn：精准定位创新点：无偏样本而非无偏估计。

- inherits_from_previous_cn：依赖理论贡献陈述。

- changes_argument_state_cn：把贡献与文献缺口对齐。

- sets_up_next_cn：为实践贡献做铺垫。

- failure_if_removed_cn：缺少后论文与估计文献的区别不成立。

- evidence_pointer：Introduction 1.2 P6 S3

### 72. Introduction 1.2 P6 S4

- order：72

- locator：Introduction 1.2 P6 S4

- paraphrase_cn：实践贡献方面，机制不仅接近最佳基准，还优于固定补偿和集中优化，是当前实践的强替代。

- move_code：CONTRIBUTION

- statement_status：contribution_claim

- why_here_cn：把性能优势转化为实践替代方案。

- inherits_from_previous_cn：依赖理论贡献和结果。

- changes_argument_state_cn：把贡献从理论扩展到实践。

- sets_up_next_cn：为可实施性做铺垫。

- failure_if_removed_cn：缺少后实践价值不明。

- evidence_pointer：Introduction 1.2 P6 S4

### 73. Introduction 1.2 P6 S5

- order：73

- locator：Introduction 1.2 P6 S5

- paraphrase_cn：此外方法具有理想实施属性，是当前实践的可行替代。

- move_code：CONTRIBUTION

- statement_status：contribution_claim

- why_here_cn：引入可实施性，防止贡献停留在理论。

- inherits_from_previous_cn：依赖实践贡献。

- changes_argument_state_cn：把实践价值具体化为可实施。

- sets_up_next_cn：为合规性做铺垫。

- failure_if_removed_cn：缺少后可实施性贡献缺失。

- evidence_pointer：Introduction 1.2 P6 S5

### 74. Introduction 1.2 P6 S6

- order：74

- locator：Introduction 1.2 P6 S6

- paraphrase_cn：这能创造一个使数据主体和买方受益、同时符合透明和同意监管要求的数据市场。

- move_code：CONTRIBUTION

- statement_status：contribution_claim

- why_here_cn：把贡献与引言开头的监管和同意需求闭环。

- inherits_from_previous_cn：依赖可实施性。

- changes_argument_state_cn：把机制价值与社会合规对接。

- sets_up_next_cn：结束引言，进入文献综述。

- failure_if_removed_cn：缺少后合规贡献与引言监管问题脱节。

- evidence_pointer：Introduction 1.2 P6 S6

## 引言逐段图谱

### 1. Introduction P1

- locator：Introduction P1

- opening_move_cn：以广泛的应用需求（广告、调查、医疗）开头，提出同意、透明、代表性的规范性条件。

- development_move_cn：立即给出本文算法市场机制方案，明确结尾用'先描述缺陷'预告。

- pivot_move_cn：从规范需求转向本文方案。

- closing_move_cn：用'我们首先描述当前方法的缺点'制造阅读期待，为后面问题段落铺垫。

- paragraph_job_cn：在开头直接宣告论文解决什么需求、提出什么方案，并预告问题描述路线。

### 2. Introduction P2

- locator：Introduction P2

- opening_move_cn：以用户用数据换服务这一当代经济基础开头。

- development_move_cn：通过互联网普及、用户数、数据量、数据价值、市场规模逐层累积。

- pivot_move_cn：从数据收集的一般事实转向对数据收集实践缺陷的批评。

- closing_move_cn：以2700亿美元市场价值结束，强化数据市场的经济利害，为P3的第三方经纪问题做铺垫。

- paragraph_job_cn：建立个体数据市场的巨大规模和商业价值，说明研究问题为什么值得处理。

### 3. Introduction P3

- locator：Introduction P3

- opening_move_cn：以第三方经纪商跨站追踪和隐蔽收集开头。

- development_move_cn：先用文献支撑'收集过程浑浊'，再说明数据被用于机器学习产品，最后指出数据主体很少被补偿。

- pivot_move_cn：从描述收集方式转向批评补偿缺失。

- closing_move_cn：以补偿缺失结尾，为下一段用户隐私工具使用提供动机。

- paragraph_job_cn：揭示现有数据收集过程的不透明和补偿缺失，建立论文的第一个治理缺口。

### 4. Introduction P4

- locator：Introduction P4

- opening_move_cn：以数据主体从愿意免费分享到迅速觉醒的时间对比开头。

- development_move_cn：用补偿缺失→隐私工具→过滤触达→样本偏差→相关性→代表性缺失→广告ROI负值的因果链层层推进。

- pivot_move_cn：从用户行为转向数据质量后果。

- closing_move_cn：以广告ROI为负收束，证明数据质量问题有真实经济后果。

- paragraph_job_cn：建立隐私工具导致样本偏差的机制，为后文无偏样本需求提供因果基础。

### 5. Introduction P5

- locator：Introduction P5

- opening_move_cn：以监管压力作为新增维度开头。

- development_move_cn：先解释GDPR/CCPA为何冲击现行范式，再叠加第三方cookie限制。

- pivot_move_cn：从市场问题转向制度环境变化。

- closing_move_cn：以'个人数据市场运作方式需要根本变革'收束，为数据市场平台和本文机制做铺垫。

- paragraph_job_cn：把问题从市场效率扩展到合规要求，形成需要新范式的制度背景。

### 6. Introduction 1.1 P1

- locator：Introduction 1.1 P1

- opening_move_cn：以新市场出现、旨在同意收集并补偿数据主体开头。

- development_move_cn：列举两类平台：可携为主补偿为辅、直接交易付费；随后介绍买方服务和附加场景。

- pivot_move_cn：从平台类型转向'这些公司依赖固定补偿或集中优化'这一共同缺陷。

- closing_move_cn：以两类机制的概括结尾，为后文机制比较建立现实对应。

- paragraph_job_cn：介绍现实中的平台中介数据市场，并定位论文要超越的两类机制。

### 7. Introduction 1.1 P2

- locator：Introduction 1.1 P2

- opening_move_cn：以'挑战不限于在线广告'开头，扩展应用场景。

- development_move_cn：依次介绍调查平台和医疗平台，说明它们同样使用固定补偿或集中优化。

- pivot_move_cn：从例子转向'当前方法缺陷'。

- closing_move_cn：以'设定补偿时不考虑隐私顾虑'收束，强调医疗等敏感场景的机制缺陷。

- paragraph_job_cn：把固定补偿/集中优化缺陷从广告扩展到调查和医疗，增强ISR问题的一般性。

### 8. Introduction 1.1 P3

- locator：Introduction 1.1 P3

- opening_move_cn：以'两类缺陷被本文直接处理'开头，收束前两段现实案例。

- development_move_cn：详细解释固定补偿的自选择偏差机制，引用文献支撑相关性；随后介绍集中优化的适用性限制。

- pivot_move_cn：从固定补偿转向集中优化，并指出'即使有部分信息也未必最优'。

- closing_move_cn：以集中优化可能不是最佳方案收束，为本文市场机制创造缺口。

- paragraph_job_cn：集中建立两种现状机制的因果缺陷，为替代机制设计提供问题陈述。

### 9. Introduction 1.2 P1

- locator：Introduction 1.2 P1

- opening_move_cn：以'我们提出替代补偿机制'开头，正式进入方案。

- development_move_cn：逐步给出合作企业、机制目标、两个构件和三个功能。

- pivot_move_cn：从问题描述转向解决方案陈述。

- closing_move_cn：以机制三功能清单收束，为后文设计章节和评价指标做铺垫。

- paragraph_job_cn：概述本文制品的组成、目标和合作背景，让读者在进入技术细节前把握整体方案。

### 10. Introduction 1.2 P2

- locator：Introduction 1.2 P2

- opening_move_cn：以当前实践'按查询购买'开头，与本文时间结构形成对照。

- development_move_cn：依次说明数据预先收集、按隐私偏好补偿、激励相容防虚报，并用高层直觉解释。

- pivot_move_cn：从机制特征转向'什么是符合数据主体利益'。

- closing_move_cn：以真实报告符合数据主体利益收束，为拍卖机制设计做铺垫。

- paragraph_job_cn：解释本文机制的运行流程和激励逻辑，用非技术语言建立机制的理解基础。

### 11. Introduction 1.2 P3

- locator：Introduction 1.2 P3

- opening_move_cn：以'中介平台至关重要'开头，说明平台角色的必要性。

- development_move_cn：逐步论证一次设置、自动化交易、规模经济、当前平台缺失、未来采用前景。

- pivot_move_cn：从平台运行逻辑转向'为何现在没有'的实践缺口。

- closing_move_cn：以'平台一旦存在可广泛采用'收束，为后文理论比较和仿真验证做铺垫。

- paragraph_job_cn：论证平台中介的必要性和机制的可实施性，回应'为何需要平台'的现实问题。

### 12. Introduction 1.2 P4

- locator：Introduction 1.2 P4

- opening_move_cn：以'我们提供理论比较'开头，从设计转向评估。

- development_move_cn：预告与固定补偿、集中优化、最佳基准的比较，再提到代表性、近最优成本和仿真稳健性。

- pivot_move_cn：从方案解说转向研究路线预告。

- closing_move_cn：以仿真稳健性收束，为第6章证据做铺垫。

- paragraph_job_cn：给读者全文评估章节的路线图，使后续理论、仿真、真实数据有预期。

### 13. Introduction 1.2 P5

- locator：Introduction 1.2 P5

- opening_move_cn：以'结果表明'开头，直接给出核心结果。

- development_move_cn：依次给出偏差零、成本接近基准、支配固定补偿、优于集中优化、放弃部分信息、平等包容、样本量洞见。

- pivot_move_cn：从性能结果转向反直觉管理结论。

- closing_move_cn：以样本量和匿名性洞见收束，为后面的参数化分析做铺垫。

- paragraph_job_cn：在引言内完成核心结果的分层宣告，形成最强卖点。

### 14. Introduction 1.2 P6

- locator：Introduction 1.2 P6

- opening_move_cn：以'本研究对理论和实践都有贡献'开头。

- development_move_cn：先给理论贡献并强调无偏样本差异，再给实践贡献并强调可实施和合规。

- pivot_move_cn：从理论转向实践。

- closing_move_cn：以合规数据市场收束，结束引言。

- paragraph_job_cn：把研究定位为既有理论创新又有实践替代方案的IS贡献，完成引言闭环。

## 理论到设计逐句图谱

### 1. Section 4 P1 S1

- order：1

- locator：Section 4 P1 S1

- paraphrase_cn：为设计产生大小为n的无偏样本的机制，我们采用如下方法。

- move_code：DESIGN_OVERVIEW

- statement_status：design_decision

- why_here_cn：开启机制设计章节，给出本节的整体路线。

- inherits_from_previous_cn：承接第3节偏差-成本权衡问题。

- changes_argument_state_cn：从问题描述转向设计步骤。

- sets_up_next_cn：为'先设计单记录补偿机制'做铺垫。

- failure_if_removed_cn：缺少后第4章结构缺乏总体指引。

- evidence_pointer：Section 4 P1 S1

### 2. Section 4 P1 S2

- order：2

- locator：Section 4 P1 S2

- paraphrase_cn：首先，为确保平台引出可靠的数据主体隐私顾虑，我们采用一种从数据集中选择单条记录、诱导真实报告的补偿机制。

- move_code：DESIGN_REQUIREMENT

- statement_status：design_decision

- why_here_cn：把'真实报告'变成第一个设计约束。

- inherits_from_previous_cn：承接总体方法。

- changes_argument_state_cn：把目标分解为单记录机制。

- sets_up_next_cn：为'样本需重复n个子群体'做铺垫。

- failure_if_removed_cn：缺少后激励相容机制没有设计入口。

- evidence_pointer：Section 4 P1 S2

### 3. Section 4 P1 S3

- order：3

- locator：Section 4 P1 S3

- paraphrase_cn：为产生大小为n的样本，该真实报告机制应在n个独立子群体内重复。

- move_code：DESIGN_DECISION

- statement_status：design_decision

- why_here_cn：把单记录机制扩展到样本量。

- inherits_from_previous_cn：依赖单记录机制。

- changes_argument_state_cn：引入子群体重复结构。

- sets_up_next_cn：为'子群体大小为2最优'做铺垫。

- failure_if_removed_cn：缺少后n样本与单记录机制脱节。

- evidence_pointer：Section 4 P1 S3

### 4. Section 4 P1 S4

- order：4

- locator：Section 4 P1 S4

- paraphrase_cn：我们证明最优子群体大小为2，即每个子群体只含两个数据主体。

- move_code：DESIGN_RATIONALE

- statement_status：design_decision

- why_here_cn：给出RSP用两人配对的理论理由。

- inherits_from_previous_cn：依赖子群体重复结构。

- changes_argument_state_cn：把子群体大小定为2。

- sets_up_next_cn：为采样算法选择配对做铺垫。

- failure_if_removed_cn：缺少后RSP的两人配对无理论依据。

- evidence_pointer：Section 4 P1 S4

### 5. Section 4 P1 S5

- order：5

- locator：Section 4 P1 S5

- paraphrase_cn：然后利用该机制，我们提出简单而稳健的采样算法来选择子群体配对。

- move_code：DESIGN_DECISION

- statement_status：design_decision

- why_here_cn：从补偿机制过渡到采样算法。

- inherits_from_previous_cn：依赖两人子群体。

- changes_argument_state_cn：把设计焦点转向配对选择。

- sets_up_next_cn：为最后组合成市场机制做铺垫。

- failure_if_removed_cn：缺少后采样算法与拍卖机制无连接。

- evidence_pointer：Section 4 P1 S5

### 6. Section 4 P1 S6

- order：6

- locator：Section 4 P1 S6

- paraphrase_cn：最后，通过把补偿机制嵌入采样算法，形成市场机制。

- move_code：DESIGN_DECISION

- statement_status：design_decision

- why_here_cn：完成三步骤的合成，预告RSP。

- inherits_from_previous_cn：依赖采样算法。

- changes_argument_state_cn：把两个构件统一为市场机制。

- sets_up_next_cn：为4.1-4.3节分别展开做铺垫。

- failure_if_removed_cn：缺少后全文核心制品没有组装。

- evidence_pointer：Section 4 P1 S6

### 7. Section 4.1 P1 S1

- order：7

- locator：Section 4.1 P1 S1

- paraphrase_cn：我们先聚焦从候选数据主体集合中选择一人的基本机制。

- move_code：DESIGN_OVERVIEW

- statement_status：design_decision

- why_here_cn：开始4.1节单记录拍卖。

- inherits_from_previous_cn：承接第4章三步骤。

- changes_argument_state_cn：把设计范围限定为单记录。

- sets_up_next_cn：为个体理性和激励相容定义做铺垫。

- failure_if_removed_cn：缺少后4.1节缺少起点。

- evidence_pointer：Section 4.1 P1 S1

### 8. Section 4.1 P1 S2

- order：8

- locator：Section 4.1 P1 S2

- paraphrase_cn：有效补偿机制必须满足两个约束：个体理性确保所有数据主体参与，激励相容确保数据主体真实报告隐私顾虑。

- move_code：THEORY_CLAIM

- statement_status：theory_claim

- why_here_cn：建立机制设计必须满足的形式约束。

- inherits_from_previous_cn：依赖单记录机制焦点。

- changes_argument_state_cn：定义评价机制的两个标准。

- sets_up_next_cn：为两个约束的数学定义做铺垫。

- failure_if_removed_cn：缺少后机制无法被证明有效。

- evidence_pointer：Section 4.1 P1 S2

### 9. Section 4.1 P1 S3

- order：9

- locator：Section 4.1 P1 S3

- paraphrase_cn：个体理性指所有数据主体期望效用非负，确保参与和数据集合代表性。

- move_code：THEORY_CLAIM

- statement_status：theory_claim

- why_here_cn：把个体理性与数据代表性连接，说明为什么这是个重要约束。

- inherits_from_previous_cn：依赖个体理性约束。

- changes_argument_state_cn：把个体理性解释为参与保障。

- sets_up_next_cn：为激励相容定义做铺垫。

- failure_if_removed_cn：缺少后IR约束的意义不明确。

- evidence_pointer：Section 4.1 P1 S3

### 10. Section 4.1 P1 S4

- order：10

- locator：Section 4.1 P1 S4

- paraphrase_cn：激励相容指真实报告使期望效用不低于虚报，确保数据主体无动机虚报。

- move_code：THEORY_CLAIM

- statement_status：theory_claim

- why_here_cn：给出激励相容的数学标准和行为含义。

- inherits_from_previous_cn：依赖激励相容约束。

- changes_argument_state_cn：把激励相容解释为防虚报。

- sets_up_next_cn：为Proposition 1做铺垫。

- failure_if_removed_cn：缺少后IC约束无法被用。

- evidence_pointer：Section 4.1 P1 S4

### 11. Section 4.1 Proposition 1

- order：11

- locator：Section 4.1 Proposition 1

- paraphrase_cn：第二补偿拍卖：选择报告隐私顾虑最低者，按第二低报告者的隐私成本支付；该机制激励相容且个体理性。

- move_code：THEORY_PROPOSITION

- statement_status：theory_claim

- why_here_cn：作为核心理论命题，给出具体补偿规则的激励性质证明。

- inherits_from_previous_cn：依赖IR和IC约束定义。

- changes_argument_state_cn：从约束标准过渡到满足标准的机制。

- sets_up_next_cn：为VCG机制连接做铺垫。

- failure_if_removed_cn：缺少后全文的激励相容基础缺失。

- evidence_pointer：Section 4.1 Proposition 1

### 12. Section 4.1 P3 S1

- order：12

- locator：Section 4.1 P3 S1

- paraphrase_cn：该机制中平台选择报告隐私顾虑最低的数据主体，并按第二低报告者的保留价支付。

- move_code：DESIGN_FEATURE

- statement_status：design_decision

- why_here_cn：用文字复述Proposition 1的规则，便于读者理解。

- inherits_from_previous_cn：依赖命题陈述。

- changes_argument_state_cn：把命题翻译为可操作规则。

- sets_up_next_cn：为命名第二补偿拍卖做铺垫。

- failure_if_removed_cn：缺少后命题公式缺少语言解释。

- evidence_pointer：Section 4.1 P3 S1

### 13. Section 4.1 P3 S2

- order：13

- locator：Section 4.1 P3 S2

- paraphrase_cn：我们称该采购机制为第二补偿拍卖，是VCG机制的变体。

- move_code：THEORY_CLAIM

- statement_status：theory_claim

- why_here_cn：把本文机制纳入VCG经典理论，借理论信誉。

- inherits_from_previous_cn：依赖拍卖规则。

- changes_argument_state_cn：把具体机制标识为VCG变体。

- sets_up_next_cn：为采购拍卖文献引用做铺垫。

- failure_if_removed_cn：缺少后机制缺乏理论家族归属。

- evidence_pointer：Section 4.1 P3 S2

### 14. Section 4.1 P3 S3

- order：14

- locator：Section 4.1 P3 S3

- paraphrase_cn：VCG中数据主体补偿按其存在与否的他人剩余差额计算。

- move_code：THEORY_CLAIM

- statement_status：theory_claim

- why_here_cn：用VCG公式解释第二补偿拍卖为何激励相容。

- inherits_from_previous_cn：依赖VCG标识。

- changes_argument_state_cn：把第二补偿拍卖与VCG的剩余差额逻辑对齐。

- sets_up_next_cn：为采购拍卖文献做铺垫。

- failure_if_removed_cn：缺少后VCG连接流于表面。

- evidence_pointer：Section 4.1 P3 S3

### 15. Section 4.1 P3 S4

- order：15

- locator：Section 4.1 P3 S4

- paraphrase_cn：在数据样本包含多个卖家的情境中，样本由多个第二补偿拍卖组合而成。

- move_code：DESIGN_RATIONALE

- statement_status：design_decision

- why_here_cn：把单记录拍卖扩展回n样本，衔接采样算法。

- inherits_from_previous_cn：依赖VCG机制。

- changes_argument_state_cn：把多个拍卖嵌入采样算法。

- sets_up_next_cn：为4.2节采样算法做铺垫。

- failure_if_removed_cn：缺少后拍卖与样本之间脱节。

- evidence_pointer：Section 4.1 P3 S4

### 16. Section 4.2 P1 S1

- order：16

- locator：Section 4.2 P1 S1

- paraphrase_cn：为提供大小为n的样本，平台需从N个数据主体创建n个子群体，并对每个子群体应用Proposition 1机制。

- move_code：DESIGN_DECISION

- statement_status：design_decision

- why_here_cn：把拍卖机制接入采样流程。

- inherits_from_previous_cn：依赖子群体重复。

- changes_argument_state_cn：确认采样算法使用相同拍卖。

- sets_up_next_cn：为偏差定义做铺垫。

- failure_if_removed_cn：缺少后采样算法与拍卖脱节。

- evidence_pointer：Section 4.2 P1 S1

### 17. Section 4.2 P1 S2

- order：17

- locator：Section 4.2 P1 S2

- paraphrase_cn：偏差定义为被选数据主体期望敏感属性与总体均值之差。

- move_code：THEORY_CLAIM

- statement_status：theory_claim

- why_here_cn：给出偏差的正式定义，是后文E(B)的模型基础。

- inherits_from_previous_cn：依赖样本选择设定。

- changes_argument_state_cn：把偏差概念形式化。

- sets_up_next_cn：为随机选择的权衡做铺垫。

- failure_if_removed_cn：缺少后B的度量无定义。

- evidence_pointer：Section 4.2 P1 S2

### 18. Section 4.2 P1 S3

- order：18

- locator：Section 4.2 P1 S3

- paraphrase_cn：若从每个子群体随机选人，则样本无偏但成本高。

- move_code：DESIGN_RATIONALE

- statement_status：design_decision

- why_here_cn：先给出天真的无偏方案并指出成本缺陷。

- inherits_from_previous_cn：依赖偏差定义。

- changes_argument_state_cn：建立随机选择的偏差-成本两难。

- sets_up_next_cn：为选最低隐私顾虑者做对照。

- failure_if_removed_cn：缺少后为何不简单随机抽样不清楚。

- evidence_pointer：Section 4.2 P1 S3

### 19. Section 4.2 P1 S4

- order：19

- locator：Section 4.2 P1 S4

- paraphrase_cn：我们选择子群体中报告隐私顾虑最低者以最小化样本成本。

- move_code：DESIGN_DECISION

- statement_status：design_decision

- why_here_cn：把第二补偿拍卖的选人规则与成本目标连接。

- inherits_from_previous_cn：依赖随机选择的成本问题。

- changes_argument_state_cn：确定选最低顾虑者。

- sets_up_next_cn：为子群体大小的偏差效应做铺垫。

- failure_if_removed_cn：缺少后拍卖规则与采样目标脱节。

- evidence_pointer：Section 4.2 P1 S4

### 20. Section 4.2 P1 S5

- order：20

- locator：Section 4.2 P1 S5

- paraphrase_cn：子群体越大，隐私顾虑差异越大，在敏感属性与隐私顾虑相关时，敏感属性差异也越大，选最低顾虑者的期望偏差增加。

- move_code：DESIGN_RATIONALE

- statement_status：theory_claim

- why_here_cn：从顺序统计量直觉导出子群体大小为2的最优性。

- inherits_from_previous_cn：依赖选最低顾虑者。

- changes_argument_state_cn：把偏差与子群体大小建立负向关系。

- sets_up_next_cn：为最小子群体设计做铺垫。

- failure_if_removed_cn：缺少后两人子群体无理论依据。

- evidence_pointer：Section 4.2 P1 S5

### 21. Section 4.2 P2 S1

- order：21

- locator：Section 4.2 P2 S1

- paraphrase_cn：平台采样算法的目标是最小化期望成本和样本偏差。

- move_code：DESIGN_OVERVIEW

- statement_status：design_decision

- why_here_cn：明确采样算法的双目标。

- inherits_from_previous_cn：依赖偏差-成本权衡。

- changes_argument_state_cn：把偏差与成本并列为设计目标。

- sets_up_next_cn：为采用最小子群体做铺垫。

- failure_if_removed_cn：缺少后采样算法评价标准缺失。

- evidence_pointer：Section 4.2 P2 S1

### 22. Section 4.2 P2 S2

- order：22

- locator：Section 4.2 P2 S2

- paraphrase_cn：为最小化偏差，我们使用最小可能的子群体，即一对数据主体。

- move_code：DESIGN_DECISION

- statement_status：design_decision

- why_here_cn：把第4章开头的两人子群体结论落到算法设计。

- inherits_from_previous_cn：依赖子群体大小效应。

- changes_argument_state_cn：确定配对规模为2。

- sets_up_next_cn：为按敏感属性排序做铺垫。

- failure_if_removed_cn：缺少后RSP的两人配对缺少推理。

- evidence_pointer：Section 4.2 P2 S2

### 23. Section 4.2 P2 S3

- order：23

- locator：Section 4.2 P2 S3

- paraphrase_cn：为进一步降低偏差，平台按敏感属性排序，选择排序后相邻的数据主体配对。

- move_code：DESIGN_DECISION

- statement_status：design_decision

- why_here_cn：引入排序相邻配对，是RSP的核心设计选择。

- inherits_from_previous_cn：依赖两人最小子群体。

- changes_argument_state_cn：用排序进一步缩小配对内差异。

- sets_up_next_cn：为相关时成本下降做铺垫。

- failure_if_removed_cn：缺少后RSP独特设计缺失。

- evidence_pointer：Section 4.2 P2 S3

### 24. Section 4.2 P2 S4

- order：24

- locator：Section 4.2 P2 S4

- paraphrase_cn：在敏感属性与隐私顾虑相关时，该法也降低配对内隐私顾虑差异，从而降低成本。

- move_code：DESIGN_RATIONALE

- statement_status：theory_claim

- why_here_cn：把排序相邻同时连接到偏差和成本两个目标。

- inherits_from_previous_cn：依赖排序配对。

- changes_argument_state_cn：证明排序同时服务双目标。

- sets_up_next_cn：为平台排序隐私成本讨论做铺垫。

- failure_if_removed_cn：缺少后排序设计的双重好处不成立。

- evidence_pointer：Section 4.2 P2 S4

### 25. Section 4.2 P3 S1

- order：25

- locator：Section 4.2 P3 S1

- paraphrase_cn：尽管平台能基于数据主体订阅时提供的敏感属性排序，我们并不认为这给数据主体带来隐私成本。

- move_code：METHOD_JUSTIFICATION

- statement_status：author_inference

- why_here_cn：预先处理读者对'平台拥有敏感属性'的隐私质疑。

- inherits_from_previous_cn：依赖排序相邻设计。

- changes_argument_state_cn：把排序排除在隐私成本之外。

- sets_up_next_cn：为信任与不信任两种情形做铺垫。

- failure_if_removed_cn：缺少后排序可能被质疑引入额外隐私成本。

- evidence_pointer：Section 4.2 P3 S1

### 26. Section 4.2 P3 S2

- order：26

- locator：Section 4.2 P3 S2

- paraphrase_cn：数据主体设置平台档案时，其隐私顾虑并不因提供敏感属性而实现，隐私顾虑只在平台把数据卖给买方时产生。

- move_code：METHOD_JUSTIFICATION

- statement_status：author_inference

- why_here_cn：给出关键区分：档案设置阶段无隐私损失。

- inherits_from_previous_cn：依赖排序无成本主张。

- changes_argument_state_cn：把隐私成本限定在出售时点。

- sets_up_next_cn：为三种理由做铺垫。

- failure_if_removed_cn：缺少后排序无成本说法无依据。

- evidence_pointer：Section 4.2 P3 S2

### 27. Section 4.2 P3 S3

- order：27

- locator：Section 4.2 P3 S3

- paraphrase_cn：该假设不失一般性，原因有三。

- move_code：ROADMAP

- statement_status：author_inference

- why_here_cn：给读者三个理由的路线图。

- inherits_from_previous_cn：依赖排序无成本假设。

- changes_argument_state_cn：组织证据。

- sets_up_next_cn：为信任情形和同态加密讨论做铺垫。

- failure_if_removed_cn：缺少后三个理由无引导。

- evidence_pointer：Section 4.2 P3 S3

### 28. Section 4.2 P4 S1

- order：28

- locator：Section 4.2 P4 S1

- paraphrase_cn：第一，在数据主体信任平台时，平台有权访问敏感属性，从而能排序。

- move_code：METHOD_JUSTIFICATION

- statement_status：author_inference

- why_here_cn：给信任情形下的排序可行性。

- inherits_from_previous_cn：依赖三理由路线。

- changes_argument_state_cn：覆盖信任情况。

- sets_up_next_cn：为不信任情形做铺垫。

- failure_if_removed_cn：缺少后信任情形未被覆盖。

- evidence_pointer：Section 4.2 P4 S1

### 29. Section 4.2 P4 S2

- order：29

- locator：Section 4.2 P4 S2

- paraphrase_cn：第二，即使数据主体不信任平台，也有工具在不知向量构成值的情况下对数据集排序，如同态加密。

- move_code：METHOD_JUSTIFICATION

- statement_status：author_inference

- why_here_cn：用密码学工具消除不信任下的隐私成本。

- inherits_from_previous_cn：依赖不信任情形。

- changes_argument_state_cn：把排序与敏感属性读取解耦。

- sets_up_next_cn：为同态加密原理说明做铺垫。

- failure_if_removed_cn：缺少后不信任情形下排序不可行。

- evidence_pointer：Section 4.2 P4 S2

### 30. Section 4.2 P4 S3

- order：30

- locator：Section 4.2 P4 S3

- paraphrase_cn：同态加密允许对加密数据执行计算，在加密状态下比较和重排记录。

- move_code：METHOD_JUSTIFICATION

- statement_status：prior_literature

- why_here_cn：解释同态加密为何能支持排序。

- inherits_from_previous_cn：依赖工具存在。

- changes_argument_state_cn：把排序工程化。

- sets_up_next_cn：为'平台不接触敏感属性'做铺垫。

- failure_if_removed_cn：缺少后同态加密说法无原理。

- evidence_pointer：Section 4.2 P4 S3

### 31. Section 4.2 P4 S4

- order：31

- locator：Section 4.2 P4 S4

- paraphrase_cn：因此排序可在加密数据上完成，平台无法访问敏感属性，不造成隐私成本。

- move_code：METHOD_JUSTIFICATION

- statement_status：author_inference

- why_here_cn：把技术可能转化为模型无额外成本。

- inherits_from_previous_cn：依赖同态加密。

- changes_argument_state_cn：完成第二理由。

- sets_up_next_cn：为第三理由做铺垫。

- failure_if_removed_cn：缺少后不信任情形仍留下隐私成本。

- evidence_pointer：Section 4.2 P4 S4

### 32. Section 4.2 P5 S1

- order：32

- locator：Section 4.2 P5 S1

- paraphrase_cn：第三，即使数据主体担心加入平台和安全性，也不影响结果，因为额外隐私成本施加于所有数据主体，个体理性约束保证加入激励。

- move_code：METHOD_JUSTIFICATION

- statement_status：author_inference

- why_here_cn：解决平台自身隐私担忧对机制结论的影响。

- inherits_from_previous_cn：依赖前两个理由。

- changes_argument_state_cn：把平台级担忧归为全用户的加性成本。

- sets_up_next_cn：为总补偿同比例上升做铺垫。

- failure_if_removed_cn：缺少后机制结论受平台不信任影响。

- evidence_pointer：Section 4.2 P5 S1

### 33. Section 4.2 P5 S2

- order：33

- locator：Section 4.2 P5 S2

- paraphrase_cn：全平台隐私顾虑上升时，本文和所有基准方法的总补偿都会增加，但不影响方法间比较。

- move_code：METHOD_JUSTIFICATION

- statement_status：author_inference

- why_here_cn：把平台级成本变化中性化。

- inherits_from_previous_cn：依赖额外隐私成本结论。

- changes_argument_state_cn：保护机制比较的稳健性。

- sets_up_next_cn：结束排序隐私讨论，进入4.3节。

- failure_if_removed_cn：缺少后比较结果可能被质疑受平台不信任影响。

- evidence_pointer：Section 4.2 P5 S2

### 34. Section 4.3 P1 S1

- order：34

- locator：Section 4.3 P1 S1

- paraphrase_cn：我们现将补偿机制与采样算法结合，设计市场机制RSP。

- move_code：DESIGN_DECISION

- statement_status：design_decision

- why_here_cn：正式命名并组装全文核心制品。

- inherits_from_previous_cn：依赖4.1拍卖和4.2采样。

- changes_argument_state_cn：把两个构件统一为RSP。

- sets_up_next_cn：为公布机制和样本量做铺垫。

- failure_if_removed_cn：缺少后全文没有核心机制名称。

- evidence_pointer：Section 4.3 P1 S1

### 35. Section 4.3 P1 S2

- order：35

- locator：Section 4.3 P1 S2

- paraphrase_cn：该法先公布机制和样本量，请数据主体报告隐私顾虑和敏感属性，然后按敏感属性排序。

- move_code：DESIGN_FEATURE

- statement_status：design_decision

- why_here_cn：给出RSP第一步：报告和排序。

- inherits_from_previous_cn：依赖RSP组装。

- changes_argument_state_cn：把设计转化为算法步骤。

- sets_up_next_cn：为Algorithm 1输入输出做铺垫。

- failure_if_removed_cn：缺少后算法输入不完整。

- evidence_pointer：Section 4.3 P1 S2

### 36. Section 4.3 P1 S3

- order：36

- locator：Section 4.3 P1 S3

- paraphrase_cn：若隐私顾虑与敏感属性正相关则升序排序，负相关则降序排序。

- move_code：DESIGN_FEATURE

- statement_status：design_decision

- why_here_cn：把相关方向纳入排序方向，保证配对内低顾虑者接近均值。

- inherits_from_previous_cn：依赖报告和排序。

- changes_argument_state_cn：把相关性方向转化为算法规则。

- sets_up_next_cn：为算法输入输出定义做铺垫。

- failure_if_removed_cn：缺少后排序方向无法解释。

- evidence_pointer：Section 4.3 P1 S3

### 37. Section 4.3 P1 S4

- order：37

- locator：Section 4.3 P1 S4

- paraphrase_cn：算法输入是样本量n和数据主体敏感属性集合，输出是n个数据主体的匿名样本和补偿集合。

- move_code：DESIGN_FEATURE

- statement_status：design_decision

- why_here_cn：给出算法的接口定义，便于后续理论推导。

- inherits_from_previous_cn：依赖排序规则。

- changes_argument_state_cn：把机制封装为输入输出。

- sets_up_next_cn：为Algorithm 1伪代码做铺垫。

- failure_if_removed_cn：缺少后算法形式化不完整。

- evidence_pointer：Section 4.3 P1 S4

### 38. Section 4.3 P2 S1

- order：38

- locator：Section 4.3 P2 S1

- paraphrase_cn：排序后，平台随机选一个数据主体，与其在排序中的下一人比较报告隐私顾虑。

- move_code：DESIGN_FEATURE

- statement_status：design_decision

- why_here_cn：给出RSP第二步：随机配对比较。

- inherits_from_previous_cn：依赖排序完成。

- changes_argument_state_cn：把配对比较确定为随机滚动。

- sets_up_next_cn：为选低顾虑者并支付做铺垫。

- failure_if_removed_cn：缺少后RSP核心操作缺失。

- evidence_pointer：Section 4.3 P2 S1

### 39. Section 4.3 P2 S2

- order：39

- locator：Section 4.3 P2 S2

- paraphrase_cn：选择配对中报告隐私顾虑较低者进入样本，按另一人的保留价补偿，并移除选中者。

- move_code：DESIGN_FEATURE

- statement_status：design_decision

- why_here_cn：把第二补偿拍卖嵌入每对比较。

- inherits_from_previous_cn：依赖随机配对。

- changes_argument_state_cn：在配对层面应用激励相容支付。

- sets_up_next_cn：为重复n次做铺垫。

- failure_if_removed_cn：缺少后拍卖与采样未结合。

- evidence_pointer：Section 4.3 P2 S2

### 40. Section 4.3 P2 S3

- order：40

- locator：Section 4.3 P2 S3

- paraphrase_cn：重复该过程n次，选择n个数据主体。

- move_code：DESIGN_FEATURE

- statement_status：design_decision

- why_here_cn：给出循环退出条件。

- inherits_from_previous_cn：依赖单轮选择。

- changes_argument_state_cn：把单对机制扩展为完整样本。

- sets_up_next_cn：为Algorithm 1伪代码做铺垫。

- failure_if_removed_cn：缺少后算法不完整。

- evidence_pointer：Section 4.3 P2 S3

### 41. Section 4.3 P3 S1

- order：41

- locator：Section 4.3 P3 S1

- paraphrase_cn：讨论可实施性：每次交易运行n个拍卖看似繁琐，但计算上类似实时竞价，常见于在线广告交易市场。

- move_code：METHOD_JUSTIFICATION

- statement_status：author_inference

- why_here_cn：在机制设计完成后立即回复可实施性质疑。

- inherits_from_previous_cn：依赖RSP算法。

- changes_argument_state_cn：把计算负担类比为成熟技术。

- sets_up_next_cn：为计算成本可忽略做铺垫。

- failure_if_removed_cn：缺少后可实施性受到挑战。

- evidence_pointer：Section 4.3 P3 S1

### 42. Section 4.3 P3 S2

- order：42

- locator：Section 4.3 P3 S2

- paraphrase_cn：每次搜索、访问或应用交互都会触发广告拍卖，计算要求通常被认为可忽略并可在一秒内重复完成。

- move_code：METHOD_JUSTIFICATION

- statement_status：prior_literature

- why_here_cn：用实时竞价文献说明拍卖计算规模不构成障碍。

- inherits_from_previous_cn：依赖实时竞价类比。

- changes_argument_state_cn：把计算可行性建立在既有产业实践上。

- sets_up_next_cn：为数据主体参与自动化做铺垫。

- failure_if_removed_cn：缺少后计算可行性缺乏支持。

- evidence_pointer：Section 4.3 P3 S2

### 43. Section 4.3 P3 S3

- order：43

- locator：Section 4.3 P3 S3

- paraphrase_cn：数据主体虽为每笔交易竞价，但可一次设置偏好和隐私顾虑，之后拍卖自动进行，不必在场。

- move_code：METHOD_JUSTIFICATION

- statement_status：author_inference

- why_here_cn：解决数据主体参与负担问题。

- inherits_from_previous_cn：依赖实时竞价类比。

- changes_argument_state_cn：把参与成本降至一次设置。

- sets_up_next_cn：为同实时竞价自动出价类比做铺垫。

- failure_if_removed_cn：缺少后数据主体参与负担质疑未回应。

- evidence_pointer：Section 4.3 P3 S3

### 44. Section 4.3 P3 S4

- order：44

- locator：Section 4.3 P3 S4

- paraphrase_cn：这也类似实时竞价中广告商基于平台设置偏好自动出价。

- move_code：METHOD_JUSTIFICATION

- statement_status：author_inference

- why_here_cn：用产业惯例再次强化自动拍卖的可行性。

- inherits_from_previous_cn：依赖数据主体自动参与。

- changes_argument_state_cn：把用户自动参与描述为行业常态。

- sets_up_next_cn：结束第4章，进入第5章理论分析。

- failure_if_removed_cn：缺少后自动参与缺乏类比支撑。

- evidence_pointer：Section 4.3 P3 S4

## 制品设计理由逐句图谱

### 1. Section 4.1 P1 S2-S4

- order：1

- locator：Section 4.1 P1 S2-S4

- paraphrase_cn：为什么补偿机制必须满足个体理性和激励相容：没有IR，数据主体不参与，数据代表性失败；没有IC，虚报导致补偿不能反映真实隐私损失。

- move_code：ARTIFACT_RATIONALE

- statement_status：theory_claim

- why_here_cn：在拍卖设计之前先建立两条约束的必要性，使后续第二补偿拍卖是'被需要'的而非任意选择。

- inherits_from_previous_cn：承接单记录机制焦点。

- changes_argument_state_cn：把设计约束与市场质量目标（代表性、真实报告）连接。

- sets_up_next_cn：为Proposition 1的具体规则做理由铺垫。

- failure_if_removed_cn：缺少后第二补偿拍卖的规则没有存在理由。

- evidence_pointer：Section 4.1 P1 S2-S4

### 2. Section 4.1 P3 S1-S2

- order：2

- locator：Section 4.1 P3 S1-S2

- paraphrase_cn：为什么采用'选最低报告者、按第二低报告者支付'：这是VCG变体，能同时满足真实报告和参与激励。

- move_code：ARTIFACT_RATIONALE

- statement_status：theory_claim

- why_here_cn：把支付规则与经典VCG理论连接，说明不是随意发明的规则。

- inherits_from_previous_cn：依赖IR/IC约束。

- changes_argument_state_cn：把具体规则合法化为VCG家族。

- sets_up_next_cn：为多个拍卖组合成样本做铺垫。

- failure_if_removed_cn：缺少后支付规则缺乏理论依据。

- evidence_pointer：Section 4.1 P3 S1-S2

### 3. Section 4.2 P1 S3-S5

- order：3

- locator：Section 4.2 P1 S3-S5

- paraphrase_cn：为什么子群体大小必须是2：随机选择无偏但贵，选最低隐私顾虑者会引入偏差，且子群体越大偏差越大，因此最小子群体两人最优。

- move_code：ARTIFACT_RATIONALE

- statement_status：theory_claim

- why_here_cn：用排除法论证两人配对是偏差-成本权衡下的最优选择。

- inherits_from_previous_cn：依赖选最低者以控成本。

- changes_argument_state_cn：把'两人'从任意选择变为推导结论。

- sets_up_next_cn：为排序相邻配对做铺垫。

- failure_if_removed_cn：缺少后RSP的两人子群体无依据。

- evidence_pointer：Section 4.2 P1 S3-S5

### 4. Section 4.2 P2 S3-S4

- order：4

- locator：Section 4.2 P2 S3-S4

- paraphrase_cn：为什么按敏感属性排序并取相邻配对：排序使配对内敏感属性差异最小，相关时也减少隐私顾虑差异，从而同时降低偏差和成本。

- move_code：ARTIFACT_RATIONALE

- statement_status：theory_claim

- why_here_cn：这是RSP区别于普通两人拍卖的设计理由：排序相邻是双赢操作。

- inherits_from_previous_cn：依赖两人配对。

- changes_argument_state_cn：把排序从工程细节提升为偏差和成本双目标机制。

- sets_up_next_cn：为同态加密排序的隐私讨论做铺垫。

- failure_if_removed_cn：缺少后排序设计没有功能解释。

- evidence_pointer：Section 4.2 P2 S3-S4

### 5. Section 4.2 P4-P5

- order：5

- locator：Section 4.2 P4-P5

- paraphrase_cn：为什么平台排序不产生额外隐私成本：信任平台时直接访问；不信任时用同态加密；即使担心平台本身，个体理性使全用户成本同升而不影响比较。

- move_code：ARTIFACT_RATIONALE

- statement_status：author_inference

- why_here_cn：保护RSP排序步骤不受隐私成本质疑，确保理论模型一致。

- inherits_from_previous_cn：依赖排序相邻配对。

- changes_argument_state_cn：把排序工程可行性转化为模型无害性。

- sets_up_next_cn：为进入4.3节RSP完整算法做铺垫。

- failure_if_removed_cn：缺少后排序步骤可能被指引入额外隐私成本。

- evidence_pointer：Section 4.2 P4-P5

### 6. Section 4.3 P2 S1-S3

- order：6

- locator：Section 4.3 P2 S1-S3

- paraphrase_cn：为什么RSP随机滚动比较相邻配对：随机化保证每个数据主体平等入选机会，相邻比较保持配对内低差异，选低者控制成本，按对方支付保持激励相容。

- move_code：ARTIFACT_RATIONALE

- statement_status：theory_claim

- why_here_cn：说明RSP'随机'与'相邻'两个操作各自承担的功能。

- inherits_from_previous_cn：依赖排序相邻和拍卖规则。

- changes_argument_state_cn：把算法操作的每个要素对应到性能性质。

- sets_up_next_cn：为第5章E(B)=0和等入选概率推导做铺垫。

- failure_if_removed_cn：缺少后算法操作与理论性质脱节。

- evidence_pointer：Section 4.3 P2 S1-S3

### 7. Section 4.3 P3 S1-S4

- order：7

- locator：Section 4.3 P3 S1-S4

- paraphrase_cn：为什么大量拍卖可实施：类似实时竞价，计算可忽略，用户一次设置自动参与，不是人工每笔操作。

- move_code：ARTIFACT_RATIONALE

- statement_status：author_inference

- why_here_cn：在机制设计完成时直接回应工程可行性，避免审稿人质疑可部署性。

- inherits_from_previous_cn：依赖完整RSP算法。

- changes_argument_state_cn：把机制从形式设计转为可部署系统。

- sets_up_next_cn：为第5-6章的理论和仿真评估做信心铺垫。

- failure_if_removed_cn：缺少后可实施性成为论文薄弱点。

- evidence_pointer：Section 4.3 P3 S1-S4

## Study开头、过渡与收束图谱

### 1. Section 5 P1

- locator：Section 5 P1

- paraphrase_cn：本节在最坏情形下测量机制性能：数据主体隐私顾虑与敏感属性完全相关。

- move_code：STUDY_OPENING

- statement_status：method_decision

- why_here_cn：设定理论分析的默认场景，说明完全相关为何代表最坏情形。

- inherits_from_previous_cn：承接第4章机制设计。

- changes_argument_state_cn：从机制设计转向性能分析。

- sets_up_next_cn：为SRS、固定补偿、RSP闭式公式推导做铺垫。

- failure_if_removed_cn：缺少后理论章节没有分析边界。

- evidence_pointer：Section 5 P1

### 2. Section 5.2 P1

- locator：Section 5.2 P1

- paraphrase_cn：SRS基准假设平台有完整隐私信息，随机选n并支付各自保留价，理论上无偏但不可行。

- move_code：BENCHMARK_OPENING

- statement_status：method_decision

- why_here_cn：定义不可实现但最优的参照系，后文'接近基准'才有意义。

- inherits_from_previous_cn：依赖测量指标定义。

- changes_argument_state_cn：建立成本下界。

- sets_up_next_cn：为TC^SRS公式和固定补偿对比做铺垫。

- failure_if_removed_cn：缺少后RSP接近最优无法度量。

- evidence_pointer：Section 5.2 P1

### 3. Section 5.3 P1

- locator：Section 5.3 P1

- paraphrase_cn：固定补偿在c低于最高保留价时有偏，且c须介于c_L和c_H之间才能有n个参与者。

- move_code：BENCHMARK_OPENING

- statement_status：method_decision

- why_here_cn：给出固定补偿的形式化约束和两种角点策略的由来。

- inherits_from_previous_cn：依赖偏差和总补偿定义。

- changes_argument_state_cn：把固定补偿转化为可比较的FCH/FCL。

- sets_up_next_cn：为Proposition 2-3的推导做铺垫。

- failure_if_removed_cn：缺少后固定补偿无法与RSP比较。

- evidence_pointer：Section 5.3 P1

### 4. Section 5.4 P1

- locator：Section 5.4 P1

- paraphrase_cn：RSP产生无偏样本，入选概率相等，期望补偿由顺序统计量间距推导。

- move_code：RESULT_OPENING

- statement_status：empirical_result

- why_here_cn：在三类方法介绍完后给出RSP的核心理论属性。

- inherits_from_previous_cn：依赖RSP算法和顺序统计量理论。

- changes_argument_state_cn：确立RSP的无偏性和公平性。

- sets_up_next_cn：为总补偿公式和比较命题做铺垫。

- failure_if_removed_cn：缺少后RSP无偏性没有理论证据。

- evidence_pointer：Section 5.4 P1

### 5. Section 5.5 Proposition 2

- locator：Section 5.5 Proposition 2

- paraphrase_cn：等价总补偿下RSP偏差更小，等价偏差下RSP总补偿更低，即RSP支配固定补偿。

- move_code：RESULT

- statement_status：theory_claim

- why_here_cn：用逐对等价比较正式确立RSP对固定补偿的支配关系。

- inherits_from_previous_cn：依赖闭式公式。

- changes_argument_state_cn：把'更好'升级为'支配'。

- sets_up_next_cn：为Proposition 3总成本比较做铺垫。

- failure_if_removed_cn：缺少后支配固定补偿的核心结论缺失。

- evidence_pointer：Section 5.5 Proposition 2

### 6. Section 5.5 Proposition 3

- locator：Section 5.5 Proposition 3

- paraphrase_cn：除非单位偏差成本ω很小，RSP总成本低于最佳固定补偿法；即只有买方不看重偏差时固定补偿才可能更便宜。

- move_code：RESULT

- statement_status：theory_claim

- why_here_cn：把支配关系扩展到总成本，并划出固定补偿的保留区域。

- inherits_from_previous_cn：依赖Proposition 2。

- changes_argument_state_cn：引入ω作为边界条件。

- sets_up_next_cn：为图3和边界直觉解释做铺垫。

- failure_if_removed_cn：缺少后固定补偿何时有用未划界。

- evidence_pointer：Section 5.5 Proposition 3

### 7. Section 5.5 Proposition 3后一段

- locator：Section 5.5 Proposition 3后一段

- paraphrase_cn：直觉解释：ω小表示买方不因数据质量差受损，固定补偿才可能胜出；若目标零偏差，最优固定补偿仍不如RSP。

- move_code：RESULT_INTERPRETATION

- statement_status：author_inference

- why_here_cn：把数学阈值转成管理直觉，供实践读者理解边界。

- inherits_from_previous_cn：依赖ω_L阈值。

- changes_argument_state_cn：把命题从数学结果升级为管理含义。

- sets_up_next_cn：为图3和样本量分析做铺垫。

- failure_if_removed_cn：缺少后边界条件难以被非数学读者理解。

- evidence_pointer：Figure 3附近段落

### 8. Section 5.6 P1

- locator：Section 5.6 P1

- paraphrase_cn：FCH和RSP的偏差与样本量无关，FCL受样本量影响显著；FCL小样本便宜但随样本量增长更快。

- move_code：RESULT

- statement_status：theory_claim

- why_here_cn：从维度比较转向样本量维度，形成第二个设计洞见。

- inherits_from_previous_cn：依赖Table 2和总补偿公式。

- changes_argument_state_cn：把比较扩展到样本量维度。

- sets_up_next_cn：为Proposition 4平均成本分析做铺垫。

- failure_if_removed_cn：缺少后样本量洞见缺失。

- evidence_pointer：Section 5.6 P1

### 9. Section 5.6 Proposition 4

- locator：Section 5.6 Proposition 4

- paraphrase_cn：FCH平均成本随样本量下降，FCL上升，RSP在α小时上升、α大时下降、中等时非单调。

- move_code：RESULT

- statement_status：theory_claim

- why_here_cn：把样本量效应与隐私成本弹性α联系起来，增加理论的粒度。

- inherits_from_previous_cn：依赖总补偿关于n和α的导数。

- changes_argument_state_cn：建立规模经济和规模不经济的条件。

- sets_up_next_cn：为第6.4节真实数据88种样本量验证做理论预期。

- failure_if_removed_cn：缺少后样本量洞见无推导。

- evidence_pointer：Section 5.6 Proposition 4

### 10. Section 5.6 Proposition 4后两段

- locator：Section 5.6 Proposition 4后两段

- paraphrase_cn：直觉解释：FCL平均成本上升因为只支付给n个最低保留者，样本扩大必须纳入更高成本者；RSP的U型来自无放回抽样使相邻间距随样本增大而指数增大与k-anonymity降低隐私成本的拉锯。

- move_code：RESULT_INTERPRETATION

- statement_status：author_inference

- why_here_cn：给Proposition 4提供机制性解释，让U型成本可理解。

- inherits_from_previous_cn：依赖Proposition 4。

- changes_argument_state_cn：把导数结果还原为无放回抽样和k-anonymity的经济解释。

- sets_up_next_cn：为仿真章节做过渡。

- failure_if_removed_cn：缺少后样本量结果像纯数学异常。

- evidence_pointer：Section 5.6 Proposition 4后两段

### 11. Section 6 P1

- locator：Section 6 P1

- paraphrase_cn：为进一步分析机制性能，生成模拟人口数据，并用基准和本文机制抽样，最后加入行业伙伴真实数据。

- move_code：STUDY_OPENING

- statement_status：method_decision

- why_here_cn：从理论章节过渡到仿真章节，预告六种证据形态。

- inherits_from_previous_cn：依赖第5章理论模型。

- changes_argument_state_cn：把证据从解析推导扩展到有限样本。

- sets_up_next_cn：为6.1完美相关仿真做铺垫。

- failure_if_removed_cn：缺少后理论结果没有有限样本验证。

- evidence_pointer：Section 6 P1

### 12. Section 6.1 P1

- locator：Section 6.1 P1

- paraphrase_cn：考虑完美相关，用N=200、n=50、α=1，每种方法抽样50万次，将仿真值与理论值对照。

- move_code：STUDY_OPENING

- statement_status：method_decision

- why_here_cn：用可复现参数把理论命题转化为可检验仿真。

- inherits_from_previous_cn：依赖第5章结果。

- changes_argument_state_cn：建立仿真验证的理论基准。

- sets_up_next_cn：为Table 3比较做铺垫。

- failure_if_removed_cn：缺少后仿真无法与理论对应。

- evidence_pointer：Section 6.1 P1

### 13. Section 6.1 Table 4附近

- locator：Section 6.1 Table 4附近

- paraphrase_cn：用TOST两单侧t检验，SRS、FCH、RSP偏差与零等价，FCL在三个等价界内无法拒绝有偏。

- move_code：RESULT

- statement_status：empirical_result

- why_here_cn：用统计检验把无偏性从解析推导扩展到有限样本。

- inherits_from_previous_cn：依赖Table 3仿真值。

- changes_argument_state_cn：把RSP无偏性转化为可通过检验的证据。

- sets_up_next_cn：为不完美相关仿真做方法铺垫。

- failure_if_removed_cn：缺少后仿真偏差结论无统计保障。

- evidence_pointer：Section 6.1 Table 4附近

### 14. Section 6.2 P1-S3

- locator：Section 6.2 P1-S3

- paraphrase_cn：放宽到不完美相关：RSP在所有相关水平下偏差可忽略，总补偿显著低于FCH并随相关接近SRS。

- move_code：RESULT

- statement_status：empirical_result

- why_here_cn：把最坏情形结论推广到一般相关结构。

- inherits_from_previous_cn：依赖TOST和完美相关仿真。

- changes_argument_state_cn：把RSP优势从完美相关扩展到连续相关域。

- sets_up_next_cn：为beta分布稳健性做铺垫。

- failure_if_removed_cn：缺少后机制优势可能被限制在完美相关特例。

- evidence_pointer：Section 6.2 P1-S3

### 15. Section 6.2 beta段

- locator：Section 6.2 beta段

- paraphrase_cn：用随机参数beta分布（α,β在1到100）随机化100万次，结果与均匀分布一致。

- move_code：ROBUSTNESS_TEST

- statement_status：empirical_result

- why_here_cn：证明结论对分布形式不敏感。

- inherits_from_previous_cn：依赖不完美相关框架。

- changes_argument_state_cn：排除均匀分布选择带来的伪影。

- sets_up_next_cn：为6.3节beta分布下RSP与固定补偿比较做铺垫。

- failure_if_removed_cn：缺少后分布假设的选择被质疑。

- evidence_pointer：Section 6.2 beta段

### 16. Section 6.3 P1

- locator：Section 6.3 P1

- paraphrase_cn：在不完美相关下，用beta分布重复Proposition 2的等价偏差/等价补偿比较。

- move_code：RESULT

- statement_status：empirical_result

- why_here_cn：把支配固定补偿的命题从最坏情形推广到一般相关。

- inherits_from_previous_cn：依赖beta稳健性和Proposition 2。

- changes_argument_state_cn：把支配关系扩展到仿真域。

- sets_up_next_cn：为真实数据验证做铺垫。

- failure_if_removed_cn：缺少后支配结论局限在最坏情形。

- evidence_pointer：Section 6.3 P1

### 17. Section 6.4 P1

- locator：Section 6.4 P1

- paraphrase_cn：用行业伙伴Numerous Limited的444名调查对象真实数据，用三个隐私问题主成分测隐私顾虑，收入作敏感属性，相关仅0.0186。

- move_code：STUDY_OPENING

- statement_status：method_decision

- why_here_cn：把机制从模拟迁移到真实数据，检验外部有效性。

- inherits_from_previous_cn：依赖全部仿真框架。

- changes_argument_state_cn：引入真实低相关场景。

- sets_up_next_cn：为Table 5-7结果做铺垫。

- failure_if_removed_cn：缺少后机制的可操作性证据不足。

- evidence_pointer：Section 6.4 P1

### 18. Section 6.4 Table 6-7附近

- locator：Section 6.4 Table 6-7附近

- paraphrase_cn：真实数据上RSP仍通过TOST无偏检验，总补偿3.0129接近SRS 2.6211远低于FCH 10.1173，FCL偏差巨大。

- move_code：RESULT

- statement_status：empirical_result

- why_here_cn：用极低相关真实数据证明机制在实际场景可用。

- inherits_from_previous_cn：依赖真实数据和仿真流程。

- changes_argument_state_cn：把外部有效性落实到具体数字。

- sets_up_next_cn：为样本量扫描做铺垫。

- failure_if_removed_cn：缺少后真实数据验证缺失。

- evidence_pointer：Section 6.4 Table 6-7附近

### 19. Section 6.4 P2

- locator：Section 6.4 P2

- paraphrase_cn：对n从5到440共88种样本量重复实验，结果与理论发现一致。

- move_code：RESULT

- statement_status：empirical_result

- why_here_cn：把真实数据验证扩展到样本量维度。

- inherits_from_previous_cn：依赖Proposition 4和真实数据。

- changes_argument_state_cn：确认样本量洞见在真实场景成立。

- sets_up_next_cn：为第7节部分信息比较做铺垫。

- failure_if_removed_cn：缺少后样本量结论只有模拟支持。

- evidence_pointer：Section 6.4 P2

### 20. Section 7 P1

- locator：Section 7 P1

- paraphrase_cn：扩展分析平台拥有数据主体隐私顾虑部分信息的情形，把不确定性建模为区间宽度d。

- move_code：STUDY_OPENING

- statement_status：method_decision

- why_here_cn：提出竞争路径的公平比较框架，回应用集中优化更好的可能质疑。

- inherits_from_previous_cn：依赖真实数据验证完成。

- changes_argument_state_cn：把比较对象从固定补偿转向集中优化。

- sets_up_next_cn：为COH/COL推导做铺垫。

- failure_if_removed_cn：缺少后结论中'放弃部分信息'无证据。

- evidence_pointer：Section 7 P1

### 21. Section 7 P2-P3

- locator：Section 7 P2-P3

- paraphrase_cn：集中优化若需无偏样本，随机选n人并按区间上界支付；偏差成本小时选低补偿有偏样本COL，偏差成本大时选零偏差随机样本COH。

- move_code：BENCHMARK_OPENING

- statement_status：method_decision

- why_here_cn：把集中优化建模为两种角点解，以便与RSP公平比较。

- inherits_from_previous_cn：依赖区间不确定性模型。

- changes_argument_state_cn：定义竞争策略的成本结构。

- sets_up_next_cn：为Proposition 5做铺垫。

- failure_if_removed_cn：缺少后集中优化比较缺乏基准。

- evidence_pointer：Section 7 P2-P3

### 22. Section 7 Proposition 5

- locator：Section 7 Proposition 5

- paraphrase_cn：当不确定性d超过阈值d̂时，RSP总补偿低于零偏差集中优化COH。

- move_code：RESULT

- statement_status：theory_claim

- why_here_cn：给出RSP优于集中优化的正式条件。

- inherits_from_previous_cn：依赖COH补偿公式与RSP总补偿。

- changes_argument_state_cn：把集中优化比下去的条件形式化。

- sets_up_next_cn：为阈值现实很小的论证做铺垫。

- failure_if_removed_cn：缺少后RSP优于集中优化无命题支撑。

- evidence_pointer：Section 7 Proposition 5

### 23. Section 7 Proposition 5后两段

- locator：Section 7 Proposition 5后两段

- paraphrase_cn：阈值d̂随n增加，上界(2H_{N+2}-3)/N在N=1000时<0.012，在N=100000时<0.00022，因此现实平台几乎总是RSP主导，应放弃部分信息。

- move_code：RESULT_INTERPRETATION

- statement_status：theory_claim

- why_here_cn：用数值例子把数学阈值转成强烈实践建议。

- inherits_from_previous_cn：依赖Proposition 5。

- changes_argument_state_cn：把条件优势升级为几乎普适。

- sets_up_next_cn：为第8章结论做铺垫。

- failure_if_removed_cn：缺少后'应放弃部分信息'的主张缺乏数值支撑。

- evidence_pointer：Section 7 Proposition 5后两段

### 24. Section 8 P1

- locator：Section 8 P1

- paraphrase_cn：结论重述个体数据价值、收集过程不透明、隐私工具偏差、监管要求同意等问题，说明需要新机制。

- move_code：DISCUSSION_OPENING

- statement_status：author_inference

- why_here_cn：把全文结果与引言开头的问题闭环。

- inherits_from_previous_cn：依赖全部理论、仿真、真实数据和部分信息结果。

- changes_argument_state_cn：从证据转向研究意义。

- sets_up_next_cn：为机制贡献总结做铺垫。

- failure_if_removed_cn：缺少后结论与引言脱节。

- evidence_pointer：Section 8 P1

### 25. Section 8 P2

- locator：Section 8 P2

- paraphrase_cn：本文首次提出产生无偏个体数据样本的机制，不依赖隐私顾虑分布，不受虚报影响。

- move_code：CONTRIBUTION

- statement_status：contribution_claim

- why_here_cn：重复最核心的理论贡献声明。

- inherits_from_previous_cn：依赖结论重述。

- changes_argument_state_cn：把'无偏样本'置为第一贡献。

- sets_up_next_cn：为与基准比较结果做铺垫。

- failure_if_removed_cn：缺少后核心贡献在结论缺失。

- evidence_pointer：Section 8 P2

### 26. Section 8 P3

- locator：Section 8 P3

- paraphrase_cn：理论结果显示机制无偏、总成本接近最佳基准、支配固定补偿、优于有部分信息的集中优化。

- move_code：RESULT

- statement_status：empirical_result

- why_here_cn：用最紧凑形式复述第5-7章核心结果。

- inherits_from_previous_cn：依赖全部证据。

- changes_argument_state_cn：把结果作为贡献的支撑。

- sets_up_next_cn：为理论贡献段落做铺垫。

- failure_if_removed_cn：缺少后贡献主张无结果支撑。

- evidence_pointer：Section 8 P3

### 27. Section 8 P4

- locator：Section 8 P4

- paraphrase_cn：研究对数据市场文献的贡献是提出含中介平台、个体理性、激励相容、近最优成本无偏样本的机制，并提供样本量和匿名性洞见。

- move_code：CONTRIBUTION

- statement_status：contribution_claim

- why_here_cn：把贡献与文献综述中的缺口对齐。

- inherits_from_previous_cn：依赖结果复述。

- changes_argument_state_cn：把技术结果升华为文献贡献。

- sets_up_next_cn：为实践贡献段落做铺垫。

- failure_if_removed_cn：缺少后文献贡献不清楚。

- evidence_pointer：Section 8 P4

### 28. Section 8 P5

- locator：Section 8 P5

- paraphrase_cn：不同于依赖差分隐私的复杂技术，本文用简单采样和常规拍卖，可实施且符合透明同意监管。

- move_code：CONTRIBUTION

- statement_status：contribution_claim

- why_here_cn：把实践贡献从性能转向可实施和合规。

- inherits_from_previous_cn：依赖理论贡献。

- changes_argument_state_cn：把贡献从理论延伸至实践。

- sets_up_next_cn：为限制和未来研究做铺垫。

- failure_if_removed_cn：缺少后实践价值不完整。

- evidence_pointer：Section 8 P5

### 29. Section 8 P6

- locator：Section 8 P6

- paraphrase_cn：未来研究包括买方样本量选择、隐私成本诱导操作化、经验估计模型参数、平台和买方定价与盈利。

- move_code：LIMITATION_AND_FUTURE

- statement_status：author_inference

- why_here_cn：划定研究边界，防止贡献被泛化。

- inherits_from_previous_cn：依赖全文未建模因素。

- changes_argument_state_cn：从贡献宣告转向边界声明。

- sets_up_next_cn：结束全文。

- failure_if_removed_cn：缺少后研究边界不清。

- evidence_pointer：Section 8 P6

## 讨论与贡献逐句图谱

### 1. Section 8 P1 S1

- order：1

- locator：Section 8 P1 S1

- paraphrase_cn：个体级数据对企业有巨大潜力，互联网使用增长为线上收集创造大量机会。

- move_code：CONTEXT_RETURN

- statement_status：fact

- why_here_cn：结论开篇回到数据价值，与引言P2呼应。

- inherits_from_previous_cn：承接第7节部分信息结果。

- changes_argument_state_cn：把研究重新放回宏观背景。

- sets_up_next_cn：为数据市场问题重述做铺垫。

- failure_if_removed_cn：缺少后结论缺少背景重置。

- evidence_pointer：Section 8 P1 S1

### 2. Section 8 P1 S2

- order：2

- locator：Section 8 P1 S2

- paraphrase_cn：但当前个体数据收集过程对数据主体和买方不透明，造成问题性数据市场。

- move_code：CONTEXT_RETURN

- statement_status：author_inference

- why_here_cn：重述论文开端的数据市场问题。

- inherits_from_previous_cn：依赖数据价值背景。

- changes_argument_state_cn：把问题重新聚焦。

- sets_up_next_cn：为隐私工具和偏差重述做铺垫。

- failure_if_removed_cn：缺少后结论的问题重述缺失。

- evidence_pointer：Section 8 P1 S2

### 3. Section 8 P1 S3-S6

- order：3

- locator：Section 8 P1 S3-S6

- paraphrase_cn：数据主体日益担心隐私，补偿缺失促使他们使用隐私工具，过滤经纪商触达，导致隐私不敏感者过度代表和样本不具代表性。

- move_code：RESULT_INTERPRETATION

- statement_status：author_inference

- why_here_cn：把引言的偏差机制再述一遍，让结论自洽。

- inherits_from_previous_cn：依赖问题市场重述。

- changes_argument_state_cn：重述偏差机制为贡献铺垫。

- sets_up_next_cn：为监管要求做铺垫。

- failure_if_removed_cn：缺少后结论中的偏差问题缺少因果链。

- evidence_pointer：Section 8 P1 S3-S6

### 4. Section 8 P1 S7

- order：4

- locator：Section 8 P1 S7

- paraphrase_cn：监管要求无同意不得收集个体数据，需要新机制以合理价格提供高质量数据、获得同意并直接补偿隐私损失。

- move_code：CONTEXT_RETURN

- statement_status：author_inference

- why_here_cn：把合规需求再次作为机制必要性收束。

- inherits_from_previous_cn：依赖偏差和监管问题。

- changes_argument_state_cn：把问题收拢到'需要新机制'。

- sets_up_next_cn：为第2段本研究贡献做铺垫。

- failure_if_removed_cn：缺少后机制必要性不完整。

- evidence_pointer：Section 8 P1 S7

### 5. Section 8 P2 S1

- order：5

- locator：Section 8 P2 S1

- paraphrase_cn：本研究提出一种新的算法化市场机制，为个体数据创造可行市场。

- move_code：CONTRIBUTION

- statement_status：contribution_claim

- why_here_cn：正式转入贡献声明。

- inherits_from_previous_cn：依赖新机制需要。

- changes_argument_state_cn：从需求转向供应方案。

- sets_up_next_cn：为中介平台和拍卖采样组合做铺垫。

- failure_if_removed_cn：缺少后结论贡献无总起句。

- evidence_pointer：Section 8 P2 S1

### 6. Section 8 P2 S2

- order：6

- locator：Section 8 P2 S2

- paraphrase_cn：方法采用中介平台，结合拍卖机制和采样算法，向买方提供无偏低成本个体级数据样本。

- move_code：CONTRIBUTION

- statement_status：contribution_claim

- why_here_cn：复述制品组成和功能。

- inherits_from_previous_cn：依赖市场机制提案。

- changes_argument_state_cn：把贡献具体化。

- sets_up_next_cn：为独特机制能力做铺垫。

- failure_if_removed_cn：缺少后贡献缺少技术内容。

- evidence_pointer：Section 8 P2 S2

### 7. Section 8 P2 S3

- order：7

- locator：Section 8 P2 S3

- paraphrase_cn：机制独特地使平台诱导真实报告并按隐私偏好补偿数据主体。

- move_code：CONTRIBUTION

- statement_status：contribution_claim

- why_here_cn：强调激励相容作为独特属性。

- inherits_from_previous_cn：依赖制品组成。

- changes_argument_state_cn：把贡献锁定在激励机制。

- sets_up_next_cn：为与文献对比做铺垫。

- failure_if_removed_cn：缺少后激励相容贡献缺失。

- evidence_pointer：Section 8 P2 S3

### 8. Section 8 P2 S4

- order：8

- locator：Section 8 P2 S4

- paraphrase_cn：文献有产生无偏聚合统计或噪声数据的方法，但据我们所知本文是第一个创建无偏个体数据样本的机制。

- move_code：CONTRIBUTION

- statement_status：contribution_claim

- why_here_cn：用'首次'界定最高层创新。

- inherits_from_previous_cn：依赖独特机制能力。

- changes_argument_state_cn：把贡献从'好机制'升级为'首次解决'。

- sets_up_next_cn：为不依赖分布和虚报做铺垫。

- failure_if_removed_cn：缺少后无偏样本的独特贡献缺失。

- evidence_pointer：Section 8 P2 S4

### 9. Section 8 P2 S5

- order：9

- locator：Section 8 P2 S5

- paraphrase_cn：方法不依赖隐私顾虑分布，不受用户虚报隐私顾虑的影响。

- move_code：CONTRIBUTION

- statement_status：contribution_claim

- why_here_cn：点明方法在假设放松上的优势。

- inherits_from_previous_cn：依赖'首次'声明。

- changes_argument_state_cn：把贡献扩展为假设需求低。

- sets_up_next_cn：为结果复述做铺垫。

- failure_if_removed_cn：缺少后假设放松优势不明显。

- evidence_pointer：Section 8 P2 S5

### 10. Section 8 P3 S1

- order：10

- locator：Section 8 P3 S1

- paraphrase_cn：为分析性能，我们比较偏差、总补偿、总成本、排除率和不平等指标。

- move_code：RESULT

- statement_status：empirical_result

- why_here_cn：复述评价指标体系。

- inherits_from_previous_cn：依赖贡献声明。

- changes_argument_state_cn：把贡献声明转回证据。

- sets_up_next_cn：为理论结果复述做铺垫。

- failure_if_removed_cn：缺少后结果复述缺少指标基础。

- evidence_pointer：Section 8 P3 S1

### 11. Section 8 P3 S2

- order：11

- locator：Section 8 P3 S2

- paraphrase_cn：理论结果显示机制提供无偏数据，总成本接近最佳基准，且在买方关注数据质量时支配固定补偿。

- move_code：RESULT

- statement_status：empirical_result

- why_here_cn：浓缩复述第5章理论结果。

- inherits_from_previous_cn：依赖指标列表。

- changes_argument_state_cn：把理论结果作为贡献的直接证据。

- sets_up_next_cn：为优于集中优化做铺垫。

- failure_if_removed_cn：缺少后理论贡献无支撑。

- evidence_pointer：Section 8 P3 S2

### 12. Section 8 P3 S3

- order：12

- locator：Section 8 P3 S3

- paraphrase_cn：机制还优于拥有部分信息的集中优化。

- move_code：RESULT

- statement_status：empirical_result

- why_here_cn：把第二个对手也被超越的结果纳入结论。

- inherits_from_previous_cn：依赖固定补偿支配。

- changes_argument_state_cn：覆盖全部竞争方法。

- sets_up_next_cn：为反直觉建议做铺垫。

- failure_if_removed_cn：缺少后集中优化结论缺失。

- evidence_pointer：Section 8 P3 S3

### 13. Section 8 P3 S4

- order：13

- locator：Section 8 P3 S4

- paraphrase_cn：令人惊讶的是，平台应放弃通过监测行为收集的任何不完美的用户隐私偏好估计。

- move_code：BOUNDARY_CONDITION

- statement_status：author_inference

- why_here_cn：把性能比较转为强管理建议。

- inherits_from_previous_cn：依赖优于集中优化。

- changes_argument_state_cn：把结果升级为反直觉洞见。

- sets_up_next_cn：为采用本文方法做铺垫。

- failure_if_removed_cn：缺少后本文最强实践洞见缺失。

- evidence_pointer：Section 8 P3 S4

### 14. Section 8 P3 S5

- order：14

- locator：Section 8 P3 S5

- paraphrase_cn：平台改用本文方法将获得更好结果。

- move_code：BOUNDARY_CONDITION

- statement_status：author_inference

- why_here_cn：给出替代行动。

- inherits_from_previous_cn：依赖放弃估计建议。

- changes_argument_state_cn：把建议落为行动方案。

- sets_up_next_cn：为直取真实信息解释做铺垫。

- failure_if_removed_cn：缺少后建议没有落点。

- evidence_pointer：Section 8 P3 S5

### 15. Section 8 P3 S6

- order：15

- locator：Section 8 P3 S6

- paraphrase_cn：这表明直接从数据主体获取真实信息的能力胜过集中优化中使用估计隐私顾虑的潜在收益。

- move_code：RESULT_INTERPRETATION

- statement_status：author_inference

- why_here_cn：给出反直觉结果的机制解释。

- inherits_from_previous_cn：依赖采用本文方法的建议。

- changes_argument_state_cn：把性能优势转化为原理优势。

- sets_up_next_cn：为文献贡献段落做铺垫。

- failure_if_removed_cn：缺少后反直觉结论缺乏解释。

- evidence_pointer：Section 8 P3 S6

### 16. Section 8 P4 S1

- order：16

- locator：Section 8 P4 S1

- paraphrase_cn：本研究对数据市场文献做出重要贡献。

- move_code：CONTRIBUTION

- statement_status：contribution_claim

- why_here_cn：开启文献贡献段落。

- inherits_from_previous_cn：依赖全部结果。

- changes_argument_state_cn：从结果转向文献意义。

- sets_up_next_cn：为先前文献对比做铺垫。

- failure_if_removed_cn：缺少后文献贡献没有总起。

- evidence_pointer：Section 8 P4 S1

### 17. Section 8 P4 S2

- order：17

- locator：Section 8 P4 S2

- paraphrase_cn：先前研究聚焦数据主体与分析者直接交易，提出联合补偿-估计机制获取有偏数据样本，目标是最小化估计误差与补偿之和。

- move_code：CONTRIBUTION

- statement_status：contribution_claim

- why_here_cn：用一句话概括被超越的文献路线。

- inherits_from_previous_cn：依赖文献贡献开启。

- changes_argument_state_cn：确立对比基线。

- sets_up_next_cn：为本文差异做铺垫。

- failure_if_removed_cn：缺少后对比不成立。

- evidence_pointer：Section 8 P4 S2

### 18. Section 8 P4 S3

- order：18

- locator：Section 8 P4 S3

- paraphrase_cn：我们相反提出个体理性且激励相容的市场机制，由中介平台向买方提供近最优成本的个体级无偏样本。

- move_code：CONTRIBUTION

- statement_status：contribution_claim

- why_here_cn：把本文与文献基线逐点对比。

- inherits_from_previous_cn：依赖文献基线。

- changes_argument_state_cn：确立本文独特位置。

- sets_up_next_cn：为样本量和匿名性洞见做铺垫。

- failure_if_removed_cn：缺少后文献贡献定位失败。

- evidence_pointer：Section 8 P4 S3

### 19. Section 8 P4 S4

- order：19

- locator：Section 8 P4 S4

- paraphrase_cn：我们还提供样本规模和匿名性对机制性能影响的洞见。

- move_code：CONTRIBUTION

- statement_status：contribution_claim

- why_here_cn：复述辅助理论贡献。

- inherits_from_previous_cn：依赖市场机制贡献。

- changes_argument_state_cn：补充贡献清单。

- sets_up_next_cn：为实践贡献做铺垫。

- failure_if_removed_cn：缺少后辅助洞见未进结论。

- evidence_pointer：Section 8 P4 S4

### 20. Section 8 P5 S1

- order：20

- locator：Section 8 P5 S1

- paraphrase_cn：本研究对个体数据行业有重要含义。

- move_code：CONTRIBUTION

- statement_status：contribution_claim

- why_here_cn：开启实践贡献段落。

- inherits_from_previous_cn：依赖理论贡献。

- changes_argument_state_cn：从理论转向实践。

- sets_up_next_cn：为差分隐私对比做铺垫。

- failure_if_removed_cn：缺少后实践贡献没有总起。

- evidence_pointer：Section 8 P5 S1

### 21. Section 8 P5 S2

- order：21

- locator：Section 8 P5 S2

- paraphrase_cn：与依赖差分隐私等复杂技术不同，本文提供更务实方案。

- move_code：CONTRIBUTION

- statement_status：contribution_claim

- why_here_cn：用替代技术路线突出可实施性。

- inherits_from_previous_cn：依赖实践贡献开启。

- changes_argument_state_cn：把可实施性与复杂技术对比。

- sets_up_next_cn：为简单采样和常规拍卖做铺垫。

- failure_if_removed_cn：缺少后可实施性缺少对照。

- evidence_pointer：Section 8 P5 S2

### 22. Section 8 P5 S3

- order：22

- locator：Section 8 P5 S3

- paraphrase_cn：我们用直接了当的采样算法和常规补偿机制，可在真实数据市场实施。

- move_code：CONTRIBUTION

- statement_status：contribution_claim

- why_here_cn：把可实施性落实到具体构件。

- inherits_from_previous_cn：依赖差分隐私对比。

- changes_argument_state_cn：把技术简单性转为市场可用。

- sets_up_next_cn：为实践优势做铺垫。

- failure_if_removed_cn：缺少后可实施性不具体。

- evidence_pointer：Section 8 P5 S3

### 23. Section 8 P5 S4

- order：23

- locator：Section 8 P5 S4

- paraphrase_cn：机制具有实践优势，是当前数据市场实践的可行替代。

- move_code：CONTRIBUTION

- statement_status：contribution_claim

- why_here_cn：重申实践替代地位。

- inherits_from_previous_cn：依赖可实施性。

- changes_argument_state_cn：把技术可行性升为市场替代方案。

- sets_up_next_cn：为性能复述做铺垫。

- failure_if_removed_cn：缺少后实践地位不明确。

- evidence_pointer：Section 8 P5 S4

### 24. Section 8 P5 S5

- order：24

- locator：Section 8 P5 S5

- paraphrase_cn：通过理论分析和仿真，我们证明机制始终接近最佳基准，在现实场景中相对固定补偿和集中优化在所有指标上更优。

- move_code：RESULT

- statement_status：empirical_result

- why_here_cn：再次用结果支撑实践贡献。

- inherits_from_previous_cn：依赖实践替代。

- changes_argument_state_cn：把实践贡献绑定到性能证据。

- sets_up_next_cn：为合规性做铺垫。

- failure_if_removed_cn：缺少后实践贡献无证据。

- evidence_pointer：Section 8 P5 S5

### 25. Section 8 P5 S6

- order：25

- locator：Section 8 P5 S6

- paraphrase_cn：这使创建有效的个人数据市场成为可能，既利于数据主体和买方，又符合透明和同意的监管要求。

- move_code：CONTRIBUTION

- statement_status：contribution_claim

- why_here_cn：把贡献与社会价值监管合规对接。

- inherits_from_previous_cn：依赖性能证据。

- changes_argument_state_cn：完成实践贡献的规范收尾。

- sets_up_next_cn：为未来研究做铺垫。

- failure_if_removed_cn：缺少后合规贡献缺失。

- evidence_pointer：Section 8 P5 S6

### 26. Section 8 P6 S1

- order：26

- locator：Section 8 P6 S1

- paraphrase_cn：未来研究可以设想多个方向。

- move_code：LIMITATION_AND_FUTURE

- statement_status：author_inference

- why_here_cn：开启边界和未来段。

- inherits_from_previous_cn：依赖全文贡献完成。

- changes_argument_state_cn：从贡献转向边界。

- sets_up_next_cn：为买方样本量选择做铺垫。

- failure_if_removed_cn：缺少后边界部分无总起。

- evidence_pointer：Section 8 P6 S1

### 27. Section 8 P6 S2

- order：27

- locator：Section 8 P6 S2

- paraphrase_cn：虽然我们提供样本大小洞见，但未直接建模买方样本量选择，这是未来研究主题。

- move_code：LIMITATION_AND_FUTURE

- statement_status：author_inference

- why_here_cn：承认一个未建模因素。

- inherits_from_previous_cn：依赖未来方向开启。

- changes_argument_state_cn：划出第一个边界。

- sets_up_next_cn：为隐私成本操作化做铺垫。

- failure_if_removed_cn：缺少后样本量边界不明。

- evidence_pointer：Section 8 P6 S2

### 28. Section 8 P6 S3

- order：28

- locator：Section 8 P6 S3

- paraphrase_cn：在平台数据主体上操作化隐私成本诱导值得未来研究，例如平台呈现合理补偿范围让用户选择。

- move_code：LIMITATION_AND_FUTURE

- statement_status：author_inference

- why_here_cn：指出从理论机制到实施的接口需要实际测量方法。

- inherits_from_previous_cn：依赖第一个未建模因素。

- changes_argument_state_cn：把未来研究指向操作化。

- sets_up_next_cn：为风险态度方法类比做铺垫。

- failure_if_removed_cn：缺少后操作化边界缺失。

- evidence_pointer：Section 8 P6 S3

### 29. Section 8 P6 S4

- order：29

- locator：Section 8 P6 S4

- paraphrase_cn：这类似于测量风险态度的程序，如Holt和Laury或Binswanger的二元选择列表。

- move_code：LIMITATION_AND_FUTURE

- statement_status：prior_literature

- why_here_cn：用成熟方法说明未来研究并非不可行。

- inherits_from_previous_cn：依赖隐私成本诱导。

- changes_argument_state_cn：为未来方法提供先例。

- sets_up_next_cn：为经验估计其他参数做铺垫。

- failure_if_removed_cn：缺少后未来研究缺少方法锚点。

- evidence_pointer：Section 8 P6 S4

### 30. Section 8 P6 S5

- order：30

- locator：Section 8 P6 S5

- paraphrase_cn：经验估计隐私成本对匿名性弹性或平台不确定性参数也很有趣。

- move_code：LIMITATION_AND_FUTURE

- statement_status：author_inference

- why_here_cn：把未来研究扩展到参数估计。

- inherits_from_previous_cn：依赖操作化讨论。

- changes_argument_state_cn：确认模型参数经验基础欠缺。

- sets_up_next_cn：为平台和买方选择做铺垫。

- failure_if_removed_cn：缺少后参数估计边界缺失。

- evidence_pointer：Section 8 P6 S5

### 31. Section 8 P6 S6

- order：31

- locator：Section 8 P6 S6

- paraphrase_cn：本文未考虑平台和买方的选择，未来可研究平台和买方盈利、平台定价和买方样本购买决策。

- move_code：LIMITATION_AND_FUTURE

- statement_status：author_inference

- why_here_cn：把最后一个边界划在平台和买方行为。

- inherits_from_previous_cn：依赖参数估计讨论。

- changes_argument_state_cn：承认市场双侧动态未被建模。

- sets_up_next_cn：结束全文。

- failure_if_removed_cn：缺少后市场双侧边界缺失。

- evidence_pointer：Section 8 P6 S6

## Study累积逻辑

### 1. 1

- study_or_phase：机制设计阶段（第4章）

- evidence_job_cn：构建能够在理论上满足激励相容、个体理性、无偏和低成本四个条件的算法化市场机制。

- what_it_establishes_cn：第二补偿拍卖是IC且IR的；两人相邻配对能同时控制偏差和成本；RSP算法给出可复现的操作规则。

- what_it_cannot_establish_cn：只给出机制，没有证明相对固定补偿和集中优化有可量化优势，也没有证明有限样本和真实数据下仍有效。

- why_next_phase_is_needed_cn：需要把机制放到与替代方法的正式比较中，才能回答'为什么更优'。

- transition_wording_function_cn：第5章开头'在最坏情形下测量性能'即从设计转到比较。

### 2. 2

- study_or_phase：最坏情形理论分析（第5章）

- evidence_job_cn：在完全相关假设下推导RSP与SRS、FCH/FCL的闭式性能，证明RSP支配固定补偿并接近SRS。

- what_it_establishes_cn：E(B^RSP)=0；E(TC^RSP)接近SRS；Proposition 2-4给出支配、总成本和样本量边界。

- what_it_cannot_establish_cn：完全相关和连续分布是理想条件；不知道有限样本和实际相关程度下结论是否成立。

- why_next_phase_is_needed_cn：需要使用有限样本仿真验证解析结果，并放宽相关性假设检验稳健性。

- transition_wording_function_cn：第6章开头'为进一步分析机制性能，生成模拟人口数据'把理论结果转向仿真验证。

### 3. 3

- study_or_phase：完美相关仿真（6.1）

- evidence_job_cn：用50万次仿真确认第5章理论结果不是解析伪影，并用TOST检验无偏性。

- what_it_establishes_cn：仿真值与Table 2理论值一致；SRS、FCH、RSP通过TOST，FCL被判定有偏。

- what_it_cannot_establish_cn：完美相关仍是最坏上限，不代表一般相关和现实数据。

- why_next_phase_is_needed_cn：需要放宽完美相关假设，检验机制在一般相关场景是否仍占优。

- transition_wording_function_cn：6.2开头'扩展仿真分析到不完美相关'直接承接。

### 4. 4

- study_or_phase：不完美相关与beta稳健性（6.2-6.3）

- evidence_job_cn：检验相关程度和分布形式变化时RSP的性能，并把支配固定补偿扩展到一般场景。

- what_it_establishes_cn：所有相关水平下RSP偏差可忽略；总补偿显著低于FCH并接近SRS；相关超过阈值时支配固定补偿；beta分布结果一致。

- what_it_cannot_establish_cn：仍是模拟数据，没有真实数据主体的拍卖行为、支付和策略报告。

- why_next_phase_is_needed_cn：需要真实调查数据证明机制在现实世界数据上同样工作。

- transition_wording_function_cn：6.4开头'测试我们的机制使用行业伙伴的真实数据集'完成从模拟到真实的升级。

### 5. 5

- study_or_phase：真实数据验证（6.4）

- evidence_job_cn：用Numerous Limited的444名调查对象数据验证机制在极低相关（0.0186）下的外部有效性，并扫描样本量。

- what_it_establishes_cn：RSP通过TOST无偏；总补偿3.0129接近SRS 2.6211远低于FCH 10.1173；88种样本量结果与理论一致。

- what_it_cannot_establish_cn：真实调查不是真实市场拍卖，没有真实支付和用户策略行为；未包含高相关真实场景。

- why_next_phase_is_needed_cn：真实数据验证还没有回应'平台有部分信息时是否该用集中优化'这一集中优化拥趸的反驳。

- transition_wording_function_cn：第7章开头'扩展分析到平台拥有部分隐私顾虑信息情形'把比较扩展到信息假设。

### 6. 6

- study_or_phase：部分信息与集中优化比较（第7章）

- evidence_job_cn：在区间不确定性模型下证明RSP相对集中优化COH/COL的优势阈值。

- what_it_establishes_cn：Proposition 5给出d̂阈值；现实人口规模N≥1000时d̂<0.012，N=100000时<0.00022，因此RSP几乎总是更优。

- what_it_cannot_establish_cn：真实平台隐私顾虑估计误差未必是均匀区间；未考虑获取部分信息的成本；未做行为实验验证平台是否会真正放弃信息。

- why_next_phase_is_needed_cn：证据链完整后需要结论把结果回接到文献缺口、贡献和边界。

- transition_wording_function_cn：第8章开头重述问题并总结贡献，完成闭环。

## 主张—证据台账

### 1. 第二补偿拍卖满足个体理性和激励相容。

- claim_cn：第二补偿拍卖满足个体理性和激励相容。

- claim_level：mechanism

- supporting_evidence_cn：Proposition 1的数学证明，依托VCG变体理论。

- support_strength：direct

- where_claim_is_made：Section 4.1 Proposition 1

- where_evidence_is_provided：Section 4.1 Proposition 1

### 2. RSP产生无偏个体数据样本。

- claim_cn：RSP产生无偏个体数据样本。

- claim_level：artifact

- supporting_evidence_cn：第5.4节推导E(B^RSP)=0；6.1和6.4节TOST检验p值极小，偏差与零等价。

- support_strength：direct

- where_claim_is_made：Section 5.4, Table 2

- where_evidence_is_provided：Section 6.1 Table 3-4; Section 6.4 Table 6-7

### 3. RSP总补偿接近最佳基准SRS。

- claim_cn：RSP总补偿接近最佳基准SRS。

- claim_level：artifact

- supporting_evidence_cn：Table 2理论值RSP 0.5056对SRS 0.5；真实数据RSP 3.0129对SRS 2.6211，远低于FCH 10.1173。

- support_strength：direct

- where_claim_is_made：Section 5.4 和引言1.2 P5 S2

- where_evidence_is_provided：Table 2; Table 6

### 4. RSP支配固定补偿。

- claim_cn：RSP支配固定补偿。

- claim_level：artifact

- supporting_evidence_cn：Proposition 2等价总补偿/等价偏差下的支配关系；Proposition 3多数ω下总成本更低；图3和图7验证。

- support_strength：direct

- where_claim_is_made：Section 5.5 Propositions 2-3

- where_evidence_is_provided：Section 5.5; Section 6.3 Figure 7

### 5. 固定补偿只在偏差不重要（ω很小）时可能更便宜。

- claim_cn：固定补偿只在偏差不重要（ω很小）时可能更便宜。

- claim_level：boundary

- supporting_evidence_cn：Proposition 3给出ω<ω_L的边界条件，并辅以直觉解释。

- support_strength：direct

- where_claim_is_made：Section 5.5 Proposition 3后

- where_evidence_is_provided：Section 5.5 Proposition 3

### 6. 即使平台有部分隐私顾虑信息，RSP也优于集中优化。

- claim_cn：即使平台有部分隐私顾虑信息，RSP也优于集中优化。

- claim_level：design_knowledge

- supporting_evidence_cn：Proposition 5给出d̂阈值；现实人口规模N=1000时d̂<0.012，N=100000时<0.00022。

- support_strength：partial

- where_claim_is_made：Section 7 Proposition 5后；引言1.2 P5 S4

- where_evidence_is_provided：Section 7 Proposition 5与阈值讨论

### 7. 机制可实际实施且计算负担可接受。

- claim_cn：机制可实际实施且计算负担可接受。

- claim_level：artifact

- supporting_evidence_cn：第4.3节用实时竞价类比说明计算可忽略；用户偏好一次设置自动参与。

- support_strength：asserted

- where_claim_is_made：Section 4.3 P3

- where_evidence_is_provided：Section 4.3 P3；无实际部署或运行时间测量

### 8. 本文首次创建无偏个体数据样本而非从有偏样本得无偏估计。

- claim_cn：本文首次创建无偏个体数据样本而非从有偏样本得无偏估计。

- claim_level：theory

- supporting_evidence_cn：第2章文献综述区分联合补偿-估计机制与本文；第8章P2 S4明确首次声明。

- support_strength：asserted

- where_claim_is_made：Section 2 P4; Section 8 P2 S4

- where_evidence_is_provided：文献综述中的对比分析

## ISR定位逻辑

- constitutive_is_problem_cn：论文把数据市场问题构成为数字平台、数据主体行为与市场机制三者互相构成的问题：平台中介缺失导致市场不透明，数据主体的隐私工具使用反过来造成样本偏差，买方依赖低质数据又压低广告回报，从而形成'技术-行为-市场'闭环。本文提出的不是单纯算法，而是一个改变平台治理结构的市场机制，使平台从估值者变为市场组织者。

- technology_behavior_or_market_entanglement_cn：技术设计嵌入行为和市场逻辑：第二补偿拍卖利用数据主体的策略性报告行为实现真实披露；排序相邻配对利用敏感属性与隐私顾虑的相关性同时控制偏差与成本；平台用同态加密排序使自己不接触敏感属性，从而不改变隐私成本；隐私工具使用这一用户保护行为被转化为样本偏差机制，成为市场机制要解决的核心问题。

- role_of_benchmark_or_objective_evidence_cn：SRS、FCH/FCL、COH/COL不只是算法对比，而是分别代表理论理想、现状实践和信息受限的集中优化。闭式公式、TOST检验和真实数据仿真被用来支持'RSP在无偏性、成本和公平性上同时成立'这一IS层面的主张，即平台应重新设计市场规则而非追加用户数据估计。

- theory_in_design_cn：理论直接进入设计：VCG拍卖理论决定支付规则；顺序统计量的相邻间距决定排序配对；k-anonymity决定隐私成本函数γ=vn^{-α}；个体理性和激励相容作为机制约束；这些理论不是事后解释结果，而是预先塑造算法结构。

- technical_vs_is_contribution_balance_cn：文章把技术贡献（拍卖+采样算法）始终放在数据市场治理和激励机制中论述：摘要强调机制而非算法；引言强调补偿缺位和合规；结论强调平台应放弃部分信息估计。技术细节（序贯抽样、闭式公式）服务于'激励相容市场机制可以同时解决偏差与成本'这一IS核心命题。

- beyond_transient_performance_cn：论文通过三条方式超越一时性能优势：一是在假设放松层面，不要求隐私顾虑分布已知、不要求用户理解复杂数学；二是在信息不利层面，证明平台有部分信息也应放弃；三是在规范层面，机制同时实现同意、透明、补偿、公平等治理价值，而不是只声称分数优势。

## 段落级仿写模板

### abstract_steps

1. 第一句用宏大但具体的现实背景建立研究对象。

2. 第二句把背景转成缺陷，并指出新兴平台的出现。

3. 第三句扩展应用场景。

4. 第四句指出现有平台两类机制导致昂贵或有偏样本。

5. 第五句提出本文机制及其三个功能。

6. 第六句用概括句开启结果。

7. 第七句给出最强反直觉结果。

8. 第八句列出辅助洞见。

### introduction_paragraph_steps

1. 用应用需求开头，直接给出方案再预告缺陷。

2. 用规模数据建立市场价值。

3. 揭示第三方收集和补偿缺失。

4. 用隐私工具使用建立偏差机制，并引用行业数据。

5. 引入监管形成根本变革需要。

6. 在1.1节用现实平台例子把问题具体化。

7. 详细分析固定补偿和集中优化两类缺陷，为机制创造缺口。

8. 在1.2节概述机制、合作背景、运行流程、评估路线、结果和贡献。

### theory_to_design_steps

1. 先列出设计目标（IR、IC、无偏、成本）。

2. 用命题证明基础机制的性质。

3. 用排除法和顺序统计量推导关键设计参数。

4. 把每一设计参数与理论性质连接。

5. 用工程可行性和密码学工具消除可实施性质疑。

6. 组合成完整算法。

### method_and_study_sequence_steps

1. 先在最坏情形下做理论推导，建立优势。

2. 用仿真验证理论，避免解析伪影。

3. 放宽关键假设，扩展适用域。

4. 用真实数据证明外部有效性。

5. 在信息条件不利时与竞争范式比较，回应替代方案。

### results_reporting_steps

1. 先列出统一评价指标。

2. 给出理论闭式结果和命题。

3. 用表格比较理论值和仿真值。

4. 用统计检验（TOST）支持无偏性。

5. 在仿真域中重复等价比较。

6. 用真实数据表和p值验证。

7. 最后用数值例子把阈值转成管理结论。

### discussion_and_contribution_steps

1. 重述引言问题并回接到机制必要性。

2. 复述制品的组成和独特能力。

3. 用结果复述支持贡献。

4. 给出反直觉管理建议并解释机制原理。

5. 把贡献与文献缺口对比。

6. 把实践贡献与可实施性和合规连接。

7. 用未来研究划出边界。

## 可执行写作算法

### 1. 1

- step：1

- rhetorical_job_cn：用规模数据、监管变化和用户行为建立数据市场治理问题的紧迫性。

- research_evidence_required_cn：需要市场价值、用户规模、隐私工具使用率、回归或文献证据证明偏差机制存在。

- sentence_pattern_function_cn：先给需求句，再给方案句，然后用'我们首先描述缺点'过渡；每段以问题现象开头、以后果或制度要求收束。

- transition_condition_cn：当读者能认同'个人数据市场需要根本变革'，进入数据市场和机制缺陷描述。

### 2. 2

- step：2

- rhetorical_job_cn：用现实平台案例把固定补偿和集中优化两类机制定义为论文的竞争对象。

- research_evidence_required_cn：需要现实或文献中的平台采用这两类机制的实证或描述性证据。

- sentence_pattern_function_cn：先给平台清单和买方服务，再总结'它们依赖固定补偿或集中优化'，随后用因果机制解释各自缺陷。

- transition_condition_cn：当固定补偿'无偏则贵'和集中优化'需要信息且未必最优'两个缺陷被确立后，进入机制设计。

### 3. 3

- step：3

- rhetorical_job_cn：在文献综述中分别与定价端、集中优化端、差分隐私端、联合补偿-估计端划界，把'无偏样本'定位为独特贡献。

- research_evidence_required_cn：需要覆盖数据市场定价、集中优化、差分隐私、联合补偿-估计四条文献线。

- sentence_pattern_function_cn：每段先综述某一文献线，再用'我们相反/不同于'句指出本文差异。

- transition_condition_cn：当读者接受'现有方法都得不到无偏样本'后，进入正式模型。

### 4. 4

- step：4

- rhetorical_job_cn：建立平台、数据主体效用、k-anonymity、隐私成本函数和相关性假设，把偏差-成本权衡形式化。

- research_evidence_required_cn：需要可推导的效用函数、隐私成本函数和相关性文献支撑。

- sentence_pattern_function_cn：先描述平台和记录类型，再给出效用函数和性质约束，最后用'这个问题位于偏差-成本权衡核心'收束。

- transition_condition_cn：当问题模型具备可推导性，进入机制设计。

### 5. 5

- step：5

- rhetorical_job_cn：用IC/IR约束出发设计第二补偿拍卖，用顺序统计量推导两人排序配对，组装RSP并回应可实施性。

- research_evidence_required_cn：需要VCG拍卖理论、顺序统计量性质、同态加密等工程工具的文献或逻辑可用性。

- sentence_pattern_function_cn：先给设计旅程图，再给命题证明，把每个设计参数与理论性质对应，最后用类比消除工程质疑。

- transition_condition_cn：当RSP可被形式化并回答'为什么这样设计'后，进入最坏情形理论分析。

### 6. 6

- step：6

- rhetorical_job_cn：在最坏情形下推导各方法闭式性能，用命题确立RSP对固定补偿的支配和总成本边界，并用样本量分析制造第二洞见。

- research_evidence_required_cn：需要能推导期望偏差、期望总补偿、排除率、Gini和Vp的抽样模型。

- sentence_pattern_function_cn：先定义指标，再对每个方法给出闭式公式，用'Proposition'给出支配结论，随后用一段直觉解释数学阈值。

- transition_condition_cn：当理论优势被确立，且有限样本未验证，进入仿真。

### 7. 7

- step：7

- rhetorical_job_cn：用完美相关仿真验证理论，用TOST支持无偏，用不完美相关、beta分布和真实数据扩展外部有效性，再把集中优化拖入比较。

- research_evidence_required_cn：需要大规模仿真、TOST检验能力、行业伙伴真实数据，以及区间不确定模型下的COH/COL推导。

- sentence_pattern_function_cn：每小节以'我们扩展/测试/进一步分析'开头，给出表、图或命题，最后以现实N的数值例子把阈值转为强烈建议。

- transition_condition_cn：当各阶段证据都到位，进入结论。

### 8. 8

- step：8

- rhetorical_job_cn：在结论中重述问题、复述贡献、给出管理建议、勾画边界和未来方向。

- research_evidence_required_cn：需要全文命题、仿真表、真实数据表和部分信息阈值作为支撑，不能引入新主张。

- sentence_pattern_function_cn：先回述引言问题，再'据我们所知首次'声明贡献，随后用'令人惊讶的是'给出管理建议，最后用未建模因素开未来清单。

- transition_condition_cn：所有主张都能回溯到前面证据时即可结束。

## 应模仿的高价值动作

1. 把创新对象定义为'无偏样本而非无偏估计'，用产出物类型而非性能分数定义贡献。

2. 用最坏情形（完全相关）作为理论分析的默认条件，再逐步放宽，形成稳健性叙事。

3. 在每个数学命题后紧跟一句管理直觉，让形式结果可被非数学读者吸收。

4. 用现实人口规模的数值例证把阈值结论转成强烈实践建议。

5. 用实时竞价类比回应可实施性，把计算负担归因于成熟产业惯例。

6. 在机制设计阶段即回答平台排序是否会引入隐私成本，通过信任、同态加密、IR约束三层论证消除质疑。

7. 用TOST等价检验而不是简单t检验证明'偏差为零'，统计方法本身支撑无偏性主张。

8. 把评价维度从偏差和成本扩展为排除率、Gini和Vp，让机制的优势不止一步性能。

## 不要只复制的表面动作

1. 不要只写'无偏低成本'而不给出由算法规则决定的无偏性推导和补偿公式。

2. 不要把仿真结果当作真实用户行为证据；本文并未声称做过现场实验。

3. 不要把'平台应放弃信息'当作无条件结论；它依赖区间不确定模型和d̂阈值。

4. 不要把'类似实时竞价'等同于已做运行测试；实际延迟未被测量。

5. 不要机械套用VCG而不说明效用函数和支付规则如何保证激励相容。

6. 不要为了扩大适用场景而堆砌平台名称而不把它们与机制比较对应。

## 证据薄弱或跳跃的动作

1. 从'区间不确定性模型下RSP优于集中优化'外推为'平台应放弃任何部分信息估计'，真实估计误差未必是均匀区间，且未考虑获取信息成本。

2. 从真实调查数据推断机制会在真实交易中运行，因为该数据没有经历真实拍卖、支付或用户策略行为。

3. 把'算法可类比实时竞价'当作可实施性证据，没有实际运行时间或用户操作测试。

4. 真实数据仅覆盖低相关场景（0.0186），高相关真实场景仍依赖仿真。

5. 未进行行为实验验证真实数据主体是否如理论那样报告隐私顾虑；激励相容是数学性质而非经验性质。

## 一句话套路

先制造一个同时有商业现实和文献基础的偏差-成本两难，再设计一个由激励相容拍卖和排序采样共同组成的市场机制，用最坏情形理论证明其无偏近优，再通过模拟、真实数据和信息放宽把该优势从一个特例扩展成一般管理建议。

## 分析边界

全文完整可读，但部分图片（图1、3-7）的具体曲线数值依赖标题和上下文定位；Algorithm 1在Markdown中呈现为伪代码块，配对和移除逻辑以文字与表格为准；Table 5的调查问题编码以原文表格为准；OCR对个别希腊字母和上标有小误差，但不影响论证结构判断；本分析未引入附录或补充材料。
