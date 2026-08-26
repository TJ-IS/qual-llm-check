# The Phishing Funnel Model: A Design Artifact to Predict User Susceptibility to Phishing Websites：ISR 句段级微观图谱

- 作者：Ahmed Abbasi; David Dobolyi; Anthony Vance; Fatemeh Mariam Zahedi
- 年份：2021
- DOI：10.1287/isre.2020.0973
- 源文件：28020_2021_the-phishing-funnel-model-a-design-artifact-to-predict-user-susceptibility-to-phishing-websites.md
- 置信度：0.78

## 核实后的宏观骨架

全文按设计科学‘构建—评价—贡献升级’的弧线组织。引言先用钓鱼攻击的普遍性与经济成本建立问题重要性，再用用户识别失败和工具警告失效两种证据把问题收窄为‘用户与工具认知失调’，随即把研究目标从‘预测网站是否钓鱼’转向‘预测用户是否会上当’，并定义易感性。第2节梳理已有易感性模型（HITLSF、AAM、PSF、DRKM、PSM），指出它们是描述性而非预测性制品。第3节提出PFM制品：以营销/Web分析中的漏斗隐喻把因变量从单一行为改为四阶段序数响应（visit、browse、consider legitimate、intend to transact），并以TAM、PMT、HITLSF为知识基础选择工具、威胁、用户三类六组变量；随后用带复合核的支持向量序数回归（SVORCK）估计模型，其中复合核内嵌累积链接混合模型（CLMM）以捕捉用户异质性和跨阶段依赖。第4节用两个纵向现场实验回答RQ1和RQ2：第5节为12个月两家企业预测实验（1,278名员工、49,373次交互），通过与竞争模型/方法的两层benchmark、特征消融、威胁通道分析和Hawthorne稳健性检验证明PFM的预测效能；第6节为3个月干预实验（1,218名员工、13,824次交互），用六种设置（PFM-SVORCK、PFM-CLMM、SVM、HITLSF、随机、标准）证明预测驱动的分级警告显著降低漏斗穿越，并用成本收益分析与敏感性分析把行为改善转化为经济价值。第7节依次完成结果汇总、三条贡献声明、为何不能自动移除钓鱼内容的边界讨论，以及局限与未来研究。文章的论证主线是‘制品是什么—测量是否可用—能否预测—预测是否有用—价值多大’。

## 摘要逐句图谱

### 1. Abstract S1

- order：1

- locator：Abstract S1

- paraphrase_cn：钓鱼是组织面临的重大安全问题，威胁员工和公众。

- move_code：CONTEXT

- statement_status：fact

- why_here_cn：开篇把研究放在IS读者关心的安全议题中，给出问题域。

- inherits_from_previous_cn：无前置句，是摘要的事实起点。

- changes_argument_state_cn：从‘无主题’推进到‘存在重大安全问题’。

- sets_up_next_cn：为下一句区分两类受害对象、放大后果作铺垫。

- failure_if_removed_cn：摘要失去问题语境，后续方案与贡献失去靶心。

- evidence_pointer：Abstract paragraph 1 S1

### 2. Abstract S2

- order：2

- locator：Abstract S2

- paraphrase_cn：针对员工的威胁可导致严重安全事件，针对公众的威胁会损害信任、满意度和品牌。

- move_code：PRACTICAL_STAKES

- statement_status：fact

- why_here_cn：把‘重大安全问题’具体化为组织和市场两类后果，说明问题不只是技术故障。

- inherits_from_previous_cn：承接S1的‘威胁员工和公众’。

- changes_argument_state_cn：把问题的性质从技术漏洞推进为组织与商业后果，抬高解决的紧迫性。

- sets_up_next_cn：为S3指出‘用户识别失败’这一根源提供动机。

- failure_if_removed_cn：读者无法判断为什么必须解决用户端问题，贡献的价值感下降。

- evidence_pointer：Abstract paragraph 1 S2

### 3. Abstract S3

- order：3

- locator：Abstract S3

- paraphrase_cn：问题根源在于互联网用户即使使用反钓鱼工具也无法识别攻击。

- move_code：PHENOMENON

- statement_status：author_inference

- why_here_cn：把问题锚定到‘用户+工具’的共同失败，而不是单纯的检测技术失败，为全文转向用户易感性预测埋下伏笔。

- inherits_from_previous_cn：承接S2的两类受害者，说明无论哪类受害者，根源都是用户端识别失败。

- changes_argument_state_cn：从‘问题存在且后果严重’推进到‘明确失败机制’。

- sets_up_next_cn：为S4提出预测易感性的设计制品提供直接理由。

- failure_if_removed_cn：摘要缺少‘为什么现有检测不够’的关键断定，PFM的必要性不成立。

- evidence_pointer：Abstract paragraph 1 S3

### 4. Abstract S4

- order：4

- locator：Abstract S4

- paraphrase_cn：我们提出钓鱼漏斗模型（PFM），一个预测用户对钓鱼网站易感性的设计制品。

- move_code：SOLUTION_OR_OBJECTIVE

- statement_status：contribution_claim

- why_here_cn：在问题说完后立即宣布解决方案制品及其类型（设计制品），完成摘要的‘问题—方案’对位。

- inherits_from_previous_cn：直接回应S3的用户识别失败。

- changes_argument_state_cn：从‘问题’转入‘制品对象’，为后续设计细节设定主题。

- sets_up_next_cn：需要解释制品包含什么、如何预测。

- failure_if_removed_cn：读者不知道本文做了什么，摘要变成纯问题陈述。

- evidence_pointer：Abstract paragraph 1 S4

### 5. Abstract S5

- order：5

- locator：Abstract S5

- paraphrase_cn：PFM纳入用户、威胁和工具相关因素，预测访问、浏览、视为合法和交易意图四个阶段的行为。

- move_code：DESIGN_FEATURE

- statement_status：design_decision

- why_here_cn：一句话概括制品的两大设计特征：变量类别（三类因素）与因变量结构（四阶段漏斗）。

- inherits_from_previous_cn：承接S4‘PFM是什么’，具体化其输入与输出。

- changes_argument_state_cn：从‘提出制品’推进到‘制品如何操作化’。

- sets_up_next_cn：为S6说明这种多阶段序数结构需要什么样的估计方法。

- failure_if_removed_cn：缺少制品核心设计，方法选择失去依据，结果难以理解。

- evidence_pointer：Abstract paragraph 1 S5

### 6. Abstract S6

- order：6

- locator：Abstract S6

- paraphrase_cn：我们使用带自定义核的支持向量序数回归，核内包含累积链接混合模型，以表示用户跨漏斗阶段的决策。

- move_code：METHOD_JUSTIFICATION

- statement_status：method_decision

- why_here_cn：说明预测方法及其与多阶段因变量之间的对应关系，为后面‘SVORCK’命名和实验对比做铺垫。

- inherits_from_previous_cn：承接S5的四阶段序数响应，说明序数回归+自定义核正是为这类结构设计。

- changes_argument_state_cn：把‘制品的预测架构’推进为‘可执行的估计方法’。

- sets_up_next_cn：为S7介绍评价方法的现场实验提供必要性。

- failure_if_removed_cn：摘要缺方法主张，读者不知道预测如何实现，后续AUC结果无方法依托。

- evidence_pointer：Abstract paragraph 1 S6

### 7. Abstract S7

- order：7

- locator：Abstract S7

- paraphrase_cn：我们在两家组织开展了为期12个月的纵向现场实验，涉及1,278名员工和49,373次钓鱼交互。

- move_code：STUDY_OVERVIEW

- statement_status：empirical_result

- why_here_cn：给出评价证据的规模和场景，说明不是实验室模拟而是真实组织中的纵向现场数据。

- inherits_from_previous_cn：承接S6的方法，说明该方法被放在真实组织环境中检验。

- changes_argument_state_cn：从‘方法设计’推进到‘证据基础’。

- sets_up_next_cn：为S8的AUC和高严重度检测率结果提供可信的样本与实验背景。

- failure_if_removed_cn：结果数字失去情境，读者无法判断外部效度。

- evidence_pointer：Abstract paragraph 1 S7

### 8. Abstract S8

- order：8

- locator：Abstract S8

- paraphrase_cn：PFM的AUC比竞争模型/方法高8%–52%，并能96%正确预测对高严重度威胁的访问，比最近竞争者高10个百分点。

- move_code：RESULT

- statement_status：empirical_result

- why_here_cn：给出核心预测效能量化结果，用AUC和高严重度访问两个指标同时说明准确性与实践重要性。

- inherits_from_previous_cn：承接S7的12个月现场数据，指标结果依据该样本。

- changes_argument_state_cn：从‘有证据基础’推进到‘证据表明PFM显著更优’。

- sets_up_next_cn：为S9提出干预实验与下游价值提供动机。

- failure_if_removed_cn：预测优势这一核心主张无支撑，全文贡献不成立。

- evidence_pointer：Abstract paragraph 1 S8

### 9. Abstract S9

- order：9

- locator：Abstract S9

- paraphrase_cn：后续三个月的现场研究显示，使用PFM的员工显著较少与钓鱼威胁互动。

- move_code：RESULT

- statement_status：empirical_result

- why_here_cn：把证据链从‘能预测’延伸到‘预测能改变真实行为’，回答RQ2。

- inherits_from_previous_cn：承接S8的预测优势，检验该优势能否转化为干预效果。

- changes_argument_state_cn：从‘预测效能’推进到‘下游行为改善’。

- sets_up_next_cn：为S10的成本收益结果作行为层面的铺垫。

- failure_if_removed_cn：全文只剩预测精度，缺少‘有用性’证据，设计科学贡献不完整。

- evidence_pointer：Abstract paragraph 1 S9

### 10. Abstract S10

- order：10

- locator：Abstract S10

- paraphrase_cn：成本收益分析显示，PFM驱动的干预比比较预测方法每员工多减少近1,900美元的钓鱼相关成本。

- move_code：RESULT

- statement_status：empirical_result

- why_here_cn：把行为改善货币化，为管理者提供经济语言的价值证据。

- inherits_from_previous_cn：承接S9的较少交互，用成本收益把这些交互差异转化为美元。

- changes_argument_state_cn：从‘行为改善’推进到‘经济价值’。

- sets_up_next_cn：为S11和S12的普适性声明与三条实践含义提供依据。

- failure_if_removed_cn：实践价值主张缺经济支撑，对ISR的 practitioner读者说服力下降。

- evidence_pointer：Abstract paragraph 1 S10

### 11. Abstract S11

- order：11

- locator：Abstract S11

- paraphrase_cn：这些结果表明PFM具有强外部效度。

- move_code：INTERPRETATION

- statement_status：author_inference

- why_here_cn：从两个组织、长期现场数据中概括出一般性声明，把实证结果升格为对制品普适性的判断。

- inherits_from_previous_cn：承接S7–S10的现场证据。

- changes_argument_state_cn：从‘本地证据’推进到‘普适主张’。

- sets_up_next_cn：为S12陈述实践含义做铺垫。

- failure_if_removed_cn：摘要直接从结果跳到含义会显得突兀；但该句本身有‘超证据外推’风险（将在分析中标注）。

- evidence_pointer：Abstract paragraph 1 S11

### 12. Abstract S12

- order：12

- locator：Abstract S12

- paraphrase_cn：发现对实践有重要含义：预测易感性作为实时防护策略有效；应把钓鱼过程各阶段一起建模；反钓鱼工具与威胁因素对易感性影响很大。

- move_code：CONTRIBUTION

- statement_status：contribution_claim

- why_here_cn：把实证结果转成三条可迁移的设计/实践知识，完成摘要的贡献收束。

- inherits_from_previous_cn：承接S8–S10的预测、干预与成本证据，并回应S3的用户-工具失败机制。

- changes_argument_state_cn：从‘证据’推进到‘知识贡献’，摘要论证闭环。

- sets_up_next_cn：无直接后续；为正文引言和讨论中的对应句子提供摘要级预告。

- failure_if_removed_cn：摘要停留在结果罗列，缺少读者能带走的设计知识。

- evidence_pointer：Abstract paragraph 1 S12

## 引言逐句图谱

### 1. Introduction P1 S1

- order：1

- locator：Introduction P1 S1

- paraphrase_cn：钓鱼是利用人的漏洞而非软件漏洞的语义攻击，是最普遍的网罪形式之一，每年影响超4000万用户。

- move_code：CONTEXT

- statement_status：fact

- why_here_cn：第一句定义问题性质并给出规模，把钓鱼从一般网安议题提升为高普遍性威胁。

- inherits_from_previous_cn：无前置，是引言论证的起点。

- changes_argument_state_cn：建立‘钓鱼是大问题’的事实基础。

- sets_up_next_cn：为S2说明IT管理者关注和经济成本提供对象。

- failure_if_removed_cn：引言失去问题定义与规模锚点。

- evidence_pointer：Introduction P1 S1

### 2. Introduction P1 S2

- order：2

- locator：Introduction P1 S2

- paraphrase_cn：钓鱼持续位列IT管理者最关心的安全问题，因为员工被骗且客户品牌与信任受损。

- move_code：PRACTICAL_STAKES

- statement_status：fact

- why_here_cn：把普遍性转化为管理者和企业的关注点，区分员工与客户两类受害对象。

- inherits_from_previous_cn：承接S1的‘最普遍形式’。

- changes_argument_state_cn：从‘问题普遍’推进到‘问题被管理者高度重视’。

- sets_up_next_cn：为S3的经济成本数字作铺垫。

- failure_if_removed_cn：缺乏管理相关性，IS读者难以看到研究价值。

- evidence_pointer：Introduction P1 S2

### 3. Introduction P1 S3

- order：3

- locator：Introduction P1 S3

- paraphrase_cn：平均一万员工公司每年花费约370万美元应对钓鱼。

- move_code：PRACTICAL_STAKES

- statement_status：fact

- why_here_cn：用具体金额量化损失，为后文成本收益分析埋下伏笔。

- inherits_from_previous_cn：承接S2的管理者关注，给出金钱尺度。

- changes_argument_state_cn：把‘重要’推进为‘昂贵’。

- sets_up_next_cn：为S4–S5提出更优方案的必要性提供经济背景；也与第6.2.1节成本收益呼应。

- failure_if_removed_cn：经济动机减弱，后文每员工1,960美元收益缺少对照基准。

- evidence_pointer：Introduction P1 S3

### 4. Introduction P2 S1

- order：4

- locator：Introduction P2 S1

- paraphrase_cn：多项研究显示互联网用户在区分合法与钓鱼网站或避免与钓鱼网站交易方面表现很差。

- move_code：PRIOR_KNOWLEDGE

- statement_status：prior_literature

- why_here_cn：从组织经济问题转入用户行为证据，建立‘用户端是薄弱环节’。

- inherits_from_previous_cn：承接第一段的问题严重性，点出问题核心出现在用户。

- changes_argument_state_cn：从‘问题存在’推进到‘用户行为失败是问题的一部分’。

- sets_up_next_cn：为S2的量化失败率作概括。

- failure_if_removed_cn：后续用户易感性概念缺少行为依据。

- evidence_pointer：Introduction P2 S1

### 5. Introduction P2 S2

- order：5

- locator：Introduction P2 S2

- paraphrase_cn：用户有40%–80%的时间无法正确识别钓鱼网站，超过70%的用户愿意与钓鱼网站交易。

- move_code：LIMITATION

