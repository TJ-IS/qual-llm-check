# Designing Personalized Treatment Plans for Breast Cancer：ISR 句段级微观图谱

- 作者：Wei Chen; Yixin Lu; Liangfei Qiu; Subodha Kumar
- 年份：2021
- DOI：10.1287/isre.2021.1002
- 源文件：28168_2021_designing-personalized-treatment-plans-for-breast-cancer.md
- 置信度：0.88

## 核实后的宏观骨架

结构：摘要（背景—设计—结果—贡献）；引言（负担—临床现象与缺口—RQ与框架—评价与关键结果—三大贡献—预告结构）；2.研究背景（2.1医疗预测分析、2.2个性化医学、2.3放疗计划与剂量绘画）；3.框架（临床需求→设计科学→预测模型TCP→MTC建模→Bayesian估计→验证→优化模型→群组/个体计划→Adam算法）；4.评价（4.1基准评价：群组/个体剂量比较；4.2附加算法评价；4.3经济效益）；5.讨论（贡献、实践含义、局限与未来）。

## 摘要逐句图谱

### 1. Abstract P1 S1

- order：1

- locator：Abstract P1 S1

- paraphrase_cn：乳腺癌仍是全球女性癌症死亡的首要原因。

- move_code：CONTEXT

- statement_status：fact

- why_here_cn：用最权威的疾病负担数据开启文章，为全文定下临床重要性基调。

- inherits_from_previous_cn：无前文，直接建立背景。

- changes_argument_state_cn：把读者注意力锁定在乳腺癌这一重大healthcare问题上，使其后提出的框架有意义。

- sets_up_next_cn：为第二句治疗复杂性提供疾病背景。

- failure_if_removed_cn：摘要缺乏现实紧迫性，读者不会理解为何需要新框架。

- evidence_pointer：Abstract P1

### 2. Abstract P1 S2

- order：2

- locator：Abstract P1 S2

- paraphrase_cn：当代乳腺癌治疗复杂，需要高度专业的医疗人员在系列信息密集流程中协作。

- move_code：CONTEXT_AND_PROBLEM_COMPLEXITY

- statement_status：fact

- why_here_cn：从疾病负担转向治疗过程本身的复杂性，为个性化困难做铺垫。

- inherits_from_previous_cn：承接乳腺癌常见性。

- changes_argument_state_cn：指出治疗不只是单一技术问题，而是信息密集型协作流程，暗示IS研究切入点。

- sets_up_next_cn：为个性化治疗计划挑战做前提。

- failure_if_removed_cn：个性化挑战失去信息与协作基础。

- evidence_pointer：Abstract P1 S2

### 3. Abstract P1 S3

- order：3

- locator：Abstract P1 S3

- paraphrase_cn：这种复杂性对制定最适合个体的治疗计划构成重大挑战。

- move_code：PROBLEM_STATEMENT

- statement_status：author_inference

- why_here_cn：将前两句自然景观转化为研究问题空间：个性化计划为何困难。

- inherits_from_previous_cn：承接治疗复杂性和信息密集流程。

- changes_argument_state_cn：把临床复杂性转化为研究目标：需要个性化治疗计划。

- sets_up_next_cn：为设计科学框架提出做铺垫。

- failure_if_removed_cn：摘要中缺少个性化问题，框架没有直接目标。

- evidence_pointer：Abstract P1 S3

### 4. Abstract P2 S1前半

- order：4

- locator：Abstract P2 S1前半

- paraphrase_cn：本研究遵循信息系统设计科学范式，提出一个用于早期乳腺癌放疗治疗计划决策支持的新框架。

- move_code：METHOD_PARADIGM_AND_ARTIFACT_INTRO

- statement_status：author_inference

- why_here_cn：明确方法范式（设计科学）与研究对象（放疗决策支持），把研究定位为IS设计科学，而非普通临床预测。

- inherits_from_previous_cn：回应前句个性化挑战。

- changes_argument_state_cn：从问题转向方案，宣称采用规范方法论。

- sets_up_next_cn：为下一句制品构成做引导。

- failure_if_removed_cn：摘要没有方法论定位，读者会误以为只是预测模型论文。

- evidence_pointer：Abstract P2 S1

### 5. Abstract P2 S1后半

- order：5

- locator：Abstract P2 S1后半

- paraphrase_cn：框架核心由预测模型和优化模型组成：前者基于临床和患者特征预测治疗结果，后者基于不同计划的预测结果优化治疗计划。

- move_code：DESIGN_FEATURE

- statement_status：design_decision

- why_here_cn：一句话概括制品架构，让读者立即知道框架为何能做个性化。

- inherits_from_previous_cn：承接新框架。

- changes_argument_state_cn：把抽象“决策支持”具体化为可计算的预测+优化循环。

- sets_up_next_cn：为摘要中的评价结果铺垫必要性：既然有制品，就需要证明有效。

- failure_if_removed_cn：读者不知道框架做什么，后续结果没有载体。

- evidence_pointer：Abstract P2 S1

### 6. Abstract P2 S2

- order：6

- locator：Abstract P2 S2

- paraphrase_cn：通过一系列仿真实验，框架生成的计划在平衡局部复发风险与放疗不良反应方面一致优于现有实践，并降低相关治疗成本。

- move_code：RESULT

- statement_status：empirical_result

- why_here_cn：给出评价结果与性能声明，直接回应框架设计价值。

- inherits_from_previous_cn：承接框架构成，说明经实验验证。

- changes_argument_state_cn：从“提出了框架”推进到“有证据表明框架更优”。

- sets_up_next_cn：为贡献声明提供证据基础。

- failure_if_removed_cn：摘要缺少核心实证声明，贡献缺乏支撑。

- evidence_pointer：Abstract P2 S2

### 7. Abstract P3 S1

- order：7

- locator：Abstract P3 S1

- paraphrase_cn：研究贡献于关于医疗信息技术在提供成本有效医疗方面潜力的文献，并通过提供有实际价值的模型和工具贡献于临床实践。

- move_code：CONTRIBUTION

- statement_status：contribution_claim

- why_here_cn：把研究意义提升到HIT文献与实践两个层面，完成摘要叙事闭环。

- inherits_from_previous_cn：承接结果与框架。

- changes_argument_state_cn：把具体仿真结果升级为领域层面贡献。

- sets_up_next_cn：为引言中的三大贡献提供浓缩版。

- failure_if_removed_cn：摘要缺少对IS文献与实践的回扣，研究意义不显。

- evidence_pointer：Abstract P3 S1

## 引言逐句图谱

### 1. Introduction P1 S1

- order：1

- locator：Introduction P1 S1

- paraphrase_cn：乳腺癌是全球女性中最常被诊断的癌症。

- move_code：CONTEXT

- statement_status：fact

- why_here_cn：开篇用全球最常见癌症定调，为现实负担提供第一层证据。

- inherits_from_previous_cn：无，作为引言起点。

- changes_argument_state_cn：建立疾病重要性。

- sets_up_next_cn：为其后美国数据和成本数据做铺垫。

- failure_if_removed_cn：引言失去现实重要性起点。

- evidence_pointer：Introduction P1 S1

### 2. Introduction P1 S2

- order：2

- locator：Introduction P1 S2

- paraphrase_cn：仅美国就有超过350万女性在2020年前被诊断为乳腺癌。

- move_code：CONTEXT_MAGNITUDE

- statement_status：fact

- why_here_cn：用具体患者数放大疾病负担，让读者感到规模。

- inherits_from_previous_cn：承接全球最常见癌症。

- changes_argument_state_cn：把疾病框架从全球缩小到美国并给出体量。

- sets_up_next_cn：引出经济影响。

- failure_if_removed_cn：疾病负担缺少规模感。

- evidence_pointer：Introduction P1 S2

### 3. Introduction P1 S3

- order：3

- locator：Introduction P1 S3

- paraphrase_cn：负担不仅来自生命损失，也来自巨大经济影响；据Forbes报道，乳腺癌治疗费用2020年预计达165亿美元。

- move_code：ECONOMIC_CONTEXT

- statement_status：fact

- why_here_cn：引入经济成本，为后文成本节约贡献埋伏笔。

- inherits_from_previous_cn：承接患者数，把数量转成费用。

- changes_argument_state_cn：建立研究的经济重要性，把临床问题与医疗成本连接。

- sets_up_next_cn：为后续“降低成本”的目标提供动机。

- failure_if_removed_cn：引言缺少经济维度，后文成本节约sentence失去根基。

- evidence_pointer：Introduction P1 S3

### 4. Introduction P2 S1

- order：4

- locator：Introduction P2 S1

- paraphrase_cn：目前大多数早期乳腺癌患者在术后接受放疗以降低局部复发风险。

- move_code：CLINICAL_PRACTICE

- statement_status：fact

- why_here_cn：转向治疗环节，指明目标领域是放疗计划。

- inherits_from_previous_cn：承接乳腺癌治疗背景。

- changes_argument_state_cn：将问题从整体乳腺癌治疗聚焦到放疗，建立文章具体场景。

- sets_up_next_cn：为其后论放疗计划的挑战做铺垫。

- failure_if_removed_cn：读者不知道研究对象是放疗计划。

- evidence_pointer：Introduction P2 S1

### 5. Introduction P2 S2

- order：5

- locator：Introduction P2 S2

- paraphrase_cn：尽管放疗总体目标明确，即靶向肿瘤细胞同时保护周围正常细胞和风险器官，但治疗轨迹中临床和非临床因素的复杂交互（引用Valdes et al. 2017）给个体治疗计划优化带来巨大挑战。

- move_code：PHENOMENON_AND_COMPLEXITY

- statement_status：author_inference

- why_here_cn：说明放疗目标看似简单但实际操作困难，为“需要系统决策支持”建立必要性。

- inherits_from_previous_cn：承接放疗应用。

- changes_argument_state_cn：把放疗引入为“复杂优化问题”。

- sets_up_next_cn：引出医生依赖经验和知识这一现状。

- failure_if_removed_cn：放疗计划优化的困难未被解释，后文问题无效。

- evidence_pointer：Introduction P2 S2

### 6. Introduction P2 S3

- order：6

- locator：Introduction P2 S3

- paraphrase_cn：医生依靠领域知识和经验做治疗计划决策。

- move_code：CURRENT_PRACTICE

- statement_status：fact

- why_here_cn：指出现状依赖医生经验，为质疑经验式计划有效性做铺垫。

- inherits_from_previous_cn：承接优化困难。

- changes_argument_state_cn：说明实际决策并非基于系统量化，而是经验驱动。

- sets_up_next_cn：引出问题：经验式计划对个体是否有效。

- failure_if_removed_cn：缺乏对现状的描述，后文问题没有对象。

- evidence_pointer：Introduction P2 S3

### 7. Introduction P2 S4

- order：7

- locator：Introduction P2 S4

- paraphrase_cn：这引出一个问题：知识驱动或经验式治疗计划在多大程度上对个体患者有效？

- move_code：RESEARCH_GAP_QUESTION

- statement_status：author_inference

- why_here_cn：把现状转化为研究缺口，指出经验式计划缺乏系统性检验。

- inherits_from_previous_cn：承接医生依赖经验。

- changes_argument_state_cn：由描述现状转向提出待研究问题。

- sets_up_next_cn：为其后正式RQ做台阶；先给问题再给正式RQ。

- failure_if_removed_cn：引言缺乏第一步问题，正式RQ显得突兀。

- evidence_pointer：Introduction P2 S4

### 8. Introduction P2 S5

- order：8

- locator：Introduction P2 S5

- paraphrase_cn：近期研究还报道，接受常规放疗的患者患肺癌和心脏病的风险更高（Darby et al. 2013, Grantzau et al. 2014）。

- move_code：EVIDENCE_OF_HARM

- statement_status：prior_literature

- why_here_cn：给问题增加实证证据：经验式常规计划不仅可能无效，还可能造成伤害。

- inherits_from_previous_cn：承接经验式计划有效性疑问。

- changes_argument_state_cn：把“可能无效”推进为“可测量的伤害风险”，为框架目标提供直接动机。

- sets_up_next_cn：为正文中剂量-反应经济分析埋下文献引用。

- failure_if_removed_cn：缺乏风险证据，研究动机弱化。

- evidence_pointer：Introduction P2 S5

### 9. Introduction P3 S1

- order：9

- locator：Introduction P3 S1

- paraphrase_cn：本研究关注放疗计划中的研究问题：如何纳入患者特异性信息预测治疗结果并适应个体患者的治疗计划？

- move_code：RQ

- statement_status：author_inference

- why_here_cn：正式提出量化研究问题，把前文现象转化成可研究问题。

- inherits_from_previous_cn：承接经验计划有效性和风险证据。

- changes_argument_state_cn：明确研究目标：个性化预测+调整计划。

- sets_up_next_cn：引出框架方法。

- failure_if_removed_cn：全文失去正式RQ。

- evidence_pointer：Introduction P3 S1

### 10. Introduction P3 S2

- order：10

- locator：Introduction P3 S2

- paraphrase_cn：为回答问题，作者遵循IS设计科学范式（Hevner et al. 2004），提出用于个体患者放疗计划决策支持的新框架。

- move_code：METHOD_PARADIGM

- statement_status：author_inference

- why_here_cn：宣布方法论框架，显示并非单纯建模，而是IS设计科学制品。

- inherits_from_previous_cn：承接RQ。

- changes_argument_state_cn：从问题转向解决方案类型。

- sets_up_next_cn：为框架构成描述做引导。

- failure_if_removed_cn：缺少方法论身份，论文在IS领域定位模糊。

- evidence_pointer：Introduction P3 S2

### 11. Introduction P3 S3

- order：11

- locator：Introduction P3 S3

