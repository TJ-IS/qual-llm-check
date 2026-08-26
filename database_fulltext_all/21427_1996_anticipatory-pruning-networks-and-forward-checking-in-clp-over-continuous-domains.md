---
otero_id: 21427
otero_key: "NYYBVU8K"
title: "Anticipatory pruning networks and forward checking in CLP over continuous domains"
authors: "Geun Sik Jo; Ken McAloon"
year: "1996"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(96)80008-x"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Anticipatory Pruning Networks and forward checking in CLP over continuous domains

Geun Sik Jo $^{a,*}$ , Ken McAloon $^{b}$

$^{a}$ Department of Computer Science and Engineering, InHa University, Inchon 402-751, South Korea $^{b}$ Brooklyn College and CUNY Graduate Center, Department of Computer and Information Science Brooklyn College, Brooklyn, NY 11210, USA

Received 29 November 1994; revised 15 May 1995; accepted 27 November 1995

## Abstract

In this paper, the notion of the Anticipatory Pruning Network (APN) is introduced and developed for the propositional part of the 2LP system; 2LP (Linear Programming and Logic Programming) is a constraint logic programming system which has been developed and implemented at the Logic Based System Lab at Brooklyn College/CUNY. Using the compilation of rules in the style of the Rete algorithm, the APN maps program clauses into a network. The APN prunes a search space by consistency checking and inconsistency propagation through the network and resets itself upon backtracking. The APN extends forward checking to continuous constraint domains. Overall, the benchmarks show the APN to be an effective forward checking mechanism for both discrete and continuous problem domains for Simplex based constraint solvers. In particular, the APN is an effective pruning method for constrained mixed integer, linear optimization problems.

Keywords: Constraint logic programming; Forward checking over continuous domains; Linear programming

## 1. Introduction

Many important AI problems can be formulated as a Constraint Satisfaction Problem (CSP). Examples of these problems, which have been researched for many years, include scheduling problems, vision and scene interpretation, and configuration problems. Along with Operations Research (OR) approaches to constraint solving, the AI community is doing research on Constraint Satisfaction Problems (CSP) which for most part deal with discrete domains of variables. However, although research in AI used to be separated from research on the constraint solving in OR, the two disciplines of constraint solving recently started to merge in solving AI problems.

The Simplex method which was being mostly used in linear programming is used nowadays to replace the syntactic unification on the Herbrand Universe of logic programming $[3,14]$ . Variations of Simplex methods have been implemented in constraint logic programming systems as a major engine of computation such as CLP(R) [15], Prolog III [4] and CHIP [8].

The CLP scheme [14] defines a class of programming language based on constraint solving and logic programming. The framework which Jaffar and Lassez defined can be represented as CLP(X), where X is the domain of discourse over constraints. One instance of the CLP paradigm is CLP(R), where R represents the real numbers. Unification in Prolog can be viewed as solving equality constraints over the Herbrand universe [3,14]. In the CLP scheme, unification is replaced by solvability of constraints which is a more general computation scheme [14]. Moreover, it yields a more declarative programming scheme than conventional logic programming from the user's point of view. The constraint solver in constraint logic programming is a variation of the Simplex method in linear programming which is a major area of operations research, management science, mathematical programming, and industrial engineering. From a high-level point of view, the Simplex based constraint solver is put in into a logic program in the design of languages such as CLP(R) and Prolog III. CHIP is another constraint logic programming language which is developed by the European Computer-Industry Research Center (ECRC). In the CHIP system, the declarative aspects of logic programming are combined with the efficient implementation of constraint solving techniques, such as CSP by introducing the domain concept in Prolog. The CHIP system [12] has been implemented with several different constraint solving techniques which depend on the computation domains that they are dealing with, such as CSP for finite domain, local propagation for Boolean terms, and Simplex for rational terms.

From the programming language point of view, we can develop powerful declarative and expressive computer programming languages such as CLP(R) by integrating a variation of Simplex with Horn clause logic. The constraint solver in constraint logic programming is mainly related to the declarativeness and inversibility of the programming language $[3,15]$ . However, the purpose of using Simplex in operations research is to optimize the given costs or profits function associated with a set of constraints.

In this research, constraint based searching in backward chaining is integrated with the Anticipatory Pruning Network (APN) which is a kind of forward chaining mechanism to minimize backtracking. The engine for backward chaining here employs a mathematical constraint solver which is a incremental version of the Simplex method. The incremental version of the Simplex method here checks the satisfiability for the set of constraints as new constraints are dynamically added to the system. To prune the search space, the forward checking mechanism is implemented through a method based on one used in Production Systems. The Anticipatory Pruning Network (APN) propagates constraints which are inconsistent with the current environment. The inconsistent constraints can be found by checking the consistency with the current environment. We used the Rete method of rule compilation to implement the forward checking mechanism. The motivation of this integration comes from the observation that AI and OR have complementary advantages: the AI approach has the expressive power and OR offers mathematical declarativeness. To develop and test the idea, we worked with minimal 2LP [21], a CLP system with propositional logic and linear constraints [5].

## 2. Minimal 2LP and APN algorithm

In terms of CLP languages, minimal 2LP [21] is minimal CLP(D), where D is the domain of rational numbers as an ordered Z-module. One of the main concerns for CLP implementors is efficiently testing the satisfiability of constraints. In this work, we show that the unsatisfiability of constraints can propagate inconsistency through the network in the minimal 2LP system. The APN algorithm here computes the consequences of the constraints which are inconsistent with the current environment. The APN also explicitly saves the consequences of inconsistency in the network. Furthermore, the APN algorithm can undo the process of computing and saving the consequences of inconsistent constraints to meet the backtracking behavior of logic programming. This section describes implementation details of the APN algorithm including the compilation of the rules in the minimal 2LP system, consistency checking and its relationship with stratification.

## 2.1. The minimal 2LP system

Let us consider the following Horn clause in Prolog:

$$
P (X _ {1}, X _ {2}, \dots , X _ {n}): -
$$

$$
C _ {1} \left(X _ {1}, X _ {2}, \dots , X _ {n}\right), C _ {2} \left(X _ {1}, X _ {2}, \dots , X _ {n}\right), \dots
$$

$$
C _ {n} \left(X _ {1}, X _ {2}, \dots , X _ {n}\right), Q _ {1} \left(X _ {1}, X _ {2}, \dots , X _ {n}\right),
$$

