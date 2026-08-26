# How Do Recommender Systems Lead to Consumer Purchases? A Causal Mediation Analysis of a Field Experiment：ISR 句段级微观图谱

- 作者：Xitong Li; Jörn Grahl; Oliver Hinz
- 年份：2022
- DOI：10.1287/isre.2021.1074
- 源文件：28279_2022_how-do-recommender-systems-lead-to-consumer-purchases-a-causal-mediation-analysis-of-a-field-exp.md
- 置信度：0.86

## 核实后的宏观骨架

论文以'推荐系统如何通过考虑集影响消费者购买'为核心展开。引言先定义推荐系统、指出早期实验室研究的局限与近期现场研究的共识，再点出现有研究未检验搜索成本假设、未探讨因果路径中的中介因素这一缺口，引入考虑集构念并分解为广度与深度两个维度，概述两个实验室试点实验和现场随机实验的设计、结果与贡献。相关文献综述分为产品销售额与销售多样性两个流派，指出未考察考虑集角色。理论部分以consider-then-choose决策过程为基础，提出广度和深度两个并行中介维度，为每一维度设置对立的理论预测。方法部分先用两个试点实验确定控制条件和推荐数量，再在真实在线书店实施会话级随机现场实验。结果部分先报告描述统计、ITT与ATT总效应，再用因果中介分析分别检验两个单一中介、做敏感性分析和交叉稳健性检验，最后进行双中介分析。讨论部分依次完成理论贡献（机制、考虑集争论、深度维度、启发式决策）、实践贡献（考虑集形成、比较工具、延长顾客旅程）与局限/未来研究（无推荐控制无法分离表层效应、未用bestselling控制、仅记忆型CF、仅图书类别）。

## 摘要逐句图谱

### 1. Abstract S1

- order：1

- locator：Abstract S1

- paraphrase_cn：问句式开头：推荐系统如何诱使消费者购买？

- move_code：GAP/QUESTION

- statement_status：author_inference

- why_here_cn：用研究问题直接建立本文的提问对象，为摘要其余部分提供组织目标。

- inherits_from_previous_cn：无，摘要起点。

- changes_argument_state_cn：把读者焦点从'推荐系统是否有效'转移到'如何/为什么有效'。

- sets_up_next_cn：下一句立即点出现有研究的盲区。

- failure_if_removed_cn：摘要失去问题框架，后续的缺口和方法都失去锚点。

- evidence_pointer：Abstract

### 2. Abstract S2

- order：2

- locator：Abstract S2

- paraphrase_cn：现有研究忽略了检验推荐系统使用导致消费者购买的因果路径。

- move_code：GAP

- statement_status：prior_literature

- why_here_cn：在提出问题后立刻指明文献空白，说明本研究的必要性。

- inherits_from_previous_cn：承接'如何诱使购买'的问题，把问题转化为一个具体缺口。

- changes_argument_state_cn：从提问转向声明研究缺口，为方法选择提供理由。

- sets_up_next_cn：引出下一句'本研究做了什么'。

- failure_if_removed_cn：缺少缺口声明，研究必要性不成立。

- evidence_pointer：Abstract

### 3. Abstract S3

- order：3

- locator：Abstract S3

- paraphrase_cn：本研究在在线图书零售商网站开展随机对照现场实验，并用新近发展的因果中介方法探索因果路径。

- move_code：STUDY_OVERVIEW/METHOD

- statement_status：method_decision

- why_here_cn：紧接缺口之后，说明用何种设计与方法回答缺口。

- inherits_from_previous_cn：缺口需要因果证据；现场实验和因果中介方法直接服务于该需要。

- changes_argument_state_cn：从'缺什么'推进到'如何补'，引入证据来源。

- sets_up_next_cn：为随后两部分结果句提供方法依据。

- failure_if_removed_cn：读者无法知道证据从何而来，结果句失去信度。

- evidence_pointer：Abstract

### 4. Abstract S4

- order：4

- locator：Abstract S4

- paraphrase_cn：结果并不意外：个性化推荐使购买倾向提高12.4%、购物篮金额提高1.7%。

- move_code：RESULT

- statement_status：empirical_result

- why_here_cn：先报告总效应，与文献共识一致，为中介结果提供可分解的总量。

- inherits_from_previous_cn：现场实验提供的数据支撑这一估计。

- changes_argument_state_cn：给出总效应，把问题从'是否有总效应'转到'效应如何传导'。

- sets_up_next_cn：下一句用'更重要的是'引出机制发现。

- failure_if_removed_cn：缺少总效应基线，中介比例无从计算和解释。

- evidence_pointer：Abstract; 正文Section 5.2 Table 6

### 5. Abstract S5

- order：5

- locator：Abstract S5

- paraphrase_cn：更重要的是，这些正向经济效应很大程度上通过影响消费者的考虑集而被中介。

- move_code：MECHANISM/RESULT

- statement_status：empirical_result

- why_here_cn：从总效应升级到机制，是本文的核心主张。

- inherits_from_previous_cn：基于总效应分解，因为中介分析需要先有总效应。

- changes_argument_state_cn：把结果从'推荐系统有效'升级为'推荐系统通过考虑集才有效'。

- sets_up_next_cn：下一句解释考虑集的哪些方面被影响。

- failure_if_removed_cn：摘要和全文的核心贡献消失。

- evidence_pointer：Abstract; 正文Section 5.3

### 6. Abstract S6

- order：6

- locator：Abstract S6

- paraphrase_cn：具体而言，个性化推荐同时增大消费者考虑集规模（广度）和每个备选项的卷入强度（深度）。

- move_code：MECHANISM/RESULT

- statement_status：empirical_result

- why_here_cn：把考虑集分解为两个具体的实证维度，使机制主张可检验、可操作。

- inherits_from_previous_cn：承接'通过考虑集'，进一步说明是哪两个维度。

- changes_argument_state_cn：将单一中介主张细化为双路径机制。

- sets_up_next_cn：下一句说明这两个变化如何进一步影响购买。

- failure_if_removed_cn：失去维度化，机制解释无法与后续中介分析对应。

- evidence_pointer：Abstract; 正文Section 5.1、Table 6

### 7. Abstract S7

- order：7

- locator：Abstract S7

- paraphrase_cn：正是这两个变化继续提高消费者的购买倾向和购物篮价值。

- move_code：MECHANISM/RESULT

- statement_status：empirical_result

- why_here_cn：完成从推荐→考虑集→购买的中介链条表述。

- inherits_from_previous_cn：直接承接'两个变化'，把它们定位为总效应的中介载体。

- changes_argument_state_cn：把中介链条陈述完整：暴露→广度/深度→购买。

- sets_up_next_cn：为下一句的路径比较提供两条路径的对象。

- failure_if_removed_cn：中介链条缺失收尾，广度与深度的作用无法明确是路径而非伴随现象。

- evidence_pointer：Abstract; 正文Section 5.3.3

### 8. Abstract S8

- order：8

- locator：Abstract S8

- paraphrase_cn：进一步发现，通过考虑集广度中介的总效应比例比通过深度中介的比例更大且更显著。

- move_code：CONTRIBUTION/RESULT

- statement_status：empirical_result

- why_here_cn：给出两条路径的相对强弱，这是全文最有辨识度的发现。

- inherits_from_previous_cn：建立在前两句两条路径均中介的基础上。

- changes_argument_state_cn：从'两条路径都存在'推进到'两条路径贡献不均'。

- sets_up_next_cn：暗示这与理论和实践贡献相关（广度更重要）。

- failure_if_removed_cn：失去路径比较，贡献的力度和区分度下降。

- evidence_pointer：Abstract; 正文Section 5.3.3、Table 9与Table 11

## 引言逐句图谱

### 1. Introduction P1 S1

- order：1

- locator：Introduction P1 S1

- paraphrase_cn：定义推荐系统为通过显式或隐式方式获取用户兴趣并据此提出建议的软件代理（引用Xiao & Benbasat）。

- move_code：CONTEXT定义

- statement_status：prior_literature

- why_here_cn：文章开头先给出构成性定义，限定研究对象。

- inherits_from_previous_cn：无，全文起点。

- changes_argument_state_cn：建立研究对象的技术轮廓。

- sets_up_next_cn：下一句区分个性化推荐与简单畅销列表。

- failure_if_removed_cn：研究对象定义缺失，个性化、CF等后续限定缺少基础。

- evidence_pointer：Introduction P1

### 2. Introduction P1 S2

- order：2

- locator：Introduction P1 S2

- paraphrase_cn：推荐可以简单到畅销榜，但本文将焦点限定为基于偏好分析为不同消费者推荐不同产品的个性化推荐系统。

- move_code：CONTEXT收窄

- statement_status：author_inference

- why_here_cn：在定义后立即收窄焦点，说明本文不研究非个性化推荐。

- inherits_from_previous_cn：承接推荐系统的定义，把'个性化'从选项变成研究对象。

- changes_argument_state_cn：把泛化的推荐系统聚焦为个性化推荐系统。

- sets_up_next_cn：为下一句'普适性'和文献回顾中的CF主线设限。

- failure_if_removed_cn：研究对象边界模糊，贡献可能被误读为覆盖所有推荐系统。

- evidence_pointer：Introduction P1

### 3. Introduction P1 S3

- order：3

- locator：Introduction P1 S3

- paraphrase_cn：推荐系统在电商中普遍存在，最著名的例子是Amazon的'买了此商品的顾客还买了'。

- move_code：CONTEXT普适性

- statement_status：prior_literature

- why_here_cn：说明研究主题的现实普遍性，确认其商业重要性。

- inherits_from_previous_cn：承接个性化推荐系统的技术定义。

- changes_argument_state_cn：从技术定义过渡到现实应用广泛。

- sets_up_next_cn：为第二段'现实影响与研究历史'铺垫。

- failure_if_removed_cn：现实重要性削弱，动机不足。

- evidence_pointer：Introduction P1

### 4. Introduction P2 S1

- order：4

- locator：Introduction P2 S1

- paraphrase_cn：推荐系统旨在降低搜索成本并帮助消费者找到最相关产品，因此对电商实践有显著影响并引发大量研究。

- move_code：PRACTICAL_STAKES

- statement_status：prior_literature

- why_here_cn：把主题的现实影响正式化，提示搜索成本这一贯穿全文的机制。

- inherits_from_previous_cn：基于推荐系统普适性。

- changes_argument_state_cn：引入'搜索成本'这一未来被检验的理论前提。

- sets_up_next_cn：下一句指出早期研究的情境局限。

- failure_if_removed_cn：搜索成本线索断掉，后续'未检验假设'的缺口失去内容。

- evidence_pointer：Introduction P2

### 5. Introduction P2 S2

- order：5

- locator：Introduction P2 S2

- paraphrase_cn：早期研究多在实验室进行，所用算法常非当前主流的CF，因此结果能否推广到商业实践并不清楚。

- move_code：LIMITATION早期研究局限

