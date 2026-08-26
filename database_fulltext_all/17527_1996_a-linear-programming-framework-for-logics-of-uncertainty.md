---
otero_id: 17527
otero_key: "GF64CC8B"
title: "A linear programming framework for logics of uncertainty"
authors: "K.A. Andersen; J.N. Hooker"
year: "1996"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(94)00055-7"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# A linear programming framework for logics of uncertainty $^{1}$

K.A. Andersen $^{a,*}$ , J.N. Hooker $^{b}$

$^{a}$ Matematisk Institut, Aarhus Universitet DK-8000 Århus C, Denmark

$^{b}$ Graduate School of Industrial Administration Carnegie Mellon University, Pittsburgh, PA 15213, USA

## Abstract

Several logics for reasoning under uncertainty distribute “probability mass” over sets in some sense. These include probabilistic logic, Dempster-Shafer theory, other logics based on belief functions, and second-order probabilistic logic. We show that these logics are instances of a certain type of linear programming model, typically with exponentially many variables. We also show how a single linear programming package can implement these logics computationally if one “plugs in” a different column generation subroutine for each logic, although the practicality of this approach has been demonstrated so far only for probabilistic logic.

Keywords: Linear programming; Logic; Uncertainty

## 1. Introduction

Several logics for reasoning under uncertainty are variations on a theme. Numbers, perhaps probabilities, are assigned to propositions to indicate degrees of confidence. The object is to determine the degree of confidence one can have in a conclusion inferred from the propositions. Dependencies among the propositions require that some of the “probability mass” assigned to one proposition be distributed to others. Solution of this distribution problem yields a range of confidence levels for the conclusion.

The oldest uncertainty logic of this kind is Boole's probabilistic logic [2,3], which was revived a few years ago by Hailperin [12,13], rediscovered by Nilsson [18], and recently discussed by a number of others [5,8–11,15–17,19]. But Dempster-Shafer theory has a similar structure [20], as does a logic based on Shafer's belief functions suggested by Dubois, Prade and others [7,16,17]. A number of other logics can be devised along similar lines.

It seems to be widely recognized that several uncertainty logics can be viewed as probability mass distribution problems in some sense. Here we not only make this sense precise but show the following; (a) Inference in all these logics can all be formulated as a linear programming problem of a certain type, typically with exponentially many variables in the worst case. (b) At least in the logics discussed here, the exponential number of variables can be dealt with computationally by using column generation schemes, a well known device for such situations. The practicality of this approach has already been demonstrated for probabilistic logic [15]. This suggests that a single linear programming code can implement several uncertainty logics, if one plugs in a different column generation subroutine for each logic. Computational testing, however, has not been carried out on logics other than probabilistic logic.

We will show how several logics fit into this framework and will describe the column generation subproblem in each case. In probabilistic logic, column generation is a pseudo-boolean optimization problem, as is already well known. In Dempster-Shafer theory it is an integer programming problem. We will introduce a second-order probability logic in which it is a mixed integer/linear programming problem. In the logic of belief functions mentioned above, there is no exponential explosion of columns, and a column generation technique is likely to be unnecessary.

For some applications one may wish to add nonlinear constraints, although we do not pursue this possibility here. For instance, Dempster's combination rule, which is a key ingredient of Dempster-Shafer theory, combines a renormalization device with an independence assumption. The rule can be used perfectly well, and in many cases more appropriately, without the independence assumption, and we do so here. But the independence assumption can be imposed by adding nonlinear constraints to the otherwise linear model. Probabilistic logic can also be augmented with independence assumptions, such as those depicted by a Bayesian network, by adding nonlinear constraints. In [1] we show when and how this can be done without an exponential growth in the number of nonlinear constraints. It is unclear at this point whether column generation techniques may be successfully extended to nonlinear problems.

We begin below with a statement of the general linear programming model. After discussing briefly how a column generation approach is implemented computationally, we show how several logics can be placed in this framework. These include probabilistic logic, a version of probabilistic logic with unreliable sources of information, Dempster-Shafer theory, second-order probabilistic logic (which allows for unreliable sources in a different way), and a simple logic of belief functions. The expositions is clarified by using some small examples.

## 2. The general model

We are given propositions $F_{1},\ldots,F_{h}$ and some information about the level of confidence we may have in them. The confidence level for $F_{i}$ is indicated by its “mass,” which is a number in the interval [0,1]. The interpretation of mass varies from one logic to another; in probabilistic logic, for instance, it is probability mass in the classical sense. Since the precise mass of $F_{i}$ may be unknown, we will suppose that an interval $[L_{i},U_{i}]$ is given, within which the mass lies. If nothing is known about the mass of $F_{i}$ , we set $L_{i}=0$ , $U_{i}=1$ .

Let $S_{i}$ be the set of possible outcomes that make proposition $F_{i}$ true. In probabilistic logic, $S_{i}$ is the set of “possible worlds” in which $F_{i}$ is true. In Dempster-Shafer theory, it is a subset of the “frame of discernment.” We let $\mu(S_{i})$ denote the mass of $F_{i}$ , which we also refer to as the mass of $S_{i}$ . The sets $S_{1},\ldots,S_{h}$ need not all be distinct.

We are interested in knowing how much confidence we can place in a proposition $F_{t}$ whose mass is not given. Its mass may be constrained by the fact that $S_{t}$ intersects some of the sets for which masses are given. In other words, $F_{t}$ may be logically related to $F_{1},\ldots,F_{h}$ . A fundamental problem, therefore, is to find out how much of the mass assigned a set $S_{i}$ can or must be associated with other sets.

## 2.1. Example 1

Suppose we assign masses 0.8 and 0.7 respectively to propositions $F_{1}$ and $F_{2}$ and wish to infer something about the mass of a third proposition $F_{3}$ . The logical relations among the propositions are indicated by the relations among the sets $S_{1}, S_{2}, S_{3}$ depicted in Fig. 1. For instance, the figure implies that $F_{1}$ and $F_{2}$ can both be true (since $S_{1}$ and $S_{2}$ intersect), and if they are both true, $F_{3}$ must also be true (since all outcomes in $S_{1} \cap S_{2}$ are in $S_{3}$ ).

The mass 0.8 assigned $S_{1}$ can be regarded as lying in $S_{1}$ 's circle. Some of this mass may lie in $S_{3}$ 's circle, and similarly for the mass of 0.7 assigned $S_{2}$ . The inference problem is to determine the minimum and maximum mass that may lie in the $S_{3}$ circle. It is therefore a mass distribution problem.

![](/api/attachments/GF64CC8B/fulltext/images/96dfc8c554201e34529810a70be44f003f8c4f8d6a954921e10249b1bc8a17d1.jpg)  
Fig. 1. Relations among the sets $S_1$ , $S_2$ and $S_3$ .

