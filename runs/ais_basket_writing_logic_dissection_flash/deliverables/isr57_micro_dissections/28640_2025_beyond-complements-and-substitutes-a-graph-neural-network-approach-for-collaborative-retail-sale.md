# Beyond Complements and Substitutes: A Graph Neural Network Approach for Collaborative Retail Sales Forecasting：ISR 句段级微观图谱

- 作者：Jing Liu; Gang Wang; Huimin Zhao; Mingfeng Lu; Lihua Huang; Gang Chen
- 年份：2025
- DOI：10.1287/isre.2023.0773
- 源文件：28640_2025_beyond-complements-and-substitutes-a-graph-neural-network-approach-for-collaborative-retail-sale.md
- 置信度：0.85

## 核实后的宏观骨架

文章遵循设计科学范式：引言从“关系赋能零售管理”切入，层层收敛到协作式零售销售预测（RSF），指出互补/替代二分法不足，形成RQ1（关系识别）与RQ2（关系利用）；随后以跨品类选择依赖理论（CCCDT）将产品关系沿关系类型和时间两个维度分解，确定三个元需求（Req1、Req2-1、Req2-2）；方法部分据此设计CL4RSF，包含SATE、DC-PRL、DRAI三个模块，并封装为端到端MS2RSF；实证部分在两个真实零售数据集上依次进行整体基准比较、关系识别策略替换、正负关系消融、异步关系消融，并辅以解释性分析和经济价值分析；最后在贡献部分提炼三个层面的贡献、两个可泛化设计原则、管理启示与局限。

## 摘要逐句图谱

### 1. Abstract S1

- order：1

- locator：Abstract S1

- paraphrase_cn：关系赋能的零售管理正受到越来越多的关注。

- move_code：CONTEXT_OPEN

- statement_status：fact

- why_here_cn：开篇用一个宽泛的学科动向建立论文所属问题域，让IS读者立即知道研究的宏观语境是“关系+零售管理”。

- inherits_from_previous_cn：无前句可继承，是摘要的起点。

- changes_argument_state_cn：设定议题域，并暗示后文要处理“关系”这一核心对象。

- sets_up_next_cn：为第二句聚焦到零售销售预测提供背景连接。

- failure_if_removed_cn：若删除，摘要直接从具体RSF问题开始，会失去抽象到具体的锚点，难以显示该研究属于关系赋能零售管理这一更大学术潮流。

- evidence_pointer：Abstract S1

### 2. Abstract S2

- order：2

- locator：Abstract S2

- paraphrase_cn：虽然已有研究承认利用相关产品信息可改善焦点产品的零售销售预测，但既有工作要么错误引入无关关系、要么遗漏有信息量的关系，且无法同时处理多面而复杂的产品关系。

- move_code：PROBLEM_AND_GAP

- statement_status：author_inference

- why_here_cn：从宏观背景收窄到本文的具体任务——协作RSF，并同时给出两个层次的问题：识别环节有噪声/遗漏，利用环节能力不足。

- inherits_from_previous_cn：承接“关系赋能零售管理”中的“关系”一词；第一句给出关系普遍性，第二句指出现有使用关系的方式有缺陷。

- changes_argument_state_cn：确立研究缺口，告诉读者当前知识状态不足以完成有效RSF。

- sets_up_next_cn：为第三至第五句引出理论视角、研究问题和制品做铺垫。

- failure_if_removed_cn：删除后，CCCDT和CL4RSF的引入会显得没有敌人的论证对象；摘要失去问题驱动结构。

- evidence_pointer：Abstract S2

### 3. Abstract S3

- order：3

- locator：Abstract S3

- paraphrase_cn：在互补/替代关系之外，基于跨品类选择依赖理论，我们从关系类型和时间两个维度辨别产品关系：正关系和负关系（类型维度，具有间接性和非对称性），以及异步和动态关系（时间维度）。

- move_code：THEORY_INTRO_AND_TAXONOMY

- statement_status：theory_claim

- why_here_cn：在摘要中提前给出全文的理论工具和关系分类法，让读者知道本文把产品关系从二分法扩展成六种可计算属性。

- inherits_from_previous_cn：前句说现有方法不能处理“多面复杂的产品关系”，此句给出作者认为应当如何认识这些关系（沿两个维度分解）。

- changes_argument_state_cn：从批判现状转向提出正面框架：CCCDT指导下的关系类型学。

- sets_up_next_cn：为下一句的三个研究问题/设计目标提供具体名称。

- failure_if_removed_cn：删除后，摘要中后续提出的CL4RSF“能够纳入上述关系”将失去具体所指。

- evidence_pointer：Abstract S3

### 4. Abstract S4

- order：4

- locator：Abstract S4

- paraphrase_cn：围绕如何精确且全面识别固有或重复的相关产品、如何同时利用间接/非对称/正/负关系、如何利用异步和动态关系，我们提出基于图神经网络的方法CL4RSF，它包含新的数据驱动产品关系识别策略并能纳入上述所有产品关系。

- move_code：RQ_AND_ARTIFACT_ANNOUNCE

- statement_status：design_decision

- why_here_cn：在摘要中同时呈现研究问题和制品名称，使读者知道本文既提出问题也给出可计算答案。

- inherits_from_previous_cn：直接使用上一句的关系维度列表作为三个“如何……”问题的宾语，形成理论—问题—方案的连贯链。

- changes_argument_state_cn：将理论分类转化为设计需求，并首次命名制品CL4RSF。

- sets_up_next_cn：下一句需要说明CL4RSF如何适配实际RSF场景，因而引出端到端架构。

- failure_if_removed_cn：删除后，摘要缺少研究问题表述，CL4RSF的命名和设计意图失去落脚点。

- evidence_pointer：Abstract S4

### 5. Abstract S5

- order：5

- locator：Abstract S5

- paraphrase_cn：为适应RSF情境，我们还设计了一个端到端深度学习架构，具备多步预测和多源信息融合能力。

- move_code：ARTIFACT_EXTENSION

- statement_status：design_decision

- why_here_cn：说明CL4RSF不是孤立的关系学习模型，而是封装进适合真实零售销售预测任务的端到端系统MS2RSF，从而连接方法与应用。

- inherits_from_previous_cn：前句提出CL4RSF用于关系识别和利用；此句指出它还需要被整合成可部署的预测架构。

- changes_argument_state_cn：把“方法”升级为“应用系统”，并预告实验中检验的对象是端到端方法。

- sets_up_next_cn：为下一句“实证评估两个真实数据集”提供被评估对象。

- failure_if_removed_cn：删除后，摘要中“在两个真实数据集上的实证评估”会缺少具体被评估的端到端方法。

- evidence_pointer：Abstract S5

### 6. Abstract S6

- order：6

- locator：Abstract S6

- paraphrase_cn：在两个真实零售数据集上的实证评估表明，所提出的端到端方法在预测性能上优于当前最优基准，并验证了CL4RSF关键设计组件和利用多种产品关系的效用。

- move_code：EMPIRICAL_RESULT_CLAIM

- statement_status：empirical_result

- why_here_cn：摘要需要在方案之后给出证据：两个数据集上的基准比较和组件验证，证明制品不只是一个概念设计。

- inherits_from_previous_cn：承接上一句提出的端到端架构，说明它确实在两个数据集上有效。

- changes_argument_state_cn：从“我们提出”转向“我们证明”，把设计主张转化为经验证据。

- sets_up_next_cn：为最后一句关于解释性分析的贡献留出空间。

- failure_if_removed_cn：删除后，CL4RSF的成效没有实证支撑，摘要无法说服读者制品有效。

- evidence_pointer：Abstract S6

### 7. Abstract S7

- order：7

- locator：Abstract S7

- paraphrase_cn：进一步的解释性分析揭示了跨品类效应和各种推断出的产品关系的洞见。

- move_code：MECHANISM_INSIGHT

- statement_status：empirical_result

- why_here_cn：在总体性能之后补上“为什么有效”的机制视角，暗示预测增益不是黑箱偶然，而是来自可解释的产品关系。

- inherits_from_previous_cn：前句已经展示性能提升，此句继续回答这些提升意味着什么（关系洞察）。

- changes_argument_state_cn：从分数比较转向意义阐释，为IS读者建立管理相关性。

- sets_up_next_cn：在摘要层面完成“背景—问题—理论—制品—证据—洞见”闭环，不需继续展开。

- failure_if_removed_cn：删除后，摘要只剩性能得分，缺少IS研究通常强调的机制/意义层面。

- evidence_pointer：Abstract S7

## 引言逐句图谱

### 1. Introduction P1 S1

- order：1

- locator：Introduction P1 S1

- paraphrase_cn：各类参与者之间的关系，如供应链伙伴合作、多渠道零售中的蚕食与互补、相邻地点的空间蚕食效应，普遍存在且对有效零售管理不可或缺。

- move_code：CONTEXT_BROAD

- statement_status：fact

- why_here_cn：全文第一句用多个IS/OM文献例子确立“关系”在零售管理中的核心位置，并暗示本研究聚焦的“产品关系”只是这一更大主题的一种。

- inherits_from_previous_cn：无，是引言起点。

- changes_argument_state_cn：建立问题域：关系无处不在且重要。

- sets_up_next_cn：下一句将“关系”从供应链/渠道/空间关系收窄到产品关系。

- failure_if_removed_cn：删除后，引言直接谈产品关系会显得没有零售管理大背景。

- evidence_pointer：Introduction P1 S1

### 2. Introduction P1 S2

- order：2

- locator：Introduction P1 S2

- paraphrase_cn：此外，探索产品关系对推荐、交叉销售、品类规划、货架空间分配等营销和运营活动也很重要，本研究聚焦利用与焦点产品相关的其他产品信息进行协作式零售销售预测（RSF），为生产、采购、营销、财务人力计划和库存管理等决策提供基础。

- move_code：NARROW_TO_PRODUCT_RELATION_AND_RSF

- statement_status：author_inference

- why_here_cn：从大背景收窄到本研究的具体焦点：产品关系用于协作RSF，并说明RSF的实际价值。

- inherits_from_previous_cn：由前句“关系在零售管理中重要”自然过渡到“产品关系也重要且本研究关注RSF”。

- changes_argument_state_cn：明确本文分析单元：其他产品信息→焦点产品销售的协作预测。

- sets_up_next_cn：为第二段介绍互补/替代传统定义铺垫概念前提。

- failure_if_removed_cn：删除后，读者不知道本研究具体预测任务是什么，后续所有文献和实验将失去锚定。

- evidence_pointer：Introduction P1 S2

### 3. Introduction P2 S1-S2

- order：3

- locator：Introduction P2 S1-S2

- paraphrase_cn：产品关系传统上主要被视为互补品和替代品；互补品是一起使用提升总效用的产品，替代品是功能相似可互换的产品。

- move_code：DEFINE_BASELINE_TAXONOMY

- statement_status：prior_literature

- why_here_cn：在正式批判前先精确给出互补/替代的经典定义，把要挑战的基线放在台面上。

- inherits_from_previous_cn：承接第一段提到的“产品关系”，现在定义最常被使用的产品关系概念。

- changes_argument_state_cn：确立传统二分法作为知识基线。

- sets_up_next_cn：第三段将指出该二分法在协作RSF中的结构性缺口。

- failure_if_removed_cn：删除后，后文“超越互补和替代”的标题和论证失去对照物。

- evidence_pointer：Introduction P2 S1-S2

### 4. Introduction P2 S3

- order：4

- locator：Introduction P2 S3

- paraphrase_cn：经济学意义上，若提高（或降低）一个产品的价格导致另一个产品销售增加，则二者为替代品（或互补品）；对互补品，一个产品销售增加通常伴随另一个销售增加，呈现正关系；对替代品，销售通常呈现负关系。

- move_code：DEFINE_SIGN_OF_RELATION

- statement_status：prior_literature

- why_here_cn：把价格定义与销售联动定义并置，为后文“正/负关系”的概念提前铺垫。

- inherits_from_previous_cn：前句定义互补/替代的一般含义，此句给出更形式化的经济学定义并引入正负记号。

- changes_argument_state_cn：建立“正关系=互补/负关系=替代”的简单对应，但也为后文指出该对应不充分作靶子。

- sets_up_next_cn：第三段将指出销售层面的关系并不等同于固有互补/替代。

- failure_if_removed_cn：删除后，摘要中的“positive and negative relations”概念缺乏引言端定义。

- evidence_pointer：Introduction P2 S3

### 5. Introduction P3 S1

- order：5

- locator：Introduction P3 S1

- paraphrase_cn：然而，互补/替代二分法无法完全覆盖对协作RSF可能有利的产品关系，因为产品之间在销售上是否有关系不仅由固有属性决定，还由消费者偏好决定。

- move_code：CRITIQUE_DICHOTOMY

- statement_status：author_inference

- why_here_cn：第一次正面挑战传统分类法，把论述从“二分法是什么”推向“二分法不够用”。

- inherits_from_previous_cn：直接使用第二段定义的互补/替代二分法作为被批评对象。

- changes_argument_state_cn：论证现有知识框架无法覆盖实际销售联动关系，为引出非本征关系铺垫。

- sets_up_next_cn：下一句用货架相邻和促销巧合两个例子具体化这一缺口。

- failure_if_removed_cn：删除后，P3 S2的两个反例缺乏统领句，会变成孤立例子。

- evidence_pointer：Introduction P3 S1

### 6. Introduction P3 S2

- order：6

- locator：Introduction P3 S2

- paraphrase_cn：例如，两个产品因在实体店货架上被邻近摆放而可能被许多顾客一起购买；虽然它们不是固有互补品，但销售可能呈现正相关。

- move_code：PHENOMENON_EXAMPLE_POSITIVE

- statement_status：author_inference

- why_here_cn：用一个常见零售现象说明非固有关系也能产生可用的正销售联动，反驳“只有固有互补才有正关系”。

- inherits_from_previous_cn：前句说销售关系由消费者偏好决定，此句给出具体机制（货架摆放影响购买）。

- changes_argument_state_cn：表明“非固有但重复出现”的正关系存在且有价值。

- sets_up_next_cn：下一句用促销巧合说明与重复关系相对的偶然关系应被排除。

- failure_if_removed_cn：删除后，后文“固有或重复关系”的“重复”标准缺少正向例证。

- evidence_pointer：Introduction P3 S2

### 7. Introduction P3 S3

- order：7

- locator：Introduction P3 S3

- paraphrase_cn：另一方面，例如两个产品因同时进行不同的促销活动而在销售上出现相似波动，这种相似只是巧合，不应推断为关系。

- move_code：PHENOMENON_EXAMPLE_TRANSIENT

- statement_status：author_inference

