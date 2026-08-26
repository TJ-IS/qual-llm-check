# Customer Acquisition via Explainable Deep Reinforcement Learning：ISR 句段级微观图谱

- 作者：Yicheng Song; Wenbo Wang; Song Yao
- 年份：2025
- DOI：10.1287/isre.2022.0529
- 源文件：28396_2025_customer-acquisition-via-explainable-deep-reinforcement-learning.md
- 置信度：0.86

## 核实后的宏观骨架

本文是一篇典型的ISR设计科学型论文。全文以‘顾客获取的序列化定向投放需要长期收益优化与可解释性’为核心问题，构造DRQN-attention制品：在DRQN基础上加入定制注意力机制，使模型在估计Q值时对下一次广告曝光机会的one-hot特征施加显式注意力瓶颈。文章的顺序是：引言建立‘序列化投放重要但困难、现有监督学习和单干预实验不足、RL潜力大但黑箱’的多重缺口；文献综述区分RL商业决策与可解释RL两流，并用Table 1对比说明注意力机制在不同情境下的query/key/value定制差异；研究情境用数字银行和中小企业融资建立现实重要性；模型部分先形式化RL状态/动作/奖励，再给出DRQN处理POMDP，最后给出DRQN-attention的定制注意力机制并强调其‘前向规划’性质；实证部分依次完成离策略基准评价（证明长期收益优势）、联邦学习评价（证明隐私敏感部署可行性）、注意力权重与关联规则对比（证明注意力捕捉长期最优轨迹而非即时关联）、三类渠道案例加测试集匹配/未匹配验证（把可解释性转化为管理洞察）；结论回扣贡献并承认注意力非直接解释、状态动作空间覆盖不足、需on-policy验证等边界。五阶段证据依次回答：能否构建、是否更优、是否可部署、为何可解释、解释是否有用。

## 摘要逐句图谱

### 1. Abstract P1 S1

- order：1

- locator：Abstract P1 S1

- paraphrase_cn：有效的顾客获取在很大程度上依赖于序列化定向投放，以确保恰当的营销信息触达恰当的顾客。

- move_code：CONTEXT_OPENING

- statement_status：fact

- why_here_cn：开篇就把‘序列化定向投放’定义为顾客获取的核心机制，为全文的问题域定调。

- inherits_from_previous_cn：无前句，独立建立话题。

- changes_argument_state_cn：把读者注意力引向顾客获取中的序列决策而非单次投放。

- sets_up_next_cn：制造对序列投放方法的需求，为下一句引入RL作铺垫。

- failure_if_removed_cn：缺乏问题锚点，读者不知道全文为何谈序列化。

- evidence_pointer：Abstract P1 S1

### 2. Abstract P1 S2

- order：2

- locator：Abstract P1 S2

- paraphrase_cn：序列化定向投放能引导顾客走过获取过程，从而为企业优化长期收入。

- move_code：PROBLEM_SIGNIFICANCE

- statement_status：author_inference

- why_here_cn：把序列投放从‘重要’推进到‘能优化长期收入’，为RL目标提供业务理由。

- inherits_from_previous_cn：承接上一句序列化投放的重要性。

- changes_argument_state_cn：确立了评价标准：长期收入，而非点击率等中间指标。

- sets_up_next_cn：为RL作为能优化长期收入的框架做铺垫。

- failure_if_removed_cn：长期收益这一核心评价标准失去前提。

- evidence_pointer：Abstract P1 S2

### 3. Abstract P1 S3

- order：3

- locator：Abstract P1 S3

- paraphrase_cn：RL在促进用户获取中的序列化定向投放方面已展现巨大潜力。

- move_code：THEORY_OR_METHOD_ENTRY

- statement_status：prior_literature

- why_here_cn：引入RL作为解决序列化投放问题的主要技术框架。

- inherits_from_previous_cn：承接序列化投放需要优化长期收入。

- changes_argument_state_cn：把问题从业务需要转向技术方案。

- sets_up_next_cn：为下一句指出RL缺陷制造对照。

- failure_if_removed_cn：RL不是显然的候选，后文黑箱批评也失去靶子。

- evidence_pointer：Abstract P1 S3

### 4. Abstract P1 S4

- order：4

- locator：Abstract P1 S4

- paraphrase_cn：然而，RL在此过程中做出的决策往往缺乏可解释性。

- move_code：GAP_OR_LIMITATION

- statement_status：prior_literature

- why_here_cn：立即给出本文的核心缺口：RL潜力与黑箱之间的张力。

- inherits_from_previous_cn：承接RL的潜力声明。

- changes_argument_state_cn：把论证状态从‘RL可行’推向‘RL需要可解释’。

- sets_up_next_cn：为提出DRQN-attention的双重目标做需要。

- failure_if_removed_cn：本文的独特贡献（可解释RL）失去动机。

- evidence_pointer：Abstract P1 S4

### 5. Abstract P2 S1

- order：5

- locator：Abstract P2 S1

- paraphrase_cn：我们引入DRQN-attention模型，在优化长期收益的同时增强决策可解释性。

- move_code：ARTIFACT_PROPOSAL

- statement_status：author_inference

- why_here_cn：直接宣布制品与双重目标，是摘要的核心claim。

- inherits_from_previous_cn：回应上一句的可解释性缺口。

- changes_argument_state_cn：从‘问题是什么’转为‘我们提出什么’。

- sets_up_next_cn：为下一句解释模型机制做引导。

- failure_if_removed_cn：摘要失去核心贡献对象。

- evidence_pointer：Abstract P2 S1

### 6. Abstract P2 S2

- order：6

- locator：Abstract P2 S2

- paraphrase_cn：核心思想是修改Q-learning，加入注意力机制形成瓶颈，迫使模型关注下一次广告曝光中能带来最优长期收益的特征。

- move_code：DESIGN_FEATURE

- statement_status：design_decision

- why_here_cn：用一句话传达模型的技术内核，让读者预知可解释性来自何处。

- inherits_from_previous_cn：承接DRQN-attention的提出。

- changes_argument_state_cn：把制品从名字推进为可理解的机制。

- sets_up_next_cn：为摘要后半部分‘前向规划’和渠道案例提供机制基础。

- failure_if_removed_cn：读者不知道为何该模型能同时优化与解释。

- evidence_pointer：Abstract P2 S2

### 7. Abstract P3 S1

- order：7

- locator：Abstract P3 S1

- paraphrase_cn：我们使用一家数字银行的综合数据集估计模型。

- move_code：DATA_SOURCE

- statement_status：method_decision

- why_here_cn：给出实证证据来源，表明不是人工或玩具环境。

- inherits_from_previous_cn：模型提出后自然需要数据估计。

- changes_argument_state_cn：把论证推进到经验检验阶段。

- sets_up_next_cn：为下一句实证结论提供基础。

- failure_if_removed_cn：结果缺乏数据依托，可信度下降。

- evidence_pointer：Abstract P3 S1

### 8. Abstract P3 S2

- order：8

- locator：Abstract P3 S2

- paraphrase_cn：实证结果显示模型具有可解释性，并且长期收益优化上优于现有方法。

- move_code：MAIN_RESULT

- statement_status：empirical_result

- why_here_cn：给出摘要层面最重要的双重结论：既可解释又更优。

- inherits_from_previous_cn：基于数据估计。

- changes_argument_state_cn：把模型从‘提出’升级为‘验证有效’。

- sets_up_next_cn：为三类具体洞察做总起。

- failure_if_removed_cn：模型的双重优势主张失去结果支撑。

- evidence_pointer：Abstract P3 S2

### 9. Abstract P3 S3

- order：9

- locator：Abstract P3 S3

- paraphrase_cn：具体来说，模型中的注意力机制发挥前向规划的作用，能找出下一次广告曝光中更可能带来最优结果的特征。

- move_code：MECHANISM_CLAIM

- statement_status：theory_claim

- why_here_cn：把性能结果提升为机制解释：注意力=前向规划。

- inherits_from_previous_cn：承接实证结果中的可解释性部分。

- changes_argument_state_cn：从‘模型可解释’推进到‘解释的具体机制’。

- sets_up_next_cn：为后面三类渠道洞察提供机制框架。

- failure_if_removed_cn：可解释性沦为抽象口号，失去机制内容。

- evidence_pointer：Abstract P3 S3

### 10. Abstract P3 S4-S6

- order：10

- locator：Abstract P3 S4-S6

- paraphrase_cn：我们进一步展示模型如何做出广告渠道选择决策：能针对不同行业选择最优渠道、能根据动态顾客行为调整渠道、能学习行业季节性并相应校准渠道。

- move_code：MANAGERIAL_INSIGHT_PREVIEW

- statement_status：empirical_result

- why_here_cn：把机制转化为管理者可用的三类渠道洞察，预告第7节结构。

- inherits_from_previous_cn：承接前向规划机制的三个功能。

- changes_argument_state_cn：把贡献从技术性能扩展到管理决策知识。

- sets_up_next_cn：为正文第7节的三个案例做预告。

- failure_if_removed_cn：文章对IS读者的实践价值被削弱。

- evidence_pointer：Abstract P3 S4-S6

## 引言逐句图谱

### 1. Introduction P1 S1-S2

- order：1

- locator：Introduction P1 S1-S2

- paraphrase_cn：成功的顾客获取是数字时代企业增长的关键因素，该过程涉及识别潜在顾客并引导其通过购买漏斗。

- move_code：CONTEXT_OPENING

- statement_status：fact

- why_here_cn：用‘增长’和‘漏斗’把顾客获取确立为重要且过程性的问题。

- inherits_from_previous_cn：无，是引言起点。

- changes_argument_state_cn：建立了领域背景和‘引导顾客通过漏斗’的序列化视角。

- sets_up_next_cn：为获客成本与效率的讨论提供框架。

- failure_if_removed_cn：没有领域锚点，后文所有动机缺乏依托。

- evidence_pointer：Introduction P1 S1-S2

### 2. Introduction P1 S3-S4

- order：2

- locator：Introduction P1 S3-S4

- paraphrase_cn：企业以获客成本和效率衡量获客策略；数字平台上的获客成本极高，确保获客成本不超过获客客户平均生命周期价值至关重要。

- move_code：PRACTICAL_STAKES

- statement_status：fact

- why_here_cn：给出经济利害关系，说明为什么需要优化方法。

- inherits_from_previous_cn：承接获客是增长关键的背景。

- changes_argument_state_cn：把顾客获取从‘重要’推进到‘有重大成本风险’。

- sets_up_next_cn：为批评随机实验和引入模型方法创造现实动机。

- failure_if_removed_cn：方法改进的必要性失去价值支撑。

- evidence_pointer：Introduction P1 S3-S4

### 3. Introduction P2 S1

- order：3

- locator：Introduction P2 S1

- paraphrase_cn：随机实验是评估顾客获取干预政策的常用方法，但这些实验通常只关注每个单独干预的影响，忽略干预之间的相互作用。

- move_code：PRIOR_METHOD_AND_LIMITATION

- statement_status：prior_literature

- why_here_cn：点出现有黄金标准方法的结构性局限，为替代方案铺垫。

- inherits_from_previous_cn：承接获客策略需要评价的背景。

- changes_argument_state_cn：把‘需要评价’升级为‘现有评价方法不够’。

- sets_up_next_cn：为序列化干预和维度灾难的描述做引子。

- failure_if_removed_cn：为什么不能直接靠随机实验回答本文问题变得不清楚。

- evidence_pointer：Introduction P2 S1

