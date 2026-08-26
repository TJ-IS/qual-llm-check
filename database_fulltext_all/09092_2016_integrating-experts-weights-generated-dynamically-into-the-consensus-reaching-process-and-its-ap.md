---
otero_id: 9092
otero_key: "AYDDVEBC"
title: "Integrating experts' weights generated dynamically into the consensus reaching process and its applications in managing non-cooperative behaviors"
authors: "Yucheng Dong; Hengjie Zhang; Enrique Herrera-Viedma"
year: "2016"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2016.01.002"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Integrating experts' weights generated dynamically into the consensus reaching process and its applications in managing non-cooperative behaviors

Yucheng Dong <sup>a,</sup>⁎, Hengjie Zhang <sup>a</sup>, Enrique Herrera-Viedma <sup>b,c</sup>

<sup>a</sup> Business School, Sichuan University, Chengdu 610065, China

<sup>b</sup> Department of Computer Science and Artificial Intelligence, University of Granada, Granada 18071, Spain

<sup>c</sup> Department of Electrical and Computer Engineering, Faculty of Engineering, King Abdulaziz University, Jeddah 21589, Saudi Arabia

## a r t i c l e i n f o

Article history: Received 12 August 2015 Received in revised form 15 December 2015 Accepted 5 January 2016 Available online xxxx

Keywords: Group decision making Consensus reaching process Self-management mechanism Non-cooperative behaviors

## a b s t r a c t

The consensus reaching process (CRP) is a dynamic and iterative process for improving the consensus level among experts in group decision making. A large number of non-cooperative behaviors exist in the CRP. For example, some experts will express their opinions dishonestly or refuse to change their opinions to further their own interests. In this study, we propose a novel consensus framework for managing non-cooperative behaviors. In the proposed framework, a self-management mechanism to generate experts' weights dynamically is presented and then integrated into the CRP. This self-management mechanism is based on multi-attribute mutual evaluation matrices (MMEMs). During the CRP, the experts can provide and update their MMEMs regarding the experts' performances (e.g., professional skill, cooperation, and fairness), and the experts' weights are dynamically derived from the MMEMs. Detailed simulation experiments and comparison analysis are presented to justify the validity of the proposed consensus framework in managing the non-cooperative behaviors.

© 2016 Elsevier B.V. All rights reserved.

## 1. Introduction

Group decision making (GDM) [29,63] can be viewed as a task to find a collective solution to a decision problem in situations in which experts express their opinions regarding multiple alternatives. Usually, at the beginning of the GDM problem, the experts' opinions may differ substantially. The consensus reaching process (CRP) is often a necessity to achieve a general consensus regarding the selected alternatives in GDM [21,24]. Classically, consensus is defined as the full and unanimous agreement of all experts regarding all possible alternatives. However, this definition is inconvenient and complete agreement is not always necessary in real life. This belief has led to the use of a “soft” consensus level (i.e., consensus measure) [7,8,26,30,31,39,56]. Based on a “soft” consensus level, different types of CRPs have been proposed: (i) CRPs under different preference representation formats [10,13,15,17,28,35, 55]; (ii) CRPs with minimum adjustments or cost [5,6,12,16,22,23,66, 68,69]; (iii) CRPs based on consistency and consensus measures [18, 20,25,54,67]; (iv) CRPs that consider the attitudes of experts [38,45]; (v) CRPs under dynamic/Web contexts [1,2,32,43,65]; (vi) CRPs based on trust or experts' weights [4,42,53].

In GDM problems, a large number of non-cooperative behaviors exist. For example, some experts will express their opinions dishonestly or refuse to change their opinions to obtain their own interests. Hence, it is necessary to address non-cooperative behaviors to ensure the quality of the GDM results. In the extant literature, Pelta and Yager [41] and Yager [59,60] investigated the non-cooperative behaviors that are called strategic manipulation behaviors and occur in the aggregation function that is used in the selection process of GDM problems. Recently, Palomares et al. [40] proposed a consensus model for addressing noncooperative behaviors in the CRP of GDM problems, in which the weights of the experts who have the non-cooperative behaviors are compulsively penalized by a moderator. Although these approaches are very useful, they still need to be further improved to cope with non-cooperative behaviors in real-world GDM problems because (1) in the works of Pelta and Yager [41] and Yager [59,60], the noncooperative behaviors are considered solely in the selection process of GDM problems and are not considered in the CRP and (2) in the work of Palomares et al. [40], the management of the non-cooperative behaviors is heavily dependent on a moderator and is occasionally excessively demanding for the moderator.

Therefore, the objective of this study is to propose a novel consensus framework based on a self-management mechanism to manage noncooperative behaviors in the CRP. In this novel consensus framework, the experts provide not only preference information about alternatives but also mutual evaluation information for experts. The mutual evaluation information is given by means of multi-attribute mutual evaluation matrices (MMEMs). We propose an optimization-based approach to obtain the experts' weights from the MMEMs. Furthermore, the obtained experts' weights are integrated into the CRP. During the CRP, the experts not only modify their preference information about alternatives to achieve a consensus but also modify their MMEMs regarding experts' performances (e.g., professional skill, cooperation, and fairness). We propose detailed simulation experiments and a comparison analysis to justify the validity of the proposed consensus framework in managing non-cooperative behaviors.

The proposal with the self-management mechanism can be applied to address non-cooperative behaviors in the CRPs of practical GDM problems. When an academic conference committee wants to select a best paper or a science foundation committee hopes to find outstanding projects to support, some committee members may adopt non-cooperative behaviors to obtain their own interests; thus, the committees are confronted with the need to manage non-cooperative behaviors. The proposal provides a self-management mechanism to help the committees cope with the non-cooperative behaviors by using the means that the committee members provide and update their MMEMs in the multiple rounds of discussion.

The remainder of this study is arranged as follows. Section 2 introduces preliminaries. Then, Section 3 describes the consensus-based GDM with non-cooperative behaviors and proposes the resolution framework. Next, we apply the proposed consensus framework to manage non-cooperative behaviors in Section 4. Following this, in Section 5, an illustrative example is provided. Finally, concluding remarks are included in Section 6.

## 2. Preliminaries

This section introduces the basic knowledge regarding the ordered weighted average (OWA) operator, the additive preference relations (also called fuzzy preference relations), and the selection process to obtain the ranking of alternatives, which provide a basis for this study.

For a GDM problem, let $X { = } \{ x _ { 1 } , x _ { 2 } , { \ldots } , x _ { n } \}$ (n≥2) be a finite set of alternatives and $E { = } \{ e _ { 1 } , e _ { 2 } , { \ldots } , e _ { m } \} \left( m { \ge } 2 \right)$ be a set of experts. When experts express their opinions about alternatives, the preference representation formats are popular techniques. There are several different preference representation formats, including utility functions [51], preference orderings [47], multiplicative preference relations [46,48], additive preference relations [27,36,51], and linguistic preference relations [14,44,50]. Herrera-Viedma et al. [28] discussed the transformation functions among different preference representation formats. In this study, we assume that experts provide their opinions about alternatives by means of additive preference relations.

(1) OWA operator

Let $\{ c _ { 1 } , c _ { 2 } , . . . , c _ { N } \}$ be a set of values to aggregate. The OWA operator [57] is defined as

$$
O W A (c _ {1}, c _ {2}, \dots , c _ {N}) = \sum_ {k = 1} ^ {N} \pi_ {k} b _ {k}.\tag{1}
$$

where $b _ { k }$ is the kth largest value in $\{ c _ { 1 } , c _ { 2 } , . . . , c _ { N } \}$ , and $\pi =$ $( \pi _ { 1 } , \pi _ { 2 } , . . . , \pi _ { N } ) ^ { T }$ is an associated weight vector such that $\pi _ { k } \in [ 0 , 1 ]$ and $\textstyle \sum _ { k = 1 } ^ { N } \pi _ { k } = 1$

In [58], Yager suggested an effective method to compute $\pi =$ $( \pi _ { 1 } , \pi _ { 2 } , . . . , \pi _ { N } ) ^ { T }$ using linguistic quantifiers, which, in the case of a non-decreasing proportional quantifier Q [64], is given by the following expression:

$$
\pi_ {i} = Q \left(\frac {i}{N}\right) - Q \left(\frac {i - 1}{N}\right), i = 1, 2,..., l,\tag{2}
$$

where Q(c) can be represented as

$$
Q (c) = \left\{ \begin{array}{c c} 0, & c <   a \\ \frac {c - a}{b - a}, & a \leq c \leq b \\ 1, & c > b \end{array} \right.\tag{3}
$$

with $a , b , c \in [ 0 , 1 ] .$

There are several common linguistic quantifiers, such as all, most, at least half, and as many as possible, where the parameters (a,b) are (0,1), (0.3,0.8), (0,0.5), and (0.5,1), respectively. When a linguistic quantifier Q is used to compute the weights of the OWA operator, it is symbolized by $O W A _ { Q } .$

(2) Additive preference relations

Definition 1. Additive preference relations [36,51]. An additive preference relation on a set of alternatives $X = \{ x _ { 1 } , x _ { 2 } , \ldots , x _ { n } \}$ is represented by a matrix $P = ( p _ { i j } ) _ { n \times n } ,$ , where $p _ { i j } \in [ 0 , 1 ]$ denotes the preference degree of the alternative $x _ { i }$ over $x _ { j } .$ An additive preference relation is usually assumed to be additive reciprocal, i.e., $p _ { i j } + p _ { j i } = 1 , \forall i , j$

For simplicity, we call the additive preference relations the preference relations in this study. Let $\mathrm { P r } = ( p r _ { 1 } , p r _ { 2 } , . . . , p r _ { n } ) ^ { T }$ be the preference vector over alternatives X derived from the preference relation $P =$ $( p _ { i j } ) _ { n \times n } ,$ where $p r _ { i } \ge 0$ is the preference value of the alternative x . In this study, the quantifier-guided dominance degree QGDD is used to quantify the preference value of the alternative $x _ { i }$ as follows [28]:

$$
p r _ {i} = Q G D D _ {i} = O W A _ {Q} (p _ {i 1}, p _ {i 2}, \dots , p _ {i n}).\tag{4}
$$

(3) Selection process in GDM

The selection process which is used to obtain the ranking of alternatives from a group of preference relations consists of two phases [28]: aggregation and exploitation.

1) Aggregation phase

Let $P ^ { ( c ) } = ( p _ { i i } ^ { ( c ) } ) _ { n \times n }$ be a collective preference relation obtained by means of the aggregation of the individual preference relations $P ^ { ( k ) } = ( p _ { i i } ^ { ( k ) } ) _ { n \times n } ^ { \smile \sim } \bar { ( } k = 1 , 2 , \dots , m )$ . The weighted average (WA) operator and OWA operators are most widely used in GDM problems. This study integrates the experts' weights into the CRP; thus, we use the WA operator to implement the aggregation operation as follows:

$$
p _ {i j} ^ {(c)} = W A \left(p _ {i j} ^ {(1)}, p _ {i j} ^ {(2)},..., p _ {i j} ^ {(m)}\right) = \sum_ {k = 1} ^ {m} \lambda_ {k} p _ {i j} ^ {(k)}\tag{5}
$$

where $\lambda _ { k } \in [ 0 , 1 ]$ is weight of the expert $e _ { k } \in E$ and $\textstyle \sum _ { k = 1 } ^ { m } \lambda _ { k } = 1$ 2) Exploitation phase

Let $P r ^ { ( c ) } = ( \hat { p r } _ { 1 } ^ { ( c ) } , p r _ { 2 } ^ { ( c ) } , . . . , p r _ { n } ^ { ( c ) } ) ^ { T }$ be the collective preference vector over alternatives X derived from the collective preference relation $P ^ { ( c ) } = ( p _ { i j } ^ { ( c ) } ) _ { n \times n } ,$ where $p r _ { i } ^ { ( c ) } { \geq } 0$ is the collective preference value of the alternative $x _ { i \cdot }$ Based on Eq. (4), we can obtain $p r _ { i } ^ { ( c ) }$ , i.e.,

$$
p r _ {i} ^ {(c)} = Q G D D _ {i} ^ {(c)} = O W A _ {Q} \left(p _ {i 1} ^ {(c)}, p _ {i 2} ^ {(c)},..., p _ {i n} ^ {(c)}\right).\tag{6}
$$

Based on $P r ^ { ( c ) }$ , the collective ranking of the alternatives X can be obtained.

## 3. Consensus-based GDM with non-cooperative behaviors

This section describes the consensus-based GDM problem with noncooperative behaviors, and then proposes its resolution framework.

3.1. Decision problem and proposed framework

(1) Decision problem

As noted in Section 1, a large number of non-cooperative behaviors exist in the CRP. Here, we propose the consensus-based GDM problem with non-cooperative behaviors as follows:

Let $E = \{ e _ { 1 } , e _ { 2 } , \ldots , e _ { m } \}$ (m≥2) be a set of experts, $X = \{ x _ { 1 } , x _ { 2 } , \ldots , x _ { n } \}$ (n≥2) be a set of alternatives, and $P ^ { ( k ) } = ( p _ { i j } ^ { ( k ) } ) _ { n \times n } ^ { - } \left( k = 1 , 2 , . . . , m \right)$ be a preference relation provided by the expert $e _ { k } .$

Please cite this article as: Y. Dong, et al., Integrating experts' weights generated dynamically into the consensus reaching process and its applications in managing non-cooperative behaviors, Decision Support Systems (2016), http://dx.doi.org/10.1016/j.dss.2016.01.002

In the CRP, some experts may adopt non-cooperative behaviors to obtain their own interests. The question is how to help experts achieve a consensus in the GDM context with non-cooperative behaviors.

## (2) Proposed framework

Solving GDM problems follows a common resolution scheme com posed of two different processes (or models) [24,28]: consensus and selection. The consensus process includes two parts: consensus measure and feedback adjustment. By integrating the experts' weights generated dynamically into the consensus process, we propose a novel consensus framework. The implementation of the novel consensus framework addresses a three-process procedure. The details of the novel consensus framework are presented in Fig. 1.

## 1) Process of generating experts' weights

In the CRP, the experts provide and update their MMEMs regarding the experts' performances (e.g., professional skill, cooperation, and fairness). Then, an optimization-based approach is proposed to obtain the experts' weights from the MMEMs.

The process used to generate experts' weights is introduced in Section 3.2.

## 2) Consensus process

The objective of the consensus process is to improve the consensus level among the experts. The implementation of this consensus process involves a two-step procedure:

## (i) Consensus measure

In this step, a consensus measure method that incorporates experts' weights is introduced to measure the consensus level among the experts.

## (ii) Feedback adjustment

Based on consensus measure, the feedback adjustment rules are used to help experts modify their preference information to improve the consensus level among experts.

The details of the consensus process are introduced in Section 3.3.

## 3) Selection process

Once the consensus among experts is achieved, the selection process introduced in Section 2 is employed to derive the collective final ranking of alternatives.

## 3.2. Process of generating experts' weights

In this section, we propose an optimization-based method to obtain the experts' weights from the MMEMs.

In the CRP, the experts provide and update their MMEMs based on multiple attributes (e.g., professional skill, cooperation, and fairness). Let $A = \{ a _ { 1 } , a _ { 2 } , \ldots , a _ { l } \}$ (l≥1) be a set of attributes in the MMEMs. Let w= $( w _ { 1 } , w _ { 2 } , . . . , w _ { l } ) ^ { T }$ be weight vector over A, where $w _ { i } { \geq } 0$ and $\textstyle \sum _ { i = 1 } ^ { l } w _ { i } = 1$ Let $V ^ { ( k ) } = ( \nu _ { i j } ^ { ( k ) } ) _ { m \times l } \ : ( k = 1 , 2 , \dots , m )$ be a MMEM, where $\nu _ { i j } ^ { ( k ) }$ denotes the evaluation value that the expert e assigned to the expert e with respect to the attribute $a _ { j } .$ In this study, we assume that $\nu _ { i j } ^ { ( k ) } \mathrm { { \in } } \bar { [ 0 , 1 0 0 ] }$ for i≠k and $\nu _ { i j } ^ { ( k ) } { = } n u l l \mathrm { f o r } i { = } k$

Transform $V ^ { ( k ) } = [ \nu _ { i j } ^ { ( k ) } ] _ { m \times l } ~ ( k = 1 , 2 , \dots , m )$ into normalized $\overline { { \boldsymbol { V } } } ^ { ( k ) } =$ $\left[ \overline { { \nu } } _ { i j } ^ { ( k ) } \right] _ { m \times l }$ by using the following formulae [62]:

$$
\overline {{v}} _ {i j} ^ {(k)} = \frac {v _ {i j} ^ {(k)}}{\sum_ {i = 1 , i \neq k} ^ {m} v _ {i j} ^ {(k)}} (i \neq k), \text {   for   benefit   attribute   } a _ {j}, j = 1, 2,..., l\tag{7}
$$

$$
\overline {{v}} _ {i j} ^ {(k)} = \frac {\left(1 / v _ {i j} ^ {(k)}\right)}{\sum_ {i = 1 , i \neq k} ^ {m} \left(1 / v _ {i j} ^ {(k)}\right)} (i \neq k), \text {   for   cost   attribute   } a _ {j}, j = 1, 2,..., l\tag{8}
$$

![](/api/attachments/AYDDVEBC/fulltext/images/d27c72ed7a45d0e1347389e95d12ad31ecefea65d015272ce3112ffdce02b6fc.jpg)  
Fig. 1. Framework for GDM with non-cooperative behaviors

Please cite this article as: Y. Dong, et al., Integrating experts' weights generated dynamically into the consensus reaching process and its applications in managing non-cooperative behaviors, Decision Support Systems (2016), http://dx.doi.org/10.1016/j.dss.2016.01.002

Y. Dong et al. / Decision Support Systems xxx (2016) xxx–xxx

$\overline { { \nu } } _ { i j } ^ { ( k ) } = n u l l \ : ( i = k )$ ; for attribute $a _ { j } , \ j = 1 , 2 , . . . , l$

ð<sup>9</sup>Þ

Le $\lambda = ( \lambda _ { 1 } , \lambda _ { 2 } , \ldots , \lambda _ { m } ) ^ { T }$ be the vector of the experts' weights, where $\lambda _ { i } { \ge } 0$ is the weight of the expert e and $\sum _ { i = 1 } ^ { m } \lambda _ { i } = 1$ . The overall evaluation value of the expert $e _ { k }$ assigned to the expert $e _ { i }$ can be computed as $u _ { i } ^ { ( k ) } =$ $\textstyle \sum _ { j = 1 } ^ { l } w _ { j } { \overline { { \nu } } } _ { i j } ^ { ( k ) } . A$ larger $u _ { i } ^ { ( k ) }$ value indicates that the expert $e _ { k }$ believes the expert $e _ { i }$ is more important, and the deviation value between $u _ { i } ^ { ( k ) }$ and $\lambda _ { i }$ can be calculated as $( u _ { i } ^ { ( k ) } - \lambda _ { i } ) ^ { 2 }$ . The total deviation value between $u _ { i } ^ { ( k ) }$ and $\lambda _ { i }$ for all experts can be computed as $\sum _ { k = 1 } ^ { m } \sum _ { i = 1 } ^ { m } { ( u _ { i } ^ { ( k ) } - \lambda _ { i } ) } ^ { 2 }$ . Naturally, we hope that the total deviation value is as small as possible. In accordance with this idea, we construct a nonlinear programming model to determine the $\lambda = ( \lambda _ { 1 } , \lambda _ { 2 } , . . . , \lambda _ { l } ) ^ { T }$ as follows:

$$
\begin{array}{l} \min \sum_ {k = 1} ^ {m} \sum_ {i = 1} ^ {m} \left(\sum_ {j = 1} ^ {l} w _ {j} \overline {{v}} _ {i j} ^ {(k)} - \lambda_ {i}\right) ^ {2}. \\ s. t. \left\{ \begin{array}{l} \sum_ {i = 1} ^ {m} \lambda_ {i} = 1 \\ \lambda_ {i} \geq 0, (i = 1, 2,..., m) \end{array} \right. \end{array}\tag{10}
$$

Theorem 1. The optimal solution to model (10) is unique and can be given as follows:

$$
\lambda_ {i} = \frac {\sum_ {k = 1} ^ {m} \left(\sum_ {j = 1} ^ {l} w _ {j} \overline {{v}} _ {i j} ^ {(k)}\right)}{m} (i = 1, 2,..., m).\tag{11}
$$

The proof of Theorem 1 is included in Appendix A.

In the CRP, the experts update MMEMs based on the other experts' performances. Thus, the experts' weights derived from the MMEMs are dynamically changed.

## 3.3. Consensus process

Usually, the consensus process is used to help experts improve the consensus level among the experts [1,9,34,52]. There are two key elements in the consensus process: consensus measure and feedback adjustment.

(1) Consensus measure

Consensus levels are used to measure the current level of consensus in the CRP. Many consensus measure methods have been proposed [9, 37,39]. This section introduces the consensus measure method proposed by Palomares et al. [40].

The consensus levels are defined at three different levels: pair of alternatives, alternatives, and relations.

1) For each pair of experts $( e _ { k } , e _ { h } ) ( k { = } 1 , \ldots , m { - } 1 , h { = } k { + } 1 , \ldots , m ) ,$ a similarity matrix, $\bar { S } M ^ { ( k h ) } = ( s m _ { i j } ^ { ( k h ) } ) _ { n \times n } ,$ is defined as

$$
s m _ {i j} ^ {(k h)} = 1 - \left| p _ {i j} ^ {(k)} - p _ {i j} ^ {(h)} \right|.\tag{12}
$$

