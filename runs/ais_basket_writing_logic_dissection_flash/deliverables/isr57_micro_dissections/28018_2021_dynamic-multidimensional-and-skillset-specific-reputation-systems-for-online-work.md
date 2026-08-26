# Dynamic, Multidimensional, and Skillset-Specific Reputation Systems for Online Work：ISR 句段级微观图谱

- 作者：Marios Kokkodis
- 年份：2021
- DOI：10.1287/isre.2020.0972
- 源文件：28018_2021_dynamic-multidimensional-and-skillset-specific-reputation-systems-for-online-work.md
- 置信度：0.78

## 核实后的宏观骨架

本文为设计科学型ISR论文。宏观结构为：摘要→引言（市场背景→声誉重要性→三类缺陷→研究问题与三原则→结果预告→贡献声明→IA/未来工作意义）→研究背景（声誉系统综述并分类为人类/机器/混合→在线劳动市场声誉的膨胀/归因/静态性缺陷→逐类排除现有方案→表1缺口→设计原则→与推荐系统的概念辨析与适配映射→表2）→框架设计（三组件：W2V技能分解、HMM动态质量评估、聚合）→数据描述与模型无关证据（LaborBazaar；图2六面板证明三类缺陷）→变量定义→评价（10折交叉验证；组件网格搜索；5个替代声誉系统；四类结果：排序、分布、非完美工人、Open内排序；推荐系统适配与协作；预测/解释性能；餐馆评论泛化）→讨论（重述缺陷-组件-结果→研究贡献→方法论贡献与泛化→平台/工人/雇主/未来工作含义→离散状态、降级转移、W2V/D2V边界等建模讨论→结论）。核心论证从'现有一维静态膨胀评分不可靠'到'三设计原则'再到'三组件制品'，以离线benchmark、子群体分析、下游AUC协作和第二情境复制层层升级贡献。

## 摘要逐句图谱

### 1. Abstract P1 S1

- order：1

- locator：Abstract P1 S1

- paraphrase_cn：声誉系统通过建立信任和减小信息不对称提高数字工作场所的交易效率。

- move_code：OPEN_CONTEXT_AND_STAKES

- statement_status：prior_literature

- why_here_cn：开篇即给声誉系统在数字工作场所中的制度功能，让读者知道后续所有技术细节服务于什么目标。

- inherits_from_previous_cn：无；直接建立在平台经济中的信任机制文献共识上。

- changes_argument_state_cn：把声誉系统放上论证主舞台，设定'交易效率'作为最终评价参照。

- sets_up_next_cn：为下一句指出现有系统未捕捉动态多维属性提供对照。

- failure_if_removed_cn：删除后读者不知道为什么要关心声誉系统设计。

- evidence_pointer：Abstract第一句

### 2. Abstract P1 S2-S3

- order：2

- locator：Abstract P1 S2-S3

- paraphrase_cn：但是现有系统没有捕捉在线工作的动态多维本质；统一平均所有技能的评分忽略技能集特定异质性（归因），并隐含假定工人质量不随时间变化（静态性）。

- move_code：PROBLEM_AND_TWO_DEFECTS

- statement_status：author_inference

- why_here_cn：在摘要第二句就亮出两个核心概念性缺陷，让读者立刻知道论文要解决的问题。

- inherits_from_previous_cn：承接'声誉系统重要'，转折到'但现有设计不足'。

- changes_argument_state_cn：将论文任务界定为修复归因与静态性。

- sets_up_next_cn：为第三句加入膨胀缺陷并说明后果。

- failure_if_removed_cn：摘要就没有研究问题。

- evidence_pointer：Abstract第二、三句

### 3. Abstract P1 S4-S5

- order：3

- locator：Abstract P1 S4-S5

- paraphrase_cn：声誉分数还过度正向（膨胀），因此常不能有效区分工人。

- move_code：THIRD_DEFECT_AND_CONSEQUENCE

- statement_status：author_inference

- why_here_cn：补上第三个缺陷，并直接给出'不能区分工人'的行为后果，使三缺陷组合成一个完整问题。

- inherits_from_previous_cn：承接静态性与归因，把问题从'不准确'扩展到'不具区分力'。

- changes_argument_state_cn：问题界定完整：一个系统同时有归因、静态性、膨胀三重失败。

- sets_up_next_cn：为下一句'因此本文提出新框架'提供必要性。

- failure_if_removed_cn：缺少膨胀，后文正态分布、区分工人等论证失去目标。

- evidence_pointer：Abstract第四、五句

### 4. Abstract P1 S6-S7

- order：4

- locator：Abstract P1 S6-S7

- paraphrase_cn：本文提出一个将人类输入与机器学习结合的增强智能声誉框架，提供动态、多维、技能集特定的工人声誉。

- move_code：PROPOSED_ARTIFACT

- statement_status：design_decision

- why_here_cn：在问题之后立即给出总体方案，并定义IA定位，让摘要形成'问题→方案'的紧凑结构。

- inherits_from_previous_cn：方案名称中的dynamic/multidimensional/skillset-specific逐一对应前述三缺陷。

- changes_argument_state_cn：论证从'现有系统不行'转为'我提供什么'。

- sets_up_next_cn：为下一句三组件拆解提供总纲。

- failure_if_removed_cn：缺少方案，摘要变成纯问题陈述。

- evidence_pointer：Abstract第六、七句

### 5. Abstract P1 S8-S12

- order：5

- locator：Abstract P1 S8-S12

- paraphrase_cn：框架由三组件构成：词嵌入把技能集映射到有限能力维（解决归因）；隐马尔可夫模型构建动态能力特定质量评估（解决静态性）；最终组件聚合生成技能集特定声誉分数。

- move_code：ARTIFACT_COMPONENTS

- statement_status：design_decision

- why_here_cn：把框架浓缩成三个可识别的组件，并逐一标注其解决的缺陷，使设计逻辑在摘要层面就能被验证。

- inherits_from_previous_cn：直接展开上一句提出的框架。

- changes_argument_state_cn：把抽象方案具体化为三个可计算的组件。

- sets_up_next_cn：为结果句说明'该组件组合在数据上带来三种改进'提供结构前提。

- failure_if_removed_cn：缺少组件描述，结果无法与设计原因挂钩。

- evidence_pointer：Abstract第八至十二句

### 6. Abstract P2 S1-S3

- order：6

- locator：Abstract P2 S1-S3

- paraphrase_cn：在包含58,459个完成任务的在线劳动市场数据上，该方法与10个替代声誉系统相比：（1）产生更合适的工人排序且声誉分布更接近正态，（2）更好地识别更可能表现不佳且更难预测的'非完美'工人，（3）改善Open内选择排序并产生显著更好的结果。

- move_code：MAIN_RESULTS

- statement_status：empirical_result

- why_here_cn：用三点数字结果预告主评价，让读者在摘要阶段就看到核心贡献的证据。

- inherits_from_previous_cn：结果的三点分别对应排序、膨胀缓解、非完美和Open内行为。

- changes_argument_state_cn：从'设计合理'推进到'经验上更优'。

- sets_up_next_cn：为下一句泛化结果提供第一情境对照。

- failure_if_removed_cn：缺少结果，摘要没有说服力。

- evidence_pointer：Abstract第二段第一至三句

### 7. Abstract P2 S4

- order：7

- locator：Abstract P2 S4

- paraphrase_cn：额外77,044条餐馆评论显示该框架成功泛化到评分过度正向且服务质量多维动态的替代情境。

- move_code：GENERALIZABILITY_RESULT

- statement_status：empirical_result

- why_here_cn：在劳动市场结果后立即提供第二个情境证据，证明贡献不是单数据集特例。

- inherits_from_previous_cn：承接主结果，扩展结论范围。

- changes_argument_state_cn：把'本市场有效'升级为'这类平台都可能有效'。

- sets_up_next_cn：为正文讨论泛化性和设计知识做预告。

- failure_if_removed_cn：贡献停留在单情境，无法支撑设计原则级主张。

- evidence_pointer：Abstract第二段第四句

## 引言逐句图谱

### 1. Introduction P1 S1

- order：1

- locator：Introduction P1 S1

- paraphrase_cn：在线劳动市场促进全球短期合同和自由职业工作。

- move_code：CONTEXT_OPENING

- statement_status：fact

- why_here_cn：以最常见的方式开场，先建立研究对象的存在性。

- inherits_from_previous_cn：无。

- changes_argument_state_cn：设定舞台：要讨论的平台类型。

- sets_up_next_cn：为下一句说明市场规模提供主语。

- failure_if_removed_cn：引言缺少背景锚点。

- evidence_pointer：Section 1 P1 S1

### 2. Introduction P1 S2

- order：2

- locator：Introduction P1 S2

- paraphrase_cn：买家从大量能完成网页开发、平面设计、会计、销售、营销、数据科学等多样化任务的在线工人处购买服务。

- move_code：CONTEXT_ELABORATION

- statement_status：fact

- why_here_cn：强调任务和技能的高度异质，为后文'归因'缺陷埋下第一个经验种子。

- inherits_from_previous_cn：承接'在线劳动市场存在'，细化其商品是多样化服务。

- changes_argument_state_cn：将舞台具体化为技能异质市场。

- sets_up_next_cn：为后文技能集特定性、技能集分解需求做铺垫。

- failure_if_removed_cn：后文'不同技能评分不同'就缺乏前置知识。

- evidence_pointer：Section 1 P1 S2

### 3. Introduction P1 S3-S4

- order：3

- locator：Introduction P1 S3-S4

- paraphrase_cn：与其他在线平台一样，在线劳动市场过去十年指数增长，这种增长会因自动化和共享经济塑造未来工作而继续或加速。

- move_code：MARKET_IMPORTANCE

- statement_status：fact

- why_here_cn：用指数增长和未来工作趋势提升话题紧迫性。

- inherits_from_previous_cn：承接平台存在，转而强调其规模与趋势。

- changes_argument_state_cn：把论文议题放进更宏观的未来工作背景。

- sets_up_next_cn：为第二段'信任与声誉是市场成功决定因素'提供重要性底座。

- failure_if_removed_cn：缺少增长背景，声誉系统的重要性缺少时代理由。

- evidence_pointer：Section 1 P1 S3-S4

### 4. Introduction P2 S1

- order：4

- locator：Introduction P2 S1

- paraphrase_cn：在线劳动市场成功的一个决定因素是平台在雇主与工人之间建立的中间信任。

- move_code：NARROW_TO_TRUST

- statement_status：prior_literature

- why_here_cn：从广阔市场背景收束到信任机制，作为进入声誉系统的桥梁。

- inherits_from_previous_cn：在'市场成功'前提下，提出其决定因素之一。

- changes_argument_state_cn：把关注焦点从市场总量移到制度机制。

- sets_up_next_cn：为下一句把声誉系统定义为信任机制进行铺垫。

- failure_if_removed_cn：声誉系统的重要性缺少中介概念。

- evidence_pointer：Section 1 P2 S1

### 5. Introduction P2 S2

- order：5

- locator：Introduction P2 S2

- paraphrase_cn：声誉系统是在线劳动市场用来增加信任、减少信息不对称的标准机制。

- move_code：DEFINE_OBJECT_OF_STUDY

- statement_status：prior_literature

- why_here_cn：明确研究对象：声誉系统。

- inherits_from_previous_cn：信任需要机制实现，声誉系统就是这种机制。

- changes_argument_state_cn：确立全文核心研究对象。

- sets_up_next_cn：为其后描述声誉如何积累和影响交易提供概念基础。

- failure_if_removed_cn：研究主题不明确。

- evidence_pointer：Section 1 P2 S2

### 6. Introduction P2 S3-S6

- order：6

- locator：Introduction P2 S3-S6

- paraphrase_cn：这些系统依靠人类输入：雇主对完成的任务评分，评分成为工人线上简历的一部分；声誉测度预期服务质量，增加雇主信任、促进交易；工人也依据声誉调整报价。

- move_code：ELABORATE_MECHANISM

- statement_status：prior_literature

- why_here_cn：详细说明声誉系统的工作机制与作用链，让后文的'系统缺陷'具有现实后果。

- inherits_from_previous_cn：在'声誉系统是标准机制'基础上说明其具体运作。

- changes_argument_state_cn：把声誉系统从一个名词变成一个因果链条：评分→简历→信任→交易→定价。

- sets_up_next_cn：第三段可顺着这条链指出链条在动态/多维情境下失效。

- failure_if_removed_cn：没有机制说明，缺陷就只是抽象抱怨。

- evidence_pointer：Section 1 P2 S3-S6

### 7. Introduction P3 S1

- order：7

- locator：Introduction P3 S1

- paraphrase_cn：尽管有这些好处，当前声誉系统设计没有捕捉在线工作的动态和多维本质。

- move_code：TURN_TO_LIMITATION

- statement_status：author_inference

- why_here_cn：从'系统有用'转向'系统设计不足'，是引言第一次转折。

- inherits_from_previous_cn：'这些好处'承接第二段全部内容，然后以'然而'转折。

- changes_argument_state_cn：开始问题化现有系统。

- sets_up_next_cn：为三类缺陷展开提供总括句。

- failure_if_removed_cn：缺少转折，引言就只是文献综述。

- evidence_pointer：Section 1 P3 S1

### 8. Introduction P3 S2-S5

- order：8

- locator：Introduction P3 S2-S5

- paraphrase_cn：声誉系统通过统一平均所有历史反馈，隐含假设工人质量不随时间演化；但新技能诞生、旧技能消失的速度比以往更快，工人必须持续再教育和再技能化。

- move_code：STATICITY_DEFECT

- statement_status：author_inference

- why_here_cn：在转折后先讲静态性，因为它直接关系到'未来工作'的动态议题。

- inherits_from_previous_cn：承接现有系统'统一平均'的设计特征。

- changes_argument_state_cn：建立第一个具体缺陷：静态性。

- sets_up_next_cn：为后文动态质量评估组件奠定动机。

- failure_if_removed_cn：HMM动态组件的动机缺失。

- evidence_pointer：Section 1 P3 S2-S5

### 9. Introduction P3 S6-S9

- order：9

- locator：Introduction P3 S6-S9

- paraphrase_cn：工人声誉分数还是一维且与技能集无关，但数字工作场所资质高度异质，工人常完成需要不同技能组合的任务，因此一维分数无法提供技能集特定的准确估计。

- move_code：ATTRIBUTION_DEFECT

- statement_status：author_inference

- why_here_cn：静态性之后提出归因，两者覆盖'时间'和'技能空间'两个维度。

- inherits_from_previous_cn：沿用'现有系统设计不捕捉动态多维本质'的总判断。

- changes_argument_state_cn：建立第二个缺陷：归因。

