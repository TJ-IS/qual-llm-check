---
otero_id: 14792
otero_key: "3DM43GHD"
title: "Emphasizing the rank positions in a distance-based aggregation procedure"
authors: "I. Contreras"
year: "2011"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2010.12.012"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Emphasizing the rank positions in a distance-based aggregation procedure

I. Contreras ⁎

Department of Economics, Quantitative Methods and Economic History, Pablo de Olavide University, Spain

## a r t i c l e i n f o

Article history: Received 19 July 2010 Received in revised form 5 October 2010 Accepted 23 December 2010 Available online 7 January 2011

Keywords: Group decision Distance-based model Linear orders Goal programming

## a b s t r a c t

This paper deals with the problem of aggregating individual preferences in order to obtain a social order. In particular, a preference aggregation procedure is proposed for those cases in which the decision-makers express their preferences by means of a ranking of alternatives. Among the most commonly applied methods for this purpose are those based on distance measures between individual and collective preferences, which look for the solution that minimizes the disagreement across decision-makers. This class of procedures may include weighting factors in order to emphasize the relative importance of the individuals. In the model proposed here, a weighted disagreement function that computes the differences between alternatives differentiating the rank positions of the alternatives is developed. The proposed disagreement function weighs the differences between orders depending on the ordinal position that the alternative occupies

© 2011 Elsevier B.V. All rights reserved

## 1. Introduction

The aggregation of individual preferences into a group or consensus order is a typical group decision problem and has a wide range of applications in group decision-making, social choice and voting systems. This family of decision-making problems contains either those problems in which individual preferences are expressed in terms of a ranking of alternatives, problems in which the group's members evaluate the alternatives by placing them in an ordinal scale, or situations in which each decision-maker (DM) is requested to choose a subset of candidates from a feasible set of alternatives and then rank that subset. In every case, the target is to obtain a fair aggregation of the preferences that represent as accurately as possible the individual's opinions. Many problems from a variety of <sup>fi</sup>elds can be represented by this formulation, including the evaluation of consumers' preferences, allocation of priorities to projects, and personnel selection.

Dealing with this class of problems generally involves three main issues [23]. The <sup>fi</sup>rst includes the decision related with the format in which information about the individual preferences is collected and represented. The second issue is the resolution of inconsistencies in the preferences provided by the individuals. Finally, when multiple agents offer individual preferences with respect to a set of alternatives, there is the task of combining these preferences into a consensus solution. This paper is focused on this third issue. The former two are only considered in order to present the model.

Different methods have been suggested for aggregating individuals' preferences into a compromise or social order. J. C. Borda [3] was the <sup>fi</sup>rst to examine the problem in terms of candidates in an election and proposed his well-known method of marks. This method ranks the alternatives according to the sum of marks, which are scores associated to the ordinal positions. Kendall [20] revises the method in a statistical framework. The solution obtained as a problem of estimation is equivalent to Borda's marks, so the procedure is frequently referred to as the Borda–Kendall rule.

The Borda–Kendall rule is considered the origin of a class of preference–aggregation procedures known as weighted scoring rules. This family of methods operates by computing a score that depends on the rank position of each alternative in the individual's order of preference. The alternatives are ranked in terms of the sum of scores received. Since a number is assigned to each candidate, these procedures guarantee a weak order of alternatives. For a complete revision of this class of procedure see, among others, the work of Young [24].

Other authors have proposed alternative approaches to ordinal preference aggregation problems, from among which, those proposals based upon a distance consensus between individual rankings have received much attention in the literature. In these procedures, the main idea is to determine which order of alternatives minimizes the disagreement across individuals, measured by means of a distance measure between orders.

Two kinds of distances, spatial and disorder distances, are often utilized to measure the differences between rank vectors and to determine the minimum-distance collective solution. The spatial distances measure the difference of rank values between the vectors that represent the individual and collective preferences. Disorder distances, on the other hand, measure the number of disordered pairs between the rank vectors.

The Kemeny rule, proposed in [18], can be considered as a benchmark of preference–aggregation procedures based on distances.

The author proposes the procedure as a way of seeking a solution when there are cycles present in the majority of the preference relations, breaking these cycles by using a distance between orders. Roughly speaking, the distance proposed measures the sum for all the individuals of the numbers of pairs of alternatives for which the relative position is different in the individual's ordinal preferences to that of the group's ordinal preferences.

Kemeny and Snell formalize this class of solutions based on distance measures in [19]. The authors provide a set of axioms which any distance measure should verify for the application in the social choice context, and prove its existence and uniqueness. In [11], the $l _ { 1 }$ metric for the determination of the consensus solution is proposed. These authors prove that the $l _ { 1 }$ metric veri<sup>fi</sup>es the axioms proposed by Kemeny and Snell in [19] and de<sup>fi</sup>nes the consensus ranking in order to minimize the total distance to the individual rankings. In Cook and Seiford [12], the equivalence between the Borda–Kendall method and the consensus method is proved, when metric l is applied. The consensus solution based upon $l _ { 2 }$ distance can therefore be seen as a formalization of the Borda–Kendall rule.