- statement_status：prior_literature

- why_here_cn：量化用户失败程度，为‘仅靠用户无法自保’提供硬数据。

- inherits_from_previous_cn：承接P2 S1的定性结论。

- changes_argument_state_cn：从‘失败存在’推进到‘失败程度严重’。

- sets_up_next_cn：为P3讨论反钓鱼工具作为潜在解决方案作对照。

- failure_if_removed_cn：用户端失败缺少幅度，后文‘需要替代方案’的说服力下降。

- evidence_pointer：Introduction P2 S2

### 6. Introduction P3 S1

- order：6

- locator：Introduction P3 S1

- paraphrase_cn：一个潜在解决方案是使用反钓鱼工具，包括浏览器安全工具栏和专有插件。

- move_code：PRIOR_KNOWLEDGE

- statement_status：prior_literature

- why_here_cn：先给出‘最显而易见的解决方案’，以便随后证明其不足。

- inherits_from_previous_cn：回应P2的用户失败，指出行业惯用应对手段。

- changes_argument_state_cn：从‘用户失败’推进到‘现有应对方案’。

- sets_up_next_cn：为S2的工具失效证据作铺垫。

- failure_if_removed_cn：缺少‘工具作为方案’的铺垫，工具失效的转折失去靶子。

- evidence_pointer：Introduction P3 S1

### 7. Introduction P3 S2

- order：7

- locator：Introduction P3 S2

- paraphrase_cn：然而即使使用这些工具，钓鱼成功率仍很高，因为用户常解释掉或忽视工具警告。

- move_code：LIMITATION

- statement_status：prior_literature

- why_here_cn：对‘工具能解决问题’给出否定证据，构成引言的关键转折。

- inherits_from_previous_cn：承接S1的‘潜在解决方案’。

- changes_argument_state_cn：从‘有工具’推进到‘工具在用户端失效’。

- sets_up_next_cn：为S3解释失效原因（警告未个性化）做准备。

- failure_if_removed_cn：没有这一否定，后文‘不同方法’的必要性不成立。

- evidence_pointer：Introduction P3 S2

### 8. Introduction P3 S3

- order：8

- locator：Introduction P3 S3

- paraphrase_cn：失败的一个原因可能是用户不认为反钓鱼工具警告是针对自己的。

- move_code：MECHANISM

- statement_status：author_inference

- why_here_cn：给出工具失效的机制解释——个性化缺失，为预测驱动个性化干预提供理论动机。

- inherits_from_previous_cn：承接S2的‘用户忽视警告’。

- changes_argument_state_cn：从‘工具失效’推进到‘失效机制’。

- sets_up_next_cn：为P4提出预测用户易感性的新方向作逻辑跳板。

- failure_if_removed_cn：个性化/易感性预测的动机链断裂。

- evidence_pointer：Introduction P3 S3

### 9. Introduction P4 S1

- order：9

- locator：Introduction P4 S1

- paraphrase_cn：本研究采用不同方法：不是预测链接或网站是否为钓鱼，而是预测用户的钓鱼易感性。

- move_code：GAP_PIVOT

- statement_status：author_inference

- why_here_cn：在引言中完成核心转向：从检测威胁对象转向预测用户行为，这是全文最关键的论证动作。

- inherits_from_previous_cn：承接P3的工具失效与个性化机制。

- changes_argument_state_cn：把问题定义从‘网站分类’改写为‘用户易感性预测’，确立研究空白。

- sets_up_next_cn：为S2定义易感性并列举三个用途。

- failure_if_removed_cn：全文没有区别于以往反钓鱼研究的新问题，贡献主张失去基础。

- evidence_pointer：Introduction P4 S1

### 10. Introduction P4 S2

- order：10

- locator：Introduction P4 S2

- paraphrase_cn：我们把易感性定义为用户与钓鱼攻击互动的程度。

- move_code：DEFINITION

- statement_status：author_inference

- why_here_cn：给新概念一个可操作、可测量的定义，为后文漏斗因变量提供概念基础。

- inherits_from_previous_cn：承接S1的‘用户易感性’。

- changes_argument_state_cn：把模糊概念转成‘互动程度’这一可预测连续体。

- sets_up_next_cn：为S3说明该定义带来的三个应用价值。

- failure_if_removed_cn：易感性概念悬空，后文四阶段漏斗缺少定义支撑。

- evidence_pointer：Introduction P4 S2

### 11. Introduction P4 S3

- order：11

- locator：Introduction P4 S3

- paraphrase_cn：这样的方案能（1）通过个性化实时警告改善安全技术使用，（2）提供个性化访问控制和安全政策，（3）随高易感性因素随时间变化而适应。

- move_code：DESIGN_IMPLICATION

- statement_status：author_inference

- why_here_cn：列出预测易感性的三个下游价值，说明为何值得开发该制品。

- inherits_from_previous_cn：承接S2的定义。

- changes_argument_state_cn：从‘可定义’推进到‘有价值’。

- sets_up_next_cn：为P5正式提出研究目标与制品作铺垫。

- failure_if_removed_cn：缺少价值预告，研究目标显得无的放矢。

- evidence_pointer：Introduction P4 S3

### 12. Introduction P5 S1

- order：12

- locator：Introduction P5 S1

- paraphrase_cn：因此本研究目标是开发预测用户对钓鱼网站易感性的设计制品。

- move_code：RESEARCH_OBJECTIVE

- statement_status：author_inference

- why_here_cn：正式陈述研究目标，把前面的问题与价值转成可执行任务。

- inherits_from_previous_cn：承接P4的新方向与三项价值。

- changes_argument_state_cn：从‘有价值的方向’推进到‘正式研究目标’。

- sets_up_next_cn：为S2引入设计科学范式作准备。

- failure_if_removed_cn：引言缺少明确目标句，全文主线不清晰。

- evidence_pointer：Introduction P5 S1

### 13. Introduction P5 S2

- order：13

- locator：Introduction P5 S2

- paraphrase_cn：我们采用设计科学范式指导PFM制品的开发。

- move_code：METHOD_OR_PARADIGM

- statement_status：method_decision

- why_here_cn：声明研究范式，为后文‘制品—评价—贡献’结构提供方法论标签。

- inherits_from_previous_cn：承接S1的‘设计制品’目标。

- changes_argument_state_cn：把研究定位为设计科学，预告评价方式。

- sets_up_next_cn：为S3–S4概括PFM内容作框架铺垫。

- failure_if_removed_cn：读者无法预判后续是理论检验还是制品构建与评价。

- evidence_pointer：Introduction P5 S2

### 14. Introduction P5 S3

- order：14

- locator：Introduction P5 S3

- paraphrase_cn：PFM强调反钓鱼工具、钓鱼威胁和用户相关因素在四个关键漏斗阶段（访问、浏览、视为合法、交易）决策中的作用。

- move_code：DESIGN_FEATURE

- statement_status：design_decision

- why_here_cn：第一次在正文给出制品名称、三类因素和四阶段因变量结构。

- inherits_from_previous_cn：承接S2的设计科学定位。

- changes_argument_state_cn：从‘开发PFM’推进到‘PFM的核心构成’。

- sets_up_next_cn：为S4的估计方法作铺垫。

- failure_if_removed_cn：制品的要素设计在引言中缺失，读者无法跟随后续模型章节。

- evidence_pointer：Introduction P5 S3

### 15. Introduction P5 S4

- order：15

- locator：Introduction P5 S4

- paraphrase_cn：模型用带自定义核的支持向量序数回归估计，可简约捕捉用户多次钓鱼遭遇中的漏斗阶段决策。

- move_code：DESIGN_FEATURE

- statement_status：design_decision

- why_here_cn：预告核心方法SVORCK，并强调‘简约’与‘用户异质性’，为第3.2节作引。

- inherits_from_previous_cn：承接S3的四阶段决策结构。

- changes_argument_state_cn：从‘制品构成’推进到‘估计方法’。

- sets_up_next_cn：为P6引出RQ1/RQ2作准备。

- failure_if_removed_cn：方法名称缺失，后文SVORCK/CLMM对比显得突兀。

- evidence_pointer：Introduction P5 S4

### 16. Introduction P6 S1

- order：16

- locator：Introduction P6 S1

- paraphrase_cn：设计科学研究问题通常关注制品内设计元素的有效性，以及制品如何提升运营效用。

- move_code：RQ_FRAME

- statement_status：prior_literature

- why_here_cn：把研究问题锚定在设计科学标准上，说明为何RQ聚焦预测力与下游价值。

- inherits_from_previous_cn：承接P5的制品与方法。

- changes_argument_state_cn：把制品开发转成可检验的研究问题框架。

- sets_up_next_cn：为S2引出两RQ作理论依据。

- failure_if_removed_cn：RQ缺乏范式依据，读者不知道这两问题为何是核心。

- evidence_pointer：Introduction P6 S1

### 17. Introduction P6 S2

- order：17

- locator：Introduction P6 S2

- paraphrase_cn：因此我们的研究问题聚焦预测能力及其下游含义。

- move_code：RQ_INTRO

- statement_status：author_inference

- why_here_cn：从一般设计科学RQ过渡到本研究的两个具体RQ。

- inherits_from_previous_cn：承接S1的设计科学RQ标准。

- changes_argument_state_cn：把‘研究问题应关注什么’落实到‘本研究的问题域’。

- sets_up_next_cn：为S3和S4的RQ1/RQ2作引。

- failure_if_removed_cn：两个RQ缺乏引导，直接出现显得突兀。

- evidence_pointer：Introduction P6 S2

### 18. Introduction P6 S3

- order：18

- locator：Introduction P6 S3

- paraphrase_cn：RQ1：PFM能否在组织中随时间有效地预测用户易感性？

- move_code：RQ1

- statement_status：author_inference

- why_here_cn：正式提出预测能力问题，决定第5节实验结构。

- inherits_from_previous_cn：承接S2的‘预测能力’。

- changes_argument_state_cn：把‘预测能力’变成一个可回答的研究问题。

- sets_up_next_cn：为RQ2作并列结构。

- failure_if_removed_cn：第5节预测实验失去问题靶心。

- evidence_pointer：Introduction P6 S3

### 19. Introduction P6 S4

- order：19

- locator：Introduction P6 S4

- paraphrase_cn：RQ2：由易感性预测驱动的干预能否改善组织中的回避结果？

- move_code：RQ2

- statement_status：author_inference

- why_here_cn：提出下游价值问题，决定第6节干预实验结构。

- inherits_from_previous_cn：承接S2的‘下游含义’，与RQ1并列。

- changes_argument_state_cn：把‘下游含义’具体化为干预效果问题。

- sets_up_next_cn：为P7预告两个现场实验作直接铺垫。

- failure_if_removed_cn：干预实验没有对应问题，研究设计缺一半。

- evidence_pointer：Introduction P6 S4

### 20. Introduction P7 S1

- order：20

- locator：Introduction P7 S1

- paraphrase_cn：为回答这些问题，我们在两个纵向现场实验中评价PFM。

- move_code：STUDY_OVERVIEW

- statement_status：method_decision

- why_here_cn：从RQ过渡到评价设计，给出两个实验的总括。

- inherits_from_previous_cn：直接对应RQ1/RQ2。

- changes_argument_state_cn：从‘问题’推进到‘如何回答’。

- sets_up_next_cn：为S2–S3分别介绍两个实验。

- failure_if_removed_cn：从RQ直接跳到结果会缺少研究设计路标。

- evidence_pointer：Introduction P7 S1

### 21. Introduction P7 S2

- order：21

- locator：Introduction P7 S2

- paraphrase_cn：第一个实验跨度12个月，在两家组织进行，涉及1,278名员工和49,373次钓鱼交互，显示PFM在真实环境中优于竞争模型。

- move_code：STUDY1_PREVIEW

- statement_status：empirical_result

- why_here_cn：预告实验1的规模与结论，使读者在正文前就掌握证据基础。

- inherits_from_previous_cn：承接S1的两个实验总括。

- changes_argument_state_cn：确立RQ1的证据规模和初步结论。

- sets_up_next_cn：为S3的第二个实验作对照。

- failure_if_removed_cn：实验1的规模与结论缺少预告，后文结果缺少期待感。

- evidence_pointer：Introduction P7 S2

### 22. Introduction P7 S3

- order：22

- locator：Introduction P7 S3

- paraphrase_cn：第二个是同一两家组织的三个月随访现场研究，考察由易感性预测引导的干预效果，展示准确预测易感性的下游价值。

- move_code：STUDY2_PREVIEW

- statement_status：empirical_result

- why_here_cn：预告实验2的目的与结论，完成RQ1/RQ2与两个实验的映射。

- inherits_from_previous_cn：承接RQ2与S1的两实验总括。

- changes_argument_state_cn：确立RQ2的价值主张。

- sets_up_next_cn：为P8贡献定位作铺垫。

- failure_if_removed_cn：干预实验的价值预告缺失，讨论中的下游价值主张缺乏早期锚点。

- evidence_pointer：Introduction P7 S3

### 23. Introduction P8 S1

- order：23

- locator：Introduction P8 S1

- paraphrase_cn：从设计科学角度看，PFM是一个新颖方案。

- move_code：CONTRIBUTION_POSITIONING

- statement_status：contribution_claim

- why_here_cn：在方法论上给贡献定位，预示后文会按设计科学准则声明贡献类型。

- inherits_from_previous_cn：承接P7的两个实验证据。

- changes_argument_state_cn：从‘有效果’推进到‘是知识贡献’。

- sets_up_next_cn：为S2解释新颖性来源作铺垫。

- failure_if_removed_cn：贡献定位缺失，贡献声明显得无根基。

- evidence_pointer：Introduction P8 S1

### 24. Introduction P8 S2

- order：24

- locator：Introduction P8 S2

- paraphrase_cn：虽然钓鱼是已知问题，但预测用户易感性是新挑战，属于主动安全分析。

- move_code：NOVELTY

- statement_status：author_inference

- why_here_cn：把‘新颖’具体化为‘新问题而非已知问题的再研究’。

- inherits_from_previous_cn：承接S1的‘新颖方案’。

- changes_argument_state_cn：确立贡献的新颖维度。

- sets_up_next_cn：为S3的‘improvement’定位作铺垫。

- failure_if_removed_cn：新颖性声明缺乏理由。

- evidence_pointer：Introduction P8 S2

### 25. Introduction P8 S3

- order：25

- locator：Introduction P8 S3

- paraphrase_cn：因此根据设计科学指南，我们的知识贡献可视为‘改进型’（improvement）贡献。

- move_code：CONTRIBUTION_TYPE

- statement_status：contribution_claim

- why_here_cn：明确贡献类型为improvement，避免宣称理论突破，符合Gregor和Hevner的分类。

- inherits_from_previous_cn：承接S2的新颖性。

- changes_argument_state_cn：把贡献从‘新颖’推进到‘可归类知识贡献’。

- sets_up_next_cn：为S4说明面向的实践群体。

- failure_if_removed_cn：贡献定位模糊，可能被审稿人质疑贡献性质。

- evidence_pointer：Introduction P8 S3

### 26. Introduction P8 S4

- order：26

- locator：Introduction P8 S4

- paraphrase_cn：制品和发现对两类群体有含义：IT安全经理和一般互联网用户。

- move_code：IMPLICATION_PREVIEW

- statement_status：contribution_claim

- why_here_cn：指出贡献的受众，为讨论部分的实践贡献作铺垫。

