---
otero_id: 16988
otero_key: "MKNEXW3J"
title: "About assessing and evaluating uncertain inferences within the theory of evidence"
authors: "Thomas Kämpke"
year: "1988"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(88)90006-1"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# About Assessing and Evaluating Uncertain Inferences Within the Theory of Evidence

Thomas KÄMPKE

Forschungsinstitut für anwendungsorientierte Wissensverarbeitung (FAW) an der Universität Ulm, 7900 Ulm, FRG

Dealing with uncertainty of facts and rules in an inference system will be discussed. The assessment and evaluation of uncertainties will be done within Dempster's and Shafer's theory of evidence. The relation between this theory and classical probability theory will be stressed.

Keywords: Associated Random Variables, Belief Functions, Evidence, Inference Systems, Production Rules.

![](/api/attachments/MKNEXW3J/fulltext/images/b656b694efa646fbcbc95e5d99b33d2ff3839c3f4c77ae42a4c78191c84550f9.jpg)

Thomas Kämpfe is on the staff of the recently founded Forschungsinstitut für anwendungsorientierte Wissensverarbeitung (FAW) at the University of Ulm, W. Germany. He held positions at the Technical University of Aachen and at the University of Passau, both W. Germany, and had been visiting the University of California, Berkeley. His research interests include scheduling, optimization, stochastic modeling and decision analysis. He is currently involved in the development of an environmental information system. His papers appeared in Journal of Applied Probability, Operations Research, Advances in Applied Probability, Annals of Operations Research, and Communications in Statistics.

## 1. Introduction

The ability to handle uncertainty is a desirable feature of software systems in many areas including operations research. The variety of applications is too large to even think of a unified approach to this capability. But when e.g. restricting to (rule based) expert systems, some general properties of assessing uncertainty can be provided. A rule and the structure imposed on it to facilitate this assessment should be considered as a unity rather than as different items. As a consequence, a logically equivalent formulation of only a few rules holding with certainty may be something completely different in an uncertain environment. Examples are given below. However, the assessment should be done in a way agreeable to the case of certainty, also from an intuitive point of view. Furthermore we will require that numerical values assessed for uncertainties do interrelate in an intuitive way. Probability theory will play a major role in both the assessment and the evaluation of systems of inferences. Independence of uncertain facts and rules can be formulated analoge to independence of random variables and assuming independence where it is absent will be shown to result in a systematic bias. Monte Carlo simulation, esp. antithetic simulation, will be demonstrated to be one method of evaluating systems of uncertain inferences.

The theory of evidence has been developed by Dempster and later on by Shafer to model uncertain knowledge, called belief or evidence, about facts under consideration. These facts may e.g. be symptoms or a diagnosis in medical context. The basic idea behind the theory of evidence is a separation of disbelief in a fact from ignorance about it. This is motivated by the every day experience that evidence not supporting a fact does not necessarily support its opposite; the evidence at hand may be too weak to either decide in favour or against some fact. A simple example from [9]: suppose a vase has been excavated and an archaeologist has to decide whether it is ancient or a modern fake. In the beginning he might assign the value .1 - on the scale [0,1] - to either possibilities, because he finds some weak evidence for both of them. The value .8 will be assigned to a third alternative “not made up his mind”. Later evidence, such as a test of age, may be found to review the original evidence. (Of course, the discovery of the label “made in ...” will drastically clear the matter.) Updating evidence is a central issue of the theory of evidence. For a thorough treatise see [9].

More recently the theory of evidence has been carried over to model not only facts, but also rules, see e.g. [1], [3], [6], [7] and [10]. The rules are like production rules (if...then...) from expert systems and they are thought of as uncertain as well. Up to date there seems to be no standard way to formalize uncertainty of inferences. Some thoughts about this will be presented in the sequel, beginning with notions from the Dempster–Shafer theory.

For a finite, non-empty set $\Theta$ , called frame of discernment, a basic probability assignment is a function $m: P(\Theta) \to [0,1]$ with $m(\Theta) = 0$ and $\sum_{A \in P(\Theta)} m(A) = 1$ , $P(\Theta)$ denotes the power set of $\Theta$ . The function $m$ may be considered as probability density prob of a set-valued random variable $X$ , where $\text{prob}(X = A) = m(A)$ , $A \in P(\Theta)$ . A frame of discernment can be seen as a set of possibilities, where exactly one of them is true, but it is unknown which one, in general. The value of $m$ for a set $A$ may be interpreted as the belief that the true possibility is in $A$ , but not in any subset of $A$ . The belief that the true possibility is in $A$ or any subset of $A$ is given by the belief function $\text{Bel}: P(\Theta) \to [0,1]$ with $\text{Bel}(A) := \sum_{B \subseteq A} m(B)$ .

