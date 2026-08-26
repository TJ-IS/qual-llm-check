---
otero_id: 4954
otero_key: "HPREU24P"
title: "Business rules management in healthcare: A lifecycle approach"
authors: "Matthew L. Nelson; Ravi Sen"
year: "2014"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2012.10.044"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Business rules management in healthcare: A lifecycle approach

Matthew L. Nelson <sup>a</sup>, Ravi Sen <sup>b,</sup>⁎

<sup>a</sup> Illinois State University, United States

<sup>b</sup> Texas A&M University, United States

a r t i c l e i n f o

Available online 6 November 2012

Keywords: Business rules management Business rules engine Healthcare business rules management Business Rules Lifecycle

## a b s t r a c t

This paper proposes a framework to apply business rules management (BRM) to healthcare service delivery. Implementation of recently government-mandated quality standards for healthcare provider requires them to modify or change their business processes, practices, and approach to healthcare delivery. An automated business rules management will provide signi<sup>fi</sup>cant bene<sup>fi</sup>ts to these providers. The bene<sup>fi</sup>ts include greater control, improved <sup>fl</sup>exibility, and the ability to rapidly deploy business rules across processes, information systems and channels (web, legacy, wireless and otherwise). These bene<sup>fi</sup>ts, in addition to trends in service orientated architectures, web semantics, and business process management, have spawned an emerging business rules engine (BRE) market. Despite these developments, little has been published in MIS journals that examine the management of business rules management systems (BRMS) development and deployments in general, and in healthcare service sector in particular. Making use of structuration research methods, we collect data from leading developers, end-users, researchers and thought leaders from the industry. Data collection results revealed a business rules management lifecycle inclusive of these steps: align, capture, organize, author, distribute, test, apply, and maintain. The contextual in<sup>fl</sup>uences, actors, inputs, outputs and artifacts are identi<sup>fi</sup>ed in each step. Academic and managerial contributions, as well as recommendations for future research are provided.

© 2012 Elsevier B.V. All rights reserved.

## 1. Introduction

The healthcare industry faces unprecedented changes and reform. Recently introduced government legislation encompassing quality standards for healthcare service providers are forcing providers to re-evaluate and analyze their existing business processes and practices. These standards require the healthcare service to provide appropriate and relevant care, avoid patient complications, and collect information on illness/diseases, their treatment, and the results of the treatment providers. In addition, to ensure information quality, this information must also be collected and validated by the hospitals as the patient is treated, not after the fact. If healthcare providers fail to meet these standards, this may result in reduced reimbursements from government-funded healthcare programs. Healthcare service providers will also need to adapt to best treatment practices and other benchmarks that emerge from the mining of nationwide data that is being collected as part of the mandated standards [17,25,57]. Add to this list a litany of industry norms, state and local legislation and existing federal laws such as the Health Insurance Portability and Accountability (HIPPA) Act of 1996, the Health Information Technology for Economic and Clinical Health (HITECH) Act of 2009 and a growing list of qualifying exceptions (and challenges) to the Health Care Affordability Act of 2009. In short, healthcare service providers need to reassess their business rules on a regular basis to ensure that they comply with the mandated standards and laws of today and best practices of tomorrow. This leads to important questions such as, “What are business rules?” and “How to best manage them?”

Whether we realize it or not, we're confronted with business rules (BR) numerous times on a daily basis. Take for example, a simple trip to the pharmacy. From a competitive perspective, business rules are structured around which drugs are offered at a sales discount, the duration of the discount, and conditions of the discount. From a regulatory perspective, business rules require restricted consumer access to certain drugs, prescribe which drugs can (and cannot) be shelved with other goods and de<sup>fi</sup>ne the allowable shelf duration of pharmaceutical products. From an industry norms perspective, business rules are used to designate certain types of check-out lanes, identify which drugs are placed near exits/entrances, and to establish return policies. From a legislative perspective, business rules dictate the sales tax rate on categories of drugs, require proof of age prior to the purchase of other drugs, and require a prescription from a licensed medical doctor prior to the purchase of still other drugs.

It is not dif<sup>fi</sup>cult to imagine that a single item, such as a prescription strength liquid cough syrup may be affected by all of the above rules. There are more than 55,000 community pharmacies across the United States, dispensing (and managing) more than 3.6 billion annual prescriptions, at a retail cost exceeding \$250 billion [13]. Pharmacies store and stock thousands of items with high turnover rates, impacted by hundreds of different business rules from a variety of sources. These rules are embedded throughout the store's pointof-sale systems, inventory systems, promotion systems, accounts payable, product placement systems and their associated business processes. This was a trip just through a pharmacy store. When one considers the volatility to which business rules are added or changed in the healthcare industry which transcend time-zones, seasons, information systems, statutory boundaries and channels (web, legacy, wireless or otherwise), the complexity of BR management can grow on an exponential basis.

## 1.1. Business rules management benefits

Fortunately, there has been some research and development to assist organizations with many of the technical challenges associated with business rules. In industry, for example, vendors such as ILOG SA, Blaze Advisor™ and Pega Systems, Inc. have been developing business rule engines (BRE) since the late 1980s and are now leaders in an emerging BRE segment [7,27]. In academia, the computer sciences and engineering outlets have been active in BR research, with extensive studies in rule programming, meta-modeling, rule mining, rules engines, business user interfaces and their role in services orientated architectures (SOA). Furthermore, joint academic and industry developed Object Management Group's (OMG) Semantics of Business Vocabulary and Business Rules (SBVR) standards (released in September 2006), which are intended to provide standards surrounding BR structure, terminology, classi<sup>fi</sup>cations and meaning in BR authoring and repositories [51].

This research and development is beginning to pay-off. The BRE market has grown to a half billion U.S. dollars in annual product sales alone with more than 50 vendors worldwide [54]. The Business Process Management (BPM) market, that BRE products are traditionally closely aligned, has an estimated market size of \$1.9 billion in annual sales and annual growth rate of 15% [55]. The drivers underlying this growth are the bene<sup>fi</sup>ts enabled to organizations with effective BREs including improved interoperability [12], greater <sup>fl</sup>exibility and control over deploying BRs across channels and systems, enhanced quality of BR updates, reduced cost and greater speed of implementing rule updates. Furthermore, the SBVR release provides a foundation for extending these bene<sup>fi</sup>ts beyond the enterprise level and into supply-chains and industrial groups.

