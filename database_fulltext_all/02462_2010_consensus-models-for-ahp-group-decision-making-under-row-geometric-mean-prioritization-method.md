---
otero_id: 2462
otero_key: "VAJ8KGG5"
title: "Consensus models for AHP group decision making under row geometric mean prioritization method"
authors: "Yucheng Dong; Guiqing Zhang; Wei-Chiang Hong; Yinfeng Xu"
year: "2010"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2010.03.003"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Consensus models for AHP group decision making under row geometric mean prioritization method

Yucheng Dong <sup>a,b,</sup>⁎, Guiqing Zhang <sup>a</sup>, Wei-Chiang Hong <sup>b</sup>, Yinfeng Xu <sup>a,c</sup>

<sup>a</sup> Management School, The Key Lab of the Ministry of Education for Process Control and Efficiency Projects, Xi'an Jiaotong University, Xi'an 710049, China

<sup>b</sup> Department of Information Management, Oriental Institute of Technology, No. 58, Section 2, Sichuan Road, Panchiao, Taipei 220, Taiwan

<sup>c</sup> State Key Lab for Manufacturing Systems Engineering, Xi'an 710049, China

## a r t i c l e i n f o

Article history: Received 29 August 2009 Received in revised form 3 March 2010 Accepted 21 March 2010 Available online 27 March 2010

Keywords: Group decision making AHP Row geometric mean prioritization method Geometric consistency index Consensus

## a b s t r a c t

The consistency measure is a vital basis for consensus models of group decision making using preference relations, and includes two subproblems: individual consistency measure and consensus measure. In the analytic hierarchy process (AHP), the decision makers express their preferences using judgement matrices (i.e., multiplicative preference relations). Also, the geometric consistency index is suggested to measure the individual consistency of judgement matrices, when using row geometric mean prioritization method (RGMM), one of the most extended AHP prioritization procedures. This paper further de<sup>fi</sup>nes the consensus indexes to measure consensus degree among judgement matrices (or decision makers) for the AHP group decision making using RGMM. By using Chiclana et al.'s consensus framework, and by extending Xu and Wei's individual consistency improving method, we present two AHP consensus models under RGMM. Simulation experiments show that the proposed two consensus models can improve the consensus indexes of judgement matrices to help AHP decision makers reach consensus. Moreover, our proposal has two desired features: (1) in reaching consensus, the adjusted judgement matrix has a better individual consistency index (i.e., geometric consistency index) than the corresponding original judgement matrix; (2) this proposal satis<sup>fi</sup>es the Pareto principle of social choice theory.

© 2010 Elsevier B.V. All rights reserved.

## 1. Introduction

Preference relations are widely used in group decision making. According to element forms in preference relations, there are often two kinds of preference relations: linguistic preference relations [17,27,28] and numerical preference relations (i.e., multiplicative preference relations [26,37,42] and fuzzy preference relations [11,12,20,22,40]). In general, group decision making problems using preference relations are faced by applying two different models (or processes) before a <sup>fi</sup>nal solution can be given [29,30]: 1) the selection model and 2) the consensus model. The selection model obtains the <sup>fi</sup>nal solution according to the preferences given by the decision makers. It involves two different steps: aggregation of individual preferences and exploitation of the collective preference.

The consensus model is an important aspect in group decision making [5,6,9,10,13,16,27,29,30,44]. Classically, consensus is de<sup>fi</sup>ned as the full and unanimous agreement of all the decision makers regarding all the possible alternatives. However, some researchers consider that complete agreement is not necessary in real life. This has led to the use of the consistency measure, which also is called “soft”

consensus degree in [27,29,30]. The consistency measure is used to measure the difference among decision makers, and is a vital basis of consensus models. For group decision making using preference relations, the consistency measure itself includes two subproblems [31]:

1. When can a decision maker, considered individually, be said to be consistent and

2. When can a whole group of decision makers be considered consistent.

In this paper, we call the <sup>fi</sup>rst subproblem individual consistency measure, and the second subproblem consensus measure. Generally, at the beginning for each group decision making problem, decision makers’ opinions may differ from each other substantially. And, consensus models are decision aid tools to help decision makers to reach consensus, based on the established consistency measure.

In the analytic hierarchy process (AHP) [37], multiplicative preference relations are called judgement matrices, and adopted to express the decision makers’ preferences. Many researchers [1,7,18,23,32,34–36,39,41,46] focus on the selection model in AHP group decision making (i.e., aggregation rules and prioritization methods). Two of the methods that have been found to be the most useful in AHP group decision making are the aggregation of individual judgments (AIJ) and the aggregation of individual priorities (AIP). AIJ follows the common resolution scheme of selection models, as mentioned above. In the aggregation phase of AIJ, the weighted geometric mean method is used to aggregating individual judgement matrices to obtain a collective judgement matrix. In the exploitation phase of AIJ, prioritization methods, such as eigenvalue method (EM) [38] and row geometric mean method (RGMM) [14], are used to derive a priority vector to order collective judgement matrix. AIP has differences in the common resolution scheme among other selection models. The weighted geometric mean method is employed to aggregate individual priorities derived using prioritization methods, to obtain the best alternative(s).

The consistency problem is also a critical step in AHP group decision making [2,8,19,21,24,33,34,38,43,45]. A number of studies focus on individual consistency in AHP. Saaty [37] develops an individual consistency index based on the EM. Crawford and Williams [14] propose an individual consistency index based on RGMM. Aguarón et al. [2] call Crawford and Williams's consistency index the geometric consistency index, and provide the thresholds associated with it. Many approaches [8,21,24,38,45] have been developed to aid the AHP decision makers to revise the individual inconsistency in judgement matrices. There are fewer studies about the consensus building for AHP group decision making. Bryson [7], Moreno-Jiménez et al. [34] and Van den Honert [41] also introduce several interesting approaches for consensus building in AHP.

In general, research progress in group decision making using preference relations can bene<sup>fi</sup>t research in AHP. Recently, the consensus problem has become a hot topic in group decision making using preference relations. In particular, Chiclana et al. [13] present a framework for integrating individual consistency into consensus model. Inspired by Chiclana et al.'s study [13], this paper develops AHP consensus models under RGMM. This paper is organized as follows. In Section 2, we introduce some preliminary knowledge of AHP. In Section 3, we de<sup>fi</sup>ne the consensus indexes (i.e., the geometric cardinal consensus index and the geometric ordinal consensus index) for AHP, and export Chiclana et al.'s consensus framework to AHP. In Section $^ { 4 , }$ we develop two AHP consensus models under Chiclana et al's framework and RGMM, and show some desired properties of the proposed consensus models. In Section $5 ,$ an illustrative example is provided. Concluding remarks and future research agenda are presented in Section 6.

## 2. Preliminary knowledge

## 2.1. Prioritization method

Let $A = ( a _ { i j } ) _ { n \times n } ,$ where $a _ { i j } { > } 0$ and $a _ { i j } \times a _ { j i } = 1$ , be a judgement matrix. The prioritization method refers to the process of deriving a priority vector $w = ( w _ { 1 } , . . . , w _ { n } ) ^ { T }$ , where $w _ { i } \ge 0$ and $\sum _ { i = 1 } ^ { n } w _ { i } = 1$ , from the judgement matrix A. Two most commonly used prioritization methods (EM and RGMM) are listed below.

(1) The eigenvalue method

Saaty [37,38] proposes the principal eigenvector of A as the desired priority vector w, which can be obtained by solving the linear system:

$$
A w = \lambda w, e ^ {T} w = 1,
$$

where λ is the principal eigenvalue of A.

(2) Row geometric mean method

The RGMM uses the $L ^ { 2 }$ metric in de<sup>fi</sup>ning an objective function of the following optimization problem:

$$
\left\{ \begin{array}{l} \min \sum_ {i = 1} ^ {n} \sum_ {j > i} \left[ \ln \left(a _ {i j}\right) - \left(\ln (w _ {i}) - \ln \left(w _ {j}\right)\right) \right] ^ {2} \\ s. t. w _ {i} \geq 0, \sum_ {i = 1} ^ {n} w _ {i} = 1 \end{array} \right..
$$

Crawford and Williams [14] have shown that the solution to the above problem is unique and can be simply found as the geometric means of the rows of matrix A:

$$
w _ {i} = \frac {\sqrt [ 1 / n ]{\prod_ {j = 1} ^ {n} a _ {i j}}}{\sum_ {i = 1} ^ {n} \left(\sqrt [ 1 / n ]{\prod_ {j = 1} ^ {n} a _ {i j}}\right)}.
$$

The RGMM is also called the logarithmic least squares method.

Dong et al. [15] and Herman and Koczkodaj [25] show that the effects of these two prioritization methods are very similar. Moreover, the computational times of EM and RGMM are $o ( n ^ { 2 } )$ and $o ( n ) ,$ , respectively. Thus, RGMM has a less computational time than EM, and we select RGMM as the prioritization method in this paper.

## 2.2. AIJ and AIP

Consider an AHP group decision making problem. Let $D = \{ d _ { 1 } , d _ { 2 } , . . . , d _ { m } \}$ be the set of decision makers, and $\lambda { = } \{ \lambda _ { 1 } , \lambda _ { 2 } { , } { \ldots } , \lambda _ { m } \}$ be the weight vector of decision makers, where $\lambda _ { k } { > } 0 , k { = } 1 , 2 { , } { . } { . } { . } , m , \ \sum _ { k { = } 1 } ^ { m } \lambda _ { k } { = } 1$ . Let $A ^ { ( k ) } =$ $( a _ { i j } ^ { ( k ) } ) _ { n \times n }$ be the judgment matrix provided by the decision maker $d _ { k }$ $( k { = } 1 , 2 , . . . , m )$ . As mentioned above, two of the methods that have been found to be the most useful in AHP group decision making are AIJ and AIP. In AIJ and AIP, the weighted geometric mean method is generally used as the aggregation procedure.

(1) The aggregation of individual judgments

For AIJ, the decision makers use the weighted geometric mean method to aggregate individual judgement matrices to obtain a collective judgement matrix, $\begin{array} { r } { \dot { A ^ { ( c ) } } = \dot { ( } a _ { i j } ^ { ( c ) } ) _ { n \times n } , } \end{array}$ where

$$
a _ {i j} ^ {(c)} = \prod_ {k = 1} ^ {m} \left(a _ {i j} ^ {(k)}\right) ^ {\lambda_ {k}}.
$$

Then, we use certain prioritization method to derive a collective priority vector $\boldsymbol { w } ^ { ( c ) } \dot { = } ( w _ { 1 } ^ { ( c ) } , w _ { 2 } ^ { ( c ) } , . . . , w _ { n } ^ { ( c ) } ) ^ { T }$ from $A ^ { ( c ) }$ to order the alternatives.

(2) The aggregation of individual priorities

Let $\boldsymbol { w } ^ { ( k ) } { = } ( w _ { 1 } ^ { ( k ) } { , { \ldots } } , w _ { n } ^ { ( k ) } ) ^ { T }$ be the individual priority vector derived from individual judgment matrix $A ^ { ( k ) }$ using certain prioritization method. Then, the collective priority vector obtained using AIP is $\boldsymbol { w } ^ { ( c ) } = ( w _ { 1 } ^ { ( c ) } , w _ { 2 } ^ { ( c ) } , . . . , w _ { n } ^ { ( c ) } ) ^ { T }$ , where,

$$
w _ {i} ^ {(c)} = \frac {\prod_ {k = 1} ^ {m} \left(w _ {i} ^ {(k)}\right) ^ {\lambda_ {k}}}{\sum_ {i = 1} ^ {n} \prod_ {k = 1} ^ {m} \left(w _ {i} ^ {(k)}\right) ^ {\lambda_ {k}}}.
$$

When selecting EM as the prioritization method, some researchers have some disputes on the use of the AIJ and the AIP. Ramanathan and Ganesh [35] observe that AIJ violates the Pareto principle of social choice theory [3], and suggest using AIP in AHP group decision making. Forman and Peniwati [23] argue that AIJ and AIP are philosophically different circumstances [8], and whether AIJ or AIP should be used depended on whether the group intends to behave as a synergistic unit or as a collection of individuals. However, when selecting RGMM as the prioritization method, Barzilai and Golany [4] have shown the equivalence between AIJ and AIP (see Lemma 1).

Lemma 1. Let $\pmb { w } ^ { ( c ) } = ( \pmb { w } _ { 1 } ^ { ( c ) } , \pmb { w } _ { 2 } ^ { ( c ) } , . . . , \pmb { w } _ { n } ^ { ( c ) } ) ^ { T }$ and $\boldsymbol { w } ^ { ( c ^ { \prime } ) } = ( w _ { 1 } ^ { ( c ^ { \prime } ) } , w _ { 2 } ^ { ( c ^ { \prime } ) } , . . . , w _ { n } ^ { ( c ^ { \prime } ) } ) ^ { T }$ be two collective priority vectors, derived using AIJ and AIP under RGMM, respectively. Then $w _ { i } ^ { ( c ) } { = } w _ { i } ^ { ( c ^ { \prime } ) } , f o r i { = } 1 , 2 { , } { \ldots } n$

AIP doesn't violate the Pareto principle of social choice theory, so, based on Lemma 1, we have that AIJ satis<sup>fi</sup>es the Pareto principle of social choice theory under RGMM (see Corollary 1).

Corollary 1. Let $\boldsymbol { w } ^ { ( k ) } = ( w _ { 1 } ^ { ( k ) } , . . . , w _ { n } ^ { ( k ) } ) ^ { T }$ and $\boldsymbol { w } ^ { ( c ) } = ( w _ { 1 } ^ { ( c ) } , w _ { 2 } ^ { ( c ) } , . . . , w _ { n } ^ { ( c ) } ) ^ { T }$ be as before. Then, $i f w _ { i } ^ { ( k ) } { \geq } w _ { j } ^ { ( \dot { k } ) } f o r k { = } 1 , 2 { , } { \ldots } , m$ , then $w _ { i } ^ { ( c ) } { \geq } w _ { j } ^ { \top { c } ) }$

