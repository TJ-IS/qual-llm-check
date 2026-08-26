# When Variety Seeking Meets Unexpectedness: Incorporating Variety-Seeking Behaviors into Design of Unexpected Recommender Systems：ISR 句段级微观图谱

- 作者：Pan Li; Alexander Tuzhilin
- 年份：2024
- DOI：10.1287/isre.2021.0053
- 源文件：28035_2024_when-variety-seeking-meets-unexpectedness-incorporating-variety-seeking-behaviors-into-design-of.md
- 置信度：0.93

## 核实后的宏观骨架

文章以消费者variety seeking为理论锚点，先在引言中建立其在营销中的重要性并指出推荐系统研究的三个技术缺口；然后构建可计算的measurement framework（距离函数+时间衰减+stationarity）并用Alibaba问卷和ADF检验确立构念效度；接着提出recommendation framework，将variety seeking作为个性化权重自动决定unexpectedness强度；再通过三个离线数据集benchmark证明模型相对多类baseline的优势；随后用大型视频平台线上A/B实验证明真实业务效应，并以异质性、平行趋势和稳健性检验支撑机制解释；最后在结论中把结果升华为可复用设计知识和理论贡献，并以公司部署作为终极现实背书。

## 摘要逐句图谱

### 1. Abstract P1

- order：1

- locator：Abstract P1

- paraphrase_cn：定义variety seeker为容易厌倦已购产品、偏好新鲜内容以拓展视野的消费者。

- move_code：CONTEXT_AND_DEFINITION

- statement_status：prior_literature

- why_here_cn：开篇用一个通俗概念界定核心研究对象，让读者立即知道本文关注的用户类型。

- inherits_from_previous_cn：没有前置句，是摘要的起点。

- changes_argument_state_cn：确立了variety seeking是一个可命名、可观察的消费者群体特征。

- sets_up_next_cn：为下一句指出该现象虽普遍但未被推荐研究充分处理制造对照。

- failure_if_removed_cn：读者不知道研究对象是什么，后续gap和研究目标失去载体。

- evidence_pointer：Abstract第一句

### 2. Abstract P1

- order：2

- locator：Abstract P1

- paraphrase_cn：尽管这一行为普遍，但由于现有variety-seeking测量方法的种种局限，推荐应用中很少研究它。

- move_code：GAP

- statement_status：author_inference

- why_here_cn：在摘要开头就把gap放在最关键位置，说明为什么需要这篇文章。

- inherits_from_previous_cn：承接前句定义的variety seeker的重要性。

- changes_argument_state_cn：把研究对象从‘重要’转为‘未充分研究’，制造研究空缺。

- sets_up_next_cn：引出本文要填补这个空缺。

- failure_if_removed_cn：研究动机不成立，整个摘要失去问题驱动。

- evidence_pointer：Abstract第二句

### 3. Abstract P2

- order：3

- locator：Abstract P2

- paraphrase_cn：为填补研究空缺，本文提出一个基于消费记录测量消费者variety-seeking水平的框架。

- move_code：OBJECTIVE_OR_SOLUTION_PREVIEW

- statement_status：author_inference

- why_here_cn：在gap后立即给出本文的解决方案预览，让读者看到测量框架是核心贡献之一。

- inherits_from_previous_cn：依赖前一句指出的测量方法局限。

- changes_argument_state_cn：从‘问题’转为‘方案’，给出本文的第一个贡献质点。

- sets_up_next_cn：为下一句说明如何验证该框架预留接口。

- failure_if_removed_cn：只有问题没有方案，读者不知道文章要做什么。

- evidence_pointer：Abstract第三句

### 4. Abstract P2

- order：4

- locator：Abstract P2

- paraphrase_cn：通过Alibaba用户问卷研究验证框架有效性，测量结果与消费者自我报告的variety-seeking水平匹配良好。

- move_code：VALIDATION_STUDY_PREVIEW

- statement_status：empirical_result

- why_here_cn：在提出框架后立刻说明第一个验证证据，强调测量框架不是纯理论构想。

- inherits_from_previous_cn：承接前句的框架存在。

- changes_argument_state_cn：把框架从‘提出’推进到‘有证据支持’。

- sets_up_next_cn：为下一句推荐框架的出现铺垫：既然测量有效，可以用于推荐。

- failure_if_removed_cn：测量框架没有直接效度证据，后续推荐设计的输入可信度下降。

- evidence_pointer：Abstract第四句

### 5. Abstract P3

- order：5

- locator：Abstract P3

- paraphrase_cn：进一步提出一个推荐框架，将识别出的variety-seeking水平与数据挖掘中的unexpected recommender systems结合。

- move_code：DESIGN_FEATURE_AND_THEORY_LINK

- statement_status：design_decision

- why_here_cn：从测量框架升级到推荐框架，是本文的第二大贡献，摘要中必须点明。

- inherits_from_previous_cn：依赖测量框架验证有效。

- changes_argument_state_cn：把variety seeking从‘可测量’推进到‘可用于设计推荐系统’。

- sets_up_next_cn：为下一句说明如何依据水平调整意外度预留逻辑。

- failure_if_removed_cn：文章只剩测量没有设计，无法解释为何要做离线在线实验。

- evidence_pointer：Abstract第五句

### 6. Abstract P3

- order：6

- locator：Abstract P3

- paraphrase_cn：在推荐框架中，对variety-seeking高的消费者提供更多unexpected推荐，对低的则相反。

- move_code：MECHANISM_STATEMENT

- statement_status：theory_claim

- why_here_cn：把设计决策背后的行为机制一句话讲清，让读者理解‘为什么这样设计’。

- inherits_from_previous_cn：承接前句框架的存在。

- changes_argument_state_cn：从‘框架’推进到‘具体运作原则’。

- sets_up_next_cn：为下一句用实验验证该原则制造预期。

- failure_if_removed_cn：设计框架缺乏内容，读者不知道框架如何工作。

- evidence_pointer：Abstract第五句后半

### 7. Abstract P4

- order：7

- locator：Abstract P4

- paraphrase_cn：通过三个不同推荐场景的离线实验和一个大型视频平台的在线受控实验，展示模型显著提升多项业务指标并产生实际经济效益。

- move_code：STUDY_OVERVIEW_AND_RESULT

- statement_status：empirical_result

- why_here_cn：摘要需要同时交代证据类型和结果强度，证明框架不只是理论。

- inherits_from_previous_cn：依赖前句设计原则，否则实验没有对象。

- changes_argument_state_cn：从‘设计合理’推进到‘已被多场景证据支持’。

- sets_up_next_cn：为最后一句部署声明提供证据基础。

- failure_if_removed_cn：摘要缺少结果，文章贡献无法落地。

- evidence_pointer：Abstract第六句

### 8. Abstract P5

- order：8

- locator：Abstract P5

- paraphrase_cn：结果带来重要管理含义，有助于理解消费者variety-seeking并设计推荐系统。

- move_code：CONTRIBUTION_IMPLICATION

- statement_status：contribution_claim

- why_here_cn：把结果上升为管理含义，是ISR读者关心的层面。

- inherits_from_previous_cn：承接前句业务指标改善。

- changes_argument_state_cn：从‘结果’升级为‘意义’。

- sets_up_next_cn：为最后一句部署声明制造更高层面的收束。

- failure_if_removed_cn：文章贡献停留在技术层面，缺少ISR视野。

- evidence_pointer：Abstract第七句

### 9. Abstract P5

- order：9

- locator：Abstract P5

- paraphrase_cn：最终，最优模型已由公司部署到视频平台服务所有消费者。

- move_code：DEPLOYMENT_AS_CONTRIBUTION_ANCHOR

- statement_status：empirical_result

- why_here_cn：以现实部署作为最强贡献锚点，强化文章的实际影响力。

- inherits_from_previous_cn：依赖前句业务改善证据。

- changes_argument_state_cn：把‘实验有效’推进到‘真实世界采纳’。

- sets_up_next_cn：结束摘要，给读者留下最深刻的印象。

- failure_if_removed_cn：摘要缺少现实背书，贡献力度下降。

- evidence_pointer：Abstract第八句

## 引言逐句图谱

### 1. Introduction P1 S1

- order：1

- locator：Introduction P1 S1

- paraphrase_cn：variety seeking描述消费者厌倦旧产品后探索新产品的动机。

- move_code：TOPIC_OPENING_DEFINITION

- statement_status：prior_literature

- why_here_cn：引言第一句直接给出核心构念的定义，让读者立刻知道文章主题。

- inherits_from_previous_cn：无前置句。

- changes_argument_state_cn：建立variety seeking是一个明确可讨论的消费者动机。

- sets_up_next_cn：为紧接着的例子和重要性铺路。

- failure_if_removed_cn：读者不知道文章在讨论什么行为。

- evidence_pointer：Introduction第一段

### 2. Introduction P1 S2

- order：2

- locator：Introduction P1 S2

- paraphrase_cn：举例：惊悚片爱好者周五晚批量观看惊悚片后可能转向浪漫喜剧。

- move_code：CONCRETE_ILLUSTRATION

- statement_status：fact

- why_here_cn：用具体场景让抽象概念可感，降低读者理解成本。

- inherits_from_previous_cn：承接variety seeking的定义。

- changes_argument_state_cn：把概念具象化为日常消费行为。

- sets_up_next_cn：为下文强调该行为的重要性提供感性基础。

- failure_if_removed_cn：定义偏抽象，读者可能无法抓住variety seeking的实际形态。

- evidence_pointer：Introduction第一段

### 3. Introduction P1 S3

- order：3

- locator：Introduction P1 S3

- paraphrase_cn：variety seeking是探索性消费者行为的重要维度，因为多样经历能提供刺激、满足好奇心、改善满意度。

- move_code：ESTABLISH_IMPORTANCE

- statement_status：prior_literature

- why_here_cn：引用多个营销/心理学文献证明variety seeking不只是边缘现象，而是核心驱动。

- inherits_from_previous_cn：承接前句定义和例子。

- changes_argument_state_cn：把variety seeking的重要性升格为学术共识。

- sets_up_next_cn：为下一句强调商业后果铺路。

- failure_if_removed_cn：没有重要性铺垫，后面的gap就缺乏分量。

- evidence_pointer：Introduction第一段

### 4. Introduction P1 S4

- order：4

- locator：Introduction P1 S4

- paraphrase_cn：variety seeker还会增加总体消费量并对促销更开放，因此是营销中的重要细分。

- move_code：PRACTICAL_STAKES

