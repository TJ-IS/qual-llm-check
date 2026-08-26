---
otero_id: 17012
otero_key: "54DGZGJW"
title: "SAGE: A decision support system for the sequencing of operations within a robotic workcell"
authors: "P. Freedman; A. Malowany"
year: "1988"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(88)90020-6"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# SAGE: A Decision Support System for the Sequencing of Operations within a Robotic Workcell

P. FREEDMAN and A. MALOWANY \*
Computer Vision and Robotics Laboratory, McGill Research Centre for Intelligent Machines, McGill University, Montréal, Québec, Canada

This paper describes a new approach to decision support based on logic programming. SAGE, Sequence Analysis by Graphical Evaluation, is a both a logic framework and a set of Prolog programs to express and then solve the problem of repetitive sequencing of operations within a robotics workcell. We create a Timed Petri Net from the user description consisting of the initial state of the workcell, plus the operations to be performed. Each operation is defined by (i) the command to be executed, (ii) a list of enabling conditions, (iii) a list of changes made to the state of the workcell by executing the command, and (iv) its relative integer duration. After some preliminary analysis, this net is used to generate the Task Space of all feasible time histories of workcell events. Repetitive sequences of all the workcell operations are then constructed from cycles in the Task space. From the feasible sequences thus identified, the time-optimal one is selected. SAGE clearly demonstrates both the power of symbolic expression, and the power of pattern matching as a basis for decision support systems.

Keywords: Robotics, Petri Nets, Prolog.

![](/api/attachments/54DGZGJW/fulltext/images/784492b13108c69bbcf18e509d6857602f813689bda7f1c206340aae3397769a.jpg)

Paul Freedman was born in Toronto, Ontario, on March 11, 1956. He received the B.A.Sc. degree in Engineering Science from the University of Toronto, Toronto, Ontario in 1978. From 1978–1981, he worked for the E.C.E. Group of Engineering Consultants, Toronto, Ontario, as Project Engineer in Building Automation. He subsequently earned the M.A.Sc. degree in Electrical Engineering from the University of British Columbia, Vancouver, British Columbia in 1983.

He is presently completing his doctoral degree at McGill University, Montréal, Québec. His current research interests include robotics, distributed control, and optimization methods. Mr. Freedman is a member of the Association of Professional Engineers of Ontario, and a student member of the IEEE.

\* The authors gratefully acknowledge the financial support of FCAR and NSERC.

## 1. Introduction

The complexity of robotic workcells continues to evolve, as manipulating elements such as robots are linked to sensing elements such as computer vision systems, and knowledge elements such as Expert Systems. Programming such a workcell involves much more than simply writing a program for each workcell element, because the tasks to be performed are tightly coupled. The programming effort would be enormously simplified if the 'what must be done' could be decoupled from the 'how to do it', by describing the tasks to be performed by these active workcell elements, and their interrelationships.

First, there are precedence constraints on the time ordering of possible tasks e.g. 'fetch-gripper-tool before fetch-board'. Ordinarily, these constraints link successive tasks to be performed by the same active workcell element. Second, there are constraints associated with the sharing of the passive workcell elements (resources), such as a common work area by two robots. These constraints typically link tasks to be performed by different active workcell elements. In what follows, we will use the term task to mean a unit of work to be performed e.g. 'move-board', and the term operation to mean the assignment of a task to a given active workcell element e.g. 'move board using robot R1'. The notation $op_{ij}$ will be used to denote task $j$ of active element $i$ .

![](/api/attachments/54DGZGJW/fulltext/images/1098cb0dac78aeb65886ad5aa4f15698f5348c1e73568089cc12a3b8d82fd48f.jpg)

sociation of the SME, and the Ordre des Ingenieurs du Québec.

We believe that the simplest user specification takes the form of a list of required operations plus the initial state of the workcell. Propositional logic seems to provide a natural vocabulary to describe the workcell state, since the truth value of propositions such as [jig = free] and [robot = idle] change as operations take place. But propositions are really just conditions, and if we think of operations as events, then we can draw a correspondence between the theory of condition/event Petri Nets (PNs) and propositional logic [39].

We associate with each workcell operation the following description: the conditions which enable the operation, called pre-conditions; the generic commands to be executed by the active element in order to perform the operation, called activities; the consequences of the operation, called state changes; and the execution time of the activities, called durations. We also define an instantaneous description of the workcell in terms of (i) the values of the state variables associated with the passive elements, and (ii) the operations now being executed by the active elements.

In itself, the determination of a feasible sequence of operations which satisfies the precedence and resource constraints is an NP-complete problem $[18]$ . Informally, this implies that the sequencing problem belongs to a class of problems for which there exists no efficient (polynomial time) algorithm. Therefore, problems of this nature are ordinarily solved with the aid of a Decision Support System (DSS) which searches the space of possible solutions using application-dependent heuristics. For example, a system to aid in critical path scheduling is described in $[30]$ . The problem is modelled by an activity-on-node AND/OR graph, and then solved using three different graph search algorithms.

One recent development in the field of decision support is the addition of optimization to the typical kinds of ‘what-if’ analysis [40]. And there is more to workcell ‘programming’ than simply determining a feasible sequence of operations, since workcells are typically configured to repetitively perform a given application. We would therefore like to optimize the order in which operations take place, so as to minimize the total time required [19]. Thus, it is critical to determine not just a feasible sequence of operations, but the time-optimal one, since this sequence will become the basis of the ‘program’ to be used by the workcell runtime environment [7]. The nature of this optimization is best explained by the following classification for repetitive workcell sequencing problems.

The simplest sequencing problem can be characterized as deterministic i.e. the workcell operations follow one another in a deterministic way. In this category, we also include sensing-related operations of a deterministic nature. For example, the details associated with grasping a randomly oriented part might change according to its orientation, but the 'grasping' event can be modelled as a deterministic operation (which always succeeds). However, most real world applications are not deterministic. Even when the outcome of each workcell operation is deterministic, there can occur instances when mutually exclusive operations become enabled at the same time. In each case, this non-determinism must be 'resolved' by examining the consequences of each alternative operation, in order to determine the time-optimal repetitive sequence.

In part due to the publicity surrounding the Japanese Fifth Generation research program, Prolog (PROgramming in LOGic) is now attracting increased attention in North America. A recent paper in this journal [27] suggested how Prolog could be used as a basis for decision support systems. Our results to be presented here represent one such system.

