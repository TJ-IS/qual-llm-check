# 审计细节：M1 漏检金标准 25 篇分类 + 疑似误纳/误排检查

## A. M1 漏检的金标准（25 篇）：分类

共 25 篇；按『CSV 中是否有该文』区分：

### A1. 不在 CSV（元数据检索天然够不到，语料覆盖问题）：0 篇


### A2. 在 CSV 但摘要/标题/关键词无词表命中（真漏词或摘要无攻防词）：25 篇

- 00358_2020_why-individual-employees-commit-malicious-computer-abuse-a-routine-activity-theory-perspective.md | Why individual employees commit malicious computer abuse: A routine activity theory perspective | 2020 | Journal of the Association for Information Systems
  - 摘要前 250 字: Prior information security studies have largely focused on understanding employee security behavior from a policy compliance perspective. We contend that there is a pressing need to develop a comprehensive understanding of the circumstances that lead
  - 关键词: Information Security; Insider Threat; Malicious Computer Abuse; Routine Activity Theory; Security Management | Activity coefficients; Personal computing; Security of data; Security systems; Comprehensive model; Employee commitment; Individual characteristics; Management programs; Organizational aspects; Organi
  - 判定理由: 全文聚焦于员工恶意计算机滥用（MCA），即内部人员故意窃取、篡改或未授权访问组织数字资产的攻击行为，并基于日常活动理论对其动机、目标适宜性和守卫因素进行建模与实证，属于内部威胁/攻击行为研究。
- 01704_2024_doxing-on-social-networking-sites-an-extension-of-the-social-cognitive-theory-of-moral-thought-a.md | Doxing on Social Networking Sites: An Extension of the Social Cognitive Theory of Moral Thought and Action | 2024 | Journal of the Association for Information Systems
  - 摘要前 250 字: Doxing on social networking sites (SNS doxing) has attracted scholarly and public attention due to the devastating consequences that this behavior can have on individuals and society. SNS doxing occurs when netizens disclose wrongdoers’ personal info
  - 关键词: Doxing; Morality; Polynomial Regression Analysis; Retributive Proportionality; Social Approval; Social Cognitive Theory of Moral Thought and Action; Social Networking Sites | Decision making; Polynomial regression; Polynomials; Social behavior; Social networking (online); Social psychology; Doxing; Morality; Polynomial regression analysis; Retributive proportionality; Soci
  - 判定理由: 文章核心研究SNS人肉搜索（doxing），即通过网络披露他人个人信息以羞辱、骚扰和惩罚目标用户的恶意行为，属于隐私披露攻击与网络欺凌范畴，研究其道德前因以支撑预防策略。
- 04526_2011_multi-tag-and-multi-owner-rfid-ownership-transfer-in-supply-chains.md | Multi-tag and multi-owner RFID ownership transfer in supply chains | 2011 | Decision Support Systems
  - 摘要前 250 字: In any supply chain, there is a high likelihood for individual objects to change ownership at least once in their lifetime. As RFID tags enter the supply chain, these RFID-tagged objects should ideally be able to seamlessly accommodate ownership tran
  - 关键词: Ownership transfer; RFID; Supply chain | Radio frequency identification (RFID); Radio navigation; Supply chain management; Supply chains; Individual objects; Ownership transfer; RF-ID tags; Simultaneous transfer; Single object; Trusted third
  - 判定理由: 研究核心是RFID标签所有权转移协议，涉及恶意对手对RFID系统的攻击、漏洞分析及安全协议设计。
- 06126_2016_internet-aggression-in-online-communities-a-contemporary-deterrence-perspective.md | Internet aggression in online communities: a contemporary deterrence perspective | 2016 | Information Systems Journal
  - 摘要前 250 字: Internet users' activities are critical to the development and success of Web 2.0 systems, such as online communities. Within the community's participation, knowledge sharing, and communications, users may conduct aggressive behaviors that would have
  - 关键词: aggression; deterrence; morals; virtual community | Internet; Social networking (online); Virtual reality; Websites; World Wide Web; Aggression; Deterrence; Internet users; Knowledge-sharing; Morals; On-line communities; Online aggressions; Virtual com
  - 判定理由: 研究核心是在线社区中的网络攻击性行为（嘲弄、辱骂、隐私披露等）及其威慑机制，属于针对系统用户的攻击行为及其防御/缓解研究。
