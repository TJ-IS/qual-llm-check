---
otero_id: 9604
otero_key: "4AVZW5J8"
title: "Stochastic ordinal regression for multiple criteria sorting problems"
authors: "Miłosz Kadziński; Tommi Tervonen"
year: "2013"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2012.12.030"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Stochastic ordinal regression for multiple criteria sorting problems

Miłosz Kadziński <sup>a,</sup>⁎, Tommi Tervonen b

<sup>a</sup> Institute of Computing Science, Poznań University of Technology, Poland

<sup>b</sup> Econometric Institute, Erasmus University Rotterdam, The Netherlands

## a r t i c l e i n f o

Article history: Received 26 October 2011 Received in revised form 24 December 2012 Accepted 27 December 2012 Available online 4 January 2013

Keywords: Decision analysis Multiple criteria sorting Stochastic multicriteria acceptability analysis Robust ordinal regression Multi-attribute value theory

## a b s t r a c t

We present a new approach for multiple criteria sorting problems. We consider sorting procedures applying general additive value functions compatible with the given assignment examples. For the decision alternatives, we provide four types of results: (1) necessary and possible assignments from Robust Ordinal Regression (ROR), (2) class acceptability indices from a suitably adapted Stochastic Multicriteria Acceptability Analysis (SMAA) model, (3) necessary and possible assignment-based preference relations, and (4) assignment-based pair-wise outranking indices. We show how the results provided by ROR and SMAA complement each other and combine them under a uni<sup>fi</sup>ed decision aiding framework. Application of the approach is demonstrated by classifying 27 countries in 4 democracy regimes.

© 2013 Elsevier B.V. All rights reserved.

## 1. Introduction

In the multiple criteria sorting problem (also called ordinal classi<sup>fi</sup>cation), a Decision Maker (DM) needs to assign decision alternatives to pre-de<sup>fi</sup>ned ordered classes [25]. For example, creditors may wish to assign customers to classes with respect to their reliability to repay debts [15], and banks can be sorted in different groups based on their overall viability, performance and risk exposure [3]. The assignments depend on the preference information elicited from the DM. The preference information may either directly specify values for the preference parameters, such as criteria weights, marginal value functions, and pro<sup>fi</sup>les or thresholds delimiting the classes, or specify the values indirectly through assignment examples (e.g. alternative a belongs to class C ) used to infer the actual parameters. Some multiple criteria sorting procedures require a large set of preference parameters, and therefore indirect preference information may be easier for the DM to provide and to understand [1].

Various elicitation techniques for admitting indirect preference information have been proposed. Refs. [16–18] introduced techniques for deriving parameters for the pseudo-criterion based ELECTRE TRI models. For sorting based on value functions, Ref. [24] proposed a technique for inferring the thresholds separating the classes. Although all these approaches avoid direct elicitation of the preference information, they deliver different values for the preference parameters due to selecting a set of parameters that is “central”, “mean”, “most discriminant”, or “representative”, and interpreted differently in each technique.

Another methodology, termed Robust Ordinal Regression (ROR) [5,7], takes into account all instances of the preference model compatible with the assignment examples. Ref. [2] proposes to compute, for each alternative, the best and the worst classes compatible with the constraints on parameter values of an ELECTRE TRI model provided directly by the DM or inferred from the assignment examples. Refs. [6,14] extend the value-function based UTADIS method by taking into account the whole set of compatible additive value functions and computing a range of possible classes for each alternative. Ref. [14] considers piecewise linear marginal value functions as in the original UTADIS, whereas Ref. [6] employs general monotone value functions and additionally computes assignments necessarily implied by the set of compatible value functions.

A different way of handling imprecise preference information in multiple criteria sorting problems was proposed in SMAA-TRI [22], that applies Stochastic Multicriteria Acceptability Analysis (SMAA) [20] to ELECTRE TRI. SMAA-TRI allows ELECTRE TRI to be used with uncertain, arbitrarily distributed values for weights, cutting level, and the pro<sup>fi</sup>les separating the classes. The method applies Monte Carlo simulation to estimate class acceptability indices that represent the share of compatible instances of the preference model assigning each alternative to a particular class. These indices quantify the amount of instability in the assignments induced by the imprecise parameter values.

All the methods discussed above fail to consider some important issues. On the one hand, ROR methods focus on identifying the possible and necessary assignments for each alternative and provide recommendations such as “depending on the chosen compatible instance of the preference model, the alternative is assigned to class medium or good or best” and “irrespective of the compatible model instance, the alternative is assigned to class bad”. However, our experiences (see e.g. [8,9,12]) indicate that the range of possible assignment can be rather wide, whereas the set of necessary assignments is often empty. From this perspective, it is useful to answer how probable it is for an alternative to be assigned to each class. Knowing the most and the least probable classes or the probability of being assigned to the best or worst classes may be valuable for practical decision support. In particular, a low probability of an assignment indicates it to be sensitive for small changes of DM preferences. Thus, ROR may be enriched with SMAA by answering how probable are the possible assignments.

The SMAA-TRI class acceptability indices can tractably be estimated to a reasonable accuracy [21]. For example, if we want to achieve an error limit of 0.01, it can be accomplished with 95% con<sup>fi</sup>dence by performing approximately $1 0 ^ { 4 }$ Monte Carlo iterations. However, the class acceptability indices estimated through simulation are not exact. Consequently, an estimated class acceptability of 0 does not exclude the possibility of the alternative being assigned to the given class. Although the conditions under which such an assignment is possible may be very speci<sup>fi</sup>c, they are still consistent with the preference information provided by the DM. Thus, it is desirable to analyze estimation of class acceptability indices of SMAA in the context of the necessary and possible assignments of ROR to provide information on which assignments occur with all, some, or no compatible preference models. Furthermore, although the SMAA modeling framework is applicable to any preference model, the sole SMAA method for multiple criteria sorting problems is SMAA-TRI that extends ELECTRE TRI. Since it applies a pseudocriterion based preference model, it requires the DM to understand the concepts of concordance and discordance as well as the employed exploitation procedure. Moreover, SMAA-TRI requires preference information in the form of density functions for the class pro<sup>fi</sup>les, cutting level, and weights, and their elicitation may be too demanding for the DM.

To address these problems, in this paper we combine ROR and SMAA in a joint approach for multiple criteria sorting problems. We focus on sorting problems applying value functions and adapt SMAA-TRI to apply general monotone value functions as the preference model. We consider both threshold- and example-based sorting procedures that use assignment examples on a subset of reference alternatives as indirect preference information. We show how the outcomes provided by the two approaches complement each other and extend the basic analysis with assignment-based preference relations that allow comparing pairs of alternatives. These may be useful when the DM is interested in the recommendation obtained for some particular alternatives, or when there are a number of alternatives possibly assigned to the same range of classes. Discriminating them with the assignment-based relations provides results such as “irrespective of the compatible model instance, the class of alternative a is never worse than the class of $b "$ or “there is at least one compatible model instance that assigns a to a class at least as good as b”. Note that the purpose of the assignment-based preference relation is not to rank the alternatives, but merely to enable their pair-wise comparisons in a manner compatible with the sorting method.

The organization of this paper is the following. Section 2 introduces the notation and the basic principles of value function based sorting procedures. In Section 3 we present the new approach for multiple criteria sorting problems and discuss extensions of the main proposal. Section 4 demonstrates use of the approach by analyzing an example. The last section concludes.

## 2. Concepts and notation

We use the following notation:

$A = \{ a _ { 1 } , . . . , a _ { i } , . . . , a _ { n } \} - a$ <sup>fi</sup>nite set of n alternatives;

$A ^ { R } = \{ a ^ { * } , b ^ { * } , \ldots \} - a$ <sup>fi</sup>nite set of reference alternatives on which the DM accepts to express preferences. Usually $A ^ { R } \subseteq A ;$

$G = \{ g _ { 1 } , . . . , g _ { j } , . . . , g _ { m } \} - \mathtt { a }$ <sup>fi</sup>nite set of m evaluation criteria, g<sub>j</sub>: $A \cup A ^ { R }  \mathbb { R } ;$

$X _ { j } = \{ g _ { i } ( a _ { i } ) , ~ a _ { i } \in A \} ~ -$ the set of evaluations on g . We assume, without loss of generality, that the greater $g _ { j } ( a _ { i } )$ , the better is alternative $a _ { i }$ on criterion g ;

$x _ { i } ^ { 1 } , . . . , x _ { i } ^ { n _ { j } ( A ) } -$ the ordered values of $X _ { j } , x _ { j } ^ { k } { < } x _ { j } ^ { k + 1 } , k { = } 1 , . . . , n _ { j } ( A ) - 1$ where ${ } n _ { j } ( A ) = | X _ { j } |$ and $n _ { j } ( A ) \leq n ;$ consequently, $\begin{array} { r } { X = \prod _ { j = 1 } ^ { m } \dot { X _ { j } } } \end{array}$ is the evaluation space;

$C _ { 1 } , . . . , C _ { p } - p$ prede<sup>fi</sup>ned classes ordered so that $C _ { h + 1 }$ is preferred to $C _ { h } , h { = } 1 , . . . , p { - } 1$

We assume that the DM provides a set of assignment examples consisting of a reference alternative $a ^ { * } \in A ^ { R }$ and its desired assignment [6]:

$$
a ^ {*} \rightarrow \left[ C _ {L _ {D M} (a ^ {*})}, C _ {R _ {D M} (a ^ {*})} \right],
$$

where $\underline { { \mathbf { \Pi } } } _ { \bullet } \left[ C _ { L _ { D M } ( a ^ { * } ) , } C _ { R _ { D M } ( a ^ { * } ) } \right]$ is an interval of contiguous classes $C _ { L _ { D M } ( a ^ { * } ) } , C _ { L _ { D M } ( a ^ { * } ) + 1 } ^ { \mathrm { ~ L ~ } ^ { \ -- } } , . . . , \widetilde { C } _ { R _ { D M } ( a ^ { * } ) } .$ An assignment example is said to be precise if $L _ { D M } ( a ^ { * } ) = R _ { D M } ( a ^ { * } )$ ) and imprecise otherwise. To assign alternatives to the classes we consider two procedures applying additive value functions of the form:

$$
U (a) = \sum_ {j = 1} ^ {m} u _ {j} (a),\tag{1}
$$

where the marginal value functions $u _ { j }$ are de<sup>fi</sup>ned by $u _ { j } ( x _ { j } ^ { k } ) , k = 1 , \ldots ,$ $n _ { j } ( A )$ ; these functions are expected to be monotonically non-decreasing and normalized so that the overall value (1) is bound within interval [0,1]. Table 1 summarizes the notation used throughout the paper.

## 2.1. Threshold-based sorting procedure

In the threshold-based sorting procedure, the limits between consecutive classes $C _ { h } , h = 1 , . . . , p ,$ , are de<sup>fi</sup>ned by a vector of thresholds $\mathbf { t } { = } \{ t _ { 1 } , . . . , t _ { p - 1 } \}$ such that $0 { < } t _ { 1 } { < } . . . { < } t _ { p - 1 } { < } 1$ , and $t _ { h - 1 }$ and $t _ { h }$ are, respectively, the lower and upper threshold of class $C _ { h } , h { = } 2 , . . . , p { - } 1$ Note that $t _ { 1 }$ is an upper threshold of class $C _ { 1 }$ while the lower threshold is $0 ,$ and $t _ { p - 1 }$ is a lower threshold of class $C _ { p }$ while the upper threshold $\mathrm { i } s > 1$

We represent the DM preferences with a pair (U, t), where U is an additive value function and t is a vector of thresholds delimiting the classes. The set of pairs $( \mathcal { U } , \mathfrak { t } ) ^ { R }$ compatible with the provided assign-<sup>U</sup>ment examples is de<sup>fi</sup>ned with the following constraints:

$$
\left. \begin{array}{l} U (a) = \sum_ {j = 1} ^ {m} u _ {j} (a), \forall a \in A, \\ U (a ^ {*}) \geq t _ {L _ {D M} (a ^ {*}) - 1}, \quad U (a ^ {*}) + \varepsilon \leq t _ {R _ {D M} (a ^ {*})}, \quad \forall a ^ {*} \in A ^ {R}, \\ t _ {1} \geq \varepsilon , t _ {p - 1} \leq 1 - \varepsilon , \\ t _ {h} - t _ {h - 1} \geq \varepsilon , h = 2, \dots , p - 1, \\ u _ {j} \Big (x _ {j} ^ {k} \Big) - u _ {j} \Big (x _ {j} ^ {(k - 1)} \Big) \geq 0, j \in J, k = 2, \dots , n _ {j} (A), \\ u _ {j} \Big (x _ {j} ^ {1} \Big) = 0, j \in J, \sum_ {j = 1} ^ {m} u _ {j} \Big (x _ {j} ^ {n _ {j} (A)} \Big) = 1, \end{array} \right\} E ^ {B A S E}\tag{2}
$$

