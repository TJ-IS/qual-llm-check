---
otero_id: 21784
otero_key: "XV8ZD2CV"
title: "Key issues in the design of an asynchronous system to support meeting preparation"
authors: "Marcos R.S Borges; Jose A Pino; David A Fuller; Ana C Salgado"
year: "1999"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(99)00051-2"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Key issues in the design of an asynchronous system to support meeting preparation

Marcos R.S. Borges <sup>a,)</sup>, Jose A. Pino <sup>b,1</sup>, David A. Fuller <sup>c,2</sup>, Ana C. Salgado <sup>d,3</sup>

<sup>a</sup> NCE, Caixa Postal 2324, UniÕersidade Federal do Rio de Janeiro, Rio de Janeiro, Brazil b Departamento de Ciencias de la Computacion, Casilla 2777, Uni ´ Õersidad de Chile, Santiago, Chile Departamento Ciencia de la Computacion, Casilla 306, Pontificia Uni´ ´Õersidad Catolica de Chile, Santiago 22, Chile Departamento de Informatica, Caixa Postal 6851, UniÕersidade Federal de Pernambuco, Recife, CEP 50740-540, Brazil

## Abstract

A review is made of the most important decisions in the design of asynchronous systems to support the preparation of business decision meetings. These decisions are illustrated with the choices made for the development of SISCO, a system of this type. The presentation considers issues in the discussion model, the group memory, the communication and visualization mechanisms, and the development of a meeting preparation sequence: how to start a session, carry it out and close it. Issues concerning coordination, participation and awareness in meeting preparation sessions are also discussed. q 1999 Elsevier Science B.V. All rights reserved.

Keywords: Pre-meeting; Asynchronous distributed systems; Structured discussions; SISCO; Group memory

## 1. Introduction

A decision meeting can be divided into three phases, as proposed by Bostrom 7 : setup, agenda <sup>w</sup> <sup>x</sup> and wrap-up. These stages correspond to what we call pre-meeting, meeting and post-meeting Ž . terminology used by Bostrom as well . The premeeting, according to Bostrom, can serve to clarify and get agreement on outcomes, make clear roles and rules, and establish a positive group effect. A ‘‘facilitator’’ is needed to perform these tasks. The same person also helps the group to adapt and execute the agenda during the meeting stage. Finally, during the post-meeting, the facilitator summarizes the meeting, detailing each point that requires further action.

The pre-meeting is an important step, since a well-done preparation can have a positive effect on the quality of the decisions made during the meeting. Very often, however, the preparation of a decision meeting is done in a hurry or not done at all. In part, this may be due to lack of a computer-based support. In this paper, we analyze the main issues concerning the design of a meeting preparation system, illustrating them with the choices we have made for SISCO, a system cooperatively designed by groups at eight universities from Latin America and Europe 3,4,44 . <sup>w</sup> <sup>x</sup>

There have been several interpretations of premeeting activities. Most authors see the pre-meeting as a planning activity, during which agenda items, logistics, schedule and pre-work are carried out 47 .<sup>w</sup> <sup>x</sup>

In SISCO we believe that preparation can encompass further activities. The pre-meeting is a great opportunity to increase common knowledge about the issues surrounding the agenda items. Moreover, participants are induced to reflect and generate ideas within an adequate time frame. Often, during a face-to-face meeting, participants are compelled to make decisions without enough time to assess their full implications. Besides, a series of preparatory tasks can be carried out: get some input data, do some simulations and other computations, etc. The need for these tasks may appear during the discussion, not necessarily beforehand.

We believe that in most cases decisions are too complex to be made over an asynchronous distributed system and thus, we assume they will be made during the second Bostrom stage: the meeting itself 7 . The SISCO approach assumes that activi- <sup>w</sup> <sup>x</sup> ties performed during the pre-meeting have always the actual meeting on focus. There is no intention to replace the meeting. Moreover, SISCO does not make sense if there is not a meeting scheduled to decide on the issues. At most, the pre-meeting interaction can be used to postpone or change an agenda item, but never to decide upon it. In this way, SISCO contrasts with newsgroup systems in which issues are freely discussed with no formal provision for a subsequent meeting.

What type of meeting preparation can be done? In the first place, the participants can start by discussing the agenda items and presenting ideas. We believe this is the most important preparation that can be done, because a preparation based only on parallel, disconnected work does not reduce the equivocality and uncertainty 18 that participants may have. The <sup>w</sup> <sup>x</sup> discussion is interesting because all participants can ponder arguments and must have the necessary time to carefully think them over.

One of the main challenges of this approach is to convince participants that sharing knowledge and having contradictory views should not be seen as loss of power or taking unnecessary risks 40 . In <sup>w</sup> <sup>x</sup> SISCO we try to emphasize teamwork achievement and individual rewards by peers. For the sake of argumentation completeness, we also stress the importance of uncoupling the participant belief on a position from alternative views that contribute to the discussion.

Several studies such as the one reported by Chidambaram 17 suggest that new attitudes may take a <sup>w</sup> <sup>x</sup> while to form among users of new technologies. Even being a new technology, the preparation of meetings can be seen as a first step towards the adoption of Electronic Meeting Systems EMS to Ž . support face-to-face meetings. This may indicate that in the beginning, active participation may be scarce and timid. Most participants may adopt a conservative attitude, choosing to read other contributions instead of exposing their own ideas.

When reporting the lessons learned on the use of EMS, Nunamaker et al. 38 stressed the importance<sup>w</sup> <sup>x</sup> of group leadership. People react differently to new technologies and some participants need stimulus to adopt a positive attitude towards the supporting system. A well-played facilitator role can change all that, turning boring or empty discussions into invigorating ones, bringing enthusiasm and partnership to an otherwise indifferent participation. In the same article, the authors reinforced the need of a wellplanned agenda. The pre-meeting outcome can provide hints about what topics have conflicting views and which ones have some consensus. Of course all this can change during the meeting, due to the addition of new elements to the discussion, but it is good to have a starting point.

We have chosen to focus on asynchronous systems in order to support the pre-meeting interaction, because they provide the required time for participants to perform the actions mentioned above. Moreover, asynchronous systems are less demanding on users to log on at any time in order to work on the preparation of a meeting, although we recognize that this requires some discipline. The additional benefit of distributed pre-meetings is that they allow the company to reduce travel costs with unnecessary or unproductive meetings.

Well known asynchronous systems which might be used for the discussion process in preparation to a meeting are TCBWorks 20 and BSCW 6 . TCB-<sup>w</sup> <sup>x</sup> <sup>w x</sup> Works is a Web-based system intended to support distributed meetings, including decision making. BSCW offers a workspace to share information, with features to store and retrieve documents to support collaborative work.

This paper initially presents general issues to be addressed in the design of asynchronous systems to support meeting preparations ASMP Section 2 .Ž . Ž . Then there is a discussion on issues concerning the support of the pre-meeting stage from its ownŽ preparation to its closure; Section 3 . In the subse-. quent section we address the implementation issues Ž . Ž . Section 4 and finally, the conclusions Section 5 .

## 2. General issues

DeSanctis and Gallupe 21 have classified Group<sup>w</sup> <sup>x</sup> Decision Support Systems GDSS in three cate-Ž . gories. Level 1 systems are those that facilitate communication among group members. Level 2 systems provide tools to reduce uncertainty the members may have decision modeling and group decision tech- Ž niques . Finally, Level 3 GDSSs have machine intel-. ligence support including expert advice. What type of system will an ASMP be?

It is clear that an ASMP facilitates communication. Is that all this type of system can do? The designers can certainly choose to develop a system just with this goal. However, it will probably be too simplistic. A more comprehensive system will have features to help reduce the confusion the members have as argued in Section 1 . Such a system, then, Ž . will adequately be classified in Level 2 category.

On a pre-meeting system, people work on a distributed setting. Each participant may do his work from the comfort and information availability of his own place 24 . Moreover, their work can be done<sup>w</sup> <sup>x</sup> asynchronously, whenever they have the time to dedicate to the meeting preparation or have had a period of time to think over an idea. Of course, this choice also has drawbacks, since usual mediated communication among people is poor when compared to face-to-face meetings. However, the premeeting phase may be considered as consisting of many divergent activities 36 which can be appro-<sup>w</sup> <sup>x</sup> priately done on a distributed asynchronous environment.

