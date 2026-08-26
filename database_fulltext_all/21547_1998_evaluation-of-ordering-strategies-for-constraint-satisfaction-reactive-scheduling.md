---
otero_id: 21547
otero_key: "NEZZREV3"
title: "Evaluation of ordering strategies for constraint satisfaction reactive scheduling"
authors: "Min Soo Suh; Albert Lee; Yung Jae Lee; Young Kwan Ko"
year: "1998"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(97)00052-3"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Evaluation of ordering strategies for constraint satisfaction reactive scheduling

Min Soo Suh <sup>a,)</sup>, Albert Lee <sup>b</sup>, Yung Jae Lee <sup>c</sup>, Young Kwan Ko <sup>d</sup>

Department of Industrial Engineering, UniÕersity of Toronto, 4 Taddle Creek Rd., Toronto, ON, Canada M5S 3G9

<sup>c</sup> Graduate School of Management, UniÕersity of California at IrÕine, IrÕine, CA 92697, USA

Department of Industrial Engineering, Seoul National UniÕersity, ShinLim-Dong San 56-1, Seoul, South Korea

## Abstract

Reactive scheduling is essential in any scheduling system to incrementally reconcile the discrepancies between the generative schedule and current status of the factory. Typical events requiring the reactive scheduling process include the delayed delivery of materials, machine breakdown, and failure to meet quality control standards. To efficiently cope with these unexpected events, a reactive scheduling procedure is proposed based on the constraint satisfaction approach, and applied to the reactive adjustment of hot-rolling schedules at steelworks. Various domain-specific strategies are devised as variable and value-ordering heuristics to guide the search directions in the reactive scheduling process, and implemented in a scheduling expert system. From the experiment conducted on the prototype system developed, we find that the schedule performance is mainly determined by the variable ordering strategy based on the criticality of scheduling activities, and it can be further improved by adopting the appropriate value-ordering strategy based on the least constraining resource heuristic. q 1998 Elsevier Science B.V.

Keywords: Constraint satisfaction scheduling; Reactive scheduling; Variable ordering; Value ordering

## 1. Introduction

In general, the process of solving scheduling problems consists of two phases: generative scheduling phase and reactive control phase. A major concern in the generative scheduling phase is to construct an efficient schedule while satisfying the various constraints imposed on the problem. In the reactive control phase, the generative schedule is modified incrementally to reconcile any discrepancies with actual progress on the shop floor arising from unexpected events such as machine breakdown, failure to meet quality control standards, and so forth. Although reactive scheduling is of great importance in any scheduling system, most scheduling research has mainly focused on the construction of a good generative schedule from scratch without providing enough attention on the reactive control phase 3 .

In the steel industry, most scheduling systems address the reactive scheduling problem by making it the responsibility of the human scheduler to evaluate the implications of the unexpected events, and to adjust the generative schedule accordingly 3,6,8 . <sup>w</sup> <sup>x</sup> However, the combinatorial complexity of the scheduling problem tends to overburden the human scheduler and may result in poor schedule performances. To efficiently deal with the reactive scheduling problem at steelworks, we propose a reactive scheduling procedure based on the constraint satisfaction problem CSP approach, and devise Ž . domain-specific strategies for variable and value ordering heuristics to guide the search directions in the reactive scheduling process. A scheduling expert system was developed to implement these strategies for the reactive adjustment of hot-rolling schedules in a hot strip mill HSM . A set of experiments was Ž . conducted on the expert system to evaluate the performance of different ordering strategies.

## 2. Reactive scheduling procedure

The generative schedules of production processes at steelworks are illustrated in Fig. 1. The generative hot-rolling schedule consists of a sequence of lots that are rolled to produce hot strip coils. Each lot comprises a set of slabs with the same mechanical properties, delivered from the preceding process or slab stockyards. In the generative scheduling phase, a hot-rolling schedule is constructed, satisfying a wide variety of constraints including mechanical rolling conditions, slab properties, and the delivery time of slabs. In the reactive control phase, unexpected events may occur and violate some of the specified constraints, leading to the invalidation of the current generative hot-rolling schedule. For instance, if the charge schedule of basic oxygen furnaces is changed due to a certain unexpected event, its succeeding cast schedule in a continuous caster plant CCP could be invalidated. In such a situation,Ž . reactive scheduling needs to modify the generative hot-rolling schedule to cope with the unforeseen event.

Typical events requiring reactive scheduling in the HSM are as follows.

## 2.1. Delayed deliÕery of slabs

