---
otero_id: 17199
otero_key: "9C592DKP"
title: "Adapting the behavior of a job-shop scheduling system"
authors: "Anne Collinot; Claude Le Pape"
year: "1991"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(91)90063-h"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Adapting the behavior of a job-shop scheduling system

Anne Collinot and Claude Le Pape

Department of Computer Science, Stanford University, Stanford, CA 94304, USA

Factory scheduling consists in assigning resources (e.g. machines) and start and end times to operations. Our work is concerned with the problems of schedule generation and schedule revision when unanticipated events occur on the factory floor. SONIA is a knowledge-based scheduling system provided with a blackboard architecture for coordinating the activation of various scheduling and analyzing knowledge sources. In this paper, we focus on the various behaviors these knowledge sources can have and we gather a collection of conclusions regarding the use of various backtracking strategies and the control of constraint propagation.

Keywords: Dynamic scheduling problems, Blackboard system, Heuristic search, Constraint propagation, Backtracking strategies.

![](/api/attachments/9C592DKP/fulltext/images/676a4ea867202b6f93ad64af08f54e7a65650a35fda3117b1c0a2127bb147931.jpg)

![](/api/attachments/9C592DKP/fulltext/images/006c9927808b06034bae4c5e7a4b7d2e872cda0e9fe3fd5f3f4b8c19bf4d7c95.jpg)

Anne Collinot is a visiting researcher in the Knowledge Systems Laboratory at Stanford University. Her main interests are the design of cognitive architectures, the control of multiple reasoning tasks and the real-time performance of knowledge-based systems. She received a D.E.A. (Master) in Computer Science from University Paris VI in 1985, and a PhD in Computer Science from University Paris VI in 1988.

Claude Le Pape is a visiting researcher in the Robotics Laboratory at Stanford University. His main interests are constraint propagation, knowledge base consistency checking and the application of symbolic reasoning techniques to manufacturing and engineering problems. He received a D.E.A. (Master) in Computer Science from University Paris XI in 1984, and a PhD in Computer Science from University Paris XI in 1988. He also attended "Ecole Normale Supérieure

de Paris" from 1982 to 1987 and received a management degree from "Collège des Ingénieurs" in 1988.

## Introduction

Important features of factory scheduling problems vary from one shop to another. In the same shop, they also vary from one situation to another. For example, the variation of the duration of operations depends on the manufactured products, and the importance of bottleneck resources varies with the global load of the shop. Consequently, it is necessary to choose relevant scheduling strategies with respect to the problem-solving context. In this paper, we present a knowledge-based scheduling system designed to test and compare various reactive scheduling strategies in various circumstances $[6,9]$ . This system, SONIA, is provided with a BB1-like blackboard architecture $[14]$ for coordinating the activation of various scheduling and analyzing knowledge sources. Most of the knowledge sources of SONIA are flexible. This means the behavior of these knowledge sources can be adjusted with respect to the problem-solving context. We investigate and discuss the various behaviors scheduling and analyzing knowledge sources can have and gather a collection of conclusions regarding the use of various backtracking strategies and the control of constraint propagation $[4]$ .

## 1. The job-shop scheduling problem

Basically, scheduling is the allocation of resources over time to perform a collection of tasks. Scheduling theory [1] provides us with a collection of principles, models and techniques. However, their application is somewhat limited. Indeed, the job-shop scheduling problem is known to be NP-complete [2,3,13]. Much of Artificial Intelligence is involved with the development of techniques to handle NP-complete problems. In particular, opportunistic reasoning is necessary for a job-shop scheduling system to provide a satisfactory schedule in the context of actual shop floors [16,21,24].

We consider scheduling as a decision-making process – the process of determining a schedule. A variety of constraints affect this process. Scheduling decisions have to satisfy pure constraints: release dates, operation durations and precedences, transfer and set-up times, resource availability constraints (shifts, down time) and sharing of resources. These restrictions define the space of admissible solutions. Furthermore, relaxable constraints characterize the quality of scheduling decisions. These preferences are related to due-dates, productivity, frequency of tool changes, inventory levels, shop stability. They lead to priority relations between manufacturing orders, alternative production routings, manufacturing operations and alternative resources. Since preference constraints may conflict with one another, the scheduling problem also consists in deciding which preferences should be satisfied and to what extent others should be relaxed.

In the context of manufacturing, two problems can be distinguished. Predictive scheduling consists in building a schedule to be executed in the future. For example, given the state of the shop in the evening, it may be worth selecting and scheduling operations to be performed the next day. Real-time reactive scheduling consists in making scheduling decisions in real-time with respect to the actual state of the shop. This does not mean every decision is made in real-time, but previous decisions are confronted with unexpected events (e.g. machine breakdown, operation tardiness, reworking). Obviously, a reactive scheduling system is all the more useful as the shop floor is a dynamic environment where unforeseeable events occur. A predictive scheduling system is not absolutely necessary, but its usefulness may be significant: because it is not subjected to real-time constraints, computational time can be spent satisfying preference constraints and ensuring the global quality of the solution.

