---
otero_id: 4902
otero_key: "6Y4TGH5X"
title: "Dealing with the effects of context mismatch in group work"
authors: "Marcos R.S. Borges; Patrick Brézillon; José A. Pino; Jean-Charles Pomerol"
year: "2007"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2006.09.006"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
www.elsevier.com/locate/dss

# Dealing with the effects of context mismatch in group work

Marcos R.S. Borges <sup>a</sup>, Patrick Brézillon <sup>b</sup>, José A. Pino <sup>c,⁎</sup>, Jean-Charles Pomerol <sup>b</sup>

<sup>a</sup> PPGI, NCE and IM, Universidade Federal do Rio de Janeiro, Brazil

<sup>b</sup> LIP6, Université Pierre et Marie Curie, France

<sup>c</sup> DCC, Universidad de Chile, Chile

Available online 16 October 2006

## Abstract

The context concept can be used with advantage in the area of Computer-Supported Cooperative Work. In many studies, several forms of context have been used without explicit association to the context concept. This paper attempts to clarify the relationship between context and group work. In particular, a framework is proposed to understand context as connected to other concepts used in group work. The framework is useful to analyze some groupware systems from the context perspective and to obtain some insight on possible improvements for users. © 2006 Elsevier B.V. All rights reserved.

Keywords: Context; Groupware; Contextual knowledge; Context framework; Awareness; Computer-Supported Cooperative Work

## 1. Introduction

The context concept has been poorly understood, used and related to the main concepts of the Computer-Supported Cooperative Work (CSCW) field. The context term has been used in some publications in the area, but it is presented with various meanings [4,15], without considering its basic definition and implications. On the other hand, when one examines studies carried out in the area of context, one finds several concepts and results which could be useful in CSCW. The only application of context to group work has been, however, to the awareness concept, starting with the seminal article on awareness by Dourish and Belloti [17]. This paper attempts to partially compensate this omission.

Our goal is to describe a conceptual framework for understanding and applying the concept of context in group work. We aim to guide the designer to the systematic use of context when developing a groupware system. The use of the framework will be illustrated by presenting group work situations where the appropriate use of context could benefit the groupware usability. We also introduce the notions of context loss and context mismatch and show how we can deal with them to reduce their detrimental effects when group interaction is supported by a groupware system.

The context concept is treated by the context research community in a different way as done by CSCW researchers [4,19,26,29]. Thus, e.g., on the one hand, there is a series of interdisciplinary conferences on modeling and using context since 1997 [12]. These conferences deal with aspects of context at the highest level of knowledge and reasoning. However, this approach rarely considers practical aspects of context in real-world applications such as collaborative work. On the other hand, in CSCW articles, several issues point to context without being called as such. Moreover, few applications use the context concept to guide design decisions, leaving context to be processed mostly by the user. We believe most misunderstanding is caused by not explicitly recognizing and representing the notion of context and its association with other elements of groupware systems.

To understand context first we need to recognize its complexity. A context has infinite dimensions [7]. Context is always relative to something: the context of each member of the work group, the context of the group itself, the context of the task, the context of the organization, etc. Thus, it would be almost impossible to support all the contexts (or the resulting global context) involved in group work. We can, nevertheless, try to select the most relevant elements of context and explicitly use them.

We identify at least two major types of context in group work. There is the context which is external to the task but relevant when executing it. Roles, goals, and expected performance are elements of this external context of the task. What is important in group work is to develop a robust shared context with a strong cohesiveness. A common understanding of this external context should be attained before the beginning of the group interaction. All context differences should be identified and reduced. If discrepancies in the external/ shared context are not solved at this time, then they will probably appear during the interaction, paralyzing it until the issues are solved. We call context mismatching to these differences.

A context mismatch is easy to identify once its negative effects have already permeated the group environment. In some cases, it is too late to recover from its damaging effects and the task is lost. To deal with context mismatching we need to prevent its occurrence or to identify and tackle it at the early stages of the joint work. The later it is addressed, the more it will cost in time and effort to recover from it.

A second type of relevant context refers to the activities performed during the task. It is the context relative to the objects pertaining to the task. This context is relative to the role being performed and knowledge about it will depend on the focus on its evolution. During an interaction, a temporary loss of context may occur, resulting from personal absence or from ambiguity of some action. While the external context is normally processed outside the monitored interaction, the system should provide internal support to recover from loss of context.

Some groupware systems provide awareness mechanisms to deal with the temporary loss of context.

These mechanisms are designed to recover from loss of one or more types of task context. In particular, six dimensions have been proposed for representing the context of task activities, characterized by the descriptors: what, when, who, where, how and why [21,27]. These dimensions, however, assume task participants share the same general context, i.e., they understand and agree with an external context (e.g., roles), the task (e.g., deadlines and goals) and the organization (e.g., culture and hierarchy). This may not always be the case. For instance, which is the value of knowing that John Smith has contributed a discussion element, if one ignores whom John Smith is or the role he is playing in the task?

Despite the classification of task context types, there is no systematic method to guide the development of awareness mechanisms for groupware systems. A similar method does not exist to promote adequate context building before a group interaction either. These shortcomings are addressed in this paper and a preliminary solution is presented. Several examples illustrate the consequences generated by the lack of context and for each of them we discuss how our proposed solution would promote the appropriate context.

The paper is organized as follows. Section 2 reviews the context concept. Section 3 presents a framework for understanding how groupware issues relate to context. Section 4 presents the groupware model for awareness mechanisms. In Section 5 we show some examples where a groupware fails in dealing with these concepts and then we apply our model to propose a solution to these situations. Section 6 concludes the paper.

## 2. Context

Context may be defined as a complex description of shared knowledge about physical, social, historical, or other circumstances within which an action or event occurs [4]. In order to understand many actions or events, it is necessary to have access to relevant contextual information. Understanding the “opening a window” action, e.g., depends on whether a real window is referred to or a window on a graphical user interface [9].

