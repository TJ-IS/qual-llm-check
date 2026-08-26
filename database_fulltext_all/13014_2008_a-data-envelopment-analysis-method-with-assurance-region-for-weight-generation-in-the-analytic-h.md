---
otero_id: 13014
otero_key: "EVAKAK92"
title: "A data envelopment analysis method with assurance region for weight generation in the analytic hierarchy process"
authors: "Ying-Ming Wang; Kwai-Sang Chin; Gary Ka Kwai Poon"
year: "2008"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2008.03.002"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A data envelopment analysis method with assurance region for weight generation in the analytic hierarchy process ☆

Ying-Ming Wang <sup>a,b,</sup>⁎, Kwai-Sang Chin <sup>b</sup>, Gary Ka Kwai Poon 1

<sup>a</sup> School of Management, Huazhong University of Science and Technology, Wuhan 430074, PR China

<sup>b</sup> Department of Manufacturing Engineering and Engineering Management, City University of Hong Kong, 83 Tat Chee Avenue, Kowloon Tong, Hong Kong, PR China

## a r t i c l e i n f o

Article history: Received 11 June 2007 Received in revised form 7 March 2008 Accepted 12 March 2008 Available online 20 March 2008

Keywords: Analytic hierarchy process Data envelopment analysis DEAHP Multiple criteria decision analysis Personal recruitment

## a b s t r a c t

Data envelopment analysis (DEA) has been combined with the analytic hierarchy process (AHP) to form a DEAHP for weight derivation and aggregation in the AHP. This paper proposes a DEA model with assurance region (AR) for priority derivation in the AHP, which is referred to as the DEA/AR model. This new DEA model can overcome the shortcomings of the DEAHP such as illogical local weights, over insensitivity to some comparisons, information loss, and overestimation of some local weights, and provide better priority estimate and better decision conclusions than the DEAHP. Numerical examples including a real application of the AHP to the recruitment of a research fellow for a research project are provided to show the advantages of the DEA/AR model and its potential applications in multiple criteria decision analysis (MCDA).

© 2008 Elsevier B.V. All rights reserved.

## 1. Introduction

As a simple and effective multiple criteria decisionmaking (MCDM) aid tool, analytic hierarchy process (AHP) has been extensively applied all over the world to a variety of <sup>fi</sup>elds such as agriculture [1], predictive maintenance [2], web service [6,15], medical and health care [7], water management [14], manufacturing, business, logistics and so on [4,18]. An important issue of applying the AHP is to determine local weights from pairwise comparison matrices. A signi<sup>fi</sup>cant number of approaches have been suggested in the AHP literature, each with some merits and demerits, but none of them can be declared as the best. Although the eigenvector method (EM) is strongly recommended and preferred by

Saaty [11], there is no wide agreement about its superiority (see Mikhailov [8] and Srdjevic [13] for example).

Very recently, Ramanathan [10] developed a DEAHP method for weight derivation and aggregation in the AHP, which views each decision criterion or alternative in a pairwise comparison matrix as a decision making unit (DMU), the row elements of the pairwise comparison matrix as the outputs of the DMUs, and uses a dummy input that has a constant value of one for all the DMUs to build an inputoriented CCR model [3] for each DMU. The best relative ef<sup>fi</sup>ciency of each DMU is then de<sup>fi</sup>ned as the local weight of the DMU. The DEAHP proved to be able to produce true weights for perfectly consistent pairwise comparison matrices and has been applied to supplier selection by Sevkli et al. [12].

However, the DEAHP has also been found to have some drawbacks. The most signi<sup>fi</sup>cant drawback is that the DEAHP may produce counterintuitive local weights for inconsistent pairwise comparison matrices. Another signi<sup>fi</sup>cant drawback is that the DEAHP is sometimes over insensitive to some comparisons in a pairwise comparison matrix. These drawbacks will be analyzed later.

To overcome these drawbacks of the DEAHP, we propose in this paper a DEA method with assurance region for weight generation in the AHP, which builds an assurance region (AR) for the DEAHP model so that local weights can be better generated. The resultant model is referred to as DEA/AR model, which turns out to be able to eliminate the abovementioned drawbacks of the DEAHP.

The paper is organized as follows. In Section 2 we brie<sup>fl</sup>y review the DEAHP and analyze its main drawbacks numerically. We then develop the DEA/AR model for the AHP in Section 3. Numerical examples are provided and examined in Section 4. The paper is concluded in Section 5.

## 2. DEAHP and its main drawbacks

Let $\pmb { A } = ( a _ { i j } ) _ { n \times n }$ be a pairwise comparison matrix with $a _ { i i } = 1$ and $a _ { i j } { = } 1 / a _ { i j } { > } 0$ for $j { \neq } i$ and $\pmb { W } \mathrm { = } ( w _ { 1 } , . . . , w _ { n } ) ^ { \mathrm { T } }$ be its weight vector. The DEAHP views each row of the matrix A as a DMU, representing a decision criterion or alternative, each row element as an output and assumes a dummy constant input of one for all the DMUs. Each DMU has n outputs and one dummy constant input, based on which the following inputoriented CCR model [10] is built to derive the local weights of the pairwise comparison matrix $\pmb { \Lambda } ;$