- sets_up_next_cn：为后文技能分解组件提供动机。

- failure_if_removed_cn：W2V分解组件的动机缺失。

- evidence_pointer：Section 1 P3 S6-S9

### 10. Introduction P3 S10-S13

- order：10

- locator：Introduction P3 S10-S13

- paraphrase_cn：与其他平台一样，在线劳动市场声誉分数过度正向，许多工人被评得'好于平均'，不能有效区分工人。

- move_code：INFLATION_DEFECT

- statement_status：author_inference

- why_here_cn：最后提出膨胀，并直接给出'不能区分'的后果，为后文正态分布目标提供依据。

- inherits_from_previous_cn：在时间与技能空间两个维度之后，补充反馈量尺本身的偏斜。

- changes_argument_state_cn：三缺陷全部到位。

- sets_up_next_cn：为研究问题和三原则提供问题集合。

- failure_if_removed_cn：缺少膨胀，后文'正态分布'和'区分工人'的目标失去来源。

- evidence_pointer：Section 1 P3 S10-S13

### 11. Introduction P4 S1

- order：11

- locator：Introduction P4 S1

- paraphrase_cn：考虑到当前声誉系统的这些不足，应如何设计动态、多维、技能集特定的声誉框架？

- move_code：RESEARCH_QUESTION

- statement_status：author_inference

- why_here_cn：在问题完整铺开后正式提出研究问题。

- inherits_from_previous_cn：'这些不足'直接指代三缺陷。

- changes_argument_state_cn：把问题从'系统有什么毛病'转为'该设计什么'。

- sets_up_next_cn：为下一句方案预告提供问题牵引。

- failure_if_removed_cn：缺少研究问题，论文没有中心任务。

- evidence_pointer：Section 1 P4 S1

### 12. Introduction P4 S2

- order：12

- locator：Introduction P4 S2

- paraphrase_cn：为回答该问题，作者提出一个增强智能系统，依赖三条设计原则：技能分解、动态能力特定质量评估、聚合。

- move_code：SOLUTION_PREVIEW

- statement_status：design_decision

- why_here_cn：紧接研究问题给出方案骨架和三条设计原则。

- inherits_from_previous_cn：研究问题直接引出设计原则。

- changes_argument_state_cn：从问题状态进入解决方案状态。

- sets_up_next_cn：为下一句逐条映射原则到缺陷提供列表。

- failure_if_removed_cn：方案缺失，论文无贡献对象。

- evidence_pointer：Section 1 P4 S2

### 13. Introduction P4 S3-S5

- order：13

- locator：Introduction P4 S3-S5

- paraphrase_cn：技能分解促进技能集特定声誉；动态质量评估解释工人学习新技能和获得专长的演化；聚合产生代表性（近正态）技能集特定信誉分布并促成工人区分。

- move_code：PRINCIPLE_DEFECT_MAPPING

- statement_status：author_inference

- why_here_cn：把三条原则与三个缺陷一一对应，并引入正态分布（Schmidt and Hunter 1983）作为设计目标，使方案看起来是逻辑必然。

- inherits_from_previous_cn：依次展开上一句的三个原则。

- changes_argument_state_cn：建立'原则-缺陷'映射，奠定框架结构与评价指标。

- sets_up_next_cn：为结果预测段提供三个承诺：更佳排序、近正态分布、区分度。

- failure_if_removed_cn：三组件设计缺乏理论逻辑，后文评价指标也失去定向。

- evidence_pointer：Section 1 P4 S3-S5

### 14. Introduction P5 S1-S2

- order：14

- locator：Introduction P5 S1-S2

- paraphrase_cn：对58,459个已完成任务的分析显示，所提方法显著优于10个先进替代声誉系统（包括当前市场声誉、链接分析、梯度提升、神经网络和推荐系统适配），尤其在排序相关、近正态分布、非完美工人识别和Open内排序上更好。

- move_code：MAIN_RESULT_PROMISE

- statement_status：empirical_result

- why_here_cn：在研究设计预告后立即给出核心实证承诺，让审稿人/读者早期就知晓证据强度。

- inherits_from_previous_cn：结果对象是三组件框架及其原则。

- changes_argument_state_cn：论证从'应然设计'进入'实证有效'。

- sets_up_next_cn：为下一句泛化结果提供对照。

- failure_if_removed_cn：引言缺少主结果，贡献主张没有支持。

- evidence_pointer：Section 1 P5 S1-S2

### 15. Introduction P5 S3

- order：15

- locator：Introduction P5 S3

- paraphrase_cn：额外77,044条餐馆评论分析显示框架成功泛化到反馈过度正向、服务质量多维且动态的替代情境。

- move_code：GENERALIZATION_PROMISE

- statement_status：empirical_result

- why_here_cn：用第二情境复制主结果，在引言阶段就把'单点优势'提升为'泛化设计'。

- inherits_from_previous_cn：承接劳动市场结果，扩展其范围。

- changes_argument_state_cn：把贡献从特定市场技术升级为可移植框架。

- sets_up_next_cn：为第六段贡献声明提供外部效度支撑。

- failure_if_removed_cn：泛化主张无证据，贡献级别降低。

- evidence_pointer：Section 1 P5 S3

### 16. Introduction P6 S1-S2

- order：16

- locator：Introduction P6 S1-S2

- paraphrase_cn：本文首次指出现有在线劳动市场声誉系统的不足并提出未来声誉系统应具备的设计原则。

- move_code：FIRST_CONTRIBUTION_CLAIM

- statement_status：contribution_claim

- why_here_cn：在结果之后给出理论/文献贡献声明，用'首次'定位。

- inherits_from_previous_cn：三缺陷和设计原则在结果支持后升级为贡献。

- changes_argument_state_cn：从'我们做了个更好的系统'转为'我们贡献了设计知识'。

- sets_up_next_cn：为下一句管理/市场价值贡献铺垫。

- failure_if_removed_cn：论文缺少贡献声明，变成纯算法报告。

- evidence_pointer：Section 1 P6 S1-S2

### 17. Introduction P6 S3-S5

- order：17

- locator：Introduction P6 S3-S5

- paraphrase_cn：准确分数（1）帮助工人区分，（2）指导雇主做出知情且快速（搜索成本降低）的决策，（3）使市场改进推荐算法并理解各潜在能力的供应分布；预测表现不佳工人还能提前警示雇主，减少负面结果并带来持续收入。

- move_code：MANAGERIAL_CONTRIBUTION

- statement_status：author_inference

- why_here_cn：把技术结果翻译成工人、雇主、平台三方的价值，使贡献符合IS期刊的实践关切。

- inherits_from_previous_cn：'准确分数'指代框架输出，'这些准确分数'为三个作用提供主语。

- changes_argument_state_cn：从技术贡献上升到管理/市场贡献。

- sets_up_next_cn：为第七段增强智能与未来工作含义提供落点。

- failure_if_removed_cn：技术贡献缺少IS层面的意义。

- evidence_pointer：Section 1 P6 S3-S5

### 18. Introduction P7 S1-S4

- order：18

- locator：Introduction P7 S1-S4

- paraphrase_cn：该IA框架展示人类输入与先进机器学习结合通过创造知情决策条件来增强智能；有效区分可引导劳动力供应再分配并指导职业路径顾问，其部署对工人、雇主、企业和未来工作有影响。

- move_code：IA_AND_FUTURE_WORK_FRAME

- statement_status：contribution_claim

- why_here_cn：把论文接回特刊主题'人类、算法与增强智能'，并扩大意义范围。

- inherits_from_previous_cn：承接三组件中的机器学习与人类评分結合。

- changes_argument_state_cn：把一篇技术设计论文嵌入更大的IS未来工作叙事。

- sets_up_next_cn：为正文第二、三节的具体设计和证据做宏大承诺。

- failure_if_removed_cn：文章与特刊主题脱节，且结尾缺社会意义。

- evidence_pointer：Section 1 P7 S1-S4

## 引言逐段图谱

### 1. Introduction P1

- order：1

- locator：Introduction P1

- opening_move_cn：界定平台类型并给出多样任务和服务提供者。

- development_move_cn：通过指数增长文献和未来工作趋势放大话题重要性。

- pivot_move_cn：无转折，始终保持宏观背景。

- closing_move_cn：以'增长将持续'结束，制造'为什么值得研究'的紧迫感。

- paragraph_job_cn：建立研究对象（在线劳动市场）及重要性，为第二段信任/声誉机制提供场景。

### 2. Introduction P2

- order：2

- locator：Introduction P2

- opening_move_cn：引入中间信任作为市场成功决定因素。

- development_move_cn：依次说明声誉系统定义、工作机制、对雇主/工人行为的作用。

- pivot_move_cn：无转折，从定义流畅过渡到作用。

- closing_move_cn：以工人根据声誉调整报价结束，说明声誉有实际经济后果。

- paragraph_job_cn：确立声誉系统作为核心研究对象的制度功能与因果链。

### 3. Introduction P3

- order：3

- locator：Introduction P3

- opening_move_cn：一句总转折'尽管有这些好处，但设计未捕捉动态多维本质'。

- development_move_cn：分别用静态性、归因、膨胀三段递进说明三个缺陷，每段都有现实机制与后果。

- pivot_move_cn：在同一段内从'好处'突然转向'不足'，属于全段转折。

- closing_move_cn：以'大多工人被评好于平均而无法区分'结束，为研究问题制造明确缺口感。

- paragraph_job_cn：把声誉系统的重要性反转为其设计缺陷，完成问题建构。

### 4. Introduction P4

- order：4

- locator：Introduction P4

- opening_move_cn：用研究问题句开段。

- development_move_cn：提出三原则，并逐条映射到缺陷，引入正态分布设计目标。

- pivot_move_cn：从问题到解决方案的转折发生在段首两句之间。

- closing_move_cn：以聚合产生近正态分布促进区分结束，把'设计原则'与'评价目标'连接。

- paragraph_job_cn：把研究问题转化为三条设计原则，预告三组件框架。

### 5. Introduction P5

- order：5

- locator：Introduction P5

- opening_move_cn：直接以'分析58,459个任务显示'开始报告主结果。

- development_move_cn：列出三大类改进，并给出10个替代系统范围。

- pivot_move_cn：从劳动市场结果转到餐馆评论泛化结果，是范围的扩展。

- closing_move_cn：以泛化结论结束，为贡献声明提供外部效度。

- paragraph_job_cn：提前展示核心实证证据，预告具体评价的层次。

### 6. Introduction P6

- order：6

- locator：Introduction P6

- opening_move_cn：用'首次'声明研究贡献。

- development_move_cn：列出准确分数对工人、雇主、市场的三方面价值，并延伸到预测干预减少负面结果。

- pivot_move_cn：从研究贡献转向实践/平台贡献。

- closing_move_cn：以'正面结果增加参与、产生收入'结束，把贡献连接到平台经济价值。

- paragraph_job_cn：把技术结果升格为研究贡献与管理价值。

### 7. Introduction P7

- order：7

- locator：Introduction P7

- opening_move_cn：把框架重新包装为IA系统。

- development_move_cn：论证区分促进供应再分配与职业建议，并列出对四类主体的影响。

- pivot_move_cn：从特定系统性能转向增强智能的广泛社会含义。

- closing_move_cn：以'对工人、雇主、企业和未来工作的影响'收尾，呼应特刊主题。

- paragraph_job_cn：把论文放入增强智能与未来工作叙事，完成引言全部任务。

## 理论到设计逐句图谱

### 1. Section 2.2.1 P1 S1

- order：1

- locator：Section 2.2.1 P1 S1

- paraphrase_cn：尽管声誉有多维效果，在线劳动市场声誉系统并不完美，并经历三类缺陷：膨胀、归因、静态性。

- move_code：FORMALIZE_THREE_DEFECTS

- statement_status：author_inference

- why_here_cn：在综述后正式给三缺陷命名，作为全文分类框架。

- inherits_from_previous_cn：承接2.2节'声誉在工作市场有重要作用'的综述。

- changes_argument_state_cn：把引言中零散问题转成正式术语。

- sets_up_next_cn：为2.2.1三个小节分别解释机制提供目录。

- failure_if_removed_cn：三缺陷没有正式定义，后文表格和实验失去语言。

- evidence_pointer：Section 2.2.1 P1 S1

### 2. Section 2.2.1 Reputation Inflation S1-S3

- order：2

- locator：Section 2.2.1 Reputation Inflation S1-S3

- paraphrase_cn：低评分工人无法被雇佣而离开市场，雇主有同伴压力给正面评分；两者结合使声誉分布正偏，每个工人都像'好于平均'。

- move_code：INFLATION_MECHANISM

- statement_status：author_inference

- why_here_cn：解释膨胀的两个微观机制，证明是一个系统性问题而非随机噪声。

- inherits_from_previous_cn：承接三缺陷命名中的第一个。

- changes_argument_state_cn：给膨胀提供机制基础，说明为何难以用现行平均分解决。

- sets_up_next_cn：为'膨胀分数形成噪声估计、不能区分'的下文后果作铺垫。

- failure_if_removed_cn：膨胀被当作可忽略偏差，后文正态目标没有依据。

- evidence_pointer：Section 2.2.1 Reputation Inflation段

### 3. Section 2.2.1 Reputation Inflation S4-S5

- order：3

- locator：Section 2.2.1 Reputation Inflation S4-S5

- paraphrase_cn：膨胀的声誉分数不能充分区分工人，因为它们形成服务质量的有噪声估计。

- move_code：INFLATION_CONSEQUENCE

- statement_status：author_inference

- why_here_cn：把膨胀连接到核心后果'不能区分'，使评价指标中的分布/正视性成为必要。

- inherits_from_previous_cn：承接膨胀机制。

- changes_argument_state_cn：膨胀的伤害被明确为区分失败。

- sets_up_next_cn：为聚合设计原则和正态分布目标做铺垫。

- failure_if_removed_cn：正态分布目标找不到问题来源。

- evidence_pointer：Section 2.2.1 Inflation段末

### 4. Section 2.2.1 Reputation Attribution S1-S5

- order：4

- locator：Section 2.2.1 Reputation Attribution S1-S5

- paraphrase_cn：当前系统提供一维总体声誉，但工作场所资质高度异质且工人完成多样技能集的任务，一维分数无法捕捉技能特定质量；用IT任务同时需要网络、C、Python的分数0.9作为例子反问。

- move_code：ATTRIBUTION_MECHANISM_AND_EXAMPLE

- statement_status：author_inference

- why_here_cn：用具体例子把抽象归因问题变成可感场景，是IS写作中'现象示例化'的典型动作。

- inherits_from_previous_cn：承接三缺陷中的归因。

- changes_argument_state_cn：归因从概念变成可检验的'分数到底属于哪个技能'问题。

