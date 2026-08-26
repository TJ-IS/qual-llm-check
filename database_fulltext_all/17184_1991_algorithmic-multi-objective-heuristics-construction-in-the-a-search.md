---
otero_id: 17184
otero_key: "HECCCTUJ"
title: "Algorithmic multi-objective heuristics construction in the A ∗ search"
authors: "Yuval Lirov"
year: "1991"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(91)90054-f"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Algorithmic multi-objective heuristics construction in the A\* search

Yuval Lirov

AT&T Bell Laboratories, Holmdel, NJ 07733-1988, USA

Merging multi-objective optimization and expert systems technology results in reduced modeling efforts and enhanced problem-solving tools. Search is one of the ways to combine multi-objective optimization and knowledge-intensive computation schemes. Search is usually associated with prohibitive computational costs and heuristics are often used to alleviate the computational burden. We propose an efficient algorithm for constructing multi-objective heuristics. We also develop some sufficiency conditions for the admissibility of the heuristic. Our multi-objective A\* algorithm has been implemented and experimentally evaluated. Its time performance is comparable and often superior to that of other more conventional algorithms.

Keywords: Multi-objective optimization, Artificial intelligence, Software engineering, Expert systems, Heuristic search.

![](/api/attachments/HECCCTUJ/fulltext/images/84175f4406fc1400e6d25d7589fa35e0a178876d90ecf9392d4e79f675ce9bcf.jpg)

Yuval Lirov is a Member of Technical Staff at AT&T Bell Laboratories in Holmdel, New Jersey, where he develops troubleshooting and scheduling expert systems for telecommunication and manufacturing operations. Prior to joining Bell Laboratories, he was Deputy Director of the Semantic Control Laboratory at Washington University in St. Louis, Missouri, where he developed numerous knowledge-based software applications such as stereotactic neurosurgery systems and

tactical decision systems for air combat. He studied Mathematics at Vilnius State University in Lithuania, Operations Research at the Technion in Israel, and Artificial Intelligence and Control at Washington University. A winner of the AIAA-87 Outstanding Achievement Award in Artificial Intelligence, Dr. Lirov has authored over fifty technical publications. He holds several patents and he has recently edited a book on Applications of Logic Programming in Decisions and Control.

## 1. Introduction

This paper pertains to an intersection of three disciplines: computer software engineering, operations research, and artificial intelligence. Specifically, we develop an algorithm to automatically compute a heuristic which can speed up significantly the search for a solution of a multi-objective optimization problem. Merging multi-objective optimization and expert systems technology results in reduced modeling efforts and enhanced problem-solving tools. Search is one of the ways to combine multi-objective optimization and knowledge-intensive computation schemes. Search is usually associated with prohibitive computational costs and heuristics are often used to alleviate the computational burden. We propose an efficient algorithm for constructing multi-objective heuristics. We also develop some sufficiency conditions for the admissibility of the heuristic. Our multi-objective A\* algorithm has been implemented and experimentally evaluated. Its time performance is comparable and often superior to that of other more conventional algorithms.

## 1.1. Motivation

## 1.1.1. Background

Multiobjective optimization finds its application in numerous fields, e.g., pollution control, communications, scheduling, computer aided design, inventory control, navigation, etc. (Fleming and Pashkevich, 1985; Lirov, 1988; Lirov and Ghosh, 1987; Liu, 1982; Murahlidhar and Sundareshan, 1982; Nishikawa et al, 1982; Payne, 1982; Sakawa et al., 1978; Ng, 1988; Rajurkar et al, 1987; Sakawa and Seo, 1982; Tabak et al, 1978; Tabak et al, 1979; Taludkar and Koo, 1978; Toivenen, 1984). The use of expert system technology in solving multi-objective optimization problems is motivated because of the inherent difficulties in mathematical modelling. Generally, optimization techniques require rigorous mathematical description of the problem and abstraction from the irrelevant details. The abstraction process is usually performed by the human modellers. This process is error-prone and time consuming. Numerous difficulties to establish the precise form of the objective functions and constraints naturally motivated the use of interactive programs which adapt the objectives and constraints by querying the user for additional information during the solution process. The so-called knowledge-intensive computation schemes supplement the classical optimization problem solving methods. (Korhonen, 1986; Korhonen et al, 1986; Carlsson, 1987; Yang et al, 1987; Malakooti, 1989; Mahmoud, 1977; Malakooti and Ravindran, 1986; Sadagapan and Ravindran, 1986; Steuer, 1977; White, 1980; Stewart, 1987; White et al, 1984).

## 1.1.2. Expected Benefits

