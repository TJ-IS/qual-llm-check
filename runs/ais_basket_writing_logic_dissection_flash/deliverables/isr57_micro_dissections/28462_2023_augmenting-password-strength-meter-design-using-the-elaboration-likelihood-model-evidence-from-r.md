# Augmenting Password Strength Meter Design Using the Elaboration Likelihood Model: Evidence from Randomized Experiments：ISR 句段级微观图谱

- 作者：Warut Khern-am-nuai; Matthew J. Hashim; Alain Pinsonneault; Weining Yang; Ninghui Li
- 年份：2023
- DOI：10.1287/isre.2022.1125
- 源文件：28462_2023_augmenting-password-strength-meter-design-using-the-elaboration-likelihood-model-evidence-from-r.md
- 置信度：0.86

## 核实后的宏观骨架

文章以密码认证在组织中的主导地位和弱密码的持续问题开篇，通过否定替代技术（密码管理器、MFA）确立密码强度计的不可替代性。引言随后把现有研究定位为集中在算法精度而忽视呈现组件，以Furnell(2011)的发现建立理论缺口，并引入ELM作为心理学理论、采用设计科学范式（Gregor Type V）推导三阶段证据链：survey证明消息被中心路径加工（proof of concept）、受控实验室实验证明行为效果（proof of value）、现场随机实验证明真实环境有效性（proof of use）。制品实现部分固定backoff Markov强度算法与阈值，仅改变提示消息：Time（恐惧诉求）、Rank（同伴比较）、Probability（共同纽带）。研究结果一致支持Rank效果最强，Time和Probability在实验室中不显著、在现场仅边缘显著。讨论把Rank优势解释为数字情境中社会比较的重要性，回馈并修正ELM，同时给出现实暴力破解效益和管理可部署性主张。

## 摘要逐句图谱

### 1. Abstract S1

- order：1

- locator：Abstract S1

- paraphrase_cn：密码认证是访问安全系统最常用的方法。

- move_code：CONTEXT

- statement_status：fact

- why_here_cn：文章第一句把后续所有讨论都锚定在密码作为主导认证机制的既定事实上，为读者建立领域常规。

- inherits_from_previous_cn：无前句。

- changes_argument_state_cn：设定问题领域和关键词。

- sets_up_next_cn：制造被下一句继承的'既然密码普遍，弱点就普遍'隐含推理。

- failure_if_removed_cn：摘要失去领域入口，后面'弱密码'和经验证据失去对象。

- evidence_pointer：Abstract S1

### 2. Abstract S2

- order：2

- locator：Abstract S2

- paraphrase_cn：经验证据显示大多数密码显著弱，鼓励用户创建更强密码是重大挑战。

- move_code：PRACTICAL_STAKES

- statement_status：prior_literature

- why_here_cn：在第一句基础上升华出该领域的持续失败点，让改进密码强度计成为有实际价值的研究目标。

- inherits_from_previous_cn：密码普遍。

- changes_argument_state_cn：从静态常用状态到动态'用户行为需要被改变'的任务陈述。

- sets_up_next_cn：为'提出新设计'提供必要性。

- failure_if_removed_cn：设计与研究目标失去现实紧迫性。

- evidence_pointer：Abstract S2

### 3. Abstract S3

- order：3

- locator：Abstract S3

- paraphrase_cn：本研究提出一个由ELM说服理论指导的理论增强的密码强度计设计。

- move_code：THEORY_INTRO

- statement_status：contribution_claim

- why_here_cn：引入具体的理论话语，把'怎么解决挑战'变成'用哪个理论设计制品'。

- inherits_from_previous_cn：需要解决用户不强密码的挑战。

- changes_argument_state_cn：宣告文章核心主张：理论引导的增强设计。

- sets_up_next_cn：预告需要被下一句中的评价方法验证。

- failure_if_removed_cn：摘要中的'设计'失去理论支撑，读者不知文章新意是什么。

- evidence_pointer：Abstract S3

### 4. Abstract S4

- order：4

- locator：Abstract S4

- paraphrase_cn：用三种独立互补方法评估设计：以学生为基础的survey（proof of concept）、MTurk上的受控实验室实验（proof of value）、与亚洲在线论坛合作的随机现场实验（proof of use）。

- move_code：STUDY_OVERVIEW

- statement_status：method_decision

- why_here_cn：在摘要第二句到第三句建立'主张'后，立刻给出证据来源，让摘要自己提供可信的方法链条。

- inherits_from_previous_cn：存在需要验证的设计。

- changes_argument_state_cn：从提议转变为'这些就是支撑该提议的证据类型'。

- sets_up_next_cn：为下一句'每项研究观察什么'提供具体实验语境。

- failure_if_removed_cn：文章实证基础无法从摘要中被看到，'findings'成为无源断言。

- evidence_pointer：Abstract S4

### 5. Abstract S5

- order：5

- locator：Abstract S5

- paraphrase_cn：在每项研究中都观察用户行为对其响应强度计的变化。

- move_code：METHOD_SCOPE

- statement_status：method_decision

- why_here_cn：强调研究的统一行为结果变量，让三种不同样本和方法的证据可被看成一个整体的效果证据。

- inherits_from_previous_cn：三种研究评价方式。

- changes_argument_state_cn：开始把方法锚定到行为改变实际结果。

- sets_up_next_cn：让下一句具体结果有了明确测量对象。

- failure_if_removed_cn：用户读不到'在每项研究中观察什么'的明确性，后面findings就没有测量立场。

- evidence_pointer：Abstract S5

### 6. Abstract S6

- order：6

- locator：Abstract S6

- paraphrase_cn：发现ELM增强型密码强度计在应对基于密码认证的挑战方面显著有效。

- move_code：RESULT

- statement_status：empirical_result

- why_here_cn：在方法预告之后用强结论锁定读者期望，摘要的主体主张落到结果上。

- inherits_from_previous_cn：三种方法对行为改变的观察。

- changes_argument_state_cn：从'预期设计有效'推进到'我们用随机证据支持该设计有效'。

- sets_up_next_cn：下一句详细说明具体变化是什么。

- failure_if_removed_cn：摘要缺少核心发现，贡献声明失去依据。

- evidence_pointer：Abstract S6

### 7. Abstract S7

- order：7

- locator：Abstract S7

- paraphrase_cn：接触到这种强度的用户更可能更改密码，新的密码显著较强。

- move_code：RESULT_DETAIL

- statement_status：empirical_result

- why_here_cn：把抽象的'显著有效'转为两个可理解的关键行为指标（密码修改和最终强度），提供摘要中最具体的发现。

- inherits_from_previous_cn：上一句声称整体有效。

- changes_argument_state_cn：把'有效'转化为'修改行为'和'强度改善'两个证据点的概括。

- sets_up_next_cn：为下一句贡献声明提供材料。

- failure_if_removed_cn：摘要丧失操作性意义，'有效'成为空洞标签。

- evidence_pointer：Abstract S7

### 8. Abstract S8

- order：8

- locator：Abstract S8

- paraphrase_cn：这些发现表明，增强型密码强度计的提案设计是促进终端用户安全密码行为的有效方法。

- move_code：CONTRIBUTION

- statement_status：contribution_claim

- why_here_cn：摘要以建议性一般化收尾，把特定实验发现转成对实践者有用的方法主张。

- inherits_from_previous_cn：上一句总结的实证结果。

- changes_argument_state_cn：从证据状态跳转到实践建议状态，完成摘要三段式：问题→证据→贡献。

- sets_up_next_cn：让读者期待正文对'如何有效'的展开。

- failure_if_removed_cn：摘要缺少可引用的贡献句。

- evidence_pointer：Abstract S8

## 引言逐句图谱

### 1. Introduction P1 S1

- order：1

- locator：Introduction P1 S1

- paraphrase_cn：密码是组织实施访问控制的主要认证机制。

- move_code：CONTEXT

- statement_status：fact

- why_here_cn：用组织/IS视角开篇，把密码问题置于企业安全语境中。

- inherits_from_previous_cn：无。

- changes_argument_state_cn：确定研究不是在纯HCI或安全工程中，而是在IS系统中。

- sets_up_next_cn：下一句可以直接谈组织相关性和价值。

- failure_if_removed_cn：文章开始缺少IS定位，容易被读成通用可用性研究。

- evidence_pointer：Introduction P1 S1

### 2. Introduction P1 S2

- order：2

- locator：Introduction P1 S2

- paraphrase_cn：因此密码安全问题对组织至关重要，改善用户'密码生成行为'的技术通常有价值。

- move_code：PRACTICAL_STAKES

- statement_status：author_inference

- why_here_cn：把第一句中的常用机制与组织利害连接起来，明确行为改变是研究价值源。

- inherits_from_previous_cn：密码是主导认证机制。

- changes_argument_state_cn：从'密码普遍'到'密码安全行为改善有组织价值'。

- sets_up_next_cn：为后面'设计需要改善用户行为'设前提。

- failure_if_removed_cn：文章最初的重要性主张缺位。

- evidence_pointer：Introduction P1 S2

### 3. Introduction P1 S3

- order：3

- locator：Introduction P1 S3

- paraphrase_cn：尽管密码安全重要，一些专家宣称密码相关问题将在不久后无关紧要。

- move_code：COUNTER_CLAIM

- statement_status：prior_literature

- why_here_cn：本文需要排除'密码即将过时'这个替代立场，使密码强度计研究仍具必要性。

- inherits_from_previous_cn：密码问题重要。

- changes_argument_state_cn：引入潜在反驳，增加论证张力。

- sets_up_next_cn：下一句用实践证据反驳它。

- failure_if_removed_cn：读者会以为替代认证即将取代密码，文章意义削弱。

- evidence_pointer：Introduction P1 S3

### 4. Introduction P1 S4

- order：4

- locator：Introduction P1 S4

- paraphrase_cn：然而实践证据显示并非如此。

- move_code：PIVOT

- statement_status：fact

- why_here_cn：一句话完成对'密码过时'论点的反转，建立文章现实出发点。

- inherits_from_previous_cn：专家宣称无关紧要。

- changes_argument_state_cn：否定替代立場，维持密码研究的相关性。

- sets_up_next_cn：随后用具体例子支撑这个反转。

- failure_if_removed_cn：前面与后续讨论脱节。

- evidence_pointer：Introduction P1 S4

### 5. Introduction P1 S5

- order：5

- locator：Introduction P1 S5

- paraphrase_cn：例如，即使依法要求增强安全性的美国国务院也难以超越密码。

- move_code：EVIDENCE_EXAMPLE

- statement_status：fact

- why_here_cn：用高公信力组织实例把'密码过时'论点具体驳倒，现实证据比专家声明更有说服力。

- inherits_from_previous_cn：实践证据反驳专家论断。

- changes_argument_state_cn：把反驳落到一个具体、可信的案例上。

- sets_up_next_cn：接下来的密码管理器和MFA问题也属于替代技术失败类别。

- failure_if_removed_cn：反转停留在断言层面。

- evidence_pointer：Introduction P1 S5

### 6. Introduction P1 S6

- order：6

- locator：Introduction P1 S6

- paraphrase_cn：与此同时，试图减轻密码问题的技术可能产生意想不到的后果。

- move_code：TRANSITION_TO_LIMITATION

- statement_status：author_inference

- why_here_cn：从'密码仍必要'转到'替代技术也有缺陷'，排除另外两条解决路径。

- inherits_from_previous_cn：密码被证实仍占据主导。

- changes_argument_state_cn：把讨论焦点收拢到'技术替代品本身也有问题'。

- sets_up_next_cn：下两句开始讲密码管理器和MFA的具体弱点。

- failure_if_removed_cn：密码管理器与MFA的批判失去总起句。

- evidence_pointer：Introduction P1 S6

### 7. Introduction P1 S7

- order：7

- locator：Introduction P1 S7

- paraphrase_cn：研究人员发现一些热门密码管理器受到严重漏洞影响，暴露用户凭证。

- move_code：TECHNOLOGY_FAILURE

- statement_status：fact

- why_here_cn：给出第一项替代技术的具体失败事实。

- inherits_from_previous_cn：替代技术可能带来意外后果。

- changes_argument_state_cn：把'密码管理器可解决问题'这一选项弱化。

- sets_up_next_cn：顺理成章地说'所以使用管理器并不一定解决问题'。

- failure_if_removed_cn：对密码管理器的排除失去证据。

- evidence_pointer：Introduction P1 S7

### 8. Introduction P1 S8

- order：8

- locator：Introduction P1 S8

- paraphrase_cn：因此使用带复杂密码的密码管理软件可能并不能解决所有密码问题。

- move_code：LIMITATION_INFERENCE

- statement_status：author_inference

- why_here_cn：把漏洞证据转化为对技术路线的否定，从事实到推断。

- inherits_from_previous_cn：密码管理器有漏洞。

- changes_argument_state_cn：密码管理器那条解决路径被排除。

- sets_up_next_cn：MFA将成为下一个被质疑的替代技术。

- failure_if_removed_cn：密码管理器失败性证伪不完全。

- evidence_pointer：Introduction P1 S8

### 9. Introduction P1 S9

- order：9

- locator：Introduction P1 S9

- paraphrase_cn：同时，实现多因素认证的成本因用短信和邮件接收一次性密码的不安全实践而显著增加。

- move_code：TECHNOLOGY_FAILURE

- statement_status：fact

- why_here_cn：排除第二种替代技术（MFA），并说明成本/安全并存的问题。

- inherits_from_previous_cn：在密码管理器已排除后，继续检查其他替代。

- changes_argument_state_cn：MFA的高成本和弱实现被呈现。

- sets_up_next_cn：下一句总结MFA对中小企业负担过高。

- failure_if_removed_cn：MFA路线未排除，文章集中在强度计上的理由不完整。

- evidence_pointer：Introduction P1 S9

### 10. Introduction P1 S10

- order：10

- locator：Introduction P1 S10

- paraphrase_cn：所以该技术对中小企业而言过于昂贵。

- move_code：LIMITATION_INFERENCE

- statement_status：author_inference

- why_here_cn：为MFA排除路线给出经济边界，说明为什么不能作为普适方案。

- inherits_from_previous_cn：MFA成本上升。

- changes_argument_state_cn：完成替代技术排除链条：密码管理器、MFA都不够可行。

- sets_up_next_cn：让第三段的焦点回到密码强度计。

- failure_if_removed_cn：MFA排除仅停留在技术层面，但'为什么不能广泛采用'缺乏经济理由。

- evidence_pointer：Introduction P1 S10

### 11. Introduction P2 S1

- order：11

- locator：Introduction P2 S1

- paraphrase_cn：由于替代技术的意外不可行，有效解决方案的聚光灯重新聚焦到诸如增强密码强度计的说服技术。

- move_code：PHENOMENON_NARROWING

- statement_status：author_inference

- why_here_cn：用'重新聚焦'完成从全行业密码问题到具体制品（强度计）的收窄。

- inherits_from_previous_cn：替代方案不可行。

- changes_argument_state_cn：研究对象被确定为密码强度计。

- sets_up_next_cn：为第二段陈述目标设计特征做好铺垫。

- failure_if_removed_cn：文章对象不明，后面的强度计讨论突兀。

- evidence_pointer：Introduction P2 S1

### 12. Introduction P2 S2

- order：12

- locator：Introduction P2 S2

- paraphrase_cn：本文设计一个增强型密码强度计，并具有以下特征。

- move_code：OBJECTIVE

- statement_status：design_decision

- why_here_cn：明确给出本文行动，是引言中第一次说明'我们做什么'。

- inherits_from_previous_cn：增强密码强度计是焦点。

- changes_argument_state_cn：从问题陈述转到问题解决设计。

- sets_up_next_cn：接下来的三个特征列点给设计标准。

- failure_if_removed_cn：研究目标不显式，读者不知道文章将呈现一个制品。

- evidence_pointer：Introduction P2 S2

### 13. Introduction P2 S3

- order：13

- locator：Introduction P2 S3

- paraphrase_cn：第一，设计由知名心理学理论驱动。

- move_code：DESIGN_CRITERION

- statement_status：design_decision

- why_here_cn：把'理论驱动'作为设计第一标准，直接呼应4-5节文献缺理论的缺口。

- inherits_from_previous_cn：本文设计增强强度计。

- changes_argument_state_cn：定义了什么算合法设计方案：必须有理论根基。

- sets_up_next_cn：后文ELM正是此标准的执行。

- failure_if_removed_cn：理论驱动性不成为设计卖点。

- evidence_pointer：Introduction P2 S3

### 14. Introduction P2 S4

- order：14

- locator：Introduction P2 S4

- paraphrase_cn：第二，在不使用被NIST指南所不鼓励的密码复杂度政策的前提下显著增强用户的密码生成行为。

- move_code：DESIGN_CRITERION

- statement_status：design_decision

- why_here_cn：把NIST SP 800-63作为必要条件，使设计必须避开复杂度要求，与政策潮流保持一致。

- inherits_from_previous_cn：设计目标列点。

- changes_argument_state_cn：划定设计禁令：不能依赖复杂度政策。

- sets_up_next_cn：设计必须找到行为干预的非强制方式，这就为消息设计做了铺垫。

- failure_if_removed_cn：设计范围太宽，读者可能期望策略型干预。

- evidence_pointer：Introduction P2 S4

### 15. Introduction P2 S5

- order：15

- locator：Introduction P2 S5

- paraphrase_cn：第三，可低成本快速部署于多种环境。

- move_code：DESIGN_CRITERION

- statement_status：design_decision

- why_here_cn：把可部署性纳入设计标准，为后文'仅客户端小改'的实践贡献铺垫。

- inherits_from_previous_cn：设计目标列点。

- changes_argument_state_cn：增加约束：不能需要大量基础设施。

- sets_up_next_cn：使得设计必须是轻量级消息而非系统级改造。

- failure_if_removed_cn：实践贡献会减少一条。

- evidence_pointer：Introduction P2 S5

### 16. Introduction P3 S1

- order：16

- locator：Introduction P3 S1

- paraphrase_cn：密码强度计计算输入密码的复杂度并显示强度，通常为弱到强。

- move_code：ARTIFACT_DEFINITION

- statement_status：fact

- why_here_cn：给出研究对象的规范描述，让后续批评有明确对象。

- inherits_from_previous_cn：研究对象是密码强度计。

- changes_argument_state_cn：把'强度计'从日常名词变成可分析的技术制品：计算+显示。

- sets_up_next_cn：引出'理想情况是用户看到反馈后修改密码'。

- failure_if_removed_cn：读者缺乏对该制品的共享定义。

- evidence_pointer：Introduction P3 S1

### 17. Introduction P3 S2

- order：17

- locator：Introduction P3 S2

- paraphrase_cn：理想情况下，最初选择较弱密码的用户会收到反馈并考虑修改密码。

- move_code：IDEAL_FUNCTION

- statement_status：design_decision

- why_here_cn：界定强度计的设计目标=促使修改密码，为后文选择obsolete指标提供依据。

- inherits_from_previous_cn：强度计显示强度。

- changes_argument_state_cn：为强度计设立行为标准。

- sets_up_next_cn：这个理想与第三段现实差距形成张力。

- failure_if_removed_cn：强度计的最终目标不明确。

- evidence_pointer：Introduction P3 S2

### 18. Introduction P3 S3

- order：18

- locator：Introduction P3 S3

- paraphrase_cn：尽管文献表明强度计在受控环境下普遍能促使用户创建更强密码，但现实中其效果仍是争议话题。

- move_code：LIMITATION

- statement_status：prior_literature

- why_here_cn：建立文献结论与现实效果之间的落差，即研究动机的重要来源。

