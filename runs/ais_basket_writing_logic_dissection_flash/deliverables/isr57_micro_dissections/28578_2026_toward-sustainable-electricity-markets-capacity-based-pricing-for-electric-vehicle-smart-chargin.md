# Toward Sustainable Electricity Markets: Capacity-Based Pricing for Electric Vehicle Smart Charging：ISR 句段级微观图谱

- 作者：Konstantina Valogianni; Wolfgang Ketter; John Collins; Gediminas Adomavicius
- 年份：2026
- DOI：10.1287/isre.2023.0078
- 源文件：28578_2026_toward-sustainable-electricity-markets-capacity-based-pricing-for-electric-vehicle-smart-chargin.md
- 置信度：0.86

## 核实后的宏观骨架

论文按设计科学（Gregor & Hevner 'Improvement'类）结构组织：问题与缺陷建构（摘要、引言、背景）→ 制品定义与形式化（Section 3）→ 解析启发式与理论性质（Section 4）→ 计算启发式（Section 5）→ 多agent仿真testbed与真实数据校准（Section 6）→ 三个难度递进的评价场景及稳健性检验（Section 7）→ 讨论、贡献、边界与未来方向（Section 8）。核心制品为容量定价（CBP）公式 P_t(r)=P0,t+αt·r；价格设定方法为解析启发式AH与计算启发式CH，CH以AH为初值并用聚合数据调整。七个阶段依次累积：解析推导、CH设计、仿真平台构建、平坦曲线场景、非平坦EV曲线场景、PV跟随场景、稳健性检验。

## 摘要逐句图谱

### 1. Abstract P1 S1

- order：1

- locator：Abstract P1 S1

- paraphrase_cn：提出一个IS赋能的、支持可变速率EV充电的定价制品，可促进可持续EV普及。

- move_code：OPEN_ARTIFACT_CLAIM

- statement_status：contribution_claim

- why_here_cn：摘要首句直接给出全文核心发明，让读者立即知道本文提供什么。

- inherits_from_previous_cn：无，是摘要论点的锚点。

- changes_argument_state_cn：从无到有建立全文对象：一个定价制品。

- sets_up_next_cn：需要说明为什么需要这个制品（下一句的碳强度和电网稳定问题）。

- failure_if_removed_cn：读者无法在开头知道论文交付物是什么，摘要变成问题综述。

- evidence_pointer：Abstract第一句

### 2. Abstract P1 S2

- order：2

- locator：Abstract P1 S2

- paraphrase_cn：EV能显著降低现代城市碳强度并应对重要可持续挑战。

- move_code：CONTEXT

- statement_status：prior_literature

- why_here_cn：建立EV的正面价值，使后文电网问题成为‘好事物带来的困难’，而非单纯负面。

- inherits_from_previous_cn：承接第1句的制品，为制品提供使用场景。

- changes_argument_state_cn：引入可持续发展的目标叙事。

- sets_up_next_cn：与下一句的峰值/稳定性风险形成对比。

- failure_if_removed_cn：缺少EV价值，后文的电网压力会被误解为纯技术问题而未上升到可持续性。

- evidence_pointer：Abstract第一段第二句

### 3. Abstract P1 S3

- order：3

- locator：Abstract P1 S3

- paraphrase_cn：但大规模EV引入预计会提高电力需求峰值，威胁电网稳定性和可靠性。

- move_code：PRACTICAL_STAKES

- statement_status：author_inference

- why_here_cn：在EV价值之后立刻给出风险，构成问题张力。

- inherits_from_previous_cn：依赖前句EV增长作为前提。

- changes_argument_state_cn：把‘EV好’转成‘EV普及有障碍’，界定问题。

- sets_up_next_cn：引出现有协调方法的缺点。

- failure_if_removed_cn：没有问题，制品的存在理由消失。

- evidence_pointer：Abstract第一段第三句

### 4. Abstract P1 S4

- order：4

- locator：Abstract P1 S4

- paraphrase_cn：多数提议的EV充电协调方法有缺点：不能保证电网与车主目标激励一致，或可能因车主收到相同价格信号而做出相似充电决策造成雪崩效应并形成新需求峰值。

- move_code：LIMITATION

- statement_status：prior_literature

- why_here_cn：迅速排除既有方案，制造空白。

- inherits_from_previous_cn：承接前句的电网压力，说明现有办法为何不够。

- changes_argument_state_cn：把问题从‘电网压力’转成‘激励不对齐与雪崩效应’这两个可设计解决的具体机制。

- sets_up_next_cn：为第5句引入CBP提供逻辑缺口。

- failure_if_removed_cn：没有缺口，制品只是另一个方案而非必要方案。

- evidence_pointer：Abstract第一段第四句

### 5. Abstract P2 S1

- order：5

- locator：Abstract P2 S1

- paraphrase_cn：为解决该问题，提出包含动态充电速率价格成分和基于解析/计算启发式的价格设定方法的容量定价制品。

- move_code：DESIGN_FEATURE

- statement_status：design_decision

- why_here_cn：在缺口之后立即给出解决物，并预告两个价格设定方法家族。

- inherits_from_previous_cn：‘To address this issue’直接承接第4句缺口。

- changes_argument_state_cn：从问题转向方案，建立全文核心对象的具体内容。

- sets_up_next_cn：接下来需要解释机制（个体优化与整体再平衡）。

- failure_if_removed_cn：摘要缺核心发明，贡献不清。

- evidence_pointer：Abstract第二段第一句

### 6. Abstract P2 S2-S3

- order：6

- locator：Abstract P2 S2-S3

- paraphrase_cn：该方法利用环境中多种可用信息，允许理性EV agent在其个体充电需求和约束下通过计划与调度优化自身成本，同时重新平衡总充电需求以缓解雪崩效应。

- move_code：REQUIREMENT_AND_MECHANISM

- statement_status：theory_claim

- why_here_cn：说明制品并非直接控制充电器，而是通过理性agent的自我优化与整体再平衡共同作用，回应引言中的分布式/集中式协调之争。

- inherits_from_previous_cn：依赖第5句制品的结构与第4句雪崩效应机制。

- changes_argument_state_cn：把设计细节翻译为行为机制：个体最优与全局再平衡兼容。

- sets_up_next_cn：支持第7-8句的结果和基准比较。

- failure_if_removed_cn：机制不清，后文结果无法解释为什么有效。

- evidence_pointer：Abstract第二段第二、三句

### 7. Abstract P3 S1-S2

- order：7

- locator：Abstract P3 S1-S2

- paraphrase_cn：该制品在降低需求波动或实现可再生能源出力与总充电需求匹配方面高度有效。

- move_code：RESULT

- statement_status：empirical_result

- why_here_cn：在机制之后给出结果主张，说明制品达成两种主要目标：降波动和匹配可再生。

- inherits_from_previous_cn：结果的有效性依赖前句所述机制成立。

- changes_argument_state_cn：从方案描述转为成果声明。

- sets_up_next_cn：接下来需要说明结果如何得到（与基准比较）。

- failure_if_removed_cn：摘要只剩下设计而无成效证据。

- evidence_pointer：Abstract第三段第一、二句

### 8. Abstract P3 S3

- order：8

- locator：Abstract P3 S3

- paraphrase_cn：通过与传统当前定价基准在多个现实场景中的实证比较展示收益。

- move_code：BENCHMARK_OR_CONTRAST

- statement_status：method_decision

- why_here_cn：使结果主张挂靠到‘相对现有实践的改进’框架，而非孤立的绝对性能。

- inherits_from_previous_cn：承接前句‘高度有效’，说明有效性是用什么参照系确定的。

- changes_argument_state_cn：引入评价方法作为证据来源。

- sets_up_next_cn：为末段的利益相关者价值主张提供证据基础。

- failure_if_removed_cn：结果缺少验证方式，读者无从判断。

- evidence_pointer：Abstract第三段第三句

### 9. Abstract P4-P5 S1-S3

- order：9

- locator：Abstract P4-P5 S1-S3

- paraphrase_cn：制品支持电网运营者跨时间重平衡总EV充电需求；使能源供应商在尊重市场约束情况下维持总收入；使市场利益相关者可诱导需求曲线跟随可再生发电模式，最大化可再生利用并减少低效。

- move_code：CONTRIBUTION

- statement_status：contribution_claim

- why_here_cn：把技术结果转译为三类利益相关者价值，使摘要面向IS读者并突出Green IS。

- inherits_from_previous_cn：所有价值主张都依赖前文结果和比较。

- changes_argument_state_cn：从‘制品有效’升华为‘对电网运营者、供应商、政策/市场利益相关者分别有意义’。

- sets_up_next_cn：结束摘要，把读者导向引言中的详细展开。

- failure_if_removed_cn：缺少利益相关者转译，摘要会停留在算法层面，失去IS定位。

- evidence_pointer：Abstract第四、五段

### 10. Abstract P5 末句（'Finally'之后）

- order：10

- locator：Abstract P5 末句（'Finally'之后）

- paraphrase_cn：最终强调可诱导需求跟随可再生能源并最大化其利用，减少低效。

- move_code：CONTRIBUTION_ESCALATION

- statement_status：contribution_claim

- why_here_cn：将最后一个贡献指向可持续性目标，呼应Green IS核心价值。

- inherits_from_previous_cn：依赖‘跟随可再生’的机制与仿真结果。

- changes_argument_state_cn：把贡献从运营效率扩到环境可持续。

- sets_up_next_cn：无，摘要结束。

- failure_if_removed_cn：摘要缺少环境意义，削弱Green IS定位。

- evidence_pointer：Abstract末段

## 引言逐句图谱

### 1. Introduction P1 S1-S3

- order：1

- locator：Introduction P1 S1-S3

- paraphrase_cn：现代城市被转化为产生大量数据的智能环境；智能城市的需求之一是降低碳强度并提高交通可用性；EV因减排潜力而流行。

- move_code：CONTEXT

- statement_status：prior_literature

- why_here_cn：引言第一段把研究问题嵌入智能城市、数据、气候的大叙事，建立宏观正当性。

- inherits_from_previous_cn：无，独立开场。

- changes_argument_state_cn：提出研究舞台：智能城市、碳减排、EV。

- sets_up_next_cn：需要提出EV带来的电网问题。

- failure_if_removed_cn：缺少宏观背景，后文的‘可持续EV引入’没有意义锚点。

- evidence_pointer：Introduction P1

### 2. Introduction P1 S4-S6

- order：2

- locator：Introduction P1 S4-S6

- paraphrase_cn：巴黎宣言设定了2030年1亿辆EV目标，2021年全球EV数量增长108%超过1100万辆；但大规模引入EV到现有电网将带来重要稳定性挑战，IS研究可以应对。

- move_code：PRACTICAL_STAKES

- statement_status：prior_literature

- why_here_cn：用具体目标与增长数据把问题现实化，并首次说出IS可介入。

- inherits_from_previous_cn：承接EV流行的背景。

- changes_argument_state_cn：把EV从环境机会转化为电网稳定议题，并为IS角色定位。

- sets_up_next_cn：下一段具体说明电网问题。

- failure_if_removed_cn：‘大规模EV是问题’缺乏数据支撑且IS定位无出处。

- evidence_pointer：Introduction P1 S4-S6

### 3. Introduction P2 S1-S2

- order：3

- locator：Introduction P2 S1-S2

- paraphrase_cn：现有电网不是为大量EV在傍晚高峰充电设计的；EV充电器是家庭最高功率负荷并运行很长时间。

- move_code：MECHANISM

- statement_status：author_inference

- why_here_cn：说明为什么EV会摧毁电网平衡：高峰时段叠加、高功率负荷。

- inherits_from_previous_cn：依赖前段‘大规模引入造成稳定性挑战’。

- changes_argument_state_cn：把宏观风险具体化为时间与功率两个机制。

- sets_up_next_cn：指向‘扩容还是需求侧管理’的选择。

- failure_if_removed_cn：问题机制不清，后文雪崩效应和容量定价缺少基础。

- evidence_pointer：Introduction P2 S1-S2

### 4. Introduction P2 S3-S5

- order：4

- locator：Introduction P2 S3-S5

- paraphrase_cn：传统应对方式只有两条：投资额外电网基础设施或提供低价换取高需求时远程关闭充电器的许可；但扩容极其昂贵且不可持续，因为额外峰值需求几乎肯定需要新建低效快响应燃气轮机等峰值机组。

- move_code：LIMITATION

- statement_status：prior_literature

- why_here_cn：用基础设施成本和环境不可持续性排除传统扩容路线，为需求侧定价方案开路。

- inherits_from_previous_cn：承接电网压力机制。

- changes_argument_state_cn：界定了讨论的解空间：需求侧协调而非物理扩容。

- sets_up_next_cn：引入现有充电协调方案及其缺陷。

- failure_if_removed_cn：读者不知道为何需要新的协调机制。

- evidence_pointer：Introduction P2 S3-S5

### 5. Introduction P3 S1-S2

- order：5

- locator：Introduction P3 S1-S2

- paraphrase_cn：现有EV充电协调方案有短板，大多源于无法实现电网与顾客激励一致，常导致雪崩效应；雪崩效应是类似顾客响应导致低价时段拥堵和新增峰值。

- move_code：PHENOMENON_DEFINITION

- statement_status：author_inference

- why_here_cn：提出全文要解决的‘现象’：雪崩效应与激励不对齐。

- inherits_from_previous_cn：直接承接前段‘现有方案’及其结构局限。

- changes_argument_state_cn：把研究问题从‘电网压力’转成可设计的‘激励一致与雪崩效应’机制问题。

- sets_up_next_cn：下一句解释雪崩效应的因果机制。

- failure_if_removed_cn：论文核心对手盘消失，CBP的贡献无对象。

- evidence_pointer：Introduction P3 S1-S2

