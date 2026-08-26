---
otero_id: 11322
otero_key: "BJA44NKQ"
title: "Developing novel solutions to realise the European Energy – Information Sharing & Analysis Centre"
authors: "Rafał Leszczyna; Tania Wallis; Michał R. Wróbel"
year: "2019"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2019.05.007"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Developing novel solutions to realise the European Energy – Information Sharing & Analysis Centre

![](/api/attachments/BJA44NKQ/fulltext/images/8140358734fbf7775a87a0f697b6aa6c9c6edf9897efecf0254d97b8b2a49231.jpg)

Rafał Leszczyna<sup>a,\*</sup>, Tania Wallis<sup>b</sup>, Michał R. Wróbel<sup>a</sup>

<sup>a</sup> Gdańsk University of Technology, Narutowicza 11/12, Gdańsk 80-952, Poland

<sup>b</sup> University of Strathclyde, 16 Richmond Street, Glasgow G1 1XQ, United Kingdom

## A R T I C L E I N F O

Keywords: Cybersecurity Situation awareness Information sharing ISAC Critical infrastructures Power systems Energy sector

## A B S T R A C T

For more efective decision making in preparation for and response to cyberevents in the energy sector, multilevel situation awareness, from technical to strategic is essential. With an uncertain picture of evolving threats, sharing of the latest cybersecurity knowledge among all sector stakeholders can inform and improve decisions and responses. This paper describes two novel solutions proposed during the formation of the European Energy – Information Sharing & Analysis Centre (EE-ISAC) to build situation awareness and support information sharing. The development of the EE-ISAC towards regular information sharing among members is described. This demonstrates the foundations achieved so far upon which a situation awareness network can be built for the energy sector.

## 1. Introduction

The cyberthreat landscape evolves rapidly. Current cyberattacks utilise multiple vectors and proliferate gradually in stages that extend over a longer time (advanced persistent threats – APTs) [1-3]. Moreover, highly targeted and specialised attacks have been introduced (targeted attacks) [4] that aim at concrete computer systems. Especially in the energy sector, these threats, together with other cybersecurity problems (see Table 1) can lead to very severe consequences. The associated key cybersecurity decisions that the energy industry fails to address ap propriately regard the scale of cybersecurity investments or the design of defence architectures and strategies (see Table 2). The causes of this situation are mostly related to the characteristics of the information available during the decision-making process, which result in improper recognition of the cybersecurity context. Decision-makers are overwhelmed with large amounts of raw, unstructured and imbalanced data delivered from numerous, heterogeneous data sources. Besides, this information can be often false, misleading, incomplete or irrelevant [5, 6].

The answer to this situation is the application of practical cybersecurity solutions that support heightened situational awareness and active information sharing [2, 5, 8-10, 12, 16-19]. Situational awareness (SA) regards an extensive analysis of the entire decision-making context. It encompasses the continuing perception of an environment, the comprehension of observations and the projection of their status onto the proximate future [20-22]. SA employs technological components that collect data related to cybersecurity events from miscellaneous system locations to be analysed collectively in order to detect attacks and promptly react to them (e.g. by applying appropriate countermeasures or reducing the efects [23]). Cybersecurity information sharing (CIS), on the other hand, relies on partners exchanging incident-related data such as the descriptions of experienced disturbances, indicators of compromise, proposed remedies and other security expertise to build preparedness for large-scale incidents and future threats [2, 24, 25]. Information Sharing and Analysis Centres (ISACs) are the institutions designated to lead sector-specific cyberincident information exchange [8, 26]. With the aim of improving cybersecurity in independent industry areas, they often interlink the industry and the governmental organisations, forming public-private partnerships. In recent years various ISACs have been established, including the European Energy – Information Sharing & Analysis Centre (EE-ISAC), the Electricity Information Sharing and Analysis Center(E-ISAC) or the Oil and Natural Gas Information Sharing and Analysis Center(ONG-ISAC). They attract members from utilities, vendors, solution providers, academia and research organisations.

This paper presents two novel solutions proposed during the development of the EE-ISAC (www.ee-isac.eu) to support its operation, namely a three-tier situation awareness network (SAN) and a dedicated, sectoral cyberincident information sharing platform (ISP), together with innovative mechanisms that address the problems related to the

Table 1

<table><tr><td>Key cybersecurity challenges of the contemporary energy sector.</td></tr><tr><td>Long-lasting, multi-vector attacks difficult to detect [6-10]</td></tr><tr><td>Stealthy application-layer attacks [11, 12]</td></tr><tr><td>Continuously-evolving attack methods [1, 3-5, 7]</td></tr><tr><td>Inefficient conventional cyberdefences [2, 5-7]</td></tr><tr><td>Deperimeterisation and inability to secure outside local perimeter [5]</td></tr><tr><td>Growing volume and variety of endpoints [5]</td></tr><tr><td>Limited visibility of security incidents [7]</td></tr><tr><td>Excessive alarm numbers, high rate of false positives [6]</td></tr><tr><td>Broad availability of attack toolkits [8]</td></tr><tr><td>Organisations often unaware of being a victim of a cyberattack [5, 7]</td></tr><tr><td>Organisations unprepared for an incident [12]</td></tr><tr><td>Table 2Cybersecurity decisions that the energy sector often fails to address.</td></tr><tr><td>Which activities to include into defence strategies? [5, 10]</td></tr><tr><td>Which elements to include into comprehensive security architectures? [10]</td></tr><tr><td>How much to invest into cybersecurity? [10]</td></tr><tr><td>Which defences to apply in the first order? [8, 13, 14]</td></tr><tr><td>Which vulnerabilities to focus on in the first order? [8]</td></tr><tr><td>Which procedures to include into organisational cybersecurity policies? [12]</td></tr><tr><td>Which rules to include into technical solutions&#x27; cybersecurity policies? [15]</td></tr><tr><td>Which actions to take in the face of an incident? [5, 8, 10]</td></tr></table>

implementation and utilisation of these systems. The development was carried out by the European project – DEnSeK (Distributed Energy Security Knowledge). The SAN integrates multiple heterogeneous sensors with Security Information and Event Management (SIEM) systems and a specialised dashboard to efectively provide cybersecurity situational awareness. The ISP aims at supporting the exchange of sectorspecific cyberincident-related data, including case descriptions, experiences or threat descriptions. The interoperability of the ISP and the SANs is supported by design – the information shared in the ISP can be directly delivered from the SANs.

In the following sections, after the discussion of the relevant work (see Section 2), the situation awareness network (Section 3) and the information sharing platform (see Section 4) are described. Section 5 is devoted to the evaluation of the proposed solutions. It includes an overview of utilised testing metrics and description of testing environments, integration as well as usability tests. Section 6 describes the realisation of the EE-ISAC towards establishing information sharing for the energy sector. The paper closes with concluding remarks.

## 2. Related work

The research on information sharing and situational awareness centres around five main domains, namely the economic aspects of information sharing (IS), models and determinants of IS, data formats, tools supporting and conceptual frameworks.

In the area of economic aspects of cybersecurity information sharing (CIS), Gordon et al. [27] investigated the impact of IS on security investments and analysed the incentives for information exchange based on economic models. Gal-Or and Ghose [28] and Hausken [29] com plemented this research by applying game-theoretical approaches. The relationships between IS decisions and cybersecurity investments were investigated by Liu et al. [30]. The work of Tosh et al. [31] is one of the most recent economic studies on CIS. The authors model the problem area as an evolutionary game between organisations and analyse IS advantages.