- inherits_from_previous_cn：理想功能。

- changes_argument_state_cn：从'理想'到'并不一定实现'。

- sets_up_next_cn：证明需要改进设计或研究呈现。

- failure_if_removed_cn：问题不成立：如果现实效果已经很好，就不再需要本文研究。

- evidence_pointer：Introduction P3 S3

### 19. Introduction P3 S4

- order：19

- locator：Introduction P3 S4

- paraphrase_cn：例如，即使许多网站和系统都有强度计，弱密码问题依然存在。

- move_code：EVIDENCE_EXAMPLE

- statement_status：fact

- why_here_cn：用行业数据强化'现实效果差'，使研究动机有经验基础。

- inherits_from_previous_cn：现实中强度计效果有争议。

- changes_argument_state_cn：把争议落实为可观察的困扰。

- sets_up_next_cn：引出'因此许多近期工作试图改进'。

- failure_if_removed_cn：效率差距只剩文献观点无现实依据。

- evidence_pointer：Introduction P3 S4

### 20. Introduction P3 S5

- order：20

- locator：Introduction P3 S5

- paraphrase_cn：因此许多近期工作致力于改进密码强度计的有效性。

- move_code：LITERATURE_CONTEXT

- statement_status：prior_literature

- why_here_cn：表明自己不是唯一发现该问题的人，确立研究所属工作流。

- inherits_from_previous_cn：弱密码问题持续。

- changes_argument_state_cn：告诉读者当前正在进行技术改进潮。

- sets_up_next_cn：下一句具体说明主流改进路径，为勾画缺口做准备。

- failure_if_removed_cn：现有工作脉络缺失，接下来的'转向'缺少对象。

- evidence_pointer：Introduction P3 S5

### 21. Introduction P3 S6

- order：21

- locator：Introduction P3 S6

- paraphrase_cn：该工作流的主要焦点是增强计算强度的算法，认为传统强度计不准确所以无效。

- move_code：MAINSTREAM_THESIS

- statement_status：prior_literature

- why_here_cn：用一句话概括主流路线及其假设，为后文'我们不同'提供清晰参照。

- inherits_from_previous_cn：存在改善工作潮。

- changes_argument_state_cn：明确了竞争者路径是'算法精度'。

- sets_up_next_cn：后句指出该路线的一系列技术方法，然后指出本文回到呈现组件。

- failure_if_removed_cn：缺口无法具体描述：读者不知道作者在反对/补充什么。

- evidence_pointer：Introduction P3 S6

### 22. Introduction P3 S7

- order：22

- locator：Introduction P3 S7

- paraphrase_cn：尽管普遍认为强度计比理想熵测量不精确，已经提出许多先进技术来克服，如概率上下文无关文法和Markov模型。

- move_code：MAINSTREAM_METHODS

- statement_status：prior_literature

- why_here_cn：展示主流路线技术成熟度，反衬呈现组件研究稀缺，形成'技术解决了算法，但界面仍黑箱'的缝隙。

- inherits_from_previous_cn：主流焦点是算法。

- changes_argument_state_cn：暗示算法路线的成就；它还不是缺口。

- sets_up_next_cn：下句又补'替代指标'，目的是使第四段的'呈现组件'缺口更精确。

- failure_if_removed_cn：后续'我们研究呈现组件'缺对照。

- evidence_pointer：Introduction P3 S7

### 23. Introduction P3 S8

- order：23

- locator：Introduction P3 S8

- paraphrase_cn：此外，还引入了模拟破解算法和密码排名算法等替代强度指标。

- move_code：MAINSTREAM_METHODS

- statement_status：prior_literature

- why_here_cn：完成对主流工具谱系的清单，强调整个领域都在精化'度量'而忽视'沟通'。

- inherits_from_previous_cn：算法改进。

- changes_argument_state_cn：把主流谱系扩展到这些复杂度量方法。

- sets_up_next_cn：为第四段'当算法固定时呈现组件如何'制造空间。

- failure_if_removed_cn：主流谱系不完整，'不被研究的大部分'不清晰。

- evidence_pointer：Introduction P3 S8

### 24. Introduction P4 S1

- order：24

- locator：Introduction P4 S1

- paraphrase_cn：在本研究中，我们从另一个角度研究传统强度计，以补充主流研究。

- move_code：GAP_COMPLEMENT

- statement_status：author_inference

- why_here_cn：第一次明确本文位置：不是替代算法研究，而是补充呈现组件研究。

- inherits_from_previous_cn：主流研究集中于算法。

- changes_argument_state_cn：宣告差异化贡献方向。

- sets_up_next_cn：下句精确界定'当算法不变时'的条件。

- failure_if_removed_cn：研究定位和差异化消失。

- evidence_pointer：Introduction P4 S1

### 25. Introduction P4 S2

- order：25

- locator：Introduction P4 S2

- paraphrase_cn：具体来说，我们在保持密码强度算法恒定的情况下研究密码强度计的呈现组件。

- move_code：RESEARCH_SCOPE

- statement_status：method_decision

- why_here_cn：用'算法固定'作为可操纵性条件，排除算法混淆，聚焦界面消息。

- inherits_from_previous_cn：替代角度。

- changes_argument_state_cn：研究边界明确。

- sets_up_next_cn：为后面'唯一差异是消息、算法一致'做设定。

- failure_if_removed_cn：实验设计和结论适用范围无法界定。

- evidence_pointer：Introduction P4 S2

### 26. Introduction P4 S3

- order：26

- locator：Introduction P4 S3

- paraphrase_cn：文章建立在Furnell的发现上：有理论基础的强度计界面设计指南稀缺。

- move_code：THEORETICAL_GAP

- statement_status：fact

- why_here_cn：用文献断定理论指南稀缺，这是文章设计科学范式正当性的主要依据。

- inherits_from_previous_cn：关注呈现组件。

- changes_argument_state_cn：从技术缺口跳到理论缺口：界面设计缺乏解释和理解性。

- sets_up_next_cn：接着Black-box叙述使'理论缺口'更具体。

- failure_if_removed_cn：论文的心理学/设计科学方向失去文献支持。

- evidence_pointer：Introduction P4 S3

### 27. Introduction P4 S4

- order：27

- locator：Introduction P4 S4

- paraphrase_cn：所以大多数强度计的设计和实现都像黑箱，没有设计选择解释，用户难以理解。

- move_code：GAP_ELABORATION

- statement_status：author_inference

- why_here_cn：把'理论指南稀缺'转成'当前实现不可解释'，说明必须引入理论解释。

- inherits_from_previous_cn：理论指南稀缺。

- changes_argument_state_cn：描述当前制品的失败认知层面。

- sets_up_next_cn：确定需要心理学理论来'解开黑箱'。

- failure_if_removed_cn：黑箱问题不存在，则引入ELM解释的理由被削弱。

- evidence_pointer：Introduction P4 S4

### 28. Introduction P4 S5

- order：28

- locator：Introduction P4 S5

- paraphrase_cn：受此启示，本文识别一种心理学理论来支撑密码强度计的核心功能。

- move_code：THEORY_INTRO

- statement_status：author_inference

- why_here_cn：由'理论指南稀缺'顺理成章地选定理论，完成从问题到理论的桥接。

- inherits_from_previous_cn：黑箱且缺理论。

- changes_argument_state_cn：宣告将有理论介入。

- sets_up_next_cn：下一句给出具体理论并指定设计科学方法。

- failure_if_removed_cn：理论引入无动机。

- evidence_pointer：Introduction P4 S5

### 29. Introduction P4 S6

- order：29

- locator：Introduction P4 S6

- paraphrase_cn：具体来说，我们借鉴ELM，按照设计科学文献的建议开发一种理论指导的强度计设计。

- move_code：THEORY_DETAIL

- statement_status：theory_claim

- why_here_cn：点明具体理论和研究范式（Gregor和Hevner），告知读者论证框架。

- inherits_from_previous_cn：需要理论。

- changes_argument_state_cn：理论工具箱明确：ELM+设计科学。

- sets_up_next_cn：让后文三个proof有方法框架。

- failure_if_removed_cn：读者不知道'哪种心理学'及'怎样实现'。

- evidence_pointer：Introduction P4 S6

### 30. Introduction P4 S7

- order：30

- locator：Introduction P4 S7

- paraphrase_cn：随后利用多个随机实验建立理论增强设计的证明概念、证明价值和证明使用。

- move_code：METHOD_OVERVIEW

- statement_status：method_decision

- why_here_cn：给出证据链总纲，将摘要中的三阶段预告在引言中重现。

- inherits_from_previous_cn：理论引导的设计。

- changes_argument_state_cn：文章论证以随机实验为核心。

- sets_up_next_cn：下一步透出'将发现'核心结果。

- failure_if_removed_cn：研究评价方式缺失，'有效'无从支撑。

- evidence_pointer：Introduction P4 S7

### 31. Introduction P4 S8

- order：31

- locator：Introduction P4 S8

- paraphrase_cn：我们发现所提强度计按理论增强了密码安全性。

- move_code：RESULT_PREVIEW

- statement_status：empirical_result

- why_here_cn：先给出正面结论，为引言的贡献声明提供证据预期。

- inherits_from_previous_cn：随机实验证据已建成。

- changes_argument_state_cn：从方法过渡到核心发现。

- sets_up_next_cn：具体行为改变被下一句细化。

- failure_if_removed_cn：读者在引言读不到结局，贡献声明空泛。

- evidence_pointer：Introduction P4 S8

### 32. Introduction P4 S9

- order：32

- locator：Introduction P4 S9

- paraphrase_cn：它有效推动用户更容易更改密码，且用户选择的新密码显著强于首次输入的密码。

- move_code：RESULT_PREVIEW_DETAIL

- statement_status：empirical_result

- why_here_cn：用行为层面具体结果让'增强安全性'可被理解。

- inherits_from_previous_cn：密码安全性增强。

- changes_argument_state_cn：引出后文两大因变量：修改行为和强度变化。

- sets_up_next_cn：为第五段'贡献'制造根据。

- failure_if_removed_cn：贡献过度笼统缺乏操作性。

- evidence_pointer：Introduction P4 S9

### 33. Introduction P5 S1

- order：33

- locator：Introduction P5 S1

- paraphrase_cn：我们的研究对理论与实践做出贡献。

- move_code：CONTRIBUTION_OPENING

- statement_status：contribution_claim

- why_here_cn：贡献段开场白，明确双层贡献。

- inherits_from_previous_cn：研究有结果。

- changes_argument_state_cn：把论文价值提升为社会性贡献。

- sets_up_next_cn：后文按理论和实践分列。

- failure_if_removed_cn：贡献部分失去总起。

- evidence_pointer：Introduction P5 S1

### 34. Introduction P5 S2

- order：34

- locator：Introduction P5 S2

- paraphrase_cn：在理论贡献方面，我们是最早为密码强度计如何与用户互动并影响用户建立理论基础的人之一。

- move_code：THEORETICAL_CONTRIBUTION

- statement_status：contribution_claim

- why_here_cn：定位理论贡献：建立互动理论基础，而非只是性能测试。

- inherits_from_previous_cn：贡献声明。

- changes_argument_state_cn：声称填补理论空白。

- sets_up_next_cn：下句说明用该基础改善设计。

- failure_if_removed_cn：理论贡献主体内容缺失。

- evidence_pointer：Introduction P5 S2

### 35. Introduction P5 S3

- order：35

- locator：Introduction P5 S3

- paraphrase_cn：然后利用这样的基础提出增强强度计，改善用户密码生成行为。

- move_code：CONTRIBUTION_ELABORATION

- statement_status：contribution_claim

- why_here_cn：把理论贡献与制品贡献绑定：理论不是独立在场，而是服务于设计。

- inherits_from_previous_cn：理论基础。

- changes_argument_state_cn：理论→设计链条已宣告。

- sets_up_next_cn：为交付的实验证据做注脚。

- failure_if_removed_cn：理论贡献与建议制品之间的联系不清。

- evidence_pointer：Introduction P5 S3

### 36. Introduction P5 S4

- order：36

- locator：Introduction P5 S4

- paraphrase_cn：通过多个实验证明改进设计是促进终端用户安全行为的有前途方式。

- move_code：CONTRIBUTION_EVIDENCE_PREVIEW

- statement_status：contribution_claim

- why_here_cn：把贡献定位与实验结果连接，预告正文证据。

- inherits_from_previous_cn：提出增强设计。

- changes_argument_state_cn：贡献声明带有实证意味。

- sets_up_next_cn：为实践贡献转向做铺垫。

- failure_if_removed_cn：理论贡献显得没有证据支持。

- evidence_pointer：Introduction P5 S4

### 37. Introduction P5 S5

- order：37

- locator：Introduction P5 S5

- paraphrase_cn：关于实践贡献，设计的创新在于只需最小化改服务器端和客户端。

- move_code：PRACTICAL_CONTRIBUTION

- statement_status：contribution_claim

- why_here_cn：把实践贡献集中到低成本可部署性，呼应第二段第三特征。

- inherits_from_previous_cn：贡献列表继续。

- changes_argument_state_cn：贡献转向实际落地。

- sets_up_next_cn：对'不需服务器资源'给出原因。

- failure_if_removed_cn：实践贡献失去卖点。

- evidence_pointer：Introduction P5 S5

### 38. Introduction P5 S6

- order：38

- locator：Introduction P5 S6

- paraphrase_cn：设计无需服务器端大量计算资源，不必像其他认证技术那样投资新硬件。

- move_code：PRACTICAL_CONTRIBUTION_MECHANISM

- statement_status：contribution_claim

- why_here_cn：解释为什么实践上很便宜，与密码管理器、MFA成本形成对照。

- inherits_from_previous_cn：客户端服务器端的修改少。

- changes_argument_state_cn：给出可部署性的技术机制。

- sets_up_next_cn：客户端修改之简便是本说明的延伸。

- failure_if_removed_cn：成本优势缺乏可验证理由。

- evidence_pointer：Introduction P5 S6

### 39. Introduction P5 S7

- order：39

- locator：Introduction P5 S7

- paraphrase_cn：对现有强度计界面进行的修改从客户端软件角度看简单而直接。

- move_code：PRACTICAL_CONTRIBUTION_MECHANISM

- statement_status：contribution_claim

- why_here_cn：把第一个实践贡献具体化到消息文本层面，暗示仅前端改动。

- inherits_from_previous_cn：无须服务器资源。

- changes_argument_state_cn：实现细节可预期。

- sets_up_next_cn：跨场景（银行 vs 论坛）有效性成为下一个主张。

- failure_if_removed_cn：'简单'或'低成本'均无操作性说明。

- evidence_pointer：Introduction P5 S7

### 40. Introduction P5 S8

- order：40

- locator：Introduction P5 S8

- paraphrase_cn：我们的方法在高安全（如银行）和低安全（如论坛）系统中都能有效刺激用户改善安全行为。

- move_code：GENERALIZABILITY_CLAIM

- statement_status：contribution_claim

- why_here_cn：预告跨场景边界结果，扩大适用性。

- inherits_from_previous_cn：设计已实现。

- changes_argument_state_cn：贡献不只针对高端场景。

- sets_up_next_cn：后续实验室场景分析将验证此宣示。

- failure_if_removed_cn：文章的适用广度无预告。

- evidence_pointer：Introduction P5 S8

### 41. Introduction P6 S1

- order：41

- locator：Introduction P6 S1

- paraphrase_cn：论文其余部分组织如下。

- move_code：ROADMAP_OPENING

- statement_status：method_decision

- why_here_cn：给出阅读路线图。

- inherits_from_previous_cn：已陈述所有贡献。

- changes_argument_state_cn：转向文章导航。

- sets_up_next_cn：按章节展开。

- failure_if_removed_cn：读者对论文结构无预期。

- evidence_pointer：Introduction P6 S1

### 42. Introduction P6 S2

- order：42

- locator：Introduction P6 S2

- paraphrase_cn：Section 2描述概念设计。

- move_code：ROADMAP_ITEM

- statement_status：method_decision

- why_here_cn：告知概念设计在何处。

- inherits_from_previous_cn：路线图开场。

- changes_argument_state_cn：导航正式开始。

- sets_up_next_cn：进入理论→设计阅读动线。

- failure_if_removed_cn：结构预告不完整。

- evidence_pointer：Introduction P6 S2

### 43. Introduction P6 S3

- order：43

- locator：Introduction P6 S3

- paraphrase_cn：概念设计中将先识别支撑强度计心理机制的心理学理论。

- move_code：ROADMAP_ITEM

- statement_status：method_decision

- why_here_cn：预告理论部分先于设计。

- inherits_from_previous_cn：Section 2陈述。

- changes_argument_state_cn：标明理论→设计顺序。

- sets_up_next_cn：让读者能追踪从ELM到三类消息的推导。

- failure_if_removed_cn：理论到设计路径变模糊。

- evidence_pointer：Introduction P6 S3

### 44. Introduction P6 S4

- order：44

- locator：Introduction P6 S4

- paraphrase_cn：然后利用该理论概念性地设计增强强度计。

- move_code：ROADMAP_ITEM

- statement_status：method_decision

- why_here_cn：说明概念设计与理论关系。

- inherits_from_previous_cn：理论识别。

- changes_argument_state_cn：导航覆盖从理论到设计。

- sets_up_next_cn：接着进入实现与评价。

- failure_if_removed_cn：缺少核心设计预告。

- evidence_pointer：Introduction P6 S4

### 45. Introduction P6 S5

- order：45

- locator：Introduction P6 S5

- paraphrase_cn：随后在Section 3描述实现与评价方法。

- move_code：ROADMAP_ITEM

- statement_status：method_decision

- why_here_cn：预告实现机制。

- inherits_from_previous_cn：概念设计已完成。

- changes_argument_state_cn：读者知道制品如何落地。

- sets_up_next_cn：三实验章节有方法论基础。

- failure_if_removed_cn：实现章节丢失预告。

- evidence_pointer：Introduction P6 S5

### 46. Introduction P6 S6

- order：46

- locator：Introduction P6 S6

- paraphrase_cn：之后呈现问卷实验和结果（Section 4）、实验室实验（Section 5）和现场实验（Section 6）。

- move_code：ROADMAP_ITEM

- statement_status：method_decision

- why_here_cn：一一列出研究顺序，展示三阶段证据链。

- inherits_from_previous_cn：实现后评估。

- changes_argument_state_cn：证据结构预告完成。

- sets_up_next_cn：读者按序阅读三个研究。

- failure_if_removed_cn：三研究顺序不明确。

- evidence_pointer：Introduction P6 S6

### 47. Introduction P6 S7

- order：47

- locator：Introduction P6 S7

- paraphrase_cn：最后讨论研究启示并结论（Section 7）。

- move_code：ROADMAP_ITEM

- statement_status：method_decision

- why_here_cn：以讨论收尾。

- inherits_from_previous_cn：三研究完成。

- changes_argument_state_cn：全文导航闭合。

- sets_up_next_cn：结束引言，进入理论和文献。

- failure_if_removed_cn：讨论和贡献部分无预告。

- evidence_pointer：Introduction P6 S7

## 引言逐段图谱

### 1. Introduction P1

- order：1

- locator：Introduction P1

- opening_move_cn：以'密码是主导认证机制'开篇，建立组织技术背景。

- development_move_cn：从'密码重要性'到'专家认为过时'再到'实践反驳'，依次堆叠动机。

- pivot_move_cn：在S6处转向'替代技术本身有意外后果'，把排除路径当作转折。

- closing_move_cn：以'替代技术不可行'收尾，制造第二段Password Strength Meter的出场需要。

