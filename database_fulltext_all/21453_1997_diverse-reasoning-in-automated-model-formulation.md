---
otero_id: 21453
otero_key: "WGMU6KH4"
title: "Diverse reasoning in automated model formulation"
authors: "Shu-Feng Tseng"
year: "1997"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(97)00013-4"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Diverse reasoning in automated model formulation

Shu-Feng Tseng \*

Department of Management Information Systems, National Chengchi University, Wenshan, Taipei, Taiwan

Received 1 June 1996; accepted 1 February 1997

## Abstract

Diverse reasoning supports a dynamic integration of various reasoning methods in a computerized system. This paper describes a control blackboard approach to simulate the control features observed in the expert's model formulation protocols. The diverse reasoning concept is incorporated so that the model formulation process is dynamically in a plan-directed, action-directed, or data-directed fashion. The diverse reasoning concept facilitates the control features simulation. By analyzing the diverse reasoning behavior in the proposed system, this paper contributes to a better understanding of and support to the modeling process for the design of intelligent decision support systems. The usefulness of the prototype system is also evaluated using an empirical experiment. © 1997 Elsevier Science B.V.

Keywords: Intelligent decision support systems; Model formulation; Blackboard systems

## 1. Introduction

Traditional decision support systems (DSS) rely on the expert's understanding of the problem and his or her strategy to construct a model that can be executed by a DSS software. There is a growing recognition that unless the DSS is extended with inference mechanism that explicitly incorporates the intelligent components of the expert's model formulation process, its functionality as the decision aid will be limited [1].

Model formulation is basically a design activity that involves the assembling of selected components using a specific format. During the design process, designers post various tasks to be performed and produce descriptions of actions capable of achieving these tasks [2]. Model formulation has been considered to be an art because it highly depends upon the modeler's cognitive process and modeling style [3]. In the modeling process, the control aspect is important because the control of adapting problem-solving behavior to the domain environment is fundamental to all cognitive processes and is the essence of human intelligence [4].

Despite the importance of the control aspect, previous research attempting to automate the process of model formulation does not address the control issues. Several Artificial Intelligence (AI) techniques have been used to support the automated model formulation $[5–11]$ . These AI techniques, however, use predefined control strategies selected by the developers. A predefined control strategy does not provide enough power since experts typically do not follow a fixed strategy for problem-solving $[12]$ and frequently switch their attention during the model formulation process [3]. These systems are not developed based on the cognitive behavior observed from the human expert's model formulation process. The selection of control strategies seems to be ad hoc and lacks a sound basis. Some model formulation systems are designed based on the expert's modeling process [13,14]. However, the developers interpret the process considering the domain aspect and ignore the important control aspect. Therefore, the flexibility in supporting the modeling process remains an open question.

To address the control problem in the expert's cognitive problem-solving process, a diverse reasoning concept is proposed by Johnson and Hayes-Roth [15]. Diverse reasoning supports a dynamic integration of different reasoning methods in a computerized system. The system can therefore operate in various fashions, such as plan-directed, goal-directed, data-directed, or action-directed, depending on the dynamic problem-solving situations.

Using the diverse reasoning concept, this paper proposes an automated model formulation approach to simulate the control behavior observed in the expert's model formulation process.

## 2. Automated model formulation

Model formulation is regarded as the construction of the selected elements and their relationships to each other based on the understanding of the problem description provided by the user. Model formulation is a complex process that requires the model builder to have a good knowledge of the related discipline. The knowledge of human modelers typically combines control knowledge with domain knowledge to make professional judgements during the formulation process $[16]$ . To facilitate the automated model formulation, various AI techniques have been used to separate control knowledge from domain knowledge. Control knowledge represents the inference engine that monitors and directs domain knowledge to perform the formulation tasks. Several approaches with predefined control strategies have been applied to model formulation. They include pattern matching, request resolution, searching and hierarchical planning.

In the pattern matching approach, the problem description is matched against the knowledge base to identify the problem type or model type. The model is formulated by instantiating the existing problem template or model template. In some studies, the problem semantics and model semantics are considered separately $[17,18]$ . In other studies, the situation is either that the model semantics are embedded in the problem representation or the problem semantics are embedded in the model representation $[6,19,11]$ . In all of these situations, the concepts of problem/subproblems types/templates and model types/templates are overlapped, and the pattern matching approach represents a data-directed approach using various problem descriptions to match against the predefined problem or model types. While it does not generate tentative hypotheses, the reasoning is based on problem data instead of formulation goals.

In the request resolution approach, modeling knowledge is expressed by the extended predicate calculus. The model formulation is initiated by a user request and the resolution refutation mechanism makes use of the axiom set in response to the user's request. The explicit resolution is used until a resolvent is obtained that cannot be further unified with any predicate in the axiom set. During the explicit resolution process, the virtual resolution is performed in the guise of data retrieval or module execution. In this way, building a model is interpreted as formulating a solution path by integrating several prestored data and predefined component modules $[7,20]$ . Because the formulation process is initiated by a user request, model formulation using this approach represents a goal-directed approach. This is different from the data-directed pattern matching approach that is initiated by problem descriptions, although the similar resolution refutation technique implemented in Prolog can be applied in either case.

In the searching approach, model formulation is described as searching through a number of possible relationships to find a route that connects the initial state of a problem to the desired final state. When using this approach, models in the model base are represented by two basic elements: nodes and edges. The nodes store data and the edges denote modules connecting the data [9]. The nodes can also store modules and the edges denote related input and output data. The model is then formulated by creating a directed graph and selecting a path on the graph [21]. This directed graph represents all possible alternatives for solving the problem and each path in the graph represents a potential model. Searching can be data-directed if it starts from the problem descriptions. In some studies of managerial model formulation [21,9], searching is used in a goal-directed fashion. However, it differs from the request resolution approach because, in the process of connecting the expressed axiom components, the searching approach, based on the domain-specific connection, strives to determine the profitable inferences and avoid the combinatorial explosion of resolvents [21].

The hierarchical planning approach is based on the assumption that all problems can be represented with different levels of abstraction. The formulation process is achieved by decomposing the problem along the abstraction hierarchy, constructing simple models from the bottom levels, and then synthesizing the solution constructed from lower levels $[22,10,14]$ . Since the hierarchical planning approach sketches a generic sequence of actions to be considered at the beginning of the process, the nature of control is plan-oriented.

Among these approaches in automating model formulation, the pattern matching approach is basically a classification-oriented approach and is considered to be insufficient due to the richness of modeling activity. Since activities involved in model formulation are evolutionary or incremental in nature, a synthesis-oriented approach better fits this challenging task $[23]$ . Searching and request resolution approaches can be synthesis-oriented, but they are nonhierarchical. They do not distinguish between high-level actions and low-level details in the problem-solving process. Since model formulation is an unstructured and complex task, organizing modeling expertise in abstraction levels is considered to be desirable and the hierarchical planning is therefore a better approach $[22,18,14]$ . Nevertheless, this approach is still a predefined control strategy used to direct and monitor the inference of the domain knowledge. The issues of flexible control are not emphasized. Some of the earlier studies do consider versatile control issues, such as model decomposition and integration, forward and backward reasoning, incompleteness identification, and correctness evaluation as the important model formulation concerns $[1,8,24]$ . But they do not propose a system architecture addressing the control issues.

## 3. Expert's model formulation process

To understand the expert's model formulation behavior, a total of 27 verbalizations (three experts working with three problems in each of the three domains: production planning, forecasting and auditing) were obtained and transcribed into protocols. The details of the protocol analysis are described in Vinze et al. [25] and Sen et al. [26]. The findings are summarized as follows.

## 3.1. Opportunism

Two phases of analysis were conducted for the protocols. The first focuses more on observations of outcomes of the expert's formulation control. The analysis reflects the opportunism exhibited in the process of model formulation. In other words, the expert's formulation decisions are generated almost arbitrarily depending on various opportunities during the formulation development [27]. The somewhat chaotic situations observed in the first analysis lead to a further analysis of the control aspect in the model formulation process.

## 3.2. Control features

The insight of the control aspect in the opportunism was investigated in the second analysis. A set of control features were identified in the protocols. These control features are suggested by managerial problem-solving literature $[28–32]$ . The roles of these control features in directing the expert's formulation behavior are summarized below.

Determining problem boundaries involves drawing the limit of the problem space in which the formulation considerations will be confined. It is identified by an explicit categorization of problem descriptions into some problem type, as well as a continuous clarification of the problem scenario during the formulation process.

Decomposing the problem involves dividing a complex problem into various components. It is recognized while the expert is elaborating on several components of the problem to be considered for the formulation.

Setting the goal involves assigning tentative goals and subgoals to be pursued during the formulation process. It can be identified in the protocols by some goal-related keywords such as ‘purpose’, ‘objective’, ‘looking for…’, ‘in order to…’, and so on.

Delineating the formulation involves specifying a course of formulation actions that construct the model components, such as variables, subscripts, expressions, and so on.

Changing the formulation involves switching or modifying the interim formulation results. It includes undoing, switching, and modifying an earlier formulation decision, as well as suspending the current formulation decision and resuming the suspended one.

Focusing on controllable components involves concentrating the formulation effort on a specific aspect of the problem or a tentative goal.

Predicting potential situations involves speculating the dynamic circumstances of related factors in the formulation scenario. In the protocols, it is recognized while the expert is imagining or making an assumption based on his or her understanding of the problem.

Reasoning the formulation involves inferring the actions to be taken based on the formulator's justifications. In the protocols, it is identified while the formulation actions are associated with key phrases like ‘if… then…’, ‘because of’, ‘the reason for…’, an so on.

Evaluating the formulation involves making a judgement of the successfulness of the past or the perspective formulation actions. It implies a dynamic evaluation view adopted by the expert in the formulation process. For example, in the protocols, while the expert checks whether the formulation includes enough variables for the problem, it is identified as evaluating the formulation.

## 4. Control approaches in blackboard systems

Since the first protocol analysis suggests an opportunistic paradigm for the system design, the blackboard approach is adopted for implementation. A blackboard architecture generally consists of three major components: knowledge sources, blackboard data structure, and control. The blackboard is a global data structure organized into levels to hold various problem-solving data, called solution elements. Knowledge sources (KS) are separate chunks of domain knowledge that read the solution elements on one blackboard level, called the stimulus-level, and update the solution elements on another blackboard level, called the response-level. The KS use the blackboard data for interacting with each other indirectly. The control module monitors the blackboard and determines the current focus of attention so that the knowledge sources will respond opportunistically to changes on the blackboard [33]. Depending on the focus of attention, the control module schedules a knowledge source to execute and consequently change the blackboard state.

