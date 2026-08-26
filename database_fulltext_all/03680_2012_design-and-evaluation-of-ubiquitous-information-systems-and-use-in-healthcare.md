---
otero_id: 3680
otero_key: "ZW3U6AE8"
title: "Design and evaluation of Ubiquitous Information Systems and use in healthcare"
authors: "Wolfgang Maass; Upkar Varshney"
year: "2012"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2012.08.007"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Design and evaluation of Ubiquitous Information Systems and use in healthcare

Wolfgang Maass <sup>a,</sup>⁎, Upkar Varshney <sup>b</sup>

<sup>a</sup> Faculty of Law and Economics, Saarland University, P.O. 15 11 50, 66041 Saarbrücken, Germany

<sup>b</sup> Department of Computer Information Systems, Georgia State University, Atlanta GA 30302, USA

## a r t i c l e i n f o

Article history: Received 21 January 2011 Received in revised form 12 July 2012 Accepted 11 August 2012 Available online 23 August 2012

Keywords: Ubiquitous computing Design science Conceptual modeling Health information systems Semantic technologies

## a b s t r a c t

Designing Ubiquitous Information Systems (UIS) for supporting complex everyday situations requires extended design methods and models. To address this, we introduce design models as a special class of conceptual models that support design processes for IS in general and UIS in particular. Design models for UIS are concise abstract conceptual models of key situations that conceive social, informational, physical, and service properties as requirements for targeted Information Systems. In this paper, we show how design models can be derived from narratives of key situations, guided by information systems ontologies, and domain speci<sup>fi</sup>c input theories. This conceptual level offers an innovative approach for designing Ubiquitous Information Systems (UIS) in general and Healthcare Ubiquitous Information Systems (H-UIS) in particular. The proposed design approach is applied for developing H-UIS for reducing Adverse Drug Events (ADEs) by improving the communications between patients and healthcare professionals. Using the domain speci<sup>fi</sup>c input theory of Health Promotion Model (HPM), the modeling guidelines for design models are generated and utilized in the development of a H-UIS to avoid ADEs. The H-UIS improves several processes involving information technologies for healthcare professionals. The system is empirically evaluated and results show high level of interest among users and initial positive adoption effects. Open issues and future research opportunities are also presented at the end.

© 2012 Elsevier B.V. All rights reserved.

## 1. Introduction

Digital environments are increasingly embedded into everyday environments by computing technologies and thus utilize users in a wide range of activities [124]. Sensors and actuators are embedded into physical environments and various user devices. All these entities are connected with digital services that, in turn, are interconnected via digital networks. Hence, the traditional view of Information Systems as digital systems that interact with users via solitary devices in localized environments is extended by an understanding that Information Systems and physical environments can become indistinguishable [121,124]. Bodily, physical, and extended individual and social experiences become important elements when designing this class of so-called Ubiquitous Information Systems (UIS) [124]. In general, UIS consist of a set of artifacts that can dynamically change their con<sup>fi</sup>gurations according to contextual changes and user behavior. UIS provide means for supporting single actors and groups in real-world situations by services over ubiquitous computing technologies anywhere and anytime [64,124]. Little research has been done so far on dedicated design methodologies and conceptual modeling for UIS [41,50]. Hence, IS researchers claim a lack of knowledge about designing UIS [64,65,114].

The idea of design requirements has changed from single, static and <sup>fi</sup>xed-point statements of desirable system properties into dynamic and evolving rationales that mediate dynamic changes between business and everyday-life environments and design and implementation worlds [43]. Designing UIS differs from traditional IS because they are required to anticipate a wider range of situations in everyday lives. Situations of future use are only partially accessible in the current world but are conceived during design phases by anticipation and envisioning, supported by approaches such as scenario planning [115,116]. Coming from usability research and design theories on affordances, it is proposed that designing UIS should particularly consider attributes such as personalization, interaction, intuition, attractiveness, and sociality instead of focusing on functionalities only [114]. The complexity of designing UIS results from underspeci<sup>fi</sup>ed usage situations accompanied by multi-perspectivity and multi-disciplinarity of design team members. Following scenario-based approaches [43], complexity can be reduced if design descriptions are rendered in local concepts familiar to stakeholders and by scenarios as an effective means for conceiving, evaluating and re<sup>fi</sup>ning design descriptions with increased complexity [14].

We investigate design models as concise conceptual models for UIS that conceive social, informational, physical, and service properties as requirements for targeted UIS. Design models help designers to focus on key elements based on underlying information system ontologies. Thus design models provide a conceptual language that is grounded in basic conceptualizations of Information Systems. This conceptual level offers an innovative approach for building UIS in general and UIS for the healthcare domain (H-UIS) in particular. The goal of design models is to support mixed design groups with a general language that supports more ef<sup>fi</sup>cient UIS design processes.

In this paper we propose a design method that combines situationbased design models with diagrammatic design models. Situationbased design models draw from screenplays and scenario-based software development approaches and are described by text-based narratives. Diagrammatic design models are derived from narratives by extracting and interrelating key conceptual entities. This extraction process is guided by information system ontologies and domain ontologies. Both design model types keep a holistic view of healthcare situations as a means for clear design pathways [93].

We apply this process with design models to the design and development of UIS for reducing Adverse Drug Events (ADEs) by improving the communications between patient and healthcare professionals. Using domain speci<sup>fi</sup>c input theory of Health Promotion Model (HPM) [89], the modeling guidelines for design models are generated and utilized in the development of a H-UIS to avoid ADEs. It is shown that the proposed design model can be used to build an H-UIS based on Ubiquitous Computing technologies, Semantic Technologies, Mobile Communication technologies and service-oriented architectures that provide a sound foundation for building innovative but also robust infrastructures for distributed real-world healthcare environments.

The designed H-UIS leads to the improvement of several IT-processes for healthcare professionals. The system is empirically evaluated and results show very high level of interest among users. H-UIS can lead to considerable savings in healthcare costs as increased medication adherence leads to better health outcomes, reduced number of hospitalizations, and reduced co-morbidities for patients. The H-UIS can also facilitate the implementation of one or more interventions, including context-sensitive reminders, for improving medication adherence in the future.

By focusing on outpatient healthcare environments, this paper looks into improving several processes involving information technologies for healthcare professionals. How our exempli<sup>fi</sup>cation by medication situations for outpatients can be transferred to other healthcare situations is discussed at the end of this article. In this paper, we introduce structures that support designers in incremental design of UIS within the healthcare domain. More speci<sup>fi</sup>cally, the contributions are:

• A situation-based design model for Ubiquitous Information Systems

• A two-step approach that combines narrative and diagrammatic design models

• An application of design process for a speci<sup>fi</sup>c outpatient situation to improve communications between patient and healthcare professionals

• A research roadmap for H-UIS

## 2. Designing Ubiquitous Information Systems

Design research investigates prescriptive methods and formalisms for crafting innovative Information Systems that provide utility to a social context [32,36,68,69,117]. A design model as a central element of any design theory “is a set of propositions or statements expressing relationships among constructs” [68]. These provide a basic language which is used for characterization of tasks, situations, or artifacts [68]. On one hand design models based on Natural Language can be used in mixed design teams but suffer from their inherent ambiguity while on the other hand formal mathematical representations provide excellent precision but require extensive training of designers.

## 2.1. Design model

From a knowledge perspective, designers and domain experts use design models for making their inner models and design knowledge explicit by formal, semi-formal, or qualitative languages so that these can be shared, discussed, and used for creating artifacts [80]. A general goal is that artifacts created by design models will have some inherent qualities outsmarting any randomly created artifacts. Design models are constrained by requirements including input theories (domain theories and kernel theories) and user requirements [69,117].

The principles that govern design development processes of a system are best-practice rules. They guide designer's behavior and constrain the design space. Design guidelines can span areas such as selection criteria, knowledge sharing, functional requirements, social dynamics, and artifact architecture [69]. Principles governing the design of a system encompass meta-designs [117], that provide vocabularies for describing design models [68], and hypotheses on artifacts (design model and implementation) [63]. In IS research, design vocabularies have been investigated within the context of design models [118] whereas hypotheses on artifacts are mainly related to implementations, e.g., [19,22,76].

Principles governing the development process encompass design methods and testable design process hypotheses. These guiding principles capture the know-how on the design of artifacts for a speci<sup>fi</sup>c class of Information Systems [69]. Design models are condensations of individual mental representations structured by entities and relations [119]. Thus, they are conceptual descriptions of Information Systems, provide architectures for compound social and technical systems [24], and are described by vocabularies and ontologies of various input theories [118].

Artifacts are implementations of design models into appropriate carrier matter. If a design model is not explicitly provided, the creator of an artifact uses an implicit design model or creates artifacts at random as instances of the whole design space. In an extension to the evaluation of design models, implementations are evaluated against models, dimensions and metrics, which have been de<sup>fi</sup>ned in corresponding models and theories (e.g., [19,22,113]). These evaluations are sample tests that provide item-based and limited type-based information about the quality of a design model and processes for implementation.

## 2.2. Abstract Information System Model

Silver et al. [69] distinguish conceptualizations of IS by three categories: (1) people, (2) organizations, and (3) existing or planned technologies. Additional concepts for design models are roles [70], goals [101], expertise [79], characteristics of users and social systems [16,63], business needs based on strategies [36], structure [16,36], culture [16,63], and existing business processes [56]. For example, structured conceptualizations are given by reference models, speci<sup>fi</sup>cation documents, and ontologies (glossary, thesaurus, class hierarchy, and axiomatic theory) [29]. The central concepts of IS design models are: (1) business community, (2) processes, (3) services, and (4) infrastructures [61]. The conceptualizations of Information Systems provide a language by which design models can be conceived, discussed, and described [68].

Various relations are de<sup>fi</sup>ned between concepts of a design model [69,119]. The meaning of concepts and relations of design models is described by shared vocabularies [68]. Shared vocabularies are either implicitly de<sup>fi</sup>ned as being part of a mutual understanding in a design community or explicitly de<sup>fi</sup>ned in forms of machine-processable representations [15]. In the latter case, the logic of a design model can be evaluated and matched with other design models which is important for re-using a design model for other Information Systems [92]. Depending on underlying infrastructures IS design models have different implementations. In this sense, an IS design model is a class description of a set of IS artifacts and an abstraction from underlying layers that could themselves be described by design models, i.e. IS design models can build recursive structures.

