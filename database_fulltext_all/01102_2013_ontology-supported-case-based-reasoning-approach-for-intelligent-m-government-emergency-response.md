---
otero_id: 1102
otero_key: "ETS2V74N"
title: "Ontology-supported case-based reasoning approach for intelligent m-Government emergency response services"
authors: "Khaled Amailef; Jie Lu"
year: "2013"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2012.12.034"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Ontology-supported case-based reasoning approach for intelligent m-Government emergency response services

Khaled Amailef, Jie Lu ⁎

Decision Systems & e-Service Intelligence (DeSI) Lab, Centre for Quantum Computation & Intelligent Systems (QCIS), School of Software, Faculty of Engineering and Information Technology, University of Technology Sydney, PO Box 123, Broadway, NSW 2007, Sydney, Australia

## a r t i c l e i n f o

Article history: Received 30 June 2012 Received in revised form 9 December 2012 Accepted 30 December 2012 Available online 17 January 2013

Keywords: Emergency response systems Ontology Case-based reasoning m-Government Mobile-based systems Information extraction

## a b s t r a c t

There is a critical need to develop a mobile-based emergency response system (MERS) to help reduce risks in emergency situations. Existing systems only provide short message service (SMS) noti<sup>fi</sup>cations, and the decision support is weak, especially in man-made disaster situations. This paper presents a MERS ontology-supported case-based reasoning (OS-CBR) method, with implementation, to support emergency decision makers to effectively respond to emergencies. The advantages of the OS-CBR approach is that it builds a case retrieving process, which provides a more convenient system for decision support based on knowledge from, and solutions provided for past disaster events. The OS-CBR approach includes a set of algorithms that have been successfully implemented in four components: data acquisition; ontology; knowledge base; and reasoning; as a sub-system of the MERS framework. A set of experiments and case studies validated the OS-CBR approach and application, and demonstrate its ef<sup>fi</sup>ciency.

Crown Copyright © 2013 Published by Elsevier B.V. All rights reserved.

## 1. Introduction

Emergency response systems (ERS) are used by organizations to assist in responding to an emergency situation. These systems support communications, data gathering, data analysis, and decisionmaking for an emergency response. They are rarely used, but when needed, must function well and without fail [24]. Due to the increasing threat of terrorist attacks, bush<sup>fi</sup>res, <sup>fl</sup>oods and other disasters, the need for effective emergency response systems has been recognized globally [5]. An emergency response demands fast and effective action, and collaboration between numerous people and groups [21].

Mobile and wireless technologies now provide high speed data transfer, and a large range of information and services can now be accessed using mobile devices. Mobile phones and other devices, such as Personal Digital Assistants (PDA), include a number of facilities such as text, audio and video data transfer. The users of mobile phones can easily now communicate by voice, email or short message service (SMS), send images, and stream audio and video <sup>fi</sup>les [28]. The International Telecommunications Union (ITU) [12] reported that the total number of mobile users worldwide, as of late 2010, is estimated to be 5.3 billion, which represent more than 90% of the world's population, and 80% of the population living in rural areas. Between 2007 and 2010, 6.1 trillion SMS text messages have been sent internationally. In other words, about 200,000 text messages are sent every second, thereby enabling citizens to use mobile technologies to access information anytime, anywhere. In an emergency response system, mobile technology can be used to link citizens, businesses, and nonpro<sup>fi</sup>t organizations, government agencies, etc. For example, in an emergency situation such as the 9/11 terrorist attack, mobile technology could be used to enhance productivity, provide rapid connectivity and response in the disaster situation, and provide rapid access to information on an anywhere–anytime basis. This is the focus for the research into emergency response systems based on mobile technology.

A mobile-based emergency response system (MERS) has been designed as one of the important new services of m-Government. It aims to support mobile users by providing information about an emergency situation through their mobile phones, and to help the government to reduce risks by providing effective advice, assistance and information. The MERS consists of <sup>fi</sup>ve major applications: registration, monitoring, analysis, decision support, and warning generation. The MERS is a general SMS-based response system and the SMS is in English. Australia is used as an example in this study to help understand how the MERS works.

Case-based reasoning (CBR) approaches [30,31] support emergency decision makers for an ERS. The bene<sup>fi</sup>t of using the CBR approach is to provide a more convenient retrieving process in disaster situations in order to reach conclusions and give recommendations based on knowledge from previous disaster events. According to Recio-Garía and Díaz-Agudo [25], ontology would support CBR approach in the following ways. As a vocabulary, ontology enables us to de<sup>fi</sup>ne case structure. As a terminology, ontology allows us to de<sup>fi</sup>ne the query vocabulary. Ontology facilitates similarity assessment by making a connection between the query terminology and the case base terminology. Therefore, an ontology-supported CBR (OS-CBR) approach will be developed in this study into the MERS.

This paper's contribution is to develop an innovative OS-CBR approach based on the CBR method, combined with ontology technology that is capable of improving the ef<sup>fi</sup>ciency of decision makers in an emergency situation. This new OS-CBR system has the ability to learn from past situations and to generate solutions for new problems based on past solutions provided for earlier problems.

The proposed ontology-supported case-based reasoning (OS-CBR) approach is novel and has been implemented in the mobile-based response system (MERS) to support emergency decision makers to effectively respond to an emergency situation. It is signi<sup>fi</sup>cant in both theory and practice.

The novelty of the OS-CBR approach includes three particular features:

(1) This approach builds a new case retrieving process to provide a more convenient decision support system based on knowledge from, and solutions provided for past similar disaster events;

(2) This approach includes the development of three new algorithms:

(a) a new extraction intelligent aggregation algorithm to fuse information from different resources in MERS;

(b) a new case retrieval algorithm using fuzzy sets to handle uncertainties;

(c) a new case adaptation algorithm for response generation;

(3) This approach is the <sup>fi</sup>rst to develop and apply ontology for real-time knowledge management in emergency response systems.

Importantly, the OS-CBS approach has been successfully implemented in four components as a sub-system of the MERS framework: data acquisition, knowledge base, knowledge presentation and reasoning.

The paper is organized as follows. Section 2 presents a literature review on of emergency response systems. Section 3 presents the ontology-supported CBR approach and related algorithms. Section 4 explains the implementation of the OS-CBR approach as a subsystem in the MERS. Section 5 reports experimental results and examines the performance of the OS-CBR approach. An evaluation of the performance of OS-CBR approach is provided in Section 6. Conclusions and further study are presented in Section 7.

## 2. Literature review of emergency response systems

This section brie<sup>fl</sup>y outlines the important literature relating to emergency response systems research. Speci<sup>fi</sup>cally, it presents relevant literature on traditional emergency response systems and web-based emergencies, particularly in the area of emergency response systems related to disasters and public safety.

## 2.1. Traditional emergency response systems

Traditional emergency response systems have been used for reporting emergencies and requesting police, <sup>fi</sup>re, medical assistance, and rescue services. These emergency methods are based on two communication models: 1) many-to-one, a telephone-based emergency report system, and, 2) one-to-many, a top-down aid distribution system.

Small-scale and local environmental emergency events can usually be handled by traditional emergency response systems; however, a large-scale environmental emergency, such as a strong earthquake, tsunami, extensive <sup>fl</sup>ood or <sup>fi</sup>re, biochemical attack, or severe nuclear radiation escape, are more complicated situations that can block and disable phone systems. Clear and immediate communication is vital for an effective response [14,16].

## 2.2. Web-based emergency response systems

This section analyzes web-based emergency response systems used to inform people about an emergency. Many applications have demonstrated that information and communications technology is critical for improving responses to disasters. The Internet is emerging as a potential source of information about particular disasters. Emergency responders now have the ability to access an enormous amount of data via web pages [26]. Web-based emergency response systems already exist and are used by private companies, schools, government of<sup>fi</sup>ces, the Red Cross, <sup>fi</sup>re-<sup>fi</sup>ghters, police, as well as many other institutions and individuals. Noti<sup>fi</sup>cations are often delivered by phone, e-mail, mobile phone and PDA.

The system in Table 1 was used to evaluate whether existing ERS support decision makers. After surveying the existing systems, it was found that they only provide SMS noti<sup>fi</sup>cations (i.e. no two-way communication), and they expose weaknesses in decision support, especially for man-made disaster situations. The ENSEMBLE system only assists decision makers and scienti<sup>fi</sup>c advisors in the management of nuclear emergencies. These systems do not provide noti<sup>fi</sup>cations in a way that considers people's needs, nor do they consider information related to previous disaster situations to provide effective emergency noti<sup>fi</sup>cations. This problem can be remedied by providing decision makers with knowledge that re<sup>fl</sup>ects the experience (CBR, in this case).

Therefore, as stated in [7], independent evaluations of free and open source software (FOSS) (e.g. SHANA) deployments are required in order to judge whether the platform has played a signi<sup>fi</sup>cant role in any given response. There are a number of challenges facing FOSS, as stated in [19], such as limited access to fundamental public data and lack of <sup>fi</sup>nancial support. The participation of organizations is required to ensure a successful deployment and to maintain appropriate solutions for the end users. Consequently, this paper focuses on the decision support application function of the MERS. Other functions can be found in our previous papers [1,2].

Table 1  
Web-based emergency noti<sup>fi</sup>cation systems.