Several approaches have been adopted for the control in blackboard systems. The Sophisticated Scheduling [4] employs all of a system's control knowledge in one complex program module. The measures associated with each KS invocation are recalculated dynamically as the blackboard state changes. This approach is adopted in the first blackboard system HEARSAY-II [34]. The Solution-Based Focusing [4] also relies upon one complex program module that embodies all of a system's control knowledge. However, the solution-based focusing does not identify or select among pending knowledge sources. Instead, it selects specific blackboard events and executes knowledge sources triggered by each one [35]. The Hierarchical Control Approach [36] organizes the control heuristic in a hierarchical structure. The execution of the higher level knowledge source will select a KS or a sequence of KS at the next level and pass the control to the invoked KS. The higher-level KS is suspended and is not responding to changes until the associated lower level KS runs out of rules that match or terminates itself. Hierarchical control architecture offers several benefits such as clarity, directness of control, and efficiency [37,36].

Different from the hierarchical control approach, the Control Blackboard Approach [4] can suspend the original control plan, including high-level and low-level control decisions, and adopt a different control plan during the problem-solving process [38,4]. To provide this flexibility, the control blackboard approach explicitly stores control decisions on a separate blackboard panel so that they can also be adopted, updated, or discarded in response to dynamic problem-solving situations. Many blackboard system designs employ this approach as the control mechanism [38,4,39,40].

The above blackboard systems basically adopt the data-driven control for problem solving. The control module mainly resolves uncertainty about that sequence of actions will satisfy its assumed long-term goals $[41]$ . Since the goals do not affect the scheduler, the inference process does not determine the effects of executing a KS beyond its immediate effects on the system state. The goal-driven approach provides a more effective way to perform expectation-based focusing and speeds up system performance by avoiding considerable amounts of work involved with focusing on the data that is not relevant to the solution $[42]$ .

To integrate goal-directed focusing with other reasoning methods in a uniform mechanism, Johnson and Hayes-Roth [15] incorporate a diverse reasoning concept into the control blackboard approach. This concept supports a dynamic integration of different reasoning methods without altering the architecture of the blackboard system. The system can operate in a data-directed fashion, in which it prefers actions that are triggered by important events or states. It can operate in a goal-directed fashion, in which it prefers actions that lead to important events or states. It can operate in an action-directed fashion, in which it prefers actions that are essentially important. Finally, it can operate in a plan-directed fashion, in which it prefers actions that are consistent with a previously adopted strategic plan.

## 5. Diverse reasoning in AEROBA

Based on the analysis of opportunism and related control features in the expert's model formulation process, the control blackboard approach is chosen and a three-panel control blackboard architecture is developed for implementation (Fig. 1). In this architecture, the design of the blackboard data structure is based on an Extended Entity Relationship model (EER) to represent the problem, the solution, and associated data involved in model formulation [43]. An architecture that mAps the Entity-Relationship On Blackboard Architecture, named AEROBA, is therefore developed for implementation.

In AEROBA, the design of domain knowledge sources is based on a structure transformation concept in which the problem structure is designed and instantiated first, and then transformed into the related model structure. The instantiated model structure represents the solution of the model formulation activity (see Fig. 1). The formulation is conducted opportunistically and is regulated by control features embedded in the system. The design of the blackboard data structure and domain knowledge sources are described in Sen et al. [44] and Vinze et al. [45]. From the diverse reasoning point of view, this paper addresses the control issues in the system design.

## 5.1. A control blackboard approach

The design of control in AEROBA is based on a control blackboard approach to perform the formulation tasks in a similar way as observed in the expert's formulation protocols. In other words, the opportunistic control of AEROBA will also exhibit control features such as Determining problem boundaries, Decomposing the problem, Setting the goal, Delin-eating the formulation, Changing the formulation, Focusing on controllable components, Reasoning the formulation, and Evaluating the formulation in the model formulation process. Since it is not clear about the direct influence of the feature Predicting potential situations on the formulation progress, the implementation of AEROBA does not include this feature.

Using the control blackboard approach, AEROBA's control decisions respond to dynamic formulation situations and direct the generic control behavior performed by the same basic control knowledge sources (CKS). All of the control decisions and associated control knowledge are explicitly associated with a separate blackboard panel 'Control' (see Fig. 1).

## 5.2. Control panel

The Control panel is divided into seven levels: General-approach, Design, Policy, Focus, Trigger-record, Chosen-record, and Event. They are described below.

![](/api/attachments/WGMU6KH4/fulltext/images/bfebf72144c44ee0c1793d5f97bc7c29af5010c062ea88100f72de75e6d2f08a.jpg)  
Fig. 1. The AEROBA architecture.

## 5.2.1. General-approach level

The General-approach level records a single generic problem-solving approach such as 'first principles' or 'case-based'. In the prototype implementation, prior model formulation cases are not retained in the storage and the formulation is based on 'first principles'. The formulation process by first principles in AEROBA involves activities such as capturing the essential elements of the problem description, selecting a suitable target model to be formulated, and mapping the problem structure into the model structure.

## 5.2.2. Design level

Based on the General-approach decision, a set of design tasks are initiated. All of these tasks corresponding to the General-approach decision establish a generic strategic plan represented by a control decision recorded on the Design level. The strategic plan is subject to change as needed. In AEROBA, the strategic plan starts with a sequence of design tasks such as 'Classifying-the-problem, Decomposing-the-problem, Setting-the-goal, Delineating-theformulation', and 'Eliciting-the-problem'. During the formulation process, the design tasks in the strategic plan can be dynamically rearranged, deleted, or modified. A new design task can also be added to the strategic plan when the dynamic problem-solving events so suggests.

A strategic plan specifies a metalevel sequence of design tasks to be performed. The formulation tasks associated with each design task, however, are not necessarily accomplished in the intended sequence. This is due to the policy constraint and the dynamic formulation opportunism. The policy decisions are explained next and the lack of sequence in performing the design tasks are explained in the focus of attention mechanism.

## 5.2.3. Policy level

This level stores decisions such as general-policy, reasoning-policy, KS-policy, and rule-policy to be followed during the entire formulation process. The general-policy decision specifies the temporal life span of a domain KS. Two settings, ‘single-hit’ and ‘multiple-hit’, are considered in AEROBA. When a general-policy is set to ‘single-hit’, the system puts a just executed KS into dormancy for several cycles to distribute formulation opportunities to other triggered domain KS. When the general-policy is set to ‘multiple-hit’, the same KS can contribute to the formulation continuously if its precondition is still satisfied.

The reasoning-policy decision guides the direction of reasoning for the KS and rule triggering. There are two reasoning policies used alternatively in AEROBA, 'designing' and 'bookkeeping'. In the 'designing' policy, the selected knowledge source (KS) generates new solution elements or modifies the structure of existing solution elements. The direction of reasoning is moving-forward. In the 'bookkeeping' policy, the knowledge source acquires values for existing target solution elements, and the direction of reasoning is moving-backward. The formulation tasks performed in 'designing' policy include mainly the building and modification of the problem and solution structure. The formulation tasks performed in 'bookkeeping' policy involves instantiating problem attributes and mapping some attribute data from the Problem panel to the Solution panel.

The KS-policy decision specifies the scheduling criterion of the triggered knowledge sources under consideration. There are two possible settings considered in AEROBA, ‘responding-to-highest-level’ and ‘responding-to-lowest-level’. When the KS-policy is set to ‘responding-to-highest-level’, the system selects a KS responding to the highest blackboard level (levels in the Solution panel are considered higher than those in the Problem panel). Similar to the general-policy, the KS-policy could be set differently to reflect a different formulation style.

The rule-policy decision specifies the priority of triggered rules of the scheduled (selected) knowledge source. The rule-policy is set to ‘with-highest-score’ in the prototype implementation of AEROBA before a possible alternative is considered.

## 5.2.4. Focus level

During the formulation process, a generation or modification of solution elements by a domain knowledge source provides an opportunity for further formulation development. However, the opportunity may not be used right away unless the knowledge source responding to this opportunity is in focus. The mechanism for focus of attention is used to monitor the state of the blackboard and decide which set of knowledge sources should be considered next. The mechanism generates the focus decision, recorded on the Focus level (see Fig. 1), to specify a group of domain KS under attention during the intermediate formulation process.

As shown in Fig. 2, there are two types of focus: strategic and opportunistic. A strategic focus is induced by the strategic plan comprised of several design tasks, and an opportunistic focus is induced by some formulation opportunities recorded as special events. A strategic focus is suspended when another strategic focus gets attention. It can be resumed and get attention again if the KS in other strategic foci cannot make a contribution to the formulation progress. A strategic focus is interrupted when an opportunistic focus gets attention. It will be recovered if the KS in the opportunistic focus have no immediate contribution to the formulation progress.

A strategic focus is a list of domain KS that elaborate a design task in the strategic plan recorded on the Design Level. Only one design task can be in focus at a time. The design tasks and their associated strategic foci in terms of domain KS are listed in Table 1.

![](/api/attachments/WGMU6KH4/fulltext/images/b2a76866c0606e71da3739ef791ec2bec408af8c92887a6e90f6a2daeb8d1811.jpg)  
Fig. 2. Focus of attention in the AEROBA architecture.

The strategic focus can be interrupted by a special formulation event. This causes the temporal attention of an opportunistic focus. The opportunistic focus consists of another group of domain KS that do not correspond to any design task. If the opportunistic focus has no KS that makes an immediate contribution, the interrupted strategic focus will be recovered. There are two opportunistic foci, (KS 08, KS 09): instantiating problem attributes and (KS 12): instantiating tool attributes in the AEROBA system.

## 5.2.5. Trigger-record level

The Trigger-record level records triggering information of the KS and the rules. For example, a decision, triggered-KS, records the triggered KS to be scheduled for execution, and another decision, triggered-rules, records the triggered rules associated with the selected KS to be scheduled for execution.

Table 1  
Design tasks and strategic foci in AEROBA