- paragraph_job_cn：确立现实紧迫性并排除替代解决方案，把唯一可行路径锁定为说服性技术—密码强度计。

### 2. Introduction P2

- order：2

- locator：Introduction P2

- opening_move_cn：S1从'不可行的替代'回到'聚焦强度计'。

- development_move_cn：S2-S5列三条设计标准：理论驱动、不依赖复杂度政策、低成本可部署。

- pivot_move_cn：无转折；P2整个是设计标准的推进。

- closing_move_cn：以'可广泛部署'收束，使下一段对强度计现状的技术描述成为必需背景。

- paragraph_job_cn：给出本文设计目标与管理约束，使后文理论选择和实现选择都有标准可循。

### 3. Introduction P3

- order：3

- locator：Introduction P3

- opening_move_cn：从'强度计是什么'的背景定义开始，建立对象。

- development_move_cn：由理想功能到现实争议再到弱密码持续的事实，逐步加深文献与现实的落差。

- pivot_move_cn：S6处转向'主流工作集中在算法'，与本文关注呈现组件形成对照。

- closing_move_cn：用算法路线和替代指标清单收尾，使下一段很自然地说'我们不研究这个方面'。

- paragraph_job_cn：描述领域主流研究并指出其集中于算法，为下一段提出'呈现组件'做铺垫。

### 4. Introduction P4

- order：4

- locator：Introduction P4

- opening_move_cn：以'我们补充主流研究，研究呈现组件'打开。

- development_move_cn：用Furnell的发现和black-box现象积累'没有理论指南'的缺口。

- pivot_move_cn：S5处由缺口转到'识别理论'，完成问题→理论转向。

- closing_move_cn：以三证明实验预告和正面结果收尾，制造贡献段的到来。

- paragraph_job_cn：精确界定研究范围，确立理论缺口，并预告设计科学/三阶段证据链方法。

### 5. Introduction P5

- order：5

- locator：Introduction P5

- opening_move_cn：直接声明双重贡献。

- development_move_cn：先是理论：建立互动理论基础并用于改善设计；继而实践：小改动、低成本、跨场景有效。

- pivot_move_cn：S5从理论贡献转向实践贡献。

- closing_move_cn：以跨高/低安全场景有效性收尾，为正文场景设计埋下伏笔。

- paragraph_job_cn：把文章对IS理论和实践的价值一次性讲清，并预告后续证据形态。

### 6. Introduction P6

- order：6

- locator：Introduction P6

- opening_move_cn：以'论文组织如下'开启导航。

- development_move_cn：按已完成的动线逐一列出章节：概念设计→实现→三个实验→讨论。

- pivot_move_cn：无转折，纯结构预告。

- closing_move_cn：以讨论和结论收尾，正式结束引言。

- paragraph_job_cn：提供全文阅读路线图，让读者对理论到多方法证据链有预期。

## 理论到设计逐句图谱

### 1. Section 2.1 P1

- order：1

- locator：Section 2.1 P1

- paraphrase_cn：本部分讨论与呈现组件紧密相关的先前研究。

- move_code：SCOPE

- statement_status：author_inference

- why_here_cn：限定文献综述范围，集中呈现组件而非所有强度计研究。

- inherits_from_previous_cn：引言已经界定呈现组件为研究对象。

- changes_argument_state_cn：文献综述被收纳到具体研究问题下。

- sets_up_next_cn：列出具体视觉刺激文献。

- failure_if_removed_cn：综述范围不明确。

- evidence_pointer：Section 2.1 P1

### 2. Section 2.1 P1 S2

- order：2

- locator：Section 2.1 P1 S2

- paraphrase_cn：对密码强度计的一般综述，引见Golla和Durmuth(2018)。

- move_code：LITERATURE_DELEGATION

- statement_status：prior_literature

- why_here_cn：一句话处理大量一般文献，让本文专注于呈现组件。

- inherits_from_previous_cn：限定范围。

- changes_argument_state_cn：排除一般综述的重复。

- sets_up_next_cn：进入具体视觉线索研究。

- failure_if_removed_cn：一般文献基础不足。

- evidence_pointer：Section 2.1 P1

### 3. Section 2.1 P1 S3

- order：3

- locator：Section 2.1 P1 S3

- paraphrase_cn：Ur等人提出进度条颜色和大小等视觉线索会显著影响用户感知。

- move_code：PRIOR_WORK

- statement_status：prior_literature

- why_here_cn：用第一个代表工作说明呈现组件的已有研究方向。

- inherits_from_previous_cn：综述集中于呈现组件。

- changes_argument_state_cn：呈现组件有先例实证。

- sets_up_next_cn：下一句补充更多视觉刺激类型。

- failure_if_removed_cn：视觉刺激研究链条不完整。

- evidence_pointer：Section 2.1 P1

### 4. Section 2.1 P1 S4

- order：4

- locator：Section 2.1 P1 S4

- paraphrase_cn：Golla等人展示雷达、速度计和跳舞兔子等视觉线索也有效吸引注意力。

- move_code：PRIOR_WORK

- statement_status：prior_literature

- why_here_cn：继续列举视觉刺激谱系，强调'颜色之外'其他视觉元素被测试。

- inherits_from_previous_cn：呈现组件研究。

- changes_argument_state_cn：视觉刺激范围内多样性扩大。

- sets_up_next_cn：表情符号作为第三种例子。

- failure_if_removed_cn：视觉刺激谱系窄化。

- evidence_pointer：Section 2.1 P1

### 5. Section 2.1 P1 S5

- order：5

- locator：Section 2.1 P1 S5

- paraphrase_cn：Furnell等人提出加入表情符号以改善用户注意力。

- move_code：PRIOR_WORK

- statement_status：prior_literature

- why_here_cn：给出视觉刺激的最后一种代表，表明领域内广泛尝试靠感官线索获得注意。

- inherits_from_previous_cn：先前视觉工作。

- changes_argument_state_cn：视觉刺激创作谱系完成。

- sets_up_next_cn：下一句总结所有这些视觉方法的共性证据。

- failure_if_removed_cn：谱系不完整，'视觉驱动'这一标签过载。

- evidence_pointer：Section 2.1 P1

### 6. Section 2.1 P1 S6

- order：6

- locator：Section 2.1 P1 S6

- paraphrase_cn：这些工作一致表明视觉驱动方法在改善密码生成行为方面显著有效。

- move_code：LITERATURE_SYNTHESIS

- statement_status：prior_literature

- why_here_cn：把上述所有工作合并为一个证据：视觉线索有效。

- inherits_from_previous_cn：三类视觉线索研究。

- changes_argument_state_cn：为后续的'但机制不明'设下对照。

- sets_up_next_cn：转折到解释性缺口。

- failure_if_removed_cn：视觉刺激有效性的概括缺失。

- evidence_pointer：Section 2.1 P1

### 7. Section 2.1 P1 S7

- order：7

- locator：Section 2.1 P1 S7

- paraphrase_cn：然而，对其驱动行为变化的底层机制和支撑理论的解释在文献中缺乏。

- move_code：THEORETICAL_GAP

- statement_status：author_inference

- why_here_cn：在承认有效性的同时，立即制造理论缺口，这是全文的枢纽句。

- inherits_from_previous_cn：视觉刺激有效。

- changes_argument_state_cn：从'有效'转为'缺乏解释'。

- sets_up_next_cn：下一句响应方法论呼吁。

- failure_if_removed_cn：引入ELM的全部理由失效。

- evidence_pointer：Section 2.1 P1

### 8. Section 2.1 P1 S8

- order：8

- locator：Section 2.1 P1 S8

- paraphrase_cn：我们回应以理论视角研究用户安全行为的号召，用理论桥梁来填补这一知识缺口。

- move_code：RESPONSE_TO_CALL

- statement_status：author_inference

- why_here_cn：把'理论缺失'转化成本文的具体任务，也显示与IS文献对话。

- inherits_from_previous_cn：文献缺乏理论解释。

- changes_argument_state_cn：文章使命定位为理论性介入。

- sets_up_next_cn：下一节开始引入ELM。

- failure_if_removed_cn：理论引入缺前置任务。

- evidence_pointer：Section 2.1 P1

### 9. Section 2.2 P1

- order：9

- locator：Section 2.2 P1

- paraphrase_cn：强度计本应是说服用户改变行为，所以用ELM作为理论基础。

- move_code：THEORY_INTRO

- statement_status：theory_claim

- why_here_cn：开始理论选择：把强度计定义为说服工具，ELM因此天然适用。

- inherits_from_previous_cn：需要理论解释。

- changes_argument_state_cn：ELM进入论证核心。

- sets_up_next_cn：ELM的核心双路径命题。

- failure_if_removed_cn：所有后续ELM推导失去开始。

- evidence_pointer：Section 2.2 P1

### 10. Section 2.2 P2

- order：10

- locator：Section 2.2 P2

- paraphrase_cn：ELM是双过程理论，描述说服如何导致态度和行为变化。

- move_code：THEORY_PROPOSITION

- statement_status：theory_claim

- why_here_cn：给出ELM的基本定义，为双路径机制提供总纲。

- inherits_from_previous_cn：把强度计与说服关联。

- changes_argument_state_cn：从工具描述进入理论机制。

- sets_up_next_cn：引出外周/中心两条路线。

- failure_if_removed_cn：双路径详细描述没有本体基础。

- evidence_pointer：Section 2.2 P2

### 11. Section 2.2 P3

- order：11

- locator：Section 2.2 P3

- paraphrase_cn：外周路径处理涉及低精细加工，个体被刺激中线索或信息推断影响，不需认知和注意力，导致的态度行为改变肤浅且短暂。

- move_code：THEORY_PROPOSITION

- statement_status：theory_claim

- why_here_cn：定义外周路径的机制和后果，后文将用它分类传统视觉刺激。

- inherits_from_previous_cn：ELM双过程。

- changes_argument_state_cn：外周路径概念可用。

- sets_up_next_cn：定义中心路径作为对照。

- failure_if_removed_cn：传统强度计为何效果有限的解释缺一半。

- evidence_pointer：Section 2.2 P3

### 12. Section 2.2 P4

- order：12

- locator：Section 2.2 P4

- paraphrase_cn：中心路径处理涉及高精细加工，受众仔细认真考虑信息内容，需大量认知和注意力，导致更显著持久的行为改变。

- move_code：THEORY_PROPOSITION

- statement_status：theory_claim

- why_here_cn：定义中心路径，作为设计处方的理论依据。

- inherits_from_previous_cn：外周路径刚定义。

- changes_argument_state_cn：两条路径完整对照，设计原则可推出。

- sets_up_next_cn：下一句把现有视觉刺激归到外周路线。

- failure_if_removed_cn：中心路径机制缺失，'如何改进'无法推导。

- evidence_pointer：Section 2.2 P4

### 13. Section 2.2 P5

- order：13

- locator：Section 2.2 P5

- paraphrase_cn：通过ELM透镜，第2.1节讨论的视觉驱动刺激似乎通过外周路径处理。

- move_code：MECHANISM_CLASSIFICATION

- statement_status：theory_claim

- why_here_cn：把现有文献中的视觉刺激纳入外周路径，为'为什么传统方法效果短暂'提供机制解释。

- inherits_from_previous_cn：两条路径定义。

- changes_argument_state_cn：已有视觉设计被理论重新解释。

- sets_up_next_cn：下一句点明外周路径改变短暂。

- failure_if_removed_cn：文献的机制诊断落空。

- evidence_pointer：Section 2.2 P5

### 14. Section 2.2 P6

- order：14

- locator：Section 2.2 P6

- paraphrase_cn：尽管这些刺激可能有效，但先前工作表明外周路径驱动的改变倾向于轻浮和短暂。

- move_code：MECHANISM_CONSEQUENCE

- statement_status：prior_literature

- why_here_cn：把外周路径理论结论引用为既有共识，与视觉刺激绑定。

- inherits_from_previous_cn：视觉刺激走外周路径。

- changes_argument_state_cn：解释为什么视觉刺激虽有效但效果短暂。

- sets_up_next_cn：用它解释现实中的弱密码持续。

- failure_if_removed_cn：外周路径的性质未应用于现实问题。

- evidence_pointer：Section 2.2 P6

### 15. Section 2.2 P7

- order：15

- locator：Section 2.2 P7

- paraphrase_cn：这可以帮助解释为什么即使视觉线索广泛实现，弱密码问题仍然持续。

- move_code：PHENOMENON_EXPLANATION

- statement_status：author_inference

- why_here_cn：把理论机制用于解释引言中的现实悖论，完成理论对现象的回填。

- inherits_from_previous_cn：外周路径改变短暂。

- changes_argument_state_cn：理论已能解释该领域核心悖论。

- sets_up_next_cn：为'应使用中心路径'提供方向。

- failure_if_removed_cn：理论与实践之间的循环论证边界消失。

- evidence_pointer：Section 2.2 P7

### 16. Section 2.2 P8

- order：16

- locator：Section 2.2 P8

- paraphrase_cn：IS文献显示中心路径类消息在技术接受和电子病历采纳等情境中显著有效。

- move_code：PRECEDENT_FOR_CENTRAL_ROUTE

- statement_status：prior_literature

- why_here_cn：证明中心路径消息在IS有效，为把该方法迁移到强度计提供了先例。

- inherits_from_previous_cn：中心路径更持久。

- changes_argument_state_cn：中心路径有IS成败证据。

- sets_up_next_cn：指出还没有人用于强度计。

- failure_if_removed_cn：中心路径的实证可行性缺乏IS背书。

- evidence_pointer：Section 2.2 P8

### 17. Section 2.2 P9

- order：17

- locator：Section 2.2 P9

- paraphrase_cn：但几乎没有先前工作用可能通过中心路径处理的刺激来增强强度计。

- move_code：GAP_AT_ARTIFACT

- statement_status：author_inference

- why_here_cn：把IS普遍证据与强度计具体缺口对接。

- inherits_from_previous_cn：中心路径在其他领域有效。

- changes_argument_state_cn：缺口被定位到强度计量身。

- sets_up_next_cn：下一句提出本文的设计任务。

- failure_if_removed_cn：文章创新点无法明确，设计动机弱。

- evidence_pointer：Section 2.2 P9

### 18. Section 2.2 P10

- order：18

- locator：Section 2.2 P10

- paraphrase_cn：因此，我们设计、开发并验证一个旨在通过ELM中心路线说服用户的增强强度计。

- move_code：STUDY_PURPOSE

- statement_status：design_decision

- why_here_cn：把前述理论缺口和中心路径先例汇合成文章任务宣言。

- inherits_from_previous_cn：缺口与先例。

- changes_argument_state_cn：明确设计原则：中心路径刺激。

- sets_up_next_cn：下一节给出具体概念设计。

- failure_if_removed_cn：理论章节与设计章节脱节。

- evidence_pointer：Section 2.2 P10

### 19. Section 2.3 P1

- order：19

- locator：Section 2.3 P1

- paraphrase_cn：我们遵循设计科学文献，用理论驱动设计原则来概念化设计。

- move_code：METHODOLOGY

- statement_status：method_decision

- why_here_cn：将设计置于设计科学范式，赋予设计方法合法性。

- inherits_from_previous_cn：需要具体设计原则。

- changes_argument_state_cn：理论向设计转化开始。

- sets_up_next_cn：本章将引Gregor的Type V理论。

- failure_if_removed_cn：设计原则没有所属方法论。

- evidence_pointer：Section 2.3 P1

### 20. Section 2.3 P2

- order：20

- locator：Section 2.3 P2

- paraphrase_cn：我们首先呈现Gregor(2006)定义的'design and action'的Type V理论。

- move_code：THEORY_SOURCE

- statement_status：theory_claim

- why_here_cn：明确使用Gregor的Type V，为设计行动提供理论合法性。

- inherits_from_previous_cn：设计科学方法。

- changes_argument_state_cn：设计将被视为理论输出。

- sets_up_next_cn：该理论提供构建制品的处方。

- failure_if_removed_cn：设计科学理论基础缺失。

- evidence_pointer：Section 2.3 P2

### 21. Section 2.3 P3

- order：21

- locator：Section 2.3 P3

- paraphrase_cn：这种理论本质上提供构建制品的明确处方。

- move_code：THEORY_APPLICATION

- statement_status：theory_claim

- why_here_cn：说明Type V能提供'设计处方'，为后续三消息的选择定了逻辑框架。

- inherits_from_previous_cn：Type V定义。

- changes_argument_state_cn：设计处方成为合法知识形式。

- sets_up_next_cn：结合ELM给出处方核心。

- failure_if_removed_cn：设计处方逻辑无用武之地。

- evidence_pointer：Section 2.3 P3

### 22. Section 2.3 P4

- order：22

- locator：Section 2.3 P4

- paraphrase_cn：回想ELM：当说服唤起受众认知好奇时，倾向于中心路径处理。

- move_code：THEORY_RECALL

- statement_status：theory_claim

- why_here_cn：重新调用ELM，把认知好奇指定为中心路径触发器。

- inherits_from_previous_cn：设计处方框架。

- changes_argument_state_cn：中心路径的实现条件确定：引发认知好奇。

- sets_up_next_cn：得出一条关键设计处方。

- failure_if_removed_cn：设计处方缺少具体操作性入口。

- evidence_pointer：Section 2.3 P4

### 23. Section 2.3 P5

- order：23

- locator：Section 2.3 P5

- paraphrase_cn：因此关键设计元素是找出并加入可能经中心路径处理的刺激，如激发思考的消息。

- move_code：DESIGN_PRESCRIPTION

- statement_status：theory_claim

- why_here_cn：这是全文理论→设计的连接句：ELM变成本文设计准则。

- inherits_from_previous_cn：认知好奇触发中心路径。

- changes_argument_state_cn：设计处方确立。

- sets_up_next_cn：为接下来选择三类消息做依据。

- failure_if_removed_cn：三类消息的来源失去统一理由。

- evidence_pointer：Section 2.3 P5

### 24. Section 2.3 P6

- order：24

- locator：Section 2.3 P6

- paraphrase_cn：为此，我们调研使用ELM提出或解释说服消息有效的文献。

- move_code：LITERATURE_SURVEY_INTRO

- statement_status：method_decision

- why_here_cn：从设计处方转向从中层文献找消息类型候选。

- inherits_from_previous_cn：需要找到中心路径刺激。

- changes_argument_state_cn：候选消息将从文献证据中选取。

- sets_up_next_cn：依次介绍恐惧诉求、同伴比较、共同纽带。

- failure_if_removed_cn：三类消息的选取显得任意。

- evidence_pointer：Section 2.3 P6

### 25. Section 2.3 P7

- order：25

- locator：Section 2.3 P7

- paraphrase_cn：第一类常被使用的正是恐惧诉求消息。

- move_code：DESIGN_FEATURE_INTRO

- statement_status：design_decision

- why_here_cn：引入第一种消息类别。

- inherits_from_previous_cn：设计处方需要刺激。

- changes_argument_state_cn：消息类型集合开始。

- sets_up_next_cn：后文以文献证明恐惧诉求有效性。

- failure_if_removed_cn：后文的Time处理失去来源。

- evidence_pointer：Section 2.3 P7

### 26. Section 2.3 P8

- order：26

- locator：Section 2.3 P8

- paraphrase_cn：恐惧诉求消息傾向激发认知注意(Ruiter et al. 2001)。

- move_code：THEORY_EVIDENCE

- statement_status：prior_literature

- why_here_cn：把恐惧诉求与中心路径触发条件（认知注意）连接。

- inherits_from_previous_cn：恐惧诉求类别。