- why_here_cn：给出需要排除的反例，建立“固有/重复”与“偶然/暂时”的区分，这正是后文两个损失函数的设计动机。

- inherits_from_previous_cn：延续前句对“关系似乎存在但性质不同”的讨论，形成正/反两个例证。

- changes_argument_state_cn：确立识别标准：要识别固有或重复关系，同时防止偶然瞬时关系。

- sets_up_next_cn：把“一致性识别”这个概念留给第三段开头的研究问题，并直接引出RQ1。

- failure_if_removed_cn：删除后，图对比损失和鲁棒性损失“抑制瞬时关系/鼓励一致性”的设计会失去问题来源。

- evidence_pointer：Introduction P3 S3

### 8. Introduction P4 S1

- order：8

- locator：Introduction P4 S1

- paraphrase_cn：识别固有或重复的产品关系是协作RSF迫切的挑战性前提，现有努力要么错误引入无关关系，要么遗漏有信息量的关系。

- move_code：GAP_STATEMENT_1

- statement_status：author_inference

- why_here_cn：把前一段的例子升华为研究缺口总述，并作为本段展开文献批判的纲。

- inherits_from_previous_cn：从“有些关系需要识别、有些需要排除”的实例过渡到“识别本身是现有方法未能很好解决的问题”。

- changes_argument_state_cn：论证识别问题是RSF的迫切前提。

- sets_up_next_cn：接下来逐一批评同品类/共视、属性相似等具体识别策略。

- failure_if_removed_cn：删除后，P4 S2起的文献批判会缺少一个核心论断。

- evidence_pointer：Introduction P4 S1

### 9. Introduction P4 S2

- order：9

- locator：Introduction P4 S2

- paraphrase_cn：一些研究假设同品类或线上共视的产品即替代品，但Kwark等发现共视产品对中有47.23%的家居品类和20%的科技品类实际无关；纳入无关产品会引入过多噪声并损害预测。

- move_code：LITERATURE_CRITIQUE_NOISE

- statement_status：prior_literature

- why_here_cn：用具体数字证明基于类别/共视的关系识别会产生噪声，支撑“精确识别”的必要性。

- inherits_from_previous_cn：前句说现有方法容易引入无关关系，此句给出证据。

- changes_argument_state_cn：把“引入噪声”从抽象问题变成有统计证据的现象。

- sets_up_next_cn：下一句批评属性相似度方法，说明“全面识别”为何难。

- failure_if_removed_cn：删除后，“精确”维度的缺口缺少实证支撑。

- evidence_pointer：Introduction P4 S2, citing Kwark et al. 2021

### 10. Introduction P4 S3

- order：10

- locator：Introduction P4 S3

- paraphrase_cn：另一种常用方法是基于产品属性寻找相似产品，但难以列举所有有影响的属性；相似性可能沿可观察和潜在维度衡量，看似无关实则相关的产品（如尿布和啤酒）可能被忽略。

- move_code：LITERATURE_CRITIQUE_MISSING

- statement_status：prior_literature

- why_here_cn：与上一句互补：一种方法引入噪声，另一种方法遗漏信息，共同说明现有识别无法同时满足精确和全面。

- inherits_from_previous_cn：承接“要么引入噪声要么遗漏信息”的二分。

- changes_argument_state_cn：把“全面”维度的问题具体化为属性不可穷尽。

- sets_up_next_cn：为RQ1的正式表述提供最后一块证据。

- failure_if_removed_cn：删除后，RQ1中“comprehensively”一词没有文献支撑。

- evidence_pointer：Introduction P4 S3, citing Voleti et al. 2015 and Ma 2024

### 11. Introduction P4 S4

- order：11

- locator：Introduction P4 S4

- paraphrase_cn：总之，有效协作RSF需要精确且全面地识别固有或重复的产品关系，因此我们提出第一个研究问题：如何尽可能精确且全面地持续识别固有或重复的产品关系？

- move_code：RQ1_FORMAL

- statement_status：theory_claim

- why_here_cn：用“In summary”把前两句文献批评收拢成正式研究问题，让读者明确本文要回答的第一件事。

- inherits_from_previous_cn：综合P4 S2和S3的噪声与遗漏证据。

- changes_argument_state_cn：从批判转向提问，赋予后文PRL设计合法性。

- sets_up_next_cn：P5将给出PRL作为对RQ1的直接回应。

- failure_if_removed_cn：删除后，R1→RQ1→PRL的设计链条断裂，P5的设计出现没有任务目标。

- evidence_pointer：Introduction P4 S4

### 12. Introduction P5 S1-S2

- order：12

- locator：Introduction P5 S1-S2

- paraphrase_cn：为回应RQ1，我们设计了数据驱动的关系学习器PRL，用销售作为引导和监督信号，替代基于类别/共视的不现实假设和明确建模所有属性的不实际需求。

- move_code：SOLUTION_1_PRL

- statement_status：design_decision

- why_here_cn：第一次给出正向解决方案：以销售为监督信号，从数据中学习产品关系，绕开类别假设和属性穷举两个旧方法缺陷。

- inherits_from_previous_cn：直接回应RQ1中对精确/全面的要求。

- changes_argument_state_cn：从问题进入设计，指明关系识别的新路子。

- sets_up_next_cn：下一句需要解释PRL如何编码“识别固有/重复”的偏好，因而引入两个损失。

- failure_if_removed_cn：删除后，DC-PRL在方法部分的出现缺少引言端的概念铺垫。

- evidence_pointer：Introduction P5 S1-S2

### 13. Introduction P5 S3

- order：13

- locator：Introduction P5 S3

- paraphrase_cn：我们将对固有或重复关系一致性识别的偏好委托给损失项设计：图鲁棒性损失鼓励相关产品识别的一致性，图对比损失抑制偶然瞬时的关系；该对比损失会惩罚在大多数时期销售模式既不相似也不相反的产品连接。

- move_code：SOLUTION_1_DETAIL_LOSSES

- statement_status：design_decision

- why_here_cn：把RQ1中的“固有/重复”、“避免瞬时”翻译成两个可计算目标，预告方法部分4.3.1与4.3.2。

- inherits_from_previous_cn：前句说PRL用销售监督，此句进一步细化监督的具体形式。

- changes_argument_state_cn：将抽象偏好转化为具体损失机制，并使“识别一致性和去噪”可被实验检验。

- sets_up_next_cn：为实验2中CGSL（去掉两个损失）的对照提供引言级依据。

- failure_if_removed_cn：删除后，图鲁棒性损失和图对比损失的提出在方法部分会显得突然。

- evidence_pointer：Introduction P5 S3

### 14. Introduction P6 S1

- order：14

- locator：Introduction P6 S1

- paraphrase_cn：识别相关产品之后，另一个挑战性问题是如何厘清并适当利用这些关系进行协作RSF；鉴于消费者选择确实影响聚合销售，我们借鉴跨品类选择依赖理论（CCCDT），在互补/替代之外沿关系类型和时间维度分解产品关系。

- move_code：TURN_THEORY_AND_RQ2_SETUP

- statement_status：theory_claim

- why_here_cn：从“识别”转向“利用”，并引入CCCDT作为全文理论支柱。

- inherits_from_previous_cn：前文已解决“识别谁”（RQ1），此句提出“识别之后还需要知道关系性质并利用”。

- changes_argument_state_cn：引入理论框架，把产品关系从两类扩展为可计算的多维体系。

- sets_up_next_cn：下一句将用CCCDT具体列举六种关系，然后引出RQ2。

- failure_if_removed_cn：删除后，后文RQ2和所有设计的理论基础消失。

- evidence_pointer：Introduction P6 S1, citing Jiang et al. 2024, Russell et al. 1999, Shocker et al. 2004

### 15. Introduction P6 S2-S6

- order：15

- locator：Introduction P6 S2-S6

- paraphrase_cn：从类型维度，产品捆绑和跨品类考虑意味着正负产品关系，且这些关系可能是间接的（如电脑→打印机→打印纸）和非对称的（如主产品与附加品）；从时间维度，跨品类学习意味着异步影响，例如满意的小米手机用户可能购买小米扫地机器人（品牌溢出）；而且关系在类型和强度上都是动态的，如电动汽车与传统燃油车竞争力不断提高、摄像机与智能手机从互补变为替代。

- move_code：THEORY_TAXONOMY_DETAIL

- statement_status：theory_claim

- why_here_cn：用CCCDT的三个构念（跨品类考虑、产品捆绑、跨品类学习）加Shocker等的动态关系，具体阐述六种关系，为后文每个设计模块提供理论标签。

- inherits_from_previous_cn：从理论引入后展开其内容，并继续使用第二段建立的正负概念。

- changes_argument_state_cn：将“复杂关系”具体化为六个可识别、可计算的关系属性，为RQ2奠定分类基础。

- sets_up_next_cn：为P6末尾的RQ2和P7的GNN设计提供逐项需求来源。

- failure_if_removed_cn：若删除，表1中每个理论依据（product bundling、cross-category consideration、cross-category learning、dynamicity）失去引言端解释。

- evidence_pointer：Introduction P6 S2-S6, citing Ogaki 1990, Lee et al. 2013, Shocker et al. 2004

### 16. Introduction P6 S7-S8

- order：16

- locator：Introduction P6 S7-S8

- paraphrase_cn：来自其他相关产品的多面影响可以同时作用到焦点产品销售上，因此基于CCCDT我们力求同时利用正、负、间接、非对称、异步和动态产品关系进行协作RSF，并提出第二个研究问题：如何同时利用这些从类型和时间维度分解出的复杂关系？

- move_code：RQ2_FORMAL

- statement_status：theory_claim

- why_here_cn：把前面的关系分类汇总为“同时利用”的研究问题，强调与逐个处理不同。

- inherits_from_previous_cn：前面的六种关系描述直接成为RQ2的对象。

- changes_argument_state_cn：确立本研究的第二个任务：不只是识别，而是同时且差异化利用。

- sets_up_next_cn：P7开始回答RQ2：采用GNN并针对性设计模块。

- failure_if_removed_cn：删除后，P7的GNN定制和三个模块设计失去需要回应的目标。

- evidence_pointer：Introduction P6 S7-S8

### 17. Introduction P7 S1

- order：17

- locator：Introduction P7 S1

- paraphrase_cn：为回应RQ2，考虑到需要建模间接产品关系，我们采用图神经网络（GNN）方法。

- move_code：CHOOSE_PARADIGM

- statement_status：design_decision

- why_here_cn：解释为什么整体架构选择GNN：间接关系是GNN多跳传播的天然强项。

- inherits_from_previous_cn：RQ2中已包含“间接关系”，此句立即给出技术选择。

- changes_argument_state_cn：从理论需求走向技术范式选择。

- sets_up_next_cn：下一句指出现有GNN不足以处理负/异步/同时容纳多面关系，导出定制模块。

- failure_if_removed_cn：删除后，整篇采用GNN的决策缺少技术合理性说明。

- evidence_pointer：Introduction P7 S1

### 18. Introduction P7 S2-S4

- order：18

- locator：Introduction P7 S2-S4

- paraphrase_cn：然而现有GNN方法不能充分处理某些产品关系（特别是负关系和异步关系），也不能同时容纳所有这些复杂关系，因此我们定制针对RSF的GNN方法；首先，焦点产品应叠加正相关产品的效应并从自身扣除负相关产品的效应，为此考虑到非对称性设计了方向适用且关系自适应的信息交互器（DRAI）；其次，为同时利用同步和异步关系，将PRL扩展为双通道PRL（DC-PRL）并设计同步与异步感知时序编码器（SATE）。

- move_code：GAP_AND_THREE_MODULES_PREVIEW

- statement_status：design_decision

- why_here_cn：在引言中首次预告三个核心模块，并把每个模块与一个具体缺口/需求绑定。

- inherits_from_previous_cn：承接GNN采用决策，紧接着指出其不足。

- changes_argument_state_cn：从通用GNN转向RSF专属GNN设计，并列出模块名。

- sets_up_next_cn：P8将总结整个计算设计研究定位和实验发现。

- failure_if_removed_cn：删除后，方法部分三个模块的出现没有引言级路线图。

- evidence_pointer：Introduction P7 S2-S4

### 19. Introduction P8 S1

- order：19

- locator：Introduction P8 S1

- paraphrase_cn：综上，在这项计算设计研究中，基于CCCDT理论支撑下对各种产品关系的辨别，我们提出理论指导的GNN方法CL4RSF，包含SATE、DC-PRL和DRAI三个主要模块。

- move_code：ARTIFACT_SUMMARY

- statement_status：contribution_claim

- why_here_cn：引言汇总段第一句把全文定位为“计算设计研究+理论指导设计”，并正式命名制品。

- inherits_from_previous_cn：汇总前面所有需求、理论、模块。

- changes_argument_state_cn：从展开论证转入收束，建立整体贡献主张。

- sets_up_next_cn：下一句提及端到端MS2RSF，把模型从CL4RSF扩展为应用架构。

- failure_if_removed_cn：删除后，论文所属设计科学范式与CL4RSF命名缺乏明示。

- evidence_pointer：Introduction P8 S1, citing Rai 2017, Abbasi et al. 2024

### 20. Introduction P8 S2

- order：20

- locator：Introduction P8 S2

- paraphrase_cn：此外，我们将CL4RSF与其他影响因素整合进一个名为MS2RSF的端到端深度学习架构，具备多源信息融合和多步预测能力。

- move_code：END_TO_END_SYSTEM

- statement_status：design_decision

- why_here_cn：指出实际实验对象是MS2RSF而非单独的CL4RSF，为摘要和实验部分统一口径。

- inherits_from_previous_cn：直接承接CL4RSF，说明它被进一步封装为可用的预测系统。

- changes_argument_state_cn：明确“方法+系统”的双层制品结构。

- sets_up_next_cn：下一句自然过渡到实验结果。

- failure_if_removed_cn：删除后，摘要中的MS2RSF命名缺少引言来源。

- evidence_pointer：Introduction P8 S2

### 21. Introduction P8 S3-S4

- order：21

- locator：Introduction P8 S3-S4

- paraphrase_cn：在两个零售数据集上的实验中，我们的端到端方法优于Facebook Prophet、Amazon DeepAR及其他先进基准；实验结果还展示了CL4RSF关键组件和利用多种产品关系对协作RSF的效用。

- move_code：EXPERIMENT_PREVIEW

- statement_status：empirical_result

- why_here_cn：用一句话预告最重要的经验证据，给读者留下“方法有效”的初步印象。

- inherits_from_previous_cn：前句已定义被检验系统，此句报告其表现。

- changes_argument_state_cn：从设计主张进入证据预告，为后文实验部分预支结论。

- sets_up_next_cn：下一句用解释性分析收束引言。

