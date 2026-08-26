---
otero_id: 17179
otero_key: "3Y77DBJP"
title: "Abductive reasoning by constructing probabilistic deduction graphs for solving the diagnosis problem"
authors: "Han-Lin Li; Chao-Chih Yang"
year: "1991"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(91)90051-c"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Abductive reasoning by constructing probabilistic deduction graphs for solving the diagnosis problem

Han-Lin Li

Institute of Information Management, National Chiao-Tung University, Hsinchu, Taiwan, R.O.C.

Chao-Chih Yang

Department of Computer Sciences, University of North Texas, Denton, Texas, USA

An algorithm is proposed for finding optimal solutions of the diagnosis problem by using deduction graphs (DG) to accomplish abductions of multiple causes and multiple symptoms. The relationship among causes, symptoms, and possible intermediaries is represented by a causal network. The algorithm accomplishes the abduction by constructing a deduction graph DG(C, S) from the cause set C to the symptom set S representing the subnetwork such that the product of the prior probability, P(C), of C and the conditional probability, P(S|C), of DG(C, S) is maximized. An optimal solution is achieved by solving a 0/1 linear integer programming problem. Based on some assumptions, the algorithm can deal with a causal network involving various mutually independent deduction graphs.

Keywords: Abduction, Causal network, Deduction, Deduction graph, Diagnosis, Expert system, Integer programming, Mutually independent or exclusive, Optimization, Probabilistic reasoning.

## 1. Introduction

There are two kinds of probabilistic reasoning: abduction and deduction. Deduction is a logical inference from the hypothesis to deduce the evidence where the hypothesis and the evidence both involve probabilities to indicate their truth values in the general case of quantitative logic. In the special case of qualitative logic where truth values are limited to true and false, if in the hypothesis “if A then B” and “A” are both true, then “B”

![](/api/attachments/3Y77DBJP/fulltext/images/9e0a171ab53b0272fa20c9d9bf111c8035724446a8a630a74cddc1df1b8039cd.jpg)

Han-lin Li is a professor in the Institute of Information Management, National Chiao-Tung University, Taiwan, R.O.C. He received the Ph.D. degree from the University of Pennsylvania, U.S.A. in 1983. In his research, Dr. Li investigates Information management systems with applications, such as decision support systems, and urban information systems. Currently, his main interest is in the areas of integrating learning and reasoning concepts into the framework of

decision support systems.  
![](/api/attachments/3Y77DBJP/fulltext/images/f8e5b4a0d4887d7b9eb6e1a277f614cfb68fd637fd169e3a323e4e855785fcd0.jpg)

Chao-Chih Yang received the B.S. degree from the Chinese Naval College of Technology in 1953, the M.S. degree from the National Chiao Tung University in 1962, and the M.S. and Ph.D. degrees from Northwestern University, Evanston, IL, in 1964 and 1966, respectively. Since 1985, he has been a Professor in the Department of Computer Sciences, North Texas State University (now University of North Texas), Denton. He was a faculty member at the University of Alabama

at Birmingham from 1972 to 1985, at the National Chiao Tung University from 1967 to 1971, and at the Washington State University from 1966 to 1967. His present research interests are in the areas of databases, expert systems, and artificial intelligence. He has published numerous research articles and is the author of Relational Databases (Englewood Cliffs, NJ: Prentice-Hall, 1986). Dr. Yang is a member of the IEEE Computer Society and the Association for Computing Machinery.

being true is correctly deduced. On the other hand, abduction is the generation of hypothetical explanations for what we see. In the special case of qualitative logic, if in the hypothesis “if A then B” and “B” are both true, then “A” being true and “A” being false are both possibly abducted where the former is favorably adopted as a hypothetical explanation for what we see. Since abductive reasoning in the general case of quantitative logic is of particular importance in solving diagnosis problems, this paper concentrates on solving the abductive reasoning problem.

Several expert systems have been developed for solving the probabilistic diagnosis problem. Based on the search and inference strategies used, those expert systems can be classified as follows. MYCIN [2], PROSPECTOR [3], GERTIS [21], GADICEUS [14], and the Pearl's method [13] use, respectively, the forward-chaining technique, the backward-chaining mechanism [15], the Dempster-Shafer theory, heuristics, and the Markov and Bayesian networks. The time complexities of MYCIN and PROSPECTOR are both exponential when multiple causes and multiple symptoms are involved, and they become worse when a causal network has intermediaries. GERTIS allows imprecise specifications of symptoms to derive a possible set of relevant causes. However, both of these systems can only solve the diagnosis problem in which its causal network is degenerated to a mutually exclusive and exhaustive tree [5,16,23]. The heuristics used in CADICEUS [14] try to partition the set of diseases into groups and then to decide which group can best fit the given symptom-set. Although CADICEUS can deal with multiple diseases and multiple symptoms, its search process is difficult to converge for yielding an optimal solution. The Markov and Bayesian networks used in the Pearl's method [13] allow explicit representation of the dependencies of multiple causes in a causal network. This approach manipulates a full joining probability distribution and avoids the usual assumption of probability independence [6]. Applying the Pearl's method for solving the diagnosis problem essentially requires that an original causal network can be converted into a tree or a polytree by a hierarchical clustering method [13]. However, such a clustering method may convert one original network into various trees of polytrees from which it is difficult to choose one for solving the diagnosis problem.

In addition it is difficult to convert some causal network into a hierarchical cluster of a limited size. This limits the application domain of the Pearl's method.

For removing the above deficiencies, we propose a new method, based on the construction of deduction graphs (DG) for solving the diagnosis problem. The proposed algorithm accomplishes the abduction by constructing a DG from the source C to the sink S, denoted as DG(C, S), representing the sub-network such that the product of the prior probability, P(C), of C and the probability, P(DG(C, S)), of DG(C, S) is maximized.

The proposed method has a number of advantages. First, it can effectively solve the diagnosis problem involving multiple causes and multiple symptoms with possible intermediaries. Second, it can deal with a causal network of any type, such as a bipartite graph, a tree, a polytree, etc. Third, it can find an optimal solution, i.e., the most probable set of causes is abducted.

This paper is organized as follows. Section 2 briefly reviews some relevant terminology of the diagnosis problem and deduction graphs. Section 3 introduces various types of message propagation, basic assumptions, and probabilistic deduction graphs. Section 4 proposes an algorithm with several illustrations. The last section covers conclusions and discussions.

## 2. Preliminaries

## 2.1. Deduction Graphs

The initial concept of deduction graphs (DG), which only concerns about deterministic cases, was reported in $[18,19,20]$ . This section extends the concept of DG from deterministic cases to probabilistic cases as follows: Let R be a set of rules or headed Horn clauses (HC), denoted as

$$
\mathrm{R} = \left\{\mathrm{R} _ {1}, \dots , \mathrm{R} _ {\mathrm{r}} \right\}.\tag{2.1}
$$

Each $R_{i}(i=1,\ldots,r)$ is an HC referred to as a rule and represented as

$$
\mathrm{R} _ {\mathrm{i}}: \mathrm{b} _ {\mathrm{i} 1}, \dots , \mathrm{b} _ {\mathrm{im}} \xrightarrow {\mathrm{f} _ {\mathrm{i}}} \mathrm{h} _ {\mathrm{j}},\tag{2.2}
$$

where $b_{i1}$ through $b_{im}$ are predicates conjuncted to compose the body or condition of $R_{i}$ , and $h_{i}$ is a predicate to form the head or conclusion of $R_{i}$ ; “→” stand for “implies;” and $f_{i}$ is the conditional probability of $h_{i}$ given $b_{i1}\ldots b_{im}$ , i.e.,

$$
\mathrm{P} \left(\mathrm{h} _ {\mathrm{i}} \mid \mathrm{b} _ {\mathrm{i} 1} \dots \mathrm{b} _ {\mathrm{im}}\right) = \mathrm{f} _ {\mathrm{i}} \quad \text { for } 0 <   \mathrm{f} _ {\mathrm{i}} <   1.\tag{2.3}
$$