A basic advantage of knowledge-based programs is their explicit representation of knowledge (the facts and the rules about a particular domain to infer new facts). Explicit representation of knowledge allows to continue knowledge acquisition after the program has been deployed. In fact, it is often impossible to complete knowledge acquisition for a system without having the system deployed first (cf. DEC's XCON – an expert system used to configure computer equipment). Merging multiobjective optimization and knowledge-based approaches holds promise to benefit from the advantages of both worlds: optimization with respect to several objectives and explicit management of knowledge.

## 1.1.3. The Domain

This work pertains to the area of automatic construction of means to combine different problem-solving paradigms. Software implementations of such combined methods require development of specialized inference mechanisms. The interested reader may wish to consult (Sterling and Beer, 1989) on the use of metaprogramming to combine various computational paradigms. Whatever amalgamation method is used, search is currently the resulting problem-solving process. In contrast to the general methods of paradigm amalgamation (e.g., metaprogramming), we draw on the specifics of the multiobjective search. We also address only one issue, though an important one in all similar problems, namely, the issue of speeding up the multiobjective search. This issue is commonly treated by the methods of heuristic search (Pearl, 1984).

Search is a technique of repeatedly transforming a candidate for the optimal solution until no improvement can be made. Two cardinal requirements are usually posed when searching: the first requirement is the efficiency requirement, which ensures that no candidate is generated twice; and the second is the utility requirement which ensures that the optimal candidate will not be missed.

Application of the search techniques, however, usually brings an additional major complication: prohibitive computational cost. Heuristic search is an AI technique which can be efficiently used to alleviate this complication. Heuristics stands for the strategies which use easily accessible but loosely applicable information to efficiently control search processes. The main result in the heuristic search theory is the A\* algorithm, which, assuming an additive single-objective function and a heuristic function satisfying the condition that it is never greater than the objective, always returns the minimal solution. Moreover, the A\* algorithm usually waists significantly less resources (i.e., generates fewer candidates) to obtain the optimal solution. We aim at utilizing the A\* algorithm for the purposes of multiobjective optimization.

## 1.1.4. The Task

In multiobjective optimization, one can not usually expect to obtain a single optimal solution that is preferred to all other solutions with respect to all objectives. Roughly speaking there are two approaches to define the meaning of an “optimal solution” for the problems involving multiple objectives. The first approach requires introduction of a concept of dominance, or Pareto optimality. This approach is covered in several books, (Chankong and Haimes, 1983; Keeney and Raiffa, 1976; Steuer, 1986; Sawaragi et al., 1985; Zeleny, 1982). The second approach translates multiobjective problems into multiattribute problems, i.e., problems in which several objectives are somehow combined into a scalar criterion. Following the translation, a conventional single-objective optimization technique can be used. This work combines both approaches to construct an efficient heuristic in order to solve faster the multiobjective optimization problems using search.

## 1.2. Related Work

## 1.2.1. Special Heuristics Construction

Several authors have considered the problem of heuristically speeding up the multiobjective optimization problems. Wang and Lu (Wang and Lu, 1987) present a strategy to carry out the weighting associated with the epsilon-constraint approach to multiobjective optimization. Their method allows to use incomplete knowledge. (Norbis and MacGregor, 1988) present a multi-level, multi-priority heuristic which is specially taylored for the use in quasi-dynamic scheduling environments. Some other heuristics are described in (Malakooti, 1988; Murahlidhar et al, 1984; and Osternark and Salmela, 1988). The use of fuzzy techniques in multiobjective optimization is described in (Chen et al, 1984 and Xu, 1988). When using heuristic methods to solve multiobjective optimization problems, the issues of utility (testing every candidate) and efficiency (not testing a candidate more than once) are often overlooked in favor to the issues of time performance. A\* is a search method which enjoys the important properties of utility and efficiency as long as the heuristics satisfy several necessary requirements.

## 1.2.2. The Use of Heuristics

We extend the recent work of Stewart and White (Stewart and White, 1987), who develop a multiobjective generalization of the heuristic search algorithm A\* and refer to it as MOA\*. MOA\* uses a set of vector-valued heuristic functions providing information on costs (values) to be accrued along a portion of a solution path. MOA\* algorithm has the important properties of completeness (a solution is discovered if it exists) and admissibility (all the solutions are discovered) when used with any admissible set of heuristic functions. The authors do not, however, propose an automated method to construct such a set of heuristic functions.

## 1.2.3. Automatic Generation of Heuristics

Automatic heuristic construction is an important Artificial Intelligence research topic. One possible approach to compute admissible heuristics for the A\* algorithm is by solving auxiliary, less constrained subproblems of the given problem (Gashnig, 1979). Unfortunately, such a computation is known to be inefficient (Valtorta, 1984). Pearl (Pearl, 1984) has postulated changing the representation paradigm to solve auxiliary problems efficiently. Our work falls into this class of methods, where we translate a multi-objective prioritized problem into a single-objective multi-attribute problem in order to obtain a good heuristic automatically.

In particular, we propose an alternative algorithm to construct a multi-objective counterpart of the fundamental A\* algorithm. The key feature of our method is the ability to construct the heuristic for the multi-objective search problems in real time, making the method particularly applicable in the problems of interactive search. Under very mild assumption of being able to assign priorities to the objectives, we also prove that the above heuristic is admissible, or in other words, that the resulting A\* search will always return the optimal solution. This work also extends the search related results reported in (Lirov, 1988) and (Lirov and Ghosh, 1988) to the cases where the number of objectives exceeds two.

## 1.3. Performance Evaluation

There are two ways to measure the performance of an algorithm: analysis and experimentation. Analysis of search algorithms is usually very hard and the performance results tend to pertain to special cases, e.g., the worst case performance analysis. Experimentation with search algorithms is often the only realistic performance estimation method. The main weakness of experimentation is that the time performance of an algorithm becomes dependent on the capabilities of both the programmer and the machine. On the other hand, using experimentation, the performance of the algorithm can be estimated even in the cases which do not submit to the analytic methods. There are no good methods to alleviate the programmer dependency problem, but the problem of machine-dependency can be treated by the techniques of scaling the observed times.

We use experimentation to demonstrate the benefits of our approach. We have tried our technique on two difficult problems: a modified Travelling Salesman Problem (Lirov, 1988) and a problem of simultaneous identification and control of linear time-variant dynamical systems (Lirov and Ghosh, 1987, 1988) and obtained very encouraging results. In particular the performance of its Pascal implemented code, solving a modified Travelling Salesman Problem, was compared with various other techniques including the multi-algorithm approach (Doty, 1988), and the linear programming approach (Padberg and Rinaldi, 1988). The program has been tested on a set of eight problems of different levels of difficulty. It was more powerful than the multialgorithm program in the half of the cases and it was more powerful than the program based on the linear programming in most of the cases (Deutch, 1988).

## 1.4. Road Map

Since we are interested in algorithmic construction of multiobjective optimization search heuristic – which belongs respectively to Software Engineering, Operations Research, and Artificial Intelligence – we use the terminology and methods of each of the domains as the need arises. To facilitate better readability, we first review the state space approach and the fundamental result of the heuristic search theory in section 2. Then we propose the algorithm for the multi-objective heuristic construction and prove its important characteristics. We conclude the paper by suggesting several future research directions.

## 2. State Space Paradigm and Search

## 2.1. State Space

One of the most popular methodologies in Artificial Intelligence is perhaps the heuristic search theory, formalized in Hart et al. (1968). It is based on the notion of state and operator. From the point of view of the computer, a state is a data structure. An operator is a means of transforming one state into another. From the computational point of view, an operator is a procedure.

A description of a state-space problem is the triple (S, F, G) where S is a set of possible starting states, F is a set of operators, and G is a set of desired states, or goals. A solution to a state-space problem is the triple (s, f, g) where s and g are states such that $s \in S$ and $g \in G$ , and f is a finite sequence of operators $q_{1}, \ldots, q_{n}$ such that

$$
\mathbf {g} = \mathrm{q} _ {\mathrm{n}} ^ {0} \mathrm{q} _ {\mathrm{n-1}} \dots {} ^ {0} \mathrm{q} _ {1} (\mathrm{s}),
$$

where $q_{i}^{0}q_{i-1}$ 's a composition of the operators $q_{i}$ and $q_{-1}$ .

Definition 1. A search graph is a collection of nodes (vertices) and arcs (edges) that correspond to states and operators, respectively. An arc, which is drawn as an arrow, leaves the parent node and enters the successor node. A node with no successors is a terminal node. A sequence of arcs and nodes from node A to node B is called a path from A to B. A is an ancestor of B when there exists a path from A to B (B is a descendant of A).

Therefore, an (S, F, G) problem solution involves finding paths between prespecified nodes in a graph. Note that the state-space paradigm can be viewed recursively, i.e., nodes can be identified as problems and arcs as operators that change problems into other problems.

## 2.2. Search

A procedure to generate a subspace of the state space for a problem, and to examine that subspace for a solution, is said to search the state space, and is called a search procedure. Search procedures, embodying heuristic information, are called heuristic procedures. The advantage of heuristic procedures stems from their ability to find the solution without generating the entire state space, thus shortening the time needed for solution.

## 2.2.1. Heuristic Search

We need heuristic since we are unable to establish the value of the entire path explicitly - the value of the path is computed by adding necessarily the values of the descendants of the current node as they are selected. The power of heuristic is in the ability to estimate the potential contribution of the descendants.

Basically there are two levels of incorporating heuristics into a search procedure: the state generation level and the state evaluation level. The state generation refers to the process of generating all successors of a given node. The state evaluation refers to the process of estimating the likelihood that the node lies on a path to a goal node.

A search procedure that expands nodes in the order in which they are generated, after generating all of them for a given node, is called a breadth-first search procedure. A search procedure that expands the most recently generated node is called a depth-first search procedure. A generation function may incorporate heuristics to generate first those successors which are most likely to lie on the paths to a goal node.

## 2.2.2. Admissibility

An ordered search procedure using the evaluation function f is a search procedure that expands the previously generated unexpanded node n for which $f(n)$ is a minimum, i.e., $n = \arg \min f$ . The central result in heuristic search theory is that of (Hart et al. 1968):

Theorem 1. For a given state-space problem (S. F, G) let $\mathrm{g}(\mathfrak{n})$ be the depth of node $\mathfrak{n}$ from the start node; let $\mathrm{h}(\mathfrak{n})$ be an estimate of the length $\mathrm{h}_{\mathfrak{p}}(\mathfrak{n})$ of the shortest path from $\mathfrak{n}$ to a goal node. If for any node $\mathfrak{n}$ we have $\mathrm{h}(\mathfrak{n}) \leq \mathrm{h}_{\mathfrak{p}}(\mathfrak{n})$ , then an ordered search procedure using the evaluation function $\mathrm{f}(\mathbf{x}) = \mathrm{g}(\mathbf{x}) + \mathrm{h}(\mathbf{x})$ will always find the shortest solution path. (The reader is referred to Hart et al, for a discussion on a very important distinction about the difference between a minimum cost path and a minimum length path).

## 2.2.3. $A^{*}$ Algorithm

When the requirements of the theorem are satisfied, the heuristic h is said to be an admissible heuristic, and the procedure is called an admissible procedure. An ordered search procedure that in addition to heuristic also incorporates dynamic programming is referred to as an A\* algorithm. Dynamic programming here means the following rule:

if two or more paths reach a common node, disregard all paths but the one with minimum cost.

The A\* algorithm can be stated as follows:

Form a queue of partial paths. The initial queue consists of a 0-length path. Until queue is empty or the goal has been reached, determine if the first path in the queue reaches the goal. If the goal is reached then do nothing. Otherwise

\- Remove the first path from the queue.

\- Form new paths from the removed path by extending 1 step.

\- Add the new paths to the queue.

\- Sort the queue by the (cost accumulated so far + estimate) with least cost paths in front.

\- If two or more paths reach a common node, leave only one with the minimum cost.

If the goal is found, then exit with success, otherwise exit with failure.

## 3. Multiple Objective Search Heuristic

When the value of the node depends on several criteria, the question of construction of the evaluation function becomes of primary importance. The evaluation function is used to satisfy the utility requirement (one of the two cardinal requirements posed when searching) to ensure that the optimal candidate is not missed during the search. Prior to giving a rigorous definition of a multiobjective goal node, we now discuss its characteristics informally.

Example. In many problems one objective is more important than the other. For example, in (Lirov, 1988), a Modified Traveling Salesman Problem (TSP) is considered, where in addition to the usual TSP formulation, each city is assigned a numerical value. There is no need to visit all the cities, but there is a total cost constraint B posed on the travelling salesman tours. The goal is to find a tour maximizing the accumulated value while staying within the cost constraint. Given two feasible tours of equal value, the tour with the lower cost is considered superior. By considering the reciprocal of the accumulated value we may characterize the goal node as follows:

$$
\min \nu_ {1}, \nu_ {2}
$$

$$
\mathrm{s.t.} \nu_ {2} \leq \mathrm{B},
$$

where $\nu_{1}$ is the reciprocal of the accumulated value and $\nu_{2}$ is the cost of the tour. It is important to note that by minimizing the second objective we may differentiate between the two nodes that appear to be optimal with respect to the first objective. In general:

Definition 2. We say that a function f is a nondecreasing (nonincreasing) function if the following inequality holds:

$$
\mathrm{f} \left(\mathrm{n} ^ {\prime}\right) \geq (\leq) \mathrm{f} (\mathrm{n}),\tag{1}
$$

for all nodes n and all nodes $n'$ which are descendants of n in the search tree.

A multi-objective goal node $n_{opt}$ is characterized by a set V of nondecreasing functions

$$
\mathbf {V} = \left\{\nu_ {\mathrm{i}} \right\} _ {\mathrm{i} = 1} ^ {\mathrm{v}},\tag{2}
$$

such that the following requirements are satisfied:

$$
\nu_ {1} \left(\mathrm{n} _ {\text { o   p   t }}\right) \geq \nu_ {1} (\mathrm{n}),\tag{3}
$$

for any $n$ in the (search tree) state space, and

$$
\nu_ {k + 1} (n _ {\text { opt }}) \geq \nu_ {k + 1} (n),\tag{4}
$$

for all nodes n such that

$$
\nu_ {k} (n _ {\text { opt }}) = \nu_ {k} (n),\tag{5}
$$

for all k = 1, ..., v - 1.

The power of our heuristic stems from the ability to forecast the contribution of the prospective nodes with respect to the multiple objectives in a single scalar value. It is the multiplicity of objectives that our heuristic addresses directly. Roughly, we replace the existing objective functions with an alternative function h which combines the original prioritized objective functions in a single scalar so as to preserve the original priorities. In other words, if $h(a) \leq h(b)$ and $\nu_{1}(a) = \nu_{1}(b)$ then $\nu_{2}(a) \leq \nu_{2}(b)$ and vice versa, where $\nu_{1}$ and $\nu_{2}$ are the original objective functions.

This feature is achieved by a lexicographic mapping technique adopted in most number systems. We use analogy to motivate our selection of a single objective heuristic. In digital number systems the value of a number is computed by multiplying the digits of the number by the powers of the base. The rightmost digit gets to be multiplied by the zeroth power of the base. The next digit to the left - by the first power of the base, and so on. Therefore, the digits to the left bear more significance. Constructing by analogy, we combine the multiple objectives into a single scalar by computing a polynomial $h(x)$ , where the coefficients are taken to be the objectives and the argument x is taken to satisfy several important properties. So, in the modified TSP example we may take a heuristic to be

$$
\mathrm{h} = \nu_ {1} ^ {2} + \nu_ {1} \nu_ {2},
$$

which, assuming that $\nu_{1}(n)>1$ for all n, will always minimize with respect to $\nu_{1}$ before minimizing with respect to $\nu_{2}$ . In other words, the accumulated value will be maximized and the total tour cost will be minimized.

A minor inconvenience of this technique is that the new objective function has different values than any of the original functions. Thus we have to prove that both sets of functions (the new, single-valued, and the original, prioritized, multi-objective) attain their optima at the same points in the state space. We refer to this property as consistency. Additionally, we have to prove two other points about the search algorithm, using the new objective function: 1) it tests all the nodes which promise to attain optimum (utility), and 2) it does not test the same node more than once (efficiency). Lemma 1 proves consistency. Utility and efficiency are proved using the fundamental result of Hart et al about admissibility of the heuristic. We state our main result in Theorem 2 which is trivially obtained from Lemmas 1 and 2.

