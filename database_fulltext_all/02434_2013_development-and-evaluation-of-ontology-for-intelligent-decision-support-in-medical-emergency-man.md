---
otero_id: 2434
otero_key: "9FJRAZW7"
title: "Development and evaluation of ontology for intelligent decision support in medical emergency management for mass gatherings"
authors: "Pari Delir Haghighi; Frada Burstein; Arkady Zaslavsky; Paul Arbon"
year: "2013"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2012.11.013"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Development and evaluation of ontology for intelligent decision support in medical emergency management for mass gatherings

Pari Delir Haghighi <sup>a</sup>, Frada Burstein <sup>a,</sup>⁎, Arkady Zaslavsky <sup>b</sup>, Paul Arbon <sup>c</sup>

<sup>a</sup> Monash University, Australia

<sup>b</sup> CSIRO, Australia

<sup>c</sup> Flinders University, Australia

## a r t i c l e i n f o

Article history: Received 24 October 2011 Received in revised form 2 August 2012 Accepted 11 November 2012 Available online 23 November 2012

Keywords: Intelligent decision support Ontology development and evaluation Medical emergency management Mass gatherings Case-based reasoning Knowledge management

## a b s t r a c t

Conducting a safe and successful major event highly depends on the effective provision of medical emergency services that are often offered by different public and private agencies. Poor communication and coordination between these agencies and teams can result in delays in decision-making and duplication of efforts. Another related issue is that emergency decisions are usually made based on individual experience and domain knowledge of relevant managerial personnel. For sustainable knowledge management and more intelligent decision support it is bene<sup>fi</sup>cial to collect, consolidate, store and share these experiences in a form of a knowledge base or domain ontology. State-of-the-art surveys identify this gap that there is no common ontology describing the domain knowledge for planning and managing medical services in mass gatherings. Part of the reason is that the process of construction of such an ontology is not a trivial task. In this paper, we describe the process of developing and evaluating a Domain Ontology for Mass Gatherings (DO4MG) with a focus on medical emergency management. As part of the evaluation, we illustrate the application of DO4MG for implementing a case-based reasoning decision support for emergency medical management in mass gatherings. Such an implementation demonstrates the potential of using ontology for resolving terminology inconsistencies and their usefulness for supporting communication between medical emergency personnel in mass gatherings. We also illustrate how this ontology can be applied to different stages of medical emergency management as part of a system architecture. The lessons learnt from building DO4MG for this domain could be bene<sup>fi</sup>cial in general to the theory and practice of intelligent decision support and knowl edge management in complex problem domains.

Crown Copyright © 2012 Published by Elsevier B.V. All rights reserved.

## 1. Introduction

Medical emergency decision making could be a challenging task, particularly during mass gathering events [2,75]. In mass gatherings, when a crisis occurs, medical emergency decisions are usually made under time pressure [3]. Further, these events typically involve participation of various emergency medical agencies that frequently use different terminology to represent the same concepts. This inconsistency can complicate communication between different emergency teams as well as integration and management of data recorded in these events.

Intelligent decision support systems aim to provide decision makers with timely, useful and valid information based on some pre-coded domain knowledge [12]; and medical emergency services (MES) in mass gatherings can bene<sup>fi</sup>t from access to such systems [27,74,75]. The underlying condition for successful development of such a system is creation of a reliable mechanism for collection, representation, and storage of domain knowledge. Literature shows that there is no common ontology describing the domain knowledge for planning and managing medical services in mass gatherings.

We suggest that better knowledge management for decision support can bene<sup>fi</sup>t from standardization of mass gathering's medical emergency management (MEM) terminology using domain ontology [64]. The importance of incorporating an ontology into a system architecture has been well recognized, in the context of intelligent decision support, as the means of knowledge representation and management and to assist decision makers with complex problem-solving [15,20,36]. With regard to mass gatherings, ontologies can improve coordination and interaction between different emergency agencies and facilitate data capture, storage, integration and querying of recorded data in the events. Moreover, the use of a common and uni<sup>fi</sup>ed domain ontology can improve the decision making process where most of the emergency decisions are dependent on individual experiences and domain knowledge of relevant managerial personnel.

The need for further research in knowledge management and decision support in medical emergency management is well recognized [2,27,71]. A domain ontology for medical emergency management is a mechanism for providing a consistent view on the problem domain that can be used by all concerned stakeholders. Delir Haghighi et al. [18] introduced a domain ontology, named DO4MG (Domain Ontology for Mass Gatherings), and discussed how it could improve decision making in the <sup>fi</sup>eld of medical emergency management by providing a uni<sup>fi</sup>ed and common knowledge base for intelligent decision support. However, one of the major requirements to adopt a domain-speci<sup>fi</sup>c ontology is to determine its <sup>fi</sup>tness and suitability over other existing ontologies in the same <sup>fi</sup>eld and to evaluate the given ontology against certain criteria and a set of standards [10,70]. Ontology evaluation requires the use of explicit and formal criteria that match ontology construction objectives.

During the years, many evaluation approaches and criteria have been proposed to analyze and validate ontologies [10]. These evaluation methods normally focused on speci<sup>fi</sup>c domain problems, and were tested for validating a certain type of ontology. These past studies con<sup>fi</sup>rmed that it is important to select an evaluation approach which <sup>fi</sup>ts the given ontology and its application domain. In this paper we present an approach for creating and evaluating the domain ontology for medical emergency management. We undertake the task of an extensive review of the existing approaches for ontology evaluation and propose a systematic process suitable for the mass gathering ontology. This includes assessment of the proposed ontology by domain experts and from its application perspective. We describe the application of the ontology within the overall mass gathering management as an integral part of knowledge management for running a safe event [19]. An example of a case-based reasoning (CBR) intelligent decision support implementation of this architecture is also presented.

In this paper, we make two main contributions as follows.

• First, we present a thorough review of current ontology evaluation methods on the basis of multiple criteria and describe the process of selecting the ones applicable for validation of DO4MG. These include the process of empirical testing of the evaluation method with the domain experts. In doing so, we also report on the lessons learned and therefore provide a re<sup>fi</sup>ned understanding of ontology evaluation methods.

• Second we describe an ontology-based system architecture for medical emergency management in mass gatherings that incorporates the DO4MG ontology, which illustrates effectiveness of the proposed approach for ontology construction and evaluation. As an example, a CBR prototype decision support system (DSS), which can be used during the pre-event and post-event stages of mass gathering events for respectively training, workload estimation and data collection and integration is described. This DSS uses the ontology to provide a uni<sup>fi</sup>ed and standard vocabulary of the domain and to overcome any problems that can arise from inconsistencies in terminology and discrepancies of data collection in emergency management for mass gatherings.

Both contributions, although validated in a speci<sup>fi</sup>c problem domain, can provide a useful insight for researchers and practitioners in dealing with complex decision situations, which involve multiple agencies and a wealth of expert knowledge.

The rest of this paper is organized as follows. Section 2 de<sup>fi</sup>nes ontologies and presents the bene<sup>fi</sup>ts of ontologies for intelligent decision support systems. Section 3 provides an overview of decision support systems for MEM in general and then discusses the application of ontologies to medical management emergency in mass gatherings. Section 4 describes the development process that we propose for building DO4MG including pre-development and design stages. Section 5 presents an overview of the current ontology evaluation approaches and provides justi<sup>fi</sup>cation for selected evaluation methods for DO4MG. Section 6 describes the application of the evaluation and re<sup>fi</sup>nement methods for verifying the contents and testing usability of DO4MG.

These include criteria-based and application-based evaluations. The criteria-based evaluation includes the re<sup>fi</sup>nement of DO4MG according to the domain experts' feedback. The application-speci<sup>fi</sup>c evaluation of DO4MG details the overall architecture for intelligent decision support in mass gatherings and an illustration of the case-based reasoning prototype developed to test its usability. Finally, Section 7 concludes the paper and suggests some directions for further research.

## 2. The role of ontologies in DSS

An ontology presents ‘a shared and common understanding of the knowledge domain’ [15:786] using major concepts and terms applied in that domain and identi<sup>fi</sup>es the relationships between these concepts. Ontologies enable aggregation and use of knowledge items and sub-processes and provide a way to move from a document-oriented view of knowledge management to a content-oriented view [63]. An ontology provides a world view and the shared understanding of a given domain which can be used as a unifying framework to address the domain problems [66]. As Gruber suggests “an ontology is an explicit speci<sup>fi</sup>cation of a conceptualization” [29:1].

The core of any decision support system is knowledge from which, and of which, decisions are made [12]. To provide a structured and formal representation of knowledge, ontologies have been applied to a number of DSS [15,48,51]. For example, Musen et al., [51] proposed EON architecture as a decision support system for protocol-based therapy. EON integrates an ontology that represents clinical protocols such as drug therapy to bene<sup>fi</sup>t from a shared and computer-based representation of all the common data elements in a precise and consistent structure. EUEDE (End-User Enabled Design Environment) [48] for dairy farm management applied semantic ontology tools to achieve effective decision systems, which are context sensitive to end-user factors and provided a generic knowledge model applicable across rural industries.