Concerning IS models, determinants and attributes, Vakilinia and Sengupta [32] studied incentives to share sensitive cyberincident data, with particular consideration to rewarding and participation-fee allo cation mechanisms. Analogous, participation cost-related factors were investigated by Tosh et al. [33]. Ghose et al. [34] modelled relationships between attackers carrying out an attack against an enterprise to investigate the incentives for and the optimal level of sharing the information about the company's vulnerabilities. Nikoofal and Zhuang [35], Zhuang et al. [36], Zhuang and Bier [37], and Dighe et al. [38] applied game theory to determine the role of CIS in cyberdefence strategies. Another approach was adopted by Sedenberg and Mulligan [39] who analysed public healthcare as a model that enabled identifying guiding principles for cybersecurity information sharing. The principles encompassed governance, reporting, anonymisation, and use limitations.

Over the last decade, several data specifications and standards have been developed to facilitate efective exchange of cybersecurity information. The MITRE-moderated, community-driven work on Trusted Automated Exchange of Indicator Information (TAXII), Cyber Observable Expression (CybOX) and Structured Threat Information Expression (STIX) [24, 40, 41] is particularly influential as many new developments derive from it. An extension to STIX that supports sharing the information about the impact of cyberevents outside an organisation was proposed by Fransen et al. [41] who discuss it in the context of operation of the Dutch National Detection Network (NDN). Qamar et al. [42] integrated concepts of STIX and CybOX together with the Common Vulnerabilities and Exposures (CVE) notation and a network model into a Web Ontology Language (OWL)-based ontology that enables threatrelated specifications, semantic reasoning and contextual analyses. de Fuentes et al. [24] enhanced STIX with privacy-preserving mechanisms. A detailed overview of existing solutions in this area is provided in the report of ENISA [43].

Multiple solutions have been proposed to support SA and CIS. Vakilinia [44] defined an anonymisation mechanism for information exchange that comprises four main components: registration, sharing, dispute and rewarding. Jajodia et al. [45] described Cauldron – a topological vulnerability analysis tool that aims at supporting missioncentric situational awareness. As a promising direction in detecting recent cyberattacks, collaborative intrusion detection (CIDS) has been studied intensively already for more than a decade [46]. Current proposals include a privacy-preserving machine-learning based CIDS for vehicular ad hoc networks (VANETs) [47], a CIDS designed specifically to protect the smart grid [48], a trust-based clustering solution that supports deploying CIDS in wireless sensor networks (WSN) [49] or a CIDS for Advanced Metering Infrastructure (AMI) [50]. Several solutions that support situational awareness are described in the edited volume of Jajodia et al. [51]

As far as operational SA or IS architectures are concerned, platforms such as AlienVault Open Threat Exchange (OTX), Malware Information Sharing Project (MISP) or ThreatView's Cyber Threat & Reputation Intelligence have been developed commercially or by communitydriven projects.

The scientific research has been focusing on conceptual models or methodologies of their development, deployment and governance. Examples of such theoretical frameworks include the proposals of the European Control System Security Incident Analysis Network (ECOSS-IAN) project [52, 53], Barth et al. [54], Klump and Kwiatkowski [55] or Brunner et al. [56], while Alcaraz and Lopez [57] introduced a systematic approach for developing and establishing situational awareness architectures in the context of critical infrastructure protection.

Regarding more practical proposals, Marchetti et al. [6] developed a platform for analysing network traffic in large computer environments to identify the most suspicious internal hosts. The solution focuses on trafic flaws instead of transmitted data content which results on its high scalability and limited computational and storage costs. Alternatively, Friedberg et al. [9] proposed a system that analyses event logs collected from various, distributed network locations in order to spot correlations that could indicate potential anomalies. The problem of data heterogeneity in similar platforms was addressed by Coppolino et al. [17] who implemented a dedicated framework able to translate data from multiple architectural layers and domains.

The analytical [27-29, 31, 32, 34-38] and practical [6, 9, 17] studies demonstrate that SA and IS are an efective response to the novel cyberthreats currently faced by the energy sector. The studies ofer many insights that can be applied during the development of working solu tions. However, the prevalence of them are still on a conceptual level, while the current practical proposals focus on the technical dimension. So far, the existing contributions have been separately addressing situational awareness and information exchange. At the same time, in order to achieve the complete advantage of these areas it is necessary to combine them [57]. The solutions described in this paper and their integration within the EE-ISAC support such a joint approach. The data delivered from distributed SA technological components are processed on the operational and tactical level of cybersecurity (see Section 3.1), enabling not only recognising attack attempts or ongoing occurrences and promptly react to them, but also devising cybersecurity operations that regard longer periods of time and are mostly related to attack prevention and preparedness. Furthermore, these processed data are utilised on the strategic-level of cybersecurity where defence strategies, policies or regulations are devised. At this level, the developed IS platform (see Section 4) plays a pivotal role.

## 3. Situation awareness network

A situation awareness network (SAN) is a technical platform that provides situation awareness (SA) with the aid of sensors deployed in various system locations [58]. It is responsible for the provision of detailed, processed cyberincident information to increase threat detection eficiency and facilitate the comprehension of reported information by human operators. This, in turn, facilitates decision making and fosters faster reaction to threats and incidents.

## 3.1. Architecture

A new, three-tiered architecture for the energy sector SAN was de signed (see Fig. 1) [58-60]. Approximately, the three tiers correspond to the three levels of cybersecurity, from technical to tactical.

The lowest tier, i.e. the data tier that operates on the technical level of cybersecurity consists of miscellaneous network and host-based sensors which enable system inspection and detection of suspect events. The sensors include or are built upon signature-based and anomalybased intrusion detection/prevention systems, network monitor soft ware or trafic analysis tools. The joining together of multiple, heterogeneous sensors is a direct response to the advent of complex, campaign-oriented cyberthreats that are undetectable with uniform approaches.

The data collected by the sensors are delivered to the middle tier of the architecture, i.e. the logic tier, which includes the Security Information and Event Management (SIEM) system. The SIEM aggregates the data, pre-processes them and performs data correlations based on predefined, technical rules. In this way, more sophisticated threats can be automatically recognised already at this level of the SAN architecture. With the detections, alerts are generated which can be further analysed by human operators (operational cybersecurity) or processed by the system in order to trigger automated attack responses.

In parallel to that, the data are transferred to the top tier of the SAN, namely the presentation tier which is based on a dedicated dashboard. The dashboard utilises multiple, flexibly configurable visualisation components to support operational-level and tactical-level cybersecurity analyses performed by human operators. This additional tier was introduced to support recognising the threats undetectable by SIEM system due to their mode of operation or architectural limitations [15, 17]. The dashboard fosters analysing and filtering large amounts of data to concentrate on the most critical determinants of a cyberincident. It enables monitoring of diverse aspects of system security situation as well as observing its evolution after an event is reported, which corresponds to the tactical cybersecurity level.

## 3.2. Security requirements for sensors

Sample security requirements for sensors and their supporting environments include auto-protection from unauthorised modifications and access to functions and data, collection and storage of information about all events that may indicate an inappropriate activity, granting authorised users the access only to appropriate functions and data, appropriate handling of potential audit and sensor data storage overflows, ensuring the confidentiality of sensor data when available to other SAN components or secure delivery, installation, management and operation of sensors. The requirements are based on the National Information Assurance Partnership (NIAP) protection profiles for intrusion detection systems, sensors, scanners and analysers [61-64] which are conformable to Common Criteria – an international standard that specifies the criteria for security evaluation of IT hardware and software products [65].

![](/api/attachments/BJA44NKQ/fulltext/images/8076ae387a1ffb1d1a69c463381cd6d38822466211514ac2a1ff3ac7c36318a2.jpg)  
Fig. 1. The logical architecture of the cybersecurity situation awareness network for the electricity sector.

## 3.3. Event correlation rules

