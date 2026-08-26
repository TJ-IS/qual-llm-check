---
otero_id: 10764
otero_key: "7FQ2ZMBU"
title: "Using Gower Plots and Decision Balls to rank alternatives involving inconsistent preferences"
authors: "Li-Ching Ma; Han-Lin Li"
year: "2011"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2011.04.004"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Using Gower Plots and Decision Balls to rank alternatives involving inconsistent preferences

Li-Ching Ma <sup>a,</sup>⁎, Han-Lin Li <sup>b</sup>

<sup>a</sup> Department of Information Management, National United University, Taiwan, ROC

<sup>b</sup> Institute of Information Management, National Chiao Tung University, Taiwan 300, ROC

## a r t i c l e i n f o

Article history: Received 5 October 2010 Received in revised form 28 March 2011 Accepted 14 April 2011 Available online 20 April 2011

Keywords: Visualization Gower Plot Decision Ball Inconsistence Ranking

## a b s t r a c t

Ranking alternatives involving inconsistent preferences is one of the most important topics in decisionmaking. Determining how to assist decision makers in understanding the decision context and adjusting inconsistencies in judgment are two important issues in ranking alternatives. This study proposes a visualization approach which will assist decision makers in ranking alternatives involving inconsistent preferences. Gower Plots are adopted to detect alternatives involving inconsistencies. An adjusting model is developed to provide suggestions for simultaneously improving ordinal and cardinal inconsistencies. A Decision Ball model is applied to visualize the decision context. By a graphical and interactive interface, decision makers can iteratively detect inconsistencies, choose the preferred way to adjust inconsistencies observe relationships among alternatives, and then rank alternatives.

© 2011 Elsevier B.V. All rights reserved

## 1. Introduction

Ranking alternatives involving inconsistent preferences is one of the most important topics in decision-making. Keeney [13] identi<sup>fi</sup>ed 12 major mistakes frequently made that limit one's ability in making good value judgments, in which “not understanding the decision context” and “failure to use consistency checks in assessing value trade-offs” are two critical mistakes. Hence, determining how to assist decision makers in understanding the decision context and adjusting inconsistencies in judgment are two important issues to be considered in ranking alternatives.

There is evidence that decision makers' preferences are often in<sup>fl</sup>uenced by visual background information [23,26]. Visual representations can simplify and aggregate complex information into a meaningful pattern, assist people in comprehending their environment and allow for the simultaneous perception of parts as well as a perception of interrelations between parts [6,19,24,27,28]. Discovering how to provide visual aids which will help decision makers observe background information is the <sup>fi</sup>rst issue to be addressed by this study.

Ranking alternatives incorporating preferences is a popular issue in decision-making. One common format for expressing preferences is to use pairwise comparisons; this forces a person to make a direct choice of one object over another when comparing two objects, rather than requiring one to compare all objects simultaneously [4]. Many methods have been proposed [12,21,25] to rank alternatives using pairwise comparisons. However, inconsistencies are not unexpected, as making value judgments is dif<sup>fi</sup>cult [13]. The ranks different methods yield do not vary signi<sup>fi</sup>cantly when the decision makers' preferences are consistent. However, if a preference matrix is highly inconsistent, different ranking methods may produce wildly different priorities and rankings. Determining how to help the decision makers to detect and adjust those inconsistencies in order to make a more reliable decision is therefore the second issue addressed here.

This study proposes a graphic ranking method, composed of the Gower Plot technique, an inconsistencies adjusting model and a Decision Ball model. These provide visual aids which help decision makers to detect inconsistencies, to adjust inconsistencies and to observe relationships among alternatives. The Gower Plot [7,8,17] technique is used to graphically pinpoint the alternatives involving major inconsistencies. An adjusting model is constructed to adjust inconsistencies. A Decision Ball model [18,19] is used to illustrate the background context by representing similarities among alternatives on a sphere. By using both graphic and interactive interface, decision makers can iteratively detect inconsistencies, choose the preferred way to adjust inconsistencies, observe relationships among alternatives, and then rank alternatives.

This paper is organized as follows. Section 2 reviews the relevant literature and section 3 sets the decision-making framework. Section 4 illustrates the proposed approach and decision-making process; three models for detecting inconsistencies, adjusting inconsistencies and displaying alternatives are introduced in this section. Section 5 <sup>fi</sup>rst presents a numerical example used to demonstrate the proposed approach and then describes an experiment conducted to test the ef<sup>fi</sup>cacy of the proposed approach in practice. Conclusions are offered in Section 6.

## 2. Relevant literature

The <sup>fi</sup>rst issue addressed in this study is providing visual aids which help decision makers to observe background information. Several graphical techniques have been developed to aid the decisionmaking process. For instance, Jank and Kannan [11] proposed a spatial multinomial model of customer choice to assist <sup>fi</sup>rms in understanding how their online customers' preferences and choices vary across geographical markets. Kiang [14] extended a self-organizing map (SOM) [15] network to classify decision choices by neural network techniques. Cox and Cox [5] developed various multidimensional scaling techniques to provide a visual representation of similarities among a set of alternatives. Li and Ma [18] developed a Decision Ball model to assist decision makers in observing decision processes. The ranks of alternatives and the similarities among them can be seen on the surface of a sphere. However, most of these graphic techniques are incapable of detecting and adjusting the decision makers' inconsistent preferences.

The second issue addressed in this study involves detecting and adjusting inconsistencies. A pairwise comparison ranking problem can be subject to magnitude of the degree of preference, intensity ranking; or in terms of ordinal preferences only, preference ranking. These are sometimes also referred to as cardinal versus ordinal preferences [9].

Determining how to adjust inconsistencies in a preference matrix has been addressed by many studies. For instance, Maas et al. [20] presented an operational model in which a preference that causes intransitivity must be reversed if it is of less importance; this method can solve the problems of ordinal inconsistency. However, the problem of cardinal inconsistency has not been addressed. Many researchers [3,9,21,22] have used multi-criteria decision making approaches to <sup>fi</sup>nd a consistent ranking with minimal error (i.e., minimum cardinal inconsistencies) in intensity-ranking problems. However, only considering cardinal inconsistencies may result in unexpected rank reversal problems. Besides, conventional eigenvalue approaches cannot treat an incomplete preference matrix, and most of these focus on adjusting cardinal or ordinal inconsistencies instead of adjusting both cardinal and ordinal incontinences simultaneously.