When some slabs are expected to be delivered later than their scheduled time due to abnormal work conditions such as employee absence and tentatively decreased production rate, the hot-rolling schedule needs to be revised to reconcile the inconsistencies caused by the delayed delivery of slabs. For example, a generative rolling schedule is shown schematically in Fig. 2. Each slab $S _ { i } \ ( j = 1 , \ldots , 4 )$ in Cast $\mathrm { C } _ { 1 1 }$ is scheduled to be finished by time $t _ { j }$ at machine CC-1 in the CCP, and to be delivered to roll $\mathsf { R } _ { 1 }$ at $t _ { j } + d _ { j }$ in the HSM. Suppose that slab $\mathrm { \Delta S _ { 4 } }$ is delayed to be finished by $t _ { 4 } + \delta$ due to a lower production rate at machine CC-1, then it would be delivered to roll $\mathsf { R } _ { 1 }$ at $t _ { 4 } + d _ { 4 } + \delta$ , resulting a gap in the rolling schedule from $t _ { 4 } + d _ { 4 }$ through $t _ { 4 } + d _ { 4 } + \delta$ as shown in Fig. 3. To eliminate the gap in roll $\mathsf { R } _ { 1 } ,$ reactive scheduling becomes necessary to find other slabs to be inserted into that gap caused by the delayed delivery of slab $\mathrm { \Delta S _ { 4 } }$

![](/api/attachments/NEZZREV3/fulltext/images/e6ec876eb27367c3b9a2aa3cae0858438f64793a7604846f2e2614e044657443.jpg)  
Fig. 1. The generative schedules of production processes at steelworks.

## 2.2. Failure to meet quality control standards

When some slabs do not meet prescribed quality control standards, they cannot be used in the mill and need to be removed from the generative rolling schedule. Fig. 4 shows that all the slabs produced from the casts, $\mathrm { C } _ { 1 1 }$ and $\mathrm { C } _ { 1 2 }$ at machine CC-1 in the CCP were originally scheduled to be used for the rolls, $\mathsf { R } _ { 1 }$ and $\mathsf { R } _ { 2 }$ in the HSM. However, slab ${ \bf S } _ { 3 }$ and $\mathrm { \Delta S } _ { 6 }$ cannot be used in $\mathsf { R } _ { 1 }$ and $\mathsf { R } _ { 2 }$ , respectively, since they failed to meet the quality control standards specified by the corresponding customers. The unqualified slabs are usually stacked on slab yards for later use to meet the demand of other less stringent customers. In this case, the unqualified slabs need to be removed from the rolling schedule of $\mathsf { R } _ { 1 }$ and $\mathsf { R } _ { 2 }$ and be replaced with other slabs satisfying the quality control standards.

![](/api/attachments/NEZZREV3/fulltext/images/24e0bbd6d8ac372fd594755a56e12b2f93f875e167cf57928432318d191a312a.jpg)  
Fig. 2. A generative hot-rolling schedule.

## 2.3. Machine breakdown

When a machine breaks down in a production process, all the activities assigned to the machine should be postponed until it is up again, triggering consecutive rescheduling in the downstream facilities. For example, Fig. 5 shows that cast $\mathrm { C } _ { 2 1 }$ was scheduled to be produced at machine CC-2 in the CCP from $t _ { 1 }$ through $t _ { 2 } .$ , and to be delivered as slabs to the rolls, $\mathsf { R } _ { 1 }$ and $\mathbf { R } _ { 2 }$ in the HSM. Suppose that machine CC-2 in the CCP broke down at $t _ { 1 }$ and is expected to be repaired by $t _ { 2 } .$ . The machine breakdown in the CCP made it impossible to provide the HSM with the slabs coming from cast $\mathrm { C } _ { 2 1 }$ on time, threatening the continuous rolling operations in the HSM. Thus, reactive scheduling is needed to remove the unavailable slabs from the generative rolling schedule and find alternative slabs from other casts or slab stockyards.

![](/api/attachments/NEZZREV3/fulltext/images/ef6136d18424f8ec49e4ef8b42db5146dbfcc17168ef29801949ea102d7ec817.jpg)  
Fig. 3. A delayed delivery of slab $\mathrm { S } _ { 4 }$ causes a gap in roll $\mathsf { R } _ { 1 }$

![](/api/attachments/NEZZREV3/fulltext/images/8cdadb3b430f220f78ab7c7f6d6e4508c2bc33e1b8430b0daf7282c935c32557.jpg)  
Fig. 4. Slab $\mathrm { S } _ { 3 }$ and $S _ { 6 }$ cannot be used due to the failure to meet quality control standards.