- inherits_from_previous_cn：承接S3的贡献类型。

- changes_argument_state_cn：把贡献与读者身份关联。

- sets_up_next_cn：为P9的三缺口清单作过渡。

- failure_if_removed_cn：实践关联缺失，ISR读者难以看到‘与我相关’。

- evidence_pointer：Introduction P8 S4

### 27. Introduction P9 S1

- order：27

- locator：Introduction P9 S1

- paraphrase_cn：本研究回应三个重要研究缺口。

- move_code：GAP_LIST_INTRO

- statement_status：author_inference

- why_here_cn：在引言末尾把前面的问题系统化为三个缺口，为讨论部分的闭合提供清单。

- inherits_from_previous_cn：承接全文背景与贡献定位。

- changes_argument_state_cn：从‘我们已经做什么’转为‘我们还填补什么空白’。

- sets_up_next_cn：为S2–S7逐条展开三个缺口。

- failure_if_removed_cn：缺口的系统声明缺失，讨论部分无法逐条回扣。

- evidence_pointer：Introduction P9 S1

### 28. Introduction P9 S2

- order：28

- locator：Introduction P9 S2

- paraphrase_cn：第一，以往研究未尝试预测用户易感性，只开发或检验描述性行为模型。

- move_code：GAP1

- statement_status：prior_literature

- why_here_cn：界定第一缺口：缺乏预测性制品。

- inherits_from_previous_cn：承接S1的缺口清单。

- changes_argument_state_cn：把‘没有预测制品’具体化为第一缺口。

- sets_up_next_cn：为S3补充IS文献依据，为S4给出填补方式。

- failure_if_removed_cn：第一贡献主张失去文献缺口背景。

- evidence_pointer：Introduction P9 S2

### 29. Introduction P9 S3

- order：29

- locator：Introduction P9 S3

- paraphrase_cn：缺乏预测性IT制品是此前IS研究也指出的空白。

- move_code：GAP1_SUPPORT

- statement_status：prior_literature

- why_here_cn：用IS领域权威呼吁（Shmueli和Koppius）证明第一缺口在学科层面成立。

- inherits_from_previous_cn：承接S2的具体缺口。

- changes_argument_state_cn：把第一缺口从‘本文观察’提升为‘学科共识’。

- sets_up_next_cn：为S4的填补声明提供依据。

- failure_if_removed_cn：缺口缺乏学科合法性。

- evidence_pointer：Introduction P9 S3

### 30. Introduction P9 S4

- order：30

- locator：Introduction P9 S4

- paraphrase_cn：我们不仅证明易感性预测的可行性，还证明其作为实时防护策略组成部分的有效性。

- move_code：GAP1_CLOSURE_PREVIEW

- statement_status：contribution_claim

- why_here_cn：预告本文如何填补第一缺口，把可行性断言升级为有效性断言。

- inherits_from_previous_cn：承接S2–S3的缺口。

- changes_argument_state_cn：从‘缺口存在’推进到‘本文填补方案’。

- sets_up_next_cn：为S5引出第二缺口。

- failure_if_removed_cn：读者不知道本文与缺口的对应关系。

- evidence_pointer：Introduction P9 S4

### 31. Introduction P9 S5

- order：31

- locator：Introduction P9 S5

- paraphrase_cn：第二，以往钓鱼研究和易感性模型通常关注单一决策或行动，如认为网站合法或愿意交易。

- move_code：GAP2

- statement_status：prior_literature

- why_here_cn：界定第二缺口：把多阶段决策压缩为单一行为。

- inherits_from_previous_cn：承接S1的缺口清单。

- changes_argument_state_cn：把第二缺口具体化。

- sets_up_next_cn：为S6说明多阶段建模的价值。

- failure_if_removed_cn：漏斗因变量的新异性失去对比对象。

- evidence_pointer：Introduction P9 S5

### 32. Introduction P9 S6

- order：32

- locator：Introduction P9 S6

- paraphrase_cn：但落入钓鱼网站攻击涉及一系列相互关联的决策与行动，把这些序列作为一个整体建模会提供更深入洞察。

- move_code：GAP2_RATIONALE

- statement_status：author_inference

- why_here_cn：为第二缺口提供理论理由，直接引出后文漏斗概念。

- inherits_from_previous_cn：承接S5的单一行为局限。

- changes_argument_state_cn：从‘单一行为不够’推进到‘整体序列更好’。

- sets_up_next_cn：为S7的第三缺口作过渡。

- failure_if_removed_cn：漏斗设计的动机断裂。

- evidence_pointer：Introduction P9 S6

### 33. Introduction P9 S7

- order：33

- locator：Introduction P9 S7

- paraphrase_cn：第三，以往易感性模型对反钓鱼工具和威胁相关因素重视不足，尽管这些因素对易感性影响很大。

- move_code：GAP3

- statement_status：prior_literature

- why_here_cn：界定第三缺口：工具与威胁因素被忽略，为PFM三类因素设计提供依据。

- inherits_from_previous_cn：承接S1的缺口清单。

- changes_argument_state_cn：确立第三缺口。

- sets_up_next_cn：直接为第3.1节工具/威胁/用户三类变量设计作引。

- failure_if_removed_cn：TAM/PMT/HITLSF变量选择失去缺口背景。

- evidence_pointer：Introduction P9 S7

## 引言逐段图谱

### 1. Introduction P1

- locator：Introduction P1

- opening_move_cn：用定义+普遍性数据开启：钓鱼是语义攻击且最普遍。

- development_move_cn：引用多个来源说明IT管理者关注、两类受害者（员工与客户）。

- pivot_move_cn：没有明显转折，以‘平均一万人公司年花费370万美元’把问题收束到经济成本。

- closing_move_cn：以成本数字收束，制造‘必须找到更好方案’的需要。

- paragraph_job_cn：建立问题规模、管理相关性与经济后果，为全文设置高利害语境。

### 2. Introduction P2

- locator：Introduction P2

- opening_move_cn：‘多项研究显示用户表现差’开启用户行为证据段。

- development_move_cn：用两组定量证据（40%–80%识别失败、70%愿意交易）累积用户失败证据。

- pivot_move_cn：无转折，直接把‘用户失败’确定为问题核心。

- closing_move_cn：以‘超70%用户愿交易’收束，制造对替代方案的急切需要。

- paragraph_job_cn：单独建立‘用户端失败’这一事实支柱，为‘预测用户’而非‘检测网站’作铺垫。

### 3. Introduction P3

- locator：Introduction P3

- opening_move_cn：先给出常识性方案‘反钓鱼工具’。

- development_move_cn：随后用‘即使用工具成功率仍高’否定该方案。

- pivot_move_cn：转折点在S2的‘然而’。

- closing_move_cn：用个性化缺失解释失效原因，制造‘需要个性化预测’的需要。

- paragraph_job_cn：完成‘工具不足—失效机制—个性化需要’的三步论证，是引言最关键的转折段。

### 4. Introduction P4

- locator：Introduction P4

- opening_move_cn：用‘本研究采取不同方法’直接转向新路径。

- development_move_cn：定义易感性，并列出个性化警告、个性化访问控制、随时间适应三个下游价值。

- pivot_move_cn：段落本身即全文转向点：从预测网站转向预测用户。

- closing_move_cn：以三个用途收束，制造‘值得开发制品’的需要。

- paragraph_job_cn：提出并定义核心新概念（易感性预测），明确与过去研究的差异。

### 5. Introduction P5

- locator：Introduction P5

- opening_move_cn：以‘研究目标是开发设计制品’开启。

- development_move_cn：引入设计科学范式，然后概括PFM的输入（三类因素）、结构（四阶段）与方法（SVOR+自定义核）。

- pivot_move_cn：从目标转向制品介绍。

- closing_move_cn：以‘估计方法’收束，为研究问题与实验作技术铺垫。

- paragraph_job_cn：正式宣布研究对象（PFM制品）及其核心设计要点。

### 6. Introduction P6

- locator：Introduction P6

- opening_move_cn：引用设计科学RQ的一般准则开启。

- development_move_cn：从一般准则收窄到本研究两个RQ。

- pivot_move_cn：‘Accordingly’引向具体RQ。

- closing_move_cn：以RQ1和RQ2收束，制造两个实验的路标。

- paragraph_job_cn：把制品开发转成两个可检验的研究问题。

### 7. Introduction P7

- locator：Introduction P7

- opening_move_cn：‘为回答这些问题’开启评价预告。

- development_move_cn：依次介绍12个月预测实验和3个月干预实验的规模与初步结论。

- pivot_move_cn：从实验1过渡到实验2，暗含‘预测准确是否可转为下游价值’。

- closing_move_cn：以实验2的下游价值收束，为贡献声明作铺垫。

- paragraph_job_cn：建立RQ与两个现场实验的映射，给出全文实证路线图。

### 8. Introduction P8

- locator：Introduction P8

- opening_move_cn：以‘从设计科学看PFM是新颖方案’开启贡献定位。

- development_move_cn：说明新颖性所在，并把贡献归类为improvement，然后指出受众。

- pivot_move_cn：从实验证据转向贡献声明。

- closing_move_cn：以两类受众收束，制造‘这些贡献具体填补什么空隙’的需要。

- paragraph_job_cn：提前给出贡献类型与受众，防止读者把本文读成纯benchmark。

### 9. Introduction P9

- locator：Introduction P9

- opening_move_cn：‘本研究回应三个重要研究缺口’开启清单。

- development_move_cn：逐条展开缺口1（无预测制品）、缺口2（单行为建模）、缺口3（工具与威胁因素被忽略），每条配文献与填补预告。

- pivot_move_cn：从缺口1的IS共识转向缺口2的漏斗动机，再到缺口3的变量选择。

- closing_move_cn：以缺口3收束，直接为第3.1节的三类因素设计铺路。

- paragraph_job_cn：把全部前言论证压缩为三个可回扣的缺口清单，作为讨论部分贡献闭合的靶子。

## 理论到设计逐句图谱

### 1. Section 2 P1 S1–S2

- order：1

- locator：Section 2 P1 S1–S2

- paraphrase_cn：传统反钓鱼研究聚焦工具基准测试与检测能力，但攻击仍成功，研究注意力转向用户易感性。

- move_code：KNOWLEDGE_BASE_SETUP

- statement_status：prior_literature

- why_here_cn：把‘检测技术’定位为已知路线，为‘用户易感性模型’的新路线作知识史铺垫。

- inherits_from_previous_cn：承接引言中‘工具失效’。

- changes_argument_state_cn：确立相关工作中‘用户模型’的地位。

- sets_up_next_cn：为S2–S6逐个介绍HITLSF、AAM、PSF、DRKM、PSM。

- failure_if_removed_cn：相关工作的历史脉络断裂，PFM的增量来源不明。

- evidence_pointer：Related Work Section P1

### 2. Section 2 P2 S1–S4

- order：2

- locator：Section 2 P2 S1–S4

- paraphrase_cn：HITLSF考虑工具相关因素和用户相关因素，这些因素影响访问、浏览和交易可能性。

- move_code：THEORY_INTRO

- statement_status：prior_literature

- why_here_cn：引入第一个知识基础，说明其变量范围与PFM三类因素中‘工具+用户’的对应。

- inherits_from_previous_cn：承接P1的‘用户易感性模型’。

- changes_argument_state_cn：建立HITLSF作为变量体系的重要参照系。

- sets_up_next_cn：为AAM、PSF、DRKM、PSM的对照介绍作起点。

- failure_if_removed_cn：用户/工具因素的设计缺乏权威理论来源。

- evidence_pointer：Related Work P2

### 3. Section 2 P6 S3

- order：3

- locator：Section 2 P6 S3

- paraphrase_cn：PFM从这些既有模型中吸收元素，同时在自变量、多决策阶段、考虑用户异质性的简约估计三方面引入新意。

- move_code：THEORY_TO_DESIGN_BRIDGE

- statement_status：author_inference

- why_here_cn：这是相关工作的收束句，把‘已有模型’与‘PFM增量’明确连接，直接为第3节设计开路。

- inherits_from_previous_cn：承接HITLSF、AAM、PSF、DRKM、PSM的介绍。

- changes_argument_state_cn：从‘文献有哪些’推进到‘PFM在此基础上新增什么’。

- sets_up_next_cn：为第3.1节变量选择和3.2节SVORCK作预告。

- failure_if_removed_cn：PFM与既有模型的关系不清，贡献增量主张落空。

- evidence_pointer：Related Work P6 S3

### 4. Section 3 P1 S1–S2

- order：4

- locator：Section 3 P1 S1–S2

- paraphrase_cn：漏斗长期用于表示完成目标所需的一系列相互关联决策，营销和Web分析中已有成熟应用。

- move_code：DESIGN_METAPHOR

- statement_status：prior_literature

- why_here_cn：为PFM的因变量结构引入‘漏斗’这一成熟隐喻，说明它不是任意设计。

- inherits_from_previous_cn：承接引言缺口2（多阶段建模）。

- changes_argument_state_cn：把‘多阶段序列’正式命名为漏斗。

- sets_up_next_cn：为P2把漏斗映射到钓鱼过程作铺垫。

- failure_if_removed_cn：漏斗概念缺少学科来源，后文四阶段设计显得武断。

- evidence_pointer：Section 3 P1

### 5. Section 3 P2 S1–S3

- order：5

- locator：Section 3 P2 S1–S3

- paraphrase_cn：无论通过邮件、搜索还是社交媒体遇到钓鱼网站，用户面对四个逐步危险的决策：访问、浏览、视为合法、交易。

- move_code：MECHANISM

- statement_status：author_inference

- why_here_cn：把一般漏斗概念落实到钓鱼场景，定义四个因变量阶段。

- inherits_from_previous_cn：承接P1的漏斗隐喻。

- changes_argument_state_cn：确立PFM因变量的四阶段结构。

- sets_up_next_cn：为Figure 1的制品总览和六类变量作铺垫。

- failure_if_removed_cn：因变量结构缺失，第3.2节序数回归没有对象。

- evidence_pointer：Section 3 P2

### 6. Section 3 P2 S8–S9

- order：6

- locator：Section 3 P2 S8–S9

- paraphrase_cn：用户不必到达最后阶段就已暴露风险；攻击者希望把用户推入漏斗越深越好，理想是用户完全避开漏斗。

- move_code：DESIGN_RATIONALE

- statement_status：author_inference

- why_here_cn：解释为何从‘只预测交易’扩张到‘预测整个漏斗’，为多阶段值提供机制理由。

- inherits_from_previous_cn：承接S3的四阶段决策。

- changes_argument_state_cn：把四阶段从描述升级为‘需要被预测’的安全对象。

- sets_up_next_cn：为S7的干预映射（不同阶段不同警告）作铺垫。

- failure_if_removed_cn：‘每阶段都重要’的设计前提缺失，干预分级依据不明。

- evidence_pointer：Section 3 P2

### 7. Section 3 Figure 1 paragraph S1–S4

- order：7

- locator：Section 3 Figure 1 paragraph S1–S4

- paraphrase_cn：Figure 1展示PFM制品：六类因素作为自变量，漏斗阶段作为序数因变量，预测用户-钓鱼遭遇的最终阶段。

- move_code：ARTIFACT_ANNOUNCE

- statement_status：design_decision

- why_here_cn：用图表加文字宣告制品总架构，把前面所有概念整合为一个可计算的输入-输出结构。

