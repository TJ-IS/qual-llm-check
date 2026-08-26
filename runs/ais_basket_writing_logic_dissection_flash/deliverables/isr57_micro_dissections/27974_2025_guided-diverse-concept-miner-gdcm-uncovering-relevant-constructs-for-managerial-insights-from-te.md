# Guided Diverse Concept Miner (GDCM): Uncovering Relevant Constructs for Managerial Insights from Text：ISR 句段级微观图谱

- 作者：Dokyun “DK” Lee; Zhaoqi “ZQ” Cheng; Chengfeng Mao; Emaad Manzoor
- 年份：2025
- DOI：10.1287/isre.2020.0494
- 源文件：27974_2025_guided-diverse-concept-miner-gdcm-uncovering-relevant-constructs-for-managerial-insights-from-te.md
- 置信度：0.74

## 核实后的宏观骨架

全文结构：摘要先给出GDCM的三个自动目标、技术机制和两个外部验证；引言从企业文本分析的现实压力出发，提出可解释、多样、相关三个要求，用2x2图把现有方法分类并定位Quadrant II缺口，再从概念理论提炼四条标准并转成三个desiderata，预告评价场景；第2节分别展开概念理论、商业主题算法、可解释机器学习三类文献，并给出理论到设计的映射；第3节构造在线零售决策旅程数据并指出现有guided exploration方法在多样性上的失败；第4节给出模型结构和四项loss，并把理论标准逐一翻译成损失函数；第5节按三个desiderata分别评价：人类判断与coherence证明可解释性，Garvin维度召回和未知概念覆盖证明多样性，预测AUC、概念系数与外部因果研究对比证明相关性，再以Y敏感性和消融做稳健性，附录A补充TopicGPT对比；第6节给出管理与研究含义并把工具定位为探索性、非因果；第7节一句话总结。

## 摘要逐句图谱

### 1. Abstract S1

- order：1

- locator：Abstract S1

- paraphrase_cn：GDCM是解释型深度学习算法，能自动从文本中抽取语料级概念、筛选出与用户指定的管理结果强相关的概念，并量化概念对该结果的相对相关重要性。

- move_code：问题与制品总述

- statement_status：contribution_claim

- why_here_cn：摘要必须在第一句就让读者知道提出什么算法、解决什么任务、输出什么。

- inherits_from_previous_cn：无前句；直接借用标题中的三个关键词。

- changes_argument_state_cn：把标题名称展开为一个完整的三重任务定义。

- sets_up_next_cn：引出后文对“无预定义、与结果相关”的强调。

- failure_if_removed_cn：读者不知道算法要解决什么问题。

- evidence_pointer：Abstract

### 2. Abstract S2

- order：2

- locator：Abstract S2

- paraphrase_cn：GDCM在不需要任何预先定义的概念或标注数据的情况下，探索并提取可能解释该管理结果的未知概念。

- move_code：方法优势声明

- statement_status：contribution_claim

- why_here_cn：需要强调与human-tagging和seeded方法的核心差异：没有先验概念要求。

- inherits_from_previous_cn：承接第一句中的“用户指定结果”和“概念”，进一步限定使用条件。

- changes_argument_state_cn：把任务从普通概念挖掘升格为无监督但受Y引导的guided exploration。

- sets_up_next_cn：为下一句的共享向量空间设计提供动机。

- failure_if_removed_cn：丢失了文章最重要的差异化条件，读者会误以为需要标签。

- evidence_pointer：Abstract

### 3. Abstract S3

- order：3

- locator：Abstract S3

- paraphrase_cn：GDCM把词、文档、概念嵌入同一个向量空间，从而能用概念向量附近的词解释概念。

- move_code：技术机制一：同空间嵌入

- statement_status：design_decision

- why_here_cn：在摘要中给出最关键的技术选择，因为这同时支撑可解释性和多样性。

- inherits_from_previous_cn：承接“不需要预定义概念”，说明没有标签时如何让概念可解释。

- changes_argument_state_cn：从“用什么任务”推进到“技术上怎么做”。

- sets_up_next_cn：为下一句的diversity/coherence/relevance配置作铺垫。

- failure_if_removed_cn：摘要缺少让读者判断方法本质的唯一关键技术信息。

- evidence_pointer：Abstract

### 4. Abstract S4

- order：4

- locator：Abstract S4

- paraphrase_cn：GDCM被显式配置为提升概念多样性、连贯性和与管理结果的相关性。

- move_code：技术机制二：三个目标配置

- statement_status：design_decision

- why_here_cn：把三个desiderata作为方法目标写进摘要，为后文的评价框架埋钩。

- inherits_from_previous_cn：在共享空间中“解释”的基础上加入多样性、相关性目标。

- changes_argument_state_cn：把设计目标明确为三元：interpretability、diversity、relevance。

- sets_up_next_cn：直接引出下一句用于演示的在线购买旅程案例。

- failure_if_removed_cn：摘要缺失评价与贡献的组织原则。

- evidence_pointer：Abstract

### 5. Abstract S5

- order：5

- locator：Abstract S5

- paraphrase_cn：作者用一个与已读评论相关的在线购买旅程数据的假设管理案例来演示GDCM。

- move_code：评价场景引入

- statement_status：method_decision

- why_here_cn：让抽象的算法主张落在具体真实数据场景上，增加可信度。

- inherits_from_previous_cn：把三个配置目标放到一个管理案例里检验。

- changes_argument_state_cn：从方法陈述转入证据层面。

- sets_up_next_cn：下一句给出在该场景中的核心结果。

- failure_if_removed_cn：评价主张没有锚点。

- evidence_pointer：Abstract

### 6. Abstract S6

- order：6

- locator：Abstract S6

- paraphrase_cn：GDCM能规模化地抽取评论中与转化高度相关的隐藏概念，并给出概念相对产品评分的重要性。

- move_code：主要结果

- statement_status：empirical_result

- why_here_cn：在摘要内展示最核心的直接结果：概念确实与Y相关且可以量化比较。

- inherits_from_previous_cn：承接决策旅程案例，报告转化场景中的输出形式。

- changes_argument_state_cn：从“提出方法”推进到“方法有效”。

- sets_up_next_cn：为下一句的外部效度证据做铺垫。

- failure_if_removed_cn：摘要只有承诺没有结果。

- evidence_pointer：Abstract

### 7. Abstract S7

- order：7

- locator：Abstract S7

- paraphrase_cn：这些概念恰是文献中已被理论化的产品品质概念，且GDCM给出的相关重要性与此前同一情境下的因果研究估计接近，构成外部验证。

- move_code：外部效度声明

- statement_status：empirical_result

- why_here_cn：这句是摘要的高潮：把发现的“概念”锚定到已有理论和因果证据，防止读者认为只是词语聚类。

- inherits_from_previous_cn：直接利用第六句中的概念和重要性估计。

- changes_argument_state_cn：把结果从“相关”提升为“与既有理论/因果一致”，为贡献提供外部锚。

- sets_up_next_cn：引出最后关于Y敏感性的灵活性声明。

- failure_if_removed_cn：贡献失去外部效度和理论意义。

- evidence_pointer：Abstract

### 8. Abstract S8

- order：8

- locator：Abstract S8

- paraphrase_cn：用其他数据做的实验显示，抽取的洞察会随着引导性管理变量而合理变化，进一步证明GDCM作为管理工具的灵活性。

- move_code：普适性与灵活性声明

- statement_status：empirical_result

- why_here_cn：补充Y敏感性证据，说明方法不是为单一Y定制。

- inherits_from_previous_cn：在外部效度之后，再展示另一个数据上的迁移证据。

- changes_argument_state_cn：把贡献从单一场景推广到“可针对不同管理变量”。

- sets_up_next_cn：没有后文需求，摘要收束。

- failure_if_removed_cn：方法显得只适配转化这一种Y。

- evidence_pointer：Abstract

## 引言逐句图谱

### 1. Introduction P1 S1

- order：1

- locator：Introduction P1 S1

- paraphrase_cn：企业越来越依赖文本数据分析来辅助战略决策。

- move_code：现实背景

- statement_status：fact

- why_here_cn：引言第一句必须在公共地平线上建立主题重要性。

- inherits_from_previous_cn：无。

- changes_argument_state_cn：把文章话题引入信息系统的决策支持语境。

- sets_up_next_cn：下一句需要说明文本数据量大带来的问题。

- failure_if_removed_cn：文章没有现实开篇，直接进入技术会显得突兀。

- evidence_pointer：Section 1 P1

### 2. Introduction P1 S2

- order：2

- locator：Introduction P1 S2

- paraphrase_cn：文本数据的海量性质带来认知负担，需要计算化地把原始文本转成管理者能理解的概念。

- move_code：现实压力

- statement_status：author_inference

- why_here_cn：在重要性之间建立“需要算法转换”的逻辑桥梁。

- inherits_from_previous_cn：承接第一句的企业依赖文本分析。

- changes_argument_state_cn：从“文本有用”推进到“需要概念化”。

- sets_up_next_cn：下一句自然提出“概念须与结果相关”。

- failure_if_removed_cn：没有“认知挑战”则为什么要自动化概念挖掘就不清楚。

- evidence_pointer：Section 1 P1

### 3. Introduction P1 S3

- order：3

- locator：Introduction P1 S3

- paraphrase_cn：被识别的概念必须与管理结果变量强相关。

- move_code：需求一：相关性

- statement_status：author_inference

- why_here_cn：在概念化的需求上立即加上“相关性”限定，为三desiderata开篇。

- inherits_from_previous_cn：承接管理者需要可行动洞察。

- changes_argument_state_cn：从“任何概念”收窄为“与Y相关的概念”。

- sets_up_next_cn：下一句加入多样性，使需求列表成型。

- failure_if_removed_cn：文章提出的核心指导变量Y失去铺垫。

