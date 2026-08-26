---
otero_id: 17596
otero_key: "9F9CMYKX"
title: "Bayesian logic"
authors: "K.A. Andersen; J.N. Hooker"
year: "1994"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(94)90031-0"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Bayesian logic

K.A. Andersen

University of Århus, 8000 Århus C., Denmark

J.N. Hooker

Carnegie Mellon University, Pittsburgh, PA 15213, USA

We combine probabilistic logic and Bayesian networks to obtain the advantages of each in what we call Bayesian logic. Like probabilistic logic, it is a theoretically grounded way of representing and reasoning with uncertainty that uses only as much probabilistic information as one has, since it permits one to specify probabilities as intervals rather than precise values. Like Bayesian networks, it can capture conditional independence relations, which are probably our richest source of probabilistic knowledge. The inference problem in Bayesian logic can be solved as a nonlinear program (which becomes a linear program in ordinary probabilistic logic). We show that Benders decomposition, applied to the nonlinear program, allows one to use the same column generation methods in Bayesian logic that are now being used to solve inference problems in probabilistic logic. We also show that if the independence conditions are properly represented, the number of nonlinear constraints grows only linearly with the number of nodes in a large class of networks (rather than exponentially, as in the general case).

Keywords: Probabilistic logic; Bayesian networks.

![](/api/attachments/9F9CMYKX/fulltext/images/1b94ffe41c198cd4ab6bda3a6d15616ac7bac573ae83ae0ee8dacf95df1fd0a5.jpg)

John N. Hooker is associate professor of industrial administration at the Graduate School of Industrial Administration, Carnegie Mellon University. He received an A.B. in mathematics from Princeton University in 1971, a Ph.D. in philosophy from Vanderbilt University in 1974, and a Ph.D. in management science from the University of Tennessee in 1984. His research interests lie in the application of optimization methods to inference problems, as well as in trans-

portation and other areas of operations research.

![](/api/attachments/9F9CMYKX/fulltext/images/7cbb5bc7c63c19d1fc99d606f72050eb7b3fd222e8f666b0e4a7705ce75f6bdd.jpg)

Kim Allan Andersen is an assistant professor at the Mathematical institute at Aarhus University. He received a masters degree in mathematics and economics from Aarhus University in 1984 and a Ph.D. in operations research from Aarhus University in 1990. His research interests lie in the application of mathematical programming to logical problems as well as integer programming.

Correspondence to: K.A. Andersen, Operations Research, Building 530, Ny Munkegade, University of Århus, 8000 Århus C., Denmark.

## Introduction

It is well known that in the nineteenth century, George Boole developed a system of propositional logic that permits one to draw inferences by calculation. But it is not so well known that he understood the importance of capturing uncertainty in logic. To do so he invented probabilistic logic, in which he assigned formulas continuous probability values rather than simply one or zero to indicate true or false [3,4]. Boole's probabilistic logic is of the highest relevance today, since it provides a basis for dealing with uncertainty in knowledge-based systems that is not only well grounded theoretically but has some practical advantages as well.

The fundamental problem of probabilistic inference is to determine the probability of a conclusion that is inferred from uncertain premises. In his careful study of Boole's work [16,18], T. Hailperin pointed out that this problem can be naturally captured in a linear programming model, which Boole himself all but formulated. About a decade later N. Nilsson reinvented probabilistic logic and its linear programming formulation [29], and his paper sparked considerable interest in the artificial intelligence community [6,9,14,15,27,31]. Hailperin provides a historical survey of probabilistic logic in [17].

The linear programming formulation permits one to calculate an interval within which the probability of an inference lies, rather than an exact probability. But unlike the confidence factors that are popular in expert systems, these probability ranges are derived systematically from a general probability model rather than from an ad hoc formula $[32]$ . Probabilistic logic also has the practical advantage that, unlike Bayesian inference, one need not specify a full array of prior and conditional probabilities in order to calculate the probability of an inferred proposition. One need only specify as many or as few probabilities as he knows, and even these may be intervals rather than exact values.

Probabilistic logic is similar to Bayesian models, however, in that it can pose a substantial computational challenge. In particular, the number of variables in the linear programming model tends to increase exponentially with the number of atomic propositions in the knowledge base. But there is a well-known technique in linear programming, known as column generation, for dealing with just this type of difficulty, and promising computational results have already been obtained by several investigators $[5,21,24,25]$ .

A serious weakness of probabilistic logic, however, is that it omits what is probably our richest source of probabilistic knowledge: the independence of events. It may be very hard to quantify the probability that the winter will be cold or that an earthquake will strike California, but it is fairly certain that the occurrence of one has no effect on the probability of the other. In fact we can understand the world only if we assume that most events are significantly influenced by relatively few events, and this assumption should be reflected in a knowledge base. But such independence assumptions cannot be added to probabilistic logic without destroying the linearity of its linear programming model.

Perhaps the best known framework for dealing with independence is a Bayesian network $[33,30]$ , in which nodes can represent propositions and directed arcs (arrows) represent dependence (if decision nodes are added, the result is an influence diagram $[23,34,30]$ ). The network is a natural device for encoding complex conditional independence relations; that is, which propositions are independent once the truth values of certain other propositions are fixed. Unfortunately, posterior probabilities cannot be calculated until a large number of prior and conditional probabilities are specified. This number grows exponentially with the maximum number of immediate predecessors of a node, and the task of supplying probabilities can eclipse even the computational task of solving the resulting network.

In short, probabilistic logic has flexible input requirements but cannot account for independence, whereas Bayesian networks represent complex independence relations but make heavy and inflexible input demands. We propose to merge probabilistic logic and Bayesian networks so as to obtain the best of both worlds, and to solve the inference problem by solving a mathematical program. We call the result of the merger

Bayesian logic. From Bayesian networks it inherits the advantage that:

\- it captures conditional independence relations among propositions in a natural way.
From probabilistic logic it inherits the following advantages.

\- There is no need to give a complete specification of prior and conditional probabilities, as one must do in traditional Bayesian networks. One need supply only as much probabilistic information as he has.

\- Network nodes can correspond to molecular as well as to atomic propositions (This can be done awkwardly in traditional Bayesian networks by adding additional nodes and appropriate conditional distributions, and only then by making possibly unwarranted independence assumptions).

\- Not every proposition need appear as a node of the network. This is useful when one has no knowledge of how or whether a proposition depends on others.

\- The problem of inferring a range of probabilities can be formulated and solved as a mathematical program (in particular, a nonlinear program).

\- The sensitivity analysis available with nonlinear programming models can provide valuable information, such as the degree to which a change in an assigned probability can affect the solution.

As in ordinary probabilistic logic, the number of variables in the mathematical programming formulation can grow exponentially with the number of atomic propositions. Also if the problem is formulated naively, the number of nonlinear constraints required to capture independence relations can grow exponentially with the number of nodes in the network. But we will propose solutions to both problems. We will show that Benders' decomposition can be applied to the nonlinear program in such a way that the column generation techniques used in ordinary probabilistic logic can be used here as well. We will also show that if properly formulated, the number of independence constraints grows only linearly with the number of nodes for a large class of networks. To obtain this result we exploit the fact that the desired probabilistic inference can be drawn without computing a complete underlying joint probability distribution for the atomic propositions.

Specifically, we show that the number of nonlinear constraints grows exponentially, not with the size of the entire network, but with the size of the largest “extended ancestral set” in the network. When the size of this set is bounded, the number of constraints grows linearly with the number of nodes.

To have an approximate understanding of this claim, we can imagine that the nodes of a Bayesian network are people, and the immediate predecessors of a node are that person's parents. (We assume a person can have more than two parents). Beginning with any person in the network, we group his parents so that no parent in one group has a common ancestor with anyone in another. We do the same with his grandparents, and so on with earlier generations. The resulting groups are “ancestral sets”. An ancestral set joined by all the parents of its members is an “extended ancestral set”. If all the extended ancestral sets are small, the problem is relatively easy to solve.

We should point out that the computational problem has never been satisfactorily solved even for traditional Bayesian networks, aside from “singly connected” networks and perhaps a larger class of networks defined by Lauritzen and Spiegelhalter [26]. Singly connected networks are those with at most one directed path connecting any two nodes. Since the ancestral sets of a singly connected network are single nodes, singly connected networks (with bounded in-degree) form only a small subclass of the networks for which the number of constraints grows linearly (the in-degree of a node is the number of its immediate predecessors). Thus our nonlinear model offers a new approach to solving many traditional Bayesian networks that are not singly connected.

The Lauritzen and Spiegelhalter algorithm for Bayesian networks requires computational time that grows exponentially with the size of the largest clique of a triangulated “moral graph” corresponding to the network. The moral graph is obtained by adding arcs between all pairs of immediate predecessors (parents) of every node. We will see that the size of cliques in the triangulated moral graph can be bounded when the size of extended ancestral sets is not, which indicates that the Lauritzen-Spiegelhalter algorithm may be practical for a larger class of networks than ours. But their algorithm solves only classical Bayesian networks.

Many computational issues regarding the nonlinear programming model remain unresolved, but our purpose here is to show that the computational problem can be limited to a reasonable size, rather than to investigate which algorithm solves it best. Nonlinear programming is a well-developed technology that offers a number of solution approaches, some of which we will examine in a future paper.

In the first two sections below we present the basic ideas of probabilistic logic and Bayesian networks, and in the third section we show how to combine the two. The next four sections deal with computational issues. Section 4 reviews three column generation methods that have been proposed for probabilistic logic, and Section 5 shows how to use the same methods in Bayesian logic via Benders decomposition. In Section 6 we describe our method of encoding nonlinear constraints and prove some bounds on their number, and in Section 7 we state a precise algorithm for generating the nonlinear constraints. In the final section we make some concluding remarks.

## 1. Probabilistic logic

Whereas ordinary propositional logic is two-valued (a formula is either true or false), the truth value of a formula in probabilistic logic can be any real number in the interval from 0 to 1. The truth value is interpreted as the probability the formula is true.

Suppose, for instance, that we have a knowledge base consisting of three formulas:

$$
\begin{array}{l} x _ {1} \\ x _ {1} \supset x _ {2} \\ x _ {2} \supset x _ {3}, \end{array}\tag{1}
$$

where $x_{1}$ , $x_{2}$ and $x_{3}$ are atomic propositions, and $x_{1} \supset x_{2}$ is the material conditional, “if $x_{1}$ , then $x_{2}$ ”. Let us say that a possible world is an assignment of truth values, true or false, to every atomic proposition. For example, $(x_{1}, x_{2}, x_{3}) = (0, 1, 1)$ , where 1 denotes true and 0 denotes false, is a possible world. In propositional logic, a model is simply a possible world. A proposition is true (or false) in a model if the corresponding assignment of truth values to atomic propositions makes the proposition true (or false). Inference of a conclusion, such as $x_{3}$ , from a set of premises, such as (1), is governed by the following principle.

The truth values the conclusion can have are those it has in the models in which the premises have the assigned truth values.

If the conclusion is true in all models in which the premises are true, we can infer the conclusion from the premises. Since $x_{3}$ is true in all models in which the premises (1) are true, we can infer $x_{3}$ from (1).

Suppose, however, that we are not sure that the formulas (1) are true and wish to assign them probabilities 0.9, 0.8 and 0.4, respectively. We want to know what probability (or probabilities) can be assigned formula $x_3$ . Probabilistic logic answers this question by letting a model be, not a possible world, but a distribution of probabilities over all possible worlds. (Ordinary propositional logic in effect assigns a probability of one to exactly one possible world and zero to the others. In this sense, probabilistic logic is a generalization of propositional logic). In a given model, the probability of a proposition is the sum of the probabilities of the possible worlds in which the proposition is true. (This follows from the law of total probability.) The inference of a conclusion, such as $x_3$ , from a set of premises, such as (1), is governed by the following principle.

The probabilities the conclusion can have are those it has in the models in which the premises have the assigned probabilities.

