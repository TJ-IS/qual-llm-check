# 1 + 1 > 2? Information, Humans, and Machines：ISR 句段级微观图谱

- 作者：Tian Lu; Yingjie Zhang
- 年份：2025
- DOI：10.1287/isre.2023.0305
- 源文件：26584_2025_1-1-2-information-humans-and-machines.md
- 置信度：0.87

## 核实后的宏观骨架

论文从人机协作普遍化但实际常因算法厌恶或过度依赖而低于预期这一现象出发，指出现有机器解释文献结论不一致，并以双加工理论提出两个必要条件：信息复杂度吸引注意、有用线索驱动深思，因而机器解释的有效性依赖于信息复杂度。作者与亚洲某小额贷款公司合作开展两阶段现场实验，同时操纵信息量（小/大）、是否看到机器建议、是否提供机器解释，先在Stage 1建立纯人类与纯机器基线，再在Stage 2用先独立决策后看机器建议再终决的两步协作流程分离人类增量贡献。核心经验结果是只有大信息量加机器解释同时满足时，人类参与才显著降低违约率；随后用三步机制分析打开人类重新思考及特征关联过程，再用经验异质性和性别公平性EOR扩展边界，最后在讨论中回到理论条件、给出管理与可推广性说明并列出局限。全文写作弧线为现象—机制—理论驱动设计—现场因果检验—机制分解—扩展—理论返回。

## 摘要逐句图谱

### 1. Abstract S1

- order：1

- locator：Abstract S1

- paraphrase_cn：数据爆炸和AI自动化使人类无论作为员工还是消费者都不可避免与机器密切协作。

- move_code：CONTEXT

- statement_status：fact

- why_here_cn：把研究置于AI时代大背景，建立普遍性。

- inherits_from_previous_cn：无。

- changes_argument_state_cn：确立问题域为人机协作。

- sets_up_next_cn：为下一句引出协作引发的问题作铺垫。

- failure_if_removed_cn：读者不知研究为何出现。

- evidence_pointer：Abstract S1

### 2. Abstract S2

- order：2

- locator：Abstract S2

- paraphrase_cn：人机交互问题随之产生，尤其要面对更大规模信息的处理困境。

- move_code：PROBLEM_FRAMING

- statement_status：author_inference

- why_here_cn：将背景收窄到信息处理难题。

- inherits_from_previous_cn：承接协作普遍化。

- changes_argument_state_cn：使机器信息处理优势成为问题切点。

- sets_up_next_cn：为比较机器优势与人类价值作引。

- failure_if_removed_cn：信息复杂度这一核心变量缺少入口。

- evidence_pointer：Abstract S2

### 3. Abstract S3

- order：3

- locator：Abstract S3

- paraphrase_cn：鉴于机器在信息处理上总体优于人类，必须探究人机协作是否有价值以及为何有价值。

- move_code：RESEARCH_QUESTION

- statement_status：author_inference

- why_here_cn：点出全文总问题（1+1>2?）。

- inherits_from_previous_cn：承接信息处理难题。

- changes_argument_state_cn：从背景进入研究问题。

- sets_up_next_cn：为讨论机器解释文献作铺垫。

- failure_if_removed_cn：摘要没有核心问题。

- evidence_pointer：Abstract S3

### 4. Abstract S4

- order：4

- locator：Abstract S4

- paraphrase_cn：近期研究提出多种解释方法打开机器学习黑箱，目标是减少人类抵抗并提高效率。

- move_code：PRIOR_WORK

- statement_status：prior_literature

- why_here_cn：引入机器解释这条文献线。

- inherits_from_previous_cn：是解决人类价值问题的一种途径。

- changes_argument_state_cn：把文献讨论聚焦到机器解释。

- sets_up_next_cn：为指出该文献结论不一致作对比。

- failure_if_removed_cn：后文理论贡献失去对象。

- evidence_pointer：Abstract S4

### 5. Abstract S5

- order：5

- locator：Abstract S5

- paraphrase_cn：然而这一文献流的发现尚无定论。

- move_code：GAP

- statement_status：author_inference

- why_here_cn：建立文献缺口。

- inherits_from_previous_cn：承接解释方法的实践。

- changes_argument_state_cn：说明需要一个能统一不一致结论的条件框架。

- sets_up_next_cn：为下一句‘影响因素未知’细化缺口。

- failure_if_removed_cn：贡献中‘解释不一致原因’失去依据。

- evidence_pointer：Abstract S5

### 6. Abstract S6

- order：6

- locator：Abstract S6

- paraphrase_cn：对影响机器解释效果的因素及其作用于人类决策过程的理由知之甚少。

- move_code：GAP_DETAIL

- statement_status：author_inference

- why_here_cn：进一步明确知识与机制缺口。

- inherits_from_previous_cn：承接结论不一致。

- changes_argument_state_cn：把缺口从‘是否有效’推进到‘条件和机制’。

- sets_up_next_cn：为研究目标（联合影响）作铺垫。

- failure_if_removed_cn：本文双条件贡献不再必要。

- evidence_pointer：Abstract S6

### 7. Abstract S7

- order：7

- locator：Abstract S7

- paraphrase_cn：本文研究信息复杂度与机器解释的联合影响。

- move_code：OBJECTIVE

- statement_status：author_inference

- why_here_cn：用一句话明确研究目标。

- inherits_from_previous_cn：回应缺口中的关键变量。

- changes_argument_state_cn：从问题进入目标。

- sets_up_next_cn：为方法句提供目标。

- failure_if_removed_cn：摘要无研究承诺。

- evidence_pointer：Abstract S7

### 8. Abstract S8

- order：8

- locator：Abstract S8

- paraphrase_cn：研究采用与亚洲某小额贷款公司合作的两阶段现场实验。

- move_code：METHOD_OVERVIEW

- statement_status：method_decision

- why_here_cn：说明证据来源是现场实验而非实验室。

- inherits_from_previous_cn：目标需要因果识别。

- changes_argument_state_cn：把研究从理论转为实证策略。

- sets_up_next_cn：为下一句理论驱动的实验操纵作铺垫。

- failure_if_removed_cn：方法可信度与生态效度不再成立。

- evidence_pointer：Abstract S8

### 9. Abstract S9

- order：9

- locator：Abstract S9

- paraphrase_cn：基于双加工理论，实验操纵信息复杂度、是否协作和是否提供机器解释。

- move_code：THEORY_TO_DESIGN

- statement_status：theory_claim

- why_here_cn：显示实验处理不是任意的，而是理论推导出来的。

- inherits_from_previous_cn：承接现场实验目标。

- changes_argument_state_cn：把理论条件映射为可操纵变量。

- sets_up_next_cn：为结果句提供处理组合。

- failure_if_removed_cn：双条件理论贡献失去设计基础。

- evidence_pointer：Abstract S9

### 10. Abstract S10

- order：10

- locator：Abstract S10

- paraphrase_cn：结果发现单独大信息量或单独机器解释都不能让人类为最终协作结果增加价值；只有大信息量与机器解释同时存在时，人类参与显著降低违约率。

- move_code：MAIN_RESULT

- statement_status：empirical_result

- why_here_cn：给出全文核心经验结果。

- inherits_from_previous_cn：由四种处理组合的比较而来。

- changes_argument_state_cn：证明两个条件缺一不可。

- sets_up_next_cn：为机制分析设置待解释现象。

- failure_if_removed_cn：摘要没有实质发现。

- evidence_pointer：Abstract S10; Table 2 比较J

### 11. Abstract S11

- order：11

- locator：Abstract S11

- paraphrase_cn：用三步实证分析解开底层机制。

- move_code：MECHANISM_METHOD

- statement_status：method_decision

- why_here_cn：预告结果后将打开黑箱。

- inherits_from_previous_cn：核心结果需要解释。

- changes_argument_state_cn：从结果升级到机制。

- sets_up_next_cn：为机制发现句铺垫。

- failure_if_removed_cn：贡献中的机制主张没有抓手。

- evidence_pointer：Abstract S11

### 12. Abstract S12

- order：12

- locator：Abstract S12

- paraphrase_cn：大信息量与机器解释并存能唤起人类主动重新思考，从而缩小性别差距并提高预测准确率。

- move_code：MECHANISM_RESULT

- statement_status：empirical_result

- why_here_cn：给出机制层面的总发现。

- inherits_from_previous_cn：三步分析的结论。

- changes_argument_state_cn：把绩效差异归因于重新思考。

- sets_up_next_cn：为具体联想机制作铺垫。

- failure_if_removed_cn：理论贡献失去核心机制。

- evidence_pointer：Abstract S12

### 13. Abstract S13

- order：13

- locator：Abstract S13

- paraphrase_cn：人类能自发把机器解释中新出现的特征与被忽略的其他特征关联，从而纠正机器错误。

- move_code：MECHANISM_SPECIFIC

- statement_status：empirical_result

- why_here_cn：给出最有新意的机制细节。

- inherits_from_previous_cn：是对主动再思考的具体化。

- changes_argument_state_cn：把人类贡献落地为可观察的特征关联。

- sets_up_next_cn：为贡献声明作铺垫。

- failure_if_removed_cn：‘人类独特价值’的主张失去独特证据。

- evidence_pointer：Abstract S13; Section 5.3

### 14. Abstract S14

- order：14

- locator：Abstract S14

- paraphrase_cn：这种能力既说明人机协作的必要性，也对系统设计有启示，兼具理论与实践意义。

- move_code：CONTRIBUTION

- statement_status：contribution_claim

- why_here_cn：用一句贡献声明收束摘要。

- inherits_from_previous_cn：机制发现的价值提升。

- changes_argument_state_cn：从结果转为贡献主张。

- sets_up_next_cn：无，摘要结束。

- failure_if_removed_cn：摘要缺少价值声明。

- evidence_pointer：Abstract S14

## 引言逐句图谱

### 1. Introduction P1 S1

- order：1

- locator：Introduction P1 S1

- paraphrase_cn：AI商业化与渗透使人类作为员工和消费者都开始与机器紧密协作。

- move_code：CONTEXT

- statement_status：fact

- why_here_cn：开篇建立时代背景，说明研究对象的普遍性。

- inherits_from_previous_cn：无。

- changes_argument_state_cn：把问题框定在人机协作场景。

- sets_up_next_cn：为举例公司AI教练系统作铺垫。

- failure_if_removed_cn：引言没有宏观入口。

- evidence_pointer：Introduction P1 S1

### 2. Introduction P1 S2

- order：2

- locator：Introduction P1 S2

- paraphrase_cn：许多公司引入AI教练系统以提升人类决策效能。

- move_code：EXAMPLE

- statement_status：fact

- why_here_cn：用实例让背景更具体。

- inherits_from_previous_cn：承接协作普遍化。

- changes_argument_state_cn：说明协作已是组织管理现实。

- sets_up_next_cn：为互补性讨论作准备。

- failure_if_removed_cn：背景缺少企业场景锚点。

- evidence_pointer：Introduction P1 S2

### 3. Introduction P1 S3

- order：3

- locator：Introduction P1 S3

- paraphrase_cn：现实里人类与机器可以互补。

- move_code：PHENOMENON_START

- statement_status：author_inference

- why_here_cn：提出协作潜力核心命题。

- inherits_from_previous_cn：由AI协作实例推出。

- changes_argument_state_cn：从背景转向协作价值。

- sets_up_next_cn：引出下面机器与人类各自优势的文献。

- failure_if_removed_cn：‘1+1>2’问题失去前提。

- evidence_pointer：Introduction P1 S3

### 4. Introduction P1 S4

- order：4

- locator：Introduction P1 S4

- paraphrase_cn：机器学习算法在一般情境下决策准确率通常高于人类。

- move_code：PRIOR_KNOWLEDGE

- statement_status：prior_literature

- why_here_cn：给出机器优势的文献事实。

- inherits_from_previous_cn：是互补性的第一半。

- changes_argument_state_cn：建立机器在统计判断上的优势。

- sets_up_next_cn：为人类独特优势句作对比。

- failure_if_removed_cn：机器贡献缺乏证据。

- evidence_pointer：Introduction P1 S4

### 5. Introduction P1 S5

- order：5

- locator：Introduction P1 S5

- paraphrase_cn：人类更倾向用经验识别低频且难入算法的案例。

- move_code：PRIOR_KNOWLEDGE

- statement_status：prior_literature

- why_here_cn：给出人类优势的文献事实，与机器互补。

- inherits_from_previous_cn：承接互补性命题。

- changes_argument_state_cn：建立人类处理稀有案例的优势。

- sets_up_next_cn：为灵活性优势句继续铺陈。

- failure_if_removed_cn：人类潜在贡献缺少基础。

- evidence_pointer：Introduction P1 S5

### 6. Introduction P1 S6

- order：6

- locator：Introduction P1 S6

- paraphrase_cn：人类在灵活性上也比机器更有优势。

- move_code：PRIOR_KNOWLEDGE

- statement_status：prior_literature

- why_here_cn：补充人类优势的第二维度。

- inherits_from_previous_cn：延续人类优势清单。

- changes_argument_state_cn：把人类贡献从单一扩展到多样化。

- sets_up_next_cn：为‘深度思考可增强绩效’句铺垫。

- failure_if_removed_cn：人类贡献不完整。

- evidence_pointer：Introduction P1 S6

### 7. Introduction P1 S7

- order：7

- locator：Introduction P1 S7

- paraphrase_cn：更重要的是，人类深度思考是被广泛确立的可增强独立或团队任务绩效的手段。

- move_code：PRIOR_KNOWLEDGE

- statement_status：prior_literature

- why_here_cn：把人类优势指向本文理论机制（深度思考）。

- inherits_from_previous_cn：从一般优势推至深度思考。

- changes_argument_state_cn：将人类贡献与系统2加工耦合。

- sets_up_next_cn：为P2现实落差提供理论对照。

- failure_if_removed_cn：双加工理论失去了引言锚点。

- evidence_pointer：Introduction P1 S7

### 8. Introduction P2 S1

- order：8

- locator：Introduction P2 S1

- paraphrase_cn：但信息不透明、算法复杂、人员经验不足等约束使协作现实表现低于预期。

- move_code：PROBLEM

- statement_status：author_inference

- why_here_cn：从潜力转到现实障碍。

- inherits_from_previous_cn：与互补性形成反差。

- changes_argument_state_cn：制造‘潜力-现实’落差，论证研究必要性。

- sets_up_next_cn：为不信任/过度依赖句作铺垫。

- failure_if_removed_cn：研究动因消失。

- evidence_pointer：Introduction P2 S1

### 9. Introduction P2 S2

- order：9

- locator：Introduction P2 S2

- paraphrase_cn：协作绩效因此因不信任机器或过度依赖机器而低于预期。

- move_code：PROBLEM_SPECIFY

- statement_status：prior_literature

- why_here_cn：具体指出行为机制：厌恶与依赖。

- inherits_from_previous_cn：继承约束条件后果。

- changes_argument_state_cn：把绩效问题归因于两类人类态度。

- sets_up_next_cn：为更坏情况句作对比。

- failure_if_removed_cn：机器解释文献的动机不完整。

- evidence_pointer：Introduction P2 S2

### 10. Introduction P2 S3

- order：10

- locator：Introduction P2 S3

