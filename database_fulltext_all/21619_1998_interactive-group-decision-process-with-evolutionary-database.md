---
otero_id: 21619
otero_key: "QH6BAJRW"
title: "Interactive group decision process with evolutionary database"
authors: "Soung Hie Kim; Sang Hyun Choi; Byeong Seok Ahn"
year: "1998"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(98)00054-2"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Interactive group decision process with evolutionary database

Soung Hie Kim <sup>a,)</sup>, Sang Hyun Choi <sup>a</sup>, Byeong Seok Ahn <sup>b</sup>

<sup>a</sup> Graduate School of Management, Korea AdÕanced Institute of Science and Technology, 207-43 Cheongryangri, Dongdaemoon, Seoul 130-012, South Korea

<sup>b</sup> Department of Business Administration and Accounting, Suwon UniÕersity, San 2-2, Wau, Bongdam, Hwasung, Kyonggi 445-743, South Korea

Accepted 10 August 1998

## Abstract

This paper presents interactive procedures for solving a multiple criteria group decision making MCGDM problem withŽ . incomplete information when multiple decision makers are involved. It is difficult for group members participating in the decision making process to articulate their preferences with cardinal values. Therefore, we represent their preferences with utility ranges obtained by solving linear programming LP problems with incompletely specified information, find Ž . conflicting judgments, if any in their specified information, and suggest interaction processes to help the group reach a consensus. This paper will provide an algorithmic basis for a normative and interactive knowledge based group decision support system. q 1998 Elsevier Science B.V. All rights reserved.

Keywords: Group decision process; Multiple criteria decision making; Incomplete information; Interactive procedure; Utility range; Dominance relation

## 1. Introduction

The increasing complexity of the socio-economic environment makes it increasingly difficult for a single decision maker DM to consider all relevant aspects of a problem. As a result, many organizations employŽ . groups in decision making. This trend also has important consequences for research on decision support, in which a group decision support system GDSS intended to aid multiple cooperating decision makers has Ž . become an important topic.

There is an increasing trend for the necessity of an interactive procedure because a selection is not generally made in a single step, and the quality of decision results is enhanced through learning effects during all steps of the interactive decision support 6 . For the support of cooperative group decision making, this paper develops <sup>w</sup> <sup>x</sup> an interactive approach requiring group members to express individual and collective preferences in an incomplete manner. In real cases, it is sometimes difficult to determine the exact values of parameters such as, criteria trade-off weights, experts’ weights, and the alternatives’ utilities on each criterion. In this paper we suggest a model that helps us find a group consensus without assessing these parameters in specific cardinal values. We also suggest a database-oriented interaction process in which the database contains range-typed utilities for reaching a consensus.

## 2. Prior studies of group decision making

Group decision making involves weighted aggregation of differing individual preferences to obtain a single collective preference. This subject has received a great deal of attention from researchers in many disciplines. Much of the research involving normative models of group decision making has focused upon the area of social choice; the early work of Arrow has been a major influence in this area. Much of the research that has followed Arrow’s work concentrates largely on utility-based theory as a tool for group decision making 4,11,12,20,22 . <sup>w</sup> <sup>x</sup>

Many studies employing cardinal representations of group preferences have been built by combining individual preference models into an additive value or utility function because of their robustness, transparency, and ease of development 12 . Only a few studies, however, have considered incomplete information in the<sup>w</sup> <sup>x</sup> group decision making process. Anandalingam 1 presented that even without specifying exact preference<sup>w</sup> <sup>x</sup> weights for criteria, dominance relationships between alternatives may be established, and a Nash bargaining solution established among the affected states. Salo 20 recently developed an interactive approach for the <sup>w</sup> <sup>x</sup> aggregation of group members’ preference judgments in the context of an evolving value representation emphasizing on interactive decision support in decision analytic techniques. Assuming additive value or utility function and an imprecise preference model, he suggests strong or weak dominance relations using intervals of individual preference value. Although each approach has characteristics peculiar to the problem domain, we find limitations in their application to real world problems in that they increase the burden on DMs to elicit preference information, and make less effort to provide a direction for consensus through interaction with their users.

A database-oriented approach to decision support system DSS was first proposed by Donovan 3 for Ž . <sup>w</sup> <sup>x</sup> single-user DSS. It was later extended to cover not only data management but model management and multiuser aspects of DSS 8 . In these research fields attempts are made to combine existing methodologies with their own<sup>w</sup> <sup>x</sup> systems 2,7,13 , but such systems require exact and complete specifications on model parameters and can be<sup>w</sup> <sup>x</sup> tedious and time consuming to assess.

## 3. Problem statement

In this paper we suggest a method for seeking consensus in a cooperative group decision context using incomplete information in order to reduce the burden on group members. A group decision making process with incomplete information should provide refined frameworks for the following tasks: 1 suggesting a preferenceŽ . aggregation method among group members; 2 establishing dominance conditions for group decision makingŽ . based on the concept of individual pairwise dominance; 3 discovering conflicting opinions of group members; Ž . and then 4 suggesting the interactive approach which is most robustly and effectively useable, especially by Ž . nonexperts in multiple criteria decision making MCDM methodology. Ž .

We will suggest frameworks to support the above tasks under the following assumptions. This paper considers a group decision problem in which a group with K members evaluates a finite set of M alternatives characterized by a finite set of N criteria. A classical evaluation of alternatives leads to the aggregation of all criteria into a unique criterion called a utility function. In this paper, the criteria are assumed to be preference independent, leading to an additive multiple criteria utility function 12 . We define our notations as follows:<sup>w</sup> <sup>x</sup> $u _ { i } ^ { k } ( a _ { \mathrm { m } } )$ is the k-th individual’s utility value associated with criterion i of selecting alternative $a _ { \mathrm { { m } } } ; \ w _ { i }$ is the set of group’s trade-off weights associated with criterion i, in situations where DMs consider common criteria; $w _ { i } ^ { k }$ is the set of k-th DM’s trade-off weights associated with criterion i, in situations where DMs individually consider different criteria. For example, when three DMs are involved and three criteria are considered, $w _ { 1 } \geq w _ { 2 } \geq w _ { 3 }$ Ž . common criteria is induced only when $w _ { 1 } ^ { k } \ge w _ { 2 } ^ { k } \ge w _ { 3 } ^ { k }$ Ž .different criteria , for $\forall \ k ; \ w ^ { k }$ is the importance weight associated with individual k; $\begin{array} { r } { W = \{ \phi _ { w } , ~ \sum _ { i } w _ { i } = 1 , ~ w _ { i } \ge 0 \} } \end{array}$ : the set of constraints or all possible values of criteria weights, $w \in W$ , where $\varPhi _ { w }$ is a set derived from the decision maker’s incomplete information regarding the relative importance among criteria; $U _ { i } ^ { k } \colon$ the set of constraints on utilities obtained from group members’ information, for consequences when criterion i is given, $\{ u _ { i } ^ { k } ( a ^ { \prime } ) , u _ { i } ^ { k } ( a ) \} \in U _ { i } ^ { k }$ $\varPsi ( a ^ { \prime } , a ) = \{ W , U \}$ , where $U = \{ U _ { i } ^ { k } \} _ { i = 1 , \mathrm { ~ \tiny ~ \dots ~ } , \mathrm { ~ \tiny ~ N } ; \mathrm { ~ \tiny ~ \xi ~ } k = 1 , \mathrm { ~ \tiny ~ \dots , ~ \mathrm { ~ \tiny ~ K } } } ; \Omega$ : the set of dominance relations between the alternatives, $\Omega \subseteq A \times A$ ; for example, $( a ^ { \prime } , a ) \in \varOmega$ means that alternative $\boldsymbol { a ^ { \prime } }$ is at least as preferable as alternative a.

