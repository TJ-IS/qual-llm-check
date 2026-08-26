# Bidder Support in Multi-item Multi-unit Continuous Combinatorial Auctions: A Unifying Theoretical Framework：ISR 句段级微观图谱

- 作者：Gediminas Adomavicius; Alok Gupta; Mochen Yang
- 年份：2022
- DOI：10.1287/isre.2021.1068
- 源文件：28268_2022_bidder-support-in-multi-item-multi-unit-continuous-combinatorial-auctions-a-unifying-theoretical.md
- 置信度：0.74

## 核实后的宏观骨架

文章按‘机制价值—参与障碍—信息需求—部分已有方案—一般MIMU缺口—最一般理论—等价化约与统一—制品化实现—模拟与基准—边界扩展—结论’推进。摘要先把组合拍卖采纳受限归因于bidder support缺失，提出MIMU问题；正文§2综述winner determination算法和MISU/SIMU已有支持结果，指出统一缺口；§3在最一般的MIMU-XOR模型中定义子auction，证明更新递推、活标条件/winning-deadness公式、活标紧上界三组定理；§4通过‘OR可视作每个标由唯一bidder提交的XOR’把MIMU-OR全部结果导出，并用M=1或u_j=1退化映射覆盖SIMU/MISU；§5把理论公式翻译成VAL/LastWinBid数据结构与增量更新算法，先对MIMU-OR和MIMU-XOR做最坏/平均模拟，再与IP/CPLEX按需计算做同一总任务基准，显示数量级优势并给出查询频率边界；§6把理论扩展到batch与hierarchical约束MIMU；§7调整子auction定义与成本最小化后扩展到reverse MIMU；§8重述统一贡献、计算贡献、边界与未来方向。

## 摘要逐句图谱

### 1. Abstract S1

- order：1

- locator：Abstract S1

- paraphrase_cn：组合拍卖虽有公认优点，但在消费类市场采纳受限，部分原因是缺少可辅助竞拍者决策的有效支持信息。

- move_code：LIMITATION

- statement_status：author_inference

- why_here_cn：开门见山把机制采纳障碍归因于支持信息缺失，为全文设定问题域。

- inherits_from_previous_cn：无

- changes_argument_state_cn：把‘组合拍卖好但没被广泛用’转化为‘需要研究bidder support’。

- sets_up_next_cn：提出全文要解决的bidder support问题。

- failure_if_removed_cn：读者没有动机期待一个bidder support理论，摘要缺少问题锚点。

- evidence_pointer：Abstract

### 2. Abstract S2

- order：2

- locator：Abstract S2

- paraphrase_cn：本文研究一般MIMU组合拍卖中的bidder support问题，其中多个异质物品、每物品多同质单位。

- move_code：RQ_OR_OBJECTIVE

- statement_status：author_inference

- why_here_cn：把研究对象具体化到一般MIMU，区别于已有MISU/SIMU。

- inherits_from_previous_cn：承接前句支持信息缺失。

- changes_argument_state_cn：给出正式研究问题与机制空间。

- sets_up_next_cn：需进一步限定连续拍卖和投标语言。

- failure_if_removed_cn：摘要没有明确研究目标。

- evidence_pointer：Abstract

### 3. Abstract S3

- order：3

- locator：Abstract S3

- paraphrase_cn：具体考虑连续MIMU拍卖，因为其对投标活动限制最少，从而降低参与复杂度。

- move_code：SCOPE_NARROWING

- statement_status：author_inference

- why_here_cn：把研究限定在连续拍卖，与迭代拍卖/活动规则区分。

- inherits_from_previous_cn：延续MIMU对象。

- changes_argument_state_cn：缩小问题范围，减少需要处理的规则约束。

- sets_up_next_cn：为后文‘只需基于实际投标的客观支持’铺垫。

- failure_if_removed_cn：研究边界不清晰，读者会以为覆盖所有MIMU机制。

- evidence_pointer：Abstract

### 4. Abstract S4

- order：4

- locator：Abstract S4

- paraphrase_cn：分别讨论OR和XOR两种主流投标语言。

- move_code：THEORY_INTRO

- statement_status：prior_literature

- why_here_cn：投标语言是全文两个平行理论流的划分依据。

- inherits_from_previous_cn：在MIMU框架下引入语言维度。

- changes_argument_state_cn：建立OR/XOR二元结构。

- sets_up_next_cn：期待后文分别推导并统一。

- failure_if_removed_cn：摘要缺失核心分析维度。

- evidence_pointer：Abstract

### 5. Abstract S5

- order：5

- locator：Abstract S5

- paraphrase_cn：对XOR投标拍卖，推导计算重要支持指标的理论结果。

- move_code：THEORY_PROPOSITION

- statement_status：theory_claim

- why_here_cn：先给最一般情形的理论贡献。

- inherits_from_previous_cn：从XOR语言切入。

- changes_argument_state_cn：宣称XOR支持指标可算。

- sets_up_next_cn：需要解释OR如何获得。

- failure_if_removed_cn：理论贡献的核心没有出现。

- evidence_pointer：Abstract; Section 3

### 6. Abstract S6

- order：6

- locator：Abstract S6

- paraphrase_cn：证明OR拍卖的bidder support结果可由XOR结果直接导出，办法是把每个OR标看作唯一bidder提交的XOR标。

- move_code：THEORY_PROPOSITION

- statement_status：theory_claim

- why_here_cn：这是全文统一框架的关键化约。

- inherits_from_previous_cn：承接XOR理论结果。

- changes_argument_state_cn：把OR归约为XOR，而不使用常见的OR* dummy goods方向。

- sets_up_next_cn：为‘MIMU-XOR最一般’声明提供依据。

- failure_if_removed_cn：OR与XOR两套结果无法统一，理论贡献大打折扣。

- evidence_pointer：Abstract; Section 4

### 7. Abstract S7

- order：7

- locator：Abstract S7

- paraphrase_cn：因此确立MIMU-XOR为最一般情形，统一不同投标语言以及SIMU和MISU两类特例。

- move_code：CONTRIBUTION_CLAIM

- statement_status：contribution_claim

- why_here_cn：把化约结果升格为统一理论贡献。

- inherits_from_previous_cn：依赖OR as XOR化约。

- changes_argument_state_cn：声称统一了两个分离研究流。

- sets_up_next_cn：为计算制品和扩展提供理论地位。

- failure_if_removed_cn：论文只是MIMU特例研究而非统一框架。

- evidence_pointer：Abstract; Section 4.3

### 8. Abstract S8

- order：8

- locator：Abstract S8

- paraphrase_cn：理论结果导致能在实践中高效提供支持信息的算法程序，并优于常用整数规划方法。

- move_code：STUDY_OVERVIEW

- statement_status：contribution_claim

- why_here_cn：把理论转化为计算制品和基准优势，预告评价方式。

- inherits_from_previous_cn：承接理论公式。

- changes_argument_state_cn：加入制品和性能维度。

- sets_up_next_cn：后文模拟与benchmark是证据。

- failure_if_removed_cn：论文缺实践可行性与相对优势主张。

- evidence_pointer：Abstract; Section 5

### 9. Abstract S9

- order：9

- locator：Abstract S9

- paraphrase_cn：理论洞察还扩展到带额外投标约束的拍卖，包括batch、hierarchical和reverse拍卖。

- move_code：CONTRIBUTION_CLAIM

- statement_status：contribution_claim

- why_here_cn：在摘要末尾预告边界扩展，避免贡献被读成一次性特例。

- inherits_from_previous_cn：统一理论建立之后。

- changes_argument_state_cn：把贡献推广至更多市场机制。

- sets_up_next_cn：读者期待Section 6/7的扩展。

- failure_if_removed_cn：贡献的普适性没有预告。

- evidence_pointer：Abstract; Sections 6-7

## 引言逐句图谱

### 1. Introduction P1 S1

- order：1

- locator：Introduction P1 S1

- paraphrase_cn：组合拍卖作为分配多种资产的市场机制，引起研究和实践越来越多关注。

- move_code：CONTEXT

- statement_status：prior_literature

- why_here_cn：开场建立机制的重要性。

- inherits_from_previous_cn：无

- changes_argument_state_cn：开始讨论组合拍卖。

- sets_up_next_cn：为应用价值句做铺垫。

- failure_if_removed_cn：问题缺少宏观背景。

- evidence_pointer：Introduction P1

### 2. Introduction P1 S2

- order：2

- locator：Introduction P1 S2

- paraphrase_cn：组合拍卖中竞拍者可对单个物品和物品束投标。

- move_code：CONTEXT

- statement_status：prior_literature

- why_here_cn：给机制一个最小定义。

- inherits_from_previous_cn：承接机制名称。

- changes_argument_state_cn：定义投标空间。

- sets_up_next_cn：为组合复杂性句提供对象。

- failure_if_removed_cn：机制定义缺失。

- evidence_pointer：Introduction P1

### 3. Introduction P1 S3

- order：3

- locator：Introduction P1 S3

- paraphrase_cn：物品价值存在协同时可带来配置效率并创造显著经济收益（引文献）。

- move_code：PRACTICAL_STAKES

- statement_status：prior_literature

- why_here_cn：说明机制有价值的证据。

- inherits_from_previous_cn：承接组合拍卖定义。

- changes_argument_state_cn：把机制价值确立为研究动机。

- sets_up_next_cn：让后续‘采纳有限’更有反差。

- failure_if_removed_cn：采纳受限的痛点缺少利害关系。

- evidence_pointer：Introduction P1

### 4. Introduction P1 S4

- order：4

- locator：Introduction P1 S4

- paraphrase_cn：因此已有FCC频谱、运输、采购等现实应用。

- move_code：PRACTICAL_STAKES

- statement_status：prior_literature

- why_here_cn：给出应用证据，增强现实意义。

- inherits_from_previous_cn：承接机制价值。

- changes_argument_state_cn：把抽象价值落实为具体场景。

- sets_up_next_cn：为消费市场受限对比做铺垫。

- failure_if_removed_cn：实际重要性不够具体。

- evidence_pointer：Introduction P1