In summary, Information Systems can be conceived as compounds of social systems, information spheres, and service systems that use information technology infrastructures for realization of desired situations [58,61,83]. In extension to Information Systems that mainly consider processing of information objects, design models for Ubiquitous Information Systems (UIS) also need means for representing physical entities. Hence, design models for UIS require conceptual descriptions of physical objects that can be related to one another and to other conceptual elements of a design model.

With the Abstract Information System Model (AISM), we propose four conceptual classes that characterize key conceptual entities of UIS (cf. Fig. 1):

1) Social system: the set of roles available with a set of attributes, such as rights, obligations, and prohibitions, interactions that support some tasks, and goals

2) Information sphere: the set of information objects used within the realm of an UIS

3) Service system: the set of all digital and physical services available within all situations in which an UIS can be used

4) Physical object system: the set of physical entities available within all situations in which an UIS can be used

## 2.2.1. Social system

According to theories from social sciences, actors in social systems take roles and interact with one another according to implicitly or explicitly de<sup>fi</sup>ned protocols [31,73]. Roles frame the rights, obligations, prohibitions, and goals of actors that can be taken by these roles. Interactions are supported by services provided by a service system. According to Social Interactionism, the interactions are embedded into language processes and symbol systems that de<sup>fi</sup>ne meanings of exchanged information [73]. Information objects that are used in situations by the social system of role-taking actors are de<sup>fi</sup>ned within an information sphere based on supporting services. Actors use roles, information objects, and services for implementing situations in work and other contexts. But an organization also consists of structural elements, in particular role systems that describe the capabilities of roles and attributes, and dynamic structures based on interactions that describe procedural aspects of an organization. Well-established interactions can be explicitly de<sup>fi</sup>ned by communication protocols (e.g., [107]). Sets of social systems, service systems and information spheres are basic conceptual dimensions of IS design models.

The social system of a design model has roles that can be taken by individuals on instance level. Roles are speci<sup>fi</sup>ed by properties on associated rights, obligations, and prohibitions that relate a role to other entities. Roles are socially constructed, i.e. a community agrees on certain roles [98]. Role-taking actors are required to comply with properties associated to a role. Interactions with other entities are generally governed by role properties. Any type of relations between roles is acceptable that is de<sup>fi</sup>ned by an underlying organizational theory or background knowledge. Relations have different types, such as power relations, interactions, and formal relations. For example, in the healthcare domain power relations between patients and physicians are given by implicit social norms, e.g., a principal–agent relation that out<sup>fi</sup>ts a physician with normative knowledge and establishes an asymmetric knowledge relationship toward a patient. Interactions are explications of task requirements that are described by directed relations between roles. For instance, a physician directs a patient to follow a certain medical procedure.

![](/api/attachments/ZW3U6AE8/fulltext/images/2c2813386ad0c2895973a736ee60235c0764170e541b24c1778ef6444f6b5809.jpg)  
Fig. 1. Abstract Information System Model (AISM).

## 2.2.2. Information sphere

The core conceptual entities of the information sphere are information objects. These are abstract conceptualizations of any kind of content, such as speech, written language, graphics, or digital contents. Information objects are realized by content objects that are themselves part of underlying realization infrastructures. Information objects can be any kind of information that actors perceive as being coherent in a situation. For example, physicians and patients perceive a prescription as a coherent information object within a consultation situation. Information objects might recursively consist of additional <sup>fi</sup>ner grained information objects. For instance, prescriptions might consist of several drugs and descriptions of healthcare procedures. In a drugstore situation a patient might use this level of detail for communication with a pharmacist. Hence, how an information object is framed depends on the social system, background knowledge, experience and other kinds of contextual factors.

Relations between information objects are de<sup>fi</sup>ned within the domain and are generally agreed within a community. For instance, fundamental relations are part-of or is-subclass-of but also additional relations, e.g., pictorially-describes, if a pictorial information object will be added to a textual information object.

Information objects always require support given by a role-taking actor or a service. In the <sup>fi</sup>rst case, a role-taking actor creates an information object by virtue of his/her human capacity, such as speech, gesture, mimics, or posture that does not require any external service. In the other case, external services can create information objects and make them available to other services or role-taking actors.

## 2.2.3. Service system

Services provide functional capabilities to roles and other services. Services that support roles are interface services. These are used by role-taking actors for achieving situation-speci<sup>fi</sup>c goals. With respect to communication, interface services support the exchange of information objects among role-taking actors. Internal services are opaque within a situation and can only be used indirectly via interface services. This allows <sup>fi</sup>ne-grained descriptions of service systems. Role-taking actors can either use interface services for performing a speci<sup>fi</sup>c task that does not require interaction with other role-taking actors or interface service support interactions with other role-taking actors. For instance, if a physician stores information about a patient, the task is to use an interface service without interaction with other roles. Instead if a physician wants to inform a patient to visit him, she might use an interface service that allows her to get in contact with the patient, such as a telephone service or SMS.

The relations among services can be manifold as well. Most importantly, services have functional relations that describe how services can be evoked by other services and which functions and data structures shall be implemented.

## 2.2.4. Physical object system

Mobile, pervasive, and ubiquitous computing [64,81,112,121] are approaches by which Information Systems (a) extend from spatially restricted access to information spheres to temporally and spatially unrestricted access forms and (b) dissolution of information technologies in physical environments. Information needs are supported everywhere at any time by natural and adaptive means without bothering about underlying technologies. For instance, RFID-based IS started with the information need of logistic managers to track and trace physical objects [81]. Therefore unambiguous relationships were speci<sup>fi</sup>ed and realized by supporting infrastructures, including RFID technologies [27,120].

The physical object system encompasses physical objects that are relevant for the design model of an Information System. Any of those physical objects have at least one relationship with an information object, role, or service. The relationships between physical objects and information objects explicitly materialize interpretations as discussed in reference semantics [105]. This also means that information objects can subsequently be enriched on demand by further analysis of physical objects.

## 2.3. Realization system

The four subsystems of the design model, namely social system, information sphere, physical object system, and service system are de<sup>fi</sup>ned on a conceptual level. Information systems and physical object systems are implemented on infrastructures that <sup>fi</sup>t to requirements of social systems, information spheres, and service systems and their relations. Hence, these three systems pose constraints on realizing infrastructures. Information objects are realized by content objects in speci<sup>fi</sup>c formats, roles are taken by entities, and services are implemented by infrastructures that can realize functional behavior of interface services and internal services.

## 2.4. Informal and diagrammatic design models

Narratives are a qualitative means for describing situations with “clear (but always temporary) boundaries around actors, actions, belief systems, language practices or imagery, and social formations” [51]. During requirements elicitation narratives are an effective means with low formality for developing a common understanding and reduce ambiguity at an early stage of an IS design process [10,57,106]. Narratives are de<sup>fi</sup>ned on instance level and provide descriptions of prototypical situations. They support narrative thinking [57] and, thus, mutual understanding of different perspectives with respect to contexts, interactions, social structures, services, physical and informational objects as part of a collaborative sense-making process [38].

The hypothesis is that story-like design models provide a spectrum that support different mental models used during design tasks and thus improve design task ef<sup>fi</sup>ciencies by, for instance, reduction of cognitive load [57]. This argument is grounded in a long-standing argument in Cognitive Science whether cognitive representations resemble images [54] or propositional representations [45] and whether both representation are antithetical or complementary. The mode of narrative thinking is highly context-sensitive, anchored in situations, articulated in temporal sequences, around individual and group intentions and actions [125]. The narratives can be de<sup>fi</sup>ned as discourses with a clear sequential order that connect events in a meaningful way for a de<sup>fi</sup>nite audience and thus offer insights about the world and/or people's experiences [37].

Narrative-based design models are an easy-to-use means for understanding target usage situations of complex UIS. Derived from perspective approaches [38] and scenario-based approaches [13,42], narrative-based descriptions of situations help to capture design models in multi-disciplinary IS design teams (as an example cf. [38]). Situations are instance-based descriptions of interactions between entities in an environment anchored in underlying ontologies. Guided by the AISM ontology, situations are described by role-taking individuals that intend to achieve certain goals by interacting with other roletaking actors, supported by service systems, and use of information objects and physical objects.

## 2.5. Derivation of diagrammatic design models from narratives

In our proposed design method, situations are described by narratives at the beginning and are subsequently translated into diagrammatic design models. Finally, diagrammatic design models are used as basis for the technical realization of the UIS. By means of a general IS theory (here AISM) and a domain theory diagrammatic design models are deduced from narratives by extracting and interrelating key concepts. Each narrative is analyzed with respect to key AISM categories. Agents take speci<sup>fi</sup>c roles within a situation. Services provide information that can be used by agents. Agents and services have speci<sup>fi</sup>c intentions to participate in a situation. Information objects have several realizations, e.g., image, text, video. Physical objects are used for services they provide. Interactions take place between service and service, service and agent as well as agent and agent in a situation. By doing this, entities in situations are abstracted into categories. For each term competency questions [33] are derived that support subsequent validation of design models.

In the following, it is shown how this design approach is applied to an example from the Healthcare domain. According to design science theories, IS designs are guided by kernel theories. Therefore, the Health Promotion Model is introduced at the beginning before it is applied to the design of a Healthcare Ubiquitous Information System (H-UIS).

## 3. Application of the design model to the healthcare domain

In the following, the proposed design model is utilized and anchored in a kernel theory from the healthcare domain.

## 3.1. General user requirements derived from the Health Promotion Model

Healthy behavior may be motivated by an individual's desire to protect health by avoiding illness or a desire to increase one's level of health in either the presence or absence of illness [89]. More specifically, Health Promotion is directed toward increasing the level of well-being and self-actualization of a given individual or a group of individuals. Health Promotion focuses on efforts to approach or move toward a positive valance state of high-level health and wellbeing [89].

The examples could include increased physical exercise, improved nutrition, use of hearing protection devices, weight-loss, increasing use of helmet for bicyclists, and increased adherence to medications and health advice. The most concise kernel theory for healthcare applications with focus on health promotion is the Health Promotion Model (HPM) proposed by Nora Pender [89] (cf. Fig. 2).

Health promoting behavior is the desired behavioral outcome and is the end point in the model. Health promoting behaviors should result in improved health, enhanced functional ability and better quality of life at all stages of development. The <sup>fi</sup>nal behavioral demand is also in<sup>fl</sup>uenced by the immediate competing demand and preferences, which can derail well-intended health promoting actions. Several meta-requirements are given by the HPM that constrain the design space of a Health Promotion IS. These are expressed as follows.