With the assumption of preference independence under certain cases, an individual $k ' s$ aggregated utility associated with alternative $a _ { \mathrm { m } }$ is given as follows:

$$
V ^ {k} \left(a _ {\mathrm{m}}\right) = f \left(u _ {l} ^ {k} \left(a _ {\mathrm{m}}\right), \dots , u _ {n} ^ {k} \left(a _ {\mathrm{m}}\right)\right) = \sum_ {i = 1} ^ {N} w _ {i} u _ {i} ^ {k} \left(a _ {\mathrm{m}}\right).\tag{1}
$$

A group’s utility function associated on alternative $a _ { \mathrm { m } }$ becomes the following:

$$
V _ {\mathrm{G}} \left(a _ {\mathrm{m}}\right) = f \left(V ^ {1} \left(a _ {\mathrm{m}}\right), V ^ {2} \left(a _ {\mathrm{m}}\right), \dots , V ^ {K} \left(a _ {\mathrm{m}}\right)\right) = \sum_ {k = 1} ^ {K} w ^ {k} \sum_ {i = 1} ^ {N} w _ {i} u _ {i} ^ {k} \left(a _ {\mathrm{m}}\right).\tag{2}
$$

In our approach, we want to find the alternative $a ^ { * }$ that has the largest group utility value. It is difficult to find the most valuable alternative mathematically because of the incompleteness or fuzziness of parameters. As detailed in Section 2, many researchers suggest different methods to solve group decision problems under some assumptions of parameters. These assumptions include that individual weights, criteria weights, and individual utilities can be elicited directly from group members. In real world application it is difficult to get exact parameter values from group members. Therefore, it is necessary to suggest a method of preference aggregation and ranking conditions for group decision making using incomplete information on parameters.

## 3.1. Types of incomplete information

<sup>w</sup> <sup>x</sup> This section considers the type of information 15,17 $\psi ( a ^ { \prime } , a )$ employed as input data, and constraints in calculating utility ranges. Note here that it is crucial that group members be cognitively comfortable as they contribute their knowledge.

The types of $\psi ( a ^ { \prime } , a )$ provided by group members are linearly unequal constraints. By way of simple illustration, we present five types of $\Phi _ { w } \in \varPsi ( a ^ { \prime } , a )$ $U _ { i }$ also has five types as same as $\phi _ { _ w } . \mathrm { ~ } \phi _ { _ w }$ can be constructed by any combination of the following five types;

F1. a weak ranking: $\{ w _ { i } \geq w _ { i } \}$ , for $i \neq j ,$

F2. a strict ranking: $\{ w _ { i } - w _ { i } \ge \alpha _ { i } \} ,$

F3. a ranking with multiples: $\{ w _ { i } \ge \alpha _ { i } w _ { i } \}$

F4. an interval form: $\{ \alpha _ { i } \leq w _ { i } \leq \alpha _ { i } + \varepsilon _ { i } \}$

F5. a ranking of differences: $\{ w _ { i } - w _ { j } \geq w _ { k } - w _ { l } \} ,$ , for $j \neq k \neq l ,$

where $\{ \alpha _ { i } \}$ and $\{ \varepsilon _ { i } \}$ are non-negative constants. Further details can be found in Park and Kim 16 . <sup>w</sup> <sup>x</sup>

## 3.2. Basic concept of utility range approach

Group member $k ' s$ utility range for each alternative may be calculated by maximizing and minimizing each group member’s utility under constraint sets $U _ { i } ^ { k } ( \subset \varPsi ( a ^ { \prime } , a ) )$ ; these computations are calculated on each criterion. Representing individual utility values by ranges facilitates aggregation of individual utilities into a group’s utility. The interactive process requires each group member to compare his<sup>r</sup>her utility with others and to modify that utility to obtain an acceptable level of common preference. In such an interactive process, range-typed utility representation is more efficient than other representation methods.

<table><tr><td colspan="3">alternative  $a_m$  / criterion i</td></tr><tr><td>individual 1</td><td>group</td><td>individual 2</td></tr><tr><td>max  $u_i^1(a_m)$ </td><td></td><td>max  $u_i^2(a_m)$ </td></tr><tr><td>min  $u_i^1(a_m)$ </td><td>agreed range</td><td>min  $u_i^2(a_m)$ </td></tr><tr><td colspan="3">total range</td></tr></table>

Fig. 1. A preference aggregation method.

If individual utility is represented by ranges, the next step is to combine these ranges to find dominance relations of alternatives. By combining group members’ utility ranges into a common range of group preferences, group members attempt to reconcile differences of opinion by searching for consensus judgments <sup>w</sup> <sup>x</sup> 20 . In this research, we use two types of group utility ranges which are termed as total range and agreed range.

For example, we consider two DMs’ utility ranges of alternative $a _ { \mathrm { m } }$ on criterion $i ;$ the group’s agreed range and total range on criterion i are depicted in Fig. 1. The group’s agreed range is calculated by finding the Ž intersection of the utility ranges for all group members, max $\cdot _ { k }$ min $U _ { i } ^ { k }  u _ { i } ^ { k } ( a _ { \mathrm { m } } )$ , min max <sub>k</sub> $U _ { i } ^ { k } u _ { i } ^ { k } ( a _ { \mathrm { m } } ) )$ . The total range is the union of the utility value ranges.

The next step is to rank alternatives based on specific dominance rules with the group’s agreed ranges for all alternatives.

## 3.3. Pairwise dominance conditions under a single decision maker

Generally, pairwise dominance conditions with incomplete information considering a single DM’s preferences can be formulated as follows:

$$
z _ {\min} \left[ a ^ {\prime}, a, \Psi (a ^ {\prime}, a) \right] = \left\{ \begin{array}{l} \min z (a ^ {\prime}, a) = V (a ^ {\prime}) - V (a) = \sum_ {i = 1} ^ {N} w _ {i} \cdot \left[ u _ {i} (a ^ {\prime}) - u _ {i} (a) \right] \\ \text { subject   to } \Psi (a ^ {\prime}, a) \end{array} \right.\tag{3}
$$

In a single decision making context, it is said that $a ^ { \prime }$ strictly dominates a if and only if min $z ( a ^ { \prime } , a ) = 0$ <sup>w</sup> <sup>x</sup> 5,14,23,24 . Considering only strict dominance SD values sometimes fails to prioritize alternatives because ofŽ . fuzziness of parameter information. Further some loss of useful information occurs if otherwise used.

The necessary and sufficient condition requires that $a ^ { \prime }$ weakly dominates $^ { a , }$ is

$$
z _ {\min} \big [ a ^ {\prime}, a, \Psi (a ^ {\prime}, a) \big ] \geq z _ {\min} \big [ a, a, \Psi (a ^ {\prime}, a) \big ].
$$

Weak dominance WD implies minimizing regrets as traditionally defined 18,19,21 . Ž . <sup>w</sup> <sup>x</sup>

Based on these dominance conditions, we suggest pairwise dominance conditions for group decision making using the group’s agreed range obtained from the preference aggregation method set forth in Section 3.2.

## 4. Dominance conditions in utility range approach

## 4.1. Ranking conditions for the group decision making

The group’s pairwise comparison with incomplete information can be formulated as follows:

$$
\min z \left(a ^ {\prime} a\right) = V _ {\mathrm{G}} \left(a ^ {\prime}\right) - V _ {\mathrm{G}} (a) = \sum_ {i = 1} ^ {N} w _ {i} \sum_ {k = 1} ^ {K} w ^ {k} \left[ u _ {i} ^ {k} \left(a ^ {\prime}\right) - u _ {i} ^ {k} (a) \right]\tag{4}
$$

subject to $\psi ( a ^ { \prime } , a )$

In order to compare group’s aggregated utilities of alternatives, we suggest group’s pairwise dominance conditions using the group’s utility range. These conditions for SD are extended from a single decision making context to a group decision making situation considering the group’s utility range.

Property 1. Assume that the incomplete information of utility values for each criterion is functionally independent, and the group’s utility values are represented by its total range. Then the sufficient condition required that $a ^ { \prime }$ strictly dominates a for the group, is

$$
\min \sum_ {i} w _ {i} \left[ \min _ {k} \min _ {U _ {i} ^ {k}} u _ {i} ^ {k} \left(a ^ {\prime}\right) - \max _ {k} \max _ {U _ {i} ^ {k}} u _ {i} ^ {k} (a) \right] \geq 0.\tag{5}
$$

Proof. See Appendix A.

While Property 1 shows a dominance condition using the group’s total range, the following Property 2 considers the group’s agreed range. The group’s utility range, that is, the range of $u _ { i } ^ { \mathrm { G } } ( a )$ , is represented by Ž max min <sub>k</sub> ${ _ { U _ { i } ^ { k } } } u _ { i } ^ { k } ( a _ { \mathrm { m } } )$ , min max <sub>k</sub> $U _ { i } ^ { k } u _ { i } ^ { k } ( a _ { \mathrm { m } } ) )$ Ž . This range can be briefly represented by min $u _ { i } ^ { \mathrm { G } } ( a )$ , max $u _ { i } ^ { \mathrm { G } } ( a ) \dot { ) }$

Property 2. If incomplete information on utility values for each criterion is functionally independent, and the group’s utility values can be represented by the group’s agreed range, then the sufficient condition requiring that $a ^ { \prime }$ strictly dominates a for the group, is

$$
\min \sum_ {i} w _ {i} \left[ \max _ {k} \min _ {U _ {i} ^ {k}} u _ {i} ^ {k} \left(a ^ {\prime}\right) - \min _ {k} \max _ {U _ {i} ^ {k}} u _ {i} ^ {k} (a) \right] \geq 0.\tag{6}
$$

## Proof. See Appendix A.

To construct pairwise dominance relationships requires $( 2 K N + 1 ) M ( M - 1 )$ Ž .  LPs for solving Eqs. 5 and Ž . 6 , respectively. The difference between total and agreed ranges is reduced in the interactive iteration, but Property 1 shows a stronger dominance relation than Property 2. Because, if alternative $a ^ { \prime }$ strictly dominates a at total range, $a ^ { \prime }$ strictly dominates a at agreed range. But the reverse is not always true. Though these pairwise dominance rules are seemingly good, SD relations between alternatives rarely occur in the real world.

Instead of SD, a WD relationship is usually used between alternatives in the group decision making process. The WD means that we are trying to select the alternative that minimizes ‘regrets’. However WD on total range is meaningless, because the density of the aggregated group’s utility value $u _ { i } ^ { \mathrm { G } } ( a )$ in the total range is not uniform. That signifies WD relationship may be determined by an extreme value of a specific group member, if total range is used. By applying the basic logic of a WD condition in a single decision making context to a group decision making situation, we can suggest a WD condition for the group’s agreed range as in the following Property 3.

Property 3. Let $\begin{array} { r } { Z _ { \operatorname* { m i n } } ( a ^ { \prime } , a ) = \operatorname* { m i n } \Sigma _ { i } w _ { i } ^ { k } [ \operatorname* { m a x } _ { \boldsymbol { k } } \operatorname* { m i n } _ { U _ { i } ^ { k } } u _ { i } ^ { k } ( a ^ { \prime } ) - \operatorname* { m i n } _ { \boldsymbol { k } } \operatorname* { m a x } _ { U _ { i } ^ { k } } u _ { i } ^ { k } ( a ) ] } \end{array}$ and assume that the group’s utility value $u _ { i } ^ { \mathrm { G } } ( a )$ is a random variable with one-dimensional interval space of the group’s agreed range. Further assume the probability distribution function $f [ u _ { i } ^ { \mathrm { G } } ( a ) ]$ of $u _ { i } ^ { \mathrm { G } } ( a )$ is symmetric about a vertical axis through $u _ { i } ^ { \mathrm { G } } ( a ) = \mu ( a )$ Ž . Ž , where a <sup>s</sup> min $u _ { i } ^ { \mathrm { G } } ( a ) +$ max $u _ { i } ^ { \mathrm { G } } ( a ) ) / 2$ . Then the required sufficient condition that $a ^ { \prime }$ weakly dominates a for the group, is

$$
Z _ {\min} \left(a ^ {\prime}, a\right) \geq Z _ {\min} \left(a, a ^ {\prime}\right).\tag{7}
$$

## Proof. See Appendix A.

This property means that the alternative having the higher positioned range in the utility value is preferred to those in the lower range in order to minimize the degree of group regret. The WD condition can be used as a certain decision rule when we don’t get enough information to get a SD relationship from group members.

## 4.2. InteractiÕe procedure for ranking alternatiÕes IPRA with incomplete information( )

