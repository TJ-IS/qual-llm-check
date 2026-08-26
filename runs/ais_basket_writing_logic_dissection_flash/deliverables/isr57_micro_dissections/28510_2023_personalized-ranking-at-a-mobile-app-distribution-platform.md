# Personalized Ranking at a Mobile App Distribution Platform：ISR 句段级微观图谱

- 作者：Shengjun Mao; Sanjeev Dewan; Yi-Jen (Ian) Ho
- 年份：2023
- DOI：10.1287/isre.2022.1156
- 源文件：28510_2023_personalized-ranking-at-a-mobile-app-distribution-platform.md
- 置信度：0.82

## 核实后的宏观骨架

本文是一篇设计科学研究型ISR论文。研究问题：移动应用分发平台应如何利用点击流中的显示偏好，在个体层面设计个性化应用排序，以同时提高平台收入和消费者效用。全文论证链为：现实平台排序粗糙与收入机制（引言）→排序文献以平均效用为主、个性化可能损害平台（文献与框架）→以分析模型导出混合排序逻辑并用结构效用模型作为主引擎（概念框架）→独特用户-印象级点击流数据含数值与文本特征（数据）→两阶段层级贝叶斯二元Probit估计个体点击与安装效用（模型）→系数、边际效应、异质性、模型拟合与稳健性检验（结果）→反事实政策实验比较非个性化与个性化排序方案（政策实验）→结论中把结果转化为贡献、管理含义、边界与未来研究。核心制品是HMUM个性化混合排序：顶部放置用户最喜欢的高效用应用并按CPA边际排序，其余按效用×边际排序。

## 摘要逐句图谱

### 1. Abstract P1 S1

- order：1

- locator：Abstract P1 S1

- paraphrase_cn：数字平台因客户数据收集便利而广泛实现内容与服务个性化。

- move_code：CONTEXT

- statement_status：fact

- why_here_cn：把研究放在数字平台个性化的大背景下，建立话题的普遍重要性。

- inherits_from_previous_cn：无，是全文起点。

- changes_argument_state_cn：确立研究对象类别：平台个性化。

- sets_up_next_cn：引出具体未研究情境（移动应用分发）。

- failure_if_removed_cn：摘要缺少宏观语境，个性化应用分发问题显得孤立。

- evidence_pointer：Abstract第一句

### 2. Abstract P1 S2

- order：2

- locator：Abstract P1 S2

- paraphrase_cn：本文研究此前未被关注的移动应用分发情境中的个性化。

- move_code：PHENOMENON_AND_GAP

- statement_status：author_inference

- why_here_cn：在第一句普遍背景后立即收窄到本文情境，并声称该情境未被研究，制造缺口。

- inherits_from_previous_cn：承接个性化普遍存在这一前提。

- changes_argument_state_cn：定义本文的具体研究场景。

- sets_up_next_cn：为下一句的综合框架提供落点。

- failure_if_removed_cn：读者不知道本文情境是什么，研究目标悬空。

- evidence_pointer：Abstract第二句

### 3. Abstract P1 S3

- order：3

- locator：Abstract P1 S3

- paraphrase_cn：开发一个综合框架，利用点击流中嵌入的显示偏好对应用印象进行个性化排序。

- move_code：RQ_OR_OBJECTIVE

- statement_status：author_inference

- why_here_cn：给出论文要完成的核心任务，将情境空白转化为研究目标。

- inherits_from_previous_cn：承接移动应用分发这一未研究情境。

- changes_argument_state_cn：明确全文目标：排序框架。

- sets_up_next_cn：引出框架需同时考虑什么目标（收入）。

- failure_if_removed_cn：摘要没有研究任务，后续方法结果缺乏指向。

- evidence_pointer：Abstract第三句

### 4. Abstract P1 S4

- order：4

- locator：Abstract P1 S4

- paraphrase_cn：为提升平台收入，框架联合考虑消费者效用与每次应用安装的CPA边际。

- move_code：REQUIREMENT

- statement_status：author_inference

- why_here_cn：把排序目标具体化为效用与收入的双重目标，这是本文设计需求的核心。

- inherits_from_previous_cn：承接排序框架这一目标。

- changes_argument_state_cn：设定设计约束：必须同时满足效用和平台收入。

- sets_up_next_cn：解释为何需要结构模型和边际数据。

- failure_if_removed_cn：读者不知道排序目标是什么，CPA边际的引入缺乏理由。

- evidence_pointer：Abstract第四句

### 5. Abstract P1 S5

- order：5

- locator：Abstract P1 S5

- paraphrase_cn：指定一个点击与安装选择的结构模型，并由一组数值与文本协变量联合估计。

- move_code：STUDY_OVERVIEW

- statement_status：method_decision

- why_here_cn：说明拟用方法：两阶段结构模型和多种协变量。

- inherits_from_previous_cn：承接效用与边际双重目标，说明如何估计效用。

- changes_argument_state_cn：给出估计策略的概貌。

- sets_up_next_cn：为下一句数据集的独特性做铺垫。

- failure_if_removed_cn：摘要缺少方法预告，结果与贡献缺乏工具支撑。

- evidence_pointer：Abstract第五句

### 6. Abstract P1 S6

- order：6

- locator：Abstract P1 S6

- paraphrase_cn：新数据集达到用户-印象粒度，且独特地包含平台实际获得的CPA边际。

- move_code：DATA

- statement_status：fact

- why_here_cn：强调数据两大优势：粒度细和含真实边际，这是本文区别于既有研究的关键资源。

- inherits_from_previous_cn：承接结构模型需要的数据输入。

- changes_argument_state_cn：把数据资源上升为研究能力。

- sets_up_next_cn：为政策实验量化收入提供具体条件。

- failure_if_removed_cn：摘要无法说明为什么本文能做个性化政策实验。

- evidence_pointer：Abstract第六句

### 7. Abstract P1 S7

- order：7

- locator：Abstract P1 S7

- paraphrase_cn：进行一系列政策实验量化个性化的价值。

- move_code：STUDY_OVERVIEW

- statement_status：method_decision

- why_here_cn：把评价方式定为政策实验，为后面的结果句做铺垫。

- inherits_from_previous_cn：承接结构模型与CPA边际数据。

- changes_argument_state_cn：将研究重心引向反事实比较。

- sets_up_next_cn：引出核心结果：个性化混合排序最优。

- failure_if_removed_cn：摘要缺少评价环节，结果没有来源。

- evidence_pointer：Abstract第七句

### 8. Abstract P1 S8

- order：8

- locator：Abstract P1 S8

- paraphrase_cn：个性化混合边际与效用边际排序胜过其他个性化方法，包括仅效用或效用加边际的方法。

- move_code：RESULT

- statement_status：empirical_result

- why_here_cn：给出全文最核心的量化结果，点明HMUM设计的优越性。

- inherits_from_previous_cn：承接政策实验。

- changes_argument_state_cn：确定了最优制品。

- sets_up_next_cn：为最后一句总体贡献提供依据。

- failure_if_removed_cn：摘要没有结果，贡献句成为空话。

- evidence_pointer：Abstract第八句

### 9. Abstract P1 S9

- order：9

- locator：Abstract P1 S9

- paraphrase_cn：总体而言，分析展示平台如何利用常规点击流数据个性化应用印象排序，从而更有效地变现移动应用分发。

- move_code：CONTRIBUTION

- statement_status：contribution_claim

- why_here_cn：把具体结果上升为平台可复用的方法论贡献，同时回应摘要第一句的个性化背景。

- inherits_from_previous_cn：承接HMUM最优这一结果。

- changes_argument_state_cn：完成摘要从背景到贡献的闭环。

- sets_up_next_cn：无，摘要结束。

- failure_if_removed_cn：摘要没有贡献句，读者不知道研究为什么重要。

- evidence_pointer：Abstract第九句

## 引言逐句图谱

### 1. Introduction P1 S1

- order：1

- locator：Introduction P1 S1

- paraphrase_cn：移动应用市场过去二十年指数增长，2020年下载2180亿次，销售额1430亿美元。

- move_code：CONTEXT

- statement_status：fact

- why_here_cn：用市场规模的客观数据建立问题的重要性，为后续平台收入主张提供宏观背景。

- inherits_from_previous_cn：无，全文开场。

- changes_argument_state_cn：确立移动应用经济是重要研究场景。

- sets_up_next_cn：引出第三方分发平台的出现。

- failure_if_removed_cn：问题的重要性缺少数据支撑。

- evidence_pointer：Section 1 P1 S1

### 2. Introduction P1 S2

- order：2

- locator：Introduction P1 S2

- paraphrase_cn：在原生应用商店之外出现了第三方应用分发平台，包括本文研究的一家。

- move_code：CONTEXT

- statement_status：fact

- why_here_cn：从市场规模收窄到第三方平台，为平台排序的实际问题定位。

- inherits_from_previous_cn：承接移动应用市场增长的大背景。

- changes_argument_state_cn：引入研究对象：第三方分发平台。

- sets_up_next_cn：为下一句的下载量和收入预测提供主体。

- failure_if_removed_cn：读者不清楚研究平台属于哪一类。

- evidence_pointer：Section 1 P1 S2

### 3. Introduction P1 S3

- order：3

- locator：Introduction P1 S3

- paraphrase_cn：到2021年第三方平台预计下载超1000亿次，年收入360亿美元，且以12%年增长。

- move_code：CONTEXT

- statement_status：fact

- why_here_cn：用具体预测进一步放大第三方平台的商业重要性，为排序收入问题提供现实紧迫性。

- inherits_from_previous_cn：承接第三方平台的出现。

- changes_argument_state_cn：量级化第三方平台的经济意义。

- sets_up_next_cn：引出平台CPA商业模式和收入决定因素。

- failure_if_removed_cn：第三方平台的重要性仍停留在定性层面。

- evidence_pointer：Section 1 P1 S3

### 4. Introduction P1 S4

- order：4

- locator：Introduction P1 S4

- paraphrase_cn：第三方平台通常运行CPA模式，按每安装预先约定的费率获得补偿。

- move_code：PRACTICAL_STAKES

- statement_status：fact

- why_here_cn：解释平台的收入来源机制，建立排序与收入之间的直接联系。

- inherits_from_previous_cn：承接第三方平台收入和下载的规模。

- changes_argument_state_cn：把注意力转向CPA收入机制。

- sets_up_next_cn：为下一句的收入取决于展示顺序做逻辑铺垫。

- failure_if_removed_cn：平台收入如何产生不清楚，排序问题失去经济含义。

- evidence_pointer：Section 1 P1 S4

### 5. Introduction P1 S5

- order：5

- locator：Introduction P1 S5

- paraphrase_cn：平台收入如同产品搜索引擎，取决于展示哪些应用印象以及按什么顺序展示。

- move_code：PRACTICAL_STAKES

- statement_status：author_inference

- why_here_cn：把CPA模式与排序设计直接挂钩，建立研究问题的核心机制。

- inherits_from_previous_cn：承接CPA收入机制。

- changes_argument_state_cn：确立排序是收入决策变量。

- sets_up_next_cn：为批评现有平台排序简单化提供对照。

- failure_if_removed_cn：排序与收入的因果关系断裂。

- evidence_pointer：Section 1 P1 S5

### 6. Introduction P1 S6

- order：6

- locator：Introduction P1 S6

- paraphrase_cn：然而第三方分发平台的排序策略通常很粗糙，使用CTR、转化率和CPA边际等简单指标，忽视用户价值的基本驱动因素。

- move_code：LIMITATION

- statement_status：fact

- why_here_cn：指出现实平台实践缺陷，制造改进空间，是问题化的关键一步。

- inherits_from_previous_cn：承接排序决定收入的前提。

- changes_argument_state_cn：从描述现状转为指出不足。

- sets_up_next_cn：为引入既有文献中平均效用排序的证据。

- failure_if_removed_cn：研究动机失去现实基础，变成纯学术偏好。

- evidence_pointer：Section 1 P1 S6

### 7. Introduction P1 S7

- order：7

- locator：Introduction P1 S7

- paraphrase_cn：既有工作显示在排序中考虑平均消费者效用能带来更高平台收入。

- move_code：PRIOR_KNOWLEDGE

- statement_status：prior_literature

- why_here_cn：引入文献基准：平均效用排序有效，为本文从平均效用走向个性化做铺垫。

- inherits_from_previous_cn：承接平台排序粗糙这一现实。

- changes_argument_state_cn：把可行性锚定在既有研究上。

- sets_up_next_cn：为本文的研究目标：个性化排序。

- failure_if_removed_cn：个性化排序缺乏文献基础，读者无法判断其与已有工作的关系。

- evidence_pointer：Section 1 P1 S7

### 8. Introduction P1 S8

- order：8

- locator：Introduction P1 S8

- paraphrase_cn：本文在此基础上展示基于个体效用而非平均效用的个性化排序可同时提高平台利润和消费者效用。

- move_code：RQ_OR_OBJECTIVE

- statement_status：author_inference

- why_here_cn：提出本文相对文献的增量目标：从平均效用升级到个体效用。

- inherits_from_previous_cn：承接平均效用排序有效的文献结论。

- changes_argument_state_cn：设置全文主张：个性化优于平均化。

- sets_up_next_cn：为第二段的个性化概念和定义提供舞台。

- failure_if_removed_cn：引言没有明确的研究主张。

- evidence_pointer：Section 1 P1 S8

### 9. Introduction P2 S1

- order：9

- locator：Introduction P2 S1

- paraphrase_cn：个性化被定义为根据过去行为和显示偏好为个体匹配内容、产品和服务的能力。

- move_code：DEFINITION

- statement_status：prior_literature

- why_here_cn：给出个性化标准定义，为后文概念辨析提供基础。

- inherits_from_previous_cn：承接上一段个性化排序目标。

- changes_argument_state_cn：界定核心概念。

- sets_up_next_cn：为个性化收益机制句提供定义基础。

