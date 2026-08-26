---
otero_id: 24611
otero_key: "629E98QT"
title: "AEROBA: A Blackboard Approach to Model Formulation"
authors: "Ajay S. Vinze; Arun Sen; Shue Feng T. Liou"
year: "1992"
journal: "Journal of Management Information Systems"
doi: "10.1080/07421222.1992.11517970"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# AEROBA: A Blackboard Approach to Model Formulation

Ajay S. Vinze, Arun Sen & Shue Feng T. Liou

To cite this article: Ajay S. Vinze, Arun Sen & Shue Feng T. Liou (1992) AEROBA: A Blackboard Approach to Model Formulation, Journal of Management Information Systems, 9:3, 123-143, DOI: 10.1080/07421222.1992.11517970

To link to this article: http://dx.doi.org/10.1080/07421222.1992.11517970

![](/api/attachments/629E98QT/fulltext/images/136239a5d999f64fa02a53944189e186b2303649620d621cff2b27569595ca12.jpg)

Published online: 16 Dec 2015.

![](/api/attachments/629E98QT/fulltext/images/e28e0d0dc6e6023a1e2373c45ecb8b42e9472815f4aea7a9f8b91e50597e0d8c.jpg)

Submit your article to this journal ↗

![](/api/attachments/629E98QT/fulltext/images/634fc0be4885e16d29c23abf029060fd506d8ef4a9cbc79825a0894069447376.jpg)

View related articles ↗

![](/api/attachments/629E98QT/fulltext/images/2713fb4b2531e2d57d569d18bb80565bf20c5737cec1fede91d01c46495a8472.jpg)

Citing articles: 7 View citing articles ↗

# AEROBA: A Blackboard Approach to Model Formulation

AJAY S. VINZE, ARUN SEN, AND SHUE FENG T. LIOU

AJAY S. VINZE received a B.Comm. degree from the University of Delhi in 1980, and an M.B.A. from the University of Connecticut in 1982. He received his Ph.D. in management information systems from the University of Arizona in 1988. Prior to joining the doctoral program at Arizona he worked in Manila, Philippines, as a computer consultant for two years. Since 1988, he has been an Assistant Professor of MIS in the department of Business Analysis and Research at Texas A&M University. His research interests focus on investigating the use of artificial intelligence techniques in solving business-related problems. Specifically his work has focused on: the blackboard paradigm and its applications; expert systems support for end-user computing; validation and verification of expert systems; intelligent decision support systems and planning systems. His published works have appeared in IEEE Transactions on Systems, Man and Cybernetics, International Journal of Man–Machine Studies, Journal of Management Information Systems, Omega, Information and Management, and International Journal of Expert Systems with Applications. He was invited to be a guest editor for a special issue of the latter journal on the blackboard paradigm and its applications.

ARUN SEN received an M.Tech. degree in electronics in 1971 from Calcutta University, and an M.S. in computer science in 1976 and a Ph.D. in information systems in 1979 from Pennsylvania State University. Since 1986 he has been an Associate Professor in the department of Business Analysis and Research at Texas A&M University. He was previously an Assistant Professor and Associate Professor at the University of South Carolina. His research interests include intelligent decision support systems, object database systems, expert systems, blackboard systems, model formulation support, and distributed networks. He has published numerous papers in Information Systems, IEEE Transactions on Systems, Man and Cybernetics, Journal of Management Information Systems, Omega, Computers and OR, Simulation, MIS Quarterly, Decision Support Systems, International Journal of Man–Machine Studies, and others. He serves on the editorial board of Journal of Database Management and is currently a guest editor, with Ajay Vinze, of the International Journal of Expert Systems with Applications.

SHUE FENG T. LIOU received her M.S. in business computing sciences in 1986 and her Ph.D. in business analysis (MIS) in 1992 from Texas A&M University. She is currently on the faculty of National Chenchi University, Taipei, Taiwan. She has published in IEEE Transactions on Systems, Man and Cybernetics, International

Acknowledgments: An earlier version of this paper was originally published in the Proceedings of the Twenty-Fifth Hawaii International Conference on System Sciences (IEEE Computer Society Press, 1992).

Journal of Man–Machine Studies, and Proceedings of the Hawaii International Conference on Systems Sciences.

ABSTRACT: Building models for problem solving is a common practice for many disciplines. Model formulation is a complex process. Researchers have in the past approached this process from a variety of angles including planning, model structuring, model integration, and model representation, among others. Here we use observations of expert modelers in an attempt to understand the process. The observations, made in the form of protocol analysis, identified three important facets to this process: formulation tasks, control considerations, and the opportunism in the process of formulation. Using these observations, the AEROBA system was constructed, based on the blackboard paradigm. The system design and implementation details are presented. A consultation trace with AEROBA is also provided.

KEY WORDS AND PIIRASES: blackboard systems, decision support, model formulation.

## 1. Introduction

MANY APPLICATIONS IN DIVERSE DISCIPLINES SUCH AS BUSINESS, engineering, and physics make use of models. A model is a structure that has been developed by an expert modeler to study the characteristics of a real-world problem. Among different kinds of models that are being used—schematic, analog, mathematical, and verbal—we concentrate in this research on the mathematical models, and more precisely on the formulation of the mathematical programming models.