For a starting node, source, and an ending node, sink, the problem of inferring a formula of the form

$$
\mathrm{G}: \text { source } \xrightarrow {\mathrm{f}} \text { sink }\tag{2.4}
$$

is solved by constructing a $DG_{k}$ (source, sink) with a probability $P(DG_{k}(source, sink)) = f$ where $0 < f \leq 1$ and either the source or the sink is unknown and being found by an algorithm. The construction of a $DG_{k}(source, sink)$ is accomplished by selecting a subset $R'$ of R such that each rule of the form (2.2) in $R'$ builds the arc $((b_{i1}, \ldots, b_{im}), h_{i})$ and each predicate builds a node such that each path is incident from the source to the sink without forming a cycle in the DG. Then the conjunction of the rules in $R'$ infers the formula (2.4) if and only if the graphically structured set $R'$ forms a $DG_{k}$ (source, sink).

Various types of nodes and arcs in a $DG_{k}$ are discussed in the following:

(1) Simple node: A node composed of a single element or predicate is a simple node. For example, given a rule $R_{1}$ which infers predicate B from a predicate A; denoted as $R_{1}: A \rightarrow B$ in fig. 1(a). Both A and B are simple nodes.

(2) Compound node: A node composed of more than one element or predicate is a compound node. For example, given two trivial rules $R_{1}: A \& B \rightarrow A$ and $R_{2}: A \& B \rightarrow B$ in Fig. 1(b). Node A & B is a compound node.

(3) Full arc: A full arc corresponds to a rule. We use a solid line to represent a full arc. For example arc $R_{1}$ in fig. 1(a) is a full arc.

(4) Dotted arc: A dotted arc provides a connection between a compound node to the component node of the compound node. We use a dotted line to represent a dotted arc. For example, arcs $R_{1}$ and $R_{2}$ in fig. 1(b) are dotted arcs.

![](/api/attachments/3Y77DBJP/fulltext/images/925128c4d32e271c66876a4ae22b26bb60237019749a0be596d4f3a010e85c00.jpg)  
Fig. 1. Node and arc types.

(5) Entry node: An entry node is a node which does not have any arc indicent to it.

(6) Exit node: An exit node is a node without any arc indicent from it.

(7) Intermediate node: An intermediate node is a node which is neither an entry node nor an exit node.

(8) In-arc: An arc incident to a node is an in-arc of the node.

(9) Out-arc: An arc incident from a node is an out-arc of the node.

Based on these notations, the types of message propagation and the associated probability of a deduction graph will be discussed in section 3.

## 2.2. The Car Diagnosis Problem

Referring to $[1,13]$ , suppose a defective car has three common symptoms: difficult to start, engine overheats, and engine lacks power. Let ten causes (or hypotheses) of causing these three symptoms be denoted by C:

C = {battery weak, battery connections faulty, transmission not in park or neutral, ignition switch faulty, starter relay faulty, startjet faulty, mainjet faulty, carbweak (weak mix from faulty carb. adjustment), carbrich (richmix from faulty carb. adjustment), nvalue (faulty needle valve in float chamber).}

Suppose we want to find the most possible cause(C) of causing the observed symptom(S) based on a car diagnosis rule-base. Such a car diagnosis rule-base, as shown in Table 1, contains three kinds of information:

(1) The prior probabilities of all causes and symptoms.

(2) The conditional probabilities (i.e., posterior probabilities) of a symptom given the cause, and of an intermediary (i.e., pathological state) given the cause.

(3) The constraints among causes, symptoms or intermediaries.