OntoWEDSS (Ontology-based Wastewater Environmental Decision-Support System) [15] uses ontologies to solve complex problems related to environmental science and engineering. The inclusion of ontologies in that study allowed improved modeling of wastewater treatment processes and facilitated the communication among different components of the environmental DSS. The advisory system for crime investigation processes proposed by Dzemydiene and Kazemikaitiene [20], used ontologies to ensure that the crime information was extracted and represented in a structured model format appropriate for decision-making in crime investigation.

Most of these examples do not report on the ontology evaluation process, neither provide enough details on general principles that can be applied to developing and evaluating other ontologies. At the same time prior research conducted by Sujanto, et al. [64] for example, demonstrated the importance of a rigorous process of ontology development and the lack of consistency in current approaches to ontology evaluation. Sujanto et al. [65] proposed a framework for development and evaluation of medical emergency management ontology from the generic design science principles.

In the work presented in this paper, we focus on qualitatively extending the approach introduced by Sujanto et al. [64] for medical decision support in the mass gathering context. We also propose a systematic validation methodology which includes formal methods and uses expert feedback for validation and re<sup>fi</sup>nement of the ontology for decision support.

The next section introduces the context for our research and discusses the importance of intelligent decision support in medical emergency decision making.

## 3. Intelligent decision support for medical emergency management

Decision support systems are in high demand when users need to make informed decisions especially during emergency situations [12,74]. Emergency situations are time-constrained and dynamic environments that change rapidly [9]. Access to up to date information and data is critical in emergency management decision support, in particular to determine the priorities for operation and resource allocation and management [9,22,74]. Examples of such systems include the Australian NSW Fire Brigades I-Zone planning system [14] and Gold Coast DSS for <sup>fl</sup>ood emergency management [50].

A common approach to decision support is employing analytical models that usually result in generation of potential solutions, evaluation/comparisons of these options based on some parameters (criteria) and selecting the best option accordingly [12,19]. In emergency situations, due to the time pressure and uncertainty, it is argued that intuitive decision processes such as recognition-primed decision (RPD) model can result in higher performance compared to analytical models [37,57]. The RPD approach describes how experienced people make decisions in uncertain and time-critical environments by extracting a course of action that matches the occurring situation and implementing it. Typically emergency incidents are not entirely identical to each other but the knowledge of past incidents enables emergency personnel and commanders to recognize a similar situation and tailor their strategies accordingly by taking a course of action that experience has shown is effective and successful [41]. The experience can be gained through attendance at many different emergency situations and, to a lesser extent through studying procedures and past incidents [16].

Case-based reasoning [39] is one of the approaches used for intelligent decision support [5], which can bene<sup>fi</sup>t decision making in emergency situations. CBR is used in decision making that produces solutions by providing access to past events in a case base and retrieving the experiences (i.e. cases) that are similar to the ‘problem case’ and providing solutions that were successfully applied in similar situations in the past [16,41]. The effectiveness of CBR can be further improved by the application of ontologies as a mechanism for reasoning about the domain concepts and dealing with the inconsistencies that can arise in the applied vocabulary when multiple agencies are involved. In Section 6 we describe an overall architecture for intelligent decision support in emergency management and use CBR as part of the application-based validation of the ontology.

The next section describes the knowledge management needs in mass gatherings, as well as the context in which the decisions are typically made.

3.1. The need for ontology-based intelligent decision support for MEM in mass gatherings

Mass gatherings are de<sup>fi</sup>ned as a temporary collection of large numbers of people at one location or over multiple sites. Examples include music concerts, sporting events, cultural gatherings, and parades. During emergencies in mass gathering events, the medical emergency teams and other emergency personnel need to make complex and time-critical decisions. These decisions can relate to timely treatment of injured or ill spectators, more advanced levels of medical care, which requires rapid evacuation of patients to nearby hospitals, requests for external and additional resources and maintaining the safety of the crowd [2,73]. Making such emergency decisions under time pressure can be facilitated by using appropriate decision support systems that cater for mass gathering emergency problems. Ontologies can also be utilized in developing DSS for mass gathering to further assist emergency teams and services with the decision-making process.

Planning and managing a safe mass gathering event requires involvement of various stakeholders such as emergency medical services, police, security personnel, ambulance services and <sup>fi</sup>rst aiders. Different agencies and services frequently use different terminology and employ emergency plans that may be established independent of other agencies. This fact increases the complexity of coordination and interaction between the involved teams during the emergencies. Inter-organizational collaboration and coordination is essential to ensure the provision of appropriate and timely medical care and to maintain a safe working environment [72]. A mass gathering ontology can be applied and shared across all events and facilitate coordination and communication between different teams [45,58].

The role of ontologies in supporting knowledge sharing activities has been emphasized by many researchers [28,31]. This strength of ontologies has been particularly recognized in crisis and emergency systems where it is imperative to share knowledge in order to establish effective coordination between stakeholders and reduce ambiguities during decision making [45]. Examples of systems that apply ontologies include rescue operation management [40], emergency evacuation planning [42], emergency alerts [45] and emergency response [58].

An ontology for mass gathering provides a common understanding of mass gatherings, their characteristics, and the relationships between them. Its inclusion in medical emergency decision support systems enables dealing with the inconsistencies and discrepancies that could arise from data modeling and management by various researchers and agencies. Since to the best of our knowledge, there is no standard ontology for this domain, we undertook a systematic review of the relevant approaches from other domains. In the next section we present an overview of the ontology development process, which was applied to construct and evaluate Domain Ontology for Mass Gatherings — DO4MG.

## 4. Development of DO4MG

Ontologies can be built from scratch or they can reuse existing ontologies. Holsapple and Joshi [34] classify ontology design approaches into <sup>fi</sup>ve categories. These include 1) inspiration approach that is based on individual creativities and personal views, 2) induction approach where the ontology is created by observation and analysis of a particular case in that domain, 3) deduction technique applies general principles and adapts them according to a speci<sup>fi</sup>c case, 4) synthesis approach <sup>fi</sup>rst identi<sup>fi</sup>es a set of ontologies and then synthesizes them with other related concepts and 5) collaboration approach is concerned with a joint effort and using the group members experience and opinions to build the ontology. Our ontology design can be considered as a hybrid approach that combines inspiration, induction and collaboration techniques as described in this section.

Methodologies provide a systemic and repeatable guideline for building ontologies and enable sharing, reuse and extension of the ontologies by others [23,24,30,34]. Some example methodologies introduced for speci<sup>fi</sup>c domains are: i) enterprise modeling processes ontology proposed by Uschold and King [66], ii) Methontology for the domain of chemicals proposed by Fernández-López et al. [23,24], iii) the generic guidelines proposed in Ontology 101 [52], iv) the knowledge metaprocess introduced by Staab et al. [63] that targets knowledge management applications (implemented), v) the OntoClean methodology for validation of ‘the adequacy and logical consistency of taxonomic relationships’ [32:201], and vi) the methodology for creating business ontology supporting semantic interoperability [53].

Development of a domain ontology for medical emergency management in mass gatherings requires a rigorous and inclusive ontology development approach as well as an ontology evaluation method involving domain experts. Studying the above-mentioned methodologies reveals that there are certain steps in these methodologies that are relatively common. The four overlapping stages that we have identi<sup>fi</sup>ed include: i) specifying the ontology scope and objectives, ii) knowledge acquisition and identifying key concepts, iii) building/coding, and iv) evaluation. We have followed similar steps in DO4MG ontology development.

Fig. 1 depicts the main steps in the process of ontology development and evaluation. These steps will be discussed and exempli<sup>fi</sup>ed in the context of a domain ontology for medical emergency management in mass gatherings in this paper. In addition to these steps, some other approaches such as those proposed by Bernaras et al. [8] and Staab et al. [63] explicitly specify a stage for re<sup>fi</sup>nement of the ontology based on expert feedback to improve the <sup>fi</sup>nal product. Taking into account the context of our ontology, emergency management, it was very important to also consider the re<sup>fi</sup>nement phase to ensure the best quality outcome. This stage was incorporated as part of the evaluation phase and is described in Section 6.

The next subsections discuss the proposed ontology development stages that have been followed for development of DO4MG.

## 4.1. Pre-development stages of DO4MG

## 4.1.1. Identifying the scope and objectives

As a <sup>fi</sup>rst step we have identi<sup>fi</sup>ed the scope and objectives of the DO4MG. The ontology focuses on MEM for mass gathering events and therefore its users include emergency medical services such as <sup>fi</sup>rst aiders, nurses, ambulance services and other involved teams in mass gathering events. The primary purpose of the ontology is to provide a better understanding of these events and enable access to domain knowledge for study and analysis. For instance, the ontology can be used for developing knowledge management applications (including an online knowledge base) to enable stakeholders to study, utilize and extend the ontology collectively. The DO4MG offers a standard knowledge structure and model (common terminology) that can be shared and used between different stakeholders, applicable to any type of emergency or mass gathering event. It can be utilized as a uni<sup>fi</sup>ed knowledge base for improving communication and interaction between different emergency teams and for assisting decision makers with event planning and resource allocation. Moreover, it can facilitate integration of mass gathering data and its management (i.e. storage and querying).

