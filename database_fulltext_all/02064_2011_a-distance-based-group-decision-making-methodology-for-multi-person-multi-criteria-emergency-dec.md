---
otero_id: 2064
otero_key: "3AQEDH7D"
title: "A distance-based group decision-making methodology for multi-person multi-criteria emergency decision support"
authors: "Lean Yu; Kin Keung Lai"
year: "2011"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2010.11.024"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# A distance-based group decision-making methodology for multi-person multi-criteria emergency decision support

Lean Yu <sup>a,</sup>⁎, Kin Keung Lai <sup>b</sup>

<sup>a</sup> MADIS, Institute of Systems Science, Academy of Mathematics and Systems Science, Chinese Academy of Sciences, Beijing 100190, China

<sup>b</sup> Department of Management Sciences, City University of Hong Kong, Tat Chee Avenue, Kowloon, Hong Kong

## a r t i c l e i n f o

Available online 25 November 2010

Keywords: Multi-criteria decision-making Group decision-making Group consensus Emergency management Emergency decision support

## a b s t r a c t

In this paper, a distance-based group decision-making (GDM) methodology is proposed to solve unconventional multi-person multi-criteria emergency decision-making problems. In this model, some decision-makers are <sup>fi</sup>rst identi<sup>fi</sup>ed to formulate a group decision-making framework. Then a standard multicriteria decision-making (MCDM) process is performed on speci<sup>fi</sup>c decision-making problems and different decision results are obtained from different decision-makers. Finally, these different decision results are aggregated into a group consensus to support the <sup>fi</sup>nal decision-making. For illustration and veri<sup>fi</sup>cation purposes, a numerical example and a practical unconventional emergency decision case are presented. Experimental results obtained demonstrate that the proposed distance-based multi-criteria GDM methodology can improve decision-making objectivity and emergency management effectiveness.

© 2010 Elsevier B.V. All rights reserved.

## 1. Introduction

Unconventional emergency events, such as earthquakes and hurricanes, often lead to unexpected catastrophic consequences [5]. When such devastating incidents occur, emergency planning and management play a crucial role in reduction and mitigation of their effects. In the emergency planning and management, there are a great many emergency decision-making problems that need to be solved, to handle effects of the destructive events. Usually, an emergency decision has the following two distinct features. First, an emergency decision must often be made in a short period of time using partial or incomplete information, especially in the early stages of the disaster occurrence. Accordingly emergence group decision-making (GDM) is an intractable task, particularly when handling some unconventional high impact emergency events. Second, these decisions may have potentially serious outcomes. In many situations, a wrong decision could result in deadly consequences [13]. In view of the unique characteristics of emergency decisions, using group decision support systems (GDSS) [6,8,9] to handle emergency decision problems could be extremely valuable.

Some previous studies [13,15,27] also revealed that the GDSS has great potential applications in modern emergency planning and management. For example, Levy and Taji [13] proposed a group analytic network process (GANP) to construct a GDSS to support hazard planning and emergency management under incomplete information. In their study, a typical unconventional emergency event, a chemical spill in the city of Brandon, Manitoba is simulated. With application in evacuation and shelter-in-place decisions, it is shown that the proposed GANP model improves emergency management effectiveness, decision transparency, and user satisfaction [13]. Zografos et al. [27] presented a methodological framework for developing a hazardous material emergency response (HAMER) decision support system (DSS) to manage emergency response operations for large-scale industrial accidents in Western Attica, Greece. Similarly, Mendonca et al. [15] designed a gaming simulation to assess GDSS for emergency response in emergency management.

Although these existing studies have shown that GDSS can improve emergency management effectiveness and decision transparency due to the fact that it can integrate group wisdom of multiple decision-makers into one group wisdom, there are two key issues that are apparently not solved well by GDSS. On the one hand, in the process of multi-criteria decision-making (MCDM), determining a set of suitable weights for multiple evaluation criteria is often considered to be a very dif<sup>fi</sup>cult task. In the existing literature, many researchers usually set some arbitrary weights for each criterion to solve speci<sup>fi</sup>ed decision-making problems in terms of subjective judgments of decision-makers. But such a processing method will add the subjectivity and thus reducing the decision accuracy, sometimes leading to wrong decision results. On the other hand, in the process of using GDM, evolving an effective group consensus out of different judgments from different decision-makers, is still an unsolved issue in the previous studies.

Inspired by the GDSS, this study attempts to propose a distancebased multi-criteria group decision-making (GDM) methodology to support multi-person emergency decision problems. As is known, GDM is one of the most active research <sup>fi</sup>elds within MCDM [3]. In

GDM, group members (i.e., decision-makers) <sup>fi</sup>rst make their own judgments on the same decision problem independently, i.e. decision actions and alternatives, based on multiple evaluation criteria. These judgments from different decision-makers are then aggregated into a group consensus to support the <sup>fi</sup>nal decision. Different from previous studies, this study tries to give an effective solution to the two unresolved issues, and to construct a distance-based multi-criteria GDM methodology for multi-person emergency decision support.

Generally, the proposed distance-based multi-criteria GDM methodology is comprised of three stages. In the <sup>fi</sup>rst stage, some decision-makers (DMs) are <sup>fi</sup>rst identi<sup>fi</sup>ed to formulate a GDM framework. Then a standard MCDM process is performed on the speci<sup>fi</sup>c decision-making problems, and accordingly different decision results are obtained from different decision-makers in the second stage. In the third stage, these different decision results are aggregated into a group consensus to support the <sup>fi</sup>nal decision. The main purpose of this study is to propose a new distance-based multi-criteria GDM model to support unconventional emergency decision-making problems. Using the proposed distance-based GDM model, many practical emergency decision-making problems can be solved effectively. For these real-world problems, decisions are made on the basis of a set of pre-de<sup>fi</sup>ned criteria. Therefore, the proposed distance-based multi-criteria GDM methodology is suitable for solving these multi-person emergency decision-making problems.

The main contribution of this study is that a new distance-based multi-criteria GDM methodology is proposed to support unconventional emergency decisions, by providing a rational solution to the two unresolved key issues. Compared with traditional GDM methods, our proposed distance-based multi-criteria GDM model has three distinct characteristics. First, the decision-makers' judgments/evaluations are made on the basis of a set of criteria to formulate a multi-person multi-criteria GDM framework. This makes the decision results more objective than traditional single-person MCDM methods [10,11,14,16,17]. Second, the weights of evaluation criteria are determined based upon the data itself, thus reducing decision bias and adding the objectiveness to the proposed GDM methodology. Finally, different from previous subjective methods and traditional time-consuming iterative procedures, this paper proposes a fast optimization technique to integrate the different decision opinions, and to make the aggregation of different decision opinions simple.

The main purpose of the proposed multi-criteria GDM methodology is to improve decision accuracy, and to enhance decision transparency and thus to increase decision effectiveness. The rest of this paper is organized as follows. In Section 2, the proposed distancebased multi-criteria GDM methodology is described in detail. For illustration and veri<sup>fi</sup>cation purposes, Section 3 presents a numerical example and a practical emergency decision case to illustrate the implementation process, and to verify the effectiveness of the proposed distance-based multi-criteria GDM methodology. Finally, some concluding remarks are drawn in Section 4.

## 2. Formulation of distance-based multi-criteria GDM methodology

In this section, a general framework for multi-criteria GDM methodology is <sup>fi</sup>rst presented. Then some main procedures or steps involved in the proposed distance-based multi-criteria GDM methodology are described in detail. Finally a summary for distance-based multi-criteria GDM methodology is given.

## 2.1. General framework for multi-criteria GDM methodology

In this study, a general multi-criteria GDM methodology framework is proposed for complex and multi-faceted decision-making problems. In order to help readers' understand multi-criteria GDM problems, a general form of multi-criteria GDM problem is shown in Table 1.