### 4. Introduction P2 S2-S3

- order：4

- locator：Introduction P2 S2-S3

- paraphrase_cn：当目标变成寻找多个干预的最优序列时，策略空间指数增长，随机实验难以克服维数灾难。

- move_code：METHOD_LIMITATION_DETAIL

- statement_status：author_inference

- why_here_cn：用组合爆炸解释随机实验为何在序列化投放中失效。

- inherits_from_previous_cn：承接随机实验忽略干预间相互作用的局限。

- changes_argument_state_cn：把对随机实验的批评聚焦到‘序列决策’这一关键困难。

- sets_up_next_cn：为‘优化不需要精确因果效应’提供情境。

- failure_if_removed_cn：模型方法的必要性论证缺少技术性理由。

- evidence_pointer：Introduction P2 S2-S3

### 5. Introduction P2 S4

- order：5

- locator：Introduction P2 S4

- paraphrase_cn：因果决策文献表明，通过随机实验精确估计每个干预的因果效应，对于决定干预内容与顺序往往并非必需；优化只需区分不同干预在不同情境下的效果。

- move_code：EPISTEMIC_JUSTIFICATION

- statement_status：prior_literature

- why_here_cn：引用权威文献为‘用模型优化替代因果识别’提供方法论辩护。

- inherits_from_previous_cn：回应维数灾难带来的实验不可行。

- changes_argument_state_cn：把放弃随机实验从‘不得已’改写为‘原则上可行且合理’。

- sets_up_next_cn：为基于模型的方法做合法性铺垫。

- failure_if_removed_cn：审稿人可能质疑不用实验的正当性。

- evidence_pointer：Introduction P2 S4

### 6. Introduction P2 S5

- order：6

- locator：Introduction P2 S5

- paraphrase_cn：因此，以期望业务结果为导向的模型方法可能是顾客获取问题的有前途解决方案。

- move_code：METHOD_TURN

- statement_status：author_inference

- why_here_cn：从对实验的批评转向模型方法，完成引言第一个转折。

- inherits_from_previous_cn：由因果决策文献的论点推出。

- changes_argument_state_cn：确立模型方法作为本文方法论立场。

- sets_up_next_cn：为机器学习模型的引入做过渡。

- failure_if_removed_cn：从问题到方法之间出现逻辑跳跃。

- evidence_pointer：Introduction P2 S5

### 7. Introduction P3 S1

- order：7

- locator：Introduction P3 S1

- paraphrase_cn：机器学习模型已成为开发经济高效获客策略的重要工具。

- move_code：TECHNOLOGY_CONTEXT

- statement_status：fact

- why_here_cn：引入现有技术路线，为后续指出其不足做铺垫。

- inherits_from_previous_cn：承接模型方法作为替代方案的结论。

- changes_argument_state_cn：把‘模型方法’具体化为‘机器学习模型’。

- sets_up_next_cn：为监督学习局限的描述提供对象。

- failure_if_removed_cn：后文对监督学习的批评缺少数技术背景。

- evidence_pointer：Introduction P3 S1

### 8. Introduction P3 S2

- order：8

- locator：Introduction P3 S2

- paraphrase_cn：现有基于机器学习的定向技术常用监督学习预测潜在顾客在单一营销干预下的盈利性。

- move_code：PRIOR_APPROACH

- statement_status：prior_literature

- why_here_cn：总结现有技术基线：监督学习只处理单次干预。

- inherits_from_previous_cn：承接机器学习工具的普遍性。

- changes_argument_state_cn：界定现有方法的能力边界。

- sets_up_next_cn：为否定单次干预假设做铺垫。

- failure_if_removed_cn：为什么需要转向序列方法缺少对照。

- evidence_pointer：Introduction P3 S2

### 9. Introduction P3 S3

- order：9

- locator：Introduction P3 S3

- paraphrase_cn：但顾客购买通常需要投入大量时间和金钱，转化不太可能由单次干预触发。

- move_code：PHENOMENON_CLAIM

- statement_status：author_inference

- why_here_cn：用真实消费决策特征说明单次干预假设不成立。

- inherits_from_previous_cn：由监督学习的局限推出。

- changes_argument_state_cn：从技术缺陷升级为现象层面的不匹配。

- sets_up_next_cn：为序列化投放和RL引入提供经验基础。

- failure_if_removed_cn：序列化投放的必然性失去依据。

- evidence_pointer：Introduction P3 S3

### 10. Introduction P3 S4

- order：10

- locator：Introduction P3 S4

- paraphrase_cn：先前的文献已把顾客获取框定为通过一系列营销信息在不同情境下逐步转化潜在顾客。

- move_code：PRIOR_FRAMING

- statement_status：prior_literature

- why_here_cn：引用文献正式把顾客获取定义为序列决策。

- inherits_from_previous_cn：承接单次干预不足的现象。

- changes_argument_state_cn：把顾客获取重新表述为序列化投放问题。

- sets_up_next_cn：为探索-利用权衡的描述提供问题框架。

- failure_if_removed_cn：顾客获取作为RL问题的合法性降低。

- evidence_pointer：Introduction P3 S4

### 11. Introduction P3 S5

- order：11

- locator：Introduction P3 S5

- paraphrase_cn：潜在顾客对不同信息的响应未知或仅部分显现，企业需要在利用已知响应稳定收益和探索不确定但可能更有利的消息之间权衡。

- move_code：MECHANISM_INTRODUCTION

- statement_status：author_inference

- why_here_cn：解释序列化投放中的根本张力：探索与利用。

- inherits_from_previous_cn：由序列化决策框架推出。

- changes_argument_state_cn：把序列化投放问题转化为RL的标准权衡。

- sets_up_next_cn：为RL框架引入做逻辑铺垫。

- failure_if_removed_cn：RL的适用性论证缺少核心机制。

- evidence_pointer：Introduction P3 S5

### 12. Introduction P3 S6

- order：12

- locator：Introduction P3 S6

- paraphrase_cn：为此，研究者转向强化学习，一个在有限预算下平衡探索与利用的框架。

- move_code：RL_ENTRY

- statement_status：prior_literature

- why_here_cn：正式把RL确立为解决方案框架。

- inherits_from_previous_cn：由探索-利用权衡推出。

- changes_argument_state_cn：完成从问题到技术框架的转换。

- sets_up_next_cn：为RL商业应用的成功案例做铺垫。

- failure_if_removed_cn：全文核心技术框架失去引入点。

- evidence_pointer：Introduction P3 S6

### 13. Introduction P4 S1

- order：13

- locator：Introduction P4 S1

- paraphrase_cn：RL已在优化广告点击率、设计序列促销、基于历史实验分配对象等商业问题上展现潜力。

- move_code：RL_SUCCESS_EVIDENCE

- statement_status：prior_literature

- why_here_cn：说明RL在商业决策中已被验证，不是空想。

- inherits_from_previous_cn：承接RL作为序列决策框架。

- changes_argument_state_cn：确立RL的可行性基线。

- sets_up_next_cn：为这些成功背后的黑箱缺陷做对照。

- failure_if_removed_cn：RL用于顾客获取的可行性缺少证据。

- evidence_pointer：Introduction P4 S1

### 14. Introduction P4 S2

- order：14

- locator：Introduction P4 S2

- paraphrase_cn：尽管有这些成功，多数用于商业决策的RL模型仍是缺乏透明度的黑箱模型。

- move_code：BLACK_BOX_GAP

- statement_status：prior_literature

- why_here_cn：点出RL应用的一般缺陷，制造‘成功但不可解释’的张力。

- inherits_from_previous_cn：承接RL成功应用的列举。

- changes_argument_state_cn：把RL从‘有用’推进到‘需要可解释性’。

- sets_up_next_cn：为企业采用条件和企业信任的讨论做铺垫。

- failure_if_removed_cn：可解释性作为核心问题失去来源。

- evidence_pointer：Introduction P4 S2

### 15. Introduction P4 S3

- order：15

- locator：Introduction P4 S3

- paraphrase_cn：企业采用RL模型必须理解决策如何做出、使用了哪些信息、为何出错。

- move_code：ADOPTION_REQUIREMENT

- statement_status：author_inference

- why_here_cn：把可解释性从学术愿望上升为企业采用的实际条件。

- inherits_from_previous_cn：承接黑箱问题。

- changes_argument_state_cn：确立可解释性是实际部署的必要条件。

- sets_up_next_cn：为缺乏可解释性导致信任下降做铺垫。

- failure_if_removed_cn：可解释性好坏影响企业采用的说法失去基础。

- evidence_pointer：Introduction P4 S3

### 16. Introduction P4 S4

- order：16

- locator：Introduction P4 S4

- paraphrase_cn：缺乏可解释性会令用户困惑并降低对智能系统的信任，阻碍模型未来应用。

- move_code：CONSEQUENCE_OF_GAP

- statement_status：prior_literature

- why_here_cn：给出黑箱缺口的现实后果，增强紧迫性。

- inherits_from_previous_cn：由企业采用需要透明推出。

- changes_argument_state_cn：把可解释性缺口与模型落地绑定。

- sets_up_next_cn：为DARPA和IS学者呼吁可解释ML做铺垫。

- failure_if_removed_cn：可解释性研究的必要性缺少后果支撑。

- evidence_pointer：Introduction P4 S4

### 17. Introduction P4 S5-S6

- order：17

- locator：Introduction P4 S5-S6

- paraphrase_cn：DARPA启动了可解释AI项目，信息系统研究者也呼吁为深度学习模型赋予可解释性。

- move_code：INSTITUTIONAL_AND_DISCIPLINARY_SUPPORT

- statement_status：prior_literature

- why_here_cn：用外部权威和本学科呼吁共同确认可解释性是正当议题。

- inherits_from_previous_cn：承接可解释性缺乏的现实后果。

- changes_argument_state_cn：把可解释性从单个企业的实际问题提升为领域内公认议程。

- sets_up_next_cn：为界定‘本文要的可解释性类型’做铺垫。

- failure_if_removed_cn：IS期刊读者可能认为可解释性只是CS问题。

- evidence_pointer：Introduction P4 S5-S6

### 18. Introduction P4 S7

- order：18

- locator：Introduction P4 S7

- paraphrase_cn：需要澄清的是，这种可解释性不一定需要来自实地实验的干净因果效应，也可以是透过模型输出窥探决策过程的洞察。

- move_code：SCOPE_DEFINITION

- statement_status：author_inference

- why_here_cn：预先界定本文可解释性的含义，防止读者用因果推断标准衡量。

- inherits_from_previous_cn：由可解释AI讨论推出。

- changes_argument_state_cn：把可解释性从因果效应松绑为决策洞察。

- sets_up_next_cn：为后文用注意力权重作为解释提供自由空间。

- failure_if_removed_cn：读者会误以为没有实验就谈不上解释。

- evidence_pointer：Introduction P4 S7

### 19. Introduction P5 S1

- order：19

- locator：Introduction P5 S1

- paraphrase_cn：本文提出DRQN-attention模型，旨在增强顾客获取RL模型的可解释性，同时保留优化长期奖励的主要目标。

- move_code：ARTIFACT_PROPOSAL

- statement_status：author_inference

- why_here_cn：正式宣告研究目标与制品，是引言的高潮。

- inherits_from_previous_cn：由全部引言铺垫收敛而来。

- changes_argument_state_cn：从问题与缺口转向本文的解决方案。

- sets_up_next_cn：为随后的模型功能定位和技术选择做引导。