### 5. Introduction P2 S1

- order：5

- locator：Introduction P2 S1

- paraphrase_cn：尽管机制优点吸引人，在eBay等大规模消费市场应用很有限，部分因为参与高度复杂。

- move_code：LIMITATION

- statement_status：author_inference

- why_here_cn：从正面价值转向负面障碍，是引言第一个转折。

- inherits_from_previous_cn：由前段机制价值反差而来。

- changes_argument_state_cn：建立采纳缺口。

- sets_up_next_cn：引出参与复杂性因素。

- failure_if_removed_cn：研究动机没有痛点。

- evidence_pointer：Introduction P2

### 6. Introduction P2 S2-S3

- order：6

- locator：Introduction P2 S2-S3

- paraphrase_cn：第一，组合性质让竞拍者难以跟踪状态：束数量随异质物品指数增长、赢标计算NP难，竞拍者可能不知道自己的标是否赢。

- move_code：PHENOMENON

- statement_status：prior_literature

- why_here_cn：提供参与复杂性的具体机制。

- inherits_from_previous_cn：承接‘高度复杂’。

- changes_argument_state_cn：把复杂归因到状态跟踪与计算困难。

- sets_up_next_cn：为实时支持信息需求铺垫。

- failure_if_removed_cn：复杂参与的具体证据缺失。

- evidence_pointer：Introduction P2

### 7. Introduction P2 S4

- order：7

- locator：Introduction P2 S4

- paraphrase_cn：而且组合投标产生复杂动态：当前不赢的标可能随后与互补束组合而赢，竞拍者难以有效出价。

- move_code：PHENOMENON

- statement_status：prior_literature

- why_here_cn：解释支持信息为什么必须理解动态而非只看当前赢家。

- inherits_from_previous_cn：承接组合状态跟踪困难。

- changes_argument_state_cn：引入互补组合动态，直接对应后文子auction理论。

- sets_up_next_cn：为winning/deadness level定义做概念准备。

- failure_if_removed_cn：读者不理解为什么需要winning/deadness信息。

- evidence_pointer：Introduction P2

### 8. Introduction P2 S5

- order：8

- locator：Introduction P2 S5

- paraphrase_cn：第二，许多行业迭代拍卖有固定轮次与活动规则，设计限制多、复杂，进一步增加普通消费者参与难度。

- move_code：PHENOMENON

- statement_status：prior_literature

- why_here_cn：给出第二个复杂性来源，为连续拍卖转向铺垫。

- inherits_from_previous_cn：延续参与复杂性列举。

- changes_argument_state_cn：把问题从投标计算难扩展到机制规则复杂。

- sets_up_next_cn：引出连续组合拍卖作为替代。

- failure_if_removed_cn：迭代拍卖vs连续拍卖的对比失去基础。

- evidence_pointer：Introduction P2

### 9. Introduction P3 S1

- order：9

- locator：Introduction P3 S1

- paraphrase_cn：认识到迭代拍卖参与困难，研究者主张连续组合拍卖更适合消费市场。

- move_code：CONTEXT

- statement_status：prior_literature

- why_here_cn：把机制选择转向连续拍卖。

- inherits_from_previous_cn：承接迭代拍卖的规则复杂。

- changes_argument_state_cn：确立本文机制类型：连续MIMU。

- sets_up_next_cn：需要回答连续拍卖需要什么条件。

- failure_if_removed_cn：连续拍卖选择缺少动机。

- evidence_pointer：Introduction P3

### 10. Introduction P3 S2

- order：10

- locator：Introduction P3 S2

- paraphrase_cn：连续拍卖中竞拍者可在任意时间加入、投标、离开，几乎不受特定规则限制。

- move_code：CONTEXT

- statement_status：author_inference

- why_here_cn：定义连续拍卖。

- inherits_from_previous_cn：承接连续拍卖主张。

- changes_argument_state_cn：明确机制自由程度。

- sets_up_next_cn：使‘仅依赖实际投标’的客观支持成为可能。

- failure_if_removed_cn：机制边界不清晰。

- evidence_pointer：Introduction P3

### 11. Introduction P3 S3

- order：11

- locator：Introduction P3 S3

- paraphrase_cn：然而要减轻参与复杂，必须提供支持投标决策的有用信息，否则机制可能不被采纳、经济结果受损。

- move_code：REQUIREMENT

- statement_status：author_inference

- why_here_cn：从机制特征转向信息需求，是引言第二个转折。

- inherits_from_previous_cn：承接连续拍卖的可行性。

- changes_argument_state_cn：把信息支持定义为机制采纳的必要条件。

- sets_up_next_cn：进一步要求实时性。

- failure_if_removed_cn：bidder support问题的必要性不成立。

- evidence_pointer：Introduction P3

### 12. Introduction P3 S4

- order：12

- locator：Introduction P3 S4

- paraphrase_cn：而且支持信息必须实时提供（每笔标之后），否则过时反馈会误导决策、损害经济结果。

- move_code：REQUIREMENT

- statement_status：author_inference

- why_here_cn：把‘有用信息’升级为‘实时信息’。

- inherits_from_previous_cn：承接信息需求句。

- changes_argument_state_cn：建立实时计算要求，为后文算法效率目标做铺垫。

- sets_up_next_cn：产出计算制品的评价标准。

- failure_if_removed_cn：实时性这一核心设计目标缺失。

- evidence_pointer：Introduction P3

### 13. Introduction P4 S1

- order：13

- locator：Introduction P4 S1

- paraphrase_cn：Adomavicius和Gupta提出只依赖实际投标的重要支持方案，提供赢家、winning level、deadness level三项信息。

- move_code：PRIOR_KNOWLEDGE

- statement_status：prior_literature

- why_here_cn：引入本文采用的三类支持指标。

- inherits_from_previous_cn：承接实时支持需求。

- changes_argument_state_cn：给出衡量支持信息的具体操作化指标。

- sets_up_next_cn：说明这些指标只覆盖两类特例。

- failure_if_removed_cn：bidder support内涵不清楚。

- evidence_pointer：Introduction P4

### 14. Introduction P4 S2-S3

- order：14

- locator：Introduction P4 S2-S3

- paraphrase_cn：前期研究主要覆盖MISU和SIMU两类基本典型拍卖，而更一般的MIMU允许任意物品集和任意单位数。

- move_code：GAP

- statement_status：prior_literature

- why_here_cn：列出已有覆盖范围，引出MIMU这一空白。

- inherits_from_previous_cn：承接已有方案。

- changes_argument_state_cn：把问题从MISU/SIMU推进到MIMU。

- sets_up_next_cn：指出统一MIMU为何困难。

- failure_if_removed_cn：一般化目标没有文献依据。

- evidence_pointer：Introduction P4

### 15. Introduction P4 S4

- order：15

- locator：Introduction P4 S4

- paraphrase_cn：尽管已有MISU/SIMU工作，统一二者并为一般MIMU提供有效支持仍是重大挑战，因为两种拍卖复杂度来源根本不同。

- move_code：WHY_GAP_MATTERS

- statement_status：author_inference

- why_here_cn：说明缺口非简单叠加，值得专门研究。

- inherits_from_previous_cn：由MIMU空白句展开。

- changes_argument_state_cn：把空白升级为有难度、有理论空间的挑战。

- sets_up_next_cn：为后文‘统一理论’设立预期。

- failure_if_removed_cn：研究价值不成立。

- evidence_pointer：Introduction P4

### 16. Introduction P5 S1

- order：16

- locator：Introduction P5 S1

- paraphrase_cn：本文研究一般连续MIMU拍卖的实时bidder support问题。

- move_code：RQ_OR_OBJECTIVE

- statement_status：author_inference

- why_here_cn：正式宣布研究问题，与摘要呼应。

- inherits_from_previous_cn：由前段缺口导出。

- changes_argument_state_cn：从描述现状转向本文目标。

- sets_up_next_cn：需要定义投标语言。

- failure_if_removed_cn：论文没有明确研究问题。

- evidence_pointer：Introduction P5

### 17. Introduction P5 S2-S4

- order：17

- locator：Introduction P5 S2-S4

- paraphrase_cn：考虑OR和XOR两种投标语言，并分别定义其含义；XOR完全表达任意偏好。

- move_code：THEORY_INTRO

- statement_status：prior_literature

- why_here_cn：引入全文的分析维度。

- inherits_from_previous_cn：承接研究问题。

- changes_argument_state_cn：把MIMU细分到OR/XOR两分支。

- sets_up_next_cn：为第三节和第四节的平行推导做铺垫。

- failure_if_removed_cn：后文OR/XOR结构失去基础。

- evidence_pointer：Introduction P5

### 18. Introduction P6 S1-S3

- order：18

- locator：Introduction P6 S1-S3

- paraphrase_cn：全文采用三个边界假设：不允许部分分配、拍卖者价值最大化而非卖完所有物品、不对行为做具体假设，只基于实际投标给客观信息。

- move_code：METHOD_JUSTIFICATION

- statement_status：author_inference

- why_here_cn：在进入理论前限定模型边界，防止被误读为博弈均衡研究。

- inherits_from_previous_cn：承接研究问题。

- changes_argument_state_cn：确立all-or-nothing、自由处置、无行为假设的框架。

- sets_up_next_cn：使理论结果适用于一般连续拍卖。

- failure_if_removed_cn：理论适用边界不清。

- evidence_pointer：Introduction P6

### 19. Introduction P7 S1

- order：19

- locator：Introduction P7 S1

- paraphrase_cn：用图1总结：bidder support分解为跟踪子auction状态和基于最新状态计算支持信息。

- move_code：STUDY_OVERVIEW

- statement_status：author_inference

- why_here_cn：给出全文主线框架。

- inherits_from_previous_cn：承接问题与边界。

- changes_argument_state_cn：把任务分解为两个子任务，预告后文章节。

- sets_up_next_cn：为理论→制品→基准的路线图服务。

- failure_if_removed_cn：全文结构缺少导航。

- evidence_pointer：Introduction P7; Figure 1

### 20. Introduction P7 S2-S4

- order：20

- locator：Introduction P7 S2-S4