- paraphrase_cn：框架由预测模型和优化模型组成：预测模型整合治疗轨迹中的患者和临床信息，预测给定治疗方案的患者结局；优化模型基于临床目标和不同计划的预测结果优化治疗计划。

- move_code：DESIGN_FEATURE

- statement_status：design_decision

- why_here_cn：一句话勾勒制品核心结构，为全篇方法部分设置索引。

- inherits_from_previous_cn：承接新框架。

- changes_argument_state_cn：把“框架”具体化为预测+优化两个模块。

- sets_up_next_cn：为其后框架评价结果做铺垫。

- failure_if_removed_cn：读者无法理解后文模型是什么。

- evidence_pointer：Introduction P3 S3

### 12. Introduction P3 S4

- order：12

- locator：Introduction P3 S4

- paraphrase_cn：通过考虑患者对不同计划的反应，框架能够为个体患者实现治疗计划的个性化定制。

- move_code：DESIGN_CLAIM

- statement_status：design_decision

- why_here_cn：解释为何预测+优化组合能形成个性化闭环。

- inherits_from_previous_cn：承接两模型。

- changes_argument_state_cn：点明设计意图：个性化。

- sets_up_next_cn：为下一段评价做逻辑衔接。

- failure_if_removed_cn：框架与个性化目标脱节。

- evidence_pointer：Introduction P3 S4

### 13. Introduction P4 S1

- order：13

- locator：Introduction P4 S1

- paraphrase_cn：作者基于真实临床数据集创建合成患者，对框架进行评价。

- move_code：METHOD_JUSTIFICATION

- statement_status：method_decision

- why_here_cn：提前说明评价证据类型：合成患者+真实数据，为后文仿真方法铺路。

- inherits_from_previous_cn：承接框架设计。

- changes_argument_state_cn：从设计转到评价，并明确评价设计。

- sets_up_next_cn：为其后具体结果报告做引子。

- failure_if_removed_cn：评价方法突然出现，读者不知为何用仿真。

- evidence_pointer：Introduction P4 S1

### 14. Introduction P4 S2

- order：14

- locator：Introduction P4 S2

- paraphrase_cn：一系列变化临床目标的仿真实验表明，框架在平衡局部复发风险和放疗不良反应方面持续优于现有计划方法。

- move_code：RESULT_SUMMARY

- statement_status：empirical_result

- why_here_cn：给出总体性能结果，支撑研究价值。

- inherits_from_previous_cn：承接合成患者仿真评价。

- changes_argument_state_cn：提供第一层实证：框架优于现有实践。

- sets_up_next_cn：为具体剂量数字和风险降低做铺垫。

- failure_if_removed_cn：引言无实证结论，后文关于效益的贡献悬空。

- evidence_pointer：Introduction P4 S2

### 15. Introduction P4 S3

- order：15

- locator：Introduction P4 S3

- paraphrase_cn：特别地，个性化计划可减少患者肺和心脏平均辐射剂量超过90%，从而大幅降低患肺癌和心脏病的风险。

- move_code：KEY_RESULT

- statement_status：empirical_result

- why_here_cn：给出最醒目量化结果（90%剂量降低），是引言最强证据。

- inherits_from_previous_cn：承接仿真实验整体优。

- changes_argument_state_cn：把“优于”具体化为可观的风险降低。

- sets_up_next_cn：为成本节约数字铺垫。

- failure_if_removed_cn：摘要中关键数值失去来源。

- evidence_pointer：Introduction P4 S3

### 16. Introduction P4 S4

- order：16

- locator：Introduction P4 S4

- paraphrase_cn：按年度新增乳腺癌病例估计，个性化治疗计划框架可减少与放疗诱发肺癌和心脏病相关的年度治疗成本超过2亿美元。

- move_code：ECONOMIC_RESULT

- statement_status：empirical_result

- why_here_cn：把风险降低转成经济价值，回应引言开篇165亿美元成本，体现IS价值量化贡献。

- inherits_from_previous_cn：承接剂量降低与风险降低。

- changes_argument_state_cn：从临床收益推进到经济收益。

- sets_up_next_cn：为后续贡献陈述提供完整证据链。

- failure_if_removed_cn：经济贡献缺少数据基础。

- evidence_pointer：Introduction P4 S4

### 17. Introduction P5 S1

- order：17

- locator：Introduction P5 S1

- paraphrase_cn：本研究对研究和实践作出若干贡献。首先，为医疗信息技术（HIT）的设计和有意义使用提供新见解。

- move_code：CONTRIBUTION_1

- statement_status：contribution_claim

- why_here_cn：开始分点贡献，把研究嵌入HIT文献。

- inherits_from_previous_cn：承接结果与框架。

- changes_argument_state_cn：从结果转向文献贡献定位。

- sets_up_next_cn：为其后具体缺口和设计贡献做铺垫。

- failure_if_removed_cn：研究结果的文献意义缺失。

- evidence_pointer：Introduction P5 S1

### 18. Introduction P5 S2

- order：18

- locator：Introduction P5 S2

- paraphrase_cn：尽管对HIT改善质量和效率并降低成本有共识，其设计和部署仍处于起步阶段（Agarwal et al. 2010, Fichman et al. 2011）。

- move_code：CONTRIBUTION_GAP

- statement_status：prior_literature

- why_here_cn：引述HIT尚未成熟，为本文填补设计空白提供文献依据。

- inherits_from_previous_cn：承接HIT意义。

- changes_argument_state_cn：说明现有HIT设计的短板。

- sets_up_next_cn：为“治疗决策支持不足”缺口做铺垫。

- failure_if_removed_cn：贡献1缺少学术缺口背景。

- evidence_pointer：Introduction P5 S2

### 19. Introduction P5 S3

- order：19

- locator：Introduction P5 S3

- paraphrase_cn：已有研究主要关注临床诊断的新模型新方法（如Bardhan et al. 2015, Lin et al. 2017），很少有研究探讨HIT在促进治疗决策方面的潜力。

- move_code：GAP_SPECIFICATION

- statement_status：prior_literature

- why_here_cn：精确指明现有研究聚焦诊断而非治疗决策，形成第一缺口。

- inherits_from_previous_cn：承接HIT设计不成熟。

- changes_argument_state_cn：把泛泛的“不成熟”具体化为“治疗决策被忽视”。

- sets_up_next_cn：为本文框架填补该缺口做铺垫。

- failure_if_removed_cn：贡献定位不清晰。

- evidence_pointer：Introduction P5 S3

### 20. Introduction P5 S4

- order：20

- locator：Introduction P5 S4

- paraphrase_cn：本研究通过设计个性化放疗计划决策支持框架填补这一缺口。

- move_code：CONTRIBUTION_CLAIM_1

- statement_status：contribution_claim

- why_here_cn：把框架与上一缺口直接对应。

- inherits_from_previous_cn：承接诊断/治疗缺口。

- changes_argument_state_cn：明确本文填补治疗决策支持缺口。

- sets_up_next_cn：为设计科学视角的贡献铺垫。

- failure_if_removed_cn：贡献1无落点。

- evidence_pointer：Introduction P5 S4

### 21. Introduction P5 S5

- order：21

- locator：Introduction P5 S5

- paraphrase_cn：我们的治疗计划框架整合了放射科医生、病理学家和放射肿瘤学家的临床专业。

- move_code：DESIGN_PRINCIPLE

- statement_status：design_decision

- why_here_cn：强调框架的多学科临床知识整合，为设计科学贡献做支撑。

- inherits_from_previous_cn：承接新框架。

- changes_argument_state_cn：把框架描述为知识密集型HIT。

- sets_up_next_cn：引出设计知识整合的贡献。

- failure_if_removed_cn：框架的临床知识整合特性未被强调。

- evidence_pointer：Introduction P5 S5

### 22. Introduction P5 S6

- order：22

- locator：Introduction P5 S6

- paraphrase_cn：从设计科学视角，本研究就如何把领域知识融入临床决策支持系统设计提供启示。

- move_code：DESIGN_KNOWLEDGE_CONTRIBUTION

- statement_status：contribution_claim

- why_here_cn：将具体设计升华为一般性设计知识，呼应设计科学。

- inherits_from_previous_cn：承接多学科知识整合。

- changes_argument_state_cn：把制品贡献转化为可迁移设计知识。

- sets_up_next_cn：为讨论5.1回扣Agarwal等做伏笔。

- failure_if_removed_cn：设计知识贡献缺失。

- evidence_pointer：Introduction P5 S6

### 23. Introduction P6 S1

- order：23

- locator：Introduction P6 S1

- paraphrase_cn：我们还为衡量HIT的效果和影响的研究作出贡献。

- move_code：CONTRIBUTION_2_INTRO

- statement_status：contribution_claim

- why_here_cn：开始第二贡献，转向HIT影响评估。

- inherits_from_previous_cn：承接第一贡献后继续。

- changes_argument_state_cn：从设计贡献转向影响评估。

- sets_up_next_cn：引入Agarwal微观研究呼吁。

- failure_if_removed_cn：第二贡献缺失。

- evidence_pointer：Introduction P6 S1

### 24. Introduction P6 S2

- order：24

- locator：Introduction P6 S2

- paraphrase_cn：引用Agarwal et al. (2010, p.802)的话，说明需要更细粒度和微观层面的研究来评估HIT的整体影响。

- move_code：QUOTE_AND_CALL

- statement_status：prior_literature

- why_here_cn：引用权威呼吁，为“微观衡量HIT影响”提供合法性。

- inherits_from_previous_cn：承接HIT影响评估。

- changes_argument_state_cn：将贡献定位为响应具体学术号召。

- sets_up_next_cn：为“本文衡量患者结局与成本”做铺垫。

- failure_if_removed_cn：第二贡献缺乏学术锚点。

- evidence_pointer：Introduction P6 S2

### 25. Introduction P6 S3

- order：25

- locator：Introduction P6 S3

- paraphrase_cn：我们通过检查新治疗计划框架对患者结局和治疗成本的影响来响应这一号召。

- move_code：CONTRIBUTION_CLAIM_2

- statement_status：contribution_claim

- why_here_cn：把响应落实到具体结果：结局+成本。

- inherits_from_previous_cn：承接Agarwal呼吁。

- changes_argument_state_cn：明确本文第二贡献的度量对象。

- sets_up_next_cn：为后文评价部分做铺垫。

- failure_if_removed_cn：第二贡献缺少明确承诺。

- evidence_pointer：Introduction P6 S3

### 26. Introduction P6 S4

- order：26

- locator：Introduction P6 S4

- paraphrase_cn：为贴近放疗临床环境，我们基于现有工作流，纳入患者特征和治疗轨迹中的临床信息。

- move_code：METHOD_JUSTIFICATION

- statement_status：method_decision

- why_here_cn：为HIT影响评估的微观性提供来源：不是抽象IT，而是临床工作流。

- inherits_from_previous_cn：承接对患者结局的衡量。

- changes_argument_state_cn：说明影响评估的输入设计。

- sets_up_next_cn：为其后结果强调实践相关性。

- failure_if_removed_cn：框架临床相关性缺乏说明。

- evidence_pointer：Introduction P6 S4

### 27. Introduction P6 S5

- order：27

- locator：Introduction P6 S5

- paraphrase_cn：这样我们能获得框架在临床实践中潜在益处的有用见解。

- move_code：CONTRIBUTION_PAYOFF

- statement_status：contribution_claim

- why_here_cn：说明第二贡献的价值所在：实践见解。

- inherits_from_previous_cn：承接临床信息纳入。

- changes_argument_state_cn：闭合第二贡献论证。

- sets_up_next_cn：为第三贡献（仿真 vs 临床试验）做过渡。

- failure_if_removed_cn：第二贡献没有结论。

- evidence_pointer：Introduction P6 S5

### 28. Introduction P7 S1

- order：28

- locator：Introduction P7 S1

- paraphrase_cn：最后，虽然临床试验仍是治疗决策的黄金标准，但在比较现状计划与替代计划对个体患者效果时有诸多局限（Goldberger and Buxton 2013）。

- move_code：CONTRIBUTION_3_INTRO

- statement_status：prior_literature

- why_here_cn：引入第三贡献：克服临床试验限制，先承认其黄金标准地位再指出局限。

- inherits_from_previous_cn：从第二贡献转向方法论贡献。

- changes_argument_state_cn：提出临床试验局限，为仿真方法辩护。

- sets_up_next_cn：为具体放疗临床试验限制做铺垫。

- failure_if_removed_cn：第三贡献无学术动机。

- evidence_pointer：Introduction P7 S1

### 29. Introduction P7 S2

- order：29

- locator：Introduction P7 S2

- paraphrase_cn：在放疗计划中，由于成本高昂和随访时间长，临床试验仅能比较少数常规放疗计划。

- move_code：DOMAIN_SPECIFIC_LIMITATION

- statement_status：fact

- why_here_cn：把通用临床试验局限具体化到放疗场景。

- inherits_from_previous_cn：承接临床试验局限。

- changes_argument_state_cn：说明为何放疗领域特别需要仿真。

- sets_up_next_cn：为本文仿真评价做铺垫。

- failure_if_removed_cn：仿真使用理由不够具体。

- evidence_pointer：Introduction P7 S2

### 30. Introduction P7 S3

- order：30

- locator：Introduction P7 S3

- paraphrase_cn：本研究用仿真评估框架，仿真允许直接比较不同治疗方案，并提示未经试验测试的有前景方案。

- move_code：CONTRIBUTION_CLAIM_3

- statement_status：contribution_claim

- why_here_cn：把仿真作为方法论贡献，强调它可测试未试验方案。

- inherits_from_previous_cn：承接临床试验局限。

- changes_argument_state_cn：从局限转向本文方法优势。

- sets_up_next_cn：为讨论5.2筛选临床试验埋下伏笔。

- failure_if_removed_cn：仿真方法的独立贡献不清。

- evidence_pointer：Introduction P7 S3