- 05690_2005_model-checking-for-design-and-assurance-of-e-business-processes.md | Model checking for design and assurance of e-Business processes | 2005 | Decision Support Systems
  - 摘要前 250 字: Use of the Internet for electronic business has the potential to revolutionize the way many businesses are conducted. Yet, several businesses have fallen victim to problems in information systems that facilitate e-Business. These problems are charact
  - 关键词: e-Business; Goods atomicity; Model checking; Money atomicity; Process and communication protocols; Valid receipt | Communication systems; Computer simulation; Internet; Mathematical models; Network protocols; Risk assessment; E-business; Goods atomicity; Model checking; Money atomicity; Process and communication p
  - 判定理由: 全文核心是用模型检查验证电子商务协议，发现可能导致欺诈、入侵和流程失败的设计漏洞，属于安全协议保证与威胁评估。
- 06092_2008_online-reputation-systems-design-and-strategic-practices.md | Online reputation systems: Design and strategic practices | 2008 | Decision Support Systems
  - 摘要前 250 字: This paper provides a comprehensive framework for evaluating the effects of feedback systems, and the potential problems with feedback systems, on seller incentives to provide high quality products under the case of asymmetric information. In particu
  - 关键词: B2B; B2C; e-Commerce; Incentive Structure; Trust | Electronic commerce; Failure analysis; Feedback control; Industrial management; Problem solving; Quality control; Feedback systems; Incentive Structure; Trust; Online systems
  - 判定理由: 文章核心研究在线拍卖反馈系统中的恶意行为（shilling、ID更换、不反馈）对系统真实性的影响及其防御措施，属于针对信息系统数据完整性的攻击与防御研究。
- 10238_2011_does-ethical-ideology-affect-software-piracy-attitude-and-behaviour-an-empirical-investigation-o.md | Does ethical ideology affect software piracy attitude and behaviour An empirical investigation of computer users in China | 2011 | European Journal of Information Systems
  - 摘要前 250 字: This study empirically examines Chinese computer users ethical ideology and its relationship to their software piracy attitude and behaviour. The investigation reveals several important findings. First, cluster analysis results show that Chinese comp
  - 关键词: China; computer users' ethics; ethical ideology; software piracy | Cluster analysis; Computer software; Philosophical aspects; China; Computer users; Empirical investigation; ethical ideology; Policy makers; Software developer; Target audience; Computer crime
  - 判定理由: 文章核心研究软件盗版（未经授权复制软件）这种针对软件资产的攻击行为，考察伦理意识形态对盗版态度和行为的影响，属于攻防安全中的攻击行为研究。
- 10634_2009_griefing-in-virtual-worlds-causes-casualties-and-coping-strategies.md | Griefing in virtual worlds: Causes, casualties and coping strategies | 2009 | Information Systems Journal
  - 摘要前 250 字: A virtual world is a computer-simulated three-dimensional environment. They are increasingly being used for social and commercial interaction, in addition to their original use for game playing. This paper studies negative behaviour, or ?griefing?, i
  - 关键词: Antisocial behaviour; Interpretative phenomenological analysis; Virtual worlds | 
  - 判定理由: 全文聚焦虚拟世界中的恶意破坏行为（griefing），包括骚扰、攻击、隐私披露等对抗行为，研究其成因、影响与应对策略，属于针对信息系统用户的攻击与防御研究。
- 09872_2021_information-technology-and-government-corruption-in-developing-countries-evidence-from-ghana-cus.md | INFORMATION TECHNOLOGY AND GOVERNMENT CORRUPTION IN DEVELOPING COUNTRIES: EVIDENCE FROM GHANA CUSTOMS | 2021 | MIS Quarterly: Management Information Systems
  - 摘要前 250 字: The literature on information technology (IT) and government corruption in developing countries indicates contradictory evidence about the realization of anti-corruption effects. So far, there is no theoretical explanation of why the anti-corruption 
  - 关键词: anti-corruption; developing countries; Government corruption; IS user responses; IT co-optation; IT implementation; neopatrimonialism; social embeddedness; street-level bureaucracy | Crime; Embedded systems; Information systems; Information use; Anti-corruption; Case-studies; Government administration; Government corruption; Information technology co-optation; Information technolo
  - 判定理由: 文章核心研究海关官员作为恶意内部人员对TradeNet信息系统功能的操纵与滥用（如数据盗窃、绕过风险分析与随机分配、伪造记录），并评估IT反腐败机制为何失效，属于内部威胁攻防安全研究。
