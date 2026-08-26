---
otero_id: 1680
otero_key: "ZDWTNN8R"
title: "Knowledge-centered design of decision support systems for emergency management"
authors: "Daniela Fogli; Giovanni Guida"
year: "2013"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2013.01.022"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Knowledge-centered design of decision support systems for emergency management

Daniela Fogli ⁎, Giovanni Guida

Dipartimento di Ingegneria dell'Informazione, Università degli Studi di Brescia Via Branze 38, 25123 Brescia, Italy

a r t i c l e i n f o

Article history: Received 1 June 2012 Received in revised form 4 December 2012 Accepted 28 January 2013 Available online 8 February 2013

Keywords: Decision-support systems Knowledge-centered design Knowledge engineering Emergency management

## a b s t r a c t

This paper focuses on the design of decision support systems for emergency managers in charge of planning, coordinating and controlling the actions carried out to respond to a critical situation. A novel knowledgecentered design methodology is proposed and demonstrated through the application in a concrete case study in the <sup>fi</sup>eld of pandemic <sup>fl</sup>u emergency management. Knowledge-centered design is based on a rational and structured approach to the elicitation and modeling of the knowledge concerning the target environment, the application domain, the intended users, their tasks, and the speci<sup>fi</sup>c activities that the decision support system is expected to provide. Our proposal aims at overcoming some of the limitations of user-centered and activity-centered design in the speci<sup>fi</sup>c context of decision support systems. Knowledge-centered design is based on an iterative process that goes through four main phases, namely: target environment identi<sup>fi</sup>cation, domain understanding, user characterization, and functional analysis. The paper illustrates each phase in detail and discusses the application in the proposed case study.

© 2013 Elsevier B.V. All rights reserved.

## 1. Introduction

Emergency management encompasses a variety of activities, such as training and preparation, early signal detection, planning, mitigation, response, and recovery, which are usually carried out to cope with potentially catastrophic events caused by natural hazards or human behavior [18]. Indeed, an emergency may have a huge impact on every business, service provider, community and family in a nation, not just because of illness and loss of life, but also for the negative effects it exerts on workforce, availability of goods and services, and economic and social conditions in general. A structured and coordinated management is fundamental to be prepared and to minimize the consequences that an emergency may originate. Different approaches to emergency management can be found in current literature. They can be roughly divided in three classes: i) solutions based on social media [8,21,39], which aim at improving information exchange and sharing, and to favor citizens' participation; ii) emergency management information systems [2,9,42], designed to address the problem of enabling communication and coordination among independent institutions that may have different and competitive goals, and where a central control is absent; and iii) decision support systems [6,15,45], proposed to provide emergency managers with indications for selecting among alternative courses of actions in complex and uncertain situations.

By examining closer the third class of approaches, we can observe that Decision Support Systems (DSS) are usually applied in speci<sup>fi</sup>c emergency situations – for example nuclear and radiological emergencies [34], earthquakes [12], health emergencies [20] – or to address speci<sup>fi</sup>c aspects of emergency management, such as situation awareness [35], improvisation [24], and context awareness [25]. The principles on which the design of these systems is based are mostly domaindependent; only rarely general and systematic approaches to the design and development of DSSs are proposed in literature. Among the few examples, we mention the knowledge-based framework proposed in [10], which exploits semantic web technologies to model the application domain and fuzzy cognitive maps to represent emergency plans; Ahmed et al. [3] present a scenario-driven, process-oriented DSS generator; <sup>fi</sup>nally, the work described in [25], even though focused on context-awareness, proposes a high-level design theory for real-time accident handling.

All such systems and approaches, even though representing important success cases, offer only a limited contribution to the general topic of DSS design for emergency management. Most of the works mentioned above focus on the conceptual and technical aspects of the DSS, but leave the design methodology and the relevant design processes in the background. Moreover, each system seems to adhere to a speci<sup>fi</sup>c design practice, which can hardly be replicated in different contexts. The <sup>fi</sup>rst goal of our work is, therefore, to face the issue of generality and to propose a methodology to DSS design that can <sup>fi</sup>t the needs of a variety of application contexts and can be effectively applied in practical cases.

Going deeper into the design issue, the paradigm of user-centered design is advocated in recent literature about emergency management as one of the most sound and viable approaches to DSS design (see, for instance, [5,7,29]). User-centered design requires to involve users throughout the design process, from requirement and task analysis to usability testing; in this way, users can directly in<sup>fl</sup>uence how the system takes shape [1,28]. Recently, however, Donald Norman has warned that satisfying user requests should not be overestimated: “listening to customers is always wise, but acceding to their requests can lead to overly complex designs” [27]. Users do not necessarily know what is good for them. Moreover, different users may express different requirements, and thus satisfying the needs of a user may imply to neglect those of another. User-centered design, although important, might not be enough and in some cases might even turn out to be harmful. Therefore, Norman suggests that activity-centered design is superior to the mere user-centered approach and should be preferred in most cases [27]. Indeed, while user-centered design focuses on what a user considers good for him/her, activity-centered design advocates the need to take into account what is actually good for a user performing a given activity. The difference between these two standpoints is evident: while the former is more subjective and puts the design responsibility onto the user's shoulders, the latter is more objective and restores the designer in his/her original role.

A closer analysis of these approaches reveals, however, that users – with their needs and activities – are generally not the ultimate targets of a DSS. Both the user and the system are part of a larger environment – a process, an organization, a social context – that is expected to bene<sup>fi</sup>t from the availability of the DSS. Considering the case of emergency management, while it is important to consider the needs and preferences of emergency managers and the requirements emerging from the analysis of their activity, it is equally – or even more – important to take into account the actual needs of the population affected by the emergency and the goals of the institutions in charge of facing the emergency. Both user-centered and activity-centered design paradigms hardly take into account these aspects and might reveal weak in complex decision making situations.

The second goal of our work is, therefore, to propose a novel approach to DSS design that focuses not only on the users and their activity, but also on the knowledge about the environment where the users operate and the DSS will be employed. Our standpoint is that if the users can express their needs and preferences, and the analysis of their activity can reveal much of the actual tasks they are in charge of, only the consideration of a larger environment can allow identifying the real goals, constraints, processes, and rules of the decision making activity. We call this novel approach knowledge-centered design, since it puts knowledge in the center: knowledge about the users of the DSS, the activities they are supposed to carry out with the support of the DSS, and the environment where the DSS will be applied. Knowledge-centered design is based on an evolutionary concept, where a design can grow step by step towards a better design, through an incremental process of mutual adaptation where each involved party – the user, the system, and the environment – can impose something to the others and accept or reject the impositions received. Our knowledge-centered design methodology does not aim at substituting user- or activity-centered design, but incorporates these concepts in a wider framework, thus making the whole design process more sound and robust. Moreover, it strongly promotes a participatory approach to design [36], where different subjects – managers, process and organization specialists, domain experts, and operative personnel – are involved in the design process and bring their speci<sup>fi</sup>c knowledge and experience.

The paper is organized as follows: Section 2 presents an overview of the knowledge-centered design methodology; Section 3 introduces the HEALTHREATS case study; Sections 4 to 7 focus on the individual phases of the methodology and present them in detail with reference to the case study considered; Section 8 illustrates the main features of the implemented DSS prototype, and Section 9 reports the main outcomes of DSS evaluation; and <sup>fi</sup>nally, Section 10 discusses the results obtained and outlines some issues for future research.

## 2. Knowledge-centered design: the methodology at a glance

## 2.1. The phases

The core of knowledge-centered design is the consideration of the different kinds of knowledge that are involved in the design of a DSS, namely: (i) knowledge about the target environment where the DSS will be used, (ii) knowledge about the user tasks, and (iii) knowledge about user pro<sup>fi</sup>les and interaction patterns. In order to satisfy this need in a structured and effective way, a knowledge-centered design methodology grounded on four main phases has been de<sup>fi</sup>ned, as illustrated below (see Fig. 1):

1. Target environment identification. This phase has the goal of developing a deep understanding of the piece of real world where the DSS will be applied, including all the stakeholders that will be in<sup>fl</sup>uenced, directly or indirectly, by the system, their work practices, the tools they are used to interact with, as well as the social and physical contexts in which they operate.