$$
\begin{array}{l} \text { Maximize } w _ {0} = \sum_ {j = 1} ^ {n} a _ {0 j} v _ {j} \\ \text { Subject   to } \left\{ \begin{array}{l} u _ {1} = 1, \\ \sum_ {j = 1} ^ {n} a _ {i j} v _ {j} - u _ {1} \leq 0, \quad i = 1, \dots , n, \\ u _ {1}, v _ {j} \geq 0, \quad j = 1, \dots , n, \end{array} \right. \end{array}\tag{1}
$$

where DMU refers to the criterion or alternative under evaluation. The optimum value w⁎ represents the DEA ef<sup>fi</sup>ciency of $\boldsymbol { \mathrm { D M U } } _ { 0 }$ and is viewed as its local weight. The linear programming model (1) is solved for all the DMUs to generate the weight vector $\mathbf { \dot { W } } ^ { * } = ( w _ { 1 } ^ { * } , . . . , w _ { n } ^ { * } ) ^ { T }$ of A. It was proved that the DEAHP could derive true weights if A is a perfectly consistent pairwise comparison matrix, i.e. $a _ { i j } { = } a _ { i k } a _ { k j }$ for all $i , j , k { = } 1 , . . . , n .$

In a hierarchical structure, the DEAHP offers the following two DEA models to aggregate local weights into global weights:

$$
\begin{array}{l l} \text { Maximize } & \sum_ {j = 1} ^ {m} w _ {0 j} v _ {j} \\ \text { Subject   to } & \left\{ \begin{array}{l} u _ {1} = 1, \\ \sum_ {j = 1} ^ {m} w _ {i j} v _ {j} - u _ {1} \leq 0, \quad i = 1, \ldots , n, \\ u _ {1}, v _ {j} \geq 0, \quad j = 1, \ldots , n, \end{array} \right. \end{array}\tag{2}
$$

and

Maximize $\nu _ { 1 } \left( \sum _ { j = 1 } ^ { m } w _ { 0 j } d _ { j } \right)$

$$
\text { Subject   to } \quad \left\{ \begin{array}{l} u _ {1} = 1, \\ v _ {1} \left(\sum_ {j = 1} ^ {m} w _ {i j} d _ {j}\right) - u _ {1} \leq 0, \quad i = 1, \dots , n, \\ u _ {1}, v _ {1} \geq 0, \end{array} \right.\tag{3}
$$

where v $( j = 1 , . . . , m )$ are decision variables, $d _ { j } = w j / w 1 ( j = 1 , . . . , m )$ are the values computed from the local weights of decision criteria, wij $( i { = } 1 , { \ldots } , n , j { = } 1 , { \ldots } , m )$ are the local weights of the ith decision alternative with respect to the jth decision criterion, and the subscript zero in objective functions refers to the decision alternative under evaluation, i.e. the DMU0 in DEA.

Model (2) determines global weights without consideration of the local weights of decision criteria, while model (3) determines global weights by maintaining the quantitative relationships among the local weights of decision criteria unchanged, i.e. $\nu _ { i } / \nu _ { 1 } \equiv w _ { i } / w _ { 1 } \mathrm { f o r } j = 1 , . . . , m$ . It was suggested by Ramanathan [10] that model $( 2 )$ should be preferred when calculating the <sup>fi</sup>nal weights of decision alternatives. If criteria weights are important and there is a strong reason to consider them, Ramanathan [10] suggested that the <sup>fi</sup>nal weights calculated with and without consideration of criteria weights should be presented together.

As mentioned before, the DEAHP suffers from some drawbacks. The most signi<sup>fi</sup>cant drawback is that the DEAHP may produce counterintuitive local weights for inconsistent pairwise comparison matrices. Consider for example the following pairwise comparison matrix:

$$
\mathbf {A} = \left[ \begin{array}{c c c c c c} 1 & 4 & 1 & 1 & 3 & 4 \\ 1 / 4 & 1 & 7 & 3 & 1 / 5 & 1 \\ 1 & 1 / 7 & 1 & 1 / 5 & 1 / 5 & 1 / 6 \\ 1 & 1 / 3 & 5 & 1 & 1 & 1 / 3 \\ 1 / 3 & 5 & 5 & 1 & 1 & 3 \\ 1 / 4 & 1 & 6 & 3 & 1 / 3 & 1 \end{array} \right].
$$

which is inconsistent $\scriptstyle \left( \mathbf { C } \mathbf { R } = 0 . 3 4 0 9 > 0 . 1 \right)$ . For this inconsistent pairwise comparison matrix, the DEAHP produces the weight vector (1, 1, 1, 1, 1, 1) for the six criteria or alternatives. Such a weight vector obviously makes no sense and is irrational. It is this drawback that restricts the applications of the DEAHP.

Another signi<sup>fi</sup>cant drawback of the DEAHP is that the DEAHP is sometimes over insensitive to some comparisons in a pairwise comparison matrix. Consider for instance the following inconsistent pairwise comparison matrices:

$$
\begin{array}{l} \mathbf {B} = \left[ \begin{array}{c c c} 1 & 2 & 5 \\ 1 / 2 & 1 & 3 \\ 1 / 5 & 1 / 3 & 1 \end{array} \right], \quad \mathbf {C} = \left[ \begin{array}{c c c} 1 & 5 & 5 \\ 1 / 5 & 1 & 3 \\ 1 / 5 & 1 / 3 & 1 \end{array} \right], \\ \mathbf {D} = \left[ \begin{array}{c c c} 1 & 9 & 5 \\ 1 / 9 & 1 & 3 \\ 1 / 5 & 1 / 3 & 1 \end{array} \right]. \end{array}
$$

For these three inconsistent pairwise comparison matrices, no matter how different they are, the DEAHP produces exactly the same weight vector (1, 0.6, 0.2) for them. Apparently, the DEAHP weights are not sensitive to the changes of $b _ { 1 2 } , c _ { 1 2 }$ and $d _ { 1 2 } .$ . This drawback also restricts the applications of the DEAHP.

It is also observed that the DEAHP weights (1, 0.6, 0.2) are actually the normalization of the last column of the above three inconsistent pairwise comparison matrices, which means that only part of information in a pairwise comparison matrix is effectively utilized by the DEAHP and all the other information is lost or not working. This leads to the third signi<sup>fi</sup>cant drawback of the DEAHP. That is the DEAHP cannot make the best use of all the pairwise comparison information in a pairwise comparison matrix.

In the next section, we will develop a DEA model with assurance region for weight generation in the AHP to overcome the above-mentioned drawbacks.

## 3. DEA/AR model for the AHP

Before developing the DEA/AR model, we <sup>fi</sup>rst introduce the lemma below.

Lemma 1. Let $\pmb { A } = ( a _ { i j } ) _ { n \times n }$ be a nonnegative matrix with nonzero row sums $r _ { 1 } , . . . , r _ { 2 }$ and maximal eigenvalue $\lambda _ { \operatorname* { m a x } } .$ Then [9]

$$
\min _ {i} \left(\frac {1}{r _ {i}} \sum_ {j = 1} ^ {n} a _ {i j} r _ {j}\right) \leq \lambda_ {\max} \leq \max _ {i} \left(\frac {1}{r _ {i}} \sum_ {j = 1} ^ {n} a _ {i j} r _ {j}\right).\tag{4}
$$

Since the nonnegative matrix A and its transpose $\pmb { A } ^ { \mathrm { T } }$ have the same maximal eigenvalue, the above inequality also holds for the transpose of A, i.e.

$$
\min _ {i} \left(\frac {1}{c _ {i}} \sum_ {j = 1} ^ {n} a _ {i j} c _ {j}\right) \leq \lambda_ {\max} \leq \max _ {i} \left(\frac {1}{c _ {i}} \sum_ {j = 1} ^ {n} a _ {i j} c _ {j}\right),\tag{5}
$$

where $c _ { 1 } , . . . , c _ { n }$ are the column sums of A.

Apparently, pairwise comparison matrices are nonnegative matrices. Consider the following characteristic equation for the pairwise comparison matrix $\begin{array} { r } { \mathbf { A } { } = ( a _ { i j } ) _ { n \times n } \colon } \end{array}$

$$
\sum_ {j = 1} ^ {n} a _ {i j} w _ {j} = \lambda_ {\max} w _ {i}, \quad i = 1, \dots , n,\tag{6}
$$

where $\lambda _ { \mathrm { m a x } }$ is the maximal eigenvalue of A. Eq. (6) can be rewritten as

$$
\sum_ {j = 1} ^ {n} a _ {i j} \left(w _ {j} / \lambda_ {\max}\right) = w _ {i}, i = 1, \dots , n.\tag{7}
$$

Let

$$
v _ {j} = \frac {w _ {j}}{\lambda_ {\max}}, \quad j = 1, \dots , n.\tag{8}
$$

Then, Eq. (7) can be equivalently expressed as

$$
\sum_ {j = 1} ^ {n} a _ {i j} v _ {j} = w _ {i}, i = 1, \dots , n.\tag{9}
$$

For any n-order pairwise comparison matrix, it has already been known that $\lambda _ { \operatorname* { m a x } } 2 n$ . By Lemma 1, the upper bound of $\lambda _ { \mathrm { m a x } }$ can also be determined. Let $\beta$ be the upper bound for $\lambda _ { \mathrm { m a x } }$ determined by Lemma 1. Then, we have $n { \leq } \lambda _ { \operatorname* { m a x } } { \leq } \beta .$ By Eq. $( 8 ) , n { \le } \lambda _ { \mathrm { m a x } } { \le } \beta$ can be equivalently expressed as n≤w / $\nu _ { j } { \le } \beta$ for $j = 1 , . . . , n$ . That is

$$
w _ {j} / \beta \leq v _ {j} \leq w _ {j} / n, j = 1, \dots , n,\tag{10}
$$

which are the constraints called assurance region (AR) [16,17] we derived for each decision variable $\nu _ { j } \left( j = 1 , . . . , n \right)$ . Combining Eqs. (9) and (10), we have the following DEA/AR model for the pairwise comparison matrix $\begin{array} { r } { \pmb { A } = ( a _ { i j } ) _ { n \times n } \mathrm { . } } \end{array}$

Maximize $w _ { 0 }$

$$
\text { Subject   to } \quad \left\{ \begin{array}{l l} w _ {i} = \sum_ {j = 1} ^ {n} a _ {i j} v _ {j} \leq 1, & i = 1, \ldots , n, \\ w _ {j} / \beta \leq v _ {j} \leq w _ {j} / n, & j = 1, \ldots , n, \end{array} \right.\tag{11}
$$

where subscript zero refers to the decision criterion or alternative under evaluation and $\beta$ is the upper bound determined by Lemma 1. That is

$$
\beta = \min \left\{\max _ {i} \left(\frac {1}{r _ {i}} \sum_ {j = 1} ^ {n} a _ {i j} r _ {j}\right), \quad \max _ {i} \left(\frac {1}{c _ {i}} \sum_ {j = 1} ^ {n} a _ {i j} c _ {j}\right) \right\},\tag{12}
$$

where $r _ { 1 } , \ldots , r _ { n }$ and $c _ { 1 } , . . . , c _ { n }$ are respectively the row sums and column sums of the pairwise comparison matrix $\pmb { A } = ( a _ { i j } ) _ { n \times n } . \mathsf { W e }$ refer to the method that utilizes model (11) to derive weights from pairwise comparison matrices as the DEA/AR method and the resultant weights as DEA/AR weights.

With regard to the DEA/AR method, we have the following theorem.

Theorem 1. If $\pmb { A } = ( a _ { i j } ) _ { n \times s n }$ is a perfectly consistent pairwise comparison matrix, then DEA/AR model (11) produces weights:

$$
w _ {i} ^ {*} = w _ {i} / \max _ {j \in \{1, \dots , n \}} \left\{w _ {j} \right\}, i = 1, \dots , n,\tag{13}
$$

which are a normalization of the true weight $w _ { i } ( i { = } 1 , . . . , n )$ of the pairwise comparison matrix A.

Proof. Since A is a perfectly consistent pairwise comparison matrix, it can be characterized by the eigenvector weights w $1 / \sum _ { i = 1 } ^ { n } a _ { i j } ( j = 1 , . . . , n )$ as $a _ { i j } = w _ { i } / w _ { j } ( i , j = 1 , . . . , n ) .$ . Accordingly, $\sum _ { j = 1 } ^ { n } a _ { i j } v _ { j } = \sum _ { j = 1 } ^ { n } \ \left( w _ { i } / w _ { j } \right) v _ { j } = w _ { i } \sum _ { j = 1 } ^ { n } \ \left( v _ { j } / w _ { j } \right) \le 1 ( i = 1 , . . . , n ) ,$ , from <sup>¼ ¼</sup>which it can be derived that $\sum _ { j = 1 } ^ { n } \big ( \boldsymbol { \nu } _ { j } / \boldsymbol { w } _ { j } \big ) { \leq } 1 / \boldsymbol { w } _ { i }$ for all $i { = } 1 , \ldots$ n. That is $\sum _ { j = 1 } ^ { n } \ \big ( \boldsymbol { \nu } _ { j } / \boldsymbol { w } _ { j } \big ) { \le \operatorname* { m i n } _ { i } } ( 1 / \boldsymbol { w } _ { i } ) = 1 / \operatorname* { m a x } _ { j \in \{ 1 , \ \dots , n \} } \big \{ \boldsymbol { w } _ { j } \big \}$ . Thus, the <sup>¼</sup>maximum objective function value of Eq. (11) can be obtained as $\begin{array} { l } { { w _ { 0 } ^ { * } = w _ { 0 } \displaystyle \sum _ { j = 1 } ^ { n } \left( \nu _ { j } ^ { * } / w _ { j } \right) = w _ { 0 } / \operatorname* { m a x } _ { j \in \{ 1 , \dots , n \} } \left\{ w _ { j } \right\} } } \\  { w _ { n } \} . } \end{array}$ , where $\boldsymbol { w } _ { 0 } \in \{ \boldsymbol { w } _ { 1 } , \ldots ,$ □

Theorem 1 shows that DEA/AR model can produce true weights for perfectly consistent pairwise comparison matrices. For inconsistent pairwise comparison matrices, due to the role of assurance region DEA/AR model is able to produce rational, logical and intuitive weights consistent with decision makers' (DMs) subjective judgments. This will be illustrated through numerical examples in the next section.

In the case of hierarchical structures, local weights need to be aggregated into global weights. Let $w _ { 1 } , . . . , w _ { m }$ be the local weights of m decision criteria and $w _ { 1 j } , . . . , w _ { n j }$ be the local weights of n decision alternatives with respect to the jth criterion $( j = 1 , \ldots , m )$ . All of them are assumed to have already been generated by solving DEA/AR model (11) and form a decision matrix, as shown in Table 1, based on which the global weight of each decision alternative can be computed using the simple additive weighting (SAW) method [5] in MCDM and then normalized to their maximum. That is

$$
w _ {\mathbf {A} _ {i}} ^ {*} = \frac {\sum_ {j = 1} ^ {m} w _ {i j} w _ {j}}{\max _ {k \in \{1 , \dots , n \}} \left\{\sum_ {j = 1} ^ {m} w _ {k j} w _ {j} \right\}}, \quad i = 1, \dots , n.\tag{14}
$$

Table 1  
Aggregation of local DEA/AR weights

<table><tr><td rowspan="2">Alternative</td><td colspan="4">Criteria</td><td colspan="2">Global weights</td></tr><tr><td> $w_1$ </td><td> $w_2$ </td><td>...</td><td> $w_m$ </td><td>Non-normalized</td><td>Normalized</td></tr><tr><td> $A_1$ </td><td> $w_{11}$ </td><td> $w_{12}$ </td><td>...</td><td> $w_{1m}$ </td><td> $\sum_{j=1}^{m} w_{1j}w_j$ </td><td> $\sum_{j=1}^{m} w_{1j}w_j / \max_i \left\{ \sum_{j=1}^{m} w_{ij}w_j \right\}$ </td></tr><tr><td> $A_2$ </td><td> $w_{21}$ </td><td> $w_{22}$ </td><td>...</td><td> $w_{2m}$ </td><td> $\sum_{j=1}^{m} w_{2j}w_j$ </td><td> $\sum_{j=1}^{m} w_{2j}w_j / \max_i \left\{ \sum_{j=1}^{m} w_{ij}w_j \right\}$ </td></tr><tr><td> $\vdots$ </td><td> $\vdots$ </td><td> $\vdots$ </td><td> $\vdots$ </td><td> $\vdots$ </td><td> $\vdots$ </td><td> $\vdots$ </td></tr><tr><td> $A_n$ </td><td> $w_{n1}$ </td><td> $w_{n2}$ </td><td>...</td><td> $w_{nm}$ </td><td> $\sum_{j=1}^{m} w_{nj}w_j$ </td><td> $\sum_{j=1}^{m} w_{nj}w_j / \max_i \left\{ \sum_{j=1}^{m} w_{ij}w_j \right\}$ </td></tr></table>

These results are exactly the same as those obtained by solving model (3). As a matter of fact, from model (3) it can be derived that

$$
v _ {1} \leq \frac {u _ {1}}{\sum_ {j = 1} ^ {m} w _ {i j} d _ {j}} = \frac {1}{\sum_ {j = 1} ^ {m} w _ {i j} d _ {j}}, i = 1, \dots , n,
$$

which can be equivalently expressed as

$$
v _ {1} \leq \min _ {i \in \{1, \dots , n \}} \left\{\frac {1}{\sum_ {j = 1} ^ {m} w _ {i j} d _ {j}} \right\} = \frac {1}{\max _ {i \in \{1 , \dots , n \}} \left\{\sum_ {j = 1} ^ {m} w _ {i j} d _ {j} \right\}}
$$

To make the objective function of Eq. (3) achieve its maximum value, $\nu _ { 1 }$ has to take its upper bound value. That is

$$
v _ {1} ^ {*} = \frac {1}{\max _ {i \in \{1 , \dots , n \}} \left\{\sum_ {j = 1} ^ {m} w _ {i j} d _ {j} \right\}}
$$

Accordingly, the maximum objective function value of Eq. (3) is computed as

$$
\begin{array}{l} w _ {\mathbf {A} _ {0}} ^ {*} = v _ {1} ^ {*} \left(\sum_ {j = 1} ^ {m} w _ {0 j} d _ {j}\right) = \frac {\sum_ {j = 1} ^ {m} w _ {0 j} d _ {j}}{\underset {i \in \{1 , \ldots , n \}} {\max} \left\{\sum_ {j = 1} ^ {m} w _ {i j} d _ {j} \right\}} \\ = \frac {\sum_ {j = 1} ^ {m} w _ {0 j} (w _ {j} / w _ {1})}{\underset {i \in \{1 , \ldots , n \}} {\max} \left\{\sum_ {j = 1} ^ {m} w _ {i j} (w _ {j} / w _ {1}) \right\}} \\ = \frac {\sum_ {j = 1} ^ {m} w _ {0 j} w _ {j}}{\underset {i \in \{1 , \ldots , n \}} {\max} \left\{\sum_ {j = 1} ^ {m} w _ {i j} w _ {j} \right\}}. \end{array}
$$

It is obvious that Eq. (14) is more convenient and more practical than model (3) and has no need to solve any programming models.

## 4. Numerical examples

In this section we provide two numerical examples to illustrate the advantages of the proposed DEA/AR model and its potential applications in multiple criteria decision analysis (MCDA).

Example 1. Re-examine the pairwise comparison matrices A, B, C, and D in Section 2.

For the pairwise comparison matrix $\mathbf A , \beta$ is determined by Eq. (12) as 11.7883. Accordingly, the DEA/AR model (11) can be written as

Maximize $w _ { 0 }$

$$
\text { Subject   to } \left\{ \begin{array}{l} v _ {1} + 4 v _ {2} + v _ {3} + v _ {4} + 3 v _ {5} + 4 v _ {6} - w _ {1} = 0, \\ \frac {1}{4} v _ {1} + v _ {2} + 7 v _ {3} + 3 v _ {4} + \frac {1}{5} v _ {5} + v _ {6} - w _ {2} = 0, \\ v _ {1} + \frac {1}{7} v _ {2} + v _ {3} + \frac {1}{5} v _ {4} + \frac {1}{5} v _ {5} + \frac {1}{6} v _ {6} - w _ {3} = 0, \\ v _ {1} + \frac {1}{3} v _ {2} + 5 v _ {3} + v _ {4} + v _ {5} + \frac {1}{3} v _ {6} - w _ {4} = 0, \\ \frac {1}{3} v _ {1} + 5 v _ {2} + 5 v _ {3} + v _ {4} + v _ {5} + 3 v _ {6} - w _ {5} = 0, \\ \frac {1}{4} v _ {1} + v _ {2} + 6 v _ {3} + 3 v _ {4} + \frac {1}{3} v _ {5} + v _ {6} - w _ {6} = 0, \\ v _ {i} - \frac {1}{1 1 . 7 8 8 3} w _ {i} \geq 0, \quad i = 1, \dots , 6, \\ v _ {i} - \frac {1}{6} w _ {i} \leq 0, \quad i = 1, \dots , 6, \\ w _ {i} \leq 1, \quad i = 1, \dots , 6 \end{array} \right..
$$

Let $\scriptstyle w _ { 0 } = w _ { 1 } , \dotsc , w _ { 6 } ,$ , respectively, and solve the above DEA/AR model. We get the local weight vector of A as (1, 0.734, 0.260, 0.581, 0.942, 0.704), which ranks the six decision criteria or alternatives as $C _ { 1 } { > } C _ { 5 } { > } C _ { 2 } { > } C _ { 6 } { > } C _ { 4 } { > } C _ { 3 }$ , where $" \succ "$ means “is preferred to”. Such a ranking is consistent with the ranking generated by the eigenvector method (EM), which produces the eigenvector weights (0.289, 0.147, 0.057, 0.128, 0.236, 0.144) for A. After normalization to their maximum, the eigenvector weights become (1, 0.509, 0.198, 0.441, 0.816, 0.498), which is close to the weight vector produced by the DEA/AR model.

The DM's subjective preferences can be approximately analyzed as follows. From the pairwise comparison matrix A, it is easy to see that $C _ { 1 }$ is the most important criterion or alternative because its row elements are all greater than or equal to one and can be removed from the pairwise comparison matrix, leading to a reduced pairwise comparison matrix. In this reduced pairwise comparison matrix, ${ \mathsf C } _ { 5 }$ appears as the most important criterion or alternative and should be ranked in the second place. Removing ${ \mathsf { C } } _ { 5 }$ from the further consideration leads to a new further reduced pairwise comparison matrix. From this reduced pairwise comparison matrix, it is observed that ${ \sf C } _ { 2 }$ is weakly important than $C _ { 6 }$ because it is seven times as important as ${ \sf C } _ { 3 }$ while $C _ { 6 }$ is only six times as important as $\mathsf { C } _ { 3 } . \mathsf { S } 0 , \mathsf { C } _ { 2 }$ and $C _ { 6 }$ are respectively the third and fourth most important criteria or alternatives. The left two criteria or alternatives ${ \sf C } _ { 3 }$ and $\mathsf { C } _ { 4 }$ are very easy to be ranked as $C _ { 4 } { \succ } C _ { 3 }$ in terms of their direct comparisons $a _ { 3 4 } = 1 / 5$ and $a _ { 4 3 } = 5 .$ . Thus, the ranking of the six criteria or alternatives can be roughly inferred as $C _ { 1 } { > } C _ { 5 } { > } C _ { 2 } { > } C _ { 6 } { > } C _ { 4 } { > } C _ { 3 }$ , which is consistent with the ranking generated by the DEA/AR model.

Local weights of the pairwise comparison matrices (A, B, C, D) produced by different models

<table><tr><td>Comparison matrix</td><td> $w_1$ </td><td> $w_2$ </td><td> $w_3$ </td><td> $w_4$ </td><td> $w_5$ </td><td> $w_6$ </td></tr><tr><td colspan="7">A: Local weights produced by the DEAHP model</td></tr><tr><td>A</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td></tr><tr><td>B</td><td>1</td><td>0.6</td><td>0.2</td><td>-</td><td>-</td><td>-</td></tr><tr><td>C</td><td>1</td><td>0.6</td><td>0.2</td><td>-</td><td>-</td><td>-</td></tr><tr><td>D</td><td>1</td><td>0.6</td><td>0.2</td><td>-</td><td>-</td><td>-</td></tr><tr><td colspan="7">B: Local weights produced by the eigenvector model (EM)</td></tr><tr><td>A</td><td>0.289</td><td>0.147</td><td>0.057</td><td>0.128</td><td>0.236</td><td>0.144</td></tr><tr><td>B</td><td>0.582</td><td>0.309</td><td>0.109</td><td>-</td><td>-</td><td>-</td></tr><tr><td>C</td><td>0.701</td><td>0.202</td><td>0.097</td><td>-</td><td>-</td><td>-</td></tr><tr><td>D</td><td>0.764</td><td>0.149</td><td>0.087</td><td>-</td><td>-</td><td>-</td></tr><tr><td colspan="7">C: Local weights produced by the eigenvector model (EM) (rescaled)</td></tr><tr><td>A</td><td>1</td><td>0.509</td><td>0.198</td><td>0.441</td><td>0.816</td><td>0.498</td></tr><tr><td>B</td><td>1</td><td>0.531</td><td>0.188</td><td>-</td><td>-</td><td>-</td></tr><tr><td>C</td><td>1</td><td>0.288</td><td>0.139</td><td>-</td><td>-</td><td>-</td></tr><tr><td>D</td><td>1</td><td>0.195</td><td>0.114</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Comparison matrix</td><td> $\beta$ </td><td> $w_1$ </td><td> $w_2$ </td><td> $w_3$ </td><td> $w_4$ </td><td> $w_5$ </td></tr><tr><td colspan="7">D: Local weights produced by the DEA/AR model</td></tr><tr><td>A</td><td>11.7883</td><td>1</td><td>0.734</td><td>0.260</td><td>0.581</td><td>0.942</td></tr><tr><td>B</td><td>3.0556</td><td>1</td><td>0.531</td><td>0.188</td><td>-</td><td>-</td></tr><tr><td>C</td><td>3.6061</td><td>1</td><td>0.295</td><td>0.143</td><td>-</td><td>-</td></tr><tr><td>D</td><td>3.9778</td><td>1</td><td>0.213</td><td>0.125</td><td>-</td><td>-</td></tr></table>

This shows that the DEA/AR model can produce the local weights consistent with the DM's subjective preferences.

For the pairwise comparison matrices B, C and D, their local weights produced by the DEA/AR model are all presented in Table 2, from which it can be seen that the weights produced by the DEA/AR model are sensitive enough to the changes of comparison elements $b _ { 1 2 } , c _ { 1 2 }$ and $d _ { 1 2 } .$ . When they vary from 2 to 9, the weight for the second criterion or alternative also changes from 0.531 to 0.213. It is obvious that the DEA/AR model better re<sup>fl</sup>ects the changes of pairwise comparisons in a pairwise comparison matrix than the DEAHP.

To check the information utilized by the two different models, we show in Table 3 the values of decision variables $\nu _ { j } ( j { = } 1 , . . . , n )$ in different solution processes and different pairwise comparison matrices, from which it can be seen clearly that the DEAHP uses only some of pairwise comparisons for weight derivation. This is the reasonwhy the DEAHP results in too many decision criteria or alternatives being DEA ef<sup>fi</sup>cient. However, due to the role or restriction of assurance region, the DEA/AR model is able to use all the pairwise comparison information for priority derivation. This ensures that the DEA/AR model derives rational and logical weights consistent with DMs' subjective judgments.

To check further the quality of the local weights derived by the DEA/AR model against the standard eigenvector method, we show in Table 4 the <sup>fi</sup>tting performances of the EM, DEAHP and DEA/AR weights for the four pairwise comparison matrices, where the <sup>fi</sup>tting performances are measured by the following Euclidean distance:

$$
\mathrm{FP} = \sqrt {\frac {1}{n ^ {2}} \sum_ {i = 1} ^ {n} \sum_ {j = 1} ^ {n} \left(a _ {i j} - w _ {i} / w _ {j}\right) ^ {2}}, \quad a _ {i j} \in \mathbf {A}, \mathbf {B}, \mathbf {C}, \mathbf {D}.\tag{15}
$$

As can be seen from Table 4, the DEA/AR weights perform as well as or even better than the EM weights in <sup>fi</sup>tting pairwise comparison matrices. It is also observed that the DEAHP weights perform well for the pairwise comparison matrix B which is nearly perfectly consistent, but poorly for the other inconsistent pairwise comparison matrices.

Information utilization by the DEAHP and DEA/AR model

<table><tr><td rowspan="2">Comparison matrix</td><td rowspan="2">Objective function</td><td colspan="6">DEAHP</td><td colspan="6">DEA/AR model</td></tr><tr><td> ${v}_{1}$ </td><td> ${v}_{2}$ </td><td> ${v}_{3}$ </td><td> ${v}_{4}$ </td><td> ${v}_{5}$ </td><td> ${v}_{6}$ </td><td> ${v}_{1}$ </td><td> ${v}_{2}$ </td><td> ${v}_{3}$ </td><td> ${v}_{4}$ </td><td> ${v}_{5}$ </td><td> ${v}_{6}$ </td></tr><tr><td rowspan="6">A</td><td> ${w}_{1}$ </td><td>0</td><td>0.182</td><td>0</td><td>0</td><td>0.091</td><td>0</td><td>0.085</td><td>0.073</td><td>0.027</td><td>0.036</td><td>0.136</td><td>0.038</td></tr><tr><td> ${w}_{2}$ </td><td>0</td><td>0</td><td>0.143</td><td>0</td><td>0</td><td>0</td><td>0.147</td><td>0.062</td><td>0.040</td><td>0.093</td><td>0.077</td><td>0.060</td></tr><tr><td> ${w}_{3}$ </td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0.167</td><td>0.061</td><td>0.043</td><td>0.080</td><td>0.077</td><td>0.058</td></tr><tr><td> ${w}_{4}$ </td><td>0.071</td><td>0</td><td>0.133</td><td>0</td><td>0.265</td><td>0</td><td>0.167</td><td>0.061</td><td>0.043</td><td>0.080</td><td>0.077</td><td>0.058</td></tr><tr><td> ${w}_{5}$ </td><td>0</td><td>0.2</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0.085</td><td>0.097</td><td>0.027</td><td>0.069</td><td>0.080</td><td>0.048</td></tr><tr><td> ${w}_{6}$ </td><td>0</td><td>0</td><td>0</td><td>0.333</td><td>0</td><td>0</td><td>0.147</td><td>0.062</td><td>0.040</td><td>0.093</td><td>0.077</td><td>0.060</td></tr><tr><td rowspan="3">B</td><td> ${w}_{1}$ </td><td>0</td><td>0</td><td>0.2</td><td></td><td></td><td></td><td>0.333</td><td>0.176</td><td>0.062</td><td></td><td></td><td></td></tr><tr><td> ${w}_{2}$ </td><td>0</td><td>0</td><td>0.2</td><td></td><td></td><td></td><td>0.333</td><td>0.176</td><td>0.063</td><td></td><td></td><td></td></tr><tr><td> ${w}_{3}$ </td><td>0</td><td>0</td><td>0.2</td><td></td><td></td><td></td><td>0.333</td><td>0.176</td><td>0.063</td><td></td><td></td><td></td></tr><tr><td rowspan="3">C</td><td> ${w}_{1}$ </td><td>0</td><td>0.2</td><td>0</td><td></td><td></td><td></td><td>0.290</td><td>0.097</td><td>0.045</td><td></td><td></td><td></td></tr><tr><td> ${w}_{2}$ </td><td>0</td><td>0</td><td>0.2</td><td></td><td></td><td></td><td>0.333</td><td>0.086</td><td>0.048</td><td></td><td></td><td></td></tr><tr><td> ${w}_{3}$ </td><td>0</td><td>0</td><td>0.2</td><td></td><td></td><td></td><td>0.333</td><td>0.086</td><td>0.048</td><td></td><td></td><td></td></tr><tr><td rowspan="3">D</td><td> ${w}_{1}$ </td><td>0</td><td>0.111</td><td>0</td><td></td><td></td><td></td><td>0.333</td><td>0.059</td><td>0.027</td><td></td><td></td><td></td></tr><tr><td> ${w}_{2}$ </td><td>0</td><td>0</td><td>0.2</td><td></td><td></td><td></td><td>0.333</td><td>0.051</td><td>0.042</td><td></td><td></td><td></td></tr><tr><td> ${w}_{3}$ </td><td>1</td><td>0</td><td>0</td><td></td><td></td><td></td><td>0.333</td><td>0.051</td><td>0.042</td><td></td><td></td><td></td></tr></table>

Table 4  
Fitting performances by different local weights

<table><tr><td rowspan="2">Comparison matrix</td><td rowspan="2">CR</td><td colspan="3">Fitting performance (FP) by</td></tr><tr><td>EM weights</td><td>DEAHP weights</td><td>DEA/AR weights</td></tr><tr><td>A</td><td>0.3409</td><td>1.6077</td><td>2.0361</td><td>1.5793</td></tr><tr><td>B</td><td>0.0032</td><td>0.1282</td><td>0.1160</td><td>0.1282</td></tr><tr><td>C</td><td>0.1169</td><td>0.9498</td><td>1.1191</td><td>0.9115</td></tr><tr><td>D</td><td>0.2797</td><td>1.8544</td><td>2.4499</td><td>1.8041</td></tr></table>

Example 2. A department in a prestigious university needs to recruit a research fellow to conduct a research project for three years. After an initial screening, three candidates are short-listed for interview. The criteria that an interview panel consisting of three professors from the department considers include Qualifications $( \mathsf { C } _ { 1 } ) _ { 1 }$ , Personal Qualities $( \mathsf { C } _ { 2 } ) ,$ Research Experience $( \mathsf { C } _ { 3 } ) ,$ , Skills and Abilities $( { \mathsf { C } } _ { 4 } ) ,$ , and Capacity for Career Development $( \mathsf C _ { 5 } ) ,$ , as shown in Fig. 1. The <sup>fi</sup>ve selection criteria are described in details in Table 5. The pairwise comparison matrices for the <sup>fi</sup>ve selection criteria and three candidates provided by the interview panel are presented in Tables 6 and 7. If the panel members cannot reach a consensus and disagree with one another on some comparison(s), then their geometric averages or weighted geometric averages should be used for the comparison(s).

For the pairwise comparison matrices in Tables 6 and 7, their local weights are computed using three different priority methods: eigenvector method (EM), DEAHP, and DEA/AR method for the purpose of comparison, where the EM weights are normalized in two ways. One is to normalize the EM weights to sum to one and the other is to normalize the EM weights to their maximum. All the local weights are then aggregated using Eq. (14) into global weights. The results are shown in Table 8, from which it is found that the EM and DEA/ AR method both evaluate Candidate B as the best candidate, while the DEAHP evaluates Candidate C as the best.

To <sup>fi</sup>nd out the reasons why the three methods result in two different decision conclusions, we look into the local weights of pairwise comparison matrices and observe their differences among the three methods. From Tables 6 and 7, the following observations have been made:

• The DEAHP evaluates ${ { \mathsf { C } } _ { 3 } }$ (Research Experience) and $\mathsf { C } _ { 4 }$ (Skills and Abilities) to be as important as each other and both to be the most important criterion, however, the two selection criteria are not equally important in terms of their pairwise comparisons provided by the interview panel, who put more emphasis on Skills and Abilities than Research Experience. In this sense, the DEAHP overestimates the relative importance of $\mathsf { C } _ { 3 } ,$ on which Candidate C has the best performance relative to the other two candidates.

• With respect to $\mathsf { C } _ { 4 }$ (Skills and Abilities), the DEAHP evaluates Candidate C to be as good as Candidate B, but in fact the former performs worse than the latter. This can be veri<sup>fi</sup>ed by the pairwise comparisons between the two candidates. Therefore, the Skills and Abilities of Candidate C is obviously overestimated by the DEAHP.

• With respect to ${ \mathsf { C } } _ { 5 }$ (Capacity for Career Development), the DEAHP evaluates Candidates A and C to be as good as each other, but in fact Candidate A performs better than Candidate C. This can be veri<sup>fi</sup>ed by the pairwise comparisons between Candidates A and B. In this sense, the Capacity for Career Development of Candidate C is also overestimated.

Based upon the above analyses, we have suf<sup>fi</sup>cient reasons to believe that the relative importance of Candidate C is overestimated by the DEAHP. So, the selection of Candidate B as the best candidate is appropriate and also more reliable. This shows the fact that the DEA/AR method can provide better decision conclusions than the DEAHP.

## 5. Conclusions

In this paper we have analyzed main drawbacks of the DEAHP and proposed an assurance region DEA model for weight generation in the AHP, which is referred to as DEA/AR model, to overcome the drawbacks of the DEAHP such as counterintuitive local weights for inconsistent pairwise

![](/api/attachments/EVAKAK92/fulltext/images/941f0dfc5c6e8cfe4c77f7d70fefa3ac263d97cc99dd416337c431a7a71f13ba.jpg)  
Fig. 1. Hierarchical structure for recruitment of a research fellow.

Table 7  
Table 5 Description of selection criteria

<table><tr><td>Criteria</td><td>Description</td></tr><tr><td>Qualifications</td><td>A postgraduate degree in a relevant subject, ideally a doctorate level degree in a relevant subject.</td></tr><tr><td>Personal Qualities</td><td>A willingness to undertake further training as appropriate, and to adopt new procedures as and when required.A willingness to work collaboratively in a multi-disciplinary research team.</td></tr><tr><td>Research Experience</td><td>Experience and track record of undertaking research and securing external research funding.A track record of publication in academic peer reviewed journals.Experience of giving oral presentations at academic/non academic conferences and meetings.</td></tr><tr><td>Skills and Abilities</td><td>Excellent written and oral communications and interpersonal skills.Ability to work largely on own initiative with minimum supervisions.Ability to develop a research programme and to write for publication in good research journals.Ability to secure research funding from external sources.Ability to provide tutorial and counselling advice to undergraduate and postgraduate students.</td></tr><tr><td>Capacity for Career Development</td><td>An interest in developing an academic career as a management scholar and teacher.</td></tr></table>

comparison matrices, over insensitivity to some comparisons, information loss in a pairwise comparison matrix, and overestimation of some local weights. We have shown through numerical examples that the proposed DEA/AR model is able to overcome all these drawbacks. For example, the DEA/AR model produces true weights for perfectly consistent pairwise comparison matrices and rational, logical and intuitive weights for inconsistent pairwise comparison matrices. It also takes the best advantage of all the pairwise comparison information in a pairwise comparison matrix to avoid any information loss due to the role of assurance region.

Pairwise comparison matrix for <sup>fi</sup>ve selection criteria and its local weights

<table><tr><td>Criteria</td><td> $C_1$ </td><td> $C_2$ </td><td> $C_3$ </td><td> $C_4$ </td><td> $C_5$ </td><td>EM weights</td><td>EM weights (rescaled)</td><td>DEAHP weights</td><td>DEA/AR weights</td></tr><tr><td> $C_1$ </td><td>1</td><td>1/2</td><td>1/3</td><td>1/4</td><td>1/2</td><td>0.081</td><td>0.226</td><td>0.25</td><td>0.227</td></tr><tr><td> $C_2$ </td><td>2</td><td>1</td><td>1/2</td><td>1/2</td><td>1</td><td>0.153</td><td>0.429</td><td>0.5</td><td>0.432</td></tr><tr><td> $C_3$ </td><td>3</td><td>2</td><td>1</td><td>1/2</td><td>2</td><td>0.255</td><td>0.715</td><td>1</td><td>0.718</td></tr><tr><td> $C_4$ </td><td>4</td><td>2</td><td>2</td><td>1</td><td>2</td><td>0.357</td><td>1</td><td>1</td><td>1</td></tr><tr><td> $C_5$ </td><td>2</td><td>1</td><td>1/2</td><td>1/2</td><td>1</td><td>0.153</td><td>0.429</td><td>0.5</td><td>0.432</td></tr></table>

Consistency ratio (CR)=0.012b0.1

Through the application to the recruitment of a research fellow for a research project, we have further shown that the DEA/AR model provides better decisions than the DEAHP, which may sometimes overestimate the relative importance of some criteria and/or decision alternatives, leading to the conclusions not very reliable.

The DEA/AR model is also easy to use and implement without the need of specifying the assurance region in advance or subjectively, which is determined by the DEA/AR model and pairwise comparison matrices automatically.

Pairwise comparison matrices for three candidates with respect to different criteria and their local weights

<table><tr><td></td><td>Candidate A</td><td>Candidate B</td><td>Candidate C</td><td>EM weights</td><td>EM weights (rescaled)</td><td>DEAHP weights</td><td>DEA/AR weights</td></tr><tr><td colspan="8">A: Comparisons of three candidates with respect to Qualifications ( $C_1$ )</td></tr><tr><td>Candidate A</td><td>1</td><td>2</td><td>1</td><td>0.4</td><td>1</td><td>1</td><td>1</td></tr><tr><td>Candidate B</td><td>1/2</td><td>1</td><td>1/2</td><td>0.2</td><td>0.5</td><td>0.5</td><td>0.5</td></tr><tr><td>Candidate C</td><td>1</td><td>2</td><td>1</td><td>0.4</td><td>1</td><td>1</td><td>1</td></tr><tr><td colspan="8">Consistency Ratio (CR)=0</td></tr><tr><td colspan="8">B: Comparisons of three candidates with respect to Personal Qualities ( $C_2$ )</td></tr><tr><td>Candidate A</td><td>1</td><td>1/2</td><td>3</td><td>0.320</td><td>0.572</td><td>0.75</td><td>0.573</td></tr><tr><td>Candidate B</td><td>2</td><td>1</td><td>4</td><td>0.558</td><td>1</td><td>1</td><td>1</td></tr><tr><td>Candidate C</td><td>1/3</td><td>1/4</td><td>1</td><td>0.122</td><td>0.218</td><td>0.25</td><td>0.219</td></tr><tr><td colspan="8">Consistency Ratio (CR)=0.016&lt;0.1</td></tr><tr><td colspan="8">C: Comparisons of three candidates with respect to Research Experience ( $C_3$ )</td></tr><tr><td>Candidate A</td><td>1</td><td>1/3</td><td>1/5</td><td>0.109</td><td>0.188</td><td>0.2</td><td>0.188</td></tr><tr><td>Candidate B</td><td>3</td><td>1</td><td>1/2</td><td>0.309</td><td>0.531</td><td>0.6</td><td>0.531</td></tr><tr><td>Candidate C</td><td>5</td><td>2</td><td>1</td><td>0.582</td><td>1</td><td>1</td><td>1</td></tr><tr><td colspan="8">Consistency Ratio (CR)=0.003&lt;0.1</td></tr><tr><td colspan="8">D: Comparisons of three candidates with respect to Skills and Abilities ( $C_4$ )</td></tr><tr><td>Candidate A</td><td>1</td><td>1/2</td><td>1/2</td><td>0.196</td><td>0.397</td><td>0.5</td><td>0.4</td></tr><tr><td>Candidate B</td><td>2</td><td>1</td><td>2</td><td>0.493</td><td>1</td><td>1</td><td>1</td></tr><tr><td>Candidate C</td><td>2</td><td>1/2</td><td>1</td><td>0.311</td><td>0.630</td><td>1</td><td>0.633</td></tr><tr><td colspan="8">Consistency Ratio (CR)=0.046&lt;0.1</td></tr><tr><td colspan="8">E: Comparisons of three candidates with respect to Capacity for Career Development ( $C_5$ )</td></tr><tr><td>Candidate A</td><td>1</td><td>5</td><td>1</td><td>0.498</td><td>1</td><td>1</td><td>1</td></tr><tr><td>Candidate B</td><td>1/5</td><td>1</td><td>1/2</td><td>0.135</td><td>0.271</td><td>0.5</td><td>0.275</td></tr><tr><td>Candidate C</td><td>1</td><td>2</td><td>1</td><td>0.367</td><td>0.737</td><td>1</td><td>0.750</td></tr><tr><td colspan="8">Consistency Ratio (CR)=0.081&lt;0.1</td></tr></table>

Table 8  
Global weights of three candidates with respect to the total goal

<table><tr><td></td><td>C1</td><td>C2</td><td>C3</td><td>C4</td><td>C5</td><td>Global weights</td><td></td></tr><tr><td colspan="8">A: Global weights of three candidates by the eigenvector method (EM)</td></tr><tr><td>Local weights of criteria</td><td>0.081</td><td>0.153</td><td>0.255</td><td>0.357</td><td>0.153</td><td></td><td></td></tr><tr><td>Candidate A</td><td>0.400</td><td>0.320</td><td>0.109</td><td>0.196</td><td>0.498</td><td>0.256</td><td></td></tr><tr><td>Candidate B</td><td>0.200</td><td>0.558</td><td>0.309</td><td>0.493</td><td>0.135</td><td>0.378</td><td></td></tr><tr><td>Candidate C</td><td>0.400</td><td>0.122</td><td>0.582</td><td>0.311</td><td>0.367</td><td>0.367</td><td></td></tr><tr><td colspan="8">B: Global weights of three candidates by the EM method (Rescaled)</td></tr><tr><td>Local weights of criteria</td><td>0.226</td><td>0.429</td><td>0.715</td><td>1.000</td><td>0.429</td><td>Non-normalized</td><td>Normalized</td></tr><tr><td>Candidate A</td><td>1.000</td><td>0.572</td><td>0.188</td><td>0.397</td><td>1.000</td><td>1.433</td><td>0.703</td></tr><tr><td>Candidate B</td><td>0.500</td><td>1.000</td><td>0.531</td><td>1.000</td><td>0.271</td><td>2.039</td><td>1.000</td></tr><tr><td>Candidate C</td><td>1.000</td><td>0.218</td><td>1.000</td><td>0.630</td><td>0.737</td><td>1.981</td><td>0.972</td></tr><tr><td colspan="8">C: Global weights of three candidates by the DEAHP</td></tr><tr><td>Local weights of criteria</td><td>0.25</td><td>0.5</td><td>1</td><td>1</td><td>0.5</td><td>Non-normalized</td><td>Normalized</td></tr><tr><td>Candidate A</td><td>1</td><td>0.75</td><td>0.2</td><td>0.5</td><td>1</td><td>1.825</td><td>0.635</td></tr><tr><td>Candidate B</td><td>0.5</td><td>1</td><td>0.6</td><td>1</td><td>0.5</td><td>2.475</td><td>0.861</td></tr><tr><td>Candidate C</td><td>1</td><td>0.25</td><td>1</td><td>1</td><td>1</td><td>2.875</td><td>1.000</td></tr><tr><td colspan="8">D: Global weights of three candidates by the DEA/AR method</td></tr><tr><td>Local weights of criteria</td><td>0.227</td><td>0.432</td><td>0.718</td><td>1</td><td>0.432</td><td>Non-normalized</td><td>Normalized</td></tr><tr><td>Candidate A</td><td>1</td><td>0.573</td><td>0.188</td><td>0.4</td><td>1</td><td>1.442</td><td>0.705</td></tr><tr><td>Candidate B</td><td>0.5</td><td>1</td><td>0.531</td><td>1</td><td>0.275</td><td>2.046</td><td>1.000</td></tr><tr><td>Candidate C</td><td>1</td><td>0.219</td><td>1</td><td>0.633</td><td>0.75</td><td>1.997</td><td>0.976</td></tr></table>

Compared with the well-known EM, the DEA/AR model is linear rather than nonlinear and is therefore easier to solve. These good features make the DEA/AR model very practical and attractive. It is expected that the DEA/AR model can <sup>fi</sup>nd more potential applications in the near future.

## Acknowledgements

The authors would like to thank the Editor-in-Chief and three anonymous reviewers for their constructive comments and suggestions which are very helpful in improving the paper.

## References

[1] C.B. Alphonce, Application of the analytic hierarchy process in agriculture in developing countries, Agricultural Systems 53 (1997) 97–112.

[2] M.C. Carnero, Selection of diagnostic techniques and instrumentation in a predictive maintenance program. A case study, Decision Support Systems 38 (2005) 539–555.

[3] A. Charnes, W.W. Cooper, E. Rhodes, Measuring the ef<sup>fi</sup>ciency of decision making units, European Journal of Operational Research 2 (1978) 429–444.

[4] W. Ho, Integrated analytic hierarchy process and its applications — a literature review, European Journal of Operational Research 186 (2008) 211–228.

[5] C.L. Hwang, K. Yoon, Multiple Attribute Decision Making: Methods and Applications, Springer-Verlag, Berlin, 1981.

[6] Y. Lee, K.A. Kozar, Investigating the effect of website quality on e-business success: an analytic hierarchy process (AHP) approach, Decision Support Systems 42 (2006) 1383–1401.

[7] M.J. Liberatore, R.L. Nydick, The analytic hierarchy process in medical and health care decision making: a literature review, European Journal of Operational Research 189 (2008) 194–207.

[8] L. Mikhailov, A fuzzy programming method for deriving priorities in the analytic hierarchy process, Journal of the Operational Research Society 51 (3) (2000) 341-349.

[9] H. Minc, Nonnegative Matrices, Wiley, New York, 1988.

[10] R. Ramanathan, Data envelopment analysis for weight derivation and aggregation in the analytic hierarchy process, Computers & Operations Research 33 (2006) 1289–1307.

[11] T.L. Saaty, The Analytic Hierarchy Process, McGraw-Hill Company, New York, 1980.

[12] M. Sevkli, S.C.L. Koh, S. Zaim, M. Demirbag, E. Tatoglu, An application of data envelopment analytic hierarchy process for supplier selection: a case study of BEKO in Turkey, International Journal of Production Research 45 (9) (2007) 1973–2003.

[13] B. Srdjevic, Combining different prioritization methods in analytic hierarchy process synthesis, Computers & Operations Research 32 (7) (2005) 1897-1919.

[14] B. Srdjevic, Linking analytic hierarchy process and social choice methods to support group decision-making in water management, Decision Support Systems 42 (2007) 2261–2273.

[15] Y. Sun, S. He, J.Y. Leu, Syndicating web services: a QoS and user-driven approach, Decision Support Systems 43 (2007) 243–255.

[16] R.G. Thompson, L.N. Langemeier, C.T. Lee, E. Lee, R.M. Thrall, The role of multiplier bounds in ef<sup>fi</sup>ciency analysis with application to Kansas farming, Journal of Econometrics 46 (1–2) (1990) 93–108.

[17] R.G. Thompson, F.D. Sigleton Jr., R.M. Throll, B.A. Smith, Comparative site evaluations for locating a high-energy physics laboratory in Texas, Interfaces 16 (6) (1986) 35–49.

[18] O.S. Vaidya, S. Kumar, Analytic hierarchy process: an overview of applications, European Journal of Operational Research 169 (2006) 1–29.

![](/api/attachments/EVAKAK92/fulltext/images/a8cc7256d45bfabfdd401372c292839bd44a59c4b110a64949de8b777e44ae76.jpg)

Dr. Ying-Ming Wang is a Professor of Management Science in the School of Public Administration, Fuzhou University, PR China. He received his BEng degree in Industrial Electric Automation from Jiangsu University of Science and Technology in 1984, MEng and PhD degrees both in Systems Engineering, respectively, from Huazhong University of Science and Technology in 1987 and Southeast University in 1991. His research interests include multiple attribute decision analysis (MADA), data envelopment analysis (DEA), analytic hierarchy process (AHP), evidential reasoning (ER)

approach, quality function deployment (QFD), and failure mode and effects analysis (FMEA). He has published nearly 150 academic papers in a wide variety of peer reviewed journals such as European Journal of Operational Research. Fuzzy Sets and Systems, Computers and Operations Research, Information Sciences, Expert Systems with Applications, Decision Support Systems, Journal of the Operational Research Society, Computers & Industrial Engineering, Journal of Computational and Applied Mathematics, Applied Mathematics and Computation, Applied Mathematical Modelling and so on.

![](/api/attachments/EVAKAK92/fulltext/images/91b457aa6c35ce687ad0bea2896c8dfebf8269a4c6f6574fcc1d1fb5a5895ea9.jpg)

Dr. Kwai-Sang Chin is an associate professor at the Department of Manufacturing Engineering & Engineering Management, City University of Hong Kong. He is a Charter Engineer in UK, a Registered Professional Engineer in Hong Kong, a Fellow Member of the Hong Kong Society for Quality and Hong Kong Quality Management Association, the Programme Leader of the MSc Engineering Management programme in the Department. He maintains intensive collaboration with industries through various consultancy work, training courses and industrial projects. His current re-

search interests are ‘Quality Management Strategies Beyond ISO9000 for Hong Kong and China’ and ‘Decision Support Methodologies/Systems for New Product Innovations and Development’. He has published a signi<sup>fi</sup>cant number of papers in peer reviewed journals such as IEEE Transactions on Engineering Management, European Journal of Operational Research, Information Sciences, Expert Systems with Applications, International Journal of Production Research, International Journal of Quality and Reliability Management, Industrial Management and Data Systems, International Journal of Advanced Manufacturing Technology, Total Quality Management. Industrial Marketing Management, and the like

![](/api/attachments/EVAKAK92/fulltext/images/cce39c868fb3bd944a6988131807ef9288022c31ce44686371674afb16c04eb8.jpg)

Dr. Gary POON Ka Kwai is currently a lecturer at the Department of Manufacturing Engineering & Engineering Management, City University of Hong Kong, teaching Quality and Reliability Engineering, and Environmental Management. His research interests include the characterization of electronics manufacturing processes, quality and environmental management. He is a Senior Member of the Institute of Industrial Engineers (IIE), Member of the Institute of Engineering and Technology (IET) and the American Society of Quality (ASQ), and a Chartered Engineer.
