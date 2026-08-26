# 金标准（全库全文筛选 388 篇）× 三层检索：对比审计

- 金标准：`ais_basket_security_relevance_fulltext_flash_v1` security_include=true，388 篇（deepseek-v4-flash 全文判定，13,909 篇全量，0 失败）
- M1 元数据检索（Title+Abstract+Keywords）：2494 条
- F2 head-8000 全文检索：4896 篇
- F3 全文检索：10093 篇

| 检索层 | 金标准召回 | 召回率 | 命中数 | 对金标准的精度(命中∩金/命中) |
|---|---|---|---|---|
| M1 元数据 | 363/388 | 93.6% | 2494 | 14.6% |
| F2 head-8000 | 381/388 | 98.2% | 4896 | 7.8% |
| F3 全文 | 387/388 | 99.7% | 10093 | 3.8% |

## M1 漏检的金标准（25 篇）

- 00358_2020_why-individual-employees-commit-malicious-computer-abuse-a-routine-activity-theory-perspective.md | Why Individual Employees Commit Malicious Computer Abuse: A Routine Activity Theory Perspective
  - F2命中=True F3命中=True | 摘要前180字: 无CSV记录
- 01704_2024_doxing-on-social-networking-sites-an-extension-of-the-social-cognitive-theory-of-moral-thought-a.md | Doxing on Social Networking Sites: An Extension of the Social Cognitive Theory of Moral Thought and Action
  - F2命中=True F3命中=True | 摘要前180字: Doxing on social networking sites (SNS doxing) has attracted scholarly and public attention due to the devastating consequences that this behavior can have on individuals and socie
- 04526_2011_multi-tag-and-multi-owner-rfid-ownership-transfer-in-supply-chains.md | Multi-tag and multi-owner RFID ownership transfer in supply chains
  - F2命中=True F3命中=True | 摘要前180字: In any supply chain, there is a high likelihood for individual objects to change ownership at least once in their lifetime. As RFID tags enter the supply chain, these RFID-tagged o
- 05690_2005_model-checking-for-design-and-assurance-of-e-business-processes.md | Model checking for design and assurance of e-Business processes
  - F2命中=True F3命中=True | 摘要前180字: Use of the Internet for electronic business has the potential to revolutionize the way many businesses are conducted. Yet, several businesses have fallen victim to problems in info
- 06092_2008_online-reputation-systems-design-and-strategic-practices.md | Online reputation systems: Design and strategic practices
  - F2命中=True F3命中=True | 摘要前180字: This paper provides a comprehensive framework for evaluating the effects of feedback systems, and the potential problems with feedback systems, on seller incentives to provide high
- 06126_2016_internet-aggression-in-online-communities-a-contemporary-deterrence-perspective.md | Internet aggression in online communities: a contemporary deterrence perspective
  - F2命中=True F3命中=True | 摘要前180字: Internet users' activities are critical to the development and success of Web 2.0 systems, such as online communities. Within the community's participation, knowledge sharing, and 
- 09872_2021_information-technology-and-government-corruption-in-developing-countries-evidence-from-ghana-cus.md | INFORMATION TECHNOLOGY AND GOVERNMENT CORRUPTION IN DEVELOPING COUNTRIES: EVIDENCE FROM GHANA CUSTOMS
  - F2命中=False F3命中=True | 摘要前180字: The literature on information technology (IT) and government corruption in developing countries indicates contradictory evidence about the realization of anti-corruption effects. S
- 10238_2011_does-ethical-ideology-affect-software-piracy-attitude-and-behaviour-an-empirical-investigation-o.md | Does ethical ideology affect software piracy attitude and behaviour An empirical investigation of computer users in China
  - F2命中=False F3命中=True | 摘要前180字: This study empirically examines Chinese computer users ethical ideology and its relationship to their software piracy attitude and behaviour. The investigation reveals several impo
- 10634_2009_griefing-in-virtual-worlds-causes-casualties-and-coping-strategies.md | Griefing in virtual worlds: Causes, casualties and coping strategies
  - F2命中=True F3命中=True | 摘要前180字: A virtual world is a computer-simulated three-dimensional environment. They are increasingly being used for social and commercial interaction, in addition to their original use for
