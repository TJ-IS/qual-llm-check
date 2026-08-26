---
otero_id: 17432
otero_key: "GZQJTPND"
title: "Defeasible deontic reasoning and its applications to normative systems"
authors: "Young U. Ryu; Ronald M. Lee"
year: "1995"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(94)00002-a"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Defeasible deontic reasoning and its applications to normative systems

Young U. Ryu $^{a,*}$ , Ronald M. Lee $^{b}$

$^{a}$ M / S JO4.4, P.O. Box 830688, The University of Texas at Dallas, Richardson, Texas 75083-0688, U.S.A. $^{b}$ Erasmus University Research Institute, For Decision and Information Systems (EURIDIS) Erasmus University Rotterdam, 3062 PA Rotterdam, The Netherlands

## Abstract

Our interests are in the application of deontic logic for the modelling of regulations in commercial law and other social institutions. We provide a first-order framework of deontic reasoning that can model and compute social regulations and rules. This effort has practical importance due to the ubiquity and complexity of social regulations and norms. Computer-mediated modelling of norms may reduce the overhead of managing complex social norms and avoid inefficiencies and social inequity resulting from complex and ill-maintained social norms. In order to achieve the goal, we apply defeasible reasoning, a clausal form logic programming approach, and capture deontic concepts in first-order representations. The proposed formalism is applied to the modelling of normative systems such as bureaucratic regulations and legal reasoning.

Keywords: Deontic logic; Defeasible reasoning; Legal reasoning; Normative system

## 1. Introduction

Deontic logic, also called logic of norm or logic of obligation, refers to a study of the normative use of language in which statements of “it is obliged …,” “it is permitted …,” etc. occur. It has applications to the modelling of regulations in commercial law and other social institutions [1,22,23,29,44]. Lee [22,23], for instance, observed deontic aspects prevailing in the control and administration of bureaucracy organizations and suggested the use of deontic concepts to model bureaucratic rules. Wieringa et al. [44] showed how deontic constraints on databases could provide better organizational modelling. Alchourrón and Bulygin [1] built a logico-linguistic foundation for philosophy of law and legal reasoning by applying deontic aspects of norms.

In this paper, we purport to provide a first-order framework of deontic reasoning that can model and compute normative rules or regulations such as bureaucratic policies, legal rules, and social regulations. Computer-mediated modelling of rules and regulations is practically important due to their ubiquity and complexity. Social rules and regulations are the basis of every civilized society. They are means of administering the society and organizations and maintaining the equity of the society that consists of various social entities having potentially conflicting interests. As the society grows more complex, with more specialization of roles, and a wider range of activities both in work and leisure, the system of social norms also grows more complex. Due to the complexity, the overhead of maintaining social norms is also increasing. In addition, ill-maintained social norms result in complaints, inefficiencies, and social inequity. Computer-based support systems for administration of social norms may reduce such overhead and problems of ill-maintained social norms [36].

Considering its purpose and properties, deontic logic is one of most suitable tools of the modelling of normative concepts. In the practical application to the modelling of regulations, however, there are two factors that are missing in standard deontic logic $[14,40]$ . First, the conventional modal representation of deontic logic $^{1}$ does not fit our purpose of integration to the first-order framework to compute normative aspects of regulations and social rules. The computation issue is crucial in building an expert or support system for reasoning about regulations in commercial law and social institutions.

Second, standard deontic logic suffers from various paradoxes $[14]$ , such as the “contrary-to-duty imperative” paradox $[8]$ , etc., which are often observed in the context of reasoning about social norms and regulations. For instance, law codes such as Uniform Commercial Code (UCC) of the U.S.A. and bureaucracy manuals are full of expressions “if … then one should (or may) …” or similar ones which potentially result in contrary-to-duty imperative paradoxes. Consider the following regulations of secured transactions in UCC:

(1) A secured party should use reasonable care of collateral in his possession [§9-207(1)].

(2) Unless otherwise agreed, when the collateral is in the secured party's possession, the risk of accidental loss or damage is on the debtor [§9-207(2)(b)].

(3) A secured party is liable for any loss caused by his failure to meet any obligation imposed by the preceding sections [§9-207(3)].

(4) Tom, who is a secured party, does not use reasonable care of collateral in his possession. We paraphrase the second and third statements to make their intended meaning clear as follows:

(2) It should be that if a secured party uses reasonable care of collateral, he is not liable for damage of collateral.

(3) If a secured party does not use reasonable care of collateral, he is liable for damage of collateral.

According to the deduction of standard deontic logic, “Tom is not liable for damage of collateral” due to (1) and (2); on the other hand, “Tom is liable for damage of collateral” due to (3) and (4). However, it is intuitively clear that the only conclusion in the situation is “Tom is liable for damage of collateral.”

Dworkin [13] and Gardner [15] address differences of “if … then …” conditionals of legal rules from material or strict implications in that the evaluation of conditionals is often subject to the situation-dependent interpretation. They distinguish concepts of “rule-guided” activities or “legal principles” that are situation-dependent and “rule-governed” activities or “legal rules” that are situation-independent. For example, a situation-dependent representation of a rule stating that a man should obey traffic signals does not “purport to set out conditions that make its application necessary” nor “necessitate a particular decision” [13], because despite its generality in applications there are exceptional situations such as emergency police matters in which a man may disobey traffic signals. Thus, a situation-dependent rule may be denied or defeated if a reasonable explanation is provided [5]. In logic, situation-dependent rules may be represented as counterfactuals, while situation-independent rules may be represented as material or strict implications [16,26,30]. Standard deontic logic does not provide representations and reasoning about such situation-dependent rules, even though it is reasonable to consider conditionals of deontic logic as counterfactuals [6,38].

Later, another system, conditional deontic logic (also called dyadic deontic logic) [18,41,42], has been introduced in order to semantically resolve deontic paradoxes, especially the contrary-to-duty imperative paradox [14]. The central ideal of conditional deontic logic is that deontic status is interpreted situation-dependently. Consider the above example again. The deontic status “a secured party is not liable for damage of collateral” is true in all possible worlds that resemble deontically perfect worlds, i.e. worlds in which all norms are fulfilled [14,18]. However, in the situation (or world) in which “a secured party does not use reasonable care of collateral,” the norm of the first rule (i.e., “a secured party should use reasonable care of collateral in his possession”) is violated and the deontic status “a secured party is not liable for damage of collateral” derived from the first rule (together with the second rule) does not hold in the situation in which “a secured party does not use reasonable care of collateral.” For the detail of the situation-dependent interpretation of deontic status, see [18].