- failure_if_removed_cn：个性化概念不清，后续讨论失去锚。

- evidence_pointer：Section 1 P2 S1

### 10. Introduction P2 S2

- order：10

- locator：Introduction P2 S2

- paraphrase_cn：个性化在不同情境被研究，包括搜索引擎、推荐系统、个性化定价、定向营销等。

- move_code：PRIOR_KNOWLEDGE

- statement_status：prior_literature

- why_here_cn：说明个性化是一个成熟研究域，但本文情境未覆盖。

- inherits_from_previous_cn：承接个性化定义。

- changes_argument_state_cn：把个性化定位成文献丰富的研究方向。

- sets_up_next_cn：为个体获益机制句提供多个对照情境。

- failure_if_removed_cn：个性化的普遍性证据不足。

- evidence_pointer：Section 1 P2 S2

### 11. Introduction P2 S3

- order：11

- locator：Introduction P2 S3

- paraphrase_cn：用户受益于个性化因为它降低搜索成本，帮助找到更相关的内容、时间和地点。

- move_code：MECHANISM

- statement_status：prior_literature

- why_here_cn：解释个性化为什么产生价值：搜索成本机制。

- inherits_from_previous_cn：承接个性化定义和普遍文献。

- changes_argument_state_cn：建立个性化正向收益机制。

- sets_up_next_cn：为满意度、转化率和收入句提供因果链起点。

- failure_if_removed_cn：个性化价值缺少微观机制。

- evidence_pointer：Section 1 P2 S3

### 12. Introduction P2 S4

- order：12

- locator：Introduction P2 S4

- paraphrase_cn：更高满意度转化为更高留存、转化率、支付意愿和单位时间平均收入。

- move_code：MECHANISM

- statement_status：prior_literature

- why_here_cn：把搜索成本降低延伸为商业收益链条。

- inherits_from_previous_cn：承接搜索成本下降。

- changes_argument_state_cn：连接个性化与收入。

- sets_up_next_cn：为异质性转收入句铺路。

- failure_if_removed_cn：个性化到收入的机制链断裂。

- evidence_pointer：Section 1 P2 S4

### 13. Introduction P2 S5

- order：13

- locator：Introduction P2 S5

- paraphrase_cn：从某种意义看，个性化是把客户异质性通过匹配显示偏好与定制内容转化为增量收入机会。

- move_code：MECHANISM

- statement_status：author_inference

- why_here_cn：把个性化与异质性直接挂钩，为本文用个体效用排序的核心思想提供概念基础。

- inherits_from_previous_cn：承接收入收益链条。

- changes_argument_state_cn：把异质性引入个性化讨论。

- sets_up_next_cn：引出个性化与定制化的区分。

- failure_if_removed_cn：个性化与异质性的联系缺失，后文个体效用估计显得突兀。

- evidence_pointer：Section 1 P2 S5

### 14. Introduction P2 S6

- order：14

- locator：Introduction P2 S6

- paraphrase_cn：有必要区分个性化与定制化，尽管二者常被混用。

- move_code：DISTINCTION

- statement_status：prior_literature

- why_here_cn：在概念上划清本文研究的是平台为用户完成的个性化，而非用户主动定制。

- inherits_from_previous_cn：承接个性化的收益讨论。

- changes_argument_state_cn：明确本文所处概念子类。

- sets_up_next_cn：为引述定制化与个性化差别定义。

- failure_if_removed_cn：本文个性化与用户配置的定制化容易混淆。

- evidence_pointer：Section 1 P2 S6

### 15. Introduction P2 S7

- order：15

- locator：Introduction P2 S7

- paraphrase_cn：简述区分：定制化由用户发起，个性化是平台为用户完成。

- move_code：DISTINCTION

- statement_status：prior_literature

- why_here_cn：用简单定义固化概念边界，确保读者理解本文的个性化排序是平台行为。

- inherits_from_previous_cn：承接定制化与个性化区分的需要。

- changes_argument_state_cn：锁定本文研究范畴。

- sets_up_next_cn：为引言后的文献表和工作分类提供概念准备。

- failure_if_removed_cn：概念边界模糊，后文平台主动排序的描述缺少理论标签。

- evidence_pointer：Section 1 P2 S7

### 16. Introduction P3 S1（Table 1附近）

- order：16

- locator：Introduction P3 S1（Table 1附近）

- paraphrase_cn：现有排序研究的共同点是消费者从排序列表中选择，结果主要是点击和转化。

- move_code：PRIOR_KNOWLEDGE

- statement_status：prior_literature

- why_here_cn：总结既有排序文献的共同特征，为Table 1的比较提供标准。

- inherits_from_previous_cn：承接上一段个性化与排序概念。

- changes_argument_state_cn：把文献归为可比较的类别。

- sets_up_next_cn：为指出文献是否考虑排序设计及其基础做铺垫。

- failure_if_removed_cn：Table 1比较标准缺失。

- evidence_pointer：Section 2.1 P1 S1（引言中对应概述，Table 1后）

### 17. Introduction P3 S2（Table 1附近）

- order：17

- locator：Introduction P3 S2（Table 1附近）

- paraphrase_cn：大部分排序设计基于平均效用，只有Yoganarasimhan在搜索中基于搜索查询做了搜索词层面的个性化，本文在应用分发中基于个体效用与边际做个性化。

- move_code：GAP

- statement_status：prior_literature

- why_here_cn：用Table 1直接显示本文在排序设计矩阵中的独特位置。

- inherits_from_previous_cn：承接排序文献分类。

- changes_argument_state_cn：把文献现状转化为研究缺口。

- sets_up_next_cn：为研究问题句提供空间。

- failure_if_removed_cn：本文新意无处安放。

- evidence_pointer：Section 1 Table 1及前一句

### 18. Introduction P4 S1

- order：18

- locator：Introduction P4 S1

- paraphrase_cn：用Adomavicius框架定位本文个性化类型：推荐产品、消费者中心、个体粒度、非侵入式。

- move_code：CLASSIFICATION

- statement_status：prior_literature

- why_here_cn：给本文个性化方法一个标准分类学位置，说明研究身份。

- inherits_from_previous_cn：承接个性化概念辨析和文献缺口。

- changes_argument_state_cn：把本文方法限定为个体级非侵入式推荐。

- sets_up_next_cn：为点击流显示偏好的前提做铺垫。

- failure_if_removed_cn：本文个性化类型缺少学术坐标，容易被误读为定制化。

- evidence_pointer：Section 1 P4

### 19. Introduction P4 S2

- order：19

- locator：Introduction P4 S2

- paraphrase_cn：本文排序方案的前提是点击流中的显示偏好可用来恢复消费者偏好并个性化应用排序。

- move_code：THEORY_INTRO

- statement_status：theory_claim

- why_here_cn：提出全文方法论前提：显示偏好映射到效用函数。

- inherits_from_previous_cn：承接个性化类型定位。

- changes_argument_state_cn：设定本文的实证基础。

- sets_up_next_cn：为点击流数据高频互动的描述做铺垫。

- failure_if_removed_cn：结构估计与个性化排序缺少理论入口。

- evidence_pointer：Section 1 P5 S1

### 20. Introduction P4 S3

- order：20

- locator：Introduction P4 S3

- paraphrase_cn：移动应用分发情境比一般产品搜索有更频繁的点击与转化互动。

- move_code：CONTEXT

- statement_status：fact

- why_here_cn：说明为什么这个情境特别适合用点击流做显示偏好恢复。

- inherits_from_previous_cn：承接点击流显示偏好的前提。

- changes_argument_state_cn：强化该情境的数据可行性。

- sets_up_next_cn：为长期积累大量选择行为做铺垫。

- failure_if_removed_cn：为什么选应用分发而非其他情境缺乏理由。

- evidence_pointer：Section 1 P5 S2

### 21. Introduction P4 S4

- order：21

- locator：Introduction P4 S4

- paraphrase_cn：长期来看这会累积大量异质用户的点击和安装选择，即显示偏好。

- move_code：CONTEXT

- statement_status：fact

- why_here_cn：说明平台能积累数据规模，让个性化学习可行。

- inherits_from_previous_cn：承接频繁互动。

- changes_argument_state_cn：建立数据资源丰富性。

- sets_up_next_cn：为平台学习需求的行动机会做铺垫。

- failure_if_removed_cn：数据可行性链条断裂。

- evidence_pointer：Section 1 P5 S3

### 22. Introduction P4 S5

- order：22

- locator：Introduction P4 S5

- paraphrase_cn：这为平台提供可行动机会去了解应用需求并用于更有效的排序与变现。

- move_code：PRACTICAL_STAKES

- statement_status：author_inference

- why_here_cn：把数据积累转化为平台可行动的研究机会，引出研究问题。

- inherits_from_previous_cn：承接显示偏好的积累。

- changes_argument_state_cn：把数据事实转为管理机会。

- sets_up_next_cn：为三个未解决问题做直接铺垫。

- failure_if_removed_cn：研究意义停留在数据描述层面。

- evidence_pointer：Section 1 P5 S4

### 23. Introduction P5 S1

- order：23

- locator：Introduction P5 S1

- paraphrase_cn：尽管排序设计已经引起研究关注，本文提出三个此前未解决的问题：效用受什么影响、如何平衡效用与边际并设计个性化排序、不同个性化方案如何比较。

- move_code：RQ

- statement_status：author_inference

- why_here_cn：用三个编号问题清晰定义全文研究任务，组织后续章节。

- inherits_from_previous_cn：承接平台学习机会和文献缺口。

- changes_argument_state_cn：把全文结构锚定在三个问题上。

- sets_up_next_cn：为数据、模型和政策实验各自的章节做导航。

- failure_if_removed_cn：研究问题不清，正文各节缺乏共同目标。

- evidence_pointer：Section 1 P6

### 24. Introduction P6 S1

- order：24

- locator：Introduction P6 S1

- paraphrase_cn：为回答问题，获得来自一家管理美国某大型移动网络首页的营销代理的独特点击下载数据集。

- move_code：DATA

- statement_status：fact

- why_here_cn：宣布本文的独特数据资源，支撑三个研究问题。

- inherits_from_previous_cn：承接三个研究问题的数据需求。

- changes_argument_state_cn：把问题研究落到可操作数据上。

- sets_up_next_cn：为后续offer wall和数据结构的描述做铺垫。

- failure_if_removed_cn：研究问题没有数据支撑。

- evidence_pointer：Section 1 P7 S1

### 25. Introduction P6 S2

- order：25

- locator：Introduction P6 S2

- paraphrase_cn：该代理运营充当应用分发平台的offer wall。

- move_code：DATA

- statement_status：fact

- why_here_cn：明确数据来自哪个具体平台形态。

- inherits_from_previous_cn：承接营销代理的数据来源。

- changes_argument_state_cn：把数据情境固定为offer wall。

- sets_up_next_cn：为后续平台业务模型图做铺垫。

- failure_if_removed_cn：数据来源不具体。

- evidence_pointer：Section 1 P7 S2

### 26. Introduction P6 S3

- order：26

- locator：Introduction P6 S3

- paraphrase_cn：用户-印象级数据包含应用印象及相应点击和安装响应。

- move_code：DATA

- statement_status：fact

- why_here_cn：强调数据的粒度级别，这是个性化估计的必要条件。

- inherits_from_previous_cn：承接offer wall平台。

- changes_argument_state_cn：把数据粒度上升为后续模型的输入条件。

- sets_up_next_cn：为结构模型估计提供对象。

- failure_if_removed_cn：个性化估计的数据条件不成立。

- evidence_pointer：Section 1 P7 S3

### 27. Introduction P6 S4

- order：27

- locator：Introduction P6 S4

- paraphrase_cn：用层级贝叶斯框架下的两阶段二元Probit模型估计点击和下载效用，自变量为广泛的数值与文本应用特征。

- move_code：STUDY_OVERVIEW

- statement_status：method_decision

- why_here_cn：给出全文核心计量方法，回应第二和第三个研究问题的方法需要。

- inherits_from_previous_cn：承接用户-印象级数据。

- changes_argument_state_cn：确定模型与估计策略。

- sets_up_next_cn：为数值文本变量细节做铺垫。

- failure_if_removed_cn：实证分析缺乏模型框架。

- evidence_pointer：Section 1 P7 S4

### 28. Introduction P6 S5

- order：28

- locator：Introduction P6 S5

- paraphrase_cn：数值变量包括屏幕排名、星级、评论量和下载量；文本特征包括从标题、描述和评论提取的信息量、模糊度和情感。

- move_code：STUDY_OVERVIEW

- statement_status：method_decision

- why_here_cn：列举协变量类别，为后文数据章节和效用函数设定提供预告。

- inherits_from_previous_cn：承接模型中的自变量集合。

- changes_argument_state_cn：明确实证输入的具体构成。

- sets_up_next_cn：为参数估计结果和文本分析做铺垫。

- failure_if_removed_cn：读者无法预期数据变量的范围。

- evidence_pointer：Section 1 P7 S5

### 29. Introduction P7 S1

- order：29

- locator：Introduction P7 S1

- paraphrase_cn：参数估计提供若干洞察：与先前研究一致，确认排名与质量的显著效应。

- move_code：RESULT_PREVIEW

- statement_status：empirical_result

- why_here_cn：在引言预告核心实证结果，让读者在方法论细节前知道关键发现。

- inherits_from_previous_cn：承接结构模型估计。

- changes_argument_state_cn：从方法转向结果。

- sets_up_next_cn：为具体量化边际效应做铺垫。

- failure_if_removed_cn：引言的实证说服力减弱。

- evidence_pointer：Section 1 P8 S1

### 30. Introduction P7 S2

- order：30

- locator：Introduction P7 S2

- paraphrase_cn：排名每上移一位CTR提高4.26%；星级每增加一星点击和安装分别提高2.91%和1.37%。

