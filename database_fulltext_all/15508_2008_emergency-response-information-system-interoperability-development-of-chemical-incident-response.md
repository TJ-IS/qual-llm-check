---
otero_id: 15508
otero_key: "Q7UBNQMG"
title: "Emergency Response Information System Interoperability: Development of Chemical Incident Response Data Model"
authors: "Rui Chen; Raj Sharman; Nirupama Chakravarti; H. Raghav Rao; Shambhu Upadhyaya"
year: "2008"
journal: "Journal of the Association for Information Systems"
doi: "10.17705/1jais.00153"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
4-2008

# Emergency Response Information System Interoperability: Development of Chemical Incident Response Data Model

Rui Chen , ruichen@buffalo.edu

Raj Sharman , rsharman@buffalo.edu

Nirupama Chakravarti , nc23@buffalo.edu

H. Raghav Rao , mgmtrao@buffalo.edu

Shambhu J. Upadhyaya , shambhu@cse.Buffalo.EDU

Follow this and additional works at: https://aisel.aisnet.org/jais

Recommended Citation Chen, Rui; Sharman, Raj; Chakravarti, Nirupama; Rao, H. Raghav; and Upadhyaya, Shambhu J. (2008) "Emergency Response Information System Interoperability: Development of Chemical Incident Response Data Model," , 9(3), . DOI: 10.17705/1jais.00153 Available at: https://aisel.aisnet.org/jais/vol9/iss3/7

This material is brought to you by the AIS Journals at AIS Electronic Library (AISeL). It has been accepted fo inclusion in Journal of the Association for Information Systems by an authorized administrator of AIS Electronic Library (AISeL). For more information, please contact elibrary@aisnet.org.

# Journal of the Association for Information Systems JAIS

Special Issue

Emergency Response Information System Interoperability: Development of Chemical Incident Response Data Model \*

Rui Chen Department of Management Science and Systems State University of New York at Buffalo ruichen@buffalo.edu

## Raj Sharman

Department of Management Science and Systems State University of New York at Buffalo rsharman@buffalo.edu

Nirupama Chakravarti Department of Computer Science and Engineering State University of New York at Buffalo nc23@buffalo.edu

H. Raghav Rao Department of Management Science and Systems Department of Computer Science and Engineering State University of New York at Buffalo mgmtrao@buffalo.edu

Shambhu J Upadhyaya Department of Computer Science and Engineering State University of New York at Buffalo shambhu@cse.buffalo.edu

## Abstract

Emergency response requires an efficient information supply chain for the smooth operations of intra- and interorganizational emergency management processes. However, the breakdown of this information supply chain due to the lack of consistent data standards presents a significant problem. In this paper, we adopt a theory-driven novel approach to develop an XML-based data model that prescribes a comprehensive set of data standards (semantics and internal structures) for emergency management to better address the challenges of information interoperability. Actual documents currently being used in mitigating chemical emergencies from a large number of incidents are used in the analysis stage The data model development is guided by Activity Theory and is validated through a RFC-like process used in standards development. This paper applies the standards to the real case of a chemical incident scenario. Further, it complies with the national leading initiatives in emergency standards (National Information Exchange Model)

Keywords: Emergency Response, Activity Theory, Data Model, Interoperability, Standards, XML

# Emergency Response Information System Interoperability: Development of Chemical Incident Response Data Model

## 1. Introduction

The 9/11 commission reports (Kean 2004) as well as analyses of Hurricane Katrina (Townsend 2006) explicate how inadequate emergency response management is a major factor contributing to the lack of an effective response. Among the factors accountable for the observed inadequacy, the response information supply chain (ISC) that connects the response operations and stakeholders has been recognized for its critical role in supporting an effective response during critical incidents (Aylward et al. 2006; DHS et al. 2006; Frale 2005; Harrison et al. 2006; Weinshel 2006). While an efficient ISC demands smooth and seamless interoperability, the reality is that there are no standards that cater to specific types of incidents such as fire or chemical incidents. The efforts of bodies such as the Department of Homeland Security, Department of Justice, and Organization for the Advancement of Structured Information Standards (OASIS) have focused primarily on standards of a more general nature dealing with emergency management issues (e.g., call alert). These have been top-down impositions of standards. However, incidents of specific types and day-to-day operations are handled mostly at local levels (Chen et al. 2005; Chen et al. 2007a). They are typically governed by local regulations and practices and are managed through collaboration with first and second responder communities from neighboring counties and towns (Bui et al. 2001; Chen et al. 2007b; Kim et al. 2007). Therefore, there is a need to adopt a more comprehensive requirements gathering approach that takes into account the social aspects, contradictions, governance rules, division of labor, etc. This paper adopts a novel approach by adapting Activity Theory to provide a framework to develop emergency data standards. Activity Theory prompts consideration of issues and concerns such as communities and sub-communities and the contradictions that are not part of traditional approaches. We provide a more detailed discussion on the approach and the benefits of this approach later in the paper.

The emergency management ISC connects the network of incident reporting sources, scanning agents, interpretation agents, and response agents, and it balances information supply and demand (Sun et al. 2005). Along the information chain, task-critical information that focuses on situational awareness and a common operating picture is exchanged to enable informed decision making and to generate synergy (See Figure 1) (Porter 1985).

![](/api/attachments/Q7UBNQMG/fulltext/images/9e7f760d1f5b2bc3c571e300c3a47a0d2a830a9000845039b0ef3b339d4a3695.jpg)

Emergency Response Information Supply Chain (Adapted from Sun & Yen 2o06)

![](/api/attachments/Q7UBNQMG/fulltext/images/c8062d8acf48a814e19df78e5b773d6b0f07464543af65473ee2d555faecd289.jpg)  
Primary Activities

Proposed model enhances information systems infrastructure and inter-organizational collaboration

Information Supply ValueChain (Adapted from Porter 1985)

Figure 1. Overview of Emergency Response Information Supply Chain

An effective information supply chain dictates the necessity to address the challenges of interoperability, which is defined as “the ability of two or more entities or systems to exchange information and to use the information that has been exchanged” (DHS 2005; IEEE 1990). The issues are more pronounced because the technologies adopted by participating agencies to support the mitigation of a critical incident are, in general, incompatible for reasons ranging from the ability of local agencies to fund technology to the lack of unified guidelines for software and hardware (BJA DOJ 2007; Fedorowicz et al. 2007; Gogan et al. 2005; Williams et al. 2005). Literature in this area provides testimony that interoperability issues stem in part from the data level (COMCARE 2002a; DHS et al. 2006; EIC 2004; NIEM 2006; Stegwee et al. 2003). Data-level support is key to ensure a common semantic understanding among participating organizations and to provide data transmission that follows consistent protocols (Chakravarti et al. 2006; Jump et al. 2003; Vinze et al. 2001). In this paper we use a theory-guided approach to develop data standards for chemical emergency scenarios based on interviews with first responders and their mutually agreed upon input (In Figure 1 we highlight the area of our contribution to the information supply chain using dotted lines). It may be noted that the other facets of interoperability (i.e., hardware, middleware, application layer compatibilities) also limit the effectiveness of emergency information sharing, and the provision of possible solutions to counter this ineffectiveness requires additional research efforts that are beyond the scope of the current study.

A number of emergency data standards have been developed to address the issues of interoperability when data is passed between applications and devices (see Table 1). However, none of these standards has been designed to support the specific incident types that involve the incident command structure (DHS 2004b). To elaborate on this issue further, in Figure 2.a we present a snapshot of one response document that exemplifies some of the information that may be exchanged during a typical chemical incident. We use this document to illustrate the point that the leading national standards fo emergency management, such as the National Information Exchange Model (NIEM) (DHS et al. 2006), do not currently support many of the elements needed for incident management (See Figure 2.b). Consequently, task-critical information that flows through these disparate systems is inconsistent and includes incompatible definitions, formats, and structures. The lack of data interoperability, therefore, limits the effectiveness of information systems and the collaborative emergency management they support.

<table><tr><td rowspan="9">DISCHARGE RATE/DURATION ESTIMATESAll contents assumed by user to discharge within 1.0 minuteDuration of discharge = 1 minutesAmount discharged = 150000 lbsState of material = Mix of gas/aerosol***** FIREBALL HAZARD RESULTSMax fireball diameter = 847 feetMaximum fireball height = 1392 feetFireball duration = 16.4 secondsFatality zone radius = 1172 feetInjury zone radius = 2227 feet</td><td>Data Element</td><td>NIEM Support</td></tr><tr><td>Duration of Charge</td><td>No Match</td></tr><tr><td>Amount Discharged</td><td>No Match</td></tr><tr><td>State of Material</td><td>No Match</td></tr><tr><td>Max Fireball Diameter</td><td>No Match</td></tr><tr><td>Maximum Fireball Height</td><td>No Match</td></tr><tr><td>Fireball Duration</td><td>No Match</td></tr><tr><td>Fatality Zone Radius</td><td>No Match</td></tr><tr><td>Injury Zone Radius</td><td>No Match</td></tr><tr><td colspan="2">Figure 2a. Example of Emergency Management Document</td><td>Figure 2b. Availability of NIEM Support for the Example Document</td></tr></table>

