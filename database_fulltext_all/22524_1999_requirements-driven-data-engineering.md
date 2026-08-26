---
otero_id: 22524
otero_key: "66Y6E6HU"
title: "Requirements-driven data engineering"
authors: "Peter Aiken; Youngohc Yoon; Belkis Leong-Hong"
year: "1999"
journal: "Information & Management"
doi: "10.1016/s0378-7206(98)00082-2"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
Case study

# Requirements-driven data engineering

Peter Aiken $^{1,a,b,*}$ , Youngohc Yoon $^{a}$ , Belkis Leong-Hong $^{c}$

$^{a}$ Information Systems Research Institute, Virginia Commonwealth University, 1015 Floyd Avenue, Richmond, VA 23221-3931, USA $^{b}$ Office of the Chief Information Officer, Defense Information Systems Agency, 701 South Courthouse Road, Arlington, VA 22204-2199, USA $^{c}$ Principal Deputy Director and Chief Information Officer, Defense Security Service, 1340 Braddock Place, Alexandria, VA 22314, USA

Received 7 November 1997; revised 10 December 1997; accepted 23 July 1998

## Abstract

In the early 1990s, the effectiveness and efficiency of the information systems (IS) supporting the US Department of Defense's non-combat operations was questioned. As had many organizations, the support had evolved into multiple, redundant, unintegrated, undocumented, stove-piped IS. These systems require unnecessarily large non-combat IS expenses, supporting war fighting efforts. Lack of integration hindered the Department from effectively providing mission support information. DOD's efforts to re-engineer the non-combat IS is one of the first attempts to apply requirements-driven data engineering to a large systems environment. Its application to DOD's non-combat IS data environment has provided tangible results: (1) from the top down, an enterprise model (EM) now specifies Department-wide requirements capable of guiding future integration and development efforts; (2) from the bottom up, non-combat IS are being significantly reduced, simplifying the overall problem; and (3) data quality engineering methods, guided by the EM, are being developed and applied to the remaining IS. This success has achieved a prerequisite necessary to increase the effectiveness and efficiency of the systems. © 1999 Elsevier Science B.V. All rights reserved

Keywords: Data engineering; Data architecture; Enterprise integration; Reverse engineering; Department of Defense (DOD); Legacy systems re-engineering; Case study

## 1. Introduction

At the start of the 1990s, the US Department of Defense (DOD) faced challenges in effective maintenance of its large information system (IS) environment. DOD's non-combat support (i.e. personnel, payroll, transportation, logistics, etc.) had evolved into redundant, un-integrated, undocumented IS. Perhaps more importantly, these systems were ‘stove-piped’ – each developed as if it existed in a vacuum with no requirements to exchange information with any other systems. In order to support war-fighting efforts these systems required unnecessarily large, non-combat-related expenses. Lack of integration hindered the Department’s ability to provide mission-supporting information effectively. ‘Desert Storm’ experience highlighted specifics that could not be ignored by DOD management. In part as a response to this, improving the efficiencies and effectiveness of non-combat IS became a key focus of the Corporate Information Management (CIM) initiative implemented in 1989.

While the specific competitive advantage and the strategic goals sought may be different, DOD's needs to leverage its data resources strategically, namely allow them to be shared with other organizations [1]. To those facing similar challenges, a key research question continues to be: How can one implement data engineering in an operational environment while continuing to provide required day-to-day support? By adopting a requirements-driven data engineering approach, DOD effectively responded to such challenges.

## 2. DOD's data engineering challenge

In the history of US defense operations, the Department of Defense is a relative newcomer. For two centuries prior to World War II, defense forces had existed as separate, unintegrated organizations. Each developed complex, fail-safe procedures ensuring mission completion. After this consolidation, progress toward integrating these operations was restricted to ‘live’ condition requirements. Over time, manual procedures were automated as IS, implementing ‘service-specific’ variations in a bottom-up fashion, each supporting localized procedures. Consequently, DOD wound up with multiple systems supporting numerous basic process variations.

DOD's 1990 IT environment included [2, 3, 4]:

1. approximately seventeen hundred largely unintegrated and often duplicative IS, as well as many ‘unofficial’ IS;

2. approximately one point four billion lines of associated code; and

3. thousands of data centers running these IS.