- paraphrase_cn：更严重的是，没有恰当设计的协作系统时，人类介入会因过度谨慎或过度关注细节而降低协作绩效。

- move_code：PROBLEM_ESCALATE

- statement_status：prior_literature

- why_here_cn：强调人类介入可能反噬，提升研究紧迫性。

- inherits_from_previous_cn：延续协作失败场景。

- changes_argument_state_cn：使问题从绩效差升级到设计风险。

- sets_up_next_cn：为P3引入机器解释作为应对。

- failure_if_removed_cn：‘设计条件’的重要性不再突出。

- evidence_pointer：Introduction P2 S3

### 11. Introduction P3 S1

- order：11

- locator：Introduction P3 S1

- paraphrase_cn：为改变人类对机器从厌恶或过度依赖到主动贡献，研究者开始转向机器学习模型解释。

- move_code：PRIOR_WORK

- statement_status：prior_literature

- why_here_cn：引入现有解决方案。

- inherits_from_previous_cn：回应P2的行为障碍。

- changes_argument_state_cn：建立机器解释这条文献主线索。

- sets_up_next_cn：为P3批判该方案作铺垫。

- failure_if_removed_cn：理论贡献失去对象文献。

- evidence_pointer：Introduction P3 S1

### 12. Introduction P3 S2

- order：12

- locator：Introduction P3 S2

- paraphrase_cn：然而现有研究偏重技术方案，缺少对影响条件与机制的系统审视。

- move_code：GAP

- statement_status：author_inference

- why_here_cn：直接构造文献缺口。

- inherits_from_previous_cn：承认机器解释方向，但指出不足。

- changes_argument_state_cn：把文献状态从‘方法多样’转为‘条件机制未知’。

- sets_up_next_cn：为下一句‘并非每场景有效’细化。

- failure_if_removed_cn：本文‘条件性’贡献失去靶子。

- evidence_pointer：Introduction P3 S2

### 13. Introduction P3 S3

- order：13

- locator：Introduction P3 S3

- paraphrase_cn：并非所有模型解释在每场景都有效，这种遗漏带来局限。

- move_code：GAP_DETAIL

- statement_status：author_inference

- why_here_cn：把缺口转为可研究的条件依赖问题。

- inherits_from_previous_cn：承接条件机制缺失。

- changes_argument_state_cn：说明需要研究何时有效。

- sets_up_next_cn：为P4引入信息复杂度作铺垫。

- failure_if_removed_cn：双条件设计缺少动机。

- evidence_pointer：Introduction P3 S3

### 14. Introduction P4 S1

- order：14

- locator：Introduction P4 S1

- paraphrase_cn：本研究强调任务复杂性，特别是信息复杂度，是影响机器解释效果的关键权变因素。

- move_code：THEORY_CLAIM_START

- statement_status：theory_claim

- why_here_cn：提出本文核心条件变量。

- inherits_from_previous_cn：回应解释效果不一致。

- changes_argument_state_cn：从缺口进入理论主张。

- sets_up_next_cn：为双条件命题作铺垫。

- failure_if_removed_cn：研究焦点消失。

- evidence_pointer：Introduction P4 S1

### 15. Introduction P4 S2

- order：15

- locator：Introduction P4 S2

- paraphrase_cn：我们认为任务复杂性与机器解释应同时作用以促进人类深思并提升协作绩效。

- move_code：THEORY_PROPOSITION

- statement_status：theory_claim

- why_here_cn：给出全文理论命题：双条件联合。

- inherits_from_previous_cn：是P4 S1的推进。

- changes_argument_state_cn：确立‘两条件缺一不可’预测。

- sets_up_next_cn：为机制解释句（S3、S4）提供分述。

- failure_if_removed_cn：所有实证比较失去方向。

- evidence_pointer：Introduction P4 S2

### 16. Introduction P4 S3

- order：16

- locator：Introduction P4 S3

- paraphrase_cn：任务复杂性与信息丰富度通过吸引注意和兴趣让人投入深思。

- move_code：MECHANISM_CONDITION1

- statement_status：prior_literature

- why_here_cn：解释条件一如何引发系统2。

- inherits_from_previous_cn：承接双条件命题。

- changes_argument_state_cn：把信息复杂度连接到认知机制。

- sets_up_next_cn：为条件二（解释线索）作并列。

- failure_if_removed_cn：条件一的理论依据缺失。

- evidence_pointer：Introduction P4 S3

### 17. Introduction P4 S4

- order：17

- locator：Introduction P4 S4

- paraphrase_cn：机器解释作为有价值的线索和参考，促使人类仔细重估决策、处理冲突并积极认知加工。

- move_code：MECHANISM_CONDITION2

- statement_status：prior_literature

- why_here_cn：解释条件二如何触发系统2。

- inherits_from_previous_cn：与条件一对应。

- changes_argument_state_cn：把机器解释连接到积极推理。

- sets_up_next_cn：为联合效果句作铺垫。

- failure_if_removed_cn：条件二的理论依据缺失。

- evidence_pointer：Introduction P4 S4

### 18. Introduction P4 S5

- order：18

- locator：Introduction P4 S5

- paraphrase_cn：两条件对齐后，人类更可能采用强化决策策略并最终提升协作绩效。

- move_code：THEORY_PREDICTION

- statement_status：theory_claim

- why_here_cn：把两个机制统一为绩效预测。

- inherits_from_previous_cn：综合S3、S4两个机制。

- changes_argument_state_cn：完成从理论机制到可检验结果的推导。

- sets_up_next_cn：为P5方法必要性问题作铺垫。

- failure_if_removed_cn：双条件预测不完整。

- evidence_pointer：Introduction P4 S5

### 19. Introduction P5 S1

- order：19

- locator：Introduction P5 S1

- paraphrase_cn：既有机器解释研究多只做实验室或模拟实验。

- move_code：METHOD_GAP

- statement_status：author_inference

- why_here_cn：转入方法选择正当性。

- inherits_from_previous_cn：理论预测需要真实行为检验。

- changes_argument_state_cn：把缺口从理论扩展到证据生态。

- sets_up_next_cn：为实验室问题句作铺垫。

- failure_if_removed_cn：方法贡献缺少靶子。

- evidence_pointer：Introduction P5 S1

### 20. Introduction P5 S2

- order：20

- locator：Introduction P5 S2

- paraphrase_cn：实验室被试会表现不同且更主动，因此该方法有挑战。

- move_code：METHOD_CRITIQUE

- statement_status：prior_literature

- why_here_cn：解释为什么实验室不足。

- inherits_from_previous_cn：承接实验室现状。

- changes_argument_state_cn：否定实验室对行为估计的代表性。

- sets_up_next_cn：为现场实验句作铺垫。

- failure_if_removed_cn：现场实验的增量价值不明。

- evidence_pointer：Introduction P5 S2

### 21. Introduction P5 S3

- order：21

- locator：Introduction P5 S3

- paraphrase_cn：因此需要更务实的方法，这促使我们设计并实施现场实验。

- move_code：METHOD_DECISION

- statement_status：method_decision

- why_here_cn：给出方法转向。

- inherits_from_previous_cn：从方法批判推出方法选择。

- changes_argument_state_cn：正式确定证据策略。

- sets_up_next_cn：为S4说明现场实验价值。

- failure_if_removed_cn：方法贡献线索断裂。

- evidence_pointer：Introduction P5 S3

### 22. Introduction P5 S4

- order：22

- locator：Introduction P5 S4

- paraphrase_cn：现场实验是在真实场景观察人类行为、尤其是应对信息复杂度和线索的关键手段。

- move_code：METHOD_JUSTIFICATION

- statement_status：author_inference

- why_here_cn：强调现场实验对研究问题恰适。

- inherits_from_previous_cn：承接方法决策。

- changes_argument_state_cn：论证方法-问题匹配。

- sets_up_next_cn：为P6研究问题概括作铺垫。

- failure_if_removed_cn：现场实验与方法贡献缺乏合理性。

- evidence_pointer：Introduction P5 S4

### 23. Introduction P6 S1

- order：23

- locator：Introduction P6 S1

- paraphrase_cn：因此本文用现场实验判断人机协作中的‘1+1>2’能否实现。

- move_code：PURPOSE

- statement_status：author_inference

- why_here_cn：把方法挂到总问题。

- inherits_from_previous_cn：综合P4-P5。

- changes_argument_state_cn：回到论文核心目标。

- sets_up_next_cn：为三个RQ作铺垫。

- failure_if_removed_cn：总问题无人问津。

- evidence_pointer：Introduction P6 S1

### 24. Introduction P6 S2

- order：24

- locator：Introduction P6 S2

- paraphrase_cn：研究问题一：不同信息复杂度与系统设计下人机协作的现实绩效如何。

- move_code：RQ1

- statement_status：author_inference

- why_here_cn：把论文拆为第一个可回答的问题。

- inherits_from_previous_cn：源于双条件命题。

- changes_argument_state_cn：规范结果部分。

- sets_up_next_cn：与RQ2、RQ3构成结构路线图。

- failure_if_removed_cn：主结果没有问题对应。

- evidence_pointer：Introduction P6 S2

### 25. Introduction P6 S3

- order：25

- locator：Introduction P6 S3

- paraphrase_cn：研究问题二：底层机制是什么。

- move_code：RQ2

- statement_status：author_inference

- why_here_cn：提出机制问题。

- inherits_from_previous_cn：承接结果需要解释。

- changes_argument_state_cn：为机制分析部分设标。

- sets_up_next_cn：为RQ3个体差异作铺垫。

- failure_if_removed_cn：机制章节没有问题指引。

- evidence_pointer：Introduction P6 S3

### 26. Introduction P6 S4

- order：26

- locator：Introduction P6 S4

- paraphrase_cn：研究问题三：人类特征如何影响协作绩效。

- move_code：RQ3

- statement_status：author_inference

- why_here_cn：提出异质性/公平性问题。

- inherits_from_previous_cn：承接前两个RQ。

- changes_argument_state_cn：为扩展分析设标。

- sets_up_next_cn：为P7实验概述作铺垫。

- failure_if_removed_cn：异质性与偏见章节缺问题。

- evidence_pointer：Introduction P6 S4

### 27. Introduction P7 S1

- order：27

- locator：Introduction P7 S1

- paraphrase_cn：研究聚焦小额贷款行业，与大型亚洲小额贷款公司合作开展两阶段现场实验。

- move_code：SETTING

- statement_status：method_decision

- why_here_cn：交代实证场景与合作形态。

- inherits_from_previous_cn：总问题需要真实领域。

- changes_argument_state_cn：使方法具体化。

- sets_up_next_cn：为理论依据句作铺垫。

- failure_if_removed_cn：结果缺乏场景锚定。

- evidence_pointer：Introduction P7 S1

### 28. Introduction P7 S2

- order：28

- locator：Introduction P7 S2

- paraphrase_cn：借鉴双加工理论，提出唤起人类深思的两个前提：信息复杂度吸引参与、有用线索驱动积极考量。

- move_code：THEORY_APPLY

- statement_status：theory_claim

- why_here_cn：重申理论依据并过渡到实验操纵。

- inherits_from_previous_cn：与P4命题一致。

- changes_argument_state_cn：为处理设计提供合法性。

- sets_up_next_cn：为三个实验操纵句作铺垫。

- failure_if_removed_cn：实验处理成为任意设计。

- evidence_pointer：Introduction P7 S2

### 29. Introduction P7 S3

- order：29

- locator：Introduction P7 S3

- paraphrase_cn：因此实验操纵了提供给评估员的借款人信息量、是否看到机器建议、是否看到机器解释。

- move_code：DESIGN_OVERVIEW

- statement_status：design_decision

- why_here_cn：把理论条件化为三个可随机化处理。

- inherits_from_previous_cn：由两个理论前提推出。

- changes_argument_state_cn：完成理论-设计翻译。

- sets_up_next_cn：为P8结果预览作铺垫。

- failure_if_removed_cn：实验内容缺交代。

- evidence_pointer：Introduction P7 S3

### 30. Introduction P8 S1

- order：30

- locator：Introduction P8 S1

- paraphrase_cn：第一，小信息量下人类评估员不能为最终结果增加额外价值。

- move_code：RESULT_FIRST

- statement_status：empirical_result

- why_here_cn：先报告条件缺失时的否定结果。

- inherits_from_previous_cn：由操纵组合比较而来。

- changes_argument_state_cn：排除单独信息不足场景。

- sets_up_next_cn：为第二句正向结果作对照。

- failure_if_removed_cn：条件必要性叙事不完整。

- evidence_pointer：Introduction P8 S1

### 31. Introduction P8 S2

- order：31

- locator：Introduction P8 S2

- paraphrase_cn：第二，当人类在最终决策前看到机器建议、机器解释且信息量大时，人类优于机器，违约率下降2.02%（5.15%到3.13%）。

- move_code：RESULT_SECOND

- statement_status：empirical_result

- why_here_cn：给出核心正向效果。

- inherits_from_previous_cn：与S1形成对照。

- changes_argument_state_cn：证明双条件联合有效。

- sets_up_next_cn：为‘条件缺失则无效’句作铺垫。

- failure_if_removed_cn：核心结果缺失。

- evidence_pointer：Introduction P8 S2; Table 2 比较J

### 32. Introduction P8 S3

- order：32

- locator：Introduction P8 S3

- paraphrase_cn：但若缺少机器解释或信息复杂度任一条件，改善即消失。

- move_code：RESULT_CONDITIONAL

- statement_status：empirical_result

- why_here_cn：强调条件缺一不可。

- inherits_from_previous_cn：是S2的反事实条件句。

- changes_argument_state_cn：把结果编码为双条件交互而非主效应。

- sets_up_next_cn：为第三句分歧率结果作铺垫。

- failure_if_removed_cn：理论主张失去因果证据。

- evidence_pointer：Introduction P8 S3; Table 2 比较I/G/H

### 33. Introduction P8 S4

- order：33

- locator：Introduction P8 S4

- paraphrase_cn：第三，独立决策时人机分歧不可避免；协作时小信息量无解释组消除62.82%分歧，而大信息量加解释组消除85.67%分歧。

- move_code：RESULT_THIRD

- statement_status：empirical_result

- why_here_cn：补充跟随行为证据，显示解释促进人类接受机器建议。

- inherits_from_previous_cn：从绩效结果过渡到行为过程。

- changes_argument_state_cn：把结果从‘是否更好’扩展到‘如何跟随’。

- sets_up_next_cn：为P9机制预览作铺垫。

- failure_if_removed_cn：后来一致率/跟随率分析失去引言预告。

- evidence_pointer：Introduction P8 S4; Figure 4

### 34. Introduction P9 S1

- order：34

- locator：Introduction P9 S1

- paraphrase_cn：为解开机制，采用三步分析框架。

- move_code：MECHANISM_INTRO

- statement_status：method_decision

- why_here_cn：预告机制分析结构。

- inherits_from_previous_cn：结果需要解释。

- changes_argument_state_cn：从结果转为机制证据。

- sets_up_next_cn：为三项机制发现句作铺垫。

- failure_if_removed_cn：机制章节缺少框架预告。

- evidence_pointer：Introduction P9 S1

### 35. Introduction P9 S2

- order：35

- locator：Introduction P9 S2

