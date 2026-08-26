# Retargeted vs. Generic Product Recommendations: When is it Valuable to Present Retargeted Recommendations?：ISR 句段级微观图谱

- 作者：Xiang (Shawn) Wan; Anuj Kumar; Xitong Li
- 年份：2024
- DOI：10.1287/isre.2020.0560
- 源文件：27979_2024_retargeted-vs-generic-product-recommendations-when-is-it-valuable-to-present-retargeted-recommen.md
- 置信度：0.9

## 核实后的宏观骨架

文章以‘重定向推荐与通用推荐在购买漏斗不同阶段的相对价值’为核心问题，构建了一个‘现象缺口—机制分解—现场随机实验—在线机制实验—总销售与反事实模拟—理论/实践贡献’的论证弧线。摘要简述缺口、方法、核心结果、MTurk机制检验、模拟收益与贡献；引言从推荐系统普遍现象出发定义两类推荐，提出阶段调节机制与双重文献缺口，给出三个研究问题，预告现场实验、MTurk实验、总销售分析与模拟结果，并提前声明三点贡献；文献综述分产品推荐、重定向广告、购买漏斗三部分，将重定向广告‘重定向’概念引入产品推荐并说明站内推荐需同时考察曝光量与转化率；现场设置部分说明零售网站、IBM Coremetrics推荐规则、曝光定义、机制预测、随机设计与两点局限；主分析将RP销售分解为转化率与曝光量/日销售两条路径（5.1.1与5.1.2），随后用MTurk两阶段在线实验分离重定向与算法亲和度（5.2），再以FP+RP总销售排除渠道替代（5.3），最后用反事实模拟量化替换策略的销售增益（6）；讨论依次完成理论贡献、管理含义、普遍性边界、局限与未来研究（7.1-7.4）。

## 摘要逐句图谱

### 1. Abstract P1 S1

- locator：Abstract P1 S1

- paraphrase_cn：虽然算法产品推荐对销售的总体效应已被理解，但重定向推荐（用户以前看过的推荐商品）与通用推荐（用户以前没看过的推荐商品）的差异效应尚不清楚。

- move_code：GAP

- statement_status：author_inference

- why_here_cn：摘要第一句必须建立已知与未知的落差，让读者立即明白论文要填的洞。

- inherits_from_previous_cn：无，这是摘要起点。

- changes_argument_state_cn：把‘推荐有效’的共识改写成‘两类推荐差异未知’的研究缺口。

- sets_up_next_cn：为下一句‘我们做现场实验’提供必要性。

- failure_if_removed_cn：缺少缺口句，读者不知道为什么要研究重定向与通用推荐。

### 2. Abstract P1 S2

- locator：Abstract P1 S2

- paraphrase_cn：我们用现场实验实证检验重定向推荐与通用推荐在用户购买漏斗不同阶段的相对销售效应。

- move_code：RQ_OR_OBJECTIVE

- statement_status：method_decision

- why_here_cn：在缺口之后立即给出研究目标和证据来源。

- inherits_from_previous_cn：承接‘差异效应不清楚’的缺口，回答‘怎么办’。

- changes_argument_state_cn：将抽象缺口转换为具体研究设计与设定。

- sets_up_next_cn：为下一句‘推荐通过两个机制影响销售’做方法铺垫。

- failure_if_removed_cn：读者不知道作者用什么办法回答缺口。

### 3. Abstract P1 S3

- locator：Abstract P1 S3

- paraphrase_cn：产品推荐可以同时通过影响推荐商品的曝光次数和曝光条件下的转化率来影响销售。

- move_code：MECHANISM

- statement_status：theory_claim

- why_here_cn：在介绍设计前先给出结果变量的分解框架，这是后文所有分析的骨架。

- inherits_from_previous_cn：承接现场实验的目标，说明要分析的机制维度。

- changes_argument_state_cn：把‘销售效应’拆成两个可分开估计的组件。

- sets_up_next_cn：为下一句‘分别估计两类推荐对曝光和转化率的效应’提供理由。

- failure_if_removed_cn：后文曝光量vs转化率的双路径分析失去概念依据。

### 4. Abstract P1 S4

- locator：Abstract P1 S4

- paraphrase_cn：我们分别估计重定向推荐和通用推荐对推荐商品曝光次数和转化率的影响。

- move_code：METHOD_JUSTIFICATION

- statement_status：method_decision

- why_here_cn：明确识别策略：不是只估计总销售，而是分解成两个路径。

- inherits_from_previous_cn：直接沿用上一句的机制分解。

- changes_argument_state_cn：把分析方法固定为‘曝光+转化率’双结果。

- sets_up_next_cn：为下面两个核心发现（转化率结果、曝光量结果）做方法准备。

- failure_if_removed_cn：结果部分的分路径报告缺少摘要层面的预告。

### 5. Abstract P1 S5

- locator：Abstract P1 S5

- paraphrase_cn：发现(i)通用推荐只在购买漏斗早期提高转化率，而重定向推荐不影响转化率；(ii)两类推荐都带来更高的推荐商品曝光量。

- move_code：RESULT

- statement_status：empirical_result

- why_here_cn：摘要必须压缩最核心的实证发现，这两点直接回答研究问题。

- inherits_from_previous_cn：是上一句‘分别估计曝光和转化率’的直接结果。

- changes_argument_state_cn：把‘两类推荐效果不同’从猜测变成有证据支撑的发现。

- sets_up_next_cn：为下一句‘总体上重定向（通用）推荐在晚期（早期）提高销售’做铺垫。

- failure_if_removed_cn：摘要缺少最核心的实证贡献。

### 6. Abstract P1 S6

- locator：Abstract P1 S6

- paraphrase_cn：总体而言，重定向（通用）推荐在购买漏斗晚期（早期）带来更高的推荐商品和总商品销售。

- move_code：RESULT

- statement_status：empirical_result

- why_here_cn：把曝光与转化率的组件结果整合成管理者最关心的销售结论。

- inherits_from_previous_cn：需要上一句的曝光量和转化率结果。

- changes_argument_state_cn：从机制组件上升到总体销售结论。

- sets_up_next_cn：为MTurk实验和模拟的价值声明做铺垫。

- failure_if_removed_cn：论文的阶段性结论在摘要中缺失。

### 7. Abstract P1 S7

- locator：Abstract P1 S7

- paraphrase_cn：我们还在Amazon MTurk上做了受控实验，揭示是重定向（向用户展示此前看过的商品）驱动了重定向推荐的效果。

- move_code：MECHANISM

- statement_status：empirical_result

- why_here_cn：现场实验的重定向推荐与算法推荐混在一起，摘要需要说明机制已被单独验证。

- inherits_from_previous_cn：承接现场结果‘重定向推荐在晚期提高销售’，回答‘为什么’。

- changes_argument_state_cn：把机制从推测变成实验证据。

- sets_up_next_cn：为下一句‘反事实模拟显示约3%销售增益’提供机制支持。

- failure_if_removed_cn：重定向效应的机制主张缺少证据支撑。

### 8. Abstract P1 S8

- locator：Abstract P1 S8

- paraphrase_cn：反事实模拟显示，把我们的发现应用到现有推荐系统可为零售商带来最高约3%的销售提升。

- move_code：RESULT

- statement_status：empirical_result

- why_here_cn：通过量化收益把学术发现转成可操作价值。

- inherits_from_previous_cn：需要前面的效应估计作为模拟输入。

- changes_argument_state_cn：把统计上的差异效应翻译成经济收益。

- sets_up_next_cn：为最后一句贡献声明提供实践依据。

- failure_if_removed_cn：摘要缺少对管理价值的量化承诺。

### 9. Abstract P1 S9

- locator：Abstract P1 S9

- paraphrase_cn：我们的研究对在线零售商和算法产品推荐系统的设计有启示。

- move_code：CONTRIBUTION

- statement_status：contribution_claim

- why_here_cn：摘要最后一句说明读者为何应该在意。

- inherits_from_previous_cn：承接前面的结果和模拟收益。

- changes_argument_state_cn：把全文定位为对实践与设计有意义的IS研究。

- sets_up_next_cn：无，摘要结束，转入引言。

- failure_if_removed_cn：摘要缺少收束句，贡献定位不清。

## 引言逐句图谱

### 1. Introduction P1 S1

- order：1

- locator：Introduction P1 S1

- paraphrase_cn：多数电商网站根据其他用户的共览和共购行为，在焦点商品页推荐少量相关商品，并附文献引用。

- move_code：CONTEXT

- statement_status：prior_literature

- why_here_cn：文章第一句必须把读者带入一个广泛且真实存在的电商现象。

- inherits_from_previous_cn：无，这是全文起点。

- changes_argument_state_cn：建立‘基于协同过滤的站内推荐很普遍’的前提。

- sets_up_next_cn：为下一句定义通用推荐提供技术背景。

- failure_if_removed_cn：读者不知道研究对象是什么。

### 2. Introduction P1 S2

- order：2

- locator：Introduction P1 S2

- paraphrase_cn：这种基于其他用户浏览行为推断用户偏好的协同过滤推荐，我们称为通用推荐。

- move_code：CONSTRUCT_DEFINITION

- statement_status：author_inference

- why_here_cn：在介绍完现象后立刻给核心构念命名，便于后文反复使用。

- inherits_from_previous_cn：沿用第一句‘根据其他用户的协看协买’的机制。

- changes_argument_state_cn：把已有技术术语‘协同过滤推荐’重新命名为本文的‘通用推荐’。

- sets_up_next_cn：为下一句定义重定向推荐提供对照。

- failure_if_removed_cn：后文‘generic recommendation’无处安放。

### 3. Introduction P1 S3

- order：3

- locator：Introduction P1 S3

- paraphrase_cn：然而有些推荐商品是用户以前看过的，我们称之为重定向推荐；有些系统专门展示这种推荐，例如Adobe Commerce和Oracle。

- move_code：PHENOMENON

- statement_status：author_inference

- why_here_cn：在通用推荐之后定义重定向推荐，形成核心对照对。

- inherits_from_previous_cn：与上一句‘通用推荐’共享同一推荐系统背景。

- changes_argument_state_cn：建立全文两个关键构念的并置。

- sets_up_next_cn：为下一段‘知道哪种推荐更好能增加销售’提供对象。

- failure_if_removed_cn：论文标题中的‘retargeted recommendation’没有定义。

### 4. Introduction P2 S1

- order：4

- locator：Introduction P2 S1

- paraphrase_cn：知道哪类推荐对用户更好并提供给他们，能够增加销售。

- move_code：PRACTICAL_STAKES

- statement_status：author_inference

- why_here_cn：在定义两个概念后立即说明研究为什么有商业价值。

- inherits_from_previous_cn：需要前一句已经定义两类推荐。

- changes_argument_state_cn：把概念区分升华为可变现的决策问题。

- sets_up_next_cn：为下一段‘两类推荐的相对价值随购买漏斗阶段变化’做铺垫。

- failure_if_removed_cn：读者不知道比较两类推荐有什么实际意义。

### 5. Introduction P3 S1

- order：5

- locator：Introduction P3 S1

- paraphrase_cn：重定向推荐与通用推荐的相对收益可能随用户在购买过程中的需求阶段（购买漏斗）而变化。

- move_code：MECHANISM

- statement_status：theory_claim

- why_here_cn：在商业价值之后提出关键调节变量：购买漏斗阶段。

- inherits_from_previous_cn：承接‘知道哪类更好能增加销售’的判断。

- changes_argument_state_cn：把两类推荐的比较从无条件差异变成条件差异。