DOD has attempted to keep its ‘overhead’ low to ensure that it has sufficient resources to carry out its primary mission: ‘providing for the common defense’ [5]. However, according to the Defense Science Board August 1996 Task Force on Outsourcing and Privatization, DOD’s support functions had consumed between US \$120 and \$160 billion annually. This indicates that 70 percent of the total defense dollars are consumed by non-combat operations. Maintaining functionally duplicative systems has, therefore, caused DOD IT spending to be unnecessarily high: this is estimated as ca. \$9 billion annually in 1990 [6]; for instance, 37 functionally duplicative pay systems and support personnel were then being used to pay DOD civilian employees. Lack of standardized data and data structures across systems hindered DOD's ability to extract information from its IS. Moreover, submitting the same query to several different systems resulted in multiple conflicting responses; these were often impossible to consolidate.

In 1991, the Iraqi invasion of Kuwait led to the US forces operating in ‘Desert Storm’. It highlighted several IT problems, including:

\- The Military Airlift Command (MAC) and the Tactical Air Command (TAC) recognized that their two command and control systems had to exchange data directly. The MAC theater airlift management system and the TAC computer-assisted force management system command post operators required 12 h to integrate data manually when developing Air Tasking Orders. This provided insufficient turnaround time to implement President Bush's desire for a more intensive air campaign. Developing a solution to this problem took days and served as a trigger for management action because combat operations were delayed due to this data integration problem [7].

\- Logistics systems had been built to track supplies to fixed supply points. When some of them were relocated, the associated supplies were ‘lost’ by the systems. This resulted in thousands of misallocated containers, hurting war-fighting efforts due to lack of delivery of essential supplies.

\- Some DOD manpower tracking systems lost data when reserves were mobilized for duty overseas. The systems listed the reservists as absent without leave (AWOL). Incorrect year end personnel statements were also received at the holiday season, arriving about the same time as some US congressional delegations who were visiting combatants from their districts to find out how they were and their attitudes.

Although these examples are not typical of all operations, they did indicate specific problems. These and others were intensified as DOD's budget began shrinking. The fiscal year (FY) 1995 budget of \$252.2 billion was down one-third from what it was five years previously, providing an additional incentive to attempt to find savings.

## 3. The CIM initiative: a data engineering response

In response to problems and budget reductions, former Deputy Defense Secretary Atwood started the CIM initiative. His written motivation stated:

“until now the Department has had to plan improvements on a function-by-function basis, with only limited ability to achieve cross-functional integration and top-down strategic planning. This has led to ‘stove-pipe’ functions and systems that are:

\- Lacking in interoperability – cannot exchange command and control information, or effectively link the battlefield to its support base

\- Slow and inflexible – cannot be re-configured rapidly to meet new situations. The inventory of existing assets and capabilities cannot be re-used to capitalize on DOD's existing investment in people and materiel.

\- Wasteful and costly – do not share common elements, but duplicate them” [8].

As shown in Fig. 1, CIM was initiated as an attempt to develop a seamless, global, secure, end-to-end data architecture of interoperable/integrated systems, that shares standard data and provides flexible and affordable information services to support common defense needs. CIM activities were thus intended to develop integrated process and data models making up an enterprise model (EM). These models would be developed in conjunction with business re-engineering. A primary output was to be the development of standard data, made available to other DOD development activities using a DOD Data Repository. Data standards were to be used to develop interoperable systems. Standardized data across systems was found to be essential to make integration possible with other enterprise-integration activities, as well as directly impacting DOD's war fighting efforts [9].

DOD established Data Administration (CIM/DA) as an integral CIM function. Fig. 2 gives its mission, and guiding principles were drawn from, and are typical of those being implemented industry-wide. The CIM/DA mission was to develop data standards, an organizational repository, and, to the extent possible, single-point of entry data. Its program areas included data program management, enterprise data engineering, and business functional data engineering. CIM/DA's role was to:

![](/api/attachments/66Y6E6HU/fulltext/images/8c2bf860a349437e711baed1daa2be3cc7c863c2f4008cfcdb71572ec08b9923.jpg)  
Fig. 1. A DOD chart used to present CIM concepts to both, top management and DOD personnel/contractors charged with implementing CIM.

![](/api/attachments/66Y6E6HU/fulltext/images/3cdb9766d419db1dffc4e86b51afcca3fa1d992e6bb1512fa5e285b13f3131a8.jpg)  
Fig. 2. CIM/DA mission and guiding principles.