- paraphrase_cn：第一，人类坚持传统重要特征（收入、教育），机器探索购物与轨迹等新信息源，解释为何机器在大信息量下更优。

- move_code：MECHANISM_FIRST

- statement_status：empirical_result

- why_here_cn：给出机制第一步发现。

- inherits_from_previous_cn：承接三步框架。

- changes_argument_state_cn：把绩效差异归因于特征使用差异。

- sets_up_next_cn：为第二步‘协作中再思考’作铺垫。

- failure_if_removed_cn：机制链条第一环缺失。

- evidence_pointer：Introduction P9 S2; Section 5.1

### 36. Introduction P9 S3

- order：36

- locator：Introduction P9 S3

- paraphrase_cn：第二，有机器解释和大信息量时，评估员会在不一致决策中进行主动再思考并提高终决准确率，如纠正对女性借款人的风险评估。

- move_code：MECHANISM_SECOND

- statement_status：empirical_result

- why_here_cn：给出核心机制发现。

- inherits_from_previous_cn：沿机制链条推进。

- changes_argument_state_cn：把条件联合效果与主动再思考连接。

- sets_up_next_cn：为第三步特征关联作铺垫。

- failure_if_removed_cn：理论贡献的核心机制缺失。

- evidence_pointer：Introduction P9 S3; Section 5.2

### 37. Introduction P9 S4

- order：37

- locator：Introduction P9 S4

- paraphrase_cn：第三，当人类认为解释中展示的特征信息性不足时，会把机器解释与其他特征关联起来完成再思考。

- move_code：MECHANISM_THIRD

- statement_status：empirical_result

- why_here_cn：给出最具体的特征关联机制。

- inherits_from_previous_cn：延续第二步。

- changes_argument_state_cn：把主动再思考操作化为特征联想。

- sets_up_next_cn：为P10异质性与偏见结果作铺垫。

- failure_if_removed_cn：机制中人类独特价值无法成立。

- evidence_pointer：Introduction P9 S4; Section 5.3

### 38. Introduction P10 S1

- order：38

- locator：Introduction P10 S1

- paraphrase_cn：个体异质性上，经验丰富的评估员更少跟随机器建议，但在机器建议与解释刺激下会启动再思考并改善绩效。

- move_code：HETEROGENEITY_RESULT

- statement_status：empirical_result

- why_here_cn：回答RQ3并增加边界认识。

- inherits_from_previous_cn：机制发现需要个体差异检验。

- changes_argument_state_cn：明确谁最可能受益。

- sets_up_next_cn：为公平结果句作铺垫。

- failure_if_removed_cn：管理启示中的经验人才主张失去依据。

- evidence_pointer：Introduction P10 S1; Section 6.1

### 39. Introduction P10 S2

- order：39

- locator：Introduction P10 S2

- paraphrase_cn：比较还款行为后发现，大信息量加机器解释的协作能缩小机器算法无意造成的性别违约率差距。

- move_code：FAIRNESS_RESULT

- statement_status：empirical_result

- why_here_cn：从绩效扩展到公平性。

- inherits_from_previous_cn：机制中女性风险评估纠正线索延续。

- changes_argument_state_cn：增加人类参与的社会价值。

- sets_up_next_cn：为贡献声明句作铺垫。

- failure_if_removed_cn：机器偏见贡献不成立。

- evidence_pointer：Introduction P10 S2; Section 6.2

### 40. Introduction P10 S3

- order：40

- locator：Introduction P10 S3

- paraphrase_cn：这进一步突出人机协作的价值与必要性。

- move_code：VALUE_UPGRADE

- statement_status：author_inference

- why_here_cn：把公平性结果升华为协作价值。

- inherits_from_previous_cn：承接S2结果。

- changes_argument_state_cn：从证据转为价值主张。

- sets_up_next_cn：为P11贡献部分作铺垫。

- failure_if_removed_cn：贡献部分缺少过渡。

- evidence_pointer：Introduction P10 S3

### 41. Introduction P11 S1

- order：41

- locator：Introduction P11 S1

- paraphrase_cn：本研究贡献是多方面的。

- move_code：CONTRIBUTION_START

- statement_status：contribution_claim

- why_here_cn：开启贡献声明段落。

- inherits_from_previous_cn：汇总全部发现。

- changes_argument_state_cn：把证据转为文献贡献。

- sets_up_next_cn：为三点贡献分述作铺垫。

- failure_if_removed_cn：论文缺少正式贡献定位。

- evidence_pointer：Introduction P11 S1

### 42. Introduction P11 S2

- order：42

- locator：Introduction P11 S2

- paraphrase_cn：第一，贡献于人机协作文献：现有研究多只隐含或表面地看结果，本文通过机制检测揭示经由合理设计的人类贡献，从而从理论与实证上展示人类再思考的存在与价值。

- move_code：CONTRIBUTION_1

- statement_status：contribution_claim

- why_here_cn：给出第一点理论贡献。

- inherits_from_previous_cn：对应P9机制发现。

- changes_argument_state_cn：把机制发现定位为文献推进。

- sets_up_next_cn：为第二点机器解释贡献句作铺垫。

- failure_if_removed_cn：贡献1不成立。

- evidence_pointer：Introduction P11 S2

### 43. Introduction P11 S3

- order：43

- locator：Introduction P11 S3

- paraphrase_cn：第二，贡献于机器解释文献：现有结论不一致，本文提出并验证原因之一是机器解释效果依赖其他条件（如环境/任务复杂性）；与既有认为解释触发系统1的观点不同，本文证明合理设计下解释可触发再思考并改善协作。

- move_code：CONTRIBUTION_2

- statement_status：contribution_claim

- why_here_cn：给出第二点理论贡献，直接回应摘要中的不一致。

- inherits_from_previous_cn：对应GAP与核心结果。

- changes_argument_state_cn：把双条件交互升华为解释文献的整合框架。

- sets_up_next_cn：为第三点机器偏见贡献作铺垫。

- failure_if_removed_cn：理论贡献2缺失。

- evidence_pointer：Introduction P11 S3

### 44. Introduction P11 S4

- order：44

- locator：Introduction P11 S4

- paraphrase_cn：第三，贡献于机器偏见文献：替代数据可缓解部分人口特征偏差，但机器失败已被证实；本文既识别性别偏差来源，也揭示人类介入弥补机器失败的价值与必要性。

- move_code：CONTRIBUTION_3

- statement_status：contribution_claim

- why_here_cn：给出第三点贡献，强调人类不可替代性。

- inherits_from_previous_cn：对应公平性结果。

- changes_argument_state_cn：把人类贡献扩展到算法公平议题。

- sets_up_next_cn：引言结束，进入文献综述。

- failure_if_removed_cn：贡献3不成立。

- evidence_pointer：Introduction P11 S4

## 引言逐段图谱

### 1. Introduction P1

- locator：Introduction P1

- opening_move_cn：以AI商业化与协作普遍性开场。

- development_move_cn：铺陈机器与人类各自的互补优势。

- pivot_move_cn：在S7转到人类深度思考这一增强绩效的工具。

- closing_move_cn：把人类优势理论化为深度思考，为双加工理论埋线。

- paragraph_job_cn：建立人机互补的潜力和人类深度思考的理论入口。

### 2. Introduction P2

- locator：Introduction P2

- opening_move_cn：以‘不幸的是’转折，引入现实约束。

- development_move_cn：列出不信任、过度依赖、过度谨慎等具体失败机制。

- pivot_move_cn：从绩效差升级到设计不当时人类介入反噬。

- closing_move_cn：制造‘需要能改变人类态度的设计’的需要。

- paragraph_job_cn：制造现实问题与理论潜力之间的落差，说明研究必要性。

### 3. Introduction P3

- locator：Introduction P3

- opening_move_cn：点明研究者已转向机器解释作为解决方案。

- development_move_cn：概括机器解释文献以技术方案为主。

- pivot_move_cn：指出条件与机制缺口，并非所有解释都有效。

- closing_move_cn：为引入信息复杂度这一权变因素铺路。

- paragraph_job_cn：构造机器解释文献的条件性缺口。

### 4. Introduction P4

- locator：Introduction P4

- opening_move_cn：直接提出本研究聚焦任务复杂性/信息复杂度。

- development_move_cn：分述信息复杂度吸引注意、机器解释提供线索两个机制。

- pivot_move_cn：在S5把两个机制综合为‘齐备时提升协作绩效’的预测。

- closing_move_cn：完成从理论机制到可检验预测的推导，为方法选择作铺垫。

- paragraph_job_cn：给出全文核心理论命题：双条件联合促成人类深思。

### 5. Introduction P5

- locator：Introduction P5

- opening_move_cn：指出既有研究多采用实验室/模拟。

- development_move_cn：解释实验室被试行为失真。

- pivot_move_cn：由方法局限转向现场实验的必然性。

- closing_move_cn：论证现场实验与信息复杂度和线索研究高度匹配。

- paragraph_job_cn：为两阶段现场实验提供方法正当性。

### 6. Introduction P6

- locator：Introduction P6

- opening_move_cn：用‘因此’把方法选择与总问题连接。

- development_move_cn：提出三个研究问题，形成路线图。

- pivot_move_cn：从总问题拆解为绩效、机制、个体差异三个层次。

- closing_move_cn：把全文结构预告为结果、机制、异质性三块。

- paragraph_job_cn：正式陈述RQ并预告文章结构。

### 7. Introduction P7

- locator：Introduction P7

- opening_move_cn：引出小额贷款公司与两阶段现场实验。

- development_move_cn：重申双加工理论的两个前提。

- pivot_move_cn：把理论前提翻译为三个实验操纵。

- closing_move_cn：预告实验设计，为结果部分铺设基线。

- paragraph_job_cn：交代研究场景与理论驱动的实验操纵。

### 8. Introduction P8

- locator：Introduction P8

- opening_move_cn：以‘我们的经验分析得出若干发现’开启结果预览。

- development_move_cn：按条件缺一不可的顺序报告三组结果。

- pivot_move_cn：从绩效结果转向跟随行为结果。

- closing_move_cn：用分歧消除率引出人类与机器的行为互动。

- paragraph_job_cn：在引言中给出承上启下的核心经验结果。

### 9. Introduction P9

- locator：Introduction P9

- opening_move_cn：以‘为解开机制，采用三步分析框架’进入机制。

- development_move_cn：依次报告人类与机器特征差异、主动再思考、特征关联三项机制发现。

- pivot_move_cn：从‘机器为何更好’推进到‘人类如何补足机器’。

- closing_move_cn：完成机制预览，使读者预期机制分析章节。

- paragraph_job_cn：预览三步机制，为‘人类重新思考’贡献铺垫。

### 10. Introduction P10

- locator：Introduction P10

- opening_move_cn：以‘进一步考虑人类异质性’开启扩展。

- development_move_cn：报告经验差异与性别公平两个扩展结果。

- pivot_move_cn：从绩效机制转向公平性价值。

- closing_move_cn：强化人类介入的价值，为贡献部分铺垫。

- paragraph_job_cn：预告异质性和偏见扩展，扩大结果的意义谱系。

### 11. Introduction P11

- locator：Introduction P11

- opening_move_cn：以‘贡献多面’开启贡献段落。

- development_move_cn：分别面向人机协作、机器解释、机器偏见三条文献流陈述贡献。

- pivot_move_cn：每点贡献都从现有不足切到本文证据。

- closing_move_cn：以人类价值与必要性总结全文定位。

- paragraph_job_cn：正式给出三点理论贡献，闭合引言与文献的缺口。

## 理论到设计逐句图谱

### 1. Section 2.1 P1 S1-S2

- order：1

- locator：Section 2.1 P1 S1-S2

- paraphrase_cn：AI应用需要人类干预与协助，既有研究探究人机协作在决策上的利弊。

- move_code：PRIOR_KNOWLEDGE

- statement_status：prior_literature

- why_here_cn：建立人机协作文献基础。

- inherits_from_previous_cn：承接引言现实问题。

- changes_argument_state_cn：综述正式展开。

- sets_up_next_cn：为机器优势/人类优势对比铺路。

- failure_if_removed_cn：文献综述缺总起。

- evidence_pointer：Section 2.1 P1

### 2. Section 2.1 P1 S3-S5

- order：2

- locator：Section 2.1 P1 S3-S5

- paraphrase_cn：统计模型通常达到或超过平均临床医生判断；机器能熟练处理大量数据，但难以处理随机不确定和边界案例。

- move_code：PRIOR_KNOWLEDGE

- statement_status：prior_literature

- why_here_cn：给出机器优势与短板。

- inherits_from_previous_cn：承接协作利弊。

- changes_argument_state_cn：确立机器擅长常规大量数据、不擅长边界随机案例。

- sets_up_next_cn：为人类优势（稀有案例、创新）作对比。

- failure_if_removed_cn：人机互补性不完整。

- evidence_pointer：Section 2.1 P1

### 3. Section 2.1 P1 S6-S9

- order：3

- locator：Section 2.1 P1 S6-S9

- paraphrase_cn：人类更擅长识别稀有案例，并在创新领域更有效；近期研究显示人机协作优于纯机器或纯人类，机器可增强人类能力，人类也可补充机器一般智能、多元想法和私有信息。

- move_code：PRIOR_KNOWLEDGE

- statement_status：prior_literature

- why_here_cn：建立人类互补价值与协作优势的文献依据。

- inherits_from_previous_cn：延续优缺点对照。

- changes_argument_state_cn：把‘协作优于单方’确立为背景公理。

- sets_up_next_cn：为Cao et al.具体证据句铺垫。

- failure_if_removed_cn：1+1>2缺乏文献前提。

- evidence_pointer：Section 2.1 P1

### 4. Section 2.1 P1 S10

- order：4

- locator：Section 2.1 P1 S10

- paraphrase_cn：Cao et al.显示分析师接触少量另类数据与机器资源后，机器算力与人类软信息理解结合产生最佳预测。

- move_code：EXEMPLAR

- statement_status：prior_literature

- why_here_cn：给出最接近本研究的互补证据。

- inherits_from_previous_cn：承接人机互补公理。

- changes_argument_state_cn：证明互补在真实金融判断中的可操作性。

- sets_up_next_cn：为第二段‘厌恶/过度依赖’作对照。

- failure_if_removed_cn：互补性缺少领域示例。

- evidence_pointer：Section 2.1 P1

### 5. Section 2.1 P2 S1-S4

- order：5

- locator：Section 2.1 P2 S1-S4

- paraphrase_cn：但近期研究揭示人类可能抵制或过度依赖机器，导致协作低效；抵制不仅发生在接受建议者，也发生在消费者等机器服务对象中。

- move_code：PRIOR_KNOWLEDGE

- statement_status：prior_literature

- why_here_cn：引入协作失败的行为机制。

- inherits_from_previous_cn：与互补性形成张力。

- changes_argument_state_cn：建立算法厌恶与过度依赖两类问题。

- sets_up_next_cn：为机器解释作为缓解手段铺路。

- failure_if_removed_cn：机器解释的必要性缺失。

- evidence_pointer：Section 2.1 P2

### 6. Section 2.1 P2 S5-S8

- order：6

- locator：Section 2.1 P2 S5-S8

- paraphrase_cn：聊天机器人披露对用户接受产生负面影响；人类厌恶也可能源于机器威胁就业；机器在多种工作中取代人类，但过度依赖同样使协作失去意义。