## 1.2. Research questions

Despite this substantial progress in business rules research, there has been little published in MIS academic outlets relating to the business rules topic and more speci<sup>fi</sup>cally to managing BR developments and deployments. The research and development presented thus far is traditionally at a micro-level, pertaining to technical considerations such as rule engines, rule mining, rule authoring and interfaces. BR automation, however, is a quintessential example of the integration of business process, information technology and human interaction. Organizations need an understanding of the entire BR perspective and context from development through implementation. For example, the IRS recently spent a considerable amount of money and time in formal solicitation and evaluating bids from BRE vendors, only to realize during an audit of the bidding process by an inspector general that a BRE was not actually required for their business rules project and should have only been considered under certain conditions [36].

In another widely publicized BR project failure, the Government of Canada's CAN\$300 million initial business rules project failure was due (in part) to front loading the project with a plethora of related (but out of scope) initiatives such as legacy systems modernization efforts [9]. Finally, Australia's Department of Family and Community Services found that 34 versions of a BR vendor's contract existed and had been changed 129 times. The estimated cost of project failure is AU\$64 million [41].

As the business drivers for automating BRs in organizations continue to grow and the bene<sup>fi</sup>ts of BR automation continue to be realized the need for viewing BR management at a higher contextual level and with a broader lifecycle perspective are mounting. Indeed, BR project management and implementation failures (such as those described above) are growing more commonplace in the absence of such studies. We seek to raise the level of discussion by considering the entire business rules management lifecycle with greater breadth, than depth and examining the larger context to which BR management <sup>fi</sup>ts in an organization. The underlying research questions include-

• Does a general process or lifecycle exist that organizations follow when automating and managing business rules?

• What steps are involved and what effective practices can be solicited from these organizations to prevent project derailment?

By utilizing a structuration lens, we explore these questions through a literature search, structured interviews and data collection from leading BR end-users, developers, and thought leaders. The study was conducted during two time periods (set 12 months apart) and the results synthesized, using techniques in structuration MIS literature to develop a business rules management lifecycle (BRMLC). The academic contributions include identi<sup>fi</sup>cation of initial BR research streams, highlighting distinctions between knowledge management versus business rules management lifecycles, extending structuration techniques into the BR area and describing the BR <sup>fi</sup>t into the larger service science, management and engineering (SSME) research context with similar initiatives such as SOA, process management, work<sup>fl</sup>ows, web semantics and the management of BRMS. Managerial contributions include an understanding of how healthcare organizations can manage their BR automation implementations, a broader perspective of the full BRMLC from initiation through maintenance and how BR management <sup>fi</sup>ts into the larger enterprise-wide context.

## 2. A literature review of business rules management systems (BRMS)

A literature search was conducted to better understand the extent, type, and streams of BR related research. The formal search focused in MIS academic journals, with less structured searches in computer science and engineering related journals and the business press.

## 2.1. Literature review methodology

The primarily literature review encompassed academic MIS journals covering time periods from the late 1980's through 2008. This time period was selected to coincide with origins and developments of modern-day BRMS in academia and industry. The journals were selected based on their ranking and propensity to published articles relating to decision management and rules-based technologies. The manuscripts were coded and highlights of the literature review results are provided below.

## 2.2. Distinguishing BRMS

Modern-day BRMS has its roots in early arti<sup>fi</sup>cial intelligence (AI), expert systems and more recently in knowledge management systems. Arguably, the mid to late 1980s is when the modern-day BRs segment began to distinguish itself from the AI and expert systems arenas. Researchers and developers began to realize the practical real-world applications of the initial arti<sup>fi</sup>cial intelligence systems. Sheil comments in her 1987 article about the practical shortcomings

• What is the relationship between IT and the business units regarding business rules management?

• Who are the key actors in the business rule management process? Who are the critical stakeholders?

of large-scale AI systems, “The ability to provide highly customized, integrated applications software has turned out to be a major strength of AI technology. The short-term value is clear....rules-based programming is an effective way to arrive at a clear, concise, yet easily extended statement of the logic underlying many discrimination and classi<sup>fi</sup>cation tasks. The simple rules-based interpreter is an effective technology for a wide-class of simple, practical problems.” [53, pages 91–97].

Sheil advocates for the automation of these routine daily decisions and to evaluate the execution of these decisions along <sup>fi</sup>ve lines: consistency, precision, speed, agility and cost. The author was not alone in this sentiment, since it was during this timeframe that initial development of many of the now dominant modern-day BRE in the market place began in earnest: Gensym Corporation's G2 in 1986 by a university professor, Haley Systems, Inc. in 1989 by a medical student, ILOG SA in 1985 by a French university professor and BlazeAdvisor™ in 1988 [7,18,22,27].

## 2.3. Results from MIS literature survey

The literature survey resulted in six emerging focal areas of business rules related research in MIS journals, including an examination of business drivers associated with BRMS, rule mining, BR repositories (including rule authoring, modeling, and user interfaces), automating BR (including BR engines and web-services), BR in the context of work<sup>fl</sup>ow management, and domain speci<sup>fi</sup>c studies (that examined BR use in a narrowly de<sup>fi</sup>ned industry or market segment).

Overall, the largest number of articles examine the business drivers pushing organizations towards IS architectural integration [24], IS infrastructure <sup>fl</sup>exibility [15] and integration [29], the use of BR in B2B e-commerce models [56], the effect of little decisions adding up [48] and dynamic synchronization of strategy and IT [46]. Several domain speci<sup>fi</sup>c studies have examined rules-based implementations including lower back pain diagnostics [34], assignment of technicians to service faults [32], forecasting S&P 500 index futures [59], build-to-order [28], customer order scheduling [62,8] and others [4,6,16,21]. MIS researchers have also studied BR automation with the use of a BR engine [14], without the use of an inference engine [26], using goals to design and verify a rule base [10] and detecting anomalies in hybrid knowledge-based systems [19,37]. There have also been select recent articles that have related the BR context to other organizational initiatives such as mobile devices [31], business processes [47,11], and inter-organizational work<sup>fl</sup>ows [60,3,5]. Finally, one study indirectly discussed the use of a rule repository through the use of managing metadata in data warehouses [52] and two studies examined the potential use of common data mining techniques in BR mining through reverse software engineering [61] and a three-tiered knowledge management discovery [50].