Formulation of a model by expert modelers involves capturing the problem descriptions or semantics, understanding the essential elements by studying structure, selecting a suitable tool with its underlying structure, and finally mapping the problem structure onto the tool structure [8]. The process involves three categories of tasks: formulation tasks, or steps in the construction of the model; control tasks to determine what to do next; and formulation process planning tasks, which refers to control-like concerns, only on a longer time horizon. Model formulation can then be thought of as a design activity that is monitored by control and planning processes.

## 2. Research Objective

THE FOCUS OF THIS PAPER IS ON THE THREE ASPECTS OF MODEL FORMULATION in the form of an automated system, AEROBA. As a first step, we report the results of a protocol analysis exercise. This exercise was an attempt to understand formulation by observing expert modelers undertaking the formulation exercises. Using the results from the protocol analysis, we have derived considerations for developing an automated support for this process. In particular, we have documented a set of formulation tasks used by the expert modelers, the control decisions made, and the overall approach to formulation, that is, opportunistic problem solving. The AEROBA system is designed to accommodate these considerations. The paper details the AEROBA system, and provides evidence of formulation tasks, control, and planning activities as model formulation is attempted by AEROBA.

TO STUDY THE MODEL FORMULATION PROCESS, A QUASI-EXPERIMENT was conducted with simple textbook problems. The use of simpler problems allowed us to observe the process of formulation in greater detail and to capture the various nuances of the process. Details of the verbalization and the protocol analysis are included in Vinze et al. [8].

The experiment focused on the think-aloud technique, where the experts are asked to verbalize as they go through their motions of formulating the model. The verbalizations were captured by audiotaping the session. The tape recordings were then transcribed and the transcripts were analyzed using protocol analysis $[3]$ .

The subjects were nine expert modelers—three each from the selected domains: Production Planning, Forecasting, and Auditing. Eight of these experts were professors with varying degrees of experience. One subject in the Auditing domain was a practicing professional. Each subject had a Ph.D. degree in the area of specialization.

Once the transcriptions for the verbalizations were obtained, the verbalizations were mapped to a cognitive model $[7, 8]$ to help analyze the protocols. The cognitive model divides the problem-solving space into five panels (figure 1). The cognitive mappings reveal several interesting angles to the process of formulation. Most importantly, they reveal a similarity in the process of formulation among experts in a problem domain as well as among experts across the selected domains. These can be summarized as follows:

• Use of a generic set of formulation tasks;

\- Opportunistic problem-solving approach to model formulation;

\- Use of a generic set of control considerations in the process of formulation.

On the basis of these findings, the blackboard paradigm was selected for the AEROBA implementation.

## 3.1. The Blackboard Paradigm

The blackboard model, according to Englemore and Morgan [2], is a complex problem-solving paradigm whose characteristics can be best described by contrasting it with more familiar computational models.

In the standard model of computation, a program acts upon a dataset. The program itself consists of a set of procedures and some control mechanism for ordering their applications. The problem-solving knowledge is embedded in the procedures and the control structure. Most programs employing algorithmic methods use this standard model.

A second model of computation is the classical expert system structure. Here we encounter three things: working memory, knowledge base, and inference engine. The input to the system and the results of computations are kept in a working memory. The contents of the working memory are used by the inference engine in conjunction with knowledge in the knowledge base to infer new hypotheses that are again placed in the working memory. The inference engine accesses the working memory (read and write) and the knowledge base (read only) until it detects a termination condition. This model separates the knowledge from the inference engine. The model has two weaknesses: (a) the control of the application of the knowledge is implicit in the structure of the knowledge base, such as in the ordering of rules for a rule-based system; (b) the representation of the knowledge is dependent on the nature of the inference engine (a rule interpreter, for example, can only work with a rule base).

![](/api/attachments/629E98QT/fulltext/images/3d3f8c9b31a5a9a05cec7c1127c07e8a0f4d809479d06f1ed6bd3c6186b11314.jpg)  
Figure 1. The Cognitive Model for AEROBA

The third model of computation is the blackboard model, which seeks to eliminate the inherent weaknesses of the classical expert system structure. The knowledge base is divided into modules (called knowledge sources) and provides a separate inference engine for each module. This eliminates the second problem mentioned above. The communication between the modules is now limited to reading and writing in the working memory. One can also subdivide the working memory (called blackboard) so that it contains regions with differing data structures. The blackboard model of problem solving is a highly structured special case of opportunistic problem solving and is divided into knowledge sources, blackboard data structure, and control.

The domain knowledge needed to solve a problem is partitioned into knowledge sources that are kept separate and independent. The objective of each knowledge source is to contribute information that will lead to a solution to the problem. A knowledge source takes a set of current information on the blackboard and updates it. The knowledge sources are represented as procedures, sets of rules, or logic assertions. Only the knowledge sources modify on the blackboard or control data structures. Each knowledge is responsible for knowing the conditions under which it can contribute to a solution. Each knowledge source has preconditions that indicate the condition on the blackboard that must exist for the knowledge source to get activated. One can view a knowledge source as a large rule. The condition part of this rule is called the knowledge source precondition, and the action part is called the body of the knowledge source.