- sets_up_next_cn：为技能分解组件提供最直接的用户需求。

- failure_if_removed_cn：技能分解动机缺少生动性和操作性。

- evidence_pointer：Section 2.2.1 Attribution段

### 5. Section 2.2.1 Reputation Staticity S1-S4

- order：5

- locator：Section 2.2.1 Reputation Staticity S1-S4

- paraphrase_cn：技能和专长快速演化，工人通过经验或学习新技能发展；当前系统统一平均评分、假定服务质量不变，这对电商产品成立但对不断获得专长的工人是误导。

- move_code：STATICITY_MECHANISM_AND_PRODUCT_ANALOGY

- statement_status：author_inference

- why_here_cn：用物理商品与工人的类比解释为什么静态假设有害，为HMM动态建模提供本质理由。

- inherits_from_previous_cn：承接三缺陷中的静态性，并呼应首节技能演化趋势。

- changes_argument_state_cn：静态性被证明是'把工人当商品'的设计错位。

- sets_up_next_cn：为动态质量估计组件提供设计需求。

- failure_if_removed_cn：HMM组件会被视为任意技术偏好。

- evidence_pointer：Section 2.2.1 Staticity段

### 6. Section 2.2.1 段尾 S1-S3

- order：6

- locator：Section 2.2.1 段尾 S1-S3

- paraphrase_cn：这些不足导致质量估计常不能预测未来表现，基于这类分数的决策可能造成失败合作并伤害市场，因此需要探索替代声誉系统。

- move_code：DEFECTS_TO_GAP

- statement_status：author_inference

- why_here_cn：把三缺陷从描述性现象转为需要行动的缺口语句，直接引出下一节'现有系统是否能解决'。

- inherits_from_previous_cn：综合三缺陷的后果。

- changes_argument_state_cn：论证从'系统有毛病'推进到'必须有替代'。

- sets_up_next_cn：为2.2.2逐类排除现有系统提供指令。

- failure_if_removed_cn：文献排除和框架设计缺少行动必要。

- evidence_pointer：Section 2.2.1段尾

### 7. Section 2.2.2 商业系统段 S1-S5

- order：7

- locator：Section 2.2.2 商业系统段 S1-S5

- paraphrase_cn：人类声誉系统经历膨胀；电商中归因出现在一维评分描述多维质量时；TripAdvisor的四维系统虽好但无法推广到任意维，而且动态产品仍经历静态性。

- move_code：EXCLUDE_HUMAN_SYSTEMS

- statement_status：prior_literature

- why_here_cn：逐一排除第一类系统，确立'即使多维人工系统也不够'的缺口。

- inherits_from_previous_cn：承接2.1对人类系统的分类。

- changes_argument_state_cn：证明商业人类系统无法解决三缺陷。

- sets_up_next_cn：为排除机器/混合系统设定同一分类框架。

- failure_if_removed_cn：表1中'商业声誉系统'一行失去论证背景。

- evidence_pointer：Section 2.2.2前半

### 8. Section 2.2.2 机器系统段 S1-S5

- order：8

- locator：Section 2.2.2 机器系统段 S1-S5

- paraphrase_cn：机器链接分析需要网络、不依赖评价测量，不适用人类感知的服务质量；混合系统目标不同或需要在线劳动市场无法获得的信息；总体上它们不针对三缺陷，因为它们所在情境不构成严重问题。

- move_code：EXCLUDE_MACHINE_HYBRID

- statement_status：prior_literature

- why_here_cn：排除第二、三类系统，强调情境不匹配。

- inherits_from_previous_cn：承接2.1机器与混合系统综述。

- changes_argument_state_cn：证明通用机器/混合系统解决的是别的问题。

- sets_up_next_cn：为接下来排除众包系统做铺垫。

- failure_if_removed_cn：表1大部分行失去排除逻辑。

- evidence_pointer：Section 2.2.2中段

### 9. Section 2.2.2 众包段 S1-S5

- order：9

- locator：Section 2.2.2 众包段 S1-S5

- paraphrase_cn：众包与在线劳动市场虽相似但工人付费高、技能高，众包系统过滤恶意工人的目标不适用；低技能AMT工人不受技能更替影响，因此众包方法不解决三缺陷。

- move_code：EXCLUDE_CROWDSOURCING

- statement_status：prior_literature

- why_here_cn：专门排除最容易被误以为适用的众包领域，保护在线劳动市场问题的独特性。

- inherits_from_previous_cn：承接'机器/混合系统不适用'，再处理最接近的情境。

- changes_argument_state_cn：把在线劳动市场与众包区分开，加强归因/静态性的特异性。

- sets_up_next_cn：为下一段讨论专门面向在线劳动市场的测试/链接方法。

- failure_if_removed_cn：审稿人可能质疑众包系统可迁移，缺口不完整。

- evidence_pointer：Section 2.2.2众包段

### 10. Section 2.2.2 技能测试段 S1-S5

- order：10

- locator：Section 2.2.2 技能测试段 S1-S5

- paraphrase_cn：基于项目反应理论的技能测试理论上能解决归因，但成本高、一次只测一个技能不能扩展、工人可只展示通过证明，且平台维护数百技能测试有成本。

- move_code：EXCLUDE_SKILL_TESTING

- statement_status：prior_literature

- why_here_cn：排除另一种可能被提出的归因方案，为无测试的自动分解留出空间。

- inherits_from_previous_cn：在众包排除后，处理专门面向在线劳动市场的机器方法。

- changes_argument_state_cn：测试方法因规模与披露问题出局。

- sets_up_next_cn：引出WorkerRank，作为与本文最接近的既有方法。

- failure_if_removed_cn：W2V分解的'无需测试'优势缺少对照。

- evidence_pointer：Section 2.2.2技能测试段

### 11. Section 2.2.2 WorkerRank段 S1-S3

- order：11

- locator：Section 2.2.2 WorkerRank段 S1-S3

- paraphrase_cn：WorkerRank用雇主隐含判断的链接分析排序工人；它不解决归因和静态性，但可能隐含缓解膨胀；第5节将实证证明本文方法在多个维度优于它。

- move_code：EXCLUDE_WORKERRANK_WITH_EMPIRICAL_PROMISE

- statement_status：prior_literature

- why_here_cn：把最贴近的在线劳动市场声誉方法单独挑出，既承认其价值又标示缺口，并预告直接benchmark。

- inherits_from_previous_cn：承接'专门面向在线劳动市场的混合方法'。

- changes_argument_state_cn：建立了本文与WorkerRank的直接竞争关系。

- sets_up_next_cn：为表1和5.2基准列表做铺垫。

- failure_if_removed_cn：最强基准消失，比较论证缺一环。

- evidence_pointer：Section 2.2.2 WorkerRank段

### 12. Section 2.2.3 P1 S1-S3

- order：12

- locator：Section 2.2.3 P1 S1-S3

- paraphrase_cn：表1比较了学术界和工业界相关声誉系统，显示它们没有明确解决三缺陷；本文通过提出三条设计原则填补缺口。

- move_code：TABLE_AS_GAP_EVIDENCE

- statement_status：author_inference

- why_here_cn：用表格把'缺口'可视化，是本文最核心的defect-to-requirement转换点。

- inherits_from_previous_cn：承接2.2.2对每个具体系统的排除。

- changes_argument_state_cn：文献排除被总结为'没有系统解决三缺陷'。

- sets_up_next_cn：为三条设计原则给出正式位置。

- failure_if_removed_cn：原则没有文献缺口支撑，贡献声明失去比较基础。

- evidence_pointer：Section 2.2.3 P1

### 13. Section 2.2.3 P1 S4-S9

- order：13

- locator：Section 2.2.3 P1 S4-S9

- paraphrase_cn：本文提出三原则：任意技能组合分解为有限能力维、动态估计能力特定声誉、按需聚合能力特定声誉生成技能集特定分数；分别解决归因、静态性和技能集特定性；由于人类能力近正态，准确技能集特定分数解决膨胀并促进区分。

- move_code：DESIGN_PRINCIPLES_DERIVATION

- statement_status：author_inference

- why_here_cn：正式陈述三条设计原则，并把每条原则映射到缺陷和理论依据（正态分布）。

- inherits_from_previous_cn：承接表1缺口。

- changes_argument_state_cn：从缺口转向设计语言，为第3节组件结构定下蓝图。

- sets_up_next_cn：为第3节三组件（W2V/HMM/聚合）提供一一对应。

- failure_if_removed_cn：第3节组件没有设计原则支撑，论文退化为算法集合。

- evidence_pointer：Section 2.2.3 P1 S4-S9

### 14. Section 2.3 P1 S1-S2

- order：14

- locator：Section 2.3 P1 S1-S2

- paraphrase_cn：与声誉系统类似，推荐系统也解决信息不对称并帮助更好决策；那么推荐系统能否解决三缺陷并提供当前技能集特定工人声誉？

- move_code：INTRODUCE_ALTERNATIVE_FRAMEWORK

- statement_status：author_inference

- why_here_cn：主动提出另一个潜在方案家族，为后文排除推荐系统适配制造问题。

- inherits_from_previous_cn：在声誉缺口确定后，问'相邻技术能否填这个缺口'。

- changes_argument_state_cn：把'声誉系统文献内方案'扩展到'相邻的推荐系统方案'。

- sets_up_next_cn：为2.3.1概念差异和2.3.2映射提供结构。

- failure_if_removed_cn：5.4.1推荐系统基准会失去论证位置。

- evidence_pointer：Section 2.3 P1

### 15. Section 2.3.1 P1-S2

- order：15

- locator：Section 2.3.1 P1-S2

- paraphrase_cn：声誉系统范围更广：可生成排名、提供质量估计影响估值、形成期望、给管理者反馈、邀请工人申请；推荐系统常服务单一目标。

- move_code：REPUTATION_VS_RECOMMENDER_DISTINCTION

- statement_status：prior_literature

- why_here_cn：从功能范围上区分两者，说明为何不能简单替换。

- inherits_from_previous_cn：承接'推荐系统能否解决'问题，先否定前提。

- changes_argument_state_cn：推荐系统被定位为更窄工具，声誉价值更广。

- sets_up_next_cn：为2.3.2的映射困难做概念基础。

- failure_if_removed_cn：推荐系统基准实验失去'为什么重要'的理由。

- evidence_pointer：Section 2.3.1

### 16. Section 2.3.2 P1-S4

- order：16

- locator：Section 2.3.2 P1-S4

- paraphrase_cn：要将传统推荐系统应用于该情境，需要把评分映射为技能集平均反馈、用户映射为工人、物品映射为技能集；困难在于任务是唯一物品，每个任务只有一个评分，因此需把相同技能集任务当作相同物品。

- move_code：MAPPING_ASSUMPTIONS

- statement_status：author_inference

- why_here_cn：具体说明推荐系统适配所需的形式化映射，为5.4.1的实证失败提供机制解释。

- inherits_from_previous_cn：承接概念差异，转向'能否适配'的具体条件。

- changes_argument_state_cn：推荐系统从概念替代变成了一组可测试的编码假设。

- sets_up_next_cn：为序列推荐和编码假设段做铺垫。

- failure_if_removed_cn：表2的'Required modifications'和5.4.1没有逻辑来源。

- evidence_pointer：Section 2.3.2前四段

### 17. Section 2.3.2 序列感知段 S1-S4

- order：17

- locator：Section 2.3.2 序列感知段 S1-S4

- paraphrase_cn：序列感知推荐系统虽能处理静态性，但主要用隐式反馈而忽略显式评分，而声誉框架需要显式反馈；因此应用需要大量编码假设，5.4.1将讨论这些假设。

- move_code：ENCODING_DEFECT_PREVIEW

- statement_status：author_inference

- why_here_cn：提前预告序列推荐系统的先天不足，并在同段把它与声誉系统对显式反馈的需求对照。

- inherits_from_previous_cn：承接映射困难，转向序列推荐这一可能解。

- changes_argument_state_cn：即使能解决静态性，序列推荐也因反馈类型不匹配而失败。

- sets_up_next_cn：直接指向5.4.1的编码实验。

- failure_if_removed_cn：CNN序列推荐的编码实验显得武断。

- evidence_pointer：Section 2.3.2序列感知段

### 18. Section 2.3.2 表2段 S1-S2

- order：18

- locator：Section 2.3.2 表2段 S1-S2

- paraphrase_cn：表2比较推荐系统相关文献与本文方法，展示推荐系统提供工人声誉所需的必要改动；这些改动在5.4和图8中显著伤害推荐系统性能，凸显情境适配声誉系统的需要。

- move_code：TABLE2_AS_FALSIFICATION_PREVIEW

- statement_status：author_inference

- why_here_cn：用表2把推荐系统适配的成本可视化，并在同一句预告实证结果，形成'理论上要改、改了就坏'的反论。

- inherits_from_previous_cn：承接映射与编码假设。

- changes_argument_state_cn：把推荐系统从竞争者变为被排除候选。

- sets_up_next_cn：为5.4.1的基准结果提供双重预告（表和句）。

- failure_if_removed_cn：推荐系统适配实验没有理论预告，读者会以为只是性能差。

- evidence_pointer：Section 2.3.2表2下段

## 制品设计理由逐句图谱

### 1. Section 3 P1 S1-S4

- order：1

- locator：Section 3 P1 S1-S4

- paraphrase_cn：框架HMM-W2V由三组件组成：A分解技能到能力维，B动态估计能力特定质量，C聚合生成任意技能集质量。

- move_code：OVERALL_ARTIFACT_STRUCTURE

- statement_status：design_decision

- why_here_cn：在理论原则之后立即把三原则实例化为制品结构，是theory-to-design的落点。

- inherits_from_previous_cn：三组件逐一对应Section 2.2.3三条原则。

- changes_argument_state_cn：论证从抽象原则进入可实现系统。

- sets_up_next_cn：为3.1、3.2、3.3逐节描述组件提供目录。

- failure_if_removed_cn：框架没有统一定义，后文公式与实验没有整体归属。

- evidence_pointer：Section 3 P1

### 2. Section 3.1 P1 S1-S4

- order：2

- locator：Section 3.1 P1 S1-S4

- paraphrase_cn：直接估计每个技能集上的声誉有三个缺点：数据稀疏、忽略技能集间相关、新技能需重训。

- move_code：DESIGN_DEFECT_MOTIVATION

- statement_status：author_inference

- why_here_cn：在描述组件前先论证'直接做法不可行'，用三个缺点证明需要分解映射。

- inherits_from_previous_cn：承接'要对任意技能集估计声誉'的需求。

- changes_argument_state_cn：排除了朴素估计方案，为W2V设定必要性。

- sets_up_next_cn：为下一句引入W2V作为解法。