2. Domain understanding. Domain understanding aims at identifying, collecting and representing all the knowledge relevant to the speci<sup>fi</sup>c domain of the DSS, including the basic entities and processes that characterize the domain, the tasks carried out by emergency managers, and the knowledge necessary to operate correctly and effectively.

![](/api/attachments/ZDWTNN8R/fulltext/images/323be1fad13e1e56d712f498d066d7fb47cdd2e55c2a128da85fa5776ebe0e3a.jpg)  
Fig. 1. The knowledge-centered design methodology.

3. User characterization. This phase concerns all aspects of design that have an impact on the quality of interaction and, <sup>fi</sup>rst of all, on usability. Therefore, the various classes of users that are expected to work with the DSS are identi<sup>fi</sup>ed, and their needs, goals, preferences, background, and social traits are brought to light. As a result, interaction requirements are then de<sup>fi</sup>ned.

4. Functional analysis. Eventually, the speci<sup>fi</sup>c functions that the DSS is expected to provide are analyzed and a detailed speci<sup>fi</sup>cation of system behavior is provided.

As it can be noted, phases (1) to (4) have a progressively narrower scope and focus on different kinds of knowledge. Starting from the target environment where the DSS is supposed to be applied, they consider in turn the application domain, the intended users, and eventually the functions that the system is expected to provide. DSS design is then followed by the development phase, and, once a prototype of the DSS has been developed, an evaluation phase is necessary to assess its performance both in an experimental setting and in the target environment.

This methodology is intrinsically iterative and includes two cycles: the inner cycle involves all the four design phases and aims at assuring through a step-wise re<sup>fi</sup>nement process that the best possible design is obtained, both in terms of correctness and completeness; the outer cycle involves also the development and evaluation phases and has the goal of favoring the incremental improvement of the DSS by repeatedly iterating through design, system development and evaluation.

## 2.2. The techniques

Applying the methodology outlined in the previous section requires the availability of sound techniques. The four design phases are all grounded on a common, fundamental activity, namely the acquisition and modeling of knowledge [17]. To this purpose, a speci<sup>fi</sup>c knowledge acquisition methodology has been adopted that can be applied, with the relevant customizations, for each of the above four phases. This methodology is organized in <sup>fi</sup>ve steps, as illustrated below (see Fig. 2):

(i) Elicitation collects and analyzes the original mind and point of view of managers, domain experts and users, with the aim of making their knowledge, needs, and expectations explicit. This step focuses both on surface knowledge that can be obtained with simple interviews, and on deep knowledge [31], which requires more introspection and analysis to be brought to light and expressed in verbal terms. All state-ofthe-art techniques for knowledge acquisition, including questionnaires, individual and group interviews, and naturalistic observation may be employed. Important information may be obtained also from available documents on the speci<sup>fi</sup>c topics at hand and from more informal sources of information like personal notes, technical drafts, and especially logbooks of past emergencies.

(ii) Modeling synthesizes the knowledge obtained through elicitation and produces a draft design in a form that can be easily and unambiguously understood by all persons involved in the design process. It focuses both on factual knowledge, including entities, properties and relations of the domain, and on procedural knowledge concerning actions, activities and processes.

(iii) Integration merges knowledge collected through different acquisition sessions and aims at producing a coherent and as far as possible complete representation of the relevant design elements. One of the main problems that has to be faced in this step is the fusion of knowledge obtained from different sources, which might be scarcely consistent or even con<sup>fl</sup>icting.

(iv) Refinement aims at resolving ambiguities, deepening concepts, looking for missing knowledge, dropping useless or misleading information, correcting errors, and improving the representation. Re<sup>fi</sup>nement stimulates the feedback of managers, domain experts and users, collects their critiques, and goes through a rehearsal of the design produced so far until a clear and shared version is achieved.

(v) Validation critically examines and scrutinizes the design devel oped to obtain a <sup>fi</sup>nal approval from all involved parties. Validation is the last but perhaps the most crucial step of knowledge acquisition, since lacking a <sup>fi</sup>nal assessment and a formal approval of the design may give rise to serious problems about the quality of the DSS to be developed.

![](/api/attachments/ZDWTNN8R/fulltext/images/6a5d7d8c90fae6e344f7a8553ee4b69e92465e75a07a9e8039aad22441b411a2.jpg)  
Fig. 2. The methodology for knowledge acquisition.

Knowledge acquisition is a typical iterative process and must go through several cycles before a sound result is eventually obtained.

## 3. Experimenting knowledge-centered design

The knowledge-centered design methodology introduced in Section 2 was <sup>fi</sup>rst proposed, in a preliminary version, in the frame of a one-year project [32] on decision support in emergency management funded by Regione Lombardia, Italy, in the years 2004–2005. In this context the fundamental traits of the methodology were outlined and practically experimented in the design of a DSS for assisting emergency managers in an earthquake case [16]. Two years later, the HEALTHREATS project [33], co-funded by the European Union in the years 2007–2010, offered the concrete occasion to develop the knowledge-centered design methodology to its full potential and to test it in a wider case concerning the issue of pandemic <sup>fl</sup>u emergency. The HEALTHREATS project included eleven partners from <sup>fi</sup>ve European countries, namely Italy, Romania, Slovenia, Portugal and Spain. The main goal was to develop an innovative DSS to assist the institutions in charge of public health in making strategic decisions underpinning the launch and management of operational interventions in response to pandemic <sup>fl</sup>u. As a starting point of our project, the relevant prescriptions of the World Health Organization (WHO) have been assumed, as speci<sup>fi</sup>ed in the “WHO global in<sup>fl</sup>uenza preparedness plan” [44], which provides national health authorities with priority goals and recommendations to develop preparedness plans. Of the six WHO pandemic phases, it was decided to focus on phases 4, 5 and 6, concerning the pandemic alert period and the pandemic period (see Table 1). The project activity was initially focused on the Italian case, namely on ASL Brescia (an important local health authority), which offered a suitable context for knowledge acquisition, DSS design, and evaluation. Afterwards, the DSS prototype was deployed to other partners of the HEALTHREATS project and further experimented in different practical cases. In Sections 4 to 7 we illustrate in detail the phases of the knowledge-centered design methodology applied to the design of the DSS prototype developed in the frame of the HEALTHREATS project.

## Table 1

WHO pandemic periods and phases [44].

<table><tr><td>Period</td><td>Phase</td><td>Description</td></tr><tr><td rowspan="2">Interpandemic period</td><td>1</td><td>No new influenza virus subtypes have been identified in humans. An influenza virus subtype that has caused human infection may be present in animals. If present in animals, the risk of human infection is considered to be low</td></tr><tr><td>2</td><td>No new influenza virus subtypes have been identified in humans, although a circulating animal influenza virus subtype poses a substantial risk of human disease</td></tr><tr><td rowspan="3">Pandemic alert period</td><td>3</td><td>Human infections with a new subtype, but no human-to-human spread or at most rare incidence of spread to a close human contact</td></tr><tr><td>4</td><td>Small clusters with limited human-to-human transmission, but spread is highly localized, suggesting that the virus is not well-adapted to humans</td></tr><tr><td>5</td><td>Larger cluster(s), but human-to-human spread still localized, suggesting that the virus is becoming increasingly better adapted to humans, but may not yet be fully transmissible</td></tr><tr><td>Pandemic period</td><td>6</td><td>Increased and sustained transmission in general human population</td></tr><tr><td>Postpandemic period</td><td></td><td>Return to interpandemic period</td></tr></table>

## 4. Identifying the target environment

Target environment identi<sup>fi</sup>cation includes several issues, largely depending on the speci<sup>fi</sup>c application context considered. In our case we focused on three main points:

• modeling the emergency scenario and identifying the main stakeholders involved and their interactions;

• analyzing the emergency management task;

• identifying the decision support paradigm appropriate for emergency management.

