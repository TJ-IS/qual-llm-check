---
otero_id: 1580
otero_key: "FA8K6YC8"
title: "Frame-based argumentation for group decision task generation and identification"
authors: "Pengzhu Zhang; Jingle Sun; Hsinchun Chen"
year: "2005"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2004.03.006"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Frame-based argumentation for group decision task generation and identification

Pengzhu Zhang<sup>a,</sup>\*, Jingle Sun<sup>b</sup>, Hsinchun Chen<sup>c</sup>

<sup>a</sup>Antai Management School, Shanghai Jiaotong University, Shanghai 200052, China <sup>b</sup>Management School, Xi’an Jiaotong University, Xi’an 710049, China <sup>c</sup> Department of MIS, University of Arizona, Tucson, AZ 85721, USA

Available online 10 May 2004

## Abstract

One of the most important stages of group decision-making is the generation and identification of decision tasks. In this paper, we define a decision task with five elements: decision makers, decision executors, decision objectives, decision problems and decision constrains. Based on this distinction, we present a conceptual model for generation and identification of group decision tasks in an organization. In addition, we describe a prototype of a group argumentation support system (GASS) that applies frame-based information structure in electronic brainstorming (EBS) and argumentation to support group decision task generation and identification. Using four group performance indicators, the prototype was evaluated in a lab experiment to determine its effectiveness and efficiency. <sup>D</sup> 2004 Elsevier B.V. All rights reserved.

Keywords: Decision task; Group support system; Argumentation

## 1. Introduction

One of the most important stages in group decision-making is the generation and identification of decision tasks [29]. According to Hart’s ‘‘think tank’’ metaphor, effective group decision-making calls for careful definition of the decision task [35], which is also emphasized in DeTombe’s COMPRAM method for handing complex societal problems [5] in which members of a decision-making group may experience three sub-phases: becoming aware of the problem and forming a (vague) mental idea of action; extending the mental idea of the action, putting the action on the task agenda, and deciding to handle the task. However, defining a decision task in an organization is difficult to achieve a number of desired outcomes, including overcoming conflicting interdependence among outcomes and uncertainty [2].

Group decision support systems or group support systems (GDSS/GSS) are useful for supporting task analysis and coordination among group members [24]. Incorporating critique and argumentation in GDSS makes it possible to improve the performance of decision groups [28,37,38]. However, most group support systems deliver support for group members only to define information exchange and communication decision tasks [3,8,11,24,23,30]. These systems store each group member’s idea information and comments in an unstructured manner in a pool for group members share.

As Hilmer and Dennis [9] have shown in their experimental research, individuals in groups have to categorize information, in order to encourage group members to better pay attention to new information received from others and to integrate it into their own individual decision-making processes. A structured group memory storing group argumentation information could productively support group decision-making.

The aim of this paper is to address the generation and identification of group decision tasks based on structured group argumentation information, which we call ‘‘frame-based argumentation’’ (FBA).

In the remainder of the paper, we define a decision task in a way that distinguishes it from other decisionmaking related concepts. We then present a conceptual model for generation and identification of group decision tasks, implement that model and evaluate it by using a prototype of our group argumentation support system (FBA-GASS). The paper proceeds as follows. In the next section, we review the related literatures. Section 3 defines a decision task, its characteristics and components. Section 4 describes a conceptual model for generation and identification of group decision tasks, an FBA-GASS prototype and the implemented decision task generation –argumentation procedures. Section 5 illustrates an application example. Section 6 lists the evaluation results based on a laboratory experiment. In the final section, we summarize our work and contributions to GDSS/GSS and then offer suggestions for future research.

## 2. Literature review

The study of tasks has a long history, both in the organizational literature and from a group process perspective [19]. Many scholars of group behavior have argued that the nature of their task plays an important role in a group’s interaction process and performance [25,31]. The importance of decision tasks in a GDSS/GSS has drawn much attention from many scholars [4,25].

In GSS research, a task classification scheme has been widely used to distinguish among tasks in various ways [19,39]. Perspectives are said to belong to one of four conceptualizations ranging from: (1) task as behavior description, (2) task as ability requirements, (3) task qua task, and (4) task as behavior requirements [39]. This paper is not intended to encompass all kinds of tasks but to focus on (4) task as behavior requirements that are typically encountered in organizational decision-making groups.

It is well recognized that the nature of a task plays an important role in a group’s interaction process and performance under the support of GDSS/GSS [39]. But what is a decision task? What are the features of a decision task? Where does a decision task in a GDSS/ GSS come from? How does one differentiate between a decision task and claims or ideas proposed by group members? And how is it possible to support group members in generating and identifying a decision task? These questions have not been adequately studied in the previous implemented group argumentation support systems [12].

As is well known, the research on group argumentation support is an outgrowth of fundamental work on GDSS/GSS [1,10,14,13,15,26,30,32– 34]. The term ‘‘argumentation’’ refers to the act of making claims, backing them up with supporting evidence or reasoning, and criticizing or challenging those reasons [1,30]. The three core factors for argumentation were pointed out by Toulmin early in 1958: (1) claim, a claim that is used to express a position or assumption; (2) data, data that support the claim; and (3) warrant, a warrant that justifies the logical relation between the claim and its supporting data [36].

Bui and Bodart [1] separated detailed argumentation factors from the actions/resources in a structural language. The nine core factors are: (1) viewer, who gives a speech in a group; (2) object ,an object used to describe the action; (3) action, the accomplishment necessary for solving a defined problem; (4) resource, which may be input or output in an action; (5) intonation, used to indicate the real meaning of a speech, such as sentiment, position, belief, conviction or persuasion; (6) position, support, oppose, don’t care; (7) justification, free-format-argumentation based on goals, constraints, facts or assumptions; (8) proposed move, indicating the shift of a view, such as drop, implement, modify or other; and (9) time stamp, a time stamp that covers all activities that occur between the start and the end of the process. Although the authors proposed ARBAS as a structuring language that incorporates an argumentation scheme to present ideas that would be likely to stimulate focused discussion among the decision makers, they did not develop a GSS to illustrate the language.