SAGE, Sequence Analysis by Graphical Evaluation, is a both a logic programming framework and set of Prolog programs to define and then solve the problem of repetitive sequencing of operations with deterministic outcomes within a robotics workcell [15,16]. We will show how both the precedence and shared resource constraints can be mapped onto a single formalism, by defining the pre-conditions and state changes of the intended operations in terms of state variables associated with the shared workcell elements. A Constraints Net (CN) is then constructed to model the constraints which link the operations, using the formalism of Timed Petri Nets [37]. A preliminary analysis detects inconsistencies or errors in the user description which give rise to graph-theoretic problems such as disconnectedness. The CN is then used to generate the Task space which makes explicit all possible concurrency among workcell operations. Repetitive sequences of the workcell operations are then constructed from cycles in this Task space. Finally, the sequence with the shortest duration is selected as the optimal one and used to derive the program for the workcell runtime environment.

This paper begins with a brief review of the relevant literature in the fields of Petri Nets, Operations Research, and Artificial Intelligence. Using a condition/event model of workcell behavior, a theory is developed in the context of Timed Petri nets to analyze the nature of repetition embedded in the user description of the workcell operations. Key parts of the analysis performed in Prolog are discussed to provide some insight into logic programming and how it differs from programming with conventional algorithmic languages. A simple example is then presented to illustrate the analysis and optimization. We conclude with a short discussion about the current implementation of SAGE and the complexity of some of our algorithms. This work is part of a larger effort within the McGill Research Centre for Intelligent machines to develop a sophisticated hierarchical programming environment for a generic robotic workcell.

## 2. Manufacturing and Petri Nets

Petri Nets are gaining increasing prominence in the manufacturing and robotics literature. Four broad research themes can be identified: modelling eg. [2], [11]; analysis and simulation eg. [1], [23], [34]; the synthesis of 'well-behaved' nets from sub-nets which model particular robotic sub-systems eg. [3], [21]; and the implementation of runtime systems eg. [9], [24], [41], [46].

Unfortunately, there has yet to emerge a standard way of modelling robotic systems, and this makes it difficult to compare research efforts. The simplest form of modelling is based on the original condition/event formalism developed by Petri, in which a token simply indicates whether or not a condition is true. In other situations, a token can be used to model the number of input parts waiting at the head of an assembly line, or the number of spaces available in an intermediate buffer. In these cases, removing a token from a place by firing a transition does not necessarily make the associated condition false. But when the user application is sufficiently complex, the large numbers of conditions and events may obscure the fundamental structure of the problem. For this reason, ‘coloured’ PNs were proposed, along with extensions to the classical analysis [22]. Instead of simply indicating the truth of a condition, a token is now allowed to take on different ‘colours’, as defined by the ‘colour set’, to represent different properties. Transitions then perform colour transformations, as defined by colour ‘functions’. For example, given a PN model of a manufacturing plant, a set of colours assigned to a ‘parts’ token might represent different kinds of parts new being manufactured. Then the colour function associated with the event ‘assembly’ would perform different assembly steps corresponding to the part type. Coloured PNs have therefore become a popular tool for modelling Flexible Manufacturing Systems (FMS) consisting of multiple robotic workcells linked by an automatic parts handling facility eg. [2].

We have adopted the binary condition/event formalism since the context of our work is the analysis of sequencing within a workcell, instead of within a FMS. Therefore, the number of operations and their inter-relationships in a typical user application is small. We also obtain a simpler description of workcell operations in terms of preconditions/post-conditions (conditions) and activities (events). Finally, we are able to exploit the correspondence with propositional logic, and programming in logic.

## 3. Manufacturing, OR, and AI

Sequencing/scheduling problems have traditionally been a part of Operations Research (OR). Most conventional techniques can be classified as (i) algebraic, such as linear or goal programming, or (ii) search with heuristics, such as branch-and-bound. But other methods have recently appeared in the OR literature which attempt to exploit results from the domain of Artificial Intelligence (AI) [44].

Of particular interest here are AI knowledge-based systems for the sequencing/planning domain in robotics [38], and Computer Integrated Manufacturing (CIM) [25]. For example, the feasibility of applying expert systems methodology to the planning domain is discussed in [47]. The authors suggest that the sub-problem called ‘process sequence selection' is best solved by a 'generate and test' (guess an answer, and then check it), or by 'selective sequence generation' guided by the problem constraints.

ISIS [14] is a knowledge-based system for planning and scheduling production in a job-shop environment. The problem of constructing a schedule is viewed as a hierarchical constraint-directed search through the space of all possibilities. There are five classes of factory-wide constraints: physical (eg. processing times of the different machines in the shop), causal (eg. job pre-conditions), resource availability, preference, and organizational (eg. cost), of which the first three are most important. The scope is factory-wide, and the research emphasizes problem representation and the satisfaction of (possibly conflicting) constraints at multiple levels.

GARI [10] is another knowledge-based system which plans a sequence of machining steps for the manufacture of mechanical parts. The planning focuses on weighted pieces of advice (which might be conflicting) about technological and economic constraints (preferences). The emphasis here is on the generation of a feasible sequence of operations from a geometric description of a part (in terms of holes, grooves, surfaces, etc.). However, the durations of operations are not modelled, and therefore sequence optimization is not discussed.

A planning formalism is described in [33] for a 'factory' consisting of a single mobile robot tending several CNC stations. Because the travel time between stations is on the order of the durations of the machining steps, the planner seeks to optimize the robot motions. The user specifies a desired partial order over the robot motions from which the robot travel times are computed. Heuristic search is used to explore alternative partial orders (robot plans) to obtain the time-optimal one. There is no discussion of coordination problems, since there are no shared resources and only one 'active' element.

A knowledge-based planning system is presented in [42] for a robotics workcell. The state of the workcell is represented in a symbolic way, via a 'world model'. Each job (task) is characterized by the duration and the set of required resources; pre-conditions and changes (additions, deletions) to the workcell are defined in terms of the world model. Precedence constraints are only invoked to resolve 'problematic interactions between planning steps', after the generation of feasible plan(s) via depth-first search. This becomes the basis of a 'dynamic' scheduler, which could flexibly respond to the arrival of different kinds of jobs at the workcell. Details about the implementation in LISP are presented in a companion paper [43].

In [29], a planning system called AC-I is developed for a multi-robot assembly workcell. The user description takes the form of a set of tasks to be performed and a routing matrix of travel times between locations in the workcell. The planning system first groups tasks with common start/stop locations into 'tours'. A traveling salesman problem is then formulated and solved for each tour to optimize the sequence of robot motions associated with the intermediate stops on the tour, according to the routing matrix. These optimized tours become the basis of the input program to the workcell run-time environment AC-II. Unfortunately, the sequence optimization is limited to just the timing of robot motions, without regard to the timing of the other tasks such as part mating which might have longer durations. The concurrency of robot tasks is not addressed as a primary concern since the optimization is based on the 'local' notion of a tour through the workcell. And tours will not always be a useful partition; we prefer to think in terms of optimizing the duration of a cycle composed of all of the assembly steps.

A different kind of optimization is described in [28] for sequencing assembly tasks within a single robot workcell. Alternatives are explicitly represented in a tree structure, and then a branch-and-bound algorithm is used to minimize the cost (assembly time).

