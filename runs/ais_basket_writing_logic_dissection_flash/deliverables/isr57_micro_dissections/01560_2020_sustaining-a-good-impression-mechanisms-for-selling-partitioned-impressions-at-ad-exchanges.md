# Sustaining a Good Impression: Mechanisms for Selling Partitioned Impressions at Ad Exchanges：ISR 句段级微观图谱

- 作者：Sameer Mehta; Milind Dawande; Ganesh Janakiraman; Vijay Mookerjee
- 年份：2020
- DOI：10.1287/isre.2019.0878
- 源文件：01560_2020_sustaining-a-good-impression-mechanisms-for-selling-partitioned-impressions-at-ad-exchanges.md
- 置信度：0.86

## 核实后的宏观骨架

论文从移动广告交易所按单一广告主全程展示印象的现状出发，识别配置低效；提出将印象切分为时间槽顺序展示多个广告的机制设计框架。在机制设计框架下将问题形式化为P^IR（每次拍卖IR）和P^MB（长期BASE效用保障）两个设置，分别推导出OPT-IR和OPT-MB两种收益最优机制。OPT-IR用虚拟价值最大化分配加Myerson支付，但因支付难以实时计算引入随机化支付RAND并兼容CPC/CPM；OPT-MB采用VCG一阶最优分配加固定BASE效用转移。文章通过SEQ（逐槽独立拍卖）和BASE（现状机制）两个基准，用解析示例、充分性定理和数值仿真（100万样本）证明：SEQ可能大幅次优；OPT-IR总给交易所更高收益但广告主可能受益或受损（win-win/win-lose）；OPT-MB在长期保证广告主BASE效用同时给交易所更高收益。最终用行业参数测试床量化收益增益（7%-33%）和社会福利改进，并讨论适用边界与未来方向。

## 摘要逐句图谱

### 1. Abstract P1 S1

- order：1

- locator：Abstract P1 S1

- paraphrase_cn：在移动广告生态中，广告交易所在匹配广告主与发布商方面的作用近年来显著增长。

- move_code：CONTEXT

- statement_status：fact

- why_here_cn：开篇把研究置于现实行业背景，说明研究对象（广告交易所）具有重要地位。

- inherits_from_previous_cn：无

- changes_argument_state_cn：建立研究领域和现实重要性。

- sets_up_next_cn：为下一句引入广告交易所实时拍卖机制作背景铺垫。

- failure_if_removed_cn：摘要失去行业语境，读者无法立即理解研究对象的重要性。

- evidence_pointer：Abstract first sentence

### 2. Abstract P1 S2

- order：2

- locator：Abstract P1 S2

- paraphrase_cn：在移动广告交易所，印象（展示广告的机会）通过拍卖机制实时卖给广告主。

- move_code：CONTEXT

- statement_status：fact

- why_here_cn：说明本文研究对象的具体交易机制。

- inherits_from_previous_cn：延续广告交易所重要性。

- changes_argument_state_cn：把研究对象具体化为实时拍卖。

- sets_up_next_cn：为下一句描述传统机制的局限作前提。

- failure_if_removed_cn：读者不知道印象如何被出售，后续低效论证缺乏载体。

- evidence_pointer：Abstract second sentence

### 3. Abstract P1 S3

- order：3

- locator：Abstract P1 S3

- paraphrase_cn：传统机制选择单一广告主，其广告在印象整个持续时间（即用户整个访问期间）展示。

- move_code：PHENOMENON

- statement_status：fact

- why_here_cn：陈述现状机制的核心特征。

- inherits_from_previous_cn：承接实时拍卖机制。

- changes_argument_state_cn：建立本文要挑战的现状。

- sets_up_next_cn：为下一句指出这种机制的效率缺陷作铺垫。

- failure_if_removed_cn：未说明传统机制是什么，低效论证失去对象。

- evidence_pointer：Abstract third sentence

### 4. Abstract P1 S4

- order：4

- locator：Abstract P1 S4

- paraphrase_cn：我们论证这种机制导致配置低效，因为只展示胜者广告会阻碍交易所利用其他广告主支付意愿在印象生命周期内变高的收入机会。

- move_code：LIMITATION

- statement_status：author_inference

- why_here_cn：提出本文的核心问题所在。

- inherits_from_previous_cn：基于传统机制单广告全程展示的事实。

- changes_argument_state_cn：定义研究要消除的效率损失。

- sets_up_next_cn：为下一句提出研究目标作依据。

- failure_if_removed_cn：摘要失去问题陈述，全文研究动机缺失。

- evidence_pointer：Abstract fourth sentence

### 5. Abstract P1 S5

- order：5

- locator：Abstract P1 S5

- paraphrase_cn：本文目标是消除这种效率损失，提供在印象生命周期内顺序展示多个广告的机制。

- move_code：RQ_OR_OBJECTIVE

- statement_status：author_inference

- why_here_cn：明确提出研究目标。

- inherits_from_previous_cn：从低效问题直接导出。

- changes_argument_state_cn：给出解决方案的方向。

- sets_up_next_cn：为下一句说明两种设置作铺垫。

- failure_if_removed_cn：读者不知道论文要解决什么。

- evidence_pointer：Abstract fifth sentence

### 6. Abstract P1 S6

- order：6

- locator：Abstract P1 S6

- paraphrase_cn：我们考虑两种设置：一种是每次拍卖对广告主个体理性，另一种是广告主长期比传统机制更好，并推导每种设置的收益最优机制。

- move_code：STUDY_OVERVIEW

- statement_status：author_inference

- why_here_cn：概述两种设置和两种最优机制。

- inherits_from_previous_cn：承接研究目标。

- changes_argument_state_cn：告知读者研究的具体范围和两个设置。

- sets_up_next_cn：为下一句解释OPT-IR的随机化支付作铺垫。

- failure_if_removed_cn：摘要缺少研究设计概览。

- evidence_pointer：Abstract sixth sentence

### 7. Abstract P1 S7

- order：7

- locator：Abstract P1 S7

- paraphrase_cn：为高效计算支付规则，第一种设置的最优机制使用随机化支付。

- move_code：DESIGN_FEATURE

- statement_status：design_decision

- why_here_cn：强调核心设计创新。

- inherits_from_previous_cn：承接第一种设置的最优机制。

- changes_argument_state_cn：引入随机化支付这一关键技术决策。

- sets_up_next_cn：为下一句讨论机制对交易所和广告主的影响作铺垫。

- failure_if_removed_cn：摘要缺少支付实现的核心创新。

- evidence_pointer：Abstract seventh sentence

### 8. Abstract P1 S8

- order：8

- locator：Abstract P1 S8

- paraphrase_cn：在该机制下，交易所相对传统机制总是受益，但广告主可能受益也可能受损——我们展示两种可能性。

- move_code：RESULT

- statement_status：empirical_result

- why_here_cn：报告关键福利结果。

- inherits_from_previous_cn：基于OPT-IR机制。

- changes_argument_state_cn：建立广告主福利不确定性，为第二种设置作动机。

- sets_up_next_cn：为下一句引入互惠机制作铺垫。

- failure_if_removed_cn：缺少对广告主福利的关键发现。

- evidence_pointer：Abstract eighth sentence

### 9. Abstract P1 S9

- order：9

- locator：Abstract P1 S9

- paraphrase_cn：第二种设置的最优机制是互惠机制，保证双方相对传统机制长期win-win。

- move_code：RESULT

- statement_status：theory_claim

- why_here_cn：报告第二种机制的性质。

- inherits_from_previous_cn：回应广告主可能受损的问题。

- changes_argument_state_cn：建立一个福利保障机制。

- sets_up_next_cn：为下一句强调可计算性作铺垫。

- failure_if_removed_cn：摘要缺少OPT-MB机制的核心贡献。

- evidence_pointer：Abstract ninth sentence

### 10. Abstract P1 S10

- order：10

- locator：Abstract P1 S10

- paraphrase_cn：令人高兴的是，两种机制的广告分配和支付都可高效计算，因此适合实时竞价。

- move_code：CONTRIBUTION

- statement_status：contribution_claim

- why_here_cn：总结机制的实际可用性。

- inherits_from_previous_cn：基于两种机制的设计。

- changes_argument_state_cn：强调可实施性，完成摘要贡献声明。

- sets_up_next_cn：摘要结束，为正文展开作铺垫。

- failure_if_removed_cn：缺少可实时实施的贡献。

- evidence_pointer：Abstract tenth sentence

## 引言逐句图谱

### 1. Introduction P1 S1

- order：1

- locator：Introduction P1 S1

- paraphrase_cn：许多移动发布商通过应用内广告获得收入。

- move_code：CONTEXT

- statement_status：fact

- why_here_cn：建立论文研究对象的现实基础。

- inherits_from_previous_cn：无

- changes_argument_state_cn：引入移动广告的价值链。

- sets_up_next_cn：为后续提到移动广告增长作铺垫。

- failure_if_removed_cn：引言失去起始语境。

- evidence_pointer：Introduction paragraph 1 sentence 1

### 2. Introduction P1 S2

- order：2

- locator：Introduction P1 S2

- paraphrase_cn：这一收入流主要靠过去几年移动广告的巨幅增长维持。

- move_code：CONTEXT

- statement_status：fact

- why_here_cn：说明移动广告收入的重要性。

- inherits_from_previous_cn：承接应用内广告收入。

- changes_argument_state_cn：建立行业增长背景。

- sets_up_next_cn：为下一句引用具体数据作铺垫。

- failure_if_removed_cn：缺少行业增长背景，研究重要性不突出。

- evidence_pointer：Introduction paragraph 1 sentence 2

### 3. Introduction P1 S3

- order：3

- locator：Introduction P1 S3

- paraphrase_cn：2017财年移动广告占全部广告收入的56.7%（499亿美元）。

- move_code：PRACTICAL_STAKES

- statement_status：fact

- why_here_cn：用具体数据证明市场规模与重要性。

- inherits_from_previous_cn：承接移动广告增长。

- changes_argument_state_cn：量化行业背景，增强研究动机。

- sets_up_next_cn：为下一句提及销售渠道作铺垫。

- failure_if_removed_cn：缺乏具体证据支撑其重要性。

- evidence_pointer：Introduction paragraph 1 sentence 3

### 4. Introduction P1 S4

- order：4

- locator：Introduction P1 S4

- paraphrase_cn：增长的关键驱动力之一是多种数字广告销售渠道的出现。

- move_code：TRANSITION

- statement_status：fact

- why_here_cn：从行业背景转向渠道结构。

- inherits_from_previous_cn：承接广告收入增长。

- changes_argument_state_cn：引入不同销售渠道。

- sets_up_next_cn：为下一句介绍广告网络作铺垫。

- failure_if_removed_cn：渠道背景缺失。

- evidence_pointer：Introduction paragraph 1 sentence 4

### 5. Introduction P1 S5

- order：5

- locator：Introduction P1 S5

- paraphrase_cn：直到最近，发布商主要通过与广告网络签订长期合同销售印象。

- move_code：CONTEXT

- statement_status：fact

- why_here_cn：介绍传统销售方式。

- inherits_from_previous_cn：承接销售渠道。

- changes_argument_state_cn：建立与后续广告交易所的对比。

- sets_up_next_cn：为引入广告交易所作铺垫。

- failure_if_removed_cn：缺乏传统机制对比背景。

- evidence_pointer：Introduction paragraph 1 sentence 5

### 6. Introduction P1 S6

- order：6

- locator：Introduction P1 S6

- paraphrase_cn：这些合同通常基于收入分成。

- move_code：CONTEXT

- statement_status：fact

- why_here_cn：解释传统合同的性质。

- inherits_from_previous_cn：承接长期合同。

- changes_argument_state_cn：明确传统销售机制局限。

- sets_up_next_cn：为广告交易所的兴起作铺垫。

- failure_if_removed_cn：削弱理解传统机制为何被替代。

- evidence_pointer：Introduction paragraph 1 sentence 6

### 7. Introduction P2 S1

- order：7

- locator：Introduction P2 S1

- paraphrase_cn：现在流行的买卖数字广告方式是通过广告交易所——一种实时拍卖的在线自动化市场。

- move_code：CONTEXT

- statement_status：fact

- why_here_cn：引入论文的研究对象广告交易所。

- inherits_from_previous_cn：承接长期合同背景。

- changes_argument_state_cn：从广告网络转向广告交易所。

- sets_up_next_cn：为下一句说明广告交易所对发布商的吸引力作铺垫。

- failure_if_removed_cn：研究对象缺失。

- evidence_pointer：Introduction paragraph 2 sentence 1

### 8. Introduction P2 S2

- order：8

- locator：Introduction P2 S2

- paraphrase_cn：广告交易所对发布商有吸引力：提供流动性、透明度，并帮助获得更好价格。

- move_code：PRACTICAL_STAKES

- statement_status：fact

- why_here_cn：说明交易所对供给方的价值。

- inherits_from_previous_cn：承接广告交易所定义。

- changes_argument_state_cn：建立交易所的重要性。

- sets_up_next_cn：为下一句说明对广告主的价值作铺垫。

- failure_if_removed_cn：缺少交易所优势论述。

- evidence_pointer：Introduction paragraph 2 sentence 2

### 9. Introduction P2 S3

- order：9

- locator：Introduction P2 S3

- paraphrase_cn：广告主也能接触大量库存并更好地定向受众。

- move_code：PRACTICAL_STAKES

- statement_status：fact

- why_here_cn：说明交易所对需求方的价值。

- inherits_from_previous_cn：承接交易所优势。

- changes_argument_state_cn：建立双方受益的格局。

- sets_up_next_cn：为下一句总结交易所增长作铺垫。

- failure_if_removed_cn：缺少需求方视角。

- evidence_pointer：Introduction paragraph 2 sentence 3

### 10. Introduction P2 S4

- order：10

- locator：Introduction P2 S4

- paraphrase_cn：由于对双方都有益，广告交易所交易数字广告的增长近年来突飞猛进。

- move_code：CONTEXT

- statement_status：fact

- why_here_cn：总结交易所的重要性。

- inherits_from_previous_cn：承接双方受益。

- changes_argument_state_cn：确立研究背景的现实重要性。

- sets_up_next_cn：为下一句提到交易所与发布商目标对齐作铺垫。

- failure_if_removed_cn：削弱研究背景。

- evidence_pointer：Introduction paragraph 2 sentence 4

### 11. Introduction P2 S5

- order：11

- locator：Introduction P2 S5

- paraphrase_cn：当今广告交易所与发布商目标紧密相连——交易所更高收入意味着发布商更高收入。

- move_code：PRACTICAL_STAKES

- statement_status：fact

- why_here_cn：为后文以交易所收益最大化为目标提供合理性。

- inherits_from_previous_cn：承接交易所重要性。

- changes_argument_state_cn：把交易所收益与发布商利益绑定。

- sets_up_next_cn：为研究目标设定作铺垫。

- failure_if_removed_cn：以交易所收益为目标缺乏动机。

- evidence_pointer：Introduction paragraph 2 sentence 5

### 12. Introduction P3 S1

- order：12

- locator：Introduction P3 S1

- paraphrase_cn：我们聚焦移动设备（如智能手机和平板）上的展示广告。

- move_code：CONTEXT

- statement_status：fact

- why_here_cn：从一般广告交易所收缩到移动展示广告。

- inherits_from_previous_cn：承接广告交易所背景。

- changes_argument_state_cn：限定研究对象。

- sets_up_next_cn：为下一句介绍移动广告交易所作铺垫。

- failure_if_removed_cn：研究对象不聚焦。

- evidence_pointer：Introduction paragraph 3 sentence 1

### 13. Introduction P3 S2

- order：13

- locator：Introduction P3 S2

- paraphrase_cn：在移动广告交易所，广告主或代理公司为来自移动设备的印象竞价。

- move_code：CONTEXT

- statement_status：fact

- why_here_cn：说明移动广告交易所的实际参与者。

- inherits_from_previous_cn：承接移动展示广告。

- changes_argument_state_cn：建立具体参与主体。

- sets_up_next_cn：为下一句强调移动应用内广告的独特性作铺垫。

- failure_if_removed_cn：移动广告交易所运作细节缺失。

- evidence_pointer：Introduction paragraph 3 sentence 2

### 14. Introduction P3 S3

- order：14

- locator：Introduction P3 S3

- paraphrase_cn：移动应用内广告尤其能从我们要消除的低效中受益，因为应用会话通常比网页访问长得多。

- move_code：PRACTICAL_STAKES

- statement_status：fact

- why_here_cn：说明时间维度在移动应用内广告中的重要性。

