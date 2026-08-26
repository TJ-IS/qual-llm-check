---
otero_id: 17624
otero_key: "DD82MCBB"
title: "Organizational activity support systems"
authors: "Dubravka Ćećez-Kecmanović"
year: "1994"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(94)90053-1"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Organizational activity support systems

Dubravka Ćećez-Kecmanović

Department of Informatics, Faculty of Electrical Engineering,
University of Sarajevo 71000 Sarajevo, Lukavica,
Bosnia and Herzegovina

Planning, performing and evaluating group processes in all kinds of organizations are challenging new applications of information and communication technologies (IT). Institutionalized group processes, called activities, are the subject of inquiry with the aim of creating IT-based support. Activities are defined in a social context: they are performed as conversations between human beings. By performing activities participants affect and change the social context. Therefore they heavily rely on means of communication and the availability of relevant organizational knowledge. This paper introduces the concept of the Organizational Activity Support System (OASS) as a new means for knowledge communication and conversation between participants in activities. The language for computer-mediated interaction and the formal model of activity, provided by OASS, are presented, illustrated by the example of a meeting of a governmental body.

Keywords: Institutionalized activity; Normatively regulated activity; Activity modelling; Organizational knowledge; Activity support system; Organizational activity support; Computer mediated activity

![](/api/attachments/DD82MCBB/fulltext/images/87722c6914515535242567374220b1112becdb2cff81e2a804c3bca500d2b65f.jpg)

Dubravka Ćećez-Kecmanović is Professor of Information Systems at the Department of Informatics and Associate Dean of the Faculty of Electrical Engineering, University of Sarajevo. She received a B.S. in Electrical Engineering from the University of Sarajevo, an M.S. in Systems Sciences from the University of Belgrade, and a Ph.D. in Information Systems from the University of Ljubljana. She has conducted a number of research projects and published papers on methodologies of information systems development and evaluation, social information systems and decision support systems. Her current research interests include organizational knowledge systems, application of non-standard logics in modelling organizational processes and computer-mediated communication between social agents. She is a member of IFIP WG 8.3.

## 1. Introduction

The supporting of organizational processes by information and communication technologies nowadays assumes rather sophisticated data and information processing, decision modelling, text processing and document management systems, image and voice processing, as well as electronic network communication and message interchange. The convergence and merging of these technologies are considered to be a main-stream development for decision-making support in organizations.

The convergence and merging of technologies are often treated from a technical point of view: different techniques, models, tools, devices, packages and systems are interconnected in order to provide various kinds of services in organizations. These interconnected technologies create a specific technological environment for organizational activities. Considerable evidence could be found to support the assertion that this new technological environment improved the transmission of information throughout an organization and its communication with the outside world, and also increased the efficiency of decision-making processes in general. However, the very nature of decision making has not been changed. For a more substantial influence on organizational processes, more profound penetration of information and communication technologies into these processes is necessary. Besides providing new tools and services for different kinds of data/text/message/document processing and management, information and communication technologies are creating new possibilities for doing things better and in a different way.

## 1.1. Background

An excellent example of innovation is the research and development of various systems to support group processes. Electronic Meeting Systems (EMS) provide tools to support genuine group activities and decision-making, such as electronic brainstorming, idea organizer, issue analyzer, voting support, alternative evaluator, policy formation and information management, [13,26,33]. Other approaches to group activity support have been developed under the names Computer-Supported Cooperative Work (CSCW), Group Decision Support Systems (GDSS), and Groupware [2,14,20,27].

Group processes and decision-making can be supported as a process and process structure or as a task and task structure [13]. Process and process-structure support includes the provision of language, communication channels and means for process structuring and conducting. Tasks are traditionally supported by quantitative models and decision modelling tools, and recently also by qualitative reasoning models. Ellis emphasizes the difference between these two domains by two terms: GPSS for group process support systems and GDSS for group decision support systems [17].

The research of organizational activities, presented in this paper, concerns problems within the domain of group process and process-structure support.

An example of process oriented decision support is the system called POLYMER which supports decomposition of goals into tasks, sequencing of tasks and cooperation of agents in performing their tasks $[3,4]$ . It assists agents in the execution of actions in different problem situations and initiates negotiation process when needed.

An innovative approach to process support for a specific type of activities—contracting processes was introduced in $[15,16,21–23]$ . A computer-mediated contracting system is proposed to support legal conversations ‘on a performative network’ in the process of formation and execution of contracts. It keeps track of the changes of deontic states and records their consequences such as obligations, permissions and prohibitions.

The problems of activity performance may be considered within wider, semiological framework introduced by Stamper [30-32]. This framework extends classical semiotics and distinguishes six levels of consideration of signs: physical, empirical and syntactical level, related to information technologies, and semantics, pragmatics and social world level, related to human information function. The problem of activity support is located at the level of pragmatics “concerned with relationships between signs (as meaningful utterances) and the behavior of responsible agents, in a social context” [32].

In considering the particular problem of institutionalized activities I emphasize signs used for action and the social context in which they have meaning and produce changes. By focusing on the pragmatic problems of signs I also refer to the problems of meaning (semantics level) and social consequences.

Activities in organizations are performed through the interaction individuals as role-playing subjects called social agents. Their actions, more or less formal, more or less structured, are social in nature. By this I emphasize the influence of socially determined constraints on human behavior and conversely the influence of human actions on social environment $[19,25]$ . Relevant to this analysis is the concept of normatively regulated action, as defined by Habermas within the lines of his theory of communicative actions $[18]$ . The concept of normatively regulated action presupposes relations between the agents and exactly two worlds: “the objective world of existing states of affairs and the social world to which the agent belongs as a role-playing subject” $[17]$ , p. 88). This explains why classical framework, supposing only the existence of the objective world, is not sufficient in considering the institutionalized activities.