In the rest of this section, we introduce a proposal for ASMP architecture, and we will present related issues on discussion and communication mechanisms, persistent memory and visualization mechanisms.

## 2.1. ASMP architecture

We propose an ASMP architecture supporting group interfaces to users, access to a common space — called group memory GM — and group com-Ž . munications see Fig. 1 3 . Ž . <sup>w</sup> <sup>x</sup>

The user interface provides direct access to the GM to store and retrieve elements relevant to the discussion. It also contains facilities to provide interpersonal communication and data driven communication.

![](/api/attachments/XV8ZD2CV/fulltext/images/5610f5e494baaf5a1435a785e6f0f0ed154502bafc4059ae3efae3f2cbf77031.jpg)  
Fig. 1. ASMP architecture.

In an ASMP, communication among participants is fundamental. People need to contribute ideas in the context of ideas put forward by other people. Therefore, participants must have previous contributions easily available. Although electronic mail systems provide a way to store previously sent or received messages, what is really needed is a common space to store the information in order to comfortably refer to it and add new contributions.

The GM should be structured so that information is organized and retrieved in a consistent way. This persistent common space should be designed so that it would be possible to follow the details of a discussion, separating the components of each discourse. The GM is also called the Collective Intelligence 2 and it can reduce uncertainty and<sup>w</sup> <sup>x</sup> indeterminism in the decision making within the organization 10 . <sup>w</sup> <sup>x</sup>

Group communication can be performed in two ways. The first is when users need to communicate with others through conversation tools such as a chat or a video conferencing system. If this interaction is asynchronous, the GM can be used to store and retrieve such information. Second, what we call ‘‘data driven communication’’ supports user awareness of some events that are happening in the discussion environment which are also important for an effective collaboration. An ASMP should keep participants informed of details which may be important to them, such as a new contribution on a specific issue.

## 2.2. Discussion mechanisms

The first decision to be made in the design of an ASMP concerns the choice of an archetype of how the discussion is going to be carried out. One possi bility is to have a discussion based on positional statements and comments afterwards. Another simple approach may be based on questions and answers. There are other more complex approaches to supporting a discussion, such as the Speech Acts theory <sup>w</sup> <sup>x</sup> 27 , implemented in a software called The Coordinator 1 . Although we do not consider The Coordina-<sup>w</sup> <sup>x</sup> tor to be strictly an ASMP, it could be used for this purpose.

It is important that the discussion be well structured. Structuring is necessary because it allows easy retrieval, idea evolution tracking and preparation for the decisions. It is easy to see that a simple collection of e-mail messages, for example, fails to meet the requirements mentioned above.

The discussion model adopted by SISCO is an extension of the IBIS argumentation model 31 . It<sup>w</sup> <sup>x</sup> has the same basic elements: issue, position and argument but includes remark and task. The data model also includes information about participants, the discussion agenda items with their objectives and pre-defined constraints 4 . The participants are clas- <sup>w</sup> <sup>x</sup> sified according to the role they have in the premeeting. The roles can be coordinator of the premeeting, facilitator, contributor or observer of an item discussion.

## 2.3. Group memory

It is not unusual that the memory of a group, i.e., the information that group members have of a problem being discussed, is stored in different places such as informal discussions, meeting memory, documents and e-mail messages. The purpose of the GM in an ASMP is to maintain a common persistent space to register the information related to a discussion in a group.

In ASMP, the GM needs to be designed considering three different information types. The first corresponds to information about the group members. Here, roles played by group members may be considered. The second type of information is about discussion items according to the defined discussion mechanisms. Note that group members should have the possibility to review what has been already said in all previous sessions, building on top of that. McCarthy 34 argues that conversation via text-based<sup>w</sup> <sup>x</sup> electronic conferencing facilities is much less orderly than one would expect from studies of normal spoken conversation. An extensive analysis 33 shows<sup>w</sup> <sup>x</sup> that rather than dealing with a topic and then moving to another in a sequential fashion, participants open new topics while old topics are still unresolved. They suggest that this is due to the persistence of the conversation in text-based communication. The third type of information contains the predecisions and meeting constraints. This information contains facts that need to be considered during the pre-meeting discussion process.

It is important to note that in an ASMP, the GM may provide the required information to support asynchronous awareness mechanisms. Also, the GM may support persistency to interpersonal communication when required. For example, a group member may require recording his computer-mediated communication through the GM as part of the discussion information. Note that organizational memory <sup>w</sup> <sup>x</sup> 2,10,14 could be constructed using the GM.

The data model associated to SISCO GM was completely specified using the Object Modeling Technique OMT 42 . The relationships among the Ž . <sup>w</sup> <sup>x</sup> object classes defined are illustrated in Fig. 2. In this methodology, aggregations are drawn like associations with a small diamond indicating the assembly end of the relationship and the notation for generalization is a triangle connecting a superclass to its subclasses. The SISCO data model object classes are described in detail in Section 4.

## 2.4. Communication mechanisms

Group interaction before the actual meeting is what we are trying to achieve with an ASMP. We are not just trying to open a wide-band channel of communication among participants. What is desired is to provide communication among participants in the context of the work they are doing together, with tools to support this joint activity. Therefore, communication is important and any design should provide the means for efficiently achieving it.

![](/api/attachments/XV8ZD2CV/fulltext/images/ae5b7e5a1254eb574f8a4ea5f07ad3531e4f433fed94b435ef3ee5d1600fd3f1.jpg)  
Fig. 2. SISCO data model.

A study of early computer-mediated communication by Hiltz and Turoff 30 found that this media-<sup>w</sup> <sup>x</sup> tion produces a sense of impersonality. In particular, anonymity and physical separation contribute to this depersonalization. In general, a distributed meeting, which does not allow verbal communication and withholds visual information about meeting participants, lacks important social context cues 23,35 .<sup>w</sup> <sup>x</sup> Valacich et al. 48 summarized previous research<sup>w</sup> <sup>x</sup> suggesting that ‘‘proximity among group members’’ is multidimensional and includes much more than the physical distances between communicating individuals.

In the SISCO approach, we do not rule out that wide-band communication can be useful, if available. Moreover, we assume that conventional communication means are available to group members: telephone, fax, and electronic mail. However, our emphasis is on using the discussion database as a communication channel. In fact, one way of viewing a collaboration process in which various users are contributing is that they are having a conversation. This is due to the fact that users are incorporating elements that reflect their way of analyzing facts, opinions, data, comments, etc. These elements are read by the other group members and thus a communication path is completed.

Communication via the discussion database is formal, structured, persistent, and public to the au-Ž thorized participants . Of course, other types of com-. munication are needed which do not fit the previous characteristics. This is why we need conventional communication means. It is expected that participants will talk by phone, send private e-mail messages, go to each other’s offices and have informal talks. These interchanges convey much useful information that the very restricted bandwidth of the discussion database cannot transport. Of course, some physical availability is necessary for these encounters to occur.

## 2.5. Visualization mechanisms

An ASMP must have various ways to access, navigate and display information. The richer the information stored in the GM, the greater the care that has to be used to effectively provide that information to the pre-meeting participants.

SISCO includes ways to quickly find discussion elements by full-text search, navigation by author, following a discussion thread, and accessing unread material. The displayed information shows the relation it has with other discussion elements.

The implementation of the visualization mechanisms can be approached in many ways. A simple one is to provide a text-based, hierarchical display of information 8,25 . However, this approach probably <sup>w</sup> <sup>x</sup> does not scale well and does not convey the temporal domain. New approaches can explore emphasis on continuous temporal navigational cues 32 or spatial<sup>w</sup> <sup>x</sup> cues such as fisheye views 43 .<sup>w</sup> <sup>x</sup>

## 3. Supporting the pre-meeting

## 3.1. Preparing the pre-meeting

## 3.1.1. Coordination function