Now we turn to the construction of a general evaluation function.

First we give a definition of the composite evaluation function and then prove its several important features. In particular, we show that the composite evaluation function h is order preserving. Additionally, by trivially modifying h we can always satisfy $h \leq \nu_{i}$ for all $i = 1, \ldots, v$ . Finally, by minimizing h, we minimize $\nu_{1}, \nu_{2}, \ldots, \nu_{v}$ in this order of preference. Now, since the conditions of Theorem 1 are satisfied, we obtain our main result:

Theorem 2 (multi-objective $A^{*}$ search). The $A^{*}$ algorithm, employing the composite cost function, returns an optimal multi-objective goal node, when one exists.

Definition 3. A composite evaluation function h is recursively constructed as:

$$
\begin{array}{l} \tilde {\nu} _ {i} \triangleq \nu_ {i} / (\nu_ {i} + 1), i = 2, \dots , v, \\ h _ {1} = \tilde {\nu} = \nu_ {1}, \\ h _ {k} = h _ {k - 1} * (h _ {k - 1} + \tilde {\nu} _ {k - 1}), \quad k = 2, \dots , v. \end{array}\tag{6}
$$

Lemma 1. A composite evaluation function is order-preserving, i.e.,

$$
\mathrm{h} _ {\mathrm{k}} (\mathrm{n}) \geq \mathrm{h} _ {\mathrm{k}} (\mathrm{m}) i f f \mathrm{h} _ {\mathrm{k} - 1} (\mathrm{n}) \geq \mathrm{h} _ {\mathrm{k} - 1} (\mathrm{m}).\tag{7}
$$