- evidence_pointer：Section 1 P1

### 4. Introduction P1 S4

- order：4

- locator：Introduction P1 S4

- paraphrase_cn：概念多样性对发现未知构念、增强理解和生成创新假设至关重要。

- move_code：需求二：多样性

- statement_status：author_inference

- why_here_cn：与相关性并列，把“发现未知”设为另一条核心需求，刻意区别于单纯预测模型。

- inherits_from_previous_cn：从相关性需求继续补充。

- changes_argument_state_cn：形成两个需求：相关 + 多样。

- sets_up_next_cn：为第二段三要求中的interpretability作铺垫。

- failure_if_removed_cn：多样性作为本文区分性主张在引言阶段就消失。

- evidence_pointer：Section 1 P1

### 5. Introduction P2 S1

- order：5

- locator：Introduction P2 S1

- paraphrase_cn：本文提出一个新文本探索算法GDCM，并给出脚注指向代码仓库。

- move_code：提出同名制品

- statement_status：contribution_claim

- why_here_cn：第二段开头必须点明本文的制品名称。

- inherits_from_previous_cn：直接回应用前两句提出的需求和压力。

- changes_argument_state_cn：从问题世界切换到解决方案世界。

- sets_up_next_cn：下一句用三个要求解释算法目标。

- failure_if_removed_cn：论文没有明确提出自己的制品。

- evidence_pointer：Section 1 P2

### 6. Introduction P2 S2

- order：6

- locator：Introduction P2 S2

- paraphrase_cn：GDCM基于三个关键要求：可解释性、发现多样概念的能力、与管理结果相关的强预测能力。

- move_code：三要求总述

- statement_status：design_decision

- why_here_cn：这是全文的组织锚：可解释、多样、相关三词将驱动理论、设计和评价三部分。

- inherits_from_previous_cn：把第一段的“相关性、多样性”扩展为三要求，并加上可解释性。

- changes_argument_state_cn：确立三个desiderata为算法与论文的验收标准。

- sets_up_next_cn：引出第三段的“概念理论”来支撑这三个要求。

- failure_if_removed_cn：理论到设计的整个链条失去支点。

- evidence_pointer：Section 1 P2

### 7. Introduction P3 S1

- order：7

- locator：Introduction P3 S1

- paraphrase_cn：为了明确文本洞察的目标，作者把概念当作基于概念理论的目标构念。

- move_code：引入哲学定位

- statement_status：theory_claim

- why_here_cn：在提出要求后立即给出理论来源，避免用词浮在工程层。

- inherits_from_previous_cn：承接“可解释且相关的概念”这一需要定义的概念。

- changes_argument_state_cn：把“概念”从日常词汇提升为理论术语。

- sets_up_next_cn：下一句引用“概念是思想积木”，支撑理论选择。

- failure_if_removed_cn：后文原型理论的出现会没有入口。

- evidence_pointer：Section 1 P3

### 8. Introduction P3 S2

- order：8

- locator：Introduction P3 S2

- paraphrase_cn：按定义，概念是思想的基础构件，构成知识并帮助我们理解和行动。

- move_code：概念重要性引用

- statement_status：prior_literature

- why_here_cn：引用标准哲学定义，把本文工作与认知科学传统绑定。

- inherits_from_previous_cn：支持上一句中“概念理论”的用语。

- changes_argument_state_cn：解释了为什么概念是值得自动挖掘的对象。

- sets_up_next_cn：下一句从管理者/研究者需求转到GDCM设计宗旨。

- failure_if_removed_cn：概念理论显得是装饰而不是动机来源。

- evidence_pointer：Section 1 P3

### 9. Introduction P3 S3

- order：9

- locator：Introduction P3 S3

- paraphrase_cn：因此作者从零开始构建GDCM，使其识别符合概念理论定义的表征。

- move_code：理论驱动声明

- statement_status：design_decision

- why_here_cn：把理论直接转化为设计目标，预告后文理论不是事后解释。

- inherits_from_previous_cn：利用概念理论的重要性推演出设计原则。

- changes_argument_state_cn：明确GDCM与普通主题模型的区别：有理论根基。

- sets_up_next_cn：为第2节原型理论的出现和四条标准作铺垫。

- failure_if_removed_cn：文章的理论贡献会在引言中丢失。

- evidence_pointer：Section 1 P3

### 10. Introduction P4 S1

- order：10

- locator：Introduction P4 S1

- paraphrase_cn：图1按探索vs提取和引导vs非引导两个维度对现有概念挖掘技术分类，并标出GDCM的位置。

- move_code：分类框架建立

- statement_status：author_inference

- why_here_cn：用一个2x2图在几段内把整个相关方法领域结构清楚，这是定位逻辑最经济的办法。

- inherits_from_previous_cn：承接第二段提出的算法，说明它在方法版图中的位置。

- changes_argument_state_cn：建立四个象限，为Quadrant II留出专门缺口。

- sets_up_next_cn：下一句开始逐象限解释管理任务。

- failure_if_removed_cn：Gap构造没有地图，后面的Quadrant II空白无从谈起。

- evidence_pointer：Section 1 P4 and Figure 1

### 11. Introduction P4 S2–S5

- order：11

- locator：Introduction P4 S2–S5

- paraphrase_cn：有经验的管理者想验证预定概念；另一些管理者想规模化抽取已知概念；进入新领域的管理者想探索显性概念；而想知道哪些评论概念与转换相关时，可用Quadrant II的guided exploration方法。

- move_code：象限任务描述

- statement_status：author_inference

- why_here_cn：通过不同的管理需求逐象限说明，最后把焦点引到Quadrant II。

- inherits_from_previous_cn：直接使用图1的四象限分类。

- changes_argument_state_cn：把坐标轴翻译成实际管理任务，为后面的缺口定位。

- sets_up_next_cn：下一句给出Quadrant II方法的问题。

- failure_if_removed_cn：缺乏为什么聚焦Quadrant II的动机。

- evidence_pointer：Section 1 P4

### 12. Introduction P4 S6

- order：12

- locator：Introduction P4 S6

- paraphrase_cn：Quadrant II现有方法，如黑箱深度学习优先预测而非解释，主题模型变体没有显式优化多样性和连贯性。

- move_code：文献缺口

- statement_status：author_inference

- why_here_cn：这是引言第一次正式打开缺口：现有guided exploration不满足三要求。

- inherits_from_previous_cn：承接上句对Quadrant II的聚焦。

- changes_argument_state_cn：从“有方法”转为“方法不满足desiderata”。

- sets_up_next_cn：为第五段GDCM补缺口的声明提供逻辑需要。

- failure_if_removed_cn：GDCM的存在理由消失。

- evidence_pointer：Section 1 P4

### 13. Introduction P5 S1

- order：13

- locator：Introduction P5 S1

- paraphrase_cn：GDCM是一个落在图1第二象限的可解释深度学习算法。

- move_code：定位复述

- statement_status：design_decision

- why_here_cn：把算法放回分类图，明确它就是用来填Quadrant II缺口的。

- inherits_from_previous_cn：承接上一句的Quadrant II缺口。

- changes_argument_state_cn：完成“缺口—解决方案”配对。

- sets_up_next_cn：下一句引出理论根基来支撑算法定位。

- failure_if_removed_cn：算法没有在方法地图中的坐标。

- evidence_pointer：Section 1 P5

### 14. Introduction P5 S2

- order：14

- locator：Introduction P5 S2

- paraphrase_cn：GDCM依据哲学和认知科学的概念理论设计，这些理论认为概念应用最少认知努力提供最多信息。

- move_code：理论依据重述

- statement_status：theory_claim

- why_here_cn：正式把design选择挂在理论命题上。

- inherits_from_previous_cn：把算法定位与第三段的原型理论连接起来。

- changes_argument_state_cn：从技术定位上升到认识论定位。

- sets_up_next_cn：下一句列出四条概念标准。

- failure_if_removed_cn：“按理论设计”的声明失去依据。

- evidence_pointer：Section 1 P5

### 15. Introduction P5 bullets 1–4

- order：15

- locator：Introduction P5 bullets 1–4

- paraphrase_cn：四条标准：词汇化保证概念可用语言表达；概念连贯性要求成员彼此相似；区分性保证概念之间可区分；相关性要求概念为感知和预测现实提供最大信息。

- move_code：四条标准列表

- statement_status：theory_claim

- why_here_cn：把抽象概念理论拆成四条可操作标准，作为GDCM的底层原则。

- inherits_from_previous_cn：直接从上一句的“理论”展开。

- changes_argument_state_cn：理论从一句话变成四条工程可对照标准。

- sets_up_next_cn：为第六段的三个desiderata转换作铺垫。

- failure_if_removed_cn：后文的loss函数没有对应来源。

- evidence_pointer：Section 1 P5 bullets

### 16. Introduction P6 S1

- order：16

- locator：Introduction P6 S1

- paraphrase_cn：GDCM通过定制架构与训练目标满足上述四条标准。

- move_code：标准到实现的连接

- statement_status：design_decision

- why_here_cn：把理论标准与算法设计正式绑定，开启desiderata段落。

- inherits_from_previous_cn：承接四条标准。

- changes_argument_state_cn：宣布理论标准已经被工程化。

- sets_up_next_cn：随后用三个desiderata具体说明怎么实现。

- failure_if_removed_cn：理论和工程脱节，整个文章支柱断裂。

- evidence_pointer：Section 1 P6

### 17. Introduction P6 S2

- order：17

- locator：Introduction P6 S2

- paraphrase_cn：GDCM在Quadrant II方法中的突出特征是显式增强多样性。

- move_code：新颖点声明

- statement_status：design_decision

- why_here_cn：把多样性标定为与其他方法区分的核心卖点。

- inherits_from_previous_cn：在“满足标准”的前提下强调具体差异。