- move_code：RESULT_PREVIEW

- statement_status：empirical_result

- why_here_cn：用经济边际效应量化排名和评分的商业价值，为排序实验做理由。

- inherits_from_previous_cn：承接排名与质量效应。

- changes_argument_state_cn：给出排名影响的具体数值。

- sets_up_next_cn：为文本变量效应句提供对照。

- failure_if_removed_cn：排名重要性缺乏量化证据。

- evidence_pointer：Section 1 P8 S2

### 31. Introduction P7 S3

- order：31

- locator：Introduction P7 S3

- paraphrase_cn：消费者偏好更有信息量的标题：标题长度增加1%带来CTR增加2.12%，标题每增加一个同义词模糊度使CTR下降3.15%。

- move_code：RESULT_PREVIEW

- statement_status：empirical_result

- why_here_cn：预告文本变量在点击阶段的作用，说明文本特征不是装饰。

- inherits_from_previous_cn：承接参数估计洞察。

- changes_argument_state_cn：把文本变量纳入核心结果。

- sets_up_next_cn：为情感词句做铺垫。

- failure_if_removed_cn：文本分析的重要性在引言中缺失。

- evidence_pointer：Section 1 P8 S3

### 32. Introduction P7 S4

- order：32

- locator：Introduction P7 S4

- paraphrase_cn：标题中的限制性词语吸引更多关注，而积极描述提高安装倾向。

- move_code：RESULT_PREVIEW

- statement_status：empirical_result

- why_here_cn：预告情感变量的通道差异：点击对标题、安装对描述。

- inherits_from_previous_cn：承接文本变量效应。

- changes_argument_state_cn：区分点击与安装的文本驱动因素。

- sets_up_next_cn：为异质性句提供具体内容。

- failure_if_removed_cn：文本效应不完整。

- evidence_pointer：Section 1 P8 S4

### 33. Introduction P7 S5

- order：33

- locator：Introduction P7 S5

- paraphrase_cn：消费者对文本变量的反应比对数值变量更异质。

- move_code：RESULT_PREVIEW

- statement_status：empirical_result

- why_here_cn：预告异质性方差结果，为个性化排序必要性提供直接依据。

- inherits_from_previous_cn：承接点击与安装文本效应。

- changes_argument_state_cn：把异质性引入结果叙事。

- sets_up_next_cn：为个性化排序的政策实验做逻辑准备。

- failure_if_removed_cn：个性化排序的动机不足。

- evidence_pointer：Section 1 P8 S5

### 34. Introduction P8 S1

- order：34

- locator：Introduction P8 S1

- paraphrase_cn：利用结构参数估计进行系列政策实验评估个性化的增量价值。

- move_code：STUDY_OVERVIEW

- statement_status：method_decision

- why_here_cn：宣布评价方式：基于结构参数的系列政策实验。

- inherits_from_previous_cn：承接个体效用参数。

- changes_argument_state_cn：把结果重心导向排序方案比较。

- sets_up_next_cn：引出平均效用排序与个性化排序对比。

- failure_if_removed_cn：个性化价值没有评估手段。

- evidence_pointer：Section 1 P9 S1

### 35. Introduction P8 S2

- order：35

- locator：Introduction P8 S2

- paraphrase_cn：比较平均效用排序与个体层面个性化排序。

- move_code：STUDY_OVERVIEW

- statement_status：method_decision

- why_here_cn：明确政策实验中最重要的对照：平均 vs 个性化。

- inherits_from_previous_cn：承接政策实验。

- changes_argument_state_cn：设定核心比较。

- sets_up_next_cn：为个性化提升收入的结果做铺垫。

- failure_if_removed_cn：政策实验没有对照设计。

- evidence_pointer：Section 1 P9 S2

### 36. Introduction P8 S3

- order：36

- locator：Introduction P8 S3

- paraphrase_cn：个性化显著提升平台期望收入。

- move_code：RESULT_PREVIEW

- statement_status：empirical_result

- why_here_cn：给出政策实验总体结论。

- inherits_from_previous_cn：承接平均与个性化对照。

- changes_argument_state_cn：确立个性化价值。

- sets_up_next_cn：为引进HMUM的进一步改进做铺垫。

- failure_if_removed_cn：个性化收益主张缺少结果支撑。

- evidence_pointer：Section 1 P9 S3

### 37. Introduction P8 S4

- order：37

- locator：Introduction P8 S4

- paraphrase_cn：为进一步提高平台盈利，提出新颖的个性化排序方案HMUM。

- move_code：DESIGN_DECISION

- statement_status：design_decision

- why_here_cn：在个性化收益基础上引入本文核心制品HMUM，说明设计的必要性。

- inherits_from_previous_cn：承接个性化显著提升收入。

- changes_argument_state_cn：推出核心设计。

- sets_up_next_cn：为HMUM的混合逻辑句做铺垫。

- failure_if_removed_cn：全文缺少核心制品。

- evidence_pointer：Section 1 P9 S4

### 38. Introduction P8 S5

- order：38

- locator：Introduction P8 S5

- paraphrase_cn：混合方法融合两种排序，精细平衡下载绩效与收入边际。

- move_code：DESIGN_DECISION

- statement_status：design_decision

- why_here_cn：用一句话点明HMUM的设计目的：平衡双目标。

- inherits_from_previous_cn：承接HMUM提出。

- changes_argument_state_cn：定义设计原则。

- sets_up_next_cn：为混合排序超过单指标排序的声明做铺垫。

- failure_if_removed_cn：HMUM的内部逻辑缺失。

- evidence_pointer：Section 1 P9 S5

### 39. Introduction P8 S6

- order：39

- locator：Introduction P8 S6

- paraphrase_cn：证明这种混合排序优于基于效用或效用加边际的替代方案，尤其在个性化时。

- move_code：RESULT_PREVIEW

- statement_status：empirical_result

- why_here_cn：给出HMUM的政策实验结果预告。

- inherits_from_previous_cn：承接HMUM设计。

- changes_argument_state_cn：把设计主张转化为经验结果。

- sets_up_next_cn：为强调混合方法常见被忽视做铺垫。

- failure_if_removed_cn：HMUM优势缺少结果支持。

- evidence_pointer：Section 1 P9 S6

### 40. Introduction P8 S7

- order：40

- locator：Introduction P8 S7

- paraphrase_cn：既有研究倾向从替代方案中选一个最优算法，忽视混合方案的潜力。

- move_code：PRIOR_KNOWLEDGE

- statement_status：prior_literature

- why_here_cn：指出文献空白：忽略混合排序，用来提升本文新颖性。

- inherits_from_previous_cn：承接HMUM优势声明。

- changes_argument_state_cn：把HMUM与文献做法形成对照。

- sets_up_next_cn：为具体混合排序结构描述做铺垫。

- failure_if_removed_cn：HMUM的学术贡献缺少文献对照。

- evidence_pointer：Section 1 P9 S7

### 41. Introduction P8 S8

- order：41

- locator：Introduction P8 S8

- paraphrase_cn：HMUM向每个用户呈现两部分：顶部放最喜爱应用按CPA边际降序。

- move_code：DESIGN_DECISION

- statement_status：design_decision

- why_here_cn：给出HMUM第一部分具体规则。

- inherits_from_previous_cn：承接混合排序方案。

- changes_argument_state_cn：明确顶部排序机制。

- sets_up_next_cn：为解释为什么用户会点击高效用应用做铺垫。

- failure_if_removed_cn：HMUM不可操作。

- evidence_pointer：Section 1 P9 S8

### 42. Introduction P8 S9

- order：42

- locator：Introduction P8 S9

- paraphrase_cn：用户无论精确顺序如何都可能点击这些高效用印象，因此CPA边际成为增量收入的关键。

- move_code：MECHANISM

- statement_status：theory_claim

- why_here_cn：解释顶部为什么按边际排序：效用差异可忽略时边际决定收入。

- inherits_from_previous_cn：承接顶部最喜爱应用按边际排序。

- changes_argument_state_cn：把设计规则转化为机制命题。

- sets_up_next_cn：为下半部分效用×边际排序做铺垫。

- failure_if_removed_cn：HMUM顶部规则失去理论依据。

- evidence_pointer：Section 1 P9 S9

### 43. Introduction P8 S10

- order：43

- locator：Introduction P8 S10

- paraphrase_cn：下半部分其余印象按效用×边际的乘积降序，同样个性化。

- move_code：DESIGN_DECISION

- statement_status：design_decision

- why_here_cn：给出HMUM第二部分排序规则，完整定义制品。

- inherits_from_previous_cn：承接顶部排序机制。

- changes_argument_state_cn：完成HMUM定义。

- sets_up_next_cn：为整体平衡消费者价值与平台收入的总结做铺垫。

- failure_if_removed_cn：HMUM缺失下半段，制品不完整。

- evidence_pointer：Section 1 P9 S10

### 44. Introduction P8 S11

- order：44

- locator：Introduction P8 S11

- paraphrase_cn：结果混合方案旨在平衡驱动个体效用与收入边际的力量，同时提升平台收入和客户价值。

- move_code：DESIGN_DECISION

- statement_status：contribution_claim

- why_here_cn：把HMUM设计总结为双目标平衡，呼应摘要中的要求。

- inherits_from_previous_cn：承接HMUM两部分规则。

- changes_argument_state_cn：把具体规则升华为设计理念。

- sets_up_next_cn：为结论中的贡献预告做铺垫。

- failure_if_removed_cn：HMUM没有价值主张。

- evidence_pointer：Section 1 P9 S11

### 45. Introduction P8 S12

- order：45

- locator：Introduction P8 S12

- paraphrase_cn：本文对文献和实践的进一步贡献在结论部分讨论。

- move_code：TRANSITION

- statement_status：fact

- why_here_cn：把贡献细节推迟到结论，避免引言过长。

- inherits_from_previous_cn：承接HMUM贡献声明。

- changes_argument_state_cn：暂时收束贡献讨论。

- sets_up_next_cn：为论文结构导航句做铺垫。

- failure_if_removed_cn：引言缺少贡献出口。

- evidence_pointer：Section 1 P9 S12

### 46. Introduction P9 S1

- order：46

- locator：Introduction P9 S1

- paraphrase_cn：论文结构如下：文献、数据、模型、结果、政策实验和结论。

- move_code：SIGNPOST

- statement_status：fact

- why_here_cn：用章节导航帮助读者预设全文组织。

- inherits_from_previous_cn：承接全文已完成的问题与方法设定。

- changes_argument_state_cn：明确章节顺序。

- sets_up_next_cn：为读者进入文献综述做准备。

- failure_if_removed_cn：读者缺少阅读地图。

- evidence_pointer：Section 1最后一段

## 引言逐段图谱

### 1. 1

- paragraph_locator：Introduction P1

- paragraph_job_cn：建立移动应用和第三方平台的市场重要性，说明CPA收入机制，指出现实排序粗糙，引入文献中平均效用排序的有效性，并提出本文个性化排序目标。

- opening_move_cn：用市场规模数据开场。

- development_move_cn：从市场到平台再到CPA收入机制，逐层收窄并连接排序。

- pivot_move_cn：在现实缺陷处转折，点出平台排序简单。

- closing_move_cn：引入文献平均效用排序并宣布本文个性化目标。

- needs_next_paragraph_cn：下一段需要定义并辨析个性化概念。

### 2. 2

- paragraph_locator：Introduction P2

- paragraph_job_cn：定义个性化并解释其收益机制，同时区分个性化与定制化，把本文锁定为平台完成的个性化。

- opening_move_cn：从定义开始。

- development_move_cn：列举文献情境，展开搜索成本到收入的机制链。

- pivot_move_cn：在机制链后转向个性化和定制化的概念区分。

- closing_move_cn：用定制化与个性化的定义界定本文范畴。

- needs_next_paragraph_cn：下一段需要把个性化放进排序文献的具体位置。

### 3. 3

- paragraph_locator：Introduction P3（Table 1段）

- paragraph_job_cn：用Table 1把本文与相关排序研究并置，直接展示本文数据与设计上的空白。

- opening_move_cn：概述既有排序研究共同特征。

- development_move_cn：分类是否考虑排序设计及排序基础。

- pivot_move_cn：从列表转向指出多数研究基于平均效用。

- closing_move_cn：把本文标记为唯一在应用分发中基于个体效用与边际。

- needs_next_paragraph_cn：下一段需要在分类框架中进一步定位本文个性化类型。

### 4. 4

- paragraph_locator：Introduction P4

- paragraph_job_cn：用Adomavicius框架定位本文的个性化类型，并陈述点击流显示偏好可恢复偏好的核心前提。

- opening_move_cn：以Adomavicius框架的四个维度开场。

- development_move_cn：逐维分配本文位置。

- pivot_move_cn：从分类转向前提：显示偏好可恢复偏好。

- closing_move_cn：强调移动分发情境点击互动频繁，积累数据并创造平台学习机会。

- needs_next_paragraph_cn：下一段需要把这些机会转化为明确研究问题。

### 5. 5

- paragraph_locator：Introduction P5

- paragraph_job_cn：提出三个编号研究问题，组织全文逻辑。

- opening_move_cn：先行承认排序设计已有研究。

- development_move_cn：用三个问题把缺口逐一具体化。

- pivot_move_cn：无，整段聚焦问题定义。

- closing_move_cn：以三个问题作为后文章节任务。

- needs_next_paragraph_cn：下一段需要说明用什么数据来回答问题。

### 6. 6

- paragraph_locator：Introduction P6

- paragraph_job_cn：介绍独特数据来源、用户-印象粒度以及两阶段结构模型和协变量。

- opening_move_cn：宣布获得独特数据。

- development_move_cn：从代理到offer wall再到数据粒度和模型。

- pivot_move_cn：从数据转入模型输入变量细节。

- closing_move_cn：列举数值和文本特征，预告模型估计范围。

- needs_next_paragraph_cn：下一段需要报告核心参数估计发现。