where ε is an arbitrarily small positive value. Note that for clarity of presentation, the above formulation de<sup>fi</sup>nes the characteristic points of marginal value functions with the evaluations of all alternatives $( A )$ , although it is suf<sup>fi</sup>cient to consider only the reference alternatives $( A ^ { R } ) \left[ 6 \right]$

Table 1 Notation.

<table><tr><td>Notation</td><td>Meaning</td></tr><tr><td> $\mathcal{U}^{R}$ </td><td>Set of value functions  $U$  compatible with the DM preferences</td></tr><tr><td> $(\mathcal{U},\mathbf{t})^{R}$ </td><td>Set of pairs  $(U,\mathbf{t})$  compatible with the DM preferences</td></tr><tr><td> $\mathcal{U}^{SMAA}$ </td><td>Set of value functions  $U$  obtained in the SMAA simulation process</td></tr><tr><td> $(\mathcal{U},\mathbf{t})^{SMAA}$ </td><td>Set of pairs  $(U,\mathbf{t})$  obtained in the SMAA simulation process</td></tr><tr><td> $U^{REP}$ </td><td>Representative value function</td></tr><tr><td> $\left[C_{L^{(a)}(a)},C_{R^{(a)}}\right]$ </td><td>Assignment of  $a$  with a value function  $U$ </td></tr><tr><td> $C^{(U,\mathbf{t})}(a)$ </td><td>Assignment of  $a$  with pair  $(U,\mathbf{t})$ </td></tr><tr><td> $\left[C_{LDM(a*)},C_{RDM(a*)}\right]$ </td><td>Assignment provided by the DM for a reference alternative  $a^{*}\in A^{R}$ </td></tr><tr><td> $C^{REP}(a)$ </td><td>Assignment of  $a$  with a representative value function  $U^{REP}$ </td></tr><tr><td> $C_{P}(a)=[L_{P}(a),R_{P}(a)]$ </td><td>Possible assignment of  $a\in A$ </td></tr><tr><td> $C_{N}(a)=[L_{N}(a),R_{N}(a)]$ </td><td>Necessary assignment of  $a\in A$ </td></tr><tr><td> $a\rightarrow^{P}C_{h}$ </td><td>Possible assignment of alternative  $a\in A$  to class  $C_{h}$ , i.e.  $h\in C_{P}(a)$ </td></tr><tr><td> $a\rightarrow^{N}C_{h}$ </td><td>Necessary assignment of alternative  $a\in A$  to class  $C_{h}$ , i.e.  $h\in C_{N}(a)$ </td></tr><tr><td> $a\succeq^{N}b$ </td><td>Necessary preference relation for pair  $(a,b)\;a\in A\times A$ </td></tr><tr><td> $a\succeq^{P}b$ </td><td>Possible preference relation for pair  $(a,b)\in A\times A$ </td></tr><tr><td> $a\succeq\rightarrow^{,N}b$ </td><td>Necessary assignment-based preference relation for pair  $(a,b)\in A\times A$ </td></tr><tr><td> $a\succeq\rightarrow^{,P}b$ </td><td>Possible assignment-based preference relation for pair  $(a,b)\in A\times A$ </td></tr><tr><td>CAI $(a,h)$ </td><td>Class acceptability index for  $a\in A$  and class  $C_{h}$ </td></tr><tr><td>CAI $(a,[h_{L},h_{R}] )$ </td><td>Class acceptability index for  $a\in A$  and a range of classes  $[C_{h_{L}},C_{h_{R}}]$ </td></tr><tr><td>CuCAI $(a,h)$ </td><td>Cumulative class acceptability index for  $a\in A$  and class  $C_{h}$ </td></tr><tr><td>APOI $(a,b)$ </td><td>Assignment-based pair-wise outranking index for pair  $(a,b)\in A\times A$ </td></tr><tr><td>APWI $(a,b)$ </td><td>Assignment-based pair-wise winning index for pair  $(a,b)\in A\times A$ </td></tr><tr><td> $E^{BASE}$ </td><td>Monotonicity and normalization constraints for marginal value functions</td></tr><tr><td> $E^{TH}$ </td><td>Constraints defining the set of compatible pairs  $(U,\mathbf{t})^{R}$ </td></tr><tr><td> $E^{EX}$ </td><td>Constraints defining the set of compatible value functions  $\mathcal{U}^{R}$ </td></tr><tr><td> $E_{Y}^{X}(Z)$ </td><td>Set of constraints for computing  $Z$  for parameters  $Y$  and procedure  $X$ </td></tr><tr><td> $X\in\{TH,EX\}$ </td><td>Sorting procedures: THreshold-based, EXample-based</td></tr><tr><td> $Z\in\{a\rightarrow^{PC}_{h},\;a\rightarrow^{NC}_{h},\;a\succeq\rightarrow^{,P}b,\;a\succeq\rightarrow^{,Nb\}$ </td><td>Possible and necessary assignment of  $a$  to  $C_{h}$  Possible and necessary assignment-based preference relations for pair  $(a,b)$ </td></tr><tr><td> $E(a\rightarrow[C_{h_{L}},C_{h_{R}}])$ </td><td>Constraints assigning  $a\in A$  to the range of classes  $[C_{h_{L}},C_{h_{R}}]$  with the example-based sorting procedure</td></tr><tr><td> $A^{h}$ </td><td>Set of reference alternatives that are assigned by the DM to a class other than  $C_{h}$ </td></tr></table>

The threshold-based sorting model is completely de<sup>fi</sup>ned with $( U , \mathbf { t } ) \in ( \mathcal { U } , \mathbf { t } ) ^ { R }$ , and alternative a is assigned to class $C _ { h } \ ( a \to C _ { h } )$ iff $U ( a ) \in [ t _ { h - 1 } , t _ { h } [$ [. Let us denote by $C ^ { ( U , \mathbf { t } ) } \left( a \right)$ the class to which alternative a is assigned with this procedure parameterized with (U, t).

## 2.2. Example-based sorting procedure

In the example-based sorting procedure the classes are explicitly delimited by the assignment examples. The set of value functions $\mathcal { U } ^ { R }$ <sup>U</sup>compatible with the DM preferences is de<sup>fi</sup>ned with the following constraints:

$$
\left. \begin{array}{l} U (a) = \sum_ {j = 1} ^ {m} u _ {j} (a),   \forall a \in A, \\ U (a ^ {*}) \geq U (b ^ {*}) + \varepsilon , \quad \forall a ^ {*}, b ^ {*} \in A ^ {R}: L _ {D M} (a ^ {*}) > R _ {D M} (b ^ {*}), \\ E ^ {B A S E}, \end{array} \right\} E ^ {E X}\tag{3}
$$

where ε is an arbitrarily small positive value. Then, alternative a is assigned to an interval of classes $[ C _ { L ^ { U } ( a ) } , C _ { R ^ { U } ( a ) } ] ( a \mathrm {  } [ C _ { L ^ { U } ( a ) } , C _ { R ^ { U } ( a ) } ] )$ in the following way:

$$
L ^ {U} (a) = \operatorname{Max} \left\{\{1 \} \cup \left\{L _ {D M} \left(a ^ {*}\right): U \left(a ^ {*}\right) \leq U (a), a ^ {*} \in A ^ {R} \right\} \right\},
$$

$$
R ^ {U} (a) = \operatorname{Min} \left\{\{p \} \cup \left\{R _ {D M} \left(a ^ {*}\right): U \left(a ^ {*}\right) \geq U (a), a ^ {*} \in A ^ {R} \right\} \right\}.
$$

Note that if we consider only a single value function U and choose, for each $h = 1 , . . . , p - 1$ , a threshold $\overline { { t _ { h } ^ { U } } }$ from within the interval

$$
\left[ \operatorname{Max} _ {a ^ {*}: R _ {D M} (a ^ {*}) \leq h} \left\{U \left(a ^ {*}\right) \right\}, \operatorname{Min} _ {a ^ {*}: L _ {D M} (a ^ {*}) > h} \left\{U \left(a ^ {*}\right) \right\} \right]
$$

we obtain the threshold-based sorting procedure assigning each reference alternative $a ^ { * } \in A ^ { R }$ to a single class in $\left[ C _ { L _ { D M } ( a ^ { * } ) , } C _ { R _ { D M } ( a ^ { * } ) } \right]$ , and each non-reference alternative to a single class in $\left\lceil C _ { L ^ { U } ( a ) , } C _ { R ^ { U } ( a ) } \right\rceil$ (see Proposition 3.4 in Ref. [6]). That is, whereas the example-based procedure would assign a to a set of contiguous classes $\left[ C _ { L ^ { \mathrm { U } } ( a ) } , C _ { R ^ { U } ( a ) } \right]$ such that $R ^ { U } ( a )$ may be strictly greater than $L ^ { U } ( a )$ , the threshold-based procedure parameterized with the pair $( U , \mathbf { t } )$ assigns a precisely to a single class $\dot { C } ^ { ( U , t ) } ( a )$ , since $U ( a )$ is always within $[ t _ { h - 1 } , t _ { h } |$ [for an $h { \in } \{ 1 , . . . , p \}$ . Moreover, if the DM provides an imprecise assignment for a reference alternative $a ^ { * } \in A ^ { R }$ (e.g. $a ^ { * } {  } [ C _ { 2 } , \ C _ { 3 } ] )$ , this assignment cannot be reproduced with the threshold-based procedure using a single pair $( U , \mathbf { t } )$ . Instead, $a ^ { * }$ is assigned to the classes speci<sup>fi</sup>ed by the DM by different compatible pairs $( \breve { U } , \mathbf { t } ) \left( \mathbf { e . g . } a ^ { \ast } \right.$ is assigned to $C _ { 2 }$ by $( U ^ { 1 } , { \mathbf t } ^ { 1 } ) \dot { \in } ( \mathcal { U } , { \mathbf t } ) ^ { R }$ and to $C _ { 3 }$ by $( U ^ { \bar { 2 } } , \mathbf { t } ^ { 2 } ) \in ( \mathcal { U } , \mathbf { t } ) ^ { R }$ , but there is no pair $( U , \mathbf { t } ) \in ( \mathcal { U } , \mathbf { t } ) ^ { R }$ <sup>U</sup>that assigns $a ^ { * }$ <sup>U</sup>to the complete range $[ C _ { 2 } , C _ { 3 } ] ,$ ).

## 3. Stochastic ordinal regression for multiple criteria sorting problems

## 3.1. Possible and necessary assignments

Given a set $A ^ { R }$ of assignment examples and a corresponding set of compatible instances of the preference model (i.e. compatible pairs $( \mathcal { U } , \mathop { \bf t } ) ^ { R }$ for the threshold-based sorting procedure or compatible <sup>U</sup>value functions $\boldsymbol { \mathcal { U } } ^ { R }$ for the example-based sorting procedure), for each alternative $a \in A ,$ , the possible assignment $C _ { P } ( a )$ is de<sup>fi</sup>ned as the set of indices of classes $C _ { h }$ for which there exists at least one compatible preference model instance assigning a to $C _ { h } ,$ and the necessary assignment $C _ { N } ( a )$ as the set of indices of classes $C _ { h }$ for which all compatible preference models assign a to $C _ { h } .$ That is, the necessary and possible assignments for the threshold-based procedure are:

$$
C _ {P} (a) = \left\{h \in H: \exists (U, t) \in (\mathcal {U}, t) ^ {R}, C ^ {(U, t)} (a) = h \right\},
$$

$$
C _ {N} (a) = \left\{h \in H: \forall (U, t) \in (\mathcal {U}, t) ^ {R}, C ^ {(U, t)} (a) = h \right\},
$$

and the assignments for the example-based procedure the following:

$$
C _ {P} (a) = \left\{h \in H: \exists U \in \mathcal {U} ^ {R}, L ^ {U} (a) \leq h \leq R ^ {U} (a) \right\},
$$

$$
C _ {N} (a) = \left\{h \in H: \forall U \in \mathcal {U} ^ {R}, L ^ {U} (a) \leq h \leq R ^ {U} (a) \right\}.
$$

Let us now de<sup>fi</sup>ne $L _ { P } ( a ) , R _ { P } ( a ) , L _ { N } ( a )$ , and $R _ { N } ( a )$ as indices of the worst and the best classes to which alternative a is assigned possibly (P) or necessarily (N) by the set of compatible instances of the preference model, i.e.:

$$
C _ {P} (a) = \left[ L _ {P} (a), R _ {P} (a) \right], \text { and } C _ {N} (a) = \left[ L _ {N} (a), R _ {N} (a) \right].
$$

3.1.1. Computation of the possible and necessary assignments for the threshold-based procedure

The possible assignment of $a \in A$ can be computed by considering Theorem 1 for each $h \in H .$

Theorem 1. a $\quad A , \forall h \in H , \exists ( U , \mathbf { t } ) \in ( \mathcal { U } , \mathbf { t } ) ^ { R } \colon C ^ { ( U , \mathbf { t } ) } ( a ) = h , \mathrm { i . e . } a \longrightarrow ^ { P } C _ { h } i f f$ $E ^ { T H } ( a \to ^ { P } C _ { h } )$ ) given below is feasible and $\varepsilon ^ { * } { = } m a x \varepsilon s . t . { \cal E } ^ { T H } ( a {  } ^ { P } C _ { h } ) { > } 0 .$

$$
\left. \begin{array}{l l} [ A 1 ] & U (a) \geq t _ {h - 1}, i f h \geq 1, \\ [ A 2 ] & U (a) + \varepsilon \leq t _ {h}, i f h \leq p - 1, \\ [ A 3 ] & E ^ {T H}. \end{array} \right\} E ^ {T H} \Big (a \to^ {P} C _ {h} \Big)
$$

Proof. In e-Appendix A.1.

The necessary assignment of alternative a is computed by consid ering Theorem 2 for each $h \in H .$

Theorem 2. ∀a∈A, ∀h∈H, $\forall ( U , \mathbf { t } ) \in ( { \mathcal { U } } , \mathbf { t } ) ^ { R } \colon C ^ { ( U , \mathbf { t } ) } ( a ) { = } h , { \mathrm { i } } . \mathrm { e } . a { \to } ^ { N } C _ { h }$ $i f f ~ E ^ { T H } ~ ( { \mathsf { a } } \to { \mathsf { ^ { N } } } C _ { h } )$ <sup>U</sup>given below is infeasible or $\varepsilon ^ { * } = m a x \ { \textit { \varepsilon } } \ s . t . \ E ^ { T H }$ $( a  { } ^ { N } C _ { h } ) \leq 0$

$$
\left. \begin{array}{l l} [ B 1 ] & U (a) + \varepsilon \leq t _ {h - 1} + M \cdot v _ {1}, \quad i f h \geq 1, \\ [ B 2 ] & U (a) \geq t _ {h} - M \cdot v _ {2}, \quad i f h \leq p - 1, \\ [ B 3 ] & v _ {1} + v _ {2} = 1, \quad i f 1 \leq h \leq p - 1, \\ [ B 4 ] & v _ {1}, v _ {2} \in \{0, 1 \}, \\ [ B 5 ] & E ^ {\mathsf {T H}}, \end{array} \right\} E ^ {\mathsf {T H}} \Big (a \to^ {N} C _ {h} \Big)
$$

where M is a big positive value (in fact, it is enough $i f M > 1 )$ .

Proof. In e-Appendix A.2.

Note that instead of using the Mixed-Integer Linear Programming (MILP) formulation $E ^ { T H } ( a \to ^ { N } C _ { h } )$ , we can consider two separate sets of Linear Programming (LP) constraints: $\{ E ^ { T H } \cup U ( a ) + \varepsilon \leq { t _ { h } } _ { - 1 } \}$ and $\{ E ^ { T H } \cup U ( a ) \geq \bar { t _ { h } } \}$ . Then, by proceeding analogously to the analysis of $a  ^ { N } C _ { h } ,$ we can verify whether either $U ( a ) \geq t _ { h - 1 } \ \mathrm { o r } \ U ( a ) < t _ { h }$ holds $\forall ( U , \mathbf { t } ) \in ( \mathcal { U } , \mathbf { t } ) ^ { R }$ , similarly to what is proposed in Ref. [6].

3.1.2. Computation of the possible and necessary assignments for the example-based procedure

Computing the possible assignment for a∈A requires considering Theorem 3 for each $h \in H .$

Theorem 3. a $A , \forall h \in H ; a \longrightarrow ^ { P } C _ { h } { \mathrm { ~ } } i f f E ^ { E X } ( a \longrightarrow ^ { P } C _ { h } )$ given below is feasible and $\varepsilon ^ { * } { = } m a x \varepsilon s . t . E ^ { E X } ( a {  } ^ { P } C _ { h } ) { > } 0 ,$

$$
\begin{array}{l l} [ C 1 ] & U (a) + \varepsilon \leq U (a ^ {*}), \quad \forall a ^ {*} \in A ^ {R}: L _ {D M} (a ^ {*}) > h,   i f   h \leq p - 1, \\ [ C 2 ] & U (a) \geq U (a ^ {*}) + \varepsilon , \quad \forall a ^ {*} \in A ^ {R}: R _ {D M} (a ^ {*}) <   h,   i f   h \geq 2, \\ [ C 3 ] & E ^ {E X}. \end{array} \Bigg \} E ^ {E X} \left(a \to^ {P} C _ {h}\right).
$$

Proof. In e-Appendix A.3.

The necessary assignment for $a \in A$ can be computed by considering Theorem 4 for each $h \in H .$

Theorem 4. $\forall a \in A , \forall h \in H : a \to ^ { N } C _ { h } { \ i f f \ } E ^ { E X } ( a \to ^ { N } C _ { h } )$ given below is infeasible or $\varepsilon ^ { * } = m a x \varepsilon s . t . E ^ { E X } ( a  ^ { N } C _ { h } ) { \leq } 0 .$

$$
\left. \begin{array}{l l} [ D 1 ] & U (a) \geq U (a ^ {*}) - M \cdot v _ {a ^ {*}}, \forall a ^ {*} \in A ^ {R}: L _ {D M} (a ^ {*}) > h, \quad i f \quad h \leq p - 1, \\ [ D 2 ] & U (a) \leq U (a ^ {*}) + M \cdot v _ {a ^ {*}}, \forall a ^ {*} \in A ^ {R}: R _ {D M} (a ^ {*}) <   h, \quad i f \quad h \geq 2, \\ [ D 3 ] & \Sigma_ {a ^ {*} \in A ^ {h}} v _ {a ^ {*}} = | A ^ {h} | - 1, \\ [ D 4 ] & v _ {a ^ {*}} \in \{0, 1 \}, \forall a ^ {*} \in A ^ {h}, \\ [ D 5 ] & E ^ {E X}, \end{array} \right\} E ^ {E X} \Big (a \to^ {N} C _ {h} \Big)
$$