On the other hand, Mitroff, Mason and Barabba and Locks [17,22,36] formalized Toulmin’s argumentation structure of logic for ill-structured decision problems. Recently, based on Barabba’s work, Ramesh and Whinston [27] presented a formal argumentation logic in a circuit graph in 1994, upon which Raghu et al. [26] developed a connectionist paradigm with a defeasible logic graph. Sillince and Saeedi [33,34] also presented many examples of computational models of argumentation. However, logic representation, although powerful and elegant, is only partially suited for representing real arguments as suggested by Sillince and Saeedi [34]. Logic-based argumentation is of not useful in many GDSS/GSS practices.

As Hua and Kimbrough [10] presented their logical apparatus based on the informal Issue-based Information System (IBIS) model of argumentation, Gordon and Karacapilidis [7] used issues, alternatives, positions, and constraints representing preference relations as argumentation elements in their implemented HERMES system. The primary task of HERMES system is to provide direct computer support for the argumentation, negotiation and mediation process in group decision-making. It is not designed to support group decision task generation and identification [13]. The issues in the argumentation framework of HERMES correspond to the decisions to be made, or the goals to be achieved [12]. That is, an issue just is one of many components consisting of a group decision task concerned in this paper. Therefore, it is required to develop a new framework of argumentation on group decision task generation and identification.

In artificial intelligence research field, a frame is a useful and intuitive knowledge representation frequently used to represent human memory, events, and expertise [20]. A frame has many slots in which to store different attributes, which can be used to warehouse the information structure of a decision task and an argumentation. It is easy to visualize different frames and their relations [18], which we believe would be useful to support group decision task generation and identification.

In next section, according to the authors’ proposed decision task model, we grouped the argumentation of decision task generation and identification into four frames (Label, Object, Function and Content) based on Toulmin’s argumentation structure [36], and Bui and Bodart’s argumentation factors [1]. Then, we adopted the frame-based argumentation (FBA) information structure in implementing our prototype group argumentation support system (FBA-GASS). The focus of the remainder of this paper is on how a group can generate and identify group decision tasks using our FBA-GASS.

## 3. Definition of a decision task and its components

The concept of a decision task is more often implied than defined. Many research works related to decision tasks simply use the term and assume the meaning to be consistent [16,39]. However, definitions of decision tasks are often equivocal and nonunanimous, as a result of which, decision makers and decision executors often produce inconsistent understandings of a decision task in the course of making real decision, thus reduce the efficiency of decisionmaking. Scholars also misunderstand one another in the course of academic exchange on decision tasks and group tasks, so it is necessary and important to define a decision task explicitly in GDSS/GSS contexts and present its components.

In order to present a working definition of a decision task, we first discuss components of a typical decision task by way of a meeting example occurred in an Import and Export Company of Electrical Equipment in Xi’an, China. In a meeting of the department, the department manager stated by saying ‘‘In order to ensure the engineering project in Malaysia to be on schedule, it is necessary for us to transport major electrical equipment for this project to Malaysia from China before February 25 of 2002. The question is how do we transport the main electrical equipments?’’ From this example, we can clearly infer what are a decision task and its components. ‘‘In order to ensure the engineering project in Malaysia stays on schedule’’ is the goal of the decision. ‘‘It is necessary for us to transport the major electrical equipment for this project to Malaysia from China’’ is a decision task. ‘‘We’’ are decision makers and decision executors as well. ‘‘How do we transport the main electrical equipment?’’ is a decision problem. ‘‘Before February 25 of $2 0 0 2 ^ { \circ }$ is a constraint. Five components are involved in a decision task: decision makers, decision executors, decision goals, decision problems and decision constraints. We define these five components and other concepts needed to discuss tasks. These components and concepts are represented explicitly in our FBA-GASS.

Definition 1 (Decision makers). Decision makers are people who lead a decision task. Let DM be a set of decision makers, then for n decision makers, we have $\mathrm { D M } ( n ) { = } \{ \mathrm { D M } _ { 1 } , . . . , \mathrm { D M } _ { n } \}$

If $n = 1 ,$ , then the decision task is an individual decision task.

If n>1, then the decision task is a group decision task.

In the above example, $\mathrm { { D M } _ { 1 } = \mathrm { { g e n e r a l } } }$ manager of power transmitting and transforming; $\mathrm { D M } _ { 2 } { = } \mathrm { m a n a g e r }$ of power transmitting and transforming team one.

Definition 2 (Decision executors). Decision executors are people who are responsible for carrying out a decision. Let DE be a set of decision executors, then $\mathrm { D E } ( n ) { = } \{ \mathrm { D E } _ { 1 } , . . . , \mathrm { D E } _ { n } \}$

If ${ \mathrm { D M } } \land { \mathrm { D E } } = \phi$ , then decision-making is defined as benefit-independent decision-making.

If $\mathrm { D M } \land \mathrm { D E } \neq \ \phi .$ , then the decision-making is a benefit-dependent decision-making.. In the above example, we assume $\mathrm { D E } _ { 1 } , \ \mathrm { D E } _ { 2 } , . . . , \ \mathrm { D E } _ { n } ,$ are power transmitting and transforming team one members 1, $2 , . . . , n .$

Definition 3 (Decision goals). Decision goals are the objectives that decision-makers want to reach or agree upon in a decision task. Let DG be a set of decision goals, then $\mathrm { D G } ( n ) { = } \{ \mathrm { D G } _ { 1 } , . . . , \mathrm { D G } _ { n } \}$

If $n = 1$ , then the decision task is a single-goal one. If n>1, then the decision task is a multi-goal one.

In the above example, $\mathrm { D G } _ { 1 } = ^ { 6 6 \prime }$ To ensure that the engineering project in Malaysia stays on schedule’’.

Definition 4 (Decision problems). Decision problems are obstacles that have to be overcome before making a decision. Let DP be a set of decision problems, then $\scriptstyle \mathrm { { D P } } ( n ) = \{ \mathrm { { D P } } _ { 1 } , . . . , \mathrm { { D P } } _ { n } \}$

In the above example, $\mathrm { D P } 1 = ^ { 6 6 }$ How do we transport the main electrical equipments?’’

Definition 5 (Decision constrains). Decision constraints are constraints for a decision task. Let DC be a set of decision constraints, then $\mathrm { D C } ( n ) { = } \{ \mathrm { D C } _ { 1 } , \ . \ . . ,$ $\mathrm { D C } _ { n } \}$