## 1.2. Purpose and organization of the paper

This paper focuses the social nature of actions in group processes and the structure of these processes as interactions of social agents. A group process performed as the institutionalized conversation of social agents intended to attain an end or to bring about the occurrence of desired state will be called an activity. Institutionalized conversation between social agents exhibits some regularities concerning the types of agents and their responsibilities and obligations, the structure of a conversation process and conditions for successful conversation and validation of outcomes (such as decisions, documents etc.). These regularities are specified by norms, that govern the behavior of agents and determine the meaning and effects of activities in a social context. The performance of an activity is expected to comply with the norms, applicable to respective activity type. The activities are judged according to their rightness: whether they are in accord with existing norms, or deviate from them.

The empirical research of institutionalized activities in different kinds of organizations (public administration, health care, social services, banks and insurance, corporations) provided significant evidence for the investigation of requirements for formal, computer based support of activity performance $[5,7–9,11]$ .

The typical problems found in the practical performance of activities are:

\- What is the meaning of an action an agent bring about in a particular conversation?

\- Is an agent authorized to execute the particular type of action?

\- Who is responsible/obliged to take an action in a certain situation (state of an activity)?

\- Is an action adequate with the respect to the actual situation?

\- What commitments and/or obligations are implied by an action?

\- Does an activity conform to regularities? If it does not, what are the consequences? Who is accountable for its verification and validation?

accountable for its verification and validation? These problems suggest the motives to analyze the nature of organizational activities and the needs of agents in performing and conducting activities in practice. The performance of activities depends on agents competence and ability to understand the social context and how it is affected by their actions. The availability and transferability of organizational knowledge is the basic prerequisite for successful conversation and execution of activities $[5,10,12]$ .

The purpose of this paper is to present some research results of the investigation of organizational knowledge structures assumed by agents and to introduce the concept of the Organizational Activity Support System (OASS) as a generic name for a new technological medium through which organizational knowledge will be generated and transmitted to agents in order to enable their successful conversation and coordination in the performance of activities. The core element of OASS – the Formal model of activity and its role in activity performance will be discussed in detail. (Logical foundation of the Model in Predicate, Deontic and Temporal logics is elaborated in [10,12]).

The paper is organized into seven sections. Section 2 provides the discussion of different approaches to activity analysis and computer-based support in activity performance. Organizational knowledge structures assumed in activity performance are briefly examined in Section 3. The analysis of the needs of agents that take actions and perform conversations and the requirements for activity modelling in OASS are summarized in Section 4. Section 5 explains the purpose of OASS and gives detailed description of the Formal model of activity. The example of a meeting activity of a governmental body illustrates a formal language based on logic and the way linguistic actions are communicated among agents. The different roles that OASS might play in organizations are examined in Section 6. The final section summarizes the main contributions of the paper and indicates future research directions.

## 2. Different approaches to activity analysis

Traditionally, organizational activities are recognized as sources of data flows or as locations of information usage and human information processing. As a consequence, when information flows are modelled, the activities are represented either as points of data generation or as points of information consumption. The activities are generally understood as places of transformation of information flows. Information modelling concerns data structures which represent the objects, attributes and relationships relevant for the activities to be performed.

The languages used for modelling in various methodologies for information systems development (e.g. ISAC, SADT, DFD) have appropriate features, formal statements, graphical symbols and natural language specifications, to represent the content of input and output information flows and the data processing part of the activities. The database is designed to recognize data inputs, perform updates, and generate the information required for the performance of various human activities.

The other type of information flow is created by documents input to, and output from, the activities. When document flows are represented in an office information system, the content of a document remains a black box for the system, while conveying information to the users in a natural language. Unless some natural language processing is provided, the only means by which its content is understood (by the system) are the data supplied with the document (such as type of document, source or generator, confidence level, date of generation etc.) and the keywords or descriptors used to delineate its scope.

This is illustrated by the example of a meeting of a governmental body. Fig. 1 shows a model of a meeting consisting of subactivities: meeting scheduling and preparation, meeting execution, and record keeping and dissemination of information. The model is documented by A-graph according to the ISAC method [24]. This is an example of activity modelling which portrays an activity as a point of information consumption and production. The relationships between the (sub)activities are described as information and document flows. (Deeper analyses gives detailed specification of these information sets and information processing part to be performed by computer.)

A - graph  
![](/api/attachments/DD82MCBB/fulltext/images/6ffd3d0f0ef8dc96d8200b3eb9e43b4d0a199c9bbb89dc5a5124098afd65bc23.jpg)  
Fig. 1. The activity ‘Governmental Body Meeting’ described according to the ISAC method [24].

The question is whether information flows coming in and out of the activities capture the relevant meanings of organizational activities in a sufficiently complete and correct manner. Let us examine for a moment how the activities are defined in a social context and how they are performed.

The activities, in general, are to be performed according to specified norms, by authorized persons, playing certain roles, enabled to take certain actions, under socially determined constraints, subject to time and resources limitations. For an activity to start a triggering action by responsible agent or the completion of some preceding activities, is usually required. Conversely, after an activity is completed certain data and documents are produced, and some commitments and obligations issued, being the conditions necessary for other activities to start. An activity may have possible and obligatory preceding, as well as succeeding, activities.

Besides the data and documents coming out of an activity, the performance of the activity itself is a source of knowledge for its social environment. Consider, for example, the governmental body meeting. It has to be carefully prepared and planned; all initiatives, requests, documents etc., from governmental as well as nongovernmental institutions, have to be properly considered, according to existing rules (which in some cases are established to protect the interests of parties involved); the procedure itself is subject to control and examination by a wider audience (e.g. why something is or is not included into the agenda of a meeting?). How the activities are performed, not merely the fact that they are performed, determines their outcomes (decisions, statements, documents) and whether they will be recognized as justified. In an extreme case of irregular performance, unauthorized actions or misuse of power, the focus of inspection is the way the activities have been executed. In any case of nontrivial human activity the meaning that agents assign to it lies beyond its resulting facts – transactions, data, documents, decisions etc.