In order to develop standards that can make collaboration and communication more effective across different platforms (Lyytinen et al. 2006; Vinze et al. 2001; Zhu et al. 2006), we elicit and analyze requirements guided by the Activity Theory framework (Bertelsen et al. 2003; Engestrom 1999). Activity Theory is not a predictive theory but a descriptive one (Kuutti 1991). It provides a framework in which the critical issues of context can be taken into account for system design (Bertelsen et al. 2003; Chaudhury et al. 2001; Uden et al. 2007). In this paper, we develop an XML-based response data model that defines consistent data semantics and internal structures using documents generated from actual chemical incidents. The XML response data model provides an effective vendor-neutral standard to stitch together disparate systems. In this article we focus on chemical incident responses because chemical incidents are among the most common and complex types of critical incidents encountered by first responders (EHC 1999; GAO 2002). The use of the Activity Theory framework is important because, like other approaches, it considers issues related to people, processes (activities) and technology; but, unlike other approaches, it also prompts consideration of communities (group – formal and informal), division of labor (rule, regulation, and task assignments), and contradiction and conflicts (O'Leary 2007).

This paper focuses on the information supply chain and the interoperability challenges in emergency contexts, and it attempts to answer the following questions: (1) what is an effective data modeling approach for emergency standard development, and (2) what are the key information components and their internal structures for emergency management interoperability, etc. This paper makes two major contributions. The first contribution is the approach used to develop the data model. In this paper we modify Activity Theory and use the adaptation as a theory to guide the requirements engineering and the data model development. Activity Theory prompts consideration of communities and sub-communities, contradictions that emanate from it, division of labor, etc. A consequence of using this approach has resulted in the development of new data types in the data standards that may otherwise not have been included. The approach can also serve as the overarching framework for information management and system design not only in other emergency contexts but also in areas where artifacts are being developed for collaborative purposes. Second, it develops a validated object-oriented XML data model to extend NIEM to address interoperability issues. Currently there are no data models that cater to specific incident types such as chemical incidents and, therefore, the model developed in this paper addresses this issue. The validation uses an RFC-like process. The model uses actual documents from a large number of chemical incidents and is, therefore, of practical value. The development work includes an implementation that allows users to create documents that are compatible with the new data model developed in this paper. The paper informs both theory and practice.

The paper is organized as follows. Section 2 reviews the literature of information supply chain and interoperability. Section 3 presents the Activity Theory informed data model design processes. Section 4 elaborates on the details of the data model. In Section 5, we present a case illustration to evaluate the usability of the data model. Section 6 describes two computer programs that we develop to help the information standardization process. Section 7 discusses the paper’s contributions, and limitations and directions for future research. In addition, as part of Appendix A, the paper includes a summary of national efforts related to emergency management interoperability. Appendix B consists of the full version of the data type illustration. Appendix C contains a detailed data model specification in a spreadsheet format. Appendix D consists of the data model XML schema. Finally, Appendix E provides a large illustration of the data model overview (i.e., Figure 4).

## 2. Literature Review

In this section, we review the existing literature of information supply chain and information interoperability. The literature review summarizes the findings in these research areas and also identifies the existing research gaps that are addressed by the current study.

## 2.1. Information Supply Chain

The information supply chain (ISC) has been studied in the context of product development, health care, physical supply chain, business intelligence, data warehousing, and emergency management (Arora et al. 2006a; Arora et al. 2006b; Gutknecht 2007; Johnston 2005; Marinos 2005; Raghu et al. 2007). The ISC has been defined as “a collection of information and communication technologies to provide a secure integrated decisional environment that enables business partners to collectively sense and respond to opportunities and challenges in a networked eco-system” (Vinze 2006). Unlike the physical supply chain, which is mostly linear, the ISC is more reminiscent of a web that consists of information sharing agents that create, sustain, retrieve, interpret, analyze, and distribute information to meet the ultimate goal of information supply and demand (Foulkrod 2006; Marinos 2005; Sun et al. 2005; Vinze 2006). During the flow of ISC, information is constantly moving along critical dimensions of the data life cycle, and it parallels organizational business processes (Marinos 2005). Prior literature suggests that the efficient design and operation of an ISC rely on (1) systemic ISC information requirements analysis through techniques such as information dependency relation (IDR) analysis, (2) collaborative development techniques such as information requirement planning (IRP), and (3) adaptation of conventional supply chain management strategies such as vendor-managed inventory (VMI) into an ISC context (Marinos 2005; Sun et al. 2005). Despite these efforts, the ISC is subject to a wide spectrum of issues with regard to data quality, system design, and infrastructure support (Sun et al. 2005). Examples of related issues include security (Johnston 2005; Vinze 2006), limitations to the information processing capacity (Sun et al. 2005), and interoperability (Howard 2007; Johnston 2005; Khan 2007).

## 2.2. Interoperability

Interoperability refers to “the ability of two or more entities or systems to exchange information and to use the information that has been exchanged” (IEEE 1990). Stegwee and Rukanova (Stegwee et al. 2003) extend this technical definition to an organizational context and suggest that interoperability resides at the interplay of human systems, business processes, and enabling technologies. Prior studies have explored interoperability issues in a wide variety of domains, including heterogeneous databases, information retrieval, knowledge systems, artificial intelligence, multimedia, geographic information systems (GIS), interoperable system architecture design, and business process modeling (Beech 1997; Goodchild et al. 1997; Gupta et al. 1997; Harrison et al. 2006; Kashyap et al. 1998; Kotinurmi et al. 2003; Sciore et al. 1994). Take heterogeneous databases, for example. Interoperability has been explored within the context of federated databases, data warehousing, integrating databases, and ontology (Allen et al. 2003; Johansson et al. 2003; March et al. 2003; March et al. 2000a; March et al. 1995; Reddy et al. 1994; Rho et al. 1997; Rishe et al. 2000; Sarda 2007; Wang et al. 1990). Supports for interoperability range from methods to meta-models, concrete models, and operational standards (Stegwee et al. 2003). The design of interoperability support should not only address the communication interactions and the data structures, but it should also address the vocabularies to be used when populating the data structures (Kuhn et al. 2001; Lee et al. 2005; March et al. 2000b). However neither of these studies deals with critical incidents nor uses a theory like Activity Theory to guide the approach. In this paper, we focus on the interoperability issues of the information supply chain (ISC) in an emergency context.

The existing research suggests that interoperability in the ISC is a multifaceted concept (COMCARE 2002a; Stegwee et al. 2003). It involves interoperability at five layers: (1) the information level with an emphasis on the data vocabulary and message sets in their storage or transport; (2) the transport level with an emphasis on the underlying infrastructures for communication; (3) the response agency application level with an emphasis on the computer supported collaborative work among response agency systems; (4) the facilitation services level with an emphasis on the facilitative utilities shared among agencies on, for example, authentication; and (5) policy and protocols with an emphasis on the governmental and administrative response practices. While all five levels of interoperability are problematic in the existing emergency ISC, data-level interoperability is deemed by the general emergency response community as the most important aspect of ISC (DHS et al. 2006; EIC 2004; NIEM 2006; SICOP 2005). Data interoperability support is key to ensuring a common semantic understanding among participating organizations and to providing data transport that follows consistent protocols (Chakravarti et al. 2006; Jump et al. 2003). It is important to note that the other dimensions of interoperability also play an important role and may limit the effectiveness of emergency information sharing if it is not addressed properly (Choi et al. 2004a).

<table><tr><td colspan="5">Table 1. Information Interoperability Solutions Nationwide</td></tr><tr><td colspan="2">Data Standards</td><td>Interoperability Focus</td><td>Responsible Parties</td><td>Objectives</td></tr><tr><td colspan="2">Vehicular Emergency Incident Data Exchange Format Standard (xml.coverpages.org/ComcareDataExchange FormatOverview.pdf)</td><td>Within-Domain Interoperability</td><td>ComCARE Alliance CAN Data Set Working Group</td><td>Enable the automatic distribution of vehicular emergency incident data between the Telematics Service Providers and emergency personnel such as 9-1-1 center, hospitals, transportation agencies, and emergency responders.</td></tr><tr><td colspan="2">Common Alerting Protocol (www.incident.com/cap)</td><td>Cross-Domain Interoperability</td><td rowspan="4">OASIS Emergency Management Technical Committee and Emergency Interoperability Consortium</td><td>Enable the automatic distribution of all types of hazard warnings and local, regional, and national reports.</td></tr><tr><td rowspan="3">Emergency Data Exchange Language (www.comcare.org/edxl.html)</td><td>Distribution Element</td><td rowspan="3">Mixture of Within-Domain and Cross-Domain Interoperability</td><td>Enable the routing control of emergency messages for efficient sharing among related agencies.</td></tr><tr><td>Resource Messaging</td><td>Enable the discovery, request, and acquisition of all types of resources.</td></tr><tr><td>Hospital Availability Exchange</td><td>Enable the exchange of hospitals&#x27; bed availability, status, and capacity among hospitals and other emergency agencies.</td></tr><tr><td rowspan="3">IEEE Std. 1512 Standards for Common Incident Message Sets (standards.ieee .org/announce ments/1512itsb ase.html)</td><td>Traffic Management Standard</td><td rowspan="3">Within-Domain Interoperability</td><td rowspan="3">IEEE and United States Department of Transportation</td><td>Enable the sharing of traffic and incident information among agencies for traffic management such as evacuation and routing.</td></tr><tr><td>Public Safety Traffic Incident Management Message Sets</td><td>Enable the sharing of transportation related safety information among agencies and the public.</td></tr><tr><td>Hazardous Material Incident Management Message Sets</td><td>Enable the sharing of chemical-related traffic incidents with information regarding the vehicle and cargo.</td></tr><tr><td colspan="2">Global Justice XML Data Model (www.it.ojp.gov/jxdm)</td><td>Within-Domain Interoperability</td><td>U.S. Department of Justice</td><td>Enable the sharing of criminal justice information among law enforcement, public safety agencies, prosecutors, public defenders, and the judicial branch.</td></tr><tr><td colspan="2">National Information Exchange Model ( www.niem.gov)</td><td>Mixture of Within-Domain and Cross-Domain Interoperability</td><td>U.S. Department of Homeland Security and U.S. Department of Justice</td><td>Enable the nationwide sharing of information on justice, emergency management, geospatial and infrastructure protection, immigration etc.</td></tr></table>

<table><tr><td colspan="2">Data Standards</td><td>Interoperability Focus</td><td>Responsible Parties</td><td>Objectives</td></tr><tr><td rowspan="2">E9-1-1 Standards (www.911cover age.org/aboutE 911.htm)</td><td>Standards for Automatic Location Identification (ALI) Data Exchange, Response &amp; GIS Mapping</td><td rowspan="2">Within-Domain Interoperability</td><td rowspan="2">National Emergency Number Association</td><td>Enable the automatic sharing of ALI data between Service Providers and 9-1-1 Data Base Management System Providers.</td></tr><tr><td>Standards for Local Exchange Carriers, ALI Service Providers &amp; 9-1-1 Jurisdictions</td><td>Enable the efficient sharing of number pooling, database communication, and general message exchanges among Service Providers and 9-1-1 Databases Management System Providers.</td></tr><tr><td colspan="2">EMS Data Dictionary (currently version 2.2.1) (www.nemsis.org/dataElements/datasetDiction aries.html)</td><td>Within-Domain Interoperability</td><td>National Emergency Medical Services Information System</td><td>Enable the efficient sharing of EMS information on EMS personnel, patients, situations, assessments, medical history, and medical devices.</td></tr><tr><td colspan="2">HL7 Messaging Protocol (www.etransx.com/hl7-xml.asp)</td><td>Within-Domain Interoperability</td><td>Health Level 7 Organization</td><td>Enable the efficient sharing of medical data among all healthcare systems.</td></tr><tr><td colspan="2">PHIN Vocabulary Standards and Specifications (www.cdc.gov/phin/vocabulary)</td><td>Within-Domain Interoperability</td><td>Public Health Information Network</td><td>Enable and foster the use and exchange of consistent information among public health partners.</td></tr></table>

Since the events of 9/11 and Hurricane Katrina/Rita, a number of research efforts have been launched by governmental agencies, public associations, and the private sector (COMCARE 2002b; DHS et al. 2006; DOJ 2005; E9-1-1 2006a; E9-1-1 2006b; EIC 2005; HL7 2006; IEEE 2000; NEMSIS 2007; OASIS 2005; PHIN 2005). In Appendix A, we list the national initiatives that address one or more aspects of interoperability in the context of critical incidents. In Table 1, we summarize the leading data standards that specifically address information interoperability issues. They are grouped by (1) the interoperability focus that is addressed either within domain interoperability (e.g., to address interoperability barriers between fire companies) or cross-domain interoperability (e.g., to address interoperability barriers between fire companies and police departments), (2) responsible parties, and (3) objectives.

However, none of the existing data standards provide sufficient support for incident management. As we illustrate in Table 1, the majority of the existing standards are targeted toward domain-specific interoperability problems, and standard sets have been developed to serve individual domains (e.g., justice, health care, and transportation). However, these standards within the domain do not fully support incident management that relies heavily on communications across domain boundaries. When cross-domain data standards are concerned, there exist mainly the National Information Exchange Model (NIEM) and Emergency Data Exchange Language (EDXL), which is currently being merged into NIEM. NIEM prescribes data standards for the entire spectrum of homeland security including a set of data standards for “Emergency Management.” However, the data standards in NIEM Emergency Management support only alarm events, resource, and message distribution elements. While these supports are necessary for emergency management, the data standards do not address other management aspects such as incident command, response operation, risk assessment, incident setting, etc. In this paper, we develop a broader set of data standards that complement the existing NIEM standards for emergency management.

## 3. Chemical Incident Response Data Model Development

A data model is a precise and unambiguous representation of organizational information requirements (Hull et al. 1987; Peckham et al. 1988). The development of a data model requires systematic approaches to elicit and analyze the internal elements, structure, and relationships the data model should represent (Zowghi et al. 2005).

An approach driven by Activity Theory represents a method that has gained increasing attention in recent years (Kaptelinin et al. 2006; Uden et al. 2007; Webb et al. 2006). Activity Theory provides a lens to analyze the computer-supported activity of a group or organization (Kaptelinin et al. 2006) and to study the design of artifacts for individuals and organizations (Bertelsen et al. 2003; Chaudhury et al. 2001).

Activity Theory suggests that human activity is directed toward a material or ideal object, mediated by artifacts or instruments, and socially constituted within the surrounding environment (Bertelsen et al. 2003; Vygotsky 1978). Activity can be understood as a systemic structure with various activities that are collated or extended away from the core activities (Bertelsen et al. 2003). The subject is the active element of the process and can be either an individual or a group. The object transformed by the activity can be an ideal or material object (Fuentes et al. 2003). The transformation process is enabled and supported by instruments (physical or logical). The instrument provides the subject with the experience historically collected by his/her community (Fuentes et al. 2003; Webb et al. 2006). During the interaction, subjects internalize and/or externalize their cognitive schemes and their understanding of the relationship between themselves and the external objects, instruments, surroundings, etc. Activity Theory also considers contradictions as one critical aspect and suggests that contradictions are the driving force in human interaction and system design (Bertelsen et al. 2003; Uden et al. 2007). The contradictions may also exist inside the subjects, objects, instruments, and their interactions. In Activity Theory, activity is constantly developing as a result of contradictions and instability and because of the development of new needs. This historical development of activity implies a development of artifacts and environment: modes of acting within an activity system are historically crystallized into artifacts (Bertelsen et al. 2003; Engestrom 1987; Kaptelinin et al. 2006;

Leont'ev 1981; Nardi 1996; Webb et al. 2006). In this study, we further extend the traditional formalisms of Activity Theory (Engestrom 1987) to include “environment” as a relevant and important construct. Environmental factors (e.g., “weather”) impact the activities carried out by subjects.

Published literature shows that a number of approaches that allow requirement elicitation and analysis for data modeling have been developed; below we present only those that are widely used. Although not exhaustive, this selection is representative of both the range described in the relevant literature and of what is currently practiced in industry (Zowghi et al. 2005): goal-oriented (Donzelli et al. 2003; Mylopoulos et al. 1999; Zhang et al. 2007), function-based (Chandrasekaran et al. 1996), and viewpoint-oriented (Finkelstein et al. 1991a; Finkelstein et al. 1991b; Kotonya 1999; Steen et al. 2004). The comparison suggests that an extended approach that is informed by Activity Theory provides a more comprehensive framework to elicit and analyze the requirements for data modeling. Take the viewpoint-oriented approach, for example. A viewpoint is a collection of information about a system or related problem that is gathered from a particular perspective (Finkelstein et al. 1991a). While viewpoint approaches model the domain from multiple perspectives to form a complete picture of the target system, they are typically criticized for not being able to take into account non-functional requirements that may be embedded in the community and social environment (Nuseibeh et al. 1996; Sommerville et al. 1998). They do not consider contradictions and conflicts that are part of collaborative systems. Prior research suggests that such conventional approaches are typically limited in the scope of analysis that they can offer (Simsion et al. 2001; West 2003). Table 2 provides a comparative summary.

Table 2. Comparison of Requirement Engineering Approaches

<table><tr><td>Dimension</td><td>Focus</td><td>Goal Oriented</td><td>Function Based</td><td>Viewpoint Oriented (VOSE/ VORD)</td><td>Adapted Activity Theory</td></tr><tr><td>Goal</td><td>Intention</td><td>X</td><td></td><td></td><td>X</td></tr><tr><td rowspan="2">People</td><td>Individual (role)</td><td>X</td><td>X</td><td>X</td><td>X</td></tr><tr><td>Community (group, role)</td><td></td><td></td><td></td><td>X</td></tr><tr><td rowspan="3">Process</td><td>Division of Labor (rule, task assignment)</td><td></td><td></td><td>X</td><td>X</td></tr><tr><td>Activity and Activity Structure</td><td>X</td><td>X</td><td>X</td><td>X</td></tr><tr><td>Object Hierarchy</td><td>X</td><td>X</td><td></td><td>X</td></tr><tr><td>Technology</td><td>Instrument (form)</td><td></td><td></td><td>X</td><td>X</td></tr><tr><td rowspan="3">Environment</td><td>Context Awareness</td><td>X</td><td>X</td><td></td><td>X</td></tr><tr><td>Social Issues</td><td></td><td></td><td></td><td>X</td></tr><tr><td>Environment Issues</td><td></td><td></td><td></td><td>X</td></tr><tr><td>Interaction</td><td>Contradictions</td><td>X</td><td></td><td></td><td>X</td></tr></table>

Adapted from Engestrom (Engestrom 1987; Engestrom 1999), we briefly illustrate in Figure 3 the extended Activity Theory and its application in the modeling of data related to the response information supply chain.

In Table 3 we map Activity Theory constructs in the context of emergency management (Bertelsen et al. 2003; Engestrom 1999). Note that the mapping in Table 3 is not an exhaustive enumeration of aspects but only an illustrative set of guidelines that we use.

<table><tr><td colspan="2">Table 3. Application of Activity Theory in Data Model Development</td></tr><tr><td>Activity Theory Construct and Perspective</td><td>Example Design Implications</td></tr><tr><td>SubjectA subject in Activity Theory is an agent that undertakes activity.In our case the subjects are individual responders and domain subject matter experts who provide or consume information from the information supply chain.</td><td>The subjects involved in mitigating incidents that involve chemicals need to be identified.Their individual experience and viewpoints will help us comprehend the response information requirement and its management.</td></tr><tr><td>ObjectAn object is an artifact shared by a community of subjects that work together to reach a desired outcome (Barthelmess et al. 2002; Kuutti 1991).The object in our case is the data model being developed to improve collaboration and coordination (outcome) to effectively deal with chemical incidents by developing common operating picture, exchanging task critical information, etc.</td><td>The data model should be comprehensive and the exchange of critical information should be easy in terms of data model usability. This prompts the use of XML in describing the data model because of its extensibility, structured nature, and platform/software independence.</td></tr><tr><td>CommunityAccording to Barthelmess and Anderson (Barthelmess et al. 2002) this construct includes subjects that share an object.The first and second responders are subjects who form the community in our case. The first and second responder community includes several sub-communities such as fire and rescue, law and order, and emergency medical personnel, FEMA, hazmat teams, etc. Sub-communities also form based on the agency to which they belong.Each sub-community brings in a different perspective that derives from its routine daily tasks, functions during critical incident, group culture, etc. These differences also include different information artifacts such as the system they bring to bear during the mitigation of a critical incident.</td><td>The interoperability needs of the different communities must be elicited. In addition requirements should also consider the communication needs between groups. Therefore requirements should be elicited from multiple municipalities as well as across levels of government in counties, cities, towns, and villages. They should also be elicited from different response function groups.</td></tr></table>

Acti or o t t y  s tes The    s l  to elmnts. cog   si uion cinn o oi s ns uioptn ele  s s       sose ohoues ss sst s iit hi it o t ital Reonne r t rne rinn rnntal uvi   t se e i te t n a i act Enviinent

inciidnt, ani  ic t t ic t cal Ths s s s   s ss sn

pP(iciioe otri orton) exon xcion  co o xcign on xmnng os  ss rs s ts s  ot the Resi a ss is i a s oy assion Ae s cs s s ss s ses  ed

elet  e sts srn s sion. stro o s ror     uo sfrucos oes ros suoo uoes ruce re Iii Sein eiitt o en  eis nn ion in  nn on (o Fur s  d ps    ary

messging crins o o   rol ra srd l ul ro roch use o csod odo oog oo o oog o asn o  ssss   e   o r sorr

## Tabe n n e e A A  d  ed)

to  u  s or T li a ic t   e s abe, To  s s on s  or

![](/api/attachments/Q7UBNQMG/fulltext/images/e097afb0ab6fe1a93781845392980516c9b87bcef29a3bc84a862b1fc53692e2.jpg)

Figure 3. Application of Activity Theory in Response Information Supply Chain Data Model (Adapted and Extended from Engestrom 1987 and 1999)

<table><tr><td colspan="3">Table 4. Examples of Contradiction of Emergency Management and Related Data Design</td></tr><tr><td>Illustrative Issue</td><td>Potential Contradiction</td><td>New Data Type</td></tr><tr><td rowspan="2">Fire, Police, Emergency Medical Service, Hazard Material Workers, etc</td><td>Response agencies often compete for the incident commander position. Most of the time, the fulfillment of this position is determined by the incident type. For example, if there is a criminal aspect to an incident, law enforcement agencies are in charge of the scene; in all other chemical-related incidents, typically the fire chief is in charge. This information should be captured and clearly identified during the incident response.</td><td>Incident Type</td></tr><tr><td>The police would like to secure the scene first before they allow other agencies to enter the incident site. This frequently interferes with the operations of other agencies such as Fire and EMS who would like to enter the site with minimal delay. The scene security information should be captured and disseminated every time it changes.</td><td>Scene Security</td></tr><tr><td>Local, State, and Federal</td><td>It is important to identify the governing jurisdiction /municipality that is primarily responsible for the incident response. Different jurisdictions (e.g., “home rule” municipalities) may vary in their regulations and practices regarding emergency management. The responsible jurisdiction also has the obligation to provide resources and to compensate external supporting agencies for their financial cost. To avoid disputes, this information should be captured and clearly identified.</td><td>Location including “District”</td></tr><tr><td>Emergency Managers</td><td>Information sharing in emergency management should be controlled to ensure that information is distributed among authorized personnel only. To avoid conflicts over access to information, the information on incident classification level and personnel security clearance level should be clearly captured and identified.</td><td>Incident classification level and responder personnel security clearance level</td></tr></table>

<table><tr><td colspan="2">Table 5. Data Model Development Process Overview</td></tr><tr><td>Development Process</td><td>Design Events</td></tr><tr><td>Document Collecting:Collecting relevant documents, information sharing requirements, management guidelines</td><td>- More than 60 documents were collected, including chemical incident response technical data forms; chemical incident response dispatch forms; field notes and chronological logs; response guidelines (e.g., Incident Command System (DHS 2004b) and 2004 Emergency Response Guidebook (DOT et al. 2004)); chemical dictionaries and fact sheets (e.g., material safety data sheets); chemical databases (e.g., Computer-Aided Management of Emergency Operations (EPA 2006)); and chemical-involved incident messaging systems (e.g., National Fire Incident Reporting System-NFIRS (DOS et al. 2006))</td></tr><tr><td>Data Analysis:Synthesize and reconcile the core information and internal relationships</td><td>- Following the Incident Command System as the basis, the rest of the documents are analyzed to develop a general information management framework, which captures the key elements and structures for the data model- This process is facilitated by interviews with domain experts in incident management</td></tr><tr><td>Data Model Specification:Define typing of identified components</td><td>- NIEM is utilized as the foundation of the new data model for the reuse and extension of data elements. NIEM contains emergency management components and is endorsed by U.S. DOJ and DOH. The NIEM compliance allows the new data model to maximize its utility- An object-oriented structure is used for the data model to allow inheritance based design for reuse and extension- XML based data model specification and implementation are used. XML is a machine readable and platform independent specification language which allows for the development of automated information processing tools via heterogeneous technological solutions</td></tr><tr><td>Request for Comment (RFC):Solicit data model review opinions from domain experts</td><td>- Seven evaluators from hazmat, fire, police, and standard development- A detailed tutorial is given in RFC to explain to responders how the data is structured through an object-oriented approach for inheritance and extension- Two experts are familiar with both emergency management information sharing and standard development- Two rounds of comments are collected</td></tr><tr><td>Feedback Synthesize and Model Update:Improve the data model with expert review</td><td>- Data model revision is facilitated by the panel of seven evaluators. Consensus building is achieved through a Delphi-like approach- Major changes are made to 8 data types in addition to around 20 other changes</td></tr><tr><td>Data Model Finalization:Documentation</td><td>- Data model specification in XML Schemas and EXCEL spreadsheet</td></tr></table>

In the remainder of this section we illustrate issues of contradictions that are an important aspect of Activity Theory. The issues concerning community and the division of labor have not been elaborated to avoid replication (See Table 3 for details). Activity Theory considers any activity system may have levels of contradictions, either inside the key elements or between them, which must be attended to in the analysis of a working situation (Engeström 1999b). Contradictions are important for system design in that they indicate emergent opportunities for the activity development and can be used as sources of improvement (Kuutti 1996). In Table 4 we provide a few examples of how the examination of contradictions has led to the creation of data types that are now part of the data model.

Contradictions also arise between the constituent nodes as may be the case, for example, between the subject (emergency managers in different counties) and the instrument (varying existing tools and forms). The subjects may have a widely discrepant view of the data model design, as each may prefer one that is compatible with his/her existing emergency management information systems. In addition, there is a conflict between the choice of instruments and the rules of the community. Due to the fact that emergency managers across county, city, town, and village levels utilize different response guidelines, forms, and documentations, there is a conflict regarding which data element should be included for a commonly agreed-upon data standard. In this regard, the data model design requires both a comprehensive collection of supportive materials at all levels as well as collaboration among the agents they represent. Due to this contradiction, an RFC-like process is used to iteratively interact with the experts to arrive at a consensus. The examination of conflicts between the stakeholders requires a validation and consensus building process much like the Delphi-methodology, yet it should also build on NIEM as the foundation for the new data model.

The data model development processes are summarized in Table 5.

We developed a conceptual framework that identifies the key aspects (dimensions and structures) of task-critical information for emergency management (see Table 6). This framework facilitates the classification of information elements, ensures internal relationships, and serves as the overarching framework to organize the newly developed data model. The development of this information management framework is grounded on national and local standard response procedures as well as management guidelines such as the Incident Command System, the 2004 Emergency Response

<table><tr><td colspan="3">Table 6. Information Management Framework for Chemical Response</td></tr><tr><td>Major Dimensions</td><td>Sub Dimensions</td><td>Example Data Types in Dictionary Vocabulary</td></tr><tr><td rowspan="3">Threat Assessment: Facts about chemical incident occurrence and its consequences. Source of the response decision making and strategy development</td><td>Incident SettingDescriptions of the physical attributes of the incident. Valuable for response preparation and initial set up</td><td>Incident specific characteristics, weather, incident location, facility</td></tr><tr><td>Chemical HazardDetails of the chemical product and its release. Bases of chemical handling procedures for achieving operation safety</td><td>Chemical property (e.g., physiochemical property, stability and reactivity, fire and explosion, etc.), container characteristics, release detail</td></tr><tr><td>ThreatsInformation on the incident impacts. Required for response strategy development (e.g., prioritizing and resource allocation)</td><td>Injury and casualty, environmental damage, property damage, public safety, fire threat, non-fire threat</td></tr><tr><td rowspan="2">Incident Command System: Records of incident response structure and progress. Source of response coordination and control</td><td>Response ManagementDescriptions of the command system and entities involved. Valuable for the structuring of adaptive response management</td><td>ICS unit, response facility, response organization, responder, resource, responder ICS association, Organization ICS association</td></tr><tr><td>Response OperationDetails of the response activities design and implementation. Bases of monitoring and evaluating the response progress</td><td>Operation plan, response activity, activity involved responder association, activity involved organizational association, activity involved resource association</td></tr></table>

<table><tr><td colspan="8">Chemical Incident Response</td></tr><tr><td colspan="8">Threat Assessment</td></tr><tr><td colspan="8">Incident Setting</td></tr><tr><td rowspan="27">Incident Specific Characteristics Incident ID, Incident Date, Incident Time, Incident End Date, Incident End Time, Incident Result Text, Incident Description, Incident Type, Cause, Classification Level</td><td rowspan="27">Weather Sky, Temperature, Barometer, Wind Speed, Wind Direction, Dew point, Precipitation, Humidity, Inversion</td><td rowspan="27">Chemical Property Chemical Name, CAS Number, DOT ID, DOT Hazard Class, Percentage By Weight, General Description, Health Rating, Flammability Rating, Reactivity Rating</td><td rowspan="27">Release Detail Chemical, Release Medium, State Of Material, Release From, Release Rate, Potential Release</td><td>Injury and Casualty Injury Description, Civilian Injury Number</td><td colspan="3">Response Management</td></tr><tr><td rowspan="3">Environmental Damage Environment Fate, Environment Toxicity</td><td rowspan="3">ICS Unit Command Person, Unit Category, Establish Date, Establish Time</td><td>Response Organization Response Organization Name, ID, Response District, Contact, Response Organization Sub Unit</td><td>Operation Plan Plan Name, Plan ID, Plan Objective, Plan Description, Evaluation</td></tr><tr><td>Responder Name, Title, Affiliation, Contact, Security Clearance Level</td><td>Response Activity Activity Date, Activity Time, Activity Description, Activity Category</td></tr><tr><td>Resource Name, Type, Description, Unit</td><td>Activity Involved Responder Association Responder, ICS Unit, Position</td></tr><tr><td>Property Damage Property Total Damage Value</td><td>Responder ICS Association Responder, ICSUnit, Position</td><td>Organization ICS Association Organization, ICS Unit, Description</td><td>Activity Involved Resource Association Resource, ICS Unit, Quantity</td></tr><tr><td rowspan="22">Public Safety Area Affected, Area Evacuated</td><td rowspan="22">Fire Threat Max Fire Ball Diameter, Max Fire Ball Height</td><td rowspan="22">Non-Fire Threat Max Hazard Zone Width, Max Weight Vapor Cloud</td><td rowspan="11">Activity Involved Organization Association Response Organization, ICS Unit, Description</td></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr><td rowspan="10"></td></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr><td>Notations: Dimension Description: Dimension Name: Data Component: Component name: List of Example Elements:</td></tr></table>

Guidebook, and the New York State Chem-Bio handbook (DHS 2004b; DOT et al. 2004; Sidell et al. 2000). It is further enriched by prior literature (Auf der Heide 1989; Shen et al. 2004; Turoff 2002; Turoff et al. 2004) and the data analysis of raw materials that were collected from local emergency responders in the western New York area. In the following section (Section 4), we introduce the data model along with the framework dimensions. In Figure 4 we present the overview of the data mode for chemical incidents. Please refer to Appendix E for an expanded version of Figure 4.

## 4. Data Model Description

In this section, we introduce the chemical response data model. It includes task critical data that is typically exchanged in a chemical emergency response. The data model also provides a validated set of standards that can be applied to fill the gaps in interoperability.

## 4.1 Threat Assessment

Threat assessment is an important response task in which response agents analyze the incident to make an informed decision and decide on the nature of their response planning. In a typical threat assessment, response agents share information on the incident setting, chemical hazards, and threats.

## 4.1.1 Incident Setting Data Vocabulary

Incident-setting data provides general information such as location and weather. It is important for strategic planning for personnel/resource entry and deployment. we provide a brief summary of incident-setting data vocabulary in Table 7 (Please refer to Appendix B, C, and D for detailed definitions). To comply with NIEM as suggested by the Activity Theory framework, we follow an objectoriented approach and define our data elements through inherence relationships from the existing NIEM standards. NIEM has developed a set of useful base elements such as u:ActivityType, which defines a data type for one or more related actions, events, or process steps (Please refer to NIEM v1.0 for details). As such, inheritance and extension from base elements allows for the rapid development of NIEM-compliant new data types. As a NIEM convention, u:SuperType is the root of the entire NIEM data model; in order to stay NIEM compliant, new data elements that are not inheritable from any existing NIEM data types are required for the establishment of inheritance relationships from u:SuperType. In addition, we relate the data model elements to the Activity Theory (AT) to suggest how they are derived.

<table><tr><td colspan="4">Table 7. Incident Setting Data Vocabulary</td></tr><tr><td>Major Data Element</td><td>Description</td><td>Data Type</td><td>Example Sub-Elements</td></tr><tr><td>Incident Location (Reference Adapted - AT (Environment))</td><td>Location info</td><td>em:LocationType</td><td>Terrain, district, population density, area description text, scene security</td></tr><tr><td>Weather (Reference Adapted - AT (Environment))</td><td>Weather info</td><td>u:SuperType</td><td>Sky, temperature, barometer, wind speed, wind direction, dew point, precipitation, humidity</td></tr><tr><td>Incident Specific Characteristics (Reference Adapted - AT (Environment))</td><td>Incident identification info</td><td>u:ActivityType</td><td>Incident ID, incident data and time, incident cause, incident type, classification level</td></tr><tr><td>Facility (Reference Adapted - AT (Environment))</td><td>Involved facility info</td><td>c:FacilityType</td><td>Organization name, address full text, person full name</td></tr></table>

## 4.1.2 Chemical Hazard Data Vocabulary

The sharing of information on chemical hazards allows the responders to comprehend the potentia hazards that may emerge due to the chemical products involved (Kim et al. 2005). Table 8 provides a brief list of data elements that describe chemical hazard information.

<table><tr><td colspan="4">Table 8. Chemical Hazard Data Vocabulary</td></tr><tr><td>Major Data Element</td><td>Description</td><td>Data Type</td><td>Example Sub-Elements</td></tr><tr><td>Chemical (Reference Adapted - AT (Environment))</td><td>Description of chemical product involved</td><td>u:SuperType</td><td>Chemical Name, CAS number, DOT ID, DOT hazard class code, is EHS indicator, is CERCLA indicator</td></tr><tr><td>Physio Property (Reference Adapted - AT (Environment))</td><td>Physiochemical attributes</td><td>u:PropertyType</td><td>PH value, odor, molecular weight, water solubility, vapor pressure</td></tr><tr><td>Stability Reactivity (Reference Adapted - AT (Environment))</td><td>Stability and reactivity properties</td><td>u:SuperType</td><td>Stability description, hazardous decomposition products and hazardous polymerization</td></tr><tr><td>Fire and Explosion (Reference Adapted - AT (Environment))</td><td>Conditions causing fire and explosion</td><td>u:SuperType</td><td>Flash point, lower flammable limit, lower explosive limit, ignition temperature, fire extinguishing agent</td></tr><tr><td>Response Precaution (Reference Adapted - AT (Activity))</td><td>Precautions for response operations</td><td>u:SuperType</td><td>Firefighting precautions, non-fire response precautions, and waste disposal precautions</td></tr><tr><td>Exposure Protection (Reference Adapted - AT (Activity))</td><td>Protection to avoid chemical contamination</td><td>u:SuperType</td><td>Airborne exposure limit, ventilation procedures, protective clothing and respirator, evacuation, isolation</td></tr><tr><td>Health Hazard First Aid (Reference Adapted - AT (Environment))</td><td>Symptoms of health and medical aids</td><td>u:SuperType</td><td>Inhalation effect, inhalation aid, eye contact effect, eye contact aid</td></tr><tr><td>Container (Reference Adapted - AT (Environment))</td><td>Chemical container property</td><td>c:PropertyType</td><td>Container category, total weight, total volume, tank rupture pressure</td></tr><tr><td>Release (Reference Adapted - AT (Environment))</td><td>Chemical release details</td><td>c:IncidentType</td><td>Material state, release into, release from, release duration, release rate</td></tr></table>

<table><tr><td colspan="4">Table 9. Chemical Threats Data Vocabulary</td></tr><tr><td>Major Data Element</td><td>Description</td><td>Data Type</td><td>Example Sub-Elements</td></tr><tr><td>Injury Casualty (Reference Adapted - AT (Environment))</td><td>Personal injury and casualty</td><td>u:SuperType</td><td>Situation description, responder injury number, civilian injury number</td></tr><tr><td>Environment Damage (Reference Adapted - AT (Environment))</td><td>Environmental contamination and pollution</td><td>u:SuperType</td><td>Environment fate description, environment toxicity description</td></tr><tr><td>Property Damage (Reference Adapted - AT (Environment))</td><td>Loss of property</td><td>u:SuperType</td><td>Property damage description, property total damage value</td></tr><tr><td>Public Safety (Reference Adapted - AT (Environment))</td><td>Impacts on public safety</td><td>u:SuperType</td><td>Affected area description, affected area size, evacuated area description</td></tr><tr><td>Fire Threat (Reference Adapted - AT (Environment))</td><td>Characteristics of the chemical fire</td><td>u:SuperType</td><td>Maximum fire-ball diameter, fire ball duration, fatality zone radius</td></tr><tr><td>Non Fire Threat (Reference Adapted - AT (Environment))</td><td>Threats existing in a non-fire situation</td><td>u:SuperType</td><td>Downwind hazard distance, maximum weight vapor cloud, relative gas in air density</td></tr></table>

## 4.1.3 Chemical Incident Threats Data Vocabulary

Information on threats reveals the immediate consequences resulting from the chemical hazards presented by the chemical spill incident. Table 9 illustrates the major data elements in this category.

## 4.2 Incident Command System

Based on their assessment of the threats involved in a chemical incident, the response agents collaborate and coordinate their task force for effective incident mitigation. The data vocabulary for the incident command system captures both the response management design and the resulting response operations. During the course of the response, it is important to publish information on the incident command system, as it provides situational awareness of the collective response, clarifies the task assignment and resource allocation, and enforces the command and control (Choi et al. 2004a; Vinze et al. 1999).

## 4.2.1 Response Management Data Vocabulary

We have defined a set of data components such as response facility, incident command system (ICS), response organization, and resources. In Table 10, we briefly describe the related data types.

<table><tr><td colspan="4">Table 10. Response Management Data Vocabulary</td></tr><tr><td>Major Data Element</td><td>Description</td><td>Data Type</td><td>Example Sub-Elements</td></tr><tr><td>Response Facility (Reference Adapted - AT (Environment))</td><td>Response facilities information</td><td>c:StructureType</td><td>Command person, description, activated date, deactivated date</td></tr><tr><td>ICS Unit (Reference Adapted - AT (Community))</td><td>ICS unit management structure</td><td>c:OrganizationType</td><td>Command person, unit category, organization established time, ICS unit sub unit, ICS unit parent unit</td></tr><tr><td>Responder (Reference Adapted - AT (Subject))</td><td>Responder characteristics</td><td>u:PersonType</td><td>Affiliated organization, title, expertise, contact, security clearance level</td></tr><tr><td>Resource (Reference Adapted - AT (Environment))</td><td>Response resource</td><td>em:ResourceType</td><td>Resource name, resource ID, resource location, certification</td></tr><tr><td>Response Organization (Reference Adapted - AT (Community))</td><td>Response organization description</td><td>u:OrganizationType</td><td>Response district, response organization sub organization</td></tr></table>

<table><tr><td colspan="4">Table 11. Response Operation Data Vocabulary</td></tr><tr><td>Major Data Element</td><td>Description</td><td>Data Type</td><td>Example Sub-Elements</td></tr><tr><td>Response Operation Plan (Reference Adapted - AT (Activity))</td><td>Details of response operation planning</td><td>u:SuperType</td><td>Plan name, plan ID, plan objective, plan description, approved date</td></tr><tr><td>Response Organization Association (Reference Adapted - AT (Activity))</td><td>Involvement of organizations in response operation</td><td>u:AssociationType</td><td>Activity reference, response organization reference, is primary organization indicator</td></tr><tr><td>Responder Association (Reference Adapted - AT (Activity))</td><td>Involvement of responders in response operation</td><td>u:AssociationType</td><td>Activity reference, responder reference, role description</td></tr><tr><td>Resource Association (Reference Adapted - AT (Activity))</td><td>Involvement of resource in response operation</td><td>u:AssociationType</td><td>Activity reference, resource reference, quantity</td></tr></table>

## 4.2.2 Response Operations Data Vocabulary

The data model also includes data elements describing response operations. The standardized data structure of response operations facilitates the monitoring, tracking, and analysis of response progress. We illustrate the related data elements in Table 11.

## 5. Case illustration of Data Model Application

The development of a data model contributes to the response information supply chain in that it supports the import and export of information exchange documents and enables the automatic processing of information through end-user processing devices (Aylward et al. 2006; DHS 2005; Frale 2005; Raghu et al. 2004; Raghu et al. 2003; Weinshel 2006). As an illustration, we apply the data vocabulary to a chemical incident in order to standardize a real document that is exchanged during a response. The document (see Figure 5) we studied is titled “Release Report Form.” It is used in western New York and it is exchanged between local hazard material agencies and the New York State Emergency Response Commission to report and manage chemical incidents.

The case provides a close reflection of the utilization of Activity Theory for interoperable information sharing in emergency management. That is, the local hazard material agencies and the New York State Emergency Response Commission (subjects) share the Release Report Form (object) to achieve the situational awareness of the chemical incident (outcome). The information sharing is mediated by the new chemical response data model that standardizes the task-critical data. The document that is exchanged is defined and restricted by the incident management guidelines (rule). Information sharing involves responders from domains such as Haz-Mat, fire, and emergency service (division of labor). Underlying this information sharing are the local, state, and federal response agencies (community). The application demonstrates the effect of the data vocabulary on real-life practices of emergency information interoperability. It further presents a typical process in which the vocabulary may be utilized to leverage existing response capabilities.

To standardize the Release Report Form using our data model, we follow the process adopted from the standard NIEM Information Exchange Package Development process (DHS 2004a). The three phases - namely Modeling, Mapping, and XML Instance Building - transfer the unstructured and un standardized paper documents into a syntactic, structured, and semantically homogeneous XML document. This transfer allows for automatic processing by end-user computer systems and enables easy importing and exporting to share response critical information.

The modeling process analyzes the document content and structure. The domain model categorizes and groups the document fields according to their relevance. For example, the document fields such as date of release, time, amount released, duration, release medium, and location together constitute information about a chemical release. Therefore we group these document fields together (as in composition operation in Object-Oriented Modeling) and create a domain entity named Release. Subsequently, the entire Release Report Form is divided and represented by a set of domain entities.

Based on the domain model, we map the document fields into the data standards in the chemica incident response data model and NIEM. We record the mapping results and illustrate then as a snapshot in Figure 6a. For example, the domain entity of Release is mapped to ReleaseType in the chemical incident response data model. This mapping thus allows the document fields of amount released, duration, release medium, and location to be mapped to corresponding data elements in the ReleaseType. If no exact mapping for a given domain entity can be found in the two data models, we map its elements individually. For instance, the caller name, affiliation, telephone, and reference in the domain entity of Caller are mapped to the corresponding elements in ResponderType while the calldate in Caller is mapped to NIEM u:DayType. The mapping reveals its usefulness and great flexibility in meeting the standardization requirements. The mapping process is followed by the XML instance creation process in which we develop an XML document (see Figure 6b) that the emergency responders can distribute among various agencies.

NEW YORK STATE EMERGENCY RESPONSE CCMMISSION RELEASE REPORT FORM.- SARA TITLE III SECTION 304

State Spil1 Hotline (800) 457-7362

Alternate # State Warning Point (518) 457-2200

1. Callers' Name MIkE WALTERS Ca11 Date 5-26-95 2. Affiliation ERIE CO.DEPT OF EMES.SERUI

5. Amount Released 24:c NETO4/ 1b/gal

6. Date of Release 5-26-95 Time \_Duration  hr \_min 7. Release Medium: airwater land

8. Weather Conditions: CCEA2 SUNNY- LIGHT .NOS

g. Location (St/BIdg. #) ENO OF CITYVIEW AUE Rl: (City/County) TOWU OF HAMBURG ( ERIE /N.Y.

10. Facility (name): (address):

11. EMERGENCY CONTACT (name):

12. Ineident Description: RR DERA/(MENT- 9 TANk CARS FuECOLPE

13. Health Risks:

15. Additional Notifications made: Local Fire Department 1 dial 911 yes no time County Department of Emergency Services- 846-6578 (24 hours) yes no time NYS DEC 1-800-457-7326 yes no time (or) 1-518-457-2200 yes no time Federal National Response Center 1-800-424-8802 yes no time

16. Remarks, etc.

(title) DEP, O.SASTER COCR".

Chen et al./Emergency Response Information System Interoperability

<table><tr><td>Domain Entities</td><td>Document Fields</td><td>Mapping</td><td>Sample Data</td></tr><tr><td rowspan="3">Chemical</td><td>Material Released</td><td>ReleaseReportForm/Chemical/ChemicalName</td><td>Low SulphurDiesel Fuel</td></tr><tr><td>EHS</td><td>ReleaseReportForm/Chemical/IsEHSIndicator</td><td></td></tr><tr><td>CERCLA</td><td>ReleaseReportForm/Chemical/IsCERCLAIndicator</td><td></td></tr><tr><td>ResponsePrecaution</td><td>Precautions</td><td>ReleaseReportForm/ResponsePrecaution/NonFirefightingPrecaution</td><td></td></tr><tr><td>Health Hazard</td><td>Health Risks</td><td>ReleaseReportForm/HealthHazard/HealthHazardSummary</td><td></td></tr><tr><td rowspan="6">Release</td><td>Date of Release</td><td>ReleaseReportForm/Release/ActivityDate</td><td>5-26-95</td></tr><tr><td>Time</td><td>ReleaseReportForm/Release/ActivityTime</td><td></td></tr><tr><td>Amount Release</td><td>ReleaseReportForm/Release/ReleaseAmount</td><td></td></tr><tr><td>Duration</td><td>ReleaseReportForm/Release/ReleaseDuration</td><td></td></tr><tr><td>Location</td><td>ReleaseReportForm/ReleaseType/IncidentLocation</td><td>End of CityViewAvenue Town ofHamburg/Erie/NY</td></tr><tr><td>Release Medium</td><td>ReleaseReportForm/ReleaseType/ReleaseInto</td><td>Land</td></tr><tr><td colspan="4">Figure. 6a Snapshot of Release Report Form Mapping Sheet</td></tr><tr><td colspan="4">&lt;Chemical&gt;&lt;ChemicalName&gt;Low Sulphur Diesel Fuel&lt;/ChemicalName&gt;&lt;/IsEHSIndicator&gt;&lt;/IsEHSIndicator&gt;&lt;/IsCERCLAIndicator&gt;&lt;/IsCERCLAIndicator&gt;&lt;/Chemical&gt;&lt;ResponsePrecaution&gt;&lt;/NonFirefightingPrecaution&gt;&lt;/NonFirefightingPrecaution&gt;&lt;/ResponsPrecautions&gt;&lt;HealthHazard&gt;&lt;HealthHazardSummary&gt;&lt;/HealthHazardSummary&gt;&lt;/HealthHazard&gt;&lt;Release&gt;&lt;ActivityDate&gt;5-26-95&lt;/ActivityDate&gt;&lt;/ActivityTime&gt;&lt;/ActivityTime&gt;&lt;/ReleaseAmount&gt;&lt;/ReleaseAmount&gt;&lt;/ReleaseDuration&gt;&lt;/ReleaseDuration&gt;&lt;IncidentLocation&gt;End of CityView Avenue Town of Hamburg/Erie/NY&lt;/IncidentLocation&gt;&lt;ReleaseInto&gt;Land&lt;/ReleaseInto&gt;&lt;/Release&gt;</td></tr><tr><td colspan="4">Figure. 6b Snapshot of Release Report Form XML Instance</td></tr></table>

The software program “Association Wizard” is developed in Java 5.0 and it functions to semiautomate the mapping process. The software (see Figure 7.a and 7.b) allows the users to navigate through entries in the hierarchy of the data dictionaries to identify the appropriate mappings for the document fields. During the document transformation, the Association Wizard keeps track of the users’ mapping selections and it automatically generates the mapping spreadsheet accordingly. The second software program is an “Auto-Generation” tool designed in Java 5.0 and functions to facilitate XML document instance building. The tool reads the mapping spreadsheet (path and sample data) and automatically produces the corresponding XML document.

The two sets of software programs semi-automate the development of documents compliant with the data model developed in this paper. The current versions of the programs primarily function in relation to the chemical incident response data model and the NIEM data model. They can be extended to incorporate the other data models as long as they are designed in compliance with the NIEM design conventions.

![](/api/attachments/Q7UBNQMG/fulltext/images/2e7b9fa964e3a78f04664d67ab3426fc96504f064c839267398273c56776f9e1.jpg)  
Figure 7a. Process Flow of the Association Wizard Tool

## 7. Conclusion

Information interoperability in the context of emergency response systems remains an understudied area. To this end, our paper informs theory in that it adapts Activity Theory to guide the requirements engineering process and it uses a novel approach to develop a set of data standards to address the challenges of information interoperability. The inclusion of an environment construct enriches the formalisms of Activity Theory, as environment factors impact activities carried out by subjects. In addition, this paper develops the information management framework (Table 6) for emergency management. This framework identifies the key dimensions and requirements in information management. It directly helps the development of a data model and may also contribute to the design of collaborative systems for organizational management in emergency response. This paper also informs practice in that the contribution of this paper includes the development of an XML based data model to allow the sharing of task-critical data across domains in support of day-to-day operations. Such a model removes the barriers in information sharing and also reduces the design and development cost needed to build and implement a robust and agile information supply chain system (Choi et al. 2004b). The paper includes a set of artifacts such as an XML-based data model and the software implementations to facilitate document standardization. Finally, the data model is validated by a panel of domain experts in emergency response and data standard development for comprehensiveness and discrepancy checking (Kim et al. 1995); we present an illustration of the data model application in this paper to exemplify its usefulness in addressing practical issues in the field.

## Welcome to the Association Wizard

This wizard helps you associate your document requirements to the chemical dictionary.

If you need to map a data element of the document to the chemical dictionary, select the items through the wizard.

To continue, lick Next. Next Cancel Help

Enter the root type ReleaseReportForm

Enter the name of the domai entity Chemical

## Select the source class or type:

Source class or type is the data source high-level object, class, or context of a single or set of data elements.

<table><tr><td>ChemicalType- A structure that describes details about the chemical product</td></tr><tr><td>TemperatureMeasureType- A structure that describes details about the temperature measurementActivityInvolvedResponderAssociationType- A structure that describes details about the association between response activity and responder</td></tr><tr><td>ChemicalType- A structure that describes details about the chemical product</td></tr><tr><td>PropertyDamageType- A structure that describes details about the physical property damagesFireExplosionType- A structure that describes details about the potential fire and explosionWeatherType- A structure that describes details about the weather conditionNonFireThreatType- A structure that describes details about the nonfire threatAreaSizeCodeSimpleType- A structure that describes the codes for area size measurement code</td></tr></table>

## Select the source element to be mapped:

<table><tr><td>GeneralDescription-A description or narrative of the chemical properties</td><td></td></tr><tr><td>GeneralDescription-A description or narrative of the chemical properties</td><td>▲</td></tr><tr><td>SpecialNote-A special notes of the NFPA 704 diamond system</td><td rowspan="7">≡</td></tr><tr><td>ResponsePrecaution-A description of the response precautions to the chemical involved incident</td></tr><tr><td>PhysioProperty-A description of the physical property of the chemical</td></tr><tr><td>ChemicalName-A name of the chemical product</td></tr><tr><td>PercentageByWeight-A percentage of the purity</td></tr><tr><td>CASNumber-A CAS number assigned to the chemical</td></tr><tr><td>FireExplosion-A description of the fire and explosion property of the chemical</td></tr></table>

## Figure 7b. Snapshot of Association Wizard Tool

The data model exemplifies several features. First, it contains reusable data components and scalable data structures. Second, with some modifications, the data model is generalizable to other incident types. As suggested by Table 6, information management for incident response consists of two major dimensions: Threat Assessment and Incident Command, each with sub-domain components. A large portion of the Threat Assessment data, including incident setting and generic threats such as injury, casualty, and environmental damages, form part of the core data elements common to other emergency contexts. This commonality is also true for all the elements in the Incident Command System dimension. Figure 8 illustrates the components of the data model that are incident specific and those that are more generalizable to other contexts. Third, the data model is extremely usable. It not only supports the creation of standardized information exchange files as demonstrated in Section 5, it also allows agencies at the local, state, and federal levels to leverage their existing information systems to participate in a national information sharing environment with only a minimal cost to retrofit existing systems and databases (DHS et al. 2006). Since XML-specified data model design is platform independent, individual agencies can easily incorporate a translation mechanism between their heterogeneous databases (Allen et al. 2003; Johansson et al. 2003; March et al. 2003; March et al. 2000a; March et al. 1995; Rho et al. 1997; Rishe et al. 2000; Sarda 2007) and the messaging infrastructure to map incoming and outgoing messages in accordance to the data standards. This implementation model is flexible because it does not require agencies to alter either their legacy systems and databases or the way they currently do business, yet it opens up the possibilities for data exchange among other agencies (Breitbart et al. 1986; Collins et al. 2002; Hammer et al. 1993; Li et al. 2000; Lim et al. 2002; March et al. 1995; Rho et al. 2000; Wei et al. 2001).

The limitations of this study provide several directions for future extensions to this work. In the remainder of this section we elaborate on these extensions.

The data model currently focuses on and identifies the task-critical information that is essential for effective response during chemical incidents. Extending these key standards to include additiona information assurance types in keeping with federal and local regulatory guidelines would make the model more comprehensive.

Figure 8. Illustration of Data Model Generalizability to Other Emergency Contexts  
![](/api/attachments/Q7UBNQMG/fulltext/images/d1cc22038d8a1f90a4a39c669222f1c993ccb1b5f0565d25f3b38a0ebc5e433f.jpg)  
Legend: Shaded components should be replaced with context specific content when extending the current data model to other emergency contexts. The other components are reuseable for all types of emergency.

Despite the fact that responders nationwide utilize similar data sharing practices, the current version of the data model best serves the shared requirements of a portion of the country. The data mode can be enhanced by integrating information sharing practices across the nation and making it a national standard.

Since the chemical response data model provides a systematic overview of the required key response information, future research may include the development of data models for other types of incidents such as fires, severe snowstorms, etc.

The current data model supports collaborative work but currently does not include direct computation of performance metrics to evaluate the efficiency of the response action. Determining appropriate metrics for performance evaluation is beyond the scope of the current study but is a future direction that would provide a valuable extension to the current work.

While the data model enhances the extent of data-level interoperability support, its potentia contribution may be limited by the effectiveness of other dimensions of interoperability such as hardware, middleware, and application layer compatibilities. These represent enormous challenges and require nationwide collaboration across levels of government, public institutions, and the private sector, to coordinate and synergize the development and governance processes. An example of such collaboration is the RapidCom initiative, announced by President Bush on July 22 2004, which initiates, organizes, guides, and supports the national research efforts (e.g., FCC, Office for Interoperability and Compatibility, and Emergency Response Council) to design interoperable communication equipment, operation procedures, communication protocols, training and exercises, and governance structures. Future research also calls for investigation into these issues.

## Acknowledgements

This research has been funded in part by NSF under grant 0705292. The usual disclaimer applies. We would like to thank Dean Messing (Ex-Hazmat Chief and now Deputy Commissioner of Emergency Management at Erie County, NY), Thomas Fitzpatrick (Captain of Hazardous Materials Operations, Buffalo Fire Department, NY), Kilpatrick Woodard (Chemistry Analyst of Hazardous Materials Operations, Buffalo Fire Department, NY), Don Connolly (Hazmat Chief, Brighton Fire Department, Tonawanda, NY), Thomas Coyne (Captain of Communications, Buffalo Fire Department, NY), Dave Humbert (Fire Chief of North Bailey Fire Department, Amherst, NY), James Guy (Ex-Fire Chief and now Chief of Environmental Affairs, University at Buffalo), Dennis Carson (Police Emergency Services Coordinator, Town of Tonawanda, NY), Elysa Jones (Chair of OASIS Emergency Management Technical Committee) for their great help in this research project. A preliminary version of the paper was presented at the CABIT 2006 Symposium, Arizona. We thank the attendees of CABIT 2006 for their comments that have improved the lucidity of the paper. Last but not least we thank the referees and the editors for their comments that have helped improved the paper greatly.

## References

Allen, G.N., and March, S.T. "Modeling Temporal Dynamics for Business Systems," Journal of Database Management (14:3) 2003, pp 21-36.

Arora, H., Mishra, B.K., and Raghu, T.S. "Autonomic Computing Approach to Secure Knowledge Management: A Game-theoretic Analysis," IEEE Transactions on Systems, Man and Cybernetics (36:3) 2006a, pp 487-497.

Arora, H., Raghu, T.S., Vinze, A., and Brittenham, P. "Using the Autonomic Computing Paradigm for Disease Outbreak Monitoring and Response," in: Third IEEE International Conference on Autonomic Computing, 2006b.

Auf der Heide, E. Disaster Response: Principles of Preparation and Coordination Mosby, St. Louis, MI, 1989.

Aylward, D., and Jones, E. "Data Interoperability: Sharing Information for a Safer America," COMCARE Emergency Response Alliance, 2006.

Beech, D. "Data Semantics on the Information Super Highway," in: Database Application Semantics, R.M.a.L. Mark (ed.), Chapman and Hall, 1997.

Bertelsen, O.W., and Bodker, S. "Activity Theory," in: HCI Models Theories, and Frameworks: Toward A Multidisciplinary Science, J.M. Caroll (ed.), Morgan Kaufmann, San Francisco, 2003, pp. 291-324.

BJA-DOJ "NIEM Executive Briefing," D.o. Justice (ed.), 2007.

Breitbart, Y., Olson, P.L., and Thompson, G.R. "Database Integration in a Distributed Heterogeneous Database System," The Second International Conference on Data Engineering IEEE Computer Society, 1986.

Bui, T.X., and Sankaran, S.R. "Design Considerations for A Virtual Information Center for Humanitarian Assistance/Disaster Relief Using Workflow Modeling," Decision Support Systems (31:2) 2001.

Chakravarti, N., Chen, R., Sharman, R., Rao, H.R., and Upadhyaya, S.J. "Common Operating Vocabulary Extensions for Emergency Management: Case of a Chemical Spill Incident," The Fourth Annual CABIT Symposium, Phoenix, AZ, 2006.

Chandrasekaran, B., and kaindl, H. "Representing Functional Requirements and User-System Interactions," AAAI-96 Workshop on Modeling and Reasoning about Function, Fortland, OR, 1996.

Chaudhury, A., Mallick, D.N., and Rao, H.R. "Web Channels in E-Commerce," Communications of the ACM (44:1) 2001, p 99.

Chen, R., Sharman, R., Rao, H.R., and Upadhyaya, S. "Design Principles of Coordinated Multiincident Emergency Response Systems," IEEE International Conference on Intelligence and Security Informatics 2005, Atlanta, GA, 2005.

Chen, R., Sharman, R., Rao, H.R., and Upadhyaya, S. "Design Principles for Critical Incident Response Systems," Information Systems and E-Business Management (5:3) 2007a.

Chen, R., Sharman, R., Rao, H.R., Upadhyaya, S., and Cook-Cottone, C. "Organizational Coordination in Extreme Events: A Case Study of Incident Response for October ’06 Snowstorm in Western New York," The Fifth Pre-ICIS SIG DSS Workshop, Montreal, Canada, 2007b.

Choi, B., Raghu, T.S., and Vinze, A. "Addressing a Standards Creation Process: A Focus on ebXML," International Journal of Human-Computer Studies (61:5) 2004a, pp 627-648.

Choi, B., Raghu, T.S., and Vinze, A. "Standards Setting Process for E-Business: A Focus on ebXML," International Journal of Human Computer Studies (61:5567-746) 2004b.

Collins, S., Navathe, S., and Mark, L. "XML Schema Mapping for Heterogeneous Database Access," Information and Software Technology (44:4) 2002, pp 251-257.

COMCARE "National Mayday Readiness Initiative," COMCARE Emergency Response Alliance, 2002a.

COMCARE "Vehicular Emergency Incident Data Exchange Format Standard," ComCARE Alliance, 2002b.

DHS "National Incident Management System."

DHS "National Incident Management System," D.o.H. Security (ed.), 2004b, p. 138.

DHS "Fact Sheet: Achieving First Responder Communications Interoperability," in: Department of Homeland Security Press, Washington, DC, 2005.

DHS, and DOJ "National Information Exchange Model," Washington, DC, 2006.

DOJ "Building Exchange Content Using the Global Justice XML Data Model," Department of Justice, Washington, DC.

Donzelli, P., and Bresciani, P. "Domain Ontology Analysis in Agent-Oriented Requirements Engineering " in: Knowledge-Based Intelligent Information and Engineering Systems, Springer Berlin / Heidelberg, 2003, pp. 1372-1379.

DOS, Preparedness-Directorate, and U.S.-Fire-Administration "National Fire Incident Reporting System," Washington, DC, 2006.

DOT, Canada, T., and SCT Emergency Response Guidebook, Washington, DC, 2004.

E9-1-1 "Standards for Automatic Location Identification (ALI) Data Exchange, Response & GIS Mapping," Enahnced 911, 2006a.

E9-1-1 "Standards for Local Exchange Carriers, ALI Service Providers & 9-1-1 Jurisdictions," Enhanced 911, 2006b.

EHC "Evaluating Chemical Hazards in the Community," Environmental Health Center, Washington, DC.

EIC "Emergency Interoperability Consortium," Emergency management Technical Commitment, OASIS, 2004.

EIC "Common Alerting Protocol ", Emergency Interoperability Consortium, 2005.

Engestrom, Y. Learning by Expanding: An Activity-Theoretical Approach to Developmental Research

Orienta-Konsultit, Helsinki, 1987.

Engestrom, Y. "Activity Theory and Individual and Social Transformation," in: Perspectives on Activity Theory, R.M.a.R.P. Engeström (ed.), Cambridge University Press, Cambridge, UK, 1999, pp. 19-38.

EPA "Computer-Aided Management of Emergency Operations," United States Environment Protection Agency, 2006.

Fedorowicz, J., Gelinas, U.J., Gogan, J.L., Howard, M., Markus, M.L., Usoff, C., and Vidgen, R. "Modeling Physical Barriers to Interorganizational System Implementation Success," International Journal of Information Technology and Management (forthcoming) 2007.

Finkelstein, A., Goedicke, M., Kramer, J., and Niskier, C. "ViewPoint oriented software development: methods and viewpoints in requirements engineering," in: Algebraic methods II: theory, tools and applications, Springer-Verlag New York, Inc., New York, NY, 1991a, pp. 29-54.

Finkelstein, A., Kramer, J., and Goedicke, M. "Viewpoint Oriented Software Development," Workshop on Software Engineering and its Applications, Toulouse, France, 1991b.

Foulkrod "BASICS: The Information Supply Chain," 2006.

Frale, D. "Emergency Interoperability Consortium Announces Agreement with Department of Homeland Security to Promote Data Sharing During Emergencies," in: PrimeZone Media Network, 2005.

Fuentes, R., Gomez-Sanz, J.J., and Pavon, J. "Social Analysis of Multi-Agent Systems with Activity Theory," 10th Conference of the Spanish Association for Artificial Intelligence, 2003.

GAO "Chemical Safety: Emergency Response Community Views on the Adequacy of Federally Required Chemical Information," United State General Accounting Office, Washington, DC.

Gogan, J.L., Williams, C.B., and Fedorowicz, J. "Fatal Flaws in Information Sharing," International Journal of Technology, Knowledge and Society (1:5) 2005, pp 93-100.

Goodchild, M., Egenhofer, M., and Fegeas, R. "Interoperating GISs: Report of a Specialist Meeting Held under the Auspices of the Varenius Project, Panel on Computational Implementations of Geographic Concepts," National Center for Geographic Information and Analysis, Santa Barbara, CA.

Gupta, A., and Jain, R. "Visual Information Retrieval," Communications of the ACM (40:5) 1997, pp 70-79.

Gutknecht, M. "Innovating the Product Information Supply Chain," XEROX Global Services.

Hammer, J., and McLeod, D. "An Approach to Resolving Semantic Heterogeneity in a Federation o Autonomous, Heterogeneous Database Systems," Journal of Intelligent & Cooperative Information Systems (2:1) 1993, pp 51-83.

Harrison, T., Gil-Garcia, J.R., Pardo, T.A., and Fiona, T. "Learning about Interoperability for Emergency Response: Geographic Information Technologies and the World Trade Center Crisis," The Thirty-Ninth Annual Hawaii International Conference on System Sciences, Computer Society Press, Hawaii, 2006.

HL7 "HL7 Messaging Protocol," Health Level 7, 2006.

Howard, P. "Product Data Quality in the Information Supply Chain," 2007.

Hull, R., and King, R. "Semantic Database Modelling: Survey, Applications, and Research Issues," ACM Computer Survey (19:3) 1987, pp 201-260.

IEEE "IEEE Standard Computer Dictionary: A Compilation of IEEE Standard Computer Glossaries," Institute of Electrical and Electronics Engineers, New York, NY.

IEEE "IEEE Std. 1512 Standards for Common Incident Message Sets," IEEE Std 1512 Working Group, 2000.

Johansson, J.M., March, S.T., and Naumann, J.D. "Modeling Network Latency and Parallel Processing in Distributed Database Design," Decision Sciences Journal (34:4) 2003.

Johnston, M. "The Information Supply Chain: Data Integrity Rises in Stature," in: Supply Chain Management, 2005.

Jump, P., and Bruce, J. "The Response Factor," in: Electric Perspectives, 2003, p. 22.

Kaptelinin, V., and Nardi, B.A. Acting with Technology: Activity Theory and Interaction Design MIT Press, Cambridge, MA, 2006.

Kashyap, V., and Sheth, A. "Semantic heterogeneity in Global Information Systems: The Role of Metadata, Context, and Ontologie," in: Cooperative Information Systems: Current Trends and Directions, M.P.a.G. Schlageter (ed.), Academic Press, 1998, pp. 139-178.

Kean, T.H. "The 9/11 Commission Report," N.C.o.T. Attacks (ed.), 2004.

Khan, S. "Information Supply Chain: Aligning Diverse Teams to Minimize Time-To-Revenue for High-Tech Products," in: Product Management Review, 2007.

Kim, J.K., Sharman, R., Rao, H.R., and Upadhyaya, S. "An Investigation of Risk Management Issues in the Context of Emergency Response Systems," Eleventh Americas Conference on Information Systems, Omaha, NB, 2005.

Kim, J.K., Sharman, R., Rao, H.R., and Upadhyaya, S. "Efficency of Critical Incident Management Systems: Instrument Development and Validation," Decision Support Systems (44:1) 2007.

Kim, Y.-G., and March, S.T. "Comparing Data Modeling Formalisms," Communications of the ACM (38:6) 1995, p 103.

Kotinurmi, P., Nurmilaakso, J.-M., and Laesvuori, H. "Standardization of XML-Based E-Business Frameworks," Standard Making: A Critical Research Frontier for Information Systems, Seattle, WA, 2003.

Kotonya, G. "Practical Experience with Viewpoint-Oriented Requirements Specification," Requirements Engineering (4:3) 1999, pp 115-133.

Kuhn, K.A., and Guise, D.A. "From Hospital Information Systems to Health Information Systems - Problems, Challenges, Perspectives," Yearbook of medical Informatics) 2001, pp 63-76.

Kuutti, K. "Activity Theory and its Applications to Information Systems Research and Development," in: Information Systems Research: Contemporary Approaches and Emergent Traditions, H.K.K.a.R.H. H-E. Nissen (ed.), Elsevier, Amsterdam, 1991, pp. 529-549.

Lee, J., Upadhyaya, S.J., Rao, H.R., and Sharman, R. "Secure Knowledge Management and the Semantic Web," Communications of the ACM (to be appear) 2005.

Leont'ev, A. Problems of the Development of Mind Progress Press, Moscow, 1981.

Li, W.S., and Clifton, C. "SEMINT: A Tool for Identifying Attribute Correspondences in Heterogeneous Databases using Neural Networks," Data and Knowledge Engineering (33) 2000, pp 49-84.

Lim, J.B., and Hurson, A.R. "Transaction Processing in Mobile, Heterogeneous Database Systems," IEEE Transaction on Knowledge and Data Engineering (14:6) 2002, pp 1330-1346.

March, S.T., and Hevner, A.R. "Integrated Decision Support: A Data Warehousing Perspective," AIS SIGDSS Pre-ICIS Workshop Research Directions on Decision Support, 2003.

March, S.T., Hevner, A.R., and Ram, S. "Research Commentary: An Agenda for Information Technology Research in Heterogeneous and Distributed Environments," Information Systems Research (11:4) 2000a, pp 327-341.

March, S.T., and Rho, S. "Allocating Data and Operations to Nodes in Distributed Database Design," IEEE Transactions on Knowledge and Data Engineering (7:2) 1995, pp 305-317.

March, S.T., and Rho, S. "A Semantic Object-Oriented Data Access System," Information Systems and E-Business Management (25:1) 2000b, pp 23-41.

Marinos, G. "The Information Supply Chain: Achieving Business Objectives by Enhancing Critical Business Processes," in: DM Review, 2005.

Mylopoulos, J., Chung, L., and Yu, E. "From Object-Oriented to Goal-Oriented Requirements Analysis," Communications of the ACM (42:1) 1999, pp 31-37.

Nardi, B.A. Context and Consciousness: Activity Theory and Human-Computer Interaction MIT Press, Cambridge, MA, 1996.

NEMSIS "EMS Data Dictionary," National Emergency Medical Services Information System Technical Assistance Center, 2007.

NIEM "NIEM Concept of Operations," Washing, DC.

Nuseibeh, B., Finkelstein, A., and Kramer, J. "Method Engineering for Multi-Perspective Software Development," Information and Software Technology (38:4) 1996, pp 267-274.

O'Leary, D. "An Activity Theory Framework for DSS for Extreme Events: With a Hurricane Example," Pre-ICIS SIG DSS Workshop 2007, Montreal, Canada, 2007.

OASIS "Emergency Data Exchange Language," OASIS Emergency Management Technical Committee, 2005.

Peckham, J., and Maryanski, F. "Semantic Data Models," ACM Computer Survey (20:3) 1988, pp 153-189.

PHIN "PHIN Vocabulary Standards and Specifications," Center for Disease Control and Prevention, 2005.

Porter, M.E. Competitive Advantage: Creating and Sustaining Superior Performance The Free Press,

New York, 1985.

Raghu, T.S., Jayaraman, B., and Rao, H.R. "Toward an Integration of Agent- and Activity-Centric Approaches in Organizational Process Modeling: Incorporating Incentive Mechanisms," Information Systems Research (15:4) 2004.

Raghu, T.S., Rao, H.R., and Sen, P.K. "Relative Performance of Incentive Mechanisms: Computational Modeling and Simulation of Delegated Investment Decisions," Management Science (49:2) 2003, pp 160-178.

Raghu, T.S., and Vinze, A. "A Business process Context for Knowledge Management," Decision Support Systems (43:3) 2007, pp 1062-1079.

Reddy, M.P., Prasad, B.E., and Reddy, P.G. "A Methodology for Integration of Heterogeneous Databases," IEEE Transactions on Knowledge and Data Engineering (6:6) 1994, pp 920-933.

Rho, S., and March, S.T. "An Analysis of Semantic Overload in Database Access Systems Using Mulit-Table Query Formulation," Journal of Database Management (8:2) 1997.

Rho, S., and March, S.T. "A Decision Support Tool for Distributed Database Design," Seoul Journal of Business (6:1/2) 2000, pp 71-111.

Rishe, N., Athauda, R.I., Yuan, J., and Chen, S.-C. "Knowledge Management for Database Interoperability," The ISCA 2nd International Conference On Information Reuse And Integration (IRI-2000), Honolulu, Hawaii, 2000, pp. 23-26.

Sarda, N.L. "Ontology-Enabled Database Management Systems," in: Ontologies in the Context of Information Systems, R.R.a.S.R. Kishore Rajiv (ed.), Springer Verlag, 2007.

Sciore, E., Siegel, M., and Rosenthal, A. "Using Semantic Values to Facilitate Interoperability Among Heterogeneous Information Systems," ACM Transactions on Database Systems (19:2) 1994, pp 254-290.

Shen, S.Y., and Shaw, M.J. "Managing Coordination in Emergency Response Systems with Information Technologies," Tenth American Conference on Information Systems, New York, 2004, pp. 2110-2120.

SICOP "Semantic Interoperability at Work: Improving Rapid First Response," Semantic Interoperability Community of Practice.

Sidell, F.R., Patrick, W.C., and Dashiell, T.R. Jane's Chem-Bio Handbook jane's Information Group, Alexandria, VA, 2000.

Simsion, G.C., and Witt, G.C. Data Modeling Essentials The Coriolis Group, Scottsdale, AZ, 2001.

Sommerville, I., Sawyer, P., and Viller, S. "Viewpoints for Requirements Elicitation: A Practical Approach," IEEE International Conference on Requirement Engineering, Colorado Springs, CO, 1998.

Steen, M.W.A., Akehurst, D.H., ter Doest, H.W.L., and Lankhorst, M.M. "Supporting Viewpoint-Oriented Enterprise Architecture," Enterprise Distributed Object Computing Conference, 2004.

Stegwee, R.A., and Rukanova, B.D. "Identification of Different Types of Standards for Domain-Specific Interoperability," Standard Making: A Critical Research Frontier for Information Systems, Seattle, WA, 2003.

Sun, S., and Yen, J. "Information Supply Chain: A Unified Framework for Information - Sharing," IEEE International Conference on Intelligence and Security Informatics, Atlanta, GA, 2005.

Townsend, F.F. "The Federal Response to Hurricane Katrina Lessons Learned," T.W. House (ed.), The White House, Washington, DC, 2006.

Turoff, M. "Past and Future Emergency Response Information Systems," Communications of the ACM (45:4) 2002, pp 29-32.

Turoff, M., Chumer, M., Van de Walle, B., and Yao, X. "The Design of A Dynamic Emergency Response Management Information System (DERMIS)," Journal of Information Technology Theory and Application (5:4) 2004.

Uden, L., and Kumaresan, A. "Usable Collaborative Email Requirements Using Activity Theory," Informatics (31) 2007, pp 71-83.

Vinze, A. "What is the Information Supply Chain," 2006.

Vinze, A., Ei-Shinnawy, M., Charles, S., and Poole, M.S. "Collaborative Systems for the Management of Resource Conflicts," America Conference on Information Systems Indianapolis, 1999.

Vinze, A., Santanam, R.T., and Choi, B.-J. "Understanding Standards Setting in the E-Business Context: A Focus on ebXML," America Conference on Information Systems, 2001.

Vygotsky, L.S. Mind and Society Harvard University Press, Cambridge, MA, 1978.

Wang, Y.R., and Madnick, S.E. "A Polygen Model for Heterogeneous Database Systems: The Source Tagging Perspective," The 16th VLDB Conference, Brisbane, Australia, 1990.

Webb, I., Robertson, M., and Fluck, A. "Activity Theory," University of Tasmania, 2006.

Wei, C., Hu, P., and Sheng, O.R.L. "A Knowledge-based System for Patient Image Pre-fetching in Heterogeneous Database Environments: Modeling, Design and Evaluation," IEEE Transactions on Information Technology on Biomedicine (5:1), March 2001, pp 33-45.

Weinshel, K. "UTC Promotes Emergency Response Interoperability," The United Telecom Council Washing, DC.

West, M. "Developing High Quality Data Models," European Process Industries STEP Technical Liaison Executive, London, UK.

Williams, C.B., Gogan, J.L., and Fedorowicz, J. "Public Safety and Cross-Boundary Data Sharing: Lessons from the CapWIN Project," IEEE Computer (38:12) 2005, p 28.

Zhang, H., Kishore, R., Sharman, R., and Ramesh, R. "Agile Integration Modeling Language (AIML): A conceptual modeling grammar for agile integrative business information systems," Decision Support Systems (44:1) 2007, pp 266-284.

Zowghi, D., and Coulin, C. "Requirement Elicitation: A Survey of Techniques, Approaches, and Tools," in: Engineering and Managing Software Requirements, Springer Berlin Heidelberg, 2005, pp. 19-46.

## Appendices

(Available at http://www.som.buffalo.edu/isinterface/ray/appendix/appendix.htm)

A. Summary of National Efforts in Emergency Management Interoperability

B. Full Version of Data Type Illustration

C. Data Model Specification

D. Data Dictionary XML Schema

E. Enlarged Version of Figure 4

## About the Authors

Rui Chen is currently a Ph.D. candidate of Management Science and Systems at State University of New York at Buffalo. His research interests are in the areas of information assurance, emergency management, coordination and collaboration, and information technology outsourcing.

Raj Sharman is a faculty member in the Management Science and Systems Department at SUNY Buffalo, NY. He received his B. Tech and M. Tech degree from IIT Bombay, India and his M.S degree in Industrial Engineering and PhD in Computer Science from Louisiana State University. His research streams include Information Assurance, and Disaster Response Management, Decision Support Systems, and Distributed Computing. His papers have been published in a number of national and international journals. He is also the recipient of several grants from the university as well as external agencies.

Nirupama Chakravarti has a Masters in Computer Science from the State University of New York at Buffalo. She is currently working as an independent consultant

H. Raghav Rao graduated from Krannert Graduate School of Management at Purdue University. His interests are in the areas of management information systems, decision support systems, e-business, emergency response management systems and information assurance. He has chaired sessions at international conferences and presented numerous papers. He also has co-edited four books of which one is on Information Assurance in Financial Services. He has authored or co-authored more than 150 technical papers, of which more than 75 are published in archival journals. His work has received best paper and best paper runner up awards at AMCIS and ICIS. Dr. Rao has received funding for his research from the National Science Foundation, the Department of Defense and the Canadian Embassy and he has received the University's prestigious Teaching Fellowship. He has also received the Fulbright fellowship in 2004. He is a co-editor of a special issue of The Annals of Operations Research, the Communications of ACM, associate editor of Decision Support Systems, Information Systems Research and IEEE Transactions in Systems, Man and Cybernetics, and coEditor- in -Chief of Information Systems Frontiers. Dr Rao also has a courtesy appointment with Computer Science and Engineering as adjunct Professor. Prof Rao is also the recipient of the 2007 State University of New York Chancellor's award for excellence in scholarship and creative activities.

Shambhu J. Upadhyaya, Ph.D. is an Associate Professor of Computer Science and Engineering at the State University of New York at Buffalo where he also directs the Center of Excellence in Information Systems Assurance Research and Education, designated by the National Security Agency and the Department of Homeland Security. His research interests are information assurance, computer security, fault diagnosis, fault tolerant computing, and VLSI Testing. He has authored or coauthored more than 200 articles in refereed journals and conferences in these areas. He was a guest co-editor of the book Managing Information Assurance in Financial Services, IGI Global, 2007 and was a guest co-editor of a special issue on Secure Knowledge Management in IEEE Transactions on Systems, Man and Cybernetics, May 2006. He is on the Program Committees o several international conferences and workshops. He is a senior member of IEEE.

Copyright © 2008, by the Association for Information Systems. Permission to make digital or hard copies of all or part of this work for personal or classroom use is granted without fee provided that copies are not made or distributed for profit or commercial advantage and that copies bear this notice and full citation on the first page. Copyright for components of this work owned by others than the Association for Information Systems must be honored. Abstracting with credit is permitted. To copy otherwise, to republish, to post on servers for commercial use, or to redistribute to lists requires prior specific permission and/or fee. Request permission to publish from: AIS Administrative Office, P.O. Box 2712 Atlanta, GA, 30301-2712 Attn: Reprints, or via e-mail from ais@gsu.edu.

ISSN: 1536-9323

Editor Kalle Lyytinen Case Western Reserve University, USA

<table><tr><td colspan="4">Senior Editors</td></tr><tr><td>Izak Benbasat</td><td>University of British Columbia, Canada</td><td>Robert Fichman</td><td>Boston College, USA</td></tr><tr><td>Varun Grover</td><td>Clemson University, USA</td><td>Rudy Hirschheim</td><td>Louisiana State University, USA</td></tr><tr><td>Juhani livari</td><td>University of Oulu, Finland</td><td>Robert Kauffman</td><td>University of Minnesota, USA</td></tr><tr><td>Frank Land</td><td>London School of Economics, UK</td><td>Jeffrey Parsons</td><td>Memorial University of Newfoundland, Canada</td></tr><tr><td>Suzanne Rivard</td><td>Ecole des Hautes Etudes Commerciales, Canada</td><td>Bernard C.Y. Tan</td><td>National University of Singapore, Singapore</td></tr><tr><td>Yair Wand</td><td>University of British Columbia, Canada</td><td></td><td></td></tr><tr><td colspan="4">Editorial Board</td></tr><tr><td>Steve Alter</td><td>University of San Francisco, USA</td><td>Michael Barrett</td><td>University of Cambridge, UK</td></tr><tr><td>Cynthia Beath</td><td>University of Texas at Austin, USA</td><td>Anandhi S. Bharadwaj</td><td>Emory University, USA</td></tr><tr><td>Francois Bodart</td><td>University of Namur, Belgium</td><td>Marie-Claude Boudreau</td><td>University of Georgia, USA</td></tr><tr><td>Susan A. Brown</td><td>University of Arizona, USA</td><td>Tung Bui</td><td>University of Hawaii, USA</td></tr><tr><td>Dave Chatterjee</td><td>University of Georgia, USA</td><td>Patrick Y.K. Chau</td><td>University of Hong Kong, China</td></tr><tr><td>Wynne Chin</td><td>University of Houston, USA</td><td>Ellen Christiaanse</td><td>University of Amsterdam, Nederland</td></tr><tr><td>Mary J. Culnan</td><td>Bentley College, USA</td><td>Jan Damsgaard</td><td>Copenhagen Business School, Denmark</td></tr><tr><td>Samer Faraj</td><td>University of Maryland, College Park, USA</td><td>Chris Forman</td><td>Carnegie Mellon University, USA</td></tr><tr><td>Guy G. Gable</td><td>Queensland University of Technology, Australia</td><td>Dennis Galletta</td><td>University of Pittsburg, USA</td></tr><tr><td>Hitotora Higashikuni</td><td>Tokyo University of Science, Japan</td><td>Kai Lung Hui</td><td>National University of Singapore, Singapore</td></tr><tr><td>Bill Kettinger</td><td>University of South Carolina, USA</td><td>Rajiv Kohli</td><td>College of William and Mary, USA</td></tr><tr><td>Chidambaram Laku</td><td>University of Oklahoma, USA</td><td>Ho Geun Lee</td><td>Yonsei University, Korea</td></tr><tr><td>Jae-Nam Lee</td><td>Korea University</td><td>Kai H. Lim</td><td>City University of Hong Kong, Hong Kong</td></tr><tr><td>Mats Lundeberg</td><td>Stockholm School of Economics, Sweden</td><td>Ann Majchrzak</td><td>University of Southern California, USA</td></tr><tr><td>Ji-Ye Mao</td><td>Remnin University, China</td><td>Anne Massey</td><td>Indiana University, USA</td></tr><tr><td>Emmanuel Monod</td><td>Dauphine University, France</td><td>Eric Monteiro</td><td>Norwegian University of Science and Technology, Norway</td></tr><tr><td>Mike Newman</td><td>University of Manchester, UK</td><td>Jonathan Palmer</td><td>College of William and Mary, USA</td></tr><tr><td>Paul Palou</td><td>University of California, Riverside, USA</td><td>Yves Pigneur</td><td>HEC, Lausanne, Switzerland</td></tr><tr><td>Dewan Rajiv</td><td>University of Rochester, USA</td><td>Sudha Ram</td><td>University of Arizona, USA</td></tr><tr><td>Balasubramaniam Ramesh</td><td>Georgia State University, USA</td><td>Timo Saarinen</td><td>Helsinki School of Economics, Finland</td></tr><tr><td>Rajiv Sabherwal</td><td>University of Missouri, St. Louis, USA</td><td>Raghu Santanam</td><td>Arizona State University, USA</td></tr><tr><td>Susan Scott</td><td>The London School of Economics and Political Science, UK</td><td>Olivia Sheng</td><td>University of Utah, USA</td></tr><tr><td>Carsten Sorensen</td><td>The London School of Economics and Political Science, UK</td><td>Ananth Srinivasan</td><td>University of Auckland, New Zealand</td></tr><tr><td>Katherine Stewart</td><td>University of Maryland, USA</td><td>Mani Subramani</td><td>University of Minnesota, USA</td></tr><tr><td>Dov Te&#x27;eni</td><td>Tel Aviv University, Israel</td><td>Viswanath Venkatesh</td><td>University of Arkansas, USA</td></tr><tr><td>Richard T. Watson</td><td>University of Georgia, USA</td><td>Bruce Weber</td><td>London Business School, UK</td></tr><tr><td>Richard Welke</td><td>Georgia State University, USA</td><td>George Westerman</td><td>Massachusetts Institute of Technology, USA</td></tr><tr><td>Youngjin Yoo</td><td>Temple University, USA</td><td>Kevin Zhu</td><td>University of California at Irvine, USA</td></tr><tr><td colspan="4">Administrator</td></tr><tr><td>J. Peter Tinsley</td><td>AIS, Executive Director</td><td colspan="2">Association for Information Systems, USA</td></tr><tr><td>Reagan Ramsower</td><td>Publisher</td><td colspan="2">Baylor University</td></tr></table>

ISSN: 1536-9323

Editor Kalle Lyytinen Case Western Reserve University, USA

<table><tr><td colspan="4">Senior Editors</td></tr><tr><td>Izak Benbasat</td><td>University of British Columbia, Canada</td><td>Robert Fichman</td><td>Boston College, USA</td></tr><tr><td>Varun Grover</td><td>Clemson University, USA</td><td>Rudy Hirschheim</td><td>Louisiana State University, USA</td></tr><tr><td>Juhani livari</td><td>University of Oulu, Finland</td><td>Robert Kauffman</td><td>University of Minnesota, USA</td></tr><tr><td>Frank Land</td><td>London School of Economics, UK</td><td>Jeffrey Parsons</td><td>Memorial University of Newfoundland, Canada</td></tr><tr><td>Suzanne Rivard</td><td>Ecole des Hautes Etudes Commerciales, Canada</td><td>Bernard C.Y. Tan</td><td>National University of Singapore, Singapore</td></tr><tr><td>Yair Wand</td><td>University of British Columbia, Canada</td><td></td><td></td></tr><tr><td colspan="4">Editorial Board</td></tr><tr><td>Steve Alter</td><td>University of San Francisco, USA</td><td>Michael Barrett</td><td>University of Cambridge, UK</td></tr><tr><td>Cynthia Beath</td><td>University of Texas at Austin, USA</td><td>Anandhi S. Bharadwaj</td><td>Emory University, USA</td></tr><tr><td>Francois Bodart</td><td>University of Namur, Belgium</td><td>Marie-Claude Boudreau</td><td>University of Georgia, USA</td></tr><tr><td>Susan A. Brown</td><td>University of Arizona, USA</td><td>Tung Bui</td><td>University of Hawaii, USA</td></tr><tr><td>Dave Chatterjee</td><td>University of Georgia, USA</td><td>Patrick Y.K. Chau</td><td>University of Hong Kong, China</td></tr><tr><td>Wynne Chin</td><td>University of Houston, USA</td><td>Ellen Christiaanse</td><td>University of Amsterdam, Nederland</td></tr><tr><td>Mary J. Culnan</td><td>Bentley College, USA</td><td>Jan Damsgaard</td><td>Copenhagen Business School, Denmark</td></tr><tr><td>Samer Faraj</td><td>University of Maryland, College Park, USA</td><td>Chris Forman</td><td>Carnegie Mellon University, USA</td></tr><tr><td>Guy G. Gable</td><td>Queensland University of Technology, Australia</td><td>Dennis Galletta</td><td>University of Pittsburg, USA</td></tr><tr><td>Hitotora Higashikuni</td><td>Tokyo University of Science, Japan</td><td>Kai Lung Hui</td><td>National University of Singapore, Singapore</td></tr><tr><td>Bill Kettinger</td><td>University of South Carolina, USA</td><td>Rajiv Kohli</td><td>College of William and Mary, USA</td></tr><tr><td>Chidambaram Laku</td><td>University of Oklahoma, USA</td><td>Ho Geun Lee</td><td>Yonsei University, Korea</td></tr><tr><td>Jae-Nam Lee</td><td>Korea University</td><td>Kai H. Lim</td><td>City University of Hong Kong, Hong Kong</td></tr><tr><td>Mats Lundeberg</td><td>Stockholm School of Economics, Sweden</td><td>Ann Majchrzak</td><td>University of Southern California, USA</td></tr><tr><td>Ji-Ye Mao</td><td>Remnin University, China</td><td>Anne Massey</td><td>Indiana University, USA</td></tr><tr><td>Emmanuel Monod</td><td>Dauphine University, France</td><td>Eric Monteiro</td><td>Norwegian University of Science and Technology, Norway</td></tr><tr><td>Mike Newman</td><td>University of Manchester, UK</td><td>Jonathan Palmer</td><td>College of William and Mary, USA</td></tr><tr><td>Paul Palou</td><td>University of California, Riverside, USA</td><td>Yves Pigneur</td><td>HEC, Lausanne, Switzerland</td></tr><tr><td>Dewan Rajiv</td><td>University of Rochester, USA</td><td>Sudha Ram</td><td>University of Arizona, USA</td></tr><tr><td>Balasubramaniam Ramesh</td><td>Georgia State University, USA</td><td>Timo Saarinen</td><td>Helsinki School of Economics, Finland</td></tr><tr><td>Rajiv Sabherwal</td><td>University of Missouri, St. Louis, USA</td><td>Raghu Santanam</td><td>Arizona State University, USA</td></tr><tr><td>Susan Scott</td><td>The London School of Economics and Political Science, UK</td><td>Olivia Sheng</td><td>University of Utah, USA</td></tr><tr><td>Carsten Sorensen</td><td>The London School of Economics and Political Science, UK</td><td>Ananth Srinivasan</td><td>University of Auckland, New Zealand</td></tr><tr><td>Katherine Stewart</td><td>University of Maryland, USA</td><td>Mani Subramani</td><td>University of Minnesota, USA</td></tr><tr><td>Dov Te&#x27;eni</td><td>Tel Aviv University, Israel</td><td>Viswanath Venkatesh</td><td>University of Arkansas, USA</td></tr><tr><td>Richard T. Watson</td><td>University of Georgia, USA</td><td>Bruce Weber</td><td>London Business School, UK</td></tr><tr><td>Richard Welke</td><td>Georgia State University, USA</td><td>George Westerman</td><td>Massachusetts Institute of Technology, USA</td></tr><tr><td>Youngjin Yoo</td><td>Temple University, USA</td><td>Kevin Zhu</td><td>University of California at Irvine, USA</td></tr><tr><td colspan="4">Administrator</td></tr><tr><td>J. Peter Tinsley</td><td>AIS, Executive Director</td><td colspan="2">Association for Information Systems, USA</td></tr><tr><td>Reagan Ramsower</td><td>Publisher</td><td colspan="2">Baylor University</td></tr></table>
