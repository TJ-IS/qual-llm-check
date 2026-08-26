---
otero_id: 14396
otero_key: "NPRC7F7E"
title: "Efficiency analysis of controls in EDI applications"
authors: "Sangjae Lee; Kidong Lee; In Won Kang"
year: "2005"
journal: "Information & Management"
doi: "10.1016/j.im.2001.09.001"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Efficiency analysis of controls in EDI applications

Sangjae Lee<sup>a,\*</sup>, Kidong Lee<sup>b</sup>, In Won Kang<sup>c</sup>

<sup>a</sup>Department of E-business, College of Business Administration, Sejong University, 98 Kunja-dong, Kwangjin-gu, Seoul 143-747, South Korea <sup>b</sup>Department of Business Administration, University of Incheon, 177 Dowha-dong, Nam-ku, Incheon 402-749, South Korea <sup>c</sup>Sungkyun Management Research Institute, Sung Kyun Kwan University, Seoul 110-745, South Korea Received 1 January 2000; received in revised form 25 July 2000; accepted 15 September 2001 Available online 28 May 2004

## Abstract

The high penetration levels of electronic data interchange (EDI), a mechanism for inter-organizational electronic commerce, has revolutionized the way organizational conduct their business. Major benefits derived from EDI, however, depend upon the use of appropriate controls to overcome potential risks and exposures inherent in integrating and utilizing of the system. As many resources and skills are required for the implementation of EDI controls, their design should proceed carefully. This paper discusses a description of a data envelopment analysis (DEA) model for analysis of the controls for a specific context of electronic data interchange. A data envelopment analysis model to analyze the efficiency of controls in the context of finance and trade. The model uses eight variables of formal or automated EDI controls as input and four variables of EDI implementation and performance as output. Automated controls are more efficiently utilized in financial than in trade applications, while formal controls are more efficiently used in trade applications. Every company can determine the relative amount of reduction in each mode or component of controls in order to make the control system efficient.

Keywords: EDI; EDI controls; Data envelopment analysis (DEA); EDI implementation; EDI performance

## 1. Introduction

Electronic data interchange (EDI) is an interorganizational electronic communication method that allows standard computer-to-computer exchange of inter-company transaction documents and information. Security and integrity controls were included as the factors that affect the attainment of EDI implementation success and advantages [3,15]. This paper therefore extends EDI research by examining the efficiency of the controls for its implementation and performance.

Effective controls are needed to protect other parties from errors or deliberate sabotage, or to protect recipient applications from intentional or unintentional errors in the systems [19]. Further, if the processes (e.g., workflow or message protocol) are not standardized, it is difficult to link to other EDI adopters. Security and control issues are impediments to such implementation especially when third parties, such as service bureaus, are involved. EDI adopters need to select the VANs and subscribers that can provide basic control functions and accept standard procedures [13]. EDI adopters will implement EDI further if its benefits exceed its costs.

Hence, controls are a prerequisite for EDI implementation success.

Customer service is improved by avoiding extra paperwork and data re-entry by the recipient partner organization. The speed, accuracy, and completeness of partner communications can increase from standardization and formalization of the communication process and procedures [23]. The communications transport protocols (e.g., SDLC, ASC, BISYNC) indicate the method by which a message is sent. The message format contains both the data and identification and routing details. Interchange control segments indicate a set of documents transmitted between organizations [22]. Such structured and routine processes enable the coordination of transmission between sending and receiving organizations, increasing the accuracy and speed of the EDI process.

The implementation of controls should be in line with the level of risk the organization is willing to accept [18]. Given the high cost and resources needed to develop and maintain controls for sophisticated system [1,14], it is necessary to analyze the efficiency of EDI control systems. There has not, however, been a single investigation into the efficiency of controls for the implementation of EDI system. This paper gives a description of EDIDEA (EDI-controls efficiency analysis using data envelopment analysis (DEA)), a data envelopment analysis model for efficiency analysis of EDI controls. DEA, first proposed by Charnes et al. [7], is now widely used in analysis of many decisional entities in public and private sectors. The purpose of this study is to provide a normative approach toward diagnosing the efficiency of an EDI application. This study classifies EDI application into two parts; financial (e.g., firm banking, cash management system, cash transfer (electronic funds transfer)) and trade applications (e.g., import/export authorization, import license open, master license open, local license open, exchange/negotiation, tariff) [25].

## 2. Method

The main data collection method was structured interviews of respondents from EDI adopters. Since all of the control items were newly developed and their description is quite lengthy, it was important to know whether the questions could be appropriately answered by EDI practitioners. Further, some questions could require the release of sensitive information about security and data integrity issues. These questions can be better answered by a structured interview than any other data collection method. One or two members of the EDI staff or management took part in the interview. They were believed to have sufficient knowledge about their implementation. The data was collected as part of a larger investigation concerning EDI controls.

Target respondents were selected as follows. First, industries that used EDI were identified. From publicly available company databases (through the Chollian network service), companies were contacted to check their level of EDI implementation. Respondents were assumed to possess the level of knowledge needed to answer the questions. A total of 110 responses comprised the final usable sample. The unit of analysis was individual EDI adopting company. The full questionnaire for variables is shown in the Appendix A.

One of goal of this study was to analyze the difference in control efficiency between financial and trade applications. The 110 firms were divided into four groups depending on their financial and trade applications. The number of EDI adopters in each group is shown in Table 1. Eight EDI adopters implement both financial and trade applications. These eight firms as well as six firms that have not implemented neither of the two applications are excluded from further investigation in order to examine the difference between financial and trade applications.

The total number of firms in the sample was 41 financial EDI applications and 39 trade applications. DMU is an individual EDI adopter. They consist of companies that have a relatively high level of implementation and performance. The relatively high extent of their implementation allows the respondents to have sufficient knowledge to answer the questionnaire. From these, the efficient level of controls that must be followed by other companies can be assessed. However, a ‘‘diversity’’ of samples was also pursued; users of various VANs were included in the sample to ensure external validity of the study, as the strength of the controls varies across VANs. The distribution of VANs is shown in Table 2.

Table 1 EDI controls in this study