- sets_up_next_cn：为下面两句分别解释通用推荐和重定向推荐在早/晚期的机制。

- failure_if_removed_cn：后文早期vs晚期的核心分样本设计失去理论引领。

### 6. Introduction P3 S2

- order：6

- locator：Introduction P3 S2

- paraphrase_cn：通用推荐在购买漏斗早期可能有用，因为它帮助用户从大量商品中发现自己想要的相关商品。

- move_code：MECHANISM

- statement_status：theory_claim

- why_here_cn：在提出阶段调节后，先解释通用推荐何时有用。

- inherits_from_previous_cn：承接上一句的阶段调节框架。

- changes_argument_state_cn：给‘早期’分配一个具体机制：发现。

- sets_up_next_cn：与下一句‘重定向推荐在晚期提醒’形成对照。

- failure_if_removed_cn：早期通用推荐有效的理论解释缺失。

### 7. Introduction P3 S3

- order：7

- locator：Introduction P3 S3

- paraphrase_cn：相反，重定向推荐在购买漏斗后期可能有用，因为此时用户偏好已经收窄，推荐可能提醒他们此前看过的商品。

- move_code：MECHANISM

- statement_status：theory_claim

- why_here_cn：在通用推荐机制之后给出重定向推荐的对称机制。

- inherits_from_previous_cn：与上一句通用推荐机制形成对照。

- changes_argument_state_cn：完成两类推荐在早/晚期的机制配对。

- sets_up_next_cn：为下一句‘提供更合适推荐能显著改善销售’做铺垫。

- failure_if_removed_cn：晚期重定向推荐有效的理论解释缺失。

### 8. Introduction P3 S4

- order：8

- locator：Introduction P3 S4

- paraphrase_cn：在合适的购买漏斗阶段给用户提供更合适的推荐能显著改善销售。

- move_code：PRACTICAL_STAKES

- statement_status：author_inference

- why_here_cn：在机制猜想后重申商业价值，强化研究动机。

- inherits_from_previous_cn：需要前两句的阶段机制。

- changes_argument_state_cn：把早/晚期机制猜想与销售收益绑定。

- sets_up_next_cn：为下一句‘但现有产品推荐研究缺乏指导’制造需求。

- failure_if_removed_cn：机制猜想似乎与实际问题脱节。

### 9. Introduction P3 S5

- order：9

- locator：Introduction P3 S5

- paraphrase_cn：然而，已有产品推荐研究几乎没有提供关于重定向推荐与通用推荐在不同购买漏斗阶段相对有效性的指导。

- move_code：GAP

- statement_status：author_inference

- why_here_cn：在机制与商业价值之后点出文献缺口。

- inherits_from_previous_cn：与上一句‘能显著改善销售’形成落差。

- changes_argument_state_cn：把现象和机制猜想转化为一个未被回答的问题。

- sets_up_next_cn：铺垫下一段‘展示广告文献也不能直接借用’。

- failure_if_removed_cn：论文缺少第一个文献缺口。

### 10. Introduction P4 S1

- order：10

- locator：Introduction P4 S1

- paraphrase_cn：展示广告文献虽然比较了通用与重定向广告对广告曝光转化率的影响，但其结论可能不适用于产品推荐情境。

- move_code：LIMITATION

- statement_status：prior_literature

- why_here_cn：在推荐文献缺口后引入相邻的重定向广告文献，说明不能从中借现成答案。

- inherits_from_previous_cn：延续‘缺少指导’的缺口，扩展到相邻文献。

- changes_argument_state_cn：把缺口从产品推荐文献扩大到展示广告文献的边界。

- sets_up_next_cn：为下一句解释为什么不适用做铺垫。

- failure_if_removed_cn：读者可能问：重定向广告已经研究过，为何还要做。

### 11. Introduction P4 S2

- order：11

- locator：Introduction P4 S2

- paraphrase_cn：通用或重定向广告通常在第三方网站展示，影响广告转化率；而推荐系统是在用户购物时于其他相关商品页展示商品，可能同时影响推荐商品的曝光次数和曝光条件下的购买概率。

- move_code：WHY_GAP_MATTERS

- statement_status：author_inference

- why_here_cn：直接说明重定向广告结论不能迁移到站内推荐的原因：渠道与机制不同。

- inherits_from_previous_cn：承接上一句‘结论可能不适用’。

- changes_argument_state_cn：确立站内推荐需要同时研究曝光量与转化率的特殊机制。

- sets_up_next_cn：为下一句‘没有研究考察推荐对曝光次数与转化率的影响’做理论准备。

- failure_if_removed_cn：跨文献迁移的障碍不清楚。

### 12. Introduction P4 S3

- order：12

- locator：Introduction P4 S3

- paraphrase_cn：据我们所知，还没有研究考察推荐对推荐商品曝光次数及其转化率的影响。

- move_code：GAP

- statement_status：author_inference

- why_here_cn：在前两句的铺垫后精确指出最具体的缺口。

- inherits_from_previous_cn：需要上一句的曝光/转化率机制。

- changes_argument_state_cn：形成本文的第二个、更细的缺口。

- sets_up_next_cn：为下一段三个研究问题提供来源。

- failure_if_removed_cn：两个缺口都失去最明确的核心表述。

### 13. Introduction P5 S1

- order：13

- locator：Introduction P5 S1

- paraphrase_cn：因此我们回答：(i)何时展示重定向推荐比通用推荐更有益，以及为什么；

- move_code：RQ_OR_OBJECTIVE

- statement_status：author_inference

- why_here_cn：在缺口后把问题显式化，这是引言的signposting。

- inherits_from_previous_cn：直接承接上一句的文献缺口。

- changes_argument_state_cn：把研究动机锁定为可回答的问题。

- sets_up_next_cn：与(ii)(iii)两个问题组成完整研究问题集。

- failure_if_removed_cn：缺少‘何时展示’的核心问题。

### 14. Introduction P5 S2

- order：14

- locator：Introduction P5 S2

- paraphrase_cn：(ii)重定向推荐与通用推荐的相对收益是否取决于消费者的情境因素（购买漏斗早期vs晚期）？

- move_code：RQ_OR_OBJECTIVE

- statement_status：author_inference

- why_here_cn：第二个问题明确调节变量，是研究设计的分样本依据。

- inherits_from_previous_cn：承接第一个问题‘何时’。

- changes_argument_state_cn：把购买漏斗阶段正式设为核心调节变量。

- sets_up_next_cn：与(iii)一起预告后续的实证内容。

- failure_if_removed_cn：后文早期/晚期分样本失去问题来源。

### 15. Introduction P5 S3

- order：15

- locator：Introduction P5 S3

- paraphrase_cn：(iii)在购买漏斗适当阶段选择性地展示重定向和通用推荐能带来多少销售增益？

- move_code：RQ_OR_OBJECTIVE

- statement_status：author_inference

- why_here_cn：第三个问题把前面的比较问题升华为经济量化问题。

- inherits_from_previous_cn：需要前两个问题的效应估计。

- changes_argument_state_cn：引出第6节反事实模拟。

- sets_up_next_cn：为‘用现场实验回答’建立直接衔接。

- failure_if_removed_cn：第6节模拟的规范目的缺少介绍性预告。

### 16. Introduction P6 S1

- order：16

- locator：Introduction P6 S1

- paraphrase_cn：我们在一家中型美国服装和家居零售商的网站上做现场实验来回答上述问题。

- move_code：STUDY_OVERVIEW

- statement_status：method_decision

- why_here_cn：在问题之后立即交代证据来源，保持引言连贯。

- inherits_from_previous_cn：直接回应三个研究问题。

- changes_argument_state_cn：把研究问题落实到一个具体现场。

- sets_up_next_cn：为下一句介绍处理/控制版本做铺垫。

- failure_if_removed_cn：读者不知道研究在哪里进行。

### 17. Introduction P6 S2

- order：17

- locator：Introduction P6 S2

- paraphrase_cn：访客被随机分配到两个版本：处理版在焦点商品页推荐四个相关商品，控制版隐藏推荐；过去会话看过推荐商品称为重定向推荐，没看过称为通用推荐。

- move_code：METHOD_JUSTIFICATION

- statement_status：method_decision

- why_here_cn：用一句紧凑的话交代随机实验、处理变量和核心构念的操作定义。

- inherits_from_previous_cn：需要上一句的现场实验。

- changes_argument_state_cn：把重定向/通用推荐从概念变成可测量变量。

- sets_up_next_cn：为下一句说明购买漏斗阶段的操作定义做铺垫。

- failure_if_removed_cn：后文Rec/ReTar两个变量没有操作性出处。

### 18. Introduction P6 S3

- order：18

- locator：Introduction P6 S3

- paraphrase_cn：沿用重定向广告文献的做法，我们把用户在某个产品品类加购之后（之前）的所有会话视为购买漏斗晚期（早期）。

- move_code：METHOD_JUSTIFICATION

- statement_status：method_decision

- why_here_cn：在操作定义重定向/通用后，再给关键调节变量一个可复制的定义。

- inherits_from_previous_cn：承接上一句的实验设计。

- changes_argument_state_cn：把‘购买漏斗阶段’从理论概念变成分析变量。

- sets_up_next_cn：为下一段报告结果建立方法论基础。

- failure_if_removed_cn：早期/晚期分样本缺少明确定义。

### 19. Introduction P7 S1

- order：19

- locator：Introduction P7 S1

- paraphrase_cn：我们发现两类推荐都会带来更多推荐商品曝光。

- move_code：RESULT

- statement_status：empirical_result

- why_here_cn：在方法概述后立刻给第一个结果，让读者知道研究有收获。

- inherits_from_previous_cn：需要前一段的实验设计。

- changes_argument_state_cn：建立‘曝光量增加’这一核心机制事实。

- sets_up_next_cn：为下一句对比转化率差异做铺垫。

- failure_if_removed_cn：曝光量这一核心发现缺失。

### 20. Introduction P7 S2

- order：20

- locator：Introduction P7 S2

- paraphrase_cn：但只有购买漏斗早期的通用推荐提高推荐商品转化率，重定向推荐在早晚期都不影响转化率。

- move_code：RESULT

- statement_status：empirical_result

- why_here_cn：在曝光结果后给出最不对称的转化率结果，这是全文最有信息量的发现。

- inherits_from_previous_cn：依赖上一句的曝光结果形成对比。

- changes_argument_state_cn：确立‘早期通用推荐特殊’这一关键结论。

- sets_up_next_cn：为下一句‘早期两类都提销售但通用更优，晚期只有重定向提销售’提供机制基础。

- failure_if_removed_cn：转化率这一最核心贡献消失。

### 21. Introduction P7 S3

- order：21

- locator：Introduction P7 S3

- paraphrase_cn：对于早期漏斗用户，两类推荐都提高推荐商品销售，但通用推荐效果更大；对于晚期漏斗用户，只有重定向推荐提高推荐商品销售，通用推荐无作用。

- move_code：RESULT

- statement_status：empirical_result

- why_here_cn：把曝光与转化率组件合成整体销售结果，给出管理者最关心的结论。

- inherits_from_previous_cn：需要前两句的曝光与转化率结果。

- changes_argument_state_cn：形成‘早期通用优、晚期重定向优’的对称结论。

- sets_up_next_cn：为下一段‘现场重定向推荐混有算法因素’做铺垫。

- failure_if_removed_cn：论文最核心的阶段化销售结论缺失。

### 22. Introduction P8 S1

- order：22

- locator：Introduction P8 S1

- paraphrase_cn：现场实验中的重定向推荐同时是用户以前看过的商品，也是推荐算法识别出的商品，因此更高销售可能来自重定向、算法或两者。