The problem-solving data are kept in a global data structure, called the blackboard. The purpose of the blackboard is to hold computational and solution-state data needed and produced by the knowledge sources. The knowledge sources use the blackboard data to interact with each other indirectly. The blackboard consists of objects (or solution elements) that can be input data, partial solutions, alternatives, and final solution and, possibly, control data. The objects of the blackboard are hierarchically organized into levels of analysis. The information attached with objects on one level serves as input (stimulus) to a set of knowledge sources, which, in turn, place new information (response) on the same or other levels.

The knowledge sources respond opportunistically to changes on the blackboard. There is a set of control modules that “monitor” the changes on the blackboard and decide what actions to take next. Various kinds of information are made globally available to the control modules. The control information is used by the control modules to determine the focus of attention.

The blackboard paradigm has several implications for the AEROBA implementation. In the following sections we discuss the three critical issues that were highlighted by the protocol analysis, namely, formulation tasks, opportunistic problem solving, and control considerations.

## 3.2. Formulation Tasks

In an attempt to identify the formulation tasks, the process of formulation was defined as a process of creating a model that is efficiently solvable by some mathematical programming solution method. The definition of these tasks used both the protocol analysis and the prior research work in model formulation. Our analysis revealed a collection of tasks, listed and described below, that the expert modelers perform in formulating a model:

Problem Scoping: collect user inputs by parsing the problem definition.

Problem Structuring: (a) classify the input into important phrases, keywords, and data; (b) create an internal model of the problem description using the user input; (c) rewrite the internal model in terms of generic domain objects.

Tool Selection: select an appropriate mathematical representation as a target tool.

Tool Verification: the tool is verified to see if it really fits the problem semantics. Algorithm Selection: an algorithm is selected for the solution of the formulated model. This influences the tool choices.

Tool Validation: the algorithm selected is used to validate the selected tool.

Reformulation: the internal structure of the application problem, its generic form, and the algebra scheme may need to be restructured to simplify.

Tool Structuring: map the generic domain objects to the formal tool semantics to create the instance of the formulated model.

## 3.3. Opportunistic Problem Solving in Model Formulation

Opportunism in the context of model formulation means that during the formulation process the expert's intermediate decisions and observations suggest opportunities for further development of the formulation.

It was observed in the protocol analysis that during the course of the model formulation process, the experts changed their focus of attention to execute alternative formulation tasks. For example, in part of a verbalization, the expert finds that the requirements are food, machinery, consumer durables, and consumer nondurables. He focuses to a more detailed level to assign indices to the product types and the regions. He quickly realizes, however, that he cannot do any formulation at this point as very little is known about the problem. So he goes back to the problem description mode. The extensive use of opportunistic problem solving has been documented separately $[8]$ .

An explanation for opportunism is that expert modelers have chunks of formulation knowledge $[5]$ that they use repeatedly and opportunistically based on different situations in the formulation process. This leads us to the next aspect of the formulation process, control.

## 3.4. Control Considerations

A control decision is defined as the selection and ordering of the sequence of tasks that are needed to execute in order to solve a problem. The control considerations reported here are supported both by the literature on model formulation and are evidenced in the protocols of the expert modelers. In an attempt to understand these features, and verify their use by AEROBA, we define these control considerations:

1. Determining problem boundaries draws the limit of the problem space in which the formulation considerations will be confined. Problem classification is an approximation approach to determine problem boundaries. Determining problem boundaries is a continuous activity if the formulator keeps monitoring the problem scenario during the formulation process.

2. Decomposing the problem divides a complex problem into different components. This feature is recognized when the expert is elaborating on several components of the problem.

3. Setting the goal assigns tentative goals/subgoals to be pursued during the formulation process.

4. Delineating the formulation specifies a course of formulation actions in terms of model components.

5. Changing the formulation switches or modifies the formulation, and includes undoing, switching, and modifying earlier formulation decisions.

6. Focusing on controllable components tentatively concentrates the formulation tasks on a specific target.

7. Predicting potential situations anticipates the dynamically certain factors of the problem environment.

8. Reasoning the formulation infers the intended actions to be taken based on some presupposed justifications.

9. Evaluating the formulation makes a judgment on the formulation tasks undertaken to this point.

## 4. AEROBA—A Blackboard Architecture

THE PROTOCOL ANALYSIS USING THE COGNITIVE MODEL and the resulting findings regarding formulation tasks, control considerations, and opportunism in problem solving form the basis of the AEROBA implementation. AEROBA is implemented in Common lisp on a Sun 3/160 workstation. The implementation is focused on formulating linear programming (LP) models in the production planning domain.

The blackboard paradigm forms the underlying basis of the AEROBA implementation. The primary reason for choosing the blackboard approach was the central role of opportunism in the model formulation process. The blackboard model of problem solving has been used as the approach of choice for opportunistic problem-solving applications such as speech understanding, image understanding, signal interpretation, and some planning and design problems $[2, 6]$ . The blackboard model has been described as analogous to having a group of specialists gathered around a common workspace, with each specialist able to read and write to this workspace. The architecture of the blackboard is usually described as consisting of three major components: blackboard data structure; knowledge sources; and control.

## 4.1. The AEROBA Blackboard Data Structure

The AEROBA system is a three-panel implementation (figure 2). The problem and the solution panel focus on the capturing of the problem semantics and the translation of these problem features into an appropriate tool or solution technique structure such as linear programming. Given the two different aims for these panels, and the need to translate entries on the problem panel to corresponding entries on the solution panel prompted the choice of identical data structures to represent both the panels. The design of both the problem and solution panel and the associated entries on them follow the Extended Entity Relationship (EER) data model. Since model formulation in the context of AEROBA is an opportunistic translation of the entries on the problem panel to representations on the solution panel, it was decided that a common data model—EER—should be used to represent the semantics of the cognitive model's problem and solution panels.

