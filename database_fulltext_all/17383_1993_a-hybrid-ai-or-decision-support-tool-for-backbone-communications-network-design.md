---
otero_id: 17383
otero_key: "MJ6G6ZVN"
title: "A hybrid AI/OR decision support tool for backbone communications network design"
authors: "Amitava Dutta; Sabyasachi Mitra"
year: "1993"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(93)90068-e"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A hybrid AI/OR decision support tool for backbone communications network design

Amitava Dutta

George Mason University, Fairfax, VA, USA

Sabyasachi Mitra

Louisiana State University, Baton Rouge, LA, USA

Much of existing DSS literature views the role of human expertise as primarily that of selecting appropriate formal models for solving a problem or synthesizing sequences thereof. Once a model (or model sequence) is determined, values of decision variables are determined by the model(s) alone. Hence, automated methods for facilitating model selection and synthesis have received considerable attention. However, a single model is often not an accurate abstraction of reality. Also, results from multiple formal models often have to be combined heuristically to obtain practical solutions. Thus, in this paper we explore the premise that human expertise needs to interact with formal models during the process of searching for solution values. Specifically, we describe a hybrid decision support tool for the design of backbone communication networks, a problem recognized as being of considerable complexity. An internal representation of the design process that employs a blackboard, a truth maintenance system and dependency directed backtracking, allows human expertise and formal models to jointly determine decision variable values in a uniform manner. The design tool has been implemented using a combination of Lisp and Fortran. Computational experiments indicate that incorporating human expertise during the search process results in superior complete solutions and added flexibility in satisfying ad hoc requirements. We conjecture that this hybrid search approach is not limited to the telecommunication network design problem and can be extended to other applications.

Keywords: Hybrid search; Telecommunication networks; Topological design; Truth maintenance; User interface; Model management; Model integration

1. Introduction

Design occupies a central role in such disciplines as engineering and management science. The purpose of the design process is to assign permissible values to a set of design variables, in order to minimise (or maximise) an objective stated in terms of such variables. Traditionally, Operations Research literature has focussed on the development of mathematical models as abstractions of real-life decision problems, and related procedures to traverse the search space of the problem in an efficient and systematic manner. Artificial intelligence literature, on the other hand, has primarily been concerned with the representation and manipulation of heuristic knowledge, and its use in solving complex decision problems. [10] enumerates the advantages of these

![](/api/attachments/MJ6G6ZVN/fulltext/images/b99a95b218fda3725a491ba544e2b6b762bed25c1d912f57e01ecfab8562edf6.jpg)

Amitava Dutta is Professor of Management Information Systems at George Mason University. He received his Ph.D. from Purdue University and a B.Tech (Electronics and Communications Engineering) from the Indian Institute of Technology, Kharagpur. His research interests include decision support systems and cost issues in planning and operation of communication networks. Dutta is on the editorial board of Expert Systems: Research and Applications, and

is a member of the IEEE, ACM, ORSA and TIMS. His papers have appeared in journals such as Decision Support Systems, Operations Research, IEEE Transactions on Communications, and IEEE Transactions on Knowledge and Data Engineering.

![](/api/attachments/MJ6G6ZVN/fulltext/images/dea492ab284a2f298599449ba22526a9b772dce50b36be9811ca5180cc704dc2.jpg)

Sabyasachi Mitra received his Bachelor of Technology degree from the Indian Institute of Technology, Kanpur in 1985. He received his Doctor of Philosophy degree in Business Administration from the University of Iowa, Iowa City. He is currently Assistant Professor of Management Information Systems at the College of Business at Louisiana State University, Baton Rouge. His research interests include telecommunication network design, AI/OR hybrid search methods, decision support systems, expert systems and distributed databases. He is a member of the Operations Research Society of America and the Institute of Management Science.

approaches, and argues that both modelling and heuristic knowledge are essential to solving complex design problems.

It is also well recognised in DSS literature [6] [25] that human judgement and experience are often crucial to the design process. Although sophisticated optimisation algorithms and tested heuristic methods may have been developed, several design problems involve complex and adhoc issues that are difficult to include in such formulations. The output from automated procedures may need to be suitably modified by human experts to meet a variety of real life criteria. Consequently, a major portion of any design process is still intuitive and informal [22]. It is in such areas of problem solving that humans excel. In dealing with complexity, he is irreplacable by even the most dizzying superstructures of mathematical analysis. Thus, several authors [29] have argued that the human should be the core around which design techniques are built to amplify his own decision making abilities.

Much of the research in this regard has focussed on the development of effective and intelligent human interfaces to otherwise automated procedures. The goals of such interfaces have been (1) to aid the human designer in formulating and structuring the design problem, (2) to aid him in selecting models to solve the problem, and (3) to remove several of the procedural details in instantiating such models. Such interfaces have been developed for single model environments [8] [17] [18] [21] [23] [24], as well as for problem environments which involve several models with sophisticated interrelationships [1] [3] [4] [5] [14] [20]. For example, [8] presents a generalised model management system which aids the designer in formulating mathematical programming applications. [18] presents a first order logic based language to formulate linear programming models of production, distribution and inventory problems. [20] describes a language for specifying model input/output and defining composite models based on these specifications using grammatical construction rules. [14] describes a formal mathematical framework for conceiving, representing and manipulating a wide variety of models. [21] provides an interface to the LP model, while [24] develops an interface for a statistical analysis software (MULTIVARIANCE). [5] describes DANEX, a prototype knowledge-based software to support users in data analysis problems. [3] gives the design features of a complex system to support users in scheduling problems, by making available to them a wide range of algorithmic tools in the field.

In this paper, we examine a different approach to incorporating human expertise in the design. Specifically, we involve the user in the search process itself, by viewing him as yet another source of design knowledge, similar to the optimisation algorithms and heuristic methods mentioned earlier. The research issue, in this case, is to develop an effective method of combining design transformations formulated by heterogeneous sources of knowledge (e.g. human experts, optimisation algorithms, heuristic procedures etc.). There are two important advantages that may result from such an approach. First, several adhoc constraints and issues which are difficult to include in a purely automated search process, can be incorporated through human participation. Second, a human is often able to make local changes to the current design state in order to obtain superior numerical results.

In an earlier paper $[10]$ , we presented a method which combines optimisation algorithms with heuristic methods, to create a computer based tool for the design of backbone communication networks. As the network design evolved, its current state was stored on a blackboard, accessible by all interacting sources of knowledge. A truth maintenance system (TMS) recorded justifications for choices leading to the current design state, as well as for promising alternatives not selected. A dependency directed backtracking procedure (DDBP) worked in conjunction with the TMS to choose other alternatives when a current partial design could not be feasibly completed. The truth maintenance system described in $[10]$ provides a convenient mechanism to integrate design transformations formulated by optimisation algorithms and heuristic design methods.

In this paper, we show how the same mechanism can also be used to integrate design transformations formulated by a human expert. The emphasis of this paper is on the use of a truth maintenance system in an interactive environment. The resulting interactive tool has been coded using a combination of Lisp and Fortran programming languages. Through several computational experiments reported in this paper, we demonstrate the two advantages of the interactive tool, mentioned in the preceding paragraph.

The rest of the paper is organised as follows. Section 1.1 describes the telecommunication network design problem addressed in this paper. Section 2 describes the automated design tool, discussed in detail in [10]. Several details have been omitted, since they are not important to the discussion here. Section 3 describes the design and implementation of the truth maintenance system as a primary mechanism for integrating heterogeneous knowledge sources. Section 4 describes the interactive design tool and shows how the TMS can be effectively used in an interactive environment. A sample interaction with the design tool illustrates its major features. Section 5 describes the results of computational experiments performed with the interactive tool. Sections 6 summarises the major conclusions of this research.

## 1.1 The telecommunication network design problem

A discussion of the complete network design problem is beyond the scope of this paper. Suffice it to say here that it is usually decomposed $[7]$ into the design of the local access network, which generally has a tree structure, and the backbone network, which has a general topology. For purposes of this paper, we concentrate on the more complex backbone network, since the integration concepts put forth herein, are also applicable to the local access design. A general statement of the backbone topological design problem (BTDP) $[7]$ is as follows:

## Given:

(1) The Node (IMP) locations

(2) Peak hour traffic requirements

(3) An upper limit on the average packet delay in the network

(4) Reliability requirements

(5) Cost elements (line tarriff structures, switch costs etc.)

(6) Technological constraints (e.g. capacity limits, discreteness of capacity etc.)