1. specify achievable organizational information requirements-supporting Departmental missions;

2. manage Departmental data assets required to deliver the required organizational information requirements strategically; and

3. maintain integration with other strategic level DOD frameworks, such as those organizing the DOD process, its communication network, and staffing model architectures.

## 4. The requirements-driven solution

The data engineering solution required: understanding; modeling; analyzing; maintaining; and evolving requirements to support the mission. Since future requirements were expected to change dramatically but were unknown, the prudent course for data administration was to organize and maintain data resources in their most flexible and adaptable state, based on the past and current departmental information requirements. Requirements specification and integration was accomplished by maintaining them as integrated process and data models. Once the requirements were understood, they were organized into an architecture. The process involved deriving the current data requirements and architecture from existing systems, formalizing them into a validated model for analysis, and using them strategically. Sometimes the most effective way to obtain specific requirements was by reverse engineering legacy systems (see, e.g. Ref.. [10] or [11])

for details). The general approach to requirements-driven data engineering addressed the situation using three simultaneous strategies:

\- Top down: Specifying a DOD EM. Because the magnitude of the challenge involved assessing thousands of legacy systems, it became clear that an architecture-based approach was needed in developing and implementing strategic level data resource management. The Department recognized the need for strategic level data planning and coordination and followed current practice in developing a strategic level enterprise model (EM) [12, 13].

\- Bottom up: Reducing the number of non-combat IS. The bottom up strategies involved examining the systems required to provide mission support. By removing redundancies, three goals could be accomplished: (1) there were less data attributes and entities to be understood and maintained; (2) the integration requirements were simplified; and (3) the effort required to maintain the organizational data resources was reduced.

\- Data quality engineering methods application. The third part involved developing and applying data quality methods to the remaining IS. It was easier to develop suitable architecturally based data quality engineering methods with fewer systems.

Implementing these strategies involved the six coordinated activities shown in Fig. 3.

## 4.1. Functional area requirements specification

DOD functional areas were charged with specifying their specific requirements by defining data needs and performing an analysis of the IS inventory. The requirements were specified using facilitated joint application development session-like model refinement and validation sessions. Use of common data and process modeling methods facilitated subsequent integration. The result is a preliminary functional area data model (FADM).

## 4.2. Functional data/system analysis, designation of migration systems

It was next necessary to understand the true dimensions of the IS inventory of each functional area by analyzing existing systems and data assets. The systems were evaluated for potential data architecture contribution and their ability to satisfy the functional data requirements. Another analysis goal was to determine stewards for systems/data and the contribution of individual data assets toward overall DOD requirements. The prevailing mind-set was that data ‘belonged’ to each functional area. However, the realities of data-sharing promoted responsibility for the protection, quality control, and controlled distribution of functional area data.

![](/api/attachments/66Y6E6HU/fulltext/images/926360926b72e705c55241dfadb4c5b4274ff25e37ad625f228adc4a149aa89f.jpg)  
Fig. 3. DOD approach to requirements-driven data engineering.

The analysis also identified candidate systems for data reverse engineering (DRE) analysis to identify specific requirements satisfied by the ‘best-of-breed’ systems in the functional area. The reduction process involved designating these as migration systems supporting the evolving functional area: user; infrastructure; standardization; and other requirements. Migration systems were used to consolidate needed data and functionality from multiple systems into a single system capable of serving the area. For example, once selected, the pay area migration system was enhanced to satisfy the requirements for the entire pay function, and plans were made to consolidate all other pay data into this system. DOD was determined to identify a relatively short list of migration systems that it would continue to support while terminating redundant systems.

## 4.3. Data architecture engineering

The purpose of data architecture engineering was to develop a data architecture guiding DOD IS development and enhancement. The EM was developed to serve as strategic level guidance. The EM is

“a critical element in the overall CIM initiative. It is the principle mechanism for senior leadership to understand their missions and functions, plan and direct improvements from a DOD-wide perspective, and measure overall progress toward established goals” [14].