- failure_if_removed_cn：W2V组件看起来像任意的技术选择。

- evidence_pointer：Section 3.1 P1

### 3. Section 3.1 P2 S1-S3

- order：3

- locator：Section 3.1 P2 S1-S3

- paraphrase_cn：用W2V把技能当作词、技能集当作文档，将相似技能投影到D维能力空间中靠近。

- move_code：W2V_SKILL_MAPPING_DESIGN

- statement_status：design_decision

- why_here_cn：描述组件A的具体机制，并点明D为超参数。

- inherits_from_previous_cn：回应直接估计的三个缺点，用词嵌入提供可扩展映射。

- changes_argument_state_cn：把技能分解从原则落实为可计算公式的组件。

- sets_up_next_cn：为公式(1)(2)和替代方法比较做铺垫。

- failure_if_removed_cn：组件A没有内容，框架不完整。

- evidence_pointer：Section 3.1 P2

### 4. Section 3.1 P3 S1-S2

- order：4

- locator：Section 3.1 P3 S1-S2

- paraphrase_cn：可用D2V或简单聚类替代W2V；也可在技能集之外加入职位描述文本；附录C.1和图11(a)讨论并实证比较这些替代。

- move_code：ALTERNATIVE_DESIGN_OPENNESS

- statement_status：method_decision

- why_here_cn：说明组件选择是可检验的，不以作者偏好替代经验比较。

- inherits_from_previous_cn：承接W2V方案，开放替代空间。

- changes_argument_state_cn：设计论证进入'我们比较后选择'模式。

- sets_up_next_cn：为5.1网格搜索和附录C建立指针。

- failure_if_removed_cn：组件选择缺乏方法论严谨性。

- evidence_pointer：Section 3.1 P3

### 5. Section 3.2 P1 S1-S5

- order：5

- locator：Section 3.2 P1 S1-S5

- paraphrase_cn：每个工人每个能力维的质量是潜在且动态演化的；每次完成新任务并提供反馈后，框架观察到新证据并随机转移到新的潜在状态。

- move_code：DYNAMIC_LATENT_QUALITY_ASSUMPTION

- statement_status：theory_claim

- why_here_cn：为HMM组件建立行为假设：工人质量是潜在且随证据更新。

- inherits_from_previous_cn：直接实现第2.2.1静态性批判和第2.2.3第二原则。

- changes_argument_state_cn：质量从静态变量变为带状态转移的潜在过程。

- sets_up_next_cn：为HMM结构公式(3)-(7)提供概念框架。

- failure_if_removed_cn：HMM组件没有行为动机，成为纯统计建模。

- evidence_pointer：Section 3.2 P1

### 6. Section 3.2 HMM Structure段 S1-S4

- order：6

- locator：Section 3.2 HMM Structure段 S1-S4

- paraphrase_cn：新工人落入初始状态s1；完成第一个任务发出观测后按模型参数随机转移到其他状态。

- move_code：INITIAL_STATE_DESIGN

- statement_status：design_decision

- why_here_cn：规定新工人无历史时的初始状态，保证框架可处理零历史工人。

- inherits_from_previous_cn：在'工人从潜在状态出发'的假设上具体化初态。

- changes_argument_state_cn：模型从抽象到可估计：有了π向量。

- sets_up_next_cn：为公式(3)初始概率向量提供语义。

- failure_if_removed_cn：新工人无法获得声誉估计。

- evidence_pointer：Section 3.2 HMM Structure段

### 7. Section 3.2 HMM Structure段 S5-S7

- order：7

- locator：Section 3.2 HMM Structure段 S5-S7

- paraphrase_cn：用历史信号（总收入、雇佣率、完成任务数等）形成Z向量，经技能权重映射成能力特定历史，直接影响转移概率。

- move_code：TRANSITION_VARIABLES_DESIGN

- statement_status：design_decision

- why_here_cn：把'经验积累影响质量'这一行为假设操作化为转移函数的输入。

- inherits_from_previous_cn：在HMM转移矩阵机制上加入情境变量。

- changes_argument_state_cn：HMM从通用模型变成劳动力市场适配模型。

- sets_up_next_cn：为第4.2节变量选择和公式(4)(5)提供来源。

- failure_if_removed_cn：动态演化缺乏经验信号，模型不能随工人历史更新。

- evidence_pointer：Section 3.2 HMM Structure段

### 8. Section 3.2 HMM Structure段 S8-S10

- order：8

- locator：Section 3.2 HMM Structure段 S8-S10

- paraphrase_cn：观测工人特征（小时费率和平均反馈）构成X向量，加权后影响发射分布，即给定状态下观测得分的概率。

- move_code：EMISSION_VARIABLES_DESIGN

- statement_status：design_decision

- why_here_cn：让观测反馈不仅依赖潜在状态，还受工人可观测特征影响，提高模型现实性。

- inherits_from_previous_cn：承接HMM的发射矩阵需求，引入情感化变量。

- changes_argument_state_cn：发射模型从状态独有变为状态+特征。

- sets_up_next_cn：为公式(6)(7)和附录B参数估计做铺垫。

- failure_if_removed_cn：发射模型忽略工人特征，可能混淆状态与特征效应。

- evidence_pointer：Section 3.2 HMM Structure段

### 9. Section 3.3 P1 S1-S3

- order：9

- locator：Section 3.3 P1 S1-S3

- paraphrase_cn：每个能力维独立估计质量p_it^d；聚合时对任意技能集求和得到P_it(R)，软最大化权重使每个能力维按相应权重贡献。

- move_code：AGGREGATION_DESIGN

- statement_status：design_decision

- why_here_cn：描述组件C如何把能力维估计转成可用的技能集特定分数，并解释公式(8)中权重来源。

- inherits_from_previous_cn：承接组件A得到的软最大权重和组件B得到的能力特定估计。

- changes_argument_state_cn：三组件正式连通：A提供权重，B提供状态，C输出分数。

- sets_up_next_cn：为评价中的技能集特定排序提供操作定义。

- failure_if_removed_cn：框架没有最终输出，评价无从进行。

- evidence_pointer：Section 3.3 P1

### 10. Section 4.1 P1 S1-S3

- order：10

- locator：Section 4.1 P1 S1-S3

- paraphrase_cn：平台雇主用1/9到9/9分数评分，平台支持先进声誉系统：双向两周盲评，图2(a)显示分布均值中位数0.86，多数工人近乎完美（膨胀）。

- move_code：MODEL_FREE_INFLATION_EVIDENCE

- statement_status：empirical_result

- why_here_cn：用真实数据先证明膨胀存在，不依赖任何模型，是'现象驱动设计'的关键证据。

- inherits_from_previous_cn：承接第4节数据介绍。

- changes_argument_state_cn：膨胀从文献主张变成直接可见分布。

- sets_up_next_cn：为图2(b)-(f)的归因和静态性证据做并列准备。

- failure_if_removed_cn：设计动机停留在二手文献，实证驱动链条断裂。

- evidence_pointer：Section 4.1 P1、Figure 2(a)

### 11. Section 4.1 P2 S1-S3

- order：11

- locator：Section 4.1 P2 S1-S3

- paraphrase_cn：图2(b)显示不同技能评分不同（翻译中位数1均值0.91，Twitter营销中位数7/9均值0.74）；图2(c)连续任务技能集余弦相似度仅0.33，而潜在空间相似度0.75。

- move_code：MODEL_FREE_ATTRIBUTION_EVIDENCE

- statement_status：empirical_result

- why_here_cn：用分技能评分差异和连续任务异质性证明归因问题，同时预演W2V潜在空间能捕捉技能间上下文相似性。

- inherits_from_previous_cn：承接前一模型的描述性证据模式，转向归因。

- changes_argument_state_cn：归因从理论概念变成两个数据图表，并顺带给出W2V合理性的早期提示。

- sets_up_next_cn：为图2(d)-(f)的动态证据切换。

- failure_if_removed_cn：W2V组件的能力相似性优势缺少前置证据。

- evidence_pointer：Section 4.1 P2、Figure 2(b)(c)

### 12. Section 4.1 P3 S1-S4

- order：12

- locator：Section 4.1 P3 S1-S4

- paraphrase_cn：图2(d)约47%工人在12个月内使用至少一个新技能；图2(e)新技能后66%初始低分；图2(f)经验增加后声誉回升。三图共同突出静态性问题。

- move_code：MODEL_FREE_STATICITY_EVIDENCE

- statement_status：empirical_result

- why_here_cn：用工人学习新技能的纵向模式证明质量动态性，并把'新技能先低后回升'的轨迹作为静态评分的失效证据。

- inherits_from_previous_cn：承接归因证据，转向时间维度。

- changes_argument_state_cn：静态性从设计批判变成可观察的典型轨迹。

- sets_up_next_cn：为第5节评价建立'质量确实动态'前提。

- failure_if_removed_cn：HMM动态组件的主体必要性没有现场数据支持。

- evidence_pointer：Section 4.1 P3、Figure 2(d)-(f)

### 13. Section 4.2 P1 S1-S3

- order：13

- locator：Section 4.2 P1 S1-S3

- paraphrase_cn：HMM需要确定转移变量（累计声誉、总收入、完成任务数、工作小时、雇佣率）和发射变量（当前声誉、小时费率）。

- move_code：VARIABLE_OPERATIONALIZATION

- statement_status：method_decision

- why_here_cn：把第3.2节的Z和X从符号操作化为具体数据变量，连接模型与现实。

- inherits_from_previous_cn：承接公式(4)(6)对Z和X的要求。

- changes_argument_state_cn：HMM模型得到可估计的输入清单。

- sets_up_next_cn：为表4描述统计和5.1调参提供变量列表。

- failure_if_removed_cn：模型不可复现，评价无从谈起。

- evidence_pointer：Section 4.2 P1、Table 4

### 14. Section 4.2 P2 S1

- order：14

- locator：Section 4.2 P2 S1

- paraphrase_cn：该变量清单是情境特定的；附录E.3展示其他情境需要不同变量选择。

- move_code：CONTEXT_SPECIFICITY_NOTE

- statement_status：author_inference

- why_here_cn：预先承认变量选择可迁移而非普适，为餐馆评论泛化时的变量调整铺设合法空间。

- inherits_from_previous_cn：承接变量操作化。

- changes_argument_state_cn：框架被定位为可调整模板而非固定参数。

- sets_up_next_cn：为5.5泛化测试和讨论边界做铺垫。

- failure_if_removed_cn：餐馆情境变量不同会被视为方法不一致。

- evidence_pointer：Section 4.2 P2

## Study开头、过渡与收束图谱

### 1. Section 5 P1 S1-S2

- order：1

- study_or_phase：评价总协议

- locator：Section 5 P1 S1-S2

- paraphrase_cn：第5节描述建模选择、调参并比较各替代声誉系统和修改推荐系统；按工人划分10折，每个工人完整历史只在一折。

- move_code：EVALUATION_PROTOCOL_OPENING

- statement_status：method_decision

- why_here_cn：在进入结果前固定评估协议，防止信息泄漏并保证所有比较公平。

- inherits_from_previous_cn：承接第4节数据，把数据变为可比较的评估设置。

- changes_argument_state_cn：所有后文结果都在这一个协议内成立。

- sets_up_next_cn：为5.1调参和5.2基准列表提供规则。

- failure_if_removed_cn：基准比较无统一协议，所有数字都可被质疑。

- evidence_pointer：Section 5 P1

### 2. Section 5.1 P1 S1-S3

- order：2

- study_or_phase：设计选择与调参

- locator：Section 5.1 P1 S1-S3

- paraphrase_cn：对组件A/B/C和维度数、状态数、转移/发射函数做网格搜索，附录C给出细节。

- move_code：GRID_SEARCH_OPENING

- statement_status：method_decision

- why_here_cn：说明最终配置不是拍脑袋，而是在候选集中选优。

- inherits_from_previous_cn：承接第3节替代设计选项和第5节评估协议。

- changes_argument_state_cn：为最终HMM-W2V版本提供选择依据。

- sets_up_next_cn：为下一段报告各组件最佳选择做铺垫。

- failure_if_removed_cn：最终制品缺乏可辩护的配置过程。

- evidence_pointer：Section 5.1 P1

### 3. Section 5.1 P2 S1-S5

- order：3

- study_or_phase：设计选择结果

- locator：Section 5.1 P2 S1-S5

- paraphrase_cn：报告最终选择：W2V优于D2V和GMM；HMM显著优于线性/SVM/LSTM/XGBoost；公式(8)聚合最优；|D|=10；K、Beta发射、多项logit转移。

- move_code：CONFIGURATION_RESULTS

- statement_status：empirical_result

- why_here_cn：把网格搜索压缩成终选列表，既透明又简短。

- inherits_from_previous_cn：在网格搜索结构下逐项报告。

- changes_argument_state_cn：HMM-W2V的具体版本被固定，后续所有比较使用该版本。

- sets_up_next_cn：为5.2定义替代系统提供'被比较方'。

- failure_if_removed_cn：主结果没有明确的制品版本支撑。

- evidence_pointer：Section 5.1 P2及附录C

### 4. Section 5.2 P1-S2

- order：4

- study_or_phase：替代声誉系统

- locator：Section 5.2 P1-S2

- paraphrase_cn：实现当前声誉、线性模型、LSTM、XGBoost、SVM回归、WorkerRank作为替代声誉系统。

- move_code：BASELINE_DEFINITION

- statement_status：method_decision

- why_here_cn：明确基准集合，使'优于10个系统'的声明可验证。

- inherits_from_previous_cn：前文表1的排除和WorkerRank预告在此实例化。

- changes_argument_state_cn：建立比较矩阵：1个HMM-W2V对6类声誉候选。

- sets_up_next_cn：为5.3多指标结果提供对手名单。

- failure_if_removed_cn：主结果没有对照物。

- evidence_pointer：Section 5.2

### 5. Section 5.3 Ranking Workers P1 S1-S3

- order：5

- study_or_phase：排序工人结果

- locator：Section 5.3 Ranking Workers P1 S1-S3

- paraphrase_cn：声誉系统最终目标是为预期服务质量排序工人，因此用排序相关、分位表现和lift衡量。

- move_code：METRIC_JUSTIFICATION

- statement_status：method_decision

- why_here_cn：在报告数字前先说明为什么用这三个指标，把指标锚定到系统目标。

- inherits_from_previous_cn：承接'准确评估应排序工人'的功能定义。

- changes_argument_state_cn：排序成为首要评价目标。

- sets_up_next_cn：为图3、图4的结果做操作定义。

- failure_if_removed_cn：排序指标显得随意。

- evidence_pointer：Section 5.3 Ranking Workers开头

### 6. Section 5.3 Ranking Workers P2-P3

- order：6