By (a) of table 1, $(\mathrm{P}(\text{battery weak}) = 2^{-4}$ means that $2^{-4}$ of all cars have the cause called “battery weak”. By (1) of table 1, $P(\text{battery faulty} | \text{battery}$ weak) = $2^{-1}$ means that half of the cars having “battery weak” displays the symptom of “battery faulty”. By denoting the cardinality of set x as |x|, we define

$$
\begin{array}{l} \mathrm {P(battery weak) = \frac {|cars with battery weak|}{|all cars|}}, \\ \mathrm {P(battery faulty |battery weak) =} \\ \frac {| \text { car with battery faulty and battery weak } |}{| \text { car with battery weak } |}. \end{array}
$$

Constraint T1 of table 1 means that the causes “carbweak” and “carbrich” are mutually exclusive. That is, these two faulties will not simultaneously happen in a car. Table 1 can be alternatively represented by a causal network as shown in fig. 2.

In fig. 2, causes are denoted by $C_{1}$ through $C_{10}$ , intermediaries by $I_{1}$ through $I_{4}$ , and symptoms by $S_{1}$ through $S_{3}$ . Each $C_{i}$ for $i=1,\ldots,10$ is an entry node that has no in-arcs, each $S_{j}$ for $j=1,\ldots,3$ is an exit node that has no out-arcs, and each $I_{k}$ for $k=1,\ldots,4$ is an intermediate node that has at least one in-arc and at least one out-arc. Each entry node affects directly some exit nodes or indirectly some exit nodes via some intermediate nodes. Each intermediate node may affect some other intermediate nodes or exit nodes. Each arc from A to B, denoted by (A, B), indicates a relationship between A and B meaning “A causes B” with a conditional probability P(B|A). The logarithmic probability with base 2 of a node or an arc is indicated by a negative value enclosed by a pair of parentheses. From now on, causes, symptoms, and intermediaries are interchangeable with entry nodes, exit nodes, and intermediate nodes, respectively.

In Fig. 2, $I_{2}$ is a compound node with two components $C_{5}$ and $C_{6}$ . That means, $C_{5}$ and $C_{6}$ are jointed together to cause the intermediary $I_{2}$ . Two dotted arcs, in which the probabilities are $2^{0}$ , are used to link $I_{2}$ to $C_{5}$ and $C_{6}$ . The symbol “ $\langle m.e.\rangle$ ” [1] is used to denote the mutual exclusive relationships in $C_{8}-C_{9}$ and in $I_{3}-I_{4}$ , as referred to constraints $T_{1}$ and $T_{2}$ in table 1.

Let $\{C_1, \ldots, C_L\}$ , $\{S_1, \ldots, S_M\}$ , and $\{I_1, \ldots, I_N\}$ be the sets of causes, symptoms, and intermediaries of a given causal network, respectively. Let $C = \{C_{i_1} \ldots C_{i_x}\}$ and $S = \{S_{j_1} \ldots S_{j_y}\}$ be, respectively, a cause-set and a symptom-set, which

(-6.5)  
(-5)  
(-4)  
(-4)  
(-4)  
(-3)  
(-3)  
![](/api/attachments/3Y77DBJP/fulltext/images/7aada701077ef56afa8a43db9a76ed59091c2468009a42dd3c9a5778c176c46d.jpg)  
Fig. 2. A causal network of a car diagnosis system.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Table 1
A Car Diagnosis Rulebase.

1. Prior probabilities of causes:
(a) P(battery weak) $2^{-4}$
(b) P(battery connections faulty) = $2^{-4}$
(c) P(transmission not in park or neutral) = $2^{-6.5}$
(d) P(ignition switch faulty) = $2^{-4}$
(e) P(starter relay faulty) = $2^{-7}$
(f) P(startjet faulty) = $2^{-5}$
(g) P(mainjet faulty) = $2^{-10}$
(h) P(carbweak) = $2^{-4}$
(i) P(carbich) = $2^{-3}$
(j) P(nvalue) = $2^{-3}$
Prior probabilities of symptoms:
(h) P(diffstart) = $2^{-3}$
(i) P(overheats) = $2^{-2}$
(j) P(lackpower) = $2^{-4}$

2. Prior Probabilities:
(1) P(battery faulty | battery weak) = $2^{-1}$
(2) P(battery faulty | battery connections faulty) = $2^{-1.5}$
(3) P(diffstart | battery faulty) = $2^{0}$
(4) P(diffstart | transmission not in park or neutral) = $2^{0}$
(5) P(diffstart | ignition faulty) = $2^{-5}$
(6) P(diffstart | really-jet faulty) = $2^{-1.5}$
(7) P(diffstart | fuel weakmix) = $2^{-3}$
(8) P(fuel weakmix | startjet faulty) = $2^{-1}$
(9) P(fuel weakmix | mainjet faulty) = $2^{-1}$
(10) P(fuel weakmix | carbweak) = $2^{-2}$
(11) P(overheats | fuel weakmix) = $2^{-5}$
(12) P(lackpower | fuel weakmix) = $2^{-1.5}$
(13) P(fuel richmix | carbrich) = $2^{-2}$
(14) P(fuel richmix | nvalue) = $2^{-1}$
(15) P(lackpower | fuel richmix) = $2^{-1.5}$
(16) P(fuel weakmix | ignition faulty) = $2^{-3}$

3. Constraints:
T1: Carbweak and carbrich are mutually exclusive.
T2: Fuel weakmix and fuel richmix are mutually exclusive.
</div>

are, respectively, a subset of $\{C_{1},\ldots,C_{L}\}$ and a subset of $\{S_{1},\ldots,S_{M}\}$ . That is, C corresponds to a combination of x out of L causes for $1 \leq x < L$ and S a combination of y out of M symptoms for $1 \leq y \leq M$ . Each above set is alternatively represented by a conjunction of its elements, such as $C = C_{i_{1}} \& \ldots \& C_{i_{x}}$ where “&” stands for “conjunction” or “logical and”.

Along the line of abductive reasoning, the conditional probability of C given S, based on the Bayes' theorem, is

$$
\mathrm{P} (\mathrm{C} \mid \mathrm{S}) = \mathrm{P} (\mathrm{C}) \frac {\mathrm{P} (\mathrm{S} \mid \mathrm{C})}{\mathrm{P} (\mathrm{S})}.\tag{2.4a}
$$

By (2.4a), maximizing P(C | S) for some C is equivalent to maximizing

$$
\mathrm{P} (\mathrm{C}) \mathrm{P} (\mathrm{S} | \mathrm{C})\tag{2.4b}
$$

since P(S) in (2.4a) is independent from C. As will be seen in subsequent sections, the conditional probability P(S|C) is the probability of a DG(C, S) being constructed.

## 3. Message Propagation, Assumptions, and Deduction Graphs

## 3.1. Types of Message Propagation

There are three types of message propagation in a causal network: fork, serial, and parallel. These types are shown in fig. 3(a)–(c). In fig. 3, each node has a prior probability and each arc represents a rule of the form (2.2) with a conditional probability of the form (2.3). More specifically, fig. 3(a) has y + 1 nodes and y arcs where each arc represents a rule of the form $C_{i} \stackrel{f_{ak}}{\rightarrow} S_{j_{k}}$ with a probability $f_{ak} = P(S_{j_{k}} | C_{i})$ for $k = 1, \ldots, y$ . The subscripts a and k of $f_{ak}$ refer, respectively, to the $DG_{a}(C_{i}, S_{j_{1}} \& \ldots \& S_{j_{v}})$ of Fig. 3(a) and the kth arc in the $DG_{a}$ . Note that the sink of this DG is compound and represented by its components $S_{j_{1}}$ through $S_{j_{v}}$ .

## 3.2. Assumptions

Concerning those types of message propagation as shown in fig. 3, some assumptions made subsequently will achieve useful reduction in solving the diagnosis problem. Denote C, a subset of $C_{1}$ through $C_{L}$ , as

![](/api/attachments/3Y77DBJP/fulltext/images/077d1dce66a7d13df201261db44a918d0c7a557c1ef987007a51321e17d49a21.jpg)

![](/api/attachments/3Y77DBJP/fulltext/images/e4b5f20eb4ab22db22f2bb141d311729a861c36ff4ad540e256b2c1c61255e44.jpg)  
Fig. 3. Types of message propagation.

$$
\mathrm{C} = \mathrm{M} \left(\mathrm{C} _ {\mathrm{i} _ {1}} \dots \mathrm{C} _ {\mathrm{i} _ {\mathrm{g}}}\right) \& \mathrm{C} _ {\mathrm{i} _ {\mathrm{g} + 1}} \& \dots \& \mathrm{C} _ {\mathrm{i} _ {\mathrm{x}}},\tag{3.1a}
$$

where $M(C_{i_{1}} \ldots C_{i_{g}})$ denotes that $C_{i_{1}} \ldots C_{i_{g}}$ are mutually exclusive and $C_{i_{g+1}} \ldots C_{i_{x}}$ are mutually independent. Similarly denote S, a subset of $S_{1}$ through $S_{M}$ as

$$
\mathrm{S} = \mathrm{M} \left(\mathrm{S} _ {\mathrm{j} _ {1}} \dots \mathrm{S} _ {\mathrm{j} _ {\mathrm{r}}}\right) \& \mathrm{S} _ {\mathrm{j} _ {\mathrm{r} + 1}} \& \dots \& \mathrm{S} _ {\mathrm{j} _ {\mathrm{y}}},\tag{3.1b}
$$

where $M(S_{j_{1}} \ldots S_{j_{r}})$ denotes that $S_{j_{1}} \ldots S_{j_{r}}$ are mutually exclusive and $S_{j_{r+1}} \ldots S_{j_{y}}$ are mutually independent. Some assumptions are then formulated as follows.

Assumption 1. The compound probability of C in (3.1a) is characterized by

$$
\mathrm{P} (\mathrm{C}) = \left(\sum_ {\mathrm{d} = 1} ^ {\mathrm{g}} \theta_ {\mathrm{d}} \cdot \mathrm{P} \left(\mathrm{C} _ {\mathrm{i} _ {\mathrm{d}}}\right)\right) \cdot \prod_ {\mathrm{e} = \mathrm{g} + 1} ^ {\mathrm{x}} \mathrm{P} \left(\mathrm{C} _ {\mathrm{i} _ {\mathrm{e}}}\right),\tag{3.2a}
$$

where $\theta_{d}$ is a 0 or 1 value and $\Sigma_{d=1}^{g}\theta_{d}=1$ . “ $\Pi$ ” means product. Similarly, for S in (3.1b) we have

$$
\mathrm{P} (\mathrm{S}) = \left(\sum_ {\mathrm{d} = 1} ^ {\mathrm{r}} \lambda_ {\mathrm{d}} \cdot \mathrm{P} \left(\mathrm{S} _ {\mathrm{j} _ {\mathrm{e}}}\right)\right) \cdot \prod_ {\mathrm{e} = \mathrm{r} + 1} ^ {\mathrm{y}} \mathrm{P} \left(\mathrm{S} _ {\mathrm{j} _ {\mathrm{e}}}\right),\tag{3.2b}
$$

where $\lambda_{\mathrm{d}}$ is a 0 or 1 value and $\sum_{\mathrm{d} = 1}^{\mathrm{r}}\lambda_{\mathrm{d}} = 1$ .

Assumption 2. For the fork type of fig. 3(a) that corresponds to a $\mathrm{DG}_{\mathrm{a}}(\mathrm{C}_{\mathrm{i}}, \mathrm{S})$ for a simple node $C_{i}$ and a compound node S in (3.1b), based on (3.2b) we assume that

$$
\begin{array}{r l} \mathrm{P} (S | C _ {i}) & = \left(\sum_ {d = 1} ^ {r} \lambda_ {d} \cdot \mathrm{P} (S _ {j _ {d}} | C _ {i})\right) \prod_ {e = r + 1} ^ {y} \mathrm{P} (S _ {j _ {e}} | C _ {i}) \\ & = \left(\sum_ {d = 1} ^ {r} \lambda_ {d} \cdot f _ {a d}\right) \cdot f _ {a, r + 1} \dots f _ {a y}. \end{array} \tag {3.3}
$$

Assumption 3. For the serial type of fig. 3(c) that corresponds to a $\mathrm{DG}_{\mathrm{c}}(\mathrm{C}_{\mathrm{i}},\mathrm{S}_{\mathrm{j}})$ , we assume

$$
\begin{array}{r l} \mathrm {P(S_ {j} | C_ {i}) = P(S_ {j} | I_ {k})P(I_ {k} |C)} \\ & = f _ {c 1} \cdot f _ {c 2}. \end{array}\tag{3.4}
$$

A more general type of message propagation is parallel as shown in Fig. 3(d), where there are z paths from the source $C_{i}$ to the sink $S_{j}$ . If all of those paths are mutually exclusive and exhaustive, then by means of the Bayes' chain rule we have $\mathrm{P}(\mathrm{S}_{\mathrm{j}}|\mathrm{C}_{\mathrm{i}})=\mathrm{f}_{11}\;\mathrm{f}_{12}+\ldots+\mathrm{f}_{z1}\;\mathrm{f}_{z2}$ . However, unless a causal network is a pure hierarchical type as described in [21] which is rare in the real world, it is very difficult to examine whether all DGs in a causal network are mutually exclusive and exhaustive. For the purpose of simplicity, we assume that all DGs in a causal network are mutually independent, described as Assumption 5 below.

Assumption 4. For the parallel type of fig. 3(d), we assume all paths from the source $C_{i}$ to the sink $S_{j}$ are mutually independent. $P(S_{j}|C_{i})$ is then computed as

$$
\mathrm{P} \left(\mathrm{S} _ {\mathrm{j}} \mid \mathrm{C} _ {\mathrm{i}}\right) = \operatorname{MAX} \left\{\mathrm{f} _ {1 1} \mathrm{f} _ {1 2}, \dots , \mathrm{f} _ {\mathrm{z} 1}, \mathrm{f} _ {\mathrm{z} 2} \right\},\tag{3.5}
$$

Assumption 4 can be expanded into Assumption 5 below.

Assumption 5. For a cause-set C and a symptom-set S in a causal network, let $\{\mathrm{DG}_{1}(\mathrm{C},\mathrm{S}),\ldots ,\mathrm{DG}_{\mathrm{w}}$ (C, S)} be the set of DG(C, S)'s. Denote $\mathbf{P}(\mathbf{DG}_{\mathbf{h}}(\mathbf{C},\mathbf{S}))$ as the probability of $\mathrm{DG_H}(\mathrm{C},\mathrm{S})$ for $h = 1,\dots ,w$ , then

$$
\mathrm{P} (S \mid C) = \underset {h = 1} {\overset {w} {\operatorname{MAX}}} \left\{\mathrm{P} \left(\mathrm{DG} _ {h} (C, S)\right)\right).\tag{3.6}
$$

Example 1. Given a simple causal network in fig. 4, let $C = C_{1}$ & $C_{2}$ and $S = S_{1}$ & $S_{2}$ , then there are two $DG_{s}$ from C to S represented as

$$
\begin{array}{l} \mathrm{DG} _ {1} (\mathrm{C}, \mathrm{S}) \colon \mathrm{C} _ {1} \xrightarrow {\mathrm{f} _ {1}} \mathrm{A}, \mathrm{C} _ {2} \xrightarrow {\mathrm{f} _ {2}} \mathrm{A}, \mathrm{A} \xrightarrow {\mathrm{f} _ {3}} \mathrm{B}, \mathrm{B} \xrightarrow {\mathrm{f} _ {4}} \mathrm{S} _ {1}, \\ \mathrm{B} \xrightarrow {\mathrm{f} _ {5}} \mathrm{S} _ {2}. \end{array}
$$

$$
\mathrm{DG} _ {2} (\mathrm{C}, \mathrm{S}): \mathrm{C} _ {1} \xrightarrow {\mathrm{f} _ {1}} \mathrm{A}, \mathrm{A} \xrightarrow {\mathrm{f} _ {3}} \mathrm{B}, \mathrm{B} \xrightarrow {\mathrm{f} _ {4}} \mathrm{S} _ {1}, \mathrm{C} _ {2} \xrightarrow {\mathrm{f} _ {6}} \mathrm{S} _ {2}.
$$

Based on (3.6), P(S|C) is computed as

$$
\begin{array}{r l} \mathrm{P} (\mathrm{S} | \mathrm{C}) & = \operatorname{MAX} \left\{\mathrm{P} \left(\mathrm{DG} _ {1} (\mathrm{C}, \mathrm{S})\right), \mathrm{P} \left(\mathrm{DG} _ {2} (\mathrm{C}, \mathrm{S})\right) \right\} \\ & = \operatorname{MAX} \left\{\mathrm{f} _ {1} \mathrm{f} _ {2} \mathrm{f} _ {3} \mathrm{f} _ {4} \mathrm{f} _ {5}, \mathrm{f} _ {1} \mathrm{f} _ {3} \mathrm{f} _ {4} \mathrm{f} _ {6} \right\} \end{array}
$$

![](/api/attachments/3Y77DBJP/fulltext/images/a9fcb978bef872371ca6015f3de7c8b0da3efef74402e88f94ddebdaa4b6ad0c.jpg)  
Fig. 4. Computation of DG(C, S).

## 3.3. Construction of Deduction Graphs by Integer Programming

Based on the assumptions discussed above, a theorem concerning abductive reasoning is entailed in the following:

Theorem. Let $\{\mathrm{DG}_1(\mathbf{C},\mathbf{S}),\ldots ,\mathrm{DG}_{\mathrm{w}}(\mathbf{C},\mathbf{S})\}$ be the set of DG's from the source C to the sink S existed in a causal network. Denote $\mathrm{P}(\mathrm{DG}_{\mathrm{h}}(\mathbf{C},\mathbf{S}))$ as the probability of $\mathrm{DG}_{\mathrm{h}}(\mathbf{C},\mathbf{S})$ for $\mathrm{h} = 1,\dots ,\mathrm{w}$ , and $\mathbf{f}_{\mathrm{hk}}$ as the conditional probability of the $k^{\prime}$ th arc in $\mathrm{DG}_{\mathrm{h}}(\mathbf{C},\mathbf{S})$ for $\mathrm{k} = 1,\dots ,\mathrm{q(h)}$ where $\mathrm{q(h)}$ is the number of arcs in $\mathrm{DG}_{\mathrm{h}}(\mathbf{C},\mathbf{S})$ . Then (2.4b), (3.2a), (3.2b), (3.3), (3.4) and (3.6) imply

$$
\begin{array}{r l} \mathrm{P} (\mathrm{C} | \mathrm{S}) & = \left[ \left(\sum_ {\mathrm{d} = 1} ^ {\mathrm{g}} \theta_ {\mathrm{d}} \cdot \mathrm{P} \left(\mathrm{C} _ {\mathrm{i} _ {\mathrm{d}}}\right)\right) \cdot \prod_ {\mathrm{e} = \mathrm{g} + 1} ^ {\mathrm{x}} \mathrm{P} \left(\mathrm{C} _ {\mathrm{i} _ {\mathrm{e}}}\right) \right. \\ & \quad / \left(\sum_ {\mathrm{d} = 1} ^ {\mathrm{r}} \lambda_ {\mathrm{d}} \cdot \mathrm{P} \left(\mathrm{S} _ {\mathrm{jd}}\right) \cdot \prod_ {\mathrm{e} = \mathrm{r} + 1} ^ {\mathrm{y}} \mathrm{P} \left(\mathrm{S} _ {\mathrm{j} _ {\mathrm{e}}}\right) \right] \\ & \cdot \underset {\mathrm{r} = 1} {\text {MAX}} \left(\prod_ {\mathrm{k} = 1} ^ {\mathrm{q(h)}} \mathrm{f} _ {\mathrm{hk}}\right). \end{array}\tag{3.7}
$$

Note that $\Pi f_{hk}$ in (3.7) is the probability of $\mathrm{DG}_{h}(\mathbf{C},\mathbf{S})$ which is equal to $\mathbf{P}(\mathbf{S}|\mathbf{C})$ , i.e.,

$$
\begin{array}{r l} \mathrm{P} (\mathrm{S} | \mathrm{C}) & = \mathrm{P} \big (\mathrm{DG} _ {\mathrm{h}} (\mathrm{C}, \mathrm{S}) \big) = \prod_ {\mathrm{k} = 1} ^ {\mathrm{q} (\mathrm{h})} \mathrm{f} _ {\mathrm{hk}} \quad \text { for } \\ \mathrm{h} & = 1, \dots , \mathrm{w}. \end{array}\tag{3.8}
$$

For the convenience of computing (3,7), let $\log_{2}\mathrm{P}(\mathrm{C}|\mathrm{S})$ be denoted by $\mathrm{LP}(\mathrm{C}|\mathrm{S})$ and $\log_{2}f_{hk}$ by $Lf_{hk}$ then (3.8) is converted into

$$
\mathrm{LP} (\mathrm{S} \mid \mathrm{C}) = \mathrm{LP} \left(\mathrm{DG} _ {\mathrm{h}} (\mathrm{C}, \mathrm{S})\right) = \sum_ {\mathrm{k}} \mathrm{Lf} _ {\mathrm{hk}} \quad \text { for }
$$

$$
\mathrm{h} = 1, \dots , \mathrm{w}\tag{3.9}
$$

and (3.7) are converted into

$$
\begin{array}{r l} \mathrm{LP} (\mathrm{C} | \mathrm{S}) & = \log_ {2} \left(\sum \theta_ {\mathrm{d}} \cdot \mathrm{P} \left(\mathrm{C} _ {\mathrm{i} _ {\mathrm{d}}}\right)\right) \\ & - \log_ {2} \left(\sum \lambda_ {\mathrm{d}} \cdot \mathrm{P} \left(\mathrm{S} _ {\mathrm{j} _ {\mathrm{d}}}\right)\right) \\ & + \sum \mathrm{LP} (\mathrm{C} _ {\mathrm{i}}) - \sum \mathrm{LP} (\mathrm{S} _ {\mathrm{j}}) + \underset {\mathrm{h} = 1} {\overset {\mathrm{w}} {\operatorname * {M A X}}} \{\mathrm{LP} (\mathrm{S} | \mathrm{C}) \} \end{array}\tag{3.10}
$$

Now we formulate the problem for constructing a DG by using integer programming technique. For an arbitrary node A in a causal network, there are five types as shown in fig. 5. Fig. 5(a) shows that $A = I_{k}$ for some $k = 1, 2, \ldots, N$ is an intermediate node. Fig. 5(b) shows that $A = C_{i}$ for some $i = 1, \ldots, L$ is an entry node. Fig. 5(c) shows that $A = S_{j}$ for some $j = 1, 2, \ldots, M$ is an exit node.

![](/api/attachments/3Y77DBJP/fulltext/images/ffebbcb70e03c36ddc0820c7f1453dc50b08414554c0a9b2611b20901a5030c0.jpg)  
(d) $\mathbf{A}_{\mathrm{i}}$ is a compound node  
$A_{1}\cdots A_{d}$ are mutual exclusive  
Fig. 5. Intermediate, entry, and exit nodes.

Let $r_{A_1}$ through $r_{A_{m(A)}}$ be the in-arcs of node A, and $t_{A_1}$ through $t_{A_{n(A)}}$ be the out-arcs of node A in a causal network. Each in-arc $r_{A_g}$ of A for g in $\{1,\ldots,m(A)\}$ , each out-arc $t_{A_g}$ , of A for $g'$ in $\{1,\ldots,n(A)\}$ , and $u_A$ or $v_A$ are defined as 0/1 decision variables such that

(1) an in-arc $r_{A_{g}} = 1$ if it is in $\mathrm{DG}_{\mathrm{h}}(\mathrm{C}, \mathrm{S})$ and 0 otherwise when A is an intermediate or exit node;

(2) an out-arc $t_{A_{g}} = 1$ if it is in $\mathrm{DG}_{\mathrm{h}}(\mathrm{C}, \mathrm{S})$ and 0 otherwise when A is an entry or intermediate node;

(3) $\mathbf{u}_{\mathbf{A}} = 1$ if node A is in $\mathrm{DG}_{\mathrm{h}}(\mathbf{C},\mathbf{S})$ and 0 otherwise when A is an entry or exit node; and

(4) $v_{A}=1$ if node A is in $\mathrm{DG}_{h}(\mathrm{C},\mathrm{S})$ and 0 otherwise when A is an intermediate node.

When a causal network has L entry nodes, M exit nodes, and N intermediate nodes, the total number of nodes is $L + M + N$ . The total number, T, of arcs is equal to that of in-arcs or to that of out-arcs, i.e.,

$$
\mathrm{T} = \sum_ {\mathrm{A}} \mathrm{m(A)} = \sum_ {\mathrm{A}} \mathrm{n(A)}\tag{3.11}
$$

for each node A in $\{C_{1},\ldots,C_{L},S_{1},\ldots,S_{M},I_{1},\ldots,I_{N}\}$ were $m(A)=0$ if A is an entry node $\{i.e.,A=C_{i}$ for each $i=1,\ldots,L)$ and $n(A)=0$ if

A is an exit node (i.e., $A = S_{j}$ for each $j = 1, \ldots, M$ ). Thus, the left or the right SUM in (3.11) involves, respectively, only $M + N$ non-zero $m(A)'s$ or $L + N$ non-zero $n(A)'s$ .

We observe that if A is an intermediate node in $\mathrm{DG}_{\mathrm{h}}(\mathrm{C}, \mathrm{S})$ , then at least one of its in-arcs and also at least one of its out-arcs are in $\mathrm{DG}_{\mathrm{h}}(\mathrm{C}, \mathrm{S})$ . In addition, if A is an entry or exit node in $\mathrm{DG}_{\mathrm{h}}(\mathrm{C}, \mathrm{S})$ , then at least one of its out-arcs or in-arcs is in $\mathrm{DG}_{\mathrm{h}}(\mathrm{C}, \mathrm{S})$ , respectively. Hence, we have the following propositions.

Proposition 1. Referring to fig. 5(a) in which A is an intermediate node $I_{k}$ of a given causal network, if $I_{k}$ is in $\mathrm{DG}_{\mathrm{h}}(\mathrm{C},\mathrm{S})$ , then $v_{k}=1$ , meaning that node $I_{k}$ is selected for constructing $\mathrm{DG}_{\mathrm{h}}(\mathrm{C},\mathrm{S})$ , $\sum_{h=1}^{m(k)}r_{k_{h}}\geq1$ , indicating that at least one of the in-arcs of $I_{k}$ must be selected for constructing $\mathrm{DG}_{\mathrm{h}}(\mathrm{C},\mathrm{S})$ , and $\sum_{h=1}^{n(k)}t_{k_{h}}\geq1$ , denoting that at least one of the out-arcs of $I_{k}$ must be selected for constructing $\mathrm{DG}_{\mathrm{h}}(\mathrm{C},\mathrm{S})$ , and all equal to 0 otherwise for some $k=1,\ldots,N$ , where k abbreviates an intermediate node $I_{k}$ . This proposition can be converted into three linear constraints:

$$
\begin{array}{l} \text {(1)} \mathrm {v_ {k}} \leq \sum_ {\mathrm{h=1}} ^ {\mathrm{m(k)}} \mathrm {r_ {k_ {h}}}, \\ \text {(2)} \mathrm {v_ {k}} \leq \sum_ {\mathrm{h=1}} ^ {\mathrm{n(k)}} \mathrm {t_ {k_ {h}}}, \\ \text {(3)} (\mathrm{m(k)} + \mathrm{n(k)}) \mathrm {v_ {k}} \geq \sum_ {\mathrm{h=1}} ^ {\mathrm{m(k)}} \mathrm {r_ {k_ {h}}} + \sum_ {\mathrm{h=1}} ^ {\mathrm{n(k)}} \mathrm {t_ {k_ {h}}}. \end{array}
$$

Proposition 2. Referring to Fig. 5(b) in which A is an entry node $C_{i}$ of a given causal network, if $C_{i}$ is in a $\mathrm{DG}_{\mathrm{h}}(\mathrm{C}, \mathrm{S})$ , then $u_{i}=1$ and $\sum_{h=1}^{n(i)}t_{i_{h}}\geq1$ and both equal to 0 otherwise for some $i=1,\ldots,L$ where i abbreviates an entry node $C_{i}$ . In this case $m(i)=0$ for each cause $C_{i}, i=1,\ldots,L$ . This proposition is represented as

$$
u _ {1} \leq \sum_ {h = 1} ^ {n (i)} t _ {i _ {h}},\tag{1}
$$

$$
\mathrm{n} (\mathrm{i}) \mathrm{u} _ {\mathrm{i}} \geq \sum_ {\mathrm{h} = 1} ^ {\mathrm{n} (\mathrm{i})} \mathrm{t} _ {\mathrm{i} _ {\mathrm{h}}}.\tag{2}
$$

Proposition 3. Referring to fig. 5(c) in which A is an exit node $\mathbf{S}_{\mathrm{j}}$ of a given causal network, if $\mathbf{S}_{\mathrm{j}}$ is in a $\mathrm{DG}_{\mathrm{h}}(\mathrm{C},\mathrm{S})$ , then $\mathbf{u}_{\mathrm{j}} = 1$ and $\sum_{\mathrm{h} = 1}^{\mathrm{m(j)}}\mathbf{r}_{\mathrm{j_h}}\geq 1$ and both equal to 0 otherwise for some $j=1,\ldots,M$ where j abbreviates an exit node $S_{j}$ . In this case, $n(j)=0$ for each symptom $S_{j}, j=1,\ldots,M$ . Represented as

$$
\mathrm{u} _ {\mathrm{j}} \geq \sum_ {\mathrm{h} = 1} ^ {\mathrm{m} (\mathrm{j})} \mathrm{r} _ {\mathrm{j} _ {\mathrm{h}}},\tag{1}
$$

(2) $\mathfrak{m}(\mathrm{j})\mathfrak{u}(\mathrm{j})\geq \sum_{\mathrm{h} = 1}^{\mathrm{m}(\mathrm{j})}\mathfrak{r}_{\mathrm{j_h}}.$

Proposition 4. Referring to fig. 5(d) in which $\mathbf{A}_{\mathrm{i}}$ is a compound node with components $\mathbf{A}_1$ through $\mathbf{A}_{\mathrm{d}}$ , then we have following properties:

(1) If $\mathbf{A}_{\mathrm{i}}$ is in $\mathrm{DG}_{\mathrm{h}}(\mathrm{C},\mathrm{S})$ then $\mathbf{A}_1$ through $\mathbf{A}_{\mathrm{d}}$ are in the $\mathrm{DG}_{\mathrm{h}}(\mathrm{C},\mathrm{S})$ . That means, if $\mathbf{u}_{\mathrm{i}} = 1$ then $\mathbf{u}_1 = \mathbf{u}_2 = \ldots = \mathbf{u}_{\mathrm{d}} = 1$ , denoted as $\mathrm{du}_{\mathrm{i}} \leq \sum_{\mathrm{j} = 1}^{\mathrm{d}} \mathbf{u}_{\mathrm{j}}$ .

(2) If one of $\mathbf{A}_1$ through $\mathbf{A}_{\mathrm{d}}$ is not in $\mathrm{DG}_{\mathrm{h}}(\mathrm{C},\mathrm{S})$ , then $\mathbf{A}_{\mathrm{i}}$ is not in the $\mathrm{DG}_{\mathrm{h}}(\mathrm{C},\mathrm{S})$ . That means, if $\mathfrak{u}_1 = 0$ or... or $\mathfrak{u}_{\mathrm{d}} = 0$ then $\mathfrak{u}_{\mathrm{i}} = 0$ , denoted as $\mathfrak{u}_{\mathrm{j}} \geq \mathfrak{u}_{\mathrm{i}}, \mathrm{j} \in [1,\mathrm{d}]$ .

Proposition 5. Referring to fig. 5(e) in which nodes $A_{1}$ through $A_{d}$ are mutual exclusive, then at most one of $A_{1}$ through $A_{d}$ is in $\mathrm{DG}_{\mathrm{h}}(\mathrm{C}, \mathrm{S})$ , denoted as $\sum_{j=1}^{d} u_{j} \leq 1$ .

## 4. Proposed algorithm

The goal of solving the abductive reasoning problem is to maximize $\mathrm{LP}(\mathrm{C}|\mathrm{S})$ in (3.10) to find C. Since the term $\log_{2}(\Sigma\lambda_{\mathrm{d}}\cdot\mathrm{P}(\mathrm{S}_{\mathrm{j}_{\mathrm{d}}}))-\Sigma\mathrm{LP}(\mathrm{S}_{\mathrm{j}})$ in (3.10) is constant, to maximize $\mathrm{LP}(\mathrm{C}|\mathrm{S})$ is the same as to maximize the objective function OBJ defined as follows:

$$
\begin{array}{l} \mathrm{OBJ} = \log_ {2} \left(\sum_ {\mathrm{d} = 1} ^ {\mathrm{g}} \theta_ {\mathrm{d}} \cdot \mathrm{P} \left(\mathrm{C} _ {\mathrm{i} _ {\mathrm{d}}}\right)\right) + \sum_ {\mathrm{i} = \mathrm{g} + 1} ^ {\mathrm{x}} \mathrm{LP} \left(\mathrm{C} _ {\mathrm{i}}\right) \\ + \mathrm{LP} \left(\mathrm{DG} _ {\mathrm{h}} (\mathrm{C}, \mathrm{S})\right). \end{array} \tag {4}\tag{4.1a}
$$

The first two trems on the right side of (4.1) can be converted into (4.2a) and (4.2b) to fit integer programming, i.e.,

$$
\begin{array}{l} (1) \log_ {2} \left(\sum_ {\mathrm{d} = 1} ^ {\mathrm{g}} \theta_ {\mathrm{d}} \cdot \mathrm{P} \left(\mathrm{C} _ {\mathrm{i} _ {\mathrm{d}}}\right)\right) + \sum_ {\mathrm{i} = \mathrm{g} + 1} ^ {\mathrm{x}} \mathrm{LP} \left(\mathrm{C} _ {\mathrm{i}}\right) \\ = \sum_ {\mathrm{i} = 1} ^ {\mathrm{L}} \mathrm{u} _ {\mathrm{i}} \cdot \mathrm{LP} \left(\mathrm{C} _ {\mathrm{i}}\right), \end{array}\tag{4.2a}
$$

(2) $\sum_{\mathrm{d} = 1}^{\mathrm{g}}\mathbf{u}_{\mathrm{i_d}}\leqslant 1$ for a set of mutually exclusive

$$
\text { causes } \mathrm{C} _ {\mathrm{i} _ {1}}, \dots , \mathrm{C} _ {\mathrm{i} _ {\mathrm{g}}},\tag{4.2b}
$$

when $u_i = 1$ for each $C_i$ , $i = i_1, \ldots, i_x$ , and 0 otherwise (by Proposition 2).

Now we transform the right term $\mathrm{LP}(\mathrm{DG}_{\mathrm{h}}(\mathrm{C},\mathrm{S}))$ in (4.1a) as follows. Let all T arcs in a given causal network be denoted by positive integers 1 through T, such as 1 through 15 in fig. 2. Let $a_{g}$ for each arc g=1,...,T be a decision variable such that $a_{g}=1$ if g is an arc in $\mathrm{DG}_{\mathrm{h}}(\mathrm{C},\mathrm{S})$ for some h=1,...,w and 0 otherwise. Let $Lf_{g}$ be the logarithmic probability with base 2 of arc g for each g=1,...,T. Then (3.9) is converted into

$$
\mathrm{LP} (\mathrm{S} \mid \mathrm{C}) = \mathrm{LP} \left(\mathrm{DG} _ {\mathrm{h}} (\mathrm{C}, \mathrm{S})\right) = \sum_ {\mathrm{g} = 1} ^ {\mathrm{T}} a _ {\mathrm{g}} \mathrm{Lf} _ {\mathrm{g}} \quad \text { for }
$$

$$
\mathrm{h} = 1, \dots , \mathrm{w}.\tag{4.3}
$$

Substituting (4.2) and (4.3) into (4.1a) yields the goal of the abductive reasoning as

$$
\text { MAXmize   OBJ } = \sum_ {\mathrm{i} = 1} ^ {\mathrm{L}} \mathrm{u} _ {\mathrm{i}} \mathrm{LP} \left(\mathrm{C} _ {\mathrm{i}}\right) + \sum_ {\mathrm{g} = 1} ^ {\mathrm{T}} \mathrm{a} _ {\mathrm{g}} \mathrm{Lf} _ {\mathrm{g}},\tag{4.1b}
$$

where $\mathbf{u}_{\mathrm{i}}$ , $\mathrm{i} = 1, \ldots, \mathrm{L}$ satisfy (4.2b).

Algorithm:

Input: A causal network and y observed symptoms (S = S $_{j_1}$ & ... & S $_{j_y}$ ) are given.

Output: Sets of x causes $(\mathbf{C} = \mathbf{C}_{\mathrm{i}_{1}} \& \ldots \& \mathbf{C}_{\mathrm{i}_{x}})$ which causes S with the Eth maximal $\mathbf{P}(\mathbf{C}^{\mathrm{E}} | \mathbf{S})$ , the next maximal $\mathbf{P}(\mathbf{C}^{\mathrm{E}+1} | \mathbf{S})$ , etc, are being found where E stands for the Eth iteration.

Method: (Use OBJ of (4.1b) as the objective function)

Step 0: Initialize E := 0.

Step 1: {Solve the following 0/1 integer programming problem} Set E := E + 1. Maximize the objective function OBJ of (4.1b) subject to the following constraints to obtain the E'th optimal solution.

CT1: $\sum_{j=1}^{d} u_j \leq 1$ (if node $A_1$ through $A_d$ are mutual exclusive).

CT2: $\mathrm{eu}_{\mathrm{i}} \leq \sum_{j=1}^{\mathrm{e}} \mathrm{u}_{\mathrm{j}}$ (if node $\mathbf{A}_{\mathrm{i}}$ is a compound node with components $\mathbf{A}_{1}$ through $\mathbf{A}_{\mathrm{e}}$ ).

CT3: $u_{j} \geq u_{i}, j \in [1, e]$ (if node $A_{i}$ is a compound node with components $A_{1}$ through $A_{c}$ ).

CT4: $\sum_{i=1}^{L}u_{i}=x$ (x out of L causes are being found).

CT5: $u_{i} \leq \sum_{i=1}^{n(i)} t_{i_h}$ for each cause $C_i, i = 1, \ldots, L$ .

CT6: $n(i)u_{i} \geq \sum_{h=1}^{n(i)} t_{i_{h}}$ for each cause $C_{i}, i = 1, \ldots, L$ .

CT7: $v_{k} \leq \sum_{h=1}^{m(k)} r_{k_{h}}$ for each intermediary $I_{k}, k = 1, \ldots, N$ .

CT8: $v_{k} \leq \sum_{h=1}^{n(k)} t_{k_{h}}$ for each intermediary $I_{k}$ , k = 1, $\ldots$ , N.

CT9: $(\mathrm{m}(\mathbf{k}) + \mathrm{n}(\mathbf{k}))\mathrm{v}_{\mathrm{k}}\geq \sum_{\mathrm{h} = 1}^{\mathrm{m}(\mathrm{k})}\mathrm{r}_{\mathrm{k_h}} + \sum_{\mathrm{h} = 1}^{\mathrm{n}(\mathrm{k})}\mathrm{t}_{\mathrm{k_h}}$ for each intermediary $\mathrm{I_k,k = 1,\dots,N}$

CT10: $\sum_{h=1}^{m(j)} r_{j_h} \geq 1$ for each observed symptom $S_j$ , $j = j_1, \ldots, j_v$ .

CT11: $\sum_{h=1}^{m(j)} r_{j_h} = 0$ for each symptom $S_j$ not observed, $j$ in $\{1, \ldots, M\} - \{j_1, \ldots, j_v\}$ .

CT12: All decision variables u's, v's, r's, and t's are 0/1 integers.

Denote the Eth optimal solution by $C^E = C_{i_1}$ & ... & $C_{i_x}, u^E, v^E, r^E, t^E$ , and

$$
\mathrm{LP} \left(\mathrm{C} ^ {\mathrm{E}} | \mathrm{S}\right) = \mathrm{OBJ} - \sum_ {\mathrm{j} = \mathrm{j} _ {1}} ^ {\mathrm{j} _ {\mathrm{y}}} \mathrm{LP} \left(\mathrm{S} _ {\mathrm{j}}\right)
$$

which is based on (3.10). If only one solution is needed, then terminate the algorithm.

The objective function (4.1b) and constraints CT1 to CT12 form a 0/1 linear integer programming problem which can be solved by a commercialized IBM integer programming package [10].

Step 2: {Find the next optimal solution.} Repeat Step 1 with the following additional constraint:

$$
\mathrm{CT13:} \sum_ {i = 1} ^ {\mathrm{L}} \left(u _ {i} - u _ {i} ^ {\mathrm{E}}\right) \neq 0.
$$

If no more solutions are needed, then terminate the algorithm.

Step 3: Repeat Steps 1 and 2 to find other optimal solutions until obtains enough information. Then terminate the algorithm.

The rest of this section will use some examples to demonstrate the operation of the proposed algorithm.

Example 1. Given $S = S_{1}$ & $S_{2}$ as shown in fig. 2, find the first two causes that cause S with the first two maximal $\mathrm{LP}(\mathrm{C}^{1} | \mathrm{S})$ and $\mathrm{LP}(\mathrm{C}^{2} | \mathrm{S})$ . The related linear integer programming problem is formulated as follows:

$$
\underset {u _ {i}, a _ {g}} {\text { MAX   OBJ }} = \sum_ {i = 1} ^ {1 0} u _ {i} \mathrm{LP} (C _ {i}) + \sum_ {g = 1} ^ {1 6} a _ {g} \mathrm{Lf} _ {g}
$$

subject to

CT1: $u_8 + u_9 \leq 1, v_3 + v_4 \leq 1.$

CT2: $2\mathrm{v}_2\leq \mathrm{u}_5 + \mathrm{u}_6.$

CT3: $u_{5} \geq v_{2}, u_{6} \geq v_{2}.$

CT4: $\sum_{i=1}^{10} u_i = 1$ (only one out of 10 causes is being found).

$$
\begin{array}{l l} \text {CT5, CT6:} & u _ {1} = a _ {1} \quad u _ {2} = a _ {2} \\ & u _ {3} = a _ {4} \quad u _ {4} \leq a _ {5} + a _ {1 6}, 2 u _ {4} \geq a _ {5} + \\ & \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \end{array}
$$

CT7: $v_{1} \leq a_{1} + a_{2}$ (for all in-arcs of $I_{1}$ in case $I_{1}$ is being selected)

$$
\mathbf {v} _ {3} \leq \mathbf {a} _ {8} + \mathbf {a} _ {9} + \mathbf {a} _ {1 0} + \mathbf {a} _ {1 6}
$$

CT8: $v_{1} \leq a_{3}$ (for all out-arcs of $I_{1}$ in case $I_{1}$ is being selected)

$$
\begin{array}{l} \mathrm{v} _ {2} \leq \mathrm{a} _ {6} \\ \mathrm{v} _ {3} \leq \mathrm{a} _ {7} + \mathrm{a} _ {1 1} + \mathrm{a} _ {1 2} \\ \mathrm{v} _ {4} \leq \mathrm{a} _ {1 5} \end{array}
$$

CT9: $3\mathrm{v}_{1} \geq \mathrm{a}_{1} + \mathrm{a}_{2} + \mathrm{a}_{3}$ (for all arcs of $\mathbf{I}_1$ in case $\mathbf{I}_1$ is not being selected)

$$
\begin{array}{l} \mathrm {v_ {2}} \geq \mathrm {a_ {6}} \\ 7 \mathrm {v_ {3}} \geq \mathrm {a_ {7}} + \mathrm {a_ {8}} + \mathrm {a_ {9}} + \mathrm {a_ {10}} + \mathrm {a_ {11}} + \mathrm {a_ {12}} + \mathrm {a_ {16}} \\ 3 \mathrm {v_ {4}} \geq \mathrm {a_ {13}} + \mathrm {a_ {14}} + \mathrm {a_ {15}}. \end{array}
$$

CT10: $a_{3} + a_{4} + a_{5} + a_{6} + a_{7} \geq 1$ (for all arcs of observed $\mathbf{S}_1$ ),

$a_{11}=1$ (for all arcs of observed $S_{2}$ ),

CT11: $a_{12} + a_{15} = 0$ (for all arcs of $S_3$ not observed).

CT12: $u_{1}$ to $u_{10}$ , $v_{1}$ to $v_{4}$ , $a_{1}$ to $a_{15}$ are 0/1 integers.

The execution of steps 0 and 1 finds the solution $u_8 = 1 \, a_7 = a_{10} = a_{11} = 1$ , which yield the first cause $C_8^1$ with maximal LP( $C_8^1 | S_1 \& S_2$ ) = -4 - 1 - 3 - .5 - (-3 - 2) = -3.5. The corresponding DG( $C_8^1, S_1 \& S_2$ ) is shown in fig. 6(a).

![](/api/attachments/3Y77DBJP/fulltext/images/959f1395d47703484f712aae027f5d54bf30087538756b4a209a846d61b1524f.jpg)  
Fig. 6. Abductive reasoning in Example 1 to 3.

Following step2, the new constraint CT13: $u_{8}=0$ ( $C_{8}$ is no longer be selected for the second solution) is added and then step 1 is repeated to find the next cause $C_{6}^{2}$ with (next to the first) maximal $\mathrm{LP}(C_{6}^{2}|S_{1}\&S_{2})=-4.5$ . The corresponding $\mathrm{DG}(C^{2},S_{1}\&S_{2})$ is shown in fig. 6(b).

Example 2. Given $S = S_{1}$ & $S_{2}$ , find a set of four causes $C = C_{i_{1}}$ & $C_{i_{2}}$ & $C_{i_{3}}$ & $C_{i_{4}}$ with the maximal LP(C |S). The integer programming formulation is identical to that of Example 1 except that CT4 is updated as:

$$
\mathrm{CT4:} \sum_ {\mathrm{i} = 1} ^ {1 0} \mathrm{u} _ {\mathrm{i}}
$$

$= 4$ (4 out of 10 causes are being found).

The optimal solution is $C = C_{1} \& C_{2} \& C_{4} \& C_{8}$ with the maximal $\mathrm{LP}(C|S_{1}\&S_{2}) = -15.5$ . The corresponding $\mathrm{DG}(C,S)$ is shown in fig. 6(c).

Example 3. Given $S = S_1 \& S_3$ to find a set of two causes $C = C_{i_1} \& C_{i_2}$ with the maximal LP(C, S). We update the constraints in Example 1 as

$$
\begin{array}{l} \text {CT4:} \sum_ {\mathrm{i} = 1} ^ {1 0} \mathbf {u} _ {\mathrm{i}} = 2 \\ \text {CT10:} \mathbf {a} _ {3} + \mathbf {a} _ {4} + \mathbf {a} _ {5} + \mathbf {a} _ {6} + \mathbf {a} _ {7} \geq 1 \\ \mathbf {a} _ {1 2} + \mathbf {a} _ {1 5} \geq 1 \\ \text {CT11:} \mathbf {a} _ {1 1} = 0 \end{array}
$$

The optimal solution is $C = C_{4} \& C_{10}$ with the maximal LP( $C_{4}$ & $C_{10}$ | $S_{1}$ & $S_{3}$ ) = -3. The corresponding DG( $C_{4}$ & $C_{10}$ ) is shown in fig. 6(d).

## 5. Conclusions and Discussions

This paper proposed an algorithm for solving the diagnosis problem by constructing probabilistic deduction graphs from a cause-set to a symptom set. Constructing a probabilistic deduction graph is accomplished by solving a 0-1 linear integer programming problem. This algorithm can not only deal with non-tree types causal networks but also find optimal solutions. However, the assumptions 4 and 5 about the message propagation may not always true for some diagnosis problems. It remains for further study to compute the probability of the causal subnetwork involving mixed mutually independent and exclusive deduction graphs.

## References

[1] A. Blake, Probabilistic Inference By Linear Optimization, in A.G. Cohn and J.R. Thomas (eds.) Artificial Intelligence and Its Applications, John Wiley & Sons, 1986.

[2] B.G. Buchanan and E.H. Shortliffe, edited, Rule-Based Expert Systems: The MYCIN Experiments of the Stanford Heuristic Programming Project, Addison-Wesley, Reading, Mass. 1984.

[3] E. Charniak and D. McDermott, Introduction to Artificial Intelligence, Addison Wesley, Reading, Mass., 1987, 453–482.

[4] P. Cohen, J. Delisio, M. Greenberg, R. Kjeldsen, D. Suthers, and P. Berman, Management of Uncertainty in Medicine, International J. of Approximate Reasoning 1, 1 (1987) 103–116.

[5] J. Gordon and E.H. Shortliffe, A Method for Managing Evidential Reasoning in a Hierarchical Hypothesis Space, Artificial Intelligence 26, 3 (1985) 323–3357.

[6] D. Heckerman, Probabilistic Interpretations for MYCIN's Certainty Factors, in [8], 167–195.

[7] E. Horvitz and D. Heckerman, The Inconsistent Use of Measures of Certainty in Artificial Intelligence Research, in [8], 137–151.

[8] L.N. Kanal and J.F. Lemmer, edited, Uncertainty in Artificial Intelligence, North Holland, 1986.

[9] H.L. Li, Solve Multicreteria Decision Making Problems Based on Logic-based Decision Support Systems, Decision Support Systems Vol. 3, No. 2, 1987.

[10] B.A. Murtagh, Advanced Linear Programming: Computation and Practice, McGraw-Hill, New York, N.Y., 1981, 177–186.

[11] J. Pearl, Fusion, Propagation and Structuring in Belief Networks, Artificial Intelligence 29, 3 (1986) 241–288.

[12] J. Pearl. Embracing Causality in Formal Reasoning. Artificial Intelligence 35, 2 (1988) 259–271.

[13] J. Pearl, Probabilistic Reasoning in Intelligent Systems, Morgan-Kaufmann, San Mateo, CA, 1988.

[14] H. Pople, Heuristic Methods for Imposing Structured Problems: The Structuring Medical Diagnosis, in Artificial Intelligence in Medicine, P. Szolovits, edited, Westview Press, Colorado. 1982, 119–185.

[15] J.A. Robinson, A Machine-Oriented Logic Based on the Resolution Principle, J. of ACM 12 1 (1965) 23–41.

[16] G. Shafer and R. Logan, Implementing Dempster's Rule for Hierarchical Evidence, Artificial Intelligence 33, 3 (Nov. 1987) 271–298.

[17] H.A. Taha, Integer Programming, Academic Press, 1975, 116–119.

[18] C.C. Yang, A Polynomial Algorithm for Logically Deducting Horn Clauses and Processing Queries, International J. of Pattern Recognition and Artificial Intelligence 1, 1 (April 1987) 157–168.

[19] C.C. Yang, Deduction Graphs: An Algorithm and Applications, IEEE Trans. on Software Engineering 15, 1 (Jan. 1989) 60–67.

[20] C.C. Yang, J.Y. Chen, and H.L. Chau, Algorithms for Constructing Minimal Deduction Graphs, IEEE Trans. on Software Engineering 15, 6 (June 1989) 760–770.

[21] J. Yen, Gertis: a Dempster-Shafer Approach to Diagnosing Hierarchical Hypotheses, Comm. of ACM 32, 5 (1989) 573–585.