<table><tr><td>Design task</td><td>Strategic focus</td></tr><tr><td>Classifying-the-problem</td><td>KS 01 ‘Set problem domain’KS 02 ‘Select problem type’</td></tr><tr><td>Decomposing-the-problem</td><td>KS 03 ‘Create problem entity type’KS 04 ‘Create problem relationship type’</td></tr><tr><td>Setting-the-goal</td><td>KS 10 ‘Set solution domain’KS 21 ‘Create solution entity type’KS 22 ‘Create solution relationship type’KS 23 ‘Create solution entity attribute’KS 24 ‘Create solution relationship attribute’</td></tr><tr><td>Delineating-the-formulation</td><td>KS 05 ‘Create problem entity attribute’KS 06 ‘Create problem relationship attribute’KS 11 ‘Map solution entity key attribute value’KS 25 ‘Get solution relationship key attribute value’</td></tr><tr><td>Eliciting-the-problem</td><td>KS 00 ‘Elicit problem feature’</td></tr><tr><td>Changing-the-formulation</td><td>KS 07 ‘Modify problem attribute’</td></tr></table>

## 5.2.6. Chosen-record level

This level records information related to the chosen KS or rule for execution. Some of these decisions on this level carry the information generated at the triggering time to be used in the execution time. For example, a Chosen-record decision, current-se, records the information of a solution element that satisfies all of the preconditions of a rule in the selected KS so that the execution of the selected rule can act based on the information of the attempted solution element.

## 5.2.7. Event level

The Event level records special events generated during the model formulation process. The events can induce changes in other control decisions and affect the subsequent control behavior. For instance, the events can cause the immediate change of focus decision directly by inducing an opportunistic focus. They can also rearrange the strategic plan and cause a future change of strategic focus.

## 5.3. Control knowledge sources

AEROBA uses the Inference Loop as the generic control mechanism for directing the system's formulation behavior. The causal relationships among related control decisions are explicitly connected by the control knowledge sources of the Control panel (see Fig. 1). The control knowledge sources are represented as function calls with influential control decisions as parameters. With this approach, the modification of control decisions and the influence they impose on the inference loop are synchronized in the same inference cycle.

As described above, the General-approach decision is set to ‘first principles’ in the AEROBA system. In response to this decision, several control knowledge sources, such as CKS 01 ‘Design strategic plan’, CKS 02 ‘Make policy’, and CKS 03 ‘Elaborate design’, are executed to set up initial formulation principles to regulate the behavior of the Inference Loop to control the formulation progress. The initial formulation principles include: (1) a strategic plan composed of the design tasks ‘Classifying-the-problem, Decomposing-the-problem, Setting-the-goal, Delineating-the-formulation, Elicit-Problem-semantics’; (2) an initial setting of policy values such as general-policy = 'single-hit', reasoning-policy = 'designing', KS-policy = 'responding-to-highest-level', and rule-policy = 'with-highest-score'; and (3) the setting of the initial focus corresponding to the first design task 'Classifying-the-problem'. Although the strategic plan specifies an intention of a sequence of design tasks to be performed, the actual execution of these tasks are not sequential due to the policy constraint and the dynamic formulation opportunism.

The Inference Loop is an iterative reasoning process in which a set of control knowledge sources are executed to direct the formulation progress. The major theme of the Inference Loop is to find out 'What to do next?' from cycle to cycle. This includes 'Which knowledge source and which rule is to be applied to which solution element?'. The activities involved in the Inference Loop and the related control knowledge sources are described below.

(1) CKS 04 ‘Initiate trigger record’ follows the general-policy and the reasoning-policy for examining solution elements related to the focused domain KS. If a solution element satisfies the precondition of the focused KS, the KS is called being triggered by the solution element. This control knowledge source writes the decision triggered-KS on the Trigger-record level.

(2) CKS 05 'Schedule KS' selects one KS from the triggered KS based on the KS-policy. For example, when the triggered KS include (KS 03 KS 04) (see Fig. 1), KS 04 is selected to be executed when the KS-policy is set to 'responding-to-highest-level'.

(3) CKS 06 ‘Elaborate trigger record’ examines each rule of the selected KS for triggering and adds further information, such as triggered-rules, to the Trigger-record level.

(4) CKS 07 'Schedule rule' selects one rule from the triggered rules based on the rule-policy.

(5) CKS 08 'Execute chosen record' executes the selected domain rule using information stored on the Chosen-record level. The execution of a domain rule typically creates or modifies the solution elements on the domain (Problem or Solution) panel.

(6) CKS 09 'Monitor policy focus' examines special events on the Event level and adjusts the control decisions on the Policy and Focus level if necessary. The execution of a domain rule typically creates or modifies solution elements on the domain panels. Sometimes, a domain rule also generates a special event that can induce the change of control decisions that, in turn, regulate the subsequent behavior of the Inference Loop in the following cycles.

![](/api/attachments/WGMU6KH4/fulltext/images/c01a7238f67c5078a76a587b96afc5170bec55eaac48e738788f2648c958ee68.jpg)  
Fig. 3. Sample control knowledge source in AEROBA.

(7) CKS 10 ‘Monitor design’ examines special events and modifies the strategic plan recorded on the Design level if necessary.

The logical construct of one control knowledge source, CKS 03, is shown in Fig. 3.

As indicated in Fig. 1, the communication between the domain panels and the control panel is through the execution of CKS 04, CKS 06, CKS 08, CKS 09 and CKS 10. Within them, CKS 04, CKS 06, CKS 08 combine control decisions and domain information into domain performance, whereas CKS 09 and CKS 10 are both event handlers that adjust the control decisions in response to domain events.

From the functioning of control decisions and control knowledge sources associated with the Control panel, the AEROBA control exhibits a diverse reasoning concept as addressed by Johnson and Hayes-Roth [15]. The mechanism for strategic focusing induces the system to operate in a plan-directed fashion, in which it follows a previously adopted strategic plan. The function for KS scheduling induces the system to operate in an action-directed fashion, in which it selects actions that are more important than others. The mechanism for event handling induces the system to operate in a data-directed fashion, in which it responds to important events or states. The system does not operate in a goal-directed fashion for selecting actions that lead to important events or states. Instead, the system uses a goal-directed bookkeeping policy to examine some domain knowledge sources on the response level and acquire data from the stimulus level or the user.

Therefore, the model formulation process of the AEROBA system no longer follows a predefined control strategy. Rather, the formulation is controlled by a dynamic integration of various reasoning approaches based on the control features observed in the expert's modeling process. The corresponding opportunism and control features in AEROBA are explained as follows.

## 5.4. Opportunism

In AEROBA, the opportunistic behavior is achieved by the mechanism of focus suspension/resumption and interruption in the AEROBA control. It is also induced by the policy constraint general-policy = 'single-hit' that restricts the same KS from being triggered continuously and distributes the formulation opportunity to other KS during the same time slot. The KS-policy = 'responding-to-highest-level' also contributes to the system opportunism since it induces the selection of the KS, from the triggered-KS, responding to the highest level. AEROBA has to jump back and forth during the formulation process because the KS responding to the higher levels will be selected once the opportunities come, but their rule executions may not be completed until the related rules of KS responding to the lower levels have been executed successfully.

## 5.5. Control features

The diverse reasoning concept included in the AEROBA architecture is used to support the various control features observed in the expert's modeling process. The control features are reflected in various control decisions recorded on the levels of Design, Policy, Focus, and Event. The control features in Protocol Analysis and the AEROBA system, and their relationships to AEROBA CKS are summarized in Table 2.

The feature of Determining Problem Boundaries is expressed by two tasks recorded on the Design level: Classifying-the-problem and Eliciting-the-problem. The former specifies the initial identification task for the problem type, and the later specifies the continuous elicitation task afterwards. These tasks combined with Decomposing-the-problem, Setting-the-goal, and Delineating-the-formulation form the strategic plan for model formulation by first principles - the General-approach decision. This strategic plan is initialized by CKS 01 'Design strategic plan', and each of the design tasks in the strategic plan is specified in terms of a group of domain KS by CKS 03 'Elaborate design' (see Fig. 1).

Table 2  
Control features and knowledge in AEROBA

<table><tr><td>Control features in protocol analysis</td><td>Control features in AEROBA</td><td>Control knowledge sources in AEROBA</td></tr><tr><td rowspan="2">Determining problem boundaries</td><td>Classifying-the-problem</td><td>CKS 01 ‘Design strategic plan’CKS 03 ‘Elaborate design’</td></tr><tr><td>Eliciting-the-problem</td><td></td></tr><tr><td>Decomposing the problem</td><td>Decomposing-the-problem</td><td>CKS 01 ‘Design strategic plan’CKS 03 ‘Elaborate design’</td></tr><tr><td>Setting the goal</td><td>Setting-the-goal</td><td>CKS 01 ‘Design strategic plan’CKS 03 ‘Elaborate design’</td></tr><tr><td>Delineating the formulation</td><td>Delineating-the-formulation</td><td>CKS 01 ‘Design strategic plan’CKS 03 ‘Elaborate design’</td></tr><tr><td>Changing the formulation</td><td>Changing-the-formulation</td><td>CKS 10 ‘Monitor design’CKS 03 ‘Elaborate design’</td></tr><tr><td>Focusing on controllable components</td><td>Focusing-on-controllable-components</td><td>CKS 03 ‘Elaborate design’CKS 09 ‘Monitor policy focus’</td></tr><tr><td>Predicting potential situations</td><td>None</td><td>Not addressed in the current implementation</td></tr><tr><td>Reasoning the formulation</td><td>Reasoning-in-bookkeeping</td><td>CKS 02 ‘Make policy’CKS 09 ‘Monitor policy focus’</td></tr><tr><td>Evaluating the formulation</td><td>Evaluating-the-formulation</td><td>CKS 09 ‘Monitor policy focus’CKS 10 ‘Monitor design’</td></tr></table>

The feature of Focusing-on-controllable-components is reflected in the decision recorded on the Focus level. A strategic focus is initialized by CKS 03 'Elaborate design' to specify a design decision in terms of domain KS, and an opportunistic focus is induced by CKS 09 'Monitor policy focus' to take an immediate action for the formulation opportunity. The feature of Reasoning-the-formulation is indeed an exercise for each cycle of the Inference Loop. Its dynamic nature is, however, reflected in the value change of the policy decision, reasoning-policy. Therefore, the AEROBA's control feature corresponding to Reasoning-the-formulation is called Reasoning-in-bookkeeping exhibited when the value of reasoning-policy is changed from the default designing to bookkeeping. This decision and other policy decisions are initialized by CKS 02 'Make policy' as the guideline to be followed during the formulation process. The value of reasoning-policy reflects the direction of reasoning and can be changed by CKS 09 'Monitor policy focus' during the formulation process.