Proof. We first prove that if $h_{k-1}(n) \geq h_{k-1}(m)$ then $h_k(n) \geq h_k(m)$ . We use mathematical induction. Let k = 2, and assume $h_2(n) \geq h_2(m)$ .

Then

$$
\mathrm{h} _ {1} (\mathrm{n}) \left(\mathrm{h} _ {1} (\mathrm{n}) + \tilde {\nu} _ {1} (\mathrm{n})\right) \geq \mathrm{h} _ {1} (\mathrm{m}) \left(\mathrm{h} _ {1} (\mathrm{m}) + \tilde {\nu} _ {1} (\mathrm{m})\right).\tag{8}
$$

But $\nu_{1} = h_{1}$ by definition. Therefore $h_{1}(n) \geq h_{1}(m)$ . Assume Eq. (7) true for all $k \leq s$ . Let $h_{s+1}(n) \geq h_{s+1}(m)$ . If $\tilde{\nu}_{s}(n) \geq \tilde{\nu}_{s}(m)$ then $h_{s}(n) \geq h_{s}(m)$ holds trivially.

Now assume that

$$
\tilde {\nu} _ {s} (n) <   \tilde {\nu} _ {s} (m).\tag{9}
$$

If $h_s(n) < h_s(m)$ , then $h_{s+1}(n) < h_{s+1}(m)$ , which contradicts the assumption.