- statement_status：prior_literature

- why_here_cn：把variety seeking从行为心理学连接到商业价值，为ISR读者提供现实关切。

- inherits_from_previous_cn：承接前句的学术重要性。

- changes_argument_state_cn：让‘为什么值得研究’从趣味性变成商业必要性。

- sets_up_next_cn：为第二段‘然而推荐系统没有研究它’制造落差。

- failure_if_removed_cn：实际价值缺失，研究动机不完整。

- evidence_pointer：Introduction第一段末

### 5. Introduction P2 S1

- order：5

- locator：Introduction P2 S1

- paraphrase_cn：variety seeking在营销中被广泛研究，但在推荐系统领域显著未充分探索。

- move_code：CROSS_FIELD_GAP

- statement_status：author_inference

- why_here_cn：把文献背景从营销转向推荐系统，直接定位本文的领域缺口。

- inherits_from_previous_cn：依赖前段variety seeking重要性的结论。

- changes_argument_state_cn：确立‘重要但未被研究’的落差。

- sets_up_next_cn：引出随后三个具体限制。

- failure_if_removed_cn：gap模糊，后续三个限制失去框架。

- evidence_pointer：Introduction第二段首句

### 6. Introduction P2 S2

- order：6

- locator：Introduction P2 S2

- paraphrase_cn：第一，现有测量只在品类或品牌层操作，用经典特征技术计算差异，无法捕捉现代推荐在细粒度产品水平的偏好异质性。

- move_code：LIMITATION_FIRST

- statement_status：author_inference

- why_here_cn：具体列出第一个技术限制，显示问题并非‘没人研究’而是‘现有方法不够用’。

- inherits_from_previous_cn：承接‘未充分探索’并细化原因。

- changes_argument_state_cn：把gap转成可操作的技术缺陷。

- sets_up_next_cn：为本文使用潜在空间表示提供动机。

- failure_if_removed_cn：测量框架第一处设计动机缺失。

- evidence_pointer：Introduction第二段

### 7. Introduction P2 S3

- order：7

- locator：Introduction P2 S3

- paraphrase_cn：传统显式特征模型也难以扩展到大多数工业平台，导致高延迟和性能下降。

- move_code：LIMITATION_FIRST_CONTINUED

- statement_status：author_inference

- why_here_cn：补充说明第一个限制在工业上的严重代价，让技术缺陷带上商业影响。

- inherits_from_previous_cn：承接前一句的产品水平限制。

- changes_argument_state_cn：让‘粒度不足’升级为‘可扩展性失败’。

- sets_up_next_cn：为autoencoder等工业可部署方法埋下伏笔。

- failure_if_removed_cn：第一个限制的后果不完整。

- evidence_pointer：Introduction第二段

### 8. Introduction P2 S4

- order：8

- locator：Introduction P2 S4

- paraphrase_cn：第二，虽然时间因素在variety-seeking建模中很重要，但现有模型不考虑购买行为间的dwell time，导致测量效果显著下降。

- move_code：LIMITATION_SECOND

- statement_status：author_inference

- why_here_cn：插入第二个独立缺陷，与第一点形成并列结构。

- inherits_from_previous_cn：延续‘现有方法不够’的总体判断。

- changes_argument_state_cn：把时间维度提为另一个缺失。

- sets_up_next_cn：为时间衰减函数设计做铺垫。

- failure_if_removed_cn：时间衰减组件失去动机。

- evidence_pointer：Introduction第二段

### 9. Introduction P2 S5

- order：9

- locator：Introduction P2 S5

- paraphrase_cn：第三，现有营销方法很少研究variety-seeking的长期属性如stationarity，导致难以提取和泛化行为模式。

- move_code：LIMITATION_THIRD

- statement_status：author_inference

- why_here_cn：第三个限制把问题从短期测量拉到长期稳定性，为stationarity假设和检验铺路。

- inherits_from_previous_cn：延续现有方法不足的论证。

- changes_argument_state_cn：把时间维度延伸到统计假设。

- sets_up_next_cn：为stationarity提出和研究作铺垫。

- failure_if_removed_cn：三组件框架缺少第三个支柱的动机。

- evidence_pointer：Introduction第二段末

### 10. Introduction P3 S1

- order：10

- locator：Introduction P3 S1

- paraphrase_cn：为处理上述问题并将variety seeking纳入推荐设计，本文提出一个variety-seeking框架，仅基于消费记录测量每个消费者的variety-seeking水平，不需要显式消费者反馈。

- move_code：SOLUTION_PREVIEW

- statement_status：design_decision

- why_here_cn：在三个限制后立即给出整体解决方案，明确框架的输入和输出。

- inherits_from_previous_cn：直接回应前句三个限制。

- changes_argument_state_cn：从‘问题清单’转为‘解决计划’。

- sets_up_next_cn：为框架三组件概述提供入口。

- failure_if_removed_cn：三个限制没有对应解决方案，文章失去主目标。

- evidence_pointer：Introduction第三段首句

### 11. Introduction P3 S2

- order：11

- locator：Introduction P3 S2

- paraphrase_cn：框架由三个关键组件组成：距离函数、时间衰减函数和stationarity属性。

- move_code：FRAMEWORK_COMPONENT_PREVIEW

- statement_status：design_decision

- why_here_cn：一句话预告框架三组件，让读者预见后续Section 3的结构。

- inherits_from_previous_cn：承接前句的框架提出。

- changes_argument_state_cn：把抽象框架具体化为三个可讨论的维度。

- sets_up_next_cn：为第三节逐组件展开提供导航。

- failure_if_removed_cn：读者不知道框架里面是什么。

- evidence_pointer：Introduction第三段

### 12. Introduction P3 S3

- order：12

- locator：Introduction P3 S3

- paraphrase_cn：对组件作具体假设时就得到对应的具体variety-seeking测量模型。

- move_code：FRAMEWORK_TO_MODEL_INSTANTIATION

- statement_status：author_inference

- why_here_cn：说明框架是模板而非单一模型，为后文多变体比较奠定基础。

- inherits_from_previous_cn：承接三组件框架。

- changes_argument_state_cn：把框架从‘结构’推进到‘可实例化’。

- sets_up_next_cn：为问卷验证中比较多个变体做铺垫。

- failure_if_removed_cn：没有实例化逻辑，后文变体比较显得无依据。

- evidence_pointer：Introduction第三段

### 13. Introduction P3 S4

- order：13

- locator：Introduction P3 S4

- paraphrase_cn：通过问卷研究证明这些测量相对现有测量有显著性能提升。

- move_code：RESULT_PREVIEW

- statement_status：empirical_result

- why_here_cn：引言中提前预告测量验证结果，使解决方案不只停留在提议。

- inherits_from_previous_cn：依赖前句框架可实例化。

- changes_argument_state_cn：把框架的有效性推进为已有证据。

- sets_up_next_cn：为进入推荐框架阶段做过渡。

- failure_if_removed_cn：测量框架缺少初步证据，后文直接进入推荐设计显得跳跃。

- evidence_pointer：Introduction第三段末

### 14. Introduction P4 S1

- order：14

- locator：Introduction P4 S1

- paraphrase_cn：进一步，本文把消费者寻求多样性的欲望与unexpected recommender systems范式连接起来。

- move_code：SECOND_KNOWLEDGE_BASE_INTRODUCTION

- statement_status：theory_claim

- why_here_cn：从测量框架转入推荐框架，引出第二根理论支柱unexpectedness。

- inherits_from_previous_cn：测量框架有效性为后文推荐设计提供输入。

- changes_argument_state_cn：把文章从‘测量’扩展到‘设计’。

- sets_up_next_cn：为unexpectedness定义和互补性论证铺垫。

- failure_if_removed_cn：文章只有测量，缺少推荐设计主线。

- evidence_pointer：Introduction第四段首句

### 15. Introduction P4 S2

- order：15

- locator：Introduction P4 S2

- paraphrase_cn：unexpectedness来自数据挖掘文献，衡量推荐产品与消费者期望的距离，是产品中心的概念；variety seeking来自营销，衡量消费者寻求显著不同内容的倾向，是消费者中心的概念。

- move_code：CONCEPTUAL_CONTRAST

- statement_status：prior_literature

- why_here_cn：通过‘产品中心vs消费者中心’的对比，为互补性论证奠定概念基础。

- inherits_from_previous_cn：承接前句两种范式的连接。

- changes_argument_state_cn：确立两个概念各自所属的领域和重心。

- sets_up_next_cn：为下一句‘互补’下结论提供依据。

- failure_if_removed_cn：互补性论证缺少概念对比，无法成立。

- evidence_pointer：Introduction第四段

### 16. Introduction P4 S3

- order：16

- locator：Introduction P4 S3

- paraphrase_cn：因此假设两概念互补，必须适当结合才能达到最优推荐性能。

- move_code：COMPLEMENTARITY_HYPOTHESIS

- statement_status：theory_claim

- why_here_cn：把前面的对比转化为可检验的假设，是全文核心命题。

- inherits_from_previous_cn：依赖前句概念对比。

- changes_argument_state_cn：从‘概念定义’推进到‘理论假设’。

- sets_up_next_cn：为下句具体说明高variety seeker偏好更多意外产品。

- failure_if_removed_cn：核心命题缺失，整个设计框架失去理论支撑。

- evidence_pointer：Introduction第四段

### 17. Introduction P4 S4

- order：17

- locator：Introduction P4 S4

- paraphrase_cn：具体展示高variety-seeking的消费者偏好更多意外产品，因此需要相应提高推荐中的unexpectedness程度，反之亦然。

- move_code：MECHANISM_SPELL_OUT

- statement_status：theory_claim

- why_here_cn：把假设细化成可操作的预测：个体差异决定意外度偏好。

- inherits_from_previous_cn：承接互补性假设。

- changes_argument_state_cn：让假设具体到‘如何调整’层面。

- sets_up_next_cn：为推荐框架中权重个性化设计做理论铺垫。

- failure_if_removed_cn：假设仍是空壳，设计不知如何落地。

- evidence_pointer：Introduction第四段

### 18. Introduction P4 S5

- order：18

- locator：Introduction P4 S5

- paraphrase_cn：因此提出一个推荐框架，自动根据每个消费者的variety-seeking水平调整unexpectedness程度，显著增强个性化水平。

- move_code：DESIGN_DECISION_FROM_THEORY

- statement_status：design_decision

- why_here_cn：把理论假设转化为具体设计决策，是文章从theory到design的枢纽。