- paraphrase_cn：先推导XOR结果，再证明OR可由XOR导出，MISU/SIMU可由MIMU导出；理论产生动态数据结构与算法，基准显示优于IP；还扩展到batch、hierarchical、reverse。

- move_code：STUDY_OVERVIEW

- statement_status：author_inference

- why_here_cn：压缩全文论证链，建立读者阅读预期。

- inherits_from_previous_cn：承接子auction分解。

- changes_argument_state_cn：预告理论统一、计算实现、基准与扩展四大模块。

- sets_up_next_cn：让后文各部分都可被追踪。

- failure_if_removed_cn：读者难以预判论文结构。

- evidence_pointer：Introduction P7

### 21. Introduction P8 S1

- order：21

- locator：Introduction P8 S1

- paraphrase_cn：主要贡献是解决连续MIMU的bidder support问题，推导理论基础并设计高效计算基础设施。

- move_code：CONTRIBUTION

- statement_status：contribution_claim

- why_here_cn：在引言末尾预先声明核心贡献。

- inherits_from_previous_cn：由路线图收束。

- changes_argument_state_cn：把前文缺口与本文解法连起来。

- sets_up_next_cn：为统一SIMU/MISU的贡献句铺垫。

- failure_if_removed_cn：读者不知道如何评价论文。

- evidence_pointer：Introduction P8

### 22. Introduction P8 S2

- order：22

- locator：Introduction P8 S2

- paraphrase_cn：基于该解法可统一SIMU与MISU的理论洞察，并揭示MIMU bidder support的根本理解。

- move_code：CONTRIBUTION

- statement_status：contribution_claim

- why_here_cn：把贡献从单点解法提升为统一理论。

- inherits_from_previous_cn：承接核心贡献。

- changes_argument_state_cn：建立理论统一性贡献。

- sets_up_next_cn：为实践贡献句做铺垫。

- failure_if_removed_cn：统一理论贡献被削弱。

- evidence_pointer：Introduction P8

### 23. Introduction P8 S3

- order：23

- locator：Introduction P8 S3

- paraphrase_cn：实践上可支持MIMU竞拍者更明智决策，并有助于自动投标系统设计。

- move_code：CONTRIBUTION

- statement_status：contribution_claim

- why_here_cn：给出实践意义，特别提示自动投标系统。

- inherits_from_previous_cn：承接核心贡献。

- changes_argument_state_cn：把计算制品连接到市场决策和未来系统。

- sets_up_next_cn：为结论中的future work埋线。

- failure_if_removed_cn：论文缺少实践落脚点。

- evidence_pointer：Introduction P8

## 引言逐段图谱

### 1. 1

- paragraph_locator：Introduction P1

- opening_move_cn：以组合拍卖作为市场机制引入，给出定义。

- development_move_cn：叠加协同价值、经济效益和应用场景三类证据。

- pivot_move_cn：从机制优点收束到研究这个机制的重要性。

- closing_move_cn：为下一段的‘但消费市场受限’制造反差。

- paragraph_job_cn：建立组合拍卖的机制价值与现实重要性。

### 2. 2

- paragraph_locator：Introduction P2

- opening_move_cn：指出消费市场采纳有限并归因于参与复杂。

- development_move_cn：分两个因素展开：状态跟踪/计算难点和动态投标复杂性、迭代规则复杂性。

- pivot_move_cn：第二个因素把问题导向机制设计（迭代vs连续）。

- closing_move_cn：为连续拍卖主张提供动机。

- paragraph_job_cn：具体化参与复杂性，论证为何需要支持信息。

### 3. 3

- paragraph_locator：Introduction P3

- opening_move_cn：主张连续组合拍卖更适合消费市场。

- development_move_cn：定义连续拍卖的开放性。

- pivot_move_cn：转折到‘需要有用信息’并要求实时。

- closing_move_cn：给出‘过时反馈误导决策’的反面后果，强化实时要求。

- paragraph_job_cn：把连续拍卖+实时支持信息确立为问题背景。

### 4. 4

- paragraph_locator：Introduction P4

- opening_move_cn：介绍已有bidder support方案及三项指标。

- development_move_cn：综述MISU/SIMU两类已有覆盖。

- pivot_move_cn：从已有覆盖转到一般MIMU的未解决。

- closing_move_cn：说明统一MIMU因复杂度来源不同而重大，为下一节埋线。

- paragraph_job_cn：定位研究缺口：一般MIMU bidder support缺失。

### 5. 5

- paragraph_locator：Introduction P5

- opening_move_cn：正式宣布研究问题：一般连续MIMU的实时bidder support。

- development_move_cn：定义OR与XOR两种投标语言。

- pivot_move_cn：通过XOR完全表达性把两种语言都纳入研究。

- closing_move_cn：给出MIMU-OR/MIMU-XOR记法，为理论章节铺路。

- paragraph_job_cn：确立研究问题及核心分析维度。

### 6. 6

- paragraph_locator：Introduction P6

- opening_move_cn：表达全文三个重要考虑。

- development_move_cn：逐条说明all-or-nothing、价值最大化、无行为假设的理由。

- pivot_move_cn：把第三个考虑从‘不做行为假设’转到‘提供客观信息’。

- closing_move_cn：说明目标是可基于实际投标计算的客观信息。

- paragraph_job_cn：限定模型边界，防止方法误读。

### 7. 7

- paragraph_locator：Introduction P7

- opening_move_cn：用图1给出任务分解：跟踪子auction状态+计算支持信息。

- development_move_cn：沿两阶段展开理论、计算、基准、扩展四项内容。

- pivot_move_cn：从理论转向制品性能，再转向扩展。

- closing_move_cn：以reverse auction结尾，预告最远边界。

- paragraph_job_cn：给出全文路线图。

### 8. 8

- paragraph_locator：Introduction P8

- opening_move_cn：声明主要贡献是解决MIMU bidder support并设计计算基础设施。

- development_move_cn：升级为统一SIMU/MISU的理论贡献。

- pivot_move_cn：转到实践意义。

- closing_move_cn：用自动投标系统收束。

- paragraph_job_cn：预先宣告贡献，设定评价标准。

## 理论到设计逐句图谱

### 1. Section 3.1 tie-breaking paragraph

- order：1

- locator：Section 3.1 tie-breaking paragraph

- paraphrase_cn：为保证多个等值分配时能系统识别赢家，采用时间公平的总序tie-breaking；晚标不能仅靠等值替代早标。

- move_code：METHOD_JUSTIFICATION

- statement_status：method_decision

- why_here_cn：在定义winner determination之后必须给出唯一赢家规则。

- inherits_from_previous_cn：承接可行分配与价值最大化。

- changes_argument_state_cn：使所有max/min和‘更新’操作well-defined。

- sets_up_next_cn：为Algorithm 1中‘严格大于才更新’提供理论依据。

- failure_if_removed_cn：tie-breaking不明确，整个递推无法唯一化。

- evidence_pointer：Section 3.1

### 2. Section 3.2 subauction definition

- order：2

- locator：Section 3.2 subauction definition

- paraphrase_cn：在MIMU-XOR中，子auction由物品向量x和bidder coalition n共同定义，包含不超出x且来自n的投标。

- move_code：THEORY_INTRO

- statement_status：theory_claim

- why_here_cn：把已有MISU/SIMU中的子auction概念推广到MIMU。

- inherits_from_previous_cn：承接引言对子auction作为building block的强调。

- changes_argument_state_cn：确立全文分析的基本单元。

- sets_up_next_cn：为Theorem 1的互补子auction更新服务。

- failure_if_removed_cn：没有可追踪的动态状态，后文全部结果失去载体。

- evidence_pointer：Section 3.2

### 3. Section 3.2 Theorem 1

- order：3

- locator：Section 3.2 Theorem 1

- paraphrase_cn：新标不进入某子auction则该子auction赢家不变；进入时新赢家为新标∪互补子auction赢家与旧赢家的择优。

- move_code：THEORY_PROPOSITION

- statement_status：theory_claim

- why_here_cn：这是全文核心递推定理，把拍卖动态压缩为局部更新规则。

- inherits_from_previous_cn：依赖子auction定义和tie-breaking总序。

- changes_argument_state_cn：从静态定义转向动态递推。

- sets_up_next_cn：为winning level公式、Algorithm 1和所有后续实现提供数学基础。

- failure_if_removed_cn：没有递推式，增量更新数据结构无法设计。

- evidence_pointer：Section 3.2

### 4. Section 3.3 winning level formula

- order：4

- locator：Section 3.3 winning level formula

- paraphrase_cn：新标要赢必须与互补子auction赢家组合击败当前赢家，故WL=总auction价值-互补子auction价值。

- move_code：THEORY_PROPOSITION

- statement_status：theory_claim

- why_here_cn：把Theorem 1变成可直接计算的winning level公式。

- inherits_from_previous_cn：直接由Theorem 1推导。

- changes_argument_state_cn：给出第一类支持指标的封闭式。

- sets_up_next_cn：为常数时间WL查询提供依据。

- failure_if_removed_cn：winning level无法计算，核心贡献缺失。

- evidence_pointer：Section 3.3

### 5. Section 3.3 Definition 1

- order：5

- locator：Section 3.3 Definition 1

- paraphrase_cn：定义VCS：在span x上焦点bidder移除若干非焦点bidder后得到的可行联盟集合。

- move_code：THEORY_INTRO

- statement_status：theory_claim

- why_here_cn：为刻画活标和deadness level引入必要概念。

- inherits_from_previous_cn：承接活标直觉：未来其他bidder可能阻塞现有竞标者。

- changes_argument_state_cn：把‘未来可能阻塞’形式化。

- sets_up_next_cn：为Theorem 2和deadness公式服务。

- failure_if_removed_cn：XOR下的活标条件无法表达。

- evidence_pointer：Section 3.3

### 6. Section 3.3 Theorem 2 and Corollary 2

- order：6

- locator：Section 3.3 Theorem 2 and Corollary 2

- paraphrase_cn：一个标活当且仅当它在恰等于其span的某VCS子auction中是赢家；deadness level为VCS上所有子auction价值的最小值。