- statement_status：prior_literature

- why_here_cn：先承认实验研究的价值但指出可推广性问题，为现场数据研究必要性铺垫。

- inherits_from_previous_cn：承接研究重要性与已有研究。

- changes_argument_state_cn：把文献从实验室研究转向现场研究的需求。

- sets_up_next_cn：下一段立即介绍近期现场研究。

- failure_if_removed_cn：缺少研究史必要性，现场实验设计缺乏理由。

- evidence_pointer：Introduction P2

### 6. Introduction P3 S1

- order：6

- locator：Introduction P3 S1

- paraphrase_cn：近期研究使用现场数据检查主流的CF推荐系统对销售和销售多样性的影响，存在一个共识：推荐系统能提高购买倾向并带来更多销售。

- move_code：PRIOR_KNOWLEDGE共识

- statement_status：prior_literature

- why_here_cn：概括领域共识，为随后批判'只研究总效应'设定靶子。

- inherits_from_previous_cn：承接上一句对现场数据研究的需要。

- changes_argument_state_cn：确立既有研究的正面成果。

- sets_up_next_cn：下一句用'然而'转向机制未检验。

- failure_if_removed_cn：缺少共识，'领域盲区'的批评失去对象。

- evidence_pointer：Introduction P3; 对应Section 2.1

### 7. Introduction P3 S2

- order：7

- locator：Introduction P3 S2

- paraphrase_cn：先前研究大多假设推荐系统降低搜索成本、帮助消费者找到更匹配的产品，却未用现场数据检验这些假设，尤其未探索因果路径和中介因素。

- move_code：LIMITATION核心缺口

- statement_status：prior_literature

- why_here_cn：点出最核心的分析盲区：搜索成本被当成假设而非检验对象。

- inherits_from_previous_cn：基于共识性总效应，批判其机制深度。

- changes_argument_state_cn：把文献图景从'有正面效应'转为'机制不明'。

- sets_up_next_cn：下一句给出缺口结论和对机制理解的限制。

- failure_if_removed_cn：全文研究缺口消失，问句式标题失去依据。

- evidence_pointer：Introduction P3

### 8. Introduction P3 S3

- order：8

- locator：Introduction P3 S3

- paraphrase_cn：因此，既有研究对推荐系统经济效应背后的机制理解有限。

- move_code：GAP声明

- statement_status：author_inference

- why_here_cn：把前一句的观察概括为正式的研究缺口。

- inherits_from_previous_cn：直接承接'未检验因果路径'。

- changes_argument_state_cn：确认缺口存在，为本文目标定位。

- sets_up_next_cn：下一段引入考虑集作为填补缺口的理论构念。

- failure_if_removed_cn：研究动机没有正式声明，理论引入显得突兀。

- evidence_pointer：Introduction P3

### 9. Introduction P4 S1

- order：9

- locator：Introduction P4 S1

- paraphrase_cn：本研究旨在填补缺口，提出消费者考虑集在推荐系统影响购买和销售的因果路径中起重要作用。

- move_code：THEORY_INTRO/PURPOSE

- statement_status：author_inference

- why_here_cn：在缺口声明后立即引入理论透镜，给出研究目的。

- inherits_from_previous_cn：回应上一句'机制理解有限'。

- changes_argument_state_cn：从'缺什么'转到'用什么填补'。

- sets_up_next_cn：下一句将缺口进一步具体化到考虑集未被研究。

- failure_if_removed_cn：理论贡献的起点丢失。

- evidence_pointer：Introduction P4

### 10. Introduction P4 S2

- order：10

- locator：Introduction P4 S2

- paraphrase_cn：据作者所知，现有对推荐系统的现场数据研究尚未探索考虑集在推荐系统影响购买中的角色；De等人只猜测消费者会进行更多外部搜索、发现更多产品并购买，但没有直接检验考虑集。

- move_code：GAP具体化

- statement_status：prior_literature

- why_here_cn：用一个具体文献实例说明'只猜测未检验'，使缺口更可信。

- inherits_from_previous_cn：承接考虑集构念的引入。

- changes_argument_state_cn：把缺口从泛泛机制空缺收缩到考虑集这一具体构念。

- sets_up_next_cn：下一段基于搜索成本和偏好匹配推理两个中介维度。

- failure_if_removed_cn：缺口的独特性减弱，'首次'声明缺少依据。

- evidence_pointer：Introduction P4; 参见De et al. 2010

### 11. Introduction P5 S1

- order：11

- locator：Introduction P5 S1

- paraphrase_cn：既然推荐系统降低搜索成本，很可能影响消费者考虑集的大小；同时因推荐更符合偏好，消费者对考虑集中备选项的卷入会与无推荐时不同。

- move_code：MECHANISM推理

- statement_status：author_inference

- why_here_cn：从搜索成本和偏好匹配两大前提推出两个中介维度。

- inherits_from_previous_cn：利用前面引入的搜索成本假设和考虑集概念。

- changes_argument_state_cn：明确两条候选路径：广度与深度。

- sets_up_next_cn：下一句把这些推理正式整理为研究模型。

- failure_if_removed_cn：两个中介维度的来源断裂，理论模型无依据。

- evidence_pointer：Introduction P5

### 12. Introduction P5 S2

- order：12

- locator：Introduction P5 S2

- paraphrase_cn：因此作者建立研究模型：考虑集中介推荐系统对购买的影响，具体为考虑集规模（广度）和每备选项卷入（深度）两个维度，二者进而影响购买倾向。

- move_code：RQ/MODEL

- statement_status：theory_claim

- why_here_cn：把推理表述为可检验的中介模型。

- inherits_from_previous_cn：整合上一句的机制推理和考虑集文献。

- changes_argument_state_cn：提出正式研究模型，后续实验和中介分析都围绕它。

- sets_up_next_cn：下一段说明用什么研究设计检验模型。

- failure_if_removed_cn：没有模型，实验设计和中介方法都失去组织原则。

- evidence_pointer：Introduction P5; 与Section 3、Figure 1对应

### 13. Introduction P6 S1

- order：13

- locator：Introduction P6 S1

- paraphrase_cn：为用现场数据检验中介模型，作者与欧洲大型在线图书零售商合作开展随机对照现场实验；为确定现场实验的设计选择，先做两个实验室试点实验。

- move_code：STUDY_OVERVIEW

- statement_status：method_decision

- why_here_cn：说明证据项目和总体设计顺序：试点→现场。

- inherits_from_previous_cn：模型需要实证检验。

- changes_argument_state_cn：从理论过渡到研究设计。

- sets_up_next_cn：下一句报告试点结果并引出设计选择。

- failure_if_removed_cn：研究设计动机缺失，方法部分缺乏上下文。

- evidence_pointer：Introduction P6

### 14. Introduction P6 S2

- order：14

- locator：Introduction P6 S2

- paraphrase_cn：第一个试点显示CF推荐相比无推荐和随机展示产品提高购买；第二个试点显示CF推荐相对无推荐的效果与推荐数量呈倒U形，展示三条推荐有效。

- move_code：RESULT试点

- statement_status：empirical_result

- why_here_cn：用试点证据为现场实验的控制条件和推荐数量辩护。

- inherits_from_previous_cn：试点实验的执行结果。

- changes_argument_state_cn：确定现场实验两个关键参数：无推荐控制、三条推荐。

- sets_up_next_cn：下一句描述现场实验具体部署。

- failure_if_removed_cn：现场实验设计选择变成任意决定，内部有效性受损。

- evidence_pointer：Introduction P6; 与Section 4.1、Table 2、Table 3对应

### 15. Introduction P6 S3

- order：15

- locator：Introduction P6 S3

- paraphrase_cn：现场实验使用CF算法，将一半访问会话随机分配到处理组并展示三条推荐于焦点书下方，控制组关闭推荐且页面其他元素完全一致。

- move_code：DESIGN_FEATURE

- statement_status：design_decision

- why_here_cn：给出处理与控制的精确操作，保障可复制性。

- inherits_from_previous_cn：按试点确定的参数和业界实践设计。

- changes_argument_state_cn：把设计选择落实为具体实验操作。

- sets_up_next_cn：为下一段报告结果提供实验基础。

- failure_if_removed_cn：不知道干预的具体形态，结果不可解释。

- evidence_pointer：Introduction P6; 与Section 4.2和Figure 2对应

### 16. Introduction P7 S1

- order：16

- locator：Introduction P7 S1

- paraphrase_cn：结果显示推荐系统平均提高下单倾向12.4%、每会话收入1.7%、考虑集规模3.2%、卷入深度0.9%，且都在95%水平显著。

- move_code：RESULT总效应

- statement_status：empirical_result

- why_here_cn：给出四个关键因变量的ITT效应，为一整段机制分析提供数量基础。

- inherits_from_previous_cn：来自现场实验估计。

- changes_argument_state_cn：确认总效应和两个中介变量的处理效应。

- sets_up_next_cn：下一句转向效应异质性（合规者驱动）。

- failure_if_removed_cn：总效应缺失，中介比例和ATT比较都没有参照。

- evidence_pointer：Introduction P7; 与Table 6对应

### 17. Introduction P7 S2

- order：17

- locator：Introduction P7 S2

- paraphrase_cn：进一步分析显示，效应主要由点击并查看至少一条推荐产品的消费者驱动，而仅被展示推荐但不点击的消费者几乎没有效应。

- move_code：RESULT异质性/机制

- statement_status：empirical_result

- why_here_cn：用合规者/不合规者对比排除纯暴露效应，强化机制解读。

- inherits_from_previous_cn：基于处理组内部点击行为分类与ITT比较。

- changes_argument_state_cn：把效应归因于实际接触推荐内容的消费者。

- sets_up_next_cn：为下一句中的中介分析建立'接触推荐'的操作性入口。

- failure_if_removed_cn：无法排除'仅仅看到推荐'也能产生效应，弱化中介机制解释。

- evidence_pointer：Introduction P7; 与Section 5.2、Table 7对应

### 18. Introduction P7 S3

- order：18

- locator：Introduction P7 S3

- paraphrase_cn：采用因果中介分析发现，考虑集规模与每备选项卷入都中介推荐系统对购买的作用；直接效应不显著，属于完全中介/间接-only；点估计显示两条路径分别中介25.7%和9.9%，合计39.2%的总效应。

- move_code：RESULT核心/机制

- statement_status：empirical_result

- why_here_cn：给出全文最核心的定量发现，把机制主张落到数字。

- inherits_from_previous_cn：建立在总效应显著和中介框架的基础上。

- changes_argument_state_cn：从'推荐有效'推进到'推荐如何有效'并给出路径份额。

- sets_up_next_cn：下一段据此列出四项贡献。

- failure_if_removed_cn：核心贡献和摘要、讨论的机制主张都失去锚点。

- evidence_pointer：Introduction P7; 与Section 5.3.1-5.3.3、Table 9、Table 11对应