- inherits_from_previous_cn：依赖前句高variety seeker偏好意外的预测。

- changes_argument_state_cn：从‘应该调整’推进到‘设计一个框架来调整’。

- sets_up_next_cn：为后文各类模型和实验提供设计对象。

- failure_if_removed_cn：缺少设计决策，全文只停留在心理学命题。

- evidence_pointer：Introduction第四段

### 19. Introduction P4 S6

- order：19

- locator：Introduction P4 S6

- paraphrase_cn：在该框架下构建一系列不同操作化的推荐模型，都显著优于现有unexpected recommender systems，通过Yelp、MovieLens、Alibaba三个数据集的离线实验证明。

- move_code：STUDY_OVERVIEW_AND_RESULT_PREVIEW

- statement_status：empirical_result

- why_here_cn：提前预告离线实验和结果，让读者知道文章会提供大规模证据。

- inherits_from_previous_cn：承接推荐框架的提出。

- changes_argument_state_cn：把设计决策推进为有多数据支持的实证主张。

- sets_up_next_cn：为摘要和结论中的离线结果提供来源。

- failure_if_removed_cn：推荐框架没有证据预告，后文实验显得突兀。

- evidence_pointer：Introduction第四段

### 20. Introduction P4 S7

- order：20

- locator：Introduction P4 S7

- paraphrase_cn：还在中国一个大型视频平台做大规模在线受控实验，将最优模型与最新生产系统比较。

- move_code：ONLINE_EXPERIMENT_PREVIEW

- statement_status：author_inference

- why_here_cn：在离线实验之后补充线上实验预告，显示证据链的完整性。

- inherits_from_previous_cn：承接离线实验证据。

- changes_argument_state_cn：把证据范围扩展到真实生产环境。

- sets_up_next_cn：为线上业务的显著提升和部署埋下伏笔。

- failure_if_removed_cn：论文缺少现场证据层级，经济影响证明不完整。

- evidence_pointer：Introduction第四段

### 21. Introduction P4 S8

- order：21

- locator：Introduction P4 S8

- paraphrase_cn：结果显示显著业务绩效提升，并带来短期和长期的实际经济影响。

- move_code：RESULT_PREVIEW

- statement_status：empirical_result

- why_here_cn：把线上实验结果压缩成一句话，作为引言阶段的实证高峰。

- inherits_from_previous_cn：依赖前句线上实验。

- changes_argument_state_cn：让证据从‘性能’升级为‘经济影响’。

- sets_up_next_cn：为下一句bridge gap和贡献总结做铺垫。

- failure_if_removed_cn：线上实验的成果缺失，经济影响声明悬空。

- evidence_pointer：Introduction第四段

### 22. Introduction P4 S9

- order：22

- locator：Introduction P4 S9

- paraphrase_cn：因此本文弥合了variety-seeking学术研究与真实世界应用之间的gap，同时改善业务绩效。

- move_code：BRIDGE_GAP_CLAIM

- statement_status：contribution_claim

- why_here_cn：在数据证据后明确宣称本文连接了学术与实践，是ISR论文的定位句。

- inherits_from_previous_cn：综合前句离线在线结果。

- changes_argument_state_cn：从‘结果’上升为‘桥接贡献’。

- sets_up_next_cn：为最后一段贡献列表提供总结性质。

- failure_if_removed_cn：研究意义不够明确，读者不知文章价值在哪。

- evidence_pointer：Introduction第四段末

### 23. Introduction P5 S1

- order：23

- locator：Introduction P5 S1

- paraphrase_cn：本文贡献包括：第一，提出variety-seeking框架测量推荐系统中消费者variety seeking的多个方面。

- move_code：CONTRIBUTION_FIRST

- statement_status：contribution_claim

- why_here_cn：贡献列表第一项，回指测量框架。

- inherits_from_previous_cn：承接全文目标和框架提出。

- changes_argument_state_cn：把‘我们做了什么’正式命名为贡献。

- sets_up_next_cn：为第二项贡献铺垫。

- failure_if_removed_cn：测量贡献没有被明文highlight。

- evidence_pointer：Introduction第五段

### 24. Introduction P5 S2

- order：24

- locator：Introduction P5 S2

- paraphrase_cn：第二，提出一个推荐框架，结合unexpectedness和variety seeking来处理消费者对产品多样性的异质需求。

- move_code：CONTRIBUTION_SECOND

- statement_status：contribution_claim

- why_here_cn：贡献列表第二项，回指推荐框架。

- inherits_from_previous_cn：承接推荐框架提出。

- changes_argument_state_cn：把推荐设计也正式标记为贡献。

- sets_up_next_cn：为第三项贡献铺垫。

- failure_if_removed_cn：推荐框架贡献被忽略。

- evidence_pointer：Introduction第五段

### 25. Introduction P5 S3

- order：25

- locator：Introduction P5 S3

- paraphrase_cn：第三，构建多个variety-seeking推荐模型，通过问卷、离线实验、在线受控实验证明其显著优于现有方案和公司最新生产系统，带来可操作的管理含义。

- move_code：CONTRIBUTION_THIRD

- statement_status：contribution_claim

- why_here_cn：把多阶段证据与贡献绑定，并用‘可操作管理含义’回应ISR受众。

- inherits_from_previous_cn：综合前两项贡献和全部证据。

- changes_argument_state_cn：把证据集成升级为贡献声明。

- sets_up_next_cn：为最后的部署声明做铺垫。

- failure_if_removed_cn：贡献列表中缺少实证支撑的统一表述。

- evidence_pointer：Introduction第五段

### 26. Introduction P5 S4

- order：26

- locator：Introduction P5 S4

- paraphrase_cn：显著的经济影响使公司把最优模型部署到生产环境，服务整个视频平台。

- move_code：DEPLOYMENT_AND_FINAL_ANCHOR

- statement_status：empirical_result

- why_here_cn：用最终部署作为引言最强收束，呼应摘要。

- inherits_from_previous_cn：依赖前句经济影响。

- changes_argument_state_cn：把贡献从‘被证明’推进到‘被采纳’。

- sets_up_next_cn：结束引言，进入文献综述。

- failure_if_removed_cn：引言缺少现实落地证据，贡献力度下降。

- evidence_pointer：Introduction第五段末

## 引言逐段图谱

### 1. Introduction P1

- locator：Introduction P1

- opening_move_cn：用定义和例子开启，使variety seeking变得具体。

- development_move_cn：通过多条文献累积variety seeking在心理学和营销中的重要性。

- pivot_move_cn：从学术重要性转向商业细分价值。

- closing_move_cn：以‘重要消费者细分’结束，制造下一段‘但推荐系统没研究’的落差。

- paragraph_job_cn：让读者承认variety seeking既重要又普遍，为后续gap提供‘值得研究’的理由。

### 2. Introduction P2

- locator：Introduction P2

- opening_move_cn：用跨领域对比开启：营销很热，推荐很冷。

- development_move_cn：连续列出三个具体技术限制，每个都指向一个设计组件。

- pivot_move_cn：无独立转折，三个限制本身就是从‘总体gap’到‘可解决缺口’的收敛。

- closing_move_cn：以‘难以泛化行为模式’结束，直接为stationarity设计铺垫。

- paragraph_job_cn：把笼统的‘未研究’转成三个具体、可被本文解决的技术缺口。

### 3. Introduction P3

- locator：Introduction P3

- opening_move_cn：用‘为解决上述问题’承接上一段三个限制。

- development_move_cn：给出框架的边界（仅消费记录、无需反馈）和三组件构成。

- pivot_move_cn：从‘组件’转到‘具体假设产生具体模型’。

- closing_move_cn：以‘问卷验证显著提升’结束，给测量框架初步证据。

- paragraph_job_cn：提出并初步确证第一个核心贡献：variety-seeking测量框架。

### 4. Introduction P4

- locator：Introduction P4

- opening_move_cn：用‘更进一步’把文章从测量引向推荐设计。

- development_move_cn：先定义unexpectedness和variety seeking的概念来源，再提出互补假设，再具体化为按水平调整意外度。

- pivot_move_cn：从‘假设成立’转到‘所以设计一个框架’。

- closing_move_cn：用离线+线上实验预告和‘桥接学术与实践’结束，制造对证据的期待。

- paragraph_job_cn：提出第二核心贡献（推荐框架）并完成从理论假设到设计决策的转化。

### 5. Introduction P5

- locator：Introduction P5

- opening_move_cn：以‘本文做出以下贡献’直接开启列表。

- development_move_cn：三项贡献层层递进：测量框架→推荐框架→多证据验证+管理含义。

- pivot_move_cn：从‘第三贡献’转到‘经济影响导致部署’。

- closing_move_cn：以部署作为最强结束锚点。

- paragraph_job_cn：系统列出贡献并对全文价值做最高级别声明。

## 理论到设计逐句图谱

### 1. Section 3 P1 S1

- order：1

- locator：Section 3 P1 S1

- paraphrase_cn：测量variety seeking的一个关键考虑是消费者探索新产品和寻求显著不同内容的倾向，产品差异用距离函数定义。

- move_code：THEORY_TO_DESIGN_MOTIVATION

- statement_status：theory_claim

- why_here_cn：确立距离函数来自variety seeking理论对‘不同内容’的定义。

- inherits_from_previous_cn：承接引言中提出的三组件框架预告。

- changes_argument_state_cn：把理论概念‘寻求不同内容’转化为可计算的距离函数。

- sets_up_next_cn：为第二假设（时间衰减）作铺垫。

- failure_if_removed_cn：距离函数缺乏理论来源，变为任意技术选择。

- evidence_pointer：Section 3第一段

### 2. Section 3 P1 S2

- order：2

- locator：Section 3 P1 S2

- paraphrase_cn：另一个基本假设是两产品差异随时间间隔增大变得不太相关，因为消费者会遗忘远经验。

- move_code：THEORY_ASSUMPTION_FOR_DESIGN

- statement_status：theory_claim

- why_here_cn：把记忆衰退作为时间衰减函数的理论基础。

- inherits_from_previous_cn：距离函数已定义，现在引入时间维度。

- changes_argument_state_cn：让‘遗忘’成为设计需求而非统计便利。

- sets_up_next_cn：为时间衰减函数的具体形式作铺垫。

- failure_if_removed_cn：时间衰减组件失去行为理论依据。

- evidence_pointer：Section 3第一段

### 3. Section 3 P1 S3

- order：3

- locator：Section 3 P1 S3

- paraphrase_cn：第三，为给消费者赋予稳定的variety-seeking水平，假设其长期稳定，因此过程应平稳。