### 7. 7

- paragraph_locator：Introduction P7

- paragraph_job_cn：预告核心参数估计结果，包括排名、质量、文本变量效应和异质性。

- opening_move_cn：以参数估计总体洞察开场。

- development_move_cn：依次给出排名、评分、标题信息性、标题模糊度和情感效应的数值。

- pivot_move_cn：从具体变量效应转向更一般的文本与数值异质性对比。

- closing_move_cn：用异质性结论为个性化必要性铺路。

- needs_next_paragraph_cn：下一段需要把参数用于排序政策实验。

### 8. 8

- paragraph_locator：Introduction P8

- paragraph_job_cn：预告政策实验设计并定义HMUM制品，用机制解释其为何有效。

- opening_move_cn：宣布政策实验。

- development_move_cn：先给出个性化总体收益，再提出HMUM并描述两部分规则。

- pivot_move_cn：从一般个性化转向混合方法的优势。

- closing_move_cn：把HMUM总结为效用与边际的平衡。

- needs_next_paragraph_cn：下一段需要给出全文章节结构。

### 9. 9

- paragraph_locator：Introduction P9

- paragraph_job_cn：提供论文结构导航。

- opening_move_cn：直接给出章节顺序。

- development_move_cn：无实质展开。

- pivot_move_cn：无。

- closing_move_cn：无，纯导航。

- needs_next_paragraph_cn：无，进入文献综述。

## 理论到设计逐句图谱

### 1. Section 2.1 P1 S1

- order：1

- locator：Section 2.1 P1 S1

- paraphrase_cn：本文的点击与转化效用建模建立在研究在线搜索选择行为的既有工作之上。

- move_code：PRIOR_KNOWLEDGE

- statement_status：prior_literature

- why_here_cn：把本文模型放进排序选择文献的传统中。

- inherits_from_previous_cn：承接引言Table 1的研究分类。

- changes_argument_state_cn：确定理论来源。

- sets_up_next_cn：为屏幕排名作用的文献小结做铺垫。

- failure_if_removed_cn：模型缺乏文献根基。

- evidence_pointer：Section 2.1开头

### 2. Section 2.1 P1 S2

- order：2

- locator：Section 2.1 P1 S2

- paraphrase_cn：这些研究的共同点是消费者从排序列表中选择信息、内容或产品。

- move_code：PRIOR_KNOWLEDGE

- statement_status：prior_literature

- why_here_cn：概括情境共同性，为Table 1比较打基础。

- inherits_from_previous_cn：承接选择行为文献。

- changes_argument_state_cn：界定文献对象。

- sets_up_next_cn：为结果变量是点击和转换做铺垫。

- failure_if_removed_cn：文献范围不清晰。

- evidence_pointer：Section 2.1 P1 S2

### 3. Section 2.1 P1 S3

- order：3

- locator：Section 2.1 P1 S3

- paraphrase_cn：屏幕排名在消费者点击倾向中起显著作用。

- move_code：PRIOR_KNOWLEDGE

- statement_status：prior_literature

- why_here_cn：提炼排序文献的一致结论，为本文Rank变量提供依据。

- inherits_from_previous_cn：承接排序选择文献。

- changes_argument_state_cn：确立排名效应为已知事实。

- sets_up_next_cn：为说明既有研究把排名当协变量做铺垫。

- failure_if_removed_cn：Rank进入点击效用函数缺少文献支撑。

- evidence_pointer：Section 2.1 P1 S3

### 4. Section 2.1 P2 S1

- order：4

- locator：Section 2.1 P2 S1

- paraphrase_cn：这些研究把屏幕排名作为解释点击与转化决策的协变量；另一些研究则聚焦排序系统本身的设计。

- move_code：PRIOR_KNOWLEDGE

- statement_status：prior_literature

- why_here_cn：区分两代文献：把排名当解释变量 vs 把排名当设计对象。

- inherits_from_previous_cn：承接排名效应文献。

- changes_argument_state_cn：把本文归入排序设计分支。

- sets_up_next_cn：为平均效用排序文献的具体介绍做铺垫。

- failure_if_removed_cn：本文属于排序设计的定位不清晰。

- evidence_pointer：Section 2.1 P2

### 5. Section 2.1 P2 S2-S3

- order：5

- locator：Section 2.1 P2 S2-S3

- paraphrase_cn：Ghose等人的酒店排序系统按平均效用降序，且被证明能显著提高平台期望收入；Ursu在Expedia的田野实验也发现平均效用排序有益。

- move_code：PRIOR_KNOWLEDGE

- statement_status：prior_literature

- why_here_cn：给出平均效用排序的经典证据，为本文基准方案提供出处。

- inherits_from_previous_cn：承接排序设计分支。

- changes_argument_state_cn：确立平均效用排序是有效基准。

- sets_up_next_cn：为De los Santos和Koulayev扩展价格敏感性的介绍做铺垫。

- failure_if_removed_cn：基准方案（1a）没有文献来源。

- evidence_pointer：Section 2.1 P2

### 6. Section 2.1 P2 S4-S5

- order：6

- locator：Section 2.1 P2 S4-S5

- paraphrase_cn：De los Santos和Koulayev在平均效用基础上考虑分段价格敏感性；本文也使用结构估计加反事实，但不同之处在于研究个体层面的个性化增量收入。

- move_code：GAP

- statement_status：prior_literature

- why_here_cn：明确指出本文相对平均效用文献的两个差异：个性化与真实边际。

- inherits_from_previous_cn：承接平均效用排序文献。

- changes_argument_state_cn：形成本文与平均效用文献的分界。

- sets_up_next_cn：为下一句的未观察佣金率缺憾做铺垫。

- failure_if_removed_cn：本文新意与平均效用文献的对比不完整。

- evidence_pointer：Section 2.1 P2最后

### 7. Section 2.1 P3 S1-S2

- order：7

- locator：Section 2.1 P3 S1-S2

- paraphrase_cn：既有研究往往不知道平台与广告商之间的收入分享细节，因而无法量化平均效用排序对收入的精确影响。

- move_code：LIMITATION

- statement_status：prior_literature

- why_here_cn：指出数据缺口：没有真实佣金率，引出本文数据优势。

- inherits_from_previous_cn：承接平均效用排序的局限。

- changes_argument_state_cn：把数据缺憾作为文献空白。

- sets_up_next_cn：为介绍本文能获得CPA边际做铺垫。

- failure_if_removed_cn：CPA边际数据的贡献突出性减弱。

- evidence_pointer：Section 2.1 P3

### 8. Section 2.1 P3 S3

- order：8

- locator：Section 2.1 P3 S3

- paraphrase_cn：本文观察到真实CPA边际，从而能显式研究消费者效用驱动因素与平台收入之间的相互作用。

- move_code：DATA_ADVANTAGE

- statement_status：fact

- why_here_cn：建立真实边际数据的独特性，为政策实验提供事实基础。

- inherits_from_previous_cn：承接佣金率不可得文献缺憾。

- changes_argument_state_cn：把数据资源转化为研究能力。

- sets_up_next_cn：为下一段单一指标排序问题做铺垫。

- failure_if_removed_cn：效用与边际权衡的核心贡献失去数据载体。

- evidence_pointer：Section 2.1 P3 S3

### 9. Section 2.1 P4 S1

- order：9

- locator：Section 2.1 P4 S1

- paraphrase_cn：既有文献倾向用一个单一绩效指标排序所有产品，这种一刀切方法在效用最大化牺牲平台收入时可能产生不良后果。

- move_code：LIMITATION

- statement_status：author_inference

- why_here_cn：铺垫混合排序逻辑的必要性。

- inherits_from_previous_cn：承接效用与平台收入相互作用。

- changes_argument_state_cn：为引入混合算法建立批评对象。

- sets_up_next_cn：为Choi和Mela混合方案作对比。

- failure_if_removed_cn：混合排序的出现缺乏问题背景。

- evidence_pointer：Section 2.1 P4 S1

### 10. Section 2.1 P4 S2-S3

- order：10

- locator：Section 2.1 P4 S2-S3

- paraphrase_cn：混合效用与边际的算法可能带来更高总收入；Choi和Mela在在线市场中展示了这种混合方案，顶部5个槽位用于CPC拍卖，下方按预期销售收入排序。

- move_code：PRIOR_KNOWLEDGE

- statement_status：prior_literature

- why_here_cn：引入混合排序的思想源头，供本文借鉴与区分。

- inherits_from_previous_cn：承接单一指标批评。

- changes_argument_state_cn：给出混合排序的可行先例。

- sets_up_next_cn：为下一句本文与Choi和Mela的两点差异做铺垫。

- failure_if_removed_cn：HMUM会被误认为完全原创的无据方案。

- evidence_pointer：Section 2.1 P4

### 11. Section 2.1 P4 S4-S5

- order：11

- locator：Section 2.1 P4 S4-S5

- paraphrase_cn：本文与Choi和Mela有两个关键差异：他们权衡广告与销售收入，本文平衡消费者效用与平台收入；他们是非个性化混合，本文量化混合与个性化两者的价值。

- move_code：DIFFERENTIATION

- statement_status：author_inference

- why_here_cn：划清本文HMUM与既有混合排序的边界，确立独特贡献。

- inherits_from_previous_cn：承接Choi和Mela混合方案。

- changes_argument_state_cn：把混合排序从文献中区分出来。

- sets_up_next_cn：为下一节个性化文献的引入做铺垫。

- failure_if_removed_cn：HMUM与Choi和Mela混合方案无法区分。

- evidence_pointer：Section 2.1 P4最后

### 12. Section 2.2 P1 S1-S3

- order：12

- locator：Section 2.2 P1 S1-S3

- paraphrase_cn：个性化研究关注消费者剩余与卖家利润两方面影响，如定向优惠券、个性化邮件和推荐系统均显示收益。

- move_code：PRIOR_KNOWLEDGE

- statement_status：prior_literature

- why_here_cn：给出个性化正向证据，与下一段的负向证据形成张力。

- inherits_from_previous_cn：承接个性化概念。

- changes_argument_state_cn：建立个性化有利的文献基线。

- sets_up_next_cn：为下一段的个性化可能损害平台做铺垫。

- failure_if_removed_cn：个性化价值的一面缺失，文献张力无法形成。

- evidence_pointer：Section 2.2 P1

### 13. Section 2.2 P2 S1-S4

- order：13

- locator：Section 2.2 P2 S1-S4

- paraphrase_cn：个性化可能损害平台利润：Zhang和Wedel发现个体一级个性化并不总是更好；Goldfarb和Tucker发现侵入式广告降低购买意愿；Ghose等人的活跃个性化对收入有负效应。

- move_code：PRIOR_KNOWLEDGE

- statement_status：prior_literature

- why_here_cn：引入与正向证据相反的文献，说明个性化不能简单假定有益。

- inherits_from_previous_cn：承接个性化收益文献。

- changes_argument_state_cn：制造个性化问题的开放性。

- sets_up_next_cn：为解释偏好与边际不一致的机制做铺垫。

- failure_if_removed_cn：本文设计的动机张力消失。

- evidence_pointer：Section 2.2 P2

### 14. Section 2.2 P3 S1-S2

- order：14

- locator：Section 2.2 P3 S1-S2

- paraphrase_cn：这些研究表明更高个性化可能以平台为代价为消费者创造利益，原因可能是消费者偏好与收入边际并不总一致。

- move_code：MECHANISM

- statement_status：author_inference

- why_here_cn：把负向证据归纳为偏好-边际错配机制，为HMUM的效用×边际设计提供理论靶心。

- inherits_from_previous_cn：承接个性化负面证据。

- changes_argument_state_cn：提炼出核心机制问题。

- sets_up_next_cn：为本文精心设计的个性化目标做铺垫。

- failure_if_removed_cn：HMUM的双目标平衡缺乏理论动机。

- evidence_pointer：Section 2.2 P3

### 15. Section 2.2 P3 S3

- order：15

- locator：Section 2.2 P3 S3

- paraphrase_cn：本文目标之一是打造精细个性化，在应用分发情境中为消费者和平台创造增量价值。

- move_code：CONTRIBUTION_CLAIM

- statement_status：author_inference

- why_here_cn：在文献正反证据后给出本文立场：精心设计的个性化可以双赢。

- inherits_from_previous_cn：承接偏好与边际不一致机制。

- changes_argument_state_cn：设定本文的理论贡献目标。

- sets_up_next_cn：为下一节概念框架中的效用与边际联合做铺垫。

- failure_if_removed_cn：本文理论贡献的靶子缺失。

- evidence_pointer：Section 2.2 P3最后

### 16. Section 2.3 P1

- order：16

- locator：Section 2.3 P1

- paraphrase_cn：概念框架图展示实证分析的完整路径：两阶段结构模型、个体异质性、CPA边际和政策实验，共同评价个性化排序对收入的影响。

- move_code：FRAMEWORK

- statement_status：theory_claim

- why_here_cn：用一张图整合文献、模型与评价，为全文章节提供地图。

- inherits_from_previous_cn：承接排序和个人化文献。

- changes_argument_state_cn：把独立文献转化为本文分析架构。

- sets_up_next_cn：为后文的个体效用恢复和排序方案比较提供框架。

- failure_if_removed_cn：各章节之间的逻辑关系缺少统一图景。

- evidence_pointer：Section 2.3 Figure 1

### 17. Section 2.3 P2 S1

- order：17

- locator：Section 2.3 P2 S1

- paraphrase_cn：为刻画最优排序方案特征，开发一个简单分析模型，考虑探索成本、应用质量和用户对质量品味异质性。

- move_code：THEORY_PROPOSITION

- statement_status：theory_claim

- why_here_cn：用线上附录的分析模型为HMUM提供理论来源，表明它不是临时启发式。

- inherits_from_previous_cn：承接概念框架。

- changes_argument_state_cn：引入规范理论推导。