- move_code：THEORY_PROPOSITION

- statement_status：theory_claim

- why_here_cn：给出活标与deadness的充分必要条件，是XOR支持指标的核心。

- inherits_from_previous_cn：依赖VCS定义和Theorem 1。

- changes_argument_state_cn：完成第二类支持指标的理论刻画。

- sets_up_next_cn：为MIMU-XOR实现中的二维查询和遍历VCS提供依据。

- failure_if_removed_cn：XOR deadness level不可计算，论文统一目标失败一半。

- evidence_pointer：Section 3.3

### 7. Section 3.4 Theorem 3

- order：7

- locator：Section 3.4 Theorem 3

- paraphrase_cn：每个span的活标数不超过min(|U-x|+1,|N|)，跨span总活标数有紧上界；构造例证上界可达。

- move_code：THEORY_PROPOSITION

- statement_status：theory_claim

- why_here_cn：量化拍卖动态复杂度，说明为什么需要追踪所有子auction。

- inherits_from_previous_cn：依赖Section 3.3活标条件。

- changes_argument_state_cn：把动态支持问题放在复杂度语境中。

- sets_up_next_cn：为后续实现复杂度判断和约束拍卖中更小状态空间做基础。

- failure_if_removed_cn：缺少对状态空间规模的理论性解释。

- evidence_pointer：Section 3.4

### 8. Section 4.1 P1

- order：8

- locator：Section 4.1 P1

- paraphrase_cn：OR投标可看成每个标由不同bidder提交的XOR投标，因此OR的理论结果可从XOR导出。

- move_code：THEORY_PROPOSITION

- statement_status：theory_claim

- why_here_cn：这是统一两种投标语言的关键等价化约。

- inherits_from_previous_cn：由第三节XOR结果提出。

- changes_argument_state_cn：把MIMU-OR从独立推导变为XOR的退化情形。

- sets_up_next_cn：为Table 2中OR公式和MIMU-OR一维实现服务。

- failure_if_removed_cn：OR与XOR两套结果无法统一。

- evidence_pointer：Section 4.1

### 9. Section 4.1 subauction simplification

- order：9

- locator：Section 4.1 subauction simplification

- paraphrase_cn：OR中不包含全部当前bidder的子auction与动态无关，只需追踪[x,N_k]。

- move_code：THEORY_PROPOSITION

- statement_status：theory_claim

- why_here_cn：把XOR的二维子auction简化为OR的一维形式。

- inherits_from_previous_cn：由OR as XOR化约推出。

- changes_argument_state_cn：解释OR实现为何比XOR简单。

- sets_up_next_cn：为MIMU-OR的VAL一维数组和简单DL公式服务。

- failure_if_removed_cn：OR实现的数据结构选择没有理论根据。

- evidence_pointer：Section 4.1

### 10. Section 4.2 VCS simplification

- order：10

- locator：Section 4.2 VCS simplification

- paraphrase_cn：因为未来标不会阻塞现有竞标者，OR拍卖的VCS退化为当前全体bidder N_k。

- move_code：THEORY_PROPOSITION

- statement_status：theory_claim

- why_here_cn：解释为什么OR的deadness只需在更大span上取最小。

- inherits_from_previous_cn：由OR as XOR推导。

- changes_argument_state_cn：完成OR支持指标公式的封闭。

- sets_up_next_cn：为Table 2和MIMU-OR实现服务。

- failure_if_removed_cn：OR deadness公式无法从统一框架推出。

- evidence_pointer：Section 4.2

### 11. Section 4.3 SIMU/MISU mapping paragraph

- order：11

- locator：Section 4.3 SIMU/MISU mapping paragraph

- paraphrase_cn：SIMU和MISU分别是MIMU在M=1或所有u_j=1时的退化情形，因此MIMU结果可映射到两类经典拍卖。

- move_code：THEORY_PROPOSITION

- statement_status：theory_claim

- why_here_cn：完成对两个分离研究流的统一。

- inherits_from_previous_cn：依赖MIMU-OR与MIMU-XOR全部结果。

- changes_argument_state_cn：MIMU成为覆盖SIMU/MISU的一般框架。

- sets_up_next_cn：为Figure 2映射和后续结论统一声明服务。

- failure_if_removed_cn：论文声称的统一框架落空。

- evidence_pointer：Section 4.3; Figure 2

### 12. Section 4.3 OR* discussion

- order：12

- locator：Section 4.3 OR* discussion

- paraphrase_cn：虽然XOR也可用OR*加dummy item实现，但deadness从OR*不便于推导；因此选择OR作为XOR特例。

- move_code：METHOD_JUSTIFICATION

- statement_status：method_decision

- why_here_cn：排除另一种统一路线，辩护为何XOR更一般。

- inherits_from_previous_cn：由OR/XOR关系分析而来。

- changes_argument_state_cn：明确统一方向的选择及其理由。

- sets_up_next_cn：为以MIMU-XOR为最一般形式的贡献声明服务。

- failure_if_removed_cn：读者会质疑为什么不采用文献已有的OR*编码。

- evidence_pointer：Section 4.3; online Appendix J

### 13. Section 5 P1

- order：13

- locator：Section 5 P1

- paraphrase_cn：实现直接由Section 3和4的理论结果驱动，有三个设计目标：增量更新、赢家确定、按需计算WL/DL。

- move_code：DESIGN_DECISION

- statement_status：design_decision

- why_here_cn：把理论结果显式转化为工程目标，是理论到设计的枢纽。

- inherits_from_previous_cn：承接所有支持指标公式。

- changes_argument_state_cn：理论部分结束，进入制品构建。

- sets_up_next_cn：为VAL/LastWinBid数据结构和Algorithm 1/2定义标准。

- failure_if_removed_cn：数据结构的每个选择会显得随意。

- evidence_pointer：Section 5 P1

## 制品设计理由逐句图谱

### 1. Section 5 P2 span mapping

- order：1

- locator：Section 5 P2 span mapping

- paraphrase_cn：把任意span向量映射为唯一整数索引，使用混合进制bitmap推广，并证明两个性质：唯一性、加减对应互补span。

- move_code：DESIGN_FEATURE

- statement_status：design_decision

- why_here_cn：数组索引需要把多维span压成一维整数，同时保留互补span的算术关系。

- inherits_from_previous_cn：直接服务于增量更新和WL查询。

- changes_argument_state_cn：从理论公式转向可计算的数据表示。

- sets_up_next_cn：为VAL和LastWinBid数组提供索引机制。

- failure_if_removed_cn：数组无法有效定位子auction。

- evidence_pointer：Section 5 P2; Properties 1-2

### 2. Section 5.1 VAL/LastWinBid paragraph

- order：2

- locator：Section 5.1 VAL/LastWinBid paragraph

- paraphrase_cn：VAL数组保存每个子auction当前价值，LastWinBid数组保存最新赢标的span、value、bidder、time信息。

- move_code：DESIGN_FEATURE

- statement_status：design_decision

- why_here_cn：支撑三个设计目标：价值用于WL/DL计算，赢标用于Algorithm 2回溯。

- inherits_from_previous_cn：由Theorem 1和winning公式决定需要保存的信息。

- changes_argument_state_cn：确定核心数据结构的两块存储。

- sets_up_next_cn：为Algorithm 1的更新提供目标数组。

- failure_if_removed_cn：没有存储子auction状态的载体，所有查询无法实现。

- evidence_pointer：Section 5.1

### 3. Section 5.1 after Algorithm 1

- order：3

- locator：Section 5.1 after Algorithm 1

- paraphrase_cn：Algorithm 1遍历互补子auction，仅当新标组合严格高于旧子auction价值时才更新；这自动实现时间公平tie-breaking。

- move_code：DESIGN_FEATURE

- statement_status：design_decision

- why_here_cn：把Theorem 1递推式变成可执行代码，并用‘严格大于’保证公平规则。

- inherits_from_previous_cn：由Theorem 1和tie-breaking总序共同决定。

- changes_argument_state_cn：理论递推转化为增量更新算法。

- sets_up_next_cn：为常数时间WL查询和较慢DL查询提供前提。

- failure_if_removed_cn：增量更新无法实现。

- evidence_pointer：Section 5.1 Algorithm 1

### 4. Section 5.1 after Algorithm 2

- order：4

- locator：Section 5.1 after Algorithm 2

- paraphrase_cn：Algorithm 2通过LastWinBid从最大span回溯得到当前赢家分配；所有子auction赢家的并集即活标集合。

- move_code：DESIGN_FEATURE

- statement_status：design_decision

- why_here_cn：解决赢家确定和活标枚举两个支持功能。

- inherits_from_previous_cn：依赖LastWinBid数组和活标定义。

- changes_argument_state_cn：补全三类支持信息（赢家、WL、DL）的查询能力。

- sets_up_next_cn：使模拟实验可以报告完整支持性能。

- failure_if_removed_cn：赢家信息无法提供。

- evidence_pointer：Section 5.1 Algorithm 2

### 5. Section 5.2 VAL/LastWinBid 2D

- order：5

- locator：Section 5.2 VAL/LastWinBid 2D

- paraphrase_cn：MIMU-XOR实现把VAL和LastWinBid扩展为二维数组，bidder set用bitmap表示，以处理VCS和bidder coalition。

- move_code：DESIGN_FEATURE

- statement_status：design_decision

- why_here_cn：XOR需要按(span, bidder set)两个维度保存子auction信息，VCS查询需要bidder集合索引。

- inherits_from_previous_cn：由XOR的VCS和Theorem 2决定。

- changes_argument_state_cn：把一维OR实现推广到最一般XOR情形。

- sets_up_next_cn：为MIMU-XOR模拟和Table 4提供制品基础。

- failure_if_removed_cn：XOR个性化winning/deadness无法计算。

- evidence_pointer：Section 5.2

### 6. Section 5.1 simulation setup

- order：6

- locator：Section 5.1 simulation setup

- paraphrase_cn：模拟构造最坏情形（全部singleton活标）和平均情形（随机span活标），并扫描物品数和单位数；singleton活标影响最多子auction。