The feature of Evaluating-the-formulation is exhibited when the system executes CKS 09 'Monitor policy focus' to interrupt the current focus and policy decisions. This feature can also be exhibited when the system executes CKS 10 'Monitor design' to modify the strategic plan, such as appending the design task Changing-the-formulation to the strategic plan. After being induced into the strategic plan as a design task, Changing-the-formulation will be specified in terms of domain KS by CKS 03 'Elaborate design' in the future cycles of the Inference Loop.

As indicated in Table 3, some control features, such as Classifying-the-problem, Decomposing-the-problem, Setting-the-goal, Delineating-the-formulation, and Eliciting-the-problem, are more domain-oriented. The major roles they play are in directing the formulation tasks performed by a set of domain KS. In AEROBA, the domain KS responding to Classifying-the-problem traces a Problem Type Discrimination Tree to identify a problem type according to the interactive problem features provided by the user. The domain KS responding to Eliciting-the-problem traces a Problem Elicitation Tree to collect more problem features from the user interactively. The other domain KS, also driven by the domain-oriented control features, perform the construction work of the model formulation based on the EER structure. The domain KS and their formulation performance on the EER structure are described in Sen et al. [44] and Vinze et al. [45].

Table 3  
Control features and roles in AEROBA

<table><tr><td>Control features</td><td>Role in specifying control</td><td>Role in directing formulation</td></tr><tr><td>Classifying-the-problem</td><td>Is a design task in the strategic plan of the formulation</td><td>Selects a problem domain and determines a problem type</td></tr><tr><td>Decomposing-the-problem</td><td>Is a design task in the strategic plan of the formulation</td><td>Creates entity types and relationship types for the problem EER</td></tr><tr><td>Setting-the-goal</td><td>Is a design task in the strategic plan of the formulation</td><td>Sets the solution domain and creates the solution EER components</td></tr><tr><td>Delineating-the-formulation</td><td>Is a design task in the strategic plan of the formulation</td><td>Creates problem attributes and solution key attributes</td></tr><tr><td>Eliciting-the-problem</td><td>Is a design task in the strategic plan of the formulation</td><td>Elicits incremental problem features</td></tr><tr><td>Changing-the-formulation</td><td>Modifies the strategic plan based on some special events, is also a design task in the strategic plan of the formulation</td><td>Modifies the earlier formulation</td></tr><tr><td>Focusing-on-controllable-components</td><td>Initiates, suspends, resumes, or interrupts a focus of attention</td><td>Confines the formulation within a strategic focus induced from a design decision or within an opportunistic focus induced from a special formulation event</td></tr><tr><td>Reasoning-in-bookkeeping</td><td>Adopts a different reasoning policy named bookkeeping</td><td>Applied the bookkeeping policy to the formulation tasks such as instantiating problem attributes and mapping non-key solution attribute values</td></tr><tr><td>Evaluating-the-formulation</td><td>Evaluates active events and decides whether to modify the strategic plan, policies, and/or to interrupt the current focus</td><td>Affects the subsequent formulation process based on the changes in control decisions</td></tr></table>

Some control features, such as Focusing-on-controllable-components and Evaluating-the-formulation are more control-oriented. The major roles they play are in adjusting the control decisions. Other control features, such as Changing-the-formulation and Reasoning-in-bookkeeping are in-between and play almost equal important roles in both domain and control aspects. Changing-the-formulation belongs to this category because it is possible to change both the strategic plan and formulation results performed by the domain KS. Reasoning-in-bookkeeping belongs to this category because the formulation tasks using the bookkeeping policy is operational based on a different reasoning policy. The in-between control features, however, imply that a further clarification of the control features deserves a future research attention.

A sample linear programming formulation problem, a Procurement problem, is shown in Appendix A and the AEROBA execution of model formulation for this problem is shown in Appendix B. The partial execution trace reveals the user interaction and control features in AEROBA, the automated model formulation framework developed using the diverse reasoning concept.

## 6. Comparison of control features

Although AEROBA uses the diverse reasoning concept to simulate the control features exhibited in the expert's modeling protocols, the interpretation of control features in the AEROBA executions are not exactly the same as in the expert's protocols, as indicated in Table 4. Table 5 shows the comparison of several control features between the protocols and the system executions for a Multi-Period Production-Inventory Problem. The fundamental differences in the interface setting and the representation structure explain the interpretation discrepancy between the control features in the expert's protocols and those in the AEROBA executions. For the verbalization, the expert was not interacting with the interviewer for the formulation. A 'reading problem statements and formulating a model' setting was used to reduce the possible bias from the interactive interruption. As a result, many control features that would not be otherwise obvious were identified in the statements of judgmental explanations in addition to the formulation verbals. On the other hand, the setting of the AEROBA implementation provides an interactive environment for helping the formulation of models. Therefore the AEROBA executions are geared toward being more system-directed and the control features are interpreted differently.

Another explanation for the difference in control features is the representation structure for data and knowledge involved in the formulation process. In the expert's protocols, there is no obvious data or knowledge representation scheme, whereas the AEROBA implementation requires an explicit representation scheme to facilitate the computerized formulation process. Since the EER constructs are used for representing the data and knowledge of formulation, the reasoning of AEROBA therefore centers around the EER structure construction, modification, mapping and instantiation.

The discrepancy is reasonable since it is very difficult to use a computer system to account for the details of protocols from different individuals ([46], p. 196). This does not mean that the computer system is incorrect. Since the protocols are encoded at a very abstract level with the goal of uncovering generalizable features of the cognitive process, the system is developed artificially based on an internal process model supported by the general features related to the description of cognitive process in the protocols ([46], p. 263). The validation of the formulation process therefore focuses on the demonstration

Table 4  
Control features in protocols and AEROBA executions

<table><tr><td>Control feature</td><td>Interpretation of control feature in the protocols</td><td>Interpretation of control feature in the AEROBA executions</td></tr><tr><td>Determining problem boundaries (DPB)</td><td>Explicit problem categorization and incremental problem elicitation</td><td>Selects a problem domain, determines a problem type in the domain, and elicits additional problem features</td></tr><tr><td>Decomposing the problem (DTP)</td><td>Divides the problem into various components</td><td>Creates the entity types and relationship types for the problem</td></tr><tr><td>Setting the goal (STG)</td><td>Specifies a tentative goal</td><td>Creates the EER components of the selected tool type</td></tr><tr><td>Delineating the formulation (DTF)</td><td>Delineates formulation actions</td><td>Creates the problem attributes and develops key attributes for the solution</td></tr><tr><td>Changing the formulation (CHG)</td><td>Modifies the formulation</td><td>Inserts or modifies the strategic plan based on some special events</td></tr><tr><td>Focusing on controllable components (FCC)</td><td>Concentrates on a specific target</td><td>Initiates, suspends, resumes, or interrupts a focus of attention</td></tr><tr><td>Predicting potential situations (PPS)</td><td>Estimates environmental factors</td><td>Not addressed in the current implementation</td></tr><tr><td>Reasoning the formulation (RTF)</td><td>Infers actions to be taken</td><td>Adopts different reasoning policy such as designing or bookkeeping</td></tr><tr><td>Evaluating the formulation (ETF)</td><td>Makes a judgement about the already taken actions</td><td>Evaluates active events to decide whether to modify the strategic plan or interrupt the current focus, or does nothing</td></tr></table>

Table 5  
Comparison of protocols and AEROBA executions in several control features

<table><tr><td>Experts' protocols (protocol number and verbalization)</td><td>AEROBA executions (cycle number and activity involved, Rule xxyy represents a rule stored in KS xx)</td></tr><tr><td colspan="2">(A) Determining problem boundaries</td></tr><tr><td>Interpretation:</td><td>Interpretation:</td></tr><tr><td>Explicit's problem categorization</td><td>Selects a problem domain, determines a problem type in the domain, and elicits additional problem features</td></tr><tr><td>Expert 1:</td><td>Cycle 1, Rule 0101 fired:</td></tr><tr><td>4. ... it's an uncapacitated type of problem ...</td><td>Set the domain name.</td></tr><tr><td>11. ... you can treat it as a single product problem ...</td><td></td></tr><tr><td>Expert 2:</td><td>Cycle 2, Rule 0201 fired:</td></tr><tr><td>2. So it is a pattern kind of problem ...</td><td>Determine problem type in Production Planning domain.</td></tr><tr><td>31.4. ... One is to try to pattern typical kinds of problems and thats faster but is more dangerous ...</td><td>The problem type is identified to be a standard OVTINV (overtime inventory) problem by tracing the Problem Type Discrimination Tree.</td></tr><tr><td>Expert 3:</td><td></td></tr><tr><td>1. ... this is a *** commodity production problem ...</td><td></td></tr><tr><td>6. ... see if I can represent this as a network problem, for instance, a transportation problem ...</td><td></td></tr><tr><td>Interpretation:</td><td>Interpretation:</td></tr><tr><td>Incremental problem elicitation</td><td>trace the Problem Elicitation Tree for the problem type</td></tr><tr><td>Expert 1:</td><td>Since the problem is a standard OVTINV problem, no further problem elicitation is necessary.</td></tr><tr><td>10. ... the problem is kinda simplistic in that there is no set-up cost from transferring from a product to the other ...</td><td></td></tr><tr><td>17–18. So it's a single-item problem. Subject to I have a series of demand constraints.</td><td></td></tr><tr><td>31. ... Let's see how this is given. The production capabilities ...</td><td></td></tr><tr><td>Expert 2:</td><td></td></tr><tr><td>31.3. ... I didn't even know until I came down here that, wait a minute there is no holding cost ...</td><td></td></tr><tr><td>Expert 3:</td><td></td></tr><tr><td>14. So this can be viewed as a transportation problem with 24 supply points and 12 demand points.</td><td></td></tr><tr><td colspan="2">(B) Decomposing the problem</td></tr><tr><td>Interpretation:</td><td>Interpretation:</td></tr><tr><td>divides the problem into various components</td><td>creates the entity types and relationship types for the problem</td></tr><tr><td>Expert 1:</td><td>Cycle 5, Rule 0309 fired:</td></tr><tr><td>20. So I have regular time capacity constraint and an OT capacity constraint.</td><td>Add entity type SUPPLY-PERIOD for problem type OVTINV.</td></tr><tr><td>22. And my demand constraints are going to have 2 types of production in it.</td><td></td></tr><tr><td>40. My cost = the sum of my production and storage. I've got 2 production. I've got regular time and overtime.</td><td>Cycle 12, Rule 0310 fired:</td></tr><tr><td>Expert 2:</td><td>Add entity type DEMAND-PERIOD for problem type OVTINV.</td></tr><tr><td>6. You can produce in any one of 2 types - you can produce normal or you can produce overtime.</td><td>Cycle 19, Rule 0405 fired:</td></tr><tr><td>21. So we got two types of constraint.</td><td>Add relationship type STORE for problem type OVTINV.</td></tr><tr><td>Expert 3:25. We have three sets of decisions.</td><td></td></tr><tr><td>(C) Delineating the formulationInterpretation:delineates formulation actions</td><td>Interpretation:creates the problem attributes and develops key attributes for the solution</td></tr><tr><td>Expert 1:21. I have to relate the amount produced in each one of those and that should be the amount produced total in my demand constraints.26. The inventory last period plus the amount I'm producing this period which is going to be the sum of 2 variables. ... regular time and overtime.30. Then I have a set of constraints for regular time capacity.So the amount I produce in regular time.</td><td>Cycle 8, Rule 0511 fired:Add a set of attributes for the entity type SUPPLY-PERIOD.Cycle 15, Rule 0512 fired:Add another set of attributes for the entity type DEMAND-PERIOD.Cycle 22, Rule 0604 fired:Add a set of attributes for the relationship type STORE.</td></tr><tr><td>Expert 2:10. I'd call them A through L and P for ... Or N for normal and O for overtime. so we got all the variable here CN, DN, all the way down to LN. And then you have AO, BO all the way down to LO for overtime.18. ... call it X sub i, sub j, sub k where i is A through L.i is the month that it is produced, j is the production process, normal or overtime, and k is when you deliver this stuff or consumed - when its meeting a demand. o i is month production, k is month consumption.</td><td></td></tr><tr><td>Expert 3:12. Supply *** units of ice cream here, 5 units here, and so on and so forth, and we got 24 of these supply points.16. Figure out how you're going to produce in January for January. You *** is there how much you're going to produce in January for February, for instance. How much you're going to produce in January, in March.21. Similarly, we got production in December, in January, overtime for January, overtime for January, the overtime for February, and all this different transportation.</td><td>...</td></tr></table>

