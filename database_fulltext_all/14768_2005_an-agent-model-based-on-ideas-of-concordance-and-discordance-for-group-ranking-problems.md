---
otero_id: 14768
otero_key: "UNMFFMY7"
title: "An agent model based on ideas of concordance and discordance for group ranking problems"
authors: "Eduardo Fernandez; Rafael Olmedo"
year: "2005"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2004.01.004"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# An agent model based on ideas of concordance and discordance for group ranking problems

Eduardo Fernandez\*, Rafael Olmedo

Escuela de Informatica, Ciudad Universitaria-UAS, Universidad Autonoma de Sinaloa, C.P. 80040 Culiacan, Sinaloa, Mexico

Received 18 December 2002; received in revised form 22 January 2004; accepted 24 January 2004 Available online 16 March 2004

## Abstract

Classical decision theory does not provide a suitable theoretical basis for designing group decision agents because the concept of collective preference is not well defined. Here, we propose a model based on fuzzy preferences. A degree of truth is associated with the group preference relation. Fairness, equity, power of majority and compromise with significant minorities are modeled using concordance and discordance principles, reflecting the natural heuristic of collaborative groups making acceptable consensus decisions. Exploitation of the fuzzy group preference relation is performed solving a multiobjective optimization problem with an evolutionary algorithm. The designed agent shows very good performance in some test examples, obtaining better results than Condorcet and Borda methods. <sup>D</sup> 2004 Elsevier B.V. All rights reserved.

Keywords: Agent; Group ranking; Fuzzy preference relation; Concordance – discordance

## 1. Introduction

The concept of a rational decision agent has privileged the functional approach of decision-making. The main fact is that decision theory provides a general paradigm in concern with complex uncertain and conflicting environments, operating in such a way that a certain global model of preferences coming from human agents is built up and used to prescribe a rational behavior. In this sense, the agent’s rationality is defined as behavior that maximizes the expected satisfaction, modeled by a utility function (e.g. Ref. [29]).

In classical decision theory preference relations hold the axiom of perfect, transitive comparability (cf. Ref. [28]), a ‘‘hard’’ model which requires several ideal conditions that are not often satisfied in the practice of decision aiding, when ill-defined preferences and other sources of imprecision and vagueness produce phenomena such as non-transitivity and incomparability. Let us discuss in more detail the previous statement: Suppose that a weak preference binary relation c is defined on the decision set A agreeing with the decision-maker’s preferences; acb $( a , b { \in } A )$ is understood as ‘‘the decision-maker (DM) considers that a is at least as good as $b ^ { \prime \prime }$ . From a normative point of view (cf. Ref. [11]), a well-defined preference relation should be a weak order on A, that is b a,b,c<sup>a</sup>A, acb and $b \gtrsim _ { c } \Rightarrow a \succeq _ { c }$ (transitivity) and b (a,b)<sup>a</sup>A  A, (a,b)gc Z (b,a)<sup>a</sup>c (comparability).

These properties come from a paradigm of an ideal decision-maker. A real model hardly could be a precise description of a well-established system of preferences in the mind of a real decision-maker. When the DM is a mythical, inaccessible or vaguely defined entity, the model is only a system of preferences with which it is possible to analyze elements of a response to certain questions [27]. In many real situations, the scientist who built the model (the socalled decision analyst) hesitates about $a { \succ } b$ or $b { \succ } a$ or both from the DM’s point of view; these hesitations may come from (cf. Ref. [27]):

If the DM is a mythical, inaccessible, vaguely defined entity or even a well-precised entity with poorly defined preference rules, the decision analyst might not know how the DM compares a and b.

The existence in the DM’s mind (if the DM is a real person) of certain ‘‘zones’’ of uncertainty, imprecised beliefs, conflicts and competing aspirations.

These hesitations can produce situations in which the statement ‘‘the decision-maker considers that a is at least as good as $\boldsymbol { \mathrm { b } } ^ { \prime \prime }$ does not hold properties of a weak order. This phenomenon is modelled by outranking relations (cf. Ref. [25]). On the other hand, there are several methods based on building up a fuzzy preference relation (e.g. Refs. [3,12,27]). The preference relation, a non-doubtful true proposition in classical decision theory, is associated to certain degree of credibility in fuzzy approaches. Fuzzy binary preference relations may be considered as a compromise between value or utility functions and crisp outranking relations; fuzzy relations are numerical like value functions, but their power of expressivity is higher since they can easily model incomparability and non-transitivity (cf. Ref. [10]), which are frequent in real problems, with real and limited decision-makers.

In this paper, we are interested in autonomous intelligent agents for group decisions. When a decision situation involves multiple actors, each with different values and informational systems, the final decision will generally be the result of an interaction between this individual’s preferences and those of others. This interaction is not free of conflict, which may be due to any of a number of factors, e.g. different ethical or ideological beliefs, different specific objectives or different roles within an organization.

Group decision-making is usually understood as the reduction of different individual preferences on a given set to a single collective preference (cf. Ref. [17]). We will not focus on the psychological aspects of group interactions. The main goal of this work is the prescription of a final group ranking from these individual preferences once they have been established.

Group decision-making covers a wide range of situations. We are interested in a problem with the following characteristics:

a. Each actor considers the same set of alternatives or potential actions.

b. The preference of each actor can accurately be represented by a ranking (with ties) of all alternatives from best to worse.

c. Homogeneity. All group members have the same importance for deriving final agreement.

d. The group members accept a final ranking derived from an aggregation of their opinions with fairness and equity.

Following Ref. [11], the problem can be formalized as: Let $A { = } \{ a _ { 1 } , . . . , a _ { M } \}$ be the decision set. Let G be the set of group members and N its cardinal. Let us suppose that each individual has considered how he would rank the actions of A if he or she alone were responsible for the choice. Let $R _ { i }$ be the weak preference ordering on A provided by the i-th individual. Given the N individuals and their preferences $R _ { i } , i = 1 , \ldots N ,$ we must prescribe how to derive from them a preference order $R _ { g }$ of A for the group as a whole.

Classical decision theory is very limited in approaching this kind of problem, because the group preference (the so-called collective preference, an intuitive concept) is poorly defined. Often, a collective opinion is identified with one that arises when certain voting rules, which define ‘‘the group constitution’’ are applied. However, according to Arrow’s Impossibility Theorem (cf. Ref. [1]), there is no aggregation method of individual rankings satisfying simultaneously the properties of universal domain, transitivity, unanimity, independence with respect to irrelevant alternatives and non-dictatorship, which are considered like components of a rational paradigm. Since the Condorcet’ Paradox was identified, it was clear that, in most popular voting systems (for instance, those based on pair-wise comparisons combined with majority rules), the binary group preference relation provided by these systems was not transitive, leading to a final ordering $R _ { g }$ depending on the voting schedule (e.g. Refs. [2,11]). Classical decision approaches do not handle incomparability, which can arise when important disjoint minorities are strongly against both assertions $^ { * } a$ is collectively preferred to $b ^ { \prime \prime }$ and $^ { 6 6 } b$ is collectively preferred to $\boldsymbol { a } ^ { \flat }$

Intuitively, to affirm the collective preference of a on b is only possible when consensus of the group exists or if the following conditions are held:

## i. A clear majority in favor of the preference.

ii. The minority against is very weak numerically or the intensity of its opposition is not significant.

Otherwise, it is not possible to use bivalent 0–1 logic to characterize the statement about collective preference. We propose here a model based on fuzzy preferences. The statement ‘‘a is collectively considered at least as good as $b ^ { \prime \prime }$ is considered as a fuzzy proposition and a degree of truth is associated with it. This degree increases with the power of majority coalition (concordance effect) and decreases (even it becomes zero) with the strength of minority coalitions (discordance effect). Power of majority is taken into account using certain measure of concordance. Necessary compromises with important minorities are modeled using veto functions. These ideas of concordance and discordance were formerly proposed in the framework of outranking relations and Multi Criteria Decision Aid (cf. Refs. [27,28]).

This paper is organized as follows: Main criticisms to previous approaches are discussed in Section 2. Having established this background information, the main proposal of this paper is detailed in Section 3 and the exploitation method for deriving a final group ranking is exposed in Section 4. Some test problems are illustrated in Section 5 and finally Section 6 closes with some concluding remarks.

## 2. A brief outline of previous approaches to group ranking problem (GRP)