- failure_if_removed_cn：删除后，引言缺少实证承诺，削弱读者继续阅读方法/实验的动力。

- evidence_pointer：Introduction P8 S3-S4

### 22. Introduction P8 S5

- order：22

- locator：Introduction P8 S5

- paraphrase_cn：进一步的解释性分析揭示了跨品类效应和各种被识别出的产品关系的洞见。

- move_code：MECHANISM_INSIGHT_CLOSE

- statement_status：empirical_result

- why_here_cn：在引言结尾强调“不仅性能好，还能产生关于产品关系的可解释洞见”，拔高贡献层次。

- inherits_from_previous_cn：前句已有性能证据，此句补上机制/意义证据。

- changes_argument_state_cn：完成引言从问题到设计到证据再到洞见的闭环。

- sets_up_next_cn：引导读者进入文献综述，了解这些缺口在文献中的位置。

- failure_if_removed_cn：删除后，引言收尾只停在性能上，缺少IS研究常有的意义层。

- evidence_pointer：Introduction P8 S5

## 引言逐段图谱

### 1. Introduction P1

- locator：Introduction P1

- opening_move_cn：以供应链、多渠道、空间蚕食等实例开篇，建立“关系在零售管理中的普遍性和重要性”。

- development_move_cn：继续引入产品关系对营销/运营活动的重要性，再收窄到协作RSF。

- pivot_move_cn：从“不同参与者的关系”转向“产品与产品之间的关系”。

- closing_move_cn：用RSF的管理决策价值（生产、采购、库存等）作为整段落点，制造下一段阐述传统产品关系分类的需要。

- paragraph_job_cn：为全文设定宏观问题域，并明确研究任务是协作RSF。

### 2. Introduction P2

- locator：Introduction P2

- opening_move_cn：直接给出互补/替代是传统主要分类的陈述。

- development_move_cn：用互补品/替代品的直观例子和经济学价格定义解释两类关系，并引入正/负销售关系。

- pivot_move_cn：无转折，本段完全服务于定义基线。

- closing_move_cn：以“正关系/负关系”收尾，制造第三段批判二分法对正负关系覆盖不足的需要。

- paragraph_job_cn：把将要被超越的传统分类法定义清楚，作为全文批评靶子。

### 3. Introduction P3

- locator：Introduction P3

- opening_move_cn：用“然而”直接否定二分法对协作RSF的充分性，并给出原因（销售关系由消费者偏好决定）。

- development_move_cn：通过货架相邻和促销巧合两个相反例子，区分非固有但重复的正关系和偶然瞬时相似。

- pivot_move_cn：从“什么关系应该被利用”转向“什么标准用于识别”，引出固有/重复与偶然/瞬时的界定。

- closing_move_cn：确立“应持续一致地识别固有或重复关系并防范瞬时关系”的标准，为RQ1奠定标准基础。

- paragraph_job_cn：论证二分法不足，并建立本文对产品关系的识别标准。

### 4. Introduction P4

- locator：Introduction P4

- opening_move_cn：用“识别固有或重复的产品关系是紧迫而具挑战的前提”总起，提出识别问题的两难。

- development_move_cn：分别用Kwark等的共视噪声数据和属性相似度遗漏例证，说明现有方法在精确/全面两个方向都失败。

- pivot_move_cn：从文献批评收拢到“因此需要精确且全面的识别”，并正式提出RQ1。

- closing_move_cn：以正式研究问题结尾，制造P5给出解决方案的需要。

- paragraph_job_cn：系统批判现有关系识别策略，并导出RQ1。

### 5. Introduction P5

- locator：Introduction P5

- opening_move_cn：以“作为对RQ1的回应”直接给出数据驱动关系学习器PRL。

- development_move_cn：说明PRL用销售监督、绕开类别/属性假设，并将其偏好编码为两个损失项。

- pivot_move_cn：从“用什么学习”转向“如何让学习体现精确/全面的偏好”。

- closing_move_cn：以图对比损失惩罚偶然连接收尾，制造下一步“识别之后如何利用”的需要。

- paragraph_job_cn：给出RQ1的初步设计答案，并预告两个关键损失。

### 6. Introduction P6

- locator：Introduction P6

- opening_move_cn：以“识别之后另一个挑战是如何厘清并利用关系”转入第二阶段问题。

- development_move_cn：引入CCCDT，将产品关系沿类型和时间两个维度展开，逐一说明正负、间接、非对称、异步、动态关系。

- pivot_move_cn：从“这些关系分别是什么”转向“它们可以同时作用，需要同时利用”。

- closing_move_cn：提出RQ2，制造P7设计定制GNN模块的需要。

- paragraph_job_cn：引入全文核心理论CCCDT，构建六种产品关系的分类体系，并导出RQ2。

### 7. Introduction P7

- locator：Introduction P7

- opening_move_cn：以“为回应RQ2，采用GNN”直接选择技术范式。

- development_move_cn：指出现有GNN处理负/异步/多面关系的能力不足，进而分别提出DRAI、DC-PRL和SATE。

- pivot_move_cn：从“通用GNN为什么不够”转向“我们如何定制”。

- closing_move_cn：以三个模块的名称和职责收尾，制造P8汇总贡献的需要。

- paragraph_job_cn：解释为什么必须定制GNN，并预告CL4RSF的三模块结构。

### 8. Introduction P8

- locator：Introduction P8

- opening_move_cn：以“总体来看，在这项计算设计研究中”对整个研究进行定位和命名。

- development_move_cn：依次概述CL4RSF、MS2RSF、实证结果和解释性洞见。

- pivot_move_cn：从方法设计转向证据和洞见，完成收束。

- closing_move_cn：以“解释性分析揭示跨品类效应和关系洞见”收尾，为文献综述创造阅读过渡。

- paragraph_job_cn：把全文概括为“理论指导设计+端到端系统+实证验证+可解释洞见”，确立贡献框架。

## 理论到设计逐句图谱

### 1. Design Rationales 3.1 P1 S1-S2

- order：1

- locator：Design Rationales 3.1 P1 S1-S2

- paraphrase_cn：健全的设计理性对确立设计科学贡献很重要，通过理论指导设计进行的有效抽象是确保IS设计研究论文在AI高速迭代时代具有健康生命力的关键。

- move_code：METHODOLOGICAL_JUSTIFICATION_FOR_THEORY

- statement_status：prior_literature

- why_here_cn：在进入具体理论前，先为“为什么要用理论指导设计”给出设计科学文献依据，回应IS审稿人对理论深度的期望。

- inherits_from_previous_cn：承接引言末尾宣称的“理论指导设计”，此处给出学术合法性。

- changes_argument_state_cn：把理论使用提升为研究设计方法本身。

- sets_up_next_cn：为CCCDT作为指导理论的选择提供标准。

- failure_if_removed_cn：删除后，后文大量CCCDT引用会显得仅仅是文献装饰而非方法论自觉。

- evidence_pointer：Section 3.1 P1, citing Gregor and Hevner 2013; Abbasi et al. 2024

### 2. Design Rationales 3.1 P2 S1-S5

- order：2

- locator：Design Rationales 3.1 P2 S1-S5

- paraphrase_cn：我们的设计从CCCDT开始，它框定了零售领域产品关系的概念特征，据此沿关系类型和时间维度分解并重组产品关系，并确定三个元需求（Req1、Req2-1、Req2-2），最终通过元设计产出制品CL4RSF（图1）。

- move_code：THEORY_TO_REQUIREMENTS_MAP

- statement_status：theory_claim

- why_here_cn：在理论引入后用一段话完整概述“理论→需求→设计→制品”的推导链，并给出图1作为视觉索引。

- inherits_from_previous_cn：前句说明理论指导设计的方法论价值，此句开始执行该方法论。

- changes_argument_state_cn：从“应该用理论”进入“我们用CCCDT具体推导出了哪些需求”，建立Req1/Req2-1/Req2-2。

- sets_up_next_cn：下一段展开CCCDT的三个跨品类效应，为需求提供更细内容。

- failure_if_removed_cn：删除后，三个元需求在全文中的位置缺少权威性入口。

- evidence_pointer：Section 3.1 P2, Figure 1

### 3. Design Rationales 3.1 P3 S1-S6

- order：3

- locator：Design Rationales 3.1 P3 S1-S6

- paraphrase_cn：在互补和替代之外还有其他关系；CCCDT识别三种跨品类效应：跨品类考虑（从多个替代品类中形成单一选择）、产品捆绑（多个产品共同满足需求，如尿布和啤酒故事）、跨品类学习（先前的购买经历影响后续产品选择）；前两者发生在单次或邻近购物场合，跨品类学习涉及顺序购买和时间扩展的捆绑；Shocker等还加入类型和强度的动态关系。

- move_code：THEORY_EXPOSITION_CCCDT

- statement_status：theory_claim

- why_here_cn：给出CCCDT的完整构念定义及例子，使后文的每个需求都能回指这些概念。

- inherits_from_previous_cn：承接P2对理论框架的概述，现在填充实质内容。

- changes_argument_state_cn：将“CCCDT指导”从空泛标签变为可操作的三类效应。

- sets_up_next_cn：为(1)关系类型视角和(2)时间视角两个小节的详细展开提供总纲。

- failure_if_removed_cn：删除后，正/负/异步/动态关系将没有理论来源。

- evidence_pointer：Section 3.1 P3, citing Russell et al. 1999; Shocker et al. 2004; Srivastava et al. 1984

### 4. Design Rationales 3.1 P4 (1) S1-S3

- order：4

- locator：Design Rationales 3.1 P4 (1) S1-S3

- paraphrase_cn：从类型视角看，产品捆绑和跨品类考虑使其他产品销售与焦点产品销售呈正或负关系；产品关系可能是间接的，引用Samuelson的茶/咖啡/奶油例子说明即使直接互补的产品也可能在另一组关系中成为间接替代。

- move_code：THEORY_PROPOSITION_INDIRECT

- statement_status：theory_claim

- why_here_cn：用经典经济学例子把“间接关系”从概念变成可感场景，为后续GNN多跳传播设计提供理论依据。

- inherits_from_previous_cn：承接P3中产品捆绑/跨品类考虑的概念。

- changes_argument_state_cn：说明“正/负关系”之外还有“间接性”这一属性。

- sets_up_next_cn：下一句继续补充非对称性。

- failure_if_removed_cn：删除后，方法部分用GNN建模间接关系的选择失去理论动力。

- evidence_pointer：Section 3.1 P4, citing Samuelson 1974; Ogaki 1990; Jabr and Zheng 2014

### 5. Design Rationales 3.1 P4 (1) S4

- order：5

- locator：Design Rationales 3.1 P4 (1) S4

- paraphrase_cn：大量研究指出产品关系的非对称性，即一个产品可能更依赖另一个产品，例如主产品销量一般正向影响附加品销量，反向影响却很小。

- move_code：THEORY_PROPOSITION_ASYMMETRY

- statement_status：theory_claim

- why_here_cn：引入非对称性，为后续磁拉普拉斯矩阵和方向适用DRAI提供需求来源。

- inherits_from_previous_cn：前句处理间接性，此句处理同属类型维度的非对称性，与表1中新意(4)对应。

- changes_argument_state_cn：建立“产品关系有方向”的意识。

- sets_up_next_cn：后文方法部分将面对“谱方法需要对称矩阵”与“非对称关系需求”的冲突。

- failure_if_removed_cn：删除后，磁拉普拉斯设计的合理性无法被理解。

- evidence_pointer：Section 3.1 P4 S4, citing Lee et al. 2013; Voleti et al. 2015; Gelper et al. 2016; Huang et al. 2019

### 6. Design Rationales 3.1 P5 (2) S1-S3

- order：6

- locator：Design Rationales 3.1 P5 (2) S1-S3

- paraphrase_cn：从时间视角看，CCCDT中的跨品类学习意味着之前购买的其他产品可能在之后对焦点产品销售产生异步影响，例如顾客使用品牌产品后产生好感进而购买同品牌其他产品（品牌溢出效应），这是产品间异步影响的一种可能机制。

- move_code：THEORY_PROPOSITION_ASYNCHRONY

- statement_status：theory_claim

- why_here_cn：用品牌溢出例子解释“异步影响”，为SATE和DC-PRL的异步图/虚拟节点设计提供理论合法性。

- inherits_from_previous_cn：直接使用P3中跨品类学习的定义。

- changes_argument_state_cn：把时间维度加入关系分类，需求从“识别谁”扩展到“何时发生影响”。

- sets_up_next_cn：下一句转向动态性。

- failure_if_removed_cn：删除后，异步关系消融实验（实验4）会失去理论理由。

- evidence_pointer：Section 3.1 P5 S1-S3

### 7. Design Rationales 3.1 P5 (2) S4-S5

- order：7

- locator：Design Rationales 3.1 P5 (2) S4-S5

- paraphrase_cn：关系动态性表现在两方面：关系类型可转变（如摄像机与智能手机从互补变为替代、两个手机可作备份而共存），关系强度随时间变化（市场环境动态）。

- move_code：THEORY_PROPOSITION_DYNAMICITY

- statement_status：theory_claim

- why_here_cn：为“动态关系”提供类型转变和强度变化两个子维度，后文DRAI的tanh注意力同时处理这两者。

- inherits_from_previous_cn：前句处理异步性，此句处理动态性，共同构成时间维度。

- changes_argument_state_cn：确立“关系不是静态标签，而是随时间变化的量”。

- sets_up_next_cn：方法部分4.4将对“类型动态”和“强度动态”分别给出机制。

- failure_if_removed_cn：删除后，tanh激活函数、动态注意力可视化的解释缺少理论依据。

- evidence_pointer：Section 3.1 P5 S4-S5, citing Shocker et al. 2004

### 8. Methodological Challenges 3.2 P1 S1-S4

- order：8

- locator：Methodological Challenges 3.2 P1 S1-S4

- paraphrase_cn：这些关系需求对协作RSF构成重大方法论挑战，特别是同时而非单独地容纳间接、非对称、正、负、异步、动态关系；例如用谱信号建模正负关系时同时建模非对称关系会带来新挑战；又如同时处理同步和异步关系时，通常每个产品只分配一个嵌入，这很棘手。

- move_code：REQUIREMENT_TO_METHOD_CHALLENGE

- statement_status：author_inference

- why_here_cn：把理论需求翻译成方法设计中的障碍，说明不能直接套用现有GNN。

- inherits_from_previous_cn：前一小节给出了所有理论关系，此节开始量化这些关系给计算模型带来的难度。

- changes_argument_state_cn：从“需要什么”进入“难点是什么”，为每个模块的定制设计提供动机。

- sets_up_next_cn：为P2-P4逐项给出Req1/Req2-1/Req2-2的解决方案。