## 4.1.2. Knowledge acquisition

After identifying the ontology's scope and objectives, the second stage, i.e. knowledge acquisition, involves discovering, eliciting and extracting knowledge from the domain of interest. The resources that we have used at this stage included primary journals and conference papers for emergency and crisis management (e.g. conference proceedings for the Integrative and Analytical Approaches to Crisis Response and Emergency Management Information Systems (ISCRAM) and the Australian Journal of Emergency Management (AJEM) were used as primary starting points). In addition, public reports, and government manuals were used such as the Emergency Management Australia (EMA)

![](/api/attachments/9FJRAZW7/fulltext/images/46fd622879c476621d70cb55d9fd2334166f1f52cc9c4dc97f45bbd658027701.jpg)  
Fig. 1. An overview of step-by-step process of ontology development and evaluation.

manuals series for mass gatherings, and the ‘Compendium of Mass Gatherings’ that includes a collection of papers mainly from the Prehospital and Disaster Medicine journal (PDM), an Of<sup>fi</sup>cial Publication of the World Association for Disaster and Emergency Medicine, collected by its President, Professor Arbon (2009). Delir Haghighi et al. [32] presented an overview of mass gathering concepts extracted from the literature (see Table 1 below). Each concept was further discussed with the experts, de<sup>fi</sup>ned, and documented including the reference sources.

In addition to the above resources, we also gathered the domain knowledge and key concepts and elements from domain experts and researchers working in the <sup>fi</sup>eld of EM during individual interviews (with three experts) and a focus group with 10 participants (discussed in Section 6.1).

## 4.2. Design and implementation of DO4MG

The DO4MG ontology is implemented in Protégé $4 . 0 , ^ { 1 }$ which supports OWL (Web Ontology Language) [47], a common ontology language used to de<sup>fi</sup>ne and describe the concepts (classes), subclasses, properties, and associated relationships of the domain of interest. The core of DO4MG is the concept of Mass Gathering. There are <sup>fi</sup>ve main key concepts, in the DO4MG ontology, which de<sup>fi</sup>ne every mass gathering event. These include CrowdFeatures, EventVenue, GatheringType, EnvironmentalFactors and MassGatheringPlan (shown in the left hand side of Fig. 2). The second level of the ontology includes 38 subclasses, i.e. “children” or “leaf classes”, which are broken into further subclasses. The total number of classes considering all the levels is 234. The encoding of the elements includes de<sup>fi</sup>nitions for most of the domain concepts and provides the references for sources of its origin. The slots/properties, instances and relations are de<sup>fi</sup>ned for the concepts for better understanding and to enable querying and reasoning about the concepts. Fig. 2 shows an example of using protégé to de-<sup>fi</sup>ne relationships, instances and properties for the DO4MG ontology.

The PersonalBrain $5 . 5 ^ { 2 }$ system has been used to visualize and present the entire ontology. The software has extra features which enable to attach <sup>fi</sup>les of the referenced papers used in de<sup>fi</sup>ning the concepts, which is useful for the ontology long-term management and documentation. Fig. 3 depicts the use of the PersonalBrain for codi<sup>fi</sup>cation and visualization of DO4MG. The <sup>fi</sup>gure shows the main classes of the ontology and some of their subclasses. The software provides an easy and <sup>fl</sup>exible interface to visualize and traverse the classes.

This concludes the process of ontology development. The next section provides an overview of ontology evaluation approaches and justi<sup>fi</sup>cation for the selection of evaluation methods for DO4MG.

## 5. DO4MG ontology evaluation

Due to the increasing availability of ontologies, it is imperative to evaluate existing ontologies as the basis of designing new, and to determine whether the ontology is suitable for representing certain domains and applications within it [69]. Ontology evaluation requires use of proper and formal evaluation criteria and methodologies. Therefore, it is important to select and apply an appropriate evaluation approach which is <sup>fi</sup>tting to the given ontology and its application domain. The next subsection provides a critical review of ontology evaluation approaches and derives the one, which we consider suitable and applied it for DO4MG evaluation.

Table 1  
Mass gathering concepts and characteristics extracted from the literature (adapted from [32])

<table><tr><td>Reference source</td><td>Concepts and variables</td></tr><tr><td>Milsten et al. [49]</td><td>Weather, attendance, event duration, whether event occurring indoors/outdoors, seated or mobile, event type, crowd mood, alcohol or drugs, crowd density, locale/physical plant, age</td></tr><tr><td>Arbon [2,3]</td><td>Psychological domain (i.e. crowd behavior and mood, individual motivation and behavior, crowd interests and culture, attendance reason, duration, use of alcohol or drugs); biomedical domain (i.e. health status, latent potential for illness/injury, age, heat or cold-related physiology, alcohol or drug-related physiology); environmental domain (i.e. crowd attendance/density, venue, event type, outdoor/indoor weather, availability of alcohol or drugs)</td></tr><tr><td>Parrillo [54]</td><td>Structure and location, nature of event, crowd size and demographics, environmental factors, transportation, equipment and involved agencies such as police</td></tr><tr><td>Berlonghi [7] and EMA [22]</td><td>Crowd type: ambulatory, disability/limited movement, cohesive/spectator, expressive/revelous, participatory, aggressive/hostile, demonstrator, escape/trampling, dense/suffocating, rushing/looting, violent</td></tr><tr><td>Zeitz et al. [73]</td><td>Crowd mood: passive, active and energetic</td></tr><tr><td>De Lorenzo [17]</td><td>Weather, duration, mobility, crowd mood, crowd density, and alcohol and drugs</td></tr><tr><td>AEM, Manual 2, [4]</td><td>Venue, crowd movement, hazards, event type, legal issues, police and security, defense assistance, safety issues (i.e. emergency response plan, indoors/outdoors, load capacity, seating, emergency tools, fire safety, communication systems, OHS), crowd control (e.g. entrance and exits, barriers, seating, alcohol, drugs and weapons), public health (e.g. food safety, water, infection control), medical care (e.g. ambulance, medical teams and equipment), psychological dimension, high risk events</td></tr></table>

## 5.1. An overview of ontology evaluation approaches

During the years, researchers have proposed a variety of approaches for evaluating ontologies. Brank et al. [10] categorizes these approaches into four main classes as follows:

1. The ‘gold standard’ evaluation — This approach compares the ontology to high-level and ‘golden’ standards which can be an ontology itself [44]. For example, Abramowicz et al. [1] describe the gold standard built ontology based on the input obtained from an expert group during a series of workshops. With regard to the gold standard evaluation, in some scenarios, access to such standards (or ontology) or its provision may not be possible. Furthermore, the evaluation results can suffer from the <sup>fl</sup>aws in the applied comparison methodology or from inappropriateness of the gold standard [11].

2. Data driven evaluation — This assessment method compares the ontology with a source of data such as a corpus [11]. The datadriven approach compares the ontology to a corpus, for example, by performing automated term extraction on the corpus and counting the number of terms that overlap between the ontology and the corpus [11]. If the terms used in the ontology are not present in the corpus or vice versa, the ontology is penalized. Such an evaluation approach is not suitable for assessing the correctness, clarity, or usefulness/applicability of an ontology and is more <sup>fi</sup>tting for measuring coverage of the ontology. The coverage has been also considered as one of the criterion in the criteria-based evaluation [69,70] that will be discussed later.

3. Evaluation by humans — This approach uses a set of pre-de<sup>fi</sup>ned criteria. Lozano-Tello and Gómez-Pérez [43] proposed Ontometric, a method to “quantify the suitability of these ontologies for the system” [pg.3], which is an example of a human-based evaluation approach. Ontometric is a multilevel framework of characteristics that allows the users to measure the suitability of existing ontologies considering the requirements of a system. The measurements are based on the <sup>fi</sup>ve main dimensions of tools, language, content, methodology, and costs. However, this approach exhibits limited support for building an ontology from scratch and evaluating it.

4. Application-based evaluation — The application-based evaluation approach <sup>fi</sup>rst uses the ontology in an application and then evaluates the results. This approach is very useful to assess the capabilities of the developed ontology to meet its objectives, e.g. decision support or knowledge management. Yet it does not validate the quality of the content and design of the ontology.

Yu et al. [70], in comparison, suggests three main categories for ontology evaluation as follows:

5. The gold standard evaluation — It can be seen that the <sup>fi</sup>rst one, the “gold standard evaluation” is overlapping with the approach proposed by Brank et al. [10].

6. Task-based evaluation — The task-based evaluation, similar to the application-based evaluation proposed by Brank et al. [10], assesses the ontology according to its competency in achieving target tasks by measuring its performance within the context of the application. Yu et al. [70] suggest this approach to be conducted for each task separately, because evaluation results for different applications and tasks may not be comparable with each other.