- 12724_2019_an-economic-analysis-of-platform-protection-in-the-presence-of-content-substitutability.md | An Economic Analysis of Platform Protection in the Presence of Content Substitutability
  - F2命中=False F3命中=True | 摘要前180字: Online platforms, such as App Store and Kindle, are facing a common dilemma: while the implementation of technology-based protection impedes piracy and hence boosts demand from leg
- 13670_2016_intellectual-property-norms-in-online-communities-how-user-organized-intellectual-property-regul.md | Intellectual property norms in online communities: How user-organized intellectual property regulation supports innovation
  - F2命中=False F3命中=True | 摘要前180字: In many online communities, users reveal innovative and potentially valuable intellectual property (IP) under conditions that entail the risk of theft and imitation. When there is 
- 14334_2009_pricing-schemes-for-digital-content-with-drm-mechanisms.md | Pricing schemes for digital content with DRM mechanisms
  - F2命中=True F3命中=True | 摘要前180字: In this paper, utilizing game-theoretic model, we examine the impact of collaborative structure, content quality, and network environment on the development of pricing scheme and D
- 15370_2019_an-integrative-theory-addressing-cyberharassment-in-the-light-of-technology-based-opportunism.md | An Integrative Theory Addressing Cyberharassment in the Light of Technology-Based Opportunism
  - F2命中=True F3命中=True | 摘要前180字: Scholars are increasingly calling for a deeper understanding of cyberharassment (CH) with the goal of devising policies, procedures, and technologies to mitigate it. Accordingly, w
- 15516_2022_technological-entitlement-its-my-technology-and-ill-ab-use-it-how-i-want-to.md | TECHNOLOGICAL ENTITLEMENT: IT’S MY TECHNOLOGY AND I’LL (AB)USE IT HOW I WANT TO
  - F2命中=True F3命中=True | 摘要前180字: Entitlement has been identified as a potentially valuable employee characteristic in the prediction of computer abuse but has not been studied systematically in the IS domain. We i
- 20849_2000_edi-controls-design-support-system-using-relational-database-system.md | EDI controls design support system using relational database system
  - F2命中=False F3命中=True | 摘要前180字: The purpose of this paper is to introduce EDIRDB (EDI controls design support system using a relational database system), a prototype audit support system based on a relational dat
- 21281_2004_sdmi-based-rights-management-systems.md | SDMI-based rights management systems
  - F2命中=True F3命中=True | 摘要前180字: Building digital rights management (DRM) systems for electronic commerce is still a complex task because such systems are usually required to manage a large set of different media 
- 22211_2003_the-is-risk-analysis-based-on-a-business-model.md | The IS risk analysis based on a business model
  - F2命中=True F3命中=True | 摘要前180字: The disruption of operations due to IS failure becomes more important as IS has become an increasingly essential component of the organization's operations and can affect its strat
- 22611_2000_flaming-among-first-time-group-support-system-users.md | Flaming among first-time group support system users
  - F2命中=False F3命中=False | 摘要前180字: Numerous benefits, including increases in efficiency, effectiveness, and participant satisfaction, have been noted in the literature when electronic meetings are used in place of t
- 23404_1990_information-systems-forensics.md | Information systems forensics
  - F2命中=True F3命中=True | 摘要前180字: This paper discusses some current issues and methods related to the investigation and successful prosecution of crimes committed with or against computerized information systems. T
- 25278_2003_identification-of-comment-authorship-in-anonymous-group-support-systems.md | Identification of comment authorship in anonymous group support systems
  - F2命中=False F3命中=True | 摘要前180字: This study examines whether technically "anonymous" comments entered by participants during group support system (GSS) brainstorming sessions are, in fact, unidentifiable. Hypothes
- 25539_2021_exposing-patterns-of-adult-solicitor-behaviour-towards-a-theory-of-control-within-the-cybersexua.md | Exposing patterns of adult solicitor behaviour: towards a theory of control within the cybersexual abuse of youth
  - F2命中=True F3命中=True | 摘要前180字: The online solicitation of youth has been established as an unintended consequence of the connectedness afforded individuals through computer-mediated conversation. Information sys
- 26923_2018_identity-management-and-tradable-reputation1.md | Identity management and tradable reputation
  - F2命中=True F3命中=True | 摘要前180字: Online reputation trading is a new phenomenon facilitated by the prosperity of e-commerce and social networks. Whether reputations will be reliable when people can purchase rather 