These studies provide beginnings of a BR research program, but collectively the research often overlooks major steps in BR management and fails to focus on BR speci<sup>fi</sup>c issues and the larger context that rules play in organizations. For example, the architectural integration and <sup>fl</sup>exibility studies discuss the general bene<sup>fi</sup>ts of these initiatives, but only indirectly present the role that BRs contribute. The same was found in data mining and knowledge management discovery manuscripts. Important dynamics in BR management are also excluded, such as IT–business alignment and the separation of the rule management and implementation environments.

Important steps in managing BRs are also overlooked such as developing an organization-wide BR meta-model and the need for a standalone (independent) rules repository. More profoundly, little was found on managing BR related development projects or other ties that BR projects have with related enterprise wide initiatives (active real-time decision making, systems integration across channels and applications, enterprise wide agility and others). The few studies found with lifecycle perspectives [39,1] focus on knowledge management systems and production decision support systems, as opposed to modern-day BRMS. These lifecycles can act as a good starting point, but need more speci<sup>fi</sup>city in a BR context.

## 3. Research methodology

To address the research questions, a structuration lens is employed in the research design, with an emphasis towards developing a process model explanation. Structuration theory is one of the most widely and effectively used methods by IS researchers [44,45]. Consistent with many IS studies where preliminary indicators suggest that a de facto process used by organizations exists, we take a positivist stance with this study [42]. An interior perspective and a constitutive mode of analysis were intentionally utilized in the study's design to better insure compatible alignment of process steps that transcend organizations and actors [44]. Qualitative research methods are employed with emphasis on structured but open-ended interviews with process actors including industry thought leaders, developers, end-users, and other stakeholders [33]. Although the authors do not necessarily claim that this paper quali<sup>fi</sup>es as an ethnographic study, additional qualitative data collection techniques were utilized to better acclimate the authors to the stakeholders in the industry including on-site visits, meeting presentations, reviewing company documents, industry white-papers, case studies and others [38].

Our research methods, interview questions, and process step descriptions are in<sup>fl</sup>uenced by Klein and Myers' [30] principles in conducting interpretive <sup>fi</sup>eld research, Poole and Descanctis' [44] seven interlocking requirements for structuration research and Pozzebon and Pinsonneault's [45] assessment of structuration theory in the IS <sup>fi</sup>eld. Based on choices in the structuration research [44], the level of analysis is a global level (identifying the BR process that is traditionally followed across organizations), with a related structures focus (narrowly focused on a closely related group of structures), with a framing perspective focused from a structure view (at an overall process level) with the focus shifting towards an actor's view at the individual process step level. The dynamics focus is simply acknowledging that higher order process steps exist, with an emphasis on system stability (as opposed to system changes), all with a positive stance.

## 3.1. Respondent profiles

57 organizations participated in the structured interviews in the <sup>fi</sup>rst round of data collection and 51 (90%) were available and agreed to participate in the second round. See Table 1 for the list of structured questions/topics. Three members of the research team were present during interview sessions. The same principal investigator led the participants through the structured questions, while all research team members took notes. The research team conducted “clean-up” sessions after interviews to compare responses. Interview sessions lasted two and one-half hours (on average).

![](/api/attachments/HPREU24P/fulltext/images/837007572e19dc0744abcca28b2cb8c4afa74678e36cb45a9076179ac6272071.jpg)  
Fig. 1. Business Rules Management Lifecycle (BRLC)

The participating organizations had three to four representatives in each session. At a minimum, this group would include a BR implementation project manager (with a business focus) and a BR technical representative (e.g. developer, architect, and engineer). Thirteen sessions included the organization's CEO/founder and six sessions also included the organization's CTO/CIO. Four sessions included thought leaders from the BR industry including two business rule handbook authors, a research scientist from the Software Engineering Institute at Carnegie Mellon and a member of the SBVR initiative. In total, the individual respondents had direct experience with 513 BRMS implementations. One hundred invitations were extended to the identi<sup>fi</sup>ed pool of potential respondents. Potential respondents were selected based on their organization's involvement in BR product development, services, end-users and other BR industry stakeholders. A review of published case studies, industry white papers and other business press were reviewed to identify <sup>fi</sup>rms that have demonstrated a willingness to discuss their BR implementations.

## 4. Findings

Fig. 1 contains the BRMLC for the healthcare industry as synthesized from the research methodology and setting. The eight steps in a nutshell, include alignment/plan of the respective BR domains with the organization's overarching data model and strategy; capture rules from the various sources; organize the rules and begin managing them in rules authoring. Once the business rules are centrally stored and managed, then begin distributing (or sharing) the rules, test the rules for interoperability and apply ‘go live’ with the automation, and <sup>fi</sup>nally maintain.

Three important characteristics of this structuration should be highlighted at the outset. First, depicting the BRMLC in this manner provides a picture of the entire perspective (regardless of the domain), as opposed to the literature survey results that focused on narrow or omitted segments. Second, lifecycle steps can be grouped into three higher level environments of align, rule management and implementation (see Fig. 2). Third, considering the three environments from a higher contextual perspective allows us to examine how they interact and vary, within the larger context of the organization and the BRMLC.

As an illustration, alignment is primarily a business strategy activity that's led by senior managers (e.g. physicians and healthcare administrators) and IT leaders, rule management is a business operations activity that is owned by business staff, and the implementation environment is primarily the responsibility of IT (e.g. vendors of BRM software and applications). The rate of change in align is slow, varying with the organization's overall mission and strategic direction. The rate of change in the rule management can reach high levels, depending on rule volumes, volatility and others. The implementation environment will experience a slower rate of change, depending on the <sup>fi</sup>rm's technological infrastructure, IT direction, and platforms.