There is increasing interest in logic programming as the basis of OR efforts [5], [27]. Unlike conventional programming which emphasizes an algorithmic or prescriptive approach, programming in Prolog has a descriptive feel because a program consists of relationships among values. This is analogous to an algebraic equation which describes how variables are related. Each definition (rule) in a Prolog program defines a relationship, and each clause in the definition specifies a condition or pattern for which the relationship holds.

Predicate logic and the mechanical theorem proving of Prolog together provide a powerful framework for solving planning problems in a manufacturing environment. For example, the suitability of Prolog for building Expert Systems for parts selection is discussed in [45].

A methodology for knowledge-based factory design is presented in [13]. The model consists of a knowledge base written in Prolog and a conventional relational database containing information such as product demands and machine specifications. The global task is decomposed into solvable components, one of which is called ‘flow path analysis/selection’. Unfortunately, no details are presented about the knowledge base itself.

A new programming language based on Prolog is described in [20] for defining the task requirements of a robotics workcell. FPROLOG extends Prolog by allowing functional and procedural programs written in LISP to be invoked as Prolog goals.

The work closest to our own is presented in [12]. A Prolog system called MASCOT is used to schedule operations on machines in a job shop. Each workcell operation is described by duration, earliest start time, latest finish time, resources required and the amounts consumed. The modelling is based on a PERT-style Activity-on-Node graph, but the graph is only used as a conceptual aid. The system uses the deadline objectives associated with resources to construct a partial order which characterizes feasible solutions. In [4], MASCOT is extended by adding a ‘decision-support’ module with heuristic knowledge, supplied by the shop-floor manager, about ‘technological constraints’. This ‘planning’ system then generates a job-shop schedule from the partial order.

## 4. Petri Nets and Timed Petri Nets

The Petri Net (PN) was first developed for modelling concurrent asynchronous systems. Events are represented by vertical bars called transitions, and the conditions associated with the events are represented by circles called places. Directed arcs between places and transitions indicate how the events and conditions are related. The presence of a token in a place indicates that the corresponding condition is 'true'. A transition 'fires' when all of its input conditions are true i.e. all of its input places are marked with a token. The firing then removes one token from each input place and deposits one token in each output place. The marking of the net is defined by the presence or absence of tokens in all the places. A sample PN is shown in Fig. 1. With the marking as shown in (a), only transition $t_{1}$ is enabled. The marking of the net after firing $t_{1}$ is shown in (b).

![](/api/attachments/54DGZGJW/fulltext/images/6183fe332cef659326a9387e118b4b8e27b256c289294329a67bd7d281d11638.jpg)  
Fig. 1. A sample Petri Net. With the marking shown in (a), just transition $t_{1}$ is enabled. The marking after the firing of $t_{1}$ is shown in (b).

As described in [27], the PN can be thought of as a combination of PERT and State Transition diagrams. The PERT diagram is typically a network of 'activities' linked by precedence relations; nodes represent instants in time and arcs represent the activities. PERT diagrams model concurrency, but cannot model coordination of events which does not respect a strict precedence relation. For example, consider a robotics workcell with two robots with overlapping work areas. If we think of the common work area as a resource for which the robots compete, then robot motions through the common work area are coupled, but not according to a strict precedence relation. This kind of behavior cannot be modelled by PERT diagram.

The PERT diagram has one further limitation in the context of repetitive sequencing. Since the graph is a representation of the precedence among events from 'start' to 'finish', it is strictly acyclic. Therefore, repetitive behavior can only be modelled at this global level and not at the level of individual operations.

Conversely, State Transition Diagrams (STD) model choice, but not concurrency. The dynamic behavior of the system is described in terms of the changing values of 'state variables' associated with observable elements of the system. A distinct node in the STD is associated with each 'state' and the dynamic behavior of the system is represented by arcs between states.

This kind of modelling becomes cumbersome when the system is asynchronous, since the description of asynchronous events must still be represented in a ‘centralized’ way. For example, consider a simple robotic workcell consisting of two robots R1, R2 working independently. If R1 has three tasks and R2 has two tasks, then we would require a total of $3! \times 2! = 12$ nodes to describe all possible ‘states’ of R1 and R2 at work (without considering ‘idle’ states). For this reason, the STD is not used for modelling asynchronous systems. The PN model effectively overcomes this limitation by ‘partitioning’ the system state into a set of conditions mapped to places. In this way, the complete state is represented by the distribution of tokens in the places i.e. marking of the net.

Given an initial marking, the set of all markings which can be ‘reached’ by firing the transitions (as they become enabled) is called the Reachability Tree (RT) of the initial marking. For a PN with m places and n transitions, we also define the $m \times n$ Incidence Matrix C as follows: $C(i, j) = -1$ if place $p_{i}$ is an input to transition $t_{j}, +1$ if place $p_{i}$ is an output of transition $t_{j}$ , and 0 otherwise. A good summary of PN research can be found in [36].

When studying conditional event systems, there are two properties which have particular importance, from an ‘operational’ perspective. Since places represent conditions which can only be true (a token present) or false (no token), we need to ensure that the token count at each place is always just 1 or 0. A PN with this property is called safe. (More generally, if the token count at each place is $\leq k$ , then the PN is called k-bounded.) In addition, we would like to know whether a particular sequence of operations can result in deadlock. If this cannot occur, we say that the PN is live. Therefore, we will expect ‘meaningful’ PNs to be LS (live and safe).

Finally, a PN is strongly connected if there exist simple paths between any two places. Practically, we shall see that strong connectivity implies that all of the transitions are sufficiently ‘bound’ together so that their firings will be eventually synchronized.

There are at least three ways of approaching the analysis of PNs. First, the behavior of the net can be simulated for all valid initial markings, and statistics can then be gathered about the occupancy of place, and whether deadlocks occur. As with all simulations, this requires much time, and extensive computing resources. A second approach makes use of Reachability Tree. By inspecting each marking in the RT, we can determine whether the PN is safe and deadlock-free. But when the size of the PN is large, the RT can quickly become too large to easily generate and analyze.

A third approach to analysis is via a linear-algebraic tool called the p-invariant [26]. Informally, a set of places form a p-invariant if the token count over all the places is constant for all markings reachable from the initial marking. When the PN is strongly connected, the (proper) p-invariants correspond to linearly independent circuits within the net, identified by a set of places. It is shown in [3] that if each place belongs to at least one p-invariant and if the token count over each p-invariant is 1, then the PN is LS.

From an engineering perspective, PNs have limited modelling power because there is no sense of time. Transitions 'fire' instantaneously, and there is no concept of clock. From among the many ways of adding timing extensions [32], we have adopted the notation of Ramchandani [37] which associates fixed durations with transitions. His Timed Petri Net (TPN) has proved to be adequate for our workcell sequencing problems since, as in most real-time applications, the execution times of events such as robot motions or image processing can be predicted quite accurately.