For a given belief function Bel the corresponding probability assignment m is given by

$$
m (A) = \sum_ {B \subseteq A} (- 1) ^ {| A - B |} \operatorname{Bel} (B).
$$

Thus, stating belief functions is equivalent to stating probability assignments and a probability assignment $m$ will often be explicitly stated only for those sets $A$ with $m(A) > 0$ , called focal sets. Note that for any belief function $\operatorname{Bel}(A) + \operatorname{Bel}(A^c) \leq 1$ ; the inequality may be strict as in the example above with $A = \{\text{vase ancient}\}$ and $A^c = \{\text{vase not ancient}\}$ .

For two belief functions with probability assignments $m_{1}$ and $m_{2}$ over the same frame of discernment $\Theta$ the orthogonal sum $\oplus$ is defined, see [9], as

$$
\begin{array}{l} m _ {1} \oplus m _ {2} (C) := \sum_ {A, B \text { with } A \cap B = C} m _ {1} (A) m _ {2} (B) \\ / \sum_ {A, B \text { with } A \cap B \neq \varnothing} m _ {1} (A) m _ {2} (B). \end{array}
$$

$\oplus$ is derived from $m_{1}$ and $m_{2}$ with corresponding random variables being stochastically independent, see [10, p. 45]. $m_{1} \oplus m_{2} = m_{2} \oplus m_{1}$ and $\oplus$ is associative if applied to more than 2 operands. $\oplus$ facilitates updating belief by combining belief from “various sources”.

In the following, frames of discernment will describe the validity of one or several propositions. The simplest case will be $\Theta=\{A,\neg A\}$ , where A stands for: proposition A holds, and $\neg A$ stands for: proposition A does not hold. To simplify the notation, we deliberately use the same symbol for a proposition itself and for the proposition being true. The context will always make clear the difference. The joint validity of several propositions will be described within the Cartesian product of the underlaying frames of discernment.

To view propositions within a narrowing or widening frame of discernment, we will make use of the extension and projection - sometimes called restriction as in [6] or marginal as in [3] - of a belief function: comp. [9]. Let $m$ be the probability assignment of a belief function over a frame $\Theta 1$ and $\Theta 2$ be another frame. The extension of $m$ onto $\Theta 1 \times \Theta 2$ is given by

$$
\left(\operatorname{ext} _ {\Theta 2} m\right) (A, \Theta 2) := m (A),
$$

$A \in P(\Theta 1)$ . For a belief function Bel on $\Theta 1 \times \Theta 2$ the projection onto $\Theta 1$ is defined by

$$
(\operatorname{pr} _ {\Theta 1} \operatorname{Bel}) (A) := \operatorname{Bel} (A, \Theta 2),
$$

$A \in P(\Theta1)$ . For properly chosen factors $\Theta1$ and $\Theta2$ the projection of the extension of a belief function is the original belief function, while the extension of the projection is generally not; comp. [3].

## Modelling Rules

Suppose two propositions A and B and the rule $R: A \rightarrow B$ (if A then B) are given. We further suppose a belief function $\mathbf{Bel}_A$ for $A$ to be given by

$$
\begin{array}{l} m _ {A} (A) = p _ {1}, \\ m _ {A} (\neg A) = p _ {2}, \\ m _ {A} (\Theta A) = p _ {3}, \end{array}
$$

with $p_1 + p_2 + p_3 = 1$ , $p_i \geq 0$ , and $\Theta A = \{A, \neg A\}$ . For the rule, a belief function $\operatorname{Bel}_{A \to B}$ on $\Theta A \times \Theta B$ will be given, the elements of $\Theta A \times \Theta B$ being denoted by e.g. $(A, \neg B)$ and a subset of $\Theta A \times \Theta B$ such as $\{(A, B), (\neg A, B), (\neg A, \neg B)\}$ will be written in disjunctive form: $(A, B) \vee (\neg A, B) \vee (\neg A, \neg B)$ .