- move_code：METHOD_DECISION

- statement_status：method_decision

- why_here_cn：性能评价需要覆盖计算复杂度边界和典型情况。

- inherits_from_previous_cn：由Algorithm 1复杂度分析导出。

- changes_argument_state_cn：建立可复现的性能证据基础。

- sets_up_next_cn：为Table 3/4的worst vs average对比服务。

- failure_if_removed_cn：性能结论缺乏最坏情况保障。

- evidence_pointer：Section 5.1 simulation setup

### 7. Section 5.3 P1-P2

- order：7

- locator：Section 5.3 P1-P2

- paraphrase_cn：本文策略增量保存全部子auction；替代策略是用IP按需计算所需子auction价值，避免指数存储；用同一任务计算所有WL/DL来比较。

- move_code：BENCHMARK_OR_CONTRAST

- statement_status：method_decision

- why_here_cn：建立公平且具有领域代表性的基准框架。

- inherits_from_previous_cn：由实时支持目标与IP在winner determination中的常用性决定。

- changes_argument_state_cn：把评价从自身速度升级为相对优势。

- sets_up_next_cn：为Table 5/6和临界查询频率服务。

- failure_if_removed_cn：不能证明本文实现优于常规做法。

- evidence_pointer：Section 5.3

### 8. Section 5.3 boundary paragraph

- order：8

- locator：Section 5.3 boundary paragraph

- paraphrase_cn：IP可能在拍卖规模很大且查询频率很低时更快；本文方法适合高频综合支持场景，并随拍卖推进其性能几乎不受历史标影响。

- move_code：BOUNDARY_CONDITION

- statement_status：empirical_result

- why_here_cn：给性能主张加上边界，增强可信度和公平性。

- inherits_from_previous_cn：由Table 5/6结果和单次IP求解时间推算。

- changes_argument_state_cn：把‘优于IP’限定为合理查询频率下的优势。

- sets_up_next_cn：为未来缓存/专用IP方向提供动机。

- failure_if_removed_cn：性能主张显得绝对且易被攻击。

- evidence_pointer：Section 5.3

## Study开头、过渡与收束图谱

### 1. Section 3 opening

- locator：Section 3 opening

- paraphrase_cn：本节讨论MIMU-XOR，给出拍卖动态和winning/deadness level计算的理论结果。

- move_code：STUDY_OPENING

- function_cn：开启最一般情形的理论推导，并预告后续Table 1记法。

- evidence_pointer：Section 3

### 2. Section 4 opening

- locator：Section 4 opening

- paraphrase_cn：本节讨论MIMU-OR，重点证明OR结果可由XOR结果导出。

- move_code：STUDY_OPENING

- function_cn：把第三节XOR理论作为前提，转向OR并预告化约方向。

- evidence_pointer：Section 4

### 3. Section 4.3 unifying paragraph

- locator：Section 4.3 unifying paragraph

- paraphrase_cn：基于MIMU-OR和MIMU-XOR结果，建立连接MIMU与SIMU/MISU的统一框架。

- move_code：THEORY_CLOSURE

- function_cn：完成统一理论声明，为设计部分提供总目标。

- evidence_pointer：Section 4.3

### 4. Section 5 opening

- locator：Section 5 opening

- paraphrase_cn：实现直接由前述理论结果驱动；提出三个设计目标并预告数据结构和模拟实验。

- move_code：TRANSITION_TO_ARTIFACT

- function_cn：从理论转向制品，把抽象公式翻译为工程目标。

- evidence_pointer：Section 5

### 5. Section 5.1 opening

- locator：Section 5.1 opening

- paraphrase_cn：用VAL和LastWinBid两个数组存储子auction价值和赢标，并给出MIMU-OR实现。

- move_code：ARTIFACT_OPENING

- function_cn：开始具体的MIMU-OR制品设计。

- evidence_pointer：Section 5.1

### 6. Section 5.2 opening

- locator：Section 5.2 opening

- paraphrase_cn：类似地用二维数组和bitmap表示MIMU-XOR的子auction信息。

- move_code：ARTIFACT_OPENING

- function_cn：把制品扩展至最一般XOR情形。

- evidence_pointer：Section 5.2

### 7. Section 5.3 opening

- locator：Section 5.3 opening

- paraphrase_cn：本文策略需要指数存储；对比策略是IP按需计算子auction价值；本节做基准分析。

- move_code：BENCHMARK_OPENING

- function_cn：把评价从自身性能转向与常用方法对比。

- evidence_pointer：Section 5.3

### 8. Section 6 opening

- locator：Section 6 opening

- paraphrase_cn：一般MIMU状态空间巨大；现实中竞拍者可能只关心部分bundle；讨论batch和hierarchical两类特例。

- move_code：EXTENSION_OPENING

- function_cn：在一般理论后转向约束变体，证明可迁移性。

- evidence_pointer：Section 6

### 9. Section 6.1 opening

- locator：Section 6.1 opening

- paraphrase_cn：以建材容器装运为例定义batch-based MIMU_B，参数为U和批次容量Ω。

- move_code：SPECIAL_CASE_OPENING

- function_cn：给出第一个约束扩展的形式化设置。

- evidence_pointer：Section 6.1

### 10. Section 6.2 opening

- locator：Section 6.2 opening

- paraphrase_cn：以FCC 700MHz频谱拍卖为例定义hierarchical MIMU_H，permitted packages形成树。

- move_code：SPECIAL_CASE_OPENING

- function_cn：给出第二个约束扩展，并预告互补span非permitted的挑战。

- evidence_pointer：Section 6.2

### 11. Section 7 opening

- locator：Section 7 opening

- paraphrase_cn：此前是forward auction；本节转向reverse auction，多个seller竞标向买家供货。

- move_code：EXTENSION_OPENING

- function_cn：把理论扩展到成本最小化的采购场景。

- evidence_pointer：Section 7

### 12. Section 8 opening

- locator：Section 8 opening

- paraphrase_cn：本文解决一般连续MIMU拍卖的实时bidder support问题，分别考虑OR和XOR语言。

- move_code：CONCLUSION_OPENING

- function_cn：重述问题并开始逐段发布贡献、边界和未来方向。

- evidence_pointer：Section 8

## 讨论与贡献逐句图谱

### 1. Section 8 P1 S1

- order：1

- locator：Section 8 P1 S1

- paraphrase_cn：本文解决一般连续MIMU拍卖的实时bidder support问题，其中多异质物品且每物品有多个不可区分单位。

- move_code：CONTRIBUTION_RESTATEMENT

- statement_status：contribution_claim

- why_here_cn：开篇重述问题，与引言P5/摘要S2呼应。

- inherits_from_previous_cn：全文论证的结果。

- changes_argument_state_cn：进入结论评估阶段。

- sets_up_next_cn：为理论贡献总结铺垫。

- failure_if_removed_cn：结论缺少主问题锚点。

- evidence_pointer：Section 8 P1

### 2. Section 8 P1 S2

- order：2

- locator：Section 8 P1 S2

- paraphrase_cn：利用子auction概念，推导新标到达时子auction如何更新，以及如何基于子auction价值计算winning和deadness levels。

- move_code：THEORY_RESTATEMENT

- statement_status：theory_claim

- why_here_cn：重述核心理论机制。

- inherits_from_previous_cn：由全文Section 3摘要而来。

- changes_argument_state_cn：把结果归纳为可重复引用的理论贡献。

- sets_up_next_cn：引出OR as XOR化约。

- failure_if_removed_cn：理论贡献的具体内容缺失。

- evidence_pointer：Section 8 P1

### 3. Section 8 P1 S3

- order：3

- locator：Section 8 P1 S3

- paraphrase_cn：重要发现是OR投标可看作每个标由唯一bidder提交的XOR投标，因此OR理论结果可由XOR导出。

- move_code：THEORY_RESTATEMENT

- statement_status：theory_claim

- why_here_cn：重述全文最关键的统一化约。

- inherits_from_previous_cn：由Section 4.1提炼。

- changes_argument_state_cn：把OR/XOR统一作为已建立事实。

- sets_up_next_cn：指出OR与XOR仍有独特差异。

- failure_if_removed_cn：统一框架贡献没有被复述。

- evidence_pointer：Section 8 P1

### 4. Section 8 P1 S4

- order：4

- locator：Section 8 P1 S4

- paraphrase_cn：尽管有该关系，OR和XOR仍有一些独特方面，例如OR最大活标数等于子auction数，而XOR中更小。

- move_code：THEORY_NUANCE

- statement_status：theory_claim

- why_here_cn：防止统一化约掩盖两类拍卖的实质差异。

- inherits_from_previous_cn：由统一关系后的比较而来。

- changes_argument_state_cn：为理论贡献补充边界性和精细度。

- sets_up_next_cn：转向SIMU/MISU连接。

- failure_if_removed_cn：统一宣称显得过度简化。

- evidence_pointer：Section 8 P1

### 5. Section 8 P2 S1

- order：5

- locator：Section 8 P2 S1

- paraphrase_cn：理论洞察允许把MIMU与两类典型特例SIMU和MISU连接；基于表示变换可直接映射既有结果。

- move_code：CONTRIBUTION_CLAIM

- statement_status：contribution_claim

- why_here_cn：把SIMU/MISU纳入统一框架。

- inherits_from_previous_cn：由Section 4.3映射关系提炼。

- changes_argument_state_cn：扩展统一范围到所有基本拍卖类型。

- sets_up_next_cn：为MIMU-XOR最一般性声明服务。

- failure_if_removed_cn：统一贡献只覆盖OR/XOR，不覆盖经典特例。

- evidence_pointer：Section 8 P2

### 6. Section 8 P2 S2

- order：6

- locator：Section 8 P2 S2

- paraphrase_cn：因此本文提出统一框架，以MIMU-XOR为最一般情形，可映射为MIMU-OR并退化为SIMU/MISU。

- move_code：CONTRIBUTION_CLAIM

- statement_status：contribution_claim

- why_here_cn：给出全文最强统一性声明。

- inherits_from_previous_cn：由前两句综合。

- changes_argument_state_cn：确立MIMU-XOR的中心地位。