Of course, the addition of timing alters the firing behavior of the net transitions. Fortunately, a sufficient (but not necessary) condition for a TPN to be LS is for the non-timed PN to be LS.

The following definitions [37] form the basis for our study of repetitive firing behavior.

A firing sequence is cyclic if it takes the initial marking back to itself, and if each transition in the TPN is fired at least once. A TPN is consistent $\Leftrightarrow$ there exists an assignment of positive integer values called 'currents' to the transitions such that the sum of these 'currents' entering and leaving each place in the TPN is zero. If we let $C$ denote the Incidence Matrix of the TPN, then the current assignment can be found as the solution to $C\phi = 0$ where $\phi[i] > 0$ can be thought of as the 'current' flowing along transition $t_i$ . Ramchandani then showed that consistency as a property of strongly connected TPNs gives rise to repetitive firing behavior in the following way.

Theorem 1: A strongly connected TPN which is LS is consistent, and must have an initial marking for which there exists a cyclic firing sequence.

We can therefore make use of p-invariant analysis to verify that the classical (non-timed) PN of a given TPN is LS, and then conclude that the TPN is LS. Thus, it must also be consistent and have a cyclic firing sequence.

But what kind of real-time behavior results when markings within the RT of the TPN re-occur? To understand this correspondence, we can register the firing of the transitions along a time axis. A firing schedule for a TPN is a set of time instants at which transitions fire. There is one important distinction to be made between the RT and the firing schedule. As previously described, we generate the RT by firing the transitions enabled in a given marking, one at a time. The firing schedule is obtained by firing all of the enabled transitions at the same time. Thus, the markings implicit in the firing schedule are just a subset of the complete RT.

A firing schedule is periodic if the repetitive firings of all transitions occur within a given time window. If the time interval $\pi$ between consecutive firings of all transitions is the same, the firing schedule is called strongly periodic. If the TPN is strongly connected, then all transitions fire with the same period $\pi$ , and therefore the processing rate of the net is constant. In this case, the cyclic firing sequence will include the firings of all transitions in the TPN.

## 5. Logic Programming and Prolog

In First Order Logic (FOL), knowledge is represented as logical propositions written as well-formed-formulas (wff's). The 'first order' means that wffs may incorporate variables (and 'second order' would mean using variables to represent wff's). A wff might have 'declarative' semantics such as 'parent(bill, sam)' i.e. 'bill' is the parent of 'sam', or it might have 'procedural' semantics such as 'parent (X, Y):-child(Y, X)' i.e. 'X' is the parent of 'Y' if 'Y' is the child of 'X'.

Knowledge implicit in the procedural semantics can be combined with the declarative semantics to infer or ‘prove’ new facts. In Prolog, this is accomplished by first translating associations of propositions into a special form called Horn clauses (by eliminating conditions, moving negation inward, replacing existential quantifiers with Skolem functions, and distributing conjunction over disjunction) [8]. The mechanical theorem proving is based on a mechanism called resolution/unification which uses depth-first search.

The basic Prolog data structure is the list. The $[H|T]$ notation is provided to identify H, the head of the list, and the remainder T, called the 'tail'. Thus, given a list $L1 = [a, b, c, d]$ , would obtain from pattern matching H = [a], and T = b, c, d]. When the list contains just one element eg. $L2 = [e]$ , we would obtain H = [e] and T = [] i.e. the empty list.

In Fig. 2, we present a Prolog fragment adapted from one of the SAGE programs for the breadth-

go(Count):- retract(path(Count.D.D.C)).    /\* have found a loop ! \*/
    assert if new(C).    /\* maybe a new circuit ? \*/
    go(Count).

go(Count):- retract(path(Count,D.N.C)).
    successors(N.L).
    New\_count is Count + 1.
    update\_paths(New\_count,D.L.C).
    go(Count).

go(Count):- path(...,...). /\* still paths ? \*/
New\_count is Count + 1.
go(New\_count).
go(-). /\* no more "path"s, so stop ! \*/ first determination of linearly independent circuits in a digraph in terms of arcs. The usual Prolog notation [8] reserves names which begin with lower case letters for predicates, and those which begin with upper case letters for variables. Conjunctive clauses within a rule are linked by commas. The key data structure is the following: 'path (Count, D, N, C)' where 'Count' is the iteration counter, 'D' is the origin node (which will eventually become the destination), 'N' is the current frontier node, and 'C' is a list of arcs traversed thus far which will (possibly) form a circuit. The symbol '-' is the universal pattern match to denote a don't care condition.

This predicate ‘go’ is defined by four rules. Prolog attempts to use them in the order in which they are written. The first is a ‘stopping’ rule which selectively removes possible solutions from further consideration. When the current frontier node and origin node coincide i.e. both are ‘D’, the list ‘C’ of arcs traversed thus far must form a circuit. The ‘path’ data structure is then deleted (via ‘retract’) from the Prolog database and ‘C’ is passed as a parameter to the predicate ‘assert-if-new’. If ‘C’ is not a permutation of an existing circuit, ‘assert-if-new’ adds it to the database (via ‘assert’) as a new linearly independent circuit. We then continue the search for other circuits by calling ‘go’ once more.

For paths which are not yet circuits, the first rule fails and Prolog examines the second rule. An expanded path is now created for each successor of the current frontier node 'N' i.e. for the elements of the list 'L', via 'update-paths' with an incremented count. Then 'go' is called once more.

Once all paths with the given ‘Count’ have been expanded, the second rule fails and the third rule is examined. As long as there are still paths to be explored, ‘Count’ is incremented and we ‘go’ again. If all of the paths have indeed become circuits, then this rule fails and the fourth rule is used to halt the search.

Note the descriptive nature of programming in Prolog. A separate rule is written for each kind of situation to be faced as the search for circuits takes place. There is nothing algorithmic encoded here, except insofar as the rules are listed. We also wish to emphasize the importance of recursion; each rule, except the last one, re-invokes the entire 'go' predicate.

## 6. The Constraints Net

The CN is a TPN constructed from the user description consisting of the operations to be performed and the initial state of the workcell. As explained in the introduction, the constraints linking the operations can be characterized as (i) those associated with the precedence ordering, and (ii) those associated with the sharing of resources. In order to map both onto a single condition/event formalism, we define a set of state variables associated with passive workcell elements such as shared jigs. A state variable might be boolean such as 'jig = {free, occupied}' or multi-valued such as 'board-in-jig = {new, inspected, repaired, checked}'. From the state variables and their values, we then define conditions which are either true or false eg. [jig = free]. These conditions are used to construct the pre-conditions and state changes of each operation. (The actual selection of state variables is left to the user, since this is closely tied to the application itself; it should be clear that this selection is not unique. This same philosophy is followed in network analysis, where the problem solver is free to choose a set of independent currents or voltages, or in control systems design where the choice of state variables is often based on engineering judgement.)