In the above example, $\mathrm { D C } _ { 1 } = ^ { 6 6 }$ before February 25 of $2 0 0 2 ^ { \circ }$

Definition 6 (Decision task). Based on the five components defined above, a decision task is then defined as the work to be done by decision makers including searching for the right executors and a correct course of actions to achieve certain decision objectives within certain constrains and problems. Let DT be a set of decision tasks, then for n tasks, we have $\mathrm { D T } { = } \{ \mathrm { D T } _ { 1 } , . . . , \mathrm { D T } _ { n } \}$

In the above example, $\mathrm { D T } _ { 1 } = ^ { 6 6 } \mathrm { T } _ { 0 }$ transport the main electrical equipments of this project to Malaysia from China.’’

Before carrying out a decision task, decision makers, decision executors, decision objectives, decision problems and constrains must be clearly identified. The five components have very close relationships with the decision task, but they obviously are not themselves a decision task. The relationships among the five components and the decision task are expressed as follows:

$$
\mathrm{DT} = F _ {\mathrm{T}} (\mathrm{DM}, \mathrm{DE}, \mathrm{DG}, \mathrm{DP}, \mathrm{DC})\tag{1}
$$

Here, $F _ { \mathrm { T } }$ is a set of task relations.

Several other variables are also important for decision tasks. In the above Malaysia project task, decision group members need to investigate ways to solve the problem. For instance, to transport the main electrical equipments from Xi’an to Malaysia requires deciding which route and which kind of transportation tools need to be taken. Indeed, there are many alternatives to solve the problem. It will be necessary for indicators to be viewed when determining criteria for the decision. If the criteria is expenses, then to make a mix by train and sea may be the best choice. Money and time are considered decision resources.

Definition 7 (Alternatives). Alternatives are candidate actions that decision makers from which the group could choose to execute. Let A be a set of alternatives, $A ( n ) { = } \{ A _ { 1 } , . . . , A _ { n } \}$

In the above example, $A _ { 1 } =$ the mix of by train and by sea, and $A _ { 2 } = \operatorname { t h e }$ mix of by land vehicle and by sea.

Definition 8 (Decision criteria). Decision criteria are standards by which decision makers decide whether a decision problem has been solved, and then decide whether the decision reached is satisfactory. Let C be a set of decision criteria, then $C ( n ) { = } \{ C _ { 1 } , . . . , C _ { n } \}$

In the above example, $C _ { 1 } { = } \mathrm { p r o m p t n e s s } ;$ $C _ { 2 } =$ expenses.

Definition 9 (Resources). Resources are consumed during carrying execution, such as money, time, materials, labor, etc. Let R be a set of resources, then $R ( n ) { = } \{ R _ { 1 } , . . . , R _ { n } \}$

In the above example, $R _ { 1 } = \mathrm { m o n e y } ; R _ { 2 } = \mathrm { t i m e } .$

Definition 10 (Actions). Actions are activities executed for the task, and often are accompanied by resources consumption. Let ACT be a set of actions selected, then $\operatorname { A C T } ( n ) { = } \{ \operatorname { A C T } _ { 1 } , . . . , \operatorname { A C T } _ { n } \}$

In the above example, $\mathrm { A C T } _ { 1 } = ^ { 6 6 } \mathrm { T c }$ transport main electrical equipments to Hong Kong from $\mathrm { X i } ^ { \prime } { \mathrm { a n } } ^ { \prime } \mathrm { \bar { \Psi } }$ ; $\mathrm { A C T } _ { 2 } = ^ { 6 6 }$ To transport the main electrical equipments from Hong Kong to Malaysia’’.

Alternatives, criteria, resources and actions are key elements considered in solving the decision problems involved in a decision task. The relationships among the four elements are expressed as follows:

$$
\mathrm{DP} = F _ {\mathrm{P}} (A, C, R, \text { ACT })\tag{2}
$$

where, $F _ { \mathrm { P } }$ is a set of task relations.

Using a structural model to illustrate the relationships among the components in the Malaysia project decision-making, it can be shown as in Fig. 1.

Table 1  
Decision types by executors and of participants

<table><tr><td></td><td>Individualdecision task</td><td>Groupdecision task</td></tr><tr><td>Execution-dependentdecision task</td><td>(I) One decides what to be done by himself.</td><td>(II) Group members decide what to be done by themselves.</td></tr><tr><td>Execution-independentdecision task</td><td>(III) One decides what to be done by others.</td><td>(IV) Group members decide what to be done by others.</td></tr></table>

Based on Definition 2 for decision executors, we could classify decision tasks as execution-dependent decision tasks or execution-independent decision tasks. If the decision makers and the action executors are the same people, a decision task can be viewed as execution-dependent decision task, otherwise a decision task can be viewed as execution-independent. An execution-dependent decision may affect only the decision makers, but the execution-independent decision may affect others as well.

Execution-dependent decision tasks and execution-independent decision tasks are different from individual decision-making and group decision-making. The latter are classified according to the number of decision makers. Based on their relationships and the number of decision-makers and executors, a classification of decision-making is shown in Table 1.

![](/api/attachments/FA8K6YC8/fulltext/images/2c86c1099782c5ae22ccdc0ce800f10f21fdb797b8bea953c554febddf3f972e.jpg)  
Fig. 1. Example of a decision task and its components.

Decision tasks of types I and II are private behavior and generally appear in an informal organization. Types III and IV often appear in a formal organization. Type III, as an individual decision, is not a focus of research regarding group decision support systems. The decision task of type IV is often involved in a formal organization and is the focus of our research.

Decision task of type IV in a formal organization often originates with a motion presented by a decision maker, a decision executor or some other relevant person. A motion is a formal proposal expected to be agreed upon by other people and may be an objective, a problem, or an alternative or a mix of the elements of a decision-making. So a motion can be defined as follows:

Definition 11 (Motion). A motion is a formal proposal concerning a decision task and is composed of a set of the same elements as a decision task (see Definition 6). Let MOT be a motion, then MOT= {DM, DE, DG, DP, DC}.

If and only if DM p / and DE p /and $\mathrm { D G } \neq ~ \phi$ and $\mathrm { D P } \neq ~ \phi$ and $\mathrm { D C } \neq \phi ,$ then $\mathrm { D T } _ { 1 } { = } \mathrm { M O T } _ { 1 }$