Among others, [7,8] and [1] extend consensus models to include ordinal rankings with intensity of preference. In this case, integer linear programming models are applied to determine the group solution. In [10] a general framework for distance-based consensus models is presented, and a generalization of the problem to a generic $l _ { p }$ metric is studied. González-Pachón and Romero present, in [15], a general model based on the $l _ { p }$ metric. By applying goal programming, the authors develop linear models to determine the solution for the cases of $l _ { 1 }$ and l metrics. In [16], interval goal programming is included by the same authors to extend the problem to include the case of incomplete ordinal rankings. Other papers related to preference aggregation methods based on distances should also be mentioned. See, for instance, [6,17,22] and [21].

More recently, several approaches try to improve existing group decision procedures by including new features like alternative forms in which preference data are elicited (see, for instance, [4]), or including weighting factors to represent the relative importance of the elements in the model (for instance, [14]). The inclusion of weighting factors traditionally focuses on the relative importance of the agents into the group. The model studied in this paper, based on a minimum-distance collective solution procedure, is proposed for the assignation of different weights to the distance between the rank position of each alternative (from the position ranked in the individual order to that in the social order) depending on which ordinal position the alternative occupies in the order. Therefore, the disagreement function will weigh the individuals' disagreement depending not only on the differences between ordinal positions, but also on which alternative, in particular its ordinal position, induces this difference.

The rest of the paper is organized as follows. In Section 2 the general context of distance-based aggregation procedures is brie<sup>fl</sup>y described. Section 3 presents the proposed weighted disagreement model inspired in the idea of weighting rank positions. In Section 4 the model is illustrated with numeric examples. Section 5 is devoted to conclusions.

## 2. Distance-based preference aggregation procedures

Let $V = \{ \nu _ { 1 } , . . . , \nu _ { K } \}$ be a set of K (K 2) DMs that give their preferences with respect to a set of N alternatives $X = \{ x _ { 1 } , . . . , x _ { N } \}$ $\left( N { \ge } 3 \right)$ . Consider that each individual ranks the complete set of alternatives from the most to the least preferred. An order vector can be derived from the preferences of each DM in such a way that it contains the names of alternatives in the preference sequence. From each order vector, a priority vector can be constructed by assigning the position number from the order vector. Note that a priority vector contains the rank values of objects while an order vector contains the names of alternatives. In this paper, rank values will be used for computation purposes, and object names will be used for description purposes.

Hence, we consider that each order of alternatives is represented by a priority vector $R _ { k } { = } ( r _ { k 1 } , { \ldots } , r _ { k N } )$ where $r _ { k j }$ is the rank given to the jth alternative by the kth DM. By convention, the value 1 is assigned to the most valued alternative and N to the least important. The group aggregated ranking is denoted by $R _ { G } = ( r _ { G 1 } , . . . , r _ { G N } )$ . The DMs individual preferences as well as the collective order are expressed by means of linear orders. In this situation, every DM is able to order the whole set of alternatives X, whereby indifference between them is not permitted. Note that in this case, priority vectors are permutations on the set $C = \{ 1 , 2 , . . . , N \}$

The objective of a preference–aggregation procedure is to determine a rank of alternatives $R _ { G }$ that represents the individual preferences of the K DMs as accurately as possible. Hence, the objective of the procedure is to determine the ranking of alternatives that best agrees with the individual preferences or, in other words, the ranking that minimizes the disagreement between individuals.

Implicit in this problem of minimizing the disagreement between DMs is the existence of a measure of agreement or disagreement between individual preferences, represented here by rankings of alternatives. Therefore the approach implies <sup>fi</sup>rst the introduction of a distance function for the set of rankings which satis<sup>fi</sup>es certain desirable axioms related to social choice properties and then the determination of that ranking which minimizes the total distance between DMs (see, among others, [11] and [10]).

Two groups of distance measures have been utilized in the literature: spatial and disorder distances.

Spatial distance measures the differences of rank values between two rank vectors. Let $R _ { k }$ and $R _ { i }$ be two priority vectors representing the individual preferences of agents k and i respectively. The distance between vectors is given by the expression

$$
d (R _ {i}, R _ {k}) = \sum_ {j = 1} ^ {N} \left| r _ {i j} - r _ {k j} \right| ^ {p}.\tag{1}
$$

When $p = 1$ , we have the Spearman foot rule distance, obtained as the summation of the absolute rank differences of two rank vectors. The Spearman distance is the square of the Euclidean distance $( p = 2 )$

Disorder distance measures the number of disorder pairs between two rank vectors. The use of consensus models based on spatial metrics or those approaches based on a rank sum automatically implies that a numerical interpretation is being associated to the ordinal scale positions. Hence the basic premise behind these approaches is that there is a utility or worth associated with the rank positions. A common criticism of using this class of models is that the rank positions are themselves being treated as those utilities [9]. Although the use of disorder distances may avoid the criticism of numeric assumptions about rank values, it should be borne in mind that this approach is only concerned with the order direction of the alternatives instead of the magnitude of rank values.