To map precedence constraints among operations to pre-conditions, we can define a multivalued state variable with a distinct value corresponding to each operation. For example, given 'repair' and 'checking' operations, the precedence constraint 'repair before checking' could be restated as follows. Beginning with the state variable 'board-in-jig' which takes on values {repaired, checked}, we can define [board-in-jig = repaired] as a pre-condition of the checking operation and the state change of the repair operation.

The mapping of shared resource constraints to pre-conditions is made simple by creating a distinct state variable for each resource. For example, given a common work are used by two robots for different operations, we could associate [shared-area = free] with the pre-conditions of both robot operations.

Our intended workcell runtime environment [7] imposes extra structure on our programming paradigm. (i) For each workcell operation, there must be a 1:1 correspondence between the state variables associated with the pre-conditions and the state variables associated with the state changes. (ii) If the same condition is a pre-condition of multiple operations, or if the same condition is a state change of multiple operations, these operations must be mutually exclusive.

The following theorem summarizes the relationship between the state variables in the user description and the p-invariants in the CN.

Theorem 2: All the conditions of a state variable in a strongly connected CN form a unique p-invariant.

Combining our two theorems, we obtain the following result.

Theorem 3: Given a strongly connected CN, any initial marking which assigns just 1 token to each state variable will be LS. Furthermore, all such markings will give rise to the same strongly periodic behavior.

## 6.1. Checking Strong Connectivity

According to [26], the strongly connected components $\{c_{i}\}$ of a PN with m places and n transitions can be obtained as the non-negative integer solutions c of Cc=0, where C is the Incidence Matrix of PN. If there exists a unique solution, then the PN is strongly connected i.e. there is just one strongly connected component. But this algebraic approach requires that the CN be explicitly represented by its Incidence Matrix, which is inherently unsuitable for modelling self-loops associated with resource sharing. In addition, the numerical solution of such an integer programming problem would be subject to errors due to truncation and roundoff. We have therefore developed the following non-numerical approach based on the algorithm outlined in fig. 2 for finding linearly independent circuits in a digraph.

We begin with a digraph representation of the CN in which transitions appear as nodes and places appear as arcs. A tour in this digraph is a closed path consisting of alternating arcs and nodes. Each linearly independent tour obtained via our graph traversal algorithm is a strongly component if the following is true. For each transition in the tour, all the input places and all the output places in the original CN must be a part of the tour. If there is only one strongly connected component, then the CN is strongly connected.

The time complexity of this connectivity analysis is $\mathcal{O}(nm)$ , where n is the number of nodes in the digraph (operations in the CN) and m is the number of arcs (conditions). This can be seen by examining the limiting situations associated with possible CN configurations.

Let $n_{T}$ be the number of tours in the CN. If $n_{T}=1$ , then all n operations belong to the same tour. There is therefore just one search path in the graph traversal, so the tour is identified in n steps.

Alternatively, if $n_{T}=n$ , then each operation is associated with a distinct tour. In this case, there are n parallel search paths and each tour is identified in 1 step. Therefore, the complexity of the tour identification is $O(n)$ .

The complexity of merging related tours has $O(nm)$ complexity. This can be seen by considering the worst case situation in which each operation i has $n_{i}^{p} > 1$ multiple pre-conditions and $n_{i}^{s} > 1$ multiple state changes; observe that $n_{i}^{p}$ , $n_{i}^{s} < m/2\forall i$ i.e. the numbers of pre-conditions and state changes must each be less than half the total number of conditions. Since each operation would give rise to $n_{i}^{p} + n_{i}^{s} < m$ merges and there are n operations, the merging is of order $O(nm)$ complexity. Therefore, the complexity of the tour identification and analysis is $O(2nm)$ , or more simply $O(nm)$ .

## 6.2. P-Invariants from Circuits

Given a PN with m places and n transitions, the $m \times 1$ p-invariants $\{s_{i}\}$ are traditionally obtained as the non-negative integer solutions of $C's = 0$ (0 is $n \times 1$ ) where C is the Incidence Matrix of PN. But numerical approaches to solving this integer programming problem are prone to exactly the same problems previously described for obtaining the strongly connected components. For this reason, other algebraic methods have been developed to obtain the p-invariants via direct manipulation of C eg. [31], but these generate spurious solutions which must then be deleted.

Our method exploits the correspondence between p-invariants and circuits (Theorem 2) using the digraph representation of the non-timed PN in which transitions (operations) are mapped to nodes and places (conditions) are mapped to arcs. The digraph is required in order to associate a circuit, defined b a set of arcs, with a p-invariant defined by a set of places. A root node for each circuit is first selected from among the conditions associated with each state variable, and then the multiple paths are expanded in parallel. The algorithm used is a slightly modified version of the Prolog fragment shown in fig. 2.

The time complexity of the p-invariant identification and analysis is $O(nm)$ . This can be seen by examining the limiting situations associated with possible CN configurations. Let $n_{p}$ be the number of p-invariants. If $n_{p}=1$ , then all m conditions belong to the same p-invariant. In this case, there is just one search path and the p-invariant is identified in $O(n)$ steps. If $n_{p}=n$ , then there are n parallel search paths and each p-invariant is identified in 1 step. Thus the time complexity of the p-invariant identification is $O(n)$ .

Once the p-invariants of the CN are identified, two types of checking must be performed to ensure that the CN is indeed LS. First, each condition must belong to at least one p-invariant. Since there are m conditions, this requires m steps.

Second, the token count of each p-invariant must be exactly 1 i.e. just one condition associated with each p-invariant must be true in the initial state as provided by the user. If $n_{p}=1$ , then all m conditions belong to the same p-invariant and the checking requires m steps. If $n_{p}=m$ , then each condition is associated with a distinct p-invariant and the checking requires 1 step for each of the m p-invariants. Thus the combined time complexity of the two types of checking is $O(2m)$ or more simply $O(m)$ . Therefore, the time complexity of the complete p-invariant identification and analysis is $O(nm)$ .

## 6.3. From Firing Schedule to Task Space

To facilitate sequence optimization, we would like to represent the time history of the execution of the CN in a way that makes explicit the concurrency of workcell events. We define a suitable representation called the Task space which combines the firing schedule of the TPN with the markings implicit in the schedule. A node in the Task space consists of a pair of fields: (i) a set of arguments, one per workcell element, which indicate the operations now being concurrently performed, and (ii) the resulting state of the workcell i.e. the new marking of the CN, as described by the values of the state variables. As noted previously, nodes in the Task space represent just a subset of the RT of the initial marking.

A closed path in this Task space is called a cycle, composed of a transient portion which does not repeat, and a repetitive portion which characterizes the fundamental repetitive behavior of the CN.