To allow SAN to recognise relations between cybersecurity events detected by diferent sensors, to identify interrelated occurrences or to trace common source or target of events, event correlation rules need to be specified in the form of machine-readable definitions. Rules for prioritisation of SAN alerts were designed to limit the number of false positives received from the data tier. The highest-priority alerts, which require an immediate response, are raised in the simultaneous occurrence of at least two alerts defined in the correlation table. In addition, the attack target must be situated in the protected network. In this mode, alerts dispatched by random events are limited, while the overall detection capability remains unafected. Medium-priority alerts are is sued when two alerts of any type are signalled in close time proximity from the data tier. Usually, this corresponds to the situation when an adversary attempts to conduct an automated attack without prior network cognisance. Medium-priority alarms automatically start autoprotection actions, such as IP address blocking. The remaining individual and separate alerts originated from the data tier are assigned the low priority. They are registered in the audit log and can be resolved in a convenient time.

## 4. Information sharing platform

The information sharing platform (ISP) aims at facilitating the ex change of sector-specific cyberincident-related knowledge by providing communication interfaces and infrastructure. The exchanged informa tion includes extended case descriptions, experiences, detailed processed input from the SAN (see Section 3), threat descriptions, coun termeasures, good practices, standards and procedures. Based on the input shared between stakeholders, sectoral cybersecurity strategies, policies and architectures can be collaboratively developed which corresponds to the strategic level of cybersecurity.

The centralised model of information exchange is implemented, where a central node is introduced which acts as an intermediary in transferring data [26]. In the implemented platform, the central node is operated by the EE-ISAC, which moderates cybersecurity communications or assures uniform distribution of the information in the whole community. However, also peer-to-peer interactions between partners are possible. Besides, the central, ISAC hub communicates with other ISACs and non-ISAC hubs, exchanging information in various forms such as client and server or hub and spoke. Both, unidirectional and bidirectional communication with the central node is facilitated, primarily in the asynchronous form. To facilitate the transmission of all cyberincident-related data in natural language and machine-readable formats, a dedicated data model was developed, which incorporates established specifications in this area (see Section 4.1).

To address the problems related to the reluctance to share sensitive data on experienced incidents [1, 8, 24], an anonymity architecture (see Section 4.5) and data sanitisation mechanisms (see Section 4.2) are introduced. The architecture takes advantage of the mobile agents paradigm that is particularly suitable for the deployment in heterogeneous environments, such as the energy sector. Data sanitisation, on the other hand, enables maintaining a proper equilibrium between security and usefulness of exchanged data. Cybersecurity requirements brought out specifically for the energy sector's information sharing platform are described in Section 4.4.

## 4.1. Data model

Creating a data model is an essential stage of the information sharing platform development as it enables identifying the types of data exchanged in the platform, facilitates the communication between the developers and the future users of the platform and supports the design of other functionalities such as data sanitisation or aggregation (see Sections 4.2 and 4.3). When developing the data model for the energy sector, particular characteristics related to the heterogeneity and geographical dispersion of participants and the broad presence of machinegenerated data needed to be addressed. The participants of the information sharing come from various environments including industrial, regulatory or academic (see Fig. 5), implement diverse business models and represent diferent (sometimes contradictory) interests. They are situated in dispersed, often remote locations. These conditions constrain eficient communication between all stakeholders, especially in the form of physical meetings. At the same time, such communication is prerequisite for agreeing on the types and format of exchanged data. The machine-generated data that need to be embraced by the model are primarily the technical and operational security data processed by SANs and security tools. To address these challenges a new approach to data model development that combines the classical data modelling methodology with an adaptation of the iterative and incremental software development model was proposed [69, 70]. Based on the approach, a data model that consists of three-level representations (very high-level data model, high-level data model and logical data model) was created [69. 70],

## 4.2. Data sanitisation

While at the situation awareness level, detailed, technical data on events are highly desirable to enable appropriate reaction, when the data are to be shared in the ISP, the high level of detail may undermine security. Precise data with computer identifiers and addresses, protocols and ports that are indispensable during low-level security processing, when delivered to all information sharing participants could open up opportunities for misuse. Data sanitisation is a method for maintaining a balance between security and usefulness of shared data by removing or altering its sensitive parts. Its significant advantage is that it does not utilise cryptography, which makes it particularly suitable for the energy sector, where cryptographic key management is hindered due to the number and diversity of computer systems and devices.

Several techniques of data sanitisation are available. In generalisation, data are replaced with a range of possible values [71], Bloom filters are one-way data structures used for protecting IP addresses [46], while data cubes hash the addresses of observables to a limited set of coordinates, and represent intensity of observables as two-dimensional values, and time as a third dimension [72]. Moreover, variants of the methods are often available. Generalisation methods include suppression – omitting a sensitive datum [73], deletion – removing a value [71], aggregation – categorising a datum with other data [73] or number variance – modifying each number value by a random percentage of its original value [74].

Sanitisation rules were specified for each entity of the ISP data model (see Section 4.1) at two sanitisation levels. The low level regards the sanitisation of the most sensitive data. High-level sanitisation, on the other hand, aims at protecting also the data which could potentially provide some indirect indications to an attacker, who based on additional knowledge, could infer the value of critical data. Sample sanitisation rules are presented in Tables 3 and 4.

Table 3  
Sanitisation rules for the Method data model entity.

<table><tr><td>Title</td><td colspan="3">Method</td></tr><tr><td>Description</td><td colspan="3">The entity provides information about a method used by an attacker in the form of a reference to a vulnerability or exploit database or a free-form description.</td></tr><tr><td>Field</td><td>Description</td><td colspan="2">Sanitisation</td></tr><tr><td></td><td></td><td>Low</td><td>High</td></tr><tr><td>Type</td><td>Type of the method e.g. DDoS, virus, stack-overflow</td><td>No</td><td>No</td></tr><tr><td>Name</td><td>Name of the method</td><td>No</td><td>No</td></tr><tr><td>Description</td><td>A brief description of the method (Full description should be shared as a separate document.)</td><td>No</td><td>No</td></tr></table>

Table 4  
Sanitisation rules for the Attack data model entity.

<table><tr><td>Title</td><td colspan="3">Attack</td></tr><tr><td>Description</td><td colspan="3">The entity contains information about the security events that constitute an incident.</td></tr><tr><td>Field</td><td>Description</td><td colspan="2">Sanitisation</td></tr><tr><td></td><td></td><td>Low</td><td>High</td></tr><tr><td>Description</td><td>The time when the incident activity was first detected by the reporter. In the case of more than one event, the time the first event was detected.</td><td>No</td><td>Yes</td></tr></table>

## 4.3. Data aggregation

The volumes of data automatically generated by situation awareness networks and security tools (see Section 4.1) can be very excessive and contain large amounts of redundant information. This hinders their analyses by human operators. Data aggregation algorithms help in resolving this issue. The development of aggregation algorithms included the selection of grouping attributes, i.e. the data entities for which identical or similar values (depending on the selected criteria) in distinct messages would result in aggregating the messages. Examples of grouping attributes include the attack source, the targeted service or the attack method. The next step was to map the selected attributes to the appropriate entities in the data model, taking into account that the aggregation can be possible only if grouping attributes have not been previously sanitised (see Section 4.2). In the algorithms, the appropriate setting of the maximum time between incidents (MTBI) attribute plays an key role as it is used to determine whether an incident can be treated as part of a previously detected attack. For instance, an attack lasting 90 min, would be recognised as two independent incidents, if the MTBI was set to an hour. For each grouping attribute, a separate MTBI can be adjusted. An example of the aggregation algorithm is presented in Fig. 2.

## 4.4. Cybersecurity requirements

Cybersecurity requirements for the information sharing platform are categorised into 15 categories that include anonymity and data sanitisation, data input and output validation, database protection, passwords or error handling. The requirements were elicited based on the study that comprised the identification of available security requirements for alternative security information exchange platforms dedicated to other sectors, the review of the literature on security require ments engineering and the analysis of the available sources of security requirements for web applications, content management systems and databases [75].