where $A ^ { h } = \{ a ^ { * } \in A ^ { R } : L _ { D M } ( a ^ { * } ) > h i f h \leq p - 1 , o r R _ { D M } ( a ^ { * } ) < h , i f h \geq 2 \}$

Proof. In e-Appendix A.4.

Analogously to the threshold-based procedure, instead of using the above MILP formulation, we can verify individually for each of the |A<sup>h</sup>| conditions whether they hold for at least one $\bar { U } \in \mathcal { U } ^ { R } .$ In this case we need to solve at most $2 \cdot | A ^ { R } |$ LP problems. Further discussion on the problem formulation and on an alternative approach can be found in e-Appendix B.

## 3.2. Possible and necessary assignment-based preference relations

For the threshold-based sorting procedure, the possible $( \succsim ^ {  , P } )$ and necessary $( \succ ) ^ {  , N } )$ assignment-based weak preference relations are de<sup>fi</sup>ned as:

$$
a \succeq \rightarrow , P b \Longleftrightarrow \exists (U, t) \in (\mathcal {U}, t) ^ {R}: C ^ {(U, t)} (a) \geq C ^ {(U, t)} (b),\tag{4}
$$

$$
a \succeq \rightarrow , N b \Longleftrightarrow \forall (U, t) \in (\mathcal {U}, t) ^ {R}: C ^ {(U, t)} (a) \geq C ^ {(U, t)} (b),\tag{5}
$$

and for the example-based sorting procedure, these relations are:

$$
a \succeq \rightarrow , P b \Leftrightarrow \exists U \in \mathcal {U} ^ {R} \left[ L ^ {U} (a) \geq L ^ {U} (b) \right] \text {   and   } \left[ R ^ {U} (a) \geq R ^ {U} (b) \right],\tag{6}
$$

$$
a \succeq \rightarrow , N b \Longleftrightarrow \forall U \in \mathcal {U} ^ {R}: \left[ L ^ {U} (a) \geq L ^ {U} (b) \right] \text { and } \left[ R ^ {U} (a) \geq R ^ {U} (b) \right].\tag{7}
$$

I ${ \mathrm { : } } a \gtrsim \cdots b ,$ , alternative a is always assigned to a class at least as good as alternative b. On the other hand, if $a \succsim \cdots b ,$ , a is sometimes assigned to a class not worse than b. Finally, if $\neg ( a \succeq \neg { } ^ { \neg } b )$ then b is assigned to a class better than a for all compatible instances of the preference model. $\succeq ^ {  , P } \mathrm { a n d } \succeq ^ {  , N }$ satisfy the following properties:

Proposition 1.

1. $\succsim ^ {  , N } \subseteq \succsim ^ {  , P } ;$

$\smash { 2 . \gtrsim ^ {  , N } \mathrm { i } s }$ a partial preorder (i.e., it is re<sup>fl</sup>exive $( \forall a \in A , a \gtrsim ^ {  , N } a )$ and transitive $( \forall a , b , c \in A , { \mathrm { i f } } a \not \simeq \not \sim \not \sim N _ { b }$ and $b \succeq  , N _ { C } ^ { \dagger } ,$ then $a \gtrsim ^ {  , N } c ) )$ 3. $\succsim \to , P$ is strongly complete $( { \mathrm { i . e . , } } \forall a , b { \in } A , a { \stackrel { } { \sim } } { \overset {  } {  } } b \ { \mathrm { o r } } \ b { \succeq } ^ {  , P } a )$ and negatively transitive $( { \mathrm { i . e . , ~ } } \forall a , b , c { \in } A , { \mathrm { i f ~ } } { \neg } ( a \succ ^ {  , P } b )$ and $\neg ( b \succsim \neg , P _ { C } )$ then $\neg ( a \overset { \cdot } { \approx } \neg ^ { P } c ) )$ binary relation.

Proof. In e-Appendix C.

3.2.1. Computation of the relations for the threshold-based procedure The truth of relation (4) is veri<sup>fi</sup>ed by considering Theorem 5.

Theorem 5. $\forall a , b \in A : a \succ {  } { \cal P } b i f f \equiv h \in \{ 1 , . . . , p \}$ such that $E _ { h } ^ { T H } ( a \gtrsim \AA ^ {  , P } b )$ given below is feasible and $\varepsilon ^ { * } =$ max ε s. t. $E _ { h } ^ { T H } ( a \gtrsim \AA ^ {  , P } b ) > 0$

$$
\begin{array}{l l}[ E 1 ]&U (a) \geq t _ {h - 1}, \quad i f h \geq 1,\\[ E 2 ]&U (b) + \varepsilon \leq t _ {h}, \quad i f h \leq p - 1,\\[ E 3 ]&E ^ {T H}.\end{array}\Bigg \} E _ {h} ^ {T H} \Big (a \succeq \rightarrow , P b \Big).\tag{8}
$$

Proof. In e-Appendix D.1.

Relation (5) can be computed by considering Theorem 6.

Theorem 6. $\forall a , b \in A : a \asymp ^ {  , N } b i f f \forall h \in \{ 1 , \dots , p - 1 \} : E _ { h } ^ { T H } ( a \asymp ^ {  , N } b )$ given below is infeasible or $\varepsilon ^ { * } =$ max ε s. t. $E _ { h } ^ { T H } ( a \gtrsim \AA ^ {  , N } b ) \leq 0$

$$
\begin{array}{l l}[ F 1 ]&U (b) \geq t _ {h},\\[ F 2 ]&U (a) + \varepsilon \leq t _ {h},\\[ F 3 ]&E ^ {T H}.\end{array}\Bigg \} E _ {h} ^ {T H} \Big (a \succeq \rightarrow , N   b \Big).\tag{9}
$$

Proof. In e-Appendix D.2.

3.2.2. Computation of the relations for the example-based procedure $a \succsim \ l ^ { - , P } b$ for the example-based procedure iff one of the following holds:

1. $a \succ \to ^ { P } b$ , i.e. $\exists U { \in } { \mathcal { U } } ^ { R } : U ( a ) \geq U ( b ) ;$

$2 . \neg ( a \succeq \neg { } ^ { \neg } b )$ , i.e. $\forall U { \in } U ^ { R } : U ( a ) { \textless } U ( b )$ , but $\exists U { \in } { \mathcal { U } } ^ { R }$ that assigns a and b to the same range $\left[ C _ { h _ { L } } , C _ { h _ { R } } \right]$