Theorem 4: There exists a 1:1 mapping from cyclic firing sequences in the RT to cycles in the Task space. Moreover, the cycles in the Task space of a strongly connected CN will all share the same repetitive portion.

Nodes in the Task space will change if the durations of the operations change sufficiently to alter their possible concurrency. We would then expect to discover a new cycle with a repetitive portion of different duration. However, changing the initial marking cannot alter the fundamental behavior of the CN.

In contrast to the PN simulation described in $[27]$ , we do not directly manipulate tokens to generate the Task space of the CN. Instead, the nodes are obtained as follows. After assigning an initial state to the workcell, a list of feasible operations are identified for each active workcell element. This identification is performed by the pattern matching of Prolog; there is no queue maintained for operations which are 'likely' to fire i.e. operations with pre-conditions which are the state changes of currently executing operations. A new node is created for each permutation of elements in these lists. Time is then advanced by 1 clock 'tick' and the state of the workcell is updated; certain changes which were pending become current, and new changes are posted as pending.

After initial transients, nodes associated with repetitive behavior will be 're-discovered.' At this point, cycles in the Task space are identified using the same kind of graph traversal algorithm previously described for finding the linearly independent circuits in a digraph.

The generation of candidate successor operations is performed by two predicates (rules) working together. The first predicate simply marks as successors those operations with pre-conditions satisfied in the current state of the workcell; this creates a feasible set of candidates. The second predicate is a heuristic which prunes candidates which appear less promising.

Thus far, we have experimented with three simple application-independent heuristics. The first one seeks to maximize the concurrency of operations at each time step by discarding successor candidates with unforced 'idle'ness. Using this heuristic, we can only be sure that the true optimal sequence will be found when all operations have the same duration. The second heuristic ranks the successor candidates according to their number of pre-conditions. This reflects the philosophy that the more pre-conditions associated with an operation, the more rarely all those pre-conditions will be satisfied. The third heuristic is the dual of the second; it ranks candidates according to their number of state changes. In this way, the candidates which bring about the most changes to the workcell are pursued first. This heuristic pruning of the search ensures that our search space will grow 'deep' instead of 'broad', so that the 'looping back' to previously discovered nodes will occur more quickly.

The time complexity of the Task space generation and analysis is difficult to measure, since it depends upon how the operations are inter-related, and their durations.

## 7. An Example

The following example is adapted from research in our laboratory about the inspection and repair of hybrid integrated circuits and printed circuit boards [17].

Consider a robotics workcell configured for the repair of printed circuit boards; see fig. 3. There are three active elements: robot R1, robot R2, and the conveyor belt fixtured for two jigs. There are six operations to be performed. Robot R1 is responsible for moving 'new' boards from the input-tray to a repair-jig, and the 'repaired' boards from the repair-jig to a checking-jig mounted on the conveyor. Robot R2 carries out the pre-defined repair using a dedicated repair tool, and the checking of the repair using a different sensor-based tool. The conveyor is responsible for moving the 'checked' boards out of the workcell; the unloading at the output-tray automatically puts the second jig, mounted on the other end of the conveyor, in the proper position for the checking operation. We assume that there is always a new board in the input-tray, and that there is always room for another board in the output-tray. And to stay within a deterministic framework, we assume that the checking always succeeds i.e. the repair is always correctly performed.

![](/api/attachments/54DGZGJW/fulltext/images/4cb22167d910a2c627df380afa7339545e2c200b267456ea0ee9d4d2b6aba950.jpg)  
Fig. 3. The workcell configuration.

Rather than associating synchronization with the workpieces themselves (boards) which are cycling through the workcell, we define three enumerative state variables in terms of the resident jigs as follows: 'board-in-repair-jig = {null, new, repaired}'; 'board-in-checking-jig = {null, repaired, checked}'; 'board-in-unloading-jig = {null, checked}'. The 'null' value simply indicates that the corresponding jig is free and in its default position.

Now we can define the workcell operations. To distinguish between the active workcell elements (which perform the operations) and the passive elements, we use the following Prolog notation: (i) status-ae(element number, task currently being performed), and (ii) status-pe(state variable, current value).

Here is the user definition for $op_{11}$ , the first task (repair) of the first active element (R2).

activities (1, 1, [repair])

pre-conditions (1, 1, [status-pe(board-in-repair-jig, new)]),

state-changes(1, 1, [status-pe(board-in-repair-jig, repaired)]),

duration ([1,1], [5])

The pre-condition to repair is simply that a 'new' board is present in the repair-jig. After the repair, the status of the board is changed to 'repaired'. The duration of this operation is 5 time units.

![](/api/attachments/54DGZGJW/fulltext/images/67b8566ad84b5dc8e82a6cba9ac8582a87cbeda35738163563f68a68961053a6.jpg)

<table><tr><td>Place (condition)</td><td>Description</td></tr><tr><td>1</td><td>board_in_checking_jig = checked</td></tr><tr><td>2</td><td>board_in_repair_jig = repaired</td></tr><tr><td>3</td><td>board_in_checking_jig = null</td></tr><tr><td>4</td><td>board_in_repair_jig = null</td></tr><tr><td>5</td><td>board_in_checking_jig = repaired</td></tr><tr><td>6</td><td>board_in_repair_jig = new</td></tr><tr><td>7</td><td>board_in_unloading_jig = checked</td></tr><tr><td>8</td><td>board_in_unloading_jig = null</td></tr><tr><td>Transition (activity)</td><td>Description</td></tr><tr><td> $op_{11}$ </td><td>repair</td></tr><tr><td> $op_{12}$ </td><td>check_the_repair</td></tr><tr><td> $op_{21}$ </td><td>move_board_from_input_tray_to_repair_jig</td></tr><tr><td> $op_{22}$ </td><td>move_board_from_repair_jig_to_checking_jig</td></tr><tr><td> $op_{31}$ </td><td>move_checking_jig_to_unloading_position</td></tr><tr><td> $op_{32}$ </td><td>unload_board_into_output_tray</td></tr></table>

Fig. 4. A sample Constraints Net.

The strongly connected CN corresponding to the example is shown in fig. 4. The three circuits in the CN correspond to the three state variables (and their associated values): repair-jig, checking-jig, unloading-jig. The connecting workcell operations $op_{22}$ and $op_{31}$ are responsible for synchronizing the movement of boards among the jigs.

This example is representative of many practical sequencing problems. The durations of the operations vary from 2 to 5 time units. There are operations which can take place in parallel, such as moving a 'new' board to the repair-jig while a 'repaired' one is checked in the checking-jig. Similarly, there are many instances when operations must be synchronized eg. before a 'checked' board can exit the workcell, the unloading-jig on the other end of the conveyor must be empty. This example also exhibits internal non-determinism: given the initial state defined by a 'new' board in the repair-jig and a 'repaired' board in the checking-jig, R2 can perform either the repair or checking operation first.

