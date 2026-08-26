---
otero_id: 16898
otero_key: "AUASQM2H"
title: "Handling shared resources in a temporal data base management system"
authors: "Thomas L. Dean"
year: "1986"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(86)90091-6"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Handling Shared Resources in a Temporal Data Base Management System

Thomas L. DEAN
Brown University, Providence, RI 02912, USA

This paper presents an approach to managing shared resources through the use of a temporal data base and special purpose reason maintenance system. All resource requests are processed through a central data base management system that assists employees in scheduling events to take advantage of available resources. A temporal data base is used to keep track of the condition and use of these resources. The system assists in resolving conflicts between employees competing for the same resources and detects when a change in the condition of a resource selected for a particular task makes it unsuitable for its intended purpose.

Keywords: Resource management, Temporal reasoning, Reason maintenance.

![](/api/attachments/AUASQM2H/fulltext/images/25ecbc9bb513d52535c9886327303ae218cef804f068ffae77f1be6605f2bcf1.jpg)

Thomas L. Dean received his B.A. in mathematics from Virginia Polytechnic Institute & State University, Blacksburg, VA in 1982 and his Ph.D. in computer science from Yale University, New Haven, CT in 1986. He is currently a member of the computer science faculty at Brown University in Providence, RI. His research interests include deductive retrieval methods for applications in artificial intelligence, logic programming, and robot problem solving.

## 1. Introduction

Today, employees at almost every level in the corporate hierarchy participate in the managerial process. Secretaries oversee the use of sophisticated computing machinery. Warehouse operators have become an integral part of inventory control. Custodial services employ complex equipment and communication devices to maintain buildings and grounds according to strict standards. All of these employees require access to information about the operational status and availability of company-owned resources to coordinate their activities. The coordination of activities involving shared resources can be characterized in terms of fairly complex deductions composed of simpler inferential steps, each of which is carried out by an employee responsible for some aspect of a company's affairs. The individual employee's deductive contribution generally depends upon the contributions of other employees. By making these dependencies explicit we can automate much of the communication necessary for efficiently managing resources. Suppose that S, the secretary in charge of office allocations, has sent a message to employee A saying that A can move into the office currently occupied by employee B any time after Tuesday. S's reallocation of B's office was made on the basis that B's office was predicted to be vacant after Tuesday. This prediction, made by someone in personnel, was based on information supplied by upper management concerning the transfer of employee B. If management decides to delay B's transfer, then the fact that B's office will no longer be available after Tuesday should quickly be relayed to S so other arrangements can be made for employee A.

Currently the communication required to effect this sort of coordination is handled through the laborious and time consuming process of filling out, sending, and reading specialized forms: what we refer to as paper-work data dependencies. Paper-work data dependencies are intended to ensure that everyone who needs to know about a given piece of information eventually will know. Processing forms can become quite complicated, however, and it is all too often the case that critical information either fails to reach its destination altogether, or reaches it too late to be of any use. It is also quite common for many people to have read and passed on information that they were not required to act upon; they simply served as transcribers and message routers.

For the purposes of this paper, forms provide a record of transactions involving the scheduling of events and the allocation and deallocation of shared resources (e.g., reserve the use of room 114A for two hours on January 15 starting at 2:00 PM for the purpose of a meeting of the board of directors). Every form refers to a prediction of some sort; whether the prediction actually comes to pass will depend upon many things (e.g., if any of the key board members are not available on January 15, then the meeting will not occur and the reservation should be cancelled). Forms are copied and distributed to make sure that each employee is aware of important new information that pertains to that individual employee's duties. In this paper we will look at a method for keeping employees abreast of important changes without the need for paper-work data dependencies. The method described here involves an extension of the techniques used in static data bases for maintaining explicit data dependencies [7] in order to deal with the complications introduced by facts that are true over some intervals but false or unknown over others. The generation and distribution of forms is eliminated by the use of a shared temporal data base to capture the predictions usually embedded in special forms and paper work. In addition, a temporal reason maintenance system [6] is used to ensure that individual employees are informed in a precise and timely manner of changes to the data base that might affect predictions that they are either responsible for or dependent upon.

## 2. Reasoning About Resources

We will begin by considering certain basic characteristics involved in reasoning about resources: change, the passage of time, uncertainty about the future, and the inevitability of conflict.