- move_code：LIMITATION

- statement_status：author_inference

- why_here_cn：在报告完现场结果后主动指出机制混淆，为MTurk实验铺路。

- inherits_from_previous_cn：需要前一句的‘晚期重定向提销售’结果。

- changes_argument_state_cn：把现场结果从结论降级为需要进一步解释的现象。

- sets_up_next_cn：为下一句介绍MTurk实验提供理由。

- failure_if_removed_cn：MTurk实验显得多余。

### 23. Introduction P8 S2

- order：23

- locator：Introduction P8 S2

- paraphrase_cn：我们在Amazon MTurk做了受控在线实验来拆解这个原因。

- move_code：STUDY_OVERVIEW

- statement_status：method_decision

- why_here_cn：在指出混淆后立即预告机制实验。

- inherits_from_previous_cn：承接上一句的机制不确定性。

- changes_argument_state_cn：把‘需要拆解’变成‘已有实验安排’。

- sets_up_next_cn：为下一句介绍实验操纵做铺垫。

- failure_if_removed_cn：第二个实验的出现没有引言层面的解释。

### 24. Introduction P8 S3

- order：24

- locator：Introduction P8 S3

- paraphrase_cn：在这个实验中，我们随机分配参与者看纯重定向商品（早期阶段看过但不由推荐算法识别的商品）或通用推荐商品；发现晚期漏斗参与者购买更多重定向商品。

- move_code：METHOD_JUSTIFICATION

- statement_status：empirical_result

- why_here_cn：用一句预告实验操纵和核心结果，让引言中的机制答案清楚可见。

- inherits_from_previous_cn：需要上一句的MTurk实验。

- changes_argument_state_cn：把‘重定向还是算法’的疑问变成有答案的机制判断。

- sets_up_next_cn：为下一句‘现场+在线一致说明是重定向效应’做总结。

- failure_if_removed_cn：机制分离的核心证据在引言中缺失。

### 25. Introduction P8 S4

- order：25

- locator：Introduction P8 S4

- paraphrase_cn：现场与在线实验的综合结果表明，晚期漏斗用户更多购买重定向推荐是因为重定向效应。

- move_code：CONTRIBUTION

- statement_status：author_inference

- why_here_cn：把两个实验的证据整合成一个机制结论。

- inherits_from_previous_cn：需要现场与在线两个结果。

- changes_argument_state_cn：机制主张从单个实验上升到跨实验结论。

- sets_up_next_cn：为下一段总销售分析做过渡。

- failure_if_removed_cn：机制结论缺乏整合性表述。

### 26. Introduction P9 S1

- order：26

- locator：Introduction P9 S1

- paraphrase_cn：虽然上述发现说明了两类推荐对推荐商品销售的相对收益，但总商品（焦点商品+推荐商品）销售在管理上更相关。

- move_code：STUDY_OVERVIEW

- statement_status：author_inference

- why_here_cn：在RP销售结论后引出一个更贴近管理者的问题：总销售。

- inherits_from_previous_cn：承接上一段RP销售结果。

- changes_argument_state_cn：把分析口径从RP销售升级为FP+RP总销售。

- sets_up_next_cn：为下一句‘高RP销售可能蚕食FP销售’做铺垫。

- failure_if_removed_cn：第5.3节总销售分析缺少引言预告。

### 27. Introduction P9 S2

- order：27

- locator：Introduction P9 S2

- paraphrase_cn：由于推荐商品属于焦点商品的子品类，更高的推荐商品销售可能蚕食焦点商品销售；因此我们估计焦点商品+推荐商品的总销售效应。

- move_code：WHY_GAP_MATTERS

- statement_status：author_inference

- why_here_cn：说明不能只看RP销售，必须检验渠道替代。

- inherits_from_previous_cn：承接上一句‘总销售更相关’。

- changes_argument_state_cn：把替代威胁设为需要排除的竞争假设。

- sets_up_next_cn：为下一句报告总销售结果做铺垫。

- failure_if_removed_cn：总销售分析的动机不清晰。

### 28. Introduction P9 S3

- order：28

- locator：Introduction P9 S3

- paraphrase_cn：与推荐商品销售结果类似，我们发现通用（重定向）推荐在购买漏斗早期（晚期）更有利于总商品销售。

- move_code：RESULT

- statement_status：empirical_result

- why_here_cn：给出总销售分析的核心结果，与RP销售结果形成一致性。

- inherits_from_previous_cn：需要上一句的替代威胁与总销售口径。

- changes_argument_state_cn：把阶段化结论推广到总销售。

- sets_up_next_cn：为下一句模拟收益做铺垫。

- failure_if_removed_cn：总销售结论缺失，渠道替代担忧未解除。

### 29. Introduction P9 S4

- order：29

- locator：Introduction P9 S4

- paraphrase_cn：我们模拟了替换现有重定向（通用）推荐后的反事实总销售，发现总销售最多可提高约3%。

- move_code：RESULT

- statement_status：empirical_result

- why_here_cn：用经济量化收束引言的主结果段。

- inherits_from_previous_cn：需要前一句的总销售效应。

- changes_argument_state_cn：把统计效应转成可操作的收益数字。

- sets_up_next_cn：为第6节模拟和第7节管理含义做预告。

- failure_if_removed_cn：模拟分析的销售增益缺失。

### 30. Introduction P10 S1

- order：30

- locator：Introduction P10 S1

- paraphrase_cn：我们的发现对IS文献中快速增长的推荐系统研究有贡献。

- move_code：CONTRIBUTION

- statement_status：contribution_claim

- why_here_cn：在结果预告后转入贡献声明。

- inherits_from_previous_cn：需要前面的全部结果。

- changes_argument_state_cn：把实证结果定位为对文献的贡献。

- sets_up_next_cn：为下面三点贡献列项做引导。

- failure_if_removed_cn：引言的贡献部分失去开场。

### 31. Introduction P10 S2

- order：31

- locator：Introduction P10 S2

- paraphrase_cn：第一，我们估计产品推荐的效果如何随访客情境因素变化，即用户是否看过推荐商品以及处于购买漏斗早期还是晚期。

- move_code：CONTRIBUTION

- statement_status：contribution_claim

- why_here_cn：第一点贡献直接呼应引言识别的缺口。

- inherits_from_previous_cn：承接上一句‘对推荐系统研究有贡献’。

- changes_argument_state_cn：正式声明情境因素贡献。

- sets_up_next_cn：为第二点贡献列项做过渡。

- failure_if_removed_cn：情境因素这一贡献主张缺失。

### 32. Introduction P10 S3

- order：32

- locator：Introduction P10 S3

- paraphrase_cn：第二，我们揭示了两类产品推荐在消费者不同购买过程阶段的相对收益。

- move_code：CONTRIBUTION

- statement_status：contribution_claim

- why_here_cn：第二点贡献强调‘比较两类推荐’这个核心创新。

- inherits_from_previous_cn：继续上一句的贡献列项。

- changes_argument_state_cn：把重定向vs通用比较定位为独立贡献。

- sets_up_next_cn：为第三点贡献做铺垫。

- failure_if_removed_cn：两类推荐比较的贡献声明缺失。

### 33. Introduction P10 S4

- order：33

- locator：Introduction P10 S4

- paraphrase_cn：第三，我们的发现与广泛使用的基于商品项的协同过滤推荐系统结合后能显著增加在线销售。

- move_code：CONTRIBUTION

- statement_status：contribution_claim

- why_here_cn：第三点贡献强调实践可落地性，使研究不只是统计效应。

- inherits_from_previous_cn：继续贡献列项并暗示第6节模拟。

- changes_argument_state_cn：把贡献升华为可复用的设计知识。

- sets_up_next_cn：结束引言，转入文献综述。

- failure_if_removed_cn：实践贡献缺失，引言收束不够有力。

## 引言逐段图谱

### 1. Introduction P1

- locator：Introduction P1

- paragraph_job_cn：定义两个核心构念（通用推荐与重定向推荐）并建立它们共存的电商推荐现象。

- opening_move_cn：以‘多数电商网站推荐相关商品’的普遍现象开场。

- development_move_cn：从协同过滤机制定义通用推荐，再转折到‘有时用户曾看过’定义重定向推荐，并给出商业系统实例。

- pivot_move_cn：‘然而’引出推荐也可能被用户看过，完成从技术推荐到用户视角重定向推荐的转折。

- closing_move_cn：以Adobe与Oracle系统专门展示重定向推荐结尾，暗示该现象有现实需求，制造下一段‘知道哪类更好’的需要。

### 2. Introduction P2

- locator：Introduction P2

- paragraph_job_cn：把两类推荐的区分升华为可增加销售的商业机会。

- opening_move_cn：单句段直接断言‘知道哪类更好并展示能增加销售’。

- development_move_cn：无，这是短过渡段。

- pivot_move_cn：无。

- closing_move_cn：以‘增加销售’收束，制造下一段解释‘何时更好’的需要。

### 3. Introduction P3

- locator：Introduction P3

- paragraph_job_cn：提出购买漏斗阶段作为调节变量的理论机制，并指出产品推荐文献没有回答这个问题。

- opening_move_cn：以‘相对收益可能随购买漏斗阶段变化’开启机制讨论。

- development_move_cn：分别给通用推荐早期发现机制和重定向推荐晚期提醒机制，并用‘提供更合适推荐可增加销售’强化实践性。

- pivot_move_cn：‘然而’从机制猜想转向文献缺口。

- closing_move_cn：以‘现有研究无指导’收束，为下一段展示广告文献边界制造需要。

### 4. Introduction P4

- locator：Introduction P4

- paragraph_job_cn：说明展示广告文献的重定向结论不能直接搬到站内推荐，并指出曝光量+转化率这一更细缺口。

- opening_move_cn：引入展示广告文献作为相邻领域。

- development_move_cn：指出重定向广告发生在第三方网站只影响广告转化率，而站内推荐影响曝光与转化两个路径。

- pivot_move_cn：‘相反’完成从广告到推荐的机制转折。

- closing_move_cn：以‘据我们所知没有研究考察曝光次数与转化率’收束，制造下一段研究问题的需要。

### 5. Introduction P5

- locator：Introduction P5

- paragraph_job_cn：把双重缺口转成三个显式研究问题。

- opening_move_cn：用‘因此我们回答下面问题’直接开启。

- development_move_cn：依次列出何时展示重定向推荐、是否受漏斗阶段调节、销售增益多大三个递进问题。

- pivot_move_cn：无，三个问题本身就是从条件到调节到量化的递进。

- closing_move_cn：以第三个问题‘多少销售增益’收束，为下一段现场实验方法制造需要。

### 6. Introduction P6

- locator：Introduction P6

- paragraph_job_cn：用一段预览现场实验设计和两个关键操作定义。

- opening_move_cn：以‘我们在一家零售网站做现场实验回答上述问题’开场。

- development_move_cn：说明随机分配处理/控制版本、四个推荐商品、重定向/通用定义，以及购买漏斗早晚期来自加购行为。

- pivot_move_cn：‘因此’从版本设计转入操作定义。

- closing_move_cn：以早晚期定义结尾，为下一段报告核心结果做铺垫。

### 7. Introduction P7

- locator：Introduction P7

- paragraph_job_cn：预告曝光量、转化率与推荐的销售结果，给出核心经验发现。

- opening_move_cn：以‘我们发现两类推荐都增加曝光’开启结果报告。

- development_move_cn：先报告转化率的不对称发现，再合成早/晚期的推荐商品销售结论。

- pivot_move_cn：‘然而’在曝光与转化率之间转折。