<table><tr><td>Control class</td><td>Subclass</td><td>Modes of controls</td><td>Description</td></tr><tr><td rowspan="4">Formal controls</td><td rowspan="2">Internal formal controls</td><td>Internal formal application controls</td><td>Procedures used to protect internal applications from errors and unauthorized access</td></tr><tr><td>Internal formal communication controls</td><td>Procedures used to ensure that the generation and receipt of message are accurate and secure</td></tr><tr><td rowspan="2">External formal controls</td><td>External formal VAN controls</td><td>Procedures used by VAN service providers to ensure security and integrity of communication</td></tr><tr><td>External formal partner controls</td><td>Procedures used by trading partners to ensure security and integrity of communication</td></tr><tr><td rowspan="4">Automated controls</td><td rowspan="2">Internal automated controls</td><td>Internal automated application controls</td><td>Automated routines used to detect and correct errors during input, process, and output of data</td></tr><tr><td>Internal automated communication controls</td><td>Automated routines used to control access and authenticate users during generation and receipt of messages</td></tr><tr><td rowspan="2">External automated controls</td><td>External automated controls by VAN</td><td>Automated control measures for system integrity and security that are provided by VAN service providers for system integrity and security</td></tr><tr><td>External automated controls by trading partners</td><td>Automated control measures for system integrity and security that are provided by trading partners for system integrity and security</td></tr></table>

## 3. Analysis

Data envelopment analysis was used to analyze the efficiency of the EDI controls. Specifically, the study used radial improvement and constant returns as the means to scale the DEA model of Charnes, Cooper, and Rhodes (CCR) [7]. This model attempts to provide a radial improvement in both inputs and outputs. Warwick-DEA software by Thanassoulis and Emrouznejad [26] was used to code the DEA model in the PC version.

DEA is a methodology based on mathematical programming that produces the relative efficiency of decision making units (DMUs) (e.g., individuals, organizational units). DEA optimizes on each individual observation provides a discrete piecewise frontier that represents the set of Pareto-efficient DMUs. DEA optimizes the performance measure of each DMU and focuses on individual observations, while the same estimated equation is assumed to apply to each DMU in parametric analysis (e.g., regression analysis, discriminant analysis). Thus, DEA provides an optima performance measure for each DMU relative to all other DMUs in the sample data. The DEA is used in a wide range of contexts, such as education (universities) [28], banking [8], health care (hospitals, clinics)

[5,9], and software projects [17]. A typical example is an investigation of organizations, such as a university department with various inputs, such as the number of staff or professors, the number of book in the library, and the number of computers, and outputs such as the number of publications produced, the number of Ph.D. students who graduate, and the number of consultancy money obtained. The purpose of DEA analysis is then to examine efficiency of the university department in transforming its inputs into outputs.

DEA is used for several reasons. First, any functional form relating the input to output variables need not be imposed. The parametric approach, such as regression equation and discriminant analysis, however, demands specific assumptions about the functional form and the distribution of error terms (e.g., independently or normally distributed). The only requirement of DEA is that each DMU lie on or below the extremal frontier. Those DMUs not on the frontier are scaled against a convex combination of the DMUs on the frontier facet closest to them. Second, multiple inputs and multiple outputs may be considered. Charnes, Cooper, and Rhodes developed the CCR model that converts the multiple output/input characterization of each DMU into that of a single ‘‘virtual’’ output and ‘‘virtual’’ input. Third, the inefficiency of each configuration of controls is provided. For each of the inputs and outputs, the inefficiency of the DMUs that lie below the frontier is given. This inefficiency may be determined from comparison with a single referent DMU (or a convex combination of other DMUs) that lies on the frontier and has the same level of inputs and a greater level of outputs. The amount of increase in outputs (or decrease in inputs) shows potential improvements of the inefficient DMUs without worsening the other inputs or outputs. Last, the sources of inefficiency may be identified to provide a direction for EDI control design. DEA can be used as a method for relating efficiency outcomes to features of organizational design [16] (EDI controls design here). The sources of relative inefficiency can be identified by EDIDEA. The internal auditors should be especially interested in identifying the specific mode or component of controls that adversely affect EDI implementation or performance. Efficiency of EDI systems can be increased by reducing the use of inefficient controls and selecting the resource-minimizing mix.

T<sub>a</sub>bl<sub>e</sub> 2 I<sub>npu</sub>t <sub>an</sub>d <sub>ou</sub>t<sub>pu</sub>t <sub>var</sub>i<sub>a</sub>bl<sub>es</sub>

<table><tr><td>Input or output</td><td>Subclass</td><td>Variables (Cronbach alpha)</td><td>Items</td><td>Sources</td></tr><tr><td rowspan="7">Input</td><td rowspan="2">Internal formal controls</td><td>Internal formal application controls (alpha = 0.710)</td><td>System change control by authorization (FC1)Integrity check of the message before processing in the application (FC2)Transaction log for the possible errors and collapse (FC3)Appropriate system login procedures using password (FC4)</td><td rowspan="7">[6,11,12,18]</td></tr><tr><td>Internal formal communication controls (alpha = 0.791)</td><td>Integrity check after generating EDI messages (FC5)Authentication of trading partners after receiving EDI messages (FC6)</td></tr><tr><td rowspan="2">External formal controls</td><td>External formal VAN controls (alpha = 0.861)</td><td>Back up and recovery plan by VAN (FC7)Retransmission after correcting erratic messages by VAN (FC8)Dispute reconciliation procedures by VAN (FC9)Access control on network by VAN (FC10)Mailbox access control by VAN (FC11)</td></tr><tr><td>External formal partner controls (alpha = 0.783)</td><td>Back up and recovery plan by trading partners (FC12)Retransmission after correcting erratic messages by trading partners (FC13)Dispute reconciliation procedures by trading partners (FC14)Access control on network by trading partners (FC15)</td></tr><tr><td>Internal automated controls</td><td>Internal automated application controls (NA)Internal automated communication controls (alpha = 0.718)</td><td>Programmed integrity check before processing in application systems (AC1)Automated data integrity check before transmission of EDI messages (AC2)Automated authentication of trading partners using message code (AC3)</td></tr><tr><td rowspan="2">External automated controls</td><td>External automated controls by VAN (alpha = 0.777)</td><td>Automated transaction log for EDI messages by VAN (AC4)Error message tracing and error reporting by VAN (AC5)Digital signatures(message authentication code) provided by VAN (AC6)</td></tr><tr><td>External automated controls by trading partners (alpha = 0.667)</td><td>Automated transaction log for EDI messages by trading partners (AC7)Error message tracing and error reporting by trading partners (AC8)Digital signatures(message authentication code) provided by trading partners (AC9)</td></tr><tr><td rowspan="3">Output</td><td>Implementation</td><td>Integration (NA) Utilization (NA)</td><td>Integration of EDI in five application systems Utilization of EDI in five application systems</td><td>[21]</td></tr><tr><td rowspan="2">Performance</td><td>Improved relations (alpha = 0.891)</td><td>Improvement of relationship by reduction response time (REL-1) Improvement of relationship by reduction of delay from errors (REL-2) Improvement of trust by enhanced authentication of message contents (REL-3) Improvement of relationship by reduction of omission or inaccuracy in transmission (REL-4) Maintenance of trust by protection of messages from modification by third parties (REL-5)</td><td>[2,10]</td></tr><tr><td>Influence on productivity (alpha = 0.868)</td><td>Increase in efficiency of interdepartmental transaction processing (ADV-1) Increase in accuracy by reduction of paper work (ADV-2) Reduction of transaction processing costs (ADV-3)</td><td></td></tr></table>