To face these issues six managers and three domain experts were involved, while three knowledge engineers were in charge of the analysis. Initially, according to the methodology illustrated in Section 2.2, a wide-scope knowledge acquisition activity has been carried out. Several naturalistic observation sessions have been performed to analyze experts' behavior in concrete emergency management tasks. Moreover, log books compiled in past health emergencies have been analyzed, which offered a deeper and detailed insight into the matter and provided new hints for further investigation. Traditional individual and group interviews have then been exploited to elicit knowledge about the typical problems faced by emergency managers and the relevant strategies adopted. Speci<sup>fi</sup>c attention has been devoted to the emergency management unit as a whole and to the need for cooperation among its members; here, several collaboration issues were brought to light and their impact on DSS design was clari<sup>fi</sup>ed. After each signi<sup>fi</sup>cant step of the analysis, managers were requested to check and possibly revise the model of the target environment under construction and eventually express their validation.

The main results obtained in this phase are illustrated in the following sections.

## 4.1. The emergency scenario

An emergency is a situation that, independently of being or not being foreseeable and independently of the level of preparedness, causes a sudden and strong modi<sup>fi</sup>cation in a speci<sup>fi</sup>c context with a widespread impact on the environment and on the society, requiring a prompt and massive intervention by all parties involved, from public institutions to private citizens. In general terms, in any emergency <sup>fi</sup>ve main classes of stakeholders are involved: i) the impact population including the persons directly affected by the events that determine the state of emergency; ii) the context population concerning the people related in any way to the impact population, but not directly affected by the occurred events, ranging from the relatives and friends of the persons belonging to the impact population to the people simply informed of the events occurred through newspapers, radio, TV or the web; iii) the intervention staff, including all professionals and volunteers engaged in the practical management of the emergency; iv) the emergency management unit, in charge of planning, coordination and control of the actions carried out by the intervention staff; and v) the institutions involved in the management of the emergency at local, governmental or world-wide levels.

In this context, several interactions occur, both internally to each class of stakeholders and among them. On the basis of these interactions, the emergency environment can be structured into four levels:

• the population level includes the subjects belonging to the impact and context populations and any interaction occurring between them;

• the operation level concerns the intervention staff and includes both the interactions occurring inside it to organize and manage the operations, and the interactions between it and the impact and context populations aimed at actuating the concrete measures necessary to face the emergency;

• the management level is about the emergency management unit and involves the various interactions internal to the emergency management unit and between the emergency management unit and the intervention staff;

• the institutional level, <sup>fi</sup>nally, concerns the interactions between the institutions and the emergency management unit.

This scenario is illustrated in Fig. 3.

The need for a DSS speci<sup>fi</sup>cally devoted to guide and support the activity of the emergency management unit is largely recognized [6,15,42]. Therefore, in the following, we will focus on the management level only.

## 4.2. The emergency management task

Emergency management is a complex and multifaceted task that involves a variety of problems and requires that the persons in charge, namely the emergency managers, carry out multiple reasoning paths in parallel. Emergency managers are not involved in operative activities, but – more importantly – have responsibility about situation assessment, action planning, and allocation of resources. They are in charge of a wide set of duties. First of all, they must acquire and validate information from the <sup>fi</sup>eld about the events occurred, their consequences, the actions undertaken to face the emergency situation and their effects. On the basis of this information – generally chaotic, redundant, and partially inconsistent – emergency managers assess the situation at hand, analyze primary needs, identify the most appropriate intervention plans, and allocate the necessary resources to the activities to be carried out. They also have to interact with the intervention staff in charge of executing the intervention plans and manage effective communication with them. Finally, they must assure correct and timely communication with all the institutions involved in emergency management.

Emergency managers carry out all these duties in a context characterized by fatigue, pressure, stress, and responsibility overload. In their job, they have to comply with formal regulations, apply stated emergency plans, <sup>fi</sup>nd solutions to new emerging problems, dynamically adapt to a rapidly changing situation, and promptly respond both to events occurring in the emergency <sup>fi</sup>eld and to the requests arriving from the institutions. These tasks are typically knowledge intensive and require emergency managers to exploit all their skills and experience and – most importantly – to collaborate. In fact, emergency management is a cooperative activity, where several specialists must share information and participate in a highly interactive deci sion making process [5].

The kind of collaboration necessary among emergency managers, however, has not to be conceived as a free and unstructured process, whose dynamics is solely governed by the goals, skills, and initiative of the participants. Collaboration is strictly ruled by domain knowl edge and is aimed at concretely supporting emergency managers in the execution of speci<sup>fi</sup>c tasks. Therefore, it must be highly structured and sacri<sup>fi</sup>ce part of freedom and spontaneity of a more <sup>fl</sup>exible con cept of collaboration in favor of effectiveness and ef<sup>fi</sup>ciency.

## 4.3. The decision support paradigm

Several approaches to decision support are possible [15], ranging from merely informative to strong normative paradigms. Informative support aims at improving the quality of human decisions by providing decision makers with more information that can help them analyze the current situation and assess alternatives. However, in the case of a large-scale emergency a merely informative approach would not be effective: decision support should not provide emergency managers with more data, but possibly with less, more focused information. Normative support, on the other hand, aims at directly helping decision makers through the suggestion of a <sup>fi</sup>nal decision, possibly the best available one, ready for use. In a sense, it aims at substituting decision makers in all possible cases, solving the decision problem at the root. A strongly normative approach would hardly be applicable in emergency management since it is practically impossible to foresee all possible cases that might occur and to identify, for each of them, an intervention strategy suitable in any context. Moreover, a too strong normative support might raise acceptance problems, since, without a justi<sup>fi</sup>cation, emergency managers might be reluctant to adhere to the suggestions produced by a DSS.

A closer analysis of the behavior of emergency managers reveals that the majority of decisions they make are simple: in front of a problem, there is only one possible solution, well known to emergency management experts. All these decisions can be made on the basis of available domain knowledge, and mostly rely on of<sup>fi</sup>cial regulations and proven response protocols. On the other hand, only a small number of decisions are really success-critical and inherently complex, requiring a high level of attention by emergency managers. Most of them concern however only three aspects: (i) the selection among alternative intervention plans suitable to face a speci<sup>fi</sup>c situation, (ii) the de<sup>fi</sup>nition of a new plan in front of rare, atypical events for which a standard operative practice does not exist, and (iii) the allocation of resources, generally largely insuf<sup>fi</sup>cient, to the activities to be carried out. According to these observations, a novel decision support paradigm is advocated, based on the following two main assumptions:

![](/api/attachments/ZDWTNN8R/fulltext/images/def07e866ce659befa07469cd756393e002c10fd48b476e45e932742d51a6546.jpg)  
Fig. 3. The emergency scenario.

• for all non-critical decisions a normative support paradigm is appropriate; existing regulations and practical experience provide a rich and reliable knowledge base for decision making in all simple cases; such knowledge can be effectively coded into intervention plans that specify the best course of actions in front of an event; decision makers only need to approve – or reject – the intervention plans proposed by the DSS and their activity becomes simpler and faster;

• for critical decisions concerning the selection between alternative intervention plans, the de<sup>fi</sup>nition of new plans, and the allocation of resources to the activities to be carried out, decision makers are left free to <sup>fi</sup>nd the best solution resorting to their own knowledge and experience; in this case a focused informative support paradigm is appropriate: context-dependent and timely information can help decision makers improve the quality of their decisions and, at the same time, cope with improvisation [24].

The resulting approach to decision support is therefore a composite one, based on two different paradigms that apply to different decision making contexts according to their complexity, as suggested in [37].

## 5. Understanding the domain

Domain understanding aims at acquiring all the knowledge about the speci<sup>fi</sup>c competence domain of the DSS necessary to:

• de<sup>fi</sup>ne the organizational structure of the collaboration context where the DSS will be used;

• identify the decision support objects, that is, the entities on which emergency managers work in their activity and that will constitute the data on which the DSS will operate.