- closing_move_cn：以‘晚期只有重定向提销售’收束，制造下一段机制混淆的需要。

### 8. Introduction P8

- locator：Introduction P8

- paragraph_job_cn：指出现场实验的机制混淆并预告MTurk在线实验作为拆解方案。

- opening_move_cn：以现场重定向推荐同时包含重定向与算法两个因素开场。

- development_move_cn：说明随机展示纯重定向或通用推荐的设计，并报告晚期参与者更喜欢重定向商品。

- pivot_move_cn：‘为了拆解原因’从问题转向实验。

- closing_move_cn：以‘综合两个实验说明是重定向效应’收束，证明机制已识别。

### 9. Introduction P9

- locator：Introduction P9

- paragraph_job_cn：从推荐商品销售上升到总商品销售，排除渠道替代，并预告反事实模拟收益。

- opening_move_cn：以‘总销售在管理上更相关’开启。

- development_move_cn：指出RP可能蚕食FP，报告总销售仍呈早期通用优、晚期重定向优，并给出最高3%的模拟增益。

- pivot_move_cn：‘然而’或‘由于’完成从RP口径到总口径和模拟的转折。

- closing_move_cn：以‘最多提高约3%’收束，为讨论与贡献段制造需要。

### 10. Introduction P10

- locator：Introduction P10

- paragraph_job_cn：提前声明三点贡献，建立全文评价标准。

- opening_move_cn：以‘我们的发现对IS推荐系统研究有贡献’开场。

- development_move_cn：依次列出情境因素、两类推荐相对收益、与现有CF系统结合可增加销售三点贡献。

- pivot_move_cn：无，这是贡献列表的递进。

- closing_move_cn：以第三点贡献收束引言，转入文献综述。

## 理论到设计逐句图谱

### 1. Section 2.1.1 P1

- locator：Section 2.1.1 P1

- paraphrase_cn：推荐系统自1990年代起成为学术与产业的重要研究领域，按所用信息分为协同过滤、基于内容和混合三类。

- move_code：PRIOR_KNOWLEDGE

- statement_status：prior_literature

- why_here_cn：文献综述第一部分要先给出分类学，让读者知道后文的item-based CF属于哪一类。

- inherits_from_previous_cn：无，这是综述的开始。

- changes_argument_state_cn：建立推荐系统类型学基础。

- sets_up_next_cn：为下一句介绍CF内部类别做铺垫。

- failure_if_removed_cn：后文’基于商品项的CF’缺少分类背景。

### 2. Section 2.1.1 P2

- locator：Section 2.1.1 P2

- paraphrase_cn：协同过滤系统基于相似用户的过往偏好推荐商品，分为基于记忆（可再分基于用户和基于商品）和基于模型两类；基于内容的系统利用产品特征，混合系统结合两者但实施成本高。

- move_code：PRIOR_KNOWLEDGE

- statement_status：prior_literature

- why_here_cn：在分类后进一步说明CF是核心方法，且item-based是其中一种。

- inherits_from_previous_cn：承接上一句的三分类。

- changes_argument_state_cn：把研究对象锁定为item-based CF的算法逻辑。

- sets_up_next_cn：为下一句‘CF是最流行模型’提供依据。

- failure_if_removed_cn：读者不清楚通用推荐背后的算法来源。

### 3. Section 2.1.1 P3

- locator：Section 2.1.1 P3

- paraphrase_cn：基于CF的技术在实践中最为流行，因此多数学术研究都考察CF推荐系统。

- move_code：PRIOR_KNOWLEDGE

- statement_status：prior_literature

- why_here_cn：说明为什么论文聚焦CF系统，既有实践意义又有文献基础。

- inherits_from_previous_cn：需要上一句的CF分类。

- changes_argument_state_cn：把研究对象限定在CF推荐系统。

- sets_up_next_cn：为下一节‘经济价值’综述做桥梁。

- failure_if_removed_cn：全文为何围绕CF展开缺乏解释。

### 4. Section 2.1.2 P1

- locator：Section 2.1.2 P1

- paraphrase_cn：本领域已有研究发现推荐系统能增加商品销售，例如Lee和Hosanagar估计购买型CF提高浏览量0.5%、销售量5%，浏览型CF提高浏览量11%、销售量0.8%；Lee和Hosanagar(2021)发现平均提高浏览量15.3%、最终转化率7.5%。

- move_code：PRIOR_KNOWLEDGE

- statement_status：prior_literature

- why_here_cn：通过具体数字展示现有文献的‘平均效应’式研究，为后文指出它们忽略情境因素做基础。

- inherits_from_previous_cn：承接上一节CF是主流方法。

- changes_argument_state_cn：建立‘推荐系统平均效应已被研究’的共识。

- sets_up_next_cn：为下一句‘共览共购网络研究’做铺垫。

- failure_if_removed_cn：引言的‘平均效应已知’缺证据。

### 5. Section 2.1.2 P2

- locator：Section 2.1.2 P2

- paraphrase_cn：还有研究考察共览/共购关系对销售的影响，例如Oestreicher-Singer和Sundararajan发现共同购买关系可见性使互补品需求放大三倍，Kumar和Tan发现联合展示既增加FP销售也增加互补品溢出销售，Kumar和Hosanagar则发现替代品推荐会增加RP销售。

- move_code：PRIOR_KNOWLEDGE

- statement_status：prior_literature

- why_here_cn：展示产品网络和替代品推荐的相关研究，指出它们也是平均效应且主要关注产品特征。

- inherits_from_previous_cn：延续产品推荐经济价值综述。

- changes_argument_state_cn：把综述从平均效应扩展到产品网络效应。

- sets_up_next_cn：为下一句‘这些研究忽略访客情境因素’做铺垫。

- failure_if_removed_cn：曝光量/产品网络机制缺少文献来源。

### 6. Section 2.1.2 P3

- locator：Section 2.1.2 P3

- paraphrase_cn：尽管这些研究考察了推荐效果如何随产品特征变化，但它们基本忽略了推荐效果如何随访客情境因素变化，例如用户是否以前看过推荐商品或处于购买漏斗早期还是晚期。

- move_code：GAP

- statement_status：author_inference

- why_here_cn：在综述产品特征文献后直接指出其盲点，这是产品推荐文献的主要缺口。

- inherits_from_previous_cn：需要前面两段的实证综述。

- changes_argument_state_cn：正式建立研究缺口之一：情境因素。

- sets_up_next_cn：为下一句‘推荐网络可影响浏览与购买’做铺垫。

- failure_if_removed_cn：论文的核心创新点失去文献基础。

### 7. Section 2.1.2 P4

- locator：Section 2.1.2 P4

- paraphrase_cn：推荐系统在网站上形成互连产品网络，可增加RP的可见性和曝光次数；在FP页展示相关RP也可能提高曝光条件下的购买概率。

- move_code：MECHANISM

- statement_status：theory_claim

- why_here_cn：在指出缺口后给出本文结果分解的理论依据：曝光量和转化率两个机制。

- inherits_from_previous_cn：承接产品网络文献和缺口。

- changes_argument_state_cn：把销售效应分解为两个可估计机制。

- sets_up_next_cn：为下一句‘本文同时考察两个机制’做铺垫。

- failure_if_removed_cn：曝光量vs转化率分解缺少理论来源。

### 8. Section 2.1.2 P5

- locator：Section 2.1.2 P5

- paraphrase_cn：本文是首项在这样细粒度上同时检查两类推荐对曝光与转化率并区分购买漏斗阶段的研究。

- move_code：CONTRIBUTION

- statement_status：contribution_claim

- why_here_cn：在综述末尾声明首创性，保护新颖性。

- inherits_from_previous_cn：需要前面所有文献综述。

- changes_argument_state_cn：把本文定位为文献中的新增量。

- sets_up_next_cn：转入下一节重定向广告综述。

- failure_if_removed_cn：文献综述没有明确本文位置。

### 9. Section 2.2 P1

- locator：Section 2.2 P1

- paraphrase_cn：展示广告文献发现广告效果对不同购买漏斗阶段消费者有差异，广告重定向是一种利用跨网站浏览行为的流行方法。

- move_code：PRIOR_KNOWLEDGE

- statement_status：prior_literature

- why_here_cn：在介绍完产品推荐文献后引入重定向广告文献，作为‘重定向’概念来源。

- inherits_from_previous_cn：无直接依赖，属于相邻文献引入。

- changes_argument_state_cn：建立‘重定向’概念在广告领域的既有用法。

- sets_up_next_cn：为下一句‘这些研究只测广告转化率’做铺垫。

- failure_if_removed_cn：‘重定向推荐’的借词来源缺失。

### 10. Section 2.2 P2

- locator：Section 2.2 P2

- paraphrase_cn：重定向广告研究通过外生展示广告来检验广告曝光转化率，但产品推荐是在FP页展示且仍处于购物网站内，因此可能同时影响曝光与转化率，故必须分别检验两类推荐对曝光和购买概率的影响。

- move_code：WHY_GAP_MATTERS

- statement_status：author_inference

- why_here_cn：给出本文不能只借用重定向广告文献结果的核心原因。

- inherits_from_previous_cn：承接上一句的重定向广告综述。

- changes_argument_state_cn：确立站内推荐的机制边界：曝光+转化双通道。

- sets_up_next_cn：为下一节购买漏斗综述做铺垫。

- failure_if_removed_cn：跨文献迁移的必要性论证缺失。

### 11. Section 2.3 P1

- locator：Section 2.3 P1

- paraphrase_cn：消费者购买路径通常包含若干离散阶段，经典AIDA模型和广泛使用的‘知晓—考虑—购买’三阶段模型是基础。

- move_code：PRIOR_KNOWLEDGE

- statement_status：prior_literature

- why_here_cn：购买漏斗是本文核心调节变量，综述必须先给出漏斗概念来源。

- inherits_from_previous_cn：无直接依赖，是第三个文献流。

- changes_argument_state_cn：建立购买漏斗的理论背景。

- sets_up_next_cn：为下一句‘潜在状态建模’做铺垫。

- failure_if_removed_cn：早晚期阶段变量的理论依据缺失。

### 12. Section 2.3 P2

- locator：Section 2.3 P2

- paraphrase_cn：一条文献用隐马尔可夫模型等潜在状态刻画漏斗阶段。

- move_code：PRIOR_KNOWLEDGE

- statement_status：prior_literature

- why_here_cn：介绍一种处理漏斗的建模方法，与后文可观察代理方法形成对照。

- inherits_from_previous_cn：承接上一句的漏斗概念。

- changes_argument_state_cn：说明漏斗阶段可被当作潜在变量处理。

- sets_up_next_cn：为下一句引出可观察代理方法做对照。

- failure_if_removed_cn：后文为何不用HMM不够清晰。

### 13. Section 2.3 P3

- locator：Section 2.3 P3

- paraphrase_cn：另一条文献用可观察行为代理漏斗阶段，例如Bleier和Eisenbeiss区分信息、考虑和购买后状态，Sahni等区分浏览页、建购物车和购买阶段。

- move_code：PRIOR_KNOWLEDGE

- statement_status：prior_literature

- why_here_cn：引出与本文一致的可观察行为代理方法并给出权威引用。

- inherits_from_previous_cn：对照上一句潜在状态方法。

- changes_argument_state_cn：确立本文可采用行为代理的合法性。

- sets_up_next_cn：为下一句‘我们沿用第二流’做铺垫。

- failure_if_removed_cn：加购后为晚期的定义缺少文献支持。

### 14. Section 2.3 P4

- locator：Section 2.3 P4