### 31. Introduction P8

- order：31

- locator：Introduction P8

- paraphrase_cn：论文其余部分组织如下：第2节综述文献和临床背景，第3节描述框架，第4节详细评价，第5节讨论贡献和未来方向。

- move_code：STUDY_OVERVIEW

- statement_status：author_inference

- why_here_cn：提供阅读地图，帮助评审和读者导航。

- inherits_from_previous_cn：承接前面全部引言。

- changes_argument_state_cn：结束引言，转换到正文。

- sets_up_next_cn：为第2节开始做衔接。

- failure_if_removed_cn：引言缺乏结构预告。

- evidence_pointer：Introduction P8

## 引言逐段图谱

### 1. Introduction P1

- locator：Introduction P1

- opening_move_cn：全球最常见癌症与美国确诊人数。

- development_move_cn：叠加美国350万确诊数，把疾病负担数量化。

- pivot_move_cn：从生命损失转向经济成本（165亿美元）。

- closing_move_cn：以成本数字结束，制造后文对“成本有效医疗”的期待。

- paragraph_job_cn：用现实负担和成本规模建立研究重要性。

### 2. Introduction P2

- locator：Introduction P2

- opening_move_cn：指出大多数早期患者接受放疗。

- development_move_cn：描述放疗目标与临床非临床因素复杂交互，医生依赖经验。

- pivot_move_cn：从现状描述转向问题：经验式计划是否对个体有效。

- closing_move_cn：引用Darby和Grantzau证据说明常规放疗的风险，为研究动机强化。

- paragraph_job_cn：建立临床现象与风险，并引出治疗决策有效性缺口。

### 3. Introduction P3

- locator：Introduction P3

- opening_move_cn：正式提出研究问题。

- development_move_cn：宣布采用设计科学范式，提出预测+优化框架。

- pivot_move_cn：从框架结构转向个性化机制解释。

- closing_move_cn：说明框架为何能实现个性化，为评价铺垫。

- paragraph_job_cn：定义核心研究问题和制品框架。

### 4. Introduction P4

- locator：Introduction P4

- opening_move_cn：说明评价对象为基于真实数据创建的合成患者。

- development_move_cn：给出仿真实验结果总述和关键数值（90%剂量降低）。

- pivot_move_cn：从临床结果转到经济结果。

- closing_move_cn：以年度2亿美元成本节约结束，为贡献做证据铺垫。

- paragraph_job_cn：用最醒目的量化结果证明框架价值。

### 5. Introduction P5

- locator：Introduction P5

- opening_move_cn：开始分点贡献，第一贡献为HIT设计。

- development_move_cn：指出HIT设计起步期和现有研究聚焦诊断而非治疗决策。

- pivot_move_cn：从缺口转向本文框架填补缺口。

- closing_move_cn：以设计知识贡献结束，强调领域知识整合。

- paragraph_job_cn：定位第一项贡献：治疗决策支持的HIT设计。

### 6. Introduction P6

- locator：Introduction P6

- opening_move_cn：声明第二贡献：度量HIT影响。

- development_move_cn：引用Agarwal微观研究呼吁，并说明本文衡量结局与成本。

- pivot_move_cn：从文献呼吁转向本文具体输入设计（临床工作流信息）。

- closing_move_cn：以实践见解收尾。

- paragraph_job_cn：定位第二项贡献：微观层面HIT影响评估。

### 7. Introduction P7

- locator：Introduction P7

- opening_move_cn：提出临床试验局限。

- development_move_cn：把局限具体到放疗：成本高、随访长。

- pivot_move_cn：从临床试验转到仿真方法优势。

- closing_move_cn：指出仿真可提示未试验方案。

- paragraph_job_cn：定位第三项贡献：仿真作为临床试验替代性评估。

### 8. Introduction P8

- locator：Introduction P8

- opening_move_cn：一句话总结论文结构。

- development_move_cn：无，直接列举。

- pivot_move_cn：无。

- closing_move_cn：无，作为引言结尾。

- paragraph_job_cn：提供全文路线图。

## 理论到设计逐句图谱

### 1. Section 2.1 P1 S1

- locator：Section 2.1 P1 S1

- paraphrase_cn：预测分析包含利用多源数据预测未来事件或结局的模型、工具和系统（Shmueli and Koppius 2011）。

- move_code：KNOWLEDGE_BASE_DEFINITION

- statement_status：prior_literature

- why_here_cn：定义预测分析，为后续综述划界。

- inherits_from_previous_cn：无，独立开始2.1。

- changes_argument_state_cn：建立第一文献领域。

- sets_up_next_cn：为医疗预测分析实例做铺垫。

- failure_if_removed_cn：2.1无定义基础。

- evidence_pointer：Section 2.1 P1 S1

### 2. Section 2.1 P1 S2–S3

- locator：Section 2.1 P1 S2–S3

- paraphrase_cn：预测分析在医疗场景表现良好，如识别高风险患者、急诊分诊、临床试验设计和流行病监测。

- move_code：LITERATURE_APPLICATIONS

- statement_status：prior_literature

- why_here_cn：展示预测分析已广泛应用，为本文使用预测分析提供领域合法性。

- inherits_from_previous_cn：承接定义。

- changes_argument_state_cn：确认预测分析的医疗价值。

- sets_up_next_cn：为“患者级分析”的转向做铺垫。

- failure_if_removed_cn：医疗预测分析领域缺失背景。

- evidence_pointer：Section 2.1 P1 S2–S3

### 3. Section 2.1 P2 S1–S2

- locator：Section 2.1 P2 S1–S2

- paraphrase_cn：早期工作关注人群级结局，但越来越多人关注患者级分析。

- move_code：LITERATURE_GAP_INTRO

- statement_status：prior_literature

- why_here_cn：建立从人群级到患者级的文献脉络，为本文患者级定位铺垫。

- inherits_from_previous_cn：承接医疗预测分析应用。

- changes_argument_state_cn：指出分析粒度变化。

- sets_up_next_cn：为介绍患者级研究做铺垫。

- failure_if_removed_cn：患者级分析趋势缺失。

- evidence_pointer：Section 2.1 P2 S1–S2

### 4. Section 2.1 P2 S3–S5

- locator：Section 2.1 P2 S3–S5

- paraphrase_cn：列举Caruana、Bardhan、Lin等患者级预测研究：再入院预测、心衰再入院、慢性病多事件风险。

- move_code：LITERATURE_EXAMPLES

- statement_status：prior_literature

- why_here_cn：用近期IS/管理刊物研究证明患者级分析已成为主流。

- inherits_from_previous_cn：承接患者级趋势。

- changes_argument_state_cn：具体化患者级预测的现状。

- sets_up_next_cn：为后续指出这些研究聚焦诊断/预测而非治疗决策做铺垫。

- failure_if_removed_cn：患者级预测综述空洞。

- evidence_pointer：Section 2.1 P2 S3–S5

### 5. Section 2.1 P3 S1–S3

- locator：Section 2.1 P3 S1–S3

- paraphrase_cn：方法论上预测分析分模型驱动（参数假设）和数据驱动（少假设）两类，数据驱动（深度学习）在图像、基因组和疾病预测中广泛应用。

- move_code：METHODOLOGY_TAXONOMY

- statement_status：prior_literature

- why_here_cn：给出方法论分类，为后文模型选择理由提供框架。

- inherits_from_previous_cn：承接患者级分析。

- changes_argument_state_cn：建立两个方法论阵营。

- sets_up_next_cn：为批评数据驱动方法做铺垫。

- failure_if_removed_cn：后文对model-free的批评没有分类基础。

- evidence_pointer：Section 2.1 P3 S1–S3

### 6. Section 2.1 P4 S1–S2

- locator：Section 2.1 P4 S1–S2

- paraphrase_cn：数据驱动的灵活性和少假设以可解释性和透明性为代价，可能导致怀疑和反感；且通常需要大量数据，而临床数据经常有限。

- move_code：DATA_DRIVEN_LIMITATION

- statement_status：prior_literature

- why_here_cn：为本文选用模型驱动提供直接方法论原因，建立研究选择合法性。

- inherits_from_previous_cn：承接方法论分类。

- changes_argument_state_cn：否定本文采用数据驱动的可行性。

- sets_up_next_cn：为TCP模型驱动方法做铺垫。

- failure_if_removed_cn：模型选择理由缺失。

- evidence_pointer：Section 2.1 P4 S1–S2

### 7. Section 2.1 P5 S1–S3

- locator：Section 2.1 P5 S1–S3

- paraphrase_cn：当前患者级分析大多用于诊断或不良事件预测以触发干预；本文旨在开发预测模型辅助治疗决策，并需考虑患者疾病轨迹。

- move_code：GAP_VS_TREATMENT_DECISION

- statement_status：prior_literature

- why_here_cn：标记第一缺口：预测分析用于诊断而非治疗决策。

- inherits_from_previous_cn：承接患者级分析综述。

- changes_argument_state_cn：明确本文差异：治疗决策支持。

- sets_up_next_cn：为引用最接近文献Meyer et al.做铺垫。

- failure_if_removed_cn：核心定位缺口缺失。

- evidence_pointer：Section 2.1 P5 S1–S3

### 8. Section 2.1 P5 S4–S5

- locator：Section 2.1 P5 S4–S5

- paraphrase_cn：最接近文献是Meyer et al. (2014)糖尿病治疗决策；区别在于Meyer用已有患者模型，本文聚焦个体放疗计划的优化。

- move_code：CLOSEST_LITERATURE_COMPARISON

- statement_status：prior_literature

- why_here_cn：通过对比最接近的IS工作，明确本文新颖点。

- inherits_from_previous_cn：承接治疗决策缺口。

- changes_argument_state_cn：证明即便最接近文献也未做个体放疗计划。

- sets_up_next_cn：为2.2个性化医学做过渡。

- failure_if_removed_cn：新颖性定位不充分。

- evidence_pointer：Section 2.1 P5 S4–S5

### 9. Section 2.2 P1 S1–S4

- locator：Section 2.2 P1 S1–S4

- paraphrase_cn：个性化医学将治疗、策略和药物定制给个体，可改善生存率和减少副作用，并可能降低总体医疗成本。

- move_code：PERSONALIZED_MEDICINE_INTRO

- statement_status：prior_literature

- why_here_cn：引入第二知识基础：个性化医学，为本文个性化计划提供理论支撑。

- inherits_from_previous_cn：承接治疗决策支持。

- changes_argument_state_cn：把个性化医学确立为研究目标。

- sets_up_next_cn：为后文“很少指导”做铺垫。

- failure_if_removed_cn：个性化计划缺乏理论背景。

- evidence_pointer：Section 2.2 P1 S1–S4

### 10. Section 2.2 P2 S1–S3

- locator：Section 2.2 P2 S1–S3

- paraphrase_cn：基因技术已推动个性化，但目前仅限少数疾病；需要HIE等基础设施和分析工具整合临床数据、识别患者相似性并提供风险档案。

- move_code：GENE_LIMITATION_AND_INFRA

- statement_status：prior_literature

- why_here_cn：说明基因驱动的个性化仍有基础设施限制，为HIT分析和仿真观点铺垫。

- inherits_from_previous_cn：承接个性化医学。

- changes_argument_state_cn：把个性化问题从基因转向信息基础设施。

- sets_up_next_cn：为信息共享讨论和仿真引入做铺垫。

- failure_if_removed_cn：不能解释为何需要HIT基础设施。

- evidence_pointer：Section 2.2 P2 S1–S3

### 11. Section 2.2 P2 S4–S5

- locator：Section 2.2 P2 S4–S5

- paraphrase_cn：Yaraghi等发现网络外部性对HIE平台关键；Demirezen等研究HIE参与和可持续性策略。

- move_code：IS_INFRA_LITERATURE

- statement_status：prior_literature

- why_here_cn：引证IS文献已研究个性化基础设施，为本文进入分析侧做对比。

- inherits_from_previous_cn：承接基础设施需求。

- changes_argument_state_cn：显示IS在基础设施侧已有工作。

- sets_up_next_cn：为分析侧工作做铺垫。

- failure_if_removed_cn：HIT基础设施文献缺失。

- evidence_pointer：Section 2.2 P2 S4–S5

### 12. Section 2.2 P3 S1–S2

- locator：Section 2.2 P3 S1–S2

- paraphrase_cn：分析侧已发展个体化估计方法，但现实中无法对每个治疗都做临床试验，医生只能无依据外推。

- move_code：TRIAL_LIMITATION

- statement_status：prior_literature

- why_here_cn：为仿真方法提供动机：临床试验不可行的替代方案需要。

- inherits_from_previous_cn：承接分析侧工作。

- changes_argument_state_cn：建立临床试验不足的论点。

- sets_up_next_cn：为仿真文献做铺垫。

- failure_if_removed_cn：仿真必要性缺失。

- evidence_pointer：Section 2.2 P3 S1–S2

### 13. Section 2.2 P4 S1–S3

- locator：Section 2.2 P4 S1–S3

- paraphrase_cn：替代方案是用计算仿真估计任意治疗方案的结局；已有HIV和MS患者自适应治疗仿真研究。

- move_code：SIMULATION_PRECEDENT

- statement_status：prior_literature

- why_here_cn：引证仿真方法在个性化医学中有先例，为本文仿真评价提供合法性。

- inherits_from_previous_cn：承接临床试验局限。

- changes_argument_state_cn：把仿真确立为可行评价方法。

- sets_up_next_cn：为本文仿真使用做对比。

- failure_if_removed_cn：仿真评价缺少文献先例。

- evidence_pointer：Section 2.2 P4 S1–S3

### 14. Section 2.2 P4 S4

- locator：Section 2.2 P4 S4

- paraphrase_cn：本文与这些仿真研究共享精神，即用仿真量化替代治疗方案的风险收益；不同之处在于本文不是基于现成疾病模型，而是先推导近似疾病进展的模型。

