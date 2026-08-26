---
otero_id: 20849
otero_key: "U9QFUHZ7"
title: "EDI controls design support system using relational database system"
authors: "Sangjae Lee; Ingoo Han"
year: "2000"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(00)00071-3"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# EDI controls design support system using relational database system

Sangjae Lee <sup>a,1</sup>, Ingoo Han <sup>b,)</sup>

Techno-Management Research Institute, Korea AdÕanced Institute of Science and Technology, 207-43 Cheongryangri-Dong Dongdaemun-Gu, Seoul 130-012 South Korea Graduate School of Management, Korea AdÕanced Institute of Science and Technology, 207-43 Cheongryangri-Dong Dongdaemun-Gu, Seoul 130-012 South Korea

Accepted 1 April 2000

## Abstract

The purpose of this paper is to introduce EDIRDB EDI controls design support system using a relational databaseŽ system , a prototype audit support system based on a relational database designed to act as a decision aid for EDI auditors. . This paper describes how EDIRDB operates; explicates the manner in which a relational database is utilized to support the design of EDI controls; suggests relevant risks resulting from the absence of some controls; and suggests test results. The system recommends effective controls and shows relevant risks in a specific organizational context, suggesting test procedures for that particular company.

The EDIRDB database consists of nine tables: 1 four tables from the entities ENVIRONMENTS, CONTROLS, RISKS,Ž . and TESTS, and 2 five tables corresponding to the relations between each of the four entities. An E–R Entity–Relation-Ž . Ž ship diagram along with a data flow diagram are drawn to show the system’s design. Relevant controls, risks, and test. procedures along with their results can be stored for each individual company. Managers can suggest required controls, relevant risks, and test procedures from results coming through cross referencing e.g., JOIN, PROJECTION, and SELECTŽ commands between the nine base tables. This system improves the efficiency and effectiveness of EDI auditing and may. also be applied to general IS auditing. q 2000 Elsevier Science B.V. All rights reserved.

Keywords: EDI; Relational database system; Environments; Controls; Risks; Tests

## 1. Introduction

EDI Electronic Data Interchange refers to anŽ . application of information technology that allows trading partners to send, receive, and process electronic documents from computer to computer. EDI systems contribute to reducing paperwork as well as lowering administrative costs and enhancing competitive advantage. It is important to understand a few critical aspects of EDI in order to obtain significant benefits from the implementation of the system.

One critical issue is the potential risks presented by the application of EDI technology 20,22 . Orga-<sup>w</sup> <sup>x</sup> nizations may face serious risks if decisions are based on incorrect data, are caused by deliberate computer abuse 30 or computing or human error<sup>w</sup> <sup>x</sup> and omissions, or if processing is disrupted by natural disasters. Inaccurate data may result in invalid issuance of production orders or payment bills. The intentional or unintentional loss of EDI resources Ž . e.g., hardware and software , in which large amounts of money are invested, may force organizations to discontinue operations if those resources cannot be promptly recovered. The computer systems that store EDI documents must be kept secure and their integrity sustained. As EDI transactions are transmitted through third-party networks, the data may be altered or corrupted by VAN Value Added Network staff.Ž . Unauthorized personnel using a VAN may input erroneous or invalid transactions that could lead to legal problems and other disputes with trading partners. Both parties, the sender as well as the receiver, of each transaction must ensure that their partner has established proper controls to ensure that EDI transmission will be accurate, authorized, and secure. Errors and omissions must be prevented in order to save both parties from substantial losses. Records must be retained for a specified amount of time in order to correct errors and recover transactions.

The objective of EDI auditing is to ensure that organizations achieve their goals through the implementation of EDI. IS auditing refers to the process of collecting and evaluating evidence in order to determine that IS is safeguarding assets, maintaining data integrity, effectively accomplishing organizational goals, and efficiently consuming resources through use of various controls 32 . EDI managers must<sup>w</sup> <sup>x</sup> recognize areas of concern within the EDI system that should be addressed and reviewed by auditors. Critical audit issues include the review of contingency planning and procedures for system development 18 . The objectives of EDI auditing can be <sup>w</sup> <sup>x</sup> achieved only if organizational management establishes proper controls.

There exist many alternative forms of controls, with environmental factors affecting the design of these controls. Organizational factors such as transaction volume, complexity, and processing speed affect the effectiveness of these controls. It is, therefore, difficult to establish if–then rules explaining the choice of controls in certain organizational contexts. The first step in the design of EDI controls is a preliminary review of the organization and its management practices in order to obtain information necessary for management to make decisions on the appropriate level of controls. The benefits of EDI controls depend on the organizational context <sup>w</sup> <sup>x</sup> 4,17,18,23 . Large organizations with sophisticated IS need more formal controls than do small firms, as they process large volumes of data at high speed. It may not be efficient for EDI managers to implement full controls that require significant resources for smaller companies. The appropriate levels of controls should be determined according to organizational contingencies. Different organizational environments require distinct types and levels of controls.

The benefits of decreased errors due to EDI control systems are hard to assess. Nevertheless, EDI auditors should determine which controls are the most cost effective, and recommend those that are most needed. They should attempt to weigh the marginal cost of each control against its marginal benefits. Thus, EDI managers can allocate IS resources step by step to design and implement controls most effectively.

Subjective and context-sensitive judgments have been used in the past to evaluate and determine the required controls. Analogies from the past experiences of EDI auditors are often utilized in designing controls and assessing risks. However, IS auditors have difficulty in recalling specific IS controls 33 ;<sup>w</sup> <sup>x</sup> the interaction among related controls may complicate the design and audit of IS controls. Cognitive and situational limitations of EDI auditors may also hinder the effectiveness of this reasoning process. Since only a small number of cases can be observed by EDI auditors, their ability to retrieve analogous cases may be limited. The increasing complexity of computerized systems raises the need for improved assistance for evidence collection and evaluation. The tasks of evaluating and designing EDI controls as performed by EDI managers or internal auditors are difficult and unstructured, and so demand the consideration of various interacting factors.

Auditors have increasingly recognized the complexity of evidence collection and evaluation decisions during the performance of an audit. As the evaluation of the controls and risks is an unstructured process, auditor decision-support software is needed. This software focuses on the decision Že.g., evaluation of evidence, risk analysis to be made. rather than the data to be collected in assessing the reliability of controls 32 .<sup>w</sup> <sup>x</sup>

One of the critical aspects for EDI auditing is the need to suggest a cost–benefit design of EDI controls and to assess the risk. Appropriate test procedures should then be suggested. EDI controls should be designed so that they focus on vulnerable subsystems in order to reduce overall risks. More resources need to be invested for the auditing and designing of controls in these vulnerable subsystems. Furthermore, the relation between controls and risks must be established in order to validate the effectiveness of these controls. It is equally important to investigate whether these controls are functioning effectively. Various evidence collection procedures e.g., code Ž review, test data, integrated test facility are sug- . gested in order to assess the quality of EDI controls.

The purpose of this paper is to introduce EDIRDB ŽEDI controls design support system using relational database system , a prototype audit support system . based on a relational database designed to act as a decision aid for EDI auditors. This paper describes how EDIRDB functions and explicates the means by which a relational database is utilized to support the design of EDI controls; it also suggests relevant risks from the absence of some controls, and proposes test results. The system recommends effective controls and shows relevant risks in specific organizational contexts, suggesting test procedures for specific companies.

## 2. Existing audit support systems

To evaluate the quality of IS the auditor must use various auditing methods. These methods can be categorized as evidence collection and evaluation techniques 33 . Evidence collection techniques in- <sup>w</sup> <sup>x</sup> clude generalized audit software that examines the data quality and systems processes, and undertakes analytical review. Code review, test data, concurrent auditing techniques, and performance monitoring tools are also evidence collection techniques. These methods collect data on system security, integrity, effectiveness and efficiency. Evidence evaluation techniques help IS auditors combine piecemeal evidence to make a global evaluation; these include various deterministic, analytic, and probabilistic models that explicate the relationship between controls and their effectiveness. EDIRDB is formulated as a systematic aid for evidence collection and evaluation by managing the data of environments, controls, risks, and tests, and by using cross reference functions e.g., JOIN, PROJECTION, and SELECTŽ commands ..

Many computer-based decision aids have been recently developed to support auditors’ evidence collection and evaluation decisions. Audit software provides data retrieval, data manipulation, and reporting capabilities oriented to the needs of auditors. The problems caused by the sophistication and diversity of IS demands the implementation of this software. Simulation software, for example, has been developed to facilitate the determination of critical controls for overall system reliability by using a sensitivity analysis of the control’s reliability 3 . Simulation<sup>w</sup> <sup>x</sup> modeling software has also been created to determine where further evidence must be gathered, and when more in-depth investigations must be carried out to determine whether past system activities have met established standards 12 . Audit tools such as<sup>w</sup> <sup>x</sup> generalized audit software packages have been developed to provide data retrieval, data manipulation, and reporting capabilities specifically oriented to the needs of auditors. This software allows the auditor to use a high-level problem-oriented language to invoke functions to be performed on data. Auditors can increase their awareness of a system and be supported during semistructured and unstructured decisions by specialized audit software.

AI artificial intelligence applications also existŽ . to aid in auditing. Garner and Tsui 13 built a<sup>w</sup> <sup>x</sup> questionnaire generator that assists auditors in determining the required evidence that should be collected when an error or irregularity is identified. The authors used AI techniques derived from the knowledge of IS auditors. Bailey et al. 1 constructed The<sup>w</sup> <sup>x</sup> Internal Control Model TICOM system, which en- Ž . ables auditors to analyze and evaluate an internal control system; modeling these systems using the knowledge of experts helps auditors to capture the characteristics of control systems, and produces a model of that system which helps the auditor assess whether control objectives have been satisfied. CBR Ž . Case-based reasoning has been also applied to IS controls 10,19,25,27 CBR is used to analyze past<sup>w</sup> <sup>x</sup> cases as a way of reminding the auditor of previous control failures. It suggests a pattern of successful controls so that auditors can evaluate their appropriateness in view of the current situation.

Many of the ‘Big Six’ accounting firms have developed decision support systems to support the auditing process 26 . Deloitte and Touche’s FR<sup>w</sup> <sup>x</sup> score system assesses the likelihood of fraudulent financial statements. Coopers and Lybrand’s Risk Advisor, Price Waterhouse’s PLANET, and KPMG Peat Marwick’s Inherent Risk Analysis have also been developed to support risk assessment. AUDIT-PLANNER was designed as a rule-based system to estimate the planning stage materiality level 29 . Gal<sup>w</sup> <sup>x</sup> <sup>w x</sup> <sup>w x</sup> 11 , Hansen and Messier 15 , and Meservy et al. <sup>w</sup> <sup>x</sup> 24 developed rule-based systems to aid internal control evaluations. Coopers and Lybrand’s C&L Control Risk Assessor uses a large decision tree along with a questionnaire to evaluate internal controls. Ernst and Young’s Flow Eval suggests a flowchart for accounting systems and helps auditors evaluate the adequacy of internal controls. Price Waterhouse has developed three expert systems, Systematic, Saville and AS<sup>r</sup>400, which help auditors suggest internal controls that would minimize control risks in certain technical platforms. Deloitte and Touche developed Internal Controls Expert that help auditors evaluate internal controls using hypertext and CD-ROM technology.