- inherits_from_previous_cn：承接P2的漏斗概念。

- changes_argument_state_cn：从‘概念’推进到‘制品蓝图’。

- sets_up_next_cn：为3.1节详述变量和3.2节详述方法作导引。

- failure_if_removed_cn：制品蓝图缺失，读者无法把变量与预测连起来。

- evidence_pointer：Section 3 Figure 1 paragraph

### 8. Section 3.1 P1 S1–S4

- order：8

- locator：Section 3.1 P1 S1–S4

- paraphrase_cn：因没有单一理论框架能涵盖三类因素，本文从TAM、PMT与human-in-the-loop文献取材，并用Table 1总结每个理论如何指导变量选择。

- move_code：THEORY_INTEGRATION

- statement_status：theory_claim

- why_here_cn：为多理论整合给出理由，并预告变量-理论映射表，是理论进入设计的枢纽句。

- inherits_from_previous_cn：承接Figure 1的六类因素。

- changes_argument_state_cn：把‘六类因素’与‘三个理论库’绑定。

- sets_up_next_cn：为3.1.1–3.1.9各小节分别展开理论到变量的推演。

- failure_if_removed_cn：六类变量的理论来源不清，变量体系会被视为拼凑。

- evidence_pointer：Section 3.1 first paragraph

### 9. Section 3.1.1 S1–S5

- order：9

- locator：Section 3.1.1 S1–S5

- paraphrase_cn：TAM认为工具采用与依赖取决于有用性和易用性感知，因此PFM同时采集工具客观性能与感知有用性、所需努力、工具错误成本。

- move_code：THEORY_TO_VARIABLES

- statement_status：theory_claim

- why_here_cn：把TAM命题转成具体的工具信息+工具感知变量，示范‘理论命题→设计选择’的写作模板。

- inherits_from_previous_cn：承接3.1的多理论整合声明。

- changes_argument_state_cn：完成第一组变量的理论合法化。

- sets_up_next_cn：为3.1.2和3.1.3详述工具信息与工具感知。

- failure_if_removed_cn：工具因素变量失去理论锚点，特征消融中工具类特征的贡献无解释力。

- evidence_pointer：Section 3.1.1

### 10. Section 3.1.4 S1–S8

- order：10

- locator：Section 3.1.4 S1–S8

- paraphrase_cn：PMT以威胁评估与应对评估为核心，受环境和先前经验影响；因此PFM纳入威胁严重性、威胁感知、领域、情境和意识。

- move_code：THEORY_TO_VARIABLES

- statement_status：theory_claim

- why_here_cn：把PMT命题转成威胁特征与威胁感知变量，为第二组变量提供理论基础。

- inherits_from_previous_cn：承接3.1的多理论整合。

- changes_argument_state_cn：完成威胁因素的变量合法化。

- sets_up_next_cn：为3.1.5和3.1.6详述威胁特征与威胁感知。

- failure_if_removed_cn：威胁因素变量失去理论依据，威胁特征消融结果无解释。

- evidence_pointer：Section 3.1.4

### 11. Section 3.1.7 S1–S11

- order：11

- locator：Section 3.1.7 S1–S11

- paraphrase_cn：HITLSF认为人口统计、知识与经验会调节警告效果；因此PFM纳入年龄、性别、教育、机构信任、熟悉度和过去损失。

- move_code：THEORY_TO_VARIABLES

- statement_status：theory_claim

- why_here_cn：把HITLSF命题转成人口学与先前网络经验变量，完成第三组用户因素的合法化。

- inherits_from_previous_cn：承接3.1的多理论整合。

- changes_argument_state_cn：完成用户因素的变量体系。

- sets_up_next_cn：为3.1.8和3.1.9详述人口学与先前经验。

- failure_if_removed_cn：人口学/先前经验变量失去理论来源，用户因素消融结果无解释。

- evidence_pointer：Section 3.1.7

### 12. Section 3.1.8 S1–S8

- order：12

- locator：Section 3.1.8 S1–S8

- paraphrase_cn：性别、年龄、教育是少数稳定影响技术使用的人口学变量，且在钓鱼易感性研究中有先例。

- move_code：VARIABLE_JUSTIFICATION

- statement_status：prior_literature

- why_here_cn：逐个人口学变量给出文献支持和机制解释，防止变量选择被批评为任意。

- inherits_from_previous_cn：承接3.1.7的HITLSF人口学主张。

- changes_argument_state_cn：把人口学变量从‘理论声称’落实为‘有证据的变量’。

- sets_up_next_cn：为3.1.9的经验变量作并列铺垫。

- failure_if_removed_cn：人口学变量选择显得武断。

- evidence_pointer：Section 3.1.8

### 13. Section 3.1.9 S1–S11

- order：13

- locator：Section 3.1.9 S1–S11

- paraphrase_cn：信任、熟悉度与过去损失对在线决策有复杂且有时反直觉的影响（如过去损失者反而更易受害）。

- move_code：VARIABLE_JUSTIFICATION

- statement_status：prior_literature

- why_here_cn：为经验类变量提供机制证据，特别用Downs等人的反直觉发现说明变量非线性价值。

- inherits_from_previous_cn：承接3.1.7的先前经验主张。

- changes_argument_state_cn：完成经验变量的理论合法化。

- sets_up_next_cn：为3.2的预测模型奠定完整变量集。

- failure_if_removed_cn：经验变量看似常识化，缺少反直觉证据会削弱其预测独特性。

- evidence_pointer：Section 3.1.9

### 14. Section 3.2 P1 S1–S3

- order：14

- locator：Section 3.2 P1 S1–S3

- paraphrase_cn：四个二元漏斗阶段可各自分类，但跨阶段依赖使单一序数回归更优。

- move_code：MODEL_CHOICE

- statement_status：design_decision

- why_here_cn：在介绍算法前先说明‘为什么一个序数模型而不是四个二元模型’，这是方法写作的关键辩护。

- inherits_from_previous_cn：承接第3节既定的四阶段因变量。

- changes_argument_state_cn：把因变量结构转成模型形式选择。

- sets_up_next_cn：为S4–S8的阈值选择讨论作铺垫。

- failure_if_removed_cn：SVORCK的出现没有动机，读者会问为什么不直接四个分类器。

- evidence_pointer：Section 3.2 P1

### 15. Section 3.2 P1 S4–S8

- order：15

- locator：Section 3.2 P1 S4–S8

- paraphrase_cn：虽然可用等距阈值简化序数模型，但漏斗阶段进展并不等距，因此使用灵活非等距阈值。

- move_code：MODEL_CHOICE

- statement_status：design_decision

- why_here_cn：为‘灵活阈值’辩护，直接支撑后续与CLMM-Equi的对比。

- inherits_from_previous_cn：承接S3的序数回归选择。

- changes_argument_state_cn：把‘序数回归’具体化为‘非等距阈值序数回归’。

- sets_up_next_cn：为S9–S12介绍核方法与SVORCK作铺垫。

- failure_if_removed_cn：CLMM-Equi对照失去设计理由。

- evidence_pointer：Section 3.2 P1 S4–S8

### 16. Section 3.2 P2 S1–S4

- order：16

- locator：Section 3.2 P2 S1–S4

- paraphrase_cn：核方法在IS中用于从噪声数据提取模式并纳入理论驱动设计，因此本文提出带复合核的SVORCK。

- move_code：METHOD_JUSTIFICATION

- statement_status：prior_literature

- why_here_cn：把SVORCK放在IS核方法传统中，说明复合核能承载PFM的关键元素（变量、漏斗阶段、灵活阈值）。

- inherits_from_previous_cn：承接S8的灵活阈值需要。

- changes_argument_state_cn：从‘需要序数模型’推进到‘需要能嵌入PFM结构的核方法’。

- sets_up_next_cn：为Eq.(1)的复合核定义作铺垫。

- failure_if_removed_cn：SVORCK变成无文献传统的任意算法选择。

- evidence_pointer：Section 3.2 P2

### 17. Section 3.2 Eq.(4) discussion

- order：17

- locator：Section 3.2 Eq.(4) discussion

- paraphrase_cn：CLMM通过随机效应捕捉同一用户的重复测量依赖，这是复合核能‘考虑用户异质性’的关键机制。

- move_code：MECHANISM

- statement_status：theory_claim

- why_here_cn：解释算法内部构造与‘用户异质性’的设计目标如何对应，把统计机制转成设计语言。

- inherits_from_previous_cn：承接K_Funnel核的提出。

- changes_argument_state_cn：把‘考虑用户异质性’从口号落实为随机效应结构。

- sets_up_next_cn：为实验中的PFM-SVORCK vs PFM-CLMM对比作理论铺垫。

- failure_if_removed_cn：用户异质性主张无统计支撑，SVORCK较CLMM的增量来源不明。

- evidence_pointer：Section 3.2 Eq.(4) and surrounding text

### 18. Section 3.2 final paragraph

- order：18

- locator：Section 3.2 final paragraph

- paraphrase_cn：后续实验将报告SVORCK和CLMM两种估计，预期CLMM已优于比较方法，而SVORCK进一步显著提升。

- move_code：RESULT_PREVIEW

- statement_status：author_inference

- why_here_cn：提前预告两种估计的预期关系，为读者建立评价预期。

- inherits_from_previous_cn：承接复合核与CLMM的介绍。

- changes_argument_state_cn：从‘设计完成’推进到‘即将评价’。

- sets_up_next_cn：为第5节实验作直接铺垫。

- failure_if_removed_cn：SVORCK与CLMM的结果对比缺少预告，读者会感到突然。

- evidence_pointer：Section 3.2 final paragraph

## 制品设计理由逐句图谱

### 1. Section 3 Figure 1 paragraph S4

- order：1

- locator：Section 3 Figure 1 paragraph S4

- paraphrase_cn：易感性被预测为一个序数响应，表示给定用户-钓鱼遭遇的最终漏斗阶段。

- move_code：ARTIFACT_LOGIC

- statement_status：design_decision

- why_here_cn：把‘预测什么’精确表述为序数因变量，是漏斗概念可计算化的关键设计决定。

- inherits_from_previous_cn：承接Figure 1的输入输出结构。

- changes_argument_state_cn：确立因变量的统计类型。

- sets_up_next_cn：为3.2的序数回归方法作铺垫。

- failure_if_removed_cn：因变量类型不清，后续AUC/ROC评价无对象。

- evidence_pointer：Section 3 Figure 1 paragraph S4

### 2. Section 3.1.1 S5

- order：2

- locator：Section 3.1.1 S5

- paraphrase_cn：与TAM一致，用户对反钓鱼工具的依赖应取决于有用性、所需努力和工具错误成本。

- move_code：ARTIFACT_LOGIC

- statement_status：theory_claim

- why_here_cn：把TAM命题落成PFM的工具感知变量设计，说明‘为什么这些变量在制品里’。

- inherits_from_previous_cn：承接S1–S4的TAM介绍。

- changes_argument_state_cn：把理论命题转成制品内变量要求。

- sets_up_next_cn：为后续工具因素变量操作化作引。

- failure_if_removed_cn：工具感知变量的存在理由缺失。

- evidence_pointer：Section 3.1.1 S5

### 3. Section 3.1.4 S8

- order：3

- locator：Section 3.1.4 S8

- paraphrase_cn：与PMT一致，用户穿越漏斗阶段的易感性将由这些威胁因素预测。

- move_code：ARTIFACT_LOGIC

- statement_status：theory_claim

- why_here_cn：把PMT命题转成‘威胁因素进预测模型’的设计逻辑。

- inherits_from_previous_cn：承接PMT的威胁评估论述。

- changes_argument_state_cn：把威胁因素从‘解释变量’确立为‘预测变量’。

- sets_up_next_cn：为威胁特征与威胁感知的子类详述作引。

- failure_if_removed_cn：威胁因素在预测模型中的地位不清。

- evidence_pointer：Section 3.1.4 S8

### 4. Section 3.1.3 S13

- order：4

- locator：Section 3.1.3 S13

- paraphrase_cn：工具错误感知成本可能与实际错误不完全相关，有的用户感知远高于他人。

- move_code：ARTIFACT_LOGIC

- statement_status：prior_literature

- why_here_cn：说明为何需要主观感知变量而非只用客观工具性能，为‘感知数据不可省’作铺垫。

- inherits_from_previous_cn：承接S8–S12的工具错误成本讨论。

- changes_argument_state_cn：把工具因素从纯客观扩充为主观感知。

- sets_up_next_cn：为第5.2.2节感知特征重要性分析埋下伏笔。

- failure_if_removed_cn：感知变量与客观变量的区分失去理论依据。

- evidence_pointer：Section 3.1.3 S13

### 5. Section 3.1.6 S1–S3

- order：5

- locator：Section 3.1.6 S1–S3

- paraphrase_cn：用户对威胁的感知与判断是任何决策行动的先决条件；感知严重性越高，保护行为越可能。

- move_code：ARTIFACT_LOGIC

- statement_status：theory_claim

- why_here_cn：为威胁感知变量提供机制解释，证明它们是预测漏斗阶段的有意义输入。

- inherits_from_previous_cn：承接3.1.4的PMT。

- changes_argument_state_cn：把‘威胁感知’确立为制品变量类别。

- sets_up_next_cn：为3.1.7转向用户因素作过渡。

- failure_if_removed_cn：威胁感知变量在消融中的贡献缺解释。

- evidence_pointer：Section 3.1.6

### 6. Section 3.1.9 S9–S11

- order：6

- locator：Section 3.1.9 S9–S11

- paraphrase_cn：过去损失按‘傻两次’逻辑应降低易感性，但Downs发现相反：有损失经历者更易受害。

- move_code：ARTIFACT_LOGIC

- statement_status：prior_literature

- why_here_cn：用反直觉证据说明用户异质性因素不能按常识剔除，强化纳入‘过去损失’的设计决定。

- inherits_from_previous_cn：承接S5–S8的熟悉度讨论。

- changes_argument_state_cn：为先前经验变量建立非平凡价值。

- sets_up_next_cn：为3.2的用户异质性建模（随机效应）作铺垫。

- failure_if_removed_cn：过去损失变量显得非必要。

- evidence_pointer：Section 3.1.9 S9–S11

### 7. Section 3.2 P2 S2–S3

- order：7

- locator：Section 3.2 P2 S2–S3

- paraphrase_cn：由于每个阶段在下一步决策上损耗，漏斗被建模为五个序数端点；CLMM提供阶段概率向量以构成漏斗核。

- move_code：ARTIFACT_LOGIC

- statement_status：design_decision

- why_here_cn：说明‘漏斗结构’如何通过CLMM概率向量进入核函数，是制品形式化的核心句。

- inherits_from_previous_cn：承接S1–S3的序数回归选择。

- changes_argument_state_cn：把概念漏斗转成可计算核。

- sets_up_next_cn：为Eq.(1)–(6)的核定义作铺垫。

- failure_if_removed_cn：复合核的K_Funnel部分无设计动机。

- evidence_pointer：Section 3.2 P2

### 8. Section 5.2 P1 S4

- order：8

- locator：Section 5.2 P1 S4

- paraphrase_cn：除SVORCK外，还评估了一个不带复合核的CLMM模型，以检验复合核的增量价值。

- move_code：ARTIFACT_RATIONALIZATION_IN_EVAL

- statement_status：method_decision

- why_here_cn：在实验设计上专门为‘复合核’设置剥离对照，把制品内部构件变成可证伪的证据点。