- inherits_from_previous_cn：承接移动广告交易所。

- changes_argument_state_cn：强化分区印象的动机。

- sets_up_next_cn：为下一句描述传统拍卖作铺垫。

- failure_if_removed_cn：时间维度动机缺失。

- evidence_pointer：Introduction paragraph 3 sentence 3

### 15. Introduction P3 S4

- order：15

- locator：Introduction P3 S4

- paraphrase_cn：传统点击广告拍卖从每个广告主征集每次点击价值报价，胜者广告在印象整个生命周期展示。

- move_code：PHENOMENON

- statement_status：fact

- why_here_cn：陈述现有机制的运作方式。

- inherits_from_previous_cn：承接移动广告场景。

- changes_argument_state_cn：建立后续要挑战的现状机制。

- sets_up_next_cn：为下一句引入低效示例作铺垫。

- failure_if_removed_cn：现状机制描述缺失。

- evidence_pointer：Introduction paragraph 3 sentence 4

### 16. Introduction P3 S5

- order：16

- locator：Introduction P3 S5

- paraphrase_cn：我们通过一个简单但说明性的例子强调传统拍卖的配置低效。

- move_code：TRANSITION

- statement_status：author_inference

- why_here_cn：引出下一小节的具体示例。

- inherits_from_previous_cn：承接传统拍卖描述。

- changes_argument_state_cn：预告低效论证。

- sets_up_next_cn：为1.1节的例子作铺垫。

- failure_if_removed_cn：低效示例缺乏引导。

- evidence_pointer：Introduction paragraph 3 sentence 5

### 17. Introduction 1.1 P1 S1

- order：17

- locator：Introduction 1.1 P1 S1

- paraphrase_cn：考虑两个广告主1和2分别竞争展示广告A和B的移动印象传统拍卖。

- move_code：PHENOMENON

- statement_status：author_inference

- why_here_cn：用最小示例建立低效现象。

- inherits_from_previous_cn：承接传统拍卖描述。

- changes_argument_state_cn：构造具体场景。

- sets_up_next_cn：为下一句说明B获胜作铺垫。

- failure_if_removed_cn：示例场景缺失。

- evidence_pointer：Introduction 1.1 paragraph 1

### 18. Introduction 1.1 P1 S2

- order：18

- locator：Introduction 1.1 P1 S2

- paraphrase_cn：假设广告主2赢得拍卖，因此广告B展示给用户。

- move_code：PHENOMENON

- statement_status：author_inference

- why_here_cn：设定胜者B。

- inherits_from_previous_cn：承接示例设定。

- changes_argument_state_cn：确定拍卖结果。

- sets_up_next_cn：为下一句说明B的点击概率变化作铺垫。

- failure_if_removed_cn：示例无法继续。

- evidence_pointer：Introduction 1.1 paragraph 1 sentence 2

### 19. Introduction 1.1 P1 S3

- order：19

- locator：Introduction 1.1 P1 S3

- paraphrase_cn：随着应用会话推进，广告B的点击概率因多种因素变化。

- move_code：CAUSAL_MECHANISM

- statement_status：author_inference

- why_here_cn：引入广告价值随时间变化的核心假设。

- inherits_from_previous_cn：承接B被展示。

- changes_argument_state_cn：建立时间维度价值变化。

- sets_up_next_cn：为下一句说明瞬时价值变化作铺垫。

- failure_if_removed_cn：时间变化机制缺失。

- evidence_pointer：Introduction 1.1 paragraph 1 sentence 3

### 20. Introduction 1.1 P1 S4

- order：20

- locator：Introduction 1.1 P1 S4

- paraphrase_cn：因为展示广告的价值与其点击概率相关，广告B的瞬时价值也随时间变化。

- move_code：CAUSAL_MECHANISM

- statement_status：author_inference

- why_here_cn：把点击概率变化与广告主支付意愿联系起来。

- inherits_from_previous_cn：承接点击概率变化。

- changes_argument_state_cn：建立广告主价值与时间的联系。

- sets_up_next_cn：为图形展示作铺垫。

- failure_if_removed_cn：低效论证缺乏因果链。

- evidence_pointer：Introduction 1.1 paragraph 1 sentence 4

### 21. Introduction 1.1 P2 S1

- order：21

- locator：Introduction 1.1 P2 S1

- paraphrase_cn：现在考虑输掉拍卖的广告A。

- move_code：PHENOMENON

- statement_status：author_inference

- why_here_cn：引入败者广告。

- inherits_from_previous_cn：承接B获胜。

- changes_argument_state_cn：构造对比对象。

- sets_up_next_cn：为下一句说明A的价值变化作铺垫。

- failure_if_removed_cn：无法对比胜者与败者。

- evidence_pointer：Introduction 1.1 paragraph 2 sentence 1

### 22. Introduction 1.1 P2 S2

- order：22

- locator：Introduction 1.1 P2 S2

- paraphrase_cn：若A被展示，其瞬时价值也随时间变化，但速率可能与B不同。

- move_code：CAUSAL_MECHANISM

- statement_status：author_inference

- why_here_cn：说明不同广告有不同价值轨迹。

- inherits_from_previous_cn：承接败者A。

- changes_argument_state_cn：建立广告间异质性。

- sets_up_next_cn：为图形对比作铺垫。

- failure_if_removed_cn：广告间异质性缺失。

- evidence_pointer：Introduction 1.1 paragraph 2 sentence 2

### 23. Introduction 1.1 P2 S3

- order：23

- locator：Introduction 1.1 P2 S3

- paraphrase_cn：在时间区间[t1,t2]，A的瞬时价值高于B。

- move_code：PHENOMENON

- statement_status：author_inference

- why_here_cn：创造低效出现的条件。

- inherits_from_previous_cn：承接A的价值轨迹。

- changes_argument_state_cn：建立A在某时段更优。

- sets_up_next_cn：为下一句说明广告主1愿意支付更多作铺垫。

- failure_if_removed_cn：低效的核心条件缺失。

- evidence_pointer：Introduction 1.1 paragraph 2 sentence 3

### 24. Introduction 1.1 P2 S4

- order：24

- locator：Introduction 1.1 P2 S4

- paraphrase_cn：因此广告主1在该区间愿意为展示A支付比广告主2为B支付更多。

- move_code：CAUSAL_MECHANISM

- statement_status：author_inference

- why_here_cn：把价值差异转化为支付意愿差异。

- inherits_from_previous_cn：承接A瞬时价值更高。

- changes_argument_state_cn：建立广告主支付意愿变化。

- sets_up_next_cn：为说明配置低效作铺垫。

- failure_if_removed_cn：支付意愿与低效的因果缺失。

- evidence_pointer：Introduction 1.1 paragraph 2 sentence 4

### 25. Introduction 1.1 P2 S5

- order：25

- locator：Introduction 1.1 P2 S5

- paraphrase_cn：但因为广告主2获胜，B在整个印象生命周期展示。

- move_code：PHENOMENON

- statement_status：author_inference

- why_here_cn：回到现状机制的约束。

- inherits_from_previous_cn：承接拍卖结果。

- changes_argument_state_cn：强调传统机制的刚性。

- sets_up_next_cn：为低效定义作铺垫。

- failure_if_removed_cn：现状机制的刚性缺失。

- evidence_pointer：Introduction 1.1 paragraph 2 sentence 5

### 26. Introduction 1.1 P2 S6

- order：26

- locator：Introduction 1.1 P2 S6

- paraphrase_cn：因此图中的阴影区域代表从广告交易所角度看传统拍卖的配置低效。

- move_code：LIMITATION

- statement_status：author_inference

- why_here_cn：正式定义低效并给出图形证据。

- inherits_from_previous_cn：承接B全程展示。

- changes_argument_state_cn：把例子转化为正式问题。

- sets_up_next_cn：为分区印象想法作铺垫。

- failure_if_removed_cn：低效问题未定义。

- evidence_pointer：Introduction 1.1 paragraph 2 sentence 6

### 27. Introduction 1.1 P3 S1

- order：27

- locator：Introduction 1.1 P3 S1

- paraphrase_cn：这引出一个想法：拍卖印象时，可分配多个广告，每个广告安排到特定时间槽。

- move_code：DESIGN_FEATURE

- statement_status：author_inference

- why_here_cn：提出核心设计方向。

- inherits_from_previous_cn：承接配置低效。

- changes_argument_state_cn：提出分区印象。

- sets_up_next_cn：为下一句说明槽按需展示作铺垫。

- failure_if_removed_cn：核心设计想法缺失。

- evidence_pointer：Introduction 1.1 paragraph 3

### 28. Introduction 1.1 P3 S2

- order：28

- locator：Introduction 1.1 P3 S2

- paraphrase_cn：当然，安排到某槽的广告只有在印象持续到该槽时才能实际展示。

- move_code：DESIGN_FEATURE

- statement_status：author_inference

- why_here_cn：说明分区印象的约束条件。

- inherits_from_previous_cn：承接分区印象想法。

- changes_argument_state_cn：明确动态约束。

- sets_up_next_cn：为下一句的示例作铺垫。

- failure_if_removed_cn：动态约束缺失，机制定义不完整。

- evidence_pointer：Introduction 1.1 paragraph 3 sentence 2

### 29. Introduction 1.1 P3 S3

- order：29

- locator：Introduction 1.1 P3 S3

- paraphrase_cn：例如，上述例子中交易所可把A安排在[t1,t2]，B安排到其他区间。

- move_code：DESIGN_FEATURE

- statement_status：author_inference

- why_here_cn：给出分区印象的具体示例。

- inherits_from_previous_cn：承接分区想法。

- changes_argument_state_cn：说明分区印象的可操作性。

- sets_up_next_cn：为下一句说明潜在收益作铺垫。

- failure_if_removed_cn：分区示例缺失。

- evidence_pointer：Introduction 1.1 paragraph 3 sentence 3

### 30. Introduction 1.1 P3 S4

- order：30

- locator：Introduction 1.1 P3 S4

- paraphrase_cn：给印象分配多个广告可能给交易所带来更多剩余。

- move_code：BENEFIT

- statement_status：author_inference

- why_here_cn：说明设计的经济动机。

- inherits_from_previous_cn：承接分区示例。

- changes_argument_state_cn：建立设计的经济收益。

- sets_up_next_cn：为下一句排除技术障碍作铺垫。

- failure_if_removed_cn：经济效益论证缺失。

- evidence_pointer：Introduction 1.1 paragraph 3 sentence 4

### 31. Introduction 1.1 P4 S1

- order：31

- locator：Introduction 1.1 P4 S1

- paraphrase_cn：实现这一想法没有技术障碍——DoubleClick和OpenX允许发布商动态重载广告。

- move_code：DESIGN_FEATURE

- statement_status：fact

- why_here_cn：排除技术可行性问题。

- inherits_from_previous_cn：承接分区想法。

- changes_argument_state_cn：确认设计可实施。

- sets_up_next_cn：为下一句提出目标作铺垫。

- failure_if_removed_cn：技术可行性论证缺失。

- evidence_pointer：Introduction 1.1 paragraph 4

### 32. Introduction 1.1 P5 S1

- order：32

- locator：Introduction 1.1 P5 S1

- paraphrase_cn：一个自然而然的想法是每个槽独立分配最佳广告。

- move_code：DESIGN_FEATURE

- statement_status：author_inference

- why_here_cn：提出直觉候选机制。

- inherits_from_previous_cn：承接分区想法。

- changes_argument_state_cn：建立SEQ机制。

- sets_up_next_cn：为下一句指出其局限作铺垫。

- failure_if_removed_cn：SEQ机制引入缺失。

- evidence_pointer：Introduction 1.1 paragraph 5

### 33. Introduction 1.1 P5 S2

- order：33

- locator：Introduction 1.1 P5 S2

- paraphrase_cn：但这种机制会带来次优收入，因为它不考虑当前槽广告对未来槽的影响。

- move_code：LIMITATION

- statement_status：author_inference

- why_here_cn：指出直觉候选的缺陷。

- inherits_from_previous_cn：承接SEQ机制。

- changes_argument_state_cn：排除简单机制。

- sets_up_next_cn：为后文详细比较SEQ作铺垫。

- failure_if_removed_cn：SEQ缺陷预告缺失。

- evidence_pointer：Introduction 1.1 paragraph 5 sentence 2

### 34. Introduction 1.1 P5 S3

- order：34

- locator：Introduction 1.1 P5 S3

- paraphrase_cn：我们将分析该机制并展示其收入可能显著低于最优机制。

- move_code：STUDY_OVERVIEW

- statement_status：author_inference

- why_here_cn：预告后续分析。

- inherits_from_previous_cn：承接SEQ缺陷。

- changes_argument_state_cn：承诺证明SEQ次优。

- sets_up_next_cn：为Section 5-6作铺垫。

- failure_if_removed_cn：缺少后续分析预告。

- evidence_pointer：Introduction 1.1 paragraph 5 sentence 3

### 35. Introduction 1.1 P6 S1

- order：35

- locator：Introduction 1.1 P6 S1

- paraphrase_cn：相关问题是对广告主的福利影响。

- move_code：TRANSITION

- statement_status：author_inference

- why_here_cn：引入福利维度。

- inherits_from_previous_cn：承接机制比较。

- changes_argument_state_cn：从交易所转移到广告主。

- sets_up_next_cn：为下一句讨论广告主是否受益作铺垫。

- failure_if_removed_cn：广告主福利维度缺失。

- evidence_pointer：Introduction 1.1 paragraph 6 sentence 1

### 36. Introduction 1.1 P6 S2

- order：36

- locator：Introduction 1.1 P6 S2

- paraphrase_cn：交易所相对传统机制肯定受益，但广告主是否受益不清楚。

- move_code：LIMITATION

- statement_status：author_inference

- why_here_cn：提出福利不确定性。

- inherits_from_previous_cn：承接福利影响。

- changes_argument_state_cn：建立win-lose可能性。

- sets_up_next_cn：为下一句考虑替代机制作铺垫。

- failure_if_removed_cn：广告主福利不确定性缺失。

- evidence_pointer：Introduction 1.1 paragraph 6 sentence 2

### 37. Introduction 1.1 P6 S3

- order：37

- locator：Introduction 1.1 P6 S3

- paraphrase_cn：如果广告主在某些情况下更差，可以考虑确保广告主至少与传统机制一样好的机制。

- move_code：GAP

- statement_status：author_inference

- why_here_cn：提出互惠机制的研究缺口。

- inherits_from_previous_cn：承接福利不确定性。

- changes_argument_state_cn：引入另一种设置。

- sets_up_next_cn：为后文P^MB作铺垫。

- failure_if_removed_cn：互惠机制动机缺失。

- evidence_pointer：Introduction 1.1 paragraph 6 sentence 3

### 38. Introduction 1.1 P7 S1

- order：38

- locator：Introduction 1.1 P7 S1

- paraphrase_cn：鉴于大量印象通过广告交易所销售，设计机制消除这种低效对广告生态有重大影响。

- move_code：RQ_OR_OBJECTIVE

- statement_status：author_inference

- why_here_cn：总结研究目标的重要性。

- inherits_from_previous_cn：承接低效和福利问题。

- changes_argument_state_cn：确立研究价值。

- sets_up_next_cn：为下一句提出实时性要求作铺垫。

- failure_if_removed_cn：研究目标的重要性缺失。

- evidence_pointer：Introduction 1.1 paragraph 7 sentence 1

### 39. Introduction 1.1 P7 S2

- order：39

- locator：Introduction 1.1 P7 S2

- paraphrase_cn：机制应适合实时竞价，即广告分配和支付应可高效计算。

- move_code：DESIGN_FEATURE

- statement_status：author_inference

- why_here_cn：提出设计的实时性要求。

- inherits_from_previous_cn：承接研究目标。

- changes_argument_state_cn：建立技术约束。

- sets_up_next_cn：为下一句要求结构简单作铺垫。

- failure_if_removed_cn：实时性要求缺失。

- evidence_pointer：Introduction 1.1 paragraph 7 sentence 2

### 40. Introduction 1.1 P7 S3

- order：40

- locator：Introduction 1.1 P7 S3

- paraphrase_cn：为更广接受度，机制结构简单也有帮助。

- move_code：DESIGN_FEATURE

- statement_status：author_inference

- why_here_cn：提出简单性要求。

- inherits_from_previous_cn：承接实时性要求。

- changes_argument_state_cn：建立设计准则。

- sets_up_next_cn：为贡献列表作铺垫。

- failure_if_removed_cn：设计准则不完整。

- evidence_pointer：Introduction 1.1 paragraph 7 sentence 3