The Hamming-distance summarizes the number of objects which have different rank values in two rank vectors

$$
d (R _ {i}, R _ {k}) = \# \left\{j \mid r _ {i j} \neq r _ {k j}, j = 1, \dots , N \right\}.\tag{2}
$$

The Kendall-distance summarizes the number of discordant pairs from pairwise comparisons between two rank vector

$$
d (R _ {i}, R _ {k}) = \sum_ {h = 1} ^ {N} \sum_ {j = 1, j \neq h} ^ {N} I \Big [ \Big (r _ {i j} - r _ {i h} \Big) \Big (r _ {k j} - r _ {k h} \Big) <   0 \Big ],\tag{3}
$$

where I is an indicator function, I=1 if the logical expression is true; $I { = } 0$ otherwise. This measure represents the number of pairwise adjacent transportations needed to transform from one list to the other.

In every case, we de<sup>fi</sup>ne the consensus vector as that vector $R _ { G }$ which minimizes the total distance across DMs over the set of feasible priority vectors. The objective of the procedure ${ \mathrm { i } } s ,$ therefore, to determine the solution of the following optimization problem

$$
\begin{array}{l l} \text {Min} & F (d (R _ {1}, R _ {G}),..., d (R _ {K}, R _ {G})) \\ \text {s.t.} & R _ {G} \in S; \end{array}\tag{4}
$$

where $s$ represents the set of permutations over the set C (equivalently the set of priority vectors that represent linear orders over the set X) and F is a disagreement function that aggregates the individual distances. Considering a weighting vector w, which emphasizes the relative importance of DMs into the group, the two most usual forms of this function are the following:

• Total disagreement across DMs. In this case $F ( d ( R _ { k } , R _ { G } ) ) =$ $\begin{array} { r } { \sum _ { k = 1 } ^ { K } w _ { k } \cdot d ( R _ { k } , R _ { G } ) } \end{array}$ . The disagreements of all the members of the group are considered in order to determine the group consensus (each weighted with the corresponding weighting factor).

• Maximum disagreement, $F ( d ( R _ { k } , R _ { G } ) ) = m a x _ { k = 1 , \ldots , K } \{ w _ { k } \cdot d ( R _ { k } , R _ { G } ) \}$ In this case, only the disagreement of the worst DM is considered in order to determine the solution for the group. This class of function is related to the concept of justice of Rawls (see, for a detailed explanation, [15]).

In order to determine the minimum of total disagreement we have to operate with a distance function which initially requires the determination of the solution of a non-linear optimization problem. In most cases, these non-linear functions can be reduced to a linear programming model by considering a Goal Programming formulation (see [15] for the case of spatial distances and [5] for the case of disorder distances).

In all these models the inclusion of weighting factors, is used in an effort to represent the relative importance of DMs in the group decision. However, the relative importance of the ordinal position of the alternative that induces the disagreement is a relevant aspect in order to determine the social order. In the following section, a new distance-based procedure is developed in which a weighted distance is proposed, where the weighting factors are related with the position that each alternative occupies in the rank orders.

## 3. Weighted distance-based aggregation procedure

The main idea of the model proposed here can be summarized as follows. When the DMs elicit their individual preferences (in our case by constructing a ranking of alternatives), the attention paid to the evaluation of the alternatives can vary depending on the rank position in which the alternative is placed. Several studies in the context of surveys, market research or contingent valuation (see, for instance, [2] or [13]) have investigated the responses' behavior in these situations, when the preference data are elicited in form of rankings, showing that more noise appears with respect to the middle positions of the rankings.

In addition, group decision procedures suppose, in some cases, the selection of a number of alternatives, those ones ranked in the top positions, or the elimination of the alternatives ranked at the bottom places. Therefore, the discrimination between those alternatives ranked in the top positions should always command more importance than those placed in the middle of the ranking. A similar interpretation can be given to the alternatives ranked in the bottom places. In these cases, in particular for those procedures in which alternatives are eliminated, the relative importance of a unit of disagreement caused by the last alternatives should be weighed appropriately.

Therefore, a disagreement function that re<sup>fl</sup>ects this feature should weigh the individual disagreement values related to the rank position that each alternative occupies in the rankings. Note that the disagreement of a DM is obtained as the sum of differences over the complete set of alternatives (the form in which these differences are computed depends on the metric <sup>fi</sup>nally considered). The idea here is to weigh the differences of each alternative by including weighting factors related to the rank position of the alternative. Hence a unit of distance determined by one alternative will be computed differently, depending on which one induces this difference (in particular, in which rank each alternative is placed determines the relative importance of this part of the disagreement).