### 19. Introduction P8 S1

- order：19

- locator：Introduction P8 S1

- paraphrase_cn：贡献一：虽现场研究发现正面效应，但对机制的中介视角仍缺；作者最早从中介视角揭示从推荐呈现到购买的因果路径，并发现广度和深度都中介效应。

- move_code：CONTRIBUTION机制贡献

- statement_status：contribution_claim

- why_here_cn：把机制发现正式表述为IS文献贡献。

- inherits_from_previous_cn：直接建立在核心中介结果上。

- changes_argument_state_cn：从证据切换到贡献判定。

- sets_up_next_cn：下一句继续列出第二、三、四项贡献。

- failure_if_removed_cn：研究的意义不够显性，摘要的贡献声明失去分量。

- evidence_pointer：Introduction P8; 对应Discussion 6.1

### 20. Introduction P8 S2

- order：20

- locator：Introduction P8 S2

- paraphrase_cn：贡献二和三：学者对推荐系统增大或减小考虑集有对立预测且多为实验室研究，本文提供第一个现场实验证据支持推荐系统扩大考虑集并提高转化率；同时首次发现每备选项卷入深度也中介正向效应。

- move_code：CONTRIBUTION争论/深度缺口

- statement_status：contribution_claim

- why_here_cn：将现场证据置于既有实验室争论和深度维度空白中，凸显独特位置。

- inherits_from_previous_cn：联系引言P4和理论部分的文献争议。

- changes_argument_state_cn：把贡献定位为对具体文献争论的直接介入。

- sets_up_next_cn：下一句给出方法贡献。

- failure_if_removed_cn：贡献缺乏文献对照，'首次'与'第一'的可信度降低。

- evidence_pointer：Introduction P8; 对应Discussion 6.1第二、三点

### 21. Introduction P8 S3

- order：21

- locator：Introduction P8 S3

- paraphrase_cn：贡献四：方法上使用最近发展的因果中介方法，允许对中介结果作清晰因果解释，而IS文献对此关注甚少。

- move_code：CONTRIBUTION方法贡献

- statement_status：contribution_claim

- why_here_cn：把方法引入本身作为一项独立贡献，说明方法论新颖性。

- inherits_from_previous_cn：基于方法实施与IS文献缺口。

- changes_argument_state_cn：扩展贡献维度到方法层面。

- sets_up_next_cn：为后文方法与中介分析章节提供安排提示。

- failure_if_removed_cn：方法的独特价值不显，IS读者的复制价值下降。

- evidence_pointer：Introduction P8; 对应Section 5.3开头

## 引言逐段图谱

### 1. Introduction P1

- locator：Introduction P1

- opening_move_cn：以学术定义开启，建立研究对象的技术轮廓。

- development_move_cn：从定义收窄到个性化推荐，再以Amazon为例说明普适性。

- pivot_move_cn：在S2处从一般推荐系统转向个性化推荐，限定全文边界。

- closing_move_cn：以现实普遍性收束，为第二段商业重要性开路。

- paragraph_job_cn：界定研究对象并说明其现实地位，为后续所有论证设限。

### 2. Introduction P2

- locator：Introduction P2

- opening_move_cn：从推荐系统的目标（降低搜索成本）和商业影响切入。

- development_move_cn：承认研究历史与实验室研究的局限，提出可推广性问题。

- pivot_move_cn：从'有大量研究'转向'早期研究能否推广到商业实践'。

- closing_move_cn：以'不清楚可推广性'制造对现场数据研究的需要。

- paragraph_job_cn：确立搜索成本作为理论前提，并铺垫现场研究必要性。

### 3. Introduction P3

- locator：Introduction P3

- opening_move_cn：以近期现场研究的共识性发现开启。

- development_move_cn：列举共识（提高购买倾向和销售）后立即指出搜索成本假设未被检验。

- pivot_move_cn：从'已知什么'转向'未知什么'。

- closing_move_cn：正式声明机制理解有限，制造研究缺口。

- paragraph_job_cn：构造全文核心缺口：总效应共识与机制未知之间的缝隙。

### 4. Introduction P4

- locator：Introduction P4

- opening_move_cn：以研究目的和理论透镜（考虑集）开启。

- development_move_cn：断言考虑集起重要作用，并用De等人'只猜测未检验'的具体案例强化。

- pivot_move_cn：从泛泛机制缺口收窄到'考虑集角色缺失'。

- closing_move_cn：用具体文献实例结束，让缺口变得可操作。

- paragraph_job_cn：把研究缺口具体化到考虑集构念，引入理论核心。

### 5. Introduction P5

- locator：Introduction P5

- opening_move_cn：从搜索成本和偏好匹配两个机制前提开始推理。

- development_move_cn：分别推出广度（考虑集大小）和深度（每备选项卷入）可能被影响。

- pivot_move_cn：从机制推理转向正式研究模型。

- closing_move_cn：以'研究模型'收束，并声明两个维度都影响购买。

- paragraph_job_cn：提出并正式化可检验的双中介理论模型。

### 6. Introduction P6

- locator：Introduction P6

- opening_move_cn：以'如何检验模型'开启，说明合作对象与整体设计顺序。

- development_move_cn：先报告试点结果，再说明据此确定的现场实验设计。

- pivot_move_cn：从试点设计选择过渡到现场实验部署。

- closing_move_cn：以处理组和控制组精确操作收束，为结果段提供设计基础。

- paragraph_job_cn：预告研究设计并说明关键设计选择有实验依据。

### 7. Introduction P7

- locator：Introduction P7

- opening_move_cn：直接报告总效应结果。

- development_move_cn：从总效应到合规者异质性，再到因果中介结果，层层收窄。

- pivot_move_cn：从'推荐有效'转向'推荐为何有效'。

- closing_move_cn：以路径份额（25.7%、9.9%、39.2%）收束，制造贡献段需要。

- paragraph_job_cn：用三段式结果（总效应、异质性、机制）全景呈现核心发现。

### 8. Introduction P8

- locator：Introduction P8

- opening_move_cn：直接以'对IS文献有几方面贡献'开启。

- development_move_cn：逐一排列机制贡献、考虑集争论贡献、深度维度贡献和方法贡献。

- pivot_move_cn：从证据陈述转向贡献判定。

- closing_move_cn：以方法贡献收束，为正文方法章节预告。

- paragraph_job_cn：把全文发现翻译为四条定位明确的文献贡献。

## 理论到设计逐句图谱

### 1. Theory Development Section 3 P1 S1

- order：1

- locator：Theory Development Section 3 P1 S1

- paraphrase_cn：提出考虑集这一营销和IS中的成熟构念在推荐系统影响购买和销售的路径中起中介作用。

- move_code：THEORY_INTRO

- statement_status：theory_claim

- why_here_cn：理论章节开头正式引入核心构念，为全文机制主张奠基。

- inherits_from_previous_cn：承接引言中考虑集缺口的声明。

- changes_argument_state_cn：从文献缺口进入理论建构。

- sets_up_next_cn：下一句展开考虑-然后-选择决策过程。

- failure_if_removed_cn：理论章节失去起点，考虑集无法成为中介变量。

- evidence_pointer：Section 3 P1

### 2. Theory Development Section 3 P1 S2

- order：2

- locator：Theory Development Section 3 P1 S2

- paraphrase_cn：大量文献表明消费者用'考虑-然后-选择'过程简化购买决策：先识别考虑集，再从考虑集中选择购买。

- move_code：THEORY_PROPOSITION

- statement_status：prior_literature

- why_here_cn：提供考虑集发挥中介作用的决策过程基础。

- inherits_from_previous_cn：承接考虑集构念的引入。

- changes_argument_state_cn：把考虑集从静态构念变成决策过程的一部分。

- sets_up_next_cn：下一句强调考虑集形成与备选项评估可并行。

- failure_if_removed_cn：没有两阶段决策过程，广度和深度的'同时'中介失去理论基础。

- evidence_pointer：Section 3 P1

### 3. Theory Development Section 3 P1 S3

- order：3

- locator：Theory Development Section 3 P1 S3

- paraphrase_cn：注意在考虑-然后-选择中，考虑集形成与备选项卷入可并行发生：消费者边搜索边评估，在购买前访问和重访考虑集中的备选项。

- move_code：MECHANISM并行性

- statement_status：author_inference

- why_here_cn：排除广度在前、深度在后的顺序假设，为设计两个同步中介变量铺路。

- inherits_from_previous_cn：基于考虑-然后-选择过程。

- changes_argument_state_cn：确认为两个中介可同时进入模型。

- sets_up_next_cn：下一句正式提出两个维度并给出Figure 1。

- failure_if_removed_cn：如果两阶段有先后，双中介模型和现场测量设计都可能被质疑。

- evidence_pointer：Section 3 P1

### 4. Theory Development Section 3 P1 S4

- order：4

- locator：Theory Development Section 3 P1 S4

- paraphrase_cn：作者基于考虑-然后-选择过程区分两个维度：广度（考虑集规模）和深度（每备选项卷入），并提议二者中介推荐系统对购买的影响；图1展示模型。

- move_code：THEORY_PROPOSITION

- statement_status：theory_claim

- why_here_cn：正式提出全文可检验的中介模型，作为设计测量和统计分析的总纲。

- inherits_from_previous_cn：整合两阶段过程和并行性讨论。

- changes_argument_state_cn：从理论叙述转为模型命题。

- sets_up_next_cn：后文两个小节分别展开两个维度。

- failure_if_removed_cn：模型命题缺失，实验的中介变量选择失去直接来源。

- evidence_pointer：Section 3 P1, Figure 1

### 5. Theory Development Section 3.1 P1 S1

- order：5

- locator：Theory Development Section 3.1 P1 S1

- paraphrase_cn：关于推荐系统减少还是增加考虑集规模，既有理论给出矛盾预测。

- move_code：THEORY_PROPOSITION张力

- statement_status：prior_literature

- why_here_cn：把广度维度定义为经验问题，为后续现场证据提供定位。

- inherits_from_previous_cn：承接总体模型中广度维度。

- changes_argument_state_cn：把方向问题开放化，预示需要数据裁决。

- sets_up_next_cn：下一段陈述'缩小'机制的推理和证据。

- failure_if_removed_cn：没有矛盾预测，'现场证据第一次支持扩大'的贡献失去对比背景。

- evidence_pointer：Section 3.1 P1

### 6. Theory Development Section 3.1 P2 S1

- order：6

- locator：Theory Development Section 3.1 P2 S1

- paraphrase_cn：一方面，推荐系统基于偏好分析让消费者更快更易找到最相关产品，因此不需加入太多备选，考虑集可能变小；Haubl等人的系列实验支持这一预测。

- move_code：MECHANISM缩小机制

- statement_status：theory_claim

- why_here_cn：给出第一种对立预测及其实验室证据。

- inherits_from_previous_cn：承接上一句矛盾预测中的'减少'一侧。