NA<sub>:</sub> B<sub>ecause</sub> th<sub>e var</sub>i<sub>a</sub>bl<sub>e</sub> i<sub>s compose</sub>d <sub>o</sub>f <sub>a s</sub>i<sub>ng</sub>l<sub>e</sub> it<sub>em no re</sub>li<sub>a</sub>bilit<sub>y an</sub>d <sub>va</sub>lidit<sub>y ana</sub>l<sub>ys</sub>i<sub>s</sub> i<sub>s con</sub>d<sub>uc</sub>t<sub>e</sub>d.

The ratio of a weighted sum of outputs to a weighted sum of inputs of each DMU must not exceed one, and this number indicates the relative technical efficiency of any DMU. The weights for both outputs and inputs are optimally determined in a manner that calculates the Pareto efficiency measure of each DMU. The relative efficiency is computed in relation to all the other DMUs after a piecewise extremal surface, which indicates the maximum output empirically obtainable given some level of inputs, is determined using the actual data values for the outputs and inputs.

## 3.1. Input of EDIDEA

EDI controls are defined here as activities to safeguard assets, maintain data integrity, accomplish organizational goals effectively, and consume resources efficiently [27]. The objective of EDI controls is to ensure that an organization achieves its goals through EDI.

As the implementation of system proceeds, tracking and control mechanisms are necessary to ensure the continuity of EDI services as the transaction volume and the speed of processing increases and human intervention is reduced [10,11]. Communication controls migrate from being managed by humans to being managed by computerized programs when internal applications are linked to external partners.

‘‘Control assurance’’ should be provided to various stakeholders, including internal users, trading partners, and any industry association, as well as user departments, before the decisions regarding further implementation can be made. This assurance can take the form of contractual obligations or agreements. If insufficient security is provided, manual work should be done [20]. If the candidate tasks (to be computerized) are done safely manually, reduction of risk is likely. In the case of inter-organizational system (IOS), companies, especially influential ones, demand trading partners to establish an ‘‘adequate’’ level of controls, specified in trading partner agreements, before connecting their system to trading partners’ systems [12]. For example, a retailer communicating its information with a manufacturer through IOS is creating a shared computing environment for marketing and manufacturing decisions. The manufacturers may have contractual obligations with their retailers about good logistics and transportation systems for the supply chain.

Major advantages and benefits derived from EDI include quick response to trading partners and improved accuracy from reduction of manual processing. EDI cannot be adopted and implemented if users are not sure about the advantages of the system. If EDI is used in payment transactions, minor errors in the communication of transactions can lead to severe degradation of system performance. Management should demand assurance that adequate controls are in place before they implement the EDI system.

EDI controls may be categorized into internal and external. Internal controls deal with internal components such as the application system interface, while external controls are involved with systems such as the VAN or trading partner. External controls are particularly important for EDI. Invalid or unauthorized transactions can be initiated by the staff in a thirdparty network. Messages could be lost, altered, duplicated, or transposed while being transmitted through the network.

In this study, controls were also classified into formality and automated. Formal controls are established by management and based on written procedures.

They have four modes. Automated controls indicate the degree to which procedures and methods are used to detect and correct errors during input, process, and output of data and ensure security and authentication software to protect the systems from unauthorized access and computer abuse. Formal controls are procedural and fundamental in that they delineate preventive, detective and corrective actions to address security issues across all systems. Automated controls also involve VANs and trading partners in protecting system integrity. Hence, there are also four modes of automated controls applied by the: application, communication, VAN, and trading partners.

Table 3  
Distribution of companies adopting EDI applications

<table><tr><td></td><td>Number of companies</td><td>Percentage (%)</td></tr><tr><td>Adopting financial applications only</td><td>41</td><td>37.3</td></tr><tr><td>Adopting trade applications only</td><td>39</td><td>35.5</td></tr><tr><td>Adopting both financial and trade applications</td><td>8</td><td>7.3</td></tr><tr><td>Adopting none</td><td>22</td><td>20</td></tr><tr><td>Total</td><td>110</td><td>100</td></tr></table>

Formal or automated controls are ‘‘visible’’ procedures or mechanisms to ensure system security and integrity. Informal controls are ‘‘invisible,’’ as they are enacted through values and beliefs of employees and inner communication and it is difficult to interpret their efficiency. Hence, this study deals with formal and automated controls. The conceptual definitions of eight modes of EDI controls are suggested in Table 3.