From the HPM we have derived <sup>fi</sup>ve key factors that are directly related to the design of H-UIS: (1) situational in<sup>fl</sup>uences, (2) reduction of perceived barriers to action, (3) perceived bene<sup>fi</sup>ts, (4) interpersonal in<sup>fl</sup>uences, and (5) perceived self ef<sup>fi</sup>cacy [89]

1. Situational in<sup>fl</sup>uences, including the environments that are fascinating and interesting, will lead to health promoting behavior as shown in [71] where situational in<sup>fl</sup>uences are shown by statistically signif icant predictors of use of hearing protectors for farmers. Therefore, interesting, usable and reliable artifact and related infrastructure will improve health-promoting behavior in H-UIS.

2. Any reduction in perceived barriers improves health promoting behavior [89]. The perceived barriers, especially structural barriers, are shown to be highly signi<sup>fi</sup>cant in elderly women [62]. In H-UIS, improved packaging and detailed information on various healthcare conditions along with simple interaction with health environment will reduce perceived barriers for patients. The artifact information/ cognitive overload will increase barriers for patients and thus negatively affect health promoting behavior. Therefore the designed system, and more speci<sup>fi</sup>cally device-user interface, should not lead to such overload.

3. The perceived bene<sup>fi</sup>ts are shown to be signi<sup>fi</sup>cant in various health actions, such as use of hearing protection [48]. Healthcare environment should in<sup>fl</sup>uence “perceived bene<sup>fi</sup>ts” for the patient, such as those by positive reinforcement in the form of external prompts on health bene<sup>fi</sup>ts.

4. The interpersonal in<sup>fl</sup>uences lead to a higher level of health promoting behavior as shown by [123]. Thus, H-UIS should facilitate suitable reminders/alerts for patients from family, caregivers, and automated systems.

5. The perceived self-ef<sup>fi</sup>cacy has been shown to be a strong predictor of healthy behavior such as exercise for even trained healthcare professionals [90]. In H-UIS, the system should promote perceived self-ef<sup>fi</sup>cacy for the patient. This could be done by showing that the patient knows how to use the system and/or showing a demo of actual use by others.

Next, a speci<sup>fi</sup>c health problem, i.e. Adverse Drug Events, is described that sets the context for designing an UIS by following the previously proposed design model.

## 3.2. Designing a H-UIS for avoiding Adverse Drug Events

The cost for prescription medications is a major component of healthcare expenses as the US alone utilizes 3 billion prescriptions a year. However, the non-adherence to these medications further leads to more than \$90 billion in avoidable hospitalization and procedures every year [77]. Additionally, people who miss their doses are three times more likely to see doctors again, resulting in further increase in healthcare expenses. Also, the medication errors in the US lead to 1.5 million Adverse Drug Events (ADE) (aka Adverse Drug Reactions) caused by errors in prescribing or taking medicine [6]. For the US, more than 1 million outpatients, i.e., patients who are not hospitalized overnight, experienced an ADE that required admission to the hospital and 4.7% of admissions were caused by drugs [60]. Patel et al. found for the UK that between 1998 and 2005, a total of 447,071 ADE representing 0.50% of total hospital episodes occurred with an increase by 45% over this period [87]. In the US and UK, ADE are also one of the leading causes of death [40,60]. Many examples include a dramatic incident in which several medication errors led to the death of a baby [78].

Medications and related problems can be subsumed by the following categories [7,11,47] (we use terms “medications” and “drugs” interchangeably):

## 1. Functional problems

a. Incorrect medication: poor packaging, resulting in incorrect use or an incorrect dose

b. The “estimated” expiry date, where an actual early expiry affects the treatment negatively and an actual late expiry does not bene<sup>fi</sup>t anyone.

c. Limited medication adherence leading to delayed recovery and or increased hospitalization

d. Dif<sup>fi</sup>culty in verifying authenticity/originality of some medications e. Negative side effects, medication errors, and allergies

f. Misplacement (or loss) of drugs in a shop, hospitals, or homes g. Lack of reusability/recyclability and the amount of trash generated by medications

2. Relational problems

a. High cost, lack of generic products for most new and expensive medications and products

3. Information over<sup>fl</sup>ow problems

a. The large number of manufactures producing drugs and medications

ADE includes both preventable errors and side effects that must be managed. Table 1 shows both of these along with multiple possibilities of preventable errors [4].

The majority of the preventable errors can be addressed by technologies. More speci<sup>fi</sup>cally, dose error, frequency, and missed dose can be addressed by automated systems. The wrong drug/patient combination is unlikely to occur in outpatient setting, which focuses on only one patient. The current practice is to address medication errors primarily by using technologies. For example, Information Systems for ADE detection and alert for hospitalized patients have been implemented (e.g., [72,94]). Additionally ADEs can be reduced by automated drug dispensing devices [78]. Beside automated monitoring and alarming, the importance of communication between role-taking actors in medical situations is largely neglected [78,87]. Gandhi et al. indicate that lack of communications between patients and physicians on drug complications results in uncertainty and dissatisfaction of patients [11]. The Health Promotion Model (Fig. 2) argues that better communication between patients and medical personnel supports patients' learning effects with medication activities, self-ef<sup>fi</sup>cacy, self-actualization, and <sup>fi</sup>nally higher levels of well-being [89]. Therefore, many of the problems with medications, including ADEs, can be avoided or better managed by improving the communications between patient and healthcare professionals. More speci<sup>fi</sup>cally, several factors involved in ADE (Table 1) including known allergy, route error, known drug-drug interactions can be prevented and if ADE occurs, it can be managed better by improved communications between the patient and healthcare professionals. Pervasive and ubiquitous technologies can very naturally play a major role to support and facilitate this communications [82,83]. This improved communications can also help in implementing one or more of several possible interventions to improve medication adherence [83]. In the following, we will address this lack of communication and describe how the proposed design process supports structured design, realization, and evaluation of a H-UIS. For this, an out-patient situation is used, in which a patient manages his/her medications on his/her own. More speci<sup>fi</sup>cally, this addresses prevention of ADEs caused by dose errors, frequency and missed medication. Although in general, improved communications can help preventing or responding to various factors that can cause ADE such as drug-drug interactions and unpredictable/ unknown side effects.

Table 1 Various causes of ADE.

<table><tr><td>ADE</td><td>Specific problem</td><td>Comments</td></tr><tr><td rowspan="7">Preventable errors</td><td>Dose error</td><td>When the amount of medication dispensed is more or less than the specified amount</td></tr><tr><td>Known allergy</td><td>When the patient has a known allergy</td></tr><tr><td>Wrong drug/patient</td><td>When multiple patients are in a care setting (not an issue with a single patient in independent living)</td></tr><tr><td>Route error</td><td>When the medication is dispensed using an incorrect route</td></tr><tr><td>Frequency</td><td>When the medication is dispensed more often or less often than prescribed</td></tr><tr><td>Missed dose</td><td>Part of the medication adherence problem</td></tr><tr><td>Known drug-drug interactions</td><td>When a medication interacts with other medications the patient is taking</td></tr><tr><td rowspan="2">Side effects</td><td>Unpredictable effects</td><td>Not any valid predictors of who will have ADE</td></tr><tr><td>Unknown effects</td><td>When a medication leads to effects that are not known (more likely for newer medications)</td></tr></table>

![](/api/attachments/ZW3U6AE8/fulltext/images/fce4c11dac15907fb5568d052f1b9b0abed1c4a180e43a83fc06ff4bf4c3f82f.jpg)  
Fig. 2. The (revised) Health Promotion Model (HPM).

## 3.3. Drugs in the context of E-health

E-health, or the application of information and communication technologies across the entire range of functions involved in the practice and delivery of healthcare, focuses on digitization of many healthcare processes and tasks [97,110]. E-health could lead to ef<sup>fi</sup>ciencies in healthcare delivery and management, improvement in the quality of healthcare, cost reduction, reduction in medical errors, and moving healthcare resources to the place of needs [52]. For homecare of outpatients, the goal is to create assistive environments for older and/or disabled people such as smart homes, which can sense themselves and their residents [52], e.g., by medication monitoring [26], smart beds [84,85], interactive mirrors [59], or even social-distant dining using immersive video [35]. These can also enact mappings between the physical world and remote monitoring and intervention services [1]. One requirement of such smart homes is a very high level of reliability and the ability to work even under failures of some components [110]. It should cause no harm to the resident and inform the caregivers about the conditions of the home.

Proactive health systems use data from multiple sources to supply individuals and communities with information that supports improvement of their state of health and avoidance of health risks [97]. Hence, modern healthcare aims at keeping people in healthy states or bringing people back to healthy states [28]. In future healthcare situations, computer-based medication ordering, automated drug retrieval, automated drug calculations, and risk-aware drugs are important features for H-UIS that help to reduce functional and relational, information over<sup>fl</sup>ow problems and overall costs [39,47].

The current drug-related information is static and is not able to consider context information about, for instance, state of patient's activities, high pulse rate, or status of a drug [75,109]. On the other hand, drugs are embedded into complex communication networks implemented by healthcare speci<sup>fi</sup>c situations (cf. Fig. 3). Generally a set of core situations exists between patients, physicians, nurses and drugs while other roles, such as a patient's employer and insurance company. Examples for core healthcare situations are consultations, seminars of pharmaceutical companies for physicians, or outpatient care (cf. Fig. 3). In the following, we look at H-UIS that support healthcare situations around outpatients. According to the proposed design process, we start with narratives that were developed with medical experts in the US and Europe.

## 3.4. Narrative “Medication Alert”

The following narrative was derived from discussions with medical experts. Paul/Nancy has been suffering from minor health problems for some time. The physician has prescribed two drugs A and B, which are not co-dependent implying either can be consumed independent of the other. Drug A must be taken as two pills three times a day. Drug B must be taken three pills two times a day. Every week Erica, an independent nurse, visits Paul/Nancy to check on medication compliance and any other problems. The alert situation is described as follows. It is Tuesday noon and Paul/Nancy has taken two pills of drug B out of a blister. The nurse receives an instant message and an alert service automatically rings Paul/Nancy by phone. By using Erica's voice the message service gives Paul/Nancy the information not to take any more dose of drug B at noon but take one pill in the evening. Next we describe how this narrative was analyzed and translated into a diagrammatic representation. A role-based design approach is utilized, i.e., creation and manipulation of information objects can only be performed by role-taking actors or role-taking services. During this step several design decisions are made, such as introducing additional roles and associated role-taking services.