These systems are designed to perform individual tasks in the process, such as internal control evaluation or risk assessment. The systems assume that the auditor has already assessed the level of inherent and control risks, or has identified test procedures that can suggest controls from the current ‘‘level’’ of risks. One desirable approach would be for the system itself to help the auditor construct the tables of environments, controls, risks, and tests and then interrelate them. In developing the structure of the modelbase in IS auditing with their corresponding management systems, the ‘‘relational concept’’, owing to its user-friendliness and flexibility necessary for the type of auditing procedures, can be suitably used. Since relations take the form of two-dimensional tables, they are easily understood and used by EDI auditors. A model is equivalent to a relation under the relational decision support system, and can assist auditors by providing access to desired data and clarifying data structures. Hansen and Messier <sup>w</sup> <sup>x</sup> 14 suggested the use of a relational database management system to describe complex relations among controls, along with their locations, the vulnerabilities caused by their absences, and any potential exposures. The system assists auditors in making decisions about where evidence should be gathered dealing with the reliability of controls. A relational database has been shown to enhance the management and analysis of basic cases, because these fields of tables can be easily deleted, changed, or added. Redundancy of data can be reduced, as each entity for different applications contains only the information needed for its domain, and duplicated storage of the same information across different applications is controlled. In addition, inconsistencies are avoided to some extent by ensuring that any change made to either entry is automatically applied to the other 17 .<sup>w</sup> <sup>x</sup>

The relational algebraic operations such as JOIN, PROJECTION, and SELECT enable auditors to examine various tables e.g., environments, controls, Ž risks, and tests . These store test results show the. nature of control failures, display locations where controls are needed, point to vulnerabilities that arise as a result of control failure, and suggest possible exposures resulting from control failure.

## 3. Need for relational decision support for EDI auditing

There is a need for decision support systems to manage the sequence of steps from risk assessment, through test procedures, to the suggestion of internal controls. EDIRDB EDI controls design support sys- Ž tem using relational database system was designed . to support this assessment of risks, test procedures, and the evaluation of controls. This study is based on the relational approach to a decision-support model for IS auditing proposed by Hansen and Messier <sup>w</sup> <sup>x</sup> 14 . The relational decision support system has been theoretically studied for its extended effectiveness in decision-support 9,31 . Hansen and Messier 14<sup>w</sup> <sup>x</sup> <sup>w x</sup> suggested that relational database systems can assist in the determination of the scope of evidence collection, by providing information about the location of where controls are needed.

The relational database system can assist EDI auditors in evaluating the outcome i.e., subsequentŽ risks of recommended controls, suggest relevant. measures for their evaluation i.e., test procedures ,Ž . and show the present state of controls by indicating test results. These recommendations can only be justified if they are relevant to the current problem. The controls can turn out to be less useful if they do not reduce the risks to the system. In such cases, EDI auditors would need to change the recommendations in order to better suit the current situation. In addition, the implementation of these controls are not attractive if the test procedures cannot be implemented. For instance, some concurrent auditing techniques to test controls, such as an integrated test facility or snapshot techniques, demand extensive IS expertise and implementation costs.

Because these relations take the form of two-dimensional tables, they are easy for EDI auditors to use. In addition, there is no preferred query method, which enhances flexibility 14 . The algebraic opera-<sup>w</sup> <sup>x</sup> tions, JOIN, PROJECT, and SELECT on the two-dimensional tables, derive the diverse tables necessary for decision-support in a straightforward way. The risk to both present controls and possible recommended controls can be computed from the operations of either PROJECT, JOIN, and SELECT in a relational database system where controls and risks are stored in tables and the relations between these tables are then defined. Auditors need to pay special attention to any controls that lead to high-risk when those controls are not working properly. Auditors must also strengthen test procedures to make sure that these controls are functioning. The risks and all test procedures relevant to the retrieved case can assist EDI auditors in understanding any comprehensive solution for the current case. The database may be updated as EDI auditors enter new information about the current case and any other environmental information. The data from the case in question, along with recommended controls and test results, are entered into the database so that auditors can make decisions on the basis of the newly updated database.

![](/api/attachments/U9QFUHZ7/fulltext/images/c1a144081015ec05219cb2534c38acb052aac9a3d597389cd6e4dfb6f506a45a.jpg)  
Fig. 1. Entity–relationship diagram.

Each entity is identified by a unique number, or key. The table ENVIRONMENTS describes general situational circumstances of the EDI system that affects EDI controls and implementation. As EDI becomes increasingly important as a viable alternative in processing transactions, attention needs to be paid to the overall environmental contexts that affect the successful use of EDI. Most preceding EDI studies have used innovative theories to identify the factors that influence implementation.

## 4. E–R diagram and database design

One widely known approach in semantic modeling for the design of databases is the so-called Entity–Relationship E–R approach 5,6 . The E–R Ž . <sup>w</sup> <sup>x</sup> diagram is depicted in Fig. 1; it suggests that the relational database system has four entities: ENVI-RONMENTS, CONTROLS, RISKS, and TESTS.

The complicated interconnections between controls, risks, environments, and tests can be conceptually represented using the data modeling approach. Five tables can be produced from these relations between entities, in addition to showing four tables from each individual entity. Major relations are constructed as follows:

```txt
ENVIRONMENTS (ORGANIZATION#, ORGANIZATION_NAME, ORGANIZATION_INDUSTRY, ORGANIZATION_SIZE)
CONTROLS (CONTROL#, CONTROL_CLASS, CONTROL_DESCRIPTION)
RISKS (RISK#, RISK_CLASS, RISK_DESCRIPTION)
TESTS (TEST#, TEST_CLASS, TEST_DESCRIPTION)
ENVIRONMENT_CONTROLS (ORGANIZATION#, CONTROL#, CONTROL_STATE, CONTROL_DATE)
CONTROL_RISKS (CONTROL#, RISK#, CONTROL_RISK_RELATION)
CONTROL_TESTS (CONTROL#, TEST#, TEST_RELEVANCE)
ENVIRONMENT_RISKS (ORGANIZATION#, RISK#, RISK_LEVEL, RISK_DATE)
ENVIRONMENT_TESTS (ORGANIZATION#, TEST#, RESULT#, TEST_RESULT, RESULT_DESCRIPTION, TEST_DATE)
```

The ENVIRONMENTS table includes the following attributes: ORGANIZATION<sub>–</sub>a, ORGANIZA-TION NAME, ORGANIZATION INDUSTRY, <sub>– –</sub> and ORGANIZATION SIZE. This table is a super- <sub>–</sub> set of five relations:

Industry ORGANIZATION Ž a, EXTERNAL INFLUENCES, TECHNOLOGICAL CHANGE. <sub>– –</sub> <sub>–</sub> IS ORGANIZATION Ž <sub>– –</sub>a, SIZE, PROFESSIONALISM, DECENTRALIZATION, MANAGERIAL ATTI-TUDE, SOPHISTICATION, PRESENT ROLE OF IS, FUTURE ROLE OF IS, COMMUNICATION <sub>–</sub> <sub>– –</sub> <sub>–</sub> <sub>– –</sub> <sub>–</sub> OPENNESS. TASK ORGANIZATION Ž a, TASK INTERDEPENDENCE, TASK ROUTINENESS. <sub>– –</sub> <sub>–</sub> PARTNER ORGANIZATION Ž <sub>– – – –</sub>a, PARTNER TRUST, PARTNER INTERDEPENDENCE, PARTNER COMMITMENT. PERFORMANCE ORGANIZATION Ž a, IMPROVED RELATION, COMPETITIVE ADVANTAGE. <sub>– – –</sub>

An ENVIRONMENTS entity can have five subentities: INDUSTRY, IS, TASK, PARTNER, and PERFORMANCE. These represent industry, IS, task, partnership characteristics, and overall EDI performance, respectively. The tables of INDUSTRY, IS, TASK, and PARTNERS are composed of industry, IS, task, and partnership characteristics that impact EDI controls and their implementation. These are obtained from structured interviews with EDI managers using a questionnaire. Environmental variables should be considered when designing EDI controls to make control systems more effective and efficient. The recommended controls for a given firm are suggested by using parallel cases that have shown high performance and share a similar environment with that of the target company. The cases are found using a series of SELCTION, PROJECTION, and

JOIN operations against the ENVIROMENTS and five subtypes.

Organizational contextual variables are determined considering several points. First, the study focused on the factors influencing EDI implementation after the adoption of EDI takes place, as well as, EDI controls. Second, various categories of variables, including industry, IS, task, and partnership characteristics that are potential feature descriptors for EDI systems are included. They could potentially influence EDI controls and implementation based on IS controls and EDI literature. Based on a review of the literature on organizational control, including specific innovation–implementation and EDI adoption literature, this paper proposes the following variables attribute name :Ž .

<sup>Ø</sup> industry: external influences EXTERNAL INFLUENCES , technological change TECHNOLOGICAL Ž . Ž <sub>– –</sub> CHANGE ;.

<sup>Ø</sup> IS: size SIZE , professionalism PROFESSIONALISM , decentralization DECENTRALIZATION , man-Ž . Ž . Ž . agerial attitude MANAGERIAL ATTITUDE , IS sophistication SOPHISTICATION , present role of ISŽ . Ž . <sub>–</sub> Ž . Ž . PRESENT–<sup>P</sup>04ROLE OF IS , future role of IS FUTURE ROLE OF IS , communication openness<sub>– – – – –</sub> Ž . COMMUNICATION OPENNESS ;<sub>–</sub>

<sup>Ø</sup> TASK: task interdependence TASK INTERDEPENDENCE , task routineness TASK ROUTINENESS ;Ž . Ž . <sub>– –</sub> <sup>Ø</sup> PARTNER: partner trust PARTNER TRUST , partner interdependence PARTNER INTERDEPEN- Ž . Ž <sub>– –</sub> DENCE , partner commitment PARTNER COMMITMENT. Ž .

Industry, IS, task, and partnership characteristics were assessed using measures from the literature <sup>w</sup> <sup>x</sup> 20 . A multiple seven-point Likert-type scale represented each variable with the exception of size and two items of IS sophistication. Size was then measured by the total number of employees along with annual sales, while the total number of IS staff and the annual IS budget were used as indicators for IS sophistication.