## 3. The consensus problem in AHP

## 3.1. Consistency measures in AHP

As indicated in previous sections, the problem of consistency measure itself includes two subproblems: individual consistency and consensus measure. For the RGMM, Crawford and Williams [14] and Aguarón et al. [2] have developed a consistency index to measure individual consistency, namely the geometric consistency index (GCI) (see De<sup>fi</sup>nition 1).

De<sup>fi</sup>nition 1. (Crawford and Williams [14]). Let $A = ( a _ { i j } ) _ { n \times n }$ be a judgement matrix, and let $\boldsymbol { w } = ( w _ { 1 } , w _ { 2 } , . . . , w _ { n } ) ^ { T }$ be the priority vector derived from A using the RGMM. The geometric consistency index (GCI) is given by

$$
G C I (A) = \frac {2}{(n - 1) (n - 2)} \sum_ {i <   j} \left(\log \left(a _ {i j}\right) - \log \left(w _ {i}\right) + \log \left(w _ {j}\right)\right) ^ {2}.
$$

When $G C I ( A ) = 0 ,$ , we consider A fully consistent. Aguarón et al. [2] also provide the thresholds (GCI) for GCI: $\overline { { G C I } } = 0 . 3 1$ for $n = 3 ;$ $\overline { { G C I } } = 0 . 3 5$ for $n { = } 4$ and $G C I = 0 . 3 7$ for $n { > } 4 .$ . When $G C I ( A ) { < } \overline { { G C I } }$ , we <sup>ð Þ</sup>consider that the matrix A is of acceptably individual consistency.

In general, the computation of the consensus indexes for group decision making using preference relations is done by measuring the distance between individual preference values and collective preference values [5,6,13,16]. Inspired by this idea, we de<sup>fi</sup>ne the geometric cardinal consensus index for AHP group decision making using RGMM (see De<sup>fi</sup>nition 2).

De<sup>fi</sup>nition 2. Let $A ^ { ( k ) } = ( a _ { i j } ) _ { n \times n } ^ { ( k ) }$ be the judgement matrix provided by the decision makers $d _ { k } ,$ and $\boldsymbol { w } ^ { ( c ) } = \{ w _ { 1 } ^ { ( \bar { c } ) } , w _ { 2 } ^ { ( \bar { c } ) } , . . . , w _ { n } ^ { ( c ) } \} ^ { T }$ be the collective priority vectors, derived from $\{ A ^ { ( 1 ) } , \ A ^ { ( \bar { 2 } ) } , . . . , A ^ { ( m ) } \}$ using AIJ under RGMM. Then, the geometric cardinal consensus index (GCCI) of $\cdot _ { A } k$ is de<sup>fi</sup>ned by

$$
G C C I \left(A ^ {(k)}\right) = \frac {2}{(n - 1) (n - 2)} \sum_ {i <   j} \left(\log \left(a _ {i j} ^ {(k)}\right) - \log \left(w _ {i} ^ {(c)}\right) + \log \left(w _ {j} ^ {(c)}\right)\right) ^ {2}.
$$

If $G C C I ( A ^ { k } ) = 0 ,$ then the kth decision maker is of fully cardinal consensus with the collective preference. Otherwise, the smaller the value of $G C C I ( A ^ { k } )$ , the more the cardinal consensus. According to the actual situation, the decision makers establish the thresholds GCCI for $G C C I ( A ^ { ( k ) } )$ . If ∀k $G C C I ( A ^ { ( k ) } ) { \leq } \overline { { G C C I } }$ , we conclude that the acceptably cardinal consensus are reached among the decision makers.

Let $w ^ { ( k ) } { = } ( w _ { 1 } ^ { ( k ) } { , } . . . , w _ { n } ^ { ( k ) } ) ^ { T }$ be the individual priority vector derived from the judgment matrix $A ^ { ( k ) }$ using RGMM, and let $\boldsymbol { \nu } ^ { ( k ) } \overset { \sim } = ( \nu _ { 1 } ^ { ( k ) } , . . . , \nu _ { n } ^ { ( k ) } ) ^ { I }$ , where $\nu _ { i } ^ { ( k ) }$ is the position of the ith alternative in $w ^ { ( k ) } .$ . For example, if $w ^ { ( k ) } =$ $( 0 . 3 , 0 . 2 , 0 . 5 ) ^ { T } ,$ then $\nu ^ { ( k ) } = ( 2 , 3 , 1 ) ^ { T }$ . Let $\pmb { w } ^ { ( c ) } = ( \pmb { w } _ { 1 } ^ { ( c ) } , \pmb { w } _ { 2 } ^ { ( c ) } , . . . , \hat { \pmb { w } } _ { n } ^ { ( c ) } ) ^ { T }$ be the collective priority vector, derived from $\{ A ^ { ( 1 ) } , A ^ { ( 2 ) } , . . . , A ^ { ( n ) } \}$ using AIJ under RGMM, and let $\overline { { \nu } } ^ { ( c ) } = ( \nu _ { 1 } ^ { ( c ) } , . . . , \nu _ { n } ^ { ( c ) } ) ^ { T }$ , where $\nu _ { i } ^ { ( c ) }$ is the position of the ith alternative in $w ^ { ( c ) } .$ . Herrera-Viedma et al. [29,30] propose the comparison approach of positions of alternatives between two preferences vectors to measure the consensus degree. Inspired by this idea, we de<sup>fi</sup>ne the geometric ordinal consensus index for AHP group decision making using RGMM (see De<sup>fi</sup>nition 3).

De<sup>fi</sup>nition 3. Let $w ^ { ( k ) } , w ^ { ( c ) } , \nu ^ { ( k ) }$ and $\boldsymbol { \nu } ^ { ( c ) }$ be as before. The geometric ordinal consensus index (GOCI) of $A ^ { k }$ is de<sup>fi</sup>ned by

$$
G O C I \left(A ^ {(k)}\right) = \frac {1}{n} \sum_ {i = 1} ^ {n} \left| v _ {i} ^ {(k)} - v _ {i} ^ {(c)} \right|.
$$

If $G O C I ( A ^ { k } ) = 0 .$ , then the kth decision maker is of fully ordinal consensus with the collective preference. Otherwise, the smaller the value of $G O C I ( A ^ { k } )$ , the more the ordinal consensus. According to the actual situation, the decision makers also may establish the thresholds

$$
G O C I (A ^ {(k)})
$$

$$
G O C I (A ^ {(k)}) \leq \overline {{G O C I}}
$$

Remark 1. Let $Q = \{ ( w _ { 1 } , w _ { 2 } , . . . , w _ { n } ) ^ { T } | 0 \leq w _ { i } \leq 1 , \sum _ { i = 1 } ^ { n } w _ { i } = 1 \}$ . According to De<sup>fi</sup>nition 1 and De<sup>fi</sup>nition 2, we have that $G C I ( A ) =$ $\begin{array} { r } { \frac { 2 } { ( n - 1 ) ( n - 2 ) } \underset { \substack { w \in Q } } { \operatorname* { m i n } } \sum _ { i < j } \big ( \log ( a _ { i j } ) - \log { ( w _ { i } ) } + \log { ( w _ { j } ) } \big ) ^ { 2 } \le G C C I ( A ) } \end{array}$ . Thus, we suggest ${ \overline { { G C C I } } } { \geq } { \overline { { G C I } } } .$ . Moreover, $\mathrm { i f ~ } G O C I ( \mathrm { A } ) \neq 0 ,$ , then $G O C I ( A ) { \geq } { \frac { 2 } { n } } .$ So, we also sugges ${ \overline { { G O C I } } } \geq _ { \overline { { n } } } ^ { 2 } .$ It may be an interesting future research issue to investigate the thresholds of GCCI and GOCI in details.

## 3.2. Exporting Chiclana et al.'s consensus framework to AHP

Recently, the consensus problem has become a hot topic in group decision making using preference relations. In particular, Chiclana et al. [13] present a framework for integrating individual consistency into consensus model. When exporting Chiclana et al.'s consensus framework to the AHP group decision making under RGMM, the implementation of this framework deals with a two-step procedure (see Fig. 1).

(1) Individual consistency improving method. The individual consistency improving method <sup>fi</sup>rstly uses GCI to measure the individual consistency degree of judgement matrices $A ^ { ( k ) }$ $k { = } 1 , 2 { \mathrm { , . . . , } } m . \operatorname { I f } G C I ( A ^ { ( k ) } ) { \leq } \overline { { G C I } }$ , it doesn't adjust $A ^ { ( k ) }$ . Otherwise, it helps the decision maker $d _ { k }$ improve the GCI values of $A ^ { ( k ) }$

(2) Consensus model. Once all judgement matrices are of acceptably individual consistency, we apply a consensus model to reach acceptable consensus. The consensus model <sup>fi</sup>rstly uses GCCI (or GOCI) to measure the consensus degree of judgement matrices $A ^ { ( k ) } , k = 1 , 2 , . . . , m$ . If $G C C I ( A ^ { ( k ) } ) { \leq } \overline { { G C C I } }$ (or $G O C I ( A ^ { ( k ) } ) { \leq } \overline { { { G O C I } } } ) , k { = } 1 , 2 { , } { \ldots } , m$ , it doesn't adjust $A ^ { ( \acute { k } ) } , k = 1 , 2 , \cdots ,$ m. Otherwise, it helps the decision makers to reach acceptable consensus. Finally, all judgement matrices $A ^ { ( k ) } , k = 1 , 2 , \dotsc , \overline { { m } } ,$ , are of acceptably individual consistency and are of acceptable consensus.