- move_code：DIFFERENTIATION_FROM_SIM_LIT

- statement_status：author_inference

- why_here_cn：既借用仿真方法又确立本文建模创新点。

- inherits_from_previous_cn：承接仿真先例。

- changes_argument_state_cn：把本文与Rosenberg和Negoescu区分。

- sets_up_next_cn：为框架中的“源自临床知识的疾病模型”做铺垫。

- failure_if_removed_cn：仿真创新性定位不清。

- evidence_pointer：Section 2.2 P4 S4

### 15. Section 2.3 P1 S1–S4

- locator：Section 2.3 P1 S1–S4

- paraphrase_cn：放疗使用高能射线杀灭肿瘤细胞，广泛用于乳腺癌症术后；虽降低复发并提高生存，但会照射邻近器官，增加心脏死亡和肺癌死亡风险。

- move_code：RADIOTHERAPY_CONTEXT

- statement_status：fact

- why_here_cn：引入第三知识基础：放疗临床背景，确定应用领域。

- inherits_from_previous_cn：承接个性化医学。

- changes_argument_state_cn：把问题锚定到放疗。

- sets_up_next_cn：为平衡复发与损伤的需求做铺垫。

- failure_if_removed_cn：放疗背景缺失。

- evidence_pointer：Section 2.3 P1 S1–S4

### 16. Section 2.3 P2 S1–S4

- locator：Section 2.3 P2 S1–S4

- paraphrase_cn：优化个性化放疗极其困难：MTC无法被影像直接检测只能病理识别；临床试验需大量患者和长时间；标准50 Gy计划未考虑肿瘤或患者异质性，可能导致次优结局。

- move_code：CLINICAL_CHALLENGE

- statement_status：fact

- why_here_cn：列出放疗个性化的具体障碍，为框架必须解决的问题做铺垫。

- inherits_from_previous_cn：承接放疗应用。

- changes_argument_state_cn：给出放疗计划研究的必要性。

- sets_up_next_cn：为MTC建模和仿真评价提供动机。

- failure_if_removed_cn：个性化放疗的必要性不完整。

- evidence_pointer：Section 2.3 P2 S1–S4

### 17. Section 2.3 P3 S1–S3

- locator：Section 2.3 P3 S1–S3

- paraphrase_cn：IMRT等进展聚焦于递送优化；但现有放疗优化文献仅关注处方剂量递送，对如何确定个体最优辐射剂量理解有限。

- move_code：GAP_IN_RT_OPTIMIZATION

- statement_status：prior_literature

- why_here_cn：定义放疗文献核心缺口：处方剂量确定而非递送。

- inherits_from_previous_cn：承接放疗优化进展。

- changes_argument_state_cn：明确本文与放疗优化文献的分界。

- sets_up_next_cn：为Table 1和“填补缺口”做铺垫。

- failure_if_removed_cn：核心缺口缺失。

- evidence_pointer：Section 2.3 P3 S1–S3

### 18. Section 2.3 P4 S1–S4

- locator：Section 2.3 P4 S1–S4

- paraphrase_cn：本文框架与dose-painting概念同源，通过适应患者异质性优化不同区域剂量；dose-painting已在其他癌症实现，但乳腺癌症因MTC不可成像而难以实现。

- move_code：DOSE_PAINTING_BRIDGE

- statement_status：prior_literature

- why_here_cn：把本文框架与临床前沿概念对接，并用乳腺MTC不可检测说明为何需要新方法。

- inherits_from_previous_cn：承接放疗优化缺口。

- changes_argument_state_cn：将本文定位为实现乳腺dose-painting。

- sets_up_next_cn：为第3节框架中的MTC建模做铺垫。

- failure_if_removed_cn：框架的临床概念基因缺失。

- evidence_pointer：Section 2.3 P4 S1–S4

### 19. Section 3 P1 S1–S2

- locator：Section 3 P1 S1–S2

- paraphrase_cn：放疗需清除残留肿瘤细胞同时减少正常组织损伤；但复杂生物物理过程使医生无法充分纳入个体临床档案，强烈需要决策支持。

- move_code：REQUIREMENT

- statement_status：author_inference

- why_here_cn：从需求出发引入框架，说明为什么必须设计一个决策支持系统。

- inherits_from_previous_cn：承接2.3放疗问题。

- changes_argument_state_cn：把文献缺口转成设计需求。

- sets_up_next_cn：为设计科学范式采用做铺垫。

- failure_if_removed_cn：框架设计缺少临床需求锚点。

- evidence_pointer：Section 3 P1 S1–S2

### 20. Section 3 P2 S1–S4

- locator：Section 3 P2 S1–S4

- paraphrase_cn：研究采用IS设计科学范式，该范式提供理解解决IS设计和实现问题的具体处方，并已用于医疗IT制品开发，如Meyer、Lin、Son等。

- move_code：DESIGN_SCIENCE_PARADIGM

- statement_status：prior_literature

- why_here_cn：明确方法论范式，把本文制品定义为设计科学成果。

- inherits_from_previous_cn：承接决策支持需求。

- changes_argument_state_cn：把解决方案框定为IT制品。

- sets_up_next_cn：为kernel theory引入做铺垫。

- failure_if_removed_cn：制品在IS设计科学传统中无位置。

- evidence_pointer：Section 3 P2 S1–S4

### 21. Section 3 P3 S1–S3

- locator：Section 3 P3 S1–S3

- paraphrase_cn：缺少设计指导时，kernel theory可帮助开发；本文因缺乏个性化放疗决策支持设计指南，先利用临床肿瘤学文献建模剂量与肿瘤进展关系，再采用决策理论方法优化剂量。

- move_code：KERNEL_THEORY

- statement_status：theory_claim

- why_here_cn：说明领域知识如何作为“内核理论”进入设计，是理论到设计的关键桥梁。

- inherits_from_previous_cn：承接设计科学范式。

- changes_argument_state_cn：建立临床肿瘤学与决策理论的指导地位。

- sets_up_next_cn：为预测+优化两步框架做铺垫。

- failure_if_removed_cn：模型构建的理论依据缺失。

- evidence_pointer：Section 3 P3 S1–S3

### 22. Section 3.1 P1 S1–S3

- locator：Section 3.1 P1 S1–S3

- paraphrase_cn：放疗结局最常用TCP度量；TCP定义为治疗结束时无克隆源细胞存活的概率；一般模型基于存活细胞数。

- move_code：TCP_THEORY_INTRO

- statement_status：prior_literature

- why_here_cn：建立预测模型的理论基础：TCP是领域知识进入设计的第一步。

- inherits_from_previous_cn：承接kernel theory。

- changes_argument_state_cn：把临床目标转为可计算概率。

- sets_up_next_cn：为公式(1)-(2)做铺垫。

- failure_if_removed_cn：TCP模型无定义基础。

- evidence_pointer：Section 3.1 P1 S1–S3

### 23. Section 3.1 P1（公式后）S4–S5

- locator：Section 3.1 P1（公式后）S4–S5

- paraphrase_cn：对于给定剂量D，存活克隆源细胞数量为N0 exp(-αD)，α为放射敏感性；高敏感性细胞可被杀灭，低敏感性细胞可能存活。

- move_code：TCP_MECHANISM

- statement_status：theory_claim

- why_here_cn：解释TCP的生物学机制，为公式(2)提供逻辑。

- inherits_from_previous_cn：承接TCP定义。

- changes_argument_state_cn：将生存概率具体化为指数衰减。

- sets_up_next_cn：为公式(2) TCP建模做铺垫。

- failure_if_removed_cn：TCP公式缺少机理推导。

- evidence_pointer：Section 3.1 P1 公式(1)

### 24. Section 3.1 P1（公式2后）S6–S8

- locator：Section 3.1 P1（公式2后）S6–S8

- paraphrase_cn：TCP公式直观：给定细胞数，剂量越高肿瘤控制越好；细胞数越多需要越多剂量。

- move_code：TCP_INTERPRETATION

- statement_status：theory_claim

- why_here_cn：为后续优化目标（最小剂量达到TCP）提供直观解释。

- inherits_from_previous_cn：承接公式(2)。

- changes_argument_state_cn：将数学公式转化为设计直觉。

- sets_up_next_cn：为随机变量建模做铺垫。

- failure_if_removed_cn：读者无法理解TCP与剂量的关系。

- evidence_pointer：Section 3.1 P1

### 25. Section 3.1 P2 S1–S2

- locator：Section 3.1 P2 S1–S2

- paraphrase_cn：作者沿用Chen et al. (2014)和Shusharina et al. (2018)，把残留MTC体积、密度和放射敏感性建模为随机变量，以刻画患者内和患者间异质性，得到公式(3)。

- move_code：HETEROGENEITY_MODELING

- statement_status：design_decision

- why_here_cn：把个体异质性纳入TCP模型，是实现个性化的关键设计决策。

- inherits_from_previous_cn：承接TCP公式。

- changes_argument_state_cn：让TCP模型从固定参数变为患者特异概率积分。

- sets_up_next_cn：为MTC建模与参数估计做铺垫。

- failure_if_removed_cn：个性化预测缺少数学表达。

- evidence_pointer：Section 3.1 P2 公式(3)

### 26. Section 3.1 P3 S1–S2

- locator：Section 3.1 P3 S1–S2

- paraphrase_cn：模型主要挑战是刻画患者特异MTC；因为无法直接检测，作者利用治疗轨迹中的患者和临床信息建模其分布。

- move_code：MTC_PROBLEM

- statement_status：author_inference

- why_here_cn：解释为什么需要治疗轨迹信息，是框架与临床数据连接的枢纽。

- inherits_from_previous_cn：承接TCP随机变量模型。

- changes_argument_state_cn：把模型挑战转向信息整合。

- sets_up_next_cn：为MTC概率分布假设做铺垫。

- failure_if_removed_cn：模型中无法解释MTC输入来源。

- evidence_pointer：Section 3.1 P3 S1–S2

### 27. Section 3.1 P3 S3–S4

- locator：Section 3.1 P3 S3–S4

- paraphrase_cn：依据临床肿瘤学发现，术前MTC体积用零膨胀泊松分布、密度用高斯分布；因手术切除部分正常组织，需考虑组织变形。

- move_code：MTC_DISTRIBUTION_ASSUMPTION

- statement_status：design_decision

- why_here_cn：给MTC分布提供临床依据，使模型可估计。

- inherits_from_previous_cn：承接MTC建模需求。

- changes_argument_state_cn：把MTC建模具体化为可计算分布。

- sets_up_next_cn：为参数估计和验证做铺垫。

- failure_if_removed_cn：MTC模型不可操作。

- evidence_pointer：Section 3.1 P3 S3–S4

### 28. Section 3.1 P4 S1–S4

- locator：Section 3.1 P4 S1–S4

- paraphrase_cn：作者选择模型驱动而非数据驱动，因为数据驱动需要大样本高质数据且临床数据有限；虽然模型简化，但可解释性在临床中重要。

- move_code：MODEL_DRIVEN_JUSTIFICATION

- statement_status：author_inference

- why_here_cn：回扣2.1对数据驱动的批评，强化选择TCP模型的合理性。

- inherits_from_previous_cn：承接TCP模型。

- changes_argument_state_cn：把模型选择上升到设计原则。

- sets_up_next_cn：为“信息可整合”假设做铺垫。

- failure_if_removed_cn：模型驱动选择无辩护。

- evidence_pointer：Section 3.1 P4 S1–S4

### 29. Section 3.1 P4 S5–S6

- locator：Section 3.1 P4 S5–S6

- paraphrase_cn：作者假设患者生物和临床信息已很好整合且易获取；现实中可能不成立，但电子病历和数字病理将促进信息无缝整合。

- move_code：ASSUMPTION_AND_PROSPECT

- statement_status：author_inference

- why_here_cn：提前承认关键假设，同时指出技术趋势，平衡可行性与前景。

- inherits_from_previous_cn：承接模型驱动选择。

- changes_argument_state_cn：设定框架使用的边界条件。

- sets_up_next_cn：为讨论中信息摩擦局限做伏笔。

- failure_if_removed_cn：信息整合假设未说明，后文局限脱节。

- evidence_pointer：Section 3.1 P4 S5–S6

### 30. Section 3.1.1 P1–P2

- locator：Section 3.1.1 P1–P2

- paraphrase_cn：用病理数据集估计MTC参数；用EORTC 22881-10882（1616名患者，50 vs 66 Gy）和EBCTCG（10801名，50 vs 0 Gy）估计克隆源细胞分数和放射敏感性。

- move_code：DATA_SOURCE

- statement_status：fact

- why_here_cn：说明参数估计的真实临床数据来源，为模型可信性奠基。

- inherits_from_previous_cn：承接TCP参数。

- changes_argument_state_cn：把理论模型与真实数据连接。

- sets_up_next_cn：为Bayesian MCMC估计方法做铺垫。

- failure_if_removed_cn：参数估计无数据基础。

- evidence_pointer：Section 3.1.1 P1–P2

### 31. Section 3.1.1 P3–P6

- locator：Section 3.1.1 P3–P6

- paraphrase_cn：用Bayesian MCMC估计c和α，假设正态先验；生成10000名合成患者并重复100次以缓解先验偏差，所有估计通过Heidelberger-Welch收敛检验。

- move_code：ESTIMATION_METHOD

- statement_status：method_decision

- why_here_cn：展示参数估计的科学性和稳健性，为后续验证铺垫。

- inherits_from_previous_cn：承接数据来源。

- changes_argument_state_cn：把模型参数变为已估计值。

- sets_up_next_cn：为模型验证做铺垫。

- failure_if_removed_cn：估计过程未报告，模型不可信。

- evidence_pointer：Section 3.1.1 P3–P6