For example, $\mathrm { M O T } _ { 1 } = ^ { \ast } \mathrm { T o }$ transport the main electrical equipments to Hong Kong from $\mathrm { X i } ^ { \prime } { \mathrm { a n } } ^ { \prime }$

## 4. Conceptual model and system implementation

During the phase of group decision task generation, group members should make it clear the decision task structure of each proposed candidate task through group discussion and argumentation. In the following sections, we present in detail how the above decision variables are incorporated into a conceptual model for group decision ask generation and identification, as well as our FBA-GASS prototype system.

## 4.1. Conceptual model for decision task generation and identification

Decision task of type VI has the following characteristics: decision makers are members of one group, while executors are members of another group, and the results of actions may affect a larger number of members in a third group. In order to reach consensus, group members need to support generation and identification of decision tasks through argumentation.

Generally, the conceptual model of the generation and identification of decision tasks in an organization may be described as in Fig. 2, which consists of two parts. In the first part, decision group members propose motions. In the second part, group members identify decision tasks through argumentation support in four steps: transforming motions to decision tasks, classifying decision tasks, sorting decision tasks and determining the components of the selected decision tasks.

## 4.2. Frame-based argumentation and GASS prototype

The argumentation of decision task generation and identification consists of four argumentation frames: label frame, object frame, function frame and content frame.

(1) Label frame, which is used to label the speakers’ status and the time he speaks.

```txt
{Label frame: viewer and time
Viewer: {indicate who gives the speech in a group}
Time: {identify when a viewer gave a speech}}.
```

(2) Object frame, which has one slot to store the object of argumentation-addressed.

{Object frame: a decision task, claim, evidence, position, weight or viewer}.

![](/api/attachments/FA8K6YC8/fulltext/images/66f150a70168b6840b7d76c4d15275e3e6034d0f9ff44f8820b42ce35c5ea38b.jpg)  
Fig. 2. A conceptual model of Decision task generation and identification.

(3) Function frame, in which one slot is used to store the types of speakers’ claims, evidence, positions, weights, reasons or other messages.

```txt
{Function frame: Claim: {refer to a statement related to a decision task} or
Evidence: {refer to evidence supporting a claim} or
Position: {refer to a position backing a corresponding claim} or
Weight: {indicate the degree of importance of a decision task proposed by group members} or
Reason: {explain why a group member makes a subjective judgment of a position or a weight} or
Other Message: {the information exchanged among the speakers}}.
```

(4) Content frame, has one slot to store the text of what the speakers have said.

Based on the above frame-based argumentation (FBA) representing, a prototype of FBA-GASS, which consists of several modules as shown in Fig. 3, has been implemented in our laboratory on a Microsoft Windows 2000 server.

FBA-GASS prototype has a two-layered structure. The top interface layer is a Browser/Server component using ASP and Java-script language, and the bottom layer is a Microsoft Access database. Many important components used in FBA-GASS, such as synchronous

EBS and argumentation, asynchronous EBS and frame-based argumentation visualization, etc., have been coded in ActiveX using an object-oriented language based on the COM technology. At any time, participants in an argumentation session can access the FBA-GASS through the Internet if they are registered members.

FBA-GASS provides a distributed platform that allows group members to participate in argumentation during decision task generation and identification without having to be physically present at the same place.

The synchronous EBS and argumentation component not only can support group members in generating ideas in EBS but also can support the group members in synchronously arguing some objects by organizing the argumentation information of group members by label, object, function and content in structured frames.

As a supplement to synchronous argumentation, a voting tool is incorporated into this component in order to prevent an argumentation deadlock.

The asynchronous EBS component supports the idea generation of group members at different place in different time.

![](/api/attachments/FA8K6YC8/fulltext/images/ddea21795c3f8df5b3878b24451f34f9291f536a14b25abc6f63ad307214560f.jpg)  
Fig. 3. Framework of the FBA GASS.

FBA-GASS also provides administrative maintenance for its users. As a knowledge repository, it provides historical argumentation and decision information for group members, who can navigate seamlessly through argumentation states and objects.

## 4.3. Key procedures for decision task generation and identification using FBA-GASS

For execution-independent group decision-making (type IV), there are many reasons for argumentation to the generation and identification of a decision task. First, the decision makers should choose the decision executors. Second, the understandings to the decision objectives may be inconsistent and unclear among the decision makers, the decision executors and the members who are influenced by the decision. Third, the understandings of decision problems are inconsistent and unclear among the inner group of decision makers. Finally, the understandings of decision constrains are inconsistent and unclear among decision group members. Using FBA-GASS, a decision group could generate motions and identify the decision tasks from tasks by the following procedures.

## 4.3.1. Generating motions using asynchronous EBS and synchronous EBS

Group members may propose their motions through either asynchronous electronic brainstorming (EBS) or asynchronous EBS in FBA-GASS, round by round until an agreed-upon time limit has elapsed.

(1) Generating motions using asynchronous EBS prior to a computer-mediated meeting in preparation for the meeting.

A motion is stored in the motion frame by decomposing a whole motion into elements. A motion consists of two sub-frames named the motion label frame and the motion content frame.

Motion label frame: {motion ID number, motion name, time stamp, and name of sponsor}.

If a motion is a new one, the motion ID is encoded in a time sequence. The sponsor fills in the motion name, and the computer fills in other items automatically according to information that has been registered by the group members.

Content frame: {decision makers, decision executors, decision goals, decision constrains and decision problems

Decision problem frame: {Alternatives, criteria, resources and actions}}.

In asynchronous EBS, a motion-sponsor can input all or part of these elements of a motion in a form. These elements of the motion are also labeled by element ID number, time stamp, and name of sponsor. The sponsor himself or other members can supply the elements of a motion, such as decision makers, decision executors, decision goals. If the motion sponsor and element sponsor are the same person, the label of time and name of sponsor will be ignored. On the other hand, group members can add a new element in a new form by double clicking on the hyperlink of this element.

The motions generated by asynchronous EBS are saved and will be presented to group members in synchronous argumentation, as shown in Fig. 4.

(2) Generating motions using synchronous EBS during a computer-mediated meeting under the direction of the facilitator [2].

A motion generated in a synchronous electronic brainstorm is structured by label, object, function and content frames as shown in Section 3.2.