- changes_argument_state_cn：明确本文的technical novelty集中在多样性。

- sets_up_next_cn：下一句用科学发现理论解释多样性为何重要。

- failure_if_removed_cn：本文与sDTM/sLDA等方法的新颖性区分变弱。

- evidence_pointer：Section 1 P6

### 18. Introduction P6 S3

- order：18

- locator：Introduction P6 S3

- paraphrase_cn：不同且多样的概念会增加新发现的可能性，这是科学探索的基本步骤。

- move_code：多样性机制论证

- statement_status：theory_claim

- why_here_cn：把多样性的工程指标提升为科学发现条件，支撑后期用recall评价多样性。

- inherits_from_previous_cn：承接上一句强调多样性。

- changes_argument_state_cn：把技术特征和科学价值绑定。

- sets_up_next_cn：为下一段的desiderata定义做铺垫。

- failure_if_removed_cn：diversity将只是一个正则项，不能支撑“发现新概念”的科学主张。

- evidence_pointer：Section 1 P6

### 19. Introduction P6 bullet 1

- order：19

- locator：Introduction P6 bullet 1

- paraphrase_cn：空间可解释性：把词、概念、文档嵌入共同空间，邻近词可解释概念，从而保证词汇化和连贯性。

- move_code：desiderata一：解释性之空间

- statement_status：design_decision

- why_here_cn：把“可解释性”拆成空间解释与预测解释两个子维度，以便对应到具体模型组件。

- inherits_from_previous_cn：承接三个desiderata中的第一条。

- changes_argument_state_cn：将interpretability操作化为“同空间+邻近词”。

- sets_up_next_cn：为4.1的嵌入网络和Table 2埋下对照。

- failure_if_removed_cn：后文用共享嵌入空间实现的解释性失去引言依据。

- evidence_pointer：Section 1 P6 bullets

### 20. Introduction P6 bullet 2

- order：20

- locator：Introduction P6 bullet 2

- paraphrase_cn：预测可解释性：用固有可解释的线性模型，用概念权重描述概念与结果的关系。

- move_code：desiderata一：解释性之预测

- statement_status：design_decision

- why_here_cn：把预测可解释性定义成线性层，为后面的系数报告和分类loss做铺垫。

- inherits_from_previous_cn：承接解释性第二条子维度。

- changes_argument_state_cn：规定GDCM的输出必须是可理解的权重关系。

- sets_up_next_cn：为Equation (7)/(10)的θ和5.3.2的系数分析做准备。

- failure_if_removed_cn：预测解释性作为desideratum没有引言定义。

- evidence_pointer：Section 1 P6 bullets

### 21. Introduction P6 bullet 3

- order：21

- locator：Introduction P6 bullet 3

- paraphrase_cn：多样性：模型迫使概念在概念空间中彼此远离，从而增强区分并提高有洞察力的候选概念召回。

- move_code：desiderata二：多样性

- statement_status：design_decision

- why_here_cn：把多样性正则与recall目标相连，为第4.2.3的“用多样性代理recall”论证作铺垫。

- inherits_from_previous_cn：承接第17-18句对多样性的强调。

- changes_argument_state_cn：首次把“多样性”和“recall”挂钩。

- sets_up_next_cn：需要下一点说明向量化是多样性的前提。

- failure_if_removed_cn：后文用recall评价多样性时会缺少引言中的动机。

- evidence_pointer：Section 1 P6 bullets

### 22. Introduction P6 bullet 4

- order：22

- locator：Introduction P6 bullet 4

- paraphrase_cn：相关性：挖掘概念被聚焦在与管理结果高度相关的概念空间子区域。

- move_code：desiderata三：相关性

- statement_status：design_decision

- why_here_cn：把相关性的实现方式明确为“聚焦相关子空间”，直接对应分类loss。

- inherits_from_previous_cn：承接三个desiderata中的第三条。

- changes_argument_state_cn：规定相关性不是事后筛选，而是训练目标。

- sets_up_next_cn：为第4.1.5的L_clf和Y引导概念作铺垫。

- failure_if_removed_cn：后文把Y加入损失函数的决定在引言中没有预告。

- evidence_pointer：Section 1 P6 bullets

### 23. Introduction P7 S1–S4

- order：23

- locator：Introduction P7 S1–S4

- paraphrase_cn：三个desiderata缺一不可：没有可解释性则概念不可理解；没有多样性则发现冗余；没有相关性则结果与管理目标脱节。

- move_code：三要求互补论证

- statement_status：author_inference

- why_here_cn：把三要求写成联合必要条件，为后文“同时优化”的主张奠定逻辑。

- inherits_from_previous_cn：直接使用前一段的三个desiderata。

- changes_argument_state_cn：从“各自重要”升级为“必须同时满足”。

- sets_up_next_cn：下一句把GDCM定位为对抗黑箱批评的工具。

- failure_if_removed_cn：同时优化的主张在引言中缺少正当性。

- evidence_pointer：Section 1 P7

### 24. Introduction P7 S5–S6

- order：24

- locator：Introduction P7 S5–S6

- paraphrase_cn：GDCM在一个步骤内同时优化这些desiderata，从而把深度学习从黑箱变成可洞察的guided exploration工具。

- move_code：贡献升格

- statement_status：contribution_claim

- why_here_cn：收束引言前半：算法不仅比现有方法多一两个正则，而是整体解决三要求。

- inherits_from_previous_cn：承接三要求缺一不可的论证。

- changes_argument_state_cn：把制品定位为“one-step”同时优化，区别于分步管道。

- sets_up_next_cn：为第八段的评价预告提供落点。

- failure_if_removed_cn：本文作为设计科学贡献的高度被削弱。

- evidence_pointer：Section 1 P7

### 25. Introduction P8 S1

- order：25

- locator：Introduction P8 S1

- paraphrase_cn：第5节将在“评论阅读与转化捆绑”的电子商务场景中展示GDCM在三个评价标准上的表现，并预告能提取Garvin已知构念且匹配Liu等因果研究。

- move_code：评价预览

- statement_status：method_decision

- why_here_cn：在引言最后给出评价路线图和两个关键外部效度证据，让读者对“证明什么”有预期。

- inherits_from_previous_cn：直接呼应三desiderata和前面所说的概念理论。

- changes_argument_state_cn：把论文重心从“提出算法”转向“以何种证据验收”。

- sets_up_next_cn：结束引言，为第2节文献递进作准备。

- failure_if_removed_cn：评价章节缺少引言级路标。

- evidence_pointer：Section 1 P8

## 引言逐段图谱

### 1. Introduction P1

- order：1

- locator：Introduction P1

- opening_move_cn：用企业文本分析普及这一公共事实开场。

- development_move_cn：从文本量大引出认知挑战，再收窄到概念必须与结果相关、概念必须多样。

- pivot_move_cn：在“概念化”之后分别加入相关性和多样性两个约束。

- closing_move_cn：留下“两个需求但没有工具”的状态，促使第二段提出GDCM。

- paragraph_job_cn：建立现实问题：管理者需要将海量文本转化为与结果相关且多样的概念。

### 2. Introduction P2

- order：2

- locator：Introduction P2

- opening_move_cn：直接提出GDCM作为解答。

- development_move_cn：用三条关键要求把算法目标写清楚。

- pivot_move_cn：把“目标”转成“验收标准”。

- closing_move_cn：用Table 1给读者一个算法IO概览。

- paragraph_job_cn：给出全文核心制品及其三个设计目标。

### 3. Introduction P3

- order：3

- locator：Introduction P3

- opening_move_cn：从管理洞察目标转向概念理论的定义。

- development_move_cn：引用概念作为思想积木的理论，说明管理者/研究者最终需要概念。

- pivot_move_cn：从“需要概念”转到“因此GDCM按概念理论设计”。

- closing_move_cn：预告后文的理论来源。

- paragraph_job_cn：为算法在哲学/认知科学中寻找根基，让技术设计获得理论合法性。

### 4. Introduction P4

- order：4

- locator：Introduction P4

- opening_move_cn：用2x2图开启方法分类。

- development_move_cn：逐一描绘四种管理任务及其对应象限方法。

- pivot_move_cn：焦点收在Quadrant II，指出其方法要么黑箱要么缺多样性/连贯性。

- closing_move_cn：制造Quadrant II缺口，留给GDCM补位。

- paragraph_job_cn：在方法版图中定位现有工具并打开核心研究缺口。

### 5. Introduction P5

- order：5

- locator：Introduction P5

- opening_move_cn：宣布GDCM属于Quadrant II。

- development_move_cn：给出理论依据（最少认知努力最大信息），并列出四条概念标准。

- pivot_move_cn：从哲学标准转到GDCM的实现原则。

- closing_move_cn：以四条标准作为第2节和模型设计的导航。

- paragraph_job_cn：把理论标准引入并宣布GDCM按标准设计。

### 6. Introduction P6

- order：6

- locator：Introduction P6

- opening_move_cn：从“满足四条标准”切到三个desiderata。

- development_move_cn：先强调显式多样性是与其它Quadrant II方法的不同点，并借科学哲学论证多样性的价值。

- pivot_move_cn：用四个bullet把三desiderata操作化到具体技术实现。

- closing_move_cn：让读者理解三desiderata的工程对应物。

- paragraph_job_cn：将理论标准转化为可实现的技术规格，并预告模型章节。

### 7. Introduction P7

- order：7

- locator：Introduction P7

- opening_move_cn：重申三个desiderata缺一不可。

- development_move_cn：逐项说明缺少每个desideratum的后果。

- pivot_move_cn：从“各要件”转向“同时优化”。

- closing_move_cn：把GDCM定位为一步式同时优化，回应黑箱批评。

- paragraph_job_cn：论证书三要求必须联合满足，为联合损失函数设计背书。

### 8. Introduction P8

- order：8

- locator：Introduction P8