- inherits_from_previous_cn：承接P1的三模型比较。

- changes_argument_state_cn：把‘复合核有价值’变成可检验命题。

- sets_up_next_cn：为Table 5中SVORCK vs CLMM对比作铺垫。

- failure_if_removed_cn：复合核增量主张缺乏对照组。

- evidence_pointer：Section 5.2 P1 S4

### 9. Section 6.1 S6–S8

- order：9

- locator：Section 6.1 S6–S8

- paraphrase_cn：预测不访问显示默认警告，预测访问/浏览显示中严重度警告，预测视为合法/意图交易显示高严重度警告。

- move_code：ARTIFACT_LOGIC

- statement_status：design_decision

- why_here_cn：把PFM的漏斗阶段预测直接映射到三级警告干预，是‘预测驱动干预’的机制落地。

- inherits_from_previous_cn：承接S3的六设置随机分组。

- changes_argument_state_cn：从‘能预测漏斗阶段’推进到‘按阶段分级警告’。

- sets_up_next_cn：为S9–S12的随机设置对照作铺垫。

- failure_if_removed_cn：干预实验的分级警告设计失去制品依据。

- evidence_pointer：Section 6.1 S6–S8

### 10. Section 6.1 S9–S12

- order：10

- locator：Section 6.1 S9–S12

- paraphrase_cn：为控制新警告类型本身引起的行为变化，加入随机设置，其警告比例依据12个月观测漏斗分布。

- move_code：ARTIFACT_RATIONALIZATION_IN_EVAL

- statement_status：method_decision

- why_here_cn：说明随机设置作为对照的逻辑：把‘警告对齐性’与‘警告出现数量/类型’分离。

- inherits_from_previous_cn：承接S6–S8的分级警告设计。

- changes_argument_state_cn：把干预效果的可替代解释（新警告更显眼）预先排除。

- sets_up_next_cn：为第6.2.2节的警告数量稳健性分析作铺垫。

- failure_if_removed_cn：PFM干预效果可能被解释为‘只是换了更显眼警告’。

- evidence_pointer：Section 6.1 S9–S12

## Study开头、过渡与收束图谱

### 1. Section 4 opening P1

- locator：Section 4 opening P1

- paraphrase_cn：为回答研究问题，我们开展两个纵向现场实验，总结在Table 2；RQ1对应12个月预测实验，RQ2对应3个月干预实验。

- move_code：OVERALL_EVALUATION_ROADMAP

- statement_status：method_decision

- why_here_cn：在方法章节开头给出全文评价路线图，把RQ与实验一一对应。

- inherits_from_previous_cn：承接引言RQ1/RQ2。

- changes_argument_state_cn：从‘问题’进入‘评价设计’。

- sets_up_next_cn：为第5和第6节分别展开实验作路标。

- failure_if_removed_cn：读者在实验中迷失RQ对应关系。

- evidence_pointer：Section 4 P1

### 2. Section 5 opening P1 S1–S2

- locator：Section 5 opening P1 S1–S2

- paraphrase_cn：为回答RQ1开展12个月纵向现场实验；纵向设计用于捕捉用户感知、威胁遭遇和工具交互随时间的变化。

- move_code：STUDY_OPENING

- statement_status：method_decision

- why_here_cn：解释为什么必须用纵向设计而非横截面，直接服务RQ1的‘随时间’。

- inherits_from_previous_cn：承接RQ1。

- changes_argument_state_cn：确立实验1的时间结构。

- sets_up_next_cn：为5.1的窗口式训练/测试作铺垫。

- failure_if_removed_cn：12个月的时间跨度无理由，窗口式评价失去依据。

- evidence_pointer：Section 5 opening

### 3. Section 5 pretest paragraph

- locator：Section 5 pretest paragraph

- paraphrase_cn：作为现场实验前奏，先做了两个实验室预试验，在大学和安全软件B2C客户中复验，用于验证变量选择、问卷题项与操作化。

- move_code：PRETEST_JUSTIFICATION

- statement_status：method_decision

- why_here_cn：在大型现场实验前用小规模预试验检验测量工具，防止现场数据无效。

- inherits_from_previous_cn：承接第3节的变量体系。

- changes_argument_state_cn：把测量从‘理论设计’推进到‘信效度检验’。

- sets_up_next_cn：为5.1的现场收集作漏斗前置。

- failure_if_removed_cn：问卷题项与操作化缺少验证，后续结果可能受测量噪声污染。

- evidence_pointer：Section 5 pretest paragraph

### 4. Section 5.1 design S1–S6

- locator：Section 5.1 design S1–S6

- paraphrase_cn：FinOrg和LegOrg的工作电脑分别配备企业级端点安全方案，均对潜在钓鱼URL显示显著警告。

- move_code：SETTING_DESCRIPTION

- statement_status：empirical_result

- why_here_cn：描述工具环境，为工具因素的客观变量（检测率、处理时间、警告）提供现场来源。

- inherits_from_previous_cn：承接Section 5的总体设计。

- changes_argument_state_cn：确立实验1的技术环境。

- sets_up_next_cn：为Table 4的操作化表作铺垫。

- failure_if_removed_cn：工具因素变量没有现场落地。

- evidence_pointer：Section 5.1 S1–S6

### 5. Section 5.1 potential phish operationalization S7–S12

- locator：Section 5.1 potential phish operationalization S7–S12

- paraphrase_cn：因现场需实时判定潜在钓鱼，URL若被端点工具判为钓鱼或出现在可靠钓鱼数据库中即作为潜在钓鱼；测量不完美但有误差控制。

- move_code：OPERATIONALIZATION

- statement_status：method_decision

- why_here_cn：解释‘49,373次交互’是如何实时定义的，并主动承认分类误差，防止审稿人质疑数据生成过程。

- inherits_from_previous_cn：承接上述端点工具描述。

- changes_argument_state_cn：把模糊的‘钓鱼遭遇’操作化为可判定事件。

- sets_up_next_cn：为漏斗阶段记录（点击流、弹窗）作铺垫。

- failure_if_removed_cn：现场数据集的合法性存疑。

- evidence_pointer：Section 5.1 S7–S12

### 6. Section 5.1 funnel stage measurement S13–S21

- locator：Section 5.1 funnel stage measurement S13–S21

- paraphrase_cn：访问和浏览由点击流自动记录，浏览定义为点击站内链接或停留30秒；会话后用弹窗询问是否视为合法/意图交易。

- move_code：OPERATIONALIZATION

- statement_status：method_decision

- why_here_cn：把四个漏斗阶段逐一操作化，特别是说明哪些由日志客观记录、哪些由弹窗自报。

- inherits_from_previous_cn：承接潜在钓鱼判定。

- changes_argument_state_cn：把概念上的四阶段变成可测量变量。

- sets_up_next_cn：为5.2.3的弹窗Hawthorne检验作铺垫。

- failure_if_removed_cn：因变量测量不透明，结果无法解释。

- evidence_pointer：Section 5.1 funnel stage measurement

### 7. Section 5.1 windowed approach S22–S26

- locator：Section 5.1 windowed approach S22–S26

- paraphrase_cn：预测使用滚动窗口：前三个月训练、后三个月测试，每窗口前用季度调查更新感知变量。

- move_code：WINDOWED_EVALUATION

- statement_status：method_decision

- why_here_cn：规定外样本评价方式，使AUC可比较且接近实际部署场景，避免时间泄漏。

- inherits_from_previous_cn：承接纵向设计动机。

- changes_argument_state_cn：把‘随时间预测’落实为窗口式训练/测试。

- sets_up_next_cn：为5.2的所有模型/方法比较提供统一评价框架。

- failure_if_removed_cn：预测性能可能被时间泄漏夸大。

- evidence_pointer：Section 5.1 windowed approach

### 8. Section 5.2 results opening P1–P3

- locator：Section 5.2 results opening P1–P3

- paraphrase_cn：两项分析：先与DRKM/AAM/HITLSF比较（都用CLMM+灵活阈值训练保证公平），再用相同PFM变量与BayesNet/SVM/SVOR/CLMM-Equi/LMM比较。

- move_code：BENCHMARK_LAYERING

- statement_status：method_decision

- why_here_cn：建立两层benchmark设计：变量组合层和算法层，分别回答‘变量集是否有贡献’和‘方法是否有贡献’。

- inherits_from_previous_cn：承接窗口式评价框架。

- changes_argument_state_cn：把单一比较拆成两个独立维度的对照。

- sets_up_next_cn：为Table 5与Figure 4的结果作铺垫。

- failure_if_removed_cn：PFM优势无法分解为‘因变量设计优于’和‘算法优于’。

- evidence_pointer：Section 5.2 P1–P3

### 9. Section 5.2 results P4 S1–S6

- locator：Section 5.2 results P4 S1–S6

- paraphrase_cn：PFM-SVORCK和PFM-CLMM的AUC显著高于三个比较模型22%–35%、高于其他方法8%–25%，SVORCK比CLMM高4个百分点。

- move_code：MAIN_RESULT

- statement_status：empirical_result

- why_here_cn：报告RQ1的核心预测结果，并指出因变量与方法都有实质影响且前者略大。

- inherits_from_previous_cn：承接两层benchmark设计。

- changes_argument_state_cn：把预测优势确立为实证事实。

- sets_up_next_cn：为5.2.1的高严重度分析和5.2.2的特征分析作铺垫。

- failure_if_removed_cn：RQ1无主结果，后续分析失去支撑。

- evidence_pointer：Section 5.2 P4; Table 5; Figure 4

### 10. Section 5.2 P5–P6 intention/observed transaction result

- locator：Section 5.2 P5–P6 intention/observed transaction result

- paraphrase_cn：PFM正确预测90%–94%的意图交易及其中的实际交易，显著优于最接近竞争者。

- move_code：RESULT_EXTENSION

- statement_status：empirical_result

- why_here_cn：把预测优势从AUC落实到‘意图-行为’两个尖峰端点，回应漏斗最后阶段的重要性。

- inherits_from_previous_cn：承接Table 5的AUC结果。

- changes_argument_state_cn：从总体AUC推进到端点阶段的实际正确预测。

- sets_up_next_cn：为高严重度分析和成本收益分析铺垫。

- failure_if_removed_cn：预测优势停留在抽象曲线，缺乏业务相关端点证据。

- evidence_pointer：Section 5.2 P5–P6; Figure 6

### 11. Section 5.2.1 opening S1–S5

- locator：Section 5.2.1 opening S1–S5

- paraphrase_cn：针对含恶意软件的高严重度URL，PFM正确预测96%的访问，且跨邮件/社交媒体/搜索渠道稳健。

- move_code：RESULT_HIGH_STAKES

- statement_status：empirical_result

- why_here_cn：单独设立小节突出‘最危险威胁’上的表现，把预测精度转成安全含义。

- inherits_from_previous_cn：承接总AUC结果。

- changes_argument_state_cn：把预测优势推广到高严重度与多通道场景。

- sets_up_next_cn：为Table 6的通道AUC和解释段落作铺垫。

- failure_if_removed_cn：高严重度主张无证据；也削弱后文‘实践意义’。

- evidence_pointer：Section 5.2.1; Figure 7

### 12. Section 5.2.1 explanation paragraph S1–S6

- locator：Section 5.2.1 explanation paragraph S1–S6

- paraphrase_cn：个人邮件和社交媒体略低可能因为威胁特征更多样、存在社交钓鱼等未纳入线索；PFM未把通道作为特征。

- move_code：BOUNDARY_EXPLANATION

- statement_status：author_inference

- why_here_cn：主动解释弱通道差异，防止被读成‘PFM不稳定’，并坦诚指出未来方向。

- inherits_from_previous_cn：承接Table 6的通道AUC。

- changes_argument_state_cn：把边界表现转成可理解的机制说明。

- sets_up_next_cn：为未来工作的通道特征作伏笔。

- failure_if_removed_cn：通道性能差异无解释，稳健性声称存疑。

- evidence_pointer：Section 5.2.1 explanation

### 13. Section 5.2.2 opening S1–S7

- locator：Section 5.2.2 opening S1–S7

- paraphrase_cn：特征消融显示移除工具性能、工具感知、威胁特征、先前经验和人口学均显著降低AUC；威胁感知仅在SVORCK中显著。

- move_code：FEATURE_ABLATION_RESULT

- statement_status：empirical_result

- why_here_cn：用消融证明六类特征对预测的贡献，把制品设计选择变成经验证据。

- inherits_from_previous_cn：承接PFM六类因素的设计。

- changes_argument_state_cn：从‘设计包含六类’推进到‘每类都有实证必要’。

- sets_up_next_cn：为特征集比较和RFE作铺垫。

- failure_if_removed_cn：六类特征的设计无法被验证，可能被批评为冗余。

- evidence_pointer：Section 5.2.2; Table 7

### 14. Section 5.2.2 feature set comparison S1–S14

- locator：Section 5.2.2 feature set comparison S1–S14

- paraphrase_cn：仅用观察特征AUC大幅下降，加入先前日志只部分补偿；加入所有竞争模型调查变量也无提升。

- move_code：FEATURE_SET_RESULT

- statement_status：empirical_result

- why_here_cn：证明PFM的感知/调查特征不可替代，且PFM变量集比‘所有竞争变量总和’更简洁有效。

- inherits_from_previous_cn：承接Table 7消融。

- changes_argument_state_cn：把‘每类特征有贡献’升级为‘PFM的特征组合最优’。

- sets_up_next_cn：为RFE特征选择分析作铺垫。

- failure_if_removed_cn：变量体系优势的完整论证缺失。

- evidence_pointer：Section 5.2.2; Table 8

### 15. Section 5.2.2 RFE paragraph S15–S20

- locator：Section 5.2.2 RFE paragraph S15–S20

- paraphrase_cn：RFE特征选择显示PFM外的额外变量未进入前12排名，说明PFM变量集本身已足够。

- move_code：FEATURE_SELECTION_RESULT

- statement_status：empirical_result

- why_here_cn：用特征选择结果进一步排除‘增加变量总更好’的替代解释。

- inherits_from_previous_cn：承接Table 8特征集比较。

- changes_argument_state_cn：把变量体系主张推向‘简约且充分’。

- sets_up_next_cn：为讨论中的‘减少问卷长度’未来方向作铺垫。

- failure_if_removed_cn：变量最优性主张缺最后一道证据。

- evidence_pointer：Section 5.2.2 RFE paragraph

### 16. Section 5.2.3 opening S1–S6

- locator：Section 5.2.3 opening S1–S6

- paraphrase_cn：季度调查和弹窗可能改变行为（Hawthorne效应），但月度漏斗图显示无调查前后模式。

- move_code：ROBUSTNESS_QUARTERLY_SURVEY

- statement_status：empirical_result

- why_here_cn：逐一排除设计本身对行为的干扰，保护前揭结果的内部效度。

- inherits_from_previous_cn：承接实验设计中的季度调查。

- changes_argument_state_cn：排除‘调查造成行为改变’的替代解释。

- sets_up_next_cn：为弹窗的pilot研究作铺垫。

- failure_if_removed_cn：结果可能被归因于测量方式而非PFM。

- evidence_pointer：Section 5.2.3; Figure 8

### 17. Section 5.2.3 pilot study paragraph S7–S21

- locator：Section 5.2.3 pilot study paragraph S7–S21

- paraphrase_cn：3个月pilot研究将205名员工随机分到弹窗/无弹窗组，两组在访问、浏览、实际交易上无显著差异，弹窗行为改变担忧缓解。