![](/api/attachments/BJA44NKQ/fulltext/images/57f25341b783c2e5d6fa42bd25ccdcd9dc2cdfe274ef8e0bca1e67c908a02c98.jpg)  
Fig. 2. Data aggregation algorithm for the attack method data fields. MTBI depicts the maximum time between incidents.

## 4.5. Anonymisation mechanisms

To encourage the exchange of even highly sensitive information between platform participants anonymisation mechanisms were introduced. They protect the identity of information senders by concealing all personally identifiable information (PII) and by mitigating sophisticated communication analysis techniques for revealing the identity (trafic analysis) [76]. A mobile agent-based anonymity architecture described in [76-78] was adapted to the ISP. The architecture consists of two modules. Module I: Untraceability Protocol Infrastructure forms an integral part of the architecture that realises an untraceability protocol to ensure that the address of a message sender to the ISP is obfuscated. Module II: Additional Untraceability Support is optional. It aims at protecting anonymity from lower-probability attacks that require substantial resources and skills from an attacker. Before enabling this component, a cost-benefit analysis is advised as the module can impose a noticeable overhead on the platform [79]. To enable efective protection, the anonymity architecture should be deployed in multiple, widely dispersed network locations [80]. In the energy sector this requirement is inherently supported (see Section 4.1).

Table 5  
Test documents' types (bold-typed) and main content components developed during the evaluation process [83].

<table><tr><td>Test plan</td><td>Test case</td><td>Test procedure</td></tr><tr><td>Test objectives</td><td>Test items</td><td>Purpose</td></tr><tr><td>Testing tasks</td><td>Input/output specifications</td><td>Procedure steps</td></tr><tr><td>Testing schedule</td><td>Environmental needs</td><td></td></tr></table>

## 5. Evaluation

The aim of the evaluation was to verify correct functioning and interoperation of SAN components as well as the efectiveness and efficiency of human-computer interactions involved in the information exchange, before the deployment of the solution in the EE-ISAC en vironment. To achieve this objective, integration (see Section 5.3) tests and usability (Section 5.4) were performed in the laboratory settings (Section 5.2).

To assure a systematic, repeatable and reusable testing process [81, 82], test plans and standardised test specifications [83] including the descriptions of test cases and test procedures were developed before the tests' execution. The main elements of the specifications are summarised in Table 5. In addition, to enable comparability, validity and usability of the assessment results [81], appropriate testing metrics were designed before the evaluation (see Section 5.1).

## 5.1. Testing metrics

To enable measurable results of the evaluation, a set of metrics applicable to situation awareness networks and information sharing platforms was proposed [58, 60]. During the metrics' elicitation process, the selection criteria related to achieving measurement consistency, numerical representation, economic and the straightforward implementation in the SA and ISP context [84] were applied. The metrics are grouped into three categories: testing process metrics, cybersecurity metrics and usability metrics. While the first two groups concentrate on the technical aspects of the evaluated products and include metrics such as source code coverage or test case defect density [58, 60], the third group contains the metrics most closely-related to the decision-making process. Selected metrics from this group are presented in Table 6. Section 5.4 contains sample results obtained with the metrics (see Figs. 3 and 4).

## 5.2. Testing environment

The evaluation was carried out in two testing laboratories. The situation awareness network was tested in the cybersecurity laboratory of the Enel Engineering and Research located in the power plant area of Livorno. The laboratory was designed to support reconstruction of realworld computer systems that operate in power sector facilities. It is primarily dedicated to the assessments of industrial control applications and comprises the relevant devices and software, such as programmable logic controllers or distributed control systems provided by various vendors. The structure of the computer network in the laboratory is based on the power plant's. The physical part of the cyber-physical system consists of field devices (pressure meters, valves, pumps etc.) deployed over the physical equipment (tanks, pipes, heaters, turbines) and controlled by programmable logic controllers. It replicates the closed-water cycle analogous to that associated with electric power generation.

Selected usability metrics applied during the evaluation process.

<table><tr><td>Metric</td><td>Symbol</td><td>Description</td></tr><tr><td>Task success</td><td>TS</td><td>The level of task completion (succeed/failed) [85]</td></tr><tr><td>Time on task</td><td>TT</td><td>Time required to complete a specific task [85]</td></tr><tr><td>Task ease</td><td>TE</td><td>The difficulty of the task [86]</td></tr><tr><td>Attractiveness</td><td>A</td><td>The capability of a program to be attractive to the user [87]</td></tr><tr><td>Credibility</td><td>C</td><td>The level of trust that the program provides the given functionality</td></tr></table>

![](/api/attachments/BJA44NKQ/fulltext/images/9af9abd33d103977709e568db6fa219eaf9a9d2aa31fa825f032f2c63330dea0.jpg)  
Fig. 3. The average values of the Task Success, Task Ease, Attractiveness and Credibility metrics obtained during the usability tests. Performed tasks included message sending (MS) and installation (I), while evaluated functionalities were related to the graphical user interface (GUI), anonymisation (A) and message publishing (MP).

![](/api/attachments/BJA44NKQ/fulltext/images/c42ba94c3755a2c032ac5332890c8ba8da8161964707df3bbd4c3b6eeb1d9812.jpg)  
Fig. 4. The average values (in the format: minutes:seconds) of the Time on Task metric obtained during the usability tests. Performed tasks included installation (I), sending a message (MS1), sending the second message (MS2). T – indicates total time.

The tests of the information sharing platform, where human interactions are strongly involved, were performed in the laboratory at Gdańsk University of Technology. The infrastructure utilised in tests consisted of several interconnected desktop computers with JADE agent platform, VirtualBox’es for computer systems emulation, Vagrant development environments management software, Wordpress content management system (CMS) to reflect information sharing activities, Eclipse software development environment, Maven software project management framework that supports project integration and unit testing, and the Git version-control system.

![](/api/attachments/BJA44NKQ/fulltext/images/1f2e21bbf4a563c0d4ed3272d8c8baefe75d12b9d57534b81313e302f7a1894a.jpg)  
Fig. 5. Communities within EE-ISAC.

## 5.3. Integration tests

To verify flawless interoperation of SAN components, integration tests were performed. Based on the designed test cases, the interactions between the dashboard and network sensors, integration of SIEM and an intrusion detection system and communication between all tiers of the SAN architecture (see Section 3.1) i.e. complete SAN integration were examined.

As far as the dashboard integration with network sensors is concerned, several issues relevant to the processing and visualisation of large amounts of data were identified. Based on the outcome of the tests, feedback to developers was provided that helped in identifying and fixing the related platform flaws.

The tests of the installation and configuration of SIEM and an in trusion detection system to work in a collaborative manner were passed successfully. However, testing of the cooperation among the two systems in a larger-scale environment revealed problems with commu nication between diferent subnetworks. This was a critical issue, as in target environments sensors will be dispersed across regions and countries, and their stable and secure connection with the SIEM is in dispensable for providing situational awareness.

The last group of test cases concerned the evaluation of the complete integration of SAN components (see Section 3.1). Communication through all SAN tiers was examined. The data collected by sensors were delivered to SIEM, where, after the application of data processing and analysis algorithms (see Section 3.3), alerts were issued and notification messages were sent to the dashboard. The information about detected threats was visualised to a human operator using dashboard widgets. During the tests, several minor issues and flaws were identified, however the overall SAN design proved correct.

## 5.4. Usability tests