- move_code：PRIOR_KNOWLEDGE

- statement_status：prior_literature

- why_here_cn：细化厌恶来源并提醒过度依赖风险。

- inherits_from_previous_cn：延续行为障碍。

- changes_argument_state_cn：说明调整人类反应是双向困难。

- sets_up_next_cn：为2.2机器解释文献作铺垫。

- failure_if_removed_cn：本文要解决的现实问题不完整。

- evidence_pointer：Section 2.1 P2

### 7. Section 2.2 P1 S1-S2

- order：7

- locator：Section 2.2 P1 S1-S2

- paraphrase_cn：缺乏模型解释会因不信任导致人类厌恶，现有文献因此用更详细决策信息提升信任。

- move_code：PRIOR_KNOWLEDGE

- statement_status：prior_literature

- why_here_cn：开启机器解释文献。

- inherits_from_previous_cn：回应算法厌恶。

- changes_argument_state_cn：把解释定位为信任工具。

- sets_up_next_cn：为解释局限句作铺垫。

- failure_if_removed_cn：机器解释主题缺入口。

- evidence_pointer：Section 2.2 P1

### 8. Section 2.2 P1 S3-S5

- order：8

- locator：Section 2.2 P1 S3-S5

- paraphrase_cn：事后解释可在多样条件下帮助人类建立心理模型以增强信任和效率，但应谨慎：不可直观解释可能无法提升信任，事后解释也可能提供不完整或有偏信息。

- move_code：PRIOR_KNOWLEDGE

- statement_status：prior_literature

- why_here_cn：给机器解释以边界条件。

- inherits_from_previous_cn：承接信任工具。

- changes_argument_state_cn：解释并非普遍有效，埋下条件性种子。

- sets_up_next_cn：为2.2第二段机制缺口作铺垫。

- failure_if_removed_cn：条件性贡献缺乏文献基础。

- evidence_pointer：Section 2.2 P1

### 9. Section 2.2 P2 S1-S3

- order：9

- locator：Section 2.2 P2 S1-S3

- paraphrase_cn：本文与这一实践一致，但少有人深入解释影响人类决策过程的机制；最相近的Bauer et al.发现人类会动态调整特征权重并适应心理模型，但解释也可能强化确认偏误。

- move_code：PRIOR_KNOWLEDGE

- statement_status：prior_literature

- why_here_cn：界定与最接近文献的关系。

- inherits_from_previous_cn：从一般解释文献到相似工作。

- changes_argument_state_cn：把文献缺口锁定为机制与条件。

- sets_up_next_cn：为两个差异点作铺垫。

- failure_if_removed_cn：与最相关工作对比消失。

- evidence_pointer：Section 2.2 P2

### 10. Section 2.2 P2 S4-S7

- order：10

- locator：Section 2.2 P2 S4-S7

- paraphrase_cn：本文与Bauer et al.有两处关键差异：第一，他们只考虑有限特征，本文引入信息复杂度并认为解释效果依赖信息复杂度；第二，他们用在线实验室实验，实验室被试行为可能被高估，本文采用真实小微金融场景的现场实验。

- move_code：DIFFERENTIATION

- statement_status：author_inference

- why_here_cn：明确本文增量贡献。

- inherits_from_previous_cn：接着差异点展开。

- changes_argument_state_cn：把本文置于与最接近研究的独特位置。

- sets_up_next_cn：为2.3微观金融背景作铺垫。

- failure_if_removed_cn：创新点阐述不完整。

- evidence_pointer：Section 2.2 P2

### 11. Section 2.3 P1 S1-S6

- order：11

- locator：Section 2.3 P1 S1-S6

- paraphrase_cn：大量学者研究P2P借贷、众筹和小额贷款中的投资者决策因素和偏差，近期研究关注机器辅助工具如机器人顾问，投资者会根据失败经验调整对机器依赖。

- move_code：PRIOR_KNOWLEDGE

- statement_status：prior_literature

- why_here_cn：建立本文实证领域背景。

- inherits_from_previous_cn：从一般决策到小微金融。

- changes_argument_state_cn：说明金融决策中的机器辅助已有研究但聚焦点不同。

- sets_up_next_cn：为本文‘机器建议如何影响用户决策’独特点作铺垫。

- failure_if_removed_cn：选择小额贷款行业缺乏文献理由。

- evidence_pointer：Section 2.3 P1

### 12. Section 2.4 P1 S1-S3

- order：12

- locator：Section 2.4 P1 S1-S3

- paraphrase_cn：人机协作价值源于互补，但人类易陷入厌恶或过度依赖；关键是在与机器共事时唤起人类深度思考。

- move_code：THEORY_START

- statement_status：theory_claim

- why_here_cn：从文献过渡到本文理论框架。

- inherits_from_previous_cn：承接2.1-2.3的困境。

- changes_argument_state_cn：把问题重新表述为唤起系统2的难题。

- sets_up_next_cn：为双加工理论介绍作铺垫。

- failure_if_removed_cn：理论框架缺过渡。

- evidence_pointer：Section 2.4 P1

### 13. Section 2.4 P1 S4-S5

- order：13

- locator：Section 2.4 P1 S4-S5

- paraphrase_cn：双加工理论提出系统1和系统2两种认知系统：系统1快速自动低努力，系统2缓慢深思熟虑并消耗认知资源。

- move_code：THEORY_BASE

- statement_status：theory_claim

- why_here_cn：给出理论核心概念。

- inherits_from_previous_cn：承接深度思考问题。

- changes_argument_state_cn：定义系统1/系统2。

- sets_up_next_cn：为条件推导作铺垫。

- failure_if_removed_cn：双加工理论名存实亡。

- evidence_pointer：Section 2.4 P1

### 14. Section 2.4 P2 S1-S2

- order：14

- locator：Section 2.4 P2 S1-S2

- paraphrase_cn：多种因素决定个体选系统1还是系统2；要鼓励系统2，必须满足一定条件，其中任务复杂性是首要条件。

- move_code：THEORY_PROPOSITION

- statement_status：theory_claim

- why_here_cn：推出条件一：任务复杂性。

- inherits_from_previous_cn：由双系统定义推出。

- changes_argument_state_cn：把系统2激活条件化为任务复杂性。

- sets_up_next_cn：为信息复杂度分述作铺垫。

- failure_if_removed_cn：条件一理论缺失。

- evidence_pointer：Section 2.4 P2

### 15. Section 2.4 P2 S3-S8

- order：15

- locator：Section 2.4 P2 S3-S8

- paraphrase_cn：任务复杂性常体现为信息复杂度，通过吸引注意激发深度思考；掌握情境是后续深思与行动选择的前提；新属性提供新颖信息强化任务识别；面对更多样陌生信息时个体倾向投入更多推理努力。

- move_code：MECHANISM_CONDITION1

- statement_status：theory_claim

- why_here_cn：把任务复杂性具体化为信息复杂度并解释认知机制。

- inherits_from_previous_cn：承接条件一。

- changes_argument_state_cn：建立信息复杂度与努力参与的因果链。

- sets_up_next_cn：为简单信息导致系统1句作对照。

- failure_if_removed_cn：信息复杂度变量失去理论支撑。

- evidence_pointer：Section 2.4 P2

### 16. Section 2.4 P3 S1-S2

- order：16

- locator：Section 2.4 P3 S1-S2

- paraphrase_cn：第二个条件是提供有用参考线索；设计良好的参考线索能促使个体仔细重估决策并与参考点比较。

- move_code：THEORY_PROPOSITION

- statement_status：theory_claim

- why_here_cn：推出条件二：有用线索。

- inherits_from_previous_cn：条件一之后需要条件二。

- changes_argument_state_cn：把系统2激活的第二条件设为参考线索。

- sets_up_next_cn：为线索的多种实现方式作铺垫。

- failure_if_removed_cn：机器解释作为条件二失去理论依据。

- evidence_pointer：Section 2.4 P3

### 17. Section 2.4 P3 S3-S6

- order：17

- locator：Section 2.4 P3 S3-S6

- paraphrase_cn：高信息质量、结构化具体信息、明确参考点等都能促进深度认知加工；个体经验与专长也会影响系统2使用。

- move_code：MECHANISM_CONDITION2

- statement_status：theory_claim

- why_here_cn：解释为何机器解释可作为有用线索。

- inherits_from_previous_cn：延续条件二。

- changes_argument_state_cn：为解释设计提供一般机理。

- sets_up_next_cn：为映射到人机协作设计作铺垫。

- failure_if_removed_cn：机器解释触发系统2的机理缺失。

- evidence_pointer：Section 2.4 P3

### 18. Section 2.4 P4 S1-S2

- order：18

- locator：Section 2.4 P4 S1-S2

- paraphrase_cn：将理论应用到人机协作，提出两种设计分别对应两个条件：提供丰富信息和向人类展示结构化机器解释。

- move_code：DESIGN_MAPPING

- statement_status：design_decision

- why_here_cn：完成理论到设计的正式翻译。

- inherits_from_previous_cn：两个条件理论。

- changes_argument_state_cn：理论条件变成可操纵处理。

- sets_up_next_cn：为后续信息量与解释可用性论证作铺垫。

- failure_if_removed_cn：实验处理与理论脱节。

- evidence_pointer：Section 2.4 P4

### 19. Section 2.4 P4 S3-S5

- order：19

- locator：Section 2.4 P4 S3-S5

- paraphrase_cn：丰富信息需要强认知能力，可唤起人类对任务复杂性的感知；机器建议配合忠实且可解释的解释能触发主动认知推理，人类可学习机器决策逻辑并检查新知识是否提升准确率。

- move_code：MECHANISM_DESIGN

- statement_status：theory_claim

- why_here_cn：解释两个设计各自的作用机制。

- inherits_from_previous_cn：承接设计映射。

- changes_argument_state_cn：连接处理与系统2加工。

- sets_up_next_cn：为‘rethinking’定义作铺垫。

- failure_if_removed_cn：设计背后的理论机制不在场。

- evidence_pointer：Section 2.4 P4

### 20. Section 2.4 P4 S6-S8

- order：20

- locator：Section 2.4 P4 S6-S8

- paraphrase_cn：把这定义为rethinking过程：仔细复核先前决策并决定是否改变；符合Jussupow et al.提出的主动考虑模式，被认为是人机协作最佳实践。

- move_code：CONSTRUCT_DEFINITION

- statement_status：theory_claim

- why_here_cn：正式界定本文核心机制构念。

- inherits_from_previous_cn：由机器解释触发过程引出。

- changes_argument_state_cn：把特征权重变化操作化为主动再思考。

- sets_up_next_cn：为实证机制检验提供概念目标。

- failure_if_removed_cn：机制贡献缺构念定义。

- evidence_pointer：Section 2.4 P4

### 21. Section 2.4 P5 S1-S3

- order：21

- locator：Section 2.4 P5 S1-S3

- paraphrase_cn：尽管人机协作研究众多，但缺乏在不同条件下人类与机器助手互动过程的机理揭示；本文聚焦信息复杂度与机器解释如何促使人类主动再思考并改善决策结果。

- move_code：THEORY_GAP_RETURN

- statement_status：author_inference

- why_here_cn：重申本文填补的缺口，闭合文献综述。

- inherits_from_previous_cn：综合2.1-2.4。

- changes_argument_state_cn：把理论转化为本文研究声明。

- sets_up_next_cn：为实验设计章节作铺垫。

- failure_if_removed_cn：文献综述缺乏总结。

- evidence_pointer：Section 2.4 P5

## 制品设计理由逐句图谱

### 1. Section 3.1 P1 S1-S2

- order：1

- locator：Section 3.1 P1 S1-S2

- paraphrase_cn：合作公司为2011年成立、服务25万借款人的亚洲小额贷款公司，提供约465美元无抵押小额贷款。

- move_code：CONTEXT

- statement_status：fact

- why_here_cn：确立现场实验的真实平台。

- inherits_from_previous_cn：承接引言中行业选择。

- changes_argument_state_cn：提供可观察真实贷款决策与还款表现的场景。

- sets_up_next_cn：为贷款流程描述作铺垫。

- failure_if_removed_cn：现场实验缺乏背景。

- evidence_pointer：Section 3.1 P1

### 2. Section 3.1 P1 S3-S6

- order：2

- locator：Section 3.1 P1 S3-S6

- paraphrase_cn：公司只用自有资金放贷，贷款多为临时资金需求，期限1-7个月，年利率12%-16%。

- move_code：CONTEXT_DETAIL

- statement_status：fact

- why_here_cn：说明借贷设置简单且可标准化。

- inherits_from_previous_cn：延续公司背景。

- changes_argument_state_cn：为贷款期限限制提供理由。

- sets_up_next_cn：为借款人申请信息句作铺垫。

- failure_if_removed_cn：贷款绩效定义缺少背景。

- evidence_pointer：Section 3.1 P1

### 3. Section 3.1 P2 S1-S4

- order：3

- locator：Section 3.1 P2 S1-S4

- paraphrase_cn：借款人需提供基本身份收入信息并选择贷款金额期限；研究只聚焦1-3个月贷款以便观察还款。

- move_code：DESIGN_DECISION

- statement_status：design_decision

- why_here_cn：解释贷款期限限制以缩短贷后观察期。

- inherits_from_previous_cn：由公司贷款流程推出。

- changes_argument_state_cn：使违约指标在五个月内可确认。

- sets_up_next_cn：为随机分配评估员句作铺垫。

- failure_if_removed_cn：违约定义与实验时间线不匹配。

- evidence_pointer：Section 3.1 P2

### 4. Section 3.1 P2 S5-S8

- order：4

- locator：Section 3.1 P2 S5-S8

- paraphrase_cn：每份申请随机分配给人类评估员，公司原批准率约47%，贷款筛选目标是保持批准率下最小化违约。

- move_code：BASELINE_RATIONALE

- statement_status：fact

- why_here_cn：说明公司与市场中常见批准率，为固定审批率提供理由。

- inherits_from_previous_cn：借贷流程句。

- changes_argument_state_cn：确立47%批准率为所有实验组的约束。

- sets_up_next_cn：为Stage1组别设计作铺垫。

- failure_if_removed_cn：组间批准率可比性缺依据。

- evidence_pointer：Section 3.1 P2

### 5. Section 3.2.1 P1-S1

- order：5

- locator：Section 3.2.1 P1-S1

- paraphrase_cn：双加工理论引入两个影响协作决策的因素，第一步通过实证设置引入信息复杂度变化。

- move_code：THEORY_TO_ARTIFACT

- statement_status：design_decision

- why_here_cn：说明处理I直接来源于理论。

- inherits_from_previous_cn：承接2.4设计映射。

- changes_argument_state_cn：使信息复杂度成为第一个随机化处理。

- sets_up_next_cn：为小信息量定义作铺垫。

- failure_if_removed_cn：处理I无理论合法性。

- evidence_pointer：Section 3.2.1 P1

### 6. Section 3.2.1 P2-S1-S2

- order：6

- locator：Section 3.2.1 P2-S1-S2

- paraphrase_cn：实验前平台完全由人类评估员基于12个基础变量决策，构成小信息量组。

- move_code：TREATMENT_DEFINITION