From this point of view an activity may be relevant with respect to execution of actions and their sequences, the fulfillment of conditions for successful execution of actions, the agents' authorization for performing actions, time-related interdependence and constraints, requirements concerning document generation, distribution and verification etc. The perception of an activity by both its participants and other agents is not limited by any means to data or documents entering and leaving the activity. Besides this, the meaning is derived from the description of tasks (how they have to be and how they are performed), the procedures involved in taking particular steps, the participation of certain individuals and groups in their proper roles, appropriate involvement of role-holders in the task performance, and the exercise of power within the bounds of their responsibilities, etc. The violation of rules defined by regulations or commonly accepted way of performing an activity has serious implications for its understanding and verification. Even not performing a certain activity when it is required usually has some consequences and in this respect may have meaning for the human beings involved.

Apart from the mere technicalities human activities become meaningful within socially created reality. Consequently, the meaning of an activity is implied by a social context as defined by norms and embodied values. Models of activities, if they are to serve managerial and governmental processes, should capture these socially implied meanings.

## 3. Representation of organizational knowledge

In order to acquire knowledge assumed in the performance of activities it is necessary to identify relevant organizational phenomena and knowledge structures inherent to each of them. First of all any institutionalized activity is embedded in a social context which is specified by norms. It recognizes organizational entities and the respective roles, persons as role holders, patterns of actions and types of activities as well as documents and information and their flows within an activity and between the activities. By instituting norms concerning the existence and behavior of these phenomena, an organization legitimates its activities, and of course, their outcomes.

An organizational entity is an organization, a department, an office, a committee, and the like. Its name, tasks, formal organization structure and relationships with other entities, its constituting procedure and mandate period, are specified by regulations.

Institutionalized activities are based on typification of agents. An agent is a person apprehended not as a particular person but as a role holder. Roles are defined in relation to organizational entities. The standard of a role specifies its area of responsibility and discretion space, its relations to other roles and its rights and obligations for taking actions. Roles are charged with such responsibilities as ‘scheduling a meeting’, ‘accepting/rejecting an item for the meeting agenda’, ‘signing a document’, ‘authorizing somebody for a particular action’ and the like. Standards for roles belong to a segment of organizational knowledge relevant for activity performance.

By bringing about the actions, agents change the state of organizational activities. Action norms define the rules governing the successful execution of a single action, a sequence of actions and the performance of the whole activity. They specify conditions for the activity to start and to be successfully completed. Action norms, like other norms mentioned above, are defined by legal acts. (There are, however, ‘usual ways’ of doing things, unwritten rules, assumed rights and obligations, which make the picture slightly less transparent.)

Although informal, the above description reveals different kinds of knowledge assumed in the performance of activities in an organizational context:

\- organizational entities, (e.g. assembly, government, governmental body);

\- roles (e.g. president of governmental body, minister of industry);

• personnel as role holders (agents);

\- activities performed by agents (e.g. a meeting of assembly, enacting a law);

\- documents and information required and used within the activities and those produced by the activities;

\- norms and legislation entities (such as laws, regulations, rules).

All these different types of entities are of very different natures. The examples of types of entities from state administration are illustrated in Fig. 2.

![](/api/attachments/DD82MCBB/fulltext/images/bc8dcd8eb70dec011e1501ff4622be6e35ea289f85ddb6e6d18d2d9035868e22.jpg)  
Fig. 2. Knowledge representation strata (KRS) for a state administration.

Being a governmental body, for example, implies possessing certain characteristics common to all organizational entities and significant for its recognition, such as organizational character, type of organizational form, area of responsibility, date of constitution, etc. These are characteristics by which an organizational phenomenon is distinguished from other phenomena – roles, personnel, or activities. The set of characteristics of a phenomenon essential for its naming by the given term (e.g. governmental body in Fig. 2) constitutes a signification (SGN) mode of meaning of the term 6. Entities are classified by their essential characteristics.

On the other hand, the meaning assigned to the term ‘governmental body’ also includes the official name, address, superordinate entities to which it reports, its mandate period, the number of its members, what constitutes a quorum, associated roles, such as secretary, vice president and president. Furthermore, the term ‘governmental body’ connotes rules or regulations governing its behavior and types of activities that it performs. The connotation or intention of a term (INT) assigns some habitual properties or relations to a phenomenon named by a given term, that are not essential for its naming or classification.

The essential characteristics that discriminate phenomena of a different nature are called dominant properties. These are e.g. ‘organizational character’, ‘normative or legislative character’, ‘role’, ‘personnel’, ‘activity’ and ‘document’ displayed in Fig. 2. Differentiation of phenomena according to these (and possibly others) dominant properties, referring to different natures, establishes criteria for the partition dimensions of organizational knowledge. The Knowledge Representation Stratum (KRS) is an abstract concept that comprises knowledge structures inherent to the phenomena of a particular nature. In other words, KRS represents knowledge structures typical for one organizational dimension [6]. KRS describes terms with common SGN and INT mode of meaning. In addition, these terms are created from their components by the same type of ‘building mechanism’. Building mechanism generally defines the way a certain phenomenon is created, including norms regulating its existence and behavior.

The meanings of terms are generally shared by agents belonging to the same social world. This is the condition of a rationality in human communications [8], particularly important in institutionalized activities.

The class of terms within the KRS, and its SGN and INT modes of meaning, may be represented by a unique data structure set (e.g. record type or relation). As a result, the requirements for mediation of these two modes of meaning of a term may be successfully fulfilled by using database technology. However, this is not the case with other modes of meaning, specific for a KRS, such as building mechanism and associated norms. These knowledge structures have to be carefully studied for each class of KRS in order to create adequate formalisms and processing means. In the remainder of this paper knowledge structures inherent to activities are examined. The other knowledge structures specific for e.g.