Again the knowledge acquisition methodology illustrated in Section 2.2 has been applied with the support of two knowledge engineers. In the elicitation step, seven domain experts have been involved, representing the heterogeneous community of professionals in charge of managing a pandemic <sup>fl</sup>u emergency, from veterinary and medical prevention, to primary health care and emergency assistance, home care and nursing service, socio-sanitary activities, and public safety. Two questionnaires have been <sup>fi</sup>rst submitted to domain experts: the former focused on the needs and goals of domain experts and on the organization of the emergency management unit, the latter collected information on databases and documents that emergency managers usually exploit in their job. Afterwards, knowledge engineers focused on deep knowledge [31]; naturalistic observation and focus groups were of great help in this activity.

The modeling step included a detailed task analysis, to identify established procedures and best practices relevant to emergency management. Domain experts have been involved, through individual and group interviews, in identifying the signi<sup>fi</sup>cant events that might occur in each pandemic phase, the actors in charge of managing the emergency, their roles and responsibilities, as well as the plans to coordinate and manage the response to the emergency.

The integration step was carried out through focus groups, aimed at identifying and solving substantial or apparent divergences among domain experts, and to merge different perspectives into a coherent frame. Re<sup>fi</sup>nement included several rehearsal activities and, often, a return to elicitation, modeling or integration steps. Eventually, validation was carried out at the end of the knowledge acquisition process, when the domain model was complete, stable, and veri<sup>fi</sup>ed through an extended try-out activity.

## 5.1. Organizational structure

From the domain analysis carried out it emerged that a hierarchical organization is necessary for successful emergency management. Four issues support the need for a hierarchy:

• a rational assignment of roles and tasks to the various components of the emergency management unit;

• a clear separation of responsibilities;

• a precise de<sup>fi</sup>nition of the information <sup>fl</sup>ow;

• an effective command chain between managers with different roles and, especially, between the emergency management unit and the intervention staff.

The analysis of the domain has shown that the management of a health emergency involves the following main levels:

• the central level, constituted by a task force, where all the departments and the directions of the health authority involved in emergency management are represented; on the basis of the events occurred, the task force decides the intervention plans to be carried out, follows their execution, and monitors the evolution of the emergency situation over time;

• the territorial level, represented by the branches of the health authority active in the geographical area involved in the emergency; this level is in charge of implementing the intervention plans suggested by the central level, by identifying the operative units and the resources necessary to carry out the individual activities prescribed by the plan; the territorial branches also manage the information <sup>fl</sup>ow from the <sup>fi</sup>eld to the task force;

• the operative level, including the units in charge of carrying out the speci<sup>fi</sup>c actions de<sup>fi</sup>ned by the running intervention plans and of providing the relevant feedback to the territorial branches.

## 5.2. Decision support objects

Decision support objects are the abstract entities on which emergency managers work in their activity and, at the same time, the raw material on which the DSS operates. In general terms, decision support for emergency management can be grounded on three fundamental entities, as described below.

## 5.2.1. Events

An event is any fact happening at a certain instant and in a certain place in the emergency <sup>fi</sup>eld, which is signi<sup>fi</sup>cant to the emergency management process. This concept includes not only the speci<sup>fi</sup>c events that originate the emergency (an earthquake shock, an epidemic viral infection, a terrorist attack, etc.), but also their consequences (damages to a high risk factory, pollution of water, unavailability of communication networks, etc.) and the effects of the actions undertaken by the intervention staff in order to face the emergency (restoring an electric power facility, activating medical assistance to injured persons, executing safety checks to damaged buildings, etc.). In our case study 14 types of primary events have been identi<sup>fi</sup>ed, which represent the original events that occur in a pandemic emergency and that need to be managed. Examples of primary events are: suspected outbreak of avian in-<sup>fl</sup>uenza in a poultry farm, human case exposed to risk of contagion, suspected human case, presence of a suspected human cluster, and need for a mass vaccination.

## 5.2.2. Plans

A plan is a formal description of an intervention procedure that should be carried out in order to face a speci<sup>fi</sup>c event. A plan speci<sup>fi</sup>es the actions that must be executed and the relevant control <sup>fl</sup>ow; actions can be executed sequentially or in parallel, can be controlled by the occurrence of conditions, and can be repeated until a certain condition is veri<sup>fi</sup>ed. Plans may also include information about the resources required to execute them and the expected completion time. Plans are intended to code all available knowledge on emergency management, including regulations, best practices and practical experience. In general, the relationship existing between events and plans is a partial many-to-many relation: several events may call for the execution of the same plan, while some events might be associated with more than one plan potentially appropriate to manage them; <sup>fi</sup>nally, some events might have no associated plan. Therefore, plans implement a form of mostly normative support, based on the best available knowledge, which applies to all cases where a proven solution is known. However, they leave the emergency managers completely free to deal with complex cases, for which no intervention plans exist or the availability of more than one possible plan calls for a choice. As a whole, 20 intervention plans in response to the 14 types of primary events have been identi<sup>fi</sup>ed. Examples of plans are: emergency vaccination plan, human resource shortage plan, vaccine virus distribution plan, plan for management of a suspected or con<sup>fi</sup>rmed human case, and nursing home emergency plan.

## 5.2.3. Resources

Each action of a plan requires the availability of speci<sup>fi</sup>c resources to be executed. In general terms, a resource may be characterized by a type, a place where it is available, and a quantity. Moreover resources can be consumable (a speci<sup>fi</sup>ed quantity of the resource is consumed when it is used) or reusable (the resource may be reused as soon as it becomes available after use). Finally, resources can be classi<sup>fi</sup>ed into human resources, material resources, and information resources. In the HEALTHREATS project, the following main human resources have been identi<sup>fi</sup>ed: health authority staff, physicians, practitioners, nurses, and social workers. Material resources have been classi<sup>fi</sup>ed into several classes, including beds in hospitals and other healthcare structures, anti-viral drugs, vaccines, individual protection equipment, diagnostic kits, material for disinfection, and other drugs. Finally, information resources include two classes of objects: reference documents and fill-in forms. Reference documents are intended to provide general informative support to the users and include, for example, norms, of<sup>fi</sup>cial recommendations, and operative procedures. Fill-in forms are aimed at generating the technical reports necessary to assure a correct and timely communication with the involved institutions. Fill-in forms must re<sup>fl</sup>ect local reporting practices of the speci<sup>fi</sup>c domain at hand and can be downloaded and completed by emergency managers whenever necessary. Both reference documents and <sup>fi</sup>ll-in forms are associated with the speci<sup>fi</sup>c situations where they should be used, in such a way as to be presented to the users in the right moment and in the right context.

## 6. Characterizing the users

The third phase of the knowledge-centered methodology aims at identifying and characterizing the user classes that will utilize the DSS and at eliciting their interaction requirements. In the HEALTHREATS project, a team, including two knowledge engineers, two human–computer interaction specialists, eight representative users and seven domain experts, has carried out this phase.

First of all, seven classes of users were identi<sup>fi</sup>ed, as shown in Table 2. Then, the interaction scenarios between the users belonging to the identi<sup>fi</sup>ed classes and the DSS have been speci<sup>fi</sup>ed. Eight use cases, divided into <sup>fi</sup>ve normative use cases and three informative use cases, have been designed; initially they have been documented in natural language according to a pre-de<sup>fi</sup>ned template and later, after detailed rehearsal and re<sup>fi</sup>nement with users and domain experts, through formal UML diagrams [14]. Finally, attention has been focused on the interaction patterns between the users and the DSS; these aspects have been represented through <sup>fi</sup>ve UML activity diagrams.

## 7. Analyzing the functions

Finally, the fourth phase of the knowledge-centered methodology focuses on the detailed speci<sup>fi</sup>cation of the functional requirements of the DSS, which constitute the fundamental reference for system development. This phase has been organized in two steps: the former devoted to the analysis of general requirements and the latter to the elicitation and modeling of knowledge about events and intervention plans.

## 7.1. General requirements

Two software designers with the collaboration of managers, domain experts and users have identi<sup>fi</sup>ed 77 functional requirements, divided into 8 areas: (i) management of events, plans, and actions; (ii) information about the emergency situation; (iii) management of material resources; (iv) management of human resources; (v) management of information resources; (vi) geographical mapping; (vii) management of knowledge and data bases; and (viii) system and user administration. Due to the high number of requirements identi<sup>fi</sup>ed and to the limited resources of the project, three classes of priorities have been de<sup>fi</sup>ned: ‘mandatory’, ‘advanced’, and ‘nice to have’.

