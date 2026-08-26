---
otero_id: 2550
otero_key: "S8YESPC6"
title: "The reliability analysis of rating systems in decision making: When scale meets multi-attribute additive value model"
authors: "Sihai Zhao; Yucheng Dong; Ying He"
year: "2020"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2020.113384"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# The reliability analysis of rating systems in decision making: When scale meets multi-attribute additive value model

![](/api/attachments/S8YESPC6/fulltext/images/0d19871ecc3ed5a69f02ddb042494eae1c1fcffab79dfe30c4ea9519df42b3b1.jpg)

Sihai Zhao<sup>a</sup>, Yucheng Dong<sup>a,⁎</sup>, Ying He<sup>b</sup>

<sup>a</sup> Center for Network Big Data and Decision-Making, Business School, Sichuan University, Chengdu 610065, China <sup>b</sup> Department of Business and Economics, University of Southern Denmark, Odense, Denmark

## A R T I C L E I N F O

Keywords: Rating systems Multi-attribute additive value model Asymmetric information Reliability Consistency

## A B S T R A C T

A rating system (RS) comprises a rating metric defined by a discrete set of integers contained in an interval (e.g., [0, N]), and an aggregation rule. RSs are widely used in various fields to capture and summarize individuals opinions on alternatives. In this paper we argue that the multi-attribute additive value model (MAVM) should be used as a benchmark to analyze the reliability of RSs, and present some tight bounds on the parameter N and overall rating scores, which guarantee the consistency between the RS [0. N] and MAVM at the ranking and rating levels. Interestingly, the tight bounds at the rating level are twice as large as those at the ranking level. The results in this paper can provide new insights about the reliability analysis of RSs.

## 1. Introduction

Rating systems (RSs) are widely used in business, management, education and many other fields as a method to capture and summarize individuals' opinions on alternatives [16,17,36,38,46,47,52]. Typically, the RS is an efective tool to deal with asymmetric information between sellers and customers in the market [1,8,45]. Using RSs, products, candidates, or enterprises are often assessed to obtain rankings or ratings in diferent decision making situations. For example, a company may rate a candidate to decide whether to ofer a job; an investor may consult the rating information of enterprises; and a bank may rate customers to determine their credit limits.

An RS usually comprises a rating metric defined by a set of integers contained in a finite interval, and an aggregation rule which combines individual rating information into an overall rating score [7]. For in stance, a binary metric [−1, 1] refers to a 3-point scale containing three rating options: −1, 0, 1. The aggregation rule might be a simple weighted average to perform the aggregation process. Using the RSs information, decisions such as buying a product or selecting an excellent employee can be made.

The reliability analysis is one of the most challenging issues in the RS research because inconsistent decision outcomes may occur under diferent RSs. In the existing literature, three ways to analyze the reliability of RSs have been proposed:

(1.) Misunderstanding of the meaning of the scale. Most research on rating scales empirically explores how people rate when given diferent rating scales [9,13,20,21,25,35], and it is found that people often do not understand the meaning of the scale in an RS [2,34,39]. Preston and Colman [42] showed that the 2-point, 3- point and 4-point scales performed significantly worse on several indices of reliability, validity and discriminating power than scales with more response categories. Weijters et al. [50] pointed out that scale formats have strong efects on response distributions and misresponse to reversed items, and then formulated recommendations on the choice of a scale format. Schwarz et al. [44] found that using a scale [−3, 3] leads to diferent rating results from using a scale [1, 7], which implies that the actual numeric values used in an RS will afect raters' expression of true opinions. If an RS cannot capture the details of people's true opinions, it may be dificult to make an efective decision, and thus the reliability of the RS is debatable. Similar studies can be found in the decision making models dealing with linguistic scales (e.g., [22,28]).

(2.) Strategic behaviors. Another explanation attributes inconsistent decision outcomes to raters' strategic behaviors. Cleveland and Murphy [10] and Murphy et al. [41] pointed out that raters may have different individual goals due to the fact that they may come from different domains or they all own particular interests. These goals will afect the efectiveness of the evaluation information they provide, which in turn afects the reliability of the final decision outcome. For example, a rater may use strategic behaviors to make his/her most preferred alternative(s) selected. In decision analysis, there exist some similar studies to examine the impacts of strategic behaviors on decision outcomes, and to provide some efective mechanisms for defending against strategic manipulations $[ 1 1 , 1 4 , 1 5 , 4 0 , 4 9 ]$

(3.) Rounding process in RSs. Bargagliotti and Li [4] proposed a novel view that diferent decision outcomes may occur without human fault. Instead, the use of the rounding process in RSs plays an important role. They investigated the consistency between the scale metric [1, N] and the binary metric [−1, 1] at the re presentation and aggregation levels. It is proved that any two opinions represented by the same rating in the scale metric are also represented by the same rating in the binary metric if and only if N is odd and $N - 1$ is not divisible by 4. Besides, several suficient conditions are provided to guarantee the same aggregation deci sion outcome when consulting both metrics.

The existing research has provided useful insights about the relia bility analysis of RSs, but most of them empirically investigated the impact of people's psychological and behavioral factors on the reliability of RSs. Although Bargagliotti and Li [4] proposed an analytical view about the RSs' reliability, we find that there are some gaps that should be further filled:

(1.) The ranking and rating consistency of multiple alternatives in RSs. Bargagliotti & Li [4] only investigated the consistency of a single alternative between the scale metric [1, N] and the binary metric [−1, 1] at the representation and aggregation levels. It is common that we want to obtain the ranking or ratings of multiple alternatives in practical RS problems. For example, when someone is going to buy a smart phone online, what she may mostly care about is the ranking of the alternative smart phones on sale. Besides, a number of hotels are rated diferent stars (e.g., a five-star hotel). Therefore, we argue that it is of key importance to study the consistency of multiple alternatives in RSs at the ranking and rating levels to cope with real-world RS decision problems.

(2.) The consistency between RSs and multi-attribute additive value model (MAVM) [31]. Essentially, RS is a method used to aggregate individuals' preferences. Such a problem has been extensively studied in economics in the fields of social choice and decision theory [3,6,18,26,32,33,37]. In decision theory, group utility is studied based on axiomatic approach, which provides a solid theoretical foundation for studying preferences aggregation. Axioms are observable conditions on the preferences. which make the utility theory testable on behavioral level. RS is proposed as a method to aggregate individuals' preferences to fulfill the same purpose as group utility theory; but it lacks such a theoretical foundation. Therefore, it is interesting to investigate how RS can be connected to the group utility theory. The MAVM is a classical model in multi-attribute utility theory [18,19,27,31,33,48], which has been used to axiomatize group utility [32]. It has the high interpretability of numerical scores that can be decomposed into individual values (e.g., [24,30]). However, when evaluating products, candidates, or enterprises in business, we often use RSs (not MAVM). In essence, RS problems can be modeled by multiple attribute decision making because evaluating an alternative by multiple raters is equivalent to that by multiple attributes [29], and in the aggregation rules of RSs the additive model is widely employed [4,7]. Therefore, RS can be considered as an approximate model of MAVM, and thus it is necessary to study the consistency between RS and MAVM. When the decision outcomes between RS and MAVM are consistent, we argue that the RS is reliable.

Similar to Bargagliotti & Li [4], it is assumed that the perceived state (PS) of a rater for the quality of an alternative exists, and the available metric requires the rater to choose a discrete rating to represent the PS for the alternative. In this paper, we model PS by a continuous measurement in the interval [0,1], and the PSs are assumed to be linearly transformed (with rounding) into discrete integer ratings in the interval [0, N], called the RS [0, N]. We argue that the PSs could be regarded as values of an alternative associated with multiple raters because the PSs and values are essentially the same thing and both of them measure how satisfied people are with an alternative [3,12,26,31,33]. Then, the MAVM is employed as the basis to analyze the reliability of RSs. We analytically present some tight bounds on the parameter N and overall rating scores to guarantee the consistency between the RS [0,N] and MAVM at the ranking and rating levels. Interestingly, the tight bounds at the rating level are twice as large as those at the ranking level. Furthermore, we present the detailed simulation analysis to show more findings on the consistency of decision outcomes between RS and MAVM.

The results in this paper can provide useful insights for the reliability analysis of RSs. If PSs are available, MAVM can be employed to get reliable results. However, RS is widely used as an approximate model of MAVM in practical decision problems, which sometimes leads to unreliable results. For instance, two candidates (A and B) compete for a position, and three interviewers with same importance rate A and B on the scale [0, 5]. The interviewers' PSs are 0.82, 0.91, 0.86 for $\mathsf { A } ;$ and 0.86, 0.89, 0.88 for B. Using the RS [0, 5], the interviewers rate A as $4 , 5 ,$ 4; and B as 4, 4, 4, respectively. Then the weighted average scores of A and B are 4.3 and 4, respectively, and thus A is more preferred. However, on the basis of MAVM, the aggregation results of PSs are 0.863 and 0.877 for A and B, respectively, and thus B is more preferred. Therefore, the RS leads to the inconsistent decision outcome with MAVM. In this paper, using MAVM as a benchmark, we provide some analytical conditions to show the key roles of the parameter N and overall rating scores in the reliability analysis of RSs.

The remainder of this paper is organized as follows. The next section introduces the framework to study the consistency between RS and MAVM. Then, we present the analytical consistency conditions between RS and MAVM at the ranking and rating levels in Section 3. Following this, in Section 4 simulation experiments are demonstrated to further explore the properties of RSs, and a hypothetical example of application is presented to illustrate the usability of the obtained results in practical RS problems. Finally, conclusion and future perspectives are included in Section 5.

## 2. Framework

An RS comprises a rating metric and an aggregation rule. The rating metric is a discrete set of integers contained in an interval. Let int[e, f] be the set of integers between e and f which contains e and f. Let $t _ { i j } \in i n t \ [ e , f ]$ be the rating of alternative i associated with rater ${ } \cdot j .$ For alternative i and m raters, $( i n t [ e , f ] ) ^ { m }$ denotes the space of all possible mtuples $( t _ { i 1 } , t _ { i 2 } , . . . , t _ { i m } ) .$ . The aggregation rule is some type of averaging function over $( t _ { i 1 } , t _ { i 2 } , . . . , t _ { i m } )$

Definition 1. (Bargagliotti and Li [4]): An RS is the pair (int[e, f], G) where G is an aggregation function from $( i n t [ e , f ] ) ^ { m }$ to the interval $\lbrack e , f ] { : }$

G: $( i n t [ e , f ] ) ^ { m }  [ e , f ]$

In this paper, we assume that the rating metric is the RS [0, N], which will not change the essence of an RS, and we consider that the RS aggregation rule is a weighted average.

Similar to [4], it is assumed that the PS of a rater for an alternative exists, and the available metric requires the rater to choose a discrete rating to represent his/her PS for the alternative. In this paper, we model the PSs as continuous values in the interval [0,1], and assume that there exists a linear transformation process (with rounding) from PSs to ratings. Let v ∈ [0, 1] be a PS, and the PS can be transformed into a rating, t, in a $[ 0 , N ]$ metric based on Eqs. (1) and (2):

$$
v ^ {\prime} = N \times v\tag{1}
$$

$$
t = \text { rounding } (v ^ {\prime})\tag{2}
$$

where v′ is the value in the interval [0, N] linearly transformed from v, and rounding is a rounding operation. When $\nu ^ { \prime }$ is located at halfway between two integer values, in this paper t will be the larger one. For instance, there is a PS that $\nu = 0 . 3 ,$ , and then its rating is t = rounding $( 0 . 3 \times 5 ) = 2$ when the rating metric is [0, 5]. This assumption is also made in the previous literature on RS. However, it should be noted that if another rounding point is adopted, all results of this paper are still valid.

The RS problem can be modeled by multiple attribute decision making because evaluating an alternative by multiple raters is equivalent to the group decision making problem where individuals values are aggregated to a group value by multiple attribute value function $[ 5 , 6 , 1 8 , 2 9 , 3 1 ]$ . Thus, in this paper we consider the following multiple attribute decision making problem:

