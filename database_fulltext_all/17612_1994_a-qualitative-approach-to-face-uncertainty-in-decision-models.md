---
otero_id: 17612
otero_key: "FN54PK4F"
title: "A qualitative approach to face uncertainty in decision models"
authors: "Alexis Tsoukiàs"
year: "1994"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(94)90047-7"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A qualitative approach to face uncertainty in decision models $^{1}$

Alexis Tsoukiàs

LAMSADE, Université Paris Dauphine, Place du Maréchal de Lattre de Tassigny, 75775 Paris Cedex 16, France

Inaccurate determination, uncertainty, imprecision and ambiguity are often present in complex decision situations where decision aid is requested. Instead of reducing complexity via quantitative models of preferences, as traditional preference modeling does, it may be necessary to represent these situations explicitly. There exist operational methods that face these problems, the principal reference being the partial comparability theory. The lack of an axiomatization however limits the operational potentialities of this theory. In the paper an axiomatic foundation of the partial comparability theory is outlined based on a sound and complete four valued logic (the truth values “true”, “false”, “unknown”, “contradictory” are accepted). This logic is extended to the first order predicate calculus. Four basic preference relations are thus defined, namely: strict preference, weak preference, indifference and incomparability. The operational perspectives are discussed in the paper as some problems in multicriteria methods can be solved in a much easier and natural way. Moreover non monotonic reasoning devices could be built enhancing the potentialities of the theory.

Keywords: Preference modeling; Four valued logic; Partial comparability; Outranking relations

## 1. Introduction

Inaccurate determination, uncertainty, imprecision and ambiguity can often be present in complex decision situations where decision aid is requested (see [24]). Thus we may distinguish between an approach that postulates the correctness of a theory and tries to model the problem “as well as possible” and an approach that fixes the attention to the decision situation and tries to model the problem “as correctly as possible” (correctly in a strictly formalized sense). Of course it is not possible to keep a net distinction between the two approaches because normative theories evolve towards more realistic representations and descriptive approaches have to introduce prescriptions and general assumptions (even if very weak) at least in order to give some general rules for decision aid.

The normative theory gave the basis for the development of quantitative approaches (value theory, expected and multiattribute utility, risk; see [9], [14], [15]; for a review see [10]) where the complexity of the decision situation is reduced in quantifiable representations treated with adequate tools as probability, fuzzy sets, belief functions etc. (see also [13]), while more qualitative work has been done in the other direction where complexity is assumed not to be reducable in a quantifiable model (see [4], [5], [12], [19], [22], [24], [31]) mainly in the field of multicriteria decision aid (MCDA).

![](/api/attachments/FN54PK4F/fulltext/images/e2a2e918773cacf4f33b1b1bcc353e0e42f28486d061e9931906e824f1fcb01d.jpg)

The paper tries to give a contribution in this last direction. The assumption is that some decision situations may present such a complexity that it is impossible to reduce them in some traditional quantitative representation. Moreover the process of decision aid presents features conflicting with the traditional assumptions made in the normative theory ([1], [17], [18], [21]). The fact is that the responsibility for the decision is the decision maker's and not the analyst's and so it is impossible to ignore that the decision maker is involved in decision processes where his ideas, representations, information and values change and evolve.

So if we accept that decision aid is provided during a decision process and that it is a process itself we cannot accept the validity of the classical assumptions of the normative theory: (1) complete availability of information; (2) decision maker's global rationality; (3) clear and perfect statement of the problem. Instead we have to accept that the decision maker will be ambiguous, uncertain and inconsistent, that he does not know well what he needs, that it is not clear what others expect from him and how his behaviour is evaluated and, most important, that we have to help him exactly in this situation without eliminating or reducing these aspects, but trying to represent them and take them into account.

The effort made in this paper is to contribute to build a new theory about preference models and their operational use. For this purpose my assumption is that (see also [29]):

\- some of the decision aid activities can be represented under models of symbolic manipulation;

– therefore it is possible to identify an appropriate formalism that enables us to encode these activities and the knowledge about them.

Under this perspective I consider preference modeling as one of the activities that, to some extent, can be represented in a specific formalism. The question is: which is the appropriate one in the case we want to deny the validity of the traditional approach?

The basic idea is that preference modeling can be viewed as a reasoning process ([29]) and therefore formalisms enabling the representation of reasoning could be used. This choice should permit more flexibility, easier maintenance and introspection of the decision models even if it could appear less efficient than the traditional ones. Moreover by this approach it is possible to enhance the potentialities of the theory towards more complex decision situations. However not any kind of reasoning formalism could be appropriate and it is necessary to identify the one suitable to the peculiar features of the preference modeling process.

In the first section the problem is stated. In the second section a four valued logic is outlined as a basis for the theory. In the third section a new theory is developed about preference modeling based on the partial comparability approach (see [23]) supported by some examples. In the fourth section some possible operational uses of this theory are presented.

## 2. The problem

Let A be a finite set of m objects. A binary relation in the classical theory is a set S (subset of $A \times A$ ) such that $(s(x, y)$ stands for the sentence x is in relation s with y and $s^{-1}(x, y)$ stands for the sentence y is in relation s with x, the inverse of S):

$$
S = \{(x, y) | s (x, y) \text { is   true }, x, y, \in A \}
$$

$$
S ^ {f} = \{(x, y) | s (x, y) \text { is   false }, x, y, \in A \}
$$

$$
S ^ {- 1 t} = \left\{\left(x, y\right) \mid s (y, x) \quad \text { is   true }, \quad x, y, \in A \right\}
$$

$$
S ^ {- 1 f} = \{(x, y) \mid s (y, x) \text {   is   false }, x, y, \in A \}
$$

From now on we will use the notation $S^{t}$ instead of only S. Of course it is obvious that $S^{-1^{-1}t}=S^{t}$ and $S^{-1^{-1}f}=S^{f}$ . A binary relation may be (this is a partial list):