## 7.2. Modeling of events and plans

Three knowledge engineers, seven domain experts, two managers and four users have collaborated to the elicitation and modeling of knowledge about events and plans already identi<sup>fi</sup>ed in the phase of domain understanding (see Sections 5.2.1 and 5.2.2). Initially, seven individual interviews with domain experts allowed knowledge engineers to analyze all possible events and to model the relevant intervention plans. Since intervention plans may refer to various types of documents (for example, operative procedures to be followed or report forms to be <sup>fi</sup>lled in) or to external data sources (typically, databases containing information about the emergency scenario), knowledge about all these kinds of external references has been elicited as well, and properly associated to the relevant plans. In a second iteration of the knowledge acquisition cycle, four individual interviews have been carried out with the aim of deepening knowledge about plans and completing their representation. Finally, two group interviews with domain experts, managers and users have been devoted to re<sup>fi</sup>ne and validate the whole set of events and plans collected.

User classes and their main tasks.

<table><tr><td>User role</td><td>Organization level</td><td>Tasks</td></tr><tr><td>Event manager</td><td>Operative level</td><td>- Collecting input information for the DSS from the emergency field or from external sources</td></tr><tr><td>Central emergency manager</td><td>Central level</td><td>- Identifying and instantiating intervention plans- Requiring the execution of a new plan by a local emergency manager- Monitoring plan execution- Managing requests for the execution of a new plan submitted by local emergency managers</td></tr><tr><td>Local emergency manager</td><td>Territorial level</td><td>- Executing intervention plans- Monitoring plan execution- Requiring the execution of a new plan or stopping a running plan- Managing resources available in the relevant territorial branch</td></tr><tr><td>Field operator</td><td>Operative level</td><td>- Executing the actions prescribed in the running intervention plan- Providing the local emergency manager with the results of the actions undertaken</td></tr><tr><td>Resource allocation manager</td><td>Central level</td><td>- Updating and monitoring allocation of resources in the various territorial branches</td></tr><tr><td>Knowledge administrator</td><td>Central level</td><td>- Managing DSS knowledge bases</td></tr><tr><td>System administrator</td><td>Central level</td><td>- Managing user accounts and user groups- Providing operative support during DSS operation</td></tr></table>

Plans have been represented in BPMN (Business Process Modeling Notation) [43], which proved to be suitable both for domain experts and knowledge engineers, thus constituting an effective communication and knowledge sharing tool. BPMN includes all the control primitives necessary to model complex processes, such as sequence, selection, iteration, and parallel execution; moreover, it can be compiled into executable computer code, thus making the implementation of the DSS easier. For example, Fig. 4 shows the “Plan for the surveillance of human subject exposed to risk of pandemic virus” associated with the primary event “Human case exposed to risk of contagion”. The start event of the plan is represented through a small circle (at the left in the example), while each rectangle denotes either an action to be carried out or a new plan to be activated (in the example, the “Plan for the management of a suspected or con<sup>fi</sup>rmed human case”). A diamond with a cross represents an exclusive gateway, that is a choice among a set of possible alternatives (in the example, the left-most exclusive gateway asks to verify the presence in the emergency environment of children attending public schools: if this turns out to be true, the action “Apply measures to restrict presence of children in the emergency environment” has to be carried out, otherwise the plan continues with the next action). Other primitives (not included in the example) allow representing inclusive decisions and parallel executions (with fork and join symbols). Actions may refer to documents or to external data sources; to denote such references, colored data objects are used; in particular, red data objects (as shown in the example) refer to procedures, standards, or of<sup>fi</sup>cial regulations, to be applied or taken into account during the execution of an action.

## 8. The DSS prototype

On the basis of the design developed according to the knowledgecentered process described in the previous sections, a web-based DSS prototype has eventually been developed. Its three-layer architecture is shown in Fig. 5.

The user interface layer is in charge of generating the web pages that allow users to access the functionalities of the DSS made available by the application layer.

The application layer is composed of four modules. The data access module and the document access module include the logical components in charge of implementing informative support. The administration module provides the functions necessary to manage all data, document, and knowledge bases of the DSS. The DSS core module is the heart of the DSS and is grounded on a knowledge-based reasoning engine. It is in charge of providing the speci<sup>fi</sup>c normative support necessary to aid emergency managers in their job; more precisely, in front of events occurring in the emergency <sup>fi</sup>eld, it suggests the most suitable intervention plans and offers support to their correct and effective execution (see [13] for more details).

The knowledge and data layer includes three components: the data base comprising the available resources and their allocation, the statistical data about the emergency, and the geographical data concerning the emergency environment; the document base containing all the documents relevant to emergency management; and the knowledge base that stores the domain knowledge on which the operation of the DSS core module is based, namely: plans, actions, event–plan associations, and resource–action relations.

From a technical point of view, the DSS has been implemented on the Java Enterprise Edition (Java EE) platform. The user interface layer is build upon the Apache web server that manages the request and generation of web pages. The application layer includes the application logic running in the JBoss container. The knowledge and data layer consists of a set of MySQL relational databases.

To develop DSS user pages, widely-accepted human–computer interaction design patterns for web applications have been adopted [41], with the aim of presenting support information – both informative and normative – in a clear and as far as possible ef<sup>fi</sup>cient way, thus facilitating interaction and enhancing usability. While different pages are necessary for the various user roles and tasks, a common basic structure has been replicated in all user pages to ensure consistency and support ease of use. A generic page includes the following fundamental elements, highlighted in Fig. 6 that shows the home page of the DSS: (1) the page header with the logo of the DSS, which also constitutes a link to the home page; (2) the main menu bar, which is different for each user role; (3) the “signed in as” area, with the username of the user logged in; (4) the page title; (5) a brief subtitle describing the page content; (6) a welcome message (just for the home page);

![](/api/attachments/ZDWTNN8R/fulltext/images/49cf706c94e41aab92c8d8ec864c16f62ae643891332f8b555c318284bd0dd73.jpg)  
Fig. 4. Plan for the surveillance of human subject exposed to risk of pandemic virus.

![](/api/attachments/ZDWTNN8R/fulltext/images/ae351bf8ecf524203cf92d09e006fa38c8b28db7b40be64e3af41fd287a25b44.jpg)  
Fig. 5. The DSS architecture.

(7) the main area, which depends on user role and system state; and (8) the footer, with the system version and the link to the project web site.

## 9. DSS evaluation

## 9.1. The quality characteristics

After DSS development, evaluation with end users was carried out, focusing both on the quality of user interaction with the DSS and on the capability of the DSS of supporting collaboration among users.

As to the evaluation of user–DSS interaction, attention has been centered on usefulness and usability, generally considered the milestones for system acceptability [26] with a direct impact on the satisfaction of user needs. Usefulness is concerned with the question whether the system meets user expectations. Speci<sup>fi</sup>cally, it assesses implemented DSS functions against the intended requirements of the users. Usability faces the question whether users can perform their tasks easily and effectively by exploiting the interaction tools offered by the DSS.

To evaluate user-to-user interaction through the DSS, only one global characteristic has been considered, namely collaboration effectiveness, which represents the degree to which the DSS can support effective and ef<sup>fi</sup>cient collaboration among the persons involved in emergency management.

## 9.2. Evaluation methods

## 9.2.1. Assessing usefulness

The following methodology, an extension of questionnaire-based methods [23], has been adopted to carry out usefulness assessment:

1. An evaluation team was <sup>fi</sup>rst de<sup>fi</sup>ned, including a set of real users in charge of assessing the implemented DSS functions.

2. A set of test cases related to the implemented requirements was selected and assumed as a reference for the evaluation.

![](/api/attachments/ZDWTNN8R/fulltext/images/5858e8cb700189e08652898f3ac0ac7875f8943b9c3e09154f66e65eb41f6530.jpg)