Now we prove the other direction. If $h_{s}(n) \geq h_{s}(m)$ then $h_{s}(n)/h_{s}(m) \geq 1$ . But

$$
\frac {\mathrm{h} _ {\mathrm{s}} (\mathrm{m}) + \tilde {\nu} _ {\mathrm{s}} (\mathrm{m})}{\mathrm{h} _ {\mathrm{s}} (\mathrm{n}) + \mathrm{gn} _ {\mathrm{s}} (\mathrm{n})} <   \frac {\mathrm{h} _ {\mathrm{s}} (\mathrm{m}) + 1}{\mathrm{h} _ {\mathrm{s}} (\mathrm{n})} \leq 1.\tag{10}
$$

$$
\frac {\mathrm{h} _ {\mathrm{s}} (\mathrm{n})}{\mathrm{h} _ {\mathrm{s}} (\mathrm{m})} > \frac {\mathrm{h} _ {\mathrm{s}} (\mathrm{m}) + \tilde {\nu} _ {\mathrm{s}} (\mathrm{m})}{\mathrm{h} _ {\mathrm{s}} (\mathrm{n}) + \tilde {\nu} (\mathrm{n})}, \quad \text { or }\tag{11}
$$

$$
\mathrm{h} _ {\mathrm{s} + 1} (\mathrm{n}) > \mathrm{h} _ {\mathrm{s} + 1} (\mathrm{m}).\tag{12}
$$