It is composed of the Defense data architecture (DDA) and the activity model (AM). The DDA, in turn, is composed of the strategic Defense data model (DDM), a set of FADM, and standard data elements. When integrated with other DOD architectures, the DDA specifies Departmental data requirements for data evolution and system development activities. Once the DDM was established, it was integrated with the AM, producing a major architecture development phase. Fig. 4 shows how DDA refinement occurred on three tiers: the DDM, FADMs, and operational level models of each system developed by DRE analysis, etc. The DDA was developed by combining the DDM, FADM, and DRE analysis outputs, with additional reference materials. Strategic-level entity definitions were too abstract to provide specific guidance to developers. Therefore, FADM were developed to provide linkage to strategic DDM guidance for implementers, thereby ensuring DOD-wide coordination. Each FADM, integrated into the DDA, linked strategic and functional requirements and extended the DDA while making it more useful simplifying data engineering.

![](/api/attachments/66Y6E6HU/fulltext/images/1640c6ffeddc8f403e541a74a106e155e57c403e28600bd9f60ff727a4059176.jpg)  
Fig. 4. Defense data architecture (DDA) development and refinement.

## 4.4. Data reverse engineering

DRE is an analysis method that produces the data requirements specifications for an existing IS. Analysis of the IS identifies candidates for DRE. The goal of the analyses is to produce validated data assets (i.e. what data supports what processes, used by what users, at what locations, by what systems). Once developed, these data assets contain precise information, unavailable before the analysis, about the target system. Key to successful DRE is identifying required data assets in light of analysis objectives $[15]$ .

As architecture development progressed, certain EM components were developed ahead of others. Data models and other domain-specific knowledge obtained by DRE were used to develop/refine data architecture components. DRE outputs, shown in Fig. 4, influenced the data architecture by validating and refining architectural components. Many of the designated migration systems were reverse engineered to obtain a knowledge base for replacement systems.

## 4.5. Data evolution

Other systems were reverse engineered to obtain metadata required to develop a plan for changing the association of data from the target system to the migration system. This often involved transforming data, as it had to be integrated into some migration systems. Aspects of data evolution are popularly described as:

\- Data migration – the process of changing the location of the data from one system to another.

\- Data conversion – the process of changing data into another form, state, or product.

\- Data quality engineering (or sometimes data scrubbing) – the process of comprehensively inspecting, verifying, and manipulating, manually re-coding, re-keying, or other preparation of data for subsequent use.

It is during data evolution, that data quality methods must be developed and applied as data is prepared for its new use(s). To help developers understand the evolution of data standards, DA defined three data categories to communicate strategic aspects of data quality to developers. Data associated with legacy systems was ‘Category 3’, migration systems data was labeled ‘Category 2’, and when it was approved as a data standard, it became ‘Category 1’. The data evolved from Category 3 to Category 1 through data architecture development, DRE, and data quality engineering activities. The volume of data was also reduced.

## 4.6. Data architecture-based systems development

Policy makers wanted IS development sponsors to demonstrate their architectural compatibility before approving funding. Developers were encouraged to adopt data engineering practices and use of Category 1 data to aid this process. A series of project funding checkpoints were developed to document architectural compatibility and use of standard data $[16]$ .

## 5. Initial results, critique, and redirection

CIM/DA achieved preliminary results and, as a result, received some re-direction. By mid-1993, CIM funding sponsored initiatives that produced results at all three architectural levels. At the enterprise level, CIM had established a Department Data Administration Council and other governance structures, developed a repository system, and facilitated data engineering efforts. At the functional level, CIM sponsored process and data modeling produced many of the DDA requirements. The FADM were developed and used to extend and validate the DDA. These efforts increased mid-level DOD management's awareness of their data requirements and the value of sharable data. Also, to facilitate operational-level participation, CIM/DA established a training program so that participants would know the necessary processes in which they were to participate and how to contribute to them. Hundreds of DOD personnel participated in process and data modeling classes. A number of migration systems were reverse engineered, producing data architecture components that were used to start, validate, and refine various FADMs. However, CIM/DA also suffered some constructive criticism, as mentioned in the following:

\- Specific technical expertise required to staff the projects was difficult to identify, locate, attract, and retain.