For a step of a task, Brézillon and Pomerol [8] distinguish the part of the context being relevant for the current performer's focus of attention from the irrelevant part. The latter part is called external knowledge. The former part is called contextual knowledge because it has strong relation to the current focus although it is not directly considered in it. Always at a given focus, part of the contextual knowledge is proceduralized. This proceduralized context is a part of the contextual knowledge, which is invoked, organized, structured, and situated according to the focus and used while performing the task at this focus (Fig. 1).

Context evolves with focus. This dynamics of context can be observed by the movement between the contextual knowledge and the proceduralized context. Thus, a part of the context is static, e.g. the context at a step of the focus of attention is defined by a fixed number of contextual elements and a fixed proceduralized context, but the overall focus of attention is associated with a dynamic context through this movement between the contextual knowledge and the proceduralized context. Static and dynamic parts of the context are intertwined and must be considered jointly.

Brézillon and Pomerol [8] point out that it is possible to organize various types of context in a twodimensional representation: in depth first, from the more general to the more specific, and in width first as a heterogeneous set of contexts at each level. In “depth first”, contexts differ by their granularity. For example, a company context (with its tradition, habits, rules, etc.) is more general (at a higher level) than the context of an employee. In this case, context has strong relationships with the enterprise organization in terms of roles [24]. According to its depth, a context contains more general information than contexts at a lower level. However, context at one level is not a simple instantiation of the context at the upper level [6]. A context is like a system of rules (constraints) for identifying triggering events and for guiding behaviors in lower contexts. A context at one level contains contextual knowledge when the application of rules at the lower levels develops/ transforms the contextual knowledge of the upper level in proceduralized contexts that fit the goals of the tasks at hand. A context (the contextual knowledge part) is like a frame of reference for the contexts below it. For instance, a person visiting Chile knows the language spoken there is Spanish (contextual knowledge in the context of the country), and he pays attention to speak this language there, assuming he knows it (proceduralized context in his individual context).

![](/api/attachments/6Y4TGH5X/fulltext/images/b8eb395f2fa73a392facfbd673a373121033c53ff5b3007eb6d408c893af97a8.jpg)  
Fig. 1. Contextual knowledge and proceduralized context [6].

In “width first”, each actor has its own individual context. An actor's context contains information on the reasons for his actions, the results of his activities, etc. The context of the software agent possesses information on the available means for the accomplishment of the task, the access restriction to the databases, a user model, etc. For a given granularity of the context, there is thus a set of contexts rather heterogeneous, and the horizontal movement from one individual context to another one goes through either the upper context (e.g. the group context) or a lower context (e.g. the project context). This movement is done thanks to the transformation of contextual knowledge into proceduralized contexts, and, once the task executes the proceduralized contexts that become pieces of the contextual knowledge, are ready to be used later in another context and another task. Note that at the group level, a group is, recursively, like an actor with his individual context and interacting with other groups in other contexts. This is why it is important to reinforce the cohesiveness of the group context: the more the group context will be internally cohesive, the more the group will be a strong entity (unity) at the upper level (e.g. the enterprise to which the group belongs).

Brézillon and Pomerol [8] discuss the transformation of contextual knowledge into some functional knowledge or causal and consequential reasoning in order to anticipate the result of actions. Data are facts, which have not been analyzed or summarized yet (e.g., see Watson [36]); information is data processed into a meaningful form, and knowledge is explained as the ability to integrate the information in the person's body of knowledge.

The transformation of contextual knowledge in a proceduralized context assumes communication between different levels. Fig. 2 represents how the proceduralized context (PC) is built from contextual knowledge (CK, and EK representing the external knowledge) in individual contexts of two actors during their interaction about the given focus of attention. The interaction context contains the pieces of contextual knowledge inserted by each actor (i.e. from their individual contexts) in the interaction context to make them visible to other actors. The interaction context is assembled and structured jointly by all the actors during the interaction to constitute the proceduralized context needed at the given focus of attention. Thus, the proceduralized context is the result of a collaborative construction by the actors of a virtual community. Once the proceduralized context has been exploited at the current focus of attention, it becomes a piece of the actors' shared contextual knowledge. Until they reach this point, however, there exist several periods during which the context is not well understood by participants who had either a different focus of attention or a different, and sometimes conflicting, individual context. The former is called in this paper as the context mismatch, while the latter is called context loss.

![](/api/attachments/6Y4TGH5X/fulltext/images/a36b02dfa60e1117ac9cd6947e7fed94cf46c4eecd0fb469ff201c13bb27d306.jpg)  
Fig. 2. A representation of the proceduralized-context construction.

The building of a proceduralized context from the contextual knowledge sometimes does not correspond to the focus. As a consequence, there is a need to add some pieces of external knowledge in the proceduralized-context building. This situation corresponds to an incremental process of (1) acquisition of new knowledge pieces, and (2) learning of a new knowledge structure as a proceduralized context. If the addition of a piece of external knowledge in the PC corresponds to a kind of knowledge acquisition, it is nevertheless a learning process because the piece of external knowledge is not simply added to the PC, but assembled and connected to the construction already existing.

## 3. Group and team work

Group and team are general terms with frequently implicit definitions. We use them defined as follows: group is a number of individuals acting as a whole in order to get something done [1]; team is a group of persons doing a cooperative effort in the interest of a common cause [28]. CSCW deals with both groups and teams to support their work. Thus, e.g., a group having a discussion can be technology-supported as well as a team trying to build a joint project design.

Cooperation is a first dimension of joint activity by groups of people. As noted by Clement [10], cooperation may be the means to empower people. Cooperation is not necessarily linked to computer support, as illustrated by Collaborative Learning, which includes cooperative learning techniques introduced before computers were intended to support them. Nevertheless, information technology can support cooperation. In particular, effective cooperation demands that people share information, and here computer networks can be very useful. Communication is then a related dimension, much wider than just computer-based message interchanging. Communication may be defined as a process by which knowledge that resides in one or more people comes to be represented in one or more others.