- failure_if_removed_cn：引言没有核心主张，全文失去落点。

- evidence_pointer：Introduction P5 S1

### 20. Introduction P5 S2

- order：20

- locator：Introduction P5 S2

- paraphrase_cn：模型的定位是在正确的情境把正确的信息展示给正确的潜在客户，是否申请仍由客户自己决定。

- move_code：ARTIFACT_SCOPE

- statement_status：design_decision

- why_here_cn：界定模型只做信息投放，不干预客户决策，为奖励函数和行动空间设定边界。

- inherits_from_previous_cn：由DRQN-attention的目标推出。

- changes_argument_state_cn：明确了模型的作用边界，避免承诺过多。

- sets_up_next_cn：为‘不展示广告’也是动作选项做铺垫。

- failure_if_removed_cn：模型范围不清，奖励设计和伦理边界会受质疑。

- evidence_pointer：Introduction P5 S2

### 21. Introduction P5 S3

- order：21

- locator：Introduction P5 S3

- paraphrase_cn：模型采用DRQN来建模顾客状态部分可观测的POMDP。

- move_code：THEORY_BASE_1

- statement_status：theory_claim

- why_here_cn：引入DRQN的理论基础：POMDP与RNN。

- inherits_from_previous_cn：为由DRQN-attention目标决定技术路线。

- changes_argument_state_cn：把制品与序列决策中的部分可观测性理论连接。

- sets_up_next_cn：为第4.1节DRQN的形式化做预告。

- failure_if_removed_cn：技术选型DRQN失去理论依据。

- evidence_pointer：Introduction P5 S3

### 22. Introduction P5 S4

- order：22

- locator：Introduction P5 S4

- paraphrase_cn：为了在RL智能体中制造瓶颈并将注意力与模型结合，模型将Q-learning与注意力机制结合。

- move_code：THEORY_BASE_2

- statement_status：design_decision

- why_here_cn：引入第二个技术支柱：Q-learning与注意力结合。

- inherits_from_previous_cn：由DRQN基础进一步推进。

- changes_argument_state_cn：确立了制品的核心架构组合。

- sets_up_next_cn：为第4.2节定制注意力设计做铺垫。

- failure_if_removed_cn：注意力如何进入模型缺少交代。

- evidence_pointer：Introduction P5 S4

### 23. Introduction P5 S5

- order：23

- locator：Introduction P5 S5

- paraphrase_cn：定制注意力机制允许直接观察模型决策所用的信息，使模型比传统RL更可解释。

- move_code：DESIGN_PROMISE

- statement_status：author_inference

- why_here_cn：把技术设计与可解释性承诺直接挂钩。

- inherits_from_previous_cn：承接注意力与Q-learning结合。

- changes_argument_state_cn：确立注意力的可解释功能。

- sets_up_next_cn：为全文可解释性分析提供评价标准。

- failure_if_removed_cn：可解释性主张与技术设计脱节。

- evidence_pointer：Introduction P5 S5

### 24. Introduction P5 S6-S7

- order：24

- locator：Introduction P5 S6-S7

- paraphrase_cn：文章随后按顺序介绍文献综述、实证情境、模型开发、模型评价、联邦学习、注意力机制洞察和渠道选择案例，并在结尾总结。

- move_code：ROADMAP

- statement_status：method_decision

- why_here_cn：给出阅读路径，让读者预期五阶段证据链。

- inherits_from_previous_cn：由制品提出后的自然展开顺序构成。

- changes_argument_state_cn：把论证结构显式化。

- sets_up_next_cn：为正文第2至第8节提供导航。

- failure_if_removed_cn：读者对多阶段分析顺序缺乏预期。

- evidence_pointer：Introduction P5 S6-S7

## 引言逐段图谱

### 1. Introduction P1

- locator：Introduction P1

- opening_move_cn：以‘顾客获取是数字时代企业增长关键’开启话题。

- development_move_cn：用获客成本高、需与客户生命周期价值比较来建立经济利害。

- pivot_move_cn：从‘为什么要获客’转向‘获客成本必须被控制’。

- closing_move_cn：制造对更高效获客策略的需要。

- paragraph_job_cn：确立顾客获取是重要且成本敏感的商业问题。

### 2. Introduction P2

- locator：Introduction P2

- opening_move_cn：以随机实验作为现有评价方法引入。

- development_move_cn：指出现有实验忽略干预互动、序列策略维度爆炸，并引用因果决策文献反驳‘必须精确估计因果效应’。

- pivot_move_cn：从‘实验有局限’转到‘优化不需要因果识别’。

- closing_move_cn：以‘模型方法可行’收束。

- paragraph_job_cn：为放弃随机实验改用以业务结果为导向的模型方法提供方法论辩护。

### 3. Introduction P3

- locator：Introduction P3

- opening_move_cn：引入机器学习作为现有获客策略工具。

- development_move_cn：指出现有监督学习只处理单次干预，但顾客转化需要时间与金钱投入，先前文献已把获客框定为序列决策。

- pivot_move_cn：从‘监督学习不足’转到‘需要序列化决策框架’。

- closing_move_cn：提出探索-利用权衡并引出RL。

- paragraph_job_cn：把顾客获取从单次预测重构为序列决策问题，并引入RL框架。

### 4. Introduction P4

- locator：Introduction P4

- opening_move_cn：列举RL在商业中的成功应用。

- development_move_cn：快速转向黑箱问题，指出企业需要可解释性、缺乏可解释性会降低信任，并引用DARPA与IS学者呼吁。

- pivot_move_cn：从‘RL有用’转到‘RL不透明是障碍’。

- closing_move_cn：界定本文所主张的可解释性不是因果效应而是决策洞察。

- paragraph_job_cn：建立可解释性缺口并界定本文对可解释性的定义。

### 5. Introduction P5

- locator：Introduction P5

- opening_move_cn：正式宣布DRQN-attention模型及其双重目标。

- development_move_cn：界定模型作用边界，并依次选择DRQN处理POMDP、结合注意力机制制造瓶颈。

- pivot_move_cn：从‘模型是什么’转到‘模型如何做到可解释’。

- closing_move_cn：用章节路线图预告全文结构。

- paragraph_job_cn：呈现研究制品、技术路线并给出阅读路径。

## 理论到设计逐句图谱

### 1. Section 2.1 P1 S1-S2

- order：1

- locator：Section 2.1 P1 S1-S2

- paraphrase_cn：RL是优化商业目标的有力工具，在营销中可学习动态自适应策略并平衡探索与利用。

- move_code：LITERATURE_CONTEXT

- statement_status：prior_literature

- why_here_cn：为RL商业应用综述定调。

- inherits_from_previous_cn：承接引言RL框架。

- changes_argument_state_cn：正式进入RL商业决策文献。

- sets_up_next_cn：为MAB到Q-learning的演进提供起点。

- failure_if_removed_cn：RL商业综述缺少开场。

- evidence_pointer：Section 2.1 P1 S1-S2

### 2. Section 2.1 P1 S3-S6

- order：2

- locator：Section 2.1 P1 S3-S6

- paraphrase_cn：MAB是最早的RL模型，能优化CTR，但主要关注即时反馈、不显式建模长期收入；后续研究用Q-learning框架优化序列投放长期收入。

- move_code：LITERATURE_EVOLUTION

- statement_status：prior_literature

- why_here_cn：展示从即时优化到长期优化的文献演进，并自然界定本文的长期收益立场。

- inherits_from_previous_cn：承接RL商业应用综述。

- changes_argument_state_cn：确立了长期收益优化的正当性，并把MAB定位为旧的、短视的基线。

- sets_up_next_cn：为后文MAB作为主要比照基线做铺垫。

- failure_if_removed_cn：MAB与Q-learning的比较失去文献基础。

- evidence_pointer：Section 2.1 P1 S3-S6

### 3. Section 2.1 最后两段 S1-S4

- order：3

- locator：Section 2.1 最后两段 S1-S4

- paraphrase_cn：现有RL商业决策模型大多通过事后分析解释决策，内在可解释RL模型在顾客获取场景几乎没有进展。

- move_code：LITERATURE_GAP

- statement_status：author_inference

- why_here_cn：区分事后解释与内在可解释，明确指出本文填补的缺口。

- inherits_from_previous_cn：承接RL商业应用综述。

- changes_argument_state_cn：把文献综述收束为可解释性缺口。

- sets_up_next_cn：为进入可解释RL文献和本文贡献声明做铺垫。

- failure_if_removed_cn：本文‘内在可解释RL’的定位失去支撑。

- evidence_pointer：Section 2.1 最后两段

### 4. Section 2.1 最后一句

- order：4

- locator：Section 2.1 最后一句

- paraphrase_cn：我们提出一个面向顾客获取的内在可解释RL模型，填补文献空白并满足商业需求。

- move_code：GAP_TO_CONTRIBUTION

- statement_status：contribution_claim

- why_here_cn：将缺口直接转化为贡献声明。

- inherits_from_previous_cn：由缺口陈述推出。

- changes_argument_state_cn：宣告本文在文献中的独特位置。

- sets_up_next_cn：为模型设计和评估提供目标。

- failure_if_removed_cn：文献综述与贡献定位之间断裂。

- evidence_pointer：Section 2.1 最后一句

### 5. Section 2.2 P1 S1-S2

- order：5

- locator：Section 2.2 P1 S1-S2

- paraphrase_cn：RL可解释性困难来自黑箱基础模型和序列化长期优化的设计复杂性。

- move_code：PROBLEM_COMPLEXITY

- statement_status：author_inference

- why_here_cn：解释为什么RL比一般ML更难解释，为注意力机制引入做铺垫。

- inherits_from_previous_cn：承接RL可解释性主题。

- changes_argument_state_cn：把可解释性困难归因到两类来源，为解决方案提供方向。

- sets_up_next_cn：为注意力机制作为解释方案做铺垫。

- failure_if_removed_cn：注意力为何是合理选择缺少理由。

- evidence_pointer：Section 2.2 P1 S1-S2

### 6. Section 2.2 P2 S1-S7

- order：6

- locator：Section 2.2 P2 S1-S7

- paraphrase_cn：注意力机制由query、key、value三部分组成，query指示关注哪些特征，注意力权重大小与输入区域对预测的相关性相关。

- move_code：ATTENTION_THEORY_BASE

- statement_status：prior_literature

- why_here_cn：给出通用注意力框架，为本文定制注意力提供概念语言。

- inherits_from_previous_cn：承接RL可解释性方案讨论。

- changes_argument_state_cn：引入query/key/value术语，后文全部设计都依赖这些概念。

- sets_up_next_cn：为视频游戏注意力RL和定制差异分析做铺垫。

- failure_if_removed_cn：后文定制注意力的全部机制描述失去定义基础。

- evidence_pointer：Section 2.2 P2 S1-S7

### 7. Section 2.2 P3 S1-S4

- order：7

- locator：Section 2.2 P3 S1-S4

- paraphrase_cn：许多注意力RL模型在视频游戏中开发，利用零成本模拟器和结构化的游戏规则解释决策。

- move_code：CONTRAST_BASE

- statement_status：prior_literature

- why_here_cn：建立本文与主流注意力RL的对照：视频游戏环境 vs 顾客获取环境。

- inherits_from_previous_cn：承接注意力RL文献。

- changes_argument_state_cn：界定已有方法的应用场景假设。

- sets_up_next_cn：为三条定制差异做对照。

- failure_if_removed_cn：本文与视频游戏注意力RL的差异失去参照。