We suggest two interactive procedures to determine dominance relations between alternatives. In a context where group members share common criteria, we calculate the group’s utility ranges of each alternative for each criterion. If we cannot find the agreed range in the first iteration, then the group is considered to have inconsistent opinions. In order to overcome the inconsistency, we try to find a modified agreed range on which more individuals concur. We can obtain this modified agreed range by excluding one by one of those members having max min ${ } _ { U _ { i } ^ { k } } u _ { i } ^ { k } ( a )$ or $\begin{array} { r } { \operatorname* { m i n } _ { k } \operatorname* { m a x } _ { U _ { i } ^ { k } } u _ { i } ^ { k } ( a ) } \end{array}$ . To represent the degree of consensus for alternative a at criterion i, the value, $v _ { i } ( a )$ is defined as the ratio of the width of an agreed range to that of a total range. The $v _ { i } ( a )$ also indicates whether or not an agreed range exists for the group. If we cannot find a range having $v _ { i } ( a ) \geq \delta _ { i }$ after the above procedure, the procedure is repeated until a modified range with the value ranges of remaining group members is found. This procedure is not so extreme that it excludes the opinions of group members; it is merely a technique for providing more information about the opinions of the others. But, if group members agree on using total ranges for the alternatives not having the agreed ranges at the initial stage, we can use the total ranges instead of the modified agreed ranges.

## 4.2.1. InteractiÕe procedure for ranking alternatiÕes under the common criteria IPRA1 ( )

Step 1. Solve the following LPs to calculate individual utility range of each alternative on each criterion with group members’ incomplete information; min<sup>r</sup>max $u _ { i } ^ { k }$ subject to $U _ { i } ^ { k } \subset \varPsi ( a ^ { \prime } , a )$

Step 2. If $v _ { i } ( a ) \geq \delta _ { i }$ , then go to Step 4. Otherwise go to Step 3.