## Decide:

(1) Link placements (topology)

(2) Capacity assignment on links (3) Flow allocation on links and routing

Objective: Minimise total network cost such that the traffic, delay and reliability requirements are satisfied within the technological constraints

There is no single model available in the literature that encompasses all aspects of the general design problem stated above. Early efforts examined subproblems in isolation. The Flow deviation method $[12]$ determined good routing given the link placements and the capacities of the links. Subsequently, several algorithms were developed, based on flow deviation, to iterate between capacity assignment and flow allocation until a local minima was reached $[15]$ $[16]$ . More recently, sophisticated optimisation algorithms have been developed for several subproblems (see $[13]$ for a survey of such literature). These methods do not address the reliability requirements of the network. The reliability literature $[2]$ $[26]$ $[27]$ $[28]$ , on the other hand, concentrate on the reliability estimation of given networks, or on synthesising graphs that meet a variety of reliability criteria. The determination of capacity or flow assignment is not considered in these efforts. It is evident from the literature survey that existing algorithms address different aspects of the BTDP and individually provide partial solutions to the design problem. The automated tool described in $[10]$ and summarised in the next section, attempts to generate a solution to the BTDP by integrating the partial solutions generated by several optimisation and algorithmic modules, through the use of a truth maintenance system and a dependency directed backtracking procedure. The interactive tool described in section 4 incorporates human expertise in the search process, as well.

Although the reliability of communication networks can be defined in a number of ways $[2]$ $[27]$ , this paper addresses the following 3 reliability constraints. First, an edge-connectivity requirement is specified for each node pair in the network. More specifically, a basic minimum connectivity (K) is specified for all node pairs, while a few important node pairs (i, j) may require higher connectivity ( $K_{ij}$ ). Second, a maximum limit is placed on the number of hops in the shortest hop path between every node pair. It is argued that the failure probability of the network increases with the presence of long chains in the network. Third, a maximum limit is placed on the degree of every node in the network. The failure of a node with a large number of links incident to it greatly disrupts the normal operation of the network. The interactive design tool can also incorporate other reliability measures, without major modifications to the solution procedure.

## 2. The automated design tool

In this section, we provide an overview of the automated design tool described in detail in $[10]$ $[19]$ . The emphasis of this section is on the structure of the automated design tool and the method of integration of modelling and heuristic knowledge in solving the BTDP. In section 3, we describe in detail the truth maintenance system as a primary mechanism for achieving such an integration. In section 4, we describe how the same mechanism can be used to integrate design transformations formulated by a human designer, as well. The material presented in this section and the next forms the basis for sections 4 and 5.

## 2.1. Integrating heterogeneous sources of knowledge

In the final analysis, a topological design is completed by assigning appropriate values to its design variables. Different knowledge sources (optimisation algorithms, heuristic modules, human experts etc.) can be thought of as performing transformations to partial designs, on the way to a complete design (see the description of a General Problem Solver in [22]). Integration is achieved first by representing the current design state in such a way as to be usable by all the knowledge sources. Second, since the BTDP is too complex for any knowledge source to guage the global effects of the transformations it makes to the current design state, it is possible that conflicting transformations will be made, and a mechanism will be necessary to back out of dead-ends. Specifically, these are achieved by a truth maintenance system (TMS) and a dependency directed backtracking procedure (DDBP), respectively.

![](/api/attachments/MJ6G6ZVN/fulltext/images/36c6282cbbc24a4435336ea29843432133122dcb68ae8a2bda73ab6f18a214d0.jpg)  
Fig. 1. The blackboard architecture of the hybrid design tool.

## 2.2. The blackboard architecture

Fig. 1 shows the architecture of the automated design tool. The interactive tool discussed in section 4 uses the same architecture, with minimal modifications. A “blackboard” holds common data structures accessible by all interacting modules. Each module has one or more triggering conditions written on the blackboard. A module becomes a candidate for invocation when any of its triggering conditions become active. One of the modules accessing the blackboard is designated the Blackboard Scheduler (BBS). This module keeps track of the triggering conditions for each module and maintains a queue of all modules that are candidates for invocation. Each module has an user defined priority that is used by the BBS in choosing modules for invocation from the queue. Thus, the BBS is independent of the specific tasks performed by each module and transfers control back and forth between modules based on the status of their triggering conditions and priorities. Modules 1–6 in Fig. 1 represent different sources of design knowledge, while modules 7, 8 and 9 support truth maintenance, error recovery and blackboard scheduling, respectively.

## 2.3. Modules 1–6: Sources of design knowledge

Module 1a in Fig. 1 is the Basic Search Module (BSM) which generates good initial link placements that might not satisfy the reliability constraints. This module is based on a lagrangian formulation [13] of the BTDP (without the reliability constraints). The lagrangian formulation is obtained by relaxing a few constraints for the BTDP by multiplying them with a set of lagrange multipliers and adding to the objective function. For any valid set of lagrange multipliers, the lagrangian problem is optimally solvable. It is well known in optimisation literature that the optimal value of the lagrangian problem is a lower bound on the optimal value of the original problem. The procedure starts with an arbitrary initial set of multipliers and the topology obtained by solving the lagrangian problem (for that value of the multipliers) is written on the blackboard.

The topology generated by the BSM might not satisfy the reliability constraints, and these are handled by the corrective modules 2–5. The triggering conditions for the corrective modules are activated by the truth maintenance procedure (explained in the next section) when the current solution does not satisfy the basic connectivity, special connectivity, shortest path or the degree constraint (see section 1.1), respectively. Each corrective module uses a heuristic cost estimate for each link to add/delete links from the current topology, to meet the corresponding reliability constraint. Module 2 uses a modified version of an algorithm reported in [11] to determine "groups" of nodes in the current topology, such that nodes in the same group are K-edge-connected to each other, but the connectivity across groups is less than K. It then determines the best set of links that can be added across groups to make the network K-edge-connected as a whole. Module 3 is invoked for every node pair (i, j) with a higher connectivity requirement not satisfied in the current topology. It uses a breadth-first search algorithm to generate partial paths from node i towards node j, and vice versa. It then determines the best set of links that can be added across the partial paths, in order to complete additional edge-disjoint paths between the two nodes. Module 5 is invoked for every node i in the current topology which has more than the maximum specified number of links adjacent to it. It calculates the number of excess links adjacent to node i, and then determines the best set of such links that can be removed from the topology to satisfy the degree constraint. Module 4, corresponding to the shortest path constraint, has not been implemented in the automated tool. Instead, we describe in sections 4 and 5 how such a constraint can be easily incorporated through user participation in the search process.

Module 1b is the Initial Flow Allocation (IFA) module which is invoked when a valid topology satisfying all the reliability constraints is found (this is indicated when the triggering conditions for the corrective modules are inactive). This module has been incorporated as a part of module 1 in Fig. 1 because the lagrangian formulation can be reworked to obtain a set of feasible initial flows. Module 6 is the Capacity and Flow Allocation (CFA) module which is invoked when a valid topology and a set of initial feasible flows have been found. This module generates a set of low cost capacities for the links, such that the delay and traffic requirements of the network are satisfied. At this stage, one iteration of the procedure is completed, and the BSM is invoked again. The subgradient optimisation procedure [13] in the BSM updates the lagrange multipliers, the lagrangian problem is resolved, a new topology is written on the blackboard, and the process continues till a specified stopping criterion [13] is valid.

This concludes a brief discussion of the automated design tool. The details of the lagrangian formulation, the subgradient optimisation procedure and the heuristic modules have been omitted from the discussion and may be found in $[10]$ $[19]$ . In the next section, we describe the truth maintenance system and the dependency directed backtracking procedure in detail.

## 3. The truth maintenance system

The truth maintenance system (TMS) and the dependency directed backtracking procedure (DDBP) presented in this section form the primary mechanism through which design transformations formulated by the various heterogeneous modules are integrated to generate good feasible solutions to the BTDP. As we shall discuss in section 4, the TMS and DDBP also provide a convenient mechanism to integrate design transformations formulated by a human expert. Few notations and terms have been used in this section and they have been described in the text wherever appropriate.

## 3.1. The need for a TMS and DDBP

Each of the corrective modules accessing the blackboard represent local procedures which add/delete links to satisfy the corresponding reliability constraint. Thus, they might act at cross purposes to each other. For example, module 2 may add links to the topology which are later deleted by module 5. Thus, there is the possibility of cycling, where each module nullifies the transformationS made by the other modules and the search returns to a previously visited state.