reflexive: $(x, x) \in S^t$ $\forall x \in A$

irreflexive: $(x, x) \in S^{f} \quad \forall x \in A$

symmetric: $(x, y) \in S^t \to (x, y) \in S^{-1t}$ ,

$$
\left(S ^ {t} = S ^ {- 1 t}\right) \quad \forall x, y \in A
$$

asymmetric: $(x, y) \in S^t \to (x, y) \in S^{-1f}$ ,

$$
\left(S ^ {t} \subset S ^ {- 1 f}\right) \quad \forall x, y \in A
$$

complete: $S^t\cup S^{-1t} = A\times A$

$$
\left(S ^ {f} \cap S ^ {- 1 f} = \emptyset\right) \quad \forall x, y \in A
$$

transitive: $(x, y) \in S^t \wedge (y, z) \in S^t$

$$
\rightarrow (x, z) \in S ^ {t} \quad \forall x, y, z \in A
$$

A preference structure is a triple $\langle P, I, R \rangle$ of relations such that:

$P$ is asymmetric $I$ is reflexive and symmetric $R$ is irreflexive and symmetric $P^{\prime}, I^{\prime}, R^{\prime}$ are two by two disjoint.

So if we characterize the preference structure by a binary relation S then: $S^{t}=P^{t}\cup I^{t}$ and you deduce:

$$
P ^ {t} = S ^ {t} \cap S ^ {- 1 f}
$$

$$
I ^ {t} = S ^ {t} \cap S ^ {- 1 t}
$$

$$
R ^ {t} = S ^ {f} \cap S ^ {- 1 f}
$$

Given to S some more properties, different orders can be identified. For instance if S is transitive and strongly complete then it is a weak order. In this case this theory becomes operationally interesting because there exists a real valued function $f \mid A \mapsto R$ such that the order can be represented by the function (for proofs see [9]):

$$
(x, y) \in S ^ {y} \Leftrightarrow f (x) \geqslant f (y)
$$

The demonstration of the theorem makes evident that this function always exists if the preference structure is complete ( $S^{f} \cap S^{-1f} = \emptyset$ ).

Hence in this theoretical frame we cannot give up complete comparability (and transitivity) without giving up also some of its quantitative potentialities offered. However as in real decision situations the assumptions of the theory may be very strong and unrealistic (as in the case of uncertainty and ambiguity) we may prefer to give up these axioms and try to verify if other theories can work. It will be necessary of course to change both our assumptions about preferences and the reasoning basis on which these relations are defined.

## 3. A "partial" logic for "partial" preferences

In the following I will try briefly to present a “new” logic on which preference modeling could be based. A detailed version of the logic is in [6] summarized in [7]. I do not argue that this is “the logic” (a normative approach), but that this is “a logic” that better represents the reasoning process of preference modeling (the interested readers can see [2], [3], [11], [27], [28]).

Classic logic is based on the assumption that any sentence can be evaluated with only two values: true (t) and false (f). Thus it is admitted that an objective world exists where each sentence has a unique truth value infinitely, that being true or false. I will not engage in the philosophical discussion about the existence of objective reality and so on, but it is reasonable to assume that there exist reasoning processes (like the ones where preferences are modeled) where the evaluations of the sentences are not objective but based on what we know and believe at any time of the process. So given a sentence p we may find ourselves (or better a reasoning device may find itself) in the following situations (read intuitively $\models p$ : as p can be believed):

(1) $p$ is true: $\models p$ and $\neq \neg p$

$$
(2) p \text {   is   false:   } \neq p \text {   and   } \vDash \neg p
$$

$$
(3) p \text {   is   unknown:   } \nvdash p \text {   and   } \nvdash \neg p
$$

$$
(4) p \text {   is   contradictory:   } \vDash p \text {   and   } \vDash \neg p
$$

In the first two cases one of the two sentences (p or $\neg p$ ) is believed and the other is not believed. We may say that in the first case p is “true” and in the second case p is “false”. In the third case nothing is believed therefore p can be evaluated “unknown” and in the fourth case both p and its negation are believed and the evaluation should be “contradictory”. Notice that in this last case it is not argued that p is both true and false (this is inconsistent), but that the knowledge and the beliefs in this moment are such that both p and $\neg p$ are believed.

This logic is based on the mathematical theory of lattices (see [2] and [3] and for a generalization [11]). It is possible to identify two lattices:

\- one where the truth values are ordered by information content, $(v_{i} \subseteq v_{j}$ : the truth value $v_{i}$ contains less information than the truth value $v_{j}$ . This is called the information lattice and its greatest lower bound (glb) is the value $u$ (nothing known) and its least upper bound (lub) is the value $k$ (too much is known);

\- the other is a lattice where the truth values are ordered by “truthness” and where the glb is the value f (definitely false) and its lub is the value t (definitely true).

So given a logical language $\mathcal{L}$ with the usual notation $(p, q, r, \ldots$ are propositions and $\vee, \wedge, \supset, \neg$ the connectives) we define an evaluation as a mapping $v \mid \mathcal{L} \mapsto V$ where $V = \{t, f, u, k\}$ . Given two propositions $p$ and $q$ we have:

$$
\begin{array}{l} v (\neg p) = \neg v (p) \\ v (p \land q) = v (p) \land v (q) \\ v (p \lor q) = v (p) \lor v (q) \end{array}
$$

with the following truth tables (they can be derived from the lattices).

<table><tr><td> $\wedge$ </td><td>u</td><td>f</td><td>t</td><td>k</td></tr><tr><td>u</td><td>u</td><td>f</td><td>u</td><td>f</td></tr><tr><td>f</td><td>f</td><td>f</td><td>f</td><td>f</td></tr><tr><td>t</td><td>u</td><td>f</td><td>t</td><td>k</td></tr><tr><td>k</td><td>f</td><td>f</td><td>k</td><td>k</td></tr></table>

![](/api/attachments/FN54PK4F/fulltext/images/e3fbca3f5cd3e17d8ca0da6cf54b9f9dbc3ce985226fa2ed8f2d0f5664faa2a5.jpg)

<table><tr><td>∨</td><td>u</td><td>f</td><td>t</td><td>k</td></tr><tr><td>u</td><td>u</td><td>u</td><td>t</td><td>t</td></tr><tr><td>f</td><td>u</td><td>f</td><td>t</td><td>k</td></tr><tr><td>t</td><td>t</td><td>t</td><td>t</td><td>t</td></tr><tr><td>k</td><td>t</td><td>k</td><td>t</td><td>k</td></tr></table>

The whole set of axioms of the propositional logic are also valid here with the exception of the so called “paradoxes of implication” ( $p \land \neg p \supset q$ and $p \supset q \lor \neg q$ ). The logic can be easily extended in the first order predicate calculus:

$$
\begin{array}{r l} & v ^ {A} \big (p \big (x _ {1}, \ldots , x _ {n} \big) \big) = t \quad \text {if} \\ & \Gamma \vDash_ {T} \big \langle x _ {1} ^ {A}, \ldots , x _ {n} ^ {A} \big \rangle \in P \quad \text {and} \\ & \Gamma \not \vDash_ {F} \big \langle x _ {1} ^ {A}, \ldots , x _ {n} ^ {A} \big \rangle \in P \\ & v ^ {A} \big (p \big (x _ {1}, \ldots , x _ {n} \big) \big) = f \quad \text {if} \\ & \Gamma \not \vDash_ {T} \big \langle x _ {1} ^ {A}, \ldots , x _ {n} ^ {A} \big \rangle \in P \quad \text {and} \\ & \Gamma \vDash_ {F} \big \langle x _ {1} ^ {A}, \ldots , x _ {n} ^ {A} \big \rangle \in P \\ & v ^ {A} \big (p \big (x _ {1}, \ldots , x _ {n} \big) \big) = u \quad \text {if} \\ & \Gamma \not \vDash_ {T} \big \langle x _ {1} ^ {A}, \ldots , x _ {n} ^ {A} \big \rangle \in P \quad \text {and} \\ & \Gamma \not \vDash_ {F} \big \langle x _ {1} ^ {A}, \ldots , x _ {n} ^ {A} \big \rangle \in P \\ & v ^ {A}) p (x _ {1}, \ldots , x _ {n}) = k \quad \text {if} \\ & \Gamma \vDash_ {T} \big \langle x _ {1} ^ {A}, \ldots , x _ {n} ^ {A} \big \rangle \in P \quad \text {and} \\ & \Gamma \vDash_ {F} \big \langle x _ {1} ^ {A}, \ldots , x _ {n} ^ {A} \big \rangle \in P) \end{array}
$$

where $p$ is an n-ary predicate symbol, $P$ is the corresponding n-ary relation, $x_{1},\ldots,x_{n}$ are the variables in the predicate, A is the structure where p varies, $v^{a}(\phi)$ is the valuation of $\phi$ in the structure A, $\Gamma$ is a set of premises and $(\Gamma\models_{T})$ should be read: the premises $\Gamma$ entail the predicate; $(\Gamma\models_{F})$ should be read: the premises $\Gamma$ entail the predicate negation.

I will try now to apply this logic so as to outline an axiomatic foundation to the partial comparability theory of Roy ([23]).

## 4. The new theory

Following the logic defined in the previous section and particularly the definitions in the predicate calculus case the theory can be outlined as follows. Given a set of premises $\Gamma$ and a set A of objects and a binary relation V we define (I will use the notation $V^{i}$ to represent the subset with the generic truth value $i(i \in \{t, f, u, k\})$ ):

$$
\begin{array}{c} V ^ {t} = \left\{(a, b) \mid \Gamma \vDash_ {T} (a, b) \in V \right. \\ \wedge \Gamma \not \vDash_ {F} (a, b) \in V, a, b \in A \} \end{array}
$$

In discursive way we can read: $V^{t}$ is the set of ordered couples $(a, b)$ in $A \times A$ such that the premises $\Gamma$ let us believe that $(a, b)$ is in the relation and does not let us believe that it is not in the relation. Now for the other truth values we have:

$$
\begin{array}{r l} & V ^ {f} = \left\{(a, b) \mid \varGamma \not \vDash_ {T} (a, b) \in V \right. \\ & \qquad \quad \land \varGamma \models_ {F} (a, b) \in V, a, b \in A \Big \} \\ & V ^ {u} = \left\{(a, b) \mid \varGamma \not \vDash_ {T} (a, b) \in V \right. \\ & \qquad \quad \land \varGamma \not \vDash_ {F} (a, b) \in V, a, b \in A \Big \} \\ & V ^ {k} = \left\{(a, b) \mid \varGamma \models_ {T} (a, b) \in V \right. \\ & \qquad \quad \land \varGamma \models_ {F} (a, b) \in V, a, b \in A \Big \} \end{array}
$$

With respect to the last definition let us give an example so that it appears clearer. Imagine that A represents a set of candidates and that the relation V represents the concept of “more suitable”. Suppose now that in a given moment of the evaluation all you know is that for a group of examiners (the premises) the candidate x is more suitable than the candidate y and for another group of examiners x is not more suitable than the candidate y and that no majority exists. Your conclusion is that the couple $(x, y)$ can be both in and out the relation “more suitable”. For the decision process where you are involved it is not important if definitely (objectively) x is more suitable than y, but how to handle the contradiction that exists. In fact further investigation may clarify the situation but it is not sure that you have the resources, the will or even the possibility of clarifying. However something has to be done. For the moment by this approach you have an explicit representation of the couples where contradiction holds (as for the other truth values of course).

Following the notation about the inverse relation we also have:

$$
\begin{array}{r l} & V ^ {- 1 t} = \left\{(a, b) \mid \Gamma \vDash_ {T} (b, a) \in V \right. \\ & \qquad \quad \wedge \Gamma \not \vDash_ {F} (b, a) \in V,   a,   b \in A \Big \} \\ & V ^ {- 1 f} = \left\{(a, b) \mid \Gamma \not \vDash_ {T} (b, a) \in V \right. \\ & \qquad \quad \wedge \Gamma \vDash_ {F} (b, a) \in V,   a,   b \in A \Big \} \\ & V ^ {- 1 u} = \left\{(a, b) \mid \Gamma \not \vDash_ {T} (b, a) \in V \right. \\ & \qquad \quad \wedge \Gamma \not \vDash_ {F} (b, a) \in V,   a,   b \in A \Big \} \\ & V ^ {- 1 k} = \left\{(a, b) \mid \Gamma \vDash_ {T} (b, a) \in V \right. \\ & \qquad \quad \wedge \Gamma \vDash_ {F} (b, a) \in V,   a,   b \in A \Big \} \end{array}
$$

Given two binary relations V and T we may define the operations of inclusion, intersection and union $((x, y) \in V^{i}$ stands for: x is in relation V with y with truth value i):

$$
\begin{array}{l} V ^ {i} \subset T ^ {j} \quad \text { iff } \quad (x, y) \in V ^ {i} \quad \text { implies } \\ (x, y) \in T ^ {i} \quad \forall x, y \in A \\ S ^ {l} = V ^ {i} \cup T ^ {j} \quad \text { iff } \quad (x, y) \in V ^ {i} \quad \text { or } \\ (x, y) \in T ^ {i} \quad \forall (x, y) \in S ^ {l} \\ S ^ {l} = V ^ {i} \cap T ^ {j} \quad \text { iff } \quad (x, y) \in V ^ {i} \quad \text { and } \\ (x, y) \in T ^ {i} \quad \forall (x, y) \in S ^ {l} \end{array}
$$

Given a binary relation V on A the following properties can be defined:

non contradictory: $\{V^u = V^k = \emptyset\}$

reflexive:

$$
(x, x) \in V ^ {t} \forall x \in A
$$

irreflexive:

$$
(x, x) \in V ^ {f} \forall x \in A
$$

asymmetric:

$$
V ^ {t} \subseteq V ^ {- 1 f} \forall x, y \in A
$$

symmetric:

$$
V ^ {t} = V ^ {- 1 t} \forall x, y \in A
$$

complete:

$$
V ^ {t} \cup V ^ {k} \cup V ^ {- 1 t} \cup V ^ {- 1 k}
$$

$$
= A \times A
$$

transitive:

$$
(x, y) \in V ^ {t} \wedge (y, z) \in V ^ {t}
$$

$$
\rightarrow (x, z) \in V ^ {\prime} \forall x, y, z \in A
$$

A preference structure S will be now defined as a quadruple $\langle P, Q, I, R \rangle$ of relations such that:

$P, Q, I, R$ are non contradictory; $P, Q$ are asymmetric; $I, R$ are symmetric; $I$ is reflexive; $R$ is irreflexive; $P^t, Q^t, I^t, R^t$ are two by two disjoint (their intersection is empty); $P^t \cap Q^{-1t} = \emptyset$ ; $Q^t \cap P^{-1t} = \emptyset$ ;

This preference structure can be characterized by a preference relation S defined as follows:

$$
\begin{array}{l} S ^ {t} = P ^ {t} \cup I ^ {t} \\ S ^ {k} = Q ^ {t} \cup I ^ {t} \\ S ^ {u} \cup S ^ {f} = P ^ {- 1 t} \cup Q ^ {- 1 t} \cup R ^ {t} = P ^ {f} \cap Q ^ {f} \cap I ^ {f} \end{array}
$$

From these definitions we can now demonstrate that (for the proofs see appendix A):

$$
\begin{array}{l} P ^ {t} = S ^ {t} \cap (S ^ {- 1 u} \cup S ^ {- 1 f}) \\ Q ^ {t} = S ^ {k} \cap (S ^ {- 1 u} \cup S ^ {- 1 f}) \\ I ^ {t} = (S ^ {t} \cup S ^ {k}) \cap (S ^ {- 1 t} \cup S ^ {- 1 k}) \\ R ^ {t} = (S ^ {j} \cup S ^ {u}) \cap (S ^ {- 1 f} \cup S ^ {- 1 u}) \end{array}
$$

Conceiving the relation S as “it can be evaluated not worse than”, the relations that are derived can be seen as the four fundamental relations introduced by Roy ([23]). P is the “strict preference” (there is strong evidence about the preference), I is the “indifference” (there is strong evidence for an equivalent evaluation), Q is the “weak preference” (there is no strong evidence for preference), R is the “incomparability” (there is no strong evidence for any of the other relations). In appendix B the complete definitions of the four relations are given in table 4. We may call S an outranking relation (see[19]). S is reflexive, but it is neither complete nor asymmetric, hence it is not transitive. It can be complete and in this case $R' = \emptyset$ . In Figure 1 we give a graphical representation where the different relations and their properties are evident. The table represents the space defined by $A \times A$ and each block is part of one of the subsets represented by $P^{t}$ , $Q^{t}$ , etc..

<table><tr><td> $A \times A$ </td><td> $S^{-1t}$ </td><td> $S^{-1f}$ </td><td> $S^{-1u}$ </td><td> $S^{-1k}$ </td></tr><tr><td> $S^{t}$ </td><td> $I^{t}$ </td><td> $P^{t}$ </td><td> $P^{t}$ </td><td> $I^{t}$ </td></tr><tr><td> $S^{f}$ </td><td> $P^{-1t}$ </td><td> $R^{t}$ </td><td> $R^{t}$ </td><td> $Q^{-1t}$ </td></tr><tr><td> $S^{u}$ </td><td> $P^{-1t}$ </td><td> $R^{t}$ </td><td> $R^{t}$ </td><td> $Q^{-1t}$ </td></tr><tr><td> $S^{k}$ </td><td> $I^{t}$ </td><td> $Q^{t}$ </td><td> $Q^{t}$ </td><td> $I^{t}$ </td></tr></table>