7. Criteria-based evaluation — The criteria-based evaluation uses a set of proposed criteria for evaluating the ontology [29]. This approach has some similarity with the third, evaluation by humans, category speci<sup>fi</sup>ed by Brank et al. [10], but is more generic and <sup>fl</sup>exible. The criteria-based evaluation can verify the content and design of the ontology and the application-based evaluation can assess the usability and applicability of the ontology in its application domain. The criteria-based evaluation requires the use of appropriate and effective attributes.

In the literature, there are various criteria speci<sup>fi</sup>ed for evaluation of ontologies. For example, to measure the quality of ontology design, Wand and Weber [67] consider the clarity and completeness of ontology constructs and propose the criteria of Construct Overload, Construct Redundancy, Construct Excess, and Construct De<sup>fi</sup>cit for examining them. They argue that these criteria measure the de<sup>fi</sup>ciencies which could undermine the usefulness of the ontology. This evaluation model has been later extended and modi<sup>fi</sup>ed by researchers to cater for additional requirements [56]. We have synthesized the criteria proposed by these authors and Table 1 presents the summary and comparison of commonly used evaluation criteria. Out of these, Yu et al. [69,70] integrate most of the existing criteria and include in addition an attribute of coverage (Table 2).

![](/api/attachments/9FJRAZW7/fulltext/images/39165d79a64c4c1f30547a6d53150782422befa54aea06400fce0e198d55366a.jpg)  
Fig. 2. An example of properties and instances used in DO4MG

![](/api/attachments/9FJRAZW7/fulltext/images/f63427cf7b6ca9e350ed70c625226a47c2fa54186bb3c7928c33c96a5418dc0f.jpg)  
Fig. 3. An overview of the DO4MG using PersonalBrain system.

The above review demonstrates that there is no one approach which will perfectly <sup>fi</sup>t all the objectives of ontology evaluation, hence it is often the case that a combination of the above or their variation is used. In the next section we propose and argue for a selection of approaches and criteria adopted for DO4MG evaluation.

## 5.2. Selection of evaluation approach for DO4MG

Having reviewed different ontology evaluation approaches, based on the DO4MG's objectives and the limitations of each approach, such as the lack of gold standards as well as of an existing ontology for mass gathering, we have selected the following two approaches for DO4MG evaluation:

Table 2  
Examples of various criteria to evaluate ontologies.

<table><tr><td>Gruber [28]</td><td>Gomez-Perez [25]</td><td>Yu et al. [69,70]</td></tr><tr><td>Clarity</td><td>-</td><td>Clarity</td></tr><tr><td>Coherence</td><td>Consistency</td><td>Consistency/coherence</td></tr><tr><td>Extendibility</td><td>Expandability</td><td>Expandability/extendibility</td></tr><tr><td>Minimal encoding bias</td><td>-</td><td>Minimal encoding bias</td></tr><tr><td>Minimal ontological commitments</td><td>-</td><td>Minimal ontological commitments</td></tr><tr><td>-</td><td>Conciseness</td><td>Conciseness</td></tr><tr><td>-</td><td>Completeness</td><td>Completeness</td></tr><tr><td>-</td><td>Sensitiveness</td><td>-</td></tr><tr><td>-</td><td>-</td><td>Coverage</td></tr><tr><td>-</td><td>-</td><td>Correctness</td></tr></table>

• Criteria-based evaluation; and

• Application-based evaluation.

Considering the evaluation criteria discussed in Section 5.1, we selected eight criteria which match the objectives of DO4MG. These criteria include: 1) clarity; 2) consistency/coherence; 3) conciseness; 4) expandability/extendibility; 5) correctness; 6) completeness; 7) minimal ontological commitment; and 8) coverage.

The two criteria that we have not considered are sensitiveness and minimal encoding bias. The sensitiveness of the ontology [25] refers to how minor changes in the de<sup>fi</sup>nitions can modify other wellde<sup>fi</sup>ned properties that have already been guaranteed. Using this criterion requires a standard measuring tool that can determine the level of sensitivity made by changes. However, since we assume a regular review and update of the ontology performed in collaboration with human experts, any changes of de<sup>fi</sup>nitions, either minor, or major will be performed accordingly. The relationships between the concepts would also capture the need for such modi<sup>fi</sup>cations.

The criterion of minimal encoding bias suggests that the ontology representation should not be limited to a certain symbol-level encoding due to the convenience of implementation. DO4MG is implemented in Protégé-OWL which provides the adequate representation choices in order to meet our objectives.

The following section reports on the results of the criteria and application-based evaluation.

## 6. Results of evaluation and re<sup>fi</sup>nement of DO4MG

To evaluate the ontology, we reviewed each concept individually based on the selected criteria and then conducted a focus group with domain experts who looked at the proposed ontology and evaluated its content in particular, for clarity, completeness, consistency, and correctness. As the result of this session the expandability of it was also demonstrated. The details of the focus group are presented in the following subsection.

## 6.1. Data collection for ontology evaluation

There are different techniques for data collection in a group setting. Examples of two well-known methods are focus groups and Delphi method. Holsapple and Joshi [34] propose the Delphi approach as an effective collaborative technique for ontology design. Delphi is a systematic and iterative process to assist a group of experts to arrive at a consensus [33,68]. This approach generally requires the use of a questionnaire, and responses are typically collected anonymously and without the need for a face-to-face meeting. Alternatively, a focus group technique can be used to collect rich qualitative data when access to the group can be arranged [60]. This technique is similar to a group interview and is coordinated by a facilitator who has strong personal skills. We selected the focus group technique since there was an opportunity for a face-to-face meeting with a group of highly quali<sup>fi</sup>ed emergency management domain experts to assist with our data collection and ontology validation. This allowed us to avoid the need for a long and complex questionnaire about more than 200 ontology concepts. Moreover, one of the group members who had previous experience as a facilitator had the role of the moderator in our focus group.

The focus group to validate and re<sup>fi</sup>ne the DO4MG involved 10 participants from different emergency management related organizations, including the World Association for Disaster and Emergency Medicine, St John Ambulance Australia, Metropolitan Ambulance Victoria, and Flinders University, Adelaide, Australia. The selection of the participants was based on their research, domain knowledge, publications and professional experience in the area of mass gathering medical management in Australia. Our aim was to use their advice to validate the draft domain ontology and improve and re<sup>fi</sup>ne it based on their feedback.

First the facilitator presented an overview of DO4MG ontology to the participants. Then he showed them every main concept of the ontology and its subclasses and collected feedback. Every ontology concept, its subclasses, and the relationships between them were discussed and suggested changes were recorded. This included deletion of some concepts and addition of new concepts.

In the next subsection we discuss examples of the domain expert feedback to re<sup>fi</sup>ne the ontology as part of our criteria-based evaluation.

## 6.2. Criteria-based evaluation of DO4MG

In this section, we describe how the data that was collected from focus group was used to conduct the evaluation according to the selected criteria.

Clarity — Gruber [28] states three requirements for clarity that include the following: i) the ontology terms should be de<sup>fi</sup>ned formally without subjectivity; ii) the ontology needs to be documented with natural language, and iii) the terms must convey ‘the intended meaning’ with regard to the requirements of social situations and computation rather than their context. In the context of formal de<sup>fi</sup>nition of the ontology terms, since we have mainly extracted these terms from the domain-related publications, formal de<sup>fi</sup>nitions are available for most of the terms. For example, the term ‘Crowd Catalyst’ is de-<sup>fi</sup>ned as factors that “contribute to or trigger a crowd from being one that is managed to one that needs to be controlled” [7:245]. We have documented these terms using natural language. With regard to the third requirement, as Yu et al. [70] suggest, that lack of measurement methods for clarity makes assessing clarity a dif<sup>fi</sup>cult task. Having access to domain experts was important and provided an ef<sup>fi</sup>- cient way to verify the clarity of the ontology and re<sup>fi</sup>ne it based on their feedback.

Examples — In the DO4GM ontology, we had ‘CrowdControl’ as a key concept that included several subclasses such as CrowdCatalyst and CrowdMood. During our focus group with domain experts, it was pointed out that the term did not communicate the intended meaning and it was replaced with ‘CrowdFeatures’ to improve clarity.

We also had a subclass of ‘Pollution’ under the ‘EnvironmentalFactors concept. Based on the feedback, this was replaced with ‘AirQuality’ with instances of ‘Dust’, ‘Pollen’, ‘Smoke’, etc.

Consistency/coherence — The concepts and elements of ontology should have a logical consistency and avoid contradictions or ambiguity. The ontology “should sanction inferences that are not consistent with the de<sup>fi</sup>nitions” [29:3]. The consistency check produced several examples where changes were required based on experts' advice.

Examples — Initially the ‘GatheringType’ was broken into two subclasses of ‘GeneralGathering’ such as political or cultural events and ‘HighRiskGathering’ like <sup>fi</sup>reworks or motor racing; according to Emergency Management Australia, Manual 2, Safe and Healthy Mass Gatherings [21] and [6]. However, the inferences were considered inconsistent and contradictory with the de<sup>fi</sup>ned concepts because in the event types such as a <sup>fi</sup>rework gathering the preparedness measures are increased and this reduces the risk. Thus a political gathering (i.e. a general gathering event) might have a higher risk than a <sup>fi</sup>rework gathering. Based on the feedback, the concepts of ‘general’ and ‘high risk’ gatherings were removed and all the gathering types were grouped under the ‘GatheringType’.