![](/api/attachments/ZW3U6AE8/fulltext/images/243330d0d9df26ac842eb2ea508a0f0c2707baca284b2e88506072f82863ffa5.jpg)  
Fig. 3. Main roles in exemplary healthcare situations.

## 3.5. Extraction of terms and assignment to categories

## 3.5.1. Social System Design

Two roles are immediately visible, i.e., a patient and a nurse (cf. Fig. 4). The discussions with medical experts and patients reveal the requirement for several other roles. First there is a need for an alert manager that triggers communication with the nurse and the patient. The communication with the person is required to be personalized by the nurse's voice. Therefore a “virtual nurse” role is required as well. The whole situation starts with taking two pills from a blister. This requires a role that is connected to the blister and is allowed to initiate alerts. For this, an alert trigger role is introduced. The interactions between these roles follow the situational description, i.e., after taking a wrong medication the alert trigger role creates an alert and sends it to the alert manager. The alert manager informs the nurse about this alert and sends this alert to the virtual nurse role. The virtual nurse creates a personalized advice information object and informs the patient accordingly.

## 3.5.2. Service system design

All roles that are not taken by humans are linked to services. These roles add rights and identities to service actions. For instance, if an alert is created with the help of the blister service the alert trigger role is linked as the responsible role for this alert and provides credentials on the creation activity (cf. Fig. 4).

## 3.5.3. Physical object system design

The integration of tangible objects with digital entities is an essential feature of UIS. In the medication alert situations, a blister is used by a role-taking actor but it is also linked to a dedicated service (blister service) that supports the patient's activity (cf. Fig. 4).

## 3.5.4. Information sphere design

In this narrative, only two information objects are key to the medication alert situation, i.e., alerts and advices. An alert is created by an alert trigger role and used within various interactions among roles (cf. Fig. 4). The advice is created by the virtual nurse role and subsequently used for communication with the patient. Supporting information objects are described in more detailed representations. For example, a personalized verbal advice requires processing of the advice based on a digital phonetic representation of Erica's voice that results in an audio information object. By careful analysis of this sub-situation, the design model logic can be reapplied on a more detailed level as well.

![](/api/attachments/ZW3U6AE8/fulltext/images/31c711e05264817cc439cca62c51964d4b87ee4c33efa62e6199537a09e1a25f.jpg)  
Fig. 4. Diagrammatic design model for the “medication alarm” situation

## 3.6. Realization

Next we describe how this design model (cf. Fig. 4) has been realized by a technical infrastructure using multiple technologies including semantic technologies and web infrastructures. The realization of the prototypical H-UIS (cf. Fig. 5) was build on top of a semantic middleware, which is based on the OSGi middleware architecture and uses semantic technologies, RFID and barcode technologies (two-dimensional barcodes, i.e., QR tags, and one-dimensional barcodes) [66]. In this application, each drug blister is equipped with a QR tag. For each pill, the patient takes from a blister, he/she places this blister on an infrared QR reader plate. The same holds for the alert service and the advice service. The interactions between these services are realized by bundleto-bundle communication within the OSGi run-time environment. The interaction with the nurse is realized by a SMS gateway within the alert service and in parallel by an application on an Android mobile phone (cf. Fig. 5). Verbal advices are preprocessed and can be accessed by the advice service from a database. Because a telephone gateway was not feasible, we also implemented the interaction to the patient by an application on an Android mobile phone. Thus the design model for the alert situation has been fully implemented on a semantic technology middleware. The mobile application has been implemented in Java (JVM implemented by the Dalvik Virtual Machine) on the Android platform (Open Handset Alliance) based on Linux Kernel 2.6. Basic client– server communication uses HTTP while high-level communication is based on the SPARQL-based protocol.

## 4. Empirical evaluation

Following design science methodologies [36,68,69], we conducted an empirical technology adoption study with the goal to investigate whether this H-UIS design <sup>fi</sup>ts functional and emotional needs of patients in principle. Change requests resulting from this study are fed back into earlier design models and subsequently into technical realizations and organizational implementations. Here, we use HPM as kernel theory that provides guidelines on various in<sup>fl</sup>uences on patient health-related behavior. Technology adoption theories are used as a <sup>fi</sup>rst approximation for evaluating an early design study of a H-UIS. Our primary focus is on HPM constructs that conceive patient perceptions, i.e. “perceived bene<sup>fi</sup>ts, barrier, and self-ef<sup>fi</sup>cacy” and “interpersonal and situational in<sup>fl</sup>uences” because these causally in<sup>fl</sup>uence commitments and health promotion behavior (cf. [89]).

Next we map the <sup>fi</sup>ve factors derived from the HPM (cf. section 5.2) onto a general technology adoption model derived from Innovation Diffusion Theory (IDT) [96], Technology Acceptance Model (TAM) [19], and Theory of Planned Behavior (TPB) [2]. This provides a wellestablished, proximate model for empirical evaluation of our H-UIS prototype. Three constructs from these theories are adequate to be utilized in our model. The <sup>fi</sup>rst construct is perceived ease of use (PEU), which refers to the degree “to which a person believes that using a particular system would be free of effort” [19]. Here, the H-UIS represents the system and supports the medication of a patient. The second construct represents perceived usefulness (PU), which is de<sup>fi</sup>ned as “the degree to which a person believes that using a particular system would enhance his or her job performance” [19]. In our context, PU refers to the degree to which a patient believes that using an H-UIS would enhance his or her performance regarding correct medication. A third construct relevant to the current work is perceived enjoyment (PEN). It is de<sup>fi</sup>ned as the extent to which the activity of using a H-UIS “is perceived enjoyable in its own right, apart from any performance consequences that may be anticipated” [21]. Accordingly, it is assumed that each successful H-UIS should share characteristics of hedonic Information Systems [108].

In our model it is assumed that situational in<sup>fl</sup>uence is directly related to PEN of a H-UIS because PEN supports analysis of a user's perception of a technology in a situation independent of its effects or functions [21]. Reduction of perceived barriers to action is supposed to directly relate to PU and PEU because if a H-UIS is perceived as being useful and easy to use it will reduce barriers to enact it with respect to health-related activities [19]. Perceived bene<sup>fi</sup>ts are result-oriented in the sense of a cause-effect relationship, i.e. if a health-related behavior is adopted it will result in particular bene<sup>fi</sup>ts. Because we want to test whether a H-UIS is perceived as being supportive for achieving a certain health-related goal, we argue that perceived bene<sup>fi</sup>ts could be measured by the behavioral intention to use a H-UIS. Following TAM, PEU is found to have mediated and direct effects on behavioral intentions, IU, while PU deploys direct effects [20]. PEN, as a non-utilitarian but hedonic latent variable has been also found to show direct effects on behavioral intentions [46]. For entertainment media it was also found that PEU might have signi<sup>fi</sup>cant relations with PEN [108]. This relationship might be less developed for H-UIS because they are less entertaining and are used in serious situations resulting in a stronger utility character.

![](/api/attachments/ZW3U6AE8/fulltext/images/993c55a54968e193e5114f532f91ee4f8bd489900be8f37f9fc88431054092ff.jpg)  
Fig. 5. Implementation of the combined “Medication Alarm” and “Additional Information” situations.

The situation described by the narrative (cf. Fig. 4) poses a situation of interpersonal communication. As a proximate measurement we mapped interpersonal in<sup>fl</sup>uences on PEN and PU because PEN measures the perception of this interpersonal H-UIS-supported situation as such while PU measures how a patient perceives the utilitarian aspect of this H-UIS-supported situation. This model does not explicitly measure a patient's self ef<sup>fi</sup>cacy because we assume that this requires interactions with the H-UIS over a longer period of time. Nonetheless it can be argued that all four constructs (PU, PEU, PEN, and IU) are proximate indicators for a patient's perceived self-ef<sup>fi</sup>cacy. This integration of the HPM kernel theory into design and empirical evaluation of the resulting H-UIS requires more detailed analysis in the future but we assume that it serves our goal to see whether HPM can inform designers of H-UIS and how it can be measured by means of well-established instruments of innovation research.

Consistent with TPB, TAM and theories on enjoyment [46,108], we hypothesize therefore the following relationships:

H1. PEU of the H-UIS has a positive relation with (a) PU, (b) IU for medication support, and (c) PEN.

H2. PU of the H-UIS has a positive relation with IU for medication support.

H3. PEN of the H-UIS has a positive relation with IU for medication support.

## 5. Method

In order to test the research model, we equipped a laboratory with the H-UIS and conducted an experiment. In the following, a detailed description of this experiment is presented. The sampling procedure was as follows. We e-mailed invitation letters to undergraduate students from a technical university. In this invitation, the experiment was promoted by claiming that each participant will receive \$8. Further, it contained a link to a website, on which the students were able to register for the experiment by choosing one out of 60 time slots.

In the <sup>fi</sup>rst part of the experiment, the H-UIS was shown to subjects and they could test its basic functionality guided by a supervisor. After this introductory brie<sup>fi</sup>ng each subject read the description of the targeted situation (cf. Section 6.2). Then the subjects were told to put themselves into Paul's (male subjects) or Nancy's (female subjects) perspective and to use the H-UIS accordingly. Each subject was given 10 minutes for taking the patient role in this healthcare situation and she or he was allowed to ask the supervisor to clarify any open issues on how to use the H-UIS.

Then in a fourth step, subjects were given a questionnaire with items regarding the perceived characteristics PEU, PU, and PEN that were adapted from existing scales [46]. The numbers of items per scale were reduced to one for PU and PEN. For PU it was found that ef<sup>fi</sup>cient acquisition of information and pure provision of information is not perceived as being indicative for perceived usefulness of a H-UIS. Therefore PU is measured by an item targeting perceived usefulness (6th item on PU [19]) (cf. Table 1). In previous studies, items are used for PEN that only remotely target enjoyment and hedonic characteristics, e.g., interest [55,108]. Hence we reduced the scale for PEN to one item as well (4th item on PEN in [55]) (cf. Table 1). On one hand, reduction to single-item scales reduces reliability while on the other hand construct validity for unidimensional re<sup>fl</sup>ective indicators are not affected, such as attitudes [44]. Reliable single-item scales are used in the healthcare domain when multi-item scales are lengthy, expensive, and burdensome to collect [23]. Furthermore, a wellestablished single-item scale was used to measure behavioral intention (IU) [21]. According to Ajzen and Fishbein [3], this construct covers the three behavioral elements action (usage), target (H-UIS) and context (information for medication support) as can be seen in Table 2. All items were based on seven-point Likert scales, ranging from extremely disagree (1) to extremely agree (7) with the neutral value of 4. At last, the questionnaire was used to collect demographic data and to ask for the length of the experiment and the comprehensibility of the instructions.