To begin with, events and actions precipitate change; if employee $A_{1}$ takes control of a non-shareable resource R during the interval from $t_{0}$ to $t_{1}$ , then R is not available for use by employee $A_{2}$ during that same period of time. In order to make plans for the future there must be some means of representing the duration of events and the spans of time over which resources are available. We need to capture information that is metric but fuzzy [5] (e.g., the meeting will take between 5 and 10 minutes, or the conference room will be available for use by 3:00, give or take 15 minutes). This provides one way to take into account uncertainty about the future. A second way involves reasoning about assumptions.

Most of the predictions we make are plausible at best. Predictions are only as accurate as the currently available information allows. Since the current information is liable to be incomplete or even false, it becomes critical to notice when assumptions made in the process of prediction are undermined by the addition of new information or the removal of old. In a corporate data base, employees will have to rely upon information gathered and maintained by other employees. Suppose that employee $A_{1}$ makes a prediction about the availability of a company car for a visiting executive on the basis of information supplied by employee $A_{2}$ . $A_{2}$ 's information is based in part on an estimate by employee $A_{3}$ in mechanical repair. If $A_{3}$ updates his information in such a way as to threaten $A_{1}$ 's prediction, then $A_{1}$ should be notified but in most cases there will be no reason to bother $A_{2}$ . All $A_{1}$ will want to know is (a) what went wrong and (b) what might be done to fix things or, barring that, what alternatives are available. The latter involves detecting and resolving conflicts between steps in the plans of separate agents. In this paper we will rely upon the intelligence of the individual employees to resolve their differences and concentrate upon the detection and annotation of assumption failures. The system described here keeps track of assumptions made in the course of prediction in order to notice possible conflicts, identify the agents involved in the conflict, and point out the reasons why the conflict has occurred, so as to suggest possible remedial steps. The resulting functionality is that of a decision support system for coordinating the activities of several agents interacting through their use of certain shared resources.

## 3. Temporal Data Base Management

In this section, we will briefly describe a system for managing the information in a data base called a time map [9] that captures what is known about events and their effects occurring over time. The system is called, naturally enough, a time map management system or TMM. Time maps are used to record information about the truth of propositions that change over time. We will be particularly interested in propositions describing the condition and availability of objects treated as resources. The basic operation of the TMM can be described in terms of:

(1) A query language that enables users to determine the truth of facts over specified intervals of time. This language supports simple retrieval of the form: Is it possible that $P$ is true at time $T$ given what is currently known? It also handles retrieval of the form: Find an interval satisfying some initial constraints such that the conjunction (and $P_1 \ldots P_n$ ) is true throughout the interval. The syntax of the language is first order predicate calculus, and the TMM can be thought of as an extension of predicate-calculus data base systems such as PROLOG [2] to handle time.

(2) A set of techniques for extending the information in the data base. These techniques allow for conditional predictions on the basis of temporal information (antecedent conditions) extracted from the data base. Predictions added to the data base in this way are made to depend upon the antecedent conditions in a meaningful way.

(3) A mechanism for monitoring the continued validity of conditional predictions. This mechanism extends the functionality of reason maintenance system [7] to temporal domains.

A time map is a graph. Its vertices refer to point (or instants) of time corresponding to the beginning and ending of events. One point is related to another using constraints where a constraint is represented as a directed edge linking two points. Each edge is labeled with an upper and lower bound on the distance separating the two points in time. These bounds allow us to represent incomplete information concerning the duration and time of occurrence of events (e.g., lunch will last between 15 and 20 minutes, or schedule an appointment for some time after 3:00).

An interval is just a pair of points. Each interval consists of a begin and an end point such that the beginning is constrained to precede or be coincident with the ending. Some intervals are more important than others, because they correspond to particular occasions when a general type of occurrence happens. These intervals are referred to as tokens of that type. A type is denoted by a formula like (location obj421 loc14) or (move obj31 loc14 loc17). An interval together with a type will often be referred to as a time token (or simply token in situations where it should cause no confusion).