Lemma 2. $\mathsf{h}_{\mathsf{k}}(\mathsf{n})\cdot \tilde{\nu}_{\mathsf{k}}(\mathsf{n})\leq \mathsf{h}_{\mathsf{k}}(\mathsf{n}_{\mathrm{opt}})\tilde{\nu}_{\mathsf{k}}(\mathsf{n}\mathsf{o}_{\mathrm{pt}})$ for any k and for any n being an ancestor of $\mathsf{n}_{\mathrm{opt}}$

Sketch of Proof. From the definitions of h and $\tilde{\nu}$ , the composite cost function (used as a heuristic) always satisfies $h_{k}(n) \leq 2 \cdot h_{k-1}^{2}(n)$ . Therefore, $h_{k}$ is an admissible heuristic for $2h_{k-1}^{2}$ . Now continue using mathematical induction.

## 4. Conclusions

We proposed a method to construct heuristics which are useful when dealing with search problems with multiobjective criteria, that can be ranked in some hierarchy. We prove the admissibility of the heuristic and show that very mild conditions need to be satisfied in order for the heuristic to be admissible. Our method constructs a single-valued heuristic from a set of prioritized objective functions, thus allowing to use A\* algorithm directly. Automated construction of multivalued heuristics, which would provide mechanized means of using MOA\* algorithm, is an important area for future research.

We have not addressed the issues of termination and completeness, since they have been addressed in several other works (e.g., Pearl, 1984, and Stewart and White, 1987). This paper does not contain information about the software tools used to construct such multiobjective expert systems which might use the heuristics described in the paper. We only note that we have coded and applied the algorithm for two problems: a modified travelling salesman problem (Lirov, 1988), and a problem of simultaneous identification and control of linear time-variant dynamical systems (Lirov and Ghosh, 1987, 1988), and obtained very encouraging results. It seems to be a proper place to speculate about the $\overline{\mathbf{A}}^*$ algorithm which is the time variant version of the $\mathbf{A}^*$ algorithm. It is the original $\mathbf{A}^*$ algorithm with the alteration that before removing the first path from the queue, the queue itself is to be resorted according to the new costs of the paths. Some preliminary results on the complexity of sorting time-varying data are reported in (Geist and Lirov, 1989).

## Acknowledgements

The author is grateful to Jakub Segen from AT&T Bell Laboratories and to Bijoy Ghosh and Ervin Rodin from Washington University, St. Louis, for numerous suggestions that improved the quality of the paper.

## References

[1] Carlsson, C., Approximate Reasoning Through Fuzzy MCDM-methods. Proceedings of the 11th Operational Research Conference, pp. 817–28. 10--14 Aug. 1987, Buenos Aires, Argentina.

[2] Chankong, V. and Y.Y. Haimes, Multiobjective Decision Making: Theory and Methodology, Amsterdam: Elsevier Science Publishing, 1983.

[3] Chen, D., Y. Pan, and J. Xue, A Fuzzy Production System For Multi-objective Scheduling to a One-Machine-N-Parts Problem, Proceedings of the 23rd IEEE Conference on Decision and Control, 1101–2, Vol. 2, 1984.

[4] Deutsch, O., Artificial Intelligence Design Challenge -

Background, Analysis, and Relative Performance of Algorithms, Journal of Guidance, Control, and Dynamics, Vol. 11, No. 5, September–October 1988, pp. 386–393.

[5] Doty, K., Multiple Algorithm Solution to the Artificial Intelligence Design Challenge, Journal of Guidance, Control, and Dynamics, Vol. 11, No. 5, September–October 1988, pp. 397–402.

[6] Fleming, P.J., and A.P. Pashkevich, Computer Aided Control System Design Using A Multi-objective Optimization Approach, International Conference – Control 85, 174–9, Vol. 1, 1985.

[7] Gashnig, J., A Problem Similarity Approach to Devising Heuristics: First Results, in Proceedings of the 6th International Joint Conference on Artificial Intelligence, 1979, pp. 301–307.

[8] Geist, D. and Y. Lirov, Time-Variant Decision Support Systems, 1989, Systems, Man, and Cybernetics Conference Proceedings, pp. 244–249.

[9] Hart, P., N. Nilsson, and B. Raphael, A Formal Basis for the Heuristic Determination of Minimum Cost Paths, IEEE Transactions Systems, Science and Cybernetics, SSC-4(2), (100–107), 1968.