$$
Q _ {2} (X _ {1}, X _ {2}, \dots , X _ {n}), \dots Q _ {n} (X _ {1}, X _ {2}, \dots , X _ {n})
$$

where $C_{1}(X_{1},X_{2},\ldots,X_{n}),C_{2}(X_{1},X_{2},\ldots,X_{n}),\ldots C_{n}(X_{1},X_{2},\ldots,X_{n})$ are constraints over real and $Q_{1}(X_{1},X_{2},\ldots,X_{n}),Q_{2}(X_{1},X_{2},\ldots,X_{n}),\ldots Q_{n}(X_{1},X_{2},\ldots,X_{n})$ are logical atoms. If we fix $X_{1},X_{2},\ldots,X_{n}$ once and for all, then the logic is propositional and the constraint variables are all global. Our research here on APN is based on the minimal 2LP system. Formally, the minimal 2LP system can be defined as follows.

Definition. A minimal CLP(D) program is given by a finite set of rules of the form

$$
\begin{array}{c} P (X _ {1}, \ldots , X _ {n}): - \\ \left(C _ {1} (Y _ {1, 1}, \ldots , Y _ {1, k _ {1}}), \ldots , C _ {s} (Y _ {s, 1}, \ldots , Y _ {s, k _ {s}}) \right. \\ Q _ {1} (X _ {1}, \ldots , X _ {n}), \ldots , Q _ {t} (X _ {1}, \ldots , X _ {n}) \end{array}
$$

where the $X_{1},\ldots ,X_{n}$ are variables and for each $i$ the $Y_{i,1},\ldots ,Y_{i,k_i}$ form a subset of $X_{1},\ldots ,X_{n}$ .

Note that this means that the variables $X_{1},\ldots,X_{n}$ are all global variables of the program and that there are no local variables. The condition that the variables appear in the same order in all the procedures of the program makes the unifications trivial and thus the logic reduces to propositional logic. In particular a minimal-CLP program without constraints reduces to a Proplog program. However, the presence of constraints makes minimal-CLP much more powerful than Proplog [5]. As an example of a minimal 2LP program, a two month blending problem in [25] is remodeled using minimal 2LP in Appendix A and Appendix B.

## 2.2. Rule compilation in the 2LP system

The compilation of rules for the APN in the 2LP system is analogous to the compilation done in the OPS5 system [9]. In contrast to OPS5, the condition elements of a rule here have only the name of the class and do not have any attributes in the sense of the OPS5 context. In the APN, the rules are compiled into a data flow network which is logically equivalent to the set of rules. In contrast, only the LHS of rules are compiled into a network in the Rete match algorithm [9,10]. The nodes of the APN are represented in the form of Von Neumann machine instructions as in the Rete algorithm. The links between the nodes are not maintained explicitly. Rather, the successor nodes are placed at the immediate adjacent memory location for navigating the nodes efficiently. The compiled APN here is represented by the linearized instruction set which can be executed by the interpreter. However, it is not enough to design the network by the linearization of the instructions if we consider the fact that some of the nodes in the APN have more than one predecessor and successor. Therefore, two more nodes are introduced. One is the Fork node which represents the fact that the node has more than one successor. The other one is the Merge node which represents the fact that the node has more than one predecessor.

In KB1, P, Q and R are logical atoms and $C_{1}, C_{2}, \ldots, C_{4}$ are constraints

$$
\begin{array}{r l} \mathrm{KB1} & = \left\{Q \leftarrow C _ {1}, C _ {2}, P \cdot Q \leftarrow C _ {2}, R \right. \\ & \times (P \leftarrow C _ {3}) (P \leftarrow C _ {4}) \}. \end{array}
$$

Fig. 1 shows an example of the network for the set of rules, KB1. The linearization of the network in an efficient machine executable form is important for real applications. For the basic human readable forms of the linearized network, the following five different types of nodes are necessary to linearize the APN:

![](/api/attachments/NYYBVU8K/fulltext/images/077ed2127378f03ca8e1338f1688476cffd23575825c189d806d57455061fda9.jpg)  
Fig. 1. Example of the network for the set of rules, KB1.

Table 1  
Linearization of network for KB1

<table><tr><td></td><td>Fork</td><td>1</td><td></td></tr><tr><td></td><td>EQ</td><td> $C_1$ </td><td></td></tr><tr><td>2</td><td>AND</td><td>T</td><td>T</td></tr><tr><td>3</td><td>AND</td><td>T</td><td>T</td></tr><tr><td></td><td>update</td><td> $R_1$ </td><td>Q</td></tr><tr><td>1</td><td>fork</td><td>4</td><td></td></tr><tr><td></td><td>EQ</td><td> $C_2$ </td><td></td></tr><tr><td></td><td>fork</td><td>6</td><td></td></tr><tr><td></td><td>Merge</td><td>2</td><td></td></tr><tr><td>4</td><td>Fork</td><td>5</td><td></td></tr><tr><td></td><td>EQ</td><td>P</td><td></td></tr><tr><td></td><td>Merge</td><td>3</td><td></td></tr><tr><td>5</td><td>Fork</td><td>8</td><td></td></tr><tr><td></td><td>EQ</td><td>R</td><td></td></tr><tr><td>7</td><td>AND</td><td>T</td><td>T</td></tr><tr><td></td><td>Update</td><td> $R_2$ </td><td>Q</td></tr><tr><td>6</td><td>Merge</td><td>7</td><td></td></tr><tr><td>8</td><td>Fork</td><td>9</td><td></td></tr><tr><td></td><td>EQ</td><td> $C_3$ </td><td></td></tr><tr><td></td><td>Update</td><td> $R_3$ </td><td>R</td></tr><tr><td>9</td><td>EQ</td><td> $C_4$ </td><td></td></tr><tr><td></td><td>Update</td><td> $R_4$ </td><td>P</td></tr></table>

1. (Fork label): The label represents the position of a node for another successor.

2. (EQ atom): One-input node for testing for equality.

3. (AND Left-memory Right-memory): Two input node which has the left memory and right memory. The left-memory takes input from the previous node and the right memory takes input from the Merge node.

4. (Join label): This node is the same as the ordinary goto instruction, but affects only the right-memory of the AND node.

5. (Update rule-id head): Update the counter of the rules with the same head and the list of available rules for selection.

The illustration for the linearization of the network for the knowledge base, KB1, is shown in Table 1.

In addition to the linearization of the body of rules, we explicitly keep the procedure tables which have information about the availability of the rules for resolving goal lists.

## 2.3. Anticipatory pruning networks

There are two functionally different components of computation in the APN. One is finding the constraints which are inconsistent with the current environment. The other is the propagations of the inconsistent constraints. In testing consistency, an incremental version of the Simplex algorithm is used. By propagating inconsistency, some rules can be pruned out from the knowledge base. Therefore, some goals are detected to be deterministic or failure can be detected early if an unsolvable atom occurs in the goal list. If deterministic, then deterministic goals are selected and resolved at once.

## 2.3.1. Consistency checking with the current environment

Let us consider consistency checking in the 2LP system. Let the active constraints (AC) be the constraints which are enforced by the logic interpreter. Let us call the set of all constraints for the given program the quick constraints (QC). The quick constraints are also called the quick list. Finally, let us call the constraints which are inconsistent with the current environment the dead constraints (DC). Whenever the constraint is enforced by the logic interpreter, the system checks consistency with the current environment. The environment here is the polyhedral set which is defined by the constraints AC. If the newly enforced constraint is consistent, the current environment is updated. Furthermore, the constraint is removed from the QC and added to the AC. To find out constraints which are inconsistent with the current environment, the system performs consistency checking with the rest of the QC. If a constraint with QC is not consistent, it is removed from the QC and added to the DC. Then the consistency checking in minimal 2LP is to check the consistency of all the constraints in QC with the newly updated environment. Therefore, every time the current environment is updated, consistency checking is performed. For an example of consistency checking with the given knowledge base KB1, if the goal is given as “? - Q”, the new goal “? - C₁, C₂, P” should be resolved. At this time, the constraint C₁ and C₂ are added to the AC list by the minimal 2LP interpreter. In the mean time, the QC list includes $C_{3}$ and $C_{4}$ , that is, all constraints in the KB1 except $C_{1}$ and $C_{2}$ . To check consistency with the current environment which is the polyhedral set defined by $C_{1}$ and $C_{2}$ , the minimal 2LP interpreter checks the consistency of all the constraints in QC which are $C_{3}$ and $C_{4}$ with the current environment. If any of the constraints are inconsistent with the current environment, these constraint will be put into DC. It is interesting to note that the consistency of QC with the current environment here can be done in parallel.

After the system finds the constraints inconsistent with the current environment, the inconsistency is propagated through the precompiled network (APN) which is explained in the next section. Some of the search tree can be pruned out a priori as a result of the propagation of inconsistency. This is called Anticipatory Pruning.

Instead of checking consistency on all the constraints in the QC with the current environment, we can have the system choose from several different sets of constraints. One of them is to compute the relevant constraints with the goal list, which is the constraints set that can be derivable from the left most branch of the search space. This is to detect the early failure in the current direction of search space. This is called Partial Anticipatory Pruning.

If we check the consistency with all constraints in QC, it is called Full Anticipatory Pruning. The benchmark results for each technique are given in the next section.

## 2.3.2. Inconsistency propagations in APN

Since we are interested in inconsistent constraint sets in order to prune unnecessary searching, all the two-input memories are initially set to be available, which means that every rule is available for selection at the beginning. As the logic interpreter finds the constraints which are inconsistent with the current constraint environment, the system generates negative tokens and the interpreter of the APN propagates the negative tokens down to the APN. As a result of propagating a negative token, some rules may be ruled out from the knowledge base to remove unnecessary search. The interpreter also can undo what has been done by propagating the positive tokens to take care of the backtracking behavior of the logic programming control mechanism. The APN interpreter basically performs the following inconsistency propagation-update cycles.

1. Match: The condition elements in the body of rules are matched against the atoms which refer to the constraints which are inconsistent with the current environment.

2. Propagating and updating the procedure table: The successfully matched atoms are propagated depending upon the inconsistency found in the condition elements in the same rule. If the inconsistency is propagated successfully, the counter associated with the head is decreased by 1 and the index of the rule associated with the head is removed from the available rule list for that head. If backtracking occurs, the counter associated with the head is increased by 1, and the index of the rule is added to the available rule list.

3. Selection: The head with the counter changed to 0 or the counter changed to 1 from 0 is selected for the further propagation.

4. Go to 1.

For example, consider the following knowledge base

$$
\begin{array}{r l}\mathrm{KB2}&= \left\{\left(r 1 B \leftarrow C _ {3}\right)\left(r 2 D \leftarrow C _ {1}, B\right)\left(r 3 D \leftarrow C _ {1}, C _ {2}\right)\right.\left. \right.\\&\times \left(r 4 G \leftarrow C _ {4}, D\right) \}.\end{array}
$$

The procedure tables maintained in APN for the above knowledge base are of the form $(B\ 1\ (r1))$ , $(D\ 2\ (r2\ r3))$ and $(G\ 1\ (r4))$ , where the first element in the parenthesis is the head of a rule, the second one is the counter which represents how many rules are presented in the rule set and the third one is the index of a rule. Moreover, these procedure tables are shared with the minimal 2LP interpreter. If the goal is given as “? - G” which can be rewritten as “? - C\_{4}, D” and, at this point, the logic interpreter finds the constraint C\_{1} inconsistent with the current environment, the assertion $\langle -C_{1}\rangle$ will be made by propagating the negative token through APN. As a result, the updated procedure tables are $(B\ 1\ (r1))$ , $(D\ 0)$ and $(F\ 1\ (r4))$ . At this point, the system will already find that there is no solution since the counter for the head D is 0.

The description of implementation in the APN interpreter is provided by the Lisp code in Appendix A in [16].

## 2.4. APN in terms of stratification

The rules in the Anticipatory Pruning Network (APN) consist of the set of constraints which can be regarded as the set of atomic assertions and the propositional rules which have the form $Q_{i} \leftarrow C_{1}, C_{2}, \ldots, C_{m}, P_{1}, P_{2}, \ldots, P_{n}$

More explicitly, the rules are generated by the recursive function:

1. A set of atomic assertions which are constraints.

2. A non-empty set of definite Horn-clause rules

$$
Q _ {i} \leftarrow C _ {1}, C _ {2}, \dots , C _ {m}, P _ {1}, P _ {2}, \dots , P _ {n}
$$

where $n \geq 0$ and $m \geq 0$ .

The constraint elements $C_1, C_2, \ldots, C_n$ of the above program all lie in the same stratum. Let $\succcurlyeq$ denote a reflexive relation on the set $X$ . The strict relation $(\succ) A \succ B$ is defined as $A \succcurlyeq B$ and $A \neq B$ .

Definition 1. In Horn-clause rules in minimal 2LP, the relation $A \succcurlyeq B$ means that $A$ refers to $B$ such that either $\{A \leftarrow B_1, \ldots, B_{i-1}, B_i, B_{i+1}, \ldots, B_n\}$ or recursively, there exists some element $B'$ such that $\{A \leftarrow B_1', \ldots, B_{i-1}', B_i', B_{i+1}', \ldots, B_n'\}$ and $B \succcurlyeq B'$ in the given program.