Step 3. Find the total range or modified agreed range for the criterion and the subset $S _ { \mathrm { m } } = \{ ( i , j ) |$ index of alternative and criterion not having the value of agreed range indicator above the threshold go to Step 5. 4

Step 4. Find the agreed range for the criterion.

Step 5. Continue Step 2–Step 4 for all criteria and alternatives.

Step 6. Find domination relations with Eqs. 5 – 7 in Section 4.2.Ž . Ž .

Step 7. Suggest an intermediate solution and constraints related to subset $S _ { \mathrm { m } } .$

Step 8. If all group members are satisfied with the solution, then stop. Otherwise, go to Step 2 with modified input.

The value $\delta _ { i }$ is referred to as the threshold of criterion i of each alternative that represents a certain degree of group consensus for that alternative on criterion i.

In contexts where each group member considers different criteria, we treat each group member’s criteria as separate dimensions in the joint representation. After calculating the individually aggregated value ranges of each alternative into $\left( \boldsymbol { Z } _ { \ast } \left( \boldsymbol { k } , \boldsymbol { a } \right) , \boldsymbol { Z } ^ { \ast } \left( \boldsymbol { k } , \boldsymbol { a } \right) \right) = \left( \operatorname* { m i n i m u m } _ { \mathrm { W } } \sum _ { i } w _ { i } ^ { k _ { \ast } } \left( \operatorname* { m i n } _ { U _ { i } ^ { k } } \boldsymbol { u } _ { i } ^ { k } ( \boldsymbol { a } ) \right) \right.$ , maximum $\_ { \mathrm { W } } \Sigma _ { i } w _ { i } ^ { k } \ast \left( \operatorname* { m a x } _ { U _ { l } ^ { k } } u _ { i } ^ { k } ( a ) \right)$ we find the agreed range for the alternative as $\begin{array} { r } { ( \operatorname* { m a x } _ { k } ~ Z _ { * } ( k , a ) . } \end{array}$ , min $\mathbf { \Sigma } _ { \cdot \cdot } ^ { \prime } \ Z ^ { * } ( k , a ) )$ . We already have the agreed ranges of alternatives considering the group members’ criteria, so a simpler dominance condition based on different criteria is needed to find dominance relations as follows:

Let $\begin{array} { r } { Z _ { \operatorname* { m i n } } ( \boldsymbol { a } , \boldsymbol { a } ^ { \prime } ) = \operatorname* { m a x } _ { \boldsymbol { k } } Z _ { * } \left( \boldsymbol { k } , \boldsymbol { a } \right) - \operatorname* { m i n } _ { \boldsymbol { k } } Z ^ { * } \left( \boldsymbol { k } , \boldsymbol { a } ^ { \prime } \right) } \end{array}$

If $Z _ { \operatorname* { m i n } } \left( a , a ^ { \prime } \right) \geq Z _ { \operatorname* { m i n } } \left( a ^ { \prime } , a \right)$ , then a weakly dominates $a ^ { \prime }$

Ž . 8

## 4.2.2. InteractiÕe procedure for ranking alternatiÕes under the different criteria IPRA2( )

Step 1. Solve the following LPs to calculate individual utility range of each alternative for each criterion with group members’ incomplete information; min<sup>r</sup>max $u _ { i } ^ { k }$ subject to $U _ { i } ^ { k } \subset \varPsi ( a ^ { \prime } , a )$

Step 2. Compute each member’s weighted value range for each alternative.

Step 3. If $v ( a ) \geq \delta$ , then go to Step 5. Otherwise go to Step 4.

Step 4. Find the total range or modified agreed range for the alternative and the subset $S = \{ j |$ index of alternative not having the value of agreed range indicator above threshold go to Step 6.4

Step 5. Find the agreed range for the alternative.

Step 6. Continue Step 2–Step 5 for all alternatives.

Step 7. Find domination relations using Eq. 8 . Ž .

Step 8. Suggest an intermediate solution and constraints related to subset S.

Step 9. If all group members are satisfied with the solution, then stop. Otherwise, go to Step 2 with modified input.

Ž . Ž In Step 3, Õ a is the degree of consensus for alternative a that is calculated by min $Z ^ { \ast } \left( k , a \right) - \operatorname* { m a x } _ { k }$ $\begin{array} { r } { Z ^ { \ast } \left( k , a \right) ) / ( \operatorname* { m a x } _ { k } ~ Z ^ { \ast } \left( k , a \right) - \operatorname* { m i n } _ { k } ~ Z ^ { \ast } \left( k , a \right) ) } \end{array}$

## 5. Database-oriented procedure for integrating the utility range approach

In group decision making contexts, it is important to find input information on conflicting opinions among group members, compare each member’s preferences with the others’, and suggest directions for reaching a consensus. Database oriented approaches to GDSS are often aimed at providing group members with individual views of the problem. These views contain a great deal of information relevant to other members and thus help group members reduce conflicting opinions.

## 5.1. Need for relational database

Since both the relational data model and MCDM methods typically present data to their users in the form of a table, where rows correspond to entities and columns correspond to properties, tables seem to be the most appealing multiple criteria decision support system data structure 10 . In general, relationships between<sup>w</sup> <sup>x</sup> relational tables and MCDM parameters can be easily established, and many MCDM researchers 8,9,22 have<sup>w</sup> <sup>x</sup> combined both concepts in their own systems. It is convenient to map rows in tables to alternatives and columns to criteria. However, there seems to exist only simple interaction between tables and approaches, such as the display of alternatives’ consequences on criteria; there is little attempt to integrate the data structure with their approaches in those systems.

In our system, we use these relations actively to provide group members with more information for reaching a consensus. For instance, whether new tables will be generated or not may be determined by a parameter in our procedure. A detailed procedure will be suggested in Section 5.2.

![](/api/attachments/QH6BAJRW/fulltext/images/68b73a18d42eac770fcb5362b6ee7610d38dba1254639bd38fc5086110553de1.jpg)  
Fig. 2. Interactive procedure with evolutionary database.

## 5.2. InteractiÕe aggregation using eÕolutionary database

In this paper we use a trigger rule for determining if deviation tables are to be generated. The trigger rule is intended to reduce the number of unnecessary tables. The evolutionary property of databases is implemented by the trigger rule and illustrated in Fig. 2.

## 5.2.1. InteractiÕe procedure for aggregating databases IPAD( )

We try to find the alternative about which there are the most disagreement and help the group reach a consensus by specifically discussing that alternative.

Step 1. Generate alternative a’s min<sup>r</sup>max table for all group members by solving the our formulation problem, where individual $k ' s$ table elements of alternative $\boldsymbol { a } ^ { \prime } \boldsymbol { s }$ range on criterion i are $Z _ { i * } ( k , a )$ and $Z ^ { i * } ( k , a )$ and table elements of the group agreed range for alternative a on criterion i are $Z _ { i * } ( G , a )$ and $Z ^ { i * } ( G , a )$

Step 2. Find the dominance relations between alternatives using IPRA1 or IPRA2.

Step 3. Calculate the total deviations from the range table for each alternative where, total deviation, $\begin{array} { r } { \mathrm { d } \boldsymbol { v } ^ { \mathrm { G } } = \sum _ { k } \mathrm { d } \boldsymbol { v } ^ { k } } \end{array}$ and the deviation of individual k means the degree dispersed from the group agreed range. These are calculated by following $\begin{array} { r } { \mathrm { i } v ^ { k } = \sum _ { i } \mathrm { d } v _ { i } ^ { k } = \sum _ { i } [ | Z _ { i * } ( k , a ) - Z _ { i * } ( G , a ) | + | Z ^ { i * } ( k , a ) - Z ^ { i * } ( G , a ) | ] } \end{array}$ for each alternative.

Step 4. Generate the above table for all alternatives.

Step 5. If the total deviation is less than the threshold for all alternatives, then stop. If the total deviation value is greater than the threshold value, then operate the projection to establish a deviation table for the t-th alternative where, elements in deviation tables for the over-deviated alternatives is of $( \mathrm { d } v ^ { k } ) _ { t }$ . This represents the individual $k ' s$ deviation of the t-th over-deviated alternative.

Step 6. Display a graph to represent the position of individual utility value ranges, and the group’s total ranges and agreed ranges.

Step 7. If at least one group member revises his<sup>r</sup>her previous assessments, then go to Step 1. Otherwise, determine dominance relations using the total ranges, and stop.

In Step 5, we operate the projection for the over-deviated alternatives in order to discover constraints that cause conflicting results. If the total deviation is less than the threshold for all alternatives, then a certain degree of consensus is reached. Therefore, it is unnecessary to operate the projection for yielding new tables and thus can save unneeded tables.

Table 1  
Husband’s utility value information

<table><tr><td></td><td>Safety</td><td>Cost</td><td>Attractiveness</td></tr><tr><td> $a_1$ </td><td> $u_1(a_1) \geq 0.5$ </td><td> $0.2 \leq u_2(a_1) \leq 0.7$  $u_2(a_2) \leq u_2(a_1)$ </td><td> $u_3(a_1) \geq 0.6$ </td></tr><tr><td> $a_2$ </td><td> $u_1(a_2) \geq 0.7$ </td><td> $u_2(a_1) - u_2(a_2) \leq u_2(a_3) - u_2(a_1)$ </td><td> $u_3(a_2) \geq 0.7$ </td></tr><tr><td> $a_3$ </td><td> $u_1(a_3) \leq u_1(a_1)$  $u_1(a_1) \leq u_1(a_2)$ </td><td> $u_2(a_3) \geq 0.5$  $u_2(a_1) \leq u_2(a_3)$ </td><td> $u_3(a_3) \geq 0.5$ </td></tr></table>

## 6. Car selection example

This section illustrates features of IPAD in the context of a modified example from White et al. 25 , in<sup>w</sup> <sup>x</sup> which a husband and wife wish to purchase a car from a group of three cars $( A = \{ a _ { 1 } , a _ { 2 } , a _ { 3 } \} )$ . The selection is to be based on three criteria: safety, cost and attractiveness. The information on the two members’ utility values is shown in Tables 1 and 2. For brevity, the group is assumed to be using the total range for an alternative not having an agreed range.

In the context of cars under consideration, the husband considers safety more important than cost, and cost more important than attractiveness. The wife feels that safety is more important than cost; and that cost is as important, but no more than two times as important as attractiveness. Under constraints on each member’s utility values, we calculate minimum and maximum values by solving 36 LP problems on each alternative and criterion as shown Table 3. The values in column $\Sigma ,$ representing each member’s aggregated ranges of alternatives, can be obtained by individually solving minimization and maximization LP problems of weightedsum under weights’ constraints.

## Case 1: Under the common criteria

Next, we can determine dominance relations between alternatives using Properties 2 or 3. For example, a dominance relation between alternative $a _ { 1 }$ and $a _ { 2 }$ is obtained by solving the following LP problem:

min $\begin{array} { r } { w _ { 1 } ( 0 . 8 - 0 . 7 ) + w _ { 2 } ( 0 . 5 - 0 . 6 ) + w _ { 3 } ( 0 . 8 - 0 . 9 ) } \end{array}$

## s.t. group member s weight s constraints

Similar LP formulations are applied to the remaining alternative pairs. As a result of solving the above LP problems, we get the values, $Z _ { \mathrm { m i n } } ( a ^ { \prime } , a )$ Ž .in Eq. 6 of Property 2 between all alternatives: $Z _ { \mathrm { m i n } } ( a _ { 1 } , a _ { 2 } ) = - 0 . 0 3$ $Z _ { \operatorname* { m i n } } ( a _ { 1 } , a _ { 3 } ) = 0 , Z _ { \operatorname* { m i n } } ( a _ { 2 } , a _ { 1 } ) = - 0 . 3 4 , Z _ { \operatorname* { m i n } } ( a _ { 2 } , a _ { 3 } ) = - 0 . 1 4 , Z _ { \operatorname* { m i n } } ( a _ { 3 } , a _ { 1 } ) = - 1$ , and $Z _ { \mathrm { m i n } } ( a _ { 3 } , a _ { 2 } ) = - 0 . 7$ . With these results we can determine that $a _ { 1 }$ dominates $a _ { 2 }$ and $a _ { 3 } ^ { \phantom { + } }$ , and $a _ { 3 }$ is dominated by $a _ { 2 }$ as an intermediate solution. We calculate the total deviation of all alternatives from the alternatives’ range table in order to check the degree of consensus. The total deviation of $a _ { 1 }$ is $\textstyle \sum _ { k } \sum _ { i } \mathrm { d } v _ { i } ^ { k } = 0 . 8 + 0 . 1 = 0 . 9$ $a _ { 2 }$ is 1.6, and $a _ { 3 }$ is 1.4. We require the modified information related to $a _ { 2 }$ having maximum deviation because we use a threshold of 1.5 in this example. We suggest to group members the intermediate solution and individual utility ranges together with constraints bringing conflict as in Fig. 3.

Table 2  
Wife’s utility value information

<table><tr><td></td><td>Safety</td><td>Cost</td><td>Attractiveness</td></tr><tr><td> $a_1$ </td><td> $u_1(a_1) \geq 0.8$ </td><td> $0.5 \leq u_2(a_1) \leq 0.8$ </td><td> $u_3(a_1) \geq 2u_3(a_3)$ </td></tr><tr><td> $a_2$ </td><td> $u_1(a_2) \leq 0.7$ </td><td> $0.3 \leq u_2(a_2) \leq 0.6$ </td><td> $0.6 \leq u_3(a_2) \leq 0.9$ </td></tr><tr><td> $a_3$ </td><td> $2u_1(a_3) \leq u_1(a_1)$ </td><td> $u_2(a_3) \leq u_2(a_1)$ </td><td> $0.4 \leq u_3(a_3) \leq 0.8$ </td></tr><tr><td></td><td></td><td> $u_2(a_3) \leq u_2(a_2)$ </td><td></td></tr></table>

Table 3  
The computed values of group members’ utility range

<table><tr><td rowspan="2">Members criteria</td><td></td><td colspan="4">Husband</td><td colspan="4">Wife</td></tr><tr><td></td><td>1</td><td>2</td><td>3</td><td> $\Sigma$ </td><td>1</td><td>2</td><td>3</td><td> $\Sigma$ </td></tr><tr><td rowspan="2"> $a_{1}$ </td><td>Min</td><td>0.5</td><td>0.2</td><td>0.6</td><td>0.35</td><td>0.8</td><td>0.5</td><td>0.8</td><td>0.5</td></tr><tr><td>Max</td><td>1</td><td>0.7</td><td>1</td><td>1</td><td>1</td><td>0.8</td><td>1</td><td>1</td></tr><tr><td rowspan="2"> $a_{2}$ </td><td>Min</td><td>0.7</td><td>0</td><td>0.7</td><td>0.35</td><td>0</td><td>0.3</td><td>0.6</td><td>0</td></tr><tr><td>Max</td><td>1</td><td>0.7</td><td>1</td><td>1</td><td>0.7</td><td>0.6</td><td>0.9</td><td>0.9</td></tr><tr><td rowspan="2"> $a_{3}$ </td><td>Min</td><td>0</td><td>0.5</td><td>0.5</td><td>0</td><td>0</td><td>0</td><td>0.4</td><td>0</td></tr><tr><td>Max</td><td>0.9</td><td>1</td><td>1</td><td>0.97</td><td>0.5</td><td>0.8</td><td>0.8</td><td>0.8</td></tr></table>

As shown in Fig. 3, we have no agreed range about $a _ { 2 }$ on the safety criterion and thus use total range to find dominance relations. In the second iteration, the wife wishes to substitute a constraint about the safety criterion, $u _ { 1 } ( a _ { 2 } ) = 0 . 7$ with the constraint that the utility difference between $a _ { 1 }$ and $a _ { 2 }$ on this criterion is less than or equal to 0.5. We perform a sensitivity analysis with newly modified input data and get a new range of $a _ { 2 }$ , 0.3, Ž 1 on both the safety criterion and the aggregation column, . . After running the second iteration, we get an agreed range 0.7, 1.0 forŽ . $a _ { 2 }$ and the total deviation for $a _ { 2 }$ is reduced into 1.0. The dominance relations are the same as in the first iteration; therefore the procedure stops because group members are satisfied with the results.

## Case 2: Under different criteria

We assume that the husband and wife consider different criteria, but the information on group members’ utilities is same as the common criteria case in Tables 1 and 2. The group members’ aggregated ranges, $\textstyle \sum$ of each alternative in Table 3 are used to determine dominance relations. The agreed ranges for alternatives $a _ { 1 } , \ a _ { 2 }$ and $a _ { 3 }$ are 0.5, 1 , 0.35, 0.9 and 0, 0.8 , respectively. We can establish the dominance relations betweenŽ . Ž . Ž . alternatives using condition 8 ;Ž . $a _ { 1 } \succ a _ { 2 } \succ a _ { 3 }$ . In the next step, deviation values for all alternatives are computed into 0.15 for $a _ { 1 } , 0 . 4 5$ for $a _ { 2 }$ and 0.17 for $a _ { 3 }$ . A second iteration is performed to reduce the total deviation for $a _ { 2 }$ . Assume that we obtain same modified information as in the common criteria case. As a result of the second iteration, the agreed range for $a _ { 2 }$ is changed to 0.35, 1.0 and the other ranges are identical to the first iteration.Ž . Additionally, the dominance relations are the same as those of the first iteration and a deviation value for $a _ { 2 }$ is reduced to 0.05. Therefore, we obtain the same dominance relations as in the common criteria problem.

<table><tr><td colspan="9">Graphic display of group members&#x27; value ranges</td></tr><tr><td colspan="3">Alternative 1</td><td colspan="3">Alternative 2</td><td colspan="3">Alternative 3</td></tr><tr><td>C1</td><td>C2</td><td>C3</td><td>C1</td><td>C2</td><td>C3</td><td>C1</td><td>C2</td><td>C3</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td>NO</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td colspan="4">Intermediate solution</td><td colspan="5">Constraints bringing conflict</td></tr><tr><td colspan="4">alternative 1 ➔ alternative 2 ➔ alternative 3</td><td colspan="5"> $u_{1}(a_{2}) \leq 0.7$  for wife $0.7 \leq u_{1}(a_{2})$  for husband</td></tr></table>

Fig. 3. Graphic display of value information after first iteration.

## 7. Conclusion and further study

We suggest interactive procedures for a utility range based preference aggregation method, and pairwise dominance conditions for MCGDM without knowing exact parameter values. Our procedures may be well suitable to situations in which we cannot determine group members’ importance weights and get exact criteria’s weights whether the same criteria are considered or not. This paper presents tools for implementing a GDSS, which would be a more reasonable approach in such a manner that decision makers can contribute their knowledge in cognitively comfortable views.

In further study, a modified procedure in which we can obtain group members’ weights is needed. We are now developing a multiple criteria group decision support system based on this integrated procedure.

## Appendix A

## A.1. Proof of Property 1

Ž . In Eq. 5 , min ${ } _ { \cdot k } \operatorname* { m i n } _ { U _ { i } ^ { k } } u _ { i } ^ { k } ( a ^ { \prime } )$ means the smallest value of group’s aggregated utility of alternative $a ^ { \prime }$ on criterion i and max max $\dot { \mathbf { \Omega } } _ { U _ { i } ^ { k } } u _ { i } ^ { k } ( a )$ means the largest value of the group’s aggregated utility of alternative a on criterion i.

It follows that min $\begin{array} { r } { \sum _ { i } w _ { i } [ u _ { i } ^ { \mathrm { G } } ( { a ^ { \prime } } ) - u _ { i } ^ { \mathrm { G } } ( { a } ) ] \geq 0 } \end{array}$ , because the value of $\begin{array} { r l } { \sum _ { i } w _ { i } [ u _ { i } ^ { \mathrm { G } } ( { a } ^ { \prime } ) - u _ { i } ^ { \mathrm { G } } ( { a } ) ] } \end{array}$ is equal to or greater than that of $\begin{array} { r } { \sum _ { i } w _ { i } \big [ u _ { i } ^ { \mathrm { G } } ( a ^ { \prime } ) - u _ { i } ^ { \mathrm { G } } ( a ) \big ] = V _ { \mathrm { G } } ( a ^ { \prime } ) - V _ { \mathrm { G } } ( a ) \geq 0 } \end{array}$

Ž . Therefore, if Eq. 5 is satisfied, $\begin{array} { r } { \sum _ { i } w _ { i } [ u _ { i } ^ { \mathrm { G } } ( a ^ { \prime } ) - u _ { i } ^ { \mathrm { G } } ( a ) ] = V _ { \mathrm { G } } ( a ^ { \prime } ) - V _ { \mathrm { G } } ( a ) = 0 } \end{array}$ and we can conclude that $a ^ { \prime }$ strictly dominates a for the group. Here, $u _ { i } ^ { \mathrm { G } } ( a )$ represents the group’s aggregated utility value of alternative a on criterion i.

## A.2. Proof of Property 2

Ž .Eq. 6 implies min $\textstyle \sum _ { i } w _ { i }$ <sup>w</sup> <sup>G</sup> Ž <sup>X</sup> . min u a <sup>y</sup> max $u _ { i } ^ { \mathrm { G } } ( a ) ] \geq 0$ by changing the notation. Thus, $\Sigma _ { i } w _ { \scriptscriptstyle i }$ <sup>w</sup> min $u _ { i } ^ { \mathrm { G } } ( a ^ { \prime } ) -$ max $u _ { i } ^ { \mathrm { G } } ( a ) ] \geq 0$

