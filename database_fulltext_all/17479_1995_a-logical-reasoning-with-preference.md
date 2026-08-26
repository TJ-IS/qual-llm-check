---
otero_id: 17479
otero_key: "HNW8DVT4"
title: "A logical reasoning with preference"
authors: "S.K. Das"
year: "1995"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(94)00028-q"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# A logical reasoning with preference

S.K. Das

Artificial Intelligence Group, Department of Computer Science, QMW, University of London, Mile End Road, London E1 4NS, UK

## Abstract

In a decision making context, multiple choices of actions are usually offered to solve a particular problem. Consequently, the question of preferences among the actions will occur. The ordering of recommended actions by preference is made by taking into account the states of the universe of discourse. We develop here a logic $L_{p}$ for reasoning about preferences in such circumstances. The language of the logic is propositional extended with a special binary relation of preference among formulae. The model theory of the logic is studied and the soundness and completeness theorem is established.

Keywords: Preference; Decision support system; Action; Logic

## 1. $\mathcal{L}_p$ informally

The study of concepts in which moral philosophers take an interest is categorized by von Wright [4] into three groups: deontological, value-concepts and anthropological. The notion of preference or betterness belongs to the group of value-concepts and holds a prominent place in decision making context. There are several application domains where preference need to be represented, for example, medicine and economics. In particular, in oncology there are preferences which if contravened may rise hazardous situation, for example, there is a preference to administer the drug taxol before cisplatin than after in the treatment of cancer [3]. Therefore, a formal study of preference is recognised as an important goal yet to be attempted. To achieve this we construct a formal logic of preference in this paper.

There are several types of preferences that are relative to state or circumstances. For example, in the treatment of deep-vein thrombosis, preferring subcutaneous administration of heparin to intravenous administration is a preference between two different kinds of action. On the other hand, preferring health to illness is a preference between two properties. Considering the importance of actions and properties in the context of preference, we study them first more formally.

The description of the universe of discourse has two aspects: static and dynamic. The static aspect of the universe of discourse is described by properties (e.g., the patient has a cold) and dynamic aspects by occurrences. An occurrence is either an event (e.g., the patient is given an injection) or a process (e.g., the patient is on drug treatment). Some occurrences involve animate agents (i.e., decision makers) performing actions. We shall not consider the cases of occurrences where animate agents do not perform any actions. If an action is taken then an occurrence occurred and, conversely, if an occurrence occurs then an action is involved. We use the two terms action and occurrence synonymously. In light of this discussion, we consider the set of all propositional symbols of $L_{p}$ divided into properties and actions.

A state of a universe of discourse is represented by a set of sentences and each state has one or more models. Some of the property and action symbols of a universe of discourse are true in a state and the rest are false. Thus, if the symbol $\phi$ represents a property and $\phi$ is present in a state then $\phi$ is true in the state or if $\neg\phi$ is present in a state then $\phi$ is not true in the state. Similarly, if $\alpha$ is an action and $\alpha$ is present in a state of the universe of discourse then $\alpha$ is taken or if $\neg\alpha$ is present in a state then $\alpha$ is not taken in the state.

Now consider a state which has a sentence that either action $\alpha$ or action $\beta$ is required to be taken on the present state and $\alpha$ is preferred to $\beta$ . Modelling a state in the presence of such sentences would be to consider all possible transitions from the present state and make an ordering by preference among all possible new states. In this case, there are two possible transitions from the present state and each transition yields a new state. One new state is obtained by taking the action $\alpha$ and represented simply by state $\alpha$ . The other is by taking the action $\beta$ and represented by state $\beta$ . According to our preference among $\alpha$ and $\beta$ we should prefer the former transition and not the latter. If we say that a property $\phi$ is preferred to another property $\psi$ then we prefer to bring about $\phi$ rather than $\psi$ . A property or a sentence is brought about by taking one or more suitable actions. Note that if a particular state contains more than one of the above type of preferential sentences then required actions are executed simultaneously to transit to a new state.

