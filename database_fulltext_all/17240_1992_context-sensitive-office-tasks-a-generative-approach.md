---
otero_id: 17240
otero_key: "74ZFZBDT"
title: "Context-sensitive office tasks a generative approach"
authors: "Knut Hinkelmann; Dimitris Karagiannis"
year: "1992"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(92)90018-k"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Context-sensitive office tasks A generative approach

Knut Hinkelmann \*

DFKI GmbH, D-6750 Kaiserslautern, Germany

Dimitris Karagiannis

FAW Ulm, D-7900 Ulm, Germany

Organizational knowledge is one of the most important aspects in office systems. Supporting task processing in the office domain can be viewed as organizational Computer-Supported Cooperative Work (CSCW). We describe three layers for modeling and processing office tasks: Conventional systems have predefined static models representing a structured task plan. The generation of a task plan at starting time can take into account the actual context giving simpler and more adequate plans. Techniques from traditional office automation are combined with inference mechanisms and Artificial Intelligence techniques for knowledge-based information systems. This approach is described in detail. In the third, most flexible approach, called ‘acting by opportunity’, the office worker has the possibility to perform actions independently from a task plan. The task processing system has to update the generated task plan according to user-driven deviations.

Keywords: Office automation, Computer-supported cooperative work, Artificial intelligence, Knowledge representation, Planning.

## 1. Introduction

With the development of local- and wide-area networks, mail systems, and multi-user databases, computers will be more and more used to increase organizational effectiveness. This so-called Computer-Supported Cooperative Work (CSCW) can be classified in three categories [EL88]:

\- Collaboration within a group geographically colocated at the same time.

\- Real-time collaboration among people who are geographically distributed.

\- Asynchronous collaboration among teams/persons geographically distributed.

Another classification is given by [Hun88]: Collaborative CSCW tools improve the productivity of meetings or document creation by increasing their efficiency. They are more or less static, i.e. they merely manage information and communication. Examples are the conference room system CoLab developed at Xerox Palo Alto Research Center and shared screen systems like videoconferencing. In organizational CSCW the amount for meetings is reduced, and collaborative document creation is promoted by automated support of communication and coordination. These systems include programs that track or facilitate the division of tasks, or those that monitor resources and performance. They are actively managing tasks, running jobs and telling people to do things.

![](/api/attachments/74ZFZBDT/fulltext/images/c51c1b7964513006e6dc490ca003fb7f2eb6d4785580fd7383df3a2724a89fe8.jpg)  
Dimitris Karagiannis holds a degree in Computer Science at the University of Berlin where he also did his thesis in the field of Artificial Intelligence and Databases. Since 1988, he has been working as senior scientist at the Research Institute for Applied Knowledge Processing (FAW) in Ulm/Germany.

![](/api/attachments/74ZFZBDT/fulltext/images/d4997df677c9f77002f286dccf3b468f4021b75879fa0a82f404b556f852f5d9.jpg)  
Knut Hinkelmann finished the study of Computer Science at the University of Kaiserslautern in 1988. From 1988 to 1990 he worked at the Research Institute for Application-Oriented Knowledge Processing (FAW) in Ulm where he was mainly engaged in the domain of office automation. Since 1990 he is working at the German Research Center for Artificial Intelligence (DFKI) in Kaiserslautern.

In our project we are engaged in supporting cooperative work in a complex office domain. Office work can be decomposed into a number of actions. A multitude of actions aspiring the satisfaction of one goal are named a task. Thus, a task is a set of actions – also called activities or processes – with logical dependencies. A task's activities may be executed sequentially or in parallel depending on logical and time constraints. If several workers are involved in one task it is called a cooperative task. Well-known examples of tasks are the editing of a scientific journal (see [Zis78], [CL88]) with actions like “ReviewPaper”, “GetReviewers” or the application for an official journey (see [WK85]) with actions like “PermissionOfJourney”, “TravelReimbursement”.

Tasks often do not follow a strict plan. Their execution is influenced by three criteria:

1. Guidelines of an organization prescribe how a task is to be processed, i.e. which jobs have to be performed; they clarify competences and specify details of the execution. Some very general guidelines may be applicable in several tasks, e.g. responsibilities for finances.