- evidence_pointer：Section 2.2 P3 S1-S4

### 8. Section 2.2 三条差异

- order：8

- locator：Section 2.2 三条差异

- paraphrase_cn：与视频游戏注意力RL不同，本文用RNN处理历史交互与静态特征构造query；注意力权重直接作用于原始进入交互特征而非CNN特征图；query由历史与静态信息构造而key/value由当前交互生成。

- move_code：DESIGN_DIFFERENCE

- statement_status：design_decision

- why_here_cn：通过三条差异精确定位本文注意力机制的情境化定制。

- inherits_from_previous_cn：承接视频游戏注意力RL的对比。

- changes_argument_state_cn：把通用注意力机制转化为顾客获取场景的设计。

- sets_up_next_cn：为第4.2节的具体公式和图做预告。

- failure_if_removed_cn：本文技术新颖性没有明确定位。

- evidence_pointer：Section 2.2 三条差异

### 9. Section 2.2 P4

- order：9

- locator：Section 2.2 P4

- paraphrase_cn：注意力RL在其他领域（医疗、NLP、股票交易）也有定制实例。

- move_code：LITERATURE_SURVEY

- statement_status：prior_literature

- why_here_cn：说明注意力定制是普遍可行，增加本文设计的合理性。

- inherits_from_previous_cn：承接注意力机制通用性。

- changes_argument_state_cn：把定制注意力从视频游戏扩展到其他领域。

- sets_up_next_cn：为Table 1总结和‘顾客获取尚无先例’的声明做铺垫。

- failure_if_removed_cn：Table 1缺少比较对象。

- evidence_pointer：Section 2.2 P4

### 10. Section 2.2 最后一段

- order：10

- locator：Section 2.2 最后一段

- paraphrase_cn：据我们所知，尚没有专门针对顾客获取问题的内在可解释RL模型。

- move_code：GAP_CLAIM

- statement_status：author_inference

- why_here_cn：给出本文独特定位的最终声明。

- inherits_from_previous_cn：由所有前人工作对比推出。

- changes_argument_state_cn：文献缺口明确闭合，本文贡献得到锚定。

- sets_up_next_cn：为研究情境和模型设计提供必要性。

- failure_if_removed_cn：本文‘首次’主张失去依据。

- evidence_pointer：Section 2.2 最后一段

### 11. Section 4 P1

- order：11

- locator：Section 4 P1

- paraphrase_cn：将顾客获取形式化为RL问题：智能体与潜在顾客交互，通过动作序列投放广告以优化长期收益。

- move_code：FORMALIZATION

- statement_status：theory_claim

- why_here_cn：把业务问题翻译成RL框架，为所有后续技术内容奠基。

- inherits_from_previous_cn：承接引言和文献的RL框架。

- changes_argument_state_cn：确立状态、动作、奖励的定义域。

- sets_up_next_cn：为状态/动作/奖励的详细定义做铺垫。

- failure_if_removed_cn：所有技术分析失去问题基础。

- evidence_pointer：Section 4 P1

### 12. Section 4 状态动作奖励定义

- order：12

- locator：Section 4 状态动作奖励定义

- paraphrase_cn：状态是交互历史与当前情境；动作是展示某广告或不展示；奖励根据点击、获客和曝光成本确定。

- move_code：DEFINITION

- statement_status：theory_claim

- why_here_cn：给出RL三元组的具体内容，是形式化的核心。

- inherits_from_previous_cn：承接RL形式化。

- changes_argument_state_cn：把抽象RL概念映射到顾客获取的具体元素。

- sets_up_next_cn：为价值函数和Q-learning定义做基础。

- failure_if_removed_cn：后文所有公式和评价没有对应物。

- evidence_pointer：Section 4 状态/动作/奖励定义

### 13. Section 4 P2-P3

- order：13

- locator：Section 4 P2-P3

- paraphrase_cn：RL学习价值函数估计期望累计奖励，因而倾向选择带来最优长期收益的动作。

- move_code：THEORY_PROPOSITION

- statement_status：theory_claim

- why_here_cn：陈述RL的核心命题：用价值函数实现长期收益优化。

- inherits_from_previous_cn：由RL三元组推出。

- changes_argument_state_cn：把‘长期收益’与‘Q值选择’连接。

- sets_up_next_cn：为进入Q-learning和DRQN做铺垫。

- failure_if_removed_cn：Q-learning的必要性没有论证。

- evidence_pointer：Section 4 P2-P3

### 14. Section 4.1 P1-P2

- order：14

- locator：Section 4.1 P1-P2

- paraphrase_cn：Q-learning估计长期累计奖励，DQN用深度网络估计Q值，但其MDP假设在未来状态只依赖最近观测。

- move_code：Q_LEARNING_BASE

- statement_status：theory_claim

- why_here_cn：提供Q-learning与DQN的理论基础，为指出MDP局限做准备。

- inherits_from_previous_cn：承接价值函数定义。

- changes_argument_state_cn：确立Q-learning的长期收益机制。

- sets_up_next_cn：为DRQN的引入做铺垫。

- failure_if_removed_cn：DRQN的技术改进失去对象。

- evidence_pointer：Section 4.1 P1-P2

### 15. Section 4.1 P3-P4

- order：15

- locator：Section 4.1 P3-P4

- paraphrase_cn：MDP假设现实中很少成立，顾客状态难以由最近观测完全描述，POMDP更符合现实；DRQN用RNN处理序列观测以综合状态。

- move_code：POMDP_AND_DRQN_MOTIVATION

- statement_status：theory_claim

- why_here_cn：用POMDP理论论证DRQN的必要性。

- inherits_from_previous_cn：由MDP局限推出。

- changes_argument_state_cn：把顾客获取重新解释为POMDP问题。

- sets_up_next_cn：为第4.1节DRQN的具体结构做铺垫。

- failure_if_removed_cn：DRQN选型失去理论依据。

- evidence_pointer：Section 4.1 P3-P4

### 16. Section 4.1 P5-P6

- order：16

- locator：Section 4.1 P5-P6

- paraphrase_cn：DRQN用GRU处理交互历史得到状态，并加入double Q-learning与dueling架构提高稳定性。

- move_code：DRQN_ARCHITECTURE

- statement_status：method_decision

- why_here_cn：给出DRQN的具体实现细节，为DRQN-attention提供基础架构。

- inherits_from_previous_cn：承接POMDP必要性。

- changes_argument_state_cn：把理论动机落实为可训练架构。

- sets_up_next_cn：为注意力机制的加入提供宿主。

- failure_if_removed_cn：后文注意力设计缺少载体。

- evidence_pointer：Section 4.1 P5-P6

### 17. Section 4.2 P1

- order：17

- locator：Section 4.2 P1

- paraphrase_cn：RL复杂模型通常不解释决策，研究者通过加入解释组件构建内在可解释模型，在保持竞争力的同时实现可解释性。

- move_code：INTRINSIC_EXPLAINABILITY_REQUIREMENT

- statement_status：author_inference

- why_here_cn：把可解释性需求从外部口号化为内部设计原则。

- inherits_from_previous_cn：承接引言可解释性讨论和DRQN架构。

- changes_argument_state_cn：确立本文设计原则：解释组件必须在模型内部。

- sets_up_next_cn：为注意力机制的加入做理论铺垫。

- failure_if_removed_cn：注意力机制的设计目标失去来源。

- evidence_pointer：Section 4.2 P1

### 18. Section 4.2 P2-P3

- order：18

- locator：Section 4.2 P2-P3

- paraphrase_cn：注意力机制可显式加权输入特征，因此可以用来识别模型决策所依赖的特征。

- move_code：ATTENTION_AS_EXPLANATION_TOOL

- statement_status：theory_claim

- why_here_cn：把注意力机制定位为内在可解释的载体。

- inherits_from_previous_cn：承接内在可解释RL研究。

- changes_argument_state_cn：确立了‘注意力权重=决策依据’的论证逻辑。

- sets_up_next_cn：为DRQN-attention的具体设计做铺垫。

- failure_if_removed_cn：注意力权重作为解释证据的合法性缺失。

- evidence_pointer：Section 4.2 P2-P3

### 19. Section 4.2 P4-P7

- order：19

- locator：Section 4.2 P4-P7

- paraphrase_cn：DRQN-attention收集静态特征、历史交互和当前交互one-hot特征；用静态特征与历史交互生成query，用当前交互特征生成key和value，经softmax得到注意力权重并与value相乘得到状态。

- move_code：CUSTOMIZED_ATTENTION_DESIGN

- statement_status：design_decision

- why_here_cn：给出核心制品设计，把可解释性与决策机制直接绑定。

- inherits_from_previous_cn：承接通用注意力框架与DRQN架构。

- changes_argument_state_cn：从‘要加注意力’推进到‘注意力如何构造’。

- sets_up_next_cn：为多头注意力、完全可微性和前向规划性质做铺垫。

- failure_if_removed_cn：全文技术贡献的核心消失。

- evidence_pointer：Section 4.2 P4-P7

### 20. Section 4.2 属性段

- order：20

- locator：Section 4.2 属性段

- paraphrase_cn：模型完全可微可训练；query是静态特征与历史交互的函数，因此注意力机制等价于自动前向规划，主动扫描下一次曝光机会中的特征以优化长期收益。

- move_code：MECHANISM_PROPERTY

- statement_status：theory_claim

- why_here_cn：把设计细节升华为‘前向规划’机制，为第6节的机制验证和第7节渠道案例埋下伏笔。

- inherits_from_previous_cn：由query构造方式和注意力机制推出。

- changes_argument_state_cn：提出全文最核心的理论主张：注意力=前向规划。

- sets_up_next_cn：为第6、7节的证据验证做铺垫。

- failure_if_removed_cn：可解释性缺乏理论表述，后续机制验证失去靶心。

- evidence_pointer：Section 4.2 属性段

## 制品设计理由逐句图谱

### 1. Section 4.2 P1 S1-S2

- order：1

- locator：Section 4.2 P1 S1-S2

- paraphrase_cn：复杂的RL模型通常不解释决策，这是采用障碍；研究者因此增加解释组件构建内在可解释模型。

- move_code：WHY_ADD_EXPLANATION_COMPONENT

- statement_status：author_inference

- why_here_cn：解释为什么要在RL模型中增加解释组件。

- inherits_from_previous_cn：承接引言黑箱采用障碍。

- changes_argument_state_cn：把可解释性从外部要求转化为内部设计需求。

- sets_up_next_cn：为注意力作为解释组件的引入做铺垫。

- failure_if_removed_cn：注意力组件的设计动机丢失。

- evidence_pointer：Section 4.2 P1 S1-S2

### 2. Section 4.2 P2 S1-S3

- order：2

- locator：Section 4.2 P2 S1-S3

- paraphrase_cn：注意力机制模仿人类认知注意，显式加权输入特征，因此可用权重识别模型依赖的特征。

- move_code：WHY_ATTENTION_IS_INTERPRETABLE

- statement_status：theory_claim

- why_here_cn：说明为什么选择注意力而非其他解释手段。

- inherits_from_previous_cn：承接解释组件需求。

- changes_argument_state_cn：确立注意力权重的解释学地位。

- sets_up_next_cn：为注意力机制的具体构造做铺垫。

- failure_if_removed_cn：注意力权重作为解释证据缺乏理论支撑。

- evidence_pointer：Section 4.2 P2 S1-S3

### 3. Section 4.2 P3 S1-S3

- order：3

- locator：Section 4.2 P3 S1-S3