- changes_argument_state_cn：恐惧诉求被纳入中心路径逻辑。

- sets_up_next_cn：给恐惧诉求应用的各类情境示例。

- failure_if_removed_cn：恐惧诉求被选为刺激的理由不足。

- evidence_pointer：Section 2.3 P8

### 27. Section 2.3 P9

- order：27

- locator：Section 2.3 P9

- paraphrase_cn：恐惧诉求被用于赌博、降低传染病风险等情境。

- move_code：PRIOR_USES

- statement_status：prior_literature

- why_here_cn：通过跨域使用案例，说明恐惧诉求是被验证的说服工具。

- inherits_from_previous_cn：恐惧诉求助认知注意。

- changes_argument_state_cn：恐惧诉求普遍适用性增强。

- sets_up_next_cn：指向信息安全领域用法。

- failure_if_removed_cn：恐惧诉求的普适性序列缺位。

- evidence_pointer：Section 2.3 P9

### 28. Section 2.3 P10

- order：28

- locator：Section 2.3 P10

- paraphrase_cn：恐惧诉求也常用于信息安全，影响个体和组织用户行为。

- move_code：IS_CONTEXT_EVIDENCE

- statement_status：prior_literature

- why_here_cn：在IS安全情境中找到恐惧诉求先例，使迁移到强度计更自然。

- inherits_from_previous_cn：恐惧诉求跨域有效。

- changes_argument_state_cn：IS领域有扎实先例。

- sets_up_next_cn：由此明确将恐惧诉求用作第一类消息。

- failure_if_removed_cn：恐惧诉求在IS安全缺先例支持。

- evidence_pointer：Section 2.3 P10

### 29. Section 2.3 P11

- order：29

- locator：Section 2.3 P11

- paraphrase_cn：因此我们提议以恐惧诉求作为第一类可加入强度计的消息。

- move_code：DESIGN_FEATURE_DECISION

- statement_status：design_decision

- why_here_cn：由文献推导出的第一个具体设计决定。

- inherits_from_previous_cn：IS安全前例与认知激发机制。

- changes_argument_state_cn：第一类消息进入设计。

- sets_up_next_cn：下一段处理同伴比较。

- failure_if_removed_cn：Time处理成为无依据设计。

- evidence_pointer：Section 2.3 P11

### 30. Section 2.3 P12

- order：30

- locator：Section 2.3 P12

- paraphrase_cn：第二，一些工作用ELM解释同伴压力的有效性。

- move_code：DESIGN_FEATURE_INTRO

- statement_status：prior_literature

- why_here_cn：引入第二种消息类别：同伴压力/同伴比较。

- inherits_from_previous_cn：第一类消息已定。

- changes_argument_state_cn：候选集合将增加第二类。

- sets_up_next_cn：详述同伴压力的认知效应。

- failure_if_removed_cn：Rank处理来源缺失。

- evidence_pointer：Section 2.3 P12

### 31. Section 2.3 P13

- order：31

- locator：Section 2.3 P13

- paraphrase_cn：同伴压力在激发认知思维中起重要作用，尤其是称为同伴比较的间接类型。

- move_code：MECHANISM

- statement_status：theory_claim

- why_here_cn：将同伴比较与中心路径认知唤起连接。

- inherits_from_previous_cn：同伴压力。

- changes_argument_state_cn：同伴比较被指定为认知激发器。

- sets_up_next_cn：后续以具体实证支持。

- failure_if_removed_cn：Rank消息的认知机制未被说明。

- evidence_pointer：Section 2.3 P13

### 32. Section 2.3 P14

- order：32

- locator：Section 2.3 P14

- paraphrase_cn：Petty等人证明同伴比较消息可用于在药物滥用预防中说服。

- move_code：PRIOR_USES

- statement_status：prior_literature

- why_here_cn：给出同伴比较的经典实证先例。

- inherits_from_previous_cn：同伴比较激发认知。

- changes_argument_state_cn：同伴比较有行为改变证据。

- sets_up_next_cn：继续补充训练场景。

- failure_if_removed_cn：同伴比较经验效度不足。

- evidence_pointer：Section 2.3 P14

### 33. Section 2.3 P15

- order：33

- locator：Section 2.3 P15

- paraphrase_cn：该消息在团体训练中也已被证明能有效激励个体。

- move_code：PRIOR_USES

- statement_status：prior_literature

- why_here_cn：补充更多情境的同伴比较有效性。

- inherits_from_previous_cn：药物滥用预防。

- changes_argument_state_cn：同伴比较适用范围扩大。

- sets_up_next_cn：指向信息安全相关应用。

- failure_if_removed_cn：同伴比较的先例谱系较短。

- evidence_pointer：Section 2.3 P15

### 34. Section 2.3 P16

- order：34

- locator：Section 2.3 P16

- paraphrase_cn：在信息安全情境中，同伴比较也常用于隐私管理和安全培训。

- move_code：IS_CONTEXT_EVIDENCE

- statement_status：prior_literature

- why_here_cn：在IS安全情境中找出同伴比较应用，支持迁移强度计。

- inherits_from_previous_cn：同伴比较跨域有效。

- changes_argument_state_cn：IS环境同类先例出现。

- sets_up_next_cn：确定为第二类消息。

- failure_if_removed_cn：Rank在IS应用支持薄弱。

- evidence_pointer：Section 2.3 P16

### 35. Section 2.3 P17

- order：35

- locator：Section 2.3 P17

- paraphrase_cn：因此我们建议将同伴比较作为第二类消息。

- move_code：DESIGN_FEATURE_DECISION

- statement_status：design_decision

- why_here_cn：从文献推导出Rank处理来源。

- inherits_from_previous_cn：IS先例与认知机制。

- changes_argument_state_cn：第二类消息定稿。

- sets_up_next_cn：第三类共同纽带。

- failure_if_removed_cn：Rank处理无理论依据。

- evidence_pointer：Section 2.3 P17

### 36. Section 2.3 P18

- order：36

- locator：Section 2.3 P18

- paraphrase_cn：第三，过去文献用ELM理论化共同纽带在激励或说服中的正面影响。

- move_code：DESIGN_FEATURE_INTRO

- statement_status：prior_literature

- why_here_cn：引入第三种消息类别：共同纽带。

- inherits_from_previous_cn：第二类已定。

- changes_argument_state_cn：候选集合获得第三类。

- sets_up_next_cn：详述共同纽带认知机制。

- failure_if_removed_cn：Probability处理来源缺失。

- evidence_pointer：Section 2.3 P18

### 37. Section 2.3 P19

- order：37

- locator：Section 2.3 P19

- paraphrase_cn：即共同纽带相关消息倾向于诱导认知过程(Postmes和Spears 2000)。

- move_code：MECHANISM

- statement_status：theory_claim

- why_here_cn：连接共同纽带与中心路径认知唤起。

- inherits_from_previous_cn：共同纽带类别。

- changes_argument_state_cn：共同纽带被纳入中心路径触发器。

- sets_up_next_cn：举具体网站设计和社会媒体研究。

- failure_if_removed_cn：共同纽带作为刺激的机制不成立。

- evidence_pointer：Section 2.3 P19

### 38. Section 2.3 P20

- order：38

- locator：Section 2.3 P20

- paraphrase_cn：Cyr等人用ELM研究共同纽带在网站设计中的说服力；Chung和Han展示其在社交媒体游客说服中的关系。

- move_code：PRIOR_USES

- statement_status：prior_literature

- why_here_cn：列举共同纽带在两个数字化情境中的成功应用。

- inherits_from_previous_cn：共同纽带诱导认知。

- changes_argument_state_cn：共同纽带有效性的证据积累。

- sets_up_next_cn：转回密码安全情境。

- failure_if_removed_cn：共同纽带经验效度不足。

- evidence_pointer：Section 2.3 P20

### 39. Section 2.3 P21

- order：39

- locator：Section 2.3 P21

- paraphrase_cn：在信息安全尤其是密码安全中，常用密码更容易被猜中，因此共同纽带消息有很大影响认知潜力。

- move_code：MECHANISM_IN_PASSWORD_CONTEXT

- statement_status：author_inference

- why_here_cn：把共同纽带概念转用到密码重复率语境，为设计Probability消息铺垫。

- inherits_from_previous_cn：共同纽带认知机制。

- changes_argument_state_cn：密码重复成为共同纽带微观载体。

- sets_up_next_cn：提出第三类消息决定。

- failure_if_removed_cn：Probability消息机制无从表达。

- evidence_pointer：Section 2.3 P21

### 40. Section 2.3 P22

- order：40

- locator：Section 2.3 P22

- paraphrase_cn：因此，我们建议将共同纽带作为本研究中的第三类消息。

- move_code：DESIGN_FEATURE_DECISION

- statement_status：design_decision

- why_here_cn：第三类设计决定完成。

- inherits_from_previous_cn：密码重复作为共同纽带。

- changes_argument_state_cn：三类消息全部确定。

- sets_up_next_cn：进入实现阶段。

- failure_if_removed_cn：三类消息构造缺完整性。

- evidence_pointer：Section 2.3 P22

### 41. Section 2.3 P23

- order：41

- locator：Section 2.3 P23

- paraphrase_cn：接下来，我们把概念设计转化为实际实现，开发'情境化制品实现'。

- move_code：IMPLEMENTATION_TRANSITION

- statement_status：method_decision

- why_here_cn：理论章节收尾，告知读者从概念走向实现。

- inherits_from_previous_cn：三类消息已构造。

- changes_argument_state_cn：设计阶段结束，实现开始。

- sets_up_next_cn：后文将连接实验。

- failure_if_removed_cn：理论与实现脱节。

- evidence_pointer：Section 2.3 P23

### 42. Section 2.3 P24

- order：42

- locator：Section 2.3 P24

- paraphrase_cn：之后通过一系列实验评估，并把结果连回设计原则和ELM。

- move_code：EVALUATION_PREVIEW

- statement_status：method_decision

- why_here_cn：预告评价闭环，说明实验不是孤立测试而是理论验证。

- inherits_from_previous_cn：实现完成。

- changes_argument_state_cn：证实策略为三实验。

- sets_up_next_cn：下面分别给出proof of concept、value、use。

- failure_if_removed_cn：实验与理论间缺乏桥接。

- evidence_pointer：Section 2.3 P24

### 43. Section 2.3 P25

- order：43

- locator：Section 2.3 P25

- paraphrase_cn：第一个实验作为概念证明，用问卷评估受众是否仔细考虑消息。

- move_code：STUDY_PREVIEW

- statement_status：method_decision

- why_here_cn：安排第一阶段的作用。

- inherits_from_previous_cn：三阶段评价。

- changes_argument_state_cn：Study 1任务被定义为概念证明。

- sets_up_next_cn：引向Study 2行为检验。

- failure_if_removed_cn：Survey在设计链中的位置不清。

- evidence_pointer：Section 2.3 P25

### 44. Section 2.3 P26

- order：44

- locator：Section 2.3 P26

- paraphrase_cn：其次，价值证明在受控实验室中检查用户是否改变行为。

- move_code：STUDY_PREVIEW

- statement_status：method_decision

- why_here_cn：安排第二阶段作用。

- inherits_from_previous_cn：概念证明后的自然步骤。

- changes_argument_state_cn：Study 2任务被定义为价值证明。

- sets_up_next_cn：最后现场应用证明。

- failure_if_removed_cn：实验室实验在证据链中的角色不清。

- evidence_pointer：Section 2.3 P26

### 45. Section 2.3 P27

- order：45

- locator：Section 2.3 P27

- paraphrase_cn：最后，通过在外场实施完成应用证明。

- move_code：STUDY_PREVIEW

- statement_status：method_decision

- why_here_cn：安排第三阶段作用。

- inherits_from_previous_cn：前两阶段结果。

- changes_argument_state_cn：Study 3任务被定义为应用证明。

- sets_up_next_cn：结束理论→评价的预告并进入下一节实现细节。

- failure_if_removed_cn：现场实验目的不明。

- evidence_pointer：Section 2.3 P27

## 制品设计理由逐句图谱

### 1. Section 3.1 P1

- order：1

- locator：Section 3.1 P1

- paraphrase_cn：我们描述作为基线的强度计和密码强度如何计算。

- move_code：METHOD_SCOPE

- statement_status：method_decision

- why_here_cn：先定义基线，让后续所有处理被理解为对基线的一种添加。

- inherits_from_previous_cn：概念设计已定。

- changes_argument_state_cn：制品实现章节开始。

- sets_up_next_cn：选择具体强度模型。

- failure_if_removed_cn：三实验缺乏共同对照。

- evidence_pointer：Section 3.1 P1

### 2. Section 3.1 P2

- order：2

- locator：Section 3.1 P2

- paraphrase_cn：密码强度有很多测量方式，没有行业或学术标准。

- move_code：METHOD_CONSTRAINT

- statement_status：fact

- why_here_cn：承认测量任意性，为选择某一模型提供理由。

- inherits_from_previous_cn：如何计算强度。

- changes_argument_state_cn：建立选型必要性。

- sets_up_next_cn：引出backoff Markov模型。

- failure_if_removed_cn：模型选择显得专断。

- evidence_pointer：Section 3.1 P2

### 3. Section 3.1 P3

- order：3

- locator：Section 3.1 P3

- paraphrase_cn：我们采用backoff Markov模型，它被一致认为最适合这类实验。

- move_code：MODEL_SELECTION

- statement_status：method_decision

- why_here_cn：在一个无标准的小领域，引用Ma等与Ur等给出最佳可用模型。

- inherits_from_previous_cn：没有行业标准。

- changes_argument_state_cn：强度度量被固定为backoff Markov。

- sets_up_next_cn：给出该模型具体变体。

- failure_if_removed_cn：后文所有强度数值定义缺失。

- evidence_pointer：Section 3.1 P3

### 4. Section 3.1 P4

- order：4

- locator：Section 3.1 P4

- paraphrase_cn：我们用带端符号归一化的Ma等(2014)的backoff Markov模型。

- move_code：MODEL_SPECIFICATION

- statement_status：method_decision

- why_here_cn：精确到模型变体，保证可复现性和一致性。

- inherits_from_previous_cn：选定模型。

- changes_argument_state_cn：核心算法细节落地。

- sets_up_next_cn：说明该模型如何用机器学习预测概率。

- failure_if_removed_cn：复现性和内部有效性受损。

- evidence_pointer：Section 3.1 P4

### 5. Section 3.1 P5

- order：5

- locator：Section 3.1 P5

- paraphrase_cn：模型用机器学习预测给定密码被选择的概率。

- move_code：MODEL_MECHANISM

- statement_status：fact

- why_here_cn：简单解释模型工作原理，使后面所有消息皆可基于’概率’计算。

- inherits_from_previous_cn：模型已指定。

- changes_argument_state_cn：概率成为全文标准化基础。

- sets_up_next_cn：强调一致性比较。

- failure_if_removed_cn：三条消息的数值基础难理解。

- evidence_pointer：Section 3.1 P5

### 6. Section 3.1 P6

- order：6

- locator：Section 3.1 P6

- paraphrase_cn：backoff Markov模型让我们在不同实验处理间保持一致的强度比较。

- move_code：CONSISTENCY_RATIONALE

- statement_status：method_decision

- why_here_cn：把模型选择与实验设计核心需求绑定：跨处理公平。

- inherits_from_previous_cn：概率模型统一。

- changes_argument_state_cn：内部有效性得到技术保障。

- sets_up_next_cn：为选择训练数据做理由。

- failure_if_removed_cn：跨处理可比性主张缺乏基础。

- evidence_pointer：Section 3.1 P6

### 7. Section 3.1 P7

- order：7

- locator：Section 3.1 P7

- paraphrase_cn：为确保真实性和提供基线，我们用RockYou训练，包含超过3200万明文密码，被视为最佳之一。

- move_code：TRAINING_DATA_SELECTION

- statement_status：method_decision

- why_here_cn：选择训练数据以确保模型贴近现实；RockYou规模和信誉被提及。

- inherits_from_previous_cn：需要使用概率模型。

- changes_argument_state_cn：强度模型对现实弱密码敏感。

- sets_up_next_cn：补充训练数据细节。

- failure_if_removed_cn：强度计算真实性受到质疑。

- evidence_pointer：Section 3.1 P7

### 8. Section 3.1 P8

- order：8

- locator：Section 3.1 P8

- paraphrase_cn：我们使用SkullSecurity提供的RockYou列表，仅含密码。

- move_code：DATA_DETAIL

- statement_status：method_decision

- why_here_cn：提升复现性，明确版本与去标识化。

- inherits_from_previous_cn：RockYou选择。

- changes_argument_state_cn：数据来源精确。

- sets_up_next_cn：进入基线强度计显示设计。

- failure_if_removed_cn：训练数据来源不透明。

- evidence_pointer：Section 3.1 P8

### 9. Section 3.1 P9

- order：9

- locator：Section 3.1 P9

- paraphrase_cn：基线强度计显示强度标签，这是许多主流网站的标准做法。

- move_code：BASELINE_DEFINITION

- statement_status：design_decision

- why_here_cn：定义对照组：只显示标签，让它可以代表大量现实网站。

- inherits_from_previous_cn：强度模型已定。

- changes_argument_state_cn：对照组操作化完成。

- sets_up_next_cn：给出弱中强标签定义。

- failure_if_removed_cn：对照条件不具体。

- evidence_pointer：Section 3.1 P9

### 10. Section 3.1 P10

- order：10

- locator：Section 3.1 P10

- paraphrase_cn：强度计根据模型显示弱、中、强之一。

- move_code：LABEL_DESIGN

- statement_status：design_decision

- why_here_cn：落实标签分级，并把所有处理共用的显示固定下来。

- inherits_from_previous_cn：基线显示标签。

- changes_argument_state_cn：标签成为四组公共部分。

- sets_up_next_cn：需要定义阈值。

- failure_if_removed_cn：等级划分不明。

- evidence_pointer：Section 3.1 P10

### 11. Section 3.1 P11

- order：11

- locator：Section 3.1 P11

- paraphrase_cn：概率位于最弱30万以内即'弱'，30万至500万为'中'，之外为'强'。

- move_code：THRESHOLD_OPERATION

- statement_status：design_decision

- why_here_cn：给出阈值操作性定义，使后文对'弱密码'的消息示例可与模型对接。

- inherits_from_previous_cn：弱中强标签。

- changes_argument_state_cn：标签具备可计算定义。

- sets_up_next_cn：承认阈值有文献依据。

- failure_if_removed_cn：标签失去量化基础。

- evidence_pointer：Section 3.1 P11

### 12. Section 3.1 P12

- order：12

- locator：Section 3.1 P12

- paraphrase_cn：阈值基于先前密码强度研究指南选择。

- move_code：THRESHOLD_RATIONALE

- statement_status：prior_literature

- why_here_cn：防止阈值显得任意。

- inherits_from_previous_cn：阈值已定义。

- changes_argument_state_cn：阈值得到领域惯例支持。

- sets_up_next_cn：强调一致性。

- failure_if_removed_cn：标签从阈值争议暴露。

- evidence_pointer：Section 3.1 P12

### 13. Section 3.1 P13

- order：13

- locator：Section 3.1 P13

- paraphrase_cn：这些阈值在所有强度计类型中总相同。

- move_code：CONTROL_ACROSS_TREATMENTS

- statement_status：design_decision

- why_here_cn：强化'唯一变化是消息'这一实验设计关键。

- inherits_from_previous_cn：阈值选择。

- changes_argument_state_cn：所有处理共享公共计算内核。

- sets_up_next_cn：后续消息仅在显示层变化。