Definition 2. The atomic element A is called minimal if there is no element B such that $B \prec A$ in the Knowledge Base. A stratum is called a minimal stratum if the stratum only consists of minimal elements.

The stratification of Horn-clause propositional logic in 2LP is a reflexive and transitive relation, $\preceq$ , on the elements of Horn-clauses which satisfies the following:

1. For all Horn-clause rules, $Q \leftarrow C_1, C_2, \ldots, C_n, P_1, P_2, \ldots, P_n$ , we have the relation $C_i \preceq Q$ and $P_i \preceq Q$ .

2. All the constraint elements are in the minimal stratum.

For example, let us consider the knowledge base, KB2 which is given in the previous section, where the minimal elements = $\{C_{1}, C_{2}, C_{3}, C_{4}\}$ and its three strata are ST21 = {r1}, ST22 = {r2, r3}, and ST23 = {r4}. The procedure tables maintained in APN for the above knowledge base are of the form (B 1 (r1)), (D 2 (r2 r3)) and (G 1 (r4)). Moreover, these procedure tables are shared with the minimal 2LP interpreter. Given the goal “:-G”, if the logic interpreter finds the constraint $C_{1}$ inconsistent with the current environment, the assertion $\langle -C_{1}\rangle$ will be made by propagating the negative token through the APN. As a result, the updated procedure tables are (B 1 (r1)), (D 0) and (F 0), where it has the single stratum ST21 = {r1} which is the rule to which the logic interpreter can refer for solving the goal list. If backtracking occurs at this point, then $\langle +C_{1}\rangle$ is propagated and the knowledge base has three strata as before.