The first service of any ASMP is the support to create a pre-meeting. Decisions must be made as to who may initiate this process and the events that must occur afterwards. In SISCO, any user can request the system to create a new pre-meeting. The corresponding action is the creation of the database structure that will contain the group memory of the pre-meeting. The system also asks the user to define the coordinator of the meeting.

There are some Group Support Systems that have been designed without an explicit coordination function, but there is a wealth of evidence that coordinators<sup>r</sup>facilitators can play an important role in improving meeting processes and outcomes 37 . In an<sup>w</sup> <sup>x</sup> empirical study by Clawson et al. 12 , 16 key<sup>w</sup> <sup>x</sup> facilitator dimensions of activity were identified; one of these, considered important by the facilitators themselves, was ‘‘Planning and Designing the Meeting’’.

In SISCO, the coordinator is the person responsible for the pre-meeting’s success. His goals are that participants acquire the comprehensive knowledge to allow informed decision making, in order to obtain an adequate documentation level to increase the company’s knowledge base. Any person with the appropriate administrative authority can play the coordinator role. The activities performed by a coordinator are the following:

1. Defining the pre-meeting users. The coordinator has to determine which people will take part in the discussion process and request the system to prepare their initial access.

2. Creating and modifying users’ roles. The coordinator assigns each user one of the four discussion roles described in Section 3.1.2 . He has toŽ . define himself as the coordinator, and in the case that he also wants to participate in the discussion process with another role, he must specify this.

3. Creating and modifying pre-meeting restrictions. The coordinator has to define and<sup>r</sup>or modify the previous conditions imposed on the discussion, such as pre-decisions and constraints.

4. Create and modify pre-meeting agenda items. The coordinator is responsible for the definition of the discussion agenda, assigning a facilitator to each item, as well as its discussion deadline.

5. Obtaining a comprehensive report at the end of the pre-meeting for use in the face-to-face meeting.

6. Monitoring the development of the pre-meeting. Some corrective actions may be needed as a result of this.

## 3.1.2. Group structure

A decision must be made concerning the type of group the ASMP will support. Constantine has classified the group structures in four extreme stereotypes 16 : Closed or Traditional Hierarchy, Random <sup>w</sup> <sup>x</sup> or Innovative Individualism, Open or Adaptive Collaboration, and Synchronous or Harmonious Alignment.

SISCO supports groups with some degree of cohesion. In terms of the group structures defined by Constantine, SISCO supports ‘‘Open Adaptive Collaboration’’ and ‘‘Closed Traditional Hierarchy’’. These two types of organizational structure have very different decision making processes, however, both are supported by the SISCO conversational model in the pre-meeting stage. In the first group type, participants are partners showing some degree of hierarchical cohesion to allow them to perform a discussion process with some structure. In this case, one of them plays the role of coordinator, and the others will assume the remaining roles, depending on their involvement in the pre-meeting.

In the Closed Traditional Hierarchy, there is a well-defined hierarchy among participants. In this case, the role of coordinator is performed by the group’s head, while the remaining roles should try to match the administrative roles played by participants in the ordinary group activities. In particular, if the group head does not participate in the discussion, he may be informed of its progress by an administrative assistant, who typically will take an observer role Ž . explained below in the pre-meeting. The other two stereotypes defined by Constantine are not supported by SISCO, since they do not have enough group cohesion to allow a structured discussion process.

## 3.2. Setting-up the pre-meeting

Various activities are needed to start the pre-meeting discussion. The ASMP must provide the support for the corresponding participants to achieve them.

## 3.2.1. Agenda items

If a discussion is to be held, there must exist a specification of the themes of the discussion. Naturally, these subjects should be related to the decisions to be made during the subsequent meeting. Therefore, whoever will head the decision meeting must be involved in this specification. Moreover, there must be priorities and deadlines set for the discussion subjects.

This specification is very important for the success of the pre-meeting. First, it provides the discussion framework: anyone initially confused about the goals of the pre-meeting can get a clarification of what is expected. Second, overly restricted, vague or ambitious goals or unrealistic deadlines could be reasons for an unproductive pre-meeting.

In SISCO, it is the coordinator’s responsibility to specify the discussion agenda, ordering the items and establishing deadlines for each of them. Furthermore, for each item, the coordinator must state the objectives of the discussion to be held within the deadline. To accomplish this task, the coordinator has the privilege to incorporate into the GM the items, deadlines and objectives.

## 3.2.2. Roles

The ASMP may have roles to be played by participants during the pre-meeting. Each role may have responsibilities, GM access privileges and specific tasks associated with them. Besides the coordinator, whose role was discussed in Section 3.1.1, there are those summoned or invited to join the pre-meeting.

Decision makers who will participate in the meeting must clearly also work in the pre-meeting discussion, since one of the main goals of the pre-meeting is to reduce their equivocality and uncertainty. If some of the guests participate in the pre-meeting pressured by their superiors or consider this activity as irrelevant, they will not perform as expected; in particular, they will probably minimize their contributions and may make the pre-meeting less useful.

In SISCO there are three additional roles defined for those people invited to join the pre-meeting: facilitator, contributor and observer. The facilitator is the person who is responsible for supervising the pre-meeting discussion of a particular agenda item. He does not necessarily have a superior position in the organization than the rest of the members. Note that the facilitator makes some important decisions concerning a discussion item, such as requesting the coordinator to invite a particular person to join the pre-meeting for that item, choosing responsibility for tasks among those members who have volunteered for them, and overseeing that the discussion progresses towards the goals.

Some of the problems which facilitators deal with concern ways to motivate participants to collaborate in an effective way in the discussion process. For this purpose, the computer system considers appropriate tools to allow the coordinator and facilitators to cope with the problem of lack of motivation.

The contributors produce the actual discussion. For each agenda item, there is a group of participants who are invited to be contributors for that item. This group constitutes a subset of all group members invited to the SISCO pre-meeting, which means that some members will not contribute in the discussion of certain agenda items. This feature gives the coordinator and facilitators the flexibility to invite consultants, for instance, to participate just in the discussion items in which their opinions are needed. The system has security features to ensure that members participate only in the discussion items for which they are authorized. The following activities are the contributors’ main responsibilities:

<sup>Ø</sup> Produce discussion elements for those items for which they are allowed to do so.

<sup>Ø</sup> Offer themselves to the facilitator as candidates to carry out a task.

<sup>Ø</sup> Perform the tasks assigned by the facilitator, within the specified deadlines.

The reading of the discussion is an activity, which is done by persons authorized to read, but not write contributions to the discussion. It is performed by the observers. A secretary, for instance, may need access to the discussion, but may not be permitted to submit discussion items.

Table 1 summarizes the access rights for the four SISCO roles concerning reading and writing for pre-meeting pre-decisions restrictions , agenda Ž . items, objectives and discussion elements. These roles allow a fine granularity concerning the work to be done. One person can be an observer for certain items but a contributor for others. This is useful in the case that the group includes experts: they are expected to contribute to a few agenda items, but need to know about other items in order to have the contextualized information.

This approach to roles has some similarity to that of TCBWorks 20 . The participant and observer are <sup>w</sup> <sup>x</sup> basically the same as our contributor and observer; the Administrator can perform any function and thus implicitly has a slightly higher hierarchical dominance in the group’s activities than our Coordinator, who can be confined to administrative matters. The Organizer is also similar to our Facilitator, but again, he has greater power, since he can delete projects Žwhich can be considered similar to our agenda items , move them, etc. In SISCO, Coordinator and. Facilitators must communicate with each other in order to make a decision about some actions they may want to take.

Table 1  
Access to the SISCO pre-meeting information by role