The notion of preference is introduced into $\mathcal{L}_p$ through the binary relation ' $p$ ' among propositional formulae. A tuple $(F,G)$ of propositional formula is in relation $p$ , that is

$$
\wp (F, G),
$$

then this is interpreted as F is preferred to G. For example, if $\alpha$ and $\beta$ are actions then $\varphi(\alpha,\beta)$ is interpreted as the action $\alpha$ is preferred to $\beta$ .

To generalise what has been said in the previous paragraph and also to provide a semantics of the relation ‘ $\wp$ ’, suppose at a particular state of a universe of discourse the formula $F$ is preferred to $G$ , that is, $\wp(F,G)$ holds. There are two possible transitions from the present state will yield two different new states. In one of these new states $F$ is true and we shall synonymously call it the state $F$ . In the other new state $G$ is true and we shall synonymously call it the state $G$ . The former transition is preferred to the latter.

Different kinds of preferences can be categorized as follows: Suppose we have a universe of discourse and F and G are formulae. Then F is preferred to G

\- unconditionally if a transition to the state $F$ is favoured to the state $G$ from every state of the universe of discourse. For example, health is preferred to illness.

\- preconditionally in a state if a transition to $F$ from the state is favoured to $G$ on condition that the state agrees in a certain specified feature called preconditions. For example, if the patient is over 50 years of age and there are no exceptional circumstances then tamoxifen is preferred to adjuvant chemotherapy. Preconditional preferences are the most useful ones in decision making context.

\- postconditionally in a state if a transition to $F$ from the state is favoured to $G$ on condition that the state $F$ agrees in a certain specified feature called postconditions. Postconditions are also known as integrity constraints.

The building process of axiom schemes and semantics of $L_{p}$ is in two steps starting from the propositional logic L presented in the following section. The logic L is then extended to the logic of preference $L_{p}$ presented in Section 3.

## 2. Logic of propositions

Suppose P is the set of all propositions divided into properties and events. The domain P is extended to the domain of propositional formulae as follows:

\- a proposition from $\mathcal{P}$ is a propositional formula.

\- $\neg F, F \land G$ are propositional formulae, where $F$ and $G$ are propositional formulae.

Other logical connectives are defined using $\neg$ and $\wedge$ as follows:

$$
\begin{array}{l}F \lor G \equiv \neg (\neg F \land \neg G),\\F \rightarrow G \equiv \neg (F \land \neg G),\end{array}
$$

We have three axiom schema

$$
F \rightarrow (G \rightarrow F).\tag{1}
$$

$$
\big (F \to (G \to H) \big) \to \big ((F \to G) \to (F \to H) \big).\tag{2}
$$

$$
(\neg G \rightarrow \neg F) \rightarrow (F \rightarrow G).\tag{3}
$$

$$
\text { The   modus   ponens   rule }
$$

$$
i f F a n d F \rightarrow G t h e n G.\tag{4}
$$

is the only rule of inference. Its corresponding standard model theoretic semantics $\mathcal{M}$ is defined as a subset of $\mathcal{P}$ such that if $p$ is in $\mathcal{M}$ then $p$ is true else $p$ is false. For an arbitrary formula $F$ , $\vDash_{\mathcal{M}} F$ is defined by means of the following rules: Rule 1. $\vDash_{\mathcal{M}} p$ iff $p \in \mathcal{M}$ .

Rule 2. $\models_{\mathcal{M}} \neg F$ iff $\neq_{\mathcal{M}} F$ .

Rule 3. $\vDash_{\mathcal{M}}(F \wedge G)$ iff $\vDash_{\mathcal{M}} F$ and $\vDash_{\mathcal{M}} G$ . A model $\mathcal{M}$ is a model for a set of formula $\mathcal{S}$ if $\vDash_{\mathcal{M}} F$ , for every $F$ in $\mathcal{S}$ . A model $\mathcal{M}$ for a set of formula $\mathcal{S}$ is minimal if there is no other model of $\mathcal{S}$ which is a subset of $\mathcal{M}$ . We have the following theorem in propositional logic:

Theorem 1. If $\mathcal{S}$ is a set of formulae in $\mathcal{L}$ then $\mathcal{S} \vdash_{\mathcal{L}} F$ if and only if $\mathcal{S} \models_{\mathcal{M}} F$ , for every minimal model $\mathcal{M}$ of $\mathcal{S}$ . Proof. Please consult any text book of mathematical logic.

The minimal models for a set of formulae $\mathcal{S}$ can be constructed by following these steps:

Step 1. Replace each member of S by their equivalent conjunctive normal form.

Step 2. Replace a member of S by its conjuncts. Step 3. A set of consistent models are formed so that each model contains one or more propositional literals from each member of S.

Step 4. Remove all negated atoms from each model.

Step 5. Exclude a model which is not minimal.

In the case of propositional logic, a state is represented by its minimal models. We illustrate this by considering this example.

Example 1. Suppose, at a particular occasion the state of a universe of discourse is given by the following set S:

$$
\begin{array}{c}\mathcal {S} = \left\{p ^ {\prime}, \neg (p ^ {\prime} \wedge R _ {-} q), \right.\\\left(R _ {-} p \vee R _ {-} s\right) \wedge \neg (R _ {-} p \wedge R _ {-} s),\\R _ {-} p \rightarrow R _ {-} q \vee R _ {-} r \},\end{array}
$$

where $p'$ , p, q, r, s are actions and a propositional symbol of the type $R_{x}$ is read as 'x is recommended'. Note that each $R_{x}$ is a property and the presence of only x implies that action x has been taken. Ideally R should be replaced by a model operator [2]. We now construct a possible transition from this state using the concept of minimal model. A minimal model of a state provides us exactly those information which are true in that state. The steps for constructing the minimal models are as follows:

$$
\begin{array}{l} \left\{p ^ {\prime}, \neg p ^ {\prime} \vee \neg R _ {-} q, \right. \\ \qquad \left(R _ {-} p \vee R _ {-} s\right) \wedge \left(\neg R _ {-} p \vee \neg R _ {-} s\right), \\ \qquad \neg R _ {-} p \vee R _ {-} q \vee R _ {-} r \}, \\ \left\{p ^ {\prime}, \neg p ^ {\prime} \vee \neg R _ {-} q, R _ {-} p \vee R _ {-} s, \right. \\ \qquad \neg R _ {-} p \vee \neg R _ {-} s, \neg R _ {-} p \vee R _ {-} q \vee R _ {-} r \}, \\ \left\{p ^ {\prime}, \neg R _ {-} q, R _ {-} p, \neg R _ {-} s, R _ {-} r \right\}, \\ \left\{p ^ {\prime}, \neg R _ {-} q, R _ {-} s, \neg R _ {-} p \right\}, \\ \left\{p ^ {\prime}, \neg R _ {-} q, R _ {-} s, \neg R _ {-} p, R _ {-} r \right\}, \\ \left\{p ^ {\prime}, R _ {-} p, R _ {-} r \right\}, \\ \left\{p ^ {\prime}, R _ {-} s \right\}, \\ \left\{p ^ {\prime}, R _ {-} s, R _ {-} r \right\}, \\ \left\{p ^ {\prime}, R _ {-} p, R _ {-} r \right\}, \\ \left\{p ^ {\prime}, R _ {-} s \right\}. \end{array}
$$