### 41. Introduction 1.2 P1 S1

- order：41

- locator：Introduction 1.2 P1 S1

- paraphrase_cn：我们提出解决当前移动广告交易所配置低效的方法。

- move_code：CONTRIBUTION

- statement_status：contribution_claim

- why_here_cn：正式列出第一项贡献。

- inherits_from_previous_cn：承接研究目标。

- changes_argument_state_cn：开始贡献声明。

- sets_up_next_cn：为下一句解释框架作铺垫。

- failure_if_removed_cn：贡献声明缺失。

- evidence_pointer：Introduction 1.2 paragraph 1

### 42. Introduction 1.2 P1 S2

- order：42

- locator：Introduction 1.2 P1 S2

- paraphrase_cn：我们开发了一个框架：把印象切成时间槽并顺序分配广告。

- move_code：CONTRIBUTION

- statement_status：design_decision

- why_here_cn：给出具体解决框架。

- inherits_from_previous_cn：承接贡献声明。

- changes_argument_state_cn：定义分区印象框架。

- sets_up_next_cn：为下一句介绍两种设置作铺垫。

- failure_if_removed_cn：框架描述缺失。

- evidence_pointer：Introduction 1.2 paragraph 1 sentence 2

### 43. Introduction 1.2 P2 S1

- order：43

- locator：Introduction 1.2 P2 S1

- paraphrase_cn：我们在两种设置下获得最优机制，两种设置在广告主效用保障上不同。

- move_code：STUDY_OVERVIEW

- statement_status：author_inference

- why_here_cn：概述两种设置。

- inherits_from_previous_cn：承接框架。

- changes_argument_state_cn：引入设置差异。

- sets_up_next_cn：为下一句具体说明设置1作铺垫。

- failure_if_removed_cn：两种设置概览缺失。

- evidence_pointer：Introduction 1.2 paragraph 2 sentence 1

### 44. Introduction 1.2 P2 S2

- order：44

- locator：Introduction 1.2 P2 S2

- paraphrase_cn：设置1要求每次拍卖个体理性；设置2要求广告主长期至少获得传统机制效用。

- move_code：STUDY_OVERVIEW

- statement_status：author_inference

- why_here_cn：说明两种设置的具体差别。

- inherits_from_previous_cn：承接设置概述。

- changes_argument_state_cn：定义P^IR和P^MB。

- sets_up_next_cn：为下一句命名两个机制作铺垫。

- failure_if_removed_cn：设置定义缺失。

- evidence_pointer：Introduction 1.2 paragraph 2 sentence 2

### 45. Introduction 1.2 P2 S3

- order：45

- locator：Introduction 1.2 P2 S3

- paraphrase_cn：我们分别称设置1和2的最优机制为OPT-IR和OPT-MB。

- move_code：STUDY_OVERVIEW

- statement_status：author_inference

- why_here_cn：命名两个机制。

- inherits_from_previous_cn：承接设置定义。

- changes_argument_state_cn：建立机制名称。

- sets_up_next_cn：为后续使用名称作铺垫。

- failure_if_removed_cn：机制名称缺失，后续行文混乱。

- evidence_pointer：Introduction 1.2 paragraph 2 sentence 3

### 46. Introduction 1.2 P2 S4

- order：46

- locator：Introduction 1.2 P2 S4

- paraphrase_cn：传统机制在两种设置下都是可行解。

- move_code：CONTRIBUTION

- statement_status：author_inference

- why_here_cn：为后文证明OPT-IR总是优于BASE作铺垫。

- inherits_from_previous_cn：承接两种设置。

- changes_argument_state_cn：建立BASE可行性。

- sets_up_next_cn：为Section 8的收益比较作铺垫。

- failure_if_removed_cn：BASE可行性的关键前提缺失。

- evidence_pointer：Introduction 1.2 paragraph 2 sentence 4

### 47. Introduction 1.2 P3 S1

- order：47

- locator：Introduction 1.2 P3 S1

- paraphrase_cn：OPT-IR和OPT-MB机制非常适合实时竞价。

- move_code：CONTRIBUTION

- statement_status：author_inference

- why_here_cn：强调机制可实施性。

- inherits_from_previous_cn：承接机制定义。

- changes_argument_state_cn：建立实时性贡献。

- sets_up_next_cn：为下一句解释机制组成作铺垫。

- failure_if_removed_cn：实时性贡献缺失。

- evidence_pointer：Introduction 1.2 paragraph 3 sentence 1

### 48. Introduction 1.2 P3 S2

- order：48

- locator：Introduction 1.2 P3 S2

- paraphrase_cn：机制由分配规则和支付规则组成。

- move_code：DESIGN_FEATURE

- statement_status：design_decision

- why_here_cn：定义机制结构。

- inherits_from_previous_cn：承接机制介绍。

- changes_argument_state_cn：建立机制组成。

- sets_up_next_cn：为下一句说明交易所处理流程作铺垫。

- failure_if_removed_cn：机制结构定义缺失。

- evidence_pointer：Introduction 1.2 paragraph 3 sentence 2

### 49. Introduction 1.2 P3 S3

- order：49

- locator：Introduction 1.2 P3 S3

- paraphrase_cn：广告交易所从收到印象到交付广告需要处理多个活动。

- move_code：CONTEXT

- statement_status：fact

- why_here_cn：描述交易所实际操作流程。

- inherits_from_previous_cn：承接机制结构。

- changes_argument_state_cn：引入实时性约束。

- sets_up_next_cn：为下一句提出时间限制作铺垫。

- failure_if_removed_cn：交易所流程背景缺失。

- evidence_pointer：Introduction 1.2 paragraph 3 sentence 3

### 50. Introduction 1.2 P3 S4

- order：50

- locator：Introduction 1.2 P3 S4

- paraphrase_cn：该过程必须在150毫秒内完成，以避免用户感知延迟。

- move_code：DESIGN_FEATURE

- statement_status：fact

- why_here_cn：提出具体实时约束。

- inherits_from_previous_cn：承接交易所流程。

- changes_argument_state_cn：建立计算复杂度要求。

- sets_up_next_cn：为下一句介绍动态规划复杂度作铺垫。

- failure_if_removed_cn：150ms约束缺失。

- evidence_pointer：Introduction 1.2 paragraph 3 sentence 4

### 51. Introduction 1.2 P3 S5

- order：51

- locator：Introduction 1.2 P3 S5

- paraphrase_cn：两种最优机制的分配规则可通过复杂度O(AN)的确定性动态规划高效获得。

- move_code：DESIGN_FEATURE

- statement_status：author_inference

- why_here_cn：说明分配规则的可计算性。

- inherits_from_previous_cn：承接150ms约束。

- changes_argument_state_cn：证明分配规则高效。

- sets_up_next_cn：为下一句强调可纳入广告交付流程作铺垫。

- failure_if_removed_cn：分配可计算性贡献缺失。

- evidence_pointer：Introduction 1.2 paragraph 3 sentence 5

### 52. Introduction 1.2 P3 S6

- order：52

- locator：Introduction 1.2 P3 S6

- paraphrase_cn：因此分配规则可纳入广告交付流程而不造成显著延迟。

- move_code：CONTRIBUTION

- statement_status：author_inference

- why_here_cn：连接可计算性与实际部署。

- inherits_from_previous_cn：承接复杂度O(AN)。

- changes_argument_state_cn：确认实时可部署性。

- sets_up_next_cn：为下一句说明OPT-MB一阶最优作铺垫。

- failure_if_removed_cn：可部署性论证缺失。

- evidence_pointer：Introduction 1.2 paragraph 3 sentence 6

### 53. Introduction 1.2 P3 S7

- order：53

- locator：Introduction 1.2 P3 S7

- paraphrase_cn：此外OPT-MB的分配规则是一阶最优，产生最大社会福祉。

- move_code：DESIGN_FEATURE

- statement_status：author_inference

- why_here_cn：强调OPT-MB的效率性质。

- inherits_from_previous_cn：承接分配规则。

- changes_argument_state_cn：建立一阶最优性。

- sets_up_next_cn：为下一句讨论支付计算作铺垫。

- failure_if_removed_cn：OPT-MB效率性质缺失。

- evidence_pointer：Introduction 1.2 paragraph 3 sentence 7

### 54. Introduction 1.2 P4 S1

- order：54

- locator：Introduction 1.2 P4 S1

- paraphrase_cn：但OPT-IR的支付规则按原样难以计算。

- move_code：LIMITATION

- statement_status：author_inference

- why_here_cn：引出支付计算难题。

- inherits_from_previous_cn：承接OPT-IR机制。

- changes_argument_state_cn：建立实现挑战。

- sets_up_next_cn：为下一句解释信息租金作铺垫。

- failure_if_removed_cn：支付计算难题缺失。

- evidence_pointer：Introduction 1.2 paragraph 4 sentence 1

### 55. Introduction 1.2 P4 S2

- order：55

- locator：Introduction 1.2 P4 S2

- paraphrase_cn：该机制需计算每个广告主的信息租金，它来自分配规则。

- move_code：CAUSAL_MECHANISM

- statement_status：author_inference

- why_here_cn：解释支付规则的计算来源。

- inherits_from_previous_cn：承接支付难题。

- changes_argument_state_cn：建立信息租金来源。

- sets_up_next_cn：为下一句说明序列变化作铺垫。

- failure_if_removed_cn：信息租金机制缺失。

- evidence_pointer：Introduction 1.2 paragraph 4 sentence 2

### 56. Introduction 1.2 P4 S3

- order：56

- locator：Introduction 1.2 P4 S3

- paraphrase_cn：随着广告出价增加，广告序列和分配给该广告的槽子集可能多次变化。

- move_code：CAUSAL_MECHANISM

- statement_status：author_inference

- why_here_cn：说明积分难以计算的原因。

- inherits_from_previous_cn：承接信息租金。

- changes_argument_state_cn：建立序列不稳定。

- sets_up_next_cn：为下一句说明无变化特征作铺垫。

- failure_if_removed_cn：积分计算困难的原因缺失。

- evidence_pointer：Introduction 1.2 paragraph 4 sentence 3

### 57. Introduction 1.2 P4 S4

- order：57

- locator：Introduction 1.2 P4 S4

- paraphrase_cn：没有关于广告序列何时变化的刻画。

- move_code：CAUSAL_MECHANISM

- statement_status：author_inference

- why_here_cn：强化计算障碍。

- inherits_from_previous_cn：承接序列变化。

- changes_argument_state_cn：明确无法预先刻画。

- sets_up_next_cn：为下一句总结支付规则难算作铺垫。

- failure_if_removed_cn：计算障碍不充分。

- evidence_pointer：Introduction 1.2 paragraph 4 sentence 4

### 58. Introduction 1.2 P4 S5

- order：58

- locator：Introduction 1.2 P4 S5

- paraphrase_cn：这使得OPT-IR支付规则难以计算，构成实现挑战。

- move_code：LIMITATION

- statement_status：author_inference

- why_here_cn：总结支付难题。

- inherits_from_previous_cn：承接序列刻画缺失。

- changes_argument_state_cn：推出实现挑战。

- sets_up_next_cn：为下一句提出随机化支付作铺垫。

- failure_if_removed_cn：实现挑战总结缺失。

- evidence_pointer：Introduction 1.2 paragraph 4 sentence 5

### 59. Introduction 1.2 P5 S1

- order：59

- locator：Introduction 1.2 P5 S1

- paraphrase_cn：作为补救，我们开发了一种既最优又易于实施的随机化支付规则。

- move_code：DESIGN_FEATURE

- statement_status：design_decision

- why_here_cn：提出核心设计创新。

- inherits_from_previous_cn：承接实现挑战。

- changes_argument_state_cn：引入RAND支付。

- sets_up_next_cn：为下一句说明CPC/CPM实施作铺垫。

- failure_if_removed_cn：随机化支付贡献缺失。

- evidence_pointer：Introduction 1.2 paragraph 5 sentence 1

### 60. Introduction 1.2 P5 S2

- order：60

- locator：Introduction 1.2 P5 S2

- paraphrase_cn：该支付可在CPC和CPM两种流行格式下实施。

- move_code：DESIGN_FEATURE

- statement_status：design_decision

- why_here_cn：强调支付的实际可用性。

- inherits_from_previous_cn：承接RAND支付。

- changes_argument_state_cn：建立格式兼容性。

- sets_up_next_cn：为下一句说明OPT-MB支付可计算作铺垫。

- failure_if_removed_cn：CPC/CPM兼容性缺失。

- evidence_pointer：Introduction 1.2 paragraph 5 sentence 2

### 61. Introduction 1.2 P5 S3

- order：61

- locator：Introduction 1.2 P5 S3

- paraphrase_cn：OPT-MB的支付规则易于计算。

- move_code：DESIGN_FEATURE

- statement_status：author_inference

- why_here_cn：对比两种机制的支付可计算性。

- inherits_from_previous_cn：承接OPT-IR支付难题。

- changes_argument_state_cn：建立OPT-MB支付优势。

- sets_up_next_cn：为下一句解释原因作铺垫。

- failure_if_removed_cn：OPT-MB支付简化缺失。

- evidence_pointer：Introduction 1.2 paragraph 5 sentence 3

### 62. Introduction 1.2 P5 S4

- order：62

- locator：Introduction 1.2 P5 S4

- paraphrase_cn：这一简化源于OPT-MB无需计算信息租金；它给每个广告主恰好传统机制的期望效用，可预先计算。

- move_code：CAUSAL_MECHANISM

- statement_status：author_inference

- why_here_cn：解释OPT-MB支付为何简单。

- inherits_from_previous_cn：承接OPT-MB支付。

- changes_argument_state_cn：说明固定BASE效用转移机制。

- sets_up_next_cn：为下一句说明支付公式作铺垫。

- failure_if_removed_cn：OPT-MB支付简单的机制缺失。

- evidence_pointer：Introduction 1.2 paragraph 5 sentence 4

### 63. Introduction 1.2 P5 S5

- order：63

- locator：Introduction 1.2 P5 S5

- paraphrase_cn：因此OPT-MB中每个广告主支付其从分配中所得价值减去传统机制的期望效用。

- move_code：DESIGN_FEATURE

- statement_status：author_inference

- why_here_cn：给出OPT-MB支付的具体形式。

- inherits_from_previous_cn：承接支付简化原因。

- changes_argument_state_cn：定义OPT-MB支付。

- sets_up_next_cn：为下一句讨论福利影响作铺垫。

- failure_if_removed_cn：OPT-MB支付公式缺失。

- evidence_pointer：Introduction 1.2 paragraph 5 sentence 5

### 64. Introduction 1.2 P6 S1

- order：64

- locator：Introduction 1.2 P6 S1

- paraphrase_cn：我们也分析OPT-IR和OPT-MB对交易所和广告主的福利影响。

- move_code：STUDY_OVERVIEW

- statement_status：author_inference

- why_here_cn：引入福利分析。

- inherits_from_previous_cn：承接机制定义。

- changes_argument_state_cn：建立福利分析范围。

- sets_up_next_cn：为下一句说明交易所受益作铺垫。

- failure_if_removed_cn：福利分析预告缺失。

- evidence_pointer：Introduction 1.2 paragraph 6 sentence 1

### 65. Introduction 1.2 P6 S2

- order：65

- locator：Introduction 1.2 P6 S2

- paraphrase_cn：因为两种设置中传统机制是可行解，交易所从最优机制中相对传统机制受益是清楚的。

- move_code：RESULT

- statement_status：author_inference

- why_here_cn：证明交易所受益。

- inherits_from_previous_cn：承接可行性论证。

- changes_argument_state_cn：建立交易所收益优势。

- sets_up_next_cn：为下一句说明广告主可能受损作铺垫。

- failure_if_removed_cn：交易所受益论证缺失。

- evidence_pointer：Introduction 1.2 paragraph 6 sentence 2

### 66. Introduction 1.2 P6 S3

- order：66

- locator：Introduction 1.2 P6 S3

- paraphrase_cn：但广告主在OPT-IR下相对传统机制可能更差。

- move_code：RESULT

- statement_status：author_inference

- why_here_cn：指出广告主福利风险。

- inherits_from_previous_cn：承接交易所受益。

- changes_argument_state_cn：建立广告主受损可能性。

- sets_up_next_cn：为下一句说明两种可能性作铺垫。

- failure_if_removed_cn：广告主受损风险缺失。

- evidence_pointer：Introduction 1.2 paragraph 6 sentence 3

### 67. Introduction 1.2 P6 S4

- order：67

- locator：Introduction 1.2 P6 S4