- opening_move_cn：直接预告第5节评价。

- development_move_cn：列出三个评价场景，补充人类/仿真基准，并预告Garvin理论和Liu因果研究两个外部锚。

- pivot_move_cn：从内部评价转向外部效度证据。

- closing_move_cn：用“外部可信”收束引言。

- paragraph_job_cn：呈现论文的证据路线，让读者对后续验证方式有清楚期待。

## 理论到设计逐句图谱

### 1. Section 2.1 P1 S1–S2

- order：1

- locator：Section 2.1 P1 S1–S2

- paraphrase_cn：古典概念理论要求严格标准，原型理论则更贴合现代认知科学，给出更清晰的数学形式。

- move_code：理论选择论证

- statement_status：theory_claim

- why_here_cn：在多个概念理论中说明为什么选择原型理论。

- inherits_from_previous_cn：承接引言中“按概念理论设计”的声明。

- changes_argument_state_cn：把“概念理论”具体化为“原型理论”。

- sets_up_next_cn：准备给出三元组(A,d,p)。

- failure_if_removed_cn：理论选择缺乏理由，后文三元组无根基。

- evidence_pointer：Section 2.1 P1

### 2. Section 2.1 P1 S3–S4

- order：2

- locator：Section 2.1 P1 S3–S4

- paraphrase_cn：原型理论中概念是(A,d,p)三元组：A是概念域，d是成员到原型p的距离。

- move_code：理论形式化

- statement_status：theory_claim

- why_here_cn：给出可被算法直接翻译的数学结构。

- inherits_from_previous_cn：由原型理论直接推出。

- changes_argument_state_cn：理论从叙述变成形式化对象。

- sets_up_next_cn：下一段把A/d/p逐一映射到嵌入空间、相似度和概念向量。

- failure_if_removed_cn：理论到模型的翻译没有分子。

- evidence_pointer：Section 2.1 P1

### 3. Section 2.1 P2 S1–S3

- order：3

- locator：Section 2.1 P2 S1–S3

- paraphrase_cn：在GDCM中，A对应共享嵌入空间，d对应相似度度量，p对应概念嵌入。

- move_code：理论到组件映射

- statement_status：design_decision

- why_here_cn：这是全文的翻译枢纽：理论三元组变成可训练组件。

- inherits_from_previous_cn：直接安装在前一句的三元组上。

- changes_argument_state_cn：把OS三要素变成模型设计规格。

- sets_up_next_cn：下面的段落分别解释lexicalization、coherence、differentiation、relevance如何实现。

- failure_if_removed_cn：理论贡献和算法实现之间的约等于关系断裂。

- evidence_pointer：Section 2.1 P2

### 4. Section 2.1 P3 S1–S4

- order：4

- locator：Section 2.1 P3 S1–S4

- paraphrase_cn：词汇化由词嵌入实现，邻近词解释原型；距离度量配合最近词让原型可解释；区分性通过惩罚概念嵌入相似性实现；相关性选取对预测最有效的分组和原型。

- move_code：四条标准逐一操作化

- statement_status：design_decision

- why_here_cn：把理论四条标准转换为可设计的组件集合。

- inherits_from_previous_cn：承接A/d/p映射。

- changes_argument_state_cn：将引言中的四条标准与具体机制一一对应。

- sets_up_next_cn：引出第4节的loss函数结构。

- failure_if_removed_cn：标准与loss的对应表（Table 4）没有逻辑铺垫。

- evidence_pointer：Section 2.1 P3

### 5. Section 2.1 P4 S1–S2

- order：5

- locator：Section 2.1 P4 S1–S2

- paraphrase_cn：小结：GDCM把原型和成员放在统一语义空间，并用loss优化多样性和相关性。

- move_code：理论设计小结

- statement_status：design_decision

- why_here_cn：收束本节，给读者一个总结性的实现图景。

- inherits_from_previous_cn：整合前四段的理论映射。

- changes_argument_state_cn：宣布理论到设计的第一步已经完成。

- sets_up_next_cn：下一段转向LDA等方法的局限性。

- failure_if_removed_cn：理论部分缺少结论句。

- evidence_pointer：Section 2.1 P4

### 6. Section 2.1 P5 S1–S2

- order：6

- locator：Section 2.1 P5 S1–S2

- paraphrase_cn：LDA及其变体的主题可粗看为原型，但主题与成员不在同一概念空间，违反原型理论；嵌入主题模型虽然有同空间改进，但缺乏明确的距离度量d。

- move_code：替代方法理论缺陷

- statement_status：author_inference

- why_here_cn：用理论标准来批评整个主题模型家族，这是本文区分性论证的关键一步。

- inherits_from_previous_cn：承接原型理论定义。

- changes_argument_state_cn：把现有方法的失败定义为“违反概念理论”而非单纯性能差。

- sets_up_next_cn：为第2.2节文献收束和GDCM定位服务。

- failure_if_removed_cn：GDCM与其他主题模型的本质区分被削弱。

- evidence_pointer：Section 2.1 P5

### 7. Section 2.2 P1–P3

- order：7

- locator：Section 2.2 P1–P3

- paraphrase_cn：商业应用中常用传统概念提取和主题模型，从LDA到ProdLDA再到嵌入主题模型都有进展，但主题常有intrusion和diffusion，缺少良定义概念的desiderata。

- move_code：商业方法综述

- statement_status：prior_literature

- why_here_cn：把主题模型的发展简史放在ISR语境中，为缺口提供文献证据。

- inherits_from_previous_cn：接续第2.1节对LDA家族的理论批评。

- changes_argument_state_cn：将理论与现实算法结合，说明问题普遍存在。

- sets_up_next_cn：下一段讨论Quadrant II方法也面临同样问题。

- failure_if_removed_cn：文献基础不够厚，GDCM的贡献缺乏对照。

- evidence_pointer：Section 2.2

### 8. Section 2.2 P4–P5

- order：8

- locator：Section 2.2 P4–P5

- paraphrase_cn：虽然引导型主题模型sLDA、HSTM、sDTM等引入Y，但仍缺少概念理论根基且不满足desiderata，因此作者设计GDCM来填补Quadrant II缺口。

- move_code：缺口正式宣告

- statement_status：author_inference

- why_here_cn：把整个Quadrant II的literature描述为“有引导但无理论根基”，为GDCM创造直接入口。

- inherits_from_previous_cn：承接Quadrant II方法的介绍。

- changes_argument_state_cn：从“review文献”转为“填补文献空白”。

- sets_up_next_cn：用Table 2给出与HSTM/sDTM/sLDA三方法的desiderata级比较。

- failure_if_removed_cn：本文作为gap-filling研究的定位消失。

- evidence_pointer：Section 2.2 P4–P5

### 9. Section 2.3 P1–P1.2

- order：9

- locator：Section 2.3 P1–P1.2

- paraphrase_cn：黑箱算法在高风险决策中带来审计、责任和隐私问题；XAI文献分为model-wise explainable和outcome-wise interpretable两类，但对interpretability没有统一定义。

- move_code：可解释性文献综述

- statement_status：prior_literature

- why_here_cn：在ISR语境中把可解释性作为一种治理和决策问题来讨论，而不只是CS指标。

- inherits_from_previous_cn：承接引言中三desiderata里的解释性。

- changes_argument_state_cn：将可解释性定义为可分维度的、可被人类判断与coherence测量的对象。

- sets_up_next_cn：引出本论文在guided exploration中如何设计interpretability。

- failure_if_removed_cn：第5.1的两类解释性证据缺少文献语境。

- evidence_pointer：Section 2.3

### 10. Section 2.3 P6 S1–S2

- order：10

- locator：Section 2.3 P6 S1–S2

- paraphrase_cn：本论文在guided exploration任务中谨慎设计可解释ML，使其既增强对语料的人类理解又保持与黑箱竞争的绩效；并用coherence和MTurk人类判断测量解释性。

- move_code：本文可解释贡献定位

- statement_status：method_decision

- why_here_cn：把XAI文献与本文的测量策略绑定。

- inherits_from_previous_cn：承接上一段对interpretability无统一定义的讨论。

- changes_argument_state_cn：把模糊的“可解释性”收敛为可用coherence和human judgment检验的指标。

- sets_up_next_cn：第3节数据与第5.1节评价方法呼之欲出。

- failure_if_removed_cn：coherence + MTurk为什么够格作为解释性证据缺少交代。

- evidence_pointer：Section 2.3 P6

## 制品设计理由逐句图谱

### 1. Section 4.1 P1 S1–S2

- order：1

- locator：Section 4.1 P1 S1–S2

- paraphrase_cn：GDCM由CAN网络、嵌入网络和分类器组成，总loss包含嵌入、稀疏、多样性和分类四项。

- move_code：总体架构声明

- statement_status：design_decision

- why_here_cn：在进入具体公式前给读者一个整体地图。

- inherits_from_previous_cn：承接第2.1节的理论映射。

- changes_argument_state_cn：把理论标准落实为四项可优化目标。

- sets_up_next_cn：下面是逐项loss解释。

- failure_if_removed_cn：模型章节没有导航。

- evidence_pointer：Section 4.1 P1

### 2. Section 4.1.1 P1–P2

- order：2

- locator：Section 4.1.1 P1–P2

- paraphrase_cn：GDCM通过skip-gram负采样把词嵌入到共享语义空间，保持语义相似的词邻近。

- move_code：词嵌入设计理由

- statement_status：design_decision

- why_here_cn：解释为什么要用skip-gram负采样而不只是词袋：为了获得距离语义。

- inherits_from_previous_cn：直接把第2.1节的概念域A定义为该空间。

- changes_argument_state_cn：理论上的A在此成为可训练的R^E空间。

- sets_up_next_cn：为同一空间中插入概念向量作准备。

- failure_if_removed_cn：同空间嵌入是GDCM一切机制的基础，缺失则全文崩塌。