Using the structured modeling approach [4], we have extended the entity relationship (ER) model designed by Chen [1]. The detailed definitions for this model are presented separately [7]. EER defines the levels of the AEROBA problem and solution panels (figure 2). In addition, the EER also helps define the solution element frame (figures 3 and 4). The basic structure of such a frame is shown in Table 1.

Following the BB1 approach [5], the AEROBA implementation collapses the three aspects of control (global design, control, and specific design) of the cognitive model (figure 1) into a control panel (figure 2).

## Problem Panel

The problem panel consists of five levels: P-Basic, P-Domain, P-Entity, P-Relationship, and P-Attribute. The P-Basic level stores information provided by the user. The P-Domain level indicates the domain of choice at the present time; this is set to Production Planning. The remaining three levels of the problem panel correspond to an EER structure used to view the problem situation $[7]$ , namely the entities involved the associated relationships and the defining attributes.

## Solution Panel

The solution panel focuses on the model being formulated. In the present implementation of AEROBA, this is Linear Programming. The levels in the solution panel have a one-to-one correspondence to the levels in the problem panel with one exception. The basic level in the problem panel does not need a corresponding level on the solution panel as the solution panel does not record user responses.

## Control Panel

The third panel, discussed in more detail under control, represents the control decisions. It is the control panel that monitors the process of formulation in AEROBA and ensures the opportunism in the process. Opportunism in the AEROBA context is translated as the ability for the different knowledge sources to contribute based on the available opportunity and the importance of such a contribution.

![](/api/attachments/629E98QT/fulltext/images/ceea98a26921267fce1a37e3f267244e0036060907d31683decdb4bf2ec7faba.jpg)  
Figure 2. The AEROBA Architecture

## 4.2. AEROBA Knowledge Sources

Knowledge sources are the formulation specialist that have been shown on the cognitive model (figure 1). The knowledge sources are the codification of the formulation tasks, and the appropriate partitioning of the same. Table 2 illustrates the translation of the formulation specialists to knowledge sources, and the functions performed by these knowledge sources.

Table 1 Basic Structure of Solution Element

<table><tr><td>Slot-name</td><td>Slot-definition</td></tr><tr><td>SE-NAME</td><td>ID number of the solution element</td></tr><tr><td>TYPE</td><td>Type of solution element (Entity or Relationship)</td></tr><tr><td>OWNER</td><td>Owner of the solution element (Entity or Relationship)</td></tr><tr><td>CONSTRAINT</td><td>Constraint type (shown on the edges of the EER diagram)</td></tr></table>

## 4.3. AEROBA Control

The control panel (figure 2) introduces domain-independent control component to AEROBA. With the introduction of the control panel, the tactical control strategies are introduced, while the overall opportunistic behavior of the system is maintained.

The control panel in AEROBA consists of seven levels: General Approach, Strategy, Policy, Focus, Trigger-Record, Chosen-Record, Event. The level definitions are based on the control process observed in the verbalizations by expert modelers.

At the General Approach level, decisions are made on whether the current problem is analogous to a problem previously attempted. In the current implementation, prior situations of solving similar problems are not retained in the memory, so each problem attempted by AEROBA is treated as a new problem. The approach to formulation is, therefore, based on “first principles.” The inclusion of this level in the current implementation was, however, based on some observations from the protocols that indicated situations where modelers equate the present problem to a prior experience, and attempt formulation using a case-based approach. Incorporation of the case-based approach to model formulation is seen as a future extension to AEROBA.

The next level of the control panel, Strategy, is based on the control considerations identified in the earlier section. The system at this level decides between problem boundary determination, problem decomposition, formulation goal setting, formulation planning, formulation replanning, formulation control focusing, and formulation component postulating. Formulation knowledge sources have been classified using these control strategies. A collection of these strategies dynamically control the first-principle formulation of the AEROBA. Each tactical knowledge source corresponds to a set of knowledge sources. For example, problem boundary determination has as its corresponding domain knowledge sources KS01 and KS02 (see Table 2 for description).

The Policy level on the control panel integrates ideas of meta-control. In particular, decisions at this level focus on “general-policy,” “reasoning-policy,” “knowledge-source-policy,” and “rule-policy.” These policies are general governing principles for formulation using the blackboard paradigm. For example, the general-policy presently is set that a rule may not have multiple firings, that is, if a rule is used at any time during the execution cycle, it is then flagged out of future contention. The reasoning-policy can be forward chaining or backward chaining.

Table 2 A Partial List of Knowledge Sources

<table><tr><td>KS-Num</td><td>KS-Name</td><td>Specialists from cognitive model</td><td>Stimulus level</td><td>Response level</td><td>Actions</td></tr><tr><td>KS01</td><td>set-problem-domain</td><td>domain-identifier</td><td>p-basic</td><td>p-domain</td><td>start the problem panel</td></tr><tr><td>KS03</td><td>create-problem-entity-type</td><td>context-analyzer</td><td>p-basic</td><td>p-entity</td><td>creates entity types</td></tr><tr><td>KS11</td><td>map-solution-key-attr</td><td>model specifier model specification setter</td><td>p-attribute</td><td>s-attribute</td><td>map key attributes to the solution panel</td></tr><tr><td>KS21</td><td>create-solution-entity-type</td><td>tool type specifier model specification inferer</td><td>s-domain</td><td>s-entity</td><td>creates entity types</td></tr></table>