[10] Keeney, R.L., and H. Raiffa, Decisions with Multiple Objectives. Preferences and Value Tradeoffs, John Wiley and Sons, 1976.

[11] Korhonen, P.J., A Hierarchical Interactive Method for Ranking Alternatives with Multiple Qualitative Criteria, European Journal of Operational Research, 24, 265–276, Sept.-Oct. 1986.

[12] Korhonen, P., H. Moskowitz, and J. Wallenius, A Progressive Algorithm for Modeling and Solving Multiple-Criteria Decision Problems, Operations Research, 34 (Sept.-Oct. 1986), 726–731.

[13] Lirov, Y., Expert Systems Approach for Generalized Traveling Salesman Problem, Journal of Guidance, Control and Dynamics, September–October 1988, pp. 495–429.

[14] Lirov, Y. and B.K. Ghosh, Simultaneous Identification of Linear Systems: A Heuristic Approach, Systems and Control Letters, 9, 1987, pp. 317–322.

[15] Lirov, Y., and B.K. Ghosh, Robust Identification and Control of Linear Time Varying Dynamical Systems, Proceedings of the 27th CDC, 1988, pp. 1818–1822.

[16] Liu, Y.A. A Practical Approach to the Multi-objective Synthesis and Optimizing Control of Resilient Heat Exchanger. Network, Proceedings of the 1982 American Control Conference, 1115–26, Vol. 3, 1982.

[17] Mahmoud, M.S., An Extension of Hierarchical Dynamic Control to Multi-objective Optimization, Proceedings of the International Conference on Cybernetics and Society, 368–72, 1977.

[18] Malakooti, B., An Exact Interactive Method for Exploring the Efficient Facets of Multiple Objective Linear Programming Problems with Quasi-Concave Utility Functions, IEEE Trans. on Systems, Man, and Cybernetics, Vol. 18, No. 5, pp. 787–801, 1988.

[19] Malakooti, B., A Decision Support System and a Heuristic Interactive Approach for Solving Discrete Multiple Criteria Problems, IEEE Trans on Systems, Man and Cybernetics, Vol. 18, No. 2, pp. 273–285, 1988.

[20] Malakooti, B., Some Theories and an Exact Interactive

Approach for Solving Discrete Multiple Criteria Problems: Trade-Offs and Paired Comparisons, forthcoming in IEEE Systems, Man, and Cybernetics, Vol. 19, 1989.

[21] Malakooti, B. and A. Ravindran, Interactive Paired Comparison Methods for MOLP Problems with Underlying Linear Utility Functions, Ann. Oper. Res., Vol. 5, pp. 575–597, 1986. Application to Dam Control Problem (Optimal Control), Trans. Inst. Electron. and Commun. Eng. Jpn. Sect. E. (Japan), Vol. E62, No. 11, 741–8, Nov. 1979.

[22] Murahlidhar, K.H., and M.K. Sundareshan, A Hierarchical Scheme for Multi-objective Adaptive Routing in Large Communication Networks, Proceedings of the 21st IEEE Conference on Decision and Control, 834–5, 1982.

[23] Murahlidhar, K.H., and M.K. Sundareshan, Adaptive Routing and Flow Control in Large Communication Network: A Hierarchical Scheme for Multi-objective Optimization, Proceedings of the IEEE INFOCOM '84, 299–308, 1984.

[24] Masuda, T., and K. Fuji, Multi-objective Optimization Method.

[25] Ng, W.-Y., A Decision Support System for Multi-Objective Design of Practical Controllers. Proceedings of the 1988 American Control Conference, pp. 713–718, Vol. 1, June 15–17, 1988, Altanta, GA.

[26] Nishikawa, Y., J. Nomura, K. Sawada and H. Takada, Multi-objective Optimization of Ordering Point Decision in Inventory Management by Use of Utility Theory, (H. Akashi, editor), Control Science and Technology for the Progress of Society, Proceedings of the Eighth Triennial World Congress of the International Federation of Automatic Control, 1533–8, Vol. 2, 1982.

[27] Nishikawa, Y., J. Nomura, T. Inaki, J. Hasizume, and K. Sawada, Multi-objective Assessment of Investment Plans By Use Of Utility Theory, Control Science and Technology for the Progress of Society, Proceedings of the Eighth Triennial World Congress of the International Federation of Automatic Control, 1539–44, Vol. 2, 1982.

[28] Norbis, M., and S. MacGregor, Multiobjective, Multi-Level Heuristic for Dynamic Resource Constrained Scheduling Problems, European Journal of Operations Research, Vol. 33, No. 1, Jan 1988, pp. 30–41.

[29] Osternark, R. and H. Salmela, Connecting Expert Systems Features to a Multiple Criteria Programming Decision Support System, Comput. Sci. Econ. Manage., Vol. 1, No. 3, 175–88, 1988.

[30] Padberg, M., and G. Rinaldi, Branch-and-Cut Approach to a Variant of the Traveling Salesman Problem, Journal of Guidance, Control, and Dynamics, Vol. 11, No. 5, September–October 1988, pp. 436–440.