- failure_if_removed_cn：处理差异可能被误归因于强度显示不同。

- evidence_pointer：Section 3.1 P13

### 14. Section 3.1 P14

- order：14

- locator：Section 3.1 P14

- paraphrase_cn：当用户将光标移出输入框后，计算并显示强度和警告消息。

- move_code：TRIGGER_DESIGN

- statement_status：design_decision

- why_here_cn：决定消息显示时机，使用户在提交前看到反馈。

- inherits_from_previous_cn：消息设计。

- changes_argument_state_cn：交互流程确定。

- sets_up_next_cn：给出技术实现（focusout事件）。

- failure_if_removed_cn：消息显示时机不明确，行为指标无法定义。

- evidence_pointer：Section 3.1 P14

### 15. Section 3.2 P1-P2

- order：15

- locator：Section 3.2 P1-P2

- paraphrase_cn：恐惧诉求有多种机制，其一为对威胁的感知易感性和脆弱性。

- move_code：MECHANISM_CHOICE

- statement_status：theory_claim

- why_here_cn：从恐惧诉求理论中选择脆弱性/易感性作为Time消息要触发的机制。

- inherits_from_previous_cn：恐惧诉求作为第一类消息。

- changes_argument_state_cn：Time处理具备明确心理维度。

- sets_up_next_cn：说明如何把威胁易感性嵌入消息。

- failure_if_removed_cn：Time消息的设计意图失去理论支撑。

- evidence_pointer：Section 3.2 P1-P2

### 16. Section 3.2 P3

- order：16

- locator：Section 3.2 P3

- paraphrase_cn：我们把恐惧诉求纳入警告消息反馈。

- move_code：DESIGN_IMPLEMENTATION

- statement_status：design_decision

- why_here_cn：具体设计决定：恐惧诉求以警告消息文本呈现。

- inherits_from_previous_cn：脆弱性机制。

- changes_argument_state_cn：Time处理操作化开始。

- sets_up_next_cn：引用恐惧诉求构成要素。

- failure_if_removed_cn：Time处理未成形。

- evidence_pointer：Section 3.2 P3

### 17. Section 3.2 P4

- order：17

- locator：Section 3.2 P4

- paraphrase_cn：恐惧诉求包含威胁的严重性和易感性再加减少威胁能力(Johnston和Warkentin 2010)。

- move_code：THEORETICAL_COMPOSITION

- statement_status：theory_claim

- why_here_cn：用权威定义确保消息至少包含严重性/易感性的成分。

- inherits_from_previous_cn：恐惧诉求纳入消息。

- changes_argument_state_cn：Time消息的内容结构有理论标准。

- sets_up_next_cn：决定消息的具体计算（破解时间）。

- failure_if_removed_cn：Time消息成分缺乏合法性。

- evidence_pointer：Section 3.2 P4

### 18. Section 3.2 P5

- order：18

- locator：Section 3.2 P5

- paraphrase_cn：设计显示按100次/秒攻击假设估计的破解输入密码所需平均时间。

- move_code：MESSAGE_CALCULATION

- statement_status：design_decision

- why_here_cn：把理论机制转成可计算消息：用破解时间激活易感性。

- inherits_from_previous_cn：恐惧诉求构成。

- changes_argument_state_cn：Time消息数值可行性。

- sets_up_next_cn：给出具体弱密码示例。

- failure_if_removed_cn：Time消息只是概念无计算逻辑。

- evidence_pointer：Section 3.2 P5

### 19. Section 3.2 P6

- order：19

- locator：Section 3.2 P6

- paraphrase_cn：弱密码例子：'预计在100次/秒攻击下需10秒破解'。

- move_code：EXAMPLE

- statement_status：design_decision

- why_here_cn：示例让读者能直观看到消息形态，也是Survey中使用截图的基础。

- inherits_from_previous_cn：破解时间计算。

- changes_argument_state_cn：Time消息的具体文本被固定。

- sets_up_next_cn：解释为何短时间唤起易感性。

- failure_if_removed_cn：消息可部署版本缺位。

- evidence_pointer：Section 3.2 P6

### 20. Section 3.2 P7-P8

- order：20

- locator：Section 3.2 P7-P8

- paraphrase_cn：显示的时间唤起对脆弱性的感知，短时间会激发恐惧诉求进而促使用户生成更强密码。

- move_code：MECHANISM_EXPLANATION

- statement_status：theory_claim

- why_here_cn：解释消息机制，说明为什么'短破解时间'能让用户更敏感。

- inherits_from_previous_cn：示例消息。

- changes_argument_state_cn：解开Time消息的因果链。

- sets_up_next_cn：为Study 1中Time组预期结果提供预期。

- failure_if_removed_cn：Time处理的结果预测缺乏机制。

- evidence_pointer：Section 3.2 P7-P8

### 21. Section 3.3 P1

- order：21

- locator：Section 3.3 P1

- paraphrase_cn：先前ELM相关研究表明同伴比较信息说服用户在行为上显著改变，因此考虑使用同伴比较设计。

- move_code：MECHANISM_CHOICE

- statement_status：prior_literature

- why_here_cn：给Rank处理提供理论先例和有效性先例。

- inherits_from_previous_cn：同伴比较为第二类消息。

- changes_argument_state_cn：Rank处理具备说理基础。

- sets_up_next_cn：解释同伴比较如何形成压力。

- failure_if_removed_cn：Rank设计失去理论依托。

- evidence_pointer：Section 3.3 P1

### 22. Section 3.3 P2-P3

- order：22

- locator：Section 3.3 P2-P3

- paraphrase_cn：同伴比较可来自同伴数据展示和群体情境中的自我意识；这种比较产生的压力表现为用户采取行动改善密码。

- move_code：MECHANISM_EXPLANATION

- statement_status：theory_claim

- why_here_cn：说明同伴比较的压力如何在心理上转化为行动，并把行为改善对象（密码）绑定到消息设计。

- inherits_from_previous_cn：同伴比较先例。

- changes_argument_state_cn：Rank消息的因果机制被具体化。

- sets_up_next_cn：设计排名消息的计算过程。

- failure_if_removed_cn：Rank为什么改变行为的解释缺失。

- evidence_pointer：Section 3.3 P2-P3

### 23. Section 3.3 P4

- order：23

- locator：Section 3.3 P4

- paraphrase_cn：设计的强度计包含警告消息，显示与隐含排行榜相比的密码排名。

- move_code：DESIGN_IMPLEMENTATION

- statement_status：design_decision

- why_here_cn：决定Rank以排名文本形式呈现。

- inherits_from_previous_cn：同伴比较机制。

- changes_argument_state_cn：Rank处理内容明确。

- sets_up_next_cn：详述排名如何从模型计算。

- failure_if_removed_cn：Rank消息未成形。

- evidence_pointer：Section 3.3 P4

### 24. Section 3.3 P5-P9

- order：24

- locator：Section 3.3 P5-P9

- paraphrase_cn：排名由生成并排序概率密码列表得出，输入密码匹配最近排名概率对并向上取整到一有效数字。

- move_code：MESSAGE_CALCULATION

- statement_status：method_decision

- why_here_cn：说明排名计算的算法，确保消息不是随意编出来的。

- inherits_from_previous_cn：Rank消息决定。

- changes_argument_state_cn：Rank具备计算公式。

- sets_up_next_cn：呈现弱密码示例。

- failure_if_removed_cn：Rank数值无法复现。

- evidence_pointer：Section 3.3 P5-P9

### 25. Section 3.3 P10

- order：25

- locator：Section 3.3 P10

- paraphrase_cn：弱密码例子：'估计你选择的密码是300个最弱密码之一'。

- move_code：EXAMPLE

- statement_status：design_decision

- why_here_cn：具体示例使读者理解Rank消息的形式。

- inherits_from_previous_cn：排名计算。

- changes_argument_state_cn：Rank消息文本固定。

- sets_up_next_cn：进入Probability设计。

- failure_if_removed_cn：Rank可部署消息缺位。

- evidence_pointer：Section 3.3 P10

### 26. Section 3.4 P1-P4

- order：26

- locator：Section 3.4 P1-P4

- paraphrase_cn：共同纽带在ELM相关研究中能有效说服，在风险情境中影响决策；密码上下文中显示概率可沟通风险，若密码与已有密码'纽带'强则用户风险高。

- move_code：MECHANISM_CHOICE

- statement_status：theory_claim

- why_here_cn：为Probability消息解释共同纽带如何翻译为密码重复概率和风险感知。

- inherits_from_previous_cn：共同纽带为第三类消息。

- changes_argument_state_cn：Probability的认知机制（重复概率→风险）成立。

- sets_up_next_cn：确定要显示什么内容。

- failure_if_removed_cn：Probability消息缺少心理机制。

- evidence_pointer：Section 3.4 P1-P4

### 27. Section 3.4 P5

- order：27

- locator：Section 3.4 P5

- paraphrase_cn：设计在警告消息中显示输入密码的计算强度以及估计的使用相同密码的账户数。

- move_code：DESIGN_IMPLEMENTATION

- statement_status：design_decision

- why_here_cn：把共同纽带机制转成'相同密码账户数'这一可见数字。

- inherits_from_previous_cn：重复概率机制。

- changes_argument_state_cn：Probability消息内容确定。

- sets_up_next_cn：给出示例文本。

- failure_if_removed_cn：Probability消息数值来源未定。

- evidence_pointer：Section 3.4 P5

### 28. Section 3.4 P6

- order：28

- locator：Section 3.4 P6

- paraphrase_cn：似然示例：'在10亿账户中，大约有10,000,000个其他账户与你有相同密码'。

- move_code：EXAMPLE

- statement_status：design_decision

- why_here_cn：给出可理解示例，体现计算的规模感和恐惧/警觉功能。

- inherits_from_previous_cn：相同账户数计算。

- changes_argument_state_cn：Probability消息文本固定。

- sets_up_next_cn：进入评价方法部分。

- failure_if_removed_cn：Probability可部署版本缺位。

- evidence_pointer：Section 3.4 P6

### 29. Section 3.5 P1

- order：29

- locator：Section 3.5 P1

- paraphrase_cn：评价密码生成行为性能有挑战，因为行为动态复杂。

- move_code：EVALUATION_RATIONALE

- statement_status：author_inference

- why_here_cn：为多方法研究提供理由：行为复杂导致单方法不足。

- inherits_from_previous_cn：三项实现已完成。

- changes_argument_state_cn：评价方法将采用多方法设计。

- sets_up_next_cn：提出三方法互补原则。

- failure_if_removed_cn：为什么用三研究而非单研究无法解释。

- evidence_pointer：Section 3.5 P1

### 30. Section 3.5 P2

- order：30

- locator：Section 3.5 P2

- paraphrase_cn：我们用多方法，发展三个互补的独立定量研究。

- move_code：METHOD_DECISION

- statement_status：method_decision

- why_here_cn：正式设定评价采用三方法。

- inherits_from_previous_cn：行为复杂性。

- changes_argument_state_cn：评价架构成型。

- sets_up_next_cn：说明三方法如何互补。

- failure_if_removed_cn：三研究设计失去依据。

- evidence_pointer：Section 3.5 P2

### 31. Section 3.5 P3-P4

- order：31

- locator：Section 3.5 P3-P4

- paraphrase_cn：用多视角探索强化发现并补足每种方法弱点。

- move_code：METHOD_RATIONALE

- statement_status：method_decision

- why_here_cn：把三方法提升为互补、印证、补差。

- inherits_from_previous_cn：三方法确定。

- changes_argument_state_cn：多方法组合获得理论正当性。

- sets_up_next_cn：分别描述各自用途。

- failure_if_removed_cn：三研究组合的正当性弱。

- evidence_pointer：Section 3.5 P3-P4

### 32. Section 3.5 P5

- order：32

- locator：Section 3.5 P5

- paraphrase_cn：首先用survey看消息是否按ELM中心路径处理。

- move_code：STUDY1_USE

- statement_status：method_decision

- why_here_cn：定义Study 1在该证据链中任务：机制显著性。

- inherits_from_previous_cn：多方法原则。

- changes_argument_state_cn：Survey目标=概念证明。

- sets_up_next_cn：实验室实验作为下一步。

- failure_if_removed_cn：Study 1目的不清。

- evidence_pointer：Section 3.5 P5

### 33. Section 3.5 P6

- order：33

- locator：Section 3.5 P6

- paraphrase_cn：问卷还能比较不同消息是否激活不同行为构念。

- move_code：STUDY1_ADDITION

- statement_status：method_decision

- why_here_cn：给Survey多一个功能：构念显著性对比。

- inherits_from_previous_cn：Survey任务。

- changes_argument_state_cn：Survey结果可做构念级诊断。

- sets_up_next_cn：引出其证明概念的功能。

- failure_if_removed_cn：Survey的意义冗余。

- evidence_pointer：Section 3.5 P6

### 34. Section 3.5 P7-P8

- order：34

- locator：Section 3.5 P7-P8

- paraphrase_cn：再者，通过受控随机实验评估效果，限制混淆和选择效应以最大化内部效度。

- move_code：STUDY2_USE

- statement_status：method_decision

- why_here_cn：给Study 2定位：用实验内部效度确证行为效果。

- inherits_from_previous_cn：需要行为证据。

- changes_argument_state_cn：实验室实验目标=价值证明。

- sets_up_next_cn：引出对其实验室人工性的担心。

- failure_if_removed_cn：Study 2的内部效度说明缺失。

- evidence_pointer：Section 3.5 P7-P8

### 35. Section 3.5 P9-P10

- order：35

- locator：Section 3.5 P9-P10

- paraphrase_cn：由于实验室人工性可能威胁外部效度，我们与网站合作进行现场实验验证结果。

- move_code：STUDY3_USE

- statement_status：method_decision

- why_here_cn：把实验室局限转为推进现场实验的直接理由。

- inherits_from_previous_cn：实验室价值证明。

- changes_argument_state_cn：现场实验目标=应用证明。

- sets_up_next_cn：完成三方法角色分配。

- failure_if_removed_cn：Study 3必要性不成立。

- evidence_pointer：Section 3.5 P9-P10

### 36. Section 3.5 P11-P12

- order：36

- locator：Section 3.5 P11-P12

- paraphrase_cn：总之，评估方法实现多方法研究的互补、印证和补偿目的，并完成'最后一英里'。

- move_code：METHOD_SYNTHESIS

- statement_status：method_decision

- why_here_cn：用Venkatesh和Nunamaker等权威收束方法章节，提升方法框架合法性。

- inherits_from_previous_cn：三研究角色。

- changes_argument_state_cn：评价策略具备多方法理论背书。

- sets_up_next_cn：接下来三节逐个实施。

- failure_if_removed_cn：多方法框架的学术背书缺失。

- evidence_pointer：Section 3.5 P11-P12

## Study开头、过渡与收束图谱

### 1. Study 1 opening P1

- order：1

- locator：Study 1 opening P1

- paraphrase_cn：我们设计使用的核心原理是经中心路径处理的消息来增强用户理解。

- move_code：STUDY_RATIONALE_OPENING

- statement_status：theory_claim

- why_here_cn：回顾设计原则，让Study 1在该原则下显得必需。

- inherits_from_previous_cn：三阶段评价方案。

- changes_argument_state_cn：开始第一个研究。

- sets_up_next_cn：指出中心路径说服不易实现。

- failure_if_removed_cn：Study 1开头无理论连贯性。

- evidence_pointer：Section 4 P1

### 2. Study 1 problem P2

- order：2

- locator：Study 1 problem P2

- paraphrase_cn：但通过中心路径说服并不琐碎，设计不当的刺激常失败。

- move_code：PROBLEM_SETUP

- statement_status：prior_literature

- why_here_cn：引入风险：消息可能不达中心路径，为Survey检验提供必要性。

- inherits_from_previous_cn：中心路径原则。

- changes_argument_state_cn：中心路径成为待验证对象。

- sets_up_next_cn：提出Survey目的。

- failure_if_removed_cn：Survey研究显得多此一举。

- evidence_pointer：Section 4 P2

### 3. Study 1 survey purpose P3-P5

- order：3

- locator：Study 1 survey purpose P3-P5

- paraphrase_cn：所以我们先用survey确定刺激是否成功经中心路径处理，并证明概念供后续研究。

- move_code：STUDY_OBJECTIVE

- statement_status：method_decision

- why_here_cn：明确给出Study 1研究问题和方法类型。

- inherits_from_previous_cn：中心路径失败的潜在风险。

- changes_argument_state_cn：Study 1定义完成。

- sets_up_next_cn：Survey设计细节。

- failure_if_removed_cn：Study 1目标不明确。

- evidence_pointer：Section 4 P3-P5

### 4. Study 1 construct selection P1-P2

- order：4

- locator：Study 1 construct selection P1-P2

- paraphrase_cn：借鉴Johnston和Warkentin以及Cho等人的安全构念以评估消息显著性。

- move_code：MEASUREMENT_DECISION

- statement_status：method_decision

- why_here_cn：选择已有成熟构念确保测量可靠。

- inherits_from_previous_cn：Survey目标为构念诊断。

- changes_argument_state_cn：测量工具确定。

- sets_up_next_cn：说明这些构念如何与ELM共用。

- failure_if_removed_cn：Survey的构念来源不清。

- evidence_pointer：Section 4.1 P1-P2

### 5. Study 1 central-route inference rule P3-P6

- order：5

- locator：Study 1 central-route inference rule P3-P6

- paraphrase_cn：如果用户对警告消息的反应与对照不同，则说明消息经中心路径处理并提供了证据。

- move_code：INFERENCE_RULE

- statement_status：author_inference

- why_here_cn：设定解释规则：构念关系差异=中心路径加工证据。

- inherits_from_previous_cn：借用构念。

- changes_argument_state_cn：后续PLS多组分析结果将按此规则被解读。

- sets_up_next_cn：说明Survey不是为了发展新理论。

- failure_if_removed_cn：构念比较结果无法被解释为路径证据。

- evidence_pointer：Section 4.1 P3-P6

### 6. Study 1 implementation P1-P3

- order：6

- locator：Study 1 implementation P1-P3

- paraphrase_cn：Qualtrics问卷分发给美国西南部某大学253名本科生，四种处理，弱密码截图。

- move_code：SAMPLE_AND_PROCEDURE

- statement_status：method_decision

- why_here_cn：交代样本来源、样本量和处理分配，展示Survey实证基础。

- inherits_from_previous_cn：Survey设计。

- changes_argument_state_cn：Survey数据产生条件明确。

- sets_up_next_cn：PLS分析。

- failure_if_removed_cn：Survey结果无法评估代表性。

- evidence_pointer：Section 4.2

### 7. Study 1 PLS analysis P1-P3

- order：7

- locator：Study 1 PLS analysis P1-P3

- paraphrase_cn：使用PLS多组分析，比较处理组与对照组的路径系数差异。

- move_code：ANALYSIS_METHOD

- statement_status：method_decision

- why_here_cn：给出统计方法，使构念比较可操作。

- inherits_from_previous_cn：Survey数据。

- changes_argument_state_cn：分析层级确定。

- sets_up_next_cn：呈现结果。

- failure_if_removed_cn：结果无从计算。

- evidence_pointer：Section 4.3 P1-P3

### 8. Study 1 results P4-P6

- order：8

- locator：Study 1 results P4-P6

- paraphrase_cn：三个处理组与对照组的显著结果互不重叠，与消息含义一致。

- move_code：KEY_RESULT

- statement_status：empirical_result

- why_here_cn：给出Survey核心发现，作为'中心路径加工'证据。

- inherits_from_previous_cn：PLS多组分析。