The Focus level on the control panel indicates the set of knowledge sources that have been identified as potential contributors to the formulation process at the present time. The focus of the formulation is directed by the tactical control decisions at the strategy level. The Trigger-Record decisions identify all pending knowledge sources, while the Chosen-Record level stores the decisions that identify the knowledge source being scheduled for execution.

Like all blackboard implementations, the knowledge source activity in AEROBA architecture is event-driven. Each change in the blackboard domain panels constitutes an event that in the presence of other information on the blackboard can trigger (satisfy the condition of) one or more knowledge sources. The blackboard events in AEROBA can be of many types. They include: problem entity construction, problem relationship construction, problem attribute construction, problem attribute modification, solution entity construction, and others. The AEROBA architecture considers events as interrupts that need to be interpreted at the control level. This is achieved by adding a level in the control panel called Event below the Chosen-Record level. As an example of how events are handled, let us consider a situation where the formulation cannot proceed without the user providing some data input to the formulation. Such an event would cause the system to suspend normal formulation tactics, which could be a “decomposition” at that time, and initiate data-gathering activities.

## 4.4. The Inference Loop in AEROBA

The inference loop, responsible for any consultation session with AEROBA, is an iterative process. The major theme of the inference loop is deciding “What to do next?”—that is, the inference loop has the task of gathering a set of knowledge sources that may contribute at any given time, and deciding which of these makes the best contribution to the situation at hand. Furthermore, the inference loop also needs to decide which rule to activate from the selected knowledge source. The algorithm for the inference loop is shown below:

ALGORITHM: INFERENCE LOOP

Step-1: Initialize
    get problem domain from user;
    set tool domain to LP;
    set Problem-Solving-Approach to First-Principles;
    execute CKS01-DESIGN (approach) to initialize strategy-list;
    execute CKS02-MAKE-POLICY (approach) to set initial policies;
    execute CKS03-ELABORATE-DESIGN (strategy-list) to set the first focus;

## Step-2: For each Current Focus

do KS-loop for triggered KSs until a KS makes contribution or no KS left;
execute CKS04-INITIATE-TR (focus, reasoning-policy);
execute CKS05-SCHEDULE-KS (trigger-KSs, KS-policy);

do RULE-loop for triggered RULEs until a rule makes contribution or no rule left;
execute CKS06-ELABORATE-TR (current-KS, reasoning-policy);
execute CKS07-SCHEDULE-RULE (trigger-rules, rule-policy);
execute CKS08-EXECUTE-CR (selected-rule, current-se);

end RULE-loop;

if a KS makes contribution,
execute CKS09-MONITOR-POLICY-FOCUS (event-list);
execute CKS10-MONITOR-DESIGN (event-list);
execute REMOVE-TERMINATED-FOCUS;
execute REMOVE-TERMINATED-EVENT;

if no KS in the current focus makes contribution, do one of the following
a. if all the solution attributes are instantiated and the event-list is empty, the formulation is complete; Stop.
b. if the current focus is opportunistic, recover the interrupted focus and reasoning-policy;
c. if no focus has been resumed, resume the suspended focus

pointed by the round-robin mechanism. The reasoning-policy for the resumed focus is always planning;

d. if the current focus is a resumed one and strategy-list has not been exhausted, execute CKS03-ELABORATE-DESIGN to bring in a new strategic focus;

e. if it is none of the above:
    /\* to see if they can generate new opportunities \*/
    execute CKS09-MONITOR-POLICY-FOCUS;
    execute CKS10-MONITOR-DESIGN;

end KS-loop;

## 4.5. A Formulation Session with AEROBA: A Sample Procurement Problem

American Hospital Inc. has two sites that require display terminals. The demands for the terminals are: 70 units at site D1, and 40 units at site D2. The terminals can be supplied from a nearby store chain called Computer-Display at a lower shipping cost. They can also be supplied from the store's out-of-town branch at a higher shipping cost. Each store has some terminals in stock and can buy more if needed. Due to working-capital constraints, Computer-Display and the store's out-of-town branch are limited to the number of units that they can purchase. The prices, stocks, and the maximum amounts that can be purchased at stores are as follows:

<table><tr><td>Supply</td><td>Purchase price</td><td>Stock purchase limit</td></tr><tr><td>S1 $400</td><td>50</td><td>300</td></tr><tr><td>S2 $350</td><td>20</td><td>200</td></tr></table>

A budget of \$15,000 is available to the store to buy the extra terminals. The costs of shipping the terminals from stores to the hospitals are:

<table><tr><td>Shipping route</td><td>Shipping cost</td></tr><tr><td>S1-D1</td><td>$20</td></tr><tr><td>S1-D2</td><td>$25</td></tr><tr><td>S2-D1</td><td>$50</td></tr><tr><td>S2-D2</td><td>$55</td></tr></table>

The objective is to determine how many terminals are to be purchased and how to ship them to the hospitals so that the total cost is minimized.