In Table 1 $, ( C _ { 1 } , C _ { 2 } , \cdots , C _ { m } )$ denotes a number of evaluation criteria or evaluation attributes, $( A _ { 1 } , A _ { 2 } , \cdots , A _ { n } )$ represents a set of alternatives or actions, $\left( D M _ { 1 } , D M _ { 2 } , \cdots , D M _ { p } \right)$ is a group of decision-makers and $U _ { k } ( C _ { j } ( A _ { i } ) ) ( i = 1 , 2 , \cdots , n ; j = 1 , 2 , \cdots , m ; k = 1 , 2 , \cdots , p )$ denotes the utility value (evaluation value) of the ith alternative under the jth evaluation criterion in terms of the judgment of the kth decisionmaker. The main feature of the multi-criteria GDM framework for solving decision-making problems is to formulate a comprehensive ordering/ranking mechanism for the given alternatives, based on a set of speci<sup>fi</sup>ed evaluation criteria and a group of decision-makers. To realize this, a general framework for multi-person multi-criteria GDM methodology is proposed, as shown in Fig. 1.

As can be seen from Fig. 1, we can <sup>fi</sup>nd that the proposed multicriteria GDM methodology consists of three main procedures: identi<sup>fi</sup>cation of group decision-makers, implementation of standard MCDM process for each decision-maker and formulation of group consensus, which are elaborated in the following subsections.

## 2.2. Identification of group decision-makers in GDM environment

In GDM environment, identi<sup>fi</sup>cation of members of the group decision-makers is an extremely important step as only competent decision-makers can effectively make eligible decisions based on a set of speci<sup>fi</sup>ed evaluation criteria; incompetent decision-makers can lead to some unexpected decision results.

Usually, multiple domain experts and important leaders from different <sup>fi</sup>elds can form a decision group to solve speci<sup>fi</sup>ed decisionmaking problems. In particularly, when we try to solve some complex and important decision-making problems, the decisions are often made by a decision group not only because of the problem complexity but also because of wider implications of the decision in terms of responsibility. For example, in the process of solving some unconventional emergency event (e.g., earthquake) decision-making problems, some experts from seismology, geology, meteorology and catastrophology, as well as of<sup>fi</sup>cers from government departments should be included in the decision group. In order to form an effective decision group, the GDM manager or moderator, in most situations, is required to have abundant knowledge of GDM and have the capability of identifying and selecting some suitable experts in speci<sup>fi</sup>ed areas. In this way, GDM environment can be constructed and GDM consensus can be formed effectively.

## 2.3. Implementation of standard MCDM proces

For a speci<sup>fi</sup>ed decision problem or decision alternative, different decision-makers usually give different estimations or judgments over a set of evaluation criteria $C = ( C _ { 1 } , C _ { 2 } , \cdots , C _ { m } )$ ). That is, a standard MCDM process is implemented for a speci<sup>fi</sup>ed decision alternative and a set of evaluation criteria after a suitable decision group is formed.

MCDM is a well-known branch of a general class of operations research (OR) models, which deal with a set of decision alternatives in terms of a number of evaluation criteria. In existing studies, there are a great number of multi-criteria models and approaches [20]. However, the standard MCDM process can be summarized in the following four main steps.

A general form of multi-criteria GDM problem.

<table><tr><td rowspan="2">Alternatives</td><td colspan="3"> $DM_1$ </td><td>......</td><td colspan="3"> $DM_p$ </td></tr><tr><td> $C_1$ </td><td>...</td><td> $C_m$ </td><td> $C_1...C_m$ </td><td> $C_1$ </td><td>...</td><td> $C_m$ </td></tr><tr><td> $A_1$ </td><td> $U_1(C_1(A_1))$ </td><td>...</td><td> $U_1(C_m(A_1))$ </td><td>...</td><td> $U_p(C_1(A_1))$ </td><td>...</td><td> $U_p(C_m(A_1))$ </td></tr><tr><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td></tr><tr><td> $A_n$ </td><td> $U_1(C_1(A_n))$ </td><td>...</td><td> $U_1(C_m(A_n))$ </td><td>...</td><td> $U_p(C_1(A_n))$ </td><td>...</td><td> $U_p(C_m(A_n))$ </td></tr></table>

![](/api/attachments/3AQEDH7D/fulltext/images/67cfda25930fca9185d7e26f1b1d49e06643b8f3bc62593336c2c9d6e8e00242.jpg)  
Fig. 1. A general framework for multi-person multi-criteria GDM methodology.

(1) Criteria selection. For any given decision-making problem, a number of suitable evaluation criteria should be <sup>fi</sup>rst determined. Very often different decision problems have different evaluation criteria. However, a MCDM process must have a number of evaluation criteria beforehand. If there are too many criteria for a decision-making problem, it is necessary to extract a subset of criteria from out of a vast number of criteria.

(2) Alternative formulation. In the process of MCDM, some feasible decision alternatives should be formulated so that a suitable number of decision alternatives can be used for evaluation, in terms of a set of decision criteria. Meantime, different utility values or evaluation scores (evaluation values) are assigned to each alternative in terms of different criteria.

(3) Criteria weight determination. In MCDM process, determination of the importance of various criteria is a critical step in formulation of the MCDM. In existing literature, there are many methods to determine criteria weights in the MCDM process. Typical approaches for criteria weight determination include expert method, Delphi method, AHP method, variation coef<sup>fi</sup>- cient method and entropy-based method [18,19]. In these approaches, the <sup>fi</sup>rst three methods involve the subjective in<sup>fl</sup>uence of the decision-maker, while the latter two are ascertained without direct participation of the decision-maker. The main advantage of the latter two methods over the former three methods is that they remove the subjectivity of the decision-maker in determining criteria weights, and are very useful in cases where decision-makers disagree on values of weights. Th-erefore, the latter two approaches are often considered as objective methods, which are more reliable than the former three subjective methods. Therefore, this paper applies the latter two objective methods to determine weights of criteria for comparison purpose. Meantime, another objective distance-based method is also proposed for criteria weight determination.

Usually, objective methods are based on the consideration that importance of a criterion is a direct function of the information conveyed by it, relative to a whole set of alternatives. In terms of the foregoing consideration, it concludes that a criterion is more important, if there is a greater dispersion in evaluations of alternatives [19]. This conclusion will be used as a generic rule to determine objective criteria weights in the subsequent task. Suppose there is a standard MCDM problem, and the matrix $\{ U ( C _ { j } ( A _ { i } ) ) \} ( i = 1 , 2 , \cdots , n ; j = 1 , 2 , \cdots , m )$ is used for the evaluation process, where U(C (A )) denotes utility values or evaluation sco-res (evaluation values) of alternative $A _ { i } ( i = 1 , 2 , \cdots , n )$ based on criterion $C _ { j } ( j = 1 , 2 , \cdots , m ) ,$ , and m and n are the maximum numbers of criteria and alternatives, respectively.

2.3.1. Variation coefficient method for criteria weight determination For the variation coef<sup>fi</sup>cient method [18], the working process for criteria weight determination is shown as follows.

(a) Normalization of evaluation value. For every criterion $j ( j =$ $1 , 2 , \cdots , m )$ , all evaluation values are divided by $\sum _ { i = 1 } ^ { n } U ( C _ { j }$ $\left( A _ { i } \right) )$ , i.e.

$$
U ^ {\prime} \left(C _ {j} (A _ {i})\right) = \frac {U \left(C _ {j} (A _ {i})\right)}{\sum_ {i = 1} ^ {n} U \left(C _ {j} (A _ {i})\right)}.\tag{1}
$$

In this way, all evaluation values are normalized into the interval [0, 1]. The main purpose of normalization is to remove the effect of magnitude of data.

(b) Mean computation of the normalized evaluation value. For the jth evaluation criterion, the average evaluation value (i.e., mean value) can be calculated by

$$
\overline {{U \left(C _ {j}\right)}} = \frac {1}{n} \sum_ {i = 1} ^ {n} U ^ {\prime} \left(C _ {j} (A _ {i})\right).\tag{2}
$$

(c) Standard deviation computation of the normalized evaluation value. Using the mean value and evaluation values, the value of standard deviation is computed by the following equation:

$$
\sigma \left(U \left(C _ {j}\right)\right) = \sqrt {\frac {1}{n} \sum_ {i = 1} ^ {n} \left(U ^ {\prime} \left(C _ {j} \left(A _ {i}\right)\right) - \overline {{U \left(C _ {j}\right)}}\right) ^ {2}}.\tag{3}
$$

(d) Variation coef<sup>fi</sup>cient computation for dispersion measurement. Using the mean value and standard deviation, the variation coef<sup>fi</sup>cient of the jth criterion for dispersion measurement can be expressed by

$$
\delta_ {j} = \frac {\sigma (U (C _ {j}))}{\overline {{U (C _ {j})}}}\tag{4}
$$