### 32. Section 3.1.2 P1–P2

- locator：Section 3.1.2 P1–P2

- paraphrase_cn：用交叉验证评估预测：将两试验患者合并随机分训练测试集，重复100次，测试集TCP RMSE为1.3%，预测精度良好。

- move_code：VALIDATION_RESULT_1

- statement_status：empirical_result

- why_here_cn：给出第一层验证：交叉验证RMSE。

- inherits_from_previous_cn：承接估计完成。

- changes_argument_state_cn：证明预测模型在测试集上准确。

- sets_up_next_cn：为外部合成验证做铺垫。

- failure_if_removed_cn：预测精度没有证据。

- evidence_pointer：Section 3.1.2 P1–P2

### 33. Section 3.1.2 P3–P5

- locator：Section 3.1.2 P3–P5

- paraphrase_cn：利用Polgar 2013部分乳腺照射试验的患者分布生成10000名合成患者预测TCP，95%置信区间为93.7%-94.4%，非常接近报告值94.1%。

- move_code：EXTERNAL_VALIDATION

- statement_status：empirical_result

- why_here_cn：提供不同于训练数据的外部验证，加强泛化主张。

- inherits_from_previous_cn：承接交叉验证。

- changes_argument_state_cn：证明模型对不同的放疗方式也能预测。

- sets_up_next_cn：为敏感性分析做铺垫。

- failure_if_removed_cn：外部有效性缺失。

- evidence_pointer：Section 3.1.2 P3–P5

### 34. Section 3.1.2 P6–P7

- locator：Section 3.1.2 P6–P7

- paraphrase_cn：做敏感性分析：在0/50 Gy和0/66 Gy子样本上训练的两模型与全样本模型预测一致，说明模型捕获数据生成过程，缓解外推担忧。

- move_code：SENSITIVITY_ANALYSIS

- statement_status：empirical_result

- why_here_cn：处理外推到训练剂量范围外的问题，为优化模型使用高剂量做辩护。

- inherits_from_previous_cn：承接外部验证。

- changes_argument_state_cn：确立模型外推可信。

- sets_up_next_cn：为优化模型中超出训练范围的剂量搜索做铺垫。

- failure_if_removed_cn：优化模型超出剂量范围使用时无依据。

- evidence_pointer：Section 3.1.2 P6–P7

### 35. Section 3.2 P1

- locator：Section 3.2 P1

- paraphrase_cn：预测模型通过把患者临床档案纳入结局预测，提供根据患者最佳方案定制治疗计划的途径；下面讨论如何在临床约束下用预测模型优化计划。

- move_code：TRANSITION_TO_OPTIMIZATION

- statement_status：author_inference

- why_here_cn：完成从预测到优化的结构过渡。

- inherits_from_previous_cn：承接已验证预测模型。

- changes_argument_state_cn：把验证结束状态转为优化需求。

- sets_up_next_cn：为优化模型两种场景做铺垫。

- failure_if_removed_cn：预测与优化脱节。

- evidence_pointer：Section 3.2 P1

### 36. Section 3.2 P2 S1–S3

- locator：Section 3.2 P2 S1–S3

- paraphrase_cn：临床试验显示增强剂量（66 Gy）可改善局部控制，但不清楚更高剂量是否改善整体结局；因此考虑无约束和以66 Gy为上限两个场景。

- move_code：OPTIMIZATION_SCENARIOS

- statement_status：prior_literature

- why_here_cn：利用临床试验证据定义优化场景，使优化问题有临床背景。

- inherits_from_previous_cn：承接优化需求。

- changes_argument_state_cn：设定优化边界条件。

- sets_up_next_cn：为群组优化铺垫。

- failure_if_removed_cn：优化场景缺乏临床理由。

- evidence_pointer：Section 3.2 P2 S1–S3

### 37. Section 3.2 P3 S1–S3

- locator：Section 3.2 P3 S1–S3

- paraphrase_cn：风险分层虽不能完全捕获异质性，但同组患者的平均预测仍有助于指导治疗；因此先优化患者组，作为标准均匀计划与个体计划之间的中间步骤。

- move_code：GROUP_PLAN_RATIONALE

- statement_status：author_inference

- why_here_cn：为群组最优计划这一中间层次提供合理依据，也解释为何不直接跳到个体。

- inherits_from_previous_cn：承接优化场景。

- changes_argument_state_cn：把优化对象定义为患者组。

- sets_up_next_cn：为群组优化数学定义做铺垫。

- failure_if_removed_cn：群组计划的必要性不清。

- evidence_pointer：Section 3.2 P3 S1–S3

### 38. Section 3.2.1 P1

- locator：Section 3.2.1 P1

- paraphrase_cn：对N人组，为计算可处理性假设MTC对称分布，把3D TCP简化为1D，得到公式(9)-(10)的个体与群组平均TCP。

- move_code：SIMPLIFYING_ASSUMPTION

- statement_status：design_decision

- why_here_cn：给出数学模型简化假设，使优化可计算。

- inherits_from_previous_cn：承接群组优化需求。

- changes_argument_state_cn：把TCP模型转为可优化函数。

- sets_up_next_cn：为平均剂量公式做铺垫。

- failure_if_removed_cn：优化模型无法数学定义。

- evidence_pointer：Section 3.2.1 公式(9)-(10)

### 39. Section 3.2.1 P2–P4

- locator：Section 3.2.1 P2–P4

- paraphrase_cn：用乳腺平均剂量作为辐射诱导不良反应指标；无约束场景优化问题为最小化AvgDose约束TCP_N=TCP目标，约束场景再加D(d)≤66 Gy。

- move_code：OPTIMIZATION_FORMULATION

- statement_status：design_decision

- why_here_cn：正式定义优化问题，是框架设计的核心决策部分。

- inherits_from_previous_cn：承接TCP与平均剂量定义。

- changes_argument_state_cn：把个性化计划问题转化为可求解优化问题。

- sets_up_next_cn：为Lagrange和Adam方法做铺垫。

- failure_if_removed_cn：个性化计划没有形式化定义。

- evidence_pointer：Section 3.2.1 公式(11)-(13)

### 40. Section 3.2.1 P5–P7

- locator：Section 3.2.1 P5–P7

- paraphrase_cn：用Lagrange乘子法构造Lagrange函数；约束场景用高惩罚项强制66 Gy上限。

- move_code：SOLVER_JUSTIFICATION

- statement_status：method_decision

- why_here_cn：说明求解方法，并给出数学函数。

- inherits_from_previous_cn：承接优化问题。

- changes_argument_state_cn：把优化问题变成可执行求解。

- sets_up_next_cn：为Adam选择做铺垫。

- failure_if_removed_cn：优化无求解方法。

- evidence_pointer：Section 3.2.1 公式(14)-(15)

### 41. Section 3.2.1 P8–P9

- locator：Section 3.2.1 P8–P9

- paraphrase_cn：因TCP强非线性且优化随机，采用Adam随机优化；Adam只需一阶梯度、内存少，适合噪声和稀疏梯度。

- move_code：ADAM_METHOD_JUSTIFICATION

- statement_status：method_decision

- why_here_cn：解释为何Adam是最合适求解器，为后文算法对照做铺垫。

- inherits_from_previous_cn：承接Lagrange函数复杂性。

- changes_argument_state_cn：选择Adam作为框架求解器。

- sets_up_next_cn：为算法模板、附加算法评价做铺垫。

- failure_if_removed_cn：算法选择无理由。

- evidence_pointer：Section 3.2.1 P8–P9

### 42. Section 3.2.2 P1–P2

- locator：Section 3.2.2 P1–P2

- paraphrase_cn：个体计划与群组计划存在成本/时间权衡；个体计划需要细粒度组织学检查，仅少数癌症中心有能力；但作者认为个性化问题太重要，不能因技术或成本限制而不研究，且数字病理工具将使其可行。

- move_code：INDIVIDUAL_PLAN_RATIONALE

- statement_status：author_inference

- why_here_cn：在承认现实限制的同时坚定研究个体计划，为剂量绘画计划提供存在理由。

- inherits_from_previous_cn：承接群组优化完成。

- changes_argument_state_cn：拓展优化对象到个体。

- sets_up_next_cn：为个体计划定义和评价做铺垫。

- failure_if_removed_cn：剂量绘画计划失去理论必要性。

- evidence_pointer：Section 3.2.2 P1–P2

### 43. Section 3.2.2 P3

- locator：Section 3.2.2 P3

- paraphrase_cn：当患者治疗轨迹中的病史和临床特征可用时，可在公式(12)(13)中用个体TCP替代平均TCP；优化计划与dose-painting同精神，故称为dose-painting plans。

- move_code：DOSE_PAINTING_DEFINITION

- statement_status：design_decision

- why_here_cn：正式定义个体计划名称并与临床概念锚定。

- inherits_from_previous_cn：承接个体计划取舍。

- changes_argument_state_cn：命名并明确个体计划的数学实现。

- sets_up_next_cn：为第4节评价个体计划做铺垫。

- failure_if_removed_cn：dose-painting plan无定义。

- evidence_pointer：Section 3.2.2 P3

## 制品设计理由逐句图谱

### 1. Section 4.1 P1 S1–S3

- locator：Section 4.1 P1 S1–S3

- paraphrase_cn：基线评价将标准均匀计划与最优计划在TCP目标90%和80%下比较；最优计划需考虑系统误差和随机误差，它们分别源于机器校准/患者数据错误和患者运动。

- move_code：BASELINE_DESIGN

- statement_status：method_decision

- why_here_cn：为后续所有评价定义基准、误差和术语。

- inherits_from_previous_cn：承接第3节框架评价需求。

- changes_argument_state_cn：把临床实践标准计划设为对照。

- sets_up_next_cn：为误差调整和计划命名做铺垫。

- failure_if_removed_cn：评价无标准基线。

- evidence_pointer：Section 4.1 P1 S1–S3

### 2. Section 4.1 P1 S4–S5

- locator：Section 4.1 P1 S4–S5

- paraphrase_cn：评价考虑三种设置误差组合：0、1、5 mm；标准均匀计划对全乳腺给相同剂量，故误差不影响其剂量确定。

- move_code：ERROR_CONDITIONS

- statement_status：method_decision

- why_here_cn：设置稳健性工况，并明确标准计划的误差不适用性。

- inherits_from_previous_cn：承接误差类型。

- changes_argument_state_cn：确定评价工况矩阵。

- sets_up_next_cn：为Table 2计划命名和后续表结果做铺垫。

- failure_if_removed_cn：误差条件与计划表命名无依据。

- evidence_pointer：Section 4.1 P1 S4–S5

### 3. Section 4.1.1 P1–P2

- locator：Section 4.1.1 P1–P2

- paraphrase_cn：图4展示群组最优计划的剂量分布随误差增加向右偏移；约束计划分布更宽，90% TCP时靠近肿瘤的区域被66 Gy封顶。

- move_code：DISTRIBUTION_INTERPRETATION

- statement_status：empirical_result

- why_here_cn：从剂量分布解释为何约束场景平均剂量更高，为Table 3数字提供机制解释。

- inherits_from_previous_cn：承接评价条件和图4。

- changes_argument_state_cn：从图转为机制理解。

- sets_up_next_cn：为平均剂量对比做铺垫。

- failure_if_removed_cn：Table 3差异缺乏分布解释。

- evidence_pointer：Section 4.1.1 P1–P2

### 4. Section 4.1.1 P3–P5

- locator：Section 4.1.1 P3–P5

- paraphrase_cn：Table 3显示最优计划平均剂量显著低于标准计划：TCP 90%无误差时无约束计划降低94.7%，约束计划降低91.4%；5 mm误差下仍降低90%以上；TCP目标更高或误差更大所需剂量越高。

- move_code：KEY_GROUP_RESULT

- statement_status：empirical_result

- why_here_cn：报告核心量化结果，是框架优于标准实践的主要证据。

- inherits_from_previous_cn：承接分布解释。

- changes_argument_state_cn：确立群组最优计划的临床剂量优势。

- sets_up_next_cn：为约束与无约束差异解释做铺垫。

- failure_if_removed_cn：框架的剂量优势无核心数值。

- evidence_pointer：Section 4.1.1 P3–P5

### 5. Section 4.1.1 P6–P7

- locator：Section 4.1.1 P6–P7

- paraphrase_cn：有趣的是，TCP 90%时约束场景平均剂量高于无约束场景；结合图4分布更宽，说明MTC密集区域剂量不足需在大范围补量，从而增加正常组织毒性。

- move_code：MECHANISM_EXPLANATION

- statement_status：author_inference

- why_here_cn：解释看似反直觉的结果，防止读者误解，同时体现机制理解。

- inherits_from_previous_cn：承接Table 3。

- changes_argument_state_cn：把结果差异归因于剂量分配机制。

- sets_up_next_cn：为“剂量适应重要”结论做铺垫。

- failure_if_removed_cn：约束场景高剂量现象无法解释。

- evidence_pointer：Section 4.1.1 P6–P7

### 6. Section 4.1.2 P1 S1–S2

- locator：Section 4.1.2 P1 S1–S2

- paraphrase_cn：因无约束与约束在个体层面的肿瘤控制差异，个体评价聚焦无约束场景和TCP 90%；图5展示dose-painting计划的聚合最优剂量分布，误差越大所需剂量越高且分布更宽。

- move_code：INDIVIDUAL_EVALUATION_SETUP

- statement_status：method_decision

- why_here_cn：说明为何个体评价只选无约束TCP 90%，解释评价聚焦决策。

- inherits_from_previous_cn：承接群组结果。

- changes_argument_state_cn：将评价对象过渡到个体。

- sets_up_next_cn：为Table 4平均剂量比较做铺垫。

- failure_if_removed_cn：个体评价范围无解释。

- evidence_pointer：Section 4.1.2 P1 S1–S2