$$
\begin{array}{l} m _ {A \to B} ((A, B) \vee (\neg A, B) \vee (\neg A, \neg B)) = q _ {1}, \\ m _ {A \to B} (\Theta A \times \Theta B) = q _ {2}, \end{array}
$$

with $q_{1} + q_{2} = 1$ and $q_{i}\geq 0$ .

Applying rule R to proposition A, which is equivalent to the modus ponens for facts and rules with certainty, will be facilitated by forming $Bel_{A} \oplus Bel_{A \to B}$ , precisely $(\text{ext}_{\theta B}\text{Bel}_{A}) \oplus \text{Bel}_{A \to B}$ (obvious extensions and projections will be omitted):

$$
\begin{array}{l} m _ {A} \oplus m _ {A \to B} ((A, B)) = p _ {1} q _ {1}, \\ \quad ((\neg A, \Theta B)) = p _ {2}, \\ \quad ((A, B) \vee (\neg A, B) \vee (\neg A, \neg B)) = p _ {3} q _ {1}, \\ \quad ((A, \Theta B)) = p _ {1} q _ {2}, \\ \quad (\Theta A \times \Theta B)) = p _ {3} q _ {2}. \\ \text { Thus, } \operatorname{Bel} _ {B} := = \operatorname{pr} _ {\Theta B} ((\operatorname{ext} _ {\Theta B} \operatorname{Bel} _ {A}) \oplus \operatorname{Bel} _ {A \to B}) \\ \text { given   by } \\ m _ {B} (B) = p _ {1} q _ {1}, \\ \quad (\neg B) = 0, \\ \quad (\Theta B) = 1 - p _ {1} q _ {1}. \end{array}
$$

We observe that $\mathbf{pr}_{\Theta A}((\mathrm{ext}_{\Theta B}\mathrm{Bel}_A)\oplus \mathrm{Bel}_{A\to B}) =$ $\mathrm{Bel}_A$ , i.e. applying the rule $A\to B$ to $A$ does not effect the initial belief in $A$ . Furthermore, the probability assignment of $\mathbf{pr}_{\Theta B}(\mathrm{Bel}_{A\to B})$ concentrates all mass in $\Theta B$ ; $m(\Theta B) = 1$ . Hence, from the formulation of the rule, there is complete ignorance about $B$ . Thus, the rule itself (!) neither implies any belief in the consequent $B$ nor does it bias the belief in the antecedent $A$

Note furthermore, that the application of a rule to a fact is given by $\oplus$ . We assume that facts are independent from rules in the sense described above.

For implied evidence the following monotonicity property holds.

Lemma 1. Given an arbitrary belief function $Bel_{1}$ for $B$ . If there is independent evidence for $B$ , denoted $Bel_{B}$ , implied by some fact $A$ and the rule $A \to B$ , then $(Bel_{1} \oplus Bel_{B})(B) \geq Bel_{1}(B)$ and $(Bel_{1} \oplus Bel_{B})(\neg B) \leq Bel_{1}(\neg B)$ .

By the belief function $Bel_{B}$ there is no disbelief in B, $\operatorname{Bel}_{B}(\neg\mathbf{B})=0$ . This gave rise to different ways to model rules. Lee and Shin [7] assess the belief $Bel_{LS}$ in a rule by

$$
\begin{array}{r l} & m _ {\mathrm{LS}} ((A, B) \vee (\neg A, B) \vee (\neg A, \neg B)) = q _ {1}, \\ & ((A, \neg B)) = q _ {2}, \\ & (\Theta A \times \Theta B) = q _ {3}, \\ & q _ {1} + q _ {2} + q _ {3} = 1, \quad q _ {i} \geqslant 0. \end{array}
$$

Thus, $\mathsf{pr}_{\Theta A}((\mathsf{ext}_{\Theta B}\mathsf{Bel}_A)\oplus \mathsf{Bel}_{\mathsf{LS}})(A)\neq$ $\mathsf{Bel}_A(A)$ , for $q_{2} > 0$ , the belief in $A$ "before" applying the rule differs from that "after". This seems strange, the rule should not bias the initial belief. Moreover, $(\mathsf{pr}_{\Theta B}\mathsf{Bel}_{\mathsf{LS}})(\neg B) = q_2$ . For $q_{2} > 0$ the rule itself - without being invoked - results in a disbelief in the consequent $B!$ Similar effects hold within the approach by Eddy and Pei [3]. Esp. a disbelief in $B$ seems hard to justify, because the rule only states sufficiency, not necessity, of $A$ for $B$ . Hence, all probability mass which is not assigned to the belief in a rule, will be committed to ignorance about it.