Fig. 1. the space $A \times A$ and the outranking relation.

Table 3

<table><tr><td> $A \times A$ </td><td> $S^{-1t}$ </td><td> $S^{-1f}$ </td></tr><tr><td> $S^{t}$ </td><td> $I^{t}$ </td><td> $P^{t}$ </td></tr><tr><td> $S^{f}$ </td><td> $P^{-1t}$ </td><td> $R^{t}$ </td></tr></table>

Fig. 2. the space $A \times A$ and the conventional preference relations.

We can make a convention so as to represent S as a graph where the nodes are the elements of the set A and the edges have the following meaning: if between a and $b(a, b \in A)$ there exists a directed arc from a to b then $(a, b) \in S^{t} \cup S^{k}$ ; if it does not exist then $(a, b) \in S^{u} \cup S^{f}$ . In other words we have an edge between a and b if one of the $P^{t}, Q^{t}, I^{t}$ has been verified.

A final observation. The conventional preference theory can be derived from this approach giving to the characteristic relation of the preference structure S some more properties. If $S^{u} = S^{k} = S^{-1u} = S^{-1k} = \emptyset$ the space $A \times A$ is reduced as in Figure 2. Only the two classical preference relations hold: preference or indifference (provided that S is complete) and all the theorems about preference modeling are still valid.

## 5. Possible operational directions

So what? A theory is developed, but how does it work? Given a real decision situation how you use this theory in an operational way? If the “outranking relation” is not complete and transitive what about the existence of a function preserving the relation?

First of all it should be said that outranking relations are now used in widely distributed commercial packages implementing well known methods as Electre, Promethe etc.. Nevertheless it is appealing and important to understand the operational directions of this theory now that an axiomatic basis is available. But let me first give an example (remember that you do not look for the optimal solution, but for a satisfying one).

Suppose now that you are involved in a decision process where a candidate has to be chosen for a post. There are five candidates $\{a, b, c, d, e\}$ and a very conflictual board of examiners.

Table 1  
Pairwise comparison of the candidates using relation $S$

<table><tr><td>S</td><td>a</td><td>b</td><td>c</td><td>d</td><td>e</td></tr><tr><td>a</td><td>t</td><td>t</td><td>t</td><td>u</td><td>k</td></tr><tr><td>b</td><td>t</td><td>t</td><td>k</td><td>u</td><td>f</td></tr><tr><td>c</td><td>u</td><td>u</td><td>t</td><td>k</td><td>f</td></tr><tr><td>d</td><td>k</td><td>t</td><td>u</td><td>t</td><td>t</td></tr><tr><td>e</td><td>k</td><td>f</td><td>t</td><td>f</td><td>t</td></tr></table>

Table 2  
The preference relations

<table><tr><td> $A \times A$ </td><td> $a$ </td><td> $b$ </td><td> $c$ </td><td> $d$ </td><td> $e$ </td></tr><tr><td> $a$ </td><td> $I^{t}$ </td><td> $I^{t}$ </td><td> $P^{t}$ </td><td> $Q^{f}$ </td><td> $I^{t}$ </td></tr><tr><td> $b$ </td><td> $I^{t}$ </td><td> $I^{t}$ </td><td> $Q^{t}$ </td><td> $Q^{f}$ </td><td> $R^{t}$ </td></tr><tr><td> $c$ </td><td> $P^{f}$ </td><td> $Q^{f}$ </td><td> $I^{t}$ </td><td> $Q^{t}$ </td><td> $P^{f}$ </td></tr><tr><td> $d$ </td><td> $Q^{t}$ </td><td> $Q^{t}$ </td><td> $Q^{f}$ </td><td> $I^{t}$ </td><td> $P^{t}$ </td></tr><tr><td> $e$ </td><td> $I^{t}$ </td><td> $R^{t}$ </td><td> $P^{t}$ </td><td> $P^{f}$ </td><td> $I^{t}$ </td></tr></table>

Given a relation S (“it can be evaluated not worse than”) Table 1 has to be examined. This table may be seen as the result of aggregating the partial preferences expressed by each examiner for each couple of candidates. In each block the truth value of the relation S is reported. You are asked to help to identify a final prescription about the candidate to choose.