A third dimension for joint activity by groups is Coordination. It may be defined as the act of working together harmoniously. However, a narrower definition may be “the act of managing interdependencies between activities performed to achieve a goal” [23]. Coordination is a necessary and important component of CSCW, since any useful contribution from a group member must be appropriately and timely related to the activities of the other members. The interdependencies mentioned in the definition refer to this relation. Closely connected to this term is the need for a group participant to know what the other team members are doing (trivial in the case of faceto-face activities, but not so in the case of distributed work): here we encounter group awareness again.

Awareness can be defined as an understanding of the activities of others, which provides a context for your own activity [17]. Note that this awareness concerns activities by people, and thus, it should not be confused with device awareness, as used in mobile devices software design. Thus, it is sometimes called group awareness. Awareness is closely related to cooperation and coordination: work on one of these dimensions typically means making incursions in the other two ones. Collazos et al. [11] have identified nine types of group awareness: organizational, task, situation, informal, social, group structural, community, multi-synchronous, and knowledge construction.

Awareness can also be analyzed according to the temporal interactions. If people are all working on a real-time basis, then they need synchronous awareness. A group, e.g., may be having a distributed meeting; synchronous awareness may provide participants with face images of the other members to perceive their reactions or know what they are doing. If people are doing non-real-time work, then they need asynchronous awareness. A person, e.g., may need to know the work other group members have done while he was off-line.

When doing joint supported work, people typically use a Shared Workspace: a construct designed to give users the feeling of being computer-mediated copresent, even in the case of actually being remotely located. Much of the shared information may be made persistent, in which case, a Group memory is built.

The 3C (Cooperation, Coordination and Communication) model proposed by Ellis et al. [18] illustrates well these dimensions and their relationships. Context, however, is not explicitly represented in this model. The only reference to context comes from the definition of awareness. On the other hand, context guides somehow all types of cooperative interactions. When an interaction model does not explicit represent context, participants have trouble in understanding and mapping the actions of others into their context [16]. Awareness mechanisms may provide part of the contextual information, but in most cases it does so without a systematic analysis where contextual information is relevant and, in some cases, essential to support group or team work [30].

## 4. Analyzing the use of context in group work

When two or more people are involved in performing a task, they require some level of common context. For example, they need to agree on a common goal, deadlines, responsibilities, etc. This common context may be called task context. Reaching this level of common understanding of the task context can be considered a coordination activity. Ideally, it should be reached before the beginning of the task or at least during its early stages. It will not change once it has been established unless a modification is required by some external event or as a result of consensus among group members. If a group cannot agree on this common context, then group members would spend precious time while clarifying the elements of the context.

Consider, for example, the preparation of a single report performed by a group of four people who attended an event. All four participants should be aware of the deadline, the target, the scope, the style, the format, the size of the text, and perhaps other contextual information. When they all agree and share the same context, the writing of the report would proceed by taking care of other issues such as the roles, the detailed contents, the actual writing, etc. On the other hand, if some contextual element is left open, e.g., the scope, then the final text may result puzzling or surprising to some group members, or there may be useless discussions while writing.

During the actual writing of the report, the lack of context may generate several understanding problems. For example, one of the participants may not understand the rationale for a new text he has not seen before; it may well be the case this was verbally agreed by the other participants while the first person was not on-line connected.

As mentioned before, however, each participant has a part of his own individual context that will not be modified by the group and the task context. It is expected that the individual and the group context would work together for the satisfaction of the individual and for the sake of the group performance. How the individual and the task contexts are mixed? They are not completely independent. Thus, the same task performed by various groups will generate different results. Also, a person assigned to a group will perform differently if he is assigned to another group, even when the task is identical.

Context has two intertwined dimensions, static and dynamic. The main dimension depends on the focus corresponding to the context: the context of an object (e.g., an action) is static, but the context of a reasoning or any intellectual process is dynamic because the focus evolves along the intellectual process. A dynamic context, in turn, may be seen along five dimensions: (1) time, (2) usage episodes, (3) social interactions, (4) internal goals, and (5) local influences [20]. Although the contextual elements in some situations are stable, understandable and predictable, there are some situations when this does not occur. Cases with apparently the same context can be different.

In order to reduce this impact, we use a conceptual framework aimed to identify and deal with common contextual elements in groupware tools [30]. The goal of the framework is to provide guidelines for research and development in groupware and context.

The conceptual framework considers the relevant elements for analysis of the use of context in groupware applications. The contextual information is clustered in five main categories: (1) people and groups, (2) scheduled tasks, (3) the relationship between people and tasks, (4) the environment where the interaction takes place and (5) tasks and activities already concluded. These clusters were borrowed from the Denver Model [31]. This model characterized groupware applications as different from single-user applications.

In synchronous environments, group members work at the same time, but in asynchronous environments, there might be a time lag between interactions. The needs differ for each type of environment, especially in connection with contextual information and the awareness required for each situation [7]. We may notice than in a synchronous situation, the shared context is progressively built by all actors. By contrast, in an asynchronous case, an actor wishing to intervene needs first to recall (or rebuild) the shared context before submitting a contribution, and the shared context that is recalled may not be the same shared context of another participant. In this latter case, the interaction context is not totally shared.

The framework is a generic classification of contextual elements. It does not cover the peculiarities of a certain domain. It does not apply to a specific type of groupware either. This generic framework may be a starting point for a classification of contextual elements for particular domains, where new contextual elements may be considered relevant.

The various types of contextual information will be grouped by the framework into the five categories. As mentioned before, the size of the contextual dimension is infinite [8]. Thus, the framework just considers contextual elements most relevant to task oriented groups, i.e., contextual knowledge and proceduralized context [7].

The first category is the information about group members. It concerns information about the individuals and their groups. There is evidence that knowledge about the group composition and its characteristics is important for the understanding of the potential ways the project or task will be developed. Also, knowledge about the characteristics of individuals and the group as a whole encourages interaction and cooperation [7].

The first category is further divided into two types of context. The individual context carries information about each individual member of the group. It includes information about his abilities, interests, location, previous experience, personal data and working hours. The group context carries information about the team characteristics. The data is similar to the aforementioned, but related to the group. It includes team composition, members' abilities and previous experience as a group, and the organizational structure.