To overcome this problem, corrective modules are not allowed to make direct transformations to the current solution state. Instead, each corrective module is required to submit a “suggestion” consisting of a sequence of alternate transformations. Each of the alternate transformations within a suggestion, achieve the same purpose and only one of them is chosen for implementation. The choice is made on more global information than is available to the recovery modules in isolation. Thus, a suggestion, $SUGG_{i}$ , is a disjunct of the form $(t^{i1} \vee t^{i2} \ldots \vee t^{ib})$ where i is the suggestion number, b is the maximum permissible number of disjuncts in a suggestion, and each $t^{ij}$ (j = 1..b) is an alternate transformation which adds and/or deletes one or more links from the current topology to satisfy a constraint. Exactly one transformation (disjunct) from each suggestion is implemented.

![](/api/attachments/MJ6G6ZVN/fulltext/images/ef7773092bce55d759510b15a5c8fc08e3117cab39e537768e01786bede32e3b.jpg)  
Fig. 2. The search tree of alternate transformations.

The disjunct chosen for implementation is determined as follows. Two transformations from different suggestions are said to “conflict” with each other, if one of them adds a link and the other deletes the same link, or vice versa. Let CHOSEN denote the set of all transformations which have been implemented thus far. When a corrective module submits a new suggestion, the disjunct chosen for implementation is the one which conflicts with the minimum number of transformations in CHOSEN. In case of a tie, the lowest cost alternative is chosen. If the chosen transformation does not conflict with any transformations in CHOSEN, no backtracking is necessary. Otherwise, the set CHOSEN is altered by a specialised backtracking procedure called dependency directed backtracking (DDB), to remove the conflict.

The advantages of using a dependency directed backtracking procedure is explained through Fig. 2. Consider the transformation $t^{k3}$ chosen for implementation, which conflicts with transformation $t^{12}$ in CHOSEN. If a chronological backtracking mechanism is employed, the procedure might backtrack to level 1 to remove the conflict, thereby losing all the work done in the later stages. With dependency directed backtracking (DDB) [9], only those decisions which contribute to the conflict, are modified. The DDB procedure is explained in section 3.4.

## 3.2. The TMS overview

The TMS presented here is based on the system described in [9]. It serves 3 purposes. First, it stores justifications for design transformations made by different knowledge sources. This is required by the DDB procedure to alter the design in the event of a conflict. Second, it provides a mechanism to automatically make the necessary changes to the set of decision variables, when a transformation is added to/deleted from the current design. Third, it automatically updates the triggering conditions as changes are made to the set of decision variables. We will explain the workings of the TMS through a small example and then follow it with the formal algorithm.

The current design state is represented on the blackboard by a collection of statements with unique statement numbers. Each statement has a justification set consisting of one or more justifications of the form JU((in-list), (out-list)). A justification is valid if all statements in its in-list are valid and all statements in its out-list are invalid. A statement is valid if it has atleast one valid justification in its justification set. A justification of the form JU((), ()) with empty in-list and out-list is called a premise justification, and is always valid. The justification of any statement can be traced back to one or more premise justifications. For the BTDP, three statement types are defined.

The first corresponds to links in the network. For each candidate link 1, two separate statements (LINK $_1$ and NOLINK $_1$ ) are created. Only one of these is valid at any time, indicating inclusion or exclusion of the link from the current topology, respectively. The second statement type corresponds to triggering conditions for the modules. A statement (BASCON) is created for the basic connectivity constraint. A statement (SP-CONN $_{ij}$ ) is created for each node pair requiring a higher than basic connectivity. A statement (SPT $_{ij}$ ) is created for the shortest path constraint between nodes i and j, for every node pair in the network. Finally, a statement (DEG $_i$ ) is created for each node i in the network, for the degree constraints. Whenever a statement representing a triggering condition is invalid, the corresponding module becomes a candidate for invocation. The third statement type, called a Suggestion statement, is for design transformations suggested by the modules. A suggestion, SUGG $_i$ , is a disjunct ( $t^{il} \vee t^{i2} \ldots \vee t^{ib}$ ) of alternate transformations, only one of which can be implemented at any point in time (see section 3.1 for details and notation). For each disjunct ( $t^{ij}$ ) in a suggestion, a suggestion statement is created. At any time, only one of these statements, corresponding to the transformation chosen for implementation, is made valid through a premise justification.

Fig. 3a and b show such statements and their justifications using a 4 node example network.

<table><tr><td></td><td>ST.NO</td><td>STATEMENT</td><td>JUSTIFICATIONS</td><td>VALID</td></tr><tr><td>1</td><td>LINK 1,2</td><td>JU( ), (2))</td><td>T</td><td></td></tr><tr><td>2</td><td>NOLINK 1,2</td><td></td><td>F</td><td></td></tr><tr><td>3</td><td>LINK 1,3</td><td></td><td>F</td><td></td></tr><tr><td>4</td><td>NOLINK 1,3</td><td>JU( ), (3)</td><td>T</td><td></td></tr><tr><td>5</td><td>LINK 1,4</td><td></td><td>F</td><td></td></tr><tr><td>6</td><td>NOLINK 1,4</td><td>JU( ), (5))</td><td>T</td><td></td></tr><tr><td>7</td><td>LINK 2,3</td><td>JU( ), (8))</td><td>T</td><td></td></tr><tr><td>8</td><td>NOLINK 2,3</td><td></td><td>F</td><td></td></tr><tr><td>9</td><td>LINK 2,4</td><td>JU( ), (10))</td><td>T</td><td></td></tr><tr><td>10</td><td>NOLINK 2,4</td><td></td><td>F</td><td></td></tr><tr><td>11</td><td>LINK 3,4</td><td>JU( ), (12))</td><td>T</td><td></td></tr><tr><td>12</td><td>NOLINK 3,4</td><td></td><td>F</td><td></td></tr><tr><td>13</td><td>BASCON</td><td>NO</td><td>F</td><td></td></tr><tr><td>14</td><td>DEG 1</td><td>JUSTIFICATIONS</td><td>F</td><td></td></tr><tr><td>15</td><td>DEG 2</td><td>YET</td><td>F</td><td></td></tr><tr><td>16</td><td>DEG 3</td><td></td><td>F</td><td></td></tr><tr><td>17</td><td>DEG 4</td><td></td><td>F</td><td></td></tr></table>

(a)

![](/api/attachments/MJ6G6ZVN/fulltext/images/99c9e3b294eeaf57eba8e9e0e70fbbf711a765a4cff6a33f767d9942d092b6a4.jpg)  
(b)  
Fig. 3. The TMS and various statements on the blackboard.

For simplicity, there are no shortest path or special connectivity requirements therein. A basic connectivity requirement of 2 edge-disjoint paths is assumed for each node pair and the maximum allowable degree of a node is 2.

For the state of the design represented by Fig. 3a, notice that there are LINK and NOLINK statements corresponding to each possible link. However, only statements 1, 4, 6, 7, 9 and 11 have valid justifications, corresponding to the presence or absence of the corresponding links from the topology. In Fig. 3a, all the justifications for the LINK and NOLINK statements have the corresponding complement statement in its out-list (the complement statement for LINK $_{i}$ is NOLINK $_{1}$ and vice versa) and an empty in-list. For instance, the justification for statement 6 is JU(( ), (5)), which says that statement 6 is valid since every statement in the in-list (in this case empty) is true, while every statement in its out-list (i.e. statement 5), is false. Such a justification is called a “weak” justification (identified in Fig. 3a). A weak justification has an empty in-list, thus depending on the invalidity of the statement in its out-list, and it represents a form of default reasoning. Weak justifications are inserted by the BSM and they can be later invalidated when a corrective module validates the statement in its out-list, to satisfy a constraint. Statements 13–17, corresponding to triggering conditions do not have any justifications as they have not yet been tested. However, it is clear that the network in Fig. 3a violates the basic connectivity constraint, and the degree constraint for node 2.