<table><tr><td rowspan="2">Role\access</td><td colspan="2">Restrictions</td><td colspan="2">Items</td><td colspan="2">Objectives</td><td colspan="2">Elements</td></tr><tr><td>Read</td><td>Write</td><td>Read</td><td>Write</td><td>Read</td><td>Write</td><td>Read</td><td>Write</td></tr><tr><td>Coordinator</td><td>x</td><td>x</td><td>x</td><td>x</td><td>x</td><td>x</td><td>x</td><td></td></tr><tr><td>Facilitator</td><td>x</td><td></td><td>x</td><td></td><td>x</td><td>x</td><td>x</td><td>x</td></tr><tr><td>Contributor</td><td>x</td><td></td><td>x</td><td></td><td>x</td><td></td><td>x</td><td>x</td></tr><tr><td>Observer</td><td>x</td><td></td><td>x</td><td></td><td>x</td><td></td><td>x</td><td></td></tr></table>

It can be noticed that within a pre-meeting, the coordination function can set up a variety of other, ad-hoc roles, for the purpose of achieving the goals in the most efficient way: devil’s advocate, reviewer, etc. These unsupported roles may help the facilitator to get a good quality discussion from the group in a short period of time.

## 3.2.3. Discussion structure

The discussion has to fit the data model provided by the ASMP. This implies that in order to keep consistent the structure of the discussion, all participants must first learn about the discussion components and their relationships and then discipline themselves to contribute according to those components.

In the case of SISCO, participants must try to clarify in which of the discussion elements a specific contribution is to be added to the GM. Initial experimentation with SISCO has indicated that some people have difficulties in distinguishing between positions and arguments. Remarks must also be used sparingly.

## 3.3. DeÕelopment

## 3.3.1. Contributing

‘‘To come into collision or disagreement; to be contradictory, at variance or in opposition; clash’’ is the first meaning of ‘‘conflict’’, according to the dictionary 28 . This meaning is the intended one<sup>w</sup> <sup>x</sup> when we say that members of a group should have conflict when they have a pre-meeting discussion. This is because a discussion cannot be an ‘‘agreement’’ session for several reasons.

First of all, it is expected that when facing a certain issue, people have different views. Those views have to be expressed because people must be free to give opinions and say what they would like to. Second, a variety of points of view enrich the joint work. It is possible for the first view even if itŽ is the group head’s view to be the best one, but this . is unlikely. It is much better to have different views and then decide which is the best. There might even be ideas that complement each other, but this is discovered after the views are presented. Previous empirical work has found that a wealth of ideas is better than a single good idea 49 . <sup>w</sup> <sup>x</sup>

Third, in the context of a discussion, different points of view enrich not only the joint work being done in our case, the preparation for the decisionŽ process , but also the group members’ knowledge. . This occurs because different points of view are frequently motivated by information which may be new to the other participants or which is being overlooked. A discussion produces more informed group members, and the group will also gain additional knowledge about the people themselves. We analyze below the main issues related to how group members contribute to the discussion and how they become acquainted with other members’ contributions.

3.3.1.1. Adding to discussion. A contributor can start a discussion on how to reach an objective and what are the questions to be clarified regarding this objective by inserting issues. Issues are questions or proposals. The operations involved in the discussion process are associating issues substituting or gener- Ž ating other issues , responding to an issue inserting . Ž a position , defining arguments in favor or against a . Ž position , supporting positions, inserting remarks as- . Ž sociated with any element and rewarding other group . members.

Contributions are not intended to be personal endorsements of ideas. In our model of cooperation, the personal preferences are to be expressed in the subsequent meeting in which decisions are going to be made. Issues, positions and arguments are then logical statements, which should support themselves on their own merits, and not because one or more contributors prefer, choose or like them. This is an important aspect that should encourage people to contribute, since they are not liable to choose an option that someone else dislikes. Contributions are then stated as options having advantages and disadvantages, and these may be expressed and reviewed by authorized participants.

3.3.1.2. Identification of contributions. The issue of anonymity has been addressed in the design of various group support systems 37 . There is no doubt <sup>w</sup> <sup>x</sup> that anonymity plays a key role when we want participants to express their views freely without fear of retaliation. In a meeting preparation system this is particularly important, as people sometimes do not want to be identified with certain positions or ideas. Although we have emphasized that the ideas expressed are not necessarily the contributor’s own positions, it is impossible to avoid this association from other group members. Therefore, in order to get the most comprehensive set of positions and ideas, it is necessary to overcome this restriction.

On the other hand, we should keep in mind that anonymity also presents some drawbacks 37 . The<sup>w</sup> <sup>x</sup> problems of free riding, and levels of aggression and anxiety can become high in certain situations and should be closely monitored by the coordinator and<sup>r</sup>or the facilitator. Although conflicts and different points of views are desirable, the coordinator must avoid the occurrence of excessive polarity and unfocused discussion as they can undermine the success of the meeting.

In SISCO, we provide anonymity to contributors who wish to disassociate their identification from elements of the discussion. The default for all contributions however, is to identify the author to all other participants. In order to set the contribution as anonymous, the contributor should express this at the time of its creation. Anonymous contributions do not count for the level of participation, defined in Section 3.3.2.1, and for the rewards.

3.3.1.3. Notification and awareness. Awareness can be defined as an ‘‘understanding of the activities of others, which provides a context for your own activity’’ 22 . Without awareness a group member cannot<sup>w</sup> <sup>x</sup> build his sense of a group and the human–human paradigm will remain mainly on the intentional level <sup>w</sup> <sup>x</sup> 46 .

Awareness mechanisms are essential for group support systems in order to transform irregular interactions of group members into a consistent and perceptive performance over time. Awareness mechanisms are important to keep members up-to-date with important events and therefore to contribute to more conscious acting on their part.

In the literature of cooperative systems, the term awareness has been used in different contexts 29 . In<sup>w</sup> <sup>x</sup> asynchronous systems the notion of awareness is often related to the loss of information and context caused by the interruption of interaction while a group member has been away from his workstation. This loss is augmented by the lack of understanding caused by the absence of real time interaction.

The definition above suggests, however, that there are different levels of awareness and a variety of ways to deal with them. A simple but inefficient awareness mechanism is one based only on notification. Members are notified about the existence of new elements by means of mail messages, for example. Besides the potentially high number of messages, this solution has the serious drawback of using a mechanism that is not integrated to the actual group memory where other contributions reside.

In SISCO we provide awareness at the time of access. Contributions that are new to a participant are shown differently from those he already knows. Colors and icons are the instruments used to make the differentiation. Awareness summaries are also provided at the beginning of a session, indicating to the contributor where he will find the new elements. We consider this solution better than a notification mechanism because the new elements are interpreted within the context of existing elements, necessary to better understand the contribution. On the other hand, in this solution there is no notification scheme. The user becomes aware of new elements only when he accesses the system and retrieves the GM.

Most solutions presented so far have left unsolved many important problems. One such situation occurs when elements are organized into a hierarchy, the insertion of a new element at the bottom level affects all elements in the hierarchy path. The problem is how to deal with the elements belonging to this path. They might not be new but the existence of new elements within their hierarchy may affect their meaning. In certain types of interactions, group members may require selective awareness mechanisms, meaning that not everything is at the same level of their interest. Some actions relate to the member’s current work, others relate to past or future work, and some perhaps are of secondary interest.

## 3.3.2. Monitoring the discussion

The coordination role has the important task of ensuring that a significant discussion is developed. To achieve this, members acting as coordinators should have specific functions enabling them to encourage contributions and to promote understanding. Some actions aimed at starting the group interaction are performed on the initiative of the coordinator at the time of the pre-meeting set-up.

During the actual discussion, however, the coordinator and facilitators should receive some feedback about the evolution of the discussion from a broad point of view. The levels of participation of contributors and the evolution of ideas are examples of feedback, which can be offered to coordinators. In what follows, we describe some key issues on monitoring and acting in the pre-meeting aimed at improving its performance.

3.3.2.1. Measures of participation. When calling a meeting, it is expected that participants will exhibit different levels of equivocality and uncertainty on the theme s of the discussion. The pre-meeting will Ž . serve to reduce or even to eliminate these adverse factors by the time of the meeting. During this process, however, it is expected that participants will have different degrees of productivity concerning contributions. One person may submit many discussion elements, another may contribute with a few but meaningful ones, while a third may just read the contributions supplied by other group members. The participation of the latter type should not be overlooked: just reading other people’s work is an important way to reduce equivocality and uncertainty. Of course, if all contributors or almost all of them are of the third type, then the discussion is poor and it is an indication that the desirable interaction is not succeeding.