Measures of EDI performance were based on the objectives for EDI usage. Reinforcement of ties with a business partner, improved customer service, cost reduction, and increased reliability of information were the most important benefits reported in EDI literatures e.g., 2 . The PRFORMANCE table Ž <sup>w</sup> <sup>x</sup>. stores the extent of both service improvement IM- Ž PROVED RELATION as well as competitiveness . <sub>–</sub> caused by EDI COMPETITIVE ADVANTAGE .Ž . <sub>–</sub> Five and three items that are seven-point Likert-type scales were used to measure IMPROVED RELA-<sub>–</sub>

TION and COMPETITIVE ADVANTAGE aver-Ž age value of the items is used . For instance, one of. item for IMPROVED RELATION was ‘‘relations with the representative trading partner are greatly improved through reduced response time after EDI adoption’’. Some of the items for COMPETITIVE ADVANTAGE include: ‘‘The efficiency of interdepartmental transaction processing is greatly increased’’; ‘‘Transaction processing costs are greatly reduced after adopting EDI’’. Respondents answered the extent to which they agree or disagree with each statement about performance. The highest and lowest performance value is seven and one. The case that has the value of IMPROVED RELATION and<sub>–</sub> COMPETITIVE ADVANTAGE closer to seven is<sub>–</sub> proposed to be the ‘‘successful’’ case that has implemented appropriate controls.

The table CONTROLS represents the EDI control procedures. The objective of EDI controls is to ensure that an organization achieves its goals through the implementation of EDI. They are activities to safeguard assets, maintain data integrity, effectively accomplish organizational goals, and efficiently consume resources.

There may be many ways to classify controls. This study uses the three dimensions of EDI controls proposed by Lee et al. 22 ; formal, informal, and<sup>w</sup> <sup>x</sup> automated controls. Formal controls refer to ‘‘written management-initiated’’ controls, while informal controls are based on shared beliefs and values developed by members of an organization. Formal controls such as standards, operational procedures, process changes, and formal contracts including legal issues with trading partners and VANs, are basic elements of EDI systems. Informal controls include the use of values, traditions, employee commitment, and social beliefs. Informal controls are initiated by organizational members using the members’ values, judgments and communications. Automated controls are measured with automated control procedures and methods. In view of the high-speed and large volumes of data, it is necessary to install automated tracking and control mechanisms for the purpose of doing continuous functions such as record retention, error corrections, or disaster recoveries.

EDI controls may also be categorized as internal and external controls. Internal controls deal with an EDI system’s internal components such as the application system interface, while external controls are involved with external EDI systems such as a VAN or an EDI system of a trading partner. Internal and external controls are different, as they are developed by EDI-adopting companies and VAN service providers or trading partners , respectively. InternalŽ . controls for EDI systems are established to monitor internal application systems such as a production system, or a sales system linked to an external network. Adequate detective controls and contingency planning should be installed to prevent errors from affecting the whole system, thereby ensuring the continuous operation of the system in a timely manner. External controls are applied to transactions during transmission to a destination e.g., mailboxŽ security, routing control . Because EDI is an interor- . ganizational system, communication is mediated by a VAN or a proprietary network with many trading partners. Invalid or unauthorized transactions can be initiated by staff in a third-party network. Messages may be lost, altered, duplicated, or transposed while they are being transmitted through the network. Consequently, external controls involving a VAN and all trading partners have special importance 4 . <sup>w</sup> <sup>x</sup>

The aforementioned control dimensions can be used to generate a framework of other control types. Internal EDI controls can also be grouped into two more categories: application and communication controls. Application and communication controls are differentiated according to whether they deal with internal EDI systems, such as an application system interface, or external EDI systems, as with the interface with a VAN or a network provided by trading partners. Application controls ensure that the input, processing, and output of transactions are properly authorized and validated. Communication controls are applied to inbound and outbound messages to ensure their security. Communication controls protect the internal system from any mishaps occurring outside e.g., edit checks to identify erro-Ž neous inbound transactions or vice versa e.g., com-. Ž pleteness check in generation and transmission of outbound messages ..

The CONTROLS table contains the attributes CONTROL<sub>– –</sub>a, CONTROL CLASS, and CON-TROL DESCRIPTION. Before EDI auditors recommend controls, a list of available control measures must be identified. The list needs to be continuously maintained in order to include updated procedures and practices. EDI controls are then classified into several types such as application and communication controls, or internal and external controls. Measures for EDI controls for this study were newly developed, for which various sources 4,17,18,23 were<sup>w</sup> <sup>x</sup> referred to. Table 1 shows an example of table CONTROLS.

Table 1 Controls table

<table><tr><td>Control_#</td><td>Control_class</td><td>Control_description</td></tr><tr><td>101</td><td>Internal formal application controls</td><td>system change control by authorization</td></tr><tr><td>103</td><td>Internal formal application controls</td><td>transaction log for the possible errors and collapse</td></tr><tr><td>104</td><td>Internal formal application controls</td><td>appropriate system login procedures using password</td></tr><tr><td>102</td><td>Internal formal application controls</td><td>integrity check of the message before processing in the application</td></tr><tr><td>201</td><td>Internal formal communication controls</td><td>Integrity check after generating EDI messages</td></tr><tr><td>202</td><td>Internal formal communication controls</td><td>authentication of trading partners after receiving EDI messages</td></tr></table>

Table 2 Risks table

<table><tr><td>Risk_#</td><td>Risk_class</td><td>Risk_description</td></tr><tr><td>101</td><td>risk of application</td><td>Data files are inaccurately processed</td></tr><tr><td>102</td><td>risk of application</td><td>Malicious intruders insert unauthorized module</td></tr><tr><td>103</td><td>risk of application</td><td>Programs are changed without authorization</td></tr><tr><td>104</td><td>risk of application</td><td>System downtime seriously affect performance of EDI</td></tr><tr><td>105</td><td>risk of application</td><td>System performance is greatly decreased by the frequent system failures</td></tr><tr><td>106</td><td>risk of application</td><td>unauthorized input</td></tr></table>

The table of RISKS shows various risks from the implementation of EDI Table 2 . Each progressiveŽ . level of integration represents a higher level of sophistication, dependency, and vulnerability. There are classes of risks such as ‘‘risks of application’ and ‘‘risks of VAN’’. The ‘‘risks of application’’ indicate risks arising from the failures or errors in internal applications. Messages can be altered or lost as a result of a disruption of internal data processing. The failures of one system rapidly influence other systems within a highly integrated system. An internal system integration with internal systems also increases ‘‘risks from VAN’’, or system vulnerability through a domino effect caused by the mishaps of trading partners or a VAN. The interdependence with trading partners lends itself to the possibility of sharing technology and databases. A domino effect can cause every trading partner to topple by the mistakes of just one of the partners. All parties must therefore protect themselves from possible disclosures or alterations of any transmitted messages made by other partners, or by an unauthorized third party.

The table TESTS indicates the test procedures that examine whether a given portion of a computerized system is properly functioning Table 3 . TheŽ . examples include various computer-aided audit techniques such as a concurrent audit module or an integrated test facility. Choosing an appropriate test procedure for controls can be accomplished by selecting substantive tests using the relation between CONTROLS and TESTS. This test can be conducted as a process to ensure that controls are actually functioning. Generalized audit software can be used to examine the quality of data produced by a program. ‘‘Test data’’ approaches use a sample of data to assess the quality of a program, and are also used to test specific aspects within a program. Program code comparisons provide assurance that the software being audited is the correct version. There are many test techniques used to control highly automated systems: concurrent audit techniques; electronic audits trails; continuous and intermittent simulations CIS techniques; real-time feedback fromŽ . integrity checks; and parallel simulation techniques to audit batch processing. Concurrent auditing techniques identify problems in application systems on a more timely basis, and use embedded modules in application systems or system software to collect, process, and print audit evidence.

Table 3 Tests table

<table><tr><td>Test_#</td><td>Test_class</td><td>Test_description</td></tr><tr><td>101</td><td>application test</td><td>Utility Software such as Flow charter Execution path Analyzer</td></tr><tr><td>102</td><td>application test</td><td>Generalized Audit Software</td></tr><tr><td>103</td><td>application test</td><td>Parallel Simulation</td></tr><tr><td>104</td><td>application test</td><td>Code Review</td></tr><tr><td>105</td><td>application test</td><td>Continuous and Intermittent Simulation</td></tr></table>

Note that all five relations among the four entities are ‘‘many-to-many’’; for example, there exist more than one instance of risks that are related to some instance of controls, and vice versa. The EnÕironments for Controls relation in Fig. 1 indicates the relation between ENVIRONMENTS and CON-TROLS. The ENVIRONMENT CONTROLS table stores the environmental status and the control status in each environment Table 4 . This relation canŽ . provide information about the appropriate controls in certain environmental contexts, by enabling auditors to systematically retrieve cases with high performance from among similar cases in the same environment as the case in question. The value of the CONTROL STATE field of the ENVIRON-<sub>–</sub> MENT CONTROLS table indicates the usage level<sub>–</sub> of controls, and is assessed using seven-point Likert-type scales. It is very difficult to assess the usage level of controls using quantitative measures such as financial investment amount, personnel resources, etc. that are spent for the implementation of controls. Qualitative scales were used instead to measure the usage of EDI controls. For instance, for the control statement, ’’integrity check of the message is applied before processing in the application‘‘ Ž . CONTROL<sub>–</sub>a is 102 , respondents answered the extent to which they agree or disagree with the statement. The value of CONTROL STATE may be<sub>–</sub> 4 if it has average usage level. CONTROL DATE<sub>–</sub> indicates the last date when the usage level of controls was measured.

The interconnections between environmental variables and EDI controls can be deduced from organizational control and EDI literature 21 . For example,<sup>w</sup> <sup>x</sup> ‘‘decentralization of organization’’ is related to informal controls, as the implementation of innovation is facilitated by organic structures normally associated with decentralization. This facilitates the initiation and testing of new ideas 28 . When EDI profes-<sup>w</sup> <sup>x</sup> sionals have more authority, they are then more likely to act on their own judgment and explore novel approaches. When exceptional incidents occur, EDI professionals can communicate with others to draw on the latter’s knowledge and skills. Informal controls are needed to facilitate this synergy of ideas in such decentralized organizations.

Table 4  
Environment controls table

<table><tr><td>Organization_#</td><td>Control_#</td><td>Control_state</td><td>Control_date</td></tr><tr><td>101</td><td>101</td><td>4</td><td>7/21/1997</td></tr><tr><td>101</td><td>103</td><td>3</td><td>8/11/1998</td></tr><tr><td>101</td><td>104</td><td>3</td><td>3/10/1998</td></tr><tr><td>102</td><td>104</td><td>4</td><td>2/11/1996</td></tr><tr><td>103</td><td>104</td><td>5</td><td>2/12/1996</td></tr><tr><td>101</td><td>102</td><td>7</td><td>9/15/1997</td></tr><tr><td>102</td><td>103</td><td>2</td><td>12/22/1997</td></tr></table>