Motion label frame: {motion sponsor, time stamp}.

Object frame: {the motion that has been presented by the group members}.

Function frame: {decision makers, decision executors, decision objectives, decision problems or decision constraints of a motion}.

![](/api/attachments/FA8K6YC8/fulltext/images/2f4497e656de64c4fc8a1f1cc39d6f15ec97a3dd3caf21c5dfb46f4714f528ad.jpg)  
Fig. 4. Information flowchart of EBS and argument In FBA-GASS.

Content frame: {the text of what the speakers have said}.

All the elements presented by the group members are linked to corresponding motions, based on the motion ID. All the elements with the same motion ID constitute a complete motion. The motions generated by the synchronous EBS are saved in a database and will be displayed according to time and the number of its elements that have been entered in the form.

(3) Using asynchronous EBS, during the second round of computer-mediated meeting, group members can furnish joint motions as supplementary to the motions proposed by individuals, especially by adding to the motion items such as evidence when slots are vacant or marked for being appended.

## 4.3.2. Identify decision tasks by synchronous argumentation

In the following procedure, three important steps, transforming motions to decision tasks, classifying decision tasks and sorting decision tasks, are taken to identify decision tasks by synchronous argumentation as shown in Fig. 5.

(1) Transforming motions to decision tasks by group argumentation

The facilitator can use an agent to extract those motions having the identification features of a decision task that appear in Definition 6 from the FBA-GASS database automatically. Once all the items of a motion have been entered, the motion will be separated from the database of motions and moved into another database of candidate decision tasks.

For each candidate task, all the group’s members can present their own claims and supporting evidence through synchronous argumentation. They can also state their own positions regarding other members’ claims and reasons for having taken those positions. Fig. 5 illustrates the most complete situation of argumentation with only two claims. The top level of the hierarchical structure is a decision task and the bottom level is composed of reasons.

By use of an automatic encoding rule, the hierarchical structure of Fig. 5 is saved in the database of synchronous argumentation in a continuum of selected decision tasks with their argumentation factors. Thus, all the information generated during group argumentation is recorded in the database.

The facilitator will end the process when one of the following conditions is met: (1) Consensus is found; (2) Agreement is reached by vote; or (3) Allowed time has elapsed [1,6].

(2) Selecting indicators for classification of decision tasks

The group leader or facilitator will complete this work ahead of the meeting. The indicators for classification of decision tasks are selected according to fields, industries or decision executors’ department.

(3) Classifying decision tasks through argumentation

The classification of decision tasks is based on the indicators selected by the facilitator. Group members comment on each decision task for which a department should be responsible and each industry in which the decision task should be applicable After sufficient communication, group members vote on the type of decision task to which each task should be assigned. Through linear weight averaging of all the opinions on each decision task, the classes of the decision tasks are decided.

![](/api/attachments/FA8K6YC8/fulltext/images/e34421c190b8845604359ac87c6d79b7ff63d3bfdb582c1e34d3dd5214a51757.jpg)  
Fig. 5. The process of synchronous argumentation.

(4) Sorting decision tasks through argumentation

The sorting of decision tasks is based on two indicators: urgency and influence. The scale of urgency and influence is 1 to 10. Group members comment on the urgency and influence of each decision task. After sufficient communication, each group member gives his own sorting of decision tasks based on the two indicators. Through linear weight averaging of all the opinions on each decision task, the decision tasks are sorted according to urgency, influence and aggregate weight.

At last, the facilitator will present all the decision tasks having been identified from the motions, and the decision tasks having been classified and sorted.

## 5. An example of group task generation and identification using FBA-GASS

In order to explain how to use our prototype of FBA-GASS to support the argumentation of decision task generation and identification, we present a case study, conducted at Import and Export Company of Electrical Equipment in Xi’an of China.

In this case, six high-level and middle-level managers attended a computer-mediated meeting. They were general manager, vice general manager, managers of first, second and third branch of power transmitting and transforming, and manager of import – export branch. Such meetings are held regularly at the company, but this one used FBA-GASS for the first time. The purpose of the meeting was announced how the company operated in the first quarter of this year and to determine how problem-solving decisions could be made more effectively. All the decision-makers gathered in one meeting room in which a computer terminal was installed at each table. Each person attending this meeting could communicate with every other individual each other through the terminals, which were linked on the intranet. Meetings are regularly announced on the web a week ahead of time.

5.1. Import and Export Company decision groupgenerating motions

(1) Generate motions using asynchronous EBS.

During the week prior to a computer-mediated meeting, all members will have presented their motions through the asynchronous EBS as illustrated in Fig. 6. The ID number of each element of a motion is encoded automatically based on the rule of encoding. If an element has appeared in the database, the ID number of the element will not be encoded repeatedly, else it will be encoded a new ID number.

(2) Generate motions using synchronous EBS during first computer-mediated meeting. A frame used to receive motion information generated in synchronous EBS is composed of motion sponsor, time stamp, object, function and content. Here, there are only motion name and the elements of the motion organized by synchronous EBS. The five frames prearranged by the group members in synchronous EBS are illustrated in Table 2.

(3) Supply supplements to the motions by use of asynchronous study.

The general manager added $\mathrm { D G } _ { 2 }$ (to reduce the costs of the project overseas) to $\mathrm { M O T _ { 1 } }$ during the interval.

In this application example, the group generated two motions $\mathrm { ( M O T _ { l } }$ and $\mathrm { M O T } _ { 2 } )$ by asynchronous EBS and 11 motions $( \mathrm { M O T } _ { 3 } , \ \mathrm { M O T } _ { 4 } , . . . )$ through synchronous EBS. Five important motions are presented in the following.

$\mathrm { M O T _ { 1 } , }$ , To speed up the schedule of the project of suspended electromagnetic iron in Taiwan.

$\operatorname { M O T } _ { 2 } \mathrm { : }$ To increase the budget of the project in Guangdong province.

$\operatorname { M O T } _ { 3 } \mathrm { : }$ To deal with the quality problem of TSG project in Malaysia.

$\operatorname { M O T } _ { 4 } { \mathrm { : } }$ To distribute second batch of GIS equipments to Hong Kong.

$\operatorname { M O T } _ { 5 } \colon$ To bid for the transformer project in The Philippines.