The rules in the minimal 2LP system are all definite Horn-clauses and facts are nothing but constraints. A program in the minimal 2LP system is always stratified in the sense of the definition of stratified program in [1] since there are no negative condition elements in the program. Recently, [18] extended the stratification defined by [1]. Their definition allows a fine grain stratification which accounts for recursion through positive occurrences of procedures. We want to restrict the stratified program in such a way that there are no negative or even positive cycles in the dependency graph of the program. If there is some program which has such a cycle, then the APN would not have the property of truth maintenance behavior after the inconsistency propagation and backtracking. For instance, let us consider the knowledge base, KB3 = {R ← C₁, Q · Q → C₂, R}. If the system propagates the inconsistency of constraint C₁ and backtracks afterward, then the system cannot get back to the same list of available rules. If there are some rules involved in cycles, these rules are excluded in constructing the network. Therefore, only the remaining rules are compiled into the linearized network. Therefore, for this section we shall assume that the program is stratifiable in the sense of [18]. As an example of a stratified program, we have the program, KB2, which is graphically represented in Fig. 2.

## 3. Applications and measurement on APN

This section presents the effectiveness of the APN in the minimal 2LP system. Section 3.1 treats application issues in solving some puzzles which are traditionally considered as integer programming problems. By treating issues in modeling problems in minimal 2LP programs, we show the advantages of minimal 2LP over conventional linear programming systems. Section 3.2 provides benchmark results on APN for some mixed integer linear programming problems which can have integer or rational variables in the problem domains.

![](/api/attachments/NYYBVU8K/fulltext/images/732cf172312ede776347b9922aa7d40fb4c82121cd13ebafe415e51f3a9a66fc.jpg)  
Fig. 2. Example of a stratified program, KB2.

## 3.1. Representation and application issues of minimal 2LP

For simplicity, the two month problem is represented in minimal 2LP as shown in Appendix A for the constraint part and Appendix B for the propositional logic part. Let us describe the 2 month blending problem. A food is produced by refining nonvegetable and vegetable oils and blending them together. There are two vegetable oils, i.e., Veg1 and Veg2; and three nonvegetable oils, i.e., Oil1, Oil2 and Oil3, available for processing. Assume that the price of oils is predictable for each month and there is no loss of weight in the refining process. There is also a restriction on hardness of the final products which should range between 3 and 6. The hardness blends linearly in the final products and the hardness of each oils is known initially. The detailed description of the problem is explained in [25]. The 2 month blending problem is remodeled using minimal 2LP and showed in Appendix A.

The problem is to maximize the profit by deciding what to buy and manufacture in each month for a two month period of time with the following additional logical constraints.

1. Mixing more than three oils in any given month is not allowed.

2. If an oil is used, at least 20 tons must be used.

3. Oil3 must be used if one of the vegetable oils is used in a month.

For simplicity, the two month problem is represented in Appendix A and discussed in this section. The six month problem is also implemented in order to observe the effectiveness of APN in the larger search space.

To discuss the advantage of minimal 2LP representation over the conventional linear programming approach, we summarize the following;

(1) Disjunctive constraint: In linear programming, the conjunctive constraints can be naturally represented and solved. However, in the case of disjunctive constraints, it is not natural to represent the logical relationship of constraints by introducing new constraints and variables, which make it difficult to model problems in the linear programming approach. For an example, in a blending problem, if we are required to use either none or more than 20 tons of an oil, it is awkward to model the problem with the linear programming approach. Whereas, in the minimal 2LP language as we have represented in Appendix A, we can express it easily as follows:

$$
\begin{array}{l} \text { Fveg11: - uveg11\geq 20.} \\ \text { Fveg11: - uveg11 = 0. } \end{array}
$$

(2) Partial solution: Using IP, it is impossible to generate the partial solution especially if we want to get a solution which is close to feasible. In some cases, IP spends lots of time and ends up with nothing [7]. However, the symbolic approach not only generates a partial solution, but we also can trace out the activity of the program. In the case of minimal 2LP, the APN can address the partial solution naturally since the APN can be viewed as the propositional expert system and the current working memories in APN are the constraints found so far to be inconsistent with the current environment.