The level of awareness of an item is closely related to the interest this item provokes in other group members. The global level of awareness is also related to user’s participation. Given a specific user it is possible to infer his level of participation by examining his level of awareness to the elements of the system.

One approach we are exploring with SISCO is to have a tool to measure and display at least some of the meaningful quantitative data concerning the participation during a pre-meeting. This tool is called ‘‘participameter’’. It displays a set of charts showing data on the number of discussion elements read by each participant, the number of elements contributed, the frequency of connections, the number of tasks for which each person has been a candidate, the number of tasks achieved, etc. We expect this tool to be particularly useful for the coordination function.

3.3.2.2. MotiÕation. What motivates group members to actively participate in a discussion? There might be personal reasons, such as a genuine interest on specific items that are important to their work. Or there might be a sincere sense of a working team. Or there might be external stimuli, such as some kind of reward that generates interest. One of the tasks of the coordinator is to identify these factors in the group and make use of them to achieve high levels of participation.

That means motivating participants in a variety of ways. For instance, the coordinator and facilitators can introduce initial issues, positions and arguments that will compel participants to quickly state their contributions: surprising, even shocking elements may be introduced to achieve this motivation. In fact, the pre-meeting success is to a large extent dependent on the richness of the discussion: if there is a poor discussion, little or nothing has been gained with the pre-meeting.

As we discussed above, it is important to stimulate people’s participation. Participants get a payoff with the exposure of their ideas. However, that may not be enough: after all, people contributing only marginal comments get some exposure as well. There must be a way to reward contributions, specially the meaningful ones. One possibility is to have the system distributing credits to the participants. Unfortunately, there is no simple way to do this; automatic credit assignment would only be possible with a very sophisticated knowledge-based approach that would qualitatively assess the contributions for originality, significance and relevance.

But this will not work in a pre-meeting being held by peers. In SISCO, there is also an optional tool to assign rewards by group members themselves: they know when a contribution or a set of contributionsŽ . deserves a word of recognition. The computer implementation must provide a simple way to easily assign such rewards, for instance, allowing a ‘‘star’’ to be graphically attached to a participant’s description. For each such star, it must be possible to know who assigned it and the corresponding rationale. Furthermore, stars should wane in time, stimulating recipients to keep contributing with significant ideas. For certain groups perhaps all group members may be allowed to assign rewards; for others, perhaps only the facilitators or a specific member — such as an executive — should be allowed to do so. The effect of rewards has not been well studied in Group Support Systems research 5 .<sup>w</sup> <sup>x</sup>

3.3.2.3. Identification of pending information. A situation that often occurs in a meeting is when participants discover that additional information is required in order to advance in a discussion. In most cases this information is unavailable during the meeting and the discussion is postponed for a time after the required information becomes available. One important benefit of a pre-meeting discussion is the identification of this kind of situation prior to the meeting. This will give time to get the necessary information and to make it available to all participants before the meeting.

In SISCO when the need for additional information is acknowledged by participants, it will generate a task whose goal is to search the data and make it available. Any contributor may suggest a task, by means of a proposal, but the actual creation of tasks is the responsibility of the facilitator of the related item. When a task is created, it will also be assigned to a participant by the facilitator, but a contributor may nominate himself to carry out a task. If the task was originated by a proposal, the facilitator sets up a corresponding link when the task is completed.

## 3.3.3. Managing the discussion deÕelopment

In Section 3.3.2, we tackled the problem of monitoring the discussion through a set of functions with respect to contributions of participants. In this section, we address managing the discussion development, which is a kind of high level monitoring. The distinction between these two levels is mostly related to the degree of decisions and actions that have to be carried out during the course of the pre-meeting in order to progress into the meeting phase.

Among these issues we have selected three that we believe are most relevant. They deal with situations in which some degree of authority is needed in order to execute the necessary corrective actions. Therefore, the functions available to handle these situations are solely under the control of the premeeting coordinator.

3.3.3.1. Discussion re-structuring. Part of the setting-up process is the decision on agenda items and sub-items. This is intended to define boundaries and to induce the focusing on certain topics. During the discussion process, however, the initial boundaries may prove inadequate. A symptom of this is the duplication of discussion elements caused by too close relationship between two agenda items. Another circumstance is the gap created by the absence of related topics, which will mislead the contributor or lengthen the contributions in order to explain aŽ contribution fully, the group member has to add context that is not present in the current discussion structure ..

Whenever this situation arises, the coordinator should act promptly by re-structuring the discussion items. The re-structuring process may require, for example, an item to be split into two or more items, or two items to be aggregated, or new items to be created. In any of these cases, the elements associated with these re-structured items also have to be re-assigned to their new affinity. This is surely not an easy task. The sooner the coordinator detects this situation, the easier the re-structuring task will be. This re-structuring may require further checking by the contributors.

In SISCO, we attacked this problem by partitioning the re-structuring process into two levels. The first level represents a minor re-structuring that can be done by creating new items and establishing re-structuring relationships with existing items. This will redirect new contributions to the new items while maintaining the existing contributions associated with the old item. For example, two new items can be created to substitute for one original item. In this case, all new contributions are made to the new items and the old item is closed. A participant may access an old contribution by opening the new item that partially replaced it and browsing the substitution relationship.

In the second level the coordinator creates a new discussion structure and moves the existing elements to the new items. This is a manual process that in some cases will require editing the contents of elements in order to fit into the new structure. As we mentioned above, the result will have to be checked by contributors in order to preserve their original ideas.

3.3.3.2. Adding new participants. There may happen that new participants are needed as a pre-meeting discussion proceeds. These new participants are required because of their expertise or experience. In other cases, a new member has joined the team who will participate in the meeting. Sometimes, the purpose is to fill a gap caused by the absence of participants playing informal roles such as devil’s advocate or visionary. They need to be added to the participants list by the coordinator and their first task is to become well acquainted with the discussion. Whatever the reason for adding a new contributor, his group membership will be facilitated by the knowledge he can acquire from the GM.

In SISCO, adding a new participant during the development of a pre-meeting is simple. The only complication comes from the awareness mechanism. We assume that everything will be unknown to the newcomer. As he browses through the GM, the awareness mechanism resets the data representing the level of awareness. It is also possible for a participant to access a summary view of the GM and visualize his general level of awareness.

3.3.3.3. Maturity of discussion. At some point during the pre-meeting the coordinator may consider that the theme has already been exhausted and it is ready for the final discussion and decision process that will occur during the actual meeting. In this case, the coordinator may close the addition of contributions to this item, allowing the discussion to continue on other items.

As it was mentioned before, SISCO provides a participameter displaying quantitative measures about contributions. Of course, a high number of contributions is not a final verdict on the maturity of the discussion of an item. The coordinator should browse the contents of contributions in order to verify the quality and diversity of the contributions, and only then decide whether the discussion of this item should be closed.

On the other hand, if there are few or no contributions for an item, this indicates that some stimulus is required to motivate participation. Some actions already discussed are those performed by the coordinator or the facilitator who can try to incite contributions with controversial statements. This may be enough to stimulate interest and contributions to an item 15 .<sup>w</sup> <sup>x</sup>

In some situations, however, a low number of contributions is sustained even after adopting these actions. This might be a sign that radical actions have to be adopted. Among these actions, we can mention the discussion re-structuring and the adding of new participants, already discussed. In other cases, the lack of contributions is due to a high level of generalized equivocality. Participants are unable to contribute because they do not understand the very basic contents and objectives of the discussion. We suggest that, in this case, the discussion within the pre-meeting should stop and a brainstorm meeting should be called. After the equivocality is reduced the discussion can re-start, perhaps with a different structure.

## 3.4. Closing-up the discussion

After a period of discussion during which many contributions have been made to the meeting it will be the time to close the pre-meeting and prepare for the face-to-face meeting. It is the responsibility of the coordinator to decide when the discussion is mature enough to proceed to the meeting. This decision may cover the entire agenda or a subset of items.