- sets_up_next_cn：为比较个性化与非个性化排序方案的模型求解做铺垫。

- failure_if_removed_cn：HMUM来源悬空，设计被视为临时的。

- evidence_pointer：Section 2.3 P2（线上附录）

### 18. Section 2.3 P2 S2

- order：18

- locator：Section 2.3 P2 S2

- paraphrase_cn：在个性化与非个性化最优排序下比较平台收入，关键结果是混合排序可能最有效。

- move_code：THEORY_PROPOSITION

- statement_status：theory_claim

- why_here_cn：给出分析模型的命题：混合排序最优，直接为HMUM设计定下方向。

- inherits_from_previous_cn：承接分析模型设定。

- changes_argument_state_cn：完成从模型到设计方向的推导。

- sets_up_next_cn：为现实平台中混合排序逻辑的展开做铺垫。

- failure_if_removed_cn：混合排序的核心假设缺少理论证据。

- evidence_pointer：Section 2.3 P2

### 19. Section 2.3 P2 S3-S4

- order：19

- locator：Section 2.3 P2 S3-S4

- paraphrase_cn：从分析模型外推到真实平台：列表顶部放该用户最高效用应用并按收入边际降序；其余位置按效用×边际乘积降序。

- move_code：THEORY_TO_DESIGN

- statement_status：design_decision

- why_here_cn：把理论命题转化为可执行的HMUM排序规则。

- inherits_from_previous_cn：承接混合排序最优命题。

- changes_argument_state_cn：把抽象命题具象为设计规则。

- sets_up_next_cn：为解释顶部为什么按边际排序做铺垫。

- failure_if_removed_cn：HMUM的理论到设计链条断裂。

- evidence_pointer：Section 2.3 P2 S3-S4

### 20. Section 2.3 P2 S5

- order：20

- locator：Section 2.3 P2 S5

- paraphrase_cn：用户很可能点击这些高效用印象，因此排序成为影响点击表现的主要因素，平台按边际排序这些槽位来最大化收入。

- move_code：MECHANISM

- statement_status：theory_claim

- why_here_cn：用机制解释顶部按边际排序为何合理。

- inherits_from_previous_cn：承接HMUM顶部设计。

- changes_argument_state_cn：补齐设计规则的行为基础。

- sets_up_next_cn：为下半部分的效用×边际排序做铺垫。

- failure_if_removed_cn：HMUM顶部规则缺少行为解释。

- evidence_pointer：Section 2.3 P2 S5

### 21. Section 2.3 P2 S6

- order：21

- locator：Section 2.3 P2 S6

- paraphrase_cn：边角其余位置按效用×边际排序，以对齐下载效用与收入边际。

- move_code：THEORY_TO_DESIGN

- statement_status：design_decision

- why_here_cn：给出下半部分设计规则并解释其目标。

- inherits_from_previous_cn：承接顶部机制。

- changes_argument_state_cn：完整定义HMUM。

- sets_up_next_cn：为总结混合方案收入表现做铺垫。

- failure_if_removed_cn：HMUM下半规则缺失。

- evidence_pointer：Section 2.3 P2 S6

### 22. Section 2.3 P2 S7

- order：22

- locator：Section 2.3 P2 S7

- paraphrase_cn：结果混合方案相比仅效用或仅边际的排序产生更高平台收入。

- move_code：THEORY_PROPOSITION

- statement_status：theory_claim

- why_here_cn：把分析模型结论再陈述一次，强化预期结果。

- inherits_from_previous_cn：承接HMUM定义。

- changes_argument_state_cn：为实证政策实验设定待检验的命题。

- sets_up_next_cn：为说明结构模型才是个体层面主引擎做铺垫。

- failure_if_removed_cn：政策实验的待检验预期不清晰。

- evidence_pointer：Section 2.3 P2 S7

### 23. Section 2.3 P3 S1-S2

- order：23

- locator：Section 2.3 P3 S1-S2

- paraphrase_cn：尽管分析模型提供指导，实证主引擎是个体层面的两阶段选择结构效用模型。

- move_code：METHOD_JUSTIFICATION

- statement_status：method_decision

- why_here_cn：把论文重心从规范模型转向结构估计，说明后文方法的地位。

- inherits_from_previous_cn：承接分析模型指导。

- changes_argument_state_cn：明确实证方法为主。

- sets_up_next_cn：为说明高分辨率模型的两个好处做铺垫。

- failure_if_removed_cn：读者不清楚分析模型和结构估计的主次关系。

- evidence_pointer：Section 2.3 P3 S1

### 24. Section 2.3 P3 S3-S4

- order：24

- locator：Section 2.3 P3 S3-S4

- paraphrase_cn：高分辨率模型有两个好处：精确刻画每位消费者偏好，而既有研究只能平均化；两阶段模型比忽略条件依赖的联立方程更符合真实决策。

- move_code：METHOD_JUSTIFICATION

- statement_status：method_decision

- why_here_cn：用两个好处说明为何选择个体级两阶段结构模型。

- inherits_from_previous_cn：承接结构模型为主引擎。

- changes_argument_state_cn：构建了模型选择的合理性。

- sets_up_next_cn：为第二点：如何平衡效用与边际做铺垫。

- failure_if_removed_cn：结构模型选择的理由不充分。

- evidence_pointer：Section 2.3 P3 S3-S4

### 25. Section 2.3 P3 S5-S6

- order：25

- locator：Section 2.3 P3 S5-S6

- paraphrase_cn：第二，具体说明如何把恢复的效用函数与CPA边际平衡，形成更有效的个性化排序。

- move_code：METHOD_JUSTIFICATION

- statement_status：method_decision

- why_here_cn：把结构模型与核心设计HMUM连接起来。

- inherits_from_previous_cn：承接模型两个好处。

- changes_argument_state_cn：完成模型到设计的显式连接。

- sets_up_next_cn：为HMUM实际逻辑的再描述做铺垫。

- failure_if_removed_cn：结构与设计之间的桥梁缺失。

- evidence_pointer：Section 2.3 P3 S5

### 26. Section 2.3 P3 S7

- order：26

- locator：Section 2.3 P3 S7

- paraphrase_cn：为了在个体层面最大化期望收入，通过混合排序显式平衡转化表现与CPA边际。

- move_code：DESIGN_DECISION

- statement_status：design_decision

- why_here_cn：把HMUM设计原则重述为方法选择。

- inherits_from_previous_cn：承接效用与边际平衡的说明。

- changes_argument_state_cn：把设计决策嵌进估计框架。

- sets_up_next_cn：为读者进入数据章节做铺垫。

- failure_if_removed_cn：政策实验中的HMUM缺少方法决策上的铺垫。

- evidence_pointer：Section 2.3 P3 S7

## 制品设计理由逐句图谱

### 1. Section 3 P1 S1-S2

- order：1

- locator：Section 3 P1 S1-S2

- paraphrase_cn：数据来自一家把美国大型移动运营商首页变现的营销代理，首页包含本地和网页搜索、内容展示和应用offer wall。

- move_code：CONTEXT

- statement_status：fact

- why_here_cn：说明数据来源和平台形态，为制品适用情境定位。

- inherits_from_previous_cn：承接概念框架需要的数据。

- changes_argument_state_cn：把研究情境具体化。

- sets_up_next_cn：为平台商业模式图做铺垫。

- failure_if_removed_cn：全部实证分析失去平台背景。

- evidence_pointer：Section 3开头

### 2. Section 3 P1 S3-S4

- order：2

- locator：Section 3 P1 S3-S4

- paraphrase_cn：第三方应用分发平台占总体安装约32%，本文聚焦该服务提供者作为应用分发平台的角色。

- move_code：JUSTIFICATION

- statement_status：fact

- why_here_cn：用市场份额说明平台代表性，支撑外部效度。

- inherits_from_previous_cn：承接平台形态。

- changes_argument_state_cn：建立样本代表性。

- sets_up_next_cn：为下一段业务模型描述做铺垫。

- failure_if_removed_cn：研究情境的代表性受到质疑。

- evidence_pointer：Section 3 P1

### 3. Section 3 P2 S1-S2

- order：3

- locator：Section 3 P2 S1-S2

- paraphrase_cn：用户访问offer wall并浏览应用印象，若感兴趣可点击并跳到应用商店，落地页提供描述、下载量、评论等细节。

- move_code：MECHANISM

- statement_status：fact

- why_here_cn：描述点击-跳转-安装的实际流程，为两阶段模型提供行为依据。

- inherits_from_previous_cn：承接平台业务模型。

- changes_argument_state_cn：建立两阶段决策的实物流程。

- sets_up_next_cn：为CPA收入和每应用预留边际做铺垫。

- failure_if_removed_cn：两阶段选择模型与真实流程脱节。

- evidence_pointer：Section 3 P2

### 4. Section 3 P2 S3-S4

- order：4

- locator：Section 3 P2 S3-S4

- paraphrase_cn：平台按CPA每下载付费模式收入，每个应用有预约定CPA边际；offer wall上只看到标题和星级，点击后才看到下载量、评分、描述和评论。

- move_code：MECHANISM

- statement_status：fact

- why_here_cn：说明两个阶段的可见信息不同，解释为何点击效用和安装效用使用不同协变量。

- inherits_from_previous_cn：承接业务模型。

- changes_argument_state_cn：把信息不对称结构化为模型设定依据。

- sets_up_next_cn：为数据变量和模型方程中的变量分工做铺垫。

- failure_if_removed_cn：点击方程与安装方程变量不同的理由不成立。

- evidence_pointer：Section 3 P2

### 5. Section 3 P3 S1-S2

- order：5

- locator：Section 3 P3 S1-S2

- paraphrase_cn：点击流数据来自2015年7月前三周服务器日志，捕捉每位用户的印象、点击和安装，按用户-印象粒度记录并可恢复屏幕排名和会话内全部印象。

- move_code：DATA

- statement_status：fact

- why_here_cn：说明数据粒度与排名可恢复性，这是个性化排序实验的输入条件。

- inherits_from_previous_cn：承接业务模型与信息结构。

- changes_argument_state_cn：建立数据集的核心优势。

- sets_up_next_cn：为数值和文本特征描述做铺垫。

- failure_if_removed_cn：个性化政策实验无法计算。

- evidence_pointer：Section 3 P3

### 6. Section 3 P4 S1

- order：6

- locator：Section 3 P4 S1

- paraphrase_cn：除点击流外还考虑数值与文本应用特征，包括排名、评论量效价、下载量和标题描述评论文本。

- move_code：DATA

- statement_status：fact

- why_here_cn：说明效用函数的协变量素材。

- inherits_from_previous_cn：承接日志数据。

- changes_argument_state_cn：扩展数据维度。

- sets_up_next_cn：为文本变量必要性的文献铺垫。

- failure_if_removed_cn：文本效应研究缺乏数据基础。

- evidence_pointer：Section 3 P3

### 7. Section 3 P4 S2-S3

- order：7

- locator：Section 3 P4 S2-S3

- paraphrase_cn：近期研究强调用可读性和情感等文本变量补充定量数据，用信息量和情感分别捕捉客观与主观内容。

- move_code：PRIOR_KNOWLEDGE

- statement_status：prior_literature

- why_here_cn：为文本变量的引入提供文献依据，避免看似随意。

- inherits_from_previous_cn：承接文本特征数据。

- changes_argument_state_cn：确立文本变量的理论基础。

- sets_up_next_cn：为信息量、长度、频率、模糊度三个构成的操作化做铺垫。

- failure_if_removed_cn：文本变量构造缺乏理论来源。

- evidence_pointer：Section 3 P4

### 8. Section 3 P5 S1-S5

- order：8

- locator：Section 3 P5 S1-S5

- paraphrase_cn：用多种文本分析工具操作化信息量和模糊度：词频计算特殊度、文本长度近似信息量、词典语义数测量模糊度、极性分类器测量情感。

- move_code：METHOD_DECISION

- statement_status：method_decision

- why_here_cn：解释每个文本变量的构造方式，让结果可复现。

- inherits_from_previous_cn：承接信息量与情感概念。

- changes_argument_state_cn：把概念转化为变量。

- sets_up_next_cn：为描述统计和相关性分析做铺垫。

- failure_if_removed_cn：文本变量的有效性无法判断。

- evidence_pointer：Section 3 P5

### 9. Section 3 P6 S1-S2

- order：9

- locator：Section 3 P6 S1-S2

- paraphrase_cn：基于317,040个观测给出描述统计：点击率1.5%，点击后安装率9%，排名范围1-59，用户平均浏览26个印象。

- move_code：DATA_DESCRIPTION

- statement_status：empirical_result

- why_here_cn：给出关键数据集基本特征，让读者判断数据量和行为频率。

- inherits_from_previous_cn：承接日志数据。

- changes_argument_state_cn：建立数据集规模与基础行为事实。

- sets_up_next_cn：为Rating、评论量、Popularity、Game等变量描述做铺垫。

- failure_if_removed_cn：数据集的规模和代表性无法评估。

- evidence_pointer：Section 3 P6 Table 2

### 10. Section 3 P6 S3-S5

- order：10

- locator：Section 3 P6 S3-S5

- paraphrase_cn：数值变量方面，平均星级刚过四星，评论量约60万且波动大，Popularity以平均下载量构造，40%应用为流行，游戏占70%，平均有8.52个同类竞争应用。

- move_code：DATA_DESCRIPTION

- statement_status：empirical_result

- why_here_cn：说明效用函数中数值协变量的分布，为后续稳健性和Game控制提供数据事实。

- inherits_from_previous_cn：承接描述统计。

- changes_argument_state_cn：细化数值变量分布。

- sets_up_next_cn：为文本变量描述做铺垫。

- failure_if_removed_cn：数值变量分布无法评估。

- evidence_pointer：Section 3 P6

### 11. Section 3 P6 S6-S7

- order：11

- locator：Section 3 P6 S6-S7