- paraphrase_cn：我们解析展示两种可能性：OPT-IR使广告主受益（win-win）和受损（win-lose）。

- move_code：RESULT

- statement_status：empirical_result

- why_here_cn：报告福利分析的关键结果。

- inherits_from_previous_cn：承接广告主受损风险。

- changes_argument_state_cn：建立win-win/win-lose。

- sets_up_next_cn：为下一句说明OPT-MB保障作铺垫。

- failure_if_removed_cn：福利可能性结果缺失。

- evidence_pointer：Introduction 1.2 paragraph 6 sentence 4

### 68. Introduction 1.2 P6 S5

- order：68

- locator：Introduction 1.2 P6 S5

- paraphrase_cn：相反，OPT-MB下每个广告主长期效用至少与传统机制一样。

- move_code：RESULT

- statement_status：author_inference

- why_here_cn：指出OPT-MB的福利保障。

- inherits_from_previous_cn：承接win-lose。

- changes_argument_state_cn：建立互惠机制。

- sets_up_next_cn：为下一句介绍数值研究作铺垫。

- failure_if_removed_cn：OPT-MB福利保证缺失。

- evidence_pointer：Introduction 1.2 paragraph 6 sentence 5

### 69. Introduction 1.2 P7 S1

- order：69

- locator：Introduction 1.2 P7 S1

- paraphrase_cn：最后我们在一组示例实例上检验OPT-IR和OPT-MB性能并对比相对优势。

- move_code：STUDY_OVERVIEW

- statement_status：author_inference

- why_here_cn：引入数值研究。

- inherits_from_previous_cn：承接机制比较。

- changes_argument_state_cn：建立数值研究范围。

- sets_up_next_cn：为下一句报告收益增益作铺垫。

- failure_if_removed_cn：数值研究预告缺失。

- evidence_pointer：Introduction 1.2 paragraph 7 sentence 1

### 70. Introduction 1.2 P7 S2

- order：70

- locator：Introduction 1.2 P7 S2

- paraphrase_cn：主要信息是两种机制都能有效消除传统机制的低效——交易所可获益7%到33%，广告异构性越强收益越大。

- move_code：RESULT

- statement_status：empirical_result

- why_here_cn：报告数值研究的关键结果。

- inherits_from_previous_cn：承接数值研究。

- changes_argument_state_cn：量化机制收益。

- sets_up_next_cn：为下一句说明社会福祉作铺垫。

- failure_if_removed_cn：数值结果缺失。

- evidence_pointer：Introduction 1.2 paragraph 7 sentence 2

### 71. Introduction 1.2 P7 S3

- order：71

- locator：Introduction 1.2 P7 S3

- paraphrase_cn：两种机制在社会福祉方面也有吸引力——OPT-IR接近一阶最优，OPT-MB实现一阶最优。

- move_code：RESULT

- statement_status：empirical_result

- why_here_cn：报告社会福祉结果。

- inherits_from_previous_cn：承接收益增益。

- changes_argument_state_cn：建立社会福祉贡献。

- sets_up_next_cn：为下一句介绍论文结构作铺垫。

- failure_if_removed_cn：社会福祉结果缺失。

- evidence_pointer：Introduction 1.2 paragraph 7 sentence 3

### 72. Introduction 1.3 P1

- order：72

- locator：Introduction 1.3 P1

- paraphrase_cn：列出论文结构：文献、初步、设置1、OPT-IR、SEQ、BASE、福利、OPT-MB、数值、结论。

- move_code：STUDY_OVERVIEW

- statement_status：author_inference

- why_here_cn：给出全文路线图。

- inherits_from_previous_cn：承接全部贡献预告。

- changes_argument_state_cn：建立读者导航。

- sets_up_next_cn：正文按此展开。

- failure_if_removed_cn：读者失去章节导航。

- evidence_pointer：Introduction 1.3 full paragraph

## 引言逐段图谱

### 1. Introduction P1

- order：1

- locator：Introduction P1

- opening_move_cn：移动发布商通过应用广告赚钱。

- development_move_cn：移动广告快速增长，并引用行业数据。

- pivot_move_cn：转向数字广告销售渠道。

- closing_move_cn：介绍传统广告网络合同。

- paragraph_job_cn：建立移动广告行业背景和传统销售模式。

### 2. Introduction P2

- order：2

- locator：Introduction P2

- opening_move_cn：引入广告交易所。

- development_move_cn：说明交易所对发布商和广告主的吸引力。

- pivot_move_cn：总结交易所增长。

- closing_move_cn：把交易所收益与发布商利益绑定。

- paragraph_job_cn：介绍研究对象广告交易所并说明其重要性。

### 3. Introduction P3

- order：3

- locator：Introduction P3

- opening_move_cn：聚焦移动设备展示广告。

- development_move_cn：说明移动应用内广告因会话长更可能从消除低效受益。

- pivot_move_cn：转向描述传统拍卖机制。

- closing_move_cn：预告用示例展示低效。

- paragraph_job_cn：从一般广告交易所收窄到移动应用内广告，并引出传统机制的低效问题。

### 4. Introduction 1.1 P1-P2

- order：4

- locator：Introduction 1.1 P1-P2

- opening_move_cn：构造两广告传统拍卖示例。

- development_move_cn：用图形说明B价值随时间变化、A在某时段价值更高。

- pivot_move_cn：指出B全程展示导致阴影区域配置低效。

- closing_move_cn：定义配置低效。

- paragraph_job_cn：用图形示例建立传统机制配置低效的现象。

### 5. Introduction 1.1 P3-P4

- order：5

- locator：Introduction 1.1 P3-P4

- opening_move_cn：提出分区印象想法。

- development_move_cn：说明如何分配多个广告到时间槽并给出示例。

- pivot_move_cn：指出没有技术障碍。

- closing_move_cn：提出设计有效机制的目标。

- paragraph_job_cn：提出分区印象的设计方向并排除技术障碍。

### 6. Introduction 1.1 P5

- order：6

- locator：Introduction 1.1 P5

- opening_move_cn：提出逐槽独立拍卖的自然想法。

- development_move_cn：指出其忽略未来槽影响的缺陷。

- pivot_move_cn：预告将分析该机制。

- closing_move_cn：宣称其收入可能显著低于最优机制。

- paragraph_job_cn：提出并排除直觉的SEQ机制候选。

### 7. Introduction 1.1 P6

- order：7

- locator：Introduction 1.1 P6

- opening_move_cn：转向广告主福利影响。

- development_move_cn：指出交易所受益但广告主是否受益不清楚。

- pivot_move_cn：提出若广告主受损可考虑替代机制。

- closing_move_cn：为后文互惠机制铺垫。

- paragraph_job_cn：引入广告主福利问题，为设置2作动机。

### 8. Introduction 1.1 P7

- order：8

- locator：Introduction 1.1 P7

- opening_move_cn：强调研究意义。

- development_move_cn：提出实时性和简单性要求。

- pivot_move_cn：总结所有研究目标。

- closing_move_cn：预告贡献列表。

- paragraph_job_cn：提炼研究目标并建立设计准则。

### 9. Introduction 1.2 P1

- order：9

- locator：Introduction 1.2 P1

- opening_move_cn：提出解决配置低效的方法。

- development_move_cn：描述分区印象框架。

- pivot_move_cn：无。

- closing_move_cn：为介绍两种设置作铺垫。

- paragraph_job_cn：列出第一项贡献：分区印象框架。

### 10. Introduction 1.2 P2

- order：10

- locator：Introduction 1.2 P2

- opening_move_cn：概述两种设置。

- development_move_cn：解释设置1和设置2的区别。

- pivot_move_cn：命名OPT-IR和OPT-MB。

- closing_move_cn：说明BASE可行。

- paragraph_job_cn：介绍两种设置和两个最优机制。

### 11. Introduction 1.2 P3

- order：11

- locator：Introduction 1.2 P3

- opening_move_cn：强调机制适合实时竞价。

- development_move_cn：描述交易所流程和150ms约束。

- pivot_move_cn：说明分配规则可高效计算。

- closing_move_cn：强调OPT-MB一阶最优。

- paragraph_job_cn：证明分配规则可实时实施。

### 12. Introduction 1.2 P4

- order：12

- locator：Introduction 1.2 P4

- opening_move_cn：指出OPT-IR支付难算。

- development_move_cn：解释信息租金和序列变化。

- pivot_move_cn：总结实现挑战。

- closing_move_cn：为随机化支付作铺垫。

- paragraph_job_cn：提出支付计算的核心难题。

### 13. Introduction 1.2 P5

- order：13

- locator：Introduction 1.2 P5

- opening_move_cn：提出随机化支付。

- development_move_cn：说明CPC/CPM实施和OPT-MB支付简单。

- pivot_move_cn：解释OPT-MB支付简化原因。

- closing_move_cn：给出OPT-MB支付公式。

- paragraph_job_cn：解决支付计算难题并介绍OPT-MB的支付设计。

### 14. Introduction 1.2 P6

- order：14

- locator：Introduction 1.2 P6

- opening_move_cn：引入福利分析。

- development_move_cn：证明交易所受益但广告主可能受损。

- pivot_move_cn：展示win-win和win-lose。

- closing_move_cn：说明OPT-MB保证广告主福利。

- paragraph_job_cn：报告福利分析结果并强调OPT-MB的保障。

### 15. Introduction 1.2 P7

- order：15

- locator：Introduction 1.2 P7

- opening_move_cn：引入数值研究。

- development_move_cn：报告7%-33%收益增益。

- pivot_move_cn：转向社会福祉。

- closing_move_cn：强调两种机制在社会福祉上的吸引力。

- paragraph_job_cn：报告数值研究结果和社会福祉贡献。

### 16. Introduction 1.3

- order：16

- locator：Introduction 1.3

- opening_move_cn：给出论文结构路标。

- development_move_cn：逐章列出。

- pivot_move_cn：无。

- closing_move_cn：为正文顺序作模板。

- paragraph_job_cn：提供全文导航。

## 理论到设计逐句图谱

### 1. Literature Review P1 S1

- order：1

- locator：Literature Review P1 S1

- paraphrase_cn：赞助搜索拍卖文献为电子生态中的广告拍卖设计了大量机制。

- move_code：PRIOR_KNOWLEDGE

- statement_status：prior_literature

- why_here_cn：建立已有文献上下文。

- inherits_from_previous_cn：无

- changes_argument_state_cn：引入空间槽拍卖文献。

- sets_up_next_cn：为后续区分空间槽和时间槽作铺垫。

- failure_if_removed_cn：已有文献基础缺失。

- evidence_pointer：Literature Review paragraph 1

### 2. Literature Review P1 bullets

- order：2

- locator：Literature Review P1 bullets

- paraphrase_cn：空间槽文献与本文有三点不同：动态程序、用户离开/点击依赖、广告可出现在多个槽。

- move_code：GAP

- statement_status：prior_literature

- why_here_cn：说明现有文献不能直接应用于本文。

- inherits_from_previous_cn：承接空间槽文献。

- changes_argument_state_cn：建立时间槽的新颖性。

- sets_up_next_cn：为后文展示机制设计差异作铺垫。

- failure_if_removed_cn：新颖性论证缺失。

- evidence_pointer：Literature Review paragraph 1 bullets

### 3. Literature Review P2

- order：3

- locator：Literature Review P2

- paraphrase_cn：Aumann等拍卖时间资源但目标是效率而非收益，且只允许连续区间分配，NP难。

- move_code：GAP

- statement_status：prior_literature

- why_here_cn：指出最接近的时间拍卖文献的局限。

- inherits_from_previous_cn：承接时间资源拍卖。

- changes_argument_state_cn：区分本文预设长度槽和收益目标。

- sets_up_next_cn：为后文说明本文可求解作铺垫。

- failure_if_removed_cn：时间拍卖文献比较缺失。

- evidence_pointer：Literature Review paragraph 2

### 4. Literature Review P3

- order：4

- locator：Literature Review P3

- paraphrase_cn：McAfee和Vassilvitskii描述设计交易所的实践原则，我们的机制受这些原则指导。

- move_code：PRIOR_KNOWLEDGE

- statement_status：prior_literature

- why_here_cn：把机制与行业实践原则连接。

- inherits_from_previous_cn：承接交易所设计文献。

- changes_argument_state_cn：建立设计准则来源。

- sets_up_next_cn：为后文说明机制遵循这些原则作铺垫。

- failure_if_removed_cn：实践设计原则连接缺失。

- evidence_pointer：Literature Review paragraph 3

### 5. Literature Review P4

- order：5

- locator：Literature Review P4

- paraphrase_cn：Sun等研究供给方广告网络固定契约下最优广告序列问题。

- move_code：PRIOR_KNOWLEDGE

- statement_status：prior_literature

- why_here_cn：介绍最接近的本文工作。

- inherits_from_previous_cn：承接广告调度文献。

- changes_argument_state_cn：建立与Sun等的比较对象。

- sets_up_next_cn：为下一句指出其局限作铺垫。

- failure_if_removed_cn：Sun等文献基础缺失。

- evidence_pointer：Literature Review paragraph 4

### 6. Literature Review P5 S1

- order：6

- locator：Literature Review P5 S1

- paraphrase_cn：本文与Sun等的上下文根本不同：广告交易所不知道广告主的每点击估值，存在信息不对称。

- move_code：GAP

- statement_status：prior_literature

- why_here_cn：建立本文的信息不对称问题。

- inherits_from_previous_cn：承接Sun等文献。

- changes_argument_state_cn：指出与Sun等的本质差异。

- sets_up_next_cn：为后文机制设计作铺垫。

- failure_if_removed_cn：与Sun等的差异缺失。

- evidence_pointer：Literature Review paragraph 5

### 7. Literature Review P5 S2

- order：7

- locator：Literature Review P5 S2

- paraphrase_cn：因此广告交易所必须设计机制（拍卖）来销售分区印象。

- move_code：GAP

- statement_status：author_inference

- why_here_cn：从信息不对称推出机制设计需求。

- inherits_from_previous_cn：承接信息不对称。

- changes_argument_state_cn：建立机制设计目标。

- sets_up_next_cn：为后文分配规则和支付规则作铺垫。

- failure_if_removed_cn：机制设计需求推导缺失。

- evidence_pointer：Literature Review paragraph 5 sentence 2

### 8. Literature Review P5 S3

- order：8

- locator：Literature Review P5 S3

- paraphrase_cn：最优机制设计涉及分配规则和支付规则。

- move_code：THEORY_INTRO

- statement_status：prior_literature

- why_here_cn：引入机制设计的两个组成部分。

- inherits_from_previous_cn：承接机制设计需求。

- changes_argument_state_cn：定义机制组成。

- sets_up_next_cn：为后文IC/IR正式化作铺垫。

- failure_if_removed_cn：机制组成定义缺失。

- evidence_pointer：Literature Review paragraph 5 sentence 3

### 9. Literature Review P5 S4

- order：9

- locator：Literature Review P5 S4

- paraphrase_cn：Sun等只关注最优日程，完全忽略广告主激励。

- move_code：GAP

- statement_status：prior_literature

- why_here_cn：强调本文与Sun等的激励差异。

- inherits_from_previous_cn：承接机制组成。

- changes_argument_state_cn：明确Sun等的局限。

- sets_up_next_cn：为后文引入激励兼容作铺垫。

- failure_if_removed_cn：激励差异缺失。

- evidence_pointer：Literature Review paragraph 5 sentence 4

### 10. Literature Review P5 S5

- order：10

- locator：Literature Review P5 S5

- paraphrase_cn：本文的随机化支付在数字广告文献中是新颖的，适合CPM/CPC实时实施。

- move_code：CONTRIBUTION

- statement_status：author_inference

- why_here_cn：预告核心设计创新。

- inherits_from_previous_cn：承接支付挑战。

- changes_argument_state_cn：建立随机化支付的贡献。

- sets_up_next_cn：为后文Section 4.2作铺垫。

- failure_if_removed_cn：随机化支付贡献预告缺失。

- evidence_pointer：Literature Review paragraph 5 sentence 5

### 11. Section 3 first list

- order：11

- locator：Section 3 first list

- paraphrase_cn：定义印象由N个等长时间槽组成，每槽点击概率p_{a,n}，用户以概率λ停留且点击广告后会话结束。

- move_code：THEORY_INTRO

- statement_status：theory_claim

- why_here_cn：建立模型基础变量。

- inherits_from_previous_cn：无

- changes_argument_state_cn：定义模型实体。

- sets_up_next_cn：为后续机制定义和动态规划作铺垫。

- failure_if_removed_cn：模型基础变量缺失。