The motivation of the procedure proposed can be summarized as follows. The model tries to overcome one of the weaknesses of the traditional distance-based models. All the differences are equally considered so a unit of distance produced by the top alternative can be compensated by a difference caused by one alternative in the middle of the ranking. The importance of the alternatives in the group order and in the individual preferences should be treated differently. A <sup>fl</sup>exible procedure is proposed here, which admits different preference representations, and can be utilized as an alternative for traditional distance-based models or as a complementary procedure, in order to discriminate between multiple solutions (in case that they appear).

Two models are presented that depend on which order (i.e., individual order or social order), is considered so as to assign the weights to the individual differences.

## 3.1. Model based on individual positions

Consider a weighting vector $\omega = ( \omega _ { 1 } , . . . , \omega _ { N } )$ associated to the rank position of an alternative such that $\omega _ { h }$ represents the weight associated to a unit of disagreement caused by an alternative ranked in the hth position. For an easier interpretation of the values conditions of nonnegativity and normalization $\begin{array} { r } { ( \sum _ { h } ^ { N } \mathbf { \sigma } _ { h } = \mathbf { \sigma } _ { 1 } \mathbf { \sigma } \mathbf { 0 } _ { h } = 1 ) } \end{array}$ are imposed, (i.e., $\mathfrak { o } \in \Lambda ^ { + } = \{ \mathfrak { o } _ { h } \in \mathbb { R } ^ { + } , \sum _ { h = 1 } ^ { N } \mathfrak { o } _ { h } = 1 \} \bar { } )$

The form of vector ω determines the idea inherent in the aggregation procedure. The interpretation of vector ω is as follows. For a DM, a unit of disagreement (measured by a unit of distance) derived from an alternative ranked in the hth position does not have the same meaning as a unit derived from an alternative that is ranked in the (h+1)th position. In particular, an exchange rate of $\frac { { { \bf { \omega } } _ { { \bf { u } } } } } { { { \bf { \omega } } _ { { \bf { u } } + 1 } } }$ is established. The selection of a particular form for ω is determined by the objective of the aggregation procedure (selection of the best alternative, selection of a group of alternatives, and elimination of the worst alternatives).

By considering a vector such that $\omega _ { h } = 1 / N , \forall h = 1 , . . . , N ;$ all the rank positions are weighted equally. This is equivalent to the traditional distance-based models in which all the differences of the alternatives compute to the same value, independently of the rank position these alternatives occupy.

A vector ω such that $\pmb { \omega } _ { 1 } \ge \pmb { \omega } _ { 2 } \ge . . . \ge \pmb { \omega } _ { N }$ gives a greater importance to the distance derived from the alternatives ranked in the top positions. In such a case, a unit of difference derived from the alternative ranked in the <sup>fi</sup>rst position computes to a higher value than the same unit produced by any other alternative (ranked in a lower position). Note that a large enough difference between the components of vector ω leads to a lexicographical order of the distances in the determination of the solution.

A vector such that $\omega _ { 1 } \geq \omega _ { 2 } \geq . . . \geq \omega _ { N / 2 } \leq \omega _ { N / 2 + 1 } \leq . . . \leq \omega _ { N }$ assigns greater importance to the extreme positions against the central ones. That ${ \mathrm { i } } s ,$ it considers that the discrimination is focused on the extreme positions of the ranking.

Two groups of constraints are required in model (4) to incorporate this feature. Firstly, in order to capture the rank position of alternative x<sub>j</sub> in the preferences of agent k, the following sets of constraints are included:

$$
\begin{array}{l l} r _ {k j} - \sum_ {h = 1} ^ {N} t _ {j h} ^ {k} \cdot h = 0, & \forall j, k \\ \sum_ {h = 1} ^ {N} t _ {j h} ^ {k} = 1, & \forall j, k \\ t _ {j h} ^ {k} \in \{0, 1 \}, & \forall h, j, k. \end{array}\tag{5}
$$

By means of the binary variables $t _ { j h } ^ { k } ,$ , the rank position of $x _ { j }$ is captured in the sense that

