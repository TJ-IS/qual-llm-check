---
otero_id: 17516
otero_key: "PEHTCBXY"
title: "Intelligent inference systems based on influence diagrams"
authors: "H.W. Gottinger; H.P. Weimann"
year: "1995"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(94)00049-x"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Intelligent inference systems based on influence diagrams

H.W. Gottinger $^{a,*}$ , H.P. Weimann $^{b}$

$^{a}$ Institute of Management Science, University of Maastricht, P.O. Box 591, NL 6200 Maastricht, The Netherlands $^{b}$ Industrieanlagen-Betriebsgesellschaft (IABG), Metzlerstraße 21, D-60594 Frankfurt, Germany

## Abstract

This paper explores various inference techniques for an intelligent decision support system based on influence diagrams. Rule-based expert systems for decision support have been successful for well-structured, well understood decision situations of a taxonomic classification type. As uncertainty is prevalent, information costly and payoff relevant, and the preferred solution depends on the specific beliefs and preferences of an individual or group decision maker the resolution methods of decision theory embodied in first-order predicate logic forms a natural basis for computerized intelligent decision support. Based on a unified characterization of knowledge inference procedures for logical probabilistic and decision theoretic reasoning are described in detail.

Keywords: Influence diagrams; Intelligent decision support systems; Probabilistic reasoning; Decision theoretic reasoning; Logical reasoning; Artificial intelligence

## 1. Introduction

An intelligent decision support system (IDSS) is a computer-based interactive tool of decision making for well-structured decision and planning situations that uses jointly decision theoretic methods and artificial intelligence-based techniques. Depending on the level of uncertainty, complexity, and novelty of a decision situation, reasoning about action requires various levels of representation and inference. In pursuing previous work [6] on this paper integrates artificial intelligence-based techniques, logic-based approaches of problem solving with techniques for probabilistic analysis and decision making under uncertainty from operations research and management science to develop methods for improving the quality of decision making [11]. Two major results in intelligent decision support are the design of a representation to describe the important elements of a decision domain, and the construction of inference techniques which can draw conclusions regarding the decision domain.

Representation: A formal declarative language has been developed based on first-order logic for the description of states, alternatives, beliefs, and preferences associated with a decision domain and decision maker [6]. The language includes constructs to explicitly enumerate the alternative possible outcomes for uncertain propositions, probability distributions over these outcomes, the choices facing the decision maker, and his preferences regarding alternative outcomes of differing likelihood's. The concept of a logic rule has been generalized to allow for the expression of conditional probabilities and information availability.

Inference: Various deductive inference techniques for reasoning using the first order domain representation have been specified and implemented. The techniques include methods for examining the many possible states attainable from a given state, methods implementing probabilistic reasoning based on conditional and joint probability distributions for various outcomes, and methods for reasoning about and construction of decision theoretic models providing decision recommendations. The techniques integrate deterministic, logical methods with probabilistic and decision-theoretic reasoning, allowing the system to select or combine the technique with the appropriate power and flexibility to solve a given problem. In this context, probability is used exclusively as a measure of uncertainty. Though the representation of uncertainty remains a topic of considerable controversy in the AI community, the selection of probability is necessitated by a focus on decision making and the desire to reason about uncertainty and decision directly, as compared to non-decision theoretic alternative calculi of Dempster-Shafer theory and related approaches [19].

Recent advances in representation and inference under uncertainty for artificial intelligence have stressed the utility of network representations ([14,18,8]). The foremost probabilistic representations include influence diagrams, developed by decision analysts ([12,10,15]) and a related formalism, Bayes network [13]. An analogue to the local computational model of Pearl based on belief functions has also been developed [17]. Though there appears to be some agreement on graphical depiction's of probabilistic dependencies for artificial intelligence applications, much less attention has been devoted to the generation or construction of these structures. Rather, most researchers focus on the procedures for propagating information and manipulating structures for given diagram ([14,16,18]). Proof procedures developed in this paper emphasize reasoning about the structure of a probabilistic or decision theoretic model as opposed to reasoning with a given model. Given a query, the basic idea is to produce a logical proof if possible. If not possible, a probabilistic network based on the query and the knowledge of the decision domain is produced and subsequently solved. The control structure serves to minimize the size of a probabilistic or decision theoretic model. The approach developed here has the following advantages over previous approaches:

\- Probabilistic reasoning can be gracefully integrated with logical, deterministic inference. This methodology allows one to consistently invoke the appropriate richness of representation for different problems.

\- The expressiveness of the language does not impose assumptions of conditional independence on the probabilistic representation. The knowledge base expresses the set of dependencies and independence's made explicit by the system builder and/or decision maker.

\- By formulating logical, probabilistic, and decision-theoretic inference within an integrating framework, techniques of explanation and heuristic search can be applied to the construction of models.

\- Through the dynamic construction of models in response to queries and changes in the state of information in the knowledge base, only those portions of the knowledge base needed to address a particular issue are incorporated in a given probabilistic representation.

\- The approach is capable of constructing multiple models for the same phenomena, thus enabling reasoning about the performance and results of different models within the same environment.

An ever increasing substantial literature covers such ([9,4,2]).

Inference is the process of generating new conclusions from existing knowledge. In a previous work [6], we defined a representation language for decision domains based on propositions and well-formed logical, probabilistic, and informational influences. In this paper, we discuss the use and manipulation of sentences in this language. Sentences in the language are a knowledge base describing the decision domain, including the beliefs, alternatives, and preferences of the decision maker. We describes deductive inference procedures which provide logical, probabilistic, and decision-theoretic conclusions from a set of well-formed influences. This is the process of deducing new facts, probability distributions, expectations, or decision recommendations from a given declarative representation of a decision domain. For probabilistic and decision-theoretic reasoning, we use the declarative, first-order representation to construct a prepositional (no quantified variables) influence diagram. The influence diagram is then manipulated to provide the answers to probabilistic and decision-theoretic queries. The emphasis therefore, focuses on the dynamic, knowledge-based construction of a probabilistic or decision model (i.e. the influence diagram) and on reasoning about the structure and extent of such a model [5].

The process description is as follows. The declarative domain description is a set of sentences in the decision language. Some of the sentences refer to the proposition A. Given a query about A, the influence diagram theorem prover attempts to construct an influence diagram which has A as its root using the declarative domain description. If a diagram can be constructed, then the influence diagram solver is invoked, using the influence diagram which is the result of the proof to answer the query. In previous work we described in detail the operations of the influence diagram theorem prover in constructing and manipulating the influence diagrams.

We now develop a set of inference techniques that, in concert, allow a very general form of reasoning about decision situations, which builds up the influence diagram solver. Take the three levels of knowledge we can represent about a proposition -absolute belief about the truth or falsity of a proposition, an assertion that one of a set of alternative outcomes for the proposition is true, and finally the assignment of a measure of uncertainty over those alternative outcomes. In the following sections we develop techniques to infer this knowledge from the propositions and influences in a knowledge base. We start with a review of logical inference, and then build on the ideas of automated logic theorem proving (logic programming) to develop methods for generating the set of alternative outcomes for a proposition and to generate a measure of uncertainty over the alternatives (either an expectation or a probability distribution). Finally, all the inference techniques presented are combined to provide a method for developing full decision models from the first-order description.