- paraphrase_cn：文本变量方面，标题比描述和评论更具体，平均约18字符；标题每词少于3个含义，描述评论超过5个解释；描述情感更积极。

- move_code：DATA_DESCRIPTION

- statement_status：empirical_result

- why_here_cn：说明文本变量的测量值分布，为标题影响点击的结论提供基础。

- inherits_from_previous_cn：承接数值变量描述。

- changes_argument_state_cn：建立文本变量实际分布。

- sets_up_next_cn：为相关矩阵分析做铺垫。

- failure_if_removed_cn：文本变量的有效性无法判断。

- evidence_pointer：Section 3 P6

### 12. Section 3 P7

- order：12

- locator：Section 3 P7

- paraphrase_cn：相关矩阵显示点击与安装相关0.297，点击安装与排名、评论量、评分、流行度正相关，文本变量间有一定相关性，竞争应用数与CTR负相关。

- move_code：DATA_DESCRIPTION

- statement_status：empirical_result

- why_here_cn：用相关矩阵提供初步证据并指出替代和竞争关系。

- inherits_from_previous_cn：承接描述统计。

- changes_argument_state_cn：给出变量间初步关联。

- sets_up_next_cn：为正式结构模型做铺垫。

- failure_if_removed_cn：进入模型前缺少数据关系概览。

- evidence_pointer：Section 3 P7 Table 3

## Study开头、过渡与收束图谱

### 1. 1

- study_or_phase：理论排序模型（线上附录，正文Section 2.3概述）

- opening_locator：Section 2.3 P2 S1

- opening_function_cn：以需要刻画最优排序方案为入口，引入分析模型。

- transition_in_function_cn：从概念框架转为规范理论推导，为HMUM提供理论导航。

- closing_locator：Section 2.3 P2 S7

- closing_function_cn：以混合方案较优收束，并把重点交给结构模型。

- argumentative_role_cn：提供HMUM的理论依据，但仅是假设方向，需要实证检验。

### 2. 2

- study_or_phase：数据收集与特征构造

- opening_locator：Section 3 P1 S1

- opening_function_cn：以数据来源公司开场。

- transition_in_function_cn：从概念框架需要的数据转入实际数据介绍。

- closing_locator：Section 3 P7

- closing_function_cn：以相关矩阵和转向模型设定的过渡句收束。

- argumentative_role_cn：确立数据的独特性和两阶段信息结构，使后续模型设定与政策实验可行。

### 3. 3

- study_or_phase：结构模型估计

- opening_locator：Section 4 P1 S1

- opening_function_cn：以开发两阶段二元Probit模型开场。

- transition_in_function_cn：从数据描述转到正式模型设定，说明决策顺序。

- closing_locator：Section 4.3末尾

- closing_function_cn：以MCMC收敛诊断收束，说明估计可靠。

- argumentative_role_cn：恢复个体点击与安装效用，为政策实验提供参数基础。

### 4. 4

- study_or_phase：模型拟合与稳健性检验

- opening_locator：Section 5开头

- opening_function_cn：以结果报告顺序开场：显著性、经济意义、异质性、稳健性。

- transition_in_function_cn：从估计方法进入结果，先把估计结果说清楚。

- closing_locator：Section 5.2末尾

- closing_function_cn：以LDA替代测度结论不变的稳健性收束。

- argumentative_role_cn：证明文本变量和异质性有价值，且估计结果不依赖子样本或测度方式。

### 5. 5

- study_or_phase：反事实政策实验

- opening_locator：Section 6 P1 S1

- opening_function_cn：以进行反事实分析探讨个性化排序如何提高平台收入开场。

- transition_in_function_cn：从稳健估计转入排序方案比较，说明结构模型优势使政策实验可行。

- closing_locator：Section 6最后一段

- closing_function_cn：以政策实验几点洞察收束：加边际有改进、但真正的收益来自个性化、HMUM在个性化下再提升。

- argumentative_role_cn：直接量化各排序方案的收入提升，是全文最核心的证据。

## 讨论与贡献逐句图谱

### 1. Section 7 P1 S1

- order：1

- locator：Section 7 P1 S1

- paraphrase_cn：开发了综合框架，利用点击流数据通过个性化排序提高移动应用分发变现效率。

- move_code：SUMMARY

- statement_status：contribution_claim

- why_here_cn：返回答题，总结全文核心任务。

- inherits_from_previous_cn：承接政策实验结论。

- changes_argument_state_cn：把文章工作浓缩为一项贡献。

- sets_up_next_cn：为平台重要性的说明做铺垫。

- failure_if_removed_cn：结论没有对全文任务的回应。

- evidence_pointer：Section 7 P1 S1

### 2. Section 7 P1 S2-S3

- order：2

- locator：Section 7 P1 S2-S3

- paraphrase_cn：此类平台占全部应用下载的32%，是重要情境；还充当开发者的广告和零售渠道。

- move_code：IMPORTANCE

- statement_status：fact

- why_here_cn：重申情境重要性，让贡献具有现实分量。

- inherits_from_previous_cn：承接综合框架。

- changes_argument_state_cn：强化研究的应用价值。

- sets_up_next_cn：为两阶段实证分析的总结做铺垫。

- failure_if_removed_cn：研究情境重要性被忽略。

- evidence_pointer：Section 7 P1 S2-S3

### 3. Section 7 P2 S1-S2

- order：3

- locator：Section 7 P2 S1-S2

- paraphrase_cn：实证分析分两阶段：先实现两阶段点击转化模型并纳入个体异质性；再恢复个体效用参数用于反事实政策实验。

- move_code：SUMMARY

- statement_status：empirical_result

- why_here_cn：用两句话梳理全文方法链，为细节结果提供框架。

- inherits_from_previous_cn：承接综合框架。

- changes_argument_state_cn：明确实证链条。

- sets_up_next_cn：为数值与文本结果的总结做铺垫。

- failure_if_removed_cn：结论缺少方法回顾。

- evidence_pointer：Section 7 P2

### 4. Section 7 P2 S3-S5

- order：4

- locator：Section 7 P2 S3-S5

- paraphrase_cn：数值与文本协变量在解释消费者选择上整体高度显著；屏幕排名是点击的关键决定因素，排名上移一位CTR提高4.26%；评论效价对安装比对点击更重要；同类竞争应用有显著替代效应。

- move_code：RESULT_SUMMARY

- statement_status：empirical_result

- why_here_cn：在结论中浓缩核心估计结果，支撑后面的文本效应和贡献。

- inherits_from_previous_cn：承接两阶段实证分析。

- changes_argument_state_cn：把结果以最简洁形式呈现。

- sets_up_next_cn：为流行度不显著的解释做铺垫。

- failure_if_removed_cn：结论中的结果支柱缺失。

- evidence_pointer：Section 7 P2

### 5. Section 7 P2 S6

- order：5

- locator：Section 7 P2 S6

- paraphrase_cn：应用流行度不解释下载行为，可能是因为最流行应用已被下载。

- move_code：RESULT_SUMMARY

- statement_status：author_inference

- why_here_cn：解释一个反直觉估计结果，避免读者质疑。

- inherits_from_previous_cn：承接结果总结。

- changes_argument_state_cn：把估计结果赋予解释。

- sets_up_next_cn：为文本信息结果总结做铺垫。

- failure_if_removed_cn：Popularity不显著的结果显得突兀。

- evidence_pointer：Section 7 P2 S6

### 6. Section 7 P3 S1-S2

- order：6

- locator：Section 7 P3 S1-S2

- paraphrase_cn：用户关注文本：点击阶段标题信息量正向显著，模糊度和情感负面；安装阶段只有描述情感正向影响决定。

- move_code：RESULT_SUMMARY

- statement_status：empirical_result

- why_here_cn：总结文本变量的阶段性差异，为平台文本内容管理的含义提供基础。

- inherits_from_previous_cn：承接结果总结。

- changes_argument_state_cn：突出文本发现。

- sets_up_next_cn：为评论文本不显著的说明做铺垫。

- failure_if_removed_cn：文本设计知识的贡献没有结果支持。

- evidence_pointer：Section 7 P3

### 7. Section 7 P3 S3-S4

- order：7

- locator：Section 7 P3 S3-S4

- paraphrase_cn：评论文本特征对安装不显著，可能原因是用户在小屏幕不读详细评论而使用数值摘要。

- move_code：RESULT_SUMMARY

- statement_status：author_inference

- why_here_cn：解释评论文本不显著，并呼应移动端界面的信息处理机制。

- inherits_from_previous_cn：承接文本效应总结。

- changes_argument_state_cn：把模型选择（排除评论变量）合理化。

- sets_up_next_cn：为政策实验的总结做铺垫。

- failure_if_removed_cn：主模型不包含评论变量的决策显得武断。

- evidence_pointer：Section 7 P3 S3-S4

### 8. Section 7 P4 S1-S2

- order：8

- locator：Section 7 P4 S1-S2

- paraphrase_cn：政策实验中用恢复的效用参数操纵印象位置，基于真实CPA边际计算期望收入；结果表明考虑效用与边际的个性化排序胜过所有其他方案。

- move_code：RESULT_SUMMARY

- statement_status：empirical_result

- why_here_cn：重申政策实验的核心结果，为贡献声明提供最强证据。

- inherits_from_previous_cn：承接结果总结。

- changes_argument_state_cn：把排序方案比较摆到结论中心。

- sets_up_next_cn：为个性化提升范围的具体数字做铺垫。

- failure_if_removed_cn：结论中缺少核心政策实验结果。

- evidence_pointer：Section 7 P4

### 9. Section 7 P4 S3

- order：9

- locator：Section 7 P4 S3

- paraphrase_cn：个性化排序相对非个性化提升从4.92%到16.73%，其中混合方案比其他个性化方案更有效。

- move_code：RESULT_SUMMARY

- statement_status：empirical_result

- why_here_cn：给出具体的收入提升区间和HMUM的核心数字。

- inherits_from_previous_cn：承接政策实验结论。

- changes_argument_state_cn：量化HMUM优势。

- sets_up_next_cn：为实施方式建议做铺垫。

- failure_if_removed_cn：个性化收益没有数值锚点。

- evidence_pointer：Section 7 P4 S3

### 10. Section 7 P4 S4

- order：10

- locator：Section 7 P4 S4

- paraphrase_cn：实施上个性化排序可通过隔夜批处理部署，预先重估效用函数并确定每个用户的排序，最小化实时计算负担。

- move_code：IMPLICATION

- statement_status：author_inference

- why_here_cn：把学术结果转成可落地的工程方案，让贡献更现实。

- inherits_from_previous_cn：承接个性化收益。

- changes_argument_state_cn：增加实践可行性。

- sets_up_next_cn：为文献贡献正式声明做铺垫。

- failure_if_removed_cn：平台不知道如何实际部署个性化。

- evidence_pointer：Section 7 P4 S4

### 11. Section 7 P5 S1

- order：11

- locator：Section 7 P5 S1

- paraphrase_cn：这些结果为文献作出多方面贡献：首先本文是最早研究应用安装变现的排序研究之一。

- move_code：CONTRIBUTION

- statement_status：contribution_claim

- why_here_cn：拉开贡献清单，锚定在情境维度。

- inherits_from_previous_cn：承接全文结果。

- changes_argument_state_cn：进入正式贡献部分。

- sets_up_next_cn：为文本协变量贡献做铺垫。

- failure_if_removed_cn：论文没有显式文献贡献。

- evidence_pointer：Section 7 P5 S1

### 12. Section 7 P5 S2-S3

- order：12

- locator：Section 7 P5 S2-S3

- paraphrase_cn：部署了数值和文本两类协变量；利用用户-印象级细粒度点击流实现个性化，这是先前研究做不到的。

- move_code：CONTRIBUTION

- statement_status：contribution_claim

- why_here_cn：强调数据粒度带来的个体异质性建模能力。

- inherits_from_previous_cn：承接首个贡献。

- changes_argument_state_cn：把数据资源升级为文献贡献。

- sets_up_next_cn：为CPA边际贡献做铺垫。

- failure_if_removed_cn：数据优势没有转化为贡献声明。

- evidence_pointer：Section 7 P5

### 13. Section 7 P5 S4

- order：13

- locator：Section 7 P5 S4

- paraphrase_cn：同时可以获得每个应用的CPA边际，这在先前工作中未见过，从而能分析精确的收入影响。

- move_code：CONTRIBUTION

- statement_status：contribution_claim

- why_here_cn：强调真实边际数据是本文数据独特贡献的顶点。

- inherits_from_previous_cn：承接用户-印象级数据贡献。

- changes_argument_state_cn：把数据证据推到贡献核心。

- sets_up_next_cn：为HMUM贡献做铺垫。

- failure_if_removed_cn：效用与边际权衡的核心主张失去证据。

- evidence_pointer：Section 7 P5

### 14. Section 7 P5 S5

- order：14

- locator：Section 7 P5 S5

- paraphrase_cn：提出的最优混合方案平衡消费者效用驱动因素与收入边际。

- move_code：CONTRIBUTION

- statement_status：contribution_claim

- why_here_cn：把HMUM作为独立贡献列出。

- inherits_from_previous_cn：承接CPA边际贡献。

- changes_argument_state_cn：完成设计贡献声明。

- sets_up_next_cn：为与市场级需求文献的区别做铺垫。

- failure_if_removed_cn：HMUM没有在贡献清单中占据位置。

- evidence_pointer：Section 7 P5 S5

### 15. Section 7 P5 S6

- order：15

- locator：Section 7 P5 S6

- paraphrase_cn：在理解移动应用消费者效用方面，本文聚焦应用分发平台的微观经济，而先前研究关注市场级需求驱动因素。

- move_code：CONTRIBUTION

- statement_status：contribution_claim

- why_here_cn：用视角差异区分本文与市场级需求文献。

- inherits_from_previous_cn：承接微观数据分析。