We explore this idea of the situation-dependent interpretation of deontic status and provide a first-order reasoning method for the deduction of deontic status. The situation-dependent treatment of concepts is a subject of counterfactual reasoning $[16,26,30]$ . A computing process of counterfactual reasoning is developed as defeasible reasoning based on conditional logic $[11,28,31,32,33,34,35]$ . Defeasible reasoning may be considered as a clausal form logic programming for nonmonotonic reasoning. We apply defeasible reasoning concepts to standard deontic logic, resolve deontic paradoxes such as “contrary-to-duty imperatives” $[8]$ , and further provide a computational version of deontic reasoning. The proposed idea is consistent with hierarchical reasoning of deontic expressions of Alchourrón and Bulygin $[2]$ . When two derived obligations seem contradictory, one from a stronger deontic expression in the hierarchy is chosen while the other is denied. Defeasible reasoning provides hierarchies of rules or deontic expressions and reasons about these hierarchies when deriving deontic status. In short, the central goal of the paper is to address a form of deontic reasoning within a first-order logic programming paradigm and capture defeasible aspects of deontic reasoning so that practical systems of norms are developed for the purpose of helping administrate social norms and regulations.

## 2. Deontic logic

## 2.1. Standard deontic logic

The deontic primitive of “obligation” is captured by the expression:

## Oφ

read that “ $\phi$ is obliged.” The sense of the deontic operator relies on what is meant by an action, or doing something [43]. What is under a deontic predication is a statement of an action. Thus reading a deontic expression as the above is better than reading it as “ $\phi$ is obligatory” because it is ambiguous, in the latter case, whether an action or a state of affairs is under the deontic constraint of obligation. Further “O $\phi$ ” itself cannot be an expression of an action and therefore the iteration of the deontic operator, for example “OO $\phi$ ,” does not make sense at all [43].

Other deontic operators are defined as follows:

$$
\mathrm{P} \phi = _ {\text { def }} \neg \mathrm{O} \neg \phi
$$

$$
" \phi \text { is   permitted },"
$$

$$
\mathrm{F} \phi = _ {\mathrm{def}} \mathrm{O} \neg \phi
$$

$$
" \phi \text { is   forbidden,"   and }
$$

$$
\mathrm{W} \phi = _ {\text { def }} \neg \mathrm{O} \phi
$$

$$
" \phi \text {   is   waived.   }"
$$

Standard deontic logic adopts axiom schemata and inference rules of propositional logic and adds the following [14]:

[DA1] $\mathrm{O}\phi \rightarrow \neg \mathrm{O}\neg \phi$

If $\phi$ is obliged, then $\phi$ is permitted.

[DA2] $\mathrm{O}(\phi \wedge \psi) \leftrightarrow \mathrm{O}\phi \wedge \mathrm{O}\psi$

$\phi$ and $\psi$ are together obliged if and only if they are obliged separately.

[DA3] $\mathrm{O}(\phi \vee \neg \phi)$

Either to do $\phi$ or not to do $\phi$ is obliged.

$$
[ \mathrm{DR} ] (\vdash \phi \leftrightarrow \psi) / (\vdash \mathrm{O} \phi \leftrightarrow \mathrm{O} \psi)
$$

If $\phi$ and $\psi$ are logically equivalent, then $O\phi$ and $O\psi$ are also logically equivalent.

## 2.2. On commitment

One of interesting sentence schemata in deontic logic, called commitment, is a formula of:

$$
\mathrm{O} (\phi \rightarrow \psi)
$$

which is read that “the performance of the act named $\phi$ commits the agent to perform the act named $\psi$ ” [40]. In a commitment formula, the interpretation of the implication between two formulas is ambiguous. It may be better explained by the following equivalent sentence schema:

$$
\mathrm{O} (\neg \phi \vee \psi)
$$

in which a commitment is understood as a choice of actions:

An agent is obliged to neglect (or not-do)

$\phi$ or do $\psi$ .

Alternatively, by the following sentence schema that is also equivalent to the above:

$$
\mathrm{F} (\phi \land \lnot \psi)
$$

a commitment can be explained in terms of incompatibility of two actions:

Doing $\phi$ without doing $\psi$ is prohibited.

Often, a commitment is confused with a conditional obligation or conditional imperative [7]:

## $\phi \rightarrow \mathrm{O}\psi$

which is read that “doing $\psi$ is obliged if $\phi$ ” where $\phi$ is a proposition of a state of affairs, or read that “doing $\psi$ is obliged if the agent does $\phi$ ” where $\phi$ is a proposition of an action.

A conditional obligation, especially an obligation of an action that holds when the agent does another action, is found in two cases:

A contrary-to-duty imperative [8] that states what should, or should not, be done (i.e., a specific sanction) if an obligation is not fulfilled [4]. For example, (a) you should refrain from robbing others; (b) if you rob others, you should be punished for robbery. Here, the second statement is a contrary-to-duty imperative, which is a conditional obligation.

\- An ethical or legal responsibility resulting from a promise made by a voluntary agent. That is, if you promise to do an action, you should do it. For example, accepting an offer may be considered as making a promise; thus if you accept an offer, you should fulfil terms expressed in the offer.

In both cases, a conditional obligation talks about the obligation of an action that holds when another action (either an action of violation of a duty or an action of promising) is actually performed.

Differently, a commitment does not talk about the actual performance of an action. A statement is modeled as a commitment formula in three cases:

A complement (vs. sanction) paid when a violation of a duty is not observed (or proved). For example, (a) you should refrain from robbing others; (b) if you rob others, you should be punished for robbery; (c) it should be that if you refrain from robbing others, you are not punished for robbery. Here, the third statement is modeled as a commitment. It reflects the principle “innocent until proven guilty.”

\- A duty or privilege derived from another duty or privilege. For example, (a) you should go to the assistance of your neighbours; (b) you should not tell them you are coming if you do not go; (c) it should be that if you go, you tell them you are coming. Here, the third statement is modeled as a commitment by which a duty of telling them you are coming is derived from another duty of going to the assistance of your neighbours.

\- Legal agency in which the agent shows the intention to act in behalf of the principal [21,45]. For example, (a) I should deliver goods to my customer; (b) you are my delivery agent; (c) you agreed to fulfil my delivery obligation. Here, the third statement is a commitment statement by which you are obliged to deliver goods to my customer.

## 2.3. Deontic conflicts

Deontic status, unlike necessity, may conflict with reality [6,19]. Many types of deontic conflicts are not intuitively but logically contradictory. This suggests that standard deontic logic is too rigid and inflexible for representing deontic aspects of actual social systems. For example, see the following conflict of complementary violations:

(1) You should not invest in stocks.

$\mathbf{O}\lnot s$

where s stands for “you invest in stocks.”

(2) You should not invest in bonds.

$\mathbf{O}\neg b$