In the AHP discipline, individual consistency improving methods are very widely investigated [8,21,24,38,45]. The RGMM version of Xu and Wei's individual consistency improving method [45] is discussed in Appendix A.1, and is adopted to deal with individual inconsistency of judgement matrices in this paper. However, only a few researchers have discussed AHP consensus models. This paper mainly focuses on AHP consensus models under RGMM. When the AHP decision makers reach consensus under Chiclana et al.'s framework and RGMM, we argue that the corresponding consensus model need satisfy the following properties:

![](/api/attachments/VAJ8KGG5/fulltext/images/f91cae2f973da01edfba4c1ee6b09de3661c61101780e0663a951381c8380a6a.jpg)  
Fig. 1. AHP consensus model under Chiclana et al.'s consensus framework

(1) it can improve the consensus indexes $( \mathrm { i . e . }$ , CCCI and COCI) of judgement matrices (or decision makers) to reach consensus,

(2) in reaching consensus, the adjusted judgement matrix has a better individual consistency index (i.e., GCI) than the corresponding original judgement matrix,

(3) and it doesn't violate the Pareto principle of social choice theory.

## 4. Consensus models in AHP

Under Chiclana et al.'s framework, once judgement matrices are of acceptably individual consistency, we need to further apply consensus models to help AHP decision makers reach consensus. In this section, we propose two AHP consensus models under Chiclana et al.'s framework and RGMM.

## 4.1. Consensus models

Let $\{ A ^ { ( 1 ) } , A ^ { ( 2 ) } , . . . , A ^ { ( m ) } \}$ and $\{ \lambda _ { 1 } , \lambda _ { 2 } , . . . , \lambda _ { m } \}$ be as before. Let $w ^ { ( k ) } = ( w _ { 1 } ^ { ( k ) } , \dots ,$ $w _ { n } ^ { ( k ) } ) ^ { T }$ be the individual priority vector derived from the judgment matrix $A ^ { ( k ) }$ using RGMM. Let $\pmb { w } ^ { ( c ) } = ( w _ { 1 } ^ { ( c ) } , w _ { 2 } ^ { ( c ) } , . . . , w _ { n } ^ { ( c ) } ) ^ { T }$ be the collective priority vector, derived from $\{ A ^ { ( 1 ) } , . . . , \dot { A } ^ { ( m ) } \}$ using AIJ under RGMM. In the subsection, we respectively propose two consensus models, based on GCCI and GOCI. Without loss of generality, suppose that the judgment matrix A<sup>τ</sup> has a largest cardinal (or ordinal) consensus index. The main step of the proposed consensus models is to construct a new judgement matrix A<sup>τ</sup> according to original judgement matrix A<sup>τ</sup>. When structuring $\overline { { A ^ { \tau } } } = \left( \overline { { a _ { i j } ^ { \tau } } } \right)$ , we suggest that

$$
\overline {{a _ {i j} ^ {(\tau)}}} = \left(a _ {i j} ^ {(\tau)}\right) ^ {\theta} \left(\frac {w _ {i} ^ {(c)}}{w _ {j} ^ {(c)}}\right) ^ {(1 - \theta)},
$$

where $0 { < } \theta { < } 1$ . Follow this procedure until judgment matrices with acceptable consensus are obtained or the established maximum number of iterations is obtained. Next, we describe these two consensus models in details.

## 4.1.1. Cardinal consensus model

Input: Judgment matrices $\{ A ^ { ( 1 ) } , A ^ { ( 2 ) } , . . . , A ^ { ( m ) } \}$ , the weight vector of decision makers $\{ \lambda _ { 1 } , \lambda _ { 2 } , . . . , \lambda _ { m } \}$ , the threshold GCCI, the established maximum number of iterations $z _ { \operatorname* { m a x } } 2 1$ and 0bθb1.

Output: Adjusted judgement matrices $\left\{ \overline { { { A ^ { ( 1 ) } } } } , \overline { { { A ^ { ( 2 ) } } } } , . . . , \overline { { { A ^ { ( m ) } } } } \right\}$ , the cardinal consensus index $G C C I \left( \overline { { A ^ { ( k ) } } } \right) ( k = 1 , 2 , . . . , m )$ , the collective $\overline { { w ^ { ( c ) } } } = \left( \overline { { w _ { 1 } ^ { ( c ) } } } , \overline { { w _ { 2 } ^ { ( c ) } } } , . . . , \overline { { w _ { n } ^ { ( c ) } } } \right) ^ { 1 }$ I priority vector , and the number of iterations z.

Step 1 Let $z = 0$ and $A _ { z } ^ { ( k ) } = ( a _ { i j z } ^ { ( k ) } ) _ { n \times n } = ( a _ { i j } ^ { ( k ) } ) _ { n \times n } ;$

Step 2 Let $w _ { z } ^ { ( c ) } = ( w _ { 1 . z } ^ { ( c ) } , w _ { 2 . z } ^ { ( c ) } , . . . , w _ { n , z } ^ { ( c ) } ) ^ { T }$ be the collective priority vector, derived from the collective judgement matrix $A _ { z } ^ { ( c ) } = ( a _ { i j z } ^ { ( c ) } )$ where $\begin{array} { r } { a _ { i j z } ^ { ( c ) } = \prod _ { k = 1 } ^ { m } ( a _ { i j z } ^ { ( k ) } ) ^ { \lambda _ { k } } } \end{array}$ , using RGMM.

<sup>ð Þ</sup>Step 3 Calculate the cardinal consensus index of $A _ { z } ^ { ( k ) }$ :

$$
\begin{array}{l} G C C I \left(A _ {z} ^ {(k)}\right) = \frac {2}{(n - 1) (n - 1)} \\ \sum_ {i <   j} \left(\log \left(a _ {i j z} ^ {(k)}\right) - \log \left(w _ {i, z} ^ {(c)}\right) + \log \left(w _ {j, z} ^ {(c)}\right) ^ {2}\right). \end{array}
$$

If ∀k, $G C C I ( A _ { z } ^ { ( k ) } ) { \leq } \overline { { G C C I } } \ \mathrm { o r } z { \geq } z _ { m a x } ,$ then go to Step $5 ;$ otherwise, <sup>ð Þ</sup>continue with the next step;

Step 4 Without loss of generality, suppose that