### 7. Section 4.1.2 P3–P5

- locator：Section 4.1.2 P3–P5

- paraphrase_cn：Table 4显示TCP 90%下dose-painting计划平均剂量为1.2-3.0 Gy，相比标准54 Gy降低约94.4%；通过降低正常组织暴露，可大幅减少副作用。

- move_code：INDIVIDUAL_RESULT

- statement_status：empirical_result

- why_here_cn：报告个体计划更极端的剂量降低，是成本效益分析的直接输入。

- inherits_from_previous_cn：承接个体评价设置。

- changes_argument_state_cn：确立个体计划剂量优势。

- sets_up_next_cn：为机制总结和经济分析做铺垫。

- failure_if_removed_cn：经济分析无剂量降幅依据。

- evidence_pointer：Section 4.1.2 P3–P5

### 8. Section 4.1.2 P6–P7

- locator：Section 4.1.2 P6–P7

- paraphrase_cn：综合表3和表4，纳入患者特异性信息和MTC分布可在显著更低剂量下达到相同TCP目标；若只有少量MTC，标准计划的过量剂量只会增加毒性而不改善控制；若无MTC则无需放疗。

- move_code：MECHANISM_SUMMARY

- statement_status：author_inference

- why_here_cn：用机制语言总结所有剂量结果，把数字提升为生物学解释。

- inherits_from_previous_cn：承接表3和表4。

- changes_argument_state_cn：把“更优”升级为“为何更优”。

- sets_up_next_cn：为算法评价留出必要性。

- failure_if_removed_cn：剂量降低缺乏解释性贡献。

- evidence_pointer：Section 4.1.2 P6–P7

### 9. Section 4.2 P1–P2

- locator：Section 4.2 P1–P2

- paraphrase_cn：为展示框架质量和计算效率，将Adam与L-BFGS-B、SA、GA三种广泛使用的随机方法比较；在相同环境下对每种方法生成10000名合成患者。

- move_code：ALGORITHM_BENCHMARK_SETUP

- statement_status：method_decision

- why_here_cn：为附加评价设定对照算法和环境，证明Adam并非凑巧好。

- inherits_from_previous_cn：承接主框架采用Adam。

- changes_argument_state_cn：引入第二层评价：求解器比较。

- sets_up_next_cn：为表5和表6结果做铺垫。

- failure_if_removed_cn：算法优势无对照。

- evidence_pointer：Section 4.2 P1–P2

### 10. Section 4.2 P3–P5

- locator：Section 4.2 P3–P5

- paraphrase_cn：表5/6显示Adam在平均剂量和计算时间上一致优于三种方法；SA和GA显著更慢且易陷入局部最优，L-BFGS-B结局接近但不够高效。

- move_code：ALGORITHM_RESULT

- statement_status：empirical_result

- why_here_cn：提供框架实际可用的重要证据：不仅预测好，优化也高效。

- inherits_from_previous_cn：承接对照设置。

- changes_argument_state_cn：确立Adam组件的质量与效率。

- sets_up_next_cn：为经济收益分析过渡。

- failure_if_removed_cn：框架的计算可用性无证据。

- evidence_pointer：Section 4.2 P3–P5

### 11. Section 4.3 P1–P2

- locator：Section 4.3 P1–P2

- paraphrase_cn：鉴于癌症护理成本上升，作者进一步估算个性化计划降低平均剂量带来的潜在成本节约。

- move_code：ECONOMIC_TRANSITION

- statement_status：author_inference

- why_here_cn：把技术结果转为医疗经济价值，回扣引言成本背景。

- inherits_from_previous_cn：承接剂量降低结果。

- changes_argument_state_cn：把评价维度扩展到成本。

- sets_up_next_cn：为剂量-反应文献引用做铺垫。

- failure_if_removed_cn：成本贡献无评价基础。

- evidence_pointer：Section 4.3 P1–P2

### 12. Section 4.3 P3–P4

- locator：Section 4.3 P3–P4

- paraphrase_cn：引用Grantzau等：每Gy肺癌风险增加8.5%；Darby等：每Gy心脏事件增加7.4%；基线发病率分别为0.64%和3%。

- move_code：DOSE_RESPONSE_LITERATURE

- statement_status：prior_literature

- why_here_cn：引用临床剂量-反应证据，使风险换算有依据。

- inherits_from_previous_cn：承接经济分析需求。

- changes_argument_state_cn：把剂量差转换成可计算风险。

- sets_up_next_cn：为具体风险降低计算做铺垫。

- failure_if_removed_cn：风险降低计算无外部依据。

- evidence_pointer：Section 4.3 P3–P4

### 13. Section 4.3 P5–P6

- locator：Section 4.3 P5–P6

- paraphrase_cn：在TCP 90%、误差5 mm保守场景下，平均剂量从54 Gy降至3 Gy；肺剂量平均减少8.22 Gy、心脏减少4.63 Gy；对应肺癌风险降低69.8%、心脏病风险降低34.2%。

- move_code：RISK_REDUCTION_CALCULATION

- statement_status：empirical_result

- why_here_cn：给出核心健康收益量化，为成本计算提供中间量。

- inherits_from_previous_cn：承接剂量-反应系数和表4剂量。

- changes_argument_state_cn：将剂量降低转为风险降低。

- sets_up_next_cn：为成本节约计算做铺垫。

- failure_if_removed_cn：风险降低结果缺失。

- evidence_pointer：Section 4.3 P5–P6

### 14. Section 4.3 P7–P8

- locator：Section 4.3 P7–P8

- paraphrase_cn：根据2018年治疗成本（肺癌88,139美元、心脏病45,532美元），每名患者节约肺癌治疗396.63美元、心脏病455.32美元；按276,480例年度新发乳腺癌，预期年节约2.355亿美元；未计其他副作用，估计保守。

- move_code：COST_SAVING_CALCULATION

- statement_status：empirical_result

- why_here_cn：把健康收益转成经济价值，回扣引言“超过2亿美元”数字。

- inherits_from_previous_cn：承接风险降低。

- changes_argument_state_cn：把框架价值扩展为经济贡献。

- sets_up_next_cn：为讨论部分贡献与局限做铺垫。

- failure_if_removed_cn：经济贡献无具体数字。

- evidence_pointer：Section 4.3 P7–P8

## Study开头、过渡与收束图谱

### 1. Introduction P3 S1; Section 2.1 开头; Section 2.3 P3

- study_or_phase：领域构建（Introduction/Section 2）

- locator：Introduction P3 S1; Section 2.1 开头; Section 2.3 P3

- opening_function_cn：用现实负担和缺口开篇，以文献综述定位研究空白。

- transition_function_cn：“下面我们讨论如何利用预测模型优化计划”，把综述结论转成设计需求。

- closure_function_cn：概述三类缺口并预告框架图（Figure 1）。

- evidence_pointer：Introduction P3; Section 2.1 P1; Section 2.3 P3

### 2. Section 3.1 开头; Section 3.1.2 开头; Section 3.1.2 末尾

- study_or_phase：预测模型构建与验证（Section 3.1）

- locator：Section 3.1 开头; Section 3.1.2 开头; Section 3.1.2 末尾

- opening_function_cn：通过TCP定义开启预测模型，说明放疗结局度量。

- transition_function_cn：从模型估计转到验证；从验证结果转到优化。

- closure_function_cn：用敏感性分析收敛“模型可信”论证，直接为优化服务。

- evidence_pointer：Section 3.1 P1; Section 3.1.2 P1; Section 3.1.2 P6

### 3. Section 3.2 P1; Section 3.2.1 开头; Section 3.2.2 末尾

- study_or_phase：优化模型（Section 3.2）

- locator：Section 3.2 P1; Section 3.2.1 开头; Section 3.2.2 末尾

- opening_function_cn：以“利用预测模型优化治疗计划”开启。

- transition_function_cn：从群组优化过渡到个体计划，用比较成本/收益。

- closure_function_cn：命名dose-painting plans，为第4节评价挂上标签。

- evidence_pointer：Section 3.2 P1; Section 3.2.2 P3

### 4. Section 4.1 P1; Section 4.1.1 P1; Section 4.1.2 末尾

- study_or_phase：基准评价（Section 4.1）

- locator：Section 4.1 P1; Section 4.1.1 P1; Section 4.1.2 末尾

- opening_function_cn：按设计科学指南声明开始评价，并定义基线。

- transition_function_cn：从群组结果过渡到个体结果；从图到表格。

- closure_function_cn：综合机制总结（如果少MTC则无需高剂量），把结果解释为剂量适应的重要性。

- evidence_pointer：Section 4.1 P1; Section 4.1.2 P6–P7

### 5. Section 4.2 P1; Section 4.2 末尾

- study_or_phase：附加算法评价（Section 4.2）

- locator：Section 4.2 P1; Section 4.2 末尾

- opening_function_cn：以“为了证明框架质量和计算效率”开启。

- transition_function_cn：从主评价转到算法对照。

- closure_function_cn：以“Adam一致优于基准”关闭，支持框架实际可用性。

- evidence_pointer：Section 4.2 P1–P5

### 6. Section 4.3 P1; Section 4.3 末尾

- study_or_phase：经济效益估算（Section 4.3）

- locator：Section 4.3 P1; Section 4.3 末尾

- opening_function_cn：以社会成本压力和医生成本压力开启。

- transition_function_cn：从剂量降低转入风险与成本换算。

- closure_function_cn：以年度2.355亿美元成本节约收尾，并说明保守性。

- evidence_pointer：Section 4.3 P1–P8

## 讨论与贡献逐句图谱

### 1. Section 5 P1 S1–S2

- locator：Section 5 P1 S1–S2

- paraphrase_cn：本研究提出指导早期乳腺癌患者个性化放疗计划的新框架；两项重要进展：将治疗轨迹患者信息纳入放射生物模型预测响应，采用Adam求解个性化计划约束优化。

- move_code：DISCUSSION_OPENING_SUMMARY

- statement_status：contribution_claim

- why_here_cn：讨论开头总结全文核心贡献，为后续细分贡献提供锚点。

- inherits_from_previous_cn：承接第3-4节全部工作。

- changes_argument_state_cn：把结果重新表述为两个科学进展。

- sets_up_next_cn：为“首个研究个体放疗计划”声明做铺垫。

- failure_if_removed_cn：讨论失去聚合起点。

- evidence_pointer：Section 5 P1 S1–S2

### 2. Section 5 P1 S3

- locator：Section 5 P1 S3

- paraphrase_cn：尽管放疗递送优化已有很多进展，据作者所知，这是首个研究个体患者放疗计划最优设计的论文。

- move_code：NOVELTY_CLAIM

- statement_status：contribution_claim

- why_here_cn：以最强新颖性声明定位全文独特性。

- inherits_from_previous_cn：承接两项进展。

- changes_argument_state_cn：把贡献提升到“首个”。

- sets_up_next_cn：为5.1贡献分节做铺垫。

- failure_if_removed_cn：讨论缺少新颖性中心。

- evidence_pointer：Section 5 P1 S3

### 3. Section 5.1 P1 S1–S2

- locator：Section 5.1 P1 S1–S2

- paraphrase_cn：本文直接响应Agarwal等关于HIT设计、实施和有意义使用的号召；框架统一统计建模与计算仿真，提供优化个体治疗计划的新能力，并纳入真实临床环境的复杂性和约束。

- move_code：CONTRIBUTION_TO_HIT

- statement_status：contribution_claim

- why_here_cn：把具体框架回接到HIT设计文献，完成贡献1。

- inherits_from_previous_cn：承接引言第一贡献缺口。

- changes_argument_state_cn：证明本文不是孤立仿真，而是回应IS号召。

- sets_up_next_cn：为个性化医学贡献做铺垫。

- failure_if_removed_cn：贡献1的文献回扣缺失。

- evidence_pointer：Section 5.1 P1 S1–S2

### 4. Section 5.1 P2 S1–S3

- locator：Section 5.1 P2 S1–S3

- paraphrase_cn：本文展示预测建模和优化在个性化医学中的潜力；当前IS个性化医学研究主要关注社交媒体和可穿戴设备的自我管理，很少量化分析驱动的治疗策略价值；本文通过个性化治疗计划框架填补空缺。

- move_code：CONTRIBUTION_TO_PERSONALIZED_MEDICINE

- statement_status：contribution_claim

- why_here_cn：把贡献定位于个性化医疗这个IS新兴领域，并指出现有缺口。

- inherits_from_previous_cn：承接HIT贡献。

- changes_argument_state_cn：把本文插入个性化医学IS文献脉络。

- sets_up_next_cn：为可迁移设计原则铺垫。

- failure_if_removed_cn：个性化医学贡献缺位置。

- evidence_pointer：Section 5.1 P2 S1–S3

### 5. Section 5.1 P2 S4

- locator：Section 5.1 P2 S4

- paraphrase_cn：尽管本研究限于乳腺放疗，框架设计原则可应用于其他涉及并发症和合并症的慢病治疗计划个性化。

- move_code：GENERALIZABILITY_CLAIM

- statement_status：contribution_claim

- why_here_cn：把具体病种结果提升为可迁移设计知识。

- inherits_from_previous_cn：承接个性化医学贡献。

- changes_argument_state_cn：扩展贡献边界。

- sets_up_next_cn：为实践含义留出空间。

- failure_if_removed_cn：设计原则可迁移性缺失。

- evidence_pointer：Section 5.1 P2 S4

### 6. Section 5.1 P3 S1–S3

- locator：Section 5.1 P3 S1–S3

- paraphrase_cn：尽管AI用于临床诊断有突破，医疗特殊性为预测模型带来挑战：需要临床工作流知识、可解释性；本文通过临床肿瘤学知识建模平衡灵活性与可解释性。

- move_code：INTERPRETABILITY_CONTRIBUTION