(3) Modeling power and maintenance: The formulation of a problem can be mathematically very declarative in some problems as in the simplified warehouse location problem [13]. On the other hand, the modeling of IPs which are somewhat complicated, like course scheduling [7], is a nontrivial problem. The IP program is also difficult to read for complicated problems. Moreover, as Dhar and Ranganathan in [7] point out, it is very difficult to modify the program once some underlying situation has been changed. By providing logical expression with some syntactic modification of the current minimal 2LP, the minimal 2LP can alleviate some of these problems.

(4) Expressive power: In addition to express the relations such as $\geq$ and = in linear programming, we can express various relations such as $\geq, =, \neq$ and >. This provides more expressive power which can directly describe the problem at hand. For example, if we want to express that the lunch time is not counted as on duty we can simply express as the following clause:

Duty\_except\_Lunch:-Duty\_hour ≥ Lunch\_hour + 1.

Duty\_except\_Lunch:-Lunch\_hour ≥ Duty\_hour + 1.

In our current implementation of the minimal 2LP system, the disequations, $X \neq Y$ , are converted into “ $X \geq Y + 1$ or $Y \geq X + 1$ ”. The delaying mechanism can be natural here and the pruning in the tree search space is also possible to some extent using APN. However, one disequality constraint becomes two inequality constraints. Moreover, the cost of resolving the logical operators “or” is not ignorable if there are many disequality constraints in the problem. This is actually converting static constraints into dynamic constraints in the CSP sense.

## 3.2. Measurement on APN

In this benchmark, the number of nodes visited is counted cumulatively during the tree search process. The number of constraint checks is also counted cumulatively. We counted the number of constraints appearing on the right hand side of the rule and added up cumulatively as the rule is rewritten. Consistency checking in the APN is counted as one constraint check for each node visited. The number of constraint checks here is a cumulative addition of the number of constraints appearing on the right hand of a rule and the consistency checking. However, we have supposed that the deterministic rewriting occurs as part of normal APN activity at a given node and did not include this in the count.

The No APN in this benchmark is the case when the APN is not active. Therefore, the basic search strategy is the same as the Prolog search strategy. In the Full APN, we check the consistency with all the bottom-most leaves which have not been explored yet. The Partial APN is to check the consistency with the constraints set that can be derivable from the left most branch of the search space. The left most branch of the search space here means that we check the consistency with the first bottom-most leaves in the search spaces among several branches.

In this problem, as shown in Table 2, the number of nodes visited and the number of constraint checks are reduced drastically. Moreover, the “SEND + MORE = MONEY” problem runs much faster than execution without APN in our current version of implementation even without introducing parallelism in checking consistency. Regarding this kind of problem, the APN can be very effective since (1) there are about ten branching factors in each domain, and (2) the constraints appearing in this problem are strong enough to find many of the inconsistencies for the APN.

Table 2  
Integer programming problems

<table><tr><td rowspan="2"></td><td colspan="2">No APN</td><td colspan="2">Partial APN</td><td colspan="2">Full APN</td></tr><tr><td>Node</td><td>Constraint</td><td>Node</td><td>Constraint</td><td>Node</td><td>Constraint</td></tr><tr><td>8-Queens</td><td>23,359</td><td>19,904</td><td>8,959</td><td>13,097</td><td>4,916</td><td>8,054</td></tr><tr><td>SEND + MORE = MONEY</td><td>1,641</td><td>1,509</td><td>144</td><td>243</td><td>4</td><td>12</td></tr><tr><td>GERALD + DONALD = ROBERT</td><td>11,317</td><td>10,472</td><td>1,203</td><td>1,798</td><td>438</td><td>739</td></tr><tr><td>Tennis puzzle</td><td>5,530</td><td>8,046</td><td>1,774</td><td>3,875</td><td>224</td><td>1,454</td></tr></table>

All the problems described in Table 1 can be viewed as the integer programming problems. However, many problems in linear programming are not pure integer programming problems. Some examples of the mixed linear integer programming problems are drawn from [25] for evaluating the effectiveness of the APN in the minimal 2LP system.

These mixed integer linear programming problems are not amenable to the consistency technique in CHIP because of the presence of continuous variables. Regarding this kind of problem, it is impossible to figure out whether the variables are integers or rational numbers before we actually solve them. In a blending problem, it is very reasonable to mix 1 1/2 gallons of vegetable oil with 2 1/3 gallons of non-vegetable oil to maximize the profit. Therefore, the concept of CSP cannot be applied to this kind of linear programming problem. However, with APN, it does not matter whether the domain is discrete or continuous, since we can use Simplex based consistency checking. We are required to use either none or more than 20 tons of an oil. This kind of “or” constraint can be expressed naturally by means of logic in the minimal 2LP system.

As the searching is performed, the latest found value of the objective function is added into the linear system as another constraint. Therefore, the system found more inconsistency as more nodes are visited during the search. Problem size can be significant. For example, in the two months blending problem, the number of nodes visited is not reduced drastically even with the Full APN. Moreover, the Full APN needs more constraint checks than the constraint checks with No APN in the two months blending problem. However, in the six months blending problem, the number of nodes visited and the number of constraint checks are reduced drastically as shown in Table 3.

## 4. Efficiency considerations of APN

As described at the beginning of this section, there are two components of computation in APN, which are consistency checking and the forward reasoning based on that. The major computing cost is checking constraint consistency with the current environment, since every time the current environment is updated, the consistency checking with the rest of the constraints (QC) should be performed. It may not be efficient in small problems because of the overhead in the Simplex method unless we do compute the consistency checking in parallel.

Without the parallelism, the following new implementation can be considered for the efficient implementation.

1. Mutually inconsistent constraints can be detected at compilation time. If one of the constraints among the disjunctive constraints is enforced, the rest of the disjunctive constraints are inconsistent.

2. The system can activate the consistency checking after the size of the quick list (constraints which never been used) is reduced to some level.

3. The different ways of choosing the relevant constraints is another possibility.

## 5. Related work

The CHIP system [8] is successfully implemented by adding the concept of CSP over finite discrete domains to the full power of Prolog. On the other hand, APN in the minimal 2LP system is dealing with propositional logic and the constraint solver. However, the consistency technique in CHIP is implemented at the propositional level. The predicate logic in Prolog is just used to generate the constraints and domains down to the propositional level during run time.

Table 3  
Mixed integer linear programming problems