### 6. Introduction P3 S3

- order：6

- locator：Introduction P3 S3

- paraphrase_cn：雪崩效应已在本领域及真实世界试点中被观察到，并可能加剧峰值而非缓解峰值。

- move_code：PHENOMENON_CONFIRMATION

- statement_status：prior_literature

- why_here_cn：引文献和试点的观察证据证明雪崩效应真实存在，而非作者臆想。

- inherits_from_previous_cn：承接现象定义。

- changes_argument_state_cn：把现象从定义升级为经验事实。

- sets_up_next_cn：为后文‘必须设计机制抑制雪崩’提供证据。

- failure_if_removed_cn：现象若只是概念，后文机制和结果的紧迫性不足。

- evidence_pointer：Introduction P3 S3

### 7. Introduction P4 S1

- order：7

- locator：Introduction P4 S1

- paraphrase_cn：电力市场的技术进步正将其转化为智能市场，计算智能可支持人做出更明智决策。

- move_code：THEORY_INTRO

- statement_status：prior_literature

- why_here_cn：把问题从电力工程转译为IS的智能市场研究议程。

- inherits_from_previous_cn：承接雪崩现象，说明技术化解决路径属于IS。

- changes_argument_state_cn：引入文献坐标：smart markets。

- sets_up_next_cn：下一句把智能市场议程收缩为本文‘定价协调EV’的目标。

- failure_if_removed_cn：方案缺少IS理论身份。

- evidence_pointer：Introduction P4 S1

### 8. Introduction P4 S2-S3

- order：8

- locator：Introduction P4 S2-S3

- paraphrase_cn：回应IS文献呼吁，引入IS赋能的定价方案以协调EV充电，最小化电网压力并最好地利用可再生；该方案只要求单向价格参数通信，不限制期望需求曲线形状。

- move_code：RQ_OR_OBJECTIVE

- statement_status：author_inference

- why_here_cn：把一般智能市场议程定向到本文具体目标，并预告两个关键设计属性：单向通信、任意形状需求曲线。

- inherits_from_previous_cn：依赖‘smart markets’理论坐标和雪崩问题。

- changes_argument_state_cn：从‘可以做什么’转到‘本论文要做什么’。

- sets_up_next_cn：接下来首次说明核心设计。

- failure_if_removed_cn：读者不知研究目标，后文设计显得突兀。

- evidence_pointer：Introduction P4 S2-S3

### 9. Introduction P4 S4-S5

- order：9

- locator：Introduction P4 S4-S5

- paraphrase_cn：特别地，提出kWh价格包含一个随充电速率/kW变化的成分；因充电速率决定占用的电网容量，称之为容量定价CBP。

- move_code：DESIGN_FEATURE

- statement_status：design_decision

- why_here_cn：首次呈现核心发明及其物理/工程依据，是全文机制支点。

- inherits_from_previous_cn：‘In particular’承接前句的定价方案预告。

- changes_argument_state_cn：给出可操作的设计公式方向：价格与充电速率相关。

- sets_up_next_cn：需要说明为何该设计能分散雪崩响应并诱导期望曲线，为Section 3-4铺路。

- failure_if_removed_cn：论文核心发明缺失。

- evidence_pointer：Introduction P4 S4-S5

### 10. Introduction P4 S6

- order：10

- locator：Introduction P4 S6

- paraphrase_cn：将CBP与智能电力市场可用信息结合，提出基于解析和计算启发式的价格设定方法，满足利益相关者目标，优于确立的基准，并以低计算复杂度诱导近最优结果。

- move_code：DESIGN_FEATURE_AND_CONTRIBUTION_PREVIEW

- statement_status：contribution_claim

- why_here_cn：把设计从价格公式扩展到价格设定方法，预告本文的AH/CH与基准比较。

- inherits_from_previous_cn：依赖前句的CBP公式。

- changes_argument_state_cn：建立制品完整结构：定价公式+价格设定方法+评价。

- sets_up_next_cn：为设计科学定位和评价方式（Gregor & Hevner）做铺垫。

- failure_if_removed_cn：制品只剩公式而无可用方法，贡献不完整。

- evidence_pointer：Introduction P4 S6

### 11. Introduction P4 S7-S8

- order：11

- locator：Introduction P4 S7-S8

- paraphrase_cn：从设计科学角度看，本研究属于Gregor & Hevner的'Improvement'类：为已知问题开发新解决方案，克服雪崩效应等现有局限，并用真实数据校准的仿真、按领域相关指标进行评估。

- move_code：METHOD_JUSTIFICATION

- statement_status：method_decision

- why_here_cn：提前为读者设定评价标准：这是设计科学中的改进类，因此仿真基准比较是合适证据。

- inherits_from_previous_cn：承接制品结构与贡献预告。

- changes_argument_state_cn：把评价方式与学科规范绑定，管理预期。

- sets_up_next_cn：为Section 6-7的仿真testbed和指标作伏笔。

- failure_if_removed_cn：读者可能用现场实证标准要求本文，造成误读。

- evidence_pointer：Introduction P4 S7-S8

### 12. Introduction P5 S1-S4

- order：12

- locator：Introduction P5 S1-S4

- paraphrase_cn：方案给利益相关者带来多重好处：电网运营者可降低峰值并保持连续运行；政策制定者可塑造需求匹配可再生使投资更经济；进而促进EV普及并减少额外电网容量需求。

- move_code：PRACTICAL_STAKES

- statement_status：contribution_claim

- why_here_cn：把技术设计转译为利益相关者收益，满足IS论文的实用价值要求。

- inherits_from_previous_cn：依赖前文制品与目标。

- changes_argument_state_cn：从‘方案是什么’转成‘方案对谁有什么价值’。

- sets_up_next_cn：为Green IS贡献定位铺垫。

- failure_if_removed_cn：贡献停留在算法层面，缺乏科学共同体关心的社会价值。

- evidence_pointer：Introduction P5

### 13. Introduction P6 S1-S4

- order：13

- locator：Introduction P6 S1-S4

- paraphrase_cn：本文贡献除smart markets与smart cities文献外，还属于Green IS；按Green IS原则，IS可带来更高效能源消耗，本文将设计一个受益于可用信息、以最小干预和低计算复杂度诱导更有利于电网的EV充电行为的制品。

- move_code：CONTRIBUTION_POSITIONING

- statement_status：contribution_claim

- why_here_cn：把贡献正式锚定在Green IS，使后文Watson框架图1有依托。

- inherits_from_previous_cn：承接前段的利益相关者收益。

- changes_argument_state_cn：宣告本文的学科贡献目标：Green IS中的可持续EV协调。

- sets_up_next_cn：为图1的Green IS框架说明做铺垫。

- failure_if_removed_cn：IS贡献定位缺失，论文会像电力工程或运筹文章。

- evidence_pointer：Introduction P6

### 14. Introduction P6 S5-S6（图1后）

- order：14

- locator：Introduction P6 S5-S6（图1后）

- paraphrase_cn：遵循并改编Watson等人Green IS框架：在供需两侧各有一个IS元素——供应侧为解析/计算价格设定启发式，消费侧为智能agent的存在与能力。

- move_code：THEORY_FRAMEWORK_ALTERATION

- statement_status：theory_claim

- why_here_cn：用图1把本文的三层制品（定价机制、启发式、agent）放进一个已有Green IS理论框架，显示理论贡献。

- inherits_from_previous_cn：依赖Green IS定位。

- changes_argument_state_cn：建立从理论框架到设计元素的映射。

- sets_up_next_cn：为Section 2.1正式展开Green IS背景。

- failure_if_removed_cn：设计元素缺少理论嵌入，理论贡献不成立。

- evidence_pointer：Introduction P6 S5-S6与Figure 1

### 15. Introduction→Section 2 过渡（P6末）

- order：15

- locator：Introduction→Section 2 过渡（P6末）

- paraphrase_cn：图1总结除核心CBP外还有两个关键IS元素：供给侧启发式实现近最优低复杂度，消费侧agent保证消费者目标被满足。

- move_code：CLOSING_AND_SIGNPOSTING

- statement_status：author_inference

- why_here_cn：段末重申三层结构，为理论背景和后续技术部分设置路标。

- inherits_from_previous_cn：依赖图1框架。

- changes_argument_state_cn：完成引言的‘框架-设计-元素’闭环，准备进入背景综述。

- sets_up_next_cn：为Section 2的文献梳理提供结构。

- failure_if_removed_cn：引言结束缺少对后文结构的预告，读者迷失。

- evidence_pointer：Introduction P6末句

## 引言逐段图谱

### 1. Introduction P1

- locator：Introduction P1

- opening_move_cn：把研究放在智能城市、数据、碳减排与EV增长的大背景。

- development_move_cn：用巴黎宣言和全球EV增长数据建立紧迫性。

- pivot_move_cn：最后一口气从EV普及转向电网稳定性挑战，并明确指出IS可应对。

- closing_move_cn：为第二段的具体电网问题制造需要。

- paragraph_job_cn：确立宏观问题舞台和IS介入权限。

### 2. Introduction P2

- locator：Introduction P2

- opening_move_cn：说明电网不是为EV负荷设计的。

- development_move_cn：加入EV充电器作为家庭最高功率负荷、运行时间长的机制细节。

- pivot_move_cn：从‘为什么是问题’转到‘传统应对只有扩容或远程关断’，并否定扩容的可持续性。

- closing_move_cn：排除物理扩容路线，为需求侧方案制造需要。

- paragraph_job_cn：把宏观风险转化为物理机制并封死传统解法。

### 3. Introduction P3

- locator：Introduction P3

- opening_move_cn：直接声称现有协调方案有根源于激励不对齐的短板。

- development_move_cn：定义雪崩效应并引文献和试点确认其真实存在。

- pivot_move_cn：无强烈转折，从定义滑到经验确认。

- closing_move_cn：以‘雪崩会加剧峰值’收尾，为‘必须设计新机制’制造需要。

- paragraph_job_cn：定义并确证本文要解决的‘现象’：激励不对齐与雪崩效应。

### 4. Introduction P4

- locator：Introduction P4

- opening_move_cn：从电力市场技术演进引出智能市场概念。

- development_move_cn：把IS文献呼吁转化为本文目标，再预告单向通信与任意曲线两个属性，随后呈现CBP公式及其物理依据。

- pivot_move_cn：从‘可以做什么’转到‘本文做什么’再到‘具体设计是什么’。

- closing_move_cn：用设计科学与评价方式声明结束本段，预告后文。

- paragraph_job_cn：把问题转化为一个具体制品（CBP）与一套评价承诺。

### 5. Introduction P5

- locator：Introduction P5

- opening_move_cn：用‘方案给利益相关者带来多种好处’直接开启价值转译。

- development_move_cn：分别列出电网运营者、政策制定者两类受益者及其收益。

- pivot_move_cn：从直接利益相关者转向社会可持续的两个途径（促进EV采用、减少电网扩容）。

- closing_move_cn：以减排和减少额外容量收尾，为Green IS定位铺垫。

- paragraph_job_cn：把制品的技术属性转译成社会与利益相关者价值。

### 6. Introduction P6

- locator：Introduction P6

- opening_move_cn：明确贡献命名：智能市场文献加Green IS。

- development_move_cn：引Green IS原理并重述本文艺术（最小干预、低计算复杂度）。

- pivot_move_cn：引入Watson等Green IS框架并通过图1把供需两侧的IS元素纳入。

- closing_move_cn：总结三层结构，为进入背景综述和后续技术部分设置路标。

- paragraph_job_cn：把贡献正式锚定在Green IS框架，并给出全文结构图。

## 理论到设计逐句图谱

### 1. Section 2.1 P1

- order：1

- locator：Section 2.1 P1

- paraphrase_cn：Green IS是研究IS在改善环境可持续中角色的子领域，共同目标是用IT改善可持续或建立可持续核心原则。

- move_code：THEORY_ANCHOR

- statement_status：prior_literature

- why_here_cn：背景2.1开头为全文理论归属建立定义。

- inherits_from_previous_cn：承接引言Green IS定位。

- changes_argument_state_cn：把贡献归属具体化为一个子领域的定义。

- sets_up_next_cn：为下一句‘本文回应Ketter et al.研究机会’提供坐标。

- failure_if_removed_cn：Green IS理论背景缺失，贡献无出处。

- evidence_pointer：Section 2.1 P1

### 2. Section 2.1 P2-P3

- order：2

- locator：Section 2.1 P2-P3

- paraphrase_cn：本文回应Ketter等关于智能可持续出行制品的研究呼吁，具体回答‘如何设计有效的移动需求响应干预以系统有利方式引导用户行为（如时间转移）’的问题。

- move_code：RESEARCH_QUESTION_ALIGNMENT

- statement_status：prior_literature

- why_here_cn：把本文CBP直接放进一个近期IS研究议程的具体研究问题中，说明论文是议程的一部分。

- inherits_from_previous_cn：依赖Green IS定义与Ketter等框架。

- changes_argument_state_cn：从‘属于Green IS’升级为‘回答特定开放问题’。

- sets_up_next_cn：后文文献将围绕该问题展开。

- failure_if_removed_cn：本文与IS议程的连接变弱，读者难以判断贡献相关性。

- evidence_pointer：Section 2.1 P2-P3

### 3. Section 2.1 P4-P5

- order：3

- locator：Section 2.1 P4-P5

- paraphrase_cn：Green IS中已有EV与可再生协同框架、EV电池再利用DSS等邻近工作。

- move_code：PRIOR_KNOWLEDGE

- statement_status：prior_literature

- why_here_cn：列举邻近Green IS制品，显示领域存在但未解决充电协调问题。

- inherits_from_previous_cn：承接Green IS定位。

- changes_argument_state_cn：建立‘Green IS有制品但缺口存在’的状态。