In this dispersion measurement, the larger the variation coef<sup>fi</sup>cient, the higher is the dispersion degree, which is consistent with the previous generic rule.

(e) Determination of criteria weights. For each criterion $C _ { j } ,$ the weight can be determined by the following form

$$
w _ {j} ^ {C} = \frac {\delta_ {j}}{\sum_ {j = 1} ^ {n} \delta_ {j}}\tag{5}
$$

## 2.3.2. Entropy-based method for criteria weight determination

For the entropy-based method [19], the process of criteria weight determination consists of the following four steps:

(a) Normalization of evaluation values. Similar to the variation coef<sup>fi</sup>cient method, the entropy method uses the same normalization method. Accordingly, the normalized evaluation values $U ^ { \prime } ( C _ { j } ( A _ { i } ) )$ can be obtained from Eq. (1).

(b) Entropy computation for the jth evaluation criterion. For each criterion $C _ { j } ,$ the entropy value can be represented as

$$
E n _ {j} = - k \sum_ {i = 1} ^ {n} U ^ {\prime} \left(C _ {j} (A _ {i})\right) \cdot \log \left(U ^ {\prime} \left(C _ {j} (A _ {i})\right)\right)\tag{6}
$$

where k is a constant and is determined through relation $k = 1 / \log ( m ) [ 1 9 ]$ and m is the number of criteria.

(c) Dispersion measurement for each criterion $C _ { j } .$ In the entropy method, the measure of dispersion for the jth evaluation criterion [19] is expressed as

$$
\varphi_ {j} = 1 - E n _ {j}\tag{7}
$$

(d) Determination of criteria weights. For each criterion $C _ { j } ,$ the weight can be determined by

$$
w _ {j} ^ {C} = \frac {\varphi_ {j}}{\sum_ {j = 1} ^ {n} \varphi_ {j}}\tag{8}
$$

## 2.3.3. Distance-based method for criteria weight determination

Motivated by the previous two objective methods, a distancebased objective weight determination method is proposed in terms of optimistic and pessimistic utility values. The distance-based method works as follows.

(a) Normalization of evaluation values. Similar to the variation coef<sup>fi</sup>cient method and entropy-based method, the distancebased method applies the same normalization method to normalize initial evaluation values. Accordingly, the normalized evaluation values $U ^ { \prime } ( C _ { j } ( A _ { i } ) )$ can be obtained from Eq. (1).

(b) Determination of optimistic and pessimistic evaluation values for the jth evaluation criterion. For each criterion $C _ { j } ,$ optimistic and pessimistic values are de<sup>fi</sup>ned as

$$
\text { Optimistic   values }: U ^ {+} = \left(U _ {1} ^ {+}, U _ {2} ^ {+}, \dots , U _ {m} ^ {+}\right)\tag{9}
$$

Pessimistic values : $U ^ { - } = ( U _ { 1 } ^ { - } , U _ { 2 } ^ { - } , \cdots , U _ { m } ^ { - } )$

10

where