<table><tr><td>System</td><td>Web</td><td>Type</td><td>Delivery</td><td>Decision support</td></tr><tr><td>Honeywell MissionMode</td><td>https://instantalert.honeywell.com/ http://www.missionmode.com</td><td>Alert Emergency notification system</td><td>Mobile pager, PDA, and e-mail Land-line or mobile phones, email, SMS text messages, pagers or faxes — all from a single web page</td><td>No No</td></tr><tr><td>ENSEMBLE Command Caller Sahana Arce</td><td>http://ensemble2.jrc.ec.europa.eu/ http://www.voicetech.com/Command_Caller_40.htm http://www.sahana.lk/ https://arce.dei.inf.uc3m.es/arce_demo/</td><td>Web-based decision support system Emergency, situational alarm, alert Emergency Emergency, situational alarm, alert, system status</td><td>Web pages Phone, E-mail, pager, fax, SMS,PDA Web pages Web pages, E-mail</td><td>Yes No No</td></tr><tr><td>AlertFind Sigame</td><td>http://www.messageone.com/crisis-communications/ http://www.sigame.es/</td><td>Emergency, situational alarm, alert Emergency</td><td>Phone, E-mail, pager, fax, SMS, PDA Web pages</td><td>No No</td></tr></table>

## 3. The ontology-supported CBR approach and related algorithms

The OS-CBR approach has four steps (data acquisition, information extraction, CBR, and knowledge presentation) with the following components:

(1) an information extraction algorithm for data acquisition,

(2) a set of ontologies,

(3) a knowledge base with related rules and cases, and (4) a CBR component that includes an ontology case retrieval algorithm (Algorithm 1), case adaptation algorithm (Algorithm 2), case revision and retain, and

(5) knowledge presentation.

Fig. 1 outlines the four steps of the OS-CBR approach and related components.

## 3.1. Data acquisition and information extraction (step 1 and step 2)

This data acquisition component [2] is based on information extraction and aggregation [32]. It inputs the SMS text messages received from mobile users in an emergency situation and stores them in a database. It is used to automatically extract structured, from unstructured information. The component consists of collected, unstructured information from SMS emergency text messages; conducted information extraction (IE) and aggregation including lexical analysis, name entity recognition, merging structure, normalization and duplication; and calculates similarity of SMS text messages.

## 3.2. Knowledge base

The knowledge base (KB) stores information about solutions for previous emergency situations and related business rules. Ontology is used to describe knowledge for previous cases.

## 3.2.1. Emergency situation case representation and indexing

A case is de<sup>fi</sup>ned as an emergency situation or problem in terms of natural language descriptions and related solutions. It incorporates three major functions: problem description; solution; and outcome [11]. In a CBR method, a case is described by a set of attributes or aims that identify the instance of a problem, its solution and its outcome, formally, as follows:

De<sup>fi</sup>nition 1. Case: (McGinty and Wilson) [20].

A case is a three–tuple, $C = ( C _ { d } , C _ { s } , C _ { o } )$ where $C _ { d } , C _ { s } ,$ , and $C _ { o }$ are used to refer to sets of features that describe the problem, a set of attributes that describe its solution, and the set of attributes that describe the outcome obtained by the solution $C _ { s }$ to the given problem $C _ { d } ,$ respectively. For a given case base CB, with $C _ { d } , C _ { s }$ and $C _ { o }$ respectively denoting the problem description, solution and outcome of a case $C A _ { i }$ so that $C A _ { i } { \in } C B , 0 { \le } i { \le } n ,$ n is the number of cases in the CB.

Based on De<sup>fi</sup>nition 1, an emergency situation case can be described in three tuples.

• Tuple 1 (speci<sup>fi</sup>cation of an emergency situation and the relevant attributes of the emergency situation): Table 2 describes the most important features from the point of view of an extensive and complicated case, to facilitate the retrieval of suitable emergency situation records. These features are viewed as the attributes of each emergency situation record in the database. These important features have been selected from a wide selection used in the related literature. The feature selection process has been conducted by interactive consultation with a number of experts. The experts have been elected from different roles, ranging from emergency management directors, to rescue team leaders who are involved in the emergency response systems.

![](/api/attachments/ETS2V74N/fulltext/images/1f134e9c3801873183cb275c94798dfce393f20008ac1cc10c41169cc6c7c1c3.jpg)  
Fig. 1. The O-SCBR approach and working process

Table 2  
Case attributes of OS-CBR approach.

<table><tr><td>Attributes</td><td>Definition</td><td>Description</td><td>Data type</td></tr><tr><td>Case Name</td><td>Restored case name</td><td>N/A</td><td>Text</td></tr><tr><td rowspan="4">Disaster Event</td><td rowspan="4">Based on disaster styles, disaster event is classified into five types</td><td>Bioterrorism</td><td>Choice</td></tr><tr><td>Chemical agent</td><td></td></tr><tr><td>Radiation</td><td></td></tr><tr><td>Terrorism</td><td></td></tr><tr><td>Disaster location</td><td>Represents any location mentioned in a SMS message that connected to the disaster event</td><td>State, city</td><td>Choice</td></tr><tr><td rowspan="2">Stage of execution</td><td rowspan="2">Disaster status</td><td>In progress</td><td>Choice</td></tr><tr><td>Accomplished attempting</td><td></td></tr><tr><td>Number of dead</td><td>Number of people killed</td><td>N/A</td><td>Numerical</td></tr><tr><td>Number of wounded</td><td>Number of people injured</td><td>N/A</td><td>Numerical</td></tr><tr><td rowspan="4">Instrument used</td><td rowspan="4">The common weapons used in a disaster event</td><td>Heavy weapon</td><td>Choice</td></tr><tr><td>Grenade attack</td><td></td></tr><tr><td>Fire arms attack</td><td></td></tr><tr><td>Cold weapon</td><td></td></tr><tr><td rowspan="2">Physical target</td><td rowspan="2">The building type mentioned in a SMS text. It is a physical target such as an educational building.</td><td>Military terrorist target</td><td>Choice</td></tr><tr><td>Civilian terrorist target</td><td></td></tr><tr><td>Date &amp; time</td><td>The date and the time of a disaster event</td><td>AM or PM</td><td>Choice</td></tr><tr><td>Magnitude</td><td>A measure of disaster event degree</td><td>Low, medium, high</td><td>Choice</td></tr><tr><td>Area affected</td><td>This indicator covers areas affected by disaster event</td><td>N/A</td><td>Numerical</td></tr><tr><td>Temperature</td><td>Quantitatively expresses the common notions of hot and cold</td><td>N/A</td><td>Numerical</td></tr><tr><td>Fire</td><td>This indicator covers areas affected by fire in disaster event</td><td>Yes or no</td><td>Choice</td></tr><tr><td>Evacuation</td><td>This indicator shows the mass movement of persons from a dangerous place due to a disaster event</td><td>Yes or no</td><td>Choice</td></tr><tr><td>Persons with disability</td><td>This indicator illustrate the aspect of evacuating a person with a disability</td><td>Yes or no</td><td>Choice</td></tr><tr><td>Explosive attack</td><td>Explosive devices are use in the disaster situation</td><td>Yes or no</td><td>Choice</td></tr><tr><td>Hijacking</td><td>Hijacking condition</td><td>Yes or no</td><td>Choice</td></tr><tr><td>Biological attack</td><td>Biological weapons and the use of bioterror</td><td>Yes or no</td><td>Choice</td></tr><tr><td>Chemical attack</td><td>Chemical incident condition</td><td>Yes or no</td><td>Choice</td></tr></table>

In the above table, “Disaster Event”, “Disaster Location”, “Stage Of execution”, “Instrument Used”, “Physical Target”, “Time”, “Magnitude”, “Fire”, “Evacuation”, “Persons With Disability”, “Explosive Attack”, “Hijacking”, “Biological Attack”, “Chemical Attack”, are the fundamental architectural settings for de<sup>fi</sup>ning a disaster event or an emergency situation. These fourteen attributes are represented by the choice of data type in the database. “Number of Dead”, “Number of Wounded”, “Area Affected”, “Temperature” are four attributes that can be represented by numerical values.

• Tuple 2 (solutions describe the stated or derived solutions to an emergency situation, comprised of tasks and constraints subclasses): the emergency response solution in the OS-CBR approach consists of three major phases: emergency situation response preparation, emergency situation response, and emergency rescue. The emergency situation response preparation is responsible for providing resource support, such as emergency team support, emergency logistics support and emergency technical support. Emergency response is responsible for launching an expert group, and establishing reliable communication with the group. Emergency rescue is responsible for providing an evacuation plan, medical aid, and alerting emergency noti<sup>fi</sup>cations.

• Tuple 3 (outcome describes the results when the solution tuple has been used in a previous emergency situation): Outcome process includes bene<sup>fi</sup>ts, status, and risks. Bene<sup>fi</sup>ts include feedback from the real world and interpretation of the feedback after applying the solutions. Status includes positive or negative consequences after applying the solutions. Risks include problem interpretation of the feedback after applying the solutions.

## 3.2.2. Emergency response ontology

The term “ontology” is de<sup>fi</sup>ned as the study of the existence of knowledge and has been widely applied in different information systems [8]. It is an explicit and formal speci<sup>fi</sup>cation of a conceptualization and advanced knowledge organization technique. Informally speaking, an ontology is able to be a conceptual model that speci<sup>fi</sup>es the terms and relationships between the concepts explicitly and formally, which in turn represent the knowledge for a speci<sup>fi</sup>c domain [3]. This study uses ontology to improve the Information Extraction process and to present the results of knowledge about response/ warning generation. As a part of the vocabulary, ontology enables us to de<sup>fi</sup>ne case structure. As part of the terminology, ontology allows us to de<sup>fi</sup>ne the query vocabulary. The development of ontologies is indeed a complex task based on knowledge management and domain experts [18].