Section 2 presents SONIA, a reactive job-shop scheduling system which integrates various knowledge sources. Section 3 is devoted to controlling the behavior of these knowledge sources. Section 4 describes some of our experiments with the system, regarding the use of various backtracking strategies and the control of constraint propagation.

## 2. Overview of SONIA

SONIA [5,8] is a knowledge-based job-shop scheduling system designed to detect and react to inconsistencies between a schedule and the actual events on a shop floor. The system is built on a BB1-like blackboard architecture [14]. It is provided with both predictive and reactive scheduling knowledge sources which are used to build and modify schedules. Analyzing knowledge sources can be employed to evaluate both predictive and reactive problem-solving contexts. Control knowledge sources may use analysis results to choose the most appropriate knowledge sources to execute and determine which “behavior” the scheduling knowledge sources should adopt (e.g. which heuristics they should use). A schedule management system (built on a flexible constraint propagation system which allows tuning of the trade-off between the anticipation of inconsistencies and the cost of propagation) is used to update schedule descriptions and detect inconsistencies as scheduling knowledge sources make decisions and unexpected events happen on the shop floor.

In section 2.1, we first call attention to the management of schedule descriptions. Next, we overview the various knowledge sources which make up the whole SONIA system: predictive and reactive scheduling knowledge sources (section 2.2), analyzing knowledge sources (section 2.3), knowledge sources constituting interfaces between SONIA and the real world (section 2.4) and control knowledge sources (section 2.5). Figure 1 shows an overview of the SONIA system (more detailed descriptions of knowledge sources of the SONIA system can be found in [5] and [7]).

## 2.1. Management of schedule descriptions

Within SONIA a shop schedule is represented as a set of resources, manufacturing orders and operations to which various kinds of constraints are attached. As in the ISIS $[11,12]$ and OPIS $[15,24]$ scheduling systems, resources are described at various levels of abstraction. At each level, time-tables composed of reservation constraints are associated with resources. To each manufacturing order are associated a release date, a due-date and a production plan represented as a hierarchy of operations. An actual-status and a schedule-status are defined for each operation:

they indicate whether the operation is completed, in-process or ignored (i.e. not started) on the shop floor and whether it is scheduled, selected or ignored by SONIA. Temporal constraints are generated in accordance with the status information.

The schedule management system is responsible for evaluating the consequences of both (1) decisions made by the various scheduling knowledge sources (or by the user of the system) and (2) unexpected events happening on the shop floor. Decisions are related to status of operations, release dates, due-dates and resource capacity (e.g. work shifts, resource sharing). Unexpected events are machine breakdowns and delays. The schedule management system is used to create reservation constraints or temporal constraints (e.g. temporal inequalities or disjunctions of temporal inequalities) [5,17] according to the type of scheduling decisions or shop floor events. These constraints are then passed to a propagation system.

Constraint propagation is a deductive activity which consists in deriving new constraints from existing ones. Such a technique is used in SONIA for two reasons: (1) some derived constraints, like time bound constraints, are very useful data; (2) constraint propagation enables the detection of inconsistencies between decisions and events happening on the shop floor. When an inconsistency is detected, an appropriate description of the conflict is built. According to the conflicting constraints, a conflict belongs to one or more of the following categories: the delays category gathers all the conflicts that result from unexpected delays (for example, a global tardiness conflict states that since some operations have begun or ended later than expected on the shop floor, it is impossible to perform all of the selected operations during the open work shifts); the capacity conflicts category gathers all the conflicts involving reservation constraints (for example, an out-of-shift conflict means that a resource is allocated to an operation outside of its work shifts); the breakdowns category is composed of delays and capacity conflicts caused by machine breakdowns.

![](/api/attachments/9C592DKP/fulltext/images/3fd69f936c34655e9a8de663729273b2d731dc231efc415f064a7b84927d916d.jpg)  
Fig. 1. An overview of SONIA.

![](/api/attachments/9C592DKP/fulltext/images/890c60f7094cdd0937b66dda41dd461a4170845d1288aaabc2daa8ed2fbf017c.jpg)  
Fig. 2. Controlling constraint propagation.

Unfortunately, constraint propagation is a time consuming activity; complete propagation – which guarantees consistency – is prohibitive for complexity reasons $[16]$ . Our experience led us to believe that the amount of propagation that enables a scheduling system to be most efficient varies from one shop to another (e.g. in a shop floor with only one major bottleneck, it is possible to combine disjunctive (resource sharing) constraints related to the bottleneck resource; this is obviously not reasonable when the whole shop is considered as over-loaded) and, in the same shop, from one problem-solving context to another (e.g. in case of emergency, it may be necessary not to evaluate all of the consequences of reactive decisions). Consequently, we developed a flexible constraint propagation system which allows tuning of the trade-off between the anticipation of inconsistencies and the cost of propagation $[4]$ . It is composed of a theory and an interpreter (figure 2).