- statement_status：design_decision

- why_here_cn：给出小信息量的可操作定义。

- inherits_from_previous_cn：基于公司原流程。

- changes_argument_state_cn：定义控制组信息环境。

- sets_up_next_cn：为大信息量构造作铺垫。

- failure_if_removed_cn：小信息量处理不清晰。

- evidence_pointer：Section 3.2.1 P2

### 7. Section 3.2.1 P2-S3-S5

- order：7

- locator：Section 3.2.1 P2-S3-S5

- paraphrase_cn：为构造大信息量场景，要求公司从2017年6月起收集借款人在最大电商平台近六个月购物和通信运营商手机使用信息，并据文献提取每类32个特征。

- move_code：TREATMENT_DESIGN

- statement_status：design_decision

- why_here_cn：给出大信息量的来源与特征数量。

- inherits_from_previous_cn：由信息复杂度概念推出。

- changes_argument_state_cn：把理论条件具体化为新增64个特征。

- sets_up_next_cn：为模型准备与解释处理作铺垫。

- failure_if_removed_cn：信息复杂度操纵不成立。

- evidence_pointer：Section 3.2.1 P2

### 8. Section 3.2.2 P1-S1-S3

- order：8

- locator：Section 3.2.2 P1-S1-S3

- paraphrase_cn：公司此前无机器协助，需要为两种信息场景分别训练预测模型；训练样本为2017年6月申请贷款的借款人。

- move_code：MACHINE_PREP

- statement_status：method_decision

- why_here_cn：说明机器建议来源需要预先训练。

- inherits_from_previous_cn：承接两种信息场景。

- changes_argument_state_cn：把机器作为可比较基线引入。

- sets_up_next_cn：为违约定义和还款观察句作铺垫。

- failure_if_removed_cn：机器条件缺生成方式。

- evidence_pointer：Section 3.2.2 P1

### 9. Section 3.2.2 P1-S4-S6

- order：9

- locator：Section 3.2.2 P1-S4-S6

- paraphrase_cn：收集获批贷款2017年7-11月还款信息；因贷款期限不超过三个月，五个月足以确认还款与违约；违约定义为逾期60天未全额还清。

- move_code：OUTCOME_DEFINITION

- statement_status：method_decision

- why_here_cn：给出违约结果变量的操作定义。

- inherits_from_previous_cn：训练样本需要结果标签。

- changes_argument_state_cn：界定全文主要因变量。

- sets_up_next_cn：为模型训练与比较作铺垫。

- failure_if_removed_cn：违约率指标无法解释。

- evidence_pointer：Section 3.2.2 P1

### 10. Section 3.2.2 P2

- order：10

- locator：Section 3.2.2 P2

- paraphrase_cn：用标准操作化（10折交叉验证、样本外预测、超参数调优）反复训练多种算法，XGBoost表现最佳故用于实验；实验中不更新模型。

- move_code：MACHINE_MODEL_CHOICE

- statement_status：method_decision

- why_here_cn：解释机器模型选择与稳定性。

- inherits_from_previous_cn：需要可靠机器基线。

- changes_argument_state_cn：确立XGBoost为机器决策主体。

- sets_up_next_cn：为训练人类评估员与SHAP解释作铺垫。

- failure_if_removed_cn：机器性能与实验稳定性缺依据。

- evidence_pointer：Section 3.2.2 P2

### 11. Section 3.2.2 P3-S1-S3

- order：11

- locator：Section 3.2.2 P3-S1-S3

- paraphrase_cn：用相同训练样本训练人类评估员，随机分到小信息与大信息两组，七天训练后评估表现稳定。

- move_code：HUMAN_TRAINING

- statement_status：method_decision

- why_here_cn：确保人类在两种信息量下达到稳定基线。

- inherits_from_previous_cn：人类评估员也是实验输入。

- changes_argument_state_cn：消除学习效应这一混淆。

- sets_up_next_cn：为阶段实验提供训练完备的人类组。

- failure_if_removed_cn：阶段间人类表现不可比。

- evidence_pointer：Section 3.2.2 P3

### 12. Section 3.2.2 P4

- order：12

- locator：Section 3.2.2 P4

- paraphrase_cn：用预训练模型设计第二个处理：采用SHAP方法产生Shapley值表示每个特征在考虑所有组合后对违约预测的平均期望边际贡献，图1展示两信息场景最重要的特征。

- move_code：EXPLANATION_DESIGN

- statement_status：design_decision

- why_here_cn：把机器解释操作化为SHAP特征重要性。

- inherits_from_previous_cn：需要结构化可解释线索。

- changes_argument_state_cn：确立处理II的实现方式。

- sets_up_next_cn：为图1与实验组别解释作铺垫。

- failure_if_removed_cn：机器解释处理无具体内容。

- evidence_pointer：Section 3.2.2 P4

### 13. Section 3.3.1 P1

- order：13

- locator：Section 3.3.1 P1

- paraphrase_cn：Stage 1于2017年12月8日开始一周；短期处理有助于排除评估员学习、算法演化和借款人分布变化的长期混淆。

- move_code：STUDY_OPENING_RATIONALE

- statement_status：method_decision

- why_here_cn：解释阶段一的时长设计。

- inherits_from_previous_cn：需要干净基线。

- changes_argument_state_cn：控制时间相关混淆。

- sets_up_next_cn：为四组随机分配作铺垫。

- failure_if_removed_cn：内部有效性缺时间控制论证。

- evidence_pointer：Section 3.3.1 P1

### 14. Section 3.3.1 P2-S1-S4

- order：14

- locator：Section 3.3.1 P2-S1-S4

- paraphrase_cn：每份新申请随机分配到四组：组1人类小信息、组2人类大信息、组3机器小信息、组4机器大信息；人类组与训练过程一致。

- move_code：STUDY_DESIGN_1

- statement_status：design_decision

- why_here_cn：给出Stage1 2×2组别。

- inherits_from_previous_cn：信息复杂度处理。

- changes_argument_state_cn：建立纯人类与纯机器基线。

- sets_up_next_cn：为审批率控制句作铺垫。

- failure_if_removed_cn：协作效果无处比较。

- evidence_pointer：Section 3.3.1 P2

### 15. Section 3.3.1 P2-S5-S6

- order：15

- locator：Section 3.3.1 P2-S5-S6

- paraphrase_cn：机器组按预测违约概率由低到高排序并保持47%批准率，所有组批准率按要求保持一致；随后跟踪获批贷款2018年1-5月还款。

- move_code：BENCHMARK_EQUALIZATION

- statement_status：method_decision

- why_here_cn：使绩效比较不受批准率差异干扰。

- inherits_from_previous_cn：公司原批准率约束。

- changes_argument_state_cn：把违约率差异归因于决策质量而非审批数量。

- sets_up_next_cn：为Stage2设计作铺垫。

- failure_if_removed_cn：组间违约率比较不干净。

- evidence_pointer：Section 3.3.1 P2

### 16. Section 3.3.2 P1-S1-S3

- order：16

- locator：Section 3.3.2 P1-S1-S3

- paraphrase_cn：Stage 2于12月15-28日进行两周，工作量与第一阶段相似；再次随机分配新申请到四组并让人类与机器协作。

- move_code：STUDY_OPENING_2

- statement_status：method_decision

- why_here_cn：说明阶段二安排与工作量匹配。

- inherits_from_previous_cn：阶段一后需要协作处理。

- changes_argument_state_cn：引入协作条件。

- sets_up_next_cn：为两步决策流程作铺垫。

- failure_if_removed_cn：协作效果无法检验。

- evidence_pointer：Section 3.3.2 P1

### 17. Section 3.3.2 P1-S4-S6

- order：17

- locator：Section 3.3.2 P1-S4-S6

- paraphrase_cn：组5-8人员在组1/2基础上随机均分，保持相同信息量；决策分两步：第一步人类独立评估，第二步呈现机器对该贷款的审批建议。

- move_code：TWO_STEP_DESIGN

- statement_status：design_decision

- why_here_cn：两步设计用于分离人类初始判断与受机器影响后的终判。

- inherits_from_previous_cn：需要识别人类增量贡献。

- changes_argument_state_cn：使‘人类贡献’可测量。

- sets_up_next_cn：为有无解释组作铺垫。

- failure_if_removed_cn：无法分离人类独立贡献。

- evidence_pointer：Section 3.3.2 P1

### 18. Section 3.3.2 P2-S1-S5

- order：18

- locator：Section 3.3.2 P2-S1-S5

- paraphrase_cn：组5/7只给机器建议不给解释，组6/8给机器建议并附带后验解释（重要特征及借款人值与未违约均值比较）；评估员被告知机器学习算法通常有强决策能力。

- move_code：EXPLANATION_TREATMENT_DESIGN

- statement_status：design_decision

- why_here_cn：操作化解释处理的两种水平。

- inherits_from_previous_cn：两步流程需要解释维度。

- changes_argument_state_cn：把理论‘有用线索’落到SHAP特征对比界面。

- sets_up_next_cn：为解释作为理想参考的推断作铺垫。

- failure_if_removed_cn：处理II无法检验。

- evidence_pointer：Section 3.3.2 P2

### 19. Section 3.3.2 P2-S6-S8

- order：19

- locator：Section 3.3.2 P2-S6-S8

- paraphrase_cn：基于理论框架，我们推断这些信息因机器优越能力而应成为理想参考；人类做出终决，可坚持己见或跟随机器；所有组保持约47%批准率并跟踪五个月还款。

- move_code：REFERENCE_CUE_RATIONALE

- statement_status：author_inference

- why_here_cn：解释为何SHAP界面算‘有用线索’。

- inherits_from_previous_cn：解释处理设计。

- changes_argument_state_cn：把界面内容与理论条件连接。

- sets_up_next_cn：为3.4数据和随机化检验作铺垫。

- failure_if_removed_cn：解释界面有效性缺少理论解释。

- evidence_pointer：Section 3.3.2 P2

### 20. Section 3.4 P1-S2-S3

- order：20

- locator：Section 3.4 P1-S2-S3

- paraphrase_cn：数据包含借款人信息、人类/机器的初始决策、终决和还款表现，以及评估员背景（性别、教育、经验月数、历史准确率）。

- move_code：DATA_DESCRIPTION

- statement_status：method_decision

- why_here_cn：说明用于随机化检验与异质性分析的变量完备。

- inherits_from_previous_cn：实验组已完成数据收集。

- changes_argument_state_cn：为随机化成功声明提供变量。

- sets_up_next_cn：为样本量清理句作铺垫。

- failure_if_removed_cn：结果可信度缺数据信息。

- evidence_pointer：Section 3.4 P1

### 21. Section 3.4 P2-S1-S3

- order：21

- locator：Section 3.4 P2-S1-S3

- paraphrase_cn：八组总贷款23,805笔，去除203个重复借款人后最终样本23,602；表1显示组间借款人、贷款和评估员特征无显著差异，说明随机化成功。

- move_code：RANDOMIZATION_CHECK

- statement_status：empirical_result

- why_here_cn：为因果推断提供随机化证据。

- inherits_from_previous_cn：数据已收集。

- changes_argument_state_cn：建立各组可比性。

- sets_up_next_cn：为Section 4组间比较作铺垫。

- failure_if_removed_cn：因果主张失去基础。

- evidence_pointer：Section 3.4 P2; Table 1

## Study开头、过渡与收束图谱

### 1. Section 4 P1 S1-S3

- study_or_phase：Section 4 empirical findings opening

- locator：Section 4 P1 S1-S3

- paraphrase_cn：关键变量为借款人违约率，是小额贷款行业通用指标；定义为获批贷款中违约占比；图3画出各组违约率，表2报告组间t检验。

- move_code：OUTCOME_AND_BENCHMARK_OPENING

- statement_status：method_decision

- why_here_cn：给出整个结果部分的结果变量与比较程序。

- inherits_from_previous_cn：实验设计与样本已就绪。

- changes_argument_state_cn：把实验处理转为可检验绩效差异。

- sets_up_next_cn：为组1基准和比较A-J作铺垫。

- failure_if_removed_cn：结果报告没有因变量定义。

- evidence_pointer：Section 4 P1

### 2. Section 4 P5 S1

- study_or_phase：Section 4 transition to behavioral decomposition

- locator：Section 4 P5 S1

- paraphrase_cn：注意到这些模式后，我们进一步分解人类在观察机器建议后的决策行为。

- move_code：RESULT_TO_BEHAVIOR_TRANSITION

- statement_status：author_inference

- why_here_cn：从绩效差异转向行为机制。

- inherits_from_previous_cn：组间绩效结果已呈现。

- changes_argument_state_cn：引出一致性与跟随率分析。

- sets_up_next_cn：为Figure 4和Table 2跟随率作铺垫。

- failure_if_removed_cn：绩效结果与机制分析之间缺桥。

- evidence_pointer：Section 4 P5

### 3. Section 5 P1 S1-S4

- study_or_phase：Section 5 mechanism section opening

- locator：Section 5 P1 S1-S4

- paraphrase_cn：本节旨在解开绩效差异与人类贡献的机制，分三步：为何人与机独立决策不同、为何协作中人类与机器建议分歧、分歧如何影响决策质量并分解再思考过程。

- move_code：MECHANISM_ARCHITECTURE

- statement_status：method_decision

- why_here_cn：为机制分析整体提供路线图。

- inherits_from_previous_cn：核心结果需要解释。

- changes_argument_state_cn：建立3步结构。

- sets_up_next_cn：为5.1具体方法作铺垫。

- failure_if_removed_cn：机制章节散乱无结构。

- evidence_pointer：Section 5 P1

### 4. Section 5.1 P1 S1

- study_or_phase：5.1 opening

- locator：Section 5.1 P1 S1

- paraphrase_cn：为回答人与机为何表现不同，通过识别决策中的重要特征来考察决策过程。

- move_code：SUBSECTION_OPENING

- statement_status：method_decision

- why_here_cn：把5.1目标限定在特征重要性差异。

- inherits_from_previous_cn：承接机制框架第一步。

- changes_argument_state_cn：引入probit模型作为特征重要性代理。

- sets_up_next_cn：为MInd交互项模型作铺垫。

- failure_if_removed_cn：机制第一步缺方法入口。

- evidence_pointer：Section 5.1 P1

### 5. Section 5.1 P5 S1-S4

- study_or_phase：5.1 closing interpretation

- locator：Section 5.1 P5 S1-S4

- paraphrase_cn：小信息量下人与机器使用相似特征；大信息量下人类坚持传统特征而机器探索购物、通话、轨迹等新源信息，这解释了机器为何在大信息量下显著更好。

- move_code：MECHANISM_RESULT_INTERPRET

- statement_status：empirical_result

- why_here_cn：把绩效差异解释为特征使用差异。

- inherits_from_previous_cn：probit回归结果。

- changes_argument_state_cn：为人类为何需再思考建立前提。

- sets_up_next_cn：为5.2协作中分歧作铺垫。

- failure_if_removed_cn：机制链条第一步断裂。

- evidence_pointer：Section 5.1 P5; Tables 3-4

### 6. Section 5.2 P1 S1-S2

- study_or_phase：5.2 opening transition

- locator：Section 5.2 P1 S1-S2

- paraphrase_cn：接下来解开协作模式下人类为何不同意机器建议的底层行为机制。