There are various standard ontology languages that represent ontology such as Web Ontology Language (OWL) and Resource Description Framework (RDF). OWL has been developed by the World Wide Web Consortium (W3C) Web Ontology Working Group for the Semantic Web. The RDF Schema [4,34] provides essential vocabularies to describe domain knowledge, the essential common model for data aggregation and integration. Some existing domain ontologies, such as the examples in [9,25] have been reviewed and assessed, and have proved useful for the purposes of this study. To speed up ontology development, several ontology development tools have been assessed, such as ontology editing tools, ontology merging tools and ontology extraction tools [23]. The ontology for the SMS text message domain has been <sup>fi</sup>nally developed by using the Protégé tool, which is the most suitable for this study based on our assessment. We constructed a case attribute domain ontology that consists of six main entities, including: physical target; disaster location; human target; weapon used; stage of execution; and disaster event. All the entities are dividing into categories and sub-categories. Fig. 2 shows a part of the ontology structure.

To enable the OS-CBR approach and its implementation to be easily understood, we explain them by using an example. For that purpose we have chosen the domain of disaster location (spatial and temporal location of attack), because the domain is widely known and its characteristics are suitable for case classi<sup>fi</sup>cation. Fig. 3 shows a possible conceptualization of the domain containing only relevant aspects of the area we are interested in. In this sense, we can think of the ontology as the task speci<sup>fi</sup>cation where the properties of concepts represent the properties for which our classi<sup>fi</sup>cation method has to determine appropriate values from input data.

![](/api/attachments/ETS2V74N/fulltext/images/4acce3aba6639b7a2b9a59fc4e8ba1c16b0e35e15b244414541ebb61fd80cb75.jpg)  
Fig. 2. Ontology domain.

![](/api/attachments/ETS2V74N/fulltext/images/30f127046b3e6dc0b44a463e0eecc01ebf894e69b44bc2a41bd6d268bb748e89.jpg)  
Fig. 3. An ontology structure of a disaster location domain.

## 3.3. Case-based reasoning component (Step 3)

The CBR component is the heart of the MERS. Fig. 4 shows the CBR component in the act of reasoning about an emergency situation. The component mainly consists of case retrieval, case adaptation, and case preservation (retain). In fact, the case adaptation phase does not replace or combine the re-use and revise stages. According to Fig. 4, the case re-use will be substituted by case adaptation, if the similarity between the retrieved case and the target case is less than a prede<sup>fi</sup>ned threshold. Subsequently, the case revision will be affected. However, we consider the substituting phases (case re-use and case adaptation), along with the revise phase, in one single stage in Fig. 4, namely the Adaptation Stage, because of their close relations in the implementation process. This stage consists of a cycle of revise and re-uses stages that repeat until a suitable solution is generated by the system.

## 3.3.1. Case retrieval

The case retrieval is the most important process in CBR design and also in the CBR component of the system. When a new disaster situation occurs, the CBR system retrieves, from a case base (CB), previous cases that are similar to the new disaster situation. For example, for a given case C′={Suicide Attack, Car bomb, Sydney, 50 killed …} information about previous disaster events similar to the current case can be found through case retrieval.

## De<sup>fi</sup>nition 2. Compromise assumption.

In a calculation process, for any two cases $C _ { 1 } , C _ { 2 } ,$ let $F ^ { 1 } = ( w _ { 1 } f _ { 1 } , w _ { 2 } f _ { 2 } . . .$ $w _ { n } f _ { n } ) , \mathrm { F } ^ { 2 } = ( w _ { 1 } \bar { f } _ { 1 } , w _ { 2 } f _ { 2 } . . . , w _ { n } \bar { f } _ { n } )$ represent features of $C _ { 1 }$ and $C _ { 2 }$ respectively, where n is the number of features $F ^ { 1 }$ and $F ^ { 2 } , \ w _ { i }$ is a weight assigned to a feature $f _ { i } ( \mathrm { i } = 1 , . . , \Pi )$ , let $Q = \{ q _ { 1 } , q _ { 2 } , . . . q _ { m } \}$ represents a target query, and $S _ { 1 } , S _ { 2 }$ are balance similarity scores obtained from linguistic evaluation for C and $C _ { 2 } ,$ respectively. C is more similar to the target query Q than $C _ { 2 } ,$ if the S is higher than $S _ { 2 } .$

To retrieve similar events from historical cases, similarity measurement is commonly used in case retrieval. The value of similarity is between 0 (not similar) and 1 (most similar). The total similarity value is calculated by [29]:

$$
S = \frac {\sum_ {i = 1} ^ {n} \sum_ {j = 1} ^ {m} \left(S _ {i j}\right)}{N}\tag{1}
$$

where $S _ { i j }$ is similarity of parameter i of a new case, compared to feature j of an old case. n is the number of the new case feature, m is the number of the old case feature, and s is the total number of features. The similarity calculation of $S _ { i j }$ depends on the data type. The possible data types are numerical, minimum and maximum numerical, text string and linguistic. For the numerical data type, the similarity value is calculated by:

$$
S _ {i j} = \left(1 - \sqrt {\left(\frac {C _ {i j} - X _ {i}}{\max (C _ {i}) - \min (C _ {i})}\right) ^ {2}}\right) \cdot \frac {W _ {i}}{1 0}\tag{2}
$$

where $S _ { i j }$ is the similarity parameter i of a new case, compared to parameter j of an old case. N is the number of parameters, $C _ { i j }$ is the value of the parameter i of the case j, X is the input value of the parameter i,

![](/api/attachments/ETS2V74N/fulltext/images/50504432d87dfddaba625e9bb706b95aa1fad3060c602fa47e6f639e0cab77b2.jpg)  
Fig. 4. Architecture of emergency situation CBR.

$W _ { i }$ is the weight factor of the parameter i, and max(C )–min(C ) is the largest scope of the $C _ { i }$ of the case j. The interval value [a,b] is calculated by the following rules:

$$
\begin{array}{l} \text { if   data - type is 'INTERVAL' and a\leq C_{ij} \leq b then} \\ S _ {i j} = \frac {W _ {i}}{1 0} \text { otherwise } S _ {i j} = 0. \end{array}\tag{3}
$$

The minimum and maximal numerical value is calculated by the following rules:

$$
\begin{array}{c} \text { if   data - type is 'MIN' and X_{i} \leq C_{ij} then} \\ S _ {i j} = \frac {W _ {i}}{1 0} \text { otherwise S_{ij} = 0} \end{array}\tag{4}
$$

if data type is MAX and $X _ { i } \geq C _ { i j }$ then

$$
S _ {i j} = \frac {W _ {i}}{1 0} \text {   otherwise   } S _ {i j} = 0.\tag{5}
$$

The textual string type parameter similarity is calculated in a straightforward way, so that, if the input value $X _ { i }$ is included in the textual string value of $C _ { i j } ,$ the similarity $S _ { i , j } = 1$ (Eq. (6)).

$$
\begin{array}{c} \text { if   data - type is 'STRING' and C^{\prime} (\infty_{i}) = C(\alpha_{i}) then} \\ S _ {i j} = \frac {W _ {i}}{1 0} \text { otherwise } S _ {i j} = 0. \end{array}\tag{6}
$$

If X and $C _ { i , j }$ are totally different to each other, the similarity $S _ { i , j } { = } 0$ The linguistic value similarity (high, medium and low) is calculated in the following way (see Eqs. (7) and (8)):

$$
\text { if } X _ {I} = C _ {i j} \text { then } S _ {i j} = \frac {W _ {i}}{1 0}\tag{7}
$$

$$
\text { if   } X _ {i} \neq C _ {i j} \text {   and   } X _ {i} \text {   or   } C _ {i j} = \text { medium   then }
$$

$$
S _ {i j} = \frac {0 . 5 \times W _ {i}}{1 0} \text { otherwise } S _ {i j} = \frac {0 . 1 \times W _ {i}}{1 0}.\tag{8}
$$

![](/api/attachments/ETS2V74N/fulltext/images/94490541ca587c9bf45afa5e902f138db12a9b788bb544904cc1ca103e01e47e.jpg)  
Fig. 5. Example of the fuzzy preference function [27].

The threshold type parameter similarity is calculated in the following way, so that, if the input value $X _ { i }$ is less than the value of $C _ { i j } ,$ the similarity $S _ { i j } { = } 1$ (see Eq. (9)).

$$
\begin{array}{c} \text { if   data - type is } ^ {\prime} T H R E S H O L D ^ {\prime} \text { and } C ^ {\prime} \left(\infty_ {j}\right) > X _ {i} \text { then } \\ S _ {i j} = \frac {W _ {i}}{1 0} \text { otherwise } S _ {i j} = 0. \end{array}\tag{9}
$$

In the degree similarity of membership of a retrieved case to a fuzzy set [17,33], these fuzzy linguistic evaluations can be de<sup>fi</sup>ned as:

$$
A = \left\{ \begin{array}{c} V e r y L o w (V L), L o w (L), M e d i u m (M), \\ H i g h (H), V e r y H i g h (V H) \end{array} \right\}\tag{10}
$$

$$
A = \left\{\left(\mu_ {A} (x), x\right) | x \in X \right\}.\tag{11}
$$

Where $0 \leq \mu _ { A } ( x ) \leq 1$ is called the membership function. The value of $\mu _ { A } ( { \boldsymbol { x } } )$ with a trapezoidal fuzzy number $A = ( \mathbf { a } , \mathbf { b } , \mathbf { c } , \mathbf { d } ; 1 )$ is de<sup>fi</sup>ned as follows:

$$
\mu_ {A} (x) = \left\{ \begin{array}{l l} \frac {x - a}{b - a}, & a \leq x \leq b \\ 1, & b \leq x \leq c \\ \frac {x - d}{c - d}, & c \leq x \leq d \\ 0, & \text { otherwise } \end{array} \right..\tag{12}
$$

These elements have a value ranging from 0 (not similar) to 1 (maximum similarity). This range is then transformed into the fuzzy preference function shown in Fig. 5. The two cases are highly similar if the balance similarity score that is obtained from linguistic evaluation is high (see Table 3).

The case retrieval algorithm (Algorithm 1) works as follows: We assume that the case base has stored the historical data related to a given disaster situation. When a new problem is input into the system, the case base is searched to retrieve all cases with a similar pro<sup>fi</sup>le. The similarity of the new problem to the stored cases is determined by calculating the distance between case features. Then, once the most similar cases have been obtained from the case base, they will be used in the next adaptation phase to generate an accurate solution.

Linguistic terms and similarity.

<table><tr><td>Fuzzy rating</td><td>Maximum score</td><td>Minimum score</td></tr><tr><td>Excellent</td><td>1</td><td>0.95</td></tr><tr><td>Good</td><td>0.94</td><td>0.75</td></tr><tr><td>Average/fair</td><td>0.74</td><td>0.25</td></tr><tr><td>Poor</td><td>0.24</td><td>0</td></tr></table>

Algorithm 1. Case retrieval algorithm.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Input: A new case C is described by n features,  $\beta = \{\beta_{1}, \beta_{2}, \ldots, \beta_{n}\}$ ,
Output: Similarity degree of a new case within the case base
Local variables: Old case  $C'$  is described by a set of features as follows:
 $\alpha = \{\alpha_{1}, \alpha_{2}, \ldots, \alpha_{n}\}$ , where n is number of case features,
Data-type = {numeric, string, interval, linguistic},
Weight (W) is the weight factor of the feature  $\beta$  so that
 $W = \{w_{1}, w_{2}, \ldots, w_{n}\}$ , Feature-function (F) is the function factor of feature  $\beta$ ,
such that  $F = \{Equal, Threshold, Interval\}$ ,  $\theta$  is a specified threshold value
Begin
Starting from i = 1, select one case  $C_{i} (0 \leq j \leq m)$ 
Begin
For each  $\alpha_{j}$  of  $C'$  do ( $0 \leq j \leq n$ ).
Begin
Compare feature value of  $\alpha$  and  $\beta$ :
Case of (Feature-function = 'Equal') do
if  $f_{i}$  (data-type) = 'numeric' then do Eq. (2)
if  $f_{i}$  (data-type) = 'string' then do Eq. (6)
Case of (Feature-function = 'Interval') do
Compute do Eq. (3)
Case of (Feature-function = 'Threshold') do
Compute Eq. (7)
Case of (Feature-function = 'Min and Max') do
Compute Eqs. (4) and (5)
Case of (Feature-function = 'Linguistic') do
Compute Eqs. (7) and (8)
End
Calculate the average of each retrieved case by Eq. (1)
Calculate the degree of similarity of retrieved case to a fuzzy set
by Eqs. (10), (11), and (12)
if  $0.95 \leq S \geq 1.0$  then Similarity is very high
if  $0.75 \leq S \geq 0.94$  then Similarity is high
if  $0.25 \leq S \geq 0.74$  then Similarity is fair
if  $0.0 \leq S \geq 0.24$  then Similarity is very low
End
End
</div>

## 3.3.2. Case adaptation

Case adaptation is the process of transforming the most similar cases retrieved from the case base into a solution appropriate for the current problem. Several strategies for case adaptation have been proposed in the literature. They can be classi<sup>fi</sup>ed in three main groups: substitution adaptation, transformational adaptation and generative adaptation. Our system uses the substitution adaptation strategy. Substitution is used when parts of the old solution are in con<sup>fl</sup>ict with, or contradict the new problem requirements. For example, part of an emergency rescue plan in a past disaster may need to be replaced and updated with a more effective and suitable plan for the current disaster situation. Substitution is performed by using prede<sup>fi</sup>ned semantic knowledge. The steps of the case adaptation algorithm (Algorithm 2) are described as follows: for every selected case in the retrieval phase, the distance between the case and its solution is calculated. If the difference of the proposed solution and those of the selected cases is acceptable, then the solution is considered as a valid one. If necessary, substitute unacceptable components violated using the prede<sup>fi</sup>ned semantic knowledge and make other adjustments. The user is then informed and the process continues to select new cases from the case base.

Algorithm 2. Case adaptation algorithm.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Input: A new case  $C = \{f, \lambda, o\}$  is described by the following attributes:
1) Set of features  $f = \{f_1, f_2, \ldots, f_n\}$ , where n is number of case features
2) Set of solution  $\lambda = \{\lambda_1, \lambda_2, \ldots, \lambda_k\}$ , where k is number of case solutions
A retrieved case  $C' = \{f', \lambda', o'\}$  is described by the following attributes:
1) Set of features  $f' = \{f_1', f_2', \ldots, f_n'\}$ , where n is number of case features
2) Set of solution  $\lambda' = \{\lambda_1', \lambda_2', \ldots, \lambda_k'\}$ , where k is number of case solutions

Output: Case adaptation

Local variables: PK represents a set of constraints; D represents a set of differences attributes

Begin

Step 1. Retrieve the most similar case from the case base
Step 2. Determine the differences between cases, so that  $d_i = f_i' - f_i$ 
Where  $d_i \in D$  for i = 1, 2, 3 ..., n, n is the number of features,
Step 3.  $\forall d_i \in D$  Search for suitable substitution using predefined semantic knowledge and constraint (PK)
Step 4. Perform the substitution and make appropriate changes

End
</div>

## 3.3.3. Case revision and preservation

When a new disaster occurs, it is compared to a collection of significant disasters whose solutions are already known. The most similar signi<sup>fi</sup>cant disasters and the respective solutions are retrieved. The solutions of retrieved cases are then adapted to meet the new disaster situation requirements. The suggested solution is revised for its suitability by experts. The revised solutions are then retained temporarily in the disaster database. When the suggested solutions are actually applied, the solution outcomes for the current situation can then be evaluated. Finally, the new disaster description and its solutions are retained as a new case in the case base to help <sup>fi</sup>nd solutions for future disasters.

## 3.4. Knowledge presentation (step 4)

This section is concerned with getting the right information and knowledge to the right people at the right time in the right form. In an emergency situation, there is a need for rapid decision making under pressured, dynamic conditions where information is partial, con<sup>fl</sup>icting and often overloaded.

## 3.4.1. Identification of need for knowledge

Knowledge needs for a current problem are used to <sup>fi</sup>nd the right knowledge to be shared, and to enable the creation of the right knowledge in case creation [15]. Therefore, it is essential to specify the requirements of the needed knowledge for a current problem to facilitate an accurate search for knowledge, or to create new knowledge.

De<sup>fi</sup>nition 3. Knowledge Need (KN).

$$
K N = \left\{a ^ {\prime} (S _ {i}) | S _ {i} \in S M S (T) \right\}
$$

Where, ${ \mathrm { } } , S _ { i }$ is a SMS text message of SMS (T), a′ (S ) is the local attribute of $S _ { i , }$ i is the number of SMS text messages.

Organization pro<sup>fi</sup>le (OP) stands for the personalisation of a service that allows a user to query particular needs. An OP is a group of settings that de<sup>fi</sup>ne how knowledge presentation is setup for a speci<sup>fi</sup>c user.

De<sup>fi</sup>nition 4. Organization pro<sup>fi</sup>le (OP).

$$
O P = \{p, r, h \}
$$

where $p , r ,$ and h denote a collection of personal data sets of user requirements, and history activities, respectively.

It is important to determine the desired type of knowledge needed. The requirements may include modules, processes and methods, which may have different speci<sup>fi</sup>cations to describe them. The speci<sup>fi</sup>- cation of need allows an accurate knowledge search, or case creation.

De<sup>fi</sup>nition 5. Knowledge Requirements (KR).

$$
K R = \left\{T (S _ {i}) \mid S _ {i} = \left(s _ {i} ^ {1}, s _ {i} ^ {2},.. s _ {i} ^ {n}\right) \right\}
$$

Where KR is knowledge requirement need, T(Si) is the requirement type, s<sub>i</sub><sup>n</sup> is requirement steps, and i is the ith knowledge requirement need.

The knowledge retrieval (KR) model is based on the information retrieval (IR) system. An IR system retrieves documents based on a user's query as input and the documents are sorted by their relevance to the query [6]. The IR system is based on keyword indexing systems and Boolean logic queries that are sometimes supplied with statistical methods [22]. The basic idea of the IR system is that the user asks the system and obtains desired information. The obtained information is then used to solve a given problem or situation. A satisfactory problem resolution dismisses the information need. The KR algorithm (Algorithm 3) is described below.

## Algorithm 3. Knowledge retrieval.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Input:
$R = \{R_1, R_2, ..., R_n\}$ is a knowledge requirement
$OP = \{OP_1, OP_2, ..., OP_k\}$ is an organization profile
$CB = \{CB_1, CB_2, ..., CB_n\}$ is an experience base
$\beta$ is a predefined threshold value

Output: Data warehouse

Begin

Step 1. Retrieve the most similar case from the case base based on knowledge requirement $R_i$ and organization profile $OP_j$. The Similarity is based on ontological similarity.