where b stands for “you invest in bonds.”

(3) You should invest in bonds if you invest in stocks.

$s\to \mathbf{O}b$

(4) You should invest in stocks if you invest in bonds.

$b\to \mathrm{Os}$

(5) You have invested in bonds.

b

From (4) and (5), you have

Os

stating that “you should invest in stocks,” which contradicts with (1). $^{2}$ However, intuitively, it is clear that “you should invest in stocks” and thus (1) should be denied.

Alternatively, one might state (1) and (2) of the above as follows:

(1') You should not invest in stocks if you do not invest in bonds.

(2') You should not invest in bonds if you do not invest in stocks.

$\neg s \to \mathbf{O} \neg b$

According to (1') and (2'), (5) is not a violation of norm. This is not the story that the original investment rules state.

Consider another type of deontic conflicts, known as the contrary-to-duty imperative paradox [8], as noted in the previous section:

(1) A secured party should use reasonable care of collateral in his possession.

Oc

where c stands for using reasonable care of collateral.

(2) It should be that if a secured party uses reasonable care of collateral, he is not liable for damage of collateral.

$$
\mathrm{O} (c \rightarrow \neg d)
$$

where d stands for paying for the damage of collateral.

(3) If a secured party does not use reasonable care of collateral, he is liable for damage of collateral.

$$
\neg c \to \mathrm{Od}
$$

(4) Tom, who is a secured party, does not use reasonable care of collateral in his possession.

$\neg c$

According to deontic logic, the following is a theorem [40]:

$$
\mathrm{O} \phi \wedge \mathrm{O} (\phi \rightarrow \psi) \rightarrow \mathrm{O} (\psi).
$$

From (1) and (2) of the above, by the theorem and the modus ponens rule:

O $\neg d$ .

On the other hand, from (3) and (4) of the above, by the modus ponens rule:

Od.

The problem of deontic logic in the above example lies in that conditional deontic expressions are treated as material implications. Rather, conditional deontic expressions should be counterfactuals [6]

In fact, conditional prima facie obligation sentences do seem to be counterfactual. When we say that if you promised to do something you should it, we seem to be saying that, in the circumstances in which you promised that are otherwise most similar to the actual world, you have an obligation to fulfil your promise. If something odd happens – if the person you've promised to take to the movies runs off to get married, … – then the obligation to take the person to the movies cancelled. [Emphases added.]

This idea of counterfactual conditional deontic statement is also supported by Ross [38], Greenspan [17], and Decew [10].

In the following sections, we adopt this concept of counterfactuals and suggest a first-order framework of deontic reasoning that is computable as well as resolves the above deontic conflicts.

## 3. First-order representation of deontics

In standard deontic logic, what is under a normative constraint (such as obligation, permission, etc.) is a generic action (in the sense of von Wright [40]). For example, a statement “a secured party should use reasonable care of collateral in his possession” is expressed as:

O("a secured party uses reasonable care of collateral")

where “a secured party uses reasonable care of collateral” is a proposition or a first-order formula.

Alternatively, deontic concepts may be considered as properties of actions. In first-order logic, a property is represented as an individual, for example:

is(banana,yellow),

or as a predicate name, for example:

yellow(banana).

Even if the above two are expressively equivalent, we prefer the latter because of the representational economy: that is, the latter does not require a special predicate name such as “is” (or similar ones) to assign a property to an entity.

To capture deontic concepts as properties of actions as the above, we first introduce a unary predicate name of a deontic property “oblige.” Second, we consider actions as individual terms rather than propositions or formulas. Thus, we represent an obligation of an action $\alpha$ as:

oblig(α),

that is, “an action $\alpha$ is obliged.” Thus, in the following expression:

oblig("a secured party uses reasonable care of collateral")

“a secured party uses reasonable care of collateral” is an individual term, not a proposition, denoting a certain action. Similarly, we introduce another unary predicate name “forbid” such that: forbid( $\alpha$ )

is read “an action $\alpha$ is forbidden.” The concepts of permission and waiver are defined in terms of obligation, prohibition, and negation:

$$
\operatorname{permit} (\alpha) = _ {\text { def }} \neg \operatorname{forbid} (\alpha)
$$

and

$\text{waive}(\alpha) = _{\text{def}} \neg \text{oblig}(\alpha).$

The commitment formula is represented as a binary predicate “commit”:

commit(α,β).

We assume that the semantic domain of a normative problem includes a set of individual actions. Syntactically, an action is represented as either a constant, a variable, or a function expression. A function expression of an action is regarded as a mapping from individual objects to an individual action. Say that the semantic domain D is a disjoint union of $D_{act}$ and $D_{ind}$ , where $D_{act}$ is a set of individual actions and $D_{ind}$ is a set of other individual objects such as people, things, etc. Let $[\cdot]$ be a semantic function that maps syntactic expressions to semantic objects, semantic expressions, or truth values [12]. Then, the denotation of an action “a secured party uses reasonable care of collateral” is an element of $D_{act}$ :

“a secured party uses reasonable care of

collateral”] ∈ D $_{act}$ .

Consider a more generic expression of the action: X“uses reasonable care of”Y

where X and Y are variables and “uses reasonable care of” is a function. Then, the denotation of “uses reasonable care of” is a function that maps a pair of elements of $D_{ind}$ to an element of $D_{act}$ , that is:

[“uses reasonable care of”] $\in D_{\mathrm{ind}} \times D_{\mathrm{ind}} \to D_{\mathrm{act}}$ .

The performance of an action $\alpha$ is represented as:

perform(α).

Often, it is required to talk about an action that cannot be performed with another action. For example, “opening the door” and “closing the door” cannot be performed by a certain agent at the same spatio-temporal location. We introduce a notation:

exclusive(α,β)

to represent the exclusiveness of actions $\alpha$ and $\beta$ .

## 4. Defeasible deontic reasoning

## 4.1. Defeasible reasoning based on conditional logic

Defeasible reasoning by Nute [31,32,33,34,35], Delgrande [11], and Loui [28] is a form of non-monotonic reasoning based on conditional logic [39,16,26,30]. $^{3}$ The basic idea is that, given two conditionals “ $\phi > \gamma$ ” and “ $\psi > \neg \gamma$ ” when $\phi$ is more specific than $\psi$ , the conditional “ $\psi > \neg \gamma$ ” is defeated by “ $\phi > \gamma$ ” (or the conclusion $\neg \gamma$ is defeated by $\gamma$ ). The specificity is roughly defined as follows:

$\phi$ is more specific than $\psi$ iff $\phi \vdash \psi$

where “←” denotes a deduction of conditional logic or first-order logic, depending on the specification of defeasible reasoning systems. The specificity may be understood as a way of ordering conditionals.

## 4.2. Formulation of conditionals

In defeasible deontic reasoning, we provide two types of conditionals:

\- Indefeasible conditional: $\phi \leftarrow \psi_1, \psi_2, \ldots, \psi_n$ - Defeasible conditional: $\phi \Leftarrow \psi_1, \psi_2, \ldots, \psi_n$ where $\phi$ and $\psi_i$ ( $i = 1, 2, \ldots, n$ ) are literals, i.e. atomic formulas or their negations, and commas between literals are regarded as conjunctions. A defeasible conditional may be denied, or defeated, in a certain circumstance if there exists a conditional with a more specific antecedent; while an indefeasible conditional is never defeated.

A deontic conditional is a defeasible conditional whose consequence is an atomic deontic expression or its negation:

$$
\cdot \operatorname{oblig} (\alpha) \Leftarrow \psi_ {1}, \psi_ {2}, \dots , \psi_ {n}
$$

$$
\cdot \text {   forbid } (\alpha) \Leftarrow \psi_ {1}, \psi_ {2}, \dots , \psi_ {n}
$$

$$
\cdot \neg \operatorname{oblig} (\alpha) \Leftarrow \psi_ {1}, \psi_ {2}, \dots , \psi_ {n}
$$

$$
\cdot \neg \text { forbid } (\alpha) \Leftarrow \psi_ {1}, \psi_ {2}, \dots , \psi_ {n}
$$

A conditional may have an empty antecedent. An empty antecedent is an empty conjunction. In the evaluation of a conjunction, we search for a false component. Thus, an empty conjunction is considered as true, because there is no false component in it. Therefore, we express such a clause as:

$\phi \leftarrow$ true or $\phi \Leftarrow$ true

where “true” is the propositional constant of truth. Often, we drop “← true” and simply write the consequence of a conditional with an empty antecedent.

Conditionals of defeasible deontic reasoning look similar to Horn clauses or general program clauses of standard logic programming $[3,27]$ . The difference is that the negation operator is allowed in the consequence of a conditional. Also, the negation in defeasible deontic reasoning is the classical negation of first-order logic and does not follow the negation as failure rule $[9]$ of standard logic programming.

## 4.3. Deduction procedure of defeasible deontic reasoning

The deduction procedure of defeasible deontic reasoning is characterized by an ordering of conditionals, a resolution that is obtained by modifying the SLD-resolution of standard logic programming $[3,27]$ , and adoption of deontic axioms within the first-order framework.

Let “Ant(C)” and “Cons(C)” denote the antecedent and the consequence of a conditional $C.^{4}$ Then, two conditionals $C_{1}$ and $C_{2}$ are said to be competing if:

\- $\operatorname{Cons}(C_1) = \phi$ and $\operatorname{Cons}(C_2) = \neg \phi$ ;

\- $\operatorname{Cons}(C_1) = \operatorname{oblig}(\alpha)$ and $\operatorname{Cons}(C_2) = \operatorname{forbid}(\alpha)$ ; or

\- $\operatorname{Cons}(C_1) = \operatorname{oblig}(\alpha)$ , $\operatorname{Cons}(C_2) = \operatorname{oblig}(\beta)$ , and exclusive $(\alpha, \beta)$ .

Often, the above definition of competing conditionals is not sufficient to represent real-world problems. It is obvious that the following two conditionals are competing:

1. flies(x) $\Leftarrow$ bird(x)

2. $\neg$ flies $(x) \Leftarrow$ penguin $(x)$

since “flies(x) ∧ ¬flies(x)” is contradictory. However, it is not clear whether the following conditionals are competing:

1. enforceable $(c) \Leftarrow$ contract $(c, p_1, p_2)$ , where $c$ denotes an instance of contract and $p_1$ and $p_2$ are parties in the contract.

2. voidable $(c) \Leftarrow$ contract $(c, p_1, p_2)$ , minor $(p_1)$

3. void(c)←contract(c,p₁,p₂), minor(p₁), disaffirmed(c,p₁)

4. unenforceable $(c) \Leftarrow$ contract $(c, p_1, p_2)$ , fraud $(p_1)$

According to contract law, “enforceable(c)” is incompatible with “void(c)” and also incompatible with “unenforceable(c).” To replace “void(c)” and “unenforceable(c)” with “ $\neg$ enforceable(c)” does not represent the above conditionals correctly, because definitions of an unenforceable contract and a void contract are different. However, it is obvious that conditionals (1) and (3) are competing and also conditionals (1) and (4) are competing. In order to represent this kind of situation, we introduce an expression [31]:

incompatible(φ,ψ)

which states that “ $\phi \wedge \psi$ ” is contradictory. Accordingly, we extend the definition of competing conditionals by adding the following in addition to the above:

\- incompatible(Cons( $C_1$ ), Cons( $C_2$ )).

There exists another case to which the above definition of competing conditionals does not apply. For example:

(1) A student ought to attend class.

$\operatorname{oblig}(c) \Leftarrow s$

where c denotes “one’s attending class” and s “one’s being a student.”

(2) A student athlete ought to play in the final games.

$\operatorname{oblig}(p) \Leftarrow s, a$

where p denotes “one’s playing in the final games” and a “one’s being an athlete.”

(3) It ought to be that if he plays in the final games, he does not attend class.

commit(p,d)

exclusive $(c,d)$

where d stands for “one’s not attending class.” It is obvious that conditionals (1) and (2) are competing due to conditional (3), because if one should play in a final game, he/she cannot attend class. That is, if an obligation and a commitment derive another obligation that is not compatible with a third obligation, then the first and the third obligation are not to be obtained together. Thus, we have the following fifth case of competing conditionals in addition to the above four:

\- $\operatorname{Cons}(C_1) = \operatorname{oblig}(\alpha)$ , $\operatorname{Cons}(C_2) = \operatorname{oblig}(\beta)$ , and either commit $(\alpha, \delta) \wedge$ exclusive $(\beta, \delta)$ or commit $(\beta, \delta) \wedge$ exclusive $(\alpha, \delta)$ .

In the above example of student athletes, we shortly consider a deontic deduction with a commitment formula. By adopting some theorems of standard deontic logic, we provide (limited) deontic deduction features for the defeasible deontic reasoning. Theorems of standard deontic logic are adopted as the following conditional expressions:

$\neg \text{forbid}(\alpha) \leftarrow \text{oblig}(\alpha)$

\- oblig(β) ← commit(α,β), oblig(α), where α and β are ground $^{5}$

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
$\frac{\phi \text{ is not explicitly stated}}{\neg \phi \text{ is assumed to be stated}}$ or even more strongly: $\frac{\phi \text{ is not deduced}}{\neg \phi \text{ is deduced}}$.
</div>

\- forbid $(\alpha) \leftarrow$ commit $(\alpha, \beta)$ , forbid $(\beta)$ , where $\alpha$ and $\beta$ are ground

$\neg \mathrm{oblig}(\alpha) \leftarrow \mathrm{commit}(\alpha, \beta), \neg \mathrm{oblig}(\beta)$ , where $\alpha$ and $\beta$ are ground

$\neg \text{forbid}(\beta) \leftarrow \text{commit}(\alpha, \beta), \quad \neg \text{forbid}(\alpha),$ where $\alpha$ and $\beta$ are ground

Given a set P of conditionals, $P_{+}$ denotes the union of P and the set of the above conditionals that are adopted from theorems of standard deontic logic.

Let $P$ be a set of conditionals and $C_1$ and $C_2$ are conditionals in $P$ . Then, we define an ordering relation $\leqslant$ on $P$ as follows:

\- $C_1 \leqslant C_2$ if $C_1$ is a defeasible conditional and $C_2$ is an indefeasible conditional;

\- $C_1 \leqslant C_2$ if both $C_1$ and $C_2$ are defeasible conditionals and $P'_+ \cup \text{Ant}(C_2) \leftarrow \text{Ant}(C_1)$ , where $P'_+ = P_+ - \{\phi \leftarrow \text{true}\} - \{\phi \Leftarrow \text{true}\}$ .

The second case of the above is called specificity [31]. We derive another ordering relation $<$ as follows:

$C_1 < C_2$ if and only if $C_1 \leqslant C_2$ and $C_2 \notin C_1$ .

If $C_1 < C_2$ , then we say that $C_2$ is superior to $C_1$ .

Now, we define the computation procedure of defeasible deontic reasoning as follows. Let P be a set of conditionals and $N_{0}$ be a query “ $\Leftarrow\phi_{1},\phi_{2},\ldots,\phi_{n}$ .”

\- Suppose $C$ is a variant $^{7}\phi \leftarrow \psi_{1},\psi_{2},\ldots ,\psi_{m}$ (or $\phi \Leftarrow \psi_1,\psi_2,\dots ,\psi_m$ ) of a conditional in $P_{+}$ . If $\phi$ and $\phi_{i}$ unify with a most general unifier $^{8}\theta$ , then:

$$
\Leftarrow \phi_ {1} \theta , \phi_ {2} \theta , \dots , \phi_ {i - 1} \theta , \psi_ {1} \theta , \psi_ {2} \theta , \dots , \psi_ {m} \theta ,
$$

$$
\phi_ {i + 1} \theta , \dots , \phi_ {m} \theta
$$

is a resolvent of $N$ and $C$ with $\theta$ .

Based on the above definition of resolvent, we define a resolution of defeasible deontic reasoning. A defeasible deontic derivation of $P_{+} \cup \{N_{0}\}$ is a maximal sequence of queries $N_{0}, N_{1}, \ldots$ , variant $C_{0}, C_{1}, \ldots$ of conditionals in $P_{+}$ , and substitutions $\theta_{0}, \theta_{1}, \ldots$ such that for all $i = 0, 1, \ldots$ :

(1) no variable of $C_{i+1}$ occur in $N_{0}, C_{0}, C_{1}, \ldots, C_{i}$ ;
(2) $N_{i+1}$ is a resolvent of $N_{i}$ and $C_{i}$ with $\theta_{i}$ ; and (3) for each defeasible conditional $C_{i}$ : (3.1) there does not exist a competing conditional in $P_{+}$ ; or (3.2) for every competing $D_{i}$ that is a variant of a conditional in $P_{+}$ , where

$$
\operatorname{Ant} (D _ {i}) = \{\gamma_ {1}, \gamma_ {2}, \dots , \gamma_ {k} \}:
$$

(3.2.1) $C_i \not\prec D_i$ ; or

(3.2.2) $C_i < D_i$ and the SLD-derivation $^9$ for $P_+ \cup \{ \leftarrow \gamma_1, \gamma_2, \ldots, \gamma_k \}$ fails.

There exist three cases of a defeasible deontic derivation:

\- refutation: a finite derivation whose last resolvent is an empty conditional,

\- failed derivation: a finite derivation whose last resolvent is not an empty conditional,

\- infinite derivation: a derivation in which resolvents are obtained infinitely.

## 4.4. On closed world assumption

The closed world assumption [37] is a way of efficient representation and deduction of negative information, which may be stated as:

For example, in a University database, there is a student file that includes information about all students in the University; and further it is assumed that if a person is not described in the student file, he/she is not a student. In standard logic programming, a restricted version of the closed world assumption, called the negation as failure rule [9], is implemented since the closed world assumption is not an efficient computing method [3,9,27].

```prolog
general-borrower(X):- special-student(X).
```

In defeasible deontic reasoning, we adopt the negation of classical first-order logic rather than the negation as failure rule. It means that the only information or conclusion supported by defeasible deontic reasoning is one that is explicitly stated or derived. In other words, not only data for students but also those for people who are not students must be explicitly stated; yet this does not seem practically feasible in certain application contexts. However, it is possible to simulate the closed world assumption in defeasible deontic reasoning, if it is necessary.

Consider the following sentence schema:

$$
\phi \Leftarrow \text { true }
$$

which is often called a presumption [31]. A presumption is a defeasible conditional whose antecedent is empty. Any other competing indefeasible conditionals (even including those with the empty antecedent) and competing defeasible conditionals whose antecedent is not empty are superior to the presumption. Thus, a presumption is the most basic default. For example:

(1) $\neg$ student $(X) \Leftarrow$ true

(2) student(tom)

(3) student(mary)

The presumption (1) states that “presumably, no one is a student.” However, Tom and Mary are students according to the above indefeasible conditionals (2 and 3) that defeat the presumption. Since there is no explicit statement about Dick, by the presumption (1), Dick is not a student.

## 4.5. Implementation notes

A prototype system of defeasible deontic reasoning is currently implemented in Prolog and d-Prolog [31]. A non-numeric constant, predicate name, or function name is written in a string starting with a lowercase alphabet. A variable is written in a string starting with an uppercase alphabet. A non-defeasible clause is represented by an ordinary Prolog rule:

p: -q, r, s.

A defeasible clause is represented by:

```txt
p := q, r, s.
```

In the prototype system, not (i.e., negation as failure), cut, and disjunction are not allowed. An operator of “\~” is introduced to represent the classical negation of first-order logic. Various system predicates, such as var, atom, today, =, etc., are available. These system predicates are excluded in the consideration of specificity. For example,

$$
p (A, B) := q (A, C), r (A, D), B = C + D.
$$

is more specific than

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
$\sim p(A, B) := q(A, C), B = C + 4.$
</div>

In the following sections, we use notations of the implemented prototype system that are written in the typewriter font.

## 5. Applications: library lending code

The General Libraries Lending Code (GLLC) of the University of Texas at Austin defines the “privileges and responsibilities of persons who borrow materials from the General Libraries at the University of Texas at Austin.” It provides procedures for loan and library use of resources including books, periodicals, class materials, etc., borrowers’ responsibilities, and sanctions.

In addition to deontic aspects of borrowing and returning library materials, temporal aspects of doing actions are to be addressed in modelling GLLC. Our notations for time markings are [24]:

```txt
<actor>:<action> by <date>
```

that is used to mark a deadline and

```txt
<actor>:<action> on <date>
```

that is used to record the time when a historical action is performed.

§15 cf GLLC defines categories of library users:

```prolog
general-borrower(X): - undergraduate(X).
```

```txt
general-borrower(X): graduate(X).
```

```prolog
general-borrower(X):-
non-professional-staff(X).
special-borrower(X):-
faculty(X).
special-borrower(X):-
professional-staff(X).
```

§10 of GLLC covers policies governing loan periods for types of materials:

\- General Collections: 14-day loan to undergraduate students; 28-day loan to other general borrowers; semester loan to special borrowers

\- Periodicals: 3-day loan

• Reserved Materials: 3-day or 7-day loan

\- Special Collections: a specific loan period for all borrowers

These policies are applied to determine the due date when one loans a library material. The library database for materials keeps information of specific loan periods for periodicals, reserved materials, and special collections.

The main responsibility of a borrower is to return materials by the due date to the circulation desk from which they are checked out ( $§4-b$ ). This responsibility, together with the above policies governing loan periods, is represented as follows:

```prolog
oblig(X: return(Y) by Z):=
perform(X:request(Y) on Z1),
due(X,Y,Z1,Z).
due(X,Y,Z1,Z):= /* Rule A */
general-collection(Y),
undergraduate(X),
Z = Z1 + 14.
due(X,Y,Z1,Z):= /* Rule B */
general-collection(Y),
general-borrower(X),
Z = Z1 + 28.
due(X,Y,Z1,Z):=
reserved-material(Y,N),
Z = Z1 + N.
```

where $\text{due}(X,Y,Z1,Z)$ means the library material Y that is requested by the borrower X on the date Z1 is due on Z. In addition to the above, we also specify a case of incompatibility:

```prolog
incompatibility(due(X,Y,Z1,Z), due(X,Y,Z1,ZZ)):-Z\ =ZZ.
```

If an undergraduate student requests a loan for a general collection, both Rules A and B might be applied. But due to the above incompatibility definition, Rules A and B are competing and Rule A is superior to Rule B. Thus, only Rule A is applied.

§A of GLLC Appendix describes overdue charges, that is, \$0.50 per day or \$12.00 maximum:

```prolog
oblig(X:pay(A)):=
oblig(X:return(Y) by Z),
perform(X:return(Y) on Z1),
Z < Z1,
A = 0.50*(Z1 - Z),
A < 12.00.
oblig(X:pay(A)):=
oblig(X:return(Y) by Z),
perform(X:return(Y) on Z1),
Z < Z1,
A = 12.00.
oblig(X:pay(A)):=
oblig(X:return(Y) by Z),
today(Z1),
Z < Z1,
~ perform(X:return(Y) by Z1),
A = 0.50*(Z1 - Z),
A < 12.0.
oblig(X:pay(A)):=
oblig(X:return(Y) by Z),
today(Z1),
Z < Z1,
~ perform(X:return(Y) by Z1),
A = 12.00.
~ perform(X:return(Y) by Z):=
true.
~ perform(X:return(Y) on Z):-
~ perform(X:return(Y) by Z1),
Z <= Z1.
```

Here, it is presumed that a borrower does not return materials unless a specific action of returning materials is observed.

In this section, we demonstrated a simplified implementation of GLLC. The complete implementation includes changes in database of materials available for loan, hold and recall procedures, damaged material charges, further bars against borrowers who do not pay bills, etc.

/\* Rule 2a: 9-312(5)(a) \*/
security-agreement(X1,Y,C,Z1,D1),
security-agreement(X2,Y,C,Z2,D2),
perform(X1:perfect-interest(C) on PD1),

## 6. Applications: secured transactions in UCC

The second application we have chosen to illustrate the effectiveness of defeasible deontic reasoning is the secured transaction under Article 9 the Uniform Commercial Code (UCC). A secured transaction is an agreement in which a secured party provides a certain benefit for another party (often called a debtor) who provides collateral from which the secured party may obtain a secured interest. For example, Tom, the debtor, borrows \$950 from the Star Pawn, the secured party, and uses his computer as collateral for the loan, whereby the Star Pawn obtains a security interest in the computer.

Given that the law of secured transactions is one of the more settled subsystems of law and that the drafters' purpose in Article 9 of UCC was to clearly and systematically detail the procedures for creating and enforcing security interests, this application seems to be amenable to rule-based legal reasoning. Secured transactions represent a large percentage of major business and consumer purchases, making this a domain whose recurrent problems could benefit from an automated legal reasoning system.

In this section, we address two issues: one, how defeasible deontic reasoning effectively represents the priority of conflicting security interests and two, how duties and liabilities of parties are captured by the defeasible deontic reasoning formalism.

## 6.1. Priorities of security interests

Rules governing priorities of security interests are:

\- that a perfected security interest has priority over an unperfected one, and

\- that if both security interests are perfected (or both are unperfected), the first to file (or the first to attach a security interest) has priority.

Perfection is a legal act whereby the secured party takes possession of the collateral or files a financing agreement to assert his/her rights to the collateral.

```txt
priority (X1,X2,Y,C):= /* Rule 1: 9-301(1)(a)/9-312(5) */
```

security-agreement(X1,Y,C,Z1,D1), security-agreement(X2,Y,C,Z2,D2), perform(X1:perfect-interest(C) on PD1).

```txt
perform(X2:perfect-interest(C) on PD2).
```

```csv
PD1<PD2.
priority (X1,X2,Y,C):=
/* Rule 2b: 9-312(5)(b) */
security-agreement(X1,Y,C,Z1,D1),
security-agreement(X2,Y,C,Z2,D2),
D1<D2.
```

where (1) security-agreement(X1,Y,C,Z1,D1) stands for the security agreement on a date D1 between the secured party X1 who provides a benefit Z1, and the debtor Y who uses C as collateral, (2) X1:perfect-interest(C) on PD1 stands for the security interest for collateral C is perfected on a date PD1 by the secured party X1, and (3) priority(X1,X2,Y,X) stands for X1's having priority of security interests over X2.

Note that only one secured party has a priority:

```prolog
incompatible(priority(X1,X2,Y,C), priority(X2,X1,Y,C)).
```

Among the above rules, Rule 2b is the most fundamental and general and Rule 2a is the most specific.

The above rules are general rules that do not exclude exceptional rules. For example, in case of a purchased money security agreement that is a kind of security agreement:

```txt
security-agreement(X,Y,C,Z,D):-pm-security-agreement(X,Y,C,Z,D). the following exceptional rule is applicable:
```

```csv
priority (X1,X2,Y,C):=
/* Rule 3: 9-312(3) */
pm-security-agreement
(X1,Y,C,Z1,D1),
security-agreement(X2,Y,C,Z2,D2),
```

```txt
perform(X1:perfect-interest(C) on PD1),
perform(X2:perfect-interest(C) on PD2),
PD2<PD1,
perform(Y:receive-possession(C) on RPD),
D1<RPD,
perform(X1:notice-in-writing(X2) on ND),
ND<D1,
perform(X2:receive-notice-from(X1) on RND),
RND<RPD+5*356. /* 5 years */
By specificity, Rule 3 is superior to Rule 2a and thus only Rule 3 is applicable in a purchased money security agreement.
```

There exist more exceptional rules in UCC. For instance, §9-312(4) is an exceptional rule of Rule 2(a), §9-313(7) is an exceptional rule of Rule 1, and §9-313(4)(a) is an exceptional rule of §9-313(7). The proposed defeasible deontic reasoning properly and effectively represents these priorities of security interests.

## 6.2. Duties and rights of parties

The primary duty of the secured party is codified in §9-207:

A secured party must use reasonable care in the custody and preservation of collateral in his possession.

```prolog
It is expressed as the following conditional:
oblig(X:use-reasonable-care(C)):= security-agreement(X,Y,C,Z,D), possess(X,C).
```

Further, §9-207(3) provides a secondary duty of the secured party when he fails to fulfil his obligation of using reasonable care of collateral:

```txt
oblig(X:pay-for-loss-or-damage(C)):= /* Rule A */
oblig(X:use-reasonable-care(C), ~ perform(X:use-reasonable-care(C)), loss-or-damage(C). On the other hand, in general, "the risk of acci-
```

dental loss or damage is on the debtor” [§9-207(2)(b)]. This states three things. One, the debtor is responsible the loss or damage of the collateral:

```prolog
oblig(Y:pay-for-loss-or-damage(C)):= /* Rule B */
security-agreement(X,Y,C,Z,D), loss-or-damage(C).
```

Two, UCC does not have the secured party be responsible for the loss or damage under the presumption that he uses reasonable care of the collateral:

```prolog
commit(X:use-reasonable-care(C), X:not-pay-for-loss-or-damage(C)). exclusive(X:pay-for-loss-or-damage(C), X:not-pay-for-loss-or-damage(C)).
```

Three, only one party is responsible for the loss or damage:

```prolog
exclusive(X:pay-for-loss-or-damage(C), Y:pay-for-loss-or-damage(C)): - X \ = Y.
```

Rules A and B are competing, but Rule A is superior. Thus, Rule A, instead of Rule B is applicable when the secured party does not (in the sense of the classical negation, not the negation as failure) use reasonable care of the collateral; otherwise, Rule B is applicable.

## 7. Concluding remarks

In this paper, we address a system of deontic reasoning based on defeasible reasoning. The proposed system provides syntactic derivations of conditional deontic expressions. The key feature is that the truth of a conditional deontic expression is interpreted situation-dependently. The situation-dependence of expressions are represented and reasoned about by an ordering relation and defeat of conditional expressions. As a result, a class of deontic dilemmas is resolved. We further propose a computation process for defeasible deontic reasoning based on clausal form logic programming paradigm. Finally, we demonstrate applications of defeasible deontic reasoning in commercial law and organizations.

The on-going research includes (1) the complete implementations of the University of Texas General Libraries Lending Code and the Secured Transactions of the Uniform Commercial Code, (2) a representation of the “speech-act” aspect of human behaviour, resulting in a model of electronic contracting systems, (3) a development of a deontic expert system by extending DX [25], and (4) managing changes in deontic rules while preserving their consistency.

## Acknowledgement

An earlier and preliminary version of Sections 2, 3, and 4 was presented at the First International Workshop on Deontic Logic in Computer Science, Amsterdam, The Netherlands, December 11-13, 1991 and in a research seminar at Erasmus University, Rotterdam, The Netherlands, August, 1992. Authors appreciate three anonymous referees of the workshop, workshop participants, and Erasmus University seminar participants, especially Professors C.E. Alchourrón (at Universidad de Buenos Aires, Argentinië), L. Åqvist (at University of Uppsala, Sweden), R. Hilpinen (at University of Turku, Finland), J.-J.Ch. Meyer (at Utrecht University, The Netherlands), R.J. Wieringa (at Vrije Universiteit, The Netherlands), for their comments and suggestions. Authors also appreciate the Editor-in-Chief of Decision Support Systems and anonymous referees for their constructive criticism. The paper is an extension of the first author's Ph.D. thesis. Authors are thankful to committee members of the thesis, especially Professors R. Causey (at The University of Texas at Austin, USA) and D. Nute (at The University of Georgia, USA).

## References

[1] C.E. Alchourrón and E. Bulygin, Normative Systems, Library of Exact Philosophy, Springer-Verlag, Wien, Austria, 1971.

[2] C.E. Alchourrón and D. Makinson, Hierarchies of regulations and their logic, In R. Hilpinen, editor, New Studies in Deontic Logic, pages 125–148, D. Reidel, Dordrecht, Holland, 1981.

[3] K.R. Apt, Introduction to logic programming, Technical Report TR-87-35 (Revised and Extended Version), Department of Computer Science, The University of Texas at Austin, 1988.

[4] L. Åqvist, Good samaritans, contrary-to-duty imperatives, and epistemic obligation, Noûs, 1(4):361–379, 1967.

[5] M. Belzer, Legal reasoning in 3-D, In Proceedings of The First International Conference on Artificial Intelligence and Law, Boston, Massachusetts, 1987.

[6] D. Bonevac, Deduction: Introductory Symbolic Logic, Mayfield, Palo Alto, CA, 1987.

[7] T.V. Carey, How to confuse commitment with obligation, The Journal of Philosophy, 72(102):276–284, 1975.

[8] R.M. Chisholm, Contrary-to-duty imperatives and deontic logic, Analysis, 24(2):33–36, 1963.

[9] K.L. Clark, Negation as failure, In H. Gallaire and J. Minker, editors, Logic and Data Bases, pages 293–322, Plenum Press, New York, NY, 1978.

[10] J.W. Decew, Conditional obligation and counterfactual, Journal of Philosophical Logic, 10(1):55–72, 1981.

[11] J.P. Delgrande, An approach to default reasoning based on a first-order conditional logic, In Proceedings of the Sixth National Conference on Artificial Intelligence, Seattle, WA, 1987.

[12] D.R. Dowty, R.E. Wall, and S. Peters, Introduction to Montague Semantics, D. Reidel, Dordrecht, 1981.

[13] R. Dworkin, Is law a system of rules, In R. Dworkin, editor, The Philosophy of Law, Oxford University Press, London, 1977.

[14] D. Føllesdal and R. Hilpinen, Deontic logic: An introduction, In R. Hilpinen, editor, Deontic Logic: Introductory and Systematic Readings, D. Reidel, Dordrecht, Holland, 1971.

[15] A. v.d. L. Gardner, Overview of an artificial intelligence approach to legal reasoning, In C. Walter, editor, Computer Power and Legal Reasoning, West Publishing, St. Paul, MN, 1985.

[16] M.L. Ginsberg, Counterfactuals, Artificial Intelligence, 30(1):35–79, 1986.

[17] P.S. Greenspan, Conditional oughts and hypothetical imperatives, The Journal of Philosophy, 22:259–276, 1975.

[18] B. Hansson, An analysis of some deontic logics, Noûs, 3:373–398, 1969.

[19] R. Hilpinen, editor, New Studies in Deontic Logic: Norms, Actions, and the Foundations of Ethics, D. Reidel, Dordrecht, Holland, 1981.

[20] P. Jackson, H. Reicheglt, and F. van Harmelen, editors, Logic-Based Knowledge Representation, The MIT Press, Cambridge, MA, 1989.

[21] G.A. Jentz, R.L. Miller, F.B. Cross, and K.W. Clarkson, West's Business Law: Alternate UCC Comprehensive Edition, West, St. Paul, MN, 4th edition, 1990.

[22] R.M. Lee, Bureaucracies as artificial intelligence, In L.B.

Methlie and R.H. Sprague Jr., editors, Knowledge Representation for Decision Support Systems: Proceedings of IFIP WG 8.3 Working Conference, North-Holland, Amsterdam, 1985.

[23] R.M. Lee, Bureaucracies as deontic systems, ACM Transactions on Office Information Systems, 6(2):87–108, 1988.

[24] R.M. Lee, H. Coelho, and J.C. Cotta, Temporal inferencing on administrative databases, Information Systems, 10(2):197–206, 1985.

[25] R.M. Lee and Y.U. Ryu, DX: A deontic expert system, to appear in: Journal of MIS, 1995.

[26] D. Lewis, Counterfactuals, Harvard University Press, Cambridge, MA, 1973.

[27] J.W. Lloyd, Foundations of Logic Programming, Springer-Verlag, Berlin, 2nd edition, 1987.

[28] R.P. Loui, Defeat among arguments: A system of defeasible inference, Computational Intelligence, 3:100–106, 1987.

[29] T. Maibaum, A logic for the formal requirements specifications of real-time embedded systems, Alvey FOREST Deliverable Report 3, Imperial College, 1986.

[30] D. Nute, Topics in Conditional Logic, D. Reidel, Dordrecht, Holland, 1980.

[31] D. Nute, A non-monotonic logic based on conditional logic, Research Report 01-007, Advanced Computational Methods Center, Univ. of Georgia, 1985.

[32] D. Nute, A logic for defeasible reasoning, In Proceedings of the 20th Hawaii International Conference on Systems Science, 1987.

[33] D. Nute, Defeasible reasoning and decision support systems, Decision Support Systems, 4:97–110, 1988.

[34] D. Nute, Defeasible reasoning and temporal projection, In Proceedings of the 22nd Hawaii International Conference on Systems Science, 1989.

[35] D. Nute, General and special defeasible logic, In Proceedings of Tübingen Workshop on Semantic Nets and Nonmonotonic Reasoning, 1989.

[36] R.B. Reich, The Resurgent Liberal (And Other Unfashionable Properties), Times Books, New York, NY, 1989.

[37] R. Reiter, On closed world data bases, In H. Gallaire and J. Minker, editors, Logic and Data Bases, pages 55–76, Plenum Press, New York, NY, 1978.

[38] W.D. Ross, The Right and the Good, Oxford University, New York, NY, 1930.

[39] J. van Benthem, Foundations of conditional logic, Journal of Philosophical Logic, 13(3):303–349, 1984.

[40] G.H. von Wright, Deontic logic, Mind, 60(237):1-15, 1951.

[41] G.H. von Wright, A new system of deontic logic, Danish Handbook of Philosophy, 1:173–182, 1964.

[42] G.H. von Wright, A correction to a new system of deontic logic, Danish Handbook of Philosophy, 2:103–107, 1965.

[43] G.H. von Wright, An essay in deontic logic and the general theory of action, Acta Philosophica Fennica, 21, 1968.

[44] R. Wieringa, J.-J.Ch. Meyer, and H. Weigand, Specifying dynamic and deontic integrity constraints, Data and Knowledge Engineering, 4(2):157–198, 1989.

[45] J.W. Wyatt and M.B. Wyatt, Business Law: Principles and Cases, McGraw-Hill, New York, NY, 6th edition, 1979.

![](/api/attachments/GZQJTPND/fulltext/images/832e3e70c7d1bdceda194464361844b74bbf568a4a3f07d0aac12e5ca1658ebe.jpg)

Young U. Ryu is Assistant Professor of Information Systems at the University of Texas at Dallas. He received his Ph.D. degree in Information Systems from the University of Texas at Austin. His research interests include logic-based modeling of bureaucracy policies and law, defeasible reasoning, nonmonotonic logic, artificial intelligence applications of management, and constraint logic program

ming of mathematical and economic models.  
![](/api/attachments/GZQJTPND/fulltext/images/27d07fcf98869c6b5d965f63ad57aa18cc6e028bb82a080aa01b1121feaa52f5.jpg)

Ronald M. Lee is currently Director of the Erasmus University Research Institute for Decision and Information Systems (EURIDIS), Rotterdam, The Netherlands. Previously he was Associate Professor of Information Systems at the University of Texas at Austin, Visiting Professor at the Universidade Nova, Lisbon, Portugal, and Research Scholar at the International Institute for Applied Systems Analysis (IIASA), Vienna, Austria. Re

search interests include intelligent network infrastructures, electronic contracting, computational deontics, and logic-based representations of bureaucratic regulations and procedures.