Alignment has a longer-term focus, however, in<sup>fl</sup>uenced by the healthcare provider's direction and vision (e.g. lower healthcare costs, better quality of healthcare, and most effective care). Rule management will have a short-term focus (e.g. compliance with emerging government mandates), a need for a real-time active decision making, and is in<sup>fl</sup>uenced by SBVR and the industry's web semantic standards. The implementation environment has a mid-range focus and in<sup>fl</sup>uenced by an array of related top-level initiatives such as SOA, work<sup>fl</sup>ow, process and channel management. Detailed descriptions of each step are provided below. As recommended in the structuration literature, each step includes highlights of the step's inputs, outputs, processes, actors and effects.

<table><tr><td></td><td>Align</td><td>Rule Management</td><td>Implementation</td></tr><tr><td>Owners</td><td>Senior Physicians, Managers &amp; IT Leaders</td><td>Operations / Business Staff</td><td>IT Staff</td></tr><tr><td>Organization Contexts</td><td>Enterprise-wide VisionIT Directional Setting</td><td>SBVR, VSC, rule volatilityWeb semantics, rule volumesBusiness process, enforcement</td><td>SOA, Channel MgmtDomain scope, BPM, WFM</td></tr><tr><td>Time Horizon</td><td>Long-termBased on organization&#x27;s longer-term vision.</td><td>Short-termReal time with active execution,based on rule duration.</td><td>Mid-termBased on IT infrastructure changes and direction.</td></tr><tr><td>Rate of Change</td><td>Low</td><td>High</td><td>Low to Moderate</td></tr><tr><td>Sources</td><td>Strategic VisionSenior Management</td><td>Legislative, regulatory, competitive industry norms and many others</td><td>Rule repository</td></tr></table>

Fig. 2. Healthcare business rules management lifecycle environments.

## 4.1. Align

The <sup>fi</sup>rst step is to develop an organization-wide strategy and plan for deploying BR management projects and aligning the plan with similar enterprise wide initiatives. The actors include senior management from the business (e.g. physicians and healthcare administrators) and IT staff. Major activities include segmenting the universe of BRs impacting the organization into logical domains (e.g. by lines of business) and an analysis of business drivers underlying those domains. Resources and other artifacts include the organization's overarching data model, their strategic IT vision, including the systems integration plans for the enterprise and beyond. The output includes a high-level BR deployment plan organized by business segments, relations between the segments, priority areas, sequencing, tentative timelines and how the plan <sup>fi</sup>ts with similar organization-wide initiatives such as SOA, semantics, and IT–business alignment. The effects of this step include consistency with similar initiatives, maximizing the opportunity for rule reuse in later stages, and a BR management deployment roadmap driven by business needs. Additional insights from respondents emphasized the need to keep initial BRMS deployments small (and manageable) and a profound regret for sometimes overlooking this step.

## 4.2. Capture

Identi<sup>fi</sup>cation of potential BRs is impacting the domain segment in development. The actors include BR business and IT staff, rule mining vendors, domain experts (from industry and the <sup>fi</sup>rm), longer-term employees and others. The resources and artifacts include user manuals, legacy system code, business contracts, legislation, memos, e-mails, procedure manuals and others. The outputs will provide identi<sup>fi</sup>cation of an exhaustive list of potential BRs in<sup>fl</sup>uencing the chosen business segment. The procedures include data mining software that sweeps legacy code (a.k.a. rule mining), user manuals, business contracts, legislation and interviews with longer-term employees [35]. The effects of this step include exposing and formally identifying potential BRs that would otherwise be buried. Indirect effects include signi<sup>fi</sup>cant improvements in business process transparency and program code ef<sup>fi</sup>ciency opportunities. Additional insights from respondents emphasized the need to remain focused on BR management during this step due to the volume of process reengineering, program code remediation and other ef<sup>fi</sup>ciency opportunities that are exposed. Paulson and Wand's [43] and more recently Torino and Politecnico's [58] earlier studies in the legacy code ef<sup>fi</sup>- ciency techniques provide additional insights.

## 4.3. Organize

After the capture step identi<sup>fi</sup>es potential BRs, the extraction process involves veri<sup>fi</sup>cation that the item is a BR and an initial organization of the rules. The actors include the organization's BR business and IT representatives and domain experts. The inputs include the potential BRs identi<sup>fi</sup>ed in the prior step and the output is validated BRs and rule sets, with preliminary plans for where and how the rules will be implemented and updated. The rule outputs from this step are ready to be formally authored BRs. This step is traditionally time consuming and necessitates extensive manual intervention and analysis. Key procedures include removing out-of-scope or otherwise invalid BRs from capture results, assessing the quality of BR sources, grouping rules into related rule sets, and preparing rule update procedures (ownership, frequency, and timing). Additional procedures also include a mapping of where the rule will be implemented (systems, processes, and layers) and how the installation will occur. The effects of this step include substantial rule authoring time savings through elimination of redundant, out-of-scope, or non-BRs prior to the authoring process. Halle [23] and Ross [49] provide useful additional resources for organizing BRs, and others provide detailed suggestions for conducting BR pattern analysis [20].

## 4.4. Author

The thrust of step four is the conversion of implicit data into explicit knowledge through formal BR authoring. Actors in this step include the BR business staffs, the <sup>fi</sup>rm's management who has authorization to make the BR decisions, and domain experts who assist with interpreting contractual and legislative business rules [49]. Inputs include the organized BRs from the prior step and outputs include a fully authored business rule in a BR repository.

The BR repository is designed for and managed by the organization's business representatives (as opposed to the IT staff) in a user-friendly environment that makes use of standard business terminology (as opposed to programming code). Optimally, the BR repository should be centrally managed, independent from the implementation environment, owned and operated by the organization's business BR representatives. Establishing the repository in this manner is important towards enabling a dynamic shift from IT owning/managing BR updates back to business users. In essence, this permits the business staff to focus on their strengths (rule authoring and management) and permits the IT staff to focus on their strengths (managing the implementation environment).