organizational entities, roles and documents are assumed to be known, and are not discussed here (more details can be found in [6,10]).

## 4. Requirements for activity modelling in OASS

The idea of creating the Formal models of activities and developing OASS is motivated by the needs of people to communicate at a level appropriate to the complexity of their tasks. Namely, the more complex the task to be performed, the higher is the required level of communication between individuals concerned [1]. The main goal of implementing OASS is to improve communication among agents so as to attain an adequate communication level for planning, performing and evaluating a single activity and an interconnected set of activities [5]. This implies requirements for communication means – language and models for the representation of activities, their social context and implications. Requirements for activity models will be discussed in this section, and the formal language and model in the next section.

Usually, there is a mutual understanding, at some level of generality, about the purpose of an activity, its structure, performance preconditions, the logical relationships between its actions, document and data inputs and outputs, obligations involved, time constraints etc. This understanding of an activity – what the creators have in mind when designing and instituting an activity – is communicated to the agents, and possibly to others affected by its performance, usually, but not necessarily, by some official document or regulation. This may also be an agreement of the people concerned of what the activity should be and how it has to be performed. The Formal model of the activity has to portray this perception of what ought to exist in reality. In this sense, the Formal model of an activity is required to be prescriptive. Sometimes the prescriptive content of an activity is reached first by the analyst if h/she starts with an analysis of documents concerning organizational regulations and rules.

However, the perceptions of agents involved in a particular activity performance constitute another relevant body of knowledge. The necessity of representing and communicating the meanings of activities attributed by their actors implies requirements for descriptive models of activities. Actually, the same (normative) model of an activity is never the same in practical performance due to differences in conditions, subject matter, different actors, etc. On the other hand, in order to be regular or legal, the practical performance of an activity has to accord with the rules defined by the prescriptive model. The role of supervisors or other authorities is to monitor the execution of activities and compare them to the prescriptive models. They make judgements about the performance and regularity of activities which have serious implications for the justification of their outcomes.

The above argument suggests that OASS have to be able to mediate both the human intention concerning what the activities should be, represented by the prescriptive models of activity types, and the human experience of what they actually are, i.e. the descriptive models of the instances of activity types. These perceptions of activities do not always coincide, which necessitates the distinction between the prescriptive and the descriptive models of activities in OASS.

## 5. Organizational Activity Support System - OASS

## 5.1. The concept of OASS

Understanding of a social context and social implications of the performance of activities is the basic precondition for agents' participation in institutionalized activities. Moreover, agents belonging to a social context have a common interest to behave in a norm-conformative way [18]. On the other hand, for certain institutionalized activities, which include, among other things, human rights protection, legitimate control mechanisms are established. These statements summarize the needs of agents in activity performance and requirements for computer mediated support.

I conceive of the Organizational Activity Support System as a new technological medium for the social construction of reality and distribution of organizational knowledge. In addition to face to face communication, paper-based support and various information/document processing and electronic transmission systems in support of organizational activities, the aim of OASS is to provide new capabilities for creating, recreating and transmitting organizational knowledge. The paradigm behind OASS reverses the classical information system paradigm: instead of ‘representing reality’ in an information system, OASS provides a new medium in which the reality is socially created and changed $[7,10,12]$ .

The nature of computer support OASS is considered to provide is derived from the needs of agents studied in the empirical research of activity performance [7]. The purpose of OASS is to provide:

(a) the language and models for continual social (re)creation of the relevant segment of organizational knowledge;

(b) assistance to agents in understanding social context and how it is affected by their actions; support to agents in planning and conducting activity performance;

(c) a communication medium for performing actions and making their consequences in the social context effective; a mechanisms for testing the correctness of actions in a given normative context;

(d) the evidence and support for testing norm-conformity of activities and justification of their outcomes; learning mechanism for improving normative context;

(e) monitoring of the performance of on-going activities, including prediction and resolution of conflicts between interconnected activities.

The concept of OASS requires new formalisms to express various knowledge structures, as defined in Section 3. Among them, the most complex and dynamic are those expressing the meanings of activities. The Formal model of activity, the core knowledge structure in OASS, is going to be examined in detail in the following subsections.

## 5.2. The formal model of activity

When an agent issues a linguistic expression with an intention to produce change in a social environment, this linguistic expression is called an action. An action may be considered an illocutionary speech act, which has its propositional content and illocutionary force $[28,29]$ . By uttering a linguistic expression, under certain conditions, an agent changes the state of an activity and creates, modifies and deletes commitments and obligations. This is called the successful execution of action.

An action is determined by the agent who performs the action, the action predicate which identifies the type of act and informative elements represented by the arguments of the predicate. The formal expression of a type of action (based on Predicate and Temporal logics $[10,12]$ ) has the following form:

$$
\begin{array}{l} \text {Ai (Agent: action\_predicate(argi1, argi2,...,} \\ \text {argin) ON t)} \end{array} \tag {5.1}
$$

where Ai is denominator of a type of action. Variable t refers to a point in time when the action is executed. (Since action predicate uniquely identifies a type of action, a denominator Ai is redundant; however the short code Ai is introduced to denote an action in the graphical representation of activity).

After the execution of an action an activity changes its state. The concept of state represents stage of performance, identified by a state predicate. The fact that a state Sj of an activity is the case or is true, in some time period, is expressed by a clause:

$$
\begin{array}{r l} \text { Sj } & (\text { state\_predicate } \quad (\arg j 1, \arg j 2, \dots , \arg j n) \\ & \text { IN } (t _ {\text { BEG }}, t _ {\text { END }})) \end{array} \tag {5}\tag{5.2}
$$