Task rountineness, for example, is related to the use of internal formal and automated controls. Routine tasks are amenable to standard operating procedures with formal rules and clear performance standards. Managers stress efficiency where activities can be measured quantitatively and are well-defined <sup>w</sup> <sup>x</sup> 18 . This leads to the formalization of work processes. In the case of production departments and assembly lines where such routine processes are typical, the processes linking these departments are usually formalized.

Process efficiency can be improved by automating such easily measured and quantified tasks 8,16 . The<sup>w</sup> <sup>x</sup> speed of repetitive transactions and the lack of human intervention in EDI systems demand prompt detection and correction of errors. Integrated test modules and automated edit checks need to be embedded within internal applications to prevent errors from spreading into other systems. Hence, automated controls are appropriate to cope with routine tasks.

The Risks for Controls relation relates CON-TROLS and RISKS entities, and indicates the relation between controls and risks. The CONTROL<sub>–</sub> RISK RELATION in the CONTROL RISKS table describes the importance of controls for the reduction of risk or the possible amount of risk caused by the absence of controls Table 5 . For instance, ifŽ . automated controls involving electronic signatures have not been properly implemented, the result could be the introduction of unauthorized transactions by outsiders or inaccurate invoicing for services not rendered. CONTROL RISK RELATION uses<sub>– –</sub> seven-point Likert-type scales according to the strength of the relation. That is, CONTROL<sub>–</sub> RISK RELATION has an ordinal value of 1<sub>–</sub> ŽVery Low. Ž . to 7 Very High . If the set of risks and controls are defined and the relations between the two sets are constructed, the importance of EDI controls can be induced in view of their contribution to the reduction of overall risks.

Table 5  
Control risks table

<table><tr><td>Control_#</td><td>Risk_#</td><td>Control_risk_relation</td></tr><tr><td>101</td><td>102</td><td>6</td></tr><tr><td>101</td><td>103</td><td>5</td></tr><tr><td>101</td><td>101</td><td>5</td></tr><tr><td>201</td><td>103</td><td>1</td></tr><tr><td>202</td><td>103</td><td>4</td></tr><tr><td>104</td><td>103</td><td>7</td></tr><tr><td>104</td><td>101</td><td>4</td></tr></table>

The Test Procedures for Controls relation represents the relevant test procedures to examine whether controls are appropriately functioning. The CON-TROL TESTS table represents the candidate test<sub>–</sub> procedures for controls Table 6 . The test dataŽ . approach might be used to test specific aspects of a program, or to assess the quality of application change controls intended to prevent unauthorized modifications of applications. TEST RELEVANCE<sub>–</sub> has seven internal scales ranging from Very Low to Very High according to the extent to which the test procedure is related to control.

The Risks of EnÕironments relation ENVIRON-Ž MENT RISKS table represents the level of risks in. <sub>–</sub> firms within a specific environmental status TableŽ 7 . The level of risks can be assessed, for example,. through the exposures scoring analysis that requires audit management to list the factors which affect the control aspects of systems, and weight their importance to the reliability of the entire system, and then obtain the weighted sum of all these factors 33 .<sup>w</sup> <sup>x</sup> RISK LEVEL has seven internal scales ranging from<sub>–</sub>

Table 6  
Control tests table

<table><tr><td>Control_#</td><td>Test_#</td><td>Test_relevance</td></tr><tr><td>101</td><td>102</td><td>Moderately High</td></tr><tr><td>101</td><td>103</td><td>Very Low</td></tr><tr><td>101</td><td>105</td><td>Very High</td></tr><tr><td>201</td><td>103</td><td>Very Low</td></tr><tr><td>102</td><td>103</td><td>Moderately High</td></tr><tr><td>202</td><td>103</td><td>Moderate</td></tr><tr><td>103</td><td>104</td><td>Very High</td></tr></table>

Table 7  
Environment risks table

<table><tr><td>Organization_#</td><td>Risk_#</td><td>Risk_level</td><td>Risk_date</td></tr><tr><td>102</td><td>101</td><td>Moderately High</td><td>3/13/1996</td></tr><tr><td>102</td><td>103</td><td>Moderate</td><td>11/21/1997</td></tr><tr><td>101</td><td>105</td><td>High</td><td>4/9/1998</td></tr><tr><td>201</td><td>105</td><td>Moderate</td><td>12/10/1997</td></tr><tr><td>101</td><td>104</td><td>High</td><td>7/1/1997</td></tr><tr><td>102</td><td>102</td><td>Very High</td><td>2/10/1996</td></tr><tr><td>101</td><td>103</td><td>Very Low</td><td>7/20/1998</td></tr></table>

Very Low to Very High according to the ‘‘real’’ risk level of a company and is determined from risk analysis after controls are implemented. RISK<sub>–</sub> DATE indicates the last date when the risk level of environments was measured.

The Test Results of EnÕironments relation EN-Ž VIRONMENT TESTS table indicates the results of. <sub>–</sub> test procedures applied to the environment of an organization Table 8 . The test results constituteŽ . evidence on the reliability of organizational environments. When test results of some environments are unsatisfactory, it indicates that these organizations do not operate EDI controls as they are purported to. Other relations, CONTROL TESTS and ENVI-<sub>–</sub> RONMENT CONTROLS, should be joined with <sub>–</sub> ENVIRONMENT TESTS to explain the test results<sub>–</sub> regarding different controls. The attribute TEST<sub>–</sub> RESULT has seven internal scales ranging from Very Bad to Very Good according to the extent to which controls satisfy the criteria of test procedures. TEST DATE indicates the date when the test of<sub>–</sub> controls was last performed.

The three relations EnÕironments for Controls, Risks of EnÕironments, and Test Results of EnÕironments, are individual-organization based, while the other two relations, Risks for Controls and Test Procedures for Controls, are not. The data for CON-TROL RISK RELATION and TEST RELE-<sub>– – –</sub> VANCE are normatively determined based on the opinion of experts or EDI practitioners in eachŽ company about EDI controls. The CONTROL . <sub>–</sub> RISK RELATION and TEST RELEVANCE fields<sub>– –</sub> have the same value for every organization. Two keys should be independently determined to identify the relation Risks for Controls Že.g., CONTROL<sub>–</sub>a and RISK a for CONTROL RISK RELATION .. Although the ‘‘level’’ of controls and risks and ‘‘test results’’ differ among companies, the relations between controls and risks or between controls and tests are assumed to be the same for all companies.

Table 8  
Environment tests table

<table><tr><td>Organization_#</td><td>Test_#</td><td>Result_#</td><td>Test_result</td><td>Result_description</td><td>Test_date</td></tr><tr><td>101</td><td>102</td><td>201</td><td>Bad</td><td>Transactions not correctly recorded in accounting records</td><td>3/13/1996</td></tr><tr><td>101</td><td>104</td><td>204</td><td>Moderate</td><td>Organization recover from failures within appropriate times</td><td>3/15/1996</td></tr><tr><td>101</td><td>105</td><td>205</td><td>Very Good</td><td>All transactions received are passed to each relevant applications and only once</td><td>3/18/1996</td></tr><tr><td>101</td><td>103</td><td>210</td><td>Very Bad</td><td>Unauthorized messages sent or received and acted upon</td><td>12/10/1997</td></tr><tr><td>103</td><td>103</td><td>301</td><td>Good</td><td>Encryption keys are kept secure and private</td><td>7/1/1998</td></tr><tr><td>104</td><td>103</td><td>302</td><td>Bad</td><td>Introduction of non-authentic transactions</td><td>12/10/1998</td></tr><tr><td>107</td><td>101</td><td>304</td><td>Moderate</td><td>Incorrect translation of application data to/from interchange document</td><td>12/20/1998</td></tr></table>

One of the two generalized intersection tables, CONTROL TESTS, can be related to ENVIRON-<sub>–</sub> MENT TESTS through the common attribute<sub>–</sub>

TEST a. ENVIRONMENT TESTS can be also related to CONTROL RISKS after ENVIRON-<sub>–</sub> MENT TESTS is joined with the ENVIRON-<sub>–</sub> MENT CONTROLS table; the common attribute is<sub>–</sub> then ORGANIZATION<sub>– –</sub>a and CONTROL a. Hence, the ENVIRONMENT TESTS table can tie the test results of each organization into two generalized intersection tables. This will identify controls or risks or the relation between them that are relatedŽ . to specific test results. If the result of a test is acceptable, the controls that are assessed by the test procedure through a join with the CONTROLŽ <sub>–</sub> TESTS table along with risks through a join with. Ž the CONTROL RISKS table can be identified; the. controls that are closely related to risks should be strengthened.

![](/api/attachments/U9QFUHZ7/fulltext/images/79bb04171b2c3d54d31f483839ba3dbe69e9e163ba89b480594e239d8b20d654.jpg)  
Fig. 2. Context diagram.

ENVIRONMENT CONTROLS and ENVIRON-MENT RISKS or the joined table contain theŽ . <sub>–</sub> ‘‘real’’ value of the usage level of controls or risk level obtained from interview or risk analysis with organization and are different from CONTROL<sub>–</sub> RISKS table which store the theoretically and normatively determined relation between controls and risks before any interview or risk analysis is con- Ž ducted . CONTROL RISK can provide the estima-. <sub>–</sub> tion of risk level for the controls before they are implemented. Thus, CONTROL RISK RELATION<sub>– –</sub> is different from the ‘‘real’’ or empirically determined association between controls and risks, which the joined table of ENVIRONMENT CONTROLS<sub>–</sub> and ENVIRONMENT RISKS provides. <sub>–</sub>

## 5. Data flow diagram

While data models provide a static view of the data used by a company, the flow of data through procedures shows a dynamic view. A data-flow diagram represents a logical flow of data through various processes, and is a hierarchical set of diagrams; each diagram in the set is a decomposition of the preceding diagram 34 . The context diagram is the <sup>w</sup> <sup>x</sup> top-level set of diagrams, since the whole process is encompassed within a single circle. The context diagram of EDIRDB is illustrated in Fig. 2. Four entities serve as both sources and destinations with respect to the data involved in EDI auditing. The type of data involved in each flow is written along the flow line.

A level-1 data flow diagram of EDIRDB is indicated in Fig. 3. The four tables were shown with entity symbols in the DFD, as they are sources or destinations of data that reside outside the system being diagrammed. CONTROLS, RISKS, and TESTS serve as sources with respect to data involved in the controls design process, while ENVI-RONMENTS is both a source and a destination from the process. The data stores specifics such as ENVI-RONMENT CONTROLS, CONTROL RISKS, and CONTROL TESTS; these appear in the level-1 diagram. The level-1 data flow diagram indicates four subprocesses, numbered 1.0, 2.0, 3.0 and 4.0. The diagram describes the content of the data flows, the processes involving the data, the storage of the data, and the sources and destination of the data. This shows specific details of these three processes: control designs, risk suggestions, and control tests.