Events corresponding to the allocation and deallocation of resources are referred to as transactions. Typical transaction events involve occupying and vacating rooms and establishing and relinquishing control of equipment. Requests to the TMM for resources specify general criteria (e.g., find a room seating at least 10 people that is available from 10:00 AM until 11:30 AM on February 3). The answers to such requests will be used, however, to instigate specific transaction events [e.g., (occupy group31 rm427)] rather than general events corresponding to existentially quantified formula [e.g., (∃ rm: (and (occupy group31 rm) (≥ (seating-capacity rm) 10))]. Note that this represents a considerable simplification of the resource management problem. We are currently considering extensions that deal with less restricted types of transaction events, but keep in mind that the general resource management problem is intractable and hence its 'solution' will require certain carefully considered compromises. Committing to specific transaction events constitutes one such compromise, but there are other less extreme measures that might be taken (see pp. 20–26 in [6] for a discussion of these issues).

Reasoning about time in the TMM consists of scanning the time map in order to determine how one event is related to another and what might be true during, before, or after an event. Since the instants are not totally ordered one can make hypotheses about what the consequences of certain additional ordering constraints might be and then proceed to explore some of those consequences. It is quite easy to jump about the time map and simultaneously keep track of a number of situations. One of the important characteristics of this representation of time is that it can be updated incrementally. That is to say, as new events and facts are added, only those parts of the graph that are affected need be changed. This is known as propagating the effects of a change. As this propagation proceeds it is important to be able to recognize when predictions formerly believed to be true are no longer so. This sort of graph scanning and updating is referred to as 'reasoning about time from the side' [9]. It's as though all of what you know about the past, present, and future is laid out in front of you. An example should help to strengthen this intuition.

Fig. 1 shows a simple time map. Tokens corresponding to events are represented by two vertical bars connected by a single horizontal bar (e.g., $|-|$ ) Tokens corresponding to facts are represented as a vertical bar indicating when the fact is first believed to be true, and either a second vertical bar providing some indication when the fact ceases to be true, or an arrow $\rightarrow$ indicating that the fact is believed to persist indefinitely into the future. The delimiters for a fact token are connected by a dashed horizontal bar (e.g., $|----\rightarrow$ ). Each token is labeled with a formula describing its type. In fig. 1, the only orderings are those shown as squiggly lines and these indicate that one point precedes another. The order of precedence is indicated with an arrow. A squiggly line with double hash marks indicates that the two connected points are coincident. There are two events shown in fig. 1: one of type (routine-maintenance projector31) and a second of type (product-demonstration unit9 grp41 product732). There are also two fact tokens describing the status of projector31 before and after the routine service event.

Tokens corresponding to facts [e.g., (status projector31 out-of-service)] that change over time are referred to as persistences (after [9]). If two tokens with contradictory types [e.g., (status projector31 out-of-service) and (status projector31 in-service)] are ordered such that one begins before the other and the earlier could persist longer than the beginning of the later, then the two are said to be apparently contradictory. The TMM resolves apparently contradictory tokens by forcing the end of the earlier to precede the beginning of the later. In fig. 1, the constraint linking the end of the token of type (status projector31 out-of-service) and the beginning of the token of type (status projector31 in-service) was added by the TMM to resolve an apparent contradiction.

![](/api/attachments/AUASQM2H/fulltext/images/b8b09bc7a0e26d9d1432476a45ee5f1f2489b931bb2d05da6f309c2b24c8a4ab.jpg)  
Fig. 1. A simple time map.

There are two types of predictive inference supported by the TMM, referred to as controlled forward inference and automatic projection. Controlled forward inference is characterized by calls to the deductive retrieval system of the form (foreach-answer (fetch antecedent-conditions) (add consequent-predictions)). This means that for each answer (set of variable bindings, temporal context, etc.) satisfying the antecedent conditions, add the consequent-predictions to the data base [having made appropriate substitutions and established constraints as required (see [6] for details)]. The consequent-predictions are made to depend upon the antecedent-conditions in such a way that if these conditions are ever undermined, then the predictions will be retracted as well. Consider the code shown in fig. 2. For-first-answer is a self-explanatory variant of for-each-answer. Predications of the form (token type token-name) are used to create new time tokens and refer to existing tokens of a given type. The token-name gives us a handle so we can speak about the interval associated with a time token. A conjunct of the form (tt $pt_1$ $pt_2$ (and $P_1 \ldots P_n$ )) is treated as a request to determine if (and $P_1 \ldots P_n$ ) is true throughout the interval corresponding to $pt_1$ and $pt_2$ , or could be made so with additional constraints. The during predicate refers to an interval relation between tokens. The code in fig. 2 tries to find a restriction (set of additional constraints) on the current time map such that it is true throughout the interval associated with the product demonstration event that there is an operational opaque projector. If the TMM finds such a restriction, then it enforces the restriction and adds what constitutes a plan for using a particular opaque projector in making a presentation.

Executing the code in fig. 2 with the time map of fig. 1 would result in the time map shown in fig. 3.

Controlled forward inference is used to guide

(for-first-answer

(fetch ' (and (token (product-demonstration unit9 grp31 product732) ?tok1)

(tt (begin ?tok1) (end ?tok1) (status ?projector in-service))

(instance-of ?projector opaque-projector)))

(add ' (and (token (presentation product732 format4 ?projector) ?tok2)

(during ?tok2 ?tok1))))