- sets_up_next_cn：为2.2节更聚焦的充电协调综述过渡。

- failure_if_removed_cn：领域基础不足，缺口表述悬空。

- evidence_pointer：Section 2.1 P4-P5

### 4. Section 2.2 P1-P2

- order：4

- locator：Section 2.2 P1-P2

- paraphrase_cn：EV充电协调可分为集中式（自上而下）和分散式（自下而上）；集中式有全局目标（如降峰值），并按目标函数与控制方式变化。

- move_code：TAXONOMY_INTRO

- statement_status：prior_literature

- why_here_cn：建立分类框架，为后文批评两类机制做准备。

- inherits_from_previous_cn：承接2.1的过渡。

- changes_argument_state_cn：引入协调机制的两分类，界定本文的位置。

- sets_up_next_cn：分别评述集中式和分散式的优缺点。

- failure_if_removed_cn：后文对两类机制的评价无框架。

- evidence_pointer：Section 2.2 P1-P2

### 5. Section 2.2 P3-P4

- order：5

- locator：Section 2.2 P3-P4

- paraphrase_cn：集中式机制可分为防拥堵类与激励降峰类，又可包括拍卖机制和定价信号；主要优点是可满足电网约束，主要挑战包括外生控制充电器、侵犯偏好、需要通信控制基础设施。

- move_code：PRIOR_KNOWLEDGE_WITH_LIMITATION

- statement_status：prior_literature

- why_here_cn：在分类基础上评述集中式机制的特征与代价，为混合机制铺路。

- inherits_from_previous_cn：依赖分类框架。

- changes_argument_state_cn：指出集中式的主要局限。

- sets_up_next_cn：转向分散式的局限。

- failure_if_removed_cn：混合方案（本文的核心）缺一个对比面。

- evidence_pointer：Section 2.2 P3-P4

### 6. Section 2.2 P5

- order：6

- locator：Section 2.2 P5

- paraphrase_cn：分散式机制以个体为目标，尊重个体偏好，但不保证个体与电网全局目标一致；当所有顾客收到相同价格信号时，充电计划相关，成本最小化者会把需求转移到最低价时段，产生雪崩效应。

- move_code：LIMITATION_AND_MECHANISM

- statement_status：author_inference

- why_here_cn：这是全文机制核心：用‘相同价格信号→相关计划→雪崩’解释分散式的失败，并说明为何需要在价格里加入容量分量。

- inherits_from_previous_cn：承接分散式定义。

- changes_argument_state_cn：把‘不一致’具体化为’低成本时段拥堵‘的机制链。

- sets_up_next_cn：为2.3节文献分类和CBP设计制造直接理由。

- failure_if_removed_cn：CBP的容量项α·r失去要解决的问题。

- evidence_pointer：Section 2.2 P5

### 7. Section 2.2 P6

- order：7

- locator：Section 2.2 P6

- paraphrase_cn：已有通过区块链、中介控制、迭代智能充电等缓解雪崩效应的尝试，但这些方案计算更复杂或需要更多信息，难以快速适应现实环境。

- move_code：GAP

- statement_status：prior_literature

- why_here_cn：把已有缓解尝试统一评价为‘复杂或信息需求高’，为本文低复杂度混合方案制造对照。

- inherits_from_previous_cn：依赖雪崩机制的确认。

- changes_argument_state_cn：确立‘缓解尝试存在但仍有代价’的缺口。

- sets_up_next_cn：下一句给出本文混合方案的总主张。

- failure_if_removed_cn：解决方案的独特性无从比较。

- evidence_pointer：Section 2.2 P6

### 8. Section 2.2 P7

- order：8

- locator：Section 2.2 P7

- paraphrase_cn：本文方案结合理性自利EV车主侧的分散决策与意图诱导期望聚合剖面的中央协调方，不侵犯消费者偏好，能缓解雪崩效应，并因少迭代而快速适应现实变化。

- move_code：DESIGN_PROPOSITION

- statement_status：author_inference

- why_here_cn：在缺口之后正式给出本文的机制定位：混合中央-分散制。

- inherits_from_previous_cn：直接回应前句‘计算复杂/信息需求高’的批评。

- changes_argument_state_cn：本文方案第一次被完整定义为‘混合协调+低迭代’。

- sets_up_next_cn：为2.3节定价文献的三类缺口总结提供对比。

- failure_if_removed_cn：本文机制定位缺失，后文缺口总结无主句。

- evidence_pointer：Section 2.2 P7

### 9. Section 2.3 P1

- order：9

- locator：Section 2.3 P1

- paraphrase_cn：定价是协调EV充电最流行方法之一，本节概述不同定价机制，排除静态分时和flat定价，并指向Limmer综述。

- move_code：SCOPE_STATEMENT

- statement_status：method_decision

- why_here_cn：限定综述范围：只评述高级动态定价，为三类缺口铺路。

- inherits_from_previous_cn：承接2.2的定价信号讨论。

- changes_argument_state_cn：界定后文文献分类的边界。

- sets_up_next_cn：为三类文献分别展开。

- failure_if_removed_cn：综述范围不清。

- evidence_pointer：Section 2.3 P1

### 10. Section 2.3 P2-P4

- order：10

- locator：Section 2.3 P2-P4

- paraphrase_cn：第一类依赖迭代学习：如Alizadeh等的拥堵系数、强化学习/GA调价、MDP策略等，通常需20-100天或大量计算资源，不允许即时决策。

- move_code：PRIOR_KNOWLEDGE_WITH_LIMITATION

- statement_status：prior_literature

- why_here_cn：用具体文献证明第一类缺口：迭代/学习成本。

- inherits_from_previous_cn：承接综述范围。

- changes_argument_state_cn：建立第一类文献及其共同限制。

- sets_up_next_cn：第二、三类文献继续累积限制。

- failure_if_removed_cn：三类缺口论证缺第一支柱。

- evidence_pointer：Section 2.3 P2-P4

### 11. Section 2.3 P5

- order：11

- locator：Section 2.3 P5

- paraphrase_cn：第二类假设车主价格响应或效用函数：如Soltani等弹性调整、Lin等sigmoid弹性代理、Yoon/Dai等效用博弈、Zhang等满意度调整、Santoyo等不耐烦因素，但这些价格静态且依赖行为假设。

- move_code：PRIOR_KNOWLEDGE_WITH_LIMITATION

- statement_status：prior_literature

- why_here_cn：用具体文献建立第二类缺口：除成本最小化外还假设消费者响应特征。

- inherits_from_previous_cn：承接综述范围。

- changes_argument_state_cn：累积第二类文献及其限制。

- sets_up_next_cn：第三类文献继续。

- failure_if_removed_cn：缺口论证缺第二支柱。

- evidence_pointer：Section 2.3 P5

### 12. Section 2.3 P6-P7

- order：12

- locator：Section 2.3 P6-P7

- paraphrase_cn：第三类涉及不同定价结构：多档实时定价、拥堵分量游戏理论、迭代定价、填谷机制、locational marginal pricing等，但它们大多只诱导平坦剖面或需要迭代，不能诱导任意形状。

- move_code：PRIOR_KNOWLEDGE_WITH_LIMITATION

- statement_status：prior_literature

- why_here_cn：建立第三类缺口：剖面形状受限。

- inherits_from_previous_cn：承接综述范围。

- changes_argument_state_cn：完成三类文献限制的累积。

- sets_up_next_cn：下一句总结三类缺口。

- failure_if_removed_cn：缺口论证缺第三支柱。

- evidence_pointer：Section 2.3 P6-P7

### 13. Section 2.3 P8

- order：13

- locator：Section 2.3 P8

- paraphrase_cn：现有文献以三种方式限制问题：依赖大量迭代/学习、假设额外消费者行为、假设期望剖面平坦或高受限；本文用不同定价制品应对。

- move_code：GAP_SUMMARY

- statement_status：author_inference

- why_here_cn：这是全文文献缺口的正式总结句系列，是贡献主张的基准。

- inherits_from_previous_cn：直接概括前三段。

- changes_argument_state_cn：把三股文献批评压缩为三个可对照的设计约束。

- sets_up_next_cn：紧接着预告本文制品如何逐一突破。

- failure_if_removed_cn：贡献清单失去靶子。

- evidence_pointer：Section 2.3 P8

### 14. Section 2.3 P9-P10

- order：14

- locator：Section 2.3 P9-P10

- paraphrase_cn：本文容量定价建立于早期非线性定价思想（Schweppe等，Gottwalt），并系统研究其理论性质与价格设定机制；具体贡献为解析启发式、计算启发式、内置收入平衡和广泛评价。

- move_code：DESIGN_POSITIONING

- statement_status：author_inference

- why_here_cn：在缺口总结后立即给制品定位，使设计不是‘没人做过’而是‘针对三大约束有意设计’。

- inherits_from_previous_cn：依赖三类缺口总结。

- changes_argument_state_cn：从‘文献缺什么’转为‘本文补什么’。

- sets_up_next_cn：为Section 3-5的制品展开设置路线图。

- failure_if_removed_cn：本文制品与文献缺口的对应关系不清。

- evidence_pointer：Section 2.3 P9-P10

### 15. Section 3 P1-P2

- order：15

- locator：Section 3 P1-P2

- paraphrase_cn：假设智能电网运营者想把现有负荷重塑为期望剖面（如平坦或可再生模式），即负载平衡问题；参与者包括电网运营者和EV车主。

- move_code：PROBLEM_FORMALIZATION

- statement_status：author_inference

- why_here_cn：正式把问题格式化为负载平衡，并界定两个参与方。

- inherits_from_previous_cn：依赖Section 2.3缺口的解决方案方向。

- changes_argument_state_cn：从文献综述转入正式建模。

- sets_up_next_cn：为3.1-3.3的信息边界、价格公式、agent模型展开。

- failure_if_removed_cn：后文数学与agent模型无问题框架。

- evidence_pointer：Section 3 P1-P2

### 16. Section 3.1 P1

- order：16

- locator：Section 3.1 P1

- paraphrase_cn：网格运营者广播未来horizon T的价格信号，目标为期望剖面D，T被离散为间隔δ。

- move_code：MODEL_SETUP

- statement_status：design_decision

- why_here_cn：定义时间horizon和价格广播机制，为后续定理和仿真建立统一时钟。

- inherits_from_previous_cn：承接问题框架。

- changes_argument_state_cn：设定模型的时间结构与控制系统。

- sets_up_next_cn：为信息边界和价格公式铺路。

- failure_if_removed_cn：所有定理和仿真的时间设定失去基础。

- evidence_pointer：Section 3.1 P1

### 17. Section 3.1 P2-P3

- order：17

- locator：Section 3.1 P2-P3

- paraphrase_cn：网格运营者只能观察聚合需求D0和总充电需求Φ，不能访问个体偏好；其目标是把Φ重塑为保持总能量不变的期望剖面D。

- move_code：INFORMATION_BOUNDARY

- statement_status：design_decision

- why_here_cn：界定不完全信息约束，这是本文所有启发式的存在理由。

- inherits_from_previous_cn：依赖时间模型。

- changes_argument_state_cn：确立信息边界：只能看聚合，不看个体。

- sets_up_next_cn：为3.2的价格公式和3.4的启发式必要性做基础。

- failure_if_removed_cn：无法解释为什么需要AH/CH。

- evidence_pointer：Section 3.1 P2-P3

### 18. Section 3.2 P1-P2（公式1）

- order：18

- locator：Section 3.2 P1-P2（公式1）

- paraphrase_cn：广播价格统一但可随时间变化并依赖消费者选择的充电速率，即P_t(r)=P0,t+αt·r；P0,t外生，可为批发价或常数。

- move_code：DESIGN_FORMULA

- statement_status：design_decision

- why_here_cn：给出全文核心设计公式，定义价格的两个成分。

- inherits_from_previous_cn：承接信息边界与目标表述。

- changes_argument_state_cn：把设计思想转化为可分析的数学形式。

- sets_up_next_cn：下一句解释容量分量为何合理。

- failure_if_removed_cn：所有定理引用公式(1)将落空。

- evidence_pointer：Section 3.2公式(1)

### 19. Section 3.2 P3

- order：19

- locator：Section 3.2 P3

- paraphrase_cn：充电速率决定所需电网容量，因此把容量成本通过α·r转移到高速率用户；用更高速率充电的EV支付更高单位电价。

- move_code：MECHANISM_RATIONALE

- statement_status：author_inference

- why_here_cn：解释为什么价格要与充电速率挂钩，这是CBP的物理与经济学依据。

- inherits_from_previous_cn：依赖公式(1)。

- changes_argument_state_cn：把公式与电网容量占用这一事实连接。

- sets_up_next_cn：为定理1中速率与α反比的结果提供直觉。

- failure_if_removed_cn：设计显得武断，无机制理由。

- evidence_pointer：Section 3.2 P3

### 20. Section 3.2 P4-P5

- order：20

- locator：Section 3.2 P4-P5

- paraphrase_cn：αt是价格曲线关于速率的斜率，被定义为控制agent的决策变量；目标是选择向量α以诱导期望聚合充电剖面。

- move_code：CONTROL_VARIABLE_DEFINITION

- statement_status：design_decision

- why_here_cn：把α从公式参数提升为设计中的控制变量，为第4节推导最优α条件设定对象。

- inherits_from_previous_cn：依赖公式(1)与容量机制。

- changes_argument_state_cn：定价问题被转成‘选α向量’的优化问题。

- sets_up_next_cn：引出4.1/4.2的最优α条件。

- failure_if_removed_cn：后文定理与仿真没有控制对象。

- evidence_pointer：Section 3.2 P4-P5

### 21. Section 3.3 P1-P3

- order：21

- locator：Section 3.3 P1-P3