- changes_argument_state_cn：概念证明成立。

- sets_up_next_cn：具体解释每组构念差异。

- failure_if_removed_cn：Study 1失去核心输出。

- evidence_pointer：Section 4.3 P4-P6

### 9. Study 1 exemplar interpretation P7-P11

- order：9

- locator：Study 1 exemplar interpretation P7-P11

- paraphrase_cn：以Rank为例解释了响应效能与他人脆弱性的显著关系，Time和Probability也分别与各自消息含义一致。

- move_code：RESULT_INTERPRETATION

- statement_status：author_inference

- why_here_cn：用单个处理与对照差异构建'消息被按含义理解'的证据链。

- inherits_from_previous_cn：总体非重叠结果。

- changes_argument_state_cn：构念差异与消息含义匹配。

- sets_up_next_cn：下结论消息被中心加工。

- failure_if_removed_cn：显著差异缺乏语义可解释性。

- evidence_pointer：Section 4.3 P7-P11

### 10. Study 1 conclusion and transition P12-P14

- order：10

- locator：Study 1 conclusion and transition P12-P14

- paraphrase_cn：初步概念证明表明个体按设计经中心路径处理消息，因此预期行为会改变，引出下两个实验。

- move_code：STUDY_CLOSURE_AND_TRANSITION

- statement_status：author_inference

- why_here_cn：总结Survey对机制的证明，并把研究推向行为实验。

- inherits_from_previous_cn：构念层面证据。

- changes_argument_state_cn：中心路径机制得到认可，行为检验成为下一步。

- sets_up_next_cn：进入Study 2。

- failure_if_removed_cn：Survey与行为实验之间缺桥接。

- evidence_pointer：Section 4.3 P12-P14

### 11. Study 2 opening P1-P2

- order：11

- locator：Study 2 opening P1-P2

- paraphrase_cn：接下来在受控随机实验中评估设计，确立价值证明；随机分配可最小化混淆和选择效应。

- move_code：STUDY_RATIONALE_OPENING

- statement_status：method_decision

- why_here_cn：说明Study 2的定位，并给出方法选择（受控实验）理由。

- inherits_from_previous_cn：Survey行为预期。

- changes_argument_state_cn：从机制证据转向因果行为证据。

- sets_up_next_cn：为MTurk平台辩护。

- failure_if_removed_cn：Study 2的'为什么能证明'缺失。

- evidence_pointer：Section 5 P1-P2

### 12. Study 2 MTurk rationale P3-P5

- order：12

- locator：Study 2 MTurk rationale P3-P5

- paraphrase_cn：在MTurk开展，因为样本已被验证有代表性且可复制传统结果，还能控制人口统计。

- move_code：SAMPLE_RATIONALE

- statement_status：prior_literature

- why_here_cn：为样本选择辩护，缓解外推性担忧。

- inherits_from_previous_cn：选择受控实验。

- changes_argument_state_cn：样品缺陷被提前辩护。

- sets_up_next_cn：介绍因变量测量。

- failure_if_removed_cn：MTurk样本合法性摇摆。

- evidence_pointer：Section 5 P3-P5

### 13. Study 2 measurement rationale P1-P2

- order：13

- locator：Study 2 measurement rationale P1-P2

- paraphrase_cn：我们用'密码强度增量'而非'最终强度'作为核心测量，以区分初始就强和由弱改强的用户。

- move_code：MEASUREMENT_DECISION

- statement_status：method_decision

- why_here_cn：直接回应上一小节的目标'修改密码'，并避免最终强度误译。

- inherits_from_previous_cn：强度计应促进的不仅是强密码而是修改。

- changes_argument_state_cn：diff_strength成为主要因变量。

- sets_up_next_cn：为数字修改次数设置作铺垫。

- failure_if_removed_cn：主结果指标失去合理性。

- evidence_pointer：Section 5.1 P1-P2

### 14. Study 2 second/third measures P3-P4

- order：14

- locator：Study 2 second/third measures P3-P4

- paraphrase_cn：第二测量为密码修改次数，第三为点击'Tips'学习密码知识的链接。

- move_code：MEASUREMENT_EXTENSION

- statement_status：method_decision

- why_here_cn：把行为结果拓展到修改次数和学习意图，以更全面地刻画强度计的作用。

- inherits_from_previous_cn：diff_strength已定。

- changes_argument_state_cn：因变量组合完整。

- sets_up_next_cn：进入实验设计。

- failure_if_removed_cn：因变量太窄，结论单一。

- evidence_pointer：Section 5.1 P3-P4

### 15. Study 2 realism/ethic constraints P1-P6

- order：15

- locator：Study 2 realism/ethic constraints P1-P6

- paraphrase_cn：实验需知情同意的披露，可能使参与者不认真，因此通过记忆验证和现场实验来缓解。

- move_code：ETHICAL_AND_BIAS_RESPONSE

- statement_status：author_inference

- why_here_cn：承认实验室的伦理约束可能造成偏差，并给出缓解方案。

- inherits_from_previous_cn：实验设计现实。

- changes_argument_state_cn：实验室局限被逐条管理。

- sets_up_next_cn：设计三个假设场景。

- failure_if_removed_cn：实验真实性问题未被正视。

- evidence_pointer：Section 5.2 P1-P6

### 16. Study 2 scenarios P1-P8

- order：16

- locator：Study 2 scenarios P1-P8

- paraphrase_cn：基于保护动机和计划行为理论设计Forum、Restaurant、Bank三个敏感度不同场景。

- move_code：DESIGN_DECISION

- statement_status：design_decision

- why_here_cn：引入场景变量，既增强任务真实感又检验敏感度调节。

- inherits_from_previous_cn：随机处理分配。

- changes_argument_state_cn：场景成为分析控制/调节。

- sets_up_next_cn：数据收集与样本描述。

- failure_if_removed_cn：场景效应与跨场景推广无从谈起。

- evidence_pointer：Section 5.2.1 P1-P8

### 17. Study 2 data collection P1-P5

- order：17

- locator：Study 2 data collection P1-P5

- paraphrase_cn：500名MTurk美国参与者，记录每位成员的完整密码历史。

- move_code：SAMPLE_AND_PROCEDURE

- statement_status：method_decision

- why_here_cn：给出样本量和数据日志类型，确立行为数据的客观性。

- inherits_from_previous_cn：设计已完成。

- changes_argument_state_cn：行为数据集已生成。

- sets_up_next_cn：回归分析。

- failure_if_removed_cn：实验样本基础不透明。

- evidence_pointer：Section 5.2.2 P1-P5

### 18. Study 2 main regression results P1-P8

- order：18

- locator：Study 2 main regression results P1-P8

- paraphrase_cn：线性、Poisson和logistic回归结果：只有Rank显著提高强度增量和修改次数，Forum效果强于Bank，Tips无差异。

- move_code：KEY_RESULT

- statement_status：empirical_result

- why_here_cn：给出实验室主结果，锁定Rank为最优处理。

- inherits_from_previous_cn：三因变量模型。

- changes_argument_state_cn：行为因果得到受控证据。

- sets_up_next_cn：解释场景的反直觉结果。

- failure_if_removed_cn：实验室贡献无法成立。

- evidence_pointer：Section 5.3 P1-P8

### 19. Study 2 scenario explanation P9-P13

- order：19

- locator：Study 2 scenario explanation P9-P13

- paraphrase_cn：银行场景强度增加最低可能因用户依赖其他保护或初始密码较强；加入initial_strength_label控制后Rank仍显著。

- move_code：ALTERNATIVE_EXPLANATION_TEST

- statement_status：author_inference

- why_here_cn：用控制变量检验反直觉场景效应的替代解释，确保主发现稳健。

- inherits_from_previous_cn：场景结果。

- changes_argument_state_cn：初始强度被纳入模型。

- sets_up_next_cn：稳健性分析。

- failure_if_removed_cn：场景效应和Rank效应都可能被质疑。

- evidence_pointer：Section 5.3 P9-P13

### 20. Study 2 robustness P14-P18

- order：20

- locator：Study 2 robustness P14-P18

- paraphrase_cn：补充learn_more控制、中介、调节、熵替代测量，结果定性一致。

- move_code：ROBUSTNESS_ANALYSIS

- statement_status：empirical_result

- why_here_cn：多角度排除混淆变量，防止结论被批评为特定测量或路径所致。

- inherits_from_previous_cn：主模型。

- changes_argument_state_cn：Rank效果稳健。

- sets_up_next_cn：转向现场实验。

- failure_if_removed_cn：主结果受稳健性威胁。

- evidence_pointer：Section 5.3 P14-P18

### 21. Study 2 closure and transition P19

- order：21

- locator：Study 2 closure and transition P19

- paraphrase_cn：实验室证明了Rank的有效性，但因知情同意和低风险，需要用现场实验提升外部效度。

- move_code：STUDY_CLOSURE_AND_TRANSITION

- statement_status：author_inference

- why_here_cn：明确实验室贡献并同时指出外部效度局限，为Study 3设置开场理由。

- inherits_from_previous_cn：实验室结果与稳健性。

- changes_argument_state_cn：论证进入现场实验。

- sets_up_next_cn：引入Study 3。

- failure_if_removed_cn：Study 3出现突兀。

- evidence_pointer：Section 5.3 P19

### 22. Study 3 opening P1

- order：22

- locator：Study 3 opening P1

- paraphrase_cn：第三项研究寻求确立实验室结果的效度，构成最后一英里和应用证明。

- move_code：STUDY_RATIONALE_OPENING

- statement_status：method_decision

- why_here_cn：开篇便重申证明层级和应用证明目标。

- inherits_from_previous_cn：实验室局限。

- changes_argument_state_cn：研究目标明确为外部效度。

- sets_up_next_cn：介绍合作伙伴和设置。

- failure_if_removed_cn：现场实验目的不清。

- evidence_pointer：Section 6 P1

### 23. Study 3 setting and measures P2-P5

- order：23

- locator：Study 3 setting and measures P2-P5

- paraphrase_cn：与亚洲在线折扣论坛合作，只收集两个行为指标（强度增量和修改次数），其余设置与实验室一致。

- move_code：SETTING_AND_MEASURES

- statement_status：method_decision

- why_here_cn：描述现场环境和因变量，确保与实验室可比。

- inherits_from_previous_cn：现场实验目标。

- changes_argument_state_cn：现场实验参数固定。

- sets_up_next_cn：讨论法律和隐私限制。

- failure_if_removed_cn：现场可比较性受损。

- evidence_pointer：Section 6 P2-P5

### 24. Study 3 Chinese wall compliance P6-P11

- order：24

- locator：Study 3 Chinese wall compliance P6-P11

- paraphrase_cn：法律禁止收集密码，因此用Chinese wall模型只收集密码强度而不存储密码，并用API验证登录和忘记密码行为。

- move_code：ETHICAL_COMPLIANCE_DESIGN

- statement_status：method_decision

- why_here_cn：解决现场实验的伦理/法律冲突：不通知用户但合规地测量行为，保证真实性。

- inherits_from_previous_cn：现场要真实。

- changes_argument_state_cn：现场数据可被合法收集。

- sets_up_next_cn：样本排除条件。

- failure_if_removed_cn：现场实验真实性无法在合规前提下实现。

- evidence_pointer：Section 6 P6-P11

### 25. Study 3 data cleaning P12-P15

- order：25

- locator：Study 3 data cleaning P12-P15

- paraphrase_cn：30天内310名新用户，排除未登录用户和忘记密码用户，保留308名进行分析。

- move_code：SAMPLE_CLEANING

- statement_status：method_decision

- why_here_cn：让读者看到样本筛选逻辑，增强现场数据分析透明度。

- inherits_from_previous_cn：API过滤。

- changes_argument_state_cn：最终样本得到定义。

- sets_up_next_cn：进行ANOVA分析。

- failure_if_removed_cn：样本有效性不清。

- evidence_pointer：Section 6 P12-P15

### 26. Study 3 ANOVA results P16-P18

- order：26

- locator：Study 3 ANOVA results P16-P18

- paraphrase_cn：ANOVA显示组间存在显著差异。

- move_code：KEY_RESULT

- statement_status：empirical_result

- why_here_cn：给出总体显著性，为成对比较提供前提。

- inherits_from_previous_cn：308名用户。

- changes_argument_state_cn：处理总体有效。

- sets_up_next_cn：进行Bonferroni校正成对比较。

- failure_if_removed_cn：后续成对比较复杂化。

- evidence_pointer：Section 6 P16-P18

### 27. Study 3 pairwise comparison P19-P22

- order：27

- locator：Study 3 pairwise comparison P19-P22

- paraphrase_cn：Bonferroni校正后，Rank在强度和修改次数上都显著优于对照；Time和Probability仅强度边缘显著。

- move_code：PAIRWISE_RESULT

- statement_status：empirical_result

- why_here_cn：确认Rank在真实环境中稳健有效，同时诚实报告Time和Probability的弱证据。

- inherits_from_previous_cn：ANOVA总显著。

- changes_argument_state_cn：现场验证完成。

- sets_up_next_cn：进入讨论总结。

- failure_if_removed_cn：现场实验无最有价值的处理比较结果。

- evidence_pointer：Section 6 P19-P22

### 28. Study 3 closure P23

- order：28

- locator：Study 3 closure P23

- paraphrase_cn：现场结果与实验室一致，Rank最优。

- move_code：STUDY_CLOSURE

- statement_status：empirical_result

- why_here_cn：把实验室与现场两个行为实验汇合，作为最终结论支撑。

- inherits_from_previous_cn：现场成对比较。

- changes_argument_state_cn：实证证据链闭合。

- sets_up_next_cn：进入Discussion的理论贡献。

- failure_if_removed_cn：讨论部分缺少跨研究一致性依据。

- evidence_pointer：Section 6 P23

## 讨论与贡献逐句图谱

### 1. Section 7.1 P1

- order：1

- locator：Section 7.1 P1

- paraphrase_cn：说服用户强密码一直是对管理者和研究者重要的任务。

- move_code：CONTEXT_RECAP

- statement_status：fact

- why_here_cn：以开场回到实践议题，提醒读者文章解决什么。

- inherits_from_previous_cn：三研究完成。

- changes_argument_state_cn：开始讨论章节。

- sets_up_next_cn：总结本研究的方法贡献。

- failure_if_removed_cn：讨论缺少实践入口。

- evidence_pointer：Section 7.1 P1

### 2. Section 7.1 P2

- order：2

- locator：Section 7.1 P2

- paraphrase_cn：我们的研究通过多方法增强强度计有效性来帮助这种努力。

- move_code：STUDY_SUMMARY

- statement_status：author_inference

- why_here_cn：总结本文做了什么，并把结果与任务连接。

- inherits_from_previous_cn：任务重要。

- changes_argument_state_cn：文章已完成目标。

- sets_up_next_cn：回顾理论内容。

- failure_if_removed_cn：研究总结缺少总起。

- evidence_pointer：Section 7.1 P2

### 3. Section 7.1 P3

- order：3

- locator：Section 7.1 P3

- paraphrase_cn：我们先用心理学文献识别底层理论。

- move_code：METHOD_RECAP

- statement_status：author_inference

- why_here_cn：重述研究路线，为理论贡献段打基础。

- inherits_from_previous_cn：研究总结。

- changes_argument_state_cn：理论概念被重新引回。

- sets_up_next_cn：说明ELM为何适配。

- failure_if_removed_cn：讨论没有理论起点。

- evidence_pointer：Section 7.1 P3

### 4. Section 7.1 P4

- order：4

- locator：Section 7.1 P4

- paraphrase_cn：发现ELM很契合，它解释了传统强度计的无效性并提供设计指南。

- move_code：THEORY_FIT

- statement_status：author_inference

- why_here_cn：为前文的理论选择提供后验合法性。

- inherits_from_previous_cn：识别理论。

- changes_argument_state_cn：ELM被确立为适合理据。

- sets_up_next_cn：解释设计如何走中心路径。

- failure_if_removed_cn：理论选择的正当性受损。

- evidence_pointer：Section 7.1 P4

### 5. Section 7.1 P5-P7

- order：5

- locator：Section 7.1 P5-P7

- paraphrase_cn：设计使用三类中心路径消息：恐惧诉求、同伴比较和共同纽带。

- move_code：DESIGN_RECAP

- statement_status：design_decision

- why_here_cn：总结设计构成，为结果总结做依据。

- inherits_from_previous_cn：ELM设计原则。

- changes_argument_state_cn：设计要素被重述。

- sets_up_next_cn：总结三项实验结果。

- failure_if_removed_cn：设计回顾不完整。

- evidence_pointer：Section 7.1 P5-P7

### 6. Section 7.1 P8

- order：6

- locator：Section 7.1 P8

- paraphrase_cn：我们进行了三项实验。

- move_code：RESULT_SUMMARY_OPEN

- statement_status：empirical_result

- why_here_cn：引出三研究总体结果。

- inherits_from_previous_cn：设计总结。

- changes_argument_state_cn：结果总结开始。

- sets_up_next_cn：三项结果互补性的核心声明。

- failure_if_removed_cn：结果总结缺少开场。

- evidence_pointer：Section 7.1 P8

### 7. Section 7.1 P9

- order：7

- locator：Section 7.1 P9

- paraphrase_cn：总体而言，结果是互补的，并提供理论和实践贡献。

- move_code：RESULT_SYNTHESIS

- statement_status：contribution_claim

- why_here_cn：把三项研究上升为统一贡献。

- inherits_from_previous_cn：三研究完成。

- changes_argument_state_cn：三研究的证据链被宣告完整。

- sets_up_next_cn：分别总结每项研究。

- failure_if_removed_cn：缺结果到贡献的桥梁。

- evidence_pointer：Section 7.1 P9

### 8. Section 7.1 P10

- order：8

- locator：Section 7.1 P10

- paraphrase_cn：Study 1的证据显示消息效果与消息含义一致，用户认真理解更强密码的含义。

- move_code：STUDY_RESULT_RECAP

- statement_status：empirical_result

- why_here_cn：总结Survey的贡献，强调其机制证据角色。

- inherits_from_previous_cn：三研究互补。

- changes_argument_state_cn：概念证明被重新表述。

- sets_up_next_cn：总结行为实验。

- failure_if_removed_cn：机制证据在讨论缺失。

- evidence_pointer：Section 7.1 P10

### 9. Section 7.1 P11-P12

- order：9

- locator：Section 7.1 P11-P12

- paraphrase_cn：Study 2和3在治疗效果排序上相互一致：Rank最好，其他两个在现场边缘显著、实验室不显著。

- move_code：STUDY_RESULT_RECAP

- statement_status：empirical_result

- why_here_cn：把两个行为实验的核心模式放在一起，显示跨情境一致性。

- inherits_from_previous_cn：Survey机制证据。

- changes_argument_state_cn：行为证据一致性确立。

- sets_up_next_cn：强调现场实验的外部效度价值。

- failure_if_removed_cn：Rank最优结论缺少跨研究总结。

- evidence_pointer：Section 7.1 P11-P12

### 10. Section 7.1 P13

- order：10

- locator：Section 7.1 P13

- paraphrase_cn：我们意识到现场'最后一英里'的好处，它提供了最强的外部效度。

- move_code：METHOD_VALUE

- statement_status：contribution_claim

- why_here_cn：把现场实验拔高为设计科学价值的关键组成部分。

- inherits_from_previous_cn：两个行为实验。

- changes_argument_state_cn：现场实验的必要性被辩护。

- sets_up_next_cn：回到与文献对话。

- failure_if_removed_cn：现场实验价值被低估。

- evidence_pointer：Section 7.1 P13