Let $X = \{ x _ { 1 } , x _ { 2 } , . . . , x _ { n } \}$ be a set of alternatives; $A = \{ a _ { 1 } , a _ { 2 } , . . . , a _ { m } \}$ be a set of attributes, where an attribute is equivalent to a rater in the RS; and $\pmb { w } = \{ w _ { 1 } , w _ { 2 } , . . . , w _ { m } \} ^ { T }$ be a weight vector of attributes such that $w _ { i } \geq 0$ and ${ \Sigma _ { i = 1 } } ^ { m } w _ { i } = 1$ . Let $V = [ \nu _ { i j } ] _ { n \times m } ,$ where $\nu _ { i j }$ denotes the PS of alternative x associated with attribute $a _ { j } .$ Let $\begin{array} { r } { { \cal T } = [ t _ { i j } ] _ { n \times m } , } \end{array}$ where $t _ { i j } = r o u n d i n g ( N \times \nu _ { i j } ) _ { : }$ , obtained via Eqs. (1) and (2), is the rating of alternative $x _ { i }$ associated with attribute $a _ { j }$ in the RS [0, N].

The PS measures how satisfied people are with an alternative, essentially, $\nu _ { i j }$ also represents the value of alternative $x _ { i }$ over attribute a in the framework of MAVM [3,12,26,31,33]. Therefore, the MAVM is employed to weigh all attributes according to the PSs provided. Then the value of alternative x is determined by $V _ { i \cdot }$

$$
V _ {i} = \sum_ {j = 1} ^ {m} w _ {j} v _ {i j}\tag{3}
$$

On the other hand, the evaluation information provided to the decision maker can be in the form of a collection of scale ratings capturing the quality of alternatives associated with raters (i.e., attributes). Then, the weighted average is used to derive the overall rating score of alternative x in the RS [0,N] by $T _ { i \cdot }$

$$
T _ {i} = \sum_ {j = 1} ^ {m} w _ {j} t _ {i j}\tag{4}
$$

Next, we introduce the concepts of the ranking and rating as fol lows:

(i) Ranking. Let $( V _ { 1 } , V _ { 2 } , . . . , V _ { n } )$ be the values of alternatives using MAVM, from which we can obtain the ranking of alternatives: ${ \cal R } a n k i n g _ { M A V M } ( x _ { i } ) = j \mathrm { i f } V _ { i }$ is the jth largest element in $( V _ { 1 } , V _ { 2 } , . . . , V _ { n } )$ . For example, suppose that $( 0 . 2 , 0 . 5 , 0 . 3 )$ are the values of three alternatives using MAVM, then Ranking (x ) = 1. Similarly, let $( T _ { 1 } , T _ { 2 } , . . . , T _ { n } )$ be the overall rating scores of alternatives using the RS $[ 0 , N ]$ , from which the ranking of alternatives can be derived: ${ \cal R } a n k i n g _ { R S } ( x _ { i } ) = j \mathrm { i f } T _ { i }$ is the jth largest element in $( T _ { 1 } , T _ { 2 } , . . . , T _ { n } )$

Based on the ranking of alternatives, we can easily have the fol lowing results:

$$
\begin{array}{l} \text {(1)} V _ {i} > V _ {j} \Leftrightarrow (x _ {i}) <   R a n k i n g _ {M A V M} (x _ {j}) \\ \text {(2)} V _ {i} = V _ {j} \Leftrightarrow R a n k i n g _ {M A V M} (x _ {i}) = R a n k i n g _ {M A V M} (x _ {j}) \\ \text {(3)} T _ {i} > T _ {j} \Leftrightarrow R a n k i n g _ {R S} (x _ {i}) <   R a n k i n g _ {R S} (x _ {j}) \\ \text {(4)} T _ {i} = T _ {j} \Leftrightarrow R a n k i n g _ {R S} (x _ {i}) = R a n k i n g _ {R S} (x _ {j}) \end{array}
$$

(ii) Rating. When considering MAVM, similar to Eqs. (1) and (2), we can transform $( V _ { 1 } , V _ { 2 } , . . . , V _ { n } )$ into ratings in the RS [0, N] by Rating<sub>MAVM</sub> $( x _ { i } ) = r o u n d i n g ( N \times V _ { i } )$ . For example, let $( V _ { 1 } , V _ { 2 } , V _ { 3 } ) = ( 0 . 6 , 0 . 4 , 0 . 7 )$ be the values of three alternatives using MAVM, and then Rating $( x _ { 3 } ) = r o u n d i n g ( 5 \times 0 . 7 ) = 4$ in the RS [0,5]. When considering the RS [0, N], we can obtain the ratings of alternatives by Rating (x ) = rounding(T ).

Based on the ratings of alternatives, we can easily have the fol lowing results:

$$
\begin{array}{l} \text {(1)} V _ {i} > V _ {j} \Rightarrow R a t i n g _ {M A V M} (x _ {i}) \geq R a t i n g _ {M A V M} (x _ {j}) \\ \text {(2)} V _ {i} = V _ {j} \Rightarrow R a t i n g _ {M A V M} (x _ {i}) = R a t i n g _ {M A V M} (x _ {j}) \\ \text {(3)} R a t i n g _ {M A V M} (x _ {i}) > R a t i n g _ {M A V M} (x _ {j}) \Rightarrow V _ {i} > V _ {j} \\ \text {(4)} T _ {i} > T _ {j} \Rightarrow R a t i n g _ {R S} (x _ {i}) \geq R a t i n g _ {R S} (x _ {j}) \\ \text {(5)} T _ {i} = T _ {j} \Rightarrow R a t i n g _ {R S} (x _ {i}) = R a t i n g _ {R S} (x _ {j}) \\ \text {(6)} R a t i n g _ {R S} (x _ {i}) > R a t i n g _ {R S} (x _ {j}) \Rightarrow T _ {i} > T _ {j} \end{array}
$$

As mentioned above, in practical decision making problems, the inconsistency between RS and MAVM may occur. We use Example 1 to illustrate this issue.

Example 1. A decision maker is going to make a choice among two alternatives x and $\mathbf { X } _ { 2 } .$ The PSs of x and x over three attributes are $( \mathrm { v } _ { 1 1 } , \mathrm { v } _ { 1 2 } , \mathrm { v } _ { 1 3 } ) = ( 0 . 5 0 , 0 . 6 5 , 0 . 4 5 )$ and $( \mathrm { v } _ { 2 1 } , \mathrm { v } _ { 2 2 } , \mathrm { v } _ { 2 3 } ) = ( 0 . 4 4 , 0 . 7 4 , 0 . 4 3 ) ,$ respectively. Let the RS be [0, 10], and let the weights of all attributes be equal. Then, the inconsistency of decision outcomes between RS and MAVM will arise:

(i) Considering the ranking level. Ranking (x ) > Ranking (x ) because $V _ { 1 } ~ = ~ ( 0 . 5 0 ~ + ~ 0 . 6 5 ~ + ~ 0 . 4 5 ) / 3 ~ = ~ 0 . 5 3$ and $V _ { 2 } = ( 0 . 4 4 \ : + \ : 0 . 7 4 \ : + \ : 0 . 4 3 ) / 3 \ : = \ : 0 . 5 4$ . In the RS [0, 10] the ratings of two alternatives over three attributes are $( t _ { 1 1 } , t _ { 1 2 } , t _ { 1 3 } ) \ = \ ( 5 , 7 , 5 )$ and $\begin{array} { r l r } { ( t _ { 2 1 } , t _ { 2 2 } , t _ { 2 3 } ) } & { { } = } & { ( 4 , 7 , 4 ) } \end{array}$ , respectively. As a result, Ranking (x ) < Ranking (x ) because $T _ { 1 } ~ = ~ ( 5 ~ + ~ 7 ~ + ~ 5 ) / 3 ~ = ~ 5 . 7$ and $T _ { 2 } = ( 4 + 7 + 4 ) / 3 = 5 .$

(ii) Considering the rating level. $R a t i n g _ { M A V M } ( x _ { 1 } ) = R a t i n g _ { M A V M } ( x _ { 2 } )$ because Rating (x ) = rounding(10 × 0.53) = 5 and Rating $( x _ { 2 } ) \ : = \ : r o u n d i n g ( 1 0 \times 0 . 5 4 ) \ : = \ : 5 ;$ while Rating (x ) > Rating (x ) because Rating (x ) = rounding(5.7) = 6 and Rating (x ) = rounding (5) = 5.

The MAVM is a foundational and well-justified theory to evaluate alternatives, and thus we argue that MAVM should be used as a benchmark to study the reliability of RSs. If an RS is reliable, the decision outcomes between RS and MAVM should be consistent. Therefore, in order to analyze the reliability of RSs, we study the consistency issue between RS and MAVM at the ranking and rating levels. The consistency between RS and MAVM at the ranking and rating levels are formally defined in Definitions 2 and 3.

Definition 2. An RS is consistent with MAVM at the ranking level if the rankings of any two alternatives $x _ { i }$ and $x _ { j }$ conveyed by the RS and MAVM are the same, i.e., one of the following conditions holds,

$$
\begin{array}{l} (1) \left(\text {Ranking} _ {\mathrm{MAVM}} (\mathrm{x} _ {\mathrm{i}}) \quad > \quad \text {Ranking} _ {\mathrm{MAVM}} (\mathrm{x} _ {\mathrm{j}})\right) \& \quad \left(\text {Ranking} _ {\mathrm{RS}} (\mathrm{x} _ {\mathrm{i}}) \right. \\ > \text {Ranking} _ {\mathrm{RS}} (\mathrm{x} _ {\mathrm{j}})). \end{array}
$$

$$
\begin{array}{r l r} (2) \left(\text {Ranking} _ {\text {MAVM}} (\mathbf {x} _ {\mathrm{i}}) \right. & = & \text {Ranking} _ {\text {MAVM}} (\mathbf {x} _ {\mathrm{j}})) \quad \& \quad \left(\text {Ranking} _ {\text {RS}} (\mathbf {x} _ {\mathrm{i}}) \right. \\ & = \text {Ranking} _ {\text {RS}} (\mathbf {x} _ {\mathrm{j}})). \end{array}
$$

$$
\begin{array}{c} (3) (\text {Ranking} _ {\text {MAVM}} (\mathrm{x} _ {\mathrm{i}}) <   \text {Ranking} _ {\text {MAVM}} (\mathrm{x} _ {\mathrm{j}})) \\ \& (\text {Ranking} _ {\text {RS}} (\mathrm{x} _ {\mathrm{i}}) <   \text {Ranking} _ {\text {RS}} (\mathrm{x} _ {\mathrm{j}})). \end{array}
$$

Definition 3. An RS is consistent with MAVM at the rating level if the ratings of any two alternatives x and x conveyed by the RS and MAVM are the same, i.e., one of the following conditions holds,

$$
\begin{array}{l} (1) \left(\text { Rating } _ {\text { MAVM }} (\mathbf {x} _ {i}) > \text { Rating } _ {\text { MAVM }} (\mathbf {x} _ {j})\right) \& \left(\text { Rating } _ {\text { RS }} (\mathbf {x} _ {i}) > \text { Rating } _ {\text { RS }} (\mathbf {x} _ {j})\right). \end{array}
$$

$$
\begin{array}{l} (2) \left(\text {Rating} _ {\mathrm{MAVM}} (\mathrm{x} _ {\mathrm{i}}) = \text {Rating} _ {\mathrm{MAVM}} (\mathrm{x} _ {\mathrm{j}})\right) \& \left(\text {Rating} _ {\mathrm{RS}} (\mathrm{x} _ {\mathrm{i}}) = \text {Rating} _ {\mathrm{RS}} (\mathrm{x} _ {\mathrm{j}})\right). \end{array}
$$

$$
(3) \left(\text { Rating } _ {\text { MAVM }} (x _ {i}) <   \text { Rating } _ {\text { MAVM }} (x _ {j})\right) \& (\text { Rating } _ {\text { RS }} (x _ {i}) <   \text { Rating } _ {\text { RS }} (x _ {j})).
$$

Furthermore, the framework to analyze the consistency between RS