- paraphrase_cn：因为静态特征和历史交互不可变，注意力应动态调整为识别进入交互中的关键特征以优化长期收益。

- move_code：QUERY_SOURCE_RATIONALE

- statement_status：design_decision

- why_here_cn：解释为什么query来自静态+历史、key/value来自当前交互。

- inherits_from_previous_cn：承接通用注意力框架。

- changes_argument_state_cn：把注意力定制原则具体化为数据来源分工。

- sets_up_next_cn：为四种数据输入和one-hot编码的设计做铺垫。

- failure_if_removed_cn：attention设计的核心差异失去理由。

- evidence_pointer：Section 4.2 P3 S1-S3

### 4. Section 4.2 P4 S1-S4

- order：4

- locator：Section 4.2 P4 S1-S4

- paraphrase_cn：当前交互特征用one-hot编码表示，因为它是注意力权重要作用的目标，one-hot使注意力权重可解释。

- move_code：ONE_HOT_RATIONALE

- statement_status：design_decision

- why_here_cn：解释为什么用one-hot编码，直接为可解释性服务。

- inherits_from_previous_cn：承接当前交互特征作为key/value。

- changes_argument_state_cn：确立了注意力权重与特征一一对应的可解释基础。

- sets_up_next_cn：为第6节将注意力权重与one-hot特征匹配分析做铺垫。

- failure_if_removed_cn：注意力权重无法直接映射到现实特征，可解释性主张落空。

- evidence_pointer：Section 4.2 P4 S1-S4

### 5. Section 4.2 P5-P8

- order：5

- locator：Section 4.2 P5-P8

- paraphrase_cn：query与key内积并经softmax生成注意力权重，权重与value相乘得到query答案，多组head与query共同生成状态表示。

- move_code：ATTENTION_COMPUTATION

- statement_status：design_decision

- why_here_cn：给出注意力计算路径，使设计可复现。

- inherits_from_previous_cn：承接query/key/value构造。

- changes_argument_state_cn：把设计思想转化为可实现的网络计算。

- sets_up_next_cn：为状态生成和Q值预测做铺垫。

- failure_if_removed_cn：模型无法训练，后续评估失去对象。

- evidence_pointer：Section 4.2 P5-P8

### 6. Section 4.2 属性段 S1

- order：6

- locator：Section 4.2 属性段 S1

- paraphrase_cn：模型完全可微，所有参数可通过反向传播最小化损失函数训练。

- move_code：TRAINABILITY_RATIONALE

- statement_status：design_decision

- why_here_cn：保证制品的可训练性，排除‘不可用玩具模型’的质疑。

- inherits_from_previous_cn：由注意力嵌入Q-learning框架推出。

- changes_argument_state_cn：确定模型工程上的可行性。

- sets_up_next_cn：为后文真实数据训练做技术铺垫。

- failure_if_removed_cn：模型不能训练，实证分析无法进行。

- evidence_pointer：Section 4.2 属性段 S1

### 7. Section 4.2 属性段 S2

- order：7

- locator：Section 4.2 属性段 S2

- paraphrase_cn：query是静态特征与历史交互的函数，这形成自动前向规划：主动查询下一次曝光机会中的特征以优化长期奖励。

- move_code：FORWARD_PLANNING_RATIONALE

- statement_status：theory_claim

- why_here_cn：把query构造方式升华为机制主张，解释为什么注意力会产生长期导向。

- inherits_from_previous_cn：由query来源设计推出。

- changes_argument_state_cn：提出全文核心机制假设：注意力=前向规划。

- sets_up_next_cn：为第6节注意力与关联规则的对比和第7节渠道案例做理论铺垫。

- failure_if_removed_cn：全文的理论贡献失去了核心机制表述。

- evidence_pointer：Section 4.2 属性段 S2

## Study开头、过渡与收束图谱

### 1. Section 5.1 opening

- order：1

- locator：Section 5.1 opening

- paraphrase_cn：描述50,000名潜在客户、静态特征、点击流收集方式和上下文特征。

- move_code：STUDY_OPENING

- statement_status：fact

- why_here_cn：建立模型评估的数据基础。

- inherits_from_previous_cn：承接模型提出后的评价需要。

- changes_argument_state_cn：从模型设计进入实证检验。

- sets_up_next_cn：为奖励校准和基准比较做铺垫。

- failure_if_removed_cn：评价结果没有数据依托。

- evidence_pointer：Section 5.1 P1-P3

### 2. Section 5.1 reward calibration paragraph

- order：2

- locator：Section 5.1 reward calibration paragraph

- paraphrase_cn：以银行实际成本收益校准曝光、点击和获客奖励。

- move_code：REWARD_CALIBRATION_RATIONALE

- statement_status：method_decision

- why_here_cn：保证离线评价的奖励与现实收入一致。

- inherits_from_previous_cn：承接数据描述。

- changes_argument_state_cn：使AR指标具有货币含义。

- sets_up_next_cn：为Table 3的AR比较提供基础。

- failure_if_removed_cn：AR数值无法解释其经济意义。

- evidence_pointer：Section 5.1 reward paragraph

### 3. Section 5.2 opening and benchmark list

- order：3

- locator：Section 5.2 opening and benchmark list

- paraphrase_cn：随机划分训练与留出样本，用Fixed-M PERS离策略评估，并与六个基准模型比较。

- move_code：EVALUATION_DESIGN

- statement_status：method_decision

- why_here_cn：说明评价方法并让每个基线扮演不同对照角色。

- inherits_from_previous_cn：承接数据与奖励设定。

- changes_argument_state_cn：把模型评价从口号变为可操作程序。

- sets_up_next_cn：为Table 3结果报告铺路。

- failure_if_removed_cn：结果没有方法支撑，无法判断优劣。

- evidence_pointer：Section 5.2 opening

### 4. Section 5.2 observations after Table 3

- order：4

- locator：Section 5.2 observations after Table 3

- paraphrase_cn：观察(1)MAB在H=1最好但Q-learning在H=3、6超越；(2)DRQN和DRQN-attention优于DQN；(3)DRQN-attention与DRQN无显著差异；(4)(5)(6)其他注意力设计在顾客获取中表现不佳。

- move_code：RESULT_INTERPRETATION

- statement_status：empirical_result

- why_here_cn：逐条解读表格，把数字转成可维护的论证。

- inherits_from_previous_cn：承接Table 3。

- changes_argument_state_cn：每个观察分别证明长期收益需要Q-learning、历史交互需要DRQN、注意力不损失性能、本文注意力定制优于替代设计。

- sets_up_next_cn：为总结DRQN-attention性能优势做铺垫。

- failure_if_removed_cn：表格本身不能自动产生论证意义。

- evidence_pointer：Section 5.2 observations (1)-(6)

### 5. Section 5.2 closing paragraph

- order：5

- locator：Section 5.2 closing paragraph

- paraphrase_cn：截至H=6，DRQN-attention超过公司现行政策和多数RL算法，证明其在顾客获取中的有效性。

- move_code：STUDY_CLOSURE

- statement_status：contribution_claim

- why_here_cn：收束第5.2节，给出性能层面的结论。

- inherits_from_previous_cn：由观察结果总结。

- changes_argument_state_cn：把性能结果转化为制品有效性的总claim。

- sets_up_next_cn：为第5.3节隐私敏感部署问题做过渡。

- failure_if_removed_cn：性能阶段的论证没有结论。

- evidence_pointer：Section 5.2 closing

### 6. Section 5.3 opening

- order：6

- locator：Section 5.3 opening

- paraphrase_cn：隐私监管趋严，顾客数据保护成全球趋势，应考虑防止数据泄漏。

- move_code：NEW_PROBLEM_OPENING

- statement_status：prior_literature

- why_here_cn：引入一个未被性能分析覆盖的部署约束。

- inherits_from_previous_cn：承接性能验证后的外部有效性需要。

- changes_argument_state_cn：把评价从‘是否更优’扩展到‘能否在隐私环境部署’。

- sets_up_next_cn：为联邦学习引入做铺垫。

- failure_if_removed_cn：联邦学习评价显得多余。

- evidence_pointer：Section 5.3 P1

### 7. Section 5.3 federated learning rationale and result

- order：7

- locator：Section 5.3 federated learning rationale and result

- paraphrase_cn：采用联邦RL，数据留在本地只交换模型更新；结果显示联邦版与原始版性能接近。

- move_code：ROBUSTNESS_TEST

- statement_status：empirical_result

- why_here_cn：用同一评价程序验证隐私增强版性能。

- inherits_from_previous_cn：承接隐私问题提出。

- changes_argument_state_cn：确立了制品在隐私敏感条件下的部署可行性。

- sets_up_next_cn：为从性能转向可解释性分析做过渡。

- failure_if_removed_cn：‘可广泛应用’的主张缺少隐私场景支持。

- evidence_pointer：Section 5.3 P2-P3, Table 4

### 8. Section 6 opening

- order：8

- locator：Section 6 opening

- paraphrase_cn：虽然注意力图不能囊括全部决策过程，但能提供模型学到的策略洞见；本节探索注意力权重捕捉了什么。

- move_code：MECHANISM_STUDY_OPENING

- statement_status：author_inference

- why_here_cn：正式从性能阶段转向机制分析阶段。

- inherits_from_previous_cn：承接前文注意力权重定义。

- changes_argument_state_cn：把评价重点从‘是否更优’转向‘为何有效’。

- sets_up_next_cn：为匹配/未匹配分组分析做铺垫。

- failure_if_removed_cn：可解释性从性能结果到机制验证之间的过渡缺失。

- evidence_pointer：Section 6 P1

### 9. Section 6 matched/unmatched design explanation

- order：9

- locator：Section 6 matched/unmatched design explanation

- paraphrase_cn：因为f是one-hot编码，高注意力权重元素对应的特征若实际为1，则说明模型关注了该特征；据此把交互分为匹配组与未匹配组。

- move_code：GROUPING_METHOD

- statement_status：method_decision

- why_here_cn：给出可操作的验证程序，把抽象注意力权重转成可比较的组别。

- inherits_from_previous_cn：承接注意力权重定义和one-hot编码设计。

- changes_argument_state_cn：为注意力权重的解释力提供统计上可比较的方案。

- sets_up_next_cn：为Table 5的匹配/未匹配结果做铺垫。

- failure_if_removed_cn：无法检验注意力权重是否与更高收益相关。

- evidence_pointer：Section 6 P2

### 10. Section 6 association rule comparison rationale

- order：10

- locator：Section 6 association rule comparison rationale

- paraphrase_cn：若只是想识别高收益特征，更简单的方法是关联规则；用关联规则作对照可检验注意力是否只是捕捉即时关联。

- move_code：ALTERNATIVE_EXPLANATION_CONTROL

- statement_status：method_decision

- why_here_cn：通过简单基线排除‘注意力=即时相关’的替代解释。

- inherits_from_previous_cn：承接注意力匹配组结果。

- changes_argument_state_cn：把机制主张的检验升级为竞争性假设检验。

- sets_up_next_cn：为Table 5第三行对比做铺垫。

- failure_if_removed_cn：‘前向规划’主张缺少最强竞争解释的排除。

- evidence_pointer：Section 6 P3

### 11. Section 6 closing

- order：11

- locator：Section 6 closing

- paraphrase_cn：关联规则在AR@1略高但在更长幕中低于注意力匹配组；注意力机制扫描可能的未来路径并选择最有前景的最优路径。

- move_code：MECHANISM_CLAIM_CLOSE