Step 2. Find the case with the max value of $Sim(C, C')$

Step 3. If $Sim(C, C') \geq \beta$ then Call DW_Extraction algorithm to extract concepts and insert them into data warehouse DW

End
</div>

## 4. System implementation

To verify the usefulness of the proposed OS-CBR approach, a OS-CBR prototype system has been developed using NetBeans IDE under Microsoft Windows 7. The NetBeans project consists of an open-source IDE and an application platform that enables developers to rapidly create a variety of applications using the Java platform. The NetBeans is connected to a relational database management system (RDBMS), which is considered as a case library/table and represented by MySQL. A <sup>fl</sup>owchart of the system is provided in Fig. 6.

The top area of the window contains Tabbed Panes in order to have several panes to share the same space, and the user chooses which component to view by selecting the tab corresponding to the desired component. These components are: con<sup>fi</sup>guration query, similarity con<sup>fi</sup>guration, case retrieval, case reuse, case revise, and case retain. Users use query interface to input the requirements and run the system. The system retrieves data about problem descriptions, solutions, and outcomes from the case repositories for users (Fig. 7).

A case-based example is now provided to illustrate the problem solving process related to an emergency situation by using previous experience. The MERS system receives the mobile users' messages and inserts them into a relational database and, as shown in Fig. 6, inputs requirements of the disaster. For example, the name of the disaster event is “Suicide Attack”, the weapon used is “Car Bomb”, and the physical target is “University”.

After the user completes the inputs, the user can choose the preferred attributes as shown in Fig. 8. A vector of four elements is used to represent a case. The elements of this vector describe the property (disaster attribute), its function, its importance within this case, and its value.

In the similarity con<sup>fi</sup>guration (Fig. 8), the system allows a user to give the relative disaster features options for similarity purposes. These options are available by clicking on the corresponding check box. A Combo Box (a drop-down list of values) allows the user choose one of several choices of function properties. The slider is used to set the weight. We offer a choice of six functions for the progression of weights from 100 (most important) to zero (irrelevant). The user can also control the value of the function property that is displayed; for example, to set the value of the threshold to a certain value. Spinner is used to let the user choose from a range of values to control the number of retrieved cases. The bottom right section of the window contains button that the user can use to proceed the case retrieval stage.

The case retrieval stage allows the decision maker to enter a query. Fig. 9 shows the application interface. There are two ways to add case retrieval query values. Firstly, the “Choose” button allows a decision-maker to capture the knowledge terminology of the disaster domain. A new window shows the ontology tree where the user can select the query features. It is not mandatory to include every component. The user might enter either a list of desired features, or a list of undesired features, for the requested disaster situation. Secondly, each disaster situation belongs to general disaster event category (‘Bioterrorism’, ‘Chemical Agent’, etc.), with the disaster instrument used (“Heavy weapon”, “Grenade attack”, etc.), the disaster location (“Africa”, “Asia”, etc.) and the disaster physical target (‘Military’, ‘Civilian’). For example, we choose car bomb (weapon), educational building (physical target), and suicide attack (disaster event) as a desired disaster feature. The user may also leave them unspeci<sup>fi</sup>ed. The two small checkboxes allow the user to specify that universal and/or common features may be assumed as available. When the user has completed, or is satis<sup>fi</sup>ed with his/her selection the query button can be pressed in order to proceed to the next step.

![](/api/attachments/ETS2V74N/fulltext/images/15264d2f54b57883f7580a11320caca2e7e0752dafe68f85b43384a9e9a1e6c0.jpg)  
Fig. 6. OS-CBR system <sup>fl</sup>owchart.

![](/api/attachments/ETS2V74N/fulltext/images/1de62d180194bcd455e8e7631c8cd1d35b815529341de453c4746d7c074601a3.jpg)  
Fig. 7. User interface for disaster situation input.

The re-use case stage (Fig. 10) allows the user to choose a disaster event from a list of k, closest similarity to the query request (k is determined in con<sup>fi</sup>guration with the similarity stage). The disaster events are sorted in descending order according to their similarity degree to the current disaster condition. The “select” button is used to proceed to the case revision stage.

The next screen (Fig. 11) illustrates the user's selection of disaster event cases. The system performs adaptation tasks. In the example, the system has provided resource support groups that can be used as a substitution group. For instance, the system has substituted

![](/api/attachments/ETS2V74N/fulltext/images/c16ccb77e56a24c7b681bf8950d3d3713cd51cdfc114fbc27a09460a59e89138.jpg)  
Fig. 8. Similarity con<sup>fi</sup>guration values.

K. Amailef, J. Lu / Decision Support Systems 55 (2013) 79–9  
![](/api/attachments/ETS2V74N/fulltext/images/251eb1c7a1f4009171e2aeafcb545db0d1a5692634c8dd0124fee07cc1e29db8.jpg)

ABC Group by Disaster Resistant Communities Group LLC (DRC). Some other categories have been changed according to the current disaster situation. In our example, chemical alerts and chemical attack plan are not required, so therefore, the system removes them from the solution section. In addition, the system shows the percentage values of key aspects of response planning. The top right section of the window contains the “DONE” button, which the user can use to continue to the next and <sup>fi</sup>nal stage (Fig. 12).

The user considers the proposed recommendation as a good solution to the current disaster situation. Then, the historical data can be retained in the case base for use in future queries using the rest of the CBR cycle. The top left area of the window contains a text <sup>fi</sup>led that the user can use to enter a unique name for the new case. The top right part of the window contains a slider that allows the user to enter the criteria measurement key aspects of the proposed solution.

Fig. 9. Case retrieval values.  
![](/api/attachments/ETS2V74N/fulltext/images/02c16737211b4e500a24b74a8ad6773e02ff9105a55a8e5a9e25b7ab14810e14.jpg)  
Fig. 10. Case reuse.

![](/api/attachments/ETS2V74N/fulltext/images/aef9a77095b59769e1e6c3c5fee7ee8ed3a28fe57d8a02eedff59981bab5d0d9.jpg)  
Fig. 11. Case revise.

## 5. Experimental analysis

This section presents major results of the experiments conducted to examine the performance of the OS-CBR approach. The approach was evaluated using the standard information retrieval measures:

![](/api/attachments/ETS2V74N/fulltext/images/5980a63676d12633c9742278ac5954f1c786cc32abc47ba6ae13ec7e8acd758f.jpg)  
Fig. 12. Case retain stage.

Table 4  
A contingency table analysis of precision and recall.

<table><tr><td colspan="5">IE system</td></tr><tr><td>Expert</td><td>Expert</td><td>Relevant</td><td>Not-relevant</td><td>Total</td></tr><tr><td>Retrieved</td><td></td><td>a</td><td>b</td><td>a+b=k</td></tr><tr><td>Not-retrieved</td><td></td><td>c</td><td>d</td><td>c+d=n-k</td></tr><tr><td>Total</td><td></td><td>a+c=r</td><td>b+d=n-r</td><td>a+b+c+d=N</td></tr><tr><td colspan="5">Overall accuracy (OA)=(a+b)/N</td></tr></table>

precision, recall and F-measure. The recall score measures the ratio of the relevant information retrieved from the cases against all the available relevant information present in the cases. The precision score measures the ratio of relevant information that was retrieved against all the information that was retrieved. The F-measure is a combined measure of precision and recall [13].

Let N be a collection of cases, n be relevant information we want to retrieve (Disaster location, Weapon used, Physical target, etc.), and r relevant information retrieved from N. The OS-CBR approach recognizes a collection of cases, in which k represents all results retrieved. The recall (R), precision (P), and F-measure formulae used are given by Eqs. (13)–(16). Table 4 summarizes the relationships between the precision and the recall in terms of a binary classi<sup>fi</sup>cation.

$$
\begin{array}{r l} \text { Recall   (R) } & = \frac {\text { Relevant   and   Retrieved }}{\text { Relevant }} \\ & = \frac {a}{a + c} \end{array}\tag{13}
$$

$$
\begin{array}{r l} \text { Precision(P) } & = \frac {\text { Relavant   and   Retrieval }}{\text { Retrieved }} \\ & = \frac {a}{a + b} \end{array}\tag{14}
$$

$$
\mathrm{F-measure} = \frac {2 R P}{R + P}\tag{15}
$$

$$
\text { Overall   accuracy } (O A) = \frac {a + b}{N}.\tag{16}
$$

Table 5 contains four main columns. The column under the heading “Number of attributes” indicates the signi<sup>fi</sup>cant attributes of the environment that describes the surroundings of the problem. The column under the heading “Cases” indicates the cases that have been used to conduct tests and verify the performance and capabilities of the proposed approach to support decision making in disaster situations. The experiment was conducted on nine different numbers of attributes (2, 3, 4, 5, 6, 7, 8, 9, and 10) and with three different cases (Case I, Case II, and Case III). The columns under the heading “CBR” and “OS-CBR” contain sub-headings including “Precision”, “Recall”, “F-measure”, and “Overall accuracy”, indicating OS-CBR approach's performance. All graphs provided in this section are based on Table 5.

This study testi<sup>fi</sup>ed the performance of the proposed OS-CBR approach through an experiment. There are three cases in the emergency response database. Each case contains 12 attributes including: Case ID, Case title, Disaster event, Weapon used, Disaster location, number of injured, Number of dead, Affected area, Temperature, Terrorism group, Magnitude, and Date. From the database, OS-CBR tried to produce an emergency response plan recommendation subject to the input user's conditions. OS-CBR will recommend reasonable reference cases to the decision maker based on the user's input features.

## 5.1. Experiment I

In the <sup>fi</sup>rst round of experiments, the effect of the number of attributes on cases retrieved for the CBR approach was examined, as shown in Fig. 13. Each of these nine graphs shows that precision is affected by the number of attributes, while recall remains <sup>fi</sup>rmly at 100% across the all number of attributes. Several tests have been conducted to verify the performance of the CBR approach. Two of these tests are presented here.

Table 5  
Initial experiment data.

<table><tr><td rowspan="2">Number of attributes</td><td rowspan="2">Cases</td><td colspan="4">CBR</td><td colspan="4">OS-CBR</td></tr><tr><td>Precision (P)</td><td>Recall (R)</td><td>F-measure</td><td>OA</td><td>Precision (P)</td><td>Recall (R)</td><td>F-measure</td><td>OA</td></tr><tr><td rowspan="3">2</td><td>Case I</td><td>1.00</td><td>1.00</td><td>1.00</td><td>1.00</td><td>1.00</td><td>1.00</td><td>1.00</td><td>1.00</td></tr><tr><td>Case II</td><td>0.50</td><td>1.00</td><td>0.67</td><td>1.00</td><td>1.00</td><td>1.00</td><td>1.00</td><td>1.00</td></tr><tr><td>Case III</td><td>0.50</td><td>1.00</td><td>0.67</td><td>1.00</td><td>0.50</td><td>1.00</td><td>0.67</td><td>1.00</td></tr><tr><td rowspan="3">3</td><td>Case I</td><td>0.67</td><td>1.00</td><td>0.80</td><td>1.00</td><td>1.00</td><td>1.00</td><td>1.00</td><td>1.00</td></tr><tr><td>Case II</td><td>0.67</td><td>1.00</td><td>0.80</td><td>1.00</td><td>0.67</td><td>1.00</td><td>0.80</td><td>1.00</td></tr><tr><td>Case III</td><td>0.33</td><td>1.00</td><td>0.39</td><td>1.00</td><td>0.67</td><td>1.00</td><td>0.80</td><td>1.00</td></tr><tr><td rowspan="3">4</td><td>Case I</td><td>0.75</td><td>1.00</td><td>0.86</td><td>1.00</td><td>1.00</td><td>1.00</td><td>1.00</td><td>1.00</td></tr><tr><td>Case II</td><td>0.50</td><td>1.00</td><td>0.67</td><td>1.00</td><td>0.75</td><td>1.00</td><td>0.86</td><td>1.00</td></tr><tr><td>Case III</td><td>0.25</td><td>1.00</td><td>0.29</td><td>1.00</td><td>0.75</td><td>1.00</td><td>0.86</td><td>1.00</td></tr><tr><td rowspan="3">5</td><td>Case I</td><td>0.60</td><td>1.00</td><td>0.75</td><td>1.00</td><td>1.00</td><td>1.00</td><td>1.00</td><td>1.00</td></tr><tr><td>Case II</td><td>0.40</td><td>1.00</td><td>0.57</td><td>1.00</td><td>0.80</td><td>1.00</td><td>0.88</td><td>1.00</td></tr><tr><td>Case III</td><td>0.40</td><td>1.00</td><td>0.57</td><td>1.00</td><td>0.60</td><td>1.00</td><td>0.75</td><td>1.00</td></tr><tr><td rowspan="3">6</td><td>Case I</td><td>0.83</td><td>1.00</td><td>0.91</td><td>1.00</td><td>1.00</td><td>1.00</td><td>1.00</td><td>1.00</td></tr><tr><td>Case II</td><td>0.67</td><td>1.00</td><td>0.80</td><td>1.00</td><td>0.83</td><td>1.00</td><td>0.91</td><td>1.00</td></tr><tr><td>Case III</td><td>0.33</td><td>1.00</td><td>0.49</td><td>1.00</td><td>0.50</td><td>1.00</td><td>0.67</td><td>1.00</td></tr><tr><td rowspan="3">7</td><td>Case I</td><td>0.71</td><td>1.00</td><td>0.83</td><td>1.00</td><td>0.88</td><td>1.00</td><td>0.94</td><td>1.00</td></tr><tr><td>Case II</td><td>0.71</td><td>1.00</td><td>0.83</td><td>1.00</td><td>0.86</td><td>1.00</td><td>0.92</td><td>1.00</td></tr><tr><td>Case III</td><td>0.29</td><td>1.00</td><td>0.45</td><td>1.00</td><td>0.57</td><td>1.00</td><td>0.73</td><td>1.00</td></tr><tr><td rowspan="3">8</td><td>Case I</td><td>0.75</td><td>1.00</td><td>0.86</td><td>1.00</td><td>0.88</td><td>1.00</td><td>0.93</td><td>1.00</td></tr><tr><td>Case II</td><td>0.63</td><td>1.00</td><td>0.77</td><td>1.00</td><td>0.88</td><td>1.00</td><td>0.93</td><td>1.00</td></tr><tr><td>Case III</td><td>0.25</td><td>1.00</td><td>0.29</td><td>1.00</td><td>0.63</td><td>1.00</td><td>0.77</td><td>1.00</td></tr><tr><td rowspan="3">9</td><td>Case I</td><td>0.78</td><td>1.00</td><td>0.87</td><td>1.00</td><td>0.89</td><td>1.00</td><td>0.94</td><td>1.00</td></tr><tr><td>Case II</td><td>0.67</td><td>1.00</td><td>0.80</td><td>1.00</td><td>0.89</td><td>1.00</td><td>0.94</td><td>1.00</td></tr><tr><td>Case III</td><td>0.33</td><td>1.00</td><td>0.49</td><td>1.00</td><td>0.89</td><td>1.00</td><td>0.94</td><td>1.00</td></tr><tr><td rowspan="3">10</td><td>Case I</td><td>0.80</td><td>1.00</td><td>0.88</td><td>1.00</td><td>0.90</td><td>1.00</td><td>0.95</td><td>1.00</td></tr><tr><td>Case II</td><td>0.60</td><td>1.00</td><td>0.75</td><td>1.00</td><td>0.80</td><td>1.00</td><td>0.88</td><td>1.00</td></tr><tr><td>Case III</td><td>0.30</td><td>1.00</td><td>0.46</td><td>1.00</td><td>0.60</td><td>1.00</td><td>0.75</td><td>1.00</td></tr><tr><td>Average</td><td></td><td>0.56</td><td>1.00</td><td>0.68</td><td>1.00</td><td>0.80</td><td>1.00</td><td>0.88</td><td>1.00</td></tr></table>

First, assume that two features were considered as the target, including Disaster event (Suicide Attack), and Physical target (University). Their weights were set to 100%. CBR would retrieve three cases. Two cases were perfectly matched with target features. According to Table 5, CBR is able to retrieve a recommended case at precision and a recall of 100%, and two other cases at precision of 50%. The result is shown in Fig. 13 (1).

Secondly, we added one more attribute, Terrorism group (Al Qaida), with the weight of 100%. CBR would retrieve two cases at precision of 67%, and one case at precision of 33%. Fig. 12 (2–9) shows the precision and recall scores for k-attributes, where k=3, 4… 10. As can be seen from Table 5, the precision reaches the maximum of 83% at attribute number=6, and the minimum of 25% at attribute number=8.

## 5.2. Experiment II

In the second round of experiments, we compared the effect of the number of attributes on cases retrieved with the OS-CBR approach as shown in Fig. 13 (right side). As each of these nine graphs shows, precision is affected by the number of attributes, while recall remains <sup>fi</sup>rmly at 100% across the all the attributes. Several tests have been conducted to verify the performance of the OS-CBR approach. Two of these tests are presented here.

We use the same assumption as in Experiment I. First, we consider the attribute number=3, according to Table 5. OS-CBR is able to retrieve two cases at precision and a recall of 100%, and one other case at precision of 50%. The result is shown on the right side of Fig. 13 (1).

Secondly, we added one more attribute, terrorism group (Al Qaida), with the weight of 100%. OS-CBR would retrieve one case at precision of 100%, and two cases at precision of 67%. The right side of Fig. 12 (2–9) shows the precision and recall scores for k-attributes, where k=3, 4… 10. As can be seen from Fig. 5, the precision reaches the maximum of 100% at attribute number=2, 3, 4, 5, and 6. The precision reaches the minimum of 50% at attribute number=2, and 6.

Comparing the performance of the two approaches in our experiments, which are shown in Fig. 14, we found that the OS-CBR approach demonstrates signi<sup>fi</sup>cantly better performance than the CBR approach.

Another way to look at these results is to compare the F-measure for the three cases in our experiments, shown in Fig. 14. CBR always suggests Case I, which has better performance than Case II and Case III. For example, when the attribute number=6, Case I is preferred because it has the best F-measure of 91%, compared to an F-measure of 80% and 49% for Case II and Case III, respectively. As shown in Fig. 15, OS-CBR reaches an F-measure of 1.00, 0.91, and 0.67 for Case I, Case II and Case III, respectively (attribute number = 6).

To summarize, the result is shown in Fig. 16 as a graph of Precision similarity against k-attributes. As expected, from a similarity viewpoint, the OS-CBR approach offers the best performance across all k-retrieved cases with a stable overall accuracy, compared to the CBR approach.

To justify the signi<sup>fi</sup>cant difference of this study from others, the Holm test [10], which is a non-parametric statistical test, and the t-test, which is a parametric statistical test, have been applied to 27

![](/api/attachments/ETS2V74N/fulltext/images/1b69a95cbe5c46a77b86acfc266e7ca671dc5ba6d08ed0c0e96b969541b04e2e.jpg)

![](/api/attachments/ETS2V74N/fulltext/images/48dd4f1aa0b883e051e188ff52c486ac2dc0f1769b18741090a0e3b0a81b8cd4.jpg)

![](/api/attachments/ETS2V74N/fulltext/images/021ca8ba9bef27826f5bef1d6d89212f91b9cc9a7b497853db9a84fdf8412cfb.jpg)

![](/api/attachments/ETS2V74N/fulltext/images/bfbb6b36823de289e5717fb44f564e28fc7737bb3715f2cd5170a69dc924b5e6.jpg)  
Fig. 13. Precision and recall of OS-CBR similarity measurement

![](/api/attachments/ETS2V74N/fulltext/images/95c37a96c07156c78596d54a290fa4126f71d66f79cc1cb7b1b43c5827d11dfa.jpg)

![](/api/attachments/ETS2V74N/fulltext/images/872dc9ab02b58d52660d7cd663766e991f89aecbdcb67404d0866a87e24e66ef.jpg)

![](/api/attachments/ETS2V74N/fulltext/images/68668922a4cee0251934070c39bf6f50fee9d1edc375754a459cdb0b71294d28.jpg)

![](/api/attachments/ETS2V74N/fulltext/images/e19e5a31ed1b4a3c75d57dbd222a1ea4796ad26c89183ff6a8f7d8a526bd2f5c.jpg)

![](/api/attachments/ETS2V74N/fulltext/images/91d15a0ebaad2fd569cfaf17ab7d5d958c6572c090a72de3a30d5bef644bb6a8.jpg)  
Fig. 13 (continued).

cases, as shown in Table 5. The results are presented in Tables 6 and 7. Because the p-value is less than it's corresponding α, the null hypothesis of mean equality is rejected and a meaningful difference in precision and F-measure are proven in both levels of signi<sup>fi</sup>cance α=0.05 and $\alpha = 0 . 1$ . To perform the statistical tests in this study, MULTITEST software, which can be downloaded from http://sci2s.ugr.es/sicidm, has been applied.

## 6. OS-CBR system evaluation

The OS-CBR system was evaluated by conducting a user survey with 24 questions, as shown in Table 8. Twenty subjects (users) took part in this survey. All had two to <sup>fi</sup>ve years of working experi ence. Before the survey, a formal presentation was given to all subjects to explain the functions and usage of the OS-CBR system.

![](/api/attachments/ETS2V74N/fulltext/images/1e80766a7a907d1e7d355ffbaf2f889d56a1c0e86617ec3327d7101052bb33ac.jpg)  
Fig. 14. F-measure against k-attributes for CBR.

Table 8 shows the questions that were grouped into four: ease of use, usefulness, disaster information presentation and overall. Each question evaluates the OS-CBR system based either on an information usefulness perspective, or on a usability perspective.

In question 1 of Table 8, the subjects agreed that they can easily use the OS-CBR system, with an overall average rating of 4.26 (questions 1, 2 and 3 of Table 8). This re<sup>fl</sup>ects that OS-CBR system is easy to use with an average rating of 4.22, functions of the OS-CBR system are easy to learn with average rating of 4.44, and it is easy to become skilful in using the OS-CBR with average rating of 4.11.

OS-CBR received an overall rating of 4.32 in usefulness evaluations. Subjects agreed that the OS-CBR helped them to understand how to evaluate the disaster situation more quickly, which is the highest usefulness in other features (Questions 4–12). OS-CBR also improved the ef<sup>fi</sup>ciency and effectiveness of usability with an average rating 4.22 and 4.44 (Questions 7 and 8 of Table 8, respectively).

![](/api/attachments/ETS2V74N/fulltext/images/3556e140a9617a34465d701f2f4303ad3dceb51096b27958a09fe3c71000f052.jpg)  
Fig. 15. F-measure against k-attributes for OS-CBR.

![](/api/attachments/ETS2V74N/fulltext/images/e135c3603aacee164783a38c30d17a21f817221a84a246388bda9499e4d89369.jpg)  
Fig. 16. Precision against k-attributes.

Table 6  
t-Test for comparison of OS-CBR with CBR.

<table><tr><td>Level of significance</td><td>Hypothesis</td><td>t</td><td>p-Value</td><td>Conclusion</td></tr><tr><td>α=0.01</td><td>OS-CBR vs. CBR (Precision)</td><td>6.753</td><td>3.64E-7</td><td>Rejected for OS-CBR</td></tr><tr><td>α=0.01</td><td>OS-CBR vs. CBR (F-measure)</td><td>8.357</td><td>7.73E-9</td><td>Rejected for OS-CBR</td></tr></table>

In the disaster information presentation evaluation, OS-CBR received an overall average rating of 4.30. For example, subjects in the experiment thought that the generated report helped them to understand the current decision support situation with an average rating of 4.67. OS-CBR really helped subjects to make a decision in an emergency situation, for example question 16 of Table 8 scored an average rating of 4.0.

In the overall rating of OS-CBR, the evaluation is 4.20. Subjects thought their mental workload in OS-CBR were reduced with an average rating of 4.44 (Question 20 of Table 8). OS-CBR helped subjects to make decisions more con<sup>fi</sup>dently with an average rating of 4.11. OS-CBR also helped subjects to <sup>fi</sup>nd accurate answers for disaster situations, and to solve input queries with an average rating of 3.89 and 4.33, respectively (Questions 22 and 24 of Table 8).

Furthermore, in terms of usefulness, the overall average rating of OS-CBR is 4.30, which indicates that the information presented by OS-CBR is very helpful for an emergency response system in a disaster situation. In terms of usability, the overall average rating is 4.18, which indicates that the information generated by OS-CBR is easy to use for an emergency response system. The ultimate goal of the OS-CBR process is to support decision makers in disaster situations to make the right and best decisions, by using recalled past experience (question 12), evaluating and understanding the disaster situation (Questions 8 and 9), and developing solutions (Questions 22, 23, and 24). In this sense, OS-CBR performs very well.

## 7. Conclusion and further study

This paper proposes an OS-CBR approach and its system implementation for a decision support system in the MERS, with the capability to improve the ef<sup>fi</sup>ciency of decision makers in an emergency situation. The proposed OS-CBR approach has two main advantages: (1) it has the ability to use ontology-based similarity measures in order to avoid synonym problems and (2) it combines the CBR method and ontology to integrate all the knowledge for emergency situation cases.

Throughout this study we have experimented with the proposed approach using three different problem situations. Our results show the F-measure values reached a high level (0.75–1.00 range) with an average of 88% for all cases retrieved. Our experiments indicate that adding ontology is bene<sup>fi</sup>cial for case similarity. The limitation of this study is that it is focused on data generated by authors to test the usability of the proposed approach; however, more cases are needed to provide a suitable level of complexity.

Table 7  
Holm test for comparison of OS-CBR with CBR.

<table><tr><td>Level of significance</td><td>Hypothesis</td><td> $z = (R_0 - R_1)/SE$ </td><td>p-Value</td><td>Conclusion</td></tr><tr><td> $\alpha = 0.05$ </td><td>OS-CBR vs. CBR (Precision)</td><td>4.619</td><td>3.86E-6</td><td>Rejected for OS-CBR</td></tr><tr><td> $\alpha = 0.05$ </td><td>OS-CBR vs. CBR (F-measure)</td><td>4.619</td><td>3.86E-6</td><td>Rejected for OS-CBR</td></tr></table>

Table 8  
OS-CBR performance evaluation results.

<table><tr><td>Statement</td><td>Subjective rating</td><td>Mean rating</td><td>Standard deviation</td></tr><tr><td>Easy of use</td><td></td><td></td><td></td></tr><tr><td>1. The system is easy to use.</td><td>2</td><td>4.22</td><td>0.83</td></tr><tr><td>2. Functions of the OS-CBR are easy to learn.</td><td>2</td><td>4.44</td><td>0.73</td></tr><tr><td>3. It is easy to become skilful in using the OS-CBR.</td><td>2</td><td>4.11</td><td>0.60</td></tr><tr><td>Usefulness</td><td></td><td></td><td></td></tr><tr><td>4. The OS-CBR system is useful for training purposes.</td><td>1</td><td>4.44</td><td>0.73</td></tr><tr><td>5. OS-CBR is useful as a decision support system.</td><td>1</td><td>4.67</td><td>0.5</td></tr><tr><td>6. The OS-CBR system helps to evaluate the disaster situation</td><td>1</td><td>4.11</td><td>0.60</td></tr><tr><td>7. The OS-CBR system helps me to evaluate the disaster situation more efficiently</td><td>1</td><td>4.22</td><td>0.83</td></tr><tr><td>8. The OS-CBR helps me to evaluate the disaster situation effectively.</td><td>1</td><td>4.44</td><td>0.53</td></tr><tr><td>9. The OS-CBR helps me to understand how to evaluate the disaster situation more quickly</td><td>1</td><td>4.56</td><td>0.53</td></tr><tr><td>10. The OS-CBR system is able to “solve” input query problems</td><td>1</td><td>4.33</td><td>0.5</td></tr><tr><td>11. The OS-CBR system is able to perform the promised service consistently?</td><td>1</td><td>3.89</td><td>0.33</td></tr><tr><td>12. The OS-CBR system contains all the essential cases that could be used to generate solutions for all possible current cases</td><td>1</td><td>4.22</td><td>0.67</td></tr><tr><td>Disaster information presentation</td><td></td><td></td><td></td></tr><tr><td>13. The generated report helped me to understand the current decision support situation</td><td>1</td><td>4.67</td><td>0.5</td></tr><tr><td>14. The generated report helps me to discover faster, well-planned actions.</td><td>1</td><td>4.33</td><td>0.71</td></tr><tr><td>15. The generated report helps me to seek further situation knowledge.</td><td>1</td><td>4.44</td><td>0.73</td></tr><tr><td>16. The generated report helps me to make a final decision.</td><td>1</td><td>4</td><td>0.5</td></tr><tr><td>17. The generated report can be easily understood.</td><td>2</td><td>3.89</td><td>0.60</td></tr><tr><td>18. The generated report is reasonable.</td><td>1</td><td>4.44</td><td>0.53</td></tr><tr><td>Overall</td><td></td><td></td><td></td></tr><tr><td>19. The user interface of OS-CBR is user friendly.</td><td>2</td><td>4.22</td><td>0.67</td></tr><tr><td>20. OS-CBR reduces mental workload during the decision support process</td><td>1</td><td>4.44</td><td>0.53</td></tr><tr><td>21. OS-CBR helps me to make support decisions more confidently.</td><td>1</td><td>4.11</td><td>0.60</td></tr><tr><td>22. OS-CBR helps me to find accurate answers for the problem situations.</td><td>1</td><td>3.89</td><td>0.60</td></tr><tr><td>23. Overall, the OS-CBR system is reliable.</td><td>1</td><td>4.22</td><td>0.44</td></tr><tr><td>24. The OS-CBR system is able to “solve” input query problems.</td><td>1</td><td>4.33</td><td>0.71</td></tr></table>

Further study will include completing other sections of the MERS, and we will focus on developing mechanisms for easier integration of a MERS solution with existing emergency response systems (traditional and web-based emergency systems) to support easier knowledge management in the system.

## Acknowledgments

The work presented in this paper was supported by the Australian Research Council (ARC) under Discovery Project DP0880739.

## References

[1] K. Amailef, J. Lu, m-Government: a framework of mobile-based emergency response system, The International Conference on Intelligent System and Knowledge Engineering, IEEE Press, Xiamen China, 2008, pp. 1398–1403.

[2] K. Amailef, J. Lu, J. MA, Text information extraction and aggregation in a mobile-based emergency response system, New Perspectives on Risk Analysis and Crisis Response: Proceedings of the 2nd International Conference on Risk Analysis and Crisis Response, Atlantis Press, Beijing, China, 2009, pp. 186–191.

[3] G. Antoniou, F. Harmelen, A Semantic Web Primer, MIT Press, 2008.

[4] D. Brickley, R.V. Guha, RDF Vocabulary Description Language 1.0: RDF Schema, viewed 23/05/2010 http://www.w3.org/TR/rdf-schema/2004.

[5] R. Chen, R. Sharman, H.R. Roa, S. upadhyaya, Design Principles of Coordinated Multi-incident Emergency Response Systems, vol. 3495, Springer, Berlin/ Heidelberg2005

[6] A. Ferrández, Lexical and syntactic knowledge for information retrieval, Information Processing and Management 47 (5) (2011) 692–705.

[7] J.C.E. Heidi, A.M. Ralph, R.d.L. Trishan, D. Jonathan, R. Jonathan, Can humanitarian open-source software development draw new students to CS? SIGCSE Bull. 39 (1) (2007) 551–555.

[8] B. Henderson-Sellers, Bridging metamodels and ontologies in software engineering, Journal of Systems and Software 84 (2) (2011) 301–313.

[9] P.J. Herrera, P. Iglesias, G. Sánchez, B. Díaz-Agudo, JaDaCook 2: cooking over ontological knowledge, the 2nd computer cooking contest, 2009.

[10] S. Holm, A simple sequentially rejective multiple test procedure, Scandinavian Journal of Statistics 6 (1979) 65–70.

[11] C.-C. Huang, T.-L. Tseng, Rough set approach to case-based reasoning application, Expert Systems with Applications 26 (3) (2004) 369–385.

[12] ITU, Information and Communication Technology (ICT) Statistics, viewed 23/06/2011 http://www.itu.int/ITU-D/ict/index.html2011.

[13] K. Katharina, A. Cem, M. Silvia, How can information extraction ease formalizing treatment processes in clinical practice guidelines? Arti<sup>fi</sup>cial Intelligence in Medicine 39 (2) (2007) 151–163.

[14] S. Kim, R. Maciejewski, K. Ostmo, E.J. Delp, T.F. Collins, D.S. Ebert, Mobile analytics for emergency response and training, Information Visualization Houndmills 7 (1) (2008) 77–88.

[15] T. Kucza, Knowledge Management Process Model, Technical Research Centre of Finland, 2001.

[16] K.F.R. Liu, Agent-based resource discovery architecture for environmental emergency management, Expert Systems with Applications 27 (1) (2004) 77–95.

[17] J. Lu, J. Ma, G. Zhang, Zh.u. Yijun, X. Zheng, K. Ludovic, Theme-based comprehensive evaluation in new product development using fuzzy hierarchical criteria group decision-making method, Industrial Electronics, IEEE Transactions on on Industrial Electronics 58 (6) (2011) 2236–2246.

[18] A. Malizia, T. Onorati, P. Diaz, I. Aedo, F. Astorga-Paliza, SEMA4A: an ontology for emergency noti<sup>fi</sup>cation systems accessibility, Expert Systems with Applications 37 (4) (2010) 3380–3391.

[19] A. Mansourian, A. Rajabifard, M.J. Valadan Zoej, I. Williamson, Using SDI and web-based system to facilitate disaster management, Computers & Geosciences 32 (3) (2006) 303–315.

[20] L. McGinty, D.C. Wilson, Case-based reasoning research and development, 8th International Conference on Case-Based Reasoning, Springer, Seattle, WA, 2009.

[21] K. Morten, N. Esben Toftdahl, K. Margit, Challenges in designing interactive systems for emergency response, e Proceedings of the 6th conference on Designing Interactive systems, University Park, PA, USA, 2006.

[22] N.A. Nasharuddin, M.T. Abdullah, R.A. Kadir, A. Azman, A review on the cross-lingual information retrieval, Information Retrieval & Knowledge Management, (CAMP), 2010, pp. 353–357.

[23] J. Park, W. Cho, S. Rho, Evaluating ontology extraction tools using a comprehensive evaluation framework, Data & Knowledge Engineering 69 (10) (2010) 1043-1061

[24] D. Phillips, Texas 9-1-1: emergency telecommunications and the genesis of surveillance infrastructure, Telecommunications Policy 29 (11) (2005) 843–856.

[25] J.A. Recio-Garía, B. Díaz-Agudo, Ontology based CBR with jCOLIBRI, in: R. Ellis, T. Allen, A. Tuson (Eds.), Applications and Innovations in Intelligent Systems, XIV, Springer, London, 2007, pp. 149–162.

[26] C.D. Robinson, E.B. Donald, First responder information <sup>fl</sup>ow simulation: a tool for technology assessment, Proceedings of the 37th conference on Winter simulation, ACM Press, Orlando, Florida, 2005, pp. 919–925

[27] S. Shiu, S.K. Pal, Foundations of Soft Case-based Reasoning, Wiley-Interscience, 2004.

[28] G. Urbas T. Krone Mobile and wireless technologies: security and risk factors paper presented to the Trends & issues in crime and criminal justice no. 329, 2006.

[29] T. Virkki-Hatakka, G.L.L. Reniers, A case-based reasoning safety decision-support tool: nextcase/safety, Expert Systems with Applications 36 (7) (2009) 10374–10380.

[30] M.-C. Wu, Y.-F. Lo, S.-H. Hsu, A fuzzy CBR technique for generating product ideas, Expert Systems with Applications 34 (1) (2008) 530–540.

[31] Z. Yang, F. Deng, W. Liu, Y. Fang, A CBR method for CFW prevention and treatment, Expert Systems with Applications 36 (3) (2009) 5469–5474, (Part 1).

[32] X. Yu, M. Tungare, W. Fan, Y. Yuan, M. Pérez-Quiñones, E.A. Fox, W. Cameron, L. Cassel, Using automatic metadata extraction to build a structured syllabus repository, Proceedings of the 10th International Conference on Asian Digital Libraries: Looking Back 10 years and Forging New Frontiers, Springer, Hanoi, Vietnam, 2007, pp. 337–346.

[34] H. Zhang, Y.-F. Li, H.B.K. Tan, Measuring design complexity of semantic web ontologies, Journal of Systems and Software 83 (5) (2010) 803–814.

[33] L.A. Zadeh, Fuzzy sets, Information and Control 8 (3) (1965) 338–353.

Professor Jie Lu is the Head of School of Software in the Faculty of Engineering and Information Technology, and the Director of the Decision Systems and e-Service Intelligence Research Laboratory in the Centre for Quantum Computation & Intelligent Systems at the University of Technology, Sydney (UTS). She received her PhD from Curtin University of Technology in 2000. Her main research interests lie in the area of decision making modeling, decision support system tools, uncertain information processing, recommender systems and e-Government and e-Service intelligence. She has published <sup>fi</sup>ve research books and 270 papers in refereed journals and conference proceedings. She has won <sup>fi</sup>ve Australian Research Council (ARC) discovery grants. She received the <sup>fi</sup>rst UTS Research Excellent Medal for Teaching and Research Integration in 2010. She serves as Editor-In-Chief for Knowledge-Based Systems (Elsevier), editor for book series on Intelligent Information Systems (World Scienti<sup>fi</sup>c).