Measures for EDI controls are newly developed based on various sources [6] (see Table 4). The first version of measures of EDI controls was modified through an interview with 10 EDI practitioners (one from each company); they were cognizant of managerial and technical aspects of EDI controls. The wording, interpretation of the items, and the possession of knowledge necessary to answer the questionnaire were reviewed. The measures were modified after each interview. Four IS professors made a final review. Respondents answered the extent to which they agree or disagree with each statement about controls; e.g., ‘‘integrity check of messages is strictly performed before the messages are processed in the application’’ (item FC2). The answers were placed on a seven-point Likert-type scales (1 ¼ totally disagree, 7 ¼ totally agree). Average value was used for the multi-item measure. The data used in validating the research model was gathered as part of a larger investigation concerning EDI controls. EDIDEA uses eight variables for input variables; four variables for formal and automated controls, respectively. Only qualitative measures were used, as it is difficult to measure the use quantitatively. Respondents may have had different opinion regarding the extent to which controls exist. However, as they were senior informed respondents within the organizational unit responsible for managing the EDI systems, it was assumed that they responded from an organizational perspective. Further, face-to-face in-depth interviews were conducted with respondents to ensure that all of the questions and terms were clearly understood.

VAN of responding firms

<table><tr><td>VAN name</td><td>Number of responses</td><td>Percentage (%) (total 168 responses)</td></tr><tr><td>KTNET</td><td>57</td><td>33.9</td></tr><tr><td>DACOM</td><td>55</td><td>32.7</td></tr><tr><td>KLNET</td><td>13</td><td>7.7</td></tr><tr><td>Samsung-Net</td><td>12</td><td>7.2</td></tr><tr><td>LG-EDS NET</td><td>8</td><td>4.8</td></tr><tr><td>Hyundai-NET</td><td>3</td><td>1.7</td></tr><tr><td>POSDATA-NET</td><td>8</td><td>4.8</td></tr><tr><td>KICC</td><td>2</td><td>1.2</td></tr><tr><td>Others</td><td>10</td><td>6</td></tr><tr><td>Total</td><td>168</td><td>100</td></tr></table>

## 3.2. Output of EDIDEA

EDI implementation has two dimensions, integration and utilization. The key to effective use of EDI is to integrate information collected through EDI with internal IS applications so that effectiveness and efficiency of the operation may be improved. Better customer service and improved inter-firm relationships are possible, because customers’ needs can be promptly met. This is especially critical in just in time (JIT) production systems.

Integration is measured by the average level of integration of application systems that respondents selected [21]. The implementation of EDI applications at the organizational level can be represented by five tasks (import/export authorization, firm banking, cash management system, cash transfer) selected by respondents. If respondents have less than five applications, the integration (and utilization) levels are measured. Integration was specifically defined by the extent to which EDI data can be directly processed within these applications without human intervention. A seven-point Likert-type scale was used to measure integration.

Utilization of EDI indicates the extent to which an organization handles its business transactions electronically. Adoption and implementation of EDI may impose significant one-time costs on organizations as they adjust their internal systems in order to permit their trading partners to interface with the firm. EDI has to be extensively utilized while being integrated with internal applications. The utilization is measured by the average level that a company uses EDI in the five EDI applications that can be processed through other means. For instance, if EDI is used 80% in order processing, while fax or e-mail is used as a complementary means (i.e., in 20% of the cases), then utilization is 80%.

The expansion of electronic links and transaction sets/documents can be assessed by the extent of EDI utilization. Economies of scale are possible by expanding the access to many external firms.

The intended benefits to firms may not be provided from installed systems. Mere measurement of EDI integration and utilization may not be sufficient indicators of success. The measures for EDI performance are based on various EDI survey results [2] and EDI management and controls. The objectives of EDI usage can then be adapted to compose the measures of perceived EDI performance. The reinforcement of ties with a business partner, improved customer service, cost reduction, and increased reliability of information are the most important benefits of most respondents. There are two dimensions of EDI performance; improved relations and influence on productivity. The former means the reinforcement of ties with a business partner and improved customer service, while the latter is related to cost reduction and increased productivity of work processes.

Hence, EDIDEA uses four output variables (two variables each for EDI implementation and performance) in this study; integration, utilization, improved relations, and influence on productivity. The measures for the implementation and performance are shown in Table 4.

## 3.3. Results and discussion

Reliability and validity tests were performed for the collected data. The Cronbach’s alphas are shown in Table 4. All scales exceed 0.6, which shows moderate to high reliability. The content validity of the items was established through the adoption of constructs that have been validated by other researchers and a pretest with 10 IS professionals. Further, extensive precautions were taken during the previous stages of development and pilot testing of the items.

As a result of separate exploratory factor analysis, the items converged on appropriate variables, as originally envisaged. Based on the results on principal component analysis, the items that loaded on multiple constructs or had low item-to-construct loading (factor loading values lower than 0.5) were abandoned from further analysis. The results generally show that each item loaded higher on its associated variable, which confirm convergent and discriminant validity of measures.

EDIDEA enabled a series of analyses of the difference in the efficiency in various combinations of inputs and outputs and the amount of reduction needed in specific mode of controls. DEA identified efficient and inefficient EDI adopters when all eight variables of EDI controls and four variables of EDI implementation and performance were used. Separate efficiency analyses were applied for financial and trade applications. The percentage of efficient firms and average efficiency are presented in Table 5. There were slightly more efficient firms in financial applications than in trade applications. More EDI adopters use EDI controls efficiently in financial applications (i.e., trade applications).

Table 6 shows the number of efficient firms and average efficiency when specific classes of input and output variables were used. Input variables were divided into formal and automated controls, and each class had four variables. Output variables were categorized into EDI implementation (integration, utilization) and EDI performance (improved relations, influence on productivity). When formal controls were used, the number of efficient firms and average efficiency was higher in trade applications than in financial applications. However, the number was higher in financial applications than in trade applications when automated controls were used as input.

Table 5  
DEA efficiency results

<table><tr><td>Application</td><td>Financial applications</td><td>Trade applications</td></tr><tr><td>Number of efficient firms (%)</td><td>23 (56.1)</td><td>15 (38.5)</td></tr><tr><td>Number of inefficient firms (%)</td><td>18 (43.9)</td><td>24 (61.5)</td></tr><tr><td>Average efficiency of inefficient firms</td><td>0.923</td><td>0.902</td></tr></table>

Table 6  
Average efficiency in specific class of input and outputs (number in parenthesis indicates the number of efficient firms)