<table><tr><td rowspan="2"></td><td colspan="2">No APN</td><td colspan="2">Partial APN</td><td colspan="2">Full APN</td></tr><tr><td>Node</td><td>Constraint</td><td>Node</td><td>Constraint</td><td>Node</td><td>Constraint</td></tr><tr><td>Six months blending problem</td><td>11,863</td><td>17,172</td><td>3,991</td><td>8,770</td><td>2,632</td><td>6,693</td></tr><tr><td>Mining problem</td><td>33,598</td><td>48,563</td><td>10,736</td><td>26,923</td><td>9,753</td><td>24,722</td></tr></table>

Both the APN in minimal 2LP and the consistency technique in the CHIP system attempted to avoid the fatal disadvantages of Prolog style searching mechanism which are labeled as “thrashing” behavior by Bobrow and Raphael [2]. However, they are functionally different. In APN, the system tries to remove the domain of each stratum by propagating inconsistency of constraints. However, the APN in the minimal 2LP system cannot prune the search space of an unstratified program. In the consistency technique in CHIP, the system tries to remove the domains of each variable in the problem. But, the system cannot prune the search space with consistency techniques if the domains of variables in the problem are not explicit. Checking consistency in CHIP is more efficient than that of APN. On the other hand, in the APN, checking consistency is somewhat separate from the propagation of the inconsistency. This can allow us to use any consistency checking mechanism, whether a CSP or Simplex based solver, depending on the problem domain. The APN is somewhat analogous to the consistency technique over discrete domains in CHIP. In contrast, the APN provides a forward checking mechanism for constraints over a continuous domain. The detailed comparison is given in [17]. In addition, the APN here preserves the operational semantics of the language which means that the backward propagation and pruning do not violate the operational semantics of the minimal 2LP language.

## 6. Conclusion

The APN in the minimal 2LP system can be very effective in solving mixed linear integer programming problems, especially if we are dealing with very large problems. Overall, regardless of problem domains, the APN is a very powerful mechanism to prune the tree search space. However, the overhead in testing consistency should be considered carefully. To minimize the overhead, there are three different methods to consider. One is checking consistency in parallel. The second is that we can apply the concept of CSP for testing consistency in the APN if it is known that the variables in the problems are finite discrete domains. The third is applying the CSP and parallelism at the same time.

The study of the APN in the minimal 2LP system has lead us to make the following conclusions.

1. The APN introduces a Forward Checking mechanism for constraints over a continuous domain. It also provides a very deep look ahead [12] for the Simplex based constraint solver. Moreover, the APN technology can be used with other solvers and other domains.

2. By using the APN, we can exploit the OR-parallelism, i.e., parallelism in consistency checking, in constraint optimization problems effectively in the minimal 2LP system [21]. As we have pointed out in the above section, the APN is very useful to solve optimization problems. Especially if we want to find an optimization solution which is a near-failure, the APN can reduce the tree search space drastically as shown in the above section.

3. The APN, which is a domain independent forward checking mechanism, opens a possibility of integrating the Simplex based constraint solver with CSP.

4. The APN can address the partial solution question naturally since the APN can be viewed as the propositional expert system, and the current working memories in the APN are the constraints found so far to be inconsistent with the current environment.

## Acknowledgements

This work is partially supported by the Korea Science and Engineering Foundation for Cooperative Research under the Korea-U.S.A. Cooperative Science Program. The authors also thank the referees for their valuable comments to improve this paper.