- paraphrase_cn：沿用第二流文献，我们将用户在某一品类加购之后的会话视为购买漏斗晚期，加购之前视为早期。

- move_code：METHOD_JUSTIFICATION

- statement_status：method_decision

- why_here_cn：在综述末尾固定全文关键操作定义，为实验设计提供规则。

- inherits_from_previous_cn：直接承接上一句的可观察代理方法。

- changes_argument_state_cn：把理论上的漏斗阶段变成可测量变量。

- sets_up_next_cn：为第3章现场实验设计做方法论准备。

- failure_if_removed_cn：早晚期操作定义无根据。

## 制品设计理由逐句图谱

### 1. Section 3.1 P1

- locator：Section 3.1 P1

- paraphrase_cn：零售网站有超过35,000种商品，按品类和子品类组织，子品类主页显示缩略图；FP页显示四个RPs。

- move_code：DESIGN_FEATURE

- statement_status：fact

- why_here_cn：先交代网站结构，让读者知道推荐商品在页面的物理位置。

- inherits_from_previous_cn：承接第2章文献综述，进入现场。

- changes_argument_state_cn：建立FP/RP的页面分析单位。

- sets_up_next_cn：为下一节说明推荐算法规则做铺垫。

- failure_if_removed_cn：FP和RP的定义缺乏平台背景。

### 2. Section 3.2 P1

- locator：Section 3.2 P1

- paraphrase_cn：零售商使用IBM Coremetrics算法计算FP-RP亲和度，基于四种分数加权：共览、览后购、弃购后购、共购。

- move_code：DESIGN_FEATURE

- statement_status：fact

- why_here_cn：说明现场推荐系统是标准的item-based CF，为后文“系统可复用”主张提供事实基础。

- inherits_from_previous_cn：承接网站结构。

- changes_argument_state_cn：把推荐商品生成机制固定为可描述的算法。

- sets_up_next_cn：为下一句推荐规则与候选集做铺垫。

- failure_if_removed_cn：读者不知道现场推荐商品如何生成。

### 3. Section 3.2 P2

- locator：Section 3.2 P2

- paraphrase_cn：除亲和度外，系统只推荐FP子品类内的商品，使RPs成为替代品；系统每天计算并保存前15个高亲和度候选，页面只展示前4个。

- move_code：DESIGN_FEATURE

- statement_status：fact

- why_here_cn：说明两个关键设计约束：替代品属性与候选集规模，前者决定渠道替代分析，后者决定模拟替换来源。

- inherits_from_previous_cn：承接亲和度算法。

- changes_argument_state_cn：确立RPs为替代品且存在第5-15位候选可用于替换。

- sets_up_next_cn：为第3.3节曝光定义和机制预测做铺垫。

- failure_if_removed_cn：第5.3节替代威胁和第6节模拟都失去依据。

### 4. Section 3.3 P1

- locator：Section 3.3 P1

- paraphrase_cn：由于推荐系统从人群共览/共购推断RP与FP的关系，我们称之为通用推荐；像广告曝光一样，FP页面对RPs的展示称为RP曝光。

- move_code：CONSTRUCT_DEFINITION

- statement_status：author_inference

- why_here_cn：把概念定义与现场数据单位绑定。

- inherits_from_previous_cn：承接第2章的‘通用推荐’定义和第3.1节的FP页面结构。

- changes_argument_state_cn：把‘通用推荐’从构念变成可计数的‘曝光’。

- sets_up_next_cn：为下一句‘一次FP页浏览产生四个RP曝光’做铺垫。

- failure_if_removed_cn：RP曝光这一核心分析单位缺少定义。

### 5. Section 3.3 P2

- locator：Section 3.3 P2

- paraphrase_cn：因此一次FP页浏览对应四个RP曝光；根据用户过去是否看过这些RP，分别称为重定向或通用RP曝光。

- move_code：CONSTRUCT_DEFINITION

- statement_status：author_inference

- why_here_cn：给出全文最核心的数据组织方式：一次浏览=四条曝光，并按ReTar分型。

- inherits_from_previous_cn：需要上一句的曝光定义。

- changes_argument_state_cn：建立Rec和ReTar两个维度在曝光层面的交叉。

- sets_up_next_cn：为下一句控制组反事实论证做铺垫。

- failure_if_removed_cn：5.1.1.1的846,804条曝光无法理解。

### 6. Section 3.3 P3

- locator：Section 3.3 P3

- paraphrase_cn：即使FP页不显示RP，访客也可能通过搜索、相邻展示或其他工具知道FP与RP的关系，因此可能访问和购买RP。

- move_code：BENCHMARK_OR_CONTRAST

- statement_status：author_inference

- why_here_cn：说明隐藏推荐的对照组仍有意义，是处理效应的反事实基础。

- inherits_from_previous_cn：承接曝光定义，回应“控制组是否无推荐”的质疑。

- changes_argument_state_cn：把控制组定义为‘不显式显示但关系可知’的状态。

- sets_up_next_cn：为下一句‘显式展示有额外两个效应’做铺垫。

- failure_if_removed_cn：控制组的反事实效度不成立。

### 7. Section 3.3 P4

- locator：Section 3.3 P4

- paraphrase_cn：在FP页显式展示RP有两种额外作用：增加被发现的机会，以及帮助用户学习商品间的相似关系。

- move_code：MECHANISM

- statement_status：theory_claim

- why_here_cn：在控制组论证后给出处理组的两个机制，解释为什么显示推荐会改变购买。

- inherits_from_previous_cn：延续上一句的控制组对照逻辑。

- changes_argument_state_cn：把处理效应拆成发现和相似性学习两个机制。

- sets_up_next_cn：为下一句重定向推荐的额外机制做铺垫。

- failure_if_removed_cn：曝光量和转化率分解缺少行为机制。

### 8. Section 3.3 P5

- locator：Section 3.3 P5

- paraphrase_cn：重定向RP曝光与通用RP曝光不同，因为重复曝光能增加登记概率、发送相关性信号、帮助回忆以前探索过的商品、并表明用户看过该品类大部分商品。

- move_code：MECHANISM

- statement_status：theory_claim

- why_here_cn：给出重定向推荐独特的心理机制，解释为何它的效果可能不同于通用推荐。

- inherits_from_previous_cn：承接上一句显示推荐的两个效应。

- changes_argument_state_cn：为重定向vs通用差异提供理论解释。

- sets_up_next_cn：为下一句购买漏斗阶段调节做铺垫。

- failure_if_removed_cn：重定向推荐的差异化机制主张缺少依据。

### 9. Section 3.3 P6

- locator：Section 3.3 P6

- paraphrase_cn：除总体差异外，两类推荐的效果可能随购买漏斗阶段变化：早期偏好可塑，通用推荐更有帮助；后期偏好收窄，重定向推荐通过相关性信号或回忆更有帮助。

- move_code：MECHANISM

- statement_status：theory_claim

- why_here_cn：把重定向机制与漏斗阶段连接，形成可检验的阶段化预测。

- inherits_from_previous_cn：需要上一句的重复曝光机制。

- changes_argument_state_cn：完成‘阶段×推荐类型’的预测矩阵。

- sets_up_next_cn：为下一句‘用表1估计相对效应’做理论总结。

- failure_if_removed_cn：早期/晚期分样本预测失去机制支撑。

### 10. Section 3.3 P7

- locator：Section 3.3 P7

- paraphrase_cn：总之，我们预期两类推荐的效果取决于是否显示、用户是否看过以及购买漏斗阶段，并用表1的八格设计估计重定向推荐相对通用推荐的效应。

- move_code：HYPOTHESIS_OR_PROPOSITION

- statement_status：theory_claim

- why_here_cn：把前面的机制预测总结为可操作的实验矩阵。

- inherits_from_previous_cn：整合第3.3节的所有机制句。

- changes_argument_state_cn：把理论预测转成表1的统计对比。

- sets_up_next_cn：为下一节随机实验设计做逻辑准备。

- failure_if_removed_cn：表1失去了理论支柱。

### 11. Section 3.4 P1

- locator：Section 3.4 P1

- paraphrase_cn：网站创建两个版本：处理版在FP页显示四个RP，控制版隐藏；随机分配一半访客，并在后续会话保持一致版本。

- move_code：DESIGN_FEATURE

- statement_status：method_decision

- why_here_cn：这是现场实验的核心随机操纵，为因果识别提供基础。

- inherits_from_previous_cn：承接表1的八格设计。

- changes_argument_state_cn：建立Rec的外生性来源。

- sets_up_next_cn：为下一句购买漏斗阶段定义做铺垫。

- failure_if_removed_cn：Rec的因果解释不成立。

### 12. Section 3.4 P2

- locator：Section 3.4 P2

- paraphrase_cn：访客在某子品类开始浏览即进入该品类购买漏斗，加购后会话进入晚期，其他会话为早期。

- move_code：METHOD_JUSTIFICATION

- statement_status：method_decision

- why_here_cn：在随机设计后给出可复制的漏斗阶段定义。

- inherits_from_previous_cn：承接随机分配设计。

- changes_argument_state_cn：把早晚期从概念变为样本划分规则。

- sets_up_next_cn：为下一句‘数据可处于八种组合’做铺垫。

- failure_if_removed_cn：早期/晚期分样本无法执行。

### 13. Section 3.4 P3

- locator：Section 3.4 P3

- paraphrase_cn：现场设计有两个局限：重定向推荐同时是看过商品和算法推荐商品，且两类推荐非外生生成，可能因未观测因素产生偏差。

- move_code：LIMITATION

- statement_status：author_inference

- why_here_cn：在方法设计后主动暴露内置的识別弱点，为5.2节在线实验制造必要性。

- inherits_from_previous_cn：需要前两段的设计描述。

- changes_argument_state_cn：把现场估计降级为需要补充验证的结果。

- sets_up_next_cn：为下一句‘我们通过在线实验处理这些局限’做铺垫。

- failure_if_removed_cn：MTurk实验的引入没有方法论理由。

## Study开头、过渡与收束图谱

### 1. Section 4 P1; Section 5 P1; Section 5.1.1

- study_or_phase：第4章与5.1.1转化率分析

- locator：Section 4 P1; Section 5 P1; Section 5.1.1

- opening_function_cn：说明样本选择规则并建立曝光级数据集；用‘我们分两步估计’预告先分解后总销售的分析顺序。

- transition_role_cn：从数据描述自然进入第一个分析：RP销售分解的第一步是转化率。

- closure_function_cn：5.1.1.4以‘只有早期通用推荐提高转化率’收束，为下一步曝光量分析留下‘转化率之外的销售变化来自哪’的问题。

### 2. Section 5.1.2 P1-P3

- study_or_phase：5.1.2曝光量与日销售分析

- locator：Section 5.1.2 P1-P3

- opening_function_cn：以‘本节检查两类推荐对每日曝光量和销售的影响’开启，承接转化率分析缺掉的‘数量’组件。

- transition_role_cn：把RP销售拆成转化率×曝光量两个组件，5.1.2填补曝光量组件。

- closure_function_cn：5.1.2.4以‘曝光量驱动销售’和‘晚期只有重定向提销售’收束，并通过稳健性检验强化因果；为在线实验留下机制混淆问题。

### 3. Section 5.2 P1; Section 5.2.1 P1

- study_or_phase：5.2 MTurk在线实验

- locator：Section 5.2 P1; Section 5.2.1 P1

- opening_function_cn：以‘如3.4所述，我们设计在线实验解决现场局限’开场，直接回指现场设计的问题。

- transition_role_cn：把证据从真实平台切换到受控实验，分离重定向与算法。