<table><tr><td rowspan="3">Input class</td><td colspan="4">Application</td></tr><tr><td colspan="2">Financial applications</td><td colspan="2">Trade applications</td></tr><tr><td> $Implementation^a$ </td><td> $Performance^a$ </td><td> $Implementation^a$ </td><td> $Performance^a$ </td></tr><tr><td>Formal controls</td><td>37.3 (2)</td><td>52.1 (3)</td><td>57.3 (5)</td><td>72.8 (4)</td></tr><tr><td>Automated controls</td><td>72.0 (7)</td><td>76.2 (11)</td><td>49.1 (5)</td><td>72.1 (7)</td></tr></table>

<sup>a</sup> Output class.

The average efficiencies were produced when specific variables of input and output were used (Table 7). As the statistical significance of the difference between applications needs to be shown, the average efficiencies were produced and the paired Wilkoxon test was performed to see whether average efficiency was different (Table 8).

These indicate that differences between financial and trade applications exist or are significant: automated controls were more efficiently utilized in financial than trade applications, while formal controls were more efficiently used in trade than financial applications. EDI adopters which adopt the applications in the same group may belong to the same industry and have similar environmental contexts.

EDI adopters in Korea depend more on automated controls of VANs or ‘‘hub’’ companies than on their own controls as the number of EDI documents and trading partners increase. This is more the case in financial application with strict standards of security and integrity needs. Firms even choose to replace their current automated controls with those provided by VAN.

Financial EDI applications involve exchange of monetary transactions between the companies and their banks. The level of security demanded at the individual transaction level is much greater than other EDI applications. Poorly controlled vulnerabilities in electronic funds transfer (EFT) may cause major financial losses and embarrassment [4].

It would be inefficient to implement expensive controls in the system if the sensitivity and vulnerability of system are not high. Of course, EDI controls should be appropriately implemented for the security and integrity of system using limited resources and expertise.

In trade EDI applications, the handling of shipping instructions and contract status by exporters and transport companies is greatly improved through the use of trade EDI applications. Customs authorities may adopt formal controls to enhance the efficiency of clearance; such clearance can easily be structured and simplified. Ports and carriers can then handle the variety of freight that passes through. As the physical movement of goods requires time, the progress of product shipments and movement can be checked and traced.

In trade applications, the security requirements are not as high as in financial applications. The primary goal of the trade EDI, however, is to speed-up cargo clearance and lower the cost of paperwork in international trade. The formal controls establish consistent cargo and customs clearance procedures and perform conversions between different trading partners’ environments and support varied protocol and access methods. The implementation of EDI in Korean trade has been supported by a government agency that monopolizes the provision of services for international trade. Trading companies depend mainly on VAN service providers for communication controls. Reliance on formal EDI controls by external parties (i.e., government, VANs) leads to low investment in control implementation by EDI adopters and a relatively high perceived efficiency of formal controls.

In financial applications, formalized procedures and standards are not universally accepted as the basic controls for EDI implementation. Further, formal procedures need to be made in order to prevent computer abuse and ‘‘opportunistic behaviors’’ by internal employees as well as intruders. As there are little known computer abuse or disputes in internal departments and with trading partners, it is difficult to perceive the benefits of formal EDI controls.

Table 7  
Average efficiency of firms

<table><tr><td rowspan="2">Input variables</td><td rowspan="2">Output variable</td><td colspan="2">Mean</td></tr><tr><td>Financial applications</td><td>Trade applications</td></tr><tr><td>Internal formal</td><td>Integration</td><td>29.4</td><td>50.5</td></tr><tr><td rowspan="3">Application controls</td><td>Utilization</td><td>20.5</td><td>36.6</td></tr><tr><td>Improved relations</td><td>34.0</td><td>58.2</td></tr><tr><td>Influence on productivity</td><td>43.6</td><td>51.0</td></tr><tr><td>Internal formal</td><td>Integration</td><td>35.5</td><td>37.1</td></tr><tr><td>Communication</td><td>Utilization</td><td>23.3</td><td>28.7</td></tr><tr><td rowspan="2">Controls</td><td>Improved relations</td><td>39.4</td><td>63.9</td></tr><tr><td>Influence on productivity</td><td>36.7</td><td>55.8</td></tr><tr><td>External formal VAN</td><td>Integration</td><td>27.6</td><td>23.0</td></tr><tr><td rowspan="3">Controls</td><td>Utilization</td><td>20.0</td><td>14.9</td></tr><tr><td>Improved relations</td><td>32.0</td><td>26.1</td></tr><tr><td>Influence on productivity</td><td>41.2</td><td>39.0</td></tr><tr><td>External formal</td><td>Integration</td><td>23.9</td><td>40.6</td></tr><tr><td rowspan="3">Partner controls</td><td>Utilization</td><td>21.1</td><td>23.7</td></tr><tr><td>Improved relations</td><td>35.1</td><td>39.4</td></tr><tr><td>Influence on productivity</td><td>44.9</td><td>46.8</td></tr><tr><td>Internal automated</td><td>Integration</td><td>61.4</td><td>45.1</td></tr><tr><td rowspan="3">Application controls</td><td>Utilization</td><td>42.8</td><td>31.2</td></tr><tr><td>Improved relations</td><td>63.5</td><td>55.3</td></tr><tr><td>Influence on productivity</td><td>60.4</td><td>48.8</td></tr><tr><td>Internal automated</td><td>Integration</td><td>31.9</td><td>19.9</td></tr><tr><td>Communication</td><td>Utilization</td><td>15.6</td><td>12.8</td></tr><tr><td rowspan="2">Controls</td><td>Improved relations</td><td>41.7</td><td>23.4</td></tr><tr><td>Influence on productivity</td><td>24.5</td><td>24.7</td></tr><tr><td>External automated</td><td>Integration</td><td>43.6</td><td>23.4</td></tr><tr><td rowspan="3">Controls by VAN</td><td>Utilization</td><td>33.8</td><td>23.2</td></tr><tr><td>Improved relations</td><td>61.0</td><td>31.7</td></tr><tr><td>Influence on productivity</td><td>54.1</td><td>24.0</td></tr><tr><td>External automated</td><td>Integration</td><td>38.0</td><td>42.5</td></tr><tr><td>Controls by trading</td><td>Utilization</td><td>33.1</td><td>20.9</td></tr><tr><td rowspan="2">Partners</td><td>Improved relations</td><td>43.3</td><td>47.2</td></tr><tr><td>Influence on productivity</td><td>42.5</td><td>47.4</td></tr></table>