### 11. Section 7.1 P14

- order：11

- locator：Section 7.1 P14

- paraphrase_cn：与文献比较时，我们解决未决问题：识别密码无效的根因和无需新算法即可改善强度的机制。

- move_code：GAP_CLOSING

- statement_status：contribution_claim

- why_here_cn：把结果与引言理论缺口对接，完成文章闭环。

- inherits_from_previous_cn：三项研究结果。

- changes_argument_state_cn：引言中理论/实践缺口被声称已关闭。

- sets_up_next_cn：进入理论贡献明细。

- failure_if_removed_cn：讨论无法回扣引言目标。

- evidence_pointer：Section 7.1 P14

### 12. Section 7.2 P1

- order：12

- locator：Section 7.2 P1

- paraphrase_cn：我们做出两个重要理论贡献。

- move_code：CONTRIBUTION_OPENING

- statement_status：contribution_claim

- why_here_cn：贡献段总起。

- inherits_from_previous_cn：研究已有结果。

- changes_argument_state_cn：开始详细展开理论贡献。

- sets_up_next_cn：第一个贡献。

- failure_if_removed_cn：理论贡献缺少总领。

- evidence_pointer：Section 7.2 P1

### 13. Section 7.2 P2

- order：13

- locator：Section 7.2 P2

- paraphrase_cn：第一贡献是为强度计如何影响用户提供理论解释。

- move_code：THEORETICAL_CONTRIBUTION_1

- statement_status：contribution_claim

- why_here_cn：声明对IS文献的理论定位。

- inherits_from_previous_cn：贡献总起。

- changes_argument_state_cn：首个理论贡献被提出。

- sets_up_next_cn：解释该理论贡献的机制。

- failure_if_removed_cn：最强理论声言消失。

- evidence_pointer：Section 7.2 P2

### 14. Section 7.2 P3

- order：14

- locator：Section 7.2 P3

- paraphrase_cn：通过ELM理论化不同刺激怎样经外周或中心路线处理并影响密码行为。

- move_code：THEORETICAL_DETAIL

- statement_status：theory_claim

- why_here_cn：明确理论贡献的内容就是路径分类与行为后果的联系。

- inherits_from_previous_cn：首个贡献。

- changes_argument_state_cn：理论贡献有具体论证。

- sets_up_next_cn：说明该贡献填补可解释性缺口。

- failure_if_removed_cn：理论贡献空泛。

- evidence_pointer：Section 7.2 P3

### 15. Section 7.2 P4

- order：15

- locator：Section 7.2 P4

- paraphrase_cn：增加可解释性并回应先前所指出的黑箱设计缺口，可作为未来工作基础。

- move_code：GAP_CONNECTION

- statement_status：contribution_claim

- why_here_cn：将贡献绑定到引言中Furnell和Carnavalet的缺口。

- inherits_from_previous_cn：理论贡献详细化。

- changes_argument_state_cn：理论贡献回填了引言缺口。

- sets_up_next_cn：解释对数字情境的意义。

- failure_if_removed_cn：理论贡献与文献缺口脱节。

- evidence_pointer：Section 7.2 P4

### 16. Section 7.2 P5-P6

- order：16

- locator：Section 7.2 P5-P6

- paraphrase_cn：ELM数字情境适应帮助理解哪些刺激经中心/外周路径以及如何影响改进行为的可能性。

- move_code：ELM_ADAPTATION

- statement_status：contribution_claim

- why_here_cn：把本地证据扩展为ELM数字一般化。

- inherits_from_previous_cn：首个贡献。

- changes_argument_state_cn：理论贡献具备通用性。

- sets_up_next_cn：指出证据：不改算法仅加消息就能改善。

- failure_if_removed_cn：ELM适应性贡献缺失。

- evidence_pointer：Section 7.2 P5-P6

### 17. Section 7.2 P7-P9

- order：17

- locator：Section 7.2 P7-P9

- paraphrase_cn：证据表明不改算法只添加理论驱动的消息就可以显著改善行为，因此理论上小的修改可产生更强密码。

- move_code：EVIDENCE_BACKED_IMPLICATION

- statement_status：empirical_result

- why_here_cn：把理论贡献落到实证：呈现组件独立于算法有效。

- inherits_from_previous_cn：ELM应用。

- changes_argument_state_cn：首个理论贡献由实证支持。

- sets_up_next_cn：转向ELM文献贡献。

- failure_if_removed_cn：理论贡献缺实证支撑。

- evidence_pointer：Section 7.2 P7-P9

### 18. Section 7.2 P10

- order：18

- locator：Section 7.2 P10

- paraphrase_cn：第二个贡献贡献于ELM文献。

- move_code：CONTRIBUTION_2_OPEN

- statement_status：contribution_claim

- why_here_cn：第二贡献开始。

- inherits_from_previous_cn：第一贡献已完成。

- changes_argument_state_cn：ELM文献成为贡献对象。

- sets_up_next_cn：提出情境依赖主张。

- failure_if_removed_cn：第二理论贡献空位。

- evidence_pointer：Section 7.2 P10

### 19. Section 7.2 P11

- order：19

- locator：Section 7.2 P11

- paraphrase_cn：将ELM应用于数字情境建议刺激有效性可能依赖情境，这之前未被承认。

- move_code：CONTEXT_DEPENDENCE_CLAIM

- statement_status：theory_claim

- why_here_cn：提出ELM情境依赖修正，作为最深入的理论贡献。

- inherits_from_previous_cn：ELM应用。

- changes_argument_state_cn：ELM命题被修正/细化。

- sets_up_next_cn：用数字社会比较现象支撑。

- failure_if_removed_cn：第二理论贡献失去杀手锏。

- evidence_pointer：Section 7.2 P11

### 20. Section 7.2 P12-P14

- order：20

- locator：Section 7.2 P12-P14

- paraphrase_cn：数字世界的参与由社会和社区因素驱动，包括分享、比较和评价。

- move_code：DIGITAL_CONTEXT_EVIDENCE

- statement_status：prior_literature

- why_here_cn：提供理论依据：为何数字情境中社会比较可能强。

- inherits_from_previous_cn：情境依赖主张。

- changes_argument_state_cn：情境依赖有机制基础。

- sets_up_next_cn：把数据结果重新解释。

- failure_if_removed_cn：Rank最优的解释缺少背景。

- evidence_pointer：Section 7.2 P12-P14

### 21. Section 7.2 P15

- order：21

- locator：Section 7.2 P15

- paraphrase_cn：尽管三种消息都配ELM中心路径，但在数字情境中同伴比较在其他刺激中胜出。

- move_code：EVIDENCE_TO_THEORY_RETURN

- statement_status：empirical_result

- why_here_cn：把Rank实验结果重新说成ELM情境依赖的证据。

- inherits_from_previous_cn：数字社会比较背景。

- changes_argument_state_cn：特定处理优势变成理论命题的证据。

- sets_up_next_cn：解释为何同伴比较最好。

- failure_if_removed_cn：实证结果无法上升为理论贡献。

- evidence_pointer：Section 7.2 P15

### 22. Section 7.2 P16-P17

- order：22

- locator：Section 7.2 P16-P17

- paraphrase_cn：同伴比较通过嵌入相似用户比较为用户的注意力和认知提供上下文；其他刺激可能不符合语境预期并需额外认知资源。

- move_code：MECHANISM_EXPLANATION

- statement_status：author_inference

- why_here_cn：给出为什么Rank最优的心理机制解释。

- inherits_from_previous_cn：Rank胜出结果。

- changes_argument_state_cn：情境依赖解释具备机制。

- sets_up_next_cn：总结对ELM的影响。

- failure_if_removed_cn：Rank优势的解释性贡献薄弱。

- evidence_pointer：Section 7.2 P16-P17

### 23. Section 7.2 P18

- order：23

- locator：Section 7.2 P18

- paraphrase_cn：这些发现对ELM有启示，可能导致重新审视不同刺激类型推动行为的预设。

- move_code：THEORY_IMPLICATION

- statement_status：contribution_claim

- why_here_cn：将具体发现转为ELM研究未来方向。

- inherits_from_previous_cn：Rank机制解释。

- changes_argument_state_cn：理论贡献达到可引用声明。

- sets_up_next_cn：转向管理意义。

- failure_if_removed_cn：第二理论贡献缺收尾。

- evidence_pointer：Section 7.2 P18

### 24. Section 7.3 P1

- order：24

- locator：Section 7.3 P1

- paraphrase_cn：研究结果提供三个管理意义。

- move_code：MANAGERIAL_OPENING

- statement_status：contribution_claim

- why_here_cn：贡献段转向实践。

- inherits_from_previous_cn：理论贡献。

- changes_argument_state_cn：实践贡献开始。

- sets_up_next_cn：第一个：经济效果。

- failure_if_removed_cn：管理贡献段缺总起。

- evidence_pointer：Section 7.3 P1

### 25. Section 7.3 P2-P3

- order：25

- locator：Section 7.3 P2-P3

- paraphrase_cn：密码强度增加在统计和经济上都显著，为抵御暴力破解提供重要防线。

- move_code：MANAGERIAL_ECONOMIC

- statement_status：author_inference

- why_here_cn：把统计显著性转成经济效益。

- inherits_from_previous_cn：管理意义总起。

- changes_argument_state_cn：贡献具有经济解释。

- sets_up_next_cn：给出具体换算例子。

- failure_if_removed_cn：统计结果无实践价值解释。

- evidence_pointer：Section 7.3 P2-P3

### 26. Section 7.3 P4

- order：26

- locator：Section 7.3 P4

- paraphrase_cn：18%的强度增加意味着破解平均账户需多花五周左右。

- move_code：ECONOMIC_EXAMPLE

- statement_status：empirical_result

- why_here_cn：用可感知例子将强度数字转换为破解时间。

- inherits_from_previous_cn：经济意义。

- changes_argument_state_cn：管理意义直观化。

- sets_up_next_cn：讨论对运营中断的防止。

- failure_if_removed_cn：经济效益停留在抽象数字。

- evidence_pointer：Section 7.3 P4

### 27. Section 7.3 P5-P7

- order：27

- locator：Section 7.3 P5-P7

- paraphrase_cn：很难用货币衡量，但终端安全整体提升受重视，因为防止运营中断和信任法律问题，尤其多数网站仍用传统强度计。

- move_code：MANAGERIAL_VALUE

- statement_status：author_inference

- why_here_cn：不以货币，而以风险防控来论证价值，并强调现实采用场景。

- inherits_from_previous_cn：经济例子。

- changes_argument_state_cn：价值主张具有广泛适用性。

- sets_up_next_cn：进入第二管理含义。

- failure_if_removed_cn：价值主张缺少实际保护解释。

- evidence_pointer：Section 7.3 P5-P7

### 28. Section 7.3 P8-P10

- order：28

- locator：Section 7.3 P8-P10

- paraphrase_cn：第二，与高级技术不同，嵌入消息只需要最小投入，适用任意算法，计算在客户端，不需要服务端资源。

- move_code：MANAGERIAL_DEPLOYABILITY

- statement_status：contribution_claim

- why_here_cn：用可部署性作为第二实践卖点。

- inherits_from_previous_cn：管理意义总起。

- changes_argument_state_cn：低成本可部署性成为可执行建议。

- sets_up_next_cn：指出其显著优于传统。

- failure_if_removed_cn：实践贡献缺落地条件。

- evidence_pointer：Section 7.3 P8-P10

### 29. Section 7.3 P11

- order：29

- locator：Section 7.3 P11

- paraphrase_cn：结果表明设计在多个维度上显著比传统强度计好。

- move_code：EVIDENCE_RESTATEMENT

- statement_status：empirical_result

- why_here_cn：用前文证据再次夯实可部署建议。

- inherits_from_previous_cn：部署成本低。

- changes_argument_state_cn：低成本与高成效兼容。

- sets_up_next_cn：第三管理含义。

- failure_if_removed_cn：成本主张没有结果支持。

- evidence_pointer：Section 7.3 P11

### 30. Section 7.3 P12-P16

- order：30

- locator：Section 7.3 P12-P16

- paraphrase_cn：第三，在低安全环境中，Rank不仅比传统好，还能提升用户安全行为，这对许多只要求邮箱的低敏感网站尤为重要。

- move_code：MANAGERIAL_BOUNDARY

- statement_status：author_inference

- why_here_cn：用实验室场景结果定位实践边界：低敏感网站也能获益。

- inherits_from_previous_cn：部署建议。

- changes_argument_state_cn：管理贡献扩展到低安全场景。

- sets_up_next_cn：进入局限。

- failure_if_removed_cn：实践贡献范围不完整。

- evidence_pointer：Section 7.3 P12-P16

### 31. Section 7.4 P1

- order：31

- locator：Section 7.4 P1

- paraphrase_cn：我们的研究并非没有局限。

- move_code：LIMITATION_OPENING

- statement_status：author_inference

- why_here_cn：开启限制清单。

- inherits_from_previous_cn：贡献总结。

- changes_argument_state_cn：研究结论被限定。

- sets_up_next_cn：列举局限。

- failure_if_removed_cn：讨论内容无自我限制。

- evidence_pointer：Section 7.4 P1

### 32. Section 7.4 P2

- order：32

- locator：Section 7.4 P2

- paraphrase_cn：第一项实验是探索性的，只关注数据可靠性和构念差异。

- move_code：LIMITATION_1

- statement_status：author_inference

- why_here_cn：主动定位Survey为探索性，防止中心路径证据被过度解读。

- inherits_from_previous_cn：限制开场。

- changes_argument_state_cn：Survey地位被谨慎限定。

- sets_up_next_cn：第二限制。

- failure_if_removed_cn：Survey证据可能被过度解释为中心路径确证。

- evidence_pointer：Section 7.4 P2

### 33. Section 7.4 P3-P4

- order：33

- locator：Section 7.4 P3-P4

- paraphrase_cn：MTurk参与者较熟悉技术，可能引入偏差；但控制变量使偏差不影响操纵效果。

- move_code：LIMITATION_2

- statement_status：author_inference

- why_here_cn：坦诚样本局限同时提供缓解。

- inherits_from_previous_cn：第一限制。

- changes_argument_state_cn：样本风险被管理。

- sets_up_next_cn：下一条未研究的行为限制。

- failure_if_removed_cn：MTurk样本偏差的坦诚缺失。

- evidence_pointer：Section 7.4 P3-P4

### 34. Section 7.4 P5-P8

- order：34

- locator：Section 7.4 P5-P8

- paraphrase_cn：没有跟踪用户点击Tips后是否阅读和使用；未来可用问卷和追踪研究。

- move_code：LIMITATION_AND_FUTURE

- statement_status：author_inference

- why_here_cn：识别因变量学习行为的盲区，提出后续研究方案。

- inherits_from_previous_cn：当前因变量。

- changes_argument_state_cn：研究缺口被自我标注。

- sets_up_next_cn：下一条消息类型限制。

- failure_if_removed_cn：学习行为未知，教育功能过度声称。

- evidence_pointer：Section 7.4 P5-P8

### 35. Section 7.4 P9

- order：35

- locator：Section 7.4 P9

- paraphrase_cn：三类消息并非穷尽，未来可研究其他消息。

- move_code：LIMITATION_3

- statement_status：author_inference

- why_here_cn：限制消息空间，避免'三类即全部'误解。

- inherits_from_previous_cn：已研究三类。

- changes_argument_state_cn：设计空间被承认开放。

- sets_up_next_cn：下一条数据训练限制。

- failure_if_removed_cn：消息类型被当作完备。

- evidence_pointer：Section 7.4 P9

### 36. Section 7.4 P10-P11

- order：36

- locator：Section 7.4 P10-P11

- paraphrase_cn：强度计算主要用RockYou训练，未来可用更新的数据集验证。

- move_code：LIMITATION_4

- statement_status：author_inference

- why_here_cn：限制训练数据时效性，并给未来复用路径。

- inherits_from_previous_cn：前面限制。

- changes_argument_state_cn：强度计算有效边界被划定。

- sets_up_next_cn：最后一个比较限制。

- failure_if_removed_cn：强度计算的通则性被过大宣称。

- evidence_pointer：Section 7.4 P10-P11

### 37. Section 7.4 P12-P13

- order：37

- locator：Section 7.4 P12-P13

- paraphrase_cn：未与其他非传统强度计比较，未来元研究可在相似条件下比较不同方法。

- move_code：LIMITATION_5_AND_FUTURE

- statement_status：author_inference

- why_here_cn：承认相对优势只相对于传统标签，并指出更广基准的未来。

- inherits_from_previous_cn：已有新设计。

- changes_argument_state_cn：相对有效性范围被限定。

- sets_up_next_cn：结束全文。

- failure_if_removed_cn：基准比较的边界未声明。

- evidence_pointer：Section 7.4 P12-P13

## Study累积逻辑

### 1. 1

- study_or_phase：理论驱动设计（概念构建）

- evidence_job_cn：把ELM的抽象命题翻译为三种可操作消息，并固定算法基线。

- what_it_establishes_cn：建立处理变量（Time、Rank、Probability）与对照组的操作化差异。

- what_it_cannot_establish_cn：不能证明用户真的会中心路径加工这些消息，也不能证明行为改变。

- why_next_phase_is_needed_cn：若不验证消息显著性，后续行为实验可能建立在无效刺激上。

- transition_wording_function_cn：Section 2.3的'我们将通过系列实验连接结果回到设计原则和ELM'，把概念设计交付给实证检验。

### 2. 2

- study_or_phase：Study 1：survey-based proof of concept

- evidence_job_cn：用自我报告构念差异证明消息被仔细加工（中心路径）。

- what_it_establishes_cn：三个处理组与对照组在安全构念关系上出现与消息含义一致的差异，且不重叠。

- what_it_cannot_establish_cn：不能证明真实密码行为变化；学生样本；自我报告。

- why_next_phase_is_needed_cn：构念层面证据之后需要行为层面随机实验；否则'消息显著'不代表'行为改变'。

- transition_wording_function_cn：Section 4结尾说'既然用户仔细处理消息，可以预期行为改变，这是接下来两个实验的焦点'，把构念证据导向行为检验。

### 3. 3

- study_or_phase：Study 2：controlled laboratory proof of value

- evidence_job_cn：在受控随机实验（MTurk）中建立设计对密码行为改写的因果效果。

- what_it_establishes_cn：Rank显著提高diff_strength和num_reset；初始强度和场景被控制；多种稳健性分析。

- what_it_cannot_establish_cn：不能完全排除实验室人工性、知情同意和低激励造成的偏差；外部效度存疑。

- why_next_phase_is_needed_cn：需要真实用户和真实风险条件下验证，避免实验室只能证明内部效度。

- transition_wording_function_cn：Section 5结尾以'实验室知情同意和低风险可能导致外部效度问题，因此进行现场实验'完成向Study 3过渡。

### 4. 4

- study_or_phase：Study 3：field randomized proof of use

- evidence_job_cn：在真实论坛注册流程中检验最优设计（Rank）的外部效度和可行性。

- what_it_establishes_cn：现场总体ANOVA显著，Rank在强度增量和修改次数上均显著优于对照，与实验室一致。

- what_it_cannot_establish_cn：无法收集控制变量；不能观察长期行为和密码复用；单国家单论坛场景。

- why_next_phase_is_needed_cn：证据链已足够形成综述，不需要下一实验；需要把跨研究证据整合为理论和实践贡献。

- transition_wording_function_cn：Discussion把三研究结果合并，并调用'最后一英里'概念证明现场实验的价值。

## 主张—证据台账

### 1. 增强消息是通过中心路径被加工（概念证明）。