- study_or_phase：排序相关结果

- locator：Section 5.3 Ranking Workers P2-P3

- paraphrase_cn：HMM-W2V比当前声誉排序平均高85%，比所有替代系统高20%-60%，p<0.001。

- move_code：CORE_RANKING_RESULT

- statement_status：empirical_result

- why_here_cn：给出第一个硬结果，同时给出改进幅度、方向和显著性。

- inherits_from_previous_cn：承接排序相关指标定义。

- changes_argument_state_cn：主优势声明成立。

- sets_up_next_cn：为分位表现和lift结果提供同一层次的额外证据。

- failure_if_removed_cn：摘要和引言中的主承诺失去数据。

- evidence_pointer：Section 5.3、Figure 3

### 7. Section 5.3 Reputation Distribution P1

- order：7

- study_or_phase：分布结果

- locator：Section 5.3 Reputation Distribution P1

- paraphrase_cn：用总变差距离测度各声誉分布与正态分布的接近程度；HMM-W2V比替代系统近最多37%。

- move_code：DISTRIBUTION_RESULT

- statement_status：empirical_result

- why_here_cn：把'近正态'从设计目标变为可计算指标，并报告对比结果。

- inherits_from_previous_cn：承接Schmidt-Hunter正态假设和引言中对膨胀的批判。

- changes_argument_state_cn：膨胀缓解得到直接量化证据。

- sets_up_next_cn：为'不能只靠整体指标'的非完美工人分析做过渡。

- failure_if_removed_cn：正态设计目标无实证支持。

- evidence_pointer：Section 5.3 Reputation Distribution、Figure 5

### 8. Section 5.3 Nonperfect Workers P1-S2

- order：8

- study_or_phase：非完美工人结果

- locator：Section 5.3 Nonperfect Workers P1-S2

- paraphrase_cn：许多工人因膨胀总是显得完美，因此模型只要预测完美工人就有高准确率；真正的挑战是少数偶尔表现不佳的工人，提前识别可防止失望体验。

- move_code：SUBGROUP_OPENING

- statement_status：author_inference

- why_here_cn：先说明为何要做子群体分析：整体准确率会被膨胀掩盖，再用'预警价值'解释为何重要。

- inherits_from_previous_cn：承接分布结果中对膨胀的讨论。

- changes_argument_state_cn：评价视角从'平均表现'转向'最难预测且成本最高的子群体'。

- sets_up_next_cn：为图6的非完美工人排序相关结果提供理由。

- failure_if_removed_cn：非完美工人子集分析显得是额外fishing。

- evidence_pointer：Section 5.3 Nonperfect Workers开头

### 9. Section 5.3 Nonperfect Workers P3

- order：9

- study_or_phase：非完美工人结果

- locator：Section 5.3 Nonperfect Workers P3

- paraphrase_cn：在至少收到一次非完美反馈的子集中，HMM-W2V显著优于所有替代系统。

- move_code：SUBGROUP_RESULT

- statement_status：empirical_result

- why_here_cn：证明优势在最困难群体上依然存在。

- inherits_from_previous_cn：承接子群体定义。

- changes_argument_state_cn：优势不再依赖完美工人占多数。

- sets_up_next_cn：为Open内排序评价切换决策情境。

- failure_if_removed_cn：整体优势可能只是'预测易的完美工人'。

- evidence_pointer：Section 5.3 Nonperfect Workers、Figure 6

### 10. Section 5.3 Within-Opening Rankings P1 S1-S3

- order：10

- study_or_phase：Open内排序结果

- locator：Section 5.3 Within-Opening Rankings P1 S1-S3

- paraphrase_cn：各系统以声誉在Open内排序申请者；对n=1到5计算Top-n被雇者平均表现。

- move_code：DECISION_CONTEXT_METRIC

- statement_status：method_decision

- why_here_cn：把评价从全局排序转到一个具体决策情境（雇主在一个职位内选择申请人），增加外部相关性。

- inherits_from_previous_cn：承接排序目标，转向'哪一个系统帮助雇主选得更好'。

- changes_argument_state_cn：评价进入个人决策层面。

- sets_up_next_cn：为图7的Top-n结果做操作定义。

- failure_if_removed_cn：全文只有全局排序，缺少决策情境证据。

- evidence_pointer：Section 5.3 Within-Opening Rankings开头

### 11. Section 5.3 Within-Opening Rankings P2

- order：11

- study_or_phase：Open内排序结果

- locator：Section 5.3 Within-Opening Rankings P2

- paraphrase_cn：HMM-W2V在Top-n上优于除WorkerRank和XGBoost外所有系统，对这两个最强基线也部分显著。

- move_code：DECISION_CONTEXT_RESULT_WITH_CAVEAT

- statement_status：empirical_result

- why_here_cn：如实报告对最强基线的部分显著性，避免过度声称。

- inherits_from_previous_cn：承接Top-n操作定义。

- changes_argument_state_cn：决策情境优势成立但允许最强基线竞争。

- sets_up_next_cn：为转入推荐系统适配做'再检验邻居方案'的铺垫。

- failure_if_removed_cn：Open内选择优势被夸大或失去证据。

- evidence_pointer：Section 5.3 Within-Opening Rankings、Figure 7

### 12. Section 5.4 P1 S1

- order：12

- study_or_phase：推荐系统适配

- locator：Section 5.4 P1 S1

- paraphrase_cn：第2.3节总结了概念差异，表2列出必要改动，5.4.1将实证检验适配的推荐系统并显示其显著不如HMM-W2V，5.4.2展示二者协作如何增强市场交易效果。

- move_code：RECOMMENDER_SECTION_ROADMAP

- statement_status：method_decision

- why_here_cn：用一段话给出整个5.4的行文路线，让读者知道先排除替代再展示互补。

- inherits_from_previous_cn：承接2.3.2映射假设和第5节评价框架。

- changes_argument_state_cn：把5.4定位为排除竞争者和展示协作的双任务。

- sets_up_next_cn：为5.4.1编码假设列表和5.4.2协作模型提供路标。

- failure_if_removed_cn：5.4的两个小节省略了位置逻辑。

- evidence_pointer：Section 5.4 P1

### 13. Section 5.4.1 P1 S1-S5

- order：13

- study_or_phase：推荐系统适配实现

- locator：Section 5.4.1 P1 S1-S5

- paraphrase_cn：按表2将技能集映射为物品、工人映射为用户、平均技能集反馈映射为评分，实现kNN/SVD/slope one和CNN序列推荐。

- move_code：RECOMMENDER_ADAPTATION

- statement_status：method_decision

- why_here_cn：把概念映射变成可实现系统，使'推荐系统不行'的结论有实证载体。

- inherits_from_previous_cn：直接执行2.3.2的映射建议。

- changes_argument_state_cn：推荐系统从理论候选变成可运行对手。

- sets_up_next_cn：为图8比较结果做铺垫。

- failure_if_removed_cn：排除推荐系统的论证只有理论没有数据。

- evidence_pointer：Section 5.4.1 P1

### 14. Section 5.4.1 P2 S1-S3

- order：14

- study_or_phase：推荐系统适配结果

- locator：Section 5.4.1 P2 S1-S3

- paraphrase_cn：网格搜索调参后，HMM-W2V显著（p<0.001）优于所有推荐系统适配，改进20%-60%；这些映射假设伤害性能，因此推荐系统不能充分解决三缺陷。

- move_code：RECOMMENDER_ADAPTATION_RESULT

- statement_status：empirical_result

- why_here_cn：用直接结果排除推荐系统适配方案，并回扣表2假设造成的性能损失。

- inherits_from_previous_cn：承接适配实现。

- changes_argument_state_cn：推荐系统被正式排除为替代方案。

- sets_up_next_cn：为下一句/下一节'声誉可以增强推荐'提供转折。

- failure_if_removed_cn：表2的'必须改动'警告没有实证验证。

- evidence_pointer：Section 5.4.1 P2、Figure 8

### 15. Section 5.4.2 P1 S1-S4

- order：15

- study_or_phase：声誉-推荐协作

- locator：Section 5.4.2 P1 S1-S4

- paraphrase_cn：声誉和推荐系统可以协同提高交易效率；用现有求职者推荐模型，在四种特征设置（当前声誉、HMM声誉、预测特征、预测特征+HMM声誉）下比较AUC。

- move_code：COLLABORATION_EXPERIMENT_OPENING

- statement_status：method_decision

- why_here_cn：在排除推荐系统后转向互补论点，用特征设置设计同时证明'比当前声誉好'和'在预测特征之上添增益'。

- inherits_from_previous_cn:null：承接5.4.1的失败结论，转为协作价值。

- changes_argument_state_cn：推荐系统从替代者变为受益者。

- sets_up_next_cn：为图9的AUC提升结果做铺垫。

- failure_if_removed_cn：论文只说推荐系统不行，缺失'准确声誉有下游价值'关键证据。

- evidence_pointer：Section 5.4.2 P1

### 16. Section 5.4.2 P2 S1-S2

- order：16

- study_or_phase：协作结果

- locator：Section 5.4.2 P2 S1-S2

- paraphrase_cn：相对当前声誉，HMM声誉带来2.4%-10% AUC提升；在预测特征上加入HMM声誉再提升1.3%-3.5%。

- move_code：COLLABORATION_RESULT

- statement_status：empirical_result

- why_here_cn：给出协作实验的关键数字，并区分两类增益来源。

- inherits_from_previous_cn：承接四种特征设置设计。

- changes_argument_state_cn：声誉准确性的下游价值被量化。

- sets_up_next_cn：为总结段'声誉与推荐协作'的论断提供证据。

- failure_if_removed_cn：管理价值声明失去数据。

- evidence_pointer：Section 5.4.2 P2、Figure 9

### 17. Section 5.4.2 P3 S1-S2

- order：17

- study_or_phase：协作总结

- locator：Section 5.4.2 P3 S1-S2

- paraphrase_cn：所提声誉框架优于推荐系统适配，进一步凸显三组件架构解决三缺陷的价值；图9还说明声誉与推荐系统并不对立，合作提供更好的用户体验。

- move_code：SECTION_CLOSURE

- statement_status：contribution_claim

- why_here_cn：收束5.4，同时把排除（替代失败）和互补（协作增益）两个发现固定下来。

- inherits_from_previous_cn：综合5.4.1与5.4.2两组结果。

- changes_argument_state_cn：5.4节结论完成：推荐系统不能替代但能受益。

- sets_up_next_cn：为5.5预测/解释性能和泛化测试切换话题。

- failure_if_removed_cn：5.4的论证没有收尾。

- evidence_pointer：Section 5.4.2 P3

### 18. Section 5.5 预测段 P1 S1-S2

- order：18

- study_or_phase：预测与解释性能

- locator：Section 5.5 预测段 P1 S1-S2

- paraphrase_cn：附录D显示HMM-W2V在MAE和RMSE上显著优于所有替代系统；表5显示在线性回归规格中R²更高。

- move_code：PREDICTIVE_AND_EXPLANATORY_RESULTS

- statement_status：empirical_result

- why_here_cn：补充排序之外的校准和解释性能，防止贡献被窄化为排名工具。

- inherits_from_previous_cn：承接主评价，扩展指标维度。

- changes_argument_state_cn：框架在预测误差和方差解释上同样占优。

- sets_up_next_cn：为泛化测试做准备。

- failure_if_removed_cn：校准优势缺失，很难说服评分系统用户。

- evidence_pointer：Section 5.5预测段、附录D、Table 5

### 19. Section 5.5 泛化段 P1 S1-S3

- order：19

- study_or_phase：泛化测试

- locator：Section 5.5 泛化段 P1 S1-S3

- paraphrase_cn：框架可泛化到其他经历归因、静态性和膨胀的情境；例举TripAdvisor/Yelp类平台，其评分正偏、动态且多维；附录E.3在77,044条餐馆评论上实现框架与替代方案。

- move_code：GENERALIZATION_CONTEXT_ARGUMENT

- statement_status：author_inference

- why_here_cn：先论证餐馆评论具备三缺陷特征，再宣布复制实验，让泛化测试在理论上指向正确情境。

- inherits_from_previous_cn：承接'框架可泛化'的声明。

- changes_argument_state_cn：第二情境被提前证明'应该适用'。

- sets_up_next_cn：为附录E.3结果句做铺垫。

- failure_if_removed_cn：餐馆复制显得是任意数据集演练。

- evidence_pointer：Section 5.5泛化段

### 20. Section 5.5 泛化段 P2 S1-S2

- order：20

- study_or_phase：泛化结果

- locator：Section 5.5 泛化段 P2 S1-S2

- paraphrase_cn：附录E.3显示HMM-W2V显著优于替代声誉系统（图14）和推荐系统适配（图15），因此实证证明框架泛化。

- move_code：GENERALIZATION_RESULT

- statement_status：empirical_result

- why_here_cn：报告第二情境中的两个主比较结果，完成外部效度验证。

- inherits_from_previous_cn：承接泛化情境论证。

- changes_argument_state_cn：框架泛化得到实证支持。

- sets_up_next_cn：为'与人工多维评分比较'的排他性检验铺垫。

- failure_if_removed_cn：设计知识级贡献缺少外部证据。

- evidence_pointer：Section 5.5泛化段、附录E.3、Figures 14-15

### 21. Section 5.5 泛化段 P3 S1-S2

- order：21

- study_or_phase：多维人工评分检验

- locator：Section 5.5 泛化段 P3 S1-S2

- paraphrase_cn：餐馆平台已有四维人工评分（食物、氛围、价值、服务）；附录E.3和图16比较后，HMM-W2V显著优于用这些人工维度做输入的替代方案，潜在维度含不同信息。

- move_code：HUMAN_DIMENSION_ALTERNATIVE_TEST

- statement_status：empirical_result

- why_here_cn：主动处理'平台已有多维人工评分'这一最可能削弱贡献的反驳。

- inherits_from_previous_cn：承接泛化结果，转向排他性。

- changes_argument_state_cn：框架不是冗余复制人工维度，而是提取了额外信息。

- sets_up_next_cn：为5.5总结段和讨论部分提供完整证据链。

- failure_if_removed_cn：'多维'贡献可被已有四维系统贬低。

- evidence_pointer：Section 5.5泛化段P3、附录E.3、Figure 16

### 22. Section 5.5 总结段 P1

- order：22

- study_or_phase：主评价总结

- locator：Section 5.5 总结段 P1

- paraphrase_cn：总体而言，实证分析显示HMM-W2V在一系列先进替代声誉和推荐系统上的优势：排序、非完美工人、Open内排序和近正态分布。

- move_code：RESULTS_SECTION_CLOSURE

- statement_status：contribution_claim

- why_here_cn：在进入讨论前把四类评价结果汇总，为第6节的重述预热。