The theory consists of propagation axioms which indicate how constraints can be combined. The interpreter uses the axioms consistently with control rules which collectively specify what is expected from the propagation system. Dynamically setting the control rules enables the adjustment (to the needs of a problem-solver) of the trade-off between the anticipation of conflicts and the amount of processing time assigned to constraint propagation. The flexibility of the constraint propagation system has a significant impact on the ability to modify the behavior of a knowledge source (cf. section 3.2).

## 2.2. Predictive and reactive scheduling knowledge sources

SONIA is able to perform five distinct domain problem-solving tasks. Each of them corresponds to the implementation of a scheduling knowledge source. In this section, we briefly present these scheduling knowledge sources.

## Global selection

The Selection knowledge source is used to choose a set of operations to be performed during the open work shifts and to assign resources to them. More precisely, this knowledge source is employed when resources are under-loaded. Operations which require the use of such resources are then selected. Operations are selected according to the capacity of these resources. Heuristics are used to determine which operations should be performed. These heuristics can vary with both the shop and the problem-solving context. For example, it may be interesting to give priority to manufacturing orders for which the remaining processing time required for achievement is important compared to the remaining time made acceptable by the due-date of the order. In some cases, it may be more profitable to take into account other scheduling criteria such as minimizing tool changes. When an operation is selected, its schedule-status is modified and the relevant constraints are created and propagated by the schedule management system.

## Order selection

The Order Selection knowledge source is employed to select operations which belong to the same production plan (in previous versions of SONIA [5], this knowledge source was also responsible for scheduling these operations; it was called “Order Scheduler”). It selects operations one after the other and stops as soon as an operation cannot be selected within the open work shifts. This component is often used when operations have been discarded by the Rejection component. This allows improvement of the schedule.

## Ordering

The Ordering knowledge source is used to make ordering decisions when disjunctive constraints (e.g. resource sharing) must be satisfied. It consists of an iterative constraint satisfaction process: disjunctive constraints which characterize the various orders in which operations can be performed are satisfied by choosing underlying temporal inequalities. At each iteration, heuristics are used to make ordering decisions which are propagated through the schedule management system. Various backtracking procedures can be invoked when some ordering free decisions (as opposed to imperative decisions) are conflicting with other constraints. These procedures select one of the conflicting free decisions to be rejected; the effects of this decision are undone by the means of the schedule management system and the reverse ordering decision is made as an imperative decision (forced by the other conflicting decisions); then the process re-starts. The constraint satisfaction process fails when a conflict is derived from imperative decisions. When the Ordering knowledge source fails (for instance, when too many operations have been selected by the Selection knowledge source), some of the less important operations are rejected by the Rejection knowledge source.

## Rejection

The Rejection knowledge source is responsible for rejecting selected operations. It is employed when the Ordering knowledge source fails or when unexpected events prevent from executing the whole predictive schedule. It uses heuristics to choose the operations to be rejected among the operations involved with conflictual situations. When an operation is rejected, its schedule-status is set back to ignored; constraints and conflicts concerning this operation are consequently removed by the schedule management system.

## Global re-scheduling

The Global Re-Scheduling knowledge source is used in order to process and modify the whole plan forward from the current date. Its process rests upon the fact that any deviation can eventually be expressed by precise delays associated with resources. The forward propagation of these delays results in conflicts relating to due-dates or to ends of work shifts, which can be solved by relaxing due-dates, extending work-shifts or rejecting operations. However, if processing time is available (i.e. if it is not necessary to correct the plan in a few seconds), it is worth reducing resources idle times by permuting operations. Consequently, two strategies are available. The first one consists of a simple right shifting strategy: for each resource, the operations to be performed remain in the same order and the schedule is moved forward from the current date. The other strategy allows permutations in order to optimize the plan and to reduce the effects of the original delay. In any case, when an operation cannot be performed within a shift, heuristics are used to determine whether the shift is extended or whether the operation is discarded or postponed until the next shift.

## 2.3. Analyzing knowledge sources

Analyzing tasks have been proved useful for improving scheduling problem-solving (e.g. [10,16,24]). For example, the detection of bottleneck and under-loaded resources (capacity analysis) enables improvement of the problem-solving task achieved by the Ordering knowledge source (cf. section 3.1). Similarly, an analysis of conflicts detected by the schedule management system allows to improve the use of reactive scheduling knowledge sources to correct the current schedule. In this section, we briefly present two knowledge sources responsible for achieving each of these analyzing tasks.

## Capacity analysis