![](/api/attachments/S8YESPC6/fulltext/images/7e0cc3321d0d738d54c3c89292289da9b944b12d9033f91bab0c5578d4cf4994.jpg)  
Fig. 1. Framework to analyze the consistency between RS and MAVM.

and MAVM is presented in Fig. 1.

The detailed procedures for the consistency analysis between RS and MAVM at the ranking and rating levels are presented below:

Step 1: Provide the PSs of alternatives associated with attributes (or raters).

Step 2: In the case of the MAVM, PSs are aggregated into the values of alternatives based on Eq. (3).

Step 3: In the case of the RS, PSs are transformed into ratings, and then ratings are aggregated into the overall rating scores of alternatives based on Eq. (4).

Step 4: Derive the ranking and ratings of alternatives based on the obtained values and overall rating scores, and then conduct the consistency analysis between RS and MAVM at the ranking and rating le vels.

## 3. Consistency between RS and MAVM at the ranking and rating levels

In this section, we present the consistency conditions between RS and MAVM at the ranking and rating levels to study the reliability issue of RSs.

First, we present Lemma 1.

Lemma 1. Let $\mathbf { v } _ { 1 } , \mathbf { v } _ { 2 } \in [ 0 , 1 ] , { \mathrm { t } } _ { 1 } =$ rounding $( \Nu \times \Nu _ { 1 } )$ and $\mathbf { t } _ { 2 } =$ rounding $( \Nu \times \Nu _ { 2 } )$ , where $\Nu \geq 1$ is an integer. Then, $\begin{array} { r } { \mathbf { v } _ { 2 } - \mathbf { v } _ { 1 } \in \left( \frac { \mathfrak { t } _ { 2 } - \mathfrak { t } _ { 1 } - 1 } { \textnormal { N } } , \frac { \mathfrak { t } _ { 2 } - \mathfrak { t } _ { 1 } + 1 } { \textnormal { N } } \right) } \end{array}$

The proof of Lemma 1 is provided in Appendix A.

Let x and $x _ { s }$ be any two alternatives in $X = \{ x _ { 1 } , x _ { 2 } , . . . , x _ { n } \}$ , and they are evaluated on multiple attributes (or raters) $A = \{ a _ { 1 } , a _ { 2 } , . . . , a _ { m } \}$ . Let $\nu _ { \eta }$ and $\nu _ { s j }$ denote the PSs of alternatives x and $x _ { s }$ associated with attribute $a _ { j } ,$ respectively. Let $V _ { r }$ and $V _ { s }$ be the values of alternatives $x _ { r }$ and $x _ { s }$ obtained by MAVM, i.e., $V _ { r } = { \Sigma _ { j = 1 } } ^ { m } w _ { j } \nu _ { r j }$ and $V _ { s } = { \Sigma _ { j = 1 } } ^ { m } w _ { j } { \nu _ { s j } } ,$ where $\pmb { w } = \{ w _ { 1 } , w _ { 2 } , . . . , w _ { m } \} ^ { T }$ is the weight vector of attributes. Let $t _ { r j }$ and $t _ { s j }$ denote the rating information of alternatives $x _ { r }$ and $x _ { s }$ associated with attribute $a _ { j }$ transformed from $\nu _ { \eta }$ and $\nu _ { s j } .$ Let $T _ { r }$ and $T _ { s }$ be the overall rating scores of alternatives $x _ { r }$ and $x _ { s }$ obtained by RS, i.e., $T _ { r } = \Sigma _ { j = 1 } { } ^ { m } w _ { j } t _ { r j }$ and $T _ { s } = { \Sigma _ { j = 1 } } ^ { m } w _ { j } t _ { s j }$

## 3.1. Tight bounds on N

Based on Definition 2 and Lemma 1, we present the consistency condition (a tight lower bound) about N between RS and MAVM at the ranking level (see Theorem 1). Notably, a tight lower bound means a maximum lower bound in mathematics.

Theorem 1. When using the $R S \ [ 0 , M ]$ to evaluate any two alternatives $x _ { r }$ and $x _ { s } ,$ we have that

(1) When $V _ { r } - \ V _ { s } \neq 0 ,$ , there are two cases:

(i) for any $\begin{array} { r } { N \ge \frac { 1 } { | V _ { r } - V _ { s } | } , } \end{array}$ , the RS $[ 0 , N ]$ is always consistent with MAVM at the ranking level for alternatives $x _ { r }$ and $x _ { s } .$

(ii) for any $\begin{array} { r } { N < \frac { 1 } { | V _ { r } - V _ { s } | } , } \end{array}$ there exist some cases that the RS $[ 0 , N ]$ is inconsistent with MAVM at the ranking level for alternatives $x _ { r }$ and $x _ { s } .$

(2) When $V _ { r } - V _ { s } = 0 $ , there exist some cases that the $\mathrm { R S } \ [ 0 , M ]$ is inconsistent with MAVM at the ranking level for alternatives $x _ { r }$ and $x _ { s }$ for any $N \in \{ 1 , 2 , . . . \}$

The proof of Theorem 1 is provided in Appendix A.

According to Theorem 1, there exists a critical value of $N ,$ which is determined by ${ \frac { 1 } { | V _ { r } - V _ { s } | } } { \bf i f } \ V _ { r } - \ V _ { s } \neq 0$ . When N is larger than the critical value, the RS $[ \dot { 0 } , \ddot { M } ]$ is consistent with MAVM at the ranking level. Meanwhile, the critical value is tight, and for any $\begin{array} { r } { N < \frac { 1 } { | V _ { r } - V _ { \mathrm { { s } } } | } , } \end{array}$ , there exist some cases that the RS [0, N] is inconsistent with MAVM at the ranking level.

On the other hand, if $V _ { r } - V _ { s } = 0 ,$ , the critical value does not exist, and there exist some cases that the RS $[ 0 , N ]$ is inconsistent with MAVM at the ranking level for any $N \in \{ 1 , 2 , . . . \}$

Next, based on Definition 3 and Lemma 1, we present a tight lower bound on $N ,$ which guarantees the consistency between RS and MAVM at the rating level (see Theorem 2).

Theorem 2. When using the $R S \ [ 0 , M ]$ to evaluate any two alternatives $x _ { r }$ and $x _ { s } ,$ , we have that

(1) When $V _ { r } - \ V _ { s } \neq 0 ,$ , there are two cases:

(i) for any $\begin{array} { r } { N \ge \frac { 2 } { | V _ { r } - V _ { s } | } , } \end{array}$ , the RS $[ 0 , N ]$ is always consistent with MAVM at the rating level for alternatives $x _ { r }$ and $x _ { s } .$

(ii) for any $\begin{array} { r } { N < \frac { 2 } { | V _ { r } - V _ { s } | } , } \end{array}$ there exist some cases that the RS $[ 0 , N ]$ is inconsistent with MAVM at the rating level for alternatives $x _ { r }$ and $x _ { s * }$

(2) When $V _ { r } - V _ { s } = 0 ,$ there exist some cases that the RS $[ 0 , N ]$ is inconsistent with MAVM at the rating level for alternatives $x _ { r }$ and $x _ { s }$ for any $N \in \{ 1 , 2 , \ldots \}$

The proof of Theorem 2 is provided in Appendix A.

According to Theorem $^ { 2 , }$ , if $V _ { r } - V _ { s } \ne 0 ,$ , the tight lower bound on N is $\frac { 2 } { | V _ { r } - V _ { s } | }$ at the rating level, and is twice as large as that at the ranking level.

Theorems 1 and 2 reveal that there exist two tights bounds on the parameter N determined by the value diference of alternatives $( \boldsymbol { \mathrm { i . e . } } ,$ $\vert V _ { r } ~ - ~ V _ { s } \vert )$ : When N is larger than the bounds, there exists the consistency between RS and MAVM at the ranking and rating levels; Otherwise, inconsistent cases may occur.

## 3.2. Tight bounds on overall rating scores

Based on Definition 2 and Lemma 1, we present a tight lower bound on overall rating scores, which guarantees the consistency between RS and MAVM at the ranking level (see Theorem 3).

Theorem 3. When using the $R S \ [ 0 , M ]$ to evaluate any two alternatives $x _ { r }$ and $x _ { s } ,$ we have that

(1) When $\left| T _ { r } \ - \ T _ { s } \right| \ \geq \ 1$ , the RS [0, N] is always consistent with MAVM at the ranking level for alternatives $x _ { r }$ and $x _ { s }$ for any $N \in \{ 1 , 2 ,$ $\cdots ^ { \chi } .$

(2) When $\left| T _ { r } - T _ { s } \right| \ < \ 1$ , there exist some cases that the RS $[ 0 , N ]$ is inconsistent with MAVM at the ranking level for alternatives $x _ { r }$ and $x _ { s }$ for any $N \in \{ 1 , 2 , . . . \}$

The proof of Theorem 3 is provided in Appendix A.

According to Theorem 3, there exists a critical value of 1. When $\left| T _ { r } \mathrm { ~ - ~ } T _ { s } \right| \geq 1$ , the RS [0, N] is consistent with MAVM at the ranking level. Meanwhile, the critical value is tight, and when $\left| T _ { r } \mathrm { ~ - ~ } T _ { s } \right| \mathrm { ~ < ~ } 1 _ { : }$ there exist some cases that the RS $[ 0 , N ]$ is inconsistent with MAVM at the ranking level.

Now, based on Definition 3 and Lemma $^ { 1 , }$ we present the consistency condition about overall rating scores between RS and MAVM at the rating level (see Theorem 4).

Theorem 4. When using the RS [0, N] to evaluate any two alternatives $x _ { r }$ and $x _ { s } ,$ we have that

(1) When $\left| T _ { r } \ - \ T _ { s } \right| \ \geq \ 2$ , the RS [0, N] is always consistent with MAVM at the rating level for alternatives x and $x _ { s }$ for any $N \in \{ 1 , 2 , \ldots \}$

(2) When $\left| T _ { r } - T _ { s } \right| < 2 ,$ there exist some cases that the RS $[ 0 , N ]$ is inconsistent with MAVM at the rating level for alternatives $x _ { r }$ and $x _ { s }$ for any $N \in \{ 1 , 2 , . . . \}$

The proof of Theorem 4 is provided in Appendix A.

According to Theorem 4, the tight lower bound on overall rating scores is 2 at the rating level, and is twice as large as that at the ranking level.

Theorems 3 and 4 present two tights bounds determined by overall rating score diference of alternatives $( \mathrm { i . e . , ~ } | T _ { r } \ - \ T _ { s } | )$ ):There are consistent outcomes between RS and MAVM at the ranking level when $\left| T _ { r } \mathrm { ~ - ~ } T _ { s } \right| \geq 1$ , and at the rating level when $\left| T _ { r } \mathrm { ~ - ~ } T _ { s } \right| \geq 2$

Although the tight bounds of the parameter N and overall rating scores are both useful to present theoretical insights about the reliability of RSs, there are some key diferences between them: The tight bounds on the parameter N are determined by the value diference of alternatives, and in practical RS problems we often don't know the values of alternatives, which limits its practical use. Instead, the tight bounds on overall rating scores depend directly on the rating information (not PSs), and thus provide a more practical tool to analyze the reliability of RSs. For example, an RS platform can directly judge whether the obtained RS results are reliable according to the data of $T _ { r }$ and $T _ { s }$ (see Section 4.2).

## 4. Simulation analysis and illustrative examples

In this section, we design simulation experiments to further explore the reliability of RSs. Moreover, we present a hypothetical example of application to illustrate the usability of the obtained results in practical RS problems.

## 4.1. Simulation analysis

The consistency conditions obtained analytically in Theorems 1-4 provide a basis to support the reliability analysis of RSs. But it is still unclear that:

(1) how the value diference of alternatives will influence the consistency between RS and MAVM when N is smaller than the critical values obtained in Theorems 1 and 2;

(2) how the overall rating score diference of alternatives will influence the consistency between RS and MAVM when the diference is smaller than the critical values obtained in Theorems 3 and 4.