Genest and Zhang [7] proposed a powerful graphical method based on the work of Gower [8], the so-called Gower Plot, to detect inconsistencies in decision makers' preferences on a 2-dimensional plane. However, the Gower Plots did not provide any systematical way of adjusting inconsistencies. Li and Ma [17] adopted Gower Plot method to detect inconsistencies and developed linear programming models to adjust these inconsistencies. Nevertheless, only users with sophisticated linear programming knowledge are able to apply this method.

Most of the methods for adjusting inconsistencies may improve them; however, the automatically adjusted preference matrix may be far beyond the real preferences acceptable to decision makers. This study incorporates the advantages of Gower Plots and Decision Balls in detecting inconsistencies and providing visual aids to help decision makers to better observe the decision context; it also develops a linear programming model designed to assist decision makers in simultaneously adjusting ordinal and cardinal inconsistencies. Decision makers can choose the preferred way to adjust inconsistencies using both a graphical and interactive interface.

## 3. Setting the decision-making framework

Multicriteria decision makers tend to use screening, ordering and choosing phases to <sup>fi</sup>nd a preference [2]. They tend to make little effort in the <sup>fi</sup>rst phase as they screen out clearly unwanted alternatives, use somewhat more effort in the second phase as they try to place a preference order on the remaining alternatives and employ the highest effort in the <sup>fi</sup>nal phase when choosing between two or three close alternatives.

The proposed decision-making framework is depicted in Fig. 1 and illustrated by these three phases as listed below:

(i) The screening phase: The decision maker tries to screen out clearly unwanted alternatives. The decision maker speci<sup>fi</sup>es upper and lower bounds by identifying particular attributes to screen out poor alternatives.

(ii) The ordering phase: The decision maker tries to obtain a preference order on the remaining alternatives. There are three steps in this phase, including specifying preferences, detecting inconsistencies and adjusting inconsistencies. Once inconsistencies are improved, a priority of alternatives is determined.

● Specifying preferences: The decision maker identi<sup>fi</sup>es personal preferences. Since it is usually not easy for a multicriteria decision maker to simultaneously compare all alternatives, pairwise comparisons are adopted here. A preference matrix is obtained in this step.

● Detecting inconsistencies: Inconsistencies in the preference matrix are determined. Because inconsistent preferences may result in an unreliable ranking order, signi<sup>fi</sup>cant inconsistencies should be detected and adjusted to achieve a reliable solution. The Gower Plot technique (denoted as Model 1) is applied in this study to help the decision maker to visually detect inconsistencies.

● Adjusting inconsistencies: Inconsistent preferences detected in the previous step are revised. A proposed optimization model (denoted as Model 2) assists decision makers in adjusting these inconsistencies.

(iii) The choosing phase: The decision maker attempts to choose between two or three close alternatives. A Decision Ball model (denoted as Model 3) is adopted to assist a decision maker in observing the ranks of alternatives and the similarities among them. The decision maker could make a <sup>fi</sup>nal choice based on the visual support of the Decision Ball.

The three models used in this study are illustrated in the next section.

## 4. The proposed approach

The decision problems in this study can be expressed generally as shown below. Consider a set of alternatives $A { = } \{ A _ { 1 } , A _ { 2 } , . . . , A _ { \mathrm { n } } \}$ for solving a choice problem, where a decision maker selects m criteria to be ful<sup>fi</sup>lled. The values of criteria $C _ { 1 } , . . . , C _ { m }$ for alternative $A _ { i }$ are expressed as $c _ { i , 1 } , . . . , c _ { i , m } .$ Denote $\mathsf { C } = [ c _ { i , k } ] _ { n \times m }$ as the criterion matrix of the decision problem. All criteria $C _ { i }$ are assumed to be bene<sup>fi</sup>cial criteria, which means the higher the value of $c _ { i , k } ,$ the better the alternative $A _ { i }$ is. Denote $S _ { i }$ as the score value of an alternative $A _ { i \cdot }$ An additive function is assumed in this study because it is more understandable for decision makers and the most commonly used form in practice [1]. An additive score function of an alternative A $( c _ { i , 1 }$ $c _ { i , 2 } , . . . , c _ { i , m } )$ is expressed below:

$$
S _ {i} (\mathbf {w}) = \sum_ {k = 1} ^ {m} w _ {k} \frac {c _ {i , k} - c _ {k}}{\overline {{c _ {k}}} - \underline {{c _ {k}}}},\tag{1}
$$

where (i) $w _ { k }$ is the weight of criterion $C _ { k } , \ 0 \le w _ { k } \le 1$ , ∀k and $\sum _ { k = 1 } ^ { m } \mathbf { \epsilon } w _ { k } = 1 . \mathbf { w } { = } ( w _ { 1 } , w _ { 2 } , . . . , w _ { m } )$ is a weight vector, (ii) c and $\underline { { c _ { k } } }$ are respectively the upper and lower bounds of a criterion $C _ { k } ,$ which can be speci<sup>fi</sup>ed by a decision maker or set as the largest and smallest values of the criterion, and $( \mathrm { i i i } ) 0 { \leq } S _ { i } ( \mathbf { w } ) { \leq } 1$ . In order to make sure all weights of criteria and the scores of alternatives are positive, a criterion $c _ { i , k }$ with a cost feature (i.e., which a decision maker would like to keep as small as possible) is transferred from $c _ { i , k } \ t o \ ( \overline { { c _ { k } } } - c _ { i , k } )$ in advance. Following the score functions, the dissimilarity between $A _ { i }$ and $A _ { j }$ is de<sup>fi</sup>ned as:

![](/api/attachments/7FQ2ZMBU/fulltext/images/d397a2db6ad63d6899a5c3bf3b2cdbceb90b5b9f0f2698455fd17bf52231951a.jpg)  
Fig. 1. The decision-making framework.

$$
\delta_ {i, j} (\mathbf {w}) = \sum_ {k = 1} ^ {m} w _ {k} \frac {\left| c _ {i , k} - c _ {j , k} \right|}{\overline {{c _ {k}}} - \underline {{c _ {k}}}},\tag{2}
$$

where $0 \leq \delta _ { i , j } ( \mathbf { w } ) \leq 1$ and ${ \delta _ { i , j } ( { \bf { w } } ) = \delta _ { j , i } ( { \bf { w } } ) }$ . Clearly, if $c _ { i , k } = c _ { j , k }$ for all k then $\delta _ { i , j } ( \mathbf { w } ) = 0$