The Capacity Analyzer is used to detect both bottleneck and under-loaded resources. As the shop-level capacity analyzer of the OPIS system $[24]$ , it divides the time-line into time periods and determines both the available capacity and the demand over each period for each considered resource. Capacity and demand are computed from the existing reservations and by building a rough predictive schedule (which is discarded once the analysis is achieved) for selected operations.

## Analysis of conflicts

The Analyzer of Conflicts is used to examine in details a set of conflicts in order to determine appropriate reactions. The analysis results in various proposals in order to solve all or some of the contemplated conflicts. Very simple rules are applied in order to determine which, and how, available reactive components should be used. For example, when several global tardiness conflicts are to be solved, it is recommended to use the Global Re-Scheduler knowledge source. Conversely, it is more appropriate to use the Rejection knowledge source in order to quickly solve an isolated global tardiness conflict. Of course the default strategy which consists in using the Global Re-Scheduler is always considered. In addition, heuristics can be used to focus the analysis on a particular category of conflicts or on conflicts related to a given work-area or manufacturing order.

## 2.4. Interfaces between SONIA and the real world

Three knowledge sources are used as interfaces between SONIA and the shop floor.

## User interface

The User Interface allows the user of the system to build and to update schedules. More precisely, the system allows:

\- to select and reject operations;

\- to order and permute operations;

\- to cut operations (e.g. pre-emption);

\- to allocate a resource to an operation over an interval of time;

\- to add and delete work shifts;

\- to update release dates and due dates;

\- to add and delete any unusual constraint which can be expressed in the underlying constraint language [17].

After each decision (or modification of original data), the user can activate the constraint propagation system and visualize the results in the form of a Gantt chart (e.g. figure 3).

## Schedule application

The Schedule Application knowledge source provides the user of the system (e.g. the shop floor manager) with a schedule generated or corrected by the predictive or reactive scheduling knowledge sources of SONIA. It is called each time a new (updated) schedule is considered acceptable.

## Execution controller

The Execution Controller informs the schedule management system about the actual course of events in the shop floor (i.e. the schedule execution with regard to unexpected events).

## 2.5. Control knowledge sources

SONIA is built upon a BB1-like blackboard architecture for both coordinating the contribution of the various knowledge sources and adjusting their behavior according to the problem-solving context. Each time a knowledge source is involved in the problem-solving process, it generates events which are posted on the domain blackboard or on the control blackboard (or on both). The domain blackboard collects events related to the actual state and progress of the scheduling decision-making process. The control blackboard collects events related to the control decision-making process; for example, potential actions at each step of the problem-solving process are recorded at the To-Do-Set level of the control blackboard. Figure 4 shows the knowledge sources of SONIA with their triggering events and with the events they generate.

![](/api/attachments/9C592DKP/fulltext/images/85cf0899c6dfadd89d80a9baf23a4656340e7aac2236e6c1e680283ae9c0f5db.jpg)  
Fig. 3. A Gantt chart.

![](/api/attachments/9C592DKP/fulltext/images/ad9a0f9192f446a43a0ab6b374684ee8eb10af402ee419fc2085f9a3a140b3c7.jpg)  
Fig. 4. Knowledge sources of the SONIA system.

As in [14], three basic control knowledge sources are used to implement the basic control loop that runs the SONIA system. The basic control loop consists in (1) updating the To-Do-Set according to both domain and control blackboard modifications, (2) selecting a pending KSAR (Knowledge Source Activation Record) according to policies recorded on the control blackboard and (3) executing the selected KSAR. The three basic control knowledge sources Update-To-Do-Set, Choose-KSAR and Interpret-KSAR are respectively responsible for updating the To-Do-Set, choosing the next action to be performed and executing the chosen action.

In addition, two high-level control knowledge sources are employed to update heuristics used by scheduling knowledge sources (section 3.1) and to control the propagation of the consequences of scheduling decisions (section 3.2).

## 3. Controlling the behavior of knowledge sources within SONIA

During the design of the SONIA system, we considered various points of flexibility. This enables refinement of problem-solving tasks with regard to the problem-solving context. Within SONIA, a knowledge source is considered as a three-part knowledge component (figure 5): the condition part allows the knowledge source to know whether it can be active; the action part determines the events the knowledge source is going to produce and is defined by a partial procedure, i.e. a procedure where there still are choices to be made; the behavior part defines flexible points which can be dynamically set to complete the partial procedure. Four control issues are considered: adjusting the set of heuristics used by a knowledge source with regard to the problem-solving context (section 3.1), controlling constraint propagation (section 3.2), choosing among various backtracking strategies (section 3.3), using preference constraints as restrictions (section 3.4).

![](/api/attachments/9C592DKP/fulltext/images/f3f2e186a70267a4729cae1a9c1cadfd0d9fe3df5b218822c8b5d8fef406251a.jpg)  
Fig. 5. A knowledge source as a three-part knowledge component.

## 3.1. Adjusting the set of heuristics used by a knowledge source