Therefore, in this section, given a pair of alternatives $( x _ { 1 }$ and $x _ { 2 } )$ and m attributes (raters), we use simulation experiments to further study the impact of the value diference and overall rating score diference of two alternatives on the consistency between RS and MAVM.

In Simulation experiment 1 we randomly generate $V _ { 1 }$ and $V _ { 2 }$ to satisfy $\begin{array} { r } { | V _ { 1 } - V _ { 2 } | \in \left[ \frac { r - 0 . 1 } { N } , \frac { r } { N } \right) } \end{array}$ when setting $r \in \{ 0 . 1 , 0 . 2 , . . . , 1 \}$ . Clearly, smaller r values show smaller diferences between $V _ { 1 }$ and $V _ { 2 } ,$ and according to Theorem 1 the inconsistency between the RS $[ 0 , N ]$ and MAVM may occur at the ranking level for any $r \in \{ 0 . 1 , 0 . 2 , . . . , 1 \}$ }. Thus, in Simulation experiment 1 we study the impact of diferent $| V _ { 1 } \ - \ V _ { 2 } |$ values on the inconsistency between RS and MAVM at the ranking level, by exploring the average inconsistency ratios under diferent r values.

Meanwhile, we present a revised version of Simulation experiment $^ { 1 , }$ called Simulation experiment 1′, to randomly generate $V _ { 1 }$ and $V _ { 2 }$ to satisfy $\begin{array} { r } { | V _ { 1 } - V _ { 2 } | \in \bigg \lceil \frac { 2 ( r ^ { \prime } - 0 . 1 ) } { N } , \frac { 2 r ^ { \prime } } { N } \bigg \rceil } \end{array}$ when setting $r ^ { \prime } \in \{ 0 . 1 , 0 . 2 , . . . , 1 \}$ , and then to show the average inconsistency ratios under diferent $r ^ { \prime }$ values at the rating level.

The details of Simulation experiments 1 and 1′ are provided in Appendix B.

We set diferent input parameters $N ,$ m, r and $^ { r , }$ and run Simulation experiments 1 and $1 ^ { \prime } 1 0 { , } 0 0 0$ times to obtain the average values of α and $\alpha ^ { \prime } ,$ which reflect the average inconsistency ratios of decision outcomes between RS [0,N] and MAVM at the ranking and rating levels, respectively. The average values of α and $\alpha ^ { \prime }$ are presented in Fig. 2.

From Fig. 2, we find the following observations:

$\mathbf { ( i ) } \mathbb { F } \mathrm { { i g . } \ 2 \ \mathbf { ( a ) } }$ and ${ \mathrm { F i g . ~ 2 ~ } } ( \mathbf { b } )$ show that the inconsistency ratios (average α and $\alpha ^ { \prime }$ values) will be close to $0 { \mathrm { ~ i f ~ } } r > 0 . 5$ and $r ^ { \prime } ~ > ~ 0 . 7 .$ The observation shows that there is still a quite high ratio of keeping consistency (close to 1) between RS and MAVM at the ranking and rating levels when the critical values obtained in Theorems 1 and 2 are reduced to certain degree. This finding indicates that a smaller N can keep the RS reliable in the vast majority of cases.

(ii) Fig. 2 (a) shows that increasing the values of r will result in decreasing the average α values under diferent N and m values. This means that a larger diference between $V _ { 1 }$ and $V _ { 2 }$ will lead to a smaller inconsistency ratio at the ranking level, and thus lead to higher relia: bility of RSs.

(iii) Fig. 2 (b) shows that a larger diference between $V _ { 1 }$ and $V _ { 2 }$ will lead to a smaller inconsistency ratio at the rating level, and thus lead to higher reliability of RSs when $r ^ { \prime } \ge 0 . 4$ . However, when $r ^ { \prime } \le 0 . 3 , \mathrm { F i g } . 2$ (b) shows lower average values of $\alpha ^ { \prime }$ under diferent N and m values as the decrease of $r \mathrm { . }$ This means that a very small diference between $V _ { 1 }$ and $V _ { 2 }$ will lead to a small inconsistency ratio at the rating level, and thus lead to high reliability of RSs. This observation is very diferent from the results at the ranking level, and can be explained as follows:

The $| V _ { 1 } - V _ { 2 } |$ value is small when $r ^ { \prime } \leq 0 . 3 ,$ , and thus the diference between $T _ { 1 }$ and $T _ { 2 }$ is small too. As a result, there is a high possibility that $: a t i n g _ { M A V M } ( x _ { 1 } ) = R a t i n g _ { M A V M } ( x _ { 2 } ) = R a t i n g _ { R S } ( x _ { 1 } ) = R a t i n g _ { R S } ( x _ { 2 } ) _ { \mid }$ which leads to high reliability of RSs at the rating level.

In Simulation experiment 2 we randomly generate $T _ { 1 }$ and $T _ { 2 }$ to satisfy $\left| T _ { 1 } \textrm { -- } T _ { 2 } \right| \in [ \theta \textrm { -- } 0 . 2 , \theta )$ when setting $\theta \in \{ 0 . 2 , 0 . 4 , . . . , 1 \}$ Clearly, smaller θ values show smaller diferences between $T _ { 1 }$ and $T _ { 2 } ,$ and according to Theorem 3 the inconsistency between the RS [0,N] and MAVM may occur at the ranking level for any $\theta \in \{ 0 . 2 , 0 . 4 , . . . , 1 \}$ Thus, in Simulation experiment 2 we study the impact of diferent $| T _ { 1 } ~ - ~ T _ { 2 } |$ values on the inconsistency between RS and MAVM at the ranking level, by exploring the average inconsistency ratios under different θ values.

Meanwhile, we present a revised version of Simulation experiment $^ { 2 , }$ called Simulation experiment $^ { 2 ^ { \prime } , }$ to randomly generate $T _ { 1 }$ and $T _ { 2 }$ to satisfy $| T _ { 1 } - T _ { 2 } | \in 2 [ \theta ^ { \prime } - 0 . 2 , \theta ^ { \prime } )$ ) when setting $\theta ^ { \prime } \in \{ 0 . 2 , 0 . 4 , . . . , 1 \}$ , and then to show the average inconsistency ratios under diferent $\theta ^ { \prime }$ values at the rating level.

The details of Simulation experiments 2 and $2 ^ { \prime }$ are provided in Appendix B.

We set diferent input parameters $N , m , \theta$ and $\theta ^ { \prime } ,$ , and run Simulation experiments 2 and 2′ 10,000 times to obtain the average values of $\mathrm { ~  ~ \cdot ~ } _ { \beta }$ and $\beta ^ { \prime } ,$ which reflect the average inconsistency ratios of decision outcomes between the RS [0,N] and MAVM at the ranking and rating levels, re spectively. The average values of $\beta$ and $\beta ^ { \prime }$ are presented in Fig. 3.

![](/api/attachments/S8YESPC6/fulltext/images/da247bcee4e9b62d0e8476d64dd6ccca0e18dad866d670289ca981a391cab22d.jpg)  
(a)

![](/api/attachments/S8YESPC6/fulltext/images/a32b73133a30b27eb52b88fdf25ba7a8fdd544c38d27ad4f3d7ad6447a708cd9.jpg)  
(b)

Fig. 2. The average α and α′ values in Simulation experiments 1 and 1′.  
![](/api/attachments/S8YESPC6/fulltext/images/ded700fba7e79c3bccccc67b22c25770bfd832aeb03a8c4bb4d23aeebe99e121.jpg)

![](/api/attachments/S8YESPC6/fulltext/images/354d05d46e6e1dbe19c969c3eaa40c658826b2052aeae32e7b2fc9bae9208f84.jpg)  
(a)  
(b)  
Fig. 3. The average β and β′ values in Simulation experiments 2 and 2′.

From Fig. 3, we have the following findings:

(i) Fig. 3 (a) and Fig. 3 (b) show that increasing the values of θ and $\theta ^ { \prime }$ will result in decreasing the average $\beta$ and $\beta ^ { \prime }$ values under diferent N and m values. This means that a larger diference between $T _ { 1 }$ and $T _ { 2 }$ will lead to a smaller inconsistency ratio at the ranking and rating le vels, and thus lead to higher reliability of RSs.

(ii) Fig. 3 (a) shows that the inconsistency ratio will be close to 0 if $\theta \geq 0 . 4$ . This observation shows that there is still a quite high ratio of keeping consistency (close to 1) between RS and MAVM at the ranking level when $\left| T _ { 1 } \ - \ T _ { 2 } \right| \ \ge \ 0 . 4 .$ . It indicates we can use a smaller critical value (e.g., 0.4) to guarantee the consistency between RS and MAVM at the ranking level. Similarly, Fig. 3 (b) shows that we can use a smaller critical value (e.g., 1.6) to guarantee the reliability of RSs at the rating level in the majority of cases.

As complementary to Theorems 1-4, the results in Simulation experiments 1, 1′, 2 and 2′ can further provide useful suggestions to im prove the decision making reliability in RSs.

(1) Quite high reliability can still be kept at the ranking and rating levels when the obtained critical values in Theorems 1-4 are reduced to certain degree.

(2) The values and overall rating scores of alternatives play important roles in the reliability of RSs. A large value diference or overall rating score diference of alternatives will lead to a low inconsistency ratio at the ranking level, and thus lead to higher reliability of RSs. When considering the rating level, a middle value diference of alternatives will result in a high inconsistency ratio, while a large overall rating score diference of alternatives will lead to a low inconsistency ratio.

Table 1  
PSs and the tight bounds of N at the ranking level

<table><tr><td rowspan="2"></td><td colspan="5"> $x_1$ </td><td colspan="5"> $x_2$ </td><td rowspan="2">Tight bounds at the ranking level (N)</td></tr><tr><td> $a_1$ </td><td> $a_2$ </td><td> $a_3$ </td><td> $a_4$ </td><td> $a_5$ </td><td> $a_1$ </td><td> $a_2$ </td><td> $a_3$ </td><td> $a_4$ </td><td> $a_5$ </td></tr><tr><td>Consumer 1</td><td>0.85</td><td>0.86</td><td>0.85</td><td>0.87</td><td>0.78</td><td>0.63</td><td>0.67</td><td>0.99</td><td>0.73</td><td>0.61</td><td>8.62</td></tr><tr><td>Consumer 2</td><td>0.70</td><td>0.86</td><td>0.84</td><td>0.73</td><td>0.90</td><td>0.76</td><td>0.95</td><td>0.79</td><td>0.64</td><td>0.64</td><td>20</td></tr><tr><td>Consumer 3</td><td>0.86</td><td>0.88</td><td>0.61</td><td>1.00</td><td>0.74</td><td>0.65</td><td>0.85</td><td>0.92</td><td>0.77</td><td>0.62</td><td>17.86</td></tr><tr><td>Consumer 4</td><td>0.99</td><td>0.87</td><td>0.77</td><td>0.79</td><td>0.77</td><td>0.92</td><td>0.94</td><td>0.88</td><td>0.93</td><td>0.95</td><td>11.63</td></tr><tr><td>Consumer 5</td><td>0.76</td><td>0.60</td><td>0.75</td><td>0.83</td><td>0.64</td><td>0.91</td><td>0.63</td><td>0.66</td><td>0.91</td><td>0.73</td><td>19.23</td></tr><tr><td>Consumer 6</td><td>0.85</td><td>0.93</td><td>0.70</td><td>0.91</td><td>0.92</td><td>0.82</td><td>0.75</td><td>0.84</td><td>0.82</td><td>0.72</td><td>13.89</td></tr><tr><td>Consumer 7</td><td>0.83</td><td>0.64</td><td>0.85</td><td>0.77</td><td>0.76</td><td>0.92</td><td>0.60</td><td>0.83</td><td>0.99</td><td>1.00</td><td>10.20</td></tr><tr><td>Consumer 8</td><td>0.98</td><td>0.82</td><td>0.87</td><td>0.92</td><td>0.86</td><td>0.63</td><td>0.93</td><td>0.88</td><td>0.71</td><td>0.71</td><td>8.47</td></tr><tr><td>Consumer 9</td><td>0.62</td><td>0.99</td><td>0.92</td><td>0.98</td><td>0.80</td><td>0.88</td><td>0.64</td><td>0.64</td><td>0.73</td><td>0.88</td><td>9.26</td></tr><tr><td>Consumer 10</td><td>0.87</td><td>0.92</td><td>0.86</td><td>0.92</td><td>0.88</td><td>0.68</td><td>0.65</td><td>0.71</td><td>0.73</td><td>0.76</td><td>5.43</td></tr></table>