![](/api/attachments/NEZZREV3/fulltext/images/841839774f187d4fc9b5da7adb04bf5126115873f0bf13e338c64b6295bf9f89.jpg)  
Fig. 5. Cancellation of cast $\mathrm { C } _ { 2 1 }$ due to machine breakdown.

These unanticipated events will result in the inevitable inconsistencies between the generative schedule and the current status of the factory. To incrementally reconcile the discrepancies and modify the generative hot-rolling schedule, we propose the following reactive scheduling procedure.

Ž . 1 Scan the generative hot-rolling schedule to detect those slabs violating given constraints. Check for the potential problem in the mechanical rolling conditions and delivery time of slabs from upstream facilities.

Ž . 2 If a certain slab fails to satisfy some constraints, it is deleted from the generative schedule, resulting in a time gap. A time gap in the rolling schedule indicates an open time interval that must be filled in with other slabs satisfying the imposed constraints on the time gap. Fig. 6 shows the time gaps resulting from deleting the slabs violating the constraints. The time gaps are scheduled in a specific order according to the ordering heuristic which will be explained in Section 3.1.

Ž . 3 Find new candidate slabs satisfying the constraints imposed on the time gaps. When a time gap is selected for scheduling, the slabs that can be allocated to the time gap are orderly inserted into that time gap. The detailed ordering strategy for choosing the slab to fill in the time gap will be described in Section 3.2. As the reactive scheduling process evolves, the number of the time gaps decreases.

This reactive scheduling procedure is executed repeatedly until there exists no time gap in the current rolling schedule. If unavoidable time gaps occur, some tight constraints could be relaxed to attract more candidate slabs for filling in the remaining time gaps. The detailed description of the constraint relaxation method is presented in Section 4.2.

![](/api/attachments/NEZZREV3/fulltext/images/fa4f407040ef43a62b61fd2787f6248ef144f1dcec38bd4e848283446b1c379a.jpg)  
Fig. 6. Time gaps resulting from removing the unsatisfactory slabs.

## 3. Ordering strategies for constrained satisfaction reactive scheduling

Most scheduling problems arising in the real manufacturing environment are inherently complex belonging to a class of NP-hard problems. To overcome this difficulty, artificial intelligence literature has recently treated such scheduling problems as CSPs 1,2,5,7,9 . When the CSP approach is applied<sup>w</sup> <sup>x</sup> to scheduling problems, the problem-solving process requires two kinds of decisions for incremental schedule construction. First, a variable ordering heuristic is necessary to choose the next activity for scheduling from the unscheduled activities. After an activity is chosen, a specific time value for the selected activity is determined according to a valueordering heuristic. A proper selection of the variable and value ordering heuristics contributes to the reduction of search space and improved schedule performance 5 .<sup>w</sup> <sup>x</sup>

In our study, we consider the reactive scheduling problem as a CSP and propose domain-specific strategies as the variable and value ordering heuristics for the reactive adjustment of hot-rolling schedules at steelworks. For the CSP representation of the problem, the time gaps are regarded as the variables, and the slabs to be assigned to the time gaps are considered as the values of associated variables. The following notations are used to represent the ordering strategies.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
$T_{i}$  time gap,  $i \in I$ $S_{j}$  slab,  $j \in J$ 
DT( $S_{j}$ ) delivery time of slab  $S_{j}$ 
ST( $T_{i}$ ) start time of time gap  $T_{i}$ 
ET( $T_{i}$ ) end time of time gap  $T_{i}$ 
PT( $T_{i}$ ) average processing time of a slab for time gap  $T_{i}$ 
NS( $T_{i}$ ) number of slabs required to completely fill in time gap  $T_{i}$
</div>

$$
\text { where } \mathrm{NS} (T _ {i}) = (\mathrm{ET} (T _ {i}) - \mathrm{ST} (T _ {i})) / (\mathrm{PT} (T _ {i})).
$$

## 3.1. Variable ordering strategies