## 3.4.1. Preparing for the meeting

At the time of the closure of a pre-meeting, a number of questions, positions and arguments have been generated. Participants are supposed to be aware of the contents of the discussion, but we believe that a reminder mechanism is necessary, particularly when the number of items is high. To help participants to access the discussion elements during the meeting, summary and cross-reference reports should be made available by the system.

In SISCO, we are studying the best format and contents of summary reports. We believe that the original model is not appropriate to certain types of data retrieval because sometimes it is necessary to bypass the hierarchy imposed by the model. String search tools and alternative data views by author, Ž for instance are examples that are under investiga- . tion.

## 4. Implementation issues

The implementation of an ASMP involves decisions on a number of issues, from the way to incorporate the discussion data model to the selection of a hardware platform in which the system is going to run. The following is a review of the most important ones and are exemplified with SISCO.

As it was mentioned in Section 2, the Group Memory includes the discussion and it must be structured. In the case of SISCO, the Group Memory has the structure shown in Fig. 2. The object classes are described below.

## 4.1. SISCO data model object classes

The basic class is the pre-meeting class, characterized by a title, a description and a deadline. The group members of a pre-meeting are described by the member class, characterized by user-id, name, affiliation, status and e-mail address. A subclass of the member class is the participant class. A coordinator of the pre-meeting is chosen from the participants. The participant class generalizes a class hierarchy representing the roles which participants can have in the interaction with each pre-meeting agenda item.

General topics that are part of a meeting agenda, supposed to be discussed in the pre-meeting, are described by the item class, characterized by name, description, creation-date and priority. A facilitator manages each discussion item. A goal pursued by the group as part of each item of the meeting agenda defines the objectiÕe class, whose attributes are name, description, status, creation-date and priority.

Assertions are made by contributors as part of a pre-meeting discussion and are represented by the element class, characterized by type, creation-date and content. The element is a generalization of the following classes: issue, position, argument, task and remark.

![](/api/attachments/XV8ZD2CV/fulltext/images/1a3f94132af63f8837559398c8a13de83f4ab1d015d95469b459f72e4c5056a8.jpg)  
Fig. 3. Discussion hierarchy.

Assertions expressing facts are represented by the pre-decision class, characterized by a name, a description and a creation-date. It results from decisions or common agreements on a subject occurred outside the pre-meeting discussions. A pre-decision is not to be questioned and should work as an assumption during the pre-meeting. It can specialize to a constraint class, representing a restriction to be considered during a discussion.

A reference material for consultation of group members defines the infobase class, with attributes: file-name, directory and supporting application. It points to a repository of information generated by some application, including a previous pre-meeting discussion.

## 4.2. SISCO implementations

As with any software system, the design of an ASMP involves the choosing of a hardware platform, the use of software tools including generators, li- Ž braries and customizable generalized systems , a user. interface, etc. The options available to the designers are the same open to the developers of any asynchronous CSCW system; a review of them can be found in Ref. 26 .<sup>w</sup> <sup>x</sup>

There have been four SISCO implementations up to date incorporating various subsets of the Discussion Data Model and the functionality described in the previous sections. N-SISCO 39 was imple-<sup>w</sup> <sup>x</sup> mented on a local PC network using Lotus Notes. O-SISCO 41 runs on an ORACLE environment<sup>w</sup> <sup>x</sup> with a TTY user interface. The two remaining implementations have had continuous work in the initial versions and some experiments have been carried on; a detailed comparison of both is found in Ref. 9 .<sup>w</sup> <sup>x</sup>

SISCO-RIO 8 has a client<sup>w</sup> <sup>x</sup> <sup>r</sup>server architecture. The server connects to the CA OpenIngres 1.1<sup>r</sup>04 DBMS via CGI and the client runs on any WWW browser. Its best feature is that the client can be used from any computer with an Internet connection and a Web browser. It can be tried at SISCO-RIO prototype 45 . In SISCO-RIO, contributors state and<sup>w</sup> <sup>x</sup> discuss their ideas through the inclusion of key elements such as issues, positions, arguments and remarks, following a pre-defined hierarchic structure. An example of how this structure is treated in SISCO-RIO is depicted in Fig. 3. The hierarchic structure expands or contracts as the user clicks the plus<sup>r</sup>minus Ž . <sup>"</sup> button. The top most level of the hierarchic tree lists all pre-meetings that the user participates followed by related items, objectives and elements.

![](/api/attachments/XV8ZD2CV/fulltext/images/8b01a1c2ba5cd313996a9ea9922dbb240709f17292a50f9e9254906db81a16cc.jpg)  
Fig. 4. U-SISCO User-interface.

U-SISCO 25 also has a client <sup>w</sup> <sup>x</sup> <sup>r</sup>server architecture. The server is a MiniSQL 1.0.16 DBMS and the client was developed in Java. Its best features are the portability of the server and the ability to use the client from a computer connected by an Intranet or Internet to the machine where the server is to be installed. Fig. 4 shows a U-SISCO window: in the upper part, a hierarchy of discussion entries concerning the Sevco Pre-Meeting. The highlighted issue is shown in detail in the lower part of the window. Additional versions are being developed including features not implemented in the first versions: graphical ‘‘participameter’’, discussion re-structuring and new user interfaces.

## 5. Conclusions

In this paper we addressed the main issues concerning the design of a pre-meeting system aimed at increasing the quality of the subsequent meeting. We chose an asynchronous system because it reduces the burden on participants’ schedules, which are usually demanding. Moreover, the asynchronous interaction allows time for participants to ponder other opinions and arguments, in order to build a comprehensive understanding of the items under discussion.

We divided the pre-meeting into four groups of activities: preparation, setting-up, development and closing-up. For each of these activities we described the issues we believe are more important to achieve the goals of the pre-meeting. We further divided the development activities into three sub-groups related to the contribution process, the monitoring and the general management of the discussion.

The contribution of this work is the value given to the preparation of the meetings, which may improve the complete meeting cycle. The experience we have obtained with the development of the SISCO project has allowed us to identify and analyze key issues in the design of an ASMP for this purpose.

The SISCO-RIO implementation has been tried in a small number of preliminary experiments. The motivation for such experiments was to test the functionality and the interface of the system. However, they also provided some hints about people’s reaction to the assumptions we made on meeting preparation activities and expected benefits. The results are far from conclusive as most experiments were carried out without the necessary planning and monitoring. We intend to increase the number and variety of controlled experiments in order to validate other assumptions and solutions that are under examination.

The initial reaction of people introduced to the system was very positive. However, as expected, the enthusiasm did not translate into high level of participation. Most people in the environment we tried lacked the required discipline to assign priority to pre-meeting activities. As a result, most participants limited their participation to the reading of other’s contributions. In spite of this, all participants agreed that the pre-meeting interaction helped them to make the meeting more productive than if it did not exist.

In a study about introducing meetingware technologies at Marriot 40 , the author proposes a num- <sup>w</sup> <sup>x</sup> ber of strategies aimed at motivating people to contribute and participate in the experiments. He noted that after an initial period of reluctance, most people become enthusiastic about the system, because they experience the benefits in their daily activities. We believe that the same process will probably occur when introducing SISCO in organizations.

We also observed that in a number of experiments the preparation seems to work best with participants that are new to the team. This might occur because new members are eager to show off their value to the team. There also has been a high level of participation when students were assigned grades according to their contributions the reward effect .Ž .

In general, we can conclude that the use of the system in decision groups has proven useful in the informal experiments we have carried out. The interaction with the system, however, is not trouble-free, with problems in understanding the data model and motivating participation. It should be noted that a full evaluation is out of the scope of this paper: an assessment of pre-meeting outputs based on the input variables must take into account all factors, including cultural and sociological aspects as stated by several authors 5,11,13,19 .

## Acknowledgements

This work was partially funded by the CYTED-SISCO project, by the National Science and Technology Fund of Chile, FONDECYT, under grant numbers 197-0342 and 198-0960, and by the Brazilian Research Council under the grant number 522036<sup>r</sup>96-1. An early version of this paper was presented at the 1997 Workshop on Information Technologies and Systems WITS’97 . M.C. Caval-Ž . canti, J. Espinosa, B. Maroja, M.Y. Endo and P. Pollard participated in the development of implementations.