- inherits_from_previous_cn：综合5.3、5.4、5.5全部结果。

- changes_argument_state_cn：评价章节正式闭合，所有贡献声明都有前置证据。

- sets_up_next_cn：为讨论部分'缺陷-组件-结果'重述提供浓缩清单。

- failure_if_removed_cn：讨论部分失去明确结果基础。

- evidence_pointer：Section 5.5总结段

## 讨论与贡献逐句图谱

### 1. Discussion P1 S1-S3

- order：1

- locator：Discussion P1 S1-S3

- paraphrase_cn：重述三缺陷（归因、静态性、膨胀）并重述HMM-W2V框架三个组件如何逐一解决。

- move_code：DEFECT_COMPONENT_RESTATEMENT

- statement_status：contribution_claim

- why_here_cn：讨论第一段把整个论证重新拼装，让读者看到问题-方案-证据的闭合。

- inherits_from_previous_cn：承接第5节全部实证结果和引言中的问题。

- changes_argument_state_cn：实证结果被重新表述为'设计成功'。

- sets_up_next_cn：为第二句/第二段四类表现总结提供框架。

- failure_if_removed_cn：讨论与引言和评价脱节。

- evidence_pointer：Discussion P1

### 2. Discussion P1 S4

- order：2

- locator：Discussion P1 S4

- paraphrase_cn：两个数据集上的应用显示HMM-W2V在排序、识别非完美工人、Open内排序和近正态分布四方面优于替代系统。

- move_code：RESULT_SUMMARY

- statement_status：empirical_result

- why_here_cn：在重述框架后立即给出四类结果清单，形成'设计-证据'对照。

- inherits_from_previous_cn：承接前三句的三组件描述，用结果验证它们。

- changes_argument_state_cn：讨论进入结论状态。

- sets_up_next_cn：为6.1研究贡献提供数据前提。

- failure_if_removed_cn：讨论开篇没有结果支持。

- evidence_pointer：Discussion P1末句

### 3. Section 6.1 P1 S1-S2

- order：3

- locator：Section 6.1 P1 S1-S2

- paraphrase_cn：鉴于在线工人数量和动态性增长，准确质量评估是线上工作最终覆盖范围的决定因素；本文首次概述声誉系统缺陷（静态性和归因）并解释为何此类系统在此情境表现不佳。

- move_code：RESEARCH_CONTRIBUTION_CLAIM

- statement_status：contribution_claim

- why_here_cn：把'准确评估'上升到'未来工作覆盖范围的决定因素'，再配'首次'声明。

- inherits_from_previous_cn：承接引言中对未来工作趋势的论述。

- changes_argument_state_cn：贡献从技术改进升级为概念化和问题化。

- sets_up_next_cn：为下一句'方案推广到任意技能集'做铺垫。

- failure_if_removed_cn：研究贡献缺失，论文只是算法报告。

- evidence_pointer：Section 6.1 P1

### 4. Section 6.1 P1 S3-S4

- order：4

- locator：Section 6.1 P1 S3-S4

- paraphrase_cn：指出不足后，提供可泛化到任意技能集的方案；由于能动态演化的技能集特定估计，本研究提供准确技能集特定声誉。

- move_code：GENERALIZABLE_SOLUTION_CLAIM

- statement_status：contribution_claim

- why_here_cn：把'首次指出缺陷'与'提供方案'结合起来，形成完整研究贡献。

- inherits_from_previous_cn：承接'首次概述'。

- changes_argument_state_cn：贡献从'指出问题'扩展到'解决问题'。

- sets_up_next_cn：为6.1第二段设计贡献做铺垫。

- failure_if_removed_cn：研究贡献不完整。

- evidence_pointer：Section 6.1 P1

### 5. Section 6.1 P2 S1-S3

- order：5

- locator：Section 6.1 P2 S1-S3

- paraphrase_cn：从设计角度看，本文通过结合人类输入与机器智能扩展了表1文献；相对以前系统，所提方法具有适合在线工作的独特动态属性；在人机协作增长背景下，该混合方法可作为未来增强智能系统的基线。

- move_code：DESIGN_AND_IA_BASELINE_CLAIM

- statement_status：contribution_claim

- why_here_cn：把贡献放到'增强智能'特刊叙事中，并将本文定位为基线。

- inherits_from_previous_cn：承接6.1总体贡献，转向设计层面。

- changes_argument_state_cn：贡献从单篇方案升格为领域基线。

- sets_up_next_cn：为6.2方法论贡献提供过渡。

- failure_if_removed_cn：与特刊主题的联系减弱。

- evidence_pointer：Section 6.1 P2

### 6. Section 6.2 P1 S1-S2

- order：6

- locator：Section 6.2 P1 S1-S2

- paraphrase_cn：方法上，本文对有意开发动态声誉系统的市场提供详细指南，涵盖概念化、建模和估计；具体指南包括技能集分解、HMM架构、参数估计、设计选择与评价。

- move_code：METHODOLOGICAL_CONTRIBUTION_OPENING

- statement_status：contribution_claim

- why_here_cn：把第3节的技术细节抽象成一串可复用的方法论指南。

- inherits_from_previous_cn：承接研究/设计贡献，进入方法层面。

- changes_argument_state_cn：技术细节升级为指南性知识。

- sets_up_next_cn：为后面四个指南条目和泛化平台列表做框架。

- failure_if_removed_cn：方法论贡献声明没有结构。

- evidence_pointer：Section 6.2 P1

### 7. Section 6.2 泛化平台段 S1-S5

- order：7

- locator：Section 6.2 泛化平台段 S1-S5

- paraphrase_cn：框架可调整到任何经历三缺陷的在线平台：Yelp/TripAdvisor可开发更动态的声誉；Uber/Lyft可内部估计司机动态服务质量并识别不同行程类型异质性；LinkedIn可估计用户多技能集演化专长并供推荐系统使用。

- move_code：BOUNDARY_AND_TRANSFER_EXAMPLES

- statement_status：contribution_claim

- why_here_cn：给出具体平台示例，把抽象设计知识翻译成可想象的应用场景。

- inherits_from_previous_cn：承接'方法论贡献可泛化'。

- changes_argument_state_cn：贡献从单一市场扩展到平台类型族。

- sets_up_next_cn：为6.3平台/工人/雇主含义提供应用图景。

- failure_if_removed_cn：泛化主张缺少可以想象的落点。

- evidence_pointer：Section 6.2泛化平台段

### 8. Section 6.3 P1 S1-S3

- order：8

- locator：Section 6.3 P1 S1-S3

- paraphrase_cn：在线劳动平台通过准确声誉受益：帮助工人区分、帮雇主快速知情决策、使市场改进推荐算法并理解供应分布；高质量工人更可能继续参与，低质量工人被激励投资新技能。

- move_code：PLATFORM_IMPLICATIONS

- statement_status：author_inference

- why_here_cn：把技术结果转化为平台收益路径，属于IS论文常见'对平台意味着什么'。

- inherits_from_previous_cn：承接引言中已提过的三类价值，但在数据支持后重申。

- changes_argument_state_cn：贡献从方法进入市场效率叙事。

- sets_up_next_cn：为下一段'非完美工人预警'的特定管理价值做铺垫。

- failure_if_removed_cn：平台实践含义缺失。

- evidence_pointer：Section 6.3 P1

### 9. Section 6.3 P2 S1-S3

- order：9

- locator：Section 6.3 P2 S1-S3

- paraphrase_cn：识别非完美工人的性能对市场管理者尤为重要：准确预测表现不佳可预先告知雇主、减少负面结果、提高雇主满意和持续参与，从而产生持续收入。

- move_code：NONPERFECT_PREDICTION_IMPLICATION

- statement_status：author_inference

- why_here_cn：把非完美工人实验结果变成干预建议，回应摘要中'减少负面影响'的承诺。

- inherits_from_previous_cn：承接6.3平台收益讨论，聚焦最相关子结果。

- changes_argument_state_cn：子群体结果获得管理行为含义。

- sets_up_next_cn：为下一段'理解供应分布与介入'做铺垫。

- failure_if_removed_cn：非完美工人结果只剩统计意义，缺实践意义。

- evidence_pointer：Section 6.3 P2

### 10. Section 6.3 P3 S1-S2

- order：10

- locator：Section 6.3 P3 S1-S2

- paraphrase_cn：通过框架平台可理解潜在能力和任意技能组合的供应分布，管理者可在合适处介入；附录H分析能力维并说明如何跟踪表现和需求以设计干预。

- move_code：SUPPLY_DISTRIBUTION_INSIGHT

- statement_status：author_inference

- why_here_cn：把W2V潜在维度的输出翻译为平台侧供需管理工具。

- inherits_from_previous_cn：承接'理解供应分布'一句，展开为干预建议。

- changes_argument_state_cn：潜在能力维从技术结构变成管理面板。

- sets_up_next_cn：为下一段人机增强的长期循环和边际化风险做铺垫。

- failure_if_removed_cn：能力维价值缺少管理应用。

- evidence_pointer：Section 6.3 P3

### 11. Section 6.3 P4 S1-S5

- order：11

- locator：Section 6.3 P4 S1-S5

- paraphrase_cn：框架把人类反馈与机器学习结合增强决策；随着持续训练AI性能改善，对工人和雇主的影响增强；高相关专长工人顺利找到任务，被低评工人可能被边缘化，职业系统可推荐新技能；更好IA甚至可能让新工人进入系统认为有历史工人不合适的任务。

- move_code：IA_LONG_TERM_AND_RISK_DISCUSSION

- statement_status：author_inference

- why_here_cn：在平台收益之后讨论IA系统的长期反馈循环、分配效应和边际化风险，体现特刊对智能增强社会后果的关切。

- inherits_from_previous_cn：承接6.3前三段的平台应用，扩大到劳动力群体后果。

- changes_argument_state_cn：贡献从效率延伸到再分配与社会风险。

- sets_up_next_cn：为下一段把IA推广到线下工作做铺垫。

- failure_if_removed_cn：特刊的'未来工作'维度未完成。

- evidence_pointer：Section 6.3 P4

### 12. Section 6.3 P5 S1-S2

- order：12

- locator：Section 6.3 P5 S1-S2

- paraphrase_cn：这些影响可扩展到线下工作：框架可通过LinkedIn概括到线下工人声誉；自动化将改变许多工作，1.2亿工人未来三年需再培训；此类声誉框架能促进供应再分配和智能区分。

- move_code：OFFLINE_WORK_GENERALIZATION

- statement_status：author_inference

- why_here_cn：把研究从在线市场推向线下未来工作，完成特刊要求的宏大叙事。

- inherits_from_previous_cn：承接上一段边缘化与再技能化的讨论，扩展到全社会再培训。

- changes_argument_state_cn：贡献边界从在线平台扩展到一般劳动力市场。

- sets_up_next_cn：为6.4建模讨论（离散状态、降级、W2V/D2V）留出转折空间。

- failure_if_removed_cn：未来工作意义停在在线平台，特刊主题不完整。

- evidence_pointer：Section 6.3 P5

### 13. Section 6.4 离散状态段 S1-S4

- order：13

- locator：Section 6.4 离散状态段 S1-S4

- paraphrase_cn：框架假设隐藏状态离散但输出连续分数；连续状态空间模型不保证更好，且可能因缺少离散状态而使管理者分析需要调阈值。

- move_code：MODEL_LIMITATION_AND_JUSTIFICATION

- statement_status：author_inference

- why_here_cn：主动承认离散假设的局限，并用连续输出和解释性理由辩护，展示建模反思。

- inherits_from_previous_cn：承接前文框架，进入建模边界讨论。

- changes_argument_state_cn：把HMM离散假设从潜在弱点变成有意识的权衡。

- sets_up_next_cn：为下一段降级转移的辩护提供同类型反思。

- failure_if_removed_cn：审稿人会质疑为什么不用连续状态空间模型。

- evidence_pointer：Section 6.4离散状态段

### 14. Section 6.4 降级转移段 S1-S5

- order：14

- locator：Section 6.4 降级转移段 S1-S5

- paraphrase_cn：多项logit允许降级到更低质量状态看似不合理，但HMM机制需要它：早期高分后期低分的工人，模型应随新证据调整到低质量状态；允许降级对框架修正估计至关重要，附录I和图18实证展示无约束转移的收益。

- move_code：REVERSE_TRANSITION_RATIONALE

- statement_status：author_inference

- why_here_cn：用具体情景解释一个反直觉设计选择，并以附录实证支撑。

- inherits_from_previous_cn：承接5.1中'多项logit转移'的配置选择。

- changes_argument_state_cn：降级看似不合理但被辩护为纠错机制。

- sets_up_next_cn：为下一段人类多维评分可行性反驳做铺垫。

- failure_if_removed_cn：后文WorkerRank等质疑和模型可信度受损。

- evidence_pointer：Section 6.4降级转移段

### 15. Section 6.4 人类维度不可能段 S1-S5

- order：15

- locator：Section 6.4 人类维度不可能段 S1-S5

- paraphrase_cn：作者认为平台已在开发多维系统可能只是恢复人工维度噪声：但技能-能力映射的复杂度、非主要维度的多技能映射，人类难以执行；框架通过W2V自动估计技能间相关完成映射，附录E.3显示比人工维度含不同信息。

- move_code：HUMAN_RATING_INFEASIBILITY_ARGUMENT

- statement_status：author_inference

- why_here_cn：深入反驳'平台现有四维评分已经足够'的替代解释，用认知负荷论证和实证共同支撑。

- inherits_from_previous_cn：承接5.5中与人工四维评分比较的结果，转成设计合理性论证。

- changes_argument_state_cn：多维人工系统被判定为认知上不可扩展。

- sets_up_next_cn：为下一段W2V vs D2V边界条件做铺垫。

- failure_if_removed_cn：多维人工系统可能完全替代本文贡献。

- evidence_pointer：Section 6.4人类维度不可能段

### 16. Section 6.4 W2V vs D2V边界段 S1-S4

- order：16

- locator：Section 6.4 W2V vs D2V边界段 S1-S4

- paraphrase_cn：在工人情境W2V更好而餐馆情境D2V更好提出了何时选何者的边界：对预定义、结构良好且每个词项都有关键信息的词池W2V更优；对非结构化文本（如评论）D2V更优。

- move_code：BOUNDARY_CONDITION_ARTICULATION

- statement_status：author_inference

- why_here_cn：把跨情境结果差异转成可复用边界条件，防止读者误以为W2V永远更好。

- inherits_from_previous_cn：承接两个数据集中的组件选择结果。

- changes_argument_state_cn：组件选择从'最佳配置'变成'情境规则'。

- sets_up_next_cn：为结论段落提供最后一个设计知识。