## 6. Results

Forty male and eleven female subjects participated in the lab experiment. Their age ranged from 20 to 24 (n=32) and from 25 to 29 (n=16) with 3 providing no answer on the age question. The instructions of the experiment and the questionnaire were perceived as being reasonable (Mean=5.61; SD=1.32) and acceptable on its length $( \mathrm { M e a n } { = } 5 . 0 8 ; \mathrm { S D } { = } 1 . 8 3 )$ ).

Consistent with prior research [46,53], partial least squares (PLS) method was used for the data analysis of our research model. PLS belonging to structural equation modeling (SEM) was chosen over regression analysis, because SEM can analyze all of the paths in one analysis [8,30]. PLS allows analyzing (1) the structural model for assessing the relationships among our theoretical constructs and (2) the measurement model for assessing the validity and reliability of our questionnaire items. In our research, all theoretical constructs were modeled as re<sup>fl</sup>ective because their questionnaire items are manifestations of them [30] and are expected to correlate with each other [17]. By using G\*Power3 [25], a sample size of 48 was calculated for three predictors (method: F-test, linear multiple regression – <sup>fi</sup>xed model, r<sup>2</sup> deviation from zero) which would be good enough to detect PLS path coef<sup>fi</sup>cients with medium to large effect sizes $( \mathsf { f } ^ { 2 } ) = . 2 5$ and error probability of 0.05). A statistical power of .80 (1-β error probability) was used, which is common in MIS research [9,18]. Thus, the total sample size of 51 subjects was suf<sup>fi</sup>cient for the lab experiment.

In order to test the validity of our constructs, a con<sup>fi</sup>rmatory factor analysis was performed by using SEM with SmartPLS 2.0 and the bootstrapping resample procedure [95]. Cronbach alpha value for PEU is above the recommended .70 value, indicating good reliability [82] (cf. Table 2). Latent variable correlations indicate a separation between the affect-oriented variable PEN and utility-oriented variables (PEN-PEU: 0.23, PEN-PU: 0.13, PEN-IU: 0.32) whereas the later show stronger correlations (PEU-IU: 0.54, PU-IU: 0,51, PEU-PU: 0.51).

Results of the PLS analysis are shown in Fig. 6. First, the path coef<sup>fi</sup>- cients between PEU and PU $( \beta = . 5 1 , \rho { < } . 0 0 1 )$ ) and PEU and IU $( \mathrm { { \beta } } = . 3 4 ,$ pb.05) are positive and signi<sup>fi</sup>cant while the coef<sup>fi</sup>cient between PEU and PEN $( \beta = . 2 3 , \rho > . 0 5 )$ is not signi<sup>fi</sup>cant. This supports H1 and H1 but not H1 . Second, the coef<sup>fi</sup>cients between PU and IU (β=.31,

## Table 2

Survey instrument and descriptive statistics (n=51).  
Note: SFL (Standardized Factor Loadings), SD (Standard Deviation)

<table><tr><td></td><td>Construct and items</td><td>SFL</td></tr><tr><td></td><td>Perceived ease of use of the H-UIS Cronbach&#x27;s Alpha: .85, Mean: 6.54, SD: .64</td><td></td></tr><tr><td>PEU1</td><td>Learning to use this H-UIS is easy ...</td><td>.894</td></tr><tr><td>PEU2</td><td>Interacting with this H-UIS is clear and understandable...</td><td>.791</td></tr><tr><td>PEU3</td><td>This H-UIS is easy to use ... ... for the acquisition of information relevant to medicationPerceived usefulness of the H-UISMean: 6.25, SD: .74</td><td>.932</td></tr><tr><td>PU</td><td>This H-UIS is useful to acquire information relevant to medicationPerceived enjoyment of the H-UIS Mean: 5.71, SD: 1.17</td><td>N/A</td></tr><tr><td>PEN</td><td>Using this H-UIS makes fun ... ... for the acquisition of information relevant to medicationIntention to use the H-UIS Mean: 6.22, SD:.85</td><td>N/A</td></tr><tr><td>IU</td><td>I would use this H-UIS to acquire information relevant to medication.</td><td>N/A</td></tr></table>

![](/api/attachments/ZW3U6AE8/fulltext/images/3b3d67f40746229a1350ffa807c536a3b9baad584bca7b40442a4dc6db083871.jpg)  
Fig. 6. PLS analysis.

pb.05) and between PEN and IU $( \beta = . 2 1 , \rho { < } . 0 5 )$ are positive and signi<sup>fi</sup>cant. Therefore, H2 and H3 are supported by the lab experiment that resembles similar studies but without signi<sup>fi</sup>cant interaction between PU and PEN (e.g., [21]). Thus PU mediated relationships between PEU and IU while a similar mediating effect was not detected for PEN.

## 7. Discussion

By this focused empirical study it was supported that the H-UIS prototype is perceived as being easy to use and useful for medication purposes within the context of the given situation. Test persons enjoyed using the H-UIS that also resulted in a signi<sup>fi</sup>cant relation with the behavioral intention to use the H-UIS. Overall, subjects did criticize the H-UIS neither qualitatively during the experimental exercise nor empirically as shown by the descriptive statistics (cf. Table 1). As a result, the H-UIS has been evaluated highly positive (97.7% scores above the neutral value of 4). One reason for these positive ratings could be due to subjects' technical background. It is thus expected that <sup>fi</sup>eld experiments will provide more widened distributions. Nonetheless several discussions were conducted on potential implications for a design revision. Descriptive statistics indicate that all constructs were rated very positive, i.e. on average above value of 6 (cf. Table 2). Based on this and small standard deviations observed it can be argued that all test persons immediately anticipated high utility of the H-UIS for drug alert situations.

Linked to the HPM it can be also argued that the H-UIS supports reduction of barriers to use drugs compliant with a therapy while service-based communication with nurses can provide positive interpersonal and situational in<sup>fl</sup>uences. Utility aspects are more focused by this H-UIS than emotional aspects. For the particular H-UIS prototype, change requests for previous design steps were not identi<sup>fi</sup>ed due to highly positive results.

## 8. Managerial and decision implications

Pervasive and ubiquitous computing technologies characterize a continuum of information technologies that are embedded in physical environments and provide different degrees of mobility [64]. Information systems that leverage these technologies provide a means for redesigning any kind of communication and collaboration situation at work, on the road, or at home [64]. Traditional Information Systems were designed to support stationary and highly structured situations. In contrast design principles for UIS are required to consider nonstationary environments in which users can perform a broad range of behaviors. UIS are more driven by communication and collaboration needs than by information technology restrictions, i.e., the guideline “information systems follow technologies” becomes reversed. We have shown how modeling tasks and empirical studies can be used together for more informed design processes that will eventually lead to a design engineering method for information systems. The empirical model was carefully derived from a kernel theory and, thus, provides clear indications whether a design prototype will support a domain dependent situation. For the H-UIS domain, we mapped the <sup>fi</sup>ve factors of the HPM onto a technology adoption model. Evaluation results of this model offer valuable clues on the <sup>fi</sup>t between the H-UIS and the targeted usage situation. In particular it gives hints on design issues, such as on need for changing communication and collaboration, information, services, or information technologies. This general approach seems to be informative and useful for a broad variety of domains.

In many ways, our work is a forward looking contribution to decision making [99] and healthcare [103,111]. The presented design languages, i.e. narratives and diagrammatic design models, were applied to the healthcare domain and were proven to be useful design tools. Our proposed method for extracting key entities from narratives was easy to use. This result encourages us to compare the proposed design model types with other types, e.g., class diagrams, use cases, and process models. During our design project we perceived that diagrammatic design models provide a degree of precision that supports common understanding among members involved in the design, evolutions, and transfer of design knowledge of H-UIS. It provides a means for reducing functional, relational and informational problems by bringing healthcare information to relevant situations. The application that reminds patients of their medication and adds new information on the <sup>fl</sup>y, can be enhanced by RFID-based services [26] that protect patients against incorrect, counterfeited [104] or expired drugs. This integrates all stakeholders and extends restricted views, such as computerized physician order entry (CPOE) for medical personnel only [49].