\- There were disagreements over modeling methodologies. The initial usefulness of some models was disappointing, perhaps due to use of limited-capacity modeling methods [17, 18]. Application of more modern methods (such as those suggested by [19] may prove useful here.

\- Creating the repositories using dated technology made them difficult to use.

\- There was little apparent progress at the operational level. Even with pressure from management to show quantifiable results, the repositories contained few standard data elements. Many personnel had been trained and were ready to begin modeling, but the required architectural guidance was incomplete.

In an effort to give strong visibility to and stimulate the program, the then Deputy Secretary of Defense Perry made his principal staff assistants responsible and accountable for completing data standardization within a three-year period $[20]$ . CIM/DA was specifically redirected to consolidate the repository system and speed up data standardization. The existing repository system was to be made more accessible to the user community via Internet technologies, migrating it to a common data management environment, and consolidating it into a single repository. Eliminating another barrier, CIM/DA subsequently developed a PC-based system that enabled users to access a historical repository extract using then popular 386-based Wintel platforms, further extending the accessibility of data architecture to data engineers.

CIM/DA also sped up the data element approval procedure. In a move similar to discarding the system of military specifications (milspecs), CIM/DA recognized a number of external as well as existing functional-based data quality efforts and standards. Instead of waiting for CIM/DA to populate functional views by extending the EM, functional areas could now leverage in-progress data standardization efforts by submitting them for approval as interim data standards (IDS). These were made available as interim functional guidance before being integrated with the DDA as guidance for other functional areas. They could then be used to guide existing functional area development efforts. The revised data element standardization process (Fig. 5) shortened the amount of time and work required to develop functional data standards. Adding interim data standards provided developers with functionally standardized data more rapidly but introduced multiple data standards for functional areas. This modification altered the focus of data architectural development efforts from top down to bottom up, resulting in a more difficult technical and functional integration problem. It involved integration of greater numbers of lower level components before the FADMs could be completed.

![](/api/attachments/66Y6E6HU/fulltext/images/6b500db745fe447e9ca110dcb22fa03aef058fa87900eb7da1093d32051bad60.jpg)  
Fig. 5. Revised CIM/DA data standardization procedure for transition legacy data to formal data standards (Note: new category designations).

## 6. Technical results

By May 1996, the CIM data engineering program had achieved tangible and intangible results. They included:

\- Increased CASE literacy levels and awareness of data engineering methods on the part of developers who were associated with CIM/DA projects, particularly where object, CASE, and DBMS technologies were successfully employed.

\- Model-based development had been institutionalized throughout DOD as CIM/DA project experiences have been assimilated. Model-based thinking now helps developers to consider departmental context and task foci.

\- A move toward more integrated systems development [21].

Tangible benefits include development of the DOD/EM, reduction in the number of non-combat IS, development of data standards, and the application of data quality standards.

![](/api/attachments/66Y6E6HU/fulltext/images/3b6182fdb970d437baf4b917f8c78c25bcc280c2ac3d07bbe78289b8962d7317.jpg)  
Fig. 6. Enterprise model: DDA component (shown unnormalized – all associations are many-to-many).

## 6.1. Enterprise model and strategic guidance

The EM was released, circulated for comment, refined, based on FADM integration and, subsequently, re-released as guidance. Fig. 6 shows that the EM consists of 13 principal data entities integrated with the four major processes (A1–A4) and 15 subprocess (A11–A44) shown in Fig. 7. In addition, governance structures were established to provide specific functional area guidance and coordination as needs arise to enhance and refine portions of the data architecture. CIM/DA now supports an accessible repository containing valuable user and data requirements for use by developers.

Fig. 7. Enterprise model: activity model component.

<table><tr><td></td><td>CONTROLS</td><td>Executive, Judicial &amp; Congressional Authorities</td><td>World situation</td><td>Federal regulations</td><td></td></tr><tr><td></td><td colspan="5">INPUTS</td></tr><tr><td></td><td colspan="5">Civian population</td></tr><tr><td></td><td colspan="5">Industrial resources</td></tr><tr><td></td><td colspan="5">Allied assets</td></tr><tr><td></td><td colspan="5">Threat forces</td></tr><tr><td></td><td colspan="5">Allied/Coalition forces</td></tr><tr><td></td><td colspan="5">International &amp; domestic community</td></tr><tr><td></td><td colspan="5">A0 PROVIDE FOR THE COMMON DEFENSE</td></tr><tr><td></td><td colspan="5"></td></tr><tr><td></td><td colspan="5"></td></tr><tr><td></td><td colspan="5"></td></tr><tr><td></td><td colspan="5"></td></tr><tr><td></td><td colspan="5"></td></tr><tr><td></td><td colspan="5"></td></tr><tr><td></td><td colspan="5"></td></tr><tr><td></td><td colspan="5"></td></tr><tr><td></td><td colspan="5"></td></tr><tr><td></td><td colspan="5"></td></tr><tr><td></td><td colspan="5"></td></tr><tr><td></td><td colspan="5"></td></tr><tr><td></td><td colspan="4"></td><td></td></tr></table>

![](/api/attachments/66Y6E6HU/fulltext/images/1cc9c264f044fce3daefe59d4c3d4412bd126228d9aac8e9a5394c766a8a8d86.jpg)  
Fig. 8. Non-combat IS reduction progress by functional area.

## 6.2. Reducing non-combat IS

DOD has taken steps to reduce the number of non-combat existing legacy IS from approximately 1700 to 174. (Legacy systems can be broadly defined as systems that have been more economical to continue to maintenance than to replace with another, possibly new, system – until now [22].) Migration plans to eliminate more than 900 IS were developed. Fig. 8 illustrates how requirements-driven data engineering has resulted in functional area migration systems and corresponding overall IS reduction.

## 6.3. Developing data standards

Perhaps most tangibly, by May 1996 data standardization efforts had produced almost 12000 data standards. Fig. 9 shows the categories 1–3 data entities, and Fig. 10 the categories 1–3 attributes. Thousands of approved organizational standard data items are currently available for use by development and maintenance activities throughout DOD. In addition, CIM/DA also began the development of a metric framework for assessing initial results. The framework consisted of an iterative cycle for estimating reverse engineering projects, learning from the experiences, and refining the estimating process (see [23] for details) (Fig. 11).

![](/api/attachments/66Y6E6HU/fulltext/images/9a2080ac14515eb50bfbba9978131ce78b1729bd33beb3e64a6334e916fd856d.jpg)  
Fig. 9. Repository entities classified by functional areas and data quality categories.

![](/api/attachments/66Y6E6HU/fulltext/images/8c607ffc63d71c02437ae449f799d89fac9bf84cfe619a6c566e5e3ec7a13bcb.jpg)  
Fig. 10. Repository attributes classified by functional area and data quality categories.

## 6.4. Application of data-quality standards

Once the functional requirements had been specified, it was possible to develop and apply data quality standards. Application of data quality methods was concentrated on the final 10% of the migration systems [24]. The organization-wide application of data engineering techniques such as data parameter checking [25], data integrity analysis [26], data quality engineering [27] simply could not be undertaken for

KEY Functional Area
DDP Director for Defense Procurement
DDR&E Director, Defense Research & Engineering
TFR Director, Test, Systems Engineering and Evaluation/Test Facilities and Resources
ES Deputy Under Secretary of Defense for Environmental Security
L Deputy Under Secretary of Defense for Logistics
EXTDODDA External Standards, Department of Defense, Data Administration
IG Inspector General, Department of Defense
USD(C) Under Secretary of Defense, Comptroller
USD(P&R) Under Secretary of Defense for Personnel & Readiness
USD(P) Under Secretary of Defense for Policy

Fig. 11. Abbreviations used in Figs. 9 and 10.

almost 1700 systems. Nor would it have been productive to do so, because these techniques fail to address the structural data-quality challenges posed by duplicative, stove-piped systems. Data engineering techniques are most effective when applied to Category 1 data: there coordinated application of DOD-wide structural data quality methods range from statistical sampling to data performance metric recording.

## 7. Conclusions

Application of requirements-driven data engineering to DOD systems has made significant contributions by reducing the resources necessary to maintain non-combat IS. The approach has the potential to reduce the number of DOD non-combat IS by an order of magnitude: from almost 1700 to 174. Several thousands of individual data elements have been integrated through shared Departmental data, data modeling, and common data architecture techniques making it possible to guide future systems development. This has also produced thousands of approved standard data items available in repository format for use by systems development and maintenance activities at data centers. The repository provides access to and management of more than 12 000, categories 1–3 DOD data standards. Developers now can access the repository information using Internet and workstation-based techniques to retrieve DOD-wide organizational data requirements, metadata and data quality standards. These accomplishments are allowing DOD to improve its IS effectiveness.

However, because of failure to meet the original timetable, these accomplishments have not drawn unconditional praise from management (see [28, 29] and the press – with one internal Pentagon assessment labeling “the entire CIM initiative... a failure” [30].

DOD's experiences and results are typical of organizational approaches to dealing with burdened IS environments. Results are obtainable but are constrained by technical integration requirements- and managerial considerations.

Data architects should incorporate political realities into their technical planning activities. In order to correct an imbalance between existing systems and operational needs and ensure high levels of quality in DOD data, the Department needs to adopt a long-term perspective to data engineering and not allow pressure for short-term results to undermine the value of the effort.

The ever-increasing importance of data within DOD was reinforced by a recent Joint Chiefs-of-Staff report detailing future war fighting capabilities, including electronic warfare and information warfare, which require effective IT implementation [31]. The CIM/DA initiative was the first step in enterprise engineering the entire DOD non-combat operations. In view of the increasingly critical role that IT plays in supporting war fighting activities, DOD's efforts must continue, regardless of the mixed reviews on the CIM initiative.

## Acknowledgements

This paper benefited enormously from critiques by several of our colleagues within the US Department of Defense, our colleague Sean O'Keefe – the VCU Data Administrator, and several anonymous reviewers. Literally hundreds of DOD employees and service members participated in the CIM initiative and related projects. In describing these results, we have attempted to detail a highly involved effort using just 5000 words. Our apologies to those whose story and participation have not been explicitly addressed and acknowledged.

## References

[1] B. Parker, L. Chambless, D. Smith, D. Satterthwaite, D. Duvall, Data Management Capability Maturity Model (March 1995) MITRE Document MP95W0000088, MITRE Software Engineering Center 7525 Colshire Drive, McLean, VA 22102.

[2] Moisey Lerner, Software maintenance crisis resolution, The New IEEE Standard Software Development 2(8), 1994, pp. 65–72.

[3] Chris Staiti, Paul Pinella, DOD's Strassmann: the politics of downsizing, Datamation 15, 1992, pp. 107–110.

[4] Status of the Department of Defense Corporate Information Management (CIM) Initiative, October 1992 – reprint ed.

[5] The DOD EM Volume 1, 11 January 1994, page 1 available from DOD Data Administration.

[6] Paul Taibl, Outsourcing and Privatization of Defense Infrastructure (Business Executives for National Security National Office, 1717 Pennsylvania Avenue, NW, Suite 350,

Washington, DC 20006-4603 http://www.bens.org/pubs/ou-trsce.html.

[7] B. Nguyen, A method for implementing data administration: a combat command model office of the Deputy Assistant Secretary of Defense (Civilian Personnel), May 1993.

[8] M. Smith, The DOD EM: a white paper project enterprise office of the Director of Defense Information, January 1994.

[9] E. Paige Jr., Six Emerging Trends in Information Management, Defense Issues 11 (16) (Address by Emmett Paige Jr., assistant secretary of defense for command, control, communications and intelligence, at the American Defense Preparedness Association's Information Management for the Warfighter Symposium, Vienna, Va., Feb. 29 1996).

[10] Kyong-Ho Kim, Young-Gul Kim, Process reverse engineering for BPR: a form-based approach, Information and Management 33(4) (1998) 187–194.

[11] P. Aiken, A. Muntz, R. Richards, DOD legacy systems: reverse engineering data requirements, Communications of the ACM 37(5), 1994, pp. 26–41.

[12] Warren Keuffel, Just doing it: Nike uses its Just Do It corporate message to create an effective software development process, Software Development 5(11), 1997, pp. 31–32.

[13] Shouhong Wang, Modeling information architecture for the organization, Information and Management 32(6) (1997) 303–317.

[14] M. Smith, The DOD EM: a white paper project enterprise, Office of the Director of Defense Information, January 1994.

[15] Peter Aiken, Data Reverse Engineering: Slaying the Legacy Dragon (New York: McGraw-Hill, 1996) ISBN 0-07-000748-9; Peter Aiken, Reverse engineering of data. IBM Systems Journal, 37(2) (1998) 246–269.

[16] Department of Defense INSTRUCTION NUMBER 8120.2 Automated Information System (AIS) Life-Cycle Management (LCM) Process, Review and Milestone Approval Procedures (available on the web at http://tecnet0.jcte.jcs.mil:9000/htdocs/teinfo/directives/soft/8120.2.html).

[17] R. Barrett, Is IDEF on the Wane? Enterprise Reengineering March 1996, p. 22.

[18] B. Gregory, M. Reingruber, IDEFinitely One for the Trash Heap, Enterprise Reengineering, June 1996, p. 25.

[19] Franco Giacomazzi, Carlo Panella, Barbara Pernici, Marco Sansoni, Information systems integration in mergers and acquisitions: A normative model, Information and Management 32(6) (1997) 289–297.

[20] William J. Perry, Accelerated Implementation of Migration Systems, Data Standards, and Process Improvement Memorandum for Secretaries of the Military Departments, Chairman of the Joint Chiefs Of Staff, Under Secretaries of Defense, Assistant Secretaries of Defense, Comptroller, General Counsel, Inspector General, Assistants To The Secretary Of Defense, Director of Administration and Management, Directors of the Defense Agencies (on the web at http://www.dtic.mil/dodim/oct1393.html), October 13, 1993.

[21] S. Butler, D. Diskin, N. Howes, K. Jordan, Architectural design of the common operating environment for the global

command and control system, IEEE Software 13(6), 1996, pp. 57–65.

[22] C. Finkelstein, P. Aiken, Data Warehousing and Decision Support: Knowledge Management for a Connected World, McGraw-Hill, 1996, New York. ISBN 0-07-913705-9.

[23] P. Aiken, P. Piper, Estimating data reverse engineering projects, Proceedings of the 5th Annual Systems Reengineering Workshop (Johns Hopkins University Applied Physics Laboratory Research Center Report RSI-95-001), February 7–9, 1995, Monterey CA, pp. 133–145.

[24] P.H. Aiken, Y. Yoon, Implementing the Organizational Data Quality Framework: A Case Study. Information Resource Management Journal (accepted for publication).

[25] R. Morey, Estimating and improving the quality of information in a MIS, Communications of the ACM 25(5), 1982, pp. 337–342.

[26] M. Svanks, Integrity analysis – methods for automating data quality assurance, Information and Software Technology 30(10), 1988, pp. 595–605.

[27] S. Broussard et al., Data Quality Engineering Handbook Defense Logistics Agency, Alexandria, VA 1994.

[28] E. Paige Jr., From the Cold War to the Global Information Age, Defense Issues 10 (34) (Prepared remarks by Emmett Paige Jr., assistant secretary of defense for command, control, communications and intelligence, to the Catoctin Chapter of the Armed Forces Communications–Electronics Association, Fort Ritchie, Md., Feb. 27, 1995).

[29] Enterprise Reengineering, Who's Talking Now: Cynthia Kendall on Reengineering the Defense Department, Enterprise Reengineering March 1996, p. 38.

[30] P. Constance, DISA tries to save some of CIM as Pentagon kills off program, Government Computer News 1–2 6–96.

[31] E. Paige Jr., Six Emerging Trends in Information Management, Defense Issues 11 (16) (Address by Emmett Paige Jr., assistant secretary of defense for command, control, communications and intelligence, at the American Defense Preparedness Association's Information Management for the Warfighter Symposium, Vienna, Va., Feb. 29, 1996).

Dr. Peter H. Aiken is a Research Director with Virginia Commonwealth University's Department of Information Systems/Information Systems Research Institute and held the position of Computer Scientist with the Office of the CIO of the Defense Information Systems Agency. Project experience and publications have been in the areas of systems engineering, data reverse engineering, hypermedia-based software requirements engineering tools and techniques. He has managed numerous re-engineering efforts for government and industry and is the author of Data Reverse Engineering (McGraw-Hill 1996) and the co-author with Clive Finkelstein of Data Warehouse Engineering (McGraw-Hill 1998). His e-mail address is: paiken@acm.org.

Youngohc Yoon is an associate professor in the Department of Information Systems at Virginia Commonwealth University. She received her M.S. from the University of Pittsburgh and her Ph.D.

from the University of Texas at Arlington. She was an assistant professor of the CIS department at Southwest Missouri State University. She has published over twenty articles in leading journals such as MIS Quarterly, Decision Support Systems, Journal of Management Information Systems, Information and Management, Journal of Operation Research Society, and others.

Belkis Leong-Hong is the former DOD Data Administrator and is a former Deputy Assistant Secretary of Defense for Plans and Resources. She is currently serving as the Principal Deputy Director and Chief Information Officer of the Defense Security Service. Her address and e-mail are: 1340 Braddock Place, Alexandria, VA 22314/BLeong-Hong@dss.mil.