- 12724_2019_an-economic-analysis-of-platform-protection-in-the-presence-of-content-substitutability.md | An Economic Analysis of Platform Protection in the Presence of Content Substitutability | 2019 | Journal of Management Information Systems
  - 摘要前 250 字: Online platforms, such as App Store and Kindle, are facing a common dilemma: while the implementation of technology-based protection impedes piracy and hence boosts demand from legal users (positive effect), the resulting restriction meanwhile impose
  - 关键词: advertising agency; content agency; content protection; online piracy; online platforms; platform protection; pricing; two-sided platforms | Computer crime; Costs; Crime; Marketing; Advertising agency; content agency; Content Protection; Online piracy; Online platforms; platform protection; Two-sided platforms; Economic analysis
  - 判定理由: 文章核心研究对象是在线平台为对抗数字盗版（未经授权复制）而实施的最优保护水平（如DRM），直接围绕攻击行为（piracy）的防御与缓解进行经济建模与分析。
- 13670_2016_intellectual-property-norms-in-online-communities-how-user-organized-intellectual-property-regul.md | Intellectual property norms in online communities: How user-organized intellectual property regulation supports innovation | 2016 | Information Systems Research
  - 摘要前 250 字: In many online communities, users reveal innovative and potentially valuable intellectual property (IP) under conditions that entail the risk of theft and imitation. When there is rivalry and formal IP law is not effective, this could lead to underin
  - 关键词: Crowdsourcing; Innovation; Intellectual property systems; Online communities; Social norms | Crowdsourcing; Innovation; Intellectual property; Social networking (online); Cumulative effects; Field experiment; Integrated systems; Netnography; On-line communities; Social norm; Underinvestment; 
  - 判定理由: 研究核心是在线社区中针对IP盗窃（抄袭/模仿）这一对抗行为的社会规范防御系统，并通过模拟抄袭的现场实验验证了检测与制裁决机制的有效性。
- 14334_2009_pricing-schemes-for-digital-content-with-drm-mechanisms.md | Pricing schemes for digital content with DRM mechanisms | 2009 | Decision Support Systems
  - 摘要前 250 字: In this paper, utilizing game-theoretic model, we examine the impact of collaborative structure, content quality, and network environment on the development of pricing scheme and DRM protection policy of digital content. DRM protection level decrease
  - 关键词: Content quality; Digital content; Digital Right Management; Network diffusion; Pricing scheme; System collaboration | Costs; Collaborative structures; Content providers; Content qualities; Digital contents; Digital right management; Game-theoretic model; Market structures; Network environments; Pricing scheme; Protec
  - 判定理由: 文章以盗版数字内容为对抗行为，研究DRM保护水平与定价策略，核心是盗版威胁的防御与缓解。
- 15516_2022_technological-entitlement-its-my-technology-and-ill-ab-use-it-how-i-want-to.md | TECHNOLOGICAL ENTITLEMENT: IT’S MY TECHNOLOGY AND I’LL (AB)USE IT HOW I WANT TO | 2022 | MIS Quarterly: Management Information Systems
  - 摘要前 250 字: Entitlement has been identified as a potentially valuable employee characteristic in the prediction of computer abuse but has not been studied systematically in the IS domain. We introduce the construct of technological entitlement as the persistent 
  - 关键词: behavioral; computer abuse; construct development; Individual behaviors; multi-method; psychological; technological entitlement; technology restriction | Behavioral research; Behavioral; Computer abuse; Construct development; Individual behavior; Multi methods; Psychological; Resource use; Technological entitlement; Technological resources; Technology 
  - 判定理由: 研究核心是内部威胁（计算机滥用）的心理预测因素，属于攻防安全中的内部威胁检测与评估。