Usability tests aimed at assessing the efectiveness and eficiency of anonymous sharing of cyberincident information as well as the associated user satisfaction [85, 86]. During the evaluation, performance of fundamental information sharing tasks using the anonymity architecture (see Section 4.5) and Tor Browser – the most popular anonymisation tool available on the Internet was compared. 11 participants were provided with descriptions of the tasks and the questionnaires composed of 14 closed-ended and one open-ended question. The questionnaires were derived from System Usability Scale (SUS), Soft ware Usability Measurement Inventory (SUMI), Computer System Usability Questionnaire (CSUQ) and Website Analysis and MeasureMent Inventory (WAMMI). Usability perceptions were measured using the Likert scale. Aggregated results of the evaluation for the Task Success (TS), Time on Task (TT), Task Ease (TE), Attractiveness (A) and Credibility (C) metrics (see Table 6) are presented in Figs. 3 and 4.

![](/api/attachments/BJA44NKQ/fulltext/images/b1a978617ff9fac28cd1c702e9c2555f3fe9f7417e9593c58d20d2d4f3bdb24c.jpg)  
Fig. 6. The EE-ISAC's information sharing platform at work

All users were able to complete the given tasks associated with information exchange (TS). While the perceived ease of use (TE) and credibility (C) of both platforms were practically similar, most users ranked higher the graphical user interface (A) of the Tor browser than the anonymity architecture's (see Fig. 3). This clearly indicates the area of further improvements of the architecture. At the same time, the tests showed that the anonymity architecture performed better in anonymous message sending tasks (TT) (see Fig. 4).

## 6. Deployment

The original vision of the EE-ISAC was to join forces across the whole energy supply chain and improve awareness among all stakeholders. Building trusting relationships among members of this newly formed network was crucial for optimal information sharing and collaboration. This was achieved through steady growth in member numbers and emphasising the requirement for member organisations to specify just one or two representatives to attend physical meetings without substitution. This enabled a trust of the EE-ISAC space to grow among the same people attending meetings regularly. As a result, close working relations to develop and encourage sharing of sensitive information during the EE-ISAC's closed member-only sessions have been established.

The careful building of a trusted network was an essential foundation to ensure the efective and appropriate use of platforms and tools ofered by the EE-ISAC and a willingness to engage with the unique collaborative opportunity that the EE-ISAC ofers. As far as the progress achieved so far with building membership, creating partnerships and forming working groups is concerned, 23 representatives of utilities, vendors, public bodies, academia and research labs have signed the membership, 10 task forces have been established, and mutual agreements have been signed with Japan and US E-ISACs.

During the development of the EE-ISAC it has been necessary to encourage the participation of utilities to keep the EE-ISAC's work and approach always tailored to the needs of energy utilities. Essential topic areas were chosen, and several technical working groups were formed to commence specific information sharing activities. This enabled focussed collaborative communities to form within the EE-ISAC to work together on the current issues, as demonstrated by Fig. 5.

In addition to holding regular member meetings, a digital sharing platform was launched, shown in Fig. 6, which takes advantage of the DEnSeK proposals (see Section 4). This is used for posting regular security bulletins and new information on threats and vulnerabilities. It also ofers a place for discussion among technical working groups. Members appreciate the added value of the EE-ISAC as a forum for discussing relevant topics and issues they all face.

The concepts described in Section 4 have also been implemented in the area of malware information sharing, with a core working group established for vetting of information to create threat intelligence tailored for the needs of the energy sector. Bi-directional access is now possible for members to both contribute to and consume the latest information (see Fig. 7).

## 7. Conclusions

Both. scientific and practical studies demonstrate that increased situational awareness and cyberincident information sharing constitute an efective tool for supporting cybersecurity decisions associated with the evolving threat landscape and sophistication of cyberattacks in the energy sector (see Section 2). Following this observation, two novel solutions were proposed, namely the cyberincident information sharing platform and a three-tier SAN (see Sections 4 and 3) that in comparison to the earlier contributions, support the operation on all cybersecurity levels, from technical to strategic and demonstrate a significant practical element, due to their application to the EE-ISAC. The novel pro posals include mechanisms that address the implementation and application problems related to the heterogeneity of processed data (Section 4.1), dificulties in their correlation and aggregation (Sections 3.3 and 4.3), or the user's reluctance to share them with other ISAC members (Sections 4.2 and 4.5). The solutions were evaluated experimentally, demonstrating correct functioning and integration of SAN components, as well as the eficiency of human-computer interactions involved in the information exchange (Section 5). Yet, at the same time they indicated certain areas of improvement, related for instance to the interface of the anonymity architecture.

![](/api/attachments/BJA44NKQ/fulltext/images/c7e8b98cb7cfc36c056a885ce8f22697cf0a656cf9ecf97fe835e24c1979545a.jpg)  
Fig. 7. EE-ISAC threat sharing.

However, the most important, real-world validation by the members of the EE-ISAC is on its course (Section 6). The initial experiences show that the sharing of cybersecurity knowledge enables better informed organisations to make more efective decisions on how to prepare and respond to modern cyberattacks. Significant progress has been made in the formation of the EE-ISAC and the establishment of a network of trust. This has fostered a unique environment for information sharing and collaborative opportunities, with the potential to become a significant enabler of improved resilience for the energy sector. The gradual evolution of EE-ISAC and partnerships with other ISACs is forming a joined-up response for the energy sector to face threats together. Attending to the cybersecurity needs of utility members, the EE-ISAC has recognised the importance of broadening their situation awareness network through developing global partnerships. The EE-ISAC has begun peer-to-peer interactions mentioned in Section 4, through twoway information sharing with partners in the USA and Japan. This has encouraged plans to work towards a future vision of 24 × 7 decision support across three time zones in the USA, Europe and Japan. This opportunity will explore and define appropriate and necessary information sharing and analysis between utilities and between nations for the energy sector. There is also work ongoing to support the cybersecurity capabilities of smaller utilities, cross-sector collaborations with other ISACs and to encourage the establishment of new energy ISACs in other areas. An important next step for this model will be an adaptation for appropriate sharing of data with other ISACs and also through the entire energy supply chain.

## Acknowledgments

The study presented in this paper is based on work carried out in the DEnSeK (Distributed Energy Security Knowledge) project founded by the European Commission, Directorate-General for Home Afairs (Programme, Prevention, Preparedness and Consequence Management of Terrorism and other Security-related Risks – CIPS, Project Reference: HOME/2012/CIPS/AG/4000003772M) and partially supported from the project funds. It is also supported by the DS Programs of Faculty of Management and Economics and Faculty of Electronics, Telecommunications and Informatics of Gdańsk University of Technology. The EE-ISAC have also supported this paper through their experiences with implementing the ISP and SAN.

## References

[1] W. Tounsi, H. Rais, A survey on technical threat intelligence in the age of sophisticated cyber attacks, Computers and Security 72 (2018) 212–233, https://doi.org 10.1016/i.cose.2017.09.001.

[2] F. Skopik, G. Settanni, R. Fiedler, A problem shared is a problem halved: a survey on the dimensions of collective cyber defense through security information sharing, Computers and Security 60 (2016) 154–176, https://doi.org/10.1016/j.cose.2016. 04.003.

[3] J. Chen, C. Su. K.H. Yeh, M. Yung, Special issue on advanced persistent threat Futur. Gener. Comput. Syst. 79 (2018) 243–246, https://doi.org/10.1016/J. FUTURE 2017.11.005

[4] C.C. Sun, A. Hahn, C.C. Liu, Cyber security of a power grid: state-of-the-art, International Journal of Electrical Power & Energy Systems 99 (2018) 45–56, https://doi.org/10.1016/J.IJEPES.2017.12.020.

[5] R. Knights, E. Morris, Move to intelligence-driven security, Netw. Secur. 2015 (8) (2015) 15–18, https://doi.org/10.1016/S1353-4858(15)30071-4.

[6] M. Marchetti, F. Pierazzi, M. Colajanni, A. Guido, Analysis of high volumes of