For selecting the time gap to be scheduled next, we consider two variable ordering strategies: earliest start time-based strategy and time $\mathrm { g a p ' s }$ criticalitybased strategy.

![](/api/attachments/NEZZREV3/fulltext/images/8db1cea8bc44a0c850c61defbb1d56e286258e3a436d8de62d2e32f293933bc4.jpg)  
The order of time gap selection ${ { T } _ { I } } \Rightarrow { { T } _ { 2 } } \Rightarrow { { T } _ { 3 } }$  
Fig. 7. Earliest start time-based strategy for variable ordering.

## 3.1.1. Earliest start time-based strategy

According to this strategy, the time gap with the earliest start time is scheduled first as shown in Fig. 7. Since the earliest start time of time gaps is fixed, the order for the selection of the time gaps does not change during the reactive scheduling process. In steel plants, the human scheduler prefers this approach since it is straightforward to select the time gaps in the chronological order.

## 3.1.2. Time gap’s criticality-based strategy

This strategy selects the next time gap for scheduling based on the time gap’s criticality. To measure the criticality of a time gap, the ratio of its total available number of slabs over its required number of slabs is computed.

For each time gap $T _ { i } ,$ , its critical ratio CR isŽ . defined as follows:

$$
\operatorname{CR} (T _ {i}) = \frac {\sum_ {j \in J} \delta_ {T _ {i}} (S _ {j})}{\operatorname{NS} (T _ {i})},
$$

where $\delta _ { T _ { i } } \big ( S _ { j } \big )$

$$
= \left\{ \begin{array}{l} 1, \text {   if   slab   } S _ {j} \text {   is   allocatable   to   time   gap   } T _ {i} \\ 0, \text {   otherwise } \end{array} \right.
$$

According to this strategy, the time gap with the least CR value is scheduled first. Since the CR value of time gaps is changed by the assignment of slabs, the order of selecting the next time gap changes dynamically in the course of reactive scheduling. As the CR value of a time gap decreases to one, the time gap is called critical. The more critical a time gap becomes, the harder it is to fill in that time gap since a critical time gap has less available slabs. As a special case, if time gap $T _ { i }$ has a CR value less than one, $\mathbf { i . e . , C R } ( T _ { i } ) < 1$ , time gap $T _ { i }$ is called an infeasible time gap with the implication that it cannot be completely filled even if all the allocatable slabs are actually assigned to the infeasible time gap. An infeasible time gap needs to acquire more candidate slabs by relaxing some of the tight constraints imposed on the time gap.

Fig. 8 illustrates an example of the time gap’s criticality-based strategy. Note that time gap $T _ { 3 }$ is scheduled first since it is the most critical time gap. In this example, if an alternative time gap, $T _ { 1 } ,$ , is chosen to be scheduled first, those slabs allocatable to time gap $T _ { 3 }$ may be assigned to time gap $T _ { 1 } ,$ resulting in making time gap $T _ { 3 }$ to be more critical. In this case the overall schedule quality becomes worse. Therefore, by scheduling the most critical time gap first, this strategy attempts to reduce the total amount of unscheduled time gaps.

![](/api/attachments/NEZZREV3/fulltext/images/b28f0c79bfba1dedda280022fc8dde79d26b3da5e655594472a18ccd2c4e853b.jpg)

$$
\begin{array}{l} S T \left(T _ {I}\right) = 1 0, E T \left(T _ {I}\right) = 1 5, S T \left(T _ {2}\right) = 3 0, E T \left(T _ {2}\right) = 3 5, \\ S T \left(T _ {3}\right) = 7 0, E T \left(T _ {3}\right) = 8 0 \\ P T \left(T _ {I}\right) = 1, P T \left(T _ {2}\right) = 0. 5, P T \left(T _ {3}\right) = 1, \\ N S \left(T _ {I}\right) = 5, N S \left(T _ {2}\right) = 1 0, N S \left(T _ {3}\right) = 1 0, \\ \sum_ {j \in J} \delta_ {T _ {i}} (S _ {j}) = 1 0, \sum_ {j \in J} \delta_ {T _ {2}} (S _ {j}) = 1 5, \sum_ {j \in J} \delta_ {T _ {3}} (S _ {j}) = 1 0, \\ C R \left(T _ {I}\right) = 1 0 / 5 = 2, \\ C R \left(T _ {2}\right) = 1 5 / 1 0 = 1. 5, \\ C R \left(T _ {3}\right) = 1 0 / 1 0 = 1, \\ \Rightarrow T _ {3} \text {is scheduled first} \end{array}
$$

Fig. 8. Time gap’s criticality-based strategy for variable ordering.

## 3.2. Value ordering strategies

When a time gap is selected for scheduling, it should be filled in with the slabs satisfying the imposed constraints on the time gap. For the selection of the slab assigned to the selected time gap, we compare two value ordering strategies: earliest resource allocation strategy and least constraining resource strategy.

## 3.2.1. Earliest resource allocation strategy

As the next candidate slab for the chosen time gap, this strategy selects the slab with the earliest delivery time from the preceding process. Fig. 9 depicts an example of the earliest resource allocation strategy. In this strategy, slabs are ordered in an ascending order of their available time, which makes it simple for the human scheduler to select the next slab for assignment.

## 3.2.2. Least constraining resource strategy

As the next slab for the selected time gap, this strategy chooses the least contended slab by the other time gaps. As a measure for evaluating the extent to which a slab is contended, its resource utilization level RUL is computed. Ž .

Let $T _ { i } ^ { * }$ denote the selected time gap to be scheduled, and TW denote the set of the other time gaps waiting for scheduling. For each unscheduled slab $S _ { j }$

![](/api/attachments/NEZZREV3/fulltext/images/3401b27a6ad28417aba6619e860b79da6d6e54c54e68805b454042ba31349eb8.jpg)  
Fig. 9. Earliest resource allocation strategy for value ordering.

Selected time gap for scheduling: T Time gaps waiting for scheduling: $T _ { 2 } \mathrm { ~ , ~ } T _ { 3 }$ Candidate slabs for T1 : S1 , S2 , S

![](/api/attachments/NEZZREV3/fulltext/images/79d0de9cf1d97ca70750e7d5bf22b8a343375055571641647732e24bae88ff6d.jpg)  
Fig. 10. Least constraining resource strategy for value ordering.

allocatable to time gap $T _ { i } ^ { * }$ , its RUL is defined as: RULŽ . Ž . S <sup>s</sup> Ý  S . j T j T<sub>k</sub><sup>g</sup>TW

The slab with a large RUL value implies that it could be assigned to many other time gaps, making it desirable to reserve the slab for later use. Thus, this strategy selects the slab with the minimum RUL value as the next candidate slab for filling in time gap $T _ { i } ^ { * }$ as illustrated in Fig. 10. In this example, slab ${ \bf S } _ { 3 }$ can be allocated only to time gap $T _ { 1 } { \mathrm { : } }$ ; thus, its assignment does not reduce the amount of available slabs for the other time gaps. If an alternative slab is chosen to be assigned first, the available amount of slabs for the other time gaps is reduced accordingly with the possibility of unnecessarily making some time gap to be critical. Therefore, this strategy attempts to improve the overall schedule performance by reserving the more contended slabs for the other time gaps.

## 4. An expert system for the reactive adjustment of hot-rolling schedules

Based on the constraint satisfaction approach described earlier, we developed a prototype expert system named ROSE for the reactive adjustment of hot-rolling schedules in the HSM at a steelworks <sup>w</sup> <sup>x</sup> 10,11 . The main characteristics of the ROSE system are described briefly in this section.

![](/api/attachments/NEZZREV3/fulltext/images/cb47fb706dd7692ab636902fddddad7de66a39dcd286c261768f984d69e26315.jpg)  
Fig. 11. A sample rule of UNIK-FWD.

4.1. Knowledge representation and inference mechanism

The ROSE system is composed of two major parts: working memory and rule base. The working memory stores the scheduling objects such as rolls, lots and constraints that can be matched with the antecedent parts of rules in the rule base. Each element in the working memory is represented as a frame for implementing the object-oriented paradigm and interfacing with the rule base. The reactive scheduling heuristics are stored in the rule base. Rules are represented using the proprietary tool UNIK-FWD 4 , as presented in Fig. 11. UNIK-FWD adopts the forward chaining method as its basic inference mechanism. To efficiently deal with the complexity of the scheduling problem, UNIK-FWD has some additional features such as 1 rule group-Ž . ing that partitions the entire rule base according to meta-attributes, 2 conflict resolution by meta-rules,Ž . and 3 parallel firing of multiple candidate instances Ž . when they are matched with a firable rule. These features help clarify the order of rule firing and reduce the pattern matching time of frames with rules.

## 4.2. Constraint relaxation

In certain circumstances, the constraints imposed on the scheduling problem are so restrictive that the system cannot perfectly eliminate all the time gaps, resulting in the infeasible time gaps. In this case, it is necessary to relax some of the tight constraints and increase the number of the candidate slabs that can be allocated to the remaining time gaps. It is the

![](/api/attachments/NEZZREV3/fulltext/images/0316a090cda86761aac9eba44f3e0af3e04395a8c8fc09957a91fc83f9a24732.jpg)  
Fig. 12. An infeasible time gap T remains.

Scheduling horizon: [t1 , t2] Maximum number of slabs to be rolled consecutively in width group B4

![](/api/attachments/NEZZREV3/fulltext/images/c8a3790cc49f9c69e044aad7028e86bb72f7f2317baefd0310c30c0e3abcb706.jpg)  
Fig. 13. Time gap $T _ { \mathrm { r } }$ can be filled in with slab ${ \bf { B } } _ { 4 }$ after constraint relaxation.

user’s responsibility to select the constraints to be relaxed and indicate the range of relaxation from their original boundaries. Based on the user’s input, the system re-runs its scheduling heuristics and provides a new rolling schedule in consideration of the modified constraints. This function of the system provides a ‘what-if’ analysis type tool to the user, and thus enhances decision-making capability.

Let us describe in detail the constraint relaxation method of the system. Suppose time gap $T _ { \mathrm { r } }$ still exists in roll $R _ { 1 }$ from $t _ { \mathrm { a } }$ through $t _ { \mathrm { b } }$ after the completion of reactive scheduling as shown in Fig. 12. To satisfy the slab delivery constraint imposed on time gap $T _ { \mathrm { r } }$ , only the slabs produced in the CCP during the time interval, $[ t _ { 1 } , \ t _ { 2 } ]$ can be assigned to that time gap. In addition, they must belong to one of the groups, B and C in terms of the slab width. The ROSE system suggests two types of constraint relaxation to cope with this situation.

Scheduling horizon: [ t1 , t3] Maximum number of slabs to be rolled consecutively in width group B and C: 3  
![](/api/attachments/NEZZREV3/fulltext/images/656db682ed0c342f367825b252f9ae857ea742d587785dfef2e7d5c6e2a38683.jpg)  
Fig. 14. Time gap $T _ { \mathrm { r } }$ can be filled in with slab $\mathrm { C } _ { 3 }$ after extending the scheduling horizon.

Scheduling horizon: $\lceil t _ { I } , t _ { 2 } \rceil$ Maximum number of slabs to be rolled consecutively in width group B and C: 3  
![](/api/attachments/NEZZREV3/fulltext/images/3642f0a1023852c9b4b1dda187f0b325a8119546e76d746a4f8cc1bab236d7ae.jpg)  
Fig. 15. Interchange of cast $\mathrm { C } _ { 2 1 }$ with cast $\mathrm { C } _ { 2 2 }$

## 4.2.1. Relaxation of mechanical rolling conditions

To prevent a damage to the rolls of the machines in the HSM, there is a limit on the consecutive number of same width slabs to be rolled. If the user relaxes this constraint and increases the limit, more slabs can be considered to fill in the remaining time gap. For example, Fig. 12 shows that the maximum number of slabs to be rolled consecutively is set to 3 for the width groups, B and $\mathrm { C } ,$ resulting in the situation where time gap $T _ { \mathrm { r } }$ can no longer be filled in with a slab belonging to width group B. If the user increases the maximum number of slabs for width group B to 4, it becomes possible for slab ${ \bf { B } } _ { 4 }$ in cast $\mathrm { C } _ { 2 1 }$ to be assigned to time gap $T _ { \mathrm { r } }$ as shown in Fig. 13.

Since this constraint relaxation will increase the fatigue level of the rolling machines, the user should carefully check the mechanical conditions of the machines.

## 4.2.2. Relaxation of the scheduling horizon

If the user extends the scheduling horizon in the cast schedule, more slabs can be considered as candidates for the time gaps in the HSM. As shown in Fig. 14, when the user extends the scheduling horizon in the cast schedule from $[ t _ { 1 } , \ t _ { 2 } ]$ to $[ t _ { 1 } , \ t _ { 3 } ]$ , the ROSE system can eliminate time gap $T _ { \mathrm { r } }$ by assigning slab $\mathrm { C } _ { 3 }$ in cast $\mathbf { C } _ { 2 2 }$ . In this case, the maximum number of slabs to be rolled consecutively is originally set to 3 for width group B; thus, only the slab belonging to width group C can be assigned to time gap $T _ { \mathrm { r } }$

Since only the slabs produced before $t _ { 2 }$ in the CCP can be actually used for roll $\mathsf { R } _ { 1 }$ in the HSM, the user attempts to interchange cast $\mathrm { C } _ { 2 1 }$ with cast $\mathrm { C } _ { 2 2 }$ as shown in Fig. 15. If the interchange of the casts does not cause any constraint violation to roll $\mathsf { R } _ { 1 } ,$ this constraint relaxation can be carried out successfully.

## 4.3. InteractiÕe scheduling

Interactive scheduling enables the user to modify the schedule when the infeasible time gaps persist despite the constraint relaxation. A graphical user interface of ROSE helps the user to easily obtain information regarding the scheduling objects and to modify the schedule interactively with the system. If the user attempts to assign a slab to an unscheduled time gap, the system automatically checks whether all the relevant constraints will be satisfied. This human–computer interaction supports the user in adjusting the schedule quickly while satisfying the constraints imposed on the problem.

## 5. Experimental results

The performance of the scheduling heuristics for the reactive scheduling problem in the HSM is evaluated in terms of productivity and safety. The productivity of the factory is increased when the rolling machines continuously process slabs without any time gap in the rolling schedule. Furthermore, the rolls of the machines could be damaged if they are in idle condition. Therefore, to improve the schedule performance, it is necessary to minimize the amount of unscheduled time gaps. Considering these facts, we chose the average size of the unscheduled time gaps as the criterion for evaluating the schedule performance of the heuristics.

To compare the performances of different ordering strategies, we combined the following variable and value-ordering heuristics.

<sup>Ø</sup> Variable ordering strategy:

–Earliest Start Time EST -based strategy Ž .

–Time Gap’s Criticality TGC -based strategy Ž .

<sup>Ø</sup> Value ordering strategy:

–Earliest Resource Allocation ERA strategy Ž .

–Least Constraining Resource LCR strategyŽ . The combined four strategies are: EST–ERA, EST–LCR, TGC–ERA and TGC–LCR. For example, the TGC–LCR strategy indicates that the TGCbased strategy is considered as a variable ordering heuristic, while the LCR strategy is used as a valueordering heuristic. Six sets of scheduling problems were generated by adjusting the proportion of slabs to produce thin coils in the total set of slabs from 40% to 80%. Since the slabs for the thin coils give a severe burden to the rolling machines, the more they are included, the harder it becomes to schedule with the critical time gaps. Each set of problems revised 30 generative rolling schedules and attempted to fill in the time gaps using the reactive scheduling procedure. Under these experimental settings, our prototype scheduling system was tested on a SUN workstation.

Table 1  
Comparison of scheduling performances of different strategies  
<sup>a</sup> Experiment PSTC Average size of unscheduled time gaps

<table><tr><td>set</td><td>(%)</td><td colspan="4">EST-ERA EST-LCR TGC-ERA TGC-LCR</td></tr><tr><td>1</td><td>40</td><td>37.4</td><td>0</td><td>0.7</td><td>0</td></tr><tr><td>2</td><td>50</td><td>46.5</td><td>0</td><td>3.6</td><td>0</td></tr><tr><td>3</td><td>60</td><td>58.0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>4</td><td>70</td><td>59.0</td><td>52.9</td><td>0</td><td>0</td></tr><tr><td>5</td><td>75</td><td>80.1</td><td>59.2</td><td>0</td><td>0</td></tr><tr><td>6</td><td>80</td><td>83.3</td><td>67.7</td><td>0</td><td>0</td></tr></table>

<sup>a</sup> Percentage of slabs for thin coils.

Table 1 shows the average size of unscheduled time gaps produced by the four combinations of the variable and value-ordering strategies. When the percentage of slabs for thin coils PSTC is below 60,Ž . the strategies, EST–LCR and TGC–LCR have completely eliminated all the time gaps from the generative hot-rolling schedule. When PSTC is above 60, the TGC–ERA and TGC–LCR strategy resulted in no time gap. These experimental results indicate that the value ordering heuristic works well in the situation having lower PSTC where few critical time gaps exist, while the variable ordering heuristic is more effective in the harder scheduling environment, i.e., higher PSTC, with many critical time gaps.

In particular, the LCR strategy as a value-ordering heuristic is shown to be very effective under PSTC less than 60, irrespective of variable ordering strategies. This can be explained by the fact that the LCR value ordering strategy can evenly distribute slabs to time gaps when most time gaps are not critical. On the contrary, when PSTC is above 60, the TGC strategy as a variable ordering heuristic is shown to be most effective, irrespective of value ordering strategies. Since the TGC variable ordering strategy schedules the most critical time gap first, it leads to good performance even if the factory is burdened with the critical time gaps.

In conclusion, the combined strategy of TGC as a variable ordering heuristic and LCR as a value ordering heuristic consistently outperforms all other strategies in all the cases. This experiments provided us with the valuable insights regarding the performances of different scheduling strategies: 1 the Ž .

schedule performance is mainly determined by the variable ordering strategy based on the criticality of time gaps, and 2 it can be further improved byŽ . adopting the appropriate value ordering strategy based on the least constraining resource heuristic.

## 6. Conclusion

To efficiently deal with the reactive scheduling problem at steelworks, we propose a reactive scheduling procedure based on the CSP approach, and devise various domain-specific strategies for the variable and value ordering heuristics. From the experiments conducted on the prototype system developed, we find that the schedule performance is mainly determined by the variable ordering strategy based on the criticality of time gaps, and it can be further improved by adopting the appropriate value ordering strategy based on the least constraining resource heuristic.

We expect the proposed variable and value ordering strategies to be applicable to other similar scheduling situations where the scheduling objective is to minimize the amount of the discrepancies between the generative schedule and actual progress on the shop floor.

## Acknowledgements

This work has been supported in part by a grant from Korea Research Foundation.

## References

<sup>w</sup> <sup>x</sup> 1 M.S. Fox, S.F. Smith, ISIS—a knowledge-based system for factory scheduling, Expert Systems 1 1 1984 25–49.Ž . Ž .

<sup>w</sup> <sup>x</sup> 2 N.P. Keng, D.Y.Y. Yun, M. Rossi, Interaction-sensitive planning system for job–shop scheduling, Proc. 2nd Conf. on Expert Systems and the Leading Edge in Production Planning and Control, 1988, pp. 57–69.

<sup>w</sup> <sup>x</sup> 3 R.M. Kerr, Scheduling in the Steel Industry, Technical Report CD-S 94<sup>r</sup>16, Vienna University of Technology, 1994.

<sup>w</sup> <sup>x</sup> 4 J.K. Lee, M.S. Suh, S.B. Oh, M.Y. Kim, J.B. Jung, J.C. Shin, Y.U. Song, Development of UNIK for the Integration of Knowledge and Optimization Models, Technical Report N486-3509-7, Korea Advanced Institute of Science and Technolology, 1988.

<sup>w</sup> <sup>x</sup> 5 J.K. Lee, M.S. Suh, M.S. Fox, Contingencies for the design of scheduling expert systems, Expert Systems with Applications 6 1993 219–230.Ž .

<sup>w</sup> <sup>x</sup> 6 M. Numao, S. Morishita, A scheduling environment for steel-making process, Proc. 5th Conf. on Artificial Intelligence Applications, 1989, pp. 279–286.

<sup>w</sup> <sup>x</sup> 7 N. Sadeh, MICRO-BOSS: a micro-opportunistic factory scheduler, Expert Systems with Applications 6 1993 377–Ž . 392.

<sup>w</sup> <sup>x</sup> 8 M.J. Shah, R. Damian, J. Silverman, Knowledge-based dynamic scheduling in a steel plant, Proc. 6th Conf. on Artificial Intelligence Applications, 1990, pp. 108–113.

<sup>w</sup> <sup>x</sup> 9 S.F. Smith, A constraint-based framework for reactive management of factory schedules, Proc. First Conf. on Expert Systems and the Leading Edge in Production Planning and Control, 1987, pp. 113–130.

<sup>w</sup> <sup>x</sup> 10 M.S. Suh, C.H. Kim, Y.K. Ko, K.S. Lee, ROSE: an expert system for reactive adjustment of hot-rolling schedules, Proc. on Computerized Production Control in Steel Plant, 1993, pp. 271–281.

<sup>w</sup> <sup>x</sup> 11 M.S. Suh, A. Lee, Y.K. Ko, A constraint satisfaction approach to reactive scheduling for hot strip mill, Proc. on the First Asia and Pacific DSI Conf. 2, 1996, pp. 739–744.

Min Soo Suh received a BS in Industrial Engineering from Seoul National University in 1985. He received his MS degree in Management Science, and PhD in Management Information Systems from Korea Advanced Institute of Science and Technology in 1987 and 1991, respectively. Since then he had led various projects for the development of decision support systems and expert systems at the Research Institute of Industrial Science and Technology, and POSCO Research Institute. He is now a visiting scholar at the University of Toronto. His research interests include intelligent decision support systems, constraint-directed scheduling, and artificial intelligence application to managerial problems.

Albert Lee received his PhD degree from University of California, Irvine in 1991. He is currently working as a corporate advisor for SAP, Korea and an assistant professor at the Pusan University of Foreign Studies. His major research areas are in the field of production and quality management, and related system development AI technology.

Yung J. Lee is a PhD candidate at the Graduate School of Management, University of California, Irvine. He holds a BA in English Literature from Korea University and an MBA degree from University of California, Irvine. His research interests include intelligent decision support systems, marketing decision making in distribution channels, and marketing information systems.

Young Kwan Ko is a PhD candidate in Industrial Engineering at Seoul National University. He received his BS and MS degrees in Industrial Engineering from Seoul National University. He has worked as a senior researcher at POSCO Research Institute. His research interests include intelligent manufacturing, production planning and scheduling.
