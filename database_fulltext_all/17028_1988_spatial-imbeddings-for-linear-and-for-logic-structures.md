---
otero_id: 17028
otero_key: "WTX7C9F4"
title: "Spatial imbeddings for linear and for logic structures"
authors: "Robert G. Jeroslow"
year: "1988"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(88)90098-x"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Spatial Imbeddings for Linear and for Logic Structures $^{1}$

Robert G. JEROSLOW

College of Management, Georgia Institute of Technology, Atlanta, GA 30332, USA

We introduce the concept of a spatial imbedding of a model structure which contains fields for both spatial and nonspatial elements, and we obtain a necessary and sufficient condition for imbeddability of a model. As shown in examples, the concept of an imbedding allows us to unify traditional MIP modelling techniques with the logic-based approaches of artificial intelligence.

Keywords: Mixed Integer Programming, Logic Programming, Disjunctive Methods, Knowledge Representation.

![](/api/attachments/WTX7C9F4/fulltext/images/3b79b4ea963482271fa84b48371e017108ee20e38eb0eb37ee32d2e264b83d01.jpg)

Robert G. Jeroslow is a Professor in the College of Management at the Georgia Institute of Technology. He received the B.S. in Industrial Engineering from Columbia University in 1964 and the Ph.D. in Mathematical Logic from Cornell University in 1969. His research interests are applied artificial intelligence, decision support systems, information systems, applied logic, knowledge representation for discrete optimization, operations management, strategy, and strategic planning.

## 1. Introduction

Spatial imbeddings provide a conceptual unification of aspects of discrete programming, database theory and logic which often occur together in applications. For instance, corporations keep records in their databases of customers, customer addresses and orders, payments received, credit worthiness, permissible substitutions in orders, etc. The distribution network of a corporation is typically represented separately, in an Operations Research model, which may also be supplemented by a model for corporate cash flow. Many queries arise in the management of the corporation, involving, e.g., revenue projections by customer and geographic groupings if various distribution links are either closed or expanded. Some of these queries involve logical deduction, e.g., a customer's payment terms may depend on both its credit worthiness and the corporate cash position (leading to 'if...then...' conditions).

The concept of an imbedding is intended to subsume a significant number of applications which combine deterministic discrete optimization with databases and logic, in which the emphasis is on the ability to process a large family of different queries (see (3.11) and (3.13) below). For more efficient processing of a small set of queries, much of the apparatus of an imbedding would be 'stripped out', although the concept remains useful.

Imbeddings provide a (Euclidean) spatial interpretation for all three aspects of such queries – the programming aspects (which are ‘already spatial’), as well as the database and logic aspects. Via this uniformity of treatment, through the process of analogy it can be possible to adapt database and logic algorithms to aid in mixed-integer programming (where they often behave as preprocessing routines), while of course spatial algorithms (such as simplex pivoting) and techniques of spatial representation are available for database and logic tasks.

The concept of an imbedding allows us to unify traditional MIP modelling, and extensions of these as reported in [31], with the logic-based approaches to artificial intelligence [43], [50], [54] as in [7], [35], [39], [41], [44] and [45]. In this manner, linear structural constraints which naturally occur in applications (e.g., capacity restrictions, material balance, economies of scale, etc.) can be treated along with logical constraints.

Mixed integer programming formulations are naturally designed to treat linear structure imposed on propositional logic constraints. When the MIP tree search algorithms are literally used on problems containing propositional logic alone, they in fact produce logic algorithms that are very similar to well-known algorithms, but have features which generally make them faster (see [6]).

Predicate logic is treated by a sequence of partial reductions to propositional logic (see [33]). When this is done in an MIP framework the resulting algorithms are in the spirit of [41], in that linear programming corresponds to fast sub-routines (e.g., unit resolution), with other resolution-like steps (e.g., branching) postponed until they are unavoidable. In addition – and this is crucial – fast heuristics used during the search attempt to find satisfying truth valuations, in order to terminate the search early. A theoretical result on predicate logic for linear constraints is stated in section 5.

The results reported in this paper are largely of a conceptual, and not of an algorithmic, nature. They were reported earlier as a part of an unpublished report [32]. Here we build directly on our earlier work on MIP representability [28]–[31], which in turn draws from two earlier developments. One of these developments is the disjunctive methods of cutting-plane theory (e.g., [1], [2], [3], [5], [18], [19], [26], [27], [55]); the other is the growing interest in techniques of MIP formulation, with particular emphases on those formulations with superior linear relaxations (e.g., [13], [17], [25], [37]–[40], [52], [53]).

As MIP algorithms use the linear relaxation to approximate MIP problems and to guide the search, the quality of that relaxation naturally emerges as crucial. The issue of MIP formulation is related to that of knowledge representation in artificial intelligence. Some earlier and relevant results on MIP formulation are summarized in section 2.

We have also been particularly influenced by the vision of broad-ranging decision-support as articulated in [8], and we have benefitted from earlier work on boolean methods [21], [22], [23].

As regards issues of notation, for a set $S \subseteq R^{n}$ in Euclidean space $R^{n}$ , we let $\text{conv}(S)$ respectively $\text{cl}(S)$ respectively $\text{clconv}(S)$ respectively $\text{cone}(S)$ , denote the convex span resp. the closure resp. the closed, convex span resp. the convex cone, generated by S. For results on linear and convex programming and convexity, we use [46] and [51] as general references. For a polyhedron P, rec (P) denotes its recession cone.

## 2. A Summary of MIP Representability and the Linear Relaxations of Representations

We summarize material from [28], [29], [30], [31].

A set $S \subseteq R^n$ in Euclidean space $R^n$ is bounded-MIP-representable (b-MIP.r) if there are matrices $A$ and $B$ , a vector $b$ , and an index set $K$ for a subset of the indices of a vector of 'parameters' $y$ , such that

$x\in S\Leftrightarrow$ for some $y$ with $y_{k}\in \{0,1\}$

$$
\text { for   all } k \in K, A x + B y = b.\tag{2.1}
$$

Briefly put, b-MIP.r sets S are exactly projections of mixed-integer constraint sets in binary variables. The term ‘bounded’ is used since the ‘control variables’ ( $y_{k} \mid k \in K$ ) are binary; the set S itself need not be bounded (The letter b in ‘b-MIP’ has no relation to the entirely general r.h.s. b in (2.1).) The constraints on the right-hand-side in (2.1) (together with K) are a b-MIP representation of S.

Often we shall call b-MIP.r sets S simply 'representable'. The more complex terminology is needed in other settings, where other concepts of representability occur.

A function $f$ is called min-b-MIP.r. (briefly: min representable) if its epigraph $\operatorname{epi}(f) = \{(z, x) | z \geqslant f(x)\}$ is a b-MIP.r. set.

The following result characterizes b-MIP.r. sets.

Theorem 2.1. [28], [30]. A set $S \subseteq R^n$ is $b$ -MIP. $r$ iff $S$ is a finite union $S = P_1 \cup \ldots \cup P_t$ of polyhedra $P_i$ with $\text{rec}(P_i)$ independent of $i = 1, \ldots, t$ .

Corollary 2.1. [28], [30]. A b-MIP.r. set S is closed. In particular, the epigraph of a min-b-MIP.r. function is closed.

Given Theorem 2.1, a natural way of introducing a recession cone for a b-MIP.r set is to define $\operatorname{rec}(S) = \operatorname{rec}(P_i)$ (in the context of Theorem 2.1). One direct consequence of the next result is that $\operatorname{rec}(S)$ , so defined, is independent of the union representation $S = P_1 \cup \ldots \cup P_t$ of $S$ .

Theorem 2.2. [28]. If $S \neq \emptyset$ is $b$ -MIP. $r$ then

$$
\begin{array}{c} r e c (S) = \left\{y \mid f o r s o m e x \in S, x + \lambda y \in S \right. \\ \text {for all} \lambda \geqslant 0 \} \\ = \left\{y \mid f o r a l l x \in S, x + \lambda y \in S \right. \\ \text {for all} \lambda \geqslant 0 \}, \end{array}\tag{2.2}
$$

$$
\operatorname{rec} (S) = \{x \mid \text {   for   some   } y \text {   with   } y _ {k} = 0 \text {   for   } k \in K,
$$

$$
\left. A x + B y = 0 \right\}.\tag{2.3}
$$

In (2.3), A, B and K derive from any representation (2.1) of S.

We now fix a representation (2.1) of $S$ and denote it by $\underline{S}$ . We define $\operatorname{rec}^*(\underline{S})$ to be the r.h.s. of (2.3). Hence, $\operatorname{rec}(S) = \operatorname{rec}^*(\underline{S})$ if $S \neq \emptyset$ .

We also define the relaxation of the representation $\underline{S}$ by

$$
\begin{array}{r l} \operatorname{Rel} (\underline {{{S}}}) & = \left\{x \mid \text { for   some } y \text { with } 0 \leqslant y _ {k} \leqslant 1, \right. \\ & \quad k \in K, \text { we   have } A x + B y = b \}. \end{array}\tag{2.4}
$$

I.e., $\operatorname{Rel}(\underline{S})$ is obtained by relaxing $y_{k} \in \{0, 1\}$ in (2.1) to $y_{k} \in [0, 1]$ . $\operatorname{Rel}(\underline{S})$ very much depends on the precise representation $\underline{S}$ . However, its recession cone does not, by the following result.

Proposition 2.1. [29]. $\text{Rel}(\underline{S})$ is a polyhedron containing $\text{conv}(S)$ and

$$
r e c ^ {*} (R e l (\underline {{{S}}})) = r e c ^ {*} (\underline {{{S}}}).\tag{2.5}
$$

A representation $\underline{S}$ of $S$ is 'sharp' if

$$
\operatorname{Rel} (\underline {{{S}}}) = \operatorname{conv} (S).\tag{2.6}
$$

In [30], we showed that sharp representations exist for any b-MIP.r. set S. However, most representations of S are not sharp, so that typically we have $\operatorname{Rel}(\underline{S}) \supseteq \operatorname{conv}(S)$ .

The existence of sharp representations shows that $\operatorname{clconv}(S) = \operatorname{conv}(S)$ for b-MIP.r sets $S$ , as $\operatorname{Rel}(\underline{S})$ in (2.6) is closed.

In [29], we introduced ‘canonical constructions’ which ‘followed’ the set operations of union, intersection, cartesian product, projection, and set sum in the precise sense of (2.7) below. The ‘constructions’ are mappings on representations, which take them to other representations. For a set operation $\mathrm{Op}(V_1, \ldots, V_t)$ and fixed representations $\underline{S}_i$ of b-MIP.r. sets $S_i$ , $1 \leqslant i \leqslant t$ , and a construction $\underline{\mathrm{Op}}(W_1, \ldots, W_t)$ , we say that $\underline{\mathrm{Op}}(\bullet)$ represents $\overline{\mathrm{Op}}(\bullet)$ on $(\underline{S}_1, \ldots, \underline{S}_t)$ if

$\underline{\mathrm{Op}}(\underline{S}_1,\dots,\underline{S}_t)$ is a b-MIP.r representation

of $\operatorname{Op}(S_1, \ldots, S_t)$ .

(2.7)

Thus if $\operatorname{Ev}(\underline{S})$ denotes the set represented by $\underline{S}$ (i.e., $\operatorname{Ev}(\underline{S}) = S$ ), (2.7) is equivalent to