There are two inferences that you can make about the candidates. The first is to identify the kind of preference relation that holds for each couple of them. The results can be seen in Table 2. The other is the graph representation (Table 3: 1 represents the presence of an arc, $S^{t} \cup S^{k}$ ; 0 represents the absence of an arc, $S^{u} \cup S^{f}$ . It is easy to observe that in this graph there are present a lot of intransitive situations ( $\{c, d, e\}$ , $\{a, c, d\}$ , $\{b, c, d\}$ are all circuits).

The graph representation

<table><tr><td> $S^{t} \cup S^{k}$ </td><td>a</td><td>b</td><td>c</td><td>d</td><td>e</td></tr><tr><td>a</td><td>1</td><td>1</td><td>1</td><td>0</td><td>1</td></tr><tr><td>b</td><td>1</td><td>1</td><td>1</td><td>0</td><td>0</td></tr><tr><td>c</td><td>0</td><td>0</td><td>1</td><td>1</td><td>0</td></tr><tr><td>d</td><td>1</td><td>1</td><td>0</td><td>1</td><td>1</td></tr><tr><td>e</td><td>1</td><td>0</td><td>1</td><td>0</td><td>1</td></tr></table>

There exist different conflict resolution techniques. You may choose the one of identifying the dominating subset $E^{d}$ (see [30]). In this case you look for the minimal subset whose elements, jointly, outrank all the other elements of the set A.

$$
\begin{array}{l} E ^ {d} = \min (E ^ {1}, \dots , E ^ {i}, \dots , E ^ {m}) \\ E ^ {i} = \left\{a \in A \mid \nexists b: a (S ^ {f} \cup s ^ {u}) b, b \in A \right\} \end{array}
$$

Applying this rule in the example you have two dominating subsets: $E^{d1} = \{a, d\}$ and $E^{d2} = \{a, c\}$ . However one of the two has to be chosen. We can now apply a new heuristic rule that chooses, among the dominating subsets, the one with the weaker relation among its objects. In this case the subset $\{a, d\}$ will be chosen due to the “weak preference relation” between a and d, while between a and c a “strict preference” relation holds. Intuitively you can say that it is easier for the board of examiners to accept as equiparable a and d rather than a and c. A complete ranking of successive dominated subsets will give us:

$$
\{a, d \} > \{b, e \} > \{c \}
$$

What is your prescription? The safest one is to suggest some further investigation limited to the candidates a and d. If absolutely something has to be decided now, then choose the candidate d as it is weakly preferred to a.

As is evident from the example, it is possible now to work in two levels, one where the outranking relation is used and the other where the disaggregated information is used. More interesting rules can be built of course depending on the problem faced. Let me discuss now what could generally be the possible operational use of this theory.

1. The existence of four basic preference relations allows you to take into account more complex situations and handle decision procedures where intransitivities and incomparabilities may appear. If you want to introduce in your preference structures lexicographic orders, general non compensatory methods, veto situations, different kinds of majority rules and you want to be able to handle the contradictions that inevitably will arise, then you need a more flexible representation and this can be one. More precisely I suggest that is easier to: – put in evidence the different importance that different criteria may have in multicriteria decision aid procedures when a non compensatory approach is used (see Roy, 1990b);

\- build heuristic rules for the construction of the final prescription;

\- explain the results to the decision maker.

2. The kind of logic we used suggests some other directions too. As an axiomatization for this theory is available based on a sound and complete logic, a reasoning device can be created that implements it. This could be ineffective from a computational point of view, but it could allow a declarative representation of the relation S without looking at any cost for a mathematical representation, the latter being difficult if not impossible. The more interesting direction however is another. If I have a reasoning device I can now build a non monotonic reasoning device, that allows the maintenance of the results of the preference modeling process as new information or knowledge become available. A non monotonic reasoning formalism is supposed to allow you to update the truth value of a formula as new facts are added to your premises set $\Gamma$ (this is impossible in classical monotonic logic). See for an introduction [32] and for the state of the art [16]. For instance a Truth Maintenance System ([8]) could control the deductions and update them to any kind of modification in which the premises set $\Gamma$ may occur without withdrawing the whole set of conclusions. For interactive multicriteria methods this should be an important improvement as it could enable you to enhance the “learning” features they have.

## 6. Conclusions

Decision situations can be so complex as to induce us to give up the classical preference modeling theory because it could lead us to shortcomings and unrealistic prescriptions. In this case more flexible and qualitative approaches are needed and the partial comparability approach could be useful as it introduces more realistic preference situations. The problem is that this approach lacks a precise axiomatic foundation and has to legitimate its operational potentialities empirically.

In the paper an axiomatic foundation is outlined based on a well known four valued logic where the truth values of “unknown” and “contradictory” are introduced. This logic is known to be sound and complete. Using the first order predicate calculus of this logic, for any binary relation four possible truth values are possible. The usual properties of binary relations are defined.

A preference structure S is now defined as a quadruple $\langle P, Q, I, R \rangle$ of binary relations with some specific properties. Assuming a binary relation S that characterizes the preference structure, the four preference relations are defined on the basis of S. An axiomatization is thus provided for the partial comparability theory being P the strict preference relation, Q the weak preference relation, I the indifference relation and R the incomparability relation. We may call S an outranking relation. The traditional preference modeling theory becomes a specific case of this new axiomatization.

Finally the operational perspectives are discussed in two directions: make easier the solution of traditional problems in the multicriteria decision aid field mainly in the use of non compensatory methods, the construction of the final prescription and the explanation of the results; enabling the building of reasoning devices that implement decision aid procedures using outranking relations without specifying a mathematical representation. Moreover non monotonic reasoning devices could be used to update the results without giving up the whole set of conclusions.

## Acknowledgements

This paper was worked out while I was visiting the Linköping University in Sweden. I have to thank Dimiter Driankov and Patrick Doherty for some very important suggestions they gave me and for having pushed me to be more correct.

## References

[1] G. Balestra, A. Tsoukiàs, (1990), “Multicriteria Analysis Represented by Artificial Intelligence Techniques”, in

Journal of the Operational Research Society, vol. 41, 419–430.

[2] N.D. Belnap, (1976), “How a computer should think”, Proceedings of the Oxford International Symposium on Contemporary Aspects of Philosophy, Oxford, England, 30–56.

[3] N.D. Belnap, (1977), “A useful four-valued logic”, in G. Epstein, J. Dumm, (eds.), Modern uses of multiple valued logics, D. Reidel, Dordrecht, 8–37.

[4] D. Bouyssou, (1984), “Approaches descriptives et constructives d’aide à la Décision: Fondements et comparaisons”, Thèse de 3me cycle, Université Paris-Dauphine, Paris.

[5] D. Bouyssou, (1989), “Building Criteria: a prerequisite for MCDA”, in C.A. Bana e Costa (ed.), Readings in Multiple Criteria Decision Aid, Springer Verlag, Berlin, 58–80.

[6] P. Doherty, D. Driankov, A. Tsoukiàs, “Partiality, Para-Consistency and Preference Modeling”, IDA research report Lith-IDA-R-92-18, Linköping University, 1992.

[7] P. Doherty, D. Driankov, A. Tsoukiàs, “Partial Logics and Partial Preferences”, Proceedings of the CEMIT 92 international conference, Tokyo, 525–528, 1992.

[8] J. Doyle, (1979), “A Truth Maintenance System”, Artificial Intelligence, vol. 12, 231–272.

[9] P.C. Fishburn, (1970), Utility theory for decision making, J. Wiley and sons, New York.

[10] P.C. Fishburn, (1989), “Foundations of Decision Analysis: Along the way”, Management Science, vol. 35., 387–405.

[11] M.L. Ginsberg, (1988), “Multivalued logics: a uniform approach to reasoning in artificial intelligence”, Computational Intelligence, vol. 4, 265–316.

[12] O. Huber, (1979), “Non transitive multidimensional preferences: theoretical analysis of a model”, Theory and Decision, vol. 10., 147–165.

[13] J. Kacprzyk, M. Roubens, (eds.), (1988), Non Conventional Preference Relations in Decision Making, LNEMS N. 301, Springer Verlag, Berlin.

[14] D. Kahneman, A. Tversky, (1979), “Prospect theory: an analysis of decision under risk”, Econometrica, vol. 47, 263–291.

[15] R.L. Keeney, H. Raiffa, (1976), Decisions with Multiple Objectives: Preferences and value Tradeoffs, J. Wiley, New York.

[16] W. Lukaszewicz, (1990), Non-monotonic reasoning, Ellis Horwood Ltd., New York.

[17] J. Moscarola, (1984), “Organizational Decision Processes and ORASA intervention”, in R. Tomlinson, J. Kiss, (eds.), Rethinking the process of Operational Research and Systems Analysis, Pergamon Press, Oxford, 169–186.

[18] M.F. Norese, A. Ostanello, (1988), “Decision aid process typologies and operational tools”, Proceedings of the AIRO conference, Centro Ricerche IBM, Pisa, 661–680.

[19] A. Ostanello, (1985), “Outranking relations”, in G. Fandel, J. Spronk, eds., Multiple Criteria Decision Methods and Applications, Springer Verlag, Berlin, 41–60.

[20] M. Roubens, Ph. Vincke, (1985), Preference Modeling, Springer Verlag, Berlin.

[21] B. Roy, (1975), “Vers une méthodologie générale de l’aide à la décision”, Revue METRA, vol. 14, 459–497.

[22] B. Roy, (1977), “Partial Preference Analysis and Decision Aid: The fuzzy outranking relation concept”, in D.E. Bell, R.L. Keeney, H. Raiffa, (eds.), Conflicting objectives in Decisions, J. Wiley, New York, 40–75.

[23] B. Roy, (1985), Méthodologie multicritère d'aide à la décision, Economica, Paris,

[24] B., Roy, (1990a), “Decision aid and decision making”, European Journal of Operational Research, vol. 45, 324–331.

[25] B. Roy, (1990b), “Sur la notion d’importance des critères et sa prise en compte formelle en aide multicritère à la décision”, presented at the 32nd meeting of the EURO Group on MCDA, Stuttgart, Germany.

[26] B. Roy, Ph. Vincke, (1984), “Relational systems of preferences with one or more pseudo-criteria: some new concepts and results”, Management Science, vol. 30, 1323–1335.

[27] E. Sandewall, (1985), “A functional approach to non-monotonic logic”, Proceedings of the 9th International Joint Conference on Artificial Intelligence, Los Angeles, 100–106.

[28] D. Scott, (1982), “Some ordered sets in computer science”, in I. Rival, (ed.), Ordered Sets, D. Reidel, Dordrecht, 677–718.

[29] A. Tsoukiàs, (1991), “Preference Modeling as a Reasoning Process. A new way to face Uncertainty in MCDSS”, European Journal of Operational Research, vol. 55, 309–318.

[30] D. Vanderpooten, (1989) “The Construction of Prescriptions in Outranking Methods”, in C.A. Bana e Costa (ed.), Readings in Multiple Criteria Decision Aid, Springer Verlag, Berlin, 184–215.

[31] G.R. Widmeyer, (1990), “Reasoning with Preferences and Values”, Decision Support Systems, vol. 6, 183–191.

[32] T. Winograd, (1980), “Extended Inference Models in Reasoning by Computer Systems”, Artificial Intelligence, vol. 13, 5–26.

Appendix A

$$
\begin{array}{r l} & 1. P ^ {t} = S ^ {t} \cap (S ^ {- 1 f} \cup S ^ {- 1 u}) \\ & S ^ {t} \cap (S ^ {- 1 f} \cup S ^ {- 1 u}) \\ & \quad = (P ^ {t} \cup I ^ {t}) \cap (P ^ {t} \cup Q ^ {t}) \cup R ^ {t}) \\ & \quad = (P ^ {t} \cap P ^ {t}) \cup (P ^ {t} \cap Q ^ {t}) \cup (P ^ {t} \cap R ^ {t}) \\ & \quad \cup (I ^ {t} \cap P ^ {t}) \cup (I ^ {t} \cap Q ^ {t}) \cup (I ^ {t} \cap R ^ {t}) \end{array}\tag{1}
$$