- paraphrase_cn：定义EV agent i的偏好θi={Δi,Φi,βi,Ei}，包括驾驶截止时间、需求能量、充电可用性向量和驾驶耗能向量。

- move_code：AGENT_MODEL_SETUP

- statement_status：design_decision

- why_here_cn：正式定义agent偏好结构，为仿真和定理建立统一模型。

- inherits_from_previous_cn：承接价格广播设定。

- changes_argument_state_cn：引入agent行为模型，为计算agent最优充电率打基础。

- sets_up_next_cn：为成本最小化问题公式(2)-(6)展开。

- failure_if_removed_cn：agent模型与仿真无法初始化。

- evidence_pointer：Section 3.3 P1-P3

### 22. Section 3.3 P4-P7（公式2-6）

- order：22

- locator：Section 3.3 P4-P7（公式2-6）

- paraphrase_cn：每个agent的目标是最小化总成本，受两个约束：充电速率上下限与每个截止时间前的最低电池能量约束。

- move_code：OPTIMIZATION_PROBLEM

- statement_status：theory_claim

- why_here_cn：把agent决策形式化为一个有约束优化问题，供定理1与仿真求解器使用。

- inherits_from_previous_cn：依赖偏好结构与价格公式。

- changes_argument_state_cn：agent决策被定义为可计算的最小化问题。

- sets_up_next_cn：3.4将指出这类优化对电网不可行，引出启发式。

- failure_if_removed_cn：定理与仿真无共同问题表达式。

- evidence_pointer：Section 3.3公式(2)-(6)

### 23. Section 3.4 P1

- order：23

- locator：Section 3.4 P1

- paraphrase_cn：理想情况下个体偏好可知最优定价，但信息可用性和计算可操作性构成两个关键障碍；网格管理者面临不完全信息问题，且大规模精确优化不可行。

- move_code：MOTIVATION_FOR_HEURISTICS

- statement_status：author_inference

- why_here_cn：明确指出为什么不能做个体级精准优化，为AH/CH的合法性铺垫。

- inherits_from_previous_cn：依赖3.3的agent复杂度。

- changes_argument_state_cn：确立‘必须用启发式’的前提。

- sets_up_next_cn：引出Sections 4-5的AH与CH设计。

- failure_if_removed_cn：启发式方法没有存在理由。

- evidence_pointer：Section 3.4 P1

### 24. Section 3.4 P2-P3

- order：24

- locator：Section 3.4 P2-P3

- paraphrase_cn：说明网格运营者可观察的信息（agent数、聚合需求、总能量）及标准行为假设（理性、早充偏好）；并称将在异质随机环境下与既有方法比较以建立有效性。

- move_code：SCOPE_AND_METHOD_PREVIEW

- statement_status：method_decision

- why_here_cn：界定启发式的信息输入和评价方式，为后文方法部分提供明确的premise。

- inherits_from_previous_cn：依赖‘必须用启发式’的论证。

- changes_argument_state_cn：从‘为什么需要启发式’转向‘用什么信息、如何评价’。

- sets_up_next_cn：为第4-7节的技术展开和仿真评价设置前提。

- failure_if_removed_cn：评价标准不清，后文仿真缺少对照框架。

- evidence_pointer：Section 3.4 P2-P3

### 25. Section 4 P1-P3

- order：25

- locator：Section 4 P1-P3

- paraphrase_cn：在没有充电可用性约束的情况下，最优定价任务可直接解析处理；理论性质直接导致可诱导期望剖面的解析启发式，因此在无约束情形最优，并自然适合约束不可观察的情形；本节只聚焦P0恒定特殊情形，一般情形见附录C/D。

- move_code：SECTION_PROPOSITION

- statement_status：theory_claim

- why_here_cn：建立第4节的理论地位：用理想无约束情形推出解析解，再把该解作为真实情境的启发式。

- inherits_from_previous_cn：依赖3.4中启发式必要性的论证。

- changes_argument_state_cn：从‘需要启发式’转向‘可以从解析解构造启发式’。

- sets_up_next_cn：为定理1-4铺路。

- failure_if_removed_cn：定理1-4缺少定位，读者不知这些定理在论证中的角色。

- evidence_pointer：Section 4 P1-P3

### 26. Section 4.1 Theorem 1

- order：26

- locator：Section 4.1 Theorem 1

- paraphrase_cn：定理1：理性无约束agent的最优充电率与αt成反比，具体为φi/[αt·δ·(1/α1+…+1/αT)]。

- move_code：THEORY_PROPOSITION_RESPONSE

- statement_status：theory_claim

- why_here_cn：提供agent对CBP的解析最优响应，是后续所有诱导与收入结果的机制根基。

- inherits_from_previous_cn：依赖公式(1)与agent优化模型。

- changes_argument_state_cn：把‘价格影响充电率’形式化为‘速率与α反比’。

- sets_up_next_cn：为图5-6的直观解释和4.2的α条件铺垫。

- failure_if_removed_cn：其后机制论证全部断裂。

- evidence_pointer：Theorem 1

### 27. Section 4.1 图5-6后

- order：27

- locator：Section 4.1 图5-6后

- paraphrase_cn：最优充电率依赖αt，因此网格运营者可通过调整αt改变需求形状；下一小节将推导诱导期望剖面的最优α。

- move_code：MECHANISM_TO_CONTROL

- statement_status：theory_claim

- why_here_cn：把定理1从‘agent响应’转成‘网格控制杆’，为4.2做过渡。

- inherits_from_previous_cn：依赖定理1与图5-6。

- changes_argument_state_cn：把αt确立为诱导需求的控制变量。

- sets_up_next_cn：为定理2的条件推导直接铺路。

- failure_if_removed_cn：定理2的目的不清。

- evidence_pointer：Figure 5-6附近的讨论

### 28. Section 4.2 Theorem 2

- order：28

- locator：Section 4.2 Theorem 2

- paraphrase_cn：定理2：在异质理性无约束agent群体中诱导期望剖面D的条件是αt·Dt/δ对所有t相等；该条件不需要个体需求信息；可用单参数F参数化D-inducing alpha族。

- move_code：THEORY_PROPOSITION_INDUCING

- statement_status：theory_claim

- why_here_cn：给出核心可执行条件，并强调不需要个体信息，直接回应用户背景2.3第二类缺口。

- inherits_from_previous_cn：依赖定理1的最优响应。

- changes_argument_state_cn：把目标‘诱导D’转化为对α的简单条件。

- sets_up_next_cn：为定理3/4的收入条件和CH的初始值选择提供基础。

- failure_if_removed_cn：CH的初始化与D=w族论证失去根基。

- evidence_pointer：Theorem 2及其讨论

### 29. Section 4.3 Theorem 3

- order：29

- locator：Section 4.3 Theorem 3

- paraphrase_cn：定理3：要在诱导剖面D的同时生成目标收入Ψ*，αz应按δ(Ψ*-P0Φ)/[Dz·Φ·Σ(εi)²]设定；需要个体需求份额εi的精确或粗略估计。

- move_code：THEORY_PROPOSITION_REVENUE

- statement_status：theory_claim

- why_here_cn：把D-inducing族中的自由度F绑定到收入目标，为后文收入等价主张提供解析担保。

- inherits_from_previous_cn：依赖定理2的解族。

- changes_argument_state_cn：定价问题从‘只诱导曲线’扩展为‘同时满足收入’。

- sets_up_next_cn：为附录推论A.5/A.6（minimal/distributional信息）和CH Step1的初始化做基础。

- failure_if_removed_cn：收入目标能力无理论支撑。

- evidence_pointer：Theorem 3

### 30. Section 4.3 定理3后讨论

- order：30

- locator：Section 4.3 定理3后讨论

- paraphrase_cn：定理3只有精确知εi才保证精确收入；缺少信息时可用人口平均或分布估计达到近似目标（推论A.5/A.6）。

- move_code：INFORMATION_VARIANT_DISCUSSION

- statement_status：author_inference

- why_here_cn：处理信息现实性，使理论从‘完全信息’退到‘可用信息’并服务CH配置。

- inherits_from_previous_cn：依赖定理3。

- changes_argument_state_cn：建立信息变体：minimal vs distributional。

- sets_up_next_cn：为第6.5节2x2配置表提供理论基础。

- failure_if_removed_cn：CBP-AH vs CBP-AH-Distrib的区分失去依据。

- evidence_pointer：Section 4.3定理3后讨论

### 31. Section 4.3 定理3后第二讨论段

- order：31

- locator：Section 4.3 定理3后第二讨论段

- paraphrase_cn：由于个体私人约束，期望剖面D可能无法实现，观测剖面D0不同会导致不同收入；但CBP的优点是可依据观测到的D0在同一D-inducing族内调整α以逼近目标收入。

- move_code：MECHANISM_FOR_CONSTRAINED_CASE

- statement_status：theory_claim

- why_here_cn：建立从无约束理论到有约束现实的桥梁，为定理4和CH Step2b铺垫。

- inherits_from_previous_cn：依赖定理2族与收入讨论。

- changes_argument_state_cn：指出在带私人约束时不放弃收入目标，可以在族内调整。

- sets_up_next_cn：直接引出定理4。

- failure_if_removed_cn：CH Step2b/2c对收入调整的理论基础缺失。

- evidence_pointer：Section 4.3定理3后第二讨论段

### 32. Section 4.3 Theorem 4

- order：32

- locator：Section 4.3 Theorem 4

- paraphrase_cn：定理4：在观测剖面D0偏离期望D时，网格运营者可从同一D-inducing族调整α'，按给定公式生成目标收入Ψ*；同样需要εi的精确或近似信息。

- move_code：THEORY_PROPOSITION_ADJUSTMENT

- statement_status：theory_claim

- why_here_cn：把收入保证扩展到有私有约束的现实情形，是CH数据驱动调整的理论依据。

- inherits_from_previous_cn：依赖定理3和前一段的调整直觉。

- changes_argument_state_cn：确立‘即使曲线被约束干扰，收入仍可调整’。

- sets_up_next_cn：为第5节CH Step2b/2c提供理论背书。

- failure_if_removed_cn：CH的收入调整无原理支持。

- evidence_pointer：Theorem 4

### 33. Section 5 P1

- order：33

- locator：Section 5 P1

- paraphrase_cn：对更复杂、有聚合可用性约束信息的情形，提出计算启发式：先用解析启发式初始化，再通过观察聚合充电行为调整价格参数，无需大量迭代与计算。

- move_code：SECTION_OPENING_DESIGN

- statement_status：design_decision

- why_here_cn：把第4节理论结果转向第5节实际算法，完成从理论到设计的耦合。

- inherits_from_previous_cn：依赖定理2-4和3.4的启发式必要性。

- changes_argument_state_cn：从‘理想情形可解析’转向‘现实情形可计算调整’。

- sets_up_next_cn：为Step1/2a/2b/2c的算法细节展开。

- failure_if_removed_cn：从理论到实际算法的桥梁断裂。

- evidence_pointer：Section 5 P1

### 34. Section 5 Step 1

- order：34

- locator：Section 5 Step 1

- paraphrase_cn：Step1：用AH和定理3推论（A.5或A.6）按目标收入选择初始α0。

- move_code：ALGORITHM_INITIALIZATION

- statement_status：design_decision

- why_here_cn：确保CH起点在无约束情形已最优，为后续数据驱动调整提供参照。

- inherits_from_previous_cn：依赖定理3/4推论。

- changes_argument_state_cn：把解析理论嵌入算法的唯一初值入口。

- sets_up_next_cn：为Step2观察和调整建立基础。

- failure_if_removed_cn：CH起点无理论保证，调整没有基准。

- evidence_pointer：Section 5 Step 1

### 35. Section 5 Step 2a

- order：35

- locator：Section 5 Step 2a

- paraphrase_cn：Step2a：用观测需求偏差w=D0/D调整α1=α0·w，使曲线逼近期望；α1属于D=w诱导族，继承解析性质。

- move_code：ALGORITHM_DATA_ADJUSTMENT

- statement_status：design_decision

- why_here_cn：第一次数据驱动调整，用可观察聚合偏差修正私人约束带来的偏离。

- inherits_from_previous_cn：依赖定理1-2的反比性质和D-inducing族。

- changes_argument_state_cn：把理论族扩展到带约束情形；建立D=w族。

- sets_up_next_cn：为Step2b/2c的收入调整提供当前α1和观测收入。

- failure_if_removed_cn：CH无法修正曲线偏离。

- evidence_pointer：Section 5 Step 2a

### 36. Section 5 Step 2b

- order：36

- locator：Section 5 Step 2b

- paraphrase_cn：Step2b：在D=w族中用定理4推论（A.7或A.8）选择α2，以调整收入从Ψ1向Ψ*靠近，同时保持D′曲线。

- move_code：ALGORITHM_REVENUE_ADJUSTMENT

- statement_status：design_decision

- why_here_cn：第二次调整针对收入，保持曲线不变，使两个目标可分离处理。

- inherits_from_previous_cn：依赖D=w族与定理4。

- changes_argument_state_cn：收入目标被纳入数据驱动框架。

- sets_up_next_cn：为Step2c的线性外推补充更精细调整。

- failure_if_removed_cn：收入目标在带约束时只能靠运气。

- evidence_pointer：Section 5 Step 2b

### 37. Section 5 Step 2c

- order：37

- locator：Section 5 Step 2c

- paraphrase_cn：Step2c：用(Ψ1,Fin)与(Ψ2,Fadj)拟合F=f(Ψ)线性函数，外推F*=f(Ψ*)，再从D=w族选α*。

- move_code：ALGORITHM_LEARNING_STEP

- statement_status：design_decision

- why_here_cn：用两个观测点线性外推目标收入对应的自由度参数，使CH不依赖大量迭代。

- inherits_from_previous_cn：依赖Step2a/2b产生的观测点。