$$
U _ {j} ^ {+} = \left\{ \begin{array}{l} \max _ {1 \leq i \leq n} \Bigl \{U ^ {\prime} \left(C _ {j} (A _ {i})\right) \Bigr \}, j \in J _ {1}, \\ \min _ {1 \leq i \leq n} \Bigl \{U ^ {\prime} \left(C _ {j} (A _ {i})\right) \Bigr \}, j \in J _ {2}. \end{array} \right.\tag{11}
$$

$$
U _ {j} ^ {-} = \left\{ \begin{array}{l} \min _ {1 \leq i \leq n} \Big \{U ^ {\prime} \Big (C _ {j} (A _ {i}) \Big) \Big \}, j \in J _ {1}, \\ \max _ {1 \leq i \leq n} \Big \{U ^ {\prime} \Big (C _ {j} (A _ {i}) \Big) \Big \}, j \in J _ {2}. \end{array} \right.\tag{12}
$$

where $J _ { 1 }$ represents the positive criteria (e.g., pro<sup>fi</sup>t) and $J _ { 2 }$ is the negative criteria (e.g., cost).

(c) Distance computation between criteria values and optimistic/ pessimistic values. Using optimistic and pessimistic values, the distance between utility values of the jth $( j = 1 , 2 , \cdots , m )$ criteria and optimistic/pessimistic values of the criteria can be calculated by

$$
d _ {j} ^ {+} = \sqrt {\sum_ {i = 1} ^ {n} \left(U ^ {\prime} \left(C _ {j} (A _ {i})\right) - U _ {j} ^ {+}\right) ^ {2}},\tag{13}
$$

$$
d _ {j} ^ {-} = \sqrt {\sum_ {i = 1} ^ {n} \left(U ^ {\prime} \left(C _ {j} (A _ {i})\right) - U _ {j} ^ {-}\right) ^ {2}}.\tag{14}
$$

(d) Dispersion measurement for each criterion $C _ { j } .$ In the distancebased method, the measure of dispersion for the jth criterion is expressed as

$$
\xi_ {j} = \frac {d _ {j} ^ {+}}{d _ {j} ^ {+} + d _ {j} ^ {-}}\tag{15}
$$

According to $\operatorname { E q . } \left( 1 3 \right)$ , the larger the value of $\langle \xi _ { j } ,$ the larger is the dispersion measure and accordingly the more important is the jth criterion, which is also consistent with the generic rule of criteria weight determination.

(e) Determination of criteria weights. For each criterion $C _ { j } ,$ the weight can be determined based on the dispersion measurement, as shown in the following equation.

$$
w _ {j} ^ {C} = \frac {\xi_ {j}}{\sum_ {j = 1} ^ {n} \xi_ {j}}\tag{16}
$$

Using criteria weights and utility values of every alternative, the alternative evaluation can be easily conducted in the next step.

(4) Alternative evaluation. After determining the criteria weights, the decision score of the ith alternative evaluation can be computed in the following additive form:

$$
z _ {i} = \sum_ {j = 1} ^ {m} w _ {j} ^ {C} \cdot U \left(C _ {j} (A _ {i})\right), i = 1, \dots , n.\tag{17}
$$

Using the aforementioned four steps, a standard MCDM process can be easily performed.

## 2.4. Formulation of group consensus

In the multi-person multi-criteria GDM framework, every decision-maker can perform the standard MCDM process for a speci<sup>fi</sup>ed decision problem and obtain a decision result based on his/her own evaluations. A subsequent task is to aggregate different decision results to an integrated group consensus. Suppose that there are p decision-makers (DMs), the p DMs produce p different decision results, i.e.

$$
Z _ {k} = z _ {k i} = (z _ {k 1}, z _ {k 2}, \dots , z _ {k n}), k = 1, \dots , p.\tag{18}
$$

In order to fuse the different decision results, le $\cdot Z { = } \psi ( Z _ { 1 } , Z _ { 2 } , \cdots Z _ { p } )$ be the aggregation of the p decision results, where $\psi ( \cdot )$ is an aggregation function. Now how to determine the aggregation function or how to aggregate these different decision results into a group consensus is an important and critical problem under the multiperson multi-criteria GDM environment. Generally speaking, there are many aggregation techniques and rules that can be used to aggregate different decision results. Some of them are linear, while others are nonlinear. Interested readers may kindly refer to Alfares and Duffuaa [1], Yager [24,25], Delgado et al. [7], Cabrerizo et al. [4] Lee [12], Xu [21,22], Zhang and Lu [26], and Xu [23] for more details. Usually, decision results of the p group members will be aggregated by using a commonly used linear additive procedure, i.e.

$$
\begin{array}{l} Z = \sum_ {k = 1} ^ {p} w _ {k} ^ {D M} Z _ {k} \\ \qquad = \left(\sum_ {k = 1} ^ {p} w _ {k} ^ {D M} z _ {k 1}, \sum_ {k = 1} ^ {p} w _ {k} ^ {D M} z _ {k 2}, \dots , \sum_ {k = 1} ^ {p} w _ {k} ^ {D M} z _ {k n}\right) \end{array}\tag{19}
$$

where $w _ { k } ^ { D M }$ is the weight of the kth decision-maker, $k = 1 , 2 , . . . , p .$ . The weights usually satisfy the following normalization condition:

$$
\sum_ {k = 1} ^ {p} w _ {k} ^ {D M} = 1\tag{20}
$$

Now our problem is how to determine the optimal weight $w _ { k } ^ { D M }$ of the kth decision-maker under the multi-person multi-criteria GDM environment. Often, different decision results from different DMs are largely dispersed and separated. In order to achieve the maximum similarity, decision results should move towards one another. This is the principle on the basis of which an aggregated decision result is generated. Based upon this principle, a distance-based least-square aggregation optimization approach is proposed to integrate different decision results produced by different DMs.

The generic idea of this proposed distance-based aggregation optimization approach is to minimize the sum of the squared distance from one decision result to another and thus make them achieve maximum agreement. Speci<sup>fi</sup>cally, the squared distance between $Z _ { k }$ and $Z _ { l }$ can be de<sup>fi</sup>ned as

$$
\begin{array}{c} d _ {k l} ^ {2} = \left(\sqrt {(w _ {k} ^ {D M} Z _ {k} - w _ {l} ^ {D M} Z _ {l}) ^ {2}}\right) ^ {2} \\ = \sum_ {i = 1} ^ {n} \Big (w _ {k} ^ {D M} z _ {k i} - w _ {l} ^ {D M} z _ {l i} \Big) ^ {2} \end{array}\tag{21}
$$

where $k ,$ l represent the kth and lth decision-makers, i.e. $k = 1 , 2 , \cdots , p ,$ $l = 1 , 2 , \cdots , p$ and i denotes the ith alternative, $i = 1 , 2 , \cdots , n .$

Using this squared distance, we can construct the following optimization model, which minimizes the sum of the squared distances between all pairs of decision results with weights:

$$
\begin{array}{l} \text {Min} D = \sum_ {k = 1} ^ {p} \sum_ {l = 1, k \neq l} ^ {p} d _ {k l} ^ {2} = \sum_ {k = 1} ^ {p} \sum_ {l = 1, k \neq l} ^ {p} \\ \left[ \sum_ {i = 1} ^ {n} \left(w _ {k} ^ {D M} z _ {k i} - w _ {l} ^ {D M} z _ {l i}\right) ^ {2} \right] \end{array}\tag{22}
$$

Subject to $\begin{array} { r } { \sum _ { k = 1 } ^ { p } w _ { k } ^ { D M } = 1 } \end{array}$

23

$$
w _ {k} ^ {D M} \geq 0, k = 1, 2, \dots , p\tag{24}
$$

In order to obtain the aforementioned optimal weights of the decision-makers, constraint $\left( \operatorname { E q . } \left( 2 4 \right) \right)$ is not considered, for convenience of computation. If the solution turns out to be non-negative, then constraint (Eq. (24)) is satis<sup>fi</sup>ed automatically. Using the Lagrange multiplier theorem, Eqs. (22) and (23) in the foregoing optimization problem are combined to be the following Lagrangian function:

$$
\begin{array}{c} L \Big (w ^ {D M}, \lambda \Big) = \sum_ {k = 1} ^ {p} \sum_ {l = 1, k \neq l} ^ {p} \left[ \sum_ {i = 1} ^ {n} \Big (w _ {k} ^ {D M} z _ {k i} - w _ {l} ^ {D M} z _ {l i} \Big) ^ {2} \right] \\ - 2 \lambda \Big (\sum_ {k = 1} ^ {p} w _ {k} ^ {D M} - 1 \Big) \end{array}\tag{25}
$$

Differentiating Eq. (25) with $w _ { k } ^ { D M }$ , we can obtain

$$
\frac {\partial L}{\partial w _ {k} ^ {D M}} = 2 \sum_ {l = 1, k \neq l} ^ {p} \left[ \sum_ {i = 1} ^ {n} \left(w _ {k} ^ {D M} z _ {k i} - w _ {l} ^ {D M} z _ {l i}\right) z _ {k i} \right] - 2 \lambda = 0\tag{26}
$$

for each $k = 1 , 2 , . . . , p .$

Eq. (26) can be simpli<sup>fi</sup>ed as

$$
(p - 1) \left(\sum_ {i = 1} ^ {n} z _ {k i} ^ {2}\right) w _ {k} ^ {D M} - \sum_ {l = 1, k \neq l} ^ {p} \left[ \sum_ {i = 1} ^ {n} (z _ {k i} z _ {l i}) \right] w _ {l} ^ {D M} - \lambda = 0\tag{27}
$$

for each $k = 1 , 2 , . . . , p .$

In Eq. (27), for convenience of representation, let $b _ { k l } = ( p - 1 )$ $\begin{array} { r } { \left( \sum _ { i = 1 } ^ { n } z _ { k i } ^ { 2 } \right) , ( k = l = 1 , 2 , \cdots , p ) , b _ { k l } = - \bar { \sum } _ { i = 1 } ^ { n } \left( z _ { k i } z _ { l i } \right) , ( k \neq l , k = 1 , 2 , \cdots , } \end{array}$ $p ; l = 1 , 2 , \cdots , p )$ , then we have

$$
B = (b _ {k l}) _ {p \times p} = \left[ \begin{array}{c c c} (p - 1) \Big (\sum_ {i = 1} ^ {n} z _ {1 i} ^ {2} \Big) & \dots & - \sum_ {i = 1} ^ {n} \Big (z _ {1 i} z _ {p i} \Big) \\ - \sum_ {i = 1} ^ {n} (z _ {2 i} z _ {1 i}) & \dots & - \sum_ {i = 1} ^ {n} \Big (z _ {2 i} z _ {p i} \Big) \\ \dots & \dots & \dots \\ - \sum_ {i = 1} ^ {n} \Big (z _ {p i} z _ {1 i} \Big) & \dots & (p - 1) \Big (\sum_ {i = 1} ^ {n} z _ {p i} ^ {2} \Big) \end{array} \right]\tag{28}
$$

In addition, if we set $W ^ { D M } = ( w _ { 1 } ^ { D M } , w _ { 2 } ^ { D M } , \cdots , w _ { p } ^ { D M } ) ^ { T }$ and $I = ( 1 , 1 , . . . , 1 ) ^ { T }$ with superscript T denoting the transpose, then Eqs. (27) and (23) can be rewritten in a matrix form.

$$
B W ^ {D M} - \lambda I = 0\tag{29}
$$

$$
I ^ {T} W ^ {D M} = 1\tag{30}
$$

Similarly, Eq. (22) can be expressed in a matrix form $\mathsf { a s } D =$ $( W ^ { D M } ) ^ { T } B W ^ { \breve { D M } }$ . Because D is a squared distance, which is usually larger than zero, B should be positive de<sup>fi</sup>nite and invertible. Using Eqs. (29) and (30) together, we can obtain

$$
\lambda^ {*} = 1 / \left(I ^ {T} B ^ {- 1} I\right)\tag{31}
$$

$$
\left(W ^ {D M}\right) ^ {*} = \left(B ^ {- 1} I\right) / \left(I ^ {T} B ^ {- 1} I\right)\tag{32}
$$

Since B is a positive de<sup>fi</sup>nite matrix, all its principal minors will be strictly positive and thus B is a non-singular M-matrix [2]. According to the properties of M-matrices, we know $B ^ { - 1 }$ is non-negative. Therefore, $\left( W ^ { D M } \right) ^ { * } \geq 0$ , which implies that the non-negative constraint in $\mathtt { E q . } ( 2 4 )$ can be satis<sup>fi</sup>ed.

Using the decision-makers' weights from Eq. (32), group consensus can be easily obtained. To summarize, the proposed distancebased multi-person multi-criteria GDM model is composed of six main procedures:

(1) To construct the GDM environment, some relevant decisionmakers are <sup>fi</sup>rst identi<sup>fi</sup>ed as members of the GDM.

(2) Based on the speci<sup>fi</sup>ed decision problems, different decision criteria are selected for decision alternative evaluation.

(3) In terms of details of decision problems, various decision alternatives are formulated. Meantime, different utility values on every decision alternative are given by different decisionmakers in terms of different criteria.

(4) Using the utility values, some subjective (e.g., Delphi and AHP methods) or objective (e.g., variation coef<sup>fi</sup>cient method, entropy method and distance-based method) criteria weight determination methods are used to determine criteria weights in the MCDM process.

(5) For every alternative, different decision-makers can give different decision results using utility values and criteria weights of different criteria in terms of the standard MCDM process.

(6) Different decision results are aggregated into a group consensus, using the previously proposed distance-based aggregation optimization method, in terms of the maximum agreement principle. The aggregated group consensus value can be used as a <sup>fi</sup>nal measurement for the <sup>fi</sup>nal decision-making purpose.

In order to verify the proposed distance-based multi-person multicriteria GDM methodology, the next section will present one numerical example and one practical experiment in emergency decision management for illustration and veri<sup>fi</sup>cation purposes.

## 3. Experimental analysis

In this section, an illustrative numerical example is <sup>fi</sup>rst presented to explain the implementation process of the proposed distancebased multi-person multi-criteria GDM methodology. Then one realworld emergency decision problem for a chemical spill emergency management is simulated, using the proposed distance-based multicriteria GDM methodology. Accordingly, some interesting results are produced by comparison of these results with some existing methods.

## 3.1. An illustrative numerical example

In order to illustrate the implementation process of the proposed distance-based multi-criteria GDM model, a simple numerical example is given. Suppose there are three evaluation criteria and <sup>fi</sup>ve alternatives for a speci<sup>fi</sup>ed decision problem, three decision-makers give different utility values to different decision alternatives in terms of different evaluation criteria. Table 2 shows the different utility values for three evaluation criteria and <sup>fi</sup>ve decision alternatives. Note that in the three criteria $C _ { 1 }$ and $C _ { 3 }$ are positive criteria, while $C _ { 2 }$ is a negative criterion.

According to the steps described in Section 2, the individual decision-maker can evaluate decision alternatives in terms of the criteria when the criteria weights are determined. In the process of criteria weight determination, three objective approaches are introduced. For comparison purpose, three criteria weight determination methods are performed. Table 3 presents the criteria weights using different approaches of different decision-makers.

Using the aforementioned criteria weights, it is not hard to obtain alternative evaluation results in terms of Eq. (17) for a certain decision-maker. In this example, we can easily obtain the following <sup>fi</sup>ve alternative evaluation results for different decision-makers and different criteria weight determination methods, as given in Table 4.

As can be seen from Table 4, different decision-makers can obtain different evaluation results for speci<sup>fi</sup>c alternatives when a certain criteria weight determination method is <sup>fi</sup>xed. However, even for the same decision-makers, evaluation results are different when different criteria weight determination methods are used. Thus in the decision fusion stage there are two aggregations at different levels. On the one hand, aggregation of decision of different decision-makers is often used to capture from the decision-makers' perspectives. Since every decision maker has different knowledge and expectations, different decision results are obtained from them. Naturally, aggregation of the decision of different decision-makers is, therefore, often used. On the other hand, for the same decision-makers, if they applied different method to obtain different decision results, aggregation of these different decision results obtained from different methods should be conducted to avoid confusion in decision-making. By changing the presentation form of Table 4, it is easy to obtain such a decision fusion scenario, as shown in Table 5.

In order to avoid ambiguous situations during the group decisionmaking process, methodology fusion is <sup>fi</sup>rst performed. That is, each decision-maker must obtain a consistent decision result before group consensus is arrived. Based on the data of Table 5, aggregation of different decision results from the perspective of different criteria weight determination methodologies is conducted. Similarly, the key issue is how to determine method weights in the process of aggregation. Using the distance-based maximum similarity principle described in Section 2.4, weights for different methods are determined in terms of Eq. (32). Accordingly, aggregation of different methods is shown in Table 6.

As can be seen from Table $6 ,$ we can <sup>fi</sup>nd that three different evaluation results from three different criteria weight determination methods for a certain decision-maker are aggregated into an integrated decision result. The subsequent task is to fuse three evaluation results obtained from three different decision-makers to obtain the <sup>fi</sup>nal decision results. As such, how to determine weights of different decision-makers becomes a key issue. In this case also, we continue using the distance-based maximum similarity principle and Eq. (32). Accordingly the <sup>fi</sup>nal decision results are obtained, as shown in Table 7.

A numerical example for multi-criteria group decision-making.

<table><tr><td rowspan="2">Alternative</td><td colspan="3"> $DM_1$ </td><td colspan="3"> $DM_2$ </td><td colspan="3"> $DM_3$ </td></tr><tr><td> $C_1$ </td><td> $C_2$ </td><td> $C_3$ </td><td> $C_1$ </td><td> $C_2$ </td><td> $C_3$ </td><td> $C_1$ </td><td> $C_2$ </td><td> $C_3$ </td></tr><tr><td> $A_1$ </td><td>0.24</td><td>0.33</td><td>0.43</td><td>0.40</td><td>0.20</td><td>0.40</td><td>0.15</td><td>0.24</td><td>0.61</td></tr><tr><td> $A_2$ </td><td>0.30</td><td>0.35</td><td>0.35</td><td>0.45</td><td>0.18</td><td>0.37</td><td>0.28</td><td>0.16</td><td>0.56</td></tr><tr><td> $A_3$ </td><td>0.28</td><td>0.33</td><td>0.39</td><td>0.35</td><td>0.25</td><td>0.40</td><td>0.23</td><td>0.44</td><td>0.33</td></tr><tr><td> $A_4$ </td><td>0.42</td><td>0.26</td><td>0.32</td><td>0.25</td><td>0.40</td><td>0.35</td><td>0.35</td><td>0.20</td><td>0.45</td></tr><tr><td> $A_5$ </td><td>0.25</td><td>0.32</td><td>0.43</td><td>0.30</td><td>0.30</td><td>0.40</td><td>0.44</td><td>0.18</td><td>0.38</td></tr></table>

Table 3  
Criteria weights determined by three different approaches.

<table><tr><td rowspan="2">DM</td><td rowspan="2">Criterion</td><td colspan="2">Variation coefficient method</td><td colspan="2">Entropy-based method</td><td colspan="2">Distance-based method</td></tr><tr><td> $\delta_j$ </td><td> $w_j^C$ </td><td> $\varphi_j$ </td><td> $w_j^C$ </td><td> $\xi_j$ </td><td> $w_j^C$ </td></tr><tr><td rowspan="3"> $DM_1$ </td><td> $C_1$ </td><td>0.2424</td><td>0.5082</td><td>0.0137</td><td>0.6599</td><td>0.7165</td><td>0.3971</td></tr><tr><td> $C_2$ </td><td>0.1076</td><td>0.2255</td><td>0.0030</td><td>0.1442</td><td>0.6869</td><td>0.3806</td></tr><tr><td> $C_3$ </td><td>0.1270</td><td>0.2663</td><td>0.0041</td><td>0.1959</td><td>0.4012</td><td>0.2223</td></tr><tr><td rowspan="3"> $DM_2$ </td><td> $C_1$ </td><td>0.2259</td><td>0.3658</td><td>0.0128</td><td>0.3200</td><td>0.5000</td><td>0.4306</td></tr><tr><td> $C_2$ </td><td>0.3316</td><td>0.5371</td><td>0.0264</td><td>0.6574</td><td>0.3603</td><td>0.3103</td></tr><tr><td> $C_3$ </td><td>0.0600</td><td>0.0971</td><td>0.0009</td><td>0.0226</td><td>0.3009</td><td>0.2591</td></tr><tr><td rowspan="3"> $DM_3$ </td><td> $C_1$ </td><td>0.3832</td><td>0.3479</td><td>0.0374</td><td>0.3702</td><td>0.5234</td><td>0.4013</td></tr><tr><td> $C_2$ </td><td>0.4651</td><td>0.4222</td><td>0.0476</td><td>0.4712</td><td>0.2627</td><td>0.2014</td></tr><tr><td> $C_3$ </td><td>0.2533</td><td>0.2299</td><td>0.0160</td><td>0.1586</td><td>0.5182</td><td>0.3973</td></tr></table>

Table 4  
Decision scores of standard MCDM process from decision-makers' perspective.

<table><tr><td>Criteria weight method</td><td>DM</td><td> $A_1$ </td><td> $A_2$ </td><td> $A_3$ </td><td> $A_4$ </td><td> $A_5$ </td></tr><tr><td rowspan="3">Variation coefficient method</td><td> $DM_1(z_1)$ </td><td>0.3109</td><td>0.3246</td><td>0.3206</td><td>0.3573</td><td>0.3137</td></tr><tr><td> $DM_2(z_2)$ </td><td>0.2926</td><td>0.2972</td><td>0.3011</td><td>0.3403</td><td>0.3097</td></tr><tr><td> $DM_3(z_3)$ </td><td>0.2938</td><td>0.2937</td><td>0.3417</td><td>0.3097</td><td>0.3164</td></tr><tr><td rowspan="3">Entropy-based method</td><td> $DM_1(z_1)$ </td><td>0.2902</td><td>0.3170</td><td>0.3088</td><td>0.3773</td><td>0.2954</td></tr><tr><td> $DM_2(z_2)$ </td><td>0.2685</td><td>0.2707</td><td>0.2854</td><td>0.3509</td><td>0.3023</td></tr><tr><td> $DM_3(z_3)$ </td><td>0.2653</td><td>0.2678</td><td>0.3448</td><td>0.2952</td><td>0.3080</td></tr><tr><td rowspan="3">Distance-based method</td><td> $DM_1(z_1)$ </td><td>0.3165</td><td>0.3301</td><td>0.3235</td><td>0.3369</td><td>0.3167</td></tr><tr><td> $DM_2(z_2)$ </td><td>0.3379</td><td>0.3455</td><td>0.3319</td><td>0.3225</td><td>0.3259</td></tr><tr><td> $DM_3(z_3)$ </td><td>0.3509</td><td>0.3671</td><td>0.3120</td><td>0.3595</td><td>0.3638</td></tr></table>

Table 5  
Decision scores of standard MCDM process from the methodology perspective.

<table><tr><td>Decision-maker</td><td>Criteria weight method</td><td> $A_1$ </td><td> $A_2$ </td><td> $A_3$ </td><td> $A_4$ </td><td> $A_5$ </td></tr><tr><td rowspan="3"> $DM_1$ </td><td>Variation coefficient method</td><td>0.3109</td><td>0.3246</td><td>0.3206</td><td>0.3573</td><td>0.3137</td></tr><tr><td>Entropy-based method</td><td>0.2902</td><td>0.3170</td><td>0.3088</td><td>0.3773</td><td>0.2954</td></tr><tr><td>Distance-based method</td><td>0.3165</td><td>0.3301</td><td>0.3235</td><td>0.3369</td><td>0.3167</td></tr><tr><td rowspan="3"> $DM_2$ </td><td>Variation coefficient method</td><td>0.2926</td><td>0.2972</td><td>0.3011</td><td>0.3403</td><td>0.3097</td></tr><tr><td>Entropy-based method</td><td>0.2685</td><td>0.2707</td><td>0.2854</td><td>0.3509</td><td>0.3023</td></tr><tr><td>Distance-based method</td><td>0.3379</td><td>0.3455</td><td>0.3319</td><td>0.3225</td><td>0.3259</td></tr><tr><td rowspan="3"> $DM_3$ </td><td>Variation coefficient method</td><td>0.2938</td><td>0.2937</td><td>0.3417</td><td>0.3097</td><td>0.3164</td></tr><tr><td>Entropy-based method</td><td>0.2653</td><td>0.2678</td><td>0.3448</td><td>0.2952</td><td>0.3080</td></tr><tr><td>Distance-based method</td><td>0.3509</td><td>0.3671</td><td>0.3120</td><td>0.3595</td><td>0.3638</td></tr></table>

From Table 7, we can easily conclude that alternative $A _ { 4 }$ is the best alternative, followed by $A _ { 3 } , A _ { 5 } , A _ { 2 } ,$ and $A _ { 1 }$ is the worst of the <sup>fi</sup>ve alternatives in terms of three different evaluation criteria and three different decision-makers. Using such aggregated decision results, the <sup>fi</sup>nal group decision-making results can be objectively obtained.

## 3.2. A practical emergency decision simulation for chemical spill emergency management

In order to verify effectiveness of the proposed multi-criteria GDM model, a practical chemical spill emergency decision example is presented. For comparison purpose, all data are obtained from Levy and Taji [13]. That is, the proposed distance-based multi-criteria GDM methodology is applied to the Brandon Emergency Support Team (BEST) “Community Contact” Emergency Exercise, which was held on Wednesday, June 21, 2006 in Brandon, Manitoba [13]. In this example, four key decision-makers were <sup>fi</sup>rst identi<sup>fi</sup>ed, including Brandon Police Service $\left( D M _ { 1 } \right)$ , Brandon Fire Division $\left( D M _ { 2 } \right)$ , Western Manitoba Hazardous Materials Technical Team $( D M _ { 3 } ) ,$ , and Brandon School Division $( D M _ { 4 } )$ to formulate a GDM framework. Mathematically, these four decision-makers DM $( k = 1 , . . . , 4 )$ are required to evaluate six emergency response alternatives $A _ { j } ( j = 1 , ~ . . . , ~ 6 )$ under the three criteria $C _ { i } ( i = 1 , 2 , 3 )$ , where $C _ { 1 }$ represents physiological discomfort $C _ { 2 }$ represents emergency cost, and $C _ { 3 }$ represents the safety criterion (in terms of expected number of lives saved). During the release of hazardous airborne material, the “shelter-in-place alternative” $\left( A _ { 1 } \right)$ is the practice of staying inside (or going indoors as quickly as possible) and moving to an area of maximum safety. Time permitting, it is recommended to shut and lock all windows and doors (locking a door may improve the seal against chemicals). On the other hand, “evacuation” involves transporting the victims to a nearby destination $\left( A _ { 2 } \right)$ or the more distant Brandon Keystone Center $( A _ { 3 } ) . A _ { 1 } ,$ , followed by $A _ { 2 } ,$ gives rise to the fourth alternative of sheltering in place followed by evacuation to a nearby location $\left( A _ { 4 } \right)$ . Similarly, $A _ { 1 }$ followed by $A _ { 3 }$ produces the <sup>fi</sup>fth alternative of sheltering-in-place followed by evacuation to the Keystone Center $\left( A _ { 5 } \right)$ . Finally, alternative $A _ { 6 }$ is “donothing” [13]. Accordingly, evaluation results of each decision-maker are provided in Table 8 in terms of different criteria. Note that Table 8 illustrates the utility scores provided by the four emergency decisionmakers for the six alternatives. $D M _ { 1 }$ evaluates alternatives $A _ { 2 }$ and $A _ { 3 }$ (only) for all three criteria, while $D M _ { 2 }$ evaluates all the alternatives under all the criteria. For all criteria, $D M _ { 3 }$ evaluates half of the alternatives $( A _ { 1 } , A _ { 2 }$ and $A _ { 3 } )$ , while $D M _ { 4 }$ evaluates every alternative (for all criteria) except alternatives $A _ { 1 }$ and $A _ { 6 } .$ . In addition, $C _ { 1 }$ and $C _ { 2 }$ are negative criteria and $C _ { 3 }$ is the positive criterion.

Table 6  
Aggregation of different evaluation results based on different methods.

<table><tr><td>Decision-maker</td><td> $A_1$ </td><td> $A_2$ </td><td> $A_3$ </td><td> $A_4$ </td><td> $A_5$ </td></tr><tr><td> $DM_1$ </td><td>0.3058</td><td>0.3239</td><td>0.3176</td><td>0.3573</td><td>0.3085</td></tr><tr><td> $DM_2$ </td><td>0.2983</td><td>0.3030</td><td>0.3052</td><td>0.3385</td><td>0.3122</td></tr><tr><td> $DM_3$ </td><td>0.3009</td><td>0.3066</td><td>0.3338</td><td>0.3196</td><td>0.3277</td></tr></table>

Table 7  
Final decision results by aggregation of different decision-makers' evaluation results.

<table><tr><td>Final decision</td><td> $A_1$ </td><td> $A_2$ </td><td> $A_3$ </td><td> $A_4$ </td><td> $A_5$ </td></tr><tr><td>Aggregated results</td><td>0.3016</td><td>0.3110</td><td>0.3188</td><td>0.3384</td><td>0.3161</td></tr><tr><td>Rank</td><td>5</td><td>4</td><td>2</td><td>1</td><td>3</td></tr></table>

Table 11  
Table 8  
A chemical spill emergency decision data with four decision-makers [13].

<table><tr><td rowspan="2">Alternatives</td><td colspan="3"> $DM_1$ </td><td colspan="3"> $DM_2$ </td><td colspan="3"> $DM_3$ </td><td colspan="3"> $DM_4$ </td></tr><tr><td> $C_1$ </td><td> $C_2$ </td><td> $C_3$ </td><td> $C_1$ </td><td> $C_2$ </td><td> $C_3$ </td><td> $C_1$ </td><td> $C_2$ </td><td> $C_3$ </td><td> $C_1$ </td><td> $C_2$ </td><td> $C_3$ </td></tr><tr><td> $A_1$ </td><td></td><td></td><td></td><td>0.15</td><td>0.25</td><td>0.15</td><td>0.20</td><td>0.67</td><td>0.25</td><td></td><td></td><td></td></tr><tr><td> $A_2$ </td><td>0.55</td><td>0.75</td><td>0.20</td><td>0.20</td><td>0.20</td><td>0.05</td><td>0.50</td><td>0.22</td><td>0.25</td><td>0.45</td><td>0.44</td><td>0.20</td></tr><tr><td> $A_3$ </td><td>0.45</td><td>0.25</td><td>0.80</td><td>0.20</td><td>0.15</td><td>0.05</td><td>0.30</td><td>0.11</td><td>0.50</td><td>0.25</td><td>0.33</td><td>0.20</td></tr><tr><td> $A_4$ </td><td></td><td></td><td></td><td>0.10</td><td>0.10</td><td>0.30</td><td></td><td></td><td></td><td>0.20</td><td>0.22</td><td>0.40</td></tr><tr><td> $A_5$ </td><td></td><td></td><td></td><td>0.10</td><td>0.05</td><td>0.40</td><td></td><td></td><td></td><td>0.10</td><td>0.11</td><td>0.20</td></tr><tr><td> $A_6$ </td><td></td><td></td><td></td><td>0.25</td><td>0.25</td><td>0.05</td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

Table 9  
Overall decision results based on distance-based multi-criteria GDM model.

<table><tr><td rowspan="2">Alternatives</td><td colspan="2">Group</td><td colspan="2"> $DM_1$ </td><td colspan="2"> $DM_2$ </td><td colspan="2"> $DM_3$ </td><td colspan="2"> $DM_4$ </td></tr><tr><td>Score</td><td>Rank</td><td>Score</td><td>Rank</td><td>Score</td><td>Rank</td><td>Score</td><td>Rank</td><td>Score</td><td>Rank</td></tr><tr><td> $A_1$ </td><td>0.1350</td><td>4</td><td></td><td></td><td>0.1851</td><td>2</td><td>0.3118</td><td>2</td><td></td><td></td></tr><tr><td> $A_2$ </td><td>0.2670</td><td>2</td><td>0.3629</td><td>2</td><td>0.1398</td><td>5</td><td>0.3067</td><td>3</td><td>0.3330</td><td>1</td></tr><tr><td> $A_3$ </td><td>0.3037</td><td>1</td><td>0.6371</td><td>1</td><td>0.1223</td><td>6</td><td>0.3816</td><td>1</td><td>0.2508</td><td>3</td></tr><tr><td> $A_4$ </td><td>0.1381</td><td>3</td><td></td><td></td><td>0.1803</td><td>3</td><td></td><td></td><td>0.2972</td><td>2</td></tr><tr><td> $A_5$ </td><td>0.1070</td><td>5</td><td></td><td></td><td>0.2029</td><td>1</td><td></td><td></td><td>0.1486</td><td>4</td></tr><tr><td> $A_6$ </td><td>0.0570</td><td>6</td><td></td><td></td><td>0.1697</td><td>4</td><td></td><td></td><td></td><td></td></tr></table>

Table 10  
Overall decision results based on GANP model [13].

<table><tr><td rowspan="2">Alternatives</td><td colspan="2">Group</td><td colspan="2"> $DM_1$ </td><td colspan="2"> $DM_2$ </td><td colspan="2"> $DM_3$ </td><td colspan="2"> $DM_4$ </td></tr><tr><td>Score</td><td>Rank</td><td>Score</td><td>Rank</td><td>Score</td><td>Rank</td><td>Score</td><td>Rank</td><td>Score</td><td>Rank</td></tr><tr><td> $A_1$ </td><td>0.1455</td><td>4</td><td></td><td></td><td>0.1611</td><td>3</td><td>0.2823</td><td>3</td><td></td><td></td></tr><tr><td> $A_2$ </td><td>0.1406</td><td>6</td><td>0.3583</td><td>2</td><td>0.1083</td><td>5</td><td>0.3163</td><td>2</td><td>0.2966</td><td>2</td></tr><tr><td> $A_3$ </td><td>0.1446</td><td>5</td><td>0.6417</td><td>1</td><td>0.1028</td><td>6</td><td>0.4012</td><td>1</td><td>0.2287</td><td>3</td></tr><tr><td> $A_4$ </td><td>0.2263</td><td>1</td><td></td><td></td><td>0.2222</td><td>2</td><td></td><td></td><td>0.3247</td><td>1</td></tr><tr><td> $A_5$ </td><td>0.1898</td><td>2</td><td></td><td></td><td>0.2778</td><td>1</td><td></td><td></td><td>0.1623</td><td>4</td></tr><tr><td> $A_6$ </td><td>0.1535</td><td>3</td><td></td><td></td><td>0.1278</td><td>4</td><td></td><td></td><td></td><td></td></tr></table>

Using the proposed procedure presented in Section 2.4 and the standard MCDM process, we can easily obtain decision results based on the distance-based multi-criteria GDM methodology and distancebased MCDM method, as shown in Table 9. Note that the second column in Table 9 is the group consensus, and others are decision results of four individual DMs.

Two interesting results can be found by comparing results in Table 9 with Table 3 in Levy and Taji (Table 10 in this paper, for direct comparison) [13]. On the one hand, decision results of the distancebased MCDM method for DM and DM are basically consistent with results of Levy and Taji [13], though numerical values of evaluation results are different. This implies that the distance-based MCDM method is an alternative solution to the multi-criteria decision-making problem. On the other hand, group decision results from the proposed distance-based multi-criteria GDM method and the Group Analytic Network Process (GANP) approach presented in the paper of Levy and Taji [13] are different. The main reason is that different criteria weight determination methods and different decision-makers weight determination approaches are used in the two different methodologies.

However, the decision results of the proposed distance-based multi-criteria GDM methodology are more suitable for practical situations than the GANP approach presented in Levy and Taji [13] because the proposed distance-based multi-criteria GDM methodology can provide more suitable alternatives than the GANP approach [13]. For illustration, we take the best and the worst alternatives of the proposed GDM method as examples. The proposed multi-criteria GDM methodology selects alternative $A _ { 3 }$ as the best alternative, while the GANP approach [13] selects alternative $A _ { 4 } .$ . If we evaluate these alternatives from the perspective of safety criterion, alternative $A _ { 3 }$ seems to be more suitable than alternative $A _ { 4 } .$ In the worst case, the proposed distance-based multi-criteria GDM methodology selects alternative $A _ { 6 } ,$ while alternative $A _ { 6 }$ ranks the third in GANP [13]. As mentioned earlier, alternative $A _ { 6 }$ represents “do-nothing”. Due to the relative importance of safety criterion, alternative “do-nothing” should be the worst selection, but GANP approach assigns this alternative more preference, relative to other alternatives. These two aspects also demonstrate that the proposed distance-based multicriteria GDM methodology is a very promising approach in solving the multi-criteria group decision-making problems.

Group decision results of different criteria weight determination methods

<table><tr><td rowspan="2">Alternatives</td><td colspan="2">Distance-based method</td><td colspan="2">Variation coefficient method</td><td colspan="2">Entropy-based method</td><td colspan="2">GANP-based method</td></tr><tr><td>Score</td><td>Rank</td><td>Score</td><td>Rank</td><td>Score</td><td>Rank</td><td>Score</td><td>Rank</td></tr><tr><td> $A_1$ </td><td>0.1350</td><td>4</td><td>0.1489</td><td>3</td><td>0.1533</td><td>3</td><td>0.1170</td><td>5</td></tr><tr><td> $A_2$ </td><td>0.2670</td><td>2</td><td>0.2982</td><td>1</td><td>0.3032</td><td>1</td><td>0.2524</td><td>2</td></tr><tr><td> $A_3$ </td><td>0.3037</td><td>1</td><td>0.2616</td><td>2</td><td>0.2649</td><td>2</td><td>0.3000</td><td>1</td></tr><tr><td> $A_4$ </td><td>0.1381</td><td>3</td><td>0.1376</td><td>4</td><td>0.1274</td><td>4</td><td>0.1607</td><td>3</td></tr><tr><td> $A_5$ </td><td>0.1070</td><td>5</td><td>0.1143</td><td>5</td><td>0.1003</td><td>5</td><td>0.1329</td><td>4</td></tr><tr><td> $A_6$ </td><td>0.0570</td><td>6</td><td>0.0483</td><td>6</td><td>0.0596</td><td>6</td><td>0.0403</td><td>6</td></tr></table>

For further comparison, two different criteria weight determination approaches, variation coef<sup>fi</sup>cient approach and entropy-based approach, are applied to evaluate these different alternatives in chemical spill emergency decision-making. Using equations in Sections 2.3 and $2 . 4 ,$ , the <sup>fi</sup>nal group decision-making results are given in Table 11. Note that the decision-makers’ weights of four different criteria weight determination methods are determined by distance-based maximum similarity method. That is, the <sup>fi</sup>nal decision results are fused by the distance-based maximum similarity method described in Section 2.4.

As can be seen from Table 11, several important conclusions are drawn. First of all, alternative $A _ { 6 }$ is the worst alternative for all criteria weight determination methods. This <sup>fi</sup>nding con<sup>fi</sup>rms the effectiveness of the proposed distance-based multi-criteria GDM methodology. Second, the best alternative in this emergency decision-making exercise should be generated from alternative $A _ { 2 }$ and $A _ { 3 }$ in terms of ranks of different methods. According to descriptions of alternatives, $A _ { 3 }$ seems to be preferable due to the relative importance of the safety criterion. Finally, all decision results are based on the original data, without involvement of decision-makers. This reveals that the proposed distance-based multi-criteria GDM is an objective decisionmaking approach to solve multi-criteria GDM problems.

In summary, the proposed distance-based multi-criteria GDM methodology can effectively provide objective group decision results, as shown by the practical simulation example, which implies that the proposed distance-based multi-criteria GDM methodology can be used as an alternative solution to multi-person multi-criteria decision-making problems.

## 4. Concluding remarks

In this paper, a distance-based multi-criteria GDM methodology is proposed for multi-person emergency decision support. In terms of experimental results, it is easy to <sup>fi</sup>nd that across different models and three different evaluation criteria, for the test cases of numerical and practical examples, the proposed distance-based multi-criteria GDM methodology can effectively solve the multi-person multi-criteria decision-making (MCDM) problems. In the presented practical cases, decision results of the proposed distance-based multi-criteria GDM methodology can provide the most suitable decision results, indicating that the proposed distance-based multi-criteria GDM methodology can be used as a promising tool for multi-person multi-criteria emergency decision-making problems. This implies that the proposed distance-based multi-criteria GDM methodology has great potential for application to other MCDM problems.

## Acknowledgements

Authors would like to thank the guest editors and anonymous referees for their valuable comments and suggestions. Their comments helped improve the quality of the paper immensely. This work is partially supported by grants from the National Science Fund for

Distinguished Young Scholars (NSFC No. 71025005), National Natural Science Foundation of China (NSFC No. 90924024) and Knowledge Innovation Program of the Chinese Academy of Sciences (CAS).

## References

[1] H.K. Alfares, S.O. Duffuaa, Determining aggregate criteria weights from criteria rankings by a group of decision makers, International Journal of Information Technology & Decision Making 7 (2008) 769–781.

[2] A. Berman, R.J. Plemmons, Nonnegative matrices in the mathematical sciences, Society for Industrial and Applied Mathematics (1987).

[3] M.J. Beynon, A method of aggregation in DS/AHP for group decision-making with the non-equivalent importance of individuals in the group, Computers & Operations Research 32 (2005) 1881–1896.

[4] F.J. Cabrerizo, S. Alonso, E. Herrera-Viedma, A consensus model for group decision making problems with unbalanced fuzzy linguistic information, International Journal of Information Technology & Decision Making 8 (2009) 109–131.

[5] J. Cosgrave, Decision making in emergencies, Disaster Prevention and Management 5 (1996) 28–35.

[6] A. Davey, D. Olson, Multiple criteria decision making models in group decision support, Group Decision and Negotiation 7 (1998) 55–75.

[7] M. Delgado, F. Herrera, E. Herrera-Viedma, L. Martinez, Combining numerical and linguistic information in group decision making, Information Sciences 107 (1998) 177–194.

[8] M. Hatcher, A tool kit for multimedia supported group/organizational decision systems (MSGDS), Decision Support Systems 15 (1995) 211–217.

[9] V.S. Jacob, H. Pirkul, A framework for supporting distributed group decisionmaking, Decision Support Systems 8 (1992) 17–28.

[10] M. Koksalan, C. Tuncer, A DEA-based approach to ranking multi-criteria alternatives, International Journal of Information Technology & Decision Making 8 (2009) 29–54.

[11] G. Kou, Y. Peng, Z. Chen, Y. Shi, Multiple criteria mathematical programming for multi-class classi<sup>fi</sup>cation and application in network intrusion detection, Information Sciences 179 (2009) 371–381.

[12] H.S. Lee, Optimal consensus of fuzzy opinions under group decision making environment, Fuzzy Sets and Systems 132 (2002) 303–315.

[13] J.K. Levy, K. Taji, Group decision support for hazards planning and emergency management: a Group Analytic Network Process (GANP) approach, Mathematical and Computer Modelling 46 (2007) 906–917.

[14] D.F. Li, Relative ratio method for multiple attribute decision making problems, International Journal of Information Technology & Decision Making 8 (2009) 289–311.

[15] D. Mendonca, G.E.G. Beroggi, D. van Gent, W.A. Wallace, Designing gaming simulations for the assessment of group decision support systems in emergency response, Safety Science 44 (2006) 523–535.

[16l Y.P. Ou Yang H.M. Shieh LD. Leu G.H. Tzeng A VIKOR-based multiple criteria decision method for improving information security risk, International Journal of Information Technology & Decision Making 8 (2009) 267–287.

[17] Y. Peng, G. Kou, Y. Shi, Z. Chen, A multi-criteria convex quadratic programming model for credit data analysis, Decision Support Systems 44 (2008) 1016–1030.

[18] J.C. Pomerol, S.B. Romero, Multicriteria Decision in Management: Principle and Practice. Kluwer Academic Publishers. 2000.

[19] R.K. Singh, A.K. Choudhury, M.K. Tiwari, R. Shankar, Improved Decision Neural Network (IDNN) based consensus method to solve a multi-objective group decision making problem, Advanced Engineering Informatics 21 (2007) 335–348.

[20] E. Triantaphyllou, Multi-criteria Decision Making Methods: a Comparative Study Springer, New York, 2000.

[21] Z.S. Xu, A method based on linguistic aggregation operators for group decision making with linguistic preference relations, Information Sciences 166 (2004) 19-30.

[22] Z.S. Xu, Uncertain linguistic aggregation operators based approach to multiple attribute group decision making under uncertain linguistic environment, Information Sciences 169 (2005) 171–184.

[23] D.L. Xu, Assessment of nuclear waste repository options using the ER approach, International Journal of Information Technology & Decision Making 8 (2009) 581–607.

[24] R.R. Yager, A general approach to criteria aggregation using fuzzy measures, International Journal of Man-Machine Studies 39 (1993) 187–213.

[25] R.R. Yager, Aggregation operators and fuzzy systems modeling, Fuzzy Sets and System 67 (1994) 129–145.

[26] G. Zhang, J. Lu, An integrated group decision-making method dealing with fuzzy preferences for alternatives and individual judgments for selection criteria, Group Decision and Negotiation 12 (2003) 501–515

[27] K.G. Zografos, G.M. Vasilakis, I.M. Giannouli, Methodological framework for developing decision support systems (DSS) for hazardous materials emergency response operations, Journal of Hazardous Materials 71 (2000) 503–521.

Lean Yu is Associate Professor in the Academy of Mathematics and Systems Science, Chinese Academy of Sciences (CAS). His research interests include arti<sup>fi</sup>cial intelligence, computer simulation, decision support systems, knowledge management, and <sup>fi</sup>nancial forecasting.

Kin Keung Lai is Chair Professor of Management Science at City University of Hong Kong, Hong Kong. His main research interests include logistics and operations management, computer simulation, artificial intelligence and business decision modeling