The second category refers to information about scheduled tasks. Group members need to be acquainted with task characteristics independently of how the interaction occurs. Task context is the name given to this context. Its goal is to identify tasks through their relevant characteristics. These characteristics include task name, its description and goals, deadline, estimated effort, technology to be used, and other requirements and pre-conditions.

The third category concerns the relationship between the group members and the scheduled tasks. Its goal is to relate each group member's action and the interaction he is involved in. This interaction begins with an execution plan and terminates when the task has been concluded, passing through a sequence of actions required for carrying out the plan. If the interaction is interrupted before the task is concluded, then the reasons for the premature ending are also part of the context and they are relevant to understand the interruption rationale. This category is further divided into two types of contexts: the interaction context and the planning one. The interaction context consists of information representing the actions, which took place during the task completion. When interaction is synchronous, it is worth to be aware of details of the activity at the time it occurs, while in asynchronous interactions it matters to provide an overview of activities.

The planning context consists of information about the project execution plan. This information may be generated at two different points in time. In the case of ad-hoc tasks, they appear as a result of the group interaction, which decides about it. For the scheduled tasks, they are generated at planning time, i.e., when the tasks are defined and the roles are associated to them. The planning context may include rules, goals, deadline strategies, and coordination activities. It is also dynamic and therefore, it can change in time. Consequently, the planning itself may be revised dynamically (reactive planning, opportunistic planning, etc.).

The fourth category groups information about the environment. It represents the aspects of the environment where the interaction takes place. It covers both the organizational issues and the technological environment, i.e., all information outside the project but within the organization that can affect the way the tasks are done. The environment gives some additional hints to group members about how the interaction will occur [22]. For example, the quality control patterns are part of this context. Strategy rules, policies, financial restrictions and institutional deadlines are other examples of this context.

The last category gathers all information about concluded tasks. Its goal is to provide background information about the experiences learned either from working within the same group or from similar tasks performed by other groups. It should include all contextual information about previous projects. The framework calls “historical context” to this set of information. This information is important for assimilating errors and successful approaches from previous projects. It can also be used out of the context of a project to provide insight into working practices and team cooperation. A summary of the framework is presented in Table 1.

## 5. Context and awareness in groupware

When people are working as a group, context becomes especially relevant. Not only individual contexts need to be proceduralized, but also the group context. As described in the framework, group context is not simply the union or intersection of individual contexts. For instance, a specific person may work differently with a certain group of colleagues than with another one.

Table 1  
Conceptual framework for context analysis in groupware

<table><tr><td>Information type</td><td>Associated contexts</td><td>Goals</td><td colspan="2">Examples of contextual elements</td></tr><tr><td rowspan="2">Group members</td><td>Individual</td><td>To identify the participants through the representation of their personal data and profiles.</td><td>NameQualifications</td><td>ExperienceWorking hours</td></tr><tr><td>Group</td><td>To identify the group through the representation of its characteristics</td><td>InterestsNameMembersRolesAbilities</td><td>Web pageExperience as a groupOrganizational structure</td></tr><tr><td>Scheduled tasks</td><td>Task</td><td>To identify the tasks through the representation of their characteristics.</td><td>NameDescriptionGoalsDeadlines</td><td>Estimated effortActivitiesRestrictionsWorkflow</td></tr><tr><td rowspan="3">Relationship between people and tasks</td><td>Synchronous interactions</td><td>To represent the activities performed during the task completion while connected.</td><td>Member/group in-chargeMessages exchangedPresence awareness</td><td>Gesture awarenessOn-going activitiesAuthorDescriptionJustification</td></tr><tr><td>Asynchronous interaction</td><td>To represent the activities performed during the task completion to people who were not present</td><td>Member/group in-chargeArtifacts generated versions</td><td>Activities completedAuthorGoalReport</td></tr><tr><td>Planning</td><td>To represent the execution plan of the task to be performed</td><td>Interaction rolesRulesAimResponsibilities</td><td>StrategiesCoordination proceduresWorking plan</td></tr><tr><td>Organizational settings</td><td>Environment</td><td>To represent the environment where the interaction occurs; i.e., characteristics that influence task execution.</td><td>Quality patternsRulesPoliciesDeadlines</td><td>Organizational structureConstraintsProceduresStrategies</td></tr></table>

Adapted from Rosa et al. [30].

How is missing context provided to team members who cannot map their current context with the task's context? Fig. 3 shows our proposed model. It is basically a context processing procedure. People individually create knowledge, part of which is communicated to the rest of the group as well as being presented in a UI and eventually stored. The generation step consists of a person contributing information to the group. Of course, this information may be contents for the group output or related information, such as questions, suggestions, or proposals. Part of this information is stored, according to previous conditions, e.g., “all contents must be stored”. It should be noted that some information may not be easily communicated [35], due to a variety of reasons (the socalled “sticky” information).

The capture step consists of procedures to gather some physical data from the generation step. For instance, in the case of joint text editing, the movement of the user's mouse may provide indication on which part of the document the user works. In another example, a camera may capture the physical movements of a person; this contextual information may be important for another user who may be wondering why the first person is not answering her questions.

The awareness step consists of the processing of contextual information to provide it to the other participants. Note that it has several inputs. The first is information from the generation step. An example would be a contribution just written by a group member. This information needs to be transformed in some way, perhaps summarized or filtered to make it available to other people. In fact, it takes into account the processing specifications given by individual users. Another type of input is from the capture step; again, this information will probably be processed to avoid information overload. It also receives information from the storage step. This occurs, e.g., when an agent decides to distribute a summary report on recent work in asynchronous systems. Finally, notice there is group context received as input. This is needed as important information to process the rest of the inputs.

![](/api/attachments/6Y4TGH5X/fulltext/images/88c9e5ea1d7ca87ad3189bccf1c744c1b2602fdb8305143d0b30a68063ba4e9c.jpg)  
Fig. 3. Context knowledge processing in group work.

The visualization step incorporates the system user interface. It provides a physical representation of knowledge – icons, text, figures, etc. – to participants. Input to this step can come from the generation procedure: the physical feedback a user receives when she contributes to the group.