- changes_argument_state_cn：在带约束环境下实现低复杂度收入匹配。

- sets_up_next_cn：结束算法，为仿真评估提供完整配置。

- failure_if_removed_cn：CH在收入上可能停在近似值。

- evidence_pointer：Section 5 Step 2c

### 38. Section 6 P1

- order：38

- locator：Section 6 P1

- paraphrase_cn：为评价制品，构建由理性EV agent与智能电网管理agent组成的多agent仿真，agent建模基于真实驾驶行为数据。

- move_code：METHOD_ANCHOR

- statement_status：method_decision

- why_here_cn：把评价方式从单一算法示例升级为可复现、数据校准的仿真testbed。

- inherits_from_previous_cn：依赖Section 3.3的agent模型与4-5节的启发式。

- changes_argument_state_cn：评价阶段开始，引入Power TAC范式。

- sets_up_next_cn：为6.1-6.5的仿真步骤、指标、数据、基准和配置展开。

- failure_if_removed_cn：对AH/CH的评价没有统一环境。

- evidence_pointer：Section 6 P1

### 39. Section 6.1 P1（Steps 1-6）

- order：39

- locator：Section 6.1 P1（Steps 1-6）

- paraphrase_cn：仿真由六步组成：输入EV数与总能量、决定期望剖面和收入目标、用AH/CH计算α、每个agent求解最优充电计划、观察聚合需求与收入、按指标评估并在CH中需要时回到Step3调整。

- move_code：SIMULATION_PROTOCOL

- statement_status：method_decision

- why_here_cn：把评价流程标准化，使后续三个场景都使用同一协议，结果可比。

- inherits_from_previous_cn：依赖Section 6引言。

- changes_argument_state_cn：评价环境的具体操作流程被定义。

- sets_up_next_cn：为6.2指标、6.3数据、6.4基准与6.5配置提供流程框架。

- failure_if_removed_cn：场景结果无从复现与比较。

- evidence_pointer：Section 6.1 Steps 1-6

### 40. Section 6.2 P1-P3

- order：40

- locator：Section 6.2 P1-P3

- paraphrase_cn：使用RMSE度量实际与期望曲线的距离；在期望平坦时用绝对峰值和PAPR度量波动与峰值强度。

- move_code：METRIC_DEFINITION

- statement_status：method_decision

- why_here_cn：定义成功标准并说明领域指标何时适用，防止误用。

- inherits_from_previous_cn：依赖仿真协议。

- changes_argument_state_cn：建立可量化的评价尺度。

- sets_up_next_cn：为Tables 2-5的结果报告提供指标框架。

- failure_if_removed_cn：结果表没有统一指标，无法比较。

- evidence_pointer：Section 6.2

### 41. Section 6.3 P1-P4

- order：41

- locator：Section 6.3 P1-P4

- paraphrase_cn：用荷兰CBS出行统计校准agent偏好、EPEX批发价加税费校准P0、荷兰家庭负荷校准期望剖面、威斯康星PV数据校准可再生场景。

- move_code：REAL_DATA_CALIBRATION

- statement_status：method_decision

- why_here_cn：真实数据校准使仿真结果具有外部有效性，支撑‘不是玩具例子’的主张。

- inherits_from_previous_cn：依赖仿真协议与指标。

- changes_argument_state_cn：评价从概念仿真升级为真实数据仿真。

- sets_up_next_cn：为7.1-7.3的场景结果提供数据基础。

- failure_if_removed_cn：外部有效性主张失去基础。

- evidence_pointer：Section 6.3

### 42. Section 6.4 P1-P3

- order：42

- locator：Section 6.4 P1-P3

- paraphrase_cn：三个基准分别为：真实世界flat定价充电数据、无容量分量的时变价格（按残余容量反向定价）、递增阶梯定价（按Borenstein并适配期望剖面）。

- move_code：BENCHMARK_DESIGN

- statement_status：method_decision

- why_here_cn：用递进基准隔离容量定价的作用：现状、无容量分量版本、最强非线性限价方案。

- inherits_from_previous_cn：依赖指标定义与仿真协议。

- changes_argument_state_cn：建立评价参照系，使‘CBP优于基准’可以因果归因到容量分量。

- sets_up_next_cn：为7.1-7.3的比较结果提供对照项。

- failure_if_removed_cn：无法判断CBP优势来自容量项还是其他设计。

- evidence_pointer：Section 6.4

### 43. Section 6.5 P1-P4（Table 1）

- order：43

- locator：Section 6.5 P1-P4（Table 1）

- paraphrase_cn：按可用性假设（无约束AH vs 带约束CH）与个体需求信息版本（Minimal vs Distributional）生成2x2配置：CBP-AH、CBP-AH-Distrib、CBP-CH、CBP-CH-Distrib；分布信息只影响收入表现。

- move_code：CONFIGURATION_DESIGN

- statement_status：method_decision

- why_here_cn：明确评价对象的四个实例，并提前说明-Distrib只改收入不改曲线性能，管理结果报告粒度。

- inherits_from_previous_cn：依赖4-5节AH/CH与推论A.5-A.8。

- changes_argument_state_cn：把‘本文方法’具体化为四个可测配置。

- sets_up_next_cn：为7.1-7.3的结果表和标签做准备。

- failure_if_removed_cn：结果报告无法区分信息版本与启发式版本。

- evidence_pointer：Table 1与Section 6.5

## 制品设计理由逐句图谱

### 1. Section 3.2 P3

- order：1

- locator：Section 3.2 P3

- paraphrase_cn：充电速率决定所需电网容量，因此将容量成本内化到电价中，高速率用户支付更高单位价格。

- move_code：DESIGN_RATIONALE_PHYSICAL

- statement_status：design_decision

- why_here_cn：给CBP的‘为什么是速率相关价格’提供物理依据：速率=容量占用。

- inherits_from_previous_cn：承接公式(1)。

- changes_argument_state_cn：把价格公式与真实电网容量成本连接。

- sets_up_next_cn：为定理1反比关系提供经济直觉。

- failure_if_removed_cn：设计失去与电网现实的关联，读者无法理解为何用速率而非其他变量。

- evidence_pointer：Section 3.2 P3

### 2. Section 4.2 Theorem 2讨论

- order：2

- locator：Section 4.2 Theorem 2讨论

- paraphrase_cn：诱导条件αt·Dt/δ恒定不需要任何个体需求信息，且存在无限多个最优α（D-inducing族），可由单自由度F参数化。

- move_code：DESIGN_RATIONALE_INFORMATION

- statement_status：theory_claim

- why_here_cn：用定理说明CBP特别适合信息受限的电网运营者，直接区别于依赖行为假设的文献。

- inherits_from_previous_cn：依赖定理2。

- changes_argument_state_cn：把‘不需要个体信息’从直觉上升为定理保证。

- sets_up_next_cn：为定理3/4和CH的配置做基础。

- failure_if_removed_cn：CBP相对文献的信息优势无证据。

- evidence_pointer：Theorem 2讨论

### 3. Section 4.2 末段

- order：3

- locator：Section 4.2 末段

- paraphrase_cn：虽然同一价格方案广播给所有agent，但每个agent因各自充电需求不同实际支付不同价格。

- move_code：DESIGN_RATIONALE_FAIRNESS

- statement_status：theory_claim

- why_here_cn：回应潜在批评：统一广播是否会不公平；证明同一价格公式下因速率不同天然产生差异化支付。

- inherits_from_previous_cn：依赖定理2与εi定义。

- changes_argument_state_cn：消除‘统一价格=一刀切’的误解。

- sets_up_next_cn：为4.3收入定理提供个体贡献份额εi的概念。

- failure_if_removed_cn：读者可能质疑CBP的公平性与个体异质性处理。

- evidence_pointer：Section 4.2末段

### 4. Section 4.3 定理3前段

- order：4

- locator：Section 4.3 定理3前段

- paraphrase_cn：D-inducing族中有无限多的最优α向量，每个向量带来不同收入；因此需要给能源供应商保持市场收入或满足政府管制收入的自由。

- move_code：DESIGN_RATIONALE_REVENUE

- statement_status：author_inference

- why_here_cn：解释为什么要在诱导曲线之外设计收入目标能力：理论与实践都需要监管/市场约束。

- inherits_from_previous_cn：依赖定理2的族结构。

- changes_argument_state_cn：把定价问题从单一目标扩展为双目标（曲线+收入）。

- sets_up_next_cn：为定理3/4和CH收入步骤提供动机。

- failure_if_removed_cn：收入平衡能力显得多余。

- evidence_pointer：Section 4.3 开头段

### 5. Section 4.3 定理3后第一讨论段

- order：5

- locator：Section 4.3 定理3后第一讨论段

- paraphrase_cn：定理3只在准确知道εi时精确保证收入；缺少信息时可使用人口平均或分布估计近似实现目标收入同时保持曲线。

- move_code：DESIGN_RATIONALE_INFORMATION_VARIANTS

- statement_status：author_inference

- why_here_cn：承认收入精确保证需要信息，但提供近似方案，使CBP在现实信息条件下仍可用。

- inherits_from_previous_cn：依赖定理3。

- changes_argument_state_cn：把理论结果映射为minimal/distributional两种信息版本。

- sets_up_next_cn：为第6.5节2x2配置提供理论接口。

- failure_if_removed_cn：CBP-AH-Distrib和minimal版本无依据。

- evidence_pointer：Section 4.3 定理3后讨论

### 6. Section 4.3 定理4前段

- order：6

- locator：Section 4.3 定理4前段

- paraphrase_cn：即使个体私人约束使期望剖面D无法实现，只要从同一D-inducing族选α，观测剖面D0固定，网格运营者仍可通过族内调整α'逼近目标收入。

- move_code：DESIGN_RATIONALE_ROBUST_REVENUE

- statement_status：theory_claim

- why_here_cn：解释CBP收入调整为何对私人约束稳健：族结构使收入调整不破坏曲线目标。

- inherits_from_previous_cn：依赖定理2族与定理3讨论。

- changes_argument_state_cn：把收入调整机制推广到现实约束情形。

- sets_up_next_cn：为定理4的公式和CH Step2b/2c提供动机。

- failure_if_removed_cn：在带约束仿真中收入匹配无理论预测。

- evidence_pointer：Section 4.3 定理4前段

### 7. Section 5 Step 2a讨论

- order：7

- locator：Section 5 Step 2a讨论

- paraphrase_cn：α1=α0·w属于D=w诱导族，因此继承所有解析性质；换族允许从D0向D′改进，同时保持收入调整能力。

- move_code：DESIGN_RATIONALE_ALGORITHM_PROPERTY

- statement_status：theory_claim

- why_here_cn：证明CH的粗略除法调整不是ad hoc，而是一个解析性质继承的换族操作。

- inherits_from_previous_cn：依赖定理2的D-inducing族结构。

- changes_argument_state_cn：把数据驱动步骤纳入理论框架，防止‘黑箱’批评。

- sets_up_next_cn：为Step2b/2c在同一族内继续调整做铺垫。

- failure_if_removed_cn：CH迭代缺少理论身份。

- evidence_pointer：Section 5 Step 2a讨论

### 8. Section 5 Step 2c讨论（'Finally'）

- order：8

- locator：Section 5 Step 2c讨论（'Finally'）

- paraphrase_cn：通过两个观测点拟合线性函数F=f(Ψ)并外推F*，可进一步改善收入匹配。

- move_code：DESIGN_RATIONALE_LOW_ITERATION

- statement_status：design_decision

- why_here_cn：用两个观测点完成学习，正面回应文献批评的‘需要大量迭代’。

- inherits_from_previous_cn：依赖Step2a/2b观测点。

- changes_argument_state_cn：CH被定义为一个近实时、低迭代算法。

- sets_up_next_cn：支持讨论中‘快速适应现实环境’的贡献主张。

- failure_if_removed_cn：低迭代优势没有设计支撑。

- evidence_pointer：Section 5 Step 2c

### 9. Section 6.4 Benchmark 2讨论（Figure 11后）

- order：9

- locator：Section 6.4 Benchmark 2讨论（Figure 11后）

- paraphrase_cn：无容量分量的时变价格导致所有agent在早间低价时段集中充电、形成高波动和雪崩效应；这正是CBP要缓解的。

- move_code：BENCHMARK_RATIONALE

- statement_status：empirical_result

- why_here_cn：用基准实例说明没有容量分量的价格会怎样，反向印证容量项的设计必要性。

- inherits_from_previous_cn：依赖Benchmark 2实现与指标。

- changes_argument_state_cn：在仿真内部确认雪崩现象并把它归因于缺乏容量分量。

- sets_up_next_cn：支撑CBP配置在7.2中优于variable pricing的结果。

- failure_if_removed_cn：CBP容量项的价值无法被对照证实。

- evidence_pointer：Section 6.4 Benchmark 2与Figure 11

### 10. Section 6.4 Benchmark 3

- order：10

- locator：Section 6.4 Benchmark 3

- paraphrase_cn：递增阶梯定价按Borenstein结构实现，被认为在平坦场景会表现好，因其设计目标就是重新分配需求使曲线平坦。

- move_code：BENCHMARK_RATIONALE_STRONGEST

- statement_status：method_decision

- why_here_cn：承认最强基准在平坦场景擅长，使后文CBP仍优于它更有说服力；同时说明其在任意形状上不够灵活。

- inherits_from_previous_cn：依赖Benchmark设计链。

- changes_argument_state_cn：设定一个公正且有挑战性的对照。

- sets_up_next_cn：为7.1-7.3中的比较结果提供参照。

- failure_if_removed_cn：比较会显得欺负弱基准。

- evidence_pointer：Section 6.4 Benchmark 3

## Study开头、过渡与收束图谱