In other words, min ${ \textstyle \sum _ { i } { w _ { i } [ u _ { i } ^ { \mathrm { G } } ( a ^ { \prime } ) - u _ { i } ^ { \mathrm { G } } ( a ) ] \geq \sum _ { i } { w _ { i } [ \operatorname* { m i n } { \ u _ { i } ^ { \mathrm { G } } ( a ^ { \prime } ) - \operatorname* { m a x } { \ u _ { i } ^ { \mathrm { G } } ( a ) } ] } } } }$ , where $\begin{array} { r l } { \sum _ { i } { w _ { i } } [ u _ { i } ^ { \mathrm { G } } ( a ^ { \prime } ) - u _ { i } ^ { \mathrm { G } } ( a ) ] } \end{array}$ is the group’s aggregated value difference between alternative $a ^ { \prime }$ and a. So, $V _ { \mathrm { { G } } } ( a ^ { \prime } ) - V _ { \mathrm { { G } } } ( a ) = 0$ and $a ^ { \prime }$ strictly dominates a for group.

## A.3. Proof of Property 3

The group’s agreed range for the alternative a, $\begin{array} { r l } { { \operatorname* { \left( m a x \right)} _ { k } \operatorname* { m i n } _ { U _ { i } ^ { k } } u _ { i } ^ { k } ( a ) , \operatorname* { m i n } _ { k } \operatorname* { m a x } _ { U _ { i } ^ { k } } u _ { i } ^ { k } ( a )  } } & { { } } \end{array}$ can be briefly Ž represented by min $u _ { i } ^ { \mathrm { G } } ( a )$ , max $u _ { i } ^ { \mathrm { G } } ( a ) )$ .