![](/api/attachments/U9QFUHZ7/fulltext/images/37a81022751eb1089a2a5aec326d85500ecc604733c39171ccc9438a10ac58b3.jpg)  
Fig. 3. Level-1 data flow diagram.

Process 1.0 collects information on the new case. A new client organization is interviewed and their industry, IS, task, partner characteristics are measured. The items to be measured are retrieved from the ENVIRONMENTS table and the collected data, in turn, updates the ENVIRONMENTS table. Process 2.0 identifies the controls to be recommended. The criterion of controls recommendation in process 2.0 is to identify the controls that are related to high EDI performance in similar organizational contexts to the current case. The organizational characteristics and performance value should be found in the ENVI-RONMENTS table and its subtypes to determine the ‘‘successful’’ case, i.e., a similar organization with high performance value. The CONTROLS table is joined with the ENVIRONMENT CONTROLS table<sub>–</sub> to find the controls to be recommended that have high values in the ‘‘successful’’ case. The recommended controls are then transferred to process 3.0 and 4.0 to suggest relevant risks and to perform tests. Process 3.0 uses the values CONTROL STATE and CONTROL RISK RELATION of the ENVIRON-MENT CONTROLS and CONTROL RISKS tables, respectively, as well as the RISKS table to estimate ‘‘preliminary’’ risk level before the controls are implemented. If the risks from process 3.0 turn out to be high, the recommendation can be changed to increase the usage level of controls, or to include other controls. Thus, another arrow is added from process 3.0 to 2.0, which represents ‘‘Demand for Change in Controls Recommendation due to High Risks’’. Process 4.0 suggests test results for the controls recommended; it retrieves the appropriate test procedures to be performed from the CON-TROL TESTS and TESTS tables, and stores the test<sub>–</sub> results in the ENVIRONMENTS TESTS table.

Some of the databases i.e., ENVIRONMENTS,Ž CONTROLS, ENVIRONMENT CONTROLS of. EDIRDB were collected from EDI adopters in Korea. This data was obtained from interviews and discussions with EDI personnel, from publicly available information provided by companies which have adopted EDI, and from relevant literature related to EDI controls and risks. The database is composed of 110 companies of more than 5000 companies that have adopted EDI in Korea. The data for RISKS, TESTS, CONTROL RISKS, and CON-TROL TESTS tables were made by adapting vari-<sub>–</sub> ous EDI literature 4,17,18,23 and from IS auditing<sup>w</sup> <sup>x</sup> <sup>w</sup> <sup>x</sup> 33 .

EDIRDB was developed using FoxPro 2.6 for Windows 98. The system defines database structures with relevant attributes of tables, and then automatically builds an interactive questionnaire to collect and edit the cases. It creates a customized questionnaire which offers a sophisticated means of collecting cases. EDI auditors can create, delete, or change the database through the user’s interface screen. Users can then browse through the various values of attributes, and edit the database after EDIRDB has finished prompting users for new data.

As the criteria for control design and test procedures changes over time, the system can be easily adjusted to incorporate new considerations by changing the database structure or attributes of the relational tables. This updated database allows more accurate prediction with recommendations for better controls and test procedures.

The nine base tables can be further joined and divided into several new tables that contain specific information about one case. These individual tables can be separately constructed using the JOIN, PRO-JECTION, and SELECT commands in the relational database, and then deliver ‘‘efficient’’ and specific information that can be useful to EDI auditors, and can be joined and projected to provide other relevant information to support auditing decisions. There is no preferred query method, since flexibility is enhanced 14 . The algebraic operations, JOIN, PRO- <sup>w</sup> <sup>x</sup> JECT, and SELECT on two-dimensional tables show straightforward information necessary to support diverse decisions.

## 6. Examples of decision support

## 6.1. Recommendation of controls

EDI auditors are required to systematically analyze cases which are similar to their current environment, cases which have successfully implemented EDI controls. Because successful controls lead to high performance, it is necessary to find cases that display high performance. The recommended controls for a certain organizational context can be predicted from parallel past cases in which controls were well-established. EDI managers may invest IS resources to implement the same controls that were considered important in these past cases. To the contrary, EDI auditors need not expend any IS resources to implement controls that have been assigned a low priority from these past cases.

One case was randomly selected from our database and analyzed to show how EDIRDB can help auditors make decisions. The sample case is shown in Table 9.

EDI performance depends on the extent to which companies have appropriately established controls; the competitive advantage derived from EDI can only be maintained if the integrity and accuracy of the data is controlled. Deliberate or erroneous loss of data during data communications can wipe out administrative savings, as well as raising operating costs. If companies make decisions based on incorrect data, they confront serious risks, which might be caused by deliberate computer abuse or by processing disruption due to some natural disaster. Inaccurate data may bring about invalid issuances of orders or bills. EDI controls ensure that an organization achieves its goals through the implementation of EDI. IS controls are activities that safeguard assets, maintain data integrity, effectively accomplish organizational goals, and efficiently consume resources <sup>w</sup> <sup>x</sup> 33 .

<table><tr><td>Attributes</td><td>New case</td></tr><tr><td>EXTERNAL INFLUENCES</td><td>5.33</td></tr><tr><td>TECHNOLOGICAL CHANGE</td><td>4.00</td></tr><tr><td>SIZE</td><td>2.58</td></tr><tr><td>PROFESSIONALISM</td><td>2.00</td></tr><tr><td>DECENTRALIZATION</td><td>4.33</td></tr><tr><td>MANAGERIAL ATTITUDE</td><td>4.00</td></tr><tr><td>IS SOPHISTICATION</td><td>0.17</td></tr><tr><td>PRESENT ROLE OF IS</td><td>5.00</td></tr><tr><td>FUTURE ROLE OF IS</td><td>3.25</td></tr><tr><td>COMMUNICATION OPENNESS.</td><td>5.00</td></tr><tr><td>TASK INTERDEPENDENCE</td><td>4.70</td></tr><tr><td>TASK ROUTINENESS.</td><td>5.80</td></tr><tr><td>PARTNER COMMITMENT</td><td>5.50</td></tr><tr><td>PARTNER INTERDEPENDENCE</td><td>4.50</td></tr><tr><td>PARTNER TRUST</td><td>3.67</td></tr></table>

The study by Lee et al. 22 suggests that EDI<sup>w</sup> <sup>x</sup> controls are critical factors for EDI implementation based on EDI implementation studies and IS control literature. Before an organization decides to implement EDI, EDI controls should be planned in advance in order to strengthen belief that their new system is safe and accurate for users, and to increase the probability of successful implementation and adjustment. EDI controls can improve both relationships with trading partners, and productivity includ-Ž ing cycle-time reductions and can also increase data . accuracy. Hence, it is assumed that if companies then have higher performance than do others, the new EDI controls that have been implemented are more appropriate.

The cases with the highest performance are selected from similar cases and retrieved through the SELECT and PROJECTION commands. If the auditor’s subjective prediction of the most recommendable cases also coincides with those that the EDI system has generated from these same most similar cases, better decisions on the level of controls can be made. In most cases, auditors should also examine this added information from the retrieved cases, and select those most relevant to the audit’s purpose. The auditor can obtain other useful information by requesting complete information about the selected cases from the database. The system can display this complete information about the organization, as well as EDI performance for the selected history of the client.

When EDI auditors implement controls that are related to high performance, they can search cases by: 1 joining the ENVIRONMENTS, ENVIRON-Ž . MENT CONTROLS, and CONTROLS tables; 2Ž . <sub>–</sub> selecting the tuple of joined tables where the attribute values in INDUSTRY, IS, TASK, and PART-NERS are similar to the current case; and 3 findingŽ . similar cases with the highest performance.

These operations can be expressed in a Õiew which shows a virtual table see below . A table, asŽ . seen by an EDI auditor, can be either a base table or the Õiew shown here. A Õiew is a ‘‘virtual’’ table that does not actually exist in physical storage but provides an alternative way for looking at a table 7 . <sup>w</sup> <sup>x</sup> The logical independence provided by a Õiew is obviously important to auditors, who want to diversely interact from a single integrated database and then make comprehensive audit decisions. This also shows that auditors and their programs are independent of the logical structure of the database. The Õiew mechanism enables EDI auditors to focus only on the data that is of vital concern to them. It can also considerably simplify data manipulation operations by EDI auditors. The Õiew, in recommending controls, uses only four environmental variables; however, other variables can be utilized according to the various requirements of auditors. The following Õiew shows an example of the retrieval of cases, in order to recommend additional EDI controls. The case shown in Table 9 was used as the input case.

<table><tr><td>CREATE</td><td>VIEW</td><td>ORGANIZATION_CONTROLS</td></tr><tr><td>AS</td><td>SELECT</td><td>ORGANIZATION_NAME, ORGANIZATION#,CONTROL_CLASS, CONTROL#,CONTROL_DESCRIPTION,</td></tr><tr><td></td><td>FROM</td><td>ENVIRONMENTS, ENVIRONMENT_CONTROLS,CONTROLS</td></tr><tr><td></td><td>WHERE</td><td>CONTROL. CONTROL_# =</td></tr><tr><td></td><td>AND</td><td>ENVIRONMENT_CONTROLS. CONTROL_#</td></tr><tr><td></td><td>AND</td><td>ENVIRONMENT. ORGANIZATION_#</td></tr><tr><td></td><td>AND</td><td>ENVIRONMENT_CONTROLS. ORGANIZATION _#</td></tr><tr><td></td><td>AND</td><td>EXTERNAL_INFLUENCES &gt; 5</td></tr><tr><td></td><td>AND</td><td>EXTERNAL_INFLUENCES &lt; 6</td></tr><tr><td></td><td>AND</td><td>PROFESSIONALSIM &gt; 1.5</td></tr><tr><td></td><td>AND</td><td>PROFESSIONALSIM &lt; 2.5</td></tr><tr><td></td><td>AND</td><td>DECENTRALIZATION &gt; 4</td></tr><tr><td></td><td>AND</td><td>DECENTRALIZATION &lt; 5</td></tr><tr><td></td><td>AND</td><td>MANAGERIAL ATTITUDE &gt; 3.5</td></tr><tr><td></td><td>AND</td><td>MANAGERIAL ATTITUDE &lt; 4.5</td></tr></table>

EDI performance depends on the extent to which customers have appropriately established controls. The retrieved cases may have a different state of implementation and performance, although the other companies may also have similar environmental conditions. As these differences in the state of performance do exist among retrieved cases, it is therefore important to select those specific cases that have the highest performance among the retrieved cases. Since they have a higher performance than the others, more appropriate controls may be then implemented, increasing productivity and reducing costs.