Implicit in these inference methods is a control strategy for construction of probabilistic, alternative outcome, and decision-theoretic models. The control is based on the selection of a particular type of reasoning mechanism over another in developing a model. In all the methods developed here, the implicit control is founded on the principle of minimizing uncertain representations, i.e. those representations in which an array of possible outcomes must be explicitly considered. This is achieved by always attempting to perform a deterministic inference procedure on a goal first –if we can make a strong statement about the outcome of a proposition, then it is used, as opposed expending the effort to construct and use a larger and computationally expensive representation. We will discuss the issues of control and consistency in the search for probabilistic models, as well as combination of information when multiple models are deducible from a given declarative description.

## 2. Logical inference

The main purpose of a logic inference procedure is to compute bindings. Given a query of the form (Q x) we wish to find a single value or set of values (the bindings) for x such that (Q x) is true. The basic procedure is to define an initial goal $G_{0}$ corresponding to the query, in this case (Q x). The proof procedure is based on deriving a series of new goals $G_{i}$ from previous goals until an empty goal set is achieved. The procedure, related to the idea of proof by contradiction and resolution theorem proving, proceeds according to an SLD-resolution proof procedure. The SLD-resolution procedure is complete for Horn clauses (i.e. logical influences). This means that if a Horn clause is logically implied by a set of Horn clauses, then there is a successful SLD-resolution procedure with that clause as the initial goal [3].

Let $G_{i}$ be a conjunction of the form $P_{1} \wedge P_{2} \wedge ..P_{k} \wedge ..... \wedge P_{m}$ where the $P_{k}$ are atomic propositions. Select some $P_{k}$ as a subgoal. $G_{i+1}$ is derived from $G_{i}$ if one of the following conditions holds:

Condition (i). There exists an influence of the form $\mathbf{A} \to \mathbf{B}$ , where $\mathbf{B}$ is a conjunction of atomic propositions of the form $\mathbf{Q}_1 \wedge \mathbf{Q}_2 \wedge .. \wedge \mathbf{Q}_n$ and a facts substitution, $\theta_{i+1}$ , such that $\mathbf{A}\theta_{i+1} = \mathbf{P}_k\theta_{i+1}$ , i.e. $\mathbf{A}$ and $\mathbf{P}_k$ unify. Then

$$
\begin{array}{r l} \mathrm{G} _ {i + 1} = & \left(\mathrm{P} _ {1} \wedge \mathrm{P} _ {2} \wedge .. \wedge \mathrm{P} _ {k - 1} \wedge \mathrm{Q} _ {1} \wedge \mathrm{Q} _ {2}.. \wedge \mathrm{Q} _ {\mathrm{n}} \right. \\ & \left. \wedge \mathrm{P} _ {k + 1}.... \wedge \mathrm{P} _ {\mathrm{m}}\right) \theta_ {i + 1} \end{array}
$$

Note that if B has no conjuncts, then A is a fact, and then

$$
G _ {i + 1} = \left(P _ {1} \wedge P _ {2} \wedge .. \wedge P _ {k - 1} \wedge P _ {k + 1} \wedge .... \wedge P _ {m}\right) \theta_ {i + 1}
$$

Condition (ii). $P_{k}$ is a proposition of the form (F $t_{1}$ $t_{2}\ldots t_{n+1}$ ), where F is an n-ary function symbol and $t_{1}\ldots t_{n}$ are object constants and $t_{n+1}$ is a variable. Then

$$
\begin{array}{c} \theta_ {i + 1} = (t _ {n + 1} | (F / t _ {1}, t _ {2},... t _ {n})) \\ G _ {i + 1} = (P _ {1} \wedge P _ {2} \wedge .. \wedge P _ {k - 1} \wedge P _ {k + 1} \\ \wedge .... \wedge P _ {m}) \theta_ {i + 1} \end{array}
$$

This step incorporates arbitrary functions (procedural attachment) into the proof procedure. The variable $t_{n+1}$ is bound to the result of applying F to its arguments $t_{1}\ldots t_{n}$ .

A successful logical proof procedure for $G_{0}$ from the resolution procedure described above where the final goal, $G_{n}$ , is the empty clause. The overall answer substitution for the proof is the composition of the unifiers $\theta_{1}\theta_{2}\ldots\theta_{n}$ used to derive each successive goal.

This fundamental procedure is the basis for the logic programming language PROLOG. As a computational procedure, as in PROLOG, we will assume a depth-first, backward chaining selection of a subgoal to work on, i.e., $P_{k} = P_{1}$ , the first subgoal in the set of subgoals is selected.

Modus ponens can be simply expressed in terms of this procedure. Given the influences:

$$
\forall \mathrm{x} (\mathrm{Ax}) \leftarrow (\mathrm{Bx})
$$

(BZ) $\leftarrow$

Let $G_0 = (A y)$ be the initial goal. The objective is to find y such that (A y) is true. Using the influence $\forall x(A x) \leftarrow (B x)$ , we know that $\theta_1 = \{x/y\}$ unifies the goal and the consequent of the influence. Therefore, the new goal $G_1 = (B x) \{x/y\} = (B y)$ . Using the fact (B Z) $\leftarrow$ , we have the substitution $\theta_2 = \{y/Z\}$ unifies (B Z) and (B y). Since (B Z) $\leftarrow$ has an empty antecedent, $G_2$ is empty and the proof is successful. The solution is $(A y)\theta_1\theta_2 = (A Z)$ .

## 3. Probabilistic inference

We now generalize the resolution proof procedure used in logic programming, to apply to probabilistic reasoning. The overall method consists of using the sentences in the first-order language to prove the existence of a strictly probabilistic (no decisions or value) influence diagram.

A probabilistic influence, incorporating a probabilistic connector, $|_{p}$ , and a probability distribution is of the form:

$$
\mathrm{A} | _ {\mathrm{p}} \mathrm{B} \equiv \pi_ {\mathrm{p}} \left(\omega_ {\mathrm{A}} \mid \omega_ {\mathrm{B}}\right)
$$

The left-hand side of the influence expresses the fact that the probability distribution over the alternative outcomes of A may be dependent on the outcome of B. The right hand side of the influence, $\pi_{\mathrm{p}}(\omega_{\mathrm{A}}|\omega_{\mathrm{B}})$ , provides the numerical values of the distribution. It can be interpreted as providing the probability distribution over the outcomes of A for a given outcomes of B.

Just as logical influences express a means of asserting facts with certainty given other facts, a probabilistic influence expresses a measure of belief in a proposition given other facts.

Foremost to any probabilistic treatment of uncertainty is the background state of information, that is, the knowledge and information available when forming a model. Howard and Matheson [10] make this distinction explicit in their works in probability, where a prior probability density function on a random variable x is written as $\{x|\xi\}$ , where $\xi$ is the background state of information. A fundamental assumption of the probabilistic reasoning developed in this paper is that all facts known with certainty and all their logical conclusions (i.e. the closure under logical implication of the facts and logical influences in the system) are subsumed into the background state of information of the probabilistic model. Therefore, these facts and conclusions do not need to be expressed explicitly in a probabilistic representation. The influence diagram which is developed by the procedure contains only those propositions about which we are uncertain. This allows us to minimize the size of the probabilistic representation, by first attempting to prove (using the logic proof procedures) that a proposition can be subsumed into the background state of information.

Inference is initiated by identifying an initial goal, say (Q x). Then the proof procedure will search the set of expressions in the decision domain to either

(1) logically derive deterministic conclusions (known with certainty) regarding the goal or (2) construct the appropriate probabilistic model that will satisfy the goal.