Since the BASCON statement has no valid justification at this stage, module 2 is invoked. Ignore, for the moment, how the knowledge sources suggest design transformations. Compare the networks in Figs. 3a and b, and the corresponding changes on the blackboard. Notice that the suggestion from module 2, consisting of two disjuncts, results in statements s-1-1 and s-1-2 (s indicates a suggestion statement, the first number is the suggestion number and the second number represents the disjunct within the suggestion). As either would suffice, statement s-1-2 (the least cost alternative) is selected by adding a premise justification, JU( ), ( ), therewith. Statement s-1-1 remains as an alternate choice, should the current course of transformations become infeasible. Notice also, that justifications have been inserted for statements 3 and 5. These justifications are called “strong” justifications (identified in Fig. 3b) and they have a suggestion statement in the in-list and an empty out-list. Statement 3 is now valid, while statement 5 is still invalid. Module 2 also inserts two justifications for the BASCON statement, indicating the two ways in which the basic connectivity constraint is satisfied by implementing either one of the two alternate transformations (s-1-1 and s-1-2). For the state of the design represented in Fig. 3b, the first justification of the BASCON statement is valid. If suggestion statement s-1-1 had been chosen in stead, the second justification of the BASCON statement would have been valid. The maintenance of justifications, and propagation of the effects of selected suggestions on existing statements constitutes the major duties of the TMS.

## 3.3. The truth maintenance algorithm (TMA)

We now state the algorithm itself. It is first necessary to introduce some terms, indicated in italics. As mentioned earlier, a statement is valid if it has atleast one valid justification. For each valid statement, TMS singles out one valid justification as the Supporting Justification for the statement. The Support Set of a valid statement is simply the set of all statements listed in the in-list and out-list of its supporting justification. For invalid statements, the TMS arbitrarily chooses an invalid statement from the in-list or a valid statement from the out-list of every justification in the justification set of the statement. Thus, the Support Set of the triggering conditions would include the LINK and NOLINK statements, while the Support Set of the LINK and NOLINK statements would include the suggestion statements. The definition of Support Set implies that the validity of a statement cannot change without a change in the validity of at least one statement in its Support Set. The Consequence Set of a statement i is the set of all statements which mention i in their Support Sets. The Repercussion Set of a statement i is the transitive closure of its Consequence Set, i.e. the Consequence Set of statement i, their Consequence Sets, and so forth. Thus, the Repercussion Set for the LINK and NOLINK statements would include the triggering conditions, while the Repercussion Set of the suggestion statements would include both the LINK and NOLINK statements and the triggering conditions. The Repercussion Set of statement i indicates the set of statements which may be affected by a change in the status of statement i. The Conflict Set of a suggestion statement s-i-j, is the set of all suggestion statements which justify a complement of statements justified by s-i-j. The Active Conflict Set of a suggestion statement is the set of all currently valid suggestion statements in its Conflict Set. The TMS stores the Support Set, Consequence Set and Conflict Set as part of the statement data structure and generates the Active Conflict Set whenever necessary. The Support Set is not directly required by the Truth Maintenance Algorithm, but is stored for future use.

The Truth Maintenance Algorithm (TMA) is now presented in somewhat aggregated form. It is invoked whenever a new suggestion (SUGG $_{i}$ ) is sent in by a corrective module.

Procedure Truth Maintenance;

STEP 1.0 For each disjunct ( $t^{ij}$ ) in suggestion $SUGG_{i} = (t^{il} \vee \ldots t^{ib})$

1.1 Create a suggestion statement uniquely numbered s-i-j

1.2 Justify existing LINK and NOLINK statements listed in $t^{ij}$ with a strong justification of the form JU ((s-i-j), ()).

STEP 2.0

2.1 List $\leftarrow \phi$

2.2 Choose the suggestion statement (disjunct) s-i-j (j = 1..b) whose Active Conflict Set (AC $_{ij}$ ) is of the least cardinality

2.3 Make this statement active by adding a premise justification to it.

2.4 List $\leftarrow$ Repercussion Set of s-i-j

2.5 IF $\mathrm{AC}_{\mathrm{ji}} = \phi$ Goto STEP 3.0

ELSE Invoke the DDB procedure to remove the conflict by altering a minimal set of valid suggestion statements

2.7 List ← List + {Repercussion Set of all suggestion statements whose status have been changed by the DDB procedure}

STEP 3.0

3.1 Mark each statement in List with a support status of “unknown” (a statement can have a support status of unknown only during the execution of the TMA)

3.2 FOR each statement in List DO;

3.2.1 If the Statement has a support status of nil, check the statement for validity or invalidity (remember that a statement can have justifications formulated in terms of statements with “unknown” status. Such justifications also have unknown status. Thus, a statement is valid if it has atleast one valid justification. A statement is invalid if it has all invalid (not unknown) justifications. Otherwise, a statement has an unknown status)

If the statement is valid/invalid then

(1) mark the statement as valid/invalid

(2) recursively perform 3.2.1 for all statements in the Consequence set of this statement with a support status of unknown.

ELSE do nothing (the support status of this statement is still unknown and its processing is postponed).

(At the end of Step 3.2, all statements would be marked valid or invalid.)

End of Truth Maintenance Algorithm

## 3.4. The dependency directed backtracking procedure (DDBP)

The DDBF is invoked whenever a new suggestion statement (s-i-j) with a premise justification conflicts with other valid suggestion statements. The DDBP forms a list of all such suggestion statements (AC $_{ij}$ ) and attempts to choose alternate suggestion statements for each element in the list. These alternate suggestion statements might in turn conflict with other valid suggestion statements and the DDBP is recursively executed till a user specified level. Thus the DDBP may report failure, although it rarely did in any of our experimental runs. Based on this observation, if the DDBP fails, the Error Recovery module is invoked. This module empties the queue and invokes the BSM again by activating its triggering condition, in order to start the next iteration. The details of the DDB procedure is outlined next. The procedure is invoked whenever a suggestion statement, s-i-j, chosen for implementation, has a non-empty Active Conflict Set (AC $_{ij}$ ).

Procedure Dependency Directed Backtracking (AC $_{ij}$ )

Step 1.0 For each suggestion statement (s-l-m) $\in$ AC $_{ij}$ DO

1.1 Find alternate suggestion (s-l-k) with minimal ACTIVE CONFLICTSET(k< >m)

1.2 Make (s-l-m) invalid and (s-l-k) valid by changing the premise justifications;

1.3 If $\mathbf{AC}_{\mathbf{lk}}$ is non-empty then

If the search has reached a user specified maximum level, STOP and indicate failure, ELSE, call the DDB procedure recursively with $AC_{lk}$ ;

![](/api/attachments/MJ6G6ZVN/fulltext/images/94a880c7e1fcc47aa584ff7c24cb86ee9285d5635f3dd453d577c8451dd50cde.jpg)  
(a)

![](/api/attachments/MJ6G6ZVN/fulltext/images/458e006ae84976ff35640189499ca379e28814c0a8b1457bea91ea1438afa9b9.jpg)  
(b)  
Fig. 4. The dependency directed backtracking procedure.

Step 2.0 If 1.0 reported failure, then activate the Error Recovery module triggering condition and STOP. Otherwise, a solution has been found.

End of Dependency Directed Backtracking Procedure

The functioning of the DDBP is explained by continuing with the design in Fig. 4. For convenience, Fig. 3b is repeated in 4a. Statements 14–17 do not have valid justifications on the blackboard, since they have not yet been tested. It can be visually observed that the degree constraints of nodes 2 and 3 are violated. Thus module 5 is invoked and it sends in a suggestion with the single disjunct (Delete Link (1, 3) AND Delete Link (2, 4)). The TMS faithfully creates a suggestion statement (statement s-2-1 of Fig. 4b) and gives it a premise justification. Propagating the effects of this suggestion results in the TMS inserting a justification for NOLINK statements 4 and 10. Unfortunately, statement s-2-1 conflicts with the currently valid suggestion statement s-1-2, invoking the DDBP. The latter looks for alternatives which would remove the conflict, resulting in selection of the alternate suggestion statement s-1-1, which has an empty Active Conflict Set. The resulting topology shown in Fig. 4b meets all the reliability constraints. Justifications for statements 14–17 have also been inserted. Notice also, for the BASCON statement, the first justification is invalid but the second is now valid. Figs. 3 and 4 show how the TMS and DDBP work hand in hand to integrate the suggestions of different knowledge sources.

Readers familiar with the TMA and DDBP reported in [9] will notice a few changes to the algorithms. First, the TMA in [9] has been greatly simplified here because of the absence of a special type of justification called Conditional-Proof (CP) justifications used in [9]. CP justifications are used in only special circumstances [9] and we found no use for them for the problem at hand. Second, the DDBP is made recursive such that all conflicts are resolved (or failure indicated) at one pass of the DDBP. Further, by choosing the alternates with minimal Active Conflict Sets, the DDBP searches the space more efficiently. In [9], the DDB algorithm blindly chooses an alternate to make active, and conflicts introduced by the alternate are resolved when the TMA invokes the DDB algorithm again. In general, we have exploited to some degree, the special structure of the problem at hand to make these changes.