2. Short- and middle-term changes in working processes may result if a person is on holiday, if resources are not available etc. Reactions on these changes also depend on guidelines, which are relevant only in exceptional cases, however.

3. Office workers involved in a task have individual freedom when and how to do a job – as long as it is not specified by guidelines.

The aim of our work is to develop an organization support system integrating (a) task processing with two other basic components of office systems: (b) communication and (c) document and information management. Concepts from traditional office automation are combined with Artificial Intelligence techniques in order to develop knowledge-based office information systems that use new knowledge representation and inference mechanisms (cp. [Kar89]). Following the above classifications supporting task processing in an office belongs to organizational CSCW with asynchronous collaborations.

Using such an organization support system an office worker – called the task initiator – determines his goals and the system infers the activities to satisfy them. Some activities can be executed automatically by the system itself, e.g. the transmission of messages to internal or external co-workers using the communication subsystem. Other activities require user interaction. In this case a competent office worker – called the agent – is chosen by the system. He is requested to perform the activity which is put into his personal task agenda. The agent can execute the action whenever he likes unless he exceeds a given deadline. When the agent decides to execute a task activity the system supplies him with all documents and information necessary to fulfill his job. As soon as the activity is finished, it is deleted from the agent's personal agenda. The system looks for other activities which are now ready for execution. A task execution stops, if there are no actions to perform anymore.

We distinguish three levels of task modeling. A first approach represents a task as a structured plan of actions. A task administrator (also called task programmer) analyzes the company's guidelines. Every step of task execution is programmed and every branch is explicitly modeled. This approach strictly follows the first of the given criteria for task processing; however, because of the dynamic office work this approach is too rigid. Taking into consideration criteria 2, every possible exception would have to be expected in advance and included into the plan by conditional branches leading to swelled, complex plans. Thus, this approach is not practical in real office environments.

To overcome the deficiencies of this first approach, the generation of structured plans has been evolved. The analysis and interpretation of guidelines to develop a task plan is performed by the system itself as soon as the task is initiated. Known exceptions – as referred to by criteria 2 – can be considered in advance at task starting time, thus leading to much simpler plans. The result of task generation is a context-sensitive plan taking into account the actual situation known at the time when the task is started.

Although this approach is more adequate than the previous one it does not necessarily satisfy criteria 3. To really satisfy this criteria the task initiator as well as any agent of the task must have the possibility to modify the task structure if it seems appropriate to him or if constraints independent from the actual task demand it. For instance, if he knows that a computer will go down in 10 minutes he should start a later action, requiring this computer, although not all of its preconditions are satisfied already. We will call this kind of task processing acting by opportunity.

These task processing approaches will be exemplified with the task of inviting a guest lecturer to a research institute. The example together with the approach of task modeling by structured plans is described in the next section. The main part of the article deals with the generation and processing of context-sensitive plans (chapter 3). A few considerations integrating acting by opportunity are presented in chapter 4.

## 2. Task processing with structured plans

Most existing task-processing systems use what [WL87b] calls a ‘procedure automation approach’. Cooperative tasks with multiple agents are explicitly represented as a structured sequence of office activities, i.e. the flow of work through an enterprise is explicitly modeled. In order to represent the specification of a task kinds of Petri nets like the one in [WK85], augmented Petri nets [Zis78], production system nets [FW89], activity networks [TLF88] and also rule systems are used forming a model of the task. Such a model contains all potential actions and establishes their order of execution, branches and conceivable alternatives. In these approaches the development and maintenance of the task model requires a task administrator [LHWM88], who analyses the general and task-specific guidelines, interpretes them and forms a task model. He has to be familiar with the system and the company or enterprise the system is applied in.

We will present this approach with a simple example happening in a research institute with various research projects and a management led by a director. Imagine a researcher working in a project who wants to invite a guest researcher to give a lecture at the institute. If his project leader agrees with the invitation the director has to permit it, because he has the financial competences for honorary and reimbursement of travel expenses. If the permission is given the guest is invited and the talk is announced. After the talk the guest will get his fee and his travel expenses reimbursed. This example is presented with a Petri net in fig. 1. The rectangles can be implemented as procedures which determine how the actions are to be performed.