- evidence_pointer：Section 3 first list

### 12. Section 3 advertisers paragraph

- order：12

- locator：Section 3 advertisers paragraph

- paraphrase_cn：每个广告主有私人每点击估值r_a，独立同分布，已知分布；点击概率共同已知。

- move_code：THEORY_INTRO

- statement_status：theory_claim

- why_here_cn：引入信息不对称模型结构。

- inherits_from_previous_cn：承接基础变量。

- changes_argument_state_cn：建立私人信息结构。

- sets_up_next_cn：为IC/IR约束作铺垫。

- failure_if_removed_cn：私人信息结构缺失。

- evidence_pointer：Section 3 advertisers paragraph

### 13. Section 3 click probabilities paragraph

- order：13

- locator：Section 3 click probabilities paragraph

- paraphrase_cn：共同知识假设基于重复交互学习；即使点击概率私有，机制仍保持IC，只是最优性需要共同知识。

- move_code：METHOD_JUSTIFICATION

- statement_status：author_inference

- why_here_cn：为点击概率共同知识假设辩护。

- inherits_from_previous_cn：承接信息结构。

- changes_argument_state_cn：界定假设的角色。

- sets_up_next_cn：避免读者认为机制适用范围太窄。

- failure_if_removed_cn：假设合理性论证缺失。

- evidence_pointer：Section 3 click probabilities paragraph

### 14. Section 3.1 regularity assumption

- order：14

- locator：Section 3.1 regularity assumption

- paraphrase_cn：正则分布假设保证虚拟价值单调且风险率非降。

- move_code：THEORY_PROPOSITION

- statement_status：theory_claim

- why_here_cn：为Myerson最优拍卖可行提供条件。

- inherits_from_previous_cn：承接估值分布。

- changes_argument_state_cn：建立虚拟价值单调性。

- sets_up_next_cn：使Theorem 1的单调性证明成立。

- failure_if_removed_cn：最优性证明条件缺失。

- evidence_pointer：Section 3.1 regularity assumption

### 15. Section 3.1 revelation principle

- order：15

- locator：Section 3.1 revelation principle

- paraphrase_cn：利用revelation principle，可无损失地只考虑IC/IR直接机制。

- move_code：THEORY_INTRO

- statement_status：prior_literature

- why_here_cn：限定机制搜索空间。

- inherits_from_previous_cn：承接机制设计理论。

- changes_argument_state_cn：把问题限制到直接机制。

- sets_up_next_cn：为定义机制μ和IC/IR约束提供理论基础。

- failure_if_removed_cn：直接机制限制缺失。

- evidence_pointer：Section 3.1 revelation principle

### 16. Section 3.1 direct mechanism definition

- order：16

- locator：Section 3.1 direct mechanism definition

- paraphrase_cn：直接机制由分配规则和支付规则组成，并定义广告a在所有时段的期望点击概率Θ_a。

- move_code：THEORY_INTRO

- statement_status：theory_claim

- why_here_cn：把抽象机制落实到广告序列和支付函数。

- inherits_from_previous_cn：承接直接机制概念。

- changes_argument_state_cn：定义机制组成。

- sets_up_next_cn：用于写出IC/IR数学约束。

- failure_if_removed_cn：机制形式定义缺失。

- evidence_pointer：Section 3.1 mechanism definition

### 17. Section 3.1 IC/IR formulas

- order：17

- locator：Section 3.1 IC/IR formulas

- paraphrase_cn：IC约束要求每个广告主真实报告估值是最优反应，IR约束要求参与拍卖的期望收益非负。

- move_code：THEORY_PROPOSITION

- statement_status：theory_claim

- why_here_cn：把激励约束正式化。

- inherits_from_previous_cn：承接期望点击概率定义。

- changes_argument_state_cn：建立IC/IR约束。

- sets_up_next_cn：是P^IR问题的约束条件。

- failure_if_removed_cn：激励约束缺失。

- evidence_pointer：Section 3.1 IC/IR equations

### 18. Section 3.2

- order：18

- locator：Section 3.2

- paraphrase_cn：交易所目标是在IC/IR约束下最大化所有广告主的期望支付之和。

- move_code：RQ_OR_OBJECTIVE

- statement_status：theory_claim

- why_here_cn：正式提出P^IR问题。

- inherits_from_previous_cn：承接IC/IR约束。

- changes_argument_state_cn：建立目标函数。

- sets_up_next_cn：后续最优机制求解的目标函数。

- failure_if_removed_cn：优化问题缺失。

- evidence_pointer：Section 3.2

### 19. Section 3.3 VCG paragraph

- order：19

- locator：Section 3.3 VCG paragraph

- paraphrase_cn：社会福利被定义为所有广告主期望价值之和，VCG机制实现IC/IR和社会福利最大化。

- move_code：THEORY_INTRO

- statement_status：prior_literature

- why_here_cn：引入效率机制作为参照。

- inherits_from_previous_cn：承接P^IR框架。

- changes_argument_state_cn：建立VCG机制。

- sets_up_next_cn：后文OPT-IR用虚拟价值替代真实估值，OPT-MB用VCG分配。

- failure_if_removed_cn：VCG参照缺失。

- evidence_pointer：Section 3.3

### 20. Section 4 Theorem 1

- order：20

- locator：Section 4 Theorem 1

- paraphrase_cn：用虚拟价值加权的总点击概率最大化分配，并用Myerson支付公式得到OPT-IR机制，它是P^IR最优解。

- move_code：THEORY_PROPOSITION

- statement_status：theory_claim

- why_here_cn：给出第一设置的核心理论结果。

- inherits_from_previous_cn：承接虚拟价值定义和IC/IR约束。

- changes_argument_state_cn：建立OPT-IR最优性。

- sets_up_next_cn：后续实现和比较都基于这一机制。

- failure_if_removed_cn：最优机制缺失。

- evidence_pointer：Section 4 Theorem 1

### 21. Section 4 proof

- order：21

- locator：Section 4 proof

- paraphrase_cn：为证明最优性，只需验证每个广告主的期望点击概率在虚拟价值单调时关于出价单调。

- move_code：METHOD_JUSTIFICATION

- statement_status：author_inference

- why_here_cn：说明证明路径。

- inherits_from_previous_cn：承接Theorem 1。

- changes_argument_state_cn：把证明简化为单调性。

- sets_up_next_cn：证明的核心是单调性。

- failure_if_removed_cn：证明路径不清晰。

- evidence_pointer：Section 4 proof

### 22. Section 4.1

- order：22

- locator：Section 4.1

- paraphrase_cn：OPT-IR分配是VCG分配把估值换成虚拟价值后的结果，可通过O(AN)动态规划实现。

- move_code：DESIGN_FEATURE

- statement_status：design_decision

- why_here_cn：把理论最优转化为可计算的算法。

- inherits_from_previous_cn：承接Theorems和VCG DP。

- changes_argument_state_cn：建立分配可计算性。

- sets_up_next_cn：满足实时性要求。

- failure_if_removed_cn：分配算法缺失。

- evidence_pointer：Section 4.1

### 23. Section 4.2

- order：23

- locator：Section 4.2

- paraphrase_cn：支付规则需要计算积分，但广告序列随出价变化多次改变且无规律，只有离散化近似，成本极高。

- move_code：LIMITATION

- statement_status：author_inference

- why_here_cn：突出现实实施障碍。

- inherits_from_previous_cn：承接OPT-IR支付规则。

- changes_argument_state_cn：建立支付计算挑战。

- sets_up_next_cn：为随机支付引入提供动机。

- failure_if_removed_cn：支付计算挑战缺失。

- evidence_pointer：Section 4.2

### 24. Section 4.2.1

- order：24

- locator：Section 4.2.1

- paraphrase_cn：由于广告主每天参与大量拍卖，可从U(0,r_a)随机抽取u_a，把积分替换为期望，构造RAND支付。

- move_code：DESIGN_FEATURE

- statement_status：design_decision

- why_here_cn：提出随机化支付这一关键设计。

- inherits_from_previous_cn：承接积分难以计算。

- changes_argument_state_cn：定义RAND支付。

- sets_up_next_cn：证明期望收益等价且保持IC/IR。

- failure_if_removed_cn：随机支付设计缺失。

- evidence_pointer：Section 4.2.1

### 25. Section 4.2.1 P2

- order：25

- locator：Section 4.2.1 P2

- paraphrase_cn：RAND支付的期望等于OPT-IR支付，且因为分配函数单调，随机样本不超过真实出价，IR也保持。

- move_code：THEORY_PROPOSITION

- statement_status：theory_claim

- why_here_cn：验证新支付规则没有破坏激励。

- inherits_from_previous_cn：承接RAND支付。

- changes_argument_state_cn：建立RAND的IC/IR保持性。

- sets_up_next_cn：使随机支付成为合法最优机制。

- failure_if_removed_cn：RAND激励性质缺失。

- evidence_pointer：Section 4.2.1 equations

### 26. Section 4.2.2

- order：26

- locator：Section 4.2.2

- paraphrase_cn：可把RAND支付转化为CPC：只在点击发生时收取M/Θ，使期望支付不变。

- move_code：DESIGN_FEATURE

- statement_status：design_decision

- why_here_cn：连接主流定价格式。

- inherits_from_previous_cn：承接RAND支付。

- changes_argument_state_cn：建立CPC实施。

- sets_up_next_cn：说明机制对实践友好。

- failure_if_removed_cn：CPC实施缺失。

- evidence_pointer：Section 4.2.2

### 27. Section 4.2.3

- order：27

- locator：Section 4.2.3

- paraphrase_cn：也可转换为CPM：按槽位展示收费，若槽未实现则不收，概率加权使期望支付等于RAND支付。

- move_code：DESIGN_FEATURE

- statement_status：design_decision

- why_here_cn：提供第二种主流格式的实现。

- inherits_from_previous_cn：承接RAND支付。

- changes_argument_state_cn：建立CPM实施。

- sets_up_next_cn：强调OPT-IR可在行业常见格式下运行。

- failure_if_removed_cn：CPM实施缺失。

- evidence_pointer：Section 4.2.3

## 制品设计理由逐句图谱

### 1. Section 4.1 P1

- order：1

- locator：Section 4.1 P1

- paraphrase_cn：OPT-IR分配是VCG分配把估值换成虚拟价值后的结果，可用O(AN)动态规划求解。

- move_code：ARTIFACT_RATIONALE

- statement_status：design_decision

- why_here_cn：说明分配规则的构造思路和计算性质。

- inherits_from_previous_cn：承接Theorem 1。

- changes_argument_state_cn：展示分配可实现性。

- sets_up_next_cn：为下一步支付实现挑战作铺垫。

- failure_if_removed_cn：分配规则可计算性论证缺失。

- evidence_pointer：Section 4.1 P1

### 2. Section 4.2 P1

- order：2

- locator：Section 4.2 P1

- paraphrase_cn：支付规则第二项积分涉及Θ_a^{OPT-IR}(t_a,r_{-a})的计算，需要所有可能出价t_a。

- move_code：ARTIFACT_RATIONALE

- statement_status：author_inference

- why_here_cn：指出支付规则的实现瓶颈。

- inherits_from_previous_cn：承接OPT-IR支付规则。

- changes_argument_state_cn：建立积分计算困难。

- sets_up_next_cn：为随机化支付作铺垫。

- failure_if_removed_cn：支付困难论证缺失。

- evidence_pointer：Section 4.2 P1

### 3. Section 4.2 Tables 2-3

- order：3

- locator：Section 4.2 Tables 2-3

- paraphrase_cn：用X、Y两广告三槽例子说明序列随出价多次跳变，无法轻易刻画。

- move_code：ARTIFACT_RATIONALE

- statement_status：empirical_result

- why_here_cn：用具体例子增强支付困难的说服力。

- inherits_from_previous_cn：承接积分计算困难。

- changes_argument_state_cn：证明序列跳变。

- sets_up_next_cn：为随机化支付必要性作铺垫。

- failure_if_removed_cn：支付困难的具体证据缺失。

- evidence_pointer：Section 4.2 Tables 2-3

### 4. Section 4.2.1 P1

- order：4

- locator：Section 4.2.1 P1

- paraphrase_cn：积分等于r_a乘以Θ_a^{OPT-IR}(u_a,r_{-a})在u_a~U(0,r_a)下的期望。

- move_code：ARTIFACT_RATIONALE

- statement_status：theory_claim

- why_here_cn：给出随机化支付的理论基础。

- inherits_from_previous_cn：承接积分难以计算。

- changes_argument_state_cn：把积分转化为期望。

- sets_up_next_cn：为定义RAND支付作铺垫。

- failure_if_removed_cn：随机化支付理论依据缺失。

- evidence_pointer：Section 4.2.1 equations

### 5. Section 4.2.1 P2

- order：5

- locator：Section 4.2.1 P2

- paraphrase_cn：RAND支付的期望等于OPT-IR支付，且IC和IR都保持。

- move_code：ARTIFACT_RATIONALE

- statement_status：theory_claim

- why_here_cn：证明RAND支付保持机制性质。

- inherits_from_previous_cn：承接RAND定义。

- changes_argument_state_cn：建立RAND最优性。

- sets_up_next_cn：为CPC/CPM实施作铺垫。

- failure_if_removed_cn：RAND性质证明缺失。

- evidence_pointer：Section 4.2.1 P2

### 6. Section 4.2.2 P1

- order：6

- locator：Section 4.2.2 P1

- paraphrase_cn：CPC实施需要广告主在点击发生时支付M^{RAND}/Θ，期望支付等于M^{RAND}。

- move_code：ARTIFACT_RATIONALE

- statement_status：design_decision

- why_here_cn：说明CPC格式的构造。

- inherits_from_previous_cn：承接RAND支付。

- changes_argument_state_cn：建立CPC实施。

- sets_up_next_cn：为CPM实施作铺垫。

- failure_if_removed_cn：CPC实施缺失。

- evidence_pointer：Section 4.2.2 P1

### 7. Section 4.2.3 P1

- order：7

- locator：Section 4.2.3 P1

- paraphrase_cn：CPM实施需要按槽收费，若槽未实现则不收；与传统CPM不同，多个广告主可能付费。

- move_code：ARTIFACT_RATIONALE

- statement_status：design_decision

- why_here_cn：说明CPM实施的构造差异。

- inherits_from_previous_cn：承接RAND支付。

- changes_argument_state_cn：建立CPM实施。

- sets_up_next_cn：为后文机制比较作铺垫。

- failure_if_removed_cn：CPM实施缺失。

- evidence_pointer：Section 4.2.3 P1

### 8. Section 5 SEQ definition

- order：8

- locator：Section 5 SEQ definition

- paraphrase_cn：SEQ机制把N个槽当作N次独立拍卖，每槽用Myerson单物品最优拍卖。

- move_code：ARTIFACT_RATIONALE

- statement_status：design_decision

- why_here_cn：给出直觉候选机制的定义。

- inherits_from_previous_cn：承接低效问题。

- changes_argument_state_cn：定义SEQ机制。

- sets_up_next_cn：为后文比较SEQ与OPT-IR作铺垫。

- failure_if_removed_cn：SEQ机制定义缺失。

- evidence_pointer：Section 5 first paragraph

### 9. Section 5 last paragraph

- order：9

- locator：Section 5 last paragraph

- paraphrase_cn：SEQ不要求改变现有技术设施，容易实施，但期望收入可能显著低于OPT-IR。

- move_code：ARTIFACT_RATIONALE

- statement_status：author_inference

- why_here_cn：总结SEQ的优缺点。

- inherits_from_previous_cn：承接SEQ定义。

- changes_argument_state_cn：建立SEQ的次优性。

- sets_up_next_cn：为下一节详细比较作铺垫。

- failure_if_removed_cn：SEQ优缺点总结缺失。

- evidence_pointer：Section 5 last paragraph

### 10. Section 7 Theorem 4

- order：10

- locator：Section 7 Theorem 4

- paraphrase_cn：最优BASE机制选择虚拟价值与总点击概率乘积最大的广告，并收取最小必要价格。

- move_code：ARTIFACT_RATIONALE

- statement_status：theory_claim

- why_here_cn：给出BASE机制的解析解。

- inherits_from_previous_cn：承接P^BASE。

- changes_argument_state_cn：定义BASE机制。

- sets_up_next_cn：作为后面收益和福利比较的BASE定义。

- failure_if_removed_cn：BASE机制解缺失。

- evidence_pointer：Section 7 Theorem 4

### 11. Section 9 before Theorem 5

- order：11

- locator：Section 9 before Theorem 5