We had included the subclass ‘Insurance’ under the ‘Mass GatheringPlan’. In the focus group, we found out that the insurance topic was carrying some ambiguity. There could be different types of insurance policies involved in planning a mass gathering event. These policies are considered to be, generally, the responsibility of the event organizers rather than emergency medical services. Since the DO4MG ontology targets the MEM, this term was removed to avoid the ambiguity and to maintain consistency.

Conciseness — The conciseness criterion means that an ontology should not include unnecessary concepts or redundancies [26,69]. This aspect has been carefully considered during our ontology development and validation.

An example — The only redundant term used in the ontology was ‘Parking’. This term was a subclass of ‘Internal Structure’ (also subclass of ‘EventVenue’) and an instance of ‘Event Management’ (also a subclass of CrowdCatalyst belonging to the class ‘CrowdFeatures’). However, since the ‘Parking’ under ‘Event Management’ refers to the lack of adequate parking spaces for the crowd, it was changed into ‘LackOfParking’.

Expendability/extendibility — This criterion refers to the ability of ontology to extend further or to be applied to a speci<sup>fi</sup>c application domain. DOEM has been built such that it provides for the reuse and extension of the different parts of the ontology.

An example — In [13], the proposed ontology for emergency transportation in mass gatherings is an extension to DO4MG. The left hand side of Fig. 4 shows the concept of ‘EmergencyTransportation’ in DO4MG, and the right graph shows the extension of DO4MG for ‘Transportation’.

Correctness — Correctness means that the ontology represents the correct modeling of the real-world concepts [69]. The correctness of DO4MG has been the main focus of our evaluation. The feedback provided by domain experts has greatly assisted in verifying this criterion.

An Example — In the DO4GM, ‘EnvironmentalFactors’ had subclasses of ‘NeighbouringLand’, ‘Insects’, ‘Darknesss’, ‘Venue’, ‘Weather’, ‘Watercourse’, ‘Animals’, and ‘Pollution’. This concept was notably revised according the feedback of domain experts.

Minimal ontological commitment — This criterion refers to allowing more <sup>fl</sup>exibility and freedom in the specialization of the ontology by minimizing the claims about the modeled world [28]. Yu et al. [69] examine this attribute with regard to supporting multiple views for the same information and <sup>fl</sup>exibility in classifying items.

Table 3  
![](/api/attachments/9FJRAZW7/fulltext/images/86405c2fad48eb9e158ecead5beb7065cf9298b0c7416b1428f4ec3348631051.jpg)  
Fig. 4. Extending DO4MG for emergency transportation.

We have evaluated this feature by developing applications that target different activities of the domain.

Completeness — This criterion applies to completeness of the individual de<sup>fi</sup>nitions of the ontology [63,69]. As Yu et al. [69] suggest this attribute can be evaluated by using competency questions which include the queries and requirements that the ontology must be able to answer [30,63]. Because of the size of the DO4MG, we present only two examples of the competency questions in Table 3.

Coverage is one of our selected criteria for ontology evaluation. To examine the DO4MG coverage, we employed a different approach. We conducted a simple experiment using a text mining software system, Leximancer [61,62] and compared the results with those included in the DO4MG ontology. The next subsection describes this evaluation.

## 6.2.1. Coverage

Coverage can be de<sup>fi</sup>ned as the completeness and coverage of terms and concepts to represent an information domain [69]. The criterion of coverage is more suitable for the data-driven evaluation where the ontology is compared to a corpus. The concepts of DO4MG were mainly extracted manually from current publications on the medical emergency management for mass gatherings or added by domain experts.

Leximancer is a computer-assisted text analysis application that uses a machine-learning technique for conceptual analysis and relational/ semantic analysis [62]. Leximancer enables discovering new information from text-based resources, <sup>fi</sup>nding patterns, and generating context maps and statistical outputs that provides an insight into a large amount of data corpus and a set of documents [61,62]. We used Leximancer to extract the main concepts and terms from the two main sets of documents that cover the domain of mass gathering. These two resources are the ‘Mass Gathering Compendium’ collected by Arbon and the Emergency Management Australia Manual ‘Safe and Healthy Mass Gatherings’, 1999, Part III, Vol. 2, Manual 2. Fig. 5 depicts the visualization and analysis output which has been automatically created.

An example of the competency questions used to evaluate completeness.

<table><tr><td>Competency questions</td><td>Concept</td><td>Relations</td></tr><tr><td rowspan="3">What demographic factors of the crowd need to be considered?</td><td>Age</td><td>hasDemographicsOf</td></tr><tr><td>Gender</td><td></td></tr><tr><td>Ethnicity</td><td></td></tr></table>

The themes are large circles that represent the main groupings of concepts (clusters) within the above-mentioned documents. We did the test using the default Leximancer parameters without any con<sup>fi</sup>guration and that resulted in extracting some of the noise words and concepts such as Nornberge, data, information, area, public, system, on-site, people, support, staff, etc. The <sup>fi</sup>gure also shows some overlapping/repeating clusters like Medical, medical and Disaster Medicine, and Crowd and Spectators.

Comparing the <sup>fi</sup>gure with our ontology, all the extracted concepts are included in the DO4MG but with a different hierarchical structure, except for the noise words which are either incomplete, too general or out of context. The DO4MG has <sup>fi</sup>ve main concepts (<sup>fi</sup>rst level) that include EventVenue, GatheringType, CrowdFeatures, MassGatheringPlan (including MedicalResponse, PatientPresentation and Injury subclasses), and EnvironmentalFactors (including WaterCourse and Weather subclasses). The extracted Crowd and Spectator correspond to CrowdFeatures, Event to Gathering Type, and Medical, Disaster Medicine and Patients to the MedicalResponse subclass under the MassGatheringPlan. The Alcohol, Water, and Access can be mapped to the subclasses of AlcoholSale, AlcoholUse, Watercourse, AccessEgress under the EnvironmentalFactors class. The Mass cluster which is too broad and incomplete can be matched to the MassGatheringPlan class.

The other extracted terms inside the clusters (ignoring the noise words) are also included in the ontology like food, <sup>fi</sup>rst-aid, police, ambulance, time yet with a relatively different structure. This experiment is useful to match and validate the concepts of an ontology against a related corpus and identify the overlapping or absent concepts. However, it also shows the limitations of Leximancer to discover the accurate hierarchy and relationships of these concepts in each cluster. Based on our <sup>fi</sup>ndings we suggest that this stage requires signi<sup>fi</sup>cant re<sup>fi</sup>nement by domain experts.

## 6.3. Application-specific evaluation of DO4MG

To perform application-speci<sup>fi</sup>c evaluation of DO4MG, we have developed generic architecture for intelligent decision support and knowledge management in mass gatherings that integrates DO4MG (shown in Fig. 6). The aim was to verify our ontology development and evaluation approach and also validate the usability of the DO4MG ontology for resolving problems which require the clear structure of the problem domain. These problems include terminological differences and semantic con<sup>fl</sup>icts that may arise from applying the different terminology used by medical emergency services to express the same concept.

![](/api/attachments/9FJRAZW7/fulltext/images/e37f02ca321908f81a1ed2a23a0124cfa17d89d603e2b25828f970c6e1984ca8.jpg)  
Fig. 5. Concept map produced by Leximancer for the mass gathering corpus.

![](/api/attachments/9FJRAZW7/fulltext/images/f195bffa5b7fb70ba8d02ce28b7a23bfc501cd72a237b64f6a65df4764f23915.jpg)  
Fig. 6. A comprehensive architecture for mass gatherings integrating ontologies Adapted from [19].

Organizing a successful mass gathering is complex and includes several stages and a variety of tasks which require participation of different agencies and services. In general mass gathering activities and tasks can be grouped under three phases of pre-event, during-theevent and post-event phases. The pre-event phase typically involves training, workload estimation and planning the event. The duringthe-event phase is the operational stage where medical response and treatment are provided and there is a need for real-time DSS. The <sup>fi</sup>nal stage of mass gathering usually entails recording data, debrie<sup>fi</sup>ng, evaluation of the event. Using a common ontology in all the stages of mass gatherings provides consistency and effectiveness in all the activities, and facilitates data entry, management, <sup>fi</sup>ltering and integration, avoids discrepancies [19,64,65].

The case-based reasoning application [19] can be used during the pre-event stage of mass gathering (see Fig. 6) for predicting workload and assisting trainees and during the post-event stage for improving data collection, integration and storage.

The data set used in this application includes 201 records of different mass gathering events which was collected by St John Ambulance Australia personnel (St. John, 2010). The CBR prototype [19] was implemented using the jCOLIBRI2 framework<sup>3</sup> in Java. jCOLIBRI2 is an open source tool that provides supports for development of different CBR applications including ontology-based CBR systems by using the Onto-Bridge<sup>4</sup> libraries [55]. The application enables the user to enter the details of a future event (querying stage) such as the event type and location, the number of attendees, environmental values like temperature and humidity (as shown in Fig. 7).