3. An indicator for usefulness was then de<sup>fi</sup>ned as a triple USF= bUSF/man, USF/adv, USF/nth>, where USF/man, USF/adv, and USF/nth represent the average values of the assessment expressed by the evaluation team about ‘mandatory’, ‘advanced’, and ‘nice to have’ requirements respectively. Users were instructed to express their judgment, for each test case, through a qualitative value in the ordered set {unacceptable, partially acceptable, adequate, satisfactory, completely satisfactory} according to the degree to which the implemented DSS functions meet their intended requirements. These values were then mapped onto the integer scale {1, 2, 3, 4, 5}.

4. A metric for USF was <sup>fi</sup>nally de<sup>fi</sup>ned to aggregate the three components of USF, namely USF/man, USF/adv, and USF/nth, into a global qualitative evaluation:

USF=EXCELLENT iff (USF/man≥4 and USF/adv≥3 and USF/nth≥3) USF=GOOD iff (USF/man≥3 and USF/adv≥2 and USF/nth≥2 and not EXCELLENT)

USF=ACCEPTABLE iff (USF/man≥3 and not (GOOD or EXCELLENT)) USF=POOR otherwise.

## 9.2.2. Assessing usability

To assess usability we have considered robustness, efficiency and memorability, which constitute a subset of the usability dimensions proposed in [26], and that were considered meaningful for the case at hand. The methods for measuring such dimensions are quite standard in the speci<sup>fi</sup>c usability literature and are based on measuring the time and the error rate for completing a selected set of tasks [26]. The following methodology has then been adopted:

1. An evaluation team was de<sup>fi</sup>ned, including a set of real users in charge of assessing DSS usability and a set of reference users perfectly trained and fully familiar with the DSS.

2. A set of test tasks, where a task is intended as a structured set of activities required to achieve a given goal [11], was selected and assumed as a reference for the evaluation.

3. An indicator for usability was then de<sup>fi</sup>ned as a triple USE=bUSE/ eff, USE/rob, USE/mem>, where USE/eff, USE/rob and USE/mem represent the ratio between the average values of the assessment of robustness, ef<sup>fi</sup>ciency and memorability recorded with the real users of the evaluation team while executing the set of test tasks de<sup>fi</sup>ned (user values) and the values obtained with the same set of test tasks by the reference users (reference values). In particular, during the execution of a test task, the time spent to carry out the task and the number of errors made were counted to assess ef<sup>fi</sup>- ciency and robustness respectively; memorability was then evaluated by repeating the execution of the same tasks after a period of inactivity with the system and by measuring the difference in ef<sup>fi</sup>- ciency observed with respect to the <sup>fi</sup>rst experimental session.

The values assigned to USE/eff, USE/rob, USE/mem were then mapped onto an integer scale from 1 to 5 with the following semantics:

1: user value>1.8×reference value

2: 1.4×reference valuebuser value≤1.8×reference value

3: 1.2×reference valuebuser value≤1.4×reference value

4: reference valuebuser value 1.2×reference value

5: user value≤reference value

4. A metric for USE was <sup>fi</sup>nally de<sup>fi</sup>ned to aggregate the three components of USE, namely USE/eff, USE/rob, and USE/mem, into a global qualitative evaluation:

USE=EXCELLENT iff (USE/eff≥4 and USE/rob≥4 and USE/mem≥3) USE=GOOD iff (USE/eff≥3 and USE/rob≥3 and USE/mem≥2 and not EXCELLENT)

USE=ACCEPTABLE iff (USE/eff≥2 and USE/rob≥2 and not (GOOD or EXCELLENT))

USE=POOR otherwise

## 9.2.3. Assessing collaboration effectiveness

The issue of evaluating the collaboration effectiveness of a computer-based system aimed at supporting task-oriented interaction between persons in a speci<sup>fi</sup>c working environment is only poorly considered in current literature. Some approaches simply focus on usability of collaboration systems (see, for example, [30,38]), while others, even if speci<sup>fi</sup>cally considering effectiveness, do not provide objective measures, but only gather comments and suggestions from the users through workshops or focus groups (see, for instance, [4]). Therefore, a new heuristic approach has been proposed, based on three dimensions: pertinence, considered as the property of user-to-user interactions to be focused on the topic at hand, avoiding out-of-scope or immaterial dialogs; correctness, intended as the property of pertinent interactions to convey correct information, avoiding misleading or even wrong messages; and utility, which accounts for the property of correct interactions to concretely contribute to the effectiveness and ef<sup>fi</sup>ciency of the collaborative task.

The following methodology, purposely designed for the case at hand, has been adopted to carry out the assessment of collaboration effectiveness:

1. An evaluation team was <sup>fi</sup>rst de<sup>fi</sup>ned, including a group of real users with the role of assessing DSS effectiveness.

2. A (simulated but realistic) test scenario was de<sup>fi</sup>ned, where the evaluation team was requested to carry out a complete emergency management job.

3. An indicator for collaboration effectiveness was then de<sup>fi</sup>ned as a triple CEF=bCEF/per, CEF/cor, CEF/uti>, where CEF/per, CEF/cor, and CEF/uti represent the average values of the assessment of pertinence, correctness and utility expressed by the users of the evaluation team while taking part in the emergency management job de<sup>fi</sup>ned. In particular, during the execution of their job, users were requested to record the total number of user-to-user interactions occurred, by distinguishing between the interactions that are considered pertinent, correct or useful. CEF/per, CEF/cor, and CEF/uti were then mapped onto an integer scale from 1 to 5 with the following semantics:

```txt
1: Ni<0.6×Nref
2: 0.6×Nref≤Ni<0.7×Nref
3: 0.7×Nref≤Ni<0.8×Nref
4: 0.8×Nref≤Ni<0.9×Nref
5: Ni≥0.9×Nref
```

where:

• for Ni=Nper, Nref=Ntot; for Ni=Ncor, Nref=Nper; and for Ni=Nuti, Nref=Ncor;

• Ntot is the total number of interactions, and Nper, Ncor and Nuti are the numbers of pertinent, correct or useful interactions respectively.

4. A metric for CEF was <sup>fi</sup>nally de<sup>fi</sup>ned to aggregate the three components of CEF, namely CEF/per, CEF/cor, and CEF/uti, into a global qualitative evaluation:

CEF=EXCELLENT iff (CEF/per≥4 and CEF/cor≥4 and CEF/uti≥4) CEF=GOOD iff (CEF/per≥3 and CEF/cor≥4 and CEF/uti≥3 and not EXCELLENT)

CEF=ACCEPTABLE iff (CEF/per≥3 and CEF/cor≥3 and CEF/uti≥3 and not (GOOD or EXCELLENT))

CEF=POOR otherwise

## 9.3. Experimental setting and assessment results

For the assessment of usefulness and usability, two human– computer interaction specialists have organized and conducted an experiment with <sup>fi</sup>ve users recruited from ASL Brescia. A set of 34 cases, covering most of the DSS requirements and comprising the main activities users have to carry out during an emergency situation, was selected and used both as test cases for the assessment of usefulness and as test tasks for the assessment of usability. Experimental sessions have then been carried out under laboratory conditions in which the users could operate in an interruption-free environment.

For the assessment of collaboration effectiveness, a test scenario offered by ASL Brescia (District No. 4 — Valle Trompia) was assumed. The emergency team created for DSS experimentation included one event manager, two central emergency managers, three local emergency managers, and four <sup>fi</sup>eld operators; separate working rooms have been prepared to simulate a distributed setting. The simulation was planned to last for a whole working day. In this period three events occurred – namely “Need for mass vaccination”, “Suspected human case”, “Need for local emergency vaccination” – which triggered seven intervention plans. During the execution of the simulated emergency, a human–computer interaction specialist provided the necessary support for the correct execution of the experimentation, observed the activities of the team, and collected user judgments about collaboration effectiveness.

The <sup>fi</sup>nal assessment of the DSS has provided the results presented in Table 3.

In addition to the evaluation reported above, informal opinions have been gathered from the users during the assessment activities. They indicate that:

• all users judged the DSS useful for their work, not only for the management of emergency situations but also as a personal assistant in their daily activity; the possibility to monitor the execution of plans in a simple and structured way was especially appreciated;