From the initial goal $G_{0}$ , a successful proof will generate a sequence of goals $G_{1}$ and $G_{n}$ where $G_{n}$ is empty. A transformation to a successive goal may add a node to the influence diagram as a side effect. The conclusion of the proof results in an influence diagram and an answer substitution $\theta$ providing the bindings on the variables in the original goal. For the variables which are bound to alternatives sets, the solution of the influence diagram can yield either

(1) an expectation over alternative values (if the alternatives are real valued) or

(2) a probability distribution over alternative outcomes.

The initial goal associated with a query is $G_{0}=(P\ t_{1}\ t_{2}.....\ t_{k})$ and the procedure initiates with an empty influence diagram $C=\{\}$ . Let $G_{i}$ be a conjunction of the form $P_{1}\wedge P_{2}\wedge\ldots\wedge P_{k}\wedge\ldots\wedge P_{m}$ and let C be a set of nodes in an influence diagram. Select some $P_{k}$ as a subgoal. Then, a new goal $G_{i+1}$ can be derived from $G_{i}$ if one certain qualifying conditions [1].

A successful probabilistic proof procedure for $G_{0}$ results in a series of goals $G_{i}$ derived from the resolution procedure described above where the final goal, $G_{n}$ , is the empty clause. The answer substitution for the proof is the compositions of the unifiers $\theta_{1}\theta_{2}\ldots\theta_{n}$ used to derive each successive goal. As a side effect, the proof procedure constructs a probabilistic influence diagram, C, with a chance node associated with the original goal $G_{0}$ . The chance node associated with the original goal $G_{0}$ will be at the root, i.e., it will have no successors. This diagram can be solved using the influence diagram solution algorithm [1] to provide an unconditional probability distribution or expectation over the alternatives for the query.

As an example, suppose the following statements make up the knowledge base:

Facts: (E Q)

Restricted Propositions: (A{X1,X2}), (B{Y1,Y2}), (C{Z1,Z2})

Influence 1: (A x)| $_{p}$ (B y) ∧ (C z) ≡ π $_{p}^{1}$ (ω $_{A}$ |ω $_{B}$ ,ω $_{C}$ )
Influence 2: (B q)| $_{p}$ (D Q) ∧ (C t) ≡ π $_{p}^{2}$ (ω $_{B}$ |ω $_{C}$ )
Influence 3: (B r)| $_{p}$ (E Q) ∧ (C r) ≡ π $_{p}^{3}$ (ω $_{B}$ |ω $_{C}$ )
Prior: (C v)| $_{p}$ ≡ π(ω $_{C}$ )

The probabilistic query and initial goal $G_{0}$ is (A p). The influence diagram C is empty. There are no logic influences, facts, or prior probabilities which match (A p).

Since (A p) matches (A x) using influence 1, $\theta_{1}=\{x/p\}$ , the new goal G $_{1}$ is (B y) ∧ (C z), and a node in the diagram is created for A with distribution $\pi_{p}^{1}(\omega_{A}|\omega_{B},\omega_{C})$ :

The new subgoals in $G_{1}$ , (B y) and (C z), are associated with node A since the were added to the subgoal list when A was created.

Select (B y) as the subgoal to consider. Since (B y) matches (B q) with Influence 2, $\theta_{2}=\{q/y\}$ , the new goal $G_{2}$ is (D Q) ∧ (C t) ∧ (C z), and a node B is added to the diagram with distribution $\pi_{p}^{2}(\omega_{B}|\omega_{C})$ . Node B has A as a successor since (B y) was added to the subgoal list when A was created.

![](/api/attachments/PEHTCBXY/fulltext/images/ffc619a10ca35e66c61bc1d0f85d1db5ad06179aedc71d0398dbbf4c61680d8e.jpg)

Select (D Q) as the subgoal to consider from the new goal set (D Q) ∧ (C t) ∧ (C z). Since no condition is satisfied, $G_{2}$ cannot be transformed into a derived goal. This branch of the search tree is unsuccessful. Therefore, we backtrack to goal $G_{1}$ , removing node B so that the diagram now consists solely of node A, and re-establishing the previous goal $G_{1}$ , (B y) ∧ (C z), as the goal set.

Again, select (B y) as the subgoal to consider. Using Influence 3 this time, (B y) matches (B r) and the new goal $G_{2}$ is (E Q) ∧ (C r) ∧ (C z). As previously, a node is created for B with distribution. $\pi_{\mathrm{p}}^{3}(\omega_{\mathrm{B}}|\omega_{\mathrm{C}})$ :

![](/api/attachments/PEHTCBXY/fulltext/images/c4d974feba2c782951f7ead8bb275c264a6c2fa5f5f5f9e50e45e9687652b56e.jpg)

Select (E Q) as the subgoal to consider. Since (E Q) is a fact, it can be removed from the list of subgoals. Note that, in general, a subgoal needs only to be provable from the set of facts and logical influences in the knowledge base in order to be removed. The new goal $G_{3}$ is (C r) ∧ (C z).

Select (C r) as the subgoal to consider. Since (C r) matches the prior on C, $\theta_{3}=\{q/y\}$ . A node in the diagram is created for C with probability $\pi(\omega_{\mathrm{C}})$ and a link to node B:

![](/api/attachments/PEHTCBXY/fulltext/images/6ed1c7162f01ac4cbcedcfbb2e9f0d2ab226f724f1b50a22f9d307aabe7c0461.jpg)

Now the new goal $G_{4}$ consists solely of (C z). It unifies with node C which is already in the diagram. Since this subgoal was added to the goal list by the influence which created node A, there is a link from C to A:

![](/api/attachments/PEHTCBXY/fulltext/images/4bf0348040991415bb3f296df0e0fd10fc1df0d40c52755c14e6117bf792d3e4.jpg)

(C z) can be removed from the goal list, thus rendering $G_{5}$ empty and the proof procedure successful, the diagram shown above as the result.

Now this diagram is solved to yield an answer to the query. Node A in the diagram has no successors, so it is selected as the node to be solved for in the solution procedure. In order to solve the diagram, node B is first removed by recalculating $\pi(\omega_{\mathrm{A}}|\omega_{\mathrm{C}})$ as:

$$
\begin{array}{r l} & {\pi (\omega_ {\mathrm{A}} | \omega_ {\mathrm{C}})} \\ & {\quad = \pi_ {\mathrm{p}} ^ {1} (\omega_ {\mathrm{A}} | (\mathrm{BY1}), \omega_ {\mathrm{C}}) \times \pi_ {\mathrm{p}} ^ {3} ((\mathrm{BY1}) | \omega_ {\mathrm{C}})} \\ & {\qquad + \pi_ {\mathrm{p}} ^ {1} (\omega_ {\mathrm{A}} | (\mathrm{BY2}), \omega_ {\mathrm{C}}) \times \pi_ {\mathrm{p}} ^ {3} ((\mathrm{BY2}) | \omega_ {\mathrm{C}})} \end{array}
$$

The next step is to remove node C.