- closure_function_cn：5.2.5以‘在线结果显示重定向本身驱动晚期销售且与亲和度无关’收束，完成机制验证；为总销售分析保留管理问题。

### 4. Section 5.3 P1

- study_or_phase：5.3总销售分析

- locator：Section 5.3 P1

- opening_function_cn：以‘用户可能用RP替换FP，管理上更应看总销售’开启，把分析口径从RP销售升级为FP+RP总销售。

- transition_role_cn：验证阶段化结论在总销售口径下仍成立，排除渠道替代。

- closure_function_cn：5.3末尾以‘表8结果与表6类似’收束，为量化政策收益的第6节模拟做铺垫。

### 5. Section 6 P1

- study_or_phase：第6节反事实模拟

- locator：Section 6 P1

- opening_function_cn：以‘我们进行模拟研究估计替换推荐带来的销售增益’开启，将前面的效应估计转化为政策收益。

- transition_role_cn：把‘推荐类型随阶段调整有用’变成‘具体替换策略值多少钱’。

- closure_function_cn：以‘替换第3-4位可获3.19%增益、替换全部前4位只有0.81%’收束，为讨论中的管理建议提供数字依据。

## 讨论与贡献逐句图谱

### 1. Section 7.1 P1 S1

- locator：Section 7.1 P1 S1

- paraphrase_cn：我们通过借用重定向广告文献中的‘重定向’概念，将‘重定向推荐’引入推荐文献。

- move_code：CONTRIBUTION

- statement_status：contribution_claim

- why_here_cn：讨论第一句直接声明概念贡献，呼应引言的双重缺口。

- inherits_from_previous_cn：需要全文结果作为基础。

- changes_argument_state_cn：把‘重定向推荐’确立为一个文献中的新构念。

- sets_up_next_cn：为下一句比较重定向广告与重定向推荐的机制差异做铺垫。

- failure_if_removed_cn：贡献的核心创新点丢失。

### 2. Section 7.1 P1 S2

- locator：Section 7.1 P1 S2

- paraphrase_cn：重定向在两种语境中相似，因为都指用户之前看过的广告或推荐；但重定向广告只影响广告转化率，重定向推荐可同时影响RP转化率和RP曝光次数。

- move_code：CONTRIBUTION

- statement_status：theory_claim

- why_here_cn：在同一句内完成‘借概念’与‘划边界’，防止读者误以为本文只是复制广告研究。

- inherits_from_previous_cn：承接上一句的概念引入。

- changes_argument_state_cn：区别本站推荐与第三方广告的机制边界。

- sets_up_next_cn：为下一句‘展示广告文献只能提供有限指导’做铺垫。

- failure_if_removed_cn：跨文献迁移的边界不清楚。

### 3. Section 7.1 P1 S3

- locator：Section 7.1 P1 S3

- paraphrase_cn：因此展示广告文献的发现只能为产品推荐提供有限指导；本研究可能是首项区分重定向与通用推荐并比较它们在用户通往推荐商品购买路径上相对效果的研究。

- move_code：CONTRIBUTION

- statement_status：contribution_claim

- why_here_cn：总结概念贡献并重申首创性。

- inherits_from_previous_cn：需要前两句的概念与边界论证。

- changes_argument_state_cn：正式确立本文在文献中的位置。

- sets_up_next_cn：为下一段机制层面的贡献做铺垫。

- failure_if_removed_cn：贡献声明缺少收束。

### 4. Section 7.1 P2 S1

- locator：Section 7.1 P2 S1

- paraphrase_cn：我们发现在购买漏斗早期通用推荐更有益，而重定向推荐在晚期更有效。

- move_code：CONTRIBUTION

- statement_status：empirical_result

- why_here_cn：机制讨论先重述核心实证发现，作为贡献的支柱。

- inherits_from_previous_cn：承接上一段的概念贡献。

- changes_argument_state_cn：把阶段化效应定位为主要实证贡献。

- sets_up_next_cn：为下一句解释机制做铺垫。

- failure_if_removed_cn：核心实证贡献缺失。

### 5. Section 7.1 P2 S2

- locator：Section 7.1 P2 S2

- paraphrase_cn：推荐销售增加的主要来源是推荐商品可见性提高，而非转化率提高，唯一例外是早期购买漏斗中的通用推荐。

- move_code：CONTRIBUTION

- statement_status：empirical_result

- why_here_cn：这一句话概括了全文最深刻的机制贡献：曝光量驱动而非转化率驱动。

- inherits_from_previous_cn：需要前一句的阶段化销售结果。

- changes_argument_state_cn：把‘曝光量vs转化率’确立为机制贡献。

- sets_up_next_cn：为下一句‘这些机制尚未被记录’做铺垫。

- failure_if_removed_cn：论文的机制灵魂缺失。

### 6. Section 7.1 P2 S3

- locator：Section 7.1 P2 S3

- paraphrase_cn：这些驱动（重定向/通用）推荐效应的底层机制尚未在现有文献中被记录。

- move_code：CONTRIBUTION

- statement_status：contribution_claim

- why_here_cn：用‘尚未被记录’强化新颖性，保护贡献。

- inherits_from_previous_cn：需要前一句的机制发现。

- changes_argument_state_cn：把机制发现与被引用文献区分开。

- sets_up_next_cn：为下一节管理含义做铺垫。

- failure_if_removed_cn：机制贡献的新颖性论证不足。

### 7. Section 7.2 P1 S1

- locator：Section 7.2 P1 S1

- paraphrase_cn：现有基于商品项的CF系统以共览共购为主要输入；我们的结果表明，考虑访客情境因素可以改进这些系统的表现。

- move_code：DESIGN_KNOWLEDGE

- statement_status：author_inference

- why_here_cn：管理含义从对现有系统的批评开始，为‘如何改进’做铺垫。

- inherits_from_previous_cn：承接7.1的机制贡献。

- changes_argument_state_cn：把理论发现转化为设计原则。

- sets_up_next_cn：为下一句具体替换策略做铺垫。

- failure_if_removed_cn：实践建议缺少系统背景。

### 8. Section 7.2 P1 S2

- locator：Section 7.2 P1 S2

- paraphrase_cn：零售商可以根据浏览历史推断漏斗阶段，并根据用户是否看过推荐商品把推荐分成重定向或通用；晚期用低排名重定向RP替换通用RP，早期相反。

- move_code：DESIGN_KNOWLEDGE

- statement_status：author_inference

- why_here_cn：给出可直接操作的设计规则：按阶段换推荐类型。

- inherits_from_previous_cn：承接上一句的情境因素改进建议。

- changes_argument_state_cn：把发现变成‘何时替换什么’的规则。

- sets_up_next_cn：为下一句模拟收益做铺垫。

- failure_if_removed_cn：设计知识没有具体操作形式。

### 9. Section 7.2 P2 S1

- locator：Section 7.2 P2 S1

- paraphrase_cn：模拟结果显示替换第3-4位符合资格的RP可带来更高的总销售；在这一策略中，正确类型带来的销售增加平均超过低亲和度带来的销售损失。

- move_code：DESIGN_KNOWLEDGE

- statement_status：empirical_result

- why_here_cn：用数字支撑设计规则，说明‘部分替换而非全部替换’的经济逻辑。

- inherits_from_previous_cn：需要上一段的具体替换策略和模拟结果。

- changes_argument_state_cn：把管理建议从定性判断升级为量化收益。

- sets_up_next_cn：为下一句‘零售商可计算净收益并决定是否执行’做铺垫。

- failure_if_removed_cn：设计建议失去经济证据。

### 10. Section 7.2 P2 S2

- locator：Section 7.2 P2 S2

- paraphrase_cn：零售商可以在每种情况下计算替换的净销售收益并决定是否采用该策略；也就是说，按案例替换而不是统一替换能实现更高销售。

- move_code：DESIGN_KNOWLEDGE

- statement_status：author_inference

- why_here_cn：把模拟结果概括为一条简单可执行的管理原则。

- inherits_from_previous_cn：承接上一句的模拟收益。

- changes_argument_state_cn：形成本文的可复用设计知识。

- sets_up_next_cn：为下一节普遍性边界做铺垫。

- failure_if_removed_cn：管理含义缺少可执行总结。

### 11. Section 7.3 P1 S1

- locator：Section 7.3 P1 S1

- paraphrase_cn：我们的发现适用于基于商品项的CF推荐系统，这是实践中最广泛使用的一类系统。

- move_code：BOUNDARY_CONDITION

- statement_status：author_inference

- why_here_cn：在给设计建议后明确结论适用范围。

- inherits_from_previous_cn：承接第3.2节现场算法和第5.2节在线算法。

- changes_argument_state_cn：把贡献限定在item-based CF。

- sets_up_next_cn：为下一句品类边界做铺垫。

- failure_if_removed_cn：结论可能被错误推广到所有推荐算法。

### 12. Section 7.3 P1 S2

- locator：Section 7.3 P1 S2

- paraphrase_cn：结果来自服装、配饰和家居类，这些占电商很大市场份额；在线实验用不同CF算法（Slope-One）得到相似结果，支持对其它item-based CF算法的推广。

- move_code：BOUNDARY_CONDITION

- statement_status：empirical_result

- why_here_cn：用外部效度证据说明边界内的普遍性。

- inherits_from_previous_cn：承接上一句的item-based CF限定。

- changes_argument_state_cn：把适用边界从单一算法扩展到同类算法。

- sets_up_next_cn：为下一句未来研究算法类别做铺垫。

- failure_if_removed_cn：普遍性主张缺少跨算法支持。

### 13. Section 7.3 P1 S3

- locator：Section 7.3 P1 S3

- paraphrase_cn：未来研究可以检验结论是否适用于其他类别算法，如基于模型的推荐算法。

- move_code：LIMITATION_AND_FUTURE

- statement_status：author_inference

- why_here_cn：在边界声明后自然延伸到未检验的算法类别。

- inherits_from_previous_cn：承接上一句的算法边界。

- changes_argument_state_cn：把未检验对象安排为未来研究。

- sets_up_next_cn：为下一节局限讨论做铺垫。

- failure_if_removed_cn：算法边界显得封闭。

### 14. Section 7.4 P1 S1

- locator：Section 7.4 P1 S1

- paraphrase_cn：现场实验中重定向和通用推荐不是外生生成的，可能使估计有偏；我们用了许多严格固定效应规范和多种安慰剂检验，并做了在线实验显示结果相似，但仍然提醒读者注意估计。

- move_code：LIMITATION_AND_FUTURE

- statement_status：author_inference

- why_here_cn：在最显眼的讨论位置诚实承认因果识别局限，建立可信度。

- inherits_from_previous_cn：承接第3.4节指出的现场局限。

- changes_argument_state_cn：把贡献强度适度下调，保护研究诚信。

- sets_up_next_cn：为下一句未来随机实验建议做铺垫。

- failure_if_removed_cn：论文会被认为过度宣称因果。

### 15. Section 7.4 P1 S2

- locator：Section 7.4 P1 S2

- paraphrase_cn：我们希望未来研究设计完全随机的实验来估计不同漏斗阶段中重定向/通用推荐的无偏效应。

- move_code：LIMITATION_AND_FUTURE

- statement_status：author_inference

- why_here_cn：把当前局限转化为可执行的研究议程。

- inherits_from_previous_cn：承接上一句的估计偏差提醒。

- changes_argument_state_cn：提出因果识别的升级方向。

- sets_up_next_cn：为下一句漏斗代理局限做铺垫。

- failure_if_removed_cn：缺少对现场局限的正面未来方向。

### 16. Section 7.4 P2 S1