$$
t _ {j h} ^ {k} = \left\{ \begin{array}{l l} 1 & \text { if   } x _ {j} \text {   is   ranked   at   the   } h \text { th   position   by   the   DM   } k, \\ 0 & \text { otherwise. } \end{array} \right.\tag{6}
$$

Once the rank position of alternative $x _ { j }$ is detected, the next step is the inclusion of the values of ω in the disagreement measure. By considering that the distances between preferences orders are measured by the $l _ { 1 }$ distance measure (a similar approximation can be obtained for other distance measures by expressing the differences induced by each alternative individually), the disagreement value of DM k can be measured by the following expression

$$
D (k) = \sum_ {j = 1} ^ {N} \left| r _ {k j} - r _ {G j} \right| \cdot \left(\sum_ {s = 1} ^ {N} \omega_ {s} \cdot t _ {j s} ^ {k}\right),\tag{7}
$$

where $| r _ { k j } - r _ { G j } |$ measures the distance between the alternative $x _ { j }$ from the individual order of agent k to the social order $R _ { G } .$

From the sum $\begin{array} { r } { \sum _ { s = 1 } ^ { N } \mathbf { \epsilon } _ { 1 } \mathbf { \epsilon } ^ { } \mathbf { \omega } ^ { } \cdot \mathbf { \epsilon } t _ { j s } ^ { k } , } \end{array}$ the weighting factor that corresponds to the alternative $x _ { j }$ is derived. It should be borne in mind that $t _ { h j } ^ { k }$ is equal to unity only in the case when $r _ { j h } = h ,$ otherwise t<sup>k</sup> is null as a consequence of the restrictions imposed in Eq. (5). This implies that $\begin{array} { r } { \sum _ { s = 1 } ^ { N } \mathbf { { \Theta } } _ { } \mathbf { { \Theta } } _ { 1 } \mathbf { { \Theta } } \sum _ { s = 1 } ^ { N } \mathbf { { \Theta } } _ { \mathbf { { 0 } } _ { h } } \mathbf { { \Theta } } _ { 1 } \mathbf { { \Theta } } _ { 2 } \mathbf { { \Theta } } _ { 1 } \mathbf { { \Theta } } _ { 2 } \mathbf { { \Theta } } _ { 2 } } \end{array}$ , that is to say, the weighting factor applied to the distance derived from $x _ { j }$ is related to the position that the alternative occupies in the ranking of DM k.

The solution of this model can be computed by solving a linear programming model, considering a linear approximation of the distance measures (in [15] the approximation of $l _ { 1 }$ and l is developed). It is worth bearing in mind that the proposed procedure is compatible with the inclusion of a vector of weights that represents the relative importance of the DMs in the <sup>fi</sup>nal decision and holds the properties veri<sup>fi</sup>ed by this class of procedures in the context of social choice (anonymity, neutrality, and non-dictatorship).<sup>1</sup>

## 3.2. Model based on group position

Contrary to the previous model, in this proposal, the weights of ω are associated to the positions that each alternative occupies in the group order and not in the individual rankings. It is worth pointing out that, in this case, social positions as well as the assignation of weighting factors are determined at the same time.

To capture these values the following sets of constraints are required:

$$
\begin{array}{l l} r _ {G j} - \sum_ {h = 1} ^ {N} t _ {j h} \cdot h = 0, & \forall j \\ \sum_ {h = 1} ^ {N} t _ {j h} = 1, & \forall j \\ t _ {j h} \in \{0, 1 \}, & \forall h, j. \end{array}\tag{8}
$$

Note that in this case the same weight will be applied to each alternative, independent of which position the alternative occupies in the individual preference rankings (since the weights are associated to rank positions in the group order). The interpretation of binary variables $t _ { j h }$ is

$$
t _ {j h} = \left\{ \begin{array}{l l} 1 & \text { if   } x _ {j} \text {   is   ranked   at   the   } h \text { th   position   in   } R _ {G}, \\ 0 & \text { otherwise. } \end{array} \right.\tag{9}
$$

The disagreement value of DM k can be measured by

$$
D (k) = \sum_ {j = 1} ^ {N} \left| r _ {k j} - r _ {G j} \right| \cdot \left(\sum_ {s = 1} ^ {N} \omega_ {s} \cdot t _ {j s}\right).\tag{10}
$$

The weighting factors assigned to each alternative, obtained through the sum $\begin{array} { r } { \sum _ { s = 1 } ^ { N } \mathbf { \epsilon } _ { 1 } \mathbf { \epsilon } _ { s } \cdot \mathbf { \epsilon } _ { t _ { j s } , } } \end{array}$ , are related with the ordinal position that each alternative occupies in the social order. Note that in the previous section, the weighting factors vary from one DM to another since these values are related to the individual perceptions of the alternatives and not with the social evaluations.

In this case it is impossible to achieve a linear expression of the model, since the values of $\omega _ { h }$ are determined as variables of the problems (and not derived directly from the individual preferences of the agents, as by model (5)). Hence the solution should be obtained using an appropriate software such as LINGO.

## 4. Illustrative example

In this section, in order to illustrate the proposed procedure two numeric examples are presented. In both examples, the model proposed in Section 3.2 is applied, in which the weights are related with the rank position that the alternatives occupy in the group order. In the <sup>fi</sup>rst case, the model is applied in order to directly determine the group's rank order, as an alternative to traditional models in which all the differences are treated equally. In Example 2, the model is applied in order to discriminate between multiple solutions obtained from a minimum-distance model.

Example 1. Let us consider a group of four experts who have expressed their preferences over a set of <sup>fi</sup>ve alternatives by means of ranking. Table 1 summarizes the individual rankings.

For the determination of the collective solution, the $l _ { 1 }$ distance is considered in order to measure the individual disagreements. It is assumed that the opinions of all the DMs are equally important and the total disagreement across DMs is computed in order to determine the social ranking. The solution obtained is $R _ { G } = ( 1 , 3 , 2 , 4 , 5 )$ and is unique. It supposes 16 units of disagreement (obtained as the sum of the individual disagreements of the DMs).

Suppose that all the DMs agree that the importance of a unit of distance between rank orders should not be computed as equal, but should instead depend of which alternative produces such a disagreement. The idea is to give more importance to the top positions against the bottom positions, whereby a unit of disagreement induced by an alternative ranked in the hth position is weighted twice that of a unit induced by an alternative placed in next position (position $h + 1 )$ . This feature can be modeled by including a set of weighting factors such that ${ \mathfrak { o } } = \left( { \frac { 1 6 } { 3 1 } } , { \frac { 8 } { 3 1 } } , { \frac { 4 } { 3 1 } } , { \frac { 2 } { 3 1 } } , { \frac { 1 } { 3 1 } } \right)$

Table 1 Example 1: individual rankings.

<table><tr><td>Alternative</td><td> $R_1$ </td><td> $R_2$ </td><td> $R_3$ </td><td> $R_4$ </td></tr><tr><td> $x_1$ </td><td>1</td><td>3</td><td>1</td><td>5</td></tr><tr><td> $x_2$ </td><td>2</td><td>1</td><td>3</td><td>3</td></tr><tr><td> $x_3$ </td><td>3</td><td>2</td><td>2</td><td>1</td></tr><tr><td> $x_4$ </td><td>4</td><td>4</td><td>5</td><td>2</td></tr><tr><td> $x_5$ </td><td>5</td><td>5</td><td>4</td><td>4</td></tr></table>

The solution of model that weights the position obtained in the group's ranking achieves a disagreement of 18 units, with a new social order such that $R _ { G } ^ { ' } = ( 3 , 2 , 1 , 4 , \bar { 5 } )$ . The optimal disagreement is raised <sup>ð Þ</sup>by two units although it improves the differences induced by the alternatives ranked in the top positions are improved.

It can be observed that the resulting value is improved from the previous solution from 4.259, (the value of disagreement induced by $R _ { G }$ when vector ω is considered), to 3.871, which corresponds to the weighted disagreement induced by $R _ { G } ^ { ' } .$ In particular, the differences induced by the alternative ranked at the <sup>fi</sup>rst position, $x _ { 1 }$ in $R _ { G }$ and $x _ { 3 }$ in $R _ { G } ^ { ' } ,$ , fall from 6 to 4 units (which also suppose that the disagreement induced by the alternatives ranked at the second and third position increase from $R _ { G }$ to $R _ { G } ^ { ' } )$ . Obviously, the weighted values are compensated in order to give a lower value of the objective function. Table 2 summarizes the main results.

Example 2. Let us consider a group decision-making problem in which <sup>fi</sup>ve DMs are required to rank a set of seven alternatives. The linear orders provided by each DM are represented in Table 3 by their corresponding priority vectors.

For the determination of the collective solution the $l _ { 1 }$ distance is considered in order to measure the individual disagreements. It is assumed that the opinions of all DMs are considered equally important and the total disagreement across DMs is computed in order to determine the social ranking. The minimum-disagreement solution is equal to 38 units. In this case, the group's ranking is not a singleton, several different orders can induce this minimum level of disagreement.

By considering the proposed model, it is possible to discriminate between optimal solutions. Suppose that all the DMs agree on the application of the same vector as that in the previous example (adapted for the context of seven-position rankings). That is to say, a vector such that ${ \mathfrak { o } } = \left( { \frac { 6 4 } { 1 2 7 } } , { \frac { 3 2 } { 1 2 7 } } , { \frac { 1 6 } { 1 2 7 } } , { \frac { 8 } { 1 2 7 } } , { \frac { 4 } { 1 2 7 } } , { \frac { 2 } { 1 2 7 } } , { \frac { 1 } { 1 2 7 } } \right)$ is considered, which implies an exchange rate $\frac { { \bf { \omega } } _ { { \bf { 0 } } _ { h } } + { \bf { \omega } } _ { 1 } } { { \bf { \omega } } _ { h } } = \frac { 1 } { 2 } .$ As before, one unit of disagreement induced by an alternative ranked in hth position is weighted twice that of a unit induced by an alternative placed in the next position (postposition h+1). In this case, the DMs agree to give more importance to the top positions against the bottom positions.

The solution of the corresponding model, in which an additional constraint is included in order to guarantee that total disagreement does not exceed the optimal level without a weighting vector (38 units), yields a unique optimal order $R _ { G } = ( 1 , 4 , 3 , 2 , 6 , 5 , 7 )$ , with an induced weighted disagreement of 4.378. This solution improves on the original ranking in the sense that it selects, from among the optimal solution set, an order such that the distance induced by the alternatives ranked at the top position is minimized. To illustrate this feature, let us consider another solution of the minimum-distance order without a weighting vector, for instance $R ^ { \prime } { } _ { G } = ( 1 , 5 , 3 , 2 , 6 , 4 , 7 )$ The main values are summarized in Table 4.

Table 2  
Main results of Example 1.

<table><tr><td>Alternative</td><td> $R_G$ </td><td> $\sum_{k=1}^{4} |r_{kj}-r_{Gj}|$ </td><td>Weighted value</td><td> $R'_G$ </td><td> $\sum_{k=1}^{4} |r_{kj}-r_{Gj}|$ </td><td>Weighted value</td></tr><tr><td> $x_1$ </td><td>1</td><td>6</td><td>3.097</td><td>3</td><td>6</td><td>0.774</td></tr><tr><td> $x_2$ </td><td>3</td><td>3</td><td>0.387</td><td>2</td><td>3</td><td>0.774</td></tr><tr><td> $x_3$ </td><td>2</td><td>2</td><td>0.516</td><td>1</td><td>4</td><td>2.605</td></tr><tr><td> $x_4$ </td><td>4</td><td>3</td><td>0.194</td><td>4</td><td>3</td><td>0.194</td></tr><tr><td> $x_5$ </td><td>5</td><td>2</td><td>0.065</td><td>5</td><td>2</td><td>0.065</td></tr><tr><td>Total</td><td></td><td>16</td><td>4.259</td><td></td><td>18</td><td>3.871</td></tr></table>

Table 3  
Example 2: individual rankings

<table><tr><td>Alternative</td><td> $R_1$ </td><td> $R_2$ </td><td> $R_3$ </td><td> $R_4$ </td><td> $R_5$ </td></tr><tr><td> $x_1$ </td><td>1</td><td>1</td><td>2</td><td>1</td><td>3</td></tr><tr><td> $x_2$ </td><td>5</td><td>3</td><td>3</td><td>5</td><td>6</td></tr><tr><td> $x_3$ </td><td>4</td><td>4</td><td>5</td><td>4</td><td>2</td></tr><tr><td> $x_4$ </td><td>2</td><td>2</td><td>1</td><td>6</td><td>1</td></tr><tr><td> $x_5$ </td><td>4</td><td>5</td><td>6</td><td>2</td><td>7</td></tr><tr><td> $x_6$ </td><td>6</td><td>7</td><td>4</td><td>3</td><td>5</td></tr><tr><td> $x_7$ </td><td>7</td><td>6</td><td>7</td><td>7</td><td>4</td></tr></table>

It is worth pointing out that the differences with respect to the top three alternatives are the same in both solutions. In fact both solutions assign the top three positions to the same alternatives and the differences between individual and group rankings are 3, 6 and 5 units, respectively. However, with respect to the alternative placed in the fourth position, $x _ { 2 }$ in $R _ { G }$ and $x _ { 5 }$ in $R _ { G } ^ { ' } ,$ the distance across DMs varies from 6 to 7 units. The same difference of one unit but in the opposite sense appears with respect to the alternative in the <sup>fi</sup>fth position. Hence, both orders yield the same sum of distances (38 units), although a better value is offered in terms of disagreement when vector ω.

## 5. Concluding remarks

The aggregation of individual preferences into a collective or social order is a classic problem in the literature. A commonly used family of procedures includes those based on the de<sup>fi</sup>nition of a distance measure in an effort to minimize the disagreement across decision makers. In this paper, a distance-based procedure is proposed that focuses on the ordinal position or the alternatives. The proposed procedure considers that the way a unit of difference between rankings should be computed depends on which alternative produces that difference and, in particular, which is the rank position the alternative occupies.

The procedure enables the prioritization, for example, of those alternatives ranked in the top positions, and therefore gives more importance to a social solution in which the alternatives ranked in the top positions are closer to individuals' preferences in contrast with traditional models that give the same weight to any unit of difference, regardless of which alternative it is induced from. Other alternatives can be performed by modifying the weighting vector. The form proposed for the disagreement function has not affect on the main properties veri<sup>fi</sup>ed by this class of procedure in the context of social choice models.

Two numeric examples are included in order to illustrate the procedure. With these examples the main aims of the proposed models are shown: <sup>fi</sup>rst the obtention of a social order in which individual disagreements are treated separately; and second, for those cases in which the solution obtained is not a singleton, whereby the proposed model is used as a secondary goal to discriminate between multiple solutions. In this second case, the disagreement is <sup>fi</sup>xed at its minimum value by including an additional constraint, and hence the proposed model is solved to decide the best solution.

Table 4  
Main results of Example 2.

<table><tr><td>Alternative</td><td> $R_G$ </td><td> $\sum_{k=1}^{5} |r_{kj}-r_{Gj}|$ </td><td>Weighted value</td><td> $R'_G$ </td><td> $\sum_{k=1}^{5} |r_{kj}-r_{Gj}|$ </td><td>Weighted value</td></tr><tr><td> $x_1$ </td><td>1</td><td>3</td><td>1.512</td><td>1</td><td>3</td><td>1.512</td></tr><tr><td> $x_2$ </td><td>4</td><td>6</td><td>0.378</td><td>5</td><td>5</td><td>0.157</td></tr><tr><td> $x_3$ </td><td>3</td><td>5</td><td>0.630</td><td>3</td><td>5</td><td>0.630</td></tr><tr><td> $x_4$ </td><td>2</td><td>6</td><td>1.512</td><td>2</td><td>6</td><td>1.512</td></tr><tr><td> $x_5$ </td><td>6</td><td>8</td><td>0.126</td><td>6</td><td>8</td><td>0.126</td></tr><tr><td> $x_6$ </td><td>5</td><td>6</td><td>0.189</td><td>4</td><td>7</td><td>0.441</td></tr><tr><td> $x_7$ </td><td>7</td><td>4</td><td>0.031</td><td>7</td><td>4</td><td>0.031</td></tr><tr><td>Total</td><td></td><td>38</td><td>4.378</td><td></td><td></td><td>4.409</td></tr></table>

It is worth pointing out that the proposed scheme can be incorporated into other preference–aggregation procedures whenever the disagreement induced by each alternative can be individualized. Future research along these lines could include the implementation of the proposed procedure in the case of weak orders.

## Acknowledgements

The author is grateful to the anonymous referees for their contribution in improving the quality of this paper.

## References

[1] I. Ali, W.D. Cook, M. Kress, Ordinal ranking with intensity of preference: a linear programming approach, Management Science 32 (12) (1986) 1642–1647.

[2] M. Ben-Akiva, T. Morikawa, F. Shiroishi, Analysis of reliability of preference ranking data, Journal of Business Research 23 (1991) 253–268.

[3] J.C. Borda, Mémoire sur les élections au scrutin, Histoire de l'Académie Royale des Sciences, 1784.

[4] Y.-L. Chen, L.C. Cheng, An approach to group ranking decision in a dinamic environment, Decision Support Systems 48 (2010) 622–634.

[5] I. Conteras, Ordered weighted disagreement functions, Group Decision and Negotiation (2010), doi:10.1007/s10726-010-9210-x.

[6] W.D. Cook, Distance-based and ad hoc consensus models in ordinal preference ranking, European Journal of Operational Reseach 172 (2006) 369–385.

[7] W.D. Cook, M. Kress, Ordinal ranking with intensity of preference, Management Science 31 (1) (1985) 26–32.

[8] W.D. Cook, M. Kress, Ordinal ranking and preference strength, Mathematical Social Sciences 11 (1986) 295–306.

[9] W.D. Cook, M. Kress, An extreme-point approach for obtaining weighted ratings in qualitative multicriteria decision making, Naval Research Logistic 43 (4) (1996) 519–531.

[10] W.D. Cook, M. Kress, L.M. Seiford, A general framework for distance-based consensus in ordinal ranking models, European Journal of Operational Research 96 (2) (1997) 392–397.

[11] W.D. Cook, L.M. Seiford, Priority ranking and consensus formation, Management Science 24 (16) (1978) 1721–1732

[12] W.D. Cook, L.M. Seiford, On the Borda–Kendall consensus method for priority ranking problems, Management Science 28 (6) (1982) 621–637.

[13] V. Foster, S. Mourato, Testing for consistency in contingent ranking experiments, Journal of Enviromental and Management 44 (2002) 309–328.

[14] J.L. García-Lapresta, Weighting individual opinions in group decision making Lecture Notes in Computer Science 4617 (2007) 92–103.

[15] J. González-Pachón, C. Romero, Distanced based consensus methods: a goal programming approach, Omega 27 (3) (1999) 341–347.

[16] J. González-Pachón, C. Romero, Aggregation of partial ordinal rankings: an interval goal programming approach, Computers and Operations Research 28 (8) (2001) 827–834.

[17] Jeabeur, K., Martel, J.M., Guitouni, A. Deriving a minimum distance-based collective preorder: a binary mathematical programming approach. OR Spectrum (in press). doi:10.1007/s00291-009-0192-5.

[18] J. Kemeny, Mathematics without numbers, Daedalus 88 (1959) 571–591.

[19] J.G. Kemeny, L.J. Snell, Preference ranking: an axiomatic approach, Mathematica Models in the Social Choice Sciences, Ginn, New York, 1962, pp. 9–23.

[20] M. Kendall, Rank Correlation Methods, Hafner, New York, 1962.

[21] C. Klamler, D. Eckert, J. Mitlöhner, C. Schlötterer, A distance-based comparison of basic voting rules, Central European Journal of Operations Research 14 (4) (2000) 377–386.

[22] H. Nurmi, A comparison of some distance-based choice rules in ranking environments, Theory and Decision 57 (1) (2004) 5–24.

[23] Y.M. Wang, J.B. Yang, D.L. Xu, A preference aggregation method through the estimation of utility intervals, Computers and Operations Research 32 (8) (2005) 2027–2049.

[24] H.P. Young, Social choice scoring functions, SIAM Journal on Applied Mathematics 28 (4) (1975) 824–838.

Ignacio Contreras is an Associate Professor at the Pablo de Olavide University, Sevilla, Spain. His topics of interests are multicriteria decision making procedures, data envelopment analysis (DEA) and group decision methods, with publications in, among others, the following journals: European Journal of Operational Research, Group Decision and Negotiations, Journal of the Operational Research Society and Expert Systems with Applications.