The <sup>fi</sup>rst condition can be veri<sup>fi</sup>ed with the LP discussed in e-Appendix E. For the second condition, note that an assignment to $\left[ C _ { h _ { L } } , C _ { h _ { R } } \right]$ is possible if $\beth ( h _ { L } , h _ { R } ) \in \ b { H } \times \ b { H }$ such that:

$$
\left. \begin{array}{c} h _ {L} \in \Bigl \{h \in H, \exists a ^ {*} \in A ^ {R}: L _ {D M} (a ^ {*}) = h _ {L} \Bigr \}, \\ h _ {R} \in \Bigl \{h \in H, \exists a ^ {*} \in A ^ {R}: R _ {D M} (a ^ {*}) = h _ {R} \text {   and   } \Bigl [ L _ {D M} (a ^ {*}) = h _ {L} \\ \text { or } \Bigl (L _ {D M} (a ^ {*}) = r > h _ {L}: \nexists b ^ {*} \in A ^ {R}, h _ {L} <   L _ {D M} (b ^ {*}) <   r \Bigr ] \Bigr \}. \end{array} \right\}\tag{10}
$$

Theorem 7. The set of conditions that guarantee assignment of $\mathrm { \dot { \boldsymbol { a } } } \in { \cal A }$ to the range of classes $\left[ C _ { h _ { L } } , C _ { h _ { R } } \right]$ is the following:

$$
\left. \begin{array}{l} [ G 1 ] U (a) \geq U (a ^ {*}) - M \cdot v _ {a ^ {*}}, \forall a ^ {*} \in A ^ {R}, L _ {D M} (a ^ {*}) = h _ {L}, \\ [ G 2 ] \sum_ {a ^ {*} \in A ^ {h _ {L}}} v _ {a ^ {*}} = \left| A ^ {h _ {L}} \right| - 1, \\ [ G 3 ] U (a) + \varepsilon \leq U (a ^ {*}), \forall a ^ {*} \in A ^ {R}, L _ {D M} (a ^ {*}) > h _ {L}, \\ [ G 4 ] U (a) \leq U (a ^ {*}) + M \cdot v _ {a ^ {*}}, \forall a ^ {*} \in A ^ {R}, R _ {D M} (a ^ {*}) = h _ {R}, \\ [ G 5 ] \sum_ {a ^ {*} \in A ^ {h _ {R}}} v _ {a ^ {*}} = \left| A ^ {h _ {R}} \right| - 1, \\ [ G 6 ] U (a) \geq U (a ^ {*}) + \varepsilon , \forall a ^ {*} \in A ^ {R}, R _ {D M} (a ^ {*}) <   h _ {R}, \\ [ G 7 ] v _ {a ^ {*}} \in \{0, 1 \}, \forall a ^ {*} \in A ^ {R}, L _ {D M} (a ^ {*}) = h _ {L}   o r   R _ {D M} (a ^ {*}) = h _ {R}, \end{array} \right\} E \Big (a \to \Big [ C _ {h _ {L}}, C _ {h _ {R}} \Big ] \Big)\tag{11}
$$

where $A ^ { h _ { L } } = \left\{ a ^ { * } { \in } A ^ { R } , L _ { D M } ( a ^ { * } ) = h _ { L } \right\}$ and $A ^ { h _ { R } } = \left\{ a ^ { * } { \in } A ^ { R } , R _ { D M } ( a ^ { * } ) = h _ { R } \right\}$ Proof. In e-Appendix D.3. □

Now, to compute $a \succsim \ l ^ { - , P } b$ we need to consider Theorem 8.

Theorem 8. $\forall a , b \in A : a \succeq ^ {  , P } b$ iff either $a \succsim { ^ P b }$ or $E _ { ( h _ { L } , h _ { R } ) } ^ { E X } \big ( a \mathfrak { z } ^ {  , P } b \big )$ given below is feasible and ε max ε s:t: $E _ { ( h _ { L } , h _ { R } ) } ^ { E X } \Big ( a \mathrm { \lesssim } ^ { \setminus \bigcirc } , P _ { b } \Big ) \mathrm { \sim } ^ { \mathrm { \ i } } 0$ for a pair $( h _ { L } , h _ { R } )$ satisfying (10).

$$
\begin{array}{l l} \text {[ H 1 ]} & E \Big (a \to \Big [ C _ {h _ {L}}, C _ {h _ {R}} \Big ] \Big), \\ \text {[ H 2 ]} & E \Big (b \to \Big [ C _ {h _ {L}}, C _ {h _ {R}} \Big ] \Big), \\ \text {[ H 3 ]} & U (a) + \varepsilon \leq U (b), \\ \text {[ H 4 ]} & E ^ {E X}. \end{array} \Bigg \} E _ {(h _ {L}, h _ {R})} ^ {E X} \Big (a \succeq \to , P b \Big).
$$

Proof. In e-Appendix D.4.

$a \succsim \ l ^ {  , N } b$ for the example-based procedure iff the following conditions hold:

$$
\begin{array}{l} \textbf {1 .} \forall U \in \mathcal {U} ^ {R}: L ^ {U} (a) \geq L ^ {U} (b); \\ \textbf {2 .} \forall U \in \mathcal {U} ^ {R}: R ^ {U} (a) \geq R ^ {U} (b). \end{array}
$$

The <sup>fi</sup>rst condition can be veri<sup>fi</sup>ed by considering Theorem 9.

Theorem 9. ∀a, $b { \in } A , \forall U { \in } { \mathcal { U } } ^ { R } ; L ^ { U } ( a ) \ge L ^ { U } ( b ) i f f \forall h { \in } \{ 2 , . . . , p \}$ , such that $\exists a ^ { * } \in A ^ { R } , \ L _ { D M } ( a ^ { * } ) = h$ <sup>U</sup>the set of constraints $E _ { h , L } ^ { E X } a \gtrsim \AA ^ {  , N } b )$ given below is infeasible or ε\* =max ε s. t. $E _ { h , L } ^ { E X } \left( a \gtrsim \cdots { } ^ { N } b \right) \leq 0 .$

$$
\left.\begin{array}{l}[ I 1 ] \quad U (a) + \varepsilon \leq U (a ^ {*}), \forall a ^ {*} \in A ^ {R}: L _ {D M} (a ^ {*}) \geq h,\\[ I 2 ] \quad U (b) \geq U (a ^ {*}) - M \cdot v _ {a ^ {*}}, \forall a ^ {*} \in A ^ {R}: L _ {D M} (a ^ {*}) \geq h,\\[ I 3 ] \quad \sum_ {A ^ {h, L}} v _ {a ^ {*}} = \left| A ^ {h, L} \right| - 1,\\[ I 4 ] \quad v _ {a ^ {*}} \in \{0, 1 \}, \forall a ^ {*} \in A ^ {R}: L _ {D M} (a ^ {*}) \geq h,\\[ I 5 ] E ^ {E X},\end{array}\right\} E _ {h, L} ^ {E X} \Big (a \succeq \rightarrow , N   b \Big)\tag{12}
$$

where $A ^ { h , L } = \{ a ^ { * } \in A ^ { R } \colon L _ { D M } ( a ^ { * } ) \geq h \}$

Proof. In e-Appendix D.5 (Condition 1).

The second condition can be veri<sup>fi</sup>ed by considering Theorem 10.

Theorem 10. ∀a $\ u , b \in { A } , \forall U \in { \mathcal { U } } ^ { R } \colon R ^ { U } ( a ) \geq R ^ { U } ( b )$ iff $\forall h { \in } \{ 1 , ~ . . . , p - 1 \}$ such that $\exists a ^ { * } \in A ^ { R } , R _ { D M } ( a ^ { * } ) = h$ , the set of constraints $E _ { h , R } ^ { E X } ( a \gtrsim \AA ^ {  , N } b )$ given below is infeasible or ε\*=max ε s.t. $E _ { h , R } ^ { E X } ( a \gtrsim \AA ^ {  , N } b ) \breve { \leq } 0 .$

$$
\left.\begin{array}{l l}[ J 1 ]&U (b) \geq U (a ^ {*}) + \varepsilon , \forall a ^ {*} \in A ^ {R}: R _ {D M} (a ^ {*}) \leq h,\\[ J 2 ]&U (a) \leq U (a ^ {*}) + M \cdot v _ {a ^ {*}}, \forall a ^ {*} \in A ^ {R}: R _ {D M} (a ^ {*}) \leq h,\\[ J 3 ]&\sum_ {A ^ {h, R}} v _ {a ^ {*}} = \left| A ^ {h, R} \right| - 1,\\[ J 4 ]&v _ {a ^ {*}} \in \{0, 1 \}, \forall a ^ {*} \in A ^ {R}: R _ {D M} (a ^ {*}) \leq h,\\[ J 5 ]&E ^ {E X},\end{array}\right\} E _ {h, R} ^ {E X} \Big (a \succeq \rightarrow , N b \Big)\tag{13}
$$

where $A ^ { h , R } = \{ a ^ { * } \in A ^ { R } \colon R _ { D M } ( a ^ { * } ) \leq h \}$

Proof. In e-Appendix D.5 (Condition 2).

Note that the number of MILP that need to be solved can be reduced by <sup>fi</sup>rst computing the necessary preference relation $a \succsim { ^ N b }$ (see e-Appendix E), as $U ( a ) \geq U ( b ) \forall U \in \bar { \mathcal { U } } ^ { R } \Rightarrow \bar { L } ^ { U } ( a ) \geq L ^ { U } ( b ) , R ^ { U } ( a ) \geq$ $R ^ { U } ( b ) \forall U { \in } \mathcal { U } ^ { R } \Rightarrow a { \succeq } \neg \neg , N _ { \textrm { b } }$ :

## 3.3. Class acceptability indices

When using the threshold-based sorting procedure, the class acceptability index $C A I ( a , h ) \in [ 0 , 1 ]$ is the share of compatible pairs (U, $\mathbf { t } ) \bar { \in } ( \mathcal { U } , \bar { \mathbf { t } } ) ^ { \bar { R } }$ that assign alternative a to class $C _ { h } .$ . It is computed as a multi-dimensional integral over the space of uniformly distributed value functions and assignment thresholds compatible with the assignment examples:

$$
C A I (a, h) = \int_ {(U, t) \in (\mathcal {U}, t) ^ {R}} m (U, t, a, h) d (U, t),\tag{14}
$$

where $m ( U , \mathbf { t } , a , h )$ is the class membership function:

$$
m (U, t, a, h) = \left\{ \begin{array}{l l} 1, & \text { if } U (a) \in \Big [ t _ {h - 1}, t _ {h} \Big ], \\ 0, & \text { otherwise }. \end{array} \right.
$$

The class acceptability index can be interpreted as a probability of membership to the particular class. Note that $\sum { } _ { h = 1 } ^ { p } C A I ( a , h ) = 1$ for each $\mathsf { a } \in A .$

The class acceptability index for the example-based sorting procedure, $C \ A I ( \ a , \ [ h _ { L } , \ h _ { R } ] )$ , is de<sup>fi</sup>ned on a range of contiguous classes $\left[ C _ { h _ { L } } , C _ { h _ { L } + 1 } , . . . , C _ { h _ { R } } \right]$ , with $h _ { L } { \leq } h _ { R } ~ ( h _ { L } , ~ h _ { R } { \in } H )$ , analogously <sup>þ</sup>to (14) as the share of compatible value functions $U { \in } { \mathcal { U } } ^ { R }$ that assign alternative a precisely to the range of classes $\left[ C _ { h _ { L } } , C _ { h _ { L } + 1 } , . . . , C _ { h _ { R } } \right]$ (i.e., $L ^ { U } \ ( a ) = h _ { I }$ and $\begin{array} { r } { R ^ { U } ( a ) = h _ { R } ) } \end{array}$ . Note that $\begin{array} { r } { \forall a \in A : \sum _ { [ h _ { L } , h _ { R } ] : 1 \leq h _ { L } \leq h _ { R } \leq p } C A I ( a , [ h _ { L } , h _ { R } ] ) = 1 . } \end{array}$

We can also compute the share of $U { \in } { \mathcal { U } } ^ { R }$ for which $C _ { h }$ is within $\left[ C _ { L ^ { U } } ( a ) , . . . , C _ { R ^ { U } } ( a ) \right]$ <sup>U</sup>, i.e. the share of functions that either precisely or <sup>ð Þ ð Þ</sup>imprecisely assign a to $C _ { h } .$ Let us call such a share the cumulative class acceptability index $C u C A I ( a , h )$ . We de<sup>fi</sup>ne it as:

$$
C u C A I (a, h) = \sum_ {[ h _ {L}, h _ {R} ]: h \in [ h _ {L}, h _ {R} ]} C A I (a, [ h _ {L}, h _ {R} ]).\tag{15}
$$

## 3.4. Assignment-based pair-wise outranking indices

The assignment-based pair-wise outranking index $A P O I ( a , b )$ is de<sup>fi</sup>ned for the threshold-based sorting procedure as the share of compatible pairs $( U , \mathbf { t } ) \in ( \mathcal { U } , \mathbf { t } ) ^ { R }$ that assign a to a class at least as good as b. It is computed as a multi-dimensional integral over the space of uniformly distributed value functions and assignment thresholds compatible with the assignment examples:

$$
A P O I (a, b) = \int_ {(U, t) \in (\mathcal {U}, t) ^ {R}} C ^ {(U, t)} (a) \succeq C ^ {(U, t)} (b) d (U, t).\tag{16}
$$

For the example-based procedure, $A P O I ( a , b )$ is de<sup>fi</sup>ned analogously to Eq. (16) as the share of compatible value functions $U { \in } { \mathcal { U } } ^ { R }$ <sup>U</sup>assigning a to the range of classes which is at least as good as the range of classes of b, i.e. $L ^ { U } ( a ) { \geq } L ^ { U } ( b )$ and $R ^ { U } ( a ) { \geq } R ^ { U } ( b )$ . Consequently, for any $( a , b ) \in A \times A { \mathrm { : } }$

$$
A P O I (a, b) \in [ 0, 1 ] \text {   and   } A P O I (a, b) + A P O I (b, a) \geq 1,
$$

and $A P O I ( a , a ) = 1$ . We de<sup>fi</sup>ne the share of compatible instances of the preference model for which a is assigned to a class strictly better than b as the assignment-based pair-wise winning index, APWI(a, $b ) = 1 - A P O I ( b , a )$

## 3.5. Estimation of the stochastic model

Estimating CAI and APOI require sampling uniformly from the set of compatible value functions, and additionally from the space of thresholds for the threshold-based procedure. The level values of a general monotone marginal value function $u _ { j } ( \cdot )$ with $n _ { j }$ levels are obtained by sampling uniformly $n _ { j } - 2$ numbers from [0,1], sorting them in an ascending order, and adding 0 to the beginning of the sequence and 1 to the end (Algorithm 1 in Ref. [21]). A similar procedure can be used for sampling the threshold values by adjusting the last sequence number to be >1. After sampling all n marginal value functions, they are scaled with weights sampled uniformly from an $n - 1$ simplex (Algorithm 2 in Ref. [21]). This leads to sampling uniformly from the space of all general monotone value functions. To sample from the restricted space, a naive rejection technique can be applied in low dimensionality problems as only 10,000 functions are needed to estimate the indices with a suf<sup>fi</sup>cient accuracy [21].

## 3.6. Results of ROR versus outcomes of SMAA

The stochastic indices CAI, CuCAI and APOI can be computed exactly only in very small problems and in this section we will consider their estimations computed through Monte Carlo simulation, CAI′, CuCAI and APOI′. Let us denote the sample of pairs (U, t) taken into account in the simulation process of SMAA by $( { \bar { \mathcal { U } } } , \mathbf { t } ) ^ { S M A A } \subseteq ( { \mathcal { U } } , \mathbf { t } ) ^ { R }$ , and the respective sample of value functions U by $\mathcal { U } ^ { S M A A } \subseteq \mathcal { U } ^ { R } .$

<sup>U U</sup>The outcomes of ROR and SMAA concerning assignments to classes with the threshold-based procedure relate to each other as follows:

## Proposition 2. For an alternative $a \in A { : }$

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
1.  $h \in [1, L_{P}(a)) \cup (R_{P}(a), p] \Rightarrow CAI'(a, h) = 0;$ 
2.  $h \in [L_{P}(a), R_{P}(a)] \Rightarrow CAI'(a, h) \in [0,1];$ 
3.  $\sum_{h=L_{p}(a)}^{R_{p}(a)} CAI'(a,h)=1;$ 
4.  $h=C_{N}(a) \Rightarrow CAI'(a,h)=1;$ 
5.  $CAI'(a, h) &gt; 0 \Rightarrow h \in [L_{P}(a), R_{P}(a)], i.e., L_{P}(a) \leq h \text{ and } h \leq R_{P}(a); in particular, CAI'(a, h) = 1 \Rightarrow h \in [L_{P}(a), R_{P}(a)];$ 
6.  $CAI'(a, h) &lt; 1 \Rightarrow h \neq C_{N}(a).$
</div>

## Proof. Considering an alternative $a \in A { : }$

1. If h ∉ $[ L _ { P } ( a ) , R _ { P } ( a ) ]$ , there is no compatible pair $( U , \mathbf { t } ) \in ( \mathcal { U } , \mathbf { t } ) ^ { R } \supseteq ( \mathcal { U } _ { \dag }$ $\mathbf { t } ) ^ { S M A \bar { A } }$ assigning a to $C _ { h } ;$ hence $C A I ^ { \prime } ( a , h ) = 0 $

2. If $h \in [ L _ { P } ( a ) , ~ R _ { P } ( a ) ] ,$ , there may be no compatible pair $( U , { \bf t } ) { \in } ( { \mathcal { U } } ,$ $\mathbf { t } ) ^ { S M A \dot { A } }$ assigning a to $C _ { h } ,$ in case $( \mathcal { U } , \mathbf { t } ) ^ { S M A \bar { A } } { \subset } ( \mathcal { U } , \bar { \mathbf { t } } ) ^ { R } ;$ ; then $C A I ^ { \prime } ( a ,$ $h ) = 0 .$ <sup>U U</sup>. Alternatively, the sample analyzed in SMAA may contain at least one compatible instance $( U , \mathbf { t } ) { \dot { \in } } ( { \mathcal { U } } , \mathbf { t } ) ^ { S M A A }$ assigning a to $C _ { h } ;$ then $C A I ^ { \prime } ( a , h ) > 0$ . Hence, $\mathrm { i f } \ h { \in } [ L _ { P } ( a ) , R _ { P } ( a ) ]$ , then $C A I ^ { \prime } ( a , h ) \in [ 0 , 1 ]$ This implies that the range of possible classes may be wider than the set of classes for which $C A I ^ { \prime } ( a , h ) > 0$

$$
\{h \in [ 1, L _ {P} (a)) \cup (R _ {P} (a), p ] \Rightarrow C A I ^ {\prime} (a, h) = 0 \}
$$

$$
h) = 1 \}
$$