Table 8  
Wilkoxon test of efficiency difference between applications

<table><tr><td>Input class</td><td>Average in financial applications</td><td>Average in trade applications</td><td>Wilkoxon Z</td><td>Significance</td></tr><tr><td>Formal controls</td><td>31.8</td><td>39.7</td><td>-2.223</td><td>0.026</td></tr><tr><td>Automated controls</td><td>43.2</td><td>32.6</td><td>-2.844</td><td>0.004</td></tr></table>

Table 9  
Slack analysis of inefficient firms (financial applications) (DMUs are ordered in ascending order of efficiency)

<table><tr><td>DMU</td><td>Internal formal application controls</td><td>Internal formal communication controls</td><td>External formal VAN controls</td><td>External formal partner controls</td><td>Internal automated application controls</td><td>Internal automated communication controls</td><td>External automated controls by VAN</td><td>External automated controls by trading partners</td><td>Efficiency</td></tr><tr><td>UNIT89</td><td>3.2</td><td>2.9</td><td>3.8</td><td>2.5</td><td>2.5</td><td>2.9</td><td>2.5</td><td>1.3</td><td>58.2</td></tr><tr><td>UNIT75</td><td>2.4</td><td>2.5</td><td>2.5</td><td>2.3</td><td>2.5</td><td>2.8</td><td>2.1</td><td>1.3</td><td>65.0</td></tr><tr><td>UNIT58</td><td>1.9</td><td>1.9</td><td>3</td><td>1.6</td><td>1.8</td><td>2.5</td><td>1.6</td><td>1.6</td><td>73.0</td></tr><tr><td>UNIT71</td><td>1.2</td><td>1.3</td><td>1</td><td>1</td><td>1.2</td><td>2.4</td><td>1</td><td>1.7</td><td>75.5</td></tr><tr><td>UNIT29</td><td>0.9</td><td>0.7</td><td>1.2</td><td>0.7</td><td>1.1</td><td>1.4</td><td>1.2</td><td>0.6</td><td>75.7</td></tr><tr><td>UNIT56</td><td>1.4</td><td>1.5</td><td>2.6</td><td>2.3</td><td>1.7</td><td>1.5</td><td>1.3</td><td>1.9</td><td>78.2</td></tr><tr><td>UNIT59</td><td>1.5</td><td>1.2</td><td>2.3</td><td>1.1</td><td>0.9</td><td>1</td><td>0.9</td><td>0.4</td><td>79.9</td></tr><tr><td>UNIT35</td><td>2</td><td>0.3</td><td>2.2</td><td>2.2</td><td>1.4</td><td>3.1</td><td>0.6</td><td>1.4</td><td>80.1</td></tr><tr><td>UNIT99</td><td>1.7</td><td>1.5</td><td>0.8</td><td>3.7</td><td>0.9</td><td>0.9</td><td>0.8</td><td>2.3</td><td>81.4</td></tr><tr><td>UNIT91</td><td>2.3</td><td>1</td><td>1.6</td><td>1.4</td><td>0.7</td><td>1.1</td><td>1.4</td><td>0.3</td><td>83.7</td></tr><tr><td>UNIT65</td><td>1</td><td>1</td><td>2.4</td><td>2.2</td><td>0.8</td><td>0.6</td><td>1.6</td><td>0.5</td><td>85.1</td></tr><tr><td>UNIT76</td><td>0.9</td><td>0.8</td><td>1</td><td>0.8</td><td>0.4</td><td>2.5</td><td>0.4</td><td>0.3</td><td>87.3</td></tr><tr><td>UNIT73</td><td>1.8</td><td>0.7</td><td>1.7</td><td>0.3</td><td>0.5</td><td>0.5</td><td>0.7</td><td>0.6</td><td>88.4</td></tr><tr><td>UNIT79</td><td>0.5</td><td>0.6</td><td>1.1</td><td>0.3</td><td>0.8</td><td>1.8</td><td>0.4</td><td>1.1</td><td>88.9</td></tr><tr><td>UNIT110</td><td>1.5</td><td>0.3</td><td>2.1</td><td>1.7</td><td>0.3</td><td>1.6</td><td>0.3</td><td>0.1</td><td>93.5</td></tr><tr><td>UNIT86</td><td>1.1</td><td>0.3</td><td>0.2</td><td>0.3</td><td>0.3</td><td>0.2</td><td>0.8</td><td>0.8</td><td>95.4</td></tr><tr><td>UNIT67</td><td>0.1</td><td>1</td><td>2.3</td><td>2.3</td><td>0.2</td><td>1</td><td>1.1</td><td>1</td><td>96.7</td></tr><tr><td>UNIT82</td><td>1.5</td><td>0.1</td><td>0.7</td><td>0.4</td><td>0.1</td><td>0.5</td><td>0.1</td><td>0</td><td>97.5</td></tr><tr><td>Average</td><td>1.49</td><td>1.09</td><td>1.81</td><td>1.51</td><td>1.01</td><td>1.57</td><td>1.04</td><td>0.96</td><td>82.4</td></tr></table>

When two trading firms establish an EDI links, the implementation of formal EDI controls can be effected by the support strategy of the VAN or government association. Given that companies are uncertain about the implementation of formal EDI controls, the trading partners or industry association must spread the reasons for using EDI within the industry. Especially in Korea, the pressures of the government make firms follow EDI standards through Korea Telecommunication Networks (KTNET) by communicating required documents whenever goods are imported or exported. They are faced with lengthy manual procedures if they do not exchange EDI messages via this network and are thus encouraged to follow the formal its controls. Hence, formal controls are more efficiently used in trade applications than in financial applications.