- statement_status：contribution_claim

- why_here_cn：把模型选择升华为一般化的设计知识贡献。

- inherits_from_previous_cn：承接整体贡献。

- changes_argument_state_cn：把方法学选择标为贡献。

- sets_up_next_cn：为实践含义部分过渡。

- failure_if_removed_cn：可解释性贡献缺失。

- evidence_pointer：Section 5.1 P3 S1–S3

### 7. Section 5.2 P1 S1–S2

- locator：Section 5.2 P1 S1–S2

- paraphrase_cn：基因测序、影像和数字病理进展提高对疾病机制理解，但患者异质性和缺乏高精度生物标志物限制治疗优化；放疗中相互冲突目标和MTC信息缺失使设计特别困难。

- move_code：PRACTICE_CHALLENGE

- statement_status：prior_literature

- why_here_cn：重申实践挑战，说明框架针对真实痛点。

- inherits_from_previous_cn：承接讨论贡献。

- changes_argument_state_cn：从研究贡献转向实践意义。

- sets_up_next_cn：为框架如何应对挑战做铺垫。

- failure_if_removed_cn：实践意义缺背景。

- evidence_pointer：Section 5.2 P1 S1–S2

### 8. Section 5.2 P2 S1–S3

- locator：Section 5.2 P2 S1–S3

- paraphrase_cn：框架通过将患者临床特征纳入疾病进展推断来定制计划，从而解决这些困难。

- move_code：PRACTICE_SOLUTION

- statement_status：contribution_claim

- why_here_cn：把框架与前面挑战直接对应。

- inherits_from_previous_cn：承接实践挑战。

- changes_argument_state_cn：闭合实践含义的因果解释。

- sets_up_next_cn：为信息共享含义做铺垫。

- failure_if_removed_cn：框架的实践解决能力未说明。

- evidence_pointer：Section 5.2 P2 S1–S3

### 9. Section 5.2 P3 S1–S4

- locator：Section 5.2 P3 S1–S4

- paraphrase_cn：研究发现强调跨学科护理中有效信息共享的必要性；个性化计划的经济收益依赖诊断和治疗轨迹中病历与临床信息的无缝整合；现实中跨机构或部门信息摩擦仍是主要障碍。

- move_code：PRACTICE_IMPLICATION_INFO_SHARING

- statement_status：author_inference

- why_here_cn：把框架成功条件转化为实践启示，呼应2.2基础设施讨论。

- inherits_from_previous_cn：承接实践解决方案。

- changes_argument_state_cn：指出信息共享是商业价值的限制条件。

- sets_up_next_cn：为研究-临床合作呼吁做铺垫。

- failure_if_removed_cn：信息共享实践启示缺失。

- evidence_pointer：Section 5.2 P3 S1–S4

### 10. Section 5.2 P4 S1–S2

- locator：Section 5.2 P4 S1–S2

- paraphrase_cn：现有数据驱动的临床预测模型围绕给定治疗和患者记录训练，不能预测未见过疗法；本文TCP模型基于临床领域知识，可评估新治疗计划。

- move_code：PRACTICE_IMPLICATION_NOVEL_PLANS

- statement_status：author_inference

- why_here_cn：强调模型驱动方法对未见过方案的可预测性优势，实用化和差异化。

- inherits_from_previous_cn：承接临床预测文献历史。

- changes_argument_state_cn：把模型选择转成实践价值。

- sets_up_next_cn：为筛选临床试验建议做铺垫。

- failure_if_removed_cn：模型驱动优势未与实践结合。

- evidence_pointer：Section 5.2 P4 S1–S2

### 11. Section 5.2 P5 S1–S2

- locator：Section 5.2 P5 S1–S2

- paraphrase_cn：临床试验昂贵费时，本文框架可用于筛选和选择未来临床试验方案，尤其适合未被重视的非传统计划。

- move_code：PRACTICE_IMPLICATION_TRIAL_SCREENING

- statement_status：contribution_claim

- why_here_cn：把仿真评价方法转成临床研究工具，补强第三贡献。

- inherits_from_previous_cn：承接未见过方案预测。

- changes_argument_state_cn：把框架定位为试验筛选器。

- sets_up_next_cn：为局限部分过渡。

- failure_if_removed_cn：仿真方法缺少实际应用出口。

- evidence_pointer：Section 5.2 P5 S1–S2

### 12. Section 5.3 P1 S1–S3

- locator：Section 5.3 P1 S1–S3

- paraphrase_cn：局限1：模型驱动需对复杂放射生物过程做简化假设；但优点是可用计算实验做反事实。

- move_code：LIMITATION_1

- statement_status：author_inference

- why_here_cn：承认建模简化并给出辩护，维系设计科学可信度。

- inherits_from_previous_cn：承接全文模型选择。

- changes_argument_state_cn：把局限转成方法优点。

- sets_up_next_cn：为局限2做铺垫。

- failure_if_removed_cn：建模简化未声明，构成隐性风险。

- evidence_pointer：Section 5.3 P1 S1–S3

### 13. Section 5.3 P2 S1–S5

- locator：Section 5.3 P2 S1–S5

- paraphrase_cn：局限2：假设经典保乳治疗设置，未考虑辅助治疗可能增加放射敏感性和放疗时间对结果的影响；一旦数据可得，可开发动态治疗计划框架。

- move_code：LIMITATION_2

- statement_status：author_inference

- why_here_cn：承认影响预测准确性的因素并给未来方向。

- inherits_from_previous_cn：承接局限1。

- changes_argument_state_cn：把临床复杂性与模型简化不匹配问题显式化。

- sets_up_next_cn：为局限3做铺垫。

- failure_if_removed_cn：辅助治疗和时间因素对预测的限制未说明。

- evidence_pointer：Section 5.3 P2 S1–S5

### 14. Section 5.3 P3 S1–S4

- locator：Section 5.3 P3 S1–S4

- paraphrase_cn：局限3：用平均剂量作为不良反应指标，不完全反映患者临床概况；未来可用更细粒度指标。

- move_code：LIMITATION_3

- statement_status：author_inference

- why_here_cn：承认指标简化，限定结论边界。

- inherits_from_previous_cn：承接局限2。

- changes_argument_state_cn：把平均剂量指标从工具性上升为可改进对象。

- sets_up_next_cn：为局限4做铺垫。

- failure_if_removed_cn：平均剂量指标局限未声明。

- evidence_pointer：Section 5.3 P3 S1–S4

### 15. Section 5.3 P4 S1–S2

- locator：Section 5.3 P4 S1–S2

- paraphrase_cn：局限4：个性化计划仅通过仿真评估，需在临床实践中进一步试验验证后采用。

- move_code：LIMITATION_4

- statement_status：author_inference

- why_here_cn：最关键的诚实声明：仿真不能替代临床验证。

- inherits_from_previous_cn：承接局限3。

- changes_argument_state_cn：明确制品当前证据级别。

- sets_up_next_cn：结束全文并为未来临床研究留口。

- failure_if_removed_cn：仿真结果可能被过度解读为临床应用。

- evidence_pointer：Section 5.3 P4 S1–S2

## Study累积逻辑

### 1. 1

- study_or_phase：阶段1：文献综述与问题构建

- evidence_job_cn：证明治疗决策支持领域存在真实研究缺口。

- what_it_establishes_cn：HIT治疗决策支持缺失、放疗优化只做递送优化、dose-painting在乳腺未实现。

- what_it_cannot_establish_cn：不能证明构建出的制品能解决问题。

- why_next_phase_is_needed_cn：缺口只说明需求，需要制品来满足。

- transition_wording_function_cn：从缺口转向设计科学框架的构建。

### 2. 2

- study_or_phase：阶段2：预测模型构建与参数估计

- evidence_job_cn：建立可工作的个性化TCP预测函数。

- what_it_establishes_cn：把MTC随机变量纳入TCP模型，并有真实临床数据估计参数。

- what_it_cannot_establish_cn：模型仅估计未验证；不能作为优化输入。

- why_next_phase_is_needed_cn：需要验证模型可信后才可用于优化。

- transition_wording_function_cn：从估计转到验证（交叉验证、外部验证、敏感性）。

### 3. 3

- study_or_phase：阶段3：预测模型验证

- evidence_job_cn：证明预测模型准确且可外推。

- what_it_establishes_cn：测试集RMSE 1.3%，外部试验TCP接近94.1%，子样本预测一致。

- what_it_cannot_establish_cn：不能证明优化计划一定优于标准计划。

- why_next_phase_is_needed_cn：需要优化模型将TCP预测转为剂量决策。

- transition_wording_function_cn：从“模型可信”转向“如何利用模型优化”。

### 4. 4

- study_or_phase：阶段4：优化模型构建与求解

- evidence_job_cn：把TCP预测转化为最小平均剂量下的个性化计划。

- what_it_establishes_cn：无约束/66 Gy约束优化问题形式化，Adam求解，生成群组和个体计划。

- what_it_cannot_establish_cn：不能证明这些计划比临床标准更好。

- why_next_phase_is_needed_cn：需要系统评价与标准计划比较。

- transition_wording_function_cn：从求解方法转到第4节评价。

### 5. 5

- study_or_phase：阶段5：基准评价

- evidence_job_cn：证明框架相比标准临床实践显著降低平均剂量且稳健。

- what_it_establishes_cn：群组计划平均剂量降低90%以上，个体计划降低约94.4%，误差增加时优势保持。

- what_it_cannot_establish_cn：不能证明求解器的选择效率最优，也不能证明经济价值。

- why_next_phase_is_needed_cn：需要算法对照证明框架可用，需要经济换算证明价值。

- transition_wording_function_cn：从主评价转向附加评价与经济效益。

### 6. 6

- study_or_phase：阶段6：附加算法评价

- evidence_job_cn：证明Adam带来计算效率与结局优势，而不仅是预测模型优势。

- what_it_establishes_cn：Adam在平均剂量和时间上优于L-BFGS-B、SA、GA。

- what_it_cannot_establish_cn：不能证明健康和经济收益。

- why_next_phase_is_needed_cn：需要把剂量优势转换为风险和成本。

- transition_wording_function_cn：从算法优势转向经济收益。

### 7. 7

- study_or_phase：阶段7：经济效益估算

- evidence_job_cn：把剂量降低转成健康风险降低和成本节约。

- what_it_establishes_cn：肺癌风险降69.8%、心脏病风险降34.2%，年节约约2.355亿美元。

- what_it_cannot_establish_cn：不能证明真实临床健康结局或实际支付节省。

- why_next_phase_is_needed_cn：需要讨论把全部结果升级为贡献和边界。

- transition_wording_function_cn：从经济结果转向讨论贡献与局限。

## 主张—证据台账

### 1. 预测模型能准确预测放疗后TCP。

- claim_cn：预测模型能准确预测放疗后TCP。

- claim_level：mechanism

- supporting_evidence_cn：临床数据交叉验证测试集RMSE 1.3%；Polgar外部合成验证95% CI 93.7%-94.4%接近94.1%。

- support_strength：direct

- where_claim_is_made：Section 3.1.2 P1–P5

- where_evidence_is_provided：Section 3.1.2 P1–P5

### 2. 模型可用于训练范围外的剂量外推。

- claim_cn：模型可用于训练范围外的剂量外推。

- claim_level：mechanism

- supporting_evidence_cn：0/50与0/66 Gy子样本模型与全样本模型预测一致。

- support_strength：direct

- where_claim_is_made：Section 3.1.2 P6–P7

- where_evidence_is_provided：Section 3.1.2 P6–P7; Figure 3

### 3. 群组最优计划相比标准计划可在更低剂量下达到相同TCP。

- claim_cn：群组最优计划相比标准计划可在更低剂量下达到相同TCP。

- claim_level：technical

- supporting_evidence_cn：TCP 90%无误差时无约束平均剂量从54 Gy降至2.86 Gy；5 mm误差下仍降约90%。

- support_strength：direct

- where_claim_is_made：Section 4.1.1 P3–P5

- where_evidence_is_provided：Table 3; Figure 4

### 4. 个体dose-painting计划可在更极端低剂量下达到TCP目标。

- claim_cn：个体dose-painting计划可在更极端低剂量下达到TCP目标。

- claim_level：technical

- supporting_evidence_cn：TCP 90%时平均剂量为1.2-3.0 Gy，较54 Gy降低约94.4%。

- support_strength：direct

- where_claim_is_made：Section 4.1.2 P3–P5

- where_evidence_is_provided：Table 4; Figure 5

### 5. 剂量适应机制可解释为何低剂量仍能控制肿瘤：MTC少时过量剂量只增加毒性。

- claim_cn：剂量适应机制可解释为何低剂量仍能控制肿瘤：MTC少时过量剂量只增加毒性。

- claim_level：mechanism

- supporting_evidence_cn：基于TCP模型中MTC分布随机性以及表3/4剂量结果推断。

- support_strength：partial

- where_claim_is_made：Section 4.1.2 P6–P7

- where_evidence_is_provided：Table 3–4; Figure 4–5

### 6. Adam是高效且患者结局更优的求解器。

- claim_cn：Adam是高效且患者结局更优的求解器。

- claim_level：technical

- supporting_evidence_cn：Table 5/6显示Adam在平均剂量和时间上均优于L-BFGS-B、SA、GA。

- support_strength：direct

- where_claim_is_made：Section 4.2 P3–P5

- where_evidence_is_provided：Table 5–6

### 7. 剂量降低显著降低肺癌和心脏病风险。

- claim_cn：剂量降低显著降低肺癌和心脏病风险。

- claim_level：boundary

- supporting_evidence_cn：基于Grantzau 8.5%/Gy和Darby 7.4%/Gy线性外推：肺癌风险降69.8%、心脏病降34.2%。

- support_strength：partial

- where_claim_is_made：Section 4.3 P5–P6