Fig. 2. Example of controlled forward inference.

decision making. Assertions corresponding to consequent predictions are generally associated with plans and transaction events. The TMM also supports rules (called automatic projection rules) that can be used to model the underlying physics of a domain or generate tasks in response to specific conditions. A rule of the form (project antecedent-conditions trigger-event delay consequent-effects) states that if an event of type trigger-event occurs, and the antecedent-conditions are true throughout the interval associated with trigger-event, then the consequent-effects are true after an interval of time determined by delay. As an example, the rule shown in fig. 4 states that if an employee is transferred to a division of a company such that his current office is not in the region designated for his new division, then after a delay of 24 hours he forfeits the old office and his new division is given the responsibility of assigning him an office in their designated space. Auto-projection rules provide an employee with one method for responding to new information added to the time map. Rules such as the one shown in fig. 4 might be used by the personnel office to automate routine tasks.

Not everything can be easily automated and there are many circumstances that require human intervention. In order to bring such circumstances to the attention of particular agents, the TMM employs two techniques referred to as pattern directed procedure invocation and dependency directed fault detection. The details of their implementation are rather complex (see [6]), but their use is quite simple. The two techniques can be thought of as corresponding to temporal analogs of IF-ADDED and IF-ERASED demons used in PLANNER-like languages [8]. Pattern directed procedure invocation is used to call a given procedure upon the assertion of an event of a specified type. So, for instance, the following would serve to notify a division administrator of the need to relocate an employee being transferred to that division.

![](/api/attachments/AUASQM2H/fulltext/images/27004e024e314a6e010dceed3f2beefc6c6083db86e6da727f914a69f88bcfba.jpg)  
Fig. 3. Time map showing the result of controlled forward inference.

## (if-occurs (achieve (relocate ?person ?division)) (notify-of-pending-task (administrator ?division)))

Dependency directed fault detection, on the other hand, is used to detect when something that was formerly believed to occur is now in danger of failing. An event is determined to be in danger of failing if one of the antecedent conditions (or assumptions) that justified its assertion is no longer true. For example, one of the antecedent conditions for (presentation product732 format4 projector31) in fig. 3 is that projector31 is believed to be in service throughout the interval associated with the product demonstration event. If projector31 is damaged prior to using it in the presentation task, then that task may fail to occur. The most common response to an anticipated failure is simply to notify the author of the event (i.e., the person responsible for asserting it initially). A slightly more complicated response might involve first trying a simple patch and then notifying the author only in the event that the patch fails. The follow-

(project (and (office-allocated ?employee ?office)
(not (designated-region ?unit2 ?office)))
(transfer ?employee ?unit1 ?unit2)
(hours 24)
(and (not (office-allocated ?employee ?office))
(achieve (relocate ?employee ?unit2))))

Fig. 4. An example of an automatic projection rule.

ing attempts to find an alternative projector satisfactory for a given format before alarming the author of a presentation task deemed in danger of failure:

(if-endangered

(presentation ?product ?format ?projector)
(if alternative-projector-available
then substitute-the-alternative
else notify-author-of-impending-failure))

The above discussion provides an overview of some of the basic functions supported by the TMM. In order to get a better idea of how the system might be used in an office setting, we'll look at a slightly more complicated example.

## 4. An Example Illustrating the Functionality of the TMM

Suppose that agent $A_{1}$ is given the task of reserving a room and equipment for a product demonstration to be staged for a group of potential investors. This will require the use of a meeting room seating at least 10 people and an opaque projector to display some of the promotional material. The demonstration is slated to occur sometime between 8:00 AM and 2:00 PM on the 14th of January. Let's suppose further that the only available room is RM17. Agent $A_{2}$ has reserved its use for a board meeting in the morning, but the room is vacant from 11:30 AM to 2:30 PM. We'll also assume that there is an opaque projector available for use throughout the required period.