$$
\operatorname{Op} \left(S _ {1}, \dots , S _ {t}\right) = \operatorname{Ev} \left(\underline {{\operatorname{Op}}} \left(\underline {{S}} _ {1}, \dots , \underline {{S}} _ {t}\right)\right).\tag{2.7'}
$$

The specific canonical constructions, for the set operations cited above, are given in [29]. Each has a domain, i.e., a set of representations $(\underline{S}_1,\ldots ,\underline{S}_t)$ for which (2.7) holds. The domain of the union representation is $\{(\underline{S}_1,\dots ,\underline{S}_t)|\mathrm{rec}^* (\underline{S}_i) = \mathrm{rec}^* (\underline{S}_j)$ for $1\leqslant i,j\leqslant t\}$ . The domain of the intersection representation (in fact, of all constructions except union) is all $(\underline{S}_1,\dots ,\underline{S}_t)$ , in the b-MIP.r setting.

A construction $\overline{\mathrm{Op}}(\bullet)$ is called (relaxation) commutative if, for all $(\underline{S}_1,\ldots,\underline{S}_t)$ in its domain $\operatorname{Rel}(\underline{\mathrm{Op}}(\underline{S}_1,\ldots,\underline{S}_t))$

$$
= \operatorname{conv} \left(\operatorname{Op} \left(\operatorname{Rel} \left(\underline {{{S}}} _ {1}\right), \dots , \operatorname{Rel} \left(\underline {{{S}}} _ {t}\right)\right)\right).\tag{2.8}
$$

The construction RL(●) of one representation argument S, takes the representation S and replaces it by a representation for Rel(S). RL(●) does this by simply relaxing all ‘ $y_{k} \in \{0, 1\}$ ’ to ‘ $y_{k} \in [0, 1]$ ’. RL(●) is related to Rel(●) by

$$
\operatorname{Rel} (\underline {{{S}}}) = \operatorname{Ev} (\operatorname{RL} (\underline {{{S}}})).\tag{2.9}
$$

A construction $\underline{\mathrm{Op}(\bullet)}$ is called elementary if

$$
\begin{array}{r l} & \mathrm{RL} \big (\underline {{\mathrm{Op}}} \big (\underline {{S}} _ {1}, \dots , \underline {{S}} _ {t} \big) \big) \\ & = \mathrm{RL} \big (\underline {{\mathrm{Op}}} \big (\mathrm{RL} \big (\underline {{S}} _ {1}), \dots , \mathrm{RL} \big (\underline {{S}} _ {t} \big) \big) \big). \end{array}\tag{2.9}
$$

for all $(\underline{S}_1, \ldots, \underline{S}_t)$ in its domain. In [29] we also established the following results:

Theorem 2.3. [29]. The canonical constructions for union, intersection, projection, cartesian product, and set sum, represent the set operation for which they are named, and are all both commutative and elementary.

Proposition 2.2. [29]. If $\underline{Op(\bullet)}$ is an elementary representation of set operation $Op(\bullet)$ , then on the domain of $Op(\bullet)$

$$
\operatorname{Rel} \left(\underline {{\mathrm{Op}}} \left(\underline {{S}} _ {1}, \dots , \underline {{S}} _ {t}\right)\right)
$$

$$
\supseteq \operatorname{conv} \left(\operatorname{Op} \left(\operatorname{Rel} \left(\underline {{{S}}} _ {1}\right), \dots , \operatorname{Rel} \left(\underline {{{S}}} _ {t}\right)\right)\right).\tag{2.10}
$$

From Proposition 2.2, for elementary constructions, commutativity (2.8) states that the general inclusion (2.10) becomes an equality.

For the union construction of $t$ arguments $\underline{S}_1, \ldots, \underline{S}_t$ which is denoted $\underline{S}_1 \vee \ldots \vee \underline{S}_t$ , commutativity (2.8) becomes

$$
\begin{array}{l} \operatorname{Rel} (\underline {{{S}}} _ {1} \vee \dots \vee \underline {{{S}}} _ {t}) \\ = \operatorname{conv} (\operatorname{Rel} (\underline {{{S}}} _ {1}) \cup \dots \cup \operatorname{Rel} (\underline {{{S}}} _ {t})). \end{array}\tag{2.11}
$$

For the intersection construction of $t$ arguments, denoted $\underline{S}_1 \wedge \ldots \wedge \underline{S}_t$ , the fact that each $\operatorname{Rel}(\underline{S}_i)$ is convex, and commutativity (2.8), give

$$
\operatorname{Rel} \left(\underline {{{S}}} _ {1} \wedge \dots \wedge \underline {{{S}}} _ {t}\right) = \operatorname{Rel} \left(\underline {{{S}}} _ {1}\right) \cap \dots \cap \operatorname{Rel} \left(\underline {{{S}}} _ {t}\right).\tag{2.12}
$$

We also showed in [29] that $\operatorname{rec}^{*}(\underline{S}_{1} \vee \ldots \vee \underline{S}_{t}) = \operatorname{rec}^{*}(\underline{S}_{i})$ for any $i, 1 \leqslant i \leqslant t$ , when $(\underline{S}_{1}, \ldots, \underline{S}_{t})$ is in the domain of the union construction (i.e., when $\operatorname{rec}^{*}(\underline{S}_{i})$ is independent of $i$ ). Thus if any $S_{i} \neq \emptyset$ , $1 \leqslant i \leqslant t$ , $S = S_{1} \cup \ldots \cup S_{t} \neq \emptyset$ , and so $\operatorname{rec}(S) = \operatorname{rec}(S_{i})$ . Also in [29] we verified that $\operatorname{rec}^{*}(\underline{S}_{1} \wedge \ldots \wedge \underline{S}_{t}) = \operatorname{rec}^{*}(\underline{S}_{1}) \cap \ldots \cap \operatorname{rec}^{*}(\underline{S}_{t})$ , so that if all $S_{i} \neq \emptyset$ with $1 \leqslant i \leqslant t$ , $\operatorname{rec}(S) = \operatorname{rec}(S_{1}) \cap \ldots \cap \operatorname{rec}(S_{t})$ where $S = S_{1} \cap \ldots \cap S_{t}$ .

In [29], we introduced the composite constructions, which arise by (repeated) composition of the canonical constructions. The domain restrictions of the composite constructions are obtained by combining all domain restrictions of the canonical constructions composed in them, in the natural, nested manner. The following results were then obtained.

Theorem 2.4. [29]. If a composite construction $\underline{Op(\bullet)}$ does not have, both, occurrences of the union construction and occurrences of the intersection construction, then it is commutative.

Theorem 2.5. [29]. If a composite construction $\underline{Op}(\bullet)$ of $t$ arguments $\underline{S}_1, \ldots, \underline{S}_t$ has no occurrences of the intersection construction, and if each $\underline{S}_i$ is a sharp representation of $S_i$ , $1 \leqslant i \leqslant t$ , then $\underline{Op}(\underline{S}_1, \ldots, \underline{S}_t)$ is a sharp representation of $\underline{Op}(S_1, \ldots, S_t)$ , provided only that $(\underline{S}_1, \ldots, \underline{S}_t)$ is in the domain of $\underline{Op}(\bullet)$ .

The sharpness of $\underline{\mathrm{Op}}(\underline{S}_1, \ldots, \underline{S}_t)$ cited in Theorem 2.5 can be stated this way

$$
\operatorname{Rel} \left(\underline {{\mathrm{Op}}} \left(\underline {{S}} _ {1}, \dots , \underline {{S}} _ {t}\right)\right) = \operatorname{conv} \left(\mathrm{Op} \left(S _ {1}, \dots , S _ {t}\right)\right).\tag{2.13}
$$

## 3. Spatial Imbeddings of Models

By a model we shall mean a structure $M = (X, D, \Omega; P_1, \ldots, P_s)$ where $X \subseteq R^n$ is a subset of some Euclidean space $R^n$ , $D$ is a set, $\emptyset \neq \Omega \subseteq X \times D$ is a non-empty subset of the Cartesian product of $X$ and $D$ ; and each $P_i \subseteq \Omega$ for $i = 1, \ldots, s$ . The $P_i$ are called predicates or relations on $\Omega$ . $X$ is called the spatial part of the model $M$ ; $D$ is the non-spatial part.

To a certain extent, the choice of the spatial part X is at the discretion of the researcher. Those parts of a model structure which are already numeric, with linear structure, can be placed into X if one wishes to imbed them ‘as is’ (in the sense of (3.2)). If one is willing to examine reformulations of the part, it can be placed in D.

In order to define an imbedding, we first need some presliminary discussion.

Each predicate $P_{j}$ has a negation $-1P_{j}$ which is simply its set-theoretic relative complement

$$
\neg P _ {j} \stackrel {\text { def }} {=} \Omega \setminus P _ {j}.
$$

An imbedding will involve sets $\operatorname{Imb}(\Omega) \neq \emptyset$ , $\operatorname{Imb}(P_j)$ , $\operatorname{Imb}(\neg P_j) \subseteq R^t$ , $t \geqslant n$ , $j = 1, \ldots, s$ in some Euclidean space $R^t$ . Of course $\operatorname{Imb}(\neg P_j)$ will be the relative complement of $\operatorname{Imb}(P_j)$ in $\operatorname{Imb}(\Omega)$ : $\operatorname{Imb}(\neg P_j) = \operatorname{Imb}(\Omega) \setminus \operatorname{Imb}(P_j)$ . These sets are to be b-MIP representable. We also require that $\operatorname{rec}(\operatorname{Imb}(\Omega)) = \operatorname{rec}(\operatorname{Imb}(P_j))$ if $P_j \neq \emptyset$ and $\operatorname{rec}(\operatorname{Imb}(\Omega)) = \operatorname{rec}(\operatorname{Imb}(\neg P_j))$ if $\neg P_j \neq \emptyset$ . In addition, other conditions to be met are now explained in detail.

Let $P_{j}^{1}$ abbreviate $P_{j}$ and $P_{j}^{-1}$ abbreviate $\neg P_{j}$ . (It is typographically simpler to let superscripts vary in $(1, -1)$ than to use the negation prefix).

Let $L$ be a propositional form built from the formal letters $P_j$ and $\neg P_j$ by use of the propositional connectives $\vee, \wedge, \neg$ , and $\Rightarrow$ . We define $\operatorname{Imb}(L)$ by induction on the formation of $L$ , where of course $\operatorname{Imb}(L) = \operatorname{Imb}(P_j^k)$ if $L$ is $P_j^k$ for $k \in \{-1, 1\}$ . We set

$$
\operatorname{Imb} \left(L _ {1} \vee L _ {2}\right) = \operatorname{Imb} \left(L _ {1}\right) \cup \operatorname{Imb} \left(L _ {2}\right),\tag{3.1a}
$$

$$
\operatorname{Imb} \left(L _ {1} \wedge L _ {2}\right) = \operatorname{Imb} \left(L _ {1}\right) \cap \operatorname{Imb} \left(L _ {2}\right),\tag{3.1b}
$$

$$
\operatorname{Imb} \left(\neg \left(L _ {1} \vee L _ {2}\right)\right) = \operatorname{Imb} \left(\left(\neg L _ {1}\right) \wedge \left(\neg L _ {2}\right)\right),\tag{3.1c}
$$

$$
\operatorname{Imb} \left(\neg \left(L _ {1} \wedge L _ {2}\right)\right) = \operatorname{Imb} \left(\left(\neg L _ {1}\right) \vee \left(\neg L _ {2}\right)\right),\tag{3.1d}
$$

$$
\operatorname{Imb} (\neg \neg L) = \operatorname{Imb} (L),\tag{3.1e}
$$

$$
\operatorname{Imb} \left(L _ {1} \Rightarrow L _ {2}\right) = \operatorname{Imb} \left(\left(\neg L _ {1}\right) \vee L _ {2}\right),\tag{3.1f}
$$

$$
\operatorname{Imb} \left(\neg \left(L _ {1} \Rightarrow L _ {2}\right)\right) = \operatorname{Imb} \left(L _ {1} \wedge \neg L _ {2}\right).\tag{3.1g}
$$

Of course, (3.1a) and (3.1b) are the natural definitions. (3.1c), (3.1d), (3.1e) and (3.1g) simply reflect the fact that we treat negations by moving them inward, until they are against predicate letters, using the de Morgan Laws. (3.1f) reflects the fact that we treat $L_{1} \Rightarrow L_{2}$ as its logical equivalent $(\neg L_{1}) \vee L_{2}$ . From herein, we shall treat forms L as if the only connectives occurring are $\vee$ and $\wedge$ .

Here is the last condition required in the definition of an imbedding:

for all $c \in R^n$ and all logical forms $L$ ,

$$
\begin{array}{r l} & {\inf \bigl \{c x | (x, d) \in L \bigr \}} \\ & {\qquad = \min \bigl \{c x | (x, y) \in \operatorname{Imb} (L) \bigr \}.} \end{array}\tag{3.2}
$$

In particular, the left-hand-side (l.h.s.) of (3.2) is consistent iff its r.h.s. is.

We next begin the technical development which shows that imbeddings exist, under broad hypotheses (Theorems 3.1). We note that an imbedding is not a model isomorphism [48], i.e., it is not a point-to-point correspondence at all. We desire only that linear optimizations (and consistency) are the same in M and its imbedding. However, in finite domains points can be imbeded by viewing them as predicates.

Clearly, an imbedding of an imbedding of $M$ is an imbedding of $M$ . Moreover, given an imbedding of $M = (X, D, \Omega; P_1, \ldots, P_s)$ and a propositional logic form $L$ with $L \cap \Omega \neq \emptyset$ , one automatically obtains an imbedding of the restriction $M' = (X, D, \Omega \cap L; P_1 \cap L, \ldots, P_s \cap L)$ by setting $\operatorname{Imb}'(L') = \operatorname{Imb}(L \cap L')$ for any logical form $L'$ .

By induction on the formation of L (3.1), one easily shows using (3.2) that $\operatorname{Imb}(L) \neq \emptyset$ iff $L \neq \emptyset$ ; that $\operatorname{Imb}(L)$ is b-MIP.r. (using Theorem 2.3); and that $\operatorname{rec}(\operatorname{Imb}(\Omega)) = \operatorname{rec}(\operatorname{Imb}(L))$ if $L \neq \emptyset$ (by the remark after (2.12)).

Let $\Gamma$ denote the space of all mappings $\gamma$ : $\{1, 2, \ldots, s\} \to \{+1, -1\}$ . Here $\bigcap_{j=1}^{s} P_j^{\gamma(j)}$ has the obvious meaning, and is called an elementary conjunct.

For the propositional form $L$ in the predicate letters $P_1, \ldots, P_s$ and $\gamma \in \Gamma$ we say that the elementary conjunct $L' = \bigcap_{j=1}^{s} P_j^{\gamma(j)}$ supports $L$ if $L'$ occurs in the complete $\{P_{1},\ldots,P_{s}\}$ -disjunctive normal form of $L$ .

We make the following observations regarding the concept of support:

$L^{\prime}$ supports $L = L_{1} \vee L_{2} \leftrightarrow L^{\prime}$ supports $L_{1}$

or $L^{\prime}$ supports $L_{2}$ ,

(3.3a)

$L^{\prime}$ supports $L = L_{1} \wedge L_{2} \leftrightarrow L^{\prime}$ supports $L_{1}$

and $L'$ supports $L_{2}$ ,

(3.3b)

$$
L = \cup \left\{L ^ {\prime} \mid L ^ {\prime} \text { supports } L \right\}.\tag{3.3c}
$$

Here (3.3b) follows from the disjointness of distinct elementary conjunctions on $\{P_{1},\ldots,P_{s}\}$ and the logical distributive laws. Of course (3.3c) re-states disjunctive normal form.

Lemma 3.1. In an imbedding,

$$
I m b (L) = \left\{I m b \left(L ^ {\prime}\right) \mid L ^ {\prime} \text { supports } L \right\}.\tag{3.4}
$$

Proof. By induction on the formation (3.1a), (3.1b) of $\operatorname{Imb}(\mathbf{L})$ . In the 'ground case' of the induction, $L = P_j^m$ for some $j = 1, \ldots, s$ and $m \in \{-1, 1\}$ . Since $\operatorname{Imb}(P_j^m) \subseteq \operatorname{Imb}(\Omega) = \operatorname{Imb}(P_k) \cup \operatorname{Imb}(\neg P_k)$ for all $k = 1, \ldots, s$ , we have $\operatorname{Imb}(L) = \operatorname{Imb}(P_j^{\pm 1}) \cap_{k \neq j} (\operatorname{Imb}(P_k) \cup \operatorname{Imb}(\neg P_k)) = \bigcup_{\gamma} \{\bigcap_{j=1}^{s} \operatorname{Imb}(P_k^{\gamma(k)}) \mid \gamma(j) = \pm 1\} = \bigcup \{\operatorname{Imb}(L') | L'\text{ supports } L\}$ .

We leave the inductive step as an exercise, which uses (3.1a), (3.1b), (3.3a) and (3.3b), and the disjointness of the $\operatorname{Imb}(L')$ . $Q.E.D$ .

Lemma 3.2. If $L$ and $L'$ are logically equivalent, then

$$
I m b (L) = I m b \left(L ^ {\prime}\right).\tag{3.5}
$$

Proof. They have the same complete $\{P_1, \ldots, P_s\}$ disjunctive normal form. The result then follows by Lemma 3.1. Q.E.D.

Let $L' \mid L$ abbreviate the fact that $L'$ supports $L$ .

Theorem 3.1. Let $M = (X, D, \Omega; P_1, \ldots, P_s)$ be a model. If $n = 0$ , $M$ is imbeddable. Suppose that $n \geqslant 1$ . Then $M$ is imbeddable iff for every non-empty elementary conjunct $L' = \bigwedge_{j=1}^{s} P_j^{\gamma(j)} \neq \emptyset$ , $\gamma \in \Gamma$ , clconv $(T(L'))$ is a polyhedron, where

$$
T (L ^ {\prime}) = \{x \mid \text { for   some } d, (x, d) \in L ^ {\prime} \},\tag{3.6}
$$

and moreover $\text{rec}(\text{clconv}(T(L'))))$ is independent of $L'$ .

Next, let $q \geqslant 1$ and let $\{u(L') | L' \neq \emptyset\}$ be distinct points of $R^q$ . For $\gamma \in \Gamma$ , let $\text{Imb}(L') = \{u(L')\}$ for $L' \neq \emptyset$ if $n = 0$ ; or let $\text{Imb}(L') = \text{clconv}(T(L')) \times \{u(L')\}$ for $L' \neq \emptyset$ if $n \geqslant 1$ , when $M$ is imbeddable. For general propositional forms $L$ , define $\text{Imb}(L)$ by (3.4). The result is then an imbedding of $M$ .

Proof. First, let $n \geqslant 1$ and suppose that $M$ is imbeddable. Then the set $S(L') = \{x \mid \text{for some } y, (x, y) \in \operatorname{Imb}(L')\}$ is a projection of a non-empty b-MIP.r. set for all elementary conjuncts $L' \neq \emptyset$ ; by Theorem 2.3, it is b-MIP.r. By Proposition 2.1, and the existence of sharp representations (2.6), $\operatorname{rec}(S(L')) = \operatorname{rec}(\operatorname{conv}(S(L'))$ is independent of $L' \neq \emptyset$ . By Proposition 2.1, $\operatorname{conv}(S(L'))$ is a polyhedron.

Clearly, from (3.2) for elementary conjuncts $L = L', \text{conv}(S(L')) = \text{clconv}(S(L')) = \text{clconv}(T(L'))$ . Consequently, $\text{rec}(\text{clconv}(T(L'))) = \text{rec}(S(L'))$ is independent of $L' \neq \emptyset$ . From the facts follows the necessity of the conditions cited.

Next suppose, if $n \geqslant 1$ , that the conditions cited do hold.

Let $L$ be a propositional form and let $c \in R^n$ . We have

$$
\begin{array}{r l} & \min \left\{c x \mid (x, y) \in \operatorname{Imb} (L) \right\} \\ & = \min _ {L ^ {\prime} \mid L} \min \left\{c x \mid (x, u (L)) \in \operatorname{Imb} (L ^ {\prime}) \right\} \\ & = \min _ {L ^ {\prime} \mid L} \inf \left\{c x \mid \text { for   some } d, (x, d) \in L ^ {\prime} \right\} \\ & = \inf \left\{c x \mid \text { for   some } d, (x, d) \in L \right\}. \end{array} \tag {3}\tag{3.7}
$$

The first equality in (3.7) follows from (3.4). The second equality follows from the setting $\operatorname{Imb}(L') = \operatorname{clconv}(T(L') \times \{u(L')\}$ and (3.6). The third equality follows from (3.3c). Of course, (3.7) verifies condition (3.2) of an imbedding.

The remaining conditions are easily verified using (3.4) and Theorem 2.3, if we recall that for $L' \neq \emptyset$ , $\operatorname{rec}(\operatorname{clconv}(T(l'))))$ is independent of $L$ . Moreover, as $\Omega = P_j \cup \neg P_j$ and $P_j \cap \neg P_j = \emptyset$ , the terms in the complete d.n.f. of $P_j$ and $\neg P_j$ are mutually exhaustive and disjoint. Hence, $\operatorname{Imb}(\Omega) = \operatorname{Imb}(P_j) \cup \operatorname{Imb}(\neg P_j)$ and $\operatorname{Imb}(P_j) \cap \operatorname{Imb}(\neg P_j) = \emptyset$ , as needed. The proof for $n = 0$ is similar to that for $n \geqslant 1$ . Q.E.D.

Motivated by Theorem 3.1, we call imbeddings with $\operatorname{Imb}(L') = \operatorname{clconv}(T(L')) \times \{u(L')\}$ for $n \geqslant 1$ , or $\operatorname{Imb}(L') = \{u(L')\}$ for $n = 0$ , disjunctive imbeddings. Of all disjunctive imbeddings, one has certain properties worth special notice.

Let $q^{*} = |\{L' | L' \text{ is an elementary conjunct, } L' \neq \emptyset\}|$ . To each coordinate position in $R^{q^*}$ we can view that a particular simple conjunct $L' \neq \emptyset$ has been associated. The unit vector $e(L') \in R^{q^*}$ has a '1' in the co-ordinate for $L' \neq \emptyset$ and zeroes elsewhere. The disjunctive imbeddings with $u(L') = e(L')$ is called the sharp imbedding. It can be viewed as an imbedding into $R^n \times R^{q^{*}-1}$ , as the unit vectors $e(L')$ span an affine space of dimension $(q^* - 1)$ in $R^{q^*}$ .

Here is the special property of the sharp imbedding.

Lemma 3.3. For the sharp imbedding, given any two propositional forms $L_{1}$ and $L_{2}$

$$
\begin{array}{r l} \operatorname{conv} \bigl (I m b \bigl (L _ {1} \wedge L _ {2} \bigr) \bigr) & = \operatorname{conv} \bigl (I m b \bigl (L _ {1} \bigr) \bigr) \\ & \cap \operatorname{conv} \bigl (I m b \bigl (L _ {2} \bigr) \bigr). \end{array}\tag{3.8}
$$

Proof. For $i = 1, 2$ we have, using (3.4) for $n \geqslant 1$ conv(Imb( $L_i$ ))

$$
\begin{array}{r l} & = \operatorname{conv} \left\{\cup \left\{\operatorname{clconv} (T (L ^ {\prime})) \right. \right. \\ & \qquad \times \left\{e (L ^ {\prime}) \right\} | L ^ {\prime} | L _ {i} \text { and } L ^ {\prime} \neq \emptyset \} \Bigg \} \\ & = \left\{(x, y) | \sum_ {L ^ {\prime}} y (L ^ {\prime}) = 1, \text { all } y (L ^ {\prime}) \geqslant 0, \quad (3 \right. \\ & \qquad y (L ^ {\prime}) = 0 \quad \text { if } L ^ {\prime} | L _ {i}, \\ & \qquad x = \sum y (L ^ {\prime}) x (L ^ {\prime}) \text { where   each } x (L ^ {\prime}) \\ & \qquad \in \operatorname{clconv} (T (L ^ {\prime})) \Bigg \}. \end{array}\tag{3.9}
$$

In (3.9), $y(L')$ is the co-ordinate of $y \in R^{q^*}$ in correspondence with $L' \neq \emptyset$ ; $x(L')$ is simply an element of $\operatorname{clconv}(T(L'))$ .

From (3.9), if $(x, y) \in \operatorname{conv}(\operatorname{Imb}(L_1)) \cap \operatorname{conv}(\operatorname{Imb}(L_2))$ , we have $y(L') = 0$ if either $L' \mid L_1$ or $L' \mid L_2$ fails. By (3.3b), $y(L') = 0$ if $L \mid L_1 \wedge L_2$ fails.

From the last paragraph, and the formula for $\operatorname{conv}(\operatorname{Imb}(L_1 \wedge L_2)$ which is analogous to (3.9), $(x, y) \in \operatorname{conv}(\operatorname{Imb}(L_1)) \cap \operatorname{conv}(\operatorname{Imb}(L_2))$ implies $(x, y) \in \operatorname{conv}(\operatorname{Imb}(L_1 \wedge L_2))$ . Thus we have proven the inclusion $\supseteq$ in (3.8).

The inclusion $\subseteq$ in (3.8) is trivial, and holds for all imbeddings. In detail

$$
\begin{array}{r l} & \operatorname{conv} (\operatorname{Imb} (L _ {1} \wedge L _ {2})) \\ & = \operatorname{conv} (\operatorname{Imb} (L _ {1}) \wedge \operatorname{Imb} (L _ {2})) \\ & \subseteq \operatorname{conv} (\operatorname{Imb} (L _ {i})), \end{array}\tag{3.10}
$$

for $i = 1,2.$ Q.E.D.

From (3.2) we have

$$
\begin{array}{r l} & {\inf \bigl \{c x | (x, d) \in L \bigr \}} \\ & {\qquad = \min \bigl \{c x | (x, y) \in \operatorname{conv} (\operatorname{Imb} (L)) \bigr \},} \end{array}\tag{3.11}
$$

for any $c \in R^n$ and any form $L$ . However, a description of $\text{conv}(\text{Imb}(L))$ via linear inequalities can be hard to obtain from a description of $\text{Imb}(L)$ , as attested to by many efforts in discrete programming.

In [28], [29] we developed techniques for obtaining canonical representations, which we shall shortly connect to this issue in (3.11) and to the sharp imbedding of Lemma 3.3. First, we need some discussion to set up the framework of Theorem 3.2.

Let us fix representations $\operatorname{Imb}\left(P_j^{\pm 1}\right)$ for $\operatorname{Imb}(P_j^{\pm 1})$ , where $P^{\pm 1}$ abbreviates the two cases $P^k$ for $k \in \{-1, 1\}$ . If $P_j^{\pm 1} \neq \emptyset$ , $\operatorname{rec}^* - (\operatorname{Imb}\left(P_j^{\pm 1}\right) = \operatorname{rec}(\operatorname{Imb}(P_j^{\pm 1}))$ is independent of $P_j^{\pm 1}$ . Via appropriate use of auxiliary variables if $P_j^{\pm 1} = \emptyset$ , we can insure that all $\operatorname{rec}^*(\operatorname{Imb}(P_j^{\pm 1}))$ are independent of $P_j^{\pm 1}$ . (Hint: Add an additional auxiliary variable $y$ with constraint $0 \leqslant y \leqslant -1$ , and use (2.3)).

For a propositional form L, we let a representation $\underline{L}$ of $\operatorname{Imb}(L)$ be obtained through use of the composite constructions of [29], with the logical ‘V’ treated through the union construction, and the logical ‘ $\Lambda$ ’ through the intersection construction. In this notation, $P_{j}^{\pm1}$ and $\operatorname{Imb}\left(P_{j}^{\pm1}\right)$ are the same.

Lemma 3.4. For the sharp imbedding, with the $\underline{P}_j^{\pm 1}$ sharp representations of the $\operatorname{Imb}(P_j^{\pm 1})$ , we have

$$
\operatorname{Re1} (\underline {{L}}) = \operatorname{conv} (I m b (L)).\tag{3.12}
$$

Proof. By induction on the formation of $L$ , with the ground case of $L = P_j^{\pm 1}$ from the sharpness of the $\underline{P}_j^{\pm 1}$ . If $L = L_1 \vee L_2$ , $\operatorname{Rel}(\underline{L}) = \operatorname{conv}(\operatorname{Rel}(\underline{L}_1) \cup \operatorname{Rel}(\underline{L}_2))$ (Theorem 2.3) = conv(conv(Imb( $L_1$ )) ∪ conv(Imb( $L_2$ ))) (induction hypothesis) = conv(Imb( $L_1$ ) ∨ Imb( $L_2$ )) = conv(Imb( $L$ )) (by (3.1a). If $L = L_1 \wedge L_2$ , $\operatorname{Rel}(\underline{L}) = \operatorname{conv}(\operatorname{Rel}(\underline{L}_1)) \wedge \operatorname{conv}(\operatorname{Rel}(\underline{L}_2))$ (by Theorem 2.3) = conv(conv(Imb( $L_1$ )) ∩ conv(Imb( $L_2$ ))) (induction hypothesis) = conv(conv(Imb( $L_1 \wedge L_2$ )) (Lemma 3.3) = conv(Imb( $L_1 \wedge L_2$ )) = conv(Imb( $L$ )).

Theorem 3.2. For the sharp imbedding, with the $\underline{P}_j^{\pm 1}$ sharp representations of the $\text{Imb}(P_j^{\pm 1})$ , we have

for all $c \in R^n$ and all propositional forms $L$ ,

$$
\inf \{c x | (x, d) \in L \}
$$

$$
= \min \left\{c x \mid (x, y) \in R e 1 (\underline {{{L}}}) \right\}.\tag{3.13}
$$

Proof. Lemma 3.4 and (3.11). Q.E.D.

Our next result states that, in terms of dimension alone, the sharp imbedding is close to 'minimal dimension' (and is minimal dimension for $n = 0$ ), if one wishes (3.13) to hold.

Theorem 3.3. In an imbedding with $q < q^{*} - n - 1$ , $q$ being the dimension of $y$ , there are disjunctive normal forms $L_{1}$ and $L_{2}$ with $L_{1} \wedge L_{2} = \emptyset$ and $\operatorname{Re1}(\underline{L}_1 \wedge \underline{L}_2) \neq \emptyset$ .

Proof. For each $\gamma \in \Gamma$ with $L'(\gamma) = \Lambda_{j=1}^{s} P_j^{\gamma(j)} \neq \emptyset$ , chose $(x(\gamma), y(\gamma)) \in \operatorname{Imb}(L'(\gamma))$ . As $q < q^* - n-1$ , and the $q^*$ vectors $(x(\gamma), y(\gamma), 1)$ lie in $R^{n+q+1}$ , there is a non-trivial linear dependence in scalars $\Theta_\gamma$ :

$$
\sum_ {\gamma} \left\{\theta_ {\gamma} (x (\gamma), y (\gamma), 1) \mid L ^ {\prime} (\gamma) \neq \emptyset \right\} = 0.\tag{3.14}
$$

Put $\lambda_{\gamma}^{(1)} = \theta_{\gamma}$ if $\theta_{\gamma} > 0$ and $\lambda_{\gamma}^{(2)} = -\theta_{\gamma}$ if $\theta_{\gamma} < 0$ . Clearly, there are some $\theta_{\gamma} > 0$ and some $\theta_{\gamma} < 0$ .

Let $L_{1} = \vee \{L'(\gamma) | \theta_{\gamma} > 0\}$ , $L_{2} = \vee \{L'(\gamma) | \theta_{\gamma} < 0\}$ . By disjointness of distinct elementary conjuncts, $L_{1} \wedge L_{2} = \emptyset$ .

Without loss of generality, $\Sigma_{\gamma}\{\lambda_{\gamma}^{(1)}|L(\gamma)$ supports $L_{1}\}=1=\Sigma\{\lambda_{\gamma}^{(2)}|\mathrm{L}(\gamma)$ supports $L_{2}\}$ . Then from (3.14), if we put $(x,y)=\Sigma_{\gamma}\{\lambda_{\gamma}^{(1)}(x(\gamma),y(\gamma))|L(\gamma)$ supports $L_{1}$ we also have $(x,y)=\Sigma_{\gamma}\{\lambda_{\gamma}^{(2)}(x(\gamma),y(\gamma))|L(\gamma)$ supports $L_{2}\}$ . Thus $(x,y)\in\mathrm{conv}(\mathrm{Imb}(L_{1}))\cap\mathrm{conv}(\mathrm{Imb}(L_{2}))\subseteq\mathrm{Rel}(\underline{L}_{1})\cap\mathrm{Rel}(\underline{L}_{2})$ (by Proposition 2.2)= $\mathrm{Rel}(\underline{L}_{1}\wedge\underline{L}_{2})$ (by Theorem 2.3). This shows that $\mathrm{Rel}(\underline{L}_{2}\wedge\underline{L}_{2})\neq\emptyset.$ Q.E.D.

Since $q^*$ is 'typically' (but not invariably) quite large, with possibly $q^* = 2^s$ (clearly $q^* \leqslant 2^s$ ), Theorem 3.3 states that the 'key property' (3.13) of the sharp imbedding necessitates large $q$ .

Trivially, if one is concerned about only the optimizations $\min\{cx|(x,y)\in\operatorname{Imb}(L)\}$ of (3.2), the part 'y' of the imbedding can be 'stripped out' as 'irrelevant', since one may work with the projection on x of $\operatorname{Imb}(L)$ . In the theoretical development, the 'y' co-ordinates serve to achieve effects such as $\operatorname{Imb}(P_j) \cap \operatorname{Imb}(\neg P_j) = \emptyset$ . More important from a practical perspective are these two rules for the 'y' co-ordinates: (1) They can achieve effects such as versions of (3.13), and in practice, one works with $\operatorname{Rel}(L)$ (and other problem relaxations) rather than directly with $\operatorname{Imb}(L)$ ; (2) They serve to 'append' information regarding the minimizing $x$ in (3.2).

## 4. Three Illustrations

We next give three examples of imbeddings. Others are given in [32]. In our first example, we show how to construe traditional MIP models as imbeddings which have ‘entirely spatial’ structures.

Example 4.1. Consider a binary mixed-integer constraint set

$$
\Omega = \left\{x \mid A x \geqslant b, x _ {j} \in \{0, 1 \} \text { for } j \in K \right\},\tag{4.1}
$$

where $x = (x_1, \ldots, x_n)$ and $K \subseteq \{1, \ldots, n\}$ . We treat it as the universe $\Omega$ of a model $M = (X, \emptyset, \Omega; P_1, \ldots, P_s)$ . Logical forms $L$ in these predicates arise only when one seeks to do optimization (or feasibility testing) over subsets of $\Omega$ defined by these forms. If $\Omega$ of (4.1) is the 'entire problem', so that no predicates are present, we take $s = 0$ and no further work is needed.

However, one can obtain meaningful predicates (i.e., subsets of $\Omega$ ) from (4.1) in many ways. For example, for any non-empty subset $J$ of $K$ , $\emptyset \neq J \subseteq K$ (possibly $K = J$ ), we may put

$$
P _ {j} = \Omega \cap \left\{x \mid x _ {j} = 1 \right\},\tag{4.2a}
$$

for $j\in J$ , so that

$$
\neg P _ {j} = \Omega \cap \left\{x \mid x _ {j} = 0 \right\}.\tag{4.2b}
$$

and $s = |J|$ . This leads to elementary conjuncts of the form

$$
\begin{array}{l} \bigcap_ {j = 1} ^ {s} P _ {j} ^ {\gamma (j)} \\ \qquad = \Omega \cap \left\{x \mid x _ {j} = \max \{0, \gamma (j) \} \text {for} j \in J \right\}. \end{array}\tag{4.3}
$$

Here it is instructive to note that the negation $\neg P_{j}$ of $P_{j}$ is given by (4.2b) and is not the 'spatial complement' of $\Omega \cap \{x | x_{j} = 1\}$ nor is $\neg P_{j}$ even $\Omega \cap \{x \mid x_j \neq 1\}$ . The latter kind of 'negation' is of course often intractable, and is not required in order to useour approach.

Even though this model M is already imbedded in space, let us see what happens if we use the general imbedding procedure of Theorem 3.1. Of course we obtain

$$
T \left(L ^ {\prime}\right) = \bigcap_ {j = 1} ^ {s} P _ {j} ^ {\gamma (j)} \quad \text { where } L ^ {\prime} = \bigwedge_ {j = 1} ^ {s} P _ {j} ^ {\gamma (j)},\tag{4.4}
$$

and so $T(L')$ is b-MIP.r. By sharpness (2.6) and Proposition 2.1, $\text{conv}(T(L'))$ is a polyhedron. It is easy to see that, for $L' \neq \emptyset$ , $\text{rec}(T(L')) = \{x \mid Ax \geqslant 0, x_j = 0 \text{ for } j \in K\}$ . Hence $\text{rec}(T(L'))$ is independent of $L' \neq \emptyset$ . We can now use Theorem 3.1 to obtain an imbedding, and we get

$$
\begin{array}{r l} \operatorname{Imb} (L ^ {\prime}) = & \operatorname{conv} \bigl \{x \mid A x \geqslant b, x _ {k} \in \{0, 1 \} \\ & \text { for } k \in K \setminus J, \\ & x _ {k} = \max \bigl \{0, \gamma (k) \bigr \} \\ & \text { for } k \in J \bigr \} \times \bigl \{u (L ^ {\prime}) \bigr \}, \end{array}\tag{4.5}
$$

when $L' = \Lambda_{j=1}^{s} P_j^{\gamma(j)} \neq \emptyset$ . We may then use Theorem 3.1, together with (3.4), to define $\operatorname{Imb}(L)$ for all propositional forms $L$ . We leave that work as an exercise.

In this instance, the y co-ordinate of the imbedding (occupied by $u(L')$ ) is not needed and can be stripped out, in terms only of an imbedding. However, it may still be useful for problem relaxations.

We shall next use this example to illustrate a different point, specifically, how one may utilize 'production rules' of the type occurring in many 'expert systems'. Those rules discussed here will be purely propositional, i.e., lacking logical quantifiers and 'certainty factors' such as treated in [15], [49].

Given a 'production rule'

$$
L _ {1} \text {   and...and   } L _ {t} \text {   implies   } L _ {0}.\tag{4.6}
$$

We view it simply as a domain restriction rather than a universal quantification on $x \in R^{n}$ . More specifically, we associate the propositional form $L = \neg L_{1} \vee \ldots \neg L_{t} \vee L_{0}$ with the rule (4.6), and use $\operatorname{Imb}(L)$ as constraints. Where several rules (4.6) are involved, the various L's are conjoined and the imbedding of the result is used as constraints.

Our practice is in conformity with the usual treatment of propositional logic by MIP. In that setting, a rule (4.6) gives rise to a constraint or set of constraints, i.e., to a restriction on the possible truth valuations. These valuations are, in specific, restricted to those truth valuations satisfying (4.6).

Example 4.2. Propositional logic on $s$ letters $P_{1},\ldots,P_{s}$ corresponds to a model structure $M=(\emptyset,D,\Omega;P_{1},\ldots,P_{s})$ which is entirely non-spatial $(\Omega=D)$ , in which $\Omega=\{(v_{1},\ldots,v_{s})|v_{i}=T$ or $F,1\leqslant i\leqslant s\}$ is the space of truth valuations; and the predicates $P_{j}=\{v\in\Omega|v_{j}=T\}$ , $\neg P_{j}=\{v\in\Omega|v_{j}=F\}$ , where $v=(v_{1},\ldots,v_{s})$ . Here we deliberately use the same name $P_{j}$ for the letter and for the corresponding predicate on $\Omega$ .

In this model, the elementary conjunctions $\Lambda_{j=1}^{s} P_{j}^{\gamma(j)} = \{v \mid v_{j} = T \text{ if } \gamma(j) = 1 \text{ and } v_{j} = F \text{ if } \gamma(j) = -1, 1 \leqslant j \leqslant s\}$ are the $2^{s}$ individual truth valuations.

The standard imbedding used extensively in the MIP literature, is to put $\operatorname{Imb}(\Omega) = \{(x_1, \ldots, x_s) | x_j = 0 \text{ or } 1, 1 \leqslant j \leqslant s\}$ , so that the truth valuations are imbedded as the corners of the unit hypercube $(v = (v_1, \ldots, v_s)$ going to $x = (x_1, \ldots, x_s)$ where $x_j = 1$ iff $v_j = T$ and $x_j = 0$ iff $v_j = F$ ). Then one sets $\operatorname{Imb}(P_j) = \{x \in \operatorname{Imb}(\Omega) | x_j = 1\}$ , $\operatorname{Imb}(\neg P_j) = \{x \in \operatorname{Imb}(\Omega) | x_j = 0\}$ . By Theorem 3.3 with $q = s$ , $n = 0$ , $q^* = 2^s$ , if $s \geqslant 2$ there will be d.n.f.'s $L_1$ and $L_2$ with $L_1 \wedge L_2 = \emptyset$ and $\operatorname{Rel}(\underline{L}_1 \wedge \underline{L}_2) \neq \emptyset$ for this imbedding. The sharp imbedding requires dimension $q = 2^s - 1$ .

There are many imbeddings which are intermediate between the standard and the sharp imbedding. To illustrate one of these, let $1 < r < s$ and for all $\gamma: \{1, \ldots, r\} \to \{-1, 1\}$ we introduce a binary variable $x(\bigwedge_{j=1}^{r} P_j^{\gamma(j)}) = x^{(\gamma)}$ . For $r < j \leqslant s$ , we have a binary variable $x_j$ . Then the truth valuation $v = (v_1, \ldots, v_s)$ is imbedded as the point $\operatorname{Imb}(v)$ for which $x(\gamma') = 1$ , $x(\gamma) = 0$ for $\gamma \neq \gamma'$ , $x_j = 1$ if $j > r$ and $v_j = T$ , $x_j = 0$ if $j > r$ and $v_j = F$ . $\gamma'$ is the unique mapping for which $\bigwedge_{j=1}^{r} P_j^{\gamma(j)}$ is made true by the valuation. This imbedding is in a space of dimension $2^r + (s - r)$ . Of course $\operatorname{Imb}(P_j) = \cup \{\operatorname{Imb}(v) | v \text{ makes } P_j \text{ true}\}$ .

In the standard imbedding, with the standard representation of each $P_j$ , it is interesting to note what the linear relaxation of a conjunctive normal form is. For example, the clause $P_1 \vee P_2 \vee P_3$ in a c.n.f. has a representation, the linear relaxation of which is the projection to $x = (x_1, x_2, x_3, \ldots, x_s)$ -space of this linear system:

$$
x _ {1} ^ {(1)} = \lambda_ {1}, \quad x _ {2} ^ {(2)} = \lambda_ {2}, \quad x _ {3} ^ {(3)} = \lambda_ {3},\tag{4.7}
$$

$$
0 \leqslant x ^ {(1)} \leqslant e \lambda_ {1}, \quad 0 \leqslant x ^ {(2)} \leqslant e \lambda_ {2}, \quad 0 \leqslant x ^ {(3)} \leqslant e \lambda_ {3},
$$

$$
\lambda_ {1} + \lambda_ {2} + \lambda_ {3} = 1, \quad 0 \leqslant \lambda_ {1}, \lambda_ {2}, \lambda_ {3},
$$

$$
x _ {j} = x _ {j} ^ {(1)} + x _ {j} ^ {(2)} + x _ {j} ^ {(3)}, \quad j = 1, \dots , s.
$$

Here, $e = (1, 1, \ldots, 1)$ is the vector of $1's$ .

From (4.7), $x_{1} + x_{2} + x_{3} \geqslant \lambda_{1} + x_{1}^{(2)} + x_{1}^{(3)} + x_{2}^{(2)} + \lambda_{2} + x_{2}^{(3)} + x_{3}^{(1)} + x_{3}^{(2)} + \lambda_{3} \geqslant \lambda_{1} + \lambda_{2} + \lambda_{3} = 1$ and $0 \leqslant x_{j} \leqslant 1$ for $j = 1, \ldots, s$ . In fact, it can be shown that the projection describes is precisely $x_{1} + x_{2} + x_{3} \geqslant 1$ ,

$$
0 \leqslant x _ {j} \leqslant 1 \quad \text { for } j = 1, \dots , s.\tag{4.8}
$$

The proof of this fact is tedious, so we omit it.

(As a hint, $x_1 \geqslant x_2 \geqslant x_3$ can be assumed in (4.8) without loss of generality. Then in (4.7), one can take $\lambda_1 = x_1$ , $\lambda_2 = \min\{1 - \lambda_1, x_2\}$ , $\lambda_3 = \min\{1 - \lambda_1 - \lambda_2, x_3\}$ , $x_k^{(j)} = 0$ for $j \geqslant k + 1$ and $k = 1, 2, 3$ ; $x_2^{(1)} = x_2 - \lambda_2$ ; $x_3^{(1)} = x_3 - \lambda_3$ ; $x_3^{(2)} = 0$ .)

The projection result (4.8) is of a general nature, so that a c.n.f. in standard imbedding is treating by the familiar ‘generalized set covering’ constraints of the standard treatments. This was the kind of constraint systems we investigated in [6]. The ability to screen propositional forms without branching (i.e., without operations which are analogous to resolution) can be improved by use of the alternate imbedding above, for example.

Example 4.3. Here we shall discuss a class of potential applications which are of a database nature. The non-spatial domain D of course plays a crucial role in such applications.

The example will also allows us to show techniques for 'imbedding individuals', even though formally only predicates are imbedded. This example will also illustrate a common application in which $q^*$ (the number of nonempty elementary conjuncts) is not very large, and the sharp embedding can be literally used.

An element $(x, d) \in \Omega$ shall have the form $x = (x_{1}, \ldots, x_{n})$ , $d = (d_{n+1}, d_{n+2}, d_{n+3}, d_{n+4}, d_{n+5}, d_{n+6}) = (\text{customer, city, volume class, credit class, service assignment, last billing})$ . Here $d_{n+1}$ is the customer account, $d_{n+2}$ is the city nearest to the local market in which the customer firm operates, volume class denotes the one of four possible customer groups which a marketing analysis has assigned to the customer, and credit class is one of three possible groups and depends on the average number of days that an outstanding balance has remained unpaid by that customer in the last year. The ‘last billing’ is the total dollar volume ordered last by the customer, which falls into one of five categories.

The ‘service assignment’ co-ordinate has one of two values, accordingly as the customer is served by the local sales office, or by the nearest regional warehouse which may serve several cities. It is not data, but is set at the discretion of the Apex Corporation, whose records we are describing. The superior service of the sales offices is reserved for the best customers. On the other hand, it is known that a customer tends to purchase more if given the superior service.

As regards the spatial part x, $x_{i}$ denotes the amount of the ith Apex product ordered by the customer over the previous twelve-month period. There are two ‘possibility sets’ $X_{1}$ and $X_{2}$ , such that $x \in X_{1}$ if service is from the warehouse, $x \in X_{2}$ if service is from the sales office, etc. The sets $X_{1}$ and $X_{2}$ may be polyhedra, or b-MIP.r representable, with the same recession cones.

In database terms the ‘record’ $(x, d) \in \Omega$ may have been created by use of two tables (database ‘relations’), in both of which the customer account name is the key field [57] (the field which determines the value of the other fields). One of the two tables may have detailed, e.g., the customer, city and volume class; the second table may have contained the fields of customer, credit class, and last billing. The first table tends to be used by marketing personnel; the second is part of the view of the billing personnel. Since the service assignment is yet undetermined and at management discretion, it is not in any table ('relation').

The Apex Corporation has 100,000 customers in 50 cities. The number of possible elements $\hat{d} = (d_{n+2}, d_{n+3}, d_{n+4}, d_{n+6})$ (note that the customer $(d_{n+1})$ and the service assignment $(d_{n+5})$ are missing here) is $50 \times 4 \times 3 \times 5 = 3,000$ ; however, the number of distinct $d \in D$ is $10,000 \times 3,000 \times 2 = 6 \times 10^7$ .

We shall develop predicates for ‘individuals’ $\hat{d}$ but not for each $d \in D$ . This is appropriate if $\hat{d}$ determines the set of the spatial co-ordinate. Here this means that $\hat{d}$ determines the set of possible demands for the customer; i.e., two customers in the same city, in the same volume class, with the same credit standing and last billing category, will be served from the same source (sales office or warehouse). It is significant here, that the individuals $\hat{d}$ do not have the key field (i.e., customer account) of both of the data base tables from which records $(x, d) \in \Omega$ constructed.

For each $\hat{d} \in \hat{D}$ ( $\hat{D}$ is all tuples ( $d_{n+2}$ , $d_{n+3}$ , $d_{n+4}$ , $d_{n+6}$ )) we define a predicate $P[\hat{d}]$ by

$$
(x, d) \in P [ \hat {d} ] \leftrightarrow d _ {i} = \hat {d} _ {i}
$$

$$
\text { for   } i = n + 2, n + 3, n + 4, n + 6.\tag{4.9}
$$

From (4.9) if $\hat{d}$ , $\hat{g} \in D$ and $\hat{d} \neq \hat{g}$ , then $P[\hat{d}] \cap P[\hat{g}] = \emptyset$ . Moreover, $\Omega = \bigcup_{\hat{d} \in \hat{D}} P[\hat{d}]$ , so that $\neg P[\hat{d}] = \Omega \setminus P[\hat{d}] = \cap \{P[\hat{g}] | \hat{g} \neq \hat{d}\}$ .

We view that each $\hat{d}$ corresponds to an index $j$ of a relation $P_{j}$ of the model $M = (X, D, \Omega; P_{1}, \ldots, P_{s})$ so that there are $s\hat{d}$ in number. From our comments in the last paragraph, we compute

$$
\begin{array}{l l} \bigcap_ {j = 1} ^ {s} P _ {j} ^ {\gamma (j)} = P [ \hat {d} ], & \text { if } \gamma (j) = + 1 \text { for   exactly } \\ & \text { one } j, \text { which } \\ & \text { corresponds to } \hat {d}, \\ = \emptyset , & \text { if } \gamma (j) = + 1 \text { for   more   than } \\ & \text { one } j, \\ = \emptyset , & \text { if } \gamma (j) = - 1 \text { for   all } j. \end{array} \tag {4.10}
$$

In general, for an imbedding via ‘individuals’ $\hat{d}$ , the associated relations $P[\hat{d}]$ correspond exactly to the non-empty elementary conjuncts. Here, there are at most 3,000 such non-empty conjuncts, although $2^{3000}$ were theoretically possible. Of course, often some $P[\hat{d}]=\emptyset$ (i.e., for some specific sity, volume, credit class, and last billing category, there are no customers with the given specifications). That will simply reduce the computation effort in the treatment described below.

We shall use the sharp embedding, which here requires y of dimension not exceeding 3,000. (More precisely, the dimension is 3,000 less the number of empty $P[\hat{d}]$ .) To this figure, the dimension n of the spatial part $x = (x_1, \ldots, x_n)$ and one dimension for the service assignment must be added.

The determination of the sharp embedding is equivalent to the determination of which $P[\hat{d}] \neq \emptyset$ , for such $P[\hat{d}]$ correspond exactly to coordinates $y[\hat{d}]$ of y in that embedding. This involves preprocessing work, which is justified by the fact that the database will be used repeatedly for inquiries. I.e., unlike many Operations Research models M, which are run with a few dozen to a few hundred parameter variations, the database may be used for tens of thousands of inquiries by hundred of users.

The pre-processing necessary can be done as follows. For each customer (the 'key field' of both tables), one creates the corresponding $\hat{d}$ . It will also be helpful to maintain a table which shows, for $\hat{d}$ with $P[\hat{d}] \neq \emptyset$ , all the customers from which $\hat{d}$ derived. (This table greatly assists in 'updating' the sharp embedding, as the set of customers changes over time.)

As in Theorem 3.2, we assume that sharp representations $P[\hat{d}]$ of the $P[\hat{d}]$ are fixed. This assumption is satisfied by the choice of unit vectors in the sharp imbedding, with the natural representation, combined via the Cartesian product with the two possible settings of the service assignment, and with a sharp representation of the demand possibilities $x \in X$ for the assignment (no coordinate is needed for the 10,000 customer firms).

Using the sharp representations $P[\hat{d}]$ , one can obtain sharp representations for each of the following classes of propositional logic forms L by use of the union construction for representations:

$$
\operatorname{City} \left(\hat {d} _ {n + 2}\right) = \bigcup_ {\hat {d} \in \hat {D}} \left\{P [ \hat {d} ] \mid d _ {n + 2} = \hat {d} _ {n + 2} \right\}.\tag{4.11a}
$$

$$
\operatorname{Vol} \left(\hat {d} _ {n + 3}\right) = \bigcup_ {\hat {d} \in \hat {D}} \left\{P [ \hat {d} ] \mid d _ {n + 3} = \hat {d} _ {n + 3} \right\},\tag{4.11b}
$$

$$
\operatorname{Cred} \left(\hat {d} _ {n + 4}\right) = \bigcup_ {\hat {d} \in \hat {D}} \left\{P [ \hat {d} ] \mid d _ {n + 4} = \hat {d} _ {n + 4} \right\},\tag{4.11c}
$$

$$
\operatorname{Bill} \left(\hat {d} _ {n + 6}\right) = \bigcup_ {\hat {d} \in \hat {D}} \left\{P [ \hat {d} ] \mid d _ {n + 6} = \hat {d} _ {n + 6} \right\}.\tag{4.11d}
$$

The following inquiry is to be answered: 'Is there any customer, in either New York, Atlanta, or Minneapolis, in one of the top two volumes classes, who is also in the two lower credit classes, and has a last billing in one of the top three categories?' That is equivalent to the question, as to whether or not the following predicate is empty:

$$
\begin{array}{r l} & (\text { City } (N Y) \lor \text { City } (A t l) \lor \text { City } (M n)) \\ & \wedge (\text { Vol } (3) \lor \text { Vol } (4)) \lor (\text { Cred } (2) \wedge \text { Cred } (3)) \\ & \wedge (\text { Bill } (3) \lor \text { Bill } (4) \lor \text { Bill } (5)). \end{array} \tag {4}\tag{4.12}
$$

From Theorem 3.2, $L = \emptyset$ iff $\operatorname{Rel}(L) = \emptyset$ ; hence the question can be answered by linear programming, if one wishes. If $L \neq \emptyset$ , one can determine the maximum quantity $x_{1}$ of Apex product one, which might possibly be ordered by such a customer, by solving the linear program $\min\{-x_{1}|(x, y) \in \operatorname{Rel}(L)\}$ .

The literal use of the Simplex Method (or a general LP code) is not recommended here, as one can achieve the equivalent effect by logic processing routines, when the sharp embedding is used. If we let $\operatorname{supp}(L)$ denote the set of non-empty elementary conjuncts (here $P[\hat{d}] \neq \emptyset$ ) which support $L$ we have, from (3.3)

$$
\left(L _ {1} \vee L _ {2}\right) = \operatorname{supp} \left(L _ {1}\right) \cup \operatorname{supp} \left(L _ {2}\right),\tag{4.13a}
$$

$$
\operatorname{supp} \left(L _ {1} \wedge L _ {2}\right) = \operatorname{supp} \left(L _ {1}\right) \cap \operatorname{supp} \left(L _ {2}\right).\tag{4.13b}
$$

Using (4.13), it is easy to compute $\operatorname{supp}(L)$ in (4.12). In this manner, one can determine if $\operatorname{supp}(L) = \emptyset$ ; and by (3.3c) $\operatorname{supp}(L) = \emptyset$ iff $L = \emptyset$ . When $\operatorname{supp}(L) \neq \emptyset$ , one can use the pre-processing work to recover the information needed for optimizations such as the one cited.

A study of the linear constraints involved in $\operatorname{Imb}(L)$ will reveal that a linear programming routine effectively does the same calculation of $\operatorname{supp}(L)$ , actually using the $y_i = 0$ settings (i.e., the non-support set). Clearly, it is more advantageous to do it directly as a logic routine, than to be carrying along irrelevant data structures, such as vectors, bases, etc.

By inclusion into $\hat{d}$ of the policy variables, which are only $d_{n+5}$ (service assignment) here, consequences of policies can be partially examined by the same techniques. For example, consider the policy: 'All customers in the bottom two volume groups, or customers with one of the two lower last billings and in the worst credit class, shall be served by the warehouse'. This is the implication:

$$
\begin{array}{l} \left(\operatorname{Vol} (1) \vee \operatorname{Vol} (2)\right) \\ \quad \vee \left(\left(\operatorname{Bill} (1) \vee \operatorname{Bill} (2)\right) \wedge \operatorname{Cred} (3)\right) \\ \Rightarrow \operatorname{Serv} (\mathbf {W H}) \end{array}\tag{4.14}
$$

where predicates $\operatorname{Serv}(d_{n+6})$ have been introduced as in (3.25). To determine the maximum amount of product 2 ordered by a customer who does not currently satisfy (4.14), one maximizes $x_{2}$ for $(x, d) \in L$ with

$$
\begin{array}{r l} L = (\operatorname{Vol} (1) \vee \operatorname{Vol} (2)) \\ & \wedge ((\operatorname{Bill} (1) \vee \operatorname{Bill} (2)) \wedge \operatorname{Cred} (3)) \\ & \wedge \neg \operatorname{Serv} (\mathbf {W H}). \end{array}
$$

## 5. A Result a Quantified Forms

Here we give a result on the imbeddability of forms in which logical quantifiers (∃ and ∀) may occur.

This result is primarily of theoretical interest, with the focus of that interest on logical quantification for spatial co-ordinates. The ‘pre-processing’ needed to obtain these predicate logic imbeddings rules out their practical use in a direct way, in most instances. Thus techniques of ‘partial imbedding’ are needed, and these will be discussed elsewhere.

The result below is an extension of Bender's decomposition [4], which it in fact yields when all quantifiers are existential and are on continuous spatial variables, and all variables are continuous. Bender's decomposition has been successfully used in settings of partial imbedding (see, e.g., [17]).

Theorem 5.1. Let a model $M = (X, D, \Omega; P_1, \ldots, P_s)$ be given. Suppose that $D$ is finite and for $d \in D$ , define

$$
\Omega (d) = \{x | (x, d) \in \Omega \},\tag{5.1a}
$$

$$
P _ {j} (d) = \left\{x \mid (x, d) \in P _ {j} \right\}.\tag{5.1b}
$$

If all $\Omega(d)$ and $P_{j}(d)$ for all $d\in D$ are $b$ -MIP. $r$ , and $\operatorname{rec}(\Omega(d))=\{0\}$ , then any finite collection of quantified predicates based on $\Omega$ , $P_{1},\ldots,P_{s}$ is $b$ -MIP. $r$ . spatially imbeddable.

The proof of Theorem 5.1 requires that we develop two new concepts (semhedra and u-semis) and lemmas concerning these concepts.

By a semi-hedron $P = \{x \in R^n | Ax \geqslant b, Cx > d\}$ we mean a set defined by a system of ordinary inequalities ( $Ax \geqslant b$ ) and strict inequalities ( $Cx > d$ ). Either set may be empty (if both are empty, $P = R^n$ ). Here $A$ and $C$ are matrices, $b$ and $d$ are vectors.

Trivially, a semi-hedron is convex, and the intersection of finitely many semihedra is a semi-hedron. The closure of a semi-hedron is a polyhedron, as our next result shows.

Lemma 5.1. If $P = \{x \in R^n | Ax \geqslant b, Cx > d\} \neq \emptyset$ is a non-empty semi-hedron, then its closure $cl(P)$ is given by

$$
c l (P) = \{x \in R ^ {n} | A x \geqslant b, C x \geqslant d \}.\tag{5.2}
$$

Proof. Fix $x^0 \in P$ . Let $x' \in R^n$ be such that

$Ax' \geqslant b, Cx' \geqslant d.$ As the r.h.s. of (5.2) defines a closed set containing $P$ , it suffices to show that $x' \in \operatorname{cl}(P)$ .

For $x \in [x^0, x')$ on the line segment from $x^0$ to $x'$ , a direct computation shows that $Cx > c$ . Hence $x \in P$ . As we may send $x$ to $x'$ , the proof is complete. Q.E.D.

Lemma 5.2. Let $P = \{(x, y) \mid A_1x + A_2y \geqslant b, C_1x + C_2y > d\}$ be a semi-hedron. Define $P'$ to be the projection

$$
P ^ {\prime} = \{x | \text { for   some } y, (x, y) \in P \}.\tag{5.3}
$$

Then $P'$ is a semi-hedron.

Proof. For a fixed $x, x \in P'$ iff the following system of linear inequalities is consistent in $y$ :

$$
A _ {2} y \geqslant b - A _ {1} x, \quad C _ {2} y > d - C _ {1} x.\tag{5.4}
$$

By the Kuhn–Fourier Theorem [51], (5.4) is consistent iff there do not exist $\lambda$ , $\theta$ satisfying

$$
\lambda , \theta \geqslant 0,
$$

$$
\lambda A _ {2} + \theta C _ {2} = 0,\tag{5.5}
$$

$$
\text { and   if } \theta = 0, \lambda (b - A _ {1} x) > 0,
$$

$$
\text { if } \theta \neq 0, \lambda (b - A _ {1} x) + \theta (d - C _ {1} x) \geqslant 0.
$$

The polyhedral cone $H = \{(\lambda, \theta) \geqslant 0 \mid \lambda A_2 + \theta C_2 = 0\}$ has a finite basis [51], i.e., for a non-empty, finite index set $I$

$$
H = \operatorname{cone} \left(\left\{\left(\lambda^ {(i)}, \theta^ {(i)}\right) | i \in I \right\}\right).\tag{5.6}
$$

Thus, if (5.4) is consistent, then we must have

$$
\lambda^ {(i)} (b - A _ {1} x) \leqslant 0 \quad \text { for } i \in I \text { with } \theta^ {(i)} = 0,\tag{5.7}
$$

$$
\lambda^ {(i)} (b - A _ {1} x) + \theta^ {(i)} (d - C _ {1} x) <   0
$$

for $i \in I$ with $\theta^{(i)} \neq 0$ .

We claim that (5.7) is equivalent to the consistency of (5.4). This claim is sufficient to complete the proof, since in variables x, (5.7) defines a semi-hedron. Moreover, to establish the claim it suffices to prove that (5.7) implies the consistency of (5.4).

Suppose that (5.7) holds and yet (5.4) is inconsistent. Then for some $(\lambda, \theta) \in H$ , by (5.5)

if $\theta = 0$ , then $\lambda (b - A_1x) > 0$ ;

$$
\text { if } \theta \neq 0, \quad \text { then } \lambda (b - A _ {1} x) + \theta (d - C _ {1} x) \geqslant 0.\tag{5.8}
$$

Moreover, for suitable scalars $p_i \geqslant 0$ , $\Sigma_{i \in I} p_i = 1$ , we have $(\lambda, \theta) = \Sigma_{i \in I} p_i (\lambda^{(i)}, \theta^{(i)})$ by (5.6).

Clearly, $\theta \neq 0$ iff for some $i$ with $p_i \neq 0$ also $\theta^{(i)} \neq 0$ .

We compute, using (5.7)

$$
\begin{array}{r l} & {\lambda (b - A _ {1} x) + \theta (d - C _ {1} x)} \\ & {\quad = \sum_ {i} \left\{p _ {i} \lambda^ {(i)} (b - A _ {1} x) \mid \theta^ {(i)} = 0 \right\}} \\ & {\qquad + \sum_ {i} \left\{p _ {i} \lambda^ {(i)} (b - A _ {1} x) \right.} \\ & {\qquad \qquad \left. + p _ {i} \theta^ {(i)} (d - C _ {1} x) \mid p _ {i} > 0, \theta^ {(i)} \neq 0 \right\}} \\ & {\leqslant \sum_ {i} \left\{p _ {i} \lambda^ {(i)} (b - A _ {1} x) \right.} \\ & {\qquad \qquad \left. + p _ {i} \theta^ {(i)} (d - C _ {1} x) \mid p _ {i} > 0, \theta^ {(i)} \neq 0 \right\}.} \end{array}\tag{5.9}
$$

(In (5.9), a sum over an empty index set is taken to be zero.) If $\theta = 0$ , then last summation is zero, so that $\lambda(b - A_1x) \leqslant 0$ , contradicting (5.8). If $\theta \neq 0$ , the last summation is strictly negative, again contradicting (5.8). This contradiction completes the proof. Q.E.D.

A finite union of semi-hedra is termed a u-semi. We need to establish several results regarding such sets. First, observe that the complement $P^{c}$ of a semi-hedron is a u-semi: it is the union of the finitely many sets obtained each by reversing an inequality of P and erasing the remaining inequalities (the reversal of $\geqslant$ being <, and the reversal of > being $\leqslant$ ).

Lemma 5.3. Let $S_{1}$ and $S_{2}$ be u-semis. Then the following are also u-semis:

(1) $S_{1} \cup S_{2}$ ,

(2) $S_{1} \cap S_{2}$ ,

(3) $S_{1}^{c}$ ,

(4) $S_{1} \setminus S_{2}$ ,

(5) any projection $S_1'$ of $S_1$ ,

(6) $S_{1} \times S_{2}$ (Cartesian product).

Proof. Put $S_{1} = \bigcup_{i\in I}P_{i}, S_{2} = \bigcup_{j\in J}Q_{j}$ , for non-empty finite index sets $I$ and $J$ , where each $P_{i}$ and each $Q_{j}$ is a semi-hedron.

(1) $S_{1} \cup S_{2} = (\bigcup_{i \in I} P_{i}) \cup (\bigcup_{j \in J} Q_{j})$ is the proof.

(2) Observe that $S_{1} \cap S_{2} = \bigcup_{i \in I} \bigcup_{j \in J} (P_{i} \cap Q_{j})$ and that each $P_{i} \cap Q_{j}$ is a semi-hedron.

(3) $S_1^c = \bigcup_{i \in I} P_i^c$ with each $P_i^c$ a semi-hedron; here part (2) applies to give the result.

(4) $S_{1} \setminus S_{2} = S_{1} \cap S_{2}^{c}$ ; parts (2) and (3) apply.

(5) Let the projection of $P_{i}$ , upon the same coordinates as that for $S_{1}$ , be denoted $P_{i}'$ . Observe that $S_{1}' = \bigcup_{i \in I} P_{i}'$ ; and Lemma 2 applies. (6) $S_{1} \times S_{2} = \bigcup_{i} \bigcup_{j} (P_{i} \times Q_{j})$ and the result follows from (1) above. Q.E.D.

Lemma 5.4. Let $S$ be a u-semi and $P$ a semi-hedron with $\text{rec}(cl(P)) = \{0\}$ . Then $cl(S \cap P)$ is b-MIP.r; and moreover $\text{rec}(cl(S \cap P)) = \{0\}$ if $S \cap P \neq \emptyset$ . Also, $clconv(S \cap P)$ is a polyhedron; moreover, $\text{rec}(clconv(S \cap P)) = \{0\}$ if $S \cap P \neq \emptyset$ .

Proof. Let us write $S = \bigcup_{i \in I} P_i$ as in the proof of Lemma 5.3. We have $S \cap P = \bigcup_{i \in I} (P \cap P_i)$ , with each $P \cap P_i$ a semi-hedron, and if $P \cap P_i \neq \emptyset$ , then $\operatorname{cl}(P \cap P_i)$ is a polyhedron by Lemma 5.1.

As there is nothing to prove if $S \cap P$ is empty, we assume $S \cap P \neq \emptyset$ in what follows.

Let $I' = \{i \in I \mid P \cap P_i \neq \emptyset\}$ . Then $\operatorname{cl}(S \cap P) = \cup_{i \in I'} \operatorname{cl}(P \cap P_i)$ , where $\operatorname{cl}(P \cap P_i)$ is a non-empty polyhedron contained in the polyhedron $\operatorname{cl}(P)$ which has $\operatorname{rec}(\operatorname{cl}(P)) = \{0\}$ . Thus $\operatorname{rec}(\operatorname{cl}(P \cap P_i)) = \{0\}$ for $i \in I$ ; and by Theorem 2.1 $\operatorname{cl}(S \cap P)$ is b-MIP.r.

By the existence of sharp representations (2.6) and Proposition 2.1, $\operatorname{conv}(\operatorname{cl}(S \cap P))$ is a polyhedron, and $\operatorname{clconv}(S \cap P) = \operatorname{clconv}(\operatorname{cl}(S \cap P)) = \operatorname{conv}(\operatorname{cl}(S \cap P)$ . By Proposition 2.1, $\operatorname{rec}(\operatorname{clconv}(S \cap P))) = \operatorname{rec}(\operatorname{conv}(\operatorname{cl}(S \cap P))) = \operatorname{rec}(\operatorname{cl}(S \cap P)) = \{0\text{ since } \operatorname{cl}(S \cap P) \subseteq \operatorname{cl}(P) \text{ and } \operatorname{rec}(\operatorname{cl}(P))\} = \{0\}$ . Q.E.D.

We now proceed to the proof of Theorem of 5.1.

Proof. Let $Q_1, \ldots, Q_t$ be the quantified forms based on the predicates $\Omega, P_1, \ldots, P_s$ . Without loss of generality, the $Q_1, \ldots, Q_t$ are in Prenex Normal Form i.e., the logical quantifiers precede a propositional matrix. Define for $d \in D$

$$
Q _ {i} (d) = \{x | (x, d) \in Q _ {i} \}.\tag{5.10}
$$

We shall need the following result before we can proceed further with the proof.

Lemma 5.5. Let the assumptions of Theorem 5.1 hold. Then $Q_{i}(d)$ is a $u$ -semi contained in $\Omega(d)$ for $i = 1, \ldots, t$ and all $d \in D$ .

Proof. The proof is by induction on the sum of the number q of logical quantifiers used in the construction of all the $Q_{i}$ .

If $q = 0$ , $Q_{i}(d)$ is a propositional form in the $P_{j}(d)$ , $1 \leqslant j \leqslant s$ . As $P_{j}(d) \subseteq \Omega(d)$ and $\neg P_{j}(d) \subseteq \Omega(d)$ with $\operatorname{rec}(\Omega(d)) = \{0\}$ , we have $\operatorname{rec}(P_{j}(d)) = \operatorname{rec}(\neg P_{j}(d)) = \{0\}$ for all $j$ . As the propositional form $Q_{i}(d)$ has a d.n.f., $Q_{i}(d)$ is a finite union of sets with zero recession direction. By Theorem 2.1, $Q_{i}(d)$ is a b-MIP.r. Clearly, a b-MIP.r set is a u-semi (it is a finite union of polyhedra).

Suppose that $q > 0$ . Write $Q = Q_i$ , $Q = (\exists d_{i*})Q'$ or $(\forall d_{i*})Q'$ , where by induction each $Q'(d)$ is a u-semi for all $d \in D$ . We explicitly treat only the existential quantifier case that $Q = (\exists d_{i*})Q'$ .

Once the existential quantifier case is established, it can be used to obtain the universal quantifier case. Indeed $(\forall d_{i*})Q' = \neg(\exists d_{i*})\neg Q'$ . By the inductive hypothesis, each $\neg Q'(d)$ is a u-semi. From the existential quantifier case, we will then have that each set $[(\exists d_{i*})\neg Q'](d), d \in D$ , is a u-semi. Then we calculate that $[(\forall d_{i*})Q'](d) = \{x | (x, d) \in \neg(\exists d_{i*})\neg Q'\} = \Omega(d) \setminus [(\exists d_{i*})\neg Q'](d)$ . From part (4) of Lemma 5.3, we will then have that each $[(\forall d_{i*})Q'](d)$ is a u-semi. Let us therefore now turn to the existential quantifier case.

There are then two subcases, according to whether the index $i^*$ of the quantifier is spatial ( $i^* \in \{1, \ldots, t\}$ ) or logical ( $i^* \in \{t + 1, \ldots, r\}$ ).

When $i^*$ is a spatial index let $S'$ denote the projection of $S = Q(d)$ on the co-ordinates other than $d_{i*}$ ; without loss of generality, $i^* = 1$ . As a union of u-semis, $S'$ is a u-semi by part (1) of Lemma 5.3. As $S \subseteq \Omega(d)$ and each $\text{rec}(\Omega(d)) = \{0\}$ , we have $\text{rec}(S) = \{0\}$ if $S \neq \emptyset$ . By part (5) of Lemma 5.3, $S'$ is a u-semi. Let $D_1$ be the projection of $\Omega(d)$ into its first coordinate. By the hypothesis on $\Omega(d)$ and Theorem 2.3, $D_1$ is b-MIP.r. Hence also $T' = D_1 \times S'$ is a u-semi by part (6) of Lemma 5.3.

When $i^*$ is a logical index, define $T = \bigcup_{\overline{d}} \{Q'(\overline{d}) | \overline{d} = d_i \text{ for } i \neq i^*\}$ . By Lemma 5.3, $T$ is a u-semi. Note that $Q(d) = T \cap Q'(d)$ . As each $Q'(\overline{\mathrm{d}})$ is a u-semi, so is $Q(d)$ by Lemma 5.3. Q.E.D.

We now continue the proof of the Theorem.

As each $Q_{i}(d)$ is a u-semi, as well as each $\Omega(d)$ , so is $\neg Q_{i}(d) = \Omega(d) \setminus Q_{i}(d)$ by Lemma 5.3.

Let $\Gamma$ be the set of all mappings $\gamma: \{1, \ldots, t\} \to \{1, -1\}$ from $\{1, \ldots, t\}$ into $\{1, -1\}$ . From the above, each set $T(\gamma, d) = \bigcap_{i=1}^{t} Q_i^{\gamma(i)}(d)$ is a u-semi, by Lemma 5.3, and is contained in the MIP.r. set $\Omega' = \bigcup_{d \in D} \Omega(d)$ with $\operatorname{rec}(\Omega') = \{0\}$ . By Proposition 2.1, $P = \operatorname{conv}(\Omega')$ is a polyhedron with $\operatorname{rec}(P) = \{0\}$ . By Lemma 5.3, each set $T(L') = \bigcup_{d \in D} T(L', d)$ is a u-semi contained in $P$ .

By Lemma 5.4, $\operatorname{clconv}(T(L') \cap P) = \operatorname{clconv}(T(L'))$ is a polyhedron with $\operatorname{rec}(\operatorname{clconv}(T(L'))) = \{0\}$ if $T(L') \neq \emptyset$ . By Theorem 3.1, the model $M' = (X, D, \Omega; Q_1, \ldots, Q_t)$ with the (quantified) predicates $Q_1, \ldots, Q_t$ is spatially-imbeddable in a b-MIP.r manner. Q.E.D.

## 6. Summary and Conclusions

We have shown that, under mild hypotheses, model structures which include optimization, database, and logic components, are imbeddable in Euclidean space as an optimization structure, in such a manner as to allow the uniform processing of queries based on the propositional connectives (Theorem 3.1). The necessary and sufficient condition for imbeddability is essentially that the spatial component of the model structure, for maximally specified queries (i.e., elementary conjunctions), can be treated as a polyhedron for all criterion functions. Representability of such spatial components is sufficient, but by no means necessary, to meet this condition.

We have also seen that, when model is imbeddable, it has an imbedding in which, for all queries, the linear relaxation is equivalent to taking the convex span of feasible points, so that all linear optimizations can be done via this relaxation (Theorem 3.2). However, this 'sharp' embedding can require excessively high dimension (Theorem 3.3), and further research is needed to explore means of dynamically activating this imbedding as needed, rather than proceeding to it directly.

Imbeddability often extends in principle to predicate logic queries (Theorem 5.1), where again future research is appropriate for dynamic activation (similar to the addition of Benders' cuts as needed).

Future investigations will no doubt seek a better understanding, in concrete applications, of the relationships between logic, database, and optimization algorithms for processing queries. As these relationships are very much affected by the imbedding chosen for a model structure, further work in

MIP representability is likely to be crucial to this program.

## References

[1] E. Balas, Disjunctive Programming: Cutting-planes from Logical Conditions, in: O.L. Mangasarian, R.R. Meyer, and S.M. Robinson, Nonlinear Programming 2 (Academic Press, New York, 1975) 279–312.

[2] E. Balas, Disjunctive Programming: Facets of the Convex Hull of Feasible Points, no. 348, GSIA, Carnegie-Mellon University (1974).

[3] E. Balas, Disjunctive Programming, in: P.L. Hammer, E.L. Johnson, and B.H. Korte, eds., Discrete Optimization II (North Holland Publishing Company, 1979) 3–52.

[4] J.F. Benders, Partitioning Procedures for Solving Mixed Variable Extremum Problems, Numerische Math. 4 (1962) 238–251.

[5] C.E. Blair, Two Rules for Deducing Valid Inequalities for Zero-One Programs, SIAM Journal of Applied Math 31 (1977) 614–617.

[6] C.E. Blair, R.G. Jeroslow, and J.K. Lowe, Some Results and Experiments on Programming Techniques for Propositional Logic, Computers and Operations Research 13 (1986) 633–645.

[7] W.W. Bledsoe and D.W. Loveland, eds. Automated Theorem Proving: After 25 Years, Contemporary Mathematics, vol. 29 (American Mathematical Society, Rhode Island, 1983).

[8] Robert H. Bonczek, Clyde W. Holsapple, and Andrew B. Whinston, Foundations of Decision Support Systems (Academic Press, New York, 1982).

[9] A. Charnes and W.W. Cooper, Management Models and Industrial Applications of Linear Programming, Vols. I and II (John Wiley, New York, 1961).

[10] H. Crowder, E.L. Johnson, and M.W. Padberg, Solving Large-Scale Zero-One Linear Programming Problems, Operations Research 31 (1983) 803–834.

[11] H. Crowder and M.W. Padberg, Solving Large-Scale Symmetric Travelling Salesman Problems to Optimality, Management Science 26 (1980) 495–509.

[12] G.B. Dantzig, Linear Programming and Extensions, (Princeton, NJ, Princeton University Press, 1963).

[13] G.B. Dantzig, Discrete Variable Extremum Problems, Operations Research 5 (1957) 266–277.

[14] Randall Davis and Douglas B. Lenat, Knowledge-Based Systems in Artificial Intelligence (McGraw-Hill International, New York, 1982).

[15] R. Davis and B. Buchanan, E. Shortliffe, Production Rules as a Representation for a Knowledge-Based Consultation Program, Artificial Intelligence 8 (1977) 15–45.

[16] G.D. Eppen and F.J. Gould, Quantitative Concepts for Management (Prentice-Hall, Englewood Cliffs, NJ, 1979).

[17] A.M. Geoffrion and G.W. Graves, Multicommodity Distribution System Design by Benders Decomposition, Management Science 20 (1974) 822–844.

[18] F. Glover, New Results on Equivalent Integer Programming Formulations, Mathematical Programming 8 (1975) 84–90.

[19] F. Glover, Polyhedral Annexation in Mixed Integer and Combinatorial Programming, Mathematical Programming 9 (1975) 161–188.

[20] R.E. Gomory, An Algorithm for Integer Solutions to Linear Programs, in: R.L. Graves and P. Wolfe, eds., Recent Advances in Mathematical Programming (McGraw-Hill, 1983).

[21] P.L. Hammer and S. Rudeanu, Boolean Methods in Operations Research and Related Areas (Springer-Verlag, New York, 1968).

[22] P.L. Hammer, Boolean Procedures for Bivalent Programming, in: Mathematical Programming in Theory and Practice, P.L. Hammer and G. Zoutendijk, eds. (North Holland Publishing Co., New York, 1974) 311–363.

[23] P.L. Hammer, Boolean Procedures in Optimization, Symposia Mathematica 19 (1976) 103–121.

[24] Frederick Hayes-Roth, Donald A. Waterman, and Douglas B. Lenat, Building Expert Systems (Addison-Wesley, Reading, MA, 1983).

[25] T. Ibaraki, Integer Programming Formulation of Combinatorial Optimization Problems, Discrete Mathematics 16 (1976) 39–52.

[26] R. Jeroslow, Cutting-Plane Theory: Disjunctive Methods, Annals of Discrete Mathematics I (1977) 292–330.

[27] R. Jeroslow, Cutting-Planes for Relaxations of Integer Programs, no. 347 GSIA (Carnegie-Mellon University, 1974).

[28] R. Jeroslow, Representability in Mixed-Integer Programming, I: Characterization Results, Discrete Applied Mathematics 17 (1987) 223–243.

[29] R. Jeroslow, Representability in Mixed Integer Programming, II: A Lattice of Relaxations (College of Management, Georgia Institute of Technology, Oct., 1984).

[30] R. Jeroslow and J.K. Lowe, Modelling with Integer Variables, Mathematical Programming Studies 22 (1984) 167–184.

[31] R.G. Jeroslow and J.K. Lowe, Experimental Results on the New Techniques for Integer Programming Formulations, Journal of Operational Research Society 36 (1985) 393–403.

[32] R. Jeroslow, An Extension of Mixed-Integer Programming Models and Techniques to Some Database and Artificial Intelligence Settings (College of Management, Georgia Institute of Technology, May, 1985).

[33] R. Jeroslow, Computation-Oriented Reductions of Predicate to Propositional Logic (College of Management, Georgia Institute of Technology, Aug., 1985).

[34] Robert Kowalski, Logic for Problem-Solving (North-Holland, Amsterdam, 1979).

[35] Donald W. Loveland, Automated Theorem-Proving: A Logical Basis (North Holland, Amsterdam, 1978).

[36] James K. Lowe, Modelling with Integer Variables, Ph.D. thesis (Georgia Institute of Technology, March, 1984).

[37] R.R. Meyer, Integer and Mixed-Integer Programming Models: General Properties, Journal of Optimization Theory and Applications 16 (1975) 191–206.

[38] R.R. Meyer, Mixed-Integer Minimization Models for Piecewise-Linear Functions of a Single Variable, Discrete Mathematics 16 (1976) 163–171.

[39] R.R. Meyer, A Theoretical and Computational Comparison of 'Equivalent' Mixed Integer Formulations, Naval Research Logistics Quarterly 28 (1981) 115–131.

[40] R.R. Meyer, M.V. Thakkar, and W.P. Hallman, Rational Mixed Integer and Polyhedral Union Minimization Models, Mathematics of Operations Research 5 (1980) 135–146.

[41] Arthur J. Nevins, A Human Oriented Logic for Automatic Theorem-Proving, Journal of the Association for Computing Machinery 21 (1974) 606–621.

[42] M.W. Padberg, Covering, Packing, and Knapsack Problems, Annals of Discrete Mathematics 4 (1979) 265–287.

[43] Elaine Rich, Artificial Intelligence (McGraw-Hill, New York, 1983).

[44] J.A. Robinson, A Machine Oriented Logic Based on the Resolution Principle, Journal of the ACM 12 (1965) 23–41.

[45] J.A. Robinson, The Generalized Resolution Principle, in: Machine Intelligence 3, Dale and Mitchie, eds. (Oliver and Boyd, Edinburgh, 1968) 77–93.

[46] R.T. Rockafellar, Convex Analysis (Princeton University Press, Princeton, NJ, 1970).

[47] T.J. Van Roy and L.A. Wolsey, Solving Mixed Integer Programs by Autoamtic Reformulation, CORE Discussion Paper No. 8432 (June, 1984).

[48] Joseph R. Shoenfield, Mathematical Logic (Addison-Wesley, London, 1967).

[49] Edward H. Shortliffe, Randall Davis, Stanton, G. Axline, Bruce G. Buchanan, C. Cordell Green, and Stanley N. Cohen, Computer-Based Consultations in Clinical Therapeutics: Explanation and Rule Acquisition Capabilities of the MYCIN System, Computer and Biomedical Research 8 (1975) 303–320.

[50] Herbert A. Simon, The Structure of Ill-Structured Problems, Artificial Intelligence 4 (1973) 181–201.

[51] J. Stoer and C. Witzgall, Convexity and Optimization in Finite Dimensions I (Springer-Verlag, (1970).

[52] H.P. Williams, Experiments in the Formulation of Integer Programming Problems, Mathematical Programming Study 2 (1974) 180–197.

[53] H.P. Williams, Model Building in Mathematical Programming (John Wiley and Sons (Wiley Interscience), 2nd edition, 1985).

[54] Patrick Henry Winston, Artificial Intelligence, 2nd ed. (Addison-Wesley, London, 1984).

[55] R.D. Young, Hyperlindrically-deduced Cuts in Zero-One Integer Programs, Operations Research 19 (1971) 1393–1405.