## 7.1. Preliminary Analysis

SAGE first confirms that the CN derived from the user description is strongly connected, and then verifies that it is LS, in the sense that its non-timed PN is LS.

![](/api/attachments/54DGZGJW/fulltext/images/5141eee9e6e4959ae54e45509f5aec8e39962812fc99aeb65d05f975ed81dbfb.jpg)  
Fig. 5. The sample Task Space.

In this example, there are 3 linearly independent p-invariants: $\{p_{1}, p_{3}, p_{5}\}, \{p_{2}, p_{4}, p_{6}\}$ , and $\{p_{7}, p_{8}\}$ , and each p-invariant links all of the conditions associated with a distinct jig (Theorem 2). Given the LS initial marking $\{p_{5}=1, p_{6}=1, p_{8}=1\}$ , SAGE concludes that the CN is LS as required.

## 7.2. The Task Space

The structure of the Task space for our example problem is shown in fig. 5.

Given the initial state {status-pe(board-in-repair-jig, new), status-pe(board-in-checking-jig, repaired), status-pe(board-in-unloading-jig, null)}, only two transitions in the CN are enabled: $op_{11}$ (repair the new board) and $op_{12}$ (check the repaired board); the other two active elements are idle. Since both require robot R2, SAGE creates two distinct successor nodes in the Task space. The operation $op_{11}$ is followed by $op_{12}$ and then $op_{31}$ . Alternatively, if the first operation is $op_{12}$ , then operations $op_{11}$ and $op_{31}$ take place concurrently. Eventually, both paths in the Task space merge (after operations $op_{11}$ , $op_{12}$ , $op_{31}$ , $op_{32}$ are performed) and then the single repetitive portion becomes apparent characterized by notes 3, 5, 7, 8. Because the Task space of this example has little branching, all three heuristics perform equivalently.

The Task space for this example has ten nodes and two complete cycles: $c_{1}$ links 5 nodes, and $c_{2}$ links 9 nodes. As predicted by Theorem 4, both cycles have identical repetitive portions consisting of four nodes (11 time units). However, the transient portion of $c_{1}$ consists of just 1 node (duration = 3 time units) while the transient portion of $c_{2}$ consists of 5 nodes (duration = 14 time units). Therefore, $c_{1}$ is used to construct the input program to the workcell runtime environment.

## 8. Implementation

SAGE currently comprises a set of Unix utilities (shell scripts and awk filters) and a series of programs written in GProlog [6], a superset of C-Prolog [35] which makes available the graphics support of Sun-3 workstations running UNIX.

For the example presented above, the preliminary analysis of the CN (to verify strong connectivity, identify and analyze the 3 p-invariants) takes about 2 seconds of CPU time. The generation of the Task space and the determination of the time-optimal sequence takes about 9 seconds.

We also have some limited experience with larger sequencing problems drawn from the published literature. One such example, based on a description of a robot workcell configured for automatic assembly $[24]$ comprises 10 task which are assigned to 2 robots, a conveyor system, and a robot cart. The identification and analysis of the 6 p-invariants takes about 6 seconds of CPU time; the longest p-invariant has 7 places. The generation of the Task space (8 nodes) plus the determination of the time-optimal sequence takes about 9 seconds.

## 9. Conclusions

This paper has described a new approach to decision support based on logic programming. SAGE, Sequence Analysis by Graphical Evaluation, is both a logic programming framework and a set of Prolog programs to define and then solve the problem of repetitive sequencing of operations within a robotics workcell. A Timed Petri Net called the Constraints Net (CN) is created from the user description consisting of the initial state of the workcell, plus the operations to be performed. We associate with each workcell operation the following description: the conditions which enable the operation, called pre-conditions; the generic commands to be executed by the active element in order to perform the operation, called activities; the consequences of the operation, called state-changes; and the (fixed) execution times of the activities, called durations. We also define an instantaneous description of the workcell in terms of (i) the values of the state variables associated with the passive elements, and (ii) the operations now being executed by the active elements.

After some preliminary analysis (to verify strong connectivity, identify and analyze the p-invariants), the CN is used to generate, in a breadth-first manner, the Task Space which makes explicit all possible concurrency among the workcell operations. Repetitive sequences of all the workcell operations are then constructed from cycles in the Task space. From the feasible sequences thus identified, the time-optimal one is selected. SAGE clearly demonstrates both the power of symbolic expression, and the power of pattern matching as a basis for decision support systems.

Unfortunately, not all workcell operations can be described in a deterministic way. Sophisticated applications typically demand sensory feedback on-line to determine what should be done. In the case of our example, we would expect to discover, every now and then, that the repair was incorrectly performed (otherwise, the checking step could be eliminated). This might mean moving the board back to the repair-jig to perform the repair again, or perhaps sending the board to a 'scrap' bin. But what can optimization mean if there are alternative sequences of workcell operations due to sensory input? The answer seems to be this: for each possible decision point related to sensory input (say, of an inspection task), determine the optimal sequence thereafter. In most cases, the number of such decision points, and thus the number of alternative sequences, is small enough to make this framework sensible.

This same approach can be used to include the kind of modelling of error/failure and subsequent recovery described in [3]. Extra conditions would be added to model alternative outcomes of an operation i.e. success/failure, and then new operations would be added associated with the recovery. SAGE would then generate extra time-optimal sequences for the error recovery from the failure states. We are currently exploring the consequences of this approach within the TPN framework.

## References

[1] P. Alanche, K. Benzakour, F. Dollé, P. Gillet, P. Rodrigues, R. Valette, PSI: A Petri Net Based Simulator for Flexible Manufacturing Systems, Lecture Notes in Computer Science: Advances in Petri Nets (1984), Vol. 188, Springer-Verlag, 1985.

[2] H. Alla, P. Ladet, Coloured Petri Nets: a Tool for Modelling, Validation, and Simulation of FMS, in Flexible Manufacturing Systems: Methods and Studies, A. Kusiak (ed.), North-Holland, 1986.

[3] C. Beck, Modelling and Simulation of Flexible Control Structures for Automated Manufacturing Systems, M.Sc. Dissertation, Carnegie-Mellon University, 1985.

[4] E. Bensana, M. Correge, G. Bel, D. Dubois, An Expert-

system Approach to Industrial Job-shop Scheduling, Proc. IEEE Int. Conf. on Robotics and Automation, 1986.

[5] R. Bharath, Logic Programming: A Tool for MS/OR?, Interfaces, Vol. 16, no. 5, September/October 1986.

[6] B. Brachman, G-Prolog User's Manual, Internal Report, Dept. Computer Science, University of British Columbia, October 29, 1985.

[7] G. Carayannis, A. Malowany, Improving the Programmability of Robotic Workcells, Proc. CG International '88 Conf., 1988.