Calling attention to the heuristics a knowledge source can use leads to considering a knowledge source as a search procedure $[16,20]$ . Obviously, the search procedure varies with the heuristics: adjusting heuristics to encountered problem-solving contexts enables the improvement of problem-solving. For example, the EDD (Earliest Due Date) priority rule $[27]$ , which consists in selecting and scheduling operations of the most urgent orders first, produces satisfactory results with respect to due-date constraints provided that the shop is not over-loaded. When the shop is overloaded (i.e. one cannot prevent the relaxation of many due-dates), this priority rule is known to provide poor results and should not be applied. Similarly, the heuristic which recommends to schedule the most critical resources first is more or less relevant, depending on the irregularities in resource loading (bottleneck and under-loaded resources). Information about irregularities in resource loading is produced by the Capacity Analyzer. The Controller of Heuristics can use this information to activate or de-activate the heuristics accordingly. This makes the behavior of the Selection and Ordering knowledge sources more appropriate.

## 3.2. Controlling constraint propagation

The flexibility of the constraint propagation system enables adjustment of the amount of propagation performed in evaluating the consequences of scheduling decisions. When the amount of propagation is reduced, a knowledge source has either to explore the search space in order to find a satisfactory solution, or to run the risk of introducing potential conflicts (which will be detected later by other knowledge sources). When the amount of propagation is extended, a knowledge source can drastically prune the search space. The search procedure the knowledge source applies varies – from purely heuristic search methods to a least-commitment approach $[26]$ – with the amount of propagation. As shown in the following examples, the amount of propagation can be adapted according to a particular problem-solving task or to more general purposes.

## Controlling propagation to make a particular knowledge source more efficient:

\- The set of rules used by the propagation system can be modified by the Constraint Propagation Controller before the Capacity Analyzer knowledge source is activated. When the Capacity Analyzer builds its rough predictive schedule in order to evaluate the available capacity and the demand for each resource, it is not necessary to take into account constraints related to the use of resources. Indeed, the Capacity Analyzer focuses attention on operation time bound constraints (which state that a given operation cannot start or end before or after a given date). Furthermore, the decisions it makes do not need to be confronted to order due-dates or to end-of-work-shift constraints. The analysis will be all the more rapid as constraint propagation is reduced to a minimum required for a significant evaluation.

\- Conversely, it is worth increasing the amount of propagation before the Order Selection knowledge source is called. Indeed, this knowledge source only makes a few decisions related to a few operations. An extended propagation of the consequences of selection decisions virtually ensures (if no inconsistency is detected) that the selected operations can be scheduled.

Controlling propagation to make problem-solving globally more efficient:

It is also possible to control the propagation system for a more general purpose (i.e. not only for one particular knowledge source to be more efficient).

\- In case of emergency (e.g. when conflicts arising from unexpected delays are related to very important manufacturing orders), reactive decisions must be made without evaluating all of their consequences. Such an emergency context can be detected by the Analyzer of Conflicts. Then, the Constraint Propagation Controller can be activated in order to specify (through the control rules of the propagation system) that only constraints concerning “imminent” events need to be combined.

\- Propagating disjunctive constraints is time consuming and generally avoided. However, it may be worth taking a closer look at operations that require the use of a scarce resource. When scarce resources are identified by the Capacity Analyzer, the Constraint Propagation Controller can specify that disjunctive constraints (e.g. resource sharing) need to be combined only if the associated operations require these resources.

## 3.3. Various backtracking strategies

When a knowledge source fails (i.e. some decisions lead to an inconsistency), various strategies from “naive” chronological backtracking to sophisticated analyses of the failure (i.e. in order to avoid further failures and to cancel, not systematically the most recent decision, but the relevant decision [23]) can be considered. For example, when some ordering decisions (made by the Ordering knowledge source) lead to an inconsistency, two backtracking strategies are available. – The chronological backtracking strategy allows to backtrack immediately (without analyzing the failure). It recommends to consider decisions in reverse chronological order and to cancel all the decisions until the most recent decision involved in the inconsistency is removed.

\- The selective backtracking strategy recommends cancellation of an ordering decision if and only if the cancellation is absolutely necessary (in order to remove the inconsistency). This strategy prevents the system from cancelling (and further remaking) ordering decisions which are not directly responsible for the inconsistency. However, these decisions may have been made in order to satisfy a preference constraint in a context involving some of the inconsistent decisions. The selective backtracking strategy is often more rapid at the expense of the homogeneity (with regard to various scheduling criteria) of the solution. This means the selective backtracking strategy can be more or less relevant depending on the problem-solving context (importance of scheduling criteria, emergency, problem size).