- evidence_pointer：Section 4.1.1

### 3. Section 4.1.2 P1–P4

- order：3

- locator：Section 4.1.2 P1–P4

- paraphrase_cn：每个概念是嵌入空间中的一个可学习向量，相当于原型理论中的原型p；文档向量是概念向量的加权线性组合，符合Gardenfors的containment模型。

- move_code：概念与文档表示理由

- statement_status：design_decision

- why_here_cn：这是把原型理论映射到模型的第二次关键翻译：p和成员在同一空间。

- inherits_from_previous_cn：承接词嵌入空间和A/d/p定义。

- changes_argument_state_cn：使得概念之间可以算距离、文档可以用概念组合解释。

- sets_up_next_cn：用扩展skip-gram loss让词、文档、概念同空间。

- failure_if_removed_cn：多样性和可解释性都失去实现载体。

- evidence_pointer：Section 4.1.2

### 4. Section 4.1.3 P1 S1–S2

- order：4

- locator：Section 4.1.3 P1 S1–S2

- paraphrase_cn：GDCM希望每份文档主要表现出少量概念，稀疏性增强预测可解释性并类比LDA/Lasso正则。

- move_code：稀疏正则理由

- statement_status：design_decision

- why_here_cn：解释为什么用Gaussian entropy而非L1/L0：为了可微。

- inherits_from_previous_cn：承接上一段文档-概念分布。

- changes_argument_state_cn：为预测解释性增加一个专门正则。

- sets_up_next_cn：给L_spr公式提供动机。

- failure_if_removed_cn：消融分析中λ的作用失去设计依据。

- evidence_pointer：Section 4.1.3

### 5. Section 4.1.4 P1–P2

- order：5

- locator：Section 4.1.4 P1–P2

- paraphrase_cn：多样性正则直接对应区分性原则，惩罚所有概念嵌入对之间的点积相似度，缓解LDA式主题重叠。

- move_code：多样性正则理由

- statement_status：design_decision

- why_here_cn：在何处解释L_div公式的动机：区分性、防止少数主导概念遮蔽低频重要概念。

- inherits_from_previous_cn：承接第3.2节指出的主题重叠问题。

- changes_argument_state_cn：把“多样性”从目标变为可微loss。

- sets_up_next_cn：下一小节切换到Y引导。

- failure_if_removed_cn：本文的核心技术新意就没有了。

- evidence_pointer：Section 4.1.4

### 6. Section 4.1.5 P1–P3

- order：6

- locator：Section 4.1.5 P1–P3

- paraphrase_cn：为让概念解释给定管理结果Y，引入线性权重θ和交叉熵分类loss；还可加入用户X以比较概念与X的相对重要性。

- move_code：相关性loss理由

- statement_status：design_decision

- why_here_cn：这是“guided”的具体实现：Y通过分类loss反过来塑造概念。

- inherits_from_previous_cn：承接三desiderata中的relevance和第3.2节管理任务。

- changes_argument_state_cn：模型从纯无监督变成监督引导的探索工具。

- sets_up_next_cn：引出Equation (7)和(10)的双重用途：预测与系数解释。

- failure_if_removed_cn：“引导”一词失去技术含义。

- evidence_pointer：Section 4.1.5

### 7. Section 4.2.1 P1–S2

- order：7

- locator：Section 4.2.1 P1–S2

- paraphrase_cn：回指原型理论的A/d/p，重申同空间嵌入同时保证词汇化和概念连贯性。

- move_code：理论回指

- statement_status：theory_claim

- why_here_cn：在模型细节后重新锚定理论，防止读者迷失在公式中。

- inherits_from_previous_cn：使用第4.1节的设计组件。

- changes_argument_state_cn：证明设计不是随意拼装而是理论驱动。

- sets_up_next_cn：为4.2.2的多样性提供连续性。

- failure_if_removed_cn：理论到实现的闭环不完整。

- evidence_pointer：Section 4.2.1

### 8. Section 4.2.2 P1–S2

- order：8

- locator：Section 4.2.2 P1–S2

- paraphrase_cn：能惩罚概念间距离是因为概念被向量化，这是GDCM在Quadrant II中的独特性，类似于对比学习目标。

- move_code：独特性论证

- statement_status：theory_claim

- why_here_cn：解释为什么其他方法做不了显式多样性：没有向量化的概念。

- inherits_from_previous_cn：承接共享空间和概念向量。

- changes_argument_state_cn：把“能否做多样性”变成区分GDCM与竞争者的结构性条件。

- sets_up_next_cn：下一段解释分类loss和整体协作机制。

- failure_if_removed_cn：GDCM的技术新颖性缺少机制性解释。

- evidence_pointer：Section 4.2.2

### 9. Section 4.2.3 P1–P2

- order：9

- locator：Section 4.2.3 P1–P2

- paraphrase_cn：分类loss为引导概念提供归纳偏置；由于guided exploration不知道真实概念，无法直接优化recall，只能先优化多样性，再让相关性约束定义假设空间，多样性在此空间内提高recall。

- move_code：recall代理论证

- statement_status：author_inference

- why_here_cn：这是全文最关键的机制声明：为什么优化diversity就能提高recall。

- inherits_from_previous_cn：结合L_spr/L_div/L_clf三者关系。

- changes_argument_state_cn：把diversity从独立目标重新解释为recall的代理优化目标。

- sets_up_next_cn：为第5.2节用召回率评价diversity提供理论合理性。

- failure_if_removed_cn：第5.2.2用Garvin召回支持多样性就变成评价错位。

- evidence_pointer：Section 4.2.3 P2

## Study开头、过渡与收束图谱

### 1. Section 3.1 P1–P2

- order：1

- locator：Section 3.1 P1–P2

- opening_cn：用在线零售商决策旅程数据开场，明确数据来源、用户数、品类和时间窗。

- transition_function_cn：从方法文献切换到真实数据任务，为所有评价建立共同场景。

- closing_cn：以UserID-ProductID为分析单位，给出样本组成和Online Appendix B.1指向。

- paragraph_job_cn：定义主数据与预测/概念发现任务。

### 2. Section 3.2 P1–P3

- order：2

- locator：Section 3.2 P1–P3

- opening_cn：重述GDCM聚焦guided exploration，并说明管理者可用Y、X、评论发现相关概念。

- transition_function_cn：从纯任务定义过渡到“现有方法失败在多样性”的核心缺口。

- closing_cn：用图3展示LDA和sDTM等主题词中的intrusion/diffusion，并指出基准方法各异问题。

- paragraph_job_cn：说明现有引导方法为什么不够，为第4节建模提供动机。

### 3. Section 4 opening

- order：3

- locator：Section 4 opening

- opening_cn：宣布本节描述GDCM主要组件与设计理由。

- transition_function_cn：从“任务缺口”跳到“解决方案”。

- closing_cn：以总体loss公式结束概述，并指向在线附录训练细节。

- paragraph_job_cn：作为模型章节的导航。

### 4. Section 5 opening

- order：4

- locator：Section 5 opening

- opening_cn：用Table 5列出全部实验及其对应的desiderata、节、图表。

- transition_function_cn：从模型章节过渡到评价章节，让每个实验都有明确验收维度。

- closing_cn：无显式关闭，直接进入5.1。

- paragraph_job_cn：建立三desiderata与实验的映射表，预先把评价逻辑讲清楚。

### 5. Section 5.1.1 opening–closing

- order：5

- locator：Section 5.1.1 opening–closing

- opening_cn：用MTurk调查评估GDCM和各引导主题模型的可解释性。

- transition_function_cn：承接解释性desideratum，用人类判断作为首选证据。

- closing_cn：报告Gini最高且给出bootstrap标准误，说明GDCM主题最清晰。

- paragraph_job_cn：用人类判断直接支持空间可解释性主张。

### 6. Section 5.1.2 opening–closing

- order：6

- locator：Section 5.1.2 opening–closing

- opening_cn：引入coherence作为算法层面的解释性衡量，说明其局限。

- transition_function_cn：从人类判断转向可复现的算法指标，作为robustness check。

- closing_cn：解释sDTM/sLDA高coherence可能因词重复虚高，并用Garvin理论外部效度收束。

- paragraph_job_cn：用coherence加固可解释性主张，同时识别高coherence的陷阱。

### 7. Section 5.2 opening–5.2.1

- order：7

- locator：Section 5.2 opening–5.2.1

- opening_cn：先给总起句：实验显示GDCM发现更多unique概念。

- transition_function_cn：从解释性转向多样性。

- closing_cn：用Figure 5/6展示GDCM在平均成对余弦距离和unique Garvin维度数上占优。

- paragraph_job_cn：用人类判断支持多样性和已知概念召回。

### 8. Section 5.2.2 opening–closing

- order：8

- locator：Section 5.2.2 opening–closing

- opening_cn：用Garvin维度词表作为ground truth，设定h_overlap阈值计算召回。

- transition_function_cn：从“人类归类”转向“可量化词重叠召回”。

- closing_cn：报告GDCM仅5次运行即超过基准50/150次运行的召回。

- paragraph_job_cn：提供已知概念召回的最强量化证据。

### 9. Section 5.2.3 opening–closing

- order：9

- locator：Section 5.2.3 opening–closing

- opening_cn：以机器恢复概念作为伪ground truth，检验unknown概念相对召回。

- transition_function_cn：从已知Garvin概念扩展到未知概念，回应“发现未知”的更高主张。

- closing_cn：报告GDCM有更高覆盖率，细节指向Online Appendix B.5。

- paragraph_job_cn：把多样性主张从“已知概念”升级到“未知概念相对覆盖”。

### 10. Section 5.3.1 opening–closing

- order：10

- locator：Section 5.3.1 opening–closing

- opening_cn：说明Y对filtering的作用，并用主数据预测转化作为sanity check。