- changes_argument_state_cn：展开减方向的机制链条。

- sets_up_next_cn：下一段给出'扩大'机制作为对立面。

- failure_if_removed_cn：缺少'缩小'一侧，矛盾张力消失，经验贡献无从谈起。

- evidence_pointer：Section 3.1 P2

### 7. Theory Development Section 3.1 P3 S1

- order：7

- locator：Theory Development Section 3.1 P3 S1

- paraphrase_cn：另一方面，消费者权衡加一个备选的边际收益与成本；推荐系统提高备选项预期效用并降低搜索成本，因此消费者会搜索并加入更多备选，扩大考虑集。

- move_code：MECHANISM扩大机制

- statement_status：theory_claim

- why_here_cn：给出第二种对立预测和完整机制推理，与上一段形成对称。

- inherits_from_previous_cn：承接'增加'一侧，并利用引言中的搜索成本前提。

- changes_argument_state_cn：展开增方向的机制链条，并引出实证文献（Pereira、Zhang等人）。

- sets_up_next_cn：下一句进一步说明考虑集规模对购买既可能促进也可能过载，仍是经验问题。

- failure_if_removed_cn：'扩大'机制消失，现场发现'扩大'就缺乏理论预期支撑。

- evidence_pointer：Section 3.1 P3

### 8. Theory Development Section 3.1 P4 S1

- order：8

- locator：Theory Development Section 3.1 P4 S1

- paraphrase_cn：更大的考虑集既可能提高'命中'购买意图的机会，也可能因信息过载降低购买倾向，因此这也是经验问题。

- move_code：BOUNDARY_CONDITION

- statement_status：theory_claim

- why_here_cn：把'规模→购买'的关系也设为开放问题，证明需要真正的中介检验。

- inherits_from_previous_cn：承接考虑集规模的方向争议。

- changes_argument_state_cn：为统计上检验总效应和中介而非仅理论推导提供依据。

- sets_up_next_cn：引出'用现场实验数据回答这些经验问题'的承诺。

- failure_if_removed_cn：如果不承认过载可能性，现场发现'扩大→更多购买'的理论贡献减弱。

- evidence_pointer：Section 3.1 P4

### 9. Theory Development Section 3.2 P1 S1

- order：9

- locator：Theory Development Section 3.2 P1 S1

- paraphrase_cn：一方面推荐产品应更吸引注意、更相关，消费者可能看更久；另一方面推荐更贴合偏好使比较更直接高效，消费者可能花更少时间；因此卷入深度方向也是经验问题。

- move_code：THEORY_PROPOSITION/MECHANISM

- statement_status：theory_claim

- why_here_cn：为第二个中介维度设置同样的理论两难。

- inherits_from_previous_cn：承接总体模型的深度维度。

- changes_argument_state_cn：把深度也定义为需要数据裁决的开放问题。

- sets_up_next_cn：下一句引入卷入-承诺文献把深度与购买联系起来。

- failure_if_removed_cn：深度维度失去理论张力，'首次发现深度中介'的贡献无法成立。

- evidence_pointer：Section 3.2 P1

### 10. Theory Development Section 3.2 P2 S1

- order：10

- locator：Theory Development Section 3.2 P2 S1

- paraphrase_cn：消费者心理学表明，卷入和参与产品会形成情感联结、提高承诺并诱发购买；产品与品牌层面以及线下超市证据都支持'卷入→承诺→购买'。

- move_code：MECHANISM卷入-承诺

- statement_status：theory_claim

- why_here_cn：建立从深度到购买的理论桥梁，使深度成为有正向预期路径的中介。

- inherits_from_previous_cn：承接深度是经验问题，但此处给出一个方向的理论支持。

- changes_argument_state_cn：把深度的经验问题与积极购买效应联系起来。

- sets_up_next_cn：为后文的现场测量（每备选项页面浏览数）与方法设计提供理论意义。

- failure_if_removed_cn：深度即使被测量，也难以解释为什么它会导致购买。

- evidence_pointer：Section 3.2 P2

## 制品设计理由逐句图谱

### 1. Section 4.1 P1 S1

- order：1

- locator：Section 4.1 P1 S1

- paraphrase_cn：现场实验有两个关键设计选择：控制/基线条件和处理组推荐的条数；作者用两个实验室试点实验来确定它们。

- move_code：DESIGN_RATIONALE总述

- statement_status：method_decision

- why_here_cn：在报告现场实验前，先声明两个参数均由试点证据决定。

- inherits_from_previous_cn：理论模型要现场检验，设计必须可辩护。

- changes_argument_state_cn：把设计选择变成有证据支撑的决策。

- sets_up_next_cn：引出Pilot Study 1和2的详细介绍。

- failure_if_removed_cn：现场实验参数显得武断，削弱实验效度。

- evidence_pointer：Section 4.1 P1, Table 1

### 2. Section 4.1.1 P1 S1

- order：2

- locator：Section 4.1.1 P1 S1

- paraphrase_cn：无推荐是自然的控制选择，但估计效应可能包含单纯展示产品的表层效应；随机推荐可作替代控制来分离表层效应。

- move_code：BENCHMARK_RATIONALE控制选择

- statement_status：method_decision

- why_here_cn：解释为何在试点中加入随机推荐条件，预先识别控制组的解释边界。

- inherits_from_previous_cn：承接'控制条件'设计选择。

- changes_argument_state_cn：为'无推荐作基线'制造方法论疑虑，随后用试点结果消除。

- sets_up_next_cn：为Pilot Study 1的四条件设计提供逻辑。

- failure_if_removed_cn：缺少表层效应意识，后续局限讨论中的'组合效应'声明无铺垫。

- evidence_pointer：Section 4.1.1 P1

### 3. Section 4.1.1 P6 S1

- order：3

- locator：Section 4.1.1 P6 S1

- paraphrase_cn：无推荐和随机推荐的系数都显著为负且值相似，说明随机推荐不优于无推荐，无推荐可作为现场实验的合理控制/基线。

- move_code：DESIGN_RATIONALE控制确定

- statement_status：empirical_result

- why_here_cn：用试点证据回答第一个设计选择：无推荐是合理控制。

- inherits_from_previous_cn：承接试点OLS结果和上一句对随机推荐的讨论。

- changes_argument_state_cn：把'无推荐作控制'从惯例升级为经验支持的决策。

- sets_up_next_cn：下一段处理第二个设计选择：推荐条数。

- failure_if_removed_cn：现场实验控制组合法性失去证据基础。

- evidence_pointer：Section 4.1.1, Table 2

### 4. Section 4.1.2 P3 S1

- order：4

- locator：Section 4.1.2 P3 S1

- paraphrase_cn：n=3的推荐效果显著为正且显著大于n=1和n=5，呈倒U形；因此现场实验处理组展示三条推荐。

- move_code：DESIGN_RATIONALE条数确定

- statement_status：empirical_result

- why_here_cn：用试点证据回答第二个设计选择，并明确指出从结果到决策的推断。

- inherits_from_previous_cn：承接Pilot Study 2的回归和t检验结果。

- changes_argument_state_cn：确定处理组推荐条数并说明条数效应形状。

- sets_up_next_cn：为现场实验干预的具体实现提供参数。

- failure_if_removed_cn：三条推荐的选择没有依据，处理组设计不稳。

- evidence_pointer：Section 4.1.2, Table 3

### 5. Section 4.1.2 P3 S2

- order：5

- locator：Section 4.1.2 P3 S2

- paraphrase_cn：作者谨慎指出n=3未必可推广到其他情境，但因测试了三个产品类别（包括书），展示三条推荐至少是现场实验的合理选择。

- move_code：BOUNDARY_DESIGN

- statement_status：author_inference

- why_here_cn：在把试点决策用于现场之前主动限定其外部效度。

- inherits_from_previous_cn：紧接三条推荐有效的结论。

- changes_argument_state_cn：防止读者把'三条'误读为普适最优。

- sets_up_next_cn：让现场实验设计决策既坚定又有边界。

- failure_if_removed_cn：条数选择可能被批评为过拟合试点数据。

- evidence_pointer：Section 4.1.2 P3

### 6. Section 4.2 P2 S1

- order：6

- locator：Section 4.2 P2 S1

- paraphrase_cn：现场实验的目标是实证检验第三节提出的中介模型。

- move_code：DESIGN_RATIONALE目标

- statement_status：method_decision

- why_here_cn：把现场实验设计重新锚定到理论模型，防止被当作单纯性能测试。

- inherits_from_previous_cn：连接理论模型和实际干预。

- changes_argument_state_cn：强调干预的目标是机制检验而非性能优化。

- sets_up_next_cn：随后描述随机化、处理和测量。

- failure_if_removed_cn：现场实验与理论脱节，中介测量显得无关。

- evidence_pointer：Section 4.2 P2

### 7. Section 4.2 P3 S1

- order：7

- locator：Section 4.2 P3 S1

- paraphrase_cn：处理在会话层随机分配并保持回访者分组稳定；处理组在焦点书详情页下方显示三条由CF生成的书名推荐，控制组看不到任何推荐；其他页面元素完全一致。

- move_code：DESIGN_FEATURE

- statement_status：design_decision

- why_here_cn：给出干预可复制的具体操作，并说明随机化单元。

- inherits_from_previous_cn：承接试点确定的条数和业界展示惯例。

- changes_argument_state_cn：把设计选择落实为可执行的实验协议。

- sets_up_next_cn：为描述统计、平衡性检验和ITT估计提供实验基础。

- failure_if_removed_cn：不知道干预的具体操作，所有估计都难以解释。

- evidence_pointer：Section 4.2, Figure 2

## Study开头、过渡与收束图谱

### 1. Study 1/Pilot Study 1 opening P1

- order：1

- locator：Study 1/Pilot Study 1 opening P1

- paraphrase_cn：介绍Pilot Study 1的目的：比较CF推荐、无推荐、随机推荐和畅销推荐四种条件，判断无推荐是否可作为合理控制。

- move_code：OPENING目的声明

- statement_status：method_decision

- why_here_cn：在报告试点前交代其在整个证据链中的位置。

- inherits_from_previous_cn：承接Section 4.1对两个设计选择的说明。

- changes_argument_state_cn：进入第一个证据阶段。

- sets_up_next_cn：后面描述实验被试、商店、算法和结果。

- failure_if_removed_cn：读者不知试点要解决什么问题。

- evidence_pointer：Section 4.1.1 P1

### 2. Study 1/Pilot Study 1 closure

- order：2

- locator：Study 1/Pilot Study 1 closure

- paraphrase_cn：结论：CF推荐优于无推荐和随机推荐，随机推荐与无推荐效果相似；无推荐可作为现场实验的合理控制。

- move_code：CLOSURE结论与过渡

- statement_status：empirical_result

- why_here_cn：以设计决策收束试点1，并把结论传递给下一个设计问题。

- inherits_from_previous_cn：基于Table 2结果。

- changes_argument_state_cn：确定第一个设计参数。