We do not pretend here to review the vast literature devoted to group decision models, GRP and social choice since the 18th century (e.g. Refs. [1,6,9,13,14,16,17,22,24]). A rough classification follows:

A. Methods based on scoring functions (e.g. Refs. [2,23])

B. Methods based on minimizing a distance measure (e.g. Ref. [4])

C. Methods based on some ways to count votes in favour of the proposition Vthe group prefers $a _ { i }$ to $a _ { k } \sp \prime , \ i = 1 , \ . . . , M , \ k = 1 , \ . . . , M , \ i \ne k \ ( \mathrm { e . g . }$ Refs. [9,30])

D. To consider each group member as a criterion of a multicriteria problem, using then some MCDM technique to obtain the best ranking (e.g. Refs. [18,22])

E. To define a valued preference relation on $A \times A$ using after an exploitation method for rank ordering (cf. Refs. [20,22]).

The idea of scoring was first proposed by Jean Charles de Borda in 1781 when he wrote a paper proposing what we will referred to ‘‘the Borda count’’, whose equivalence to minimize a distance was proved 200 years later [4]. Different scoring and distance functions have been proposed (cf. Ref. [23]) (many inspired in the Borda count), but all suffer of two weak points: (1) dependence with respect to irrelevant alternatives (that is, the fact considered by many like irrational, on which the position of two alternatives $^ { a , b }$ in the ranking $R _ { g }$ depends not only of the group explicit preference concerning $^ { ( a , b ) }$ , but also of the presence of other alternatives within the decision set; the relative position of a and b in the final ranking can change when another action c is included in (or excluded from) the decision set); and (2) compensation (a strong disagreement of a minority can be compensated by a good agreement of remaining voters, an effect which produces certain dictatorship of majority). Point 1 leads to irrational situations, which have been discussed in many references (e.g. Ref. [11]). To cite a well-known example in which the controversial character of that dependence is pointed-out, let us suppose a customer walks into a restaurant and notes from the menu that there are only two possible and cheap main courses, rump steak and roast chicken. He chooses the chicken; however, the waiter arrives and communicates that there is also a very nice option of shrimp. Against all rationality, the customer immediately changes his choice and eats the steak. Point 2 could affect fairness and equity concerning minorities, because it does not favor compromises with them. Fairness and equity are very related ethical concepts. The first concerns the preferences of individuals and groups, the way in which they influence on final decisions and the ways in which they consider themselves in relation to others. Equity is usually interpreted as a sort of equality, meaning that people should be considered equal and treated with equal concern and respect (cf. Ref. [21]). There is a little or no strong disagreement in solutions with fairness and equity [21]. That effect (majority dictatorship) is symptomatic of lack of fairness and equity, and can produce a deep dissatisfaction and instability of the group. Majority dictatorship is acceptable as a result of applying rules previously admitted by the group (group constitution). However, to make compromises with important and strongly unsatisfied minorities approaches the group final decision to a reasonable agreement, perhaps a consensus.

Phenomena such as non-transitivity and cycles are usual when a group preference relation is built up based upon the power of a ‘‘winning coalition’’ (point C), which also suffer of dictatorship of majority. The first method in this category was proposed by Condorcet in 1785; it fails when there is not a ‘‘Condorcet winner’’. Many voting techniques are only variants of the Condorcet method (cf. Refs. [2,9]).

The idea of introducing a supra decision-maker and considering each member as a separate criterion of a multicriteria decision problem was first proposed by Ref. [18]. The intent of constructing an ordinal group value function from individual preference functions has some important difficulties [11]. This approach needs to know cardinal value functions $\nu _ { 1 } , . . . ,$ v<sub>N</sub> corresponding to each member, which should be built using a common scale; however, there is no satisfactory method of making meaningful interpersonal comparisons of preferences. It is the main reason of introducing a supra decision-maker responsible for all interpersonal comparisons; however, we observe some drawbacks: firstly, the group should accept his/her judgments without question; secondly, this approach seems too complicated to be implemented by an autonomous software agent; finally, some important questions about fairness, equity and minority rights are not well answered.

The idea of using fuzzy preference relations to model group preferences is very attractive. Some interesting approaches introduced a model of consensus based on the use of linguistic to provide individu-$\mathrm { a l s } ^ { \prime }$ opinions and on the use of the concept of fuzzy majority represented by means of a linguistic quantifier (cf. Refs. [13,14]). However, the following idea leads to a more straightforward generalization of classical decision theory based on the properties of the weak preference relation $\succ \colon \mathrm { A }$ proposition such as $^ { * } a$ is collectively considered at least as good as $b ^ { \prime \prime }$ (denoted $a S _ { g } b )$ is considered as an assertion with a degree of truth $\sigma ( a , b )$ in [0,1]. The proposition $a S _ { g } b$ has a membership value $\mu ( a S _ { g } b ) = \sigma ( a , b )$ to the fuzzy set of true assertions about group binary preferences. There is a certain cut-level k such that $a S _ { g } b \Leftrightarrow \mu ( a S _ { g } b ) \geq \lambda$ Phenomena such as non-transitivity $( a S _ { g } b$ and $b S _ { g } c$ and $a n S _ { g } c )$ and incomparability $( a n S _ { g } b$ and $b n S _ { g } a )$ are easily handled by this model. No conditions are imposed on the actor of decision-making process, and therefore ill-defined preferences (such as in group decision) are easily modeled. Within these methods, it is common to distinguish two different steps:

\- The construction step in which a fuzzy preference relation is built. It should express the degree of credibility associated with the non-fuzzy preference relation.

\- The exploitation step in which the fuzzy preference relation is used to derive a ranking of A.

In order to be applied to GRP, the main problem is to build up a fuzzy preference relation representing a degree of truth of a proposition about collective preferences. Accepted principles of democracy, fairness and equity should be taken into account by a good model. A compensatory scheme makes difficult to avoid a dictatorship of majority and therefore such scheme does not seem to be able to achieve a good reflex of group preferences. Recently, a method inspired in ELECTRE III methodology was proposed to solve the multicriteria group ranking problem (cf. Ref. [20]). The main advantage of ELECTRE is the use of ideas of concordance and discordance, which concern the way in which groups make heuristic pair wise comparisons. Veto effects combined with majority rules and thresholds are considered in ELECTRE methodology (cf. Refs. [25,27]), becoming useful as tools to model basic principles of democracy and respect to important minorities. In Ref. [20], concordance and discordance are modeled in a way very similar to ELECTRE III.

We defend the convenience of modeling group preferences with fuzzy outranking relations using concordance and discordance measures, but not necessarily the construction of the binary fuzzy relation should be similar to the scheme of ELECTRE III. In ELECTRE I, II and III methods, the concordance index is equal to 1 only when all criteria agree with outranking (cf. Refs. [25,27]). Such high power of concordance coalition is extreme in group decision, where a qualified majority without veto condition is usually considered high enough to establish a nondoubtful group preference. In this sense, the proposal by Ref. [20] can be objected. Here, we propose an improved model of fuzzy group preference relation.

On the other hand, most popular techniques of exploitation are based on some scoring functions, which can receive similar criticisms of methods in point A. Recently, a new approach with good properties has been proposed based on solving a multiobjective optimization problem in which the objective functions are positive and negative arguments about the quality of prescription (cf. Refs. [7,8]).

## 3. A fuzzy outranking relation for aggregating group preferences

## 3.1. Preliminary definitions

Definition 1. We say that action a outranks action $a ^ { \prime }$ from the point of view of actor k (restricted outranking relation $a S _ { k } a ^ { \prime } )$ if and only if $a R _ { k } a ^ { \prime }$

Definition 2. An actor k is in concordance with the assertion $a S _ { g } a ^ { \prime } \ ( S _ { g }$ means a is collectively considered at least as good as $a ^ { \prime \prime \prime } )$ , if and only if $a S _ { k } a ^ { \prime }$

In the following, $C ( a S _ { g } a ^ { \prime } )$ will denote the concordant coalition, the set of actors which are in concordance with $a S _ { g } a ^ { \prime } . n _ { c } { = } \mathrm { c a r d } \{ C ( a S _ { g } a ^ { \prime } ) \}$

Definition 3. An actor k is in discordance with the assertion $a S _ { g } a ^ { \prime }$ if and only if $a n R _ { k } a ^ { \prime } . \ D ( a S _ { g } a ^ { \prime } )$ will denote the discordant coalition, joining the actors which are in discordance with $a S _ { g } a ^ { \prime }$ V. Let us denote $n _ { d } = \mathrm { c a r d } \{ D ( a S _ { g } a ^ { \prime } ) \}$