Capture, storage, awareness and visualization are all processing steps done by the system on the basis of the user's specifications and pre-established rules. Besides generation, there is another human processing step: the interpretation process. A person performs this step when, considering the visualized information and her individual context, she assimilates the presented information into knowledge. This is needed by the person to generate new contributions, thus closing the cycle of processing context to do participatory work within a group. A person may need some information from the storage, requesting it; this petition may be as simple as a mouse click over a button on the UI or a complex query specification.

## 6. Context and awareness in four case studies

We illustrate our view of context awareness with four examples taken from the groupware area: SisPro [2] is a computer environment for project design; SISCO [3] is a meeting preparation asynchronous system aimed at supporting the group discussion that occurs before an actual decision meeting; CO2DE [25], a cooperative editor supporting multiple versions as a way to deal with conflicting views when building a diagram; and a workflow and discussion system intended to improve communication within a company [5]. These systems do not support context explicitly, although they use several contextual elements to support group work. The goal of this section is to analyze how context, at its several levels, may be represented and used in these systems. In particular, how the framework can be used.

Notice that making context explicit is a way to remember, not only the way in which a solution was developed, but also the alternatives at the time of solution building, existing constraints, etc. Thus, awareness is achieved by comparing context at that time and the current context.

If the goal is the realization of the solution, it is also important to account for individual contexts. A specialist can propose a solution from her field of domain. Yet, another specialist may give constraints. In such a case, the first specialist should modify her context to include the fact the pair (problem, solution) in her domain must be changed to the triple (problem, context, solution).

By working together, each person will increasingly share more experience with others. Thus, their individual contexts will have a non-empty intersection making their interaction short and efficient. We should notice these examples assume a positive/collaborative attitude from group members. A non-cooperative environment may generate many negative attitudes, such as personality clashes and concealment of information. Although in some cases these attitudes are caused by a lack of a common context, we think that our approach does not apply to non-cooperative environments.

## 6.1. The SisPro project

The objective of this system is to ease collaborative activities (including negotiation) and learning processes, and the development of teamwork competence [2]. Fig. 4 presents the general architecture.

For supporting exchanges among participants, the SisPro environment proposes different workspaces that we assimilate to contexts. A first type of virtualworkspace is attached to each participant (individual context). These individual contexts allow participants to manage their own information, choosing the part of it which is to be communicated to other participants. A second type of workspace is attached to each project (project context) and is shared by all participants in the project. This workspace is the medium for the negotiation among participants. The project context represents the project state that results from the consensus among the various participants at each moment. In contextual terms, participants draw from their individual context contextual-knowledge elements to negotiate with others in order to build a shared proceduralized context in the project context. This case study points out the movement between the different levels of context shown in Fig. 1.

Each individual context benefits, on the one hand, from external specialist's sources of reference of the team member and, on the other hand, from the team context. The team project has a more general context than the individual contexts that explains why the members met in this project (such as an European project) where partial solutions are negotiated and are new knowledge for the specialist (as a proceduralized context at a previous step of the design). However, the individual contexts are relatively static with respect to the team project that possesses the dynamics required for the progress of the design.

## 6.2. The SISCO example

There have been several interpretations of premeeting activities. Most authors see the pre-meeting as a planning activity, during which agenda items, logistics, schedule and pre-work are carried out [33]. We believe that preparation can encompass further activities. SISCO is a decision meeting preparation support system [3]. One of the goals of SISCO is to prepare participants, increasing their knowledge about the agenda items, before the actual meeting.

![](/api/attachments/6Y4TGH5X/fulltext/images/75953897260caecdcfd26ba4eec1d96f1660ea00b61713de0703375ee7f30e01.jpg)  
Fig. 4. The SISPRO Architecture with the project context and the individual contexts.

Context mismatching is a very common event in general meetings. In such meetings, the required common context is not related to the participants' daily activities, such as a project or a routine process they are involved. Their views about general issues are usually mapped into their individual context, missing it at a general level. Daft and Lengel [14] classified this situation as a high level of equivocality, which can be interpreted as another name for context mismatching. The common context is essential to the success of a meeting and its subsequent activities.

When context mismatching occurs during a meeting, it is hard to progress before a common context is agreed and understanding is restored. This process wastes time and causes distress to all participants, not only those involved in the discrepancy. In SISCO, we use the premeeting phase as an opportunity to identify and reduce context mismatch about the issues surrounding the agenda items. The agenda items are previously presented to participants and they have the opportunity to exchange their views and access other people's views. The common context can then be achieved during the meeting preparation. Hopefully, participants will go to the face-to-face meeting with a low level of equivocality, making better use of their time and enhancing the decision process that will occur during the meeting.

The accomplishment of a common context should not be confused with groupthink, an undesired effect on decision meetings [34]. Groupthink occurs when uncertainty is left aside artificially due to a dominating opinion about the decision. The search for a common context does not have a negative effect on the uncertainty. On the contrary, when common context is achieved, i.e., equivocality is reduced, meeting participants can concentrate on their difference of opinions, i.e., on the uncertainty about the issues under discussion.

SISCO provides the coordinator with a tool for identifying levels of participation and contribution during the pre-meeting. The type of contribution usually shows how to contextualize the contributor's work. Sometimes, however, a context mismatching hides behind a nonparticipative attitude. If the coordinator identifies a high level of context mismatching he can act accordingly. For example, he can try to seek clarification from the person who included the agenda item. As an ultimate act, the coordinator can postpone the meeting until a desirable level of common context has been achieved.

The asynchronous interaction, however, may generate a temporary loss of context to participants who have been away from the discussion. Perhaps no one has a complete knowledge of the contributions. After absence from an intensive interaction, a participant may lose context and may not be able to combine the current contributions with her past understanding of the discussion. Thus, the system has to make contributions persistent and provide awareness mechanisms to allow users to update their individual contexts with the discussion context represented by the set of contributions. Whenever a participant logs in, the system generates a schematic view of the discussion contents, indicating what is new to her. This keeps the contextual knowledge uniform among group members even when they stay disconnected from the system during long periods.