For reasons that will become evident as we examine particular logics, we will formulate this problem as one of distributing each set's mass over its intersections with other sets. For convenience let us write the intersection $\cap_{i\in J}S_i$ as $S_j$ . Then we wish to distribute each $S_i$ 's mass over $S_i$ 's intersections $S_J$ with other sets. Or more precisely, we will distribute $S_i$ 's mass over the index sets $J$ that indicate which sets are intersected. The two are not the same, because possibly $S_J = S_{J'}$ when $J\neq J'$ . In Fig. 1, for instance, $S_{\{1,2\}} = S_{\{1,2,3\}}$ . The notion of distributing mass over index sets may seem odd at this point, but it is one of the keys to unifying logics of uncertainty.

The precise distribution problem varies from logic to logic because the structure of the logic dictates which index sets J may receive mass. We will show how the distribution problem of Fig. 1 would be formulated in probabilistic logic, and then how it would be formulated in Dempster-Shafer theory. We will explain the motivation for these formulations in the ensuing sections of the paper. Our sole purpose here is to illustrate that the distribution problem can be formulated in different ways.

## 2.2. Example 1; Probabilistic interpretation

In probabilistic logic we view the 0.8 mass assigned $S_{1}$ as distributed over the three regions of the $S_{1}$ circle in Fig. 1, and similarly for $S_{2}$ . One possible distribution is shown in the figure. Once a distribution of this sort is specified, the mass inside $S_{3}$ is determined.

To view this as distribution of mass over intersections, we add propositions $F_{4}, \ldots, F_{7}$ to the original three, where $F_{4}, F_{5}, F_{6}$ are respectively $\neg F_{1}, \neg F_{2}, \neg F_{3}$ , and $F_{7}$ is a tautology. $S_{4}, S_{5}, S_{6}$ are therefore the complementary sets $\overline{S}_{1}, \overline{S}_{2}, \overline{S}_{3}$ , respectively. We also assign mass 1 to the tautology.

The distribution problem just described is equivalent to distributing each $S_{i}$ 's mass over the sets J for which $S_{J}$ is one of the regions into which $S_{i}$ is divided in Fig. 1. Thus the 0.8 mass of $S_{1}$ is distributed over the index sets $\{1,2,3\},\{1,5,3\},\{1,5,6\}$ , which correspond to the three regions of the $S_{1}$ circle, namely $S_{\{1,2,3\}} = S_{1} \cap S_{2} \cap S_{3}$ , $S_{\{1,5,3\}} = S_{1} \cap \overline{S}_{2} \cap S_{3}$ , and $S_{\{1,5,6\}} = S_{1} \cap \overline{S}_{2} \cap \overline{S}_{3}$ .

Let $q_{J}$ be the mass distributed to J. Then in general we have,

$$
\mu (S _ {i}) = \sum_ {J \in I (i)} q _ {J},\tag{1}
$$

where $I(i) \subset I$ is the family of index sets over which the mass $\mu(S_{i})$ of $S_{i}$ is to be distributed. Since $\mu(S_{i})$ must lie in $[L_{i}, U_{i}]$ , we have the constraints,

$$
L _ {i} \leq \mu (S _ {i}) \leq U _ {i}, i = 1, \dots , m.\tag{2}
$$

$$
q _ {J} \geq 0, \text {   all   } J \in I,\tag{3}
$$

where $\mu(S_i)$ is given by (1).

We can place bounds on the mass of $S_{t}$ by solving the two optimization problems,

$$
\min / \max \frac {\mu^ {*} (S _ {t})}{1 - \mu^ {*} (\emptyset)} \text {   s.t.   } (2), (3).\tag{4}
$$

The notation $\mu^{*}(S_{t})$ is used to indicate that mass may be distributed differently in the objective function than in the constraints. Thus we have,

$$
\mu^ {*} (S _ {t}) = \sum_ {J \in I ^ {*} (t)} q _ {J},\tag{5}
$$

where the index set $I^{*}(t)$ depends on the logic.

## 2.3. Example 1; Probabilistic interpretation, continued

In the probabilistic logic interpretation, the mass $\mu(S_{1})=0.8$ is distributed over the index sets in $I(1)=\{\{1,2,3\},\{1,5,3\},\{1,5,6\}\}$ . So,

$$
\mu (S _ {1}) = q _ {\{1, 2, 3 \}} + q _ {\{1, 5, 3 \}} + q _ {\{1, 5, 6 \}},
$$

and similarly for $\mu(S_{2})$ . The unknown mass $\mu^{*}(S_{3})$ is distributed in the same way. No mass is assigned to the empty set, so that $\mu^{*}(\varnothing)=0$ . So the optimization problems (4) become,

$$
\begin{array}{l} \min / \max q _ {\{1, 2, 3 \}} + q _ {\{1, 5, 3 \}} + q _ {\{4, 2, 3 \}} + q _ {\{4, 5, 3 \}} \\ \text {s.t.} 0. 8 \leq q _ {\{1, 2, 3 \}} + q _ {\{1, 5, 3 \}} + q _ {\{1, 5, 6 \}} \leq 0. 8 \\ 0. 7 \leq q _ {\{1, 2, 3 \}} + q _ {\{4, 2, 3 \}} + q _ {\{4, 2, 6 \}} \leq 0. 7 \\ 1 \leq q _ {\{1, 2, 3 \}} + q _ {\{4, 2, 3 \}} + q _ {\{1, 5, 3 \}} + q _ {\{4, 5, 3 \}} \\ \quad + q _ {\{4, 2, 6 \}} + q _ {\{1, 5, 6 \}} + q _ {\{4, 5, 6 \}} \leq 1 \\ q _ {J} \geq 0 \end{array}
$$

It is easy to see that the distribution in Fig. 1, in which $\mu(S_3) = 0.5$ , minimizes $\mu(S_3)$ . The maximum value of $\mu(S_3)$ is 1, obtained by setting $(q_{\{1,2,3\}}, q_{\{1,5,3\}}, q_{\{4,2,3\}}) = (0.5, 0.3, 0.2)$ .

## 2.4. Example 1; Dempster-Shafer interpretation

In Dempster-Shafer theory, the mass 0.8 assigned $S_{1}$ is divided into a) mass that lies specifically in $S_{1} \cap S_{2} \cap S_{3}$ b) additional mass that could lie anywhere in $S_{1} \cap S_{2}$ c) additional mass that could lie anywhere in $S_{1} \cap S_{3}$ and d) additional mass that could lie anywhere in $S_{1}$ . (In this example, it happens that $S_{1} \cap S_{2} = S_{1} \cap S_{2} \cap S_{3}$ .) So $\mu(S_{1}) = 0.8$ is distributed among $q_{\{1\}}$ , $q_{\{1,2\}}$ , $q_{\{1,3\}}$ , $q_{\{1,2,3\}}$ . Also we add a tautology to the original three propositions and assign it mass 1.

Unlike probabilistic logic, Dempster-Shafer theory distributes the inferred mass $\mu^{*}(S_{\mathrm{t}})$ differently than the given masses $\mu(S_{\mathrm{i}})$ . Here $\mu^{*}(S_{3})$ is regarded as the sum of masses distributed to $J$ 's for which $S_{J} \subset S_{3}$ . Since $S_{3}, S_{1} \cap S_{2}, S_{1} \cap S_{3}, S_{2} \cap S_{3}$ and $S_{1} \cap S_{2} \cap S_{3}$ are all subsets of $S_{3}$ , $\mu^{*}(S_{3})$ is distributed to the index sets in $I^{*}(3) = \{\{3\}, \{1,2\}, \{1,3\}, \{2,3\}, \{1,2,3\}\}$ . Here $\mu^{*}(\emptyset) = 0$ because none of the intersections $S_{J}$ is a subset of the empty set.

The optimization problems (4) become,

$$
\begin{array}{l} \min / \max \frac {q _ {\{3 \}} + q _ {\{1 , 2 \}} + q _ {\{1 , 3 \}} + q _ {\{2 , 3 \}} + q _ {\{1 , 2 , 3 \}}}{1 - 0} \\ \text {s.t.} 0. 8 \leq q _ {\{1 \}} + q _ {\{1, 2 \}} + q _ {\{1, 3 \}} + q _ {\{1, 2, 3 \}} \leq 0. 8 \\ 0. 7 \leq q _ {\{2 \}} + q _ {\{1, 2 \}} + q _ {\{2, 3 \}} + q _ {\{1, 2, 3 \}} \leq 0. 7 \\ 1 \leq q _ {\emptyset} + q _ {\{1 \}} + q _ {\{2 \}} + q _ {\{3 \}} + q _ {\{1, 2 \}} + q _ {\{1, 3 \}} + q _ {\{2, 3 \}} \\ \quad + q _ {\{1, 2, 3 \}} \leq 1 \\ q _ {J} \geq 0 \end{array}
$$

(The variable $q_{\varnothing}$ represents mass that is assigned to no particular set.) It happens that $\mu^{*}(S_{3})$ is restricted to the same interval as in the probabilistic interpretation, namely [0.5,1]. It is 0.5 when $(q_{\{1\}}, q_{\{2\}}, q_{\{1,2\}}) = (0.3, 0.2, 0.5)$ . It is 1 when $(q_{\{3\}}, q_{\{1,2\}}, q_{\{1,3\}}) = (0.2, 0.7, 0.1)$ .

Note that the objective function in (4) is normalized by dividing by the mass that is not assigned to the empty set. Among the logics we discuss, this plays a role only in Dempster-Shafer theory. (In the above example, $\mu^{*}(\emptyset)$ happened to be zero.) In the other logics, no mass is assigned to the empty set, so that $\mu^{*}(\emptyset)=0$ and (4) is a linear programming problem. When $\mu^{*}(\emptyset)\neq0$ , (4) becomes a fractional programming problem that is readily transformed to a linear programming problem using well-known methods [4].

The sets $I(i)$ and $I^{*}(t)$ give instructions for generating the columns of the coefficient matrix in (4). Each column corresponds to a set $J \in I$ . Assuming $\mu^{*}(\emptyset) = 0$ , it has the form $(y_{0}, y_{1}, \ldots, y_{m})$ , where $y_{i} (i \geq 1)$ is the coefficient of $q_{J}$ in constraint $i$ and $y_{0}$ its coefficient in the objective function. The column is given by,