- move_code：ROBUSTNESS_PILOT

- statement_status：empirical_result

- why_here_cn：用独立随机对照消除‘弹窗引起行为变化’的威胁，同时承认自报阶段仍有响应偏差。

- inherits_from_previous_cn：承接季度调查稳健性结论。

- changes_argument_state_cn：把主要测量干扰排除，并诚实标注残余偏差。

- sets_up_next_cn：为第6节干预实验作准备。

- failure_if_removed_cn：弹窗干扰无法排除，干预实验前的基线可信度受损。

- evidence_pointer：Section 5.2.3; Figure 9

### 18. Section 6 opening S1–S6

- locator：Section 6 opening S1–S6

- paraphrase_cn：第二个RQ问预测驱动干预能否改善回避结果；因此在同一两家组织做3个月纵向多变量现场实验，1,218人参与。

- move_code：STUDY2_TRANSITION

- statement_status：method_decision

- why_here_cn：从预测实验过渡到干预实验，用RQ2明确‘下游价值’作为原由。

- inherits_from_previous_cn：承接实验1的样本与结果。

- changes_argument_state_cn：把评价重点从‘能预测’转向‘预测是否有用’。

- sets_up_next_cn：为6.1的六设置设计作铺垫。

- failure_if_removed_cn：实验2缺动机，会被视为重复。

- evidence_pointer：Section 6 opening

### 19. Section 6.1 design S1–S5

- locator：Section 6.1 design S1–S5

- paraphrase_cn：参与者随机分配到六种设置：PFM-SVORCK、PFM-CLMM、SVM、HITLSF、随机、标准；前四组按预测易感性显示默认/中/高三级警告。

- move_code：STUDY2_DESIGN

- statement_status：method_decision

- why_here_cn：把RQ2转成随机对照设计，并纳入随机/标准两个对照以隔离‘对齐性’效果。

- inherits_from_previous_cn：承接Section 6的过渡。

- changes_argument_state_cn：确立实验2的因果识别结构。

- sets_up_next_cn：为6.2的结果与ANOVA作铺垫。

- failure_if_removed_cn：干预效果无法归因，因果主张不成立。

- evidence_pointer：Section 6.1 S1–S5

### 20. Section 6.2 results S1–S8

- locator：Section 6.2 results S1–S8

- paraphrase_cn：PFM设置下用户较少穿越各漏斗阶段，高层级阶段比SVM/HITLSF/标准好7–20个百分点，实际交易率低至标准的三分之一到六分之一。

- move_code：STUDY2_MAIN_RESULT

- statement_status：empirical_result

- why_here_cn：报告干预实验主结果，并把随机设置劣于标准解释为‘不对齐的警告无效’。

- inherits_from_previous_cn：承接六设置设计。

- changes_argument_state_cn：确立RQ2的答案。

- sets_up_next_cn：为ANOVA统计检验作铺垫。

- failure_if_removed_cn：RQ2无核心行为证据。

- evidence_pointer：Section 6.2; Figure 10

### 21. Section 6.2 ANOVA paragraph S9–S17

- locator：Section 6.2 ANOVA paragraph S9–S17

- paraphrase_cn：ANOVA显示六设置在每阶段显著不同；Bonferroni对比显示PFM均值显著优于非PFM设置，且SVORCK在多数阶段优于CLMM。

- move_code：STATISTICAL_INFERENCE

- statement_status：empirical_result

- why_here_cn：用统计检验把描述性差异升格为推断性结论，并给出SVORCK vs CLMM的组内比较。

- inherits_from_previous_cn：承接Figure 10的描述性差异。

- changes_argument_state_cn：把‘看起来更好’推进为‘统计上更优’。

- sets_up_next_cn：为成本收益分析作铺垫。

- failure_if_removed_cn：行为差异可能被归因于抽样噪声。

- evidence_pointer：Section 6.2 ANOVA paragraph

### 22. Section 6.2.1 opening S1–S3

- locator：Section 6.2.1 opening S1–S3

- paraphrase_cn：设计科学文献认为成本收益分析适合评估现场部署制品的实践价值；货币收益可量化为减少漏斗穿越的节省。

- move_code：COST_BENEFIT_OPENING

- statement_status：method_decision

- why_here_cn：为成本收益分析提供方法论正当性，并把行为指标映射为货币指标。

- inherits_from_previous_cn：承接干预行为结果。

- changes_argument_state_cn：从‘行为改善’推进到‘经济评估’。

- sets_up_next_cn：为S4–S10的成本参数作铺垫。

- failure_if_removed_cn：经济价值主张缺少方法论理由。

- evidence_pointer：Section 6.2.1 S1–S3

### 23. Section 6.2.1 cost parameters S4–S10

- locator：Section 6.2.1 cost parameters S4–S10

- paraphrase_cn：FinOrg估计避免一次访问节省约70美元、一次浏览节省1.5小时、避免一次交易节省约1,000美元；不必要的高严重度警告每次成本约50美元。

- move_code：COST_PARAMETERS

- statement_status：empirical_result

- why_here_cn：给出货币化所需参数及其来源（FinOrg估计、行业报告），让成本收益计算可审计。

- inherits_from_previous_cn：承接S1–S3的货币化框架。

- changes_argument_state_cn：把行为差异转成可计算的美元值。

- sets_up_next_cn：为Table 9的结果作铺垫。

- failure_if_removed_cn：成本收益数字变成无依据的外推。

- evidence_pointer：Section 6.2.1 S4–S10

### 24. Section 6.2.1 Table 9 discussion S11–S21

- locator：Section 6.2.1 Table 9 discussion S11–S21

- paraphrase_cn：以10,000员工公司外推，PFM-SVORCK每员工年收益约1,960美元，PFM-CLMM约1,454美元，SVM约68美元，HITLSF约-198美元，随机约-1,284美元。

- move_code：COST_BENEFIT_RESULT

- statement_status：empirical_result

- why_here_cn：用美元数字统帅各设置的相对价值，把干预实验结论翻译成管理语言。

- inherits_from_previous_cn：承接S4–S10的成本参数。

- changes_argument_state_cn：确立PFM的经济价值主张。

- sets_up_next_cn：为敏感性分析作铺垫。

- failure_if_removed_cn：经济价值声明缺核心表格证据。

- evidence_pointer：Section 6.2.1 Table 9 discussion

### 25. Section 6.2.1 sensitivity S22–S29

- locator：Section 6.2.1 sensitivity S22–S29

- paraphrase_cn：敏感性分析在收益降低40%、成本提高40%的极端情形下，PFM-SVORCK仍保持每员工超1,000美元年收益，而比较方法产生亏损。

- move_code：SENSITIVITY_ANALYSIS

- statement_status：empirical_result

- why_here_cn：检验经济主张对成本假设的稳健性，防止‘收益来自乐观参数’的批评。

- inherits_from_previous_cn：承接Table 9基线收益。

- changes_argument_state_cn：把经济主张升级为‘在宽范围假设下仍成立’。

- sets_up_next_cn：为6.2.2的警告数量稳健性作铺垫。

- failure_if_removed_cn：经济结论可能因参数脆弱而崩溃。

- evidence_pointer：Section 6.2.1 sensitivity; Figure 11

### 26. Section 6.2.2 robustness S1–S7

- locator：Section 6.2.2 robustness S1–S7

- paraphrase_cn：六组警告总数无显著差异，PFM组并非高严重度警告最多，因此行为改善不是警告数量造成，而是预测对齐性造成。

- move_code：WARNING_COUNT_ROBUSTNESS

- statement_status：empirical_result

- why_here_cn：用警告数量分布检验排除‘干预效果只是更多警告’的替代解释，强化个性化机制。

- inherits_from_previous_cn：承接干预行为结果。

- changes_argument_state_cn：把机制解释从‘更多警告’锁定为‘对齐易感性’。

- sets_up_next_cn：为第7节讨论作铺垫。

- failure_if_removed_cn：个性化机制主张无防护，可能被简化为警告频率效应。

- evidence_pointer：Section 6.2.2; Figure 12

## 讨论与贡献逐句图谱

### 1. Section 7.1 P1 S1–S3

- order：1

- locator：Section 7.1 P1 S1–S3

- paraphrase_cn：实验证明PFM的效用；管理者需要多管齐下的安全方法；Table 10总结关键发现。

- move_code：RESULTS_SUMMARY_OPENING

- statement_status：empirical_result

- why_here_cn：讨论开头先回纳所有实证结果，并给出总表，防止贡献声明悬空。

- inherits_from_previous_cn：承接实验1和实验2的全部结果。

- changes_argument_state_cn：从‘单个结果’升级为‘整体证据链’的总结。

- sets_up_next_cn：为RQ1/RQ2逐条回答案作铺垫。

- failure_if_removed_cn：讨论缺乏对证据的完整性回纳。

- evidence_pointer：Section 7.1 P1

### 2. Section 7.1 RQ1 answer S4–S6

- order：2

- locator：Section 7.1 RQ1 answer S4–S6

- paraphrase_cn：实验1显示PFM在组织中显著优于竞争模型，AUC高8%–52%，高严重度访问预测96%；窗口式方法支持随时间适应。

- move_code：RQ1_ANSWER

- statement_status：empirical_result

- why_here_cn：把RQ1的答案浓缩为三个数字型结论，并补上‘随时间适应’的解释性转译。

- inherits_from_previous_cn：承接Table 10与实验1结果。

- changes_argument_state_cn：完成对引言RQ1的闭合。

- sets_up_next_cn：为RQ2回答作并列铺垫。

- failure_if_removed_cn：RQ1未在讨论中闭合，引言缺口1悬而未决。

- evidence_pointer：Section 7.1 S4–S6

### 3. Section 7.1 RQ2 answer S7–S10

- order：3

- locator：Section 7.1 RQ2 answer S7–S10

- paraphrase_cn：实验2显示个性化实时易感性预测驱动的警告与用户易感性更一致，用户穿越减少，交易概率降至三分之一到一半。

- move_code：RQ2_ANSWER

- statement_status：empirical_result

- why_here_cn：把RQ2的答案与引言P3的‘警告未个性化’呼应，建立机制闭环。

- inherits_from_previous_cn：承接实验2的干预结果。

- changes_argument_state_cn：完成对RQ2的闭合，并把‘个性化’机制重新拉回论证。

- sets_up_next_cn：为S11–S14的更大图景与应用设想作铺垫。

- failure_if_removed_cn：RQ2未回扣，个性化机制主张缺少闭环。

- evidence_pointer：Section 7.1 S7–S10

### 4. Section 7.1 implications S11–S14

- order：4

- locator：Section 7.1 implications S11–S14

- paraphrase_cn：结果支持主动识别易感用户和个性化实时警告/访问控制的更大图景；FinOrg和LegOrg正探索实时阻断等保护措施。

- move_code：PRACTICAL_EXTENSION

- statement_status：author_inference

- why_here_cn：把两个RQ答案外推为组织安全政策设想，并用‘企业正在探索’增强可行性。

- inherits_from_previous_cn：承接RQ1/RQ2答案。

- changes_argument_state_cn：从‘能预测、干预有效’推进到‘可落地部署’。

- sets_up_next_cn：为7.2的贡献声明作铺垫。

- failure_if_removed_cn：实践含义停留在抽象层面，缺少应用想象。

- evidence_pointer：Section 7.1 S11–S14

### 5. Section 7.2 contribution intro S1–S2

- order：5

- locator：Section 7.2 contribution intro S1–S2

- paraphrase_cn：本文提出PFM作为预测设计制品，贡献有三方面。

- move_code：CONTRIBUTION_OPENING

- statement_status：contribution_claim

- why_here_cn：正式进入贡献清单，明确三事项。

- inherits_from_previous_cn：承接7.1的实证总结。

- changes_argument_state_cn：从‘结果’升级为‘贡献声明’。

- sets_up_next_cn：为逐条贡献展开作导引。

- failure_if_removed_cn：贡献主张无总括，读者难以把握。

- evidence_pointer：Section 7.2 S1–S2

### 6. Section 7.2 contribution 1 S3–S5

- order：6

- locator：Section 7.2 contribution 1 S3–S5

- paraphrase_cn：第一贡献：开发PFM制品，含漏斗机制、理论驱动的变量集和SVORCK估计方法。

- move_code：CONTRIBUTION_1

- statement_status：contribution_claim

- why_here_cn：把制品本身声明为贡献，并重述其三个构成元素（漏斗、理论变量、SVORCK）。

- inherits_from_previous_cn：承接S2的贡献清单。

- changes_argument_state_cn：确立制品层面的知识贡献。

- sets_up_next_cn：为第二个贡献（评价）作铺垫。

- failure_if_removed_cn：‘设计了什么’这一贡献无声明。

- evidence_pointer：Section 7.2 S3–S5

### 7. Section 7.2 contribution 2 S6–S10

- order：7

- locator：Section 7.2 contribution 2 S6–S10

- paraphrase_cn：第二贡献：用两个大样本纵向现场实验评价PFM，预测和干预两方面都优于竞争模型。

- move_code：CONTRIBUTION_2

- statement_status：contribution_claim

- why_here_cn：把两个实验的规模与结果作为评价贡献，呼应设计科学‘制品必须被严格评价’。

- inherits_from_previous_cn：承接S3–S5的制品贡献。

- changes_argument_state_cn：确立评价层面的知识贡献。

- sets_up_next_cn：为improvement定位作铺垫。

- failure_if_removed_cn：缺少评价贡献声明，PFM只是提案而非被验证的制品。

- evidence_pointer：Section 7.2 S6–S10

### 8. Section 7.2 positioning S11–S14

- order：8

- locator：Section 7.2 positioning S11–S14

- paraphrase_cn：PFM遵循设计科学指南，其性能提升代表improvement贡献；也遵循IS预测分析研究指南。

- move_code：CONTRIBUTION_TYPE

- statement_status：contribution_claim

- why_here_cn：把贡献在Gregor-Hevner和Shmueli-Koppius框架中定位，阻止读者要求理论突破。

- inherits_from_previous_cn：承接第二贡献的评价证据。

- changes_argument_state_cn：把贡献类型稳定为‘改进型’与‘预测分析’。

- sets_up_next_cn：为第三贡献（在线安全领域）作铺垫。

- failure_if_removed_cn：贡献类型不清，可能被审稿人以‘缺理论’批评。

- evidence_pointer：Section 7.2 S11–S14

### 9. Section 7.2 contribution 3 S15–S21

- order：9

- locator：Section 7.2 contribution 3 S15–S21

- paraphrase_cn：第三贡献面向在线安全领域：预测能力对安全软件公司、浏览器开发者、被仿冒企业和员工所在组织四类主体有含义。

- move_code：CONTRIBUTION_3

- statement_status：contribution_claim

- why_here_cn：把贡献从制品和评价扩展到领域实践，细分四类受钓鱼影响的主体。

- inherits_from_previous_cn：承接S11–S14的定位。

- changes_argument_state_cn：确立实践贡献。

- sets_up_next_cn：为‘为何不自动移除钓鱼邮件’的边界讨论作铺垫。

- failure_if_removed_cn：实践贡献主张缺失，ISR的应用导向受损。

- evidence_pointer：Section 7.2 S15–S21

### 10. Section 7.2 why not auto-remove S22–S31

- order：10

- locator：Section 7.2 why not auto-remove S22–S31