- 15370_2019_an-integrative-theory-addressing-cyberharassment-in-the-light-of-technology-based-opportunism.md | An Integrative Theory Addressing Cyberharassment in the Light of Technology-Based Opportunism | 2019 | Journal of Management Information Systems
  - 摘要前 250 字: Scholars are increasingly calling for a deeper understanding of cyberharassment (CH) with the goal of devising policies, procedures, and technologies to mitigate it. Accordingly, we conducted CH research that (1) integrated social learning theory (SL
  - 关键词: cyberharassment; deviance; online harassment; self-control theory; social learning theory; social-psychological-technological (S-P-T) phenomenon; technology-based opportunism | Engineering education; Cyber-harassment; deviance; online harassment; Social learning theory; social-psychological-technological (S-P-T) phenomenon; Technology-based; Control theory
  - 判定理由: 文章以网络骚扰（在线欺凌/内容攻击）的动因、社会-心理-技术模型和缓解设计为研究核心，明确属于攻防安全。
- 20849_2000_edi-controls-design-support-system-using-relational-database-system.md | EDI controls design support system using relational database system | 2000 | Decision Support Systems
  - 摘要前 250 字: The purpose of this paper is to introduce EDIRDB (EDI controls design support system using a relational database system), a prototype audit support system based on a relational database designed to act as a decision aid for EDI auditors. This paper d
  - 关键词:  | Computer systems programming; Electronic data interchange; Relational database systems; Response time (computer systems); Audit support systems; Decision support systems
  - 判定理由: 文章核心是EDI审计支持系统，针对EDI系统中的恶意/未授权访问、数据篡改、系统中断等安全威胁，设计控制措施并评估风险，属于攻防安全中的防御与风险评估。
- 21281_2004_sdmi-based-rights-management-systems.md | SDMI-based rights management systems | 2004 | Decision Support Systems
  - 摘要前 250 字: Building digital rights management (DRM) systems for electronic commerce is still a complex task because such systems are usually required to manage a large set of different media contents, rights information, and enabling technologies. The Secure Di
  - 关键词: Copyright protection; Digital watermarking; Electronic commerce; Intellectual property protection; Rights management | CD-ROM; Computer crime; Computer music; Computer software; Copyrights; Digital libraries; Digital television; Digital watermarking; Electronic commerce; Internet; Multimedia systems; Technology transf
  - 判定理由: 全文以数字水印和SDMI实现数字版权管理为核心，明确针对盗版、未授权复制和传播等对抗行为，研究其检测、防御与遏制机制。
- 22211_2003_the-is-risk-analysis-based-on-a-business-model.md | The IS risk analysis based on a business model | 2003 | Information and Management
  - 摘要前 250 字: The disruption of operations due to IS failure becomes more important as IS has become an increasingly essential component of the organization's operations and can affect its strategic objectives. Nevertheless, traditional IS risk analysis methods do
  - 关键词: Analytic Hierarchy Process (AHP); Asset valuation; Asset-function assignment; Business model; Paired comparison; Risk analysis | Costs; Decision making; Risk assessment; Value engineering; Business models; Information management
  - 判定理由: 文章核心是IS风险分析方法，明确将故意内部/外部威胁（如篡改、破坏、泄露）纳入风险分析，并围绕资产价值、威胁概率和年损失期望进行威胁评估与建模。
- 23404_1990_information-systems-forensics.md | Information systems forensics | 1990 | Journal of Information Technology
  - 摘要前 250 字: This paper discusses some current issues and methods related to the investigation and successful prosecution of crimes committed with or against computerized information systems. The paper maintains that a new extension to the forensic sciences is a 
  - 关键词:  | 
  - 判定理由: 文章核心是计算机犯罪/滥用的调查、取证、检测与起诉，即针对信息系统攻击的防御与响应研究。
- 22611_2000_flaming-among-first-time-group-support-system-users.md | Flaming among first-time group support system users | 2000 | Information and Management
  - 摘要前 250 字: Numerous benefits, including increases in efficiency, effectiveness, and participant satisfaction, have been noted in the literature when electronic meetings are used in place of traditional, oral meetings. However, several costs, or process losses, 
  - 关键词: Brainstorming; Disinhibition; Electronic meetings; Flaming; Group support systems | 
  - 判定理由: 本文以匿名GSS中的攻击性评论（flaming）为核心研究对象，分析其发生规律与用户特征的相关性，属于对在线内容攻击（网络欺凌）的评估与建模。
- 25278_2003_identification-of-comment-authorship-in-anonymous-group-support-systems.md | Identification of comment authorship in anonymous group support systems | 2003 | Journal of Management Information Systems
  - 摘要前 250 字: This study examines whether technically "anonymous" comments entered by participants during group support system (GSS) brainstorming sessions are, in fact, unidentifiable. Hypotheses are developed and tested about the influences of comment length, co
  - 关键词: Anonymity; Computer-mediated communication; Group support systems; Social networks | Communication systems; Computers; Decision support systems; Social networks; Management information systems
  - 判定理由: 研究核心是评估匿名群组支持系统中技术匿名是否可被参与者通过评论线索准确识别，即对匿名机制的去匿名化攻击及安全性评估，属于攻防安全范畴。
- 25539_2021_exposing-patterns-of-adult-solicitor-behaviour-towards-a-theory-of-control-within-the-cybersexua.md | Exposing patterns of adult solicitor behaviour: towards a theory of control within the cybersexual abuse of youth | 2021 | European Journal of Information Systems
  - 摘要前 250 字: The online solicitation of youth has been established as an unintended consequence of the connectedness afforded individuals through computer-mediated conversation. Information systems research focused on the behavioural patterns of online solicitors
  - 关键词: child sexual abuse; grounded theory; Mike Gallivan; online sexual predation; Pär Ågerfalk; Social media; social media theory | Information systems; Grounded theory; Instant messaging; Software developer; Theoretical foundations; Unintended consequences; Online systems
  - 判定理由: 本文以网络性诱拐未成年人的恶意成年人为核心研究对象，系统分析其grooming、predation、offending及控制行为模式，目的在于支持检测软件开发和预防在线性剥削，属于社交工程与内容攻击范畴的攻防安全研究。
- 27242_1981_online-computer-auditing-through-continuous-and-intermittent-simulation.md | Online computer auditing through continuous and intermittent simulation | 1981 | MIS Quarterly: Management Information Systems
  - 摘要前 250 字: A new computer auditing technique, called Continuous and Intermittent Simulation (CIS), is introduced. It has been specifically designed as a compliance auditing technique for timesharing systems that can be used to audit internal controls. CIS is an
  - 关键词: Computer auditing; Internal auditing; Internal controls; Online auditing; Parallel simulation | 
  - 判定理由: 文章核心是面向在线系统的审计与监控技术，用于检测安全漏洞、未经授权的数据库访问、欺诈性代码和非法穿透等对抗行为，属于攻防安全范畴。
- 27203_1983_the-data-dictionary-an-evaluation-from-the-edp-audit-perspective.md | The data dictionary: An evaluation from the EDP audit perspective | 1983 | MIS Quarterly: Management Information Systems
  - 摘要前 250 字: The data dictionary system Is a documentation source that is useful for management reviews of existing and proposed systems, EDP audits, and system development functions. Early data dictionary systems had limitations that reduced their effectiveness 
  - 关键词: Data dictionary; Data management; Database administration; Database management systems; EDP auditing | 
  - 判定理由: 文章从EDP审计视角评估数据字典，核心内容包括利用数据字典检测和防止未授权源代码修改等内部恶意行为，属于攻击防御与审计检测范畴。
- 26923_2018_identity-management-and-tradable-reputation1.md | Identity management and tradable reputation | 2018 | MIS Quarterly: Management Information Systems
  - 摘要前 250 字: Online reputation trading is a new phenomenon facilitated by the prosperity of e-commerce and social networks. Whether reputations will be reliable when people can purchase rather than build them originally is a natural concern and also a challenge t
  - 关键词: Audit; Electronic market; Identity management; Online community; Reputation | Online systems; Separation; Audit; Electronic market; Identity management; On-line communities; Reputation; Electronic commerce
  - 判定理由: 文章研究在线声誉交易中低能力者购买好声誉并欺骗消费者的对抗性行为，并通过审计与声誉系统设计实现分离防御，核心为在线市场身份/声誉真实性的防御。
- 28238_2022_an-economic-analysis-of-rebates-conditional-on-positive-reviews.md | Racial Bias in Customer Service: Evidence from Twitter | 2022 | Information Systems Research
  - 摘要前 250 字: This paper provides the first large-scale evidence of business-to-customer racial bias (B2C bias) on a digital platform, on which the perpetrators are individual employees who act on behalf of a company and the victims are customers. This is in contr
  - 关键词: customer service; deep learning; racial bias; social media | Character recognition; Deep learning; Face recognition; Sales; Social networking (online); Business to customers; Call centers; Corporates; Customer-service; Deep learning; Digital platforms; Large-sc
  - 判定理由: 文章以策略性卖家通过‘好评返现’操纵在线评论为核心，明确使用‘fake reviews’‘review manipulation’等概念，并讨论平台检测与治理对策，属于评论/评分操纵这一攻击类型。

## B. 噪声中疑似安全文献的判定复核（抽样）

- On information technology and the safety of police officers | 2019 | Decision Support Systems
  - status=no_security_relevance include=False
  - reason: 研究核心是警察IT使用对警官职业安全（减少袭击/死亡）的影响，属于传统犯罪预防与执法优化，不涉及信息系统攻防或恶意技术攻击。
  - decision: 文章主题为IT对警察职业安全的影响，恶意行为者是现实罪犯而非针对信息系统的对抗者，损害对象为人身安全而非信息安全属性，不满足攻防安全核心定义。
- Can bots help create knowledge? The effects of bot intervention in open collaboration | 2021 | Decision Support Systems
  - status=no_security_relevance include=False
  - reason: 全文研究机器人（bots）干预对wikiHow开放协作平台用户参与度的影响，不涉及恶意行为者、攻击或安全防御。
  - decision: 研究对象是良性bot对开放协作用户参与度的影响，不涉及信息系统攻击、恶意行为或安全防护。

## C. 99 篇（v2 算法开发金标准）在新金标准 388 中的覆盖：92/99

- 5972 | 05972_2016_secure-attribute-sharing-of-linked-microdata.md | status=security_peripheral_context reason=文章关注组织间共享链接微数据时通过掩蔽保护敏感属性值，属于统计披露控制与隐私保护数据共享，假设共享双方相互信任，不存在恶意或对抗行为者，亦非围绕攻击或漏洞的攻防研究。
- 13656 | 13656_2007_complex-problem-solving-identity-matching-based-on-social-contextual-information.md | status=security_peripheral_context reason=研究核心是执法数据库中的身份匹配算法，用于犯罪调查中的记录关联，属于传统执法优化，不涉及信息系统攻防对抗。
- 14514 | 14514_2007_managing-user-relationships-in-hierarchies-for-information-system-security.md | status=security_peripheral_context reason=文章聚焦于设计基于数论的密钥对方案来管理用户层级关系，属于一般性访问控制/信息保护机制，未涉及攻击者、恶意行为或具体的攻防评估。
- 9492 | 09492_2006_matching-information-security-vulnerabilities-to-organizational-security-profiles-a-genetic-algo.md | status=no_security_relevance reason=文章核心是使用遗传算法优化安全技术组合以最小成本覆盖漏洞，属于组织信息安全投资决策与资源配置，未以恶意行为者或攻防检测/防御为研究核心。
- 12794 | 12794_2020_hiding-sensitive-information-when-sharing-distributed-transactional-data.md | status=security_peripheral_context reason=文章研究零售交易数据共享前的敏感项集隐藏（数据净化）算法，目的是防止商业伙伴挖掘出促销等商业敏感模式，不涉及恶意或对抗行为者，非信息系统攻防安全。
- 13760 | 13760_2013_secure-federation-of-semantic-information-services.md | status=security_peripheral_context reason=文章核心是安全联邦架构设计（访问控制、认证、传输安全），没有以恶意行为者或攻防对抗作为研究核心，且属于无攻击建模的访问控制方案。
- 19544 | 19544_2012_constructing-a-reliable-web-graph-with-information-on-browsing-behavior.md | status=security_peripheral_context reason=文章核心是利用浏览行为构建可靠Web图以改进页面质量估计，虽有垃圾页面识别作为评估任务，但恶意行为者并非研究核心，攻击/防御不是研究焦点。