- failure_if_removed_cn：删除后，方法部分的每个创新点（磁拉普拉斯、虚拟节点等）缺少“为什么不能简单做”的论证。

- evidence_pointer：Section 3.2 P1

### 9. Methodological Challenges 3.2 P2 S1-S6

- order：9

- locator：Methodological Challenges 3.2 P2 S1-S6

- paraphrase_cn：针对Req1，我们设计基于图结构学习的PRL，利用可学习参数推断图连边；为简单和建模非对称能力，采用基于余弦相似度的kNN图；但现有GSL一般无约束，可能不利于持续识别固有或重复关系；为此设计图鲁棒性损失（鼓励相似度分布偏离均匀分布）和图对比损失（使连接节点相似或相反、非连接节点既不相似也不相反），并对对比损失修改相似度度量以考虑相反销售模式。

- move_code：REQ1_TO_PRL_DESIGN

- statement_status：design_decision

- why_here_cn：把Req1的精确/全面/一致性目标落实到两个损失函数和kNN图学习上，并解释对一般对比学习的零售域适配。

- inherits_from_previous_cn：直接回应上一段的“挑战”，并衔接引言P5已简要提出的PRL。

- changes_argument_state_cn：从需求到具体可计算设计转化。

- sets_up_next_cn：后文方法部分4.3将正式给出这些损失的公式。

- failure_if_removed_cn：删除后，实验2中CGSL（无两个损失）的对照设计失去理论解释。

- evidence_pointer：Section 3.2 P2

### 10. Methodological Challenges 3.2 P3 S1-S3

- order：10

- locator：Methodological Challenges 3.2 P3 S1-S3

- paraphrase_cn：针对Req2-1，需要计算模型能差异化利用正负关系，同时容纳间接和非对称关系；常规GCN本质是低通滤波器，能探索正关系但不能处理负关系，因为振荡（高频）信号会被滤除；为此设计将正负关系映射到低/高频信号的策略，与用不同边类型区分正负关系的方法相比，避免GSL复杂度并绕开不平衡路径问题；由于谱方法数学基础要求对称矩阵，而零售场景需要非对称关系，因此引入磁拉普拉斯矩阵，贡献方向适用的谱GNN方法。

- move_code：REQ2-1_TO_DRAI_DESIGN

- statement_status：design_decision

- why_here_cn：详细解释DRAI的两个关键决策（频谱映射正负、磁拉普拉斯处理非对称），说明它们分别解决低通滤波限制和对称矩阵限制。

- inherits_from_previous_cn：承接P1提出的两个挑战（正负同时建模、非对称与谱方法冲突）。

- changes_argument_state_cn：从需求到具体技术方案，并预告与FAGCN/SGCN的差异。

- sets_up_next_cn：后文4.4中的MagNet/FAGCN实现和实验3的正负消融都以此为依据。

- failure_if_removed_cn：删除后，DRAI模块的核心创新点和实验3的对照目标消失。

- evidence_pointer：Section 3.2 P3

### 11. Methodological Challenges 3.2 P4 S1-S6

- order：11

- locator：Methodological Challenges 3.2 P4 S1-S6

- paraphrase_cn：针对Req2-2，需要计算模型能处理异步和动态关系；同时利用同步与异步关系的关键挑战是每个产品通常只有一个嵌入；为此设计双通道PRL，一个通道学习同步图、另一个学习异步图，异步图中为每个产品分配“previous_”和“current_”两个虚拟节点，只允许从前节点指向当前节点；为表达异步时间模式，以滑动窗口生成多个前序时间区间并用注意力融合；为建模动态关系类型和强度，采用范围[-1,1]的注意力激活函数，使注意力可判断当前时期主导关系类型并自适应接收信息。

- move_code：REQ2-2_TO_DC_PRL_SATE_DESIGN

- statement_status：design_decision

- why_here_cn：将异步和动态需求映射到三个具体设计：双通道图、虚拟节点、注意力机制，并解释每种设计的必要性。

- inherits_from_previous_cn：承接P1中“同步与异步同时处理”的挑战。

- changes_argument_state_cn：把时间维度需求落实为可执行的架构特征。

- sets_up_next_cn：后文4.2/4.3/4.4会分别详细实现SATE、DC-PRL、DRAI。

- failure_if_removed_cn：删除后，实验4和动态关系解释性分析失去设计层面的依据。

- evidence_pointer：Section 3.2 P4

## 制品设计理由逐句图谱

### 1. Proposed Method 4.1 P1 S1-S7

- order：1

- locator：Proposed Method 4.1 P1 S1-S7

- paraphrase_cn：CL4RSF架构中SATE提供同步和异步时序模式作为初始产品表示，DC-PRL分别学习异步图和同步图，异步图中每个产品有“previous_”和“current_”两个虚拟节点，DRAI在两类图上分别传播生成两个隐藏嵌入后融合用于下游预测，所有模块联合训练以避免误差传播。

- move_code：ARCHITECTURE_OVERVIEW

- statement_status：design_decision

- why_here_cn：在详细公式前先给出系统级数据流，让读者理解三模块如何组合、为什么联合训练。

- inherits_from_previous_cn：直接实现3.2节三个需求的设计方案，并给出图3作为视觉化总览。

- changes_argument_state_cn：把散落的单个解决方案组织为一个可运行架构。

- sets_up_next_cn：后续4.2-4.5小节按模块顺序详细展开。

- failure_if_removed_cn：删除后，方法部分将只有碎片化模块，缺少整体结构。

- evidence_pointer：Section 4.1, Figure 3

### 2. Proposed Method 4.2 P1 S1-S4

- order：2

- locator：Proposed Method 4.2 P1 S1-S4

- paraphrase_cn：鉴于销售序列的序列性，采用GRU而非LSTM以提升效率；用GRU计算同步图节点初始表示并取最后时间步；为探索异步关系，生成w1个滑动窗口异步序列，用注意力机制融合各前序时间段的隐藏表示，得到异步图中“previous_”节点的初始表示。

- move_code：SATE_DESIGN_RATIONALE

- statement_status：design_decision

- why_here_cn：解释SATE为什么用GRU、如何初始化两种节点、如何用注意力融合多个历史时段，使异步关系可被表达。

- inherits_from_previous_cn：直接承接4.1中“SATE提供初始表示”的职责。

- changes_argument_state_cn：把“异步表示”落实到序列编码层面。

- sets_up_next_cn：4.3将展示DC-PRL如何在这些表示上学习图。

- failure_if_removed_cn：删除后，异步虚拟节点没有初始特征来源，图学习无法运行。

- evidence_pointer：Section 4.2

### 3. Proposed Method 4.3 P1 S1-S5

- order：3

- locator：Proposed Method 4.3 P1 S1-S5

- paraphrase_cn：DC-PRL学习同步和异步两类有向图，节点代表产品、边代表关系；邻接矩阵中Aij表示从节点j到i的有向边，通过归一化点积相似度取Topk邻居；异步图使用u_i与v_j的点积，其中v_j是“previous_”虚拟节点嵌入；最终异步图邻接矩阵将“previous_”到“current_”部分设为A1，并限制从当前到之前的信息泄漏。

- move_code：DC_PRL_GRAPH_LEARNING_RATIONALE

- statement_status：design_decision

- why_here_cn：定义图结构学习的具体机制，特别是异步图的方向性和禁止信息泄漏，保证异步关系的因果方向。

- inherits_from_previous_cn：实现3.2中Req2-2的双通道虚拟节点设计。

- changes_argument_state_cn：把异步关系编码为有向图，并规定方向语义。

- sets_up_next_cn：随后4.3.1和4.3.2分别给出两个损失，以约束图学习。

- failure_if_removed_cn：删除后，实验2中“DC-PRL优于CGSL”的对比没有图学习机制细节支撑。

- evidence_pointer：Section 4.3

### 4. Proposed Method 4.3.1 P1 S1-S2

- order：4

- locator：Proposed Method 4.3.1 P1 S1-S2

- paraphrase_cn：图鲁棒性损失鼓励每个节点的相似度分布偏离均匀分布，从而在多次实验中保持Topk邻居一致性，用KL散度度量与均匀分布的距离并给出损失式。

- move_code：GRAPH_ROBUSTNESS_LOSS_RATIONALE

- statement_status：design_decision

- why_here_cn：把“一致性识别”偏好转化为一项可直接优化并测试的损失，是PRL相对普通GSL的核心创新之一。

- inherits_from_previous_cn：承接3.2 P2对图鲁棒性损失的设计动机。

- changes_argument_state_cn：从文字动机进入数学形式，使“一致性”可计算。

- sets_up_next_cn：下一小节给出图对比损失，两个损失共同构成联合损失函数。

- failure_if_removed_cn：删除后，DC-PRL与CGSL的性能差无法归因于鲁棒性正则。

- evidence_pointer：Section 4.3.1

### 5. Proposed Method 4.3.2 P1 S1-S4

- order：5

- locator：Proposed Method 4.3.2 P1 S1-S4

- paraphrase_cn：图对比损失以观察到的销售历史为监督，将连接节点视为正样本、非连接节点为负样本，采用InfoNCE目标；为考虑负相关产品，将相似度度量改为绝对余弦相似度。

- move_code：GRAPH_CONTRASTIVE_LOSS_RATIONALE

- statement_status：design_decision

- why_here_cn：解释对比损失如何利用销售序列区分真实关系与偶然相似，并说明“绝对值”修改为何必要（负关系也应是连接候选）。

- inherits_from_previous_cn：承接3.2 P2中“相邻节点应相似或相反”的零售域适配动机。

- changes_argument_state_cn：使负关系也能驱动图连接，与DRAI对正负关系的利用形成配套。

- sets_up_next_cn：为实验2中CGSL（无两个损失）的劣化提供可验证预期。

- failure_if_removed_cn：删除后，模型对“偶然瞬时关系”的抑制没有机制保证。

- evidence_pointer：Section 4.3.2

### 6. Proposed Method 4.4 P1 S1-S3

- order：6

- locator：Proposed Method 4.4 P1 S1-S3

- paraphrase_cn：同步图和异步图中的方向信息含义不同：同步图表示非对称关系，异步图表示序列依赖；因此DRAI对两类图采用不同实现，同步图用基于磁拉普拉斯的MagNet，异步图用FAGCN以避免信息泄漏。

- move_code：DRAI_TWO_IMPL_RATIONALE

- statement_status：design_decision

- why_here_cn：统一解释为什么同一个DRAI有两种实现，防止读者对“同一模块为何两种做法”产生困惑。

- inherits_from_previous_cn：承接4.3中两类图的定义。

- changes_argument_state_cn：把方向语义差异转换为技术实现差异。

- sets_up_next_cn：随后用公式(13)-(16)定义同步图上的低频/高频滤波与注意力，并在段尾说明异步图用FAGCN。

- failure_if_removed_cn：删除后，读者可能误以为DRAI实现矛盾。

- evidence_pointer：Section 4.4 P1

### 7. Proposed Method 4.4 P2-S3 (公式13-16后)

- order：7

- locator：Proposed Method 4.4 P2-S3 (公式13-16后)

- paraphrase_cn：通过tanh激活的注意力系数αG可在[-1,1]变化，正值表示正关系主导、负值表示负关系主导，且系数依赖随时间变化的节点表示，因此既能自适应确定主导关系类型，也能建模动态关系；随后给出MagNet-DRAI的卷积式并说明对复数输出的处理。

- move_code：DRAI_SPECTRAL_AND_DYNAMIC_RATIONALE

- statement_status：design_decision

- why_here_cn：这是DRAI的核心论证：一个注意力机制同时实现正负关系选择、非对称方向编码和动态类型/强度建模，从而同时满足Req2-1和Req2-2中的动态需求。

- inherits_from_previous_cn：前一段说明了磁拉普拉斯和低频/高频滤波，此段把注意力系数与正负主导关系挂钩。

- changes_argument_state_cn：将谱信号与关系语义连接，使正负关系可被差异化传播。

- sets_up_next_cn：为实验3（正负消融）和解释性分析中的正负/动态注意力可视化提供直接依据。

- failure_if_removed_cn：删除后，DRAI对正负关系同时利用的机制失去解释，实验3的预期结果也无从推导。

- evidence_pointer：Section 4.4, 公式13-16

### 8. Proposed Method 4.5 P1 S1-S3

- order：8

- locator：Proposed Method 4.5 P1 S1-S3

- paraphrase_cn：为适配RSF，将CL4RSF与多源信息融合、多步预测整合为端到端网络MS2RSF，以MAE作为预测损失并加入图鲁棒性损失和图对比损失的加权项，最终损失从解码器输出反传整个架构。

- move_code：END_TO_END_ARCHITECTURE_RATIONALE

- statement_status：design_decision

- why_here_cn：解释为什么需要MS2RSF而非只在CL4RSF内预测，说明多源信息、多步预测和联合优化的系统级设计。

- inherits_from_previous_cn：前面三个模块已定义，此处将它们与RSF实际需求封装在一起。

- changes_argument_state_cn：从模型到应用系统，明确实验中所有性能比较的对象。

- sets_up_next_cn：为实验部分确定“检验MS2RSF整体+组件消融”的设计。

- failure_if_removed_cn：删除后，摘要和实验中的MS2RSF名称失去方法端定义。

- evidence_pointer：Section 4.5

## Study开头、过渡与收束图谱

### 1. Experiments 5.1 opening P1-S1

- order：1

- locator：Experiments 5.1 opening P1-S1

- paraphrase_cn：为评估所设计方法的有效性，我们在两个真实零售数据集Drugs和Grocery上做了一系列实验。

- move_code：EVALUATION_OPEN

- statement_status：method_decision

- why_here_cn：交代实验开始，并提前给出两个数据集的名称，为后文分别描述数据特征设框架。

- inherits_from_previous_cn：承接方法部分MS2RSF被检验的需要。

- changes_argument_state_cn：从设计转入评价。

- sets_up_next_cn：下一句开始描述Drugs数据集的来源和规模。

- failure_if_removed_cn：删除后，实验部分失去开篇引导。

- evidence_pointer：Section 5.1 P1 S1

### 2. Experiments 5.1 Drugs description S2-S6

- order：2

- locator：Experiments 5.1 Drugs description S2-S6

- paraphrase_cn：Drugs数据集包含3700多万条交易记录、15077个SKU、240家药店；我们选择呼吸系统和心血管疾病两类药物，因为它们看似无关联但在销售上可能相关（如天气等共同因素），以突显识别微妙相关产品的挑战并强调DC-PRL的能力；按周聚合交易，并依据无连续缺失和相同时间跨度原则筛选150个SKU，还引入每周平均气温。