Note that $C ( a S _ { g } a ^ { \prime } ) \cup D ( a S _ { g } a ^ { \prime } ) = G$ and $C ( a S _ { g } a ) \cap$ $D ( a S _ { g } a ^ { \prime } ) = \emptyset .$

## 3.2. Extreme discordance and veto effect

Let $u _ { k } \colon A \longrightarrow N$ be a function defined as

$$
u _ {k} (a _ {i}) = \operatorname{card} (B)
$$

where $B { = } \{ a _ { j } { \in } A \colon a _ { i } \ R _ { k } \ a _ { j }$ and $a _ { j } ~ n R _ { k } ~ a _ { i } \} ~ ( n R _ { k }$ means negation).

Note that, if $a _ { i }$ is the best in $R _ { k } ,$ then $u _ { k } ( a _ { i } ) =$ card $( A ) - 1 . { \mathrm { I f } } a _ { i }$ is the worst ranked, $u _ { k } ( a _ { i } ) = 0$

We can distinguish five different situations:

$u _ { k } ( a ) \gg u _ { k } ( a ^ { \prime } )$ denotes the case in which action a is ranked as one of the best action, while $a ^ { \prime }$ is one of the worst (this classification is defined by agent designer)

$u _ { k } ( a ) { > } u _ { k } ( a ^ { \prime } )$ denotes when action a is ranked better than $a ^ { \prime } ,$ but the previous situation does not hold.

$- u _ { k } ( a ) = u _ { k } ( a ^ { \prime } )$ actions a and $a ^ { \prime }$ are tied in the ranking, or their difference is negligible.

$$
- u _ {k} \left(a ^ {\prime}\right) > u _ {k} (a)
$$

$$
- u _ {k} \left(a ^ {\prime}\right) \gg u _ {k} (a).
$$

Here, it is not possible to assess a quantitative meaning to the statements ‘‘one of the best ranked actions’’ and ‘‘one of the worst’’. It depends on the number of ranked actions and ties. The agent designer, with his specific knowledge about the problem being approached, should be able to precise this issue. Roughly, we could use the following criteria:

\* If $M { \leq } 3$ , the concept $u _ { k } ( a ) \gg u _ { k } ( a ^ { \prime } )$ is not defined.

\* If $M = 4 , \ 5 , \ 6 , \ u _ { k } ( a ) \gg u _ { k } ( a ^ { \prime } )$ means a is the best ranked and $a ^ { \prime }$ the worst.

$^ { * } \mathrm { I f } \ M { = } 7 , u _ { k } ( { \mathrm { a } } ) { \gg } u _ { k } ( a ^ { \prime } )$ means $u _ { k } ( a ) - u _ { k } ( a ^ { \prime } ) = 5 , 6 .$

$^ { * } \mathrm { I f } \ M { = } 8 , u _ { k } ( a ) { \gg } u _ { k } ( a ^ { \prime } )$ means $u _ { k } ( a ) - u _ { k } ( a ^ { \prime } ) = 6 , 7$

\* If $M { = } 9 , \ u _ { k } ( a ) { \gg } u _ { k } ( a ^ { \prime } )$ means $u _ { k } ( a ) = 7$ or 8 and $u _ { k } ( a ^ { \prime } ) = 0 \ \mathrm { o r } \ 1$

\* If $M \geq 1 0$ , take the top 20% and the bottom $2 0 \% ,$ respectively, as reference levels for ‘‘one of the best’’ and ‘‘one of the worst’’.

Definition 4. An actor k belongs to veto coalition V $( a S _ { g } a ^ { \prime } )$ if and only if $u _ { k } ( a ^ { \prime } ) \gg u _ { k } ( a )$ . Let us call $n _ { \nu } =$ card $\{ V ( a S _ { g } a ^ { \prime } ) \}$

## 3.3. The concordance index

It measures the strength of arguments in favor of $a S _ { g } a ^ { \prime }$ , which are included in C. We propose a simple continuous piece wise linear model based on notable points $n _ { c } = 1 / 3 N$ and $n _ { c } { = } 2 / 3 N$ (qualified minority and majority, respectively) that follows (Fig. 1):