- move_code：TRANSITION_TO_STEP2

- statement_status：author_inference

- why_here_cn：从独立决策机制推进到协作决策机制。

- inherits_from_previous_cn：人类-机器特征差异已建立。

- changes_argument_state_cn：把关注点从‘为什么不同’转到‘分歧后如何变’。

- sets_up_next_cn：为IfFinal交互项回归作铺垫。

- failure_if_removed_cn：5.2缺乏过渡。

- evidence_pointer：Section 5.2 P1

### 7. Section 5.2 P6 S1-S3

- study_or_phase：5.2 competing mechanisms frame

- locator：Section 5.2 P6 S1-S3

- paraphrase_cn：提出人与机分歧的两条可能路径：边界案例不确定而跟随，或特征评估差异而坚持己见。

- move_code：COMPETING_EXPLANATIONS

- statement_status：theory_claim

- why_here_cn：为Figure 5分布证据提供理论预期。

- inherits_from_previous_cn：前文发现人类会改变决策规则。

- changes_argument_state_cn：把跟随行为解释为条件性而非盲目。

- sets_up_next_cn：为边界案例与特征差异分布可视化作铺垫。

- failure_if_removed_cn：对跟随率的解读缺少竞争机制。

- evidence_pointer：Section 5.2 P6-P7

### 8. Section 5.2 P8 S1-S2

- study_or_phase：5.2 closing group 8 result

- locator：Section 5.2 P8 S1-S2

- paraphrase_cn：组8却有不同结果：ATV shopping virtual等替代特征显著解释人类终决，而这些特征在独立决策比较中不显著，说明大信息量加解释促使评估员重新考虑初始决策。

- move_code：MECHANISM_RESULT_STEP2

- statement_status：empirical_result

- why_here_cn：给出再思考的关键证据。

- inherits_from_previous_cn：组7无解释对照结果。

- changes_argument_state_cn：把绩效改善与主动再思考直接连接。

- sets_up_next_cn：为5.3分解再思考过程作铺垫。

- failure_if_removed_cn：主动再思考主张无实证核心。

- evidence_pointer：Section 5.2 P8; Table 7

### 9. Section 5.3 P1 S1-S2

- study_or_phase：5.3 opening

- locator：Section 5.3 P1 S1-S2

- paraphrase_cn：前文观察到在大信息量加解释时人类重新考虑ATV shopping virtual这一双方独立时都不用的特征；我们推断这源于人类将其与游戏卡消费关联。

- move_code：MECHANISM_STEP3_OPENING

- statement_status：theory_claim

- why_here_cn：提出具体联想机制假设。

- inherits_from_previous_cn：组8替代特征显著性。

- changes_argument_state_cn：把抽象再思考具体化为特征关联。

- sets_up_next_cn：为特征分布证据作铺垫。

- failure_if_removed_cn：机制新意丧失。

- evidence_pointer：Section 5.3 P1

### 10. Section 5.3 P3 S1-S3

- study_or_phase：5.3 closing with C.4

- locator：Section 5.3 P3 S1-S3

- paraphrase_cn：在线附录C.4比较组7和组8的贷后表现，证明用更新规则的人类更可能正确选择机器拒绝的好贷款，而坚持旧规则则无改善；这为1+1>2提供绩效支点。

- move_code：MECHANISM_TO_PERFORMANCE_CLOSE

- statement_status：empirical_result

- why_here_cn：把机制结果与最终决策质量挂钩。

- inherits_from_previous_cn：特征关联机制已建立。

- changes_argument_state_cn：确认机制不仅改变行为也提升绩效。

- sets_up_next_cn：为6.1异质性扩展作铺垫。

- failure_if_removed_cn：机制发现与绩效脱节。

- evidence_pointer：Section 5.3 P3; Online Appendix C.4

### 11. Section 5.3 P4 S1-S2

- study_or_phase：5.3 closing synthesis

- locator：Section 5.3 P4 S1-S2

- paraphrase_cn：综合所有发现，合理设计唤醒人类主动再思考时，人机协作可实现1+1>2：机器负责边界案例，人类在感知到机器矛盾且受到信息线索启发时，通过主动再思考纠正随机案例中的机器错误。

- move_code：MECHANISM_SYNTHESIS

- statement_status：author_inference

- why_here_cn：把三个机制步骤整合成总命题。

- inherits_from_previous_cn：5.1-5.3全部发现。

- changes_argument_state_cn：把机制分析升华为协作分工主张。

- sets_up_next_cn：为Section 6扩展作铺垫。

- failure_if_removed_cn：机制部分没有结论。

- evidence_pointer：Section 5.3 P4

### 12. Section 6.1 P1 S1-S2

- study_or_phase：Section 6.1 opening with heterogeneity rationale

- locator：Section 6.1 P1 S1-S2

- paraphrase_cn：近期研究显示经验会改变对机器建议的接受与协作绩效，因此按工作月数分解评估员异质性。

- move_code：EXTENSION_OPENING

- statement_status：prior_literature

- why_here_cn：给异质性分析以文献依据。

- inherits_from_previous_cn：机制分析后需要边界检验。

- changes_argument_state_cn：把经验设定为调节因子。

- sets_up_next_cn：为三向交互模型作铺垫。

- failure_if_removed_cn：异质性分析无动机。

- evidence_pointer：Section 6.1 P1

### 13. Section 6.2 P1 S1-S3

- study_or_phase：Section 6.2 opening fairness question

- locator：Section 6.2 P1 S1-S3

- paraphrase_cn：表5显示若干主要变量与绩效相关且同时与性别相关，自然产生公平性问题：这种相关会影响不同性别借款人的贷款审批吗？

- move_code：FAIRNESS_OPENING

- statement_status：author_inference

- why_here_cn：把机制分析转向公平性扩展。

- inherits_from_previous_cn：ATV shopping virtual与性别相关。

- changes_argument_state_cn：引入性别偏差作为新结果维度。

- sets_up_next_cn：为组别非违约率与EOR分析作铺垫。

- failure_if_removed_cn：公平性贡献缺问题入口。

- evidence_pointer：Section 6.2 P1

### 14. Section 7.1 P1 S1-S4

- study_or_phase：Section 7.1 opening theory return

- locator：Section 7.1 P1 S1-S4

- paraphrase_cn：人机协作文献缺少人类何时能主动贡献和如何增值的系统理解；本文回到信息加工文献，用信息复杂度和有用外部线索两个前提，在小额贷款背景设置两个处理，并通过两阶段现场实验量化绩效。

- move_code：CONCLUSION_THEORY_RETurn

- statement_status：contribution_claim

- why_here_cn：讨论开头重述研究问题、理论与方法，闭合论证弧线。

- inherits_from_previous_cn：全文结果与机制已建立。

- changes_argument_state_cn：从实证升级为理论总结。

- sets_up_next_cn：为双条件缺一不可的讨论作铺垫。

- failure_if_removed_cn：讨论缺少全局回顾。

- evidence_pointer：Section 7.1 P1

### 15. Section 7.2 P1 S1

- study_or_phase：Section 7.2 opening implication

- locator：Section 7.2 P1 S1

- paraphrase_cn：基于独特实验设计，本研究为实践者提供非平凡启示。

- move_code：IMPLICATION_OPENING

- statement_status：contribution_claim

- why_here_cn：从理论返回转向管理启示。

- inherits_from_previous_cn：双条件结论已阐发。

- changes_argument_state_cn：把结果转化为实践建议。

- sets_up_next_cn：为成本-收益分析句作铺垫。

- failure_if_removed_cn：实践贡献缺开场。

- evidence_pointer：Section 7.2 P1

### 16. Section 7.3 P1 S1

- study_or_phase：Section 7.3 opening generalizability

- locator：Section 7.3 P1 S1

- paraphrase_cn：我们的理论驱动设计和实证发现可推广到任务目标不异常复杂或能清晰表述的其他情境。

- move_code：GENERALIZABILITY_OPENING

- statement_status：contribution_claim

- why_here_cn：界定外部效度范围。

- inherits_from_previous_cn：理论-设计一致性支撑迁移。

- changes_argument_state_cn：把结果从单个平台扩展到一类任务。

- sets_up_next_cn：为适用条件细节作铺垫。

- failure_if_removed_cn：外部效度主张缺失。

- evidence_pointer：Section 7.3 P1

### 17. Section 7.4 P1 S1

- study_or_phase：Section 7.4 opening limitations

- locator：Section 7.4 P1 S1

- paraphrase_cn：本文存在若干限制，为未来研究提供机会。

- move_code：LIMITATION_OPENING

- statement_status：contribution_claim

- why_here_cn：开启局限部分。

- inherits_from_previous_cn：所有贡献与边界讨论后。

- changes_argument_state_cn：明确研究边界与未来方向。

- sets_up_next_cn：为四条具体局限分述作铺垫。

- failure_if_removed_cn：学术诚信号召缺失。

- evidence_pointer：Section 7.4 P1

## 讨论与贡献逐句图谱

### 1. Section 7.1 P1 S1

- order：1

- locator：Section 7.1 P1 S1

- paraphrase_cn：人机协作文献缺乏对人类何时能主动贡献与如何增值的系统理解。

- move_code：GAP_RECAP

- statement_status：author_inference

- why_here_cn：讨论开头重述文献缺口。

- inherits_from_previous_cn：回到引言核心问题。

- changes_argument_state_cn：为本文贡献定位。

- sets_up_next_cn：为理论回顾句作铺垫。

- failure_if_removed_cn：讨论缺少问题锚点。

- evidence_pointer：Section 7.1 P1 S1

### 2. Section 7.1 P1 S2-S3

- order：2

- locator：Section 7.1 P1 S2-S3

- paraphrase_cn：我们回到信息加工文献，用信息复杂度和有用外部线索两个唤醒深思考的前提，并在小额贷款背景下设置信息量与机器解释两个处理。

- move_code：THEORY_RECAP

- statement_status：theory_claim

- why_here_cn：把理论-设计链条重述一遍。

- inherits_from_previous_cn：承接缺口重述。

- changes_argument_state_cn：将实证工作解释为理论的自然应用。

- sets_up_next_cn：为两阶段实验方法句作铺垫。

- failure_if_removed_cn：理论贡献缺重述。

- evidence_pointer：Section 7.1 P1 S2-S3

### 3. Section 7.1 P1 S4

- order：3

- locator：Section 7.1 P1 S4

- paraphrase_cn：独特的两阶段现场实验帮助我们明确量化相应绩效。

- move_code：METHOD_RECAP

- statement_status：method_decision

- why_here_cn：把方法作为独特证据来源。

- inherits_from_previous_cn：理论-设计陈述。

- changes_argument_state_cn：强调因果识别的可信度。

- sets_up_next_cn：为‘两条件均不可少’结论句作铺垫。

- failure_if_removed_cn：结论缺少证据来源说明。

- evidence_pointer：Section 7.1 P1 S4

### 4. Section 7.1 P2 S1

- order：4

- locator：Section 7.1 P2 S1

- paraphrase_cn：经验发现强调两个理论驱动条件的重要性和兼容性，显示两者缺一不可。

- move_code：CENTRAL_INTERPRETATION

- statement_status：contribution_claim

- why_here_cn：把实证结果提炼为理论命题。

- inherits_from_previous_cn：全部结果已报告。

- changes_argument_state_cn：从结果转为理论贡献。

- sets_up_next_cn：为‘第一，条件一单独无效’讨论作铺垫。

- failure_if_removed_cn：讨论没有核心论点。

- evidence_pointer：Section 7.1 P2 S1

### 5. Section 7.1 P2 S2-S3

- order：5

- locator：Section 7.1 P2 S2-S3

- paraphrase_cn：第一，虽然大信息量蕴含更多潜在知识，但人类倾向使用自己擅长的旧特征，因为学习有成本且即时反馈不确定；缺乏外部动机会阻碍人类接受机器建议，且坚持旧规则易导致欠适配决策。

- move_code：CONDITION1_DISCUSSION

- statement_status：author_inference

- why_here_cn：解释为何仅信息复杂度不足。

- inherits_from_previous_cn：由组1-2和组4-7比较推出。

- changes_argument_state_cn：把否定结果解释为学习成本与动机缺失。

- sets_up_next_cn：为条件二讨论作并列。

- failure_if_removed_cn：条件一单独无效的解释缺失。

- evidence_pointer：Section 7.1 P2 S2-S3

### 6. Section 7.1 P3 S1-S2

- order：6

- locator：Section 7.1 P3 S1-S2

- paraphrase_cn：第二，仅提供机器解释而无大信息量不能激发人类更多贡献，因为机器的优越预测受信息可得性限制；在有限信息上人类不可能比机器更聪明。

- move_code：CONDITION2_DISCUSSION

- statement_status：author_inference

- why_here_cn：解释为何仅解释不足。

- inherits_from_previous_cn：由组6-8比较推出。

- changes_argument_state_cn：把解释无效归因于机器自身受限。

- sets_up_next_cn：为近期相关文献对比句作铺垫。

- failure_if_removed_cn：条件二单独无效的解释缺失。

- evidence_pointer：Section 7.1 P3 S1-S2

### 7. Section 7.1 P3 S3-S5

- order：7

- locator：Section 7.1 P3 S3-S5

- paraphrase_cn：近期研究关注解释价值，但本文表明任务复杂性等权变因素影响解释效果；即使解释提供更多参考信息，若动机不足人类不会利用，反而会对边界贷款更多信任并跟随机器。

- move_code：LITERATURE_DIALOGUE

- statement_status：author_inference

- why_here_cn：把本文结果与现有机器解释文献对话。

- inherits_from_previous_cn：条件二讨论后。

- changes_argument_state_cn：把解释文献不一致归因于条件缺失。

- sets_up_next_cn：为双条件同时满足结论作铺垫。

- failure_if_removed_cn：解释文献贡献不清晰。

- evidence_pointer：Section 7.1 P3 S3-S5

### 8. Section 7.1 P4 S1-S2

- order：8

- locator：Section 7.1 P4 S1-S2

- paraphrase_cn：因此只有大信息量与机器解释同时存在，才能通过主动再思考使协作优于人类或机器单独执行，并进一步改善准确率与缓解机器有偏决策。

- move_code：CORE_THEORETICAL_CLAIM

- statement_status：contribution_claim

- why_here_cn：重申核心理论主张。

- inherits_from_previous_cn：两个条件单独无效讨论后。

- changes_argument_state_cn：把双条件从经验结果升华为理论贡献。

- sets_up_next_cn：为双加工理论推广句作铺垫。

- failure_if_removed_cn：全文核心主张悬空。

- evidence_pointer：Section 7.1 P4 S1-S2

### 9. Section 7.1 P4 S3

- order：9

- locator：Section 7.1 P4 S3

- paraphrase_cn：这证实将双加工理论从人类独立或人际决策推广到机器辅助情境是合理的。

- move_code：THEORY_EXTENSION

- statement_status：contribution_claim

- why_here_cn：给出理论贡献的明确主张。

- inherits_from_previous_cn：核心条件结论。

- changes_argument_state_cn：把机制发现升格为理论扩展。

- sets_up_next_cn：为7.2管理启示作铺垫。

- failure_if_removed_cn：理论贡献标签缺失。