Logic testing is included in authoring procedures as well, such as rule ambiguity, accuracy, completeness, and redundancy tests. Artifacts and resources include handbooks that provide in-depth business rules authoring from a business perspective [23,49], managing rule sets and aligning BR with the organization's information systems [34] and with service-orientated architecture initiatives [20]. The OMG's release of an adopted speci<sup>fi</sup>cation SBVR in 2006 is also an important artifact [51]. Its release through the OMG should provide signi<sup>fi</sup>cant strides in uniformity of rule authoring across organizational boundaries and industrial groups. Effects of this step include an enhanced understanding and communication of rules, higher quality rule development, enables a shift in control of rule updates from IT to the business staff, facilitates a clear distinction between the rule management versus the implementation environments, and affords the <sup>fi</sup>rm greater <sup>fl</sup>exibility in the selection of a technical implementation solution.

## 4.5. Distribute

This step requires sharing (or distributing) formally authored BR from the rule repository to the selected implementation environment(s). Inputs include BR from the rule repository and information from the organize step that includes preliminary assessments of where the rule needs to be implemented (systems, processes, and layer) and how the installation will occur. Ownership in the BRMLC now shifts to the IT staff to build out the implementation environment(s). A seamless interoperability is important to maintain the business orientation of the rules repository and allowing for control of BR updates to be retained by the business staff. The outputs include detailed decisions regarding how the automation between the rules repository and the distribution (destination) points will take place and a beta solution. Key actors will include BR vendors, the <sup>fi</sup>rm's IT staff, and IT management.

Although new techniques are routinely in development, three basic solutions include a business rules engine, a centralized service in an SOA, or a dedicated interface to the application (going direct). The solution choice depends on numerous variables including transaction volumes, rule volumes, frequency of rule changes (rule volatility), timeliness, rule scope, and the extent of BR implementations. For example, an application that runs high transaction volumes with near real-time processing expectations, would likely require a standalone dedicated interface (going direct) between the rule repository and the application to better insure that performance needs are met. Alternatively, a <sup>fi</sup>rm that is well established towards SOA (and has completed BR initiatives in other domains) would likely choose to establish their deployments as part of central SOA services. The effects of this step are increased <sup>fl</sup>exibility to design a solution that best <sup>fi</sup>ts with business needs and the envisioned IT architecture.

## 4.6. Test

This step insures that the interoperability between the repository and the implementation environment is working appropriately. Inputs in this step include the BRs from the repository via the selected implementation environment and the outputs include test results. Actors include the IT staff, business BR staff, BR vendors and domain experts. Testing procedures will generally focus in three areas; (1) unit testing, (2) integration testing that includes interoperability and connectivity testing from the rule repository to the application program and (3) acceptance testing. This testing should be distinguished from rule logic testing such as rule ambiguity, accuracy, completeness, and redundancy tests that are conducted during rule authoring in the repository stage. The effects of this step is to better insure that the interoperability is working (prior to deployment) and learning if the selected environment solution is meeting the organization's business needs.

## 4.7. Apply

This is the step of making the <sup>fi</sup>nal tested BRs fully operational and formally implemented and placed into active operations (e.g. “go live”). The inputs in this step include results and feedback from testing and the outputs include the fully applied BRs. The actors include the IT staff, business staff, and management. Traditional options for deploying new systems are useful here including a direct conversion, parallel start-up, phased roll-out or conducting pilots. When possible, the phased-in approach that spreads the deployment over a logical time sequence, or across segments of the population, or segments of the business offers advantages. Respondents emphasized the importance of preparing short-term fallback policies in case of problems or logical errors. The effects of this step provides a well managed and predictable deployment plan for new BRs, as well as improving the ability of business staff to more swiftly respond and implement BR updates; thus improving the <sup>fi</sup>rm's <sup>fl</sup>exibility and ability to rapidly react to changes in competition, legislation and other industry dynamics.

## 4.8. Maintain

Maintaining the alignment environment includes routinely evaluating, realigning, reprioritizing and selecting business domains of where the next BR automation needs to occur, in consideration of larger contextual in<sup>fl</sup>uences (changing business drivers, new markets, new geographies, ensuing legislative changes, and emerging competitive dynamics). Maintaining the rule management environment will focus on tactical issues including systematically capturing new or changes in rules, reexamining the organization and patterns to which business units, systems, and processes need rule access and how the access will be established. Rule repository owners should concentrate on effective rule authorship (maximizing rule reuse and accuracy), rule management (balancing rule volatility and churn workloads) and the integrity of the central rule repository (minimizing rule con<sup>fl</sup>icts and concurrency issues). Maintaining the implementation environment(s) focuses on insuring consistency with the organization's IT direction, awareness of new interoperability solutions between the repository and distribution sites, enabling rapid deployments, and managing system performance while enabling business users to be rightful owners of BR updates.

## 5. Discussion

Our discussion will brie<sup>fl</sup>y compare the BRMLC with the Knowledge Management Lifecycle Model (KMLC) literature and highlight key distinctions between the two. We also revisit the three BR project failures identi<sup>fi</sup>ed in the paper's introduction and illustrate how the BRMLC based can be applied.

The BRMLC can be compared to Nissen, Kamel and Sengupta's [40] Knowledge Management Lifecycle Model (KMLC) which includes the following six phases (create, organize, formalize, distribute, apply, and evolve). The authors' refer to this model as an amalgamated model, since it is synthesized from four prior knowledge management lifecycle studies. Whereas the knowledge management model begins with create, which the authors' de<sup>fi</sup>ne to include functions of discovery and development of new knowledge [39, page 255], the <sup>fi</sup>rst two BRMLC phases include plan and capture. A plan phase is included due to the importance of enterprise-wide planning for BR management initiatives and aligning these deployments with related contextual initiates. The BRMLC capture phase is narrower in scope than create, with the BRMLC's emphasis towards rule discovery. The KMLC's phases of organize (the data that has been captured), distribute (the explicit knowledge to stakeholders), and apply (‘go live’ with the knowledge) are similar in nature and intent with those in the BRMLC. The KMLC's formalize phase is similar to BRMLC's authoring stage, in that they both involve the conversion of existing knowledge from tacit to explicit form. The authoring stage is broader in scope, however, by going beyond an initial conversion to an ongoing management of this conversion on a regular and timely basis. Similarly, BRMLC's maintain phase is broader in scope than evolve, with emphasis towards maintaining and re-aligning the three larger environments of align, rule management and implementation.