- failure_if_removed_cn：泛化主张缺少适用条件，会被识别为无边界声明。

- evidence_pointer：Section 6.4 W2V vs D2V边界段

### 17. Section 6.5 Conclusion P1 S1-S3

- order：17

- locator：Section 6.5 Conclusion P1 S1-S3

- paraphrase_cn：总结：本文提出解决归因、静态性和膨胀的增强智能框架；两个不同情境的应用显示它能跨维度追踪演化实体并提供准确质量估计；部署在不同在线平台可能对工人、雇主、企业和未来工作产生重要影响。

- move_code：CONCLUSION_RESTATEMENT

- statement_status：contribution_claim

- why_here_cn：以标准结论三段式收束：方案、证据、影响。

- inherits_from_previous_cn：依赖全部前文框架与结果。

- changes_argument_state_cn：全文论证闭合。

- sets_up_next_cn：无，结束。

- failure_if_removed_cn：论文没有收尾。

- evidence_pointer：Section 6.5

## Study累积逻辑

### 1. 1

- study_or_phase：模型无关证据（4.1）

- evidence_job_cn：证明三类缺陷在真实数据中存在，且不依赖任何模型。

- what_it_establishes_cn：声誉分布均值0.86（膨胀）；不同技能评分不同且连续任务技能集相似度0.33（归因）；47%工人12个月学新技能、66%新技能后初始低分但随后回升（静态性）。

- what_it_cannot_establish_cn：不能证明新框架能够克服这些缺陷，也不能说明该用哪种建模。

- why_next_phase_is_needed_cn：现象存在只是设计需要，下一步需要确定可计算的框架配置。

- transition_wording_function_cn：第5节开篇的'下面描述建模选择和调参'把现象证据转换为设计选择任务。

### 2. 2

- study_or_phase：组件选择与网格搜索（5.1）

- evidence_job_cn：在候选建模选项中为每个组件选出最适合的实现，防止最终制品被指认为任意技术偏好。

- what_it_establishes_cn：W2V优于D2V/GMM；HMM优于线性/SVM/LSTM/XGBoost；公式(8)聚合最优；D=10；K向量、Beta发射、多项logit转移。

- what_it_cannot_establish_cn：该配置只在设计目标内最优，尚未证明比外部声誉系统更强。

- why_next_phase_is_needed_cn：企业愿意问的是'与现行声誉和先进ML比，整体谁好'。

- transition_wording_function_cn：'基于这些设计选择和超参，框架在任意技能集上估计声誉'把调参结果引入基准比较环节。

### 3. 3

- study_or_phase：主基准评价（5.3）

- evidence_job_cn：在同一评估协议下，用多指标证明HMM-W2V优于当前声誉和多个先进ML/链接分析基准。

- what_it_establishes_cn：排序相关高20%-85%；Top表现高8%、lift高9%；分布近正态高37%；非完美工人子集显著更优；Open内Top-n大多显著更好。

- what_it_cannot_establish_cn：不能排除推荐系统适配同样可达此效果，也不能证明下游交易真正受益。

- why_next_phase_is_needed_cn：需要排除另一候选方案族（推荐系统）并展示声誉的协作价值。

- transition_wording_function_cn：第5.4节开头'表2识别必要修改…5.4.1实证检验适配'把主基准结果转入推荐系统环节。

### 4. 4

- study_or_phase：推荐系统适配基准（5.4.1）

- evidence_job_cn：把推荐系统按映射/编码假设适配为声誉框架，证明其显著弱于HMM-W2V。

- what_it_establishes_cn：kNN/SVD/slope one/CNN序列推荐适配后，HMM-W2V显著胜出20%-60%。

- what_it_cannot_establish_cn：不能证明声誉模块在推荐系统中的启用能带来业务改善。

- why_next_phase_is_needed_cn：需要在下游推荐任务中展示准确声誉的实际增益。

- transition_wording_function_cn：'最后5.4.2显示声誉与推荐系统如何协作'把排除实验转向互补实验。

### 5. 5

- study_or_phase：声誉-推荐协作（5.4.2）

- evidence_job_cn：证明HMM-W2V声誉作为求职者推荐模型特征时，AUC明显提升，展示下游交易效率价值。

- what_it_establishes_cn：HMM声誉替代当前声誉带来2.4%-10% AUC提升；在预测特征上叠加HMM声誉再提升1.3%-3.5%。

- what_it_cannot_establish_cn：AUC增益未直接映射为平台收入或雇主真实决策质量。

- why_next_phase_is_needed_cn：还需要证明优势不只在排序层面，也在预测误差/解释力层面和外部情境。

- transition_wording_function_cn：第5.5节'除了此分析，还评价预测解释性能和泛化性'把协作结果引向补充评价。

### 6. 6

- study_or_phase：预测与解释性能（5.5上半）

- evidence_job_cn：补充排序之外的校准（MAE/RMSE）与解释力（R²）证据。

- what_it_establishes_cn：HMM-W2V显著降低MAE/RMSE，并在线性规格中解释更多观察绩效方差。

- what_it_cannot_establish_cn：未检验这些误差优势在其他情境中的稳定性。

- why_next_phase_is_needed_cn：需要用第二情境复制来证明设计知识而非数据集特例。

- transition_wording_function_cn：'泛化性：该框架可推广到其他经历三缺陷的情境'把预测性能引向外部效度。

### 7. 7

- study_or_phase：餐馆评论泛化（5.5下半）

- evidence_job_cn：在另一个评分膨胀、质量多维且动态的平台复制主要比较，并证明与人工多维评分不同。

- what_it_establishes_cn：77,044条评论上显著优于替代声誉与推荐系统适配；潜在维度含与人工四维不同的信息。

- what_it_cannot_establish_cn：单一外部数据集不足以证明所有此类平台都适用；餐厅评分的四维差异未近似。

- why_next_phase_is_needed_cn：结果需要回到设计原则和边界条件的表述，形成可复用设计知识。

- transition_wording_function_cn：第6节'当前声誉系统经历三个不足…本文提出框架'把跨情境结果重述为设计知识和边界条件。

## 主张—证据台账

### 1. 现有在线劳动市场声誉系统存在归因、静态性和膨胀三类缺陷。

- claim_cn：现有在线劳动市场声誉系统存在归因、静态性和膨胀三类缺陷。

- claim_level：theory

- supporting_evidence_cn：文献综述+模型无关数据：图2(a)分布均值0.86、图2(b)分技能差异、图2(c)连续任务相似度0.33、图2(d)-(f)新技能轨迹。

- support_strength：direct

- where_claim_is_made：引言P3、Section 2.2.1

- where_evidence_is_provided：Section 4.1、Figure 2(a)-(f)

### 2. 任何现有声誉系统（人类/机器/混合/技能测试/WorkerRank）都不能同时解决三缺陷。

- claim_cn：任何现有声誉系统（人类/机器/混合/技能测试/WorkerRank）都不能同时解决三缺陷。

- claim_level：design_knowledge

- supporting_evidence_cn：逐类排除的文献论证和Table 1的缺口矩阵。

- support_strength：partial

- where_claim_is_made：Section 2.2.2

- where_evidence_is_provided：Section 2.2.2、Table 1

### 3. 三条设计原则（技能分解、动态能力特定评估、按需聚合）能分别解决三缺陷。

- claim_cn：三条设计原则（技能分解、动态能力特定评估、按需聚合）能分别解决三缺陷。

- claim_level：theory

- supporting_evidence_cn：概念论证和Schmidt-Hunter正态分布引用，以及后文实验结果。

- support_strength：asserted

- where_claim_is_made：引言P4、Section 2.2.3

- where_evidence_is_provided：Section 2.2.3原则段；后文5.3结果为间接支持

### 4. HMM-W2V框架在排序相关、排序表现和lift上显著优于当前声誉和5个ML/链接替代。

- claim_cn：HMM-W2V框架在排序相关、排序表现和lift上显著优于当前声誉和5个ML/链接替代。

- claim_level：technical

- supporting_evidence_cn：10折工人级交叉验证结果：85%对当前，20%-60%对替代；Top表现8%、lift 9%，均p<0.001。

- support_strength：direct

- where_claim_is_made：引言P5、摘要P2

- where_evidence_is_provided：Section 5.3、Figures 3-4

### 5. HMM-W2V声誉分布更接近正态，缓解膨胀并促进区分。

- claim_cn：HMM-W2V声誉分布更接近正态，缓解膨胀并促进区分。

- claim_level：mechanism

- supporting_evidence_cn：与正态分布的总变差距离接近37%（p<0.001）。

- support_strength：partial

- where_claim_is_made：引言P4、Section 5.3

- where_evidence_is_provided：Section 5.3 Reputation Distribution、Figure 5

### 6. 框架在非完美工人识别上显著优于所有替代。

- claim_cn：框架在非完美工人识别上显著优于所有替代。

- claim_level：mechanism

- supporting_evidence_cn：至少一次非完美反馈子集的Spearman/Kendall，p<0.001。

- support_strength：direct

- where_claim_is_made：摘要P2、引言P5

- where_evidence_is_provided：Section 5.3 Nonperfect Workers、Figure 6

### 7. 框架改善Open内申请者排序，带来显著更好结果。

- claim_cn：框架改善Open内申请者排序，带来显著更好结果。

- claim_level：technical

- supporting_evidence_cn：Top-n平均被雇者表现大多p<0.05；对WorkerRank只在n=4,5为p<0.05，对XGBoost n=1为p<0.1。

- support_strength：partial

- where_claim_is_made：摘要P2、引言P5

- where_evidence_is_provided：Section 5.3 Within-Opening Rankings、Figure 7

### 8. 推荐系统适配不足以提供工人声誉。

- claim_cn：推荐系统适配不足以提供工人声誉。

- claim_level：artifact

- supporting_evidence_cn：kNN/SVD/slope one/CNN序列推荐适配后，HMM-W2V显著胜出20%-60%（p<0.001）。

- support_strength：direct

- where_claim_is_made：Section 2.3.2、表2

- where_evidence_is_provided：Section 5.4.1、Figure 8

### 9. HMM声誉能增强求职者推荐系统的AUC，具有下游交易价值。

- claim_cn：HMM声誉能增强求职者推荐系统的AUC，具有下游交易价值。

- claim_level：mechanism

- supporting_evidence_cn：AUC提升2.4%-10%相对当前声誉，1.3%-3.5%相对预测特征。

- support_strength：direct

- where_claim_is_made：Section 5.4.2、讨论6.3

- where_evidence_is_provided：Section 5.4.2、Figure 9

### 10. 框架可泛化到其他评分过度正向、质量多维且动态的平台。

- claim_cn：框架可泛化到其他评分过度正向、质量多维且动态的平台。

- claim_level：design_knowledge

- supporting_evidence_cn：77,044餐馆评论上显著优于替代声誉系统（图14）和推荐系统适配（图15），并优于人工四维输入（图16）。

- support_strength：partial

- where_claim_is_made：摘要P2、引言P5、Section 6.2

- where_evidence_is_provided：Section 5.5泛化段、附录E.3、Figures 14-16

### 11. 本文首次指出静态性和归因缺陷，并提供可复用设计原则。

- claim_cn：本文首次指出静态性和归因缺陷，并提供可复用设计原则。

- claim_level：theory

- supporting_evidence_cn：文献回顾和表1缺口比较；无直接对照证据可核查首次性。

- support_strength：asserted

- where_claim_is_made：引言P6、Section 6.1

- where_evidence_is_provided：Section 2.2.3、Table 1

### 12. AUC提升会转化为平台收入和更满意雇主。

- claim_cn：AUC提升会转化为平台收入和更满意雇主。

- claim_level：boundary

- supporting_evidence_cn：引用Kokkodis et al. 2015和Tripp/Grégoire的因果链，但无本研究现场测量。

- support_strength：asserted

- where_claim_is_made：Section 5.4.2结束段、Section 6.3

- where_evidence_is_provided：无直接新证据

### 13. 离散假设可通过连续输出和降级转移辩护，连续状态模型不保证更好。

- claim_cn：离散假设可通过连续输出和降级转移辩护，连续状态模型不保证更好。

- claim_level：boundary

- supporting_evidence_cn：连续输出论证和附录I/图18的降级转移实证。

- support_strength：partial

- where_claim_is_made：Section 6.4

- where_evidence_is_provided：Section 6.4、附录I、Figure 18

### 14. W2V在结构化技能词项情境更好，D2V在非结构化文本情境更好。

- claim_cn：W2V在结构化技能词项情境更好，D2V在非结构化文本情境更好。

- claim_level：boundary

- supporting_evidence_cn：劳动市场W2V优（附录C.1）和餐馆D2V优（附录E.3）的对比。

- support_strength：partial

- where_claim_is_made：Section 6.4 W2V vs D2V段

- where_evidence_is_provided：附录C.1、附录E.3

## ISR定位逻辑

- constitutive_is_problem_cn：作者没有把问题写成纯机器学习调参问题，而是写成信息不对称制度的失效：声誉系统是平台用来建立中间信任、减少信息不对称的标准机制，其设计缺陷（一维平均、静态、过度正向）导致雇主决策噪声、工人被错误区分、市场交易失败。三缺陷都是数字平台与人类行为互动的产物：评分来自雇主行为偏差（同伴压力、淘汰机制），技能演化来自劳动力市场供需变化，工人质量动态来自持续再学习。因此这是一个IS层面的制度设计问题，算法只是实现制度原则的载体。

- technology_behavior_or_market_entanglement_cn：技术设计处处与行为和市场纠缠：W2V技能分解利用的是技能与技能之间的共现/文本关系，反映劳动力市场技能组合结构；HMM的转移变量是工人累计声誉、收入、雇佣率等市场信号，发射变量包括小时费率；聚合公式使用技能权重软最大，使分数反映具体求职场景的需求。推荐系统适配实验的失败也被归因于'物品单一评分、工人技能集异质'等市场结构特征，而非单纯算法缺点。下游AUC实验进一步把声誉评分嵌入推荐决策流，显示技术制品与交易效率直接关联。

- role_of_benchmark_or_objective_evidence_cn：离线benchmark承担多个IS论证任务：（1）与当前市场声誉系统比较，证明制度性缺陷可以被设计修复；（2）与先进ML模型比较，排除'只是用更复杂模型'的解释；（3）与推荐系统适配比较，排除相邻技术族作为替代方案；（4）子群体（非完美工人）比较，说明膨胀条件下整体准确率会掩盖系统性的区分失败；（5）AUC协作实验把排序优势转化为下游决策质量证据。因此客观证据不只是'分数更高'，而是为'设计原则指导的系统在制度和交易层面更优'提供支持。