Furthermore, possibilities of analyzing failures (i.e. inconsistencies) in order to gain information can be considered. The Ordering knowledge source can invoke an inconsistency processing procedure in order to record incompatibilities detected by the schedule management system. This avoids making the same mistake twice (i.e. making the same conflictual decisions twice). When some decisions $D_{1}\ldots D_{n}$ are conflictual with regard to a set of constraints $\{C_{1}\ldots C_{m}\}$ , it is possible to create a new constraint $(OR\ (NOT\ D_{1})\ldots(NOT\ D_{n}))$ and to maintain it as long as $C_{1}\ldots C_{m}$ are considered. The creation of such a constraint guarantees that the same inconsistency resulting from the decisions $D_{i}$ and the constraints $C_{j}$ will not be met again (provided that the amount of propagation is sufficient). However, it is worth noting that the cost of storing and exploiting incompatibilities may be more important than the resulting gain in search processing time.

## 3.4. Considering a criterion as a preference or as a restriction

A knowledge source may consider a preference constraint as a restriction. This means the knowledge source makes decisions in order to satisfy a preference constraint and carries on searching for a solution without relaxing this constraint (the knowledge source will fail if the constraint cannot be satisfied). This conveys a very high importance to criteria embedded in preference constraints. Conversely, when a preference constraint is not considered as a restriction (it can be relaxed), it is used merely as a heuristic to guide the search $[11,18]$ .

For example, the Global Re-Scheduler knowledge source can decide to systematically ignore schedules which cannot be obtained without cancelling previous ordering decisions. This means that a stability criterion is now considered as a restriction used to discard potential schedules as opposed to a preference constraint used to compare potential schedules. When the Global Re-Scheduler allows cancellation of ordering decisions, the re-scheduling process is less rapid but enables optimization of resource schedules.

## 4. Experiments

SONIA can be used with a simulator to investigate various reactive scheduling strategies.

\- Given a description of a shop floor, we can measure the utility of reactive scheduling, compared to the use of classical dispatching rules.

\- We can investigate the relevance and the efficiency of each knowledge source in various contexts (e.g. over-loaded shop, highly disrupted shop).

\- The behavior of scheduling and analyzing knowledge sources can be adjusted with respect to several control issues.

This section describes some of our experiments regarding the use of various backtracking strategies and the control of constraint propagation. [6] provides a detailed description of the results obtained so far and also discusses both the global utility of reactive scheduling and the efficiency of reactive methods implemented in the SONIA system. Note that the global utility of reactive scheduling has already been studied by other researchers (e.g. [19,28]). On the other hand, a lot of work regarding the relevance and the efficiency of various scheduling methods – based on multiple decompositions of scheduling problems – has been done at Carnegie-Mellon University [25,22].

## 4.1. Description of the experiments

Experiments regarding backtracking strategies and constraint propagation have been made (using a LISP-machine SYMBOLICS 3600) for three shop floors: an actual sheet-iron shop (23 machines, 100 to 150 operations per shift), a bottleneck area of this shop (6 machines, about 30 operations per shift) and a hypothetical shop obtained by doubling the capacity of this bottleneck area (12 machines, about 60 operations per shift). Figure 6 shows for each workshop the number of tests made, the number of shifts per test and the number of operations per shift. Shifts are 7 to 12 hours long. The demand/capacity ratio in the sheet-iron shop varies from 30% for under-loaded machines to 90% for bottleneck machines. In the two other shops, machines are equally loaded. The duration of operations varies from a few minutes to a few hours in the sheet-iron shop and from 45 minutes to 3 hours in the two other shops. Tool set-ups are costly (10 to 40 minutes). Unexpected events are delays, operation interruptions and mainly machine breakdowns. For each machine, breakdowns are generated with respect to a Poisson law the parameter of which is 2000 minutes. In most cases, the machine is unavailable for 90 minutes or less.

<table><tr><td>Workshop</td><td>Sheet-Iron Workshop</td><td>Bottleneck Area</td><td>Hypothetical Workshop</td></tr><tr><td>Number of Machines</td><td>23</td><td>6</td><td>12</td></tr><tr><td>Number of Tests</td><td>15</td><td>100</td><td>100</td></tr><tr><td>Number of Shifts</td><td>3.5</td><td>2.5</td><td>2.5</td></tr><tr><td>Number of Operations</td><td>100 to 150</td><td>30</td><td>60</td></tr></table>

Fig. 6. Experiments with three workshops.

Two backtracking issues are considered: (1) chronological or selective (dependency-directed) backtracking; (2) recording or not recording incompatibilities detected by the schedule management system (recording incompatibilities prevents the re-making of the same “mistakes”). Consequently, four backtracking strategies are available.

Similarly, a series of constraint propagation “scenarios” is defined with respect to the following issues:

\- Constraint propagation can be restricted to the determination of critical paths in a PERT-like graph [6]. This means disjunctive constraints are not considered by the constraint propagation system. On the contrary, the constraint propagation system can use a generalization of the resolution rule to confront temporal inequalities with disjunctions (in addition to the determination of critical paths). For example, if a machine is planned to be unavailable throughout the interval of time (68) and if an operation op must be performed on this machine without interruption, we can deduce $start(op) \geq 8$ from $end(op) \geq 7$ and (OR $(start(op) \geq 8)$ (end(op) ≤ 6)).

