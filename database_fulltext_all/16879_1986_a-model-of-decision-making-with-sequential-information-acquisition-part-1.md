---
otero_id: 16879
otero_key: "BQKPKMAZ"
title: "A model of decision-making with sequential information-acquisition (Part 1)"
authors: "James C. Moore; Andrew B. Whinston"
year: "1986"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(86)90001-1"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# A Model of Decision-Making with Sequential Information-Acquisition (Part 1) \*

James C. MOORE and Andrew B. WHINSTON
Department of Computer Science and Krannert Graduate School of Management, Purdue University, West Lafayette, IN 47907, USA

While most real-life decisions are of necessity made with less than perfect information, there is usually some opportunity to acquire additional information regarding the problem at hand before a final decision is made. It is, of course, the recognition of this fact which has led to the importance now attached to the field of Decision Support Systems. On the other hand, the formal analysis of the sort of decision problem for which Decision Support Systems can be useful appears to have lagged behind the developments in applications. In this paper we develop a model of decision-making in which there is available a variety of informational sources (experiments) which can reduce (though generally not eliminate) the uncertainty

\* Our early work on the material covered in this paper was done as part of a larger project in which H. Keith Hall, now at the University of Arkansas, was an active participant. In fact, much of section 2 and some parts of section 3 of the present paper were completed during that period, and Hall made many helpful suggestions and comments on this material. He should, of course, be completely absolved of all responsibility for any remaining errors or confusion.

![](/api/attachments/BQKPKMAZ/fulltext/images/1abe7e0666a65353790c0e7adaf080a03725f354bb0828f8b1c95929776ed7e6.jpg)

Andrew B. Whinston is on the faculty of the Krannert Graduate School of Management and the Department of Computer Science at Purdue University. His primary teaching interest is management information systems. His current research interests include data base management and applications of artificial intelligence to economics and management. He has also studied applied economics, regulatory economics, and accounting theory.

Among his numerous publications, he has co-authored two books (with C. Holsapple and R. Bonczek), Foundations of Decision Support Systems (Academic Press, 1981), and Micro Database Management – Practical Techniques for Application Development (Academic Press, 1985). He has been a consultant to various companies, governmental agencies, and international organizations on data processing questions.

associated with the final decisions. Since the informational sources are available only at some cost (either monetarily or in terms of time, or both), the decision-maker must solve two conceptually distinct problems: (1) developing an optimal information-gathering strategy, and (2) developing an optimal final decision strategy, conditional upon the information obtained during the information-gathering process. A theoretical framework is developed here for the analysis of this general problem, and fairly complete solutions are obtained for some interesting special cases; most notably the computer file search problem.

Keywords: Decision support systems, Decision theory, Dynamic programming, File management

## 1. Introduction

In many instances of decision-making under uncertainty, there is an opportunity to acquire information pertinent to the problem before a final decision is made. While such information will generally reduce the uncertainty involved in the final decision, it is typically only obtainable at a cost. Thus at the outset, the decision-maker faces two conceptually distinct though closely inter-related problems: (1) developing an optimal information-gathering strategy, and (2) developing an optimal final decision strategy, conditional upon the information obtained during the information-gathering process. In this paper we shall develop a conceptual theoretical framework for the analysis of this multi-faceted problem, and

![](/api/attachments/BQKPKMAZ/fulltext/images/ee4ea10f6e20e589460a6eac27b6ffd23a00485050ae9404b3bb4b048b77bc86.jpg)

University, he taught at the University of Missouri, Columbia. Dr. Moore is a member of the American Economics Association and the Econometrics Society.

develop a fairly complete solution for some special cases; most notably for the computer file-search problem. The techniques we develop are, however, applicable to a much wider variety of problems than the computer search problem; in fact, nearly all of the results used to obtain a solution for this particular problem are formulated and proved in a considerably more general framework.

This paper is simultaneously a theoretical study of a general class of decision problems and a step toward a proposed basis for a theory of Decision Support Systems (DSS). The information-gathering portion of the class of decision problems studied in this paper can be interpreted as either gathering information directly from the environment, or specifying the execution of various computer algorithm, depending on the form of the specific problem under investigation. Thus the superficial connection, at least, between the decision problems being studied here and the field of DSS is obvious. We believe, however, that the potential long-run ramifications of this connection are both deeper and more wide-ranging than this surface comparison would indicate; if one can characterize an optimal information-gathering strategy in terms of the other given data (payoff function, state space, probability distribution, etc.) of a general decision problem, one has the basis for an optimal data base design and retrieval system for a class of users corresponding to the qualitative assumptions made in the general decision problem.

The entire paper is published in two parts. Part 1 includes sections 1 through 3 and an appendix, and Part 2 contains sections 4 through 6. In section 2 we develop the basic model of decision-making to be used in this study, although some of the details regarding the reasons for the formulation used here are relegated to the appendix. In section 3 we discuss the concept of an optimal solution in detail, and develop the notions of efficient and 'admissible' strategies for the decision problem. The notion of an efficient strategy is particularly important in the theoretical analysis developed in the subsequent sections of the paper.

In section 4 (Part 2) we introduce a special case of our model which we call the 'categorization problem'. In subsequent sections we develop a set of sufficient conditions for the solution of this problem, and obtain detailed solutions for two special cases of this problem: the computer file search problem and something we call the ‘only correct guesses count’ problem (the familiar game of ‘twenty questions’ can be regarded as a special case of this problem). The basic formulations of both these latter two problems are also presented in this section, and some preliminary results are developed regarding the solution of the categorization problem.

In section 5 we develop a number of results regarding the fineness of the final information structure obtained in an information-gathering process, and the cost of obtaining same. The results are then applied to the categorization problem, and a fairly complete solution is developed for the 'only correct guesses count' problem.

In section 6 we analyze the situation where one is dealing with binary or trinary information structures (two or three possible outcomes for each ‘experiment’, respectively), and where a linear ordering can be defined over the experiments available. This linear ordering arises naturally in the computer search problem, but may in principle be definable in the context (and useful in the solution) of any problem of the general form developed in section 2 in which there are only two or three possible outcomes for each individual information-gathering activity ('experiment'). The results of this section are then used to develop a complete solution of the computer file search problem. The results we obtain in this application are consistent with those which have been obtained in the computer science literature; however, our results are developed under a somewhat broader concept of optimality than has been used in this literature, which results in some new insight regarding their interpretation.

## 2. A Model of Decision Making

## 2.1. Model 1 $^{1}$

Our decision problem is defined by eight ele-

ments

$$
\mathbf {D} = \langle X, \phi , D, \omega^ {*}, A, \left\{\mathbf {M} _ {a} | a \in A \right\}, c, r \rangle ,
$$

where X is the set of possible (mutually exclusive) states. We use the generic notation ‘x’ to denote elements of X. $\phi: X \rightarrow [0,1]$ is the probability density function. $\phi$ defines the probability distribution function $\pi: P(X) \rightarrow [0,1]$ by

$$
\pi (Y) = \sum_ {x \in Y} \phi (x) f o r Y \subseteq X,
$$

where ‘ $P(X)$ ’ denotes the power set of $X$ . $D$ is the set of available (final) decisions. $\omega^{*}$ : $X \times D \times \mathbb{R} \to \mathbb{R}$ is the payoff function (the inclusion of the third variable allows for the effect of the cost of information-gathering on payoffs). $A$ is the set of ‘initial’ (information-gathering) actions, or experiments, available. $M_{a}$ is the information structure associated with action $a \in A$ . (Each $M_{a}$ is a partition of $X$ , as will be explained in more detail below.) $c$ : $A \to \mathbb{R}_{+}$ is the cost function; $c(a)$ is the cost of utilizing action $a \in A$ . $r$ is a positive integer representing the number of information-gathering actions which can be taken before a final decision is made.

We shall explain the form and role of A and $M_{a}$ more fully in the next subsection. The source and rationale for the limitation on the number of information gathering steps allowable (r) is explained in the appendix. In the meantime, the initial assumptions we shall employ regarding this model are as follows.

Assumptions: X, D, and A are all finite, and $(\forall x \in X)$ : $\phi(x) > 0$ . In particular, we shall assume that A has $n + 1$ elements, where $n \geq 1$ , and write $A = \{0, 1, \ldots, n\}$ . Other assumptions regarding A and $\{M_{a} | a \in A\}$ will be set out in the next section.

The decision-maker is assumed to have a finite set of feasible (final) decisions, D, and to receive a payoff which depends upon the state of the environment, $x \in X$ , the decision chosen, $d \in D$ , and the cost of information-gathering, c. One may suppose (see, e.g., Marschak and Radner [1972]), that there is a deterministic relationship between decisions, states of the environment, costs and a set of outcomes (or effects), E, such that there exists an outcome function, $\rho(x, d, c)$ mapping the set $X \times D \times |R|$ into the set of outcomes. If the decision-maker's preferences over the outcomes and the cost of the decision may be represented by a real valued utility function, $u(e, d)$ , for all $e \in E$ and $d \in D$ , then the payoff function may be defined by

$$
\omega^ {*} (x, d, c) = u [ \rho (x, d, c), d ].\tag{1}
$$

For the remainder of our theoretical discussion we will take the payoff function, $\omega^{*}(\cdot)$ , as given. $^{2}$

The remaining elements of our decision problem revolve around the construction of an information structure, and the costs of obtaining information. The result of an information acquisition strategy, $\alpha$ , is a partition

$$
\mathbf {B} = \left\{B _ {1}, \dots , B _ {q} \right\}
$$

on $X$ such that $B_{i} \cap B_{j} = \emptyset$ for $i \neq j$ , and $\bigcup_{i=1}^{q} B_{i} = X$ . As will be set forth in more detail shortly, with each set $B \in B$ , there will be associated a cost of information-gathering, $C(B)$ . Thus if the decision-maker follows the decision function $\delta: B \to D$ , the expected payoff for the joint strategy $(\alpha, B, \delta)$ will be given by

$$
\begin{array}{l} \Omega^ {*} (\alpha , \mathbf {B}, \delta) \\ = \sum_ {B \in \mathbf {B}} \sum_ {x \in B} \phi (x) \omega^ {*} [ x, \delta (B), C (B) ]. \end{array}\tag{2}
$$

In a summary statement, we can roughly describe the goal of the decision problem being analyzed as: Choose as information strategy $\alpha$ and a decision function $\delta\colon B\to D$ in such a way as to maximize (2) over all $\alpha'$ and $\delta'\colon B\to D$ .

To complete the description of our decision problem, we shall first need to explain our treatment of the problem of information acquisition in more detail.

## 2.2. Information Acquisition

As mentioned earlier, we let $A = \{0,1,\ldots,n\}$ denote the set of initial actions (or experiments) available to the decision-maker. Associated with each $a \in A$ is a set of information signals, $Y_{a}$ , and a function $\eta_{a} \colon X \to Y_{a}$ . We shall assume that each $Y_{a}$ contains a finite number, $n(a)$ , of different signals, so that, without loss of generality, we can write $Y_{a} = \{1,2,\ldots,n(a)\}$ . We shall also assume that

(i) for each $a \in A$ , $\eta_{a}$ is onto $Y_{a}$ , and (ii) $n(0) = 1$ (so that the $a = 0$ action is the null information action).

For a given element of the set of states, $x \in X$ , there is a single signal receivable from each of the n information signal sets. More generally, one might wish to consider allowing for ‘errors in observation’ and/or measurement. In such a case, in place of $\eta_{a}$ a conditional probability density function $h_{a}: X \times Y_{a} \to [0,1]$ , where $h_{a}(x, y) = \Pr(y|x)$ , would be used. $^{3}$ In the present discussion, we shall only consider the case where information is obtained deterministically ('noiseless information'); however, it can be shown that noisy information can be incorporated within the present model by including the signals as a part of the specification of the state space. $^{4}$

We define

$$
M _ {a y} = \{x \in X | \eta_ {a} (x) = y \} = \eta_ {a} ^ {- 1} (\{y \})
$$

$$
\text { for } \quad a = 0, 1, \dots , n, \quad y = 1, \dots , n (a)
$$

and $M_{a} = \{M_{a1},\dots ,M_{a,n(a)}\}$

for $a = 0,1,\ldots ,n$

2.2.1. Definition. Let $B \subseteq X$ be non-empty. We shall say that a family of subsets of $X, B$ , is an information structure on $B$ iff

(i) $\pmb{B}$ is a partition of $\pmb{B}$ (that is, the sets in $\pmb{B}$ are pairwise disjoint, and their union equals $\pmb{B}$ ).