- move_code：DATASET_JUSTIFICATION

- statement_status：method_decision

- why_here_cn：详细说明Drugs数据选择两类的理由，使数据集的构造直接服务于检验跨品类微妙关系的核心假设。

- inherits_from_previous_cn：从“两个数据集”介绍进入第一个数据集的结构描述。

- changes_argument_state_cn：将抽象研究问题转化为可检验的数据场景。

- sets_up_next_cn：下一段描述Grocery数据集，形成两个互补场景。

- failure_if_removed_cn：删除后，实验2和解释性分析中的跨品类效应证据缺少数据设计基础。

- evidence_pointer：Section 5.1 P1 S2-S6

### 3. Experiments 5.1 Grocery description S1-S3

- order：3

- locator：Experiments 5.1 Grocery description S1-S3

- paraphrase_cn：Grocery数据集来自Corporación Favorita，我们选择18号店铺的数据以支持单店决策，筛选209个SKU、覆盖11个产品族，并纳入促销和节假日变量。

- move_code：DATASET_JUSTIFICATION_2

- statement_status：method_decision

- why_here_cn：描述第二个数据集，与Drugs形成对照：广泛品类、单店、含促销节假日。

- inherits_from_previous_cn：承接第一个数据集描述，补上第二个场景。

- changes_argument_state_cn：提供外部效度的第二个支点。

- sets_up_next_cn：下一句解释两数据集采样策略不同的原因。

- failure_if_removed_cn：删除后，Grocery实验结果缺少数据来源和选择合理性。

- evidence_pointer：Section 5.1 P2-S1-S3

### 4. Experiments 5.1 S4-S5

- order：4

- locator：Experiments 5.1 S4-S5

- paraphrase_cn：我们分别以聚焦预测（Drugs中两个选定的产品类别、全店聚合）和广泛预测（Grocery中单店所有产品）两种方式构造数据，以评估不同场景；为稳健性还在完整数据集上比较（在线附录E）；按时间顺序以6:2:2划分训练/验证/测试，最大最小归一化并在评价时还原尺度。

- move_code：EXPERIMENT_DESIGN_RATIONALE

- statement_status：method_decision

- why_here_cn：解释两种采样策略的互补性、时间划分的时序逻辑和归一化处理，为后续统计对比的公平性提供依据。

- inherits_from_previous_cn：前两句分别描述两数据集，此句解释为何构造方式不同。

- changes_argument_state_cn：确立实验评价方法，防止数据泄漏和尺度偏差。

- sets_up_next_cn：5.2主实验部分将列出基准和四个实验。

- failure_if_removed_cn：删除后，结果中两个数据集的差异无法归因于场景设计。

- evidence_pointer：Section 5.1 S4-S5

### 5. Experiments 5.2 opening S1-S3

- order：5

- locator：Experiments 5.2 opening S1-S3

- paraphrase_cn：我们进行了四个主要实验：实验1比较端到端MS2RSF与10个基准；实验2用其他关系识别策略替换DC-PRL；实验3通过消融检验正负关系的效用；实验4比较有异步与无异步的预测性能。

- move_code：EXPERIMENT_ROADMAP

- statement_status：method_decision

- why_here_cn：在结果前明确四个实验的各自目标，让读者理解每一部分证据回答哪个问题。

- inherits_from_previous_cn：用前文三个需求（Req1/Req2-1/Req2-2）组织实验结构：实验2对应Req1，实验3对应Req2-1，实验4对应Req2-2。

- changes_argument_state_cn：把全文从“我们设计了什么”转向“我们如何检验”。

- sets_up_next_cn：随后逐一说明10个基准和方法实现细节。

- failure_if_removed_cn：删除后，结果部分四个小节的排列缺乏路线图。

- evidence_pointer：Section 5.2 S1-S3

### 6. Experiments 5.2 benchmark description B1-B10

- order：6

- locator：Experiments 5.2 benchmark description B1-B10

- paraphrase_cn：选择Prophet、DeepAR、TFT、STGCN、DCRNN、DeepGLO、MTGNN、GTS、Shopper-GAT和MSGNet作为基准，并解释每个方法的基本机制和如何适配RSF；其中STGCN/DCRNN以相似度图为输入，Shopper-GAT基于Shopper推断的潜在特征构造图，DeepGLO等纳入所有序列，MTGNN/GTS/MSGNet进行图学习。

- move_code：BENCHMARK_SELECTION_JUSTIFICATION

- statement_status：method_decision

- why_here_cn：通过覆盖统计、概率RNN、Transformer、时域GNN、图学习GNN、矩阵分解、购物篮模型等类别，使主实验的对比谱系完整。

- inherits_from_previous_cn：承接实验1的定义，解释所选基准如何代表不同技术路线。

- changes_argument_state_cn：建立与MS2RSF对比的基线集合，并透露各基准的关系来源（相似度图、图学习、购物篮推断等），为后文解释性能差异埋下伏笔。

- sets_up_next_cn：后续实验2-4的设计、结果解释以及贡献部分的benchmark叙事都可依据这里的分类。

- failure_if_removed_cn：删除后，表格2-3的结果缺乏解释框架。

- evidence_pointer：Section 5.2 benchmark list

### 7. Experiments 5.2 metrics and statistics S1-S2

- order：7

- locator：Experiments 5.2 metrics and statistics S1-S2

- paraphrase_cn：使用MAE和RMSE，每个深度学习方法重复10次不同随机初始化，进行超参数敏感性分析、DM检验和Bonferroni校正，解释性分析见在线附录I。

- move_code：EVALUATION_PROTOCOL

- statement_status：method_decision

- why_here_cn：说明性能估计可靠性、显著性检验和敏感性分析，增强结果的统计可信度。

- inherits_from_previous_cn：前面已列出基准和实验，此段补充测量和检验方式。

- changes_argument_state_cn：把性能比较置于严格统计框架内。

- sets_up_next_cn：5.3结果部分将按实验1-4的顺序报告。

- failure_if_removed_cn：删除后，文中所有均值±标准差和DM检验失去协议基础。

- evidence_pointer：Section 5.2 metrics

### 8. Experiment 1 result 5.3.1 P1 S1-S3

- order：8

- locator：Experiment 1 result 5.3.1 P1 S1-S3

- paraphrase_cn：实验1表明MS2RSF在两个数据集、所有预测视界、MAE和RMSE上一致优于所有基准；优势随h增加而增大，主要来自异步关系探索；它优于其他考虑跨序列依赖的深度方法，说明识别合适相关产品并利用多样产品关系的重要性。

- move_code：OVERALL_RESULT_CLAIM

- statement_status：empirical_result

- why_here_cn：报告核心性能证据，并立即给出“优势随h增大”的初步归因，指向异步关系消融。

- inherits_from_previous_cn：直接依据表格2-3。

- changes_argument_state_cn：确立整体有效性，但也制造“为什么好”的问题。

- sets_up_next_cn：后文从“哪些基准忽略了什么”过渡到实验2-4的组件归因。

- failure_if_removed_cn：删除后，全文最重要的总体性能主张缺失。

- evidence_pointer：Section 5.3.1, Tables 2-3

### 9. Experiment 1 result 5.3.1 P2-S1-S2

- order：9

- locator：Experiment 1 result 5.3.1 P2-S1-S2

- paraphrase_cn：在识别相关产品方面，DeepGLO不加区分纳入所有序列，STGCN/DCRNN用销售相关图，MTGNN/GTS/MSGNet做图学习，Shopper用序列概率模型推断替代和互补；在利用关系方面，几乎所有基准忽视负关系和异步关系。

- move_code：BENCHMARK_INTERPRETATION

- statement_status：author_inference

- why_here_cn：用基准的关系来源和关系类型编码解释性能差距：MS2RSF胜出是因为它做了“识别+多面利用”。

- inherits_from_previous_cn：承接5.2的基准描述，并在结果后赋予解释功能。

- changes_argument_state_cn：把分数差异转化为设计差异的论证。

- sets_up_next_cn：为后续组件实验提供基准层面的整体解读。

- failure_if_removed_cn：删除后，主实验结果只是数字，无法说明哪些设计选择带来增益。

- evidence_pointer：Section 5.3.1 P2

### 10. Experiment 1 result 5.3.1 P3-S1-S3

- order：10

- locator：Experiment 1 result 5.3.1 P3-S1-S3

- paraphrase_cn：与优性能基准相比，MS2RSF呈现更强泛化性：例如MSGNet在Grocery数据上表现良好但在Drugs长视界上因参数过多的自注意力而欠佳；Drugs中最优基准Shopper-GAT在Grocery中因缺乏细粒度购物篮数据而不可行。

- move_code：GENERALIZABILITY_AND_BASELINE_LIMIT

- statement_status：empirical_result

- why_here_cn：指出单个基准无法稳定适用两个场景，进而强调本文方法不依赖购物篮数据、对细粒度数据缺失更鲁棒。

- inherits_from_previous_cn：紧承表格2-3中MSGNet和Shopper-GAT的表现差异。

- changes_argument_state_cn：把性能优势延伸到场景泛化能力的论证。

- sets_up_next_cn：为实验2中Shopper在Drugs识别正关系失败的解释铺垫。

- failure_if_removed_cn：删除后，Shopper-GAT在Grocery中的缺失可能需要单独解释。

- evidence_pointer：Section 5.3.1 P3

### 11. Experiment 2 result 5.3.2 P1-S1-S2

- order：11

- locator：Experiment 2 result 5.3.2 P1-S1-S2

- paraphrase_cn：表格4-5表明DC-PRL一致优于几种现有关系识别策略，验证了它稳健有效识别相关产品的效用；类别和共购策略性能下降主要因为引入过多噪声，且类别策略无法利用跨品类关系。

- move_code：COMPONENT_RESULT_PRI

- statement_status：empirical_result

- why_here_cn：报告实验2主要结论，把性能下降归因于关系标签噪声和跨品类缺失，与引言P4的缺口形成呼应。

- inherits_from_previous_cn：依据表格4-5的结果。

- changes_argument_state_cn：证明DC-PRL相对旧识别策略的价值。

- sets_up_next_cn：下一句用注意力分数图5进一步解释这些策略引入噪声的机制。

- failure_if_removed_cn：删除后，RQ1的设计答案缺乏实证支撑。

- evidence_pointer：Section 5.3.2 P1, Tables 4-5

### 12. Experiment 2 result 5.3.2 P2-S1-S4

- order：12

- locator：Experiment 2 result 5.3.2 P2-S1-S4

- paraphrase_cn：图5显示类别策略下正负关系共存、共购策略主要捕捉正关系，但二者注意力分数绝对值较小，说明确实引入噪声；DRAI给噪声分配较小注意力从而缓解其负面影响。

- move_code：MECHANISM_VISUALIZATION_PRI

- statement_status：empirical_result

- why_here_cn：用注意力分数可视化把“噪声”转化为可观察现象，并揭示DRAI如何进一步吸收剩余噪声。

- inherits_from_previous_cn：前句已用性能表证明差异，此句用机制图解释差异来源。

- changes_argument_state_cn：从“更差”升级为“为什么更差以及我们的机制如何应对”。

- sets_up_next_cn：下一句讨论Shopper在Drugs场景中的失败原因。

- failure_if_removed_cn：删除后，实验2只有数字没有机制证据。

- evidence_pointer：Section 5.3.2 P2, Figure 5

### 13. Experiment 2 result 5.3.2 P3-S1-S5

- order：13

- locator：Experiment 2 result 5.3.2 P3-S1-S5

- paraphrase_cn：Shopper在Drugs中未能有效识别正关系，因为药物购买具有被动性和单一性（85.64%交易只包含一件商品），这阻碍了依赖购物篮推断互补的Shopper；我们推测这是情境特定缺陷，不是Shopper本身固有的，但它在Drugs中的失败和Grocery中的不可行仍显示我们方法在泛化性上更强，因为我们利用聚合销售而非细粒度购物篮。

- move_code：COMPETITOR_FAILURE_EXPLANATION

- statement_status：author_inference

- why_here_cn：在承认Shopper作为强基准的同时，解释其失败情境，避免让读者认为只是benchmark太弱，同时突出本文数据依赖更宽松。

- inherits_from_previous_cn：前文提到Shopper-GAT在Drugs最优但在Grocery不可行，此句给出深层原因。

- changes_argument_state_cn：把技术劣势转化为“数据需求差异”的论述。

- sets_up_next_cn：下一句用t-SNE可视化对比Shopper与CL4RSF表征，进一步验证跨品类能力。

- failure_if_removed_cn：删除后，Shopper在Drugs/ Grocery上的表现差异会显得像偶然。

- evidence_pointer：Section 5.3.2 P3, Figure I.1

### 14. Experiment 2 result 5.3.2 P4-S1-S3

- order：14

- locator：Experiment 2 result 5.3.2 P4-S1-S3

- paraphrase_cn：我们再用t-SNE可视化Shopper和CL4RSF的潜在产品表征：Shopper表征中同品类产品较接近（与Ruiz等一致），而CL4RSF表征打破品类边界，展现捕捉跨品类关系的能力。

- move_code：MECHANISM_VISUALIZATION_T_SNE

- statement_status：empirical_result

- why_here_cn：用表征分布直接显示CL4RSF学习到的产品空间不是按品类聚集，为跨品类关系主张提供可视化证据。

- inherits_from_previous_cn：前句已指出Shopper依赖品类语义，此句通过表征分布形成直观对比。

- changes_argument_state_cn：把性能差异延伸为表征语义差异。

- sets_up_next_cn：下一句讨论相关图策略的噪声问题和CGSL的对比，完成实验2收尾。

- failure_if_removed_cn：删除后，CL4RSF“跨品类”能力缺少直接视觉证据。

- evidence_pointer：Section 5.3.2 P4, Figure 6

### 15. Experiment 2 result 5.3.2 P5-S1-S3

- order：15

- locator：Experiment 2 result 5.3.2 P5-S1-S3

- paraphrase_cn：相关图策略易受噪声影响，尤其在长期预测中性能差且标准差高，说明存在一些不会持续的巧合瞬时相关；无两个损失的CGSL也比DC-PRL标准差更高、性能更差，验证两个损失项在增强GSL稳健性和有效性方面的效用。

- move_code：COMPONENT_RESULT_CGSL

- statement_status：empirical_result

- why_here_cn：完成实验2归因链：相关性策略受瞬时相关干扰，CGSL缺两个损失而劣化，DC-PRL因损失设计而稳健。

- inherits_from_previous_cn：前文已比较各种PRI，此句集中解释相关图和CGSL两个最关键对照。

- changes_argument_state_cn：把实验2的性能结果与引言P5中两个损失的设计动机精确对应。