To conclude disbelief in a proposition, we require a rule whose consequent is the negation of the proposition. For example, a proposition $C$ might - with uncertainty - imply $\neg B$ , i.e. besides $A \to B$ there might be another rule $C \to \neg B$ . Not to violate the intuition behind implications, it seems reasonable to assume that it takes two production rules to conclude belief and disbelief in a proposition.

This immediately gives rise to the occurrence of contradictions, because a proposition and its negation may both be concluded with a certain degree of belief. Dealing with contradictions will be an issue of evaluating inferences.

We assume that propositions which do not appear as consequences in any rule in a system of inferences are independent, meaning that their set-valued random variables are stochastically independent. The independence may equivalently be stated without random variables. E.g. two propositions A and B may be called (evidentially) independent, iff

$$
\begin{array}{r l} \mathbf {B e l} _ {\Theta A \times \Theta B} = & \mathrm{ext} _ {\Theta B} (\mathbf {p r} _ {\Theta A} \mathbf {B e l} _ {\Theta A \times \Theta B}), \\ & \oplus \mathrm{ext} _ {\Theta A} (\mathbf {p r} _ {\Theta B} \mathbf {B e l} _ {\Theta A \times \Theta B}), \end{array}
$$

i.e. the joint belief in A and B is the orthogonal sum of the projected belief functions. Elementary applications of extensions and of $\oplus$ lead to

Lemma 2. Let $A$ and $B$ be independent propositions. Then

$$
\begin{array}{l l} (a) & B e l (A \lor B) = B e l (A) + B e l (B) - \\ & B e l (A) B e l (B), \\ & B e l (\neg (A \lor B)) = B e l (\neg A) B e l (\neg B). \end{array}
$$

$$
\begin{array}{l l} (b) & B e l (A \wedge B) = B e l (A) B e l (B), \\ & B e l (\neg (A \wedge B)) = B e l (\neg A) + B e l (\neg B) - \\ & B e l (\neg A) B e l (\neg B). \end{array}
$$

(E.g. $A \vee B$ is a short notation for $(A, B) \vee (\neg A, B) \vee (A, \neg B)$ within the frame $\Theta A \times \Theta B$ .)

Furthermore, elementary calculations show that the equations of lemma 2 are extreme in the following sense.

Lemma 3. Let $A$ and $B$ be propositions, possibly dependent. Then

(a) $Bel(A \land B) + Bel(A \lor B) \geq Bel(A) + Bel(B)$ ,
(b) $Bel(\neg(A \land B)) + Bel(\neg(A \lor B)) \geq Bel(\neg A) + Bel(\neg B).$

Rules with uncertainty are sometimes, as in [7], simplified to the form $A_1 \wedge \ldots \wedge A_n \to B$ , i.e. the antecedent is a conjunction of propositions while the consequent is a single one. A given rule such as $A \to (B \wedge C)$ is substituted by the two rules $A \to B$ and $A \to C$ . This is of course reasonable within certain facts and rules. But it seems difficult to decompose rules within uncertainty. It is not obvious how to assess the belief functions of the single rules from the given one. Moreover, it seems impossible to combine single beliefs to the joint one for $B \wedge C$ , because the single rules have the same antecedent, are thus dependent, and thus $\oplus$ is not the proper operation of combination. We will hence not decompose in the modelling process. However, whenever necessary, we will introduce propositions such as $D := B \wedge C$ so that a given rule may formally be viewed as one having only a single proposition as consequent. This serves to simplify the terminology.

There is another difference between production systems with certainty and those with uncertainty. Consider for example 4 propositions A, B, C and D related by the rules $R1: A \rightarrow (B \vee C)$ , $R2: B \rightarrow D$ , and $R3: C \rightarrow D$ :

$$
\begin{array}{c} \text { A } \longrightarrow \text { B } \vee \text { C } \\ \downarrow \quad \downarrow \\ \text { D } \end{array}
$$

If facts and rules hold with certainty, then D holds whenever A holds, the rule $A \rightarrow D$ can be derived. But if facts and rules contain uncertainty, rules R2 and R3 can not be invoked without further assumptions: the belief in $B \vee C$ , implied by R1, does not tell to what degree there is belief in B resp. C alone. Even if B and C were known to be independent, there are infinitely many belief functions for B and C which lead to the given belief in $B \vee C$ , comp. lemma 4. We will not pursue any questions of “completeness” here.