where Sj is a state denominator, state\_predicate uniquely identifies a state and arguments (object constants, variables or expressions) represent informative content of a state. The informative content of a state consists of all information generated by the sequence of actions preceding the state. If alternative sequences of actions lead to the same state, then informative contents of the state may be different.

The successful execution of an action causes a change of the actual state. Necessary conditions for successful execution of action causing the change of state and consequences in social context produced by that change are defined by so-called transition rule:

$$
\mathrm{T} ^ {\mathrm{ik}} = \left(\mathrm{Si}, \mathrm{Sk}, \mathrm{Aj}, \mathrm{CD} ^ {\mathrm{ik}}, \mathrm{CQ} ^ {\mathrm{ik}}\right)\tag{5.3}
$$

with the following meaning: When actual state is:

$$
\text { Si } (\text { state\_predicate\_i } (\arg i 1, \dots , \arg i n))
$$

IN(t1 t2))

and action executed:

$$
\operatorname{Aj} (\text { action\_predicate } (\arg j 1, \dots , \arg j m) \quad \text { ON } \quad t)
$$

and conditions CD $^{ik}$ are fulfilled, then the new state is:

$$
\begin{array}{r l} & \text { Sk(state\_predicate\_k(argk1,\ldots,argk1) } \\ & \text { IN(t3,t4)) } \end{array}
$$

and consequences are $CQ^{ik}$ . Conditions $CD^{ik}$ for a successful execution of action include authorization of the agent, time limits for execution, availability of a document, etc. Social consequences $CQ^{ik}$ , implied by the successful execution of action, constitute the performative content of the state Sk.

The informative content of a state is one part of the meaning of a state, the one that can be derived explicitly from actions leading to the state. Complementary to this part is the performative content (meaning) of a state which expresses a change of social relations, obligations, permissions, prohibitions etc., implied by the actions performance. The performative content depends on the type of illocutionary point of the actions performed $[28,29]$ :

\- an action which is an assertive speech act implies agent's commitment and 'latent' obligation to provide argumentation or evidence;

\- an action which is a directive speech act (order, command, request) produces obligation for the agent to whom it is addressed;

\- an action which is a commisive speech act (premise, acceptance, approval) creates an obligation for its agent to perform certain acts in the future;

\- being a declarative speech act an action changes social relations: establishes new roles or role-holders, changes legal status of organizational entities, persons or documents, introduces new rules, obligations, prohibitions etc.

These meanings are not obvious, they are derived from a social context [8-12].

The Formal model of activity is defined by a set action types, all possible states attainable by actions execution and transition rules describing the changes of states:

$$
\mathrm{ACT} = \{\mathscr {A}, \mathscr {S}, \mathscr {T} \}\tag{5.4}
$$

where the set of actions, the set of states and the set of transition rules are:

$$
\mathcal {A} = \{\mathrm{A1}, \dots , \mathrm{An} \}
$$

$$
\mathcal {S} = \{\mathrm{S0}, \dots , \mathrm{Sm} \}
$$

$$
\mathcal {T} = \left\{\mathrm{T} ^ {\mathrm{ij}}, \dots , \mathrm{T} ^ {\mathrm{kl}} \right\}
$$

whose elements are given by (5.1), (5.2) and (5.3) respectively. (Detailed explanation of this model and its logical foundation, together with its further derivatives – the model of activity with recurrence and hierarchical model – are given in [12]).

The real life examples of formal models of activities are usually very complex and difficult to perceive. In order to enable comprehensive and compact representation, suitable for human users, a graphical language for activity representation – ACT NET – is developed $[8–12]$ . A state is represented by a circle, with its name inside, and a transition from one state to another by directed arc, labeled with action causing transition.

Since an important aspect of activity performance is its dynamics, the Formal model of activity includes temporal variables, operators and functions that enable relative and absolute temporal reasoning, based on temporal logics $[10,12]$ .

## 5.3. The example of governmental body meeting

The Formal model of activity and the language used to communicate knowledge about the activity, defined above, will be demonstrated by the example of a meeting of a governmental body (presented in Figs. 1 and 2). The Formal model for the first subactivity in Fig. 1 'Meeting scheduling and preparation' will be examined and partly described in Figs. 3–8. The meeting preparation is enacted by certain persons: for a governmental body meeting these are officers and responsible persons with special discretion. The responsible person is authorized to plan the meeting on date tm, which is denoted as action A1:

A1 (Responsible\_per:

plan\_meeting

(Government\_body, Meeting\_no, tm)

ON t1)

where t1 is the time of action execution. This action causes the transition form the beginning state S0 to the state S1:

S1 (meeting\_planned

(Government\_body, Meeting\_no, tm)

IN (tb1, te1))

provided that the person taking action is authorized to do it and that the action is executed at least 15 days before the meeting date tm.

Furthermore the responsible person takes other actions in order to prepare meeting: h/she specifies the meeting agenda 'AG' (action A2 with action predicate: specify\_agenda) and defines documents obligatory for the meeting (action A4 with action predicate: specify\_obligatory\_documents). Then a responsible person specifies these documents by several actions of the type A3 (action predicate: specify\_document). After that the invitation to the meeting is issued (action A5 with action predicate: issue\_invitation) to the members of the governmental body. The above sequence of actions causes the change of states in the meeting preparation from S0 to S1, S2, S3, S4 and S5 which denotes the state when the meeting can start. The Formal model of activity type Meeting Preparation Model 'MP-1', described by ACT NET, is presented in Fig. 3(a), where A1, A2, A3, A4 and A5 are action types specified in Fig. 4.