- where_evidence_is_provided：Section 4.3 P3–P6; Grantzau et al. 2014; Darby et al. 2013

### 8. 框架每年可节约超过2亿美元治疗成本。

- claim_cn：框架每年可节约超过2亿美元治疗成本。

- claim_level：design_knowledge

- supporting_evidence_cn：每名患者估算节约851.95美元，乘以276,480年新发病例得到约2.355亿美元。

- support_strength：partial

- where_claim_is_made：Section 4.3 P7–P8

- where_evidence_is_provided：Section 4.3 P7–P8; Kakushadze et al. 2017; Yu et al. 2013

### 9. 框架通过领域知识+可解释模型可评价未见过治疗方案。

- claim_cn：框架通过领域知识+可解释模型可评价未见过治疗方案。

- claim_level：design_knowledge

- supporting_evidence_cn：敏感性分析支持外推；模型基于TCP机制；无直接实验证据。

- support_strength：asserted

- where_claim_is_made：Section 5.2 P4

- where_evidence_is_provided：Section 3.1.2 P6–P7; Section 5.2 P4

### 10. 这是首个研究个体患者放疗计划最优设计的论文。

- claim_cn：这是首个研究个体患者放疗计划最优设计的论文。

- claim_level：theory

- supporting_evidence_cn：作者自评，文献综述仅限定INFORMS期刊放疗优化文章。

- support_strength：asserted

- where_claim_is_made：Section 5 P1 S3

- where_evidence_is_provided：Section 5 P1 S3; Table 1

## ISR定位逻辑

- constitutive_is_problem_cn：核心IS问题不是单纯预测或优化，而是在信息密集的多学科治疗过程中，如何设计决策支持系统来整合治疗轨迹中的患者级信息，使机器可预测患者特异性治疗结果并据此优化计划；这回应了HIT设计和有意义使用以及患者级分析从诊断转向治疗决策的IS缺口。

- technology_behavior_or_market_entanglement_cn：技术与临床行为相互构成：技术制品（TCP+RAdam框架）之所以有价值，是因为它改变了放疗医生的决策依据——从经验式均匀剂量转向基于MTC分布的概率性个性化计划；反过来，临床工作流中的信息摩擦（病理切片不共享给放疗科）又决定技术能否落地，作者的框架因此与组织信息共享行为绑定。

- role_of_benchmark_or_objective_evidence_cn：仿真和剂量基准不仅用于技术指标（平均剂量、RMSE、收敛时间、成本），更被用于支持IS主张：设计科学制品能显著改善患者结局和成本；尤其是算法对照证明“技术选择”是设计贡献的一部分，而不是可随意替换的实现细节。

- theory_in_design_cn：理论以kernel theory形式进入设计：临床肿瘤学TCP模型直接决定预测模型形式；决策理论（优化目标）与设计科学范式指导制品结构；这些理论不仅解释结果，而是塑造模型结构和求解方法，属于强理论设计耦合。

- technical_vs_is_contribution_balance_cn：作者以IS文献贡献为主（HIT设计、微观影响、个性化医学），技术细节（TCP、Adam、MCMC）作为支撑证据但未在讨论中占据主导；技术报告控制篇幅，贡献讨论回扣Agarwal等IS文献和医疗实践。

- beyond_transient_performance_cn：作者试图通过三方面超越暂时性能：用机制解释（MTC分布导致剂量适应）、用可迁移设计知识（领域知识model-based、信息整合条件）、用未见过方案的可预测性来表明框架是持久设计原则而非一次性优化。但在成本外推和“首个”声明上存在依赖文献线性外推和自评的成分，超越仍部分声称多于证明。

## 段落级仿写模板

### abstract_steps

1. 第一步：用全球公认疾病负担或问题规模开启。

2. 第二步：指出该问题的治疗过程复杂且信息密集，使个性化困难。

3. 第三步：声明采用设计科学范式并给出制品结构（通常两个模型）。

4. 第四步：给出评价方式（仿真）与总体结果（优于现有实践）。

5. 第五步：给出关键量化结果（可显著降低风险或成本）。

6. 第六步：分研究和实践两层声明贡献。

### introduction_paragraph_steps

1. 第一步：用统计/成本数据建立疾病重要性。

2. 第二步：描述当前临床实践及其固有局限。

3. 第三步：用文献证据指出常规实践的潜在风险或无效性。

4. 第四步：提出正式研究问题并宣示方法范式。

5. 第五步：概述框架结构并解释设计意图。

6. 第六步：说明评价方式并给出最强数量结果。

7. 第七步：分三条贡献回扣各自文献缺口。

8. 第八步：预告论文结构。

### theory_to_design_steps

1. 第一步：综述相关领域知识，把研究放在文献中。

2. 第二步：建立知识缺口：诊断vs治疗、递送优化vs最优剂量。

3. 第三步：引入设计科学范式，说明缺少设计指南时用kernel theory。

4. 第四步：把领域理论形式化为预测模型（TCP），清楚定义变量和假设。

5. 第五步：用真实数据和Bayesian方法估计参数，说明估计过程的稳健性。

6. 第六步：交叉验证、外部验证、敏感性分析逐层证明模型可信。

7. 第七步：把预测模型嵌入优化模型，定义目标函数、约束、求解器，并说明求解器选择理由。

8. 第八步：区分群组与个体计划，为每种计划给出临床理由。

### method_and_study_sequence_steps

1. 第一步：声明评价遵循方法论指南，并定义基线。

2. 第二步：定义工况（误差组合、目标参数、约束条件）与命名规则。

3. 第三步：先展示分布形态，再报告平均指标。

4. 第四步：对每个结果给出机制解释或反直觉解释。

5. 第五步：从主要评价扩展到算法基准，证明技术选择有效。

6. 第六步：把最终技术结果转成风险与成本。

### results_reporting_steps

1. 第一步：用表格/图先展示原始条件矩阵。

2. 第二步：报关键数值和百分比变化。

3. 第三步：指出误差和目标对结果的调节作用。

4. 第四步：解释非直观结果背后的机制。

5. 第五步：把结果显示转移到下一个评价维度（个体/算法/经济）。

### discussion_and_contribution_steps

1. 第一步：用两三句话重申核心贡献。

2. 第二步：用最强新颖性声明定位全文。

3. 第三步：分研究贡献回扣引言中的各缺口。

4. 第四步：加入可迁移设计知识声明。

5. 第五步：转向实践含义，把框架与真实工作流条件绑定。

6. 第六步：列出四类局限，但为关键局限提供辩护。

7. 第七步：用未来方向收尾。

## 可执行写作算法

### 1. 1

- step：1

- rhetorical_job_cn：建立疾病/问题的重要性并给出经济或社会负担。

- research_evidence_required_cn：权威流行病学统计、成本报告或临床指南。

- sentence_pattern_function_cn：首句给出全球或国家级规模，第二句给出具体数量，第三句转向经济/流程复杂度。

- transition_condition_cn：当读者感到问题值得关注时，进入下一步。

### 2. 2

- step：2

- rhetorical_job_cn：描述当前实践及其局限，并给出文献证据。

- research_evidence_required_cn：临床实践指南、真实工作流描述、关于现有实践风险的研究。

- sentence_pattern_function_cn：“尽管目标简单，但因素复杂；医生依赖经验；近期研究显示……”以问题句结束。

- transition_condition_cn：当“经验式计划是否有效”成为自然问题时，进入RQ。

### 3. 3

- step：3

- rhetorical_job_cn：提出研究问题并宣示方法论范式。

- research_evidence_required_cn：一个明确可研究的RQ和至少一个方法范式依据（如设计科学）。

- sentence_pattern_function_cn：“我们关注RQ：如何……为回答问题，我们遵循……并提出框架，框架由X和Y组成。”

- transition_condition_cn：当读者知道研究要构建什么样的制品后，进入证据预览。

### 4. 4

- step：4

- rhetorical_job_cn：告知评价方式并给出最强结果预览。

- research_evidence_required_cn：已完成仿真/实验的初步结果，包括一个让人记住的百分比或金额。

- sentence_pattern_function_cn：“我们基于真实数据创建合成患者进行仿真；结果表明框架更好；关键数字是……”。

- transition_condition_cn：当最强结果已展示后，进入贡献声明。

### 5. 5

- step：5

- rhetorical_job_cn：分条陈述贡献并分别对应文献缺口。

- research_evidence_required_cn：每一条贡献对应的领域文献和具体缺口。

- sentence_pattern_function_cn：“首先/我们也/最后，我们贡献于X；具体文献缺口是Y；本文通过Z填补。”

- transition_condition_cn：当三点贡献都锚定在文献中后，进入正文。

### 6. 6

- step：6

- rhetorical_job_cn：用领域知识综述定位研究，建立缺口。

- research_evidence_required_cn：多个领域文献综述，并能指出具体未回答的问题。

- sentence_pattern_function_cn：先综述已有应用，再分类方法，然后指出“现有聚焦诊断而非治疗决策”。

- transition_condition_cn：当缺口足够具体时，进入框架设计。

### 7. 7

- step：7

- rhetorical_job_cn：用kernel theory建模预测模型，明确参数和数据。

- research_evidence_required_cn：领域理论（如TCP）、可用的真实数据集、估计方法。

- sentence_pattern_function_cn：“领域标准度量是X；我们将关键变量建模为随机变量；使用A数据估计B参数。”

- transition_condition_cn：当模型可估计时，进入验证。

### 8. 8

- step：8

- rhetorical_job_cn：多层验证模型：交叉验证、外部验证、敏感性。

- research_evidence_required_cn：训练/测试数据、外部试验数据、可用于敏感性分析的子样本。

- sentence_pattern_function_cn：“先交叉验证得到误差；再在外部数据上预测；最后做敏感性分析缓解外推担忧。”

- transition_condition_cn：当模型被认为是可信输入时，进入优化。

### 9. 9

- step：9

- rhetorical_job_cn：设计优化模型，定义目标、约束、求解器和两种计划。

- research_evidence_required_cn：临床目标、约束条件、可求解的数学模型、算法选择理由。

- sentence_pattern_function_cn：“优化问题为最小化X，约束Y；因为目标非线性随机，选用算法Z；区分群组与个体计划。”

- transition_condition_cn：当计划类型和算法都已定义后，进入评价。

### 10. 10

- step：10

- rhetorical_job_cn：系统评价：基线、工况、算法对照、经济换算。

- research_evidence_required_cn：标准实践基线数据、多种工况设置、对照算法结果、外部成本数据。

- sentence_pattern_function_cn：“基线评价比较标准与优化计划；附加评价比较算法；经济收益把剂量差转成风险差和成本差。”

- transition_condition_cn：当每个主张都有表格或计算支持时，进入讨论。

### 11. 11

- step：11

- rhetorical_job_cn：讨论贡献、实践含义、局限和未来。

- research_evidence_required_cn：对全文结果的归纳、设计知识声明、对关键假设的边界说明。

- sentence_pattern_function_cn：“本文带来两项进展；贡献于X；实践需要Y条件；局限包括1-4，但其中1可通过……缓解。”

- transition_condition_cn：当读者清楚贡献与边界后，论文结束。

## 应模仿的高价值动作

1. 引言中的‘三层缺口叠加’：先HIT设计缺口，再放疗优化缺口，最后个性化医学仿真缺口

2. 在评价开始时明确声明遵循设计科学评价指南，使评审感到方法严谨

3. 对反直觉结果给出机制解释（约束场景高剂量因需在MTC密集区封顶后大范围补量）

4. 用多种验证方式（交叉验证、外部合成验证、敏感性分析）提前封堵外推质疑

5. 算法评价把‘技术实现’上升为‘设计贡献’，防止被当作可替换细节

6. 经济换算先引用文献风险系数和成本数据，再计算并附保守性声明

7. 讨论中把一个领域证据限制转化为设计知识优势（模型驱动可预测未见过方案）

## 不要只复制的表面动作

1. 不能只做预测+优化框架而不报告模型验证与误差

2. 不能沿用“标准计划为基线”而不考虑真实放疗中的分次和边界效应

3. 不能把平均剂量下降直接当作最终收益，必须有文献支持的剂量-反应换算

4. 不能只报优化算法更好而不报告收敛时间与环境，否则计算效率主张无证据

5. 不能一上来就宣称‘首个’，必须与最接近文献做具体差异对比

## 证据薄弱或跳跃的动作

1. “首个研究个体放疗计划设计”声明依赖作者文献限定，未对非INFORMS放疗物理文献全面核对，属于自评性较强声明

2. 从仿真平均剂量降低到真实健康风险降低的线性外推：个性化计划剂量分布与标准均匀计划结构不同，线性剂量-反应系数可能不完全适用

3. 年度2.355亿美元成本节约为点估计，未考虑框架实施成本（数字病理、细粒度组织学检查）

4. MTC建模基于假设性概率分布和不可直接观测的MTC，验证只能通过间接外部合成数据集进行，真实患者数据缺失；作者已做说明但仍属薄弱环节

5. 外部验证使用由Polgar试验分布生成的合成患者，而非真实个体层面预测，严格说只能支持模型在人群分布上的外推

## 一句话套路

以临床治疗缺口和成本负担为入口，用设计科学范式把领域知识内置为可解释预测模型，再用优化模型把预测转为个性化计划，以多工况仿真+算法对照+经济换算证明制品在患者结局、效率和成本上的三重优势。

## 分析边界

分析基于文章全文与第一阶段导航，但第3.1节的Online Appendix EC.1-EC.3内容不在提供文本中，因此MTC信息流细节、组织变形建模、梯度推导等未逐句核查；Table 1和若干图注OCR可能不完整；经济分析部分有文本中明显的公式排版错误（如约等号位置），已按原始数值重建计算逻辑；‘首个研究’为作者自评，未进行外部文献广度核验。