Lemma 4. Let $B$ and $C$ be independent propositions whose disjunction has the known belief function $Bel(B \vee C) = p \in (0,1)$ and $Bel(\neg (B \vee C)) = q \in [0,1), p + q \leq 1$ . Then there are infinitely many belief functions for $B$ and $C$ leading to the given one for $B \vee C$ .

Proof. For $p \in (0, 1)$ select $p_B \in (0, p)$ and set $p_C := (p - p_B) / (1 - p_B)$ , $q_B := 1 - p_B$ , and $q_C := q / q_B = q / (1 - p_B)$ . The belief functions

$$
\begin{array}{l l} \operatorname{Bel} (B) = p _ {B} & \text { and } \\ \operatorname{Bel} (\neg B) = q _ {B} & \text { Bel } (\neg C) = q _ {C} \end{array}
$$

have - by lemma 2 - the desired property. Because $p_B$ is arbitrary in $(0, p)$ , there are infinitely many of such functions.

## 3. Evaluating Uncertain Inferences

For the moment we assume that no contradictions may occur. Later on, this assumption will be dropped. Suppose a system of facts and rules without “cycles” is given, i.e. there are no chains leading back to a former fact such as $A \rightarrow B \rightarrow C \rightarrow \ldots \rightarrow A$ .

As proposed in [6], an inference system may be considered as a reliability network, a directed graph with propositions corresponding to nodes and rules to arcs. The reliability probability of an arc (node) is the belief in the corresponding rule (fact). Remember that the initial propositions $A1, \ldots, An$ – those which are not consequences in any rule – were assumed to be independent. Then holds, see [6]:

Theorem 1. The belief in a proposition B is the reliability probability $p_{B}$ of node B:

$$
\begin{array}{c} B e l _ {B} (B) = p r _ {\Theta B} \big (B e l _ {A 1} \oplus \ldots \oplus B e l _ {A n} \oplus B e l _ {R 1} \oplus \ldots \\ \oplus B e l _ {R m}) (B) = p _ {B}, \end{array}
$$

with $\{R1,\ldots ,Rm\}$ being the set of all rules of the system.

Of course the components of the orthogonal sum of theorem 1, which do not play a role for B, may be omitted, though it is generally difficult to tell what those components are. To simplify the calculations for a belief function of some proposition, one might derive it from all its antecedents only. Note that the antecedents leading to a proposition need not be evidently independent. This is due to several antecedents possibly depending on the same proposition. We do not require the graph of the reliability network to be an intree in order to allow the same piece of evidence to be used in several antecedents. This is important from the applicational point of view. Reusing evidence may very well fit a domain expert's paradigm of drawing conclusions (such as in medical context). For example: the 4 propositions A, B, C and D may be related by the rules R1: $A \rightarrow B$ , R2: $C \rightarrow B$ , R3: $B \rightarrow D$ , and R4: $C \rightarrow D$ :

![](/api/attachments/MKNEXW3J/fulltext/images/d9e36854abd5d2c3483198b08fe3a36d9eb39696f29c100f37c739434c9f044f.jpg)

If the belief in D is supposed to be calculated from the belief in B and C, then we must take into account the dependence of B and C. If for instance the belief in A and C is .9 and the belief in all 4 rules is .8, then the resulting belief in D is .946. If B and C are assumed to be independent, then the belief in D increases to .952. For more complex inference networks larger deviations have to be expected.

The evaluation of the belief in a fact may generally be done by assigning each fact A resp. each rule R to a binary random variable $X_{A}$ resp.

$X_{R}$ , where e.g. $X_{A}=0$ means that fact A does not hold, and $X_{R}=1$ means that rule R holds, if its antecedent is valid. This formulation of rules differs from the MIP (mixed integer programming) representation of clauses from propositional logic as given by e.g. Jeroslov [5] or Hooker [4]. Each rule is assigned a variable of its own, it is not made up from the variables of the involved propositions.

Thus, as known from reliability theory, the validity of a proposition can be expressed as an increasing function of the underlaying random variables. For instance, in the last example we get $X_{D} = \max \{X_{B} \cdot X_{R3}, X_{C} \cdot X_{R4}\}$ with $X_{B} = \max \{X_{A} \cdot X_{R1}, X_{C} \cdot X_{R2}\}$ . The belief in $D$ is then $P(X_{D} = 1)$ .