The meeting context covers as much as possible the wide range of options and arguments related to the agenda items. During the discussion supported by SISCO using an IBIS<sup>1</sup>-like argumentation model, most contributions are based on the participants' individual context, thus the authorship provides some hints about the associated context. SISCO also encourages participants to express not their own views, but those which are logically consistent with the meeting context. In this way the system intends to disassociate opinions from individual contexts and move them towards the meeting context. A way of achieving it is by removing authorship from the contributions, but anonymity introduces other types of problems, such as free riding [13]. The trade-off between anonymity and full authors' identification is still an open issue.

Another form of supporting meeting context is through the definition of roles. When playing a role in SISCO, an individual is given a narrower context with specific awareness mechanisms. For example, the coordinator role is provided with a participameter, a widget informing the level of participation in the discussion [3]. The participameter is considered a kind of group or task context and provides the coordinator with elements to decide on what to do when, for example, the level of participation in a certain item is low: remind people, promote discussion or even drop the topic. Fig. 5 illustrates the user interface of the participameter.

## 6.3. The CO2DE example

The CO2DE editor [25] allows for individual contexts to be joined into a single diagram by providing a synchronous cooperative edition facility and a WYSI-WIS (What You See is What I See) interface (Fig. 6). Although it also allows asynchronous interaction, it does not focus on it. The diagram works as the persistency of the latest group context, in this case the union of individual contexts. However, the notion of context is not explicitly treated in CO2DE.

![](/api/attachments/6Y4TGH5X/fulltext/images/811fcbb5e04d2b5c232e1e2cb5439eed7c7858e28157a53be225c55252da95ee.jpg)  
Fig. 5. The participameter as an awareness widget.

When conflicting views arise on a diagram, most cooperative editors support users to reach a consensus by means of a communication mechanism, e.g., a chat. CO2DE deals with conflicts in a different way. It allows several versions of the diagram to co-exist. It organizes the versions into a tree to associate each version to its origin, its alternative versions resulting from the conflict and its further decomposition originated from another conflict. In none of these cases, however, the system represents contextual information, e.g., the conflict and the assumptions for a version. This information is kept within each individual context and is not stored. If a person wants to understand the rationale behind the creation of a new version, he has to ask its creator.

During the elaboration of the diagram, several versions may co-exist. It is left to participants to solve the conflicts and express the resulting consensus in a single version. The CO2DE approach has the advantage of allowing users to represent their views in a more comprehensive format, since a single conflict in many cases involves several elements of the diagram. It is like discussing two or more options using the complete picture, instead of discussing element by element. Another advantage is the representation of the work evolution by means of a set of step-refined versions. The approach also supports a mental comparison of two alternatives. With a simple click of the mouse one can rapidly perceive the differences between diagrams.

The previously presented framework helps to visualize a possible improvement to CO2DE. When many versions of a diagram are present, it is desirable to have the rationale of each version stored with it, since even its creator may forget it. This context is not awareness information. The system should be extended to handle these explanations and allow the user to retrieve them by clicking over a certain button in the version representation. This is equivalent to “requesting additional information” arrow from “Interpretation” to “Storage” in Fig. 3.

## 6.4. The gap between decisions and their implementations

Much research has been done on improving the decision making process but little attention has been paid to the implementation phase following a decision.

![](/api/attachments/6Y4TGH5X/fulltext/images/7fd9e66e7188d3d4907c205060a992196446e55af8dec630fefeecf7e7c029e9.jpg)  
Fig. 6. CO2DE user interface [25].

Although many authors propose that these two phases should not be seen as separate processes [32], many organizations continue dealing with them as loosely coupled activities. As a result, many decisions are not implemented or the implementation does not conform to the essence of the decision. The gap between the end of a decision making process and its implementation activities may, in fact, turn the decision inconsequent, due to difference of contexts between decision makers and those who will implement the decision [5]. Often, the context close to decision makers is at the strategic level, while the context at the operational level guides the actions of decision implementers. Decisions that are implemented without reducing the context mismatch may generate outcomes, which are different from those planned at the time of the decision. The same is true for decisions made without the appropriate context at the operational level.

The context mismatch causes the gap. To reduce this gap, a common context should be sought for the environment to be affected by the decision. Communication and common forms of interaction are the key factors to reduce the context mismatch

Borges et al. [5] provide a case in which insufficient common project context causes the mentioned mismatch. Its origin is a request for purchases originated in a certain

Department; after being approved by the Company Board, the Purchasing Department does the acquisition. Unfortunately, the results are not the ones expected by the request originators. In fact, several other analyzed outcomes are also unsatisfactory. Even with good will from all actors, the problem has no solution if there are no means for communication and discussion of an acceptable option to choose. The tools proposed by Borges et al. to support the reduction of context mismatch and the finding of a solution are workflow and discussion supporting tools. They claim that a workflow representation should be able to expose the differences between what is expected and what is possible to implement from a decision.

## 7. Discussion and conclusions

Work on context and CSCW has largely been done independently. Perhaps this has not been a good idea for groupware designers, who might benefit from research in context. The framework may be a first step to narrow the gap by relating the concepts of context and groupware. The model representing how awareness mechanism can carry the contextual information illustrates how the notion of context is related to other widely used terms in CSCW, such as user interfaces, automatic capture and storage.

The context process model presents group work as a knowledge-processing job with some activities possible to do by machine as support to the human tasks. This dataflow-type modeling is novel, as well as the presentation of context as knowledge flowing among processing activities.

The framework and the model can be applied together to obtain some insight into some groupware designs. In particular, by considering context as knowledge to be applied during group work, one can have a wider perspective than just focusing on the information provided to users by awareness mechanisms, as shown in the previous section. Other groupware designs would probably be suitable for analysis from this viewpoint.

Making context explicit is a way to remember, not only the way in which a solution was developed, but also the existing alternatives at the time of the solution building, the existing constraints, etc. Thus, by comparing the context at that time and the current context allows awareness.