- sets_up_next_cn：实验3将转向正负关系利用的消融。

- failure_if_removed_cn：删除后，两个损失的独立价值在实验2中无端不到证据。

- evidence_pointer：Section 5.3.2 P5

### 16. Experiment 3 result 5.3.3 P1-S1-S3

- order：16

- locator：Experiment 3 result 5.3.3 P1-S1-S3

- paraphrase_cn：表格6显示去掉正关系或负关系都会导致性能下降，验证同时利用正负关系的效用；对心血管类疾病，正关系可能来自联合用药、负关系可能来自谨慎换药；对呼吸类疾病，正关系可能来自联合用药或对外部环境的相似反应、负关系可能来自替代效应或环境变化；比较两类消融还显示心血管中正关系影响更大，呼吸中正负同等重要。

- move_code：COMPONENT_RESULT_POS_NEG

- statement_status：empirical_result

- why_here_cn：用消融结果证明DRAI正负关系同时利用的必要性，并提供疾病用药领域解释，展示结果不只是数字。

- inherits_from_previous_cn：承接实验3的设计和表格6。

- changes_argument_state_cn：建立“正负关系各自有价值”的实证主张，并给出领域机制解释。

- sets_up_next_cn：实验4转向异步关系消融，继续时间维度验证。

- failure_if_removed_cn：删除后，DRAI“频谱映射正负/高频低频”的核心设计失去消融证据。

- evidence_pointer：Section 5.3.3, Table 6

### 17. Experiment 4 result 5.3.4 P1-S1-S2

- order：17

- locator：Experiment 4 result 5.3.4 P1-S1-S2

- paraphrase_cn：表格7显示去除异步关系导致性能下降，尤其在长预测视界上更明显，突显利用异步关系的效用。

- move_code：COMPONENT_RESULT_ASYN

- statement_status：empirical_result

- why_here_cn：报告异步关系消融结果，并与实验1中“优势随h增大”的解释呼应。

- inherits_from_previous_cn：依据表格7，直接承接实验4定义。

- changes_argument_state_cn：验证SATE/DC-PRL异步通道的独立价值，并解释长视界优势来源。

- sets_up_next_cn：5.4解释性分析将展示异步关系的具体表现，完成从“性能”到“存在”的阶梯。

- failure_if_removed_cn：删除后，异步模块的存在缺乏独立验证。

- evidence_pointer：Section 5.3.4, Table 7

### 18. Explanatory analyses 5.4.1 P1-S1-S3

- order：18

- locator：Explanatory analyses 5.4.1 P1-S1-S3

- paraphrase_cn：在线附录I.2显示两个数据集中确实存在跨品类效应，印证CCCDT指导的合理性；在Drugs数据上，单品类实验的最佳Topk为5，而两品类整体实验的最佳Topk为7，说明需要更多跨品类邻居，为跨品类效应提供了补充且有力的证据。

- move_code：MECHANISM_INSIGHT_CROSS_CATEGORY

- statement_status：empirical_result

- why_here_cn：用Topk变化这一合理却间接的证据说明跨品类邻居价值，回扣数据集设计动机（呼吸/心血管看似无关但相关）。

- inherits_from_previous_cn：前一小节实验3中已在每个品类内做了消融，此处利用其Topk设置。

- changes_argument_state_cn：把跨品类关系从理论猜想升级为可观察经验规律。

- sets_up_next_cn：下一小节继续展示正负/异步/动态关系的推断可视化。

- failure_if_removed_cn：删除后，CCCDT“跨品类效应”在实证中缺少直接支持。

- evidence_pointer：Section 5.4.1, Figure I.2

### 19. Explanatory analyses 5.4.2 P1-S1-S2

- order：19

- locator：Explanatory analyses 5.4.2 P1-S1-S2

- paraphrase_cn：我们的方法不仅能提升RSF性能，还能提供产品关系洞察；进一步解释性分析包括学习到的关系图、正负注意力分数、动态注意力分数和时间注意力分数（在线附录I.3-I.6），结果表明正、负、异步、动态产品关系确实存在，且我们的方法能同时自适应地纳入这些复杂关系。

- move_code：MECHANISM_INSIGHT_RELATIONS

- statement_status：empirical_result

- why_here_cn：总结解释性分析的证据范围，把模型内部注意力转化为业务可解释的关系信号。

- inherits_from_previous_cn：5.4.1已处理跨品类效应，此句扩大到全部六种关系。

- changes_argument_state_cn：从“模型预测准”上升为“模型学到有意义的关系结构”。

- sets_up_next_cn：为贡献部分宣称六种关系建模和关系洞察提供实证基础。

- failure_if_removed_cn：删除后，贡献部分“解释性分析揭示各种推断关系”的声称失去依据。

- evidence_pointer：Section 5.4.2, Online Appendix I.3-I.6

## 讨论与贡献逐句图谱

### 1. Contributions 6.1 P1 S1-S2

- order：1

- locator：Contributions 6.1 P1 S1-S2

- paraphrase_cn：本研究做出多重贡献；第一，在协作RSF中，我们在互补/替代之外沿类型和时间维度辨别了六种产品关系，拓宽了可被用于增强销售预测的产品关系视野。

- move_code：CONTRIBUTION_1_TAXONOMY

- statement_status：contribution_claim

- why_here_cn：贡献部分第一项把前文的理论分解上升为领域知识贡献，点名“超越互补/替代”这一标题承诺。

- inherits_from_previous_cn：综合全文理论部分的关系分类和解释性分析证据。

- changes_argument_state_cn：开始把局部设计结果汇总为学科贡献。

- sets_up_next_cn：第二项贡献转向设计科学与制品层面。

- failure_if_removed_cn：删除后，论文标题和摘要中的“Beyond complements and substitutes”失去兑现。

- evidence_pointer：Section 6.1 P1

### 2. Contributions 6.1 P2 S1-S5

- order：2

- locator：Contributions 6.1 P2 S1-S5

- paraphrase_cn：第二，对IS计算设计科学范式，我们贡献一个新型设计制品和两个可泛化设计原则：制品是编码多面产品关系的GNN方法，可适配其他业务问题；设计原则一是“从管道到联合优化”（避免先定关系再预测的误差传播），二是“旋转与编织”（用current_和previous_双节点建模异步关系，为每个SKU产生双表征）。

- move_code：CONTRIBUTION_2_DESIGN_PRINCIPLES

- statement_status：contribution_claim

- why_here_cn：把MS2RSF/CL4RSF从单个预测模型提升为可迁移的设计知识，是设计科学论文贡献升级的关键段。

- inherits_from_previous_cn：前项贡献是理论分类，此项贡献是制品和抽象原则。

- changes_argument_state_cn：使论文贡献不依赖于一次性benchmark结果，而成为可复制设计知识。

- sets_up_next_cn：第三项贡献聚焦方法论创新。

- failure_if_removed_cn：删除后，论文作为设计科学研究的定位被削弱，贡献可能退化为“一个更好的预测模型”。

- evidence_pointer：Section 6.1 P2

### 3. Contributions 6.1 P3 S1-S3

- order：3

- locator：Contributions 6.1 P3 S1-S3

- paraphrase_cn：第三，异步感知GNN（双通道异步GSL和异步感知时序编码器）、带两个新损失项的稳健有效GSL、以及DRAI构成方法论贡献；DRAI尤其是用低/高频信号建模正负关系的新视角，相比用不同边类型和平衡路径策略（如SGCN）提供了新的建模思路，可为其他模型提供灵感。

- move_code：CONTRIBUTION_3_METHOD

- statement_status：contribution_claim

- why_here_cn：把三个模块和两个损失的具体技术选择包装成可复用的方法论贡献，并用表8给出跨领域应用前景。

- inherits_from_previous_cn：前两项贡献已给出领域和设计层贡献，此项补上更低层的技术/方法层贡献。

- changes_argument_state_cn：完成三层贡献架构：领域—设计—方法。

- sets_up_next_cn：下一段转向管理启示，说明预测性能和产品关系洞察的实际用途。

- failure_if_removed_cn：删除后，方法部分的大量技术新颖性没有被“贡献”化。

- evidence_pointer：Section 6.1 P3, Table 8

### 4. Managerial Implications 6.2 P1 S1-S3

- order：4

- locator：Managerial Implications 6.2 P1 S1-S3

- paraphrase_cn：端到端架构因纳入多种产品关系而优于先进替代方法，对零售店经理、库存、采购、运营、营销和平台等多类利益相关者有两方面价值：一是改进预测为供应链、资源规划、库存控制和采购计划提供更坚实的数据支持，降低成本并增加利润；二是产品关系洞察可促进合理定价和促销、提升推荐相关性和多样性、改善品类规划、交叉销售和货架空间分配。

- move_code：MANAGERIAL_IMPLICATIONS_OPEN

- statement_status：contribution_claim

- why_here_cn：把技术贡献翻译成管理语言，分“预测改进”和“关系洞察”两条路径，让IS读者看到实践价值。

- inherits_from_previous_cn：承接前三项贡献的经验结果和关系可视化。

- changes_argument_state_cn：从“我们有什么贡献”转向“这些贡献对管理者意味着什么”。

- sets_up_next_cn：下一段预告经济价值分析和两个下游应用（推荐、品类规划）。

- failure_if_removed_cn：删除后，论文对实践读者的相关性会显著降低。

- evidence_pointer：Section 6.2 P1

### 5. Economic Value Analysis 6.2.1 P1-S1-S6

- order：5

- locator：Economic Value Analysis 6.2.1 P1-S1-S6

- paraphrase_cn：参照Sun等的增量价值估计，我们在Drugs案例按样本粒度估计经济价值；区分两种预测误差：预测低于实际导致机会成本（损失利润），预测高于实际导致仓储物流成本；据此给出每个样本的误差成本公式和单位仓储物流成本u的估算公式。

- move_code：ECONOMIC_VALUE_METHOD

- statement_status：method_decision

- why_here_cn：为把MAE/RMSE优势转成经济收益，先给出成本模型，让随后的大额数字有透明计算基础。

- inherits_from_previous_cn：承接管理启示中“降低成本”的说法，并给出具体可计算定义。

- changes_argument_state_cn：把预测误差转化为货币度量。

- sets_up_next_cn：下一段报告∆Value在不同场景下相对各基准的成本减少。

- failure_if_removed_cn：删除后，表9中的金额缺乏计算方法。

- evidence_pointer：Section 6.2.1, 公式17-18

### 6. Economic Value Analysis 6.2.1 P2-S1-S4

- order：6

- locator：Economic Value Analysis 6.2.1 P2-S1-S4

- paraphrase_cn：表9显示在四个场景中我们的模型相对各基准产生显著成本减少：从测试集逐步外推到一年、所有SKU、全国连锁店，忽略不同时间/SKU/店铺/城市的异质性；例如相对最佳基准Shopper-GAT，估计节省超过2.5亿元。

- move_code：ECONOMIC_VALUE_RESULT

- statement_status：empirical_result

- why_here_cn：用具体金额让性能优势变得直观可感，但当报告大数字时也交代了外推假设。

- inherits_from_previous_cn：前句已定义成本，此句计算并展示结果。

- changes_argument_state_cn：把预测改进转化成管理收益主张。

- sets_up_next_cn：下一小节转向下游应用CSPR推荐，展示关系洞察的第2个用途。

- failure_if_removed_cn：删除后，管理启示中的“经济价值”没有实证支撑。

- evidence_pointer：Section 6.2.1, Table 9

### 7. Downstream Application 6.2.2 P1-S1-S4

- order：7

- locator：Downstream Application 6.2.2 P1-S1-S4

- paraphrase_cn：对有效的互补替代推荐（CSPR），高质量产品关系信息很关键；已有研究用文本/图像特征推断互补替代品，但容易遗漏相关产品（如网球拍与运动上衣无文本图像相似性）；近年用户行为数据策略被广泛采用，但共购/共视并不准确反映互补/替代，且通常牺牲跨品类推荐多样性。

- move_code：DOWNSTREAM_GAP

- statement_status：prior_literature

- why_here_cn：在CSPR应用中先批评现有特征法和用户行为法，为CL4RSF产品关系进入推荐场景铺垫需求。

- inherits_from_previous_cn：承接管理启示中“提升推荐相关性和多样性”的说法。

- changes_argument_state_cn：建立下游推荐场景中的缺口。

- sets_up_next_cn：下一段说明CL4RSF推导的关系如何在相关性、适时性、多样性三方面改善CSPR。

- failure_if_removed_cn：删除后，CSPR讨论没有问题靶子。

- evidence_pointer：Section 6.2.2 P1

### 8. Downstream Application 6.2.2 P2-S1-S6

- order：8

- locator：Downstream Application 6.2.2 P2-S1-S6

- paraphrase_cn：CL4RSF推导的产品关系为CSPR提供相关、及时、多样的推荐基础：相关性上，推荐正相关产品、排除负相关产品，如小米手机与小米耳机为正关系、与另一品牌手机为负关系，可在购买手机后推荐耳机并排除竞品；适时性上，额外区分同步/异步关系，利用异步关系和时间注意力决定“何时推荐”，如购买小米手机后过一段时间推荐小米扫地机器人；多样性上，跨品类关系可推荐网球拍之后推荐网球、运动上衣、运动水壶等跨品类正相关产品。

- move_code：DOWNSTREAM_APPLICATION_EXPAN

- statement_status：author_inference

- why_here_cn：用三个具体推荐场景说明CL4RSF关系输出的下游价值，是“预测性能之外的管理意义”最具体的展开。

- inherits_from_previous_cn：前段已建立CSPR缺口，此段用推导关系回应。

- changes_argument_state_cn：把关系建模能力桥接到推荐任务，但未实际运行推荐系统实验，停留在潜在价值论证。

- sets_up_next_cn：下一段总结并给出图7玩具示例。

- failure_if_removed_cn：删除后，推荐应用中的相关性/适时性/多样性三个主张无内容。

- evidence_pointer：Section 6.2.2 P2, Figure 7

### 9. Downstream Application 6.2.2 P3-S1-S2

- order：9

- locator：Downstream Application 6.2.2 P3-S1-S2

- paraphrase_cn：总之，相比常见的品类特定用户行为数据策略，CL4RSF赋能的CSPR模型有望提升推荐相关性、及时性和多样性；图7给出用于说明的玩具示例，因为真实场景更复杂，例如在早期浏览阶段替代品也可作为候选以提供更多选择。

- move_code：DOWNSTREAM_SUMMARY

- statement_status：author_inference

- why_here_cn：用三点式总结强化CSPR主张，并把示例明确标示为“illustration”，避免过度声称。

- inherits_from_previous_cn：直接综合P2的三个推荐场景。