$$
G C C I \left(A _ {z} ^ {(\tau)}\right) = \max _ {k} \left\{G C C I (A _ {z} ^ {(k)} \right\}.
$$

Let $A _ { z + 1 } ^ { ( k ) } = ( a _ { i j , z + 1 } ^ { ( k ) } ) _ { n \times n } ,$ where

$$
a _ {i j, z + 1} ^ {(k)} = \left\{ \begin{array}{l l} \left(a _ {i j, z} ^ {(k)}\right) ^ {\theta} \left(\frac {w _ {i , z} ^ {(c)}}{w _ {j , z} ^ {(c)}}\right) ^ {(1 - \theta)} & k = \tau \\ a _ {i j, z} ^ {(k)} & k \neq \tau \end{array} \right.,
$$

and $z = z + 1$ . Then, go to Step 2.

Step 5 Let $\overline { { A ^ { ( k ) } } } = A _ { z } ^ { ( k ) }$ Þ and $\overline { { w ^ { ( c ) } } } = w _ { z } ^ { ( c ) }$ Þ. Output the adjusted judgement matrix $\overline { { A ^ { ( k ) } } }$ , its cardinal consensus index $G C C I { \left( \overline { { A ^ { ( k ) } } } \right) }$ , the collective priority vector $\overline { { w ^ { ( c ) } } }$ and the number of iterations z.

## 4.1.2. Ordinal consensus model

Input: Judgment matrices $\{ A ^ { ( 1 ) } , A ^ { ( 2 ) } , . . . , A ^ { ( m ) } \}$ , the weight vector of decision makers $\{ \lambda _ { 1 } , \lambda _ { 2 } , . . . , \lambda _ { m } \}$ , the threshold GOCI, and the established maximum number of iterations $z _ { \operatorname* { m a x } } 2 1$ and $0 { < } \theta { < } 1$

Output: Adjusted judgement matrices $\left\{ \overline { { \overline { { A ^ { ( 1 ) } } } } } , \overline { { \overline { { A ^ { ( 2 ) } } } } } , . . . , \overline { { \overline { { A ^ { ( m ) } } } } } \right\}$ , the ordinal consensus index $G O C I \left( \overline { { A ^ { ( k ) } } } \right) ^ { \downarrow } \left( k = 1 , 2 , . . . , m \right)$ , the collective priority vector $\overline { { \overline { { w ^ { ( c ) } } } } } = \left( \overline { { \overline { { w _ { 1 } ^ { ( c ) } } } } } , \overline { { \overline { { w _ { 2 } ^ { ( c ) } } } } } , . . . , \overline { { \overline { { w _ { n } ^ { ( c ) } } } } } \right) ^ { 1 }$ , and the number of iterations z.

Step 1 Let $z = 0$ and $A _ { z } ^ { ( k ) } = ( a _ { i j z } ^ { ( k ) } ) _ { n \times n } = ( a _ { i j } ^ { ( k ) } ) _ { n \times n } ;$

Step 2 Let $w _ { z } ^ { ( k ) } = ( w _ { 1 , z } ^ { ( k ) } , . . . , w _ { n , z } ^ { ( \bar { k } ) } ) ^ { T }$ be the individual priority vector derived from judgment matrix $A _ { z } ^ { ( k ) }$ using RGMM, and $v _ { z } ^ { ( k ) } =$ $( \nu _ { 1 , z } ^ { ( k ) } , . . . , \nu _ { n , z } ^ { ( k ) } ) ^ { T }$ , where $\nu _ { i , z } ^ { ( k ) }$ is the position of the ith alternative in $w _ { z } ^ { ( k ) } .$ . Let $\boldsymbol { w _ { z } ^ { ( c ) } } = ( w _ { 1 , z } ^ { ( c ) } , w _ { 2 , z } ^ { ( c ) } , . . . , w _ { n , z } ^ { ( c ) } ) ^ { T }$ be the collective priority vector, derived from the collective judgement matrix $A _ { z } ^ { ( c ) }$ where $\begin{array} { r } { a _ { i j z } ^ { ( c ) } = \prod _ { k = 1 } ^ { m } ( a _ { i j z } ^ { ( k ) } ) ^ { \lambda _ { k } } } \end{array}$ ; using RGMM, and $\nu _ { z } ^ { ( c ) } = ( \nu _ { 1 , z } ^ { ( c ) } , \dots$ $\nu _ { n , z } ^ { ( c ) } ) ^ { 1 }$ <sup>T</sup>, where $\nu _ { i , z } ^ { ( c ) }$ <sup>ð Þ</sup>is the position of alternative $x _ { i }$ in $\boldsymbol { w } ^ { ( c ) }$

Step 3 Calculate the ordinal consensus index

$$
G O C I (A _ {z} ^ {(k)}) = \frac {1}{n} \sum_ {i = 1} ^ {n} | v _ {i, z} ^ {(k)} - v _ {i, z} ^ {(c)} |,
$$

for $k = 1 , 2 , . . . , m$ . If ∀k, $G O C I ( A _ { z } ^ { ( k ) } ) { \leq } \overline { { G O C I } }$ or $z \geq z _ { \mathrm { m a x } } ,$ then go to <sup>ð Þ</sup>Step 5; otherwise, continue with the next step;

Step 4 Without loss of generality, suppose that

$$
G O C I \left(A _ {z} ^ {(\tau)}\right) = \max _ {k} \left\{G O C I \left(A _ {z} ^ {(k)}\right) \right\}.
$$

Let $A _ { z + 1 } ^ { ( k ) } = ( a _ { i j , z + 1 } ^ { ( k ) } ) _ { n \times n } ,$ where

$$
a _ {i j, z + 1} ^ {(k)} = \left\{ \begin{array}{c c} \left(a _ {i j, z} ^ {(k)}\right) ^ {\theta} \left(\frac {w _ {i , z} ^ {(c)}}{w _ {j , z} ^ {(c)}}\right) ^ {(1 - \theta)} & k = \tau \\ a _ {i j, z} ^ {(k)} & k \neq \tau \end{array} \right.,
$$

and $z = z + 1$ . Then, go to Step 2.

Step 5 Let $\overline { { \overline { { A ^ { ( k ) } } } } } = A _ { z } ^ { ( k ) }$ , and $\overline { { w ^ { ( c ) } } } = w _ { z } ^ { ( c ) }$ . Output the adjusted judgement matrix $\overline { { A ^ { ( k ) } } }$ , its ordinal consensus index $G O C I \biggl ( \overline { { { \overline { { A ^ { ( k ) } } } } } } \biggr )$ , the collective priority vector $w ^ { ( c ) }$ and the number of iterations z.

Remark 2. The ordinal consensus model and the cardinal consensus model have similarity with each other. The main difference between these two consensus models is using different consensus indexes. These two consensus models both are inspired by Xu and Wei's individual consistency method [45]. They reduce into the RGMM version of Xu and Wei's method, when the number of the decision makers $m = 1$

Remark 3. The proposed consensus models are arti<sup>fi</sup>cial consensus improving methods. We also may allow the decision makers to participate in consensus models. For example, if the decision maker with the worst consensus index does not wish to change his/her original preference values, we consider the decision maker with the second worst consensus index and repeat the process.

## 4.2. Properties of consensus models

In this subsection, we introduce some desired properties of the proposed consensus models. Before proposing these properties, we introduce Lemma 2, presented in Escobar et al. [19].

Lemma 2. (Escobar et al. [19]). Let $\{ A ^ { ( 1 ) } , A ^ { ( 2 ) } , . . . , A ^ { ( m ) } \} , \ : \{ \lambda _ { 1 } , \lambda _ { 2 } , . . . , \lambda _ { m } \}$ and $A ^ { ( c ) }$ be as before. Then, $G C I ( A ^ { ( c ) } ) { \leq }$ max $\big \{ G C I ( A ^ { ( k ) } ) \big \}$

Theorem 1. Let $\bigl \{ A ^ { ( 1 ) } , A ^ { ( 2 ) } , . . . , A ^ { ( m ) } \bigr \} , \left\{ \overline { { { A ^ { ( 1 ) } } } } , \overline { { { A ^ { ( 2 ) } } } } , . . . , \overline { { { A ^ { ( m ) } } } } \right\}$ and $\left\{ \overline { { \overline { { A ^ { ( 1 ) } } } } } , \overline { { \overline { { A ^ { ( 2 ) } } } } } , . . . , \overline { { \overline { { A ^ { ( m ) } } } } } \right\}$ be as before. Then, $G C I { \left( \overline { { A ^ { ( k ) } } } \right) } { \leq } G C I { \left( A ^ { ( k ) } \right) }$ and ${ \dot { G } } C I \left( { \overline { { A ^ { ( k ) } } } } \right) { \le } G C I \left( A ^ { ( k ) } \right)$ , for $k = 1 , 2 , . . . , m$

The proof of Theorem 1 is provided in Appendix A.2.

Theorem 1 guarantees the adjusted judgement matrix has a better individual consistency index (i.e., GCI) than the corresponding original judgement matrix, when using the proposed consensus models.

From Theorem 1, we have Corollary 2.

Corollary 2. Let $\overline { { A ^ { ( c ) } } }$ and $\overline { { \overline { { A ^ { ( c ) } } } } }$ be the collective judgement matrices of $\{ \overline { { A ^ { ( 1 ) } } } , \overline { { A ^ { ( 2 ) } } } , . . . , \overline { { A ^ { ( m ) } } } \}$ and $\{ \overline { { A ^ { ( 1 ) } } } , \overline { { A ^ { ( 2 ) } } } , . . . , \overline { { A ^ { ( m ) } } } \}$ , respectively. Then, $G C I ( \overline { { A ^ { ( c ) } } } ) { \leq } \overline { { G C I } }$ and $G C I ( \overline { { A ^ { ( c ) } } } ) { \leq } \overline { { G C I } }$ under the condition that $G C I ( A ^ { ( k ) } ) { \leq } \overline { { { G C I } } } f o r k { = } 1 , 2 { , } { . } { . } { . } { , } m .$

Theorem 2. Let $\{ A ^ { ( 1 ) } , A ^ { ( 2 ) } , . . . , A ^ { ( m ) } \} , w ^ { ( k ) } = \{ w _ { 1 } ^ { ( k ) } , w _ { 2 } ^ { ( k ) } , . . . , w _ { n } ^ { ( k ) } \} ( k = 1 , 2 , . . . ,$ m), $\overline { { w ^ { ( c ) } } } = \left\{ \overline { { w _ { 1 } ^ { ( c ) } } } , \overline { { w _ { 2 } ^ { ( c ) } } } , . . . , \overline { { w _ { n } ^ { ( c ) } } } \right\}$ and $\overline { { \overline { { w ^ { ( c ) } } } } } = \{ \overline { { w _ { 1 } ^ { ( c ) } } } , \overline { { w _ { 2 } ^ { ( c ) } } } , . . . , \overline { { w _ { n } ^ { ( c ) } } } \}$ be as before. Then, i $\lceil w _ { i } ^ { ( k ) } > w _ { j } ^ { ( k ) }$ , for $k = 1 , 2 , . . . , m$ , we have that $\overline { { w _ { i } ^ { ( c ) } } } > \overline { { w _ { j } ^ { ( c ) } } }$ and $\overline { { w _ { i } ^ { ( c ) } } } > \overline { { w _ { j } ^ { ( c ) } } }$

The proof of Theorem 2 is provided in Appendix A.2.

Theorem 2 guarantees the proposed consensus models satisfy the Pareto principle of social choice theory.

## 4.3. Discussion on convergence of the consensus models

Naturally, we hope that the proposed consensus models can improve the consensus indexes (i.e., GCCI and GOCI) of judgement matrices to help the decision makers reach consensus. In the following, we use simulation methods to study this issue. The main idea of the simulation methods is to randomly generate decision makers’ judgement matrices and the corresponding weights of the decision makers. Using the RGMM version of Xu and Wei's individual consistency improving method [45], we transform these judgement matrices into ones with acceptably individual consistency. Then, we take these judgement matrices with acceptably individual consistency as the inputs of the proposed consensus models to study the convergence of the proposed consensus models.

Next, we describe the simulation methods in details.

Simulation method I

Input: n, m, $\overline { { G C C I } } , z _ { \mathrm { m a x } }$ and $0 { < } \theta { < } 1$ Output: z and p

Step 1 We randomly generate m n×n judgement matrices $\{ A ^ { ( 1 ) } , . . . , A ^ { ( m ) } \}$ whose entries are uniformly randomly selected from {1/9,1/ $8 , \ldots , 1 , \ldots , 8 , 9 \}$

Step 2 We random generate a weight vector, $\lambda { = } \{ \lambda _ { 1 } , \lambda _ { 2 } { , } { \ldots } { } , \lambda _ { n } \}$ , where $\lambda _ { i } ( i = 1 , 2 , . . . n )$ is uniformly distributed on [0,1]. Then we normalize $\lambda { = } \{ \lambda _ { 1 } , \lambda _ { 2 } { , } { \ldots } , \lambda _ { n } \}$ , that is $\begin{array} { r } { \lambda _ { i } = \frac { \lambda _ { i } } { \sum _ { i = 1 } ^ { n } \lambda _ { i } } . } \end{array}$

Step 3 Using the RGMM version of Xu and Wei's individual consistency improving method, we transform $\{ A ^ { ( 1 ) } , . . . , A ^ { ( m ) } \}$ into the judgement matrices with acceptably individual consistency. For simplicity, we still denote these judgement matrices with acceptably individual consistency as $\{ A ^ { ( \top ) } , . . . , A ^ { ( m ) } \}$

Step 4 We take $\{ A ^ { ( 1 ) } , . . . , A ^ { ( m ) } \} , \lambda = \{ \lambda _ { 1 } , \lambda _ { 2 } , . . . , \lambda _ { m } \} , \overline { { { G C C I } } } , z _ { \mathrm { m a x } }$ and $0 { < } \theta { < } 1$ as the inputs of the cardinal consensus model. Applying the cardinal consensus model, we obtain the adjusted judgement matrices A <sup>k</sup> $( k = 1 , 2 , . . . , n )$ , and the cardinal consensus indexes $G C C I \left( \overline { { A ^ { ( k ) } } } \right) ~ ( k = 1 , 2 , . . . , n )$ , and the number of iteration z.

Step 5 If $\operatorname* { m a x } _ { k } ( G C C I \left( \overline { { A ^ { ( k ) } } } \right) ) { \leq } \overline { { G C C I } }$ , then $p = 1$ . Otherwise $p { = } 0 .$ . Output z and p.

In simulation method I, we replace the cardinal consensus model, GCCI, GCCI by the ordinal consensus model, GOCI and $\overline { { G O G } }$ , respectively. We call the modi<sup>fi</sup>ed simulation method, simulation method II.

When setting different input parameters of simulation method I, we run this simulation method 1000 times, obtaining the average values of z and p. We also set different input parameters for simulation method II, and run it 1000 times to obtain the average values of z and p. Tables 1 and 2 respectively show the corresponding average values of z and p, under the different input parameters for simulation method I and simulation method II.

Note 1. The average value of p has a de<sup>fi</sup>nite physical implication, and re<sup>fl</sup>ects the success ratio of reaching consensus in the simulation experiments. Moreover, in running the simulation experiments, we $\mathsf { s e t } z _ { \mathrm { m a x } } = 3 0 0$ , and approximatively consider that the decision makers are of fully cardinal consensus when $G C C I ( A ^ { ( k ) } ) { \leq } 0 . 0 1$ for $k = 1 , 2 , . . . , m$

From Tables 1 and 2, we have the following observations:

(1) Simulation method I/Simulation method II de<sup>fi</sup>nitely help decision makers reach cardinal/ordinal consensus, under the established input parameters.

(2) With the increase of n and m, the number of the iterations z is increasing. Moreover, the smaller the parameter θ, the smaller the number of the iterations z.

Based on Theorem 1, Theorem 2 and the above simulation analysis, we <sup>fi</sup>nd that these two consensus models satisfy the properties presented in Section 3.2.

Table 1  
Average values of z and p for simulation method I under the different input parameters.

<table><tr><td rowspan="2">n</td><td rowspan="2">m</td><td rowspan="2"> $\overline{GCCI}$ </td><td colspan="2">θ=0.1</td><td colspan="2">θ=0.3</td><td colspan="2">θ=0.5</td><td colspan="2">θ=0.8</td></tr><tr><td>p</td><td>z</td><td>p</td><td>z</td><td>p</td><td>z</td><td>p</td><td>z</td></tr><tr><td rowspan="2">3</td><td rowspan="2">3</td><td>0.01</td><td>1</td><td>5.49</td><td>1</td><td>7.67</td><td>1</td><td>11.76</td><td>1</td><td>31.09</td></tr><tr><td>0.31</td><td>1</td><td>2.02</td><td>1</td><td>2.76</td><td>1</td><td>3.55</td><td>1</td><td>9.07</td></tr><tr><td rowspan="2">3</td><td rowspan="2">7</td><td>0.01</td><td>1</td><td>12.42</td><td>1</td><td>17.96</td><td>1</td><td>27.6</td><td>1</td><td>76.59</td></tr><tr><td>0.31</td><td>1</td><td>5.68</td><td>1</td><td>6.9</td><td>1</td><td>9.2</td><td>1</td><td>22.63</td></tr><tr><td rowspan="2">4</td><td rowspan="2">5</td><td>0.01</td><td>1</td><td>9.35</td><td>1</td><td>13.05</td><td>1</td><td>19.53</td><td>1</td><td>54.16</td></tr><tr><td>0.35</td><td>1</td><td>4.08</td><td>1</td><td>4.61</td><td>1</td><td>6.33</td><td>1</td><td>14.88</td></tr><tr><td rowspan="2">4</td><td rowspan="2">9</td><td>0.01</td><td>1</td><td>15.7</td><td>1</td><td>22.63</td><td>1</td><td>35.19</td><td>1</td><td>98.13</td></tr><tr><td>0.35</td><td>1</td><td>7.73</td><td>1</td><td>8.65</td><td>1</td><td>11.81</td><td>1</td><td>28.11</td></tr><tr><td rowspan="2">7</td><td rowspan="2">7</td><td>0.01</td><td>1</td><td>12.11</td><td>1</td><td>16.35</td><td>1</td><td>25.45</td><td>1</td><td>70.62</td></tr><tr><td>0.37</td><td>1</td><td>6.03</td><td>1</td><td>6.2</td><td>1</td><td>7.21</td><td>1</td><td>15.53</td></tr><tr><td rowspan="2">7</td><td rowspan="2">9</td><td>0.01</td><td>1</td><td>15.25</td><td>1</td><td>20.96</td><td>1</td><td>32.66</td><td>1</td><td>91.01</td></tr><tr><td>0.37</td><td>1</td><td>7.98</td><td>1</td><td>8.19</td><td>1</td><td>9.68</td><td>1</td><td>20.77</td></tr><tr><td>9</td><td>20</td><td>0.37</td><td>1</td><td>18.58</td><td>1</td><td>19.14</td><td>1</td><td>19.62</td><td>1</td><td>39.6</td></tr></table>

Table 2  
Average values of z and p for simulation method II under the different input parameters.

<table><tr><td rowspan="2">n</td><td rowspan="2">m</td><td rowspan="2"> $\overline{GOCI}$ </td><td colspan="2">θ=0.1</td><td colspan="2">θ=0.3</td><td colspan="2">θ=0.5</td><td colspan="2">θ=0.8</td></tr><tr><td>p</td><td>z</td><td>p</td><td>z</td><td>p</td><td>z</td><td>p</td><td>z</td></tr><tr><td rowspan="2">3</td><td rowspan="2">3</td><td>0</td><td>1</td><td>2.28</td><td>1</td><td>2.90</td><td>1</td><td>3.76</td><td>1</td><td>9.73</td></tr><tr><td>2/3</td><td>1</td><td>0.83</td><td>1</td><td>0.94</td><td>1</td><td>1.07</td><td>1</td><td>2.33</td></tr><tr><td rowspan="2">3</td><td rowspan="2">7</td><td>0</td><td>1</td><td>6.58</td><td>1</td><td>8.43</td><td>1</td><td>11.96</td><td>1</td><td>31.47</td></tr><tr><td>2/3</td><td>1</td><td>2.64</td><td>1</td><td>3.24</td><td>1</td><td>3.93</td><td>1</td><td>9.33</td></tr><tr><td rowspan="2">4</td><td rowspan="2">5</td><td>0</td><td>1</td><td>6.22</td><td>1</td><td>8.16</td><td>1</td><td>11.54</td><td>1</td><td>28.47</td></tr><tr><td>1/2</td><td>1</td><td>3.72</td><td>1</td><td>4.68</td><td>1</td><td>5.98</td><td>1</td><td>14.42</td></tr><tr><td rowspan="2">4</td><td rowspan="2">9</td><td>0</td><td>1</td><td>11.94</td><td>1</td><td>15.44</td><td>1</td><td>22.44</td><td>1</td><td>60.43</td></tr><tr><td>1/2</td><td>1</td><td>6.98</td><td>1</td><td>9.12</td><td>1</td><td>13.11</td><td>1</td><td>30.95</td></tr><tr><td rowspan="2">7</td><td rowspan="2">7</td><td>0</td><td>1</td><td>14.09</td><td>1</td><td>19.47</td><td>1</td><td>28.74</td><td>1</td><td>56.22</td></tr><tr><td>2/7</td><td>1</td><td>11.35</td><td>1</td><td>14.95</td><td>1</td><td>21.77</td><td>1</td><td>54.9</td></tr><tr><td rowspan="2">7</td><td rowspan="2">9</td><td>0</td><td>1</td><td>18.82</td><td>1</td><td>24.69</td><td>1</td><td>37.88</td><td>1</td><td>99.95</td></tr><tr><td>2/7</td><td>1</td><td>14.56</td><td>1</td><td>19.46</td><td>1</td><td>28.69</td><td>1</td><td>75.55</td></tr><tr><td>9</td><td>20</td><td>2/9</td><td>1</td><td>38.44</td><td>1</td><td>54.7</td><td>1</td><td>84.54</td><td>1</td><td>235.93</td></tr></table>

## 5. Numerical examples

In order to show how the consensus models work in practice, let us consider the following example. Suppose we have a set of <sup>fi</sup>ve decision makers providing the following judgement matrices $\{ A ^ { ( 1 ) } , . . . , A ^ { ( 5 ) } \}$ on a set of four alternatives. Let $\Breve { w } ^ { ( k ) } = ( w _ { 1 } ^ { ( k ) } , . . . , w _ { 4 } ^ { ( k ) } ) ^ { T }$ be the individual priority vector derived from judgment matrix $\dot { A } ^ { ( k ) }$ using RGMM. $A ^ { ( k ) }$ and $w ^ { ( k ) } \left( k = 1 , 2 , . . . , 5 \right)$ are listed below.

$$
A ^ {(1)} = \left( \begin{array}{c c c c} 1 & 4 & 6 & 7 \\ 1 / 4 & 1 & 3 & 4 \\ 1 / 6 & 1 / 3 & 1 & 2 \\ 1 / 7 & 1 / 4 & 1 / 2 & 1 \end{array} \right),
$$

$$
w ^ {(1)} = \{0. 6 1 4 5, 0. 2 2 4 6, 0. 0 9 8 5, 0. 0 6 2 4 \} ^ {T}.
$$

$$
A ^ {(2)} = \left( \begin{array}{c c c c} 1 & 5 & 7 & 9 \\ 1 / 5 & 1 & 4 & 6 \\ 1 / 7 & 1 / 4 & 1 & 2 \\ 1 / 9 & 1 / 6 & 1 / 2 & 1 \end{array} \right),
$$

$$
w ^ {(2)} = \{0. 6 4 6 1, 0. 2 2 7, 0. 0 7 9 3, 0. 0 4 7 6 \} ^ {T}.
$$

$$
A ^ {(3)} = \left( \begin{array}{c c c c} 1 & 3 & 5 & 8 \\ 1 / 3 & 1 & 4 & 5 \\ 1 / 5 & 1 / 4 & 1 & 2 \\ 1 / 8 & 1 / 5 & 1 / 2 & 1 \end{array} \right),
$$

$$
w ^ {(3)} = \{0. 5 6 9 3, 0. 2 7 6 4, 0. 0 9 6 7, 0. 0 5 7 5 \} ^ {T}.
$$

$$
A ^ {(4)} = \left( \begin{array}{c c c c} 1 & 4 & 5 & 6 \\ 1 / 4 & 1 & 3 & 3 \\ 1 / 5 & 1 / 3 & 1 & 2 \\ 1 / 6 & 1 / 3 & 1 / 2 & 1 \end{array} \right),
$$

$$
w ^ {(4)} = \{0. 5 9 6 7, 0. 2 2 0 8, 0. 1 0 8 9, 0. 0 7 3 6 \} ^ {T}.
$$

$$
A ^ {(5)} = \left( \begin{array}{c c c c} 1 & 1 / 2 & 1 & 2 \\ 2 & 1 & 1 / 2 & 3 \\ 1 & 1 / 2 & 1 & 4 \\ 1 / 2 & 1 / 3 & 1 / 4 & 1 \end{array} \right),
$$

$$
w ^ {(5)} = \{0. 2 2 4 7, 0. 2 9 5 8, 0. 3 7 8, 0. 1 0 1 5 \} ^ {T}.
$$

Note 2. The judgment matrices $A ^ { ( 1 ) } , A ^ { ( 2 ) } , . . . , A ^ { ( 4 ) }$ are <sup>fi</sup>rst provided in Xu [43].

Let $\lambda { = } \{ 0 . 1 , 0 . 3 , 0 . 1 , 0 . 2 , 0 . 3 \}$ be the weights of decision makers. Let $A ^ { ( c ) }$ be the collective judgement matrix derived from $\{ A ^ { ( 1 ) } , . . . , A ^ { ( 5 ) } \}$ using $\mathrm { A I J } .$

Table 3  
The GCI, GCCI and GOCI values o $\mathbf { \dot { A } } ^ { ( k ) }$ $( k = 1 , 2 , . . . , 5 )$ and $A ^ { ( c ) } .$

<table><tr><td></td><td> $A^{(1)}$ </td><td> $A^{(2)}$ </td><td> $A^{(3)}$ </td><td> $A^{(4)}$ </td><td> $A^{(5)}$ </td><td> $A^{(c)}$ </td></tr><tr><td>GCI(•)</td><td>0.1349</td><td>0.2358</td><td>0.1194</td><td>0.1657</td><td>0.2208</td><td>0.056</td></tr><tr><td>GCCI(•)</td><td>0.4285</td><td>0.8707</td><td>0.4113</td><td>0.3774</td><td>2.1944</td><td>Undefined</td></tr><tr><td>GOCI(•)</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>Undefined</td></tr></table>

Let $\boldsymbol { w } ^ { ( c ) } = ( w _ { 1 } ^ { ( c ) } , w _ { 2 } ^ { ( c ) } , . . . , w _ { n } ^ { ( c ) } ) ^ { T }$ be the collective priority vector, derived from $A ^ { ( c ) }$ using RGMM. $A ^ { ( c ) }$ and $w ^ { ( c ) }$ are listed below.

$$
A ^ {(c)} = \left( \begin{array}{c c c c} 1 & 2. 2 2 7 & 3. 4 7 5 6 & 5. 0 9 3 7 \\ 0. 4 4 9 0 & 1 & 1. 9 6 6 3 & 4. 0 0 0 5 \\ 0. 2 8 7 7 & 0. 5 0 8 6 & 1 & 2. 4 6 2 3 \\ 0. 1 9 6 3 & 0. 2 5 0 0 & 0. 4 0 6 1 & 1 \end{array} \right),
$$

$$
w ^ {(c)} = \{0. 4 9 8 4, 0. 2 7 2 7, 0. 1 5 4 1, 0. 0 7 4 7 \} ^ {T}.
$$

We compute the GCI, GCCI and GOCI values of $A ^ { ( k ) } ( k = 1 , 2 , . . . , 5 )$ and $A ^ { ( c ) }$ . These values are listed in Table 3.

Table 3 shows that $G C I ( A ^ { ( k ) } ) < \overline { { { G C I } } } = 0 . 3 5 ( k = 1 , 2 , . . . , 5 ) , 5 0 A ^ { ( 1 ) } , . . . , A ^ { ( 5 ) }$ are of acceptably individual consistency.

When setting $\overline { { G C C I } } = 0 . 3 5$ and θ = 0.8, we apply the cardinal consensus model to adjust judgement matrices. The adjusted judgement matrices and the collective judgement matrix are $\overline { { A ^ { ( k ) } } } , ( k = 1 , 2 , . . . , 5 )$ and $\overline { { A ^ { ( c ) } } }$ , respectively. The corresponding prior-<sup>ð Þ</sup>i t y v e c t o r a r e $\overline { { w ^ { ( k ) } } } = ( w _ { 1 } ^ { ( \hat { k } ) } , . . . , w _ { 4 } ^ { ( \bar { k } ) } ) ^ { T } ~ ( \ k = 1 , \bar { 2 } , . . . , 5 )$ a n d $\overline { { w ^ { ( c ) } } } = ( \overline { { w _ { 1 } ^ { ( c ) } } } , . . . , \overline { { w _ { 4 } ^ { ( c ) } } } ) ^ { T }$ , respectively. The cardinal consensus model ends in the 4th iteration. We <sup>fi</sup>nd tha ${ \overline { { A ^ { ( k ) } } } } = A ^ { ( k ) } \operatorname { a n d } { \overline { { w ^ { ( k ) } } } } = w ^ { ( k ) }$ for $k { = } 1 , 2 { \mathrm { , . . . , } } 4 . { \mathrm { A n d } } , { \overline { { A ^ { ( 5 ) } } } } , { \overline { { A ^ { ( c ) } } } } , { \overline { { w ^ { ( 5 ) } } } }$ , and $\overline { { w ^ { ( c ) } } }$ are listed below.

$$
\overline {{A ^ {(5)}}} = \left( \begin{array}{c c c c} 1. 0 0 0 0 & 1. 1 2 9 7 & 2. 2 0 1 4 & 4. 3 3 5 2 \\ 0. 8 8 5 2 & 1. 0 0 0 0 & 1. 1 0 4 4 & 3. 4 1 0 8 \\ 0. 4 5 4 3 & 0. 9 0 5 5 & 1. 0 0 0 0 & 2. 6 1 5 8 \\ 0. 2 3 0 7 & 0. 2 9 3 2 & 0. 3 8 2 3 & 1. 0 0 0 0 \end{array} \right),
$$

$$
w ^ {(5)} = \{0. 3 9 5 4, 0. 2 9 4 9, 0. 2 2 2 2, 0. 0 8 7 5 \} ^ {T}.
$$

$$
A ^ {(c)} = \left( \begin{array}{c c c c} 1. 0 0 0 0 & 2. 8 4 3 9 & 4. 4 0 4 0 & 6. 4 2 4 3 \\ 0. 3 5 1 6 & 1. 0 0 0 0 & 2. 4 9 4 0 & 4. 1 5 7 5 \\ 0. 2 2 7 1 & 0. 4 0 1 0 & 1. 0 0 0 0 & 2. 1 6 7 7 \\ 0. 1 5 5 7 & 0. 2 4 0 5 & 0. 4 6 1 3 & 1. 0 0 0 0 \end{array} \right),
$$

$$
w ^ {(c)} = \{0. 5 5 4 0, 0. 2 5 5 6, 0. 1 2 3 3, 0. 0 6 7 1 \} ^ {T}.
$$

We compute the GCI and GCCI values o $\overline { { \lceil A ^ { ( k ) } } } ( k = 1 , 2 , . . . , 5 )$ and $\overline { { A ^ { ( c ) } } }$ These values are listed in Table 4.

When setting GOCI = 0 and $\theta = 0 . 5$ , we apply the ordinal consensus model to adjust judgement matrices. The adjusted judgement matrices and the collective judgement matrix are $\overline { { A ^ { ( k ) } } } , ( k = 1 , 2 , . . . , 5 )$ and $\overline { { \overline { { A ^ { ( c ) } } } } }$ , respectively. The corresponding priority v e c t o r a r e $\overline { { \overline { { w ^ { ( k ) } } } } } = ( \overline { { w _ { 1 } ^ { ( k ) } } } , . . . , \overline { { w _ { 4 } ^ { ( k ) } } } ) ^ { T } ~ ( ~ k = 1 , 2 , . . . , 5 ~ )$ a n d $\overline { { \overline { { w ^ { ( c ) } } } } } = ( \overline { { w _ { 1 } ^ { ( c ) } } } , . . . , \overline { { w _ { 4 } ^ { ( c ) } } } ) ^ { I }$ , respectively. The ordinal consensus model ends in the 2nd iteration. We <sup>fi</sup>nd tha $\overline { { \cdot \overline { { A ^ { ( k ) } } } } } = A ^ { ( k ) } \mathrm { a n d } \overline { { \overline { { w ^ { ( k ) } } } } } = w ^ { ( k ) }$ for $k { = } 1 , 2 { , } { \ldots } , 4 . \operatorname { A n d } , \overline { { { A ^ { ( 5 ) } } } } , \overline { { { A ^ { ( c ) } } } } , \overline { { { w ^ { ( 5 ) } } } }$ , and w <sup>c</sup> are listed below.

The GCI and GCCI values o $\overline { { A ^ { ( k ) } } } ( k = 1 , 2 , . . . , 5 )$ and $\overline { { A ^ { ( c ) } } }$

<table><tr><td></td><td> $A^{(1)}$ </td><td> $A^{(2)}$ </td><td> $A^{(3)}$ </td><td> $A^{(4)}$ </td><td> $A^{(5)}$ </td><td> $A^{(c)}$ </td></tr><tr><td>GCI(•)</td><td>0.1349</td><td>0.2358</td><td>0.1194</td><td>0.1657</td><td>0.037</td><td>0.0688</td></tr><tr><td>GCCI(•)</td><td>0.1054</td><td>0.2579</td><td>0.1051</td><td>0.1150</td><td>0.3138</td><td>Undefined</td></tr></table>

$$
\overline {{\overline {{A ^ {(5)}}}}} = \left( \begin{array}{c c c c} 1 & 0. 9 5 6 0 & 1. 7 9 8 4 & 3. 6 5 2 1 \\ 1. 0 4 6 0 & 1 & 0. 9 4 0 6 & 3. 3 0 8 5 \\ 0. 5 5 6 0 & 1. 0 6 3 1 & 1 & 2. 8 7 1 9 \\ 0. 2 7 3 8 & 0. 3 0 2 3 & 0. 3 4 8 2 & 1 \end{array} \right),
$$

$$
\overline {{\overline {{w ^ {(5)}}}}} = \{0. 3 0 2 8, 0. 3 0 2 1, 0. 2 9 8 5, 0. 0 9 6 6 \} ^ {T}.
$$

$$
\overline {{\overline {{A ^ {(c)}}}}} = \left( \begin{array}{c c c c} 1. 0 0 0 0 & 2. 7 0 4 9 & 4. 1 4 4 8 & 6. 1 0 2 2 \\ 0. 3 6 9 7 & 1. 0 0 0 0 & 2. 3 7 6 7 & 4. 1 1 9 7 \\ 0. 2 4 1 3 & 0. 4 2 0 7 & 1. 0 0 0 0 & 2. 2 2 9 3 \\ 0. 1 6 3 9 & 0. 2 4 2 7 & 0. 4 4 8 6 & 1. 0 0 0 0 \end{array} \right),
$$

$$
\overline {{\overline {{w ^ {(c)}}}}} = \{0. 5 4 1 6, 0. 2 5 9 7, 0. 1 2 9 9, 0. 0 6 8 8 \} ^ {T}.
$$

We compute the GCI and GOCI values of $\overline { { \overline { { A ^ { ( k ) } } } } } ( k = 1 , 2 , . . . , 5 )$ and $\overline { { A ^ { ( c ) } } }$ . These values are listed in Table 5.

We can <sup>fi</sup>nd that the results in this example are in accordance with Theorems 1 and 2.

## 6. Conclusion

Consensus models have been a hot topic in group decision making using preference relations. In general, research progress in group decision making using preference relations can bene<sup>fi</sup>t research in AHP. This paper de<sup>fi</sup>nes the consensus indexes (i.e., the geometric cardinal consensus index and the geometric ordinal consensus index) to measure consensus degree among judgement matrices (or decision makers). Inspired by Chiclana et al.'s consensus framework [13] and Xu and Wei's individual consistency improving method [45], we propose two new AHP consensus models (i.e., cardinal consensus model and ordinal consensus model) under RGMM. Simulation results and <sup>fi</sup>eld experiments show these consensus models can effectively improve the consensus indexes (i.e., GCCI and GOCI) of judgement matrices to help AHP decision makers reach consensus. Comparing the existing AHP consensus models, the proposed two consensus models have two desired features:

(1) in reaching consensus, the adjusted judgement matrix has a better individual consistency index (i.e., geometric consistency index) than the corresponding original judgement matrix,

(2) and they satisfy the Pareto principle of social choice theory.

Thus, our proposals are not only very effective to help AHP decision makers reach consensus, but also providing more convinced alternatives.

In addition, similar to individual consistency improving method of AHP [8,21,45], the consensus models should only be considered as a decision aid, which the decision makers use as a reference to modify their own judgement matrices. Therefore, a feasible future research issue could be focused on the effectiveness assessment of consensus models.

## Acknowledgements

Yucheng Dong and Yinfeng Xu acknowledge the <sup>fi</sup>nancial support of grants (nos. 70801048 and 70525004) from NSF of China and a grant (no. 200806981067) form the Ph.D. Programs Foundation of Ministry of

The GCI and GOCI values o $\cdot \overline { { \overline { { A ^ { ( k ) } } } } } ( k = 1 , 2 , . . . , 5 )$ and ${ \overline { { \overline { { A ^ { ( c ) } } } } } } .$

<table><tr><td></td><td> $\overline{A^{(1)}}$ </td><td> $\overline{A^{(2)}}$ </td><td> $\overline{A^{(3)}}$ </td><td> $\overline{A^{(4)}}$ </td><td> $\overline{A^{(5)}}$ </td><td> $\overline{A^{(c)}}$ </td></tr><tr><td>GCI(•)</td><td>0.1349</td><td>0.2358</td><td>0.1194</td><td>0.1657</td><td>0.1077</td><td>0.0659</td></tr><tr><td>GCCI(•)</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>Undefined</td></tr></table>

Education of China. Wei-Chiang Hong acknowledges the <sup>fi</sup>nancial support of grants (nos. 98-2410-H-161-001 and 98-2811-H-161-001) from NSC of Taiwan.

## Appendix A

## A.1. The RGMM version of Xu and Wei's method

Xu and Wei [45] propose an individual consistency improving method based on the EM and Saaty's consistency index. In Xu and Wei’ method, we replace EM by RGMM, and replace Saaty's consistency index by the geometric consistency index. In this way, we obtain the RGMM version of this method.

Let z be the number of iterations, and 0bθb1. The steps of the RGMM version of Xu and Wei's method are described as follows:

The RGMM version of Xu and Wei's method

Input: The judgement matrix A, the threshold GCI and $0 { < } \theta { < } 1$ Output: The adjusted judgement matrix B, its geometric consistency index GCI(B) and the number of iterations z.

Step 1 Let $A ^ { ( 0 ) } = ( a _ { i j } ^ { ( 0 ) } ) _ { n \times n } = ( a _ { i j } ) _ { n \times n }$ and $z = 0 ;$

Step 2 Let $\boldsymbol { w } ^ { ( z ) } = ( \bar { w } _ { 1 } ^ { ( z ) } , w _ { 2 } ^ { ( z ) } , . . . , w _ { n } ^ { ( z ) } ) ^ { T }$ be the priority vector derived from $A ^ { ( z ) }$ using RGMM.

Step 3 We calculate the geometric consistency index:

$$
G C I (A) = \frac {2}{(n - 1) (n - 2)} \sum_ {i <   j} \left(\log \left(a _ {i j}\right) - \log \left(w _ {i}\right) + \log \left(w _ {j}\right)\right) ^ {2}.
$$

Step 4 If $G C I ( A ^ { ( z ) } ) { \leq } \overline { { G C I } } ,$ , then go to Step 6; otherwise, continue with <sup>ð Þ</sup>the next step;

Step 5 Let $\begin{array} { r } { \pmb { A } ^ { ( z + 1 ) } = ( a _ { i j } ^ { ( z + 1 ) } ) _ { n \times n } , } \end{array}$ where

$$
a _ {i j} ^ {(z + 1)} = \left(a _ {i j} ^ {(z)}\right) ^ {\theta} \left(\frac {w _ {i} ^ {(z)}}{w _ {j} ^ {(z)}}\right) ^ {(1 - \theta)}.
$$

Step 6 Let $B { = } A ^ { ( z ) }$ . Output the adjusted judgement matrix B, its geometric consistency index GCI(B) and the number of iterations z.

Theorem 3. Let $\{ A ^ { ( z ) } \}$ be the judgement matrix sequence in the RGMM version of Xu and Wei's method. Then, we have that $G \dot { C } I ( A ^ { ( z + 1 ) } ) { < } G C I ( A ^ { ( z ) } )$ for each z, and $\operatorname* { l i m } _ { z  \infty } { \big ( } G C I ( A ^ { ( z ) } ) { \big ) } { \leq } \overline { { G C I } }$

The proof of Theorem 3 is provided in Appendix A.2.

Theorem 3 guarantees that any judgement matrix with unacceptably individual consistency can be transformed into one with acceptably individual consistency (in the GCI sense), by using the RGMM version of Xu and Wei's method.

## A.2. The proofs of theorems

Proof of Theorem 1. We <sup>fi</sup>rst prove $G C I ( \overline { { A ^ { ( k ) } } } ) { \leq } G C I ( A ^ { ( k ) } )$ . Let $A _ { z } ^ { ( k ) } =$ $( a _ { i j z } ^ { ( k ) } ) _ { n \times n } ~ ( k = 1 , 2 , . . . , m )$ <sup>ð Þ ð Þ</sup>be the adjusted judgment matrices in the zth iteration using the cardinal consensus model. Let $w _ { z } ^ { ( c ) } = ( w _ { 1 , z } ^ { ( c ) } , w _ { 2 , z } ^ { ( c ) } . . . , w _ { n , z } ^ { ( c ) } ) ^ { T }$ be the collective priority vector, derived from the collective judgement matrix $A _ { z } ^ { ( c ) } = ( a _ { i j z } ^ { ( c ) } ) _ { n \times n }$ , where $\begin{array} { r } { a _ { i j z } ^ { ( c ) } = \prod _ { k = 1 } ^ { m } ( a _ { i j z } ^ { ( k ) } ) ^ { \lambda _ { k } } } \end{array}$ , using RGMM. Without loss of generality, suppose that $G C C I ( A _ { z } ^ { ( \tau ) } ) = \operatorname* { m a x } _ { k } \left\{ G C C I ( A _ { z } ^ { ( k ) } ) \right\}$ We consider two cases. □

Case $\begin{array} { r } { \mathrm { ~ A ~ } k = \tau . } \end{array}$ In this case, according to the cardinal consensus model, we have that $A _ { z + 1 } ^ { ( k ) } { = } \bar { ( } a _ { i j , z + 1 } ^ { ( k ) } ) _ { n \times n } ,$ , where $a _ { i j , z + 1 } ^ { ( k ) } =$ $( a _ { i j , z } ^ { ( k ) } ) ^ { \Theta } ( \frac { w _ { i , z } ^ { ( c ) } } { w _ { i , z } ^ { ( c ) } } ) ^ { ( 1 - \Theta ) }$ . Let $\begin{array} { r } { W _ { z } = ( w _ { i j , z } ) = ( \frac { w _ { i , z } ^ { ( c ) } } { w _ { i , z } ^ { ( c ) } } ) } \end{array}$ . From Lemma 2, we have that $G C I ( A _ { z + 1 } ^ { ( k ) } )$ ≤ max{GCI(A<sub>z</sub><sup>(k)</sup>),GCI(W<sub>z</sub>)} = GCI(A<sub>z</sub><sup>(k)</sup>).

Case B $k \neq \tau .$ . In this case, $A _ { z + 1 } ^ { ( k ) } = A _ { z } ^ { ( k ) } . 5 0 , G C I ( A _ { z + 1 } ^ { ( k ) } ) = G C I ( A _ { z } ^ { ( k ) } )$

Summarizing Case A and Case B, we have that $G C I ( A _ { z + 1 } ^ { ( k ) } ) \leq G C I$ $( A _ { z } ^ { ( k ) } )$ for $k = 1 , 2 , . . . , m$

$$
\text { Consequently, } G C I (\overline {{A ^ {(k)}}}) \leq G C I (A _ {0} ^ {(k)}) = G C I (A ^ {(k)}) \text { for } k = 1, 2,..., m.
$$

Similarly, we can prove $G C I ( \overline { { A ^ { ( k ) } } } ) { \leq } G C I ( A ^ { ( k ) } )$ . This completes the proof of Theorem 1.

Proof of Theorem 2. We <sup>fi</sup>rst prove $\overline { { w _ { i } ^ { ( c ) } } } > \overline { { w _ { i } ^ { ( c ) } } }$ . Let $A _ { z } ^ { ( k ) } = ( a _ { i j z } ^ { ( k ) } ) _ { n \times n }$ $( k = 1 , 2 , . . . , m )$ be adjusted judgment matrices in the zth iteration using the cardinal consensus model. Let $w _ { z } ^ { ( k ) } { = } ( w _ { 1 , z } ^ { ( k ) } { , . . . , w _ { n , z } ^ { ( k ) } } ) ^ { T }$ be individual priority vector derived from judgment matrix $A _ { z } ^ { ( k ) }$ using RGMM. Let $\mathbf { \bar { \boldsymbol { w } } } _ { z } ^ { ( c ) } = ( w _ { 1 , z } ^ { ( c ) } , w _ { 2 , z } ^ { ( c ) } , . . . , w _ { n , z } ^ { ( c ) } ) ^ { T }$ be the collective priority vector, derived from the collective judgement matrix $\bar { \boldsymbol { A } } _ { z } ^ { ( c ) } = \dot { ( } \boldsymbol { a } _ { i j z } ^ { ( c ) } ) _ { n \times n }$ , where $\begin{array} { r } { a _ { i j z } ^ { ( c ) } = \prod _ { k = 1 } ^ { m } ( a _ { i j z } ^ { ( k ) } ) ^ { \lambda _ { k } } } \end{array}$ , using RGMM. □

By induction over z, the proof can be completed. $\mathrm { F o r } z = 0 ,$ , we have that $\mathbf { \bar { \rho } } _ { W _ { z } } ( k ) = \mathbf { \bar { \rho } } _ { W } ( k )$ . Since $w _ { i } ^ { ( k ) } > w _ { i } ^ { ( k ) } ~ ( k = 1 , 2 , . . . , \not m )$ , we have that $w _ { i , 0 } ^ { ( k ) } >$ $w _ { i , 0 } ^ { ( k ) }$ for $k = 1 , 2 , . . . , m$ . According to Corollary 1, we have that $w _ { i , 0 } ^ { ( c ) } { > } w _ { j , 0 } ^ { ( c ) }$ Suppose that it is true for z, i.e., $w _ { i , z } ^ { ( k ) } { > } w _ { j , z } ^ { ( k ) }$ for $k = 1 , 2 , . . . , m$ , and $w _ { i , z } ^ { ( \bar { c } ) } >$ $w _ { j , z } ^ { ( c ) } .$

Without loss of generality, suppose that $G C C I ( A _ { z \mathrm { ~ + ~ } 1 } ^ { ( \tau ) } ) = \underset { k } { \operatorname* { m a x } }$ $\{ G C C I ( A _ { z + 1 } ^ { ( k ) } ) \}$ : For $z + 1$ , we consider two cases.

Case A $k = \tau .$ In this case, according to the cardinal consensus model, we have that $A _ { z + 1 } ^ { ( k ) } = ( a _ { i j , z + 1 } ^ { ( k ) } ) _ { n \times n } ,$ , where $a _ { i j , z + 1 } ^ { ( k ) } = ( a _ { i j , z } ^ { ( k ) } ) ^ { \Theta } ( \frac { w _ { i , z } ^ { ( c ) } } { w _ { \therefore } ^ { ( c ) } } ) ^ { ( 1 - \Theta ) }$ Since $w _ { i , z } ^ { ( k ) } > w _ { j , z } ^ { ( k ) }$ and $w _ { i , z } ^ { ( c ) } { > } w _ { j , z } ^ { ( c ) }$ , according to Corollary 1, we have that $w _ { i , z + 1 } ^ { ( k ) } { > } w _ { j , z + 1 } ^ { ( k ) }$ .

Case B $k \neq \tau .$ . In this case, $A _ { z + 1 } ^ { ( k ) } = A _ { z } ^ { ( k ) }$ and $w _ { z + 1 } ^ { ( k ) } = w _ { z } ^ { ( k ) }$ . Since $w _ { i , z } ^ { ( k ) } >$ $w _ { j , z } ^ { ( k ) }$ , we have $w _ { i , z + 1 } ^ { ( k ) } { > } w _ { j , z + 1 } ^ { ( k ) } .$

Summarizing Case A and Case B, we have that $w _ { i , z } ^ { ( k ) } + 1 { > } w _ { j , z } ^ { ( k ) } -$ <sub>+ 1</sub>for $k = 1 , 2 , . . . , m$ . From Corollary 1, we have that $w _ { i , z + 1 } ^ { ( c ) } { > } w _ { j , z + 1 } ^ { ( c ) }$

$$
\overline {{w _ {i} ^ {(c)}}} > \overline {{w _ {i} ^ {(c)}}}
$$

Similarly, we can prove $\overline { { \overline { { w _ { i } ^ { ( c ) } } } } } > \overline { { w _ { j } ^ { ( c ) } } }$ . This completes the proof of Theorem 2.

Proof of Theorem 3. Let $Q = \{ ( w _ { 1 } , w _ { 2 } , . . . , w _ { n } ) ^ { T } | 0 \leq w _ { i } \leq 1 , \sum _ { i = 1 } ^ { n } w _ { i } = 1 \}$ According to De<sup>fi</sup>nition 1, we have that

$$
\begin{array}{l} G C I \Big (A ^ {z + 1} \Big) = \frac {2}{(n - 1) (n - 2)} \sum_ {i <   j} \Big (\log \Big (a _ {i j} ^ {(z + 1)} \Big) - \log \Big (w _ {i} ^ {(z + 1)} \Big) + \log \Big (w _ {j} ^ {(z + 1)} \Big) \Big) ^ {2} \\ = \frac {2}{(n - 1) (n - 2)} \min _ {W \in Q} \sum_ {i <   j} \Big (\log \Big (a _ {i j} ^ {(z + 1)} \Big) - \log (w _ {i}) + \log (w _ {j}) \Big) ^ {2} \\ \leq \frac {2}{(n - 1) (n - 2)} \sum_ {i <   j} \Big (\log \Big (a _ {i j} ^ {(z + 1)} \Big) - \log \Big (w _ {i} ^ {(z)} \Big) + \log \Big (w _ {j} ^ {(z)} \Big) \Big) ^ {2}. \end{array}
$$

Since $a _ { i j } ^ { ( z + 1 ) } = ( a _ { i j } ^ { ( z ) } ) ^ { \ L \ L \theta } ( \frac { w _ { i } ^ { ( z ) } } { w _ { j } ^ { ( z ) } } ) ^ { ( 1 - \theta ) }$ , we have that

$$
\begin{array}{c} G C I (A ^ {z + 1}) \leq \frac {2 \theta}{(n - 1) (n - 2)} (\log {(a _ {i j} ^ {(z)})} - \log (w _ {i} ^ {(z)}) + \log (w _ {j} ^ {(z)})) ^ {2} \\ = \theta G C I (A ^ {z}) <   G C I (A ^ {z}). \end{array}
$$

For each $z , G C I ( A ^ { ( z ) } ) { \geq } 0$ . Thus, the sequence $\{ G C I ( A ^ { ( z ) } ) \}$ } is monotone decreasing and has lower bounds. Then we have

$$
\lim _ {z \to \infty} \left(G C I \left(A ^ {(z)}\right)\right) = \inf \left\{G C I \left(A ^ {(z)}\right) \right\}.
$$

$$
\text { Let } \lim _ {z \to \infty} (A ^ {(z)}) = A ^ {\infty}, \text { then }
$$

$$
G C I (A ^ {\infty}) = \inf \left\{G C I \left(A ^ {(z)}\right) \right\}.
$$

Suppose that $G C I ( A ^ { \infty } ) > { \overline { { G C I } } }$ . By applying the RGMM version of Xu <sup>ð Þ</sup>and Wei's method to continue improving the consistency of $A ^ { \infty }$ , we can obtain the adjusted judgement matrix $\overline { { A ^ { \infty } } }$ . Obviously, we have $G C I ( \overline { { A ^ { \infty } } } ) { < } G C I ( A ^ { \infty } )$

$\begin{array} { r } { \operatorname * { i n t } _ { { \tilde { \mathbf { \Gamma } } } } \mathrm { T h u s } , G C I \big ( \overline { { A ^ { \infty } } } \big ) } \\ { \operatorname* { i n f } \{ G C I ( A ^ { ( z ) } ) \} . } \end{array}$ b inf $\big \{ G C I ( A ^ { ( z ) } ) \big \}$ , which contradicts the de<sup>fi</sup>nition of

This completes the proof of Theorem 3.

## References

[1] J. Aguarón, M.T. Escobar, J.M. Moreno-Jiménez, Consistency stability intervals for a judgement in AHP decision support systems, European Journal of Operational Research 145 (2) (2003) 382–393.

[2] J. Aguarón, J.M. Moreno-Jiménez, The geometric consistency index: Approximated thresholds, European Journal of Operational Research 147 (2003) 137–145.

[3] K.J. Arrow, Social Choice and Individual Values, 2nd edition, Wiley, New York, 1963.

[4] J. Barzilai, B. Golany, AHP rank reversal normalization and aggregation rules, INFOR 32 (1994) 57–64.

[5] D. Ben-Arieh, T. Easton, Multi-criteria group consensus under linear cost opinion elasticity, Decision Support Systems 43 (2007) 713–721.

[6] D. Ben-Arieh, T. Easton, B. Evans, Minimum cost consensus with quadratic cost functions, IEEE Transactions on Systems, Man, and Cybernetics Part A: Systems and Humans 39 (2009)210-217

[7] N. Bryson, Group decision-making and the analytic hierarchy process: exploring the consensus-relevant information content, Computers & Operations Research 23 (1996) 27–35.

[8] D. Cao, L.C. Leung, J.S. Law, Modifying inconsistent comparison matrix in analytic hierarchy process: a heuristic approach, Decision Support Systems 44 (2008) 944–953.

[9] Y.L. Chen, L.C. Cheng, Mining maximum consensus sequences from group ranking data European Journal of Operational Research 198 (2009) 241–251

[10] A.K. Choudhury, R. Shankar, M.K. Tiwari, Consensus-based intelligent group decision-making model for the selection of advanced technology, Decision Support Systems.42 (2006)1776-1799

[11] F. Chiclana, F. Herrera, E. Herrera-Viedma, Integrating three representation models in fuzzy multipurpose decision making based on fuzzy preference relations, Fuzzy Sets and Systems 97 (1998) 33–48.

[12] F. Chiclana, F. Herrera, E. Herrera-Viedma, Integrating multiplicative preference relations in a multipurpose decision-making model based on fuzzy preference relations, Fuzzy Sets and Systems 122 (2001) 277–291.

[13] F. Chiclana, F. Mata, L. Martínez, E. Herrera-Viedma, S. Alonso, Integration of a consistency control module within a consensus decision making model, International Journal of Uncertainty, Fuzziness and Knowledge-Based Systems 16 (2008) 35–53.

[14] G. Crawford, C. Williams, A note on the analysis of subjective judgement matrices, Journal of Mathematical Psychology 29 (1985) 387–405.

[15] Y.C. Dong, Y.F. Xu, H.Y. Li, M. Dai, A comparative study of the numerical scales and the prioritization methods in AHP, European Journal of Operational Research 186 (2008) 229–242.

[16] Y.C. Dong, Y.F. Xu, H.Y. Li, B. Feng, The OWA-based consensus operator under linguistic representation models using position indexes, European Journal of Operational Research 203 (2010) 455–463.

[17] Y.C. Dong, Y.F. Xu, S. Yu, Linguistic multiperson decision making based on the use of multiple preference relations, Fuzzy Sets and Systems 160 (2009) 603–623.

[18] M.T. Escobar, J.M. Moreno-Jiménez, Aggregation of individual preference structures in AHP group decision making, Group Decision and Negotiation 16 (2007) 287–301.

[19] M.T. Escobar, J. Aguarón, J.M. Moreno-Jiménez, A note on AHP group consistency for the row geometric mean priorization procedure, European Journal of Operational Research 153 (2004) 318–322.

[20] Z.P. Fan, S. Xiao, G. Hu, An optimization method for integrating two kinds of preference information in group decision-making, Computers & Industrial Engineering 46 (2004) 329–335.

[21] J.S. Fiana, W.J. Hurley, The analytic hierarchy process: does adjusting a pairwise comparison matrix to improve the consistency ratio help? Computers & Operations Research 24 (1997) 749–755.

[22] J. Fodor, M. Roubens, Fuzzy Preference Modelling and Multicriteria Decision Support, Kluwer Dordrecht 1994

[23] E. Forman, K. Peniwati, Aggregating individual judgments and priorities with the analytic hierarchy process European Journal of Operational Research 108 (1998 165-169

[24] P.T. Harker, Derivatives of the Perron root of a positive reciprocal matrix: with application to the analytic hierarchy process, Applied Mathematics and Computation 22 (1987) 217–232.

[25] M.W. Herman, W.W. Koczkodaj, A Monte Carlo study of pairwise comparison, Information Processing Letters 57 (1996) 25–29.

[26] F. Herrera, E. Herrera-Viedma, F. Chiclana, Multiperson decision-making based on multiplicative preference relations, European Journal of Operational Research 129 (2001) 372–385.

[27] F. Herrera, E. Herrera-Viedma, J.L. Verdegay, A model of consensus in group decision making under linguistic assessments, Fuzzy Sets and Systems 78 (1996) 73–87.

[28] F. Herrera, L. Martínez, A 2-tuple fuzzy linguistic representation model for computing with words, IEEE Transactions on Fuzzy Systems 8 (2000) 746–752

[29] E. Herrera-Viedma, S. Alonso, F. Chiclana, F. Herrera, A consensus model for group decision making with incomplete fuzzy preference relations, IEEE Transactions on Fuzzy Systems 15 (2007) 863–877.

[30] E. Herrera-Viedma, F. Herrera, F. Chiclana, A consensus model for multiperson decision making with different preference structures, IEEE Transactions on Systems, Man and Cybernetics Part A: Systems and Humans 32 (2002) 394–402.

[31] E. Herrera-Viedma, F. Herrera, F. Chiclana, M. Luque, Some issues on consistency of fuzzy preference relations, European Journal of Operational Research 154 (2004) 98–109.

[32] Y.-S. Huang, J.-T. Liao, Z.-L. Lin, A study on aggregation of group decisions, Systems Research and Behavioral Science 26 (2009) 445–454.

[33] L.C. Leung, D. Cao, On consistency and ranking of alternatives in fuzzy AHP, European Journal of Operational Research 124 (2000) 102–113.

[34] J.M. Moreno-Jiménez, J. Aguarón, M.T. Escobar, The core of consistency in AHP-group decision making, Group Decision and Negotiation 17 (2008) 249–265.

[35] R. Ramanathan, L.S. Ganesh, Group preference aggregation methods employed in AHP: an evaluation and intrinsic process for deriving members’ weightages, European Journal of Operational Research 79 (1994) 249–265.

[36] F.D. Robert, E.H. Forman, Group decision support with the analytic hierarchy process, Decision Support Systems 8 (2) (1992) 99–124.

[37] T.L. Saaty, The Analytic Hierarchy Process, McGraw-Hill, New York, 1980.

[38] T.L. Saaty, Decision-making with the AHP: why is the principal eigenvector necessary, European Journal of Operational Research 145 (2003) 85–91.

[39] B. Srdjevic, Linking analytic hierarchy process and social choice methods to support group decision-making in water management, Decision Support Systems 42 (2007) 2261–2273.

[40] T. Tanino, Fuzzy preference orderings in group decision making, Fuzzy Sets and Systems 12 (1984) 117–131.

[41] R.C. Van den Honert, Stochastic group preference modelling in the multiplicative AHP: a model of group consensus, European Journal of Operational Research 110 (1998) 99–111.

[42] Y.M. Wang, K.-S. Chin, G.K.K. Poon, A data envelopment analysis method with assurance region for weight generation in the analytic hierarchy process, Decision Support Systems 45 (2008) 913–921.

[43] Z.S. Xu, On consistency of the weighted geometric mean complex judgement matrix in AHP, European Journal of Operational Research 126 (2000) 683–687.

[44] Z.S. Xu, An automatic approach to reaching consensus in multiple attribute group decision making, Computers & Industrial Engineering 56 (4) (2009) 1369–1374.

[45] Z.S. Xu, C.P. Wei, A consistency improving method in analytic hierarchy process European Journal of Operational Research 116 (1999) 443–449.

[46] J.-M. Yeh, C. Lin, B. Kreng, J.-Y. Gee, A modi<sup>fi</sup>ed procedure for synthesising ratio judgements in the analytic hierarchy process, Journal of the Operational Research Society 50 (1999) 867–873

Yucheng Dong is an Assistant Professor at the School of Management, Xi'an Jiaotong University, Xi'an, China. He is a research fellow of the Department of Information Management, Oriental Institute of Technology, Taipei, Taiwan. He received his Ph.D. degree in management from Xi'an Jiaotong University in 2008. His current research interests include group decision making, computing with words, and on-line algorithm. His research results have been published in the European Journal of Operational Research IEEE Transactions on Fuzzy Systems, System Engineering and Electronics, and Fuzzy Sets and Systems, among others.

Guiqing Zhang is a PhD candidate at the School of Management, Xi'an Jiaotong University, Xi'an, China. She received her B.S. degree from the Department of Information and Computation Science, Chongqing University in 2004, and her M.S. degree from the Department of Applied Mathematics, Chongqing University in 2007. Her research interests include group decision making and decision support systems.

Wei-Chiang Hong is an Assistant Professor at the Department of Information Management, Oriental Institute of Technology, Taipei, Taiwan. He received his Ph.D. degree in management from Da Yeh University in 2008. He is the editor-in-chief of the International Journal of Applied Evolutionary Computation. His current research interests include decision analysis, evolutionary computation, and decision support systems. His research results have been published in Applied Mathematical Modelling, Electric Power Systems Research, International Journal of Electrical Power & Energy Systems, Energy Conversion and Management, and Applied Mathematics and Computation, among others.

Yinfeng Xu is a Professor at the School of Management, Xi'an Jiaotong University, Xi'an, China. He received his Ph.D. degree in operational research from the Academy of Mathematics and Systems Science, Chinese Academy of Sciences, in 1992. His current research interests include combinatorial optimization, theoretical computer science and decision analysis. His research results have been published in Theoretical Computer Science, Journal of Global Optimization, Information Processing Letters, Journal of Combinatorial Optimization, Discrete & Computational Geometry, European Journal of Operational Research, and IEEE Transactions on Fuzzy Systems, among others.