- statement_status：empirical_result

- why_here_cn：把对比结果收束为‘前向规划’的核心机制结论。

- inherits_from_previous_cn：由Table 5对比推出。

- changes_argument_state_cn：把可解释性从‘权重与高收益相关’升级为‘注意力面向长期最优轨迹’。

- sets_up_next_cn：为第7节把机制转成渠道决策做铺垫。

- failure_if_removed_cn：核心理论贡献失去证据闭环。

- evidence_pointer：Section 6 P4

### 12. Section 7 opening

- order：12

- locator：Section 7 opening

- paraphrase_cn：本节探索注意力机制如何选择广告渠道，通过三个案例说明其如何规划最优广告曝光路径。

- move_code：MANAGERIAL_STUDY_OPENING

- statement_status：author_inference

- why_here_cn：从机制验证转向管理洞察展示。

- inherits_from_previous_cn：承接前向规划机制。

- changes_argument_state_cn：把技术机制转化为管理者可操作的知识。

- sets_up_next_cn：为三个案例和MIF/奇异特征定义做铺垫。

- failure_if_removed_cn：IS论文的管理价值部分缺失。

- evidence_pointer：Section 7 P1

### 13. Section 7 MIF and singular features definition

- order：13

- locator：Section 7 MIF and singular features definition

- paraphrase_cn：定义最重要特征（在top 10中频率超过80百分位的26个特征）和奇异特征（某次注意力top 10中非MIF者）。

- move_code：CONCEPT_TOOL_DEFINITION

- statement_status：method_decision

- why_here_cn：为案例中提取特征模式提供分析工具。

- inherits_from_previous_cn：承接注意力权重数据结构。

- changes_argument_state_cn：把注意力权重转化为可描述的模式语言。

- sets_up_next_cn：为三个案例的top特征表做铺垫。

- failure_if_removed_cn：案例特征描述缺乏统一口径。

- evidence_pointer：Section 7 P2

### 14. Section 7.1 case 1

- order：14

- locator：Section 7.1 case 1

- paraphrase_cn：IT、金融法律、教育行业的注意力奇异特征不同，模型能按行业特征选择不同广告渠道和地点。

- move_code：CASE_EXAMPLE

- statement_status：empirical_result

- why_here_cn：第一个案例证明注意力包含可解释的行业定向模式。

- inherits_from_previous_cn：承接奇异特征概念。

- changes_argument_state_cn：确立‘模型能按行业学习渠道’的经验事实。

- sets_up_next_cn：为其他案例和最终匹配/未匹配验证做铺垫。

- failure_if_removed_cn：管理洞察的第一个支柱缺失。

- evidence_pointer：Section 7.1 P1, Table 6

### 15. Section 7.2 case 2

- order：15

- locator：Section 7.2 case 2

- paraphrase_cn：当用户在LiveStream1多次曝光未点击时其不再进入top特征；当用户在CCTV1点击后CCTV1与Trans1进入top特征。

- move_code：CASE_EXAMPLE

- statement_status：empirical_result

- why_here_cn：第二个案例证明模型能根据动态行为调整渠道并跨渠道协同。

- inherits_from_previous_cn：承接MIF与奇异特征分析工具。

- changes_argument_state_cn：确立‘模型能响应动态行为’的经验事实。

- sets_up_next_cn：为跨渠道协调管理建议做铺垫。

- failure_if_removed_cn：动态调整渠道洞察失去证据。

- evidence_pointer：Section 7.2 P1, Table 7

### 16. Section 7.3 case 3

- order：16

- locator：Section 7.3 case 3

- paraphrase_cn：农业企业家在prepeak与peak阶段的注意力特征不同，peak阶段转向金融保险地点和金融新闻App。

- move_code：CASE_EXAMPLE

- statement_status：empirical_result

- why_here_cn：第三个案例证明模型能学习行业季节性。

- inherits_from_previous_cn：承接前三案例结构。

- changes_argument_state_cn：确立‘模型能对季节调整渠道’的经验事实。

- sets_up_next_cn：为管理者的两项业务行动（监控行业趋势、定制产品）做铺垫。

- failure_if_removed_cn：季节性渠道洞察缺失。

- evidence_pointer：Section 7.3 P1-P2, Table 8

### 17. Section 7 validation paragraph

- order：17

- locator：Section 7 validation paragraph

- paraphrase_cn：借鉴Allen et al.对可解释ML的验证策略，在训练集生成解释，在测试集用匹配/未匹配比较平均奖励验证洞察。

- move_code：VALIDATION_METHOD

- statement_status：method_decision

- why_here_cn：防止案例洞察只是训练集上的启发性描述，提升外部有效性。

- inherits_from_previous_cn：承接三个案例得到的渠道推荐。

- changes_argument_state_cn：把案例洞察从描述升级为可检验结论。

- sets_up_next_cn：为Table 9匹配/未匹配结果做铺垫。

- failure_if_removed_cn：案例洞察缺少在留出集上的验证。

- evidence_pointer：Section 7 validation paragraph

### 18. Section 7 closing after Table 9

- order：18

- locator：Section 7 closing after Table 9

- paraphrase_cn：七个案例中匹配组平均奖励几乎都高于未匹配组，验证了三类渠道洞察在测试集上有效。

- move_code：CASE_VALIDATION_RESULT

- statement_status：empirical_result

- why_here_cn：提供外部有效性证据，证明三个案例洞察不只基于训练集。

- inherits_from_previous_cn：由测试集匹配/未匹配比较推出。

- changes_argument_state_cn：把管理洞察从‘有趣’提升为‘有效’。

- sets_up_next_cn：为结论中的贡献总结做铺垫。

- failure_if_removed_cn：案例洞察的外部有效性没有证明。

- evidence_pointer：Section 7, Table 9

## 讨论与贡献逐句图谱

### 1. Conclusion P1 S1

- order：1

- locator：Conclusion P1 S1

- paraphrase_cn：本文引入DRQN-attention模型，目标是优化顾客获取长期收益并为模型决策提供有意义的解释。

- move_code：CONTRIBUTION_RESTATEMENT

- statement_status：contribution_claim

- why_here_cn：结论开篇重述制品与双重目标，回扣引言。

- inherits_from_previous_cn：由全文证据链收束。

- changes_argument_state_cn：把两个目标确定为本文最终贡献。

- sets_up_next_cn：为性能与可解释性双优势的总结做铺垫。

- failure_if_removed_cn：结论没有主贡献声明。

- evidence_pointer：Conclusion P1 S1

### 2. Conclusion P1 S2-S4

- order：2

- locator：Conclusion P1 S2-S4

- paraphrase_cn：实证显示模型长期收益高于现有RL模型，并能识别重要特征、指导渠道选择、提供直观解释，因此具有良好可解释性和适用性，可广泛应用于顾客获取。

- move_code：CONTRIBUTION_SUMMARY

- statement_status：contribution_claim

- why_here_cn：把性能结果、机制结果和案例结果压缩为总体贡献声明。

- inherits_from_previous_cn：由所有实证章节推出。

- changes_argument_state_cn：确立‘可广泛使用’的总体主张。

- sets_up_next_cn：为局限的承认做对照。

- failure_if_removed_cn：全文的贡献不知道在哪里集中表述。

- evidence_pointer：Conclusion P1 S2-S4

### 3. Conclusion P1 S5

- order：3

- locator：Conclusion P1 S5

- paraphrase_cn：本研究为寻求改进顾客获取的数字企业提供了有价值工具。

- move_code：PRACTICAL_SIGNIFICANCE

- statement_status：contribution_claim

- why_here_cn：明确面向实践的价值主张。

- inherits_from_previous_cn：承接适用性主张。

- changes_argument_state_cn：把贡献对象扩展到数字企业用户。

- sets_up_next_cn：为应用场景的进一步描述做铺垫。

- failure_if_removed_cn：实践价值主张缺失。

- evidence_pointer：Conclusion P1 S5

### 4. Conclusion P2 S1-S2

- order：4

- locator：Conclusion P2 S1-S2

- paraphrase_cn：模型擅长学习长期收益策略并揭示注意力权重，但注意力权重本身不像决策树那样直接可解释，需要额外分组与比较才能学习目标模式。

- move_code：LIMITATION_ACKNOWLEDGEMENT

- statement_status：author_inference

- why_here_cn：诚实地界定可解释性的类型边界，防止过度承诺。

- inherits_from_previous_cn：承接贡献声明。

- changes_argument_state_cn：把‘可解释’限定为‘需要后处理的注意力洞察’。

- sets_up_next_cn：为直接学习模式的研究方向做铺垫。

- failure_if_removed_cn：论文会被批评把注意力权重等同于直接解释。

- evidence_pointer：Conclusion P2 S1-S2

### 5. Conclusion P2 S3-S4

- order：5

- locator：Conclusion P2 S3-S4

- paraphrase_cn：数据可能未完全覆盖状态动作空间，因此策略未必全局最优；若在on-policy环境运行，可采用Boltzmann探索等方法改进策略并更新洞察。

- move_code：BOUNDARY_AND_FUTURE

- statement_status：author_inference

- why_here_cn：承认离线评价与数据覆盖的限制，并给出on-policy改进方向。

- inherits_from_previous_cn：由经验数据与评价方法推出。

- changes_argument_state_cn：把结果限定在离线数据支持范围内。

- sets_up_next_cn：为公平性和跨平台应用方向做铺垫。

- failure_if_removed_cn：全局最优或离线结果会被误读为已证明。

- evidence_pointer：Conclusion P2 S3-S4

### 6. Conclusion P2 S5

- order：6

- locator：Conclusion P2 S5

- paraphrase_cn：未来可把公平性视角纳入模型，在优化长期收益同时确保营销信息公平传递。

- move_code：FUTURE_RESEARCH

- statement_status：author_inference

- why_here_cn：引入伦理维度，填补当前模型未处理公平性的边界。

- inherits_from_previous_cn：由模型目标与当前局限推出。

- changes_argument_state_cn：把研究议程扩展到规范性问题。

- sets_up_next_cn：为最后一个跨平台适用性方向做铺垫。

- failure_if_removed_cn：公平性缺口未被承认。

- evidence_pointer：Conclusion P2 S5

### 7. Conclusion P2 S6

- order：7

- locator：Conclusion P2 S6

- paraphrase_cn：DRQN-attention是可用于用户/顾客获取最优序列干预策略的通用方案，不依赖跨App跟踪，可扩展到单一App内的序列消息。

- move_code：GENERALIZABILITY_CLAIM

- statement_status：contribution_claim

- why_here_cn：最后把贡献从数字银行场景抽象为通用顾客获取方案。

- inherits_from_previous_cn：承接模型一般性设计和联邦学习可部署性。

- changes_argument_state_cn：把应用边界扩展到不需要跨App跟踪的场景。

- sets_up_next_cn：无，文章到此收束。

- failure_if_removed_cn：IS论文的通用设计知识主张被削弱。

- evidence_pointer：Conclusion P2 S6

## Study累积逻辑

### 1. 1

- study_or_phase：阶段1：RL问题形式化与DRQN-attention制品构建

- evidence_job_cn：证明该顾客获取问题可以被表达为RL问题，并且设计出的DRQN-attention具有可训练性和内在可解释性组件。

- what_it_establishes_cn：建立状态、动作、奖励三元组；给出DRQN处理POMDP的架构；给出定制注意力机制如何让注意力权重直接映射到one-hot特征。