[31] Payne, A. N., Control System Design by Multi-objective Optimization, Proceedings of the 21st IEEE Conference on Decision and Control, 546–7, Vol. 2, 1982.

[32] Pearl, J., Heuristics: Intelligent Search Strategies for Computer Problem Solving, Addison Wesley, 1984.

[33] Rajurkar, K.P., V.V. Navelkar, and Y. Kamelian, Application of Multi-Objective Optimization Techniques to Manufacturing Systems, Proceedings of the 1987 IEEE Conference on Systems, Man, and Cybernetics, pp. 513–516, Alexandria, VA, 1987.

[34] Sadagapan, S. and A. Ravindran, Multicriteria Mathe-

matical Programming - A Unified Interactive Approach, Eur. Oper. Res., Vol. 25, No. 2, pp. 947-957, 1986.

[35] Sakawa, M., R. Narutaki, K. Sawada, Y. Sawaragi, Multi-objective Optimization in Water Resources Problems of Kakogana River Basin, (Y. Sawaragi and H. Akashi, editors), Environmental Systems Planning, Design and control, 255–62, 1978.

[36] Sakawa, M., and F. Seo, Interactive Multi-objective Decision Making by the Sequential Proxy Optimization Technique (SPOT) and its Application to Environmental Systems, (H. Akashi, editor), Control Science and Technology for the Progress of Society, Proceedings of the Eighth Triennial World Congress of the International Federation of Automatic Control, 1527–32, Vol. 2, 1982.

[37] Sawaragi, Y., H. Nakayama, and T. Tanino, Theory of Multiobjective Optimization, Academic Press, 1985.

[38] Sterling, L. and R. Beer, Metaintrepreters for Expert System Construction, J. Logic Programming, 1989, 163–178.

[39] Steuer, R.E., An Interactive Multiple Objective Linear Programming Procedure, in M.K. Starr and M. Zeleny, Eds. Multiple Criteria Decision Making, New York: North-Holland, 1977, pp. 925–239.

[40] Steuer, R.E., Multiple Criteria Decision Making: Theory and Applications, New York: John Wiley, 1986.

[41] Stewart, T.. Interactive Multiple Objective Linear Programming Method Based on Piecewise-Linear Additive Value Functions, IEEE Transactions on Systems, Man, and Cybernetics, Vol. SMC-17, No. 5, 1987, pp. 799–805.

[42] Stewart, B. and C. White, Heuristic Search With Multiple Criteria and Additive Cost Structure, Proceedings of the 26th IEEE Conference on Decision and Control. Los Angeles, CA, December 1987, pp. 1078–1083.

[43] Tabak, D., A.A. Schy, D.P. Giesy, and K.G. Johnson, Aircraft Control Systems Design by Multi-objective Optimization, (H.W. Hale and A.N. Michel, editors) 21st Midwest Symposium on Circuits and Systems, 290–1. 14–15 Aug. 1978, Ames, IA, USA.

[44] Tabak, D., A.A. Schy, D.P. Giesy, and K.S. Johnson, Application of Multi-objective Optimization in Aircraft Control Systems Design, Automatica, Vol. 15, No. 4, 595–600, Sept. 1979.

[45] Talukdar, S.N., and R.L. Koo, Multi-objective Trajectory Optimization for Electric Trains, Joint Automatic Control Conference, 303–16, 1978.

[46] Toivonen, H.T., A Multi-objective Linear Quadratic Gaussian Control Problem, IEEE Trans. Autom. Control, Vol. AC-29, No. 3, 279–80, March 1984.

[47] Valtorta, M., A Result on the Computational Complexity of Heuristic Estimates for the A\* Algorithm. Information Sciences 34, 47–59, 1984.

[48] Wang, S. and Y. Lu, Knowledge-Based Multiobjective Nonlinear Optimization Method for Large Scale Systems, Proceedings of the 1987 IEEE Conference on Systems, Man. and Cybernetics, Alexandria, VA, October 1987, pp. 497–431.

[49] White, C., A. Sage, and S. Dozono, A Model of Multiattribute Decision Making and Trade-off Weight Determination Under Uncertainty, IEEE Trans. on Systems, Man, and Cybernetics, SMC-14, (Mar.-Apr. 1984), 223–229.

[50] White, D.J., Multiobjective Interactive Programming, J. Oper. Res. Soc., Vol. 31, pp. 517–523, 1980.

[51] Ku, L.D., A Fuzzy Multiobjective Programming Algorithm in Decision Support Systems, Ann. Oper. Res., Vol. 12, No. 1–4, 315–20, 1988.

[52] Yang, J.-B., C. Chen, and Z.-J. Zhang, The Interactive Step Trade-Off Method (ISTM) for Multiobjective Optimization, Proceedings of the IEEE International Symposium on Intelligent Control, pp. 408–14, 19–20 Jan. 1987, Philadelphia, PA.

[53] Zeleny, M.. Multiple Criteria Decision Making, McGraw-Hill, 1982.