Assume a decision maker can specify his/her preferences by the ratio of the score of one alternative to another alternative in a pairwise fashion. Denote $\mathsf { R } = [ r _ { i } ,$ <sub>, j</sub>]<sub>n×n</sub> as a decision maker's preference matrix where $r _ { i , j }$ is the ratio of S to $S _ { j } , r _ { i , j } { = } 1 / r _ { j , i }$ for all i, j. If the decision maker is unclear about the ratio of S to $S _ { j } , r _ { i , j }$ remains blank (denoted as $r _ { i , j } { = } \varphi )$ . R is ordinally inconsistent (intransitive) if for some $i , j , k { \in } \{ 1 , 2 , 3 , . . . , n \}$ there exists $r _ { i , j } >$ $1 , r _ { j , k } > 1$ , but $r _ { i , k } < .$ 1. R is cardinally inconsistent if for some $i , j , k { \in } \{ 1 , . . . , n \}$ there exists $r _ { i , k } { \neq } r _ { i , j } { \times } r _ { j , k } [ 7 ]$ . R is incomplete if there any $r _ { i , j } { = } \varphi \mathrm { e x i s t s } .$

## 4.1. Detecting inconsistencies

Many researchers have adopted the consistency ratio (CR) [21] to measure the inconsistency of a complete preference matrix. If the value of CR is smaller or equal to 10%, the level of inconsistency is acceptable. However, decision makers are unable to know if there is ordinal inconsistency by using CR.

Given a $\mathtt { R } = [ r _ { i , j } ] _ { n \times n } , \mathtt { a }$ Gower Plot [7,8] can be displayed to detect the ordinal consistency for R. This section brie<sup>fl</sup>y introduces how to use Gower Plots to detect ordinal inconsistency. The mathematical properties of Gower Plots are illustrated in Appendix A.

## 4.1.1. Model 1 Gower Plots

Denote $\boldsymbol { \mathrm { T } } = [ t _ { i , \ j } ] _ { n \times n } , \ \boldsymbol { \mathrm { a } }$ skew-symmetric matrix, as a tournament matrix corresponding to R, where $t _ { i , j } = 1 { \mathrm { i f } } r _ { i , j } { > } 1 ; t _ { i , j } = 0 { \mathrm { i f } } r _ { i , j } = 1 ; t _ { i , j } =$ $- 1 \mathrm { i f } \ r _ { i , j } < 1$ . A plot called the ordinal Gower Plot based on T can be depicted in a plane by applying singular value decomposition [10]. Denote T<sup>t</sup> as a transposition of T. Let $\lambda _ { 1 }$ be the largest singular value of $\operatorname { T . L e t } \operatorname { U } { } = ( u _ { 1 } , . . . , u _ { n } ) ^ { \mathrm { t } }$ and $\mathsf { V } = ( \nu _ { 1 } , . . . , \nu _ { n } ) ^ { t }$ as n points $P _ { i } = ( u _ { i } , \nu _ { i } )$ in the plane, where U and V are orthonormal eigenvectors of T<sup>t</sup>T corresponding to $\lambda _ { 1 } ^ { 2 } .$ . Each decision alternative $A _ { i }$ is expressed as a point $P _ { i }$ on an ordinal Gower Plot. A set of alternatives is said to be ordinally consistent if the following three conditions are satis<sup>fi</sup>ed: (i) the location of all points are equidistant from the origin within a $1 8 0 ^ { \circ }$ arc; (ii) the angles between consecutive points are equal to 180/n degrees; (iii) the faithfulness of the graphical representation is demonstrated by the variability factor being approximately 1 (see Appendix A).

For an ordinally consistent matrix R, suppose the points are arranged counter-clock-wise in the order of $A _ { i } , A _ { j } , . . . , A _ { k } ,$ then the superiority for decision alternatives is $A _ { i } { > } A _ { j } { > } { \ldots } { > } A _ { k } ,$ , where $A _ { i } \ { } ^ { * } { \succ } ^ { n } A _ { j }$ implies that $A _ { i }$ dominates A . If R is complete and ordinally consistent, all $A _ { i }$ can be ranked immediately; otherwise, R should be adjusted in advance.

## 4.2. Adjusting inconsistencies

An adjusting model is proposed to adjust ordinal and cardinal inconsistencies simultaneously. Given a preference matrix $\mathtt { R } = [ r _ { i , j } ] _ { n \times }$ <sub>n</sub>, where R may be incomplete or inconsistent. A model for adjusting R is formulated below:

$$
\begin{array}{l l} \underset {\{w _ {k} \}} {\text { Min }} & M \times O b j 1 + O b j 2 \\ & O b j 1 = \sum_ {i = 1} ^ {n} \sum_ {j > i} ^ {n} b _ {i, j} \\ & O b j 2 = \sum_ {i = 1} ^ {n} \sum_ {j > i} ^ {n} \alpha_ {i, j} \end{array}\tag{3}
$$

s:t: $\left( \frac { S _ { i } } { S _ { j } } - 1 \right) \times \left( r _ { i , j } - 1 \right) + M \times b _ { i , j } \geq \mathfrak { E } .$ ; for all $i , j$ where $r _ { i , j } \neq \varphi$ and r<sub>i;j</sub>≠1;

$$
- \left| S _ {i} - S _ {j} \right| + M \times b _ {i, j} \geq 0, \text {   for   all   } i, j \text {   where   } r _ {i, j} = 1,\tag{4}
$$

$$
\left| \frac {S _ {i}}{S _ {j}} - r _ {i, j} \right| \leq \alpha_ {i, j}, \forall i, j,\tag{5}
$$

$$
S _ {i} (\mathbf {w}) = \sum_ {k = 1} ^ {m} w _ {k} \frac {c _ {i , k} - c _ {k}}{\overline {{c _ {k}}} - \underline {{c _ {k}}}}, \forall i\tag{6}
$$

$$
\sum_ {k = 1} ^ {m} w _ {k} = 1,\tag{7}
$$

$$
0 \leq w _ {k} \leq 1, \forall k,\tag{8}
$$

$b _ { i , j } { \in } \{ 0 , 1 \}$ ; M is a large value; ε is a tolerable error:

9