Table 9 shows the slack of controls for the 18 inefficient financial EDI applications (the number of efficient financial applications is 23). These indicate the number of reductions that are needed for the formal and automated controls in order to make the control system efficient. The ‘‘trouble spots’’ are identified by evaluating the relative efficiency of the EDI adopters. As an example, firm 89 needs to reduce the usage level of internal formal application and external formal VAN controls and the needed reduction is greater than 3.0. This appears relatively greater than the other slack values, strongly suggesting a need to reduce the usage level for these two controls. Firm 82 demands the reduction of less than 1.0 in every input variable except internal formal application controls. Firm 99 has one input variable, external formal partner controls, that requires a reduction of more than 3.0. On average, DEA analysis shows that the input variables of all formal controls except internal communication demand slightly higher reduction of the usage level than for automated controls. EDI adopters should reduce the usage level of formal more than automated controls to make the systems more efficient.

## 4. Conclusions

IS controls and security is ranked as the third most important issue in IS management across the globe and its importance becomes steeply greater during recent years. One out of five firms in US suffer from at least one security breach in a 3-year period, with one firm reporting a two-million dollars loss. The growing dependence on IS makes the demand for reliability and integrity of information greater. EDI adopters are moving EDI technology onto the Internet as a costeffective channel for EDI transactions away from traditional Value Added Network (VAN) and this leads to the establishment of Internet-based EDI. A significant portion of EDI traffic does not travel over the Internet yet, however, because there are many business issues to be resolved. One such problem is the security and reliability of the Internet.

This study of the efficiency of EDI controls has significant implications for practitioners and researchers. Although EDI controls have been considered important, few studies verify their efficiency. From a security management and planning perspective, an overall normative approach to evaluation and design of controls is lacking. Current security practice is lacking in security planning efforts to evaluate the fit between security requirements and potential security solutions [24]. Further, when the system risks are not predictable and cannot be eliminated, it is difficult to establish if-then rules explaining the choice of controls. The application of DEA provides a basis for logical and prudent decision procedures when EDI auditors and mangers have to determine the mode and level of controls in the process of EDI implementation for overall high efficiency of the control systems. Through the analyses of efficient controls, it is possible to demonstrate why some companies have lower system performance when they appear to establish no apparent control procedures and mechanisms, or why frequent system errors break out in companies that have developed strong formal and technical procedures.

Each company needs to determine the need for controls in order to make a successful EDI system. In Fig. 1, if the organization is on the ‘‘d’’ and ‘‘e’’ curve, management should consider giving resources to make their control system efficient by respectively moving to ‘‘b’’ and ‘‘c,’’ which lie on the ‘‘efficiency frontier.’’ The efficiency analysis of controls will help

![](/api/attachments/NPRC7F7E/fulltext/images/f4eea9bb350c4ea23cef9df31223d2ea2b2bab6e6ef0e2755329a5cab19e4974.jpg)  
Fig. 1. Example of control design.

EDI managers and auditors decide whether the proper formal or automated controls have been installed.

Commitment to efficiency management of controls by EDI adopters may not matter much in a situation where much of the work processes for EDI implementation becomes structured and formalized by the influence of external trading partners and VAN service providers. This is often the case in Korea. Many companies have been using EDI for less than 5 years and the state of their implementation is under strong external influence from trading partners and VAN service providers. Additionally, Korean companies have not recognized the seriousness of exposure in using EDI.

## Appendix A. Input variables (eight variables)

Respondents answer the extent to which they agree or disagree with each statement about controls. The seven-point Likert-type scales are used. Select the representative value added network service your company uses the most. If your company does not use VAN, skip the questions about VAN.

(1) Internal formal application controls

(1.1) Systems are changed only through authorization from the responsible managers.

(1.2) Integrity check of messages is strictly performed before the messages are processed in the application.

(1.3) Audit trails of transactions are always maintained for correction of errors and contingency planning.

(1.4) System login is appropriately controlled by access control procedures such as passwords.

(2) Internal formal communication controls

(2.1) EDI messages are checked for duplication, omission or inaccuracy after they are generated and before transmitting the messages.

(2.2) The sender, receiver, and contents of EDI messages are appropriately authenticated after the messages are generated or received.

(3) External formal VAN controls

(3.1) VAN service providers have an appropriate contingency plan for network failures.

(3.2) VAN service providers retransmit messages if the messages are omitted, duplicated, or inaccurate.

(3.3) VAN service provider maintains audit trails for recovery of inaccurate messages.

(3.4) VAN service provider controls unauthorized access and dial login to network.

(3.5) VAN service provider controls unauthorized access to mailbox by internal staff.

(4) External formal partner controls

(4.1) The representative trading partner has an appropriate contingency plan for network failures.

(4.2) The representative trading partner retransmits messages if they are omitted, dupli cated, or inaccurate.

(4.3) The representative trading partner maintains audit trails for the recovery of inaccurate messages.

(4.4) The representative trading partner controls unauthorized access and dial login to network.

(5) Internal automated application controls

(5.1) Automated integrity check of data fields is performed using embedded software before received messages are processed in internal applications.

(6) Internal automated communication controls

(6.1) Embedded software is effectively used to automatically check accuracy of messages received.

(6.2) Automated authentication procedures effectively ascertain the identity of sources or destination before sending and after receiving messages.

(7) External automated controls by VAN

(7.1) The VAN service provider automatically records messages for the correction of errors and retransmission of corrected messages.

(7.2) The VAN service provider automatically tracks and reports the status of message communication.

(7.3) The VAN service provider attaches message identification codes or digital signatures to effectively authenticate the messages.

(8) External automated controls by trading partners

(8.1) The representative trading partner automatically records messages for the correction of errors and retransmission of corrected messages.

(8.2) The representative trading partner automatically tracks and reports the status of message communication.

(8.3) The representative trading partner attaches message identification codes or digital signatures to effectively authenticate the messages.

## A.1. Output variables (four variables)

(1) Integration (average integration of five application)

The extent to which EDI data can be directly processed within five applications (selected by respondents) without human intervention. The seven-point Likert-type scales are used.

(2) Utilization (average utilization of five application)

The proportion (%) that a company uses EDI processing. These can be processed using other complementary means. It is measured as the proportion that a firm’s information exchange and processing are handled through EDI in five applications (selected by respondents).

(3) Improved relations (average of five items)

(3.1) Relations with the representative trading partner are greatly improved through reduced response time after adopting EDI.

(3.2) Our company maintains improved relations with the representative trading partner by reducing delay from errors.

(3.3) Our company improved trust in relations with the representative trading partner by enhancing confidentiality of documents.