of the feasibility of this development approach, rather than the assessment of the quality of the system performance [47]. Despite the difference in the interpretation and the sequence of the control features, the exertion of the equivalent control features in the system executions demonstrates the appropriateness of the internal process model. That means, an internal process model incorporated in the AEROBA design has been constructed adequately such that the abstract human behavior exhibited in the protocols can be transformed into a computerized environment.

## 7. Usefulness of the AEROBA system

The AEROBA system is developed to help the formulation of models based on the observation of the expert's modeling behavior. The usefulness of the system is tested in an experiment to evaluate the comparative merits of the AEROBA-assisted process and the manual process in LP formulation. The subjects for the experiment were students taking Business Information Systems Concepts (BANA217), the first MIS course offered by the Department of Business Analysis and Research at Texas A&M University. Several LP problems were used for the experiment. One of them is shown in Appendix C. The formulation interaction between the subject and the AEROBA system is shown in Appendix D. The opinions of the users for each of the two processes were measured in terms of the perceived ‘formulation effectiveness’. The correctness of the formulation and the time spent on the formulation task when using these two different processes were also compared.

Table 6  
Experiment setting for effectiveness measurement

<table><tr><td rowspan="2">Order of process the subjects are exposed to</td><td colspan="2">Type of process the subjects are measured on</td></tr><tr><td>Manual</td><td>AEROBA-assisted</td></tr><tr><td>Manual → AEROBA-assisted</td><td>Group-1</td><td>Group-2</td></tr><tr><td>AEROBA-assisted → Manual</td><td>Group-3</td><td>Group-4</td></tr></table>

To facilitate the comparison, each subject was asked to go through both processes for formulating LP models but was measured for only one of the processes. The experiment is designed as a $2 \times 2$ factorial. The first factor studied is the type of process, the AEROBA-assisted process as compared to the manual process, used in formulating an LP model. The second factor in the design is the order of the processes the subject is exposed to. The second factor is included to test whether the order of the processes interacts with the type of process to affect the subject's performance and perception. This design allows the use of two-way analysis of variance for analyzing the data. The assignment of these two factors to the experiment groups is shown in Table 6. The details of the experiment design are described in Liou [48].

## 7.1. Effectiveness questionnaires

The user's opinions for each of the process are measured in terms of the perceived ‘formulation effectiveness’. Two questionnaires are used for measuring the effectiveness of the manual formulation process and the AEROBA-assisted formulation process. The questionnaires share a common set of 17 questions. The remainder of the questions focus on evaluating the specific features of the two processes. These ‘effectiveness questionnaires’ are derived from those used in Vinze [49] with only minor modifications. These instruments have been validated and are therefore reliable software verification instruments [49].

The common questions shared by the two instruments for measuring effectiveness of the two formulation processes produce a composite score for the 'formulation effectiveness'. The common questions are divided into three embedded factors-user satisfaction, task basis for effectiveness, and formulation basis for effectiveness. According to Vinze's [49] analysis, the first two factors are reliable since the levels of the internal consistency are higher than an acceptable value. The third factor, although it is associated with a low reliability score, is included because it is consistent with the system effectiveness measurement literature. The distribution of the common questions to these three factors is outlined in Table 7. The measures using these instruments include the scores for the underlying individual factors and the composite score for all of these three factors. This setup allows for a factorwise evaluation, as well as an overall evaluation of the formulation effectiveness.

## 7.2. Formulation effectiveness

In evaluating the comparative effectiveness of the AEROBA-assisted process and the manual process, the dependent variable, formulation effectiveness, is represented by the composite score from the 17 common questions. The statistics from the two-way ANOVA used for testing this composite score are presented in Table 8. The statistics also indicate that there is a significant overall effect (p = 0.0084) and no significant effect from the interaction of the independent variables, the type of process and the order in which the subjects are exposed to the processes (p = 0.1738). The null hypothesis for testing the first main effect is: H0: The Formulation effectiveness is independent of the type of formulation process.

Table 7  
Factorwise common questions in the effectiveness questionnaires

<table><tr><td>Factor</td><td>Common question</td></tr><tr><td>User satisfaction</td><td>Q1: In general, how would you describe your experience in completing the task assigned?Q4: Was the process of obtaining the formulation for your task:Q5: Time taken for obtaining the formulation for your task was:Q9: While completing the task I was:Q13: How confident were you about the formulation made?Q14: Did you perceive the time limit of the formulation to be:Q16: How do you feel about the formulation made by the manual process?Q17: If faced with a task requiring LP formulation in the future, would you like to do it by yourself?</td></tr><tr><td>Task basis for effectiveness</td><td>Q2: The task was:Q6: Did you get to voice all your concerns about the task prior to the formulation?Q8: The time required for preparing for the task was:Q15: The LP formulation made was:</td></tr><tr><td>Formulation basis for effectiveness</td><td>Q7: While completing the task I:Q11: In your opinion was the formulation process:Q18: If given the choice between a manual process and a computer-assisted process to formulate an LP model, which would you prefer?</td></tr></table>

The results show the F-value to be 10.05 (d.f. = 1, 63), allowing the null hypothesis to be rejected with p = 0.0024. It is concluded that the type of formulation process does have an impact on the overall formulation effectiveness. The cell means, 2.677 and 3.633 (see Table 8), suggest that the students perceive the AEROBA-assisted process to be more appropriate than the manual process in terms of the overall formulation effectiveness. The t-test also indicates that there is a significant difference between the means (p = 0.0019).

The null hypothesis for testing the second main effect is: H0: The Formulation effectiveness is independent of the order of exposure to the formulation processes.

Table 8  
Statistical results for the overall formulation effectiveness analysis

<table><tr><td colspan="2">Source of variance</td><td>DF</td><td>Sum of squares</td><td>Mean square</td><td>F value</td><td>Probability &gt; F</td></tr><tr><td colspan="2">Overall model</td><td>3</td><td>18.581</td><td>6.194</td><td>4.26</td><td>0.0084</td></tr><tr><td colspan="2">Error</td><td>63</td><td>91.634</td><td>1.455</td><td></td><td></td></tr><tr><td colspan="2">Type of process (AEROBA-assisted vs. Manual)</td><td>1</td><td>14.618</td><td>14.618</td><td>10.05</td><td>0.0024</td></tr><tr><td colspan="2">Order of the processes</td><td>1</td><td>0.495</td><td>0.495</td><td>0.34</td><td>0.5617</td></tr><tr><td colspan="2">Interaction effect</td><td>1</td><td>2.753</td><td>2.753</td><td>1.89</td><td>0.1738</td></tr><tr><td colspan="7">Statistical results from t-test for the type of process</td></tr><tr><td>Process</td><td>N</td><td>DF</td><td>Mean</td><td>Standard error</td><td>t Value</td><td>Probability &gt; |t|</td></tr><tr><td>AEROBA-Assisted</td><td>33</td><td>65</td><td>2.677</td><td>0.155</td><td>-3.24</td><td>0.0019</td></tr><tr><td>Manual</td><td>34</td><td></td><td>3.633</td><td>0.249</td><td></td><td></td></tr></table>

As shown in Table 8, the F-value of 0.34 does not allow the null hypothesis to be rejected (p = 0.5617). This suggests that the order in which the subjects are exposed to the formulation processes does not affect the overall formulation effectiveness. It is therefore concluded that the students perceive a higher degree of overall formulation effectiveness for the AEROBA-assisted process compared to the manual process, regardless of the order in which the students are exposed to these two processes.

The statistical results for the individual factors, ‘user satisfaction’ and ‘formulation basis for effectiveness’, are similar to the results for the overall comparative effectiveness. In other words, the students are more satisfied with the AEROBA-assisted process and perceive it to be more effective. It is reasonable to have no statistical significance for the factor ‘task basis for effectiveness’ since the formulation tasks assigned to students working on both processes are similar.