where sm $\boldsymbol { \mathbf { \mathit { i } } } _ { j } ^ { ( k h ) } \in [ 0 , 1 ]$ is the similarity level between experts $e _ { k }$ and $e _ { h }$ in their preference values $p _ { i j } ^ { ( k ) }$ and $p _ { i j } ^ { ( h ) }$

2) A consensus matrix $C M = ( c m _ { i j } ) _ { n \times n }$ is computed by aggregating similarity matrices, considering the importance weights $w _ { k h } \in [ 0 , 1 ]$ ] associated to each pair of experts $( e _ { k } , e _ { h } ) ( k = 1 , . . . , m - 1 , h =$ $k + 1 , \ldots , m )$ . In the work of Palomares et al. [40], the $w _ { k h }$ is computed as $w _ { k h } { = } \operatorname* { m i n } \left( w _ { k } , w _ { h } \right)$ . The element $c m _ { i j } { \in } [ 0 , 1 ] \ ( i { \neq } j )$ ) is the collective consensus level on the pair of alternatives (x<sub>i</sub>,x<sub>j</sub>), obtained by the following formula:

$$
c m _ {i j} = \frac {\sum_ {k = 1} ^ {m - 1} \sum_ {h = k + 1} ^ {m} w _ {k h} s m _ {i j} ^ {(k h)}}{\sum_ {k = 1} ^ {m - 1} \sum_ {h = k + 1} ^ {m} w _ {k h}}.\tag{13}
$$

3) Once the consensus matrix is computed, the consensus levels are computed at three different levels:

(i). Consensus level on a pair of alternatives $( x _ { i } , x _ { j } ) , c p _ { i j } = c m _ { i j } .$

(ii). Consensus level on alternative x , $c a _ { i } = \frac { \sum _ { j = 1 , j \neq i } ^ { n } c m _ { i j } } { n - 1 } .$ (iii). Collective consensus level,

$$
c l = \frac {\sum_ {i = 1} ^ {n} c a _ {i}}{n}.\tag{14}
$$

Obviously, $c l \in [ 0 , 1 ] . \operatorname { I f } c l = 1$ , then all experts are at full consensus. Otherwise, a larger cl value indicates a higher consensus level among experts.

(2) Feedback adjustment

Feedback adjustment aims to provide adjustment suggestions to help the experts improve the consensus level. Many feedback adjustment methods have been proposed [18,28,49]. Here, we introduce the feedback adjustment rules to help experts modify their preferences.

Let $P ^ { ( k ) } = ( p _ { i j } ^ { ( k ) } ) _ { n \times n } ( k = 1 , 2 , . . . , m )$ and $P ^ { ( c ) } = ( p _ { i j } ^ { ( c ) } ) _ { n \times n }$ be as before. Let $\overline { { P ^ { ( k ) } } } = ( \overline { { p _ { i j } ^ { ( k ) } } } ) _ { n \times n } ( k = 1 , 2 , \dots , m )$ be the adjusted preference relation associated with $P ^ { ( k ) }$ . When constructing $\overline { { P ^ { ( k ) } } } = \left[ p _ { i j } ^ { ( k ) } \right] _ { n \times n }$ , we suggest that