- changes_argument_state_cn：把推荐应用主张正式归入管理贡献，但承认只是潜在价值。

- sets_up_next_cn：最后进入局限性部分。

- failure_if_removed_cn：删除后，6.2.2的推荐论述缺少收束。

- evidence_pointer：Section 6.2.2 P3

### 10. Limitations 7 P1-S1-S3

- order：10

- locator：Limitations 7 P1-S1-S3

- paraphrase_cn：本研究有三项局限：DC-PRL只处理现有产品，未来可研究支持新产品的动态图GSL和GNN；当前使用固定kNN邻居数，可探索更灵活图结构学习；虽然实验、经济价值分析和下游应用讨论支持操作效用，但真实世界价值仍需现场实验进一步检验。

- move_code：LIMITATION_AND_FUTURE

- statement_status：author_inference

- why_here_cn：诚实划定边界，把冷启动、灵活图、现场验证三个未解决问题留给未来研究，也保护论文不过度声称。

- inherits_from_previous_cn：全文方法和证据的边界条件在此被明确。

- changes_argument_state_cn：从贡献主张转向边界声明，使论文在承认局限中结束。

- sets_up_next_cn：无后续内容；是全文收束。

- failure_if_removed_cn：删除后，论文缺少设计科学常见的谦逊边界，可能被审稿人视为过度泛化。

- evidence_pointer：Section 7

## Study累积逻辑

### 1. 1

- study_or_phase：研究阶段1：理论驱动的需求分析与设计（Section 3）

- evidence_job_cn：从CCCDT推导出产品关系分类体系和三个元需求，并在表1建立理论依据→需求→方案→新颖性的映射。

- what_it_establishes_cn：建立“哪些关系应该被识别和利用”的概念框架，以及每个设计决策的合法性来源。

- what_it_cannot_establish_cn：不能证明这些关系在实际销售数据中真实存在，也不能证明计算模型能识别和利用它们。

- why_next_phase_is_needed_cn：理论需求必须被具体化为可执行的模型，否则只是分类学而非设计科学。

- transition_wording_function_cn：“The theoretical rationales and requirements (Table 1) motivate us to design a GNN-based deep-learning method (i.e., CL4RSF)”把需求转为模型设计入口。

### 2. 2

- study_or_phase：研究阶段2：方法构建（Section 4）

- evidence_job_cn：将三个元需求转化为SATE、DC-PRL、DRAI三个模块和MS2RSF端到端架构，并为每个模块给出设计理由与公式。

- what_it_establishes_cn：建立一个可复现、可运行的计算制品，说明每个模块如何服务特定需求。

- what_it_cannot_establish_cn：不能证明这些模块比替代方案更好，也不能证明它们单独贡献了预测增益。

- why_next_phase_is_needed_cn：设计科学必须评价，不能只停留在“我们构建了什么”。

- transition_wording_function_cn：“To evaluate the effectiveness of our designed method, we have conducted a series of experiments...”从方法转入评价。

### 3. 3

- study_or_phase：研究阶段3：数据准备（Section 5.1）

- evidence_job_cn：构造两个互补的真实零售数据集，分别突出“跨品类微妙关系”（Drugs）和“一般多品类单店场景”（Grocery），并保证时序划分公平。

- what_it_establishes_cn：建立可检验模型的外部效度基础，并展示数据构造本身的服务目标。

- what_it_cannot_establish_cn：不能证明模型在这些数据上会赢。

- why_next_phase_is_needed_cn：需要实际运行模型与基准比较。

- transition_wording_function_cn：“We conducted four main experiments...”用实验路线图开启结果部分。

### 4. 4

- study_or_phase：研究阶段4：实验1整体基准比较

- evidence_job_cn：证明端到端MS2RSF在两个数据集、所有视界和两个指标上全面优于10个基准。

- what_it_establishes_cn：建立整体性能优越性，显示复杂关系建模对RSF有实际增益。

- what_it_cannot_establish_cn：不能说明哪个组件或哪类关系贡献最大，也不能排除是整体架构而非特定设计带来的优势。

- why_next_phase_is_needed_cn：需要组件级实验分离效应，否则“为什么赢”仍是黑箱。

- transition_wording_function_cn：“In Experiments 2–4, we examined the utility of key designed components...”从整体转向组件归因。

### 5. 5

- study_or_phase：研究阶段5：实验2关系识别策略替换

- evidence_job_cn：固定其他模块，仅替换PRI策略，检验DC-PRL及其两个损失相对于Category/Copurchase/Shopper/Correlation/CGSL的价值。

- what_it_establishes_cn：证明关系识别模块和两个损失项对性能的必要性，并给出注意力分数/t-SNE作为机制证据。

- what_it_cannot_establish_cn：不能证明DC-PRL在所有零售品类上都优于这些策略，也没有关系ground-truth标签来验证识别准确率。

- why_next_phase_is_needed_cn：识别出关系还不足够，需要检验“利用正负关系”是否有独立价值。

- transition_wording_function_cn：“Experiment 3 assessed the utility of leveraging positive and negative product relations through ablation analyses.”从识别转入利用。

### 6. 6

- study_or_phase：研究阶段6：实验3正负关系消融

- evidence_job_cn：通过w/o positive和w/o negative两个变体，证明DRAI同时利用正负关系的必要性，并在心血管/呼吸两个品类内提供领域解释。

- what_it_establishes_cn：建立“正关系和负关系各自有增量价值”的消融证据，并展示不同疾病场景的差异模式。

- what_it_cannot_establish_cn：不能精确量化这些关系在真实世界中的因果效应，也没有验证模型推断的正负标签是否准确。

- why_next_phase_is_needed_cn：类型维度之外还需验证时间维度（异步）的贡献。

- transition_wording_function_cn：“In Experiment 4, we examined the utility of leveraging asynchronous relations...”从类型维度转向时间维度。

### 7. 7

- study_or_phase：研究阶段7：实验4异步关系消融

- evidence_job_cn：比较有异步与无异步变体，证明异步关系利用的价值，尤其在长预测视界上。

- what_it_establishes_cn：建立异步模块的独立贡献，并解释主实验中长视界优势的来源。

- what_it_cannot_establish_cn：不能证明异步关系来自品牌溢出或消费者学习等具体机制，也不能排除是短期波动相关。

- why_next_phase_is_needed_cn：组件实验只证明“有效”，还需解释性分析说明模型学到了什么有意义的结构。

- transition_wording_function_cn：“Moreover, explanatory analyses...”从性能组件验证转向机制/意义分析。

### 8. 8

- study_or_phase：研究阶段8：解释性分析与经济价值分析

- evidence_job_cn：用跨品类Topk证据、关系图、注意力分数、t-SNE和经济成本估算，将性能提升转化为可观察的关系结构和货币价值。

- what_it_establishes_cn：建立“跨品类效应存在、正负/异步/动态关系可被推断、预测改进有经济价值”三类辅助证据。

- what_it_cannot_establish_cn：不能证明推荐或品类规划等下游任务上的端到端效果，也不能保证经济价值外推的准确性。

- why_next_phase_is_needed_cn：没有下一阶段；这些分析为讨论部分将局部结果升级为贡献提供了最后一块证据。

- transition_wording_function_cn：“This study makes multiple contributions...”把经验结果汇总为贡献主张。

## 主张—证据台账

### 1. MS2RSF的预测性能在两个数据集、所有视界和MAE/RMSE上优于所有基准

- claim_cn：MS2RSF的预测性能在两个数据集、所有视界和MAE/RMSE上优于所有基准

- claim_level：technical

- supporting_evidence_cn：表格2-3：MS2RSF在两个数据集四个视界上均为最优，且10次重复标准差较小；DM检验在附录H中保证显著性。

- support_strength：direct

- where_claim_is_made：Section 5.3.1 P1

- where_evidence_is_provided：Tables 2-3; Section 5.2; Online Appendix H

### 2. DC-PRL及其两个损失项相比现有关系识别策略能更稳健有效地识别相关产品

- claim_cn：DC-PRL及其两个损失项相比现有关系识别策略能更稳健有效地识别相关产品

- claim_level：artifact

- supporting_evidence_cn：表格4-5中DC-PRL优于Category/Copurchase/Shopper/Correlation/CGSL，且CGSL去掉两个损失后劣化；图5注意力分数显示替代策略引入噪声。

- support_strength：direct

- where_claim_is_made：Section 5.3.2 P1和P5

- where_evidence_is_provided：Tables 4-5; Figure 5; Section 5.3.2

### 3. 同时利用正关系和负关系对预测有增益

- claim_cn：同时利用正关系和负关系对预测有增益

- claim_level：mechanism

- supporting_evidence_cn：表6：w/o positive和w/o negative均比完整模型差，且在心血管/呼吸品类中模式不同。

- support_strength：direct

- where_claim_is_made：Section 5.3.3 P1

- where_evidence_is_provided：Table 6; Section 5.3.3

### 4. 利用异步关系能提升预测性能，尤其在长视界

- claim_cn：利用异步关系能提升预测性能，尤其在长视界

- claim_level：mechanism

- supporting_evidence_cn：表7：w/o asyn在h=1到12均劣于with asyn，长视界差距更明显。

- support_strength：direct

- where_claim_is_made：Section 5.3.4 P1

- where_evidence_is_provided：Table 7; Section 5.3.4

### 5. 存在跨品类效应，需要更多跨品类邻居

- claim_cn：存在跨品类效应，需要更多跨品类邻居

- claim_level：boundary

- supporting_evidence_cn：Drugs中单品类最佳Topk为5而两品类整体为7；在线附录I.2的相关矩阵与示例。

- support_strength：direct

- where_claim_is_made：Section 5.4.1 P1

- where_evidence_is_provided：Section 5.4.1; Figure I.2

### 6. 模型能推断正、负、异步、动态产品关系，并同时自适应利用

- claim_cn：模型能推断正、负、异步、动态产品关系，并同时自适应利用

- claim_level：mechanism

- supporting_evidence_cn：在线附录I.3-I.6的关系图、注意力分数、动态注意力、时间注意力可视化。

- support_strength：partial

- where_claim_is_made：Section 5.4.2 P1

- where_evidence_is_provided：Online Appendix I.3-I.6; Section 5.4.2

### 7. 模型推导的产品关系可用于改善CSPR推荐的相关性、适时性和多样性

- claim_cn：模型推导的产品关系可用于改善CSPR推荐的相关性、适时性和多样性

- claim_level：design_knowledge

- supporting_evidence_cn：概念性讨论和玩具示例（图7），引用了RSF结果作为“关系质量更高”的间接证据，但没有在真实推荐系统上运行端到端评测。

- support_strength：asserted

- where_claim_is_made：Section 6.2.2 P2-P3

- where_evidence_is_provided：Section 6.2.2; Figure 7; 间接证据为Tables 4-5的关系识别结果

### 8. 模型相对基准可节省大量经济成本（最高超2.5亿元人民币）

- claim_cn：模型相对基准可节省大量经济成本（最高超2.5亿元人民币）

- claim_level：boundary

- supporting_evidence_cn：表9基于误差成本公式和四个场景外推，但依赖统一单位成本、忽略时间/SKU/店铺/城市异质性，没有现场实验验证。

- support_strength：partial

- where_claim_is_made：Section 6.2.1 P2

- where_evidence_is_provided：Table 9; Section 6.2.1 公式17-18

## ISR定位逻辑

- constitutive_is_problem_cn：本文把“产品关系”从经济学/营销学中的互补替代静态标签，重构为数字零售场景中由消费者偏好、外部事件和时间动态共同构成的多面现象，并把它嵌入协作RSF这一IS关注的预测决策任务。文章不是单纯在技术上优化预测，而是以CCCDT解释“为什么产品关系是多面且可计算的”，因此问题本身带有消费理论、零售运营和信息系统设计的交叉构成性。

- technology_behavior_or_market_entanglement_cn：技术制品（CL4RSF/MS2RSF）不是对现有产品关系的值化工具，而是与消费者行为和市场动态互相构成：正/负关系来自捆绑和跨品类考虑，异步关系来自跨品类学习和品牌溢出，动态关系来自市场环境变化；模型则以销售序列为监督来外化这些行为驱动的内在关系。通过把消费者理论变成图学习目标（同步/异步双通道、频谱映射、注意力动态），技术设计与行为机制紧紧缠绕在一起。

- role_of_benchmark_or_objective_evidence_cn：基准比较和消融实验不只是证明“我们分数更高”，而是用来支持“现有关系识别方法会引入噪声/遗漏信息/无法同时容纳负关系和异步关系”这一IS层面的知识主张；基准按关系来源和关系类型编码，使每个性能差距都能被回指到某个设计决策（如DC-PRL vs. 相关图、DRAI vs. SGCN）。经济价值分析则把分数优势转成管理者可理解的成本减少。

- theory_in_design_cn：CCCDT确实进入了设计前端：它决定了本文辨别哪些关系（正负、间接、非对称、异步、动态）、确定三个元需求，并直接影响DC-PRL的异步图/虚拟节点、SATE的注意力融合、DRAI的正负频谱映射与动态tanh注意力。但对低层技术选择（GRU、KL散度、InfoNCE、MagNet、FAGCN）的约束较弱，更多来自机器学习领域需求；理论到设计属于“问题与模块层面的强耦合、低层技术选择的弱耦合”。

- technical_vs_is_contribution_balance_cn：技术贡献篇幅很大（方法公式、图结构学习、对比损失、磁拉普拉斯、端到端架构），但IS贡献被明确分成三层：领域关系分类学、设计科学与设计原则、方法论创新。作者用了表1把每个技术细节链接到理论和需求，并在贡献部分把技术细节抽象为“从管道到联合优化”“旋转与编织”等可迁移原则，避免论文退化为纯算法报告。

- beyond_transient_performance_cn：论文通过四条路径超越暂时性能优势：一是性能优势被归因于理论关系维度（正负、异步、动态）而非偶然调参；二是通过实验2-4逐一证明每个设计组件有独立价值；三是通过解释性分析把注意力/关系图与业务语义连接，说明模型学到的是可解释产品关系；四是通过两个设计原则使技术方案可迁移到其他领域（表8），并讨论CSPR、品类规划等下游应用，使贡献不止于当下数据集的分数。

## 段落级仿写模板

### abstract_steps

1. 第一句：用一句学科动向或宏观背景打开摘要，点明核心概念域（如关系赋能零售管理）。

2. 第二句：收窄到本研究的具体任务，同时陈述现有研究在识别和利用两个层面的缺口。

3. 第三句：引入一个能重新组织问题现象的理论，给出新的分类轴线，并用括号概括每条轴线下的属性。

4. 第四至五句：把理论分类转成两个或三个研究问题，然后命名制品，并说明制品如何回应这些问题；必要时补充一个适配应用场景的端到端架构。