A historical context may also be useful. It consists of information about projects and tasks already completed. This information is important for the understanding of errors and successful approaches in previous projects to be used in current tasks. It can also be used out of the context of a project to provide insight into working practices and team cooperation. When we make the historical context available, users can access the real reasons on which a decision was made, for example.

During the progress of building a solution, one observes that the project context evolves jointly to the solution building, and even individual contexts of the participants are modified. Once all participants agree on a proceduralized context, this later becomes a piece of the solution construction, and each participant retains it in his individual context as a piece of the shared part of all individual contexts. For example, a specialist on a certain subject can propose a solution from his competence field. However, another specialist may introduce constraints which are clear from his own domain but not in the other field. In such a case, the first specialist should modify her context to take into account the fact that the pair (problem, solution) in her domain must be modified becoming the triple (problem, context, solution).

In a collaborative work, participants share experience with others. As a consequence, participants see their individual contexts enriched with contextual knowledge that will be shared with other individuals and found also in their individual contexts. This will lead later to more efficient interaction among them. For example, if a group must meet regularly in the framework of a project, they will spend the first meeting to establish the frequency of the following meetings, the day of the week, the time, the location, etc. Once all participants have agreed (eventually after negotiation), all these pieces of contextual information will be shared, structured, and assembled together in a coherent whole (the proceduralized context), and they will finish the first meeting by saying only “see you next time” that will be a shared pointer towards a chunk of knowledge containing the date, the location, etc. of the next meeting.

## Acknowledgments

This work was supported by grants from: CNPq (Brazil) 305900/2005-6 and Fondecyt (Chile) No. 1040952.

## References

[1] T.K. Bikson, J.D. Eveland, The interplay of work group structures and computer support, in: J. Galegher, R. Kraut, C. Egido (Eds.), Intellectual Teamwork, Lawrence Erlbaum Associ ates, Hillsdale, NJ, 1990, pp. 245–290.

[2] M. Borges, R. Naveiro, R. Souza Fillho, SISPRO — a computer support system for conceptual design in architecture, Proceedings of the 12th International Conference in Engineering Design, Heurista, Munich, 1999.

[3] M.R.S. Borges, J.A. Pino, D. Fuller, A. Salgado, Key issues in the design of an asynchronous system to support meeting preparation, Decision Support Systems 27 (3) (1999) 271–289.

[4] M.R.S. Borges, P. Brézillon, J.A. Pino, J.C. Pomerol, Groupware system design and the context concept, Lecture Notes in Computer Science 3168 (2005) 45–54.

[5] M.R.S. Borges, J.A. Pino, R.M. Araujo, Common context for decisions and their implementations, Group Decision and Negotiation 15 (3) (2006) 221–242.

[6] P. Brézillon, Context in problem solving: a survey, The Knowledge Engineering Review 14 (1) (1999) 1–34.

[7] P. Brézillon, Individual and team contexts in a design process, Proceedings of the 36th Hawaii International Conference on Systems Sciences, HICSS-36, Track Collaboration Systems and Technology, R.H. Sprague (Ed.), Los Alamitos: IEEE, CD-Rom, 2003.

[8] P. Brézillon, J.-Ch. Pomerol, Contextual knowledge sharing and cooperation in intelligent assistant systems, Le Travail Humain 62 (3) (1999) 223–246.

[9] P. Brézillon, F. Adam, J.-Ch. Pomerol, Supporting complex decision making processes in organizations with collaborative applications — a case study, Lecture Notes in Computer Science 2806 (2003) 261–276.

[10] A. Clement, Cooperative support for computer work: a social perspective on the empowering of end users, Proceedings of CSCW'90, ACM, Los Angeles, CA, 1990, pp. 223–236.

[11] C. Collazos, L.A. Guerrero, J.A. Pino, Knowledge construction awareness, Journal of Student Centered Learning 1 (2) (2003) 77–86.

[12] Context 2005, Modeling and Using Context, Proceedings of the 5th International and Interdisciplinary Conference, Paris, France, Lecture Notes in Artificial Intelligence, vol. 3554, 2005.

[13] W.H. Cooper, R.B. Gallupe, S. Pollard, J. Cadsby, Some liberating effects of anonymous electronic brainstorming, Small Group Research 29 (2) (1998) 147–178.

[14] R.L. Daft, R.H. Lengel, Organizational information requirements, media richness and structural design, Management Science 5 (May 1986) 554–571.

[15] A.K. Dey, D. Salber, G.D. Abowd, A conceptual framework and a toolkit for supporting the rapid prototyping of context-aware applications, Human-Computer Interaction 16 (2–4) (2001) 97–166.

[16] P. Dourish, Seeking a foundation for context-aware computing, Human-Computer Interaction 16 (2–4) (2001).

[17] P. Dourish, V. Bellotti, Awareness and coordination in shared workspaces, Proceedings of CSCW'92, ACM, Toronto, Canada, 1992, pp. 107–114.

[18] C.A. Ellis, S.J. Gibbs, G.L. Rein, Groupware — some issues and experiences, Communications of the ACM 34 (11) (1991) 38–58.

[19] A.J. Gonzalez, R. Ahlers, Context-based representation of intelligent behavior in training simulations, Transactions of the Society for Computer Simulation International 15 (4) (1999) 153–166.

[20] S. Greenberg, Context as a dynamic construct, Human-Computer Interaction 16 (2–4) (2001) 257–268.

[21] C. Gutwin, S. Greenberg, A descriptive framework of workspace awareness for real-time groupware, Proceedings of the ACM Conference on Computer Supported Cooperative Work, 2002, Access: April, 2002. Available at: http://www.cpsc.ucalgary.ca/ grouplab/papers/.

[22] S. Hudson, I. Smith, Techniques for addressing fundamental privacy and disruption tradeoffs in awareness support systems, Proceedings of the ACM Conference on Computer-Supported Cooperative Work (CSCW 96), ACM Press, New York, 1996, pp. 248–257.

[23] T. Malone, K. Crowston, The interdisciplinary study of coordination, ACM Computing Surveys 26 (1) (1994) 87–119.