![](/api/attachments/74ZFZBDT/fulltext/images/0e2ba991eedc45092d1717cc5a8c92cdd59e709a2d23dc26a7cdbed7e93237f3.jpg)  
Fig. 1. Example task: inviting a guest lecturer.

Initiating a task means to select the right net or plan, instantiate it, i.e. select the persons who have to perform actions, specify infrastructural resources, documents, and time constraints etc. and start the execution. However, if the guest is invited by a project leader or the director himself, some activities in the plan of fig. 1 are superfluous. Thus, before plan instantiation an extraction phase can be fit in, extracting the relevant subplan (i.e. the essential nodes) for the actual task (cp. fig. 2).

This kind of task modeling is rather rigid. Every possible exception has to be included into the plan. If, for instance, in absence of the project leader the permission can be given by the director directly, this has to be explicitly modeled as indicated by the dashed line in fig. 1. The same holds for many other exceptions of how actions can be executed. E.g. while the announcement of a lecture is conventionally presented at the bulletin board it must be distributed by electronic mail, if the time between announcement and lecture is very short.

![](/api/attachments/74ZFZBDT/fulltext/images/1e9c25260bf80fddaf280ab891ac5543eb15ac0059d5b23214537d401120c679.jpg)  
Fig. 2. Generative task processing: Generating plan 1 or plan 2.

In addition to the detailed representation of task plans, [LHWM88] gives office workers the opportunity to add their own aspects by completing or modifying tasks. However, the disadvantage of this structured plan approach is not removed, because the plan remains very complex and the system itself can not react on exceptional situations.

## 3. A generative approach for task processing

The a priori generation of accurate structured task plans (chapter 2) is not feasible in complex real world domains. The predefined task structure should be as flexible as possible. Included in the task plan are many conditional branches. When executing a task one of these branches is chosen depending on the actual state of the task. Many of these decisions, however, can be made already at starting time. Therefore the exact specification of a task plan should be delayed until there is enough information to make it optimally adequate. A context-sensitive plan can be generated at the time when the task is started taking into account the actual situation known at this time. It should be rather indefinite and will be made more precise during execution when additional information is available.

A system roughly following this scheme is POLYMER [CL88], which uses interactive planning. A task manager specifies what has to be done, how it should be done, who should do it and when it must be done. He is responsible for planning and performance of the task. A planning system refines the initial plan and resolves inconsistencies arising from an incomplete or wrong domain model or from user-driven deviations from the initial plan.

As already described in chapter 1 task processing depends on guidelines, the actual situation and individual freedom of the office worker. The way in which to perform a task is prescribed by the guidelines of the company. These guidelines do not specify a concrete task plan, but they determine rules how to process a job. The guidelines, however, are not strictly assigned to one task. On the contrary, there are very general guidelines which are applicable in many different tasks.

In our generative approach we will concentrate on the automatic generation of a task plan. $^{1}$ Instead of having a task administrator ([LHWM 88]) or task manager ([CL88]) to be responsible for specifying a task plan we will present a system interpreting the guidelines of the company with respect to the actual situation and thus generating a context-sensitive task plan by itself. The term ‘context-sensitive’ means, that unlike the plans of chapter 2 the task plan does not include all task variations. It is an adequate model in accordance to the actual context. A similar approach is developed in the area of machine learning, called ‘sloppy modeling’ [Mor89]. To obtain this possibility the guidelines themselves have to be represented in the system.

## 3.1. Representing office knowledge

In analogy to declarative programming languages our generative task processing approach separates control from domain knowledge. An adequate conceptualization of domain knowledge plays a dominant role as [Wim89] argues, where a general framework for knowledge representation is given. Domain knowledge includes three sources of knowledge (cp. [KK87]):

\- organizational knowledge: knowledge about projects and responsibilities of persons and departments; infrastructural knowledge about non-human resources and actual data-like schedules,

\- knowledge about office activities which can be composed to tasks,

\- knowledge about guidelines for office work.

Control is undertaken by two subsystems for (1) task generation (also called task planning) and (2) task execution. Task generation forms a task plan out of predefined activities. Activities are selected by goals which they contribute to reach. Guidelines of various specificity (general, company-specific and task-dependent) determine generation as well as execution of tasks. Depending on changes in current organizational knowledge identical goals may result in different task plans.