- locator：Section 7.4 P2 S1

- paraphrase_cn：用可观察行为代理潜在漏斗阶段在现有研究中很常见，因为它能提供可操作的管理含义；但纳入潜在消费者状态是有趣的未来方向，未来可用更精确的漏斗模型。

- move_code：LIMITATION_AND_FUTURE

- statement_status：author_inference

- why_here_cn：承认漏斗阶段代理的局限，并给出潜在状态建模方向。

- inherits_from_previous_cn：承接上一段的漏斗代理定义。

- changes_argument_state_cn：把方法局限转化为未来建模机会。

- sets_up_next_cn：为下一句无条件于阶段的研究做铺垫。

- failure_if_removed_cn：漏斗阶段代理的局限未被讨论。

### 17. Section 7.4 P3 S1

- locator：Section 7.4 P3 S1

- paraphrase_cn：我们分别估计了早期和晚期漏斗中的相对收益；未来研究可以外生操纵漏斗阶段，探索不限定于阶段的效应。

- move_code：LIMITATION_AND_FUTURE

- statement_status：author_inference

- why_here_cn：最后一句给出终极的未来实验设计方向，结束全文。

- inherits_from_previous_cn：承接对漏斗阶段的讨论。

- changes_argument_state_cn：把阶段变量的内生性变成外部操纵的研究计划。

- sets_up_next_cn：无，这是全文最后一句。

- failure_if_removed_cn：文章的结尾缺少未来方向。

## Study累积逻辑

### 1. 1

- study_or_phase：现场实验转化率分析（5.1.1）

- evidence_job_cn：证明转化率这一机制组件在四类条件（推荐类型×漏斗阶段）下的不同表现。

- what_it_establishes_cn：显示推荐提高点击率但降低条件转化率；只有早期通用推荐显著提高总体转化率。

- what_it_cannot_establish_cn：不能说明销售总量变化，因为缺少曝光量组件；也不能区分重定向与算法亲和度。

- why_next_phase_is_needed_cn：销售=曝光量×转化率，仅转化率分析无法解释销售为何增加。

- transition_wording_function_cn：5.1.2开头用‘本节检查每日曝光和销售’转入第二个组件。

### 2. 2

- study_or_phase：现场实验曝光量与日销售分析（5.1.2）

- evidence_job_cn：证明推荐销售增加主要由曝光量驱动，并确立‘早期通用优、晚期重定向优’的销售模式。

- what_it_establishes_cn：两类推荐都显著提高每日曝光量；早期通用推荐销售更高，晚期只有重定向推荐显著提高销售；通过稳健性检验排除替代解释。

- what_it_cannot_establish_cn：现场重定向推荐非外生生成，且与算法推荐混在一起，不能确定机制是重定向本身。

- why_next_phase_is_needed_cn：机制问题仍开放：晚期重定向销售是来自重定向还是算法亲和度？

- transition_wording_function_cn：5.2开头回指3.4的两点局限，引出在线实验。

### 3. 3

- study_or_phase：MTurk在线实验（5.2）

- evidence_job_cn：用独立算法生成纯重定向与通用推荐，分离重定向效应与算法亲和度。

- what_it_establishes_cn：晚期漏斗中随机挑选的已浏览商品比算法选定的一般商品更常被购买；高/低相似度子样本结果相似，说明是重定向而非亲和度驱动。

- what_it_cannot_establish_cn：不是真实零售平台；购买规模小；漏斗阶段仍由参与者的自然加购行为决定而非外生操纵。

- why_next_phase_is_needed_cn：RP销售可能蚕食FP销售，管理者需要总销售口径。

- transition_wording_function_cn：5.3开头用‘管理上总销售更相关’转入总销售分析。

### 4. 4

- study_or_phase：总销售分析（5.3）

- evidence_job_cn：把阶段化结论从推荐商品销售推广到焦点商品+推荐商品总销售，排除渠道替代。

- what_it_establishes_cn：早期通用推荐显著提高FP+RP总销售，晚期重定向推荐显著提高总销售；结论与RP销售一致。

- what_it_cannot_establish_cn：不能量化‘按最优策略改动推荐系统’的实际销售增益。

- why_next_phase_is_needed_cn：管理者需要知道照做值多少钱。

- transition_wording_function_cn：第6节开头用‘模拟估计替换推荐带来的销售增益’转入反事实模拟。

### 5. 5

- study_or_phase：反事实模拟（6）

- evidence_job_cn：用推荐系统真实候选集把统计效应转化为可操作的替换策略及其销售增益。

- what_it_establishes_cn：替换第3-4位低排名候选可获得最高3.19%总销售增益；替换全部前4位只获0.81%，低亲和度损失抵消类型调整收益。

- what_it_cannot_establish_cn：模拟依赖Logit预测而非真实部署随机实验；未考虑用户对推荐变化的动态反应。

- why_next_phase_is_needed_cn：讨论与结论需要把模拟收益上升为设计原则和理论贡献。

- transition_wording_function_cn：讨论开头用‘我们引入重定向推荐概念’把证据链升级为贡献。

## 主张—证据台账

### 1. 展示推荐提高点击率

- claim_cn：展示推荐提高点击率

- claim_level：technical

- supporting_evidence_cn：表2模型自由证据与表4第(1)列回归结果，四种条件点击率系数都显著为正。

- support_strength：direct

- where_claim_is_made：5.1.1.2与5.1.1.4

- where_evidence_is_provided：Table 2; Table 4 Column (1)

### 2. 展示推荐降低条件转化率（除晚期重定向）

- claim_cn：展示推荐降低条件转化率（除晚期重定向）

- claim_level：technical

- supporting_evidence_cn：表2所有条件条件转化率差值都为负；表4第(2)列系数在大多数条件下为负。

- support_strength：direct

- where_claim_is_made：5.1.1.4

- where_evidence_is_provided：Table 2; Table 4 Column (2)

### 3. 只有早期购买漏斗中的通用推荐显著提高总体转化率

- claim_cn：只有早期购买漏斗中的通用推荐显著提高总体转化率

- claim_level：mechanism

- supporting_evidence_cn：表4第(3)列早期generic系数0.4008***，其他条件均不显著；表7在线实验早期generic转化率3.3567**。

- support_strength：direct

- where_claim_is_made：5.1.1.4; 5.2.4

- where_evidence_is_provided：Table 4 Column (3); Table 7

### 4. 两类推荐都增加推荐商品曝光量

- claim_cn：两类推荐都增加推荐商品曝光量

- claim_level：technical

- supporting_evidence_cn：表6每日曝光量四个条件都显著为正；表7在线实验RP曝光也显著。

- support_strength：direct

- where_claim_is_made：5.1.2.4; 5.2.4

- where_evidence_is_provided：Table 6; Table 7

### 5. 晚期购买漏斗中重定向推荐显著提高RP销售且优于通用推荐

- claim_cn：晚期购买漏斗中重定向推荐显著提高RP销售且优于通用推荐

- claim_level：mechanism

- supporting_evidence_cn：表6晚期重定向日销售0.0005**、与通用差异0.0004*；表7在线实验晚期重定向销售0.7320***、差异0.5361*。

- support_strength：direct

- where_claim_is_made：5.1.2.4; 5.2.4

- where_evidence_is_provided：Table 6; Table 7

### 6. 重定向推荐的晚期效果由重定向本身而非算法亲和度驱动

- claim_cn：重定向推荐的晚期效果由重定向本身而非算法亲和度驱动

- claim_level：mechanism

- supporting_evidence_cn：在线实验从已浏览商品中随机抽取重定向推荐，且高/低相似度子样本结果相似（附录I）。

- support_strength：partial

- where_claim_is_made：5.2.5

- where_evidence_is_provided：Section 5.2.5; Online Appendix I

### 7. 总销售结论与RP销售一致：早期通用优、晚期重定向优

- claim_cn：总销售结论与RP销售一致：早期通用优、晚期重定向优

- claim_level：technical

- supporting_evidence_cn：表8早期通用总销售0.0031***、晚期重定向总销售0.0019***。

- support_strength：direct

- where_claim_is_made：5.3

- where_evidence_is_provided：Table 8

### 8. 按漏斗阶段替换推荐可使总销售提高最多3.19%

- claim_cn：按漏斗阶段替换推荐可使总销售提高最多3.19%

- claim_level：design_knowledge

- supporting_evidence_cn：表9：替换第3-4位候选获得3.19%增益；替换全部前4位只有0.81%。

- support_strength：partial

- where_claim_is_made：6; 7.2

- where_evidence_is_provided：Table 9

### 9. 结果适用于基于商品项的协同过滤推荐系统

- claim_cn：结果适用于基于商品项的协同过滤推荐系统

- claim_level：boundary

- supporting_evidence_cn：现场采用IBM Coremetrics（item-based CF），在线实验采用Slope-One（另一item-based CF）得到定性一致结果。

- support_strength：partial

- where_claim_is_made：7.3

- where_evidence_is_provided：Section 3.2; Section 5.2.2; Table 7

## ISR定位逻辑

- constitutive_is_problem_cn：论文把‘推荐算法生成什么商品’这一技术问题改写为‘算法输出何时与用户过往行为和购买阶段匹配’的行为与决策问题：同一推荐系统在不同情境下产生不同的曝光与转化路径，因此价值不是算法平均性能而是情境匹配。

- technology_behavior_or_market_entanglement_cn：重定向推荐的存在依赖技术（协同过滤算法给出推荐）与行为（用户以前看过该商品）的纠缠；论文通过MTurk实验把两者拆开，证明晚期重定向推荐的价值来自行为侧的重定向信号而非算法侧的相似度，从而回答‘数字技术如何与用户历史共同塑造购买’。

- role_of_benchmark_or_objective_evidence_cn：隐藏推荐的对照组不是单纯无推荐基线，而是‘关系可知但不显式展示’的反事实；每日曝光面板中用同一天其他条件为零构造条件间对比；反事实模拟以不替换的原始销售为基线。这些客观证据支持的不是‘某算法分数更高’，而是‘推荐类型与漏斗阶段匹配才产生增量销售’。

- theory_in_design_cn：购买漏斗理论和重定向广告文献进入设计逻辑：加购后为晚期这一操作定义来自可观察行为代理文献；重定向推荐构念来自重定向广告文献；将销售分解为曝光量与转化率则来自产品网络文献。但推荐商品生成算法（Coremetrics、Slope-One）不是从本文理论推导的新算法，而是现成商品项CF，因此理论对设计的影响是部分而非直接。

- technical_vs_is_contribution_balance_cn：技术贡献很轻：没有提出新推荐算法；主要贡献在IS层面——区分推荐类型、识别情境调节、分解曝光与转化机制、并把结论翻译成现有CF系统上的替换策略。论文把技术算法当作可嵌入的背景基础设施，而非创新对象。

- beyond_transient_performance_cn：论文没有停留在‘某推荐效果更好’的暂时性表现上，而是给出机制解释（曝光量vs转化率、重定向信号vs算法亲和度）、跨算法可复制性（Coremetrics与Slope-One定性一致）、以及设计原则（替换第3-4位而不是全部替换以避免低亲和度损失），使贡献成为可迁移的设计知识。

## 段落级仿写模板

### abstract_steps

1. 第一句用‘虽然……但……’构造已知到未知的缺口，要求有被普遍接受的已知结论。

2. 第二句用‘我们用……实验’给出证据来源，要求有一个能操纵核心变量的研究设计。

3. 第三至四句给出结果变量的分解框架并说明分别估计，要求销售/效果可拆成至少两个组件。