## References

<sup>w</sup> <sup>x</sup> 1 Action Technologies home page. URL: http:<sup>rr</sup>www. actiontech.com.

<sup>w</sup> <sup>x</sup> 2 V. Balasubramanian, ‘‘Organizational Learning and Information Systems’’, URL: http:<sup>rr</sup>eies.njit.edu<sup>r ;</sup>333<sup>r</sup>olcover. html.

<sup>w</sup> <sup>x</sup> 3 G. Bellassai, M. Borges, D.A. Fuller, J.A. Pino, A.C. Salgado, SISCO: A tool to improve meetings productivity, Proceedings of the I CYTED-RITOS International Workshop on Groupware, Lisbon, Portugal, September 1995, pp. 149– 161.

<sup>w</sup> <sup>x</sup> 4 G. Bellassai, M. Borges, D.A. Fuller, J.A. Pino, A.C. Salgado, An IBIS-based model to support group discussions, in: B. Glasson, D. Vogel, P. Bots, J.F. Nunamaker Eds. , Ž . Information Systems and Technology in the Internationa Office of the Future, Chapman and Hall, London, 1996, pp. 49–62.

<sup>w</sup> <sup>x</sup> 5 I. Benbasat, L. Lim, The effects of group, task, context, and technology variables on the usefulness of Group Support Systems, Small Group Research 24 4 1993 430–462.Ž . Ž .

<sup>w</sup> <sup>x</sup> 6 R. Bentley, T. Horstmann, K. Sikkel, J. Trevor, ‘‘Supporting Collaborative Information Sharing with the World Wide Web: The BSCW Shared Workspae System’’. URL: http:<sup>rr</sup>bscw.gmd.de.

<sup>w</sup> <sup>x</sup>7 R.P. Bostrom, Successful application of communication techniques to improve the systems development process, Information and Management 16, 279–295.

<sup>w</sup> <sup>x</sup> 8 M.C. Cavalcanti, M.R. Borges, M.Y. Endo, SISCO-RIO: an asynchronous system to support meeting preparation, Proceedings of the III CYTED-RITOS International Workshop on Groupware CRIWG’97 , Madrid, Spain, 1997, pp. 25–32. Ž .

<sup>w</sup> <sup>x</sup> 9 M.C. Cavalcanti, J. Espinosa, B. Maroja, M.Y. Endo, Pre-Meeting Support Views based on the SISCO Model. Working Paper No. 05<sup>r</sup>97, Nucleo de Computacao Eletronica, Universidade Federal do Rio de Janeiro, Brazil, 1997.

<sup>w</sup> <sup>x</sup> 10 H. Chen, et al, ‘‘A Textual Database<sup>r</sup>Knowledge-base Coupling Approach to Creating Computer-Supported Organizational Memory’’, URL: http:<sup>rr</sup>ai.bpa.arizona.edu<sup>r</sup> papers<sup>r</sup>ijmms93<sup>r</sup>ijmms93.html.

<sup>w</sup> <sup>x</sup> 11 A.S. Clark et al. Groupware at Big Six Consulting Firms: How Successful was it?, Groupware: Collaborative Strategies for Corporate LANs and Intranets, in: D. Coleman Ed. ,Ž . Prentice Hall, NJ, 1997, pp. 533–561.

<sup>w</sup> <sup>x</sup>12 V.K. Clawson, R.P. Bostrom, R. Anson, The role of the facilitator in computer-supported meetings, Small Group Research 24 4 1993 547–565.Ž . Ž .

<sup>w</sup> <sup>x</sup>13 D. Coleman, Electronic meeting as today’s presentations, in: D. Coleman Ed. , Groupware: Collaborative Strategies forŽ . Corporate LANs and Intranets, Prentice Hall, NJ, 1997, pp. 183–191.

<sup>w</sup> <sup>x</sup> 14 E.J. Conklin, ‘‘Designing Organizational Memory: Preserving Intellectual Assets in a Knowledge Economy’’. URL: http:<sup>rr</sup>www.zilker.net<sup>r</sup>business<sup>r</sup>info<sup>r</sup>pubs<sup>r</sup>desom<sup>r</sup>.

<sup>w</sup> <sup>x</sup> 15 T. Connolly, R.L. Routhieaux, S.K. Schneider, On the effectiveness of group brainstorming, Small Group Research 24 Ž . Ž .4 1993 490–503.

<sup>w</sup> <sup>x</sup> 16 L. Constantine, Work organization: paradigms for project management and organization, Communications of the ACM 36 10 1993 35–43.Ž . Ž .

<sup>w</sup> <sup>x</sup> 17 L. Chidambaram, Relational development in computer-supported groups, MIS Quarterly 20 2 1996 143–165.Ž . Ž .

<sup>w</sup> <sup>x</sup> 18 R.L. Daft, R.H. Lengel, Organizational information requirements, media richness and structural design, Management Science 5 1986 554–571.Ž .

<sup>w</sup> <sup>x</sup> 19 R. Davison, Socio-psychological aspects of group processes, Working Paper QP95<sup>r</sup>03, City University of Hong Kong, June 1995, 41 pp.

<sup>w</sup> <sup>x</sup> 20 A. Dennis, Pootheri, S.K., V. Natarajan, ‘‘TCBWorks: A First Generation Web-Groupware System’’. URL: http:<sup>rr</sup>tcbworks.mgmt.uga.edu:8080<sup>r;</sup>adennis<sup>r</sup>tcbwh.htm.

<sup>w</sup> <sup>x</sup> 21 G. DeSanctis, R.B. Gallupe, A foundation for the study of Group Decision Support Systems, Management Science 33 Ž . Ž .5 1987 589–609.

<sup>w</sup> <sup>x</sup>22 P. Dourish, V. Bellotti, Awareness and coordination in shared spaces, In: Proceedings of CSCW ’92, ACM Press, Toronto, Canada, November 1992, pp. 107–114.

<sup>w</sup> <sup>x</sup> 23 V.J. Dubrovsky, S. Kiesler, B.N. Sethna, The equalization phenomenon: status effects in computer-mediated and faceto-face decision-making groups, Human–Computer Interaction 6 1991 119–146.Ž .

<sup>w</sup> <sup>x</sup> 24 C.A. Ellis, S.J. Gibbs, G.L. Rein, Groupware: some issues and experiences, Communications of the ACM 34 1 1991Ž . Ž . 39–58.

<sup>w</sup> <sup>x</sup> 25 J. Espinosa, J.A. Pino, P. Pollard, On the development of a

SISCO implementation using Java, Proceedings of the III CYTED-RITOS International Workshop on Groupware Ž . CRIWG’97 , Madrid, Spain, 1997, pp. 17–24.

<sup>w</sup> <sup>x</sup> 26 J. Favela, M.T. Soriano, M.A. Zapata, A Design Space and Development Process for Collaborative Systems, Proceedings of the III CYTED-RITOS International Workshop on Groupware CRIWG’97 , Madrid, Spain, 1997, pp. 33–42.Ž .

<sup>w</sup> <sup>x</sup> 27 F. Flores, M. Graves, B. Hartfield, T. Winograd, Computer systems and the design of organizational interaction, ACM Transactions on Office Information Systems 6 2 1988Ž . Ž . 153–172.

<sup>w</sup> <sup>x</sup> 28 Gramercy Books, Webster’s Encyclopedic Unabridged Dictionary of the English Language, Random House, New York, 1989.

<sup>w</sup> <sup>x</sup> 29 C. Gutwin, S. Greenberg, M. Roseman, ‘‘Supporting Awareness of Others in Groupware’’. URL: http:<sup>rr</sup>www.cpsc. ucagary.ca<sup>r ;</sup>gutwin<sup>r</sup>papers<sup>r</sup>suite-intro<sup>r</sup>intro.html.

<sup>w</sup> <sup>x</sup> 30 S.R. Hiltz, M. Turoff, The Network Nation: Human Communication Via Computer, Addison-Wesley, Reading, 1978.