If we revisit the three BR project failures noted in the paper's introduction, we can further illustrate how a higher contextual level BRMLC perspective can be of bene<sup>fi</sup>t. The IRS case, for example, represents a common misconception in BR automation projects that a business rules engine is required in all BR automation deployments. Although BRE vendors would likely prefer this ‘tunnel vision’ myth to continue, as noted in the BRMLC there are several alternative implementation solutions to choose from (SOA, business rules engine, going direct, and others) with advantages and disadvantages for each.

The type of failure in the Canadian project is also common in BR implementations. As emphasized by respondents, early phases in the BRMLC expose related but out-of-scope opportunities, such as cost reductions with business process reengineering and program ef<sup>fi</sup>ciencies in legacy code. The temptation is so appealing, that businesses will often postpone the BR implementation to capture the short-term gains. As the delays continue, the BR development ultimately becomes derailed.

In the Australian case, project leaders from the vendor and the government clearly lacked a shared understanding regarding the project's scope and in what direction the BR implementation should be guided. It is precisely in these types of situations that an understand ing of the BRMLC at the project's outset and during initial project planning and contractual negotiations would add value.

Indeed, all three illustrations highlight the managerial contributions that studies such as this can deliver and that MIS academic researchers are uniquely positioned to provide through presenting a balanced, unbiased perspective grounded in appropriate research methods and transcends speci<sup>fi</sup>c industries and domains. Collectively, we can begin viewing business rules management from a service science perspective, where service systems are de<sup>fi</sup>ned as “value-creation networks composed of people, technology and organizations. Interventions taken to transform state and coproduce value constitute services” [63]. By viewing business rules management in this broader service system context, we can identify key actors (service providers and service clients) that transcend traditional organizational boundaries, their forms of responsibility and ownership on the service targets (codi<sup>fi</sup>ed business rules and BR technology) and their forms of value coproduction.

## 6. Conclusion

The challenges confronting healthcare organizations with managing BRs are growing in complexity as the need for real-time, distributed and consistent decision making across systems, organizations, and channels rise. The pipeline of recently passed and emerging healthcare legislation at the federal and state levels, especially those pertaining to data collection and standards, only add to this level of need and complexity [13,17,25]. One study found that 70% of Health Care CIO's reported that new Federal health care mandates necessitated an acceleration of planned IT investments, with 62% of those investments occurring in 2011 and 2012 alone. Since the most significant of these federal legislative mandates become law in 2014, it's important for managers to be prepared.

This study is intended to assist managers with an important (and often overlooked) component of their IT architecture regarding business rules technologies. Organizations that embraced a longer-term, structured view of business rules management were found to have experienced signi<sup>fi</sup>cant bene<sup>fi</sup>ts such as improved interoperability, reduced costs, and greater control over managing BRs across systems and channels.

With the use of structuration research methods, the study collected data and conducted interviews with leading end-users, developers, researchers and thought leaders from the BR industry. The <sup>fi</sup>ndings suggest that a lifecycle has indeed emerged in business rules management and it is one that is distinct from the traditional knowledge management lifecycles. Based on synthesizing results from the study, the BRMLC was found to include three high level environments (align, rule management and implementation), that are decomposed into eight steps (plan, capture, organize, author, distribute, test, apply, and maintain). The primary effects of embracing a BRMLC approach provide essential managerial insights such as separating the rule management from the implementation environment, the use of an independent rules repository, shifting control of rule authoring and updates from IT to business staff, and alignment of BR deployments with similar enterprise-wide initiatives.

There are limitations in the study that should be highlighted. First, we examined business rules management with greater breadth, than depth. Thus, each step identi<sup>fi</sup>es the actors, artifacts, procedures and effects, which should be examined in greater detail. Second, the literature search concentrated in MIS related journals and, to a lesser extent, the business press. Although this approach is consistent with the study's intent, future efforts should consider comparing and supplementing the results to research similar streams from computer science and engineering related outlets. Finally, greater longitudinal analysis has traditionally been recommended in applying structuration research methods [44]. The authors did seek to make use of longitudinal considerations by separating the two rounds of interviews by one year.

Despite these limitations, we found that signi<sup>fi</sup>cant bene<sup>fi</sup>ts are enabled through effective BR management, including greater <sup>fl</sup>exibility, improved control, higher quality and speed of deploying and managing BRs. Other BRMLC bene<sup>fi</sup>ts include exposing buried BRs, preventing BRs from “walking out the door”, as well as formally documenting, maintaining and systematically evaluating where rules need to be deployed [2].

Recommendations for future research include BRMS technology diffusion, as managers continue to push automated BR management across their organizations. Also, the dynamics that occur between IT and the business staff during BR deployments should be more closely examined and has much to offer to the IT–business alignment literature. Furthermore, the literature search results revealed that certain areas of the BRMLC (such as the rule repository and authoring) have very few studies, if any, in MIS literature despite their growing importance and in<sup>fl</sup>uences. Finally, additional BR research in a broader context from a service science perspective (possibly as “value-creation networks”) will be increasingly important in business rules management in health care. As referenced in the paper, there's little doubt of the health care industry's emerging pressures from legislative and expense structure standpoints. As the need for increased transparency and seamless interoperability between systems and organizations along the health care value chain grows, so will the number of external actors and the industry's reliance on information technology to enable ef<sup>fi</sup>ciencies and cost reductions. It is anticipated that additional studies that examine BR management in a service science perspective, that transcend organizational boundaries and examine information systems and data sharing in an inter-organizational perspective will be essential to the industry in the long term.

## Acknowledgments

The authors gratefully acknowledge The Office of Extended University at Illinois State University for the funding of this study.