4. 第五至六句按顺序报告最不对称的组件发现和整合后的总体发现，要求有可压缩的具体系数或方向。

5. 第七句用‘我们还做了……’报告机制实验，要求有一个能拆掉主要混淆的附加实验。

6. 第八句用‘反事实模拟显示……’量化经济收益，要求有条件于真实数据候选集的模拟。

7. 第九句用‘对……有启示’声明受众与贡献。

### introduction_paragraph_steps

1. 第一段：从普遍现象开场，定义一个熟悉构念，再转折定义新构念，要求新构念有工具或平台实例。

2. 第二段：用单句短段点出商业价值。

3. 第三段：提出一个调节变量并给两类对称机制，然后以‘然而’转到文献缺口，要求机制有足够的心理学/行为学推理。

4. 第四段：引入相邻领域，说明其结论不能直接迁移，并指出更细的机制缺口，要求相邻领域与本领域有明确渠道/机制差异。

5. 第五段：把缺口转成2-3个递进研究问题，要求问题之间有‘条件→调节→量化’的递进关系。

6. 第六段：用一段预告现场实验与关键操作定义，要求设计细节能用一个段落讲完。

7. 第七至九段：按与正文相同的顺序预告核心结果、机制实验、总销售与模拟，要求每个结果预告都有一句对应的‘为什么需要下一步’。

8. 第十段：提前声明三点贡献并使其分别呼应前面的缺口。

### theory_to_design_steps

1. 先用分类学综述建立研究对象（CF/item-based）的正当性，要求有算法类别和流行度证据。

2. 综述经济价值文献并给出具体效应量，最后指出平均效应背后的盲点。

3. 引入相邻领域（重定向广告）并明确其在本领域不可迁移的机制原因。

4. 综述调节变量的理论（购买漏斗）并选择一种可观察操作定义，要求有同类文献的代理方法。

5. 固定全文的关键操作定义，使后面的实验设计有算法式规则可依。

### method_and_study_sequence_steps

1. 先介绍平台结构，再介绍制品/系统如何生成（算法公式、业务规则、候选集）。

2. 给出核心分析单位的定义（如一次浏览=四条曝光）并论证控制组反事实的有效性。

3. 说明随机分配、阶段定义与版本一致性，然后主动列出设计局限，预告补救实验。

4. 数据描述要包含样本选择规则与平衡性证据，并用一个数字证明控制组不是空反事实。

### results_reporting_steps

1. 对每个结果先定义路径结构（点击率×条件转化率=总体转化率；销售=曝光量×转化率）。

2. 先给模型自由证据（均值差t检验），再给回归规范，再给系数表。

3. 识别讨论要分产品层面与访客层面，说明哪些混淆被固定效应吸收、哪些交互项可识别。

4. 稳健性检验要覆盖固定效应、样本子集、替代解释、安慰剂，并指向附录。

5. 机制实验要用独立算法把混淆变量拆开，并报告与主结果的一致性。

6. 政策/模拟分析要用真实候选集和模型选择（交叉验证）把效应换成钱。

### discussion_and_contribution_steps

1. 讨论第一句从相邻文献借概念并声明首创性，然后马上划清与相邻文献的边界。

2. 重述核心实证发现并把机制贡献落在一个清晰的‘不是A而是B’句上。

3. 管理建议要具体到‘对谁、怎么做、替换哪些位置’，并用模拟数字支撑。

4. 普遍性边界要限定算法类别与品类，并用跨算法一致的证据强化。

5. 局限与未来研究要承认因果识别的弱点，并给出随机实验、潜在状态建模等升级方向。

## 可执行写作算法

### 1. 1

- step：1

- rhetorical_job_cn：在引言建立两个对比构念并给出它们共享的算法背景。

- research_evidence_required_cn：需要推荐系统真实使用场景、两类推荐都能被定义的历史浏览数据或工具实例。

- sentence_pattern_function_cn：第一句描述普遍技术现象；第二句定义基线构念；第三句用‘然而/但是’转折定义对比构念。

- transition_condition_cn：当读者能区分两类推荐且知道它们在真实系统都存在时，进入下一步。

### 2. 2

- step：2

- rhetorical_job_cn：在引言给出调节变量及其双向机制，并指出双重文献缺口。

- research_evidence_required_cn：需要一个有理论来源的调节变量和一个不能直接用相邻文献答案的机制差异。

- sentence_pattern_function_cn：用‘可能取决于’引入调节，用两个‘因为’句给出对称机制，用‘然而’转缺口。

- transition_condition_cn：当机制预测与文献缺口形成清晰落差时，进入下一步。

### 3. 3

- step：3

- rhetorical_job_cn：把缺口转成三到四个递进研究问题，并预告实证设计。

- research_evidence_required_cn：需要至少一个能回答这些问题的现场/平台实验或可模拟的情境。

- sentence_pattern_function_cn：用‘因此我们回答’引出问题列表；随后用‘我们在……做现场实验’一句话预告设计。

- transition_condition_cn：当每个研究问题都能与后面的一个分析章节对应时，进入下一步。

### 4. 4

- step：4

- rhetorical_job_cn：在文献综述中分别处理主文献、相邻领域和调节变量的理论，并把操作定义固定下来。

- research_evidence_required_cn：需要主文献的具体效应量、相邻领域的边界论证、调节变量的代理方法文献。

- sentence_pattern_function_cn：先综述再在每小节末尾写‘尽管……但忽略了……’；最后一句固定‘我们沿用……将……视为……’。

- transition_condition_cn：当每个缺口都有文献引用支撑、操作定义可复制时，进入研究设计。

### 5. 5

- step：5

- rhetorical_job_cn：在研究设计部分描述平台、制品生成规则、核心分析单位和控制组反事实。

- research_evidence_required_cn：需要真实的平台结构、算法公式、候选集规则、以及能证明控制组不是空反事实的数字。

- sentence_pattern_function_cn：先用‘零售商使用……算法’讲制品，再用‘一次FP页浏览=四条RP曝光’定义分析单位，接着用‘即使不显示……也可能……’论证反事实。

- transition_condition_cn：当读者明白处理、重定向、阶段三个变量如何在数据中构造时，进入主分析。

### 6. 6

- step：6

- rhetorical_job_cn：在结果部分按‘路径分解→模型自由证据→回归→稳健性’的顺序报告主效应。

- research_evidence_required_cn：需要能够分解结果变量的路径（如点击率×条件转化率；曝光量×转化率）。

- sentence_pattern_function_cn：先定义路径，再用‘表X报告……’给模型自由证据，然后用固定效应回归给系数，最后用‘我们做了多重稳健性检验’收束。

- transition_condition_cn：当每个组件都有估计且总体销售可以用组件解释时，进入机制实验。

### 7. 7

- step：7

- rhetorical_job_cn：用一个受控实验把主实验中最强的混淆变量拆开，并报告跨实验一致性。

- research_evidence_required_cn：需要能独立生成两个对比条件的实验设计（如不同算法分别生成重定向与通用推荐）。

- sentence_pattern_function_cn：先回指主实验局限，再用‘我们随机显示……’讲操纵，最后用‘结果与现场一致’收束。

- transition_condition_cn：当机制主张有独立实验支持时，进入总销售或政策分析。

### 8. 8

- step：8

- rhetorical_job_cn：用总口径排除替代解释，并用反事实模拟把效应转成经济收益。

- research_evidence_required_cn：需要总销售数据、真实候选集排名与价格，以及经过交叉验证的预测模型。

- sentence_pattern_function_cn：先用‘管理上总销售更相关’转口径，再用‘我们模拟替换第X位候选’定义策略，最后报告增益百分比。

- transition_condition_cn：当政策收益有了数字支持时，进入讨论。

### 9. 9

- step：9

- rhetorical_job_cn：在讨论中依次完成概念贡献、机制贡献、设计知识、边界与局限。

- research_evidence_required_cn：需要能对应引言缺口的贡献陈述、可执行的管理建议、跨算法/跨品类证据以及诚实标注的局限。

- sentence_pattern_function_cn：第一句借概念并划边界；第二段用‘我们发现……主要原因是……而不是……’概括机制；随后用‘零售商可以……’给建议；用‘我们的发现适用于……’限边界；最后用‘未来研究可以……’收束。

- transition_condition_cn：当贡献与引言缺口一一对应、且局限被如实说明时，全文完成。

## 应模仿的高价值动作

1. 把相邻领域的‘重定向’概念借入产品推荐并立即用‘广告只影响转化率、推荐还影响曝光量’划清边界，既获得概念新颖性又获得机制特殊性。

2. 用‘销售=曝光量×转化率’的事实分解把黑箱打开，使每个后续实验结果都能归到某一具体组件。

3. 在引言中按正文相同顺序预告结果、机制实验、总销售与模拟，使读者一进引言就握有全文路线图。

4. 在每阶段结尾主动声明‘尚未解决的不确定性’，用它作为下一研究的过渡理由。

5. 在线实验用独立算法分别生成重定向与通用推荐，把现场实验中纠缠的重定向效应与算法亲和度拆开，是机制验证的高价值操作。

6. 用对称机制句（早期偏好可塑→通用发现；晚期偏好收窄→重定向提醒）给调节变量提供可理解的行为解释。

7. 反事实模拟用真实候选集和多种替换策略作梯度对照，并解释‘为什么不是全部替换而是第3-4位’，使设计知识可操作。

## 不要只复制的表面动作

1. 不要只写‘首次区分重定向与通用推荐’却没有真实历史浏览数据或干净的算法分离设计。

2. 不要在没有真实推荐候选排名的情况下做反事实模拟并宣称3%收益。

3. 不要把隐藏推荐的控制组当作完全无推荐；必须先论证用户可能通过搜索/相邻展示知道FP-RP关系。

4. 不要在没有随机分配或固定效应识别论证的情况下复制‘交互项系数可识别’的说法。

5. 不要把在线小规模实验的定性一致直接当作现场估计完全无偏的证据；应在局限中如实承认。

6. 不要模仿‘我们分两步’却不提前告诉读者两步分别是什么。

## 证据薄弱或跳跃的动作

1. 将‘曝光量增加’解释为销售增长的主要驱动时，曝光量作为‘被显示次数’与处理本身高度机械相关，二者之间存在近乎定义性的关联；作者未充分讨论这一机械性程度。

2. 把现场与在线实验的定性一致解读为对现场内生性问题的‘支持’仍属较弱推断，作者在7.4也承认不能完全消除，贡献强度应低于直接外生实验。

3. 将服装/家居一个品类的结果外推到整个基于商品项CF领域，主要靠现场与在线两个平台和两种算法的相似性，边界仍较窄。

4. 模拟中的3.19%销售增益来自Logit模型预测的反事实概率，而非真实部署；作者没有讨论用户看到新推荐后的动态重复访询或学习效应可能改变收益。

5. 在线实验的漏斗阶段仍由参与者在第一阶段是否加购自然形成，并非外生操纵，因此对阶段调节的因果表述有限。

## 一句话套路

把相邻领域的‘重定向’概念借进站内产品推荐，用真实零售网站随机现场实验把销售分解为曝光量与转化率，再用独立算法的在线实验拆掉机制混淆，最后用反事实模拟把统计效应换算成可操作的销售增益，从而把技术算法问题写成一个关于数字技术与人机情境匹配的IS研究。

## 分析边界

分析基于用户提供的全文Markdown文本；Online Appendices D-J只被正文引用而未在本文中展开，涉及附录的稳健性细节和具体系数只能依据正文描述推断；全文未提供PDF页码，位置证据以章节、段落和表格标识；表格中少量OCR字符（如RPPur_1等下标）不影响论证理解。