<sup>w</sup> <sup>x</sup>31 W. Kunz, H. Rittel, Issues as Elements of Information Systems, Working Paper a 131, Institute of Urban and Regional Development, U. of California at Berkeley, 1970.

<sup>w</sup> <sup>x</sup> 32 G.L. Lohse, K. Biolsi, N. Walker, H. Rueter, A classification of visual representations, Communications of the ACM 37 Ž . Ž .12 1994 36–49.

<sup>w</sup> <sup>x</sup> 33 J.C. McCarthy, P.C. Wright, A.F. Monk, Coherence in textbased electronic conferencing: coupling text and context, Journal of Language and Social Psychology 11 1992 267–Ž . 276.

<sup>w</sup> <sup>x</sup> 34 J.C. McCarthy, V.C. Miles, A.F. Monk, M.D. Harrison, A.J. Dix, P.C. Wright, Text-based on-line conferencing: a conceptual and empirical analysis using a minimal prototype, Human–Computer Interaction 8 1993 147–183.Ž .

<sup>w</sup> <sup>x</sup> 35 S.E. McDaniel, G.M. Olson, J.C. Magee, Identifying and Analyzing Multiple Threads in Computer-Mediated and Face-to-Face Conversations, Proceedings of Computer Supported Cooperative Work CSCW’96 , Cambridge, USA,Ž . 1996, pp. 39–47.

<sup>w</sup> <sup>x</sup> 36 J.F. Nunamaker, A.R. Dennis, J.S. Valacich, D.R. Vogel, J.F. George, Electronic meeting systems to support group work, Communications of the ACM 34 7 1991 40–61.Ž . Ž .

<sup>w</sup> <sup>x</sup> 37 J.F. Nunamaker, A.R. Dennis, J.S. Valacich, D.R. Vogel, J.F. George, Group Support Systems Research: experience from the lab and field, in: L.M. Jessup, J.S. Valacich Eds. , Ž . Group Support Systems — New Perspectives, MacMillan Pub., New York, 1993, pp. 125–145.

<sup>w</sup> <sup>x</sup> 38 J.F. Nunamaker, R. Briggs, D.D. Mittleman, Electronic meeting systems: ten years of lessons learned, in: Groupware: Technologies and Applications, D. Coleman, R. Khanna Ž . Eds. , Prentice Hall, NJ, 1995, pp. 146–193.

<sup>w</sup> <sup>x</sup> 39 R. Parra, J.A. Pino, N-SISCO: A Notes implementation of SISCO, Proceedings of the I CYTED-RITOS International Workshop on Groupware CRIWG’95 , Lisbon, Portugal, Ž . 1995, pp. 125–137.

<sup>w</sup> <sup>x</sup> 40 C.D. Pietro, Meetingware and organizational effectiveness, in: D. Coleman, R. Khanna Eds. , Groupware: Technologies Ž . and Applications, Prentice Hall, NJ, 1995, pp. 437–473.

<sup>w</sup> <sup>x</sup> 41 F. Romero, ‘‘Sistema Colaborativo para el Apoyo Electronico ´

a Reuniones’’ in Spanish . URL: http: Ž . <sup>rr</sup>www.ing.puc.cl<sup>r</sup> <sup>;</sup>group<sup>r</sup>sisco.

<sup>w</sup> <sup>x</sup> 42 J. Rumbaugh et al., Object-oriented Modeling and Design, Prentice-Hall, Englewood Cliffs, NJ, 1991.

<sup>w</sup> <sup>x</sup> 43 M. Sarkar, M.H. Brown, Graphical fisheye views, Communications of the ACM 37 12 1994 73–83.Ž . Ž .

<sup>w</sup> <sup>x</sup> 44 SISCO project home page. URL: http:<sup>rr</sup>www.nce.ufrj. br<sup>r ;</sup>sisco.

<sup>w</sup> <sup>x</sup> 45 SISCO-RIO prototype. URL: http:<sup>rr</sup>www-aep.nce.ufrj. br<sup>r</sup>sisco.

<sup>w</sup> <sup>x</sup> 46 M. Sohlenkamp, G. Chwelos, Integrating communication, cooperation, and awareness: DIVA virtual office environment, in Proceedings of CSCW ’94, ACM Press, Chapel Hill, USA, 1994, pp. 331–343.

<sup>w</sup> <sup>x</sup> 47 J. Szerdy, M.R. McCall, How to facilitate distributed meetings using SEM Tools, in: D. Coleman Ed. , Groupware:Ž . Collaborative Strategies for Corporate LANs and Intranets, Prentice Hall, NJ, 1997, pp. 207–230.

<sup>w</sup> <sup>x</sup> 48 J.S. Valacich, J.F. George, J.F. Nunamaker, D.R. Vogel, Physical proximity effects on computer-mediated group idea generation, Small Group Research 25 1 1994 83–104.Ž . Ž .

<sup>w</sup> <sup>x</sup> 49 D.R. Vogel, J.F. Nunamaker, Design and assessment of a group decision support system, in: J. Galegher, R. Kraut, C. Egido Eds. , Intellectual Teamwork. Lawrence Erlbaum As- Ž . soc., Hillsdale, NJ, 1990, pp. 511–528.

![](/api/attachments/XV8ZD2CV/fulltext/images/4869ef39e46a58df2a3d10eb2bdde8b7ab59adcbe23cd04033160cad9293818e.jpg)

Marcos Borges is an Associate Professor at the Federal University of Rio de Janeiro. Dr. Borges received his PhD from University of East Anglia, England, in 1986 and since then is an Associate Professor at Federal University of Rio de Janeiro, Brazil. Dr. Borges works as a Consultant for TDI Brazil, a company aimed at deploying new technologies to corporations. Before founding TDI Brazil, Dr. Borges worked as a visiting professor at Santa Clara Univer-

sity and as a Senior Consultant at TDI, Inc, both in Santa Clara, California. His areas of interest include workflow and other groupware tools, especially EMS.

![](/api/attachments/XV8ZD2CV/fulltext/images/ee04f40ae38b1f8c048a9bb83ee626b2b6eb7cfd29d9182e578bd626d5bdbefa.jpg)

Jose A. Pino is currently Associate Pro-´ fessor of Computer Science at the Universidad de Chile. His research interests include Human–Computer Interaction, Computer-Supported Collaborative Work and Software Industry Studies. He has served as President of the Chilean Computer Science Society SCCC andŽ . President of CLEI the Latin AmericanŽ Association of Universities concerning Information Technology . He is cur-. rently the International Coordinator of

the CYTED RITOS research network. He has co-authored six books and published research papers in international conferences and journals, including Journal of the ACM, Communications of the ACM, Interacting with Computers and Journal of Microcomputer Applications.

![](/api/attachments/XV8ZD2CV/fulltext/images/00d9dacd10348fa355342a65c775bdcd2bba832d0606e27b60a9fda6164b2a05.jpg)

David A. Fuller is an Associate Professor of Computer Science at the Pontificia Universidad Catolica de Chile. He´ received his PhD in Computer Science from Imperial College of Science, Technology and Medicine at the London University, England, a MS. in Computer Science from the University of California, Los Angeles, and a BS in Electrical Engineering from Pontificia Universidad Catolica de Chile. His research interests´ include collaborative systems, systems

development, object-oriented frameworks and visual programming.

![](/api/attachments/XV8ZD2CV/fulltext/images/82871f85406166294a47ddef5d07f48b354559c0482b96d1801858bb857e51d2.jpg)

Ana Carolina Salgado is an Associate Professor at the Universidade Federal de Pernambuco, Brazil Department of In-Ž formatics . She obtained her Doctorate. from the University of Nice France inŽ . 1988. Her main research interests are in the area of non-conventional databases, specially geographical databases, interoperability of heterogeneous databases and cooperative systems. Dr. Salgado has published over 40 technical articles in conference proceedings and journals.

She is a member of the Brazilian Computer Society and of its Special Interest Group for Computer Science Education. She also held office as chair of the Informatics Department and as head of undergraduate studies.