\- The schedule management system can either ignore or detect re-scheduling opportunities. For example, $end(op) \geq 7$ may disappear in the course of the simulation (because an operation preceding $op$ ends earlier than expected, thereby enabling $op$ to start earlier than expected). If no other constraint prevents $op$ from ending before 6, the schedule management system can then delete $start(op) \geq 8$ and signal an opportunity for re-scheduling $op$ .

\- We considered two well-known methods for updating critical paths as scheduling decisions are made. One of them consists in exploring the PERT-like graph. Its complexity is $O(n^3)$ in the worst case (where $n$ denotes the number of manufacturing operations considered within a shift). The other one consists in maintaining a matrix $M$ such that $M(i j)$ denotes the longest path from node $i$ to node $j$ in the graph. Its complexity is $O(n^2)$ .

\- When disjunctions of temporal inequalities are considered, we can use subsumption rules to “hide” disjunctions the satisfaction of which results from the satisfaction of other constraints (for example, $OR\ (start(op) \geq 8)\ (end(op) \leq 6)$ is subsumed by $start(op) \geq 10$ ).

\- For two knowledge sources of the SONIA system (Order Selection and Capacity Analyzer), we were able to design appropriate scenarios which were more efficient than others.

## 4.2. Results

As expected, selective backtracking strategies are in most cases more efficient than chronological backtracking strategies. However, extended constraint propagation often leads to a significant decrease in the number of backtracks. Consequently, the utility of selective backtracking is reduced (and sometimes reversed) when constraint propagation is extended. Similarly, the recording of incompatibilities is all the more useful as constraint propagation is reduced.

The system reacted more quickly to unexpected events when constraint propagation was restricted to the determination of critical paths (cf. figure 7). Globally, the quality of the schedule finally executed was not significantly altered by the absence (due to reduced propagation) of both early detection of conflicts and detection of scheduling opportunities. On the other hand, for predictive scheduling, the cost of an extended constraint propagation was balanced by a reduction of search in nearly 50% of the cases. In 90% of the cases, the exploration of the PERT-like graph was much more efficient than the matrix-based method (although it is $O(n^{3})$ against $O(n^{2})$ in the worst case). The cost of subsuming disjunctive constraints was hardly balanced by the resulting reduction of search: in 80% of the cases, subsumption did not enable to save more than 10% of the total (search + constraint propagation) time.

![](/api/attachments/9C592DKP/fulltext/images/6cf3b301497c5769e79f9cb29401ddf7d108447e58abbb94067235249a367e2c.jpg)  
Fig. 7. Reaction time.

![](/api/attachments/9C592DKP/fulltext/images/578b887feeaff14ae63971108631f5df15ae3ed7028649b580dfae017c922535.jpg)  
Fig. 8. Capacity analysis.

Providing propagation scenarios dedicated to two knowledge sources of the SONIA system turned out to be very worthwhile. By performing reduced propagation, the Capacity Analyzer was able to save 18% to 78% of its computational time while producing equivalent results (cf. figure 8). By performing extended propagation, the Order Selection knowledge source was able to immediately detect cases in which several operations of the same order could not be performed during the same shift without re-scheduling operations of other orders - thereby enabling the whole system to prune the search space.

## 5. Conclusion

Controlling the behavior of knowledge sources enables improvement of the efficiency of problem-solving. This paper stressed the various behaviors a knowledge source can have within SONIA. We proposed various points of flexibility that focus upon both the process of finding a solution and the consistency of the decisions made by knowledge sources: the set of heuristics used by a knowledge source can vary with the problem-solving context; the amount of propagation performed in evaluating the consequences of scheduling decisions can be adjusted through the control rules of the flexible constraint propagation system; when a knowledge source fails, various backtracking strategies can be considered; and, finally, a knowledge source can take a quality criterion into account either to discard potential solutions or to prefer some solutions to the others.

Such a decomposition of the flexibility of our system enables the focus of attention on distinct pieces of knowledge in order to improve the global efficiency of problem-solving. Given a description of a shop floor, one can use the SONIA system as a support for determining whether some scheduling strategies perform well in some contexts. A challenging problem is now to figure out how we can provide such a system with control knowledge to dynamically determine the most appropriate behavior of its knowledge sources. The definition of various points of flexibility within the system should facilitate the acquisition of this knowledge.

## Acknowledgements

The scheduling system and simulator discussed in this paper were developed by the authors and Gérard Pinoteau in Laboratoires de Marcoussis. Anne Collinot is now sponsored by INRIA and Claude Le Pape by Elf-Aquitaine.

## References

[1] K.R. Baker, Introduction to Sequencing and Scheduling (John Wiley and Sons, 1974).