An EDI auditor can identify critical controls through the systematic analysis of retrieved cases. The case that has the highest performance values should of course be selected. In our study, the selected case is Case 48 Table 10 , which has theŽ . highest value in performance among the 10 cases retrieved IMPROVED RELATIONŽ <sup>s</sup>6.1, COM-PETITIVE ADVANTAGE <sup>s</sup> 6.4 . From the se-. lected case, it is possible to determine the controls that effectively affect performance. Controls with a score greater than or equal to five this ‘‘cutoff’’ Ž usage level of five is arbitrarily set and just represents the level that discriminates the ‘‘high’’ and ‘‘low’’ usage level of controls in the Case 48 are. marked. These controls are highly used in Case 48 and might have contributed to the high performance value of Case 48 more than other controls. Five of sixteen EDI controls have a value greater than or Ž equal to five. Auditors, or the organization manage- . ment, should place the utmost emphasis on these controls.

## 6.2. Suggestion of risks and test of controls

A number of other tables can be made by interjoining the nine base tables. EDI auditors can retrieve various information by selecting appropriate tuples from joined tables. The CONTROL RISK RELATION field of CONTROL RISKS <sub>– –</sub> table can be used to suggest ‘‘preliminary’’ a risk level before controls are implemented. The RISK<sub>–</sub> LEVEL field of ENVIRONMENT RISK table should be examined to determine the actual ‘‘substantive’’ company-specific level of risk. When EDI auditors, for example, need information about the risks not actual, but estimated classified asŽ . Unauthorized Access in the controls categorized as Automated Application Controls in Daewoo Chemicals, they can find this information by first joining the tables RISKS, CONTROLS, and CONTROL<sub>–</sub> RISKS, and then joining the tables ENVIRON-MENTS, ENVIRONMENT CONTROLS. By selecting the tuple of joined tables where CONTROL CLASS and ORGANIZATION NAME<sub>– –</sub> are, respectively, Automated Application Controls and Daewoo Chemicals; these operations can be expressed as follows:

<table><tr><td rowspan="10">CREATE</td><td>VIEW</td><td>ENVIRONMENT_RISK_CONTROLS</td></tr><tr><td>AS</td><td>SELECT ORGANIZATION_NAME, CONTROL_CLASS, RISK_CLASS, RISK#, RISK_DESCRIPTION, CONTROL#, CONTROL_DESCRIPTION CONTROL_STATE, CONTROL_RISK_RELATION</td></tr><tr><td>FROM</td><td>ENVIRONMENT_CONTROLS, ENVIRONMENTS, RISKS, CONTROLS, CONTROL_RISKS</td></tr><tr><td>WHERE</td><td>CONTROL_RISKS. CONTROL_# =</td></tr><tr><td>AND</td><td>ENVIRONMENT_CONTROLS. CONTROL_#</td></tr><tr><td>AND</td><td>RISKS.RISK_# = CONTROLS_RISKS.RISK_#</td></tr><tr><td>AND</td><td>ENVIRONMENT_CONTROLS. ORGANIZATION_# =</td></tr><tr><td>AND</td><td>ENVIRONMENTS. ORGANIZATION _#</td></tr><tr><td>AND</td><td>CONTROL_CLASS = Automated Application Controls</td></tr><tr><td>AND</td><td>ORGANIZATION_NAME = Daewoo Chemicals</td></tr></table>

Table 11 represents controls and their related risks. System Change Control by Authorization, which contains CONTROL a 101, is related, albeit negatively, to various risks. The effects of the control on these risks is indicated by the value of the field CONTROL RISK RELATION. When CON-TROL RISK RELATION is defined, the level of risk can be obtained from the level of controls in each company. The field CONTROL RISK RELA-<sub>– –</sub> TION can be shown as CONTROL<sub>– –</sub>a and RISK a are identified in Table 11. The ‘‘preliminary’’ risk level before the implementation of controls can be provided by using the values of both CONTROL<sub>–</sub> STATE and CONTROL RISK RELATION. The<sub>– –</sub> CONTROL STATE indicates the usage level of<sub>–</sub> controls; risk is negatively proportional to the value of this field. Hence, the value of CONTROL STATE is subtracted from 7, which indicates the amount of risk occurring from incomplete usage of the control. The subtracted value is multiplied by the ‘‘weight’’, i.e., the value of CONTROL RISK RELATION in the same tuple, and the weighted sum across tuples indicates the overall risk level. For example, CON-TROL a 101 has a CONTROL STATE of 2. Thus, 5 i.e., 7 minus 2 is multiplied by 6, which is theŽ . value of CONTROL RISK RELATION in the same<sub>– –</sub> tuple. The weighted sum is 96 for Table 11; this is then compared with other organizations to decide whether risk is high or low. Hence, it is possible to compare risk levels of organizations preliminarily by using a value of CONTROL STATE that is differ-<sub>–</sub> ent across organizations and CONTROL RISK RE-<sub>– –</sub> LATION field.

Some controls significantly decrease risks and provide significant insights into the selection of controls that are to be implemented from a cost–benefit

Table 10  
The recommended similar case

<table><tr><td>Control class</td><td>Average usage level of controls in Case 48</td></tr><tr><td>Internal formal application controls</td><td>3.75</td></tr><tr><td>Internal formal communication controls</td><td> $5^a$ </td></tr><tr><td>External formal VAN controls</td><td>4</td></tr><tr><td>External formal partner controls</td><td>4</td></tr><tr><td>Internal informal controls from risk recognition</td><td>4</td></tr><tr><td>Internal informal controls from sense of responsibility</td><td> $5^a$ </td></tr><tr><td>Internal informal controls from experience</td><td>4.75</td></tr><tr><td>Internal informal controls from interaction</td><td>3.5</td></tr><tr><td>External informal controls from risk recognition</td><td>4</td></tr><tr><td>External informal controls from sense of responsibility</td><td> $5^a$ </td></tr><tr><td>External informal controls from experience</td><td> $5^a$ </td></tr><tr><td>External informal controls from interaction</td><td> $5^a$ </td></tr><tr><td>Internal automated application controls</td><td>3.75</td></tr><tr><td>Internal automated communication controls</td><td>4</td></tr><tr><td>External automated VAN controls</td><td>4</td></tr><tr><td>External automated partner controls</td><td>2</td></tr></table>

<sup>a</sup> Higher or equal to than 5.Ž .

viewpoint. For example, the risks that can be significantly reduced by the introduction of the control CONTROL<sub>– –</sub>a 101 are RISK a s 101 and 106, as the CONTROL RISK RELATION of the control is<sub>– –</sub> valued as 6 and 7. Because these controls are perceived to increase the overall reliability of the system, these controls should of course be implemented.

Suggestions on test results of controls can help EDI auditors to evaluate whether to further implement EDI controls. The test results of controls for a specific organization can be determined by joining intersection tables. For example, if EDI auditors want to obtain the test procedures and results of the control class for the Automated Application Controls of Samsung Electronics, they can determine the test results of the Automated Application Controls of Samsung Electronics by joining the ENVIRON-

Table 11  
Relevant risks of the recommended controls

<table><tr><td>Control_#</td><td>Risk_#</td><td>Control_state</td><td>Risk_class</td><td>Risk_description</td><td>Control_risk_relation</td></tr><tr><td>101</td><td>101</td><td>2</td><td>risk of application</td><td>Data files are inaccurately processed</td><td>6</td></tr><tr><td>101</td><td>103</td><td>4</td><td>risk of application</td><td>Programs are changed without authorization</td><td>5</td></tr><tr><td>101</td><td>105</td><td>1</td><td>risk of application</td><td>System performance is greatly decreased by the frequent system failures</td><td>4</td></tr><tr><td>101</td><td>106</td><td>5</td><td>risk of application</td><td>unauthorized input</td><td>7</td></tr><tr><td>101</td><td>201</td><td>4</td><td>risk of communication</td><td>Internal users may abuse systems for their private purpose</td><td>3</td></tr><tr><td>101</td><td>204</td><td>3</td><td>risk of communication</td><td>Organization can not recover from errors within appropriate times</td><td>1</td></tr><tr><td>101</td><td>301</td><td>7</td><td>risk of VAN</td><td>Duplicated, omitted or inaccurate messages are delivered and received</td><td>4</td></tr></table>

MENTS, CONTROL TESTS, ENVIRONMENT TESTS, and CONTROLS tables. They must then select the tuple of joined tables in which the ORGA-NIZATION NAME is<sub>–</sub> Samsung Electronics and the CONTROL CLASS is <sub>–</sub> Automated Application Controls. These operations can be expressed as follows:

<table><tr><td>CREATE</td><td>VIEW</td><td>ORGANIZATION_RESULTS</td></tr><tr><td>AS</td><td>SELECT</td><td>ORGANIZATION_NAME, CONTROL_CLASS, CONTROL#,CONTROL_DESCRIPTION, TEST_DESCRIPTION,RESULT_DESCRIPTION, TEST_DATE</td></tr><tr><td></td><td>FROM</td><td>CONTROL_TESTS, ENVIRONMENT_TESTS, ENVIRONMENTS,CONTROLS</td></tr><tr><td></td><td>WHERE</td><td>CONTROL_TESTS.TEST_# =</td></tr><tr><td></td><td>AND</td><td>ENVIRONMENT_TESTS.TEST_#</td></tr><tr><td></td><td>AND</td><td>ENVIRONMENT_TESTS. ORGANIZATION_#</td></tr><tr><td></td><td>AND</td><td>ENVIRONMENTS. ORGANIZATION_#</td></tr><tr><td></td><td>AND</td><td>CONTROL_TESTS. CONTROL_# = CONTROLS. CONTROL_#</td></tr><tr><td></td><td>AND</td><td>ORGANIZATION_NAME = Samsung</td></tr><tr><td></td><td>AND</td><td>CONTROL_CLASS = AUTOMATED APPLICATION CONTROLS</td></tr></table>

These test procedures and results can then be displayed as a table by using a view see Table 12Ž for our example . This shows the results of applying. various tests to CONTROL<sub>–</sub>a 101. When test procedures and results are suggested by EDI controls, and also recommended for each individual control, EDI auditors can better recognize the extent of any problems in their current control system.

TEST RESULT can give insights influencing the<sub>–</sub> decision whether to implement specific EDI controls.

EDI auditors also must concentrate on those that are not appropriately implemented according to test results. TEST RESULT values of controls that are<sub>–</sub> either ‘Very Bad’ or ‘Bad’ should be examined. Auditors need to judge the importance of these controls for their organizations from a cost–benefit perspective, and then make a final decision whether to use them. On the other hand, if the test results of specific EDI controls are good i.e., when snap shotŽ or code comparison is applied , the further use of.

Table 12  
Test procedures and results of the controls