## 5.2. Import and Export Company decision group identification of decision tasks by synchronous argumentation

(1) Transform motions to decision tasks by group argumentation.

After filtering the motion database automatically to obtain the candidate tasks from the motions generated by group members, 13 motions were filtered out and saved into the candidate task database. Using the synchronous argumentation component, the decision group argued each candidate task as shown in Fig. 5 and agreed on 13 decision tasks.

![](/api/attachments/FA8K6YC8/fulltext/images/cbb9f5cad386c00923fdb67e6ada15063d8674fde44cc0281e49ff0424c75abd.jpg)  
Fig. 6. A synchronous E-brainstorming for generating motions.

Five frames about motion information generated in synchronous EBS

<table><tr><td>Motion sponsor</td><td>Time stamp</td><td>Object</td><td>Function</td><td>Content</td></tr><tr><td>1st branch manager</td><td>03.28 14:35</td><td></td><td>new motion</td><td>(MOT3) To deal with the quality problem of TSG of the project in Malaysia</td></tr><tr><td>Vice general manager</td><td>03.28 14:41</td><td>MOT3</td><td>new DM</td><td>(DM3) 1st branch manager</td></tr><tr><td>1st branch manager</td><td>03.28 14:42</td><td>MOT3</td><td>new DE</td><td>(DE1) 1st branch</td></tr><tr><td>3rd branch manager</td><td>03.28 14:44</td><td></td><td>new motion</td><td>(MOT4) To distribute second batch of GIS equipments to HANGKONG</td></tr><tr><td>General manager</td><td>03.28 14:49</td><td>MOT3</td><td>new DG</td><td>(DG1) to assure the project on the schedule</td></tr></table>

(2) Select indicators for classifying decision tasks.

The company has only four branches. The facilitator appended these branch names as indicators into a code database initializing process.

(3) Argumentation of classification of decision tasks.

Based on the functions of four branches, the group members classified 13 tasks into four groups through argumentation. Five decision tasks were to be executed by the first branch of power transmitting and transforming as follows.

$\mathrm { D T } _ { 1 } \colon$ To bid for the transformer project in The Philippines.

$\operatorname { D T } _ { 2 } \colon$ To speed up the schedule of the project of Shanguang DC.

$\operatorname { D T } _ { 3 } \colon$ To deal with the quality problem of TSG project in Malaysia.

$\mathrm { D T } _ { 4 } \mathrm { : }$ To distribute second batch of GIS equipments to Hong Kong.

$\operatorname { D T } _ { 5 } \colon$ To increase the budget of suspended electromagnetic iron project in Taiwan.

## (4) Argumentation sorting of decision tasks.

The decision group also argued importance as being based on two indicators: urgency and influence. Fig. 7 shows the interface of synchronous argumentation of sorting decision tasks into four panels. The upper-left panel shows the contents of argumentation; the upper-right panel displays the list of objects for argumentation, which is driven by a pop-menu of ‘‘Object Type’’; the lower-left panel is a set of forms for entering all kinds of messages; and the lower-right panel shows a set of buttons to use for settings. In Fig. 7, all the shaded information marked was generated automatically by FBA-GASS.

Fig. 8 shows the argumentation related to the importance of decision task DT<sub>1</sub> : To bid for the transformer project in Philippines.

In Fig. 8, the encoding rule to the ID number of argumentation factors is to connect a code of argumentation function, an ID of argumentation object and a digital number by $\cdot , \cdot ,$ . The code of argumentation function consists of T, C, E, P and R, which respectively represent decision task, claim, evidence, position and reason. The ID numbers in Fig. 8 mean as follows.

ID number of the decision task is T1;

ID number of the second claim to T1 is C-T1-2;

ID number of the fist evidence to claim C-T1-2 is E-C-T1-2-1;

ID number of the fist position to claim C-T1-2 is P-C-T1-2-1;

ID number of the fist position to evidence E-C-T1- 2-1 is P-E-C-T1-2-1-1; and

ID number of the first reason for position P-E-C-T1-2-1-1 is R-P-E-C-T1-2-1-1-1.

All the numbers of each object were automatically encoded by computer and all the contents of argumentation were saved in a database.

## 6. System evaluation and limitation

It is well known that strong information –organization support will promote group work productivity [3,23]. FBA-GASS delivers well-structured synchronous EBS and asynchronous EBS to support group members in proposing their motions. Using FBA-

![](/api/attachments/FA8K6YC8/fulltext/images/fd6e6e39aea0897b74c8297a4445f0f913d3f66655d14237b10e3c1bb05872a7.jpg)  
Fig. 7. An interface of synchronous argumentation for sorting decision tasks.

GASS, a single member of a group can present claims, objects, positions, and evidence on a candidate task in the frame-based argumentation information structure, which makes it easy for other members to share and understand his view of the total task. To verify that FBA-GASS provided superior support to a decision group in the process of the generation and identification of decision tasks, we devised an experiment to evaluate outcome using FBA-GASS prototype in a lab experiment.

To the experiment results, we used four quantitative and operable indicators to evaluate the group performance: the number of perceived motions, the number of decision tasks generated, the number of decision tasks having incomplete elements, the number of selected tasks.

## 6.1. Experiment design

The experiment participants were two PhD candidates (one male, one female), one master’s candidate (male) and three undergraduate business students (two male, one female). All were enrolled in the Department of IT and Management in a university business school. The average age was 26.1 years. Each participant worked alone with a desktop computer networked with the server installed the software of FBA-GASS.

The experimental task was to generate motions to increase profits and enhance the competitive strength of Import and Export Company of Electrical Equipment in Xi’an and then to argue which motions should be carried out.

![](/api/attachments/FA8K6YC8/fulltext/images/d937c102a7cb49c8f5cebbe7753d67ddf1a997f5e13adf90c2cd421eb3fab66d.jpg)  
Fig. 8. Illustration of argumentation on decision task T<sub>1</sub>.

In order to familiarize participants with the details of operation in this firm, one of the authors, as a facilitator, organized a training course about the firm that included video-tapes and reading materials. From a research perspective, the motions generated could be somewhat strategic, which would promote higher involvement and enable participants to draw on personal knowledge and experiences. For role-playing, the roles of branch managers and employees were randomly assigned to the participants.