### 1. Section 7 开头总纲 P1-P3

- locator：Section 7 开头总纲 P1-P3

- study_phase：评价总纲

- opening_move_cn：说明使用第6节testbed、δ=1h、T=168h，并引文献证明该粒度与horizon常用。

- development_move_cn：指出关心总需求曲线峰值、波动性和收入目标，将需求与收入结合评价。

- closing_move_cn：预告按不同波动性期望剖面分场景评价。

- transition_function_cn：建立三个评价场景的统一前提和指标。

### 2. Section 7.1 P1

- locator：Section 7.1 P1

- study_phase：场景1：平坦曲线

- opening_move_cn：直接给出场景设定：I=1000、Φ=168 MWh、P0=0.05。

- development_move_cn：引Figures 12与Table 2，指出CBP-CH近最优RMSE/PAPR/Peak；解释小偏差来自异质性；承认递增阶梯在平坦场景设计上擅长但仍落后。

- closing_move_cn：转入收入目标维度：引Theorem 3与Figure 13说明族-收入关系，再用Table 3报告收入偏差。

- transition_function_cn：证明在经典平坦任务中CBP既匹配曲线又满足收入，并制造下一个更难场景的需要。

### 3. Section 7.1 末段（收入小结）

- locator：Section 7.1 末段（收入小结）

- study_phase：场景1收入小结

- opening_move_cn：直接评价收入结果：CBP-AH偏差2.70%，-Distrib 0.14%，CBP-CH 0.12%，CBP-CH-Distrib 0.08%。

- development_move_cn：指出线性关系在带约束群体中仍存在所以CH能低复杂度完成收入匹配。

- closing_move_cn：总结CBP在诱导需求与收入两方面都优于基准且无高计算复杂度。

- transition_function_cn：把平场景结果提升为‘双重目标同时实现’的主张，转入7.2非平坦场景。

### 4. Section 7.2 P1-P2

- locator：Section 7.2 P1-P2

- study_phase：场景2：家庭负荷互补

- opening_move_cn：扩展场景：定价必须在家庭负荷之上诱导EV曲线，使组合总曲线平坦。

- development_move_cn：报告Figures 14-15与Table 4；指出rate-independent variable pricing因所有agent低价时段充电产生约8.5 MWh早峰（雪崩）；flat pricing弱于CBP；increasing-block在基准中最好但不如CBP的粒度控制。

- closing_move_cn：引Online Appendix H报告收入能力良好，总结CBP在非平坦EV曲线任务仍最优。

- transition_function_cn：用更难的诱导任务排除CBP只适用平坦剖面的解释。

### 5. Section 7.2 末段

- locator：Section 7.2 末段

- study_phase：场景2小结

- opening_move_cn：直接总结CBP在总曲线平坦目标下仍最优且近最优。

- development_move_cn：重复证据：最低峰值、PAPR接近1、RMSE低至0.03 MWh。

- closing_move_cn：用‘非平坦期望剖面也适用’收尾。

- transition_function_cn：进入更可持续的PV跟随场景。

### 6. Section 7.3 P1-P2

- locator：Section 7.3 P1-P2

- study_phase：场景3：PV跟随

- opening_move_cn：把场景直接连接到增加社会可持续性目标：按可再生出力塑形需求。

- development_move_cn：说明方案定位后给出PV数据来源（威斯康星，4月25日至6月23日）；比较CBP-AH（RMSE 0.83）与CBP-CH（0.21）并报告increasing-block仅4.65。

- closing_move_cn：报告收入目标在波动剖面也达成（附录H），并总结可持续性含义。

- transition_function_cn：把结果升级为可再生整合的贡献，并引出对未来预测误差和agent能力的稳健性检验。

### 7. Section 7.3 末段（总体结果与概括）

- locator：Section 7.3 末段（总体结果与概括）

- study_phase：总体概括

- opening_move_cn：总结三场景总体结果：可成功诱导不同种类曲线同时满足收入目标。

- development_move_cn：指出可再生主要挑战是波动性与稳定家庭负荷不匹配，本文可诱导跟随任意剖面。

- closing_move_cn：把方法推广到风力或其他可再生，贡献于可持续。

- transition_function_cn：为7.4稳健性检验做铺垫。

### 8. Section 7.4 P1

- locator：Section 7.4 P1

- study_phase：稳健性检验

- opening_move_cn：说明将评价延伸到更近视、少规划agent能力。

- development_move_cn：指出同一三场景仍用同一testbed，结果在Online Appendix J，报告显示保持优势。

- closing_move_cn：以‘结果对agent能力不敏感’收尾。

- transition_function_cn：为讨论中‘可推广性’主张提供边界支撑。

## 讨论与贡献逐句图谱

### 1. Section 8 P1 S1-S3

- order：1

- locator：Section 8 P1 S1-S3

- paraphrase_cn：EV充电协调是可持续城市的重要挑战；现有方案因激励不对齐而失败；本文描述一个新协调艺术，结合分布式自利决策与中央协调，用容量定价诱导期望聚合剖面。

- move_code：OPENING_RESTATEMENT

- statement_status：contribution_claim

- why_here_cn：讨论开篇重述引言问题与方案，把读者带回全文主线。

- inherits_from_previous_cn：承接Section 7全部结果。

- changes_argument_state_cn：从‘结果证明有效’转向‘这意味着什么贡献’。

- sets_up_next_cn：为Green IS理论贡献展开。

- failure_if_removed_cn：讨论缺回归主线的锚点。

- evidence_pointer：Section 8 P1

### 2. Section 8 P1 S4-S6

- order：2

- locator：Section 8 P1 S4-S6

- paraphrase_cn：本研究对Green IS特别重要，因为制品可诱导匹配或补充任意形状发电剖面的EV需求，包括平坦、补充已有需求、跟随可再生复杂曲线。

- move_code：THEORY_CONTRIBUTION

- statement_status：contribution_claim

- why_here_cn：把仿真结果提升为Green IS理论贡献：任意曲线诱导实现eco-equity与eco-effectiveness。

- inherits_from_previous_cn：依赖7.1-7.3场景。

- changes_argument_state_cn：从‘方法有效’升级为‘满足Green IS目标’。

- sets_up_next_cn：下一句继续解释基础设施节约与可再生利用。

- failure_if_removed_cn：Green IS理论贡献不成立。

- evidence_pointer：Section 8 P1 S4-S6

### 3. Section 8 P1 S7-S9

- order：3

- locator：Section 8 P1 S7-S9

- paraphrase_cn：这样的匹配能力更高效利用现有电网基础设施、减少额外铜缆等投资；使需求跟随可再生可增加可再生利用、节省常规能源并减排。

- move_code：THEORY_CONTRIBUTION_DEVELOPMENT

- statement_status：contribution_claim

- why_here_cn：把任意曲线诱导转译为基础设施节约与减排，即Green IS两大目标。

- inherits_from_previous_cn：依赖前句Green IS定位。

- changes_argument_state_cn：把设计能力连接到环境结果。

- sets_up_next_cn：最后用Watson术语总结生态公平与生态效益。

- failure_if_removed_cn：Green IS贡献缺乏环境和基础设施意义。

- evidence_pointer：Section 8 P1 S7-S9

### 4. Section 8 P1 S10

- order：4

- locator：Section 8 P1 S10

- paraphrase_cn：遵循Watson等术语和图1，制品同时满足生态公平（电网平衡）与生态效益（可再生整合）以及有环保意识的EV司机需求。

- move_code：THEORY_FRAMEWORK_RETURN

- statement_status：contribution_claim

- why_here_cn：用引言引入的Watson框架术语收束Green IS贡献，完成‘问题-理论-设计-检验-回到理论’闭环。

- inherits_from_previous_cn：依赖引言图1与全篇结果。

- changes_argument_state_cn：宣布理论框架层面的贡献完成。

- sets_up_next_cn：接下来进入七个具体研究贡献列表。

- failure_if_removed_cn：理论框架闭环断裂，贡献缺少语言体系。

- evidence_pointer：Section 8 P1 S10

### 5. Section 8 贡献(1)

- order：5

- locator：Section 8 贡献(1)

- paraphrase_cn：贡献1：描述一个新的IS赋能的容量定价制品，包括基于充电速率的动态组件，可对不同速率按其电网影响定价。

- move_code：CONTRIBUTION_LIST_ARTIFACT

- statement_status：contribution_claim

- why_here_cn：第一条贡献对应核心制品本身，是后续所有贡献的母体。

- inherits_from_previous_cn：承接Green IS总贡献。

- changes_argument_state_cn：开始逐条列出可审计的贡献。

- sets_up_next_cn：为解析启发式贡献(2)铺垫。

- failure_if_removed_cn：贡献清单缺第一支柱。

- evidence_pointer：Section 8 贡献(1)

### 6. Section 8 贡献(2)

- order：6

- locator：Section 8 贡献(2)

- paraphrase_cn：贡献2：开发基于理论性质的解析价格设定启发式（AH）。

- move_code：CONTRIBUTION_LIST_ANALYTICAL

- statement_status：contribution_claim

- why_here_cn：第二条贡献指向Section 4解析结果。

- inherits_from_previous_cn：依赖贡献(1)制品。

- changes_argument_state_cn：把理论推导列为独立贡献。

- sets_up_next_cn：为计算启发式贡献(3)铺垫。

- failure_if_removed_cn：解析部分只剩技术细节而无贡献名分。

- evidence_pointer：Section 8 贡献(2)

### 7. Section 8 贡献(3)

- order：7

- locator：Section 8 贡献(3)

- paraphrase_cn：贡献3：以解析启发式为起点开发低复杂性计算启发式，利用观测充电行为改善平衡结果。

- move_code：CONTRIBUTION_LIST_COMPUTATIONAL

- statement_status：contribution_claim

- why_here_cn：第三条贡献指向Section 5 CH，强调低复杂度与数据驱动。

- inherits_from_previous_cn：依赖贡献(2)的起点。

- changes_argument_state_cn：把数据驱动算法列为独立贡献。

- sets_up_next_cn：为收入平衡贡献(4)铺垫。

- failure_if_removed_cn：CH经验贡献缺名分。

- evidence_pointer：Section 8 贡献(3)

### 8. Section 8 贡献(4)

- order：8

- locator：Section 8 贡献(4)

- paraphrase_cn：贡献4：提供内置收入平衡能力，这是使定价方案适应各种现实经济环境的关键组件。

- move_code：CONTRIBUTION_LIST_REVENUE

- statement_status：contribution_claim

- why_here_cn：第四点把收入等价从辅助结果提为独立贡献，回应监管实用需求。

- inherits_from_previous_cn：依赖定理3/4与仿真Table 3。

- changes_argument_state_cn：突出双目标能力。

- sets_up_next_cn：为近最优任意曲线贡献(5)铺垫。

- failure_if_removed_cn：收入能力的工程与理论价值被低估。

- evidence_pointer：Section 8 贡献(4)

### 9. Section 8 贡献(5)

- order：9

- locator：Section 8 贡献(5)

- paraphrase_cn：贡献5：在随机EV充电环境中提供诱导任意需求曲线的近最优解，例如跟随光伏出力，以可再生产物覆盖充电需求。

- move_code：CONTRIBUTION_LIST_ARBITRARY_PROFILE

- statement_status：contribution_claim

- why_here_cn：第五点指向任意曲线诱导这一‘技术升级’，并连接到可再生与可持续。

- inherits_from_previous_cn：依赖7.1-7.3三个场景。

- changes_argument_state_cn：把场景证据归纳为普适能力。

- sets_up_next_cn：为突破文献限制贡献(6)铺垫。

- failure_if_removed_cn：‘任意曲线’主张无证据对应。

- evidence_pointer：Section 8 贡献(5)

### 10. Section 8 贡献(6)

- order：10

- locator：Section 8 贡献(6)

- paraphrase_cn：贡献6：把领域进展推进到突破文献常见限制：不需大量学习迭代、不需除理性外的行为假设、不需受限需求剖面；因此能快速适应变化环境。

- move_code：CONTRIBUTION_LIST_BEYOND_LITERATURE

- statement_status：contribution_claim

- why_here_cn：第六点直接回扣2.3节三类缺口，声称本文逐一突破。

- inherits_from_previous_cn：依赖2.3缺口与全篇设计结果。

- changes_argument_state_cn：完成‘缺口-解决’闭环。

- sets_up_next_cn：为广泛评价贡献(7)铺垫。

- failure_if_removed_cn：文献贡献主张无锚点。

- evidence_pointer：Section 8 贡献(6)

### 11. Section 8 贡献(7)

- order：11

- locator：Section 8 贡献(7)

- paraphrase_cn：贡献7：在多个现实平衡场景中对提出方法进行了非常广泛的评价。

- move_code：CONTRIBUTION_LIST_EVALUATION

- statement_status：contribution_claim

- why_here_cn：第七点把评价本身列为贡献，符合设计科学惯例。

- inherits_from_previous_cn：依赖Section 6-7全部评价。

- changes_argument_state_cn：收束贡献清单。

- sets_up_next_cn：进入实践与社会意涵。

- failure_if_removed_cn：评价工作量不被承认。

- evidence_pointer：Section 8 贡献(7)

### 12. Section 8 实践意涵段 S1-S6

- order：12

- locator：Section 8 实践意涵段 S1-S6

- paraphrase_cn：工作对智能电网运营者、能源供应商、城市交通规划者有实际意义；运营者减少峰值、供应商管理容量成本、规划者促进可持续EV采用；公用事业可维持需求与收入目标；EV司机受益于低停电风险与绿色电价。

- move_code：PRACTICAL_CONTRIBUTION

- statement_status：contribution_claim

- why_here_cn：把技术贡献向五类利益相关者转译，满足IS实践影响要求。

- inherits_from_previous_cn：依赖贡献清单(1)-(7)。