- move_code：THEORY_ASSUMPTION_FOR_DESIGN

- statement_status：theory_claim

- why_here_cn：把variety seeking作为内在特质引向stationarity假设。

- inherits_from_previous_cn：前两句已经建立了距离和时间两个组件。

- changes_argument_state_cn：使stationarity成为框架的第三个理论支柱。

- sets_up_next_cn：为Equation (1)(2)和ADF检验作铺垫。

- failure_if_removed_cn：stationarity组件没有理论来源，后续检验失去意义。

- evidence_pointer：Section 3第一段末

### 4. Section 3 Equation (1)

- order：4

- locator：Section 3 Equation (1)

- paraphrase_cn：定义Product_Variety为所有历史消费产品到目标产品距离的加权和，权重来自时间衰减函数。

- move_code：FORMALIZATION_OF_THEORY

- statement_status：design_decision

- why_here_cn：用公式把前三条理论假设整合成可计算定义。

- inherits_from_previous_cn：依赖距离函数和时间衰减的讨论。

- changes_argument_state_cn：理论假设落地为数学表达式。

- sets_up_next_cn：为下一公式Variety_Seeking(i)提供原料。

- failure_if_removed_cn：测量框架没有形式化，无法进行任何验证。

- evidence_pointer：Equation (1)

### 5. Section 3 Equation (2)

- order：5

- locator：Section 3 Equation (2)

- paraphrase_cn：Variety_Seeking(i)被定义为所有产品variety水平的算术平均，以满足stationarity。

- move_code：STATIONARITY_OPERATIONALIZATION

- statement_status：design_decision

- why_here_cn：用算术平均作为stationarity的实现方式，是最简单且符合文献的选择。

- inherits_from_previous_cn：依赖前句stationarity假设。

- changes_argument_state_cn：让‘稳定’变成‘可计算为均值’。

- sets_up_next_cn：为组件清单和后续检验作准备。

- failure_if_removed_cn：没有聚合方式，测量框架无法输出单个消费者水平。

- evidence_pointer：Equation (2)

### 6. Section 3.1 P1

- order：6

- locator：Section 3.1 P1

- paraphrase_cn：文献中最早用binary值计算variety seeking，但忽略了产品间的相似度差异。

- move_code：PRIOR_KNOWLEDGE_LIMITATION

- statement_status：prior_literature

- why_here_cn：用文献演进说明binary方法的不足，为特征距离和潜在距离铺垫。

- inherits_from_previous_cn：承接距离函数是框架组件的讨论。

- changes_argument_state_cn：确立现有距离方法的第一个缺陷。

- sets_up_next_cn：引出特征距离方法。

- failure_if_removed_cn：距离函数的演进叙事不完整。

- evidence_pointer：Section 3.1第一段

### 7. Section 3.1 P2

- order：7

- locator：Section 3.1 P2

- paraphrase_cn：研究者提出用两产品间显式特征相同比例测量variety seeking，在binary之上有显著提升。

- move_code：PRIOR_KNOWLEDGE_CONTINUED

- statement_status：prior_literature

- why_here_cn：说明特征距离是现有最佳方法之一，为本文的潜在空间距离提供对比基线。

- inherits_from_previous_cn：承接binary方法的局限。

- changes_argument_state_cn：让特征距离成为距离函数的‘现状’。

- sets_up_next_cn：为本文提出潜在距离作铺垫。

- failure_if_removed_cn：特征距离没有出现，潜在距离的贡献就缺乏比较对象。

- evidence_pointer：Section 3.1第二段

### 8. Section 3.1 P3

- order：8

- locator：Section 3.1 P3

- paraphrase_cn：本文提出在深度学习潜在空间计算距离，比特征空间更能细分消费者异质性。

- move_code：DESIGN_DECISION_FOR_DISTANCE

- statement_status：design_decision

- why_here_cn：把距离函数选择推进到潜在空间，是本文相对现有方法的技术升级点。

- inherits_from_previous_cn：承接特征距离的不足。

- changes_argument_state_cn：距离函数的默认选择从特征空间转向潜在空间。

- sets_up_next_cn：为autoencoder选型作铺垫。

- failure_if_removed_cn：没有潜在距离，后续autoencoder的引入失去依据。

- evidence_pointer：Section 3.1第三段

### 9. Section 3.1 P4

- order：9

- locator：Section 3.1 P4

- paraphrase_cn：选择autoencoding模型作为潜在表示模型，因为它在工业平台最流行、灵活、可扩展且内存高效。

- move_code：TECHNICAL_CHOICE_JUSTIFICATION

- statement_status：design_decision

- why_here_cn：在多个潜在表示模型中选择AE，并用工业部署性和效率辩护。

- inherits_from_previous_cn：依赖前句潜在距离的需求。

- changes_argument_state_cn：把潜在距离的实现具体化为AE。

- sets_up_next_cn：为AE的encoder-decoder和损失函数描述作铺垫。

- failure_if_removed_cn：潜在距离停留在抽象，无法执行。

- evidence_pointer：Section 3.1第四段

### 10. Section 3.1 P5

- order：10

- locator：Section 3.1 P5

- paraphrase_cn：AE模型学习encoder将显式特征映射为潜在表示，decoder还原特征，通过重建损失联合优化，最后用潜在表示的欧氏距离计算产品差异。

- move_code：TECHNICAL_DETAIL_OF_CHOSEN_MODEL

- statement_status：design_decision

- why_here_cn：给出AE的实现细节，使设计可复现。

- inherits_from_previous_cn：承接AE选择。

- changes_argument_state_cn：把距离计算落实为可代码实现的操作。

- sets_up_next_cn：为3.1小结中把Euclidean定为推荐距离作铺垫。

- failure_if_removed_cn：设计无法复现，后文实验结果失去可验证性。

- evidence_pointer：Section 3.1第五段

### 11. Section 3.2 P1

- order：11

- locator：Section 3.2 P1

- paraphrase_cn：时间衰减函数在营销应用（广告、销售）中很重要，最常用的是指数衰减。

- move_code：THEORY_AND_DESIGN_FOR_TIME_DECAY

- statement_status：prior_literature

- why_here_cn：用营销文献支撑指数衰减的选用。

- inherits_from_previous_cn：承接Section 3的基本时间衰减假设。

- changes_argument_state_cn：把‘遗忘’落实为指数函数。

- sets_up_next_cn：为后文对比双曲和添加剂模型作铺垫。

- failure_if_removed_cn：时间衰减函数没有文献基础，只能算任意设定。

- evidence_pointer：Section 3.2第一段

### 12. Section 3.2 P2

- order：12

- locator：Section 3.2 P2

- paraphrase_cn：先前的variety-seeking模型没有考虑时间因素，但时间对消费者在线体验很重要，例如dwell time。

- move_code：GAP_RESTATEMENT_FOR_TIME

- statement_status：author_inference

- why_here_cn：再次强调时间因子是本文测量框架的独特贡献。

- inherits_from_previous_cn：承接指数衰减函数的讨论。

- changes_argument_state_cn：把时间衰减从‘可选项’升为‘必须项’。

- sets_up_next_cn：为问卷消融结果（去除衰减后效果变差）作铺垫。

- failure_if_removed_cn：时间衰减的重要性没有独立论证。

- evidence_pointer：Section 3.2第二段

### 13. Section 3.3 P1

- order：13

- locator：Section 3.3 P1

- paraphrase_cn：stationarity是最后也是关键维度，因为variety seeking是消费者内在特征，应该稳定。

- move_code：THEORY_ASSUMPTION_FOR_STATIONARITY

- statement_status：theory_claim

- why_here_cn：把stationarity从统计概念绑定到行为特质理论。

- inherits_from_previous_cn：承接框架第三组件预告。

- changes_argument_state_cn：让均值统计成为stationarity的实现而非随意选择。

- sets_up_next_cn：为ADF检验和描述性数据分析作铺垫。

- failure_if_removed_cn：stationarity只是一个统计偏好而非理论必要。

- evidence_pointer：Section 3.3第一段

### 14. Section 3.3 P2

- order：14

- locator：Section 3.3 P2

- paraphrase_cn：明确提出stationarity假设：消费的variety-seeking行为是平稳时间序列，并说明这是简化但合理的假设。

- move_code：HYPOTHESIS_STATEMENT

- statement_status：theory_claim

- why_here_cn：把stationarity正式化为可检验假设，并为其辩护。

- inherits_from_previous_cn：承接前句个别特质稳定性。

- changes_argument_state_cn：让ADF检验有明确对象。

- sets_up_next_cn：为随后的实证检验作铺垫。

- failure_if_removed_cn：ADF检验没有假设可检验。

- evidence_pointer：Section 3.3第二段

### 15. Section 3.3 P3

- order：15

- locator：Section 3.3 P3

- paraphrase_cn：通过视频平台数据展示产品variety水平均值方差小，用户早期观看有波动但晚期收敛。

- move_code：DESCRIPTIVE_EVIDENCE_FOR_STATIONARITY

- statement_status：empirical_result

- why_here_cn：在正式检验前先用直观图像支持stationarity，让读者有第一印象。

- inherits_from_previous_cn：承接stationarity假设。

- changes_argument_state_cn：为假设提供初步直接观察。

- sets_up_next_cn：为ADF检验的正式统计结果作铺垫。

- failure_if_removed_cn：ADF检验显得凭空出现。

- evidence_pointer：Figure 2

### 16. Section 3.3 P4

- order：16

- locator：Section 3.3 P4

- paraphrase_cn：用ADF检验证实有衰减的variety measure平稳，无衰减则不平稳。

- move_code：FORMAL_TEST_RESULT

- statement_status：empirical_result

- why_here_cn：用统计检验取代直觉，是stationarity的关键证据。

- inherits_from_previous_cn：承接前句描述性观察。

- changes_argument_state_cn：让stationarity从假设变为被证实。

- sets_up_next_cn：为框架总结里强调时间衰减的必要性作铺垫。

- failure_if_removed_cn：stationarity只有观察没有统计确认。

- evidence_pointer：Table 1

### 17. Section 4.1 P1

- order：17

- locator：Section 4.1 P1

- paraphrase_cn：经典推荐模型效用只由relevance决定，目标是找最相关产品。

- move_code：PRIOR_KNOWLEDGE_BASELINE

- statement_status：prior_literature

- why_here_cn：设定传统基线，用以引出unexpectedness的加入。

- inherits_from_previous_cn：从测量框架转向推荐框架。