- transition_function_cn：从多样性转向相关性。

- closing_cn：报告GDCM AUC 0.8885，超过所有可解释基线，并接近CNN/XGB。

- paragraph_job_cn：用预测性能证明概念与Y相关。

### 11. Section 5.3.2 opening–closing

- order：11

- locator：Section 5.3.2 opening–closing

- opening_cn：说明GDCM输出概念与用户X的相对重要系数。

- transition_function_cn：从预测性能转向经济含义，即“概念重要性”有没有道理。

- closing_cn：报告Aesthetics最高、Serviceability最低，且与Liu et al. (2019)系数接近，并指出无置信区间。

- paragraph_job_cn：用外部因果研究锚定概念重要性的经济意义。

### 12. Section 5.3.3.1–5.3.3.2 opening–closing

- order：12

- locator：Section 5.3.3.1–5.3.3.2 opening–closing

- opening_cn：先用DonorsChoose验证不同Y对概念发现的影响。

- transition_function_cn：从单Y场景扩展到多Y场景。

- closing_cn：用消融报告ρ提高AUC、η提高解释性、λ降低AUC但不影响解释性。

- paragraph_job_cn：通过Y敏感性与消融建立artifact claim的组分证据与边界。

### 13. Section 5.4 opening–closing

- order：13

- locator：Section 5.4 opening–closing

- opening_cn：综述5.1-5.3证据，指出在未知概念场景下LDA多次运行仍失败而GDCM五次成功。

- transition_function_cn：把分散的desiderata证据汇总为整体价值主张。

- closing_cn：把高解释性、高召回、高相关性三者合在一起收束评价。

- paragraph_job_cn：完成评价章节的总括和向管理含义过渡。

### 14. Section 6.1 opening–closing

- order：14

- locator：Section 6.1 opening–closing

- opening_cn：从电子商务案例说明GDCM如何帮助发现与转化相关的Garvin概念。

- transition_function_cn：把评价结果转成管理行动价值。

- closing_cn：给出动态监控、产品设计、filter bubble检测等应用。

- paragraph_job_cn：为管理者建立使用场景和收益。

### 15. Section 6.2 opening–closing

- order：15

- locator：Section 6.2 opening–closing

- opening_cn：对研究者声明GDCM是非因果、相关性的探索工具。

- transition_function_cn：从管理者应用转向研究者边界。

- closing_cn：强调用户领域知识决定什么值得继续因果研究。

- paragraph_job_cn：设定边界条件并区分相关性与因果。

### 16. Section 7 opening–closing

- order：16

- locator：Section 7 opening–closing

- opening_cn：用一句话总结GDCM是什么，做什么，由Y引导。

- transition_function_cn：文章结束时的收束句。

- closing_cn：最后希望读者创造性地使用。

- paragraph_job_cn：给出极简结论。

## 讨论与贡献逐句图谱

### 1. Section 6.1 P1 S1–S4

- order：1

- locator：Section 6.1 P1 S1–S4

- paraphrase_cn：用Garvin维度说明GDCM从评论中发现与转化相关的概念，并引用文献证明这些维度确有经济价值，如产品缺陷、特征偏好、市场结构。

- move_code：管理含义锚定

- statement_status：prior_literature

- why_here_cn：在管理含义开头把GDCM发现的概念与已证实的商业价值挂钩。

- inherits_from_previous_cn：承接5.4的Garvin概念结果。

- changes_argument_state_cn：把“发现Garvin概念”从技术结果转换为经济价值声明。

- sets_up_next_cn：下一段上升到文本价值研究的普遍困境。

- failure_if_removed_cn：管理贡献缺乏实际价值支撑。

- evidence_pointer：Section 6.1 P1

### 2. Section 6.1 P2 S1–S3

- order：2

- locator：Section 6.1 P2 S1–S3

- paraphrase_cn：现有文本价值研究要么只给文本信号不给内容，要么只量化已知概念；GDCM能同时提供连贯概念、未知概念与经济重要性。

- move_code：文本研究空白填补

- statement_status：author_inference

- why_here_cn：把GDCM置于IS/营销文本研究的两种范式之间，强调其同时解决两者缺陷。

- inherits_from_previous_cn：利用前一段的文献例子。

- changes_argument_state_cn：把贡献从“算法更好”扩展为“填补文本研究的方法论缺口”。

- sets_up_next_cn：下一段讲操作优势。

- failure_if_removed_cn：管理贡献失去与文本研究传统的联系。

- evidence_pointer：Section 6.1 P2

### 3. Section 6.1 P3–P4 S1–S4

- order：3

- locator：Section 6.1 P3–P4 S1–S4

- paraphrase_cn：GDCM还能一键引导挖掘、对未见文档预测与提取概念、可通过SGD动态重训，适用于动态监测反馈、产品设计和filter bubble检测。

- move_code：操作优势与应用场景

- statement_status：author_inference

- why_here_cn：给管理者具体使用界面和场景。

- inherits_from_previous_cn：承接GDCM作为工具的工程能力。

- changes_argument_state_cn：把算法从离线分析工具提升为可动态部署的管理仪表盘组件。

- sets_up_next_cn：下一节切换到研究者含义。

- failure_if_removed_cn：管理贡献缺少“怎么用”的回答。

- evidence_pointer：Section 6.1 P3–P4

### 4. Section 6.2 P1 S1–S3

- order：4

- locator：Section 6.2 P1 S1–S3

- paraphrase_cn：对研究者，GDCM是探索性非因果的相关工具，服务于假设生成、经验推广和计算密集型理论构建。

- move_code：研究角色声明

- statement_status：contribution_claim

- why_here_cn：这是境界句：把GDCM定义为假设生成工具而非因果证明工具。

- inherits_from_previous_cn：承接评价结果和潜在发现能力。

- changes_argument_state_cn：限定了GDCM的贡献类型，防止过度解释。

- sets_up_next_cn：下一句讲ML在两类研究任务中的角色。

- failure_if_removed_cn：本文会被误读为因果工具，边界主张丢失。

- evidence_pointer：Section 6.2 P1

### 5. Section 6.2 P2 S1–S3

- order：5

- locator：Section 6.2 P2 S1–S3

- paraphrase_cn：ML的两种使用场景：规模化假设检验和从数据发现假设；GDCM属于后者。

- move_code：发现假设定位

- statement_status：prior_literature

- why_here_cn：把GDCM放在ML研究的第二类任务中，为计算机辅助理论构建提供正当性。

- inherits_from_previous_cn：承接“假设生成”的目标。

- changes_argument_state_cn：把GDCM贡献定位为augmented hypothesis development。

- sets_up_next_cn：下一句做用户依赖与因果性的限定。

- failure_if_removed_cn：GDCM作为研究工具的角色不清晰。

- evidence_pointer：Section 6.2 P2

### 6. Section 6.2 P3 S1–S3

- order：6

- locator：Section 6.2 P3 S1–S3

- paraphrase_cn：GDCM最终取决于用户领域判断；它控制变量但抓取的是文本现状，不能作因果声明；研究者需凭逻辑和领域知识判断哪些值得深究。

- move_code：边界与用户依赖

- statement_status：author_inference

- why_here_cn：作为边界声明收束讨论，避免被批评为因果或自动发现。

- inherits_from_previous_cn：承接“工具”与“假设生成”的定位。

- changes_argument_state_cn：把产品边界写成“相关而非因果、人机协同”。

- sets_up_next_cn：为结论段的温和收尾作了铺垫。

- failure_if_removed_cn：边界缺失会让贡献主张过度。

- evidence_pointer：Section 6.2 P3

### 7. Section 7 P1 S1–S2

- order：7

- locator：Section 7 P1 S1–S2

- paraphrase_cn：总结GDCM是按Y引导探索、组织、提取文本信息的深度学习方法，希望管理者与研究者创造性地用于构建新假设和理论。

- move_code：结论句

- statement_status：contribution_claim

- why_here_cn：用一句话干净收尾。

- inherits_from_previous_cn：把全文的定义、评价、边界浓缩进结论。

- changes_argument_state_cn：把技术文章最终定性为假设生成工具。

- sets_up_next_cn：无。

- failure_if_removed_cn：缺少文章最后的总结锚点。

- evidence_pointer：Section 7

## Study累积逻辑

### 1. 1

- study_or_phase：S1 数据与任务构造（Section 3）

- evidence_job_cn：构造一个管理者对相关概念一无所知的guided exploration真实场景。

- what_it_establishes_cn：提供评论文本、结构X、二元转化Y和UserID-ProductID旅程样本，证明后续评价有现实基础。

- what_it_cannot_establish_cn：不能证明GDCM在该数据上表现如何，也不能证明其他方法失败。

- why_next_phase_is_needed_cn：需要算法实现后才能在同样数据上评价。

- transition_wording_function_cn：“Our method... focuses on guided exploration”把任务交给GDCM。

### 2. 2

- study_or_phase：S2 现有方法失败展示（Section 3.2）

- evidence_job_cn：用LDA等主题词可视化证明现有方法在intrusion/diffusion上不可用。

- what_it_establishes_cn：现有guided exploration方法缺少多样性且主题词混乱。

- what_it_cannot_establish_cn：不能证明GDCM能解决这些问题。

- why_next_phase_is_needed_cn：需要提出并实现GDCM。

- transition_wording_function_cn：“Presented with such outputs, it is unclear how managers may...”紧接Section 4。

### 3. 3

- study_or_phase：S3 GDCM建模（Section 4）

- evidence_job_cn：把三desiderata实现为四个loss组件，说明每个设计为什么这样选。

- what_it_establishes_cn：制品存在且其设计可追溯到原型理论。

- what_it_cannot_establish_cn：不能证明制品有效。

- why_next_phase_is_needed_cn：需要实证评价。

- transition_wording_function_cn：“Table 5 lists the experiments...”直接进入评价。