In general, if a proposition $B$ is implied by several rules $R1: A1 \to B, \ldots, Rk: Ak \to B$ , then $X_B = \max \{X_{A1} \cdot X_{R1}, \ldots, X_{Ak} \cdot X_{Rk}\}$ .

In principle, the calculation of $P(X_{B}=1)$ can be done: the distribution of $X_{Ai}$ resp. $X_{Ri}$ is given by $P(X_{Ai}=1)$ resp. $P(X_{Ri}=1)$ being the belief in proposition Ai resp. rule Ri. All rules are independent, the difficulty of the evaluation lies in possible dependencies of the propositions and the possibly large number of antecedents having to be evaluated first.

To simplify the calculations, the dependencies might be neglected always leading to an overestimation, i.e. a too optimistic estimation, of the true value, comp. the last example.

The result is based on the association of random variables, see e.g. [2] for the definition and the next lemma.

Definition. A set of real-valued random variables $X_{1},\ldots,X_{n}$ is called associated, iff for all non-decreasing functions, $f,g\colon\mathbb{R}^{n}\to\mathbb{R}$ holds: $\operatorname{Cov}(f(X_{1},\ldots,X_{n}),g(X_{1},\ldots,X_{n}))\geq0.$

Two important properties of associated random variables are the following.

Lemma 5. (a) If $X_{1},\ldots,X_{n}$ are independent, then $X_{1},\ldots,X_{n}$ are associated. (b) If $X_{1},\ldots,X_{n}$ are associated, then $f_{i}(X_{1},\ldots,X_{n})$ are associated for arbitrary nondecreasing functions $f_{i}:\mathbb{R}^{n}\to\mathbb{R}$ , $i=1,\ldots,m\in\mathbb{N}$ . (c) If $X_{1},\ldots,X_{n}$ are associated, then for all $t\in\mathbb{R}$ : $P(X_{1}\leq t,\ldots,X_{n}\leq t)\geq P(X_{1}\leq t)\cdot\ldots\cdot P(X_{n}\leq t)$ .

Lemma 6. If the initial propositions of an inference system are independent, then for any set of propositions $A1, \ldots, Ak$ the random variables (a) $X_{A1}, \ldots, X_{Ak}$ and (b) $X_{A1}X_{R1}, \ldots, X_{Ak}X_{Rk}$ are associated.

Proof. Trivial by lemma 5, since all variables $X_{A1},\ldots,X_{Ak}$ resp. $X_{A1}\cdot X_{R1},\ldots,X_{Ak}\cdot X_{Rk}$ are nondecreasing functions of the random variables of the initial propositions and the involved rules.

All together this gives the next theorem.

Theorem 2. $Bel(B) = P(X_B = 1) \leq P^*(X_B = 1)$ , with $P^*$ being the measure for independent antecedents.

Proof. By the independence of the rules from the propositions and the independence of all the rules from each other, we obtain

$$
\begin{array}{r l} & P (X _ {B} = 1) \\ & \quad = P (\max \left\{X _ {A 1} \cdot X _ {R 1}, \dots , X _ {A k} \cdot X _ {R k} \right\} = 1) \\ & \quad = 1 - P (\max \left\{X _ {A 1} \cdot X _ {R 1}, \dots , X _ {A k} \cdot X _ {R k} \right\} = 0) \\ & \quad = 1 - P (X _ {A 1} \cdot X _ {R 1} \leq 0, \dots , X _ {A k} \cdot X _ {R k} \leq 0) \\ & \quad \leq 1 - P (X _ {A 1} \cdot X _ {R 1} \leq 0) \cdot \dots \cdot P (X _ {A k} \cdot X _ {R k} \leq 0), \end{array}
$$

the inequality holding by lemmas 5 and 6. Clearly, the last term is equal to $P^{*}(X_{B} = 1)$ .

Simulation of an inference network is another way to evaluate it. All random variables $X_{R}$ resp. $X_{A}$ for initial propositions will be realized. The validity of all propositions one is interested in can be evaluated deterministically. This procedure is repeated independently, say N times, and for some proposition B of interest $\operatorname{Bel}(B)=P(X_{B}=1)$ is approximated by

$$
1 / N \cdot \sum_ {1 \leq j \leq N} X _ {B, j},
$$

where $X_{B,j}$ is the validity of proposition B in run j.