- claim_cn：增强消息是通过中心路径被加工（概念证明）。

- claim_level：mechanism

- supporting_evidence_cn：Survey PLS多组分析显示每个处理组与对照组在安全构念关系上出现与消息含义一致的非重叠差异。

- support_strength：partial

- where_claim_is_made：Section 4.3 P4-P6

- where_evidence_is_provided：Table 2, Section 4.3

### 2. Rank（同伴比较）显著提高密码强度增量。

- claim_cn：Rank（同伴比较）显著提高密码强度增量。

- claim_level：artifact

- supporting_evidence_cn：实验室线性回归系数0.089(p<0.01)并控制初始强度后仍显著；现场Bonferroni成对比较均值差0.186(p=0.007)。

- support_strength：direct

- where_claim_is_made：Section 5.3 P3, Section 6 结果段

- where_evidence_is_provided：Table 3, Table 4, Table 6

### 3. Rank（同伴比较）显著提高密码修改次数。

- claim_cn：Rank（同伴比较）显著提高密码修改次数。

- claim_level：artifact

- supporting_evidence_cn：实验室Poisson回归系数0.993(p<0.01)；现场均值差0.393(p=0.004)。

- support_strength：direct

- where_claim_is_made：Section 5.3 P3, Section 6 结果段

- where_evidence_is_provided：Table 3, Table 6

### 4. Time和Probability也有一定效果。

- claim_cn：Time和Probability也有一定效果。

- claim_level：artifact

- supporting_evidence_cn：现场Bonferroni校正后两者在强度增量上边缘显著(p<0.10)，但实验室两者不显著，Probability修改次数不显著。

- support_strength：partial

- where_claim_is_made：Section 6 结果段、Section 7.1

- where_evidence_is_provided：Table 6, Table 3

### 5. 效果来自消息呈现，而不是强度算法改进。

- claim_cn：效果来自消息呈现，而不是强度算法改进。

- claim_level：artifact

- supporting_evidence_cn：所有处理使用相同的backoff Markov模型、阈值和标签，唯一改变是消息文本。

- support_strength：direct

- where_claim_is_made：Section 3.1 P13, Section 3.5 P21

- where_evidence_is_provided：Section 3.1, Table 1

### 6. 设计部署成本低并兼容现有算法（实践贡献）。

- claim_cn：设计部署成本低并兼容现有算法（实践贡献）。

- claim_level：design_knowledge

- supporting_evidence_cn：实现为客户端JavaScript/AJAX消息显示，无需新服务器硬件的设计说明。

- support_strength：partial

- where_claim_is_made：Introduction P5 S5-S7, Section 7.3 P8-P10

- where_evidence_is_provided：Section 3.1-3.4实现描述

### 7. ELM刺激有效性在数字情境中是情境依赖的，同伴比较优于其他刺激。

- claim_cn：ELM刺激有效性在数字情境中是情境依赖的，同伴比较优于其他刺激。

- claim_level：theory

- supporting_evidence_cn：实验室、现场两项随机实验一致显示Rank最优，且数字参与受社会比较驱动。

- support_strength：partial

- where_claim_is_made：Section 7.2 P11-P17

- where_evidence_is_provided：Table 3, Table 6

## ISR定位逻辑

- constitutive_is_problem_cn：文章不是单纯展示一个更好的密码强度计，而是把'弱密码持续存在'写成一个组织访问控制中的技术-行为问题：技术制品的呈现组件如何构成用户的安全行为结果。文章从组织视角（密码是主导认证机制）开篇，并在讨论中把行为效果转化为暴力破解风险与管理价值，因此问题的本质是信息系统中的用户行为管理。

- technology_behavior_or_market_entanglement_cn：技术与人/组织的纠缠体现在：强度计只是一个信息呈现工具，但用户是否修改密码、修改后强度如何，是人与制品界面互动的结果；文章更把数字环境中的社会比较特性（社交参与、评价、产品流行度）引入来解释为什么Rank优于其他刺激，即技术呈现与社会心理在数字平台上相互构成。

- role_of_benchmark_or_objective_evidence_cn：benchmark始终是'仅显示强度标签的传统强度计'，而非高级算法或最优破解器。客观证据（密码强度增量、修改次数）被用来支持'理论驱动消息改变行为'这个IS主张，而不是证明算法优劣；现场随机实验更是证明在真实平台和合法合规约束下，呈现设计仍能改变行为。

- theory_in_design_cn：理论深度进入设计：ELM在实验前就决定了设计原则（必须使用中心路径刺激），三类消息都从ELM相关文献合法推导，随后Survey验证哪些构念被激活，而不是事后用ELM解释结果。这种做法使ELM成为设计处方而非事后标签。

- technical_vs_is_contribution_balance_cn：技术贡献约占三成：backoff Markov实现、排名计算、前端JS架构；IS贡献约占七成：理论驱动的行为干预、三阶段随机证据链、组织访问安全的实践意义。文章把技术设计包裹在'如何影响用户'的IS叙事中，避免技术细节成为主角。

- beyond_transient_performance_cn：文章用三种方式超越暂时分数优势：一是所有实验固定算法，证明非分数提升而是消息呈现效果；二是跨survey、实验室、现场三种样本形成的稳定性证据；三是把Rank最优上升为ELM情境依赖的理论贡献，而不仅是'这个设计分数更高'。

## 段落级仿写模板

### abstract_steps

#### 1. 1

- step：1

- action_cn：用领域最常见机制开场，给出研究发生的技术环境。

- sentence_function_cn：一句话建立普遍背景。

#### 2. 2

- step：2

- action_cn：转出该机制中一个持续失败的行为事实，并表明挑战。

- sentence_function_cn：第二句给出问题张力。

#### 3. 3

- step：3

- action_cn：提出用某个规范理论增强现有制品设计。

- sentence_function_cn：给出理论入口。

#### 4. 4

- step：4

- action_cn：说明使用哪几个证据来源和它们分别证明什么。

- sentence_function_cn：方法预告，带proof概念。

#### 5. 5

- step：5

- action_cn：报告总体发现和一个关键行为指标的变化。

- sentence_function_cn：结果简述。

#### 6. 6

- step：6

- action_cn：把发现升华为针对终端用户的实践方法。

- sentence_function_cn：贡献句。

### introduction_paragraph_steps

#### 1. 1

- step：1

- action_cn：用主导技术现象建立组织语境并指出其现实价值。

- sentence_function_cn：第一段背景+利害。

#### 2. 2

- step：2

- action_cn：用具体证据或反例否定替代路线，把问题收窄到唯一可行方案。

- sentence_function_cn：第二段对象聚焦。

#### 3. 3

- step：3

- action_cn：描述制品的工作原理与理想功能，再引出现实与文献落差。

- sentence_function_cn：第三段制品背景与问题。

#### 4. 4

- step：4

- action_cn：明确自己的补充性切入角度与具体研究边界。

- sentence_function_cn：第四段定位与范围。

#### 5. 5

- step：5

- action_cn：用一条文献证据建立理论缺口，引出理论并给出方法预告。

- sentence_function_cn：第四段后部理论引入。

#### 6. 6

- step：6

- action_cn：分别列出理论贡献和实践贡献，并用路线图收尾。

- sentence_function_cn：第五、六段贡献与导航。

### theory_to_design_steps

#### 1. 1

- step：1

- action_cn：先综述与所选组件（而非整个技术）最接近的文献。

- sentence_function_cn：限定综述范围。

#### 2. 2

- step：2

- action_cn：承认该组件有作用，但紧接着指出'机制/理论'缺失。

- sentence_function_cn：形成理论缺口。

#### 3. 3

- step：3

- action_cn：把制品重新定义为某种说服/影响工具，再引入双过程理论。

- sentence_function_cn：理论登场。

#### 4. 4

- step：4

- action_cn：用理论把现有组件方式归到'低精细路线'，从而解释其短暂性。

- sentence_function_cn：理论重述已有现象。

#### 5. 5

- step：5

- action_cn：引用同一个理论在其他IS情境的成功例证，并指出无人用于该制品。

- sentence_function_cn：缺口精确化。

#### 6. 6

- step：6

- action_cn：按设计科学范式提取一条'应加入中心路径刺激'的设计处方。

- sentence_function_cn：理论转设计处方。

#### 7. 7

- step：7

- action_cn：从ELM文献中逐一选三类消息，每类都先用理论机制再用应用先例支撑。

- sentence_function_cn：设计候选生成。

#### 8. 8

- step：8

- action_cn：预告实现为'情境化制品'，并用三阶段评价（概念/价值/应用）作为后续证据链。

- sentence_function_cn：设计到验证的桥。

### method_and_study_sequence_steps

#### 1. 1

- step：1

- action_cn：描述基线制的实现和强度模型的唯一选择，强调所有处理共享。

- sentence_function_cn：基线+内部效度基础。

#### 2. 2

- step：2

- action_cn：逐一说明各消息如何由模型数据计算，给出示例文本。

- sentence_function_cn：处理可操作化。

#### 3. 3

- step：3

- action_cn：用'行为复杂'为多方法辩护，并给每个研究分配proof级任务。

- sentence_function_cn：多方法框架。

#### 4. 4

- step：4

- action_cn：第一个研究检验'机制是否如理论所预期被激活'，用成熟构念和组间比较。

- sentence_function_cn：机制证明。

#### 5. 5

- step：5

- action_cn：第二个研究用随机受控实验检验行为指标，选择一个能捕捉'变化'的因变量。

- sentence_function_cn：行为证明。

#### 6. 6

- step：6

- action_cn：第三个研究通过真实平台和合规设计复现关键结果。

- sentence_function_cn：应用证明。

### results_reporting_steps

#### 1. 1

- step：1

- action_cn：先陈述主回归规格或分析方法，再说明各因变量的特殊结构。

- sentence_function_cn：方法细节前置于结果。

#### 2. 2

- step：2

- action_cn：按因变量顺序报告处理效应，显著与不显著都明确列出。

- sentence_function_cn：主结果。

#### 3. 3

- step：3

- action_cn：用'奇怪结果+可能解释'的方式引出控制变量分析。

- sentence_function_cn：替代解释。

#### 4. 4

- step：4

- action_cn：用稳健性小节逐一回应：额外控制、中介、调节、替代测量。

- sentence_function_cn：稳健性。

#### 5. 5

- step：5

- action_cn：最后总结该研究能证明什么、不能证明什么来推动下一研究。

- sentence_function_cn：研究间过渡。

### discussion_and_contribution_steps

#### 1. 1

- step：1

- action_cn：用回扣开篇，重述任务与三研究互补性。

- sentence_function_cn：总结。

#### 2. 2

- step：2

- action_cn：把实证结果重述为'解决了文献中的理论缺口'。

- sentence_function_cn：贡献定位。

#### 3. 3

- step：3

- action_cn：提出第一条理论贡献：为该制品建立理论机制解释。

- sentence_function_cn：理论贡献1。

#### 4. 4

- step：4

- action_cn：提出第二条理论贡献：把结果回馈给原理论，给出情境依赖修正。

- sentence_function_cn：理论贡献2。

#### 5. 5

- step：5

- action_cn：用可感知的经济换算或部署成本谈管理意义。

- sentence_function_cn：实践意义。

#### 6. 6

- step：6

- action_cn：逐条列出局限，并为每条给出未来研究方向。

- sentence_function_cn：边界与未来。

## 可执行写作算法

### 1. 1

- step：1

- rhetorical_job_cn：用领域普遍机制开场，并指出该机制中的持续失败事实。

- research_evidence_required_cn：行业基准报告、记录在案的技术失败案例、或权威实证结论如'大多数密码弱'。

- sentence_pattern_function_cn：第一句给背景，第二句给问题张力，第三句排除替代路线。

- transition_condition_cn：当读者已接受'该问题重要且替代方案不可行'，立即进入'制品为本'的聚焦。

### 2. 2

- step：2

- rhetorical_job_cn：选定研究对象并列出满足'理论驱动、轻量、低成本'的设计约束。

- research_evidence_required_cn：对目标制品已具备清晰的功能定义与领域标准（如NIST指南）。

- sentence_pattern_function_cn：用'我们设计一个满足以下特征的…'枚举约束。

- transition_condition_cn：当设计约束能把后继理论选择'锁定'时，进入文献解剖。

### 3. 3

- step：3

- rhetorical_job_cn：把现有工作拆成主流路线和缺口路线，指出主流集中于算法而忽视呈现。

- research_evidence_required_cn：该领域的综述性工作、代表算法/指标文献、以及至少一条'缺乏理论指南'的权威发现。

- sentence_pattern_function_cn：先列'很多工作都在做X'，再用转折'但这些都忽略Y'。

- transition_condition_cn：当缺口指向'缺少理论解释'和'黑箱设计'时，才能过渡到理论选择。

### 4. 4

- step：4

- rhetorical_job_cn：引入一个可解释该制品为何失效的理论，并指定设计科学范式。

- research_evidence_required_cn：该理论对双过程机制的经典定义、在其他IS情境成功应用的实证先例，以及在目标制品上未经测验的证据。

- sentence_pattern_function_cn：把制品重新定义为说服工具，再登入理论，再指出'没有人在这种制品上用中心路径刺激'。

- transition_condition_cn：当理论能同时解释既有失败和指出新设计方向时，进入设计处方。

### 5. 5

- step：5

- rhetorical_job_cn：从理论推导出一句清晰的设计处方，再逐类从文献中选消息类型。

- research_evidence_required_cn：每种消息类型都有理论机制文本支持和跨域实证先例。

- sentence_pattern_function_cn：处方句给出'要加入中心路径刺激'，随后每类消息按'理论机制→应用案例→IS应用→设计决定'推进。

- transition_condition_cn：当三类消息都具备各自机制和示例文本后，可以进入实现与评价。

### 6. 6

- step：6

- rhetorical_job_cn：实现基线并保持跨处理固定，把每个处理定义为对基线的一个小改动。

- research_evidence_required_cn：可复现的强度模型、训练数据集、精确阈值选择和实现技术（如focusout事件）。

- sentence_pattern_function_cn：先选模型并辩护，再定义阈值，再强调所有处理共享同算法，最后给每类消息的生成规则。

- transition_condition_cn：当每个处理具备明确计算逻辑且唯一变量是消息文本时，可组建对比。

### 7. 7

- step：7

- rhetorical_job_cn：用'行为复杂'正当化多方法，并按概念/价值/应用三级分配证据任务。

- research_evidence_required_cn：三个可实施的研究：构念级survey、行为级随机实验、现场随机实验；每个都标注proof级别。

- sentence_pattern_function_cn：先陈述行为复杂，再列出三方法互补，再分别说明每个研究要证明什么。

- transition_condition_cn：当证明链能回答'理论生效了吗→行为改变了吗→现实可用吗'时，展开三研究。

### 8. 8

- step：8

- rhetorical_job_cn：第一个研究用构念差异验证理论机制，但要在讨论中限定其为探索性。

- research_evidence_required_cn：成熟测量量表、多组比较统计工具（如PLS）、样本代表性说明。

- sentence_pattern_function_cn：说明借用构念，设定'差异=中心路径证据'的解释规则，报告非重叠显著性并逐组解释。

- transition_condition_cn：当构念结果支持中心路径时，声明'因此应观察到行为变化'并进入行为研究。

### 9. 9

- step：9

- rhetorical_job_cn：第二个研究用受控随机实验验证行为，选择能代表'变化'而不是终点的因变量。

- research_evidence_required_cn：随机分配、行为日志、与因变量匹配的回归模型、至少一种稳健性替代测量。

- sentence_pattern_function_cn：先为样本方法和因变量选择辩护，再报告主回归，再用额外分析排除替代解释。

- transition_condition_cn：当某项处理稳定显著而其他处理不显著时，进入现场实验确认该处理的外部效度。

### 10. 10

- step：10

- rhetorical_job_cn：第三个研究在真实平台复现关键结果，并用合规设计说明如何在伦理下保持真实。

- research_evidence_required_cn：真实平台合作、随机分配机制、法律/伦理约束设计、明确的样本筛选日志。

- sentence_pattern_function_cn：先确立外部效度目标，再用'不收集敏感数据+API验证'化解两难，最后用总体ANOVA和校正后成对比较报告。

- transition_condition_cn：当现场结果与实验室一致、且差异有明确统计量时，可以进入综合讨论。

### 11. 11

- step：11

- rhetorical_job_cn：讨论中先汇总证据链，再把最优处理上升为理论情境修正，最后落回实践部署。

- research_evidence_required_cn：跨研究的模式一致性、至少一个理论层面的新命题、可实施的管理建议。

- sentence_pattern_function_cn：总结→回填文献缺口→声明理论贡献1、2→经济效益/部署成本→限制与未来。

- transition_condition_cn：当证据能同时支持IS贡献和ELM文献贡献时，才可宣称完成。

## 应模仿的高价值动作

1. 用理论把既有制品定义为'说服工具'，从而让理论机制直接介入设计选择。

2. 在实验前就明确'中心路径消息'设计处方，避免事后贴标签。

3. 用算法固定+仅改消息文本的对照组设计，把呈现组件效果与技术效果分离开。

4. 在每个Study开头明确指出它承担proof of concept/value/use中的哪一级。

5. 用'强度增量'而非'最终强度'作为因变量，并用一个反例说明为什么终点强度会误导。

6. 在结果段主动报告不显著的处理，再用现场边缘显著来补充而不是掩盖。

7. 在讨论中把'Rank最好'从结果上升为'ELM刺激有效性与情境相关'的理论命题。

8. 用'最后一英里'和Nunamaker等来提升设计科学论文的贡献层级。

9. 对每个限制不仅说局限，还给出未来研究可执行的方向。

10. 把现场伦理限制用Chinese wall模型+API验证化解，展示合规与真实可并存。

## 不要只复制的表面动作

1. 不要只贴'设计科学、Type V理论'标签而不给出设计处方是如何从理论推导来的。

2. 不要只声称'中心路径'，而没有像Survey那样的构念级验证。

3. 不要把三类处理全部称为'有效'，实验室中Time和Probability并不显著。

4. 不要在没有任何真实平台合作的情况写下'完成应用证明'。

5. 不要重复用'多方法互补'套话而不具体说明每个方法补哪个弱点。

6. 不要只报告最终强度而不解释初始状态；经验教训应融入指标选择。

## 证据薄弱或跳跃的动作

1. Survey的'中心路径证据'实际只是自我报告构念关系的推断，没有直接认知加工测量；作者自己也限定为探索性。

2. Time和Probability在实验室不显著，但讨论把现场边缘显著视为有效性证据，证据强度有限。

3. '数字情境中社会比较更强'是对Rank最优的事后解释，并非预先假设，且缺少直接中介证据。

4. 现场实验没有控制变量，却被用来支持管理意义的量化（18%→多五周破解），外部变量的混淆无法排除。

5. 三类消息不穷尽，但文章在贡献部分把'消息有效性'说得较广。

## 一句话套路

用一个心理学理论重新解释既有安全提示为何效果有限，把理论命题译成三种可落地的消息设计，再用从问卷到现场的三阶段因果证据链证明设计有效，最后把最强的Rank结果反哺为ELM情境依赖的理论修正。

## 分析边界

正文完整但图表（图1-4）只看到占位符，无法核实视觉文本；表格Text OCR基本可见但Table 2中部分数值可能因OCR缺位。在线附录A-F、稳健性分析材料、测量题项和随机化检查细节未纳入全文，因此对问卷可靠性和部分稳健性结论只依据正文描述判断。文章收稿/录用时间线显示在线发表为2022年3月，版本记录2023年Infoms版权。