[8] W. Clocksin, C. Mellish, Programming in Prolog, Springer-Verlag, 1984.

[9] D. Crockett, A. Desrochers, Manufacturing Workstation Control using Petri Nets, Technical Report, Robotics and Automation Laboratory, Rensselaer Polytechnic Institute, August 1986.

[10] Y. Descotte, J.-C. Latombe, GAR1: a problem solver that plans how to machine mechanical parts, Proc. IJCAI Conf., 1981.

[11] D. Dubois, K. Stecke, Using Petri Nets to Represent Production Systems, Proc. IEEE CDC Conf., 1983.

[12] J. Erschuler, P. Esquirol, Decision-aid in Job Shop Scheduling: a knowledge-based approach, Proc. IEEE Int. Conf. on Robotics and Automation, 1986.

[13] E. Fisher, Logic-based Factory Design, Proc. IEEE Int. Conf. on Robotics and Automation, 1985.

[14] M. Fox, S. Smith, ISIS – a knowledge based system for factory scheduling, Expert Systems, Vol. 1, no. 1, 1984.

[15] P. Freedman, A. Malowany, Sequencing Tasks within a Robotics Workcell: from feasibility to optimality, Proc. IEEE Pacific Rim Conf., Victoria, B.C., June 1987.

[16] P. Freedman, A. Malowany, The Analysis and Optimization of Repetition within a Robot Workcell Sequencing Problems, Proc. IEEE Int. Conf. Robotics and Automation, 1988.

[17] P. Freedman, G. Carayannis, D. Gauthier, D., A. Malowany, A Session Layer for a Distributed Robotics Environment, Proc. IEEE COMPINT '85 Conf., 1985.

[18] M. Garey, D. Johnson, Computers and Intractability: A Guide to Theory of NP-completeness, Freeman and Co., 1979.

[19] G. Giralt, Research Trends in Decisional and Multisensory Aspects of Third Generation Robots, Proc. 2nd Int. Symp. on Robotics Research, MIT Press, 1985.

[20] S. Hutchinson, A. Kak, FProlog: A Language to Integrate Logic and Functional Programming for Automated Assembly, Proc. IEEE Int. Conf. on Robotics and Automation, 1986.

[21] G. Hutchinson, A. Clementson, Manufacturing Control Systems: an approach to reducing software costs, Robotics and Computer Aided Manufacturing, Vol. 1, no. 3/4, 1984.

[22] K. Jensen, Coloured Petri Nets and the Invariant Method, Theoretical Computer Science, Vol. 14, 1981.

[23] H. Kodate, K. Fujii, K. Yamanoi, Representation of FMS with Petri Net Graph and its Application to Simulation of System Operation, Robotics and Computer Aided manufacturing, Vol. 3, no. 3, 1987.

[24] N. Komoda, K. Kera, T. Kubo, An Autonomous, Decentralized Control System for Factory Automation, IEEE Computer, Vol. 17, no. 12, December 1984.

[25] A. Kusiak, Artificial Intelligence and Operations Research in Flexible manufacturing Systems, INFOR, Vol. 25, no. 1, 1987.

[26] K. Lautenbach, H. Schmid, Use of Petri Nets for Proving Correctness of Concurrent Process Systems, Information Processing '74: Proceedings of the IFIP Congress, North Holland, 1974.

[27] R. Lee, L. Miller, A Logic Programming Framework for Planning and Simulation, Decision Support Systems, Vol. 2, 1986.

[28] J. Lee, T. Raz, Optimization of Robot Assembly Planning, Proc. IEEE Int. Conf. on Robotics and Automation 1987.

[29] O. Maimon, Activity Controller for a Multiple Robot Assembly Cell, Ph. D. Dissertation, Purdue University, 1984.

[30] R. Marcus, An Application of Artificial Intelligence to Operations Research, Communications of the ACM, Vol. 27, no. 10, October 1984.

[31] J. Martinez, M. Silva, A Simple and Fast Algorithm to Obtain all Invariants of a Generalized Petri Net, Lecture Notes in Computer Science, No. 52, Springer-Verlag, 1980.

[32] M. Menasche, PAREDE: An Automated Tool for the Analysis of Time(d) Petri Nets, Proc. IEEE Int. Workshop on Timed Petri Nets, Torino, Italy, July 1985.

[33] D. Miller, R. Firby, T. Dean, Deadlines, Travel Time, and Robot Problem Solving, Proc. IJCAI Conf., 1985.

[34] T. Murata, N. Komoda, K. Matsumoto, K. Haruna, A Petri Net-based Controller for Flexible and Maintainable Sequence Control and its Applications in Factory Automation, IEEE Trans. on Industrial Electronics, Vol. 33, no. 1, February 1986.

[35] F. Pereira, C-Prolog User's Manual, Dept. Architecture, University of Edinburgh, February 1984.

[36] J. Peterson, Petri Net Theory and the modelling of Systems, Prentice-Hall, 1981.

[37] C. Ramchandani. Analysis of Asynchronous Concurrent systems by Petri Nets, Technical Report, MIT/LCS/TR-120, M.I.T., February 1974.

[38] P. Rayson, A Review of Expert Systems Principles and their roles in manufacturing Systems, Robotica, Vol. 3, 1985.

[39] W. Reisig, Petri Nets - an introduction, Springer-Verlag, 1985.

[40] A. Roy, From What-if to What's-best in DSS, Decision Support Systems, Vol. 3, 1987, pp. 27–35.

[41] T. Sha, K. Fujisaki, E. Masada, Microcomputer Implementation of Event Driven System based on Table Analysis of Petri Net, Proc. IEEE IECON Conf., 1985.

[42] M. Shaw, A. Whinston, Automatic Planning + Flexible Scheduling: A Knowledge based Approach, Proc. IEEE Int. Conf. on Robotics and Automation, 1985.

[43] M. Shaw, A. Whinston, Applications of Artificial Intelligence to Planning and Scheduling in flexible Manufacturing, in Flexible Manufacturing Systems: Methods and Studies, A. Kusiak (ed.), North-Holland, 1986.

[44] H. Simon, Two Heads Are Better Than One: The Collaboration Between AI and OR, Interfaces, Vol. 17, no. 4, July/August 1987.

[45] S. Subramanyam, R. Askin, An Expert Systems Approach to Scheduling in Flexible Manufacturing Systems, in Flexible Manufacturing Systems: Methods and Studies, A. Kusiak (ed.), North-Holland, 1986.

[46] E. Thuriot, R. Valette, M. Courvoisier, Implementation of a Centralized Synchronization Concept for Production systems, Proc. IEEE Conf. on Real-Time Systems, 1983.

[47] M. Wu, C. Liu, Automated Process Planning and Expert Systems, Proc. IEEE Int. Conf. on Robotics and Automation, 1985.