The Meeting Preparation Model ‘MP-1’ in Fig. 3(a) shows the smooth sequence of actions A1, A2, [A3] and A4, A5 and A6, which produce a chain of states S1 (meeting planned), S2 (agenda defined), ..., and S5 (meeting to start). Although it describes the main stream of actions in meeting preparation it is incomplete in a sense that it does not include necessary preconditions for some transitions to take place. For example, a meeting cannot be planned without reservation of a room big enough for this meeting. The reservation of a room and its confirmation are examples of interaction with the other activity (Room Allocation Model). Also, the process of meeting preparation is not always so smooth. This is why an extended version of the Meeting Preparation Model ‘MP-2’ is created, presented in Fig. 3(b). The examples of transition rules, from this model, are given in Figs. 5–7. Compared to the first model in Fig 3(a), ‘MP-2’ contains the new state S6 characterized by the definition of documents obligatory for the meeting (according to agenda items), due to the execution of A4, and by the incomplete set of these documents prepared by the responsible agents. After the submission of missing documents (by several actions A3) the transition from S6 to S3 (meeting documents ready) takes place.

![](/api/attachments/DD82MCBB/fulltext/images/7cac489448a3f55c60ecf8ab63904e6e26549641795d2123b6655544e3f331e6.jpg)  
Fig. 3. Formal model of the part of the activity ‘Governmental Body Meeting’ represented by ACT NET.

‘MP-2’ represents rules defined by the regulations of a governmental body. In practice, however, preparation of a meeting may take different course of actions in urgent situations. When an urgent meeting is scheduled the agenda may or may not be defined, usually documents are not prepared in advance, except the issuance of an invitation (A5) which is delivered to participants (A3). Rules applying to different urgent situations could not be found in regulation but are assumed by most of the participants. Sometimes, however, these ‘implicit models’ (or perceptions) of an urgent meeting preparation provoke trouble and validation problems. The more elaborated version of the Meeting Preparation Model ‘MP-3’, described in Fig. 3(c), demonstrates an attempt to explicate a perception of an urgent meeting preparation. By adding or changing the transition rules the model has been gradually adapted to the actual needs.

![](/api/attachments/DD82MCBB/fulltext/images/b2ddac463ebb08d95bad6c672273d06bdb0edf81d1f4056e317e49b0a041037b.jpg)  
Fig. 4. Specification of action types for Meeting Preparation Model "MP".

The Meeting Preparation Model is defined as a set of sentences describing actions, states and state transitions. When an actual activity starts the participants perform the actions (e.g. the instances of actions in Fig. 8) that are interpreted by the Meeting Preparation Model. When an action is executed the new state can be inferred according to the evidence of the present state by applying the appropriate transition rule. At the same time the regularity of action is checked. Each new inferred state makes obligations and commitments of agents, as well as other social consequences, explicit.

![](/api/attachments/DD82MCBB/fulltext/images/84f86ddade0d221a105842de1639a075616cb1cdadfb575a1bc41b4cd778e06b.jpg)  
Fig. 5. Meeting preparation model ‘MP’: transition from initial state S0 to state S1.

![](/api/attachments/DD82MCBB/fulltext/images/c0343cb18e4455fb272ae52476b60695fe14de3013fa30d8fff341ad9acfb92d.jpg)  
Fig. 6. Meeting preparation model 'MP': transition from state S1 to state S2.

![](/api/attachments/DD82MCBB/fulltext/images/3f43dbf36b20d8b8e1a0eac423867948e68d45c8152d67d9923e043a234a66a3.jpg)  
Fig. 7. Meeting preparation model ‘MP’: transition from state S2 to state S6.

![](/api/attachments/DD82MCBB/fulltext/images/87946a509686fee5b616abebdb5a01f00a406f24c9f8584f4f534693e2bd7b35.jpg)  
Fig. 8. Instances of actions that constitute formal conversation of agents mediated by Meeting preparation model 'MP'

The above example demonstrates how the meanings of actions and activities, derived from a social context, are formally expressed in OASS. The actions taken to prepare the meeting are meaningful according to norms described by legal acts and also those assumed by agents.

The computer-implemented version of the formal language for activity modelling, called ARL, is presented in $[7,11]$ . Specifications of the Formal model of activity in ARL are interpreted by KSE (Knowledge System Environment) and stored in the knowledge base (which contains specifications of organizational entities, roles and agents, documents and norms, as well). KSE functions as a generator of OASS $[7,12]$ .

## 6. Examination of possible roles of activity models in OASS

The Formal model of activity in OASS captures the meaning of an activity type. An activity type, however, does not exist as such. What does exist are perceptions of activities in the minds of those involved and verbal description of the activity type in legislation, regulation or in some instructive document. Data about the activity may also be empirically collected. Here a particular kind of support for human activities is identified during:

## (a) Creation of the formal model of an activity type

In order to represent the meaning of the activity type the actual activities, belonging to the given type, have to be analyzed and compared with the rules defined by legislation or different kinds of regulations. Even this process of searching for relevant regulations and comparison of legal rules and practice of activity performance, is worthwhile. It necessarily discovers impressions in the definition of the activity, the presence of vagueness, and may also illuminate issues causing contradictions. In some cases the verbal model of an activity, found in a legal act, describes an ‘ideal type’ of this activity, which is not often feasible in practice. Creation of a Formal model of an activity, in all these cases, requires redefinition of the activity in a new light and its representation by means of the formal language. It may also include changes in regulations, improvement of practical procedures and the introduction of new tools, procedures, requirements, obligations and the like. The mere process of creation of Formal models of activities may be seen as a knowledge-increasing process.

When a number of Formal models of activities are available for practical usage, OASS can provide several kinds of assistance:

(b) Performance support before the activity takes place

The Formal model of the activity may help the user to anticipate and plan the future dynamics of activities, conditions for performing them and predict possible or obligatory actions accordingly; it may also suggest ways for handling an activity and the complex network of activities.

(c) Performance support during the activity execution