• usability was considered good, with the exception of some complaints for the long time required to carry out some speci<sup>fi</sup>c operations;

• some users pointed out how the DSS can prevent that different people simultaneously make incoherent or even contradictory decisions;

• the majority of the members of the emergency team agreed that the DSS can simplify person-to-person interactions and make them more effective and focused on the goal; moreover, they observed that new management processes induced by the adoption of the DSS make operators feel more involved in a complex organization.

## 10. Discussion and conclusion

The research and experience reported in this paper provide a contribution to the state of the art in collaboration and emergency management from three perspectives. First of all, from the point of view of design methodologies, it proposes a novel knowledge-centered approach to DSS design which is a step further both with respect to user-centered design promoted in emergency management literature [7,29] and DSS research [22,40], and to activity-centered design proposed by Norman [27] for the development of complex interactive systems. In comparison with other approaches to DSS design recently proposed in literature, which are mainly concerned with the development of general frameworks (see for example, [3,10]) or high-level design theories (e.g., [25]), our methodology is based on a rational and structured approach, which exploits sound knowledge engineering methods to carry out all the phases and tasks of the design process. Besides emergency management, it is applicable in any decisionsupport context characterized by the availability of a variety of knowledge sources and by the need of balancing between informative and normative support. The practical application of the methodology is demonstrated with reference to HEALTHREATS project.

Second, the experience reported in the paper has shown the validity – at least in emergency management applications – of the new decision support paradigm adopted, which combines normative and focused informative support. The advantages of this approach are many. First of all, emergency managers can concentrate only on critical cases that de<sup>fi</sup>nitely require their personal competence and experience, relying for all simple decisions on a normative support. This way, their cognitive resources are not dispersed among a number of trivial choices, but can be focused on a small set of crucial aspects. Moreover, for critical decisions, emergency managers do not receive a generic informative support, which might give rise to the undesired result of increasing their information overload, but receive a focused support that provides them with synthetic information speci<sup>fi</sup>cally tailored to the decision problem at hand.

Third, a multifaceted approach to the evaluation of a DSS has been proposed, which considers not only the quality of user–DSS interaction, including usefulness and usability, but also the level of user-to-user interaction through the DSS, namely collaboration effectiveness. This represents a substantial advancement with respect to existing literature that usually focuses only on usability [19] and misses to consider the degree to which a system meets the concrete requirements of an application context. Moreover, the proposed approach has been developed in all technical details necessary for practical implementation and has been actually experimented in the case study considered.

Finally, the present work has disclosed several promising research directions. An important topic, mentioned by more than one user during the experimentation, concerns the capability of the DSS to provide explanations and justi<sup>fi</sup>cations for the intervention plans proposed, showing the goals that have inspired the design of the plan, the reasons behind the actions suggested, the alternatives discarded, and the expected bene<sup>fi</sup>ts. This point might greatly contribute both to increase the level of system acceptance and to support its use as a training tool for improving emergency preparedness.

Another issue concerns the possibility of providing the DSS with a new functional module that enables users, under speci<sup>fi</sup>ed and controlled conditions, to modify existing plans or to edit new plans at run-time in face of unforeseen situations. These plans might then be reconsidered after the emergency is concluded and, after critical revi sion, might become part of the permanent knowledge base of the system or discarded if they revealed to be inappropriate or ineffective. This might expand the <sup>fl</sup>exibility of the DSS, stimulate a more active user participation, and set the background for continuous improvement; moreover, the DSS might support this way the incremental construction of a valuable repository of emergency management knowledge. A last, but not less important, direction for future activity is the extension and experimentation of the DSS to face other types of emergencies; a project in the area of safety in work environments will most probably be launched shortly.

## Acknowledgments

The authors would like to thank all the colleagues who contributed to the de<sup>fi</sup>nition of the knowledge-centered methodology, to the design of the DSS prototype, and to the experimental assessment, in particular Pietro Baroni, Massimiliano Giacomin, and Loredana Parasiliti

Table 3 Assessment results

<table><tr><td colspan="3">Usefulness</td><td colspan="3">Usability</td><td colspan="3">Collaboration effectiveness</td></tr><tr><td>USF/man</td><td>USF/adv</td><td>USF/nth</td><td>USE/eff</td><td>USE/rob</td><td>USE/mem</td><td>CEF/per</td><td>CEF/cor</td><td>CEF/uti</td></tr><tr><td>4.05</td><td>4.40</td><td>4.83</td><td>3.66</td><td>4.61</td><td>4.15</td><td>4.12</td><td>4.89</td><td>3.45</td></tr><tr><td>USF = EXCELLENT</td><td></td><td></td><td>USE = GOOD</td><td></td><td></td><td>CEF = GOOD</td><td></td><td></td></tr></table>

Provenza. The contribution of all partners of the HEALTHREATS project is also recognized.

## References

[1] C. Abras, D. Maloney-Krichmar, J. Preece, User-centered design, in: W. Bainbridge (Ed.), Encyclopedia of Human–Computer Interaction, Sage Publications, Thousand Oaks, CA, USA, 2004, pp. 763–767.

[2] I. Aedo, P. Díaz, J.M. Carroll, G. Convertino, M.B. Rosson, End-user oriented strategies to facilitate multi-organizational adoption of emergency management information systems, Information Processing and Management 46 (1) (2010) 11–21.

[3] D.M. Ahmed, D. Sundaram, S. Piramuthu, Knowledge-based scenario management — process and support, Decision Support Systems 49 (2010) 507–520.

[4] J.E. Bardram, Activity-based computing for medical work in hospitals, ACM Transactions on Computer–Human Interaction 16 (2) (2009) 10:1–10:36.

[5] P. Baroni, D. Fogli, M. Giacomin, G. Guida, L. Parasiliti Provenza, M. Rossi, M. Bohanec, M. Žnidaršič, Supporting DSS acceptability through a user-centered design methodology: experiences in emergency management, in: A. Respìcio, et al., (Eds.), Bridging the Socio-technical Gap in DSS, IOS Press, Amsterdam, Nederland, 2010, pp. 87–98.

[6] F. Burstein, G.R. Widmeyer, Decision support in an uncertain and complex world, Decision Support Systems 43 (2007) 1647–1649.

[7] L. Carver, M. Turoff, Human–computer interaction: the human and computer as a team in emergency management information systems, Communications of the ACM 50 (3) (2007) 33–38.

[8] L.M. Collins, J.E. Powell, C.E. Dunford, K.K. Mane, M.L.B. Martinez, Emergency information synthesis and awareness using E-SOS, Proceedings of the 5th ISCRAM Conference, Washington, DC, 2008, pp. 618–623.

[9] M. Couturier, E. Wilkinson, Open Advanced System for Improved crisiS management (OASIS), Proceedings of the 2nd ISCRAM Conference, Brussels, Belgium 2005, pp. 283–286.

[10] C. De Maio, G. Fenza, M. Gaeta, V. Loia, F. Orciuoli, A knowledge-based framework for emergency DSS, Knowledge-Based Systems 24 (8) (2011) 1372–1379.

[11] D. Diaper, N. Stanton (Eds.), The Handbook of Task Analysis for Human– Computer Interaction, Lawrence Erlbaum Ass, Hillsdale, NJ, USA, 2003.

[12] H. Engelmann, F. Fiedrich, Decision support for the members of an emergency operation centre after an earthquake, Proceedings of the 4th ISCRAM Conference, Delft, NL, 2007, pp. 317–326.

[13] D. Fogli, G. Guida, Enabling collaboration in emergency management through a knowledge-based decision support system, in: A. Respìcio, F. Burstein (Eds.), Fusing Decision Support Systems into the Fabric of the Context, IOS Press, Amsterdam, Nederland, 2012, pp. 291–302.

[14] M. Fowler, UML Distilled: A Brief Guide to the Standard Object Modeling Language, 3rd ed. Pearson Education Inc., Boston, MA, USA, 2004.

[15] S. French, M. Turoff, Decision support systems, Communications of the ACM 50 (3) (2007) 39–40.