The session shows the questions asked by the system as “AEROBA>” prompt. The system asks for the user’s input by displaying the “USER-RESPONSE>” prompt.

The explanation messages and the other prompts by the system, including the final outcome of the formulation, are shown in italics.

(load "aeroba.mf")

At this point AEROBA loads the model formulation module and is ready for execution.

## (initialize)

AEROBA> Problem domain of interest (ProdPlan Auditing Forecasting)?

Notice that the current version only addresses production planning problems.

## USER-RESPONSE> ProdPlan

AEROBA> OK, the initialization is set up.

Please type (solve) to proceed the formulation.

During the initialization stage, the system sets the solution domain as “linear programming” and the general problem-solving approach as “first principles.” Formulating model by first principles, AEROBA establishes an initial strategic plan and a set of initial policies to guide the overall formulation process. The strategic plan and policies are subject to change due to the dynamic formulation situations. By first principles, the strategic plan consists of a group of design decisions: Classifying-the-Problem, Decomposing-the-Problem, Setting-the-Goal, Delin-eating-the-Formulation, and Elicit-Problem-Semantics. The last step of the initialization is to elaborate the first design decision Classifying-the-Problem as a strategic focus composed of several domain KSs.

## USER-RESPONSE> (solve)

AEROBA> Is it a Product Transformation (PT) OR Resource Allocation (RA) problem?

## USER-RESPONSE>PT

AEROBA> What describes transformation in your problem (Place, Time, Form)?

## USER-RESPONSE> Place

AEROBA> Is yours a single product situation (Yes No)?

## USER-RESPONSE> Yes

Under the strategic focus elaborating Classifying-the-Problem, AEROBA traces the problem type discrimination tree and selects the problem type as single product transportation problem (SPTP). When the strategic focus is shifted to those elaborating Decomposing-the-Problem, Setting-the-Goa!, and Delineating-the-Formulation, AEROBA will start building the standard EERD for this problem type and the tool EERD for LP. Once a problem type is identified, the strategic focus elaborating Classifying-the-Problem is expired and will no longer be resumed as the focus of attention.

AEROBA> Please enter data for SL.NAME (separated by a space)

USER-RESPONSE>S1 S2

AEROBA> Please enter data for DL.NAME (separated by a space)

USER-RESPONSE>D1 D2

So far, AEROBA has elaborated the design Delineating-the-Formulation and partially constructed EER attributes for the problem. When a key attribute or data attribute is attached to an entity or relationship type, a formulation event is also created. This event induces the interrupt of the current focus and causes the attention of an opportunistic focus responsible for collecting data from the user.

AEROBA> Please enter data for DL.REQ D1

USER-RESPONSE>70

AEROBA> Please enter data for DL.REQ D2

USER-RESPONSE>40

AEROBA> Please enter data for SL.CAP S1

USER-RESPONSE>

AEROBA> Please enter data for SL.CAP S2

## USER-RESPONSE>

The above two questions are asked because the standard EERD for SPTP includes a data attribute SL.CAP. However, this problem is not a standard SPTP and has no supply capacity data. The user just enters <RTN> when the question is not applicable to the problem. The attribute type of SL.CAP will be modified once the system recognizes the problem as a variation of SPTP.

AEROBA> State an alternate objective (Profit-Max Time-Min Neither)

## USER-RESPONSE> Neither

AEROBA traces the problem elicitation tree and asks for further features about this problem. This is processed when the strategic focus elaborating the design decision Elicit-Problem-Semantics gets attention.

AEROBA> Please enter data for SH.COST (S1 D1)

USER-RESPONSE>20

AEROBA> Please enter data for SH.COST (S1 D2)

USER-RESPONSE> 25

AEROBA> Please enter data for SH.COST (S2 D1)

USER-RESPONSE> 50

Figure 3. The State of the Blackboard (Cycle 14)

<table><tr><td rowspan="7">P-Attribute</td><td rowspan="7">ky</td><td rowspan="7">da</td><td>sh name</td><td>sh cost</td><td>sh qty</td><td>sh tot cost</td><td>di name</td><td>di req</td><td>di tot sh qty</td></tr><tr><td>dk</td><td>da</td><td>ac</td><td>dc</td><td>ky</td><td>da</td><td>dr</td></tr><tr><td colspan="7">SHIP</td></tr><tr><td colspan="7">DEMAND-LOCATION</td></tr><tr><td colspan="7">Supply-LOCATION</td></tr><tr><td colspan="7">Prod-Plan</td></tr><tr><td colspan="7">(P-Domain:ProdPlan) (S-Domain:Linear-Programming) (Problem:SPTP)</td></tr><tr><td>P-Entity</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>P-Domain</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>P-Basic</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

AEROBA> Please enter data for SH.COST (S2 D2)

USER-RESPONSE> 55

When the strategic focus elaborating Delineating-the-Formulation is resumed, more formulation events are created to cause the interrupt of the current focus. The opportunistic focus responsible for collecting data then gets attention again.

AEROBA> Are there additional activities in the problem (Procurement Supply-Location-Selection Route-Selection None)?

USER-RESPONSE> Procurement

Again, AEROBA traces the problem elicitation tree and asks further features about this problem because the strategic focus elaborating Elicit-Problem-Semantics is resumed. The new problem feature (activity procurement) will induce the appending of a new design decision Changing-the-Formulation to the strategic plan. This new design decision will then cause another strategic focus under which the problem EERD will be modified to include more attributes.