As Fig. 7 shows some of the attributes like Gathering Type allows the user to directly select the input from the ontology. After de<sup>fi</sup>ning a future event, the user will enter two important values which are patient presentation rate and transportation to hospital rate. These two attributes are used to estimate the workload of medical emergency services. For example, a larger number of attendees or higher temperature and humidity may result in a higher rate of patients and transportation to hospital. The CBR application enables the user to compare their estimated patient presentation rate (PPR) to the similar events in the past. This comparison provides users with better understanding of such events and assists them with decision making about the expected workload and required resources. The usability of DO4MG is mainly assessed during the retrieve stage. During this stage, a ‘problem case’ entered by the user is compared to the case base (i.e. stored past events) by using the selected similarity functions, and the most similar cases are retrieved. At this stage we demonstrate how the DO4MG ontology deals with terminology con<sup>fl</sup>icts.

Reviewing the literature for mass gathering shows that different researchers or agencies use different attributes/terms to record the same concept [35,38,46,49,71]. For example, there are terms that represent the same or a very similar concept to ‘motor racing’. These terms include ‘auto racing’ [49], ‘motor sports’ [38], ‘motor race’[35], and ‘automobile races’ [46].

When the data from several events need to be integrated or used collectively, the inconsistencies and discrepancies between different data sets can complicate data integration and management [19]. If the recorded data and the query entered by the user use different terms/ attributes but have the same meaning, they will not be matched correctly. To address this issue, ontologies provide an elegant solution by supporting synonyms and providing richer queries that could be performed using concept based similarity functions [19,55]. The DO4MG is developed in Protege which provides several options to create synonyms. We have used annotations (i.e. labels) to create different synonyms for a concept. For ‘motor racing’ we have included all the above-mentioned synonyms as labels in DO4MG ontology.

The data set used for case-based reasoning can store different terms/words to express the same concept which can lead to inaccurate retrieval of similar cases. Through using the ontology and de<sup>fi</sup>ned synonyms, the developed application is able to match the terms speci<sup>fi</sup>ed in the query correctly to the stored cases such that all the synonyms will be considered at the retrieve stage. Thus the accuracy of results and generated solutions was improved. In our example, the ‘MotorSports’ attribute used in the data set has been matched correctly to the ‘MotorRacing’ concept in the DO4MG ontology because it was de<sup>fi</sup>ned as its synonym. This will retrieve the correct cases from the data set and resolves the issue of inconsistency and terminology con<sup>fl</sup>icts.

The developed prototype demonstrates feasibility of applying DO4MG to the decision support system component to deal with complexity and inconsistency of decisions in medical emergency management, thus satisfying the requirements of the application-based evaluation of our ontology.

## 7. Conclusion

Ontologies as a uni<sup>fi</sup>ed representation of a problem domain provide a common basis to deal with coordination issues, inconsistencies and communication between different emergency teams in mass gatherings, and are often recommended as part of knowledge management for intelligent decision support systems [59,63,64]. Despite an increasing number of ontologies, there is still no generic agreement on how they can be constructed in the most ef<sup>fi</sup>cient way to facilitate better knowledge management and decision-making. When using ontologies for decision support in the risk-intensive context, such as emergency management in mass gatherings, it is imperative to determine whether they provide a valid representation of the application domain.

In this paper, we described the process of construction and evaluation of DO4MG (Domain Ontology for Mass Gatherings) based on a systematic review of the literature, analysis and synthesis of existing methods of ontology construction that can be applied to other domains. The resulting ontology was evaluated based on two main approaches; criteria-based and application-speci<sup>fi</sup>c evaluation. As part of the validation, we illustrated the application of the DO4MG for implementation of a cased-based reasoning decision support for medical emergency management in mass gatherings. Such implementation demonstrates the potential bene<sup>fi</sup>ts of using ontologies in resolving terminology inconsistencies and con<sup>fl</sup>icts, and its usefulness to increase the ef<sup>fi</sup>ciency of communication between emergency medical personnel in mass gatherings.

In future, we intend to use the constructed ontology and developed evaluation methodology in other decision support approaches and study the outcomes involving <sup>fi</sup>eld studies and domain experts. We aim to offer this ontology to others as a validated robust description of this important problem domain. We also intend to target mobile applications and implement ontology-based decisions support for MEM in mass gatherings that can operate on mobile devices as extension to the proposed approach [19,32]. The potential of transferability of the approaches used in this research onto other areas of ontology creation would be worthwhile empirical testing.

## Acknowledgments

This research is funded by Australian Research Council (ARC) Linkage grant LP0774834.

![](/api/attachments/9FJRAZW7/fulltext/images/9992e89293db45267e2ceb1bf812227527fe91f1dca18a8d8824baefcac028a7.jpg)  
Fig. 7. The querying stage of CBR using DO4MG ontology.

The team includes CIs: Prof Frada Burstein, A/Prof Shonali Krishnaswami, Prof Paul Arbon, PI: Prof Arkady Zaslavsly; Research Fellow Dr Pari Delir Haghighi. We acknowledge support of Jamie Ranse in conducting the focus group as part of data collection for this paper.

## References

[1] W. Abramowicz, M. Vargas-Vera, M. Wisniewski, Axiom-based feedback cycle for relation extraction in ontology learning from text, in: DEXA Workshops, 2008, pp. 202–206.

[2] P. Arbon, The development of conceptual models for mass-gathering health, Prehospital and Disaster Medicine: The Of<sup>fi</sup>cial Journal of the National Association of EMS Physicians and the World Association for Emergency and Disaster Medicine in association with the Acute Care Foundation 19 (2004) 208–212.

[3] P. Arbon, Mass-gathering medicine: a review of the evidence and future directions for research, Prehospital and Disaster Medicine: The Of<sup>fi</sup>cial Journal of the National Association of EMS Physicians and the World Association for Emergency and Disaster Medi cine in association with the Acute Care Foundation 22 (2007) 131–135.

[4] Australian emergency manuals series: manual 2—safe and healthy mass gatherings, A Health, Medical and Safety Planning Manual for Public Events, Commonwealth of Australia, Dickson ACT, 1999.