## References

[1] R. Agarwal, M. Tanniru, A structured methodology for developing production systems, Decision Support Systems 8 (6) (November 1992) 483–499.

[2] M. Alavi, Y. Yoo, D. Vogel, Using information technology to add value to management education, Academy of Management Journal 40 (6) (1997) 1310–1333.

[3] A. Ardalan, Analysis of local decision rules in a Dual-Kanban <sup>fl</sup>ow shop, Decision Sciences 28 (1) (1997) 195–211 (Winter)

[4] R. Ash, D.E. Smith-Daniels, The effects of learning, forgetting, and relearning on decision rule performance in multiproject scheduling, Decision Sciences 30 (1) (1999) 47–82 (Winter).

[5] A. Basu, A. Kumar, Research commentary: work<sup>fl</sup>ow management issues in e-Business, Information Systems Research 13 (1) (March 2002) 1–14.

[6] P.P. Belobaba, L.R. Weatherford, Comparing decision rules that incorporate customer diversion in perishable asset revenue management situations, Decision Sciences 27 (2) (1996) 343–363 (Spring).

[7] Blaze Adisor™ information was obtained from this website, http://www.fairisaac. com(and was last accessed on April 15th, 2011).

[8] J.D. Blocher, D. Chhajed, M. Leung, Customer order scheduling in a general job shop environment, Decision Sciences 29 (4) (1998) 951–981 (Fall).

[9] Business Rules Forum, www.businessrulesforum.com2000(and accessed June 10, 2007).

[10] P.G. Chander, R. Shinghal, T. Radhakrishnan, Using goals to design and verify rule bases, Decision Support Systems 21 (4) (December 1997) 281–305.

[11] M. Chen, A model-driven approach to accessing managerial information: the development of a repository-based executive information system, Journal of Management Information Systems 11 (4) (1995) 33–64 (Spring).

[12] CIO, The information was taken from a survey of 500 CIOs since 2002. posted on http://www.cio.com(and accessed Jun 1 2006).

[13] Coalition for Community Pharmacy Action (CCPA) website, last accessed on October 9, 2011.

[14] D. Dubois, J. Koning, A decision engine based on rational aggregation of heuristic knowledge, Decision Support Systems 11 (4) (May 1994) 337–361.

[15] N.B. Duncan, Capturing <sup>fl</sup>exibility of information technology infrastructure: a study of resource characteristics and their measures, Journal of Management Information Systems 12 (2) (1995) 37–58 (Fall).

[16] W. Elmaghraby, P. Keskinocak, Dynamic pricing in the presence of inventory considerations: research overview, current practices, and future directions, Management Science 49 (10) (October 2003) 1287–1309.

[17] M. Freudenheim, Health Law in a Swirl of Forecasts, New York Times, June 20, 2011.

[18] Gensym, Inc. information was obtained at this website, http://www.gensym.com/ (and was last accessed on June 10, 2007).

[19] H.W. Gottinger, P. Weimann, Intelligent decision support systems, Decision Support Systems 8 (4) (August 1992) 317–332.

[20] I. Graham, Business Rules Management and Services Orientated Architectures, John Wiley & Sons, West Sussex, England, 2006.

[21] D. Gulati, M.R. Tanniru, A model-based approach to investigate performance improvements in rule-based expert systems, Decision Sciences 24 (1) (Jan/Feb 1993) 42–59.

[22] Haley, Inc information was obtained at this website, http://www.haley.com/(and was last accessed on June 10, 2007)

[23] Barbara V. Halle, Business Rules Applied: Building Better Systems Using the Business Rules Approach John Wiley & Sons Inc, New York New York 2002.

[24] W. Hasselbring, Information System Integration, Communications of the ACM 43 (6) (June 2000) 32–38.

[25] Health Care Affordability Act. last accessed October 9, 2011, http://www healthcare.gov.

[26] R.C. Hicks, The no inference engine theory — Performing con<sup>fl</sup>ict resolution during development, Decision Support Systems 43 (2) (March 2007) 435–444.

[27] ILOG, SA information was obtained from this website http://www.ilog.com/(and was last accessed on June 10, 2007).

[28] M. Johnson, G. Scudder, Supporting quick response through scheduling of make-to-stock production/inventory systems, Decision Sciences 30 (2) (1999) 441–467 (Spring).

[29] A. Kambil, J.E. Short, Electronic integration and business network redesign: a roles-linkage perspective, Journal of Management Information Systems 10 (4) (1994) 59–84 (Spring).

[30] H.K. Klein, M.D. Myers, A set of principles for conducting and evaluating interpretive <sup>fi</sup>eld studies in information systems, MIS Quarterly 23 (1) (1999) 67–93 (Special Issue on Intensive Research).

[31] N. Kumar, A. Gangopadhyay, G. Karabatis, Supporting mobile decision making with association rules and multi-layered caching, Decision Support Systems 43 (1) (February 2007) 16–30.

[32] A. Lazarov, P. Shoval, A rule-based system for automatic assignment of technicians to service faults, Decision Support Systems 32 (4) (March 2002) 343–360.

[33] D. Leidner, S. Jarvenpaa, The information age confronts education: Case Studies on Electronic Classrooms, Information Systems Research 4 (1) (March 1993) 24–54.

[34] Lin Lin Jen-Hwa, Hu Paul, Sheng Olivia R. Liu, A decision support system for lower back pain diagnosis: uncertainty management and clinical evaluations, Decision Support Systems 42 (2) (November 2006) 1152–1169.

[35] T. Morgan, Business Rules and Information Systems: Aligning IT with Business Goals, Addison-Wesley, Boston MA, 2002.

[36] M. Mosquera, IRS Tightens Business Rules Management, Government Computer News (GCN), http://gcn.com/articles/2006/01/20/irs-tightens-business-rules-management. aspx?sc\_lang=en (January 20, 2006).

[37] R. Mukherjee, R.F. Gamble, J.A. Parkinson, Classifying and detecting anomalies in hybrid knowledge-based systems, Decision Support Systems 21 (4) (December 1997) 231–251.