- what_it_cannot_establish_cn：不能证明模型在实际数据上优于现有方法；不能证明注意力权重确实捕捉到高收益特征。

- why_next_phase_is_needed_cn：形式化与设计只保证‘可以构建’，需要真实数据证明‘是否更优’。

- transition_wording_function_cn：第5节‘Empirical Analysis’以数据与评价方式承接模型，把‘我们提出’转成‘我们验证’。

### 2. 2

- study_or_phase：阶段2：离策略基准评价

- evidence_job_cn：证明DRQN-attention在长期收益优化上优于公司现有系统与多数SOTA RL方法。

- what_it_establishes_cn：MAB在H=1最好但Q-learning在H=3、6超越；DRQN类优于DQN；DRQN-attention与DRQN无显著差异且优于其他注意力设计。

- what_it_cannot_establish_cn：不能证明可解释性内容的实际含义；不能证明隐私敏感环境下可用。

- why_next_phase_is_needed_cn：性能优势只回答‘是否更优’，还需验证部署约束与解释机制。

- transition_wording_function_cn：第5.3节以隐私监管趋势开头，把评价从性能转向部署。

### 3. 3

- study_or_phase：阶段3：联邦学习鲁棒性评价

- evidence_job_cn：证明模型在隐私敏感设定下仍保持服务质量。

- what_it_establishes_cn：联邦版各模型与原始版性能接近，只有微小下降。

- what_it_cannot_establish_cn：不能揭示注意力权重捕捉什么；联邦学习的安全性只部分讨论。

- why_next_phase_is_needed_cn：只有‘可部署’还不够，还要回答‘为什么可解释’。

- transition_wording_function_cn：第6节开头用‘注意力图虽不涵盖全部决策但可提供洞见’把读者从性能引向机制。

### 4. 4

- study_or_phase：阶段4：注意力权重作为前向规划的机制验证

- evidence_job_cn：证明注意力权重识别的是带来更高长期收益的特征，而非即时关联。

- what_it_establishes_cn：匹配组平均奖励高于未匹配组；注意力在长幕中超过关联规则匹配组；注意力权重与关联规则高相关但长期结果不同。

- what_it_cannot_establish_cn：不能说明注意力如何转成具体的广告渠道选择。

- why_next_phase_is_needed_cn：机制验证证明了‘可解释性在统计上有效’，还需要展示‘解释对管理者意味着什么’。

- transition_wording_function_cn：第7节开头用‘如何选择广告渠道’把机制主张转成渠道选择案例分析。

### 5. 5

- study_or_phase：阶段5：广告渠道选择案例分析及测试集验证

- evidence_job_cn：把前向规划机制转化为管理者可用的渠道定向洞察，并在留出测试集上验证。

- what_it_establishes_cn：模型能按行业选择渠道、按动态行为调整渠道、按农业季节调整渠道；测试集匹配组平均奖励普遍高于未匹配组。

- what_it_cannot_establish_cn：不能证明在线on-policy策略的真实表现；不能证明注意力权重具有因果解释力。

- why_next_phase_is_needed_cn：这些未决问题被收束到结论中的局限与未来研究。

- transition_wording_function_cn：第8节结论用‘我们引入…’把案例洞察收拢为最终贡献并承认边界。

## 主张—证据台账

### 1. DRQN-attention在长期收益优化上超过公司现有系统和多数RL基准

- claim_cn：DRQN-attention在长期收益优化上超过公司现有系统和多数RL基准

- claim_level：technical

- supporting_evidence_cn：Table 3中DRQN-attention AR@6为0.3999，超过MAB的0.3406和大多数基准；与DRQN无显著差异且显著优于MAB。

- support_strength：direct

- where_claim_is_made：Section 5.2 closing; Abstract P3 S2

- where_evidence_is_provided：Section 5.2 Table 3 and observations

### 2. 注意力机制不牺牲模型性能

- claim_cn：注意力机制不牺牲模型性能

- claim_level：technical

- supporting_evidence_cn：DRQN-attention与DRQN平均奖励差异不显著p=0.708。

- support_strength：direct

- where_claim_is_made：Section 5.2 observation (3)

- where_evidence_is_provided：Section 5.2 Table 3

### 3. 替代注意力设计（I-DQN、ST-ADRQN）在顾客获取中更差，说明本文注意力定制更适合该场景

- claim_cn：替代注意力设计（I-DQN、ST-ADRQN）在顾客获取中更差，说明本文注意力定制更适合该场景

- claim_level：artifact

- supporting_evidence_cn：Table 3显示I-DQN AR@6=0.3789、ST-ADRQN AR@6=0.3628，均低于DRQN-attention的0.3999。

- support_strength：direct

- where_claim_is_made：Section 5.2 observations (4)-(5)

- where_evidence_is_provided：Section 5.2 Table 3

### 4. 联邦学习下模型性能几乎不受影响，可在隐私敏感设定可用

- claim_cn：联邦学习下模型性能几乎不受影响，可在隐私敏感设定可用

- claim_level：artifact

- supporting_evidence_cn：Table 4联邦版DRQN-attention AR@6=0.3892，与Table 3的0.3999接近，只有微小下降。

- support_strength：direct

- where_claim_is_made：Section 5.3 conclusion

- where_evidence_is_provided：Section 5.3 Table 4

### 5. 注意力权重识别的是面向长期收益的特征而非即时关联

- claim_cn：注意力权重识别的是面向长期收益的特征而非即时关联

- claim_level：mechanism

- supporting_evidence_cn：Table 5中注意力匹配组AR@3=0.2298、AR@6=0.4815，高于关联规则匹配组的0.1939和0.3946；注意力匹配组在AR@1低于关联规则匹配组。

- support_strength：direct

- where_claim_is_made：Section 6 P4

- where_evidence_is_provided：Section 6 Table 5

### 6. 注意力机制相当于前向规划，扫描未来路径并选择有前途的最优路径

- claim_cn：注意力机制相当于前向规划，扫描未来路径并选择有前途的最优路径

- claim_level：theory

- supporting_evidence_cn：注意力匹配组长期奖励更高、超出关联规则即时匹配，且query由固定历史与静态信息构造。

- support_strength：partial

- where_claim_is_made：Section 6 P4; Abstract P3 S3

- where_evidence_is_provided：Section 6 Table 5; Section 4.2 属性段

### 7. 模型能按行业选择最优广告渠道

- claim_cn：模型能按行业选择最优广告渠道

- claim_level：mechanism

- supporting_evidence_cn：Table 6显示IT、金融法律、教育行业各自的奇异特征不同。

- support_strength：direct

- where_claim_is_made：Section 7.1

- where_evidence_is_provided：Section 7.1 Table 6

### 8. 模型能根据动态顾客行为调整渠道，并发现跨渠道协同

- claim_cn：模型能根据动态顾客行为调整渠道，并发现跨渠道协同

- claim_level：mechanism

- supporting_evidence_cn：Table 7显示LiveStream1多次曝光未点击后退出top特征；CCTV1点击后CCTV1与Trans1进入top特征。

- support_strength：direct

- where_claim_is_made：Section 7.2

- where_evidence_is_provided：Section 7.2 Table 7

### 9. 模型能学习行业季节性并相应调整广告渠道

- claim_cn：模型能学习行业季节性并相应调整广告渠道

- claim_level：mechanism

- supporting_evidence_cn：Table 8显示农业企业家在prepeak与peak阶段的奇异特征不同。

- support_strength：direct

- where_claim_is_made：Section 7.3

- where_evidence_is_provided：Section 7.3 Table 8

### 10. 从注意力权重得到的渠道洞察在留出测试集上有效

- claim_cn：从注意力权重得到的渠道洞察在留出测试集上有效

- claim_level：boundary

- supporting_evidence_cn：Table 9显示七个案例中匹配组AR@1、AR@3、AR@6几乎全部高于未匹配组。

- support_strength：direct

- where_claim_is_made：Section 7 validation paragraph

- where_evidence_is_provided：Section 7 Table 9

### 11. 模型具有良好可解释性和适用性，可广泛应用于顾客获取

- claim_cn：模型具有良好可解释性和适用性，可广泛应用于顾客获取

- claim_level：design_knowledge

- supporting_evidence_cn：综合Table 3、4、5、9以及三个案例；但单一数据源和离线评估不支持‘广泛应用’。

- support_strength：asserted

- where_claim_is_made：Conclusion P1 S4

- where_evidence_is_provided：Section 5-7 综合证据

### 12. 注意力权重可提供不亚于后验解释的洞见

- claim_cn：注意力权重可提供不亚于后验解释的洞见

- claim_level：theory

- supporting_evidence_cn：正文仅提示与后验可解释模型对比在Online Appendix G。

- support_strength：partial

- where_claim_is_made：Section 7 closing

- where_evidence_is_provided：Online Appendix G（不在主文中）

## ISR定位逻辑

- constitutive_is_problem_cn：文章把顾客获取重新表述为一个数字平台上的信息投放与用户响应互相构成的问题：企业不断投放广告消息，用户通过点击、申请等行为反馈状态，下一轮投放又依赖这些反馈。顾客获取不是一次性转化决策，而是数字渠道中的序列化、跨平台、长期导向的决策过程。

- technology_behavior_or_market_entanglement_cn：技术制品（DRQN-attention）与用户行为深度纠缠：模型不仅预测用户行为，还会改变其后续曝光机会；用户的静态特征、历史交互和动态行为反过来决定注意力权重如何选择下一个渠道。作者用CCTV1点击后Trans1成为top特征说明跨渠道协同，用LiveStream1多次曝光未点击后退出top特征说明模型自动避免无效渠道，从而展示技术与用户行为在反馈回路中共构。

- role_of_benchmark_or_objective_evidence_cn：离策略评价和AR指标不是单纯证明‘算法更好’，而是支持三个IS主张：(1) 长期收益优化优于公司现用CTR优化的MAB，说明以最终客户获取而非中间点击为目标的价值；(2) 联邦学习下性能几乎不降，支持隐私保护与商业目标的可兼容性；(3) 通过匹配/未匹配和关联规则对比，客观证据支持‘注意力权重=前向规划’这一关于决策机制的主张。

- theory_in_design_cn：理论不是事后解释结果，而是直接进入设计：POMDP理论决定用DRQN处理历史交互；注意力机制的可解释性理论决定用one-hot特征使权重可映射；‘query由固定历史与静态信息构造’直接由顾客获取场景中静态与历史不可变、当前交互可变推出，从而在模型结构层面就预设了‘前向规划’机制。理论的每个要素都对应一个设计决定，并在后续评价中被检验。

- technical_vs_is_contribution_balance_cn：技术细节（注意力query/key/value构造、DRQN、离策略评估、联邦学习）约占全文一半篇幅，但另一半给了行为洞察和管理应用：三个渠道案例、匹配/未匹配验证、注意力与关联规则的比较、管理者可用的渠道选择与季节性洞察。作者把技术性能结果最终转译为对管理者决策有价值的渠道选择知识，而不仅是算法精度。

- beyond_transient_performance_cn：文章不止报告一时的离线性能优势，而是把结果升级为可复用设计知识：注意力权重可作为‘前向规划’机制观察模型决策；注意力与one-hot输入的绑定使模型具备内在可解释性；匹配/未匹配和关联规则对比提供了验证解释有效性的通用方法；三类案例分析说明模型可以发现的渠道洞察类型。这些主张面向‘如何设计与验证内在可解释RL’的方法论知识，而非某个时间点的分数优势。

## 段落级仿写模板