The blend of logic programming and LISP style syntax used by the TMM is unsuitable for most office environments. Instead, we employ a preprocessor that prompts a user for the information that would normally be contained on a special requisition form, and then converts that information into calls to the TMM. Fig. 5 shows how $A_1$ would go about reserving a meeting room for a product demonstration. Fig. 6 shows a program fragment representing a portion of the TMM code generated in response to $A_1$ 's request. (Some additional rules used in running this example are included in fig. 7 for completeness.) The code in fig. 6 might be paraphrased as follows: If it is true, or can be made so by restricting the current partially ordered time map, that a moderately clean room capable of seating 10 people is free for at least one hour during which an opaque projector is also available, then if the room and time are approved by the user, plan to occupy that room and appropriate the services of said projector. The TMM code fragment sets up the necessary temporal data dependencies and modifies the time map to reflect the plans of agent $A_1$ .

Assuming that $A_{1}$ chooses to reserve the use of room RM17 and opaque projector OP31, let's consider some of the ways in which $A_{1}$ 's plans might be upset.

(1) The time allotted for the board meeting scheduled by $A_{2}$ is extended for some reason. In this case, $A_{2}$ would attempt to modify the event corresponding to the board member vacating RM17. This would result in the TMM detecting a potential interaction between $A_{1}$ and $A_{2}$ involving RM17. At that time $A_{2}$ would be requested to resolve the conflict with

Fig. 5. Transcript of $A_{1}$ 's initial interaction with the TMM for the meeting room example.

```lisp
(for-each-answer
(fetch '(and (occurs (product-demonstration unit9 grp41 ?product) ?tok1)
(elt (distance (begin ?tok1) (end ?tok1)) 60 90)
(tt (begin ?tok1) (end ?tok1)
(and (available-for-exclusive-occupancy ?room grp41)
(>= (seating-capacity ?room) 10)
(condition ?room ?status)
(member ?status !<pristine moderately-clean>)
(available-for-exclusive-use ?projector grp41)
(instance-of ?projector opaque-projector)
(operational-status ?projector in-service)))))

until (and (prompt-user-for-ok ?room ?projector)
(prompt-user-for-start-time ?start-time))
result (add '(and (pt= (begin ?tok1) (point-reference ?start-time))
(occurs (occupy grp41 ?room) ?tok2)
(pt= (end ?tok2) (begin ?tok1))
(occurs (vacate grp41 ?room) ?tok3)
(pt= (begin ?tok2) (end ?tok1))
(occurs (appropriate grp1 ?projector) ?tok4)
(pt= (end ?tok4) (begin ?tok1))
(occurs (relinquish grp41 ?projector) ?tok5)
(pt= (begin ?tok5) (end ?tok1))))
```  
Fig. 6. Data base operations initiated in the course of the interaction shown in Fig. 5.

$A_{1}$ . Some of the options suggested by the system would be for $A_{2}$ to schedule an earlier start time or $A_{1}$ to schedule a later start time.

(2) Security or maintenance might report OP31 lost, stolen, or damaged. An equipment failure would be reported by asserting a token of type (malfunction OP31) and constraints on the time of its occurrence. Automatic projection rules such as those shown in fig. 7 would take care of making the appropriate consequences explicit in the data base.

(3) Similarly something might occur to change the condition of RM17. For example, the maintenance people might report a power outage or plumbing problem in an area including RM17 that would result (again through the use of projection rules) in the assertion of tokens [e.g., (condition RM17 uninhabitable)] that would violate assumptions made by $A_{1}$ in choosing RM17.

In each of the above three situations, an assumption made in processing $A_1$ 's resource allocation request was either undermined of in danger of being undermined. In the first case, $A_2$ might avoid a conflict without ever bothering $A_1$ . If it were important, however, $A_2$ would know whom to contact. In the latter two situations, $A_1$ would be notified of the situation and presented with alternatives (e.g., an alternative room or piece of projection equipment). The actual decision making is left up to human operators.

## 5. Decision Support Systems