- changes_argument_state_cn：把推荐框架讨论放在既有relevance范式之上。

- sets_up_next_cn：为下一句指出relevance-only的局限作铺垫。

- failure_if_removed_cn：没有基线，unexpectedness的引入缺乏背景。

- evidence_pointer：Section 4.1第一段

### 18. Section 4.1 P1

- order：18

- locator：Section 4.1 P1

- paraphrase_cn：然而仅用relevance会忽略消费者对新内容的需求，因此加入unexpectedness目标：Utility = Relevance + α×Unexpectedness，其中α对所有消费者固定。

- move_code：PRIOR_KNOWLEDGE_WITH_FIXED_ALPHA

- statement_status：prior_literature

- why_here_cn：描述现有unexpectedness推荐模型的标准形式，并指出固定α的问题。

- inherits_from_previous_cn：承接relevance-only的局限。

- changes_argument_state_cn：把‘需要unexpectedness’定位为已有方案，但留下异质性缺口。

- sets_up_next_cn：为variety seeking作为α的替代作铺垫。

- failure_if_removed_cn：没有固定α模型，本文的个性化权重设计没有对手。

- evidence_pointer：Section 4.1第一段

### 19. Section 4.1 P1

- order：19

- locator：Section 4.1 P1

- paraphrase_cn：但不同消费者variety seeking水平差异很大，而unexpectedness是产品属性，因此两者互补，应用variety seeking决定每个消费者的unexpectedness程度。

- move_code：THEORY_TO_DESIGN_BRIDGE

- statement_status：theory_claim

- why_here_cn：这是从理论到设计的枢纽句，把个体差异与产品属性连起来。

- inherits_from_previous_cn：依赖前句固定α的不足。

- changes_argument_state_cn：把固定的α替换为个性化的variety seeking权重。

- sets_up_next_cn：引出Equation (3)的效用函数。

- failure_if_removed_cn：推荐框架的核心设计逻辑断裂。

- evidence_pointer：Section 4.1第一段后半

### 20. Section 4.1 Equation (3)

- order：20

- locator：Section 4.1 Equation (3)

- paraphrase_cn：提出统一推荐框架：Utility = Relevance + f(Variety_Seeking(i), Unexpectedness(i,j))，其中f是聚合函数。

- move_code：FORMAL_DESIGN_EQUATION

- statement_status：design_decision

- why_here_cn：用公式把理论互补性变成可计算推荐目标。

- inherits_from_previous_cn：依赖前句互补性论证。

- changes_argument_state_cn：把设计思想固化为效用函数。

- sets_up_next_cn：为Table 5的配置选项作铺垫。

- failure_if_removed_cn：推荐框架没有形式化，无法实例化多种模型。

- evidence_pointer：Equation (3)

### 21. Section 4.1 P2

- order：21

- locator：Section 4.1 P2

- paraphrase_cn：框架沿relevance、unexpectedness、aggregation三个维度提供多种配置：NCF/DIN、feature/latent、multiply/exponential/power。

- move_code：CONFIGURATION_MATRIX

- statement_status：design_decision

- why_here_cn：把Equation (3)展开为可操作的模型矩阵，供实验比较。

- inherits_from_previous_cn：承接效用函数。

- changes_argument_state_cn：把单一框架转化为2×2×3的模型族。

- sets_up_next_cn：为离线实验比较所有配置作铺垫。

- failure_if_removed_cn：没有配置矩阵，实验缺乏系统性。

- evidence_pointer：Table 5

### 22. Section 4.1 P2末

- order：22

- locator：Section 4.1 P2末

- paraphrase_cn：预告“DIN+Latent+Multiply”组合会取得最佳性能。

- move_code：RESULT_PREVIEW

- statement_status：empirical_result

- why_here_cn：提前告诉读者最佳模型，便于后文实验按这个锚点解读。

- inherits_from_previous_cn：承接配置矩阵。

- changes_argument_state_cn：让模型族有明确的最优代表。

- sets_up_next_cn：为Section 5线上实验直接使用该模型作铺垫。

- failure_if_removed_cn：后文最佳模型声明显得突然。

- evidence_pointer：Section 4.1

## 制品设计理由逐句图谱

### 1. Section 3.1 P4

- order：1

- locator：Section 3.1 P4

- paraphrase_cn：选择autoencoder因为它可扩展、高效，且被阿里巴巴和亚马逊等工业平台使用。

- move_code：ARTIFACT_RATIONALE_INDUSTRIAL

- statement_status：design_decision

- why_here_cn：技术选型不仅要学术合理，还要能在工业落地，这是ISR中制品设计的重要限定。

- inherits_from_previous_cn：承接潜在距离的需求。

- changes_argument_state_cn：把设计选择绑定到真实部署约束。

- sets_up_next_cn：为可复现的encoder-decoder细节作铺垫。

- failure_if_removed_cn：AE选择看似任意，无法解释为何不用其他深度模型。

- evidence_pointer：Section 3.1第四段

### 2. Section 3.1 P5

- order：2

- locator：Section 3.1 P5

- paraphrase_cn：AE通过最小化重建损失联合优化encoder和decoder，得到产品潜在表示后计算欧氏距离。

- move_code：ARTIFACT_RATIONALE_TECHNICAL

- statement_status：design_decision

- why_here_cn：解释AE的内部工作机制，使潜在距离计算不再是黑箱。

- inherits_from_previous_cn：承接AE选择。

- changes_argument_state_cn：让制品在技术层面可理解和可复现。

- sets_up_next_cn：为Euclidean作为推荐距离作铺垫。

- failure_if_removed_cn：潜在距离计算无法理解，也不可复现。

- evidence_pointer：Section 3.1第五段

### 3. Section 3.2 P1

- order：3

- locator：Section 3.2 P1

- paraphrase_cn：最常用的时间衰减函数是指数衰减，它符合比例风险和加速失效时间模型。

- move_code：ARTIFACT_RATIONALE_EXPONENTIAL

- statement_status：prior_literature

- why_here_cn：用统计模型传统说明为什么选指数衰减而不是随意选择。

- inherits_from_previous_cn：承接时间衰减的重要性。

- changes_argument_state_cn：让指数衰减有传统统计模型背书。

- sets_up_next_cn：为后文双曲、添加剂模型对比作铺垫。

- failure_if_removed_cn：指数衰减的选用缺乏理论依据。

- evidence_pointer：Section 3.2第一段

### 4. Section 3.3 P1

- order：4

- locator：Section 3.3 P1

- paraphrase_cn：选择算术平均作为汇总统计，因为它满足stationarity且已被多篇文献使用。

- move_code：ARTIFACT_RATIONALE_STATISTIC

- statement_status：design_decision

- why_here_cn：为为何用均值而非其他统计提供稳定性和文献两个理由。

- inherits_from_previous_cn：承接stationarity假设。

- changes_argument_state_cn：把均值选择从‘最简单’升级为‘理论+实证支持’。

- sets_up_next_cn：为附录中比较其他统计作铺垫。

- failure_if_removed_cn：均值选择缺乏辩护，可能被审稿人质疑。

- evidence_pointer：Section 3.3第一段

### 5. Section 4.1

- order：5

- locator：Section 4.1

- paraphrase_cn：把variety seeking嵌入效用函数可以免于手动确定α，使设计更可管理、更实用。

- move_code：ARTIFACT_RATIONALE_CONTROL_ELIMINATION

- statement_status：design_decision

- why_here_cn：自动化权重的设计不仅理论更优，也规避固定α调参成本。

- inherits_from_previous_cn：承接固定α模型的不足。

- changes_argument_state_cn：强调新设计的操作优势。

- sets_up_next_cn：为后文模型家族提供支撑。

- failure_if_removed_cn：新设计缺少实用理由，可能被认为是学术空想。

- evidence_pointer：Section 4.1

### 6. Section 4.1 P2

- order：6

- locator：Section 4.1 P2

- paraphrase_cn：聚合函数可以用乘法、指数或幂函数，并用DIN/NCF计算relevance，用 feature/latent计算unexpectedness。

- move_code：ARTIFACT_RATIONALE_MODEL_FAMILY

- statement_status：design_decision

- why_here_cn：通过三大维度扩展模型族，使框架不是单一模型。

- inherits_from_previous_cn：承接Equation (3)的灵活f。

- changes_argument_state_cn：让框架有多个可实现实例，支持后文全面实验。

- sets_up_next_cn：为离线实验中2×2×3矩阵比较作铺垫。

- failure_if_removed_cn：实验矩阵缺少设计依据。

- evidence_pointer：Table 5

## Study开头、过渡与收束图谱

### 1. Study 1 (measurement framework) Section 3.5 opening

- locator：Study 1 (measurement framework) Section 3.5 opening

- paraphrase_cn：为验证测量框架有效性，遵循标准营销实践在Alibaba做消费者问卷分析。

- move_code：STUDY_JUSTIFICATION_AND_SETUP

- statement_status：method_decision

- why_here_cn：用标准营销方法为测量构念效度提供外部验证。

- inherits_from_previous_cn：承接第三节框架的形式化。

- changes_argument_state_cn：从‘提出框架’进入‘验证框架’。

- sets_up_next_cn：为问卷参与者和题目细节作铺垫。

- failure_if_removed_cn：测量框架只有形式没有效度证据。

- evidence_pointer：Section 3.5 P1

### 2. Study 1 closing

- locator：Study 1 closing

- paraphrase_cn：总结：本文提出的variety-seeking测量与自报水平相关良好，且每个组件都重要。

- move_code：STUDY_CLOSURE_AND_COMPONENT_CLAIM

- statement_status：empirical_result

- why_here_cn：收束问卷验证，并把结论提升为组件必要性声明。

- inherits_from_previous_cn：依赖Table 4相关结果。

- changes_argument_state_cn：让三组件框架在效度上站稳。

- sets_up_next_cn：为第四节的推荐框架作过渡。

- failure_if_removed_cn：测量验证没有总结，下一节显得突兀。

- evidence_pointer：Section 3.5末

### 3. Study 2 (offline experiments) Section 4.2 opening

- locator：Study 2 (offline experiments) Section 4.2 opening

- paraphrase_cn：本节考虑多个符合框架的模型，并在与商业收入最相关的点击率预测任务上测试性能。

- move_code：STUDY_OPENING_WITH_TASK_JUSTIFICATION

- statement_status：method_decision

- why_here_cn：开篇就交代为什么选CTR任务，让后续离线结果有业务指向。

- inherits_from_previous_cn：承接推荐框架模型族。