but:

$$
\begin{array}{l} \left(P ^ {t} \cap P ^ {t}\right) = P ^ {t}, \left(P ^ {t} \cap Q ^ {t}\right) = \emptyset , \left(P ^ {t} \cap R ^ {t}\right) = \emptyset , \\ \left(I ^ {t} \cap P ^ {t}\right) = \emptyset \left(I ^ {t} \cap Q ^ {t}\right) = \emptyset , \left(I ^ {t} \cap R ^ {t}\right) = \emptyset \end{array}
$$

hence the whole expression (1) is equal to $\mathbf{P}^{\mathrm{t}}$ . (Q.E.D.)

$$
2. Q ^ {t} = S ^ {k} \cap (S ^ {- 1 f} \cup S ^ {- 1 u})
$$

$$
\begin{array}{r l} S ^ {k} \cap (S ^ {- 1 f} \cup S ^ {- 1 u}) & \\ = (Q ^ {t} \cup I ^ {t}) \cap (P ^ {t} \cup Q ^ {t}) \cup R ^ {t}) & \\ = (Q ^ {t} \cap P ^ {t}) \cup (Q ^ {t} \cap Q ^ {t}) \cup (Q ^ {t} \cap R ^ {t}) & \\ \cup (I ^ {t} \cap P ^ {t}) \cup (I ^ {t} \cap Q ^ {t}) \cup (I ^ {t} \cap R ^ {t}) \end{array}\tag{2}
$$