### 4. 4

- study_or_phase：S4 人类可解释性评价（5.1.1）

- evidence_job_cn：证明人类对GDCM主题的分类共识更高。

- what_it_establishes_cn：GDCM概念更可解释、更连贯、无intrusion。

- what_it_cannot_establish_cn：不能证明concept多样性和Y相关性。

- why_next_phase_is_needed_cn：需要用算法指标和多样性/相关性证据补全。

- transition_wording_function_cn：“As a robustness check, we adopt the coherence score...”

### 5. 5

- study_or_phase：S5 coherence评价（5.1.2）

- evidence_job_cn：用独立于人类判断的算法指标加固可解释性。

- what_it_establishes_cn：GDCM coherence高于LDA且多轮范围不重叠。

- what_it_cannot_establish_cn：不能证明高coherence不是重复词造成的，也不能证明多样性。

- why_next_phase_is_needed_cn：需要多样性指标。

- transition_wording_function_cn：“Experiments show that GDCM discovers a higher number of unique concepts...”

### 6. 6

- study_or_phase：S6 已知概念多样性/召回（5.2.1-5.2.2）

- evidence_job_cn：证明GDCM主题更分散且能恢复更多已知Garvin概念。

- what_it_establishes_cn：多样性正则确实减少主题重叠并提高已知理论概念召回。

- what_it_cannot_establish_cn：不能证明能发现真正未知概念。

- why_next_phase_is_needed_cn：需要unknown概念检验。

- transition_wording_function_cn：“As a robustness check, we also test GDCM’s relative recallability of unknown concepts...”

### 7. 7

- study_or_phase：S7 未知概念相对召回（5.2.3）

- evidence_job_cn：在伪ground truth设定下检验GDCM对机器发现未知概念的覆盖率。

- what_it_establishes_cn：多样性对未知概念发现也有利。

- what_it_cannot_establish_cn：伪ground truth不是真实科学新概念。

- why_next_phase_is_needed_cn：需要证明概念与Y的相关性。

- transition_wording_function_cn：“Experiments show that the concepts produced by GDCM correlate highly with the managerial outcome.”

### 8. 8

- study_or_phase：S8 预测相关性（5.3.1）

- evidence_job_cn：用AUC证明GDCM概念对转化有强预测力，超过所有可解释基线并接近黑箱。

- what_it_establishes_cn：relevance desideratum成立。

- what_it_cannot_establish_cn：不能证明概念重要性更一般不只是一次预测。

- why_next_phase_is_needed_cn：需要经济意义和外部对照。

- transition_wording_function_cn：“To better utilize the extracted concepts, GDCM provides correlational importance...”

### 9. 9

- study_or_phase：S9 概念重要性外部对照（5.3.2）

- evidence_job_cn：用系数符号与排序同Liu et al. (2019)因果研究匹配来锚定经济意义。

- what_it_establishes_cn：GDCM自动概念在经济重要性上与理论因果研究一致。

- what_it_cannot_establish_cn：不能证明因果；数据不完全相同；无置信区间。

- why_next_phase_is_needed_cn：需要证明组分有效性和迁移性。

- transition_wording_function_cn：“Lastly, we highlight that GDCM’s end-to-end automated correlational result mostly replicates top-down theory-driven causal results...”

### 10. 10

- study_or_phase：S10 Y敏感性与消融（5.3.3）

- evidence_job_cn：展示概念随Y合理变化，并分离各loss组分的独立作用。

- what_it_establishes_cn：GDCM不是为单一Y定制，且λ/η/ρ各司其职。

- what_it_cannot_establish_cn：不能证明交互作用或长期部署表现。

- why_next_phase_is_needed_cn：需要回应最新LLM替代方案。

- transition_wording_function_cn：Appendix A的比较补在正文之外。

### 11. 11

- study_or_phase：S11 TopicGPT对比（Appendix A）

- evidence_job_cn：排除prompt-based LLM主题模型作为直接替代。

- what_it_establishes_cn：TopicGPT最佳AUC仍明显低于GDCM且存在幻觉。

- what_it_cannot_establish_cn：不能限制未发布或未来LLM。

- why_next_phase_is_needed_cn：补充后论文进入讨论与边界，不再需要新实验。

- transition_wording_function_cn：论文正文以边界声明收尾。

## 主张—证据台账

### 1. GDCM能同时实现高可解释性、多样性和相关性。

- claim_cn：GDCM能同时实现高可解释性、多样性和相关性。

- claim_level：technical

- supporting_evidence_cn：Gini最高、coherence优于LDA、Garvin召回最高、AUC 0.8885超过所有可解释基线。

- support_strength：direct

- where_claim_is_made：Introduction P6-P7, Section 5.4

- where_evidence_is_provided：Section 5.1.1, 5.1.2, 5.2.2, 5.3.1

### 2. 显式多样性正则和分类损失是GDCM改进的原因。

- claim_cn：显式多样性正则和分类损失是GDCM改进的原因。

- claim_level：artifact

- supporting_evidence_cn：消融显示提高η提高解释性、提高ρ提高AUC、提高λ降低AUC。

- support_strength：partial

- where_claim_is_made：Section 4.1.4-4.1.5

- where_evidence_is_provided：Section 5.3.3.2, Figure 9

### 3. 多样性正则提高对相关未知概念的recall。

- claim_cn：多样性正则提高对相关未知概念的recall。

- claim_level：mechanism

- supporting_evidence_cn：4.2.3机制论证、Garvin概念5次运行恢复、unknown概念覆盖率更高。

- support_strength：partial

- where_claim_is_made：Section 4.2.3, Introduction P6

- where_evidence_is_provided：Section 5.2.2, 5.2.3, Table 8

### 4. GDCM发现的概念是文献已理论化的产品品质维度。

- claim_cn：GDCM发现的概念是文献已理论化的产品品质维度。

- claim_level：boundary

- supporting_evidence_cn：GDCM的输出主题与Garvin维度匹配。

- support_strength：direct

- where_claim_is_made：Section 5.1.2末

- where_evidence_is_provided：Section 5.2.1-5.2.2

### 5. GDCM概念重要性匹配此前因果研究，是外部效度。

- claim_cn：GDCM概念重要性匹配此前因果研究，是外部效度。

- claim_level：theory

- supporting_evidence_cn：Aesthetics高、Serviceability低，与Liu et al. (2019)系数接近。

- support_strength：partial

- where_claim_is_made：Abstract S7, Section 5.3.2末

- where_evidence_is_provided：Figure 8(b)(c)

### 6. GDCM是探索性、非因果工具，不能直接用于因果推断。

- claim_cn：GDCM是探索性、非因果工具，不能直接用于因果推断。

- claim_level：boundary

- supporting_evidence_cn：作者明确声明，且系数为线性相关性。

- support_strength：direct

- where_claim_is_made：Section 6.2 P1/P3

- where_evidence_is_provided：Section 6.2, Figure 8注释

### 7. 概念提取对Y敏感且合理地变化。

- claim_cn：概念提取对Y敏感且合理地变化。

- claim_level：boundary

- supporting_evidence_cn：DonorsChoose多Y实验（附录C）。

- support_strength：partial

- where_claim_is_made：Section 5.3.3.1

- where_evidence_is_provided：Online Appendix C

### 8. TopicGPT等LLM主题模型不能替代GDCM。

- claim_cn：TopicGPT等LLM主题模型不能替代GDCM。

- claim_level：technical

- supporting_evidence_cn：TopicGPT最佳AUC约0.7095低于GDCM 0.8885，且有幻觉样例。

- support_strength：direct

- where_claim_is_made：Appendix A

- where_evidence_is_provided：Figure A.1, Table A.2

## ISR定位逻辑

- constitutive_is_problem_cn：文章把文本分析从自然语言处理任务重构成管理决策支持问题：管理者需要在无先验概念时，从评论语料中发现与转化等结果变量相关的概念，并据此生成假设、辅助研究。核心IS问题不是单纯预测性能，而是“文本—管理者可理解概念—管理结果”三者之间的构成关系。

- technology_behavior_or_market_entanglement_cn：在线零售决策旅程把用户阅读评论的行为、产品价格评分等结构数据与购买/放弃结果绑在一起；GDCM通过Y引导概念学习，使算法发现的概念嵌入用户评论阅读与转化决策的共同语境。技术在这里不是可替换工具，而是用来连接用户生成内容与管理行为的解释性中介。

- role_of_benchmark_or_objective_evidence_cn：AUC、coherence、Gini、召回率等客观指标主要用于支持“概念具有可解释性和相关性”这一IS主张，而不是单纯展示技术分数：可解释性通过人类Gini与coherence双重验证；相关性通过AUC和概念系数与外部因果研究对照。benchmark被用来证明GDCM满足了概念理论驱动的desiderata，而非声称全面最优。

- theory_in_design_cn：理论直接进入设计：原型理论的(A,d,p)被翻译为共享嵌入空间、距离度量、概念向量；四条概念标准分别映射到嵌入loss、稀疏loss、多样性loss和分类loss；第4.2节和Table 4明确展示loss与desiderata对应关系。理论不只是解释结果的叙事。

- technical_vs_is_contribution_balance_cn：文章把约两成的篇幅给技术公式和模型，把约六成给多维度评价，把约两成给管理/研究含义。技术贡献只被定位为“探索工具”，IS贡献则落在假设生成、文本研究价值、动态监控、filter bubble检测等组织/平台应用上。平衡点是：技术说明足够让方法可复现，但没有过度宣称性能纪录。

- beyond_transient_performance_cn：作者通过四层设计超越一时分数优势：一是用Garvin理论概念作为外部ground truth证明概念语义有理论对应；二是用Liu et al. (2019)因果研究锚定经济重要性；三是以Y敏感性说明工具可随不同管理问题变化；四是在边界中把贡献降级为假设生成而非因果工具。这使得贡献是“可复用的设计知识和理论驱动的探索流程”，而不只是AUC高0.03。