The experiment was completed under the direction of the facilitator by the following procedures:

(1) After the introductory training, the facilitator took the participants to the experimental site, a computer lab and asked them to generate as many motions to increase the business profit and enhance the competitive strength as possible and then to argue the feasibility of each of them.

(2) Based on the facilitator’s advice, the participants took 1 h to generate motions using synchronous E-brainstorming of FBA-GASS.

(3) Half an hour later of the end (2), the participants took thirty minutes to provide supplementary motions using the asynchronous one.

(4) After a half-hour break, under the help of the facilitator, the participants took another 30 min to argue and select the decision tasks resulting from generated motions using the synchronous argumentation function embedded in synchronous Ebrainstorming of FBA-GASS.

## 6.2. Experimental results

In 2 h, using FBA-GASS, each participant generated 9.167 motions on average as shown in Table 3. There were no decision tasks with incomplete elements, for the frame-based information structure in FBA-GASS made it easy for the group members to find and fill the vacant slots of a motion or task. Moreover, each participant generated an average 4.167 decision tasks. And for each participant, on average, there were 1.5 selected decision tasks.

## 6.3. Limitations of FBA-GASS

Based on the experimental experience, we find that FBA-GASS is useful to support group decision task generation and identification in the following organizational conditions:

Table 3  
Experimental results for the group using FBA-GASS

<table><tr><td>Item</td><td>Mean</td><td>S.D.</td></tr><tr><td>Total number of motions</td><td>9.167</td><td>2.317</td></tr><tr><td>Number of incomplete tasks</td><td>0.000</td><td>0.000</td></tr><tr><td>Number of tasks generated</td><td>4.167</td><td>0.983</td></tr><tr><td>Number of selected tasks</td><td>1.500</td><td>0.548</td></tr></table>

(1) The decision tasks are behavior requirements that are typically encountered in organizational decision-making groups, especially for the decision task of type IV, group members decide what to be done by others.

(2) The organization leader or top management team does not satisfy the organization performance but could not decide what to do.

(3) When organizational environments change rapidly, there are many optional motions in the organizational decision-making group. For FBA-GASS saves all the group argumentation information into database with the frame-based argumentation information structure, which makes it easy for the group leader or facilitator to process the argumentation results of group decision task generation and identification.

However, due to the multi-components of the decision task defined in our model, we do not think that FBA-GASS can deliver well support for the following group decision task generation and identification:

(1) the routine management or operational decision occurred in organizations;

(2) the organizational decision is dependent on one leader or few members of top management team, and the leader has his candidate decision tasks in mind.

## 7. Conclusions and future directions

In this paper, we have defined a decision task with five elements: decision makers, decision executors, decision objectives, decision problems and decision constraints.

Based on the decision task definition, we have described a two-part conceptual model for generation and identification of group decision tasks in an organization. In the first part, decision group members propose motions. In the second part, group members identify the decision tasks through argumentation in four steps: transforming motions to decision tasks, classifying decision tasks, sorting decision tasks and recording the components of the selected decision tasks. We have emphasized that this model is designed for the decision task of type IV, group members decide what to be done by others.

Furthermore, we have presented the frame-based argumentation (FBA) information structure that has been implemented in the FBA-GASS prototype. Through providing the procedures and an application at Import and Export Company of Electrical Equipment in Xi’an of China, we have clearly showed how a decision group can use our FBA-GASS to generate and identify group decision tasks. By the given four group performance indicators, we have described the evaluation results of the FBA-GASS prototype in a lab experiment.

The work presented here is a part of a larger project that attempts to use structured argumentation to support collaboration work in group decision-making in complex decision tasks. Some components of the FBA-GASS prototype still are being developed or need to be improved. Such components include multimedia visualization of group argumentation, group decision integration tools to help group members to reach consensus on conflicted motions, evidence and alternatives, etc., summarization of group EBS and argumentation, task-oriented group knowledge extraction from intranet or internet sources, and solving approaches to decision problems, and identification of creative or tacit knowledge emerging during group argumentation.

Our next research work will focus on group decision task structuring, problem formalization and generation of decision alternatives. We also believe that that many behavior problems could be researched using our FBA-GASS. Among these are: how to optimize the group argumentation procedures, what main influence factors in the Chinese cultural background block effective group outcomes, how can group members resolve conflicts in evidence, claims, problem solutions and weighing decision alternatives.

## Acknowledgements

The research is supported by Natural Science of Foundation of China (NSFC) project No. 79990580 (06-30-1999) and excellent group project No. 70121001 (12-30-2001).

## References

[1] T.X. Bui, F. Bodart, et al., ARBAS: a formal language to support argumentation in network-based organizations, Journal of Management Information Systems 14 (3) (1997) 223 – 238.

[2] D.J. Campbell, Task complexity: a review and analysis, Academy of Management Review 13 (1) (1988) 40– 52.

[3] A.R. Dennis, Information exchange and use in group decisionmaking: you can lead a group to information but you can’t make it think, MIS Quarterly 20 (4) (1996) 433–455.

[4] G. DeSanctis, R.B. Gallupe, A foundation for the study of group decision support systems, Management Science 33 (5) (1987) 589–609.

[5] D.J. DeTombe, Complex societal problems in operational research, European Journal of Operational Research 140 (2) (2002) 232– 240.

[6] G.W. Dickson, J.L. Partridge, L.H. Robinson, Exploring modes of facilitative support for GDSS technology, MIS Quarterly 17 (2) (1993) 173 – 194.

[7] T. Gordon, N. Karacapilidis, The zeno argumentation framework, Proceedings of the 6th Int. Conference on AI and Law (ICAIL’97), Melbourne, Australia, ACM Press, New York, 1997, pp. 10 – 18.

[8] J.M. Hender, D.L. Dean, T.L. Rodgers, J.F. Nunamaker, An examination of the impact of stimuli type and GSS structure on creativity: brainstorming versus non-brainstorming techniques in a GSS environment, Journal of Management Information Systems 18 (4) (2002) 59– 85.

[9] K.M. Hilmer, A.R. Dennis, Stimulating thinking: cultivating better decisions with groupware through categorization, Journal of Management Information Systems 17 (3) (2000) 93 – 114.

[10] G.H. Hua, S.O. Kimbrough, On hypermedia-based argumentation decision support systems, Decision Support Systems 22 (3) (1998) 259– 275.