## 4.2. Hypothetical application

In the following, we present a hypothetical example of application to illustrate the usability of the theoretical and simulation results. Suppose there are two cafes $( x _ { 1 }$ and $x _ { 2 } )$ in a university campus. A team of marketing students conducts a consumer preference survey, and consumers (University staf and students) are invited to evaluate these two cafes from five attributes: Location $\left( a _ { 1 } \right)$ , Product quality $( a _ { 2 } ) ,$ Atmosphere $\left( a _ { 3 } \right)$ , Waiting time $( a _ { 4 } )$ and Space available $\left( a _ { 5 } \right) .$ . In the example the weights of the attributes are equal. Here we only illustrate the usability of Theorems 1 and $^ { 3 , }$ and the cases of Theorems 2 and 4 are similar.

In Case $\mathrm { A } ,$ we illustrate the results of Theorem 1 and Simulation experiment 1.

Case A. Consumers are asked to provide their PSs of the two cafes over the five attributes, and the PSs are presented in Table 1.

It is assumed that the consumers will provide their rating informa tion through the transformation of PSs (i.e., Eqs. (1) and (2)) based on the rationality principle. Then, based on Theorem 1 we can obtain the tight bounds of N (see Table 1) to check the consistency between MAVM and RS at the ranking level, which measures the reliability of the RSs used by consumers. In the example, when the consumers use the RS with $N \geq 2 0$ , the 10 consumers' evaluation results about the ranking of the two cafes are all reliable in the sense of MAVM.

Further, let CR be the proportion of the consumers who have consistent evaluations between MAVM and RS at the ranking level. Clearly, $C R \in [ 0 , 1 ]$ . The larger the value of CR, the higher proportion of consumers whose evaluation results are reliable. If $C R = 1$ , all consumers evaluation results are reliable. The CR values under diferent parameter N are present in Fig. 4.

According to Fig. 4, a high consistency proportion can still be kept when N = 8 even though most of the tight bounds on N are larger than 8 (See Table 1). This result indicates that there still exists high relia bility in most cases when the tight bound on N at the ranking level is obviously reduced, which coincides with Simulation experiment 1.

Further, we use case B to illustrate the results of Theorem 3 and Simulation experiment 2.

Case B. In practical RS problems, we often don't know people's PSs, and Theorem 3 provides a useful tool to determine whether the consistency exists between MAVM and RS at the ranking level (i.e., the reliability of the RS can be guaranteed). Suppose ten consumers are asked to rate the two cafes using the RS [0, 6]. Table 2 shows the rating information and the corresponding overall rating score diferences.

Theorem 3 shows that $\left| T _ { 1 } \mathrm { ~ - ~ } T _ { 2 } \right| \geq 1$ can guarantee the consistency between MAVM and RS at the ranking level, and Simulation 2 indicates that there is still a high possibility to keep the consistency when $\left| T _ { 1 } \ - \ T _ { 2 } \right| \ \ge \ 0 . 4$ . The results in Table 2 coincide with Theorem 3 and

![](/api/attachments/S8YESPC6/fulltext/images/fe3bdb73f8b5e2592efd2ceb52da00238f902bca957387f313a141f1ee6e35a4.jpg)  
Fig. 4. The CR values under diferent parameter N.

Simulation 2. In summary, both the theoretical results and simulation results are validated in the hypothetical application.

## 5. Conclusion

RSs are widely used to obtain the ranking or ratings of alternatives in decision making, and one of the most challenging issues in RS problems is reliability because diferent RSs may lead to inconsistent decision outcomes. In this paper, we use MAVM as a benchmark to study the reliability of the RS [0, N]. Diferent from the existing research to investigate the impact of people's psychological and behavioral factors on the reliability of RSs, in this paper we analytically reveal the mechanism from the view of the rounding process to guarantee the reliability of RSs at the ranking and rating levels. The main contributions are concluded as follows:

(1) We find that there exist tight bounds on the parameter N, which are determined by the value diference of alternatives (see Theorems 1 and 2). When N is larger than the bounds, the consistency between RS and MAVM will hold at the ranking and rating levels; Otherwise, inconsistent cases may occur. Particularly, the tight bound on N at the rating level is twice as large as that at the ranking level.

(2) We present the tight bounds on overall rating scores (see Theorems 3 and 4): The consistency between RS and MAVM will hold when the overall rating score diference among alternatives is larger than 1 at the ranking level and larger than 2 at the rating level.

(3) We develop the detailed simulation analysis to show that the consistency between RS and MAVM at the ranking and rating levels can still be kept in most cases if the obtained tight bounds are reduced to certain degree. These simulation results further provide useful sugges tions to improve the decision making reliability in RSs.

Table 2  
The ratings with the RS [0, 6] and the corresponding overall rating score diferences

<table><tr><td rowspan="2"></td><td colspan="5"> $x_1$ </td><td colspan="5"> $x_2$ </td><td rowspan="2"> $|T_1 - T_2|$ </td><td rowspan="2">Consistency at the ranking level</td></tr><tr><td> $a_1$ </td><td> $a_2$ </td><td> $a_3$ </td><td> $a_4$ </td><td> $a_5$ </td><td> $a_1$ </td><td> $a_2$ </td><td> $a_3$ </td><td> $a_4$ </td><td> $a_5$ </td></tr><tr><td>Consumer 1</td><td>5</td><td>5</td><td>5</td><td>5</td><td>5</td><td>4</td><td>4</td><td>6</td><td>4</td><td>4</td><td>0.6</td><td>Yes</td></tr><tr><td>Consumer 2</td><td>4</td><td>5</td><td>5</td><td>4</td><td>5</td><td>5</td><td>6</td><td>5</td><td>4</td><td>4</td><td>0.2</td><td>No</td></tr><tr><td>Consumer 3</td><td>5</td><td>5</td><td>4</td><td>6</td><td>4</td><td>4</td><td>5</td><td>6</td><td>5</td><td>4</td><td>0</td><td>No</td></tr><tr><td>Consumer 4</td><td>6</td><td>5</td><td>5</td><td>5</td><td>5</td><td>6</td><td>6</td><td>5</td><td>6</td><td>6</td><td>0.6</td><td>Yes</td></tr><tr><td>Consumer 5</td><td>5</td><td>4</td><td>5</td><td>5</td><td>4</td><td>5</td><td>4</td><td>4</td><td>5</td><td>4</td><td>0.2</td><td>No</td></tr><tr><td>Consumer 6</td><td>5</td><td>6</td><td>4</td><td>5</td><td>6</td><td>5</td><td>5</td><td>5</td><td>5</td><td>4</td><td>0.4</td><td>Yes</td></tr><tr><td>Consumer 7</td><td>5</td><td>4</td><td>5</td><td>5</td><td>5</td><td>6</td><td>4</td><td>5</td><td>6</td><td>6</td><td>0.6</td><td>Yes</td></tr><tr><td>Consumer 8</td><td>6</td><td>5</td><td>5</td><td>6</td><td>5</td><td>4</td><td>6</td><td>5</td><td>4</td><td>4</td><td>0.8</td><td>Yes</td></tr><tr><td>Consumer 9</td><td>4</td><td>6</td><td>6</td><td>6</td><td>5</td><td>5</td><td>4</td><td>4</td><td>4</td><td>5</td><td>1</td><td>Yes</td></tr><tr><td>Consumer 10</td><td>5</td><td>6</td><td>5</td><td>6</td><td>5</td><td>4</td><td>4</td><td>4</td><td>4</td><td>5</td><td>1.2</td><td>Yes</td></tr></table>