OASS makes possible monitoring of the actual activity with respect to execution of actions, fulfillment of condition/action requirements and state transitions; according to the Formal model of an activity type and the present state of an ongoing instance of activity the next step(s), that may be or must be taken, are formally derived and presented to the user; warning signals may be activated when the actual or predicted state requires particular agent attention and/or intervention; under certain conditions the model may invoke automatic actions and procedures.

## (d) Post examination support and verification

After the activity has taken place OASS compares the evidence of the actual activity performance with the formal model of activity type, producing one of the following diagnosis:

(1) Concordance of the actual activity and the model, in which case the activity is accepted as correct,

(2) Tolerant deviations in the performance of the actual activity, when the ‘tolerance trigger’ allows it to be accepted as correct, but keeping a record of tolerated disagreements, or

(3) Intolerant deviations of actual activity from a norm, represented in the model of activity type, which means a violation of rules that is dangerous for organizational well-being; the prohibition trigger is invoked by OASS causing registration of the activity as unacceptable; at the same time OASS provides the user with the complete explanation of its diagnosis together with recommendations of what to do in order to overcome present difficulties.

Note here that the decision concerning verification of the activity stays with the responsible authority. If, for some reason, such an authority accepts a certain activity as correct, despite the fact that it has not been performed according to the rules (therefore being diagnosed as ‘unacceptable’) OASS has nothing to do, except to register ‘over-ruled by authority X’. Moreover, since verification of an activity necessarily includes all its consequences for the other activities to which it is related, OASS has to overcome a situation where some connections are missing, by querying the user(s), and to continue to work as if the activity was regular.

Although an activity cannot be regular as long as it severely violates the established norm or the agreement of the participants, OASS cannot ignore the fact that it has happened and that it has been perceived as legal by the responsible authority. Here we approach inconsistency between the desired/proclaimed norms for performing activities and the perceptions of agents in practice. Knowledge of an activity type built in laws, regulations or rules established by institutions, does not always correspond to knowledge acquired from practice. This kind of knowledge inconsistency is inherent to human activity systems. A formal system such as OASS aiming at supporting human agents in the performance of their activities should take into account these inherent inconsistencies.

The assumption that the activities are to be executed regularly, according to accepted rules or policies, is implicitly present. However, the best we can hope for is that OASS is ‘regular’ and ‘responsible’ as much as the people concerned are so. This does not mean that OASS would not contain inconsistent knowledge. It only says that knowledge inconsistency, inherent to human activities, is necessarily present in a formal system by which human knowledge is represented and mediated.

If we accept this, which seems reasonable enough, we can envisage the role that OASS can play above the level of supporting activity performance, namely:

## (e) Support meta-performance level

The evidence about activities, accumulated in OASS, diagnosed as ‘unacceptable’, but approved by the users, may invoke a higher level (automatic) process for examination of deviations and their frequencies. These findings may support the learning process at the level of performance of activities and may also help in restructuring and redesigning them. According to the investigation of current practice and the evidence of a significant number of deviations and inconsistencies, provided by OASS, the users become aware of the existence of multiple perceptions and attitudes towards activities performance. As a consequence any activity or the whole structure of activities can be subject to change and redesign. This might contribute to greater overall organizational flexibility and adaptiveness.

## 7. Concluding remarks

I have examined organizational activities as a kind of institutionalized conversation processes in which the actions and organizational knowledge assumed by agents are communicated by means of the Organization Activity Support System – OASS. OASS is intended to assist participants in planning, performing and evaluating activities. OASS provides a language for computer-mediated conversation of participants, the models of activity types that capture the meanings of the activities in a social environment and mechanisms to reason about appropriateness and regularity of actions.

This paper addresses a subtle issue of the role of formal systems, such as OASS, and its mechanized reasoning within basically informal human activities. In order to discuss it I should probably first recall the prime motive for activity modelling. It has often been declared that the purpose is not to displace human responsibility or to mechanize its super-ego. The formal system is aimed to help people to work together, within the social world they create, and to attain goals assigned to the activities they perform. The activity models built in OASS are intended to do this due to their ability to understand what has to be done, what is going on and what might be done under certain conditions. They also recognize different perceptions of activities and can infer the consequences of these differences. Therefore OASS is able to assist agents of activities or complex structures of activities, to monitor ongoing activities and to activate various warning mechanisms when deviations and irregularities are discovered. Naturally, they give evidence of their way of reasoning.

Looking from an individual or group perspective the motive for using OASS is to increase the ability to handle each activity properly and effectively and also to enhance overall understanding of the activity environment and improve interactions with it. From the organizational perspective the purpose of implementation of OASS for assisting performance of activities is to increase the overall effectiveness of complex structures of interrelated activities, decrease mismatches between connected agents and ease the resolution of conflicts due to different perceptions of the discretion space.

However promising, the concept of OASS has to be evaluated in practical applications. The experiments are designed for future research to verify the hypothesis about its impact on communication level among group members and effectiveness of activity performance as well as on group behavior and organizational culture.

## Acknowledgements

The concept of OASS and the Formal model of activities, presented in this paper, together with software system KSE (Knowledge System Environment) that generates OASS, were developed by the author and the research group at

LASA – Laboratory for Systems Analysis, Faculty of Electrical Engineering University of Sarajevo, within the basic research project ‘New Information Management Technologies’ (DCIX PRODUCTICA, 1988–1992, Science Foundation of Bosnia and Herzegovina) [7].

## References

[1] M. Aamodt, Forutsetninger for a ha till onskede forwarding i en darling samarbeidssituasion, Proc. Nordic Conf. on Management Research, Oslo (1977).

[2] L.J. Bannon and K. Schmidt, CSCW: Four characters in search of a context, Proc. First Europ. Conf. on Computer Supported Cooperative Work (1989).