(ii) $(\forall B' \in B): B' \neq \varnothing$ .

Notice, that for $a \in A$ , $M_{a}$ is an information structure on X (by Definition 1). We shall refer to $M_{a}$ as the information structure associated with (or induced by) a.

2.2.2. Definition. Let $B \subseteq X$ be non-empty, and let $a \in A$ . We define the information structure induced on $B$ by $a$ , $\iota(B, a)$ , as

$$
\begin{array}{r l} \iota (B, a) & = \left\{B \cap M _ {a 1}, B \cap M _ {a 2}, \dots , B \cap M _ {a, n (a)} \right\} \\ & \backslash \{\varnothing \}. \end{array}
$$

Notice that if $B \subseteq X$ is non-empty, and $a \in A$ , then $\iota(B, a)$ is an information structure on $B$ .

2.2.3. Definition. Let $B \subseteq X$ be non-empty, let $B = \{B_1, \ldots, B_k\}$ be an information structure on $B$ , and let $\alpha: B \to A$ (we shall refer to such a function as an action function on $B$ ). The refinement of $B$ by $\alpha$ , $R(B, \alpha)$ , is defined by

$$
R (\mathbf {B}, \alpha) = \bigcup_ {j = 1} ^ {k} \iota [ B _ {j}, \alpha (B _ {j}) ].
$$

2.2.4. Definition. Let $B \subseteq X$ be non-empty, and let $B_1$ and $B_2$ be information structures on $B$ . We shall say that $B_1$ is as fine as $B_2$ (or that $B_1$ is a refinement of $B_2$ or that $B_2$ is no finer than $B_1$ ), and write $B_1 \geq B_2$ , iff

$$
(\forall B ^ {\prime} \in \mathbf {B} _ {1}) (\exists B ^ {\prime \prime} \in \mathbf {B} _ {2}): B ^ {\prime} \subseteq B ^ {\prime \prime}.
$$

Notice that if B is a non-empty subset of X, B is an information structure on B, and $\alpha$ is an action function on B, then $R(B, \alpha)$ is (an information structure on B and is) a refinement of B.

Assumption. The decision-maker can take up to r information-gathering actions, where $1 \leq r \leq n$ . Since we include the null information action in A (and its associated cost will be assumed to be zero), we can, without loss of generality, assume that the decision-maker takes exactly r information-gathering actions. We also assume that there are no duplicate information structures, i.e.,

$$
(\forall a, a ^ {\prime} \in A): \mathbf {M} _ {a} = \mathbf {M} _ {a ^ {\prime}} \Rightarrow a ^ {\prime}.
$$

2.2.5. Definition. A feasible strategy for $D$ , $\sigma$ , is a sequence of $r + 1$ pairs $\sigma = \langle (B_1, \alpha_1), (B_2, \alpha_2), \ldots, (B_r, \alpha_r), (\mathcal{B}_{r+1}, \delta) \rangle$ satisfying

$$
\begin{array}{l l}(1)&\boldsymbol {B} _ {1} = \{\boldsymbol {X} \},\\(2 a)&\alpha_ {t}: \boldsymbol {B} _ {t} \rightarrow A \quad \text { for } \quad t = 1, 2, \dots , r,\\(2 b)&\boldsymbol {B} _ {t + 1} = R (\boldsymbol {B} _ {t}, \alpha_ {t}) \quad \text { for } \quad t = 1, 2, \dots , r,\\(3)&\delta : \boldsymbol {B} _ {r + 1} \rightarrow D.\end{array}
$$

We shall denote the set of all feasible strategies for D by ‘Σ(D)’.

A sequence of action functions can be seen to create, a priori, a sequence of partitions on X, each a refinement of the previous partition in the sequence. The element of a given partition in the sequence in which the 'true' state of the environment falls will determine the exact sequence of signals that the decision-maker will receive from the sequence of action functions generating the partition. If a sequence of action functions, its associated sequence of partitions, and a final decision function defined on the last partition in the sequence are chosen a priori, then a decision strategy is formed. The decision-maker in effect generates the information structure from which he will make his final decision.

We shall often find it convenient to regard a feasible strategy $\sigma = \langle (B_1, \alpha_1), \ldots, (B_r, \alpha_r), (B_{r+1}, \delta) \rangle$ as being composed of two parts

(i) the information-gathering strategy $\alpha = \langle (B_1, \alpha_1), \ldots, (B_r, \alpha_r) \rangle$ ,

(ii) the decision strategy $(\pmb{B}_{r + 1},\delta)$ .

Accordingly, we define the following:

2.2.6. Definition. A feasible information-gathering strategy for D, $\alpha$ is a sequence of r pairs $\alpha = \langle (B_{1}, \alpha_{1}), \ldots, (B_{r}, \alpha_{r}) \rangle$ satisfying 1 and 2 of Definition 5, and a feasible decision strategy for D is a pair $(B, \delta)$ , where

(1) there exists a feasible information-gathering strategy for $D$ , $\alpha = \langle (B_1, \alpha_1), \ldots, (B_r, \alpha_r) \rangle$ such that $R(B_r, \alpha_r) \geq B$ ,

(2) $\delta: B \to D$ .

2.2.7. Example. Suppose a decision-maker holds two units of a commodity which he can sell in either of two markets. We shall assume that each market is equally accessible to our decision-maker, but that information about prices in these two markets is costly to obtain and somewhat imperfect. We shall also suppose that the commodity is perishable, and must be sold this period.

To keep the example simple, we suppose that institutional constraints and/or the decision-maker's a-priori beliefs are such that $p_{i}$ , the price in the ith market, can only take one of the four values 0, 1, 2, 3. Thus the state space, X, is given by

$$
X = \left\{\left(p _ {1}, p _ {2}\right) \mid p _ {i} \in \{0, 1, 2, 3 \} \quad \text { for } \quad i = 1, 2 \right\}.\tag{3}
$$

We shall also suppose that decision-maker's subjective probability distribution over $X$ is uniform, so that

$$
(\forall x \in X): \phi (x) = 1 / 1 6.\tag{4}
$$

Further, we suppose the decision-maker's utility is linear in money, so that if we let $q_{i}$ denote the quantity sold in market $i(i=1,2)$ ,

$$
\omega (x, d) = \omega [ (p _ {1}, p _ {2}),
$$

$$
\left. \left(q _ {1}, q _ {2}\right) \right] = p _ {1} q _ {1} + p _ {2} q _ {2}, \quad \text { and }\tag{5}
$$

$$
\mathbf {D} = \left\{d _ {1}, d _ {2}, d _ {3} \right\}, \quad \text { where }\tag{6}
$$

$$
d _ {1} = (2, 0), d _ {2} = (1, 1), d _ {3} = (0, 2)\tag{7}
$$

[i.e., $d_{1}$ is the decision to sell both units in the first market, etc.].

We shall also suppose that the decision-maker has three informational sources available (all available at a positive price). He can obtain

(1) the average price in the two markets (for notational convenience, however, we shall suppose that he is obtaining $p_{1} + p_{2}$ , which is, of course, mathematically equivalent).

(2) the minimum price in the two markets; unfortunately for the decision-maker, however, without the additional specification of which market this minimum price prevails in.

(3) the price in market one.

Thus in this case, $A = \{0, 1, 2, 3\}$ , where

$$
\eta_ {0} (p _ {1}, p _ {2}) = 0 [ \text { null   information } ],\tag{8}
$$

$$
\eta_ {1} (p _ {1}, p _ {2}) = p _ {1} + p _ {2},\tag{9}
$$

$$
\eta_ {2} \left(p _ {1}, p _ {2}\right) = \min \left\{p _ {1}, p _ {2} \right\}, \quad \text { and }
$$

$$
\eta_ {3} (p _ {1}, p _ {2}) = p _ {1}.\tag{10}
$$

(11)

Thus, e.g.,

$$
Y _ {1} = \{0, 1, 2, 3, 4, 5, 6 \}, \quad Y _ {2} = \{0, 1, 2, 3 \} = Y _ {3},\tag{12}
$$

and the information structures are as indicated in figs. 1a–c. We shall also suppose that

$$
c (0) = 0, c (1) = 1 / 4, c (2) = 1 / 8, c (3) = 4 / 5,
$$

and that r=2, that is, the decision-maker can purchase at most two pieces of information.

Consider the strategy $\sigma^{*}$ , whose representation in decision-tree format is given in fig. 2. Thus in this case,

$$
\alpha_ {1} (X) = 2, \quad \mathbf {B} _ {2} = \left\{M _ {2 0}, M _ {2 1}, M _ {2 2}, M _ {2 3} \right\} = \mathbf {M} _ {2},
$$

and $\alpha_{2}$ is given by

$$
\alpha_ {2} (M _ {2 0}) = 3 = \alpha_ {2} (M _ {2 1}), \quad \alpha_ {2} (M _ {2 2}) = 0 = (M _ {2 3}).
$$

Graphically, our final information structure, $B_{3}$ is as indicated in fig. 3.

![](/api/attachments/BQKPKMAZ/fulltext/images/0ed0df080c815e82d9e87cb24f927d06ec75dc8643c0b6d9d9a4e40b0a986e4c.jpg)

![](/api/attachments/BQKPKMAZ/fulltext/images/e8d5822229dcbe3f8c37c5255dbffe70e1ab95b9efd8367528486130f5e65fe3.jpg)  
Fig. 1a.  
Fig. 1b.  
Fig. 1c

2.2.8. Definition. If $\alpha = \langle (\pmb{B}_1, \alpha_1), \ldots, (\pmb{B}_r, \alpha_r) \rangle$ is a feasible information-gathering strategy for $\pmb{D}$ we define, for each $q \in \{1, \ldots, r + 1\}$ and each $B \in \pmb{B}_q$

$$
\mathbf {B} _ {t} (B) = \left\{B ^ {\prime} \in \mathbf {B} _ {t} \mid B ^ {\prime} \cap B \neq \varnothing \right\}
$$

for $t = q, \ldots, r + 1$ ,

( )

where we write $B_{r+1}=R(B_{r},\alpha_{r})$ . We shall refer to $B_{t}(B)$ as the information structure on B at the tth step. $^{5}$

The following result will probably contain no surprises for the reader who has followed the development carefully to this point; but the properties set forth are important to our subsequent development.

2.2.9. Lemma. If $\alpha = \langle (B_1, \alpha_1), \ldots, (B_r, \alpha_r) \rangle$ is a feasible information-gathering strategy for $D$ , and $t \in \{1, \ldots, r + 1\}$ , then

(i) for each $B \in \mathbf{B}_t$ , and each $q \in \{1, \ldots, t\}$ , there exists exactly one $B^q \in \mathbf{B}_q$ such that $B \in \mathbf{B}_t(B^q)$ , and furthermore, $B \subseteq B^q$ .

![](/api/attachments/BQKPKMAZ/fulltext/images/3fb51431c04584e96033d3e59bd60e0da8261e424c619676a420d6f075e029d1.jpg)  
(a) $B_{t}(B) = \{B\}$ ,

(ii) if we write $B_{t}=\{B_{1},\ldots,B_{k}\}$ , then $\{\boldsymbol{B}_{q}(B_{1}),\ldots,\boldsymbol{B}_{q}(B_{k})\}$ is an information structure on $B_{q}$ for $q=t,\ldots,r+1$ ; that is $\{\boldsymbol{B}_{q}(B_{1}),\ldots,\boldsymbol{B}_{q}(B_{k})\}$ is a partition of $B_{q}$ and $\boldsymbol{B}_{q}(B_{i})\neq\varnothing$ for $i=1,\ldots,k$ .

(iii) for each $B \in B_{t}$ , we have (b) $B_{q}(B)$ is an information structure on $B$ for $q = t, \ldots, r + 1$ ,

(c) if $t \leq r$ , $\boldsymbol{B}_{q+1}(B) = R[\boldsymbol{B}_{q}(B), \alpha_{q}]$ for $q = t, \ldots, r$ .

Proof. (i) Let $B \in B_t$ and $q \in \{1, \ldots, t\}$ be arbitrary. We have

$$
\mathbf {B} _ {t} \geq \mathbf {B} _ {q},
$$

and hence there exists $B^q \in B_q$ such that,

$$
\boldsymbol {B} \subseteq \boldsymbol {B} ^ {q}.
$$

Since $\pmb{B}_q$ is a partition of $X$ , it then follows that if $\pmb{B}' \in \pmb{B}_q$ is such that $\pmb{B}' \neq \pmb{B}^q$ , then

$$
B \cap B ^ {\prime} = \varnothing ,
$$

and our result follows.

(ii) If we write $B_{t} = \{B_{1},\ldots ,B_{k}\}$ and $q\in \{t,\dots ,r + 1\}$ , it follows immediately from part (i) that

$$
\bigcup_ {B \in \mathbf {B} _ {q} (B _ {j})} B \subseteq B _ {j} \quad \text { for } \quad j = 1, \dots , k.\tag{14}
$$

Furthermore, since $B_{q}$ is a partition of X, we obviously have, for each $j \in \{1, \ldots, k\}$ ,

$$
B _ {j} \subseteq \bigcup_ {\boldsymbol {B} \in \mathbf {B} _ {q}} B,
$$

and, from the definition of $\boldsymbol{B}_{q}(\boldsymbol{B})$ , it then follows that

$$
B _ {j} \subseteq \bigcup_ {B \in \mathbf {B} _ {q} (B _ {j})} B.
$$

(15)

![](/api/attachments/BQKPKMAZ/fulltext/images/15514545d957024a0d9c843bdd038e96acbca3e7c875774c75aa118f5ea5dd67.jpg)

Combining (14) and (15), we then have

$$
B _ {j} = \bigcup_ {B \in \mathbf {B} _ {q} (B _ {j})} B
$$

for $j = 1, \ldots, k, \quad q = t, \ldots, r + 1.$

(16)

From part (i) of our proof we see that

$$
\mathbf {B} _ {q} = \bigcup_ {j = 1} ^ {k} \mathbf {B} _ {q} (B),
$$

while from (16) and the fact that $B_{t}$ is a partition

![](/api/attachments/BQKPKMAZ/fulltext/images/87030c280b5dbd8972394a6c582b6ecd86ee89d8e71a99861fb4eb3b42906346.jpg)

of $\mathbf{X}$ , it follows that

$$
\mathbf {B} _ {q} \left(B _ {j}\right) \cap \mathbf {B} _ {q} \left(B _ {j ^ {\prime}}\right) = \varnothing \quad \text { for } \quad j \neq j ^ {\prime}.
$$

Finally, we note that it also follows from (16) that

$$
\mathbf {B} _ {q} \left(B _ {j}\right) \neq \varnothing \quad \text { for } \quad j = 1, \dots , k.
$$

Therefore

$$
\left\{\mathbf {B} _ {q} (B _ {q}), \dots , \mathbf {B} _ {q} (B _ {k}) \right\}
$$

is an information structure on $\pmb{B}_q$ .

(iii) Let $t \in \{1, \ldots, r + 1\}$ be arbitrary, and let $B \in B_t$ . We note first of all that it follows at once from (16) above, and the fact that $B_t$ is a partition of $X$ , that

$$
\widetilde {\mathbf {B}} _ {t} (\boldsymbol {B}) = \{\boldsymbol {E} \}.
$$

Now let $q \in \{1, \ldots, r + 1\}$ be arbitrary. It follows at once from the definition of $\boldsymbol{B}_{q}(B)$ and the fact that $B_{q}$ is a partition of X, that the sets in $\boldsymbol{B}_{q}(B)$ are non-empty and pairwise disjoint. Using (16), above, it then follows that $\boldsymbol{B}_{q}(B)$ is an information structure on B.

Suppose now that $t \leq r$ and let $q \in \{1, \ldots, r\}$ . From part (ii) and the definition of a feasible

strategy, we have

$$
\begin{array}{r l} & {\mathbf {B} _ {q + 1} = R \big (\mathbf {B} _ {q}, \alpha_ {q} \big) = \bigcup_ {B \in \mathbf {B} _ {q}} \iota \Big [ B, \alpha_ {q} (B) \Big ]} \\ & {\quad = \bigcup_ {B \in \mathbf {B} _ {t}} \bigcup_ {B ^ {\prime} \in \mathbf {B} _ {q} (B)} \iota \Big [ B ^ {\prime}, \alpha_ {q} (B ^ {\prime}) \Big ]} \\ & {\quad = \bigcup_ {B \in \mathbf {B} _ {t}} R \Big [ \mathbf {B} _ {q} (B), \alpha_ {q} \Big ].} \end{array}\tag{17}
$$

However, by part (ii)

$$
\mathbf {B} _ {q + 1} = \bigcup_ {B \in \mathbf {B} _ {t}} \mathbf {B} _ {q + 1} (B),
$$

and using (17) and the fact that for each $\mathbf{B} \in \mathbf{B}_t$ , both $\mathbf{B}_{\mathbf{q}}(\mathbf{B})$ and $\mathbf{B}_{\mathbf{q} + \mathbf{q}}(\mathbf{B})$ are information structures on $B$ , it then follows easily that for each $B \in \mathbf{B}_t$ , $\mathbf{B}_{q+1}(B) = R[\mathbf{B}_q(B), \alpha_q]$ . Q.E.D.

In defining the sequence $\boldsymbol{B}_{q}(B)(q=t,\ldots,r+1)$ for $B\in B_{t}$ we are, in effect, tracing forward the segment leading from B of the sequence $\boldsymbol{B}_{q}(q=t,\ldots,r+1)$ . It will often be useful to trace the sequence backward from $B\in B_{t}$ as well; which is the point of the next definition.

2.2.10. Definition. Let $\alpha = \langle (B_1, \alpha_1), \ldots, (B_r, \alpha_r) \rangle$ be a feasible information-gathering strategy for $D$ , and let $B_{r+1} = R(B_r, \alpha_r)$ . For each $q \in \{1, \ldots, r+1\}$ , and each $B \in B_q$ , we define the sequence $\langle \beta_t(B) \rangle_{t=1}^q$ by

$\beta_{t}(B)=\text{that}\quad B^{\prime}\in\mathbf{B}_{t}\quad\text{such that}\quad B\cap B^{\prime}\neq\varnothing.$ (18)

(Note that it follows at once from Lemma 9 that $\langle \beta_t(B) \rangle_{t=1}^q$ is well-defined.) We shall refer to $\beta_t(B)$ as the predecessor of $B$ at $t$ .

2.2.11. Lemma. Suppose $\alpha = \langle (\pmb{B}_1, \alpha_1), \ldots, (\pmb{B}_r, \alpha_r) \rangle$ is a feasible information-gathering strategy for $\pmb{D}$ , and let $\pmb{B}_{r+1} = R(\pmb{B}_r, \alpha_r)$ . Then we have

(i) for each $q \in \{1, \ldots, r + 1\}$ , and each $t \in \{1, \ldots, q\}$ , each $B \in B_q$ , and each $B' \in B_t$ , $B' = \beta_t(B)$ if, and only if, $B \in B_q(B')$ .

(ii) for each $q \in \{1, \ldots, r + 1\}$ , and each $B \in B_q$ , $B = \beta_{q}(B) \subseteq \beta_{q-1}(B) \subseteq \cdots \subseteq \beta_{1}(B) = X.$

(iii) if, for some $q$ , $q' \in \{1, \ldots, r + 1\}$ , $B \in B_q$ , and $B' \in B_{q'}$ , we have, $q \geq q'$ and $B \cap B' \neq \varnothing$ , then

$$
\begin{array}{l} \beta_ {t} (B) = \beta_ {t} (B ^ {\prime}) \\ \text { for } \quad t = 1, \dots , q ^ {\prime} \left[ \text { and } \quad B ^ {\prime} = \beta_ {q ^ {\prime}} (B) \right]. \end{array}
$$

Proof. Part (i) of our conclusion follows immediately from the definitions. To prove (ii), let $q \in \{1, \ldots, r + 1\}$ and $B \in B_{q}$ be arbitrary. Since $B_{q}$ is a partition of X, it is obvious that

$$
\beta_ {q} (B) = B,
$$

and, since $\pmb{B}_1 = \{X\}$ , it is equally apparent that $\beta_1(B) = X$ .

Now suppose $q \geq 1$ , let $t \in \{1, \ldots, q - 1\}$ , and define

$$
B _ {1} = \beta_ {t} (B) \quad \text { and } \quad B _ {2} = \beta_ {t + 1} (B).
$$

From part (i), and part (i) of Lemma 9, we have $B \subseteq B_i$ for $i = 1, 2$ ,

so that

$$
B _ {1} \cap B _ {2} \neq \varnothing .
$$

Therefore

$$
B _ {2} \in \mathbf {B} _ {t + 1} (B _ {1}),
$$

and it follows from Lemma 9 that

$$
B _ {2} = \beta_ {t + 1} (B) \subseteq B _ {1} \subseteq \beta_ {t} (B).
$$

In order to prove (iii), we note that if the hypotheses of (iii) hold, we have

$$
\beta_ {q ^ {\prime}} (B) = B ^ {\prime}.
$$

It then follows at once from (ii) and the definition of $\langle \beta_t(B)\rangle_{t=1}^q$ that $\beta_t(B)=\beta_t(B')$ for $t=1,\ldots,q'$ . Q.E.D.

## 2.3. Costs and Payoffs of Strategies

The following definition (and the results of the preceding subsection) will enable us to provide a convenient characterization of the expected cost of a feasible strategy.

2.3.1. Definition. Let $\alpha = \langle (B_1, \alpha_1), \ldots, (B_r, \alpha_r) \rangle$ be a feasible information-gathering strategy for $D$ , and let $B_{r+1} = R(B_r, \alpha_r)$ . For each $q \in \{1, \ldots, r+1\}$ , and each $B \in B_q$ , we define $a(B)$ as the sequence (of length $q-1$ ) of actions taken by the strategy $\alpha$ along the path that yields $B$ ; that is,

$$
\mathbf {a} (B) = \langle a (1, B), \dots , a (q - 1, B) \rangle .
$$

where we define $^{6}$

$$
a (t, B) = \alpha_ {t} [ \beta_ {t} (B) ] \quad \text { for } \quad t = 1, \dots , q - 1.
$$

Assumption. We suppose that, with each $a \in A$ is associated a nonnegative cost, $c(a)$ , the cost of employing action a. Further, we assume that $c(0) = 0$ .

In a given realization of the type of decision problem under study, the application of a feasible information-gathering strategy.

$$
\boldsymbol {\alpha} = \left\langle \left(\mathbf {B} _ {1}, \alpha_ {1}\right), \dots , \left(\mathbf {B} _ {r}, \alpha_ {r}\right) \right\rangle ,
$$

will result in the determination that $\hat{x}$ , the true state, is an element of some $B \in B_{r+1} \equiv R(B_r, \alpha_r)$ . The cost of determining that $\hat{x} \in B$ will be the sum of the costs of all the actions taken along the path yielding (ending in) B, and will therefore be given by

$$
C (B) = \sum_ {t = 1} ^ {r} c [ a (t, B) ].\tag{1}
$$

As noted earlier, we suppose that there is a deterministic relationship between decisions, states of the environment, costs, and a set of outcomes (effects); that is, we suppose that there exists a function

$$
\rho : X \times D \times \mathbb {R} \rightarrow E,
$$

where ‘E’ denotes the set of outcomes (effects) (cf. Marschak and Radner [1972]). We also suppose that there exists a (von Neumann–Morgenstern) utility function

$$
\mathbf {u}: E \rightarrow \mathbb {R},
$$

such that $u(\cdot)$ represents the decision-maker's preferences over outcomes. Thus the payoff function $\omega^{*}: X \times D \times R \to R$ is defined by

$$
\begin{array}{l} \omega^ {*} (x, d, c) = \mathbf {u} [ \rho (x, d, c) ] \\ \text { for } (x, d, c) \in X \times D \times \mathbb {R}, \end{array}\tag{2}
$$

and we shall assume that $\omega^{*}(x, d, c)$ is strictly decreasing in $c$ , for all $(x, d) \in X \times D$ .

If $\sigma = \langle (B_1, \alpha_1), \ldots, (B_r, \alpha_r), (B_{r+1}, \delta) \rangle$ is a feasible strategy for $D$ , we see, therefore, that the expected payoff for $\sigma$ will be given by

$$
\Omega^ {*} (\sigma) \equiv \sum_ {B \in \mathbf {B} _ {r + 1}} \sum_ {x \in B} \phi (x) \omega^ {*} [ x, \delta (B), C (B). ]. \tag {2}\tag{3}
$$

We then suppose that the goal of our decision problem is to

choose $\sigma^{*}\in\Sigma(\mathbf{D})$ such that for all $\sigma\in\Sigma(\mathbf{D})$ , $\Omega^{*}(\sigma^{*})\geq\Omega^{*}(\sigma)$ . (4)

However, suppose we assume that the set of consequences (effects), E, takes the form

$$
\boldsymbol {E} = \mathbb {R} \times W,
$$

where ‘W’ denotes the space of non-monetary components of the consequences of an act; and that the consequences function, $\rho$ , takes the form

$$
\rho (x, d, c) = \left(\rho_ {1} (x, d) - c, \rho_ {2} (x, d)\right),
$$

where

$$
\rho_ {1} \colon X \times D \to \mathbb {R}\tag{5}
$$

yields the monetary aspect of the consequence, and

$$
\rho_ {2}: X \times D \rightarrow W
$$

yields the non-monetary aspect of the outcome. If we also suppose that $u(\cdot)$ , the decision-maker's utility function, can be written in the form

$$
u (\mu , w) = a \mu + u _ {2} (w) \quad \text { for } \quad (\mu , w) \in \mathbb {R} \times W,
$$

where a > 0 is a positive constant; then we can further suppose, without loss of generality, that a = 1. Thus, with these assumptions we can write

$$
\begin{array}{r l} \omega^ {*} (x, d, c) & \equiv u [ \rho (x, d, c) ] \\ & = \rho_ {1} (x, d) - c + u _ {2} [ \rho_ {2} (x, d) ], \end{array}
$$

and, if we define

$$
\omega (x, d) = \rho_ {1} (x, d) + u _ {2} [ \rho_ {2} (x, d) ],
$$

our net payoff function becomes

$$
\omega^ {*} (x, d, c) = \omega (x, d) - c.\tag{6}
$$

Thus in this case if $\sigma = \langle \alpha, B_{r+1}, \delta \rangle$ is a feasible strategy, the expected net payoff from $\sigma$ , (3), becomes

$$
\begin{array}{r l} \Omega^ {*} (\sigma) & = \sum_ {B \in \mathbf {B} _ {r + 1}} \sum_ {x \in B} \phi (x) [ \omega (x, \delta (B)) - C (B) ] \\ & = \sum_ {B \in \mathbf {B} _ {r + 1}} \sum_ {x \in B} \phi (x) \omega [ x, \delta (B) ] \\ & - \sum_ {B \in \mathbf {B} _ {r + 1}} \pi (B) C (B). \end{array} \tag {$3^{\prime$}}
$$

From (1) we see that expected cost of strategy $\sigma$ , $\Gamma(\sigma)$ is given by

$$
\Gamma (\sigma) = \sum_ {B \in \mathbf {B} _ {r + 1}} \pi (B) C (B).\tag{7}
$$

If we also define the expected gross payoff of $\sigma$ , $\Omega(\sigma)$ , by

$$
\Omega (\sigma) = \sum_ {B \in \mathbf {B} _ {r + 1}} \sum_ {x \in B} \phi (x) \omega [ x, \delta (B) ],\tag{8}
$$

we see from (3') that in this case the expected net payoff of $\sigma$ , $\Omega^{*}(\sigma)$ , can be written as the difference between expected gross payoff, $\Omega(\sigma)$ , and expected cost, $\Gamma(\sigma)$ ; i.e.,

$$
\Omega^ {*} (\sigma) = \Omega (\sigma) - \Gamma (\sigma).\tag{3"}
$$

In most of the remainder of this paper (all of section 3 onward), we shall assume that $\omega^{*}(\cdot)$ can be written in the form of (6), so that expected net payoff can be written in the form $(3^{\prime})$ or $(3^{\prime \prime})$ . Where this is the case, we shall say that the payoff function is linearly separable (in monetary outcomes).

If we re-examine the expression (7), which gives the expected cost of $\sigma$ , we note that it depends only on the information-gathering portion of $\sigma$ . Thus if $\alpha = \langle (\boldsymbol{B}_1, \alpha_1), \ldots, (\boldsymbol{B}_r, \alpha_r) \rangle$ is a feasible information-gathering strategy for $\boldsymbol{D}$ , we define $\gamma(\alpha)$ , the expected cost of $\alpha$ by

$$
\gamma (\alpha) = \sum_ {B \in \mathbf {B} _ {r + 1}} \pi (B) C (B),\tag{9}
$$

where $\boldsymbol{B}_{r+1} = \boldsymbol{R}(\boldsymbol{B}_{r}, \alpha_{r})$ . In the context of the linearity assumption developed in the previous paragraph, the following result will often be useful. $^{8}$

2.3.2. Proposition. If $\alpha = \langle (B_1, \alpha_1), \ldots, (B_r, \alpha_r) \rangle$ is a feasible information-gathering strategy for $D$ , then:

$$
\begin{array}{l} \gamma (\alpha) = c [ \alpha_ {1} (X) ] + \sum_ {B \in \mathbf {B} _ {2}} \pi (B) c [ \alpha_ {2} (B) ] \\ \qquad + \dots + \sum_ {B \in \mathbf {B} _ {r}} \pi (B) c [ \alpha_ {r} (B) ] \\ \qquad = \sum_ {t = 1} ^ {r} \sum_ {B \in \mathbf {B} _ {t}} \pi (B) c [ \alpha_ {t} (B) ]. \end{array}
$$

Proof. Using (9) and (1), we have

$$
\begin{array}{r l} \gamma (\alpha) & = \sum_ {B \in \mathbf {B} _ {r + 1}} \pi (B) \sum_ {t = 1} ^ {r} c [ a (t, B) ] \\ & = \sum_ {t = 1} ^ {r} \sum_ {B \in \mathbf {B} _ {t + 1}} \pi (B) c [ a (t, B) ]. \end{array}\tag{10}
$$

Now, let $t \in \{1, \ldots, r\}$ be arbitrary. We have by Lemma 2.9 that

$$
\begin{array}{l} \sum_ {B \in \mathbf {B} _ {r + 1}} \pi (B) c [ a (t, B) ] \\ = \sum_ {B \in \mathbf {B} _ {t}} \sum_ {B ^ {\prime} \in \mathbf {B} _ {r + 1} (B)} \pi (B ^ {\prime}) c [ a (t, B ^ {\prime}) ]. \end{array}\tag{11}
$$

However, from Lemma 2.11 we have, for each $\mathbf{B} \in \mathbf{B}_{\mathfrak{t}}$ , that:

$$
\left(\forall B ^ {\prime} \in \mathbf {B} _ {r + 1} (B)\right): a (t, B ^ {\prime}) = \alpha_ {t} (B);
$$

and thus

$$
\begin{array}{l} \sum_ {B \in \mathbf {B} _ {t}} \sum_ {B ^ {\prime} \in \mathbf {B} _ {r + 1} (B)} \pi (B ^ {\prime}) c [ a (t, B ^ {\prime}) ] \\ = \sum_ {B \in \mathbf {B} _ {t}} c [ \alpha_ {t} (B) ] \sum_ {B ^ {\prime} \in \mathbf {B} _ {r + 1} (B)} \pi (B ^ {\prime}). \end{array}\tag{12}
$$

Furthermore, again using Lemma 2.9,

$$
\sum_ {B ^ {\prime} \in \mathbf {B} _ {r + 1} (B)} \pi (B ^ {\prime}) = \pi (B).\tag{13}
$$

From (11)-(14) we have, for each $t \in \{1, \ldots, r\}$ ,

$$
\sum_ {B \in \mathbf {B} _ {r + 1}} \pi (B) c [ a (t, B) ] = \sum_ {B \in \mathbf {B} _ {t}} \pi (B) c [ \alpha_ {t} (B) ].\tag{14}
$$

Substituting (14) into (10), we then obtain the stated result. Q.E.D.

Before concluding this subsection, it is worthwhile to consider the problem of determining an optimal strategy for Example 2.7.

2.3.3. Example (Example 2.7 Cont'd). It can be shown that the strategy $\sigma^{*}$ defined in our previous discussion of Example 1, which has an expected payoff $\Omega^{*}(\sigma^{*})$ given by

$$
\Omega^ {*} (\sigma^ {*}) = 3 3 / 8 - 1 / 8 - (1 - 1 / 4) 4 / 5 = 3 2 / 5.
$$

is optimal for the decision problem under consideration. This example illustrates several aspects of the decision model developed here which are worth noting.

(1) The optimal strategy does not obtain full information, even though such is available. This statement has two aspects:

(a) $M_{22}$ , which is not a singleton, is an element of $\pmb{B}_2$ , and if experiment 3 were to be performed at that point, better information (i.e., a finer partition) would be obtained. However, it is not optimal to do so, for this action would increase expected cost by more than it would increase expected gross payoff.

(b) The strategy $\sigma^1$ , displayed in fig. 4, results in full information (allows a decision to be made with certainty).

![](/api/attachments/BQKPKMAZ/fulltext/images/dceb7f117217dd89cf9101fe140b060baa0bfb353420a25b1a4759bbdb324d3c.jpg)  
Fig. 4

However, $\sigma^{1}$ has an expected return given by

$$
\begin{array}{r l} \Omega^ {*} (\sigma^ {1}) & = 3 4 / 8 - 1 / 4 - (1 - 1 / 8) 4 / 5 = 4 - 7 / 1 0 \\ & = 3 3 / 1 0, \end{array}
$$

which is less than $\Omega^{*}(\sigma^{*})$ . On the other hand, $\sigma^{1}$ is an efficient strategy in the sense that if we set $\alpha_{2}(B)=0$ for any $B\in B_{2}$ for which we now have $\alpha_{2}(B)=3$ , the expected return would be smaller.

(2) In the sense of the Marschak and Radner [1972] definitions, both experiments 1 and 2 have zero information value. Since the optimal strategy begins with experiment 2, it follows that we cannot build up an optimal strategy by making use of their definition of the value of information at each stage $t(t = 1, 2, \ldots, r + 1)$ , although at $t = r$ we can make the choice of $\alpha_r$ on the basis of maximizing the value of information in the Marschak and Radner sense.

(3) The order in which experiments are conducted is of critical importance in obtaining the optimal strategy. In our example, experiments 2 and 3 are performed in that order in the optimal strategy. However, the largest expected return obtainable from a strategy which begins with experiment 3 ( $\alpha_{1}(X)=3$ ) is 3 31/80, which is less than $\Omega^{*}(\sigma^{*})$ .

(4) The optimal procedure with t=1 is to perform experiment 3 and then sell appropriately (both units in market 2 if the price in market one is zero, etc.). As pointed out above, however, the optimal strategy does not begin with experiment 3 if r=2.

## 2.4. Sequential and Non-sequential Strategies

2.4.1. Definition. If a feasible strategy for $D$ , $\sigma = \langle (B_1, \alpha_1), \ldots, (B_r, \alpha_r), (B_{r+1}, \delta) \rangle$ (respectively, a feasible information-gathering strategy, $\alpha = \langle (B_1, \alpha_1), \ldots, (B_r, \alpha_r) \rangle$ ) is such that for all $t(t = 1, \ldots, r)$ and all $B, B' \in B_t$ , we have

$$
\alpha_ {t} (B) = \alpha_ {t} (B ^ {\prime}),\tag{1}
$$

we shall say that $\sigma$ (respectively, $\alpha$ ) is a non-sequential strategy. Otherwise, $\sigma$ (respectively, $\alpha$ ) will be said to be a sequential strategy.

The reason for the terminology here is that sequential strategies use information in a sequential fashion; that is, the information obtained at the tth step is used in deciding the $(t+1)$ th action. $^{9}$ A non-sequential strategy involves a fixed sequence of actions, with a given action in the sequence to be carried out regardless of the information obtained from the previous action in the sequence. It is apparent that non-sequential strategies are defined completely by the sequence of actions to be employed and the decision function $\delta$ to be used at the $(r+1)$ th step. Thus, if $\sigma=\langle(B_{1},\alpha_{1}),\ldots,(B_{r},\alpha_{r}),(B_{r+1},\delta)\rangle$ is a non-sequential strategy, we can by (1) above, define, for any fixed $B\in B_{r+1}$

$$
\bar {\alpha} (t) = a (r, B) \quad \text { for } \quad t = 1, 2, \dots , r.
$$

The strategy is then completely defined by the $(r + 2)$ -tuple

$$
\left[ \bar {\alpha} (1), \bar {\alpha} (2), \dots , \bar {\alpha} (r), \left(\mathbf {B} _ {r + 1}, \delta\right) \right],\tag{2}
$$

and for our present discussion we shall modify our previous notation to use an $(r+2)$ -tuple of the form (2) to denote non-sequential strategies.

Non-sequential strategies, while being generally less efficient than sequential strategies, have the advantage that they can be done in parallel. Thus if we consider a strategy of the form (2), we can imagine a central agent delegating a subset of $\{\bar{\alpha}(1),\ldots,\bar{\alpha}(r)\}$ to one or each of several agents. The principal advantage of this, of course, is that it would serve to effectively expand r, the number of information-gathering actions which can be taken before a final decision is made (see the discussion regarding r in the appendix). Partially, or possibly wholly, offsetting this advantage are (a) the fact that sequential strategies are generally more efficient than non-sequential strategies (sequential strategies often obtain the same or more information than non-sequential strategies, with a lower expected cost), and (b) the cost of employing the agents. However, while the general problem of the delegation of problem-solving tasks is something which we believe can fruitfully be studied within the context of this model, we shall not pursue this topic further in this paper.

2.4.2. Definition. We define the finest information structure obtainable from $A$ , $\pmb{B}^{A}$ , by

$$
\mathbf {B} ^ {A} = \left\{\bigcap_ {a = 1} ^ {n} M _ {a 1}, \bigcap_ {a = 1} ^ {n - 1} M _ {a 1} \cap M _ {n 2}, \ldots , \right.
$$

9 This distinction is essentially the same as between sequential and non-sequential sampling in statistical decision theory. See, e.g., DeGroot [1970, Chapter 12].

$$
\begin{array}{l} \bigcap_ {a = 1} ^ {n - 1} M _ {a 1} \cap M _ {n, n (n))}, \ldots , \\ \bigcap_ {a = 1} ^ {n - 2} M _ {a 1} \cap M _ {n - 1, 2} \cap M _ {n 1}, \ldots , \\ \left. \bigcap_ {a = 1} ^ {n} M _ {a, n (a)} \right\} \setminus \{\varnothing \}. \end{array}
$$

It can be shown that $B^{A} \geq B_{r+1}$ , for any feasible final information structure, $B_{r+1}$ , which justifies our terminology in the above definition. This gives us a simple necessary condition which must be satisfied by any feasible final information structure, and we shall often make use of this fact in the material to follow.

Notice that in a given realization of Model I, $B^{A}$ represents the best information that can be obtained even if $r \geq n$ . (Thus, for example, the finite memory of even the largest computer available puts an upper limit on the number of decimal places one can use in representing a real number.) From the standpoint of the decision problem, therefore, any data concerning individual elements of members of $B^{A}$ is, in a sense, irrelevant to the decision at hand. This is another property which can be usefully exploited in the analysis of our decision problem.

It will often be useful to have a characterization of a feasible information structure which we can invoke without a reference to the feasible strategy from which it arises. Moreover, it will sometimes be useful to be able to speak of a set that could arise as an element of a feasible information structure without having to specifically tie it to a feasible final information structure of which it is an element, or the feasible strategy with which it is connected. We can develop a definition of both which will be satisfactory for most purposes by first developing the following.

We first extend our definition of a feasible information-gathering strategy to: A k-feasible information-gathering strategy $(k=1,\ldots,n)$ , $\alpha$ is a sequence of k pairs,

$$
\boldsymbol {\alpha} = \left\langle \left(\mathbf {B} _ {1}, \alpha_ {1}\right), \dots , \left(\mathbf {B} _ {k}, \alpha_ {k}\right) \right\rangle
$$

satisfying 1 and 2 of Definition 2.2.5. (with 2 holding for $t = 1, \ldots, k$ ). We can then define the following.

2.4.3. Definition. Let $k \in \{1, \ldots, n\}$ . We shall say that

(1) an information structure on X, B, is k-feasible iff there exists a k-feasible information-gathering strategy,

$$
\boldsymbol {\alpha} = \left\langle \left(\mathbf {B} _ {1}, \alpha_ {1}\right), \dots , \left(\mathbf {B} _ {k}, \alpha_ {k}\right) \right\rangle ,
$$

such that

$$
\mathbf {B} = R \left(\mathbf {B} _ {k}, \alpha_ {k}\right).
$$

(2) a set $B \subseteq X$ is $k$ -feasible iff there exists a $k$ -feasible information structure on $X$ , $B$ , such that $B \in B$ .

Notice that for any $k \in \{1, \ldots, n\}$ , and any $k$ -feasible information structure, $B$ , we will have

$$
\mathbf {B} ^ {A} \geq \mathbf {B}.\tag{3}
$$

Furthermore, $\mathbf{B}^A$ is $n$ -feasible (i.e., $k$ feasible for $k = n$ ).

2.4.4. Definition. For each $B \subseteq X$ , we define $\pmb{B}^{A}(B) \subseteq \pmb{B}^{A}$ by

$$
\mathbf {B} ^ {A} (B) = \left\{B ^ {\prime} \in \mathbf {B} ^ {A} \mid B \cap B ^ {\prime} \neq \varnothing \right\}.
$$

The following is then an easy consequence of (3), and the proof will be left to the interested reader.

2.4.5. Proposition. If $B \subseteq X$ is $k$ -feasible for some $k \in \{1, \ldots, n\}$ , then $B^A(B)$ is an information structure on $B$ . Furthermore, if $B = \{B_1, \ldots, B_q\}$ is a $k$ -feasible information structure for some $k \in \{1, \ldots, n\}$ , then

$$
\left\{\mathbf {B} ^ {A} \left(B _ {1}\right), \dots , \mathbf {B} ^ {A} \left(B _ {q}\right) \right\}
$$

is an information structure on $B^{A}$ .

While we shall make use of Proposition 5 on a number of occasions, we shall postpone our first application to the next subsection; in the meantime directing our attention to another question.

We shall at times be interested in the question of whether it is possible and/or desirable to obtain a solution with certainty. The following notation and definitions will be convenient in such discussion.

If we define

$$
\mathbf {B} ^ {X} = \left\{\{x \} \mid x \in X \right\},
$$

we obviously have

$$
\mathbf {B} ^ {X} \geq \mathbf {B} ^ {A},\tag{7}
$$

and, in fact, for any k-feasible information structure, B,

$$
\mathbf {B} ^ {X} \geq \mathbf {B}.\tag{8}
$$

We can define two notions of a solution with certainty, depending upon whether one of the converse inclusions [converse of (7) or (8)] holds.

## 2.4.6. Definitions. We shall say that $\pmb{D}$

(i) admits of potential certainty iff

$$
\mathbf {B} ^ {A} \geq \mathbf {B} ^ {X}.\tag{9}
$$

(ii) is solvable with certainty iff there exists a feasible strategy for D, $\sigma = \langle \alpha, B_{r+1}, \delta \rangle$ , such that

$$
\mathbf {B} _ {r + 1} \geq \mathbf {B} ^ {X}.\tag{10}
$$

Obviously if D is solvable with certainty, then it admits of potential certainty but the converse is not necessarily true. In any case, it is obviously not necessarily the case that either (9) or (10) holds.

We close this section with the following result, which we shall sometimes find useful in the material to follow.

2.4.7. Proposition. If $B \subseteq X$ is $k$ -feasible, for some $k \in \{1, \ldots, n\}$ , and $B \notin B^A$ , then there exists $\bar{a} \in A$ such that

$$
\# \iota (B, \bar {a}) \geq 2.
$$

Proof. Using Proposition 5, we see that if $B$ is $k$ -feasible and $B \notin B^A$ , then

$$
\# \mathbf {B} ^ {A} (B) \geq 2.
$$

Accordingly, let $B_{1}, B_{2} \in \mathbf{B}^{A}(B)$ be such that $B_{1} \neq B_{2}$ .

From the definition of $\pmb{B}^A$ , we see that there exist sequences $\langle y_1^i, \ldots, y_n^i \rangle (i = 1, 2)$ , such that

$y_{a}^{i}\in \{1,\dots ,n_{a}\}$ for $i = 1,2,a = 1,\ldots ,n,$ and

$$
B _ {i} = \bigcap_ {a = 1} ^ {n} M _ {a y _ {a} ^ {i}} \quad \text { for } \quad i = 1, 2.\tag{11}
$$

Furthermore, since $B_{1} \neq B_{2}$ , we must have

$$
\left\langle y _ {1} ^ {1}, \dots , y _ {n} ^ {1} \right\rangle \neq \left\langle y _ {1} ^ {2}, \dots , y _ {n} ^ {2} \right\rangle .
$$

Letting

$$
\bar {a} = \min \left\{a \in A _ {1} \mid y _ {a} ^ {1} \neq y _ {a} ^ {2} \right\}, \quad \text { where }
$$

$$
A _ {1} \equiv \{a \in A | a \neq 0 \} = A \setminus \{0 \},
$$

we then see from (11) and the fact that $B_{i} \subseteq B$ for $i = 1, 2$ , that

$$
B _ {1} \subseteq M _ {\bar {a} y ^ {1}} \cap B, B _ {2} \subseteq M _ {\bar {a} y ^ {2}} \cap B,
$$

and thus $\# \iota(B, \bar{a}) \geq 2$ . Q.E.D.

## 2.5. Conditional Optimality with Linear Separability

Throughout this subsection, and throughout the remainder of the paper, we shall assume that the payoff function is linearly separable in monetary outcomes, so that we write

$$
\omega^ {*} (x, d, c) = \omega (x, d) - c,\tag{1}
$$

and for a feasible strategy $\sigma = \langle (B_1, \alpha_1), \ldots, (B_r, \alpha_r), (B_{r+1}, \delta) \rangle$ we can express the expected net payoff of $\sigma$ as

$$
\Omega^ {*} (\sigma) = \Omega (\sigma) - \Gamma (\sigma),\tag{2}
$$

where $\Omega(\sigma)$ , the expected gross payoff from $\sigma$ is given by

$$
\Omega (\sigma) = \sum_ {B \in \mathbf {B} _ {r + 1}} \sum_ {x \in B} \phi (x) \omega [ x, \delta (B) ],\tag{3}
$$

and $\Gamma(\sigma)$ , the expected cost of $\sigma$ , is given by

$$
\Gamma (\sigma) = \sum_ {B \in \mathbf {B} _ {r + 1}} \pi (B) C (B),\tag{4}
$$

(see the discussion in section 2.3). Given this assumption, some new concepts become of interest, for example the following.

2.5.1. Definitions. If $B \subseteq X$ is non-empty, we define the potential gross payoff associated with $B$ , $v(B)$ , and the conditionally optimal decision set for $B$ , $D^{*}(B)$ , by

$$
v (B) = \max _ {d \in D} \sum_ {x \in B} \phi (x | B) \omega (x, d),\tag{5}
$$

and

$$
D ^ {*} (B) = \left\{d \in D \mid \sum_ {x \in B} \phi (x \mid B) \omega (x, d) = v (B) \right\},\tag{6}
$$

respectively.

Notice that we can equally well define $D^{*}(B)$ , the conditionally optimal set for $B$ , as

$$
\begin{array}{r l} D ^ {*} (B) & = \left\{d \in D \mid \sum_ {x \in B} \phi (x) \omega (x, d) \right. \\ & \quad \left. = \pi (B) v (B) \right\}. \end{array}\tag{7}
$$

Given this consideration, the following result becomes more or less immediate.

2.5.2. Proposition. If $\sigma = \langle \alpha, B_{r+1}, \delta \rangle$ is optimal for $D$ , then for each $B \in B_{r+1}$ we must have $\delta(B) \in D^{*}(B)$ . Furthermore, the expected gross payoff for $\sigma, \Omega(\sigma)$ , will be given by

$$
\Omega (\sigma) = \sum_ {B \in \mathbf {B} _ {r + 1}} \pi (B) v (B).
$$

Making use of the second part of Proposition 2.4.5. we can define a mapping from $\Sigma(D)$ to the family of all decision functions defined on $B^{A}$ which will sometimes be very useful in comparing the payoffs of two different feasible strategies, as follows.

2.5.3. Definition. Given a feasible strategy for D,

$$
\sigma = \left\langle \left(\mathbf {B} _ {1}, \alpha_ {1}\right), \dots , \left(\mathbf {B} _ {r}, \alpha_ {r}\right), \left(\mathbf {B} _ {r + 1}, \delta\right) \right\rangle ,
$$

we define $\delta_{\sigma}^{A}: B^{A} \to D$ by

$\delta_{\sigma}^{A}(B) = \delta(B')$ for that unique $B' \in \mathbf{B}_{r+1}$

such that $B \in \mathbf{B}^A(B')$ .

Our first use of this definition will be in conjunction with the following.

2.5.4. Definition. For each $d \in D$ we define $\pmb{B}^{A}(d) \subseteq \pmb{B}^{A}$ by

$$
\mathbf {B} ^ {A} (d) = \left\{B \in \mathbf {B} ^ {A} \mid d \in D ^ {*} (B) \right\}.
$$

We then define, for each $d \in D$ ,

$$
X _ {d} = \bigcup_ {\boldsymbol {B} \in \mathbf {B} ^ {A} (d)} B.
$$

2.5.5. Proposition. Suppose $\sigma^{*} = \langle (B_{1}^{*},\alpha_{1}^{*}),\ldots ,$ $(B_{r}^{*},\alpha_{r}^{*}),(B_{r + 1}^{*},\delta^{*})\rangle$ is a feasible strategy for $D$ satisfying

$$
\left(\forall B \in \mathbf {B} _ {r + 1} ^ {*}\right): B \subseteq X _ {\delta^ {*} (B)}.
$$

Then for any feasible strategy, $\sigma = \langle \alpha, B_{r+1}, \delta \rangle$ , we have

$$
\Omega (\sigma) \leq \Omega (\sigma^ {*}).
$$

Proof. We have, using Proposition 2.4.5.,

$$
\Omega (\sigma) = \sum_ {B \in \mathbf {B} _ {r + 1}} \sum_ {x \in B} \phi (x) \omega [ x, \delta (B) ]
$$

$$
\begin{array}{l} = \sum_ {B \in \mathbf {B} _ {r + 1}} \sum_ {B ^ {\prime} \in \mathbf {B} ^ {A} (B)} \sum_ {x \in B ^ {\prime}} \phi (x) \omega [ x, \delta (B) ] \\ = \sum_ {B \in \mathbf {B} _ {r + 1}} \sum_ {B ^ {\prime} \in \mathbf {B} ^ {A} (B)} \sum_ {x \in B ^ {\prime}} \phi (x) \omega [ x, \delta_ {\sigma} ^ {A} (B ^ {\prime}) ]. \end{array} \tag {8}\tag{8}
$$

However, since $B_{r+1}$ and $B_{r+1}^{*}$ are both partitions of X, we have

$$
\begin{array}{l} \sum_ {B \in \mathbf {B} _ {r + 1}} \sum_ {B ^ {\prime} \in \mathbf {B} ^ {A} (B)} \sum_ {x \in B ^ {\prime}} \phi (x) \omega [ x, \delta_ {\sigma} ^ {A} (B ^ {\prime}) ] \\ = \sum_ {B \in \mathbf {B} _ {r + 1} ^ {*}} \sum_ {B ^ {\prime} \in \mathbf {B} ^ {A} (B)} \sum_ {x \in B ^ {\prime}} \phi (x) \omega [ x, \delta_ {\sigma} ^ {A} (B ^ {\prime}) ] \\ = \sum_ {B \in \mathbf {B} _ {r + 1} ^ {*}} \sum_ {B ^ {\prime} \notin \mathbf {B} ^ {A} (B)} \pi (B ^ {\prime}) \sum_ {x \in B ^ {\prime}} \phi (x | B ^ {\prime}) \\ \times \omega [ x, \delta_ {\sigma} ^ {A} (B ^ {\prime}) ] \\ \leq \sum_ {B \in \mathbf {B} _ {r + 1} ^ {*}} \sum_ {B ^ {\prime} \in \mathbf {B} ^ {A} (B)} \pi (B ^ {\prime}) \sum_ {x \in B ^ {\prime}} \phi (x | B ^ {\prime}) \\ \times \omega [ x, \delta^ {*} (B) ]. \end{array}\tag{9}
$$

where the inequality is by the fact that for each $B \in B_{r+1}^{*}$ , $B \subseteq X_{\delta^{*}(B)}$ . Using this same fact, we have

$$
\begin{array}{l} \sum_ {B \in \mathbf {B} _ {r + 1} ^ {*}} \sum_ {B ^ {\prime} \in \mathbf {B} ^ {A} (B)} \pi (B ^ {\prime}) \sum_ {x \in B ^ {\prime}} \phi (x | B ^ {\prime}) \omega [ x, \delta^ {*} (B) ] \\ = \sum_ {B \in \mathbf {B} _ {r + 1} ^ {*}} \sum_ {B ^ {\prime} \in \mathbf {B} ^ {A} (B)} \sum_ {x \in B ^ {\prime}} \phi (x) \omega [ x, \delta^ {*} (B) ] \\ = \sum_ {B \in \mathbf {B} _ {r + 1} ^ {*}} \sum_ {x \in B} \phi (x) \omega [ x, \delta^ {*} (B) ] = \Omega (\sigma^ {*}), \end{array} \tag {10}\tag{10}
$$

where the second equality is by the first part of Proposition 2.4.5. Combining (8)-(10) yields the desired result. Q.E.D.

The following is an immediate implication of Proposition 8.

2.5.6. Corollary. If $B \subseteq X$ is $k$ -feasible, for some $k \in \{1, \ldots, n\}$ , and for some $d \in D$ we have $B \subseteq X_d$ ,

then $d\in D^{*}(B)$

## 3. Efficient, Admissible, and Optimal Strategies

## 3.1. Efficient Strategies

We begin our investigation here by showing that, in the case of a linearly-separable payoff function (section 2.3), our decision problem D satisfies the critical condition necessary for the application of dynamic programming techniques to obtain a solution. We first define the following.

3.1.1. Definition. If $\alpha = \langle (B_1, \alpha_1), \ldots, (B_r, \alpha_r) \rangle$ is a feasible information-gathering strategy for $D$ , and we define

$$
\mathbf {B} _ {r + 1} = R \left(\mathbf {B} _ {r}, \alpha_ {r}\right),
$$

then for each $q \in \{1, \ldots, r + 1\}$ , we define the expected cost of obtaining $\pmb{B}_q$ , $\hat{\gamma}(\pmb{B}_q)$ , by

$$
\hat {\gamma} \left(\mathbf {B} _ {q}\right) = \left\{ \begin{array}{l l} \sum_ {t = 1} ^ {q - 1} \sum_ {B \in \mathbf {B} _ {t}} \pi (B) c [ \alpha_ {t} (B) ] & \text { if } \quad q \geq 2, \\ 0 & \text { if } \quad q = 1. \end{array} \right.\tag{1}
$$

Using the above definition, we can establish that the expected net payoff of a feasible strategy decomposes as follows.

3.1.2. Proposition. If $\sigma = \langle (B_1, \alpha_1), \ldots, (B_r, \alpha_r), (B_{r+1}, \delta) \rangle$ is a feasible strategy for $D$ , we have, for any $q \in \{1, \ldots, r\}$ ,

$$
\begin{array}{l} \Omega (\sigma) - \Gamma (\sigma) \\ = \sum_ {B \in \mathbf {B} _ {q}} \left\{\sum_ {B ^ {\prime} \in \mathbf {B} _ {r} + 1 (B)} \sum_ {x \in B ^ {\prime}} \phi (x) \omega [ x, \delta (B ^ {\prime}) ] \right. \\ \left. - \sum_ {t = q} ^ {r} \sum_ {B ^ {\prime \prime} \in \mathbf {B} _ {t} (B)} \pi (B ^ {\prime \prime}) c [ \alpha_ {t} (B) ] \right\} - \hat {\gamma} (\mathbf {B} _ {q}). \end{array}\tag{2}
$$

Proof. Our result is trivial for $q = 1$ , while for $q \in \{2, \ldots, r\}$ , we have

$$
\begin{array}{l} \Omega (\sigma) - \Gamma (\sigma) \\ = \sum_ {B \in \mathbf {B} _ {r + 1}} \sum_ {x \in B} \phi (x) \omega [ x, \delta (B) ] \\ - \sum_ {t = 1} ^ {r} \sum_ {B \in \mathbf {B} _ {t}} \pi (B) c [ \alpha_ {t} (B) ] \\ = \sum_ {B \in \mathbf {B} _ {q}} \sum_ {B ^ {\prime} \in \mathbf {B} _ {r + 1} (B)} \sum_ {x \in B ^ {\prime}} \phi (x) \omega [ x, \delta (B) ] \\ - \sum_ {t = 1} ^ {q - 1} \sum_ {B \in \mathbf {B} _ {t}} \pi (B) c [ \alpha_ {t} (B) ] \\ - \sum_ {t = q} ^ {r} \sum_ {B \in \mathbf {B} _ {q}} \sum_ {B ^ {\prime} \in \mathbf {B} _ {t} (B)} \pi (B ^ {\prime}) \cdot c [ \alpha_ {t} (B ^ {\prime}) ] \end{array}
$$

$$
\begin{array}{l} = \sum_ {B \in \mathbf {B} _ {q}} \left\{\sum_ {B ^ {\prime} \in \mathbf {B} _ {r + 1}} \sum_ {x \in B ^ {\prime}} \phi (x) \omega [ x, \delta (B ^ {\prime}) ] \right. \\ \left. - \sum_ {t = q} ^ {r} \sum_ {B ^ {\prime \prime} \in \mathbf {B} _ {t} (B)} \pi (B ^ {\prime \prime}) c [ \alpha_ {t} (B ^ {\prime \prime}) ] \right\} - \hat {\gamma} (\mathbf {B} _ {q}), \end{array}
$$

where the second equality is by Lemma 2.2.9. Q.E.D.

Our decision problem, D, is defined by eight elements

$$
\mathbf {D} = \langle X, \phi , D, \omega , A, \{M _ {a} | a \in A \}, c, r \rangle .
$$

Notice, however, that, given any non-empty $B \subseteq X$ , and any positive integer, s, D can be used to define a decision problem, $D(B, s)$ , which is structurally equivalent to D, and is given by $^{10}$

$$
\begin{array}{c} \mathbf {D} (B, s) = \langle B, \phi (\cdot | B), D, \omega , A, \\ \{\iota (B, a) | a \in A \}, c, s \rangle , \end{array}
$$

where $\phi(\cdot|B)$ is the conditional density function defined by $\phi$ on B, i.e.,

$$
\phi (x \mid B) = \phi (x) / \pi (B) \quad \text { for } \quad x \in B.
$$

Furthermore, a feasible strategy for D defines feasible strategies for a number of such decision problems as is noted in the following, the proof of which is left to the reader (it follows easily from Lemma 2.2.9).

3.1.3. Lemma. Let $\sigma = \langle (B_1, \alpha_1), \ldots, (B_r, \alpha_r), (B_{r+1}, \delta) \rangle$ be a feasible strategy for $D$ . Then for each $q \in \{1, \ldots, r\}$ , and each $B \in B_q$ , $\sigma$ defines a feasible strategy for $D(B, r+1-q)$ , $\sigma(B, r+1-q)$ , by 11

$$
\begin{array}{r l} \sigma (B, r + 1 - q) & = \langle (\mathbf {B} _ {q} (B), \alpha_ {q}), (\mathbf {B} _ {q + 1} (B), \alpha_ {q + 1}), \dots , \\ & (\mathbf {B} _ {r} (B), \alpha_ {r}), (\mathbf {B} _ {r + 1} (B), \delta) \rangle . \end{array}
$$

If $\sigma = \langle (B_1, \alpha_1), \ldots, (B_r, \alpha_r), (B_{r+1}, \delta) \rangle$ is a feasible strategy for $D$ , and $q \in \{1, \ldots, r\}$ , then it follows at once from Proposition 2 that

$$
\begin{array}{l} \Omega (\sigma) - \Gamma (\sigma) \\ = \sum_ {B \in \mathbf {B} _ {q}} \pi (B) \left\{\sum_ {B ^ {\prime} \in \mathbf {B} _ {r + 1} (B)} \sum_ {x \in B ^ {\prime}} \phi (x | B) \right. \\ \times \omega [ x, \delta (B ^ {\prime}) ] \\ - \sum_ {t = q} ^ {r} \sum_ {B ^ {\prime \prime} \in \mathbf {B} _ {t} (B)} \pi (B ^ {\prime \prime} | B) c [ \alpha_ {t} (B ^ {\prime \prime}) ] \Bigg \} \\ - \hat {\gamma} (\mathbf {B} _ {q}). \end{array}\tag{3}
$$

Using (3) and Lemma 3, the following is then more or less immediate.

3.1.4. Theorem. If $\sigma = \langle (B_1, \alpha_1), \ldots, (B_r, \alpha_r), (B_{r+1}, \delta) \rangle$ is feasible for $D$ , then $\sigma$ is optimal for $D$ if, and only if, we have

for each $q \in \{1, \ldots, r\}$ , and each $B \in B_{q}$ , $\sigma(B, r+1-q)$ is optimal for $\mathbf{D}(B, r+1-q)$ . (4)

Theorem 4 shows that our problem satisfies Bellman's fundamental necessary condition for the application of dynamic programming (Bellman [1957, p. 83]).

An optimal policy has the property that, whatever the initial state and initial decisions are, the remaining decisions must constitute an optimal policy with regard to the state resulting from the first decision.

Unfortunately, there is generally no effective way to work backward from a k-feasible set $B \subseteq X$ ( $k \in \{1, \ldots, r\}$ ) to develop an optimal strategy on the basis of backward induction techniques. However, in section 6 we will develop one special case (which includes the computer file search problem as a subcase) in which we can fruitfully apply backward induction to obtain an optimal solution. In the meantime, our main technique for simplifying the problem of obtaining a solution for the general case revolves around the use of the following.

3.1.5. Definition. If $\sigma = \langle \alpha, B_{r+1}, \delta \rangle$ and $\sigma^* = \langle \alpha^*, B_{r+1}^*, \delta^* \rangle$ are feasible strategies for $D$ , we shall say that $\sigma^*$ (weakly) dominates $\sigma$ [respectively, strictly dominates $\sigma$ ], iff

$$
\begin{array}{l} \Omega (\sigma^ {*}) - \Gamma (\sigma^ {*}) \geq \Omega (\sigma) - \Gamma (\sigma) \\ \left[ \text { respectively }, \Omega (\sigma^ {*}) - \Gamma (\sigma^ {*}) > \Omega (\sigma) - \Gamma (\sigma) \right]. \end{array}
$$

3.1.6. Definition. We shall say that a non-empty set $\Sigma^{*} \subseteq \Sigma(D)$ is a dominating (strategy) set for $D$ iff

$$
\begin{array}{l} \big (\forall \sigma \in \Sigma (D) \big) \big (\exists \sigma^ {*} \in \Sigma^ {*} \big): \Omega (\sigma^ {*}) - \Gamma (\sigma^ {*}) \\ \qquad \geq \Omega (\sigma) - \Gamma (\sigma), \end{array}\tag{5}
$$

(so that $\sigma^{*}$ dominates $\sigma$ ).

The following is a straightforward modification of a standard result in decision theory, and is easily proved.

3.1.7. Proposition. If $\Sigma^{*} \subseteq \Sigma(D)$ is a dominating set for $D$ , and if $\sigma^{*} \in \Sigma^{*}$ satisfies

$$
(\forall \sigma \in \Sigma^ {*}): \Omega (\sigma^ {*}) - \Gamma (\sigma^ {*}) \geq \Omega (\sigma) - \Gamma (\sigma),
$$

then $\sigma^{*}$ is optimal for $D$ .

Proposition 3.1.7 states that we can simplify our search for an optimal strategy for D in that we can confine our search to an appropriately chosen dominating set for D. In our theoretical work, the dominating set with which we shall work is the set of ‘efficient’ strategies for D, as defined below.

3.1.8. Definition. We shall say that a feasible information-gathering strategy for D,

$$
\pmb {\alpha} = \langle (\mathbf {B} _ {1}, \alpha_ {1}), \dots , (\mathbf {B} _ {r}, \alpha_ {r}) \rangle ,
$$

is efficient iff

(i) for each $t \in \{1, \ldots, r - 1\}$ , and each $B \in B_t$ , we have

if $\alpha_{t}(B) = 0$ , then $\alpha_{t+1}(B) = 0$ ,

(note that if $\alpha_{t}(B) = 0$ , then $B \in B_{t+1}$ ), and (ii) for each $t \in \{1, \ldots, r\}$ , and each $B \in B_{t}$ ,

(a) if $\alpha_{t}(B) = \hat{a} \neq 0$ , then $\# \iota(B, \hat{a}) \geq 2$ ,

$$
\begin{array}{l l} \text {(b)} & \text { if,   for   some } \quad d \in D, B \subseteq X _ {d}, \\ & \text { then } \quad \alpha_ {t} (\mathbf {B}) = 0. \end{array}
$$

3.1.9. Definition. We shall say that a feasible strategy for $D$ , $\sigma = \langle \alpha, B_{r+1}, \delta \rangle$ , is efficient iff (i) $\alpha$ is an efficient information-gathering strategy for $D$ , and

(ii) for each $B \in B_{r+1}$ , $\delta(B) \in D^{*}(B)$ .

We shall denote the set of all efficient strategies for D by $\Sigma^{e}(D)$ .

The key fact needed to establish that $\Sigma^{e}(\boldsymbol{D})$ is a dominating set for D is the following.

3.1.10. Proposition. If $B \subseteq X$ is $k$ -feasible for some $k \in \{1, \ldots, n\}$ and $d^* \in D$ is such that $B \subseteq X_{d^*}$ , then for every feasible information structure on $\mathbf{B}$ , $^{12} \mathbf{B}$ , and every $\delta: \mathbf{B} \to D$ , we have

$$
\begin{array}{l} \sum_ {B ^ {\prime} \in \mathbf {B}} \sum_ {x \in B ^ {\prime}} \phi (x) \omega [ x, \delta (B ^ {\prime}) ] \\ \leq \sum_ {x \in B} \phi (x) \omega (x, d ^ {*}) = \pi (B) v (B). \end{array}\tag{5}
$$

Proof. Suppose B is a feasible information structure on B, and that $\delta: B \rightarrow D$ . Then

$$
\mathbf {B} ^ {A} (B) \geq \mathbf {B},
$$

and hence we have

$$
\begin{array}{l} \sum_ {B ^ {\prime} \in \mathbf {B}} \sum_ {x \in B ^ {\prime}} \phi (x) \omega [ x, \delta (B ^ {\prime}) ] \\ = \sum_ {B ^ {\prime} \in \mathbf {B}} \sum_ {B ^ {\prime \prime} \in \mathbf {B} ^ {A} (B ^ {\prime})} \pi (B ^ {\prime \prime}) \sum_ {x \in B ^ {\prime \prime}} \phi (x | B ^ {\prime \prime}) \\ \times \omega [ x, \delta (B ^ {\prime}) ] \\ \leq \sum_ {B ^ {\prime} \in \mathbf {B}} \sum_ {B ^ {\prime \prime} \in \mathbf {B} ^ {A} (B ^ {\prime})} \pi (B ^ {\prime \prime}) \sum_ {x \in B ^ {\prime \prime}} \phi (x | B ^ {\prime \prime}) \\ \times \omega (x, d ^ {*}) \\ = \sum_ {B ^ {\prime} \in \mathbf {B}} \sum_ {B ^ {\prime \prime} \in \mathbf {B} ^ {A} (B ^ {\prime})} \sum_ {x \in B ^ {\prime \prime}} \phi (x) \omega (x, d ^ {*}) \\ = \sum_ {x \in B} \phi (x) \omega (x, d ^ {*}), \end{array}
$$

where the inequality follows from the fact that for each $B' \in B$ , we have $\boldsymbol{B}^{A}(\boldsymbol{B}') \subseteq \boldsymbol{B}^{A}(\boldsymbol{B})$ .

The above argument establishes the inequality in (5). To prove the equality, we note that, since $B = \{B\}$ is a particular feasible information structure for B, we have, for any $d \in D$

$$
\begin{array}{r l} & {\pi (B) \sum_ {x \in B} \phi (x | B) \omega (x, d)} \\ & {\quad = \sum_ {x \in B} \phi (x) \omega (w, d)} \\ & {\quad \leq \sum_ {x \in B} \phi (x) \omega (x, d ^ {*})} \\ & {\quad = \pi (B) \sum_ {x \in B} \phi (x | B) \omega (x, d ^ {*}).} \end{array}
$$

$$
\begin{array}{l} \text { Thus   for   all } d \in D \\ \sum_ {x \in B} \phi (x | B) \omega (x, d) \leq \sum_ {x \in B} \phi (x | B) \omega (x, d ^ {*}), \end{array}
$$

which establishes the equality in (5). Q.E.D.

The proof of the following is then conceptually easy, though a bit tedious. Since the result also appears to be fairly obvious, we shall leave the proof to the interested reader.

3.1.11. Theorem. The set of efficient strategies for $\pmb{D}$ , $\Sigma^e(\pmb{D})$ , is a dominating set for $\pmb{D}$ .

## 3.2. Admissible Strategies

The criterion for efficiency, as developed in the previous sub-section, is fairly straightforward, and we will find it very useful in our analytic work in the section to follow. The hypotheses of the results we shall present in this subsection can be used to define the notion of an admissible strategy; and if we require that an admissible strategy also be efficient, the set of admissible strategies will be a dominating set for D, and a proper subset of $\Sigma^{e}(D)$ . However, a full formal definition of an admissible strategy is very messy, and we shall not be able to put it to much use in the section to follow. Consequently, we shall not formally state a definition of an admissible strategy here. However, the results to follow are quite useful in trying to solve an actual realization of our decision problem.

3.2.1. Proposition. Suppose $\sigma = \langle (B_1, \alpha_1), \ldots, (B_r, \alpha_r), (B_{r+1}, \delta) \rangle$ is feasible for $D$ , and that there exists $q \in \{1, \ldots, r\}$ , $B^* \in B_q$ , and $a^* \in A$ such that

$$
\begin{array}{l l} \iota (B ^ {*}, a ^ {*}) \geq \iota [ B ^ {*}, \alpha_ {q} (B ^ {*}) ] & \text { and } \\ c (a ^ {*}) \leq c [ \alpha_ {q} (B ^ {*}) ]. \end{array}\tag{1}
$$

Then $\sigma$ is dominated.

Proof. Suppose there exist $B^{*} \in B_{q}$ and $a^{*} \in A$ satisfying (1). We then construct a strategy $\sigma^{*}$ by modifying $\sigma$ as follows. We let

$$
\begin{array}{l} \left(\mathbf {B} _ {t} ^ {*}, \alpha_ {t} ^ {*}\right) = \left(\mathbf {B} _ {t}, \alpha_ {t}\right) \quad \text { for } \quad t = 1 q - 1, \\ \alpha_ {t} ^ {*} (B) = \alpha_ {t} (B) \quad \text { for } \quad B \in \mathbf {B} _ {t} \backslash \mathbf {B} _ {t} (B ^ {*}), \\ t = q, \dots , r, \end{array}
$$

and

$\delta^{*}(B) = \delta(B)\quad \text{for} \quad B \in \mathbf{B}_{r+1} \setminus \mathbf{B}_{r+1}(B^{*}).$ Further, for $B \in \mathbf{B}_{t}^{*}(B^{*})(t = q, \ldots, r)$ , let $\alpha_{t}^{*}(B) = \alpha_{t}(B')$ for that unique $B' \in \mathbf{B}_{t}(B')$ for which $B \subseteq B'$ ,

and finally let

$$
\delta^ {*} (B) \in D ^ {*} (B) \quad \text { for } \quad B \in \mathbf {B} _ {r + 1} ^ {*} (B ^ {*}).
$$

It is then easy to show that

$$
\Gamma (\sigma^ {*}) \leq \Gamma (\sigma),
$$

and we have

$$
\begin{aligned} \Omega (\sigma^{*}) & = \sum_{B\in \mathbf{B}_{r + 1}^{*}}\sum_{x\in B}\phi (x)\omega [x,\delta^{*}(B)] \\ & = \sum_{B\in \mathbf{B}_{r + 1}^{*}\setminus \mathbf{B}_{r + 1}^{*}(B^{*})}\sum_{x\in B}\phi (x)\omega [x,\delta^{*}(B)]\\ & \quad +\sum_{B\in \mathbf{B}_{r + 1}^{*}(B^{*})}\pi (B)v(B)\\ & \geq \sum_{B\in \mathbf{B}_{r + 1}\setminus \mathbf{B}_{r + 1}(B^{*})}\sum_{x\in B}\phi (x)\omega [x,\delta (B)]\\ & \quad +\sum_{B\in \mathbf{B}_{r + 1}(B^{*})}\sum_{\substack{B^{\prime}\in \mathbf{B}_{r + 1}^{*}(B^{*})\\ B^{\prime}\subseteq B}}\sum_{x\in B^{\prime}}\phi (x)\\ & \quad \times \omega [x,\delta (B)]\\ & = \sum_{D\in \mathbf{B}_{r + 1}\setminus \mathbf{B}_{r + 1}(B^{*})}\sum_{x\in B}\phi (x)\omega [x,\delta (B)]\\ & \quad +\sum_{B\in \mathbf{B}_{r + 1}(B^{*})}\sum_{x\in B}\phi (x)\omega [x,\delta (B)]\\ & = \Omega (\sigma). \qquad \text{Q.E.D.} \end{aligned}
$$

The following can be proved by an argument very similar to the proof of Proposition 2.5.8. We will leave the details of the proof to the interested reader.

3.2.2. Proposition. If $\sigma = \langle (B_1, \alpha_1), \ldots, (B_r, \alpha_r), (B_{r+1}, \delta) \rangle$ is a feasible strategy for $D$ such that there exists $q \in \{1, \ldots, r\}$ and $B \in B_q$ with $\# \mathbf{B}_{r+1}(B) > 1$ and $\bigcap_{B' \in \mathbf{B}_{r+1}(B)} D^*(B') \neq \phi$ ,

then $\sigma$ is dominated.

The following two results provide two fundamental ‘working formulas’ for the construction of admissible strategies for a specific realization of our decision problem. One can then compare the expected net payoffs of the admissible strategies to obtain an optimal strategy. We shall not attempt to set forth an algorithm here, since we have as yet no very efficient algorithm for the general case. We shall, however, be able to present quite effective algorithms for special cases in section 6.

3.2.3. Proposition. If $\sigma = \langle (B_1, \alpha_1), \ldots, (B_r, \alpha_r), (B_{r+1}, \delta) \rangle$ is a feasible strategy for $D$ such that, for some $B^* \in B_{r+1}$ , $q \in \{1, \ldots, r\}$ , and $\bar{a} \in A$ , we have

$$
(a) a (q, B ^ {*}) = 0,
$$

$$
\begin{array}{l} (b) \sum_ {B ^ {\prime} \in t (B ^ {*}, \bar {a})} \pi (B ^ {\prime}) v (B ^ {\prime}) \\ - \sum_ {x \in B ^ {*}} \phi (x) \omega [ x, \delta (B ^ {*}) ] > \pi (B ^ {*}) c (\bar {a}), \end{array}
$$

then $\sigma$ is strictly dominated.

$$
\begin{array}{l} \text { Proof.   Let } \\ B ^ {\tau} \equiv \beta_ {q} (B ^ {*}), \end{array}
$$

and define a new strategy, $\sigma^{*}$ , by first letting

$$
\alpha_ {t} ^ {*} (B) = \alpha_ {t} (B) \quad \text { for   all } \quad B \in \mathbf {B} _ {t} \setminus \mathbf {B} _ {t} (B ^ {\tau}),
$$

and

$$
\begin{array}{l l} \alpha_ {t} ^ {*} (B) = \alpha_ {t + 1} (B) & \text { for } \quad B \in \mathbf {B} _ {t} (B ^ {\tau}), \\ t = q, \ldots , r - 1, \end{array}
$$

$$
\alpha_ {r} ^ {*} (B) = \left\{ \begin{array}{l l} 0 & \text { for } \quad B \in \mathbf {B} _ {r + 1} (B ^ {\tau}) \setminus \{B ^ {*} \}, \\ \bar {a} & \text { for } \quad B = B ^ {*}. \end{array} \right.
$$

It is clear that the information-gathering strategy just defined, $\alpha^{*} = \langle (B_{1}^{*},\alpha_{1}^{*}),\ldots ,(B_{r}^{*},\alpha_{r}^{*})\rangle$ has the property that, defining

$$
\mathbf {B} _ {r + 1} ^ {*} = R \left(\mathbf {B} _ {r} ^ {*}, \alpha_ {r} ^ {*}\right),
$$

we have

$$
\mathbf {B} _ {t} ^ {*} = \left\{ \begin{array}{l l} \mathbf {B} _ {t} & \text { for } \quad t = 1, \dots , q, \\ \left[ \mathbf {B} _ {t} \setminus \mathbf {B} _ {t} (B ^ {\tau}) \right] \cup \mathbf {B} _ {t + 1} (B ^ {\tau}) \\ & \text { for } \quad t = q + 1, \dots , r - 1, \end{array} \right.
$$

and

$$
\mathbf {B} _ {r + 1} ^ {*} = \left[ \mathbf {B} _ {r + 1} \setminus \{B ^ {*} \} \right] \cup \iota (B ^ {*}, \bar {a}).
$$

Thus we can complete our definition of $\sigma^{*}$ by defining

$$
\delta^ {*} (B) = \delta (B) \quad \text { for } \quad B \in \mathbf {B} _ {r + 1} \setminus \{B ^ {*} \},
$$

and letting

$$
\delta^ {*} (B) \in D ^ {*} (B) \quad \text { for } \quad B \in \iota (B ^ {*}, \bar {a}).
$$

Furthermore, it is also apparent that

$$
\begin{array}{l} \Gamma (\alpha^ {*}) = \hat {\gamma} (\mathbf {B} _ {q} ^ {*}) + \sum_ {t = q} ^ {r} \sum_ {B \in \mathbf {B} _ {t}} \pi (B) c [ \alpha_ {t} ^ {*} (B) ] \\ = \hat {\gamma} (\mathbf {B} _ {q}) + \sum_ {t = q} ^ {r} \left\{\sum_ {B \in \mathbf {B} _ {t} ^ {*} \backslash \mathbf {B} _ {t} ^ {*} (B ^ {\tau})} \pi (B) c [ \alpha_ {t} ^ {*} (B) ] + \sum_ {B \in \mathbf {B} _ {t} ^ {*} (B ^ {\tau})} \pi (B) c [ \alpha_ {t} ^ {*} (B) ] \right\} \\ = \hat {\gamma} (\mathbf {B} _ {q}) + \sum_ {t = q} ^ {r - 1} \left\{\sum_ {B \in \mathbf {B} _ {t} \backslash \mathbf {B} _ {t} (B ^ {v _ {t}})} \pi (B) c [ \alpha_ {t} (B) ] + \sum_ {B \in \mathbf {B} _ {t + 1} (B ^ {\tau})} \pi (B) c [ \alpha_ {t + 1} (B) ] \right\} \\ + \sum_ {B \in \mathbf {B} _ {r} \backslash \mathbf {B} _ {r} (B ^ {\tau})} \pi (B) c [ \alpha_ {r} (B) ] + \pi (B ^ {*}) c (\bar {a}) \\ = \Gamma (\sigma) + \pi (B ^ {*}) c (\bar {a}), \end{array} \tag {2}
$$

where the last equality is by the fact that

$$
\alpha_ {q} (B ^ {\tau}) = 0,
$$

and hence

$$
c \left[ \alpha_ {q} (B ^ {\tau}) \right] = 0.
$$

Finally, we have

$$
\begin{array}{r l} \Omega (\sigma^ {*}) & = \sum_ {B \in \mathbf {B} _ {r + 1} ^ {*}} \phi (x) \omega [ x, \delta^ {*} (B) ] \\ & = \sum_ {B \in \mathbf {B} _ {r + 1} ^ {*} \setminus \iota (B ^ {*}, \bar {a})} \phi (x) \omega [ x, \delta^ {*} (B) ] \\ & \quad + \sum_ {B \in \iota (B ^ {*}, \bar {a})} \phi (x) \omega [ x, \delta^ {*} (B) ] \\ & = \sum_ {B \in \mathbf {B} _ {r + 1} \setminus \{B ^ {*} \}} \phi (x) \omega [ x, \delta (B) ] \\ & \quad + \sum_ {B \in \iota (B ^ {*}, \bar {a})} \pi (B) v (B) \\ & = \Omega (\sigma) - \sum_ {x \in \mathbf {B} ^ {*}} \phi (x) \omega [ x, \delta (B ^ {*}) ] \\ & \quad + \sum_ {B \in \iota (B ^ {*}, \bar {a})} \pi (B) v (B). \end{array}\tag{3}
$$

From (2) and (3) we have

$$
\begin{array}{l} \Omega (\sigma^ {*}) - \Gamma (\sigma^ {*}) - [ \Omega (\sigma) - \Gamma (\sigma) ] \\ = \sum_ {B \in \iota (B ^ {*}, \bar {a})} \pi (B) v (B) \end{array}
$$

$$
- \sum_ {x \in B ^ {*}} \phi (x) \omega [ x, \delta (B ^ {*}) ] - \pi (B ^ {*}) c (\bar {a}),\tag{4}
$$

which, by hypothesis is strictly positive. Therefore $\sigma$ is strictly dominated. Q.E.D.

3.2.4. Proposition. If $\sigma = \langle (\pmb{B}_1, \alpha_1), \ldots, (\pmb{B}_r, \alpha_r), (\pmb{B}_{r+1}, \delta) \rangle$ is a feasible strategy for $\pmb{D}$ , and for some $B^* \in B_r$ we have, writing $a^* = \alpha_r(B^*)$ : there exists $d^* \in D$ such that

$$
\begin{array}{l} \sum_ {B \in \iota (B ^ {*}, a ^ {*})} \sum_ {x \in B} \phi (x) \omega [ x, \delta (B) ] - \pi (B ^ {*}) c (a ^ {*}) \\ <   \sum_ {x \in B ^ {*}} \phi (x) \omega (x, d ^ {*}), \end{array} \tag {5}
$$

then $\sigma$ is strictly dominated.

Proof. This result is the mirror image of Proposition 3, and the proof is very similar. This time we modify $\sigma$ to obtain a new strategy $\sigma^{*}$ , by changing only two things

$$
\alpha_ {r} ^ {*} (B ^ {*}) = 0,
$$

and

$$
\delta^ {*} (B ^ {*}) = d ^ {*}.
$$

It is then easily shown that (5) implies

$$
\Omega (\sigma^ {*}) - \Gamma (\sigma^ {*}) > \Omega (\sigma) - \Gamma (\sigma).\tag{Q.E.D.}
$$

Appendix

In this appendix we shall discuss some possible generalizations of our Decision Model I; and, in the process, provide a rationalization of our assumption that a fixed maximum number of information-gathering steps can be undertaken before a final decision is made.

The generalizations we wish to discuss can all formally be incorporated into our basic model by adding a ninth element to the eight we are presently using to define our decision problem D (see section 2.1), namely a set

$$
\mathbf {S} \subseteq A ^ {n} \times D \times \mathbf {P} (X),
$$

to represent the allowable sequences of information-gathering actions and final decisions. Correspondingly, we would then add a fourth requirement to the definition of a feasible strategy for D (Definition 2.2.5), viz.

(4) for each $B \in B_{r+1}$ , $(a(B), \delta(B), B) \in S$ (see Definition 2.3.1).

The two possible reasons that one might have for wishing to take account of some such restriction which we would like to discuss here are the following.

First, in a more complete model, one might wish to express a limitation on the information-gathering process via a time constraint, T. The idea here is that, in order to define feasible strategies, we need to take into account the fact that the experiments (initial actions) will take time to complete, that decisions $d \in D$ may take varying amounts of time to implement, and that all of this needs to be completed within the time constraint of T hours.

As we see it, the time constraint, T, comes about in the following way. Our formulation of the information structures associated with the experiments $a \in A$ implicitly assumes that a given experiment would, if performed twice in a particular realization of the problem, yield the same result both times. Thus, to take the example of medical diagnosis, the applicability of our model requires that, during the period of information-gathering, if a given patient's temperature were to be taken twice, the same reading would be obtained on both occasions. $^{13}$ Since the patient's condition would presumably change over time, this would put an upper bound of, say T hours, on the period of time during which it would be reasonable, even as a first approximation, to suppose this assumption holds. In other applications an upper limit might be placed on the period of time available to obtain a solution on the grounds of providing a safety margin, meeting a deadline, and so on.

In any case, in order to define the feasible strategies in such a way as to take these time constraints into account, we can proceed as follows. Let the function $\tau: A_{1} \to R_{+}$ be defined

by $^{14}$

$\tau(a)$ is the time required to carry out and evaluate experiment $a$ , for $a \in A_1$ , and assume that

$$
(\forall a \in A _ {1}): \tau (a) > 0 \quad \text { and } \quad \tau (0) = 0.
$$

Furthermore, let the function $t: D \times B \to \mathbb{R}_+$ be defined by

$t(d, B)$ is the time required to evaluate $\delta(B)$ (if $d = \delta(B)$ ) and to implement decision $d$ , $^{15}$

where B denotes the collection of n-feasible sets (see section 2.4). With this notation, we can take the time constraint into account by requiring that a strategy $\sigma=\langle(\alpha,B_{r+1},\delta)\rangle$ be feasible only if for each $B\in B_{r+1}$ ,

$$
\sum_ {s = 1} ^ {r (B)} \tau [ a (s, B) ] + t [ \delta (B), B ] \leq T,\tag{1}
$$

where $r(B)$ is the number of information-gathering actions taken to arrive at B. However, in this situation, there are quite significant notational advantages to be gained from the following procedure.

Let Z denote the set of integers, and define $N: R \to Z$ by: $N(x) = \text{that unique } N \in Z$ satisfying $N - 1 < x \leq N$ , and let

$$
\begin{array}{l} \tau^ {*} = \min \bigl \{\tau (a) | a \in A _ {1} \bigr \}, \\ t ^ {*} = \min \bigl \{t (d, B) | d \in D \& B \in \mathbf {B} \bigr \}, \end{array}
$$

and

$$
r = \min \left\{N \left[ (T - t ^ {*}) / \tau^ {*} \right], n \right\}.
$$

Since $\tau(0)=0$ , we can then suppose that each feasible information-gathering strategy takes exactly $r$ steps along each path; for if $\sigma=\langle\alpha, B_{r+1}, \delta\rangle$ satisfies (1), then for each $B\in B_{r+1}$ we have

$$
\begin{array}{r l} T - t ^ {*} & \geq T - t [ \delta (B), B ] \geq \sum_ {s = 1} ^ {r (B)} \tau [ a (s, B) ] \\ & \geq r (B) \tau^ {*}, \end{array}
$$

so that

$$
r (B) \leq (T - t ^ {*}) / \tau^ {*} \leq N [ (T - t ^ {*}) / \tau^ {*} ].
$$

Since for an efficient strategy we will also have $r(B) \leq n$ ,

it then follows that

$$
r (B) \leq \min \left\{N [ T - t ^ {*}) / \tau^ {*} ], n \right\} \equiv r.
$$

However, while the above argument establishes the fact that we can suppose that each feasible strategy takes exactly r information-gathering steps, not all information-gathering strategies taking r steps will satisfy condition (1). On the other hand, we can eliminate this difficulty by requiring condition 4 (set forth at the beginning of this appendix) in our definition of a feasible strategy, where

$$
\begin{array}{l} \mathbf {S} = \left\{\left(a _ {1}, \dots , a _ {r}, d, B\right) \in A ^ {r} \times D \times \mathbf {B} \mid \right. \\ \left. \sum_ {s = 1} ^ {r} \tau (a _ {s}) + t (d, B) \leq T \right\}. \end{array}\tag{2}
$$

In the text we have essentially assumed that

$$
(\forall a \in A _ {1}): \tau (a) = \tau^ {*},
$$

and

$$
(\forall (d, B) \in D \times \mathbf {B}): t (d, B) = t ^ {*},
$$

so that (1) [and condition 4, for $S$ defined as in (2)] becomes superfluous.

On the other hand, another rationale for the inclusion of condition 4 is that we may not always be able to perform the initial actions in A in an arbitrary order. Thus, for example, there is some appeal in the notion of treating sequential sampling as a special case of our problem (it is more naturally considered as a special case of our Model II, however) in which we assume that we can take up to n samples, and that, for $a \in A_{1}$ , experiment a consists of taking the a th sample. In this case, and considering only this constraint, we can taken r = n, and

$$
\begin{array}{l} \mathbf {S} = \left\{\mathbf {a} \in A ^ {n} \mid a _ {1} \in \{0, 1 \} \text {   and   } a _ {i + 1} \in \{0, a _ {i} + 1 \} \right. \\ \text { for } \quad i = 1, \ldots , r - 1 \}. \end{array}
$$

Another sort of additional constraint of which we might wish to take account stems from the fact that in some cases one might not regard an experiment as being feasible unless it were known that $\hat{x}$ , the true state, were an element of some proper subset of the state space. For example, a chemist conducting an analysis of an unknown liquid would presumably not attempt to determine its boiling point until he has determined that the liquid is not nitroglycerin! We would take this constraint into account by adding a fifth condition to Definition 2.2.5, as follows:

(5) for each $t \in \{1, \ldots, r\}$ , and each $B \in B_t$ ,

$$
B \subseteq X _ {\alpha_ {i} (B)},
$$

where $X_{a} =$ that subset of $X$ where experiment $a \in A$ may be used (with $X_0 = X$ ).

We ignore this sort of complication in the text of this paper, however; or, effectively, we assume

$$
X _ {a} = X \quad \text { for   each } \quad a \in A,
$$

so that condition 5 becomes superfluous.

## References

Bellman, R. (1957). Dynamic Programming, Princeton University Press, New Jersey.

Bonczek, R.H., Holsapple, C.W. and Whinston, A.B. (1981). Foundations of Decision Support Systems, Academic Press.

DeGroot, H.M. (1970). Optimal Statistical Decisions, McGraw-Hill, Inc.

Jacob, V.S., Moore, J.C. and Whinston, A.B. (1986). "A Decision Theoretic Perspective of the Integrated Human-Machine Information Processor", Proc. of the 1st International Conference on Economics and Artificial Intelligence, Pergamon Press, forthcoming 1986.

Marschak, J. and Miyasawa, K. (1968). "Economic Comparability of Information Systems", International Economic Review, 9, 137–174.

Marschak, J. and Radner, R. (1972). Economic Theory of Teams, Cowles Foundation.