## 3.1.1. Organizational knowledge

For representing the organizational knowledge, object-oriented tools are used; these are also proposed by [TFGN87] and [WL87a]. Since our system is implemented in KEE, $^{2}$ the objects are called units. Objects consist of two parts: a control part defining methods and a conceptual description. The conceptual description is given by definitions of the object's properties which are called slots. Objects are described by classes and organized in inheritance hierarchies. A simplified conceptual description for a class Research-Project could look like

```txt
class: ResearchProject
    Superclass: Department
    ProjectLeader: (of class Researcher)
    ProjectMember: (of class Researcher)
    Theme: unknown
    Organization: (of class Organizational-Structure)
...
```

Representations of specific real-world things are instances of these classes, e.g. a project occupied with the development of organization support systems:

```yaml
Unit: OSSY-Project
class: ResearchProject
ProjectLeader: John
ProjectMember: Paul, George, Ringo
Theme: ``Organization Support Systems''
Organization: LineStructure
...
```

![](/api/attachments/74ZFZBDT/fulltext/images/6938f1de87d2cd907c571ef224d639c6c66bb224ec49eafdd53bb42c1f39e552.jpg)  
Fig. 3. A hierarchy of activities (detail).

## 3.1.2. Guidelines

Labour in a company or institute is directed by a large set of guidelines. They can be found in the organizational handbook of the company and lay down, for instance, who is responsible for which jobs; they can determine which single actions are necessary to make an official journey, who is allowed to permit this journey, how much money is reimbursed etc. For the representation of these guidelines production rules are appropriate, because they are similar to their conventional description. Three kinds of rules can be distinguished: $^{3}$

\- generation rules to determine activities (by declaring goals)

```txt
IF (an Object of CurrentTask is ?lecture)
(?lecture is in class Lecture)
THEN (a Goal of CurrentTask is
'(the Permission of ?lecture is
?yes.or.no))
(a Goal of CurrentTask is
(the Date of ?lecture is ?date))
```

"A lecture has to be permitted and the date must be appointed."

\- sequencing rules to plan the sequential order of action execution:

```txt
IF ...
(an Activity of CurrentTask is ?Permission)
(an Activity of CurrentTask is ?DateSetting)
...
THEN (a SubsequentActivity of ?Permission is ?DateSetting)
(a Precondition of ?DateSetting is (the Goal of ?Permission))
```

"Before permission the date has to be fixed"

\- rules for task execution:

```txt
IF (an Object of CurrentTask is ?lecture)
(the lecturer of ?lecture is ?guest)
(the TravellingDistance of ?guest is far)
...
THEN (the Reimbursement of Expenses is 100)
```

"If the travelling distance of the guest lecturer is very far, he will get reimbursement of his travel expenses of 100 per cent"

The guidelines vary from specialized to very general ones. As a consequence, some guidelines have to be used in different tasks. For example, the guideline, that a permission has to be given on the application form is applicable in nearly all permission procedures. Rules representing the guidelines can be collected to rule classes whereby the same rule can belong to several rule classes. Referring to a rule class selects all the rules of the class. Thus, the general rules, which belong to multiple classes, can be used for many different tasks.

Many objects in our knowledge base - especially activity descriptions - have a slot Guidelines referring to rules (see also Permission in fig. 4):

```txt
Class: Lecture
    Superclass: Event
    Lecturer: unknown
    Theme: unknown
    Date: unknown
    Permission: (one.of granted rejected consultation)
    Guidelines: PermissionGuidelines,
    TravellingGuidelines,
    LectureGuidelines
....
```

These rules are added to the slot Guidelines of those activity instances, which affect the object. They are applied when executing the activity. General rules are referenced by many objects, while for specialized jobs there are specialized rules.

The representation of office tasks and actions also fits into the object-oriented concept as shown by [CL88] or [Kem88]. The actions are also structured in an object hierarchy, part of which is shown in fig. 3. There are system activities, which are executed like programs without any user interaction, and activities being activated and executed by one or multiple persons. The latter person's activities can be either atomic or composed of subactivities.