The statistical analysis of the comparative effectiveness measurements indicates the AEROBA-assisted process scores higher in terms of formulation effectiveness. The percentage of subjects generating the correct formulation is also higher for the AEROBA-assisted process than for the manual process (69.7% vs. 41.2%). However, the subjects measured on the AEROBA-assisted process spend more time in completing the assigned formulation task (average 8.5 min vs. 6.1 min). This can be attributed to the nature of the human-computer interaction process. It is therefore concluded that the AEROBA-assisted process is effective in helping users with limited LP knowledge to formulate a model for problems with similar difficulty level as those used for the experiment.

## 8. Conclusion

The importance of the control aspect in model formulation has been emphasized in the literature but not addressed in most earlier research on automated model formulation. In this paper, we address the diverse reasoning concept in the AEROBA system that adopts a control blackboard approach to simulate the control behavior, including the opportunism and control features, observed in the expert's model formulation process. The diverse reasoning concept facilitates the simulation of the control features in the system design and enhances the understanding of these abstract features in the expert's cognitive process. The control features that are subjectively defined for the expert's protocols are explicitly clarified in the system implementation settings. We therefore have moved toward better understanding of and supporting to the modeling process for the design of intelligent decision support systems.

While the concepts of process abstraction and data abstraction induce benefits such as information hiding and code reuse for the development of transaction-based information systems, the control abstraction established by various control features in intelligent decision support systems is expected to attract more attention. The expert system shell, the most popular development tool for intelligent systems, indeed provides the most generic control features. Layered control features with richer control semantics should help in better communication between experts and the knowledge engineer for system development, as well as in better explanation to the users for the system implementation. The coordination of distributed and multimedia decision support agents also depend on the control aspect of intelligent systems. Currently, we only evaluate the AEROBA's simulation of the expert's formulation behavior in terms of control features and the usefulness of the AEROBA-assisted formulation process in terms of formulation effectiveness. Further research on the control aspect of intelligent decision support systems to enhance the communication and coordination effectiveness for system development and system use is also expected.

## Acknowledgements

The author would like to acknowledge the contribution of her Ph.D. advisors at Texas A&M University, Dr. Arun Sen and Dr. Ajay S. Vinze, to the concept development presented in this paper. It is also highly appreciated for Dr. Marietta J. Tretter's contribution to the experiment design and statistical analysis adopted in this paper.

## Appendix A. Procurement problem

A store chain has an order for 70 display terminals at location D1 and 40 at location D2. It has 2 stores, S1 and S2, from which it may ship terminals at costs given in the following table:

<table><tr><td>Shipping route</td><td>Unit shipping cost</td></tr><tr><td>S1-D1</td><td>US$20</td></tr><tr><td>S1-D2</td><td>US$25</td></tr><tr><td>S2-D1</td><td>US$50</td></tr><tr><td>S2-D2</td><td>US$55</td></tr></table>

Unfortunately, neither store has sufficient stock to supply the order. Thus more terminals must be purchased. The chain has US\$15 000 available for buying new terminals. Each store can buy terminals at a cost that varies due to the different distances of the stores from the suppliers, and newly bought units must be shipped to D1 and D2 as needed. Each store buys terminals at a different price. The number of terminals in stock and the cost of buying more terminals are listed in the following table:

<table><tr><td>Store site name</td><td>Purchase price per unit</td><td>Stock amount</td></tr><tr><td>S1</td><td>US$400</td><td>50</td></tr><tr><td>S2</td><td>US$350</td><td>20</td></tr></table>

Due to the limit of the truck load, no more than 65 and no more than 45 terminals can be purchased at stores S1 and S2 respectively. Determine how many terminals must be bought by each store and how many should be shipped from each store to each destination to minimize the total expense to the chain.

Note: For this example, the system first examines a series of problem characteristics and recognizes it as a single product transportation problem (SPTP). The system then starts building a standard structure in terms of EER for this problem. However, this is not a standard SPTP. It involves a procurement activity and a budget constraint at the supply location. The supply capacity is supported by the existing stock and a new purchasing amount. There is also integer constraints for shipping and purchasing goods like display terminals. Because of the incremental understanding, the system will further elicit the problem and make modification while continuing its ongoing formulation. The overall process is conducted opportunistically and dynamically directed by the control features set in the system.

## Appendix B. Partial trace of control features for the procurement problem

AEROBA>

Which problem area you working on?

Please answer one area name such as PRODPLAN, AUDITING, or FORECASTING?

USER-RESPONSE>

PRODPLAN

cycle-number 0, Focusing-on-Controllable-Components

AEROBA>

AEROBA system is developed based on the opportunistic problem solving process observed from the expert modeler. Therefore the system MAY NOT FOLLOW A PARTICULAR SEQUENCE to perform various formulation tasks. You may be prompted with a question out of your expectation. Don't be surprised! Just FOLLOW THE AEROBA'S THINKING PROCESS and READ THE PROBLEM DESCRIPTION CAREFULLY to find the answer.

Now, AEROBA starts the formulation process by first focusing on the task of Classifying-the-Problem.

Classification task begins...

cycle-number 1, Classifying-the-Problem

cycle-number 1, Evaluating-the-Formulation

AEROBA>

Is this problem related to transforming goods (answer TR), or related to allocating personnel or capital (answer AL)?

USER-RESPONSE>

## TR

## AEROBA>

Which type of product transformation is involved in your problem (answer PLACE, TIME, or FORM)?

USER-RESPONSE>

## PLACE

## AEROBA>

Is yours a single product situation (answer YES or NO)?

USER-RESPONSE>

YES

## AEROBA>

Now, AEROBA classifies the problem type as SINGLE-PRODUCT-TRANSPORTATION-PROBLEM.

AEROBA will now perform various formulation tasks, such as Decomposing-the-Problem, Setting-the-Goal, and Delineating-the-Formulation, depending on the current formulation opportunities.

AEROBA will perform these tasks without user involvement. When a data collection or more problem information is needed, AEROBA will interrupt the current process and request either of them from you. These formulation tasks are to organize the problem structure and construct a corresponding LP model.

Formulation continues...

cycle-number 2, Classifying-the-Problem

cycle-number 2, Evaluating-the-Formulation

cycle-number 3, Focusing-on-Controllable-Components

cycle-number 4, Focusing-on-Controllable-Components

cycle-number 5, Decomposing-the-Problem

cycle-number 5, Evaluating-the-Formulation

cycle-number 6, Focusing-on-Controllable-Components

cycle-number 7, Focusing-on-Controllable-Components

cycle-number 8, Delineating-the-Formulation

cycle-number 8, Evaluating-the-Formulation

cycle-number 8, Focusing-on-Controllable-Components

## AEROBA>

Please enter all of the data in letters for SUPPLY-LOCATION-NAMES (separated by a space).

USER-RESPONSE>

S1 S2

AEROBA>

Are you really sure these are data for SUPPLY-LOCATION-NAMES (answer YES or NO)?

USER-RESPONSE>

YES

cycle-number 9, Reasoning-in-Bookkeeping

cycle-number 9, Evaluating-the-Formulation

cycle-number 9, Focusing-on-Controllable-Components

cycle-number 11, Focusing-on-Controllable-Components

cycle-number 12, Decomposing-the-Problem

cycle-number 12, Evaluating-the-Formulation

cycle-number 12, Focusing-on-Controllable-Components

cycle-number 14, Focusing-on-Controllable-Components

cycle-number 15, Delineating-the-Formulation

cycle-number 15, Evaluating-the-Formulation

cycle-number 15, Focusing-on-Controllable-Components

## AEROBA>

Please enter all of the data in letters for DEMAND-LOCATION-NAMES (separated by a space).

USER-RESPONSE>

D1 D2

## AEROBA>

Are you really sure these are data for DEMAND-LOCATION-NAMES (answer YES or NO)?

## USER-RESPONSE>

YES

cycle-number 16, Reasoning-in-Bookkeeping

cycle-number 16, Evaluating-the-Formulation

cycle-number 16, Focusing-on-Controllable-Components

cycle-number 18, Focusing-on-Controllable-Components

cycle-number 19, Decomposing-the-Problem

cycle-number 19, Evaluating-the-Formulation

cycle-number 19, Focusing-on-Controllable-Components

cycle-number 21, Focusing-on-Controllable-Components

cycle-number 22, Delineating-the-Formulation

cycle-number 22, Evaluating-the-Formulation

cycle-number 22, Focusing-on-Controllable-Components

## AEROBA>

Please enter the datum in number for DEMAND-LOCATION-REQUIREMENT of D1.

## USER-RESPONSE>

70

## AEROBA>

Please describe the constraint for DEMAND-LOCATION-REQUIREMENT of D1.

Is it a Maximum-Amount (answer MAX), Exact-Amount (answer EXACT), or Minimum-Amount (answer MIN)?

USER-RESPONSE>

## EXACT

## AEROBA>

Please enter the datum in number for DEMAND-LOCATION-REQUIREMENT of D2.

## USER-RESPONSE>40

## AEROBA>

Please describe the constraint for DEMAND-LOCATION-REQUIREMENT of D2.

Is it a Maximum-Amount (answer MAX), Exact-Amount (answer EXACT), or Minimum-Amount (answer MIN)?

USER-RESPONSE>

## EXACT

cycle-number 23, Reasoning-in-Bookkeeping

cycle-number 23, Evaluating-the-Formulation

cycle-number 23, Focusing-on-Controllable-Components

cycle-number 25, Focusing-on-Controllable-Components

cycle-number 26, Focusing-on-Controllable-Components

cycle-number 27, Focusing-on-Controllable-Components

cycle-number 28, Focusing-on-Controllable-Components
cycle-number 29, Setting-the-Goal
cycle-number 29, Evaluating-the-Formulation
cycle-number 29, Focusing-on-Controllable-Components
...
cycle-number 162, Focusing-on-Controllable-Components
cycle-number 164, Focusing-on-Controllable-Components
cycle-number 165, Evaluating-the-Formulation
cycle-number 165, Focusing-on-Controllable-Components
cycle-number 166, Reasoning-in-Bookkeeping
cycle-number 166, Evaluating-the-Formulation
cycle-number 166, Focusing-on-Controllable-Components
cycle-number 168, Focusing-on-Controllable-Components
cycle-number 170, Focusing-on-Controllable-Components
cycle-number 171, Evaluating-the-Formulation
cycle-number 171, Focusing-on-Controllable-Components
cycle-number 172, Reasoning-in-Bookkeeping
cycle-number 172, Evaluating-the-Formulation
cycle-number 172, Focusing-on-Controllable-Components
cycle-number 174, Focusing-on-Controllable-Components
cycle-number 176, Focusing-on-Controllable-Components
cycle-number 177, Evaluating-the-Formulation
cycle-number 177, Focusing-on-Controllable-Components
cycle-number 178, Reasoning-in-Bookkeeping