<table><tr><td>Control_#</td><td>Test_description</td><td>Test_result</td></tr><tr><td>101</td><td>Utility Software such as Flow charter Execution path Analyzer</td><td>Good</td></tr><tr><td>101</td><td>Code Review</td><td>Bad</td></tr><tr><td>101</td><td>Review File</td><td>Moderately Good</td></tr><tr><td>101</td><td>Snapshot</td><td>Very Bad</td></tr><tr><td>101</td><td>Generalized Audit Software</td><td>Moderate</td></tr><tr><td>101</td><td>Code Comparison</td><td>Very Good</td></tr><tr><td>101</td><td>Integrated Test Facility</td><td>Moderate</td></tr></table>

these controls should be discouraged, because they are already properly functioning.

## 7. Conclusion

EDIRDB has been developed to support EDI auditors in finding the controls that fit a specific firm within a certain environmental context, and to suggest possible risks and further test procedures. The reasoning process for EDI auditors is inevitably subject to human cognitive limitations and bias; and being human, their memories are variable and finite. They, therefore, cannot be completely consistent in searching for relevant experiences, interpreting them, or applying them to problem-solving. Using EDIRDB, controls are recommended using the database’s control procedures along with a company’s own environmental information. This system does improve the efficiency and effectiveness of EDI auditing, and can be further applied to general EDP auditing.

EDI auditors can identify critical controls through our systematic analysis of similar cases. Controls are critical if they are highly implemented in cases that are environmentally similar and result in high system performance. A relational database system is employed to aid the EDI auditors in retrieving relevant risks and test procedures. The controls should both be effective in reducing risks and lead to high performance. Controls that can significantly decrease the level of risks are recommended. Further, because controls demand appropriate test procedures to examine whether they have been successfully implemented, it is therefore critical to suggest further test procedures relevant to those new controls.

As the number of cases increases, it becomes more important to manage various entities and their relations. EDIRDB is designed to help EDI auditors manage a database of controls, risks, and test procedures and then store new information such as theŽ level of controls, risks, and test results . This data . can be stored in the form of relational tables for later reference. The relations among the various tables can be tapped using relational algebra such as JOIN PROJECTION, and SELECT to provide specific information that is useful to EDI auditors. Various other tables built from the nine base tables can also provide useful insights into the interpretation and justification of controls before they are tried out in the real world.

In our paper, an illustrative example has been provided to show the decision-support process in EDI auditing. A new case is entered into the system and a set of similar cases are retrieved by the system. A set of controls having high performance values are recommended. Risks and test procedures are selected by joining the tables ENVIRONMENTS, CON-TROLS, RISKS, and TESTS. The information about the state of risks along with the test results have been the basis for the evaluation of controls and the recommendation for further controls.

EDIRDB may serve both internal and external auditors. Both internal and external EDI auditors are charged with the responsibility of expressing an opinion on the integrity and security of EDI. Internal IS auditors, however, may participate in the design phase of IS and design appropriate controls for system effectiveness. Internal auditors are concerned, furthermore, with whether the choice of controls is optimal from a cost–benefit point of view, while external auditors focus on the causes of loss relating to violation of data integrity and lack of safeguards over assets from a detached, objective viewpoint <sup>w</sup> <sup>x</sup> 33 . EDIRDB may help internal auditors design appropriate EDI controls that are related to EDI performance in view of organizational context. EDIRDB also supports external auditors evaluating EDI controls, locating the ‘‘important’’ controls, and investing their limited audit resources to assess whether these controls are appropriate.

This system may also be applied to general IS auditing. The fundamental database structure of four entities need not be changed. The data for the attributes of EDIRDB, however, may be different when EDIRDB is applied to other IS. For example, the table CONTROLS, RISKS, TESTS, representing the control procedures, risks, and test procedures of EDI should be replaced with the new ones when they are applied to other IS. For instance, the controls of client<sup>r</sup>server systems need not include external controls that pertain to interactions with VAN providers and trading partners; they should encompass the management procedures of server and client systems. The intersection tables should also be changed and the data replaced with new information, as the rela-

tions among these tables cannot be the same. For example, in the context of client<sup>r</sup>server system, the risk from the failure of communication controls between client and server systems is high, and CON-TROL RISK RELATION in CONTROL RISKS table should be adjusted accordingly.

## Appendix A. Questionnaire items

## 1. INDUSTRY table

Ž . Ž . 1 External Pressure EXTERNAL INFLUENCES <sub>–</sub>

1 Our company had a lot pressure from trading partners to implement EDI. .

2 Our company had a lot pressure from government or industry associations to implement. .

Ž . Ž . 2 Technological Change TECHNOLOGICAL CHANGE <sub>–</sub>

1 There exists a frequent change in hardware and software for EDI technology. .

## 2. IS table

Ž . Ž . 1 size SIZE

1 Total number of employees .

2 Total Sales .

Ž . Ž . 2 Professionalism PROFESSIONALISM

1 The proportion of IS staff that has a master’s or Ph.D. degree in communication or computer science is high. .

Ž . Ž . 3 Decentralization DECENTRALIZATION

1 Participation of subordinates in company decision making is encouraged. .

2 Subordinates have enough authority to make their own decisions..

3 Management has exclusive authority to make decisions related to entire organization. .

Ž . Ž . 4 Managerial Attitude MANAGERIAL ATTITUDE<sub>–</sub>

1 Top management is willing to accept changes in organizational structure or process to implement. IT successfully.

2 Top management is willing to absorb technology, hardware, and software, with which the organization . is not familiar.

3 Top management is willing to commit large investment to new applications and network design. .

Ž . Ž . 5 IS Sophistication SOPHISTICATION

1 Steering committee exerts strong control over IS development and operation. .

2 Users actively involve with the IS development process. .

3 The number of IS staff excluding data entry personnel . Ž .

4 The amount the annual budget for IS function excluding wages . Ž .

5 The proportion % of administrative or decision support systems to aid strategic planning among . Ž . total application systems

6 The proportion % of total IS budge allocated for management controls and strategic planning . Ž . among total IS budgets

Ž . Ž .6 Present Role of IS PRESENT ROLE OF IS

1 Our systems can no longer operate if computer center is down. .

2 The functions of IS systems can be replaced by manual processing..

3 IS function develops systems for cost reductions and productivity improvement. .

Ž . Ž . 7 Future Role of IS FUTURE ROLE OF IS

1 IS function always develops systems to provide new ways to compete in business. .

2 IS function always studies the impact of new IS technologies and areas of application..

3 IS function develops applications that are vital for long-term strategic objectives. .

## Ž . Ž . 8 Communication Openness COMMUNICATION OPENNESS <sub>–</sub>

1 IS members can easily obtain information about EDI technologies from their colleagues or . by participating in seminars.

Select five tasks A, B, C, D, E that are most closely connected with EDIŽ .

Examples of tasks:

Import<sup>r</sup>Export Authorization, Import License Open, Master License Open, Local License Open,

Exchange<sup>r</sup>Negotiation, Tariff, Sending Order, Receiving Order, Production, Transportation,

Shipment<sup>r</sup>Inventory, Firm Banking, Sending Bill, Cash Management System, Cash Transfer

Insurance Engagement, Credit Card Usage Recording

## 3. TASK table

Ž . Ž . 1 Task Interdependence TASK INTERDEPENDENCE <sub>–</sub>

Ž . Ž . 2 Task routineness TASK ROUTINENESS<sub>–</sub>

1 Average repetitiveness and regularity are high in processing tasks .

## 4. PARTNER table

Ž . Ž .1 Partner Trust PARTNER TRUST

1 Our company highly trusts the representative trading partner while processing EDI tasks. .

2 Our company trusts in the benefits of the representative trading partner’s decision. .

3 Our company expects a fair deal from the representative trading partners’ .

Ž . Ž . 2 Partner Interdependence PARTNER INTERDEPENDENCE <sub>–</sub>

1 The possibility of changing the representative trading partner with others by our company is high. .

2 The possibility of changing our company with others by the representative trading partner is high. .

Ž . Ž . 3 Partner Commitment PARTNER COMMITMENT <sub>–</sub>

1 Our company strongly wants to continue the relationship with the representative trading partner. .

2 The representative trading partner strongly wants to continue the relationship with our company. .

## 5. PERFORMANCE table

Ž . Ž . 1 Improved Relation IMPROVED RELATION <sub>–</sub>

1 Relations with the representative trading partner are greatly improved through reduced response . time after adopting EDI.

2 Our company maintains improved relations with the representative trading partner by reducing . delay from errors.

3 Our company improved trust in relations with the representative trading partner by enhancing. confidentiality of documents

4 Relations with the representative trading partner are greatly improved by reducing omission and . inaccurate transmission.

5 Our company maintains high trust with the representative trading partner by protecting messages . from disclosure to unauthorized third party.

Ž . Ž . 2 Competitive Advantage COMPETITIVE ADVANTAGE . <sub>–</sub>

1 The efficiency of interdepartmental transaction processing is greatly increased. .

2 Accuracy is greatly improved by reduced paperwork..

3 Transaction processing costs are greatly reduce after adopting EDI..

## 6. CONTROLS table

The candidate values of CONTROL DESCRIPTION are presented for each of control class <sub>–</sub> Ž . CONTROL CLASS .<sub>–</sub>

Ž . 1 Internal Formal Application Controls

1 Systems are changed only through authorization from the responsible managers. .

2 Integrity check of messages is strictly performed before the messages are processed in the application. .

3 Audit trails of transactions are always maintained for correction of errors and contingency planning..

4 System login is appropriately controlled by access control procedures such as passwords..

Ž . 2 Internal Formal Application Controls

1 EDI messages are checked for duplication, omission or inaccuracy after they are generated . and before transmitting the messages.

2 The sender, receiver, and contents of EDI messages are appropriately authenticated after. the messages are generated or received.

Ž . 3 External Formal VAN Controls

1 VAN service providers have an appropriate contingency plan for network failures. .

2 VAN service providers retransmit messages if the messages are omitted, duplicated, or inaccurate. .

3 VAN service provider maintains audit trails for recovery of inaccurate messages.

4 VAN service provider controls unauthorized access and dial login to network..

5 VAN service provider controls unauthorized access to mailbox by internal staff..

Ž . 4 External Formal Partner Controls

1 The representative trading partner has an appropriate contingency plan for network failures. .

2 The representative trading partner retransmits messages if they are omitted, duplicated, or inaccurate. .

3 The representative trading partner maintains audit trails for the recovery of inaccurate messages. .

4 The representative trading partner controls unauthorized access and dial login to network. .

Ž . 5 Internal Informal Controls by EDI Staffs

1 EDI staff clearly recognizes the risks of the possible propagation of errors from one system to another..

2 EDI staff clearly recognizes the importance of their responsibility for the performance of EDI system. .

3 EDI staff can evaluate tasks of colleagues to see whether they are incorrect..

4 EDI staff can cope with errors in EDI messages using their own experience. .