Since activities are dynamic objects the definition of the control part is very important. For each activity there are predefined methods for activation and execution control. Other methods can be triggered by the user if he wants additional information or if he wants to delay the execution or if he wants to cancel or reject an action because he feels not responsible. The conceptual part of an action is defined by properties like involved persons and resources, conditions for their activation, sequencing relations to other actions etc. To each activity definition its semantics is described – in our current version of the system by definition of goals that the activity can reach. Goals are atomic formulas which are true when the activity has been finished. The class description of Permission is presented in fig. 4. Most of the slots are still uninstantiated. They will be instantiated shortly before execution time when the activity instance is activated. This is the time when information is most detailed and reliable.

## 3.1.3. Activities

```txt
class: Permission
    Superclass: ComposedActivity
    Agent: unknown
    Documents: unknown
    Object: unknown
    Guidelines: PermissionGuidelines
    Goal: (the Permission of ?x is ?y)
    Preconditions: (the Application of ?x is proposed)
    SubsequentActivities: unknown
    Subgoals: (the Applicant of ?x is notified)
    SubactivityClasses: FillingForm
    Subactivities: unknown
    Start: <method>
    Activate: <method>
    Delay: <method>
    Inform: <method>
    Cancel: <method>
    Reject: <method>
...
```  
Fig. 4. Class description for activity permission.

The most important slot for task planning is the slot Goal. In the activities' class definitions this slot is filled with uninstantiated formulas determining the purpose, which the activity is to be applied for. Activity instances are generated during task generation. Then the slots Preconditions and SubsequentActivities are instantiated linking activity instances and thus building up a task plan. They determine the logical dependencies and sequential order of activity execution.

The slots SubactivityClasses and Sub-goals specify, which kind of subactivities contribute to an activity instance which is composed of subactivities. They play a role in the phase of fine planning during task execution. Permission is an activity consisting of two subactivities: Filling in a form and notifying the applicant whether the permission is given or not.

As can be seen from this example, activities can be rather general so that they can be used for various different tasks. Thus, the Permission activity may be used for official journeys as well as holiday permissions or even invitation of guest researchers (see below).

## 3.2. Planning context-sensitive tasks

## 3.2.1. Generating activities

To start a task an office worker – called the task initiator – describes what he wants to do. In the simplest case he presents one or more goals to the system and gives references to relevant objects. He can also give definitions of new objects, e.g. the partial description of a lecture if he intends to invite a guest lecturer:

```yaml
Unit: LectureDagobert
    InstanceOf: Lecture
    Lecturer: DagobertDuck
    Theme: "How to increase your money"
    Audience: 50
```

Then, for instance, a goal presented by the initiator could be

```txt
(the Hotel of Lecture Dagobert is ?hotel)
```

The task initiator's specifications determine access to relevant parts of the organizational knowledge base leading to the selection of appropriate guidelines. Thus, in the class description of Lecture the rule classes PermissionGuide-

Lines, TravellingGuidelines and LectureGuidelines are referred to. The generation rules of these rule classes infer goals that must be satisfied during task execution. The goals determine milestones of the task but do not say anything about how they are to be reached. For example the generation rule given in section 3.1.2 will derive the goals

```lisp
(the Permission of LectureDagobert is ?yes.or.no)
(the Date of LectureDagobert is ?date)
```

Now the task initiator has the chance to manipulate the goal list. He can add further goals or delete some of the goals if they seem not necessary or if he wants to do the job in his own way. As soon as the goal list is fixed, the system has to find activities that can help to satisfy the goals. It iterates over the list of goals and tries to unify them with the formulas in the Goal slot of the activity classes. For each successful unification a new instance of the activity class is created. For example the goal (the Permission of LectureDagobert is ?yes.or.no) is unifiable with the formula in the Goal slot of the activity class Permission with unifier $\sigma$ and binding ?x to LectureDagobert. Consequently, a new instance of this class is created – call it Permission-1 – and all formulas in the slots Preconditions and Subgoals of this new activity are instantiated according to $\sigma$ . The new activity Permission-1 now has the following new slot entries:

```yaml
Unit: Permission-1
    InstanceOf: Permission
    Object: LectureDagobert
    Goal: (the Permission of LectureDagobert is ?y)
    Preconditions: (the Application of LectureDagobert is proposed)
    Subgoals: (the applicant of LectureDagobert is informed)
    ....
```