- paraphrase_cn：虽然PFM有效，但不应自动移除可疑邮件，因为钓鱼判断高度依赖上下文、误报不可避免且用户会转向限制较少的工具；选择性阻断可作为未来方向。

- move_code：BOUNDARY_CONDITION

- statement_status：author_inference

- why_here_cn：主动为‘预测驱动警告’划定边界，解释为何不以‘自动移除’替代，保护设计的合理性。

- inherits_from_previous_cn：承接贡献3的有效性。

- changes_argument_state_cn：限定制品的适用范围，防止过度应用批评。

- sets_up_next_cn：为7.3的局限与未来工作作铺垫。

- failure_if_removed_cn：读者会质疑‘为什么不直接删邮件’，制品边界不清。

- evidence_pointer：Section 7.2 S22–S31

### 11. Section 7.3 limitation 1 S1–S7

- order：11

- locator：Section 7.3 limitation 1 S1–S7

- paraphrase_cn：漏斗止于意图交易，存在意图-行为差距（15%–20%未实际交易），虽有缓解但仍需未来把实际交易纳入模型。

- move_code：LIMITATION_AND_FUTURE

- statement_status：author_inference

- why_here_cn：先承认最核心的概念限制，再给出部分缓解证据，最后指向未来工作。

- inherits_from_previous_cn：承接7.2的边界讨论。

- changes_argument_state_cn：从‘贡献’转入‘诚实边界’。

- sets_up_next_cn：为泛化性限制作并列铺垫。

- failure_if_removed_cn：核心因变量限制被隐藏，审稿人更可能攻击。

- evidence_pointer：Section 7.3 S1–S7

### 12. Section 7.3 limitation 2 S8–S14

- order：12

- locator：Section 7.3 limitation 2 S8–S14

- paraphrase_cn：PFM仅在金融和法律行业员工中测试；调查与弹窗可能影响行为，虽有对策但仍有自报偏差与泛化问题。

- move_code：LIMITATION_AND_FUTURE

- statement_status：author_inference

- why_here_cn：界定外部效度边界，并以已做稳健性分析作为部分缓解证据。

- inherits_from_previous_cn：承接限制1。

- changes_argument_state_cn：把边界从‘因变量’扩展到‘样本与测量’。

- sets_up_next_cn：为未来研究议程作铺垫。

- failure_if_removed_cn：外部效度主张无边界控制，会被批评过度推广。

- evidence_pointer：Section 7.3 S8–S14

### 13. Section 7.3 limitation 3 S15–S20

- order：13

- locator：Section 7.3 limitation 3 S15–S20

- paraphrase_cn：未来应考虑调查时滞与重训率的权衡、特征子集选择、成本纳入训练过程，以及警告设计元素层面的研究。

- move_code：FUTURE_AGENDA

- statement_status：author_inference

- why_here_cn：把前面证据中未做的优化逐条转化为未来方向，形成完整研究议程。

- inherits_from_previous_cn：承接S8–S14的边界与局限。

- changes_argument_state_cn：把‘局限’转成‘下一步可做’。

- sets_up_next_cn：为收尾句作铺垫。

- failure_if_removed_cn：局限显得无建设性，未来研究缺乏起点。

- evidence_pointer：Section 7.3 S15–S20

### 14. Section 7.3 closing S21

- order：14

- locator：Section 7.3 closing S21

- paraphrase_cn：尽管存在局限，本文回应了用现场数据理解员工安全和安全分析研究的呼吁，是改进易感性预测的重要第一步。

- move_code：CLOSING_CLAIM

- statement_status：contribution_claim

- why_here_cn：收尾把研究重新放回IS学科议程，并以‘重要第一步’适度谦逊地主张贡献。

- inherits_from_previous_cn：承接全部局限与未来方向。

- changes_argument_state_cn：把‘有边界的结果’重新升格为‘对学科议题的有意义贡献’。

- sets_up_next_cn：无；文章结束。

- failure_if_removed_cn：文章在局限中结束，缺少最终贡献感的收拢。

- evidence_pointer：Section 7.3 S21

## Study累积逻辑

### 1. 1

- study_or_phase：阶段1：PFM制品构建（第3节）

- evidence_job_cn：把理论、漏斗隐喻与统计方法整合为一个可计算的预测制品，回答‘制品是什么’。

- what_it_establishes_cn：建立六类因素、四阶段因变量、SVORCK/CLMM估计方法之间的设计一致性。

- what_it_cannot_establish_cn：不能证明变量测量有效、算法在真实组织中有效、或预测能改变行为。

- why_next_phase_is_needed_cn：需要预试验验证测量工具，再进入现场证明预测力。

- transition_wording_function_cn：第3节末尾‘在随后的实验中…’把设计引向评价。

### 2. 2

- study_or_phase：阶段2：实验室预试验（第5节前奏）

- evidence_job_cn：检验PFM变量、问卷题项与操作化的信度和建构效度。

- what_it_establishes_cn：测量工具可用，避免现场数据受测量噪声污染。

- what_it_cannot_establish_cn：不能证明预测算法在真实组织中的性能或下游干预效果。

- why_next_phase_is_needed_cn：需要真实组织环境中的大规模纵向数据来回答RQ1。

- transition_wording_function_cn：‘作为现场实验的前奏’连接预试验与12个月实验。

### 3. 3

- study_or_phase：阶段3：12个月纵向现场预测实验（第5节，RQ1）

- evidence_job_cn：证明PFM在真实组织中随时间预测用户易感性的效能，并识别预测优势的来源（变量集、方法、特征类别、通道稳健性）。

- what_it_establishes_cn：PFM的AUC显著高于竞争模型/方法；高严重度访问预测96%；六类特征大多有贡献；跨通道稳健；测量干扰被排除。

- what_it_cannot_establish_cn：不能证明预测准确性可转化为实际防护行为改善或经济收益。

- why_next_phase_is_needed_cn：需要干预实验把‘能预测’提升为‘预测有用’。

- transition_wording_function_cn：第6节开头用RQ2和‘下游价值’显式连接两实验。

### 4. 4

- study_or_phase：阶段4：3个月干预现场实验（第6节，RQ2）

- evidence_job_cn：证明由易感性预测驱动的分级警告能显著降低用户与钓鱼网站的交互，并排除‘警告数量’这一替代解释。

- what_it_establishes_cn：PFM组在各漏斗阶段穿越率显著更低，实际交易率低3–6倍；SVORCK优于CLMM；随机设置劣于标准设置。

- what_it_cannot_establish_cn：不能直接建立经济账户；行为改善的货币价值未知。

- why_next_phase_is_needed_cn：需要成本收益与敏感性分析把行为改善转化为企业可决策的美元价值。

- transition_wording_function_cn：第6.2.1节用‘设计科学文献认为成本收益分析有用’引入经济评估。

### 5. 5

- study_or_phase：阶段5：成本收益与敏感性分析（第6.2.1节）

- evidence_job_cn：把干预实验的行为差异货币化，并用敏感性分析验证经济主张的稳健性。

- what_it_establishes_cn：PFM-SVORCK每员工年收益约1,960美元，且在收益降40%、成本升40%的极端情形下仍超1,000美元。

- what_it_cannot_establish_cn：不能证明在其他行业/人群的收益相同，也不能消除成本参数主要来自单家企业估计的局限。

- why_next_phase_is_needed_cn：需要讨论部分把局部结果升华为可复用设计知识与边界。

- transition_wording_function_cn：第7节‘结果讨论’把RQ1/RQ2答案和成本结果汇总为贡献。

## 主张—证据台账

### 1. PFM的预测效能显著高于竞争模型与基准方法。

- claim_cn：PFM的预测效能显著高于竞争模型与基准方法。

- claim_level：artifact

- supporting_evidence_cn：Table 5：PFM-SVORCK AUC=0.875、PFM-CLMM AUC=0.831，显著高于HITLSF(0.642)、DRKM(0.562)、AAM(0.548)及SVM(0.761)、SVOR(0.753)等（p<0.001）。

- support_strength：direct

- where_claim_is_made：摘要S8；Introduction P7 S2；Section 5.2 P4；Section 7.1 S4–S5

- where_evidence_is_provided：Table 5; Figure 4; Section 5.2 P4

### 2. PFM能96%正确预测对高严重度威胁的访问，比最近竞争者高10个百分点。

- claim_cn：PFM能96%正确预测对高严重度威胁的访问，比最近竞争者高10个百分点。

- claim_level：artifact

- supporting_evidence_cn：Figure 7：PFM-SVORCK在9个月测试期内对高严重度URL访问的正确预测率为96%，比最接近竞争者多170次。

- support_strength：direct

- where_claim_is_made：摘要S8；Section 5.2.1 S4；Section 7.1 S5

- where_evidence_is_provided：Figure 7; Section 5.2.1

### 3. PFM六类特征对预测都有实证贡献。

- claim_cn：PFM六类特征对预测都有实证贡献。

- claim_level：artifact

- supporting_evidence_cn：Table 7消融：移除工具性能、工具感知、威胁特征、先前经验、人口学后AUC显著下降；威胁感知在SVORCK显著（p=0.002）、在CLMM不显著（p=0.051）。

- support_strength：direct

- where_claim_is_made：Section 5.2.2 S5–S7；Table 10

- where_evidence_is_provided：Table 7; Section 5.2.2

### 4. 感知/调查特征对预测不可或缺，PFM变量集优于所有竞争变量总和。

- claim_cn：感知/调查特征对预测不可或缺，PFM变量集优于所有竞争变量总和。

- claim_level：artifact

- supporting_evidence_cn：Table 8：PFM observed only AUC=0.772，加入prior logs后0.821，仍显著低于完整PFM的0.875；all variables 0.860也不优于PFM。

- support_strength：direct

- where_claim_is_made：Section 5.2.2 S12–S14

- where_evidence_is_provided：Table 8; Section 5.2.2

### 5. PFM跨威胁通道表现稳健。

- claim_cn：PFM跨威胁通道表现稳健。

- claim_level：artifact

- supporting_evidence_cn：Table 6：PFM在搜索(0.903/0.855)、工作邮件(0.881/0.833)、社交媒体(0.872/0.827)与总体接近，仅个人邮件略低（SVORCK 0.862）。

- support_strength：direct

- where_claim_is_made：Section 5.2.1 S1、S4

- where_evidence_is_provided：Table 6; Section 5.2.1

### 6. 季度调查与弹窗未显著改变行为，测量干扰有限。

- claim_cn：季度调查与弹窗未显著改变行为，测量干扰有限。

- claim_level：artifact

- supporting_evidence_cn：Figure 8无调查前后模式；Figure 9 pilot研究中弹窗组与对照组在访问、浏览、实际交易无显著差异。

- support_strength：direct

- where_claim_is_made：Section 5.2.3 S5–S6、S19

- where_evidence_is_provided：Figures 8–9; Section 5.2.3

### 7. 预测驱动的分级警告能显著降低用户与钓鱼的交互。

- claim_cn：预测驱动的分级警告能显著降低用户与钓鱼的交互。

- claim_level：artifact

- supporting_evidence_cn：Figure 10与ANOVA：六设置每阶段显著不同，PFM组显著优于非PFM组；PFM-SVORCK实际交易率0.50% vs 标准2.64%（3–6倍差异）。

- support_strength：direct

- where_claim_is_made：摘要S9；Section 6.2 S3–S5；Section 7.1 S9

- where_evidence_is_provided：Figure 10; Section 6.2 ANOVA

### 8. PFM-SVORCK优于PFM-CLMM。

- claim_cn：PFM-SVORCK优于PFM-CLMM。

- claim_level：artifact

- supporting_evidence_cn：干预实验直接对比：SVORCK在visit、browse、consider legitimate、intend to transact均显著优于CLMM（p<0.05），observed transaction不显著（p=0.090）。

- support_strength：direct

- where_claim_is_made：Section 6.2 S17；Table 10

- where_evidence_is_provided：Section 6.2 ANOVA contrasts

### 9. PFM驱动的干预带来显著且稳健的经济收益。

- claim_cn：PFM驱动的干预带来显著且稳健的经济收益。

- claim_level：design_knowledge

- supporting_evidence_cn：Table 9：PFM-SVORCK每员工年收益$1,960；Figure 11敏感性分析在最差情形（收益降40%、成本升40%）下仍超$1,000。

- support_strength：partial

- where_claim_is_made：摘要S10；Section 6.2.1 S17、S28–S29

- where_evidence_is_provided：Table 9; Figure 11

### 10. 干预效果不是由警告数量差异驱动，而是由预测对齐性驱动。

- claim_cn：干预效果不是由警告数量差异驱动，而是由预测对齐性驱动。

- claim_level：mechanism

- supporting_evidence_cn：Figure 12显示六组警告总量无显著差异，PFM组高严重度警告并非最多，却表现最好。

- support_strength：partial

- where_claim_is_made：Section 6.2.2 S7

- where_evidence_is_provided：Figure 12; Section 6.2.2

### 11. 结果具有强外部效度。

- claim_cn：结果具有强外部效度。

- claim_level：boundary

- supporting_evidence_cn：两个不同行业/规模组织、12+3个月纵向现场数据、1,278和1,218名员工、49,373和13,824次交互；未见其他行业/人群测试。

- support_strength：partial

- where_claim_is_made：摘要S11；Section 7.1 S1

- where_evidence_is_provided：Table 3; Section 5; Section 6

### 12. 建模整个钓鱼漏斗比只关注单一用户行动更好。

- claim_cn：建模整个钓鱼漏斗比只关注单一用户行动更好。

- claim_level：design_knowledge

- supporting_evidence_cn：多阶段序数模型（PFM）AUC显著高于单行为/等距阈值替代模型（SVOR、CLMM-Equi）；干预效果随阶段分化。

- support_strength：direct

- where_claim_is_made：摘要S12(2)；Section 3.2；Section 7.2 S3

- where_evidence_is_provided：Table 5; Section 3.2 rationale

## ISR定位逻辑

- constitutive_is_problem_cn：本文的问题不是纯检测技术问题，而是‘技术制品—用户认知—组织安全’三者的相互构成：反钓鱼工具的有效性取决于用户是否信任、理解并服从其警告，用户的易感性又取决于工具、威胁与用户特征三者的交互。作者把‘预测网站是否钓鱼’改写为‘预测用户在上当过程中会走到哪一步’，从而把技术检测、用户行为与组织防护统一到一个预测制品中。

- technology_behavior_or_market_entanglement_cn：技术不是可替换的工具：PFM将工具性能（检测率、警告、处理时间）与用户对工具的感知（有用性、费力程度、错误成本）同时作为预测输入，并在干预中把预测结果映射为分级警告；技术设计与用户行为在同一模型中互相定义，特征消融又证明这些技术相关变量对预测有独特贡献。

- role_of_benchmark_or_objective_evidence_cn：AUC、高严重度访问检测率、漏斗穿越百分比并非只做算法比较；它们被用来支持三个IS主张：多阶段漏斗因变量优于单行为建模、工具和威胁因素应进入易感性预测、预测驱动的个性化警告能改变真实安全行为。benchmark证据同时服务于制品评价与设计知识升级。

- theory_in_design_cn：TAM、PMT、HITLSF在变量选择层面进入设计：每个理论命题被翻译成至少一个可测变量类别，并在特征消融中作为可证伪的设计成分被检验。CLMM/随机效应把‘用户异质性’落实为统计结构，使理论构念进入估计方式。不过理论并未被作为假设检验，算法细节多来自ML/统计文献，因此理论与设计的耦合是‘实质但不完全’。