AEROBA> Please enter data for SL.STOCK S1

USER-RESPONSE> 50

AEROBA> Please enter data for SL.STOCK S2

USER-RESPONSE>20

Again, new formulation events cause the switch of the focus of attention to an opportunistic focus for collecting data.

AEROBA> Please enter data for SL.PUR.COST S1

USER-RESPONSE> 400

AEROBA> Please enter data for SL.PUR.COST S2

USER-RESPONSE> 350

The attribute SL.PUR.COST is also added because of the problem feature (activity procurement). This is another data attribute that causes the data collection activity.

Notice that the attribute SL.CAP has been modified to derived attribute. Because of the purchasing activity involved at the supply location, the supply capacity becomes the summation of the existing stock and additional purchasing quantity. Also notice that the updated problem attributes are only partially mapped into the Solution panel.

AEROBA> Are there constraints on shipping quantities (Integer Capacitated Neither)?

USER-RESPONSE> Integer

This new problem feature (sh.qty-constraint integer) will cause the system to attach integer constraint to the values of attribute SH.QTY later in the formulation process.

AEROBA> Are there constraints on the quantities being purchased Please select answer(s) from the list (separated by a space) (Integer Capacitated Neither)?

USER-RESPONSE> Integer Capacitated

This new problem feature (sl.pur.qty-constraint integer capacitated) will induce AEROBA to set integer constraint and collect capacity data for attribute SL.PUR.QTY later in the formulation process.

AEROBA> Please enter capacity for SL.PUR.QTY S1

USER-RESPONSE> 300

AEROBA> Please enter capacity for SL.PUR.QTY S2

USER-RESPONSE> 200

AEROBA> Are there any budget constraints in the problem (Yes No)?

USER-RESPONSE> Yes

Here is another problem feature inquired for SPTP. This new problem feature will cause another addition of EERD attributes and further data collection if necessary.

AEROBA> Please enter data for SL.TOT.BUDGET

USER-RESPONSE> 15000

AEROBA> Please enter the relationship between SL.TOT.COST and 15000 (LE GE EQ)

USER-RESPONSE> LE

AEROBA> formulation completed ...
Please type (algebra) to show the formulation outcome in algebra format.
real-time = 132080 (132.080 seconds)
run-time = 17760 (17.760 seconds)

Along the way of structure building, problem elicitation, and data collection, AEROBA also derives attribute data and maps related problem data into the LP EERD structure in the Solution panel. The formulation is completed when all design decisions are elaborated, all events are terminated, and finally all of LP EERD attributes are instantiated. The final solution panel state is shown in Figure 5.

USER-RESPONSE> (algebra)

Objective Function is:

Minimize Total Cost =