The decision variables in Model 2 are $\left( w _ { 1 } , w _ { 2 } , . . . , w _ { m } \right)$ . The <sup>fi</sup>rst objective (Obj1) of Model 1 is to achieve ordinal consistency by minimizing the number of preferences $( \mathrm { i } . \mathrm { e } . , r _ { i , j } )$ being reversed. If $r _ { i , j }$ is reversed, the binary variable $b _ { i , j } = 1 ;$ ; otherwise, $b _ { i , j } = 0$ . Expression (3) means: when $r _ { i , j } \neq$ ϕ and $\begin{array} { r } { r _ { i , j } \neq 1 , b _ { i , j } = 0 , \mathrm { i f } \left( \mathrm { i } \right) \left( \frac { S _ { i } } { S _ { i } } > 1 \right) } \end{array}$ and $( r _ { i , j } > 1 )$ or (ii) $\left( \frac { S _ { i } } { S _ { j } } < 1 \right)$ <sup></sup>and $\left( r _ { i , j } < 1 \right)$ ; and otherwise $b _ { i , j } = 1$ . A tolerable positive number ε is used to avoid $\begin{array} { r } { \frac { S _ { i } } { S _ { i } } = 1 } \end{array}$ . Expression (4) means: when $r _ { i , j } = 1 , b _ { i , j } = 0$ $\mathrm { i f } S _ { i } = S _ { j } ;$ and otherwise $b _ { i , j } = 1$ . The second objective $( O b j 2 )$ is to achieve cardinal consistency by minimizing the $\alpha _ { i , j }$ values. Expression (5) is used to minimize the difference between $\frac { S _ { i } } { S _ { j } }$ and $r _ { i , j }$ . Since ordinal consistency (Obj1) is more important than cardinal consistency $( O b j 2 )$ , Obj1 is multiplied by a large value M in the objective function. Expressions (6) and (7) are derived from Expression (1). Expression (8) sets the upper and lower boundaries for weighting.

This model is nonlinear, which can be converted into the following linear mixed 0–1 program:

Model 2 Adjusting model

$$
\underset {\{w _ {k} \}} {\text { Min }} \quad M \times O b j 1 + O b j 2
$$

$$
O b j 1 = \sum_ {i = 1} ^ {n} \sum_ {j > i} ^ {n} b _ {i, j}
$$

$$
O b j 2 = \sum_ {i = 1} ^ {n} \sum_ {j > i} ^ {n} \alpha_ {i, j}\tag{10}
$$

s:t: $\left( S _ { i } - S _ { j } \right) \times \left( \boldsymbol { r } _ { i , j } - 1 \right) + M \times b _ { i , j } \geq \varepsilon ,$ ; for all $i , j$ where $r _ { i , j } \neq \Phi$ and r<sub>i;j</sub>≠1;

$$
- M \times b _ {i, j} \leq S _ {i} - S _ {j} \leq M \times b _ {i, j}, \text {   for   all   } i, j \text {   where   } r _ {i, j} = 1,\tag{11}
$$

$$
\begin{array}{l} S _ {j} \times r _ {i, j} - \alpha_ {i, j} \leq S _ {i} \leq S _ {j} \times r _ {i, j} + \alpha_ {i, j}, \forall i, j, \\ (6) \sim (9), \end{array}\tag{12}
$$