$$
\begin{array}{l} y _ {i} = \left\{ \begin{array}{l l} 1 & \text {if} J \in I (i) \\ 0 & \text {otherwise,} \end{array} \right. i = 1, \ldots , m, \\ y _ {0} = \left\{ \begin{array}{l l} 1 & \text {if} J \in I ^ {*} (t) \\ 0 & \text {otherwise.} \end{array} \right. \end{array}\tag{6}
$$

A similar column definition can be given for the linearized version of (4) when $\mu^{*}(\varnothing)\neq0$ .

<table><tr><td></td><td>Probabilistic logic</td><td>Dempster-Shafer theory</td><td>2nd-order probabilistic logic</td><td>Belief functions</td></tr><tr><td>Interpretation of set  $S_i$ </td><td>Set of possible worlds in which proposition $F_i$  is true</td><td>Subset of frame of discernment associated with some evidence source k</td><td>Half-space in probability space defined by  $Pr(F_i) \leq \pi$ </td><td>Subset of frame of discernment</td></tr><tr><td>Constraints, where $\mu(S_i) = \sum_{J \in I(i)} q_J$ </td><td>Bounds on prior probabilities1: $L \leq \mu(S_i) \leq U$ </td><td>Value of basic probability function: $\mu(S_i) = m_k(S_i)$ </td><td>Bounds on 2nd-order probability that  $Pr(F_i) \leq \pi: L \leq \mu(S_i) \leq U$ </td><td>Bounds on value of belief function  $Bel(S_i): L \leq \mu(S_i) \leq U$ </td></tr><tr><td>Objective function, where $\mu^*(S_i) = \sum_{J \in I^{*}(i)} q_J$ </td><td>Posterior probability: $\frac{\mu^*(S_i \cap S_{c(i)})}{\mu^*(S_{c(i)})}$ </td><td>Normalized probability:  $\frac{\mu^*(S_t)}{1 - \mu^*(\emptyset)}$ </td><td>2nd-order probability that  $Pr(F_i) \leq \pi: \mu^*(S_t)$ </td><td>Value of belief function  $Bel(S_t): \mu^*(S_t)$ </td></tr><tr><td>Intersections  $S_J = \cap_{i \in J} S_i$ </td><td>All minimal2nonempty intersections of sets  $S_i$ </td><td>All intersections of one  $S_i$  associated with each evidence source k</td><td>All minimal nonempty intersections of half-spaces  $S_i$ </td><td>The sets  $S_i$ </td></tr><tr><td>I(i) contains all J for which:I*(i) contains all J for which:Practical generationof columns  $q_J$ </td><td> $S_J \subset S_i$  $S_J \subset S_i$ Pseudo-boolean optimization</td><td> $i \in J$  $S_J \subset S_i$ Integer programming</td><td> $S_J \subset S_i$  $S_J \subset S_i$ Mixed integer programming</td><td> $S_J \subset S_i$  $S_J \subset S_i$ None required</td></tr><tr><td colspan="5">1Can also place bounds on conditional probabilities  $L_i \leq Pr(F_i | F_{c(i)}) \leq U_i$  by using the constraints  $L_i \mu(S_{c(i)}) \leq \mu(S_i \cap S_{c(i)})$  and  $U_i \mu(S_{c(i)}) \leq \mu(S_i \cap S_{c(i)})$ .2A minimal intersection  $S_J$  is one containing no other nonempty intersection of  $S_i$ &#x27;s.</td></tr></table>

Logics that use conditional probabilities require a model in which the masses in (4) are replaced with “conditional masses.” A conditional mass $\mu(S|T)$ is defined to be equal to $\mu(S\cap T)/\mu(T)$ . Intervals $[L_{i}, U_{i}]$ are given for conditional masses $\mu(S_{i}|S_{c(i)})$ , where $S_{c(i)}$ is one of the sets $S_{1},\ldots,S_{h}$ . Thus the constraints (2) become,

$$
L _ {i} \leq \frac {\mu (S _ {i} \cap S _ {c (i)})}{\mu (S _ {c (i)})} \leq U _ {i}.
$$

These constraints can be written in linear form,

$$
\begin{array}{l} 0 \leq \mu \big (S _ {i} \cap S _ {c (i)} \big) - L _ {i} \mu \big (S _ {c (i)} \big) \\ \mu \big (S _ {i} \cap S _ {c (i)} \big) - U _ {i} \mu \big (S _ {c (i)} \big) \leq 0. \end{array}\tag{7}
$$

Assuming $\mu^{*}(\emptyset)=0$ , the linear programming problem (4) becomes a fractional programming problem,

$$
\min / \max \frac {\mu^ {*} \left(S _ {t} \cap S _ {c (t)}\right)}{\mu^ {*} \left(S _ {c (t)}\right)}
$$

s.t. (7), (3).

(8)

This is again convertible to a linear programming problem.

When the objective function of (8) is an unconditional mass $\mu^{*}(S_{t})$ , column J of (8) has the form $(y_{0}, y_{1}, z_{1}, \ldots, y_{m}, z_{m})$ , where

$$
y _ {i} = \left\{ \begin{array}{c c} 1 - L _ {i} & \text {if} J \in I (i) \cap I (c (i)) \\ - L _ {i} & \text {if} J \in I (c (i)) \setminus I (i), i = 1, \ldots , m, \\ 0 & \text {otherwise} \end{array} \right.
$$

$$
z _ {i} = \left\{ \begin{array}{l l} 1 - U _ {i} & \text { if } J \in I (i) \cap I (c (i)) \\ - U _ {i} & \text { if } J \in I (c (i)) \setminus I (i), i = 1, \ldots , m, \\ 0 & \text { otherwise }, \end{array} \right.\tag{9}
$$

$$
y _ {o} = \left\{ \begin{array}{l l} 1 & \text { if } J \in I ^ {*} (t) \\ 0 & \text { otherwise } \end{array} \right.
$$

When the objective function is conditional, a similar column definition can be given for the linearized form of (8).

Table 1 shows how the four uncertainty logics considered here fit into this pattern.

## 3. The column generation subproblem

We have the model

$$
\begin{array}{l} \min / \max \mu^ {*} (S _ {t}) = \sum_ {J \in I ^ {*} (t)} q _ {J} \\ \text {s.t.} \mu (S _ {i}) = \sum_ {J \in I (i)} q _ {J} \leq U _ {i}, i = 1, \dots , m. \\ \mu (S _ {i}) = \sum_ {J \in I (i)} q _ {J} \geq L _ {i}, i = 1, \dots , m. \\ q _ {J} \geq 0, J \in I \end{array}\tag{10}
$$

In general, depending on the logic, there can be an exponential number of columns in the above program. Therefore it might be a good idea to use a column generation procedure. For an introduction to column generation procedures, especially Dantzig-Wolfe, see [6]. Assume that we have only generated some columns

$$
\begin{array}{l} \min / \max \mu^ {*} S _ {t} = \sum_ {J \in \bar {I} ^ {*} (t)} q _ {J} \\ \text {s.t.} \mu (S _ {i}) = \sum_ {J \in \bar {I} (i)} q _ {J} \leq U _ {i}, i = 1, \dots , m. \\ \mu (S _ {i}) = \sum_ {J \in \bar {I} (i)} q _ {J} \geq L _ {i}, i = 1, \dots , m. \\ q _ {J} \geq 0, J \in \bar {I} \end{array}\tag{11}
$$

Here the index sets $\bar{I}^{*}(t)$ , $\bar{I}(i)$ and $\bar{I}$ denote the set of columns generated so far. What we need now is to determine if the above columns are sufficient for solving the program and if not how a new (improving) column may be generated. This is usually done by constructing a subproblem. By maximizing or minimizing a certain objective function over some set, it is possible to decide if an improving column does exist. If one exists it is added to the program which is then resolved. If no improving column exists the optimal solution to the program has been found. The procedure can be started with any set of known columns, possibly none, in which case the program only contains slack- and surplus variables in the constraints.

To describe the column generation procedure suppose we are maximizing the programs (10)

and (11). The procedure is similar when minimizing. Let $\lambda_{i}, i = 1, \ldots, m$ , denote the dual variables to the constraints $\sum_{J \in \bar{I}(i)} q_{J} \leq U_{i}$ , and let $\gamma_{i}, i = 1, \ldots, m$ , denote the dual variables to the constraints $\sum_{J \in \bar{I}(i)} q_{J} \geq L_{i}$ . Then $\lambda_{i} \geq 0$ and $\gamma_{i} \leq 0$ , $i = 1, \ldots, m$ . Suppose we construct a set, say $P$ , such that the extreme points of $P$ are exactly the possible columns $q_{J}, J \in I$ . Then the subproblem becomes:

$$
\min (\lambda - \gamma) y - y _ {0}
$$

s.t.

$$
y = \left(y _ {1}, \dots , y _ {m}\right) \in P\tag{12}
$$

where $\lambda = (\lambda_1, \ldots, \lambda_m)$ and $\gamma = (\gamma_1, \ldots, \gamma_m)$ .

If the optimal solution to this problem is strictly less than 0, then an improving column $q_{J}$ has been found. The index J is added to the index sets $\bar{I}^{*}(t)$ , $\bar{I}(i)$ and $\bar{I}$ , meaning that column $q_{J}$ is added to the program (11), which is then resolved. If the optimal solution to the contrary is at least 0, then an optimal solution to (10) has been determined. We notice that the problem is in a sense to state the set P in a reasonable way. For the logics described in this paper the sets P are described in Sections 4–7.

## 4. Probabilistic logic

In probabilistic logic, conditional probabilities $Pr(F_{i}|F_{c(i)})$ are constrained to lie in intervals $[L_{i}, U_{i}]$ , where the $F_{i}$ 's are formulas of propositional logic. (An unconditioned probability $Pr(F_{i})$ can be given by letting $F_{c(i)}$ be a tautologous proposition.) The object is to compute bounds on a probability mass $Pr(F_{t}|F_{c(i)})$ that are consistent with the given probabilistic information.

The formulas $F_{i}$ contain atomic propositions $x_{1},\ldots,x_{n}$ . A possible world is an assignment $v:\{x_{1},\ldots,x_{n}\}\to\{0,1\}^{n}$ of truth values to the atomic propositions. $F_{i}$ is true in a possible world v when the assignment v makes it true, which we indicate by writing $v(F_{i})=1$ .

Let $S_{i}$ be the set of possible worlds in which $F_{i}$ is true. Thus $Pr(F_{i})$ is the probability that the actual world lies in $S_{i}$ . We therefore interpret $\mu(S_i)$ to be the probability $Pr(F_i)$ and $\mu(S_i|S_{c(i)})$ to be the conditional probability $Pr(F_i|F_{c(i)})$ .

The given intervals $[L_{i}, U_{i}]$ impose the constraints (7). Since the probability of all possible worlds must sum to one, we use one of the constraints (7) to assign a mass of one to a tautologous proposition.

By the law of total probability, $\mu(S_{i})$ is the sum of the probabilities of the possible worlds in $S_{i}$ . The probability mass $\mu(S_{i})$ must therefore be distributed over these worlds. If we let $q_{v}$ denote the probability of world v, we have

$$
\mu (S _ {i}) = \mu^ {*} (S _ {i}) = \sum_ {v (S _ {i}) = 1} q _ {v}.\tag{13}
$$

The interference problem is to place bounds on a conditional probability $Pr(F_{t}|F_{c(t)})$ . Thus we solve (8), where $\mu$ and $\mu^{*}$ are given by (13).

## 4.1. Example 2

We now give a small example. Suppose we have the following information:

$$
\begin{array}{l} P r (x _ {1}) \in [ L _ {1}, U _ {1} ] \\ P r (x _ {1} \to x _ {2}) \in [ L _ {2}, U _ {2} ] \\ P r (x _ {2} \to x _ {3}) \in [ L _ {3}, U _ {3} ] \\ P r (x _ {3} | x _ {1} \wedge x _ {2}) \in [ L _ {4}, U _ {4} ] \end{array}
$$

where $x_{1}$ , $x_{2}$ and $x_{3}$ are atomic propositions. We are interested in computing the bounds on $Pr(x_{3})$ , given the above information.

In this case:

$$
\begin{array}{l}F _ {1} = \left\{x _ {1} \right\}, F _ {2} = \left\{x _ {1} \rightarrow x _ {2} \right\}, F _ {3} = \left\{x _ {2} \rightarrow x _ {3} \right\},\\F _ {4} = \left\{x _ {3} \right\}, F _ {c (4)} = \left\{x _ {1} \wedge x _ {2} \right\}, F _ {t} = \left\{x _ {3} \right\}\end{array}
$$

Truth table for Example 2

<table><tr><td> $(x_{1},x_{2},x_{3})$ </td><td>Probability</td><td> $x_{1}\rightarrow x_{2}$ </td><td> $x_{2}\rightarrow x_{3}$ </td><td> $x_{1}\wedge x_{2}$ </td></tr><tr><td>(0,0,0)</td><td> $p_{1}$ </td><td>1</td><td>1</td><td>0</td></tr><tr><td>(0,0,1)</td><td> $p_{2}$ </td><td>1</td><td>1</td><td>0</td></tr><tr><td>(0,1,0)</td><td> $p_{3}$ </td><td>1</td><td>0</td><td>0</td></tr><tr><td>(0,1,1)</td><td> $p_{4}$ </td><td>1</td><td>1</td><td>0</td></tr><tr><td>(1,0,0)</td><td> $p_{5}$ </td><td>0</td><td>1</td><td>0</td></tr><tr><td>(1,0,1)</td><td> $p_{6}$ </td><td>0</td><td>1</td><td>0</td></tr><tr><td>(1,1,0)</td><td> $p_{7}$ </td><td>1</td><td>0</td><td>1</td></tr><tr><td>(1,1,1)</td><td> $p_{8}$ </td><td>1</td><td>1</td><td>1</td></tr></table>

Let $(p_{1},\ldots,p_{8})$ denote the probabilities of the eight possible worlds $(x_{1},x_{2},x_{3})$ as shown in Table 2.

Now let us write the usual LP for determining the bounds on the probability of the atomic proposition $x_{3}$ .

$\min / \max p_{2} + p_{4} + p_{6} + p_{8}$

s.t.

$$
\left\{ \begin{array}{c c c c c c c c} 0 & 0 & 0 & 0 & 1 & 1 & 1 & 1 \\ 1 & 1 & 1 & 1 & 0 & 0 & 1 & 1 \\ 1 & 1 & 0 & 1 & 1 & 1 & 0 & 1 \\ 0 & 0 & 0 & 0 & 0 & 0 & - U _ {4} & (1 - U _ {4}) \\ 0 & 0 & 0 & 0 & 1 & 1 & 1 & 1 \\ 1 & 1 & 1 & 1 & 0 & 0 & 1 & 1 \\ 1 & 1 & 0 & 1 & 1 & 1 & 0 & 1 \\ 0 & 0 & 0 & 0 & 0 & 0 & - L _ {4} & (1 - L _ {4}) \\ 1 & 1 & 1 & 1 & 1 & 1 & 1 & 1 \end{array} \right\} \left\{ \begin{array}{l} p _ {1} \\ p _ {2} \\ p _ {3} \\ p _ {4} \\ p _ {5} \\ p _ {6} \\ p _ {7} \\ p _ {8} \end{array} \right\} \stackrel {{\leq}} {{=}} \left\{ \begin{array}{l} U _ {1} \\ U _ {2} \\ U _ {3} \\ 0 \\ L _ {1} \\ L _ {2} \\ L _ {3} \\ 0 \\ 1 \end{array} \right\}
$$

$$
p _ {i} \geq 0, i = 1, \dots , 8
$$

Note that to solve this program it is not necessary to distinguish between the probabilities $p_{2}$ and $p_{4}$ . The two columns they represent are identical, so that in this case it is sufficient to use seven probabilities.

We now show that probabilistic logic fits the general model of the previous section. Whenever an interval, $[L_{i}, U_{i}]$ is given for $Pr(F_{i})$ , the interval $[1 - U_{i}, 1 - L_{i}]$ is implicitly given for $Pr(\neg F_{i})$ . We therefore assume without harm that $\neg F_{i}$ belongs to the list $F_{1}, \ldots, F_{h}$ whenever $F_{i}$ does; that is, the complement $\overline{S}_{i}$ of $S_{i}$ belongs to the list $S_{1}, \ldots, S_{h}$ whenever $S_{i}$ does. Since the probability mass attributed to a set is spread over the possible worlds in the set, empty sets cannot receive probability mass.

The intersections $S_{J}, J \in I$ , are all minimal nonempty intersections of $S_{1}, \ldots, S_{h}$ . A minimal intersection $S_{J}$ is one that properly contains no nonempty intersection. More precisely,

$$
\begin{array}{c} I = \left\{J \subset \{1, \dots , h \} | S _ {J} \neq \emptyset \text {   and   } S _ {J ^ {\prime}} \not \subset S _ {J} \text {   for   all   } \right. \\ J ^ {\prime} \subset \{1, \dots , h \} \end{array}
$$

Due to the fact that $\overline{S}_{i}$ is among $S_{i},\ldots,S_{h}$ whenever $S_{i}$ is, the distinct intersections $S_{J}$ for J ∈ I partition the set of all possible worlds. Note that $S_{i}$ may contain $S_{J}$ when $i\notin J$ . To distribute the probabilities $Pr(S_{i})$ over the $q_{J}$ 's as in (1), we let

$$
I (i) = \left\{J \in I | S _ {J} \subset S _ {i} \right\}.\tag{14}
$$

We must now show that distributing probability over the variables $q_{J}$ as in (1) results in the same problem (8) as distributing it over possible world probabilities $q_{v}$ as in (13). We can do this by showing that (8) has the same columns in either case. Note first that for any $J \in I$ , $q_{J}$ occurs in a constraint or objective function of (8) with a given coefficient if and only all variables $q_{J'}$ with $S_{J'} = S_{J}$ occur with that coefficient. These variables can therefore be collapsed into one, say $q_{J}$ , which represents the set $S_{J}$ in the partition of possible worlds. But the column corresponding to $q_{J}$ is identical to that for $q_{v}$ , where v is any possible world in $S_{J}$ . Thus the possible worlds v generate the same column as the sets J.

## 4.2. Example 2, continued

In this case the sets $S_{i}$ 's are as follows:

$$
\begin{array}{l} S _ {1} = \{(1, 0, 0), (1, 0, 1), (1, 1, 0), (1, 1, 1) \} \\ S _ {2} = \{(0, 0, 0), (0, 0, 1), (0, 1, 0), (0, 1, 1), (1, 1, 0), \\ \quad (1, 1, 1) \} \\ S _ {3} = \{(0, 0, 0), (0, 0, 1), (0, 1, 1), (1, 0, 0), (1, 0, 1), \\ \quad (1, 1, 1) \} \\ S _ {4} = \{(0, 0, 1), (0, 1, 1), (1, 0, 1), (1, 1, 1) \} \\ S _ {c (4)} = \{(1, 1, 0), (1, 1, 1) \} \\ S _ {t} = S _ {4} \end{array}
$$

The minimal intersections $S_{J}$ of the sets $S_{1}$ , $S_{2}$ , $S_{3}$ , $S_{4}$ , $S_{c(4)}$ , $\overline{S}_{1}$ , $\overline{S}_{2}$ , $\overline{S}_{3}$ , $\overline{S}_{4}$ and $S_{c(4)}$ are given by:

$$
\begin{array}{l} S _ {J _ {1}} = \overline {{S}} _ {1} \cap S _ {3} \cap \overline {{S}} _ {4} = \{(0, 0, 0) \} \\ S _ {J _ {2}} = \overline {{S}} _ {1} \cap S _ {4} = \{(0, 0, 1), (0, 1, 1) \} \\ S _ {J _ {3}} = \overline {{S}} _ {3} \cap S _ {c _ {(4)}} = \{(0, 1, 0) \} \\ S _ {J _ {4}} = \overline {{S}} _ {2} \cap \overline {{S}} _ {4} = \{(1, 0, 0) \} \\ S _ {J _ {5}} = \overline {{S}} _ {2} \cap S _ {4} = \{(1, 0, 1) \} \end{array}
$$

$$
S _ {J _ {6}} = \overline {{{{S}}}} _ {3} \cap \overline {{{{S}}}} _ {c _ {(4)}} = \{(1, 1, 0) \}
$$

$$
S _ {J _ {7}} = S _ {3} \cap S _ {c _ {(4)}} = \{(1, 1, 1) \}
$$

We notice that the set I is given by:

$$
I = \left\{J _ {1}, J _ {2}, J _ {3}, J _ {4}, J _ {5}, J _ {6}, J _ {7} \right\}
$$

Furthermore we have

$$
\begin{array}{l} I (1) = \left\{J \in I | S _ {J} \subset S _ {1} \right\} = \left\{J _ {4}, J _ {5}, J _ {6}, J _ {7} \right\} \\ I (2) = \left\{J \in I | S _ {J} \subset S _ {2} \right\} = \left\{J _ {1}, J _ {2}, J _ {3}, J _ {6}, J _ {7} \right\} \\ I (3) = \left\{J \in I | S _ {J} \subset S _ {3} \right\} = \left\{J _ {1}, J _ {2}, J _ {4}, J _ {5}, J _ {7} \right\} \\ I (4) = \left\{J \in I | S _ {J} \subset S _ {\angle} \right\} = \left\{J _ {2}, J _ {5}, J _ {7} \right\} \\ I (c (4)) = \left\{J \in I | S _ {J} \subset S _ {c (4)} \right\} = \left\{J _ {6}, J _ {7} \right\} \\ I (t) = \left\{J \in I | S _ {J} \subset S _ {t} \right\} = \left\{J _ {2}, J _ {5}, J _ {7} \right\} \end{array}
$$

If we formulate the program (8) using the descriptions of the columns (9), the problem below is obtained:

$\min / \max q_{J_2} + q_{J_5} + q_{J_7}$

s.t.

$$
\left( \begin{array}{c c c c c c c} 0 & 0 & 0 & 1 & 1 & 1 & 1 \\ 1 & 1 & 1 & 0 & 0 & 1 & 1 \\ 1 & 1 & 0 & 1 & 1 & 0 & 1 \\ 0 & 0 & 0 & 0 & 0 & - U _ {4} & (1 - U _ {4}) \\ 0 & 0 & 0 & 1 & 1 & 1 & 1 \\ 1 & 1 & 1 & 0 & 0 & 1 & 1 \\ 1 & 1 & 0 & 1 & 1 & 0 & 1 \\ 0 & 0 & 0 & 0 & 0 & - L _ {4} & (1 - L _ {4}) \\ 1 & 1 & 1 & 1 & 1 & 1 & 1 \end{array} \right) \left( \begin{array}{c} q _ {J _ {1}} \\ q _ {J _ {2}} \\ q _ {J _ {3}} \\ q _ {J _ {4}} \\ q _ {J _ {5}} \\ q _ {J _ {6}} \\ q _ {J _ {7}} \end{array} \right) \left( \begin{array}{c} U _ {1} \\ U _ {2} \\ U _ {3} \\ 0 \\ L _ {1} \\ L _ {2} \\ L _ {3} \\ 0 \\ 1 \end{array} \right)
$$

$$
q _ {J _ {i}} \geq 0, i = 1, \dots , 7
$$

The above problem is almost the same as the one we found earlier using the possible world probabilities. The only difference is the notation and that two identical columns corresponding to the possible world probabilities $p_{2}$ and $p_{4}$ have been collapsed together.

The column description (14) is not computationally practical. Determining whether $J \in I$ involves solving a satisfiability problem to check whether $S_J$ is empty. Thus we generate columns corresponding to possible worlds $v$ rather than sets $J$ . In the nonconditional problem (4) this yields columns $(y_0, y_1, \ldots, y_m)$ with $y_i = v(F_i)$ . If (for instance) $F_i$ is a logical clause $\bigvee_{j \in P} x_j \lor \bigvee_{j \in s} \neg x_j$ , then $y_i$ can be written as a pseudo-boolean function $y_{i}=1-\prod_{j\in P}(1-x_{j})\prod_{j\in N}x_{j}$ . Thus the column generation subproblem, which is to minimize (12), becomes a pseudo-boolean optimization problem. The situation is similar for the conditional problem (8).

Whether generated by $J$ 's or possible worlds, some of the columns of (4) are identical. But two identical columns will never appear in the basis of the solution. Thus when several possible worlds generate the same column, only one of the worlds will in practice absorb all the probability attributed to the set $S_{J}$ containing those worlds.

## 5. Probabilistic logic with unreliable sources

In probabilistic logic, the probabilities $Pr(F_{i})$ of logical formulas $F_{i}$ are delivered from a single evidence source. However, it might be useful to extend the model, such that it is possible to allow for more than one evidence source to supply probabilities (or estimates of these) to the logical formulas in question. This can be done in a straightforward manner.

Suppose there are K evidence sources, denoted by $ES_{k}$ , $k = 1, \ldots, K$ . If K = 1, the ordinary model for probabilistic logic is obtained. If $K \geq 2$ , we instead get conditional probabilities $Pr(F_{i}|ES_{k})$ , for all i, all k. The interpretation of these probabilities is: the probability of $F_{i}$ given that evidence source k is reliable. For each of the logical formulas $F_{i}$ , there are K probabilities, namely the ones obtained from the K evidence sources.

Let $S_{i}$ be the set of possible worlds in which $F_{i}$ is true, and let $R_{k}$ be the set of possible worlds, in which evidence source k is reliable (with certainty). Notice that here is a slight difference from probabilistic logic. The model not only has possible worlds in which some logical formulas are true but also possible worlds in which evidence sources are reliable. Suppose that evidence source k informs us that the probability of $S_{j}$ is in the interval $[L_{i}^{k}, U_{i}^{k}]$ . This gives rise to the set of linear constraints:

$$
L _ {i} ^ {k} \leq P r \left(F _ {i} | E S _ {k}\right) \leq U _ {i} ^ {k}, i, \dots , m, k = 1, \dots , K.
$$

These constraints can be rewritten as

$$
0 \leq P r (S _ {i} \cap R _ {k}) - L _ {i} ^ {k} P r (R _ {k})\tag{15}
$$

$$
P r (S _ {i} \cap R _ {k}) - U _ {i} ^ {k} P r (R _ {k}) \leq 0\tag{16}
$$

It is of course also possible for each evidence source to specify conditional probabilities. Suppose that evidence source k informs us that the conditional probability of $F_{i}$ given $F_{c(i)}$ belongs to some interval $[L_{ic(i)}^{k}, U_{ic(i)}^{k}]$ . The following set of constraints is then obtained:

$$
\begin{array}{c} L _ {i c (i)} ^ {k} \leq P r \big (F _ {i} | F _ {c (i)}, E S _ {k} \big) \leq U _ {i c (i)} ^ {k}, \\ i = 1, \ldots , m, k = 1, \ldots , K. \end{array}
$$

These constraints can be rewritten as follows:

$$
0 \leq P r \left(S _ {i} \cap S _ {c (i)} \cap R _ {k}\right) - L _ {i c (i)} ^ {k} P r \left(S _ {c (i)} \cap R _ {k}\right).\tag{17}
$$

$$
\operatorname * {P r} \left(S _ {i} \cap S _ {c (i)} \cap R _ {k}\right) - U _ {i c (i)} ^ {k} \operatorname * {P r} \left(S _ {c (i)} \cap R _ {k}\right) \leq 0.\tag{18}
$$

In ordinary probabilistic logic K=1, it is implicitly assumed that the evidence source is reliable. This need of course not be the case. Therefore, in addition to the above mentioned conditional probabilities, it is possible to specify probability intervals $[L^{k},U^{k}]$ , $k=1,\ldots,K$ , indicating to which degree the different evidence sources are reliable. This gives rise to the set of constraints:

$$
L ^ {k} \leq P r (E S _ {k}) \leq U ^ {k}, k = 1, \dots , K.\tag{19}
$$

If one believes in some of the evidence sources with certainty, the corresponding probability intervals should overlap, since otherwise the model is inconsistent. We cannot with certainty believe, for instance, that a probability is in the interval $[0.2, 0.3]$ and at the same time with certainty believe that it is in the interval $[0.5, 0.6]$ .

As in ordinary probabilistic logic, we have:

$$
P r (S _ {i} \cap R _ {k}) = \sum_ {v (S _ {i} \cap R _ {k}) = 1} q _ {v}
$$

where $q_{v}$ denotes the probability of world $v$ .

The inference problem is to place bounds on a conditional probability $Pr(F_{t}|F_{c(t)})$ . As in ordinary probabilistic logic, we solve a fractional linear program similar to,

$$
\min / \max \frac {P r (S _ {t} \cap S _ {c (t)})}{P r (S _ {c (t)})}
$$

$$
\begin{array}{l} s. t. \\ (1 5), (1 6), (1 7), (1 8), (1 9). \end{array}
$$

The sets $S_{1},\ldots,S_{h}$ are those defined above: the sets of possible worlds in which the given formulas $F_{i}\wedge ES_{k},F_{i}\wedge F_{c(i)}\wedge ES_{k},ES_{k},i=1,\ldots,m,k=1,\ldots,K$ , respectively, are true.

The probabilities of these formulas can be expressed in terms of possible worlds as explained in Section 4.

We see that the only difference from probabilistic logic is that we now have possible worlds in which some formulas are true and possible worlds in which an evidence source is reliable (with certainty). Instead of just having probabilities of formulas, we have probabilities conditioned on evidence sources. Furthermore, it is possible to state the probability of the reliability of some evidence source. If any of the probabilities are unknown, they are simply left unspecified.

So, everything in this section has been formulated in the same way as was done in the section on probabilistic logic. In particular, the model falls into the general framework. The column generation procedure is as in probabilistic logic.

## 6. Dempster-Shafer theory

In Dempster-Shafer theory there are several evidence sources, indexed by $k = 1, \ldots, K$ . Each evidence source k distributes a probability mass of one over a family $\{S_{i} | i \in H_{k}\}$ of distinct sets of possible outcomes. The index sets $H_{k}$ are disjoint, but a set $S_{i}$ in one family may be equal to a set $S_{i}$ in another family. The union of the $S_{i}$ 's is the frame of discernment, denoted $\Theta$ .

For each $i \in H_{k}$ , we interpret the mass $\mu(S_{i})$ to be the value $m_{k}(S_{i})$ of the basic probability function $m_{k}$ , which indicates the strength of k's evidence that the actual outcome lies in $S_{i}$ . Thus we have constraints (2) with $L_{i}=U_{i}=m_{k(i)}(S_{i})$ , where $i\in H_{k(i)}$ . Although $\sum_{i\in H_{k}}m_{k}(S_{i})=1$ for each evidence source k, some of its mass can be assigned to a set representing the universe $\Theta$ , which contains all possible situations. This mass represents evidence that supports no particular proposition.

When there are K evidence sources, the intersections $S_{J}$ are associated with cells of a K-dimensional cube. Each cell corresponds to an index set J that contains for each $k \in \{1, \ldots, K\}$ an index $i \in H_{k}$ representing the “coordinate” of the cell along dimension k. Since $S_{J}$ may be the same for different J’s, the same $S_{J}$ may be associated with several cells. The mass $\mu(S_{i})$ for $i \in H_{k}$ is distributed over the masses $q_{J}$ of all cells J whose k-th coordinate is i; i.e., all cells J with $i \in J$ . Thus we have (1), with $I(i) = \{J \in I | i \in J\}$ .

Classical Dempster-Shafer theory uses the particular distribution dictated by Dempster's combination rule:

$$
q _ {J} = \prod_ {i \in J} m _ {k (i)} (S _ {i}),\tag{20}
$$

which assumes that the evidence sources are in some sense independent. But we will allow any distribution observing (1), since independence assumptions may be unjustified. The classical theory can be obtained by adding the constraints (20) to the model.

This distribution scheme has the curious result that an empty set $S_{J}$ may receive probability mass. But it also implies that the constraints (2) and (3) always have a feasible solution. This can be seen by noting that the probabilities dictated by Dempster's combination rule satisfy them.

Whenever $S_J \subset S_t$ , evidence that $S_J$ contains the actual outcome adds to the evidence that $S_t$ does. So we interpret $\mu^*(S_t)$ as the sum of the masses of all $S_J \subset S_t$ . Thus we have (5) with $I^*(t) = \{J | S_J \subset S_t\}$ .

Since empty $S_{J}$ 's receive mass, this mass is ignored and the rest renormalized so that it sums to one. Thus the inference problem is to obtain bounds on

$$
B e l (S _ {t}) = \frac {\mu^ {*} (S _ {t})}{1 - \mu^ {*} (\emptyset)},\tag{21}
$$

where “Bel” is Shafer’s notation. We therefore obtain the fractional programming problem (4).

## 6.1. Example 3

Suppose that a detective is investigating a burglary of a shop. From one source he gets evidence supporting the beliefs that the thief is left-handed and that he is not an insider. From another source he gets evidence supporting the beliefs that the theft was an inside job and that the thief is right-handed. One of the clerks in the shop is left-handed, and the detective must decide with what certainty he can accuse the clerk.

For solving this problem we define two atomic propositions:

$x_{1}$ : The thief is left - handed.

$x_{2}$ : The thief is an insider.

A possible outcome is indicated by a pair of truth values $(x_{1}, x_{2})$ , and the frame of discernment consists of the four possible pairs. We are given the following six quantities:

$$
\begin{array}{l} m _ {1} (S _ {1}) = m _ {1} (\{(1, 0), (1, 1) \}) \\ \text {(source 1 evidence for x_ {1})} \\ m _ {1} (S _ {2}) = m _ {1} (\{(0, 0), (1, 0) \}) \\ \text {(source 1 evidence for \neg x_ {2})} \\ m _ {1} (S _ {3}) = m _ {1} (\Theta) (= 1 - m _ {1} (S _ {1}) - m _ {1} (S _ {2})) \\ m _ {2} (S _ {4}) = m _ {2} (\{(0, 1), (1, 1) \}) \\ \text {(source 2 evidence for x_ {2})} \\ m _ {2} (S _ {5}) = m _ {2} (\{(0, 0), (0, 1) \}) \\ \text {(source 2 evidence for \neg x_ {1})} \\ m _ {2} (S _ {6}) = m _ {2} (\Theta) (= 1 - m _ {2} (S _ {4}) - m _ {2} (S _ {5})) \end{array}
$$

We construct the following table of intersections:

<table><tr><td colspan="4">Table 3Intersections</td></tr><tr><td> $S_6 = \Theta$ </td><td> $\{(1,0),(1,1)\}$ </td><td> $\{(0,0),(1,0)\}$ </td><td> $\Theta$ </td></tr><tr><td> $S_5 = \{(0,0),(0,1)\}$ </td><td> $\emptyset$ </td><td> $\{(0,0)\}$ </td><td> $\{(0,0),(0,1)\}$ </td></tr><tr><td> $S_4 = \{(0,1),(1,1)\}$ </td><td> $\{(1,1)\}$ </td><td> $\emptyset$ </td><td> $\{(0,1),(1,1)\}$ </td></tr><tr><td></td><td> $S_1 = \{(1,0),(1,1)\}$ </td><td> $S_2 = \{(0,0),(1,0)\}$ </td><td> $S_3 = \Theta$ </td></tr></table>

Notice that the empty set $\varnothing$ may occur in the table, and that the same set may occur several times. In this particular case the empty set $\varnothing$ occurs twice.

Now let us associate a mass $q_{J}$ with each particular cell:

<table><tr><td colspan="4">Table 4 $q_{J}$ &#x27;s</td></tr><tr><td> $m_{2}(\Theta)$ </td><td> $q_{J_{1}}$ </td><td> $q_{J_{4}}$ </td><td> $q_{J_{7}}$ </td></tr><tr><td> $m_{2}(S_{5})$ </td><td> $q_{J_{2}}$ </td><td> $q_{J_{5}}$ </td><td> $q_{J_{8}}$ </td></tr><tr><td> $m_{2}(S_{4})$ </td><td> $q_{J_{3}}$ </td><td> $q_{J_{6}}$ </td><td> $q_{J_{9}}$ </td></tr><tr><td></td><td> $m_{1}(S_{1})$ </td><td> $m_{1}(S_{2})$ </td><td> $m_{1}(\Theta)$ </td></tr></table>

Each $m_{k}(S_{i})$ is distributed over the corresponding row or column. For instance, $m_{1}(S_{1}) = q_{J1} + q_{J2} + q_{J3}$ .

We wish to determine the mass $\mu^{*}(\{1,1\})$ that can be associated with the proposition $x_{1}\wedge x_{2}$ that the thief is a lefthanded insider. The normalized objective function of (4) is given by $q_{J_3} / (1 - q_{J_2} - q_{J_6})$ (in this particular case, $\mu^{*}(\emptyset) = q_{J2} + q_{J6}$ ). The resulting program (4) is:

$$
\min / \max \frac {q _ {J _ {3}}}{1 - q _ {J _ {2}} - q _ {J _ {6}}}
$$

s.t.

$$
\begin{array}{l} q _ {J _ {1}} + q _ {J _ {2}} + q _ {J _ {3}} = m _ {1} (S _ {1}) \\ q _ {J _ {4}} + q _ {J _ {5}} + q _ {J _ {6}} = m _ {1} (S _ {2}) \\ q _ {J _ {3}} + q _ {J _ {6}} + q _ {J _ {9}} = m _ {2} (S _ {4}) \\ q _ {J _ {2}} + q _ {J _ {5}} + q _ {J _ {8}} = m _ {2} (S _ {5}) \\ \sum_ {i = 1} ^ {9} q _ {J _ {i}} = 1 \\ q _ {J _ {i}} \geq 0, i = 1, \dots , 9 \end{array}
$$

The classical Dempster-Shafer theory associates the mass

$$
\begin{array}{l} m _ {1} (S _ {1}) m _ {2} (S _ {4}) \\ \quad / [ 1 - m _ {1} (S _ {1}) m _ {2} (S _ {5}) - m _ {1} (S _ {2}) m _ {2} (S _ {4}) ] \\ \text { with   the   proposition } x _ {1} \wedge x _ {2}. \end{array}
$$

Assuming for simplicity that all intersections $S_{J}$ are nonempty so that $\mu^{*}(\varnothing)=0$ , the columns $(y_{0}, y_{1}, \ldots, y_{m})$ of (4) satisfy

$$
\sum_ {i \in H _ {k}} y _ {i} = 1, k = 1, \dots , K.\tag{22}
$$

The objective function coefficient $y_{o}$ is 1 if and only if $\bigcap_{y_{i}=1} S_{i} \subset S_{t}$ , which is to say $\wedge_{yi=1} F_{i} \supset F_{t}$ . If the $F_{i}$ 's are formulas of propositional logic, additional constraints and 0-1 variables representing atomic propositions can be used to define $y_{0}$ in terms of $y_{1}, \ldots, y_{m}$ , using well-known methods [14]. The column generation subproblem becomes an integer programming problem: minimize (12) subject to (22) and the additional constraints. When $\mu^{*}(\emptyset) \neq 0$ , the linearized version of (4) can be similarly treated.

## 7. Second-Order probabilistic logic

Second-order probabilistic logic assigns probability distributions to $Pr(F_{j}|F_{c(j)})$ , rather than specifying $Pr(F_{j}|F_{c(j)})$ directly. These second-order distributions are approximated by specifying the probability that $Pr(F_{j}|F_{c(j)})$ lies in each of several intervals $[0,\pi_{i}]$ . Probabilistic information is therefore given in the form,

$$
L _ {i} \leq P r \left(\frac {P r \left(F _ {j _ {i}} \wedge F _ {c (j _ {i})}\right)}{P r \left(F _ {c (j _ {i})}\right)} \leq \pi_ {i}\right) \leq U _ {i}, i = 1, \dots , m.\tag{23}
$$

The propositions $F_{j}$ again belong to propositional logic and contain atomic propositions $x_{1},\ldots,x_{n}$ . In general, probabilities from a less reliable source will have a more dispersed second order distribution.

The first-order probability space consists of all probability distributions $(\pi_{1},\ldots,\pi_{2^{n}})$ over the possible worlds v. Each constraint in (23) places limits on the probability mass assigned to a region $S_{i}$ of this space. Specifically, $S_{i}$ is the half-space in which $Pr(F_{j_{i}}\wedge F_{c(j_{i})})\leq\pi_{i}Pr(F_{c(j_{i})})$ , or

$$
\sum_{\substack{v(F_{j_{i}}) = 1\\ v(F_{c(j_{i})}) = 1}}p_{v}\leq \pi_{i}\sum_{v(F_{c(j_{i})}) = 1}p_{v}.\tag{24}
$$

We interpret $\mu(S_{i})$ as the second-order probability that $Pr(F_{j_{i}}|F_{c(j_{i})})\leq\pi_{i}$ . We can again suppose that $\overline{S}_{i}$ belongs to the list $S_{1},\ldots,S_{h}$ whenever $S_{i}$ does. Thus the set of all minimal nonempty intersections $S_{J}$ of halfspaces partitions probability space into polyhedral regions. The probability mass $Pr(S_{i})$ of a halfspace is the sum of the masses $q_{J}$ of the polyhedra $S_{J}$ in it. Thus we have (1) with $I(i)=\{J|S_{J}\subset S_{i}\}$ .

The inference problem is to find bounds on $\mu^{*}(S_{t}) = \mu(S_{t})$ by solving (4), which is a linear programming problem because $\mu^{*}(\emptyset) = 0$ .

It remains to find a computationally practical way to implement the column generation scheme (6) when $I(i)=\{J|S_{j}\subset S_{i}\}$ . This can be done via mixed integer programming. From (24), each $S_{i}$ consists of the vectors p in probability space satisfying the i-th constraint of

$$
\begin{array}{l} - y _ {i} <   \sum_ {\substack {v (F _ {j _ {i}}) = 1 \\ v (F _ {c (j _ {i})}) = 1}} p _ {v} - \pi_ {i} \sum_ {v (F _ {c} (j _ {i})) = 1} p _ {v} \leq 1 - y _ {i}, \\ i = 1, \dots , m, \end{array}\tag{25}
$$

when $y_{i}=1$ , and its complement consists of those satisfying this same constraint when $y_{i}=0$ . Thus the sets $S_{J}$ for $J\in I$ are precisely the nonempty solution sets of (25) over all 0-1 vectors $y=(y_{1},\ldots,y_{m})$ . The column generation subproblem is therefore to minimize (12) subject to (25) and

$\sum_{v}p_{v} = 1,p_{v}\geq 0,\mathrm{all}v,$

where $y_0 = y_t$ .

## 7.1. Example 4

Suppose we have the following set of second-order probabilities:

$$
\begin{array}{l}P r \big (P r (x _ {1}) \leq \pi_ {1} \big) \in [ L _ {1}, U _ {1} ]\\P r \big (P r (x _ {1} \rightarrow x _ {2}) \leq \pi_ {2} \big) \in [ L _ {2}, U _ {2} ]\\P r \big (P r (x _ {1} \rightarrow x _ {2}) \leq \pi_ {3} \big) \in [ L _ {3}, U _ {3} ]\\P r \big (P r (x _ {1} \rightarrow x _ {2}) \leq \pi_ {4} \big) \in [ L _ {4}, U _ {4} ]\\P r \big (P r (x _ {3} | x _ {1} \wedge x _ {2}) \leq \pi_ {5} \big) \in [ L _ {5}, U _ {5} ]\end{array}
$$

Note that the distribution of $Pr(x_{1} \rightarrow x_{2})$ is somewhat more accurately specified than the others, because three cumulative second-order probabilities are given. We want to determine the bounds on the probability $Pr(Pr(x_{3}) \leq \pi_{5})$ . Notice that all the $\pi$ 's are given. The sets, $S_{i}$ , $1 \leq i \leq 4$ , are given as follows:

$$
\begin{array}{l} S _ {1}: \Big \{p \in \Re_ {+} ^ {8} | \Sigma_ {i = 1} ^ {8} p _ {i} = 1,   p _ {5} + p _ {6} + p _ {7} + p _ {8} \leq \pi_ {1} \Big \} \\ S _ {2}: \Big \{p \in \Re_ {+} ^ {8} | \Sigma_ {i = 1} ^ {8} p _ {i} = 1, p _ {1} + p _ {2} + p _ {3} + p _ {4} + p _ {7} + p _ {8} \\ \quad \leq \pi_ {2} \Big \} \\ S _ {3}: \Big \{p \in \Re_ {+} ^ {8} | \Sigma_ {i = 1} ^ {8} p _ {i} = 1, p _ {1} + p _ {2} + p _ {3} + p _ {4} + p _ {7} + p _ {8} \\ \quad \leq \pi_ {3} \Big \} \\ S _ {4}: \Big \{p \in \Re_ {+} ^ {8} | \Sigma_ {i = 1} ^ {8} p _ {i} = 1, p _ {1} + p _ {2} + p _ {3} + p _ {4} + p _ {7} + p _ {8} \\ \quad \leq \pi_ {4} \Big \} \\ S _ {5}: \Big \{p \in \Re_ {+} ^ {8} | \Sigma_ {i = 1} ^ {8} p _ {i} = 1,    p _ {8} \leq \pi_ {5} (  p _ {7} + p _ {8}) \Big \}, \end{array}
$$

where $R_{+}^{8}$ is the nonnegative orthant of $R^{8}$ . The set $S_{t}$ is given by:

$$
S _ {t}: \left\{p \in \Re_ {+} ^ {8} | \Sigma_ {i = 1} ^ {8} p _ {i} = 1, p _ {2} + p _ {4} + p _ {6} + p _ {8} \leq \pi_ {5} \right\}
$$

It is not particularly easy to see what the nonempty intersections $S_{J}$ of the halfspaces $S_{1}$ , $S_{2}$ , $S_{3}$ , $S_{4}$ and $S_{t}$ are. However, the columns of (4) can be found using the following system of linear constraints:

$$
\begin{array}{l} - y _ {1} <   p _ {5} + p _ {6} + p _ {7} + p _ {8} - \pi_ {1} \leq 1 - y _ {1} \\ - y _ {2} <   p _ {1} + p _ {2} + p _ {3} + p _ {4} + p _ {7} + p _ {8} - \pi_ {2} \leq 1 - y _ {2} \\ - y _ {3} <   p _ {1} + p _ {2} + p _ {3} + p _ {4} + p _ {7} + p _ {8} - \pi_ {3} \leq 1 - y _ {3} \\ - y _ {4} <   p _ {1} + p _ {2} + p _ {3} + p _ {4} + p _ {7} + p _ {8} - \pi_ {4} \leq 1 - y _ {4} \\ - y _ {5} <   p _ {8} + \pi_ {5} (p _ {7} + p _ {8}) \leq 1 - y _ {5} \\ - y _ {0} <   p _ {2} + p _ {4} + p _ {6} + p _ {8} - \pi_ {5} \leq 1 - y _ {0} \\ \sum_ {i = 1} ^ {8} p _ {i} = 1 \\ p _ {i} \geq 0, i = 1, \dots 8, y _ {i} \in \{0, 1 \}, i = 0, \dots , 5 \end{array}
$$

The columns of (4) are the binary vectors $(y_{0}, y_{1}, y_{2}, y_{3}, y_{4}, y_{5})$ that are feasible for the above constraint set. An approximate second-order distribution for $Pr(x_{3})$ can be found by solving this problem for several values of $\pi_{5}$ .

## 8. Belief functions

Dempster-Shafer theory derives the plausibility $Bel(S_{t})$ of $S_{t}$ by combining evidence from several sources. Each source k provides support for several sets $S_{i}$ that is measured by a basic probability function $m_{k}$ .

A variation on this approach is to suppose that the evidence for the sets $S_{i}$ is combined in advance, outside the mechanism of the theory. This provides an estimate $Bel(S_{i})$ of the plausibility of each $S_{i}$ . The goal is to find what values of $Bel(S_{t})$ are consistent with these estimates.

Thus we interpret $\mu(S_i) = \mu^*(S_i)$ to be $Bel(S_i)$ . Again any evidence for a subset of $S_t$ is evidence for $S_t$ . We therefore postulate an underlying basic probability function $m(S_i)$ that measures evidence in favour of the particular set $S_i$ , with $Bel(S_i) = \sum_{S_j \subset S_i} \mathbf{t}_t$ $m(S_j)$ . This means that we distribute the mass $\mu(S_i) = Bel(S_i)$ over the variables $q_J = q_{\{j\}} = m(S_j)$ for all subsets $S_j$ of $S_i$ . So the “intersections” $S_J$ are simply the sets $S_j$ . The distribution formula is (1) with $I(i) = \{\{j\}|S_j \subset S_i\}$ .

If the precise value of $Bel(S_{i})$ is given for all $S_{i}$ , the underlying basic probability function is determined by the inclusion-exclusion formula,

$$
m \left(S _ {i}\right) = \sum_ {S _ {j} \subset S _ {i}} (- 1) ^ {\left| S _ {i} \backslash S _ {j} \right|} B e l \left(S _ {j}\right).
$$

But if $Bel(S_{i})$ is only partially specified, several basic probability functions are possible, and $Bel(S_{t})$ may be restricted to a range but not precisely determined.

If $L_{i}$ , $U_{i}$ are the bounds placed on $Bel(S_{i}) = \mu(S_{i})$ , we have the constraints (2). To obtain bounds on $Bel(S_{t}) = \mu^{*}(S_{t})$ we solve (4), which is linear because $\mu^{*}(\varnothing) = 0$ . Since this problem contains only one column for each $S_{i}$ , column generation should not in general be necessary. Also it should normally be easy to determine whether $S_{j} \subset S_{i}$ (i.e., whether $F_{j}$ implies $F_{i}$ ), since the given propositions $F_{i}$ should normally be simple.

## 9. Conclusion

In this paper we have demonstrated how several logics for reasoning under uncertainty fit into the same framework. Each admits a linear programming model of essentially the same structure, except that the different logics are implemented with different column generation procedures. The column generation procedures include pseudo-boolean optimization, integer programming and mixed integer programming. The logics that we have been able to show fit into this general framework include probabilistic logic, probabilistic logic with unreliable sources of information, Dempster-Shafer theory, second order probabilistic logic and a simple logic of belief functions.

An important question is how well the column generation scheme will work in practice. It has been demonstrated to work very well in the case of probabilistic logic $[15]$ , and therefore also for the special version of probabilistic logic with unreliable sources of information. Further computational experience is needed to determine how well it will work in Dempster-Shafer theory and second-order probabilistic logic.

## References

[1] Andersen, K.A., and J.N. Hooker, Bayesian logic, Decision Support Systems 11 (1994) 191–210.

[2] Boole, G., An Investigation of the Laws of Thought, on which are Founded the Mathematical Theories of Logic and Probabilities. Dover Publications (New York, 1951). Original work published 1854.

[3] Boole, G., Studies in Logic and Probability, ed. by R. Rhees, Watts and Co (London) and Open Court Publishing Company (La Salle, Illinois, 1952).

[4] Charnes, A., and W.W. Cooper, Programming with linear fractionals, Naval Research Logistics Quarterly 9 (1962) 181–186.

[5] Chen, S.S., Some extensions of probabilistic logic, in J.F. Lemmer and L.N. Kanal, eds., Uncertainty in Artificial Intelligence 2, North-Holland (1988).

[6] Dirickx, I.M.I., and L.P. Jennergren, Systems Analysis by Multilevel Methods: With Applications to Economics and Management. Wiley, Chichester (1979).

[7] Dubois, D., and H. Prade, The principle of minimum specificity as a basis for evidential reasoning, Uncertainty in Knowledge-Based Systems, Lecture Notes in Computer Science 286 (1986) 75–84

[8] Dubois, D., and H. Prade, A tentative comparison of numerical approximate reasoning methodologies, International Journal Man-Machine Studies 27 (1987) 149–183.

[9] Georgakopolous, G., D. Kavvadias and C.H. Papadimitriou, Probabilistic satisfiability, Journal of Complexity 4 (1988) 1–11.

[10] Grosof, B.N., An inequality paradigm for probabilistic reasoning, in J.F. Lemmer and L.N. Kanal, eds., Uncertainty in Artificial Intelligence 1, North-Holland (1986).

[11] Grosof, B.N., Non-monotonicity in probabilistic knowledge, in J.F. Lemmer and L.N. Kanal, eds., Uncertainty in Artificial Intelligence 2, North-Holland (1986).

[12] Hailperin, T., Boole's Logic and Probability, Studies in Logic and the Foundations of Mathematics v. 85, North-Holland (1976).

[13] Hailperin, T., Probability logic, Notre Dame Journal of Formal Logic 25 (1984) 198–212.

[14] Hooker, J.N., A quantitative approach to logical inference, Decision Support Systems 4 (1988) 45–69.

[15] Jaumard, B., P. Hansen and M.P. Aragaö, Column generation methods for probabilistic logic, ORSA Journal on Computing 3 (1991) 135–148.

[16] McLeish, M., Probabilistic logic: some comments and possible use for nonmonotonic reasoning, in J.F. Lemmer and L.N. Kanal, eds., Uncertainty in Artificial Intelligence 2, North-Holland (1986).

[17] McLeish, M., Nilsson's probabilistic entailment extended to Dempster-Shafer theory, in Uncertainty in Artificial Intelligence 3 (1989) 23–34.

[18] Nilsson, N.J., Probabilistic logic, Artificial Intelligence 28 (1986) 71–87.

[19] Paaß, G., Probabilistic logic, in Non-standard Logics for Automated Reasoning, ed. P. Smets em et al., Academic Press (New York, 1988) 213–251.

[20] Shafer, G., A Mathematical Theory of Evidence, Princeton University Press (1976).

![](/api/attachments/GF64CC8B/fulltext/images/fbacefb36201c856f8a79a4c713174a2c73bcf28ede51b8e8a71a2e5f4330c89.jpg)  
Kim Allan Andersen is associate professor at the Mathematical Institute at Aarhus University. He received a masters degree in mathematics and economics from Aarhus University in 1984 and a Ph.D. in operations research from Aarhus University in 1990. His research interests lie in the application of mathematical programming to logical problems, as well as integer programming.

John Hooker is Professor in the Graduate School of Industrial Administration at Carnegie Mellon University. He is interested in new modelling paradigms for operations research, including logico-mathematical models as well as empirical models, and in the mathematical structure of propositional, probabilistic and other logics.