[3] W.B. Croft and L.S. Lefkowitz, Task support in an office system, ACM Trans. Office Informat. Syst. 2 (1984).

[4] W.B. Croft and L.S. Lefkowitz, Knowledge-based support of cooperative activities, Proc. Twenty-first Annual Hawaii Int. Conf. on System Science, Hawaii (1988).

[5] D. Ćećez-Kecmanović, Organizational knowledge systems: An investigation on knowledge communication uncertainty, Comput. Networks ISDN Syst. 14 (1987).

[6] D. Ćećez-Kecmanović, Morphological approach to organizational knowledge systems, in: M. Carnevalle, M. Lucertini and S. Nikosia, eds., Modelling the Innovation: Communications, Automation and Information Systems (North-Holland, Amsterdam, 1990).

[7] D. Ćećez-Kecmanović, New information management technologies, Progress report of the basic research project, PRODUCTICA Conf., Sarajevo (1992).

[8] D. Čećez-Kecmanović et al., Formal models supporting organizational activities, Proc. Int. Symp. Computer at the University, Cavtat, Yugoslavia (1990).

[9] D. Ćećez-Kecmanović et al., Activity representation language – The means for formal communications, Mediterranean Electrotechnical Conf. MELECON'91, Ljubljana, Yugoslavia (1991).

[10] D. Ćećez-Kecmanović et al., Representation of norms in computer supported formal conversation, Proc. Third Int. Conf. on Information Systems Developers Workbench: Methodologies, Techniques, Tools and Procedures, Gdansk, Poland (1992).

[11] D. Ćećez-Kecmanović and O. Kruševac, Modelisation de la conversation formelle, ERGO.IA'92, Ergonomie et Informatique Avancee, Biarritz, France (1992).

[12] D. Ćećez-Kecmanović and O. Kruševac, Formal model of activity as a segment of organizational stock of knowledge, Yougoslav J. Operat. Res. YUJOR 2 (4) (1992).

[13] A.R. Dennis et al., Evaluation of electronic meeting systems to support strategic management, in: J.I. De-Gross, M. Alavi and H. Oppelland, eds., Proc. Eleventh Int. Conf. on Information Systems, Copenhagen (1990).

[14] G.L. DeSanctis and R.B. Gallupe, A foundation for the study of group decision support systems, Management Sci. 33 (5) (1987).

[15] S.D. Dewitz, Contracting on a performative network: Using information technology as a legal intermediary, in: R.K. Stamper, P. Kerola, R. Lee and K. Lyytinen, eds., Collaborative Work, Social Communications and Infor-

mation Systems, Proc. IFIP TC8 Working Conf. (North-Holland, Amsterdam, 1991).

[16] S.D. Dewitz and R.M. Lee, Legal procedures as formal conversations: Contracting on a performative network, in: J.I. DeGross, J.C Henderson and B.R. Konsynski, eds., Proc. Tenth Int. Conf. on Information Systems Boston, MA (1989).

[17] S.C. Ellis, The socialization of computers, in: R.K. Stamper, P. Kerola, R. Lee and K. Lyytinen. eds., Collaborative Work, Social Communications and Information Systems, Proc. IFIP TC8 Working Conf. (North-Holland, Amsterdam, 1991).

[18] J. Habermas, The Theory of Communicative Action, Vol. 1 (Beacon Press, Boston, 1984).

[19] M.A. Janson et al., The role of communicative action in the construction of decision support systems, Int. Conf. on Computer, Man and Organization II, ULB, Nivelles, Belgium (1990).

[20] K.L. Kraemer and J.L. King, Computer-based systems for cooperative work, Comput. Surv. 20 (2) (1988).

[21] R.M. Lee, International contracting - Formal language approach, Proc. Twenty-first Annual Hawaii Int. Conf. on System Science (Hawaii, 1988).

[22] R.M. Lee, A logic model for electronic contracting, Decision Support Syst. 4, (1) (1988).

[23] R.M. Lee and S.D. Dewitz, Finding international contracting opportunities: AI extensions of EDI, in: J.I. DeGross, M. Alavi and H. Oppelland, eds., Proc. Eleventh Int. Conf. on Information Systems, Copenhagen (1990).

[24] M. Lundeberg, G. Goldkuhl and A. Nilsson, Information Systems Development—A Systematic Approach (Prentice-Hall, Englewood Cliffs, NJ, 1981).

[25] K. Lyytinen, H. Klein and R. Hirschheim, Effectiveness of office information systems: A social action perspective, J. Informat. Syst. 1 (1) (1991).

[26] J. Nunamaker et al., Experiences at IBM with group support systems: A field study. Decision Support Syst. 5(2) (1989).

[27] L.S. Richman and S.L. Jarvenpaa. Computer support for groups: A search for theoretical models, Proc. Twenty-second Hawaii Int. Conf. on Systems Science Hawaii (1989).

[28] J.R. Searle, Speech Acts - An Essay in the Philosophy of Language (University Printing House, Cambridge, 1969).

[29] J.R. Searle and D. Vanderveken, Foundation of Illocutionary Logic (Cambridge University Press, 1985).

[30] K.R. Stamper, A logic of social norms for the semantics of business information, in: T.B. Steel and R. Meersmann, eds., Database Semantics (North-Holland, Amsterdam, 1985).

[31] K.R. Stamper, Semantics, Ch. 3, in R.J. Boland and R.A. Hirschheim, eds., Critical Issues in Information Systems Research (Wiley, New York, 1991).

[32] K.R. Stamper, Signs, organizations and information systems, Australian Nat. Information Systems Conf., Wolongong (1992).

[33] D. Vogel et al., Group decision support systems: Evolution and status at the University of Arizona, in: R.M. Lee, A.H. McCosh and P. Megliarese, eds., Organizational Decision Support Systems (North-Holland, New York, 1989).