- changes_argument_state_cn：从‘设计框架’进入‘评估框架’。

- sets_up_next_cn：为三个数据集介绍和baseline列表作铺垫。

- failure_if_removed_cn：离线实验的任务选择没有理由，结果意义不清。

- evidence_pointer：Section 4.2 P1

### 4. Study 2 transition to online

- locator：Study 2 transition to online

- paraphrase_cn：总结：三个离线数据集代表不同业务和稀疏度，结果证明有效性、泛化性和外部效度。

- move_code：GENERALIZATION_CLAIM

- statement_status：empirical_result

- why_here_cn：把离线结果从‘单一场景有效’升级为‘跨场景泛化’。

- inherits_from_previous_cn：依赖三个数据集上的显著提升。

- changes_argument_state_cn：为进入线上实验制造‘离线已证明，但仍需真实业务证据’的需要。

- sets_up_next_cn：为Section 5线上实验开头作铺垫。

- failure_if_removed_cn：离线实验结论没被总结，线上实验的动机不足。

- evidence_pointer：Section 4.3末

### 5. Study 3 (online experiment) Section 5.1 opening

- locator：Study 3 (online experiment) Section 5.1 opening

- paraphrase_cn：为进一步证明经济收益和实际影响，我们在中国一家大型视频公司进行大规模在线受控实验。

- move_code：STUDY_OPENING_ECONOMIC

- statement_status：method_decision

- why_here_cn：开篇明确线上实验的目的是经济影响，回应离线实验留下的问题。

- inherits_from_previous_cn：承接离线实验的泛化结论。

- changes_argument_state_cn：把证据从离线推进到现场随机实验。

- sets_up_next_cn：为平台背景和自选择偏差讨论作铺垫。

- failure_if_removed_cn：线上实验缺乏理由，显得可有可无。

- evidence_pointer：Section 5.1 P1

### 6. Study 3 closing on deployment

- locator：Study 3 closing on deployment

- paraphrase_cn：基于A/B测试结果和显著业务提升，公司已把模型部署到整个视频平台。

- move_code：DEPLOYMENT_ANCHOR

- statement_status：empirical_result

- why_here_cn：用现实部署作为线上实验的最终closure。

- inherits_from_previous_cn：依赖线上ATE和经济估算。

- changes_argument_state_cn：把研究结果推进为真实世界采纳。

- sets_up_next_cn：为异质性分析提供平台背景，但主要结束研究叙事。

- failure_if_removed_cn：线上实验只有数字没有现实背书。

- evidence_pointer：Section 5.3

### 7. Study 4 (heterogeneity) Section 5.4 opening

- locator：Study 4 (heterogeneity) Section 5.4 opening

- paraphrase_cn：本节展示绩效提升并非对所有消费者一致，而是按variety-seeking水平异质。

- move_code：HETEROGENEITY_OPENING

- statement_status：empirical_result

- why_here_cn：从平均效应转向异质性，深化机制解释。

- inherits_from_previous_cn：承接线上平均ATE结论。

- changes_argument_state_cn：把‘总体有效’细化为‘谁更有效’。

- sets_up_next_cn：为20个bin和交互回归作铺垫。

- failure_if_removed_cn：平均效应可能掩盖关键机制，读者会质疑普适性。

- evidence_pointer：Section 5.4 P1

### 8. Study 5 (parallel trend) Section 5.5 opening

- locator：Study 5 (parallel trend) Section 5.5 opening

- paraphrase_cn：本节做平行趋势分析，观察预处理期无差异、后处理期持续显著。

- move_code：CAUSAL_VALIDITY_OPENING

- statement_status：empirical_result

- why_here_cn：用平行趋势排除预先存在的趋势，强化因果解释。

- inherits_from_previous_cn：承接异质性和线上结果。

- changes_argument_state_cn：让ATE更接近因果效应。

- sets_up_next_cn：为稳健性检查作铺垫。

- failure_if_removed_cn：线上结果可能被质疑是趋势差异而非处理效应。

- evidence_pointer：Section 5.5

### 9. Study 6 (robustness) Section 5.6 opening

- locator：Study 6 (robustness) Section 5.6 opening

- paraphrase_cn：我们进行额外实验来检查结果稳健性，包括不同特征组合、logit/probit、排除自有内容和新增地区。

- move_code：ROBUSTNESS_OPENING

- statement_status：method_decision

- why_here_cn：用多个设定变体显示结论非偶然。

- inherits_from_previous_cn：承接前面ATE和平行趋势结论。

- changes_argument_state_cn：把因果估计从‘单一设定’扩展到‘多设定稳健’。

- sets_up_next_cn：为结论中的边界讨论作铺垫。

- failure_if_removed_cn：线上结果缺乏稳健性保障，因果主张较为脆弱。

- evidence_pointer：Section 5.6

## 讨论与贡献逐句图谱

### 1. Conclusions P1 S1

- order：1

- locator：Conclusions P1 S1

- paraphrase_cn：variety seeking在建模消费者意图和理解行为中起重要作用，推荐需要回应消费者对产品多样性的需求。

- move_code：RESTATE_IMPORTANCE

- statement_status：contribution_claim

- why_here_cn：结论开头重述主题重要性，为总结全文定调。

- inherits_from_previous_cn：承接全文论证。

- changes_argument_state_cn：让读者回到‘为何重要’的初始问题。

- sets_up_next_cn：为总结两个框架作铺垫。

- failure_if_removed_cn：结论没有上下文，直接列贡献显得突兀。

- evidence_pointer：Conclusions P1

### 2. Conclusions P1 S2

- order：2

- locator：Conclusions P1 S2

- paraphrase_cn：为此，我们提出variety-seeking框架，包含距离函数、时间衰减函数和stationarity假设三个维度。

- move_code：SUMMARIZE_FRAMEWORK

- statement_status：contribution_claim

- why_here_cn：一句话复述第一贡献。

- inherits_from_previous_cn：承接前句重要性。

- changes_argument_state_cn：把全文核心构件以结论形式收束。

- sets_up_next_cn：为推荐框架总结作铺垫。

- failure_if_removed_cn：测量框架贡献在结论中没有得到确认。

- evidence_pointer：Conclusions P1

### 3. Conclusions P1 S3

- order：3

- locator：Conclusions P1 S3

- paraphrase_cn：随后提出推荐框架，用variety-seeking水平决定效用函数中的unexpectedness程度。

- move_code：SUMMARIZE_SECOND_FRAMEWORK

- statement_status：contribution_claim

- why_here_cn：复述第二贡献。

- inherits_from_previous_cn：承接测量框架。

- changes_argument_state_cn：确认推荐框架是全文的另一支柱。

- sets_up_next_cn：为机制重申作铺垫。

- failure_if_removed_cn：推荐框架在结论中被遗漏。

- evidence_pointer：Conclusions P1

### 4. Conclusions P1 S4

- order：4

- locator：Conclusions P1 S4

- paraphrase_cn：这样可以为variety seeker提供更多意外产品，为偏好熟悉内容的消费者提供更熟悉产品，从而提升满意度和业务绩效。

- move_code：MECHANISM_RESTATEMENT

- statement_status：theory_claim

- why_here_cn：重申核心机制，将两个框架连接为统一叙述。

- inherits_from_previous_cn：承接推荐框架。

- changes_argument_state_cn：把设计机制再讲一遍，让读者记住‘为什么有效’。

- sets_up_next_cn：为证据总结作铺垫。

- failure_if_removed_cn：机制丢失，贡献变成黑箱结果。

- evidence_pointer：Conclusions P1

### 5. Conclusions P2 S1

- order：5

- locator：Conclusions P2 S1

- paraphrase_cn：为证明框架有效性，我们做了广泛离线实验和大型视频平台在线受控实验。

- move_code：EVIDENCE_SUMMARY

- statement_status：empirical_result

- why_here_cn：结论阶段重新陈述证据类型，提醒读者结论有实证支撑。

- inherits_from_previous_cn：承接两个框架的总结。

- changes_argument_state_cn：把贡献绑定到具体证据。

- sets_up_next_cn：为具体业务结果总结作铺垫。

- failure_if_removed_cn：贡献声明缺少证据绑定。

- evidence_pointer：Conclusions P2

### 6. Conclusions P2 S2

- order：6

- locator：Conclusions P2 S2

- paraphrase_cn：我们将variety seeking纳入unexpected推荐设计，显著增加了视频消费量，相比公司最新生产模型。

- move_code：RESULT_RESTATEMENT

- statement_status：empirical_result

- why_here_cn：复述核心线上结果，强调与最新生产系统对比。

- inherits_from_previous_cn：承接证据总结。

- changes_argument_state_cn：把结果具体化为视频消费量提升。

- sets_up_next_cn：为异质性总结作铺垫。

- failure_if_removed_cn：最重要的业务结果在结论中缺失。

- evidence_pointer：Conclusions P2

### 7. Conclusions P2 S3

- order：7

- locator：Conclusions P2 S3

- paraphrase_cn：进一步展示业务提升并非对所有消费者均匀：强烈偏好或强烈反对variety的消费者获益最大。

- move_code：HETEROGENEITY_RESTATEMENT

- statement_status：empirical_result

- why_here_cn：把异质性结果提升为结论中的关键发现，支撑机制解释。

- inherits_from_previous_cn：承接业务结果。

- changes_argument_state_cn：把‘有效’细化为‘对谁最有效’。

- sets_up_next_cn：为‘对所有人都有影响’作铺垫。

- failure_if_removed_cn：结果显得一律有效，无法体现个性化机理。

- evidence_pointer：Conclusions P2

### 8. Conclusions P2 S4

- order：8

- locator：Conclusions P2 S4

- paraphrase_cn：然而模型对所有消费者都有显著影响，因为提供了更多新鲜视频内容，同时仍有用的推荐并改善体验。

- move_code：ALL_POSITIVE_CLAIM

- statement_status：empirical_result

- why_here_cn：在异质性后补充总体正效应，避免‘只对极端者有效’的误会。

- inherits_from_previous_cn：承接前句异质性。

- changes_argument_state_cn：让结论在异质与普适之间取得平衡。

- sets_up_next_cn：为部署声明作铺垫。

- failure_if_removed_cn：读者可能误以为中等消费者没有收益。

- evidence_pointer：Conclusions P2

### 9. Conclusions P2 S5

- order：9

- locator：Conclusions P2 S5

- paraphrase_cn：由于在Company A的强经济效果，模型已被部署到整个平台。