5. 第六句：报告实证结果，必须具体说明数据场景和结果类型（整体优于基准+组件验证）。

6. 第七句：用解释性洞见收尾，给读者留下“不只性能好，还有机制/意义”的印象。

### introduction_paragraph_steps

1. P1段：以该领域最常见的若干关系实例建立背景，然后把镜头推到本文应用任务，并点明该任务的管理决策价值。

2. P2段：把领域内既有基线分类（如互补/替代）定义清楚，包括其经济学定义和符号化表达。

3. P3段：用“然而”挑战基线分类，给出正反两个真实场景例子，区分“实质关系”与“偶然相似”并引出识别标准。

4. P4段：对现有识别方法做分组批评，一组批评引入噪声（用文献数字），一组批评遗漏信息（用属性不可穷尽），然后提出RQ1。

5. P5段：直接用“为回应RQ1”给出第一层设计答案，并说明该设计如何避免被批评的缺陷；再把设计偏好具体化为可计算损失/模块。

6. P6段：用“识别之后，另一个问题是如何利用”转向第二阶段；引入核心理论，系统展开其构念并形成RQ2。

7. P7段：针对RQ2选择技术范式，指出现有技术不足以处理新需求，预告定制模块的职责。

8. P8段：整个研究收束：命名制品、端到端系统，给出实证结果和解释性洞见，建立贡献框架。

### theory_to_design_steps

1. 先给“为什么用理论指导设计”的方法论依据，引用设计科学文献说明理论抽象对论文长期价值的必要性。

2. 用一段话给出“理论→需求→制品”的整体推导链，并提供一张示意图（如Figure 1）作为导航。

3. 逐段展开理论的每个构念，每段对应一个维度（如类型维度、时间维度），并用具体例子让概念可感。

4. 在需求推导后，用“这些需求带来方法论挑战”过渡，说明为什么不能直接套用现有方法。

5. 对每个元需求（Req1、Req2-1、Req2-2）分别给出解决方案，并解释该方案如何克服具体挑战。

6. 建立一张表格，横向映射“理论依据→需求→解决方案→新颖性→模块”，作为全文设计与实验的最重要索引。

### method_and_study_sequence_steps

1. 方法部分开头先给整体架构总览和视觉图，说明模块间数据流和联合训练方式。

2. 每个模块小节按“需求→设计决策→为什么这样做→公式/算法→为后续实验埋下可检验预期”的顺序展开。

3. 两个损失等创新点要用一小节单独介绍，说明其目标、数学形式和对一般方法的零售域适配。

4. 端到端架构单独作为一节，把前面的模型封装进实际可预测应用系统。

5. 实验部分先说明两个数据集如何构造并互补，强调数据选择服务于研究假设（如跨品类微妙关系）。

6. 在实验开始前给出“四个实验各回答什么问题”的路线图。

7. 结果部分按“整体基准比较→组件替换→类型消融→时间消融→解释性分析”的顺序递进，每个结果都先给结论句再给证据表。

### results_reporting_steps

1. 每个实验小节第一句用粗体结论式陈述，直接回答该实验要检验的问题。

2. 先报告表格数字，再在下一句解释数字差异来自哪个设计决策（如“类别/共购策略引入噪声”“CGSL缺两个损失”）。

3. 对关键基准的失败给出情境化解释（如Shopper在药物购买场景失效），避免把差距归为benchmark太弱，同时突出本文数据需求更低。

4. 用注意力分布、t-SNE等可视化把性能结果转为机制证据。

5. 消融结果用“去掉X性能下降”作为直接证据，并辅以领域解释（如心血管/呼吸的用药行为）使数字有业务意义。

6. 解释性分析作为独立小节，用Topk变化、关系图、注意力时间变化等把“模型学到了什么”可视化，为贡献部分铺垫。

### discussion_and_contribution_steps

1. 贡献部分分三层：领域概念贡献（新的分类/关系类型）、设计科学贡献（制品+可泛化设计原则）、方法贡献（具体组件和技术路径）。

2. 每个贡献主张都要回指一个前文已经验证的证据类型，不能新瓶装旧酒或凭空宣称。

3. 设计原则用简短命名式概括（如“从管道到联合优化”“旋转与编织”），并用实验中的对比结果作为原则依据。

4. 管理启示分两条路径：预测改进支持供应链/库存决策，关系洞察支持定价/推荐/品类规划。

5. 经济价值分析需要先给出透明的成本模型和外推假设，再报告金额，避免数字被质疑。

6. 下游应用讨论要明确区分“潜在价值”和“已验证”，用illustration示例引导但不过度声称。

7. 最后用三点式局限收尾，每个局限对应一条未来研究。

## 可执行写作算法

### 1. 1

- step：1

- rhetorical_job_cn：建立宏观背景并收窄到核心研究对象（协作RSF），说明其管理价值。

- research_evidence_required_cn：至少掌握若干与“关系”相关的零售/IS/OM文献或现象，能支撑“关系普遍且重要”。

- sentence_pattern_function_cn：先写“各类关系普遍存在且重要”，再写“本研究聚焦其中一个具体任务并指出其价值”，让读者知道焦点在哪里。

- transition_condition_cn：当读者已经清楚本文任务是“利用其他产品信息做RSF”时，可以进入传统分类定义。

### 2. 2

- step：2

- rhetorical_job_cn：精确定义将被挑战的传统分类，并给出正/负关系的基础标记。

- research_evidence_required_cn：经典经济学/营销文献对互补/替代及销售方向关系的定义。

- sentence_pattern_function_cn：先定义概念，再给经济学定义，然后说明概念在销售数据上的直观表现（正/负）。

- transition_condition_cn：当基线定义足够清晰后，用“然而”进入批判。

### 3. 3

- step：3

- rhetorical_job_cn：用正反现实例子论证二分法不足，并建立“固有/重复vs偶然/瞬时”的识别标准。

- research_evidence_required_cn：至少一个非固有但重复产生销售联动的例子，和一个偶然相似的例子。

- sentence_pattern_function_cn：先给否定判断，再用“例如……；另一方面，例如……”成对例子说明边界。

- transition_condition_cn：当读者认可“有些关系应该用、有些应该排除”后，可进入文献批判。

### 4. 4

- step：4

- rhetorical_job_cn：分组批评现有识别方法，指出噪声和遗漏两类缺陷，并正式提出RQ1。

- research_evidence_required_cn：针对类别/共视方法的不准确率数据，针对属性相似度方法的“属性不可穷尽”论证。

- sentence_pattern_function_cn：先用“既有努力要么……要么……”总起，再逐类批评，最后用“总之，因此我们提出RQ1”收束。

- transition_condition_cn：当RQ1形成后，下一段应直接给出设计答案。

### 5. 5

- step：5

- rhetorical_job_cn：给出RQ1的初步设计答案，并把设计偏好编码为可计算损失。

- research_evidence_required_cn：有数据驱动的监督信号（如销售）可以替代旧方法，两个损失的设计有清晰目标。

- sentence_pattern_function_cn：先写“为回应RQ1我们设计了X”，再说明X如何避免旧缺陷，然后用“具体地，损失A鼓励…损失B抑制…”继续。

- transition_condition_cn：当读者已看到识别解决方案后，用“识别之后另一个问题是……”转向利用。

### 6. 6

- step：6

- rhetorical_job_cn：引入核心理论，沿新维度展开丰富的关系类型，并正式提出RQ2。

- research_evidence_required_cn：一个能提供关系类型/时间维度分解的理论，且每个构念可以对应到具体计算需求。

- sentence_pattern_function_cn：先写“我们借鉴理论X并沿维度A和B分解”，再逐条解释每一类的含义与例子，最后用“因此……我们提出RQ2”收束。

- transition_condition_cn：当RQ2列出所需关系类型后，下一段应选择技术范式并预告定制模块。

### 7. 7

- step：7

- rhetorical_job_cn：选择技术范式，指出现有技术不足，预告定制模块的职责。

- research_evidence_required_cn：说明技术范式天然适合某种关系（如GNN适合间接关系），且现有方法在负/异步/同时性上的局限。

- sentence_pattern_function_cn：先写“鉴于需要建模X，我们采用Y范式”，再写“然而现有Y不能处理A和B，因此我们定制Y：模块1负责…，模块2负责…”

- transition_condition_cn：当三个模块被预告后，用“总体来看，这是计算设计研究”收束引言。

### 8. 8

- step：8

- rhetorical_job_cn：在方法部分把每个需求转为具体模块公式，并为每个设计决策给出“为什么不能直接套用现有方法”的理由。

- research_evidence_required_cn：算法公式、损失函数、图学习机制均已实现，且每个关键决策都能与某个理论需求对应。

- sentence_pattern_function_cn：每个模块按“需求→挑战→方案→公式→实现细节→预期可检验效果”顺序组织。

- transition_condition_cn：当全部模块和端到端架构定义完成，进入实验设计。

### 9. 9

- step：9

- rhetorical_job_cn：设计两个互补数据集和四个实验，每个实验对应一个具体需求或设计组件。

- research_evidence_required_cn：两个真实数据集能覆盖不同挑战（如跨品类微妙关系 vs 一般多品类），每个消融/替换只改变一个变量。

- sentence_pattern_function_cn：先写数据构造和选择理由，再写实验路线图，然后逐一说明基准/变体。

- transition_condition_cn：当实验设计清楚后，按“整体→组件→机制”顺序报告结果。

### 10. 10

- step：10

- rhetorical_job_cn：用解释性分析把性能结果转成关系洞察和业务含义，为贡献升级做铺垫。

- research_evidence_required_cn：有可视化（注意力、关系图、t-SNE）或合理的超参数变化证据（Topk）能显示模型学到了有意义结构。

- sentence_pattern_function_cn：先展示证据（如Topk变化、注意力分布），再给出业务解释和理论回扣。

- transition_condition_cn：当机制证据已呈现，可在讨论部分把结果升级为领域/设计/方法三层贡献。

### 11. 11

- step：11

- rhetorical_job_cn：把贡献分成三层，并以可泛化设计原则和透明外推的经济价值收束。

- research_evidence_required_cn：每一项贡献都必须有前文实证或概念证据对应，避免无根据升级。

- sentence_pattern_function_cn：先写“本研究贡献包括：领域层面…；设计层面…；方法层面…”，再写“管理启示分预测改进和关系洞察”，最后用局限收尾。

- transition_condition_cn：当三层贡献和局限都清晰后，全文论证闭环完成。

## 应模仿的高价值动作

1. 用理论（CCCDT）把模糊的“关系”拆成可计算的维度，并用表1把每个维度与需求、方案、新颖性逐一映射，形成设计科学论文的“理论—设计—实验”索引。

2. 在每个设计决策处直接说明“现有方法为什么做不到”，且把批评落到具体机制上（如GCN低通滤波会滤掉高频负关系、谱方法需要对称矩阵而零售关系非对称）。

3. 实验采用“整体基准+组件替换+正负消融+异步消融+解释性分析”三级证据结构，逐层回答“整体是否好、为什么好、哪个组件好、模型学到了什么”。

4. 基准比较不仅报数字，还按“关系来源”和“关系类型”给基准编码，使每个性能差距都能回指到某个具体设计选择。

5. 把广告级的可视化（注意力分数、t-SNE、Topk变化）用于机制解释，使黑箱模型学习到的关系变成可业务解释的证据。

6. 对强基准的失败给出情境化解释（如Shopper在药物购买被动场景失效），既保持学术礼貌，又突出本文数据需求的优势。

7. 经济价值分析先给出透明的成本公式和外推假设，再报金额，避免大数字显得不可信。

8. 设计原则用简短命名式概括（“从管道到联合优化”“旋转与编织”），并用表8给出跨领域迁移场景，防止贡献退化为一次性性能优势。

## 不要只复制的表面动作

1. 不要只堆叠GNN模块并宣称“多关系建模”，必须让每个模块与某个理论或业务关系维度明确对应，并有消融证据。

2. 不要仅凭性能提升宣称“识别了关系”，需要至少通过解释性分析展示关系语义（如注意力图、t-SNE）避免空泛。

3. 不要照搬“固定kNN邻居+离线数据集”作为泛化的默认选择；如果场景需要冷启动或动态目录，应先说明边界。

4. 不要复制Shopper-GAT在Grocery中的不可行处理；若使用购物篮依赖基准，必须保证数据可得。

5. 不要在没有现场实验的情况下，把经济价值外推数字当成实测收益；应明确标注情景外推和假设。

6. 不要把“理论指导设计”简化为引言中引用一个理论就结束；理论必须出现在需求定义、模块设计和贡献命名三个层面。

## 证据薄弱或跳跃的动作

1. CSPR推荐应用只在概念层面论述，用图7玩具示例说明“相关性、及时性、多样性”潜力，但没有真实推荐系统端到端评测；论文也承认只是“potential”，但读者需注意这一点。

2. 经济价值分析依赖统一单位成本、忽略各SKU/店铺/城市异质性，从28周外推到全年、全SKU、全国连锁；超过2.5亿元的金额是强假设下的估算。

3. 模型被说成能“识别”固有或重复关系，但没有外部ground-truth关系标签，实验只能证明“预测导向的隐式关系学习有效”，不能等同于关系发现任务上的有标签准确率。

4. 动态关系虽有tanh注意力机制和在线附录中的注意力可视化，但没有定量验证关系类型/强度变化的准确性，也没有对比ground-truth动态标签。

5. 在线附录I、E、G、H等大量证据仅在附录出现，主文依赖摘要描述；若审稿人或读者不查阅附录，部分稳健性主张的证据强度会被削弱。

6. 两个通用关键组件（SATE、FAGCN-based DRAI）在异步图中的实现细节被部分放到在线附录D.1，主文只有一个方向性说明，可能影响对核心机制的完整理解。

## 一句话套路

这篇ISR论文的套路是用一个消费选择理论（CCCDT）把“关系”拆成可计算的维度，再把这些维度逐一翻译成GNN模块和损失项，然后用“整体赢+组件赢+可解释”的三段式实验证明理论到设计的每一环都不是装饰，最后以设计原则和经济价值把性能优势升级为可迁移的IS知识。

## 分析边界

本分析基于主文全文和第一阶段标记的附录引用。部分在线附录（Appendix B、D、E、G、H、I）的内容只能通过摘要和引用推断，无法逐项核查具体数字和细节，因此涉及附录证据的条目标记为间接。表格/公式中的OCR存在少量符号变形（如上下标、矩阵排版），但不影响结构和论证判断。部分低层技术组件（如FAGCN-based DRAI、MS2RSF详细结构）的具体实现被放在在线附录中，主文仅给出方向性介绍。