- sets_up_next_cn：下一节进入第二个设计参数（推荐条数）。

- failure_if_removed_cn：控制条件决策悬空，现场实验无法开始。

- evidence_pointer：Section 4.1.1结尾, Table 2

### 3. Study 2/Pilot Study 2 opening P1

- order：3

- locator：Study 2/Pilot Study 2 opening P1

- paraphrase_cn：Pilot Study 2旨在确定现场实验处理组展示多少条推荐，因此包含n=0、1、3、5四个条件。

- move_code：OPENING目的声明

- statement_status：method_decision

- why_here_cn：在报告第二个试点前交代其针对性问题。

- inherits_from_previous_cn：承接试点1已确定控制条件后的下一步。

- changes_argument_state_cn：进入第二个参数确定阶段。

- sets_up_next_cn：后文描述被试、商店和结果。

- failure_if_removed_cn：推荐条数设计无来由。

- evidence_pointer：Section 4.1.2 P1

### 4. Study 2/Pilot Study 2 closure

- order：4

- locator：Study 2/Pilot Study 2 closure

- paraphrase_cn：结论：3条推荐显著有效，现场实验使用n=3，但该数字可能不普适；三个产品类别都支持这一选择。

- move_code：CLOSURE结论与边界

- statement_status：empirical_result

- why_here_cn：以设计决策加边界声明收束试点2。

- inherits_from_previous_cn：基于Table 3结果。

- changes_argument_state_cn：确定第二个设计参数并主动限定其外推性。

- sets_up_next_cn：下一节进入真实现场实验设计。

- failure_if_removed_cn：处理组条数无依据且可能被视为过度拟合。

- evidence_pointer：Section 4.1.2结尾, Table 3

### 5. Field experiment opening P1-P2

- order：5

- locator：Field experiment opening P1-P2

- paraphrase_cn：描述合作书店为荷兰纯在线电子书零售商、此前从未使用推荐系统，现场实验目的是检验第三节中介模型。

- move_code：OPENING情境与目的

- statement_status：method_decision

- why_here_cn：在报告现场实验前确认真实平台上下文，并重申检验理论模型的目的。

- inherits_from_previous_cn：承接试点确定的参数。

- changes_argument_state_cn：把证据从实验室推进到真实平台。

- sets_up_next_cn：随后介绍推荐系统部署、随机化和处理。

- failure_if_removed_cn：现场实验的生态效度与理论目标不清。

- evidence_pointer：Section 4.2 P1-P2

### 6. Field experiment transition to results

- order：6

- locator：Field experiment transition to results

- paraphrase_cn：描述完设计与随机化后，下一节开始报告描述统计、平衡性、ITT和ATT。

- move_code：TRANSITION设计→结果

- statement_status：method_decision

- why_here_cn：从设计部分转向证据部分，为读者提供路径指引。

- inherits_from_previous_cn：基于实验协议完成。

- changes_argument_state_cn：完成了证据生成条件，进入证据呈现。

- sets_up_next_cn：为Section 5.1描述统计开路。

- failure_if_removed_cn：设计与结果之间缺乏衔接，读者容易迷失。

- evidence_pointer：Section 4.2结尾至Section 5.1

### 7. Results 5.1 opening

- order：7

- locator：Results 5.1 opening

- paraphrase_cn：说明测量单位为处理/控制会话，收集浏览、时间戳、购买和图书信息。

- move_code：OPENING数据来源与单位

- statement_status：method_decision

- why_here_cn：在给出任何数字前交代数据来源和测量粒度。

- inherits_from_previous_cn：现场实验部署的直接产物。

- changes_argument_state_cn：建立结果章节的证据基础。

- sets_up_next_cn：随后报告描述统计和操作化。

- failure_if_removed_cn：统计结果缺乏测量上下文。

- evidence_pointer：Section 5.1 P1

### 8. Results 5.1 operationalization P3

- order：8

- locator：Results 5.1 operationalization P3

- paraphrase_cn：参考Moe和Ghose等文献，将考虑集操作化为会话中浏览的独特图书集合，广度为独特图书数，深度为每个独特书的平均页面浏览数。

- move_code：OPERATIONALIZATION理论→测量

- statement_status：method_decision

- why_here_cn：把理论构念转成可计算的变量，并引用文献证明测量合理。

- inherits_from_previous_cn：承接描述统计对'CS size'和'Page views per product'的定义。

- changes_argument_state_cn：让中介变量进入统计分析。

- sets_up_next_cn：为后续对数变换和回归使用奠定基础。

- failure_if_removed_cn：中介分析与理论构念脱钩，测量效度存疑。

- evidence_pointer：Section 5.1 P3, Table 4

### 9. Results 5.2 transition

- order：9

- locator：Results 5.2 transition

- paraphrase_cn：在描述统计符合中介模型后，作者先估计推荐系统对结果和中介变量的总体效应。

- move_code：TRANSITION描述→总效应

- statement_status：empirical_result

- why_here_cn：从描述统计进入正式估计，先建立总效应。

- inherits_from_previous_cn：基于Table 5比较显示处理组显著更高。

- changes_argument_state_cn：从描述性证据升级为回归估计。

- sets_up_next_cn：报告ITT效应并与Lee和Hosanagar比较。

- failure_if_removed_cn：总效应没有正式估计，中介无从分解。

- evidence_pointer：Section 5.2 P1

### 10. Results 5.2 complier/non-complier discussion

- order：10

- locator：Results 5.2 complier/non-complier discussion

- paraphrase_cn：并非所有消费者对推荐同样敏感；区分点击查看至少一条推荐的合规者和未点击的不合规者。

- move_code：OPENING异质性

- statement_status：method_decision

- why_here_cn：引入消费者异质性，为区分ITT与ATT作准备。

- inherits_from_previous_cn：基于处理组内点击行为数据。

- changes_argument_state_cn：在总效应之外增加处理接触程度的维度。

- sets_up_next_cn：接下来用2SLS估计ATT并比较合规者/不合规者。

- failure_if_removed_cn：无法解释为何效应主要由点击者驱动，机制解释减弱。

- evidence_pointer：Section 5.2 P2

### 11. Results 5.2 closure

- order：11

- locator：Results 5.2 closure

- paraphrase_cn：总结：推荐系统提高转化率、订单金额、考虑集规模和卷入深度，效应完全由点击并查看推荐的访问者驱动；下一节将检验是否被两个中介变量传递。

- move_code：CLOSURE总效应总结+过渡

- statement_status：empirical_result

- why_here_cn：收束总效应和ATT分析，并预告下一步因果中介分析。

- inherits_from_previous_cn：基于Table 6和Table 7。

- changes_argument_state_cn：稳定总效应结论，把问题转向'为什么'。

- sets_up_next_cn：直接引出Section 5.3因果中介方法。

- failure_if_removed_cn：总效应与中介分析之间断裂。

- evidence_pointer：Section 5.2结尾

### 12. Results 5.3 opening

- order：12

- locator：Results 5.3 opening

- paraphrase_cn：中介分析是重要的实证任务，已从Baron-Kenny发展到Zhao改进再到反事实因果框架；本文采用后者以求清晰因果解释。

- move_code：OPENING方法引入

- statement_status：method_decision

- why_here_cn：在报告中介结果前为方法选择提供文献背景。

- inherits_from_previous_cn：承接总效应存在但机制未知的状态。

- changes_argument_state_cn：引入NDE/NIE作为核心分解工具。

- sets_up_next_cn：随后写出中介方程和结果方程。

- failure_if_removed_cn：NDE/NIE结果无法被理解，方法贡献也失去依据。

- evidence_pointer：Section 5.3 P1

### 13. Single mediator set size opening

- order：13

- locator：Single mediator set size opening

- paraphrase_cn：先以lnSetSize为单一中介、以Order为结果变量；由于事前不清楚处理与中介是否交互，按因果中介最佳实践在结果方程加入暴露-中介交互项。

- move_code：OPENING单中介设置

- statement_status：method_decision

- why_here_cn：明确第一个中介、结果变量和分析规范，说明与经典Baron-Kenny的差异。

- inherits_from_previous_cn：承接因果中介框架。

- changes_argument_state_cn：定义第一个正式机制检验。

- sets_up_next_cn：报告Table 8的两步回归结果。

- failure_if_removed_cn：第一个中介检验没有明确设置，无法解释后续数字。

- evidence_pointer：Section 5.3.1 P1-P2

### 14. Single mediator set size closure

- order：14

- locator：Single mediator set size closure

- paraphrase_cn：稳健性检查：将lnViewsPerItem作为潜在中介-结果混淆纳入后结果相似；因此通过考虑集规模的中介结论大体稳健。

- move_code：CLOSURE稳健性总结

- statement_status：empirical_result

- why_here_cn：在转向下一中介前，用控制另一个中介的检验增强当前结论。

- inherits_from_previous_cn：基于Table 8第3-4列和Table 9第二行。

- changes_argument_state_cn：加固广度路径的稳健性。

- sets_up_next_cn：下一节转入深度路径。

- failure_if_removed_cn：广度结论易受'深度是混淆'的批评。

- evidence_pointer：Section 5.3.1结尾, Table 8, Table 9

### 15. Single mediator depth opening

- order：15

- locator：Single mediator depth opening

- paraphrase_cn：现在研究卷入深度（lnViewsPerItem）是否也中介推荐系统效应，同样加入暴露-中介交互。

- move_code：OPENING第二中介

- statement_status：method_decision

- why_here_cn：与广度检验对称，确定第二个中介和分析规范。

- inherits_from_previous_cn：承接广度检验完成后的下一步。

- changes_argument_state_cn：定义第二个机制检验。

- sets_up_next_cn：报告Table 10和Table 11结果。

- failure_if_removed_cn：深度路径悬空，双中介模型无法构建。

- evidence_pointer：Section 5.3.2 P1-P2

### 16. Single mediator depth closure

- order：16

- locator：Single mediator depth closure

- paraphrase_cn：将lnSetSize作为潜在混淆后，NIE仍显著但NDE变为不显著，中介类型变为间接-only，占比9.32%。

- move_code：CLOSURE稳健性总结

- statement_status：empirical_result

- why_here_cn：收束深度检验，并指出控制广度后直接效应消失，说明广度吸收较多路径。

- inherits_from_previous_cn：基于Table 11第二行。

- changes_argument_state_cn：深度路径被确认但更脆弱，为路径比较作铺垫。

- sets_up_next_cn：下一节进入双中介分析。

- failure_if_removed_cn：深度路径的稳健性与相对地位不明。

- evidence_pointer：Section 5.3.2结尾, Table 11

### 17. Two-mediator analysis opening

- order：17

- locator：Two-mediator analysis opening

- paraphrase_cn：单中介结果显示通过lnSetSize的效应（25.7%）远大于通过lnViewsPerItem的效应（10.2%），因此将两者同时作为中介进行多重中介分析。