### abstract_steps

1. 第1句：用领域公认事实建立背景，并点出核心过程机制。

2. 第2句：把背景与业务目标（长期收入）挂钩。

3. 第3句：引入主流技术框架（RL）并承认其潜力。

4. 第4句：给出该框架的关键缺陷（黑箱）。

5. 第5句：宣告本文制品及双重目标。

6. 第6句：用一句话解释制品的核心机制设计。

7. 第7句：给出数据来源。

8. 第8句：给出主要实证结论（既能又优）。

9. 第9句：把结果升华为机制主张（如‘前向规划’）。

10. 第10句：列出可操作的管理洞察类型。

### introduction_paragraph_steps

1. P1：以领域大背景开启，用成本或市场规模建立利害关系。

2. P2：介绍黄金标准方法，指出其在核心问题上的结构性局限，并引用方法论文献为替代方案辩护，最后转向模型方法。

3. P3：介绍现有技术路线，指出其假设与现象不符，用真实消费特征说明必须序列化，最后引入RL的探索-利用框架。

4. P4：列举技术框架的成功应用，随即指出其普遍缺陷，把缺陷后果与企业采用绑定，用机构与学科呼声增强正当性，并界定本文可解释性的含义。

5. P5：正式公布制品与目标，界定制品作用边界，给出两个理论基础，并把设计承诺与可解释性挂钩，最后用路线图结束。

### theory_to_design_steps

1. 先综述主流方法及其演进，让长期收益优化成为自然立场。

2. 用‘事后解释 vs 内在可解释’的二分把文献缺口收紧。

3. 引入制品的核心组件（如注意力机制）并给出通用框架。

4. 用场景差异（如视频游戏 vs 顾客获取）产生定制点。

5. 逐条列出与既有设计的差异，解释每条差异源于什么问题特性。

6. 宣称文献空白并宣布本文填补方式。

7. 把业务问题形式化为理论框架（如RL三元组）。

8. 由理论局限（如MDP）推出架构选择（如DRQN）。

9. 由可解释性需求推出解释组件（如注意力），并落实为具体数据流和公式。

10. 把设计中的某个性质升华为机制主张，为后续检验做好铺垫。

### method_and_study_sequence_steps

1. 先描述数据来源和业务背景，让数据有现实意义。

2. 用现实成本收益校准奖励，使指标有经济含义。

3. 将数据划分为训练和留出样本，并选择适合离线RL的评价方法。

4. 列出多个基准，说明每个基准承担不同对照功能。

5. 报告结果并逐条解读表格，让数字服务论证。

6. 用新约束（如隐私）开启下一阶段评价，说明为什么需要该阶段。

7. 报告新约束下的结果，只声明该结果支持的结论。

8. 若需要机制解释，设计匹配/未匹配分组和简单基线排除替代解释。

9. 如果目标面向管理，用案例把权重或输出翻译成决策建议。

10. 用测试集验证案例洞察，防止解释只在训练集有效。

### results_reporting_steps

1. 先说明评价方法和指标。

2. 给出主表，按模型行、按时长列排列。

3. 逐条列出观察，每条把一行或一列转成一个论证点。

4. 用负面对照说明替代设计为何更差。

5. 用p值或数值差异说明关键比较。

6. 最后用一段总结把表格结果升华为总体结论。

### discussion_and_contribution_steps

1. 重述制品与目标。

2. 用一句话压缩性能、机制和案例三类结果。

3. 提出实践价值与适用性主张。

4. 承认解释形式的局限（不能当作直接规则）。

5. 承认数据与评价的边界（如状态动作空间覆盖不足）。

6. 给出1-2个具体未来方向（如on-policy改进、公平性）。

7. 用通用性主张结束，把贡献从单一情境抽离。

## 可执行写作算法

### 1. 1

- step：1

- rhetorical_job_cn：建立现实背景与利害关系

- research_evidence_required_cn：目标业务领域的公认重要性证据，如成本数据、市场规模或行业报告。

- sentence_pattern_function_cn：用领域事实开场，再用成本或规模把问题从‘重要’推进到‘必须解决’。

- transition_condition_cn：读者已接受该问题重要且需要工具。

### 2. 2

- step：2

- rhetorical_job_cn：批评现有黄金标准方法

- research_evidence_required_cn：至少一个现有方法在序列化或长期优化上不可行的结构性理由，如维度爆炸、忽略交互。

- sentence_pattern_function_cn：先承认方法的流行，再指出其只适用于单个干预，最后用方法论文献为‘优化不等于因果识别’辩护。

- transition_condition_cn：读者接受需要替代实验的模型方法。

### 3. 3

- step：3

- rhetorical_job_cn：引入技术框架并制造缺口

- research_evidence_required_cn：技术框架在相邻领域的成功案例，以及该框架在目标问题中的已知缺陷。

- sentence_pattern_function_cn：用两三句列举成功，随即用‘然而’指出黑箱，把缺陷后果与企业采用和信任绑定。

- transition_condition_cn：读者确认技术可行但需要可解释性。

### 4. 4

- step：4

- rhetorical_job_cn：综述相关文献并声明独特空白

- research_evidence_required_cn：足够多的可比较先前方法，并在方法、场景或设计上与本文形成差异。

- sentence_pattern_function_cn：按两到三个文献流综述，用对比表或显式差异列表突出本文定制点，最后用‘据我们所知’声明空白。

- transition_condition_cn：读者确认没有任何先例直接解决该空白。

### 5. 5

- step：5

- rhetorical_job_cn：形式化问题并把理论映射到设计

- research_evidence_required_cn：问题可被表达为目标框架（如RL三元组）的定义，且每个理论局限都有对应的架构选择。

- sentence_pattern_function_cn：先定义状态、动作、奖励；再用理论局限（如MDP不成立）推出架构选择（如DRQN）；最后由可解释性需求推出解释组件并给出公式。

- transition_condition_cn：读者理解制品的每个设计都源于问题特性。

### 6. 6

- step：6

- rhetorical_job_cn：建立评价方法与基线

- research_evidence_required_cn：适合离线评估的方法、多个覆盖不同功能的基线、有经济含义的奖励校准。

- sentence_pattern_function_cn：先说明数据来源与奖励校准，再介绍评价方法，逐条列出基线并说明每个基线回答什么问题。

- transition_condition_cn：读者相信评价能区分每个设计因素。

### 7. 7

- step：7

- rhetorical_job_cn：报告结果并逐条解释

- research_evidence_required_cn：主结果表以及可解释差异的数字证据。

- sentence_pattern_function_cn：用观察列表逐条把表格数字转成论证点，包括正面对照、无差异比较和负面对照。

- transition_condition_cn：性能主张获得多角度证据。

### 8. 8

- step：8

- rhetorical_job_cn：增加部署或鲁棒性检验

- research_evidence_required_cn：一个未在核心评价中考虑的部署约束，以及约束下的对照实验。

- sentence_pattern_function_cn：先用趋势或监管事实引入新约束，再报告约束下结果，只声明约束内支持的结论。

- transition_condition_cn：“可用性”主张在更多情境下成立。

### 9. 9

- step：9

- rhetorical_job_cn：验证机制而非只验证性能

- research_evidence_required_cn：把模型输出（如注意力权重）与结果关联的组别设计，以及至少一个简单基线排除替代解释。

- sentence_pattern_function_cn：先说明为什么需要机制验证，再定义分组标准，报告组间差异，用简单基线对照说明长期导向，最后把结果升华为机制主张。

- transition_condition_cn：读者接受‘可解释性不是表面相关’。

### 10. 10

- step：10

- rhetorical_job_cn：将机制转译为管理洞察并用测试集验证

- research_evidence_required_cn：有业务含义的细分案例，每个案例有可识别的输出模式，且能在留出集上做匹配/未匹配验证。

- sentence_pattern_function_cn：先定义分析工具（如MIF和奇异特征），用三个案例展示不同模式，再用训练集生成解释、测试集验证解释的方法确认洞察有效。

- transition_condition_cn：读者认为机制不仅是统计现象，更是管理者可用知识。

### 11. 11

- step：11

- rhetorical_job_cn：收束贡献并承认边界

- research_evidence_required_cn：前几步的全部证据；尚无法回答的问题列表。

- sentence_pattern_function_cn：重述制品与双重目标，压缩三类结果，给出实践价值，随后用‘我们承认限制’过渡到数据覆盖、解释类型和on-policy问题，最后用通用性和未来方向收尾。

- transition_condition_cn：读者对贡献与边界都有清晰认识。

## 应模仿的高价值动作

1. 用因果决策文献把‘不运行随机对照实验也能做优化’确立为方法论立场，为离线模型评价提供正当性。

2. 在文献综述中用Table 1对比不同注意力RL的query/key/value，使本文的定制差异一目了然。

3. 让每个基线承担独立论证功能：MAB证明长期收益需要序列模型，DQN证明需要历史信息，DRQN证明注意力不损失性能，I-DQN和ST-ADRQN证明注意力需要针对场景定制。

4. 用one-hot编码设计使注意力权重与真实特征一一对应，把技术可解释性变成可验证、可操作的分析。

5. 用注意力匹配/未匹配分组加关联规则基线，把‘可解释性’从定性装饰提升为可检验机制。

6. 借鉴可解释ML的验证策略，在训练集生成解释、在测试集用匹配/未匹配验证，为案例洞察提供外部有效性。

7. 在结论前将案例洞察上升到管理者行动（监控行业趋势、定制产品），让IS读者看到技术转化为业务价值。

## 不要只复制的表面动作

1. 不要只加注意力层就声称可解释，必须证明权重与收益或决策相关。

2. 不要只报告‘我们比MAB好’，必须解释MAB代表哪种旧目标，以及长期与短期差异的含义。

3. 不要把注意力top特征直接解读为因果渠道效果，应承认缺乏随机实验或干预验证。

4. 不要在没有状态-动作空间覆盖证据时宣称策略全局最优。

5. 不要把单一数据源的结论无边界推广到所有获客场景。

## 证据薄弱或跳跃的动作

1. 从注意力匹配组长期奖励更高跳到‘注意力=前向规划’是较大的理论跳跃：没有直接展示模型如何在多个未来路径间显式模拟和选择。

2. 把案例中top特征解读为模型‘学到渠道因果选择’偏强，注意力权重仍是模型内部分数，不是随机实验证明的因果效应。

3. 结论中‘可广泛用于顾客获取’超出单一数字银行数据和离线评估的支持范围。

4. 匹配/未匹配组定义（top 10中>=5 vs <=2）是作者自定义阈值，未报告对阈值选择的敏感性分析。

5. ‘与后验可解释模型对比’被放到Online Appendix G，主文读者无法直接检验该比较。

## 一句话套路

先用真实业务数据和文献漏斗把顾客获取收窄为‘长期收益优化+内在可解释’的RL制品缺口，再通过定制注意力机制构建DRQN-attention，用离策略基准证明性能、用联邦学习证明隐私可用、用关联规则对比证明注意力是前向规划、用渠道案例加测试集验证把可解释性升级为管理者可用的渠道选择知识。

## 分析边界

分析基于主文全文Markdown，OCR与格式转换可能影响表格和公式的精确呈现；未包含Online Appendix B、D、E、F、G、H的细节，对联邦学习安全性、注意力验证程序和后验模型对比只能依赖主文复述；没有精确页码，只能使用章节、段落和表号定位；部分段落边界可能因Markdown表格和图片说明而难以严格区分，但论证句覆盖完整。