According to this scheme instances of the activity classes HotelReservation and DateAppointment are generated.

Further activity instances can be derived interpreting the preconditions of generated actions as goals, too. The precondition of an action A means, that A can not be executed before the precondition has been satisfied. Hence, there must be activities to satisfy these preconditions.

As the precondition of Permission-1 is unifiable with the goal formula of the activity class Application a new instance of this class is generated. As a result of our generation phase we have four activity instances:

```txt
Permission-1
Application-2
DateAppointment-3
HotelReservation-4
```

## 3.2.2. Sequencing activities

To get a task plan also the order of execution has to be arranged. Execution order is a partial order. For two activities A and B we say that $A \prec B$ , if A has to be executed before B. A task plan is represented implicitly by the slots SubsequentActivities and Preconditions linking two subsequent activities. If $A \prec B$ , then the goal of activity A is added to the preconditions list of B and the name of B is inserted into the slot SubsequentActivities of A. Concurrency is a basic property of office work, which has to be taken into account during task planning, as described in [SR86]. So some conditions – called ‘prevail conditions’ – must hold for the whole duration of the action, and therefore must not be made false by any concurrent activity. However, for reasons of simplicity these are omitted in this paper.

In principal there are two ways to determine the order between two activities: First, $A \prec B$ for every activity A created to satisfy a precondition of a previously generated activity B. Since the activity Application-2 should satisfy the precondition of Permission-1 it has to be executed first. Therefore Permission-1 is inserted as a value to the slot SubsequentActivity of the application activity.

The second way to find a rule ordering is via sequencing rules. Applying the sequencing rule in section 3.1.2 derives that Permission-1<DateAppointment-3. Fig. 5 shows a graphical representation of the resulting task plan for our little example. In the object descriptions only the slots determining the execution order are presented.

It should be especially emphasized that the task generation phase considers the actual situation. Depending on the context at starting time tasks are planned and executed in different variations. Fig. 6 shows two distinct plans of the same task for inviting a guest lecturer. Both tasks had been initiated by a project leader so that the first step of the task (see fig. 1) was superfluous. Additionally the task initiator of plan (b) did some actions by himself before starting the system. As the lecture should take place within 5 days the task initiator personally contacted the director for giving his permission. As a consequence the activities of permission and date appointment are not included in the task. Another simplification of plan 2 has its origin in the fact that the lecturer had a short journey and thus the action for hotel reservation was dropped.

![](/api/attachments/74ZFZBDT/fulltext/images/bcf74f4ee0b6058a2e34e7ad8fba5db4ac027937d7e1359e0b79461ced0edd6b.jpg)  
Fig. 5. Activity ordering by Preconditions and SubsequentActivities.

## 3.3. Hierarchical planning

In the first phase of task generation only activities immediately contributing to predefined goals had been created. Subactivities of composed activities are not yet created. This is delayed until fine planning while executing the activity. Generating activity instances as late as possible will result in more suitable plans, because at execution time more actual data are present. Thus, as an advantage of this hierarchical planning we get an increase in flexibility. By the way the task planning is simplified, because fewer actions have to be analyzed for execution ordering.

## 3.4. Executing context-sensitive tasks

When the task generation is finished, those actions with satisfied preconditions will be activated. First, outstanding information is derived: the office worker responsible for execution – the agent – is determined, the documents and forms are made available, the deadline can be computed etc.

## 3.4.1. Fine planning

When a composed activity has to be executed the subactivities are computed in a fine planning phase:

1. A new instance is created for every activity class listed in the slot Subactivity-Classes.

![](/api/attachments/74ZFZBDT/fulltext/images/8bea339185d39f2388f07d59fe02985289f95d0135a2cfba7a17177670c52cc6.jpg)

![](/api/attachments/74ZFZBDT/fulltext/images/179ed1529ed30fc0fedb982c3f2c3a7f0eed393476d6ceb2c5fec3c77d4b9886.jpg)  
Fig. 6. Two plans for the task of inviting a guest lecturer.

2. Generating activities for subgoals proceeds in the same way as described in section 3.2 for the activity's main goal.