$$
\left\{ \begin{array}{l l} \overline {{p _ {i j} ^ {(k)}}} \in \Big [ \min \Big (p _ {i j} ^ {(k)}, p _ {i j} ^ {(c)} \Big),   \max \Big (p _ {i j} ^ {(k)}, p _ {i j} ^ {(c)} \Big) \Big ], & i f i \leq j \\ \overline {{p _ {i j} ^ {(k)}}} = 1 - \overline {{p _ {j i} ^ {(k)}}}, & i f i > j \end{array} \right.\tag{15}
$$

The detailed consensus process is presented in Algorithm I, which is provided in Appendix B.

## 4. Application of the proposed consensus framework to manage non-cooperative behaviors

In this section, we employ the proposed consensus framework to manage non-cooperative behaviors. Specifically, several noncooperative behaviors are introduced. Then, the detailed simulation methods and comparison analysis are designed to justify the validity of the proposed consensus framework in managing the non-cooperative behaviors.

## 4.1. Non-cooperative behaviors

The purpose of the CRP is to achieve a high level of agreement before making a decision. However, in a real-world CRP, some experts will express their preferences dishonestly or refuse to change their preferences to obtain their own interests. In the following, we introduce several non-cooperative behaviors.

(1) Non-cooperative behavior I

In the CRP, experts need to modify their individual preferences based on the suggestions received to achieve a consensus. However,

Please cite this article as: Y. Dong, et al., Integrating experts' weights generated dynamically into the consensus reaching process and its applications in managing non-cooperative behaviors, Decision Support Systems (2016), http://dx.doi.org/10.1016/j.dss.2016.01.002

Y. Dong et al. / Decision Support Systems xxx (2016) xxx–xxx

some experts will refuse to change their preferences or change their preferences by only a small fraction. In this study, we call this type of behavior non-cooperative behavior I.

Let $P ^ { ( k , z ) } = ( \bar { p } _ { i i } ^ { ( k , z ) } ) _ { n \times n } ( k = 1 , 2 , . . . , m )$ be a preference relation provided by the expert $e _ { k }$ in consensus round z.

Let

$$
d _ {i j} ^ {(k, z)} = \left\{ \begin{array}{c l} \left| p _ {i j} ^ {(k, z)} - p _ {i j} ^ {(k, z - 1)} \right|, & \text { if } p _ {i j} ^ {(k, z)} \in \Bigl [ \min \bigl (p _ {i j} ^ {(k, z - 1)}, p _ {i j} ^ {(c, z - 1)} \bigr), \max \bigl (p _ {i j} ^ {(k, z - 1)}, p _ {i j} ^ {(c, z - 1)} \bigr) \Bigr ] \\ 0, & \text { otherwise } \end{array} \right.\tag{16}
$$

$$
A D ^ {(k, z)} = \sum_ {i = 1} ^ {n} \sum_ {j = 1} ^ {n} d _ {i j} ^ {(k, z)},\tag{17}
$$

and

$$
D ^ {(k, z)} = \sum_ {i = 1} ^ {n} \sum_ {j = 1} ^ {n} \left| p _ {i j} ^ {(k, z - 1)} - p _ {i j} ^ {(c, z - 1)} \right|.\tag{18}
$$

where $d _ { i j } ^ { ( k , z ) }$ denotes the adjustment amount of expert $e _ { k }$ regarding the pair $( x _ { i } , \bar { x } _ { j } )$ according to Eq. $( 1 5 ) , A D ^ { ( k , z ) }$ denotes the total adjustment amount of expert $e _ { k }$ regarding all of the pairs $( x _ { i } , x _ { j } ) ( i , j = 1 , 2 , \ldots , n )$ , and $D ^ { ( k , z ) }$ denotes the total adjustment amount of expert $e _ { k }$ to achieve complete consensus over all of the pairs $( x _ { i } , x _ { j } ) \ ( i , j { = } 1 , 2 , . . . , n )$

Let

$$
s _ {1} ^ {(k, z)} = 1 - \frac {A D ^ {(k , z)}}{D ^ {(k , z)}}.\tag{19}
$$

The $\frac { A D ^ { ( k , z ) } } { D ^ { ( k , z ) } }$ value represents the degree to which expert $e _ { k }$ modifies his/her preferences and moves them closer to consensus, according to the advice received. Clearly, $s _ { 1 } ^ { ( k , z ) } \in [ 0 , 1 ]$ , and a larger $s _ { 1 } ^ { ( k , z ) }$ value indicates a higher probability of expert $e _ { k } ,$ who exhibits non-cooperative behavior I. Let α $( \alpha \in [ 0 , 1 ] )$ be the established threshold. $\mathrm { I f } \ \hat { s } _ { 1 } ^ { ( k , z ) } \geq \alpha ,$ we deduce that expert $e _ { k }$ satisfies the characteristic of the noncooperative behavior I in the consensus round z.

0:5 0:45 0:45 Example 1. Let Pð<sup>1;z−1</sup>Þ 0:55 0:5 0:4 and $P ^ { ( c , z - 1 ) } =$ 0:5 0:51 0:52 0:55 0:6 0:5 0:49 0:5 0:65 0:48 0:35 0:5

We assume that expert $e _ { 1 }$ provides the adjusted preference relation $P ^ { ( 1 , z ) }$ <sup>)</sup> as follows:

$$
P ^ {(1, z)} = \left( \begin{array}{c c c} 0. 5 & 0. 4 4 & 0. 4 8 \\ 0. 5 6 & 0. 5 & 0. 4 2 \\ 0. 5 2 & 0. 5 8 & 0. 5 \end{array} \right)
$$

Based on Eq. (16), we can obtain that $d _ { 1 2 } ^ { ( 1 , z ) } = 0 , d _ { 1 3 } ^ { ( 1 , z ) } = 0 . 0 3 , d _ { 2 1 } ^ { ( 1 , z ) } =$ $0 , \ d _ { 2 3 } ^ { ( 1 , z ) } = 0 . 0 \bar { 2 } , \ d _ { 3 1 } ^ { ( 1 , z ) } = 0 . 0 3$ , and $d _ { 3 2 } ^ { ( 1 , z ) } = 0 . 0 2$ . Using Eq. (17) and Eq. (18) yields $A { \stackrel { \smile } { D } } ^ { ( 1 , z ) } = 0 . 1$ and $D ^ { ( 1 , \overline { { { z } } } ) } = 0 . 7 6 ,$ respectively. Then, we can obtain that $s _ { 1 } ^ { ( 1 , z ) } = 0 . 8 6 8$ , according to Eq. (19). In this example, if we set $\alpha { = } 0 . 8$ , we will deduce that expert e satisfies the characteristic of the non-cooperative behavior I because $s _ { 1 } ^ { ( 1 , z ) } { > } \alpha$

(2) Non-cooperative behavior II

In the CRP, some experts will express their preferences dishonestly to obtain their own interests. A common dishonest behavior is that an expert decreases the evaluation for the collective most preferred alternative in the CRP. In this study, we call this type of behavior noncooperative behavior II.

Let $P r ^ { ( c , z - 1 ) } = ( p r _ { 1 } ^ { ( c , z - 1 ) } , p r _ { 2 } ^ { ( c , z - 1 ) } , \ldots , p r _ { n } ^ { ( c , z - 1 ) } ) ^ { T }$ be the preference vector that derived from $P ^ { ( c , z - 1 ) }$ according to Eq. (6). Let $\mathbf { \widehat { x } } _ { o } ^ { ( c , z - 1 ) }$ be the collective most preferred alternative based on $P r ^ { ( c , z - 1 ) }$ . Using Eq. (4) obtains the preference vector $P r ^ { ( k , z ) } = ( p r _ { 1 } ^ { ( k , z ) } , p r _ { 2 } ^ { ( k , z ) } , . . . , p r _ { n } ^ { ( k , z ) } ) ^ { T }$ $( k = 1 , 2 , \ldots , m )$ from $P ^ { ( k , z ) }$

Let

$$
O ^ {(k, z)} = \left(o ^ {(k, z)} (x _ {1}), o ^ {(k, z)} (x _ {2}),..., o ^ {(k, z)} (x _ {n})\right) ^ {T}\tag{20}
$$

be the preference ordering associated with $e _ { k } ,$ where $o ^ { ( k , z ) } ( x _ { i } )$ is the position of the alternative x in X according to $P r ^ { ( k , z ) }$ . For example, if $P r ^ { ( k , z ) } = ( 0 . 3 , 0 . 5 , 0 . 2 ) ^ { T } , O ^ { ( k , z ) } = ( 2 , 1 , 3 ) ^ { T } .$

$$
s _ {2} ^ {(k, z)} = \left\{ \begin{array}{l l} 1, & \text { if } o ^ {(k, z)} \Big (x _ {o} ^ {(c, z - 1)} \Big) > r o u n d (\beta \times n) \\ 0, & \text { otherwise } \end{array} \right.\tag{21}
$$

where the round is the usual rounding operation and $\beta ( \beta \in [ 0 , 1 ] )$ is a parameter. $\mathrm { I f } s _ { 2 } ^ { ( k , z ) } = 1$ , we deduce that expert $e _ { k }$ satisfies the characteristic of the non-cooperative behavior II in the consensus round z.

Example 2. Let $P ^ { ( 1 , z - 1 ) }$ and $P ^ { ( c , z - 1 ) }$ be as in Example 1. Suppose that expert $e _ { 1 }$ provides his/her adjusted preference relation $P ^ { ( 1 , z ) }$

$$
P ^ {(1, z)} = \left( \begin{array}{c c c} 0. 5 & 0. 4 9 & 0. 4 8 \\ 0. 5 1 & 0. 5 & 0. 4 8 \\ 0. 5 2 & 0. 5 2 & 0. 5 \end{array} \right).
$$

Using Eq. (6) yields the preference vector $P r ^ { ( c , z - 1 ) } =$ $( 0 . 5 0 3 3 , 0 . 4 9 3 3 , 0 . 4 3 6 7 ) ^ { T }$ from $P ^ { ( c , z - 1 ) }$ . Based on $P r ^ { ( c , z - 1 ) }$ , we have $\boldsymbol { x } _ { o } ^ { ( c , z - 1 ) } = \boldsymbol { x } _ { 1 }$ . According to $\operatorname { E q . } \left( 4 \right)$ and $\operatorname { E q . } \left( 2 0 \right)$ , we can obtain that $P r ^ { ( 1 , z ) } = ( 0 . 4 8 3 3 , 0 . 4 8 6 7 , \bar { 0 . 5 } 0 6 7 ) ^ { T }$ and $O ^ { ( 1 , z ) } \dot { = } \dot { ( } 3 , \dot { 2 } , 1 ) ^ { T }$ , respectively. In this example, if we set $\beta = 0 . 5 ,$ , we will deduce that expert $e _ { 1 }$ has the characteristic of the non-cooperative behavior II because $s _ { 2 } ^ { ( 1 , z ) } = 1$

(3) Non-cooperative behavior III

In the CRP, if there is an expert whose preference always has a significant difference from the remainder of the experts, we deduce that this expert has non-cooperative behavior III in this study.

Let

$$
s _ {3} ^ {(k, z)} = \frac {1}{(m - 1) (n ^ {2} - n)} \sum_ {h = 1, h \neq k} ^ {m} \sum_ {i = 1} ^ {n} \sum_ {j = 1} ^ {n} \left| p _ {i j} ^ {(k, z)} - p _ {i j} ^ {(h, z)} \right|.\tag{22}
$$

Clearly, $S _ { 3 } ^ { ( k , z ) } \in [ 0 , 1 ]$ and reflects the deviation of opinions between expert $e _ { k }$ with the other experts.

Let $\gamma ( \gamma \in [ 0 , 1 ] )$ be the established threshold. $\operatorname { I f } S _ { 3 } ^ { ( k , z ) } \geq \gamma ,$ we deduce that expert $e _ { k }$ satisfies the characteristic of non-cooperative behavior III in consensus round z.

Example 3. Let $P ^ { ( 1 , z ) }$ be as in Example 1. Le $\cdot P ^ { ( 2 , z ) } { = } \left( \begin{array} { c c c } { { 0 . 5 } } & { { 0 . 4 9 } } & { { 0 . 4 7 } } \\ { { 0 . 5 1 } } & { { 0 . 5 } } & { { 0 . 4 2 } } \\ { { 0 . 5 3 } } & { { 0 . 5 8 } } & { { 0 . 5 } } \end{array} \right)$ and $P ^ { ( 3 , z ) } = \left( { 0 . 1 2 0 . 5 0 . 9 } \right)$

Base on $\operatorname { E q . }$ (22), we can obtain that $s _ { 3 } ^ { ( 1 , z ) } = 0 . 2 1 6 7 , s _ { 3 } ^ { ( 2 , z ) } = 0 . 2 1$ and $s _ { 3 } ^ { ( 3 , z ) } = 0 . 4 0 6 \bar { 7 }$ . In this example, if we set $\gamma { = } 0 . 3 5$ , then we will deduce that expert e satisfies the characteristic of the non-cooperative behavior III because $S _ { 3 } ^ { ( 3 , z ) } > \gamma .$

Note 1. The parameters $\alpha , \beta ,$ and γ are used as thresholds to deduce whether experts' behaviors satisfy the characteristics of the noncooperative behaviors I–III, respectively. Larger $\alpha , \beta ,$ and γ values indicate the stricter criteria to deduce non-cooperative behaviors I–III, respectively. According to the actual situation, the experts can set $\alpha , \beta ,$ and γ values. When setting different $\alpha , \beta ,$ and γ values, the proposed consensus framework is effective for managing non-cooperative behaviors, as shown in the following simulation experiments and comparison analysis.

## 4.2. Simulation experiments

To study whether the proposed consensus framework can manage non-cooperative behaviors, this section presents detailed simulation methods.

In the simulation methods, we randomly generate the initial preference relations and MMEMs. The MMEMs involve three attributes: professional skill (a ), cooperation (a ), and fairness (a ). There are numerous approaches to set the attribute weights in multiple attribute decision making (e.g., [3,11,62]). In practical group decision situation, there are different types of non-cooperative behaviors, and we don't know which type of non-cooperative behaviors experts will use. In our consensus framework, each type of non-cooperative behaviors is managed by one or more attributes in MMEMs, so we set that the attribute weights are equal to effectively manage non-cooperative behaviors. In the following, Simulation methods I–III, which are based on the natural hypotheses 1–3, are presented, respectively.

Hypothesis 1. If an expert is deduced as using the non-cooperative behavior I, the other experts will decrease the evaluation of this expert regarding the attribute “cooperation $( a _ { 2 } ) . ^ { \prime }$

Hypothesis 2. If an expert is deduced as using the non-cooperative behavior II, the other experts will decrease the evaluation of this expert regarding the attribute “fairness (a ).”

Hypothesis 3. If an expert is deduced as using the non-cooperative behavior III, the other experts will decrease the evaluation of this expert regarding the attributes “professional skill $( a _ { 1 } ) "$ and “cooperation (a ).”

(1) Simulation experiment I

The main idea of Simulation method I is that we randomly generate the initial preference relations and MMEMs. In the CRP, if expert $e _ { k }$ is deduced as using the non-cooperative behavior I, then based on

Hypothesis 1, other experts e $( h = 1 , . . . , m , h \neq k )$ will decrease the evalu ation of expert $e _ { k }$ regarding the attribute “cooperation (a<sub>2</sub>).”

(2) Simulation experiment II

The basic idea of Simulation method II is similar to Simulation method I. If expert $e _ { k }$ is deduced as using the non-cooperative behavior II, based on Hypothesis 2, other experts $e _ { h } ( h { = } 1 , . . . , m , h { \neq } k )$ will decrease the evaluation of expert $e _ { k }$ regarding the attribute “fairness $( a _ { 3 } ) .$

(3) Simulation experiment II

The basic idea of Simulation method III is also similar to Simulation method I. If expert $e _ { k }$ is deduced as using the non-cooperative behavior III, based on Hypothesis 3, other experts $e _ { h } ( h { = } 1 , \ldots , m , h { \neq } k )$ will decrease the evaluation of expert $e _ { k }$ regarding the attributes “professional skill $\left( a _ { 1 } \right) ^ { \mathfrak { n } }$ and “cooperation $( a _ { 2 } ) . \ "$

Simulation methods I–III are included in Appendixes C, D, and E, respectively.

Note 2. In Simulation methods I–III, (1) the parameter z denotes the iteration number to achieve a consensus, and the parameter s reflects whether the predefined consensus level can be achieved or not; (2) the parameter θ (θ∈[0,1]) that is used in Steps 5, 5′, and $5 ^ { \prime \prime }$ denotes the penalty coefficient, and the larger the parameter θ value is, the larger the penalty strength will be; (3) the parameter r denotes the number of experts who adopt non-cooperative behaviors, and Steps 6, 6′, and 6″ can guarantee that experts $\{ e _ { 1 } , . . . , e _ { r } \}$ have non-cooperative behaviors I–III, respectively; (4) we use the OWA operator with the linguistic quantifier “as many as possible” to derive the preference vector from a preference relation.

## 4.3. Simulation results

Let $z _ { \mathrm { m a x } } = 5 ,$ and cl 0:85. When setting different input parameters m, n, α, θ, and r for Simulation methods I and setting different input parameters m, n, β, θ, and r for Simulation method II, we run these two simulation methods 1000 times to obtain the average values of s and

Average values of z and s in Simulation method I under different parameters.

<table><tr><td rowspan="2" colspan="3"></td><td colspan="6">r=1</td><td colspan="6">r=2</td><td colspan="6">r=3</td></tr><tr><td colspan="2">θ=0.2</td><td colspan="2">θ=0.4</td><td colspan="2">θ=0.6</td><td colspan="2">θ=0.2</td><td colspan="2">θ=0.4</td><td colspan="2">θ=0.6</td><td colspan="2">θ=0.2</td><td colspan="2">θ=0.4</td><td colspan="2">θ=0.6</td></tr><tr><td>m</td><td>n</td><td>α</td><td>z</td><td>s</td><td>z</td><td>s</td><td>z</td><td>s</td><td>z</td><td>s</td><td>z</td><td>s</td><td>z</td><td>s</td><td>z</td><td>s</td><td>z</td><td>s</td><td>z</td><td>s</td></tr><tr><td rowspan="6">5</td><td rowspan="3">5</td><td>0.5</td><td>2.332</td><td>1</td><td>2.202</td><td>1</td><td>1.986</td><td>1</td><td>3.156</td><td>1</td><td>2.899</td><td>1</td><td>2.466</td><td>1</td><td>4.497</td><td>0.821</td><td>3.912</td><td>1</td><td>3.368</td><td>1</td></tr><tr><td>0.65</td><td>2.421</td><td>1</td><td>2.300</td><td>1</td><td>2.132</td><td>1</td><td>3.321</td><td>0.988</td><td>3.012</td><td>1</td><td>2.645</td><td>1</td><td>4.577</td><td>0.712</td><td>4.125</td><td>0.852</td><td>3.801</td><td>1</td></tr><tr><td>0.8</td><td>2.625</td><td>1</td><td>2.432</td><td>1</td><td>2.211</td><td>1</td><td>3.413</td><td>0.976</td><td>3.225</td><td>1</td><td>2.792</td><td>1</td><td>4.693</td><td>0.645</td><td>4.411</td><td>0.845</td><td>4.055</td><td>0.927</td></tr><tr><td rowspan="3">7</td><td>0.5</td><td>2.351</td><td>1</td><td>2.115</td><td>1</td><td>1.998</td><td>1</td><td>3.048</td><td>1</td><td>2.792</td><td>1</td><td>2.401</td><td>1</td><td>4.655</td><td>0.729</td><td>3.757</td><td>1</td><td>3.580</td><td>1</td></tr><tr><td>0.65</td><td>2.461</td><td>1</td><td>2.222</td><td>1</td><td>2.106</td><td>1</td><td>3.201</td><td>0.992</td><td>3.123</td><td>1</td><td>2.655</td><td>1</td><td>4.675</td><td>0.681</td><td>4.210</td><td>0.821</td><td>3.715</td><td>1</td></tr><tr><td>0.8</td><td>2.656</td><td>1</td><td>2.442</td><td>1</td><td>2.323</td><td>1</td><td>3.322</td><td>0.985</td><td>3.285</td><td>1</td><td>2.825</td><td>1</td><td>4.854</td><td>0.589</td><td>4.555</td><td>0.830</td><td>4.275</td><td>0.872</td></tr><tr><td rowspan="6">7</td><td rowspan="3">5</td><td>0.5</td><td>1.992</td><td>1</td><td>1.875</td><td>1</td><td>1.767</td><td>1</td><td>2.432</td><td>1</td><td>2.276</td><td>1</td><td>1.976</td><td>1</td><td>2.975</td><td>1</td><td>2.755</td><td>1</td><td>2.452</td><td>1</td></tr><tr><td>0.65</td><td>2.162</td><td>1</td><td>1.992</td><td>1</td><td>1.843</td><td>1</td><td>2.655</td><td>1</td><td>2.456</td><td>1</td><td>2.245</td><td>1</td><td>3.332</td><td>1</td><td>3.178</td><td>1</td><td>2.845</td><td>1</td></tr><tr><td>0.8</td><td>2.253</td><td>1</td><td>2.145</td><td>1</td><td>2.138</td><td>1</td><td>2.867</td><td>1</td><td>2.672</td><td>1</td><td>2.575</td><td>1</td><td>3.519</td><td>0.995</td><td>3.389</td><td>1</td><td>3.126</td><td>1</td></tr><tr><td rowspan="3">7</td><td>0.5</td><td>2.002</td><td>1</td><td>1.864</td><td>1</td><td>1.705</td><td>1</td><td>2.295</td><td>1</td><td>2.001</td><td>1</td><td>1.977</td><td>1</td><td>2.967</td><td>1</td><td>2.701</td><td>1</td><td>2.554</td><td>1</td></tr><tr><td>0.65</td><td>2.156</td><td>1</td><td>1.997</td><td>1</td><td>1.854</td><td>1</td><td>2.489</td><td>1</td><td>2.247</td><td>1</td><td>2.012</td><td>1</td><td>3.290</td><td>1</td><td>3.079</td><td>1</td><td>2.799</td><td>1</td></tr><tr><td>0.8</td><td>2.345</td><td>1</td><td>2.152</td><td>1</td><td>2.028</td><td>1</td><td>2.755</td><td>1</td><td>2.557</td><td>1</td><td>2.452</td><td>1</td><td>3.501</td><td>1</td><td>3.312</td><td>1</td><td>3.099</td><td>1</td></tr><tr><td rowspan="6">9</td><td rowspan="3">5</td><td>0.5</td><td>1.967</td><td>1</td><td>1.743</td><td>1</td><td>1.684</td><td>1</td><td>2.245</td><td>1</td><td>1.989</td><td>1</td><td>1.879</td><td>1</td><td>2.675</td><td>1</td><td>2.345</td><td>1</td><td>2.201</td><td>1</td></tr><tr><td>0.65</td><td>2.002</td><td>1</td><td>1.878</td><td>1</td><td>1.701</td><td>1</td><td>2.379</td><td>1</td><td>2.224</td><td>1</td><td>2.078</td><td>1</td><td>2.804</td><td>1</td><td>2.654</td><td>1</td><td>2.476</td><td>1</td></tr><tr><td>0.8</td><td>2.084</td><td>1</td><td>1.921</td><td>1</td><td>1.798</td><td>1</td><td>2.516</td><td>1</td><td>2.398</td><td>1</td><td>2.275</td><td>1</td><td>2.931</td><td>1</td><td>2.828</td><td>1</td><td>2.719</td><td>1</td></tr><tr><td rowspan="3">7</td><td>0.5</td><td>1.962</td><td>1</td><td>1.754</td><td>1</td><td>1.601</td><td>1</td><td>2.289</td><td>1</td><td>1.981</td><td>1</td><td>1.856</td><td>1</td><td>2.654</td><td>1</td><td>2.445</td><td>1</td><td>2.300</td><td>1</td></tr><tr><td>0.65</td><td>1.994</td><td>1</td><td>1.865</td><td>1</td><td>1.704</td><td>1</td><td>2.487</td><td>1</td><td>2.312</td><td>1</td><td>2.221</td><td>1</td><td>2.879</td><td>1</td><td>2.652</td><td>1</td><td>2.425</td><td>1</td></tr><tr><td>0.8</td><td>2.112</td><td>1</td><td>1.994</td><td>1</td><td>1.890</td><td>1</td><td>2.772</td><td>1</td><td>2.644</td><td>1</td><td>2.523</td><td>1</td><td>3.081</td><td>1</td><td>2.866</td><td>1</td><td>2.692</td><td>1</td></tr><tr><td rowspan="6">11</td><td rowspan="3">5</td><td>0.5</td><td>2.097</td><td>1</td><td>1.992</td><td>1</td><td>1.843</td><td>1</td><td>2.356</td><td>1</td><td>2.278</td><td>1</td><td>1.948</td><td>1</td><td>2.643</td><td>1</td><td>2.432</td><td>1</td><td>2.005</td><td>1</td></tr><tr><td>0.65</td><td>2.194</td><td>1</td><td>2.078</td><td>1</td><td>1.996</td><td>1</td><td>2.477</td><td>1</td><td>2.411</td><td>1</td><td>2.192</td><td>1</td><td>2.894</td><td>1</td><td>2.612</td><td>1</td><td>2.441</td><td>1</td></tr><tr><td>0.8</td><td>2.208</td><td>1</td><td>2.100</td><td>1</td><td>2.001</td><td>1</td><td>2.642</td><td>1</td><td>2.621</td><td>1</td><td>2.332</td><td>1</td><td>3.010</td><td>1</td><td>2.812</td><td>1</td><td>2.600</td><td>1</td></tr><tr><td rowspan="3">7</td><td>0.5</td><td>1.999</td><td>1</td><td>1.855</td><td>1</td><td>1.810</td><td>1</td><td>2.408</td><td>1</td><td>2.178</td><td>1</td><td>1.989</td><td>1</td><td>2.702</td><td>1</td><td>2.525</td><td>1</td><td>2.375</td><td>1</td></tr><tr><td>0.65</td><td>2.079</td><td>1</td><td>1.927</td><td>1</td><td>1.900</td><td>1</td><td>2.555</td><td>1</td><td>2.467</td><td>1</td><td>2.301</td><td>1</td><td>2.844</td><td>1</td><td>2.671</td><td>1</td><td>2.471</td><td>1</td></tr><tr><td>0.8</td><td>2.215</td><td>1</td><td>2.098</td><td>1</td><td>1.999</td><td>1</td><td>2.874</td><td>1</td><td>2.770</td><td>1</td><td>2.599</td><td>1</td><td>3.171</td><td>1</td><td>2.967</td><td>1</td><td>2.821</td><td>1</td></tr></table>

Please cite this article as: Y. Dong, et al., Integrating experts' weights generated dynamically into the consensus reaching process and its applications in managing non-cooperative behaviors, Decision Support Systems (2016), http://dx.doi.org/10.1016/j.dss.2016.01.002

Y. Dong et al. / Decision Support Systems xxx (2016) xxx–xxx

Table 3  
Table 2  
Average values of z and s in Simulation method II under different parameters.

<table><tr><td rowspan="2" colspan="3"></td><td colspan="6">r=1</td><td colspan="6">r=2</td><td colspan="6">r=3</td></tr><tr><td colspan="2">θ=0.2</td><td colspan="2">θ=0.4</td><td colspan="2">θ=0.6</td><td colspan="2">θ=0.2</td><td colspan="2">θ=0.4</td><td colspan="2">θ=0.6</td><td colspan="2">θ=0.2</td><td colspan="2">θ=0.4</td><td colspan="2">θ=0.6</td></tr><tr><td>m</td><td>n</td><td>β</td><td>z</td><td>s</td><td>z</td><td>s</td><td>z</td><td>s</td><td>z</td><td>s</td><td>z</td><td>s</td><td>z</td><td>s</td><td>z</td><td>s</td><td>z</td><td>s</td><td>z</td><td>s</td></tr><tr><td rowspan="6">5</td><td rowspan="3">6</td><td>0.35</td><td>2.015</td><td>1</td><td>1.997</td><td>1</td><td>1.798</td><td>1</td><td>3.115</td><td>1</td><td>2.712</td><td>1</td><td>2.482</td><td>1</td><td>4.835</td><td>0.337</td><td>4.662</td><td>0.845</td><td>4.518</td><td>0.955</td></tr><tr><td>0.5</td><td>2.256</td><td>1</td><td>2.026</td><td>1</td><td>1.976</td><td>1</td><td>3.543</td><td>0.984</td><td>3.161</td><td>1</td><td>2.876</td><td>1</td><td>4.939</td><td>0.130</td><td>4.756</td><td>0.634</td><td>4.616</td><td>0.823</td></tr><tr><td>0.65</td><td>2.445</td><td>1</td><td>2.224</td><td>1</td><td>2.111</td><td>1</td><td>3.773</td><td>0.967</td><td>3.312</td><td>1</td><td>3.001</td><td>1</td><td>4.998</td><td>0.082</td><td>4.881</td><td>0.316</td><td>4.788</td><td>0.607</td></tr><tr><td rowspan="3">8</td><td>0.35</td><td>2.113</td><td>1</td><td>1.897</td><td>1</td><td>1.722</td><td>1</td><td>3.233</td><td>0.989</td><td>2.631</td><td>1</td><td>2.256</td><td>1</td><td>4.969</td><td>0.122</td><td>4.621</td><td>0.852</td><td>4.552</td><td>0.942</td></tr><tr><td>0.5</td><td>2.249</td><td>1</td><td>2.014</td><td>1</td><td>1.895</td><td>1</td><td>3.556</td><td>0.982</td><td>3.182</td><td>1</td><td>2.878</td><td>1</td><td>4.988</td><td>0.090</td><td>4.766</td><td>0.515</td><td>4.675</td><td>0.744</td></tr><tr><td>0.65</td><td>2.398</td><td>1</td><td>2.156</td><td>1</td><td>2.078</td><td>1</td><td>3.786</td><td>0.896</td><td>3.264</td><td>1</td><td>2.997</td><td>1</td><td>4.994</td><td>0.060</td><td>4.892</td><td>0.261</td><td>4.765</td><td>0.623</td></tr><tr><td rowspan="6">7</td><td rowspan="3">6</td><td>0.35</td><td>2</td><td>1</td><td>1.998</td><td>1</td><td>1.993</td><td>1</td><td>2.559</td><td>1</td><td>2.453</td><td>1</td><td>2.309</td><td>1</td><td>3.67</td><td>0.914</td><td>3.165</td><td>1</td><td>2.938</td><td>1</td></tr><tr><td>0.5</td><td>2.027</td><td>1</td><td>2</td><td>1</td><td>1.995</td><td>1</td><td>2.645</td><td>1</td><td>2.528</td><td>1</td><td>2.402</td><td>1</td><td>3.72</td><td>0.886</td><td>3.286</td><td>1</td><td>3.104</td><td>1</td></tr><tr><td>0.65</td><td>2.17</td><td>1</td><td>2.091</td><td>1</td><td>2</td><td>1</td><td>2.786</td><td>1</td><td>2.655</td><td>1</td><td>2.513</td><td>1</td><td>3.976</td><td>0.715</td><td>3.465</td><td>1</td><td>3.256</td><td>1</td></tr><tr><td rowspan="3">8</td><td>0.35</td><td>2.141</td><td>1</td><td>1.996</td><td>1</td><td>1.992</td><td>1</td><td>2.445</td><td>1</td><td>2.256</td><td>1</td><td>2.205</td><td>1</td><td>3.650</td><td>0.924</td><td>3.156</td><td>1</td><td>2.742</td><td>1</td></tr><tr><td>0.5</td><td>2.214</td><td>1</td><td>2.152</td><td>1</td><td>2.002</td><td>1</td><td>2.625</td><td>1</td><td>2.545</td><td>1</td><td>2.301</td><td>1</td><td>3.741</td><td>0.884</td><td>3.242</td><td>1</td><td>3.025</td><td>1</td></tr><tr><td>0.65</td><td>2.276</td><td>1</td><td>2.192</td><td>1</td><td>2.101</td><td>1</td><td>2.765</td><td>1</td><td>2.705</td><td>1</td><td>2.655</td><td>1</td><td>3.866</td><td>0.794</td><td>3.488</td><td>1</td><td>3.166</td><td>1</td></tr><tr><td rowspan="6">9</td><td rowspan="3">6</td><td>0.35</td><td>1.996</td><td>1</td><td>1.987</td><td>1</td><td>1.899</td><td>1</td><td>2.183</td><td>1</td><td>2.099</td><td>1</td><td>2.061</td><td>1</td><td>2.833</td><td>1</td><td>2.786</td><td>1</td><td>2.765</td><td>1</td></tr><tr><td>0.5</td><td>2.003</td><td>1</td><td>1.995</td><td>1</td><td>1.966</td><td>1</td><td>2.259</td><td>1</td><td>2.112</td><td>1</td><td>2.099</td><td>1</td><td>2.895</td><td>1</td><td>2.841</td><td>1</td><td>2.804</td><td>1</td></tr><tr><td>0.65</td><td>2.256</td><td>1</td><td>2.112</td><td>1</td><td>2.071</td><td>1</td><td>2.388</td><td>1</td><td>2.218</td><td>1</td><td>2.159</td><td>1</td><td>3.172</td><td>1</td><td>3.103</td><td>1</td><td>3</td><td>1</td></tr><tr><td rowspan="3">8</td><td>0.35</td><td>1.965</td><td>1</td><td>1.921</td><td>1</td><td>1.867</td><td>1</td><td>2.222</td><td>1</td><td>2.008</td><td>1</td><td>1.998</td><td>1</td><td>2.796</td><td>1</td><td>2.642</td><td>1</td><td>2.589</td><td>1</td></tr><tr><td>0.5</td><td>2.222</td><td>1</td><td>2.192</td><td>1</td><td>2.004</td><td>1</td><td>2.345</td><td>1</td><td>2.221</td><td>1</td><td>2.123</td><td>1</td><td>2.992</td><td>1</td><td>2.812</td><td>1</td><td>2.756</td><td>1</td></tr><tr><td>0.65</td><td>2.358</td><td>1</td><td>2.289</td><td>1</td><td>2.178</td><td>1</td><td>2.445</td><td>1</td><td>2.312</td><td>1</td><td>2.212</td><td>1</td><td>3.179</td><td>1</td><td>3.117</td><td>1</td><td>2.942</td><td>1</td></tr><tr><td rowspan="6">11</td><td rowspan="3">6</td><td>0.35</td><td>2.235</td><td>1</td><td>2.100</td><td>1</td><td>2.095</td><td>1</td><td>2.334</td><td>1</td><td>2.178</td><td>1</td><td>2.101</td><td>1</td><td>2.885</td><td>1</td><td>2.712</td><td>1</td><td>2.501</td><td>1</td></tr><tr><td>0.5</td><td>2.323</td><td>1</td><td>2.203</td><td>1</td><td>2.196</td><td>1</td><td>2.443</td><td>1</td><td>2.276</td><td>1</td><td>2.198</td><td>1</td><td>2.944</td><td>1</td><td>2.855</td><td>1</td><td>2.615</td><td>1</td></tr><tr><td>0.65</td><td>2.489</td><td>1</td><td>2.308</td><td>1</td><td>2.277</td><td>1</td><td>2.632</td><td>1</td><td>2.445</td><td>1</td><td>2.321</td><td>1</td><td>3.313</td><td>1</td><td>3.105</td><td>1</td><td>2.975</td><td>1</td></tr><tr><td rowspan="3">8</td><td>0.35</td><td>2.188</td><td>1</td><td>2.065</td><td>1</td><td>2.021</td><td>1</td><td>2.324</td><td>1</td><td>2.201</td><td>1</td><td>2.092</td><td>1</td><td>2.787</td><td>1</td><td>2.521</td><td>1</td><td>2.388</td><td>1</td></tr><tr><td>0.5</td><td>2.413</td><td>1</td><td>2.234</td><td>1</td><td>2.189</td><td>1</td><td>2.524</td><td>1</td><td>2.300</td><td>1</td><td>2.240</td><td>1</td><td>2.888</td><td>1</td><td>2.744</td><td>1</td><td>2.687</td><td>1</td></tr><tr><td>0.65</td><td>2.499</td><td>1</td><td>2.295</td><td>1</td><td>2.208</td><td>1</td><td>2.678</td><td>1</td><td>2.512</td><td>1</td><td>2.368</td><td>1</td><td>3.258</td><td>1</td><td>3.189</td><td>1</td><td>2.946</td><td>1</td></tr></table>

z. The average s and z value, respectively, reflect the success ratio and iteration number of achieving the established consensus level in the simulation experiments. The average values of s and z, under different input parameters for Simulation methods I and II, are listed in Tables 1 and 2, respectively.

Let $: z _ { \mathrm { m a x } } = 5 , \overline { { c l } } = 0 . 8 5 ,$ and r=1. When setting different input parameters m, γ, and θ for Simulation method III, we run this simulation method 1000 times, obtaining the average values of s and z. The obtained average values of s and z are listed in Table 3.

Furthermore, the average z values in Simulation methods I–III under different parameters are depicted in Figs. 2–4, respectively.

From Tables 1–3 and Figs. 2–4, we have the following observations:

(1) The proposed consensus framework can manage noncooperative behaviors I–III when setting different parameter values. Generally, it needs an average of 2–3 rounds to achieve a consensus, and it has high consensus success ratios (close to 1) for most cases.

(2) When the proportion of the experts who adopt non-cooperative behaviors increases to a certain level (approximately 30%–40%), the ability to manage non-cooperative behaviors of the proposed consensus framework will decrease.

(3) With decreasing α, β, and γ values or an increasing θ value, the average z value decreases, and the average s value increases. This finding implies that adopting the relaxed criteria to deduce the non-cooperative behaviors or using the strong penalty strength will accelerate the speed to achieve a consensus and will improve the success ratio of achieving a consensus.

## 4.4. Comparison analysis

In the proposed consensus framework, the experts' weights are dynamically updated and integrated into the CRP. However, in traditional CRPs, the experts' weights remain unchanged. In the following, we

Average values of z and s in Simulation method III under different parameters.

<table><tr><td rowspan="2">m</td><td rowspan="2">n</td><td rowspan="2"> $\gamma$ </td><td colspan="2"> $\theta=0.2$ </td><td colspan="2"> $\theta=0.4$ </td><td colspan="2"> $\theta=0.6$ </td><td rowspan="2">m</td><td rowspan="2">n</td><td rowspan="2"> $\gamma$ </td><td colspan="2"> $\theta=0.2$ </td><td colspan="2"> $\theta=0.4$ </td><td colspan="2"> $\theta=0.6$ </td></tr><tr><td>z</td><td>s</td><td>z</td><td>s</td><td>z</td><td>s</td><td>z</td><td>s</td><td>z</td><td>s</td><td>z</td><td>s</td></tr><tr><td rowspan="6">4</td><td rowspan="3">5</td><td>0.25</td><td>4.566</td><td>0.991</td><td>3.886</td><td>1</td><td>3.402</td><td>1</td><td>7</td><td>5</td><td>0.25</td><td>2.548</td><td>1</td><td>2.388</td><td>1</td><td>2.175</td><td>1</td></tr><tr><td>0.35</td><td>4.815</td><td>0.988</td><td>4.067</td><td>1</td><td>3.612</td><td>1</td><td></td><td></td><td>0.35</td><td>2.929</td><td>1</td><td>2.676</td><td>1</td><td>2.267</td><td>1</td></tr><tr><td>0.45</td><td>4.895</td><td>0.898</td><td>4.210</td><td>1</td><td>3.823</td><td>1</td><td></td><td></td><td>0.45</td><td>3.202</td><td>1</td><td>2.997</td><td>1</td><td>2.481</td><td>1</td></tr><tr><td rowspan="3">7</td><td>0.25</td><td>4.440</td><td>1</td><td>3.788</td><td>1</td><td>3.271</td><td>1</td><td></td><td>7</td><td>0.25</td><td>2.606</td><td>1</td><td>2.293</td><td>1</td><td>2.006</td><td>1</td></tr><tr><td>0.35</td><td>4.796</td><td>0.992</td><td>3.946</td><td>1</td><td>3.662</td><td>1</td><td></td><td></td><td>0.35</td><td>2.866</td><td>1</td><td>2.495</td><td>1</td><td>2.285</td><td>1</td></tr><tr><td>0.45</td><td>4.897</td><td>0.897</td><td>4.196</td><td>1</td><td>3.875</td><td>1</td><td></td><td></td><td>0.45</td><td>3.292</td><td>1</td><td>2.886</td><td>1</td><td>2.553</td><td>1</td></tr><tr><td rowspan="6">5</td><td rowspan="3">5</td><td>0.25</td><td>3.652</td><td>1</td><td>3.286</td><td>1</td><td>2.578</td><td>1</td><td>8</td><td>5</td><td>0.25</td><td>2.601</td><td>1</td><td>2.345</td><td>1</td><td>2.074</td><td>1</td></tr><tr><td>0.35</td><td>3.783</td><td>1</td><td>3.452</td><td>1</td><td>2.665</td><td>1</td><td></td><td></td><td>0.35</td><td>2.747</td><td>1</td><td>2.512</td><td>1</td><td>2.215</td><td>1</td></tr><tr><td>0.45</td><td>3.992</td><td>1</td><td>3.578</td><td>1</td><td>2.948</td><td>1</td><td></td><td></td><td>0.45</td><td>3.299</td><td>1</td><td>2.678</td><td>1</td><td>2.532</td><td>1</td></tr><tr><td rowspan="3">7</td><td>0.25</td><td>3.586</td><td>1</td><td>3.046</td><td>1</td><td>2.447</td><td>1</td><td></td><td>7</td><td>0.25</td><td>2.468</td><td>1</td><td>2.278</td><td>1</td><td>1.939</td><td>1</td></tr><tr><td>0.35</td><td>3.740</td><td>1</td><td>3.421</td><td>1</td><td>2.749</td><td>1</td><td></td><td></td><td>0.35</td><td>2.742</td><td>1</td><td>2.438</td><td>1</td><td>2.021</td><td>1</td></tr><tr><td>0.45</td><td>4.063</td><td>1</td><td>3.668</td><td>1</td><td>2.982</td><td>1</td><td></td><td></td><td>0.45</td><td>2.911</td><td>1</td><td>2.718</td><td>1</td><td>2.253</td><td>1</td></tr><tr><td rowspan="6">6</td><td rowspan="3">5</td><td>0.25</td><td>2.723</td><td>1</td><td>2.348</td><td>1</td><td>2.102</td><td>1</td><td>9</td><td>5</td><td>0.25</td><td>2.656</td><td>1</td><td>2.545</td><td>1</td><td>2.174</td><td>1</td></tr><tr><td>0.35</td><td>3.084</td><td>1</td><td>2.668</td><td>1</td><td>2.355</td><td>1</td><td></td><td></td><td>0.35</td><td>2.767</td><td>1</td><td>2.678</td><td>1</td><td>2.305</td><td>1</td></tr><tr><td>0.45</td><td>3.346</td><td>1</td><td>3.005</td><td>1</td><td>2.411</td><td>1</td><td></td><td></td><td>0.45</td><td>3.199</td><td>1</td><td>2.878</td><td>1</td><td>2.562</td><td>1</td></tr><tr><td rowspan="3">7</td><td>0.25</td><td>2.589</td><td>1</td><td>2.259</td><td>1</td><td>2.003</td><td>1</td><td></td><td>7</td><td>0.25</td><td>2.768</td><td>1</td><td>2.478</td><td>1</td><td>2.239</td><td>1</td></tr><tr><td>0.35</td><td>2.642</td><td>1</td><td>2.402</td><td>1</td><td>2.208</td><td>1</td><td></td><td></td><td>0.35</td><td>2.822</td><td>1</td><td>2.638</td><td>1</td><td>2.321</td><td>1</td></tr><tr><td>0.45</td><td>3.153</td><td>1</td><td>2.896</td><td>1</td><td>2.462</td><td>1</td><td></td><td></td><td>0.45</td><td>3.121</td><td>1</td><td>2.918</td><td>1</td><td>2.663</td><td>1</td></tr></table>

Please cite this article as: Y. Dong, et al., Integrating experts' weights generated dynamically into the consensus reaching process and its applications in managing non-cooperative behaviors, Decision Support Systems (2016), http://dx.doi.org/10.1016/j.dss.2016.01.002

![](/api/attachments/AYDDVEBC/fulltext/images/ca97e41478fd7ccd1e86453be3a1517e30201c746e5037d94952573804f36f58.jpg)

Y. Dong et al. / Decision Support Systems xxx (2016) xxx–xxx

(a) $m = 4$ $n = 5$ , r = 1  
![](/api/attachments/AYDDVEBC/fulltext/images/4bf22e7697a5e011d90f8c0695b408f843b1fbfd454ac01b411185aa6f15b239.jpg)  
(b) $m = 6$ , n = 6 , r = 2

![](/api/attachments/AYDDVEBC/fulltext/images/c2c334be4e8d37bedece659d044dc3e7cafe7ff33434ce092b527e921c24bf67.jpg)  
(c) $m = 8$ $n = 7$ $r = 3$

Fig. 2. Average z values in Simulation method I under different parameters θ and α (a) m=4, n=5, r=1; (b) m=6, n=6, r=2; (c) m=8, n=7, r=3.  
![](/api/attachments/AYDDVEBC/fulltext/images/58bb621fdb266cfe877624672daa4c5f3fbb59c784411b958af71523b83bba02.jpg)  
(a) $m = 4$ $n = 6$ , r = 1

![](/api/attachments/AYDDVEBC/fulltext/images/98f2b20652af69c3f256b3a3bb9d55f4f89b93143c9c9274f02fb32e670c8462.jpg)  
(b) $m = 6$ $n = 7$ , r = 2

![](/api/attachments/AYDDVEBC/fulltext/images/36a85cb839a0be61164b74528cc8d8e53efc2f5db0a104377a6f3e85588ee1a1.jpg)  
(c) $m = 8$ $n = 8$ $r = 3$  
Fig. 3. Average z values in Simulation method II under different parameters θ and β (a) m=4, n=6, r=1; (b) m=6, n=7, r=2; (c) m=8, n=8, r=3.

compare the proposed consensus framework with the traditional CRPs. In other words, we remove Steps 6, 6′, and 6″ from Simulation methods I–III and we obtain Simulation methods I′–III″ based on the traditional CRPs, respectively.

Let $\cdot n { = } 5 , z _ { \operatorname* { m a x } } { = } 5 , \overline { { c l } } { = } 0 . 9 , \theta { = } 0 . 2$ , and r=2. When setting different input parameters m and α for Simulation methods I and I′, we run these two simulation methods 1000 times, obtaining the average values of s and z. The average values z and s under Simulation methods I and I′ are described in Fig. 5.

(a) $m = 4$ $n = 5$ $r = 1$  
![](/api/attachments/AYDDVEBC/fulltext/images/df28fd7933196db8879c70586446b697f44f528911e99e40aa4e6bddd0796c7e.jpg)

Let $n = 5 , z _ { \mathrm { m a x } } = 5 , \overline { { c l } } = 0 . 9 , \theta = 0 . 2 ,$ , and r=2, and set different parameters m and β for Simulation methods II and II′. We run these two simulation methods 1000 times to obtain the average values of s and z. The average values z and s under Simulation methods II and II′ are described in Fig. 6.

![](/api/attachments/AYDDVEBC/fulltext/images/e416df369bc729c7ee8798fc9874a4879ebd62e0f0c39020995651231cdd764f.jpg)  
(b) $m = 6$ $n = 6$ , r = 1

![](/api/attachments/AYDDVEBC/fulltext/images/1b4dcd2ffaedee379a669a616b866c8e5dc4bc48ab8867638cd5c02d0864d623.jpg)  
(c) $m = 8$ $n = 7$ , r = 1  
Fig. 4. Average z values in Simulation method III under different parameters θ and γ (a) m=4, n=5, r=1; (b) m=6, n=6, r=1; (c) m=8, n=7, r=1.

Please cite this article as: Y. Dong, et al., Integrating experts' weights generated dynamically into the consensus reaching process and its applications in managing non-cooperative behaviors, Decision Support Systems (2016), http://dx.doi.org/10.1016/j.dss.2016.01.002

![](/api/attachments/AYDDVEBC/fulltext/images/a6f28670ffbfe7cbb6bf04e6ff11b981e348c7224026aaf2f8ad28d6988728f4.jpg)

![](/api/attachments/AYDDVEBC/fulltext/images/2c1c1c724de6f6d60226dc4cdfb7a535e955a54ffaa87e9dc6bbda237a30e6a3.jpg)  
Fig. 5. Average z and s values in Simulation methods I and I′ under different parameters m and α.

Let $n = 5 , z _ { \mathrm { m a x } } = 5 , \overline { { c l } } = 0 . 9 , \theta = 0 . 2 , \mathrm { a n d } r = 1$ . When setting different input parameters m and γ for Simulation methods III and III′, we run these two simulation methods III and III′ 1000 times to obtain the average values of s and z. The average values z and s under Simulation methods III and III′ are described in Fig. 7. In Figs. 5-7, SM is the abbreviation of the simulation method.

From Figs 5–7, we have the following observations:

(1) There are clearly fewer average consensus rounds in the proposed consensus framework than in the traditional CRP. This finding implies that the proposed consensus framework can accelerate the speed to achieve a consensus.

(2) The consensus success ratios in the proposed consensus framework are obviously higher than those in the traditional CRP. This finding means that the proposed consensus framework can improve the success ratio of achieving a consensus by managing the non-cooperative behaviors.

## 5. Illustrative example

To demonstrate our proposal, let us consider the example presented by Herrera-Viedma et al. [28]. In Herrera-Viedma et al.'s example, a set of eight experts $E = \{ e _ { 1 } , e _ { 2 } , \ldots , e _ { 8 } \}$ provide their preferences over a set of six alternatives $X = \{ x _ { 1 } , x _ { 2 } , \ldots , x _ { 6 } \}$ with different preference representation structures. By using transformation functions, these different preference representation structures are transformed into preference relations. These preference relation $P ^ { ( k ) } ( k = 1 , 2 , . . . , 8 )$ are listed below:

![](/api/attachments/AYDDVEBC/fulltext/images/9b50772763a077e808544aaa65d87f6b1c5c8edca46e18f22e2267fa2689860b.jpg)

$$
P ^ {(1)} = \left( \begin{array}{c c c c c c} 0. 5 & 0. 4 & 0. 6 & 0. 9 & 0. 7 & 0. 8 \\ 0. 6 & 0. 5 & 0. 7 & 1 & 0. 8 & 0. 9 \\ 0. 4 & 0. 3 & 0. 5 & 0. 8 & 0. 6 & 0. 7 \\ 0. 1 & 0 & 0. 2 & 0. 5 & 0. 3 & 0. 4 \\ 0. 3 & 0. 2 & 0. 4 & 0. 7 & 0. 5 & 0. 6 \\ 0. 2 & 0. 1 & 0. 3 & 0. 6 & 0. 4 & 0. 5 \end{array} \right),
$$

$$
P ^ {(2)} = \left( \begin{array}{c c c c c c} 0. 5 & 0. 7 & 0. 8 & 0. 6 & 1 & 0. 9 \\ 0. 3 & 0. 5 & 0. 6 & 0. 4 & 0. 8 & 0. 7 \\ 0. 2 & 0. 4 & 0. 5 & 0. 3 & 0. 7 & 0. 6 \\ 0. 4 & 0. 6 & 0. 7 & 0. 5 & 0. 9 & 0. 8 \\ 0 & 0. 2 & 0. 3 & 0. 1 & 0. 5 & 0. 4 \\ 0. 1 & 0. 3 & 0. 4 & 0. 2 & 0. 6 & 0. 5 \end{array} \right),
$$

$$
\begin{array}{l} P ^ {(3)} = \left( \begin{array}{c c c c c c} 0. 5 & 0. 6 9 & 0. 1 2 & 0. 2 & 0. 3 6 & 0. 9 \\ 0. 3 1 & 0. 5 & 0. 0 6 & 0. 1 & 0. 2 & 0. 8 \\ 0. 8 8 & 0. 9 4 & 0. 5 & 0. 6 4 & 0. 8 & 0. 9 8 \\ 0. 8 & 0. 9 & 0. 3 6 & 0. 5 & 0. 6 9 & 0. 9 7 \\ 0. 6 4 & 0. 8 & 0. 2 & 0. 3 1 & 0. 5 & 0. 9 4 \\ 0. 1 & 0. 2 & 0. 0 2 & 0. 0 3 & 0. 0 6 & 0. 5 \end{array} \right), \\ P ^ {(4)} = \left( \begin{array}{c c c c c c} 0. 5 & 0. 1 & 0. 3 6 & 0. 6 9 & 0. 1 6 & 0. 2 6 \\ 0. 9 & 0. 5 & 0. 8 4 & 0. 9 5 & 0. 6 2 & 0. 7 6 \\ 0. 6 4 & 0. 1 6 & 0. 5 & 0. 8 & 0. 2 5 & 0. 3 9 \\ 0. 3 1 & 0. 0 5 & 0. 2 & 0. 5 & 0. 0 8 & 0. 1 4 \\ 0. 8 4 & 0. 3 8 & 0. 7 5 & 0. 9 2 & 0. 5 & 0. 6 6 \\ 0. 7 4 & 0. 2 4 & 0. 6 1 & 0. 8 6 & 0. 3 4 & 0. 5 \end{array} \right), \end{array}
$$

![](/api/attachments/AYDDVEBC/fulltext/images/71224be9186f5540e09ec6bd4ddf2ffab29a3ac4cbde51871c04808e1e00910c.jpg)  
Fig. 6. Average z and s values in Simulation methods II and II′ under different parameters m and β.

Please cite this article as: Y. Dong, et al., Integrating experts' weights generated dynamically into the consensus reaching process and its applications in managing non-cooperative behaviors, Decision Support Systems (2016), http://dx.doi.org/10.1016/j.dss.2016.01.002

![](/api/attachments/AYDDVEBC/fulltext/images/0ebb47607e45b5cf20f5b8407a750fd24e53322111d2dcae900f41a1d516c812.jpg)

![](/api/attachments/AYDDVEBC/fulltext/images/509c754b0592583a1b726bfad96e946cba6168986e3c15e04d67e897d53720ac.jpg)  
Fig. 7. Average z and s values in Simulation methods III and III′ under different parameters m and $\gamma .$

$$
\begin{array}{l} P ^ {(5)} = \left( \begin{array}{c c c c c c} 0. 5 & 0. 5 5 & 0. 4 5 & 0. 2 5 & 0. 7 & 0. 3 \\ 0. 4 5 & 0. 5 & 0. 7 & 0. 8 5 & 0. 4 & 0. 8 \\ 0. 5 5 & 0. 3 & 0. 5 & 0. 6 5 & 0. 7 & 0. 6 \\ 0. 7 5 & 0. 1 5 & 0. 3 5 & 0. 5 & 0. 9 5 & 0. 6 \\ 0. 3 & 0. 6 & 0. 3 & 0. 0 5 & 0. 5 & 0. 8 5 \\ 0. 7 & 0. 2 & 0. 4 & 0. 4 & 0. 1 5 & 0. 5 \end{array} \right), \\ P ^ {(6)} = \left( \begin{array}{c c c c c c} 0. 5 & 0. 7 & 0. 7 5 & 0. 9 5 & 0. 6 & 0. 8 5 \\ 0. 3 & 0. 5 & 0. 5 5 & 0. 8 & 0. 4 & 0. 6 5 \\ 0. 2 5 & 0. 4 5 & 0. 5 & 0. 7 & 0. 6 & 0. 4 5 \\ 0. 0 5 & 0. 2 & 0. 3 & 0. 5 & 0. 8 5 & 0. 4 \\ 0. 4 & 0. 6 & 0. 4 & 0. 1 5 & 0. 5 & 0. 7 5 \\ 0. 1 5 & 0. 3 5 & 0. 5 5 & 0. 6 & 0. 2 5 & 0. 5 \end{array} \right), \end{array}
$$

$$
\begin{array}{l} P ^ {(7)} = \left( \begin{array}{c c c c c c} 0. 5 & 0. 3 4 & 0. 2 5 & 0. 8 2 & 0. 7 5 & 0. 8 7 \\ 0. 6 6 & 0. 5 & 0. 2 5 & 0. 1 8 & 0. 8 2 & 0. 9 1 \\ 0. 7 5 & 0. 7 5 & 0. 5 & 0. 9 4 & 0. 9 1 & 1 \\ 0. 1 8 & 0. 8 2 & 0. 0 6 & 0. 5 & 0. 3 4 & 0. 7 5 \\ 0. 2 5 & 0. 1 8 & 0. 0 9 & 0. 6 6 & 0. 5 & 0. 8 2 \\ 0. 1 3 & 0. 0 9 & 0 & 0. 2 5 & 0. 1 8 & 0. 5 \end{array} \right), \\ P ^ {(8)} = \left( \begin{array}{c c c c c c} 0. 5 & 0. 1 3 & 0. 1 8 & 0. 3 4 & 0. 7 5 & 0. 0 9 \\ 0. 8 7 & 0. 5 & 0. 6 6 & 0. 8 2 & 0. 9 1 & 0. 2 5 \\ 0. 8 2 & 0. 3 4 & 0. 5 & 0. 7 5 & 0. 8 7 & 0. 8 2 \\ 0. 6 6 & 0. 1 8 & 0. 2 5 & 0. 5 & 0. 7 5 & 0. 9 1 \\ 0. 2 5 & 0. 0 9 & 0. 1 3 & 0. 2 5 & 0. 5 & \text {   } \text {   } \text {   } \text {   } \text {   } \text {   } \text {   } \text {   } \text {   } \text {   } \text {   } \text {   } \text {   } \text {   } \text {   } \text {   } \text {   } \text {   } \text {   } \text {   } \text {   }\right). \end{array}
$$

In this example, we assume that three attributes, i.e., professional skill $\left( a _ { 1 } \right)$ , cooperation $\left( a _ { 2 } \right)$ , fairness $\left( a _ { 3 } \right)$ , are used in the MMEMs. The original MMEMs $V ^ { ( k ) } ( k = 1 , 2 , . . . , 8 )$ that the experts provided are listed in Tables 4-5:

$$
P ^ {(c)} = \left( \begin{array}{c c c c c c} 0. 5 & 0. 4 5 1 5 & 0. 4 3 8 5 & 0. 5 9 2 7 & 0. 6 2 7 3 & 0. 6 2 1 2 \\ 0. 5 4 8 5 & 0. 5 & 0. 5 4 4 8 & 0. 6 3 7 3 & 0. 6 1 8 5 & 0. 7 2 0 6 \\ 0. 5 6 1 5 & 0. 4 5 5 2 & 0. 5 & 0. 6 9 6 9 & 0. 6 7 8 8 & 0. 6 9 2 7 \\ 0. 4 0 7 3 & 0. 3 6 2 7 & 0. 3 0 3 1 & 0. 5 & 0. 6 0 8 1 & 0. 6 2 2 \\ 0. 3 7 2 7 & 0. 3 8 1 5 & 0. 3 2 1 2 & 0. 3 9 1 9 & 0. 5 & 0. 7 4 8 8 \\ 0. 3 7 8 9 & 0. 2 7 9 4 & 0. 3 0 7 3 & 0. 3 7 8 & 0. 2 5 1 2 & 0. 5 \end{array} \right).
$$

Table 4 MMEMs V<sup>(1)</sup>–V<sup>(4)</sup>.

<table><tr><td rowspan="2"></td><td colspan="3"> $V^{(1)}$ </td><td colspan="3"> $V^{(2)}$ </td><td colspan="3"> $V^{(3)}$ </td><td colspan="3"> $V^{(4)}$ </td></tr><tr><td> $a_1$ </td><td> $a_2$ </td><td> $a_3$ </td><td> $a_1$ </td><td> $a_2$ </td><td> $a_3$ </td><td> $a_1$ </td><td> $a_2$ </td><td> $a_3$ </td><td> $a_1$ </td><td> $a_2$ </td><td> $a_3$ </td></tr><tr><td> $e_1$ </td><td>null</td><td>null</td><td>null</td><td>80</td><td>89</td><td>94</td><td>85</td><td>93</td><td>92</td><td>80</td><td>92</td><td>87</td></tr><tr><td> $e_2$ </td><td>85</td><td>88</td><td>94</td><td>null</td><td>null</td><td>null</td><td>85</td><td>90</td><td>100</td><td>85</td><td>89</td><td>88</td></tr><tr><td> $e_3$ </td><td>90</td><td>96</td><td>87</td><td>85</td><td>92</td><td>93</td><td>null</td><td>null</td><td>null</td><td>90</td><td>88</td><td>89</td></tr><tr><td> $e_4$ </td><td>80</td><td>95</td><td>88</td><td>90</td><td>90</td><td>92</td><td>80</td><td>88</td><td>94</td><td>null</td><td>null</td><td>null</td></tr><tr><td> $e_5$ </td><td>95</td><td>93</td><td>86</td><td>80</td><td>92</td><td>91</td><td>85</td><td>89</td><td>85</td><td>85</td><td>89</td><td>90</td></tr><tr><td> $e_6$ </td><td>85</td><td>92</td><td>89</td><td>80</td><td>90</td><td>88</td><td>85</td><td>91</td><td>83</td><td>80</td><td>91</td><td>91</td></tr><tr><td> $e_7$ </td><td>85</td><td>91</td><td>92</td><td>85</td><td>90</td><td>89</td><td>85</td><td>87</td><td>82</td><td>85</td><td>92</td><td>90</td></tr><tr><td> $e_8$ </td><td>80</td><td>90</td><td>95</td><td>80</td><td>89</td><td>91</td><td>90</td><td>89</td><td>90</td><td>92</td><td>93</td><td>88</td></tr></table>

Using Eq. (5) provides the collective preference relation $P ^ { ( c ) }$

When constructing $P ^ { ( k , 1 ) } = ( p _ { i j } ^ { ( k , 1 ) } ) _ { n \times n } ~ ( k = 1 , 2 , \dots , 8 )$ , we suggest that

$$
\left\{ \begin{array}{l} p _ {i j} ^ {(k, 1)} = \Big [ \min \Big (p _ {i j} ^ {(k)}, p _ {i j} ^ {(c)} \Big),   \max \Big (p _ {i j} ^ {(k)}, p _ {i j} ^ {(c)} \Big) \Big ], i f i \leq j \\ p _ {i j} ^ {(k, 1)} = 1 - p _ {j i} ^ {(k, 1)}, \qquad \qquad \qquad \text { if } i > j \end{array} \right.
$$

Based on Eq. (14), we obtain that cl=0.6973.

The MMEMs in this round are equal to the original MMEMs, i.e., $V ^ { ( k , 1 ) } { = } V ^ { ( k ) } ( k { = } 1 , 2 , . . . , 8 ) ,$

In this example, let $\overline { { c l } } = 0 . 8 5 , \theta = 0 . 2 , \alpha = 0 . 8 , \beta = 0 . 5 , \mathrm { a n d } \gamma = 0 . 3 5$ When deriving a preference vector from a preference relation, we use the OWA operator with the linguistic quantifier “as many as possible.”

(1) In the first round, using Eq. (11) obtains the experts' weights from {V<sup>(1)</sup>, V<sup>(2)</sup>, ... , V<sup>(8)</sup>}. λ = (0.1252, 0.1256, 0.1263, 0.1248, 0.1244, 0.1245, 0.1233, 0.1259)<sup>T</sup>.

In the following, we use the proposed consensus framework to help experts achieve a consensus.

Table 5 MMEMs $V ^ { ( 5 ) } – V ^ { ( 8 ) } .$

<table><tr><td rowspan="2"></td><td colspan="3"> $V^{(5)}$ </td><td colspan="3"> $V^{(6)}$ </td><td colspan="3"> $V^{(7)}$ </td><td colspan="3"> $V^{(8)}$ </td></tr><tr><td> $a_1$ </td><td> $a_2$ </td><td> $a_3$ </td><td> $a_1$ </td><td> $a_2$ </td><td> $a_3$ </td><td> $a_1$ </td><td> $a_2$ </td><td> $a_3$ </td><td> $a_1$ </td><td> $a_2$ </td><td> $a_3$ </td></tr><tr><td> $e_1$ </td><td>82</td><td>91</td><td>90</td><td>81</td><td>100</td><td>97</td><td>85</td><td>90</td><td>91</td><td>86</td><td>85</td><td>84</td></tr><tr><td> $e_2$ </td><td>85</td><td>89</td><td>88</td><td>87</td><td>92</td><td>98</td><td>86</td><td>88</td><td>85</td><td>85</td><td>87</td><td>89</td></tr><tr><td> $e_3$ </td><td>92</td><td>92</td><td>89</td><td>90</td><td>93</td><td>89</td><td>84</td><td>89</td><td>84</td><td>90</td><td>84</td><td>88</td></tr><tr><td> $e_4$ </td><td>86</td><td>100</td><td>86</td><td>85</td><td>94</td><td>84</td><td>85</td><td>90</td><td>82</td><td>86</td><td>85</td><td>91</td></tr><tr><td> $e_5$ </td><td>null</td><td>null</td><td>null</td><td>84</td><td>89</td><td>85</td><td>86</td><td>92</td><td>86</td><td>84</td><td>84</td><td>92</td></tr><tr><td> $e_6$ </td><td>83</td><td>90</td><td>92</td><td>null</td><td>null</td><td>null</td><td>90</td><td>91</td><td>87</td><td>91</td><td>85</td><td>90</td></tr><tr><td> $e_7$ </td><td>86</td><td>88</td><td>91</td><td>85</td><td>88</td><td>86</td><td>null</td><td>null</td><td>null</td><td>83</td><td>83</td><td>88</td></tr><tr><td> $e_8$ </td><td>91</td><td>87</td><td>90</td><td>90</td><td>92</td><td>87</td><td>88</td><td>89</td><td>90</td><td>null</td><td>null</td><td>null</td></tr></table>

Please cite this article as: Y. Dong, et al., Integrating experts' weights generated dynamically into the consensus reaching process and its applications in managing non-cooperative behaviors, Decision Support Systems (2016), http://dx.doi.org/10.1016/j.dss.2016.01.002

Without loss of generality, based on the adjustment suggestions, the experts provided their adjusted preference relations $P ^ { ( k , 1 ) } \left( k = \right.$ $1 , 2 , . . . , 8 )$ , which are as follows:

$$
\begin{array} { l } P ^ { ( 1 , 1 ) } = \left( \begin{array} { c c c c c c } 0 . 5 & 0 . 4 0 4 3 & 0 . 5 9 4 2 & 0 . 8 8 4 3 & 0 . 6 9 9 7 & 0 . 7 6 7 \\ 0 . 5 9 5 7 & 0 . 5 & 0 . 6 7 1 1 & 0 . 9 8 8 1 & 0 . 7 6 6 6 & 0 . 8 7 1 5 \\ 0 . 4 0 5 8 & 0 . 3 2 8 9 & 0 . 5 & 0 . 7 9 0 9 & 0 . 6 0 4 1 & 0 . 6 9 8 9 \\ 0 . 1 1 5 7 & 0 . 0 1 1 9 & 0 . 2 0 9 1 & 0 . 5 & 0 . 3 0 4 & 0 . 4 3 4 1 \\ 0 . 3 0 0 3 & 0 . 2 3 3 4 & 0 . 3 9 5 9 & 0 . 6 9 6 & 0 . 5 & 0 . 6 2   _ { 1 } { \bf { m } } \\ \hline \textcolor [ t h ] { o m e n t a r i g ; t h e r m a t i o n } { o l u e d } & \textcolor [ t h ] { o l u e d } { o l u e d } { o l u e d } & \textcolor [ t h ] { o l u e d } { o l u e d } { o l u e d } & \textcolor [ t h ] { o l u e d } { o l u e d } { o l u e d } & \textcolor [ t h ] { o l u e d } { o l u e d } { o l u e d } & \textcolor     [ o l u e d ] { o l u e d } { o l u e d } \\ \hline \textcolor [ t h ] { o l u e d } { o l u e d } { o l u e d } & \textcolor [ t h ] { o l u e d } { o l u e d } { o l u e d } & \textcolor [ t h ] { o l u e d } { o l u e d } { o l u e d } & \textcolor [ t h ] { o l u ed } { o l u e d } { o l u e d } & \textcolor [ t h ] { o l u e d } { o l u e d } { o l u e d } & \textcolor     [ o l u e d ] { o l u e d } { o l u e d } \\ \hline P ^ { ( \mathrm{2,1}) } = \left( \begin{array} { c c c c c c } \textcolor [ t h ] { o l u e d }  \textcolor [ t h ] { o l u e d }  \textcolor [ t h ] { o l u e d }  \textcolor [ t h ] { o l u e d }  \textcolor [ t h ] { o l u e d }  \textcolor [ t h ] { o l u e d }  \textcolor [ t h ] { o l u e d }  \textcolor [ t h ]  o n t h i n s t a r i g i n t a r i g i n t a r i g i n t a r i g i n t a r i g i n t a r i g i n t a r i g i n t a r i g i n t a r i g i n t a r i g i n t a r i g i n t a r i g i n t a r i g i n t a r i g i n t a r i g i n t b a r i g i n t a r i g i n t a r i g i n t a r i g i n t a r i g i n t a r i g i n t a r i g i n t a r i g i n t a r i g i n t a r i g i n t a r i g i n t a r i g i n t a r i g i n t a r i g i n t a v e r f o r f o r f o r f o r f o r f o r f o r f o r f o r f o r f o r f o r f o r f o r f o r f o r f o r f o r f o r f o r f o r f o r f o r f o r f o r f o r f o r f o r f o r f o r f o r f o r f o r f o v e r f o r f o v e r f o v e r f o v e r f o v e r f o v e r f o v e r f o v e r f o v e r f o v e r f o v e r f o v e r f o v e r f o v e r f o v e r f o v e r f o v e r f o v e r f o v e r f o v e r f o v e r f o v w e r f o v w e w w w w w w w w w w w w w w w w w w w w w w w w w w w w w w w w w w w w w w w w w w w w w w w w w w w w w w w w w w w w w w w w w w w w w w w w w w w w w w w w w w w w w w w w w w w w w w w w w w w w \\ \textcolor [ t h ] { o l u e d }  \textcolor [ t h ] { o l u e d }  \textcolor [ t h ] { o l u e d }  \textcolor [ t h ] { o l u e d }  \textcolor [ t h ] { o l u e d }  \textcolor [ t h ] { o l u e d }  \textcolor [ t h ]  o p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p c m a x y z | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |
\end{array} \right) , \\ P ^ { ( \mathrm{3,1}) } = \left( \begin{array} { c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c } P ^ { ( \mathrm{4,1}) } = \left( \begin{array} { c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c } P ^ { ( \mathrm{4,1}) } = \left( \begin{array} { c c c c c} \textcolor [ t h ]  O L I N G E M S T H E M S T H E M S T H E M S T H E M S T H E M S T H E M S T H E M S T H E M S T H E M S T H E M S T H E M S T H E M S T H E M S T H E M S T H E M S T H E M S T H E M S T H E M S T H E M S T H E M S T I N W A N D I N D I N D I N D I N D I N D I N D I N D I N D I N D I N D I N D I N D I N D I N D I N D I N D I N D I N D I N D I N D I N D I N D I N D I N D I N D I N D I N D I N D I N D I N D I N D I N D I N D IN D I N D I N D I N D I N D I N D I N D I N D I N D I N D I N D I N D I N D I N D I N D I N D I N D I N D I N D I N D I N D I N D I N D I N D I N D I N D I N D I N D I N D I N D I N D I N D I N D I ND I N D I N D I N D I N D I N D I N D I N D I N D I N D I N D I N D I N D I N D I N D I N D I N D I N D I N D I N D I N D I N D I N D I N D I N D I N D I N D I N D I N D I N D I N D I N D I N D I N DI N D I N D I N D I N D I N DI N DI N DI N DI NDNIINNINNINNINNINNINNINNINNINNINNINNINNINNINNINNINNINNINNINNINNINNINNINNINNINNINNINNINNINNINNINNINNINNINNINNINNINNINNINNINNINNINNINNINNINNINNINNINNINNINNINMINTENNINTENNINTENNINTENNINTENNINTENNINTENNINTENNINTENNINTENNINTENNINTENNINTENNINTENNINTENNINTENNINTENNINTENNINTENNINTENNINTENNINTENNINTENNINTENNINTENNINTENNINTENNINTENNINTENNINTENNINTENNINTENNINTENNINTENNNTENNINTENNINTENNINTENNINTENNINTENNINTENNINTENNINTENNINTENNINTENNINTENNINTENNINTENNINTENNINTENNINTENNINTENNINTENNINTENNINTENNINTENNINTENNINTENNINTENNINTENNINTENNINTENNINTENNINTENNINTENNINTENNINTENNINTENTENTENTENTENTENTENTENTENTENTENTENTENTENTENTENTENTENTENTENTENTENTENTENTENTENTENTENTENTENTENTENTENTENTENTENTENTENTENTENTENTENTENTENTENTENTENTENTENTENTENTENTENTENTENTENTENTENTENTENTENTENTENTENTENTENTENTENTENTENTENTENTENTENTENTENTENTENTENTENTENTENTENTENTENTENTENTENTENTENTENTENTENTENTENTENTENTENTENTENTANTENTENTNTENTNTNTNTNTNTNTNTNTNTNTNTNTNTNTNTNTNTNTNTNTNTNTNTNTNTNTNTNTNTNTNTNTNTNTNTNTNTNTNTNTNTNTNTNTNTNTNTNTNTNTNTNTNTNTNTNTNTNTNTNTNTNTNTNTNTNTNTNTNTNTNTNTNTNTNTNTNTNTNTNTNTNTNTNTNTNTNTNTNTNTNTNTNTNTNTNTNTNTNTNTTMTTMTTMTTMTTMTTMTTMTTMTTMTTMTTMTTMTTMTTMTTMTTMTTMTTMTTMTTMTTMTTMTTMTTMTTMTTMTTMTTMTTMTTMTTMTTMTTMTTMTTMTTMTTMTTMTTMTTMTTMTTMTTMTTMTTMTTMTTMTTMTTMTTMTTATTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTGPTCTGPTCTGPTCTGPTCTGPTCTGPTCTGPTCTGPTCTGPTCTGPTCTGPTCTGPTCTGPTCTGPTCTGPTCTGPTCTGPTCTGPTCTGPTCTGPTCTGPTCTGPTCTGPTCTGPTCTGPTCTGPTCTGPTCTGPTCTGPTCTGPTCTGPTCTGPTCTGPTCTGPTCTTGPTCTTGPTCTTGPTCTTGPTCTTGPTCTTGPTCTTGPTCTTGPTCTTGPTCTTGPTCTTGPTCTTGPTCTTGPTCTTGPTCTTGPTCTTGPTCTTGPTCTTGPTCTTGPTCTTGPTCTTGPTCTTGPTCTTGPTCTTGPTCTTGPTCTTGPTCTTGPTCTTGPTCTTGPTCTTGPTCTTGPTCTTGPTCTTGPTCTTGTPSTTGTPSTTGTPSTTGTPSTTGTPSTTGTPSTTGTPSTTGTPSTTGTPSTTGTPSTTGTPSTTGTPSTTGTPSTTGTPSTTGTPSTTGTPSTTGTPSTTGTPSTTGTPSTTGTPSTTGTPSTTGTPSTTGTPSTTGTPSTTGTPSTTGTPSTTGTPSTTGTPSTTGTPSTTGTPSTTGTPSTTGTPSTTGTPSTTGTPST TGTPSTTGTPSTTGTPSTTGTPSTTGTPSTTGTPSTTGTPSTTGTPSTTGTPSTTGTPSTTGTPSTTGTPSTTGTPSTTGTPSTTGTPSTTGTPSTTGTPSTTGTPSTTGTPSTTGTPSTTGTPSTTGTPSTTGTPSTTGTPSTTGTPSTTGTPSTTGTPSTTGTPSTTGTPSTTGTPSTTGTPSTTGTPSTTGTPSTTGFPSTTGFPSTTGFPSTTGFPSTTGFPSTTGFPSTTGFPSTTGFPSTTGFPSTTGFPSTTGFPSTTGFPSTTGFPSTTGFPSTTGFPSTTGFPSTTGFPSTTGFPSTTGFPSTTGFPSTTGFPSTTGFPSTTGFPSTTGFPSTTGFPSTTGFPSTTGFPSTTGFPSTTGFPSTTGFPSTTGFPSTTGFPSTTGFPSTTGFP STGFP STGFP STGFP STGFP STGFP STGFP STGFP STGFP STGFP STGFP STGFP STGFP STGFP STGFP STGFP STGFP STGFP STGFP STGFP STGFP STGFP STGFP STGFP STGFP STGFP STGFP STGFP STGFP STGFP STGFP STGFP STGFP STGFP STGFRSUSUSUSUSUSUSUSUSUSUSUSUSUSUSUSUSUSUSUSUSUSUSUSUSUSUSUSUSUSUSUSUSUSUSUSUSUSUSUSUSUSUSUSUSUSUSUSUSUSUSUSUSUSUSUSUSUSUSUSUSUSUSUSUSUSUSUSUSUSUSUSS USUSS USUSS USUSS USUSS USUSS USUSS USUSS USUSS USUSS USUSS USUSS USUSS USUSS USUSS USUSS USUSS USUSS USUSS USUSS USUSS USUSS USUSS USUSS USUSS USUSS USUSS USUSS USUSS USUSS USUSS USUSS USUSS USUSS US USS USUSS USUSS USUSS USUSS USUSS USUSS USUSS USUSS USUSS USUSS USUSS USUSS USUSS USUSS USUSS USUSS USUSS USUSS USUSS USUSS USUSS USUSS USUSS USUSS USUSS USUSS USUSS USUSS USUSS USUSS USUSS USUSS USUss Uss Uss Uss Uss Uss Uss Uss Uss Uss Uss Uss Uss Uss Uss Uss Uss Uss Uss Uss Uss Uss Uss Uss Uss Uss Uss Uss Uss Uss Uss Uss Uss Uss Uss Uss Uss Uss Uss Uss Uss Uss Uss Uss Uss Uss Uss Uss Uss Uss Uss Vss Uss Uss Uss Uss Uss Uss Uss Uss Uss Uss Uss Uss Uss Uss Uss Uss Uss Uss Uss Uss Uss Uss Uss Uss Uss Uss Uss Uss Uss Uss Uss Uss Uss Uss Uss Uss Uss Uss Uss Uss Uss Uss Uss Uss Uss Uss Uss Uss Uss Aot Aot Aot Aot Aot Aot Aot Aot Aot Aot Aot Aot Aot Aot Aot Aot Aot Aot Aot Aot Aot Aot Aot Aot Aot Aot Aot Aot Aot Aot Aot Aot Aot Aot Aot Aot Aot Aot Aot Aot Aot Aot Aot Aot Aot Aot Aot Aot Aot Aot Alot Biot Biot Biot Biot Biot Biot Biot Biot Biot Biot Biot Biot Biot Biot Biot Biot Biot Biot Biot Biot Biot Biot Biot Biot Biot Biot Biot Biot Biot Biot Biot Biot Biot Biot Biot Biot Biot Biot Biot Biot Biot Biot Biot Biot Biot Biot Biot Biot Biot Biot Blot Blot Blot Blot Blot Blot Blot Blot Blot Blot Blot Blot Blot Blot Blot Blot Blot Blot Blot Blot Blot Blot Blot Blot Blot Blot Blot Blot Blot Blot Blot Blot Blot Blot Blot Blot Blot Blot Blot Blot Blot Blot Blot Blot Blot Blot Blot Blot Blot Blot BletuBlotBlotBlotBlotBlotBlotBlotBlotBlotBlotBlotBlotBlotBlotBlotBlotBlotBlotBlotBlotBlotBlotBlotBlotBlotBlotBlotBlotBlotBlotBlotBlotBlotBlotBlotBlotBlotBlotBlotBlotBlotBlotBlotBlotBlotBlotBlotBlotBlotBlotBletuBlotBlotBlotBlotBlotBlotBlotBlotBlotBlotBlotBlotBlotBlotBlotBlotBlotBlotBlotBlotBlotBlotBlotBlotBlotBlotBlotBlotBlotBlotBlotBlotBlotBlotBlotBlotBlotBlotBlotBlotBlotBlotBlotBlotBlotBletuBlotBaotBaotBaotBaotBaotBaotBaotBaotBaotBaotBaotBaotBaotBaotBaotBaotBaotBaotBaotBaotBaotBaotBaotBaotBaotBaotBaotBaotBaotBaotBaotBaotBaotBaotBaotBaotBaotBaotBaotBaotBaotBaotBaotBaotBaotBaotBaotBaotBaotBaotBaolBAoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoAloBAoOBtBAoOBtBAoOBtBAoOBtBAoOBtBAoOBtBAoOBtBAoOBtBAoOBtBAoOBtBAoOBtBAoOBtBAoOBtBAoOBtBAoOBtBAoOBtBAoOBtBAoOBtBAoOBtBAoOBtBAoOBtBAoOBtBAooOBtBAooOBtBAooOBtBAooOBtBAooOBtBAooOBtBAooOBtBAooOBtBAooOBtBAooOBtBAooOBtBAooOBtBAooOBtBAooOBtBAooOBtBAooOBtBAooOBtBAooOBtBAooOBtBAooOBtBAooOBtBAooOBtBAooOBtBAooOBtBAooOBtBAoooobobobobobobobobobobobobobobobobobobobobobobobobobobobobobobobobobobobobobobobobobobobobobobobobobobobobobobobobobobobobobobobobobobobobobobobobobobobobobobobobobobobobobobobobobobobobobobobobobobobohboxbobobobobobobobobobobobobobobobobobobobobobobobobobobobobobobobobobobobobobobobobobobobobobobobobobobobobobobobobobobobobobobobobobobobobobobobobobobobobobobobobobobobobobobobobobobobobobobobobobobobobocboxbocboxbocboxbocboxbocboxbocboxbocboxbocboxbocboxbocboxbocboxbocboxbocboxbocboxbocboxbocboxbocboxbocboxbocboxbocboxbocboxbocboxbocboxbocboxbocboxbocboxbocboxbocboxbocboxbocboxbocboxbocboxbocboxbocboxbbocboxbbocboxbbocboxbbocboxbbocboxbbocboxbbocboxbbocboxbbocboxbbocboxbbocboxbbocboxbbocboxbbocboxbbocboxbbocboxbbocboxbbocboxbbocboxbbocboxbbocboxbbocboxbbocboxbbocboxbbocboxbbocboxbbocboxbbocboxbbocboxbbocboxbbocboxbbocboxbbocboxbbocoonnlllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllccccc|ccccc|ccccc|ccccc|ccccc|ccccc|ccccc|ccccc|ccccc|ccccc|ccccc|ccccc|ccccc|ccccc|ccccc|ccccc|ccccc|ccccc|ccccc|ccccc|ccccc|ccccc|ccccc|ccccc|ccccc|ccccc|ccccc|ccccc|ccccc|ccccc|ccccc|ccccc|ccccc|ccccc|cctcccc|cctcccc|cctcccc|cctcccc|cctcccc|cctcccc|cctcccc|cctcccc|cctcccc|cctcccc|cctcccc|cctcccc|cctcccc|cctcccc|cctcccc|cctcccc|cctcccc|cctcccc|cctcccc|cctcccc|cctcccc|cctcccc|cctcccc|cctcccc|cctcccc|cctccc|cctcccc|cctcccc|cctcccc|cctcccc|cctcccc|cctcccc|cctcccc|cctcccc|cctcccc|cctcccc|cctcccc|cctcccc|cctcccc|cctcccc|cctcccc|cctcccc|cctcccc|cctcccc|cctcccc|cctcccc|cctcccc|cctcccc|cctcccc|cctcccc|cactcccc|cactcccc|cactcccc|cactcccc|cactcccc|cactcccc|cactcccc|cactcccc|cactcccc|cactcccc|cactcccc|cactcccc|cactcccc|cactcccc|cactcccc|cactcccc|cactcccc|cactcccc|cactcccc|cactcccc|cactcccc|cactcccc|cactcccc|cactcccc|cactcccc|cctcccc|cctcccc|cctcccc|cctcccc|cctcccc|cctcccc|cctcccc|cctcccc|cctcccc|cctcccc|cctcccc|cctcccc|cctcccc|cctcccc|cctcccc|cctcccc|cctcccc|cctcccc|
C:CC:CC:CC:CC:CC:CC:CC:CC:CC:CC:CC:CC:CC:CC:CC:CC:CC:CC:CC:CC:CC:CC:CC:CC:CC:CC:CC:CC:CC:CC:CC:CC:CC:CC:CC:CC:CC:CC:CC:CC:CC:CC:CC:CC:CC:CC:CC:CC:CC:CC:CCC:CCC:CCC:CCC:CCC:CCC:CCC:CCC:CCC:CCC:CCC:CCC:CCC:CCC:CCC:CCC:CCC:CCC:CCC:CCC:CCC:CCC:CCC:CCC:CCC:CCC:CCC:CCC:CCC:CCC:CCC:CCC:CCC:CCC:CCC:CCC:CCC:CCC:CCCC:CCC:CCCC:CCCC:CCCC:CCCC:CCCC:CCCC:CCCC:CCCC:CCCC:CCCC:CCCC:CCCC:CCCC:CCCC:CCCC:CCCC:CCCC:CCCC:CCCC:CCCC:CCCC:CCCC:CCCC:CCCC:CCCC:CCCC:CCCC:CCCC:CCCC:CCCC:CCCC:CCCC:CCCC:CCCC:CCCC:CCCC:CCCC:CCCC:CCCC:CCCC:CCCC:CCCC:CCCC:CCCC:CCCC:CCCC:CCCC:CCCC:CCCC:CCCC:CCCCCC:C C C C C C C C C C C C C C C C C C C C C C C C C C C C C C C C C C C C C C C C C C C C C C C C C C C C C C C C C C C C C C C C C C C C C C C C C C C C C C C C C C C C C C C C C C C C C C C C C C C C C CC : CC : CC : CC : CC : CC : CC : CC : CC : CC : CC : CC : CC : CC : CC : CC : CC : CC : CC : CC : CC : CC : CC : CC : CC : CC : CC : CC : CC : CC : CC : CC : CC : CC : CC : CC : CC : CC : CC : CC : CC : CC : CC : CC : CC : CC : CC : CC : CC : CC : CC /cc : cc : cc : cc : cc : cc : cc : cc : cc : cc : cc : cc : cc : cc : cc : cc : cc : cc : cc : cc : cc : cc : cc : cc : cc : cc : cc : cc : cc : cc : cc : cc : cc : cc : cc : cc : cc : cc : cc : cc : cc : cc : cc : cc : cc : cc : cc : cc : cc : cc : cc : ttcctttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttggggtgggtgggtgggtgggtgggtgggtgggtgggtgggtgggtgggtgggtgggtgggtgggtgggtgggtgggtgggtgggtgggtgggtgggtgggtgggtgggtgggtgggtgggtgggtgggtgggtgggtgggtgggtgggtgggtgggtgggtgggtgggtgggtgggtgggtgggtgggtgggtgggtgggtgggttggaatggaatggaatggaatggaatggaatggaatggaatggaatggaatggaatggaatggaatggaatggaatggaatggaatggaatggaatggaatggaatggaatggaatggaatggaatggaat
$$

(2) In the second round, using Eq. (11) obtains the experts' weights from {V<sup>(1,</sup> <sup>1)</sup>, V<sup>(2,1)</sup>, ... , V<sup>(8,1)</sup>}, λ = (0.1252, 0.1256, 0.1263, 0.1248, 0.1244, 0.1245, 0.1233, 0.1259)<sup>T</sup>.

Based on Eq. (14), we obtain $c l _ { 1 } { = } 0 . 8 0 7 1$

Using Eq. (19) $\mathrm { y i e l d s } s _ { 1 } ^ { ( 1 , 1 ) } = 0 . 9 0 6 5 , s _ { 1 } ^ { ( 2 , 1 ) } = 0 . 8 7 1 6 , s _ { 1 } ^ { ( 3 , 1 ) } = 0 . 4 3 6 1$ $s _ { 1 } ^ { ( 4 , 1 ) } = \bar { 0 } . 4 4 0 1 , \ s _ { 1 } ^ { ( 5 , 1 ) } = 0 . 5 0 4 3 , \ s _ { 1 } ^ { ( 6 , 1 ) } = 0 . 5 0 3 8 , \ s _ { 1 } ^ { ( 7 , 1 ) } = 0 . 5 6 4 1 ,$ , and $s _ { 1 } ^ { ( 8 , 1 ) } = 0 . 6 0 8 9$ . Then, Eq. (21) results in $s _ { 2 } ^ { ( 1 , 1 ) } = 0 , \stackrel { \cdot } { s _ { 2 } ^ { ( 2 , 1 ) } } = 0 , s _ { 2 } ^ { ( 3 , 1 ) } = 1$ $s _ { 2 } ^ { ( 4 , 1 ) } = 0 , s _ { 2 } ^ { ( 5 , 1 ) } = 0 , s _ { 2 } ^ { ( 6 , 1 ) } = 0 , s _ { 2 } ^ { ( 7 , 1 ) } = 0 ,$ , and $s _ { 2 } ^ { ( 8 , 1 ) } = 0 .$ . Next, using Eq. (22) provides ${ s _ { 3 } ^ { ( 1 , 1 ) } } = 0 . 2 0 3 3 , \stackrel { \sim } { s _ { 3 } ^ { ( 2 , 1 ) } } = 0 . 2 2 9 , \stackrel { \sim } { s _ { 3 } ^ { ( 3 , 1 ) } } = 0 . 1 8 7 7 , \stackrel { \sim } { s _ { 3 } ^ { ( 4 , 1 ) } } =$ 0.1993, s<sup>(5,1)</sup>=0.1627, s<sup>(6,1)</sup>=0.1609, $s _ { 3 } ^ { ( 7 , 1 ) } = 0 . 1 8 9$ , and $s _ { 3 } ^ { ( 8 , 1 ) } = \bar { 0 . 2 1 } 0 9 .$ Due to $s _ { 1 } ^ { ( 1 , 1 ) } > \alpha , s _ { 1 } ^ { ( 2 , \stackrel {  } { 1 } ) } > \alpha , \mathrm { a n d } s _ { 2 } ^ { ( 3 , \stackrel {  } { 1 } ) } = 1$ , we deduce that experts $e _ { 1 }$ and $e _ { 2 }$ have the characteristic of non-cooperative behavior I and that expert $e _ { 3 }$ has the characteristic of non-cooperative behavior II. In this situation, we assume that the experts provide the adjusted MMEMs $V ^ { ( k , 2 ) }$ $( k = 1 , 2 , \ldots , 8 )$ that are listed in Tables 6–7.

MMEMs V<sup>(1,2)</sup>–V<sup>(4,2)</sup>.

<table><tr><td rowspan="2"></td><td colspan="3"> $V^{(1,2)}$ </td><td colspan="3"> $V^{(2,2)}$ </td><td colspan="3"> $V^{(3,2)}$ </td><td colspan="3"> $V^{(4,2)}$ </td></tr><tr><td> $a_1$ </td><td> $a_2$ </td><td> $a_3$ </td><td> $a_1$ </td><td> $a_2$ </td><td> $a_3$ </td><td> $a_1$ </td><td> $a_2$ </td><td> $a_3$ </td><td> $a_1$ </td><td> $a_2$ </td><td> $a_3$ </td></tr><tr><td> $e_1$ </td><td>null</td><td>null</td><td>null</td><td>80</td><td>65</td><td>94</td><td>85</td><td>70</td><td>92</td><td>80</td><td>70</td><td>87</td></tr><tr><td> $e_2$ </td><td>85</td><td>60</td><td>94</td><td>null</td><td>null</td><td>null</td><td>85</td><td>68</td><td>100</td><td>85</td><td>65</td><td>88</td></tr><tr><td> $e_3$ </td><td>90</td><td>96</td><td>60</td><td>85</td><td>92</td><td>70</td><td>null</td><td>null</td><td>null</td><td>90</td><td>88</td><td>68</td></tr><tr><td> $e_4$ </td><td>80</td><td>95</td><td>88</td><td>90</td><td>90</td><td>92</td><td>80</td><td>88</td><td>94</td><td>null</td><td>null</td><td>null</td></tr><tr><td> $e_5$ </td><td>95</td><td>93</td><td>86</td><td>80</td><td>92</td><td>91</td><td>85</td><td>89</td><td>85</td><td>85</td><td>89</td><td>90</td></tr><tr><td> $e_6$ </td><td>85</td><td>92</td><td>89</td><td>80</td><td>90</td><td>88</td><td>85</td><td>91</td><td>83</td><td>80</td><td>91</td><td>91</td></tr><tr><td> $e_7$ </td><td>85</td><td>91</td><td>92</td><td>85</td><td>90</td><td>89</td><td>85</td><td>87</td><td>82</td><td>85</td><td>92</td><td>90</td></tr><tr><td> $e_8$ </td><td>80</td><td>90</td><td>95</td><td>80</td><td>89</td><td>91</td><td>90</td><td>89</td><td>90</td><td>92</td><td>93</td><td>88</td></tr></table>

Then, using Eq. (5) yields the collective preference relation $P ^ { ( c , 1 ) }$

$$
P ^ {(c, 1)} = \left( \begin{array}{c c c c c c} 0. 5 & 0. 4 3 8 & 0. 4 5 1 1 & 0. 6 1 5 1 & 0. 6 4 5 5 & 0. 6 1 2 7 \\ 0. 5 6 2 & 0. 5 & 0. 5 4 7 8 & 0. 6 1 6 & 0. 6 2 6 & 0. 7 0 3 4 \\ 0. 5 4 8 9 & 0. 4 5 2 2 & 0. 5 & 0. 7 0 1 4 & 0. 6 8 9 2 & 0. 6 7 7 2 \\ 0. 3 8 4 9 & 0. 3 8 4 & 0. 2 9 8 6 & 0. 5 & 0. 6 2 6 3 & 0. 5 8 6 7 \\ 0. 3 5 4 5 & 0. 3 7 4 & 0. 3 1 0 8 & 0. 3 7 3 7 & 0. 5 & 0. 6 9 5 5 \\ 0. 3 8 7 3 & 0. 2 9 6 6 & 0. 3 2 2 8 & 0. 4 1 3 3 & 0. 3 0 4 5 & 0. 5 \end{array} \right).
$$

When constructing $P ^ { ( k , 2 ) } = ( p _ { i j } ^ { ( k , 2 ) } ) _ { n \times n } ( k = 1 , 2 , \dots , 8 )$ , we suggest that

$$
\left\{ \begin{array}{l l} p _ {i j} ^ {(k, 2)} = \Big [ \min \Big (p _ {i j} ^ {(k, 1)}, p _ {i j} ^ {(c, 1)} \Big),   \max \Big (p _ {i j} ^ {(k, 1)}, p _ {i j} ^ {(c, 1)} \Big) \Big ], & i f i \leq j \\ p _ {i j} ^ {(k, 2)} = 1 - p _ {j i} ^ {(k, 2)}, & i f i > j \end{array} \right.
$$

Without loss of generality, based on the adjustment suggestions, the experts provided their adjusted preference relations $P ^ { ( k , 2 ) } \left( \bar { k } = 1 , 2 , . . . , 8 \right)$ as follows:

$$
P ^ {(2, 2)} = \left( \begin{array}{c c c c c c} 0. 5 & 0. 5 8 2 1 & 0. 5 2 1 & 0. 6 1 2 6 & 0. 8 9 7 3 & 0. 8 4 7 1 \\ 0. 4 1 7 9 & 0. 5 & 0. 5 5 8 1 & 0. 4 7 2 2 & 0. 7 0 0 9 & 0. 7 0 3 \\ 0. 4 7 9 & 0. 4 4 1 9 & 0. 5 & 0. 5 2 2 2 & 0. 6 9 4 4 & 0. 6 7 1 3 \\ 0. 3 8 7 4 & 0. 5 2 7 8 & 0. 4 7 7 8 & 0. 5 & 0. 8 1 2 8 & 0. 6 9 6 5 \\ 0. 1 0 2 7 & 0. 2 9 9 1 & 0. 3 0 5 6 & 0. 1 8 7 2 & 0. 5 & 0. 6 6 4 5 \\ 0. 1 5 2 9 & 0. 2 9 7 & 0. 3 2 8 7 & 0. 3 0 3 5 & 0. 3 3 5 5 & 0. 5 \end{array} \right),
$$

Table 7 MMEMs V<sup>(5,2)</sup>–V<sup>(8,2)</sup>.

<table><tr><td rowspan="2"></td><td colspan="3"> $V^{(5,2)}$ </td><td colspan="3"> $V^{(6,2)}$ </td><td colspan="3"> $V^{(7,2)}$ </td><td colspan="3"> $V^{(8,2)}$ </td></tr><tr><td> $a_1$ </td><td> $a_2$ </td><td> $a_3$ </td><td> $a_1$ </td><td> $a_2$ </td><td> $a_3$ </td><td> $a_1$ </td><td> $a_2$ </td><td> $a_3$ </td><td> $a_1$ </td><td> $a_2$ </td><td> $a_3$ </td></tr><tr><td> $e_1$ </td><td>82</td><td>72</td><td>90</td><td>81</td><td>78</td><td>97</td><td>85</td><td>70</td><td>91</td><td>86</td><td>65</td><td>84</td></tr><tr><td> $e_2$ </td><td>85</td><td>64</td><td>88</td><td>87</td><td>72</td><td>98</td><td>86</td><td>68</td><td>85</td><td>85</td><td>65</td><td>89</td></tr><tr><td> $e_3$ </td><td>92</td><td>92</td><td>67</td><td>90</td><td>93</td><td>70</td><td>84</td><td>89</td><td>65</td><td>90</td><td>84</td><td>67</td></tr><tr><td> $e_4$ </td><td>86</td><td>100</td><td>86</td><td>85</td><td>94</td><td>84</td><td>85</td><td>90</td><td>82</td><td>86</td><td>85</td><td>91</td></tr><tr><td> $e_5$ </td><td>null</td><td>null</td><td>null</td><td>84</td><td>89</td><td>85</td><td>86</td><td>92</td><td>86</td><td>84</td><td>84</td><td>92</td></tr><tr><td> $e_6$ </td><td>83</td><td>90</td><td>92</td><td>null</td><td>null</td><td>null</td><td>90</td><td>91</td><td>87</td><td>91</td><td>85</td><td>90</td></tr><tr><td> $e_7$ </td><td>86</td><td>88</td><td>91</td><td>85</td><td>88</td><td>86</td><td>null</td><td>null</td><td>null</td><td>83</td><td>83</td><td>88</td></tr><tr><td> $e_8$ </td><td>91</td><td>87</td><td>90</td><td>90</td><td>92</td><td>87</td><td>88</td><td>89</td><td>90</td><td>null</td><td>null</td><td>null</td></tr></table>

Please cite this article as: Y. Dong, et al., Integrating experts' weights generated dynamically into the consensus reaching process and its applications in managing non-cooperative behaviors, Decision Support Systems (2016), http://dx.doi.org/10.1016/j.dss.2016.01.002

$$
P ^ {(3, 2)} = \left( \begin{array}{c c c c c c} 0. 5 & 0. 5 6 5 & 0. 3 6 1 5 & 0. 4 9 5 4 & 0. 6 4 & 0. 7 4 1 6 \\ 0. 4 3 5 & 0. 5 & 0. 4 4 2 9 & 0. 3 9 8 4 & 0. 4 7 7 9 & 0. 7 1 9 1 \\ 0. 6 3 8 5 & 0. 5 5 7 1 & 0. 5 & 0. 6 7 1 3 & 0. 7 0 8 6 & 0. 8 1 1 3 \\ 0. 5 0 4 6 & 0. 6 0 1 6 & 0. 3 2 8 7 & 0. 5 & 0. 6 3 5 6 & 0. 6 6 3 \\ 0. 3 6 & 0. 5 2 2 1 & 0. 2 9 1 4 & 0. 3 6 4 4 & 0. 5 & 0. 7 0 3 \\ 0. 2 5 8 4 & 0. 2 8 0 9 & 0. 1 8 8 7 & 0. 3 3 7 & 0. 2 9 7 & 0. 5 \end{array} \right),
$$

$$
P ^ {(4, 2)} = \left( \begin{array}{c c c c c c} 0. 5 & 0. 2 6 6 6 & 0. 4 3 7 8 & 0. 6 1 4 7 & 0. 4 0 3 3 & 0. 5 4 8 9 \\ 0. 7 3 3 4 & 0. 5 & 0. 5 7 8 7 & 0. 6 5 3 9 & 0. 6 2 5 2 & 0. 7 0 6 8 \\ 0. 5 6 2 2 & 0. 4 2 1 3 & 0. 5 & 0. 7 2 3 2 & 0. 6 1 4 1 & 0. 5 7 0 5 \\ 0. 3 8 5 3 & 0. 3 4 6 1 & 0. 2 7 6 8 & 0. 5 & 0. 5 4 6 5 & 0. 4 8 5 9 \\ 0. 5 9 6 7 & 0. 3 7 4 8 & 0. 3 8 5 9 & 0. 4 5 3 5 & 0. 5 & 0. 6 7 0 6 \\ 0. 4 5 1 1 & 0. 2 9 3 2 & 0. 4 2 9 5 & 0. 5   {1}   {4} _ {1} & {0.} {3} _ {2} {9} _ {4} & {0.} {5} \end{array} \right),
$$

$$
P ^ {(5, 2)} = \left( \begin{array}{c c c c c c} 0. 5 & 0. 4 6 2 8 & 0. 4 4 8 8 & 0. 5 7 1 7 & 0. 6 4 3 5 & 0. 4 8 6 7 \\ 0. 5 3 7 2 & 0. 5 & 0. 6 4 6 7 & 0. 7 3 2 5 & 0. 6 0 6 6 & 0. 7 2 3 3 \\ 0. 5 5 1 2 & 0. 3 5 3 3 & 0. 5 & 0. 7 0 0 1 & 0. 6 8 9 4 & 0. 6 7 4 3 \\ 0. 4 2 8 3 & 0. 2 6 7 5 & 0. 2 9 9 9 & 0. 5 & 0. 6 2 7 7 & 0. 6 0 6 8 \\ 0. 3 5 6 5 & 0. 3 9 3 4 & 0. 3 1 0 6 & 0. 3 7 2 3 & 0. 5 & 0.   {7}   {0}   {5}   {7} \\ {0.} {5} {1} {3} {3} {3} & {0.} {2} {7} {6} {7} & {0.} {3} {2} {5} {7} & {0.} {3} {9} {3} {2} & {0.} {2} {9} {4} {3} & {0.} {5} \end{array} \right),
$$

$$
P ^ {(6, 2)} = \left( \begin{array}{c c c c c c} 0. 5 & 0. 4 4 8 3 & 0. 5 3 1 6 & 0. 6 6 4 4 & 0. 6 3 4 1 & 0. 6 7 4 \\ 0. 5 5 1 7 & 0. 5 & 0. 5 4 6 & 0. 6 2 3 9 & 0. 4 9 6 9 & 0. 7 0 3 5 \\ 0. 4 6 8 4 & 0. 4 5 4 & 0. 5 & 0. 7 0 0 5 & 0. 6 7 8 4 & 0. 6 4 9 8 \\ 0. 3 3 5 6 & 0. 3 7 6 1 & 0. 2 9 9 5 & 0. 5 & 0. 6 8 & 0. 5 4 9 4 \\ 0. 3 6 5 9 & 0. 5 0 3 1 & 0. 3 2 1 6 & 0. 3 2 & 0. 5 & 0. 7 1 3 \\ 0. 3 2 6 & 0. 2 9 6 5 & 0. 3 5 0 2 & 0. 4 5 0 6 & 0. 2 8 7 & 0. 5 \end{array} \right),
$$

$$
P ^ {(7, 2)} = \left( \begin{array}{c c c c c c} 0. 5 & 0. 4 1 2 3 & 0. 3 8 0 5 & 0. 7 1 4 7 & 0. 6 5 3 4 & 0. 6 6 5 3 \\ 0. 5 8 7 7 & 0. 5 & 0. 4 1 3 7 & 0. 6 1 3 5 & 0. 6 6 8 7 & 0. 8 4 1 6 \\ 0. 6 1 9 5 & 0. 5 8 6 3 & 0. 5 & 0. 8 1 9 2 & 0. 6 9 4 1 & 0. 7 4 4 9 \\ 0. 2 8 5 3 & 0. 3 8 6 5 & 0. 1 8 0 8 & 0. 5 & 0. 6 1 4 5 & 0. 7 1 5 3 \\ 0. 3 4 6 6 & 0. 3 3 1 3 & 0. 3 0 5 9 & 0. 3 8 5 5 & 0. 5 & 0. 7 2 0 4 \\ 0. 3 3 4 7 & 0. 1 5 8 4 & 0. 2 5 5 1 & 0. 2 8 4 7 & 0. 2 7 9 6 & 0. 5 \end{array} \right),
$$

$$
P ^ {(8, 2)} = \left( \begin{array}{c c c c c c} 0. 5 & 0. 2 4 8 & 0. 2 5 9 3 & 0. 5 6 9 9 & 0. 6 4 5 8 & 0. 5 0 2 7 \\ 0. 7 5 2 & 0. 5 & 0. 6 0 2 1 & 0. 6 5 5 2 & 0. 7 9 0 2 & 0. 5 3 2 9 \\ 0. 7 4 0 7 & 0. 3 9 7 9 & 0. 5 & 0. 7 2 3 & 0. 7 3 1 9 & 0. 6 8 8 2 \\ 0. 4 3 0 1 & 0. 3 4 4 8 & 0. 2 7 7 & 0. 5 & 0. 6 8 1 1 & 0. 6 4 2 5 \\ 0. 3 5 4 2 & 0. 2 0 9 8 & 0. 2 6 8 1 & 0. 3 1 8 9 & 0. 5 & 0. 7 1 1 3 \\ 0. 4 9 7 3 & 0. 4 6 7 1 & 0. 3 1 1 8 & 0. 3 5 7 5 & 0. 2 8 8 7 & 0. 5 \end{array} \right).
$$

(3) In the third round, using Eq. (11) provides the experts' weights from $\{ V ^ { ( 1 , 2 ) } , V ^ { ( 2 , 2 ) } , \ldots , V ^ { ( \stackrel { \sim } { 8 } , 2 ) } \} , \stackrel { { . } } { \lambda } _ { 2 } = \stackrel { { . } } { ( 0 . 1 1 8 7 , 0 . 1 1 8 4 , 0 . 1 2 , 0 . 1 \stackrel { \sim } { 8 } } 8 ,$ 0.1283, 0.1286, 0.1273, 0.1298)<sup>T</sup>.

Based on Eq. (14), we obtain $c l _ { 2 } { = } 0 . 8 8 3 7 .$ . The predefined consensus level is achieved. Then, using the selection process, we can observe that the collective ranking of alternatives is $x _ { 2 } > x _ { 3 } > x _ { 1 } > x _ { 4 } > x _ { 5 } > x _ { 6 } .$

## 6. Conclusion

In this study, we consider the non-cooperative behaviors in the CRP, and propose a novel consensus framework to manage non-cooperative behaviors. In this framework, a self-management mechanism to generate experts' weights is devised and then integrated into the CRP, in which the experts' weights are dynamically derived from the MMEMs. The detailed simulation experiments and a comparison analysis are presented to show the validity of the proposed consensus framework in managing the non-cooperative behaviors.

The proposal in this study can provide the decision support to help experts cope with the non-cooperative behaviors, and this ability will be key either for an academic conference committee attempting to select a best paper or for a science foundation committee that wants to find outstanding projects to support.

Modeling large-scale GDM has become a trend with the development of technology and society (e.g., e-democracy [19,33] and social networks [61]). However, in a large-scale GDM context, the experts may feel that it is difficult to provide the MMEMs. We argue that it will be interesting in future research to design a self-management mechanism to manage non-cooperative behaviors in a large-scale GDM.

## Acknowledgments

This work was supported in part by the NSF of China under grants 71171160 and 71571124, in part by the SSEM Key Research Center at Sichuan Province under grant xq15b01, in part by the FEDER funds under grant TIN2013-40658-P, and in part by Andalusian Excellence Project under grant TIC-5991.

## Appendix A. The Proof of Theorem 1

We construct the following Lagrange function:

$$
L (\lambda_ {i}, \varepsilon) = \sum_ {k = 1} ^ {m} \sum_ {i = 1} ^ {m} \left(\sum_ {j = 1} ^ {l} w _ {j} \overline {{v}} _ {i j} ^ {(k)} - \lambda_ {i}\right) ^ {2} + \varepsilon \left(\sum_ {i = 1} ^ {m} \lambda_ {i} - 1\right),\tag{23}
$$

where ε is the Lagrange multiplier.

Then, the partial derivatives of L are computed as

$$
\frac {\partial L (\lambda_ {i} , \varepsilon)}{\partial \lambda_ {i}} = - 2 \sum_ {k = 1} ^ {m} \left(\sum_ {j = 1} ^ {l} w _ {j} \bar {v} _ {i j} ^ {(k)} - \lambda_ {i}\right) + \varepsilon = 0,\tag{24}
$$

and

$$
\frac {\partial L (\lambda_ {i} , \varepsilon)}{\partial \varepsilon} = \sum_ {i = 1} ^ {m} \lambda_ {i} - 1 = 0.\tag{25}
$$

By solving Eq. (24), we have

$$
w _ {i} = - \frac {\varepsilon}{2 m} + \frac {\sum_ {k = 1} ^ {m} \sum_ {j = 1} ^ {l} w _ {j} \overline {{v}} _ {i j} ^ {(k)}}{m}.\tag{26}
$$

Putting Eq. (26) into Eq. (25), we can obtain

$$
- \frac {\varepsilon}{2} + \frac {\sum_ {i = 1} ^ {m} \sum_ {k = 1} ^ {m} \sum_ {j = 1} ^ {l} w _ {j} \overline {{v}} _ {i j} ^ {(k)}}{m} = 1.\tag{27}
$$

Base on Eq. (7), Eq. (8), and Eq. (9), we have $\begin{array} { r } { \sum _ { i = 1 } ^ { m } w _ { j } \overline { { \nu } } _ { i j } ^ { ( k ) } = } \end{array}$ $\begin{array} { r } { w _ { j } \sum _ { i = 1 } ^ { m } \overline { { \nu } } _ { i j } ^ { ( k ) } = w _ { j } ; } \end{array}$ thus,

$$
\sum_ {i = 1} ^ {m} \sum_ {k = 1} ^ {m} \sum_ {j = 1} ^ {l} w _ {j} \overline {{v}} _ {i j} ^ {(k)} = \sum_ {k = 1} ^ {m} \sum_ {j = 1} ^ {l} w _ {j} \sum_ {i = 1} ^ {m} \overline {{v}} _ {i j} ^ {(k)} = \sum_ {k = 1} ^ {m} \sum_ {j = 1} ^ {l} w _ {j} = m.\tag{28}
$$

Putting Eq. (28) into Eq. (27), we can obtain ε=0. Then, based on Eq. (26), we have

$$
\lambda_ {i} = \frac {\sum_ {k = 1} ^ {m} \left(\sum_ {j = 1} ^ {l} w _ {j} \overline {{v}} _ {i j} ^ {(k)}\right)}{m} (i = 1, 2,..., m).
$$

This completes the proof of Theorem 1.

## Appendix B. Algorithm I

Input: The preference relations $P ^ { ( k ) } = ( p _ { i j } ^ { ( k ) } ) _ { n \times n } ( k = 1 , 2 , \dots , m )$ , the MMEMs $V ^ { ( k ) } { \bar { = } } ( \nu _ { i j } ^ { ( k ) } ) _ { m \times l } ( k { = } 1 , 2 , { \dots } , m )$ , the weight vector of the attributes $w = ( w _ { 1 } , w _ { 2 } , \ldots , w _ { l } ) ^ { T }$ in the MMEMs, the established consensus level cl, and the established maximum number of rounds $z _ { \mathrm { m a x } } 2 1$

Please cite this article as: Y. Dong, et al., Integrating experts' weights generated dynamically into the consensus reaching process and its applications in managing non-cooperative behaviors, Decision Support Systems (2016), http://dx.doi.org/10.1016/j.dss.2016.01.002

Output: The adjusted preference relations $\overline { { P ^ { ( k ) } } } = ( \overline { { p _ { i j } ^ { ( k ) } } } ) _ { n \times n } \ : \ : ( k =$ $1 , 2 , \ldots , m )$ , the adjusted MMEMs $\overline { { V ^ { ( k ) } } } = \left( \overline { { V _ { i j } ^ { ( k ) } } } \right) _ { m \times l } \ : \left( k = 1 , 2 , \dots , m \right)$ , and the number of iterations z.

Step 1: Let $z = 0 , P ^ { ( k , z ) } = P ^ { ( k ) }$ , and $V ^ { ( k , z ) } = V ^ { ( k ) } \left( k = 1 , 2 , . . . , m \right)$

Step 2: Use Eq. (11) to obtain the experts' weights $\lambda _ { z } =$ $( \lambda _ { 1 , z } , \lambda _ { 2 , z } , \ldots , \lambda _ { m , z } ) ^ { T } ,$ , where $\lambda _ { i , z } = \frac { \sum _ { k = 1 } ^ { m } \left( \sum _ { j = 1 } ^ { l } w _ { j } \overline { { \nu } } _ { i j } ^ { ( k , z ) } \right) } { m }$

Step 3: Use Eq. (14) to obtain the consensus level among experts cl . If cl ≥ cl or $Z \geq Z _ { \mathrm { m a x } } , { \mathrm { g o } }$ to Step 6; otherwise, continue with the next step. Step 4: Expert e<sub>k</sub> $( k = 1 , 2 , . . . , m )$ provides his/her updated MMEM $V ^ { ( k , z + \hat { 1 } ) } = ( \nu _ { i j } ^ { ( \hat { k } , z + 1 ) } ) _ { m \times l }$ based on other experts' performances.

Step 5: Use Eq. (5) to obtain the collective preference relation $P ^ { ( c , z ) } =$ $( p _ { i j } ^ { ( c , z ) } ) _ { n \times n } ,$ where $\begin{array} { r } { p _ { i j } ^ { ( c , z ) } = \sum _ { k = 1 } ^ { m } \lambda _ { k , z } p _ { i j } ^ { ( k , z ) } } \end{array}$ . When constructing $P ^ { ( k , z + 1 ) } =$ $( p _ { i j } ^ { ( k , z + 1 ) } ) _ { n \times n } ( k { = } 1 , 2 , \dots , m )$ , we suggest that

$$
\left\{ \begin{array}{l l} p _ {i j} ^ {(k, z + 1)} \in \Big [ \min \Big (p _ {i j} ^ {(k, z)}, p _ {i j} ^ {(c, z)} \Big),   \max \Big (p _ {i j} ^ {(k, z)}, p _ {i j} ^ {(c, z)} \Big) \Big ], & \text { if } i \leq j \\ p _ {i j} ^ {(k, z + 1)} = 1 - p _ {j i} ^ {(k, z + 1)}, & \text { if } i > j \end{array} \right..
$$

Let $\scriptstyle z = z + 1$ , then go to Step 2.

Step 6: Let $\overline { { P ^ { ( k ) } } } = P ^ { ( k , z ) }$ and $\overline { { V ^ { ( k ) } } } = V ^ { ( k , z ) }$ . Output the adjusted preference relations $\overline { { P ^ { ( k ) } } } = \left( \overline { { p _ { i j } ^ { ( k ) } } } \right) _ { n \times n }$ , the MMEMs $\overline { { V ^ { ( k ) } } } = \left( \overline { { \nu _ { i j } ^ { ( k ) } } } \right) _ { m \times l } ( k =$ $1 , 2 , . . . , m )$ , and the number of rounds z.

## Appendix C. Simulation method I

Input: m, n $\overline { { c l } } , z _ { \mathrm { m a x } } , \alpha , \theta ,$ , and r.

Output: s, z.

Step 1: We randomly generate m n×n preference relations $\{ P ^ { ( 1 ) } , \hat { . . . } , P ^ { ( m ) } \}$ and m m×l MMEMs $\{ V ^ { ( 1 ) } , . . . , V ^ { ( m ) } \}$

Step $2 \colon \mathsf { L e t } z = 0 , P ^ { ( k , z ) } = P ^ { ( k ) }$ , and $V ^ { ( k , z ) } = V ^ { ( k ) } \left( k = 1 , 2 , . . . , m \right)$

Step 3: Use $\operatorname { E q . } \ \left( 1 1 \right)$ to yield the experts' weights $\lambda _ { z } =$

$( \lambda _ { 1 , z } , \lambda _ { 2 , z } , . . . , \lambda _ { m , z } ) ^ { T } ,$ , where $\lambda _ { i , z } = \frac { \sum _ { k = 1 } ^ { m } \left( \sum _ { j = 1 } ^ { l } w _ { j } \overline { { \nu } } _ { i j } ^ { ( k , z ) } \right) } { m }$

Step 4: Use Eq. (14) to obtain the consensus level among experts, $c l _ { z } .$ $\operatorname { I f } c l _ { z } { \ge } \overline { { c l } }$ or $z { \ge } z _ { \mathrm { m a x } } ,$ then go to Step $7 ;$ otherwise, continue with the next step.

Step $5 \colon \mathrm { H } z = 0 ,$ then let $V ^ { ( k , z + 1 ) } = V ^ { ( k , z ) }$ ; otherwise, use Eq. (19) to obtain $s _ { 1 } ^ { ( i , z ) } ( i { = } 1 , 2 , . . , m )$ . Based on Hypothesis 1, if $\begin{array} { r } { \dot { s } _ { 1 } ^ { ( i , z ) } \ge \alpha \left( z \ge 1 \right) } \end{array}$ , then experts $e _ { k } ( k = 1 , 2 , . . , m , k \neq i )$ will decrease the evaluation of expert $e _ { i }$ regarding the attribute “cooperation $( a _ { 2 } ) .$ ” Without loss of generality, the updated MMEM $\begin{array} { r } { \ L { s V } ^ { ( k , z + 1 ) } { = } ( \nu _ { i j } ^ { ( k , z + 1 ) } ) _ { m \times l } ( i { = } 1 , 2 , . . , m , z { \ge } 1 ) } \end{array}$ are provided by using the following method:

(i) If j = 1, 3, then let $\nu _ { i j } ^ { ( k , z + 1 ) } = \nu _ { i j } ^ { ( k , z ) }$

(ii) If j = 2, then let

$$
v _ {i j} ^ {(k, z + 1)} = \left\{ \begin{array}{l l} n u l l, & i f i = k \\ \max \Big (v _ {i j} ^ {(k, z)} - 1 0 0 \theta , 0 \Big), & i f i \neq k \land s _ {1} ^ {(i, z)} \geq \alpha \\ v _ {i j} ^ {(k, z)}, & i f i \neq k \land s _ {1} ^ {(i, z)} <   \alpha \end{array} \right..
$$

Step 6: Use $\operatorname { E q . } \left( 5 \right)$ to obtain the collective preference relation $P ^ { ( c , z ) } =$ $( p _ { i j } ^ { ( c , z ) } ) _ { n \times n } ,$ where $\begin{array} { r } { p _ { i j } ^ { ( c , z ) } = \sum _ { k = 1 } ^ { m } \lambda _ { k , z } p _ { i j } ^ { ( k , z ) } } \end{array}$ . When constructing $P ^ { ( k , z + 1 ) } =$ $( p _ { i j } ^ { ( k , z + 1 ) } ) _ { n \times n } ( k { = } 1 , 2 , \dots , m )$ , two cases are considered.

Case A. k≤r. In this case, expert $e _ { k }$ provides $P ^ { ( k , z + 1 ) }$ as follows:

For $i = 1 , 2 , \dots , n$ and $j = i + 1 , \ldots , n ,$ , then let $p _ { i j } ^ { ( k , z + 1 ) } = ( 1 -$ $\mu ) p _ { i j } ^ { ( k , z ) } + \mu p _ { i j } ^ { ( c , z ) }$ , where the value of u is uniformly randomly selected from the interval $[ 0 , 1 - \alpha ] , \ p _ { j i } ^ { ( k , z + 1 ) } = 1 - p _ { i j } ^ { ( k , z + 1 ) }$ , and $p _ { i i } ^ { ( k , z + 1 ) } = 0 . 5$

Case B. $r < k \leq m .$ . In this case, expert $e _ { k }$ provides $P ^ { ( k , z + 1 ) }$ , as follows:

For $i = 1 , 2 , \dots , n$ and $j = i + 1 , \ldots , n ,$ , then let $p _ { i j } ^ { ( k , z + 1 ) } = ( 1 -$ $\mu ) p _ { i j } ^ { ( k , z ) } + \mu p _ { i j } ^ { ( c , z ) }$ , where the value of u is uniformly randomly selected from the interval $[ 1 - \alpha , 1 ] , p _ { j i } ^ { ( k , z + 1 ) } = 1 - p _ { i j } ^ { ( k , z + 1 ) }$ , and $p _ { i i } ^ { ( k , z + \mathbf { \bar { 1 } } ) } = 0 . 5$

Let $z { = } z + 1 ,$ , then go to Step 3.

Step 7: If ${ \dot { c l } } _ { z } \geq { \overline { { c l } } } ,$ then $s { = } 1 ;$ otherwise $s { = } 0 .$ Output s and z.

## Appendix D. Simulation method II.

In Simulation method I, we replace Input and Steps 5 and 6 with Input′ and Steps 5′ and 6′, respectively, and then obtain a new simulation method: Simulation method II. Input′ and Steps $5 ^ { \prime }$ and $6 ^ { \prime }$ are given below:

Input′: Input': $m , n , \overline { { c l } } , z _ { \mathrm { m a x } } , \beta , \theta , \mathrm { a n d } r .$

Step $5 ^ { \prime } { : } \operatorname { I f } z = 0 .$ , let $V ^ { ( k , z + 1 ) } = V ^ { ( k , z ) } ;$ ; otherwise, use Eq. (21) to obtain $s _ { 2 } ^ { ( i , z ) } ( \dot { i } = 1 , 2 , . . . , m )$ . Based on Hypothesis $2 , \operatorname { i f } s _ { 2 } ^ { ( i , z ) } = 1 \ ( z \geq 1 )$ , experts $e _ { k }$ $( k = 1 , 2 , \ldots , m , k \neq i )$ will decrease the evaluation of expert e regarding the attribute “fairness $( a _ { 3 } ) . "$ Without loss of generality, the updated MMEMs $V ^ { ( k , z + 1 ) } = ( \nu _ { i j } ^ { ( \dot { k } , z + 1 ) } ) _ { m \times l } ( k = 1 , 2 , \dots , \overline { { m } } , z { \ge } 1 )$ are provided, as follows:

$$
\begin{array}{l} \text {(i) if j = 1, 2, let v_{ij} ^{(k,z+ 1)} = v_{ij} ^{(k,z)} ;} \\ \text {(ii) if j = 3, let} \end{array}
$$

$$
v _ {i j} ^ {(k, z + 1)} = \left\{ \begin{array}{l l} n u l l, & i f i = k \\ \max \Big (v _ {i j} ^ {(k, z)} - 1 0 0 \theta , 0 \Big), & i f i \neq k \wedge s _ {2} ^ {(i, z)} = 1 \\ v _ {i j} ^ {(k, z)}, & i f i \neq k \wedge s _ {2} ^ {(i, z)} = 0 \end{array} \right..
$$

Step $6 \prime { : }$ Use Eq. (5) to obtain the collective preference relation $P ^ { ( c , z ) } = ( p _ { i j } ^ { ( c , z ) } ) _ { n \times n } ,$ where $\begin{array} { r } { p _ { i j } ^ { ( c , z ) } = \sum _ { k = 1 } ^ { m } \lambda _ { k , z } p _ { i j } ^ { ( k , z ) } } \end{array}$ . Then, use Eq. (6) to obtain the preference vector $P r ^ { ( c , z ) }$ and the collective most preferred alternative $\boldsymbol { x } _ { o } ^ { ( c , z ) }$ from $P ^ { ( c , z ) }$ . When constructing $P ^ { ( k , z + 1 ) } = ( p _ { i j } ^ { ( k , z + 1 ) } ,$ )<sub>n×n</sub> $( k = 1 , 2 , \ldots , m )$ , two cases are considered.

Case A. k≤r. In this case, the expert $e _ { k }$ provides $P ^ { ( k , z + 1 ) } = ( p _ { i j } ^ { ( k , z + 1 ) } )$ n×n as follows:

(i) For $i = 1 , 2 , \ldots , n , j = i + 1 , \ldots , n ,$ , and $i , j { \neq } 0 ,$ , then let $p _ { i j } ^ { ( k , z + 1 ) } =$ $( 1 - \mu ) p _ { i j } ^ { ( k , z ) } + \mu p _ { i j } ^ { ( c , z ) }$ , where the value of u is uniformly randomly selected from the interval $[ 0 . 2 , 1 ] , p _ { j i } ^ { ( k , z + 1 ) } = 1 - p _ { i j } ^ { ( \check { k } , z + 1 ) }$ , and $p _ { i i } ^ { ( k , z + 1 ) } = 0 . 5$

(ii) For $j = 1 , 2 , \dots , n$ and $j { \neq } 0$ , then let the value of $p _ { o j } ^ { ( k , z + 1 ) }$ be uniformly randomly selected from the interval [0, 1], and $p _ { { p } _ { 0 } } ^ { ( k , z + \mathbf { \breve { 1 } } ) } = 1 - p _ { o j } ^ { ( k , \mathbf { \breve { z } } + 1 ) }$

(iii) $\mathrm { F o r } j = 0 ,$ then let $p _ { o , o } ^ { ( k , z + 1 ) } = 0 . 5$

Use Eq. (20) and Eq. (21) to obtain the $O ^ { ( k , z + 1 ) } =$ $( o ^ { ( k , z + 1 ) } ( x _ { 1 } ^ { \bullet } ) , \ldots , o ^ { ( k , z + 1 ) } ( x _ { n } ) ) ^ { ^ { 1 } }$ and $s _ { 2 } ^ { ( k , z + 1 ) }$ , respectively. Repeat (ii) until $s _ { 2 } ^ { ( k , z + 1 ) } = 1 ( k \leq r )$

Case B. rbk≤m. In this case, expert $e _ { k }$ provides $P ^ { ( k , z + 1 ) } = ( p _ { i j } ^ { ( k , z + 1 ) } ) _ { n \times n }$ as follows:

For $i = 1 , 2 , \dots , n$ and $j = i + 1 , \ldots , n ,$ then let $p _ { i j } ^ { ( k , z + 1 ) } = ( 1 - \mu )$ $p _ { i j } ^ { ( k , z ) } + \mu p _ { i j } ^ { ( c , z ) }$ , where the value of u is uniformly randomly selected from the interval $[ 1 - \alpha , 1 ] , p _ { j i } ^ { ( k , z + 1 ) } = 1 - p _ { i j } ^ { ( k , z ) }$ , and $p _ { i i } ^ { ( k , z + 1 ) } = 0 . 5$ Let $z = z + 1$ , then go to Step 3.

## Appendix E. Simulation method III

In Simulation method I, we replace Input and Steps 5 and 6 with Input″ and Steps $5 ^ { \prime \prime }$ and $6 \%$ , respectively, and then obtain a new

Please cite this article as: Y. Dong, et al., Integrating experts' weights generated dynamically into the consensus reaching process and its applications in managing non-cooperative behaviors, Decision Support Systems (2016), http://dx.doi.org/10.1016/j.dss.2016.01.002

simulation method: Simulation method III. Input″ and Steps $5 ^ { \prime \prime }$ and $6 ^ { \prime \prime }$ are provided as follows:

Input″: $m , n , \overline { { c l } } , z _ { \mathrm { m a x } } , \gamma , \theta ,$ and r.

Step 5″: If $z = 0 ,$ let $V ^ { ( k , z + 1 ) } = V ^ { ( k , z ) } ( i = 1 , 2 , \ldots , m )$ ; otherwise, use $\operatorname { E q . } \left( 2 2 \right)$ to provide $s _ { 3 } ^ { ( i , z ) } ( i { = } 1 , 2 , . . . , m )$ . Based on Hypothesis $3 , \mathrm { i f } s _ { 3 } ^ { ( i , z ) } \ge \gamma$ $( z \ge 1 )$ , experts $e _ { k } ( k { = } 1 , 2 , \ldots , m , k { \neq } i )$ will decrease the evaluation of expert e<sub>i</sub> regarding the attributes “professional skill $( a _ { 1 } ) "$ and “cooperation $\left( a _ { 2 } \right) .$ ” Without loss of generality, the updated MMEMs $V ^ { ( k , z + 1 ) } =$ $( \nu _ { i j } ^ { ( k , z + 1 ) } ) _ { m \times l } \ : ( k { = } 1 , 2 , \ldots , m , z { \geq } 1 )$ are provided, as follows:

(i). if j = 3, then let $\nu _ { i j } ^ { ( k , z + 1 ) } = \nu _ { i j } ^ { ( k , z ) }$

(ii). If j = 1, 2, then let

$$
v _ {i j} ^ {(k, z + 1)} = \left\{ \begin{array}{l l} n u l l, & i f i = k \\ \max \Big (v _ {i j} ^ {(k, z)} - 1 0 0 \theta , 0 \Big), & i f i \neq k \wedge s _ {3} ^ {(i, z)} \geq \gamma \\ v _ {i j} ^ {(k, z)}, & i f i \neq k \wedge s _ {3} ^ {(i, z)} <   \gamma \end{array} \right..
$$

Step $6 \%$ Use Eq. (5) to obtain the collective preference relation $P ^ { ( c , z ) } = ( p _ { i j } ^ { ( c , z ) } ) _ { n \times n } ,$ , where $\begin{array} { r } { p _ { i j } ^ { ( c , z ) } = \sum _ { k = 1 } ^ { m } \lambda _ { k , z } p _ { i j } ^ { ( k , z ) } } \end{array}$ . When constructing $P ^ { ( k , z + 1 ) } = ( p _ { i j } ^ { ( k , z + 1 ) } ) _ { n \times n } ( k { = } \bar { 1 } , 2 , . . . , m )$ , two cases are considered.

Case A. k $\neq r = 1$ . In this case, expert $e _ { k }$ provides $P ^ { ( k , z + 1 ) } = ( p _ { i j } ^ { ( k , z + 1 ) } ) _ { n \times n }$ as follows: for $i = 1 , 2 , \dots , n$ and $j = i + 1 , \ldots , n$ , then let $p _ { i j } ^ { ( k , z + 1 ) } { = } ( 1 - \mu ) p _ { i j } ^ { ( k , z ) } { + } \mu p _ { i j } ^ { ( c , z ) }$ , where the value of u is uniformly randomly selected from the interval $[ 0 . 2 , 1 ] , p _ { i i } ^ { ( k , z + 1 ) } = 1 - p _ { i j } ^ { ( k , z + 1 ) }$ , and $p _ { i i } ^ { ( k , z + 1 ) } { = } 0 . 5$

Case B. $k = r = 1$ . In this case, expert $e _ { 1 }$ provides $P ^ { ( k , z + 1 ) } = ( p _ { i i } ^ { ( k , z + 1 ) } ) _ { n \times n }$ as follows: for $i = 1 , 2 , \ldots , n$ and $j = i + 1 , \ldots , n$ , then let the value of $p _ { i i } ^ { ( k , z + 1 ) }$ be uniformly randomly selected from the interval [0,1], $\begin{array} { r } { \dot { p } _ { j i } ^ { ( k , z + 1 ) } = 1 - p _ { i j } ^ { ( k , z + 1 ) } } \end{array}$ , and $p _ { i i } ^ { ( k , z + \bar { 1 } ) } { = } 0 . 5$

Use the Eq. (22) to obtain the $s _ { 3 } ^ { ( k , z ) }$ . Repeat this process until $S _ { 3 } ^ { ( k , z ) } \ge \gamma$ $\scriptstyle ( k = r = 1 )$ .

$\operatorname { L e t } z = z + 1$ , then go to Step 3.

## References

[1] S. Alonso, E. Herrera-Viedma, F. Chiclana, F. Herrera, A web based consensus support system for group decision making problems and incomplete preferences, Information Sciences 180 (2010) 4477–4495.

[2] S. Alonso, I.J. Pérez, F.J. Cabrerizo, E. Herrera-Viedma, A linguistic consensus model for Web 2.0 communities, Applied Soft Computing 13 (2013) 149–157.

[3] F.H. Barron, B.E. Barrett, Decision quality using ranked attribute weights, Management Science 42 (1996) 1515-1523.

[4] D. Ben-Arieh, Z.F. Chen, Linguistic-labels aggregation and consensus measure for autocratic decision making using group recommendations, IEEE Transactions on Systems, Man, and Cybernetics Part A: Systems and Humans 36 (2006) 558–568.

[5] D. Ben-Arieh, T. Easton, Multi-criteria group consensus under linear cost opinion elasticity. Decision Support Systems 43 (2007) 713-721.

[6] D. Ben-Arieh, T. Easton, B. Evans, Minimum cost consensus with quadratic cost functions, IEEE Transactions on Systems, Man, and Cybernetics Part A: Systems and Humans 39 (2008) 210–217.

[7] G. Bordogna, M. Fedrizzi, G. Pasi, A linguistic modeling of consensus in group decision making based on OWA operators, IEEE Transactions on Systems, Man, and Cybernetics Part A: Systems and Humans 27 (1997) 126–133.

[8] F.J. Cabrerizo, J.M. Moreno, I.J. Pérez, E. Herrera-Viedma, Analyzing consensus approaches in fuzzy group decision making: advantages and drawbacks, Soft Computing 14 (2010) 451-463.

[9] F. Chiclana. LM. Tapia García, M.I. del Moral. E. Herrera-Videdma, A statistical comparative study of different similarity measures of consensus in group decision making, Information Sciences 221 (2013) 110–123.

[10] A.K. Choudhury, R. Shankar, M.K. Tiwari, Consensus-based intelligent group decision-making model for the selection of advanced technology, Decision Support Systems 42 (2006) 1776–1799.

[11] M. Danielson, L. Ekenberg, Y. He, Augmenting ordinal methods of attribute weight approximation, Decision Analysis 11 (2014) 21–26.

[12] Y.C. Dong, X. Chen, F. Herrera, Minimizing adjusted simple terms in the consensus reaching process with hesitant linguistic assessments in group decision making, Information Sciences 297 (2015) 95–117.

[13] Y.C. Dong, Z.P. Fan, S. Yu, Consensus building in a local context for the AHP-GDM with the individual pumerical scale and prioritization method JEEE Transactions on Fuzzy Systems 23 (2015) 354–368

[14] Y.C. Dong, E. Herrera-Viedma, Consistency-driven automatic methodology to set interval numerical scales of 2-tuple linguistic term sets and its use in the linguistic GDM with preference relation, IEEE Transactions on Cybernetics 45 (2015) 780–792.

[15] Y.C. Dong, C.C. Li, Y.F. Xu, X. Gu, Consensus-based group decision making under multi-granular unbalanced 2-tuple linguistic preference relations, Group Decision and Negotiation 24 (2015) 217–242.

[16] Y.C. Dong, Y.F. Xu, H.Y. Li, B. Feng, The OWA-based consensus operator under linguistic representation models using position indexes, European Journal of Operational Research 203 (2010) 455–463.

[17] Y.C. Dong, H.J. Zhang, Multiperson decision making with different preference representation structures: a direct consensus framework and its properties, Knowledge-Based Systems 58 (2014) 45–57.

[18] Y.C. Dong, G.Q. Zhang, W.C. Hong, Y.F. Xu, Consensus models for AHP group decision making under row geometric mean prioritization method, Decision Support Systems 49 (2010) 281–289.

[19] R. Efremov, D. Rios-Insua, A. Lotov, A framework for participatory decision support using Pareto frontier visualization, goal identification and arbitration, European Journal of Operational Research 199 (2009) 459–467.

[20] M.T. Escobar, J. Aguarón, J.M. Moreno-Jiménez, Some extensions of the precise consistency consensus matrix, Decision Support Systems 74 (2015) 67–77.

[21] M. Fedrizzi, J. Kacprzyk, S. Zadrożny, An interactive multi-user decision support system for consensus reaching processes using fuzzy logic with linguistic quantifiers, Decision Support Systems 4 (1988) 313–327.

[22] Z.W. Gong, X.X. Xu, H.H. Zhang, U.A. Ozturk, E. Herrera-Viedma, C. Xu, The consensus models with interval preference opinions and their economic interpretation, Omega 55 (2015) 81–90.

[23] Z.W. Gong, H.H. Zhang, J. Forrest, L.S. Li, X.X. Xu, Two consensus models based on the minimum cost and maximum return regarding either all individuals or one individual, European Journal of Operational Research 240 (2015) 183–192.

[24] F. Herrera, E. Herrera-Viedma, J.L. Verdegay, A model of consensus in group decision making under linguistic assessments, Fuzzy Sets and Systems 78 (1996) 73–87.

[25] F. Herrera, E. Herrera-Viedma, J.L. Verdegay, A rational consensus model in group decision making using linguistic assessments, Fuzzy Sets and Systems 88 (1997) 31–49.

[26] E. Herrera-Viedma, F.J. Cabrerizo, J. Kacprzyk, W. Pedrycz, A review of soft consensus models in a fuzzy environment, Information Fusion 17 (2014) 4–13.

[27] E. Herrera-Viedma, F. Chiclana, F. Herrera, S. Alonso, Group decision-making model with incomplete fuzzy preference relations based on additive consistency, IEEE Transactions on Systems, Man, and Cybernetics Part B: Cybernetics 31 (2007) 227–234.

[28] E. Herrera-Viedma, F. Herrera, F. Chiclana, A consensus model for multiperson decision making with different preference structures, IEEE Transactions on Systems, Man, and Cybernetics Part A: Systems and Humans 32 (2002) 394–402.

[29] J. Kacprzyk, Group decision making with a fuzzy linguistic majority, Fuzzy Sets and Systems 18 (1986) 105–118.

[30] J. Kacprzyk, M. Fedrizzi, A ‘soft’ measure of consensus in the setting of partial (fuzzy) preferences, European Journal of Operational Research 34 (1988) 316–325.

[31] J. Kacprzyk, M. Fedrizzi, H. Nurmi, Soft degrees of consensus under additive preferences and fuzzy majorities, in: J. Kacprzyk, H. Nurmi, M. Fedrizzi (Eds.), Consensus Under Fuzziness, Kluwer, Boston 1996, pp. 55–83

[32] J. Kacprzyk, S. Zadrozny, Soft computing and Web intelligence for supporting consensus reaching, Soft Computing 14 (2010) 833–846.

[33] J. Kim, A model and case for supporting participatory public decision making in edemocracy, Group Decision and Negotiation 17 (2008) 179–193.

[34] F. Mata, L. Martínez, E. Herrera-Viedma, An adaptive consensus support model for group decision-making problems in a multigranular fuzzy linguistic context, IEEE Transactions on Fuzzy Systems 17 (2009) 279–290.

[35] F. Mata, L.G. Pérez, S.M. Zhou, F. Chiclana, Type-1 OWA methodology to consensus reaching process in multi-granular linguistic contexts, Knowledge-Based Systems 58 (2014) 11–22.

[36] S.A. Orlovsky, Decision-making with a fuzzy preference relation, Fuzzy Sets and Sys tems 1 (1978) 155–167.

[37] I. Palomares, F.J. Estrella, L. Martínez, F. Herrera, Consensus under a fuzzy context: taxonomy, analysis framework AFRYCA and experimental case of study, Information Fusion 20 (2014) 252–271.

[38] I. Palomares, J. Liu, Y. Xu, L. Martínez, Modelling experts' attitudes in group decision making, Soft Computing 16 (2012) 1755–1766.

[39] I. Palomares, L. Martínez, A semisupervised multiagent system model to support consensus-reaching processes, IEEE Transactions on Fuzzy Systems 22 (2014) 762–777.

[40] I. Palomares, L. Martínez, F. Herrera, A consensus model to detect and manage noncooperative behaviors in large-scale group decision making, IEEE Transactions on Fuzzy Systems 22 (2014) 516–530.

[41] D.A. Pelta, R.R. Yager, Decision strategies in mediated multiagent negotiations: an optimization approach, IEEE Transactions on Systems, Man, and Cybernetics Part A: Systems and Humans 40 (2010) 635–640.

[42] I.J. Pérez, F.J. Cabrerizo, S. Alonso, E. Herrera-Viedma, A new consensus model for group decision making problems with non-homogeneous experts, IEEE Transactions on Systems Man, and Cybernetics 44 (2014) 494–498.

[43] I.J. Pérez, F.J. Cabrerizo, E. Herrera-Viedma, A mobile decision support system for dynamic group decision-making problems, IEEE Transactions on Systems, Man, and Cybernetics Part A: Systems and Humans 40 (2010) 1244–1256.

[44] P. Pérez-Asurmendi, F. Chiclana, Linguistic majorities with difference in support, Applied Soft Computing 18 (2014) 196–208.

Please cite this article as: Y. Dong, et al., Integrating experts' weights generated dynamically into the consensus reaching process and its applications in managing non-cooperative behaviors, Decision Support Systems (2016), http://dx.doi.org/10.1016/j.dss.2016.01.002

[45] R.M. Rodríguez, I. Palomares, L. Martínez, Attitude-based consensus model for heterogeneous group decision making, in: F. Sun, et al., (Eds.), Knowledge Engineering and Management, Advances in Intelligent Systems and Computing 214, Springer, 2014.

[46] T.L. Saaty, The Analytic Hierarchy Process, McGraw-Hill, New York, 1980.

[47] F. Seo, M. Sakawa, Fuzzy multiattribute utility analysis for collective choice, IEEE Transactions on Systems, Man, and Cybernetics 15 (1985) 45–53.

[48] B. Srdjevic, Linking analytic hierarchy process and social choice methods to support group decision-making in water management, Decision Support Systems 42 (2007) 2261–2273.

[49] B. Srdjevic, Z. Srdjevic, B. Blagojevic, K. Suvocarev, A two-phase algorithm for consensus building in AHP-group decision making, Applied Mathematical Modelling 37 (2013) 6670–6682.

[50] B.Z. Sun, W.M. Ma, An approach to consensus measurement of linguistic preference relations in multi-attribute group decision making and application, Omega 51 (2015) 83–92.

[51] T. Tanino, On group decision making under fuzzy preferences, in: J. Kacprzyk, M. Fedrizzi (Eds.), Multiperson Decision Making Using Fuzzy Sets and Possibility Theory, Kluwer Academic Publishers, Dordrecht 1990, pp. 172–185.

[52] M. Tavana, D.T. Kennedy, P. Joglekar, A group decision support framework for consensus ranking of technical manager candidates, Omega 24 (1996) 523–538.

[53] J. Wu, F. Chiclana, A social network analysis trust-consensus based approach to group decision-making problems with interval-valued fuzzy reciprocal preference relations, Knowledge-Based Systems 59 (2014) 97–107.

[54] Z.B. Wu, J.P. Xu, A consistency and consensus based decision support model for group decision making with multiplicative preference relations, Decision Support Systems 52 (2012) 757–767.

[55] Z.S. Xu, X.Q. Cai, On consensus of group decision making with interval utility values and interval preference orderings, Group Decision and Negotiation 22 (2013) 997–1019.

[56] Y.J. Xu, K.W. Li, H.M. Wang, Distance-based consensus models for fuzzy and multiplicative preference relations, Information Sciences 253 (2013) 56–73.

[57] R.R. Yager, On ordered weighted averaging aggregation operators in multicriteria decision making, IEEE Transactions on Systems, Man, and Cybernetics 18 (1988) 183–190.

[58] R.R. Yager, Quantifier guided aggregation using OWA operators, International Journal of Intelligence Systems 11 (1996) 49–73.

[59] R.R. Yager, Penalizing strategic preference manipulation in multi-agent decision making, IEEE Transactions on Fuzzy Systems 9 (2001) 393–403.

[60] R.R. Yager, Defending against strategic manipulation in uninorm-based multi-agent decision making, European Journal of Operational Research 141 (2002) 217–232.

[61] R.R. Yager, Intelligent social network analysis using granular computing, International Journal of Intelligence Systems 23 (2008) 1197–1219.

[62] K. Yoon, C.L. Hwang, Multiple Attribute Decision Making: Methods and Applications, Springer, Berlin, 1981.

[63] L. Yu, K.K. Lai, A distance-based group decision-making methodology for multiperson multi-criteria emergency decision support, Decision Support Systems 51 (2011) 307–315.

[64] L.A. Zadeh, A computational approach to fuzzy quantifiers in natural languages, Computers & Mathematcs with Applications 9 (1983) 149–184.

[65] S. Zadrozny, J. Kacprzyk, An Internet-based group decision and consensus reaching support system, in: X. Yu, J. Kacprzyk (Eds.), Applied Decision Support with Soft Computing, Springer, Heidelberg 2003, pp. 263–275.

[66] B.W. Zhang, Y.C. Dong, Y.F. Xu, Maximum expert consensus models with linear cost function and aggregation operators, Computers and Industrial Engineering 66 (2013) 147–157.

[67] G.Q. Zhang, Y.C. Dong, Y.F. Xu, Consistency and consensus measures for linguistic preference relations based on distribution assessments, Information Fusion 17 (2014) 46–55.

[68] B.W. Zhang, Y.C. Dong, Y.F. Xu, Multiple attribute consensus rules with minimum adjustments to support consensus reaching, Knowledge-Based Systems 67 (2014) 35–58.

[69] G.Q. Zhang, Y.C. Dong, Y.F. Xu, H.Y. Li, Minimum-cost consensus models under aggregation operators, IEEE Transactions on Systems, Man, and Cybernetics Part A: Systems and Humans 41 (2011) 1253–1261.

Yucheng Dong is a professor at the Business School, Sichuan University, China. He received his Ph.D. degree in management from Xi'an Jiaotong University in 2008. His current research interests include group decision making, decision support systems, and computing with words in decision making. Dr. Dong published over 50 international journal papers in Decision Support Systems, European Journal of Operational Research, IEEE Transactions on Cybernetics, IEEE Transactions on Fuzzy Systems, IEEE Transactions on Systems, Man, and Cybernetics, among others. Dr. Dong is a member of the editorial board of the journal Information Fusion.

Hengjie Zhang is a Ph.D. candidate at the Business School, Sichuan University, China. He received his B.S. degree from the School of Economics and Management, Chongqing University of Posts and Telecommunications in 2012. His research interests include group decision making, consensus reaching process, and decision support systems.

Enrique Herrera-Viedma is a Professor of Computer Science and the Vice-President for Research and Transfer in University of Granada. He received the M.Sc. and Ph.D. degrees in Computer Science from the University of Granada in 1993 and 1996, respectively. His current research interests include group decision making, consensus models, linguistic modelling, and aggregation of information, information retrieval, bibliometric, digital libraries, web quality evaluation, recommender systems, and social media. His h-index is 48 with more than 7500 citations received [WoS], He was identified in 2014 and 2015 as one of the world's most influential researchers by the Shanghai Center and Thomson Reuters in both Computer Science and Engineering. Dr. Herrera-Viedma is an Associate Editor of several journals such as IEEE Transactions on Systems Man and Cybernetics: Systems, Information Sciences, and Knowledge-Based Systems.