- evidence_pointer：Section 7.1 P4 S3

### 10. Section 7.2 P1 S1-S2

- order：10

- locator：Section 7.2 P1 S1-S2

- paraphrase_cn：本研究为实践者提供非平凡启示，可指导公司在人力、数据购买/收集与AI技术采用之间的成本收益平衡。

- move_code：IMPLICATION_OPENING

- statement_status：contribution_claim

- why_here_cn：开启实践贡献。

- inherits_from_previous_cn：理论贡献已陈述。

- changes_argument_state_cn：把结果用于管理决策。

- sets_up_next_cn：为实验探测因素句作铺垫。

- failure_if_removed_cn：实践贡献缺开场。

- evidence_pointer：Section 7.2 P1 S1-S2

### 11. Section 7.2 P1 S3-S4

- order：11

- locator：Section 7.2 P1 S3-S4

- paraphrase_cn：我们的实验探测了多种可管理因素对协作效率的负面影响，并给出实证证据，同时对实践者偏爱大数据、AI技术与协作提出警示。

- move_code：IMPLICATION_DEVELOP

- statement_status：contribution_claim

- why_here_cn：强调实证证据对管理启示的支撑。

- inherits_from_previous_cn：成本收益句。

- changes_argument_state_cn：把管理建议建立在本实验证据上。

- sets_up_next_cn：为大数据情境建议作铺垫。

- failure_if_removed_cn：管理建议显得无证据。

- evidence_pointer：Section 7.2 P1 S3-S4

### 12. Section 7.2 P1 S5-S8

- order：12

- locator：Section 7.2 P1 S5-S8

- paraphrase_cn：如果大数据可得，协作可实现效率与公平兼得；但当员工感到AI威胁或过度主导时可能抵触或过度依赖，因此我们提供机器可解释性方案；若只有小数据，机器单独就足够，人类介入不能显著改善准确率或性别偏差。

- move_code：CONTINGENT_RECOMMENDATION

- statement_status：contribution_claim

- why_here_cn：给出依条件而变的管理建议。

- inherits_from_previous_cn：承接警示句。

- changes_argument_state_cn：把双条件结果转为可操作建议。

- sets_up_next_cn：为招聘与培训建议作铺垫。

- failure_if_removed_cn：管理建议缺乏条件性。

- evidence_pointer：Section 7.2 P1 S5-S8

### 13. Section 7.2 P2 S1-S3

- order：13

- locator：Section 7.2 P2 S1-S3

- paraphrase_cn：经验异质性显示有经验者更可能达到高协作绩效并修正机器偏差，但平台不应忽视培训，包括数据素养、及时反馈、伦理与偏见意识模块。

- move_code：IMPLICATION_HIRING_TRAINING

- statement_status：contribution_claim

- why_here_cn：把6.1结果转为人力资源建议。

- inherits_from_previous_cn：经验异质性证据。

- changes_argument_state_cn：扩展实践贡献至组织人力。

- sets_up_next_cn：为7.3可推广性作铺垫。

- failure_if_removed_cn：异质性结果无实践落地。

- evidence_pointer：Section 7.2 P2 S1-S3

### 14. Section 7.3 P1 S1-S3

- order：14

- locator：Section 7.3 P1 S1-S3

- paraphrase_cn：研究发现可推广到任务目标不过度复杂或可清晰表述、且能获取更多信息以增强绩效的情境，如候选人筛选、供应商评估和医疗决策。

- move_code：GENERALIZABILITY

- statement_status：contribution_claim

- why_here_cn：界定适用场景范围。

- inherits_from_previous_cn：理论-设计普适性。

- changes_argument_state_cn：把结果从微金融扩展到其他结构化决策任务。

- sets_up_next_cn：为机器一般优势句作铺垫。

- failure_if_removed_cn：外部效度主张缺失。

- evidence_pointer：Section 7.3 P1 S1-S3

### 15. Section 7.3 P1 S4-S5

- order：15

- locator：Section 7.3 P1 S4-S5

- paraphrase_cn：机器在结构化分类/预测问题上稳定优于人类；大信息量虽引起注意但不保证人类会帮忙，还需解释等额外线索引导人类再思考复杂信息。

- move_code：GENERAL_MACHINE_CLAIM

- statement_status：author_inference

- why_here_cn：重申机器优势与线索必要性。

- inherits_from_previous_cn：场景范围句后。

- changes_argument_state_cn：把结论上升到一般机制。

- sets_up_next_cn：为适用性前提讨论作铺垫。

- failure_if_removed_cn：可推广机制不完整。

- evidence_pointer：Section 7.3 P1 S4-S5

### 16. Section 7.3 P2 S1-S6

- order：16

- locator：Section 7.3 P2 S1-S6

- paraphrase_cn：但实际系统设计存在若干注意事项：人类需对决策绩效负责；人类能力应与协作绩效关联；算法必须适合任务且训练良好；新获取信息必须有内在价值；解释必须清晰有力；解释应便于比较、可理解并能刺激推理；员工AI知识与责任也与态度相关。

- move_code：CAVEAT_LIST

- statement_status：author_inference

- why_here_cn：为双条件结论附上边界前提。

- inherits_from_previous_cn：可推广性句后。

- changes_argument_state_cn：防止读者过度泛化。

- sets_up_next_cn：为上下文具体情境句作铺垫。

- failure_if_removed_cn：结论显得无条件普适。

- evidence_pointer：Section 7.3 P2 S1-S6

### 17. Section 7.3 P2 S7

- order：17

- locator：Section 7.3 P2 S7

- paraphrase_cn：在本研究中评估员对机器学习知识有限，薪酬结构也不鼓励其提升算法理解；在其他更懂AI且动机更强的环境中，对机器建议的反应可能不同。

- move_code：CONTEXT_CAVEAT

- statement_status：author_inference

- why_here_cn：进一步限定外部效度。

- inherits_from_previous_cn：员工知识态度前提。

- changes_argument_state_cn：承认结论对组织文化与能力敏感。

- sets_up_next_cn：为技术视角句作铺垫。

- failure_if_removed_cn：外部效度声明过度。

- evidence_pointer：Section 7.3 P2 S7

### 18. Section 7.3 P3 S1-S3

- order：18

- locator：Section 7.3 P3 S1-S3

- paraphrase_cn：技术视角上，本文处理不依赖特定可解释AI形式；只要提供清晰信号，都可能有价值；分析可外推到更先进AI技术。

- move_code：TECHNICAL_GENERALITY

- statement_status：contribution_claim

- why_here_cn：强调设计原则而非特定工具。

- inherits_from_previous_cn：情境限定后。

- changes_argument_state_cn：把SHAP结果提升为通用信号价值。

- sets_up_next_cn：为干预理论导向句作铺垫。

- failure_if_removed_cn：技术贡献显得局限于SHAP。

- evidence_pointer：Section 7.3 P3 S1-S3

### 19. Section 7.3 P4 S1-S3

- order：19

- locator：Section 7.3 P4 S1-S3

- paraphrase_cn：无法显式评估AI身份；结果不能区分效果来自机器/资深管理者的额外信息还是人类对AI的直接态度，但资深管理者真实表现可能不如机器稳定高效，且人类难以表达决策规则，机器却能提取特征重要性。

- move_code：AI_IDENTITY_CAVEAT

- statement_status：author_inference

- why_here_cn：承认AI身份混淆，同时用机器优势辩护。

- inherits_from_previous_cn：技术推广后。

- changes_argument_state_cn：为机器作为协作对象的合理性辩护。

- sets_up_next_cn：为两阶段设计讨论作铺垫。

- failure_if_removed_cn：AI身份混淆成为一个未回应威胁。

- evidence_pointer：Section 7.3 P4 S1-S3

### 20. Section 7.3 P5 S1-S4

- order：20

- locator：Section 7.3 P5 S1-S4

- paraphrase_cn：实验强调两阶段决策过程价值；但两阶段可能不可行，单阶段直接提供机器建议可能因缺少独立判断对比而导致过度依赖或不信任，并阻碍规则识别，尤其对低经验者。

- move_code：DESIGN_GENERALIZability

- statement_status：author_inference

- why_here_cn：把设计边界与实用性结合。

- inherits_from_previous_cn：AI身份讨论后。

- changes_argument_state_cn：提醒从两阶段到单阶段推广的损耗。

- sets_up_next_cn：为7.4局限作铺垫。

- failure_if_removed_cn：实践可应用性缺边界。

- evidence_pointer：Section 7.3 P5 S1-S4

### 21. Section 7.4 P1 S1-S4

- order：21

- locator：Section 7.4 P1 S1-S4

- paraphrase_cn：局限一：静态设计未考虑人类学习；未来可用强化学习模型研究人机相互学习。局限二：信息量为二元大/小，未来可探索连续信息复杂度。局限三：实验期仅一至两周，未来可延长观察长期动态。局限四：文化与行业差异可能影响结论，未来需跨行业跨国验证。

- move_code：LIMITATION_LIST

- statement_status：author_inference

- why_here_cn：系统列出边界与未来方向。

- inherits_from_previous_cn：全部贡献与边界讨论后。

- changes_argument_state_cn：以学术谦逊结束全文。

- sets_up_next_cn：无。

- failure_if_removed_cn：结论显得过于绝对。

- evidence_pointer：Section 7.4 P1-S4

## Study累积逻辑

### 1. 1

- study_or_phase：理论构建与预处理（Section 2.4, 3.2.1）

- evidence_job_cn：建立理论条件并转化为实验处理定义。

- what_it_establishes_cn：确立信息复杂度与机器解释是有理论依据的可操纵变量。

- what_it_cannot_establish_cn：不能证明该条件在现实中有效。

- why_next_phase_is_needed_cn：理论预测必须经真实行为检验。

- transition_wording_function_cn：Section 3.2.1 直接把两个条件称为处理，并进入模型与解释准备。

### 2. 2

- study_or_phase：机器与人类准备（Section 3.2.2）

- evidence_job_cn：生成高质量、稳定、可解释的机器建议与训练完备的人类评估员。

- what_it_establishes_cn：机器基线可信且XGBoost表现最佳；人类在两种信息量下达到稳定评估。

- what_it_cannot_establish_cn：不能证明协作能改善绩效。

- why_next_phase_is_needed_cn：需要随机化组间比较来识别因果效果。

- transition_wording_function_cn：模型与解释就绪后进入两阶段实验设计。

### 3. 3

- study_or_phase：Stage 1 纯人类与纯机器基线（Section 3.3.1, 4）

- evidence_job_cn：比较人类与机器在两种信息量下的独立决策绩效。

- what_it_establishes_cn：机器在大信息量下优于人类且差距扩大；小信息量下机器略优。

- what_it_cannot_establish_cn：不能说明协作能否让人类贡献额外价值。

- why_next_phase_is_needed_cn：需要Stage 2两步流程分离人类增量贡献。

- transition_wording_function_cn：Stage 2在同平台引入机器建议与解释，直接检验协作效果。

### 4. 4

- study_or_phase：Stage 2 人机协作且有/无解释（Section 3.3.2, 4）

- evidence_job_cn：检验信息复杂度与机器解释各自及联合对协作绩效的影响。

- what_it_establishes_cn：只有大信息量+解释时人类参与显著降低违约率；缺失任一条件改善消失。

- what_it_cannot_establish_cn：不能揭示人类如何实现改善。

- why_next_phase_is_needed_cn：需要打开黑箱解释绩效差异来源。

- transition_wording_function_cn：Section 4末尾从绩效转向行为分解，Section 5开头给出三步机制框架。

### 5. 5

- study_or_phase：机制第一步：人与机特征差异（Section 5.1）

- evidence_job_cn：证明独立决策时人类与机器的特征使用差异解释绩效差距。

- what_it_establishes_cn：小信息量两者特征相似；大信息量人类坚持传统特征、机器使用新特征。

- what_it_cannot_establish_cn：不能说明协作中人类是否改变。

- why_next_phase_is_needed_cn：需要检验协作中人类对机器建议的反应。

- transition_wording_function_cn：5.2开头用‘接下来解开协作中的行为机制’承接。

### 6. 6

- study_or_phase：机制第二步：分歧与跟随（Section 5.2）

- evidence_job_cn：证明在双条件满足时人类终决使用新特征，体现主动再思考。

- what_it_establishes_cn：组8中ATV shopping virtual、Gender等替代特征解释终决变化；其他组仍用原有特征。

- what_it_cannot_establish_cn：不能具体说明人类为何选择该新特征。

- why_next_phase_is_needed_cn：需要分解再思考的具体联想路径。

- transition_wording_function_cn：5.3开头提出特征关联假设并检验。

### 7. 7

- study_or_phase：机制第三步：再思考分解与决策质量（Section 5.3, Online C.4）

- evidence_job_cn：把主动再思考落实为特征关联过程，并与绩效改善连接。

- what_it_establishes_cn：人类因游戏卡消费零值密集而转用相关虚拟商品消费特征，并用其正确选择机器拒绝的好贷款。

- what_it_cannot_establish_cn：不能证明该联想在所有人群或任务中都普遍发生。

- why_next_phase_is_needed_cn：需要检验个体差异与公平性以扩展边界和意义。

- transition_wording_function_cn：5.3结尾以‘合理设计唤醒主动再思考可实现1+1>2’过渡到扩展分析。

### 8. 8

- study_or_phase：扩展：经验异质性与性别公平（Section 6）

- evidence_job_cn：检验机制的条件性（谁更受益）与公平性（是否纠正机器偏差）。

- what_it_establishes_cn：经验丰富者在双条件下更可能再思考；大信息量机器有性别偏好，人类加解释降低EOR。

- what_it_cannot_establish_cn：不能证明在非小微金融领域同样成立。

- why_next_phase_is_needed_cn：需要总括贡献、可推广边界与局限。

- transition_wording_function_cn：Section 7.1 开头重述问题与理论，把证据升级为理论结论。

## 主张—证据台账

### 1. 大信息量下机器单独决策优于人类，且差距扩大。

- claim_cn：大信息量下机器单独决策优于人类，且差距扩大。

- claim_level：empirical

- supporting_evidence_cn：Table 2 比较B（H&S vs M&S）、D（H&L vs M&L）均显著。

- support_strength：direct

- where_claim_is_made：Section 4 P2；Introduction P8 S1

- where_evidence_is_provided：Table 2; Figure 3

### 2. 单独信息复杂度或单独机器解释都不能带来协作增益。

- claim_cn：单独信息复杂度或单独机器解释都不能带来协作增益。

- claim_level：empirical

- supporting_evidence_cn：比较G/H（小信息量有无解释 vs 机器）与I（大信息量无解释 vs 机器）不显著；E不显著。

- support_strength：direct

- where_claim_is_made：Section 4 P3；Introduction P8 S3

- where_evidence_is_provided：Table 2 比较E/G/H/I

### 3. 大信息量与机器解释同时存在时，人类参与显著降低违约率，实现1+1>2。

- claim_cn：大信息量与机器解释同时存在时，人类参与显著降低违约率，实现1+1>2。

- claim_level：empirical

- supporting_evidence_cn：Table 2 比较J：组4 vs 组8，默认率5.15%降至3.13%，差2.02%，p=0.0071。

- support_strength：direct

- where_claim_is_made：Abstract S10；Introduction P8 S2；Section 4 P3