- sets_up_next_cn：强调该理解的深层价值。

- failure_if_removed_cn：核心贡献不可识别。

- evidence_pointer：Section 8 P2

### 7. Section 8 P2 S3

- order：7

- locator：Section 8 P2 S3

- paraphrase_cn：鉴于SIMU/MISU和OR/XOR之间存在根本差异，发现的映射关系进一步推动对不同组合拍卖的理解。

- move_code：CONTRIBUTION_CLAIM

- statement_status：contribution_claim

- why_here_cn：解释为什么统一不是平凡结果。

- inherits_from_previous_cn：承接统一框架声明。

- changes_argument_state_cn：把统一贡献定义为理解升级。

- sets_up_next_cn：转入计算制品的贡献。

- failure_if_removed_cn：统一贡献的难度没有表达。

- evidence_pointer：Section 8 P2

### 8. Section 8 P3 S1

- order：8

- locator：Section 8 P3 S1

- paraphrase_cn：理论结果自然产生计算设计；提出数据结构和算法追踪所有子auction的value与winner。

- move_code：CONTRIBUTION_CLAIM

- statement_status：contribution_claim

- why_here_cn：重述理论到制品的因果关系。

- inherits_from_previous_cn：由理论统一转入计算实现。

- changes_argument_state_cn：建立计算基础设施贡献。

- sets_up_next_cn：加入模拟证据。

- failure_if_removed_cn：数字制品的贡献缺少理论来源。

- evidence_pointer：Section 8 P3

### 9. Section 8 P3 S2

- order：9

- locator：Section 8 P3 S2

- paraphrase_cn：模拟实验表明即使在最坏情形（只有singleton标）也能为实际相关规模提供实时反馈。

- move_code：EMPIRICAL_RESULT

- statement_status：empirical_result

- why_here_cn：用最坏情形结果支持实时性主张。

- inherits_from_previous_cn：由Table 3/4结果提炼。

- changes_argument_state_cn：把理论可行性落实为实测证据。

- sets_up_next_cn：转向与IP的比较。

- failure_if_removed_cn：实时性主张没有证据。

- evidence_pointer：Section 8 P3; Tables 3-4

### 10. Section 8 P3 S3

- order：10

- locator：Section 8 P3 S3

- paraphrase_cn：通过系统性追踪和更新所有子auction，本文实现大幅优于基于IP的传统方法，且是在合理查询频率下。

- move_code：EMPIRICAL_RESULT

- statement_status：empirical_result

- why_here_cn：用基准结果支持相对优势。

- inherits_from_previous_cn：由Table 5/6提炼。

- changes_argument_state_cn：制品从可行升级为更优。

- sets_up_next_cn：引出‘唯一适合’的判断。

- failure_if_removed_cn：相对优势主张没有证据。

- evidence_pointer：Section 8 P3; Tables 5-6

### 11. Section 8 P3 S4

- order：11

- locator：Section 8 P3 S4

- paraphrase_cn：因此本方法特别适合高效提供综合bidder support。

- move_code：CONTRIBUTION_CLAIM

- statement_status：contribution_claim

- why_here_cn：把证据升格为对制品独特定位的总结。

- inherits_from_previous_cn：由前两句结果综合。

- changes_argument_state_cn：完成计算贡献声明。

- sets_up_next_cn：转向状态空间边界。

- failure_if_removed_cn：性能优势没有贡献性总结。

- evidence_pointer：Section 8 P3

### 12. Section 8 P4 S1

- order：12

- locator：Section 8 P4 S1

- paraphrase_cn：一般MIMU状态空间很大，且并非每个bundle都有价值；因此讨论带package constraints的batch与hierarchical变体。

- move_code：BOUNDARY

- statement_status：author_inference

- why_here_cn：给统一理论加适用边界，并为扩展章节作总结。

- inherits_from_previous_cn：由Section 6内容提炼。

- changes_argument_state_cn：把扩展重新框定为边界条件。

- sets_up_next_cn：为大规模在线市场应用服务。

- failure_if_removed_cn：一般MIMU的规模限制未被承认。

- evidence_pointer：Section 8 P4

### 13. Section 8 P4 S2

- order：13

- locator：Section 8 P4 S2

- paraphrase_cn：一般MIMU理论可直接用于batch和hierarchical；由于permitted bundles更少，可处理更大规模，是大型在线市场的有前景机制。

- move_code：EXTENSION_CONTRIBUTION

- statement_status：contribution_claim

- why_here_cn：把约束扩展写成正向贡献，而非附带说明。

- inherits_from_previous_cn：由Section 6结果支持。

- changes_argument_state_cn：扩展研究成果。

- sets_up_next_cn：转入reverse拍卖。

- failure_if_removed_cn：扩展章节没有在结论中兑现。

- evidence_pointer：Section 8 P4; Section 6

### 14. Section 8 P4 S3

- order：14

- locator：Section 8 P4 S3

- paraphrase_cn：最后考虑reverse MIMU拍卖，尽管有重要区别，前向MIMU主要结果可自然扩展。

- move_code：EXTENSION_CONTRIBUTION

- statement_status：contribution_claim

- why_here_cn：总结reverse扩展。

- inherits_from_previous_cn：由Section 7结果支持。

- changes_argument_state_cn：把reverse也纳入贡献版图。

- sets_up_next_cn：给出reverse实际意义。

- failure_if_removed_cn：reverse扩展被遗漏。

- evidence_pointer：Section 8 P4; Section 7

### 15. Section 8 P4 S4

- order：15

- locator：Section 8 P4 S4

- paraphrase_cn：由于reverse拍卖广泛用于采购，本文结果可改善该场景的时间和经济效益。

- move_code：PRACTICAL_STAKE

- statement_status：contribution_claim

- why_here_cn：把扩展连接到现实应用价值。

- inherits_from_previous_cn：承接reverse扩展。

- changes_argument_state_cn：强化实践相关性。

- sets_up_next_cn：为未来方向收尾。

- failure_if_removed_cn：reverse扩展缺少现实意义。

- evidence_pointer：Section 8 P4

### 16. Section 8 P5 S1

- order：16

- locator：Section 8 P5 S1

- paraphrase_cn：未来方向之一是重新审视有拍卖机制/活动规则限制的专门MIMU机制，当前WL/DL会变成下限。

- move_code：FUTURE_WORK

- statement_status：author_inference

- why_here_cn：承认当前研究未覆盖专门机制，并给出可推导的边界直觉。

- inherits_from_previous_cn：由全文无限制模型延伸。

- changes_argument_state_cn：布置未来研究第一项。

- sets_up_next_cn：继续列未来方向。

- failure_if_removed_cn：无限制模型的边界不够诚实。

- evidence_pointer：Section 8 P5

### 17. Section 8 P5 S2

- order：17

- locator：Section 8 P5 S2

- paraphrase_cn：未来可研究直接高效计算支持信息的专用IP公式。

- move_code：FUTURE_WORK

- statement_status：author_inference

- why_here_cn：回应benchmark部分对IP可改进性的讨论。

- inherits_from_previous_cn：由Section 5.3未来段延伸。

- changes_argument_state_cn：布置未来研究第二项。

- sets_up_next_cn：继续未来方向。

- failure_if_removed_cn：IP改进可能性没有后续处理。

- evidence_pointer：Section 8 P5

### 18. Section 8 P5 S3

- order：18

- locator：Section 8 P5 S3

- paraphrase_cn：未来可把框架推广到多买方多卖方共存的组合交易所。

- move_code：FUTURE_WORK

- statement_status：author_inference

- why_here_cn：指出从双向拍卖再进一步的一般化方向。

- inherits_from_previous_cn：由reverse拍卖扩展逻辑延伸。

- changes_argument_state_cn：布置未来研究第三项。

- sets_up_next_cn：以自动投标系统收尾。

- failure_if_removed_cn：一般化方向缺一项。

- evidence_pointer：Section 8 P5

### 19. Section 8 P5 S4

- order：19

- locator：Section 8 P5 S4

- paraphrase_cn：最后，未来可构建MIMU拍卖自动投标系统，需要把算法扩展到更大规模并考虑人类因素。

- move_code：FUTURE_WORK

- statement_status：author_inference

- why_here_cn：与引言P8的自动投标系统预告呼应，给出未来应用蓝图。

- inherits_from_previous_cn：由全篇计算制品延伸。

- changes_argument_state_cn：把未来方向落到行为/人因研究。

- sets_up_next_cn：结束全文。

- failure_if_removed_cn：引言中自动投标系统的伏笔没有回收。

- evidence_pointer：Section 8 P5

## Study累积逻辑

### 1. 1

- study_or_phase：阶段1：MIMU-XOR理论结果推导（Section 3）

- evidence_job_cn：建立最一般情形的理论基础：子auction更新递推、winning/deadness公式、活标上界。

- what_it_establishes_cn：证明在MIMU-XOR中支持指标可计算，且子auction是核心构建模块。

- what_it_cannot_establish_cn：不能证明OR拍卖结果可从XOR导出，不能证明SIMU/MISU可被覆盖，也不能证明公式可实时实现。

- why_next_phase_is_needed_cn：需要把结果扩展到OR语言以及SIMU/MISU特例，才能宣称统一框架。

- transition_wording_function_cn：Section 4开头明确‘OR结果可由XOR推出’，把理论范围扩大。

### 2. 2

- study_or_phase：阶段2：MIMU-OR化约与SIMU/MISU统一（Section 4）

- evidence_job_cn：用OR-as-XOR等价化约覆盖OR，再用表示退化覆盖SIMU/MISU。

- what_it_establishes_cn：MIMU-XOR是最一般情形；OR、SIMU、MISU的支持结果均可推导。

- what_it_cannot_establish_cn：不能证明理论能转化成计算制品，也不能证明实时效率。

- why_next_phase_is_needed_cn：需要一个可执行的数据结构和算法来兑现‘实时bidder support’。

- transition_wording_function_cn：Section 5开头把理论结果直接引向三个设计目标。

### 3. 3

- study_or_phase：阶段3：MIMU-OR实现与模拟（Section 5.1）

