---
otero_id: 15480
otero_key: "8C5GBT6Y"
title: "Dominance-based rough set approach for groups in multicriteria classification problems"
authors: "Salem Chakhar; Inès Saad"
year: "2012"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2012.05.050"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Dominance-based rough set approach for groups in multicriteria classi<sup>fi</sup>cation problems

Salem Chakhar <sup>a,</sup>⁎, Inès Saad <sup>b,c,1</sup>

<sup>a</sup> Centre for Research in Regional Planning and Development, University of Laval, Félix Antoine Savard, Québec City, Québec Canada G1K 7P4

<sup>b</sup> Amiens Business School, 18, Place Saint-Michel, 80038 Amiens, France

<sup>c</sup> MIS, University of Picardie Jules Verne, 33 Rue Saint Leu, 80039 Amiens, France

## a r t i c l e i n f o

Article history: Received 5 May 2010 Received in revised form 20 May 2012 Accepted 29 May 2012 Available online 7 June 2012

Keywords: Group decision-making Multicriteria classi<sup>fi</sup>cation Rough sets theory DRSA Aggregation Decision rule

## a b s t r a c t

The paper proposes a two-phase methodology to support groups in multicriteria classi<sup>fi</sup>cation problems. The <sup>fi</sup>rst phase, which relies on a dominance-based rough set approach (DRSA), takes a set of assignment examples as input and outputs a set of collective decision rules, representing a generalized description of the decision makers preference information. The second phase then applies these collective decision rules to classify all decision objects. The methodology uses “if … then …” aggregation rules that coherently implement the majority principle and veto effect. The aggregation rules thus allow obtaining consensual decisions. Furthermore, the contribution of each decision maker to the collective decision is objectively measured by the quality of individual classi<sup>fi</sup>cation conducted by this decision maker during the <sup>fi</sup>rst phase. The methodology has been validated by developing a prototype and applied to a nuclear risk management decision problem.

© 2012 Elsevier B.V. All rights reserved.

## 1. Introduction

Multicriteria analysis has been successfully applied in different domains, and different methods have been proposed and used to handle many real-world decision problems. Most methods “assume a single decision maker for simplicity” [27], while real-world decision problems naturally imply multiple decision makers with con<sup>fl</sup>icting objectives and distinct value systems. Several authors have recognized the need for group multicriteria decision-making methods [1,23], and the literature has proposed different methods [19,24,25,28]. As some authors have indicated [9,21], most research on group multicriteria decisionmaking considers choice [7,11,13,20] or ranking [2,5,8] problems rather than classi<sup>fi</sup>cation. An interesting exception is the InteliTeam framework [6] that includes several multicriteria methods which can address sorting, ranking, and choice problems, thus implying multiple decision makers. In [18], the authors introduce two new methods for multiple criteria group ranking and sorting problems. These methods use a set of additive value functions as a preference model. The recently proposed methods and decision support systems for group multicriteria classi<sup>fi</sup>cation problems [9,10,17,18,21,33] offer a partial solution to this situation. Further research on group multicriteria classi<sup>fi</sup>cation is still needed, as advocated by several authors [9,17,21] and con<sup>fi</sup>rmed by real-world decision problems in which the authors of this study intervened [26,34].

The primary aim of this paper is to propose a methodology to support groups in multicriteria classi<sup>fi</sup>cation decision-making. The methodology assumes the existence of a mediator who acts as a third-party member to structure meetings and reach a <sup>fi</sup>nal decision based on the facts brought up during the discussions. The proposed methodology has two phases: (i) constructing a collective preference model and (ii) exploiting this model to support decision-making. The <sup>fi</sup>rst phase, which is based on the dominance-based rough set approach (DRSA) [16], takes a set of assignment examples as input and outputs a set of collective decision rules, representing a generalized description of the decision makers' preference information. The second phase exploits the collective decision rules to classify all decision objects.

A prototype supporting the methodology has been developed. This prototype is loosely coupled with the existing software called 4eMka2 (available at http://idss.cs.put.poznan.pl), which implements the DRSA. The 4eMka2 software assumes a single decision maker and thus cannot support the proposed methodology.

Two major issues should be addressed in group decision-making. The <sup>fi</sup>rst issue, whose importance has been addressed in previous research [2,8,20,21], concerns de<sup>fi</sup>ning appropriate techniques to combine individual preferences. In this paper, we design a set of “if … then …” aggregation rules that coherently implement the majority principle and veto effect, thus allowing us to obtain consensual decisions. The second issue is de<sup>fi</sup>ning suitable tools that consider that decision makers generally have different “powers” or “weights”, as recognized by different authors [8,20–22,31]. In the proposed methodology, the contribution of each decision maker in the collective decision is measured by the quality of individual classi<sup>fi</sup>cation conducted by this decision maker. Generally, more experimented decision makers obtain a higher classi<sup>fi</sup>cation quality. This has been con<sup>fi</sup>rmed in different real-world decision problems [26,32–34]. This leads to more “democratic” decisions, because decision makers are only discriminated based on their classi<sup>fi</sup>cation quality and not their hierarchical levels.

The methodology proposed in this work was experimentally implemented in real-world project supervised by the IRSN (French Institute for Radioprotection and Nuclear Safety). The project, designed by PRIME (French acronym for “Research Project on radioecology sensibility Indicators and Multicriteria methods applied to the Environment of an industrial territory”) concerns managing post-accident nuclear risk in the southern region of France. The objective of PRIME is to characterize districts in the study area and classify them according to their vulnerability in a nuclear accident event using a six-level risk scale. This project involved several actors, including the IRSN and other risk expert institutions, representatives of public authorities and representatives of local information commissions. The present work only considers three decision makers. For anonymity, these decision makers are called CM, PP and CAL in this paper. This decision problem is used throughout the paper to illustrate the proposed methodology. The methodology is generic enough such that it may be applied with no modi<sup>fi</sup>cation to other group multicriteria classi<sup>fi</sup>cation problems.

The present work is organized as follows. Section 2 sets the background. Section 3 presents the general methodology schema. Section 4 details the aggregation procedure, which is used in the <sup>fi</sup>rst phase of the methodology. Section 5 presents a nuclear risk management case study. Section 6 discusses some related work. Section 7 concludes the paper.

## 2. Background

Previous research has proposed the DRSA [15,16] to overcome the shortcomings of conventional rough sets theory [29,30] in multicriteria classi<sup>fi</sup>cation. The basic idea of DRSA is to replace the indiscernibility relation used in classical rough sets theory with the dominance relation, which is more appropriate for multicriteria decision-making.

## 2.1. Basic concepts

In rough sets theory, information regarding the decision objects is often structured in a 4-tuple information table $\pmb { S } = \langle U , \ Q \ V , f \rangle ,$ where U is a non-empty <sup>fi</sup>nite set of objects and Q is a non-empty <sup>fi</sup>nite set of attributes such that $q { : } U { \to } V _ { q }$ for every $q \in Q , V _ { q }$ is the domain of attribute q. $V = \cap _ { q \in Q } V _ { q } ,$ and $f \colon U \times Q \to V$ is the information function de<sup>fi</sup>ned such that $f ( x , \ q ) \in V _ { q }$ for each attribute q and object x U. Q is often divided into a sub-set $C \neq \emptyset$ of condition attributes and a sub-set $D \neq \emptyset$ of decision attributes such that $C \cup D { = } Q$ and $C \cap D = \emptyset$ . In this case, S is called a decision table.

Example 1. Table 1 gives the decision table used in this paper. The obiect set $U = \{ x _ { k } { : } k = 1 , 2 , . . . , 1 8 \}$ contains eighteen objects (districts) that have been selected from the study area. Each district is described using seven condition attributes $C = \{ A _ { 1 } , \ A _ { 2 } , . . . , A _ { 7 } \}$ } and three decision attributes $D = \{ E _ { 1 } , ~ E _ { 2 } , ~ E _ { 3 } \}$ . Table 1 also gives the evaluations of selected districts for all attributes. The values of attributes $A _ { 1 }$ through $A _ { 7 }$ correspond to the partial $( \mathrm { i . e . , }$ , for a single attribute) vulnerability levels associated with each condition attribute. The values of decision attributes $E _ { 1 }$ $E _ { 2 }$ and $E _ { 3 }$ correspond to the global vulnerability levels speci<sup>fi</sup>ed by decision makers CM, PP and CAL, respectively.

Table 1 Decision table.