- paraphrase_cn：把BASE效用约束求和后，得到交易所收益的上界等于VCG社会福利减去各广告主BASE效用之和。

- move_code：ARTIFACT_RATIONALE

- statement_status：theory_claim

- why_here_cn：给出OPT-MB机制的理论上界。

- inherits_from_previous_cn：承接VCG效率性质。

- changes_argument_state_cn：建立上界论证。

- sets_up_next_cn：构造OPT-MB达到该上界。

- failure_if_removed_cn：OPT-MB上界缺失。

- evidence_pointer：Section 9 upper bound argument

### 12. Section 9 Theorem 5

- order：12

- locator：Section 9 Theorem 5

- paraphrase_cn：OPT-MB采用VCG分配，支付为VCG支付加期望VCG效用减期望BASE效用，达到P^MB上界。

- move_code：ARTIFACT_RATIONALE

- statement_status：design_decision

- why_here_cn：给出互惠最优机制的构造。

- inherits_from_previous_cn：承接上界论证。

- changes_argument_state_cn：定义OPT-MB机制。

- sets_up_next_cn：证明其最优性和可实现性。

- failure_if_removed_cn：OPT-MB机制构造缺失。

- evidence_pointer：Section 9 Theorem 5

### 13. Section 9 salient features

- order：13

- locator：Section 9 salient features

- paraphrase_cn：OPT-MB分配一阶最优，支付等于价值减期望BASE效用，广告主长期恰得BASE效用。

- move_code：ARTIFACT_RATIONALE

- statement_status：theory_claim

- why_here_cn：提炼机制的主要性质。

- inherits_from_previous_cn：承接Theorem 5。

- changes_argument_state_cn：建立OPT-MB福利分配。

- sets_up_next_cn：为数值结果解释why η≈0。

- failure_if_removed_cn：OPT-MB机制性质缺失。

- evidence_pointer：Section 9 salient features

## Study开头、过渡与收束图谱

### 1. Section 6 opening P1

- order：1

- locator：Section 6 opening P1

- paraphrase_cn：本节开始用两广告两槽简单例子说明SEQ的劣性能。

- move_code：STUDY_OPENING

- statement_status：method_decision

- why_here_cn：进入SEQ与OPT-IR比较。

- inherits_from_previous_cn：承接Section 5 SEQ定义。

- changes_argument_state_cn：建立比较研究。

- sets_up_next_cn：为Example 1作铺垫。

- failure_if_removed_cn：SEQ比较研究无引言。

- evidence_pointer：Section 6 opening paragraph

### 2. Section 6 Example 1

- order：2

- locator：Section 6 Example 1

- paraphrase_cn：在两广告两槽极端例子中，SEQ收入约仅为OPT-IR的一半。

- move_code：EMPIRICAL_RESULT

- statement_status：empirical_result

- why_here_cn：用反例直接证明SEQ不最优。

- inherits_from_previous_cn：承接比较研究。

- changes_argument_state_cn：建立SEQ次优。

- sets_up_next_cn：为寻找次优条件提供直觉。

- failure_if_removed_cn：SEQ次优反例缺失。

- evidence_pointer：Section 6 Example 1

### 3. Section 6.2 Theorem 2

- order：3

- locator：Section 6.2 Theorem 2

- paraphrase_cn：在估值与首槽点击概率负相关、点击概率常数衰减、W值函数满足一定不等式时，OPT-IR严格优于SEQ。

- move_code：BOUNDARY_CONDITION

- statement_status：theory_claim

- why_here_cn：给出SEQ次优的充分条件。

- inherits_from_previous_cn：承接Example 1观察。

- changes_argument_state_cn：建立次优充分条件。

- sets_up_next_cn：说明并非所有负相关都导致次优。

- failure_if_removed_cn：次优充分条件缺失。

- evidence_pointer：Section 6.2 Theorem 2

### 4. Section 6.3 Example 3

- order：4

- locator：Section 6.3 Example 3

- paraphrase_cn：即使估值与点击概率不满足负相关，SEQ仍可能次优。

- move_code：ROBUSTNESS_OR_BOUNDARY_TEST

- statement_status：empirical_result

- why_here_cn：扩大次优现象的适用范围。

- inherits_from_previous_cn：承接Theorem 2。

- changes_argument_state_cn：说明Theorem 2条件非必要。

- sets_up_next_cn：推动读者接受SEQ整体不稳健。

- failure_if_removed_cn：次优适用范围不完整。

- evidence_pointer：Section 6.3 Example 3

### 5. Section 6.4 Theorem 3

- order：5

- locator：Section 6.4 Theorem 3

- paraphrase_cn：如果高估值广告在每个槽都有较高点击概率，则SEQ最优。

- move_code：BOUNDARY_CONDITION

- statement_status：theory_claim

- why_here_cn：给出SEQ最优的充分条件。

- inherits_from_previous_cn：承接SEQ比较。

- changes_argument_state_cn：界定SEQ有效场景。

- sets_up_next_cn：数值实验中偏离同序条件导致收益下降。

- failure_if_removed_cn：SEQ最优条件缺失。

- evidence_pointer：Section 6.4 Theorem 3

### 6. Section 6.5 Table 8

- order：6

- locator：Section 6.5 Table 8

- paraphrase_cn：数值显示随着负相关程度增加，SEQ相对OPT-IR收入比从100%降到约75%。

- move_code：EMPIRICAL_RESULT

- statement_status：empirical_result

- why_here_cn：用量化证据支持SEQ次优。

- inherits_from_previous_cn：承接Theorem 3。

- changes_argument_state_cn：量化次优程度。

- sets_up_next_cn：转入BASE机制研究。

- failure_if_removed_cn：SEQ次优量化证据缺失。

- evidence_pointer：Section 6.5 Table 8

### 7. Section 7 opening

- order：7

- locator：Section 7 opening

- paraphrase_cn：当前移动广告交易所使用传统机制即BASE机制：胜者广告在整个生命周期展示。

- move_code：STUDY_OPENING

- statement_status：fact

- why_here_cn：引入现状基准机制。

- inherits_from_previous_cn：承接SEQ比较。

- changes_argument_state_cn：定义BASE机制。

- sets_up_next_cn：为P^BASE形式化作铺垫。

- failure_if_removed_cn：BASE机制引入缺失。

- evidence_pointer：Section 7 opening

### 8. Section 8 opening

- order：8

- locator：Section 8 opening

- paraphrase_cn：因为BASE是P^IR的可行解，OPT-IR收入总不低于BASE；但广告主可能更好或更差。

- move_code：STUDY_OPENING

- statement_status：theory_claim

- why_here_cn：开启OPT-IR与BASE的福利比较。

- inherits_from_previous_cn：承接Theorem 1和4。

- changes_argument_state_cn：建立收益简单比较和福利不确定性。

- sets_up_next_cn：定义win-win和win-lose。

- failure_if_removed_cn：福利比较引言缺失。

- evidence_pointer：Section 8 opening paragraph

### 9. Section 8.1 Table 9

- order：9

- locator：Section 8.1 Table 9

- paraphrase_cn：在win-win场景，两个广告主效用均提高75%，交易所收入提高18.75%。

- move_code：EMPIRICAL_RESULT

- statement_status：empirical_result

- why_here_cn：证明win-win可能性。

- inherits_from_previous_cn：承接福利比较。

- changes_argument_state_cn：建立win-win。

- sets_up_next_cn：为win-lose作对比。

- failure_if_removed_cn：win-win证据缺失。

- evidence_pointer：Section 8.1 Table 9

### 10. Section 8.2 Table 10

- order：10

- locator：Section 8.2 Table 10

- paraphrase_cn：在win-lose场景，广告主X效用下降100q%，交易所收入上升100q%。

- move_code：EMPIRICAL_RESULT

- statement_status：empirical_result

- why_here_cn：证明广告主可能受损。

- inherits_from_previous_cn：承接win-win。

- changes_argument_state_cn：建立win-lose。

- sets_up_next_cn：为互惠机制提供动机。

- failure_if_removed_cn：win-lose证据缺失。

- evidence_pointer：Section 8.2 Table 10

### 11. Section 8 final paragraph

- order：11

- locator：Section 8 final paragraph

- paraphrase_cn：存在win-win和win-lose两种可能，因此值得设计保证双方长期至少与BASE一样好的机制。

- move_code：TRANSITION

- statement_status：author_inference

- why_here_cn：把前文比较过渡到新问题。

- inherits_from_previous_cn：承接Tables 9-10。

- changes_argument_state_cn：提出互惠机制目标。

- sets_up_next_cn：为Section 9的P^MB设置作铺垫。

- failure_if_removed_cn：互惠机制过渡缺失。

- evidence_pointer：Section 8 final paragraph

### 12. Section 9 opening

- order：12

- locator：Section 9 opening

- paraphrase_cn：因为广告主每天对成千上万的印象竞价，可考虑长期BASE效用约束的机制设计问题。

- move_code：STUDY_OPENING

- statement_status：author_inference

- why_here_cn：开启设置2的机制设计。

- inherits_from_previous_cn：承接互惠机制动机。

- changes_argument_state_cn：定义P^MB。

- sets_up_next_cn：为OPT-MB机制定义目标。

- failure_if_removed_cn：P^MB引入缺失。

- evidence_pointer：Section 9 problem (P^MB)

### 13. Section 9.1 Tables 11-12

- order：13

- locator：Section 9.1 Tables 11-12

- paraphrase_cn：在win-win场景OPT-MB给交易所159.38%收益增量高于OPT-IR；在win-lose场景OPT-MB保住广告主效用但交易所收益涨幅较小。

- move_code：EMPIRICAL_RESULT

- statement_status：empirical_result

- why_here_cn：展示两种机制的福利权衡。

- inherits_from_previous_cn：承接OPT-MB设计。

- changes_argument_state_cn：建立机制选择权衡。

- sets_up_next_cn：帮助用户理解何时选择OPT-IR或OPT-MB。

- failure_if_removed_cn：机制权衡证据缺失。

- evidence_pointer：Section 9.1 Tables 11-12

### 14. Section 10 opening

- order：14

- locator：Section 10 opening

- paraphrase_cn：定义收入增益ρ^μ和效用增益η^μ，并说明将用行业参数构造测试床。

- move_code：STUDY_OPENING

- statement_status：method_decision

- why_here_cn：开启数值研究。

- inherits_from_previous_cn：承接解析结果。

- changes_argument_state_cn：定义量化指标。

- sets_up_next_cn：为10.1测试床作铺垫。

- failure_if_removed_cn：数值指标定义缺失。

- evidence_pointer：Section 10 opening

### 15. Section 10.1

- order：15

- locator：Section 10.1

- paraphrase_cn：设定测试床参数：A=10、N=10、估值U[0,1]、λ=0.9、同质/异构广告场景。

- move_code：METHOD_DECISION

- statement_status：method_decision

- why_here_cn：说明数值实验设计。

- inherits_from_previous_cn：承接指标定义。

- changes_argument_state_cn：建立可复现参数。

- sets_up_next_cn：为Table 13和Figure 3的数值结果作铺垫。

- failure_if_removed_cn：数值实验设计缺失。

- evidence_pointer：Section 10.1

### 16. Section 10 Table 13

- order：16

- locator：Section 10 Table 13

- paraphrase_cn：数值显示OPT-IR在同质和异构广告下分别给交易所7.01%和18.22%收入增益；OPT-MB为23.02%和33.60%。

- move_code：EMPIRICAL_RESULT

- statement_status：empirical_result

- why_here_cn：给出核心量化证据。

- inherits_from_previous_cn：承接测试床。

- changes_argument_state_cn：量化机制收益。

- sets_up_next_cn：支撑管理启示。

- failure_if_removed_cn：核心量化证据缺失。

- evidence_pointer：Section 10 Table 13

### 17. Section 10 Figure 3

- order：17

- locator：Section 10 Figure 3

- paraphrase_cn：衰减率变异越大、广告主数量越多，两个机制相对BASE的收入增益越高。

- move_code：ROBUSTNESS_OR_BOUNDARY_TEST

- statement_status：empirical_result

- why_here_cn：用敏感性分析给出机制优势的边界条件。

- inherits_from_previous_cn：承接Table 13。

- changes_argument_state_cn：建立边界条件。

- sets_up_next_cn：总结收益何时最大。

- failure_if_removed_cn：边界条件证据缺失。

- evidence_pointer：Section 10 Figure 3

### 18. Section 10 Table 15

- order：18

- locator：Section 10 Table 15

- paraphrase_cn：社会福祉方面，BASE实现84.48%/77.45%的一阶最优，OPT-IR为91.54%/95.46%，OPT-MB达到100%。

- move_code：EMPIRICAL_RESULT

- statement_status：empirical_result

- why_here_cn：把收入指标扩展到效率指标。

- inherits_from_previous_cn：承接所有机制分配。

- changes_argument_state_cn：建立社会福祉贡献。

- sets_up_next_cn：为总结机制整体改善作铺垫。

- failure_if_removed_cn：社会福祉证据缺失。

- evidence_pointer：Section 10 Table 15

### 19. Section 10 final observation paragraph

- order：19

- locator：Section 10 final observation paragraph

- paraphrase_cn：两个机制相对BASE收益提升程度随广告多样性和竞争增强而增加。

- move_code：CLOSING

- statement_status：empirical_result

- why_here_cn：总结数值研究核心信息。

- inherits_from_previous_cn：承接Figure 3。

- changes_argument_state_cn：把边界结果综合为管理含义。

- sets_up_next_cn：为结论章节作铺垫。

- failure_if_removed_cn：数值研究总结缺失。

- evidence_pointer：Section 10 final observation paragraph

## 讨论与贡献逐句图谱

### 1. Section 11 P1 S1

- order：1

- locator：Section 11 P1 S1

- paraphrase_cn：随着在线广告生态技术快速演化，利益相关者必须提高利润率和供应链效率。

- move_code：CONTEXT

- statement_status：author_inference

- why_here_cn：结论开篇回归行业背景。

- inherits_from_previous_cn：承接全文。

- changes_argument_state_cn：重设宏观语境。

- sets_up_next_cn：为下一句总结研究问题作铺垫。

- failure_if_removed_cn：结论失去行业语境。

- evidence_pointer：Section 11 first paragraph

### 2. Section 11 P1 S2

- order：2

- locator：Section 11 P1 S2

- paraphrase_cn：数字广告交付过程因碎片化供应链存在多种低效。

- move_code：CONTEXT

- statement_status：author_inference

- why_here_cn：引出研究问题所在。

- inherits_from_previous_cn：承接行业背景。

- changes_argument_state_cn：建立低效背景。

- sets_up_next_cn：为下一句点名本文研究的低效作铺垫。

- failure_if_removed_cn：研究问题背景缺失。

- evidence_pointer：Section 11 first paragraph sentence 2

### 3. Section 11 P1 S3

- order：3

- locator：Section 11 P1 S3

- paraphrase_cn：本文分析了一次性把印象卖给单一广告主的低效，并获得了适合实时竞价的机制。

- move_code：CONTRIBUTION

- statement_status：contribution_claim

- why_here_cn：重述核心贡献。

- inherits_from_previous_cn：承接低效背景。

- changes_argument_state_cn：总结解决方案。

- sets_up_next_cn：为下一句行业期望作铺垫。

- failure_if_removed_cn：核心贡献总结缺失。

- evidence_pointer：Section 11 first paragraph sentence 3

### 4. Section 11 P1 S4

- order：4

- locator：Section 11 P1 S4

- paraphrase_cn：我们希望这些机制受到行业重视，因为它们更好匹配广告主和发布商，并有吸引人的收入影响。

- move_code：CONTRIBUTION

- statement_status：contribution_claim

- why_here_cn：表达行业意义。

- inherits_from_previous_cn：承接核心贡献。

- changes_argument_state_cn：强调实际影响。

- sets_up_next_cn：为下一句讨论限制作铺垫。

- failure_if_removed_cn：行业意义表达缺失。

- evidence_pointer：Section 11 first paragraph sentence 4

### 5. Section 11 P2 S1

- order：5

- locator：Section 11 P2 S1

- paraphrase_cn：我们假设广告主的私人信息（每点击估值）在当前会话中保持不变。

- move_code：LIMITATION_AND_FUTURE

- statement_status：author_inference

- why_here_cn：承认模型简化。

- inherits_from_previous_cn：承接研究总结。

- changes_argument_state_cn：开启限制讨论。

- sets_up_next_cn：为下一句讨论动态机制设计作铺垫。

- failure_if_removed_cn：限制声明缺失。

- evidence_pointer：Section 11 second paragraph