where Expressions (10), (11) and (12) are transformed from Expressions (3), (4) and (5) respectively. After the weight vector, $\left( w _ { 1 } , \ w _ { 2 } , \ . . . , \ w _ { m } \right)$ , is found, $S _ { i } ( \pmb { w } ) =$ $\sum _ { \nu = 1 } ^ { m } w _ { k } \frac { c _ { i , k } - c _ { k } } { \overline { { c _ { k } } } - \underline { { c _ { k } } } }$ <sup>ð Þ</sup>can be calculated and a complete matrix can be obtained as $\mathbb { R } ^ { \prime } = [ r ^ { \prime } { } _ { i , j } ] _ { n \times { } n } ,$ where $\begin{array} { r } { r _ { i , j } ^ { ' } = \frac { S _ { i } } { S _ { i } } \mathrm { i f } r _ { i , j } ^ { } = \varphi _ { } 0 \mathrm { r } b _ { i , j } = 1 ; } \end{array}$ ; otherwise, $r _ { i , j } ^ { \prime } { = } r _ { i , j } .$ The dissimilarities between two alternatives $\delta _ { i , j } ( \pmb { w } )$ can also be calculated based on Expression (2).

## 4.3. Displaying alternatives

A Decision Ball model [19] based on a non-metric multidimensional scaling technique is used to display all alternatives on the surface of a sphere. This study uses a sphere model rather than the traditional 2- dimensional plane or 3-dimensional cube models because the sphere is easier to observe and involves no edges. The arc length between two alternatives is used to represent the dissimilarity between them, e.g. the larger the difference, the longer the arc length. In addition, the alternative with a higher score is designed to be closer to the North Pole so that alternatives can be located on the concentric circles surrounding the pole in their order of rank when viewed from above.

For the purpose of comparison, we de<sup>fi</sup>ne an ideal alternative $A _ { * }$ where $A _ { * } = A _ { * } ( \overline { { c _ { 1 } } } , \overline { { c _ { 2 } } } , . . . , \overline { { c _ { m } } } )$ and $S _ { * } = 1 \ . A _ { * }$ is designed to be located at the north pole with coordinate $( x _ { * } , y _ { * } , z _ { * } ) = ( 0 , 1 , 0 )$ . Denote $d _ { i , j } { \sf a s }$ the Euclidean distance between $A _ { i }$ and $A _ { j } .$ Based on the non-metric multidimensional scaling technique [5], denote $\hat { d } _ { i , j }$ as a monotonic transformation of dissimilarity $\delta _ { i , j }$ satisfying the following condition: $\mathrm { i f } \delta _ { i , j } { < } \delta _ { p , q } ,$ then $\hat { d } _ { i , j } { < } \hat { d } _ { p , q } .$ . The coordinates $\left( x _ { i } , y _ { i } , z _ { i } \right)$ of all alternatives $A _ { i }$ can be calculated using the following model:

## Model 3 Decision Ball Model

$$
\underset {\{x _ {i}, y _ {i}, z _ {i} \}} {\text { Min }} O b j 3 = \sum_ {i = 1} ^ {n} \sum_ {j > i} ^ {n} \left(d _ {i, j} - \hat {d} _ {i, j}\right) ^ {2}
$$

$$
\mathrm{s.t.} \qquad y _ {i} = 2 S _ {i} - S _ {i} ^ {2}, \forall i,\tag{13}
$$

$$
\hat {d} _ {i, j} \leq \hat {d} _ {p, q} - \varepsilon , \forall \delta_ {i, j} <   \delta_ {p, q},\tag{14}
$$

$$
d _ {i, j} ^ {2} = \left(x _ {i} - x _ {j}\right) ^ {2} + \left(y _ {i} - y _ {j}\right) ^ {2} + \left(z _ {i} - z _ {j}\right) ^ {2}, \forall i, j,\tag{15}
$$

$$
x _ {i} ^ {2} + y _ {i} ^ {2} + z _ {i} ^ {2} = 1, \forall i,\tag{16}
$$

$$
- 1 \leq x _ {i}, z _ {i} \leq 1, \quad 0 \leq y _ {i} \leq 1, \forall i, \varepsilon \text {   is   a   tolerable   error.   }\tag{17}
$$

The objective (Obj3 ) of Model 3 is to minimize the sum of the difference between $d _ { i , j }$ and ${ \ddot { d } } _ { i , j } .$ . Expression (13) is from the work of Ma [19], which indicates that the alternative with a higher score is designed to be closer to the North Pole. Expression (14) is based on the non-metric multidimensional scaling technique. Expressions (16) and (17) ensure that all alternatives are graphed on the surface of the ball and are located on the northern hemisphere.

The faithfulness of this visual representation can be measured by Stress [16], which is a numerical measure of the closeness between the dissimilarities in the lower dimension and the original spaces formulated as follows:

$$
\text { Stress } = \sqrt {\frac {O b j 3}{\sum_ {i = 1} ^ {n} \sum_ {j > i} ^ {n} d _ {i , j} ^ {2}}}\tag{18}
$$

A solution is desirable if its stress value is less than 10%.

## 4.4. The process

The <sup>fl</sup>owchart of the proposed approach is shown in Fig. 2. The decision-making process is illustrated in the following four major steps:

## bThe screening phaseN

A decision maker may specify upper and lower bounds by identifying particular attributes to screen out poor alternatives in advance.

bThe ordering phaseN

Step 1 (Input data) A decision maker inputs a data matrix $\mathsf { C } = [ c _ { i , k } ] _ { n \times m } ,$ and speci<sup>fi</sup>es a preference matrix $\begin{array} { r } { \mathtt { R } = [ r _ { i , j } ] _ { n \times n } , } \end{array}$ where R can be an incomplete matrix.

Step 2 (Detecting inconsistencies) Applying the Gower Plot model (Model 1) to R, an ordinal Gower Plot is shown. The ordinal inconsistencies can be detected.

Step 3 (Adjusting inconsistencies) Applying Model 2 to the data and preference matrix yields a set of weights w. Based on the weights w obtained, the score of alternatives $S _ { i } ( \boldsymbol { \mathsf { w } } )$ and dissimilarities $\delta _ { i , j } ( \pmb { \mathsf { w } } )$ among alternatives are calculated. If R <sup>ð Þ</sup>is not consistent, options for adjustments are listed. The decision maker can choose to adjust the preference matrix from the suggested options. If the decision maker decides to adjust preferences directly then go to Step 1.

## bThe choosing phaseN

Step 4 (Displaying alternatives) Applying the Decision Ball model (Model 3) to S (w) and $\delta _ { i , j } ( \pmb { w } )$ yields the coordinates $( x _ { i } , y _ { i } , z _ { i } )$ <sup>ð Þ</sup>of alternatives on the Decision Ball. The Decision Ball is then displayed to the decision maker. The decision maker can observe the ranks of alternatives and the similarities among them on the ball, and make a <sup>fi</sup>nal decision.

## 5. An example and an experiment

This section <sup>fi</sup>rst presents a numerical example used to demonstrate the proposed approach and then describes an experiment conducted to test the ef<sup>fi</sup>cacy of the proposed approach in practice.

## 5.1. A numerical example

The choice of a store location has a profound effect on the entire business life of a retail operation. Consider a manager who needs to select a location for opening a grocery store. Eight alternative locations from $A _ { 1 }$ through $A _ { 8 }$ are under consideration. The manager sets four criteria to be ful<sup>fi</sup>lled: $\left( C _ { 1 } \right)$ suf<sup>fi</sup>cient space, (C ) high population density, (C ) heavy traf<sup>fi</sup>c, and (C ) low cost. Store size is measured in square feet. The number of people who live within a onemile radius is used to calculate population density. The number of vehicles passing the spot per hour is adopted to evaluate the volume of traf<sup>fi</sup>c <sup>fl</sup>ow. Cost is measured by monthly rental fee.

![](/api/attachments/7FQ2ZMBU/fulltext/images/66d973fc71c93ef36df9e3ed21cb859ba8b922b4f84a1d216a508734aad144e8.jpg)  
Fig. 2. The <sup>fl</sup>owchart of the proposed approach.

The decision-making process is illustrated following the steps in Section 4.4 as detailed below:

Step 1 (Input data) The manager inputs the criteria values of eight candidate locations in the criterion matrix C, as shown in Table 1. Next, the manager uses pairwise comparisons to express preferences among pairs of alternatives in preference matrix R, as listed in Fig. 3(a). Because the manager is unable to make comparison among some pairs, the relationships $r _ { 1 , 8 } ,$ $r _ { 2 , 5 } ,$ $r _ { 3 , 6 } ,$ r and $r _ { 6 , 7 }$ are left blank, which means R is incomplete.

Step 2 (Detecting inconsistencies) Since the preference matrix R is incomplete, the CR cannot be measured directly. Applying the Gower Plot model (Model 1) to R, an ordinal Gower Plot is shown in Fig. 3(b) with faithfulness 83.99%. The preference matrix R is ordinally inconsistent because the location of $A _ { 1 } , A _ { 3 }$ and $A _ { 7 }$ are out of the $1 8 0 ^ { \circ }$ arc, which indicates that $A _ { 1 } , A _ { 3 } ,$ , and

Criterion matrix of the store location example.

<table><tr><td rowspan="2" colspan="2">Criteria</td><td colspan="8">Alternative</td></tr><tr><td>A1</td><td>A2</td><td>A3</td><td>A4</td><td>A5</td><td>A6</td><td>A7</td><td>A8</td></tr><tr><td> $C_1$ </td><td>Store size</td><td>1600</td><td>850</td><td>600</td><td>1000</td><td>900</td><td>1000</td><td>1500</td><td>800</td></tr><tr><td> $C_2$ </td><td>Population</td><td>960</td><td>960</td><td>1140</td><td>750</td><td>840</td><td>900</td><td>840</td><td>1260</td></tr><tr><td> $C_3$ </td><td>Traffic</td><td>510</td><td>520</td><td>550</td><td>440</td><td>450</td><td>500</td><td>530</td><td>600</td></tr><tr><td> $C_4$ </td><td>Rental fee</td><td>3200</td><td>4500</td><td>4000</td><td>6600</td><td>5500</td><td>4400</td><td>3800</td><td>3500</td></tr></table>

A are the alternatives involving major ordinal inconsistence. There exists an intransitive relationship among $A _ { 1 } , A _ { 3 }$ and $A _ { 7 } .$ That is, $A _ { 1 }$ is preferred to A<sub>3</sub> $\left( r _ { 1 , 3 } > 1 \right)$ , and $A _ { 3 }$ is preferred to $A _ { 7 }$ $( r _ { 3 , 7 } > 1 ) ;$ however, $A _ { 7 }$ is preferred to $\begin{array} { l l } { A _ { 1 } } & { ( r _ { 1 , 7 } { < } 1 ) } \end{array}$ . The preference causing major ordinal inconsistency is $r _ { 1 , 7 } , r _ { 3 , 7 } ,$ or $r _ { 1 , 3 \cdot } \mathrm { R }$ is also cardinally inconsistent. For instance, there exists $r _ { 1 , 2 } = 2 , r _ { 2 , 4 } = 3 ; \mathrm { b u t } , r _ { 1 , 4 } = 2 .$

3 (Adjusting inconsistencies) Applying Model 2 to the data and preference matrix yields: (Option 1) Obj1=1, Obj2=3.41, $u _ { 1 , 7 } = 1 , ( w _ { 1 } , w _ { 2 } , w _ { 3 } , w _ { 4 } ) = ( 0 . 2 6 , 0 . 6 4 , 0 . 0 5 , 0 . 0 5 ) , ( S _ { 1 } , S _ { 2 } , S _ { 3 } ,$ $S _ { 4 } , S _ { 5 } , S _ { 6 } , S _ { 7 } , S _ { 8 } ) = ( 0 . 6 0 , 0 . 3 8 , 0 . 5 6 , 0 . 1 3 , 0 . 2 0 , 0 . 3 4 , 0 . 4 1 , 0 . 7 8 )$ The values of unspeci<sup>fi</sup>ed preferences can be computed as: $r _ { 1 , 8 } = S _ { 1 } / S _ { 8 } = 0 . 7 6 , r _ { 2 , 5 } = 1 . 9 2 , r _ { 3 , 6 } = 1 . 6 5 , r _ { 4 , 8 } = 0 . 1 6 ,$ , and $r _ { 6 , 7 } = 0 . 8 1$ . Option 1 suggests reversing $r _ { 1 , 7 }$ from 0.5 to 1.44 $( S _ { 1 } / S _ { 7 } )$ to minimize both ordinal and cardinal inconsistencies. After adjustment, the CR for Option 1 is 4.9%. Option 2 can be obtained by adding a constraint $u _ { 1 , 7 } = 0$ into $\mathrm { M o d e l } 2 . \mathrm { O p t i o n } 2 \mathrm { y i e l d s } : O b j 1 = 1 , O b j 2 = 5 . 7 4 , u _ { 3 , 7 } = 1 , ( w _ { 1 } , w _ { 2 }$ $w _ { 3 } , w _ { 4 } ) = ( 0 . 2 2 , 0 . 1 0 , 0 . 6 3 , 0 . 0 5 ) , ( S _ { 1 } , S _ { 2 } , S _ { 3 } , S _ { 4 } , S _ { 5 } , S _ { 6 } , S _ { 7 } , S _ { 8 } ) =$ (0.59, 0.43, 0.54, 0.11, 0.13, 0.38, 0.61, 0.81). Option 2 suggests reversing $r _ { 3 , 7 }$ from 3 to 0.88 to adjust inconsistencies. After adjustment, the CR for Option 1 is 5.3%. Similarly, Option 3 can be acquired by adding two constraints $u _ { 1 , 7 } = 0$ and $u _ { 3 , 7 } = 0$ into Model 2. Option 3 yields: Obj1=1, Obj2=5.53, u =1, (w , w , $w _ { 3 } , w _ { 4 } ) = ( 0 . 1 7 , 0 . 1 3 , 0 . 6 5 , 0 . 0 5 ) , ( S _ { 1 } , S _ { 2 } , S _ { 3 } , S _ { 4 } , S _ { 5 } , S _ { 6 } , S _ { 7 } , S _ { 8 } ) =$ (0.56, 0.44, 0.58, 0.09, 0.12, 0.38, 0.58, 0.86). Option 3 suggests reversing $r _ { 1 , 3 }$ from 2 to 0.96 to improve inconsistencies. The CR after adjustment is 6.3%. The three options for adjustment are listed in Fig. 3(c).

After adjustment, the corresponding Gower Plots (all with faithfulness 90.26%) for Options 1, 2, and 3 are depicted in

![](/api/attachments/7FQ2ZMBU/fulltext/images/f5f584897e13dc9a0f86c210c6a10320da3527d5a7ca4b1d4310bb5f1d8f18f6.jpg)  
Fig. 3. Decision process of the store location example.

Fig. 3(d). Since all alternatives are evenly located on a $1 8 0 ^ { \circ }$ arc and the faithfulness approximates 1, the preference matrixes for three options are all ordinally consistent. The similarities between alternatives for each option can be calculated based on Expression (2).

Step 4 (Displaying alternatives) Applying the Decision Ball model (Model 3) to $S _ { i } ( \boldsymbol { \mathsf { w } } )$ and $\delta _ { i , j } ( \pmb { w } )$ yields the coordinates $\left( x _ { i } , y _ { i } , z _ { i } \right)$

of alternatives on the Decision Ball. The Decision Ball is then displayed to the decision maker. The corresponding Decision Balls for Options 1, 2, and 3 (with Stress 9.36%, 6.03%, and 5.26% respectively) are depicted in Fig. 3(e).

For Option 1, reversing $r _ { 1 , 7 } \mathrm { a s } r _ { 1 , 7 } { > } 1$ (means $A _ { 1 }$ is preferable to $A _ { 7 } )$ generates an ordinally consistent situation with $A _ { 8 } \succ A _ { 1 }$ y $A _ { 3 } \succ A _ { 7 } \succ A _ { 2 } \succ A _ { 6 } \succ A _ { 5 } \succ A _ { 4 } ;$ the corresponding Decision Ball illustrates this, considering $A _ { 8 } , \ A _ { 1 }$ and $A _ { 3 } , \ A _ { 8 } \ \succ \ A _ { 1 } \ \succ \ A _ { 3 } .$ However $A _ { 3 }$ is more similar t ${ \tt O A } _ { 8 }$ than $A _ { 1 }$ because the distance between $A _ { 3 }$ and $A _ { 8 }$ is shorter than that between $A _ { 1 }$ and $A _ { 8 } .$ Therefore, if the manager cannot rent $A _ { 8 }$ for business, $A _ { 3 }$ may be a similar choice than $A _ { 1 }$

For Option 2 (reversing $r _ { 3 , 7 } )$ , the corresponding Decision Ball illustrates that the ranks of alternatives are: $A _ { 8 } \mathrm { > } A _ { 7 } \mathrm { > } A _ { 1 } \mathrm { > } A _ { 3 } \mathrm { > }$ $A _ { 2 } { > } A _ { 6 } { > } A _ { 5 } { > } A _ { 4 }$ . Alternatives $A _ { 1 }$ and A are very close. Thus, if alternative $A _ { 8 }$ is impossible to rent for business then $A _ { 1 }$ as well as $A _ { 7 }$ could be a good choice. For Option 3 (reversing $r _ { 1 , 3 } )$ , the ranks of choices in this option are: $A _ { 8 } \mathrm { > } A _ { 3 } \mathrm { > } A _ { 7 } \mathrm { > } A _ { 1 } \mathrm { > } A _ { 2 } \mathrm { > } A _ { 6 } \mathrm { > }$ $A _ { 5 } { \succ } A _ { 4 }$

The manager can observe the ranks of alternatives and similarities among them on the Decision Ball, and make a <sup>fi</sup>nal decision.

## 5.2. An experiment

In order to evaluate the ef<sup>fi</sup>cacy of the proposed approach, we developed a prototype visualization system by applying the models proposed in Section 4. An experiment has been conducted to test the usefulness of the proposed approach in decision-making. Thirty-three subjects were recruited to participate in the experiment; all of them were undergraduate senior students. No subjects had any prior experience in using Gower Plots and Decision Balls. A training session was given to all of the subjects before they conducted the test. The training session included: (i) a 20-minute session for an introduction to the proposed approach, (ii) a 10-minutes practice section to allow subjects to become familiar with the tools.

In the experiment, all of the participants were asked to make a choice related to the decision issue: If possible, which graduate school would you prefer in order to resume your master's degree? Five graduate schools with similar reputations were chosen in advance for evaluation. All of the participants had to select the one that they most preferred among these <sup>fi</sup>ve graduate schools, based on the support of the proposed prototype system. After the experiment, all of the participants were required to <sup>fi</sup>ll out a questionnaire. The questionnaire consists of 3 items rated on a <sup>fi</sup>ve-point Likert-type scale, as follows:

1. Does the proposed approach provide visual aids to help you observe background information?

2. Does the proposed approach enhance your con<sup>fi</sup>dence in decision making?

3. Is the proposed approach helpful for decision making?

Thirty-one (94%) out of thirty-three participants agreed that the proposed approach provided visual aids to help them observe background information. Twenty-eight (85%) participants agreed that the proposed approach enhanced their con<sup>fi</sup>dence in regard to decision making. Twenty-<sup>fi</sup>ve (76%) participants agreed that the proposed approach was helpful for decision making. This test supports the usefulness of the proposed approach.

## 6. Conclusions

This study develops a visualization approach which can assist decision makers in ranking alternatives involving inconsistent preferences. Gower Plots are adopted to detect alternatives involving major inconsistencies. An adjusting model is developed to provide suggestions for simultaneously improving ordinal and cardinal inconsistencies. After that, a Decision Ball model is applied to assist in visualizing the background context of alternatives. Decision makers can detect inconsistencies, choose the preferred way to adjust inconsistencies, observe relationships among alternatives, and then rank alternatives using a graphical and interactive interface.

The proposed approach can be extensively applied in many <sup>fi</sup>elds. Possible applications include: the selection of suppliers in supply chain management, evaluation of partners in virtual enterprises, ranks of promotion plans in marketing, analysis of investment decisions in <sup>fi</sup>nance, choices in personal decision-making etc. The proposed approach can also be conveniently developed into a decision support system. In future studies, determining how to provide a graphical method for adjusting inconsistencies could be addressed.

## Acknowledgement

This research is supported by the National Science Council of the Republic of China under contract NSC 99-2410-H-239-004.

## Appendix A. (Mathematical properties of Gower Plots [7])

The singular values of a matrix M of rank n are the positive square roots of the eigenvalues of the symmetric matrix M<sup>t</sup>M, where M<sup>t</sup> stands for transposition of M. If M is skew-symmetric, i.e. ${ \bf M } ^ { t } = - { \bf M } ,$ the singular values of the matrix M are equal to the norm of its purely imaginary eigenvalues.

Let $\lambda _ { 1 } \ge . . . \ge \lambda _ { m } \ge 0$ (and $\lambda _ { m + 1 } = 0$ if n is an odd number) represent those singular values, with m indicating the integer part of $n / 2$ . Using singular value decomposition [10], a skewsymmetric matrix M can be decomposed into the form

$$
\mathbf {M} = \sum_ {j = 1} ^ {m} \lambda_ {j} \left(\mathbf {U} _ {2 j - 1} \mathbf {U} _ {2 j} ^ {t} - \mathbf {U} _ {2 j} \mathbf {U} _ {2 j - 1} ^ {t}\right)
$$

where $\mathrm { U } _ { 2 j - 1 }$ and $\mathrm { U } _ { 2 j }$ are orthonormal eigenvectors of M<sup>t</sup>M corresponding to $\lambda _ { j } ^ { 2 }$ .

The matrix $\mathbf { M } ^ { * } = \lambda _ { 1 } ( \mathbf { U } \mathbf { V } ^ { t } - \mathbf { V } \mathbf { U } ^ { t } )$ with $\mathrm { U } = \mathrm { U } _ { 1 }$ and $\mathsf { V } = \mathsf { U } _ { 2 }$ provides <sup>Þ</sup>the best approximation of a skew-symmetric matrix M of rank two, because the <sup>fi</sup>rst term of M gives the best least-squares <sup>fi</sup>t of rank two to M. $\operatorname { L e t } \operatorname { U } = ( u _ { 1 } , . . . , u _ { n } ) ^ { \mathrm { t } }$ and $\mathsf { V } = ( \nu _ { 1 } , . . . , \nu _ { n } ) ^ { t }$ as n points $P _ { j } = ( u _ { j } , v _ { j } )$ in the plane. A Gower Plot of a skew-symmetric matrix M is a twodimensional graph composed of all $P _ { j } , 1 { \le } j { \le } n$ , on the graph.

M is provided by variability $\mathbf { \tau } = \frac { | | \mathbf { M } ^ { * } | | } { | | \mathbf { M } | | } = \frac { \lambda _ { 1 } ^ { 2 } } { \underset { j = 1 } { \sum } } .$ References

[1] V. Belton, T.J. Stewart, Multiple criteria decision analysis, An Integrated Approach, Kluwer Academic Publishers, Norwell, MA, 2002.

[2] C.M. Brugha, Phased multicriteria preference <sup>fi</sup>nding, European Journal of Operational Research 158 (2004) 308–316.

[3] B. Chandran, B. Golden, E. Wasil, Linear programming models for estimating weights in the analytic hierarchy process, Computers & Operations Research 32 (2005) 2235–2254.

[4] W.D. Cook, B. Golany, M. Kress, M. Penn, T. Raviv, Optimal allocation of proposals to reviewers to facilitate effective ranking, Management Science 51 (4) (2005) 655–661.

[5] T.F. Cox, M.A.A. Cox, Multidimensional Scaling, Chapman & Hall, London, 2000.

[6] Y. Fassin, Imperfections and shortcomings of the stakeholder model's graphical representation, Journal of Business Ethics 80 (4) (2008) 879–888.

[7] C. Genest, S.S. Zhang, A graphical analysis of ratio-scaled paired comparison data, Management Science 42 (3) (1996) 335–349.

[8] J.C. Gower, The analysis of asymmetry and orthogonality, in: J.-R. Barra, F. Brodeau, G. Romier, B. Van Cutsem (Eds.), Recent Developments in Statistics, North-Holland.Amsterdam. 1977 pp. 109-123

[9] D.S. Hochbaum, A. Levin, Methodologies and algorithms for group-rankings decision, Management Science 52 (9) (2006) 1394–1408.

[10] R.A. Horn, C.R. Johnson, Matrix Analysis, Cambridge University Press, London, 1985.

[11] W. Jank, P.K. Kannan, Understanding geographical markets of online <sup>fi</sup>rms using spatial models of customer choice Marketing science 24 (4) (2005) 623–634

[12] C. Kahraman, I. Kaya, A fuzzy multicriteria methodology for selection among energy alternatives Expert Systems with Applications 37 (2010) 6270–6281

[13] R.L. Keeney, Common mistakes in making value trade-offs, Operations Research 50 (6) (2002) 935–945.

[14] M.Y. Kiang, Extending the Kohonen self-organizing map networks for clustering analysis Computations Statistics and Data Analysis 38 (2001) 161–180

[15] T. Kohonen, Self-organizing maps, Springer, Berlin, 1995.

[16] J.B. Kruskal, Non-metric multidimensional scaling: a numerical method, Psychometrica 29 (1964) 115–129.

[17] H.L. Li, L.C. Ma, Detecting and adjusting ordinal and cardinal inconsistencies through a graphical and optimal approach in AHP models, Computers and Operations Research 34 (2007) 780–798.

[18] H.L. Li, L.C. Ma, Visualizing decision processes on spheres based on the even swap concept, Decision Support Systems 45 (2008) 354–367.

[19] L.C. Ma, Visualizing preferences on spheres for group decisions based on multiplicative preference relations, European Journal of Operational Research 203 (2010) 176–184.

[20] A. Maas, T. Bezembinder, P. Wakker, On solving intransitivities in repeated pairwise choices, Mathematical Social Sciences 29 (1995) 83–101.

[21] T.L. Saaty, The analytic hierarchy process, McGraw-Hill, New York, 1980.

[22] T.L. Saaty, L.G. Vargas, Comparison of eigenvalue, logarithmic least squares and least squares methods in estimating ratios, Mathematical Modeling 5 (1984) 309–324.

[23] L.M. Seiford, J. Zhu, Context-dependent data envelopment analysis – measuring attractiveness and progress, OMEGA 31 (5) (2003) 397–408.

[24] D. Sullivan, Cognitive tendencies in international business research: implications of a ‘narrow vision’, Journal of International Business Studies 29 (4) (1998) 837–862.

[25] M. Tam, V.M. Rao Tummala, An application of the AHP in vendor selection of a telecommunications system, OMEGA 29 (2001) 171–182.

[26] A. Tversky, I. Simonson, Context-dependent preferences, Management Science 39 (10) (1993) 1179–1189.

[27] N. Worren, K. Moore, R. Elliott, When theories become tools: toward a framework for pragmatic validity, Human Relations 55 (10) (2002) 1227–1249.

[28] B. Zhu, S. Watts, H. Chen, Visualizing social network concepts, Decision Support Systems 49 (2010) 151–161.

Li-Ching Ma is an Associate Professor in the Department of Information Management at National United University, Taiwan. She received her PhD degree in Information Management from National Chiao Tung University, Taiwan. Her research interests include decision-making, visualization, and optimization. Her articles have appeared in Decision Support Systems, Computers & Operations Research, European Journal of Operational Research, OMEGA, Asia-Paci<sup>fi</sup>c Journal of Operational Research etc

Han-Lin Li is a Chair Professor of National Chiao Tung University, Taiwan. He received his PhD degree from University of Pennsylvania, USA. His articles have appeared in Operations Research, Decision Support Systems, Fuzzy Sets and Systems, Journal of the Operational Research Society, European Journal of Operational Research, Journal of Global Optimization, Computers and Operational Research, and many other publications.