All these subactivities are recorded in the slot Subactivities of the superior activity and the execution order is committed. Activating the first subactivity can recursively start another fine planning phase, if it is a composed activity itself. Looking at our example, the fine planning for the activity Permission-1 could find the following informations with new subactivities FillingForm-5 and Notification-6:

```txt
Unit: Permission-1
    InstanceOf: Permission
    Agent: John
    Documents: Form-125
    Guidelines: PermissionGuidelines
    SubsequentActivities: unknown
    Object: LectureDagobert
    Goal: (the Permission of LectureDagobert is ?y)
    Preconditions: (the Application of LectureDagobert is proposed)
    Subgoals: (the applicant of LectureDagobert is informed)
    SubactivityClasses: FillingForm
    Subactivities: FillingForm-5, Notification-6
```

## 3.4.2. Activity execution

For activities we have to distinguish between system activities and jobs that are to be done by office workers. System activities are carried out like programs as soon as possible. If the activity has to be executed by a human agent, this person is sent a request. Every office worker has a personal agenda containing all his actual jobs. In principal he can perform his jobs at a time he likes. Only if there is a deadline for an activity the system will send the agent a reminder. When the agent has decided to attend to an activity, the start method of the activity object is executed.

In our example, John is the agent of the action Permission-1. Therefore the action is added to his agenda. As soon as he starts the action a text system presenting the application form Form-125 will be opened. In this case John has the possibility to ask for information about the current status of the task and about all the data necessary to do his job. In the case of Permission-1 it may be necessary for John to know, how much fee the guest lecturer should get, how many other lectures are planned, he may also want to see his personal calender for entering the lecture data etc.

As soon as the execution of an activity is finished, its subsequent activities are analyzed whether their preconditions are satisfied. All subsequent activities with satisfied preconditions are activated. Subsequent activities with preconditions that are still unsatisfied are delayed. In the task generation phase, however, for every precondition in every activity instance a particular action had been generated. Additionally all actions are linked by the slot SubsequentActivities. Therefore for every precondition of an activity A there exists an activity $B \prec A$ and A is a SubsequentActivity of B. As a consequence, analyzing only the subsequent activities of finished actions will ultimately find all executable activities. Task execution stops, if all activated activities are executed and no further activities with satisfied preconditions do exist.

## 4. Acting by opportunity

Following the approach of generating and executing context-sensitive office tasks as described in the previous chapter, an office worker has the possibility to perform his tasks whenever he wants. However, this does not give him full individual freedom in doing his work as it is possible in the real office domain. The generated activities are fixed, they can not be deleted or replaced. As soon as an agent starts a job the corresponding method is executed. This method is a predefined sequence of activity steps that are to be performed with all the drawbacks of the first approach. The office worker may only interrupt and delay them to procure needed information. The advantage of this approach compared to the detailed definition of the whole plan structure (chapter 2) is that the exceptions have to be anticipated only at the level of activities instead of the level of the whole task.

To give an office worker full individual freedom in doing his work he should be able to change the order of activity execution in a task, to replace a whole set of actions, to add new activities to achieve new goals etc. This presupposes, however, that the system has any knowledge about the semantics of activities. The definition of methods alone does not suffice. If the office worker does his own variations of the generated task plan, it may happen that this plan will become inconsistent with the system's internal state. In this case the system must detect whether some preconditions have already been satisfied by a user and then modify its plan to reach a consistent state. This can be achieved by reordering activities, rejecting previous assumptions, or dropping goals or actions.

Assume that the task plan of inviting a guest lecturer as shown in fig. 1 had been generated. Now imagine that the director may intervene in the execution: To permit the invitation he may offer the lecturer an overall amount for fee and reimbursement of travel expenses, but under the condition, that the guest has to reserve and pay the hotel room by himself. In this case the actions Hotel Reservation and Permission are combined although they are not subsequent in the plan. The system has to detect this variation and delete the action Hotel Reservation from the plan.

## 5. Conclusion