- where_evidence_is_provided：Table 2 比较J; Figure 3

### 4. 大信息量下人类坚持传统特征而机器使用新特征，解释机器优势。

- claim_cn：大信息量下人类坚持传统特征而机器使用新特征，解释机器优势。

- claim_level：mechanism

- supporting_evidence_cn：Tables 3-4 的MInd交互项显示人类仅新增#Outgoing contacts，机器使用游戏卡、轨迹等；表5相关分析。

- support_strength：direct

- where_claim_is_made：Section 5.1 P5；Introduction P9 S2

- where_evidence_is_provided：Tables 3-4; Section 5.1

### 5. 只有在大信息量加解释时，人类终决才会采用此前双方都不用的新特征。

- claim_cn：只有在大信息量加解释时，人类终决才会采用此前双方都不用的新特征。

- claim_level：mechanism

- supporting_evidence_cn：Table 7模型3/4中ATV shopping virtual和Gender交互项在组8显著，组7不显著。

- support_strength：direct

- where_claim_is_made：Section 5.2 P8；Introduction P9 S3

- where_evidence_is_provided：Table 7

### 6. 人类把机器解释中的非熟悉特征（游戏卡）关联到相关新特征（ATV虚拟购物），形成再思考。

- claim_cn：人类把机器解释中的非熟悉特征（游戏卡）关联到相关新特征（ATV虚拟购物），形成再思考。

- claim_level：mechanism

- supporting_evidence_cn：游戏卡特征中位数为零而ATV shopping virtual中位数为8.70；在线C.4显示新特征与违约显著相关且人类能用于选好贷款。

- support_strength：partial

- where_claim_is_made：Section 5.3 P1-P2

- where_evidence_is_provided：Online Figure A.1; Online Appendix C.4; Table 5

### 7. 经验丰富的评估员更少跟随机器，但在双条件下会启动再思考并改善风险。

- claim_cn：经验丰富的评估员更少跟随机器，但在双条件下会启动再思考并改善风险。

- claim_level：boundary

- supporting_evidence_cn：Table 8 三向交互L×Expl×Work=3/4在IfDefault回归中显著为负；Model 4中高经验在大信息量下更少跟随。

- support_strength：direct

- where_claim_is_made：Section 6.1 P3；Introduction P10 S1

- where_evidence_is_provided：Table 8; Online Appendix D.2

### 8. 人机协作在大信息量加解释时缩小机器产生的性别偏差。

- claim_cn：人机协作在大信息量加解释时缩小机器产生的性别偏差。

- claim_level：boundary

- supporting_evidence_cn：EOR从机器大信息量组1.201降至组8的1.056，接近公平；非默认率性别差缩小。

- support_strength：direct

- where_claim_is_made：Section 6.2 P3；Introduction P10 S2

- where_evidence_is_provided：Figure 6; Online Table D.5

### 9. 双加工理论可推广到人机协作情境。

- claim_cn：双加工理论可推广到人机协作情境。

- claim_level：theory

- supporting_evidence_cn：双条件联合效应的显著性加上机制分析中的再思考证据。

- support_strength：partial

- where_claim_is_made：Section 7.1 P4 S3

- where_evidence_is_provided：Section 4; Section 5; Section 6

### 10. 机器解释效果依赖信息复杂度，解释文献不一致源于条件缺失。

- claim_cn：机器解释效果依赖信息复杂度，解释文献不一致源于条件缺失。

- claim_level：theory

- supporting_evidence_cn：Table 2中解释单独无效果、信息量大且有解释才有效。

- support_strength：direct

- where_claim_is_made：Introduction P11 S3；Section 7.1 P3

- where_evidence_is_provided：Table 2; Figure 3

## ISR定位逻辑

- constitutive_is_problem_cn：问题不是一个纯CS或HCI可用性问题，而是数字技术（机器学习建议与解释）如何与人类认知、组织决策和市场信贷结果互相构成：机器解释的效果取决于人类面对的信息复杂度，人类再思考弥补机器预测偏差，最终改变信贷违约率与性别公平。

- technology_behavior_or_market_entanglement_cn：技术设计（SHAP解释、信息量）不是可随意替换的工具，而是通过改变人类系统2加工概率来发挥影响；人类行为又反过来纠正技术（机器）的算法性性别偏差，形成技术-认知-市场三重纠缠。

- role_of_benchmark_or_objective_evidence_cn：违约率、EOR、跟随率等客观现场结果被用来支持‘人类贡献不能被机器替代’这一IS主张，说明技术设计只有当其能激活人类独特认知过程时才产生组织与市场价值。

- theory_in_design_cn：理论不是事后解释结果，而是事先进入设计：双加工理论的两个条件直接决定实验处理（信息量与机器解释）的构造与组别；机制分析又回到理论构念（rethinking）打开行为过程。

- technical_vs_is_contribution_balance_cn：技术部分（XGBoost、SHAP）只作为工具准备出现，篇幅短；主要篇幅放在条件、人机行为机制、绩效与公平上，确保文章是IS研究而非机器学习论文。

- beyond_transient_performance_cn：贡献不只是一时的违约率下降2.02%，而是识别出解释文献不一致的条件性原因、人类再思考机制以及人类纠正机器性别偏差的不可替代价值，从而形成可迁移的设计知识。

## 段落级仿写模板

### abstract_steps

1. 第一句：用数据与AI时代背景引发普遍性。

2. 第二句：从背景转入信息处理难题与总问题。

3. 第三句：简述已有方案（机器解释）与其不一致结论。

4. 第四句：明确本文目标（两条件联合影响）。

5. 第五句：说明方法（现场实验与理论驱动操纵）。

6. 第六句：给出核心结果（只有双条件同时满足才有效）。

7. 第七句：预告机制与公平发现。

8. 第八句：声明理论与实践贡献。

### introduction_paragraph_steps

1. P1：背景→互补性→人类深度思考，建立潜力。

2. P2：现实约束→厌恶/依赖→设计风险，制造落差。

3. P3：已有方案→条件/机制缺口→非普遍有效，构造缺口。

4. P4：提出权变变量→双条件命题→两个机制→联合预测，给出理论。

5. P5：批评实验室→需要现场实验→说明匹配性，选择方法。

6. P6：总问题→三个RQ→结构路线图。

7. P7：领域与平台→理论依据→三个操纵，预告设计。

8. P8：否定结果→正向结果→条件缺失无效→跟随行为，预览结果。

9. P9：三步机制预告，建立过程证据。

10. P10：异质性→公平性→价值升级。

11. P11：三点贡献面向三条文献流。

### theory_to_design_steps

1. 先综述三类文献并各建一个缺口子项。

2. 引入理论框架（双加工），给出系统1/系统2定义。

3. 分两步推导条件：任务/信息复杂度→注意与参与；有用线索→重估与推理。

4. 把条件翻译成具体设计：丰富信息与结构化机器解释。

5. 定义核心机制构念（rethinking）并为实证检验提供概念目标。

### method_and_study_sequence_steps

1. 先描述平台与审批流程，说明为什么适合做因果实验。

2. 再报告处理定义与机器/人类准备，确保所有输入可信。

3. 用Stage 1比较纯人类/纯机器基线。

4. 用Stage 2的两步决策分离人类初始与终决，识别增量贡献。

5. 报告随机化检查，为因果推断奠基。

### results_reporting_steps

1. 先定义因变量并给出组间比较程序（t检验、多重假设校正）。

2. 按‘条件一单独无效→条件二单独无效→双条件联合有效’的顺序报告主结果。

3. 补充行为证据（一致率与跟随率）。

4. 转入三步机制：特征差异→协作中再思考→具体联想。

5. 再补异质性与公平性扩展，扩大结果意义。

### discussion_and_contribution_steps

1. 重述问题、理论与方法，闭合循环。

2. 分别讨论两个条件单独无效的原因。

3. 重申双条件联合命题并把结果升华为理论推广。

4. 给出依条件的管理建议。

5. 界定可推广情境并列出权变前提。

6. 承认AI身份与设计边界。

7. 列出局限与未来方向。

## 可执行写作算法

### 1. 1

- step：1

- rhetorical_job_cn：用数据/AI时代背景开场，说明人机协作普遍性。

- research_evidence_required_cn：行业报告或代表性文献证明AI协作已成为现实。

- sentence_pattern_function_cn：背景句建立普遍性，为后续问题提供舞台。

- transition_condition_cn：当读者承认协作普遍后，进入互补性。

### 2. 2

- step：2

- rhetorical_job_cn：建立机器与人类各自优势的互补性。

- research_evidence_required_cn：有关机器统计优势与人类灵活性/稀有案例优势的文献。

- sentence_pattern_function_cn：‘机器强在X，人类强在Y’式对照，为1+1>2设伏。

- transition_condition_cn：当互补性确立后，用‘然而’转入现实障碍。

### 3. 3

- step：3

- rhetorical_job_cn：描述现实协作失败（厌恶/过度依赖/过度谨慎）。

- research_evidence_required_cn：算法厌恶、过度依赖、人为介入造成绩效下降的实证文献。

- sentence_pattern_function_cn：‘虽有可能，但现实中因……绩效低于预期’产生张力。

- transition_condition_cn：当读者意识到问题后，引入已有解决方案。

### 4. 4

- step：4

- rhetorical_job_cn：综述已有方案（机器解释）并指出条件/机制缺口。

- research_evidence_required_cn：机器解释文献，尤其结论不一致的证据。

- sentence_pattern_function_cn：‘研究者转向X，但……并不总是有效，条件机制未知’。

- transition_condition_cn：当缺口明确后，提出自己的理论变量。

### 5. 5

- step：5

- rhetorical_job_cn：引入理论并推导出两个必要条件。

- research_evidence_required_cn：理论文献能将任务复杂性/信息复杂度与有用线索连接到深度思考。

- sentence_pattern_function_cn：‘理论提出两个前提：一是……，二是……’。

- transition_condition_cn：当两条件可操作化后，转入实验设计。

### 6. 6

- step：6

- rhetorical_job_cn：说明为什么需要现场实验而非实验室。

- research_evidence_required_cn：关于实验室行为失真的文献或论证。

- sentence_pattern_function_cn：‘由于被试在实验室表现不同，需要现场实验’。

- transition_condition_cn：当方法论证充分后，列出RQ。

### 7. 7

- step：7

- rhetorical_job_cn：用三个RQ组织论文结构。

- research_evidence_required_cn：无需新证据，只需把问题拆成绩效、机制、异质性。

- sentence_pattern_function_cn：‘研究问题：(1)……(2)……(3)……’。

- transition_condition_cn：当RQ列出后，进入领域与实验概述。

### 8. 8

- step：8

- rhetorical_job_cn：描述实验平台、处理、组别与随机化。

- research_evidence_required_cn：真实平台允许随机分组、固定审批率、跟踪还款。

- sentence_pattern_function_cn：‘我们与合作方……随机分配……保持审批率……’。

- transition_condition_cn：当设计描述完并确认随机化成功，才可报告结果。

### 9. 9

- step：9

- rhetorical_job_cn：按条件必要性顺序报告主结果。

- research_evidence_required_cn：组间默认率比较、p值与效应量。

- sentence_pattern_function_cn：‘首先，单独A无效；其次，单独B无效；只有当A与B同时存在……’。

- transition_condition_cn：当绩效结果讲清后，明确其需要机制解释。

### 10. 10

- step：10

- rhetorical_job_cn：用多步机制分析打开决策黑箱。

- research_evidence_required_cn：回归交互项、特征分布、线上附录补充分析能显示决策规则变化。

- sentence_pattern_function_cn：‘第一步……第二步……第三步……’，每步都落到证据。

- transition_condition_cn：当机制证据链完整后，才可升华为理论贡献。

### 11. 11

- step：11

- rhetorical_job_cn：用异质性与公平性扩展边界与意义。

- research_evidence_required_cn：经验交互项与EOR/fairness指标。

- sentence_pattern_function_cn：‘进一步，我们检验谁更受益以及是否纠正偏差’。

- transition_condition_cn：当扩展分析完成后，进入讨论。

### 12. 12

- step：12

- rhetorical_job_cn：讨论中返回理论，明确贡献、可推广性、边界与局限。

- research_evidence_required_cn：不需要新数据，但所有主张都要能回溯到前面证据。

- sentence_pattern_function_cn：‘我们的发现证明……因此……但需要注意……’。

- transition_condition_cn：当四类讨论（理论、实践、可推广、局限）完成后，文章自然收束。

## 应模仿的高价值动作

1. 把两个理论条件直接转化为2×2实验处理，并用‘缺失任一条件效果消失’组织结果，替代单变量主效应的平庸叙事。

2. 两阶段实验设计：先独立决策后看机器建议再终决，从而能分离人类独立贡献与跟随效应。

3. 对核心机制不是只给绩效结果，而是用特征重要性的probit交互项打开决策规则变化。

4. 将‘重新思考’操作化为可检验的特征关联现象（如非熟悉特征零值过多→转向相关新特征）。

5. 同时用绩效结果（违约率）和行为结果（跟随率）两条证据线支撑同一结论。

6. 用最相近文献（Bauer et al.）做显式对照，把信息复杂度与现场实验作为差异点。

7. 在讨论中用‘两个条件缺一不可’把结果重新抽象为理论命题，并声称双加工理论的推广。

8. 把公平性（EOR）作为人类价值的额外证据，使贡献超越纯绩效优化。

## 不要只复制的表面动作

1. 不要照搬‘1+1>2’口号式标题；必须要有对应的交互效应。

2. 不要在没有交互显著或固定审批率的情况下重复‘缺一不可’。

3. 不要只是展示SHAP界面；必须解释界面为什么符合‘有用线索’的理论条件。

4. 不要用‘主动思考’标签掩盖缺乏过程数据的事实；至少要有特征权重变化或跟随行为证据。

5. 不要在没有分组随机化检查时声称现场实验因果。

6. 不要用‘大数据一定更好’或‘解释一定更好’；本文的关键恰是条件性。

## 证据薄弱或跳跃的动作

1. ‘人类自发将游戏卡消费关联到ATV虚拟购物’主要是事后分布推断，缺少直接测量人类联想过程的证据。

2. 经验异质性三向交互分析在小样本分层下可能不够稳健。

3. EOR计算基于获批贷款的非违约率，存在选择样本限制，对公平性结论的稳健性仍需线上附录支持。

4. 无法分离AI身份（机器建议 vs 资深管理者建议），作者用‘机器稳定性和可解释性’辩护，但这是陈述而非实验证据。

5. 单一SHAP解释方式不能完全支撑‘任何清晰信号都有效’的推广。

## 一句话套路

先用双加工理论推导出两个必须同时满足的条件，再到真实小微金融平台用两阶段现场实验操纵两者组合，再以三步机制分析证明绩效改善来自人类主动再思考，最后以异质性和性别公平性扩展证明人类贡献不可替代并返回理论提出可迁移设计知识。

## 分析边界

在线附录C/D只以引用形式出现，无法逐表核实稳健性检验；Figure 1/2/5等图像内容依赖图片说明而非像素级阅读；Table 7注脚在OCR中出现移位，但主要回归系数仍可读；对‘再思考’机制的解释依赖作者对回归和特征分布的叙述，可能受作者意图影响。