All random variables $X_{A}$ resp. $X_{R}$ , which have to be drawn, will be transformed from independent 0–1 uniform random variables U. For instance for A: $X_{A}=1$ , if $U\geq1-\operatorname{Bel}(A)$ , 0 otherwise. Thus, $P(X_{A}=1)=1-(1-\operatorname{Bel}(A))=\operatorname{Bel}(A)$ and $X_{A}$ is increasing in U. The random variable $X_{B}$ is increasing in all underlaying 0–1 random variables. This allows for another use of the association of all the variables $X_{A1},\ldots,X_{Ak}$ : the efficiency of the simulation can be increased by antithetic sampling. All 0–1 variables U can be used twice by forming $X_{B,j}$ from 1-U as well, denoted by $X_{B,j,ant}$ . The estimator

$$
1 / N \cdot \sum_ {1 \leq j \leq N} \left(X _ {B, j} + X _ {B, j, \mathrm{ant}}\right) / 2
$$

can be shown, see e.g. [8] to have a smaller variance than the estimator given above, even if the above estimator is based on 2N instead of N simulation runs.

We will now allow inference systems with propositions having negations such as the following: suppose there are 3 propositions A, B, and C related by the rules R1: $A \rightarrow C$ , R2: $B \rightarrow C$ , and R3: $\neg B \rightarrow \neg C$ :

![](/api/attachments/MKNEXW3J/fulltext/images/4fd6c1a3275d7c9aaed0537614315def12168502438f274675f1eb05541b8e50.jpg)

If both $A$ and $\neg B$ are true and both the rules $R1$ and $R3$ hold, then there is the contradiction $C \wedge \neg C$ . Contradictions may of course be implied without the initial propositions being contradictory.

When evaluating such inference systems - by the definition of $\oplus$ - all belief implied is calculated in the same way as in systems without negations, with one exception: the probabilities calculated for a proposition have to be normalized by the probability that there is no contradiction for this proposition $= 1$ - probability that there is a contradiction. Note that contradictions, i.e. the simultaneous validity of a proposition e.g. $C$ and its negation $\neg C$ , ar given by $\emptyset$ . When forming the orthogonal sum, these are exactly the cases being counted in the denominator, see above.

In these situations, simulation again is a means to evaluate inference systems. However, some of the simulation runs have to be rejected: the runs in which there are contradictions must not be counted. On the other hand, not all probability mass assigned to the belief in a proposition can be assigned to its negation. It may well be that no conclusion about a proposition can be reached by e.g. failure of some rules. This is essential to belief functions. Thus, when evaluating the belief function of a proposition C, we have to take into account explicitly at least two out of three cases: C, $\neg C$ and $\Theta C$ . For each proposition C we will hence introduce two binary random variables $X_{C}$ and $X_{\neg C}$ describing the validity of $C$ and $\neg C$ , where e.g. $X_{C} = X_{\neg C} = 1$ denotes a contradiction. Thus, $\operatorname{Bel}(C) = P(X_{C} = 1, X_{\neg C} = 0) / P(X_{C} + X_{\neg C} \leq 1)$ . If an inference system is simulated $N$ times, we approximate $\operatorname{Bel}(C)$ by

(number of runs with $X_{C} = 1$ and $X_{\neg C} = 0) / N$

$$
\begin{array}{l} / (\text { number   of   runs   with } X _ {C} + X _ {\neg C} \leq 1) / N \\ = (\text { number   of   runs   with } X _ {C} = 1 \text { and } X _ {\neg C} = 0) \\ / (\text { number   of   runs   with } X _ {C} + X _ {\neg C} \leq 1). \end{array}
$$

Antithetic sampling can also be applied in these situations. For some proposition C, whose belief is to be evaluated, we define $f(X_{C}, X_{\neg C}) := 1$ , if $X_{C} = 1$ and $X_{\neg C} = 0$ , 0 otherwise. $N_{acc}$ denotes the number of accepted runs out of N trials. $X_{C,j}(X_{\neg C,j})$ denotes the outcome of $X_{C}(X_{\neg C})$ in run j. Instead of estimator

$$
1 / N _ {\mathrm{acc}} \cdot \sum_ {j \in \mathbf {A c c}} f (X _ {C, j}, X _ {\neg C j}),
$$

we can use the antithetic estimator