$$
\begin{array}{l} \pi (\omega_ {\mathrm{A}}) = \pi_ {\mathrm{p}} (\omega_ {\mathrm{A}} | (\mathrm{CZ1})) \times \pi ((\mathrm{CZ1})) \\ + \pi_ {\mathrm{p}} (\omega_ {\mathrm{A}} | (\mathrm{CZ2})) \times \pi ((\mathrm{CZ2}) \end{array}
$$

The distribution $\pi(\omega_{\mathrm{A}})$ is the answer to the original probabilistic query.

## 4. Alternative outcome inference

The objective of this procedure is to determine the set of alternative outcomes for a proposition if alternative sets for variables in the proposition have not been entered directly. In particular, in many cases we desire to learn what the possible ramifications of uncertainties are on the objectives in a given decision problem. Taking the example of security trading [6], suppose the proposition (PROFIT p) represents the statement the profit is p, the value in the decision problem.

The influences describing the generation of profit are:

```lisp
(PROFIT p) → (REVENUES r)
∧ (COSTS c) ∧ (-r c p)
(REVENUES r) → (PRICE p)
∧ (QUANTITY-SOLD q)
∧ (* p q r)
(COSTS c) → (UNIT-COST uc)
∧ (QUANTITY-SOLD q)
∧ (* uc q c)
```

Suppose in addition we also have the information about the outcomes of some of these propositions. We wish to determine the ramifications our uncertainty portends regarding the outcomes for profit. Thus, this section develops a procedure that cascades alternative outcomes through a set of logical influences.

In the proof procedures described above, a sequence of goals is generated. Each goal constitutes a conjunction and the procedures succeed when an empty goal state is achieved. As noted in the example for probabilistic reasoning, we use backtracking to search until a single successful path (i.e. terminating in an empty goal) is found. In attempting to determine alternative outcomes, it is necessary to explore all possible paths to prove a proposition. Therefore, instead of a sequence of goals, the proof procedure described here generates a tree of goal states. A single goal state may have several associated derived goals. These derived goals will be referred to as the descendants of a goal state. The branch of a tree will terminate when a goal state on that branch is empty. Alternative outcomes will be determined by examining all branches of the tree from the initial goal to the branches which terminate successfully. As a side effect of the proof procedure, a deterministic influence diagram, consisting entirely of deterministic chance nodes, is constructed.

Let G be a goal of the form $P_{1} \wedge P_{2} \wedge \ldots \wedge P_{k} \wedge \ldots \wedge P_{m}$ , and let C be a set of chance nodes in an influence diagram. One step in the proof procedure consists of the derivation of a set of descendant goals $G_{1}, \ldots, G_{r}$ and descendant substitutions $\theta_{1}, \ldots, \theta_{r}$ for G. Select some $P_{k}$ in G as a subgoal. The descendant goals for G exist if one of the following conditions holds:

Condition (i). $P_{k}$ is logically derivable from the set of influences of the form $A \leftarrow B$ with answer substitution $\theta_{1}$ . Then, the single descendant of G is

$$
\mathrm{G} _ {1} = \left(\mathrm{P} _ {1} \wedge \mathrm{P} _ {2} \wedge .. \wedge \mathrm{P} _ {\mathrm{k} - 1} \wedge \mathrm{P} _ {\mathrm{k} + 1} \wedge .... \wedge \mathrm{P} _ {\mathrm{m}}\right) \theta_ {1}
$$

Thus, if a subgoal is logically provable from the knowledge base, it can be eliminated from the explicit enumeration of alternative values. This minimizes the sizes of the representation generated by this procedure.

Condition (ii). There exists is a node labelled N in C and an alternative substitution, $\theta$ , such that $N\theta = P_{k}\theta$ . Recall that $\Theta(A)$ is the set of fact substitutions which can be used to develop the alternative instantiations of a restricted proposition. Then the descendant substitutions for G is the set $\Theta(N\theta)$ and the set of descendant goals for G is:

$$
\begin{array}{r l} & {\left\{\mathrm{G} _ {1},.. \mathrm{G} _ {\mathrm{r}} \right\}} \\ & {\quad = \left\{\left(\mathrm{P} _ {1} \wedge \mathrm{P} _ {2} \wedge .. \wedge \mathrm{P} _ {\mathrm{k-1}} \wedge \mathrm{P} _ {\mathrm{k+1}} \wedge .... \wedge \mathrm{P} _ {\mathrm{m}}\right) \theta | \theta \right.} \\ & {\quad \text { where   r   is   the   cardinality   of } \Theta (\mathrm{N} \theta),} \end{array}
$$

that is, the number of alternative possible outcomes for N. In addition, it is necessary to add a link from node N to the node created when $P_{k}$ was originally added to the list of subgoals.

In this step, a node has been found which is already in the diagram and matches the selected subgoal. This node defines the set of alternative outcomes for the selected subgoal.

Condition (iii). There exists a restricted proposition assertion $A \leftarrow$ and an alternative substitution $\theta$ such that $A\theta = P_{k}\theta$ . Then the descendant substitutions for G is the set $\Theta(A\theta)$ and the set of descendant goals for G is:

$$
\begin{array}{r l} & {\left\{\mathbf {G} _ {1},.. \mathbf {G} _ {\mathrm{r}} \right\}} \\ & {\quad = \left\{\left(\mathbf {P} _ {1} \wedge \mathbf {P} _ {2} \wedge .. \wedge \mathbf {P} _ {\mathrm{k-1}} \wedge \mathbf {P} _ {\mathrm{k+1}} \wedge .... \wedge \mathbf {P} _ {\mathrm{m}}\right) \theta | \theta \right.} \\ & {\quad \text { where } r \text { is   the   cardinality   of } \Theta (\mathrm{N} \theta),} \end{array}
$$

that is the number of alternative possible outcomes for A. The set of deterministic chance nodes in C is augmented with a node labelled $A\theta$ . In addition, it is necessary to add a link from node Aθ to the node created when $P_{k}$ was originally added to the list of subgoals. The new node Aθ has no predecessors. Although the restricted proposition Aθ may appear in the consequent of probabilistic and informational influences, these effects are not relevant to the calculation of alternative outcomes. This step is analogous to unification with a fact in logical inference or a prior probability in probabilistic inference.

Condition (iv). There exists a set of influences

I of the form $A_{r} \leftarrow B_{r}$ where $B_{r}$ is a conjunction of the form $Q_{r1} \wedge Q_{r2} \wedge .. \wedge Q_{rn}$ such that for each influence r in I there is a fact substitution $\theta_{r}$ such that $A_{r}\theta_{r} = P_{k}\theta_{r}$ . Then the descendant substitutions set for G is $\{\theta_{1}, \theta_{2}, ..., \theta_{r}\}$ and the set of descendant goals for G is:

$$
\left\{\left(P _ {1} \wedge P _ {2} \wedge .. \wedge P _ {k - 1} \wedge Q _ {1 1} \wedge Q _ {1 2} \dots . \wedge Q _ {1 n} \right. \right.
$$

$$
\wedge \dots \wedge \left. P _ {m}\right) \theta_ {1}
$$

![](/api/attachments/PEHTCBXY/fulltext/images/66bdece2833cc7ae137be51700c630718676ebb46449e3a7707be05fe029b9e9.jpg)  
Fig. 1. Alternative outcome search tree.

$$
\begin{array}{r l} & , (P _ {1} \wedge P _ {2} \wedge .. \wedge P _ {k - 1} \wedge Q _ {2 1} \wedge Q _ {2 2}.... \wedge Q _ {2 n} \\ & \quad \wedge ... \wedge P _ {m}) \theta_ {2} \\ & ,...... \\ & , (P _ {1} \wedge P _ {2} \wedge .. \wedge P _ {k - 1} \wedge Q _ {r 1} \wedge Q _ {r 2}.... \wedge Q _ {r n} \\ & \quad \wedge ... \wedge P _ {m}) \theta_ {r} \} \end{array}
$$

The set of chance nodes in the diagram C is augmented with a deterministic chance node labelled A, and as previously, an arc is added from A to the node which was created when $P_{k}$ was added to the descendant subgoal list. Each subgoal $Q_{ij}$ added to the subgoal lists is associated with the new node A, so that the necessary arcs can be added to the diagram.

This final step is the “backward chaining” portion of the alternative outcome proof procedure. We examine all possible rules which could provide a conclusion about the proposition, and based on the alternative outcomes of all the propositions in their antecedents, the alternative outcomes for the target proposition are developed.

A successful alternative outcome proof procedure for $G_{0}$ results in a tree of derived goals, each leaf of which is the empty set. During the course of generating the goal sets, an influence diagram consisting solely of deterministic chance nodes is developed. The deterministic mapping $\pi_{i}$ for each node is determined by calculating the composition of the substitutions on each branch of the tree descending from a given goal. The diagram will consist of the root node, corresponding to the original goal, which has no successors; a set of intermediate nodes which have both successors and predecessors; and some leaf nodes, which have no predecessors. The alternative outcomes for the root are obtained by removing all intermediate deterministic chance nodes from the diagram.

Suppose a knowledge base consists of the influences

(REVENUES {400, 500})

← and (COSTS {150, 200}) ← .

We wish to draw conclusions about the possible outcomes for (PROFIT x) knowing that either (REVENUES 400) or (REVENUES 500) is true and that either (COSTS 150) or (COSTS 200) is true. Using the alternative outcomes proof procedure described above, the alternative outcome search tree displayed in Fig. 1 is developed.

$G_{0}$ is the original goal. Since there is only one influence whose consequent unifies with the goal, there is a single descendant goal, $G_{1}$ . A node for (PROFIT p) is created in the diagram.

At this point, (REVENUES r) is selected as the next subgoal to consider. Since the alternative set is $\{400, 500\}$ , $G_{1}$ has two descendant goals, $G_{2}$ and $G_{3}$ . Node (REVENUES $\{400, 500\}$ ) is created, with an arc to (PROFIT p).

At the next level in the tree (COSTS c) is the selected subgoal to consider. The alternative possibilities are (COSTS 150) and (COSTS 200), $G_{2}$ and $G_{3}$ both having two descendant goals, $\{G_{4}, G_{5}\}$ and $\{G_{6}, G_{7}\}$ respectively. Node (COSTS {150 200}) is created with an arc to node (PROFIT p).

The final level of the tree indicates the evaluation of the function “-” within the proof procedure, resulting in single descendants for $G_{4}$ , $G_{5}$ , $G_{6}$ and $G_{7}$ . The alternative outcomes for (A y) are calculated from the composition of the substitution on each path through the tree.

The previous example was straightforward in that the dependency structure was a tree. The deterministic influence diagram construction is necessary when the influences do not imply a tree dependency structure. As another example, let us extend the previous example with the following influences which constitute the knowledge base.

```lisp
(PROFIT p) → (REVENUES r) ∧ (COSTS c)
∧ (-r c p)
(REVENUES r) → (PRICE p)
∧ (QUANTITY-SOLD q)
∧ (*p q r)
(COSTS c) → (UNIT-COST uc)
∧ (QUANTITY-SOLD q)
∧ (*uc q c)
(UNIT-COST 3) ←
(PRICE {5 6}) ←
(QUANTITY-SOLD {100 120}) ←
```

The deterministic diagram associated with an alternative outcome query on (PROFIT y) is:

![](/api/attachments/PEHTCBXY/fulltext/images/b4d259bf3a5d73d5c18b30bfaa3fea7e87527f9e2e8abeee86cafecf2ee089bd.jpg)

(REVENUES 300) ∧ (COSTS 150)
imply (PROFIT 150)
(REVENUES 300) ∧ (COSTS 200)
imply (PROFIT 100)
(REVENUES 400) ∧ (COSTS 150)
imply (PROFIT 250)
(REVENUES 400) ∧ (COSTS 200)
imply (PROFIT 200)
(REVENUES 375) ∧ (COSTS 150)
imply (PROFIT 225)
(REVENUES 375) ∧ (COSTS 200)
imply (PROFIT 175)
(REVENUES 500) ∧ (COSTS 150)
imply (PROFIT 350)
(REVENUES 500) ∧ (COSTS 200)
imply (PROFIT 300)

We need to reduce this diagram to a single deterministic node. First, the REVENUES node is removed. This leaves a dependency structure as:

![](/api/attachments/PEHTCBXY/fulltext/images/c090d7ebac97075851af54a0cb638415f270a623238c6a11ee81e2feeab56742.jpg)  
(PRICE 10) ∧ (QUANTITY-SOLD 30)
∧ (COSTS 150) imply (PROFIT 150)
(PRICE 10) ∧ (QUANTITY-SOLD 30)
∧ (COSTS 200) imply (PROFIT 100)

(PRICE 10) ∧ (QUANTITY-SOLD 40)
∧ (COSTS 150) imply (PROFIT 250)
(PRICE 10) ∧ (QUANTITY-SOLD 40)
∧ (COSTS 200) imply (PROFIT 200)
(PRICE 12.5) ∧ (QUANTITY-SOLD 30)
∧ (COSTS 150) imply (PROFIT 225)
(PRICE 12.5) ∧ (QUANTITY-SOLD 30)
∧ (COSTS 200) imply (PROFIT 175)
(PRICE 12.5) ∧ (QUANTITY-SOLD 40)
∧ (COSTS 150) imply (PROFIT 350)
(PRICE 12.5) ∧ (QUANTITY-SOLD 40)
∧ (COSTS 200) imply (PROFIT 300)
Now remove COSTS.

![](/api/attachments/PEHTCBXY/fulltext/images/2fbc5ddce495473b30edd2b8e9bcce9c27aee804128268ffcb153bb99e8d25a3.jpg)

(PRICE 10) ∧ (QUANTITY-SOLD 30)
imply (PROFIT 150)
(PRICE 10) ∧ (QUANTITY-SOLD 40)
imply (PROFIT 200)
(PRICE 12.5) ∧ (QUANTITY-SOLD 30)
imply (PROFIT 225)
(PRICE 12.5) ∧ (QUANTITY-SOLD 40)
imply (PROFIT 300)

This diagram shows the true nature of the dependency. The alternative outcomes for profit are determined by the variations in the quantity sold and the price.

## 5. Decision theoretic inference

The next step is to combine and extend the logical, probabilistic, and alternative outcome procedures described in the previous sections to decision making. The procedure described here involves the consideration of the decision maker's values as well as explicit consideration of decisions.

The overall structure of the procedure is the same as that for probabilistic inference -a set of declarative sentences is used of construct an influence diagram. In this case we require that the diagram be a decision network, i.e., it must have exactly one value node, zero or more decision nodes, and zero or more chance nodes. Moreover the proof procedure must allow for the inclusion of decision nodes in the diagram.

Definition. Let $G_{0}$ be a proposition of the form $(P t_{1} t_{2}... t_{n})$ where the $t_{i}$ are terms. If there is exactly one term in $G_{0}$ which is a restricted variable, say x, and the members of the alternative set associated with $x = \{X_{1}, X_{2}, ... X_{3}\}$ are real numbers, then the maximization of $G_{0}$ with respect to x is a valid goal of a decision-theoretic proof procedure.

This places a restriction on the alternative outcomes of a value proposition- namely, that they must be based on the alternative set of a single variable in the proposition, and the members of the alternatives set must be real numbers. This requirement allows us to treat that variable as a cardinal value measure for expected value calculations for decision making. For example, the proposition (SALES {100 125 150}) WIDGETS) can be treated as a value proposition.

The decision-theoretic proof procedure starts with a valid goal, $G_{0}$ , and an empty influence diagram $N = \{\}$ . As in the previous cases, we describe a set of transformations of the goal. Let a goal, $G_{i}$ , be a conjunction of the form $P_{1} \wedge P_{2} \wedge .. \wedge P_{k} \wedge ..... \wedge P_{m}$ , and let N be the set of nodes in an influence diagram, where $N = C \cup D \cup V\}$ . C is the set of chance nodes. D is the set of decision nodes, and v is the value node. Select some $P_{k}$ as a subgoal. Then, a new goal, $G_{i+1}$ , can be derived from $G_{i}$ if one of the following conditions holds:

Condition (i). $P_{k}$ is logically derivable from the set of influences of the form $A \leftarrow B$ with answer substitution $\theta_{i+1}$ . Then

$$
\mathrm{G} _ {\mathrm{i+1}} = \left(\mathrm{P} _ {1} \wedge \mathrm{P} _ {2} \wedge .. \wedge \mathrm{P} _ {\mathrm{k-1}} \wedge \mathrm{P} _ {\mathrm{k+1}} \wedge .... \wedge \mathrm{P} _ {\mathrm{m}}\right) \theta_ {\mathrm{i+1}}
$$

As previously, if a subgoal is explicitly entered in the knowledge base or is provable from the set of logical influences in the knowledge base, then it can be removed from the list of goals.

Condition (ii). There exists a node, labelled $N_{j}$ in N and an alternatives substitution $\theta_{i+1}$ , such that $N_{j}\theta_{i+1}=P_{k}\theta_{i+1}$ . Then

$$
\mathrm{G} _ {\mathrm{i} + 1} = \left(\mathrm{P} _ {1} \wedge \mathrm{P} _ {2} \wedge .. \wedge \mathrm{P} _ {\mathrm{k} - 1} \wedge \mathrm{P} _ {\mathrm{k} + 1} \wedge .... \wedge \mathrm{P} _ {\mathrm{m}}\right) \theta_ {\mathrm{i} + 1}
$$

An arc is added from node N to the node which was created when $P_{k}$ was originally added to the list of subgoals. Again as in previous cases, the subgoal $P_{k}$ has already been accounted for in the diagram and therefore can be removed from the list of subgoals.

Condition (iii). There exists an informational influence of the form $A|_{i}B$ , where B is a conjunction of the form $Q_{1} \wedge Q_{2} \wedge .. \wedge Q_{n}$ and an alternatives substitution $\theta_{i+1}$ such that $A_{j}\theta_{i+1} = P_{k}\theta_{i+1}$ . Then

$$
\begin{array}{r l} \mathrm{G} _ {\mathrm{i+1}} = & (\mathrm{P} _ {1} \wedge \mathrm{P} _ {2} \wedge .. \wedge \mathrm{P} _ {\mathrm{k-1}} \wedge \mathrm{Q} _ {1} \wedge \mathrm{Q} _ {2} \wedge .. \wedge \mathrm{Q} _ {\mathrm{n}} \\ & \wedge \mathrm{P} _ {\mathrm{k+1}} \wedge .... \wedge \mathrm{P} _ {\mathrm{m}}) \theta_ {\mathrm{i+1}} \end{array}
$$

The set of decision nodes in the diagram. D, is augmented with a node labelled $A\theta_{i+1}$ . An arc is added to the diagram from the new node created when $P_{k}$ was added to list of subgoals. The new node's predecessors are associated with the restricted variables $Q_{i}\theta_{i+1}$ in B. This step is identical to the addition of a probabilistic node in the probabilistic inference and condition (iv) below, except that a decision node is added to the diagram.

Condition (iv). There exists an influence of the form $A|_{p}B \equiv \pi_{p}(A|B)$ , where b is a conjunction of the form $Q_{1} \wedge Q_{2} \wedge .. \wedge Q_{n}$ and an alternatives substitution, $\theta_{i+1}$ , such that $A_{i}\theta_{i+1} = P_{k}\theta_{i+1}$ . Then

$$
\begin{array}{c} \mathrm{G} _ {\mathrm{i+1}} = \big (\mathrm{P} _ {1} \wedge \mathrm{P} _ {2} \wedge .. \wedge \mathrm{P} _ {\mathrm{k-1}} \wedge \mathrm{Q} _ {1} \wedge \mathrm{Q} _ {2} \wedge .. \wedge \mathrm{Q} _ {\mathrm{n}} \\ \wedge \mathrm{P} _ {\mathrm{k+1}} \wedge .... \wedge \mathrm{P} _ {\mathrm{m}} \big) \theta_ {\mathrm{i+1}}. \end{array}
$$

The set of chance nodes, C, in the diagram is augmented with node labelled $A\theta_{i+1}$ and conditional probability distribution $\pi_{p}(A|B)$ . An arc is added to the diagram from the new node to the node created when $P_{k}$ was added to list of sub-goals.

Condition (v): There exists an alternative outcomes proof procedure for $P_{k}$ starting with influence diagram N and resulting in an answer substitution, $\theta_{i+1}$ , and a set of leafnodes labelled $\{Q_{1} \wedge Q_{2} \wedge .. \wedge Q_{n}\}$ . Then

$$
\begin{array}{r l} \mathrm{G} _ {i + 1} = & \left(\mathrm{P} _ {1} \wedge \mathrm{P} _ {2} \wedge .. \wedge \mathrm{P} _ {\mathrm{k} - 1} \wedge \mathrm{Q} _ {1} \wedge \mathrm{Q} _ {2} \wedge .. \wedge \mathrm{Q} _ {\mathrm{n}} \right. \\ & \left. \wedge \mathrm{P} _ {\mathrm{k} + 1} \wedge .... \wedge \mathrm{P} _ {\mathrm{m}}\right) \theta_ {i + 1} \end{array}
$$

This step is used primarily in evaluation of a value function for scoring sets of outcomes for uncertain propositions.

A successful decision-theoretic proof procedure for $G_{0}$ results in a series of goals $G_{i}$ derived from the steps described above where the final goal, $G_{n}$ , is the empty clause. The answer substitution for the proof is the composition of the unifiers, $\theta_{1}\theta_{2}\ldots\theta_{n}$ , used to derive each successive goal. As a side effect, the proof procedure constructs a prepositional influence diagram, with a single value node associated with the original goal $G_{0}$ and decision nodes and chance nodes corresponding to the informational and probabilistic influences encountered in the proof. This diagram, which incorporates the information, alternatives, and preferences of the decision maker as expressed in the knowledge base, is solved using the influence diagram solution algorithm. The solution procedure provides the expectation over the alternatives for the query and for the sequence of optimal decisions, expressed in terms of a set of decision functions $\pi_{d}$ .

To demonstrate this procedure, we will use the example. The influences provide a set of templates or patterns for the generation of many probabilistic and decision-theoretic models. The proof procedures described above will search this description, as well as the facts and prior probabilities in the knowledge base at the time of a particular query, in order to generate the appropriate diagram. The complete set of influences in the knowledge base, are listed by number in the Appendix.

The query is (PROFIT p 3), that is, “What is the expectation for the variable ”p“ in the profit proposition for time 3?”. Since there is a logical influence which has PROFIT as its conclusion (A10), the procedures will first attempt to prove deterministically the binding on “p” in (PROFIT p 3). However, the values of profit are driven ultimately (via A7-A10) by the outcomes of (PRICE price time) and (TRADE act time). Because these propositions are not known with certainly by virtue of their alternative sets designations (A1, A2) and the influences which are applicable to these propositions (A11, A12, A14-A15), profit cannot be deduced with certainty. There are not probabilistic or informational influences that unify with (PROFIT p 3); therefore, we invoke the alternative outcome proof procedure to generate the set of possible outcomes for (PROFIT p 3). This procedure will generate the deterministic diagram of Fig. 2.

![](/api/attachments/PEHTCBXY/fulltext/images/60d70f21aebf38a2ba1d1ea7507ae8b4e4ba921aed61f2190c8c864125593c20.jpg)  
Fig. 2. Deterministic diagram for profit.

The procedure terminates when it encounters facts (e.g. (PROFIT 0 0) and (POSITION 0 0)) and when alternative outcomes are specified (e.g. for PRICE and TRADE A1 and A2). To this point we have developed a model mapping uncertain outcomes (PRICE) and decisions (TRADE) into value (PROFIT p 3).

The diagram in Fig. 2 is an intermediate product. The interior nodes in the diagram will be removed as part of the alternative outcome proof procedure, as described in section 4. The influence diagram, N, which will be the ultimate result of the query consists of a single node for (PROFIT p 3). The rest of the diagram is completed by addressing the new subgoals in $G_{1}$ represented by the leaf nodes of the deterministic diagram in Fig. 2. These subgoals are:

![](/api/attachments/PEHTCBXY/fulltext/images/e5006bfe67782701bf2e04ba032597f1d4db6b72e8381617a9ba1aa728023d30.jpg)  
Fig. 3. Construction of an influence diagram.

(PRICE {90,91,92}0) ∧ (PRICE {90,91,92} 1)

$\wedge$ (TRADE {BUY SELL

HOLD}1) ∧ (PRICE {90,91,92} 2)

$\wedge(\text{TRADE } \{\text{BUY SELL HOLD}\} 2) \wedge$

(PRICE {90,91,92}3)

(PRICE price 0) has a prior probability distribution from influence A16 and therefore an additional node is added to the diagram. The subgoal (PRICE price 1) matches the probabilistic influence A11 that has the previous period's PRICE in its antecedent. Similarly, by way of A15, (TRADE act 1) is linked to (PRICE price 1). The state of the diagram to this juncture is illustrated in Fig. 3 (i).

The next subgoal to consider is (PRICE {90,91,92} 2). Since (FUTURES-EXPIRE 2) is true (A18) prices are conditioned not by previous prices but by (FUTURES-ACTIVITY level 2) as expressed in influence A12. The diagram expands reflecting this rule in Fig. 3(ii). Next we consider (TRADE action 2). By influence A14, the trader has a market assessment from the GURU available at the time of this decision, as well as information about the current price. The additional nodes and links associated with this rule are shown in Fig. 3(iii).

The trader's opinion of the quality of the information from the trader is expressed in influence A13. This influence creates links from PRICE in the current period and the next period to GURU. Informally the GURU's assessment is "influenced" by current and future prices in the sense that given that future prices are greater than current prices. The GURU is more likely to be BULLISH. A node for (PRICE price 3) is created. Its probabilistic structure is again determined by A11, and therefore a link is added to (PRICE price 2). The final subgoal to consider is (PRICE price 3) which already is in the diagram. Therefore all that is needed to complete the diagram is a link from (PRICE {} 3) to (PROFIT {} 3). The completed diagram is in Fig. 4.

This diagram has several important features. First, is has no quantified variables in the sense they are used in first-order predicate calculus. The proof procedure has provided values (or sets of values) for all variables that appear in the influences used to construct the diagram.

Second, the diagram has been constructed using only the information needed to address the particular query. Additional information, which can in no way effect the results, is ignored. For example, probabilistic information regarding the GURU and FUTURES are not included for periods 0 and 1, since the conditions under which we need to consider these factors are not met.

![](/api/attachments/PEHTCBXY/fulltext/images/2bd27f92e8ba0295faa7090b1f192aba17cf5a36b50cd07bfe027e89c6415de3.jpg)  
Fig. 4. Complete diagram.

Similarly, the probabilistic representation is limited to only those propositions that are explicitly uncertain. For example, propositions referring to net position and previous values of profit are not explicitly in the probabilistic representation, since they can be expressed completely with the other propositions in the diagram.

Solution of the diagram yields two primary outputs. The first is a set of decision functions, one for each decision node in the diagram. The functions express the optimal choice (Buy, Sell or Hold) as a function of what is known at each TRADE point. In addition, the expectation of “p” from the original query (assuming the decision embodied in the decision functions are followed) is a product of the influence diagram solution algorithm.

## 6. Conclusions

In this paper we have presented a set of complementary inference techniques for reasoning about decision making. The methods were:

\- Logical Inference

\- Probabilistic Inference

• Alternative Outcome Inference

• Decision-Theoretic Inference

The idea that unifies the last three techniques is the dynamic construction of an influence diagram model of the dependencies related to a particular query. Two fundamental characteristics of the procedures described here are

(1) there is an implicit control structure guiding the search for models, and

(2) it is possible that a single query could generate several probabilistic or decision theoretic models consistent with a decision domain knowledge base.

The inference procedure described above admit a precedence in choosing which procedure to follow when attempting to address a particular subgoal. This precedence implies a control structure for the search for probabilistic and decision theoretic models. Overall, control is focused on minimizing the extent of models that explicitly account for uncertainty—either probabilistically or the less informative alternative outcome sets. All the techniques initially use logic to attempt to draw conclusions regarding any subgoal. If there is information available that asserts the absolute truth value of a proposition, then the other possible values can be ignored.

Another level of control involves the selection of alternative probabilistic representations. In the implementation of these methods, the probabilistic inference procedure will search for a prior probability distribution (i.e. an influence of the form $A|_{p}$ ) before attempting to use probabilistic influences of the form $A|_{p}B$ , which in general can increase the size of the probabilistic representation.

A third kind of implicit control relates to decision recommendations. As noted previously, proof procedure that encounters a proposition as a subgoal will first attempt to use logic procedures to determine a binding; if unsuccessful, then other methods are attempted. Thus in attempting to prove something about $(D\ t_{1}...),$ our approach will first look at influences of the form $(D\ t_{1}...)\leftarrow C$ (where C is a conjunction of preconditions) before examining rules of the form $(D\ t_{1}...)|_{i}$ C which express information availability and can only be used explicitly within the context of decision theoretic inference. Therefore, a logical decision rule entered explicitly into the knowledge base takes precedence over one that is derived by decision-theoretic methods.

This discussion raises the issue of consistency. Since multiple influences can provide conclusions about a given proposition, multiple models (and their associated decision recommendations) may be consistent with a single knowledge base and query. The issue becomes how can we resolve the conclusions of these different models? One answer is further refinement of the knowledge base to make explicit any conditions under which one representation is preferred to another. Similarly, one can construct probabilistic or other representations that embody methods for combining information's and outputs. The inference methods as currently defined do not explicitly have methods for resolving and insuring consistency among the multiple models that may be derivable from a knowledge base. However, the overall approach provides the ability to generate the multiple models. The system can then appeal to a higher level authority, perhaps the human decision maker, to interpret and integrate the findings. Explicit and formal methods for reasoning about alternative models and their conclusions is an ongoing and future area of research.

## 7. For further reading

[7]

## Appendix A

## Influence for trading example

(TRADE (BUY SHELL HOLD) TIME) ← (A1)
(PRICE (90 91 92) time) ← (A2)
(FUTURE-VOLUME {HEAVY MODERATE} time) ← (A3)
(GURU {BULLISH BEARISH} time) ← (A4)
(PROFIT 0.0 0) ← (A5)
(POSITION 0.0 0) ← (A6)
(POSITION new-position time) ← (-time 1 last-time) ∧ (A7)
(POSITION old-position last-time) ∧
(TRADE BUY time) ∧
(+old-position 100 new-position)
(POSITION new-position time) ← (-time 1 last-time) ∧ (A8)
(POSITION old-position last-time) ∧
(TRADE SELL time) ∧
(-old-position 100 new-position)
(POSITION old-position time) ← (-time 1 last-time) ∧ (A9)
(POSITION old-position last-time) ∧
(TRADE HOLD time)
(POSITION new-profit time) ← (-time 1 last-time) ∧ (A10)
(PROFIT old-profit last-time) ∧
(PRICE old-price last-time) ∧
(PRICE price time) ∧
(POSITION old-position last-time) ∧
(-price old-price change-in-price) ∧
(\* old-position change-in-price change-in-value) ∧

(+old-profit change-in-value new-profit)

PRICE new-price time) |p (FUTURES-EXPIRE time) ∧ (A11)
(FUTURES-ACTIVITY level time)
= π\_p (ω(PRICE new-price time)|ω(FUTURES-
ACTIVITY level time)

PRICE new-price time)|p (FUTURES-EXPIRE time) ∧ (A12)
(FUTURES-ACTIVITY level time)
= π\_p (ω(PRICE new-price time)|ω(FUTURES-
ACTIVITY level time)

(GURU assessment time p)|p (+time 1 next-time) ∧ (A13)
(PRICE price time) ∧ (PRICE next-price next-time)
= π\_p (ω(GURU assessment time)|ω(PRICE price time) ∧
(PRICE next-price next-time))

(TRADE action2)|i (GURU assessment 2) ∧ (A14)
∧(PRICE price 2)

(TRADE action time)|i (PRICE price time) ∧ (A15)
(PRICE price 0)|p ≡ π\_p(ω(FUTURES-
ACTIVITY level time))

(FUTURES-ACTIVITY level time)|p ∧ (A17)
≡ π\_p(ω(FUTURE-ACTIVITY level time))

(FUTURE-EXPIRE 2) ← (A18)

## References

[1] J. Breese and E. Tse, Integrating Logical and Probabilistic Reasoning for Decision Making, AAAI, Third Workshop on Uncertainty in AI, Seattle, Wash. 1987, 355–362.

[2] C.F. Cooper, A Method for Using Belief Networks as Influence Diagrams, AAAI, Fourth Workshop on Uncertainty in AI, Minneapolis, Minn., 1988, 55–63.

[3] Gallier, J.A. Logic for Computer Science: Foundations of Automatic Theorem Proving, New York: Harper and Row, 1986.

[4] D. Geiger and J. Pearl, On the Logic of Counsel Models, AAAI, Third Workshop on Uncertainty in AI, Sealth Wash, 1987, 136–147.

[5] A.M. Geoffrion, The Formal Aspects of Structured Modeling, Operations Research 37, 1989, 30–51.

[6] H.W. Gottinger and H.P. Weimann, Intelligent Decision Support Systems, CISM/IIASA Seminar on DSS, Udine, Sept. 1990.

[7] S. Holtzmann and J.S Breese, Exact Reasoning about Uncertainty: On the Design of Expert Systems for Decision Support, In Kanal. and Lemmer (editors), Uncertainty in Artificial Intelligence, Amsterdam: North Holland, 1986, pp. 339–346.

[8] S. Holtzmann, Intelligent Decision Systems, Addison Wesley, Publ. Co. Reading, Mass. 1989

[9] E.J. Horvitz, Reasoning about Beliefs and Actions under Computational Resource Constraints, in L.N. Kanal, T.S. Levit, and J.F. Lemmer (eds) Uncertainty in Artificial Intelligence 3, North Holland: Amsterdam 1989, 301–324.

[10] R.A. Howard and J.E. Matheson, Influence Diagrams, 1981, In Howard R.A. and J.E. Matheson (editors), The Principles and Applications of Decision Analysis, SDG Publications, Strategy Decisions Group, Menlo Park, California, 1984.

[11] M. Jarke and F.J. Radermacher, The AI Potential of Model Management and its Central Role in Decision Support, Decision Support Systems 4, 1988, 387–404.

[12] A.C. Miller and M.M. Merkhofer, R.A. Howard, Development of Automated Aids for Decision Analysis, Stanford Research Institute, May 1976.

[13] J. Pearl, Fusion, Propagation, and Structuring in Belief Networks, Artificial Intelligence. (29:3), September 1986, pp. 241–288.

[14] J. Pearl, Probabilistic Reasoning in Intelligent Systems, Morgan Kaufmann Publ.: San. Mateo, 1988.

[15] R.D. Shatcher, Evaluating Influence Diagrams, Operations Research. Nov.-Dec. 1986.

[16] R.D. Shatcher, Probabilistic Inference and Influence Diagrams, Operations Research, see also IEEE SMC 20 No 2, 1990, pp. 365–379.

[17] P.P. Shenoy and G. Shafer, K. Mellouli, Propagation of Belief Functions: A Distributed Approach, Proceedings of the RCA/AAAI Workshop on Uncertainty and Probability in Artificial Intelligence, Philadelphia, PA, August, 1986, pp. 249–260.

[18] M.P. Wellmann, Fundamental Concepts of Qualitative Probabilistic Networks, Mimeo -Wright-Patterson AFB, Sept. 1989.

[19] L.A. Zadeh, A Simple View of the Dempster-Shafer Theory of Evidence, AI Magazine 7(2), 1986.

![](/api/attachments/PEHTCBXY/fulltext/images/a8fbdb4550a0542df1067dc167afe307cb870ce55f321b8cf80c4857c889de4d.jpg)

Hans W. Gottinger received a diploma in Economics from the University of Munich (1966). PhD Math. Statist., University of Munich, 1969 Habil. Oper. Researcher, Technical University of Munich, 1973. He held positions as Visiting Professor at the University of California, Berkeley (1972–1974), the University of California, Los Angeles (1976) and the University of Virginia Charlottesville (1985–1987). He has been Professor of Man-

agement Science, University of Maastricht, the Netherlands since 1985 and Director, Fraunhofer Institute of Technological Forecasting, Euskirchen/Bonn, Germany since 1987. Since 1990 he has been on leave of absence as a Visiting Professor to Nuffield College and the Oxford Institute for Energy Studies, Oxford, UK.

![](/api/attachments/PEHTCBXY/fulltext/images/d40c4f3616d3a4e9e407bef9a08316cab98c28b21e78359825bff23aaa4b6126.jpg)

H. Peter Weimann received his diploma in Computer Science from the University of Dortmund in 1985. Currently working for the IABG he has been involved in the research and development of expert systems throughout his career and is at present involved in expert database systems, intelligent decision support systems, and object oriented technology. He has written and contributed in several publications and papers. Since

1990 he is official expert and person of contact for AI/Expert Systems in his company.