(3.4) Relations with the representative trading partner are greatly improved by reducing omission and inaccurate transmission.

(3.5) Our company maintains high trust with the representative trading partner by protecting messages from disclosure to unauthorized third party.

(4) Influence on productivity (average of three items)

(4.1) The efficiency of interdepartmental transaction processing is greatly increased.

(4.2) Accuracy is greatly improved by reduced paperwork.

(4.3) Transaction processing costs are greatly reduce after adopting EDI.

## References

[1] G. Aggarwal, Z. Rezaee, Introduction to EDI internal control, IS Audit & Control Journal 2, 1994, pp. 64–68.

[2] S. Banerjee, D.Y. Golhar, Electronic data interchange: characteristics of users and nonusers, Information & Management 26, 1994, pp. 65–74.

[3] F. Bergeron, L. Raymond, Managing EDI for corporate advantage: a longitudinal study, Information & Management 31, 1997, pp. 319–333.

[4] A.D. Boef, Assessing electronic funds transfer (EFT) security vulnerabilities in SAP R/3 environments, IS Audit & Control Journal 1, 1999, pp. 25–28.

[5] P. Byrnes, V. Valdmanis, Variable cost frontiers: an investigation of labor costs in hospitals, in: T.R. Gulledge Jr., L.A. Litteral (Eds.), Cost Analysis Applications of Economics and Operations Research. Springer-Verlag, Berlin, 1989.

[6] S. Chan, M. Govindan, J.Y. Picard, E. Leschiutta, EDI for Managers and Auditors. Electronic Data Interchange Council of Canada, Toronto, Ont., 1993.

[7] A. Charnes, W.W. Cooper, E. Rhodes, Measuring the efficiency of decision making units, European Journal of Operational Research 2 (6), 1978, pp. 429–444.

[8] A. Charnes, W.W. Cooper, D.B. Sun, Z.M. Huang, Polyhedral cone-ratio DEA models with an illustrative application to large commercial bank, Journal of Econometrics 46, 1990, pp. 73–91.

[9] J.A. Chilingerian, D. Sherman, Managing physicians efficiency and effectiveness in providing hospital services,

Health Services Management Research 3 (1), 1990, pp. 3–15.

[10] J.V. Hansen, N.C. Hill, Control and audit of electronic data interchange, MIS Quarterly 13 (4), 1989, pp. 403–413.

[11] ISACA, EDI Control Guide, EDI Council of Australia, Sydney Chapter, Information Systems Audit and Control Association, 1990.

[12] R. Jamieson, EDI: An Audit Approach, The EDP Auditors Foundation Inc., Rolling Meadows, IL, 1994.

[13] G.W. Joseph, All VANs are not created equal regarding internal control, IS Audit & Control Journal (1999) 41–47.

[14] C.M. Lawrence, Usage of concurrent EDP audit tools, The EDP Auditor Journal 3, 1988, pp. 49–54.

[15] S. Lee, I. Han, H. Kym, The Impact of EDI controls on EDI implementation, International Journal of Electronic Commerce 2 (4), 1988, pp. 71–98.

[16] A.Y. Lewin, J.W. Minton, Determining organizational effectiveness: another look, and an agenda for research, Management Science 32 (5), 1986, pp. 514–538.

[17] M.A. Mahmood, K.J. Pettingell, A.I. Shaskevich, Measuring productivity of software projects: a data envelopment analysis approach, Decision Sciences 27 (1), 1996, pp. 57–80.

[18] J.A. Marcella, S. Chan, EDI Security, Control, and Audit, Artech House Inc., Norwood, MA, 1993.

[19] R.N. Mehta, Risks and controls in an EDI environment, IS Audit & Control Journal 5, 1998, pp. 40–44.

[20] D.B. Parker, Computer Security Management, Reston Publishing Company Inc., Reston, VA, 1981.

[21] G. Premkumar, K. Ramamurthy, S. Nilakanta, Implementation of electronic data interchange: an innovation diffusion perspective, Journal of Management Information Systems 11 (2), 1994, pp. 157–186.

[22] J.A. Senn, Electronic Data Interchange; the Elements of Implementation, Information Systems Management (Winter) (1992) 45–53.

[23] L.W. Stern, P.J. Kaufmann, EDI in selected consumer goods industries: an inter-organizational perspective, in: R. Buzzel, Marketing in an Electronic Age, Harvard Business School Press, Boston, 1985.

[24] D.W. Straub, R.J. Welke, Coping with systems risk: security planning models for management decision making, MIS Quarterly 22 (4), 1998, pp. 441–469.

[25] H.H. Teo, B.C.Y. Tan, K.K. Wei, Organizational transformation using electronic data interchange: the case of TradeNet in Singapore, Journal of Management information Systems 13 (4), 1997, pp. 139–165.

[26] E. Thanassoulis, A. Emrouznejad, Warwick Windows DEA Version 1.02: User’s Guide, Warwick Business School, University of Warwick, Conventry, United Kingdom, First Print, 1996.

[27] R. Weber, Information Systems Control and Audit, Prentice-Hall Inc., Upper Saddle River, NJ, 1999.

[28] L.L. Wood, Measuring the relative efficiency of schools in the Philadelphia PA, Masters Paper, Department of Public Policy and Management, Wharton School, University of Pennsylvania, 1983.

Sangjae Lee is a professor at the School of Management in Sejong University. He received his Ph.D. in management information systems from the Graduate School of Management, Korea Advanced Institute of Science and Technology. He is a certified information systems auditor (CISA). His research interests include electronic data interchange, information systems control and audit

Kidong LEE is an assistant professor at Department of Business Administration in University of Incheon. He received M.B.A. from University of Maine and earned Ph.D. in management systems from Kent State University. His research interests include neural computing, intellectual property management, e-learning, and e-business applications

In Won Kang is a research professor of MIS at Sungkyun Management Research Institute, Seoul, Korea. His research focuses on marketing applications in decision making, LISREL analysis of electronic commerce performance, and B2B commerce. He accumulated a plentiful experience in aviation industry for 10 years. He is developing several working papers specializing in trust, trust transfer in multi-channels, and artificial intelligencebased analysis of IS performance.