- move_code：OPENING双中介

- statement_status：empirical_result

- why_here_cn：在比较单中介结果后，用双中介模型得到合计中介比例。

- inherits_from_previous_cn：直接整合两个单中介分析的结果。

- changes_argument_state_cn：从两条独立路径升级为联合机制图景。

- sets_up_next_cn：报告合计39.2%和间接-only结论。

- failure_if_removed_cn：没有合计中介比例，机制总力度无法陈述。

- evidence_pointer：Section 5.3.3 P1

### 18. Two-mediator closure / transition to discussion

- order：18

- locator：Two-mediator closure / transition to discussion

- paraphrase_cn：两个中介共中介约39.2%的总效应，直接效应不显著，属间接-only。

- move_code：CLOSURE证据收束

- statement_status：empirical_result

- why_here_cn：以机制分解的总数字结束结果章节，为讨论部分提供最终证据。

- inherits_from_previous_cn：多重中介分析输出。

- changes_argument_state_cn：把证据链完整闭合。

- sets_up_next_cn：下一节讨论中把结果回接到理论争议与实践启示。

- failure_if_removed_cn：结果章节没有总结性数字，讨论部分显得悬空。

- evidence_pointer：Section 5.3.3 P1

## 讨论与贡献逐句图谱

### 1. Discussion 6.1 P1 S1

- order：1

- locator：Discussion 6.1 P1 S1

- paraphrase_cn：首先，先前现场研究假设推荐系统降低搜索成本但未深入检验；本文理论化并提出考虑集广度和深度两条路径，发现支持这些中介关系。

- move_code：THEORY_RETURN

- statement_status：contribution_claim

- why_here_cn：讨论第一点把结果放回搜索成本假设，解释本文如何把假设变成检验对象。

- inherits_from_previous_cn：基于中介结果和引言中的缺口。

- changes_argument_state_cn：从结果陈述转为理论贡献判定。

- sets_up_next_cn：下一段进入考虑集规模争论。

- failure_if_removed_cn：与引言缺口的闭环断裂，贡献失去起点。

- evidence_pointer：Discussion 6.1 P1

### 2. Discussion 6.1 P2 S1

- order：2

- locator：Discussion 6.1 P2 S1

- paraphrase_cn：其次，关于推荐系统增大还是减小考虑集存在争论；作者用现场证据支持CF扩大了考虑集，并给出与Haubl实验室结果不一致的三种可能解释：算法类型不同、实验室启动效应、推荐准确度。

- move_code：THEORY_RETURN争论裁决

- statement_status：author_inference

- why_here_cn：把现场证据直接放入既有理论对立中，并解释差异来源。

- inherits_from_previous_cn：联系理论部分Section 3.1的争论。

- changes_argument_state_cn：把经验发现转化为对理论预测的选择和调和。

- sets_up_next_cn：下一段转向深度维度研究缺口的贡献。

- failure_if_removed_cn：考虑集争论的贡献没有落点。

- evidence_pointer：Discussion 6.1 P2

### 3. Discussion 6.1 P3 S1

- order：3

- locator：Discussion 6.1 P3 S1

- paraphrase_cn：第三，先前研究用总卷入难以区分卷入与数量，存在机械正相关；本文用每备选项卷入提供更细粒度视角，并发现深度确实中介且弱于广度。

- move_code：CONTRIBUTION构念细分

- statement_status：contribution_claim

- why_here_cn：说明为何'每备选项卷入'比'总卷入'更有分析价值。

- inherits_from_previous_cn：基于深度操作化和中介结果。

- changes_argument_state_cn：从经验发现升级为构念测量学贡献。

- sets_up_next_cn：下一段从决策启发式理论解释广度与深度并存。

- failure_if_removed_cn：深度测度的贡献不显，测量合法性受质疑。

- evidence_pointer：Discussion 6.1 P3

### 4. Discussion 6.1 P4 S1

- order：4

- locator：Discussion 6.1 P4 S1

- paraphrase_cn：最后，消费者用非补偿性启发式形成考虑集、用补偿性启发式比较备选；推荐系统同时促进两类启发式使用，因为结果显示既看更多产品又更深入评估平均备选项。

- move_code：THEORY_RETURN启发式

- statement_status：author_inference

- why_here_cn：用决策启发式理论解释为什么广度与深度同时增加在认知上是合理的。

- inherits_from_previous_cn：基于两个中介同时显著的经验事实。

- changes_argument_state_cn：把机制发现提升到认知理论层面。

- sets_up_next_cn：下一节转向实践含义。

- failure_if_removed_cn：机制发现缺少理论深度，讨论停留在结果重述。

- evidence_pointer：Discussion 6.1 P4

### 5. Discussion 6.2 P1 S1

- order：5

- locator：Discussion 6.2 P1 S1

- paraphrase_cn：实践含义一：在线零售商可按预测偏好接近度降序显示推荐，并标注接近度分数，以帮助消费者快速筛选并加入考虑集。

- move_code：CONTRIBUTION实践

- statement_status：author_inference

- why_here_cn：把'考虑集形成起作用'转换为可操作的设计建议。

- inherits_from_previous_cn：基于广度路径中有效的机制。

- changes_argument_state_cn：从机制证据转到设计处方。

- sets_up_next_cn：下一句继续实践建议（比较工具）。

- failure_if_removed_cn：实践贡献缺少具体抓手。

- evidence_pointer：Discussion 6.2 P1

### 6. Discussion 6.2 P2 S1

- order：6

- locator：Discussion 6.2 P2 S1

- paraphrase_cn：实践含义二：考虑集扩大能诱发购买，但过大可能难管理；建议提供保存备选项和比较矩阵等工具帮助比较。

- move_code：CONTRIBUTION实践

- statement_status：author_inference

- why_here_cn：把信息过载这一边界与设计工具联系起来。

- inherits_from_previous_cn：基于广度与深度中介和过载文献。

- changes_argument_state_cn：把机制结果转化为工具设计方向。

- sets_up_next_cn：下一句讨论顾客旅程设计的哲学。

- failure_if_removed_cn：深度路径的实践转化缺失。

- evidence_pointer：Discussion 6.2 P2

### 7. Discussion 6.2 P3 S1

- order：7

- locator：Discussion 6.2 P3 S1

- paraphrase_cn：实践含义三：在线商店设计中的主流观点是'尽可能精简便利'，但结果显示有意义的顾客旅程延长可通过扩大考虑集规模和深度提高购买概率。

- move_code：CONTRIBUTION设计哲学

- statement_status：author_inference

- why_here_cn：用中介结果挑战'越简短越好'的商店设计原则。

- inherits_from_previous_cn：综合广度和深度结果。

- changes_argument_state_cn：把机制发现上升为设计理念修正。

- sets_up_next_cn：下一节列出局限。

- failure_if_removed_cn：实践贡献缺乏与主流观点对比，力度下降。

- evidence_pointer：Discussion 6.2 P3

### 8. Discussion 6.3 P1 S1

- order：8

- locator：Discussion 6.3 P1 S1

- paraphrase_cn：局限一：现有现场研究都用无推荐作控制、真实零售商难以部署随机或无关推荐；因此估计效应是组合效应，包含单纯展示的表层效应；虽然试点显示随机推荐与无推荐相似，但现场没有分离表层效应。

- move_code：LIMITATION边界声明

- statement_status：author_inference

- why_here_cn：诚实声明估计效应的边界，防止读者把组合效应误读为纯推荐效果。

- inherits_from_previous_cn：承接现场实验控制条件选择和试点结果。

- changes_argument_state_cn：给效应解释设置边界。

- sets_up_next_cn：下一句讨论未用的bestselling控制。

- failure_if_removed_cn：表层效应问题未声明，全文的核心解释易受攻击。

- evidence_pointer：Discussion 6.3 P1

### 9. Discussion 6.3 P2 S1

- order：9

- locator：Discussion 6.3 P2 S1

- paraphrase_cn：局限二：作者也未用bestselling推荐作为替代控制条件，可能与任何典型CF一样倾向于推荐流行产品；未来可比较个性化CF与非个性化bestselling。

- move_code：LIMITATION未来研究

- statement_status：author_inference

- why_here_cn：说明未选择一种重要的替代基线，并指出未来方向。

- inherits_from_previous_cn：承接现场实验控制选择。

- changes_argument_state_cn：划定个性化推荐效果的边界。

- sets_up_next_cn：下一句讨论算法类型可推广性。

- failure_if_removed_cn：非个性化基准缺失的局限未被承认。

- evidence_pointer：Discussion 6.3 P2

### 10. Discussion 6.3 P3 S1

- order：10

- locator：Discussion 6.3 P3 S1

- paraphrase_cn：局限三：记忆型CF虽常用，但还存在模型型CF、内容型CF、混合和深度学习推荐；结论能否推广到其他类型尚不清楚。

- move_code：LIMITATION算法边界

- statement_status：author_inference

- why_here_cn：对算法选择作边界声明，限制机制结论的普适性。

- inherits_from_previous_cn：承接现场实验的算法选择。

- changes_argument_state_cn：把结论限定在记忆型CF。

- sets_up_next_cn：下一句讨论产品类别局限。

- failure_if_removed_cn：读者可能误以为结论适用所有推荐算法。

- evidence_pointer：Discussion 6.3 P3

### 11. Discussion 6.3 P4 S1

- order：11

- locator：Discussion 6.3 P4 S1

- paraphrase_cn：局限四：考虑集可能因产品类型而不同；合作书店只售图书，无法探索不同产品类别的异质性。

- move_code：LIMITATION产品边界

- statement_status：author_inference

- why_here_cn：承认单一产品类别的限制，并给出具体的未来产品类型研究。

- inherits_from_previous_cn：承接现场实验的单一类别。

- changes_argument_state_cn：把外部效度边界明确到产品类别。

- sets_up_next_cn：全文在局限与未来研究处收束。

- failure_if_removed_cn：外部效度问题未处理，讨论不完整。

- evidence_pointer：Discussion 6.3 P4

## Study累积逻辑

### 1. 1

- study_or_phase：Pilot Study 1（推荐类型选择）

- evidence_job_cn：在受控实验室环境中证明CF推荐优于无推荐和随机推荐，并判断无推荐可作为合理控制条件。

- what_it_establishes_cn：建立现场实验的基线选择：无推荐是合理控制，随机展示产品不能提高购买，CF效果不只来自表层可见性。

- what_it_cannot_establish_cn：不能建立真实平台上的效应；不能确定处理组应展示多少条推荐；样本为学生、产品单一。

- why_next_phase_is_needed_cn：确定了'用哪个控制'之后，还需确定'展示几条推荐'才能设计现场实验。

- transition_wording_function_cn：从'无推荐是合理基线'过渡到'还需决定处理组推荐数量'。

### 2. 2

- study_or_phase：Pilot Study 2（推荐数量选择）

- evidence_job_cn：在实验室中寻找推荐数量与购买效果的关系，为现场实验确定处理强度。