- theory_in_design_cn：理论以三条设计原则的形式进入设计，而不是事后解释：静态性和归因来自在线劳动市场声誉文献中的现象总结；正态分布（Schmidt and Hunter 1983）直接规定聚合步骤的目标，使接近正态成为设计要求和评价指标；HMM的'转移'和'发射'变量来自对工人经验积累和可观测特征的机制假设。但理论-设计耦合是部分的：W2V和HMM的具体算法选择主要通过网格搜索与其他ML模型比较决定，而非来自行为理论；餐馆情境中D2V反超W2V也说明组件选择是数据驱动的。

- technical_vs_is_contribution_balance_cn：文章在技术贡献（组件、公式、调参、基准）和IS贡献（三缺陷概念化、设计原则、平台含义）之间维持明确的篇幅分层。第2节用大量篇幅建立制度框架和缺陷分类，第3节用第三节连接原则与组件；评价部分（第5节）虽然技术密集，但每个结果都回扣到'区分工人、帮助雇主、改善交易'的IS目标；讨论部分再次把技术细节提炼为设计知识和平台影响。缺点是技术细节（HMM似然、转移/发射函数）对普通IS读者是障碍，文章依赖附录处理大部分推导，正文保留了可读的结果叙事。

- beyond_transient_performance_cn：文章的贡献不只是一时分数优势，因为：（1）它把'准确声誉'定义为制度目标（减少信息不对称、区分工人、支持交易），数据结果服务于这个目标；（2）多指标评价（排序、分布、非完美、Open内、AUC）覆盖系统在不同决策点的表现，而不是单一精度；（3）推荐系统适配和人工四维评分检验排除了替代解释，证明优势来自设计逻辑而非偶然；（4）第二情境复制把结果转化为可复用设计知识与边界条件（W2V vs D2V），使贡献可移植。但AUC到平台收益的跳跃仍是未验证推断，正态分布作为最优目标也带有假设性。

## 段落级仿写模板

### abstract_steps

1. 第1步：用一句制度功能陈述开场，说明所研究系统的价值（声誉系统提高交易效率）。

2. 第2步：立即指出该系统设计未能捕捉关键维度，并用三个命名缺陷具体化（归因、静态性、膨胀）。

3. 第3步：给出方案总称（增强智能框架），并说明方案特征正是缺陷的反面。

4. 第4步：把框架拆成三组件，逐条标注组件-缺陷映射。

5. 第5步：报告主数据集上的多点结果，按缺陷/评价目标分条。

6. 第6步：报告第二情境的泛化证据，把单点结果升级为框架级贡献。

### introduction_paragraph_steps

1. 第1段：建立市场背景→突出规模与未来增长→引出研究对象平台。

2. 第2段：从平台成功收束到信任→定义声誉系统→展开其因果机制（评分→简历→信任→交易→定价）。

3. 第3段：一句总转折'尽管有益但设计不足'→按静态性、归因、膨胀顺序展开三个具体缺陷，每段附机制和后果。

4. 第4段：提出研究问题→给出三原则方案→逐条原则-缺陷映射→引入理论锚点（如正态分布）。

5. 第5段：报告主结果（多基准、多点）→报告泛化结果。

6. 第6段：声明'首次'研究贡献→把结果翻译为工人/雇主/市场三方价值。

7. 第7段：把工作接入更大议题（增强智能/未来工作），给社会意义。

### theory_to_design_steps

1. 综述相关系统并分类（人类/机器/混合）。

2. 聚焦目标情境，给每个具体缺陷命名并附机制解释。

3. 把所有现有系统逐类排除，用表格制成缺陷-系统缺口矩阵。

4. 把三个缺陷转译为三条设计原则。

5. 主动提出相邻技术族（推荐系统）并分析其适配映射的缺陷，用第二张表预告实证排除。

6. 第3节把原则落实为组件：用'直接做法有三个缺点'为每个组件制造必要性。

### method_and_study_sequence_steps

1. 先描述数据来源、规模和字段。

2. 在建模前用模型无关图证证明缺陷现象存在（每类缺陷一个图）。

3. 定义HMM变量并注明情境特异性。

4. 固定评估协议（如按个体分10折）。

5. 通过网格搜索确定组件配置，并报告每个组件的最佳选择。

6. 定义基准列表（当前系统+多个先进ML+领域特化方法）。

7. 每个评价目标先说明'为什么用这个指标'，再报告结果和显著性。

### results_reporting_steps

1. 主结果：排序相关+排序表现+lift，给出改进百分比和置信区间。

2. 分布结果：用理论参照（正态）的统计距离度量设计目标是否达成。

3. 子群体结果：识别容易被整体指标掩盖的困难子群体，单独报告。

4. 决策情境结果：在具体决策（如Open内Top-n）中比较基准。

5. 排除替代：将竞争技术族按映射假设实现，并报告其失败。

6. 互补/下游：在同一任务中把新制品作为特征，报告增量增益。

7. 泛化：在第二个满足相同制度条件的情境中复制主比较，并做排他性检验（如vs人工维度）。

### discussion_and_contribution_steps

1. 重述'缺陷-组件-结果'映射，把结果重新拼装成闭合论证。

2. 声明研究贡献：首次概念化缺陷，提供可推广方案。

3. 声明设计贡献：把技术细节提炼为可复用指南（分解、HMM结构、参数估计、评价流程）。

4. 给出边界条件与平台示例（Yelp/Uber/LinkedIn）。

5. 把结果翻译为平台、工人、雇主的管理价值，处理非完美预测等特定结果。

6. 讨论建模假设的局限并逐条辩护（离散状态、降级转移、W2V/D2V）。

7. 结论段：方案+两情境证据+对四类主体和未来工作的影响。

## 可执行写作算法

### 1. 1

- step：1

- rhetorical_job_cn：建立研究对象的重要性，并把话题从市场成长收束到声誉机制。

- research_evidence_required_cn：平台或市场存在性、规模增长趋势、声誉系统在交易中的作用链。

- sentence_pattern_function_cn：先用事实句给出背景，再用'决定因素之一是…'式句子把焦点移到制度机制，然后定义研究对象。

- transition_condition_cn：当读者已接受'声誉系统重要'时进入下一步。

### 2. 2

- step：2

- rhetorical_job_cn：命名并解释现有系统的具体缺陷，使问题可检验。

- research_evidence_required_cn：对系统机制的定义性分析（如统一平均=静态），以及缺陷的微观机制（淘汰和同伴压力=膨胀）。

- sentence_pattern_function_cn：用'尽管有好处，但设计…'转折，随后每个缺陷一个子段，先机制后后果。

- transition_condition_cn：当读者知道'哪些具体设计特征导致哪些失败'时进入下一步。

### 3. 3

- step：3

- rhetorical_job_cn：逐类排除现有候选方案，用表格使缺口可见。

- research_evidence_required_cn：对每个候选方案逐一检查其是否解决每个缺陷；能放进'系统×缺陷'矩阵。

- sentence_pattern_function_cn：先按分类列出候选，再一句'不解决……因为目标/情境不匹配'，最后用表总结。

- transition_condition_cn：当缺口矩阵显示'没有系统同时满足三列'时进入下一步。

### 4. 4

- step：4

- rhetorical_job_cn：把每个缺陷翻译成一条设计原则，作为后续制品的蓝图。

- research_evidence_required_cn：缺陷与设计特征的对应关系；一个可引用的理论锚点（如正态分布）支持目标设定。

- sentence_pattern_function_cn：用编号列表给出原则，每条用'解决X'句式回指缺陷，再用一句综合说明原则组合的效果。

- transition_condition_cn：当原则列表与缺陷一一对应并被读者理解时进入下一步。

### 5. 5

- step：5

- rhetorical_job_cn：把设计原则落地为组件，并提前排除'直接做法'。

- research_evidence_required_cn：对每个组件的'直接/朴素做法'列出具体缺点（稀疏、忽略相关、需重训）；可计算的方法实现。

- sentence_pattern_function_cn：先说'理论上可直接…但有三个缺点'，再接'为克服这些缺点，我用…'，最后开放替代方案比较。

- transition_condition_cn：当每个组件都有必要性和可实现性后进入下一步。

### 6. 6

- step：6

- rhetorical_job_cn：用模型无关证据证明缺陷现象在数据中真实存在。

- research_evidence_required_cn：真实数据中的分布图、分技能差异图、时序技能变化图和特征轨迹。

- sentence_pattern_function_cn：逐图解释：图(a)显示膨胀；图(b)(c)显示归因；图(d)-(f)组合显示动态性，每个图都有明确数值。

- transition_condition_cn：当三类缺陷都有直接影像后进入下一步。

### 7. 7

- step：7

- rhetorical_job_cn：固定评估协议并选定最终配置，使后续比较可信。

- research_evidence_required_cn：按个体分折的交叉验证设置；对每个组件候选做网格搜索的对比结果。

- sentence_pattern_function_cn：先声明协议（'每个工人完整历史只在一折'），再报告网格搜索最终选择，逐项列出。

- transition_condition_cn：当最终配置确定且协议透明后进入下一步。

### 8. 8

- step：8

- rhetorical_job_cn：用多指标和多基准确立主优势，并细化为子群体和决策情境。

- research_evidence_required_cn：排序相关、排序表现、lift、分布距离、子群体结果、Open内Top-n结果及各baseline指标。

- sentence_pattern_function_cn：对每个评价目标先'为什么用此指标'，再报告改进百分比和显著性，最后把结果回挂到缺陷。

- transition_condition_cn：当主优势在多个评价层面成立后进入下一步。

### 9. 9

- step：9

- rhetorical_job_cn：排除相邻技术族，展示新制品的不可替代性。

- research_evidence_required_cn：把相邻技术（推荐系统）按映射/编码假设改造成候选，并实现在同一协议下比较。

- sentence_pattern_function_cn：先用一节说明概念差异和映射假设，再在结果节实现并报告性能差距，最后总结'适配假设伤害性能'。

- transition_condition_cn：当相邻技术族被实证排除后进入下一步。

### 10. 10

- step：10

- rhetorical_job_cn：展示制品在下游任务中的协作价值，把排序优势转化为交易效率。

- research_evidence_required_cn：下游预测任务（如申请者推荐）的特征设置对比实验和AUC增量。

- sentence_pattern_function_cn：设计多组特征设置，报告'替代当前特征'与'在原有特征上叠加'两类增益。

- transition_condition_cn：当下游增益量化后进入下一步。

### 11. 11

- step：11

- rhetorical_job_cn：用第二情境复制证明泛化，并排他地处理已有相似系统的解释。

- research_evidence_required_cn：一个满足相同制度条件的外部数据集；与替代系统和已有相关评分的比较。

- sentence_pattern_function_cn：先论证目标情境具备三缺陷条件，再报告复制结果，最后与人工维度比较排除冗余解释。

- transition_condition_cn：当外部效度和排他性都成立后进入下一步。

### 12. 12

- step：12

- rhetorical_job_cn：把实证结果升级为设计知识、方法论指南和边界条件，并开放未来工作。

- research_evidence_required_cn：对建模假设的辩护、边界条件（如W2V vs D2V）的实证来源、平台应用的合理推理。

- sentence_pattern_function_cn：先重述缺陷-组件-结果，再分层声明研究/设计贡献，然后给出指南和平台示例，最后逐一处理维护假设和边界。

- transition_condition_cn：当贡献、边界和未来方向全部覆盖后结束。

## 应模仿的高价值动作

1. 缺陷命名法：用三个可记忆标签（膨胀、归因、静态性）把模糊问题变成可检验缺口。

2. 缺口表：用表1把每个现有系统对每个缺陷打叉，使'无人解决'可见。

3. 模型无关证据在建模之前，用图2六面板逐证三现象，让设计原则有经验根据。

4. 组件级网格搜索：每个组件都报告'试了什么、为什么选这个'。

5. 反直觉设计选择辩护：对降级转移用HMM纠错情景解释，并附附录实证。

6. 子群体评价：用非完美工人子集防止整体准确率被膨胀掩盖。

7. 排除-互补两步策略：先让候选技术族在自己设定的映射下失败，再展示新制品作为其特征的增量增益。

8. 第二情境复制加排他检验：餐馆数据不仅复制主结果，还证明与人工四维评分不同。

9. 边界条件明确：在W2V/D2V差异处承认情境依赖，避免过度泛化。

10. 讨论开篇的三句重述法：重述缺陷、重述组件、重述结果，把全文闭合。

## 不要只复制的表面动作

1. 不要只堆'动态、多维、技能集'等标签，却没有让这些概念对应到可测量的数据特征（如技能集相似度、新技能轨迹）。

2. 不要仅声称'首次'而不提供可核查的现有系统比较矩阵。

3. 不要在没有子群体分析的情况下声称系统解决膨胀；完美工人主导的准确率会掩盖问题。

4. 不要把正态分布作为设计目标却不报告分布接近程度。

5. 不要只做总体精度提升，而不展示决策情境（如Top-n选择）和下游任务（如推荐AUC）收益。

6. 不要忽略相邻技术族的适配实验，仅以'概念不同'排除推荐系统。

7. 不要把离线AUC/排序提升直接写成平台收入；应区分结果与推断。

## 证据薄弱或跳跃的动作

1. 从离线AUC提升到平台收入/雇主满意/持续收入的跳跃没有直接现场或因果关系证据。

2. '首次'主张依赖文献覆盖质量，无法由本文数据验证。

3. 以正态分布作为最优声誉分布的目标有强假设性质：近正态是否等于更好区分工人未被直接证明。

4. Open内排序对最强基线（WorkerRank和XGBoost）只在部分n上显著，摘要/引言中'显著更好'的表述弱化了这一局限。

5. 餐馆评论泛化只有一个外部情境，不能证明对Yelp/Uber/LinkedIn等全部平台成立。

6. 模型无关证据中的'新技能后低分随后回升'是描述性轨迹，未控制选择效应（何时学新技能可能与绩效相关）。

7. 潜在能力维的含义（附录H）是事后解释，未经验证其稳定性和可解释性。

## 一句话套路

把对手系统在三个命名缺陷上打靶，把缺陷翻译成三条设计原则，把原则落地成组件，用多基准、多指标、子群体、下游任务和跨领域复制证明制品更优，再把结果重述为可复用的设计知识和边界条件。

## 分析边界

正文Markdown完整可读，但Online Appendices A-I只有正文引用而无原文，参数推导、图11/13-16、表5和附录E.3的具体数字无法直接核对，因此对附录支撑的细节判断以正文引用和图表标题为准；OCR在表格脚注处有截断（Table 1/2的Notes），部分脚注信息可能被遗漏。摘要、引言、正文、讨论均已逐句核实，第一阶段分析中关于'声誉分布接近正态平均37%'、'AUC 2.4-10%'等数字在正文中确认。