cycle-number 178, Evaluating-the-Formulation
cycle-number 178, Focusing-on-Controllable-Components
cycle-number 180, Focusing-on-Controllable-Components
cycle-number 182, Focusing-on-Controllable-Components
cycle-number 183, Evaluating-the-Formulation
cycle-number 183, Focusing-on-Controllable-Components
cycle-number 184, Reasoning-in-Bookkeeping
cycle-number 184, Evaluating-the-Formulation
cycle-number 184, Focusing-on-Controllable-Components
cycle-number 186, Focusing-on-Controllable-Components

## AEROBA>

The formulation in algebra format for this problem is:

Objective Function: Minimize Total Cost = 400 \* (SL.PUR.QTY. S1) + 350 \* (SL.PUR.QTY. S2) + 20 \* (SH.QTY S1 D1) + 25 \* (SH.QTY S1 D2) + 50 \* (SH.QTY S2 D1) + 55 \* (SH.QTY S2 D2)

Subjected to:
    1 \* (SH.QTY S1 D1) + 1 \* (SH.QTY S2 D1) = 70
    1 \* (SH.QTY S1 D2) + 1 \* (SH.QTY S2 D2) = 40
    - 1 \* (SL.PUR.QTY. S1) + 1 \* (SH.QTY S1 D1) + 1 \* (SH.QTY S1 D2) = 50
    - 1 \* (SL.PUR.QTY. S2) + 1 \* (SH.QTY S2 D1) + 1 \* (SH.QTY S2 D2) = 20
    400 \* (SL.PUR.QTY. S1) + 350 \* (SL.PUR.QTY. S2) <= 15000
    (SL.PUR.QTY. S1): integer, (SL.PUR.QTY. S1) <= 65, (SL.PUR.QTY. S2): integer, (SL.PUR.QTY.

S2) $< = 45$ , (SH.QTY S1 D1): integer, (SH.QTY S1 D2): integer, (SH.QTY S2 D1): integer, (SH.QTY S2 D2): integer

AEROBA>

The time spent for the overall AEROBA session is:

overall-real-time = 7119/25 seconds

overall-run-time = 223/10 seconds

Good Job!

total cycle = 207

count of Classifying-the-Problem = 2

count of Decomposing-the-Problem = 3

count of Setting-the-Goal = 7

count of Delineating-the-Formulation = 12

count of Changing-the-Formulation = 5

count of Eliciting-the-Problem = 5

count of Reasoning-in-Bookkeeping = 32

count of Focusing-on-Controllable-Components = 143

count of Evaluating-the-Formulation = 81

AEROBA>

Now, please type (quit) after the prompt > to finish this session!

Thank you for your cooperation.

BYE-BYE!

## Appendix C. Diet problem

A hospital dietitian must prepare breakfast menus for the hospital patients. Part of the dietitian's responsibility is to make certain that minimum daily requirements for vitamins A and B are met. At the same time, the menus must be kept at the lowest possible cost to avoid waste. The minimum requirements for vitamin-A is 16 mg per day and that for vitamin B is 12 mg per day. The main breakfast staples providing vitamins A and B are eggs, bacon, and cereal. The vitamin contributions for the staples are listed below.

<table><tr><td colspan="4">Vitamin contribution (mg/unit of staple)</td></tr><tr><td>Vitamin</td><td>Egg</td><td>Bacon</td><td>Cereal</td></tr><tr><td>Vitamin A</td><td>2</td><td>4</td><td>1</td></tr><tr><td>Vitamin B</td><td>3</td><td>2</td><td>1</td></tr></table>

The cost of an egg is 4 cents, the cost of a bacon strip is 3 cents, and a cup of cereal costs 2 cents. The dietitian wants to know how much of each staple to serve to meet the minimum daily requirements while minimizing total cost.

## Appendix D. Aeroba consultation session for the diet problem

>(load 'aeroba')

AEROBA> Now, the AEROBA system is loaded and ready to help you to formulate linear programming (LP) models. During the formulation process, you have to read the problem description carefully and answer all questions prompted by the system. The answers can be in UPPER CASE, lower case, or a combination of both. For most questions, you have the option to ask 'What' and/or 'Why' for explanation. In addition to prompting questions, AEROBA will generate some information to help you understand the formulation process being conducted. Now, please type FORMULATE to start the process.

USER-RESPONSE> FORMULATE

AEROBA> Which problem domain are you working on (ProdPlan Auditing Forecasting)? [Enter data, What, or Why]

ANSWER-TO-WHAT> ProdPlan means Production Planning that is the activity of establishing production goals to meet stated production requirements or to take advantage of potential sales opportunities. Notice that the current system only addresses Production Planning problems. Please type in ProdPlan for this question.

ANSWER-TO-WHY> The system framework allows the formulation of models in the areas of production planning, auditing, and forecasting. However, the current implementation only addresses production planning problems.

## USER-RESPONSE> ProdPlan

AEROBA> Based on the opportunistic problem solving behavior observed from the expert modeler, AEROBA will not follow a particular process to perform various formulation tasks. You may be prompted with a question out of your expectation. Don't be surprised! Just follow AEROBA's thinking process and read the problem description carefully to find the answer. Now, AEROBA starts the formulation process by first focusing on the task of classifying-the-problem.

Classification task begins...

AEROBA> Is it a Product Transformation (PT) OR Resource Allocation (RA) problem? [Enter data What or Why]

ANSWER-TO-WHAT> If the problem is related to transforming product(s) from source(s) to destination(s), then answer PT. If the problem is relevant to allocating resource(s) such as personnel assignment or capital budgeting, then answer RA.

ANSWER-TO-WHY> While the classification is being performed, AEROBA requests information to classify the type of problem you are dealing with. You will be prompted with a series of questions until a problem type is identified.

## USER-RESPONSE> PT

AEROBA> Which type of product transformation is involved in your problem (PLACE TIME FORM)? [Enter data, What, or Why]

ANSWER-TO-WHAT> Please identify one major type of product transformation involved in this problem and select an answer from the parenthesis. Hint: If the problem involves shipping products from one place to another, then answer PLACE. If the problem involves storing product(s) at one time to be used at another time, then answer TIME. If the problem involves generating some outcomes from input resources, then answer FORM.

ANSWER-TO-WHY> same as the last answer-to-why

USER-RESPONSE> Form

AEROBA> Are the decisions for the Inputs (IN) or Outcomes (OUT) of the transformation?

ANSWER-TO-WHAT> If the decisions to be made are for the input resources of the product transformation, then answer IN. If they are made for the outcomes of the transformation, then answer OUT.

ANSWER-TO-WHY> same

USER-RESPONSE> IN

AEROBA> Are the outcomes Nutrients (NT) or Components (CP)?

ANSWER-TO-WHAT > If the outcomes generated from the product transformation are nutrients, then answer NT. If they are components other than nutrients, then answer CP.

ANSWER-TO-WHY> same

USER-RESPONSE> NT

AEROBA> Now, AEROBA classifies the problem type as DIET Problem. AEROBA will now perform other formulation tasks alternatively, such as decomposing-the-problem, setting-the-goal, and delineating-the-problem. AEROBA will perform these tasks internally without user interaction except to collect more problem feature or data from you. These tasks are to construct an internal representation and a LP structure for the problem.

Formulation continues...

AEROBA> Please enter all of the data for DT.NAME (separated by a space)

ANSWER-TO-WHAT> DT.NAME stands for Diet-Names that specify what diets are used to provide nutrients.

ANSWER-TO-WHY> While recognizing that certain types of attributes have been established as part of the problem structure, AEROBA interrupts the current formulation process and requests data from you.

USER-RESPONSE> Egg Bacon Cereal

AEROBA> Please enter all of the data for NT.NAME (separated by a space)

ANSWER-TO-WHAT> NT.NAME stands for Nutrient-Names that specify what nutrients are contained in the diets.

ANSWER-TO-WHY> same

USER-RESPONSE> VIT-A VIT-B

AEROBA> Please enter data for NT.REQ of VIT-A

ANSWER-TO-WHAT> NT.REQ stands for Nutrient-Requirement that specifies the requirement of a specific nutrient.

ANSWER-TO-WHY> same

USER-RESPONSE> 16

AEROBA> Please enter the constraint for NT.REQ of VIT-A (<=>==)

USER-RESPONSE> > =

AEROBA> Please enter data for NT.REQ of VIT-B

ANSWER-TO-WHAT> same as the last answer-to-what.

AEROBA> Please enter the constraint for NT.REQ of VIT-B (<=>==)

USER-RESPONSE> > =

AEROBA> Please enter data for DT.COST of EGG [Enter data what why]

USER-RESPONSE> 12

ANSWER-TO-WHAT> DT.COST stands for Unit-Diet-Cost that is the cost involved by using one unit of diet.

ANSWER-TO-WHY> same

ANSWER-TO-WHY> same

USER-RESPONSE> 4

AEROBA> Please enter data for DT.COST of BACON [Enter data what why]

ANSWER-TO-WHAT> same

ANSWER-TO-WHY> same
USER-RESPONSE> 3

AEROBA> Please enter data for DT.COST of CEREAL [Enter data what why]

ANSWER-TO-WHAT> same

ANSWER-TO-WHY> same

USER-RESPONSE> 2

AEROBA> Please enter data for CN.RATE of (EGG VIT-A) [Enter data what why]

ANSWER-TO-WHY> same

ANSWER-TO-WHAT> CN.RATE stands for containing rate that specifies the amount of nutrient contained in one unit of diet.

USER-RESPONSE> 2

AEROBA> Please enter data for CN.RATE of (EGG VIT-B) [Enter data what why]

ANSWER-TO-WHAT> same

ANSWER-TO-WHY> same

USER-RESPONSE> 3

AEROBA> Please enter data for CN.RATE of (BACON VIT-A) [Enter data what why]

ANSWER-TO-WHAT> same

ANSWER-TO-WHY> same

USER-RESPONSE> 4