- changes_argument_state_cn：把制品贡献转为管理意义。

- sets_up_next_cn：为边界与未来研究铺垫。

- failure_if_removed_cn：实践应用价值缺失。

- evidence_pointer：Section 8 实践意涵段

### 13. Section 8 未来研究段 S1-S2

- order：13

- locator：Section 8 未来研究段 S1-S2

- paraphrase_cn：所有结果假设价格不改变私人驾驶需求与充电可用性；未来可研究更极端定价对消费偏好的影响，可考察leader-follower动态博弈框架。

- move_code：BOUNDARY_AND_FUTURE

- statement_status：author_inference

- why_here_cn：诚实划定边界：价格不影响出行需求；并给出未来研究路径。

- inherits_from_previous_cn：依赖贡献与评价边界。

- changes_argument_state_cn：保护贡献免于过度外推。

- sets_up_next_cn：继续两个未来方向。

- failure_if_removed_cn：读者可能把结果外推到价格改变行为的情形。

- evidence_pointer：Section 8 未来研究段 S1-S2

### 14. Section 8 未来研究段 S3-S4

- order：14

- locator：Section 8 未来研究段 S3-S4

- paraphrase_cn：第二个未来方向：假设所有EV车主订阅本方案；未来可研究有其他电价套餐存在时的效果。

- move_code：BOUNDARY_AND_FUTURE

- statement_status：author_inference

- why_here_cn：承认订阅独占性假设是边界。

- inherits_from_previous_cn：承接边界讨论。

- changes_argument_state_cn：进一步限定适用范围。

- sets_up_next_cn：最后一个未来方向。

- failure_if_removed_cn：方案的现实采纳场景被高估。

- evidence_pointer：Section 8 未来研究段 S3-S4

### 15. Section 8 未来研究段 S5

- order：15

- locator：Section 8 未来研究段 S5

- paraphrase_cn：第三个未来方向：纳入更细粒度IoT信息反映更细致agent约束与偏好，可带来更高效结果。

- move_code：FUTURE_RESEARCH

- statement_status：author_inference

- why_here_cn：用未来技术方向收束，留下正面展望。

- inherits_from_previous_cn：承接前两个方向。

- changes_argument_state_cn：结束全文，把边界转为开放问题。

- sets_up_next_cn：无，文章结束。

- failure_if_removed_cn：全文缺收束性的展望句。

- evidence_pointer：Section 8 未来研究段 S5

## Study累积逻辑

### 1. 1

- study_or_phase：阶段1：解析启发式推导（Section 4）

- evidence_job_cn：证明CBP在理想无约束情形下可同时诱导期望曲线与目标收入。

- what_it_establishes_cn：建立agent最优充放电率与α反比（定理1）、诱导条件（定理2）、收入条件（定理3-4）以及D-inducing族结构。

- what_it_cannot_establish_cn：不能证明在带私有可用性约束、异质随机agent的真实情形下有效。

- why_next_phase_is_needed_cn：现实网格管理者只有聚合观测且agent有私人约束，需要数据驱动的算法来适应。

- transition_wording_function_cn：Section 5开头说明从解析到计算的动因：更复杂且不可解析可处理的情形。

### 2. 2

- study_or_phase：阶段2：计算启发式CH设计（Section 5）

- evidence_job_cn：用少量聚合观测数据把理想解析解调整为带约束现实情形可用的低复杂度算法。

- what_it_establishes_cn：CH通过初始化、需求偏差调整、收入调整与线性外推在有限迭代内逼近双目标。

- what_it_cannot_establish_cn：不能证明其在真实数据、异质agent、多基准对照的仿真中优于现状。

- why_next_phase_is_needed_cn：需要统一仿真平台来公平评价AH/CH与基准。

- transition_wording_function_cn：Section 6开头说明搭建多agent仿真testbed的必要性。

### 3. 3

- study_or_phase：阶段3：仿真testbed与数据校准（Section 6）

- evidence_job_cn：为后续评价提供可复现、真实数据校准的受控实验环境。

- what_it_establishes_cn：仿真协议、评价指标、三个基准与四个CBP配置，外部有效性通过荷兰/威斯康星真实数据建立。

- what_it_cannot_establish_cn：平台本身不产生关于CBP有效性的结论。

- why_next_phase_is_needed_cn：需要实际运行三个场景以产生结果。

- transition_wording_function_cn：Section 7开头说明评价场景结构。

### 4. 4

- study_or_phase：阶段4：场景1平坦曲线（Section 7.1）

- evidence_job_cn：证明CBP在经典平坦剖面任务中同时最优匹配曲线与收入。

- what_it_establishes_cn：CBP-CH RMSE 0.02、PAPR 1.07、Peak 1.03近最优；收入偏差最低0.08%；基准无收入目标能力。

- what_it_cannot_establish_cn：不能证明CBP在非平坦或高波动剖面上有效。

- why_next_phase_is_needed_cn：平坦是最简单任务，现实更关心非平坦与可再生跟随。

- transition_wording_function_cn：7.2开头说明扩展场景：在家庭负荷上补EV使总曲线平坦。

### 5. 5

- study_or_phase：阶段5：场景2家庭负荷互补（Section 7.2）

- evidence_job_cn：证明CBP可诱导非平坦EV曲线以平抑组合总负荷，并实证雪崩效应。

- what_it_establishes_cn：CBP-CH RMSE 0.03、PAPR 1.06仍最优；无容量分量的variable pricing产生8.5 MWh早峰雪崩。

- what_it_cannot_establish_cn：不能证明CBP可跟随高波动可再生曲线。

- why_next_phase_is_needed_cn：可持续目标（可再生整合）需要更高波动期望剖面。

- transition_wording_function_cn：7.3开头直接连接到可持续性目标与PV场景。

### 6. 6

- study_or_phase：阶段6：场景3 PV跟随（Section 7.3）

- evidence_job_cn：证明CBP能近最优跟随高波动可再生出力曲线，连接Green IS可持续贡献。

- what_it_establishes_cn：CBP-AH RMSE 0.83、CBP-CH 0.21，远优于increasing-block的4.65。

- what_it_cannot_establish_cn：不能证明结果在期望剖面含预测误差或agent更近视时仍成立。

- why_next_phase_is_needed_cn：需要排除结果由理想假设驱动。

- transition_wording_function_cn：7.3末与7.4开头引入预测误差与近视agent的稳健性检验。

### 7. 7

- study_or_phase：阶段7：稳健性检验（Section 7.4 + Online Appendices I/J）

- evidence_job_cn：检验结论是否依赖agent规划能力或完美期望剖面。

- what_it_establishes_cn：根据作者报告，CBP在myopic agents与预测误差设定下仍优于所有基准。

- what_it_cannot_establish_cn：不能证明真实世界现场有效性或用户行为长期响应。

- why_next_phase_is_needed_cn：稳健性后需要把经验结果提升为设计知识与理论贡献。

- transition_wording_function_cn：Section 8讨论开篇重述问题并把结果上升为Green IS贡献。

## 主张—证据台账

### 1. CBP制品可诱导期望EV充电曲线并同时满足收入目标。

- claim_cn：CBP制品可诱导期望EV充电曲线并同时满足收入目标。

- claim_level：artifact

- supporting_evidence_cn：三个场景中CBP-CH RMSE分别0.02/0.03/0.21 MWh，收入偏差最低0.08%/附录H报告其他场景一致。

- support_strength：direct

- where_claim_is_made：摘要P3、Introduction P4、Section 7.1-7.3、Section 8贡献(4)(5)

- where_evidence_is_provided：Section 7.1 Table 2-3、7.2 Table 4、7.3 Table 5、Online Appendix H

### 2. 容量相关的速率项α·r是CBP优于基准的关键。

- claim_cn：容量相关的速率项α·r是CBP优于基准的关键。

- claim_level：mechanism

- supporting_evidence_cn：Benchmark 2（无容量分量时变价格）在7.2产生8.5 MWh早峰雪崩，而CBP的PAPR接近1；定理1证明速率与α反比。

- support_strength：direct

- where_claim_is_made：Introduction P3-P4、Section 3.2、Section 7.2

- where_evidence_is_provided：Section 6.4 Benchmark 2与Figure 11、Section 7.2 Table 4、Theorem 1

### 3. CBP诱导曲线不需要个体偏好信息（仅需聚合观测）。

- claim_cn：CBP诱导曲线不需要个体偏好信息（仅需聚合观测）。

- claim_level：design_knowledge

- supporting_evidence_cn：定理2最优条件不含εi；CH的Step2a只用聚合需求偏差w=D0/D调整。

- support_strength：direct

- where_claim_is_made：Section 4.2、Section 5 Step2a、Section 8贡献(6)

- where_evidence_is_provided：Theorem 2及其讨论、Section 5 Step2a讨论

### 4. CBP不需要大量迭代或学习，可快速适应环境变化。

- claim_cn：CBP不需要大量迭代或学习，可快速适应环境变化。

- claim_level：design_knowledge

- supporting_evidence_cn：CH仅需初始α0、一次需求调整、一次收入调整和两点线性外推；与文献中20-100天迭代的对照。

- support_strength：direct

- where_claim_is_made：Section 2.3缺口总结、Section 5 Step2c、Section 8贡献(3)(6)

- where_evidence_is_provided：Section 5 Step2c算法、Section 2.3文献对照、Section 7.1-7.3结果

### 5. CBP可诱导任意形状需求曲线，不只平坦。

- claim_cn：CBP可诱导任意形状需求曲线，不只平坦。

- claim_level：mechanism

- supporting_evidence_cn：三个场景分别展示平坦、家庭负荷互补（非平坦EV曲线）、PV跟随（高波动）三种形状均近最优。

- support_strength：partial

- where_claim_is_made：Introduction P4、Section 8贡献(5)

- where_evidence_is_provided：Section 7.1-7.3三个场景；但只测了三种曲线，并非真正任意形状

### 6. 收入目标可由minimal或distributional信息近似达成。

- claim_cn：收入目标可由minimal或distributional信息近似达成。

- claim_level：artifact

- supporting_evidence_cn：Table 3中CBP-AH偏差2.70%，-Distrib 0.14%，CBP-CH 0.12%，CBP-CH-Distrib 0.08%。

- support_strength：direct

- where_claim_is_made：Section 4.3、Section 7.1末、Section 8贡献(4)

- where_evidence_is_provided：Table 3、Online Appendix H

### 7. CBP在myopic agent与预测误差设定下仍保持优势。

- claim_cn：CBP在myopic agent与预测误差设定下仍保持优势。

- claim_level：boundary

- supporting_evidence_cn：Section 7.4与Online Appendices I/J报告保持优于所有基准，但主文未给具体表/数字。

- support_strength：partial

- where_claim_is_made：Section 7.4、Section 8贡献(6)

- where_evidence_is_provided：Online Appendices I/J（主文只引用，无具体数据）

### 8. CBP实现Green IS的eco-equity与eco-effectiveness。

- claim_cn：CBP实现Green IS的eco-equity与eco-effectiveness。

- claim_level：theory

- supporting_evidence_cn：电网平衡（eco-equity）与可再生跟随（eco-effectiveness）分别由三个场景与图1框架证明。

- support_strength：partial

- where_claim_is_made：Introduction P6、Section 8 P1

- where_evidence_is_provided：仿真结果映射到框架的推断性连接；该连接是作者的理论解释而非直接测量

### 9. CBP收入保持不改变总充电成本（收入等价）。

- claim_cn：CBP收入保持不改变总充电成本（收入等价）。

- claim_level：artifact

- supporting_evidence_cn：以flat pricing收入17,878.6为目标，CBP-CH-Distrib偏差0.08%，满足监管等价要求。

- support_strength：direct

- where_claim_is_made：Abstract末、Section 7.1末、Section 8贡献(4)

- where_evidence_is_provided：Section 7.1 Table 3

## ISR定位逻辑

- constitutive_is_problem_cn：本文把问题构成为‘智能市场中的信息与协调问题’而非纯电力工程问题：网格运营者拥有聚合信息但缺乏个体偏好信息，EV owners拥有私人偏好却无法自组织避免集体次优（雪崩效应），IS制品（定价机制+agent）作为信息协调层同时服务两者。

- technology_behavior_or_market_entanglement_cn：技术（容量定价价格信号）与行为（理性agent成本最小化、私有约束、异质性）相互构成：价格信号利用agent理性以诱导行为，而agent的私人约束反过来决定需要数据驱动的CH调整；智能agent既是技术实现（移动设备/充电控制器上的软件代理），也是用户行为的代表。

- role_of_benchmark_or_objective_evidence_cn：三类benchmark起因果隔离作用：flat pricing代表现状、rate-independent variable pricing证明没有容量分量时动态价格仍产生雪崩、increasing-block代表最强的传统非线性定价；客观指标RMSE/PAPR/peak把‘可持续’操作化为可测量的电网平衡性能，用来支持机制主张而非仅分数优势。

- theory_in_design_cn：理论以强耦合方式进入设计：非线性/spot定价与理性agent优化知识直接推导出公式(1)与定理1-4，定理又成为AH的构成条件与CH的初始化/换族依据；不是事后用理论解释结果。

- technical_vs_is_contribution_balance_cn：技术贡献（新定价公式、AH/CH算法、定理）占较大篇幅，但作者通过三层方式把它转换为IS贡献：把制品定义为‘IS-enabled pricing artifact’、嵌入Watson等Green IS框架并用Ketter等研究议程定位、以及把仿真结果转译为电网运营者/供应商/政策制定者/司机的利益相关者价值。

- beyond_transient_performance_cn：不只是一时分数优势：作者声称优势来自CBP的结构性质（容量项分散理性响应、D-inducing族继承解析性质、族内调整实现收入等价），并以定理保证、多场景鲁棒性、低迭代与信息要求低作为可复用设计知识；同时作者用边界条件（价格不变出行需求、订阅独占、仿真而非现场）把主张限制在可辩护范围。