but:

$$
\begin{array}{l} \left(Q ^ {t} \cap Q ^ {t}\right) = Q ^ {t}, \left(Q ^ {t} \cap P ^ {t}\right) = \emptyset , \left(Q ^ {t} \cap R ^ {t}\right) = \emptyset , \\ \left(I ^ {t} \cap P ^ {t}\right) = \emptyset \left(I ^ {t} \cap Q ^ {t}\right) = \emptyset , \left(I ^ {t} \cap R ^ {t}\right) = \emptyset \end{array}
$$

hence the whole expression (2) is equal to $\mathbf{Q}^{\mathrm{t}}$ . (Q.E.D.)

$$
I ^ {t} = (S ^ {t} \cup S ^ {k}) \cap (S ^ {- 1 t} \cup S ^ {- 1 k})
$$

$$
\begin{array}{l} \left(S ^ {t} \cup S ^ {k}\right) \cap \left(S ^ {- 1 t} \cup S ^ {- 1 k}\right) \\ = \left(S ^ {t} \cap S ^ {- 1 t}\right) \cup \left(S ^ {t} \cap S ^ {- 1 k}\right) \\ \cup \left(S ^ {k} \cap S ^ {- 1 t}\right) \cup \left(S ^ {k} \cup S ^ {- 1 k}\right) \\ = \left(\left(P ^ {t} \cup I ^ {t}\right) \cap \left(P ^ {- 1 t} \cup I ^ {- 1 t}\right)\right) \\ \cup \left(\left(P ^ {t} \cup I ^ {t}\right) \cap \left(Q ^ {- 1 t} \cup I ^ {- 1 t}\right)\right) \\ \cup \left(\left(Q ^ {t} \cup I ^ {t}\right) \cap \left(P ^ {- 1 t} \cup I ^ {- 1 t}\right)\right) \\ \cup \left(\left(Q ^ {t} \cup I ^ {t}\right) \cap \left(Q ^ {- 1 t} \cup I ^ {- 1 t}\right)\right) \\ = \left(P ^ {t} \cap P ^ {- 1 t}\right) \cup \left(P ^ {t} \cap I ^ {- 1 t}\right) \cup \left(I ^ {t} \cap P ^ {- 1 t}\right) \\ \cup \left(I ^ {t} \cap I ^ {- 1 t}\right) \cup \left(P ^ {t} \cap Q ^ {- 1 t}\right) \cup \left(P ^ {t} \cap I ^ {- 1 t}\right) \\ \cup \left(I ^ {t} \cap Q ^ {- 1 t}\right) \cup \left(I ^ {t} \cap I ^ {- 1 t}\right) \cup \left(Q ^ {t} \cap I ^ {- 1 t}\right) \\ \cup \left(Q ^ {t} \cap P ^ {- 1 t}\right) \cup \left(I ^ {t} \cap I ^ {- 1 t}\right) \cup \left(I ^ {t} \cap P ^ {- 1 t}\right) \\ \cup \left(Q ^ {t} \cap Q ^ {- 1 t}\right) \cup \left(Q ^ {t} \cap I ^ {- 1 t}\right) \\ \cup \left(I ^ {t} \cap Q ^ {- 1 t}\right) \cup \left(I ^ {t} \cap I ^ {- 1 t}\right) \end{array} (3
$$

but:

$(I^t \cap I^{-1t}) = I^t$ , and all the other couples are equal to the $\emptyset$ hence the whole expression (3) is equal to $I^t$ . (Q.E.D.)

$$
\begin{array}{l} 4. R ^ {t} = (S ^ {f} \cup S ^ {u}) \cap (S ^ {- 1 f} \cup S ^ {- 1 u}) \\ (S ^ {u} \cup S ^ {f}) \cap (S ^ {- 1 u} \cup S ^ {- 1 f}) \\ \quad = (P ^ {- 1 t} \cup Q ^ {- 1 t} \cup I ^ {- 1 t}) \cap (P ^ {t} \cup Q ^ {t} \cup R ^ {t}) \\ \quad = (P ^ {t} \cap P ^ {- 1 t}) \cup (P ^ {t} \cap Q ^ {- 1 t}) \cup (P ^ {t} \cap R ^ {t}) \\ \quad \cup (Q ^ {t} \cap P ^ {- 1 t}) \cup (Q ^ {t} \cap Q ^ {- 1 t}) \cup (Q ^ {t} \cap R ^ {t}) \\ \quad \cup (R ^ {t} \cap P ^ {- 1 t}) \cup (R ^ {t} \cap Q ^ {- 1 t}) \cup (R ^ {t} \cap R ^ {t}) \end{array}\tag{4}
$$

but:

$(R^{t} \cap R^{t}) = R^{t}$ , and all the other couples are equal to the $\emptyset$ hence the whole expression (4) is equal to $R^{t}$ .
(Q.E.D.)

## Appendix B

Table 4  
Fundamental Preference Relations (quoted from Roy and Vincke, 1984)

<table><tr><td>Relation</td><td>Definition</td></tr><tr><td>Indifference</td><td>Two actions are indifferent in the sense that there exist clear and positive reasons to choose equivalence.</td></tr><tr><td>Strict preference</td><td>There exist clear and positive reasons to justify that one (well specified) of the two actions is significantly preferred to the other.</td></tr><tr><td>Weak preference</td><td>One (well specified) of the two actions is not strictly preferred to the other but it is impossible to say if the other is strictly preferred or indifferent to the first one.</td></tr><tr><td>Incomparability</td><td>Two actions are not comparable in the sense that none of the above three situations predominates</td></tr></table>