[2] J.L. Bruno, E.G. Coffman Jr., R.L. Graham, W.H. Kohler, R. Sethi, K. Steiglitz and J.D. Ullman, Computer and Job-Shop Scheduling Theory (John Wiley and Sons, 1976).

[3] J. Carlier and P. Chrétienne, Problèmes d'ordonnancement: Modélisation/Complexité/Algorithms (Masson, 1988).

[4] A. Collinot and C. Le Pape, Controlling Constraint Propagation, in: Proceedings of the 10th International Joint Conference on Artificial Intelligence (1987).

[5] A. Collinot, C. Le Pape and G. Pinoteau, SONIA: a Knowledge-Based Scheduling System, International Journal for Artificial Intelligence in Engineering 3 (1988) 86–94.

[6] A. Collinot and C. Le Pape, Comparaison de plusieurs modes d'utilisation d'un système d'ordonnancement flexible (Comparison of various utilization modes of a flexible scheduling system), Laboratoires de Marcoussis (1988).

[7] A. Collinot, Le problème du contrôle dans un système flexible d'ordonnancement (The control problem in a flexible scheduling system), Thèse d'Université, Université Paris VI (1988).

[8] A. Collinot and C. Le Pape, Controlling the Behavior of Knowledge Sources within SONIA, in: Proceedings of the 22nd Hawaii International Conference on System Sciences (1989).

[9] A. Collinot and C. Le Pape, Testing and Comparing Reactive Scheduling Strategies, in: Proceedings of the AAAI-SIGMAN Workshop on Manufacturing Scheduling (1989).

[10] Y. Descotte and H. Delesalle, Une architecture de système

expert pour la planification d'activités (Architecture of a planning expert system), in: Proceedings of the 6th International Workshop on Expert Systems and their Applications (1986).

[11] M.S. Fox, Constraint Directed Search: a Case Study of Job-Shop Scheduling, PhD Thesis, Carnegie-Mellon University (1983).

[12] M.S. Fox and S.F. Smith, ISIS: a Knowledge-Based System for Factory Scheduling, Expert Systems 1 (1984) 25–49.

[13] M.R. Garey and D.S. Johnson, Computers and Intractability. A Guide to the Theory of NP-Completeness (W.H. Freeman and Company, 1979).

[14] B. Hayes-Roth, A Blackboard Architecture for Control, Artificial Intelligence 26 (1985) 251–321.

[15] C. Le Pape and S.F. Smith, Management of Temporal Constraints for Factory Scheduling, in: Proceedings of the Working Conference on Temporal Aspects in Information Systems (1987).

[16] C. Le Pape, Des systèmes d'ordonnancement flexibles et opportunistes (Flexible and opportunistic scheduling systems), These d'Université, Université Paris XI (1988).

[17] C. Le Pape, The Completeness of a Solution Maintenance Component, Working Paper, Stanford University (1989).

[18] J. Mostow and K. Voigt, Explicit Integration of Goals in Heuristic Algorithm Design, in: Proceedings of the 10th International Joint Conference on Artificial Intelligence (1987).

[19] A.P. Muhlemann, A.G. Lockett and C.K. Farn, Job-Shop Scheduling Heuristics and Frequency of Scheduling, International Journal of Production Research 20 (1982) 227–241.

[20] P.S. Ow, Heuristic Knowledge and Search for Scheduling, PhD Thesis, Carnegie-Mellon University (1984).

[21] P.S. Ow and S.F. Smith, Towards an Opportunistic Scheduling System, in: Proceedings of the 19th Hawaii International Conference on System Sciences (1986).

[22] P.S. Ow, S.F. Smith and A. Thiriez. Reactive Plan Revision, in: Proceedings of the 7th National Conference on Artificial Intelligence (1988).

[23] E.D. Sacerdoti, Problem Solving Tactics, in: Proceedings of the 6th International Joint Conference on Artificial Intelligence (1979).

[24] S.F. Smith, P.S. Ow, C. Le Pape, B. McLaren and N. Muscettola, Integrating Multiple Scheduling Perspectives to Generate Detailed Production Plans, in: Proceedings of the SME Conference on Artificial Intelligence in Manufacturing (1986).

[25] S.F. Smith, M.S. Fox and P.S. Ow, Constructing and Maintaining Detailed Production Plans: Investigations into the Development of Knowledge-Based Factory Scheduling Systems, AI Magazine 7 (1986) 45–61.

[26] M. Stefik, Planning with Constraints, PhD Thesis, Stanford University (1980).

[27] A.P.J. Vepsalainen, State Dependent Priority Rules for Scheduling, PhD Thesis, Carnegie-Mellon University (1984).

[28] M. Yamamoto and S.Y. Nof, Scheduling/Re-Scheduling in the Manufacturing Operating System Environment, International Journal of Production Research 23 (1985) 705–722.