## 段落级仿写模板

### abstract_steps

1. 第1步：用一句话定义算法名称、类型和三个自动完成的任务。

2. 第2步：说明不需要预定义概念或标注数据，强调使用条件。

3. 第3步：给出关键技术机制——所有实体嵌入同一空间。

4. 第4步：列出三个目标配置：多样性、连贯性、相关性。

5. 第5步：引入真实场景与数据集。

6. 第6步：报告最核心结果：发现概念、给出重要性、与基准比较。

7. 第7步：用外部已发表的理论/因果研究作为外部效度锚。

8. 第8步：补充第二个数据上的Y敏感性结果，突出普适性。

### introduction_paragraph_steps

1. 第1段：公共背景→认知挑战→两个需求（相关+多样）。

2. 第2段：提出制品→三个要求→IO表。

3. 第3段：用理论定义核心构念→引用权威定义→宣布理论驱动设计。

4. 第4段：用2x2分类图→逐象限解释管理任务→聚焦目标象限→指出缺口。

5. 第5段：把制品放回图→声明理论根基→列出四条标准。

6. 第6段：把标准转成三desiderata→突出新颖点（多样性）→用bullet给技术实现。

7. 第7段：论证三要求缺一不可→同时优化→回击黑箱批评。

8. 第8段：预告评价路径、数据和外部效度。

### theory_to_design_steps

1. 第1步：在两个候选理论中选择一个可形式化的，并说明理由。

2. 第2步：给出理论的数学形式（三元组/结构）。

3. 第3步：把理论要素逐一对应到算法组件。

4. 第4步：把每个理论标准翻译为具体机制和loss。

5. 第5步：用一段小结宣布理论已被实现。

6. 第6步：用理论标准批评现有方法家族。

7. 第7步：在文献综述中把同一标准用于评价整个Quadrant II。

8. 第8步：用对照表（Table 2/4）固定“理论标准×方法×实现”三列。

### method_and_study_sequence_steps

1. 第1步：构造一个与Y绑定的真实数据集。

2. 第2步：显示现有方法在该任务上的具体失败样例。

3. 第3步：给出模型结构和总loss，先给地图再给公式。

4. 第4步：用一张实验映射表预告每个实验检验哪个desideratum。

5. 第5步：每个desideratum用至少两种证据（人类+算法）。

6. 第6步：从“已知概念”推进到“未知概念”证据。

7. 第7步：用预测和系数建立与Y的相关性证据。

8. 第8步：用外部因果研究做效度锚。

9. 第9步：用消融和Y敏感性保护artifact claim。

10. 第10步：用新兴LLM对比回应最新替代方案。

### results_reporting_steps

1. 第1步：报告指标前先声明该结果对应哪个desideratum。

2. 第2步：给出数字并说明与最优基准的差距。

3. 第3步：解释为什么该差距可以接受（比如0.03 AUC）。

4. 第4步：对异常高的基准分数给出替代解释（重复词虚高coherence）。

5. 第5步：用理论标准把数字转成外部意义（Garvin维度、因果研究）。

6. 第6步：在段落末声明局限，自然引到下一维度。

### discussion_and_contribution_steps

1. 第1步：回指评价结果并锚定到已有文献的经济价值。

2. 第2步：把工具置于该领域研究范式缺口之中。

3. 第3步：给出可操作的应用场景列表。

4. 第4步：对研究者声明方法类型（探索性、相关性）。

5. 第5步：区分ML的两种研究用途并把自己放入第二种。

6. 第6步：明确用户依赖和因果边界。

7. 第7步：用一句话结论收束。

## 可执行写作算法

### 1. 1

- step：1

- rhetorical_job_cn：在引言首段建立现实问题，让读者感受到文本分析的规模与认知压力。

- research_evidence_required_cn：需要至少一个真实行业事实或引用，说明企业依赖文本；需要能指出文本量带来的具体问题。

- sentence_pattern_function_cn：首段句子依次承担：事实背景→问题出现→行动必要性；不写技术细节，只写管理场景。

- transition_condition_cn：当读者认同“需要将文本转成概念且概念必须相关多样”时，进入第二步。

### 2. 2

- step：2

- rhetorical_job_cn：提出制品并用三个要求概述。

- research_evidence_required_cn：需要一个已成型或以鲜明方式提出的算法名称和三句以内要求描述。

- sentence_pattern_function_cn：产品句+要求句+表格句；要求用编号或bullet清晰列出。

- transition_condition_cn：当三个要求已列出并可对应到后续章节时，进入第三步。

### 3. 3

- step：3

- rhetorical_job_cn：用理论为概念下定义，把技术工作放入认识论传统。

- research_evidence_required_cn：需要选择有数学或结构化描述的理论，并准备好引用。

- sentence_pattern_function_cn：先定义目标构念，再引用权威理论定义，最后声明“因此从零设计”。

- transition_condition_cn：当理论来源明确且能形式化时，进入第四步。

### 4. 4

- step：4

- rhetorical_job_cn：构建方法分类图并打开缺口。

- research_evidence_required_cn：需要一个二维分类框架，能放下所有相关方法。

- sentence_pattern_function_cn：图句→各象限任务句→目标象限问题句；目标象限的问题必须是其他象限没有的。

- transition_condition_cn：当读者理解为什么聚焦Quadrant II并承认其方法不足时，进入第五步。

### 5. 5

- step：5

- rhetorical_job_cn：从理论提炼标准并转成desiderata。

- research_evidence_required_cn：需要理论标准列表和将其操作化的技术规格。

- sentence_pattern_function_cn：标准列表句→算法满足句→desiderata bullet句；每条标准都要在后续有实现点。

- transition_condition_cn：当每条desiderata都能对应一个later section时，进入第六步。

### 6. 6

- step：6

- rhetorical_job_cn：展示模型架构和每个设计决策的理由。

- research_evidence_required_cn：需要有模型结构、总loss、每个正则的动机和理论映射表。

- sentence_pattern_function_cn：架构声明→逐项loss动机→理论回指→协作机制解释。

- transition_condition_cn：当每个loss都能回答“为什么这样设计”时，进入第七步。

### 7. 7

- step：7

- rhetorical_job_cn：为每个desideratum分别设计评价并逐层累积证据。

- research_evidence_required_cn：需要人类判断、算法指标、ground truth召回、预测性能、外部对照等至少三到五类证据。

- sentence_pattern_function_cn：实验映射表→人类证据→算法证据→已知概念→未知概念→预测→外部效度→稳健性。

- transition_condition_cn：当每个desideratum都有直接证据且证据从内部转向外部时，进入第八步。

### 8. 8

- step：8

- rhetorical_job_cn：在讨论中依次完成结果解释、管理含义、研究含义、边界与限制。

- research_evidence_required_cn：需要能回指评价结果的贡献主张，以及坦诚的边界声明。

- sentence_pattern_function_cn：管理价值→研究范式→应用场景→工具边界→用户依赖→结论。

- transition_condition_cn：当贡献与边界都已声明且不越界时，写作完成。

## 应模仿的高价值动作

1. 用理论三元组直接翻译为模型组件，使理论成为设计的一部分而不是事后解释

2. 用2x2分类图在引言内快速建立领域地图并精准留出缺口

3. 把评价拆成desiderata映射表，每个实验明确回答一个验收标准

4. 在每个desideratum下同时使用人类判断与算法指标，形成互补证据

5. 用已发表的理论维度（Garvin）和因果研究（Liu et al. 2019）作为外部锚，防止贡献只是技术表演

6. 对高但可疑的基准分数主动给出替代解释（sDTM/sLDA重复词虚高coherence）

7. 在讨论中老实降级为探索性、相关性工具，并将未知概念发现锚定到假设生成而非因果推断

8. 用少量运行vs大量运行的对话（5次 vs 50/150次）让效率优势具象化

## 不要只复制的表面动作

1. 如果模型没有概念向量化，不要套用“多样性通过向量距离实现”的论证

2. 如果评价只有AUC，不可以直接宣称可解释性或外部效度

3. 不要仅仅因为用了MTurk就声称人类验证；需要Gini或类似一致性指标

4. 没有ground truth或外部因果对照时，不要声称“发现理论概念”

5. 不要在相关证据下宣称因果边界以外的因果结论

6. 不要为了显示方法全面而把不相关的LLM比较硬塞进正文；本文将其放在附录是有理由的

## 证据薄弱或跳跃的动作

1. “GDCM系数与Liu et al. (2019)接近”缺乏统计检验，且数据并不完全相同

2. “多样性提高recall”是机制推断，论文没有对每个概念逐一归因

3. 未知概念召回使用机器恢复概念作为伪ground truth，不能等同于真实科学新发现

4. 消融只单独变化单个超参数，未系统检验λ、η、ρ之间的交互

5. DonorsChoose和未知概念细节在在线附录，主文本读者无法核对

6. 将“GDCM+XGB可提高AUC”作为论据时可能模糊GDCM本身的可解释边界

## 一句话套路

先用概念理论把“概念”定义成可形式化的三元组并翻译成共享空间、距离和概念向量，再用可解释、多样、相关三个desiderata组织设计、评价与贡献，最后把工具限定为假设生成的引导探索而非因果推断引擎。

## 分析边界

在线附录B.1、B.2、B.5、B.6、C未提供，DonorsChoose、unknown concept recall和部分统计细节只能引用无法核对；图4、图5、图6、图7、图9为图片，具体数值只能依赖正文表述；Table 10中coherence与AUC在同一张表，但正文对某些baseline高coherence的讨论存在维度切换，需要读者判别；全文无页码，位置编码基于章节和段落序号估算；TopicGPT对比在Appendix A，主文本没有完整复述其提示和参数。