- 27203_1983_the-data-dictionary-an-evaluation-from-the-edp-audit-perspective.md | The data dictionary: An evaluation from the EDP audit perspective
  - F2命中=True F3命中=True | 摘要前180字: The data dictionary system Is a documentation source that is useful for management reviews of existing and proposed systems, EDP audits, and system development functions. Early dat
- 27242_1981_online-computer-auditing-through-continuous-and-intermittent-simulation.md | Online computer auditing through continuous and intermittent simulation
  - F2命中=True F3命中=True | 摘要前180字: A new computer auditing technique, called Continuous and Intermittent Simulation (CIS), is introduced. It has been specifically designed as a compliance auditing technique for time
- 28238_2022_an-economic-analysis-of-rebates-conditional-on-positive-reviews.md | Racial Bias in Customer Service: Evidence from Twitter
  - F2命中=True F3命中=True | 摘要前180字: This paper provides the first large-scale evidence of business-to-customer racial bias (B2C bias) on a digital platform, on which the perpetrators are individual employees who act 

## M1 命中但未通过金标准（噪声，2131 条）抽样 25 条

- Can bots help create knowledge? The effects of bot intervention in open collaboration | 2021 | Decision Support Systems
- Bigger from a distance: The moderating role of spatial distance on the importance of traditional and rhetorical quality signals for transactions in crowdfunding | 2022 | Decision Support Systems
- Morality and Computers: Attitudes and Differences in Moral Judgments | 1999 | Information Systems Research
- The domestication of online technologies by smaller businesses and the 'busy day' | 2011 | Information and Organization
- STP technology: An overview and a conceptual framework | 2006 | Information and Management
- Information systems solutions for environmental sustainability: How can we do more? | 2016 | Journal of the Association for Information Systems
- Maximizing accuracy of shared databases when concealing sensitive patterns | 2005 | Information Systems Research
- Adversarial knowledge-sharing in a coopetitive environment: a darknet hacker context | 2025 | European Journal of Information Systems
- Understanding the CEO/CIO relationship | 1992 | MIS Quarterly: Management Information Systems
- Improving Phishing Reporting Using Security Gamification | 2022 | Journal of Management Information Systems
- Empowering crisis information extraction through actionability event schemata and domain-adaptive pre-training | 2025 | Information and Management
- Evaluation of on-line trading systems: Markov-switching vs time-varying parameter models | 2017 | Decision Support Systems
- Hate Speech Detection on Online News Platforms: A Deep-Learning Approach Based on Agenda-Setting Theory | 2025 | Journal of Management Information Systems
- Sustaining collaborative software development through strategic consortium | 2021 | Journal of Strategic Information Systems
- A framework to limit systems developers' legal liabilities | 1996 | Journal of Management Information Systems
- How to leverage digital platforms in enhancing organizational resilience: The roles of supply chain integration and market orientation | 2026 | Decision Support Systems
- WEARABLE SENSOR-BASED CHRONIC CONDITION SEVERITY ASSESSMENT: AN ADVERSARIAL ATTENTION-BASED DEEP MULTISOURCE MULTITASK LEARNING APPROACH | 2022 | MIS Quarterly: Management Information Systems
- An exploratory study to identify the critical factors affecting the decision to establish Internet-based interorganizational information systems | 2004 | Information and Management
- Impact of top management leadership styles on ERP assimilation and the role of organizational learning | 2017 | Information and Management
- A comparison of transaction cost, agency, and knowledge-based theory predictors of IT outsourcing decisions: A U.S.-Japan cross-cultural field study | 2007 | Journal of Management Information Systems
- Technocognitive Structuration: Modeling the Role of Cognitive Structures in Technology Adaptation | 2025 | Journal of the Association for Information Systems
- On information technology and the safety of police officers | 2019 | Decision Support Systems
- Strategic signaling through cloud service certifications: Comparing the relative importance of certifications’ assurances to companies and consumers | 2019 | Journal of Strategic Information Systems
- A nomological network of customers’ privacy perceptions: linking artifact design to shopping efficiency | 2019 | European Journal of Information Systems
- Detection of naming convention violations in process models for different languages | 2013 | Decision Support Systems