- evidence_job_cn：证明理论公式可制品化，并在最坏/平均合成数据上实现可用效率。

- what_it_establishes_cn：VAL/LastWinBid+Algorithm 1/2能增量维持子auction状态；WL查询极快，更新是瓶颈。

- what_it_cannot_establish_cn：不能证明XOR情形也可行，也不能证明方法优于常用IP。

- why_next_phase_is_needed_cn：需要处理XOR的bidder coalition维度并建立相对优势证据。

- transition_wording_function_cn：Section 5.2开头说‘类似地’扩展二维数组；5.3开头引入IP作为替代策略。

### 4. 4

- study_or_phase：阶段4：MIMU-XOR实现与模拟（Section 5.2）

- evidence_job_cn：证明最一般XOR情形也能在合理规模内实时计算支持信息。

- what_it_establishes_cn：二维bitmap能处理VCS/coalition，更新在测试规模下多为毫秒级。

- what_it_cannot_establish_cn：不能证明相对IP有优势。

- why_next_phase_is_needed_cn：需要与领域常规IP方法做同一任务基准。

- transition_wording_function_cn：Section 5.3建立替代策略并比较。

### 5. 5

- study_or_phase：阶段5：与IP/CPLEX性能基准对比（Section 5.3）

- evidence_job_cn：把制品优势从‘自身快’升级为‘优于常用方法’。

- what_it_establishes_cn：计算全部WL/DL时IP慢几个数量级，尤其DL；只有查询极低频时IP才可能更快。

- what_it_cannot_establish_cn：不能证明在真实拍卖数据、更多bidder/物品规模或更优IP制定下仍占优。

- why_next_phase_is_needed_cn：一般MIMU状态空间巨大，需要演示约束/反向扩展以证明更广适用。

- transition_wording_function_cn：Section 6以状态空间巨大开头，转向两个约束特例。

### 6. 6

- study_or_phase：阶段6：Batch-based MIMU扩展（Section 6.1）

- evidence_job_cn：证明统一理论在固定批次容量约束下自动成立且计算更省。

- what_it_establishes_cn：permitted spans数量约降为1/Ω，增量更新只需追踪S中的子auction，可处理更大规模。

- what_it_cannot_establish_cn：不能证明更一般的非闭合span结构（如层级）也可处理。

- why_next_phase_is_needed_cn：需要处理互补span可能非permitted的更复杂情形。

- transition_wording_function_cn：Section 6.2以‘另一个重要特例’开启hierarchical扩展。

### 7. 7

- study_or_phase：阶段7：Hierarchical MIMU扩展（Section 6.2）

- evidence_job_cn：证明理论在permitted packages构成树时可迁移，并处理非permitted互补span。

- what_it_establishes_cn：只需考虑父span的更新，非permitted互补span可分解为permitted spans之和，因而可处理更大拍卖。

- what_it_cannot_establish_cn：不能证明适用于成本最小化的reverse拍卖。

- why_next_phase_is_needed_cn：需要把方向性差异（最小化成本、新的子auction定义）纳入框架。

- transition_wording_function_cn：Section 7以‘到目前为止是forward，现在转向reverse’开启。

### 8. 8

- study_or_phase：阶段8：Reverse MIMU拍卖扩展（Section 7）

- evidence_job_cn：证明统一理论经成本最小化和子auction定义调整后适用于采购拍卖。

- what_it_establishes_cn：R-MIMU-OR的WL/DL公式可用类似结构导出，只是方向上下界反转。

- what_it_cannot_establish_cn：不能证明reverse XOR扩展已完整构建；也没有reverse模拟或实证。

- why_next_phase_is_needed_cn：理论覆盖面已达到本文边界，结论中用未来研究收拾残局。

- transition_wording_function_cn：Section 8把forward/reverse/约束扩展统一为贡献和边界。

## 主张—证据台账

### 1. MIMU-XOR拍卖中，winning/deadness level和活标条件可由子auction理论正确刻画。

- claim_cn：MIMU-XOR拍卖中，winning/deadness level和活标条件可由子auction理论正确刻画。

- claim_level：theory

- supporting_evidence_cn：Theorem 1-3与Corollary 2，附录A形式证明，Illustration 1-2数值例证。

- support_strength：direct

- where_claim_is_made：Section 3.2-3.4; Abstract S5

- where_evidence_is_provided：Section 3.2-3.4; online Appendix A

### 2. OR拍卖的bidder support结果可由XOR结果直接导出。

- claim_cn：OR拍卖的bidder support结果可由XOR结果直接导出。

- claim_level：theory

- supporting_evidence_cn：OR as XOR唯一bidder化约，Table 2公式汇总，附录B证明，Illustration 3-4。

- support_strength：direct

- where_claim_is_made：Section 4.1-4.2; Abstract S6

- where_evidence_is_provided：Section 4.1-4.2; Table 2; online Appendix B

### 3. MIMU-XOR是最一般情形，可映射到MIMU-OR并退化为SIMU/MISU，从而统一两研究流。

- claim_cn：MIMU-XOR是最一般情形，可映射到MIMU-OR并退化为SIMU/MISU，从而统一两研究流。

- claim_level：theory

- supporting_evidence_cn：表示退化（M=1或u_j=1）、Figure 2映射、Observation 1-3、附录C汇总。

- support_strength：direct

- where_claim_is_made：Section 4.3; Abstract S7; Section 8 P2

- where_evidence_is_provided：Section 4.3; Figure 2; online Appendix C

### 4. 本文实现能在实际相关拍卖规模下实时提供bidder support信息。

- claim_cn：本文实现能在实际相关拍卖规模下实时提供bidder support信息。

- claim_level：artifact

- supporting_evidence_cn：Table 3/4最坏与平均模拟计时，覆盖M=2-5、u=25-50、|N|=4/8等规模。

- support_strength：partial

- where_claim_is_made：Section 5.1-5.2; Section 8 P3 S2

- where_evidence_is_provided：Section 5.1-5.2; Tables 3-4

### 5. 与IP/CPLEX按需计算相比，本文方法在计算全部WL/DL时快若干数量级。

- claim_cn：与IP/CPLEX按需计算相比，本文方法在计算全部WL/DL时快若干数量级。

- claim_level：artifact

- supporting_evidence_cn：Tables 5-6基准对比，同一任务、同一硬件、对IP有利的工时统计；给出查询频率边界。

- support_strength：partial

- where_claim_is_made：Section 5.3; Abstract S8; Section 8 P3 S3

- where_evidence_is_provided：Section 5.3; Tables 5-6; endnotes 7-10

### 6. 统一理论可扩展到batch-based和hierarchical MIMU约束拍卖。

- claim_cn：统一理论可扩展到batch-based和hierarchical MIMU约束拍卖。

- claim_level：boundary

- supporting_evidence_cn：Section 6.1-6.2形式化定义、Theorem F.1/Corollary F.1、Illustration 5、附录F/G模拟。

- support_strength：partial

- where_claim_is_made：Section 6; Section 8 P4

- where_evidence_is_provided：Section 6; online Appendices F-G

### 7. 统一理论可扩展到reverse MIMU拍卖。

- claim_cn：统一理论可扩展到reverse MIMU拍卖。

- claim_level：boundary

- supporting_evidence_cn：Section 7调整子auction与成本最小化，Table 7公式，Illustration 6，附录H证明。

- support_strength：partial

- where_claim_is_made：Section 7; Abstract S9; Section 8 P4

- where_evidence_is_provided：Section 7; Table 7; online Appendix H

## ISR定位逻辑

- constitutive_is_problem_cn：文章把一个算法/拍卖理论问题写成IS问题的方式是：数字市场机制（组合拍卖）的价值取决于参与者能否在实时环境中使用信息反馈；缺乏计算可得、客观、实时bidder support是市场设计的重要组成部分。问题不是单纯算法复杂度，而是实时信息反馈与市场采纳之间的相互构成。

- technology_behavior_or_market_entanglement_cn：技术制品与行为/市场纠缠较弱但存在：作者明确说支持信息用于辅助竞拍者决策并可能支持自动投标系统；但他们不做行为实验，只保证客观计算信息可以实时产生。纠缠主要停留在机制设计层面：实时信息决定市场能否被采纳。

- role_of_benchmark_or_objective_evidence_cn：模拟与IP基准不是用来支持行为主张，而是支持‘该理论能落地成实时计算基础设施’这一IS制品主张；客观运行时间、同一任务计算全部WL/DL、查询频率临界点把制品的价值从‘算法快’升到‘可支持市场参与者高频查询’。

- theory_in_design_cn：理论直接进入设计：Theorem 1决定增量更新只遍历互补子auction；winning/deadness公式决定查询只需查VAL和遍历较大span；VCS/OR-as-XOR决定MIMU-XOR需要二维bitmap、MIMU-OR可一维化。理论不是只用来解释结果，而是规定了数据结构、更新条件和存储维度。

- technical_vs_is_contribution_balance_cn：篇幅上技术/理论贡献占主导（定理、算法、模拟、benchmark），IS贡献通过统一已有IS/管理科学中的两类拍卖研究（MISU/SIMU）以及实时反馈的市场采用意义来体现；没有行为实验，实践贡献是推断性的。

- beyond_transient_performance_cn：作者用三种方式把贡献从一次性速度优势提升：把OR-as-XOR作为理论化约并给出为何不用OR*；把SIMU/MISU纳入退化映射；用batch/hierarchical/reverse扩展证明结果可迁移。不过‘超越’主要靠理论统一和扩展，而非实证。

## 段落级仿写模板

### abstract_steps

1. 第1句：指出某机制有公认优点但采纳受限，把原因归于缺失某类支持信息。

2. 第2句：宣布研究一般化问题的bidder support。

3. 第3句：把研究对象限定到一个限制最少的机制变体。

4. 第4句：引入两个关键分析维度（如投标语言）。

5. 第5-6句：报告对最一般情形的理论推导，并给出一个化约关系把其他语言/情形纳入。

6. 第7句：声明最一般情形的统一地位及对已有特例的覆盖。

7. 第8句：预告理论导致的算法和与常用baseline相比的优势。