- move_code：DEPLOYMENT_RESTATEMENT

- statement_status：empirical_result

- why_here_cn：以部署作为结论中的最终现实锚点。

- inherits_from_previous_cn：承接前句经济影响。

- changes_argument_state_cn：把研究结论从‘建议’升为‘已被采纳’。

- sets_up_next_cn：为边界和未来工作作铺垫。

- failure_if_removed_cn：结论缺少现实背书。

- evidence_pointer：Conclusions P2

### 10. Conclusions P3 S1

- order：10

- locator：Conclusions P3 S1

- paraphrase_cn：水平variety在高消费率行业尤其常见，如娱乐产品，本文主要关注这一类型。

- move_code：BOUNDARY_CONDITION

- statement_status：author_inference

- why_here_cn：主动限定适用范围，防止过度泛化。

- inherits_from_previous_cn：承接全文经验边界。

- changes_argument_state_cn：界定框架适用场景。

- sets_up_next_cn：为垂直差异未来工作作铺垫。

- failure_if_removed_cn：读者可能错误外推到所有行业。

- evidence_pointer：Conclusions P3

### 11. Conclusions P3 S2

- order：11

- locator：Conclusions P3 S2

- paraphrase_cn：未来计划研究垂直差异化的variety seeking并纳入推荐设计。

- move_code：FUTURE_WORK_VERTICAL

- statement_status：author_inference

- why_here_cn：把边界转成明确的未来研究方向。

- inherits_from_previous_cn：承接水平vs垂直边界。

- changes_argument_state_cn：让文章不是封闭结论而是研究项目起点。

- sets_up_next_cn：为平台扩展未来工作作铺垫。

- failure_if_removed_cn：边界没有被转化为后续研究路线。

- evidence_pointer：Conclusions P3

### 12. Conclusions P3 S3

- order：12

- locator：Conclusions P3 S3

- paraphrase_cn：计划在其他平台（TikTok、YouTube）和其他业务（音乐、电影、电视、书籍）做类似线上实验。

- move_code：FUTURE_WORK_PLATFORM

- statement_status：author_inference

- why_here_cn：把单一平台结果的一般化计划明说。

- inherits_from_previous_cn：承接边界限定。

- changes_argument_state_cn：承认当前外部效度有限，并给出扩展路径。

- sets_up_next_cn：为动态measure未来工作作铺垫。

- failure_if_removed_cn：平台泛化问题悬而未决，没给读者出路。

- evidence_pointer：Conclusions P3

### 13. Conclusions P3 S4

- order：13

- locator：Conclusions P3 S4

- paraphrase_cn：计划研究更复杂的variety-seeking测量，如动态measure以放松stationarity假设。

- move_code：FUTURE_WORK_DYNAMIC

- statement_status：author_inference

- why_here_cn：承认stationarity是简化假设，并给出未来放松方向。

- inherits_from_previous_cn：承接测量框架边界。

- changes_argument_state_cn：让测量框架不是终点而是起点。

- sets_up_next_cn：为产品侧heterogeneous treatment effect未来工作作铺垫。

- failure_if_removed_cn：stationarity假设的简化性未被承认，可能被审稿人攻击。

- evidence_pointer：Conclusions P3

### 14. Conclusions P3 S5

- order：14

- locator：Conclusions P3 S5

- paraphrase_cn：计划利用框架研究哪些视频类型或品类更有吸引力，基于hedonic/utilitarian特征，帮助从产品侧理解异质处理效应。

- move_code：FUTURE_WORK_PRODUCT_SIDE

- statement_status：author_inference

- why_here_cn：把未来方向从‘平台扩展’延伸到‘产品属性解释’，弥补当前产品侧机制不足。

- inherits_from_previous_cn：承接异质性发现。

- changes_argument_state_cn：指出异质性可能由产品特征驱动，为后续研究提供假设。

- sets_up_next_cn：结束全文。

- failure_if_removed_cn：结论没有进一步研究路线，新颖性无法延续。

- evidence_pointer：Conclusions P3

## Study累积逻辑

### 1. 1

- study_or_phase：阶段一：测量框架形式化与stationarity初步检验

- evidence_job_cn：把营销学variety seeking概念转化为可计算的度量，并初步验证其时间平稳性。

- what_it_establishes_cn：距离函数+时间衰减+stationarity的三组件框架能够产出平稳的variety-seeking水平。

- what_it_cannot_establish_cn：不能证明该度量与消费者主观感受一致，也不能证明它能改善推荐性能。

- why_next_phase_is_needed_cn：需要用户问卷确认测量构念效度，否则度量只是技术构造。

- transition_wording_function_cn：用‘遵循标准营销实践进行问卷分析’把话头从技术定义转向消费者验证。

### 2. 2

- study_or_phase：阶段二：用户问卷验证

- evidence_job_cn：用Alibaba问卷自报数据验证测量构念效度，并与营销baseline比较。

- what_it_establishes_cn：Euclidean+Exponential+Mean与消费者自我报告的variety水平相关性最强，显著优于APF/PAS。

- what_it_cannot_establish_cn：不能证明该测量在真实推荐任务中带来更好的业务指标。

- why_next_phase_is_needed_cn：测量效度好不等于推荐性能好，需要将测量嵌入推荐框架并在离线benchmark上检验。

- transition_wording_function_cn：用‘基于这个框架，我们现在关注推荐框架’把测量阶段收束并引出设计。

### 3. 3

- study_or_phase：阶段三：离线推荐实验

- evidence_job_cn：在三个不同行业数据集上与多类baseline比较，证明框架模型族的性能优势。

- what_it_establishes_cn：所有框架模型显著优于relevance、unexpectedness、diversity、bandit四类baseline，平均提升3.81%。

- what_it_cannot_establish_cn：离线AUC/HR@10不能等同于真实用户反应或商业收入。

- why_next_phase_is_needed_cn：需要线上随机实验把离线指标转换为真实业务结果。

- transition_wording_function_cn：用‘为进一步证明经济收益’把证据链升级到现场实验。

### 4. 4

- study_or_phase：阶段四：线上受控实验（ATE）

- evidence_job_cn：用大型视频平台随机分流实验证明模型相对生产系统的真实业务提升。

- what_it_establishes_cn：CTR+2.29%、VV+4.56%、TS+39.2秒，p<0.01。

- what_it_cannot_establish_cn：平均效应无法说明机制，也无法排除趋势差异或特定用户群无效。

- why_next_phase_is_needed_cn：需要异质性、平行趋势和稳健性分析把平均效应转化为机制解释和边界知识。

- transition_wording_function_cn：用‘提升并非对所有消费者一致’把话头从ATE转向异质性。

### 5. 5

- study_or_phase：阶段五：异质性、平行趋势与稳健性

- evidence_job_cn：把线上平均效应细化为消费者异质性、时间趋势和模型设定的稳定结论。

- what_it_establishes_cn：所有消费者均有正收益，高/低variety seeker获益最大；预处理无差异；多个设定下结论稳健。

- what_it_cannot_establish_cn：不能直接证明心理中介机制，单一视频平台的外部效度有限。

- why_next_phase_is_needed_cn：结论部分需要把这些证据重新组织为设计知识和未来研究边界。

- transition_wording_function_cn：用‘我们做了额外实验检查稳健性’收束实证部分，再进入结论总结。

## 主张—证据台账

### 1. 提出的variety-seeking框架能有效测量消费者variety seeking

- claim_cn：提出的variety-seeking框架能有效测量消费者variety seeking

- claim_level：artifact

- supporting_evidence_cn：Alibaba问卷相关显著高于APF/PAS，ADF平稳性检验通过。

- support_strength：direct

- where_claim_is_made：Section 3.5

- where_evidence_is_provided：Table 4, Table 1

### 2. 距离函数+时间衰减+stationarity三组件都必要

- claim_cn：距离函数+时间衰减+stationarity三组件都必要

- claim_level：artifact

- supporting_evidence_cn：无时间衰减变体在问卷相关和ADF检验中表现差。

- support_strength：direct

- where_claim_is_made：Section 3.5末

- where_evidence_is_provided：Table 4, Table 1

### 3. Euclidean+Exponential+Mean是最优variety-seeking测量

- claim_cn：Euclidean+Exponential+Mean是最优variety-seeking测量

- claim_level：artifact

- supporting_evidence_cn：Table 4中该组合相关系数最高，ADF统计量最强。

- support_strength：direct

- where_claim_is_made：Section 3.5

- where_evidence_is_provided：Table 4

### 4. variety seeking与unexpectedness互补

- claim_cn：variety seeking与unexpectedness互补

- claim_level：theory

- supporting_evidence_cn：离线实验中所有结合两概念的模型显著优于纯relevance和固定α unexperted模型。

- support_strength：partial

- where_claim_is_made：Introduction P4, Section 4.1

- where_evidence_is_provided：Table 7

### 5. variety seeking应作为unexpectedness的个性化权重

- claim_cn：variety seeking应作为unexpectedness的个性化权重

- claim_level：design_knowledge

- supporting_evidence_cn：DIN+Latent+Multiply等个性化模型在三个数据集和线上实验均显著优于固定α生产系统。

- support_strength：direct

- where_claim_is_made：Section 4.1

- where_evidence_is_provided：Table 7, Table 9

### 6. 模型带来真实业务经济效益

- claim_cn：模型带来真实业务经济效益

- claim_level：artifact

- supporting_evidence_cn：线上CTR/VV/TS显著提升，公司部署。

- support_strength：direct

- where_claim_is_made：Section 5.3

- where_evidence_is_provided：Table 9, Section 5.3

### 7. 高和低variety seeker获益最大

- claim_cn：高和低variety seeker获益最大

- claim_level：mechanism

- supporting_evidence_cn：Treatment×Variety_Seeking交互项估计的U型效应。

- support_strength：partial

- where_claim_is_made：Section 5.4

- where_evidence_is_provided：Figure 5

### 8. 模型效果长期而非短暂新奇

- claim_cn：模型效果长期而非短暂新奇

- claim_level：boundary

- supporting_evidence_cn：平行趋势显示后处理期持续显著，只小幅回落。

- support_strength：direct

- where_claim_is_made：Section 5.5

- where_evidence_is_provided：Figure 6

### 9. 结果在多种设定下稳健

- claim_cn：结果在多种设定下稳健

- claim_level：boundary

- supporting_evidence_cn：不同特征组合、logit/probit、排除自有内容和新地区后结论不变。

- support_strength：direct

- where_claim_is_made：Section 5.6