The tight bounds on the parameter N and overall rating scores both provide interesting insights about the reliability of RSs in theoretical aspects, but they behave diferently in practical RS problems: We can't directly use the tight bounds of the parameter N to judge the reliability of the used RSs because we often don't know the values of alternatives (i.e., people's PSs) when using an RS. However, the tight bounds on overall rating scores depend directly on the rating information (not PSs), and thus provide more practical tools to analyze the reliability of RSs.

There are two limitations in this paper: (1) strategic behaviors are common in decision making activities $[ 1 5 , 2 3 , 4 0 , 4 3 ]$ , but we assume that the decision makers honestly express their preferences using RSs; (2) the rating scores mean diferent things (the personalized individual semantics [51]) to diferent decision makers, but we don't consider this issue in RSs. Therefore, it will be interesting to study the reliability of RSs in a decision context with strategic behaviors and personalized individual semantics.

## Acknowledgments

This work was supported by the grant (No. 71871149) from NSF of China, and the grants (Nos. sksyl201705 and 2018hhs-58 and LH2018004) from Sichuan University.

## Appendix A. Proofs

The proof of Lemma 1:

Let $\nu _ { 1 } \in [ 0 , 1 ]$ and $\nu _ { 2 } \in [ 0 , 1 ]$ . Transform them into the interval [0, N] via Eqs. (1) and (2), we have $t _ { 1 } = r o u n d i n g ( N \times \nu _ { 1 } )$ and $t _ { 2 } =$ rounding $( N \times \nu _ { 2 } )$ . Then, we have:

$$
v _ {2} - v _ {1} \in \left\{ \begin{array}{l l} \bigg (\frac {t _ {2} - t _ {1} - 1}{N}, \frac {t _ {2} - t _ {1} + 1}{N} \bigg), & t _ {2} - t _ {1} \geq 2 \\ \bigg (0, \frac {2}{N} \bigg), & t _ {2} - t _ {1} = 1 \\ \bigg (- \frac {1}{N}, \frac {1}{N} \bigg), & t _ {2} - t _ {1} = 0 \\ \bigg (- \frac {2}{N}, 0 \bigg), & t _ {2} - t _ {1} = - 1 \\ \bigg (\frac {t _ {2} - t _ {1} - 1}{N}, \frac {t _ {2} - t _ {1} + 1}{N} \bigg), & t _ {2} - t _ {1} \leq - 2. \end{array} \right.\tag{5}
$$

Based on Eq. (5), we have $\begin{array} { r } { v _ { 2 } - v _ { 1 } \in \left( \frac { t _ { 2 } - t _ { 1 } - 1 } { N } , \frac { t _ { 2 } - t _ { 1 } + 1 } { N } \right) } \end{array}$

This completes the proof of Lemma 1.

The proof of Theorem 1:

(1) We prove (i) based on reduction to absurdity as follows.

We assume $V _ { r } ~ > ~ V _ { s } , \mathrm { i . e . }$ ., Ranking (x ) < Ranking (x ). Based on Lemma 1, we have:

$$
\begin{array}{r} V _ {r} - V _ {s} = w _ {1} (v _ {r 1} - v _ {s 1}) + \ldots + w _ {i} (v _ {r i} - v _ {s i}) + \ldots + w _ {m} (v _ {r m} - v _ {s m}) <   \frac {1}{N} (w _ {1} (t _ {r 1} - t _ {s 1} + 1) + \ldots + w _ {i} (t _ {r i} - t _ {s i} + 1) + \ldots + w _ {m} (t _ {r m} - t _ {s m} + 1)) \\ = \frac {1}{N} (w _ {1} (t _ {r 1} - t _ {s 1}) + \ldots + w _ {i} (t _ {r i} - t _ {s i}) + \ldots + w _ {m} (t _ {r m} - t _ {s m}) + (w _ {1} + \ldots + w _ {i} + \ldots + w _ {m})) = \frac {1}{N} (T _ {r} - T _ {s} + (w _ {1} + \ldots + w _ {i} + \ldots + w _ {m})) \end{array}\tag{6}
$$

If the inconsistency occurs at the ranking level, we have ${ \cal R } a n k i n g _ { R S } ( x _ { r } ) \ : \geq \ : { \cal R } a n k i n g _ { R S } ( x _ { s } ) , \mathrm { i . e . , } \ : T _ { r } \leq T _ { s }$ according to Definition 2. As a result, based on [6] we have

$$
V _ {r} - V _ {s} <   \frac {1}{N} (w _ {1} + \ldots + w _ {i} + \ldots + w _ {m}) = \frac {1}{N}.\tag{7}
$$

Then, we have that $\begin{array} { r } { 0 < V _ { r } - V _ { s } < \frac { 1 } { N } , \mathrm { i . e . , } N < \frac { 1 } { V _ { r } - V _ { s } } , } \end{array}$ , which contradicts $\begin{array} { r } { N \ge \frac { 1 } { \mid V _ { r } - V _ { s } \mid } } \end{array}$ . Notably, we can prove (i) in the case of $V _ { r } ~ < ~ V _ { s }$ in the same way.

$$
\mathrm{So},
$$

$$
[ 0, N ]
$$

$$
x _ {r}
$$

$$
x _ {s} \text {   if   } N \geq \frac {1}{| V _ {r} - V _ {s} |} (V _ {r} - V _ {s} \neq 0).
$$

Next we prove (ii). We assume $V _ { r } - V _ { s } > 0$ , i.e., Ran $k i n g _ { M A V M } ( x _ { r } ) \ < \ R a n k i n g _ { M A V M } ( x _ { s } )$ . Because $N < \frac { 1 } { \mid V _ { r } - V _ { s } \mid } ,$ we have that

$$
N <   \frac {1}{V _ {r} - V _ {s}} = \frac {1}{w _ {1} (v _ {r 1} - v _ {s 1}) + . . . + w _ {i} (v _ {r i} - v _ {s i}) + . . . + w _ {m} (v _ {r m} - v _ {s m})}.\tag{8}
$$

Then, for any $N < \frac { 1 } { w _ { 1 } ( \nu _ { r 1 } - \nu _ { s 1 } ) + \ldots + w _ { i } ( \nu _ { r i } - \nu _ { s i } ) + \ldots + w _ { m } ( \nu _ { r m } - \nu _ { s m } ) } ,$ there exist $\nu _ { r i } , \nu _ { s i } ( i = 1 , 2 , . . . , m )$ satisfying Eq. (9).

$$
\left\{ \begin{array}{c} v _ {r i} - v _ {s i} = \frac {1}{2 N} \\ \text {rounding} (N \times v _ {r i}) = \text {rounding} (N \times v _ {s i}). \end{array} \right.\tag{9}
$$

Thus, we have t − t = rounding(N × v ) − rounding( ${ N \times \nu _ { s i } } ) = 0 ( i = 1 , 2 , . . . , m )$ and $T _ { r } = T _ { s } ,$ , i.e., Rankin $\smash { \xi _ { R S } ( x _ { r } ) = R a n k i n g _ { R S } ( x _ { s } ) }$ . As a result, the inconsistency between the RS [0,N] and MAVM occurs at the ranking level accoding to Definition 2. Notably, we can prove (ii) in the case of $V _ { r } ~ < ~ V _ { s }$ in the same way.

Therefore, for any $\begin{array} { r } { \dot { N ^ { < } } \frac { 1 } { \mid V _ { r } - V _ { s } \mid } ( V _ { r } - V _ { s } \neq 0 ) } \end{array}$ , there exist some inconsistency cases between the RS [0,N] and MAVM at the ranking level for alternatives $x _ { r }$ and $x _ { s } .$

This completes the proof of (ii).

(2) When $V _ { r } - V _ { s } = 0 , \mathrm { i . e . , } R a n k i n g _ { M A V M } ( x _ { r } ) = R a n k i n g _ { M A V M } ( x _ { s } ) ,$ we have:

$$
V _ {r} - V _ {s} = w _ {1} (v _ {r 1} - v _ {s 1}) + \ldots + w _ {i} (v _ {r i} - v _ {s i}) + \ldots + w _ {m} (v _ {r m} - v _ {s m}) = 0.\tag{10}
$$

For any $N \in \{ 1 , 2 , . . . \}$ , we set $\begin{array} { r } { w _ { i } = \frac { 1 } { m } ( i = 1 , 2 , . . . , m ) } \end{array}$ , and there exist $\nu _ { r i } , \nu _ { s i } ( i = 1 , 2 , . . . , m )$ satisfying Eq. (11).

$$
\left\{ \begin{array}{c} (v _ {r i} - v _ {s i}) \to 0, (t _ {r i} - t _ {s i}) = - 1, i = 1, 2,..., m - 1 \\ (v _ {r m} - v _ {s m}) \to 0, (t _ {r m} - t _ {s m}) = 0 \\ w _ {1} (v _ {r 1} - v _ {s 1}) +... + w _ {i} (v _ {r i} - v _ {s i}) +... + w _ {m} (v _ {r m} - v _ {s m}) = 0. \end{array} \right.\tag{11}
$$

Then, in this case $T _ { r } ~ < ~ T _ { s } , \mathrm { i . e . , } R a n k i n g _ { R S } ( x _ { r } ) ~ > ~ R a n k i n g _ { R S } ( x _ { s } )$ . As a result, the inconsistency between the RS [0, N] and MAVM occurs at the ranking level accoding to Definition 2.

So, for any $N \in \{ 1 , 2 , . . . \}$ , there exist some inconsistency cases between the RS [0,N] and MAVM at the ranking level for alternatives $x _ { r }$ and $x _ { s }$ when $V _ { r } - \ V _ { s } = 0$

This completes the proof of (2).

The proof of Theorem 2:

(1) We prove (i) based on reduction to absurdity as follows.

We assume $V _ { r } > V _ { s } , \mathrm { i . e . , } R a t i n g _ { M A V M } ( x _ { r } ) \geq R a t i n g _ { M A V M } ( x _ { s } )$ . Based on Lemma 1, we have Eq. (6), i.e., $\begin{array} { r } { V _ { r } - V _ { s } < \frac { 1 } { N } ( T _ { r } - T _ { s } + w _ { 1 } + . . . + w _ { i } + . . . + w _ { m } ) } \end{array}$ If the inconsistency occurs at the rating level, we have

(a) $R a t i n g _ { M A V M } ( x _ { r } ) ~ > ~ R a t i n g _ { M A V M } ( x _ { s } )$ and $R a t i n g _ { R S } ( x _ { r } ) \ < \ R a t i n g _ { R S } ( x _ { s } ) ( T _ { r } \ < \ T _ { s } )$ . As a result, based on Eq. (6) we have

$$
V _ {r} - V _ {s} <   \frac {1}{N} (w _ {1} + \ldots + w _ {i} + \ldots + w _ {m}) = \frac {1}{N}.\tag{12}
$$

(b) Rating (x ) > Rating (x ) and Rating (x ) = Rating (x )(| T − T | < 1). As a result, based on Eq. (6) we have

$$
V _ {r} - V _ {s} <   \frac {1}{N} (1 + w _ {1} + \ldots + w _ {i} + \ldots + w _ {m}) = \frac {2}{N}.\tag{13}
$$

$( \mathbf { c } ) R a t i n g _ { M A V M } ( x _ { r } ) = R a t i n g _ { M A V M } ( x _ { s } ) ( \mid V _ { r } - V _ { s } \mid < \frac { 1 } { N } )$ , then we have that

$$
N <   \frac {1}{| V _ {r} - V _ {s} |} = \frac {1}{| w _ {1} (v _ {r 1} - v _ {s 1}) + . . . + w _ {i} (v _ {r i} - v _ {s i}) + . . . + w _ {m} (v _ {r m} - v _ {s m}) |}.\tag{14}
$$

For any < N + … + + … +w v v w v v w v v<sup>1</sup>( ) ( ) ( ) there exist $\nu _ { r i } , \nu _ { s i } ( i = 1 , 2 , . . . , m )$ satisfying Eq. (15).

$$
v _ {r i} - v _ {s i} = \frac {1}{2 N}\tag{15}
$$

Thus, we have t − t = rounding( $N \times \nu _ { r i } ) -$ rounding( ${ N \times \nu _ { s i } } ) = 1 ( i = 1 , 2 , . . . , m )$ and $T _ { r } - T _ { s } = 1 , \mathrm { i . e . } ,$ , Rating (x ) > Rating (x ). As a result, the inconsistency between the RS [0,N] and MAVM occurs at the rating level accoding to Definition 3.

Notably, we can prove (i) in the case of $V _ { r } ~ < ~ V _ { s }$ in the same way.

So, the RS [0, N] is consistent with MAVM at the rating level for alternatives x and x if $\begin{array} { r } { { \bf \nabla } N \ge \frac { 2 } { \mid V _ { r } - V _ { s } \mid } ( V _ { r } - V _ { s } \ne 0 ) , } \end{array}$

Next, we prove (ii). We assume $V _ { r } - V _ { s } > 0 ,$ i.e., Rat $\mathsf { i } n g _ { M A V M } ( x _ { r } ) \geq R a t i n g _ { M A V M } ( x _ { s } )$ . Because $\begin{array} { r } { N < \frac { 2 } { \mid V _ { r } - V _ { s } \mid } , } \end{array}$ we have that

$$
N <   \frac {2}{V _ {r} - V _ {s}} = \frac {2}{w _ {1} (v _ {r 1} - v _ {s 1}) + . . . + w _ {i} (v _ {r i} - v _ {s i}) + . . . + w _ {m} (v _ {r m} - v _ {s m})}.\tag{16}
$$

Then, for any $N < \frac { 2 } { w _ { 1 } ( \nu _ { r 1 } - \nu _ { s 1 } ) + \ldots + w _ { i } ( \nu _ { r i } - \nu _ { s i } ) + \ldots + w _ { m } ( \nu _ { r m } - \nu _ { s m } ) } ,$ we set $\begin{array} { r } { w _ { i } = \frac { 1 } { m } ( i = 1 , 2 , . . . , m ) } \end{array}$ , and there exist $\nu _ { r i } , \nu _ { s i } ( i = 1 , 2 , . . . , m )$ satisfying Eq. (17).

$$
\left\{ \begin{array}{c} (v _ {r i} - v _ {s i}) \to 0, (t _ {r i} - t _ {s i}) = - 1, i = 1, 2,..., m - 1 \\ (v _ {r m} - v _ {s m}) \to \frac {1}{2 N}, (t _ {r m} - t _ {s m}) = 0 \\ w _ {1} (v _ {r 1} - v _ {s 1}) +... + w _ {i} (v _ {r i} - v _ {s i}) +... + w _ {m} (v _ {r m} - v _ {s m}) > 0. \end{array} \right.\tag{17}
$$

Then, in this case $T _ { r } < T _ { s } , \mathrm { i . e . } ,$ , Rati $\smash { \imath g _ { R S } ( x _ { r } ) \leq R a t i n g _ { R S } ( x _ { s } ) }$ , As a result. the inconsistency between the RS $[ 0 , N ]$ and MAVM occurs at the rating level accoding to Definition 3. Notably, we can prove (ii) in the case of $V _ { r } ~ < ~ V _ { s }$ in the same way.

Therefore, for any $\begin{array} { r } { N < \frac { 2 } { \mid V _ { r } - V _ { s } \mid } ( V _ { r } - V _ { s } \neq 0 ) } \end{array}$ , there exist some inconsistency cases between the RS [0,N] and MAVM at the rating level for

alternatives x and x .

This completes the proof of (ii).

(2) When $V _ { r } - \ V _ { s } = 0 ;$ , i.e., Rating<sub>MAVM</sub>(x<sub>r</sub>) = Rating<sub>MAVM</sub>(x<sub>s</sub>), we have:

$$
V _ {r} - V _ {s} = w _ {1} (v _ {r 1} - v _ {s 1}) + \ldots + w _ {i} (v _ {r i} - v _ {s i}) + \ldots + w _ {m} (v _ {r m} - v _ {s m}) = 0.\tag{18}
$$

For any $N \in \{ 1 , 2 , . . . \}$ , we set $\begin{array} { r } { w _ { i } = \frac { 1 } { m } ( i = 1 , 2 , . . . , m ) } \end{array}$ , and there exist $\nu _ { r i } , \nu _ { s i } ( i = 1 , 2 , . . . , m )$ satisfying Eq. (19).

$$
\left\{ \begin{array}{c} (v _ {r i} - v _ {s i}) \to 0, (t _ {r i} - t _ {s i}) = - 1, i = 1, 2,..., m - 1 \\ (v _ {r m} - v _ {s m}) \to 0, (t _ {r m} - t _ {s m}) = 0 \\ w _ {1} (v _ {r 1} - v _ {s 1}) +... + w _ {i} (v _ {r i} - v _ {s i}) +... + w _ {m} (v _ {r m} - v _ {s m}) = 0. \end{array} \right.\tag{19}
$$

Then, in this case $T _ { r } \ < \ T _ { s } , \mathrm { i . e . , } R a t i n g _ { R S } ( x _ { r } ) \nonumber \ \leq R a t i n g _ { R S } ( x _ { s } )$ . As a result, the inconsistency between the RS [0, N] and MAVM occurs at the rating level accoding to Definition 3

So, for any $N \in \left\{ { 1 , 2 , \ldots } \right\}$ , there exist some inconsistency cases between the RS $[ 0 , N ]$ and MAVM at the rating level for alternatives $x _ { r }$ and $x _ { s }$ when $V _ { r } - \ V _ { s } = 0 .$

This completes the proof of (2).

The proof of Theorem 3:

(1) According to Eq. (6), we have $\begin{array} { r } { V _ { r } - V _ { s } < \frac { T _ { r } - T _ { s } + 1 } { N } } \end{array}$ . Similarly, we can obtain that $\begin{array} { r } { V _ { r } - V _ { s } > \frac { T _ { r } - T _ { s } - 1 } { N } . } \end{array}$ , i.e.,

$$
\frac {T _ {r} - T _ {s} - 1}{N} <   V _ {r} - V _ {s} <   \frac {T _ {r} - T _ {s} + 1}{N}.\tag{20}
$$

We first consider the case of $T _ { r } - T _ { s } \geq 1$ . In this case, $R a n k i n g _ { R S } ( x _ { r } ) \ <$ Ranking (x ). Based on Eq. (20), we have $V _ { r } - V _ { s } > 0 , { \mathrm { i . e . } }$ , Ranking<sub>MAVM</sub> $( x _ { r } ) \ : < \ : R a n k i n g _ { M A V M } ( x _ { s } )$ . Thus, for any $N \in \{ 1 , 2 , \ldots \}$ the RS $[ 0 , N ]$ is consistent with MAVM at the ranking level for alternatives $x _ { r }$ and $x _ { s }$ . Notably, we can prove (1) in the case of $T _ { r } - T _ { s } \leq - 1$ in the same way.

(2) We assume $0 \leq T _ { r } - T _ { s } < 1$ , i.e., Ranking (x ) ≤ Ranking (x ), then:

$$
0 \leq T _ {r} - T _ {s} = w _ {1} (t _ {r 1} - t _ {s 1}) +... + w _ {i} (t _ {r i} - t _ {s i}) +... + w _ {m} (t _ {r m} - t _ {s m}) <   1.\tag{21}
$$

For any $N \in \{ 1 , 2 , . . . \}$ , we set $\begin{array} { r } { w _ { i } = \frac { 1 } { m } ( i = 1 , 2 , . . . , m ) . } \end{array}$ , and there exist $\nu _ { r i } , \nu _ { s i } ( i = 1 , 2 , . . . , m )$ satisfying Eq. (22).

$$
\left\{ \begin{array}{c} (v _ {r i} - v _ {s i}) \to 0,   (t _ {r i} - t _ {s i}) = 0,   i = 1, 2,..., m - 1 \\ (v _ {r m} - v _ {s m}) \to 0,   (t _ {r m} - t _ {s m}) = 0 o r 1 \\ w _ {1} (v _ {r 1} - v _ {s 1}) +... + w _ {i} (v _ {r i} - v _ {s i}) +... + w _ {m} (v _ {r m} - v _ {s m}) <   0 \\ 0 \leq w _ {1} (t _ {r 1} - t _ {s 1}) +... + w _ {i} (t _ {r i} - t _ {s i}) +... + w _ {m} (t _ {r m} - t _ {s m}) <   1. \end{array} \right.\tag{22}
$$

Thus, in this case $V _ { r } ~ < ~ V _ { s } , \mathrm { i . e . , } R a n k i n g _ { M A V M } ( x _ { r } ) ~ > ~ R a n k i n g _ { M A V M } ( x _ { s } )$ . As a result, the inconsistency between the RS [0, N] and MAVM occurs at the ranking level accoding to Definition 2. Notably, we can prove (2) in the case of $- 1 ~ < ~ T _ { r } - T _ { s } \le 0$ in the same way.

This completes the proof of (2).

The proof of Theorem 4:

(1) According to Eq. (20), we have

$$
\frac {T _ {r} - T _ {s} - 1}{N} <   V _ {r} - V _ {s} <   \frac {T _ {r} - T _ {s} + 1}{N}.\tag{23}
$$

We first consider the case of $T _ { r } \mathrm { ~ - ~ } T _ { s } \geq 2$ . In this case, $R a t i n g _ { R S } ( x _ { r } ) \ >$ Rating (x ). Based on Eq. (23), we have $\begin{array} { r } { V _ { r } - V _ { s } > \frac { 1 } { N } , } \end{array}$ i.e., Rating<sub>MAVM</sub> $( x _ { r } ) > R a t i n g _ { M A V M } ( x _ { s } )$ . Thus, for any $N \in \{ 1 , 2 , . . . \}$ the RS [0, N] is consistent with MAVM at the rating level for alternatives $x _ { r }$ and $x _ { s } .$ . Notably, we can prove (1) in the case of $T _ { r } - T _ { s } \leq - 2$ in the same way.

This completes the proof of (1).

(2) We assume $0 \leq T _ { r } - T _ { s } < 2 .$ , i.e., Rating (x ) ≥ Rating (x ). Then:

$$
0 \leq T _ {r} - T _ {s} = w _ {1} (t _ {r 1} - t _ {s 1}) + \ldots + w _ {i} (t _ {r i} - t _ {s i}) + \ldots + w _ {m} (t _ {r m} - t _ {s m}) <   2.\tag{24}
$$

For any $N \in \{ 1 , 2 , \ldots \}$ , we set $\begin{array} { r } { w _ { i } = \frac { 1 } { m } ( i = 1 , 2 , . . . , m ) } \end{array}$ , and there exist $\nu _ { r i } , \nu _ { s i } ( i = 1 , 2 , . . . , m )$ satisfying Eq. (25).

$$
\left\{ \begin{array}{c} (v _ {r i} - v _ {s i}) \to - \frac {1}{N}, (t _ {r i} - t _ {s i}) = 0,   i = 1,   2,..., m - 1 \\ (v _ {r m} - v _ {s m}) \to 0,   (t _ {r m} - t _ {s m}) = 0 o r 1 \\ w _ {1} (v _ {r 1} - v _ {s 1}) +... + w _ {i} (v _ {r i} - v _ {s i}) +... + w _ {m} (v _ {r m} - v _ {s m}) <   0 \\ 0 \leq w _ {1} (t _ {r 1} - t _ {s 1}) +... + w _ {i} (t _ {r i} - t _ {s i}) +... + w _ {m} (t _ {r m} - t _ {s m}) <   2. \end{array} \right.\tag{25}
$$

Thus, in this case, $V _ { r } < V _ { s } \mathrm { i } . e .$ , Rating (x ) ≤ Rating (x ). As a result, the inconsistency between the RS [0, N] and MAVM occurs at the rating level accoding to Definition 3. Notably, we can prove (2) in the case of $- 2 ~ < ~ T _ { r } - ~ T _ { s } \leq 0$ in the same way.

This completes the proof of (2).

## Appendix B. Simulations

Simulation experiment 1

Input:N, m and r.

Output:α.

Step 1: Uniformly and randomly generate the PSs $\nu _ { i j } ( i = 1 , 2 ; j = 1 , 2 , . . . , m )$ for alternatives $x _ { 1 }$ and $x _ { 2 }$ over m attributes in the interval [0, 1]. Let $\begin{array} { r } { V _ { 1 } = \frac { 1 } { m } \overline { { \sum } } _ { j = 1 } ^ { m } \nu _ { 1 j } } \end{array}$ and $\begin{array} { r } { \dot { V } _ { 2 } = \frac { 1 } { m } \sum _ { j = 1 } ^ { m } \nu _ { 2 j } . } \end{array}$

Step 2: If $\begin{array} { r } { | V _ { 1 } - V _ { 2 } | \in \bigg [ \frac { r - 0 . 1 } { N } , \frac { r } { N } \bigg ) . } \end{array}$ , go to next step; otherwise, go to Step 1.

Step 3: Transform $\nu _ { i j }$ into $t _ { i j }$ in the RS [0, N] via Eqs. (1) and (2). Use Eq. (4) to obtain $\begin{array} { r } { T _ { 1 } = \frac { 1 } { m } \sum _ { i = 1 } ^ { m } t _ { 1 j } } \end{array}$ and $\begin{array} { r } { T _ { 2 } = \frac { 1 } { m } \sum _ { j = 1 } ^ { m } \ t _ { 2 j } . } \end{array}$

Step 4: Based on $V _ { 1 } , V _ { 2 } , T _ { 1 }$ and $T _ { 2 } ,$ the rankings of alternatives can be obtained by the $\mathrm { R S } \ [ 0 , M ]$ and MAVM, respectively.

Step 5: If inconsistency occurs at the ranking level (Definition 2 is not satisfied), then $\alpha = 1 ;$ otherwise $\alpha = 0$

Simulation experiment 1’

Input:N, m and r′.

Output:α′.

Step 1: Same to Step 1 in Simulation experiment 1.

Step 2: I $\begin{array} { r } { \hat { \boldsymbol { \mathrm { \sf \sf \Pi } } } | V _ { 1 } - V _ { 2 } | \in \biggl \lceil \frac { 2 ( r ^ { \prime } - 0 . 1 ) } { N } , \frac { 2 r ^ { \prime } } { N } \biggr ) . } \end{array}$ , go to next step; otherwise, go to Step 1.

Step 3: Same to Step 3 in Simulation experiment 1.

Step 4: Based on $V _ { 1 } , V _ { 2 } , T _ { 1 }$ and $T _ { 2 } ,$ the ratings of alternatives can be obtained by the RS [0,N] and MAVM via Eqs. (1) and (2), respectively. Step 5: If inconsistency occurs at the rating level (Definition 3 is not satisfied), then $\alpha ^ { \prime } = 1 ;$ otherwise $\alpha ^ { \prime } = 0$

Simulation experiment 2

Input:N, m and θ.

Output:β.

Step 1: Uniformly and randomly generate the ratings $t _ { i j } ( i = 1 , 2 ; j = 1 , 2 , . . . , m )$ ) for alternatives $x _ { 1 }$ and $x _ { 2 }$ over m attributes in the interval $[ 0 , N ]$ Let $\begin{array} { r } { T _ { 1 } = \frac { 1 } { m } \sum _ { j = 1 } ^ { m } t _ { 1 j } } \end{array}$ and $\begin{array} { r } { T _ { 2 } = \frac { 1 } { m } \sum _ { j = 1 } ^ { m } \ t _ { 2 j } . } \end{array}$

Step 2: $\mathrm { I f ~ } \left| T _ { 1 } - { \mathit { \Pi } } _ { T _ { 2 } } \right| \in [ \theta \mathrm { ~ - ~ } 0 . 2 , \theta ) .$ , go to next step; otherwise, go to Step 1.

Step 3: Generate $\nu _ { i j } \in \bigg \lceil \frac { t _ { i j } - 0 . 5 } { N } , \frac { t _ { i j } + 0 . 5 } { N } \bigg \rceil$ in the interval [0, 1]. Use Eq. (3) to obtain $\begin{array} { r } { V _ { 1 } = \frac { 1 } { m } \sum _ { i = 1 } ^ { m } \nu _ { 1 j } } \end{array}$ and $\begin{array} { r } { V _ { 2 } = \frac { 1 } { m } \sum _ { j = 1 } ^ { m } \nu _ { 2 j } , } \end{array}$

Step 4: Based on $V _ { 1 } , \ \bar { V _ { 2 } } , \ T _ { 1 }$ and $T _ { 2 } ,$ the rankings of alternatives can be obtained by the RS [0,N] and MAVM, respectively.

Step 5: If inconsistency occurs at the ranking level (Definition 2 is not satisfied), then $\beta = 1 ;$ ; otherwise $\beta = 0 .$

Simulation experiment 2’

Input:N, m and θ.

Output:β′.

Step 1: Same to Step 1 in Simulation experiment 2.

Step 2: $\mathrm { ~ I f ~ } \left| T _ { 1 } - { \cal T } _ { 2 } \right| \in 2 [ \theta - 0 . 2 , \theta ) _ { \mathrm { { \Omega } } }$ , go to next step; otherwise, go to Step 1.

Step 3: Same to Step 3 in Simulation experiment 2.

Step 4: Based on $V _ { 1 } , V _ { 2 } , T _ { 1 }$ and $T _ { 2 } ,$ the ratings of alternatives can be obtained by the RS [0,N] and MAVM via Eqs. (1) and (2), respectively. Step 5: If inconsistency occurs at the rating level (Definition 3 is not satisfied), then $\beta ^ { \prime } = 1 ;$ otherwise $\beta ^ { \prime } = 0$

## References

[1] G. Adomavicius, Y. Kwon, New recommendation techniques for multicriteria rating systems JFFE Intell Syst, 22 (3) (2007) 48–55

[2] D.E. Alwin. J.A. Krosnick. The measurement of values in surveys: A comparison of

[3] K.J. Arrow, Social Choice and Individual Values, John Wiley & Sons, New York, 1951.

[4] A.E. Bargagliotti, L. Li, Decision making using rating systems: When scale meets binary, Decis, Sci, 44 (6) (2013) 1121–1137.

[5] F.H. Barron, B.E. Barrett, Decision quality using ranked attribute weights, Manag.

[6] M. Baucells, R.K. Sarin, Group decisions with multiple criteria, Manag. Sci. 49 (8) (2003) 1105–1118.

[7] R. Bhattacharjee, A. Goel, Avoiding ballot stufing in ebay-like reputation systems, Proceedings of the 2005 ACM SIGCOMM Workshop on Economics of Peer-to-Peet Systems. Philadelphia. PA. 2005

[8] P.Y. Chen, Y. Hong, Y. Liu, The value of multidimensional rating systems: Evidence from a natural experiment and randomized experiments, Manag. Sci. 64 (10) (2017) 4629–4647.

[9] G.A. Churchill Jr., J.P. Peter, Research design efects on the reliability of rating scales: A meta-analysis, J. Mark, Res, 21 (4) (1984) 360–375.

[10] J.N. Cleveland, K.R. Murphy, Analyzing performance appraisal as goal-directed behavior, Res. Pers. Hum. Resour. Manag. 10 (2) (1992) 121–185.

[111 V.P. Crawford, J. Sobel. Strategic information transmission, Econometrica 50 (1982)1431–1451.

[12] M. Danielson, L. Ekenberg, Y. He. Augmenting ordinal methods of attribute weight approximation, Decis. Anal. 11 (1) (2014) 21–26.

[13] J. Dawes, Do data characteristics change according to the number of scale points used? An experiment using 5-point, 7-point and 10-point scales, Int. J. Mark. Res 50 (1) (2008) 61–104.

[14] Y. Dong, Y. Liu, H. Liang, F. Chiclana, E. Herrera-Viedma, Strategic weight ma nipulation in multiple attribute decision making, Omega 75 (2018) 154–164.

[15] Y. Dong, H. Zhang, E. Herrera-Viedma, Integrating experts’ weights generated dynamically into the consensus reaching process and its applications in managing non cooperative behaviors, Decis. Support. Syst. 84 (2016) 1–15.

[16] M. Doumpos, J.R. Figueira, A multicriteria outranking approach for modeling corporate credit ratings: an application of the Electre tri-nC method, Omega 82 (2019) 166–180.

[17] M. Doumpos, C. Zopounidis, A multicriteria outranking modeling approach for credit rating, Decis, Sci, 42 (3) (2011) 721–742.

[18] J.S. Dyer, R.K. Sarin, Group preference aggregation rules based on strength of

[19] P.H. Farquhar, L.R. Keller, Preference intensity measurement, Ann. Oper. Res. 19 (1) (1989) 205–217

[20] H.H. Friedman. T. Amoo. Rating the rating scales, J. Mark, Manag, 9 (3) (1999)

[21] H. Friedman, E. Friedman, A comparison of six overall evaluation rating scales, J.

[22] J.L. García-Lapresta, D. Pérez-Román, A consensus reaching process in the context of non-uniform ordered qualitative scales, Fuzzy Optim. Decis. Making 16 (4) (2017) 449–461,

[23] A. Gibbard, Manipulation of voting schemes: A general result. Econometrica 41 (1973) 587–601.

[24] S. Greco, M. Kadzinski, V. Mousseau, R. Slowinski, Robust ordinal regression for multiple criteria group decision: UTAGMS-GROUP and UTADISGMS-GROUP, Decis. Support. Syst, 52 (3) (2012) 549–561.

[25] P.E. Green, V.R. Rao, Rating scales and information recovery. How many scales and response categories to use? J. Mark. 34 (1970) 33–39.

[26] J.C. Harsanyi, Cardinal welfare, individualistic ethics, and interpersonal comparisons of utility J. Polit, Fcon. 63 (4) (1955) 309–321

[27] J. Hauser, Consumer preference axioms: Behavioral postulates for describing and predicting stochastic choice, Manag. Sci. 24 (13) (1978) 1331–1341.

[28] F. Herrera, L. Martínez, A model based on linguistic 2-tuples for dealing with multigranular hierarchical linguistic contexts in multi-expert decision-making, IEEE Trans. Syst. Man Cybern., Part B (Cybern.) 31 (2) (2001) 227–234.

[29] D.S. Hochbaum, A. Levin, Methodologies and algorithms for group-rankings decision, Manag. Sci. 52 (9) (2006) 1394–1408.

[30] M. Kadzinski, M. Ghaderi, J. Wąsikowski, N. Agell, Expressiveness and robustness ference disaggregation methods: An experimental analysis. Comput. Oper. Res, 87 (87) (2017) 146–164.

[31] R.L. Keeney. H. Raiffa. Decision with Multiple Obiectives: Preferences and Value Tradeofs, John Wiley & Son, New York, 1976.

[32] R.L. Keeney, A group preference axiomatization with cardinal utility, Manag. Sci. 23 (2) (1976) 140–145.

[33] R.L. Keeney, C.W. Kirkwood, Group decision making using cardinal social welfare functions, Manag, Sci, 22 (4) (1975) 430–437.

[34] F.J. Landy, J.L. Farr, Performance rating, Psychol. Bull. 87 (1) (1980) 72–107.

[35] D.R. Lehmann, J. Hulbert, Are three-point scales always good enough? J. Mark. Res. 9 (4) (1972) 444–446.

[36] J. Liu, X. Liao, W. Zhao, N. Yang, A classification approach based on the outranking

[37] F. Maccheroni, M. Marinacci, A. Rustichini, Social decision theory: Choosing withir

[38] S. Maldonado, C. Bravo, J. López, J. Pérez, Integrated framework for profit-based feature selection and SVM classification in credit scoring, Decis. Support. Syst. 104

(2017) 113–121.

[39] J.A. McCarty, L.J. Shrum, The measurement of personal values in survey research: A test of alternative rating procedures, Public Opin. Quar. 64 (3) (2000) 271–298.

[40] J. Morgan, P.C. Stocken, Information aggregation in polls, Am. Econ. Rev. 98 (3) (2008) 864–896.

[41] K.R. Murphy, J.N. Cleveland, A.L. Skattebo, T.B. Kinney, Raters who pursue different goals give diferent ratings, J. Appl. Psychol. 89 (1) (2004) 158–164.

[42] C. Preston, A.M. Colman, Optimal number of response categories in rating scales: Reliability, validity, discriminating power, and respondent preferences, Acta Psychol. 104 (1) (2000) 1–15.

[43] M.A. Satterthwaite, Strategy-proofness and Arrow’s conditions: Existence and correspondence theorems for voting procedures and social welfare functions, J. Econ. Theory 10 (2) (1975) 187–217.

[44] N. Schwarz, B. Knäuper, H.J. Hippler, E. Noelle-Neumann, L. Clark, Rating scales numeric values may change the meaning of scale labels, Public Opin. Quart. 55 (4) (1991) 570–582.

[45] X. Sun, M. Han, J. Feng, Helpfulness of online reviews: Examining review informativeness and classification thresholds by search products and experience products, Decis. Support. Syst. 124 (2019) 113099.

[46] H. Tüselmann, R.R. Sinkovics, G. Pishchulov, Towards a consolidation of worldwid journal rankings–A classification using random forests and aggregate rating via dat envelopment analysis, Omega 51 (2015) 11–23.

[47] T. Van Gestel, B. Baesens, P. Van Dijcke, J. Garcia, J.A. Suykens, J. Vanthienen, A process model to develop an internal rating system: Sovereign credit ratings, Decis. Support. Syst, 42 (2) (2006) 1131–1151.

[48] D. Von Winterfeldt, W. Edwards, Decision Analysis and Behavioral Research. Cambridge University Press. Cambridge. 1986.

[49] M. Waung, S. Highhouse, Fear of conflict and empathic bufering: Two explanations for the inflation of performance feedback, Organ. Behav. Hum. Decis. Process. 71 (1) (1997) 37–54.

[50] B. Weijters, E. Cabooter, N. Schillewaert, The efect of rating scale format on response styles: The number of response categories and response category labels, Int. J. Res. Mark. 27 (3) (2010) 236–247.

[51] H. Zhang, Y. Dong, J. Xiao, F. Chiclana, E. Herrera-Viedma, Personalized individual

semantics-based approach for linguistic failure modes and efects analysis with incomplete preference information, IISE Trans. (2020), https://doi.org/10.1080 24725854.2020.1731774 in press.

[52] L. Zhang, K. Mistry, C.P. Lim, S.C. Neoh, Feature selection using firefly optimization for classification and regression models, Decis. Support. Syst. 106 (2018) 64–85.

Sihai Zhao received the B.S. degree from the Business School, Sichuan University, Chengdu, China in 2016. He is currently pursuing the Ph.D. Degree with the Business School, Sichuan University, Chengdu, China. His current research interests include group decision making, and risk analysis.

Yucheng Dong received the B.S. and M.S. degrees in mathematics from Chongqing University, Chongqing, China, in 2002 and 2004, respectively, and the Ph.D. degree in management from Xi'an Jiaotong University, Xi'an, China, in 2008. He is currently a Professor with the Business School, Sichuan University, Chengdu, China. His current research interests include decision analysis, human dynamics, big data analytics, social network, and risk analysis. He has published over 100 international journal papers in DSS, EJOR, IEEE TBD, IEEE TCYB, IEEE TFS, IEEE TCSS, IEEE TSMCS, IEEE TR, Omega and Scientific Data. Prof. Dong is an Area Editor/Associate Editor of Computers and Industrial Engineering, Group Decision and Negotiation, IEEE TSMC: Systems, and Information Fusion. He has been identified by Clarivate as Highly Cited Researcher in the field of computer science.

Ying He received the B.S. degree in economics from Xi'an jiaotong University, Xi'an, China, in 2004, and the Ph.D. degree in information, risk, and operations management from McCombs School of Business at the University of Texas at Austin in 2013. He was awarded the first-place prize from the INFORMS Decision Analysis Society for its student paper competition in 2011. Currently, he is an associate professor in the Department of Business and Economics at University of Southern Denmark. His research interests include decision analysis, utility theory, and behavioral decision making. He has published over 10 international journal papers in Decision Analysis, Journal of Mathematical Economics, and Operations Research.