### 6. Section 11 P2 S2

- order：6

- locator：Section 11 P2 S2

- paraphrase_cn：一般地，广告主估值可随时间演化，这需要动态机制设计。

- move_code：LIMITATION_AND_FUTURE

- statement_status：author_inference

- why_here_cn：指出模型的前提限制。

- inherits_from_previous_cn：承接静态估值假设。

- changes_argument_state_cn：提出动态机制设计方向。

- sets_up_next_cn：为下一句未来研究作铺垫。

- failure_if_removed_cn：动态机制设计方向缺失。

- evidence_pointer：Section 11 second paragraph sentence 2

### 7. Section 11 P2 S3

- order：7

- locator：Section 11 P2 S3

- paraphrase_cn：设计适应广告主私人信息变化的动态机制是复杂问题，值得未来研究。

- move_code：LIMITATION_AND_FUTURE

- statement_status：author_inference

- why_here_cn：提出具体未来研究方向。

- inherits_from_previous_cn：承接动态机制设计。

- changes_argument_state_cn：完成限制讨论。

- sets_up_next_cn：为下一段讨论slot长度作铺垫。

- failure_if_removed_cn：未来研究方向缺失。

- evidence_pointer：Section 11 second paragraph sentence 3

### 8. Section 11 P3 S1

- order：8

- locator：Section 11 P3 S1

- paraphrase_cn：分区印象中一个自然的设计问题是时间槽长度的确定。

- move_code：LIMITATION_AND_FUTURE

- statement_status：author_inference

- why_here_cn：提出slot长度问题。

- inherits_from_previous_cn：承接限制讨论。

- changes_argument_state_cn：引入设计变量。

- sets_up_next_cn：为下一句说明现状作铺垫。

- failure_if_removed_cn：slot长度问题缺失。

- evidence_pointer：Section 11 third paragraph

### 9. Section 11 P3 S2

- order：9

- locator：Section 11 P3 S2

- paraphrase_cn：目前OpenX和DoubleClick允许发布商控制刷新率并给出广泛指南。

- move_code：CONTEXT

- statement_status：fact

- why_here_cn：提供slot长度现状。

- inherits_from_previous_cn：承接slot长度问题。

- changes_argument_state_cn：描述行业现状。

- sets_up_next_cn：为下一句独立研究作铺垫。

- failure_if_removed_cn：slot长度现状缺失。

- evidence_pointer：Section 11 third paragraph sentence 2

### 10. Section 11 P3 S3

- order：10

- locator：Section 11 P3 S3

- paraphrase_cn：动态确定slot长度和估计点击概率需要单独研究。

- move_code：LIMITATION_AND_FUTURE

- statement_status：author_inference

- why_here_cn：指出另一个未来方向。

- inherits_from_previous_cn：承接slot长度现状。

- changes_argument_state_cn：定义未来研究。

- sets_up_next_cn：为下一段推广到其他场景作铺垫。

- failure_if_removed_cn：slot长度未来研究缺失。

- evidence_pointer：Section 11 third paragraph sentence 3

### 11. Section 11 P4 S1

- order：11

- locator：Section 11 P4 S1

- paraphrase_cn：我们的分析可潜在应用到其他设置。

- move_code：BOUNDARY_CONDITION

- statement_status：author_inference

- why_here_cn：展开贡献适用范围。

- inherits_from_previous_cn：承接研究总结。

- changes_argument_state_cn：建立一般化贡献。

- sets_up_next_cn：为下一句抽象问题特征作铺垫。

- failure_if_removed_cn：一般化贡献缺失。

- evidence_pointer：Section 11 fourth paragraph

### 12. Section 11 P4 S2

- order：12

- locator：Section 11 P4 S2

- paraphrase_cn：更一般表述，我们的问题特征是：可分割商品、子商品间依赖关系、子商品估值异质。

- move_code：BOUNDARY_CONDITION

- statement_status：author_inference

- why_here_cn：抽象问题的一般结构。

- inherits_from_previous_cn：承接一般化贡献。

- changes_argument_state_cn：建立抽象框架。

- sets_up_next_cn：为下一句的应用示例作铺垫。

- failure_if_removed_cn：问题抽象框架缺失。

- evidence_pointer：Section 11 fourth paragraph sentence 2

### 13. Section 11 P4 S3

- order：13

- locator：Section 11 P4 S3

- paraphrase_cn：我们的目标更一般地是获得主方和代理方相对当前实践的win-win。

- move_code：CONTRIBUTION

- statement_status：author_inference

- why_here_cn：强调互惠目标的普适性。

- inherits_from_previous_cn：承接抽象框架。

- changes_argument_state_cn：建立设计目标普适性。

- sets_up_next_cn：为具体应用示例作铺垫。

- failure_if_removed_cn：目标普适性缺失。

- evidence_pointer：Section 11 fourth paragraph sentence 3

### 14. Section 11 P4 bullet 1

- order：14

- locator：Section 11 P4 bullet 1

- paraphrase_cn：示例1：多个代理使用共享资源（如计算能力）。

- move_code：BOUNDARY_CONDITION

- statement_status：author_inference

- why_here_cn：给出第一个推广应用示例。

- inherits_from_previous_cn：承接抽象框架。

- changes_argument_state_cn：展示跨领域适用性。

- sets_up_next_cn：为第二个示例作铺垫。

- failure_if_removed_cn：推广示例1缺失。

- evidence_pointer：Section 11 fourth paragraph bullet 1

### 15. Section 11 P4 bullet 2

- order：15

- locator：Section 11 P4 bullet 2

- paraphrase_cn：示例2：多个代理使用共享空间（如购物中心零售店）。

- move_code：BOUNDARY_CONDITION

- statement_status：author_inference

- why_here_cn：给出第二个推广应用示例。

- inherits_from_previous_cn：承接抽象框架。

- changes_argument_state_cn：进一步展示普适性。

- sets_up_next_cn：为下一段讨论header bidding作铺垫。

- failure_if_removed_cn：推广示例2缺失。

- evidence_pointer：Section 11 fourth paragraph bullet 2

### 16. Section 11 P5 S1

- order：16

- locator：Section 11 P5 S1

- paraphrase_cn：鉴于在线广告竞争性质，行业应继续寻找更好的变现方式。

- move_code：CONTEXT

- statement_status：author_inference

- why_here_cn：引入header bidding讨论。

- inherits_from_previous_cn：承接推广讨论。

- changes_argument_state_cn：重设行业语境。

- sets_up_next_cn：为下一句讨论header bidding作铺垫。

- failure_if_removed_cn：header bidding讨论语境缺失。

- evidence_pointer：Section 11 fifth paragraph

### 17. Section 11 P5 S2

- order：17

- locator：Section 11 P5 S2

- paraphrase_cn：为克服跨网络和跨交易所发现最佳价格的低效，行业开始采用header-bidding。

- move_code：CONTEXT

- statement_status：fact

- why_here_cn：引入相关技术发展。

- inherits_from_previous_cn：承接变现讨论。

- changes_argument_state_cn：描述行业新实践。

- sets_up_next_cn：为下一句比较需求侧和供给侧厚度作铺垫。

- failure_if_removed_cn：header bidding描述缺失。

- evidence_pointer：Section 11 fifth paragraph sentence 2

### 18. Section 11 P5 S3

- order：18

- locator：Section 11 P5 S3

- paraphrase_cn：header-bidding和我们的机制分别改善需求侧和供给侧市场厚度。

- move_code：CONTRIBUTION

- statement_status：author_inference

- why_here_cn：把本文机制与最新实践关联。

- inherits_from_previous_cn：承接header bidding。

- changes_argument_state_cn：定位本文机制的角色。

- sets_up_next_cn：为下一句未来研究作铺垫。

- failure_if_removed_cn：机制定位缺失。

- evidence_pointer：Section 11 fifth paragraph sentence 3

### 19. Section 11 P5 S4

- order：19

- locator：Section 11 P5 S4

- paraphrase_cn：未来研究分析这两种机制的互动及其对生态的联合改善。

- move_code：LIMITATION_AND_FUTURE

- statement_status：author_inference

- why_here_cn：提出联合研究问题。

- inherits_from_previous_cn：承接机制定位。

- changes_argument_state_cn：完成结论开放方向。

- sets_up_next_cn：无，全文结束。

- failure_if_removed_cn：未来开放方向缺失。

- evidence_pointer：Section 11 fifth paragraph sentence 4

## Study累积逻辑

### 1. 1

- study_or_phase：阶段1：Setting 1问题形式化

- evidence_job_cn：把现实的分区印象出售抽象成机制设计问题。

- what_it_establishes_cn：印象由N个时间槽组成；广告主有私人估值；IC/IR约束；P^IR目标函数；VCG作为效率参照。

- what_it_cannot_establish_cn：不能给出最优机制的具体形式，也没有考虑支付是否可实时计算。

- why_next_phase_is_needed_cn：需要求解P^IR并解决实现问题。

- transition_wording_function_cn：由P^IR的表述进入Section 4的定理推导。

### 2. 2

- study_or_phase：阶段2：OPT-IR推导与实时实现

- evidence_job_cn：证明收益最优机制存在并解决其支付规则实时实现问题。

- what_it_establishes_cn：Theorem 1证明OPT-IR是P^IR最优；分配可用O(AN)动态规划；随机化支付RAND保持IC/IR并兼容CPC/CPM。

- what_it_cannot_establish_cn：不能说明广告主福利相对现状如何，也不能说明SEQ是否近优。

- why_next_phase_is_needed_cn：需要与自然的myopic机制（SEQ）和现状BASE机制比较。

- transition_wording_function_cn：由Section 4结束进入Section 5 SEQ机制。

### 3. 3

- study_or_phase：阶段3：SEQ机制比较

- evidence_job_cn：排除逐槽独立拍卖这一直觉候选机制。

- what_it_establishes_cn：Example 1显示SEQ收入可仅为OPT-IR一半；Theorem 2给出次优充分条件；Example 3显示负相关并非必要；Theorem 3给出SEQ最优的充分条件；数值显示负相关越强SEQ越差。

- what_it_cannot_establish_cn：尚未进行比较BASE现状机制，也没有评估广告主福利。

- why_next_phase_is_needed_cn：需要转向当前实践BASE机制并衡量广告主福利。

- transition_wording_function_cn：由数值分析结束进入Section 7 BASE机制。

### 4. 4

- study_or_phase：阶段4：BASE机制与广告主福利

- evidence_job_cn：建立现状基准机制并证明OPT-IR对广告主福利有两种可能。

- what_it_establishes_cn：BASE是P^IR的同槽约束版本，Theorem 4给出其解；BASE是P^IR可行解故OPT-IR收入总不低于BASE；win-win和win-lose两个解析场景均存在。

- what_it_cannot_establish_cn：未给出如何构造保证广告主长期受益的最优机制。

- why_next_phase_is_needed_cn：win-lose场景需要互惠机制来保障广告主长期福利。

- transition_wording_function_cn：由Section 8总结进入Section 9 P^MB设置。

### 5. 5

- study_or_phase：阶段5：OPT-MB互惠机制

- evidence_job_cn：构造长期互惠最优机制。

- what_it_establishes_cn：Theorem 5证明OPT-MB是P^MB最优；VCG分配一阶最优；支付固定转移使广告主恰得BASE效用；win-win场景交易所收益更高；win-lose场景广告主免受损失。

- what_it_cannot_establish_cn：尚未在更现实的多广告异质环境下量化收益。

- why_next_phase_is_needed_cn：需要用行业参数测试床量化两个机制的相对收益和边界。

- transition_wording_function_cn：由Section 9.1对比进入Section 10数值研究。

### 6. 6

- study_or_phase：阶段6：数值测试床与边界分析

- evidence_job_cn：用行业参数量化机制相对BASE的收益和福利增益并检验边界。

- what_it_establishes_cn：OPT-IR同质/异构下收入增益7.01%/18.22%；OPT-MB为23.02%/33.60%；广告主效用OPT-IR下13.72%/55.61%，OPT-MB约0%；社会福祉BASE为84.48%/77.45%，OPT-IR为91.54%/95.46%，OPT-MB为100%；衰减率变异和广告主数量增大增益增大。

- what_it_cannot_establish_cn：不能替代真实市场数据；没有测试动态估值和变长slot；单次随机支付方差未讨论。

- why_next_phase_is_needed_cn：数值结果需转成结论中的设计知识和未来边界。

- transition_wording_function_cn：由Table 15社会福祉进入Section 11结论。

## 主张—证据台账

### 1. OPT-IR是P^IR收益最优机制

- claim_cn：OPT-IR是P^IR收益最优机制

- claim_level：theory

- supporting_evidence_cn：Theorem 1证明：虚拟价值单调性保证Θ_a^{OPT-IR}关于出价单调，满足Myerson最优性充分条件。

- support_strength：direct

- where_claim_is_made：Section 4 Theorem 1

- where_evidence_is_provided：Section 4 proof和Online Appendix A

### 2. OPT-IR分配可用O(AN)动态规划实现

- claim_cn：OPT-IR分配可用O(AN)动态规划实现

- claim_level：technical

- supporting_evidence_cn：OPT-IR分配是VCG分配把估值换成虚拟价值，动态规划(8)-(9)复杂度O(AN)。

- support_strength：direct

- where_claim_is_made：Section 4.1

- where_evidence_is_provided：Section 4.1 公式(8)-(9)

### 3. RAND支付保持期望收益和IC/IR

- claim_cn：RAND支付保持期望收益和IC/IR

- claim_level：mechanism

- supporting_evidence_cn：积分等于期望；E_u[M^{RAND}]=M^{OPT-IR}；分配单调保证IR。

- support_strength：direct

- where_claim_is_made：Section 4.2.1

- where_evidence_is_provided：Section 4.2.1 公式和论证

### 4. SEQ是近视的且可能大幅次优

- claim_cn：SEQ是近视的且可能大幅次优

- claim_level：technical

- supporting_evidence_cn：Example 1显示SEQ收入仅约OPT-IR一半；定理2给出充分条件；Table 8数值显示负相关增强时比率降至75.5%。

- support_strength：direct

- where_claim_is_made：Section 5末段和Section 6

- where_evidence_is_provided：Example 1, Theorem 2, Table 8

### 5. 负相关不是SEQ次优的必要条件

- claim_cn：负相关不是SEQ次优的必要条件

- claim_level：boundary

- supporting_evidence_cn：Example 3在非负相关下SEQ仍次优约5%。

- support_strength：direct

- where_claim_is_made：Section 6.3

- where_evidence_is_provided：Example 3

### 6. 估值与各槽点击概率同序时SEQ最优

- claim_cn：估值与各槽点击概率同序时SEQ最优

- claim_level：boundary

- supporting_evidence_cn：Theorem 3给出充分条件。

- support_strength：direct

- where_claim_is_made：Section 6.4

- where_evidence_is_provided：Theorem 3和Online Appendix D

### 7. OPT-IR收益总不低于BASE

- claim_cn：OPT-IR收益总不低于BASE

- claim_level：theory

- supporting_evidence_cn：BASE是P^IR的可行解（同槽约束版本），故P^IR最优的OPT-IR收益不低于BASE。

- support_strength：direct

- where_claim_is_made：Section 8 opening

- where_evidence_is_provided：Section 3.2 P^IR 与 Section 7 P^BASE

### 8. 广告主在OPT-IR下可能受益也可能受损

- claim_cn：广告主在OPT-IR下可能受益也可能受损

- claim_level：mechanism

- supporting_evidence_cn：win-win场景（Table 9）两广告主效用提高75%；win-lose场景（Table 10）广告主X效用下降100q%。

- support_strength：direct

- where_claim_is_made：Introduction 1.2和Section 8

- where_evidence_is_provided：Section 8.1 Table 9和Section 8.2 Table 10

### 9. OPT-MB是P^MB最优且一阶最优分配

- claim_cn：OPT-MB是P^MB最优且一阶最优分配

- claim_level：theory

- supporting_evidence_cn：VCG上界加固定转移构造达到上界；Theorem 5。

- support_strength：direct

- where_claim_is_made：Section 9

- where_evidence_is_provided：Theorem 5和上界论证

### 10. OPT-MB保证广告主长期恰得BASE效用

- claim_cn：OPT-MB保证广告主长期恰得BASE效用

- claim_level：mechanism

- supporting_evidence_cn：支付为M_VCG+E[U_VCG]-E[U_BASE]，约束(13)取等号；数值η≈0。

- support_strength：direct

- where_claim_is_made：Section 9 salient features

- where_evidence_is_provided：公式(15)和Table 13