network trafic for advanced persistent threat detection, Comput. Netw. 109 (2016) 127-141, https://doi.org/10.1016/ji.comnet.2016.05.018

[7] M. Conti, T. Dargahi, A. Dehghantanha, Cyber Threat Intelligence: Challenges and Opportunities, Springer International Publishing, Cham, 2018, pp. 1–6, https://doi. org/10.1007/978-3-319-73951-9\_1.

[8] S.E. Jasper, U.S. Cyber Threat intelligence sharing frameworks, International Journal of Intelligence and CounterIntelligence 30 (1) (2017) 53–65, https://doi. org/10.1080/08850607.2016.1230701.

[9] I. Friedberg, F. Skopik, G. Settanni, R. Fiedler, Combating advanced persistent threats: from network event correlation to incident detection, Computers & Security 48 (2015) 35–57, https://doi.org/10.1016/j.cose.2014.09.006 arXiv:41.

[10] R. Leszczyna, Cybersecurity in the Electricity Sector, Springer, 2019, http://www. springer.com/978-3-030-19537-3 arXiv:41.

[11] A. Lohachab, B. Karambir, Critical analysis of DDos–an emerging security threat over IoT networks, Journal of Communications and Information Networks 3 (3) (2018) 57–78, https://doi.org/10.1007/s41650-018-0022-5

[12] D. Anstee, Preparing for tomorrow's threat landscape, Network Security 2015 (8) (2015) 18–20, https://doi.org/10.1016/S1353-4858(15)30072-6.

[13] L.P. Rees, J.K. Deane, T.R. Rakes, W.H. Baker, Decision support for cybersecurity risk planning, Decision Support System 51 (3) (2011) 493–505, https://doi.org/10. 1016/i.dss,2011.02.013

[14] T. Sawik, Selection of Cybersecurity Safequards Portfolio, Springer International Publishing, Cham, 2018, pp. 315–335, https://doi.org/10.1007/978-3-319-58823- 0\_11.

[15] C. Di Sarno, A. Garofalo, I. Matteucci, M. Vallini, A novel security information and event management system for enhancing cvber security in a hydroelectric dam International Journal Critical Infrastructure Protection 13 (2016) 39–51, https:// doi.org/10.1016/i.jicip.2016.03.002.

[16] ENISA, Report on cyber security information sharing in the energy sector, Tech. Rep. 2016 https://www.enisa.europa.eu/publications/information-sharing-in-the energy-sector.

[17] L. Coppolino, S. D’Antonio, V. Formicola, L. Romano, A framework for mastering heterogeneity in multi-layer security information and event correlation, Journal System Architecture 62 (2016) 78–88, https://doi.org/10.1016/j.sysarc.2015.11. 010.

[18] D. Howell, Building better data protection with SIEM, Computer Fraud & Security 2015 (8) (2015) 19–20, https://doi.org/10.1016/S1361-3723(15)30077-4.

[19] K.M. Moriarty, Incident coordination, IEEE Security Privacy 9 (6) (2011) 71–75, https://doi.org/10.1109/MSP.2011.164.

[20] G.P. Tadda, J.S. Salerno, S. Jajodia, P. Liu, V. Swarup, C. Wang, Overview of cyber situational awareness, Cyber Situational Awareness, Advances in Information Security, vol. 46, Springer, US, Boston MA, 2010, pp. 15–35, , https://doi.org/10. 1007/978-1-4419-0140-8 http://link.springer.com/10.1007/978-1-4419-0140-8.

[21] M.R. Endsley, D.J. Garland, Situation Awareness Analysis and Measurement, CRC Press, Inc., 2000.

[22] U. Franke, J. Brynielsson, Cyber situational awareness - a systematic review of the literature, Computers and Security 46 (2014) 18–31, https://doi.org/10.1016/j. cose.2014.06.008 arXiv:72.

[23] T. Sawik, Selection of optimal countermeasure portfolio in IT security planning, Decision Support System 55 (1) (2013) 156–164, https://doi.org/10.1016/j.dss. 2013.01.001

[24] J.M. de Fuentes, L. González-Manzano, J. Tapiador, P. Peris-Lopez, PRACIS: privacy-preserving and aggregatable cybersecurity information sharing, Computers and Security 69 (2017) 127–141. https://doi.org/10.1016/i.cose,2016.12.011.

[25] J.L. Hernandez-Ardieta, G. Suarez-Tangil, J.E. Tapiador, Information sharing models for cooperative cyber defence, 2013 5th International Conference on Cyber Conflict, 2013, pp. 60–87, , https://doi.org/10.1016/j.pupt.2014.10.005.

[26] M. He, L. Devine, J. Zhuang, Perspectives on cybersecurity information sharing among multiple stakeholders using a decision-theoretic approach, Risk Analysis 38 (2) (2018) 215–225, https://doi.org/10.1111/risa.12878 http://doi.wiley.com/10 1111/risa.12878.

[27] L.A. Gordon, M.P. Loeb, W. Lucyshyn, Sharing information on computer systems security: an economic analysis, Journal Accounting and Public Policy 22 (6) (2003) 461–485. https://doi,org/10.1016/i.jaccpubpol.2003.09.001

[28] E. Gal-Or, A. Ghose, The economic incentives for sharing security information. Information Systems Research 16 (2) (2005) 186–208, https://doi.org/10.1287/ isre 1050.0053

[29] K. Hausken, Information sharing among firms and cyber attacks, Journa Accounting and Public Policy 26 (6) (2007) 639–688, https://doi.org/10.1016/j. jaccpubpol.2007.10.001.

[30] D. Liu, Y. Ji, V. Mookerjee, Knowledge sharing and investment decisions in information security, Decision Support System 52 (1) (2011) 95–107, https://doi.org 10.1016/i.dss.2011.05.007.

[31] D. Tosh, S. Sengupta, C.A. Kamhoua, K.A. Kwiat, Establishing evolutionary game models for CYBer security information EXchange (CYBEX), Journal of Computer and System Science 98 (July 2016) (2018) 27–52, https://doi.org/10.1016/j.jcss. 2016.08.005

[32] I. Vakilinia, S. Sengupta, A coalitional game theory approach for cybersecurity information sharing, Proceedings - IEEE Military Communications Conference MILCOM 2017-Octob, 2017, pp. 237–242, , https://doi.org/10.1109/MILCOM. 2017.8170845

[33] D. Tosh, S. Sengupta, C. Kamhoua, K. Kwiat, A. Martin, An evolutionary gametheoretic framework for cvber-threat information sharing, JEEE International Conference on Communications 2015-Septe, 2015, pp. 7341–7346, , https://doi. org/10.1109/ICC.2015.7249499.

[34] A. Ghose, K. Hausken, A strategic analysis of information sharing among cyber

attackers, Journal of Information Systems and Technology Management 12 (2) (2015) 245–270, https://doi.org/10.2139/ssrn.928138.

[35] M.E. Nikoofal, J. Zhuang, On the value of exposure and secrecy of defense system: first-mover advantage vs. robustness, European Journal of Operational Research 246 (1) (2015) 320–330, https://doi.org/10.1016/j.ejor.2015.04.043 http://www. sciencedirect.com/science/article/pii/S0377221715003367.

[36] J. Zhuang, V.M. Bier, O. Alagoz, Modeling secrecy and deception in a multiple period attacker-defender signaling game, European Journal of Operational Research 203 (2) (2010) 409–418, https://doi.org/10.1016/j.ejor.2009.07.028.

[37] J. Zhuang, V.M. Bier, Reasons for secrecy and deception in homeland-security resource allocation, Risk Analysis 30 (12) (2010) 1737–1743, https://doi.org/10. 1111/j.1539-6924.2010.01455.x.