The summarized information on drug usage can also give feedback to physicians and pharmaceutical industry toward investigating new medical treatments or new drugs. Relational problems, e.g., determination of generic drugs during prescription processes, can be solved by drug information and medical information only. Initial semantic descriptions and ontologies for drugs [74], medicine in general (e.g., http://bioportal.bioontology.org/ontologies and [91]) and cancer in particular [5] already exist that can be used by semantic and probabilistic technology enhanced H-UIS [34,86]. The reusability of drugs requires high-quality context information, drug information, and medical information after prescription of drugs. Several technical HIS have failed to meet needs of medical personnel as those lacked understandings of ‘soft issues’ [102]. Results presented in this article argue for iterative designs that support careful designs of H-UIS by a deploying a bottom-up approach.

H-UIS could lead to savings in healthcare, but further evaluations in large-scale environments, such as hospitals, cities, or even countries, should be conducted. H-UIS could target functional, relational and informational problems for expensive drugs, such as for cancer treatments, costing in thousands of dollars.

## 9. Discussion and Limitations

Designing UIS has recently gained some momentum because Ubiq uitous and Semantic Technologies move from pure research prototypes to business applications [100,122]. For this innovative class of IS, we have outlined parts of a generic design process and design models. Early design phases were detailed up to prototypical implementations. Design models are embedded into a two-step design process: (1) use of narrative-based design models and (2) use of diagrammatic design models. Following design science theories, we used the Health Promotion Model (HPM) as kernel theory for the healthcare domain. Five key requirements were derived from HPM that were used for qualitative evaluation of narratives. During the evaluation phase, these requirements were mapped onto a technology adoption model that, in turn, was used for empirical evaluation of a prototypical realization of the H-UIS. Results were used for a discussion on re<sup>fi</sup>nements of narratives and diagrammatic design models. Hence, we described a full run-through a design process for a H-UIS.

Both, narratives and diagrammatic design models were ef<sup>fi</sup>cient means for creating design models for H-UIS. Narratives support shared understanding and facilitate discussions of ideas for UIS with experts from different domains. But it requires that all participants share a common understanding of the domain. Otherwise a pre-phase is assumed for establishing shared understandings. Creating narratives is a design task by its own right. By following physicians, nurses, and patients during their daily business take-ups were collected and subsequently translated into narratives. Narratives were discussed with medical personnel and re<sup>fi</sup>ned according to their comments. They are required to take a neutral viewpoint, are well-de<sup>fi</sup>ned, and keep a similar level of complexity and detail. Therefore designers who write narratives require enough experience.

Next, narratives were translated into diagrammatic design models. Diagrammatic design models were also discussed with medical personnel. We found that they quickly took up the modeling principles. Nonetheless the application of translation guidelines still requires suf<sup>fi</sup>cient training. Narratives and diagrammatic design models were used for reviewing requirements with medical personnel and patients and as input descriptions for subsequent systems design and realization. Understanding of narratives was framed by the AISM and made it easier for the designers to keep their focus on key entities. The AISM helped structured analysis of narratives and the creation of diagrammatic design models. Nonetheless these steps require a lot of experience in IS design and argumentations against requirements creep by technical personnel.

More dif<sup>fi</sup>cult was the integration of the Health Promotion Model. While it was straightforward to use HPM for building the empirical model, it was not so clear how it can be directly used when building design models. This is a current limitation already indicated by other design scientists [36,117]. In future work we will investigate how information system ontologies can be used for analysis of kernel theories so that results can be integrated into design models in a structured manner. This is intended to be an intermediate step toward more general justi<sup>fi</sup>catory knowledge and the embedding of our approach into a general information system design theory [32].

Further research on dedicated methods and frameworks for evaluating H-UIS is required. For this, we are currently working on two H-UIS implementations in the domains of (a) pulmonary cancer medicine and (b) children obesity management. The Health Promotion Model could be modeled in more detail so that healthcare situations can be evaluated against HPM requirements and countermeasures can be taken on the <sup>fl</sup>y.

Several limitations became visible. The H-UIS application in our article is rather focused. We have not discussed the potential for combining small H-UIS design models into larger ones and small H-UIS applications into larger ones. At least on technical level our modular and service-oriented approach supports modular and open architectures that <sup>fi</sup>t to innovative system architectures, such as OSGi.

The complexity of applying design science methodologies is generally high (e.g., [36,88]). Therefore we had to leave out some details for the design methodology used for H-UIS. For instance, development of design models is generally a complex intellectual task. The underlying approach for using design patterns [67] has not been presented and how this relates to recent results on formal ontologies [12].

The expressiveness of the AISM is deliberately reduced to a small set of conceptual entities that allow modeling of certain aspects relevant in a real-world situation. Eventually the AISM might become too limited so that other concepts are equally relevant and must be added, e.g., processes, intentions, and plans. But this must be done with outmost care because otherwise design models become fuzzy, overloaded, and ambiguous.

Several decisions have to be made when de<sup>fi</sup>ning design models. We have not focused on details of the decision making process of design because it is a highly complex task by itself. Experts from different domains have different ideas rooted in deep belief sets and expertise for a design model that <sup>fi</sup>ts to the overall purpose. On all four levels of the AISM ontological decisions are made, such as dissection of entities into sub-entities or integration into super-entities.

Similar to theatre scenes, narratives are textual descriptions of entities and their interactions within an environment. On a technical level, narratives resemble use cases that shall describe prototypical and easy to understand small-scale system-user interactions in a coherent manner. Designing narratives is currently not well understood and also requires experience. Our research is in<sup>fl</sup>uenced by Goffman's ideas [31] but we currently investigate more formalized theories of theatre plays, such as proposed by [67].

As for any Information System, evaluation of H-UIS is not free of limitations. These could include cheating by subjects, who may have incentives to outsmart these systems. There are also privacy challenges, as information processed by H-UIS and all interactions could be monitored and used for the bene<sup>fi</sup>ts of other healthcare actors at the expense of patient's rights and bene<sup>fi</sup>ts. Nonetheless H-UIS has the potential to provide major bene<sup>fi</sup>ts including better information and control for patients on drugs, improved caretaking and sophisticated business models for insurance and pharmaceutical companies; public-private partnerships, enhanced drug development in particular regarding effects of multiple drug application by elderly patients, targeted and adaptive medication, and graceful degrading of Healthcare Information Systems.

## 10. Summary and open issues

Based on previous design theories, we have described a design process for UIS that conceives generic requirements given by real-world environments that consist of <sup>fi</sup>ve core elements: user requirements, principles governing the design of a system, principles governing the development process, design models, and implementations. We have concentrated on two steps that translate user requirements into narratives and then into diagrammatic design models. We have shown how these steps and models are guided and constrained by AISM and the Health Promotion Model. Finally, we have presented a resulting implementation based on Ubiquitous Computing, Semantic Technologies, and Mobile technologies. Thus we deployed a complete design process (build and evaluate) as proposed by IS design theorists [36,117].

This work is innovative in at least two ways. First, it describes a detailed and integrated design model that can be used for a wide range of IS in general and H-UIS in particular. Second, by explicit description of single design steps, other researchers will have the opportunity to extend and challenge our design model within healthcare and other domains. This might guide toward a general IS design theory and applied design methods.

There are several challenges and research problems, which we hope will be addressed by other researchers as future work. These include

• Consideration of privacy and user acceptance issues within the design process of UIS

• Reusability of IS design models

• Design modeling in the large and evaluation of diagrammatic design models

• Deeper integration of kernel theories into to design process

• Comparison of IS that were built by using different design processes and design models

Our presented research is clearly exploratory and only conclusive with respect to some adoption behavior. This approach is guided by design science meta-theories [32,36,117] but extends it by an operational level given by various design models, prototypes, and empirical evaluation bridging kernel theories and innovation management theories. We hope that this will encourage other researchers as well to investigate structures and processes underlying design science theories.

## References

[1] G. Abowd, E. Mynatt, T. Rodden, The human experience, Pervasive Computing (Jan-Mar 2002) 48–57.

[2] I. Ajzen, The theory of planned behavior, Organizational Behavior and Human Decision Processes 50 (1991) 179–211.

[3] I. Ajzen, M. Fishbein, Understanding Attitudes and Predicting Social Behaviour, Prentice Hall, Inglewood Cliffs, NJ, 1980.

[4] Reducing and Preventing Adverse Drug Events to Decrease Hospital Costs, in: Research in Action, Agency for Healthcare Research and Quality (AHRQ), Rockville, MD, 2001, (http://www.ahrq.gov/qual/aderia/aderia.htm)

[5] M. Ashburner, C. Ball, J. Blake, D. Botstein, H. Butler, J. Cherry, A. Davis, K. Dolinski, S. Dwight, J. Eppig, M. Harris, D. Hill, L. Issel-Tarver, A. Kasarskis, S. Lewis, J. Matese, J. Richardson, M. Ringwald, G. Rubin, G. Sherlock, Gene Ontology: tool for the uni<sup>fi</sup>cation of biology, Nature Genetics 25 (May 2000) 25–29.

[6] P. Aspden, J. Wolcott, R. Palugod, T. Bastien, Preventing Medication Errors, Institute of Medicine, 2006.

[7] N. Azad, Adverse drug events in the elderly population admitted to a tertiary care hospital, Journal of Healthcare Management 47 (5) (2002) 295–306.

[8] D. Barclay, C. Higgins, R. Thompson, The partial least squares approach to causal modeling: personal computer adoption and use as an illustration, Technology Studies: Special Issue on Research Methodology 2 (2) (1995) 285–324.

[9] J.J. Baroudi, W.J. Orlikowski, The problem of statistical power in MIS research, MIS Quarterly 13 (1) (1989) 7–106.

[10] R. Boland, K. Lyytinen, Information systems research as design: identity, process and narrative, in: B. Kaplan, D. Truex III, D. Wastell, A. Wood-Harper, J. DeGross (Eds.), Information Systems Research: Relevant Theory and Informed Practice, Kluwer Academic Publishers, Boston, 2004, pp. 1–19.

[11] T.K. Gandhi, H.R. Burstin, Cook EF, et al., Drug complications in outpatients, Journal of General Internal Medicine 15 (2000) 149–154.

[12] A. Burton-Jones, Y. Wand, R. Weber, Guidelines for the empirical evaluation of conceptual modeling grammars, Journal of the Association for Information Systems 10 (6) (2009) 495–532.

[13] J.M. Carroll, Making Use: Scenario-Based Design of Human–Computer Interactions, MIT Press, Cambridge, MA, 2000.

[14] J. Carroll, Scenarios and design cognition, in: Proceedings of the IEEE Joint International Conference on Requirements Engineering (RE'02), Essen, Germany, 2002.

[15] B. Chandrasekaran, Design problem solving: a task analysis, AI Magazine 11 (4) (1990) 59–71.

[16] P. Checkland, Systems Thinking, Systems Practice, Wiley, Chichester, 1981.

[17] W.W. Chin, The partial least squares approach for structural equation modeling, in: G.A. Marcoulides (Ed.), Modern methods for business research, Lawrence Erlbaum, 1998, pp. 295–336.

[18] J. Cohen, Statistical Power Analysis for the Behavioral Sciences, Academic Press, New York, USA, 1977.

[19] F.D. Davis, Perceived Usefulness, Perceived Ease of Use, and User Acceptance of Information Technology, MIS Ouarterly 13 (1989) 319–339

[20] F. Davis, V. Venkatesh, Toward Preprototype User Acceptance Testing of New Information Systems: Implications for Software Project Management, IEEE Transactions on Engineering Management 51 (1) (2004) 31–46.

[21] F.D. Davis, R.P. Bagozzi, P.R. Warshaw, Extrinsic and intrinsic motivation to use computers in the workplace, Journal of Applied Social Psychology 22 (1992) 1111–1132.

[22] W.H. DeLone, E.R. McLean, Information systems success: The quest for the dependent variable, Information Systems Research 3 (1) (1992) 60–95.

[23] K.B. DeSalvo, W.P. Fisher, T. Ky, N. Bloser, W. Merrill, J. Peabody, Assessing measurement properties of two single-item general health measures, Quality of Life Research 15 (2) (2006) 191-201

[24] G. DeSanctis, M. Poole, Capturing the complexity in advanced technology use: adaptive structuration theory, Organization Science 5 (2) (1994) 121–147.

[25] F. Faul, E. Erdfelder, A.G. Lang, A. Buchner, G\*Power3: a <sup>fl</sup>exible statistical power analysis program for the social. behavioral, and biomedical sciences, Behavior Research Methods 39 (2) (2007) 175–191.

[26] K. Fishkin, M. Wang, A <sup>fl</sup>exible, in: Low-Overhead Ubiquitous System for Medication Monitoring, Intel Research, 2003, p. 21.

[27] C. Floerkemeier, C. Roduner, M. Lampe, RFID application development with the accada middleware platform, IEEE Systems Journal 1 (2) (2007) 82–94.

[28] R. Galloway, Health promotion: causes, beliefs and measurements, Clinical Medicine & Research 1 (3) (2003) 249–258.

[29] A. Gangemi, Some Design Patterns for Domain Ontology Building and Analysis, 2004.

[30] D. Gefen, D. Straub, M.-C. Boudreau, Structural equation modeling and regression: guidelines for research practice Communications of AIS 7 (7) (2000) 1-78

[31] E. Goffman, The Presentation of Self in Everyday Life, Doubleday, 1959.

[32] S. Gregor, D. Jones, The anatomy of a design theory, Journal of the Association for Information Systems 8 (5) (2007) 312–335.

[33] M. Grueninger, M.S. Fox, The role of competency questions in enterprise engineering, in: Proceedings of the IFIP WG5.7 Workshop on Benchmarking — Theory and Practice, 1994.

[34] T. Hayes, M. Pavel, N. Larimer, I. Tsay, J. Nutt, A. Adami, Distributed healthcare: simultaneous assessment of multiple individuals, Pervasive Computing 6 (1) (2007) 36–43.

[35] S. Helal, W. Mann, H. El-Zabadani, J. King, Y. Kaddoura, E. Jansen, The Gator Tech Smart House: a programmable pervasive space, Computer 38 (3) (2005) 50–60.

[36] A.R. Hevner, S.T. March, J. Park, S. Ram, Design science in information systems research (1), MIS Quarterly 28 (1) (2004) 75–105.

[37] L. Hinchman, S. Hinchman, Memory, identity, community: the idea of narrative in the human sciences, State University of New York Press Albany, 1997.

[38] R. Hirschheim, H. Klein, Four paradigms of information systems development Communications of the ACM 32 (10) (1989) 1199–1216.

[39] K. Hudson, New treatment options push patient care forward, Nursing Management (August 2006) 49–51.

[40] M. Pirmohamed, S. James, S. Meakin, Ch. Green, A.K. Scott, Th. J. Walley, K. Farrar, B.K. Park, A.M. Breckenridge: BMJ 2004, 329:15–19., Adverse drug reactions as cause of admission to hospital: prospective analysis of 18 820 patients, British Medical Journal 329 (July 2004) 15–19.

[41] S. Janzen, T. Kowatsch, W. Maass, A methodology for content-centered design of ambient environments, in: R. Winter, J. Zhao, S. Aier (Eds.), 5th International Conference on Design Science Research in Information Systems and Technology (DESRIST), 2010, pp. 210–225, St. Gallen, Switzerland.

[42] M. Jarke, X. Tung Bui, J. Carroll, Scenario management: an interdisciplinary approach, Requirements Engineering 3 (1998) 155–173.

[43] M. Jarke, P. Loucopoulos, K. Lyytinen, J. Mylopoulos, W. Robinson, The brave new world of design requirements, Information Systems 36 (7) (2011) 992–1008.

[44] C.B. Jarvis, S.B. MacKenzie, P.M. Podsakoff, A critical review of construct indicators and measurement model misspeci<sup>fi</sup>cation in marketing and consumer research, Journal of Consumer Research 30 (2) (2003) 199–218.

[45] P.N. Johnson-Laird, Mental Models: Towards a Cognitive Science of Language, Inference, and Consciousness, Cambridge University Press, 1983.

[46] A. Kamis, M. Koufaris, T. Stern, Using an attribute-based decision support system for user-customized products online: an experimental investigation, MIS Quarterly 32 (1) (2008) 159–177.

[47] W. Kelly, Medication errors, Professional Safety (July 2004) 35–41.

[48] M. Kerr, S. Lusk, D. Ronis, Explaining Mexican American workers' hearing protection use with the health promotion model, Nursing Research 51 (2) (2002) 100–109.

[49] P. Kilbridge, E. Welebob, D. Classen, Development of the Leapfrog methodology for evaluating hospital implemented inpatient computerized physician order entry systems, Quality & Safety in Health Care 15 (2006) 81–84.

[50] S. Klemmer, J. Landay, Toolkit support for integrating physical and digital interactions, Human Computer Interaction 24 (2009) 315–366

[51] R. Kling, Audiences, narratives, and human-values in social-studies of technology, Science Technology & Human Values 17 (3) (1992) 349–365.

[52] S. Koch, M. Marschollek, K.H. Wolf, M. Plischke, R. Haux, On health-enabling and ambient-assistive technologies — what has been achieved and where do we have to go? Methods of Information in Medicine 48 (1) (2009) 29–37.

[53] S.Y.X. Komiak, I. Benbasat, The effects of personalization and familiarity on trust and adoption of recommendation agents, MIS Quarterly 30 (4) (2006) 941–960.

[54] S.M. Kosslyn, Image and Mind, Harvard University Press, Cambridge, MA, London 1980.

[55] M. Koufaris, Applying the technology acceptance model and <sup>fl</sup>ow theory to online consumer behavior, Information Systems Research 13 (2) (2002) 205–223.

[56] W. Kuechler, V. Vaishnavi, So, talk to me: the effect of explicit goals on the comprehension of business process narratives, MIS Quarterly 30 (4) (2006) 961-996

[57] W. Kuechler, V. Vaishnavi, On theory development in design science research: anatomy of a research project, European Journal of Information Systems 17 (2008) 489–504.

[58] R. Lamb, R. Kling, Reconceptualizing users as social actors in information systems research, MIS Quarterly 27 (2) (2003) 197–235.

[59] T.A. Lashina, Intelligent bathroom, in: European Symposium on Ambient Intelligence, 2004, Eindhoven, Netherlands.

[60] J. Lazarou, B. Pomeranz, P. Corey, Incidence of adverse drug reactions in hospital ized patients: a meta-analysis of prospective studies, Journal of the American Medical Association 279 (1998) 1200–1205

[61] U. Lechner, B.F. Schmid, Communities and media — towards a reconstruction of communities on media, in: 34th Annual Hawaii International Conference on Systems Sciences (HICSS-34), 2001.

[62] J. Lucas, S. Orshan, F. Cook, Determinants of health-promotion behavior among women ages 65 and above living in the community, Scholarly Inquiry for Nursing Practice 14 (177–100) (2000).

[63] K. Lyytinen, Different perspectives on information systems: problems and solutions, ACM Computing Surveys 19 (1) (1987) 5–46.

[64] K. Lyytinen, Y. Yoo, Issues and challenges in ubiquitous computing, Communication of the ACM 45 (2002) 62–65.

[65] K. Lyytinen, Y. Yoo, Research commentary: the next wave of nomadic computing, Information Systems Research 13 (4) (2002) 377–388.

[66] W. Maass, A. Filler, Towards an infrastructure for semantically annotated physical products, in: C. Hochberger, R. Liskowsky (Eds.), Informatik 2006, Springer, Berlin 2006 pp. 544–549

[67] W. Maass, S. Janzen, Pattern-based approach for designing with diagrammatic and propositional conceptual models, in: 6th Int. Conf. on Design Science Research in Information Systems and Technology (DESRIST 2011), 2011, Milwaukee, Wisconsin USA.

[68] S. March, G. Smith, Design and natural science research on information technology, Decision Support Systems 15 (1995) 251–266.

[69] M.L. Markus, A. Majchrzak, L. Gasser, A design theory for systems that support emergent knowledge processes, MIS Quarterly 26 (3) (2002) 179–203.

[70] C. Masolo, L. Vieu, E. Bottazzi, C. Catenacci, R. Ferrario, A. Gangemi, N. Guarino, Social roles and their descriptions, in: D. Dubois, Ch. Welty, M. Williams (Eds.), Ninth International Conference on the Principles of Knowledge Representation and Reasoning (KR2004), 2004, pp. 267–277, (Whistler, BC, Canada, 2004).

[71] M. McCullagh, S. Luck, D. Ronis, Factors in<sup>fl</sup>uencing use of hearing protection among farmers: a test of the Pender Health Promotion Model, Nursing Research 51 (1) (2002) 33–39.

[72] C. McDonald, Use of a computer to detect and respond to clinical events: its effect on clinician behavior, Annals of Internal Medicine 84 (1976) 162–167.

[73] G.H. Mead, Philosophy of the Act, Chicago Press, 1938.

[74] G.H. Merrill, P.B. Ryan, J.L. Painter, Applying a UMLS/SNOMED-based drug ontology for observational pharmacovigilance, in: J. Holmes, A. Tucker (Eds.), Intelligent Data Analysis in Biomedicine and Pharmacology, 2008, Washington, D.C.

[75] M. Mikkonen, S. Vayrynen, V. Ikonen, M. Heikkila, User and concept studies as tools in developing mobile communication services for the elderly, Personal and Ubiquitous Computing 6 (2002) 113–124.

[76] G.C. Moore, I. Benbasat, Development of an instrument to measure the perceptions of adopting an information technology innovation, Information Systems Research 2 (1991) 173–191.

[77] Mpill, in, (2008).

[78] M. Murray, Automated medication dispensing devices, in: Making Health Care Safer: A Critical Analysis of Patient Safety Practices, Agency for Healthcare Re search and QualityUS Department of Health & Human Services, 2001.

[79] K. Nelson, S. Nadkarni, V. Narayanan, M. Ghods, Understanding software operations support expertise: a revealed causal mapping approach, MIS Quarterly 24 (3) (2000) 475–507.

[80] S. Newton, Designing as disclosure, Design Studies 25 (1) (2004) 93–109.

[81] E.W.T. Ngai, T.C.E. Cheng, S. Au, K.-H. Lai, Mobile commerce integrated with RFID technology in a container depot, Decision Support Systems 43 (1) (2007) 62–76 [82] J.C. Nunnally, Psychometric Theory, McGraw-Hill, New York, 1967.

[83] W.J. Orlikowski, S.R. Barley, Technology and institutions: what can research on information technology and research on organizations learn from each others? MIS Quarterly 25 (2) (2001) 145–165.

[84] C. Orwat, A. Graefe, T. Faulwasser, Towards pervasive computing in health care — a literature review, BMC Medical Informatics and Decision Making 28 (6) (2008).

[85] T. Østbye, D. Lobach, D. Cheesborough, A.M. Lee, K.M. Krause, V. Hasselblad, D. Bright, Evaluation of an infrared/radiofrequency equipment-tracking system in a tertiary care hospital, Journal of Medical Systems 27 (4) (2003) 367–380.

[86] F. Paganelli, D. Giuli, A context-aware service platform to support continuous care networks for home-based assistance, in: C. Stephanidis (Ed.), Universal Access in HCI, Part II, HCII 2007, Springer, 2007, pp. 168–177.

[87] H. Patel, D. Bell, M. Molokhia, J. Srishanmuganathan, M. Patel, J. Car, A. Majeed, Trends in hospital admissions for adverse drug reactions in England: analysis of national hospital episode statistics 1998–2005, BMC Clinical Pharmacology 7 (9) (2007).

[88] K. Peffers, T. Tuunanen, M.A. Rothenberger, S. Chatterjee, A design science research methodology for information systems research, Journal of Management Information Systems 24 (3) (2007) 45–77.

[89] N.J. Pender, C. Murdaugh, M.A. Parsons, Health Promotion in Nursing Practice, 5 ed. Prentice-Hall Upper Saddle River NI 2006.

[90] J. Piazza, K. Conrad, J. Wilbur, Exercise behavior among female occupational health nurses: influence of self-efficacy, perceived health, control. and age Journal of the American Association of Occupational Health Nurses (AAOHN) 49 (2) (2001) 79–86.

[91] C. Price, K. Spackman, SNOMED clinical terms, British Journal of Healthcare Computing & Information Management 17 (3) (2000) 27–31.

[92] S. Purao, V.C. Storey, T.D. Han, Improving reuse-based system design with learning, Information Systems Research 14 (3) (2003) 269–290.

[93] B. Reeder, R. Hills, G. Demiris, D. Revere, J. Pina, Reusable design: a proposed approach to Public Health Informatics system design, BMC Public Health 11 (1) (2011) 116.

[94] D. Rind, C. Safran, R. Phillips, Q. Wang, D. Calkins, T. Delbanco, L. Howard, M. Bleich, V. Warner, M. Slack, Effect of computer-based alerts on the treatment and outcomes of hospitalized patients, Archives of Internal Medicine 154 (1994) 1511–1517.

[95] C.M. Ringle, S. Wende, S. Will, SmartPLS 2.0 (M3) Beta, 2003. Hamburg.

[96] E.M. Rogers, Diffusion of Innovations, 5 ed. Free Press, New York, 2003.

[97] A. Schweiger, A. Sunyaev, J.-M. Leimeister, H. Krcmar, Information systems and healthcare: toward seamless healthcare with software agents, Communications of the Association for Information Systems 19 (2007) 692–710.

[98] J.R. Searle, The Construction of Social Reality, Free Press, New York, 1995.

[99] J.P. Shim, M. Warkentin, J. Courtney, D.J. Power, R. Sharda, C. Carlsson, Past, present, and future of decision support technology, Decision Support Systems 33 (2) (2002) 111–126.

[100] C. Silva, S. Yates, R. Whiteley, R. Dines, R. Batiancila, The Rise of Ubiquitous Mobility Solutions: Solutions for “Anywhere” Connectivity Begin to Take Shape, Forrester Research, 2007.

[101] H.A. Simon, The Sciences of the Arti<sup>fi</sup>cial, second ed. MIT Press, 1981.

[102] D. Sittig, A. Wright, L. Simonaitisc, J. Carpenter, G. Allen, B. Doebbeling, A. Sirajuddin I. Ash B. Middleton The state of the art in clinical knowledge management: an inventory of tools and techniques, International Journal of Medical Informatics 79 (1) (2010) 44–57

[103] S. Sneha, U. Varshney, Enabling ubiquitous patient monitoring: model, decision protocols, opportunities and challenges, Decision Support Systems 46 (3) (2009) 606–619.

[104] T. Staake, E. Fleisch, Countering Counterfeit Trade — Illicit Market Insights, Best-Practice Strategies, and Management Toolbox, Springer-Verlag Berlin, 2008.

[105] A. Tarski, Der Wahrheitsbegriff in den formalisierten Sprachen, Studia philosophica I (1935) 261–405.

[106] D. Te'eni, Review: a cognitive–affective model of organizational communication for designing IT, MIS Quarterly 25 (2) (2001) 251–312

[107] UN/CEFACT, OASIS, Message Service Speci<sup>fi</sup>cation: ebXML Transport, Routing & Packaging Version 1.0, 2001.

[108] H. van der Heijden, User acceptance of hedonic information systems, MIS Quarterly 28 (4) (2004) 695–704.

[109] U. Varshney, Pervasive healthcare and wireless health monitoring, Mobile Network Applications 12 (July 2007) 113–127.

[110] U. Varshney, Pervasive healthcare, IEEE Computer 36 (12) (2003) 138–140.

[111] U. Varshney, A framework for supporting emergency messages in wireless patient monitoring, Decision Support Systems 45 (4) (2008) 981–996.

[112] U. Varshney, R.J. Vetter, R. Kalakota, Mobile commerce: a new frontier, Computer 33 (10) (2000).32-38

[113] V. Venkatesh, M.G. Morris, G.B. Davis, F.D. Davis, User acceptance of information technology: toward a uni<sup>fi</sup>ed view, MIS Quarterly 27 (3) (2003) 425–478.

[114] S. Vodanovich, D. Sundaram, M. Myers, Digital natives and ubiquitous information systems, Information Systems Research 21 (4) (2010) 711–723.

[115] P. Wack, Scenarios — shooting the rapids, Harvard Business Review 63 (6) (1985) 139–150.

[116] P. Wack, Scenarios — uncharted waters ahead, Harvard Business Review 63 (5) (1985) 72–89.

[117] J. Walls, G. Widmeyer, O. El Sawy, Building an information system design theory for viligant EIS, Information Systems Research 3 (1) (1992) 36–59.

[118] Y. Wand, R. Weber, Information systems and conceptual modeling — a research agenda, Information Systems Research 13 (4) (2002) 363–376.

[119] Y. Wand, D. Monarchi, J. Parsons, C. Woo, Theoretical foundations for conceptual modelling in information systems development, Decision Support Systems 15 (1995) 285–304.

[120] R. Want, RFID, a key to automating everything, Scienti<sup>fi</sup>c American 290 (1) (2004) 56–65.

[121] M. Weiser, The computer for the 21st century, Pervasive Computing First published: Scienti<sup>fi</sup>c Amercian 1 (1) (2002) 18–25

[122] D. West, M. Gilpin, D. D'Silva, What Semantic Technology Means to Application Development Professionals: Semantic Technology is Now Ready for Increased but Focused Use, Forrester Research, 2009.

[123] T. Wu, N. Pender, Determinants of physical activity among Taiwanese adolescents: an application of health promotion model, Research in Nursing & Health 25 (1) (2002) 25–36.

[124] Y. Yoo, Computing in everyday life: a call for research on experiential computing, MIS Quarterly 34 (2) (2010) 213–231.

[125] H. Zukier, The paradigmatic and narrative modes in goal-guided inference, in: R. Sorrentino, E. Higgins (Eds.), Handbook of Motivation and Cognition: Foundations of Social Behavior, Guilford Press, New York, 1986, pp. 465–502.

Wolfgang Maass is full professor and chair in Information and Service Systems (ISS), faculty of Law and Economics, Saarland University, Germany. He was awarded with a habilitation by the Department of Management at the University of St. Gallen, Switzerland and received his Ph.D. in Computer Science from the faculty of Natural Sciences and Technology I at the Saarland University. His doctorate studies were funded by a graduate program in Cognitive Science by the German National Science Foundation (DFG). Prior to that he studied Computer Science at the RWTH Aachen, Germany. His current research interests are focused on ubiquitous information systems incl. Internet of Things, design science methodologies, conceptual modeling, big data processing in bioinformatics, and recommendation agents. His work has been published in journals including IEEE Intelligent Systems, Computers in Human Behavior, Arti<sup>fi</sup>cial Intelligence Review Journal, Electronic Markets, BMC Bioinformatics, and Algorithms for Molecular Biology. He was guest professor at the Department of Bioinformatics and Computational Biology (MD Anderson Cancer Center), University of Texas, USA and guest researcher at the National Center for Geographic Information and Analysis (NCGIA), UC Santa Barbara, USA.

Upkar Varshney is currently Associate Professor of Computer Information Systems at Georgia State University, Atlanta. His current interests include pervasive healthcare, mobile commerce, ubiquitous computing, and wireless networks. He has authored over 130 papers including 60 in national and international journals. He is credited with several “<sup>fi</sup>rst” papers in streams of mobile commerce and pervasive healthcare. According to Scholar-Google, his papers are among the highly cited including. He is the founding cochair (with Prof. Imrich Chlamtac) of International Pervasive Health Conference (http://www.pervasivehealth.org/previous/index.html) in 2006 and the steering committee co-chair for 2008 conference (http://www.pervasivehealth.org). Upkar is also the program co-chair for Americas Conference on Information Systems (AMCIS-2009)

Upkar has presented over fifty tutorials workshops and a few keynotes at maior wireless computing, and information systems conferences. He has also received grants totaling \$500K from several funding agencies including the National Science Foundation. His teaching awards include Myron T. Greene Outstanding Teaching Award (2004), RCB College Distinguished Teaching Award (2002), and Myron T. Greene Outstanding Teaching Award (2000). He has served or is serving as an editor/guest editor for several major journals including IEEE Transactions on IT in Biomedicine, ACM/Springer Mobile Networks (MONET), Decision Support Systems (DSS), IEEE Computer, Communications of the AIS (CAIS), Int. J. on Network Management (IJNM), Int. Journal on Mobile Communications (IJMC) among others.