## 3.5. The complexity of the truth maintenance algorithm

It is important to analyze the complexity and worst case behavior of the Truth Maintenance Algorithm. In the analysis which follows, let b be the maximum number of disjuncts per suggestion, let m be the total number of candidate links, let s be the number of active suggestion statements on the blackboard, and let t be the total number of triggering conditions on the blackboard.

It is fairly obvious that Step 1.0 of the TMA requires O(b) computations. Ignore Step 2.0 for the moment. In the worst case, the List in Step 3.0 contains all the LINK/NOLINK statements and the triggering conditions, a total of $(2 * m + t)$ statements. Step 3.2.1 is executed for each of these statements. Moreover, for each of the $2 * m$ LINK/NOLINK statements, Step 3.2.1 is executed recursively for all triggering statements in its consequence set. In the worst case, each LINK/NOLINK statement may have t triggering conditions in its consequence set. Thus, Step 3.2.1 may be executed O(m \* t) times. Note that the TMA could have been simplified by taking advantage of the special structure of this specific problem and processing all the LINK/NOLINK statements first and then the triggering conditions. In that case, Step 3.2.1 need not have been performed recursively and would need to be executed O(m + t) times. However, the general algorithm given in [9] has been partly retained so that some other statement types may be added later without a change to the TMA.

All steps in Step 2.0 (except 2.5) require O(1) computations. Step 2.5 calls a recursive procedure (DDBP) and requires further analysis. In the worst case, the Active Conflict Set (AC $_{ij}$ ) in Step 2.5 contains all the other s-1 active suggestion statements. For each of these statements, the DDBP chooses alternate suggestion statements. Moreover, each of the newly activated suggestion statements, in turn, may conflict with s-1 other active suggestion statements and the DDBP is executed recursively till an user specified level (u). Thus, in the worst case, O(s $^{u}$ ) executions of the DDBP may be required. In all experimental runs, we used a value of 2 for u. Therefore, in the worst case, Step 2.5 required O(s $^{2}$ ) computations. The analysis above gives the worst case behavior of the TMA. The actual CPU times required in the average case are reported in section 5.

## 4. An interactive design tool

The quality of solutions generated by the automated design tool described in section 2 can be significantly enhanced through human participation in the search process, in two ways. First, a human is better able to incorporate ad-hoc constraints and issues which are difficult to include in the automated version of the design tool. Second, a human designer is often able to make local changes to the current design state, to obtain superior numerical results. In this section, we show how the automated tool can be easily extended to support human interaction, with minimal changes to the existing procedure. The truth maintenance system described in section 3 also provides a convenient mechanism to integrate design transformations formulated by a human expert. Through several computational experiments reported in section 5, we demonstrate the important advantages of the resulting interactive design tool.

Although the automated tool is not interactive, its architecture facilitates human participation in the search process. Its modular structure provides us with convenient breakpoints in the search process, where the human expert may be allowed to make design transformations. Further, the truth maintenance system and dependency directed backtracking procedures can serve as convenient vehicles to integrate such design transformations with those formulated by optimisation algorithms and heuristic procedures. Thus, integration is achieved by perceiving the human expert as another source of design knowledge, similar to the optimisation algorithms and heuristic procedures, described earlier.

## 4.1. Interaction through a user module

All human interaction is supported through a separate user module, which is similar to the other modules accessing the blackboard. As before, this module is invoked by the BBS depending on the status of its triggering conditions and priority. Introducing such a module requires minimal changes to the existing design tool, beyond that of specifying its priority and triggering conditions to the BBS.

The triggering conditions of the user module are defined such that the module is activated when (1) a corrective module fails to find design transformations to satisfy a constraint, or (2) the DDBP procedure fails to alter the set of active transformations to remove a conflict, or (3) after a valid topology is found at each iteration, such that the user can make necessary changes to obtain better numerical solutions and/or incorporate ad-hoc constraints, or (4) at the beginning of the first iteration to allow the user to input the necessary data for the problem, or (5) at the end of the final iteration, such that the user can store the results of the session for later retrieval. The user module is given the highest priority, such that it is invoked immediately when any of its triggering conditions become active.

## 4.2. Valid operations by a user

The user module is similar to any of the other modules accessing the blackboard. Thus, valid operations by the user would include any of the operations which are considered valid for another module accessing the blackboard. Therefore, to change the current design state, there are three valid operations that a user can perform.

First, like any of the other corrective modules, a user can send a new suggestion to the TMS to add/delete links to satisfy an ad-hoc constraint. The suggestion may consist of several disjuncts, one of which would be implemented by the TMS. If the disjunct chosen for implementation conflicts with another active transformation, the DDBP is automatically invoked to remove the conflict. Further, the TMS updates the set of design variables and triggering conditions, when a disjunct from the new suggestion has been implemented (see section 3 for details). Thus, if the user inadvertently violates any of the other constraints, the corresponding corrective module is invoked later.

Second, recall from section 3 that the BSM adds “weak” justifications to one of a pair of LINK $_{1}$ and NOLINK $_{1}$ statements. Such a justification has an empty in-list and an out-list containing the corresponding complement statement (a complement statement for LINK $_{1}$ is NOLINK $_{1}$ , and vice versa). Thus, a weak justification is valid if the complement statement included in its out-list is invalid. Such a justification represents a form cf default reasoning, and says that the corresponding link is included in/excluded from the current topology, because the BSM thinks it is cost-efficient to do so. A weak justification may be later invalidated when a corrective module adds a “strong” justification to the complement statement mentioned in its out-list. Therefore, a user is allowed to delete weak justifications from a LINK $_{1}$ /NOLINK $_{1}$ statement, and add it to the corresponding complement statement, if he thinks that the cost of the current design can be reduced by deleting/adding the link from the current topology, respectively. Once again, the TMS is invoked to propagate any changes made to the design variables to the triggering conditions.

Third, recall from section 3 that the DDBP can alter the set of active transformations to remove a conflict. Thus, the user is allowed to alter the set of active transformations, by choosing alternate transformations which achieve the same purpose. However, like the DDDP, he must ensure that the set of active transformations chosen by him, does not contain a conflict. Otherwise, the DDBP is automatically invoked to remove any such conflict introduced by the user. Once again, the TMS is invoked to propagate the changes to the design variables and triggering conditions, when a change is made to the set of active transformations.

## 4.3. Advantages of a user module

Incorporating user interaction through a separate user module with its own triggering conditions and priorities, as described above, has significant advantages. First, introducing such a module requires minimal changes to the existing design tool, beyond that of specifying its triggering conditions and priorities to the BBS. Indeed, this is one of the advantages of the hybrid procedure. Second, changes made to the design variables by the user are automatically propagated to the triggering conditions by the TMS. Thus, the necessary corrective modules are invoked again, if the user inadvertently violates a constraint. Third, any conflict introduced by the user in the set of active transformations, is automatically removed by the DDBP. This ensures that the topology generated by the user meets all the stated requirements. Fourth, the design tool can be run in automated mode by simply removing the triggering conditions of the user module from the blackboard. Further, additional triggering conditions for the user module can be added later to suit the problem at hand.

<table><tr><td>User MenuReason for Invocation : To get Input Data</td></tr><tr><td>1. Retrieve previous session2. Start new session3. Change input parameters4. Start program Execution</td></tr></table>

Fig. 5. The input menu.

<table><tr><td>User MenuReason for Invocation : Completed required iterations</td></tr><tr><td>1. View Summary results2. Store session for later retrieval3. Close session and write output4. Exit the user module</td></tr></table>

Fig. 6. The output menu.

## 4.4. The user menus

The user module operates through a system of menus. The particular menu displayed at any invocation depends on the triggering condition which activated the user module. Fig. 5 shows the Input Menu which is displayed when the user module is invoked at the start of the first iteration. The options on the menu allow the user to start a new design session by specifying the input parameters, or retrieve a stored session from disk. Fig. 6 shows the Output Menu displayed when the user module is invoked at the end of the last iteration. The user is allowed to view a summary of the best solution obtained. He may also store the details of the current session, such that the session can be restarted at a later time.