### 11. OPT-IR/OPT-MB相对BASE带来7%-33%收入增益

- claim_cn：OPT-IR/OPT-MB相对BASE带来7%-33%收入增益

- claim_level：design_knowledge

- supporting_evidence_cn：100万样本蒙特卡洛：同质时7.01%和23.02%；异构时18.22%和33.60%。

- support_strength：direct

- where_claim_is_made：Introduction 1.2

- where_evidence_is_provided：Section 10 Table 13

### 12. 广告异构性和竞争增强收益增益

- claim_cn：广告异构性和竞争增强收益增益

- claim_level：boundary

- supporting_evidence_cn：Figure 3显示衰减率变异越大、广告主越多，增益越大。

- support_strength：direct

- where_claim_is_made：Section 10 Table 14和Figure 3

- where_evidence_is_provided：Figure 3(a)和3(b)

### 13. OPT-MB实现一阶最优社会福祉

- claim_cn：OPT-MB实现一阶最优社会福祉

- claim_level：design_knowledge

- supporting_evidence_cn：VCG分配最大化社会福利；Table 15显示同质和异构均达到100%。

- support_strength：direct

- where_claim_is_made：Section 10 Table 15

- where_evidence_is_provided：Table 15

### 14. 机制可推广到共享资源和共享空间等其他场景

- claim_cn：机制可推广到共享资源和共享空间等其他场景

- claim_level：design_knowledge

- supporting_evidence_cn：抽象问题具备可分割商品、依赖关系、异质估值三个特征；给出两个推广示例。

- support_strength：asserted

- where_claim_is_made：Section 11 P4

- where_evidence_is_provided：Section 11 P4两个推广示例

## ISR定位逻辑

- constitutive_is_problem_cn：论文把广告交易所在实时拍卖中把一次印象卖给单一广告主的做法，构成为数字平台上的资源配置问题：广告主支付意愿在印象生命周期内变化而机制无法利用，造成可计算的配置低效。问题不是纯算法优化或纯拍卖理论，而是一个IS基础设施（实时竞价平台）如何通过机制改变供需匹配效率的问题。

- technology_behavior_or_market_entanglement_cn：技术设计与用户行为和市场结构相互纠缠：用户留在会话的概率λ、点击后会话结束的随机过程决定了广告序列的展示概率；点击概率随时间衰减（impulse vs steady ads）使不同广告的即时价值交错；交易所的150ms实时交付约束直接决定了支付规则能否实现。技术不是可随意替换的工具，因为时间槽结构和用户随机离开/点击过程共同塑造了机制设计的动态规划结构和实现约束。

- role_of_benchmark_or_objective_evidence_cn：数值测试床和解析示例被用来支持IS层面的主张：相对BASE的收入增益（7%-33%）证明分区印象能消除真实交易所可以观察到的低效；win-win/win-lose解析场景证明福利分配并非由简单收益排序决定；Table 15的社会福祉百分比把机制论证从“收入更高”升级为“同时改善社会效率”。这些客观证据不是用来证明算法更快，而是证明平台治理机制改变广告市场的效率与福利分配。

- theory_in_design_cn：理论直接进入设计：Myerson虚拟价值最大化决定OPT-IR分配规则；Myerson支付公式决定支付结构，其积分计算困难驱动随机化支付RAND；VCG效率分配加固定BASE效用转移构造OPT-MB；revelation principle限制搜索空间。理论不是事后解释结果，而是每个设计决策的生成来源。理论既解释结果的产生机制（虚拟价值单调性、期望等价），也规定机制的约束（IC/IR、BASE效用下界）。

- technical_vs_is_contribution_balance_cn：论文在技术贡献（最优机制推导、动态规划、随机化支付、CPC/CPM实现）和IS贡献（消除平台配置低效、价格形成机制、广告主福利保障、交易所与广告主的双边利益分配）之间大致平衡。前半部分是机制设计推导，后半部分win-win/win-lose解析场景、数值测试床和一般化为共享资源分配进一步把技术结果指向行为和组织后果。随机支付和固定转移不只是数学技巧，而是被论证为“使机制可被真实广告交易所采用”的设计知识。

- beyond_transient_performance_cn：文章超越了暂时的性能优势：其一，用最优性定理证明不是击败某个baseline，而是在给定约束下已经是收益上界；其二，展示OPT-IR与OPT-MB的福利权衡，说明没有绝对占优，贡献是设计空间和选择依据；其三，用行业参数测试床和敏感性分析（广告异构性、竞争强度、衰减率变异）揭示增益何时出现及为何出现；其四，把结果抽象为“可分割+依赖+异质估值资源”的一般问题，把具体广告场景升华为可迁移的机制设计知识。

## 段落级仿写模板

### abstract_steps

1. 第一步：用行业背景句定位研究对象（移动广告生态、交易所作用）。

2. 第二步：陈述现状机制的事实（单一广告主全程展示）。

3. 第三步：指出该机制的效率缺陷（配置低效，忽略广告主支付意愿随时间变化）。

4. 第四步：提出研究目标（顺序展示多个广告的机制）。

5. 第五步：概述两个设置和两个最优机制。

6. 第六步：描述第一个机制的关键设计（随机化支付）。

7. 第七步：报告第一个机制的福利结果（交易所受益、广告主可能受益或受损）。

8. 第八步：报告第二个机制的性质（互惠、长期win-win）。

9. 第九步：强调两种机制均可高效计算、适合RTB。

### introduction_paragraph_steps

1. 第一步：行业背景和市场规模，建立研究重要性。

2. 第二步：介绍研究对象（广告交易所）的运作方式及其吸引力。

3. 第三步：收窄到具体场景（移动应用内广告），用会话长度说明时间维度的重要性。

4. 第四步：用图形示例建立低效现象（胜者全程展示，败者在某时段更高价值）。

5. 第五步：提出设计方向（分区印象），排除技术障碍。

6. 第六步：提出并排除自然候选机制（逐槽独立拍卖），预告分析。

7. 第七步：引入利益相关者福利问题，为第二设置作铺垫。

8. 第八步：提炼研究目标，提出实时性和简单性要求。

9. 第九步：列贡献：框架、两个最优机制、分配可计算性、支付挑战与随机化支付、福利权衡、数值增益。

10. 第十步：给出论文结构路标。

### theory_to_design_steps

1. 第一步：文献综述建立与现有空间槽/时间拍卖文献的差异。

2. 第二步：定义模型基础变量（印象、时间槽、点击概率、用户留驻概率、广告主估值分布）。

3. 第三步：论证关键假设合理性（点击概率共同知识）。

4. 第四步：引入机制设计理论（正则分布、revelation principle、直接机制、IC/IR）。

5. 第五步：形式化P^IR目标函数。

6. 第六步：引入VCG机制作为效率参照。

7. 第七步：推导最优机制（Theorem 1）并说明证明路径。

8. 第八步：把理论最优转化为可计算分配（动态规划）。

9. 第九步：识别支付计算障碍，用示例展示。

10. 第十步：引入随机化支付并证明性质保持，然后转化为CPC/CPM。

### method_and_study_sequence_steps

1. 第一步：从最优机制出发，引入自然候选SEQ机制，说明其直觉而可能的缺陷。

2. 第二步：用反例和数值展示SEQ次优，用充分条件界定其次优情境和最优情境。

3. 第三步：转入现状BASE机制，形式化为带同槽约束的问题，给出其解。

4. 第四步：比较OPT-IR与BASE，证明交易所受益、广告主可能受损。

5. 第五步：用两个解析场景证明win-win和win-lose都存在。

6. 第六步：基于福利缺陷提出设置2（P^MB），构造OPT-MB并证明最优性。

7. 第七步：重新用win-win/win-lose场景比较两种机制。

8. 第八步：用行业参数测试床量化收益/福利增益和边界。

### results_reporting_steps

1. 第一步：定义结果指标（如收入增益ρ^μ和效用增益η^μ）。

2. 第二步：说明测试床参数来源（行业实践、文献）。

3. 第三步：报告主结果（两种机制相对BASE的收益和效用增益）。

4. 第四步：解释结果为何出现（异构性提高低效，机制可挖掘）。

5. 第五步：报告边界分析（衰减率变异、竞争者数量）。

6. 第六步：报告社会福祉结果。

7. 第七步：总结管理含义（机制选择取决于环境和广告主保障意愿）。

### discussion_and_contribution_steps

1. 第一步：重述行业背景和研究问题。

2. 第二步：总结核心贡献（机制设计、实时实现、两种机制）。

3. 第三步：承认模型限制（静态估值、固定slot长度）。

4. 第四步：提出理论未来方向（动态机制设计、slot长度优化）。

5. 第五步：把具体问题抽象为一般资源分配特征（可分割、依赖、异质估值）。

6. 第六步：给出跨领域推广示例（共享资源、共享空间）。

7. 第七步：与最新行业实践（header bidding）关联并提出联合研究。

## 可执行写作算法

### 1. 1

- step：1

- rhetorical_job_cn：建立行业背景与研究对象，简述现状机制的运作。

- research_evidence_required_cn：行业报告或市场数据说明市场规模；对现状机制的事实性描述。

- sentence_pattern_function_cn：用背景句打开，用事实句描述机制，用数据句量化重要性。

- transition_condition_cn：趋势：介绍现状机制后自然指向其局限。

### 2. 2

- step：2

- rhetorical_job_cn：构造一个图形化的低效示例，把现实问题变成可观察的机会损失。

- research_evidence_required_cn：至少一个参数化示例，能显示胜者广告的即时价值在某时段低于败者。

- sentence_pattern_function_cn：设场景、设胜者、设败者、指出交替区间、定义阴影区域为低效。

- transition_condition_cn：发现：低效被定义后，自然产生设计方向。

### 3. 3

- step：3

- rhetorical_job_cn：提出设计方向（如分区印象），排除技术障碍，形成研究目标。

- research_evidence_required_cn：行业技术事实（如平台支持刷广告）；对设计方向可行性的简单论证。

- sentence_pattern_function_cn：用“这带来想法”连接低效；用事实排除技术障碍；用目标句收束。

- transition_condition_cn：方向：设计方向明确后，引入自然候选和福利问题。

### 4. 4

- step：4

- rhetorical_job_cn：把问题形式化为可求解的机制设计模型。

- research_evidence_required_cn：参与者、私人类型、效用函数、机制组成、IC/IR约束的清晰数学定义；revelation principle、正则分布等理论条件。

- sentence_pattern_function_cn：先给模型要素，再给机制定义，再写约束，最后写出优化问题。

- transition_condition_cn：模型：目标函数和约束明确后，可进入求解。

### 5. 5

- step：5

- rhetorical_job_cn：推导并证明最优机制，同时指出实现障碍。

- research_evidence_required_cn：最优性定理、充分条件；对实现难点的分析；最小示例展示难点。

- sentence_pattern_function_cn：用定理句声明最优；用证明路径句解释；用例子句展示实现挑战。

- transition_condition_cn：挑战：最优但难实现时，引出设计改进。

### 6. 6

- step：6

- rhetorical_job_cn：设计实现改进（如随机化支付），证明性质保持并连接行业格式。

- research_evidence_required_cn：期望等价证明；IC/IR保持论证；与CPC/CPM格式的转换构造。

- sentence_pattern_function_cn：先给构造定义，再证期望等价，再证性质保持，最后给CPC/CPM版本。

- transition_condition_cn：可实施：机制可部署后，需要比较基准。

### 7. 7

- step：7

- rhetorical_job_cn：引入自然候选机制和现状基准机制，分别比较并界定边界。

- research_evidence_required_cn：候选机制定义；次优性/最优性反例或充分条件；数值表量化幅度。

- sentence_pattern_function_cn：先定义候选；用反例否定；用定理给条件；用数值表量化。

- transition_condition_cn：福利：发现利益相关者可能受损后，引入新设置。

### 8. 8

- step：8

- rhetorical_job_cn：提出第二设置并构造互惠机制，证明最优性和福利性质。

- research_evidence_required_cn：新约束定义（如长期BASE效用）；VCG上界论证；固定转移构造；最优性定理。

- sentence_pattern_function_cn：先定义新问题；再给上界；再给机制；最后证明并列出性质。

- transition_condition_cn：量化：理论性质完成后，进入数值测试床。

### 9. 9

- step：9

- rhetorical_job_cn：用行业参数构造测试床，量化收益/福利增益和边界。

- research_evidence_required_cn：行业参数来源（会话时长、曝光下限、CTR、广告主数量）；蒙特卡洛样本；参数敏感性设计。

- sentence_pattern_function_cn：先定义指标；再给参数来源；再报告主结果；再报告边界；再给社会福祉。

- transition_condition_cn：综合：数值结果可直接支撑管理启示。

### 10. 10

- step：10

- rhetorical_job_cn：总结贡献、承认限制、提出未来方向并推广到一般问题。

- research_evidence_required_cn：与引言低效问题的闭环；对假设的坦诚评估；抽象出可迁移的设计特征和推广示例。

- sentence_pattern_function_cn：重述问题、总结贡献、列限制、提方向、再抽象推广、最后与最新实践关联。

- transition_condition_cn：结束：全文与引言闭环，开放问题留给未来。

## 应模仿的高价值动作

1. 用图形示例定义配置低效，把数学机制设计问题翻译成可感知的行业损失。

2. 把优化问题写成机制设计形式：最大化目标、IC/IR约束，并明确说明每个约束的含义。

3. 用Theorem+证明路径句+单调性充分条件的方式证明最优性，而不是只声称。

4. 识别Myerson支付积分在实际无法快速计算后，用均匀随机化把积分变成期望，并用期望等价和单调性保持IC/IR。

5. 把新支付转换为CPC和CPM两种行业格式，让机制不只在理论中成立。

6. 用两个解析场景（win-win和win-lose）证明福利分配的非单一性，为第二机制创造动机。

7. 用VCG上界+固定转移构造互惠机制，使广告主恰得BASE效用、交易所拿走剩余，并证明达到上界。

8. 用行业参数测试床和100万样本蒙特卡洛量化机制增益，同时用衰减率变异和广告主数量做边界分析。

9. 把具体广告场景抽象为‘可分割+依赖+异质估值’的一般资源分配问题，给出共享资源和共享空间两个推广示例。

## 不要只复制的表面动作

1. 不要在没有具体反例或充分条件下断言某一自然候选机制次优；本文严格配备Example和Theorem。

2. 不要只声称随机化支付保持机制性质而不给出期望等价和IC/IR保持的推导。

3. 不要只报告仿真百分比而不说明参数来源和样本设计；本文明确给出行业来源和100万样本。

4. 不要声称一个机制绝对优于另一个；本文明确指出OPT-IR和OPT-MB在不同场景各有取舍。

5. 不要把点击概率共同知识和静态估值当作无关紧要；本文论证其角色并说明若放宽需要什么。

6. 不要只总结数值增益而不解释增益机制（异构性增加低效、机制挖掘低效）。

## 证据薄弱或跳跃的动作

1. 数值增益7%-33%来自仿真而非真实市场数据，声称‘交易所可以获益’时需限定为数值结论。

2. OPT-MB以BASE效用为参照，现实中BASE本身可能随市场变化，长期保证的基准可能漂移。

3. 点击概率共同知识假设虽被部分放宽（机制保持IC），但最优性证明仍依赖它；不能过度宣称适用所有现实。

4. RAND支付只验证期望收益，未讨论单次拍卖支付的方差和广告主风险厌恶。

5. 150ms实时性只通过O(AN)复杂度推断，没有真实RTB延迟测量。

6. Theorem 2/3和win-win/win-lose的完整证明在在线附录中，正文只给结论，读者需要依赖附录（本文未逐项验证附录细节）。

7. 共享资源和共享空间的推广是断言性示例，没有形式化证明机制在这些场景的最优性。

## 一句话套路

把一个数字平台可观察的资源配置低效转成机制设计问题，先用理论构造收益最优机制并解决实时实现，再用自然候选和现状基准分层反驳，发现利益相关者福利缺陷后改用VCG加固定效用转移构造互惠机制，最后用行业参数仿真量化边界并抽象为一般设计知识。

## 分析边界

全文以PDF文本提供，Figure 1/2/3和部分表格数据主要通过文字转述；部分数学公式因PDF/HTML转换可能有微变体，但符号和推导关系清晰；未获得在线附录，Theorem 2/3、win-win/win-lose的详细证明和Remark 2的证明依赖附录，本文对证明细节的还原以正文结论为准；部分段落边界（如Introduction 1.1的段落切分）因原文紧缩排版存在轻微不确定性。