$$
c (a, a ^ {\prime}) = \left\{ \begin{array}{l l} 1 & \text { if } n _ {c} \geq 2 / 3 N \\ (3 / N) n _ {c} - 1 & \text { if } 1 / 3 N \leq n _ {c} <   2 / 3 N \\ 0 & \text { if } n _ {c} \leq 1 / 3 N \end{array} \right.\tag{1}
$$

Remark. Note that, when $n _ { c } = 1 / 2 N ,$ we have $c ( a , a ^ { \prime } ) { = } 0 . 5$

## 3.4. The power of veto coalition

In order to determine if a veto condition holds, we should consider the following issues:

1. The number of actors in strong disagreement with $a S _ { g } a ^ { \prime } ( n _ { \nu } )$ . We should identify two real numbers $\rho , \eta$ $( 0 < \rho < 1 / 4 )$ , $( \rho < \eta < 1 / 2 )$ such that (a) if $n _ { \nu } \ge \rho N$ the power of veto coalition starts to weakening the outranking and (b) if $n _ { \nu } \ge \eta N$ its power is so high that no credibility is associated to $a S _ { G } a ^ { \prime }$ whichever $c ( a , a ^ { \prime } )$ could be.

2. The level of concordance. It is obvious that given $n _ { \nu } \left( \rho N { \leq } n _ { \nu } { \leq } \eta N \right)$ the credibility of a veto condition is a decreasing function of $c ( a , a ^ { \prime } )$ .

![](/api/attachments/UNMFFMY7/fulltext/images/7ce47ad60f9e55e9e220cd669d73addf60abd59a3b6d87c313ba9877a3de609d.jpg)  
Fig. 1. Concordance Index.

![](/api/attachments/UNMFFMY7/fulltext/images/38835b9f3523dcb4960da2bbf79c0b410f7c279ea68b09355a01e3d4d4bd9138.jpg)  
Fig. 2. Weakness of the veto coalition as a function of $\mathrm { n } _ { \mathrm { v } }$

We propose to model these issues introducing a function $\varphi ( n _ { \nu } , n _ { c } )$ measuring the weakness of the veto coalition. Fixed $n _ { c } ,$ the one-dimensional function $\phi ( n _ { \nu } ) = \varphi ( n _ { \nu } , n _ { c } )$ is defined as a continuous piece wise linear model that follows (Fig. 2):

$$
\phi (n _ {v}) = \left\{ \begin{array}{l l} 1 & \text { if } n _ {v} \leq \rho N \\ ((I _ {v} - 1) n _ {v} + N (1 / 4 - \rho I _ {v})) / (N (1 / 4 - \rho)) & \text { if } \rho N <   n _ {v} <   1 / 4 N \\ I _ {v} & \text { when } n _ {v} = 1 / 4 N \\ I _ {v} (\eta N - n _ {v}) / ((\eta - 1 / 4) N) & \text { if } 1 / 4 N <   n _ {v} <   \eta N \\ 0 & \text { if } n _ {v} \geq \eta N \end{array} \right.\tag{2}
$$

$I _ { \nu }$ is a value between 0 and 1, expressing the weakness of veto coalition when $n _ { \nu } = 1 / 4 N ,$ a significant minority but not so important to become in zero the degree of truth of $a S _ { g } a ^ { \prime }$

The dependence of $\varphi ( n _ { \nu } , n _ { c } )$ with $n _ { c }$ is now introduced considering that $I _ { \nu }$ is a monotonic increasing function of $n _ { c } .$ Note that fixed $n _ { \nu } \varphi ( n _ { \nu } , n _ { c } )$ increases monotonically with $n _ { c }$ . We suggest the following very simple model for $I _ { \nu } ( n _ { c } )$ based on the generally accepted level of qualified majority $( n _ { c } { = } 2 / 3 N )$ :

$$
I _ {v} = \left\{ \begin{array}{l l} I _ {1} & \text { if } n _ {c} \geq 2 / 3 N \\ I _ {2} & \text { if } n _ {c} <   2 / 3 N \end{array} \right.\tag{3}
$$

$I _ { 1 }$ and $I _ { 2 } \left( I _ { 1 } { > } I _ { 2 } \right)$ are constant belonging to (0,1).

The set of parameters included in the model should be assessed by the agent designer. We suggest to take $\rho$ between 0.1 and 0.2, g between 1/3 and $2 / 5 ; I _ { 1 }$ and $I _ { 2 }$ should be assessed according to the value chosen for $\eta ;$ if $\eta = 1 / 3$ , we suggest $I _ { 1 } = 1 / 2$ and $I _ { 2 } = 1 / 3$

## 3.5. A fuzzy group preference relation

The precedent models allow us to define a fuzzy group preference relation as follows:

$$
\sigma_ {g}: A \times A \to [ 0, 1 ]
$$

$$
\sigma_ {g} (a, a ^ {\prime}) = c (a, a ^ {\prime}) \varphi (a, a ^ {\prime})\tag{4}
$$

where $c ( a , a ^ { \prime } )$ and $\varphi ( a , a ^ { \prime } )$ are given by Eqs. $( 1 ) - ( 3 )$ $\sigma _ { g }$ should be interpreted as the degree of credibility of the assertion $^ { * } a$ is collectively considered at least as good as $b ^ { \prime \prime }$ . If the veto coalition is empty or very weak, $\sigma _ { g } ( a , a ^ { \prime } ) = c ( a , a ^ { \prime } )$ . But this credibility is reduced when its strength increases, vanishing when that minority strongly unsatisfied is considered as sufficiently important.

## 4. The exploitation method for deriving a final ranking

Let us present a short view of a recent proposal discussed in detail in Ref. [8] improving the approach suggested by Refs. [7,19].

Let r be a fuzzy preference relation defined on $A \times A$ with image in [0,1]. $\sigma ( x , y )$ can be interpreted as the credibility degree of the proposition $^ { 6 6 } x$ is at least as good as $y '$ . Let $\lambda$ be a real number in [0,1] such that, if $\sigma ( x , y ) \geq \lambda$ , we say that x outranks y with credibility $\lambda ,$ denoted by xS(k)y. Otherwise, the outranking is rejected $( x n S ( \lambda ) y )$

We assume the existence of a threshold $\beta { > } 0$ such that, if $x S ( \lambda ) y$ and also $\sigma ( y , x ) \le ( \lambda - \beta )$ , then there is an asymmetric preference relation favoring x that will be denoted by $x P ( \lambda , \beta ) y .$ It can be agreed that for some values of $\lambda$ and $\beta ,$ the conditions defining $P ( \lambda , \beta )$ are good arguments for justifying a strict preference relation in the sense proposed by Roy [28].

Let $R _ { \sigma }$ be a total preorder on A, derived from r using an exploitation method. If $( a , b ) { \in } R _ { \sigma }$ and $( b , a ) \notin R _ { \sigma }$ we say that a is ranked higher than b (a is prescribed as better than b). If $( a , b ) { \in } R _ { c }$ and $( b , a ) { \in } R _ { \sigma } ,$ , a and $b$ are $ { { } ^ { 6 6 } } \mathrm { e x }$ aequo’’, no one is prescribed as better than the other. It allows to rank all the actions in decreasing order of preference, deriving a prescription for the concerning decision-making problem.

Let us consider also the following definitions.

The set of strong discrepancies is defined as: $\mathrm { S D } { = } \{ ( x , y ) { \in } A \times A $ such that $x P ( \lambda , \beta ) y$ and $y R _ { \sigma } \mathrm { x } \}$ ; card(S) is denoted by $n _ { \mathrm { S D } }$

The set of incomparable actions is defined as $I { = } \{ ( x , y ) { \in } A \times A$ , such that xn $S ( \lambda ) y$ and $y n S ( \lambda ) x \}$ ; (card(I))/2 is denoted by $n _ { I } .$

Remark. Note that $( x , y ) { \in } I { \Rightarrow } ( y , x ) { \in } I .$ We are not interested in counting simultaneously $( x , y )$ and $( y , x )$ Therefore, we divide per two the cardinal of the set I. $n _ { \mathrm { S D } }$ is a function of R , k and $\beta ; n _ { I }$ is a function of k. Given $R _ { \sigma } , ~ n _ { \mathrm { S D } }$ is a decreasing function of $\lambda ,$ but $n _ { I }$ increases monotonically with k. Note also that Max $n _ { I } { = } M ( M - 1 ) / 2$

In Ref. [19], the prescribed ranking is obtained as a compromise solution to the problem

$$
\underset {R _ {\mathrm{s}}, \lambda \text {with} \lambda \in \mathfrak {N}} {\text {Min}} (n _ {\mathrm{SD}}, n _ {I}), \underset {} {\text {Max}} \lambda\tag{5}
$$

$R _ { \mathrm { s } }$ denotes strict total orders of A considered like variables in this optimization problem.

The minimization of $n _ { \mathrm { S D } }$ can be regarded as a process of reducing the magnitude of the arguments against $R _ { \sigma } .$ . Increasing k improves the credibility of $P ( \lambda , \beta )$ and $S ( \lambda )$ , relations on which the ranking is based. A value of $\lambda$ between 0.65 and 0.75 could be considered sufficient for establishing a likely outranking (cf. Ref. [25]) and no further increments are normally required. Several consistency properties of solutions containing minimum strong discrepancies were derived in Ref. [7], including an improved robustness respect to irrelevant alternatives.

Note that Eq. (5) is a combinatorial multiobjective optimization problem in which the decision variables are rankings and real numbers. Its difficulty increases exponentially with M. Its structure strongly suggests the use of Evolutionary Algorithms (EAs). In the last years, EAs have become in a powerful tool for solving difficult problems in different fields, and in particular, for the treatment of the nonlinearity and of the global optimization in polynomial time. EAs are less sensitive to the mathematical properties of objectives and constraints than the traditional mathematical programming techniques. Additionally, in case of problem (5), an EA helps to handle its exponential complexity because computer efficiency of these methods is less sensitive to problem size in comparison to the traditional techniques.

Fuzzy logic controllers and fuzzy preferences have been used to improve performance of EAs (cf. Refs. [5,15]). Here, following Ref. [19], we propose an evolutionary approach to improve a decision-making process based on fuzzy binary preferences.

In Ref. [19], an EA which uses preemptive priority for $n _ { \mathrm { S D } }$ was suggested. However, this lexicographic approach can fail when $P ( \lambda , \beta )$ has cycles for high k values due to an existing narrow connection between cycles and strong discrepancies such as was established by Ref. [7].

A more operational method for solving Eq. (5) was proposed by Ref. [8] and it is an important tool used in the present work for exploiting the fuzzy group preference relation from Section 3 and obtaining a final ranking. The main idea is to consider separately the following sub-problems:

$$
\text { Max } \lambda , \underset {\lambda} {\text { Min }} n _ {I}\tag{6}
$$

and

$$
\text { Min } n _ {\mathrm{SD}} (R _ {\mathrm{s}}, \lambda^ {*})\tag{7}
$$

where $\lambda ^ { * }$ corresponds to the best compromise of problem (6). In Ref. [8], authors suggest a simple interactive adjustment of $\lambda ^ { * } \operatorname { i f } n _ { \mathrm { S D m i n } } = \operatorname { M i n } n _ { \mathrm { S D } } ( \lambda ^ { * } )$ is different from zero.

For each $( x , y ) { \in } A \times A , \alpha ( x , y )$ is defined as follows:

$$
\alpha (x, y) = \max (\sigma (x, y), \sigma (y, x))
$$

Note that $\alpha ( x , y ) = \alpha ( y , x )$ . Hence, there are at most $L = M ( M - 1 ) / 2$ different $\alpha ( x , y )$ in $A \times A . ~ \alpha _ { 1 } \leq \alpha _ { 2 } \leq$ $\dots \le \alpha _ { L }$ denote the values of $\alpha ( x , y )$ in $A \times A .$

In order to justify the method for solving Eq. (6), the following result was presented by Ref. [8].

Theorem. Under previous notation, the set of objective vectors $( n _ { I } ( \alpha _ { k } ) ,$ $\boldsymbol { \alpha _ { k } } )$ is the complete set of Pareto optimal solutions of sub-problem $( 6 )$

As a consequence of this theorem, the cardinal of the Pareto set is at most $M ( M - 1 ) / 2$ , and it can be easily explored in order to find a good compromise between $n _ { I }$ and k. This compromise solution denoted by $\lambda ^ { * }$ will be used to minimize $n _ { \mathrm { S D } }$ . If $n _ { \mathrm { S D m i n } } ( \lambda ^ { * } )$ is not satisfactory, the decision-maker can interactively increase k for improving $n _ { \mathrm { S D } } ,$ keeping for a minimally acceptable card(S(k)) (i.e. n<sub>I</sub>).

In order to minimize $n _ { \mathrm { S D } } ( \lambda ^ { * } , \ R )$ , Ref. [7] proposed an EA that is in some extent similar to the one discussed by Ref. [19]. Let us explain it very shortly.

An individual is represented as a string of M-ary alphabet. In such a representation, each alternative is coded into M-ary form. Then, they are then linked together to produce a long M-ary string or individual (so-called chromosome in Genetic Algorithms). An alternative coded as $a _ { k i }$ in the i-th entry of the string means that it is ranked at the i-th place of the ordering, and $a _ { k i }$ is preferred to $a _ { k j }$ if $i < j ,$ , where $a _ { k i } { \in } A { = } \{ a _ { 1 }$ $a _ { 2 } , . ~ . ~ . , a _ { M } \} , ~ i = 1 , ~ 2 , ~ . ~ . \cdot , ~ M ,$ and $[ k _ { 1 } , k _ { 2 } , . . . , k _ { M } ]$ is a permutation of $[ 1 , 2 , . . . , M ]$

The schematic representation of an individual (solution of ranking problem) is illustrated in Fig. 3.

Another important concern is the fitness function $f .$ Fitness measures ‘‘how good’’ an individual is with regards to solve the ranking problem; this measure is used during the selection and replacement phases. Ref. [8] takes $f { = } n _ { \mathrm { S D } }$

A k-ary tournament selection method is used for parent selection, in which k individuals are chosen randomly from the population, and the fittest is then put in a reproductive trial. In order to produce an offspring, two k-ary tournaments are performed, each one produces a parent string. These two parent strings are then combined to produce an offspring.

The crossover operator takes genes from each parent string and ‘‘combines’’ them to create a child string. Working with permutation encoding, it is necessary to create a crossover operation, which should be specific to this way of encoding. Refs. [8,19] proposed the crossover operator UX2 first introduced by Ref. [26]. It is explained in Fig. 4.

<table><tr><td>1</td><td>2</td><td>3</td><td>4</td><td>i</td><td>M-1</td><td>M</td><td>← place in the ordering</td></tr><tr><td> $a_{k_1}$ </td><td> $a_{k_2}$ </td><td> $a_{k_3}$ </td><td> $a_{k_4}$ </td><td>...</td><td> $a_{ki}$ </td><td>...</td><td> $a_{k_{M-1}}$ </td></tr></table>

Fig. 3. Schematic representation of a chromosome.

![](/api/attachments/UNMFFMY7/fulltext/images/11efb0e444605808c1249cde32a93fe078c7283b89d0e25237cca583eecab627.jpg)  
Fig. 4. The union crossover 2 (UX2).  
5. Set $t = t + 1$

The mutation operator is applied to the offspring string generated after crossover. It works by interchanging a pair of randomly chosen genes in an individual.

The population replacement scheme is very simple. Once an offspring has been generated it will replace the ‘‘less fitted’’ member of the population (i.e. the individual with maximum $n _ { \mathrm { S D } }$ in current population).

Summary of an EA for solving sub-problem (7):

1. Generate an initial population of N1 random solutions. Set iteration counter $t = 0$

2. Select two individuals $P _ { i }$ and $P _ { j }$ from the population using k-ary tournaments.

3. Combine $P _ { i }$ and $P _ { j }$ to form a new solution O using the UX2 crossover operator.

4. Mutate two randomly selected genes in $O .$

6. Replace the less fitted individual in the population by O.

7. Repeat steps 2–6 until t = GEN solutions have been generated, where GEN is the number of generations.

More specifically, we have used the following parameters in the EA:

<table><tr><td>Population size</td><td>50</td></tr><tr><td>Number of generations</td><td>500</td></tr><tr><td>Cardinal of the k-ary tournaments</td><td>5</td></tr><tr><td>Crossover probability</td><td>0.8</td></tr><tr><td>Mutation probability</td><td>0.5</td></tr></table>

Note that encoding as a string leads to solutions being strict rankings. To obtain a weak order allowing ties, we should perform many trials. A statistical distribution of these strict orderings gives us the necessary information to decide about proper positions in final ranking. It will make clear in some examples.

## 5. Some computational experiments

## 5.1. Example 1

Let $\{ A , B , C , D \}$ be the set of alternatives for a 4 voters election. The member rankings R are shown in Table 1:

The Borda count (4 points to the first alternative, 3 points to the second and so on) suggests a ranking $( A \sim B ) { > } C { > } D$ . The strong opposition against A shown in $R _ { 3 }$ is compensated by $R _ { 1 }$ and $R _ { 4 }$

Calculating the concordance indexes according to Eq. (1), we obtain the results pointed out in Table 2.

The unique relevant veto situation happens when $\sigma _ { g } ( A , C )$ is analyzed. The third member $\left( R _ { 3 } \right)$ belongs to veto coalition. We have $n _ { \nu } = 1 / 4 N ,$ $n _ { c } { = } 3 / 4 N$ and choosing $\rho { = } 0 . 1$ $\eta = 1 / 3$ $I _ { \nu } = 0 . 5 ,$ then from Eqs. (2) and (3) $\varphi ( A , C ) = 0 . 5 .$ . Combining it with the concordance matrix and using Eq. (4), we arrive to the fuzzy group preference relation shown in Table 3.

The next step consists of using the exploitation method described in Section 4. The agent for this phase was coded in Builder C++, running on a PC Pentium III, 900 MHz. Choosing k = 0.5 and using the EA exposed in Section 4 we obtained many different solutions (strict rankings) satisfying $n _ { \mathrm { S D } } { = } 0 ;$ ; the number of times that an alternative is found at a certain place in the ranking is given in Table 4 with respect to 100 variations of the seed parameter. The run time was 42 s (for 100 trials).

Table 1  
Member rankings

<table><tr><td> $R_1$ </td><td> $R_2$ </td><td> $R_3$ </td><td> $R_4$ </td></tr><tr><td>A</td><td>B</td><td>C</td><td>A</td></tr><tr><td>B</td><td>A</td><td>D</td><td>B</td></tr><tr><td>C</td><td>C</td><td>B</td><td>C</td></tr><tr><td>D</td><td>D</td><td>A</td><td>D</td></tr></table>

Table 2  
Concordance matrix

<table><tr><td></td><td>A</td><td>B</td><td>C</td><td>D</td></tr><tr><td>A</td><td>-</td><td>0.5</td><td>1</td><td>1</td></tr><tr><td>B</td><td>0.5</td><td>-</td><td>1</td><td>1</td></tr><tr><td>C</td><td>0</td><td>0</td><td>-</td><td>1</td></tr><tr><td>D</td><td>0</td><td>0</td><td>0</td><td>-</td></tr></table>

Table 3  
The fuzzy group preference relation

<table><tr><td></td><td>A</td><td>B</td><td>C</td><td>D</td></tr><tr><td>A</td><td>-</td><td>0.5</td><td>0.5</td><td>1</td></tr><tr><td>B</td><td>0.5</td><td>-</td><td>1</td><td>1</td></tr><tr><td>C</td><td>0</td><td>0</td><td>-</td><td>1</td></tr><tr><td>D</td><td>0</td><td>0</td><td>0</td><td>-</td></tr></table>

(For instance, the number 100 in the first row, column corresponding to A, means that this alternative occupied the highest position in 100 optimal individuals generated during 100 runs each with different seed.)

These results suggest the same ranking as Borda method did. But if we judge $\lambda = 0 . 5$ as too low credibility and choose k = 1, we obtain other results (different from previous ones) pointed out in Table 5.

These new results suggest an ordering $B { > } A { > } C { > } D ,$ which seems to be a consensus ranking.

Table 4  
Results with different trials

<table><tr><td></td><td>A</td><td>B</td><td>C</td><td>D</td></tr><tr><td>1</td><td>100</td><td>100</td><td>0</td><td>0</td></tr><tr><td>2</td><td>100</td><td>100</td><td>0</td><td>0</td></tr><tr><td>3</td><td>0</td><td>0</td><td>200</td><td>0</td></tr><tr><td>4</td><td>0</td><td>0</td><td>0</td><td>200</td></tr></table>

Table 5  
Results with k = 1

<table><tr><td></td><td>A</td><td>B</td><td>C</td><td>D</td></tr><tr><td>1</td><td>100</td><td>200</td><td>0</td><td>0</td></tr><tr><td>2</td><td>100</td><td>100</td><td>100</td><td>0</td></tr><tr><td>3</td><td>100</td><td>0</td><td>200</td><td>0</td></tr><tr><td>4</td><td>0</td><td>0</td><td>0</td><td>300</td></tr></table>

Table 7 Member rankings

Table 8 Concordance matrix

Many tests were performed for analyzing robustness. Choosing arbitrary numbers for $\rho$ in the interval $[ 0 . 1 , 0 . 2 4 ]$ , g in [0.3, 0.4], $I _ { 2 }$ in [0.3, 0.45], with $I _ { 1 } = 0 . 5 ,$ , we always obtained the fuzzy preference relation given by Table 3. If $I _ { 1 }$ increases, the veto effect included in $\sigma _ { g } ( A , C )$ is degraded. Fixed $I _ { 1 } = 0 . 6$ and choosing again arbitrary values of $\rho$ in the interval [0.1, 0.24], g in [0.3, 0.4], $I _ { 2 }$ in [0.3, 0.5], we systematically obtained the fuzzy group preference relation shown in Table 6. Finally, applying the EA of Section 4 with $\lambda { = } 0 . 6 .$ , we arrived to the same results pointed out in Table 4. No premature convergence was observed. From these results, we obtain $( A \sim B ) { > } C { > } D$ (the Borda ranking). As a consequence of reducing the veto effect, we achieve an improvement of the credibility of the Borda ranking. However, with $\lambda = 1$ , we obtained the same results from Table 5, deriving an ordering $B { > } A { > } C { > } D$

## 5.2. Example 2

The member rankings $R _ { i }$ are shown in Table 7.

In this case, A is the Condorcet winner. Additionally, the Borda count (sharing points when ties) suggests the ordering $A { > } B { > } ( C \sim D )$ . The strong opposition against A shown in $R _ { 4 }$ is compensated by the remaining members. However, B is a well-ranked alternative for all members and therefore one could ask if to rank B in the first position would not be a good compromise.

Calculating the concordance matrix according to Eq. (1), we obtain the results pointed out in Table 8.

Here, the unique relevant veto situation happens between A and B. The fourth member $( R _ { 4 } )$ belongs to veto coalition. Again, we have $n _ { \nu } { = } 1 / 4 N , ~ n _ { c } { = } 3 / 4 N$ and choosing $\rho { = } 0 . 1$ , g = 1/3, $I _ { \nu } { = } 0 . 5$ , then from expressions (2) and (3) $\varphi ( A , B ) = 0 . 5 .$ . Combining it with the concordance matrix and expression (4), the fuzzy group preference relation is obtained and shown in Table 9.

Table 6  
Fuzzy group preference relation with $I _ { 1 } = 0 . 6$

<table><tr><td></td><td>A</td><td>B</td><td>C</td><td>D</td></tr><tr><td>A</td><td>-</td><td>0.5</td><td>0.6</td><td>1</td></tr><tr><td>B</td><td>0.5</td><td>-</td><td>1</td><td>1</td></tr><tr><td>C</td><td>0</td><td>0</td><td>-</td><td>1</td></tr><tr><td>D</td><td>0</td><td>0</td><td>0</td><td>-</td></tr></table>

<table><tr><td> $R_1$ </td><td> $R_2$ </td><td> $R_3$ </td><td> $R_4$ </td></tr><tr><td>A</td><td>A</td><td>A</td><td>B</td></tr><tr><td>B, C</td><td>B, D</td><td>B</td><td>D</td></tr><tr><td>-</td><td>-</td><td>C</td><td>C</td></tr><tr><td>D</td><td>C</td><td>D</td><td>A</td></tr></table>

<table><tr><td></td><td>A</td><td>B</td><td>C</td><td>D</td></tr><tr><td>A</td><td>-</td><td>1</td><td>1</td><td>1</td></tr><tr><td>B</td><td>0</td><td>-</td><td>1</td><td>1</td></tr><tr><td>C</td><td>0</td><td>0</td><td>-</td><td>0.5</td></tr><tr><td>D</td><td>0</td><td>0</td><td>0.5</td><td>-</td></tr></table>

Using the exploitation method described in Section 4 with $\lambda { = } 0 . 5$ , the number of times that an alternative is found at a certain place in the ranking is given in Table 10 with respect to 100 variations of the seed parameter. The run time was $2 9 \mathrm { ~ s ~ } ( \mathrm { f o r ~ } 1 0 0 \mathrm { ~ t r i a l s } )$ . No premature convergence was observed.

Table 9  
The fuzzy group preference relation

<table><tr><td></td><td>A</td><td>B</td><td>C</td><td>D</td></tr><tr><td>A</td><td>-</td><td>0.5</td><td>1</td><td>1</td></tr><tr><td>B</td><td>0</td><td>-</td><td>1</td><td>1</td></tr><tr><td>C</td><td>0</td><td>0</td><td>-</td><td>0.5</td></tr><tr><td>D</td><td>0</td><td>0</td><td>0.5</td><td>-</td></tr></table>

Table 10  
Results with different trials

<table><tr><td></td><td>A</td><td>B</td><td>C</td><td>D</td></tr><tr><td>1</td><td>200</td><td>0</td><td>0</td><td>0</td></tr><tr><td>2</td><td>0</td><td>200</td><td>0</td><td>0</td></tr><tr><td>3</td><td>0</td><td>0</td><td>100</td><td>100</td></tr><tr><td>4</td><td>0</td><td>0</td><td>100</td><td>100</td></tr></table>

Table 11  
Results with k = 1

<table><tr><td></td><td>A</td><td>B</td><td>C</td><td>D</td></tr><tr><td>1</td><td>200</td><td>200</td><td>0</td><td>0</td></tr><tr><td>2</td><td>200</td><td>200</td><td>0</td><td>0</td></tr><tr><td>3</td><td>0</td><td>0</td><td>200</td><td>200</td></tr><tr><td>4</td><td>0</td><td>0</td><td>200</td><td>200</td></tr></table>

These results suggest the same ranking as Borda method did. But, however, if we increase the credibility level choosing $\lambda = 1$ , we obtain different results shown in Table 11.

These new results suggest an ordering $( B \sim A ) ^ { \triangleright }$ $( C \sim D )$ , which seems closer than the previous one to a group consensus.

Analyzing robustness, we chose arbitrary numbers for q in the interval [0.1, 0.24], g in [0.3, 0.4], $I _ { 2 }$ in [0.3, 0.45]. With $I _ { 1 } = 0 . 5 ,$ , we obtained the fuzzy preference relation given by Table 9 for every $( \rho ,$ $\eta , I _ { 2 } )$ . In this example, when $I _ { 1 }$ increases, the veto effect included in $\sigma _ { g } ( A , B )$ is degraded. Fixed $I _ { 1 } = 0 . 6 ,$ we obtained for every $( \rho , \eta , I _ { 2 } )$ the fuzzy preference relation pointed out in Table 12. Using the EA of Section 4 with $\lambda { = } 0 . 6 ,$ we arrived to the same results shown in Table 10 and the same ranking as Borda method did. With k = 1, we obtained again the performance exhibited in Table 11, which does not lead to Borda prescription. The same conclusion, again: as a consequence of reducing the veto effect, we achieve an improvement of the credibility of the Borda ranking. In the extreme limit, when the veto effect becomes very weak, the credibility of Borda ranking approaches 1.

## 5.3. Example 3

The following example was adapted from Ref. [2]. Suppose an election with 101,000 voters, which express their preferences on a set $\{ a , b , c , d , e , f , g $ h, y}. Let us suppose that

Table 12  
Fuzzy group preference relation with $I _ { 1 } = 0 . 6$

<table><tr><td></td><td>A</td><td>B</td><td>C</td><td>D</td></tr><tr><td>A</td><td>-</td><td>0.6</td><td>1</td><td>1</td></tr><tr><td>B</td><td>0</td><td>-</td><td>1</td><td>1</td></tr><tr><td>C</td><td>0</td><td>0</td><td>-</td><td>0.5</td></tr><tr><td>D</td><td>0</td><td>0</td><td>0.5</td><td>-</td></tr></table>

<table><tr><td>19,000 voters ranked</td><td>yOaObOcOdOeOfOgOh</td></tr><tr><td>21,000 voters ranked</td><td>eOfOgOhOyOaObOcOd</td></tr><tr><td>10,000 voters ranked</td><td>eOhOyOaObOcOdOfOg</td></tr><tr><td>10,000 voters ranked</td><td>fOhOyOaObOcOdOeOg</td></tr><tr><td>10,000 voters ranked</td><td>gOhOyOaObOcOdOeOf</td></tr><tr><td>31,000 voters ranked</td><td>yOaObOcOdOhOeOfOg</td></tr></table>

O means ‘‘ranked higher than’’.

Alternative h is the Condorcet winner because it wins against every other alternative with a majority of 51,000 votes. However, note that 50,000 voters consider y as the best alternative while no one accepts h at the first position. So, it seems that alternative y should be ranked higher than h in group final ordering. In fact, the Borda count suggests to elect y as the best group option. Note that no veto conditions hold on $\sigma _ { g } ( y , \mathfrak { X } ) \ \forall \ ^ { * } \in A$

Table 13  
Concordance matrix of example 3

<table><tr><td></td><td>h</td><td>y</td><td>a</td><td>b</td><td>c</td><td>d</td><td>e</td><td>f</td><td>g</td></tr><tr><td>h</td><td>-</td><td>0.515</td><td>0.515</td><td>0.515</td><td>0.515</td><td>0.515</td><td>0.515</td><td>0.515</td><td>0.515</td></tr><tr><td>y</td><td>0.485</td><td>-</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td></tr><tr><td>a</td><td>0.485</td><td>0</td><td>-</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td></tr><tr><td>b</td><td>0.485</td><td>0</td><td>0</td><td>-</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td></tr><tr><td>c</td><td>0.485</td><td>0</td><td>0</td><td>0</td><td>-</td><td>1</td><td>1</td><td>1</td><td>1</td></tr><tr><td>d</td><td>0.485</td><td>0</td><td>0</td><td>0</td><td>0</td><td>-</td><td>1</td><td>1</td><td>1</td></tr><tr><td>e</td><td>0.485</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>-</td><td>1</td><td>1</td></tr><tr><td>f</td><td>0.485</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>-</td><td>1</td></tr><tr><td>g</td><td>0.485</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td></tr></table>

Table 14  
Cardinal and weakness of veto coalition

<table><tr><td>Pair</td><td> $n_v$ </td><td> $\varphi$ </td></tr><tr><td>(d,e)</td><td>21,000</td><td>0.640</td></tr><tr><td>(d,f)</td><td>21,000</td><td>0.640</td></tr><tr><td>(e,f)</td><td>10,000</td><td>1</td></tr><tr><td>(e,g)</td><td>10,000</td><td>1</td></tr><tr><td>(f,g)</td><td>10,000</td><td>1</td></tr><tr><td>(h,y)</td><td>19,000</td><td>0.608</td></tr><tr><td>(h,a)</td><td>19,000</td><td>0.608</td></tr><tr><td>(c,e)</td><td>21,000</td><td>0.640</td></tr><tr><td>(c,f)</td><td>21,000</td><td>0.640</td></tr><tr><td>(e,h)</td><td>20,000</td><td>0.564</td></tr><tr><td>(f,h)</td><td>20,000</td><td>0.564</td></tr><tr><td>(g,h)</td><td>20,000</td><td>0.564</td></tr></table>

Table 15  
Fuzzy group preference relation of example 3

<table><tr><td></td><td>h</td><td>y</td><td>a</td><td>b</td><td>c</td><td>d</td><td>e</td><td>f</td><td>g</td></tr><tr><td>h</td><td>-</td><td>0.313</td><td>0.313</td><td>0.515</td><td>0.515</td><td>0.515</td><td>0.515</td><td>0.515</td><td>0.515</td></tr><tr><td>y</td><td>0.485</td><td>-</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td></tr><tr><td>a</td><td>0.485</td><td>0</td><td>-</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td></tr><tr><td>b</td><td>0.485</td><td>0</td><td>0</td><td>-</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td></tr><tr><td>c</td><td>0.485</td><td>0</td><td>0</td><td>0</td><td>-</td><td>1</td><td>0.640</td><td>0.640</td><td>1</td></tr><tr><td>d</td><td>0.485</td><td>0</td><td>0</td><td>0</td><td>0</td><td>-</td><td>0.640</td><td>0.640</td><td>1</td></tr><tr><td>e</td><td>0.274</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>-</td><td>1</td><td>1</td></tr><tr><td>f</td><td>0.274</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>-</td><td>1</td></tr><tr><td>g</td><td>0.274</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>-</td></tr></table>

Let us solve this example using our proposal with $\rho = 0 . 1 , \eta = 1 / 3$ . The concordance matrix is shown in Table 13.

Table 14 pointed out the pairs in which the veto coalition is not empty and the concordance index is different from zero. In this calculation, we used $I _ { \nu } = 1 /$ 3 when $n _ { c } { < } 2 / 3 N .$

Table 16  
Results of 100 trials with $\lambda = 1$

<table><tr><td></td><td>h</td><td>y</td><td>a</td><td>b</td><td>c</td><td>d</td><td>e</td><td>f</td><td>g</td></tr><tr><td>1</td><td>93</td><td>381</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>2</td><td>85</td><td>93</td><td>300</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>3</td><td>65</td><td>0</td><td>178</td><td>235</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>4</td><td>69</td><td>0</td><td>0</td><td>243</td><td>90</td><td>0</td><td>76</td><td>0</td><td>0</td></tr><tr><td>5</td><td>53</td><td>0</td><td>0</td><td>0</td><td>197</td><td>22</td><td>190</td><td>16</td><td>0</td></tr><tr><td>6</td><td>44</td><td>0</td><td>0</td><td>0</td><td>130</td><td>63</td><td>156</td><td>85</td><td>0</td></tr><tr><td>7</td><td>30</td><td>0</td><td>0</td><td>0</td><td>61</td><td>160</td><td>56</td><td>171</td><td>0</td></tr><tr><td>8</td><td>30</td><td>0</td><td>0</td><td>0</td><td>0</td><td>233</td><td>0</td><td>206</td><td>9</td></tr><tr><td>9</td><td>9</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>469</td></tr></table>

Table 17  
Results of 100 trials with $\lambda { = } 0 . 6 4$

<table><tr><td></td><td>h</td><td>y</td><td>a</td><td>b</td><td>c</td><td>d</td><td>e</td><td>f</td><td>g</td></tr><tr><td>1</td><td>35</td><td>145</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>2</td><td>31</td><td>35</td><td>114</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>3</td><td>28</td><td>0</td><td>66</td><td>86</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>4</td><td>22</td><td>0</td><td>0</td><td>94</td><td>64</td><td>0</td><td></td><td>0</td><td>0</td></tr><tr><td>5</td><td>21</td><td>0</td><td>0</td><td>0</td><td>116</td><td>43</td><td>0</td><td>0</td><td>0</td></tr><tr><td>6</td><td>13</td><td>0</td><td>0</td><td>0</td><td>0</td><td>137</td><td>30</td><td>0</td><td>0</td></tr><tr><td>7</td><td>13</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>150</td><td>17</td><td>0</td></tr><tr><td>8</td><td>13</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>163</td><td>4</td></tr><tr><td>9</td><td>4</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>176</td></tr></table>

Table 18 Borda count

<table><tr><td>Alternative</td><td>Points</td></tr><tr><td>y</td><td>765,000</td></tr><tr><td>a</td><td>664,000</td></tr><tr><td>b</td><td>563,000</td></tr><tr><td>h</td><td>509,000</td></tr><tr><td>e</td><td>488,000</td></tr><tr><td>c</td><td>462,000</td></tr><tr><td>f</td><td>407,000</td></tr><tr><td>d</td><td>361,000</td></tr><tr><td>g</td><td>326,000</td></tr></table>

Combining the concordance information with $\varphi$ according to expression (4), we have the fuzzy group preference relation shown in Table 15.

Note that the degree of truth of the proposition $h S _ { G } { ^ * }$ is low $\forall \ { } ^ { * } \in { \cal A }$ . Alternative y is clearly the best in a group consensus.

With $\lambda = 1 , ~ n _ { I } = 1 2$ , the number of times that an alternative is found at a certain place in the ranking is given in Table 16 with respect to 100 variations of the seed parameter. The run time was 61 s (for 100 trials). No premature convergence was observed.

Table 16 suggests a final ranking $y { > } a { > } b { > }$ $h { > } ( c \sim e ) { > } ( d \sim f ) { > } g$ . This solution is robust with respect to changes of U in the interval [0.1, 0.24], g in $[ 0 . 3 , 0 . 4 ] , I _ { 2 }$ in [0.25, 0.40] and $I _ { 1 }$ in [0.45, 0.6].

With $\lambda { = } 0 . 6 4$ , we obtain results of Table 17. According to these results, the group consensus ranking seems to be $y > a > b > h > c > d > e > f > g .$

The Borda count is pointed out in Table 18. We can see that the ranking suggested is rather similar to our proposal with $\lambda = 1$

## 6. Conclusions

A crucial point of our proposal is to model group preferences with fuzzy binary relations, avoiding paradoxes related to the ill-defined concept of collective preferences. This proposal is a natural extension of concepts of concordance and discordance (basic ideas of ELECTRE methodology for multicriteria decision-making problems) to group ranking problems, using multiobjective optimization and an evolutionary algorithm with very good properties for exploiting the fuzzy group outranking relation.

The proposed method does not have structural properties which limit its application. The number of group members is not limited. The number of alternatives can cover most complex situations of real group decision-making.

The designed agent performed very well in some examples in the sense of quality of solutions as well as in the sense of computational effort. Results showed a very acceptable robustness respect to changes of imprecise model parameters. Our proposal performs better than classical paradigms for solving group ranking problems in a few test examples, probably because a compensatory scheme or a majority rule are not always well suited for group decision-making, where veto effects are often very important. This agent model works with the natural heuristic used by collaborative groups for making reasonable or consensus agreements, based on universally accepted majority rules combined with the necessary observance of important minorities, principles of fairness and equity.

## Acknowledgements

This research is supported by the Mexican National Board of Science and Technology (CONACYT).

## References

[1] K.J. Arrow, Social Choice and Individual Values, Wiley, New York, 1963.

[2] D. Bouyssou, Th. Marchant, P. Perny, A. Tsoukias, Ph. Vincke, Evaluations and Decision Models: A Critical Perspective, Kluwer Academic Publishing, Dordrecht, 2000.

[3] J.P. Brans, Ph. Vincke, A preference ranking organization meth od, Management Science 31 (1985) 647 – 656.

[4] S. Cook, L. Seiford, On the Borda-Kendall Consensus method for priority ranking, Management Science 28 (1982) 621 – 637.

[5] D. Cvetkovic, I.C. Parmee, Preferences and their application in evolutionary multiobjective optimisation, IEEE Transactions on Evolutionary Computation 6 (2002) 42– 57.

[6] D.M. Farrell, Comparing Electoral Systems, Contemporary Political Studies, Prentice Hall, New York, 1997.

[7] E. Fernandez, J.C. Leyva, A method based on multiobjective optimization for deriving a ranking from a fuzzy preference relation, European Journal of Operational Research 154 (2004) 110– 124.

[8] E. Fernandez, R. Olmedo, An improved method for deriving final ranking from a fuzzy preference relation via multiobjective optimization, Foundations of Computing and Decision Sciences 28 (3) (2003).

[9] P.C. Fishburn, Condorcet social choice function, SIAM Journal of Applied Mathematics 33 (1977) 469– 489.

[10] J. Fodor, M. Roubens, Fuzzy Preference Modeling and Multicriteria Decision Support, Kluwer, Dordrecht, 1994.

[11] S. French, Decision Theory: an Introduction to the Mathematics of Rationality, Ellis Horwood, London, 1993.

[12] R. Fuller, Ch. Carlsson, Fuzzy multiple criteria decision making: recent developments, Fuzzy Sets and Systems 78 (1996) 139–153.

[13] F. Herrera, E. Herrera-Viedma, J.L. Verdegay, A model of consensus in group decision making under linguistic assessments, Fuzzy Sets and Systems 78 (1996) 73– 87.

[14] F. Herrera, E. Herrera-Viedma, J.L. Verdegay, Choice processes for nonhomogeneous group decision making in linguistic settings, Fuzzy Sets and Systems 94 (1997) 287 – 308.

[15] F. Herrera, M. Lozano, Adaptation of genetic algorithm parameters based on fuzzy logic controllers, in: F. Herrera, J.L. Verdegay (Eds.), Genetic Algorithms and Soft Computing, Physica-Verlag, Heidelberg, 1996, pp. 95–125.

[16] C.L. Hwang, M.J. Lin, Group decision making under multiple criteria, Lecture Notes in Economics and Mathematical Systems, vol. 281, Springer Verlag, Berlin, 1987.

[17] T. Jelassi, G. Kersten, S. Ziont, An introduction to group decision and negotiation support, in: C.A. Bana e Costa (Ed.), Readings in Multiple Criteria Decision Aid, Springer Verlag, Berlin, 1990, pp. 537 – 568.

[18] R.L. Keeney, H. Raiffa, Decision with Multiple Objectives: Preferences and Value Tradeoffs, Wiley, New York, 1976.

[19] J.C. Leyva, E. Fernandez, A genetic algorithm for deriving final ranking from a fuzzy outranking relation, Foundations of Computing and Decision Sciences 24 (1999) 33–47.

[20] J.C. Leyva, E. Fernandez, A new method for group decision support based on ELECTRE III methodology, European Journal of Operational Research 148 (2003) 14– 27.

[21] F.A. Lootsma, R. Ramanathan, H. Schuijt, Fairness and equity via concepts of multicriteria decision analysis, in: T.J. Stewart, R.C. Van den Honert (Eds.), Trends in Multicriteria Decision Making, Lecture Notes in Economics and Mathematical Systems, vol. 465, Springer Verlag, Berlin-Heidelberg, 1998, pp. 215– 226.

[22] C. Macharis, J.P. Brans, B. Mareschal, The GDSS Promethee Procedure, Journal of Decision Systems 7-SI (1998) 283 – 307.

[23] T. Marchant, Ranking with Scoring Functions, Technical Report IS-MG 97/05, Institut de Statistique et de Recherche Ope´rationnelle, Universite Libre de Bruxelles, Serie Mathematiques de la Gestion (1995).

[24] H. Nurmi, Comparing Voting Systems, D. Reidel, Dordrecht, 1987.

[25] A. Ostanello, Outranking methods, in: B. Fandel, G. Spronk, J. Matarazzo (Eds.), International Summer School on Multiple Criteria Decision Making Methods, Aplications and Software volume 1, Springer-Verlag, Acireale, Italy, 1983, pp. 41 – 60.

[26] P.W. Poon, J.N. Carter, Genetic algorithm crossover operators for ordering applications, Computers and Operations Research 22 (1) (1995) 135– 147.

[27] B. Roy, The outranking approach and the foundations of ELECTRE methods, in: C.A. Bana e Costa (Ed.), Reading

in Multiple Criteria Decision Aid, Springer-Verlag, Berlin, 1990, pp. 155 – 183.

[28] B. Roy, Multicriteria Methodology for Decision Aiding, Kluwer Academic Publishing, Dordrecht, 1996.

[29] S. Russell, P. Norvig, Artificial Intelligence, A Modern Approach, Prentice Hall, New York, 1995.

[30] F. Turnovec, Monotonicity of power indices, in: T.J Stewart, R.C. Van den Honert (Eds.), Trends in Multicriteria Decision Making, Lecture Notes in Economics and Mathematical Systems, vol. 465, Springer Verlag, Berlin, 1998, pp. 199–214.

![](/api/attachments/UNMFFMY7/fulltext/images/5447544b1b7bebd8c07d0b7e5e9aca502593040125f88648818839ddd10b8c1b.jpg)  
Eduardo Fernandez was born in Cuba, 1951. He received the BSc degree in Physics from the University of Havana in 1973 and the PhD degree in Computer Aided Design of Electronic Circuits, from Poznan University of Technology, 1987. He is currently Senior Professor in the School of Computer Science, Autonomous University of Sinaloa (UAS), Mexico. His main areas of interest are mathematical decision models and intelligent decision support systems.

![](/api/attachments/UNMFFMY7/fulltext/images/608368c8ef6a6b5a541c6b114386fc6cb724cae376a3ca3e936e6844e1e158e8.jpg)

Rafael Olmedo was born in Mexico City, 1956. He obtained the BSc degree in Mathematics from Autonomous National University of Mexico in 1982 and MSc degree in Computer Science from Autonomous University of Sinaloa (UAS), 2000. He is currently Associate Professor in the Faculty of Physical and Mathematical Sciences, UAS. His areas of interest are group decision support systems and evolutionary algorithms.