8. 第9句：预告扩展范围。

### introduction_paragraph_steps

1. 第1段：介绍机制及现实价值，建立研究动机。

2. 第2段：指出机制在目标市场采纳有限，给出两个参与复杂性因素。

3. 第3段：转向更合适的机制变体，提出支持信息需求和实时要求。

4. 第4段：综述已有支持方案和两类特例，暴露一般情形缺口并说明难度。

5. 第5段：宣布研究问题，引入核心分析维度。

6. 第6段：给出建模假设和边界。

7. 第7段：用图/路线图预告理论→制品→基准→扩展。

8. 第8段：预先声明理论、统一、实践三层贡献。

### theory_to_design_steps

1. 定义正式状态（如auction size、bid tuple）。

2. 定义核心构建模块（如subauction）。

3. 给出动态递推定理（新事件如何改变模块状态）。

4. 从递推导出支持指标公式（winning/deadness）。

5. 给出复杂度上界（如活标数）并构造紧性例证。

6. 把其他语言/特例化约为最一般情形。

7. 选择能支持公式中关键运算的表示（如整数映射）。

8. 把公式翻译为设计目标、数据结构和算法。

9. 为评价设计模拟和baseline。

### method_and_study_sequence_steps

1. 先立最一般理论，再化约特殊情形，最后实现，确保统一是推导出来的而非拼凑的。

2. 实现前明确三个设计目标，让每个数据结构都有理论来源。

3. 模拟分最坏和平均两类，给性能边界。

4. 基准必须与常用方法做同一总任务，并计入本文增量更新成本。

5. 报告边界条件（如查询频率）以增加公平性。

6. 用约束变体和反向拍卖展示可迁移性。

### results_reporting_steps

1. 先报告自身模拟：更新是瓶颈、WL查询极快、DL较慢。

2. 再报告XOR实现如何随bidder数指数增长但在测试规模内可用。

3. 再报告与IP基准的数量级差距，强调DL尤其慢。

4. 报告IP可能占优的边界，并解释本文适合的综合高频场景。

5. 最后在结论中用最坏情形和基准结果重述实时性和优越性。

### discussion_and_contribution_steps

1. 第1段：重述问题和核心理论机制，并给统一化约。

2. 第2段：声明统一框架及其对经典特例的覆盖。

3. 第3段：重述计算制品的贡献并用模拟/基准结果支撑。

4. 第4段：给出状态空间边界，把约束/反向扩展转为贡献。

5. 第5段：列出未来方向，并回收引言中的伏笔。

## 可执行写作算法

### 1. 1

- step：1

- rhetorical_job_cn：构建机制价值和采纳障碍的反差，把问题归于支持信息缺失。

- research_evidence_required_cn：需要文献/案例证明机制有实际价值且消费市场采纳有限。

- sentence_pattern_function_cn：先给机制定义和应用，再用‘despite/limited’转折引入障碍。

- transition_condition_cn：当读者接受‘缺支持信息是采纳障碍’时，进入信息需求。

### 2. 2

- step：2

- rhetorical_job_cn：建立实时支持信息的需求并限定机制类型。

- research_evidence_required_cn：需要论证连续拍卖比迭代拍卖更适合消费市场，且实时信息是必要非充分。

- sentence_pattern_function_cn：用‘it must be provided in timely fashion; otherwise...’给出必要条件与反面后果。

- transition_condition_cn：当读者接受实时信息需求后，进入已有方案综述。

### 3. 3

- step：3

- rhetorical_job_cn：综述已有支持方案，暴露一般化缺口并说明难度。

- research_evidence_required_cn：需要有可借鉴的特例研究（MISU/SIMU）和作者自己的核心概念传统（subauction）。

- sentence_pattern_function_cn：先列已有指标，再说已有覆盖局限，再用‘despite...remained challenge’点出缺口。

- transition_condition_cn：当缺口被读者接受，进入研究问题和分析维度。

### 4. 4

- step：4

- rhetorical_job_cn：正式宣布研究问题、核心分析维度和模型边界。

- research_evidence_required_cn：需要明确的语言区分（OR/XOR）和建模假设（all-or-nothing、价值最大化、无行为假设）。

- sentence_pattern_function_cn：用‘we study...We consider...we have three considerations’铺设边界。

- transition_condition_cn：当边界清晰后，可给出全文路线图。

### 5. 5

- step：5

- rhetorical_job_cn：建立最一般情形的正式理论并证明核心定理。

- research_evidence_required_cn：需要严格定义、递推定理、支持指标公式和活标上界，以及至少一个构造性例证。

- sentence_pattern_function_cn：定义核心构建模块，再给‘Theorem+直觉解释+Illustration’。

- transition_condition_cn：当最一般情形公式完整后，进入化约与统一。

### 6. 6

- step：6

- rhetorical_job_cn：把其他语言和特例化约为最一般情形，建立统一框架。

- research_evidence_required_cn：需要表示变换（OR as XOR、M=1或u_j=1）和公式对比表，并说明为何不用替代路线（OR*）。

- sentence_pattern_function_cn：用‘can be viewed as...directly derived’给出化约，再用‘we note other ways...however’排除替代方向。

- transition_condition_cn：当统一框架建立后，进入理论到制品的转换。

### 7. 7

- step：7

- rhetorical_job_cn：把理论公式翻译成设计目标、数据结构和算法。

- research_evidence_required_cn：需要每个设计目标都有理论来源，并给出数据结构的空间复杂度和算法伪代码。

- sentence_pattern_function_cn：先用‘implementation is informed directly by...’列出三个目标，再逐项给数据结构和算法。

- transition_condition_cn：当实现完成后，设计模拟和benchmark。

### 8. 8

- step：8

- rhetorical_job_cn：用模拟和基准证明制品的实时性与相对优势，并报告边界。

- research_evidence_required_cn：需要最坏/平均合成数据、参数扫描、同一总任务下的IP基准、对baseline有利的工时处理。

- sentence_pattern_function_cn：先报自身性能，再报与IP数量级差距，最后用‘can potentially outperform when...’给边界。

- transition_condition_cn：当性能和边界都清楚后，进入扩展与结论。

### 9. 9

- step：9

- rhetorical_job_cn：用约束变体和反向拍卖展示可迁移性，并在结论中完成贡献、边界和未来。

- research_evidence_required_cn：需要每个扩展的形式化定义和至少一个例证/模拟，以及结论对副引用的回收。

- sentence_pattern_function_cn：扩展用‘we discuss two special cases...Finally we consider reverse’，结论用‘In this paper...Several directions are open’。

- transition_condition_cn：当扩展、边界和未来都覆盖后，文章可收束。

## 应模仿的高价值动作

1. 嵌套式缺口构建：机制价值→采纳障碍→信息需求→已有方案只覆盖特例→一般情形缺口且有难度。

2. 用‘OR as XOR with unique bidder’做理论化约，并明确排除OR*路线，使统一不仅成立还具备可推导性。

3. 理论结果直接决定三个设计目标，让每个数据结构都能追溯到定理而非工程偏好。

4. 用同一总任务（计算全部WL/DL）做基准，并把增量更新成本计入本文方法；对IP做有利处理（不计预处理、不强制tie-breaking）再报告边界。

5. 用worst-case singleton vs average-case random活标分开报告性能，给出复杂度边界。

6. 在每个定理后立即放Illustration数值例证，把抽象公式落地。

7. 用Observation 1-3提炼XOR/OR共享和差异，把推导结果变成可迁移的理论洞察。

8. 用batch/hierarchical/reverse三个扩展证明结果不是一次性特例，并在结论中把扩展重新框定为贡献。

9. 结论逐段回收引言中的问题、路线图、实践伏笔（自动投标系统）。

## 不要只复制的表面动作

1. 不能只写‘组合拍卖好但采纳有限’而不连接到具体支持信息需求。

2. 不能只说‘统一了’而不给出显式表示映射、公式表或化约说明。

3. 不能只claim实时支持而不提供模拟计时和worst-case分析。

4. 不能只用‘比IP快’一句话，需要同一任务、计入更新成本、给查询频率边界。

5. 不能把算法性能直接当作IS贡献而不连接市场采纳、决策支持或自动投标系统。

6. 不能把扩展写成列表，要用形式定义+例证说明每个扩展如何调整核心概念。

7. 不能宣称‘支持竞拍者’但没有行为实验或至少明确说明这是客观计算信息而非用户效用。

## 证据薄弱或跳跃的动作

1. ‘支持bidders做出更明智决策’没有行为实验支撑，属于推断性实践贡献。

2. OR-as-XOR会使bidder数量随时间k增长，可能产生理论代价（N_k不断扩张），正文未深入讨论。

3. Theorem 3的活标紧上界已推导，但实现并未利用该上界做存储剪枝，理论红利没有被兑现。

4. IP基准只针对直接IP公式和CPLEX，未与缓存机制或专用IP公式比较；作者自己承认这是未来方向。

5. 模拟基于合成数据，没有真实拍卖数据或真实竞拍者验证；‘实践中相关规模’是作者的选择而非外部验证。

6. reverse MIMU-XOR扩展只在Section 7末尾简要提及，未给出完整公式与证明。

7. batch/hierarchical的完整证明和模拟放在在线附录，正文只有断言和例证，主文不可见。

8. 把‘计算基础设施’称为市场设计贡献，但没有部署或采用证据，贡献等级存在跳跃。

## 一句话套路

用子auction递推把最一般的MIMU-XOR理论建立起来，再用‘OR=每个标由唯一bidder提交的XOR’这一等价化约把MIMU-OR和SIMU/MISU统一进来，随后把公式翻译成增量式数据结构并以IP/CPLEX为baseline证明实时综合支持优势，最后用batch/hierarchical/reverse扩展证明框架可迁移，从而把看似算法性能的工作写成IS市场设计中的bidder support统一理论。

## 分析边界

Markdown转录缺少图1/图2视觉细节，附录A-K未在正文，表格格式可能丢失；位置使用章节/段落索引而非页码；OCR导致部分公式符号错乱，但论证句和定理声明可辨识。