[5] O. Babka, S. Whar, Case-based reasoning and decision support systems, in: IEEE International Conference on Intelligent Processing Systems (ICIPS '97), Beijing, China, 1997, pp. 1532–1536.

[6] A.E. Berlonghi, The Special Event Risk Management Manual, The Special Event Liability Series Volume 1. Dana Point CA USA: Alexander Berlonghi 1994

[7] A. Berlonghi, Understanding and planning for different spectator crowds, Safety Science 18 (1995) 239–247

[8] A. Bernaras, I. Laresgoiti, J. Corera, Building and reusing ontologies for electrical network applications, in: Proceedings of the European Conference on Arti<sup>fi</sup>cial Intelligence (ECAI'96), 1996, pp. 298–302.

[9] M.R.S. Borges, S.F. Ochoa, J.A. Pino, A.S. Vivacqua, Assigning emergency vehicles to urban incidents, in: DSS, 2010, pp. 498–509.

[10] J. Brank, M. Grobelnik, D. Mladenic, in: A Survey of Ontology Evaluation Techniques in Proceedings of Conference on Data Mining and Data Warehouses (SiKDD 2005), Ljubljana, Slovenia, 2005.

[11] C. Brewster, H. Alani, S. Dasmahapatra, Y. Wilks, Data driven ontology evaluation, in: Proc. of Intl. Conf. on Lang. Resources and Eval., Lisbon, Portugal, 2004.

[12] F. Burstein, S. Carlsson, Decision support through knowledge management, in: Frada Burstein, Clyde W. Holsapple (Eds.), Handbook on Decision Support Sys tems 1: Basic Themes, Springer-Verlag, Berlin Germany, 2008, pp. 103–120.

[13] F. Burstein, P. Delir Haghighi, A. Zaslavsky, Context-aware mobile medical emergency management decision support system for safe transportation, chapter 9 in decision support: an examination of the DSS discipline, Annals of Information Systems 14 (2010) 163–181.

[14] G. Byrne, I-Zone planning: supporting frontline <sup>fi</sup>re<sup>fi</sup>ghters, The Australian Journal of EM 24 (2009) 48-58.

[15] L. Ceccaroni, U. Cortes, M. Sanchez-Marre, Ontowedss: augmenting environmental decision-support systems with ontologies, Environmental Modelling and Soft ware 19 (2004) 785–797.

[16] B. Chakraborty, D. Ghosh, R.K. Maji, S. Garnaik, N. Debnath, Knowledge management with case-based reasoning applied on fire emergency handling, in: 8th IEEE Interna. tional Conference on Industrial Informatics (INDIN), 2010, pp. 708–713.

[17] R.A. De Lorenzo, Mass gathering medicine: a review. Prehospital and Disaster Medicine: The Official Journal of the National Association of EMS Physicians and the World Association for Emergency and Disaster Medicine in association with the Acute Care Foundation 12 (1997) 68–72.

[18] P. Delir Haghighi, F. Burstein, H. Al Taiar, P. Arbon, S. Krishnaswamy, Ontology-based service-oriented architecture for emergency management in mass gatherings, in: IEEE International Conference on Service-Oriented Computing and Applications (SOCA'10), December 13–15, IEEE Computer Society, Perth, Australia, 2010.

[19] P. Delir Haghighi, F. Burstein, P. Arbon, A. Zaslavsky, Using ontology for IT-enabled comprehensive management of mass gatherings, in: Ana Respício, Frada Burstein (Eds.), Frontiers in Arti<sup>fi</sup>cial Intelligence and Applications, Fusing Decision Support Systems into the Fabric of the Context, 238, IOS Press, 2012, pp. 303–314

[20] D. Dzemydiene, E. Kažemikaitiene, Ontology-based Decision support system for crime investigation processes, in: A. Caplinskas, O. Vasilecas, W. Woitkowsky, S. Wrycza, et al., (Eds.), Information Systems Development: Advances in Theory Practice and Education, Kluwer Academic Press, 2005, pp. 245–256.

[21] Emergency Management Australia, [On line] Australian emergency manual: safe and healthy mass gatherings, emergency management Australia, Commonwealth of Australia, Canberra, 1999. (Accessed 11 September 2011, http://www.health. sa.gov.au/PEHS/publications/ema-mass-gatherings-manual.pdf).

[22] A. Engelbrecht, M.R.S. Borges, A.S. Vivacqua, Digital tabletops for situational awareness in emergency situations, in: CSCWD, 2011, pp. 669–676.

[23] M. Fernández-López, A. Gómez-Pérez, Overview and analysis of methodologies for building ontologies, The Knowledge Engineering Review 17 (2002) 129–156.

[24] M. Fernández-López, A. Gómez-Pérez, J.P. Sierra, A.P. Sierra, Building a chemical ontology using methontology and the ontology design environment, IEEE Intelli gent Systems 14 (1999) 37–45.

[25] A. Gómez-Pérez, Towards a framework to verify knowledge sharing technology, Expert Systems with Applications 11 (1996) 519–529.

[26] A. Gómez-Pérez, Evaluation of ontologies, International Journal of Intelligent Systems 16 (2001) 391–409.

[27] M. Gaynor, M. Seltzer, S. Moulton, J. Freedman, A dynamic, data-driven, decision support system for emergency medical services, in: International Conference on Computational Science, 2, 2006, pp. 703–711.

[28] T.R. Gruber, Toward principles for the design of ontologies used for knowledge sharing, International Journal of Human Computer Studies 43 (1995) 907–928.

[29] M. Grüninger, M. Fox, Methodology for the design and evaluation of ontologies, in: IJCAI'95, Workshop on Basic Ontological Issues in Knowledge Sharing, 1995.

[30] M. Gruninger, J. Lee, Ontology applications and design, in: Special Issue in Communications of the ACM (CACM), 45. 2002, pp. 39–45

[31] N. Guarino, C.A. Welty, An overview of ontoclean, in: S. Staab, D. Rudi Studer (Eds.), International Handbooks on Information Systems, 2009, Handbook on Ontologies, Part 2, Springer, 2009, pp. 201–220.

[32] Delir Haghighi, F. Burstein, A. Zaslavsky, P. Arbon, S. Krishnaswamy, The role of domain ontology for medical emergency management in mass gatherings, in: Ana Respicio, Frederic Adam, Gloria Phillips-Wren, Carlos Teixeira, Joao Telhada (Eds.), Bridging the Socio-technical Gap in Decision Support Systems: Challenges for the Next Decade, IOS Press, Amsterdam Netherlands, 2010, pp. 520–531.

[33] F. Hasson, S. Keeney, H. McKenna, Research guidelines for the Delphi survey technique, Journal of Advanced Nursing 32 (2000) 1008–1015.

[34] C.W. Holsapple, K.D. Joshi, A collaborative approach to ontology design, Communications of the ACM 45 (2002) 42–47.

[35] K.M. Johnsson, P.A. Örtenwall, A.L. Kivi, A.H. Hedelin, Medical support during the European Union Summit in Gothenberg, Prehospital and Disaster Medicine: The Of<sup>fi</sup>cial Journal of the National Association of EMS Physicians and the World Association for Emergency and Disaster Medicine in association with the Acute Care Foundation 21 (2006) 282–285.

[36] I. Jurisica, J. Mylopoulos, E. Yu, Ontologies for knowledge management: an information systems perspective, Knowledge and Information Systems 6 (2004) 380–401.

[37] G.A. Klein, in: G.A. Klein, J. Orasanu, R. Calderwood, C.E. Zsambok (Eds.), A Recognition-Primed Decision (RPD) Model of Rapid Decision Making, Ablex, 1993, pp. 138–147.

[38] K. Koenig, C. Schultz, Koenig and Schultz's disaster medicine, Comprehensive Principles and Practices, Cambridge University Press, December 2009.

[39] J.L. Kolodner, An introduction to case-based reasoning, Arti<sup>fi</sup>cial Intelligence Review 6(1992)3-34

[40] S. Konstantopoulos, G. Paliouras, J. Schon, D. Schneider, T. Winkler, J. Pottebaum, R. Koch, in: Mobile Response: Second International Workshop on Mobile Information Technology for Emergency Response, MobileResponse, 2008, pp. 112–121, (Bonn, Germany)

[41] A. Lewis, RIMSAT DSS project: integrating model-based and case-based reasoning, DSSResources.COM. Available: http://dssresources.com/papers/features/lewis lewis04052004 html2004

[42] X. Li, G. Liu, A. Ling, J. Zhan, N. An, L. Li, Y. Sha, Building a practical ontology for emergency response systems, in: International Conference on Computer Science and Software Engineering, CSSE, vol. 4, 2008, pp. 222–225.

[43] A. Lozano-Tello, A. Gómez-Pérez, Ontometric: a method to choose the appropriate ontology, Journal of Database Management 15 (2004) 1–18.

[44] A. Maedche, S. Staab, Measuring similarity between ontologies, in: Proc. of 13th Intl. Conf. on Knowledge Eng. and Knowledge Management Ontologies and the Semantic Web, Springer, 2002, pp. 251–263.

[45] A. Malizia, F. Astorga-Paliza, T. Onorati, P. Díaz, I. Aedo, Emergency alerts for all: an ontology based approach to improve accessibility in emergency alerting systems, in: Proceedings of the 5th International ISCRAM Conference — Washington, DC, USA, 2008.

[46] C. Martin-Gill, W.J. Brady, K. Barlotta, A. Yoder, A. Williamson, B. Sojka, D. Haugh, M.L. Martin, M. Sidebottom, L. Sandridge, MSd hospital-based healthcare provider (nurse and physician) integration into an emergency medical services–managed massgathering event, The American Journal of Emergency Medicine 25 (2007) 15–22.

[47] D.L. McGuinness, F. van Harmelen, [On line] Owl Web Ontology Language overview: W3c recommendation. 10 February. 2004 World Wide Web Consortium (W3C). last accessed 8 September 2011 http://www.w3.org/TR/owl-features/.

[48] S.J. Miah, J. Gammack, D. Kerr, Ontology development for context-sensitive decision support, in: Third International Conference on Semantics, Knowledge and Grid (SKG 2007) Xian China 2007.

[49] A.M. Milsten, B.J. Maguire, R.A. Bissell, Seaman KG: mass-gathering medical care: a review of the literature, Prehospital and Disaster Medicine: The Of<sup>fi</sup>cial Journal of the National Association of EMS Physicians and the World Association for Emergency and Disaster Medicine in association with the Acute Care Foundation 17 (2002) 151–162.

[50] H. Mirfenderesk, Flood emergency management decision support system on the Gold Coast, Australia, The Australian Journal of EM 24 (2009) 17–24.

[51] M.A. Musen, S.W. Tu, A. Das, Y. Shahar, Eon: a component-based approach to automation of protocol-directed therapy, Journal of the AMIA 3 (1996) 367–388.

[52] N.F. Noy, D.L. McGuinness, Ontology development 101: a guide to creating your <sup>fi</sup>rst ontology, in: Stanford Knowledge Systems Laboratory Technical Report KSL-01-05 and Stanford Medical Informatics Technical Report SMI-2001-0880, March 2001.

[53] A. Paredes-Moreno, F.J. Martínez-López, D.G. Schwartz, A methodology for the semi-automatic creation of data-driven detailed business ontologies, Information Systems 35 (2010) 758–773.

[54] S.J. Parrillo, Medical care at mass gatherings: considerations for physician involvement, Prehospital and Disaster Medicine: The Official Journal of the National Association of EMS Physicians and the World Association for Emergency and Disaster Medicine in association with the Acute Care Foundation 10 (1995) 273–275.

[55] J.A. Recio-García, B. Díaz-Agudo, A.A. Sánchez-Ruiz, P.A. González-Calero, Lessons learnt in the development of a CBR framework, in: Proceedings of the 11th UK Workshop on Case Based Reasoning, CMS Press, University of Greenwich, 2006

[56] M. Rosemann, P. Green, M. Indulska, Towards an enhanced methodology for ontological analyses, in: 16th International Conference on Advanced Information Systems Engineering, Faculty of Computer Science and Information Technology, Riga, 2004, pp. 122–131.

[57] K.G. Ross, G.A. Klein, P. Thunholm, J.F. Schmitt, H.C. Baxter, The recognitionprimed decision model, Military Review (2004) 6–10.

[58] X. Ru-zhi, D. Xiao-liang, Y. Feng, L. Pei-guang, Research on the construction method of emergency plan ontology based-on OWL, in: Proceedings of the 2009 International Symposium on Web Information Systems and Applications (WISA'09) Nanchang, China, 2009, pp. 19–23.

[59] P. Serwylo, P. Arbon, G. Rumantir, Predicting patient presentation rates at mass gatherings using machine learning, in: 8th International Conference on Information Systems for Crisis Response and Management (ISCRAM 2011), Lisbon, Portugal, 2011.

[60] J. Sim, Collecting and analysing qualitative data: issues raised by the focus group, Journal of Advanced Nursing 28 (1998) 345–352.

[61] A.E. Smith, Automatic extraction of semantic networks from text using Leximancer in: Human Language Technology Conference 2003

[62] A.E. Smith, M.S. Humphreys, Evaluation of unsupervised semantic mapping of natural language with Leximancer concept mapping, Behavior Research Methods 38 (2006) 262–279.

[63] S. Staab, R. Studer, H. Schnurr, Y. Sure, Knowledge processes and ontologies, Intelligent Systems 16 (2001) 26–34.

[64] F. Sujanto, F. Burstein, A.S. Ceglowski, L. Churilov, Application of domain ontology for decision support in medical emergency coordination, in: Proceedings of the 14th Americas Conference on Information Systems, Information Systems, Toronto, Canada, 2008.

[65] F. Sujanto, A.S. Ceglowski, F. Burstein, L. Churilov, An integrated framework for comprehensive collaborative emergency management, in: P. Zarate, J. Belaud, G. Camilleri E. Ravat (Eds.) Collaborative Decision Making: Perspectives and Challenges, IOS Press, Amsterdam Netherlands, 2008, pp. 127–138.

[66] M. Uschold, M. Gr¨uninger, Ontologies: principles, methods and applications, The Knowledge Engineering Review 11 (1996) 93–155.

[67] Y. Wand, R. Weber, Research commentary: information systems and conceptual modeling a research agenda, Information Systems Research 13 (2002) 363–376.

[68] P.L. Williams, C. Webb, The Delphi technique: an adaptive research tool, British Journal of Occupational Therapy 61 (1994) 153–156.

[69] J. Yu, J.A. Thom, A. Tam, Evaluating ontology criteria for requirements in a geographic travel domain, in: Proc. of Intl. Conf. on Ontologies, Databases and Applications of Semantics, 2005.

[70] J. Yu, J.A. Thom, A. Tam, Ontology evaluation using Wikipedia categories for browsing, in: Proceedings of the Sixteenth ACM Conference on Conference on Information and Knowledge Management, ACM, Lisbon, Portugal, 2007, pp. 223–232.

[71] K. Zeitz, D. Schneider, D. Jarrett, C. Zeitz, Mass gathering events: retrospective analysis of patient presentations over seven years at an agricultural and horticultural show, Prehospital and Disaster Medicine: The Of<sup>fi</sup>cial Journal of the National Association of EMS Physicians and the World Association for Emergency and Disaster Medicine in association with the Acute Care Foundation 17 (2002) 147–150.

[72] K. Zeitz, C. Zeitz, P. Arbon, F. Cheney, R. Johnston, J. Hennekam, Practical solutions for injury surveillance at mass gatherings, Prehospital and Disaster Medicine: The Of<sup>fi</sup>cial Journal of the National Association of EMS Physicians and the World Association for Emergency and Disaster Medicine in association with the Acute Care Foundation 23 (2008) 76–81

[73] K.M. Zeitz, H.M. Tan, C.J. Zeitz, Crowd behavior at mass gatherings: a literature review, Prehospital and Disaster Medicine 21 (2009) 32–38.

[74] A. Zerger, D.I. Smith, Impediments to using GIS for real-time disaster decision support, Computers, Environment and Urban Systems 27 (2003) 123–141.

[75] S. Zhu, J. Abraham, S.A. Paul, M. Reddy, J. Yen, M. Pfaff, C. DeFlitch, R-CAST-MED: applying intelligent agents to support emergency medical decision making teams, in: Proc. of the 11th Conference on Arti<sup>fi</sup>cial Intelligence in Medicine, Lecture Notes In Arti<sup>fi</sup>cial Intelligence, 4594, Springer, 2007, pp. 24–33.

![](/api/attachments/9FJRAZW7/fulltext/images/fa639f64b54eabc366f7e60b20acdd99f061b0cefa5ce550b84869482daa5b0c.jpg)  
Pari Delir Haghighi is a lecturer at Faculty of Information Technology, Monash University, Australia. She was awarded the PhD degree from Monash University in 2010. She graduat ed with Bachelor of Computing (Hons) with <sup>fi</sup>rst class honors. She received the Graduate Certi<sup>fi</sup>cate in Commercialization Research from Monash University. During her study, she has been awarded three scholarships including Monash Graduate Scholarship, Sir John Monash Deans scholar's award for Honors study, and Australian Postgraduate Award (APA). She has served as conferences program committee member, reviewer for journal articles and book chapters. Her current research interests include context-aware computing, decision support systems and emergency management. She is a member of DSSE (Distributed Systems and Software Engineering

Centre) and Knowledge Management (KM) research Program at Monash University.

![](/api/attachments/9FJRAZW7/fulltext/images/d59cb5026beb6ffa48da6711a26b0f35e488050153a35ea11f86eec242f245e7.jpg)

Frada Burstein is a Professor at Faculty of Information Technology, Monash University, Melbourne, Australia. At Monash University, Prof. Burstein initiated and continues to lead Knowledge Management Research Program, which comprises a virtual Knowledge Management Laboratory. She has been a Chief Investigator for a number of research projects supported by grants and scholarships from the Australian Research Council and industry, including two projects in emergency management decision support. Her current research interests include knowledge management technologies, intelligent decision support, mobile and real-time decision support, and health informatics. Her work appears in journals such as Decision Support Systems, Journal of Organizational Computing and Electronic Commerce, Journal of the American Society for Information Science and Technology, Information Technology & People, European Journal of Operations Research, and Knowledge Management Research and Practice. Prof. Burstein is an Area Editor for Decision Support Systems Journal and Co-Editor for Journal of Decision Systems and VINE: the journal of information and knowledge management systems. Prof. Burstein has been a guest editor of a few special issues of journals and collections of research papers. The most recent and substantial work was a set of two volumes of Handbook of Decision Support Systems, published by Springer.

![](/api/attachments/9FJRAZW7/fulltext/images/d7d36a4e5ff11b690cde2f02ea0db950af1820f1e0897e89431ce824a8f7fe7a.jpg)

![](/api/attachments/9FJRAZW7/fulltext/images/e1ec1dac0534a84248c453c006a22bfc2081fd0f05e22eb01c593f3ad4e6eaa4.jpg)

Arkady Zaslavsky is Science Leader at The Commonwealth Scienti<sup>fi</sup>c and Industrial Research Organisation (CSIRO), Australia. He received MSc in Applied Mathematic majoring in Computer Science from Tbilisi State University (Georgia, USSR) in 1976 and PhD in Computer Science from the Moscow Institute for Control Sciences (IPU-IAT), USSR Academy of Sciences in 1987. Prof. Zaslavsky has published more than 240 research publications through out his professional career. He organized and chaired many workshops and conferences in mobile computing area. He is an area editor for “Distributed databases” IEEE Computing-Online. His research interests include mobile and pervasive computing; distributed and mobile agents and objects; wireless networks; distributed computing and database systems; distributed object technology and mobile commerce. Prof. Zaslavsky has been awarded and involved in many research grants and projects including “M3: Enterprise Architecture for Mobile Computation”, “Context-rich mobile agent technology to support information needs of <sup>fi</sup>nancial institutions”, “Adaptive Distributed Information Services”, “Mobile City” and others. He is a member of ACM, IEEE Com puter and Communications Societies.

Paul Arbon is the Dean of the School of Nursing and Midwifery and Professor of Nursing (Population Health) Faculty of Health Sciences, Flinders University, Adelaide, South Australia He was awarded the Order of Australia (Member) for services to the community, particularly as Chief Commissioner of St John Ambulance Australia and for nursing and nursing research. Prof Arbon is the President of the World Association for Disaster and Emergency Medicine (WADEM). He is also the Director of Torrens Resilience Institute. His research interests include real-time surveillance, mass gathering health care, disaster medicine, triage education, the application of multi-casualty triage models at the scene of road traf<sup>fi</sup>c accidents, the use of <sup>fi</sup>rst aid during road traf<sup>fi</sup>c accidents, and volunteering in emergency and disaster management.