Fig. 7 shows the menu which is displayed at all other invocations of the user module. For later reference in the paper, this menu is termed the Main Menu. The reason for invocation of the user module is indicated at the top of the menu. Menu option 1 allows the user to change a few runtime parameters, like the stopping criterion used by the subgradient procedure, the various heuristic parameters used by the corrective modules, and the triggering conditions for the user module. Menu options 2–5 in Fig. 7 allow the user to view the contents of the blackboard. Options 2 and 3 display the current topology and the best solution obtained thus far, respectively. Option 4 displays the details of the justifications used for the LINK and NOLINK statements in the current solution. Option 5 displays the details of the suggestions sent in by the corrective modules. The information displayed by these options helps the user to formulate design transformations, to improve the current solution state.

Menu options 6–8 allow the user to actually change the current design state, and correspond to the three valid operations discussed in section 4.2. If these options are used, the TMS and DDBP are automatically invoked to propagate changes and remove conflicts introduced by the user, respectively.

Menu option 9 allows the user to copy the current design state into a temporary location, such that he may examine the effects of various design transformations, before actually implementing them through options 6–8. The submenu of option 9 (the Workspace Menu) is shown in Fig. 8. Notice in the figure that the user is allowed to load and execute an user defined function. This is helpful in determining whether the current design state satisfies an ad-hoc constraint, not accounted for in the design tool. For example, a function which calculates the number of links in the shortest hop paths between nodes may be helpful in determining if the current solution violates the shortest path constraint. If the constraint is violated, the user can implement design transformations using options 6–8 in the main menu. As we discuss in the next section, such a function was used to incorporate the shortest path constraint (section 1.1) in the design of a 15 node example network.

<table><tr><td>User MenuReason for Invocation : Valid Topology found</td></tr><tr><td>1. Change Runtime parameters2. Display current solution3. Display best solution4. Display Justifications5. Display Suggestions6. Alter Active Transformations7. Alter Weak Justifications8. Send New Suggestions9. Use Temporary Workspace10. Cancel this iteration11. Stop the procedure12. Exit the User module</td></tr></table>

Fig. 7. The main menu.

<table><tr><td>WORKSPACE MENU</td></tr><tr><td>1. View current link placements2. Add link3. Delete link4. Execute CFA5. Load user file6. Execute function in user file7. Exit</td></tr></table>

Fig. 8. The workspace menu.

## 4.5. A sample interaction

In this section, we present a sample interaction with the interactive design tool discussed in the preceding sections. The purpose of this presentation is to demonstrate how a human designer would use the various options in the menu, to improve the current design state. The computer output is lengthy. For brevity of presentation, several interactive displays have been omitted. The various menus (Input, Output, Main and Workspace Menus) have not been shown at any stage. These menus can be found in Figs. 5–8. Comments and explanations are in italics, and have been enclosed in braces.

## →(load 'bbs.l)

{The lisp file containing the program for the Blackboard scheduler (BBS) is loaded into the lisp system. The BBS loads all the necessary lisp and fortran files, sets up the triggering conditions and priorities of the modules, and starts program execution. At the beginning of the first iteration, the user module is invoked to read input data. The user may restart a previous design session, or start a new session by specifying the input parameters.}

## Input Menu

Enter Choice: 2 {Start new design session}

{The user starts a new design session. The input parameters are specified through an interactive process, after which the input menu is displayed again.}

## Input Menu

Enter Choice: 4 {Start program execution}

Enter Choice: 4 {Start program execution}
{The user starts execution of the program by choosing option 4. If a valid topology satisfying all the constraints is found, the user module (Main Menu) is invoked again to allow the user to make changes to the current topology}

## Main Menu

Enter choice: 2 {View current link placements} {At this stage, the user may wish to view the current topology, in order to formulate design changes. The current version of the design tool does not have a graphical interface. The topology is displayed as a table, not shown here.}

{After viewing the current topology, the user decides that deleting a link (18, 21) may improve the cost of the solution. He, therefore, chooses option 9 from the main menu to copy the current topology to a temporary workspace, and examine the effect of these changes}

## Main Menu

Enter Choice: 9 {Use temporary workspace}
Copying current solution into temporary workspace....

## Workspace Menu

Enter Choice: 4 {Execute CFA}

Cost of current topology is \$252,911.52

{The user performs a CFA on the current topology to determine the total network cost. Through option 3 in the Workspace menu, the user deletes link (18,: 21) in the temporary workspace, and reexecutes CFA.}

## Workspace Menu

Enter Choice: 3 {Delete link}
Delete link between nodes (node 1 node2): 18 21
Deleted link (18, 21)....

Workspace Menu
Enter Choice: 4 {Execute CFA}
Cost of current topology is \$250,987.52 {There is a decrease in cost. Hence, the user returns to the main menu, to view the justifications for link (18, 21), to determine if it can be deleted from the topology}

Workspace Menu
Enter Choice: 7 {Exit the temporary workspace}

## Main Menu

Enter choice: 4 {View Justifications}
For which Link (node 1 node2): 18 21
Justifications for Link between nodes 18 and 21

Statement Justified by
Sugg. No Disjunct No. CHO-
SEN

LINK 18 21 Weak Justification
NOLINK 18 21
LINK statement is currently valid

{For a specified link 1, this menu option shows the justifications for the LINK $_{1}$ and NOLINK $_{1}$ statements. It displays the suggestion number (i) and the disjunct number (j) which justifies this statement. It also displays whether this disjunct has been chosen for implementation. For link (18, 21), there are no such strong justifications for either the LINK or the NOLINK statement. The LINK statement is currently valid through a weak justification. The user can, therefore, delete the link by deleting the weak justification for the LINK statement, and adding it to the NOLINK statement, through menu option 7}

## Main Menu

Enter Choice: 7 {Change weak justifications}

Enter Link (node1 node2): 18 21

Current Weak Justification is for LINK 18 21 Statement

Set Weak Justification for (1 LINK, 2 NOLINK) statement: 2

Invoking TMS to propagate changes....

{The TMS is invoked to propagate the changes to the triggering conditions

Having successfully deleted link (18, 21), the user may now wish to view the suggestions sent in by the corrective modules, to examine whether choosing alternate disjuncts from these suggestions may decrease the cost}

Main Menu
Enter Choice: 5 {View Suggestions}
There are 4 suggestions....
Enter Suggestion Number: 1
Details of Suggestion 1

<table><tr><td>Disj.</td><td>Justifies LINKS</td><td>Justifies NO-LINKS</td><td>Conf. set</td><td>Active Conf. set</td><td>CHO-SEN</td></tr><tr><td>1</td><td>((14 18))</td><td>nil</td><td>nil</td><td>nil</td><td>t</td></tr><tr><td>2</td><td>((12 18))</td><td>nil</td><td>nil</td><td>nil</td><td>nil</td></tr><tr><td>3</td><td>((9 14))</td><td>nil</td><td>nil</td><td>nil</td><td>nil</td></tr></table>