[11] S.M. Kaplan, A.M. Carroll, Supporting collaborative processes with Conversation Builder, Computer Communications 15 (8) (1992) 489 – 501.

[12] N. Karacapilidis, Integrating new information and communication technologies in a group decision support system, International Transactions in Operational Research 7 (2000) 487 – 507.

[13] N. Karacapilidis, D. Papadias, Collaborative environmental planning with GeoMed, European Journal of Operational Research 102 (2) (1997) 335 – 346.

[14] N. Karacapilidis, D. Papadias, A computational approach for argumentative discourse in multi-agent decision-making environments, AI Communications 11 (1) (1998) 21 – 33.

[15] N. Karacapilidis, C. Pappis, Computer-supported collaborative argumentation and fuzzy similarity measures in multiple criteria decision-making, Computers & Operations Research 27 (7–8) (2000) 653– 671.

[16] S.S.K. Lam, The effects of group decision support systems and task structures on group communication and decision quality, Journal of Management Information Systems 13 (4) (1997) 193– 216.

[17] M.O. Locks, The logic of policy as argument, Management Science 31 (1) (1985) 109 – 116.

[18] A.B. Markman, Knowledge Representation, Lawrence Erlbaum, Mahwah, NJ, 1999.

[19] J.E. McGrath, Groups: Interaction and Performance, Prentice-Hall, Englewood Cliffs, NJ, 1984.

[20] M.L. Minsky, Artificial Intelligence, Oregon State System of Higher Education, Eugene, 1974.

[21] S.M. Miranda, R.P. Bostrom, Meeting facilitation: process versus content interventions, Journal of Management Information Systems 15 (4) (1999) 89 – 114.

[22] I.I. Mitroff, R.O. Mason, V.P. Barabba, Policy as argument: a logic for ill-structured decision problems, Management Science 28 (12) (1982) 1391– 1404.

[23] J.F. Nunamaker, A.R. Dennis, J.S. Valacich, D.R. Vogel, J.F. George, Electronic meeting systems to support group work, Communications of the ACM 34 (7) (1991) 40 – 61.

[24] J.F. Nunamaker, R.O. Briggs, D.D. Mittleman, D.R. Vogel, P.A. Balthazard, Lessons from a dozen years of group support systems research: a discussion of lab and field findings, Journal of Management Information Systems 13 (3) (1997) 163– 207.

[25] M.S. Poole, D.R. Siebold, R.D. McPhee, Group decisionmaking as a structurational process, Quarterly Journal of Speech 71 (1) (1985) 74 – 102.

[26] T.S. Raghu, R. Ramesh, A.M. Chang, A.B. Whinston, Collaborative decision-making: a connectionist paradigm for dialectical support, Information Systems Research 12 (4) (2001) 363–383.

[27] R. Ramesh, A.B. Whinston, Claims, arguments, and decisions: formalisms for representation, gaming, and coordination, Information Systems Research 5 (3) (1994) 294–325.

[28] A. Ravenscroft, Designing argumentation for conceptual development, Computers and Education 34 (3– 4) (2000) 241– 255.

[29] S.P. Robbins, Essentials Of Organizational Behavior, 3rd ed., Prentice-Hall, Englewood Cliffs, NJ, 1992.

[30] M.H. Saeedi, J.A.A. Sillince, Issues of feasibility, coherence and robustness in a premise-to-claim model of argumentation: results from four experiments, European Journal of Operational Research 133 (2001) 94 – 119.

[31] M.E. Shaw, Group dynamics, The Psychology of Small Group Behavior, McGraw-Hill, New York, 1981.

[32] J.A.A. Sillince, Argumentation and contract models for strategic organization support systems, Decision Support Systems 16 (1996) 255 – 274.

[33] J.A.A. Sillince, M.H. Saeedi, Incorporating rhetorical and plausible reasoning in an electronic conferencing system, Knowledge Based Systems 12 (1999) 113– 127.

[34] J.A.A. Sillince, M.H. Saeedi, Computer-mediated communication: problems and potentials of argumentation support systems, Decision Support Systems 26 (4) (1999) 287 – 306.

[35] P. ’t Hart, Preventing groupthink revisited: evaluating and reforming groups in government, Organizational Behavior and Human Decision Processes 73 (1998) 306 – 326.

[36] S.E. Toulmin, The Use of Arguments Cambridge, University Press, Cambridge, 1958.

[37] R. Vahidov, R. Elrod, Incorporating critique and argumentation in DSS, Decision Support Systems 26 (3) (1999) 249– 258.

[38] J.M. van Bruggen, P.A. Kirschner, W. Jochems, External representation of argumentation in CSCL and the manage-

ment of cognitive load, Learning and Instruction 12 (1) (2002) 121–138.

[39] I. Zigurs, B.K. Buckland, A theory of task/technology fit and group support systems effectiveness, MIS Quarterly 22 (3) (1998) 313– 335.

![](/api/attachments/FA8K6YC8/fulltext/images/9e6e0fc345a57efbabb830b6789ba8c5337d61e32c08ab0c84d54c8de0d68e8e.jpg)

Pengzhu Zhang is Chair Professor in MIS and E-Commerce, Director of Center for Management Information Systems, Antai School of Management, Shanghai Jiaotong University. His articles have appeared in Decision Support Systems, Information Systems Engineering and many journals in Chinese. His research interests include group decision/team support systems, financial management information systems, E-government and E-commerce.

Hsinchun Chen (Please refer to another paper in this special issue).

![](/api/attachments/FA8K6YC8/fulltext/images/edfd301f6a5c537b169e9069bb66e27d2b569060f4561b3d8cac361a745dffb8.jpg)

![](/api/attachments/FA8K6YC8/fulltext/images/63e28e0fafb5f73dfe63d31f3b395c174ecd342121697b53381184f1368541f5.jpg)

edge processing in argumentation, and information technology implementation.

Jingle Sun is an Associate Professor of Air Force University of Engineering in the Department of Computer and Management. He is a PhD student in Business School of Xi’an Jiaotong University. His research has appeared in HICSS conference sponsored by IEEE, Journal of system engineering in China and other journals. His current research interests include group decision and group argumentation, information technology architecture, information and knowl-