$$
\left\{\sum_ {h = 1} ^ {p} C A I ^ {\prime} (a, \right.
$$

$$
\sum_ {h = L _ {p} (a)} ^ {R _ {P} (a)} C A I ^ {\prime} (a, h) = 1.
$$

4. If the necessary assignment for a∈A is not empty, all compatible pairs $( U , \ \mathbf { t } ) \in ( \mathcal { U } , \ \mathbf { t } ) ^ { \bar { R } } \supseteq ( \mathcal { U } , \ \mathbf { t } ) ^ { S M A A }$ assign a to $C _ { h } ,$ such that $h =$ C<sub>N</sub>(a);hence $C A I ^ { \prime } ( a , h ) = 1$

5. If $C A I ^ { \prime } ( a , h ) > 0 ,$ , then there exists at least one compatible instance $( U , \mathbf { t } ) \in ( \mathcal { U } , \mathbf { t } ) ^ { R } \supseteq ( \mathcal { U } , \mathbf { t } ) ^ { S M A A }$ assigning a to $C _ { h } ,$ and thus $\textstyle h \in [ L _ { P } ( a )$ <sup>U</sup>R (a)]. Even if $C A I ^ { \prime } ( a , h ) = 1$ , there may be a compatible instance $( U , \mathbf { t } ) \in ( \mathcal { U } , { \mathbf { t } } ) ^ { R } \backslash ( \mathcal { U } , { \mathbf { t } } ) ^ { S M A A }$ not assigning a to $C _ { h } .$ Thus, in this case, <sup>U U</sup>we can only deduce that $h \in [ L _ { P } ( a ) , ~ R _ { P } ( a ) ]$ , but not $h = C _ { N } ( a )$ . In fact, with respect to the necessary assignment, from the analysis of CAI′ we can only infer the negative information.

6. If $C A I ^ { \prime } ( a , h ) { < } 1$ , then there exists at least one compatible instance $( U , \mathbf { t } ) \dot { \in } ( \mathcal { U } , \dot { \mathbf { t } } ) ^ { R } \supseteq ( \mathcal { U } , \mathbf { t } ) ^ { S M A A }$ not assigning a to $C _ { h } ;$ hence $h \neq C _ { N } ( a )$ . □

The interdependencies between the outcomes of ROR and SMAA concerning assignments to classes with the example-based procedure are summarized by the following proposition.

## Proposition 3. For an alternative $a \in A { : }$

1. $\neg ( [ h _ { L } , h _ { R } ] \subseteq [ L _ { P } ( a ) , R _ { P } ( a ) ] ) \Rightarrow C A I ^ { \prime } ( a , [ h _ { L } , h _ { R } ] ) = 0 ;$

$$
([ h _ {L}, h _ {R} ] \subseteq [ L _ {P} (a), R _ {P} (a) ] \Rightarrow C A I ^ {\prime} (a, [ h _ {L}, h _ {R} ]) \in [ 0, 1 ];
$$

$$
\sum_ {[ h _ {L}, h _ {R} ]: L _ {P} (a) \leq h _ {L} \leq h _ {R} \leq R _ {P} (a)} C A I ^ {\prime} (a, [ h _ {L}, h _ {R} ]) = 1;
$$

4. $C A \dot { I } ^ { \prime } ( a , [ h _ { L } , ~ h _ { R } ] ) > 0 \Rightarrow ( [ h _ { L } , ~ h _ { R } ] \subseteq ( [ L _ { P } ( a ) , ~ R _ { P } ( a ) ] ,$ , i.e., $L _ { P } ( a ) \leq h _ { L }$ and $h _ { R } { \leq } R _ { P } ( a ) ;$

5. $\begin{array} { r } { h \in C _ { N } ( a ) \Rightarrow C u C A I ^ { \prime } ( a , h ) = 1 ; } \end{array}$

6. $C u C A I ^ { \prime } ( a , h ) > 0 \Rightarrow h \in [ L _ { P } ( a ) , R _ { P } ( a ) ] , { \mathrm { i . e . , } } L _ { P } ( a ) \leq h$ and $h \leq R _ { P } ( a )$ ; in $\begin{array} { r l } { \mathrm { p a r t i c u l a r } , C u C A I ^ { \prime } ( a , h ) = 1 \Rightarrow h \in [ L _ { P } ( a ) , R _ { P } ( a ) ] ; } \end{array}$

$$
C u C A I ^ {\prime} (a, h) <   1 \Rightarrow \neg (h \subseteq C _ {N} (a)).
$$

Proof. 1–4 Analogously to the proof of Proposition 2 (1–4) with the exception of considering class acceptability with respect to the ranges of classes $[ h _ { L } , h _ { R } ]$ , with $h _ { L } \leq h _ { R } ,$ , rather than with respect to the individual classes $h \in H .$

5–7 Analogously to the proof of Proposition 2 (5–7) with the exception of considering $C u C A I ^ { \prime } ( a , h )$ rather than $C A I ^ { \prime } ( a , h )$ and assignments to the ranges of contiguous classes containing $C _ { h }$ rather than the precise assignments to $C _ { h } .$

Let us now discuss the interdependencies between the outcomes of ROR and SMAA concerning assignment-based preference relations. They are summarized by Proposition 4.

Proposition 4. For a pair of alternatives $a , b \in A { : }$

1. $a \gtrsim {  } , N b \Rightarrow A P O I ^ { \prime } ( a , b ) = 1 ;$

2. ¬(ac <sup>→,P</sup>b)⇒APOI' (a,b)=0 and APWI' (b, a)=1;

$$
A P O I ^ {\prime} (a, b) > 0 \Rightarrow a \succeq^ {\rightarrow , P} b;
$$

4. $A P O I ^ { * } ( a , b ) { < } 1 \Rightarrow \neg ( a \succeq ^ {  , N } b )$

Proof. Considering a pair of alternatives $a , b \in A \colon$

1. If $a \gtrsim \AA ^ {  , N } b ,$ , the class of a is at least as good as the class of b for all compatible instances of the preference model, including the sample analyzed in the simulation process of SMAA; hence $A P O I ^ { \prime } ( a , b ) = 1$

2. $[ \mathbf { f } \neg ( a \succsim \neg P b )$ , a is assigned to a class worse than b for all compatible instances of the preference model, including the sample analyzed in the simulation process of SMAA; hence $A P O I ^ { \prime } ( a , b ) = 0 \quad$

3. I $\mathrm { f } A P O I ^ { \prime } ( a , b ) > 0 ,$ there exists at least one compatible instance of the preference model assigning a to a class at least as good as b, and thus $a \succsim \ l ^ { - , P } b$

4. $1 \mathrm { f } A P O I ^ { \prime } ( a , b ) < 1$ , there exists at least one compatible instance of the preference model assigning a to a class worse than $b ,$ and thus $\neg ( a \succeq \neg , N _ { b } )$ □

Consequently, by analyzing APOI′ we can only deduce truth of the possible relation $( \operatorname { i f } A P O I ^ { \prime } ( a , b ) > 0 )$ or falsity of the necessary relation (if $\cdot { A P O I ^ { \prime } } ( a , b ) { < } 1 )$ , not the complete relations.

3.7. Relation between provided preference information and the model outcomes

The joint application of SMAA and ROR for multiple criteria sorting problems is designed for incremental speci<sup>fi</sup>cation of assignment examples. The suggested procedure is to provide new assignment examples for alternatives with multiple possible assignments but signi<sup>fi</sup>cantly higher CAI′ for a proper subset of $C _ { P } ( a )$ than for the remaining classes. In the same spirit, the DM may wish to make more precise the assignments of some reference alternatives already considered in the previous iteration. Furthermore, the DM may analyze the assignment-based weak preference relations, and in the following iteration provide disjoint assignments for pairs of alternatives $( a , \ b ) { \in } A { \times } A$ for which APWI(a,b) is close to one.

Note that for any $a ^ { * } \in A ^ { R }$ with $a ^ { * } {  } [ C _ { L _ { D M } ( a * ) } , C _ { R _ { D M } ( a * ) } ] [ 6 ] :$

$$
L _ {P} \left(a ^ {*}\right) \geq L _ {D M} \left(a ^ {*}\right) \text { and } R _ {P} \left(a ^ {*}\right) \leq R _ {D M} \left(a ^ {*}\right).
$$

If the assignment provided by the DM is precise, the necessary assignment is not empty. Thus, by providing more exemplary assignments, the DM may directly enrich the necessary assignment or make the possible assignment more precise. For a pair of reference alternatives $a ^ { * } , b ^ { * } \in { \check { A } } ^ { R }$ the following implications are satis<sup>fi</sup>ed when considering the ranges of desired classes provided by the DM:

$$
L _ {D M} \left(a ^ {*}\right) \geq R _ {D M} \left(b ^ {*}\right) \Rightarrow a \succ^ {\rightarrow , N} b \text { and } A P O I ^ {\prime} \left(a ^ {*}, b ^ {*}\right) = 1,
$$

$$
L _ {D M} \left(a ^ {*}\right) > R _ {D M} \left(b ^ {*}\right) \Rightarrow \neg \left(b \gtrsim^ {\rightarrow , P} a\right) \text {   and   } A P O I ^ {\prime} \left(b ^ {*}, a ^ {*}\right) = 0.
$$

## 3.8. Selection of a representative value function

If the set of value functions compatible with the provided preference information is not empty, traditional UTA-like methods apply some rules to select a single value function for the subsequent analysis (see e.g. [10,19,24]). These rules indicate the “mean”, “central”, or “most discriminant” value function. On the other hand, Refs. [8,11] introduced the notion of a representative value function. In this case, the representativeness of the selected value function is based on ROR outcomes that can be obtained with all compatible value functions. The representative preference model for sorting problems was originally selected with an interactive procedure that involved the DM supplying priorities with respect to pre-de<sup>fi</sup>ned targets [8]. For example, if the advantage of one alternative over the other is acknowledged by all compatible value functions (e.g. if the worst possible class of a is better than the best possible class of $b ) _ { \cdot }$ , then the representative value function is selected so that the difference between the values of the two alternatives is maximized. On the contrary, if the comparison of a pair of alternatives is not clearly in favor of one of them (e.g. if for all compatible value functions a and b are assigned to the same class or the order of classes for a and b for different compatible functions is not univocal), then the representative value function should minimize the difference between their comprehensive values.

Selection of a single, representative value function allows less abstract analysis than that of the whole set of compatible value functions. In this way, the DM can assess alternatives based on exact numerical values and inspect relative importance of the criteria through their scaling constants. In addition, the possibility to represent numerous compatible sorting models with a single value function can improve robustness of decisions based on the applied model.

We provide a representative value function selection procedure that incorporates APWIs to allow formulating more precise requirements than those in Ref. [8] while sharing the same motivation and interpretation of representativeness. Incorporating APWI into the representative value function can help the DM understand better the results of the stochastic analysis. The general additive value functions provide measurable preference intensities $U ( a ) - U ( b )$ , and our procedure relates these intensities with $A P W I ^ { \prime } ( a , b )$ , that is, the share of compatible value functions for which a is assigned to a class better than b. In this way, we build the representative value function on the recommendation provided by all compatible value functions considered in the stochastic analysis.

Precisely, when considering the comparison of a and b, we promote an alternative assigned to a better class for the majority of compatible value functions. In such a case, a representative value function $U ^ { R E P }$ needs to satisfy the following additional requirement for $a , b \in A { : }$

$$
\text { if } A P W I ^ {\prime} (a, b) > A P W I ^ {\prime} (b, a), \text { then } U ^ {R E P} (a) > U ^ {R E P} (b).
$$

If the share of compatible value functions assigning a to a class better than b is greater than the share of compatible value functions for which a is assigned to a class worse than b, then it is reasonable to require $U ( a )$ to be greater than $U ( b )$ . The following procedure, called REPDIS, selects a representative value function for the example-based sorting procedure:

1. For all $a , b \in A ,$ , such that $A P W I ^ { \prime } ( a , b ) > A P W I ^ { \prime } ( b , a )$ , add the following constraints to the set of constraints $E ^ { E X } \mathrm { ; }$

$$
\begin{array}{l} U (a) - U (b) \geq \varepsilon (a, b), \\ \varepsilon (a, b) \geq \varepsilon . \end{array}
$$

2. Maximize $\varepsilon ,$ subject to the set of $\mathrm { L P }$ constraints from point (1), i.e. maximize the minimal intensity of preference for pairs $( a , b )$ , such that $A P W I ^ { \prime } ( a , b ) { > } A P W I ^ { \prime } ( b , a )$ . When using such a maximin rule, the obtained results can be easily interpreted, i.e. we can observe what is the minimal intensity of preference for pairs of alternatives satisfying the conditions.

3. Add the constraint $\varepsilon = \varepsilon ^ { * }$ , with $\varepsilon ^ { * } { = } m a x \varepsilon$ from the previous point, to the set of LP constraints considered in point (1). This allows to maintain the differences of values of pairs of alternatives considered in point (1) at their optimized levels.

4. Maximize $\sum a , b : A P W I ^ { \prime } ( a , b ) > A P W I ^ { \prime } ( b , a ) \mathcal { E } \big ( a , b \big )$ , subject to the set of LP constraints from point (3), i.e. choose a function for which the sum of elementary components optimized in point (2) is optimal. This allows potential tie-breaking between value functions for which $\varepsilon ^ { * }$ from point (3) is optimal.

5. Read off the representative comprehensive values $U ^ { R E P } ( a )$ and corresponding marginal values from the solution of the LP problem considered in point (4).

It is clear that each procedure for selecting a single value function implements a different idea, therefore introducing a degree of arbitrariness and instrumental bias into the obtained results, which will consequently vary depending on the procedure applied. We leave the choice of the most appropriate procedure for selecting a representative value function to the analyst.

## 4. Illustrative study

Let us consider a problem of assigning countries to four types of regimes: full democracies $( C _ { 4 } )$ , <sup>fl</sup>awed democracies $\left( C _ { 3 } \right)$ , hybrid regimes $\left( C _ { 2 } \right)$ , and authoritarian regimes (C<sub>1</sub>). This problem has been originally considered by the Economist Intelligence Unit (EIU) [4]. They took into account sixty indicators grouped in <sup>fi</sup>ve categories: electoral process and pluralism $\left( g _ { 1 } \right)$ , functioning of the government (g<sub>2</sub>), political participation $\left( g _ { 3 } \right)$ , political culture $( g _ { 4 } ) _ { \ i }$ , and civil liberties (g ). We classify $2 7$ countries (Table 2) applying the example-based sorting procedure and assume a DM to have provided preference information in form of the nine exemplary assignments in Table 3. These are consistent and the set of compatible instances of the preference model is not empty.

Countries' performance matrix, their possible and necessary assignments to the four types of regimes, and assignments with a representative value function selected with REPDIS.

<table><tr><td>Country (a)</td><td> $g_1$ (a)</td><td> $g_2$ (a)</td><td> $g_3$ (a)</td><td> $g_4$ (a)</td><td> $g_5$ (a)</td><td> $L_P$ (a)</td><td> $R_P$ (a)</td><td> $L_N$ (a)</td><td> $R_P$ (a)</td><td> $C^{REP}$ (a)</td></tr><tr><td>New Zealand</td><td>10.00</td><td>9.29</td><td>8.89</td><td>8.13</td><td>10.00</td><td>4</td><td>4</td><td>4</td><td>4</td><td> $C_4$ </td></tr><tr><td>Australia</td><td>10.00</td><td>8.93</td><td>7.78</td><td>9.38</td><td>10.00</td><td>4</td><td>4</td><td>4</td><td>4</td><td> $C_4$ </td></tr><tr><td>South Korea</td><td>9.17</td><td>7.86</td><td>7.22</td><td>7.50</td><td>8.83</td><td>3</td><td>4</td><td>-</td><td>-</td><td> $C_3-C_4$ </td></tr><tr><td>Japan</td><td>9.17</td><td>8.21</td><td>6.11</td><td>7.50</td><td>9.41</td><td>4</td><td>4</td><td>4</td><td>4</td><td> $C_4$ </td></tr><tr><td>Taiwan</td><td>9.58</td><td>7.14</td><td>5.56</td><td>5.63</td><td>9.71</td><td>3</td><td>3</td><td>3</td><td>3</td><td> $C_3$ </td></tr><tr><td>India</td><td>9.58</td><td>8.57</td><td>4.44</td><td>4.38</td><td>9.41</td><td>2</td><td>4</td><td>-</td><td>-</td><td> $C_3-C_4$ </td></tr><tr><td>Timor Leste</td><td>8.67</td><td>6.79</td><td>5.56</td><td>6.88</td><td>8.24</td><td>3</td><td>3</td><td>3</td><td>3</td><td> $C_3$ </td></tr><tr><td>Thailand</td><td>7.83</td><td>6.07</td><td>5.56</td><td>6.25</td><td>7.06</td><td>2</td><td>3</td><td>-</td><td>-</td><td> $C_2-C_3$ </td></tr><tr><td>Papua New Guinea</td><td>7.33</td><td>6.43</td><td>4.44</td><td>6.25</td><td>8.24</td><td>2</td><td>3</td><td>-</td><td>-</td><td> $C_2-C_3$ </td></tr><tr><td>Indonesia</td><td>6.92</td><td>7.50</td><td>5.58</td><td>5.63</td><td>7.06</td><td>2</td><td>4</td><td>-</td><td>-</td><td> $C_2-C_3$ </td></tr><tr><td>Mongolia</td><td>8.33</td><td>5.71</td><td>3.89</td><td>5.63</td><td>8.24</td><td>2</td><td>3</td><td>-</td><td>-</td><td> $C_2-C_3$ </td></tr><tr><td>Malaysia</td><td>6.50</td><td>6.79</td><td>5.56</td><td>6.25</td><td>5.88</td><td>3</td><td>3</td><td>3</td><td>3</td><td> $C_3$ </td></tr><tr><td>Philippines</td><td>8.33</td><td>5.00</td><td>5.00</td><td>3.13</td><td>9.12</td><td>1</td><td>3</td><td>-</td><td>-</td><td> $C_2-C_3$ </td></tr><tr><td>Hong Kong</td><td>3.50</td><td>5.36</td><td>4.44</td><td>6.88</td><td>9.41</td><td>2</td><td>2</td><td>2</td><td>2</td><td> $C_2$ </td></tr><tr><td>Singapore</td><td>4.33</td><td>7.50</td><td>2.78</td><td>7.50</td><td>7.35</td><td>1</td><td>4</td><td>-</td><td>-</td><td> $C_2-C_3$ </td></tr><tr><td>Bangladesh</td><td>7.42</td><td>5.43</td><td>4.44</td><td>5.00</td><td>7.06</td><td>2</td><td>2</td><td>2</td><td>2</td><td> $C_2$ </td></tr><tr><td>Cambodia</td><td>6.08</td><td>6.07</td><td>2.78</td><td>5.00</td><td>4.41</td><td>1</td><td>3</td><td>-</td><td>-</td><td> $C_1-C_2$ </td></tr><tr><td>Bhutan</td><td>6.25</td><td>5.36</td><td>3.89</td><td>4.38</td><td>3.53</td><td>2</td><td>2</td><td>2</td><td>2</td><td> $C_2$ </td></tr><tr><td>Pakistan</td><td>5.17</td><td>5.71</td><td>2.22</td><td>4.38</td><td>5.29</td><td>1</td><td>3</td><td>-</td><td>-</td><td> $C_1-C_2$ </td></tr><tr><td>Nepal</td><td>1.83</td><td>4.29</td><td>3.89</td><td>5.63</td><td>5.59</td><td>1</td><td>2</td><td>-</td><td>-</td><td> $C_1-C_2$ </td></tr><tr><td>Fiji</td><td>0.42</td><td>2.86</td><td>3.33</td><td>3.75</td><td>3.82</td><td>1</td><td>2</td><td>-</td><td>-</td><td> $C_1-C_2$ </td></tr><tr><td>China</td><td>0.00</td><td>5.00</td><td>3.89</td><td>5.63</td><td>1.18</td><td>1</td><td>1</td><td>1</td><td>1</td><td> $C_1$ </td></tr><tr><td>Vietnam</td><td>0.00</td><td>4.29</td><td>3.33</td><td>5.63</td><td>4.41</td><td>1</td><td>2</td><td>-</td><td>-</td><td> $C_1-C_2$ </td></tr><tr><td>Afghanistan</td><td>2.50</td><td>0.79</td><td>2.78</td><td>2.50</td><td>3.82</td><td>1</td><td>1</td><td>1</td><td>1</td><td> $C_1$ </td></tr><tr><td>Laos</td><td>0.00</td><td>3.21</td><td>1.11</td><td>5.00</td><td>1.18</td><td>1</td><td>1</td><td>1</td><td>1</td><td> $C_1$ </td></tr><tr><td>Myanmar</td><td>0.00</td><td>1.79</td><td>0.56</td><td>5.63</td><td>0.88</td><td>1</td><td>1</td><td>1</td><td>1</td><td> $C_1$ </td></tr><tr><td>North Korea</td><td>0.00</td><td>2.50</td><td>1.67</td><td>1.25</td><td>0.00</td><td>1</td><td>1</td><td>1</td><td>1</td><td> $C_1$ </td></tr></table>

Preference information provided by the DM for the problem of assigning countries to different types of regimes.

<table><tr><td>Class</td><td>Assigned countries</td></tr><tr><td> $C_4$ </td><td>Japan</td></tr><tr><td> $C_3$ </td><td>Taiwan, Timor Leste, Malaysia</td></tr><tr><td> $C_2$ </td><td>Hong Kong, Bangladesh, Bhutan</td></tr><tr><td> $C_1$ </td><td>China, Afghanistan</td></tr></table>

## 4.1. Possible and necessary assignments and class acceptability indices

The possible and necessary assignments are presented in Table 2. We additionally list countries possibly assigned to particular ranges of classes in Table 4. For these nine countries the necessary assignment is not empty. Another <sup>fi</sup>ve non-reference alternatives (New Zealand, Australia, Laos, Myanmar, North Korea) are precisely assigned to a single class $( C _ { 4 }$ or C ).

For the remaining 13 alternatives, the necessary assignment is empty and the possible assignments are imprecise. There are 7 countries possibly assigned to two consecutive classes $( \mathrm { i . e . , } C _ { 1 } \mathrm { - } C _ { 2 } \mathrm { o r } C _ { 2 } \mathrm { - } C _ { 3 }$ or $C _ { 3 ^ { - } } C _ { 4 } )$ and 5 countries with a possible assignment of three classes (i.e., $C _ { 1 } { - } C _ { 3 }$ or $C _ { 2 ^ { - } } C _ { 4 } )$ . The sole country possibly assigned to any class $C _ { 1 } { - } C _ { 4 }$ is Singapore (Table 4). The average width of the range of possible classes is 1.73.

Let us examine the way the class acceptability indices enrich the ROR outcomes for this particular problem. Obviously, the 14 countries that are necessarily assigned to a single class have the class CAI 100% and CAIs of other classes zero (see Fig. 1). For many alternatives that are possibly assigned to at least two consecutive classes, we can indicate a single recommendation suggested by the majority of compatible value functions (e.g., CAI(Fiji, $C _ { 1 } ) { = } 9 0 . 6 2 \% ,$ CAI(Indonesia, $C _ { 3 } ) = 8 0 . 0 7 \% ,$ CAI (Thailand, $C _ { 3 } ) = 6 9 . 4 1 \% ,$ , CAI(Cambodia, $C _ { 2 } ) = 6 5 . 4 \%$ . Note that since we used the example-based sorting procedure, the prevailing recommendation does not have to be precise (e.g., CAI(Nepal, $C _ { 1 } { - } C _ { 2 } ) =$ 64.32%, CAI(South Korea, $C _ { 3 ^ { - } } C _ { 4 } ) = 6 3 . 0 7 \% ,$ CAI(Papua New Guinea, $C _ { 2 } - C _ { 3 } ) = 5 0 . 0 5 \% )$ . For other countries, an analysis of CAIs allows narrowing down the range of most probable classes. For example, for 90% of the compatible value functions, Singapore is assigned to classes $C _ { 2 }$ and $C _ { 3 } ,$ whereas, in general, it could be placed in classes between $C _ { 1 }$ and $C _ { 4 } .$ Furthermore, for almost 99% of the compatible value functions, Pakistan is assigned to $C _ { 1 }$ and $C _ { 2 } ,$ whereas only 1% of the functions admit it to $C _ { 3 } .$ . An observation of the same type applies to Cambodia, Indonesia, and India. Such information could subsequently be used for an incremental speci<sup>fi</sup>cation of the assignment examples.

The analysis can be further enhanced by considering CuCAIs presented in Fig. 2 for a few exemplary countries. For example, Thailand and Indonesia are possibly assigned to $C _ { 3 }$ with 98% of the compatible value functions (resulting from their possible assignments to $C _ { 3 }$ and $\left[ C _ { 2 } , C _ { 3 } \right]$ or $C _ { 3 }$ and $[ C _ { 3 } , C _ { 4 } ] ,$ , respectively), whereas Cambodia and Indonesia are possibly assigned, respectively, to class $C _ { 2 }$ or $C _ { 1 }$ with 93% of the compatible value functions.

Possible assignments for the problem of assigning countries to different types of regimes.

<table><tr><td> $L_P-R_P$ </td><td>Nr of countries</td><td>Assigned countries</td></tr><tr><td> $C_4$ </td><td>3</td><td>New Zealand, Australia, Japan</td></tr><tr><td> $C_3-C_4$ </td><td>1</td><td>South Korea</td></tr><tr><td> $C_3$ </td><td>3</td><td>Taiwan, Timor Leste, Malaysia</td></tr><tr><td> $C_2-C_4$ </td><td>2</td><td>India, Indonesia</td></tr><tr><td> $C_2-C_3$ </td><td>3</td><td>Thailand, Papua New Guinea, Mongolia</td></tr><tr><td> $C_2$ </td><td>3</td><td>Hong Kong, Bangladesh, Bhutan</td></tr><tr><td> $C_1-C_4$ </td><td>1</td><td>Singapore</td></tr><tr><td> $C_1-C_3$ </td><td>3</td><td>Philippines, Cambodia, Pakistan</td></tr><tr><td> $C_1-C_2$ </td><td>3</td><td>Nepal, Fiji, Vietnam</td></tr><tr><td> $C_1$ </td><td>5</td><td>China, Afghanistan, Laos, Myanmar, North Korea</td></tr></table>

![](/api/attachments/4AVZW5J8/fulltext/images/a7ced819e82e10d005a112712d49d5511993f437c818b8e1add4cce1a2df50e4.jpg)  
Fig. 1. Class acceptability indices (in %) for the problem of assigning countries to different types of regimes

## 4.2. Assignment-based preference relations and outranking indices

A Hasse diagram of the necessary assignment-based preference relation is presented in Fig. 3. There are 306 ordered pairs of alternatives $( a , b ) { \in } A \times A \ ( a \neq b )$ related by the necessary assignment-based weak preference relation $\succsim \to , N$ , i.e. a is assigned to a class at least as good as b for all compatible value functions. Note that countries assigned to the same class with all compatible value functions (e.g., New Zealand, Australia, and Japan) are indifferent in terms of $\succsim \neg , N$ and thus they form a single node in Fig. 3. Note also that there are 268 ordered pairs of alternatives $( a , b ) \in A \times A \ ( \mathrm { e . g . }$ , (New Zealand, South Korea), (India, Nepal)) related by the strict necessary relation $\succsim \neg , N .$

When analyzing the most certain consequences of the preference information, it is obvious that New Zealand, Australia, and Japan, that are necessarily assigned to $C _ { 4 } ,$ should be perceived as the most democratic countries, i.e. they are necessarily preferred to the remaining alternatives. On the other hand, China, Afghanistan, Laos, Myanmar, and North Korea are necessarily assigned to $C _ { 1 }$ and can be considered to be the least democratic countries.

Let us discuss $\succsim \to , N$ for a few exemplary pairs of alternatives (a, $b ) \in { \cal A } \times { \cal A }$ in the context of their possible assignments. $\mathrm { I f } L _ { P } ( a ) > R _ { P } ( b )$

it is clear that a is assigned to a class better than b for all compatible value functions (e.g., (Australia, Thailand), (Indonesia, China)), and therefore $a \succ \ l ^ {  , N } b$ . Furthermore, if $L _ { P } ( a ) > L _ { P } ( b )$ and $R _ { P } ( a ) { < } R _ { P } ( b )$ (the worst possible class of a is better than the best class of b, while for their best classes the order is the inverse), neither $a \succsim \ l ^ { \ l , N } b$ nor $b \succsim \to , N _ { a }$ (e.g., (Singapore, Mongolia), (Pakistan, Bhutan)). Finally, if the best and the worst possible classes of a are at least as good as b with one of them being strictly better, we cannot be sure that a is assigned to a class at least as good as b for all compatible value functions. It is the case for some pairs of alternatives (e.g., (South Korea, Indonesia), (Taiwan, Papua New Guinea)), but other pairs (e.g., (Mongolia, Philippines), (Singapore, Nepal)) are incomparable in terms of c<sup>→,N</sup>.

If the intersection of the possible assignments for a pair of alternatives is empty, one of them is assigned to a class better than the other one for all compatible value functions. If not, it is useful to know the shares of compatible value functions con<sup>fi</sup>rming the possible assignment-based weak preference relation. The nodes corresponding to these countries are not related by an arc (neither directly nor when considering transitivity of the necessary relation) in Fig. 3.

To save space, we will skip comprehensive discussion of assignmentbased pair-wise outranking indices for the whole set of alternatives.

![](/api/attachments/4AVZW5J8/fulltext/images/52b228dfea141079784dac326949b66e08f55c172a5ed41e0c9c7a55fbea6e74.jpg)  
Fig. 2. Cumulative class acceptability indices (in %) for the subset of six countries.

![](/api/attachments/4AVZW5J8/fulltext/images/acffb4b44f2645bb5ba402e35432862894ce588479f70143269fdb5dbee5c303.jpg)  
Fig. 3. Hasse diagram of the necessary assignment-based preference relation. The relation is transitive and the arcs obtainable by the transitive closure are omitted

Instead, let us present APOIs for two signi<sup>fi</sup>cant subsets of alternatives, i.e. countries that can possibly be assigned to either $C _ { 4 }$ (Fig. 4) or to $C _ { 1 }$ (Fig. 5). When considering the nodes corresponding to a particular pair (a, b), we indicate with a smaller (greater) head of the arc alternative a (b) for which the result of the SMAA-based comparison is positive (negative) (i.e., APOI(a, b)>APOI(b, a)). The values of the indices are provided near the corresponding heads of the arc. In particular, for a pair (South Korea, India), APOI (South Korea, India)=93.34% and APOI (India, South Korea)=34.45%.

When comparing the subset of the most democratic countries (Fig. 4), the APOIs provide recommendations not following directly from the analysis of the possible assignments. For example, South Korea is never assigned to a class worse than Indonesia or Singapore (i.e., APOI(South Korea, Indonesia) and APOI(South Korea, Singapore)

are equal to 100%). Moreover, neither Indonesia nor Singapore is assigned to a range of classes at least as good as New Zealand, Australia, or Japan.

For the subset of the least democratic countries (see Fig. 5), it is clear that all countries are assigned to a class at least as good as China, Afghanistan, Laos, Myanmar, and North Korea, which are assigned necessarily and precisely to $C _ { 1 } .$ Singapore could be perceived as the most democratic among these countries since a majority of compatible value functions assign it to a better class than the others. Furthermore, Fiji could be viewed as one of the least democratic countries as for a majority of the considered countries the APOI(·, Fiji)>99%. Finally, let us note that for some pairs of alternatives, designating the more democratic country on the basis of APOIs is straightforward (e.g., (Singapore, Pakistan), (Philippines, Vietnam)), whereas for other pairs, such indication is ambiguous since their APOIs do not differ signi<sup>fi</sup>cantly (e.g., (Pakistan, Nepal), (Singapore, Philippines)).

![](/api/attachments/4AVZW5J8/fulltext/images/83af4f0927e379d494b0b34c0e654bca546997fe53673940a8a9deb559d6aa62.jpg)  
Fig. 4. Graph of the possible assignment-based preference relation enriched with the pair-wise outranking indices (in %) for alternatives that could be possibly assigned to class $C _ { 4 } .$

![](/api/attachments/4AVZW5J8/fulltext/images/95c8446d4949835f1dbf46940aef69e3fd7835bfe4e68ff3b1310696df7a70ef.jpg)  
Fig. 5. Graph of the possible assignment-based preference relation enriched with the pair-wise outranking indices (in %) for alternatives that could be possibly assigned to class $C _ { 1 } .$

## 4.3. Representative value function

The representative value function selected with the REPDIS procedure is presented in Fig. 6. The selected function may be explicitly presented along with the outcomes of stochastic ordinal regression to help the DM understand better both the assignment-based preference relation and the class acceptability indices. In such a way, the DM can easily assess relative importance of the criteria understood as a share of a given criterion in the comprehensive value. Furthermore, a representative value function may be used along with the provided assignment examples as an input for the example-based sorting procedure. The corresponding representative assignments (Table 2, column $C ^ { R E P } ( a ) )$ can be analyzed in the context of ROR and

![](/api/attachments/4AVZW5J8/fulltext/images/2027e26e2ea8b8f66c66816e7096bdd66c6f1ff0ea9f072fa26c4559dec67b52.jpg)

SMAA outcomes. This is useful because they are more precise than the possible assignments, more general than the necessary assignments, and often contain classes for which the CAIs are the greatest.

## 5. Conclusions

In this paper we presented a new approach for multiple criteria sorting problems. We considered a set of preference model instances compatible with assignment examples consisting of a reference alternative and its assignment to a contiguous set of classes. Depending on the type of sorting procedure applied, we referred to compatible value functions (the example-based procedure) or compatible pairs of value functions and class thresholds (the threshold-based procedure). Then, we determined the possible and necessary assignments with robust ordinal regression, and enriched the analysis with class acceptability indices adapted from Stochastic Multicriteria Acceptability Analysis (SMAA).

![](/api/attachments/4AVZW5J8/fulltext/images/e664e2829132ec9e2e0a97fbc821d9617a8ef231aa18f1219c142c19c2ba2070.jpg)

![](/api/attachments/4AVZW5J8/fulltext/images/32850f1e75f035b8706351814da75b2aa7cd606a908f2fa7b3ab3524a57d27ff.jpg)

![](/api/attachments/4AVZW5J8/fulltext/images/3daa3c876082f3279fb21e5a288d142c5eedcff248d5eb4dce2889c5356a2be6.jpg)

![](/api/attachments/4AVZW5J8/fulltext/images/9375e41dd407dd0abbba5f3be09e1ab7b8aac5316a85f0969784a3732696e69b.jpg)  
Fig. 6. Representative value function selected with the REPDIS procedure

We also introduced the notion of assignment-based weak preference relations. Analogously to the assignments, we established necessary and possible assignment-based relations, and estimated assignmentbased pair-wise outranking indices. We emphasized how the ordinal and stochastic analyses can bene<sup>fi</sup>t from a complementary use. Although not discussed in detail, results of the SMAA simulation process could additionally be used to support speci<sup>fi</sup>cation of the desired cardinalities of classes as presented in Ref. [13], making it possible to present to the DM, for example, the minimal, maximal, and average cardinalities of each class (or ranges of contiguous classes) in the sample of compatible preference model instances analyzed in SMAA.

Rejection sampling of the value functions for the model presented in Section 4 took less than 20 seconds with an R implementation and a standard desktop PC. However, the rejection rate grows exponentially with the number of criteria and polynomially with the amount of assignment examples, and becomes infeasible already with a moderate amount of criteria (≥10, see Ref. [23]). Future research should investigate application of pseudo polynomial-time Markov Chain Monte Carlo algorithms, similarly to [23], for sampling the value functions used in estimation of the stochastic indices.

## Acknowledgments

The authors thank the three anonymous reviewers whose comments helped to improve previous versions of the paper. The <sup>fi</sup>rst author wishes to acknowledge <sup>fi</sup>nancial support from the Poznan University of Technology, grant no. 91-516/DS-MLODA KADRA.

## Appendix A. Supplementary data

Supplementary data to this article can be found online at http://dx. doi.org/10.1016/j.dss.2012.12.030.

## References

[1] S. Damart, L.C. Dias, V. Mousseau, Supporting groups in sorting decisions: methodology and use of a multi-criteria aggregation/disaggregation DSS Decision Support Systems 43 (4) (2007) 1464–1475, http://dx.doi.org/10.1016/j.dss.2006.06.002.

[2] L. Dias, V. Mousseau, J. Figueira, J. Clímaco, An aggregation/disaggregation approach to obtain robust conclusions with ELECTRE TRI, European Journal of Operational Research 138 (2) (2002) 332–348, http://dx.doi.org/10.1016/S0377-2217(01)00250-8.

[3] M. Doumpos, C. Zopounidis, A multicriteria decision support system for bank rating, Decision Support Systems 50 (1) (2010) 55–63, http://dx.doi.org/10.1016/j.dss. 2010.07.002.

[4] EIU, Democracy index 2010, Democracy in Retreat, Economist Intelligence Unit, London, 2010

[5] S. Greco, V. Mousseau, R. Słowiński, Ordinal regression revisited: multiple criteria ranking using a set of additive value functions, European Journal of Operational Research 191 (2) (2008) 415–435, http://dx.doi.org/10.1016/j.ejor.2007.08.013.

[6] S. Greco, V. Mousseau, R. Słowiński, Multiple criteria sorting with a set of additive value functions, European Journal of Operational Research 207 (4) (2010) 1455–1470, http://dx.doi.org/10.1016/j.ejor.2010.05.021.

[7] S. Greco, M. Kadziński, V. Mousseau, R. Słowiński, ELECTRE<sup>GKMS</sup>: robust ordinal regression for outranking methods, European Journal of Operational Research 214 (1) (2011) 118–135, http://dx.doi.org/10.1016/j.ejor.2011.03.045.

[8] S. Greco, M. Kadziński, R. Słowiński, Selection of a representative value function in robust multiple criteria sorting, Computers and Operations Research 38 (11) (2011) 1620–1637, http://dx.doi.org/10.1016/j.cor.2011.02.003.

[9] S. Greco, M. Kadziński, V. Mousseau, R. Słowiński, Robust ordinal regression for multiple criteria group decision problems: UTA<sup>GMS</sup>-GROUP and UTADIS<sup>GMS</sup>-GROUP, Decision Support Systems 52 (3) (2012) 549–561, http://dx.doi.org/10.1016/j.dss.2011.10.005.

[10] E. Jacquet-Lagrèze, Y. Siskos, Assessing a set of additive utility functions for multicriteria decision making: the UTA method, European Journal of Operational Research 10 (1982) 151–164, http://dx.doi.org/10.1016/0377-2217(82)90155-2.

[11] M. Kadziński, S. Greco, R. Słowiński, Selection of a representative value function in robust multiple criteria ranking and choice, European Journal of Operational Research 217 (3) (2012) 541–553, http://dx.doi.org/10.1016/j.ejor.2011.09.032.

[12] M. Kadziński, S. Greco, R. Słowiński, Selection of a representative value function for robust ordinal regression in group decision making, Group Decision and Negotiation (to appear), http://dx.doi.org/10.1007/s10726-011-9277-z

[13] M. Kadziński, R. Słowiński, DIS-CARD: a new method of multiple criteria sorting to classes with desired cardinality, Journal of Global Optimization (to appear). http://dx.doi.org/10.1007/s10898-012-9945-9.

[14] M. Köksalan, S. Bilgin Özpeynirci, An interactive sorting method for additive utility functions, Computers and Operations Research 36 (9) (2009) 2565–2572, http://dx.doi.org/10.1016/j.cor.2008.11.006.

[15] J. Li, L. Wei, G. Li, W. Xu, An evolution strategy-based multiple kernels multi-criteria programming approach: the case of credit decision making, Decision Support Systems 51 (2) (2011) 292–298, http://dx.doi.org/10.1016/j.dss.2010.11.022.

[16] V. Mousseau, R. Słowiński, Inferring an ELECTRE TRI model from assignment examples, Journal of Global Optimization 12 (2) (1998) 157–174, http://dx.doi.org/10.1023/A: 1008210427517.

[17] V. Mousseau, R. Słowiński, P. Zielniewicz, A user-oriented implementation of the ELECTRE TRI method integrating preference elicitation support, Computers and Operations Research 27 (7–8) (2000) 757–777, http://dx.doi.org/10.1016/ S0305-0548(99)00117-3.

[18] A. Ngo The, V. Mousseau, Using assignment examples to infer category limits for the ELECTRE TRI method, Journal of Multi-Criteria Decision Analysis 11 (1) (2002) 29–43, http://dx.doi.org/10.1002/mcda.314.

[19] Y. Siskos, A way to deal with fuzzy preferences in multicriteria decision problems, European Journal of Operational Research 10 (3) (1982) 314–324, http://dx.doi.org/ 10.1016/0377-2217(82)90230-2

[20] T. Tervonen, J. Figueira, A survey on stochastic multicriteria acceptability analysis methods, Journal of Multi-Criteria Decision Analysis 15 (1–2) (2008) 1–14, http://dx.doi.org/10.1002/mcda.407

[21] T. Tervonen, R. Lahdelma, Implementing stochastic multicriteria acceptability analysis, European Journal of Operational Research 178 (2) (2007) 500–513, http://dx.doi.org/10.1016/j.ejor.2005.12.037.

[22] T. Tervonen, J. Figueira, R. Lahdelma, J. Almeida Dias, P. Salminen, A stochastic method for robustness analysis in sorting problems, European Journal of Operational Research 192 (1) (2009) 236–242, http://dx.doi.org/10.1016/j.ejor.2007.09.008.

[23] T. Tervonen, G. van Valkenhoef, N. Baştürk, D. Postmus, Hit-and-run enables ef<sup>fi</sup>cient weight generation for simulation-based multiple criteria decision analysis, European Journal of Operational Research 224 (3) (2013) 552–559, http://dx.doi.org/10.1016/j.ejor.2012.08.026.

[24] C. Zopounidis, M. Doumpos, PREFDIS: a multicriteria decision support system for sorting decision problems, Computers and Operations Research 27 (7–8) (2000) 779–797, http://dx.doi.org/10.1016/S0305-0548(99)00118-5.

[25] C. Zopounidis, M. Doumpos, Multicriteria classi<sup>fi</sup>cation and sorting methods: a literature review, European Journal of Operational Research 138 (2002) 229–246, http://dx.doi.org/10.1016/S0377-2217(01)00243-0.

Miłosz Kadziński is an Assistant Professor at the Poznan University of Technology, member of the Laboratory of Intelligent Decision Support Systems (IDSS) within the Institute of Computing Science. He received his M.Sc, in Computer Science (2008) from Poznan University of Technology and defended his PhD thesis in 2012. His main research interests are in Multiple Criteria Decision Analysis (particularly in robust ordinal regression and multiple objective optimization cone contraction methods), text processing, and exploratory data analysis. His works have been published in journals such as EJOR, Computers & OR, Omega, DSS, GDN, JOGO, and IJITDM.

Tommi Tervonen is an Assistant Professor at the Econometric Institute of Erasmus University Rotterdam. He received a double-degree PhD in 2007 from the Universities of Turku (Computer Science) and Coimbra (Management Science). His main research interests are theory of MCDA (especially SMAA methods), MCDA in drug bene<sup>fi</sup>t-risk analysis, and medical informatics. His research has appeared in journals such as EJOR, Omega, DSS, Statistics in Medicine, Journal of Clinical Epidemiology, Statistics and Computing, Information and Software Technology, Journal of MCDA, and Journal of Nanoparticle Research.