- changes_argument_state_cn：完成文献贡献清单。

- sets_up_next_cn：为管理含义段做铺垫。

- failure_if_removed_cn：本文与市场级文献的关系不清。

- evidence_pointer：Section 7 P5 S6

### 16. Section 7 P6 S1-S2

- order：16

- locator：Section 7 P6 S1-S2

- paraphrase_cn：提供可执行的管理含义：多数内容分发平台使用简单变现启发式，本文给出如何更好变现的可执行指导。

- move_code：IMPLICATION

- statement_status：contribution_claim

- why_here_cn：把研究结果转成平台行动建议。

- inherits_from_previous_cn：承接文献贡献。

- changes_argument_state_cn：从学术贡献转向实践建议。

- sets_up_next_cn：为个性化同时提高收入和消费者剩余的声明做铺垫。

- failure_if_removed_cn：实践价值不被明确。

- evidence_pointer：Section 7 P6 S1-S2

### 17. Section 7 P6 S3-S4

- order：17

- locator：Section 7 P6 S3-S4

- paraphrase_cn：点击流加CPA边际可部署比现用算法更有利可图的排序；平台可以个性化排序产生更高收入和更高消费者剩余。

- move_code：IMPLICATION

- statement_status：contribution_claim

- why_here_cn：明确提出双赢主张，但注意该主张主要由设计逻辑推断。

- inherits_from_previous_cn：承接可执行指导。

- changes_argument_state_cn：把结果扩展至消费者福利。

- sets_up_next_cn：为跨情境可推广性做铺垫。

- failure_if_removed_cn：管理含义缺少激励性结论。

- evidence_pointer：Section 7 P6

### 18. Section 7 P6 S5-S6

- order：18

- locator：Section 7 P6 S5-S6

- paraphrase_cn：个性化排序随移动运营商实时处理能力提高而日益可行；混合个性化排序可推广到电影、音乐分发和产品搜索等效用与边际都重要的情境。

- move_code：IMPLICATION

- statement_status：contribution_claim

- why_here_cn：把结论从单一情境推广到更广泛数字平台。

- inherits_from_previous_cn：承接双赢管理含义。

- changes_argument_state_cn：建立外部效度和设计知识。

- sets_up_next_cn：为文本内容管理建议做铺垫。

- failure_if_removed_cn：贡献被限制在单一平台。

- evidence_pointer：Section 7 P6

### 19. Section 7 P7 S1-S2

- order：19

- locator：Section 7 P7 S1-S2

- paraphrase_cn：分析指出文本内容对平台和开发者重要，可用于没有足够评分的新应用的推广。

- move_code：IMPLICATION

- statement_status：contribution_claim

- why_here_cn：单独把文本发现转成第三方和开发者的操作建议。

- inherits_from_previous_cn：承接管理含义。

- changes_argument_state_cn：把文本研究转化为设计知识。

- sets_up_next_cn：为文本异质性定向建议做铺垫。

- failure_if_removed_cn：文本结果的实践用途未被利用。

- evidence_pointer：Section 7 P7

### 20. Section 7 P7 S3

- order：20

- locator：Section 7 P7 S3

- paraphrase_cn：营销人员可利用文本信息偏好异质性进行定向，例如给常读描述的用户提供更多细节，用不同情感措辞定向特定消费者。

- move_code：IMPLICATION

- statement_status：contribution_claim

- why_here_cn：把异质性发现转成用户定向策略。

- inherits_from_previous_cn：承接文本内容推广建议。

- changes_argument_state_cn：完成设计知识向实践的转化。

- sets_up_next_cn：为限制和未来研究做铺垫。

- failure_if_removed_cn：文本异质性的实践价值没有体现。

- evidence_pointer：Section 7 P7 S3

### 21. Section 7 P8 S1

- order：21

- locator：Section 7 P8 S1

- paraphrase_cn：研究受数据限制：因隐私保护无法收集消费者人口统计。

- move_code：LIMITATION

- statement_status：author_inference

- why_here_cn：坦诚数据局限，为未来研究留空间。

- inherits_from_previous_cn：承接管理含义。

- changes_argument_state_cn：进入边界部分。

- sets_up_next_cn：为人口统计可进一步改进排序的说法做铺垫。

- failure_if_removed_cn：结论缺少诚实边界。

- evidence_pointer：Section 7 P8

### 22. Section 7 P8 S2-S3

- order：22

- locator：Section 7 P8 S2-S3

- paraphrase_cn：用层级模型处理未观测异质性；平台若有人口统计可进一步强化个性化排序。

- move_code：LIMITATION

- statement_status：author_inference

- why_here_cn：解释模型如何部分弥补人口统计缺失，并指出改进空间。

- inherits_from_previous_cn：承接隐私限制。

- changes_argument_state_cn：把限制转为未来机会。

- sets_up_next_cn：为未做随机现场实验的限制做铺垫。

- failure_if_removed_cn：人口统计限制显得无法处理。

- evidence_pointer：Section 7 P8 S2-S3

### 23. Section 7 P8 S4-S5

- order：23

- locator：Section 7 P8 S4-S5

- paraphrase_cn：没有在随机田野实验中评估排序策略，而是依赖政策实验；未来可做实验得到更稳健结论。

- move_code：LIMITATION

- statement_status：author_inference

- why_here_cn：明确政策实验的方法边界，防止过度声称因果。

- inherits_from_previous_cn：承接人口统计限制。

- changes_argument_state_cn：承认反事实方法的局限。

- sets_up_next_cn：为动态效应限制做铺垫。

- failure_if_removed_cn：HMUM的因果主张可能被夸大。

- evidence_pointer：Section 7 P8

### 24. Section 7 P8 S6-S7

- order：24

- locator：Section 7 P8 S6-S7

- paraphrase_cn：未从动态视角估计时间效应；模型精确估计了阶段依赖和个体异质性，但加入动态会带来识别和计算困难，留作未来研究。

- move_code：LIMITATION

- statement_status：author_inference

- why_here_cn：承认没有动态模型，并解释原因，提出未来方向。

- inherits_from_previous_cn：承接田野实验限制。

- changes_argument_state_cn：完成边界设定。

- sets_up_next_cn：为总体收尾句做铺垫。

- failure_if_removed_cn：动态效应边界未声明，结论显得过于广泛。

- evidence_pointer：Section 7 P8

### 25. Section 7 P8 S8

- order：25

- locator：Section 7 P8 S8

- paraphrase_cn：总体而言，分析为平台提供可执行行动，提升应用分发变现并为移动生态系统多利益相关者带来潜在收益。

- move_code：CLOSING

- statement_status：contribution_claim

- why_here_cn：以总体贡献声明收束全文。

- inherits_from_previous_cn：承接所有限制。

- changes_argument_state_cn：完成论文闭环。

- sets_up_next_cn：无。

- failure_if_removed_cn：结论没有最终价值总结。

- evidence_pointer：Section 7 P8最后

## Study累积逻辑

### 1. 1

- study_or_phase：分析性排序模型

- evidence_job_cn：从规范理论方向证明混合排序可能最优。

- what_it_establishes_cn：在搜索成本、质量差异和口味异质性下，混合排序优于单指标排序。

- what_it_cannot_establish_cn：无法证明真实数据中混合排序表现如何，因为假设较强。

- why_next_phase_is_needed_cn：需要真实平台数据和个体效用估计来检验该命题。

- transition_wording_function_cn：正文用'虽然分析模型提供有用指导，但实证主引擎是结构效用模型'把理论让位给实证。

### 2. 2

- study_or_phase：数据收集与特征构造

- evidence_job_cn：确立数据集的独特性和两阶段信息结构。

- what_it_establishes_cn：用户-印象级点击流、真实CPA边际、数值与文本特征均可得。

- what_it_cannot_establish_cn：不能解释变量间的因果或排序收入效应。

- why_next_phase_is_needed_cn：需要结构模型把数据转成个体效用参数。

- transition_wording_function_cn：以'我们转而讨论实证模型与估计策略'把数据引向模型。

### 3. 3

- study_or_phase：结构模型估计

- evidence_job_cn：恢复个体层面的点击与安装效用参数。

- what_it_establishes_cn：排名、评分、标题信息量和模糊度、描述情感等显著影响点击或安装，且存在个体异质性。

- what_it_cannot_establish_cn：参数本身不等于排序政策的效果，也不代表预测最优。

- why_next_phase_is_needed_cn：需要用模型拟合比较确认包含文本和异质性的价值。

- transition_wording_function_cn：正文用结果章节'先讨论显著性再讨论异质性最后稳健性'组织过渡。

### 4. 4

- study_or_phase：模型拟合与验证

- evidence_job_cn：证明文本变量和个体异质性对预测有增量价值。

- what_it_establishes_cn：全模型样本内外RMSE/MSE/MAD均最优，文本改善约13.33%，异质性改善约35.59%。

- what_it_cannot_establish_cn：预测改善不等于平台收入提升。

- why_next_phase_is_needed_cn：需要稳健性检验排除子样本和测度方式的影响。

- transition_wording_function_cn：结果节末尾列出'一些稳健性检验'作为独立小节。

### 5. 5

- study_or_phase：稳健性检验

- evidence_job_cn：排除特殊子样本和替代文本测度对结果的驱动。

- what_it_establishes_cn：游戏与非游戏子样本定性一致；LDA主题分散度替代描述信息量后结论不变。

- what_it_cannot_establish_cn：仍没有排序层面的收入结果。

- why_next_phase_is_needed_cn：需要把个体效用参数用于反事实排序收入比较。

- transition_wording_function_cn：Section 6以'我们通过政策实验进行反事实分析'从稳健性转入收入比较。

### 6. 6

- study_or_phase：反事实政策实验

- evidence_job_cn：直接量化各排序方案的预期收入提升。

- what_it_establishes_cn：个性化HMUM收入提升16.73%，高于其他方案。

- what_it_cannot_establish_cn：不是现场随机实验，不包含用户动态反应、开发者策略调整或实施误差。

- why_next_phase_is_needed_cn：把结果转成文献贡献、管理含义和未来研究。

- transition_wording_function_cn：Section 7以'我们开发综合框架'把政策实验升华为结论与贡献。

## 主张—证据台账

### 1. 移动应用市场规模巨大，第三方平台有数十亿收入和快速增长。

- claim_cn：移动应用市场规模巨大，第三方平台有数十亿收入和快速增长。

- claim_level：technical

- supporting_evidence_cn：市场报告引用App Annie 2021和2017数据。

- support_strength：direct

- where_claim_is_made：Introduction P1 S1-S3

- where_evidence_is_provided：Introduction P1 及脚注1

### 2. 第三方平台排序策略粗糙，仅用CTR、转化率和CPA边际。

- claim_cn：第三方平台排序策略粗糙，仅用CTR、转化率和CPA边际。

- claim_level：technical

- supporting_evidence_cn：行业报告Dogtiev 2019引用。

- support_strength：partial

- where_claim_is_made：Introduction P1 S6

- where_evidence_is_provided：Introduction P1 S6及引用

### 3. 平均效用排序能提高平台收入。

- claim_cn：平均效用排序能提高平台收入。

- claim_level：theory

- supporting_evidence_cn：Ghose et al. 2014、De los Santos和Koulayev 2017、Ursu 2018的文献结论。

- support_strength：direct

- where_claim_is_made：Introduction P1 S7、Section 2.1

- where_evidence_is_provided：Section 2.1文献综述

### 4. 个性化可能损害平台利润。

- claim_cn：个性化可能损害平台利润。

- claim_level：theory

- supporting_evidence_cn：Zhang和Wedel 2009、Goldfarb和Tucker 2011、Ghose et al. 2014的负面证据。

- support_strength：direct

- where_claim_is_made：Section 2.2 P2-P3

- where_evidence_is_provided：Section 2.2文献

### 5. 屏幕排名显著影响点击，排名上移一位CTR提高4.26%。

- claim_cn：屏幕排名显著影响点击，排名上移一位CTR提高4.26%。

- claim_level：technical

- supporting_evidence_cn：结构模型估计，Table 4 Rank系数和边际效应计算。

- support_strength：direct

- where_claim_is_made：Introduction P7、Section 5.1

- where_evidence_is_provided：Table 4及边际效应段落

### 6. 标题信息量和模糊度显著影响点击。

- claim_cn：标题信息量和模糊度显著影响点击。

- claim_level：mechanism

- supporting_evidence_cn：Table 4中TitleFreq、ln(TitleLen)、TitleAmb系数显著。

- support_strength：direct

- where_claim_is_made：Section 5.1

- where_evidence_is_provided：Table 4

### 7. 消费者对文本变量的反应比数值变量更异质。

- claim_cn：消费者对文本变量的反应比数值变量更异质。

- claim_level：mechanism

- supporting_evidence_cn：Table 5异质性方差中文本变量方差较大。

- support_strength：direct

- where_claim_is_made：Introduction P7、Section 5.1

- where_evidence_is_provided：Table 5

### 8. 文本变量和完全异质性显著改善模型拟合。

- claim_cn：文本变量和完全异质性显著改善模型拟合。

- claim_level：technical

- supporting_evidence_cn：Table 6样本内外RMSE/MSE/MAD比较。

- support_strength：direct

- where_claim_is_made：Section 5.1模型拟合段落

- where_evidence_is_provided：Table 6

### 9. 结果不由游戏应用或超级流行应用驱动。

- claim_cn：结果不由游戏应用或超级流行应用驱动。

- claim_level：boundary

- supporting_evidence_cn：Table 7游戏与非游戏子样本估计定性一致。

- support_strength：direct

- where_claim_is_made：Section 5.2

- where_evidence_is_provided：Table 7

### 10. 结果不受文本测度方式影响。

- claim_cn：结果不受文本测度方式影响。

- claim_level：technical

- supporting_evidence_cn：Table 8用LDA主题分散度替代后结论不变。