- what_it_establishes_cn：建立n=3作为处理组推荐条数；建立推荐数量与购买效果的倒U形形状。

- what_it_cannot_establish_cn：不能证明三条在真实平台最优；不能建立任何机制或因果关系之外的平台效果。

- why_next_phase_is_needed_cn：两个设计参数确定后，必须回到真实平台检验理论模型。

- transition_wording_function_cn：从'设计参数确定'转向'真实在线书店中的随机现场实验'。

### 3. 3

- study_or_phase：随机现场实验（总效应与ATT）

- evidence_job_cn：在真实在线书店用随机分配建立推荐系统的因果总效应，并区分合规者与不合规者。

- what_it_establishes_cn：推荐系统提高购买倾向12.4%、订单金额1.7%、考虑集规模3.2%、卷入深度0.9%；效应主要由点击推荐的访问者驱动；随机化平衡有效。

- what_it_cannot_establish_cn：总效应不能说明机制；ITT可能被不合规者稀释；不能回答'为什么'。

- why_next_phase_is_needed_cn：总效应和中介变量变化不足以证明中介传递，必须用因果中介分析分解路径。

- transition_wording_function_cn：用'在下一节我们将检验正效应是否通过考虑集规模和卷入程度被中介'作显式过渡。

### 4. 4

- study_or_phase：单中介分析：考虑集规模

- evidence_job_cn：检验广度是否为推荐系统到购买的真实因果中介路径。

- what_it_establishes_cn：NIE优势比1.029显著，25.7%总效应被中介；直接效应不显著，属indirect-only；敏感性阈值ρ>0.30且控制深度后结果相似。

- what_it_cannot_establish_cn：不能排除深度作为同时存在的另一条路径；顺序可忽略性不可检验。

- why_next_phase_is_needed_cn：既然深度也可能是路径且对广度构成潜在混淆，需要单独检验深度并比较路径强度。

- transition_wording_function_cn：以'现在研究卷入程度是否也中介'开启第二单中介分析。

### 5. 5

- study_or_phase：单中介分析：卷入深度

- evidence_job_cn：检验深度是否为第二条独立的中介路径。

- what_it_establishes_cn：NIE优势比1.011显著，10.2%总效应被中介；单独时NDE显著为互补中介，控制广度后变为indirect-only，占比9.32%。

- what_it_cannot_establish_cn：深度路径较脆弱；不能说明两条路径合起来解释多少效应。

- why_next_phase_is_needed_cn：分别检验完后，需要双中介模型给出合计解释力和路径比较。

- transition_wording_function_cn：用单中介结果的比较（25.7% vs 10.2%）引出双中介分析。

### 6. 6

- study_or_phase：双中介分析

- evidence_job_cn：同时纳入两个中介，量化总中介比例并比较两条路径的相对贡献。

- what_it_establishes_cn：两中介合计中介39.2%总效应；直接效应不显著，属indirect-only；广度份额明显大于深度。

- what_it_cannot_establish_cn：不能解释剩余约60%总效应；不能建模两个中介之间的顺序或相关性；不能直接检验未观测混淆。

- why_next_phase_is_needed_cn：证据链完成后需要把机制结论转化为理论、实践贡献和边界条件。

- transition_wording_function_cn：从证据收束自然过渡到讨论部分的理论回接。

## 主张—证据台账

### 1. CF推荐相比无推荐和随机推荐更能提高购买（实验室）。

- claim_cn：CF推荐相比无推荐和随机推荐更能提高购买（实验室）。

- claim_level：technical

- supporting_evidence_cn：Pilot Study 1中无推荐与随机推荐系数显著为负且相似（-14.59, -14.60）。

- support_strength：direct

- where_claim_is_made：Introduction P6 S2; Section 4.1.1 P6

- where_evidence_is_provided：Section 4.1.1, Table 2

### 2. 展示三条推荐比展示一条或五条更有效，效果与条数呈倒U形。

- claim_cn：展示三条推荐比展示一条或五条更有效，效果与条数呈倒U形。

- claim_level：technical

- supporting_evidence_cn：Pilot Study 2中n=3系数10.48显著且显著大于n=1和n=5。

- support_strength：direct

- where_claim_is_made：Introduction P6 S2; Section 4.1.2 P3

- where_evidence_is_provided：Section 4.1.2, Table 3

### 3. 推荐系统提高购买倾向和订单金额（现场）。

- claim_cn：推荐系统提高购买倾向和订单金额（现场）。

- claim_level：technical

- supporting_evidence_cn：ITT：Order优势比变化12.4%，lnOrderVal +1.7%，均显著。

- support_strength：direct

- where_claim_is_made：Introduction P7 S1; Section 5.2

- where_evidence_is_provided：Section 5.2, Table 6

### 4. 推荐系统提高考虑集规模和每备选项卷入深度。

- claim_cn：推荐系统提高考虑集规模和每备选项卷入深度。

- claim_level：mechanism

- supporting_evidence_cn：ITT：lnSetSize +3.2%、lnViewsPerItem +0.9%，均显著；描述统计表5亦显示处理组更高。

- support_strength：direct

- where_claim_is_made：Introduction P7 S1; Section 5.1

- where_evidence_is_provided：Section 5.1 Table 5; Section 5.2 Table 6

### 5. 效应由点击并查看推荐的访问者驱动，仅暴露不点击者几乎没有效应。

- claim_cn：效应由点击并查看推荐的访问者驱动，仅暴露不点击者几乎没有效应。

- claim_level：mechanism

- supporting_evidence_cn：合规者ATT全部显著且远大于ITT；不合规者各项效应不显著（Table 7）。

- support_strength：direct

- where_claim_is_made：Introduction P7 S2; Section 5.2 P2-P3

- where_evidence_is_provided：Section 5.2, Table 7

### 6. 考虑集规模中介推荐系统对购买的影响。

- claim_cn：考虑集规模中介推荐系统对购买的影响。

- claim_level：mechanism

- supporting_evidence_cn：NIE优势比1.029显著，NDE不显著，25.7%被中介；敏感性阈值ρ>0.30；控制lnViewsPerItem后结果相似。

- support_strength：direct

- where_claim_is_made：Introduction P7 S3; Section 5.3.1

- where_evidence_is_provided：Section 5.3.1, Table 8, Table 9, Figure 3

### 7. 卷入深度也中介推荐系统对购买的影响。

- claim_cn：卷入深度也中介推荐系统对购买的影响。

- claim_level：mechanism

- supporting_evidence_cn：NIE优势比1.011显著，单独时NDE也显著，10.2%被中介；敏感性ρ≈0.20；控制lnSetSize后NIE仍显著，占比9.32%。

- support_strength：direct

- where_claim_is_made：Introduction P7 S3; Section 5.3.2

- where_evidence_is_provided：Section 5.3.2, Table 10, Table 11

### 8. 广度比深度中介更大比例的效应。

- claim_cn：广度比深度中介更大比例的效应。

- claim_level：mechanism

- supporting_evidence_cn：广度25.7% vs 深度10.2%（单中介）；双中介合计39.2%。

- support_strength：partial

- where_claim_is_made：Abstract S8; Introduction P7 S3; Section 5.3.3

- where_evidence_is_provided：Section 5.3.3; 但未正式报告两比例差异的统计检验，正文以点估计和显著性描述

### 9. 推荐系统通过扩大考虑集并提高每备选项卷入来传导正面效应，直接效应不显著，属完全/间接-only中介。

- claim_cn：推荐系统通过扩大考虑集并提高每备选项卷入来传导正面效应，直接效应不显著，属完全/间接-only中介。

- claim_level：theory

- supporting_evidence_cn：双中介分析显示合计39.2%被中介，NDE不显著。

- support_strength：partial

- where_claim_is_made：Abstract; Introduction P7 S3; Discussion 6.1

- where_evidence_is_provided：Section 5.3.3; 剩余约60%总效应未被解释，'完全中介'依赖NDE不显著而非效应为零

### 10. 本文提供第一个现场实验证据支持推荐系统增大考虑集并提高转化率。

- claim_cn：本文提供第一个现场实验证据支持推荐系统增大考虑集并提高转化率。

- claim_level：boundary/design_knowledge

- supporting_evidence_cn：现场ITT和中介分析中lnSetSize +3.2%、NIE显著。

- support_strength：partial

- where_claim_is_made：Introduction P8 S2; Discussion 6.1 P2

- where_evidence_is_provided：Section 5.2 Table 6; Section 5.3.1; '第一'声明依赖作者对文献覆盖的评估

### 11. 因果中介方法在IS文献中很少使用，本文较早采用。

- claim_cn：因果中介方法在IS文献中很少使用，本文较早采用。

- claim_level：theory

- supporting_evidence_cn：引用Peng (2019)说明IS关注不足，并以上下文综述为支撑。

- support_strength：asserted

- where_claim_is_made：Introduction P8 S3; Section 5.3 P1

- where_evidence_is_provided：同一位置；无系统文献计量证据

## ISR定位逻辑

- constitutive_is_problem_cn：本文把推荐系统既当作数字技术制成品、也当作改变消费者搜索与决策过程的信息干预，回答'技术如何通过改变考虑集进而改变购买'这一IS式机制问题，而不是单纯报告性能提升。

- technology_behavior_or_market_entanglement_cn：推荐系统降低搜索成本这一技术属性与消费者考虑集形成、卷入承诺等行为机制互相构成：技术特性（CF匹配、推荐条数、位置）通过行为路径（广度、深度）传导经济结果。

- role_of_benchmark_or_objective_evidence_cn：随机推荐和无推荐对照、ITT/ATT、NDE/NIE不是用来比拼算法分数，而是分别用于排除表层效应、区分暴露与使用、分解直接与间接因果路径，从而支持'机制如何起作用'的IS主张。

- theory_in_design_cn：考虑-然后-选择理论和卷入-承诺模型进入设计：理论决定了中介变量的选择（广度、深度）、测量方式（会话内独特书数、每书平均浏览数）和统计模型（双中介），而不只是事后解释结果；但具体推荐算法与条数主要由试点实验和业界实践决定。

- technical_vs_is_contribution_balance_cn：技术细节（CF算法、Slope-One、3条推荐）被压缩为可复制的背景，正文主要篇幅用于机制理论、中介方法、结果和讨论；技术与行为贡献按'设计参数来自试点、机制贡献来自现场中介'分工，没有让技术性能喧宾夺主。

- beyond_transient_performance_cn：本文通过把效应分解为考虑集广度与深度两条可复用路径、并作敏感性分析，将一次性现场效应转化为关于'推荐系统如何改变考虑集→购买'的机制认知；因此即使12.4%等数字只在特定书店成立，路径结构和测量方案仍可迁移。

## 段落级仿写模板

### abstract_steps

1. 第一句用研究问题或直接缺口开启，点名字面问题。

2. 第二句声明现有研究忽视因果路径。