<table><tr><td colspan="3">Appendix A. Constraints</td><td>uoil31 /0 ≥ 44 / 5uveg11 + 61/10uveg21 + 2</td></tr><tr><td colspan="3">objective-function</td><td></td></tr><tr><td>max</td><td>-110 bveg11 -120 bveg21 -130 boil11 -110 boil21 -115 boil31 +150 prod1 - 5sveg11 - 5sveg21 -5 soil11 - 5soil21 - 5soil31 - 130bveg12-130 bveg22 -110 boil12 -90 boil22 -115 boil32 +150 prod2 /</td><td> $C_8$ </td><td>21/5 uoil21 + 5u o i l 31 - 6prod1 /0 ≥ -44 / 5uveg11 - 61/10uveg21 - 2uoil11 -21/5 uoil21 -5 uoil31 + 3prod1 /0 = 1 uveg11 + 1uveg21 + 1uoil11 +1 uoil21 + 1u o i l 31 - 1prod1 /</td></tr><tr><td>static</td><td></td><td> $C_{11}$ </td><td>0 = 1 sveg11 - 1uve g 12 + 1</td></tr><tr><td> $C_1$ </td><td>0 = 1 sveg10 - 1uve g 11 + 1bveg11 - 1sveg11 /</td><td> $C_{12}$ </td><td>bveg12 - 1sveg12 /0 = 1 sveg21 - 1uve g 22 + 1</td></tr><tr><td> $C_2$ </td><td>0 = 1 sveg20 - 1uve g 21 + 1bveg21 - 1sveg21 /</td><td> $C_{13}$ </td><td>bveg22 - 1sveg22 /0 = 1 soil11 - 1u o i l 12 + 1</td></tr><tr><td> $C_3$ </td><td>0 = 1 soil10 - 1u o i l 11 + 1boil11 - 1soil11 /</td><td> $C_{14}$ </td><td>boil12 - 1soil12 /0 = 1 soil21 - 1u o i l 22 + 1</td></tr><tr><td> $C_4$ </td><td>0 = 1 soil20 - 1u o i l 21 + 1boil21 - 1soil21 /</td><td> $C_{15}$ </td><td>boil22 - 1soil22 /0 = 1 soil31 - 1u o i l 32 + 1</td></tr><tr><td> $C_5$ </td><td>0 = 1 soil30 - 1u o i l 31 + 1boil31 - 1soil31 /</td><td> $C_{16}$ </td><td>boil32 - 1soil32 /200 ≥ 1 uveg12+ 1 uveg22 /</td></tr><tr><td> $C_6$ </td><td>200 ≥ 1 uveg11+ 1 uveg21 /</td><td> $C_{17}$ </td><td>250 ≥ 1 uoil12+ 1 uoil22 + 1</td></tr><tr><td> $C_7$ </td><td>250 ≥ 1 uoil11+ 1 uoil21 + 1uveg12 + 61 / 10</td><td> $C_{18}$ ccc</td><td>uoil32 /0 ≥ 44 / 5soil20 = 500</td></tr><tr><td rowspan="5"></td><td>uveg22 + 2</td><td>ccc</td><td>soil30 = 500</td></tr><tr><td>uoil12 +</td><td>ccc</td><td>sveg12 = 500</td></tr><tr><td>21/5 uoil22 + 5</td><td>ccc</td><td>sveg22 = 500</td></tr><tr><td>u oil 32 - 6</td><td>ccc</td><td>soil12 = 500</td></tr><tr><td>prod2 /</td><td>ccc</td><td>soil22 = 500</td></tr><tr><td rowspan="7"> $C_{19}$ </td><td>0 ≥ -44 / 5</td><td>ccc</td><td>soil32 = 500</td></tr><tr><td>uveg12 - 61 / 10</td><td></td><td></td></tr><tr><td>uveg22 - 2</td><td>ccc</td><td>sveg11 ≤ 1000</td></tr><tr><td>uoil12 -</td><td>ccc</td><td>sveg21 ≤ 1000</td></tr><tr><td>21/5 uoil22 -</td><td>ccc</td><td>soil11 ≤ 1000</td></tr><tr><td>5 uoil32 + 3</td><td>ccc</td><td>soil21 ≤ 1000</td></tr><tr><td>prod2 /</td><td>ccc</td><td>soil31 ≤ 1000</td></tr><tr><td rowspan="7"> $C_{20}$ </td><td>0 = 1 uveg12 + 1`</td><td>ccc</td><td>prod1 ≤ 700</td></tr><tr><td>uveg22 + 1</td><td>ccc</td><td>prod2 ≤ 700</td></tr><tr><td>uoil12 +</td><td></td><td></td></tr><tr><td>1 uoil22 + 1</td><td>ccc</td><td>uveg11 ≤ 200</td></tr><tr><td>u oil 32 - 1</td><td>ccc</td><td>uveg21 ≤ 200</td></tr><tr><td>prod2 /</td><td>ccc</td><td>uoil11 ≤ 250</td></tr><tr><td></td><td>ccc</td><td>uoil21 ≤ 250</td></tr><tr><td rowspan="2">binding-or-bounding</td><td></td><td>ccc</td><td>uoil31 ≤ 250</td></tr><tr><td></td><td>ccc</td><td>uveg12 ≤ 200</td></tr><tr><td> $C_{95}$ </td><td>uoil31 ≥ 20</td><td>ccc</td><td>uveg22 ≤ 200</td></tr><tr><td> $C_{65}$ </td><td>uoil31 = 0</td><td>ccc</td><td>uoil12 ≤ 250</td></tr><tr><td> $C_{94}$ </td><td>uoil21 ≥ 20</td><td>ccc</td><td>uoil22 ≤ 250</td></tr><tr><td> $C_{64}$ </td><td>uoil21 = 0</td><td>ccc</td><td>uoil32 ≤ 250\</td></tr><tr><td> $C_{93}$ </td><td>uoil11 ≥ 20</td><td></td><td></td></tr><tr><td> $C_{63}$ </td><td>uoil11 = 0</td><td></td><td></td></tr><tr><td> $C_{92}$ </td><td>uveg21 ≥ 20</td><td></td><td></td></tr><tr><td> $C_{62}$ </td><td>uveg21 = 0</td><td colspan="2">Appendix B. Rules</td></tr><tr><td> $C_{91}$ </td><td>uveg11 ≥ 20</td><td></td><td></td></tr><tr><td rowspan="2"> $C_{61}$ </td><td>uveg11 = 0</td><td colspan="2" rowspan="2">Foil21: - $C_{94}$ /Foil21: - $C_{64}$ /</td></tr><tr><td></td></tr><tr><td> $C_{100}$ </td><td>uoil32 ≥ 20</td><td></td><td></td></tr><tr><td> $C_{70}$ </td><td>uoil32 = 0</td><td colspan="2">Foil11: - $C_{93}$ /</td></tr><tr><td> $C_{99}$ </td><td>uoil22 ≥ 20</td><td colspan="2">Foil11: - $C_{63}$ /</td></tr><tr><td> $C_{69}$ </td><td>uoil22 = 0</td><td></td><td></td></tr><tr><td> $C_{98}$ </td><td>uoil12 ≥ 20</td><td colspan="2">Fveg11: - $C_{91}$ /</td></tr><tr><td> $C_{68}$ </td><td>uoil12 = 0</td><td colspan="2">Fveg11: - $C_{61}$ /</td></tr><tr><td> $C_{97}$ </td><td>uveg22 ≥ 20</td><td colspan="2">Fveg21: - $C_{92}$ /</td></tr><tr><td> $C_{67}$ </td><td>uveg22 = 0</td><td colspan="2">Fveg21: - $C_{62}$ /</td></tr><tr><td> $C_{96}$ </td><td>uveg12 ≥ 20</td><td></td><td></td></tr><tr><td> $C_{66}$ </td><td>uveg12 = 0</td><td colspan="2">Rl: - $C_{63}$  Fveg21 Fveg11/Rl: - $C_{93}$  X1 /</td></tr><tr><td colspan="2">initial-binding-or-bounding</td><td></td><td></td></tr><tr><td></td><td></td><td colspan="2">Xl: - $C_{62}$  Fveg11 /</td></tr><tr><td>ccc</td><td>sveg10 = 500</td><td colspan="2">Xl: - $C_{92}$  C61 /</td></tr><tr><td>ccc</td><td>sveg20 = 500</td><td></td><td></td></tr><tr><td>ccc</td><td>soil10 = 500</td><td colspan="2">Foil22: - $C_{99}$ /</td></tr></table>

Foil22: -C\$\_{69}\$
Foil12: -C\$\_{98}\$
Foil12: -C\$\_{68}\$
Fveg22: -C\$\_{97}\$
Fveg22: -C\$\_{67}\$
Fveg12: -C\$\_{96}\$
Fveg12: -C\$\_{66}\$
G1: -C\$\_{95}\$ Q1 /
G1: -C\$\_{65}\$ C\$\_{62}\$ C\$\_{61}\$ Foil21 Foil11 /
G2: -C\$\_{100}\$ Q2 /
G2: -C\$\_{70}\$ C\$\_{67}\$ C\$\_{66}\$ Foil22 Foil12 /
Q1: -C\$\_{64}\$ R1 /
Q1: -C\$\_{94}\$ C\$\_{63}\$ X1 /
Q2: -C\$\_{69}\$ R2 /
Q2: -C\$\_{99}\$ C\$\_{68}\$ X2 /
R2: -C\$\_{68}\$ Fveg22 Fveg12 /
R2: -C\$\_{98}\$ X2 /
X2: -C\$\_{67}\$ Fveg12 /
X2: -C\$\_{97}\$ C66 /
G02: -max C\$\_{1}\$ C\$\_{2}\$ C\$\_{3}\$ C\$\_{4}\$ C\$\_{5}\$ C\$\_{6}\$ C\$\_{7}\$ C\$\_{8}\$ C\$\_{9}\$ C\$\_{10}\$ C\$\_{11}\$ C\$\_{12}\$
C\$\_{13}\$ C\$\_{14}\$
C\$\_{15}\$ C\$\_{16}\$ C\$\_{17}\$ C\$\_{18}\$ C\$\_{19}\$ C\$\_{20}\$
G: -G02 G1 G2 /

## References

[1] Krzysztof R. Apt, Howard A. Blair and Adrian Walker, Towards a Theory of Declarative Knowledge, Foundations of Deductive Databases and Logic Programming (Morgan Kaufmann Publishers, 1988) 89–148.

[2] D.G. Bobrow and B. Raphael, New Programming Languages for AI Research (Computing Surveys 6, 1974) 153–174

[3] Jacques Cohen, Constraint Logic Programming Languages, Communications of the ACM 33, No. 7 (1990) 52–68.

[4] Alain Colmerauer, An Introduction to Prolog III, Communications of the ACM 33, No. 7 (July 1990) 69–90.

[5] Jim Cox, Ken McAloon and Carol Tretkoff, Computational Complexity and Constraint Logic Programming, Annals of Mathematics and Artificial Intelligence (1992) 163–190.

[6] Ernest Davis, Constraint Propagation with Interval Labels, Artificial Intelligence 32 (North-Holland, Amsterdam, 1987) 281–331.

[7] Vasant Dhar and Nicky Ranganathan, Integer Programming

vs. Expert Systems: An Experimental Comparison, Communications of the ACM (March 1990) 323–336.

[8] M. Dincbas, Pascal Van Hentenryck, H. Simonis, A. Aggoun, T. Graf and F. Berthier, The Constraint Logic Programming Language CHIP, Proceedings of the International Conference on Fifth Generation Computing Systems (1988).

[9] Charles Forgy, On the Efficient Implementation of Production Systems, Ph.D. Thesis, Carnegie-Mellon University, 1979.

[10] Charles Forgy, Rete: A Fast Algorithm for the Many Pattern/Many Object Pattern Match Problem, Artificial Intelligence 19, (North-Holland, Amsterdam, 1982) 17–37.

[11] Robert M. Haralick and Gordon L. Elliott, Increasing Tree Search Efficiency for Constraint Satisfaction Problems, Artificial Intelligence 14 (North-Holland, Amsterdam, 1980) 263–313.

[12] Pascal Van Hentenryck, Constraint Satisfaction in Logic Programming (The MIT Press, 1989).

[13] Pascal Van Hentenryck and Jean-Philippe Carillon, Generality versus Specificity: An Experience with AI and OR Technique, AAAI Proceedings (1988) 660–664.

[14] J. Jaffar and J.L. Lassez, Constraint Logic Programming, Fourteenth ACM Symposium on the Principles of Programming Languages (Munich, 1987) 111–119.

[15] J. Jaffar and S. Michaylov, Methodology and Implementation of a Constraint Logic Programming System, Proceedings of the Fourth International Conference on Logic Programming (Melbourne, MIT Press, 1987) 196–218.

[16] Geun-Sik Jo, Anticipatory Pruning Networks and Minimal 2LP, Ph.D. Thesis, CUNY (Feb. 1991).

[17] Geun Sik Jo, Ken McAloon, Constraint Solving in CLP language, Proceedings of the 2nd Pacific Rim International Conference on Artificial Intelligence (Sept. 15–18, 1992) 758–763.

[18] Catherine Lassez, Ken McAloon and Graeme Port, Stratification and Knowledge Base Management, Journal of Symbolic Computation (1989) 509–522.

[19] Catherine Lassez, Ken McAloon and Roland Yap, Constraint Logic Programming and Option Trading, IEEE Expert (Fall), (IEEE Computer Society, 1987) 42–50.

[20] Alan K. Mackworth, Consistency in Networks of Relations, Artificial Intelligence 8 (North-Holland, Amsterdam, 1977) 99–118.

[21] K. McAloon and C. Tretkoff, 2LP: A Logic Programming and Linear Programming System, Proceedings of PPCP '93 (edited by P. Kanellakis, J.L. Lassez and V. Saraswat, 1993).

[22] Daniel P. Miranker, TREAT: A Better Match Algorithm for AI Production Systems, AAAI-87 Proceedings (July) (American Association for Artificial Intelligence, 1987) 42–47.

[23] Bernald A. Nadel, Representation Selection for Constraint Satisfaction: A Case Study Using N-Queens, IEEE Expert (June) (IEEE Computer Society, 1990) 16–23

[24] Guy L. Steele, The Definition and Implementation of a Computer Programming Language Based on Constraints, Ph.D. Thesis (MIT, Aug. 1980).

[25] H.P. Williams, Model Building in Mathematical Programming (John Wiley & Sons, 1985).

![](/api/attachments/NYYBVU8K/fulltext/images/1ac41d5c279388e72272870db6ede0ef606b9c49363662d2494e67a3a11a37b0.jpg)  
Geun-Sik Jo received his B.S. degree from the Department of Computer Science, Inha University in 1982, his M.S. in Computer Science from Queens College/CUNY in 1985, and his Ph.D. in Computer Science from the City University of New York in 1991. Geun-Sik Jo is currently Assistant Professor in the Department of Computer Science and Engineering, Inha University in Inchon, Korea. His research interests include CLP languages, intelligent scheduling and expert systems.

![](/api/attachments/NYYBVU8K/fulltext/images/dedc2d89ecc9bee263fd73af695b674066ca69b9cabdf51718e5026eba400978.jpg)  
Ken McAloon is Broeklundian Professor of Computer Science at Brooklyn College and the CUNY Graduate Center. He is the head of the Logic Based Systems Lab and a specialist in constraint logic programming. He has taught at the University of Paris and Princeton University and is the author of Optimization and Computational Logic (Wiley) and numerous research papers.