- support_strength：direct

- where_claim_is_made：Section 5.2

- where_evidence_is_provided：Table 8

### 11. 个性化排序比非个性化排序显著提高平台收入。

- claim_cn：个性化排序比非个性化排序显著提高平台收入。

- claim_level：artifact

- supporting_evidence_cn：Table 9中所有个性化方案相对基准均高于非个性化。

- support_strength：direct

- where_claim_is_made：Section 6

- where_evidence_is_provided：Table 9

### 12. 个性化HMUM是最优排序方案。

- claim_cn：个性化HMUM是最优排序方案。

- claim_level：artifact

- supporting_evidence_cn：Table 9中个性化HMUM提升16.73%，高于其他方案。

- support_strength：direct

- where_claim_is_made：Abstract S8、Introduction P8、Section 6

- where_evidence_is_provided：Table 9；脚注18仅作阈值敏感性说明

### 13. 混合方法在个性化下更有效，非个性化下并不更优。

- claim_cn：混合方法在个性化下更有效，非个性化下并不更优。

- claim_level：artifact

- supporting_evidence_cn：Table 9中非个性化HMUM提升2.38%略低于效用×边际的2.46%，个性化HMUM 16.73%高于效用×边际15.56%。

- support_strength：direct

- where_claim_is_made：Section 6最后一句

- where_evidence_is_provided：Table 9

### 14. 个性化同时提高平台收入和消费者效用。

- claim_cn：个性化同时提高平台收入和消费者效用。

- claim_level：theory

- supporting_evidence_cn：政策实验只计算平台收入；消费者效用提升由个性化设计和效用排序逻辑推断，无直接测量。

- support_strength：partial

- where_claim_is_made：Introduction P1 S8、Section 7 P6

- where_evidence_is_provided：无直接证据，依据设计逻辑

### 15. 分夜批处理能落地个性化排序。

- claim_cn：分夜批处理能落地个性化排序。

- claim_level：design_knowledge

- supporting_evidence_cn：仅作为实施建议，无现场部署数据。

- support_strength：asserted

- where_claim_is_made：Section 7 P4 S4

- where_evidence_is_provided：无

### 16. HMUM可推广至电影、音乐和产品搜索等其他效用与边际都重要的数字分发情境。

- claim_cn：HMUM可推广至电影、音乐和产品搜索等其他效用与边际都重要的数字分发情境。

- claim_level：design_knowledge

- supporting_evidence_cn：基于机制相似性推断，无跨情境实证。

- support_strength：asserted

- where_claim_is_made：Section 7 P6

- where_evidence_is_provided：无

## ISR定位逻辑

- constitutive_is_problem_cn：本文的问题不是单纯的排序算法问题，而是数字平台如何利用常规点击流数据中体现的用户行为显示偏好，与平台商业变现机制（CPA）相互构成的问题。排序同时是信息技术制品和平台收入决策变量，平台行为（展示顺序）和消费者行为（点击安装）互为条件。

- technology_behavior_or_market_entanglement_cn：技术设计与用户行为紧密纠缠：两阶段结构模型把平台展示的屏幕排名、标题、描述等技术与用户点击安装行为连接起来；HMUM是技术排序设计，但其有效性依赖用户对顶部高效用应用必定点击的行为机制和CPA市场边际；文本特征作为技术信号影响行为并反过来成为平台推广新应用的干预工具。

- role_of_benchmark_or_objective_evidence_cn：反事实收入公式和Table 9的百分比提升是事实证据，被用来支持'个性化优于平均化''加入边际有收益但真正收益来自个性化''混合在个性化时最有效'三个递进主张。客观证据不是用来证明算法工程性能，而是用来证明平台在何种设计选择下能同时改善变现与用户体验这一IS层面的判断。

- theory_in_design_cn：理论进入了设计前端：随机效用理论决定点击安装两阶段效用函数；搜索成本和口味异质性分析模型直接导出HMUM顶部按边际排序的规则；显示偏好理论决定用点击流恢复个体效用；个性化文献中的偏好-边际错配机制决定设计目标必须平衡效用与边际。理论不只是结果解释，而是设计的生成来源。

- technical_vs_is_contribution_balance_cn：本文技术贡献（个体级结构估计、文本特征操作化）篇幅较大，但最终被引向IS贡献：平台排序设计知识、变现能力提升、文本内容管理建议和跨情境推广。作者给政策实验和结论分配了足够篇幅，把技术从'模型表现'升华为'平台设计和公共管理含义'。

- beyond_transient_performance_cn：本文没有停留在收入百分比上：追加了机制解释（顶部高效用用户点击行为）、设计知识（文本对冷启动和新应用推广的作用）、实施方案（分夜批处理）和跨情境推广（电影、音乐、产品搜索），并用数据粒度和真实CPA边际等资源性差异支撑长期价值。

## 段落级仿写模板

### abstract_steps

1. 第一句用普遍现象开场（数字平台个性化）。

2. 第二句收窄到无人研究的具体情境。

3. 第三句给出研究目标（开发框架）。

4. 第四句设定设计目标（同时效用与收入边际）。

5. 第五句预告模型核心。

6. 第六句宣布数据独特性。

7. 第七句预告评价方式（政策实验）。

8. 第八句给出关键结果（最优排序方案）。

9. 第九句把结果上升为平台可复用贡献。

### introduction_paragraph_steps

1. 第一段：市场规模→平台模式→收入机制→现有实践粗糙→文献平均效用排序→本文个性化目标。

2. 第二段：定义核心概念→文献情境→收益机制→异质性转收入→概念辨析→锁定本文范畴。

3. 文献定位段：表格列示相关文献→指出共同模式→用表格空缺标记本文位置。

4. 分类定位段：用标准化框架给本文方法占位→再陈述显示偏好可恢复偏好的前提。

5. 问题段：承认已有进展→用编号问题逐一列出缺口。

6. 数据段：宣布独特数据→描述平台形态→强调数据粒度→预告模型与变量。

7. 结果预告段：总体洞察→具体边际效应→文本效应→异质性结论。

8. 实验及设计段：政策实验→平均与个性化对比→提出核心制品→解释机制→文献对照→描述制品规则→总结价值。

9. 结构段：章节导航。

### theory_to_design_steps

1. 先综述排序文献并指出共同不足（平均效用、无边际）。

2. 再综述个性化文献并制造正反张力（收益 vs 平台损害）。

3. 用概念框架图整合效用、异质性、边际与政策实验。

4. 用简单分析模型导出最优排序结构。

5. 把模型命题外推为现实排序规则。

6. 用机制解释每段设计规则的合理性。

7. 最后说明结构模型才是实证主引擎及其两个好处。

### method_and_study_sequence_steps

1. 数据段先说明业务模型和信息结构，使两阶段模型设定有依据。

2. 模型段按决策顺序设定点击与安装方程，说明异质性先验。

3. 估计段说明MCMC流程和收敛诊断。

4. 结果段按显著性、经济意义、异质性、模型拟合、稳健性的顺序组织。

5. 政策实验段先给出收入公式，再定义基准和非个性化方案，再引入个性化方案，最后解释差异。

### results_reporting_steps

1. 先给统计显著性方向和变量类别。

2. 再把Probit系数转成边际效应。

3. 再讨论异质性方差说明个性化必要性。

4. 再用模型拟合比较说明文本和异质性价值。

5. 最后用子样本和替代测度做稳健性。

6. 政策实验用表格同时展示非个性化与个性化，并按基准百分比报告。

### discussion_and_contribution_steps

1. 先概述全文方法链。

2. 再总结数值与文本结果的要点。

3. 再重申政策实验的核心数字。

4. 再给出实施建议。

5. 再逐条声明文献贡献。

6. 再转管理含义和跨情境推广。

7. 最后承认数据、实验方法和动态模型的局限并指出未来方向。

## 可执行写作算法

### 1. 1

- step：1

- rhetorical_job_cn：建立现实问题和市场重要性。

- research_evidence_required_cn：市场规模、平台收入模式、现有排序实践的描述和报告。

- sentence_pattern_function_cn：从市场规模数据开始，逐步收窄到具体平台商业模式，指出实践缺口。

- transition_condition_cn：当读者明白'排序决定收入且平台排序粗糙'后，进入文献定位。

### 2. 2

- step：2

- rhetorical_job_cn：用文献表定位研究缺口。

- research_evidence_required_cn：可比相关文献的上下文、结果、是否做排序设计、排序基础。

- sentence_pattern_function_cn：先把文献按共同特征归类，再指出多数用平均效用、无边际、无个性化，把本文置于表格唯一格。

- transition_condition_cn：当读者看到本文在表格中的独特位置后，进入概念框架。

### 3. 3

- step：3

- rhetorical_job_cn：用分析模型导出设计方向。

- research_evidence_required_cn：包含搜索成本、质量、异质性的简约模型，可比较个性化与非个性化收入的命题。

- sentence_pattern_function_cn：陈述模型要素，给出'混合排序可能最有效'命题，再外推为顶部按边际、其余按效用×边际的具体规则。

- transition_condition_cn：当读者接受混合排序的理论来源后，把重心交给结构估计。

### 4. 4

- step：4

- rhetorical_job_cn：建立数据独特性与两阶段决策结构。

- research_evidence_required_cn：用户-印象级点击流、屏幕排名可恢复性、真实CPA边际、数值和文本特征变量。

- sentence_pattern_function_cn：描述业务模型和信息流程，说明点击阶段只看到标题和星级，安装阶段才看到描述和评论，为两阶段模型提供事实基础。

- transition_condition_cn：当读者明白各阶段信息差异后，进入正式模型。

### 5. 5

- step：5

- rhetorical_job_cn：用结构模型恢复个体效用。

- research_evidence_required_cn：两阶段二元Probit设定、层级贝叶斯个体异质性、MCMC估计和收敛诊断。

- sentence_pattern_function_cn：先按决策顺序设定点击与安装方程，再说明互依性用相关误差建模，最后报告估计流程。

- transition_condition_cn：当估计参数收敛且可信后，进入结果与稳健性。

### 6. 6

- step：6

- rhetorical_job_cn：用结果、异质性、模型拟合和稳健性支撑估计可信度。

- research_evidence_required_cn：系数表、边际效应、异质性方差、样本内外拟合比较、子样本和替代测度结果。

- sentence_pattern_function_cn：先显著性后经济意义，再异质性，再拟合比较，最后稳健性。

- transition_condition_cn：当读者相信个体参数可靠后，进入政策实验。

### 7. 7

- step：7

- rhetorical_job_cn：用政策实验比较排序方案。

- research_evidence_required_cn：每个用户的点击与安装概率、每个应用的CPA边际、待比较的非个性化与个性化排序方案。

- sentence_pattern_function_cn：先给收入公式，再设平均效用为基准，逐步加入边际、混合和个性化，用表格按百分比报告。

- transition_condition_cn：当收入和最优方案比较清晰后，进入结论。

### 8. 8

- step：8

- rhetorical_job_cn：把结果升华为贡献、管理含义和边界。

- research_evidence_required_cn：上文全部估计和政策实验证据；实施建议和未来方向不需要新证据但需明确标注。

- sentence_pattern_function_cn：先概述方法链和关键数字，再宣布贡献，再给管理建议，最后列限制和未来研究。

- transition_condition_cn：当贡献、含义、边界都写清后，文章结束。

## 应模仿的高价值动作

1. 用一张文献表把本文在排序设计矩阵中的独特位置直接显示出来。

2. 用三个编号研究问题组织全文并让每节回应其中一个。

3. 先分析模型后实证检验，给排序设计一个理论来源。

4. 政策实验按'基准→加边际→加混合→个性化'递进比较，分离每个设计变化的增量。

5. 用样本内外拟合比较证明文本变量和异质性不是可有可无。

6. 在政策实验解释段把Table 9差异重新用搜索成本、高效用点击行为等机制重述，使数字成为机制证据。

7. 把实施建议具体到分夜批处理，增强结果可落地性。

8. 在结论中区分情境贡献、数据贡献、方法贡献和设计贡献，逐层声明。

## 不要只复制的表面动作

1. 没有真实用户-印象级CPA边际数据时，不能照搬'政策实验收入提升百分之十几'的叙述。

2. 不能只提出HMUM概念而不做结构估计和反事实比较。

3. 不能把'个性化更好'当作普遍结论，必须回应个性化可能损害平台的文献。

4. 不能只报告系数的统计显著性而不给经济边际效应，因为排序主张需要商业意义。

5. 不能在结论中直接声称消费者剩余同时提高，除非直接测量或明确标注为推断。

## 证据薄弱或跳跃的动作

1. '消费者效用同时提高'是从设计逻辑推断而不是消费者剩余的直接测量，存在无证据升级。

2. HMUM顶部5%阈值虽经敏感性说明，但没有从理论中推导出来。

3. 非个性化HMUM（2.38%）并不高于非个性化效用×边际（2.46%），作者只在结论和解释中谨慎处理，若表述不精确会被误读为混合总优于单指标。

4. 分夜批处理实施建议没有现场证据，不能与已验证结果并列。

5. 跨情境推广到电影、音乐、产品搜索是基于机制相似性的推断，无直接实证。

## 一句话套路

用真实平台的用户-印象级点击流和一个含真实CPA边际的结构效用模型恢复个体偏好，再通过反事实政策实验证明'个性化混合排序（HMUM）'在平衡消费者效用与平台收入方面优于平均效用和其他单指标排序，从而把一条技术排序规则提升为可复用的平台变现设计知识。

## 分析边界

全文由OCR提取，公式、表格和部分特殊符号排印可能不准确；线上附录中的分析模型细节和命题不可见；正文无标准页码，定位基于章节与段落；Table 9中非个性化基准数值506.30为原文表格呈现，OCR对百分比差异的表述已尽量与原表核对；对顶部5%阈值的敏感性只依赖脚注18转述，无法核对Online Table A2。