- technical_vs_is_contribution_balance_cn：文章对SVORCK/CLMM的数学细节、核构造、窗口式训练花费大量篇幅（约1/4），但贡献声明没有停在算法精度上；篇幅重心通过两个现场实验转移到‘预测—干预—成本’链，最终把贡献定位为设计制品与可复用设计知识（漏斗建模、三类因素、分级警告），技术只是支撑该IS贡献的手段。

- beyond_transient_performance_cn：作者通过四种方式使贡献超越一次性分数优势：（1）12+3个月两个组织的纵向现场数据而非离线benchmark；（2）干预实验证明预测能改变真实行为；（3）成本收益与敏感性分析把性能转成管理价值；（4）多层次稳健性（特征消融、通道、Hawthorne、警告数量）排除替代解释。但‘强外部效度’声明仍部分依赖两个行业的样本，属作者推断而非完全经验证明。

## 段落级仿写模板

### abstract_steps

1. 第一步：一句话界定问题域，指出该问题影响的主要对象。

2. 第二步：用一个句子区分不同受害群体的后果，放大利害关系。

3. 第三步：把问题根源定位到用户与现有工具的共同失败处，为方案提供靶心。

4. 第四步：用一句话提出制品名称并声明其类型（设计制品）。

5. 第五步：概括制品的核心设计：输入变量类别与输出结构。

6. 第六步：说明估计方法及其与输出结构的对应关系。

7. 第七步：给出评价场景：时长、组织数、样本量与交互数。

8. 第八步：报告核心预测量化结果（AUC范围＋高利害端点检测率）。

9. 第九步：报告下游干预结果，说明行为显著变化。

10. 第十步：报告经济转化结果（每单位成本节省）。

11. 第十一步：概括外部效度判断。

12. 第十二步：以三条实践含义或设计知识收束。

### introduction_paragraph_steps

1. 第一段：用定义或规模数据开场，接着指出管理者/组织关心，最后用经济成本收束。

2. 第二段：引用多项研究证明用户行为失败，再用具体百分比强化严重性。

3. 第三段：先给出最明显的现有方案，再用证据否定其充分性，最后给出一个机制解释。

4. 第四段：用一个‘本研究不同’句完成转向，随后定义核心概念，并列出该概念带来的应用价值。

5. 第五段：正式陈述研究目标，声明范式，然后概括制品构成与估计方法。

6. 第六段：引用该范式的研究问题准则，再落到两个具体RQ。

7. 第七段：用‘为回答这些问题’开启，依次预告每个实验的规模与结论。

8. 第八段：提前把贡献定位为novelty/improvement，并指出受众。

9. 第九段：以‘本文回应三个缺口’开场，逐条列出缺口并配文献，最后以仍待闭合的缺口收束。

### theory_to_design_steps

1. 第一步：先铺知识史，说明已有模型的路线与局限。

2. 第二步：引入第一个理论来源，说明其变量范围。

3. 第三步：逐一点评其他已有模型，指出各自变量焦点。

4. 第四步：用‘PFM吸收其元素并在三方面新增’收束文献段。

5. 第五步：引入成熟隐喻（如漏斗）并说明其在相邻领域的应用。

6. 第六步：把这个隐喻映射到目标现象，定义因变量结构。

7. 第七步：在3.1开头说明为何多理论整合，并给出变量-理论映射表预告。

8. 第八步：每个理论小节重复‘理论命题→机制→PFM变量选择→一致性陈述’的模板。

9. 第九步：转入模型形式，先说明为何用序数而不是多二元分类，再为阈值选择辩护。

10. 第十步：把统计机制（如随机效应）翻译成设计目标（用户异质性），并预告两种估计的预期关系。

### method_and_study_sequence_steps

1. 第一步：在第4节给出总路线图，把RQ与实验一一对应。

2. 第二步：每个实验开头重述所回答的RQ，并解释设计（纵向、随机化）对RQ的必要性。

3. 第三步：先交代预试验/测量工具验证，再描述现场环境、操作化和样本。

4. 第四步：指定评价协议（窗口式训练/测试、公平比较条件）。

5. 第五步：报告主结果前先说明benchmark层次，把变量集贡献与算法贡献分离。

6. 第六步：主结果用‘表+AUC±显著性’呈现，随后补ROC/端点等补充图。

7. 第七步：单独小节处理高利害对象（高严重度威胁），再处理稳健性（通道、特征、Hawthorne）。

8. 第八步：过渡到干预实验时用RQ2和‘下游价值’建立桥梁。

9. 第九步：干预实验先描述随机分组与处理设置，再报告行为差异和统计检验。

10. 第十步：以成本收益+敏感性分析收束经济价值，并以警告数量稳健性排除替代解释。

### results_reporting_steps

1. 第一步：用一句总括说明实验回答的RQ与采用的评价方式。

2. 第二步：交代比较对象和公平性条件（同算法、同变量集）。

3. 第三步：定义评价指标并引用IS先例。

4. 第四步：用主表报告AUC差异并附p值，随后用ROC/图说明实际意义。

5. 第五步：补充高利害端点的正确预测数量与百分比。

6. 第六步：用子标题逐项报告特征消融、通道稳健性、测量干扰。

7. 第七步：每小节末尾都以‘这说明…’把数字转成对制品设计判断的支撑。

8. 第八步：干预结果先给图描述，再给ANOVA与对比统计，最后解释随机设置的含义。

9. 第九步：成本收益先给参数来源，再给主表，再给敏感性图，最后承认参数局限。

### discussion_and_contribution_steps

1. 第一步：用总表汇总全部关键发现，一句句回答各RQ。

2. 第二步：把RQ答案与引言中的机制（如个性化缺失）回扣，形成论证闭环。

3. 第三步：将结果外推为应用设想，并以‘企业正在探索’增强可行性。

4. 第四步：用‘贡献有三’开启正式贡献清单，逐条对应制品、评价、领域影响。

5. 第五步：在Gregor-Hevner或Shmueli-Koppius框架中给贡献定位，防止过度主张。

6. 第六步：主动讨论‘为什么不做替代方案’（如自动移除），划定边界。

7. 第七步：先承认最核心的概念限制，再给部分缓解证据。

8. 第八步：界定外部效度边界，把局限转为未来研究议程。

9. 第九步：以‘重要第一步’适度谦逊地收尾，回扣学科呼吁。

## 可执行写作算法

### 1. 1

- step：1

- rhetorical_job_cn：建立问题规模与利害关系。

- research_evidence_required_cn：有可靠来源的问题定义、影响人数、管理者关注度与经济损失数字。

- sentence_pattern_function_cn：‘X是…，影响…’→‘X不仅因为…而且因为…’→‘平均…花费…’。

- transition_condition_cn：当读者已确信该问题重要且昂贵，即可转入用户端失败。

### 2. 2

- step：2

- rhetorical_job_cn：证明用户行为是问题核心。

- research_evidence_required_cn：多项实证研究显示用户在目标任务上的失败率。

- sentence_pattern_function_cn：‘多项研究显示…很差’→‘文献表明用户X%时间无法识别，Y%愿意交易’。

- transition_condition_cn：当用户失败被量化后，即可转向‘已有工具能否解决’。

### 3. 3

- step：3

- rhetorical_job_cn：否定最明显的解决方案并给出机制。

- research_evidence_required_cn：工具使用下仍失败的成功率数据，以及失效机制文献。

- sentence_pattern_function_cn：‘一个潜在方案是…’→‘然而，即使用这些工具…’→‘失败原因可能是…’。

- transition_condition_cn：当‘工具因未个性化而失效’被确立，即可转向新思路。

### 4. 4

- step：4

- rhetorical_job_cn：完成问题转向并定义核心概念。

- research_evidence_required_cn：对新概念的可操作定义，以及该定义能支撑的应用价值清单。

- sentence_pattern_function_cn：‘本研究采取不同方法：不是…而是…’→‘我们把X定义为…’→‘该方案将(1)…(2)…(3)…’。

- transition_condition_cn：当核心概念与三项价值被列出，即可正式提出研究目标与制品。

### 5. 5

- step：5

- rhetorical_job_cn：提出制品并预告设计。

- research_evidence_required_cn：已构建或可构建的制品蓝图：输入变量、输出结构、估计方法。

- sentence_pattern_function_cn：‘研究目标是开发设计制品’→‘我们采用…范式’→‘制品强调…’→‘模型用…估计’。

- transition_condition_cn：当制品蓝图为读者所知，即可提出RQ。

### 6. 6

- step：6

- rhetorical_job_cn：把制品开发转为可检验的研究问题。

- research_evidence_required_cn：范式层面的RQ准则；两个能覆盖‘性能’与‘下游价值’的具体问题。

- sentence_pattern_function_cn：‘设计科学RQ通常关注…’→‘因此我们聚焦…’→‘RQ1…RQ2…’。

- transition_condition_cn：当RQ1/RQ2确立，即可预告评价设计。

### 7. 7

- step：7

- rhetorical_job_cn：预告研究设计并定位贡献。

- research_evidence_required_cn：至少有一个能回答RQ的实证研究计划；对贡献类型的自我定位。

- sentence_pattern_function_cn：‘为回答这些问题，我们…’→‘第一个…第二个…’→‘从设计科学看…是novelty/improvement’。

- transition_condition_cn：当读者知道实验路线与贡献类型，即可列出缺口清单。

### 8. 8

- step：8

- rhetorical_job_cn：把问题背景浓缩为可回扣的缺口清单。

- research_evidence_required_cn：对文献缺口的准确概括，以及每条缺口与本文方案的对应关系。

- sentence_pattern_function_cn：‘本文回应三个缺口’→‘第一…第二…第三…’，每条由‘文献事实＋IS依据＋本文填补’构成。

- transition_condition_cn：当三个缺口形成后，即可进入理论与制品章节逐条展开。

### 9. 9

- step：9

- rhetorical_job_cn：用两层benchmark和稳健性分析把预测优势变成可分解的证据。

- research_evidence_required_cn：一个公平对照框架：同算法比较变量组合，同变量比较算法；特征消融、通道、Hawthorne等稳健性分析。

- sentence_pattern_function_cn：‘两项分析’→‘第一比较模型…第二比较方法…’→主表AUC±p值→子标题稳健性各小节，每节以‘这说明…’收束。

- transition_condition_cn：当预测优势充分分解并排除替代解释后，即可追问‘预测是否有用’。

### 10. 10

- step：10

- rhetorical_job_cn：用干预实验和经济分析把预测价值升级为下游价值。

- research_evidence_required_cn：随机分配的处理/对照设置；行为结果；成本参数及其来源；敏感性分析。

- sentence_pattern_function_cn：‘第二研究问题问…’→‘随机分配到六种设置’→图+ANOVA+对比→成本参数→主收益表→敏感性图→警告数量稳健性。

- transition_condition_cn：当行为与经济价值均已证明，即可在讨论中把结果升级为贡献与设计知识。

### 11. 11

- step：11

- rhetorical_job_cn：在讨论中依次完成结果汇总、贡献声明、边界与局限。

- research_evidence_required_cn：RQ答案的浓缩；三条与制品、评价、领域对应的贡献；对边界（为何不做替代方案）与局限（因变量、样本、测量）的诚实说明。

- sentence_pattern_function_cn：‘实验证明…’→‘对RQ1…对RQ2…’→‘贡献有三：…’→‘一个明显问题是为什么不…’→‘我们的工作不无局限…’。

- transition_condition_cn：当贡献与局限同时清楚，即可用‘重要第一步’收尾。

## 应模仿的高价值动作

1. 把问题从‘检测威胁对象’转向‘预测用户行为’，用一个可操作定义（易感性＝互动程度）锚定新概念。

2. 用三层证据链（预测AUC→干预行为→经济收益）支撑同一个设计制品，每层对应一个RQ。

3. 两层benchmark设计：同算法比较不同变量组合、同变量比较不同算法，从而把‘变量集贡献’与‘算法贡献’分离。

4. 在评价中主动为制品内部构件设置剥离对照（如SVORCK vs 无复合核的CLMM），使构件可证伪。

5. 用随机设置和警告数量分布检验排除‘新警告本身更有效’这一替代解释。

6. 用特征消融逐类证明六类变量的贡献，把理论选择变成经验证据。

7. 用成本收益主表＋敏感性分析图保护经济主张，并诚实披露参数来源与局限。

8. 用pilot研究和月度趋势图排除Hawthorne效应，保护行为证据的内部效度。

9. 讨论中把RQ答案与引言中的机制句（警告未个性化）回扣，形成论证闭环。

10. 用Gregor-Hevner和Shmueli-Koppius给贡献定位，主动把贡献类型限定为improvement，防止过度主张。

## 不要只复制的表面动作

1. 不要只给概念贴‘漏斗’标签而无真实的序数因变量与对应预测模型。

2. 不要在无窗口式训练/保留样本的情况下直接报告AUC。

3. 不要把实验室或离线精度直接称为组织现场有效性。

4. 不要在没有随机设置/标准设置对照时声称干预由‘个性化’驱动。

5. 不要把AUC或检测率数字直接等同于企业安全收益，必须有成本参数与敏感性分析。

6. 不要把‘强外部效度’建在两个行业样本上而不声明边界。

7. 不要把感知变量重要性当作常识而省略特征集/消融证据。

8. 不要逐字复制‘人类比计算机更能判断上下文’式引文而不与自己的干预设计绑定。

## 证据薄弱或跳跃的动作

1. ‘这些结果表明强外部效度’（摘要S11）：仅基于金融与法律两个行业、两个组织的员工样本，属于作者推断而非直接证明。

2. 成本收益外推到10,000员工企业：成本参数主要来自FinOrg自报，LegOrg与行业外推均未充分验证。

3. 把随机设置劣于标准设置解读为‘没有对齐易感性的警告无益’：未直接检验警告本身的可厌性或显示方式差异，存在替代解释空间。

4. CLMM/随机效应‘简约地’捕捉用户异质性的声称：缺乏与更复杂异质性模型的复杂度/拟合比较，’简约‘更多是理论声明。

5. 比较模型（DRKM、AAM、HITLSF、SVM等）为本文改编重实现：作者在第7.3节和Online Appendix C中承认存在上下文差异，可能带来公平性偏差。

6. 意图-行为差距：15%–20%的意图交易未实际发生，但漏斗端点仍止于意图，作者用预测表现和干预效果部分缓解而非完全解决。

7. 干预实验仅3个月，不能排除长期警告习惯化；作者也承认未来需探索。

## 一句话套路

用理论选择变量，把用户行为建模为多阶段漏斗序数响应，用内嵌混合模型的复合核算法预测，用12个月现场实验证明预测力，再用3个月干预实验证明预测驱动的分级警告能改变真实安全行为，最后用成本收益与敏感性分析把行为改进转化为稳健的管理价值。

## 分析边界

全文文本完整可读，但图片（Figure 1-12）、部分表格视觉细节和数学公式在OCR中可能有轻微失真；实验室预试验细节仅在正文中作摘要式提及，详细内容依赖Online Appendices（未提供）；精确页码不可得，位置证据基于章节/图/表/句序号；成本参数来自文章自报的FinOrg估计，未做外部审计；比较模型的重新实现细节在Online Appendix C中，正文无法核实其公平性。