{(Suggestion 1 has 3 disjuncts, and they add links (14, 18), (12, 18) and (9, 14), respectively. Disjunct 1 is currently active. Conflictsets and Active Conflictsets (see section 3) are nil for all the disjuncts. The LINK and NOLINK statements corresponding to these links will have strong justifications, as shown below for link (14, 18)}

## Main Menu

Enter Choice: 4 {View Justifications}
For which Link (node1 node2): 14 18
Justifications for Link between nodes 14 and 18

<table><tr><td rowspan="2">Statement</td><td colspan="3">Justified by</td></tr><tr><td>Sugg. No</td><td>Disjunct No.</td><td>CHO-SEN</td></tr><tr><td>LINK 14 18</td><td>1</td><td>1</td><td>t</td></tr><tr><td>NOLINK 14 18</td><td colspan="3">Weak Justification</td></tr><tr><td colspan="4">LINK statement is currently valid</td></tr></table>

{The LINK 14 18 statement is justified by disjunct 1 of suggestion 1. Since this disjunct is active, the LINK statement is currently valid. The user may decide (using the temporary workspace or otherwise) that implementing disjunct 2 of suggestion 1 may be more cost efficient. He uses menu option 6 to alter the set of active transformations}

## Main Menu

Enter Choice: 6 {Alter set of active transformations}

Menu to Alter the CHOSEN Transformations 1. Get Conflict Summary

2. Display Suggestion

3. Alter the set of chosen transformations

4. Quit

Enter Choice: 3
Enter Suggestion Number: 1
Details of Suggestion 1

<table><tr><td>Disj.</td><td>Justifies LINKS</td><td>Justifies NO-LINKS</td><td>Conf.</td><td>Active Conf. set</td><td>CHO-SEN</td></tr><tr><td>1</td><td>((14 18))</td><td>nil</td><td>nil</td><td>nil</td><td>t</td></tr><tr><td>2</td><td>((12 18))</td><td>nil</td><td>nil</td><td>nil</td><td>nil</td></tr><tr><td>3</td><td>((9 14))</td><td>nil</td><td>nil</td><td>nil</td><td>nil</td></tr></table>

Enter Disjunct to make active: 2  
Invoking TMS to propagate changes....  
No conflict reported ....

{(Disjunct 2 of suggestion 1 is made active. Thus, link (14, 18) is deleted from the topology, and link (12, 18) added. The TMS is invoked to propagate changes. Since the Active Conflictset of disjunct 2 is nil, no conflict is reported and the DDBP is not invoked}

Menu to Alter the CHOSEN transformations
Enter Choice: 4 {Quit this menu and return to the Main Menu}

## Main Menu

{Finally, the user may wish to delete link (19, 21) from the topology, to satisfy an ad-hoc constraint. He uses menu option 8 to send a suggestion to the TMS. In this case, the suggestion sent to the TMS has only one disjunct}

Enter Choice: 8 {Send new suggestion}

Do you want to delete or add links (0 del 1 add): 0

Enter number of disjuncts in suggestion: 1
For disjunct 1 enter the links to be deleted as a list of the form ((a b)(c d)...): ((19 21))
Invoking TMS to propagate changes....
Conflict detected...Invoking DDBP...
Successfully implemented suggestion...

## Main Menu

Enter choice: 5 {View suggestions}

There are 5 suggestions..

Enter Suggestion Number: 5

Details of Suggestion 5 {This is the new suggestion sent in by the user}

<table><tr><td>Disj.</td><td>Justifies LINKS</td><td>Justifies NO-LINKS</td><td>Conf. set</td><td>Active Conf. set</td><td>CHO-SEN</td></tr><tr><td>1</td><td>nil</td><td>((19 21))</td><td>((2 1))</td><td>nil</td><td>t</td></tr></table>

Table 1  
Node locations for a 15 node random network.

<table><tr><td>X</td><td>Y</td><td>X</td><td>Y</td></tr><tr><td>590</td><td>575</td><td>366</td><td>519</td></tr><tr><td>84</td><td>78</td><td>52</td><td>29</td></tr><tr><td>474</td><td>899</td><td>722</td><td>115</td></tr><tr><td>952</td><td>185</td><td>72</td><td>521</td></tr><tr><td>886</td><td>847</td><td>398</td><td>615</td></tr><tr><td>308</td><td>821</td><td>964</td><td>101</td></tr><tr><td>950</td><td>600</td><td>706</td><td>315</td></tr><tr><td>288</td><td>321</td><td></td><td></td></tr></table>

{Note that the single disjunct in suggestion 5 conflicts with disjunct 1 of suggestion 2. The DDBP is, therefore, invoked, to remove the conflict. The DDBP modifies suggestion 2 by making disjunct 2 active, and disjunct 1 inactive, thereby removing the conflict.}

## Main Menu

Enter Choice: 5 {View Suggestion}

There are 5 suggestions..

Enter Suggestion Number: 2

Details of Suggestion 2

<table><tr><td>Disj.</td><td>Justifies LINKS</td><td>Justifies NO-LINKS</td><td>Conf. set</td><td>Active Conf. set</td><td>CHO-SEN</td></tr><tr><td>1</td><td>((19 21))</td><td>nil</td><td>((5 1))</td><td>((5 1))</td><td>nil</td></tr><tr><td>2</td><td>((7 19))</td><td>nil</td><td>nil</td><td>nil</td><td>t</td></tr><tr><td>3</td><td>((14 21))</td><td>nil</td><td>nil</td><td>nil</td><td>nil</td></tr></table>

{(Finally, the user is satisfied with the current topology and decides to quit the user module. However, he now wishes the program to run in automated mode}

## Main Menu

Enter Choice: 1 {Change runtime parameters}
{The user chooses menu option 1 to remove the triggering condition of the user module, such that the program runs in automated mode. The main menu is displayed again. The user chooses option 12 to quit the user module.}

Table 2  
The capacity options

<table><tr><td>Capacity (Kbits/s)</td><td>Fixed cost ($)</td><td>Variable cost ($/mile)</td></tr><tr><td>56</td><td>10000.0</td><td>10.0</td></tr><tr><td>112</td><td>10500.0</td><td>19.0</td></tr><tr><td>168</td><td>11000.0</td><td>28.0</td></tr><tr><td>224</td><td>11500.0</td><td>37.0</td></tr></table>

{The program has the flexibility to allow the user to define a lisp predicate as a triggering condition for the user module. Thus, the user can define a predicate which will activate the user module when a specific constraint (for example the shortest path constraint) is violated. This will allow the user module to be invoked in automated mode, only when a specific constraint is violated in the current design. The user can then make the necessary changes to satisfy the constraint}

## Main Menu

Enter Choice: 12 {Quit the user module} {At the end of the specified number of iterations, the Output Menu is displayed. The user may use the various options in the Output Menu to store the session for later execution, store details about the best solution, or view information on the screen.}

## 5. Computational results

The quality of solutions generated by the automated version of the design tool has been established in $[10]$ $[19]$ , through comparisons with the lagrangian lower bound and existing solutions in the literature. The purpose of the computational experiments reported in this section is to (1) numerically compare the solutions generated by the interactive design tool with those generated by the automated version, and (2) demonstrate that an ad-hoc constraint can be incorporated in the design through user participation. Specifically, we incorporate the shortest path constraint (section 1.1) in the design.

Table 3  
Comparing the 2-edge-connected solutions.

<table><tr><td>γ (Kbps)</td><td>Lower (K$)</td><td>Auto. (K$)</td><td>Interact. (K$)</td><td>Savings (K$)</td><td>Interact/ Lower</td><td>CPU/ Iteration (secs)</td><td>Resp. time (secs)</td></tr><tr><td>210.0</td><td>184.5</td><td>196.9</td><td>192.8</td><td>4.1</td><td>1.04</td><td>5.19</td><td>0.10</td></tr><tr><td>315.0</td><td>185.1</td><td>214.3</td><td>208.1</td><td>6.2</td><td>1.12</td><td>5.84</td><td>0.08</td></tr><tr><td>420.0</td><td>186.3</td><td>227.7</td><td>219.1</td><td>8.6</td><td>1.17</td><td>5.52</td><td>0.08</td></tr><tr><td>525.0</td><td>187.7</td><td>241.5</td><td>232.5</td><td>9.0</td><td>1.24</td><td>6.15</td><td>0.10</td></tr></table>

The computational experiments were performed on a randomly generated network of 15 nodes. The node locations for the network are shown in Table 1. The capacity options used for the computations are shown in Table 2. The maximum permissible delay in the network ( $T_{max}$ ) was 0.2 secs/message. A message length of 1000 bits was assumed. In all cases, the starting values of the lagrangian multipliers was set at 0.0015.

Table 3 compares the 2-edge-connected solutions generated by the automated and interactive versions. In all cases, only the best automated solutions were retrieved and modified through user interaction, as discussed in section 4.0. Several throughput levels ranging from 210 kbits/s to 525 kbits/s were used. A 2 edge-connectivity restriction was imposed on the network. The lagrangian bound does not incorporate the reliability constraint. An improvement in cost for solutions generated by the interactive design tool, is observed in all cases. This is mainly due to the heuristic nature of the modules accessing the blackboard. A human designer is usually able to determine local changes to the generated solutions, to improve the cost of the design. In all cases, 60 iterations of the automated procedure were performed. Since many of the automated solutions were close to optimal (as indicated by the lagrangian bound), improvements may not be significant in some cases.

Table 3 also reports the CPU times required by the procedure. The seventh column in Table 3 reports the CPU time required by the automated procedure per iteration. This represents the amount of time the user has to wait for the procedure to complete one iteration and display the user menu again. The last column in Table 3 shows the average amount of CPU time required per user move (hitherto called response time). The response time represents the CPU time required by the procedure to implement a user suggestion (menu option 8), and invoke the TM4 to propagate changes and resolve conflicts, if any. It is observed from the table that the CPU time per iteration of the automated procedure increases only slightly with the throughput, mainly due to the increased time spent in Capacity and Flow allocation. The response time is largely independent of the throughput. Table 3 shows that the CPU times required by the procedure are reasonably small such that the procedure can be executed interactively.

For the results shown in Table 4, a 3-edge-connectivity requirement was specified for each node pair. The maximum allowable degree of a node was set at 4. Higher throughput levels were tried than those reported in Table 3, since the network has more number of links. Only the best automated solution was retrieved and modified through user participation. The Table compares the solutions generated by the automated and interactive versions. Once again, for reasons mentioned earlier, an improvement in cost is observed in all cases. Table 4 also shows the CPU times required by the procedure. The reader should notice that the CPU times are slightly higher than those reported in Table 3 because of the additional constraints imposed.

The 2-edge-connectivity experiments were repeated with the interactive design tool, with the maximum number of links in the shortest hop path between any pair of nodes set at 6. The shortest path constraint was incorporated through user participation, as outlined in section 3.0.

Table 4  
3-connected solutions with degree constraint.

<table><tr><td>γ (kbits)</td><td>Auto. (K$)</td><td>Interact. (K$)</td><td>Savings (K$)</td><td>CPU/ Iteration (secs)</td><td>Resp. time (secs)</td></tr><tr><td>315.0</td><td>302.2</td><td>301.3</td><td>0.9</td><td>7.72</td><td>0.13</td></tr><tr><td>630.0</td><td>327.3</td><td>323.2</td><td>4.1</td><td>9.80</td><td>0.13</td></tr><tr><td>945.0</td><td>350.4</td><td>340.5</td><td>9.9</td><td>7.26</td><td>0.13</td></tr></table>

Table 5  
Incorporating the shortest path constraint.

<table><tr><td>Throughput (kbits/s)</td><td>Automated (K$)</td><td>Interactive (K$)</td><td>Increase (K$)</td></tr><tr><td>210.0</td><td>196.9</td><td>205.0</td><td>8.1</td></tr><tr><td>315.0</td><td>214.3</td><td>208.2</td><td>-6.1</td></tr><tr><td>420.0</td><td>227.7</td><td>227.4</td><td>-0.3</td></tr><tr><td>525.0</td><td>241.5</td><td>245.6</td><td>4.1</td></tr></table>

Table 6  
CPU times for 3 networks.

<table><tr><td>No of nodes</td><td>CPU/iteration (secs)</td><td>Response time (secs)</td></tr><tr><td>15</td><td>5.19</td><td>0.10</td></tr><tr><td>20</td><td>13.07</td><td>0.13</td></tr><tr><td>25</td><td>20.97</td><td>0.15</td></tr></table>

These results are shown in Table 5. The results were compared with the original 2-edge-connected solutions generated by the automated procedure. The automated results do not incorporate the shortest path constraint. Surprisingly, it is observed that the cost of the solutions generated by the interactive design tool is often lower, even though an additional constraint has been incorporated.

Table 6 reports CPU times for two additional networks of 20 and 25 nodes, for a throughput value of 210.0 kbps. The CPU times for the 15 node network is repeated from Table 3. As expected, the CPU time per iteration of the automated procedure increases significantly with the number of nodes. The Response time also increases (but less significantly) with the number of nodes in the network. Since the Response time incorporates the time required by the TMA to propagate changes and resolve conflicts in response to an user suggestion, it is conjectured that the execution time of the TMA is not significantly affected by the size of the network.

## 6. Concluding remarks

In an earlier paper [10], we presented a method to combine heuristic design knowledge with optimisation algorithms, through the use of a blackboard, a truth maintenance system and a dependency directed backtracking procedure. The resulting hybrid design tool has significant advantages, as demonstrated through several computational experiments reported in [10]. In this paper, we have shown how the same structure of the design tool can be used to integrate design transformations formulated by a human designer. The interactive design tool has been implemented through a combination of Lisp and Fortran programming languages. Through several computational experiments reported here, we verified two important advantages of incorporating the user in the search process. First, superior numerical results can be obtained through user participation in the design. Second, several ad-hoc constraints and issues which are difficult to include in an automated tool, can be incorporated in the interactive tool. We believe that the hybrid approach presented in this paper is not limited to telecommunication network design problems, and can be extended to other applications as well.

## References

[1] P. d'Alessandro, M. Dalla Mora, E. De Santis, Issues in Design and Architecture of Advanced Dynamic Model Management for Decision Support Systems, Decision Support Systems 5, No. 4 (1989).

[2] M.O. Ball, Complexity of Network Reliability Computations, Networks 10 (1980).

[3] M. Bartusch, R.H. Mohring, F.J. Radermacher, Design Aspects of an Advanced Model Oriented DSS for Scheduling Problems in Civil Engineering, Decision Support Systems 5, No.4 (1989).

[4] M. Binbasioglu and J. Matthias, Domain Specific Tools for Knowledge Based Model Building, Decision Support Systems 2 (1986).

[5] I. Bockenholt, M. Both and W. Gaul, A Knowledge Based System for Supporting Data Analysis Problems, Decision Support Systems 5, No.4 (1989).

[6] R.H. Bonczek, C.W. Holsapple and A.B. Whinston, Foundations of Decision Support Systems (Academic Press, New York, (1981) 11–17.

[7] R.R. Boorstyn and H. Frank, Large Scale Network Topological Optimisation, IEEE Trans. on Comm. (Jan. 1979) 29–47.

[8] R.R. Dolk A Generalised Model Management System for Mathematical Programming, ACM Transactions on Mathematical Software 12, No. 2 (1986).

[9] J. Doyle, A Truth Maintenance System, Artificial Intelligence (1979).

[10] A. Dutta and S. Mitra, Integrating Heuristic Knowledge and Optimisation Models for Communication Network Design, Working Paper (College of Business, University of Iowa, Iowa City, IA Aug. 1990).

[11] S. Even, An Algorithm for Determining Whether the Connectivity of a Graph is at least K, SIAM Journal of Computing 4 (Sept. 1975).

[12] L. Fratta, M. Gerla and L. Kleinrock, The Flow Deviation Method: An Approach to Store Forward Communication Network Design, Networks 3, No. 2 (1973) 97–133.

[13] B. Gavish and I. Neumann, A System for Routing and Capacity Assignment in Computer Communication Networks, IEEE Trans. on Commun. 37, (1989) 360–366.

[14] A.M. Geoffrion, An Introduction to Structured Modelling, Management Science 33, No. 5 (1987).

[15] M. Gerla, The Design of Store and Forward Networks for Computer Communications, Ph.D Dissertation. (University of California, Los Angeles, CA, Jan. 1973).

[16] M. Gerla, A Cut Saturation Algorithm For Topological Design of Packet Switched Communication Networks, Proc. Nat. Telecommun. Conf. (Dec. 1974).

[17] H.J. Greenberg, A Natural Language Discourse Model to Explain Linear Programming Models and Solutions, Decision Support Systems 3, No. 4 (1987).

[18] R. Krishnan, A Logic Modelling Language for Automatic Model Construction, Decision Support Systems 6 (1990).

[19] S. Mitra, AI/OR Hybrid Methods in Telecommunication Network Design, Ph.D Dissertation (The Graduate College, University of Iowa, Iowa City, IA, Dec. 1990).

[20] W. Muhanna, R. Pick, Composite Models in SYMMS,

Proceedings of the 21st Annual Hawaii Conference on System Sciences (Kona, HI. 1988).

[21] F.H. Murphy, E.A. Stohr, An Intelligent System for Formulating Linear Programs, Decision Support Systems 3, No. 1 (1986).

[22] H.A. Simon, The Sciences of the Artificial, 2nd ed. (MIT Press, Cambridge, MA, 1981).

[23] I.S. Singh and S. Sadagopan, A Support System for Optimisation Modelling, Decision Support System 3, No. 2 (1987)?

[24] A.M.R. Smith, L.S. Lee and D.J. Hand, Interactive User-Friendly Interfaces to Statistical Packages, The Computer Journal 26, (1983).

[25] R.H. Sprague, E.D. Carlson, Building Effective Decision Support Systems (Prentice Hail, Englewood Cliffs, NJ, 1982).

[26] S. Ueno, Y. Kajitani and H. Wada, Minimum Augmentation of a Tree to a K-edge-connected Graph, Networks 18 (1988) 19–25.

[27] R. Van Slyke and H. Frank, Network Reliability Analysis: Part I, Networks 1 (1971) 139–172.

[28] R.S. Wilkov, Analysis and Design of Reliable Computer Networks, IEEE Trans. on Comm. 20, No. 3 (June 1972).

[29] M. Zeleny, Multiple Objectives on Mathematical Programming: Letting the Man in, Computers and Operations Research 7 (1980).