<table><tr><td>Object</td><td> $A_1$ </td><td> $A_2$ </td><td> $A_3$ </td><td> $A_4$ </td><td> $A_5$ </td><td> $A_6$ </td><td> $A_7$ </td><td> $E_1$ </td><td> $E_2$ </td><td> $E_3$ </td></tr><tr><td> $x_1$ </td><td>4</td><td>5</td><td>5</td><td>5</td><td>4</td><td>1</td><td>1</td><td>4</td><td>4</td><td>5</td></tr><tr><td> $x_2$ </td><td>4</td><td>5</td><td>5</td><td>5</td><td>4</td><td>2</td><td>2</td><td>4</td><td>4</td><td>5</td></tr><tr><td> $x_3$ </td><td>4</td><td>5</td><td>5</td><td>5</td><td>4</td><td>2</td><td>1</td><td>4</td><td>4</td><td>5</td></tr><tr><td> $x_4$ </td><td>4</td><td>5</td><td>5</td><td>5</td><td>4</td><td>3</td><td>1</td><td>5</td><td>4</td><td>5</td></tr><tr><td> $x_5$ </td><td>3</td><td>2</td><td>2</td><td>4</td><td>4</td><td>2</td><td>0</td><td>3</td><td>2</td><td>3</td></tr><tr><td> $x_6$ </td><td>1</td><td>1</td><td>1</td><td>2</td><td>4</td><td>1</td><td>0</td><td>0</td><td>0</td><td>1</td></tr><tr><td> $x_7$ </td><td>2</td><td>2</td><td>1</td><td>2</td><td>4</td><td>1</td><td>0</td><td>3</td><td>2</td><td>2</td></tr><tr><td> $x_8$ </td><td>1</td><td>2</td><td>1</td><td>2</td><td>2</td><td>1</td><td>0</td><td>0</td><td>0</td><td>1</td></tr><tr><td> $x_9$ </td><td>3</td><td>2</td><td>2</td><td>4</td><td>4</td><td>2</td><td>0</td><td>3</td><td>2</td><td>2</td></tr><tr><td> $x_{10}$ </td><td>3</td><td>3</td><td>3</td><td>4</td><td>4</td><td>1</td><td>0</td><td>3</td><td>2</td><td>3</td></tr><tr><td> $x_{11}$ </td><td>3</td><td>3</td><td>3</td><td>4</td><td>4</td><td>1</td><td>0</td><td>3</td><td>2</td><td>3</td></tr><tr><td> $x_{12}$ </td><td>3</td><td>3</td><td>2</td><td>4</td><td>4</td><td>1</td><td>0</td><td>3</td><td>2</td><td>3</td></tr><tr><td> $x_{13}$ </td><td>3</td><td>2</td><td>2</td><td>4</td><td>4</td><td>1</td><td>0</td><td>2</td><td>2</td><td>3</td></tr><tr><td> $x_{14}$ </td><td>2</td><td>2</td><td>2</td><td>4</td><td>4</td><td>1</td><td>0</td><td>2</td><td>1</td><td>2</td></tr><tr><td> $x_{15}$ </td><td>2</td><td>2</td><td>1</td><td>4</td><td>3</td><td>1</td><td>0</td><td>2</td><td>1</td><td>2</td></tr><tr><td> $x_{16}$ </td><td>2</td><td>2</td><td>1</td><td>4</td><td>4</td><td>1</td><td>0</td><td>2</td><td>1</td><td>2</td></tr><tr><td> $x_{17}$ </td><td>1</td><td>1</td><td>1</td><td>2</td><td>4</td><td>1</td><td>0</td><td>3</td><td>3</td><td>4</td></tr><tr><td> $x_{18}$ </td><td>1</td><td>1</td><td>0</td><td>1</td><td>4</td><td>1</td><td>0</td><td>3</td><td>3</td><td>3</td></tr></table>

2.2. Presenting a dominance-based rough set approach for a single decision maker

In multicriteria decision-making, the domain (or scale) of condition attributes should be ordered according to decreasing or increasing preference. Such attributes are called criteria. DRSA proponents assume that the preference increases with a value of ${ \dot { \boldsymbol { f } } } ( \cdot , \ q )$ for every $q \in C .$ . We also assume that the decision attribute set $D = \{ d \}$ is a singleton. The unique decision attribute d partitions U into a <sup>fi</sup>nite number of decision classes $\mathbf { C l } = \{ C l _ { t } , ~ t \in T \} , ~ T = \{ 0 , . . . , ~ n \} ,$ , such that each $x { \in } U$ belongs to one and only one class. Furthermore, we suppose that the classes are preference-ordered, i.e., for all $r , \ s { \in } T$ such that $r > s ,$ objects from $C l _ { r }$ are preferred to objects from $C l _ { s } .$

## 2.2.1. Dominance relation

Let $P \subseteq C$ be a subset of condition attributes. The dominance relation $\Delta _ { P }$ <sup></sup>associated with P is de<sup>fi</sup>ned for each pair of objects x and y thus:

$$
x \Delta_ {P} y \Longleftrightarrow f (x, q) \succcurlyeq f (y, q), \forall q \in P.
$$

In the above de<sup>fi</sup>nition, the symbol $\ " \succcurlyeq \ "$ should be replaced with $" \leqslant "$ for criteria that are ordered according to decreasing preferences. We associate two sets with each object x∈U: (i) the P-dominating set Δ<sup>+</sup> $\left( x \right) = \left\{ y \in U : y \varDelta _ { P } x \right\}$ containing objects that dominate x and (ii) the P-dominated set $\Delta _ { P } ^ { - } ( x ) = \{ y \in U { : } x \Delta _ { P } y \}$ containing objects dominated by x. These sets are used to approximate decision classes.

Example 2. Consider Table 1 and suppose that $U { = } \{ x _ { 1 } , ~ x _ { 2 } , ~ x _ { 3 } , ~ x _ { 4 } , ~ x _ { 5 } \}$ and $P { = } \{ A _ { 2 } , A _ { 5 } , A _ { 6 } \}$ . All condition attributes are ordered according to decreasing preferences. Consider objects $x _ { 1 }$ and $x _ { 4 } .$ . Based on this information, it is easy to establish that $x _ { 1 }$ dominates objects $x _ { 2 } , x _ { 3 }$ and $x _ { 4 } ,$ because $f ( x _ { 1 } , ~ A _ { j } ) \preccurlyeq f ( x _ { k } , ~ A _ { j } ) , k = 2 , ~ 3 , ~ 4 ; ~ j = 2 , ~ 5 , ~ 6$ . In turn, there is no dominance relationship between objects x and $x _ { 5 } ,$ because the evaluation of $x _ { 1 }$ is better than the one of $\dot { \boldsymbol { x } } _ { 5 }$ on attribute $A _ { 6 }$ but the evaluation of $x _ { 5 }$ is better than that of x on attribute $A _ { 1 }$ . Objec $x _ { 4 }$ is clearly dominated by all objects in $U ,$ as $f ( x _ { 4 } , \ A _ { j } ) \succcurlyeq f ( x _ { k } , \ A _ { j } ) , \ k = 1 , \ 2 , \ 3 , \ 5 ; \ j = 2 , \ 5 , \ 6 .$ Table 2 summarizes the P-dominating and P-dominated sets associated with objects $x _ { 1 } , x _ { 2 } , x _ { 3 } ,$ x and $x _ { 5 } .$

## 2.2.2. Approximating upward and downward class unions

In DRSA, the represented knowledge is a collection of upward unions $C l _ { t } ^ { \geq }$ and downward unions $C l _ { t } ^ { \le }$ of classes de<sup>fi</sup>ned thus:

$$
C l _ {t} ^ {\geq} = \cup_ {s \geq t} C l _ {s},   C l _ {t} ^ {\leq} = \cup_ {s \leq t} C l _ {s}.
$$

Table 3  
Table 2  
P-dominating and P-dominated sets.

<table><tr><td>Object</td><td>P-dominating set</td><td>P-dominated set</td></tr><tr><td> $x_{1}$ </td><td> $\Delta_{\bar{p}}^{+}(x_{1})=\{x_{1}\}$ </td><td> $\Delta_{\bar{P}}^{-}(x_{1})=\{x_{1}, x_{2}, x_{3}, x_{4}\}$ </td></tr><tr><td> $x_{2}$ </td><td> $\Delta_{\bar{p}}^{+}(x_{2})=\{x_{1}, x_{2}, x_{3}, x_{5}\}$ </td><td> $\Delta_{\bar{P}}^{-}(x_{2})=\{x_{2}, x_{3}, x_{4}\}$ </td></tr><tr><td> $x_{3}$ </td><td> $\Delta_{\bar{p}}^{+}(x_{3})=\{x_{1}, x_{2}, x_{3}, x_{5}\}$ </td><td> $\Delta_{\bar{P}}^{-}(x_{3})=\{x_{2}, x_{3}, x_{4}\}$ </td></tr><tr><td> $x_{4}$ </td><td> $\Delta_{\bar{p}}^{+}(x_{4})=\{x_{1}, x_{2}, x_{3}, x_{4}, x_{5}\}$ </td><td> $\Delta_{\bar{P}}^{-}(x_{4})=\{x_{4}\}$ </td></tr><tr><td> $x_{5}$ </td><td> $\Delta_{\bar{p}}^{+}(x_{5})=\{x_{5}\}$ </td><td> $\Delta_{\bar{P}}^{-}(x_{5})=\{x_{2}, x_{3}, x_{4}, x_{5}\}$ </td></tr></table>

The assertion $" x \in C l _ { t } ^ { \geq } { } ^ { \prime }$ means that $" x$ belongs to at least class ${ C l } _ { t } ^ { \prime \prime } .$ while $" x \in C l _ { t } ^ { \leq n }$ means that “x belongs to at most class ${ C l } _ { t } ^ { \dag } .$ . The P-lower and P-upper Cl<sub>t</sub><sup>≥</sup> approximations with respect to $P \subseteq C ,$ respectively denoted $\overline { { \underline { P } } } \left( C l _ { t } ^ { \geq } \right)$ and $\bar { P } \left( C l _ { t } ^ { \geq } \right)$ , are de<sup>fi</sup>ned thus:

$$
\begin{array}{l} \bullet \underline {{P}} \left(C l _ {t} ^ {\geq}\right) = \left\{x \in U: \Delta_ {P} ^ {+} (x) C l _ {t} ^ {\geq} \right\}, \\ \bullet \bar {P} \left(C l _ {t} ^ {\geq}\right) = \cup_ {x \in C l _ {t} ^ {\geq}} \Delta_ {P} ^ {+} (x) = \left\{x \in U: \Delta_ {P} ^ {-} (x) \cap C l _ {t} ^ {\geq} \neq \emptyset \right\}. \end{array}
$$

Analogously, the P-lower and P-upper Cl<sup>≤</sup> approximations with respect to $P \subseteq C ,$ respectively denoted $\left( P \left( C l _ { t } ^ { \leq } \right) \right.$ and $\hat { P } \left( C l _ { t } ^ { \le } \right)$ , are de-<sup>fi</sup>ned thus:

$$
\begin{array}{l} \bullet \underline {{P}} \Big (C l _ {t} ^ {\leq} \Big) = \Big \{x \in U: \Delta_ {P} ^ {-} (x) C l _ {t} ^ {\leq} \Big \}, \\ \bullet \bar {P} \Big (C l _ {t} ^ {\leq} \Big) = \cup_ {x \in C l _ {t} ^ {\leq}} \Delta_ {P} ^ {-} (x) = \Big \{x \in U: \Delta_ {P} ^ {+} (x) \cap C l _ {t} ^ {\leq} \neq \emptyset \Big \}. \end{array}
$$

The P-lower approximation of $C l _ { t } ^ { \geq } \left( \mathrm { r e s p . } C l _ { t } ^ { \leq } \right)$ that contains all objects with P-dominating (resp. P-dominated) set is assigned with certainty to classes that are at most as good as $C l _ { t } .$ The P-upper approximation of $C l _ { t } ^ { \geq }$ (resp. Cl<sup>≤</sup>) that contains all objects with $P -$ dominating (resp. P-dominated) set is assigned to a class at least as good as $C l _ { t } .$

The P-boundaries (or P-doubtful region) of $C l _ { t } ^ { \geq }$ and $C l _ { t } ^ { \le }$ are:

$$
\begin{array}{l} \bullet B n _ {P} \Big (C l _ {t} ^ {\geq} \Big) = \bar {P} \Big (C l _ {t} ^ {\geq} \Big) - \underline {{P}} \Big (C l _ {t} ^ {\geq} \Big), \\ \bullet B n _ {P} \Big (C l _ {t} ^ {\leq} \Big) = \bar {P} \Big (C l _ {t} ^ {\leq} \Big) - \underline {{P}} \Big (C l _ {t} ^ {\leq} \Big). \end{array}
$$

The boundaries group objects that can be ruled neither in nor out as members of class $C l _ { t }$

Example 3. Consider Table 1 and suppose that $U { = } \{ x _ { 1 } , ~ x _ { 2 } , ~ x _ { 3 } , ~ x _ { 4 } , ~ x _ { 5 } \}$ and $P = \{ A _ { 2 } , A _ { 5 } , A _ { 6 } \}$ . Assume that the decision attribute domain $E _ { 1 }$ is $\{ 3 , ~ 4 , ~ 5 \}$ . For decision attribute $E _ { 1 } ,$ objects in U are divided into three preference-ordered classes: $C l _ { 3 } = \{ 3 \} , C l _ { 4 } = \{ 4 \} ,$ , and $C l _ { 5 } = \{ 5 \}$ . Thus, the class unions that should be approximated are:

$C l _ { 3 } ^ { \leq } , \mathsf { i . e . }$ , the class of districts with (at most) “moderate risk”,

$C l _ { 4 } ^ { \leq } , \mathrm { i . e . , }$ the class of districts with at most “major risk”,

$C l _ { 4 } ^ { \geq } , \mathrm { i . e . }$ , the class of districts with at least “major risk”,

$C l _ { 5 } ^ { \geq } , \mathrm { i . e . }$ ., the class of districts with (at least) “major and long-lasting $\mathrm { r i } s \mathrm { k } ^ { \prime \prime }$

Lower and upper approximations and boundary regions.

<table><tr><td>Lower approximations</td><td>Upper approximations</td><td>Boundary</td></tr><tr><td> $\underline{P}\left(Cl_{3}^{\leq}\right)=\varnothing$ </td><td> $\overline{P}\left(Cl_{3}^{\leq}\right)=\{x_{2}, x_{3}, x_{4}, x_{5}\}$ </td><td> $Bn_{P}(Cl_{3}^{\leq})=\{x_{2}, x_{3}, x_{4}, x_{5}\}$ </td></tr><tr><td> $\underline{P}\left(Cl_{4}^{\leq}\right)=\varnothing$ </td><td> $\overline{P}\left(Cl_{4}^{\leq}\right)=\{x_{1}, x_{2}, x_{3}, x_{4}, x_{5}\}$ </td><td> $Bn_{P}(Cl_{4}^{\leq})=\{x_{1}, x_{2}, x_{3}, x_{4}, x_{5}\}$ </td></tr><tr><td> $\underline{P}\left(Cl_{4}^{\geq}\right)=\{x_{1}\}$ </td><td> $\overline{P}\left(Cl_{4}^{\geq}\right)=\{x_{1}, x_{2}, x_{3}, x_{4}, x_{5}\}$ </td><td> $Bn_{P}(Cl_{4}^{\geq})=\{x_{2}, x_{3}, x_{4}, x_{5}\}$ </td></tr><tr><td> $\underline{P}\left(Cl_{5}^{\geq}\right)=\varnothing$ </td><td> $\overline{P}\left(Cl_{5}^{\geq}\right)=\{x_{1}, x_{2}, x_{3}, x_{4}, x_{5}\}$ </td><td> $Bn_{P}(Cl_{5}^{\geq})=\{x_{1}, x_{2}, x_{3}, x_{4}, x_{5}\}$ </td></tr></table>

Table 3 gives the lower and upper approximations and boundary regions associated with these classes, i.e., computing $\underline { { P } } \left( C l _ { 4 } ^ { \geq } \right)$ . According to the above de<sup>fi</sup>nition, we have $\underline { { P } } \left( C l _ { 4 } ^ { \geq } \right) = \left\{ x { \in } U : \Delta _ { P } ^ { + } ( x ) C l _ { 4 } ^ { \geq } \right\}$ . Based on Table 1, we obtain $C l _ { 4 } ^ { \geq } = \{ x _ { 1 } , \ x _ { 2 } , \ x _ { 3 } , \ x _ { 4 } \}$ . Using the $P -$ dominating sets given in Table $\begin{array} { r l } { 2 , \ } & { { } \Delta _ { P } ^ { + } ( x _ { 1 } ) = \{ x _ { 1 } \} \ C l _ { 4 } ^ { \geq } } \end{array}$ and $\Delta _ { P } ^ { + } ( x _ { k } ) ~ C l _ { 4 } ^ { \geq } ,$ $k = 2 , 3 , 4 , 5 .$ . Consequently, the lower approximation of $C l _ { 4 } ^ { \geq }$ is $P \left( C l _ { 4 } ^ { \geq } \right) = \{ x _ { 1 } \}$

## 2.2.3. Quality of classification

The following ratio measures the classi<sup>fi</sup>cation quality of a partition Cl using a criteria set P:

$$
\gamma_ {P} (\mathbf {C l}) = \frac {\left| U - \left(\left(\cup_ {t \in T} B n _ {P} \left(C l _ {t} ^ {\geq}\right)\right) \cup \left(\cup_ {t \in T} B n _ {P} \left(C l _ {t} ^ {\leq}\right)\right)\right) \right|}{| U |}.\tag{1}
$$

It expresses the ratio of all P-correctly classi<sup>fi</sup>ed objects to all objects in the system

## 2.3. Decision rules

Decision attributes induce a partition of U that is independent of condition attributes. Accordingly, a decision table may be observed as a set $0 \mathrm { f } ^ { \mathrm { ~ \tiny ~ w } } \mathrm { i f } \ldots$ then $\cdots ^ { \dag }$ decision rules, where the condition part speci<sup>fi</sup>es values assumed by one or more condition attributes and the decision part speci<sup>fi</sup>es an assignment to one or more decision classes. Three types of decision rules may be considered in DRSA: (i) certain rules generated from lower approximations of class unions, (ii) possible rules generated from upper approximations of class unions and (iii) approximate rules generated from boundary regions.

An object x ∈U supports a decision rule if its description matches both the condition and decision parts of the rule. A decision rule covers object x if the description of x matches at least the condition part of the rule. Each decision rule is characterized by its strength, which is the number of objects that support this rule. If the consequence is univocal (i.e., contains only one decision), the rule is exact; otherwise, it is approximate.

## 3. Methodology

The methodology has two phases (Fig. 1): (i) constructing a collective preference model, and (ii) exploiting collective decision rules. The <sup>fi</sup>rst phase takes a set of assignment examples as input and outputs a set of collective decision rules generalizing the decision makers' preference information. The second phase is devoted exploiting the collective decision rules to classify all decision objects. Both phases are described below.

![](/api/attachments/8C5GBT6Y/fulltext/images/22a555018ba7787388c25f6e0013103db05d57d68f19bac62b8db989d74c755d.jpg)  
Fig. 1. General methodology schema

First, we introduce some new notations. Let $H = \{ 1 , . . . , i , . . . , h \}$ with $h \geq 2$ be a <sup>fi</sup>nite decision maker set and $\mathbf { I } = \langle U , \mathcal { Q } , V , f \rangle$ be a common information table for all decision makers. Let $E _ { 1 } , . . . , E _ { i } , . . . , E _ { h }$ be h decision attributes de<sup>fi</sup>ned in the same domain and associated with decision makers in H. We suppose that each decision maker $i { \in } H$ has a preference order for U represented by a <sup>fi</sup>nite set of preference-ordered classes $\mathbf { C l } _ { i } = \{ C l _ { t , ~ i } , \ t \in T _ { i } \} , \ T _ { i } = \{ 0 , . . . , \ n _ { i } \} ,$ , such that $\cup _ { t = 1 } ^ { n _ { i } } C l _ { t , ~ i } = U ,$ ${ C l } _ { t , \ i } \cap { C l } _ { r , \ i } = \emptyset ,$ , ∀ r, t ∈ Ti, r ≠ t, and i $\mathrm { \Delta } x { \in } C l _ { r , ~ i } , y { \in } C l _ { s , }$ <sup>¼ ¼</sup>and r>s, then x is better than y for the ith decision maker.

## 3.1. Phase I. Constructing a collective preference model

This <sup>fi</sup>rst phase contains three steps (Fig. 2).

## 3.1.1. Step 1: individual classification

In this step, each decision maker uses the common information table I to construct her/his own decision table $\pmb { \mathsf { S } } _ { i } = \langle U , C \cup \{ E _ { i } \} , V , f _ { i } \rangle$ <sup>¼ f g</sup>where E and f are the decision attribute and information function associated with the ith decision maker, respectively. Each decision maker applies the DRSA using her/his decision table S as input. At the end of this step, the classi<sup>fi</sup>cation conducted by each decision maker is characterized using (i) the P-lower approximation and P-boundary of $C l _ { t , } ^ { \le }$ and

$C l _ { t _ { * } } ^ { \geq }$ for each $t \in T _ { i } ,$ and (ii) the classi<sup>fi</sup>cation quality γ<sup>i</sup> de<sup>fi</sup>ned in Eq. (1). This information represents the input for the next step.

## 3.1.2. Step 2: constructing a collective decision table

This step aims to construct a collective decision table $\pmb { S } = \langle U , \ C \cup D _ { \pmb { \mathrm { i } } }$ $V , g \rangle ,$ , where $D = \{ E \}$ <sup>¼</sup>, E is a collective decision attribute and g is a collective information function de<sup>fi</sup>ned for each $x { \in } U ;$

$$
g (x, q) = \left\{ \begin{array}{l l} f (x, q), & \text { if } q \in C, \\ g (x, E), & \text { if } q = E. \end{array} \right.\tag{2}
$$

The collective decision attribute E partitions U into a set of decision classes $\mathbf { C l } = \{ C l _ { t } , ~ t \in T \} , T = \{ 0 , . . . ,$ n} such that each x∈U belongs to one and only one class ${ \cal C l } _ { t } { \in } { \bf C l } .$

To de<sup>fi</sup>ne S, it suf<sup>fi</sup>ces to specify the values of $g ( x , \ E )$ for all $x \in U .$ We thus designed an aggregation procedure, detailed in Section 4. The basic idea of this procedure is to use the outputs of the individual classi<sup>fi</sup>cation step to assign to each object $x \in U$ an assignment interval $I ( x ) = [ l ( x )$ , u(x)], where l(x) and $u ( x )$ are respectively the lower and upper classes to which object x can be assigned. Some simple rules are used to reduce the assignment interval I(x) into a single element that represents the value of $g ( x , \ E )$

The aggregation procedure requires de<sup>fi</sup>ning three parameters: a majority threshold, a veto threshold, and an interval reduction rule.

![](/api/attachments/8C5GBT6Y/fulltext/images/ef71fbed832e552d32f88d1feadbfff6392d1f3ba21ad24374654002bd88bb22.jpg)  
Fig. 2. General schema of Phase I.

The majority and veto thresholds de<sup>fi</sup>ne the aggregation rules. The interval reduction rule reduces the assignment intervals.

## 3.1.3. Step 3: generating collective decision rules

In this step, the mediator should apply the DRSA on the collective decision table S to infer a set of collective decision rules, thus generalizing the decision makers' preference information. The obtained rules are then used as input for the exploitation phase. Using DRSA at this level is similar to using it with a single decision maker (Section 2).

## 3.2. Phase II. Exploiting collective decision rules

The second phase aims to exploit the collective decision rules to classify other decision objects. For more advanced applications, collective decision rules can also be used to develop a rule-based decision support system by incorporating these rules into the knowledge base, but this action is clearly beyond the scope of this paper.

The methodology is structured as an iterative decision-making process. At the end of each step/phase, input data can be modi<sup>fi</sup>ed and the step/phase can be restarted. During the individual classi<sup>fi</sup>cation, each decision maker can iteratively run the DRSA to solve possible inconsistency problems [16]. At the end of the third step, a collective decision rule set is generated. If the involved decision makers agree on these rules, then the decision-making process ends. Otherwise, the process can be restarted by considering new input data.

## 4. Aggregation procedure

The aggregation procedure is used when constructing the collective decision table S 〈U; C∪D; V; g〉 to specify the values of the col-<sup>¼</sup>lective decision information function g with respect to the collective attribute E. The aggregation procedure contains three steps.

## 4.1. Step 1: computing the concordance and discordance powers

This step computes the concordance and discordance powers that the next step uses to de<sup>fi</sup>ne the aggregation rules. First, we must standardize the classi<sup>fi</sup>cation quality $\gamma _ { P } ^ { i } ( \forall i \in H )$ :

$$
{ } ^ { i } \gamma _ { P } ^ { \prime } = \frac { \gamma _ { P } ^ { i } } { \sum _ { r = 1 } ^ { h } \gamma _ { P } ^ { r } } .\tag{3}
$$

## 4.1.1. Concordance power

We de<sup>fi</sup>ne two sets for each $x \in U$ and $\begin{array} { r l } { C l _ { t } { \in } \mathbf { C l } ; } & { { } L \Big ( x , \ C l _ { t } ^ { \le } \Big ) = } \end{array}$ $\left\{ i : i \in H \wedge x \in \underline { { P } } \left( C l _ { t , \ i } ^ { \leq } \right) \right\} \quad \mathrm { a n d } \quad L \Big ( x , \ C l _ { t } ^ { \geq } \Big ) = \left\{ i : i \in H \wedge x \in \underline { { P } } \left( C l _ { t , \ i } ^ { \geq } \right) \right\}$ The <sup>fi</sup>rst (resp. second) set represents the decision makers for whom object x belongs to the lower approximation of $C l _ { t } ^ { \le }$ (resp. $C l _ { t } ^ { \geq } )$ . The concordance powers for assigning x to $C l _ { t } ^ { \le }$ and $C l _ { t } ^ { \geq }$ are computed thus:

$$
L ^ {+} \left(x, C l _ {t} ^ {\leq}\right) = \sum_ {i \in L \left(x, C l _ {t} ^ {\leq}\right)} ^ {i} \gamma_ {P} ^ {\prime}\tag{4}
$$

$$
L ^ {+} \left(x, C l _ {t} ^ {\leq}\right) = \sum_ {i \in L \left(x, C l _ {t} ^ {\geq}\right)} ^ {i} \gamma_ {P} ^ {\prime}.\tag{5}
$$

The number $L ^ { + } ( x , \ C l _ { t } ^ { \leq } )$ (resp. $L ^ { + } ( x , \ C l _ { t } ^ { \geq } ) )$ measures the coalition power of the decision makers who assign x to the lower approximation of $C l _ { t } ^ { \le }$ (resp. Cl<sup>≥</sup>).

The concordance power is de<sup>fi</sup>ned based on the lower class approximation, which contains objects that are assigned with certainty to a given class. In this sense, concordance power can be observed as an argument that supports assigning objects to classes.

Table 4  
Lower approximations of $\begin{array} { r } { C l _ { 3 } ^ { \leq } . } \end{array}$

<table><tr><td>Decision maker</td><td>Lower approximation</td></tr><tr><td>CM</td><td> $\underline{P}\left(CI_{3}^{\leq}\right)=\{x_5,x_6,x_7,x_8,x_9,x_{10},x_{11},x_{12},x_{13},x_{14},x_{15},x_{16},x_{17},x_{18}\}$ </td></tr><tr><td>PP</td><td> $\underline{P}\left(CI_{3}^{\leq}\right)=\{x_5,x_6,x_7,x_8,x_9,x_{10},x_{11},x_{12},x_{13},x_{14},x_{15},x_{16},x_{17},x_{18}\}$ </td></tr><tr><td>CAL</td><td> $\underline{P}\left(CI_{3}^{\leq}\right)=\{x_8,x_{15},x_{18}\}$ </td></tr></table>

Example 4. Here, we illustrate the computation of $L ^ { + } ( x _ { 5 } , \ C l _ { 3 } ^ { \le } ) . \mathsf { A p - }$ plying DRSA on Table 1, where $P { = } \{ A _ { 1 } , . . . , A _ { 7 } \}$ and decision attributes $E _ { 1 } , E _ { 2 }$ and $E _ { 3 }$ correspond to decision makers CM, PP and CAL, respectively, leads to the following classi<sup>fi</sup>cation qualities: $\gamma _ { P } ^ { 1 } = 0 . 6 1$ $\gamma _ { P } ^ { 2 } = 0 . 3 3$ and $\gamma _ { P } ^ { 3 } = 0 . 3 3$ . First, we normalize the classi<sup>fi</sup>cation qualities γ<sup>1</sup>, γ<sup>2</sup>, and $\gamma _ { P } ^ { 3 }$ using Eq. (3), giving $^ 1 \gamma ^ { \prime } { } _ { P } = 0 . 4 8 . , \ ^ { 2 } \gamma ^ { \prime } { } _ { P } = 0 . 2 6 .$ . and $^ { 3 } \gamma ^ { \prime } { } _ { P } = 0 . 2 6 . \ \mathrm { T a b l e } \ 4$ gives the lower approximations of Cl<sup>≤</sup> according to decision makers CM, PP and CAL. According to this information, we have $L ( x _ { 5 } , \ C l _ { 3 } ^ { \le } ) = \{ 1 , \ 2 \}$ . Based on Eq. (4), we obtain $L ^ { + } ( x _ { 5 } , ~ C l _ { 3 } ^ { \le } ) =$ ${ } ^ { 1 } \gamma ^ { \prime } { } _ { P } + { } ^ { 2 } \gamma ^ { \prime } { } _ { P } = 0 . 7 4 .$

## 4.1.2. Discordance power

For each x∈U and Cl ∈Cl, we de<sup>fi</sup>ne sets B(x, $C l _ { t } ^ { \le } ) = \{ i { : } i { \in } H \land x { \in } B n _ { P }$ $( C l _ { t , } ^ { \le } \left. _ { i } \right) \}$ and $B ( x , \ C l _ { t } ^ { \geq } ) = \{ i { : } i { \in } H \land x { \in } B n _ { P } ( C l _ { t , \ i } ^ { \geq } ) \}$ . The <sup>fi</sup>rst (resp. second) set represents the decision makers for whom object x belongs to the boundary of $C l _ { t } ^ { \le }$ (resp. Cl<sup>≥</sup>). The discordance powers for assigning x to the boundary of Cl<sup>≤</sup> and Cl<sup>≥</sup> are computed thus:

$$
B ^ {+} \left(x, C l _ {t} ^ {\leq}\right) = \sum_ {i \in B \left(x, C l _ {t} ^ {\leq}\right)} ^ {i} \gamma_ {P} ^ {\prime}\tag{6}
$$

$$
B ^ {+} \left(x, C l _ {t} ^ {\geq}\right) = \sum_ {i \in B \left(x, C l _ {t} ^ {\geq}\right)} ^ {i} \gamma_ {P} ^ {\prime}.\tag{7}
$$

The number $B ^ { + } ( x , \ C l _ { t } ^ { \le } ) \ ( \mathrm { r e s p . } \ B ^ { + } ( x , \ C l _ { t } ^ { \ge } ) )$ measures the coalition power of the decision makers who assign x to the boundary of $C l _ { t } ^ { \le }$ (resp. Cl<sup>≥</sup>).

De<sup>fi</sup>ning the discordance power is based on class boundaries, which contain objects that can be ruled neither in nor out as class members. In this sense, it represents an argument that opposes assigning objects to classes.

Example 5. Let's now consider the computing of $B ^ { + } ( x _ { 5 } ,$ Cl<sup>≥</sup>). Table 5 gives the boundaries of $C l _ { 4 } ^ { \geq }$ according to decision makers CM, PP and CAL. According to this information, we obtain $B ( x _ { 5 } , \ C l _ { 4 } ^ { \geq } ) = \{ 3 \} . \ A p p \mathrm { { l y i n g } }$ Eq. (7), we obtain $B ^ { + } ( x _ { 5 } , \ C l _ { 4 } ^ { \geq } ) = { } ^ { 3 } \gamma ^ { \prime } { _ { P } } { = } 0 . 2 6 .$

Finally, the semantic interpretations of concordance and discordance powers introduced above are similar to the concepts of concordance and discordance used in the ELECTRE family of multicriteria methods [14]. However, this paper de<sup>fi</sup>nes, computes and uses these concepts differently.

<table><tr><td>Decision maker</td><td>Boundary</td></tr><tr><td>CM</td><td> $Bn_{P}(Cl_{4}^{\geqslant}) = \emptyset$ </td></tr><tr><td>PP</td><td> $Bn_{P}(Cl_{4}^{\geqslant}) = \emptyset$ </td></tr><tr><td>CAL</td><td> $Bn_{P}(Cl_{4}^{\geqslant}) = \{x_{5}, x_{6}, x_{7}, x_{9}, x_{10}, x_{11}, x_{12}, x_{13}, x_{14}, x_{16}, x_{17}\}$ </td></tr></table>

## 4.2. Step 2: definition of assignment intervals

We <sup>fi</sup>rst introduce the aggregation rules that de<sup>fi</sup>ne the assignment intervals. Let θ∈[0.5, 1.0] be a majority threshold and $\theta ^ { \prime } \in \left[ 0 , \ 0 . 5 \right] :$ a veto threshold. Based on the concordance and discordance powers, we may distinguish four situations for assigning x to $\begin{array} { r } { C l _ { t } ^ { \leq . } } \end{array}$

<table><tr><td></td><td> $B^{+}(x, Cl_{t}^{\leq})<\theta'$ </td><td> $B^{+}(x, Cl_{t}^{\leq})\geq\theta'$ </td></tr><tr><td> $L^{+}(x, Cl_{t}^{\leq})\geq\theta$ </td><td> $x\in Cl_{t}^{\leq}$ </td><td> $x\notin Cl_{t}^{\leq}$ </td></tr><tr><td> $L^{+}(x, Cl_{t}^{\leq})<\theta$ </td><td> $x\notin Cl_{t}^{\leq}$ </td><td> $x\notin Cl_{t}^{\leq}$ </td></tr></table>

The following aggregation rule can summarize these situations:

$$
\text {   If   } L ^ {+} (x, C l _ {t} ^ {\leq}) \geq \theta \wedge B ^ {+} (x, C l _ {t} ^ {\leq}) <   \theta^ {\prime} \text {   then   } x \in C l _ {t} ^ {\leq} \text {   else   } x \notin C l _ {t} ^ {\leq} \text {(Rule 1).   }
$$

The same four situations also apply to assigning x to $C l _ { t } ^ { \geq }$ and can be summarized by the following aggregation rule:

$$
\text {   If   } L ^ {+} (x, C l _ {t} ^ {\geq}) \geq \theta \land B ^ {+} (x, C l _ {t} ^ {\geq}) <   \theta^ {\prime} \text {   then   } x \in C l _ {t} ^ {\geq} \text {   else   } x \notin C l _ {t} ^ {\geq} \text {(Rule 2).   }
$$

The <sup>fi</sup>rst (resp. second) aggregation rule can be explained as follows. Object x is assigned to $C l _ { t } ^ { \le }$ (resp. Cl<sup>≥</sup>) if and only if: (i) there is a “suf<sup>fi</sup>- cient” majority of decision makers – using their classi<sup>fi</sup>cation quality – who assign x to $C l _ { t } ^ { \le }$ (resp. Cl<sup>≥</sup>), and (ii) when the <sup>fi</sup>rst condition holds, no minority of decision makers shows an “important” opposition to assigning x to $C l _ { t } ^ { \le }$ (resp. Cl<sup>≥</sup>).

The <sup>fi</sup>rst condition of the aggregation rules allows implementing the majority principle. Setting $L ^ { + } ( x , \ C l _ { t } ^ { \leq } ) \geq \theta \ \mathrm { \ ( r e s p . ~ } L ^ { + } ( x , \ C l _ { t } ^ { \geq } ) \geq \theta \ )$ where $0 . 5 { \le } \theta { \le } 1$ , ensures that at least <sup>fi</sup>fty percent of the decision makers support assigning x to Cl<sup>≤</sup> (resp. Cl<sup>≥</sup>). The second condition allows implementing the veto effect. In fact, setting $B ^ { + } ( x , \ C l _ { t } ^ { \le } ) < \theta ^ { \prime }$ (resp. $B ^ { + } ( x , \ C l _ { t } ^ { \geq } ) < \theta ^ { \prime } )$ , where $0 \leq \theta ^ { \prime } \leq 0 . 5$ , ensures that the minority of decision makers may have a veto effect on the <sup>fi</sup>nal decision when their combined power is equal to or greater than the veto threshold θ′.

Applying aggregation rules to object set U allows associating a collective assignment interval $I ( x ) = [ l ( x )$ , u(x)] with each object x, where:

$$
l (x) = \left\{ \begin{array}{l l} \operatorname{argmax} _ {C l _ {t}} N _ {1} (x), & \text { if } N _ {1} (x) \neq \emptyset , \\ C l _ {0}, & \text { otherwise }. \end{array} \right.\tag{8}
$$

$$
u (x) = \left\{ \begin{array}{l l} \operatorname{argmin} _ {C l _ {t}} N _ {2} (x), & \text { if } N _ {2} (x) \neq \emptyset , \\ C l _ {n}, & \text { otherwise }. \end{array} \right.\tag{9}
$$

where $N _ { 1 } ( x ) = \{ C l _ { t } { : } x { \in } C l _ { t } ^ { \geq } \}$ and $N _ { 2 } ( x ) = \{ C l _ { t } { : } x { \in } C l _ { t } ^ { \leq } \} . \ N _ { 1 } ( x )$ contains the classes to which x is assigned by applying the second aggregation rule (Rule 2), while $N _ { 2 } ( x )$ contains the classes to which x is assigned by applying the <sup>fi</sup>rst aggregation rule (Rule 1).

Example 6. Assume that =0.5 and $\theta ^ { \prime } { = } 0 . 3$ . Table 6 summarizes the application of Rules 1 and 2 to object x . This table shows that the <sup>fi</sup>rst aggregation rule is veri<sup>fi</sup>ed only for $C l _ { 3 } ^ { \le }$ and $C l _ { 4 } ^ { \le }$ while the second aggregation rule is veri<sup>fi</sup>ed only for Cl<sup>≥</sup> and Cl<sup>≥</sup>. We thus obtain $x _ { 5 } \in C l _ { 3 } ^ { \le }$ $x _ { 5 } \in C l _ { 4 } ^ { \le } , x _ { 5 } \in C l _ { 1 } ^ { \ge }$ and $x _ { 5 } \in C l _ { 2 } ^ { \geq }$ . Based on this information, we obtain $N _ { 1 } ( x _ { 5 } ) = \{ C l _ { 1 } , C l _ { 2 } \}$ and $N _ { 2 } ( x _ { 5 } ) = \{ C l _ { 3 } , \ C l _ { 4 } \}$ . Using Eqs. (8) and (9), we obtain $l ( x _ { 5 } ) = C l _ { 2 }$ and $u ( x _ { 5 } ) = C l _ { 3 } .$ . Finally, we obtain $I ( x _ { 5 } ) { = } [ C l _ { 2 } , C l _ { 3 } ]$

Application of aggregation rules to object x with $\theta { = } 0 . 5$ and $\theta ^ { \prime } { = } 0 . 3 .$

<table><tr><td> $Cl_{t}$ </td><td> $Cl_{0}^{\leqslant}$ </td><td> $Cl_{1}^{\leqslant}$ </td><td> $Cl_{2}^{\leqslant}$ </td><td> $Cl_{3}^{\leqslant}$ </td><td> $Cl_{4}^{\leqslant}$ </td><td> $Cl_{1}^{\geqslant}$ </td><td> $Cl_{2}^{\geqslant}$ </td><td> $Cl_{3}^{\geqslant}$ </td><td> $Cl_{4}^{\geqslant}$ </td><td> $Cl_{5}^{\geqslant}$ </td></tr><tr><td> $L^{+}(x_{5}, Cl_{t})$ </td><td>0</td><td>0</td><td>0</td><td>0.74</td><td>1</td><td>1</td><td>1</td><td>0.48</td><td>0</td><td>0</td></tr><tr><td> $B^{+}(x_{5}, Cl_{t})$ </td><td>0</td><td>0</td><td>0.52</td><td>0.26</td><td>0</td><td>0</td><td>0</td><td>0.52</td><td>0.26</td><td>0</td></tr><tr><td>Decision</td><td>No</td><td>No</td><td>No</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>No</td><td>No</td><td>No</td></tr></table>

## 4.3. Step 3: reducing the assignment interval

This step aims to reduce the assignment intervals $I ( x ) , \forall x \in U ,$ , to a single class that represents the value to assign to the collective decision attribute $g ( x , \ E ) ,$ as in Section 3.1. Let $I ( x ) = [ l ( x ) , \ u ( x ) ]$ be the assignment interval for object $x \in U$ de<sup>fi</sup>ned as above. Two cases hold for reducing I(x). The <sup>fi</sup>rst case holds when $l ( x ) = u ( x )$ . Here, object x is assigned to a single class, and we can set g(x, $E ) = l ( x ) = u ( x )$ The second case holds when $l ( x ) { < } u ( x )$ . This corresponds to the situation where object x can be assigned to more than one class. To specify the value of g(x, E) when the second case holds, we may apply one of the following rules to reduce the collective assignment interval I(x) to a single class:

• use the “min” operator on $I ( x ) \colon g ( x , \ E ) = l ( x ) \ ( { \mathrm { R u l e } } \ 3 )$

• use the “max” operator on $I ( x ) \colon g ( x , \ E ) = u ( x ) \ ( { \mathrm { R u l e } } \ 4 )$

• use the “median” operator on $l ^ { \prime } , . . . , u ^ { \prime } ,$ where $l ^ { \prime } , \ldots , u ^ { \prime }$ is an ordered list issued from $l ( x ) , . . . , u ( x ) \colon g ( x , \ E ) = \mu ( l ^ { \prime } , . . . , u ^ { \prime } )$ (Rule 5).

• use the “<sup>fl</sup>oor” of the median value: $g ( x , \ E ) { = } \lfloor \mu ( l ^ { \prime } , { \ldots } , \ u ^ { \prime } ) \rfloor { \mathrm { ~ ( R u l e ~ 6 ) ~ } }$

• use the $" \mathrm { c e i l " }$ of the median value: $g ( x , \ E ) { = } \left[ \mu ( l ^ { \prime } , { \ldots } , \ u ^ { \prime } ) \right] \left( \mathrm { R u l e } \ 7 \right)$

Function μ(⋅) returns the median of the values given as parameters. The median of a <sup>fi</sup>nite list of values can be found by arranging the numbers in ascending order and picking the middle one. If there is an even number of values, then there is no single middle value; the median is thus the mean of the two middle values. Decision attributes are generally de<sup>fi</sup>ned on ordinal scales, and it is thus not possible to compute the mean of the middle values to obtain the median. The two last rules (floor and ceil) are added to avoid this problem. Let a and $a _ { i + 1 }$ be the two middle values of a set $\{ a _ { 1 } . . . , a _ { i } , a _ { i + 1 } ,$ $\ldots , a _ { n } \}$ of n ordinal values with $a _ { i } \leq a _ { i + 1 } , \forall i ,$ , and n is an even number. The floor operator chooses the lower value among a and $a _ { i + 1 } , \mathrm { i } . \mathbf { e } . , a _ { i } ,$ while the ceil operator chooses the higher value among a and $a _ { i + 1 } ,$ $\mathrm { i } . \mathsf { e } . , a _ { i + 1 } .$

Example 7. In the previous example, we obtained $I ( x _ { 5 } ) { = } [ C l _ { 2 } , C l _ { 3 } ] .$ The value of $g ( x _ { 5 } , \ E )$ according to the interval reduction rules “min”, “max”, “<sup>fl</sup>oor” and “ceil” is $C l _ { 2 } , C l _ { 3 } ,$ Cl and $\boldsymbol { C l } _ { 3 } ,$ respectively. The “median” operator does not apply in this particular decision problem.

## 5. Case study

The methodology has been validated by developing a prototype. This section <sup>fi</sup>rst provides a brief description of this prototype and presents the application of the prototype to the nuclear risk management decision problem. More details are available in a previous study [4].

## 5.1. Prototype

A prototype called RSGMC (Rough Set-based Group Multicriteria Classi<sup>fi</sup>cation) has been developed using Visual C++. The prototype is coupled with 4eMka2, which, as indicated above, is a decision support system for multicriteria classi<sup>fi</sup>cation problems based on DRSA. It is also loosely coupled with the PRIME software developed during the PRIME project. In this paper, PRIME software is used to generate the global venerability map. The evaluation matrix is implemented as an Excel spreadsheet. The data exchange between system components is based on “.txt” <sup>fi</sup>les.

## 5.2. Problem description

This research has been initially motivated by a real-world project – designed by PRIME – about managing post-accident nuclear risk in the southern region of France. More information on this project is available [26]. The study zone covers a radius of 50 km around the three nuclear sites (Cruas, Tricastin-Pierrelatte and Marcoule) in the lower Rhône Valley. The territory studied also covers the Rhône River downstream from Marcoule and the nearby coastal territories, and it extends along the Rhône River to the Mediterranean coastal area. The PRIME project aims to characterize the districts in the study area and classify them using their vulnerability in a nuclear accident event. The PRIME working group has thus adopted a six-level scale from 0 (normal situation) to 5 (major and long-lasting negative impact).

To serve as assignment examples, different members of the PRIME working team have selected eighteen districts from the study area. Each district is described using a set of seven attributes: three attributes to measure the radioecological vulnerability of the agricultural area $\left( A _ { 1 } \right)$ , forest area $\left( A _ { 2 } \right)$ and urban area $( A _ { 3 } ) ;$ one attribute to measure the Rhône River's radioecological vulnerability $( A _ { 7 } ) ;$ and three attributes to measure the vulnerability of real estate $\left( A _ { 4 } \right)$ , tourism $\left( A _ { 5 } \right)$ and economic activity $\left( A _ { 6 } \right)$ . Table 1, above, presents the evaluations of the selected districts over all attributes.

## 5.3. Application

## 5.3.1. Phase I. Constructing a collective preference model

The individual classi<sup>fi</sup>cation step requires that each decision maker applies DRSA on her/his own decision table. As DRSA is not included in the current version of the prototype, decision makers should (individually) use 4eMka2. Once all inconsistency problems are solved, decision makers should save the appropriate results and provide them to the mediator for further treatment.

To construct the collective decision table in the second step, the mediator should <sup>fi</sup>rst specify the preference parameters (majority and veto thresholds), interval reduction rule, and individual decision tables' locations. After specifying all required parameters, the mediator can run the aggregation procedure. The output is the collective decision table.

Finally, the mediator should use 4eMka2 to apply DRSA, using the collective decision table. This allows obtaining the <sup>fi</sup>nal collective decision rules. For illustration, the screen capture in Fig. 3 provides an extract from the obtained collective decision rules.

Describing the decision rules is straightforward. Rule 20, for example, says that object x is assigned to Cl<sup>≥</sup> when (i) its evaluation using attribute $A _ { 2 }$ is less than or equal to 2 and (ii) its evaluation using attribute $A _ { 5 }$ is less or equal to 4. The strength of Rule 20 is 92.86%, and all decision objects except $x _ { 6 } , x _ { 8 } , x _ { 1 5 } , x _ { 1 7 }$ and $x _ { 1 8 }$ support this rule.

## 5.3.2. Phase II. Exploiting collective decision rules

Once the <sup>fi</sup>rst phase is achieved, collective decision rules can be used to classify the districts in the study area. In this decision problem, the classi<sup>fi</sup>cation results can also be obtained in map form from the PRIME software. The screen capture in Fig. 4 provides the global vulnerability map generated by the PRIME software.

The left-hand side of the interface in Fig. 4 shows the global vulnerability scale with the shaded tones. The map on the right-hand side of the interface shows the <sup>fi</sup>nal classi<sup>fi</sup>cation of the different districts. Vulnerability decreases relatively concentrically around the Tricastin-Pierrelatte nuclear site, which is the location of the <sup>fi</sup>ctive accident considered in this case study.

## 6. Comparative study

This section discusses some existing proposals to help groups with multicriteria classi<sup>fi</sup>cation problems with different characteristics. The <sup>fi</sup>rst characteristic considers the aggregation level adopted to combine individual perspectives. Two approaches are generally distinguished in the multicriteria literature to aggregate these perspec tives [10,11], either at the input or output levels. For classi<sup>fi</sup>cation problems, the <sup>fi</sup>rst approach proceeds thus: (i) individual input data and preference values are combined into a set of data and values accepted by the group, and (ii) a multicriteria classi<sup>fi</sup>cation method is used to obtain the <sup>fi</sup>nal result. Previous studies present examples of proposals based on this approach [9,10]. In the second approach, (i) each decision maker performs her/his individual classi<sup>fi</sup>cation and (ii) an appropriate aggregation operator is used to combine the individual classi<sup>fi</sup>cations into a collective one. Previous research includes examples of proposals based on this approach [17,20,33]. The methodology proposed in this paper adopts the output level aggregation approach.

![](/api/attachments/8C5GBT6Y/fulltext/images/25fabc8be98a22aa66a3a1261f0ccf2de80e50eb9f36297b6fc7bb5a859ac73d.jpg)  
Fig. 3. A screen capture showing the collective decision rules.

![](/api/attachments/8C5GBT6Y/fulltext/images/e23ad7a4ad3797be1748bdfee814a38f51920a1a79eee314f190dbc7dae2285a.jpg)  
Fig. 4. Global vulnerability map.

The second characteristic is the aggregation rule used to combine the input data. Three categories of aggregation rules may be distinguished: statistical, functional and rule-based techniques. The main advantage of statistical operators is their compactness and simplicity. The functional aggregation rules are based on using functions, i.e., a weighted-sum or distance measure. Researchers have presented examples of proposals based on functional aggregation [3,20]. Rulebased aggregation techniques are based on using Boolean and/or “if … then …” rules. These rules apply to complex situations for which statistical or functional aggregation rules cannot be applied. In some situations, aggregating the input data is simply based on discussion between different decision makers [9,33].

The third characteristic concerns computing decision makers' “weights”. The mediator can simply specify these weights. In this case, weights generally re<sup>fl</sup>ect the hierarchical level of decision makers in the organization. However, there is a need for more formal and objective methods [8]. Some researchers [31] thus propose using the AHP [35] method to derive members' weights. More recently, a study has [22] proposed using a previous method [36] to integrate the relative importance of the groups' members in the consensus construction. The contribution of each decision maker in the proposed methodology is measured by the quality of the individual classi<sup>fi</sup>cation conducted by a decision maker.

The fourth characteristic is related to the decision-making strategy used. This characteristic considers the decision-making procedure adopted, which is more related to practical decision-making aspects. There are two main procedures in group decision-making: parliamentary and consensus decision-making. Parliamentary procedure seeks the agreement of most decision makers, while consensus decision-making seeks the agreement of most decision makers and the resolution of mitigating minority objections. The proposed methodology is based on consensus decision-making procedure, as in previous proposals [9,10].

The <sup>fi</sup>fth characteristic is related to the preference parameters requirement. In most proposed approaches [9,10], we must de<sup>fi</sup>ne several preference parameters, such as the relative importance of criteria. Several proposals [17,33] do not need any preference parameters. The proposed methodology requires de<sup>fi</sup>ning two preference parameters (majority and veto thresholds) and an interval reduction rule.

The sixth characteristic considers the preference elicitation strategy. At this level, we distinguish two approaches to specify preference parameters: direct or indirect. Direct elicitation requires that decision makers explicitly specify the values for all decision parameters [10]. Indirect elicitation preference parameters are implicitly obtained. This is the case with the previously proposed aggregation/disaggregation approach [12]. The basic idea of this approach is to infer values for preference parameters based on a set of assignment examples supplied by the decision makers. The problem with the aggregation/disaggregation approach is that it becomes more complex and dif<sup>fi</sup>cult to implement in group decision-making. To avoid this dif<sup>fi</sup>culty, a previous study [9] proposes using an intensive dialog between the decision makers to construct a set of collective assignment examples collectively and interactively, which are then used as input to the aggregation/disaggregation approach [12]. The methodology proposed in this paper requires the mediator to explicitly de<sup>fi</sup>ne three parameters.

The last characteristic is related to the support of robust assignment, i.e., accepting interval-based de<sup>fi</sup>nitions of assignment examples [9,10]. Conversely, some proposals [17,33], as well as our proposed methodology, do not support robust assignment. However, it is possible to extend the methodology to support robust assignment [10,12]. This will be addressed in a forthcoming paper.

## 7. Conclusion and future work

We proposed a methodology to support groups in multicriteria classi<sup>fi</sup>cation problems. The methodology is composed of two phases. The <sup>fi</sup>rst phase, based on using DRSA, takes a set of assignment examples as input and outputs a set of collective decision rules, representing a generalized description of the decision makers' preference information. The second phase then applies these collective decision rules to classify all decision objects. The methodology has two main qualities. The <sup>fi</sup>rst one is using “if … then …” aggregation rules that coherently implement the majority principle and veto effect, thus obtaining consensual decisions. The second quality is using the quality of individual classi<sup>fi</sup>cations to objectively measure the contribution of each decision maker to the collective decision.

The methodology requires de<sup>fi</sup>ning three parameters (the majority threshold, the veto threshold and the interval reduction rule). However, decision makers may not agree on these parameters' values. A possible solution to this problem could be using an indirect elicitation approach (see Section 6). Another possible critique of the methodology is the reduced collaboration level among decision makers during the individual classi<sup>fi</sup>cation step. A possible solution to this shortcoming is to combine the input and output aggregation-level approaches introduced above.

Several topics need future investigation. First, it would be interesting to study the possibility of using other aggregation rules (e.g., Minmax or Leximax criteria). Second, it is possible to explore using decision rulerelated information to de<sup>fi</sup>ne the aggregation rules. Third, it might be fruitful to investigate other classi<sup>fi</sup>cation methods that accept intervalbased assignment examples. Finally, we intend to enhance our work by robust assignment and con<sup>fl</sup>ict resolution support.

## References

[1] V. Belton, J. Pictet, A framework for group decision using a MCDA model: sharing, aggregation or comparing individual information, Journal of Decision Systems 6 (3) (1997) 283-303.

[2] S. Ben Khélifa, J.-M. Martel, A distance-based collective weak ordering, Group Decision and Negotiation 10 (4) (2001) 317–329.

[3] I. Brigui-Chtioui, I. Saad, A multi-agent approach for collective decision making in knowledge management, Group Decision and Negotiation 20 (1) (2011) 19–37.

[4] S. Chakhar, I. Saad, A Methodology to Support Group Multicriteria Classi<sup>fi</sup>cation Research Report RR-MIS-2011-01, MIS, University of Picardie Jules Verne, Amiens, France, 2011, http://www.mis.u-picardie.fr/Publications/Rapports-de-recherche/.

[5] Y.-L. Chen, L.-C. Cheng, An approach to group ranking decisions in a dynamic environment, Decision Support Systems 48 (4) (2010) 622–634.

[6] I. Cil, O. Alpturk, H.R. Yazgan, A new collaborative system framework based on a multiple perspective approach: InteliTeam, Decision Support Systems 39 (4) (2005) 619–641.

[7] G. Colson, The OR's prize winner and the software ARGOS: how a multijudge and multicriteria ranking GDSS helps a jury to attribute a scienti<sup>fi</sup>c award, Computers and Operations Research 27 (2000).741-755

[8] W.D. Cook, Distance-based and ad hoc consensus model in ordinal preference ranking with intensity of preference, European Journal of Operational Research 172 (2) (2006) 369–385.

[9] S. Damart, L.C. Dias, V. Mousseau, Supporting groups in sorting decisions: methodology and use of a multicriteria aggregation/disaggregation DSS, Decision Support Systems 43 (4) (2007) 1464–1475.

[10] L.C. Dias, J.N. Clímaco, ELECTRE TRI for groups with imprecise information on parameter values, Group Decision and Negotiation 9 (2000) 355–377.

[11] L.C. Dias, J.N. Clímaco, Dealing with imprecise information in group multicriteria decisions: a methodology and a GDSS architecture, European Journal of Operational Research 160 (2005) 291–307

[12] L.C. Dias, V. Mousseau, J. Figueira, J. Clímaco, An aggregation/disaggregation approach to obtain robust conclusions with ELECTRE TRI, European Journal of Operational Research 138 (2002) 332–348.

[13] R.F. Dyer, E.H. Forman, Group decision support with the AHP, Decision Support Systems 8 (1992) 99–124.

[14] I.R. Figueira. V. Mousseau. B. Roy, Electre methods, in: I.R. Figueira. S. Greco, M Ehrgott (Eds.), Multiple Criteria Decision Analysis: State of the Art Surveys, Springer-Verlag, New York, 2005, pp. 133–162.

[15] S. Greco, B. Matarazzo, R. Słowiński, The use of rough sets and fuzzy sets in Multiple-Criteria Decision Making, in: T. Gal, T. Stewart, T. Hanne (Eds.), Advances in Multiple Criteria Decision Making, Kluwer Academic Publishers. Boston. 1999. pp. 14.1–14.59.

[16] S. Greco, B. Matarazzo, R. Słowiński, Rough sets theory for multicriteria decision analysis, European Journal of Operational Research 129 (1) (2001) 1–47.

[17] S. Greco, B. Matarazzo, R. Słowiński, Dominance-based rough set approach to decision involving multiple decision makers, in: S. Greco, Y. Hata, S. Hirano, M. Inuiguchi, S. Miyamoto, H.S. Nguyen, R. Słowiński (Eds.), Proceedings of the 5th International Conference Rough Sets and Current Trends in Computing, Kobe, Japan, November 6–8, Volume 4259 of LNAI, Springer-Verlag, Berlin Heidelberg 2006, pp. 306–317.

[18] S. Greco, M. Kadzinski, V. Mousseau, R. Słowiński, Robust ordinal regression for multiple criteria group decision: UTA<sup>GMS</sup>-GROUP and UTADIS<sup>GMS</sup>-GROUP, Decision Support Systems 52 (3) (2012) 549–561.

[19] A. Hatami-Marbini, M. Tavana, An extension of the Electre I method for group decision-making under a fuzzy environment, Omega 39 (2011) 373–386.

[20] K. Jabeur, J.-M. Martel, A collective choice method based on individual preferences relational systems (p.r.s.), European Journal of Operational Research 177 (3) (2007) 1549–1565.

[21] K. Jabeur, J.-M. Martel, An ordinal sorting method for group decision-making, European Journal of Operational Research 180 (2007) 1272–1289.

[22] K. Jabeur, J. Martel, S. Ben Khelifa, A distance-based collective preorder integrating the relative importance of the group's members, Group Decision and Negotiation 13 (2004) 327–349.

[23] T. Jelassi, G.E. Kersten, S. Zionts, An Introduction to Group Decision and Negotiation Support, in: C.A. Bana e Costa (Ed.), Readings in Multiple Criteria Decision Aid, Springer-Verlag Publishing, Berlin, 1990, pp. 537–568.

[24] C. Macharis, J.P. Brans, B. Mareschal, The GDSS PROMETHEE procedure — a PROMETHEE-GAIA based procedure for group decision support, Journal of Deci sion Systems 7 (1998) 283–307.

[25] N.F. Matsatsinis, A.P. Samaras, MCDA and preference disaggregation in group decision support systems, European Journal of Operational Research 130 (2001) 414–429.

[26] C. Mercat-Rommens, S. Chakhar, E. Chojnacki, V. Mousseau, Coupling GIS and multi-criteria modelling to support post-accident nuclear risk evaluation: an application in the southern France region Research Report CR-LGI-2010-18, LGI, Ecole Centrale Paris, France, 2010, http://www.lgi.ecp.fr/Biblio/PDF/CR-LGI-2010-18.pdf.

[27] G. Munda, Social multi-criteria evaluation (SMCE): methodological foundations and operational consequences, European Journal of Operational Research 158 (3) (2004) 662–677.

[28] H. Nurmi, J. Kacprzyk, M. Fedrizzi, Probabilistic, fuzzy and rough concepts in social choice, European Journal of Operational Research 95 (2) (2007) 264–277.

[29] Z. Pawlak, Rough sets, International Journal of Information & Computer Sciences 11 (1982) 341–356.

[30] Z. Pawlak, Rough Set. Theoretical Aspects of Reasoning about Data, Kluwer Academic Publishers, Dordrecht, 1991.

[31] R. Ramanathan, L. Ganesh, Group preference aggregation methods employed in AHP: an evaluation and an intrinsic process for deriving members' weights, European Journal of Operation Research 79 (1) (1994) 249–265.

[32] I. Saad, S. Chakhar, A decision support for identifying crucial knowledge requiring capitalizing operation, European Journal of Operational Research 195 (3) (2009) 889–904.

[33] I. Saad, C. Rosenthal-Sabroux, M. Grundstein, Improving the decision making process in the design project by capitalizing on company's crucial knowledge, Group Decision and Negotiation 14 (2) (2005) 131–145.

[34] I. Saad, M. Grundstein, C. Rosenthal-Sabroux, How to improve collaborative decision making in the context of knowledge management, in: P. Zaraté, J.P. Belaud, G. Camilleri, F. Ravat (Eds.), Collaborative Decision Making: Perspectives and Challenges, Proceedings of the IFIP TC8/WG8.3 Working Conference, International Conference on Collaborative Decision Making, CDM 2008, Toulouse, France, July 1–4, IOS Press, Amsterdam, The Netherlands, 2008, pp. 493–500

[35] T.L. Saaty, The Analytic Hierarchy Process, McGraw Hill, New York, 1980.

[36] M. Zeleny, Multiple Criteria Decision Making, McGraw-Hill, New York, 1982

![](/api/attachments/8C5GBT6Y/fulltext/images/f4ab513338bf08041bd8d2e162befefa1efd9891e7a151dbdfb42f055095f180.jpg)

Salem Chakhar is with the Centre for Research in Regional Planning and Development, University of Laval, Quebec City, Canada. He received his M.S. in Computer Science and Modeling from the High School of Management of Tunis (Tunisia) and his Ph.D. in Computer Science from the University of Paris-Dauphine (France), Salem Chakhar's research interests include geographical information science and systems, spatial modeling and analysis, database and information systems, fuzzy theory and applications and decision support systems. He has published in journals such as International Journal of Geographical Information Science; Computers, Environment and Urban Systems; Infor mation Sciences; Information and Software Technology;

European Journal of Operational Research; and Environment and Planning B: Planning and Design.

![](/api/attachments/8C5GBT6Y/fulltext/images/b25453c25430d120f3e80f6006afd4568690b818d4862ec0acbbff8936c017cd.jpg)  
Man, and Cybernetics, etc.

Inès Saad is an Associate Professor in Computer and Information Systems Department at Amiens Business School, France. She is also a Researcher within the MIS Laboratory at the University of Picardie Jules Verne (France). She obtained her Ph.D. in Computer Science from the University of Paris-Dauphine in 2005. From 2005 to 2006, Dr. Saad has been an Assistant Professor at the University of Paris-Dauphine. The focus of her research is on the knowledge management, information system and multiple criteria decision making. She has several publications in international conferences and journals such as EJOR, GDN, and SIM. Inès SAAD is also a reviewer in many international journals and conferences such as EJOR and IEEE Transactions on Systems,