[38] M.D. Myers, Investigating information systems with ethnographic research, Communication of the AIS 2 (23) (1999) 1–20.

[39] M.E. Nissen, An extended model of knowledge-<sup>fl</sup>ow dynamics, Communication of the AIS 8 (2002) 251–266.

[40] M.E. Nissen, M. Kamel, K. Sengupta, Integrated analysis and design of knowledge systems and processes, Information Resources Management Journal (Jan–Mar 2000) 24–43.

[41] R. O'Neill, Verdict on a \$64m Project Failure, The Sydney Morning Herald, http:// www.smh.com.au/news/Breaking/Verdict-on-a-64m-project-failure/2005/04/ 15/1113509904098.html (April 15, 2005).

[42] W. Orlikowski, J. Baroudi, Studying Information Technology in organizations: research approaches and assumptions, Information Systems Research 2 (1) (March 1991) 1–28.

[43] D. Paulson, Y. Wand, An Automated Approach to Information Systems Decomposition, JEEETransactions Software Engineering 18 (3) (March 1992) 174–189.

[44] M.S. Poole, G. DeSanctis, Structuration theory in information systems research: methods and controversies, in: M.E. Whitman, A.B. Woszczynski (Eds.), The Handbook for Information Systems Research, The Idea Group, Hershey, PA, 2004, pp. 206–249.

[45] M. Pozzebon, A. Pinsonneault, Structuration theory in the IS <sup>fi</sup>eld: an assessment of research strategies, in: The 9th European Conference on Information Systems (ECIS), Bled Slovenia, June 27–29, 2001, pp. 205–217.

[46] C.K. Prahalad, M.S. Krishnan, The dynamic synchronization of strategy and Information Technology, MIT Sloan Management Review 43 (4) (2002) 24–33.

[47] T.S. Raghu, B. Jayaraman, H.R. Rao, Toward an integration of agent-and activity-centric approaches in organizational process modeling: incorporating incentive mechanisms, Information Systems Research 15 (4) (December 2004) 316–335.

[48] F. Rohde, Little decisions add up, Harvard Business Review 83 (6) (June 2005) 24–26.

[49] R.G. Ross, Principles of the Business Rule Approach, Addison-Wesley, Boston, MA, 2003.

[50] R. Sabherwal, I. Becerra-Fernandez, An empirical study of the effect of knowledge management processes at individual, group, and organizational levels, Decision Sciences 34 (2) (2003) 225 (Spring 36p.).

[51] Semantics of Business Vocabulary and Business Rules (SBVR), Object Management Group. The document is available at this website http://www.omg.org/ (and accessed on June 12, 2007).

[52] G. Shankaranarayanan, and A. Even, Managing Metadata in Data Warehouses: Pitfalls and Possibilities, Communications of AIS 14(13) 247–274.

[53] B. Sheil, Thinking about Arti<sup>fi</sup>cial Intelligence, Harvard Business Review (July– August 1987) 91–97.

[54] J. Sinur, Magic Quadrant for Business Rule Engines, Gartner Research Note #G00125811, Note: Initial data taken from this study were updated based on actual sales data results from vendors for 2005 and 2006, February 2005.

[55] J. Sinur, J.B. Hill, Magic quadrant for business process management suites, Gartner Research (18 October 2010) (ID:G00205212).

[56] J.M. Swaminathan, S.R Tayur, Models for supply chains in E-Business, Management Science 49 (10) (October 2003) 1387–1406.

[57] The New York Times, Health Insurance and Managed Care, A collection of articles about health insurance and managed care published in The New York Times, http://topics. nytimes.com/top/news/health/diseasesconditionsandhealthtopics/health\_insurance\_ and\_managed\_care/health\_care\_reform/index.html, September 28, 2011(Last accessed October 8, 2011).

[58] P. Torino, C.P. Politecnico, Modularization techniques for active rules design, ACM Transactions on Database Systems (March 1996) 1–29 (TODS) archive (21/1).

[59] Tsaih Ray, Hsu Yenshan, C. Lai Charles, Forecasting S&P 500 stock index futures with a hybrid AI system, Decision Support Systems 23 (2) (June 1998) 161–174.

[60] W.M.P. Van der Aalst, A. Kumar, XML-based schema de<sup>fi</sup>nition for support of interorganizational work<sup>fl</sup>ow, Information Systems Research 14 (1) (March 2003) 23–46.

[61] R.C. Waters, E.J. Chikofsky, Reverse Engineering: progress along many dimensions, Communications of the ACM 37 (5) (May 1994) 22–24.

[62] K.K. Yang, Effects of erroneous estimation of activity durations on scheduling and dispatching a single project, Decision Sciences 27 (2) (1996) 255–290 (Spring).

[63] P. Maglio, S. Srinivasan, J.T. Kreulen, J. Spohrer, Service systems, service scientists, SSME and innovation, Communications of the ACM 49 (7) (July 2006) 81–85

Matthew L. Nelson, CPA, Ph.D BIO. Dr. Matthew Nelson is an Associate Professor in the Accounting & Business Information Systems Department. Nelson's courses include Information Systems in Organizations, e-Business, and IT Auditing. Nelson's research interests include business rules technology, open source software, business intelligence, vertical standards development consortia and the value of IT. Nelson has publications in the Journal of Management Information Systems, Decision Support Systems, Information and Management, International Journal of Electronic Commerce, Mathematical and Computer Modeling, Electronic Markets, Journal of Information Systems Education and others. Nelson earned a Bachelor's Degree in Accounting, Masters Degree in Management Information Systems and a Ph.D. in Management Information Systems from the University of Illinois.

Ravi Sen, PhD, BIO. Dr. Ravi Sen is an Associate Professor in the Department of Information and Operations Management at the Mays Business School, Texas A&M University. He received his Ph.D. in Business Administration from the University of Illinois at Urbana—Champaign in 2003, His research interests include economics of electronic commerce, open source software, and software security, He has published in the Journal of Management Information Systems, Decision Support Systems, International Journal of Electronic Commerce, Communications of the AIS, Electronic Markets, Journal of Electronic Commerce Research, and others.