## 段落级仿写模板

### abstract_steps

1. 步骤1：第一句给出制品（IS-enabled pricing artifact + 应用背景）。

2. 步骤2：一句话给出背景价值（EV不错）。

3. 步骤3：一句话给出问题（大规模引入导致电网峰值/威胁稳定）。

4. 步骤4：一句话给出现有方案缺陷（激励不对齐/雪崩效应）。

5. 步骤5：第二段给出制品的组成（动态价格成分+解析/计算启发式）。

6. 步骤6：一句话说明机制（理性agent自优化+总体再平衡）。

7. 步骤7：第三段给出结果（降低波动/匹配可再生）。

8. 步骤8：说明结果如何获得（与当前定价基准比较）。

9. 步骤9：末段把结果转译为利益相关者价值（电网、供应商、市场利益相关者）。

### introduction_paragraph_steps

1. 步骤1：宏观背景段：把问题放入智能城市/气候/大数据叙事，用具体数字建立紧迫性，最后指出IS可介入。

2. 步骤2：问题机制段：把宏观风险转化为具体机制（高峰时段、高功率负荷），用成本/不可持续性封死传统解法。

3. 步骤3：现象段：定义核心现象（雪崩/激励不对齐）并引文献经验确认。

4. 步骤4：方案段：用理论坐标（smart markets）把问题转译为IS议程，预告方案属性（单向通信、任意曲线），呈现核心设计（CBP公式+价格设定方法+设计科学定位）。

5. 步骤5：利益相关者段：把技术方案转译为各利益相关者收益与社会可持续途径。

6. 步骤6：贡献定位段：把贡献锚定到理论框架（Green IS），用框架图展示供需两侧IS元素，结束并预告后文。

### theory_to_design_steps

1. 步骤1：理论锚定：定义所属子领域与研究议程中的具体开放问题。

2. 步骤2：文献分类评述：用两分类或三分类组织既有文献，每类明确适用条件与失败模式。

3. 步骤3：缺口总结：把多股文献批评压缩为少数几个设计约束（如迭代、行为假设、剖面受限）。

4. 步骤4：问题形式化：定义参与方、目标、信息边界、控制变量。

5. 步骤5：设计公式：给出核心公式并解释其物理/机制依据。

6. 步骤6：agent模型：定义agent偏好与优化问题，使机制‘理性agent如何响应’可分析。

7. 步骤7：启发式动因：指出不完全信息+计算困难，因此需要解析与计算启发式。

8. 步骤8：解析推导：给出最优响应、诱导条件、收入条件（定理），并说明信息需求。

9. 步骤9：算法设计：以解析解为初值，用可观察聚合数据进行调整，并解释每个调整的理论性质。

10. 步骤10：评价衔接：用仿真testbed与真实数据校准把设计代入评价阶段。

### method_and_study_sequence_steps

1. 步骤1：搭建仿真环境：明确agent模型与网格agent的协议（Steps 1-6）。

2. 步骤2：定义指标：RMSE为主，领域指标PAPR/peak只在平坦场景使用。

3. 步骤3：真实数据校准：用真实出行、电价、负荷、PV数据。

4. 步骤4：设计递进基准：现状、无关键分量版本、最强替代方案。

5. 步骤5：配置化制品：2x2表（解析/计算×信息版本），提前声明哪些指标受信息影响。

6. 步骤6：场景难度递进：简单→非平坦→高波动，每场景先给设定、再报告指标、再解释基准为什么差。

7. 步骤7：收入目标与曲线目标并行报告：每个场景至少报告需求与收入两方面。

8. 步骤8：稳健性检验：扰动agent能力与期望误差，报告优势保持。

9. 过渡句功能：每个场景结尾预告更难的下一场景；稳健性后转入讨论。

### results_reporting_steps

1. 步骤1：场景开头陈述设定（I、Φ、P0、T）。

2. 步骤2：引图/表给出主结果，识别最优配置（如CBP-CH）。

3. 步骤3：解释与理想值的差距来源（随机性、异质性）。

4. 步骤4：对基准逐类解释为何差（如递增阶梯不够灵活、variable pricing雪崩）。

5. 步骤5：收入目标单独报告，并解释理论关系（族-收入）为何在带约束下仍近似成立。

6. 步骤6：用‘低计算复杂度’等设计属性对结果做因果归因，而非只报数字。

7. 步骤7：场景末总结把结果概括为能力主张（如‘可以诱导任意剖面’）。

### discussion_and_contribution_steps

1. 步骤1：重述问题与方案，把仿真结果带回主线。

2. 步骤2：把能力主张上升为理论贡献（如Green IS的eco-equity/eco-effectiveness），用框架术语收束。

3. 步骤3：逐条列出贡献：(1)制品(2)解析启发式(3)计算启发式(4)收入平衡(5)任意曲线(6)突破文献限制(7)广泛评价。

4. 步骤4：把技术贡献转译为利益相关者与管理意义。

5. 步骤5：诚实划定边界（价格不变行为、订阅独占、仿真非现场）。

6. 步骤6：以未来研究方向收束全文。

- results_reporting_steps_note_cn：注意：报告要区分哪些主张由直接证据（表/图/定理）支持，哪些由推论与理论解释支持。

## 可执行写作算法

### 1. 1

- step：1

- rhetorical_job_cn：建立现实问题与利害关系，把研究嵌入大叙事。

- research_evidence_required_cn：能展示目标领域发展（数据、政策目标、增长数字）与一个具体风险（峰值、稳定性）。

- sentence_pattern_function_cn：首句给背景价值，次句给问题，末句给IS介入角色。

- transition_condition_cn：当读者明白‘某好事物将带来危险且IS可参与’时进入下一步。

### 2. 2

- step：2

- rhetorical_job_cn：把问题机制化和物理化，排除传统解法。

- research_evidence_required_cn：需要具体机制（时段、功率、基础设施成本）证据。

- sentence_pattern_function_cn：用‘不是因为……而是因为……’式机制句与成本句封死旧路。

- transition_condition_cn：当读者同意旧解不可行时进入下一步。

### 3. 3

- step：3

- rhetorical_job_cn：定义核心现象/瓶颈并确证其真实存在。

- research_evidence_required_cn：需要文献与真实试点证据。

- sentence_pattern_function_cn：先给定义句（‘现象是……’），再给列举句（‘已在……被观察到’）。

- transition_condition_cn：当读者把问题视为可设计解决的机制问题时进入下一步。

### 4. 4

- step：4

- rhetorical_job_cn：用理论坐标把技术问题转译为本学科议程。

- research_evidence_required_cn：需要本学科的智能市场/设计科学框架文献。

- sentence_pattern_function_cn：用‘技术进步把X转化为……我们回应……’句式定位研究问题。

- transition_condition_cn：当读者把问题与IS议程连接后进入下一步。

### 5. 5

- step：5

- rhetorical_job_cn：呈现核心设计及其物理/机制依据。

- research_evidence_required_cn：需要能解释设计要素与问题机制对应关系（如容量≈速率）。

- sentence_pattern_function_cn：先给公式/结构句，再给‘因为……所以……’机制句。

- transition_condition_cn：当读者理解设计要素为何对应问题时进入下一步。

### 6. 6

- step：6

- rhetorical_job_cn：进行系统文献分类并制造精确缺口。

- research_evidence_required_cn：需要可归纳为少数限制的文献集合。

- sentence_pattern_function_cn：用‘第一/第二/第三’分类句和‘现有文献以三种方式限制问题’总结句。

- transition_condition_cn：当缺口可表述为可设计约束（迭代、信息、形状）时进入下一步。

### 7. 7

- step：7

- rhetorical_job_cn：形式化问题、信息边界与控制变量，使设计可分析。

- research_evidence_required_cn：需要明确参与方、目标函数、约束、可观测信息。

- sentence_pattern_function_cn：用‘目标是……’、‘只能观察……’、‘控制变量为……’的建模句。

- transition_condition_cn：当问题可被代入数学与算法时进入下一步。

### 8. 8

- step：8

- rhetorical_job_cn：在理想情形推导闭合条件，形成解析启发式。

- research_evidence_required_cn：需要能够解析求解的简化模型与定理。

- sentence_pattern_function_cn：用‘定理：在……条件下……’及随后的‘三个洞见’讨论句。

- transition_condition_cn：当理想解给出可执行条件且说明信息需求后进入下一步。

### 9. 9

- step：9

- rhetorical_job_cn：把解析解转化为数据驱动算法，回应‘计算复杂/需要信息’批评。

- research_evidence_required_cn：需要可观察的聚合信息与调整规则；最好有算法继承解析性质。

- sentence_pattern_function_cn：用‘Step……选择/调整/外推’分步算法句，每步解释理论性质。

- transition_condition_cn：当算法在有限观测内逼近双目标且继承理论性质时进入下一步。

### 10. 10

- step：10

- rhetorical_job_cn：用真实数据仿真和递进基准公平评价制品。

- research_evidence_required_cn：需要真实数据校准、指标定义、递进基准与多个场景。

- sentence_pattern_function_cn：用‘我们构建……’、‘我们使用……指标’、‘基准包括……’的协议句。

- transition_condition_cn：当不同场景结果一致支持制品后进入下一步。

### 11. 11

- step：11

- rhetorical_job_cn：把结果升华为贡献并划定边界，以未来研究收束。

- research_evidence_required_cn：需要贡献清单与每个贡献对应的表/图/定理，以及未测试的假设。

- sentence_pattern_function_cn：用‘贡献如下……’清单句和‘假设……未来可研究……’边界句。

- transition_condition_cn：当贡献得到证据对应且边界清晰后文章可结束。

## 应模仿的高价值动作

1. 用递进基准隔离核心设计分量：现状（flat）、无关键分量（rate-independent variable pricing）、最强替代（increasing-block）；分别证明‘现状差、无分量差、强替代仍不如CBP’。

2. 把解析可解情形作为算法初值，再设计数据驱动换族调整；每个算法步骤都交代其理论性质（如D=w-inducing族）防止被批评为黑箱。

3. 场景难度递进结构：平坦→非平坦（家庭负荷互补）→高波动（PV跟随）；每次升级都对应一个新的更可持续目标，支撑‘任意曲线’主张。

4. 提前在2.3节把文献缺口总结为三个可设计约束，并在贡献(6)处逐条回扣；形成‘缺口-设计-贡献’闭环。

5. 把结果从‘技术有效’转译为多利益相关者价值（电网、供应商、政策制定者、司机），并在摘要、引言、讨论三处重复该转译。

6. 用定理和族结构揭示‘虽然统一广播价格，但每个agent支付不同价格’的公平性解释，预防批评。

7. 讨论中用Watson等框架术语（eco-equity/eco-effectiveness）把仿真结果重新命名，而不是新造理论概念。

8. 把评价指标与领域含义绑定（PAPR=波动代理、RMSE=匹配度），使读者知道每个指标为什么重要。

## 不要只复制的表面动作

1. 不能只写‘引入一个动态价格成分’而不给出参数设定条件与收入调整机制；否则退化为一般动态定价。

2. 不能宣称‘任意曲线可诱导’而只报告平坦场景；至少需要一个非平坦与一个高波动场景。

3. 不能在摘要中说‘高度有效’而无基准比较与具体结果数字；IS论文需要对照。

4. 不能把仿真结果直接说成真实市场结论；需要边界句（如价格不变出行行为、订阅假设、预测误差等）。

5. 不能只重复Green IS套话而不把具体affordance（peak mitigation、renewable following）映射到结果。

6. 不要用过长benchmark代码描述替代机制解释；基准需要转译为对CBP机制的正面说明。

7. 不要只为每个定理添加一个段落而不说明该定理对设计与后文算法的具体用途。

## 证据薄弱或跳跃的动作

1. 从三种测试曲线推断‘任意形状需求曲线可诱导’的跳跃：作者在贡献(5)使用‘any desired profile’，但实际只测平坦、家庭负荷互补和PV三种。

2. myopic与预测误差的稳健性结果只放Online Appendices I/J，主文只有叙述性断言无具体表/图；读者无法验证强度。

3. 收入精确保证依赖εi信息；在minimal信息下只近似（偏差2.70%），但摘要与讨论仍强调‘维持总收入’，粒度需注意。

4. CH的线性外推F=f(Ψ)是对两点的线性假设；在极端非线性约束或收入函数强非线性的群体中可能失效，作者未测试。

5. 对Green IS理论贡献（eco-equity/eco-effectiveness）是框架映射式的解释，不是对可持续结果的直接测量。

6. 没有与最新深度RL或迭代方法在同一算例做运行时间/迭代次数的直接对比，低复杂度优势由文献叙述与算法观察支撑。

7. 家庭负荷与PV场景分别来自荷兰真实家庭数据与非同时地/时期的威斯康星PV数据；场景组合的地理一致性未说明。

## 一句话套路

用一个资源占用相关的容量定价价格公式把分布式自利agent行为转化为中央协调的柔性控制，先以解析解为初值、再用聚合数据小步调整，最后在难度递进、真实数据校准的多agent仿真中同时证明曲线匹配与收入等价并回接到Green IS框架。

## 分析边界

全文以在线全文与第一阶段导航为基础；定位用章节/段/表/图，无精确页码；附录I/J/H只以主文引用形式呈现，myopic、预测误差及场景2/3收入表的具体数据未在本全文文本中独立出现，故相关判断基于作者叙述；Section 6.4中关于rate-independent variable pricing和benchmark构造的句子因涉及较多数据细节在sentence_map中合并处理；图1-16无法逐图验证其视觉内容，只能核实其在文中的论证角色。