Then $Z _ { \operatorname* { m i n } } ( a ^ { \prime } , a ) =$ min $\Sigma _ { i } w _ { i } [ \mathrm { m i }$ n $u _ { i } ^ { \mathrm { G } } ( a ^ { \prime } ) -$ max $u _ { i } ^ { \mathrm { G } } ( a ) ]$ and $Z _ { \mathrm { m i n } } ( a , a ^ { \prime } ) = \mathrm { m i n } \quad \Sigma _ { i } w _ { i } [ \mathrm { m i n } \quad u _ { i } ^ { \mathrm { G } } ( a )$ <sup>y</sup>max $u _ { i } ^ { \mathrm { G } } ( a ^ { \prime } ) ]$ Ž . Ž <sup>G</sup> Ž . <sub>i</sub>. From  a <sup>s</sup> min u a <sup>q</sup> max $u _ { i } ^ { \mathrm { G } } ( a ) ) / 2$ , min $u _ { i } ^ { \mathrm { G } } ( a ) = 2 \mu ( a ) -$ max $u _ { i } ^ { \mathrm { G } } ( a )$ . Similarly, min $u _ { i } ^ { \mathrm { G } } ( { a } ^ { \prime } )$

$$
\begin{array}{l} = 2 \mu (a ^ {\prime}) - \max u _ {i} ^ {\mathrm{G}} (a ^ {\prime}). \\ \text {The condition} Z _ {\min} (a ^ {\prime}, a) - Z _ {\min} (a, a ^ {\prime}) \\ Z _ {\min} (a ^ {\prime}, a) - Z _ {\min} (a, a ^ {\prime}) \\ = \min \sum_ {i} w _ {i} \big [ \min u _ {i} ^ {\mathrm{G}} (a ^ {\prime}) - \max u _ {i} ^ {\mathrm{G}} (a) \big ] - \min \sum_ {i} w _ {i} \big [ \min u _ {i} ^ {\mathrm{G}} (a) - \max u _ {i} ^ {\mathrm{G}} (a ^ {\prime}) \big ] \\ = \min \sum_ {i} w _ {i} \big [ 2 \mu (a ^ {\prime}) - \max u _ {i} ^ {\mathrm{G}} (a ^ {\prime}) - \max u _ {i} ^ {\mathrm{G}} (a) \big ] - \min \sum_ {i} w _ {i} \big [ 2 \mu (a) - \max u _ {i} ^ {\mathrm{G}} (a) - \max u _ {i} ^ {\mathrm{G}} (a ^ {\prime}) \big ] \\ = 2 \mu (a ^ {\prime}) + \min \sum_ {i} w _ {i} \big [ - \max u _ {i} ^ {\mathrm{G}} (a ^ {\prime}) - \max u _ {i} ^ {\mathrm{G}} (a) \big ] - 2 \mu (a) \\ - \min \sum_ {i} w _ {i} \big [ - \max u _ {i} ^ {\mathrm{G}} (a) - \max u _ {i} ^ {\mathrm{G}} (a ^ {\prime}) \big ] = 2 \big [ \mu (a ^ {\prime}) - \mu (a) \big ] \geq 0. \end{array}
$$