In this paper we presented three layers to achieve full flexibility in supporting task processing in a real office domain. The simplest approach is the predefinition of a structured plan for each task to be supported. This approach has poor possibilities to react on any exceptional cases, because it seems impossible to anticipate all of them at definition time. Generating a context-sensitive plan when starting a task can take into consideration all the exceptional information known at that time. A system has been implemented as a “demonstrator” according to this methodology. It was developed on a workstation under UNIX by using the Knowledge Engineering Environment KEE. $^{4}$ For this system a simulation tool has also been realized. Thus, we got empirical results about the utilization factor of the working places and resources in the office environment. Analyzing these results we found that giving the office workers more freedom in doing their jobs would be more effective and could be more satisfying for them, thus also leading to a better acceptance of the system in a real office. This forced us to the third layer called acting by opportunity, where any office worker can intervene in the execution of a task unless he passes his competences.

## References

[CL88] W.B. Croft and L.S. Lefkowitz. A Goal-Based Representation of Office Work. In W. Lamersdorf, editor, Office Knowledge: Representation, Management, and Utilization. Elsevier Science Publishers B.V. (North Holland), IFIP, 1988.

[EL88] D. Engelbart and H. Lehtman. Working Together. BYTE, December 1988.

[FW89] H. Fleischhack and A. Weber. Rule Based Programming, Predicate Transition Nets and the Modeling of Office Procedures and Flexible Manufacturing Systems. Bericht TI 3, Universität Oldenburg, 1989.

[Hun88] L. Hunter. AI Attitude and Techniques Informing CSCW. Artificial Intelligence Research, 1988.

[Kar89] D. Karagiannis. Flexible Bürosysteme (FBS) - Architektur und Einsatzmöglichkeiten. In S. Fuhrmann and T. Pietsch, editors, Praktische Anwendungen moderner Bürotechnologien, Band 12. Erich Schmitt-Verlag, 1989. in German.

[Kem88] C. Kemke. Darstellung von Aktionen in Vererbungshierarchien. In W. Höppner, editor, Künstliche Intelligenz, GWAI-88. Springer-Verlag, 1988. in German.

[KK87] A.K. Kaye and G.M. Karam. Cooperating Knowledge-Based Assistants for the Office. ACM Transactions on Office Information Systems, 5(4), 1987.

[LHWM88] F.H. Lochovsky, J.S.. Hogg, S.P. Weiser, and A.O. Mendelzon. OTM: Specifying Office Tasks. In R.B. Allen, editor, Conference on Office Information Systems, Palo Alto, California, 1988.

[Mor89] K. Morik. Sloppy Modeling. In K. Morik, editor, Knowledge Representation and Organization in Machine Learning. Springer-Verlag, 1989.

[SR86] E. Sandewall and R. Rönnquist. A Representation of Action Structures. In Proceedings of the National Conference on Artificial Intelligence (AAAI-86), 1986.

[TFGN87] D. Tsichritzis, E. Fiume, S. Gibbs, and O. Nierstrasz. KNOs: KKnowledge Acquisition, Dissemination, and Manipulation Objects. ACM Transactions on Office Information Systems, 5(1), 1987.

[TLF88] M. Tueni, J. Li, ad P. Fares. AMS: A Knowledge-based Approach to Task Representation, Organization and Coordination. In R.B. Allen, editor, Conference on Office Information Systems, Palo Alto, California, 1988.

[Wim89] K. Wimmer. An Approach to the Representation of Offices. PhD thesis, Bundeswehrhochschule München, 1989.

[WK85] G. Woetzel and Th. Kreifelts. Die Vorgangssprache CoPlan. WISDOM-Forschungsbericht FB-GMD-85-92, Gesellschaft für Mathematik und Datenverarbeitung mbH, St. Augustin, 1985. in German.

[WL87a] S.P. Weiser and F.H. Lochovsky. OZ+: An Object-oriented Database System. In F.H. Lochovsky, editor, Of-

fice and Data Base Systems Research '87. University of Toronto, 1987. Technical Report CSRI-195.

[WL87b] C.C. Woo and L.H. Lochovsky. Integrating Procedure-Automation and Problem-Solving Approaches to Supporting Office Work. In G. Bracchi and D. Tsichritzis,

editors, Office Systems: Methods and Tools. IFIP, Elsevier Science Publishers B.V. (North-Holland), 1987.

[Zis78] M.D. Zisman. Use of Production Systems for Modeling Asynchronous Concurrent Processes. In Pattern-directed Inference Systems. Academic Press Inc., 1978.