5 EDI staff frequently cooperates with colleagues to assist in correcting errors. .

Ž . 6 Internal Informal Controls by Users

1 Users who process EDI messages clearly recognize the risks of possible propagation of . errors from one system to another.

2 Users who process EDI messages clearly recognize the importance of their responsibility for the. performance of EDI system.

3 Users who process EDI messages can evaluate tasks of colleagues to see whether they are incorrect. .

4 Users who process EDI messages can cope with errors in EDI messages using their own experience. .

5 Users who process EDI messages frequently cooperate with their colleagues to assist in correcting errors. .

Ž . 7 External Informal VAN Controls

1 EDI staff clearly recognizes that errors of the VAN can seriously affect our system. .

2 EDI staff clearly recognizes that the active participation of the VAN service provider is necessary . for successful EDI implementation.

3 EDI staff has extensive experience in successfully processing errors with the cooperation of the . VAN service provider.

4 EDI staff knows which items among contracts with the VAN service provider should be applied . in communicating messages strictly.

5 EDI staff processes their tasks by actively communicating information to their counterparts . in the VAN service provider.

Ž . 8 External Informal Partner Controls

1 EDI staff clearly recognizes that errors of the system of the representative trading partner can seriously . affect our system.

2 EDI staff clearly recognizes that the active participation of the representative trading partner is necessary . for successful EDI implementation.

3 EDI staff has extensive experience in processing errors successfully with the cooperation . of the representative trading partner.

4 EDI staff knows through experience which items among contracts with the representative trading . partner should be strictly applied in communicating messages.

5 EDI staff processes their tasks by actively communicating information to their counterparts . in the representative trading partner.

Ž . 9 Internal Automated Application Controls

1 Automated integrity check of data fields is performed using embedded software before received messages . are processed in internal applications.

2 Access to sensitive files and programs is effectively controlled using access controls software. .

Ž . 10 Internal Automated Communication Controls

1 Embedded software is effectively used to automatically check accuracy of messages received. .

2 Automated authentication procedures effectively ascertain the identity of sources or destination before. sending and after receiving messages.

Ž . 11 External Automated VAN Controls

1 The VAN service provider automatically records messages for the correction of errors.

and retransmission of corrected messages.

2 The VAN service provider automatically tracks and reports the status of message communication..

3 The VAN service provider attaches message identification codes or digital signatures to effectively . authenticate the messages.

4 The VAN service provider supports connections with diverse environment .

through various protocol conversion services.

5 The VAN service provider supports connections with diverse environments through providing. various message standards.

Ž . 12 External Automated Partner Controls

1 The representative trading partner automatically records messages for the correction of errors . and retransmission of corrected messages.

2 The representative trading partner automatically tracks and reports the status of message communication. .

3 The representative trading partner attaches message identification codes or digital signatures to effectively . authenticate the messages.

## References

<sup>w</sup> <sup>x</sup> 1 A.D. Bailey, L.D. Gordon, J.H. Gerlach, C. Ko, R.D. Meservy, A.B. Whinston, TICOM and the analysis of internal controls, The Accounting Review 1985 186–201, April.Ž .

<sup>w</sup> <sup>x</sup> 2 S. Banerjee, D.Y. Golhar, Electronic data interchange: characteristics of users and nonusers, Information and Management 26 1994 65–74.Ž .

<sup>w</sup> <sup>x</sup> 3 D.C. Burns, J.K. Loebbecke, Internal control evaluation: how the computer can help, Journal of Accountancy 1975 60–70,Ž . August.

<sup>w</sup> <sup>x</sup>4 S. Chan, M. Govindan, J.Y. Picard, E. Leschiutta, EDI for Managers and Auditors, Electronic Data Interchange Council of Canada, Toronto, Ontario, 1993.

<sup>w</sup> <sup>x</sup> 5 P.P. Chen, The entity–relationship model – toward a unified view of data, ACM TODS 1 1 1976 March.Ž . Ž .

<sup>w</sup> <sup>x</sup> 6 P.P. Chen, in: M. Stonebraker Ed. , Readings in DatabaseŽ . Systems, Morgan Kaufmann, San Marteo, Calif., 1988.

<sup>w</sup> <sup>x</sup> 7 L.R. Daft, R.M. Steers, Organizations: A Micro<sup>r</sup>Macro Approach, Scott, Foresman, 1986.

<sup>w</sup> <sup>x</sup> 8 C.J. Date, An Introduction to Database Systems, Addison-Wesley Publishing, 1990.

<sup>w</sup> <sup>x</sup> 9 C. Dell’Aquila, E. Lefons, F. Tangorra, L. Colazzo, Architecture of a relational decision support system, Decision Support Systems 5 1989 65–78.Ž .

<sup>w</sup> <sup>x</sup> 10 E.L. Denna, J.V. Hansen, R.D. Meservy, L.E. Wood, Casebased reasoning and risk assessment in audit judgment, International Journal of Intelligent Systems in Accounting, Finance and Management 1 3 1992 163–171.Ž . Ž .

<sup>w</sup> <sup>x</sup> 11 Gal, G., 1985. Using knowledge to formulate data model constraints: Expert systems for internal control evaluation, Ph.D. Dissertation, Michigan State University, East Lansing, MI.

<sup>w</sup> <sup>x</sup> 12 B.J. Garner, J. Pinnis, Modeling as an audit technique, Australian Computer Journal 1984 48–53, May.Ž .

<sup>w</sup> <sup>x</sup> 13 B.J. Garner, E. Tsui, Recent advances in computer audit approach, EDP Journal 4 1985 3–16.Ž .

14 J.V. Hansen, W.F. Messier, A relational approach to decision support in EDP auditing, in: Communication of the ACM,1984, pp. 1129–1133, November.

<sup>w</sup> <sup>x</sup> 15 J.V. Hansen, W.F. Messier, A preliminary investigation of EDP-XPERT, Auditing: A Journal of Practice and Theory Ž .1986 109–123, Fall.

<sup>w</sup> <sup>x</sup> 16 D.J. Hickson, D.S. Pugh, D.C. Pheysey, Operations technology and organization structure: an empirical reappraisal, Administrative Science Quarterly 14 1 1969 378–397.Ž . Ž .

<sup>w</sup> <sup>x</sup>17 ISACA, EDI Control Guide, Information Systems Audit and Control Association, EDI Council of Australia, Sydney, 1990, Chapter.

<sup>w</sup> <sup>x</sup> 18 R. Jamieson, EDI: An Audit Approach, The EDP Auditors Foundation, Rolling Meadows, IL, 1994.

<sup>w</sup> <sup>x</sup> 19 J. Kolodner, Case-Based Reasoning, Morgan Kaufmann, San Mateo, CA, 1993.

<sup>w</sup> <sup>x</sup> 20 S. Lee, I. Han, The design of EDI controls using case-based reasoning: EDICBR, International Journal of Intelligent Systems in Accounting, Finance and Management 7 3 1998Ž . Ž . 135–152.

<sup>w</sup> <sup>x</sup> 21 Lee, S., Han, I., 1998b. The impact of environmental variables on EDI controls, Working Paper, Korea Advanced Institute of Science and Technology.

<sup>w</sup> <sup>x</sup> 22 S. Lee, I. Han, H. Kym, The impact of EDI controls on EDI implementation, International Journal of Electronic Commerce 2 4 1998 71–98.Ž . Ž .

<sup>w</sup> <sup>x</sup> 23 J.A. Marcella, S. Chan, EDI Security, Control, and Audit, Artech House, Norwood, MA, 1993.

<sup>w</sup> <sup>x</sup> 24 R.D. Meservy, A.D. Bailey, P.E. Johnson, Internal control evaluation: a computational model of the review process, Auditing: A Journal of Practice and Theory 6 1 1986Ž . Ž . 44–74.

<sup>w</sup> <sup>x</sup> 25 B.W. Morris, SCAN: a case-based reasoning model for generating information system control recommendation, International Journal of Intelligent Systems in Accounting, Finance and Management 3 1 1994 47–63.Ž . Ž .

<sup>w</sup> <sup>x</sup>26 D. Murphy, C.E. Brown, The use of advanced information technology in audit planning, International Journal of Intelligent Systems in Accounting, Finance and Management 1 3Ž . Ž . 1992 187–193.

<sup>w</sup> <sup>x</sup> 27 C.K. Riesbeck, R.C. Schank, Inside Case-Based Reasoning, Erlbaum, Hillsdale, NJ, 1989.

<sup>w</sup> <sup>x</sup> 28 D.R. Russel, C.J. Russel, An examination of the effects of organizational norms, organizational structure, and environmental uncertainty on entrepreneurial strategy, Journal of Management 18 4 1992 639–656.Ž . Ž .

<sup>w</sup> <sup>x</sup> 29 P. Steinbart, The construction of a rule-based expert system as a method for studying materiality judgements, The Accounting Review 1987 97–116, January.Ž .

<sup>w</sup> <sup>x</sup> 30 D.W. Straub, Effective IS security: an empirical study, Information Systems Research 1 3 1992 255–276.Ž . Ž .

<sup>w</sup> <sup>x</sup> 31 E. Suh, H. Hinomoto, Use of a dialogbase for integrated relational decision support systems, Decision Support Systems 5 1989 277–286.Ž .

<sup>w</sup> <sup>x</sup> 32 R. Weber, Some characteristics of the free recall of computer controls by EDP auditors, Journal of Accounting Research 18 Ž . Ž . 1 1980 214–241, Spring.

<sup>w</sup> <sup>x</sup> 33 R. Weber, Information Systems Control and Audit, Prentice Hall, Upper Saddle River, NJ, 1999.

<sup>w</sup> <sup>x</sup> 34 J.W. Wilkinson, Accounting Information Systems: Essential Concepts and Applications, 2nd edn., John Wiley and Sons, 1993.

![](/api/attachments/U9QFUHZ7/fulltext/images/b1dd8cbbf30d4259358781d0ee8fb6a3935f3f7c0d4cd95e2ac522173ff926ca.jpg)  
Sangjae Lee is a researcher at Techno-Management Research Institute in Korea Advanced Institute of Science and Technology KAIST . He received hisŽ . PhD from KAIST in Management Information Systems. He is a certified information systems auditor CISA . His Ž . research interests include electronic commerce, IS control and audit, and decision support system in IS auditing.

![](/api/attachments/U9QFUHZ7/fulltext/images/e882e0b57036f77267e61bff991e9c23443515b1508c9845cf570fa83d73eff3.jpg)

Ingoo Han is an associate professor at the Graduate School of Management, Korea Advanced Institute of Science and Technology. He received his PhD from University of Illinois at Urbana-Champaign. His research interests are information systems audit and security, information system evaluation, and AI applications in accounting and finance. The recent research issues include the audit and control under electronic commerce, prediction of stock price using

neural network, and integration of AI techniques.