[24] J. McCarthy, Notes on formalizing context, Proceedings of the 13th IJCAI, vol. 1, 1993, pp. 555–560.

[25] A. Meire, M. Borges, R. Araujo, Supporting multiple viewpoints in collaborative graphical editing, Journal of Multimedia Tools and Applications, 2006 (to appear).

[26] T.P. Moran, P. Dourish, Context-aware computing, Human-Computer Interaction 16 (2–4) (2001) 87–94.

[27] M.K. Pinheiro, J.V. Lima, M.R.S. Borges, A framework for awareness support in groupware systems, Computers in Industry 52 (1) (2003) 47–57.

[28] Random House Webster's Concise College Dictionary, Random House, New York, 1999.

[29] M. Rittenbruch, ATMOSPHERE: a framework for contextual awareness, International Journal of Human-Computer Interaction 14 (2) (2002) 159–180.

[30] M.G.P. Rosa, M.R.S. Borges, F.M. Santoro, A conceptual framework for analyzing the use of context in groupware, Lecture Notes in Computer Science 2806 (2003) 300–313.

[31] T. Salvador, J. Scholtz, J. Larson, The Denver Model for groupware design, SIGCHI Bulletin 28 (1) (1996).

[32] R.H. Sprague, A framework for the development of decision support systems, MIS Quarterly 4 (4) (1980) 1–26.

[33] J. Szerdy, M.R. McCall, How to facilitate distributed meetings using SEM tools, in: David Coleman (Ed.), Groupware: Collaborative Strategies for Corporate LANs and Intranets, Prentice Hall, New Jersey, 1997, pp. 207–230.

[34] M.E. Turner, A.R. Pratkanis, Twenty-five years of groupthink theory and research: lessons from the evaluation of a theory,

Organizational Behavior and Human Decision Processes 73 (2– 3) (1998) 105–115.

[35] E. Von Hippel, Sticky information and the locus of problem solving: implications for innovation, Management Science 40 (4) (1994) 429–439.

[36] R.T. Watson, Data management, Databases and Organizations, Second edition, John Wiley and Sons Inc., New York, 1998.

![](/api/attachments/6Y4TGH5X/fulltext/images/0460cef4e4f8e137a61d9ba263c9ae065f3ff9f62723f74868789c3839c030be.jpg)

Marcos R. S. Borges is Associate Professor in the Computer Science Department and a senior researcher at the NCE, both at the Federal University of Rio de Janeiro, Brazil. He earned his doctorate in Computer Science from the University of East Anglia, UK in 1986. From 1994 to 1996, he was a visiting research scholar and a member of the Object Technology Laboratory at Santa Clara University, California, USA. Borges has also served as Visiting Professor at the Polytechnic University of

Valencia, Spain (2004–2005). He has published over a hundred research papers in international conferences and journals, including Decision Support Systems, Computers in Industry, and the European Journal of Operational Research. His research interests include CSCW, Decision Support Systems and Organizational Computing.

![](/api/attachments/6Y4TGH5X/fulltext/images/8acbd4e5bb09fa74242c5b07688707945b3902fdb6cfe8481bb643b6edae28f3.jpg)

Dr. Patrick Brezillon defended his Thèse d'Etat in 1983 on “Mathematical Modeling of Self-Oscillating Nonlinear Systems. Application in Biology to Serotonin and Calcium Metabolisms.” He belongs now to the SYSDEF team since the creation of the Laboratoire d'Informatique de Paris 6. Since 1992, the research of Dr. Brezillon has been focusing on the notion of context, and he is now acknowledged as one of the main leaders in the community interested by context by participat-

ing in the organization of the series of international and interdisciplinary conference on context (CONTEXT), initiating the French Association for Context. His ideas on context are now formalized in a context-based formalism–called Contextual Graphs–for representing in a uniform way elements of reasoning and of contexts. This formalism is used in 15 different domains concerned by decision making. He published about 290 papers in international conference and international journals (e.g., IEEE Expert, AI Magazine, The Knowledge Engineering Review, the International Journal on Human-Computer Studies).

![](/api/attachments/6Y4TGH5X/fulltext/images/e8c7ca3ee42398cbc660424651d40d7469d2eed768d09037ceb2999950159f3c.jpg)

Jose A. Pino is an Associate Professor of Computer Science and Director of the Ph.D. program in Computer Science at the Universidad de Chile. His research interests include Computer-Supported Cooperative Work, Human-Computer Interaction and Software Industry Studies. He has served as President of the Chilean Computer Science Society (SCCC) and President of CLEI (the Latin American Association of Universities concerning Information Technology). He has

co-authored six books and published research papers in international conferences and journals, including Journal of the ACM, Communications of the ACM, Decision Support Systems, Interacting with Computers and Information Technology and People.

![](/api/attachments/6Y4TGH5X/fulltext/images/ee9e9b3e9798643654da6d30265b5e3e1bf94222f7cb8e29b6f8b78cb4162af4.jpg)

J.-Ch. Pomerol got his Ph.D. in Computer Science (optimization) in 1980. He is professor of Computer Science and Rector of the Pierre et Marie Curie University (UPMC) in Paris (France). For six years he headed the lab of Artificial Intelligence (AI) of UPMC. He was also with the French National Center for Scientific Research (CNRS) as a project manager for information science and technology from 1995 to 2000. The first part of J.-Ch. Pomerol's career was devoted to game theory

and convex analysis. By the eighties, J.-Ch. Pomerol turned to AI, Computer Aided Decision and ‘intelligent’ decision support systems. This activity resulted into two books on Expert Systems and Decision Support Systems. Meanwhile J.-Ch. Pomerol developed many concepts merging the ideas of Multi-criteria Decision making (MCDM) and Artificial Intelligence to improve the interactivity of multi-criteria methods. With Barba-Romero he wrote a book on “Multicriterion Decision Making for Management” translated to Spanish and French. Now J.-Ch. Pomerol is still working on MCDM but also on the pragmatics of the decision, and on the representation of contextual information in decision, aiming at incorporating contextual information in DMSS.