AEROBA> Please enter data for CN.RATE of (BACON VIT-B) [Enter data what why]

ANSWER-TO-WHAT> same

ANSWER-TO-WHY> same

USER-RESPONSE> 2

AEROBA> Please enter data for CN.RATE of (CEREAL VIT-A) [Enter data what why]

ANSWER-TO-WHAT> same

ANSWER-TO-WHY> same

USER-RESPONSE> 1

AEROBA> Please enter data for CN.RATE of (CEREAL VIT-B) [Enter data what why]

ANSWER-TO-WHAT> same

ANSWER-TO-WHY> same

USER-RESPONSE> 1

AEROBA> Formulation Completed.

The AEROBA formulation for this problem is shown below.

Objective Function:

Minimize Total Cost = 4 \* (DT.QTY. EGG) + 3 \* (DT.QTY. BACON) + 2 \* (DT.QTY. CEREAL)

Subjected to:

$2*(\text{DT.QTY. EGG}) + 4*(\text{DT.QTY. BACON}) + 1*(\text{DT.QTY. CEREAL}) > = 16$

$3*(\text{DT.QTY. EGG}) + 2*(\text{DT.QTY. BACON}) + 1*(\text{DT.QTY. CEREAL}) > = 12$

(DT.QTY. EGG) $> = 0$ , (DT.QTY. BACON) $> = 0$ , (DT.QTY. CEREAL) $> = 0$

## References

[1] J.J. Elam, B. Konsynski, Using artificial intelligence techniques to enhance the capabilities of model management systems, Decision Sci. 18 (1987) 487–502.

[2] J.S. Gero, Design prototypes: a knowledge representation schema for design, AI Magazine 11 (4) (1990) 26–36.

[3] T.R. Willemain, Model formulation: what experts think about and when, Oper. Res. 43 (6) (1995) 916–932.

[4] B. Hayes-Roth, A blackboard architecture for control, Artificial Intelligence 26 (1985) 251–321.

[5] S. Ba, K.R. Lang, A.B. Whinston, Enterprise modeling and decision support, Proceedings of 1993 Pan Pacific Conference on Information Systems, k1–k12.

[6] M. Binbasioglu, M. Jarke, Domain specific DSS tools for knowledge-based model building, Decision Support Systems 2 (1986) 213–223.

[7] R.H. Bonczek, C.W. Holsapple, A.B. Whinston, A generalized decision support system using predicate calculus and network data base management, Oper. Res. 29 (2) (1981) 263–281.

[8] R. Krishnan, A logic modeling language for automated model construction, Decision Support Systems 6 (2) (1990) 123–152.

[9] T.P. Liang, Development of a knowledge-based model management system, Oper. Res. 36 (6) (1988) 849–863.

[10] F.H. Murphy, E.A. Stohr, An intelligent system for formulating linear programs, Decision Support Systems 2 (1) (1986) 39–47.

[11] R. Santhanam, M.J. Schniederjans, A model formulation system for information system project selection, Computers Oper. Res. 20 (7) (1993) 755–767.

[12] J.A. Barnett, Some issues of control in expert systems, IEEE Cybernetics and Society (1982) 1–5.

[13] W. Orlikowski, V. Dhar, Imposing structure on linear programming problems: an empirical analysis of expert and novice models, Proceedings of National Conference on Artificial Intelligence, Philadelphia (1986) 308–315.

[14] S. Raghunathan, MODFORM: a knowledge-based tool to support the modeling process, Information Systems Res. 4 (4) (1993) 331–358.

[15] M.V. Johnson Jr., B. Hayes-Roth, Integrating diverse reasoning methods in the BBI blackboard control architecture, Proceedings of the National Conference on Artificial Intelligence (1987) 30–35.

[16] T.J. Van Roy, Solving mixed integer programming problems using automatic reformulation, Oper. Res. 35 (1) (1987) 45–57.

[17] D. Dolk, B. Konsynski, Knowledge representation for model management systems, IEEE Trans. Software Engrg. 10 (6) (1984) 1–8.

[18] R. Lazimi, A generic shell approach for knowledge elicitation and representation in IDSS, Proceedings of the Eighth International Conference on Information Systems, Pittsburgh, PA (1987) 335–351.

[19] M.V. Mannino, B.S. Greenberg, S.N. Hong, Knowledge representation for model libraries, Proceedings of the Twenty-Second Annual Hawaii International Conference on System Sciences, Vol. III, Decision Support and Knowledge-Based Systems Track (1988) 349–355.

[20] A. Dutta, A. Basu, An artificial intelligence approach to

model management in decision support systems, IEEE Computer 17 (9) (1984) 89–97.

[21] J. Fedorowicz, G.D. Williams, Representing modeling knowledge in an intelligent decision support system, Decision Support Systems 2 (1) (1986) 3–14.

[22] V. Dhar, H.E. Pople, Rule-based versus structure-based models for explaining and generating expert behavior, Commun. ACM 30 (6) (1987) 542–555.

[23] V. Dhar, On the plausibility and scope of expert systems in management, J. Management Info. Sys. 4 (1) (1987) 25–41.

[24] T.P. Liang, C.V. Jones, Meta-design considerations in developing model management systems, Decision Sci. 19 (1988) 72–92.

[25] A.S. Vinze, A. Sen, S.T. Liou, Operationalization of opportunistic behavior in model formulation, Int. J. Man-Machine Studies 38 (1993) 509–540.

[26] A. Sen, A.S. Vinze, S.T. Liou, Role of control in the model formulation process, Information Systems Res. 5 (3) (1994) 219–248.

[27] B. Hayes-Roth, F. Hayes-Roth, A cognitive model of planning, Cognitive Sci. 3 (1979) 275–310.

[28] R.L. Ackoff, The art and science of mess management, Interfaces 11 (1) (1981) 20–26.

[29] H. Mintzberg, D. Raisinghani, A. Theoret, The structure of ‘unstructured’ decision processes, Administrative Sci. Q. 21 (1976) 246–275.

[30] I.I. Mitroff, J.R. Emshoff, R.H. Kilmann, Assumptional analysis: a methodology for strategic problem solving, Management Sci. 25 (6) (1979) 583–593.

[31] G.F. Smith, Toward a heuristic theory of problem structuring, Management Sci. 34 (12) (1988) 1489–1506.

[32] R.J. Volkema, Problem formulation in planning and design, Management Sci. 29 (6) (1983) 639–652.

[33] H.P. Nii, Blackboard systems: the blackboard model of problem solving and the evolution of blackboard architectures, AI Magazine (1986) 38–53.

[34] F. Hayes-Roth, V.R. Lesser, Focus of attention in the Hearsay-II speech understanding system, Proc. of Int. Joint Conference on Artificial Intelligence, 77 (1977) 27–35.

[35] H.P. Nii, E.A. Feigenbaum, J.J. Anton, A.J. Rockmore, A signal-to-symbol transformation: HASP/SIAP case study, AI Magazine (1982) 23–35.

[36] A. Terry, The CRYSALIS project: hierarchical control of production systems, Technical Report HPP-83-19, Heuristic Programming Project, Stanford University (1983).

[37] H. Laasri, B. Maitre, Flexibility and efficiency in blackboard systems: studies and achievements in ATOME, in: V. Jagannathan, R. Dodhiawala, L.S. Baum (Eds.), Blackboard Architectures and Applications, Academic Press (1989) 309–322.

[38] C.D.B. Boyle, Knowledge acquisition in expert systems: learning in a blackboard environment, Dissertation, Queen Mary College, UK (1987).

[39] R. Isenberg, Comparison of BB1 and KEE for building a production planning expert system, Proceedings of the Third International Expert Systems Conference, London (1987).

[40] C. Popp, Answering WHY? HOW? and WHY-NOT? questions in blackboard systems, Proceedings of the Eighth European Conference on Artificial Intelligence (1988).

[41] E.H. Durfee, V.R. Lesser, Incremental planning to control a blackboard-based problem solver, Proceedings of the Fifth National Conference on Artificial Intelligence (1986) 58–64.

[42] D.D. Corkill, V.R. Lesser, E. Hudlicka, Unifying data-directed and goal-directed control: an example and experiments, Proceedings of the National Conference on Artificial Intelligence, Pittsburgh PA (1982) 143–147.

[43] A. Sen, A. Vinze, C.D.B. Boyle, S.T. Liou, Mapping the entity relationship model to a blackboard architecture, Proceedings of AAAI-90 Workshop on Blackboard Systems, Boston, MA (1990).

[44] A. Sen, A.S. Vinze, S.T. Liou, Construction of a model formulation consultant: the AEROBA experience, IEEE Transactions on Systems, Man, and Cybernetics, 22 (5) (1992–1993) 1220–1232.

[45] A.S. Vinze, A. Sen, S.T. Liou, AEROBA: a blackboard approach to model formulation, J. Management Info. Sys. 9(3) (1992) 123–143.

[46] K.A. Ericsson, H.A. Simon, Protocol analysis: verbal reports as data, MIT Press, Cambridge, M.A. (1984).

[47] M.J. Bouwman, Human diagnostic reasoning by computer: an illustration from financial analysis, Management Sci. 29(6) (1983) 653–672.

[48] S.T. Liou, AEROBA: a control blackboard approach for model formulation, Dissertation, Texas A&M University (1992).

[49] A.S. Vinze, Knowledge-based support for software selection in information centers: design criteria, development issues, and empirical evaluation. Dissertation, University of Arizona, 1988.

![](/api/attachments/WGMU6KH4/fulltext/images/b0a0c11444afdc76d29431332e29dc2503d801880ec6e06e1243960854aa896b.jpg)

Shu-Feng Tseng, also known as Shue-Feng Tzeng Liou, is an associate professor of National Chengchi University, Taipei, Taiwan. She received her BS in 1979 and MS in 1981 from National Taiwan University and worked in the Data Processing and Audit Center of Ministry of Finance of ROC. from 1982 to 1984. She received another MS in Business Computing Sciences in 1986 and her PhD in Business Analysis (MIS) in 1992 from Texas A&M University.

Her research interests are Intelligent Decision Support Systems, Executive Information Systems, Banking Information Systems, and Software Reengineering Issues. She has published in IEEE Transactions on Systems, Man, and Cybernetics, International Journal of Man-Machine Studies, Proceedings of the Hawaii International Conference on System Sciences, and Proceedings of the Research Projects Conference of National Science Foundation of ROC.