The TMM is designed to support fewer functions than office-tasks support systems such as those described in [3] or [1]. The TMM is not a planning system; it simply assists a number of relatively expert planners in coordinating their activities. Rather than formulate plans, the TMM assists in exploring the range of plans appropriate for achieving tasks in a given set of circumstances. Once a plan is chosen, the system keeps track of whether the reasons for choosing a given plan continue to be valid. The TMM handles certain of the well understood aspects of problem solving involving time and prerequisite conflict detection, and leaves the hard parts, such as conflict resolution, up to the agents implicated in the conflict. The functionality of the TMM can be summarized as follows:

\- The TMM provides users with information about the status and availability of resources and about the time of occurrence and duration of events. The system assists users in scheduling events to take advantage of available resources.

\- The TMM allows for several users to specify the effects and consequences of a given action or process, each according to his or her individual expertise and responsibility. These effects and consequences are stated in terms of causal relationships and rules that serve to determine tasks that should be performed under a given set of circumstances. Automatic projection rules provide the means for employees to anticipate the occurrence of important events without having to generate and scan large amounts of paper work.

\- The TMM's change driven interrupt facility and temporal reason maintenance system allow an employee to formulate automatic responses to frequently encountered problems. These mechanisms allow one to notice when conditions change so as to endanger plans and predictions made on the basis of some earlier state of the temporal data base.

\- The TMM can detect and annotate possible interactions between agents competing for the use of some shared resource. The system is capable of determining the cause of the interaction, the other agents involved, and possible fixes that might serve to resolve the conflict.

\- The TMM provides an interface for enforcing representational conventions and minimal integrity constraints. Type checking is handled by a preprocessor [10] that keeps track of known predicates, and the type and number of their arguments. A rule browser modeled after TEIRESIAS [4] allows users to inspect and modify the rule base. At their present stage of development these tools are mainly useful to programmers developing the user interface, but to give individual users greater autonomy, some of this machinery will eventually have to be integrated into functions at the user level. The system also prevents the addition of metric constraints that would render the data base inconsistent.

## 6. Extensions

The current system makes it possible to view portions of the time map graphically on a CRT screen. We're now exploring techniques whereby a user might interact with the TMM by directly manipulating this graphical display. This should be especially useful for modifying the network of constraints (e.g., specifying and updating deadlines). The information stored in the time map is somewhat more difficult to view than graphical representations such as those generated from PERT charts [11]. This is due to the uncertainty captured in the partially ordered events and fuzzy metric constraints. This uncertainty can be resolved by viewing the same information from more than one frame of reference. With a small amount of user feedback, it should be possible to determine a minimal set of displays that will provide the user with a clear idea of what's going on with regard to a given set of events.

There is also an effort underway to augment the resource management routines to handle discretely changing quantities and thus approximate the allocation and replenishment of consumable resources involving continuously changing quantities. The general problem of reason maintenance involving discretely changing quantities appears to be NP-complete. Fortunately, there are some techniques for making conservative estimates of resource availability that perform in polynomial time. We hope to show that these techniques are sufficient for many routine resource handling tasks.

## References

[1] Barber, G., Supporting organizational problem solving with a work station, ACM Transactions on Office Information Systems 1 (1983) 45–67.

[2] Clocksin, W.F. and C.S. Mellish, Programming in Prolog, Springer-Verlag (1984).

[3] Croft, W.B. and L.S. Lefkowitz, Task support in an office system, ACM Transactions on Office Information Systems 2 (1984) 197–212.

[4] Davis, Randall, TEIRESIAS: Applications of meta-level knowledge, in: Randall Davis and Douglas B. Lenat, eds.,

Knowledge-Based Systems in Artificial Intelligence, McCraw-Hill (1982) 227–490.

[5] Dean, Thomas, Planning and temporal reasoning under uncertainty, Proceedings IEEE Workshop on Principle of Knowledge-Based Systems, IEEE (1984).

[6] Dean, Thomas, Temporal imagery: An approach to reasoning about time for planning and problem solving, Technical report 433, Yale University (1985).

[7] Doyle, Jon, A truth maintenance system, Artificial Intelligence 2 (1979) 231–272.

[8] Hewitt, Carl, PLANNER: A language for proving theorems in robots, Proceedings IJCAII, Washington, D.C., IJCAI (1969).

[9] McDermott, Drew V., A temporal logic for reasoning about processes and plans, Cognitive Science 6 (1982) 101–155.

[10] McDermott, Draw V., The DUCK Manual, Technical report 399, Yale University (1985).

[11] Wiest, J.D. and F.K.. Levy, A management guide to PERT /CPM, Prentice-Hall, NJ (1969).