[38] N.S. Dighe, J. Zhuang, V.M. Bier, Secrecy in defensive allocations as a strategy for achieving more cost-efective attacker deterrence, International Journal of Performability Engineering 5 (1) (2009) 31–43 https://paris.utdallas.edu/IJPE/ Vol05/Issue01/VOL5N1P3LLKJ.pdf

[39] E.M. Sedenberg, D.K. Mulligan, Public health as a model for cybersecurity information sharing, Berkeley Technology Law Journal, https://dx.doi.org/10.3945/ ajcn.115.110825.Reply.

[40] K.V. Impe, How STIX, TAXII and CybOX Can Help With Standardizing Threat Information, (2015), https://doi.org/10.1039/b926102h.

[41] F. Fransen, A. Smulders, R. Kerkdijk, Cyber security information exchange to gain insight into the efects of cyber threats and incidents, e & i Elektrotechnik und Informationstechnik 132 (2) (2015) 106–112, https://doi.org/10.1007/s00502- 015-0289-2 http://link.springer.com/10.1007/s00502-015-0289-2

[42] S. Qamar, Z. Anwar, M.A. Rahman, E. Al-Shaer, B.T. Chu, Data-driven analytics for cyber-threat intelligence and information sharing, Computers and Security 67 (2017) 35–58, https://doi.org/10.1016/j.cose.2017.02.005.

[43] R. Bourgue, J. Budd, J. Homola, M. Wlasenko, D. Kulawik, Detect, SHARE, protect solutions for improving threat data exchange among CERTs, Tech. Rep. October 2013 https://www.enisa.europa.eu/publications/detect-share-protect-solutionsfor-improving-threat-data-exchange-among-certs.

[44] I. Vakilinia, Privacy-preserving cybersecurity information exchange mechanism, Proceedings - 2017 International Symposium on Performance Evaluation of Computer and Telecommunication Systems (SPECTS), 2017, pp. 1–7, , https://doi. org/10.23919/SPECTS.2017.8046783.

[45] S. Jajodia, S. Noel, P. Kalapa, M. Albanese, J. Williams, Cauldron: mission-centric cyber situational awareness with defense in depth, Proceedings - IEEE Military Communications Conference MILCOM, 2011, pp. 1339–1344, , https://doi.org/10. 1109/MULCOM.2011.6127490

[46] M.E. Locasto, J.J. Parekh, A.D. Keromytis, S.J. Stolfo, Towards collaborative security and P2P intrusion detection, Proceedings from the 6th Annual IEEE System, Man and Cybernetics Information Assurance Workshop, SMC 2005, vol. 2005, 2005, pp. 333–339, , https://doi.org/10.1109/IAW.2005.1495971.

[47] T. Zhang, Q. Zhu, Distributed privacy-preserving collaborative intrusion detection systems for VANETs, IEEE Transactions on Signal and Information Processing over Networks 4 (1) (2018) 148–161, https://doi,org/10.1109/TSIPN.2018.2801622

[48] A. Patel, H. Alhussian, J.M. Pedersen, B. Bounabat, J.C. Júnior, S. Katsikas, A nifty collaborative intrusion detection and prevention architecture for smart grid ecosystems, Computers and Security 64 (2017) 92–109, https://doi.org/10.1016/j. cose,2016.07.002.

[49] T. Abdellatif. M. Mosbah. Efficient monitoring for intrusion detection in wireless sensor networks, Concurrency and Computation: Practice and Experience (2017) e490z. https://doi.org/10.1002/cpe.4907 https://onlinelibrary.wilev.com/doi abs/10.1002/cpe.4907.

[50] X. Liu, P. Zhu, Y. Zhang, K. Chen, A collaborative intrusion detection mechanism against false data injection attack in advanced metering infrastructure, IEEE Transactions on Smart Grid 6 (5) (2015) 2435–2443. https://doi,org/10.1109/TSG 2015.2418280

[51] S. Jajodia, P. Liu, V. Swarup, C. Wang, ECOSSIAN, Cyber Situational Awareness: Advances in Information Security, (2010), https://doi.org/10.1007/978-1-4419- 0140-8.1.

[52] ECOSSIAN, European COntrol System Security Incident Analysis Networ (ECOSSIAN) Proiect Website. http://ecossian.eu/.

[53] H. Kaufmann, R. Hutter, F. Skopik, M. Mantere, A structural design for a Pan European early warning system for critical infrastructures, e & i Elektrotechnik und Informationstechnik 132 (2) (2015) 117–121, https://doi.org/10.1007/s00502- 015-0286-5 http://link.springer.com/10.1007/s00502-015-0286-5

[54] R. Barth, S. Meyer-Nieberg, S. Pickl, M. Schuler, J. Wellbrink, Proceedings of the Symposium on Emerging Applications of M&S in Industry and Academia Symposium, 2012 EAIA. 2012, pp. 106–113 http://dl.acm.org/citation.cfm?id= 2338790.2338793.

[55] R. Klump, M. Kwiatkowski, Distributed IP watchlist generation for intrusion de tection in the electrical smart grid, IFIP Advances in Information and Communication Technology 342 AICT (2010) 113–126, https://doi.org/10.1007 978-3-642-16806-2.8

[56] M. Brunner, H. Hofinger, C. Roblee, P. Schoo, S. Todt, Anonymity and privacy in distributed early warning systems, Lecture Notes in Computer Science (Including Subseries Lecture Notes in Artificial Intelligence and Lecture Notes in Bioinformatics), LNCS, vol. 6712, Springer, Berlin, Heidelberg, 2011, pp. 81–92, , https://doi.org/10.1007/978-3-642-21694-7\_7 http://link.springer.com/10.1007/ 978-3-642-21694-7 7.

[57] C. Alcaraz, J. Lopez, Wide-area situational awareness for critical infrastructure protection, Computer 46 (4) (2013) 30–37, https://doi.org/10.1109/MC.2013.72

[58] D. Bolzoni, R. Leszczyna, M.R. Wróbel, M. Wrobel, Situational awareness network for the electric power system: the architecture and testing metrics, in: M. Ganzha,

L. Maciaszek, M. Paprzycki (Eds.), Proceedings of the 2016 Federated Conference on Computer Science and Information Systems, FedCSIS 2016, IEEE, 2016, , https://doi.org/10.15439/2016F50.

[59] R. Leszczyna, M.R. Wrobel, Evaluation of open source SIEM for situation awareness platform in the smart grid environment, 2015 IEEE World Conference on Factory Communication Systems (WFCS), IEEE, 2015, , https://doi.org/10.1109/WFCS. 2015.7160577.

[60] R. Leszczyna, R. Małkowski, M.R. Wróbel, Testing situation awareness network for the electrical power infrastructure, Acta Energetica 3 (28) (2016) 81–87, https:// doi.org/10.12736/issn.2300-3022.2016308.

[61] Science Applications International Corporation, Intrusion detection system system protection profile version 1.4, Tech. Rep. 2002 https://www.commoncriteriaportal. org/files/ppfiles/pp\_ids\_sys\_v1.4.pdf.

[62] Science Applications International Corporation, Intrusion detection system sensor protection profile version 1.2, Tech. Rep. National Security Agency, Columbia, 2005. https://www.niap-cceys.org/MMO/PP/pp ids sen v1.2.pdf

[63] Science Applications International Corporation, Intrusion detection system scanner protection profile version 1.2, Tech. Rep. National Security Agency, Columbia, 2005, https://www.niap-ccevs.org/MMO/PP/pp\_ids\_sca\_v1.2.pdf.

[64] Science Applications International Corporation, Intrusion detection system analyzer protection profile version 1.2, Tech. Rep. National Security Agency, Columbia, 2005, https://www.niap-ccevs.org/MMO/PP/pp\_ids\_ana\_v1.2.pdf.