In the example, we cannot infer a single probability for $x_{3}$ , because $x_{3}$ has different probabilities in different models in which the premises have the assigned probabilities. One such model is the following (the 1's indicate in which worlds the four propositions listed are true). In this model, $x_{1}$ indeed has the assigned probability

0.9, since it is true in the last four worlds. Similarly, the probabilities of $x_{1} \supset x_{2}$ and $x_{2} \supset x_{3}$ are 0.8 and 0.4, respectively. The probability of $x_{3}$ in this particular model is 0.23, but it has other probabilities in other models consistent with the assigned probabilities. Our goal is to determine what probabilities $x_{3}$ can have over all such models.

To do this in general, suppose there are n atomic propositions and m logical formulas, so that there are $2^{n}$ possible worlds. Let a vector p of $N = 2^{n}$ components denote the distribution of probabilities over possible worlds. Then the probability of a given formula is ap, where a is a binary row vector indicating in which worlds the formula is true. For example, $a = (1, 1, 0, 1, 1, 1, 0, 1)$ for the formula $x_{2} \supset x_{3}$ . Let A be an $m \times N$ matrix in which the i-th row indicates, in this manner, the worlds in which the i-th formula is true. Denote $\pi = (\pi_{1}, \ldots, \pi_{m})$ , where $\pi_{i}$ is the probability of the i-th formula. Then we have the following connection between A, p and $\pi$ :

$$
A p = \pi , \sum_ {j = 1} ^ {N} p _ {j} = 1, p \geq 0.
$$

The equation $Ap = \pi$ expresses the fact that the probability of a given formula is the sum of the probabilities of the possible worlds in which it is true. The last two statements say that the vector p is a probability distribution.

In the example, we have $\pi_{1}=0.9$ , $\pi_{2}=0.8$ and $\pi_{3}=0.4$ . We can assign $x_{3}$ any probability $\pi_{4}$ that satisfies the system:

$$
\left( \begin{array}{c c c c c c c c} 0 & 0 & 0 & 0 & 1 & 1 & 1 & 1 \\ 1 & 1 & 1 & 1 & 0 & 0 & 1 & 1 \\ 1 & 1 & 0 & 1 & 1 & 1 & 0 & 1 \\ 0 & 1 & 0 & 1 & 0 & 1 & 0 & 1 \end{array} \right) \left( \begin{array}{c} p _ {1} \\ \vdots \\ p _ {8} \end{array} \right) = \left( \begin{array}{c} 0. 9 \\ 0. 8 \\ 0. 4 \\ \pi_ {4} \end{array} \right)\tag{2}
$$

$$
\sum_ {j = 1} ^ {8} p _ {j} = 1, p _ {j} \geq 0, j = 1, \ldots , 8.
$$

Possible worlds

<table><tr><td> $(x_1, x_2, x_3) =$ Probability =</td><td>(0, 0, 0)0.02</td><td>(0, 0, 1)0.01</td><td>(0, 1, 0)0.03</td><td>(0, 1, 1)0.04</td><td>(1, 0, 0)0.15</td><td>(1, 0, 1)0.05</td><td>(1, 1, 0)0.57</td><td>(1, 1, 1)0.13</td></tr><tr><td> $x_1$ </td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>1</td><td>1</td><td>1</td></tr><tr><td> $x_1 \supset x_2$ </td><td>1</td><td>1</td><td>1</td><td>1</td><td>0</td><td>0</td><td>1</td><td>1</td></tr><tr><td> $x_2 \supset x_3$ </td><td>1</td><td>1</td><td>0</td><td>1</td><td>1</td><td>1</td><td>0</td><td>1</td></tr><tr><td> $x_3$ </td><td>0</td><td>1</td><td>0</td><td>1</td><td>0</td><td>1</td><td>0</td><td>1</td></tr></table>

Our task is to determine which values $\pi_{4}$ can take. The system (2) says that the vector $(0.9, 0.8, 0.4, \pi_{4})$ is a convex combination of the columns of the A-matrix. But the columns can be interpreted as points in 4-dimensional space, so that the vector must lie in the convex hull of these points. As $\pi_{4}$ varies, $(0.9, 0.8, 0.4, \pi_{4})$ traces out a line, and its intersection with the convex hull is a line segment that corresponds to a range of values that $\pi_{4}$ can take.

An obvious way of finding the range of values for $\pi_{4}$ is to minimize and maximize $\pi_{4}$ subject to the constraints (2). This is a linear programming problem. The minimum value of $\pi_{4}$ is 0.1, and the maximum value is 0.4, which means that $\pi_{4}$ can be any probability in the range from 0.1 to 0.4 (actually an example of this particular form can be solved in closed form; see [1]).

In general we have m formulas and fix the probabilities of some of them in advance. Let us say we fix the probabilities $\overline{\pi} = (\pi_{1}, \ldots, \pi_{k})$ to $\overline{\pi}^{0} = (\pi_{1}^{0}, \ldots, \pi_{k}^{0})$ . To find the range of values for an unknown probability $\pi_{j} (k + 1 \leq j \leq m)$ , we solve the two linear programs,

max/min $\pi_{j}$

$$
\text { s.t. } A p = \pi\tag{3}
$$

$$
\overline {{{\pi}}} = \overline {{{\pi}}} ^ {0}
$$

$$
\sum_ {j = 1} ^ {N} p _ {j} = 1,   p \geq 0.
$$

In so doing we do not determine how $\pi_{k+1},\ldots,\pi_{m}$ interact. Also the matrix A may have as many as $2^{n}$ columns, which is impractical when n is large. In Section 4 we describe some column generation methods for dealing with this problem.

An added benefit of the linear programming model (3) is that sensitivity analysis is readily available. For instance, the dual variables (Lagrange multipliers) associated with the constraints $\overline{\pi} = \overline{\pi}^{0}$ indicate how sensitive the solution value is to a perturbation in the assigned probabilities $\overline{\pi}^{0}$ . This provides an indication of which probability estimates are critically important and which do not matter much. One might then want to review the assigned probabilities that are critical.

## 2. Bayesian networks

A Bayesian network $[33,30]$ consists of nodes representing events and directed arcs representing probabilistic dependence among the events. An event can in general have several possible outcomes, but we will associate each node with an atomic proposition, which can have two possible outcomes: true and false. In Figure 1, for instance, we can imagine that node 1 represents the proposition that a patient has a certain symptom. Nodes 2 and 3 represent assertions that the patient has either of two diseases that may cause the symptom, which we may call disease 2 and disease 3. Node 4 represents the proposition that the patient has a genetic trait that predisposes him to both diseases. Finally, a patient has this genetic trait when he has gene 5 (represented by node 5) or when he has gene 6 (represented by node 6) or both.

We will associate each node j with atomic proposition $x_{j}$ . The probability that $x_{j}$ is true is $\Pr(x_{j})$ , and the probability that $x_{j}$ is false is the probability $\Pr(\bar{x}_{j}) = 1 - \Pr(x_{j})$ that its denial $\bar{x}_{j}$ is true. It will be convenient to let $X_{j}$ be a variable whose value is either $x_{j}$ or $\bar{x}_{j}$ . For instance,

$$
\sum_ {X _ {j}} \operatorname * {P r} (X _ {j}) = \operatorname * {P r} (x _ {j}) + \operatorname * {P r} (\bar {x} _ {j}).
$$

It is also convenient to denote the probability $\operatorname{Pr}(X_i \wedge X_j)$ that both $X_i$ and $X_j$ are true with the two notational styles $\operatorname{Pr}(X_i X_j)$ and $\operatorname{Pr}(\{X_i, X_j\})$ . For sets $A$ and $B$ of propositions or propositional variables, we let $\operatorname{Pr}(A, B) = \operatorname{Pr}(A \cup B)$ .

The conditional probability of $X_{i}$ given $X_{j}$ is $\Pr(X_{i} \mid X_{j}) = \Pr(X_{i}X_{j}) / \Pr(X_{j})$ . Two propositions $X_{i}$ and $X_{j}$ are independent if $\Pr(X_{i} \mid X_{j}) = \Pr(X_{i})$ , which is to say $\Pr(X_{i}X_{j}) = \Pr(X_{i})\Pr(X_{j})$ . Conditional independence is defined as follows: $X_{i}$ and $X_{j}$ are independent, given that $X_{1},\ldots ,X_{k}$ are true, if $\Pr (X_i\mid X_jX_1\dots X_k) = \Pr (X_i\mid X_1\dots X_k)$ , which is to say $\Pr (X_iX_j\mid X_1\dots X_k) = \Pr (X_i\mid X_1\dots X_k)\Pr (X_j\mid X_1\dots X_k)$ .

![](/api/attachments/9F9CMYKX/fulltext/images/65c59db08394ac72451fd276f114e753e47cee168d4802dfcc796af692199809.jpg)  
Fig. 1.

Node j is a predecessor of node k if there is a directed path from j to k. Node j is an immediate predecessor (or parent) of k if a directed arc runs from j to k. A Bayesian network must be acyclic, meaning that no directed path leads from a node back to the node. A singly connected network is a special case of an acyclic network in which there is at most one directed path connecting any two nodes.

The meaning of the Bayesian network is summed up in the following principle: the probability that a node is true, when conditioned on the truth values of all its predecessors, is equal to the probability it is true, conditioned only on the truth values of its immediate predecessors. In Figure 1 the probability of observing the symptom depends only on which diseases the patient has, which is to say $\Pr(x_{1} \mid X_{2}X_{3}X_{4}X_{5}X_{6}) = \Pr(x_{1} \mid X_{2}X_{3})$ for all values of $X_{2}, \ldots, X_{6}$ . From this it follows that $\Pr(x_{1} \mid S) = \Pr(x_{1} \mid X_{2}X_{3})$ , where S is any subset of $\{X_{2}, \ldots, X_{6}\}$ containing $X_{2}$ and $X_{3}$ .

Bayesian networks encode conditional independence in the following way. We say that nodes $i$ and $j$ are independent relative to a set $\{1, \ldots, k\}$ of nodes if $X_i$ and $X_j$ are independent, given that $X_1, \ldots, X_k$ are true, for all substitution values of $X_1, \ldots, X_k$ , $X_i$ , $X_j$ . In a Bayesian network, nodes $i$ and $j$ are independent relative to a set $S$ of nodes if $i$ and $j$ have no common predecessor when the nodes in $S$ and all arcs incident to them are removed. For instance, nodes 2 and 3 are independent relative to node 4 in Figure 1, because 2 and 3 have no common predecessor when node 4 and the four attached arcs are removed. Thus whether one has disease 2 is independent of whether he has disease 3, once it is known whether he has the genetic trait. Mathematically, the joint probability of the two diseases is $\Pr(X_2 X_3 | X_4) = \Pr(X_2 | X_3 X_4) \Pr(X_3 | X_4) = \Pr(X_2 | X_4) \Pr(X_3 | X_4)$ .

For classical Bayesian networks, one must specify the probability of each node conditioned on every possible outcome of its immediate predecessors. For instance, we might say that the patient has the genetic trait (node 4) precisely when he has gene 5 or gene 6 or both, so that we can define the conditional probabilities of node 4 as follows:

$$
\begin{array}{l l} \operatorname * {P r} \big (x _ {4} | x _ {5} x _ {6} \big) = 1 & \operatorname * {P r} \big (x _ {4} | \bar {x} _ {5} x _ {6} \big) = 1 \\ \operatorname * {P r} \big (x _ {4} | x _ {5} \bar {x} _ {6} \big) = 1 & \operatorname * {P r} \big (x _ {4} | \bar {x} _ {5} \bar {x} _ {6} \big) = 0. \end{array}
$$

Thus $\Pr(x_{4})=\Pr(x_{5}x_{6})+\Pr(x_{5}\bar{x}_{6})+\Pr(\bar{x}_{5}x_{6})$ . This in effect associates the molecular proposition $x_{5}\vee x_{6}$ (“ $x_{5}$ or $x_{6}$ ”) with node 4. The network also shows nodes 5 and 6 to be independent, since $\Pr(x_{5}\mid X_{6})=\Pr(x_{5})$ . We do not really know that the two genes occur independently, but since we are equally ignorant of the conditional probability relating one to the other, we will suppose they are independent.

We can also suppose that the conditional probabilities of observing the symptom are:

$$
\begin{array}{l l} \operatorname * {P r} (x _ {1} | x _ {2} x _ {3}) = 0. 9 5 & \operatorname * {P r} (x _ {1} | \bar {x} _ {2} x _ {3}) = 0. 8 \\ \operatorname * {P r} (x _ {1} | x _ {2} \bar {x} _ {3}) = 0. 7 & \operatorname * {P r} (x _ {1} | \bar {x} _ {2} \bar {x} _ {3}) = 0. 1. \end{array}\tag{4}
$$

Assume further that the predisposition to either disease is captured in the following conditional probabilities:

$$
\begin{array}{l l} \operatorname * {P r} (x _ {2} | x _ {4}) = 0. 4 & \operatorname * {P r} (x _ {2} | \bar {x} _ {4}) = 0. 0 5 \\ \operatorname * {P r} (x _ {3} | x _ {4}) = 0. 2 & \operatorname * {P r} (x _ {3} | \bar {x} _ {4}) = 0. 1. \end{array}\tag{5}
$$

We can calculate the probability associated with a node by conditioning on its immediate predecessors. For instance, we can calculate the probability of observing the symptom in a patient with the genetic trait by conditioning on whether he has the two diseases:

$$
\begin{array}{r l} \operatorname * {P r} (x _ {1} | x _ {4}) & = \sum_ {X _ {2} X _ {3}} \operatorname * {P r} (x _ {1} | X _ {2} X _ {3} x _ {4}) \operatorname * {P r} (X _ {2} X _ {3} | x _ {4}) \\ & = \sum_ {X _ {2} X _ {3}} \operatorname * {P r} (x _ {1} | X _ {2} X _ {3}) \operatorname * {P r} (X _ {2} | x _ {4}) \\ & \quad \operatorname * {P r} (X _ {3} | x _ {4}) = 0. 4 4 4. \end{array}\tag{6}
$$

If the patient is known to have disease 2, the probability of the symptom is,

$$
\begin{array}{r l} \operatorname * {P r} (x _ {1} | x _ {2} x _ {4}) & = \sum_ {X _ {3}} \operatorname * {P r} (x _ {1} | x _ {2} X _ {3} x _ {4}) \operatorname * {P r} (X _ {3} | x _ {2} x _ {4}) \\ & = \sum_ {X _ {3}} \operatorname * {P r} (x _ {1} | x _ {2} X _ {3}) \operatorname * {P r} (X _ {3} | x _ {4}) = 0. 7 5. \end{array}\tag{7}
$$

Similarly, $\operatorname{Pr}(x_1 \mid x_3 x_4) = 0.86$ , and $\operatorname{Pr}(x_1 \mid x_3 \bar{x}_4) = 0.8075$ .

We can use Bayes' rule to reason backward from effects to causes. Bayes' rule says that $\Pr(X_j \mid X_i) = \Pr(X_i \mid X_j)\Pr(X_j)/\Pr(X_i)$ . Thus if we observe the symptom in a person with the genetic condition, the probability he has disease 2 is,

$$
\begin{array}{r l} \operatorname * {P r} (x _ {2} | x _ {1} x _ {4}) & = \operatorname * {P r} (x _ {1} | x _ {2} x _ {4}) \operatorname * {P r} (x _ {2} | x _ {4}) / \operatorname * {P r} (x _ {1} | x _ {4}) \\ & = 0. 6 7 5 7. \end{array}
$$

A powerful feature of Bayesian networks is that they can account for preemptive causation. Thus if we observe somehow that the patient actually has disease 3, then (in this particular case) the probability that he has disease 2 decreases, since the presence of disease 3 is a likely explanation for the symptom. Applying Bayes' rule,

$$
\begin{array}{r l} \operatorname * {P r} (x _ {2} | x _ {1} x _ {3} x _ {4}) & = \operatorname * {P r} (x _ {1} | x _ {2} x _ {3} x _ {4}) \operatorname * {P r} (x _ {2} | x _ {3} x _ {4}) / \\ & \quad \operatorname * {P r} (x _ {1} | x _ {3} x _ {4}) \\ & = \operatorname * {P r} (x _ {1} | x _ {2} x _ {3}) \operatorname * {P r} (x _ {2} | x _ {4}) / \\ & \quad \operatorname * {P r} (x _ {1} | x _ {3} x _ {4}) = 0. 4 4 1 9, \end{array}
$$

so that the probability of disease 2 drops from 0.6757 to 0.4419. Similarly, $\Pr(x_{2} \mid x_{1}x_{3}\bar{x}_{4}) = 0.0588$ (If the conditional probabilities were different, observing disease 3 could increase the posterior probability of disease 2).

Finally, if we know prior probabilities of the patient's having gene 5 and of his having gene 6, we can compute posterior probabilities without observing whether he has the genetic trait. For instance, if

$$
\operatorname * {P r} (x _ {5}) = 0. 2 5 \quad \operatorname * {P r} (x _ {6}) = 0. 1 5,\tag{8}
$$

then the probability he has the genetic trait is

$$
\begin{array}{r l} \operatorname * {P r} (x _ {4}) & = \sum_ {X _ {5} X _ {6}} \operatorname * {P r} (x _ {4} | X _ {5} X _ {6}) \operatorname * {P r} (X _ {5} X _ {6}) \\ & = \sum_ {X _ {5} X _ {6}} \operatorname * {P r} (x _ {4} | X _ {5} X _ {6}) \operatorname * {P r} (X _ {5}) \operatorname * {P r} (X _ {6}) \\ & = 0. 3 6 2 5. \end{array}
$$

(Note that if we had not assumed independence of the two genes, we would have had to write $\Pr(X_{5}X_{6})=\Pr(X_{5}\mid X_{6})\Pr(X_{6})$ , which involves the unknown conditional probability $\Pr(X_{5}\mid X_{6})$ . It follows that the probability, say, of finding disease 2 in a patient with unknown genetic makeup who has disease 3 and the symptom is,

$$
\begin{array}{r l} \operatorname * {P r} (x _ {2} | x _ {1} x _ {3}) & = \sum_ {X _ {4}} \operatorname * {P r} (x _ {2} | x _ {1} x _ {3} X _ {4}) \operatorname * {P r} (X _ {4} | x _ {1} x _ {3}) \\ & = 0. 2 6 8 6, \end{array}
$$

where $\Pr(x_{4}\mid x_{1}x_{3})=0.5478$ is obtained by several additional calculations.

## 3. Bayesian logic

Bayesian logic is the result of using the possible world model of probabilistic logic to interpret the probability statements associated with a Bayesian network. The mathematical programming model is exactly the same as in probabilistic logic, except that conditional independence statements must be encoded as additional, nonlinear constraints. We will first show how the model specifies prior and conditional probabilities, then how it incorporates (conditional) independence assumptions, and finally it can be used to infer probability ranges.

Consider again the example of Figure 1. Since there are six atomic propositions $x_{1},\ldots,x_{6}$ , there are $2^{6}=64$ possible worlds. Let p be the vector of their probabilities. To fix the probabilities of having gene 5 and having gene 6 as in (8), we simply use the constraints,

$$
\begin{array}{l} \operatorname * {P r} (x _ {5}) = 0. 2 5 \\ \operatorname * {P r} (x _ {6}) = 0. 1 5, \end{array}\tag{9}
$$

where $\Pr(x_{5})$ and $\Pr(x_{6})$ are regarded as variables in the mathematical program (Before, we used $\pi_{j}$ 's, but a different notation is more convenient now). As in ordinary probabilistic logic, $\Pr(F)$ for any formula F is the sum of the probabilities of the possible worlds in which F is true. We therefore add the constraint $\Pr(x_{5}) = ap$ , where $a_{j}$ is 1 when $x_{5}$ is true in possible world j and is 0 otherwise, and similarly for $\Pr(x_{6})$ .

To set the conditional probability $\Pr(x_{1}|x_{2}x_{3})$ to 0.95 as in (4), we impose the constraint $\Pr(x_{1}x_{2}x_{3})/\Pr(x_{2}x_{3})=0.95$ . This is equivalent to the first constraint below, which is followed by constraints fixing the other conditional probabilities $\operatorname{Pr}(x_1 \mid X_2X_3)$ .

$$
\begin{array}{l} \operatorname * {P r} (x _ {1} x _ {2} x _ {3}) - 0. 9 5 \operatorname * {P r} (x _ {2} x _ {3}) = 0 \\ \operatorname * {P r} (x _ {1} x _ {2} \bar {x} _ {3}) - 0. 7 \operatorname * {P r} (x _ {2} \bar {x} _ {3}) = 0 \\ \operatorname * {P r} (x _ {1} \bar {x} _ {2} x _ {3}) - 0. 8 \operatorname * {P r} (\bar {x} _ {2} x _ {3}) = 0 \\ \operatorname * {P r} (x _ {1} \bar {x} _ {2} \bar {x} _ {3}) - 0. 1 \operatorname * {P r} (\bar {x} _ {2} \bar {x} _ {3}) = 0. \end{array}\tag{10}
$$

We again impose constraints of the form $\Pr(F)=ap$ , where F ranges over the eight formulas in (10).

If instead of fixing $\Pr(x_{1}|x_{2}x_{3})$ at exactly 0.95, we wanted to put it in the interval from 0.9 to 0.98, we would replace the first constraint of (10) with the two constraints $0.9 \leq \Pr(x_{1}x_{2}x_{3}) / \Pr(x_{2}x_{3}) \leq 0.98$ , which can be written,

$$
\begin{array}{l} \operatorname * {P r} (x _ {1} x _ {2} x _ {3}) - 0. 9 \operatorname * {P r} (x _ {2} x _ {3}) \geq 0 \\ - \operatorname * {P r} (x _ {1} x _ {2} x _ {3}) + 0. 9 8 \operatorname * {P r} (x _ {2} x _ {3}) \geq 0. \end{array}
$$

The conditional probabilities $\Pr(x_{2}|X_{4})$ and $\Pr(x_{3}|X_{4})$ in (5) are fixed as follows:

$$
\begin{array}{l} \operatorname * {P r} (x _ {2} x _ {4}) - 0. 4 \operatorname * {P r} (x _ {4}) = 0 \\ \operatorname * {P r} (x _ {2} \bar {x} _ {4}) - 0. 0 5 \operatorname * {P r} (\bar {x} _ {4}) = 0 \\ \operatorname * {P r} (x _ {3} x _ {4}) - 0. 2 \operatorname * {P r} (x _ {4}) = 0 \\ \operatorname * {P r} (x _ {3} \bar {x} _ {4}) - 0. 1 \operatorname * {P r} (\bar {x} _ {4}) = 0. \end{array}\tag{11}
$$

(12)

The six probability variables in (11) and (12) are defined in terms of p using the same sort of constraint as above.

Since $x_{4}$ is really the disjunction of $x_{5}$ and $x_{6}$ , probabilistic logic permits us to omit nodes 5 and 6 and the conditional probabilities $\Pr(x_{4} \mid X_{5}X_{6})$ . Instead, we merely define $\Pr(x_{5}x_{6})$ , $\Pr(x_{5}\bar{x}_{6})$ , $\Pr(\bar{x}_{5}x_{6})$ and $\Pr(x_{4})$ in terms of p in the usual way and add the constraint

$$
\operatorname * {P r} \left(x _ {4}\right) = \operatorname * {P r} \left(x _ {5} x _ {6}\right) + \operatorname * {P r} \left(x _ {5} \bar {x} _ {6}\right) + \operatorname * {P r} \left(\bar {x} _ {5} x _ {6}\right)\tag{13}
$$

This allows us to drop the gratuitous assumption that the two genes occur independently, since in probabilistic logic, the conditional probabilities $\Pr(x_{5} \mid X_{6})$ need not be specified if we do not know them. If we wanted to retain the assumption that the genes occur independently, we would simply retain nodes 5 and 6 in the network.

We can fix prior probabilities that play no role in the Bayesian network. For instance, if we knew somehow that there is a 50% chance that the patient has either disease 2 or disease 3, then we cold add the constraint,

$$
\operatorname * {P r} (x _ {2} \vee x _ {3}) = 0. 5.
$$

The variable $\Pr(x_{2} \vee x_{3})$ is defined by a constraint $\Pr(x_{2} \vee x_{3}) = ap$ in the usual way, and it does not appear in the network.

We can also specify conditional probabilities that do not correspond to arcs in the network. We could, for instance, specify that $\Pr(x_{2} \mid x_{1}) = 0.4$ . In fact, if we added directed arcs to the network for every specified conditional probability, the network could well have directed cycles. The arc (1, 2) corresponding to $\Pr(x_{2} \mid x_{1})$ , for instance, completes the directed cycle 2.1.2. But since we include in the network only those arcs necessary to define the desired independence relations, the network must be acyclic.

Up to now we have not departed from ordinary probabilistic logic. But the independence relations implicit in a Bayesian network must somehow be encoded. The most straightforward approach is the following. Using the definition of conditional probability, we can compute the joint probability distribution of the atomic propositions $x_{1},\ldots,x_{4}$ in Figure 1 as follows (We omit $x_{5}$ and $x_{6}$ since we dropped the corresponding nodes).

$$
\begin{array}{r l} \operatorname * {P r} (X _ {1} X _ {2} X _ {3} X _ {4}) & = \operatorname * {P r} (X _ {1} | X _ {2} X _ {3} X _ {4}) \operatorname * {P r} (X _ {2} | X _ {3} X _ {4}) \\ & \times \operatorname * {P r} (X _ {3} | X _ {4}) \operatorname * {P r} (X _ {4}) \end{array} \tag {14}
$$

The computation is valid for any substitution of $x_{j}$ or $\bar{x}_{j}$ for each $X_{j}$ . Due to the structure of the Bayesian network, two of the conditional probabilities in (14) simplify as follows:

$$
\operatorname * {P r} \left(X _ {1} \mid X _ {2} X _ {3} X _ {4}\right) = \operatorname * {P r} \left(X _ {1} \mid X _ {2} X _ {3}\right)\tag{15}
$$

$$
\operatorname * {P r} \left(X _ {2} \mid X _ {3} X _ {4}\right) = \operatorname * {P r} \left(X _ {2} \mid X _ {4}\right).\tag{16}
$$

This means that the joint probability in (14) can be computed,

$$
\begin{array}{c} \operatorname * {P r} (X _ {1} \dots X _ {4}) = \operatorname * {P r} (X _ {1} | X _ {2} X _ {3}) \operatorname * {P r} (X _ {2} | X _ {4}) \\ \times \operatorname * {P r} (X _ {3} | X _ {4}) \operatorname * {P r} (X _ {4}). \end{array}\tag{17}
$$

We conclude that the independence constraints (15) and (16) are adequate for calculating the underlying joint distribution and therefore capture the independence properties of the network. Again using the definition of conditional probability, we write (15) and (16) as the following nonlinear constraints:

$$
\begin{array}{r l} \operatorname * {P r} (X _ {1} X _ {2} X _ {3} X _ {4}) \operatorname * {P r} (X _ {2} X _ {3}) & = \operatorname * {P r} (X _ {1} X _ {2} X _ {3}) \\ & \times \operatorname * {P r} (X _ {2} X _ {3} X _ {4}) \\ \operatorname * {P r} (X _ {2} X _ {3} X _ {4}) \operatorname * {P r} (X _ {4}) & = \operatorname * {P r} (X _ {2} X _ {4}) \operatorname * {P r} (X _ {3} X _ {4}) \end{array}\tag{18}
$$

(19)

It is important to note that an independence assumption like (15) or (16) represents several constraints, since it must hold when each $X_{j}$ is replaced by $x_{j}$ or $\bar{x}_{j}$ . In general, an independence assumption has the form

$$
\operatorname * {P r} \left(A, A _ {0} \mid B, B _ {0}, C, C _ {0}\right) = \operatorname * {P r} \left(A, A _ {0} \mid B, B _ {0}\right)\tag{20}
$$

where A is a set of propositional variables $X_{1}, \ldots, X_{a}$ , B is a set of b propositional variables, and C is a set of propositional variables $Y_{1}, \ldots, Y_{c}$ . Also $A_{0}, B_{0}$ , and $C_{0}$ are sets of fixed atomic propositions. We assume that the six sets are pairwise disjoint and that neither $A \cup A_{0}$ nor $C \cup C_{0}$ is empty. (20) represents $2^{a+b+c}$ constraints, corresponding to the $2^{a+b+c}$ possible values of the variables in A, B and C. But some of these constraints are redundant, due to the following.

Lemma 1 If A and C are nonempty, the $2^{a+b+c}$ constraints (20) are equivalent to the $(2^{a}-1)2^{b}(2^{c}-1)$ constraints corresponding to all values of the variables in A, B and C except those for which $(X_{1},\ldots,X_{a})=(\bar{x}_{1},\ldots,\bar{x}_{a})$ or $(Y_{1},\ldots,Y_{c})=(\bar{y}_{1},\ldots,\bar{y}_{c})$ . If A is empty and C nonempty, (20) is equivalent to $2^{b}(2^{c}-1)$ constraints. If A is nonempty and C empty, (20) is equivalent to $(2^{a}-1)2^{b}$ constraints. If both A and C are empty, (20) is equivalent to $2^{b}$ constraints.

Proof Suppose first that $A$ and $C$ are nonempty. We do not need to impose (20) with $(X_1, \ldots, X_a) = (\bar{x}_1, \ldots, \bar{x}_a)$ because we can sum either side of (20) over all $X$ except $(\bar{x}_1, \ldots, \bar{x}_a)$ and take the complement of both sides to obtain,

$$
\begin{array}{r l} & \operatorname * {P r} \big (\{\bar {x} _ {1}, \dots , \bar {x} _ {a} \}, A _ {0} | B, B _ {0}, C, C _ {0} \big) \\ & = \operatorname * {P r} \big (\{\bar {x} _ {1}, \dots , \bar {x} _ {a} \}, A _ {0} | B, B _ {0} \big). \end{array}
$$

We do not need to impose (20) when $(Y_{1},\ldots ,Y_{c})$ $= (\bar{y}_1,\dots ,\bar{y}_c)$ because Bayes' rule allows us to rewrite (20) as,

$$
\begin{array}{c} \operatorname * {P r} (C, C _ {0} | A, A _ {0}, B, B _ {0}) \operatorname * {P r} (A, A _ {0} | B, B _ {0}) / \\ \operatorname * {P r} (C, C _ {0} | B, B _ {0}) = \operatorname * {P r} (A, A _ {0} | B, B _ {0}), \end{array}
$$

which is equivalent to

$$
\begin{array}{l} \operatorname * {P r} (C, C _ {0} | A, A _ {0}, B, B _ {0}) \operatorname * {P r} (A, A _ {0} | B, B _ {0}) \\ = \operatorname * {P r} (C, C _ {0} | B, B _ {0}) \operatorname * {P r} (A, A _ {0} | B, B _ {0}). \end{array}\tag{21}
$$

(We do not divide by $\Pr(A, A_{0} \mid B, B_{0})$ because it could be zero). Summing each side of (21) over all values of $(Y_{1}, \ldots, Y_{c})$ except $(\bar{y}_{1}, \ldots, \bar{y}_{c})$ , and subtracting $\Pr(A, A_{0} \mid A, B_{0})$ from either side, we get (after reversing the sign),

$$
\begin{array}{l} \operatorname * {P r} \big (\{\bar {y} _ {1}, \dots , \bar {y} _ {c} \}, C _ {0} | A, A _ {0}, B, B _ {0} \big) \\ \times \operatorname * {P r} (A, A _ {0} | B, B _ {0}) \\ = \operatorname * {P r} \big (\{\bar {y} _ {1}, \dots , \bar {y} _ {c} \}, C _ {0} | B, B _ {0} \big) \operatorname * {P r} (A, A _ {0} | B, B _ {0}). \end{array}
$$

From this it follows that,

$$
\begin{array}{l} \operatorname * {P r} \big (A, A _ {0} | B, B _ {0}, \{\bar {x} _ {1}, \dots , \bar {x} _ {c} \}, C _ {0} \big) \\ = \operatorname * {P r} \big (A, A _ {0} | B, B _ {0} \big), \end{array}
$$

as desired. The rest of the lemma is similarly obtained. □

For example, (15) is equivalent to the $(2^{1} - 1)$ $2^{2}(2^{1} - 1) = 4$ constraints,

$$
\begin{array}{l} \operatorname * {P r} (x _ {1} | x _ {2} x _ {3} x _ {4}) = \operatorname * {P r} (x _ {1} | x _ {2} x _ {3}) \\ \operatorname * {P r} (x _ {1} | x _ {2} \bar {x} _ {3} x _ {4}) = \operatorname * {P r} (x _ {1} | x _ {2} \bar {x} _ {3}) \\ \operatorname * {P r} (x _ {1} | \bar {x} _ {2} x _ {3} x _ {4}) = \operatorname * {P r} (x _ {1} | \bar {x} _ {2} x _ {3}) \\ \operatorname * {P r} (x _ {1} | \bar {x} _ {2} \bar {x} _ {3} x _ {4}) = \operatorname * {P r} (x _ {1} | \bar {x} _ {2} \bar {x} _ {3}), \end{array}\tag{22}
$$

and (16) to the $(2^{1} - 1)2^{1}(2^{1} - 1) = 2$ constraints,

$$
\begin{array}{l} \operatorname * {P r} (x _ {2} | x _ {3} x _ {4}) = \operatorname * {P r} (x _ {2} | x _ {4}) \\ \operatorname * {P r} (x _ {2} | x _ {3} \bar {x} _ {4}) = \operatorname * {P r} (x _ {2} | \bar {x} _ {4}). \end{array}\tag{23}
$$

Finally, we can obtain bounds on the probability of any formula $F_{0}$ by solving the two nonlinear programs,

$$
\min / \max \operatorname * {P r} (F _ {0})\tag{24}
$$

$$
\begin{array}{r l} \text { subject   to } & \operatorname * {P r} (\{x _ {i} \}, S _ {i}, T _ {i}) \operatorname * {P r} (S _ {i}) = \operatorname * {P r} (S _ {i}, T _ {i}) \\ & \operatorname * {P r} (\{x _ {i} \}, S _ {i}), \quad i = 1, \dots , m \end{array}\tag{25}
$$

$$
B \pi = b\tag{26}
$$

$$
C \pi \geq c\tag{27}
$$

$$
A p = \pi ,\tag{28}
$$

$$
\sum_ {j = 1} p _ {j} = 1\tag{29}
$$

$$
p _ {j} \geq 0, \quad j = 1, \dots , 2 ^ {n}\tag{30}
$$

The nonlinear constraints (25) enforce (conditional) independence assumptions. The linear constraints (26), (27) fix or place bounds on those prior and conditional probabilities for which information is available. The vector $\pi$ contains all variables of the form $\Pr(F)$ . Constraints (26) also equate atomic propositions with molecular propositions, as in (13). The linear constraints (28) define $\pi$ in terms of the probability distribution over possible worlds. If we want to obtain bounds on a conditional probability $\Pr(F_{0} \mid G_{0})$ , we replace (24) with

$\min / \max \Pr(F_0 \wedge G_0) / \Pr(G_0)$

Suppose, for example, that we wish to calculate the probability $\Pr(x_{2}|x_{1}x_{3})$ that a patient with disease 3 and the symptom has disease 2. We found this probability in section 2 to be 0.2686, on the unwarranted assumption that the two genes occur independently. We solve (24)-(30) by minimizing and then maximizing the objective function (24), which in this case is $\Pr(x_{1}x_{2}x_{3})/\Pr(x_{1}x_{3})$ . The independence constraints (25) are the nonlinear equations (15) corresponding to the four constraints (22) and the nonlinear equations (16) corresponding to the two constraints (23). The linear equality constraints (26) are the 11 constraints in (9), (10), (11), (12), and (13). There are no inequality constraints (27). The equations (28) define the probabilities of the 20 formulas that appear elsewhere in terms of the possible world probabilities $p_{j}$ . The minimum and maximum values of the objective function are 0.2179 and 0.2836, which define the range within which $\Pr(x_{2}|x_{1}x_{3})$ can lie when no unwarranted independence assumptions are made.

Sensitivity analysis is again available with the nonlinear programming model. In particular, the Lagrange multipliers associated with constraints (26) and (27) indicate how sensitive the solution is to changes in the assigned probabilities. For instance, if a prior probability bound for $x_{j}$ is given with a constraint $\Pr(x_{j}) \geq c_{i}$ that has Lagrange multiplier $\mu_{i}$ in the optimal solution, then a small perturbation $\delta$ in the bound $c_{i}$ would in general change the solution value by about $\mu_{i}\delta$ . Or if a conditional probability $\Pr(x_{j}|x_{k})$ is bounded with a constraint $\Pr(x_{j}x_{k}) - \alpha\Pr(x_{k}) \geq 0$ that has Lagrange multiplier $\mu_{i}$ , a small perturbation $\delta$ in the bound $\alpha$ is roughly equivalent to changing the right-hand side by $\delta\Pr(x_{k})^{*}$ , where $\Pr(x_{k})^{*}$ is the solution value of $\Pr(x_{k})$ . The resulting change in the solution value is therefore about $\mu_{i}\delta\Pr(x_{k})^{*}$ .

## 4. Column generation methods for probabilistic logic

Column generation was suggested for probabilistic logic by Nilsson [29] and by Georgakopoulos, Kavvadias and Papadimitriou [12] in their paper on probabilistic satisfiability. In this section, we review three particular column generation methods for solving inference problems in probabilistic logic – those proposed by Hooker [21], by Jaumard, Hansen, Aragaö and Brun [24,5], and by Kavvadias and Papadimitriou [25]. The rationale for these methods is that they introduce variables into the problem only as they are needed to improve the solution, so that only a small fraction of the total variable set may eventually be used.

If we let $a^j = (a_1^j, \ldots, a_n^j)$ be column $j$ of $A$ , we can rewrite the liner program (3) as follows:

$$
\begin{array}{l} \max \sum_ {j \in J} p _ {j} a _ {t} ^ {j} - M \sum_ {i = 1} ^ {k + 1} s _ {i} \\ \text {s.t.} \sum_ {j \in J} p _ {j} \overline {{a}} ^ {j} + s = \overline {{\pi}} _ {0} (\lambda) \\ \sum_ {j \in J} p _ {j} + s _ {k + 1} = 1 (\lambda_ {0}) \\ p _ {j} \geq 0, j \in J, s _ {i} \geq 0, i = 1, \ldots , k \end{array}\tag{31}
$$

where M is any large number (“big M”), $\bar{a}^{j} = (a_{1}^{j}, \ldots, a_{k}^{j})$ , and $s_{k+1}$ and $s = (s_{1}, \ldots, s_{k})$ are artificial variables. We associate a vector $\lambda$ of dual variables and the dual variable $\lambda_{0}$ with the constraints as shown. We treat only maximization here, but the minimization problem can be solved by changing the objective function to,

$$
\max - \sum_ {j \in J} p _ {j} a _ {t} ^ {j} - M \sum_ {i = 1} ^ {k + 1} s _ {i}.
$$

All three methods perform simplex pivots to solve the master problem (31). Initially the index set J is empty, and the starting basis consists of the slack columns. On subsequent pivots, all three methods solve a subproblem in order to generate a column $(a_{t}, \bar{a}^{j})$ that, when brought into the basis, will improve the solution. Such a column must satisfy $a_{t}^{j} - \lambda^{T}\bar{a}^{j} > \lambda_{0}$ . The index j is added to J, and a pivot is performed so as to bring $(a_{t}, \bar{a}^{j})$ into the basis. The procedures continue until no more improving columns can be found.

The three methods differ in how they generate an improving column. In the method proposed by Hooker [21], the subproblem is formulated as an integer program. In the example of the previous section, the columns of A have the form $(y_{1}, y_{2}, y_{3}, y_{4})$ , where

$$
\begin{array}{l} y _ {1} \equiv x _ {1} \\ y _ {2} \equiv x _ {1} \supset x _ {2} \\ y _ {3} \equiv x _ {2} \supset x _ {3} \\ y _ {4} \equiv x _ {3} \end{array}\tag{32}
$$

and $(x_{1}, x_{2}, x_{3})$ ranges over all possible worlds. We want a column $(a_{t}, \bar{a}^{i}) = (y_{4}, y_{1}, y_{2}, y_{3})$ for which

$$
y _ {4} - \left(\lambda_ {1} y _ {1} + \lambda_ {2} y _ {2} + \lambda_ {3} y _ {3}\right)\tag{33}
$$

is greater than $\lambda_{0}$ . We next write (32) as a system of linear inequalities in binary variables. To do this, we note that an equivalence $a \equiv b$ can be written as two conditionals, $a \supset b$ and $b \supset a$ , and a conditional $a \supset b$ can be written as a logical clause $\neg a \vee b$ . Finally, a clause $\neg a \vee b$ can be written as an inequality $(1 - a) + b \geq 1$ , or $-a + b \geq 0$ , where a and b are binary (0-1) variables for which 1 corresponds to “true” and 0 to “false”. This allows us to write (32) as the following linear system in binary variables:

$$
\begin{array}{c c c c} x _ {1} & - y _ {1} & \geq 0 \\ - x _ {1} & + y _ {1} & \geq 0 \\ - x _ {1} + x _ {2} & - y _ {2} & \geq - 1 \\ x _ {1} & + y _ {2} & \geq 1 \\ - x _ {2} & + y _ {2} & \geq 0 \\ - x _ {2} + x _ {3} & - y _ {3} & \geq - 1 \\ x _ {2} & + y _ {3} & \geq 1 \\ - x _ {3} & + y _ {3} & \geq 0 \\ x _ {3} & - y _ {4} \geq 0 \\ + x _ {3} & + y _ {4} \geq 0 \end{array}\tag{34}
$$

Now it is clear that the columns of A are precisely the vectors $(y_{1}, y_{2}, y_{3}, y_{4})$ such that $(x_{1}, x_{2}, x_{3}, y_{1}, y_{2}, y_{3}, y_{4})$ is a binary solution of (34) for some $(x_{1}, x_{2}, x_{3})$ . We can therefore solve the subproblem by maximizing (33) subject to (34).

In general, the columns of A are the vectors y such that $(x, y)$ is a binary solution of a system $H_{y}^{(x)} \geq h$ for some binary x, where the system is similar to (34). The subproblem can therefore be solved by solving the following integer program.

$$
\begin{array}{l} \text { Max } y _ {t} - \lambda^ {T} \bar {y} \\ \text { s.t. } H \binom {x} {y} \geq h, x \text { binary }. \end{array}\tag{35}
$$

where $\bar{y}=(y_{1},\ldots,y_{k})$ . Only x is explicitly required to be binary, since it can be shown that y is binary in any feasible solution in which x is binary. Since we seek only a solution for which the value of the objective function is greater than $\lambda_{0}$ , it is generally unnecessary to solve (35) to optimality. If, for example, a branch band bound method is used, branching can terminate whenever a sufficiently good solution is found. When no more improving columns exist, however, this must be verified by a complete traversal of the branch and bound tree. See [22] for a review of methods for solving integer programs with constraints that represent logical clauses.

In the method proposed by Jaumard et al. [24,5], the subproblem is formulated as a pseudo-boolean optimization problem. Each variable $y_{j}$ is first written as a numerical function of x, where the $x_{j}$ 's and $y_{j}$ 's again take the values 1 and 0 to indicate true and false. In the example, $y_{2}$ (which is equivalent to the clause $\neg x_{1} \vee x_{2}$ ) can be written as the function $f_{2}(x) = 1 - x_{1}\bar{x}_{2}$ , where $x = (x_{1}, x_{2}, x_{3})$ and $\bar{x}_{2}$ is an abbreviation for $1 - x_{2}$ . So, the subproblem can be written as the unconstrained pseudo-boolean optimization problem,

$$
\begin{array}{r l} & \max f _ {4} (x) - \sum_ {i = 1} ^ {3} \lambda_ {i} f _ {i} (x) \\ & \quad = x _ {3} - \left[ \lambda_ {1} x _ {1} + \lambda_ {2} \big (1 - x _ {1} \bar {x} _ {2} \big) + \lambda_ {3} \big (1 - x _ {2} \bar {x} _ {3} \big) \right], \end{array}
$$

where the $x_{j}$ 's are binary.

In general, if each formula of the data base is a clause, the subproblem is,

$$
\begin{array}{l} \max _ {x} f _ {i} (x) - \sum_ {i = 1} ^ {k} \lambda_ {i} f _ {i} (x), \quad \text { where } \\ f _ {i} (x) = 1 - \prod_ {j \in P _ {i}} \bar {x} _ {j} \prod_ {j \in N _ {i}} x _ {j} \end{array}\tag{36}
$$

Here, $P_{i}$ is the index set of positive literals in the i-th formula, and $N_{i}$ is the index set of negative literals. Jaumard et al. recommend using a tabu search heuristic for solving (30) [20,13]. If it fails to produce a solution value greater than $\lambda_{0}$ , they solve (30) with an exact method of Crama, Hansen and Jaumard [7] that is based on the method of Hammer and Rudeanu [19].

Finally, the method of Kavvadias and Papadimitriou [25] proposes what is in effect another heuristic for solving (30). For a given value of $x$ , the potential $\phi_j(x)$ of a variable $x_j$ is the change in the objective function value when the current value $x_j^*$ of $x_j$ is flipped to $1 - x_j^*$ . Thus

$$
\phi_ {j} (x) = \sum_ {i = 1} ^ {k} \lambda_ {i} \left[ f _ {i} \left(x ^ {\prime}\right) - f _ {i} (x) \right],
$$

where $x'$ is the result of flipping $x_{j}$ in x. The basic idea of the heuristic is to try flipping the values of one variable after another and to stop at the point the objective function is most improved. Each time we flip a variable, we flip the one that brings the most improvement. This comprises the first stage of calculation, and once it is done, we start all over again with a second stage, and keep on until no further improvement is possible.

More precisely, we start with a reasonable initial value for x and perform the first stage of computation as follows. Let $x^{l}$ be the result of the flipping the first l variables and $\Delta_{l}$ the cumulative effect on the objective function, so that $x^{0}=x$ and $\Delta_{0}=0$ . For each l, beginning with l=0, pick the variable $x_{j*}$ with the largest potential $\phi_{j}(x^{l})$ , let $\Delta_{l+1}=\Delta_{l}+\phi_{j*}(x^{l})$ , and flip the value of $x_{j*}^{l}$ in $x^{l}$ to get $x^{l+1}$ . Stop when $\Delta_{l}<0$ or l=n, and let $\Delta_{l*}$ be the largest $\Delta_{l}$ found. Let $x=x^{l*}$ and start a new stage, unless $\Delta_{1}<0$ , in which case the heuristic terminates.

To get a starting value for x, Kavvadias and Papadimitriou pick the clause i for which $\lambda_{i}$ is most negative and assign its variables values that falsify the clause. This is repeated with the clause with the next most negative $\lambda_{i}$ , and so on until no clauses with negative $\lambda_{i}$ are left, or prior assignments make it impossible to falsify the next clause. In the latter case, the unassigned variables are given random truth values.

Since this procedure is only a heuristic, its failure to find an improving column does not prove that no improving column exists. The generation of columns may therefore terminate before an optimum is found. Kavvadias and Papadimitriou discuss some similar heuristics that are more reliable but are quite time-consuming.

The second and third methods above have been computationally tested with promising results. Jaumard et al., for instance, solve problems with 70 atomic propositions and 100 clauses in about a minute on a Sun Sparc computer. About 600 columns are generated, out of a possible $2^{70}$ . The computation times obtained by Kavvadias and Papadimitriou are on the same order of magnitude.

## 5. Applying benders decomposition to Bayesian logic

We expressed the inference problem in Bayesian logic as a nonlinear program (24)-(30). Since the number of possible world probabilities $p_j$ can grow exponentially with the number of atomic propositions, we wish to use the column generation methods that are used to solve ordinary probabilistic logic problems. We can do so if we apply Benders decomposition [2,28] to (24)-(30) in an appropriate way.

The Benders decomposition technique allows one to distinguish certain “complicating” variables and to split the problem into a “master problem” and a “subproblem” so that the latter contains no complicating variables. In our case the complicating variables are those occurring in nonlinear constraints, namely the vector $\pi$ , so that the master problem contains (24)–(27) and the subproblem contains (28)–(30). The master problem then becomes:

max

$$
\operatorname * {P r} (F _ {0})\tag{24}
$$

$$
\begin{array}{r l} \text { subject   to } & \operatorname * {P r} (\{x _ {i} \}, S _ {i}, T _ {i}) \operatorname * {P r} (S _ {i}) \\ & = \operatorname * {P r} (S _ {i}, T _ {i}) \operatorname * {P r} (\{x _ {i} \}, S _ {i}), \\ & i = 1, \dots , m \end{array}\tag{25}
$$

$$
B \pi = b\tag{26}
$$

$$
C \pi \geq c\tag{27}
$$

$$
u ^ {r} \pi + u _ {0} ^ {r} \geq 0, \quad r = 1, \dots , R\tag{37}
$$

$$
0 \leq \pi_ {i} \leq 1, \quad i = 1, \dots , m\tag{38}
$$

where the additional constraints (37) are “Benders cuts”, explained below. The bounds (38) make sure that the problem has a finite solution (if any solution). The subproblem is the feasibility problem,

min 0

subject to $Ap = \pi, (u)$

(28)

$$
e ^ {T} p = 1, \left(u _ {0}\right)\tag{29}
$$

$$
p _ {j} \geq 0, \quad j = 1, \dots , 2 ^ {n}\tag{30}
$$

where $\pi$ in (28) is regarded as a constant. The master problem is a nonlinear program, but it contains only the variables in $\pi$ , which are limited in number. The subproblem contains exponentially many variables $p_{j}$ , but it is an ordinary probabilistic logic problem (in particular, a probabilistic satisfiability problem) that can be solved by the column generation methods reviewed in Section 4.

We start the procedure by first solving the master problem, without Benders cuts $(r=0)$ , for $\pi$ . We then solve the subproblem, using in (28) the value of $\pi$ just obtained. If the subproblem has a feasible solution, we are finished. Otherwise, the dual of the subproblem has an unbounded optimal value along some extreme ray $(u^{1}, u_{0}^{1})$ , where u is the vector of dual variables corresponding to (28) and $u_{0}$ the dual variable corresponding to (29). That ray gives rise to the first Benders cut in (37) $(r=1)$ . Now we re-solve the master problem in order to obtain a new $\pi$ vector, and we continue in this way. The procedure stops when either the master problem is infeasible or the subproblem is feasible. In the former case, the original problem is infeasible, and in the latter case, the optimal solution of the original problem has been found. The procedure stops in a finite number of steps (the minimization problem is solved by maximizing the negative of the objective function according to the procedure above).

For example, if we use Benders decomposition to calculate the lower bound on $\Pr(x_{2}|x_{1}x_{3})$

derived in Section 3, we obtain the solution value 0.2179 after adding 53 Benders cuts.

## 6. Limiting the number of independence constraints

Unfortunately the number of nonlinear constraints required to capture the independence assumptions, if they are formulated as above, can grow exponentially with the number of nodes. In this section we show a more efficient formulation in which the number of constraints grows only linearly with the number of nodes, provided certain structural parameters of the network are bounded.

We remarked earlier that we can capture the independence relations in a Bayesian network by imposing the constraints that are required to compute the joint probability distribution using the formula,

$$
\begin{array}{r l} \operatorname * {P r} (X _ {1} X _ {2} \dots X _ {n}) & = \operatorname * {P r} (X _ {1} | X _ {2} \dots X _ {n}) \\ & \times \operatorname * {P r} (X _ {2} | X _ {3} \dots X _ {n}) \\ & \dots \operatorname * {P r} (X _ {n}). \end{array}\tag{39}
$$

Some of the factors $\Pr(X_{k} \mid X_{k+1} \ldots X_{n})$ are equated with simpler conditional probabilities $\Pr(X_{k} \mid S)$ , where S is a subset of $\{X_{k+1}, \ldots, X_{n}\}$ . By Lemma 1, each such equation requires $2^{n-k} - 2^{j}$ nonlinear constraints, where S contains j propositions. In the worst case j = 0, which means that capturing all the independence conditions can require as many as $2^{n-1} + 2^{n-2} + \ldots + 2^{0} - n = 2^{n} - n - 1$ nonlinear constraints.

Fortunately, this exponential explosion can be avoided in a large class of networks by using only those constraints that are necessary to calculate the desired probability. Rather than write an expression like (39) for the entire joint distribution and equating conditional probabilities as needed, we generate an expression for the desired probability in a certain way and equate conditional probabilities as needed. This process is best explained by example.

Suppose first we wish to calculate $\Pr(x_{1} \mid x_{4})$ in the example of Figure 1. This probability can be derived by conditioning on $X_{2}$ and $X_{3}$ as in (6). Evaluating this expression requires only the independence constraints $\Pr(x_{1} \mid X_{2}X_{3}x_{4}) = \Pr(x_{1} \mid X_{2}X_{3})$ and $\Pr(X_{2}X_{3}\mid x_{4})=\Pr(X_{2}\mid x_{4})\Pr(X_{3}\mid x_{4})$ . As it happens the former are equivalent to the constraints (22) and the latter to the constraints (23) that are needed to compute the total joint distribution in (17), so that in this case we cannot reduce the number of constraints. But in larger problems the reduction can be dramatic.

For a second example, consider the larger Bayesian network of Figure 2, and suppose we wish to derive bounds on $\Pr(x_{1})$ . It will be convenient to assign each node to one or more generations relative to $x_{1}$ . Node 1 lies in generation 0, and in general all the parents of nodes in generation k form generation $k + 1$ .

The probability $\Pr(x_{1})$ can be determined by conditioning on its immediate predecessors:

$$
\begin{array}{c} \operatorname * {P r} (x _ {1}) = \sum \operatorname * {P r} (x _ {1} | X _ {2} X _ {1 0} X _ {1 1} X _ {1 2} X _ {1 6}) \\ \times \operatorname * {P r} (X _ {2} X _ {1 0} X _ {1 1} X _ {1 2} X _ {1 6}), \\ = \sum \operatorname * {P r} (x _ {1} | X _ {2} X _ {1 0} X _ {1 1} X _ {1 2} X _ {1 6}) \\ \times \operatorname * {P r} (X _ {2}) \operatorname * {P r} (X _ {1 0} X _ {1 1} X _ {1 2} X _ {1 6}), \end{array}
$$

where the sum is understood to be taken over all variables on which we condition, in this case $X_{2}$ , $X_{10}$ , $X_{11}$ , $X_{12}$ , $X_{16}$ . The second equality makes use of the fact that $X_{2}$ has no common predecessor with any of the other four nodes, so that we have the independence relation,

$$
\operatorname * {P r} \left(X _ {2} \mid X _ {1 0} X _ {1 1} X _ {1 2} X _ {1 6}\right) = \operatorname * {P r} \left(X _ {2}\right),
$$

which by Lemma 1 is captured in $2^{4} - 2^{1} = 14$ nonlinear constraints. We have therefore reduced the problem of calculating a probability in generation 0 to that of calculating the joint probability of the nodes in generation 1, which in turn is split into the problems of calculating $\Pr(X_{2})$ and $\Pr(X_{10}X_{11}X_{12}X_{16})$ separately.

![](/api/attachments/9F9CMYKX/fulltext/images/4009936af011e0ccb70b96efb89f6488d41d092774e4348bf1a81fd1de5bec0f.jpg)  
Fig. 2.

To calculate $\Pr(X_{2})$ , we condition on its predecessors in generation 2:

$$
\operatorname * {P r} (X _ {2}) = \sum \operatorname * {P r} (X _ {2} | X _ {3} X _ {4}) \operatorname * {P r} (X _ {3} X _ {4}).
$$

This requires no independence constraints and leaves the problem of calculating the joint probability of nodes in generation 2 by conditioning on probabilities in generation 3:

$$
\begin{array}{r l} \operatorname * {P r} (X _ {3} X _ {4}) & = \sum \operatorname * {P r} (X _ {3} X _ {4} | X _ {5} X _ {6}) \operatorname * {P r} (X _ {5} X _ {6}) \\ & = \sum \operatorname * {P r} (X _ {3} | X _ {4} X _ {5} X _ {6}) \operatorname * {P r} (X _ {4} | X _ {5} X _ {6}) \\ & \times \operatorname * {P r} (X _ {5} X _ {6}). \end{array}
$$

This calls for the equations $\Pr(X_{3} \mid X_{4}X_{5}X_{6}) = \Pr(X_{3} \mid X_{5})$ , which require 6 nonlinear constraints by Lemma 1. Next we condition on probabilities in generation 4,

$$
\begin{array}{c} \operatorname * {P r} (X _ {5} X _ {6}) = \sum \operatorname * {P r} (X _ {5} | X _ {6} X _ {7} X _ {8}) \operatorname * {P r} (X _ {6} | X _ {7} X _ {8}) \\ \times \operatorname * {P r} (X _ {7} X _ {8}), \end{array}
$$

which requires the conditions $\Pr(X_5 \mid X_6X_7X_8) = \Pr(X_5 \mid X_7X_8)$ and $\Pr(X_6 \mid X_7X_8) = \Pr(X_6 \mid X_8)$ , another 6 constraints. Finally,

$$
\operatorname * {P r} (X _ {7} X _ {8}) = \sum \operatorname * {P r} (X _ {7} | X _ {8} X _ {9}) \operatorname * {P r} (X _ {8} | X _ {9}) \operatorname * {P r} (X _ {9}),
$$

which requires 2 constraints. Note that the independence conditions never involve nodes in more than two consecutive generations. This is the key to bounding the number of constraints.

To complete the other branch of the tree, we condition on the nodes $X_{13}$ , $X_{15}$ that are in generation 2 of that branch,

$$
\begin{array}{r l} & {\operatorname * {P r} (X _ {1 0} X _ {1 1} X _ {1 2} X _ {1 6})} \\ & {\quad = \sum \operatorname * {P r} (X _ {1 0} | X _ {1 1} X _ {1 2} X _ {1 6} X _ {1 3} X _ {1 5})} \\ & {\qquad \times \operatorname * {P r} (X _ {1 1} | X _ {1 2} X _ {1 6} X _ {1 3} X _ {1 5})} \\ & {\qquad \times \operatorname * {P r} (X _ {1 2} | X _ {1 6} X _ {1 3} X _ {1 5})} \\ & {\qquad \times \operatorname * {P r} (X _ {1 6} | X _ {1 3} X _ {1 5}) \times \operatorname * {P r} (X _ {1 3} X _ {1 5}).} \end{array}
$$

This requires a total of 51 independence constraints. Next we condition on the third generation nodes $X_{14}$ and $X_{16}$ ; note that $X_{16}$ also belongs to the first generation.

$$
\begin{array}{r l} \operatorname * {P r} (X _ {1 3} X _ {1 5}) & = \sum \operatorname * {P r} (X _ {1 3} | X _ {1 5} X _ {1 4} X _ {1 6}) \\ & \times \operatorname * {P r} (X _ {1 5} | X _ {1 4} X _ {1 6}) \operatorname * {P r} (X _ {1 4} X _ {1 6}) \end{array}
$$

We use six constraints to express $\Pr(X_{13} \mid X_{15}X_{14}X_{16}) = \Pr(X_{13} \mid X_{14})$ . Since $\{X_{14}, X_{16}\}$ does not split and descends from no older generation, we need no further independence constraints.

We can therefore solve the problem with a total of 85 independence constraints. By contrast, if we used all the constraints necessary to determine the joint distribution in (39), we would have (due to Lemma 1) $2^{15}-2^{14}+\ldots+2^{1}-70=65.465$ nonlinear constraints.

We can develop these ideas formally as follows. Let us say that two sets $R_{i}$ and $R_{j}$ of nodes in a Bayesian network are independent relative to a set S of nodes if every node in $R_{i}$ is independent of every node in $R_{j}$ relative to S. A set R of nodes splits into a collection of disjoint sets $R_{1},\ldots,R_{m}$ , relative to a set S of nodes, if R is the union of $R_{1},\ldots,R_{m}$ ( $m\geq1$ ), every pair $R_{i}$ , $R_{j}$ ( $i\neq j$ ) are independent relative to S, and no $R_{i}$ contains subsets that are independent relative to S. In Figure 2, for instance, the set $R=\{3,4\}$ splits into $\{3\}$ , $\{4\}$ relative to $S=\{5\}$ but not relative to $S=\{6\}$ . We have the following recursive upper bound on the number $N(R|S)$ of independence constraints needed to compute the joint probabilities $\Pr(R|S)$ , where the r variables in R range over $2^{r}$ possible values, and S is a set of fixed atomic propositions. It is convenient to use the notation $(\alpha|C)$ for quantity $\alpha$ and logical condition C, defined by,

$$
(\alpha \mid C) = \left\{ \begin{array}{l l} \alpha , & \text { if } C \text { is   true } \\ 0, & \text { if } C \text { is   false }. \end{array} \right.
$$

Also, for a node set U we let $T(U)$ be the set of nodes not in U that are immediate predecessors of nodes in U.

Lemma 2 Let a set R of r nodes split into $R_{1}, \ldots, R_{m}$ relative to a set S of nodes, where each $R_{i}$ contains $r_{i}$ nodes. Then if $t_{i}$ is the number of nodes in $T(R_{i})\setminus S$ (i.e., the number of nodes in $T(R_{i})$ but not in S),

$$
\begin{array}{l} N (R | S) \leq \left(2 ^ {r + 1} \mid m \geq 2\right) \\ \quad + \sum_ {i = 1} ^ {m} \left(\left(2 ^ {r _ {i}} - 1\right) 2 ^ {t _ {i}} \mid S \not \subset T \left(R _ {i}\right) o r r _ {i} > 1\right) \\ \quad + N \left(T \left(R _ {i}\right) \backslash S \mid S\right). \end{array} \tag {40}
$$

Proof Since any node in $R_{i}$ is independent of any node in $R_{j}$ relative to S, $\Pr(R \mid S)$ is given by,

$$
\begin{array}{c} \operatorname * {P r} (R | S) = \operatorname * {P r} (R _ {1} | R _ {2}, \dots , R _ {m}, S) \\ \times \operatorname * {P r} (R _ {2} | R _ {3}, \dots , R _ {m}, S) \dots \operatorname * {P r} (R _ {m} | S), \end{array}
$$

together with independence constraints (when $m \geq 2$ ),

$$
\begin{array}{l} \operatorname * {P r} (R _ {i} | R _ {i + 1}, \dots , R _ {m}, S) = \operatorname * {P r} (R _ {i} | S), \\ i = 1, \dots , m - 1, \end{array}\tag{41}
$$

and the constraints needed to determine each $\Pr(R_{i}|S)$ . Since S is fixed, by Lemma 1 the number of constraints needed to enforce (41) for each i (when $m \geq 2$ ) is $(2^{r_{i}} - 1)(2^{r_{i+1} + \cdots + r_{m}} - 1) \leq 2^{r_{i} + \cdots + r_{m}}$ . Thus, when $m \geq 2$ , the total number of constraints in (41) for $i = 1, \ldots, m - 1$ is bounded above by $2^{r+1}$ , and when m = 1 it is zero. Whence the first term of (40).

To find the number of constraints needed to determine each $\Pr(R_{i} \mid S)$ , let $R_{i} = \{Y_{1}, \ldots, Y_{r_{i}}\}$ , where the $Y_{j}$ 's are numbered so that $Y_{i} \notin T(Y_{j})$ when i < j (this is possible because the network is acyclic). We condition only on the immediate predecessors of $T(R_{i})$ that are not in S, since nodes in S are already fixed to true or false. Letting $T_{i} = T(R_{i})$ , we have,

$$
\begin{array}{l} \operatorname * {P r} (R _ {i} | S) = \sum_ {T _ {i} \setminus S} \operatorname * {P r} (R _ {i} | T _ {i} \setminus S,   S) \operatorname * {P r} (T _ {i} \setminus S | S) \\ = \sum_ {T _ {i} \setminus S} \operatorname * {P r} \bigl (Y _ {1} | Y _ {2}, \ldots , Y _ {r _ {i}},   T _ {i} \setminus S,   S \bigr) \\ \quad \times \operatorname * {P r} (Y _ {2} | Y _ {3}, \ldots , Y _ {r i},   T _ {i} \setminus S,   S) \ldots \\ \quad \operatorname * {P r} \bigl (Y _ {r _ {i}} | T _ {i} \setminus S,   S \bigr) \operatorname * {P r} (T _ {i} \setminus S | S). \end{array}\tag{42}
$$

The j-th factor requires independence constraints

$$
\operatorname * {P r} \left(Y _ {j} \mid \left\{Y _ {j + 1}, \dots , Y _ {r _ {i}} \right\}, T _ {i} \backslash S, S\right) = \operatorname * {P r} \left(Y _ {j} \mid T (Y _ {j})\right),
$$

When $r_{i}=1$ , $T_{i}$ contains just the immediate predecessors of the one node in $R_{i}$ , so that $T(Y_{j})=T_{i}$ ; thus when $S\setminus T_{i}=\phi$ no independence conditions are needed, and otherwise at most $2^{t_i}$ are needed. Let us suppose, then, that $r_i \geq 2$ . In the worst case $T(Y_j)$ and $T_i \cap S$ are empty, so that by Lemma 1, $2^{r_i + t_i - j} - 1$ constraints are needed. So, summing over $j = 1, \ldots, r_i$ , (42) requires at most $(2^{r_i} - 1)2^{t_i} - r_i$ constraints. Thus, whether $r_i$ is 1 or greater, the number of constraints is at most $(2^{r_i} - 1)2^{t_i}$ , and it is zero when $r_i = 1$ and $S \subset T_i$ . Finally, we need at most $N(T(R_i) \setminus S | S)$ independence constraints to determine $\Pr(T_i \setminus S | S)$ . The lemma follows.

Lemma 2 can be used to obtain a closed-form upper bound on the number of constraints needed. To do this we introduce the notion of an “ancestral set . The ancestral sets of $x_{1}$ for the network of Figure 2 are encircled in Figure 3. Formally, we can recursively define an ancestral set of a node $X_{j}$ with respect to a set S of nodes other than $x_{j}$ as follows. $\{x_{j}\}$ is an ancestral set, and if A is an ancestral set, then so are the sets $A_{1},\ldots,A_{m}$ obtained by splitting $T(A)\backslash S$ . We refer to $A_{1},\ldots,A_{m}$ as the parent sets of A. An extended ancestral set of $x_{j}$ with respect to S is $A\cup T(A)\backslash S$ for any ancestral set A of $x_{j}$ with respect to S. The extended ancestral sets of $x_{1}$ for the network of Figure 2 are encircled in Figure 4.

If $|U|$ indicates the number of elements in set U, the following theorem is a direct result of Lemma 2.

Theorem 1 The number $N(x_{j}|S)$ of independence constraints required to determine the probability $\operatorname{Pr}(x_j|S)$ has the following bound,

![](/api/attachments/9F9CMYKX/fulltext/images/705cc3ba94f87e50a3bb1a6950f3b0442cfea2967de44989a1d64a2b42087789.jpg)  
Fig. 3.

![](/api/attachments/9F9CMYKX/fulltext/images/48222b8c50e728625cd4a522daf100886ae0c055305361c122c5c951880b9fc6.jpg)  
Fig. 4.

$$
\begin{array}{l} N (x _ {j} | S) \\ \leq \sum_ {A} \left[ \left(2 ^ {| T (A) \setminus S | + 1} \Big | m \geq 2\right) \right. \\ \left. + \left((2 ^ {| A |} - 1) 2 ^ {| T (A) \setminus S |} \Big | S \subset T (A) o r | A | > 1\right) \right], \end{array}
$$

where $A$ ranges over all ancestral sets of $X_{j}$ relative to $S$ , and $A$ has $m$ parent sets.

For instance, to determine $\Pr(x_{1}|x_{4})$ in Figure 1, we note that the ancestral sets of $X_{1}$ relative to $X_{4}$ are $\{X_{1}\}$ and its parent sets $\{X_{2}\},\{X_{3}\}$ . Thus the number of nonlinear constraints is bounded by $(2^{2+1}+1\cdot2^{2})+0+0=12$ (the actual number is 6). The number of constraints needed to determine $\Pr(x_{1})$ in Figure 2 is bounded by 175 (the actual number is 85).

An immediate corollary of Theorem 1 is that the number of independence constraints grows exponentially with the size of extended ancestral sets and increases linearly with the number of nodes if this size is bounded.

Corollary 1 Let E bound the number of nodes in any extended ancestral set of $X_{j}$ relative to S. Then the number of independence constraints grows linearly with the number of ancestral sets and therefore with the number of nodes. In particular, if the network contains K ancestral sets, then

$$
N \left(x _ {j} \mid S\right) \leq K \cdot 2 ^ {E + 1}
$$

![](/api/attachments/9F9CMYKX/fulltext/images/aef733407abfd894d6a8b95d3a365cdb8165833c20b1d3483bb4c8fe0916a4bf.jpg)  
Fig. 5.

Proof Since $A \cup (T(A) \setminus S)$ is an extended ancestral set, $|A| + |T(A) \setminus S|$ is its size, which is at least, $|T(A) \setminus S| + 1$ . The corollary follows immediately from Theorem 1. ☐

Proof The first term of the bound in theorem 1 vanishes because $m = 1$ , and the second term is at most $2^{|T(A)\setminus S|} \leq 2^{\Delta}$ .

If the network is singly connected, then every ancestral set consists of one node, so that an extended ancestral set consists of a node and its immediate predecessors. We conclude the following.

Corollary 2 Let v be the number of nodes in a single connected Bayesian network, and let $\Delta$ be an upper bound on the in-degree (i.e., the number of immediate predecessors) of any node. Then

We conclude by comparing these results with those of Lauritzen and Spiegelhalter [26]. They use the notion of a moral graph, which is obtained from a Bayesian network by connecting (i.e., “marrying”) all parents of every node with undirected arcs and removing the directions from the original arcs. The graph is then triangulated by adding arcs so that every cycle of length greater than three contains a chord. Their algorithm has complexity that is exponential in the size of the largest clique in the triangulated moral graph. To see that the size of such cliques can be bounded when the size of extended ancestral sets is not, consider the family of Bayesian networks having the diamond-shaped form of the network in Figure 5. That is, for each integer k we consider the diamond-shaped network with $k^{2}$ nodes arranged in 2k - 1 columns. The extended ancestral sets of the rightmost node consist of any two consecutive columns of nodes, and they therefore grow without bound as k grows. The moral graph, obtained by adding vertical arcs between adjacent nodes in each column, is already triangulated, and all of its cliques have the constant size three.

$$
N \left(x _ {j} \mid S\right) \leq v \cdot 2 ^ {\Delta}.
$$

## 7. Generation of nonlinear constraints

We now state, in the form of a recursive algorithm, the procedure for generating nonlinear constraints that is described in the previous section.

Call $\text{SPLIT}(x_j, S)$ . [Generate constraints necessary to calculate bounds on $\Pr(x_j | S)$ .]

Procedure SPLIT(R, S). ["Split" a set R of nodes relative to S.]

Split $R$ into $R_{1},\ldots ,R_{m}$ (i.e., partition $R$ into one or more sets

$R_{1},\ldots ,R_{m}$ that are pairwise independent relative to $S$ , where independence is defined in Section 2).

Call CONSTRAIN $(R_{i}, S, R_{i+1} \cup \ldots \cup R_{m})$ for $i = 1, \ldots, m-1$ .

Call EXPAND( $R_{i}, S$ ) for $i = 1, \ldots, m$ .

End SPLIT.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Procedure EXPAND(R, S). [Condition on immediate predecessors of nodes in R relative to S.] Let  $R = \{Y_{1}, \ldots, Y_{r}\}$ , where the  $Y_{j}$ 's are numbered so that  $Y_{i} \notin T(Y_{j})$  when i &lt; j.
If r &gt; 1 then for  $j = 1, \ldots, r$  do:
Let  $\overline{T} = (\{Y_{j+1}, \ldots, Y_{r}\} \cup T(R) \cup S) \setminus T(Y_{j})$ 
If  $\overline{T} \neq \phi$  then call CONSTRAIN( $Y_{j}, T(Y_{j}) \setminus S, \overline{T}$ ).
If  $T(R) \setminus S \neq \phi$  then call  $\text{SPLIT}(T(R) \setminus S, S)$ .
End EXPAND.
</div>

Procedure CONSTRAIN(A, B, C). [Generate nonlinear constraints to enforce $\Pr(A|B, C) = \Pr(A|B)$ .]

Let $A = \{X_1, \ldots, X_a\}$ , $B = \{Y_1, \ldots, Y_b\}$ , $C = \{Z_1, \ldots, Z_c\}$ .

Impose the nonlinear constraints

$$
\operatorname * {P r} (X _ {1} \dots X _ {a} Y _ {1} \dots Y _ {b} Z _ {1} \dots Z _ {c}) \operatorname * {P r} (Z _ {1} \dots Z _ {c})
$$

$$
= \operatorname * {P r} (X _ {1} \dots X _ {a} Y _ {1} \dots Y _ {b}) \operatorname * {P r} (Y _ {1} \dots Y _ {b} Z _ {1} \dots Z _ {c})
$$

for all values of $X_1, \ldots, X_a, Y_1, \ldots, Y_b, Z_1, \ldots, Z_c$ , where $X_i \in \{x_i, \bar{x}_i\}$ , $Y_j \in \{y_j, \bar{y}_j\}$ , $Z_k = \{z_k, \bar{z}_k\}$ , except those constraints for which $(X_1, \ldots, X_a) = (\bar{x}_1, \ldots, \bar{x}_a)$ or $(Z_1, \ldots, Z_c) = (\bar{z}_1, \ldots, \bar{z}_c)$ .

End CONSTRAIN.

## 8. Concluding remarks

We have shown that the inference problem in Bayesian logic can be solved in the form of a nonlinear program in which the number of nonlinear constraints need not grow rapidly with the size of the problem. In particular, the number of constraints grows only linearly in networks whose extended ancestral sets have bounded size. Most of these networks are not singly connected. Also, computational tests performed by others show that column generation methods can limit the variables used to a reasonable number in life-sized probabilistic logic problems, and Benders decomposition allows us to use those same methods in Bayesian logic.

It is unclear at this point which techniques should be used to solve the nonlinear programming problem, and how well they would perform on large problems. One promising feature of the problem is that it can be formulated as a specially structured signomial program that is in fact a geometric program except for one inequality constraint whose sign is the reverse of what it should be $[8,10,11]$ . Geometric, signomial and general nonlinear programming are well developed technologies, and computational testing is necessary to find the best methods for Bayesian logic.

The nonlinear program we must solve is a nonconvex program, and nonconvex programs can in general have several local optima. It is an open question whether a Bayesian logic problem can have local optima with different objective function values. It is also an open question whether all probabilities between the minimum and maximum are necessarily realized by some feasible solution.

Probabilistic logic is sometimes criticized on the ground that one can make inconsistent probability assignments to propositions in a knowledge base. The same of course holds for Bayesian logic. But the possibility of inconsistency is appropriate if each probability assignment represents a judgment that considers all available evidence. In this case assigning a lower probability bound of 0.8 to both a proposition and its negation, for instance, is inconsistent and should not be allowed. It makes no sense to say that, all things considered, a proposition is probably true, and all things considered, it is probably false. On the other hand, if a probability assignment indicates how much support a particular piece of evidence lends to a proposition, then any set of assignments can make sense. It is quite possible that one piece of evidence would weigh heavily in favor (0.8) of a proposition, and another weigh heavily against it. For this sort of application one needs a mechanism for accumulating or combining evidence, such as Dempster's combination rule in Dempster-Shafer theory [35], and one should not use probabilistic or Bayesian logic in the first place. We will not take up the issue as to whether Dempster's rule or any other known mathematical scheme combines evidence in a satisfactory way.

In any case it is straightforward to avoid inconsistent assignments in probabilistic and Bayesian logic. As propositions are added to a knowledge base, one can simply calculate the permissible range of probabilities for each new proposition, and assign it a probability in that range. Even if inconsistent assignments have already been made, Jaumard et al. [24] point out that, in probabilistic logic, the problem of making adjustments to restore consistency (and allowing for the fact that one is more willing to adjust some assignments than others) is itself a linear program similar to that expressing the inference problem. An analogous nonlinear program can be written for Bayesian logic.

Finally, it is sometimes said that probabilistic logic results in probability intervals that are too wide, and that some mechanism should be used to obtain a single probability estimate – such as a maximum entropy estimate, which Nilsson himself proposed [29]. But a maximum entropy calculation introduces computational difficulties into both probabilistic and Bayesian logic. In probabilistic logic it replaces the linear objective function with the nonlinear entropy formula $-\sum_{j}p_{j}\log p_{j}$ . Not only does a linear problem become nonlinear, but column generation is no longer effective, and one must find some other way of dealing with the exponential explosion of variables. In Bayesian logic the nonlinear entropy function becomes the objective function in the Benders subproblem, since it involves the variables $p_{j}$ . Column generation is therefore forfeited as a means of solving the subproblem, where one encounters the same difficulties as when maximizing entropy in ordinary probabilistic logic.

Computational issues aside, it is unclear that this fear of wide probability intervals is based on experience with realistic data bases in which conditional probabilities and independence conditions are specified. (Such additional constraints tend to reduce the size of the probability intervals obtained.) In any case these probability intervals, wide or narrow, provide valuable information, because they represent what can actually be deduced about the probability of an inferred proposition.

## References

[1] Andersen, K.A., On the Chaining Problem in Probabilistic Logic, Publication no. 90/3, Matematisk Institut, University of Aarhus, DK-8000 Aarhus C., Denmark, January 1990.

[2] Benders, J.F., Partitioning Procedures for Solving Mixed Variables Programming Problems, Numerische Mathematik 4 (1962) 238–252.

[3] Boole, G., An Investigation of the Laws of Thought, on which are Founded the Mathematical Theories of Logic and Probabilities, Dover Publications, New York (151). Original work published 1854.

[4] Boole, G., Studies in Logic and Probability, ed. by R. Rhees, Watts & Co, London, and Open Court Publishing Company, La Salle, Illinois (1952).

[5] Brun, T., Structure probabiliste en logique des propositions, Mémoire d'Ingénieur, École des Hautes Études Commerciales, Montréal, Canada (1988).

[6] Chen, S.S., Some Extensions of Probabilistic Logic, in J.F. Lemmer and L.N. Kanal, eds., Uncertainty in Artificial Intelligence 2, North-Holland (1988).

[7] Crama, Y., P. Hansen and B. Jaumard, The Basic Algorithm For Pseudo-Boolean Programming Revised, Discrete Applied Mathematics 29 (1990) 171–186.

[8] Dembo, R.S., Current State of the Art of Algorithms and

Computer Software for geometric Programming, Journal of Optimization Theory and Applications 26 (1978) 149-193.

[9] Dubois, D., and H. Prade, A Tentative Comparison of Numerical Approximate Reasoning Methodologies, International Journal Man-Machine Studies 27 (1987) 709–716.

[10] Ecker, J.G., Geometric Programming: Methods, Computations and Applications, SIAM Review 22 (1980) 338-362.

[11] Ecker, J.G., W. Gochet, and Y. Smeers, Computational Aspects of Geometric Programming: 3. Some Primal and Dual Algorithms for Posynomial and Signomial Geometric Programs, Engineering Optimization 3 (1978) 147–160.

[12] Georgakopoulos, G., D. Kavvadias and C.H. Papadimitriou, Probabilistic Satisfiability, Journal of Complexity 4 (1988) 1–11.

[13] Glover, F., Tabu Search - Part I, ORSA Journal on Computing 1 (1989) 190-206.

[14] Grosof, B.N., An Inequality Paradigm for Probabilistic Reasoning, in J.F. Lemmer and L.N. Kanal, eds., Uncertainty in Artificial Intelligence 1, North-Holland (1986).

[15] Grosof, B.N., Non-monotonicity in Probabilistic Knowledge, in J.F. Lemmer and L.N. Kanal, eds., Uncertainty in Artificial Intelligence 2, North-Holland (1988).

[16] Hailperin, T., Boole's Logic and Probability, Studies in Logic and the Foundations of Mathematics v. 85, North-Holland (176).

[17] Hailperin, T., Probability Logic, Notre Dame Journal of Formal Logic 25 (1984) 198–212.

[18] Hailperin, T., Boole's Logic and Probability, Second Edition, Studies in Logic and the Foundations of Mathematics v. 85, North-Holland (1986).

[19] Hammer, P., and S. Rudeanu, Boolean Methods in Operations Research and Related Areas, Springer-Verlag, Berlin (1968).

[20] Hansen, P., and B. Jaumard, Algorithms for the Maximum Satisfiability Problem, Computing 44 (1990) 279-303.

[21] Hooker, J.N., A Mathematical Programming Model for Probabilistic Logic, working paper 05-88-89, Graduate School of Industrial Administration, Carnegie Mellon University, Pittsburgh, PA 15213 (July 1988).

[22] Hooker, J.N., A Quantitative Approach to Logical Inference, Decision Support Systems 4 (1988) 45–69.

[23] Howard, R.A., and J.E. Matheson, Influence Diagrams, in R.A. Howard and J.E. Matheson, eds., The Principles and Applications of Decision Analysis, v. 2, Strategic Decision Group, Menlo Park, CA (1981).

[24] Jaumard, B., P. Hansen, M.P. de Aragaö, Column generation Methods for Probabilistic Logic, ORSA Journal on Computing 2, no. 3 (1991) 135–148.

[25] Kavvadias, D., and C.H. Papadimitriou, A. Linear Programming Approach to Reasoning about Probabilities, to appear in Annals of Mathematics and Artificial Intelligence.

[26] Lauritzen, S.L. and D.J. Spiegelhalter, Local Computations with Probabilities on Graphical Structures and their Application to Expert Systems, Journal of the Royal Statistical Society B 50 (1988) 157–224.

[27] McLeish, M., Probabilistic Logic: Some Comments and

Possible Use for Nonmonotonic Reasoning, in J.F. Lemmer and L.N. Kanal, eds., Uncertainty in Artificial Intelligence 2, North-Holland (1988).

[28] Minoux, M., Mathematical Programming: Theory and Algorithms, Wiley, New York (1986).

[29] Nilsson, N.J., Probabilistic Logic, Artificial Intelligence 28 (1986) 71–87.

[30] Oliver, R.M. and J.Q. Smith, Influence Diagrams, Belief Nets and decision Analysis, Wiley, Chichester, U.K. (1990).

[31] Paass, G., Probabilistic Logic, in P. Smets et al., eds.

Non-standard Logics for Automated Reasoning, Academic Press, New York (1988) 213–251.

[32] Pearl, J., Fusion, Propagation and Structuring in Belief Networks, Artificial Intelligence 29 (1986) 241–288.

[33] Pearl, J., Probabilistic Reasoning in Intelligent Systems: Networks of Plausible Inference, Morgan Kaufmann, San Mateo, California (1988).

[34] Shachter, R.D., Evaluating influence diagrams, Operations Research 34 (1986) 871–82.

[35] Shafer, G.W., A Mathematical Theory of Evidence, Princeton University Press (1976).