- where_evidence_is_provided：online appendix part VII

## ISR定位逻辑

- constitutive_is_problem_cn：文章把营销学中的消费者行为构念（variety seeking）转化为推荐系统的设计输入，问题不是单纯的算法优化，而是‘数字平台如何根据消费者内在行为特质调整推荐内容’这一IS核心问题。

- technology_behavior_or_market_entanglement_cn：variety seeking被概念化为介于消费者内在特质与平台推荐刺激之间的动态交互：平台推荐的意外程度会反过来影响消费者体验和消费时长，因此技术设计不是中性工具，而是改变用户行为与平台收入的中介。

- role_of_benchmark_or_objective_evidence_cn：离线AUC/HR@10和线上CTR/VV/TS被用来支持一个IS层面的主张：个性化意外的推荐系统比固定的、非个性化的意外推荐更能满足消费者异质需求。客观指标不是终极贡献，而是证明行为理论可落地。

- theory_in_design_cn：理论确实进入了设计：distance函数、time-decay和stationarity三个设计组件全部直接来自variety seeking行为理论；unexpectedness权重用variety seeking水平决定也是理论命题的操作化。但具体深度学习实现（AE、DIN）来自CS工程，属于部分耦合。

- technical_vs_is_contribution_balance_cn：文章约一半篇幅用于技术框架（测量模型、推荐模型、离线实验），另一半用于行为验证（问卷、线上实验、异质性、机制解释）、管理含义和部署。作者明确用‘消费者行为+业务指标’来包装技术贡献，使文章落脚在IS而非纯CS。

- beyond_transient_performance_cn：文章不只报告‘分数提升’：通过跨三个不同行业的离线数据和一个月线上实验证明泛化，通过平行趋势排除新奇效应，通过异质性分析展示个性化机制，并以公司部署作为现实采纳证据，把一次性性能优势转化为可复用的设计知识和理论驱动结论。

## 段落级仿写模板

### abstract_steps

1. 用一句话定义核心行为构念，并给出直观例子。

2. 用一句话指出该构念在推荐领域因测量局限而未充分研究。

3. 用一句话提出测量构念的框架。

4. 用一句话说明测量如何被问卷验证。

5. 用一句话提出把测量用于设计的下游框架。

6. 用一句话描述设计框架的核心机制（按个体水平调整参数）。

7. 用一句话概括离线+在线证据。

8. 用一句话给出业务影响或部署作为贡献锚点。

### introduction_paragraph_steps

1. 第一段：定义核心构念并给例子，累积学术重要性和商业后果。

2. 第二段：用‘尽管A广泛研究，但B未研究’制造跨领域gap，再列2-3个具体技术限制。

3. 第三段：宣布本文解决方案，并预告框架组件。

4. 第四段：引入第二个理论概念，证明它与第一个概念互补，把互补性转化为设计决策，并预告证据链。

5. 第五段：列出二至三项贡献，最后用最强现实证据（部署或经济效益）收束。

### theory_to_design_steps

1. 从理论构念中提炼可计算维度，每个维度对应一个公式组件。

2. 为每个组件提供文献依据或理论假设。

3. 给出整合所有组件的核心公式。

4. 说明具体假设如何产生具体测量模型。

5. 进入设计阶段后，用‘现有方法固定参数’作为设计缺口。

6. 把理论互补性转化为新的效用函数，并以配置矩阵实例化。

### method_and_study_sequence_steps

1. 先做测量效度验证（问卷或行为外部标准）。

2. 再把测量嵌入推荐设计。

3. 再用多数据集离线benchmark与多类baseline比较。

4. 再升级到线上随机实验证明真实业务效应。

5. 最后做异质性、平行趋势和稳健性分析。

### results_reporting_steps

1. 先报告主结果和主指标。

2. 再报告与baseline的相对提升。

3. 再报告最优模型选择。

4. 再补充跨数据集泛化或稀疏度robustness。

5. 每个声明后紧跟图表编号。

### discussion_and_contribution_steps

1. 重述核心构念重要性和两个框架。

2. 重述机制。

3. 重述关键证据并补充‘对谁有效’的异质性。

4. 用部署声明作为现实锚点。

5. 明确边界条件。

6. 列出未来工作（垂直差异、其他平台、动态测量、产品侧解释）。

## 可执行写作算法

### 1. 1

- step：1

- rhetorical_job_cn：定义核心构念并建立其学术与商业重要性。

- research_evidence_required_cn：构念的定义文献、重要性文献、商业后果文献。

- sentence_pattern_function_cn：一句定义+一个例子+一组重要性文献+一个商业结果。

- transition_condition_cn：读者已经认可‘这个构念重要’。

### 2. 2

- step：2

- rhetorical_job_cn：在目标领域制造研究缺口并列出具体技术限制。

- research_evidence_required_cn：目标领域文献中确实存在的2-3个具体方法缺陷。

- sentence_pattern_function_cn：一句跨领域对比+第一限制+第二限制+第三限制。

- transition_condition_cn：限制清单已经形成，且每个限制都能由后续设计组件回应。

### 3. 3

- step：3

- rhetorical_job_cn：宣布测量框架并说明组件。

- research_evidence_required_cn：每个组件有理论或文献依据，且能组合出多个可测试模型。

- sentence_pattern_function_cn：一句方案+一句框架结构+一句‘具体假设产生具体模型’。

- transition_condition_cn：框架已经具备可实例化逻辑。

### 4. 4

- step：4

- rhetorical_job_cn：验证测量构念效度。

- research_evidence_required_cn：外部效标（问卷/自我报告）、baseline准则、相关或分类指标、显著性检验。

- sentence_pattern_function_cn：一句‘用标准方法验证’+一句数据描述+一句结果+一句消融。

- transition_condition_cn：测量已被外部效标支持，且每个组件都显示必要性。

### 5. 5

- step：5

- rhetorical_job_cn：把测量嵌入下游设计框架。

- research_evidence_required_cn：一个能指导设计决策的理论互补性论证，以及可配置的模型矩阵。

- sentence_pattern_function_cn：一句现有模型基线+一句固定参数不足+一句互补性机制+一个公式+一个配置表。

- transition_condition_cn：设计框架已覆盖多个可测试模型，并有一个理论上最优候选。

### 6. 6

- step：6

- rhetorical_job_cn：用多数据集离线实验证明相对优势。

- research_evidence_required_cn：多个代表性数据集、多类baseline、公平超参优化、主要指标。

- sentence_pattern_function_cn：一句任务选择理由+一句数据集介绍+一句baseline列表+一句结果+一句泛化宣称。

- transition_condition_cn：离线结果在多个数据集都显著，且能推出外部效度声明。

### 7. 7

- step：7

- rhetorical_job_cn：用线上随机实验证明真实业务效应。

- research_evidence_required_cn：平台合作、随机分流、业务指标、因果识别策略。

- sentence_pattern_function_cn：一句动机+一句平台背景+一句分流方法+一句识别方程+一句结果+一句部署。

- transition_condition_cn：线上结果显著，且具备可解释的机制方向和部署证据。

### 8. 8

- step：8

- rhetorical_job_cn：用异质性、平行趋势和稳健性把平均效应转化为机制与边界。

- research_evidence_required_cn：处理×个体特征交互、预处理期数据、替代模型设定。

- sentence_pattern_function_cn：一句异质性发现+一句机制解释+一句平行趋势+一句稳健性清单。

- transition_condition_cn：结果能同时说明‘总体有效’和‘谁更有效’，且经得起替代设定。

### 9. 9

- step：9

- rhetorical_job_cn：在结论中把结果组织为贡献、边界和未来。

- research_evidence_required_cn：全部证据总结、明确的边界条件、可执行的未来方向。

- sentence_pattern_function_cn：一句重述重要性+一句框架总结+一句机制+一句证据+一句边界+一串未来工作。

- transition_condition_cn：读者能清晰提取可复用设计知识和研究边界。

## 应模仿的高价值动作

1. 用‘三组件框架’把抽象行为构念形式化为可计算模块，每个组件都有独立理论依据。

2. 在测量阶段就使用用户问卷自报数据作为外部效标，而不是只依赖内部一致性。

3. 把时间衰减作为stationarity的必要条件，用ADF检验把行为假设变成统计事实。

4. 用‘产品中心vs消费者中心’的概念对比建立unexpectedness与variety seeking的互补性。

5. 把固定α的现有模型作为明确设计缺口，再用variety seeking水平推导个性化权重。

6. 离线实验覆盖三种行业数据集和四类baseline，并说明公平超参优化。

7. 用线上随机分流+时间固定效应回归作为因果识别策略，并用倾向值分布验证平衡。

8. 在平均ATE之后用异质性分析(20 bin交互项)揭示U型效应，连接机制。

9. 用平行趋势区分长期效果与暂时新奇效应。

10. 用‘公司部署’作为最终贡献锚点，并给出大致经济估算。

## 不要只复制的表面动作

1. 不应只模仿‘提出一个框架+多个变体’的外壳，而不为每个变体提供独立理论动机。

2. 不应只报告平均提升3.81%而忽略对baseline公平性的详细说明。

3. 不应把‘最优模型’作为投稿点，除非有在线实验和部署支撑。

4. 不应只依赖离线指标宣称经济影响，必须展示真实平台实验。

5. 不应把stationarity作为通用假设随手使用，而需用ADF等检验证据支撑。

## 证据薄弱或跳跃的动作

1. ‘潜在额外3000万美元收入’基于2.29% CTR提升与平台收入的比例假设，未做严格归因。

2. U型异质性被解释为个性化机制，但文章没有直接测量中间心理过程。

3. ‘所有消费者都受益’来自总体显著，个别bin在图上可能接近零且置信区间较宽。

4. stationarity假设只在有限时间跨度数据上验证，长期更广场景未测。

5. 机制验证依赖相关和交互效应，未做正式中介分析。

## 一句话套路

先把一个营销学构念操作化为三组件可计算框架并用用户问卷建立构念效度，再把该构念作为推荐效用函数的个性化参数，用多场景离线benchmark和大型线上随机实验证明行为理论驱动的技术设计能显著改善真实业务指标，最终以公司部署和机制异质性把一次性性能优势转化为IS层面可复用设计知识。

## 分析边界

分析基于全文正文，未包含在线附录（part I–X）的完整问卷题目、DID细节和更多稳健性表；图表只能依赖OCR文字和文中描述判断，个别数值可能存在OCR误差（例如Table 4中的星号标记和Table 1临界值），但不影响整体论证结构判断。