[65] R. Leszczyna, Standards on cyber security assessment of smart grid, International Journal of Critical Infrastructure Protection 22 (2018) 70–89, https://doi.org/10. 1016/i.iicip.2018.05.006 http://www.sciencedirect.com/science/article/pii/ S1874548216301421.

[69] R. Leszczyna. M.R. Wróbel. Data model development for security information sharing in smart grids, International Journal for Information Security Research 4 (2014) 479–489 http://infonomics-society.org/wp-content/uploads/ijisr/ published-papers/volume-4-2014/Data-Model-Development-for-Security-Information-Sharing-in-Smart-Grids.pdf.

[70] R. Leszczyna, M.R. Wrobel, Security information sharing for smart grids: developing the right data model, The 9th International Conference for Internet Technology and Secured Transactions (ICITST-2014), IEEE, 2014, pp. 163–169, , https://doi.org/ 10.1109/ICITST.2014.7038798.

[71] M. Bishop, J. Cummins, S. Peisert, A. Singh, B. Bhumiratana, D. Agarwal, D. Frincke, M. Hogarth. Relationships and data sanitization: a study in Scarlet. Proceedings of the 2010 Workshop on New Security Paradigms, 2010, pp. 151–164 , https://doi.org/10.1145/1900546.1900567.

[72] A. Valdes, M. Fong, K. Skinner, Data Cube Indexing of Large-Scale Infosec Repositories, http://www.csl.sri.com/papers/AusCERT\_2006/, (2006).

[73] R. Crawford, M. Bishop, B. Bhumiratana, L. Clark, K. Levitt, Sanitization models and their limitations, Proceedings of the 2006 Workshop on New Security Paradigms, 2007, pp. 41–56, , https://doi.org/10.1145/1278940.1278948.

[74] D. Edgar, Data sanitization techniques, Tech. Rep. Net 2000 (2004) http://www. orafaq.com/papers/data\_sanitization.pdf.

[75] R. Leszczyna, M.R.M. Wrobel, R. Malkowski, Security requirements and controls for incident information sharing in the Polish power system, Proceedings - 2016 10th International Conference on Compatibility, Power Electronics and Power Engineering, CPE-POWERENG 2016, 2016, pp. 94–99, , https://doi.org/10.1109/ CPE,2016.7544165

[76] R. Leszczyna. Anonymity architecture for mobile agent systems, in: V. Mařík (Ed.) Holonic and Multi-Agent Systems for Manufacturing, Lecture Notes in Computer Science, vol. 4659, Springer Berlin Heidelberg, Heidelberg, Germany, 2007, pp. 93–103, , https://doi.org/10.1007/978-3-540-74481-8\_10 http://link.springer. com/10.1007/978-3-540-74481-810.

[77] R. Leszczyna, J. Górski, An untraceability protocol for mobile agents and its en hanced security study, 15th EICAR Annual Conference Proceedings, Hamburg, Germany, 2006, pp. 26–37.

[78] R.R. Leszczyna, J. Górski, Untraceability of mobile agents, Proceedings of the Fourth International Joint Conference on Autonomous Agents and Multiagent Systems - AAMAS '05 3. 2005, p. 1233. . https://doi,org/10.1145/1082473. 1082709 http://portal.acm.org/citation.cfm?doid=1082473.1082709.

[79] R. Leszczyna, J. Górski, P. Stone, G. Weiss, Performance analysis of untraceability protocols for mobile agents using an adaptable framework, in: P. Stone, G. Weiss

(Eds.), Proceedings of the 4th International Joint Conference on Autonomous Agents and Multiagent Systems (AAMAS ’05), vol. 2006, Association for Computing Machinery (ACM) Press, New York, NY, USA, 2006, p. 1063, , https://doi.org/10. 1145/1160633.1160824 http://portal.acm.org/citation.cfm?doid=1160633. 1160824.

[80] R. Leszczyna, M. Łosiński, R. Małkowski, Security information sharing for the Polish power system, Proceedings of the Modern Electric Power Systems 2015 - MEPS 2015, IEEE, London, United Kingdom, 2015, pp. 163–169, , https://doi.org/10. 1109/MEPS.2015.7477170.

[81] I. Burnstein, Practical software. Testing, Springer Professional Computing, Springer-Verlag, New York, 2003, https://doi.org/10.1007/b97392 http://link.springer. com/10.1007/b97392

[82] V. Garousi, M. Felderer, T. Hacaloğlu, Software test maturity assessment and test process improvement: a multivocal literature review, Information and Software Technology 85 (2017) 16–42, https://doi.org/10.1016/j.infsof.2017.01.001 http:/ www.sciencedirect.com/science/article/pii/S0950584917300162

[83] ISO/IEC/IEEE International Standard Software, Software and Systems Engineering Software Testing Part 3: Test Documentation. ISO/IEC/IEEIEEE 29119-3:2013(E). 2013, pp. 1–138, https://doi.org/10.1109/IEEESTD.2013.6588540.

[84] A. Jaquith, Security Metrics, Replacing Fear, Addison-Wesley Professional, Uncertainty, and Doubt. 2007.

[85] T. Tullis, B. Albert, Measuring the User Experience: Collecting, Analyzing, and Presenting Usability Metrics, 2nd ed., Elsevier Inc., Waltham, MA, USA, 2013.

[86] J. Sauro, J.R. Lewis, Quantifying the User Experience. Practical Statistics for User Research, 2nd ed., Elsevier Inc., Waltham, MA, USA, 2016arXiv:arXiv:1011. 1669v3.

[87] ISO/IEC, ISO/IEC 9126-1:2001 software engineering - product quality - part 1: quality model, Tech. Rep. ISO/IEC, 2001.

Dr Rafal Leszczyna is an assistant professor at Gdańsk University of Technology, Faculty of Management and Economics. He holds the MSc. degrees of Computer Science and Business Management. In December, 2006 he earned a Ph.D. in Computer Science, specialisation – Computer Security at the Faculty of Electronics. Telecommunications and Informatics of Gdansk University of Technology. Between 2004 and 2008 he worked in the European Commission Joint Research Centre, in the teams dealing with information security and the security of critical networked infrastructures. After his return to the university in 2008, from 2010 to 2012 he was seconded to the European Network and Information Security Agency (ENISA), where among the others he was responsible for coordinating the studies related to the security of industrial control systems and smart grids. His professional interests focus on the security of information systems, information security of critical infrastructures, and the issues relevant to information security management. Between 2013 and 2015 he was a project manager at Gdansk University of Technology of the DEnSeK project.

Dr Michaeł Wróbel is an assistant professor at Gdańsk University of Technology, Faculty of Electronics, Telecommunications and Informatics. He graduated from the faculty in 2002 with a degree in Computer Science, specialisation in Software Engineering and Databases, Until 2006. he worked as system administrator in several enterprises, in cluding CI TASK. Since 2006, he has worked at Faculty of Electronics, Telecommunications and Informatics. He received Ph.D. in Computer Science in 2011. Dr Wróbel's research interests include human aspects of software engineering and IT systems security. Currently, his research focuses on the role of emotions in software development process. He applies the afective computing methods to recognise and influence software developers emotions. Between 2013 and 2015 he was a member of the DEnSeK project.

Ms Tania Wallis is a researcher at the University of Strathclyde and the Power Networks Demonstration Centre, Since 201Z. she has been the Secretary of EE-ISAC. where she has been facilitating collaboration on Cybersecurity & Grid Resilience across Europe's energy sector. She holds MEnv degree from University of Melbourne and BEng (Hons) in Electronic & Electrical Engineering from University of Edinburgh. Her research interests include resilience analysis, cybersecurity issues influencing power systems architectures, considering human factors in risk assessments and interdependencies across the whole system and decentralised responsibility for cybersecurity across supply chains.