That is, $E U ( a ^ { \prime } ) - E U ( a ) \geq 0 .$

Therefore, we conclude that alternative $a ^ { \prime }$ weakly dominates alternative a if $Z _ { \mathrm { m i n } } ( a ^ { \prime } , a ) \geq Z _ { \mathrm { m i n } } ( a , a ^ { \prime } )$

## References

<sup>w</sup> <sup>x</sup>1 G. Anandalingam, A multiagent multiattribute approach for conflict resolution in acid rain impact mitigation, IEEE Trans. Syst. Man Cybern. 19 1989 1142–1153.Ž .

<sup>w</sup> <sup>x</sup> 2 T.X. Bui, M. Jarke, Communications design for Co-oP: a group decision support system, ACM Transactions on Office Information Systems 4 2 1986 81–103.Ž . Ž .

<sup>w</sup> <sup>x</sup> 3 J.J. Donovan, Database system approach to management decision support, ACM Transactions on Database Systems 1 4 1976 Ž . Ž . 344–369.

<sup>w</sup> <sup>x</sup> 4 J.S. Dyer, R.K. Sarin, Group preference aggregation rules based on strength of preference, Manage. Sci. 25 1979 822–832.Ž .

<sup>w</sup> <sup>x</sup> 5 P.C. Fishburn, Analysis of decisions with incomplete knowledge of probabilities, Operations Research 13 1965 217–237.Ž .

<sup>w</sup> <sup>x</sup>6 C.L. Hwang, M.J. Lin, Group Decision Making under Multiple Criteria: Lecture Notes in Economics and Mathematical Systems, Springer-Verlag, New York, 1986.

<sup>w</sup> <sup>x</sup> 7 M. Jarke, Knowledge sharing and negotiation support in multiperson decision support systems, Decision Support Systems 2 1986Ž . 93–102.

<sup>w</sup> <sup>x</sup> 8 M. Jarke, M.T. Jelassi, M.F. Shakun, MEDIATOR: towards a negotiation support system, EJOR 31 1987 314–334. Ž .

<sup>w</sup> <sup>x</sup> 9 M.T. Jelassi, A. Foroughi, Negotiation support systems: an overview of design issues and existing software, Decision Support Systems 5 1989 167–181.Ž .

<sup>w</sup> <sup>x</sup> 10 M.T. Jelassi, M. Jarke, E.A. Stohr, Designing a generalized multiple criteria decision support system, J. MIS 1 1985 24–43.Ž .

<sup>w</sup> <sup>x</sup> 11 R.L. Keeney, C.W. Kirkwood, Group decision making using cardinal social welfare function, Manage. Sci. 22 1975 430–437. Ž .

<sup>w</sup> <sup>x</sup> 12 R.L. Keeney, H. Raiffa, Decisions with Multiple Objectives: Preferences and Value Trade-offs, Wiley, New York, 1976.

<sup>w</sup> <sup>x</sup> 13 G.E. Kersten, NEGO-Group decision support system, Information and Management 8 1985 237–246. Ž .

<sup>w</sup> <sup>x</sup> 14 C.W. Kirkwood, R.K. Sarin, Ranking with partial information: a method and an application, Operations Research 33 1985 38–48. Ž .

<sup>w</sup> <sup>x</sup>15 E. Kofler, Z.W. Kmietowicz, A.D. Pearman, Decision making with linear partial information L.P.I. , J. Opl. Res. Soc. 35 1984Ž . Ž . 1079–1090.

<sup>w</sup> <sup>x</sup> 16 K.S. Park, S.H. Kim, Tools for interactive multiattribute decision making with incompletely identified information, EJOR 98 1997Ž . 111–123.

<sup>w</sup> <sup>x</sup> 17 K.S. Park, S.H. Kim, W.C. Yoon, Establishing strict dominance between alternatives with special type of incomplete information, EJOR 96 1996 398–406.Ž .

<sup>w</sup> <sup>x</sup> 18 A.D. Pearman, Establishing dominance in multiattribute decision making using an ordered metric method, J. Opl. Res. Soc. 44 1993Ž . 461–469.

<sup>w</sup> <sup>x</sup>19 A.D. Pearman, Z.W. Kmietowicz, Stochastic dominance with linear partial information, EJOR 23 1986 57–63.Ž .

<sup>w</sup> <sup>x</sup> 20 A.A. Salo, Interactive decision aiding for group decision support, EJOR 84 1995 134–149. Ž .

<sup>w</sup> <sup>x</sup> 21 R.K. Sarin, Screening of multiattribute alternatives, Omega 5 1977 481–489. Ž .

<sup>w</sup> <sup>x</sup> 22 R. Vetschera, Integrating databases and preference evaluations in group decision support: a feedback-oriented approach, Decision Support Systems 7 1991 67–77. Ž .

<sup>w</sup> <sup>x</sup> 23 M. Weber, Decision making with incomplete information, EJOR 28 1987 44–57. Ž .

<sup>w</sup> <sup>x</sup> 24 C.C. White, A.P. Sage, A multiple objective optimization-based approach to choice making, IEEE Trans. Syst. Man Cybern. 10 1980 Ž . 315–326.

<sup>w</sup> <sup>x</sup> 25 C.C. White, A.P. Sage, S. Dozono, A model of multiattribute decision making and trade-off weight determination under uncertainty, IEEE Trans. Syst. Man Cybern. 14 1984 223–229.Ž .

Soung Hie Kim is Professor of Graduate School of Management at the Korea Advanced Institute of Science and Technology KAIST . HeŽ . holds a BS from Seoul National University, and a MS from the University of Missouri-Columbia, and a PhD in Engineering–Economic Systems from Stanford University. His teaching and research specialties are in the fields of Decision Support Systems, Multicriteria Decision, Decision Theory, Group Decision Support Systems, CALS, and Business Reengineering. He has published numerous papers, which have appeared in European Journal of Operational Research, Journal of the Operational Research Society, NaÕal Research Logistics, Information and Decision Technologies, Technological Forecasting and Social Change, Expert Systems with Applications, Applied Artificial Intelligence, International Journal of Systems Sciences, etc.: Sang Hyun Choi is a Visiting Scholar of MIS Department at the University of Arizona. He received a PhD in Graduate School of Management from KAIST, his MS in Industrial Engineering from KAIST and his BS in Industrial Engineering from Hanyang University. His research interests are Decision Support Systems, Multicriteria Decision Making, Application of Decision Analytic Technique, Design and Development of Database Management System DBMS andŽ . Group Decision Support Systems. Byeong Seok Ahn is an Assistant Professor of Department of Business Administration and Accounting at Suwon University. He received his PhD in Graduate School of Management from KAIST, his MS in Management Science from KAIST and his BS in Applied Statistics from Yonsei University. His research interests include Multicriteria Decision Making, Intelligent Decision Support Systems, Managerial Evaluation based on OR, Group Decision Support Systems and Information System Analysis<sup>r</sup>Design.