[16] M. Giacomin, G. Guida, M. Rossi, A. Viola, A knowledge-based decision support system for crisis management in the <sup>fi</sup>eld of public health, Proceedings Workshop on Intelligent Decision Support in Process Environment Siena, Italy, 2005.

[17] M. Greenwell, Knowledge Engineering for Expert Systems, Halsted Press, New York. NY. USA. 1988.

[18] G.D. Haddow, J.A. Bullock, Introduction to Emergency Management, Butterworth-Heinemann, Amsterdam, Nederland, 2003.

[19] K. Hornbæk, Current practice in measuring usability: challenges to usability studies and research, International Journal of Human Computer Studies 64 (2006) 79–102.

[20] J. Jenvald, M. Morin, T. Timpka, H. Eriksson, Simulation as decision support in pandemic in<sup>fl</sup>uenza preparedness and response, Proceedings of the 4th ISCRAM Conference, Delft, NL, 2007, pp. 295–304.

[21] A. Krakovsky, The role of social networks in crisis situations: public participation and information exchange, Proceedings of the 7th ISCRAM Conference, Seattle, WA, USA, 2010.

[22] S. Lepreux, M. Abed, C. Kolski, A human-centred methodology to decision support system design and evaluation in a railway network context, Cognitive Technology Work 5 (2003) 248–271.

[23] A.M. Lund, Measuring usability with the USE Questionnaire, STC Usability SIG Newsletter 8:2, available at http://www.stcsig.org/usability/newsletter/0110\_ measuring\_with\_use.html 2001, (last visited May 2012).

[24] D. Mendonça, G.E.G. Beroggi, W.A. Wallace, Decision support for improvisation during emergency response operations, International Journal of Emergency Man agement 1 (1) (2001) 30–38.

[25] E.W.T. Ngai, T.K.P. Leung, Y.H. Wong, M.C.M. Lee, P.Y.F. Chai, Y.S. Choi, Design and development of a context-aware decision support system for real-time accident handling in logistics, Decision Support Systems 52 (2012) 816–827.

[26] J. Nielsen, Usability Engineering, Academic Press, San Diego, CA, USA, 1993

[27] D. Norman, Human-centered design considered harmful, Interactions 12 (4) (2005) 14–19.

[28] In: D.A. Norman, S.W. Draper (Eds.), User-centered System Design: New Perspectives on Human–Computer Interaction, Lawrence Erlbaum Ass, Hillsdale, NJ, USA, 1986.

[29] T. Onorati, A. Malizia, P. Diaz, I. Aedo, Interaction design for web emergency management information systems, Proceedings of the 7th ISCRAM Conference, Seattle, WA, USA, 2010.

[30] D. Pinelle, C. Gutwin, Task analysis for groupware usability evaluation: modeling shared-workspace tasks with the mechanics of collaboration, ACM Transactions on Computer–Human Interaction 10 (4) (2003) 281–311.

[31] M. Polanyi, The Tacit Dimension, Rouledge & Kegan Paul, London, UK, 1967.

[32] Project 196320, An integrated decision support system for crisis management, supported by Regione Lombardia, Italy, FSE, Misura D4, November 2004–December 2005.

[33] Project 2006203, HEALTHREATS — Integrated Decision Support System for Health Threats and Crises Management, Supported by the European Union, Executive Agency for Health and Consumers, May 2007–September 2010.

[34] W. Raskob, V. Bertsch, J. Geldermann, S. Baig, F. Gering, Demands to and experience with the decision support system RODOS for off-site emergency management in the decision making process in Germany, Proceedings of the 2nd ISCRAM Conference, Brussels, Belgium, 2005, pp. 269–278.

[35] C. Sapateiro, P. Antunes, An emergency response model toward situational awareness improvement, Proceedings of the 6th ISCRAM Conference, Goteborg, Sweden, 2009.

[36] D. Schuler, A. Namioka (Eds.), Participatory Design, Principles and Practice, Lawrence Erlbaum Ass, Hillsdale, NJ, USA, 1993.

[37] D.J. Snowden, M.E. Boone, A leader's framework for decision making, Harvard Business Review 85 (11) (November 2007) 68–76.

[38] M. Steves, E. Morse, C. Gutwin, S. Greenberg, A comparison of usage evaluation and inspection methods for assessing groupware usability, Proceedings Int. Conf. on Computer-Supported Cooperative Work (CSCW 2001), ACM Press, New York, 2001, pp. 96–105.

[39] J. Sutton, L. Palen, I. Shklodvski, Backchannels on the front lines: emergent uses of social media in the 2007 Southern California wild<sup>fi</sup>res, Proceedings of the 5th ISCRAM Conference, Washington, DC, 2008, pp. 624–632.

[40] K.A. Thursky, M. Mahemoff, User-centered design techniques for a computerized antibiotic decision support system in an intensive care unit, International Journal of Medical Informatics 76 (2007) 760–768.

[41] J. Tidwell, Designing Interfaces. Patterns for Effective Interaction Design, O'Reilly, Sebastopol, CA, USA, 2005.

[42] M. Turoff, S.R. Hiltz, C. White, L. Plotnick, A. Hendela, X. Yao, The past as the future of emergency preparedness and management, International Journal of Information Systems for Crisis Response and Management 1 (1) (2009) 12–28.

[43] S.A. White, D. Miers, BPMN Modeling and Reference Guide, Future Strategies Wallsend, UK, 2008.

[44] WHO — World Health Organization, Global In<sup>fl</sup>uenza Preparedness Plan (WHO/CDS/CRS/GIP/2005.5), 2005. (Geneva, Switzerland).

[45] M.H. Zack, The role of decision support systems in an indeterminate world, Decision Support Systems 43 (2007) 1664–1674.

Daniela Fogli received the Laurea degree in Computer Science from the University of Bologna, Italy, in 1994 and the Ph.D. degree in Information Engineering from the University of Brescia, in 1998. From 1998 to 2000, she was a post-doc grant holder at the Joint Research Centre of the European Commission. Since 2000, she is assistant professor at the Department of Information Engineering, Faculty of Engineering, University of Brescia, Italy. She has published more than 70 scienti<sup>fi</sup>c papers. Her research interests include methods for designing complex interactive systems, meta-design, end-user development, web usability and accessibility, and system personalization through artificial intelligence technigues. She performed her research activity in collaboration with scholars of many Italian universities and of the National Research Council. She also collaborated with the members of the Center for LifeLong Learning & Design (L3D), University of Colorado at Boulder, USA, where she has been a visiting scholar several times. She served as short papers co-chair of the ACM Conference Advanced Visual Interfaces (AVI'06) and doctoral consortium co-chair for the 3rd International Symposium on End-User Development (ISEUD 2011). She is member of SIGCHI Italy (the Italian Chapter of ACM SIGCHI — ACM's Special Interest Group on Computer–Human Interaction).

Giovanni Guida received the Laurea degree (Dr.Ing.) in Electronic Engineering (major in computer science) from Politecnico di Milano, Italy, in 1975.

He is currently a full professor of Computer Science at the Faculty of Engineering, University of Brescia, Italy and a principal investigator of the “Knowledge Engineering and Human–Computer Interaction” research group at the Department of Information Engineering of the University of Brescia.

Previously, he taught at the Politecnico di Milano (1984–1986) and at the University of Udine (1979–1983, 1987–1990), where he founded and directed a research group in the area of arti<sup>fi</sup>cial intelligence for ten years (1980–1990). He has been the director of the computing center of the University of Udine (1984–1985, 1989–1990) and of the University of Brescia (1991–1993).

His present research interests include knowledge-based systems, decision support, uncertain reasoning, argumentation theory, human–computer interaction, knowledge engineering methodologies and applications, collaboration and cooperation, and web site design. Formerly, he has carried out research activity in the <sup>fi</sup>elds of formal languages, programming languages and systems, problem solving and searching, natural language processing, and intelligent information retrieval.

Dr. Guida is active as an independent consultant in the area of information technology applications and knowledge management. He teaches advanced courses and conducts executive seminars in the <sup>fi</sup>eld of emerging information technologies