Each of the above two minimal models corresponds to a possible transition. Therefore, the minimal model $\{p', R_{-}p, R_{-}r\}$ suggests that a possible transition from the present state is by taking actions p and r. The other model is interpreted in a similar manner. There is no preference for one to the other.

## 3. Logic of preference

Into the language of the logic $\mathcal{L}$ , we now introduce sentences involving $\wp(F,G)$ , where $F$ and $G$ are propositional formulae. The domain $\mathcal{P}$ of propositional formulae is extended to the domain $\mathcal{P}_p$ of preferential formulae as follows:

\- a proposition is a preferential formula.

\- $\wp(F, G)$ is a preferential formula, called a preferential atom, where $F$ and $G$ are propositional formulae.

\- $\neg F$ , $F \wedge G$ are preferential formulae, where $F$ and $G$ are preferential formulae.

Other logical connectives are defined earlier. The system of logic of preference $L_{p}$ is based on the logic L and contains the following axioms and inference rule: Axioms (1), (2) and (3) and inference rule (4), where F, G and H are preferential formulae.

(D5) The relation of preference is asymmetry. In other words, if one state is preferred to another then the second state is not preferred to the first.

$$
\wp (F, G) \rightarrow \neg \wp (G, F).\tag{5}
$$

(D6) The relation of preference is transitive. In other words, if one state is preferred to another and this second is preferred to a third state then the first state is preferred to the third state.

$$
\wp (F, G) \wedge \wp (G, H) \rightarrow \wp (F, H).\tag{6}
$$

The above two axioms are clear and uncontroversial. The following axiom excludes the possibility of having both the formulae concerned in the new state:

(D7) If one state F is preferred to another state G then the state $F \wedge \neg G$ is preferred to the state $\neg F \wedge G$ , and vice versa.

$$
\wp (F, G) \leftrightarrow \wp (F \wedge \neg G, \neg F \wedge G).\tag{7}
$$

The justification for the above axiom is given as follows. We have four possibilities:

1. Assume that both $F$ and $G$ hold in the present state. If $F$ is preferred to $G$ then, obviously, it is preferred to have a change from the present state to $F \wedge \neg G$ than to $\neg F \wedge G$ .

2. When the present state is $F \wedge \neg G$ then it is preferred to continue this state than lose F and get G.

3. When the present state is $\neg F \land G$ then it is preferred to a change from $\neg F$ to $F$ and $G$ to $\neg G$ rather than remaining in the present state.

4. If neither F nor G hold in the present state then a preference of F to G means to get F and continue to be without G.

Therefore, in all four cases, to say that F is preferred to G is equivalent to saying that the state $F \wedge \neg G$ is preferred to $\neg F \wedge G$ .

The following two axioms makes it possible to transform any given preferential formulae into a standard form to which the model theoretic evaluation of an arbitrary formula can be carried out: (D8) Disjunctive preferences are conjunctively distributive.

$$
\begin{array}{l} \wp (F \lor G, H) \leftrightarrow \wp (F, H) \land \wp (G, H), \\ \wp (F, G \lor H) \leftrightarrow \wp (F, G) \land \wp (F, H). \end{array}\tag{8}
$$

Although a disjunction inside a preferential atom is interpreted as exclusive, the above two axioms do not reflect this property. The first axiom of (8) should have been of the form $\wp(F \vee G, H) \leftrightarrow \wp(F \wedge \neg G, H) \wedge \wp(G \wedge \neg F, H)$ and the second axiom should have been in a similar form. But this exclusive behaviour of disjunction will be taken into account when we consider minimal models rather than any models for computing transitions.

Two actions (resp. properties) p and q can be asserted as equivalent, that is, propositions p and q are equivalent (written as $p \leftrightarrow q$ ) if and only if the cost, benefit, outcome, etc. involved to carry out (resp. bring about) p is exactly the same as that of q. The equivalence between two arbitrary formulae can be defined in a usual manner taking into account the definition of equivalence between propositions. Note that F and G are equivalent then neither of these two formulae can be preferred over the other, that is, neither $\wp(F,G)$ nor $\wp(G,F)$ holds. Based on this definition of equivalence, in addition to modus ponens, the logic $L_{p}$ will have the following rule of inference which is self-explanatory:

$$
i f \wp (F, G), F \leftrightarrow F ^ {\prime} a n d G \leftrightarrow G ^ {\prime} t h e n \wp (F ^ {\prime}, G ^ {\prime}).\tag{9}
$$

We now extend the idea of minimal models in the presence of preferential sentences. Constructing a minimal model in such situations will also mean constructing a possible transition from the present state but there will be a preference among all transitions. Consider the set of all propositional symbols as well as preferential atoms of the form $\varphi(F,G)$ , where F and G are conjunction of propositional literals. A preferential model theoretic semantics Mp is defined as a subset of this set with the following properties:

\- If $\wp(F,G)$ is in $\mathcal{M}p$ then $\wp(G,F)$ is not in $\mathcal{M}p$ .
- If $\wp(F,G)$ and $\wp(G,H)$ are in $\mathcal{M}p$ then $\wp(F,H)$ is also in $\mathcal{M}p$ .

The two restrictions correspond to axioms of asymmetry and transitivity respectively. Therefore, a preferential model has the form

$$
\left\{p _ {1}, \dots , p _ {m}, \wp (F _ {1}, G _ {1}), \dots , \wp (F _ {n}, G _ {n}) \right\}, m + n > 0,
$$

where each $F_{i}$ and $G_{j}$ is a conjunction of propositional literals. If $p$ is either a propositional or preferential atom and if $p$ is in $\mathcal{M}p$ then $p$ is true else $p$ is false. For an arbitrary formula $F$ , $\models_{\mathcal{M}} F$ is defined using these rules:

Rule 1. $\models_{\mathcal{M}_p} p$ iff $p \in \mathcal{M}_p$ .

Rule 2. $\models_{\mathcal{M}^p}\wp(F,G)$ iff either $\wp(F,G)\in\mathcal{M}_p$ or $\wp(F',G')\in\mathcal{M}_p$ , where $F\leftrightarrow F'$ and $G\leftrightarrow G'$ .

$$
\text { Rule   3. } \models_ {\mathcal {A} _ {n}} \neg F \text {   iff   } * * * _ {\mathcal {A} _ {n}} F.
$$

$$
\text { Rule   4. } \vDash_ {\mathcal {M} _ {n}} ^ {p} (F \wedge G) \text {   iff   } \vDash_ {\mathcal {M} _ {n}} ^ {p} F \text {   and   } \vDash_ {\mathcal {M} _ {n}} G.
$$

Rule 5. $\models_{\mathcal{M}_p}\wp(F,G)$ iff $\models_{\mathcal{M}_p}\wp(F\land\neg G,\neg F\land G)$ . Rule 6. $\models_{\mathcal{M}_p}\wp(F\lor G,H)$ iff $\models_{\mathcal{M}_p}\wp(F,H)\land\wp(G,H)$ .

$$
\begin{array}{l l} \text { Rule } 7. & \vDash_ {\mathcal {M} _ {p}} \wp (F, G \vee H) \quad \text { iff } \quad \vDash_ {\mathcal {M} _ {p}} \wp (F, G) \wedge \\ \wp (F, H). \end{array}
$$

The preferential models for a set of formulae S can be constructed by following these steps:

Step 1. Apply the following transformations on each $\wp(F,G)$ occurring in $\mathcal{S}$ :

(a) Replace $\wp(F,G)$ by $\wp(F \wedge \neg G, \neg F \wedge G)$ . For example, replace $\wp(p \wedge q, \neg r)$ by $\wp(p \wedge q \wedge \neg \neg r, \neg r \wedge \neg (p \wedge q))$ .

(b) Replace each of $F \wedge \neg G$ and $\neg F \wedge G$ by its equivalent disjunctive normal form. For example, the last expression by $\wp(p \wedge q \wedge r, (\neg p \wedge \neg r) \vee (\neg q \wedge \neg r))$ .

(c) Transform the resultant formula to a conjunction by the rule of conjunctive distributivity. For example, the last expression by $\wp(p \wedge q \wedge r, \neg p \wedge \neg r) \wedge \wp(p \wedge q \wedge r, \neg q \wedge \neg r)$ .

Step 2. Replace each member of S by their equivalent conjunctive normal form.

Step 3. Replace a member of S by its conjuncts. Step 4. A set of consistent models are formed so that each model contains one or more propositional or preferential literals from each member of S.

Step 5. Extend each model by applying the axioms (6).

Step 6. Exclude a model which is inconsistent and does not satisfy the asymmetry property.

Step 7. Remove all negated prepositional and negated preferential atoms from each model.

Theorem 2. If $\mathcal{S}$ is a set of formulae in $\mathcal{L}_p$ then $\mathcal{S} \vdash_{\mathcal{L}_p} F$ if and only if $\vDash_{\mathcal{M}_p} F$ , for every preferential model $\mathcal{M}_p$ of $\mathcal{S}$ .

Proof. On proof theoretic side we have the axioms and inference rules of $L_{p}$ and on model theoretic side we have steps for constructing preferential models and rules for evaluating truth values with respect to these models. To prove the theorem, it is enough to show a correspondence between these two sides. This correspondence will guarantee that the derivation in $L_{p}$ is truth preserving. Conversely, the definition of validity of the rules for determining truth values with respect to preferential models implies a valid derivation step of a proof in $L_{p}$ .

First of all the correspondence between the axioms (1), (2), (3) and the inference rule (4) correspond to the rules 1, 3, 4 for determining truth values. This comes from the model theoretic and proof theoretic equivalence of propositional logic. A formula which can be deduced from axiom (6) is true in preferential models by means of step 5 for preferential model construction, and vice versa. Similarly, axiom (5) corresponds to step 6 together with rule 3, axiom (7) corresponds to step 1(a) together with rule 2, axioms of (8) correspond to step 1(c) together with rules 6 and 7. The inference rule (9) corresponds to step 2 together with rule 3. Hence, the theorem is established. □

Once we have a set of preferential models, for each of them, consider their propositional part $\{p_{1},\ldots,p_{m}\}$ if m>0 and retain only the minimal ones. Using these minimal models compute all possible transitions $\mathcal{T}_1, \ldots, \mathcal{T}_n$ from the present state. Now we shall develop a preference among these transitions. The transition $\mathcal{T}_i$ is preferred to $\mathcal{T}_j$ , $i \neq j$ , if for every $\wp(F, G)$ such that $\mathcal{S} \models \wp(F, G)$ then $\models_{\mathcal{T}_i} F$ and $\models_{\mathcal{T}_j} G$ . Therefore, the set $\mathcal{S}$ yields a set of transitions and a preference ordering relation among them. Let us now extend example 1.

Example 2. Suppose, at a particular occasion the state of a universe of discourse is given by the following set S:

$$
\begin{array}{c}\mathcal {S} = \left\{p ^ {\prime}, \neg (p ^ {\prime} \wedge R _ {-} q), \right.\\\left(R _ {-} p \vee R _ {-} s\right) \wedge \wp (R _ {-} p, R _ {-} s),\\R _ {-} p \rightarrow R _ {-} q \vee R _ {-} r \}.\end{array}
$$

The only difference between the set S in example 1 and above S is that $\neg(R_{-}p\land R_{-}s)$ is replaced by the preferential atom $\varphi(R_{-}p,R_{-}s)$ . The former stated that not both of the actions p and s can be recommended and the latter states that the recommendation of action p is preferred to the recommendation of action s. Applying step 1 on S we rewrite S as

$$
\begin{array}{r l}&{\mathcal {S} = \left\{p ^ {\prime}, \neg (p ^ {\prime} \land R _ {-} q), R _ {-} p \lor R _ {-} s, \right.}\\&{\quad \wp (R _ {-} p \land \neg R _ {-} s, \neg R _ {-} p \land R _ {-} s),}\\&{\quad \left. R _ {-} p \rightarrow R _ {-} q \lor R _ {-} r \right\}.}\end{array}
$$

The preferential models are

$$
\begin{array}{r l} & \mathcal {M} _ {p} ^ {1} = \big \{p ^ {\prime}, R _ {-} p, \wp (R _ {-} p \wedge \neg R _ {-} s, \neg R _ {-} p \wedge R _ {-} s), \\ & \qquad \qquad \qquad \qquad \qquad \qquad R _ {-} r \big \}, \\ & \mathcal {M} _ {p} ^ {2} = \big \{p ^ {\prime}, R _ {-} s, \wp (R _ {-} p \wedge \neg R _ {-} s, \neg R _ {-} p \wedge R _ {-} s) \big \}, \\ & \mathcal {M} _ {p} ^ {3} = \big \{p ^ {\prime}, R _ {-} s, \wp (R _ {-} p \wedge \neg R _ {-} s, \neg R _ {-} p \wedge R _ {-} s), \\ & \qquad \qquad \qquad \qquad \qquad R _ {-} r \big \}, \\ & \mathcal {M} _ {p} ^ {4} = \big \{p ^ {\prime}, R _ {-} s, \wp (R _ {-} p \wedge \neg R _ {-} s, \neg R _ {-} p \wedge R _ {-} s), \\ & \qquad \qquad \qquad \qquad R _ {-} r \big \}, \\ & \mathcal {M} _ {p} ^ {5} = \big \{p ^ {\prime}, R _ {-} p, R _ {-} s, \\ & \qquad \qquad \qquad \wp (R _ {-} p \wedge \neg R _ {-} s, \neg R _ {-} p \wedge R _ {-} s), \\ & \qquad \qquad \qquad R _ {-} r \big \}. \end{array}
$$

Considering the propositional part of each $M_{p}^{i}$ we obtain the following sets:

$$
\begin{array}{l} \left\{p ^ {\prime}, R _ {-} p, R _ {-} r \right\}, \\ \left\{p ^ {\prime}, R _ {-} s \right\}, \\ \left\{p ^ {\prime}, R _ {-} s R _ {-} r \right\}, \\ \left\{p ^ {\prime}, R _ {-} s, R _ {-} r \right\}, \\ \left\{p ^ {\prime}, R _ {-} s, R _ {-} p, R _ {-} r \right\}. \end{array}
$$

Retaining only the minimal ones, we obtain the following sets:

$$
\begin{array}{l} \mathcal {T} _ {1} = \left\{p ^ {\prime}, R _ {-} p, R _ {-} r \right\}, \\ \mathcal {T} _ {2} = \left\{p ^ {\prime}, R _ {-} s \right\}. \end{array}
$$

Each of the above two minimal models corresponds to a possible transition. Therefore $T_{1}$ suggests that a possible transition from the present state is by taking actions p and r. Now we have $\mathcal{S}\models\wp(R\_p\land\neg R\_s,\neg R\_p\land R\_s)$ and $\models_{T_{1}}R\_p\land\neg R\_s$ and $\models_{T_{2}}\neg R\_p\land R\_s$ . Therefore, the transition $T_{1}$ is preferred to $T_{2}$ . This is what one expects from S. In the propositional case, we did not achieve this preference due to the absence of the preferential sentence in S.

## 4. Discussion

The notion of preference among actions was an important aspect of the logic $L_{safe}$ [2] for reasoning about safety in decision support systems. Here we have studied the concept of preference in detail and developed a logic of preference $L_{p}$ . The main intended application is in medical decision support system although the logic is generic enough to be used in other areas of artificial intelligence where reasoning about preference is involved. An implemented proof procedure based on our formalisation of preference will essentially be nonmonotonic in nature due to the fact that order of preference can be altered on the arrival of new information.

Our work is based on the idea of [von Wright, 1963] but differs in a number of respects. First of all, our concept of preference is not somebody's preference rather a preference involving justifications, for example, test results, statistics, etc. We can represent somebody's preference directly into the knowledge base without any conditions attached to it. Although this kind of preference will be rare in the context of a decision support system where construction behind preferences involved justifications. The fifth axiom in [4] is

$$
\begin{array}{c} \wp (F, G) \leftrightarrow \wp (F \wedge H ^ {\prime}, G \wedge H) \\ \wedge \wp (F \wedge \neg H, G \wedge \neg H), \end{array}
$$

which corresponds to the above unconditional preference and therefore has not been considered in our theory of preference. Also, axioms of (8) are a simplified version of their counterpart.

Two possible enhancements of $L_{p}$ and their combinations are certainly worth considering. The first is to extend the present propositional $L_{p}$ to the first-order logic of preference. We do not see any immediate problems in this regard although the method for constructing preferential models will have to be extended. The second extension is to analyze the impact of time on states and how it changes modelling, transitions, etc. Suppose we introduce in $L_{p}$ the temporal modal operators as intervals $[i_{1}, i_{2}]$ where $i_{1}, i_{2}$ are integers or one of the symbols $\infty, -\infty$ . An operator $[i_{1}, i_{2}]$ governs the proposition p as

$$
\left[ i _ {1}, i _ {2} \right] p,
$$

which says that if p is a property, then p holds sometime during interval $[i_{1},i_{2}]$ or if p is an action then p is taken sometime during $[i_{1},i_{2}]$ . In general, if F is a formula then $[i_{1},i_{2}]F$ says that the formula F is true in the interval $[i_{1},i_{2}]$ .

When time is taken into consideration in representing a universe of discourse, the preference operator $\wp$ now governs a tuple of temporal formulae. Earlier in the non-temporal case, models of a state of the universe remain fixed until an action is taken. In the temporal case, models of a state of the universe of discourse change with time. We consider formulae involving $\wp([t_1,t_2]\alpha,[t_3,t_4]\beta)$ , $[t_1,t_2]\wp(p,q)$ , $\wp([t_1,t_2]\alpha,[t_3,t_4]\alpha)$ , and so on, where $\alpha$ and $\beta$ are actions and $p$ and $q$ are properties. These are interpreted respectively as action $\alpha$ during interval $[t_1,t_2]$ is preferred to action $\beta$ during interval $[t_3,t_4]$ , property $p$ is preferred to property $q$ sometime during the interval $[t_1, t_2]$ , action $\alpha$ is preferred during $[t_1, t_2]$ than $[t_3, t_4]$ , and so on. An example of sentences of the form $\wp([t_1, t_2] \alpha, [t_3, t_4] \alpha)$ is the following safety related requirement in a protocol for cancer management: 'The patient undergoes chemotherapy within four weeks and preferably within two weeks after the initial biopsy has been completed'. We need to add a set of axioms related to time, action and properties [2]. In addition to these, the axiom $\forall t_1 \forall t_2 ([t_1, t_2] \wp(F, G) \leftrightarrow \wp([t_1, t_2] F, [t_1, t_2] G))$ , should also be added to formalise the behaviour of preference in time intervals.

## Acknowledgements

The author would like to thank his colleagues in the RED project, especially, Peter Hammond of Imperial Cancer Research Fund for many helpful discussions on this work. The author is supported under the DTI/SERC project ITD 4/1/9053: Safety-Critical Systems Initiative.

## References

[2] J.F. Allen, 1984, Towards a general theory of action and time, North-Holland: Artificial Intelligence, Vol. 23, pp. 123–154.

[2] S.K. Das and J. Fox, 1993, A logic for reasoning about safety in decision support systems, Springer-Verlag: Proceeding of the 2nd European Conference on Symbolic and Quantitative Approaches to Reasoning and Uncertainty.

[3] E.K. Rowinsky, M.R. Gilbert, W.P. McGuire, et al., 1991, Sequences of taxol and cisplatin: A phase I and pharmacologic study, Journal of Clinical Oncology, Vol. 9, pp. 1692–1703.

[4] G.H. von Wright, 1963, The logic of preference, Edinburgh University Press.

![](/api/attachments/HNW8DVT4/fulltext/images/af6e52d5bdff4ac034b98ef5b644c8709d7f1321da0b65462904cbe8aef14f9f.jpg)  
Dr. Subrata K. Das is a Research Associate in the Department of Computer Science at Queen Mary and Westfield College, University of London. His research interest includes databases, symbolic decision theory, expert systems and applied non-classical logics. He is the author of the book Deductive Databases and Logic Programming.