$$
\begin{array}{l} 1 / N _ {\mathrm{acc}} \cdot \sum_ {j \in \mathrm{Acc}} f (X _ {C, j}, X _ {\neg C, j}) / 2 + 1 / N _ {\mathrm{acc,ant}} \\ \cdot \sum_ {j \in \mathrm{Acc,ant}} f (X _ {C, j, \mathrm{ant}}, X _ {\neg C, j, \mathrm{ant}}) / 2, \end{array}
$$

where Acc is the set of accepted simulation runs out of $\{1,\ldots,N\}$ and all terms with index “ant” are those from the antithetic runs; $N_{acc}=|Acc|$ .

Lemma 7. The estimator and the antithetic estimator are unbiased.

Proof. For the estimator $1/N_{\mathrm{acc}} \cdot \Sigma_{j \in \mathrm{Acc}} f(X_{C,j}, X_{\neg C,j})$ only. The antithetic estimator is dealt with in the same way.

$$
\begin{array}{l} E \Big (1 / N _ {\mathrm{acc}} \sum_ {j \in \mathrm{Acc}} f \big (X _ {C, j}, X _ {\neg C, j} \big) \Big) \\ = \sum_ {1 \leq k \leq N} E \Bigg (1 / k \sum_ {j \in \mathrm{Acc}, | \mathrm{Acc} | = k} f \big (X _ {C, j}, X _ {\neg C, j} \big) \\ \quad \mid N _ {\mathrm{acc}} = k \Big) \cdot P \big (N _ {\mathrm{acc}} = k \big) \\ = \sum_ {1 \leq k \leq N} 1 / k \cdot \sum_ {1 \leq j \leq k} E \Big (f \big (X _ {C, j}, X _ {\neg C, j} \big) \\ \quad \mid N _ {\mathrm{acc}} = k \Big) \cdot P \big (N _ {\mathrm{acc}} = k \big) \end{array}
$$

$$
\begin{array}{l} = \sum_ {1 \leq k \leq N} E \big (f (X _ {C}, X _ {\neg C}) | X _ {C} + X _ {\neg C} \leq 1 \big) \\ \cdot P (N _ {\mathrm{acc}} = k) \\ = E \big (f (X _ {C}, X _ {\neg C}) | X _ {C} + X _ {\neg C} \leq 1 \big) \\ = P (X _ {C} = 1, X _ {\neg C} = 0 | X _ {C} + X _ {\neg C} \leq 1) \\ = \operatorname{Bel} (C). \end{array}
$$

Note that $N_{\mathrm{acc}} = k$ is short for: there are exactly $k$ indices $j \in \{1, \dots, N\}$ with $X_{C,j} + X_{\neg C,j} \leq 1$ .

The monotonicity of f ensures variance reduction of the antithetic estimator over the unrefined one. Moreover, empirical results showed that in inference systems with contradictions the reduction of variance was greater than in systems without.

Taking all into account we conclude that the Dempster–Shafer theory, at least when applied to inference systems, appears to be not too far away from “classical” Bayes theory. Methods from probability theory may well serve the theory of evidence.

## References

[1] Barnett, J.A.: Computational methods for a mathematical theory of evidence, Proc. Int. Joint Conf. on Artif. Intell., 1981, p. 868–875.

[2] Barlow, R.E., Proschan, F.: Statistical theory of reliability and life testing, To Begin With, Silver Spring, MD, 1981.

[3] Eddy, W.F., Pei, G.P.: Structure of rule based belief functions, IBM J. Res. Develop. 30, 1986, p. 93–101.

[4] Hooker, J.N.: A quantitative approach to logical inference, Dec. Sup. Syst. 4, 1988, p. 45–69.

[5] Jeroslov, R.: Spatial imbeddings for linear and for logic structures, Dec. Sup. Syst. 4, 1988, p. 71–86.

[6] Kohlas, J.: Conditional belief structures, report 131, University of Fribourg/CH, Institute for Automation and OR, 1987.

[7] Lee, S., Shin, K.G.: Uncertain inference using belief functions, Proc. 3rd Conf. Artif. Intell. Appl., Kissimmec, FL, 1987, p. 238–243.

[8] Ross, S.M.: Introduction to probability models, Academic Press, Orlando, FL, 1985.

[9] Shafer, G.: A mathematical theory of evidence, Princeton University Press, Princeton, 1976.

[10] Shafer, G., Shenoy, P.P., Mellouli, K.: Propagating belief functions in qualitative Markov trees, working paper, School of Business, University of Kansas, 1986.