3. 第三句交代研究设计与方法。

4. 第四句先报总效应，作为机制可分解的基线。

5. 第五句用'更重要的是'引入机制中介主张。

6. 第六、七句把机制拆成两个维度并完成链条。

7. 第八句比较两条路径贡献，给出最具辨识度的结论。

### introduction_paragraph_steps

1. 第一段定义并收窄研究对象，用知名企业例证普适性。

2. 第二段讲目标与商业重要性，指出早期研究局限。

3. 第三段总结近期现场共识，随即指出共识中的未检验假设，正式声明缺口。

4. 第四段引入理论构念，用具体文献实例把缺口具体化。

5. 第五段从机制前提推出两个维度并建立研究模型。

6. 第六段预告研究设计和试点依据，说明关键参数。

7. 第七段按总效应→异质性→中介结果三层报告核心发现。

8. 第八段把发现翻译为四条文献贡献。

### theory_to_design_steps

1. 引入成熟构念并综述决策过程理论。

2. 强调维度可并行，为同步中介建模提供依据。

3. 为每个维度设置对立理论预测并引用实验室证据。

4. 把方向问题标为经验问题，说明需要现场数据。

5. 为每一维度提供从构念到购买的理论桥梁。

6. 在中介模型明确后，转入实验设计并确保设计选择有试点证据。

### method_and_study_sequence_steps

1. 先列出现场实验的关键设计参数。

2. 用试点实验依次决定每一参数，并在每步报告证据。

3. 在进入现场实验前确认真实平台、干预物和测量。

4. 用描述统计与平衡性检验先行验证随机化和方向。

5. 先报告ITT，再用合规者/不合规者和2SLS估计ATT。

6. 在报告中介前先用一段说明方法选择和与经典方法的差异。

7. 按单一中介一、单一中介二、双中介的顺序铺开，每步都加敏感性检验。

### results_reporting_steps

1. 先用Table报告描述统计和组间比较。

2. 报告ITT效应并给出百分比解释，与已有研究比较量级。

3. 通过合规者分类和ATT说明效应来源。

4. 引入因果中介方法，给出中介方程和结果方程。

5. 对每个中介报告NIE/NDE、置信区间、中介类型和百分比。

6. 用敏感性分析（ρ和R²乘积）说明结论对违假定有多稳健。

7. 用控制另一个中介作为潜在混淆作稳健性检验。

8. 最后给出双中介合计比例与路径比较。

### discussion_and_contribution_steps

1. 第一点把结果放回文献假设，说明理论贡献。

2. 第二点把结果放入既有理论对立，解释差异来源。

3. 第三点提出构念测量层面的贡献并比较路径强弱。

4. 第四点用更抽象的理论（如启发式）重述机制意义。

5. 实践部分依次给出界面设计、辅助工具、顾客旅程设计建议。

6. 局限部分依次声明控制条件、算法类型、产品类别等边界。

7. 以未来研究路径收束。

## 可执行写作算法

### 1. 1

- step：1

- rhetorical_job_cn：在引言建立研究对象的技术定义并收窄为个性化推荐。

- research_evidence_required_cn：需要一篇权威定义和至少一个知名企业实例（如Amazon）。

- sentence_pattern_function_cn：用'推荐系统是……（定义）；本文聚焦……（收窄）；推荐系统在……普遍存在（例证）'三句完成开场。

- transition_condition_cn：当读者明确研究对象和边界后进入下一步。

### 2. 2

- step：2

- rhetorical_job_cn：构造研究缺口：先承认共识，再指出共识中的未检验假设。

- research_evidence_required_cn：需要若干现场研究支持'总效应有共识'，并有一个只猜测未检验的具体文献线索（如De et al. 2010）。

- sentence_pattern_function_cn：用'近期研究……存在共识（枚举文献）；然而先前研究假设……却未检验……尤其未探索因果路径和中介因素'句式。

- transition_condition_cn：当缺口从泛泛'机制不明'收窄到一个具体构念后可进入theory引入。

### 3. 3

- step：3

- rhetorical_job_cn：引入理论构念并分解为两个可检验维度。

- research_evidence_required_cn：需要营销/IS中关于该构念的成熟文献，以及每个维度能形成对立预测的文献。

- sentence_pattern_function_cn：用'我们提出……起重要作用；基于……决策过程，区分两个维度：广度…与深度…；图1展示模型'句式。

- transition_condition_cn：当每个维度都成为经验问题且有理论桥梁后进入设计。

### 4. 4

- step：4

- rhetorical_job_cn：用试点实验为现场实验的设计参数提供经验依据。

- research_evidence_required_cn：需要能够比较控制条件和处理强度的实验室数据，至少回答两个设计问题。

- sentence_pattern_function_cn：用'现场实验有两个关键设计选择……为确定它们，我们进行两个试点实验；试点1结果……因此选择……；试点2结果……因此选择……'句式。

- transition_condition_cn：当每个参数都有试点证据支持且边界被声明后进入现场实验。

### 5. 5

- step：5

- rhetorical_job_cn：报告现场实验设计并先建立总效应证据。

- research_evidence_required_cn：需要真实平台上的随机化、处理/控制干预和会话级行为数据。

- sentence_pattern_function_cn：用'实验单位为……；处理随机分配……；我们估计……结果发现……（表）'句式，并比较合规者与不合规者。

- transition_condition_cn：当总效应和中介变量变化都显著且效应来源明确后进入中介分析。

### 6. 6

- step：6

- rhetorical_job_cn：介绍因果中介方法并指出其相对经典方法的改进。

- research_evidence_required_cn：需要反事实中介框架的方法论文献，以及中介和结果方程。

- sentence_pattern_function_cn：用'中介分析……经历了……；本文采用反事实框架……我们估计两个方程……NDE测量……NIE测量……'句式。

- transition_condition_cn：当读者理解NDE/NIE定义后进入单中介结果。

### 7. 7

- step：7

- rhetorical_job_cn：依次检验单一中介，每个中介报告NIE/NDE、敏感性分析、控制另一中介的稳健性。

- research_evidence_required_cn：需要两个候选中介变量的测量、两步回归结果、bootstrap置信区间和敏感性参数。

- sentence_pattern_function_cn：用'先以M为单一中介并加入暴露-中介交互……NIE=…显著，NDE=…；敏感性分析显示ρ需大于…才使效应消失；将另一中介作为潜在混淆后结果相似'句式。

- transition_condition_cn：当两个单中介都完成且彼此比较明确后进入双中介。

### 8. 8

- step：8

- rhetorical_job_cn：用双中介模型给出合计中介比例和路径比较。

- research_evidence_required_cn：需要同时纳入两个中介的多重中介分析结果。

- sentence_pattern_function_cn：用'单中介结果显示A比B更大，因此我们同时纳入两者……合计中介……%总效应，直接效应不显著，属间接-only'句式。

- transition_condition_cn：当机制份额数据稳定后进入讨论。

### 9. 9

- step：9

- rhetorical_job_cn：在讨论中依次完成结果回接理论、理论贡献、实践贡献和局限。

- research_evidence_required_cn：需要能够把每个贡献对应到文献中的具体缺口，并知道哪些边界的证据未覆盖。

- sentence_pattern_function_cn：用'首先……填补某假设未检验的缺口；第二……在既有争论中提供现场证据并解释差异；第三……提出测量/构念贡献；实践上……；最后局限……未来研究……'句式。

- transition_condition_cn：当贡献逐条对应引言缺口且局限诚实列出后结束全文。

## 应模仿的高价值动作

1. 用'总效应有共识但机制未检验'构造核心缺口，并给出一个'只猜测未检验'的具体文献作为靶子。

2. 用一个理论构念把模糊的'降低搜索成本'假设转化为两个可检验、可操作的中介维度。

3. 理论部分为每个维度设置对称的对立预测，把方向问题标为经验问题，让现场证据成为裁决者。

4. 用两个小规模试点实验为现场实验的两个关键参数提供证据基础，并主动声明参数不普适。

5. 在一篇以现场实验为主的论文中，先报告ITT再报告2SLS估计的ATT，并用合规者/不合规者说明效应来源。

6. 在中介分析中引入暴露-中介交互项，严格区分与经典Baron-Kenny方法的差异。

7. 用敏感性分析（ρ阈值和R²乘积）把不可检验的顺序可忽略性转换为可量化稳健性。

8. 在单一中介检验中把另一个中介作为潜在混淆纳入，用对称方式加固两条路径结论。

9. 讨论部分把结果放回两个对立理论位置并给出差异来源的多种解释，而不只是重述结果。

10. 实践贡献把机制结果翻译为界面排序、比较矩阵、顾客旅程延长三大可操作建议。

## 不要只复制的表面动作

1. 不要在没有现场随机实验和中介数据的情况下直接声称'效应由考虑集中介'。

2. 不要只报告中介百分比而不报告NIE/NDE置信区间和敏感性分析。

3. 不要把浏览行为直接等同于心理考虑集而不引用操作化文献和讨论代理假设。

4. 不要把无推荐控制下的效应解释为纯个性化推荐效果，必须承认组合效应/表层效应。

5. 不要仅凭一个现场的百分比差异宣称'广度显著大于深度'，需要说明统计检验或明确承认点估计。

6. 不要把'三条推荐最优'当作可推广事实，需要限定试点情境。

## 证据薄弱或跳跃的动作

1. '完全中介/间接-only'的表述：双中介后NDE不显著，但仍有约60%总效应未被两个中介解释，'完全'只能是统计术语层面的间接-only，不能解释为全部机制。

2. 广度与深度中介比例的比较：正文以点估计差异（25.7% vs 10.2%）作结论，未报告两比例差异的统计检验。

3. 将每备选项页面浏览数视为卷入深度的代理：浏览数与认知卷入之间存在概念跳跃，正文仅以页面浏览数替代，虽在脚注提供时间替代，但未直接测量心理卷入。

4. '第一个现场证据支持考虑集扩大'的声明：依赖作者对文献覆盖范围的评估，未见系统排除所有现场研究的证据。

5. '因果中介方法在IS中很少使用'的断言：仅引用Peng (2019)一个来源，未提供系统文献计量证据。

6. 双中介模型未建模两个中介之间的顺序或相关结构，存在路径间关系的未检验假设。

## 一句话套路

先找领域共识里的未检验假设，用一个成熟理论构念把模糊机制拆成两个对立可检验维度，用试点实验确定现场实验参数，用真实平台随机实验证明总效应并用因果中介加敏感性分析证明路径效应，最后把路径强弱转化为文献争论的裁决和可复用设计知识。

## 分析边界

分析基于OCR全文，无法阅读在线附录A-D、图表原始版式及Figure 3细节；正文只完整展示以Order为结果变量的中介结果，lnOrderVal等结果以脚注说明未展示；双中介模型中两个中介的顺序和相关性未被建模；'第一次/较早'类声明依赖作者文献覆盖，无法独立核实。