20\*(SH.QTY S1 D1) + 25\*(SH.QTY S1 D2) + 50\*(SH.QTY S2 D1) + 55\*(SH.QTY

S-Attribute S-Relationship S-Entity S-Domain

![](/api/attachments/629E98QT/fulltext/images/9b2498d3fd643f76f33227d9e1b19ac7fe32c76d636174cdc8745121ad9fa0dc.jpg)  
Problem Panel

![](/api/attachments/629E98QT/fulltext/images/3ded23200c21e2667e32bf98b18afd17f48f9c33c006847f42a07279bd477450.jpg)  
Figure 4. The State of the Blackboard after Initial Data Input from the User (Cycle 38)  
Solution Panel

<table><tr><td rowspan="3"></td><td colspan="101">value = all-der-assoc = (S1 (((SL PUR QTY S1) 1) ((SH.QTY S1 D1) 1) ((SH.QTY S1 D2) 1)) S2) (((SL PUR QTY S2) 1) ((SH.QTY S2 D1) 1) ((SH.QTY S2 D2) 1))</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td rowspan="2">P-Attribute</td><td rowspan="2">s1 name</td><td rowspan="2">sl cap</td><td rowspan="2">dr</td><td rowspan="2">l</td><td rowspan="2">&lt;sl pur qty, sl stock&gt;</td><td rowspan="2">c</td><td rowspan="2">&lt;eg, sl tot sh qty&gt;</td><td rowspan="2">l</td><td rowspan="2">&lt;sh qty&gt;</td><td rowspan="2">sl stock</td><td rowspan="2">da</td><td rowspan="2">sl pur cost</td><td rowspan="2">ac</td><td rowspan="2">sl pur qty</td><td rowspan="2">sl tot budget</td><td rowspan="2">cl</td><td rowspan="2">sl tot cost</td><td rowspan="2">dc</td><td rowspan="2">sh name</td><td rowspan="2">dk</td><td rowspan="2">sh cost</td><td rowspan="2">da</td><td rowspan="2">ac</td><td rowspan="2">sh cost</td><td rowspan="2">sh qty</td><td rowspan="2">sh tot cost</td><td rowspan="2">dc</td><td rowspan="2">sh name</td><td rowspan="2">dy</td><td rowspan="2">dy</td><td rowspan="2">dy</td><td rowspan="2">dy</td><td rowspan="2">dy</td><td rowspan="2">dy</td><td rowspan="2">dy</td><td rowspan="2">dy</td><td rowspan="2">dy</td><td rowspan="2">dy</td><td rowspan="2">dy</td><td rowspan="2">dy</td><td rowspan="2">dy</td><td rowspan="2">dy</td><td rowspan="2">dy</td><td rowspan="2">dy</td><td rowspan="2">dy</td><td rowspan="2">dy</td><td rowspan="2">dy</td><td rowspan="2">dy</td><td rowspan="2">dy</td><td rowspan="2">dy</td><td rowspan="2">dy</td><td rowspan="2">dy</td><td rowspan="2">dy</td><td rowspan="2">dy</td><td rowspan="2">dy</td><td rowspan="2">dy</td><td rowspan="2">dy</td><td rowspan="2">dy</td><td rowspan="2">dy</td><td rowspan="2">dy</td><td rowspan="2">dy</td><td rowspan="2">dy</td><td rowspan="2">dy</td><td rowspan="2">dy</td><td rowspan="2">dy</td><td rowspan="2">dy</td><td rowspan="2">dy</td><td rowspan="2">dy</td><td rowspan="2">dy</td><td rowspan="2">dy</td><td rowspan="2">dy</td><td rowspan="2">dy</td><td rowspan="2">dy</td><td rowspan="2">dy</td><td rowspan="2">dy</td><td rowspan="2">dy</td><td rowspan="2">dy</td><td rowspan="2">dy</td><td rowspan="2">drl</td><td rowspan="2">dy</td><td rowspan="2">dy</td><td rowspan="2">dy</td><td rowspan="2">dy</td><td rowspan="2">dy</td><td rowspan="2">dy</td><td rowspan="2">dy</td><td rowspan="2">dy</td><td rowspan="2">dy</td><td rowspan="2">dy</td><td rowspan="2">dy</td><td rowspan="2">dy</td><td rowspan="2">dy</td><td rowspan="2">dy</td><td rowspan="2">dy</td><td rowspan="2">dy</td><td rowspan="2">dy</td><td rowspan="2">dy</td><td rowspan="2">dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>du</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>DY</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>y</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dx</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dyn</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dry</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>day</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>ds</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dst</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>yst</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dt</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>dy</td><td>DT</td><td>(=70)</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

S2 D2) + 400\*(SL.PUR.QTY S1) + 350\*(SL.PUR.QTY S2)
Subjected to:
1\*(SH.QTY S1 D1) + 1\*(SH.QTY S2 D1) = 70
1\*(SH.QTY S1 D2) + 1\*(SH.QTY S2 D2) = 40
1\*(SH.QTY S1 D1) + 1\*(SH.QTY S1 D2) + -1\*(SL.PUR.QTY S1) = 50
1\*(SH.QTY S2 D1) + 1\*(SH.QTY S2 D2) + -1\*(SL.PUR.QTY S2) = 20
400\*(SL.PUR.QTY S1) + 350\*(SL.PUR.QTY S2) <= 15000
(SH.QTY S1 D1): integer, (SH.QTY S1 D2): integer, (SH.QTY S2 D1): integer,
(SH.QTY S2 D2): integer, (SL.PUR.QTY S1): integer, (SL.PUR.QTY S1) <= 300,
(SL.PUR.QTY S2): integer, (SL.PUR.QTY S2) <= 200

## 5. Conclusions

MODEL FORMULATION IS A VERY KNOWLEDGE-INTENSIVE TASK. This paper focuses on the understanding of the process of model formulation, in particular the aspects of formulation tasks, control considerations, and opportunism in the process. Using the protocol analysis, components and concerns for each of these facets were highlighted. Subsequently, the protocol analysis provided the necessary input for constructing an automated support system for model formulation. The implementation of the AER-OBA system illustrates the utility of the blackboard paradigm to support the process of model formulation.

The AEROBA system simulates the human expert's behavior in using similar control features to direct the formulation progress. With the computer simulation of the control features, the relationship between the control and domain behavior is further clarified. At the same time, the values of some control decisions can be changed to reflect experts' cognitive propensities. In terms of overall contribution from system building effort, we have come one step forward toward realization of the idea of supporting the human modeling process.

## REFERENCES

1. Chen, P.P. The entity-relationship model: toward a unified view of data. ACM Transactions on Database Systems, 1 (1976), 9–36.

2. Engelmore, R., and Morgan, T. (eds.) Blackboard Systems. New York: Addison-Wesley, 1988.

3. Ericsson, K.A., and Simon, H.A. Protocol Analysis: Verbal Reports as Data. Cambridge, MA: MIT Press, 1984.

4. Geoffrion, A. M. An introduction to structured modeling. Management Science, 33, 5 (1987), 547–589.

5. Hayes-Roth, B., and Hayes-Roth, F. A cognitive model of planning. Cognitive Science, 3 (1979), 275–310.

6. Nii, H.P. Blackboard systems: blackboard application systems, blackboard systems from a knowledge engineering perspective. AI Magazine (August 1986), 82–106.

7. Sen, A.; Vinze, A.; and Liou, S.T. Construction of a model formulation consultant: the AEROBA experience. IEEE Transactions on Systems, Man and Cybernetics, 22, 5 (September/October 1992), in press.

8. Vinze, A.S.; Sen, A.; and Liou, S.T. Operationalizing the opportunistic behavior in model formulation. International Journal of Man–Machine Studies, 31 (1992), in press.
