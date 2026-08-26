---
otero_id: 4824
otero_key: "GBQCT8N9"
title: "Some extensions of the precise consistency consensus matrix"
authors: "María Teresa Escobar; Juan Aguarón; José María Moreno-Jiménez"
year: "2015"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2015.04.005"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
María Teresa Escobar, Juan Aguarón, José María Moreno-Jiménez ⁎

Grupo Decisión Multicriterio Zaragoza, Facultad de Economía y Empresa, Universidad de Zaragoza, Gran Vía 2, 50005 Zaragoza, Spain <sup>1</sup>

## a r t i c l e i n f o

Article history: Received 10 September 2014 Received in revised form 25 February 2015 Accepted 6 April 2015 Available online 14 April 2015

Keywords: Group Decision Making (GDM) Consensus Analytic Hierarchy Process (AHP) Consistency Compatibility

## a b s t r a c t

The Precise Consensus Consistency Matrix (PCCM) is an AHP-Group Decision Making (AHP-GDM) tool, de<sup>fi</sup>ned by Aguarón et al. [2] and developed in a local context (a single criterion) in which the decision makers are assigned the same weights. Using the Row Geometric Mean as the prioritisation procedure, consensus is sought between the different decision makers when the modi<sup>fi</sup>cations of their initial positions or judgements are guaranteed to be within the range of values accepted for a given inconsistency level. This paper upgrades the algorithm initially proposed for obtaining the PCCM in two ways: (i) it considers the case of different weights for the decision makers; and (ii) it strengthens the idea of consistency in the design of the algorithm. One of the drawbacks of this decisional tool is that it is sometimes impossible to achieve a complete matrix. To address this, we propose a procedure for attaining a complete common consensus judgement matrix or, at least, a matrix with the minimum number of entries that are required to derive the priorities. Finally, we compare the results obtained when applying the extensions of the PCCM with those obtained using the two traditional procedures (AIJ and AIP) usually employed in AHP-GDM. In order to do this, we use a set of indicators that measure the violations in consistency of the group pairwise matrices and the compatibility between the individuals and group positions in four cases associated with two scenarios (weighted and non-weighted decision makers) and two situations (complete and incomplete PCCMs).

© 2015 Elsevier B.V. All rights reserved.

## 1. Introduction

The collaborative resolution of decisional problems (decision making involving multiple actors) and the evaluation of the associated intangible aspects (or the integration of tangible and intangible aspects in the formal models) are two of the most signi<sup>fi</sup>cant issues of the Knowledge Society [19].

A fundamental concept in decision making with multiple actors [2, 10,17,21,32], particularly with regard to Group Decision Making (GDM), is consensus. Consensus refers to the approach, model, tools, and procedures for deriving the <sup>fi</sup>nal group priority vector [21]. If we understand consensus as agreement between the actors implicated in the resolution of the problem, agreement usually refers to collective preferences, although, on occasions, it can refer to the procedures followed for obtaining them, which are themselves based on individual preferences. If it is not possible to act as a homogenous group under the principle of consensus (a characteristic of group decision making), it is usual to seek collective preferences, so that the compatibility of individual preferences is as high as possible [25,33,34] and the modi<sup>fi</sup>cations of the individual preferences that are required to fall in line with the group are minimised. This favours the overall acceptability of the collective result for the individuals implicated in the resolution of the problem.

These two criteria are normally followed in Negotiated Decision Making (NDM), under the principle of agreement [6,17]. Nevertheless, whilst it would be useful to resolve this semantic question as soon as possible, in the scienti<sup>fi</sup>c literature on group decision making, the term consensus is commonly employed to re<sup>fl</sup>ect the idea of agreement or compatibility between individual and collective preferences [4,9,12,34].

Of the different multicriteria approaches followed for decision making, one that best captures [6] the two basic issues inherent in the Knowledge Society (multiple actors and the integration of intangible aspects) is the Analytic Hierarchy Process (AHP). The process allows the application of most of the different perspectives (determinist, stochastic, fuzzy etc.) used in the scienti<sup>fi</sup>c literature with regard to the search for consensus [5–7,12,13,15–17,22,23,26,27,30,34,35].

AHP [23,24] is one of the most frequently employed approaches, both from theoretical and practical point of view. Two of its most important characteristics are: (i) it offers the possibility to evaluate the consistency of the judgements emitted in order to capture the preferences of the decision makers; and (ii) its correct behaviour in multiple actor decision making contexts. De<sup>fi</sup>ned as the cardinal transitivity of judgements [23], the concept of consistency differentiates AHP from other multicriteria techniques and it has been widely examined in the literature on AHP [8,17]. In multiactor decision making, AHP perfectly adapts to the three contexts that are contemplated [2,17,21]: Group Decision

Making (GDM), Negotiated Decision Making (NDM), and Systematic Decision Making (SDM). For all three, a variety of procedures have been developed for evaluating compatibility between individual and collective positions.

A number of attempts have been made to integrate consistency and consensus (or compatibility) in multiple actor decision making using AHP [12,17,18,34]. With the aim of reaching collective positions close to the individuals' initial positions, that is to say, to preserve the initial positions as much as possible, Moreno-Jiménez et al. [17,18] proposed a new decisional tool for collective decision making – the Consistency Consensus Matrix (CCM) – that identi<sup>fi</sup>es the core consistency of the group decision. This interval judgement matrix does not have to be complete and it does not even have to connect the nodes. Aguarón et al. [2] further re<sup>fi</sup>ned the tool, de<sup>fi</sup>ning the Precise Consistency Consensus Matrix (PCCM) which is able to select a precise value for each judgement interval in such a way that the quantity of slack that remains free for successive algorithm iterations is the maximum possible. The PCCM was designed for a local context (a single criterion) and, due to its mathematical properties,<sup>2</sup> under the Row Geometric Mean (RGM) prioritisation procedure. As with the CCM, the PCCM is not guaranteed to be complete or connected, although it is more democratic than the CCM as it includes more entries or cells in which there is consensus in consistency (non-null cells).

The original PCCM proposal [2] allowed for multiactor decision making in which all the actors were given equal weighting. In this paper, we present a series of PCCM extensions that complement the original de<sup>fi</sup>- nition and permit the assignation of different weights to the decision makers in addition to strengthening the concept of consistency in the design of the algorithm. At the same time, we suggest a number of methods for connecting an unconnected matrix and to complete the PCCMs that have empty cells.

There are other models that use varying perspectives of consistency which allow the construction of a consensus matrix in AHP-GDM with multiplicative preference relations [12,34]. The main differences between these models and the new tool (PCCM) advanced for the AHP-GDM are that: (i) the PCCM seeks to maximise the number of entries of the consensus matrix that belongs to the consistency stability intervals of all the decision makers; and (ii) it guarantees that the consensus matrix entries are found within the levels permitted for <sup>fi</sup>xed inconsistency in the process. This avoids the rejection (veto) inherent in moving away from the initial positions to a degree that is superior to that which is assumed by the accepted inconsistency level.

The remainder of this paper is structured as follows: Section 2 outlines the initial PCCM proposal [2]; Section 3 presents the extensions; Section 4 offers a series of numerical examples to illustrate the application of the extensions; and Section 5 details the most signi<sup>fi</sup>cant results and conclusions of the work.

## 2. The Precise Consensus Consistency Matrix (PCCM)

The two classic approaches followed in AHP-group decision making [13,17,22,23] are: (i) the Aggregation of Individual Judgements (AIJ) which constructs a pairwise comparison matrix for the group from which the priority vector is calculated by following any of the existing prioritisation procedures; and (ii) the Aggregation of Individual Priorities (AIP), in which the group priorities are obtained by aggregating the individual priorities (the Weighted Geometric Mean is most commonly used as the aggregation procedure).

A number of different measures have been put forward for evaluating the inconsistency of the decision makers when eliciting their judgements with AHP (it is not necessary for them to be perfectly consistent or transitive). Given a pairwise comparison matrix $A = \left( a _ { i j } \right)$ $i , j = 1 , . . . , n ,$ A is said to be consistent if there is cardinal transitivity between the judgements, that is to say, $\mathrm { i f } a _ { i j } \cdot a _ { j k } = a _ { i k } \forall i , j , k [ 2 3 ]$ ]. Saaty suggests the Consistency Ratio for measuring the inconsistency if the Eigenvector method has been used to obtain the local priorities. When the local priorities have been derived by using the Row Geometric Mean (RGM), Aguarón and Moreno-Jiménez [3], basing themselves on Crawford and Williams [11], advocate the Geometric Consistency Index (GCI).

Given a pairwise comparison matrix $A = ( a _ { i j } ) , i , j = 1 , . . . , n ,$ , and let $w = ( w _ { j } ) , j = 1 , \ldots , n ,$ be the corresponding priority vector obtained

![](/api/attachments/GBQCT8N9/fulltext/images/9d9c69f9890c6792fe23cab1e8c88e62421fd99c606231bb8ea75cd8efd5a75b.jpg)  
Fig. 1. The PCCM algorithm.

![](/api/attachments/GBQCT8N9/fulltext/images/98e14ae723e59b9d274fe3cdda67c07cb90576659bcfd28cbc34d6fc2d5f1386.jpg)  
Fig. 2. The augmented PCCM process.

using the Row Geometric Mean Method. The Geometric Consistency Index (GCI) is then de<sup>fi</sup>ned as:

$$
G C I = \frac {2}{(n - 1) (n - 2)} \sum_ {1 \leq i <   j \leq n} \log^ {2} e _ {i j} \text {   with   } e _ {i j} = a _ {i j} \cdot \frac {w _ {j}}{w _ {i}}.\tag{1}
$$

The aforementioned authors also established the thresholds which, depending on the order of the matrix, allow an analogous interpretation of up to 10% for the Consistency Ratio [23]. These values for the GCI are: 0.31 for $n = 3 ; 0 . 3 5$ for n = 4 and 0.37 for $n > 4 .$

Consistency has already been used in AHP-GDM in order to obtain a common judgement matrix, for all the members of the group, which does not deviate too much from the individual positions. Initially, for the RGM prioritisation procedure, Moreno-Jiménez et al. [17,18] proposed the construction of a matrix named the Consistency Consensus Matrix (CCM). This was an interval judgement matrix in which the entries correspond to those intervals in which the decision makers are simultaneously consistent in their initial matrices. The main drawback of the CCM is that on consideration of consistent interval judgements for the entries, the available consistency slack for the following judgements is quickly consumed.

Using a local context and the RGM prioritisation method, Aguarón et al. [2] presented a similar procedure but with the selection of a precise value in the intervals, thereby obtaining a precise matrix — the Precise Consensus Consistency Matrix (PCCM). The precise value is selected by allotting the greatest slack to the most inconsistent decision maker, or, in other words, the selected value minimises the GCI of the most inconsistent decision maker. This means that the most slack is available for the following iterations. In this way, the PCCM provides more informed and participative group decision making than the CCM and offers more accurate estimations for the group's priorities. It can also be used as a starting point for posterior negotiation processes between the actors.

One of the limitations of the methodology proposed by Aguarón et al. [2] is that it does not consider the possibility that the decision makers may have different importance or weights. Another drawback is that the procedure does not guarantee that the <sup>fi</sup>nal values of the PCCM belong to the initial consistency stability intervals (CSI). This paper reformulates the algorithm (Section 3) to allow for the possibility of having different weights and to guarantee that the condition of belonging to the initial CSI is ful<sup>fi</sup>lled. Finally, given that it is not always possible to achieve a complete consensus matrix, or at least one with the minimum number of connected entries necessary for deriving the priorities, we advance a set of proposals for dealing with these situations (incomplete PCCMs).

Before the presentation of the extensions (Section 3), it is worth looking at a series of theoretical results which refer to the de<sup>fi</sup>nitions of the relative consistency stability interval and the consistency stability interval for a judgement [1].

De<sup>fi</sup>nition 1. Given a pairwise comparison matrix, $A = ( a _ { i j } ) , i , j = 1 , . . . , n ,$ and a variation Δ $( \Delta > 0 )$ for the GCI, we de<sup>fi</sup>ne:

i) The Consistency Relative Stability Interval (CRSI) for the judgement $a _ { r s }$ as the interval $\left[ \underline { { \delta } } _ { r s } ( \Delta ) , \overline { { \delta } } _ { r s } ( \Delta ) \right]$ in which its relative variations can oscillate without the increment of GCI exceeding Δ.

ii) The Consistency Stability Interval (CSI) for the judgement $a _ { r s }$ given is the interval $[ \underline { { a } } _ { r s } ( \Delta ) , \overline { { a } } _ { r s } ( \Delta ) ] ^ { 3 }$ in which the judgement can oscillate without the increment of GCI exceeding Δ. Its value is given by: $\underline { { a } } _ { r s } ( \Delta ) = a _ { r s } \underline { { \delta } } _ { r s } ( \Delta )$ and $\overline { { a } } _ { r s } ( \Delta ) = a _ { r s } \overline { { \delta } } _ { r s } ( \Delta )$ .

Notation. Let $A = ( a _ { i j } )$ be a pairwise comparison matrix, GCI(A) denotes the Geometric Consistency Index of matrix A [3] and $A ^ { \prime } = ( a ^ { \prime } { } _ { i j } )$ is the matrix obtained by modifying one or more judgements of matrix A. Let $t _ { i j } = a _ { i j } ^ { \prime } / a _ { i j }$ be the relative variation of judgement $a _ { i j } , \tau _ { i j } ( \tau _ { i j } =$ log $t _ { i j } )$ its logarithm, $e _ { i j } ( e _ { i j } = a _ { i j } \omega _ { j } / \omega _ { i } )$ the error, and $\varepsilon _ { i j }$ its logarithm $( \varepsilon _ { i j } = \log e _ { i j } )$

Table 1  
Pairwise comparison matrices for the three political parties.

<table><tr><td>PSOE</td><td>DUV</td><td>IUV</td><td>PUV</td><td>EV</td><td>BV</td><td>PP</td><td>DUV</td><td>IUV</td><td>PUV</td><td>EV</td><td>BV</td><td>PAR</td><td>DUV</td><td>IUV</td><td>PUV</td><td>EV</td><td>BV</td></tr><tr><td>DUV</td><td>1</td><td>3</td><td>5</td><td>8</td><td>6</td><td>DUV</td><td>1</td><td>3</td><td>7</td><td>9</td><td>5</td><td>DUV</td><td>1</td><td>5</td><td>7</td><td>7</td><td>5</td></tr><tr><td>IUV</td><td></td><td>1</td><td>3</td><td>5</td><td>4</td><td>IUV</td><td></td><td>1</td><td>3</td><td>7</td><td>1</td><td>IUV</td><td></td><td>1</td><td>1</td><td>5</td><td>1</td></tr><tr><td>PUV</td><td></td><td></td><td>1</td><td>3</td><td>2</td><td>PUV</td><td></td><td></td><td>1</td><td>5</td><td>1/5</td><td>PUV</td><td></td><td></td><td>1</td><td>5</td><td>1/3</td></tr><tr><td>EV</td><td></td><td></td><td></td><td>1</td><td>1/3</td><td>EV</td><td></td><td></td><td></td><td>1</td><td>1/5</td><td>EV</td><td></td><td></td><td></td><td>1</td><td>1/5</td></tr><tr><td>BV</td><td></td><td></td><td></td><td></td><td>1</td><td>BV</td><td></td><td></td><td></td><td></td><td>1</td><td>BV</td><td></td><td></td><td></td><td></td><td>1</td></tr></table>

## 3. Some extensions of the PCCM

## 3.1. Different weights and strengthening consistency

The <sup>fi</sup>rst extension involves a twofold upgrading of the algorithm de-<sup>fi</sup>ned by Aguarón et al. [2] for obtaining the PCCM: (i) to allow for different weights for the decision makers; and (ii) to strengthen the idea of consistency, guaranteeing that the values of the PCCM belong to the initial consistency stability intervals. This paper does not contemplate the assignation of weights to the decision-makers. For more information on the question see Xu and Cai [29] and Yue [31].

The algorithm for constructing the PCCM starts by calculating the variance of the logarithms of the corresponding judgements (Step 1) and selecting the judgement with least variance (Step 2) that has a non-null intersection for the initial individual consistency stability intervals. For this judgement, the consistency stability intervals for each decision maker are calculated (Step 3) and the intersection of all these intervals is obtained (Step 4). In this common interval, it is guaranteed that the individual judgements can oscillate without the GCI exceeding a previously <sup>fi</sup>xed level of inconsistency. The intersection of the previous interval with the initial consistency stability intervals is then calculated (Step 5). This avoids taking a value that is further from the initial judgements of all the decision makers than the amount allowed for the previously <sup>fi</sup>xed inconsistency level (for Saaty's Consistency Ratio it is usually 10%). The procedure then selects a precise judgement that belongs to the common interval (Step 6). Any value within this interval will have acceptable inconsistency. Nevertheless, some of the matrices will be more inconsistent than others and they will therefore allow less slack for the following iterations. It would seem logical to select the value that provides the greatest slack for the most inconsistent matrix or, in other words, the value that minimises the GCI of the most inconsistent matrix.

To obtain this value, the following problem must be solved:

$$
\underset { \begin{array}{c} a _ {r s} \in [ \underline {{a}} _ {r s}, \overline {{a}} _ {r s} ] \end{array} } {\text {Min}} \underset {k} {\text {Max}} G C I \Big (A ^ {(k)} \Big)\tag{2}
$$

or the equivalent (see [1,2]):

$$
\underset { \begin{array}{c} a _ {r s} \\ a _ {r s} \in [ \underline {{a}} _ {r s}, \overline {{a}} _ {r s} ] \end{array} } {\text {Min}} \underset {k} {\text {Max}} G C I \Big (A ^ {(k)} \Big) + \frac {2}{n (n - 1)} \left(\tau_ {r s} ^ {(k) 2} + \frac {2 n}{n - 2} \tau_ {r s} ^ {(k)} \varepsilon_ {r s} ^ {(k)}\right)\tag{3}
$$

Pairwise comparison matrix for the new party (NP).

<table><tr><td>NP</td><td>DUV</td><td>IUV</td><td>PUV</td><td>EV</td><td>BV</td></tr><tr><td>DUV</td><td>1</td><td>1/2</td><td>1/5</td><td>1/8</td><td>1/7</td></tr><tr><td>IUV</td><td></td><td>1</td><td>1/4</td><td>1/6</td><td>1/5</td></tr><tr><td>PUV</td><td></td><td></td><td>1</td><td>1/4</td><td>1/3</td></tr><tr><td>EV</td><td></td><td></td><td></td><td>1</td><td>3</td></tr><tr><td>BV</td><td></td><td></td><td></td><td></td><td>1</td></tr></table>

Finally, the value obtained is included as an entry of the PCCM and serves to update the initial individual judgement matrices (Step 7).

With regard to the algorithm proposed by Aguarón et al. [2], changes have been made to Steps 1, 2, 5, and 6. In Step 1, the calculation of the variance has been reformulated in order to allow for the possibility that the decision makers have different weights. This step also provides the initial Consistency Stability Intervals for the individuals and the group. Step 2 includes a new constraint when selecting the order of the entries that are candidates to be incorporated in the PCCM. Step 5 has also been reformulated and now guarantees that the judgements belong to Saaty's fundamental scale range of values [1/9,9] and that the <sup>fi</sup>nal values of the PCCM belong to the initial consistency stability intervals of the different decision makers. In terms of permitted inconsistency, the changes in the judgements with respect to the initial positions will therefore be acceptable. This new condition strengthens the idea of consistency in the design of the algorithm. In Step 6, the optimisation problem has been modi<sup>fi</sup>ed to include different weights for the decision makers. This means that the algorithm designed to solve the optimisation problem is more dif<sup>fi</sup>cult as there are a greater number of possibilities that must be analysed.

Next, we present a new version of the PCCM that allows the consideration of several decision makers with different weights and the improvement of the algorithm's ef<sup>fi</sup>cacy from the point of view of consistency. A <sup>fl</sup>owchart of the algorithm used in constructing this version of the PCCM can be seen in Fig. 1.

Algorithm. Let $\mathsf { A } ^ { t , ( k ) } \left( k { = } 1 , . . . , r ; t { = } 0 , . . . , \mathrm { T } \right)$ be the individual judgement matrix for the decision maker k after the iteration t of the algorithm, where $t = 0$ corresponds to the initial individual judgement matrix $\mathsf { A } ^ { 0 , ( k ) } = ( a _ { i j } ^ { 0 , ( k ) } ) = ( \dot { a } _ { i j } ^ { ( k ) } ) = \mathsf { A } ^ { ( k ) }$ , and $t > 0 , \mathsf { A } ^ { t , ( k ) }$ is obtained by replacing the values of $\mathsf { \bar { A } } ^ { ( k ) }$ by the non-null entries of the PCCM after iteration t; let $G C \Gamma ^ { t , ( k ) }$ be the Geometric Consistency Index for the matrix $\mathsf { A } ^ { t , ( k ) }$

Step 1 Calculate

(i) The auxiliary matrix $\Sigma = ( \sigma _ { i j } ^ { 2 } )$ where $\sigma _ { i j } ^ { 2 } = V a r ( \log a _ { i j } ^ { ( k ) } )$

$$
\sigma_ {i j} = \sum_ {k = 1} ^ {r} \alpha^ {(k)} \log^ {2} a _ {i j} ^ {(k)} - \left(\sum_ {k = 1} ^ {r} \alpha^ {(k)} \log a _ {i j} ^ {(k)}\right) ^ {2}\tag{4}
$$

where $\mathbf { \boldsymbol { \alpha } } ^ { ( \mathrm { k } ) }$ is the weight of the decision maker k $( \alpha ^ { ( k ) } { \in } [ 0 , \mathrm { , } 1 ]$ ;

$$
\sum_ {k} \alpha^ {(k)} = 1).
$$

Individual priority vectors, consistencies, and rankings

<table><tr><td>Alt.\Priorities</td><td>PSOE</td><td>PP</td><td>PAR</td><td>NP</td></tr><tr><td>DUV (1)</td><td>0.513</td><td>0.520</td><td>0.560</td><td>0.038</td></tr><tr><td>IUV (2)</td><td>0.251</td><td>0.195</td><td>0.135</td><td>0.059</td></tr><tr><td>PUV (3)</td><td>0.115</td><td>0.072</td><td>0.101</td><td>0.149</td></tr><tr><td>EV (4)</td><td>0.042</td><td>0.030</td><td>0.035</td><td>0.480</td></tr><tr><td>BV (5)</td><td>0.079</td><td>0.182</td><td>0.168</td><td>0.274</td></tr><tr><td>GCIs</td><td>0.143</td><td>0.303</td><td>0.298</td><td>0.203</td></tr><tr><td>Rankings</td><td>1-2-3-5-4</td><td>1-2-5-3-4</td><td>1-5-2-3-4</td><td>4-5-3-2-1</td></tr></table>

Table 4  
Precise Consistency Consensus Matrix (PCCM) for r = 3 and no weights.

<table><tr><td>PCCM</td><td>DUV</td><td>IUV</td><td>PUV</td><td>EV</td><td>BV</td></tr><tr><td>DUV</td><td>1</td><td>2.17</td><td>4.93</td><td>9</td><td>2.54</td></tr><tr><td>IUV</td><td>0.46</td><td>1</td><td>2.93</td><td>6.36</td><td>1.44</td></tr><tr><td>PUV</td><td>0.20</td><td>0.34</td><td>1</td><td>2.85</td><td>0.63</td></tr><tr><td>EV</td><td>0.11</td><td>0.16</td><td>0.35</td><td>1</td><td>0.35</td></tr><tr><td>BV</td><td>0.39</td><td>0.70</td><td>1.58</td><td>2.84</td><td>1</td></tr></table>

(ii) The Consistency Interval Judgement matrix (CIJ) for each decision maker, $\mathrm { C I J } { \sf A } ^ { 0 , ( k ) } = \left( \left[ \underline { { a } } _ { i j } ^ { 0 , ( k ) } , \overline { { a } } _ { i j } ^ { 0 , ( k ) } \right] \right)$ <sup></sup>, where $\left\lceil a _ { i j } ^ { 0 , ( k ) } , \overline { { a } } _ { i j } ^ { 0 , ( k ) } \right\rceil$ are the consistency stability intervals for $a _ { i j } ^ { ( k ) } = \overset {  } { a _ { i j } ^ { t } } = 0 , \overset {  } { ( k ) }$ with $\Delta ^ { 0 , ( \mathrm { k } ) } = \mathrm { G C I ^ { * } } - \mathrm { G C I } ^ { 0 , ( k ) }$ <sup>)</sup>, GCI\* being the maximum inconsistency allowed for the problem and $\mathsf { G C I } ^ { 0 , ( k ) }$ the Geometric Consistency Index for the initial matrix $\mathsf { A } ^ { ( k ) }$

(iii) The Consistency Interval Judgement matrix for the group $\left( \mathrm { G C I J A } \right) , \mathrm { G C I J A } = \left( \left[ a _ { i j } ^ { 0 } , \overline { { a } } _ { i j } ^ { 0 } \right] \right)$ , where $\underline { { { a } } } _ { i j } ^ { 0 } = M \underline { { { a } } } x \Big \{ \underline { { { a } } } _ { r s } ^ { 0 , ( k ) } \Big \}$ and $\underline { { a } } _ { i j } ^ { 0 } =$ ${ M i n \left\{ \overline { { a } } _ { r s } ^ { 0 , ( k ) } \right\} }$ . Let $t = 0 ,$

Step 2 Select the entry (r,s) of Σ with the minimum value that has not been previously considered and with $\left[ { \underline { { a _ { i j } ^ { 0 } } } , \overline { { a _ { i j } ^ { 0 } } } } \right] \neq \emptyset$

Step 3 For each decision maker k calculate:

(i) The variation $\Delta ^ { t , ( k ) }$ for the $G { \bf C } \boldsymbol { \mathrm { I } } ^ { t , ( k ) }$ , which is given by $\Delta ^ { t , ( k ) } =$ $\mathrm { G C I ^ { * } } \mathrm { ~ - ~ } \mathrm { G C I } ^ { t , ( k ) }$ , where GCI\* is the maximum inconsistency allowed for the problem.

(ii) The Consistency Stability Interval for the judgement $a _ { r s } ^ { t , ( k ) }$ of the $\mathsf { A } ^ { t , ( k ) }$ matrix: $\left[ \underline { { a } } _ { r s } ^ { t , ( k ) } \left( \Delta ^ { t , ( k ) } \right) , \overline { { a } } _ { r s } ^ { t , ( k ) } \left( \Delta ^ { t , ( k ) } \right) \right]$

Step 4 Obtain the intersection of these intervals: $\begin{array} { r } { \Omega _ { k } [ \underline { { a } } _ { r s } ^ { t , ( k ) } , \overline { { a } } _ { r s } ^ { t , ( k ) } ] = } \end{array}$ $\left\lceil M a x \Bigl \{ \underline { { { a } } } _ { r s } ^ { t , ( k ) } \Bigr \} , \quad M i n \Bigl \{ \overline { { { a } } } _ { r s } ^ { t , ( k ) } \Bigr \} \right\rceil$ . If this is null, leave the entry (r,s) of the PCCM as blank and go to Step 8.

Step 5 Calculate the intersection of the previous interval with the intersection of the initial consistency stability intervals $\cap _ { k } [ \underline { { a } } _ { r s } ^ { 0 , ( k ) } , \overline { { a } } _ { r s } ^ { 0 , ( k ) } ] = \biggl [ M \underline { { a } } x \Bigl \{ \underline { { a } } _ { r s } ^ { 0 , ( k ) } \Bigr \} , \quad M \underline { { i } } n \Bigl \{ \overline { { a } } _ { r s } ^ { 0 , ( k ) } \Bigr \} \biggr ]$ and [1/9, 9]. The resulting interval is denoted as $\left[ \underline { { a _ { r s } ^ { t } } } , \overline { { a } } _ { r s } ^ { t } \right]$ , where $\underline { { a } } _ { r s } ^ { t } =$ Max $\left\{ \underline { { a } } _ { r s } ^ { t , ( k ) } ; \underline { { a } } _ { r s } ^ { 0 , ( k ) } ; 1 / 9 \right\}$ and $\overline { { { a } } } _ { r s } ^ { t } = M i n \{ \overline { { { a } } } _ { r s } ^ { t , ( k ) } ; \overline { { { a } } } _ { r s } ^ { 0 , ( k ) } ; { \bf 9 } \}$ . If this ink terval is null $\left( \underline { { a } } _ { r s } ^ { t } { > } \overline { { a } } _ { r s } ^ { t } \right)$ , leave the entry (r,s) of the PCCM as blank and go to Step 8.

Step 6 Obtain a precise value from this interval $b _ { r s } ^ { t } { \in } \lceil { \underline { { a } } _ { r s } ^ { t } } , \overline { { a } } _ { r s } ^ { t } \rceil$ that minimises the inconsistency of the most inconsistent matrix by solving the problem given by:

$$
\left. \operatorname{Min} _ {\alpha_ {r s}} \operatorname{Max} _ {k} \alpha^ {(k)} \left(G C I ^ {(k)} + \frac {2}{n (n - 1)} \left[ \left(\alpha_ {r s} - \alpha_ {r s} ^ {(k)}\right) ^ {2} + \frac {2 n}{n - 2} \left(\alpha_ {r s} - \alpha_ {r s} ^ {(k)}\right) \varepsilon_ {r s} ^ {(k)} \right]\right). \right.\tag{5}
$$

with $\alpha _ { r s } \mathrm { { = } } \left\lceil \log a _ { r s } ^ { t } , \log \overline { { a } } _ { r s } ^ { t } \right\rceil$ , where $\alpha _ { r s } = 1 0 \mathrm { g } \ a _ { r s }$ and $\alpha _ { r s } ^ { ( k ) } =$ log $a _ { r s } ^ { ( k ) }$

Table 5  
Priority and rankings vectors for r = 3 and no weights.

<table><tr><td>Priorities</td><td>AIJ</td><td>PCCM</td></tr><tr><td>DUV</td><td>0.540</td><td>0.452</td></tr><tr><td>IUV</td><td>0.191</td><td>0.248</td></tr><tr><td>PUV</td><td>0.096</td><td>0.099</td></tr><tr><td>EV</td><td>0.036</td><td>0.044</td></tr><tr><td>BV</td><td>0.137</td><td>0.157</td></tr><tr><td>Rankings</td><td>1-2-5-3-4</td><td>1-2-5-3-4</td></tr></table>

Table 6  
Indicators values for r = 3 and no weights.

<table><tr><td>r = 3 no weights</td><td>AIJ</td><td>PCCM</td></tr><tr><td>GCI</td><td>0.149</td><td>0.038</td></tr><tr><td>CVN</td><td>0</td><td>0</td></tr><tr><td>GCOMPI</td><td>0.468</td><td>0.568</td></tr><tr><td>PVN</td><td>0.139</td><td>0.139</td></tr></table>

\*In bold: the best value of the two methods, for each indicator

Step 7 Assign the value $b _ { r s } ^ { t }$ to the entry (r,s) and $1 / b _ { r s } ^ { t }$ to the entry $\scriptstyle ( s , r )$ of the PCCM<sup>t</sup> <sup>+</sup> <sup>1</sup> and modify the entries (r,s) and (s,r) of $\begin{array} { r } { \dot { \mathsf { A } } ^ { t } { } ^ { + 1 , ( k ) } , a _ { r s } ^ { t } { } ^ { + 1 , ( k ) } = b _ { r s } ^ { t } } \end{array}$ and $\dot { a } _ { s r } ^ { t + 1 , ( k ) } = \dot { 1 / b } _ { r s } ^ { t }$ for all k. Calculate $G \mathsf { C l } ^ { t + 1 }$

Step 8 If there are entries of the PCCM which have not yet been considered, go back to Step 2 with $t = t + 1$ . If all the entries have been considered, the process is complete.

## 3.2. The incomplete PCCM: the k-judgement augmented PCCM

On some occasions, the consistency interval judgements of all the decision makers will have a null intersection for a speci<sup>fi</sup>c matrix entry (Steps 4 and 5) and it will not be possible to achieve a complete consensus judgement matrix, even with a connected matrix. This occurs more often in the previous extension as a consequence of guaranteeing that the values of the PCCM belong to the initial consistency stability intervals (Step 5).

In this case, the procedure followed to construct the PCCM matrix provides a partial agreement on the judgements that will at least bring the decision makers closer together. For these situations, we propose a series of options that will be especially helpful in those cases in which the priority vector cannot be obtained because there are not enough judgements (a minimum of n − 1 judgements that connect all the nodes are necessary):

▪ Option 1: Only incorporate the cells that are necessary to reach the n − 1 connected entries that are required to derive the priorities. In this option, there are a number of possibilities for achieving this minimum number. We suggest two methods for selecting them:

a. Select those judgements with least variance (as in the initial PCCM algorithm).

b. Select those judgements with a minimum rejection index (see the de<sup>fi</sup>nition below).

▪ Option 2: Incorporate those entries that for a rejection index (see the de<sup>fi</sup>nition below) do not exceed a previously <sup>fi</sup>xed threshold.

▪ Option 3: Incorporate all the entries that are missing in order to obtain a complete matrix.

For the three options we recommend <sup>fi</sup>lling each given entry by using (as in the AIJ procedure) the weighted geometric mean of the values obtained for the decision makers to this entry (see Fig. 2).

The idea of de<sup>fi</sup>ning the rejection index is to avoid using the geometric mean when individual positions are strongly in disagreement with the group position, given by the geometric mean. One way to de<sup>fi</sup>ne it is to measure the smallest distance between the stability intervals when they have a null intersection.

Table 7  
Precise Consistency Consensus Matrix (PCCM) for r = 3 with weights.

<table><tr><td>PCCM</td><td>DUV</td><td>IUV</td><td>PUV</td><td>EV</td><td>BV</td></tr><tr><td>DUV</td><td>1</td><td>2.05</td><td>5.51</td><td>9</td><td>3.17</td></tr><tr><td>IUV</td><td>0.49</td><td>1</td><td>3</td><td>6.08</td><td>1.74</td></tr><tr><td>PUV</td><td>0.18</td><td>0.33</td><td>1</td><td>2.71</td><td>0.68</td></tr><tr><td>EV</td><td>0.11</td><td>0.16</td><td>0.37</td><td>1</td><td>0.35</td></tr><tr><td>BV</td><td>0.32</td><td>0.58</td><td>1.47</td><td>2.4</td><td>1</td></tr></table>

Table 8  
Priority and ranking vectors for r = 3 with weights.

<table><tr><td>Priorities</td><td>AIJ</td><td>PCCM</td></tr><tr><td>DUV</td><td>0.533</td><td>0.467</td></tr><tr><td>IUV</td><td>0.208</td><td>0.255</td></tr><tr><td>PUV</td><td>0.096</td><td>0.095</td></tr><tr><td>EV</td><td>0.037</td><td>0.044</td></tr><tr><td>BV</td><td>0.125</td><td>0.139</td></tr><tr><td>Rankings</td><td>1-2-5-3-4</td><td>1-2-5-3-4</td></tr></table>

De<sup>fi</sup>nition 2. The rejection index for the judgement (r,s) is de<sup>fi</sup>ned as

$$
R I _ {r s} = \underline {{a}} _ {r s} ^ {t} - \overline {{a}} _ {r s} ^ {t} \quad \text { when } \underline {{a}} _ {r s} ^ {t} > \overline {{a}} _ {r s} ^ {t}\tag{6}
$$

where t is the iteration of the algorithm in which the judgement (r,s) is considered and the values $a _ { r s } ^ { t }$ and $\bar { a } _ { r s } ^ { t }$ are those obtained in Step $5 \colon \underline { { a } } _ { r s } ^ { t } =$ $M a x \Big \{ a _ { r s } ^ { t , ( k ) } ; \underline { { a } } _ { r s } ^ { 0 , ( k ) } ; 1 / 9 \Big \} ; \overline { { a } } _ { r s } ^ { t } = M i n \Big \{ \overline { { a } } _ { r s } ^ { t , ( k ) } ; \overline { { a } } _ { r s } ^ { 0 , ( k ) } ; 9 \Big \}$ . When $a _ { r s } ^ { t } { > } \overline { { a } } _ { r s } ^ { t }$ the intersection in Step 5 is null and therefore the entry (r,s) is null.

With Options 1 and 2, the resulting matrix will probably be incomplete and the procedure for obtaining the priority vector and the calculation of the GCI should be adapted to the case of incomplete matrices. See, respectively, Tone [28] and Moreno-Jiménez et al. [17].

To compare the behaviour of the PCCM and that of traditional AIJ, four indicators (the same as those that were proposed by [2]) are contemplated: two are associated with the consistency of the group pairwise matrices: the Geometric Consistency Index (GCI) and the Number of Violations in Consistency (CVN); and two are associated with the compatibility between the individual judgements and the group priorities: the Geometric Compatibility Index (GCOMPI) and the Number of Violations in Priorities (PVN).

The CVN considers the mean number of entries of the group pairwise comparison matrix that do not belong to the corresponding consistency stability interval judgement of each individual, calculated for the inconsistency threshold considered in the problem. The GCOMPI measures the compatibility between the group priority vector, obtained with any of the existing procedures (PCCM, AIJ etc.), and the initial judgements of each decision maker, using an expression adapted from the GCI to the multiplicative model $( e _ { i j } ^ { ( \breve { k } ) } = a _ { i j } ^ { ( \breve { k } ) } w _ { j } ^ { ( G ) } / w _ { i } ^ { ( G ) } )$ employed in Altuzarra et al. [5] for AHP-group decision making. The PVN measures the ordinal compatibility of each AHP-GDM procedure by means of the minimum number of violations [14].

The de<sup>fi</sup>nitions for indicators in the case of complete matrices can be seen in Aguarón et al. [2]. Below are the expressions for which α<sup>(k)</sup> represents the weight of the decision maker k $( \alpha ^ { ( k ) } { \in } [ 0 , 1 ] , \sum _ { k } \alpha ^ { ( k ) } = 1 )$

Indicators values for r = 3 with weights.

<table><tr><td>r = 3 with weights</td><td>AIJ</td><td>PCCM</td></tr><tr><td>GCI</td><td>0.122</td><td>0.023</td></tr><tr><td>CVN</td><td>0.018</td><td>0</td></tr><tr><td>GCOMPI</td><td>0.464</td><td>0.529</td></tr><tr><td>PVN</td><td>0.136</td><td>0.136</td></tr></table>

\*In bold: the best value of the two methods, for each indicator.

Table 10  
Precise Consistency Consensus Matrix (PCCM) for r = 4 and no weights

<table><tr><td>PCCM</td><td>DUV</td><td>IUV</td><td>PUV</td><td>EV</td><td>BV</td></tr><tr><td>DUV</td><td>1</td><td>2.29</td><td>0</td><td>0</td><td>0</td></tr><tr><td>IUV</td><td>0.44</td><td>1</td><td>0</td><td>0</td><td>0</td></tr><tr><td>PUV</td><td>0</td><td>0</td><td>1</td><td>1.03</td><td>0.75</td></tr><tr><td>EV</td><td>0</td><td>0</td><td>0.97</td><td>1</td><td>0</td></tr><tr><td>BV</td><td>0</td><td>0</td><td>1.33</td><td>0</td><td>1</td></tr></table>

De<sup>fi</sup>nition 3. The Consistency Violation Number (CVN) for the group is given by:

$$
\mathrm{CVN} ^ {(G)} = \Sigma_ {k} \alpha^ {(k)} C V N ^ {(k, G)}\tag{7}
$$

where<sup>4</sup>

$$
\mathrm{CVN} ^ {(k, \mathrm{G})} = \frac {2}{n (n - 1)} \sum_ {i <   j} ^ {n} I _ {i j} \left(C I J A ^ {(k)} / A ^ {(G)}\right)\tag{8}
$$

and

$$
I _ {i j} \Big (C I J A ^ {(k)} / A ^ {(G)} \Big) = \left\{ \begin{array}{l l} 1 & \text {   if   } a _ {i j} ^ {(G)} \not \in \big [ \underline {{a}} _ {i j} ^ {0, (k)}, \overline {{a}} _ {i j} ^ {0, (k)} \big ] \\ 0 & \text {   otherwise   } \end{array} \right..\tag{9}
$$

De<sup>fi</sup>nition 4. The Geometric Compatibility Index (GCOMPI) for the group is given by:

$$
G C O M P I ^ {(G)} = \Sigma_ {k} a ^ {(k)} G C O M P I ^ {(k, G)}\tag{10}
$$

where

$$
G C O M P I ^ {(k, G)} = \frac {2}{(n - 1) (n - 2)} \sum_ {i <   j} \log^ {2} \left(a _ {i j} ^ {(k)} w _ {j} ^ {(G)} / w _ {i} ^ {(G)}\right).\tag{11}
$$

De<sup>fi</sup>nition 5. The Priority Violation Number (PVN) for the group is given by:

$$
\mathrm{PVN} ^ {(G)} = \Sigma_ {k} a ^ {(k)} P V N ^ {(k, G)}\tag{12}
$$

$$
\mathrm{PVN} ^ {(k, \mathrm{G})} = \mathrm{PVN} \left(A ^ {(k)} / A ^ {(\mathrm{G})}\right) = \frac {2}{(n - 1) (n - 2)} \sum_ {i <   j} ^ {n} I _ {i j} \left(A ^ {(k)} / A ^ {(\mathrm{G})}\right)\tag{13}
$$

and

$$
I _ {i j} \Big (A ^ {(k)} / A ^ {(G)} \Big) = \left\{ \begin{array}{l l} 1 & \text {if} a _ {i j} ^ {(k)} > 1   \text {and} w _ {i} ^ {G} <   w _ {j} ^ {G} \\ 0. 5 & \text {if} a _ {i j} ^ {(k)} = 1   \text {and} w _ {i} ^ {G} \neq w _ {j} ^ {G} \\ 0. 5 & \text {if} a _ {i j} ^ {(k)} \neq 1   \text {and} w _ {i} ^ {G} = w _ {j} ^ {G} \\ 0 & \text {otherwise.} \end{array} \right.\tag{14}
$$

In the case of incomplete PCCMs, the expressions of the GCI and the CVN need to be rede<sup>fi</sup>ned. This is not necessary for the GCOMPI and the PVN because the values of $a _ { i j } ^ { ( G ) }$ do not appear in their expressions.

With respect to the GCI, it is necessary to update the normalising $\scriptstyle { \mathrm { t e r m } } : { \frac { 2 } { ( n - 1 ) ( n - 2 ) } } .$ This term re<sup>fl</sup>ects the number of entries in the upper triangular block of the matrix in the complete case minus the number n − 1. For incomplete matrices, it seems logical to normalise using the number of non-null entries minus n − 1.

In the case of the CVN, two changes should be made: in the indicator function, only those non-null entries that do not belong to the CSI should be counted and the normalisation factor should be modi<sup>fi</sup>ed by dividing by the number of non-null entries.

1-judgement augmented PCCM for $\mathrm { r } = 4$ and no weights (Option 1a). In bold: the values of judgements that have been <sup>fi</sup>lled.

<table><tr><td>PCCM O1a</td><td>DUV</td><td>IUV</td><td>PUV</td><td>EV</td><td>BV</td></tr><tr><td>DUV</td><td>1</td><td>2.29</td><td>0</td><td>0</td><td>0</td></tr><tr><td>IUV</td><td>0.44</td><td>1</td><td>1.22</td><td>0</td><td>0</td></tr><tr><td>PUV</td><td>0</td><td>0.82</td><td>1</td><td>1.03</td><td>0.75</td></tr><tr><td>EV</td><td>0</td><td>0</td><td>0.97</td><td>1</td><td>0</td></tr><tr><td>BV</td><td>0</td><td>0</td><td>1.33</td><td>0</td><td>1</td></tr></table>

In what follows, we can see the rede<sup>fi</sup>ned expressions for incomplete matrices:

De<sup>fi</sup>nition 6. The Geometric Consistency Index (GCI) for an incomplete group matrix $A ^ { ( G ) } = ( a _ { i j } ^ { ( G ) } )$ is given by:

$$
GCI\Big(A^{(G)}\Big) = \frac{1}{N - (n - 1)}\sum_{i = 1}^{n}\sum_{\substack{i <   j\\ j\in P_{i}}}\log^{2}\text{with} e_{ij}^{(G)} = a_{ij}^{(G)}w_{j}^{(G)} / w_{i}^{(G)}\tag{15}
$$

where N is the total number of comparisons made (non-null entries) in the upper triangular block and $P _ { i }$ is the set of vertices adjacent to i.

De<sup>fi</sup>nition 7. The Consistency Violation Number (CVN) for the group when $A ^ { ( G ) }$ is incomplete is given by $\mathrm { C V N } ^ { \mathrm { ( G ) } } = \dot { \Sigma } _ { k } \dot { \alpha ^ { ( k ) } } C \dot { V N } ^ { ( k , \mathrm { G ) } }$ <sup>)</sup>, where

$$
C V N ^ {(k, G)} = \frac {1}{N} \sum_ {i <   j} ^ {n} I _ {i j} \left(C I J A ^ {(k)} / A ^ {(G)}\right)\tag{16}
$$

N is the total number of comparisons made (non-null entries) in the upper triangular block, and

$$
I _ {i j} \Big (C I J A ^ {(k)} / A ^ {(G)} \Big) = \left\{ \begin{array}{l l} 1 & \text { if } a _ {i j} ^ {(G)} \not \in \big [ \underline {{a}} _ {i j} ^ {(k)}, \overline {{a}} _ {i j} ^ {(k)} \big ] \text { and } a _ {i j} ^ {(G)} \text { is   not   null } \\ 0 & \text { otherwise. } \end{array} \right.\tag{17}
$$

The revised version of the algorithm and the extension for considering incomplete matrices have been programmed in Delphi and have been integrated into a DSS (PRIOR-PCCM) which is currently being translated into English. It includes all the phases of the algorithm: the calculation of the consistency stability intervals; the resolution of the optimisation problem; the derivation of priorities for incomplete matrices; evaluation of compatibility; etc.

## 4. Case study

To demonstrate how the improved procedure works in practice, it has been applied to the same case study used by Aguarón et al. [2]; a real-life, public investment project (known as ‘HistoPark’) for the restoration of the historical and cultural heritage of the village of Monreal del Campo (Aragón, Spain). The investment, including the technical plans, technical work and the acquisition and urbanization of approximately 100,000 m<sup>2</sup> of land for the development of a tourist complex, was to be around 24 million Euros. It was hoped that the park would receive some 130,000 visitors per year: 65,000 direct tourists and another 65,000 excursionists or passers-by.

## Table 12

1-judgement augmented PCCM for r = 4 and no weights (Option 1b). In bold: the values of judgements that have been <sup>fi</sup>lled.

<table><tr><td>PCCM O1b</td><td>DUV</td><td>IUV</td><td>PUV</td><td>EV</td><td>BV</td></tr><tr><td>DUV</td><td>1</td><td>2.29</td><td>0</td><td>0</td><td>0</td></tr><tr><td>IUV</td><td>0.44</td><td>1</td><td>0</td><td>0</td><td>0.95</td></tr><tr><td>PUV</td><td>0</td><td>0</td><td>1</td><td>1.03</td><td>0.75</td></tr><tr><td>EV</td><td>0</td><td>0</td><td>0.97</td><td>1</td><td>0</td></tr><tr><td>BV</td><td>0</td><td>1.06</td><td>1.33</td><td>0</td><td>1</td></tr></table>

Table 13  
3-judgements augmented PCCM for r = 4 and no weights (Option 2). In bold: the values of judgements that have been <sup>fi</sup>lled.

<table><tr><td>PCCM O2</td><td>DUV</td><td>IUV</td><td>PUV</td><td>EV</td><td>BV</td></tr><tr><td>DUV</td><td>1</td><td>2.29</td><td>0</td><td>0</td><td>0</td></tr><tr><td>IUV</td><td>0.44</td><td>1</td><td>1.22</td><td>0</td><td>0.95</td></tr><tr><td>PUV</td><td>0</td><td>0.82</td><td>1</td><td>1.03</td><td>0.75</td></tr><tr><td>EV</td><td>0</td><td>0</td><td>0.97</td><td>1</td><td>0.45</td></tr><tr><td>BV</td><td>0</td><td>1.06</td><td>1.33</td><td>2.24</td><td>1</td></tr></table>

Moreno-Jiménez et al. [20] developed a methodology for the evaluation of the viability of public investment projects based on use values (direct, indirect and potential) and non-use values (existence and bequest) for the assessment of social and environmental aspects (usually considered as intangible) in economic terms.

In the case of the HistoPark project, environmental aspects were not considered as relevant so viability was exclusively focused on the economic and social aspects, using the following <sup>fi</sup>ve values (for a more detailed description, see [2,20]): Direct Use Value (DUV); Indirect Use Value (IUV); Potential Use Value (PUV); Existence Value (EV); and Bequest Value (BV).

The <sup>fi</sup>ve values (DUV, IUV, PUV, EV and BV) were evaluated by means of a questionnaire which was sent to the spokespersons of the three political parties (PSOE, PP and $\mathrm { P A R } ) ^ { 5 }$ represented on the municipal council. Their pairwise comparison matrices are shown in Table 1.

To examine all the possible situations contemplated in this paper, we have considered a context in which a new political party (NP) has joined the municipal council. The pairwise comparison matrix for this new party is given in Table 2.

Two scenarios are considered: one in which all political parties have the same importance or weight and another in which each political party has an importance proportional to the number of councillors they have on the municipal council. For r = 3, the weights are: 5 (PSOE); 4 (PP); 2 (PAR) and for r = 4 they are: 3 (PSOE); 4 (PP); 2 (PAR); and 2 (NP). For each scenario we have considered two situations associated with the number of decision makers. In this way, four cases are contemplated: with weights, without weights, with complete PCCMs, and with incomplete PCCMs.

The following table (Table 3) gives the resulting priorities using the RGM method for each of the four individual matrices and their corresponding rankings. It can be seen that the <sup>fi</sup>rst three political parties gave the most relative importance to the DUV and the least relative importance to the EV, whilst the fourth, in contrast, gave most importance to the EV and the least to the DUV.

We have applied the procedure proposed in Section 3 to obtain the PCCM for two different situations (r = 3 and r = 4) for each scenario (equal and different weights for the actors). This results in four cases that re<sup>fl</sup>ect the four situations: Case 1 with r = 3 and equal importance for the 3 decision makers (r = 3 with no weights — complete PCCM); Case 2 with r = 3 and different importance for decision makers (r = 3 and weights — complete PCCM); Case 3 with r = 4 and equal importance for the 4 decision makers (r = 4 with no weights — incomplete PCCM); and Case 4 with r = 4 and different importance for decision makers (r = 4 and weights — incomplete PCCM). The results (the priority vectors and the indicator values) obtained for the four cases are given below.

Case 1. (r = 3 and no weights)

The PCCM obtained with the new algorithm is given in Table 4.

The priorities derived from this matrix are shown in Table 5, along with those that were obtained by applying the AIJ procedure. It can be observed that the ranking is the same.

Table 14  
6-judgements augmented PCCM for r = 4 and no weights (Option 3). In bold: the values of judgements that have been <sup>fi</sup>lled.

<table><tr><td>PCCM O3</td><td>DUV</td><td>IUV</td><td>PUV</td><td>EV</td><td>BV</td></tr><tr><td>DUV</td><td>1</td><td>2.29</td><td>2.65</td><td>2.82</td><td>2.15</td></tr><tr><td>IUV</td><td>0.44</td><td>1</td><td>1.22</td><td>2.32</td><td>0.95</td></tr><tr><td>PUV</td><td>0.38</td><td>0.82</td><td>1</td><td>1.03</td><td>0.75</td></tr><tr><td>EV</td><td>0.35</td><td>0.43</td><td>0.97</td><td>1</td><td>0.45</td></tr><tr><td>BV</td><td>0.46</td><td>1.06</td><td>1.33</td><td>2.24</td><td>1</td></tr></table>

When comparing the PCCM and AIJ using the indicators proposed in Section 2 (Table 6), it should be noted (as was expected, given the construction of both matrices) that: (i) the consistency (cardinal consistency) for the PCCM (GCI(PCCM) = 0.038) is considerably better than that of the AIJ (GCI(AIJ) = 0.149), the GCI(AIJ) is almost four times greater than the GCI(PCCM), and the number of violations in consistency (ordinal consistency) for both methods coincide (CVN(PCCM) = CVN(AIJ) = 0); (ii) with respect to the compatibility (cardinal compatibility) between the group priorities obtained with the PCCM and the AIJ, the values for the AIJ (GCOMPI(AIJ) = 0.468) are better (17.5%) than those of the PCCM (GCOMPI(PCCM) = 0.568). Finally, the analysis of the number of violations (ordinal compatibility) found that both methods gave the same result (PVN(AIJ) = PVN(PCCM) = 0.139).

These results are slightly different from those obtained by Aguarón et al. [2] because the algorithm we have applied is different. It is necessary for the values of the PCCM to fall within the initial stability intervals of the different decision makers and they must belong to the interval [1/9,9].

## Case 2. (r = 3 with weights)

In the second scenario, the weight associated with each political party is proportional to the number of councillors on the city council (PSOE: 5; PP: 4; and PAR: 2); the new PCCM matrix is given in Table 7.

The PCCM is slightly different to that obtained in the previous case. The priorities derived from this matrix as well as those obtained with the AIJ procedure are shown in Table 8.

Table 9 shows the indicators values for both group procedures: AIJ and PCCM. With respect to the indicators that measure consistency (GCI and CVN), the values are better for the PCCM: the GCI(PCCM) = 0.023 is considerably better than the GCI(AIJ) = 0.122 (the GCI(AIJ) is more than <sup>fi</sup>ve times greater than the PCCM), and the CVN(PCCM) = 0 is also better than the CVN(AIJ) = 0.018.

With respect to the compatibility between the group priorities obtained with the PCCM and that provided by the AIJ, the values for the AIJ (GCOMPI(AIJ) = 0.464) are better (12.3%) than those of the PCCM (GCOMPI(PCCM) = 0.529). Finally, in the analysis of the number of violations (ordinal compatibility), both methods gave the same result (PVN(AIJ) = PVN(PCCM) = 0.136).

## Case 3. (n = 4 and no weights)

The PCCM obtained by applying the procedure described in Section 3 is given in Table 10.

As can be observed, this PCCM is incomplete and not all the entries are connected. The <sup>fi</sup>rst two alternatives are connected on one side and the three last alternatives on the other. This means that the priority vector cannot be calculated unless new judgements are considered, but at least a partial agreement between the decision makers is provided. They all agree that the <sup>fi</sup>rst alternative (DUV) is better than the second (IUV) and that the <sup>fi</sup>fth alternative (BV) is better than the third (PUV), which is better than the fourth (EV), however, the decision makers have different opinions on the ranking between these two groups of alternatives.

Table 15  
Priorities and rankings for the different options with r = 4 and no weights.

<table><tr><td>Priorities (r = 4, no weights)</td><td>AIJ</td><td>PCCM O1a</td><td>PCCM O1b</td><td>PCCM O2</td><td>PCCM O3</td></tr><tr><td>DUV</td><td>0.366</td><td>0.384</td><td>0.388</td><td>0.396</td><td>0.374</td></tr><tr><td>IUV</td><td>0.188</td><td>0.167</td><td>0.169</td><td>0.172</td><td>0.188</td></tr><tr><td>PUV</td><td>0.141</td><td>0.136</td><td>0.135</td><td>0.131</td><td>0.137</td></tr><tr><td>EV</td><td>0.091</td><td>0.132</td><td>0.130</td><td>0.105</td><td>0.106</td></tr><tr><td>BV</td><td>0.214</td><td>0.181</td><td>0.179</td><td>0.195</td><td>0.196</td></tr><tr><td>Rankings</td><td>1-5-2-3-4</td><td>1-5-2-3-4</td><td>1-5-2-3-4</td><td>1-5-2-3-4</td><td>1-5-2-3-4</td></tr></table>

Table 16 Table 16  
Indicators for r = 4 and no weights. In bold: the best value of the <sup>fi</sup>ve methods, for each indicator.

<table><tr><td>r = 4 no weights</td><td>AIJ</td><td>PCCM O1a</td><td>PCCM O1b</td><td>PCCM O2</td><td>PCCM O3</td></tr><tr><td>GCI</td><td>0.073</td><td>0</td><td>0</td><td>0.046</td><td>0.044</td></tr><tr><td>CVN</td><td>0.3</td><td>0</td><td>0.063</td><td>0.083</td><td>0.275</td></tr><tr><td>GCOMPI</td><td>2.867</td><td>3.019</td><td>3.015</td><td>2.908</td><td>2.893</td></tr><tr><td>PVN</td><td>0.187</td><td>0.187</td><td>0.187</td><td>0.187</td><td>0.187</td></tr></table>

In order to obtain a complete ranking we need to add new judgements to this matrix. In what follows, we apply the three options which were proposed in Section 3 to examine how they function in practice. The <sup>fi</sup>rst possibility (Option 1) is to only complete the minimum number of entries that will provide the possibility of obtaining the priorities. In this particular case, we have 6 possible judgements {(1,3),(1,4), (1,5), (2,3), (2,4), (2,5)} to be <sup>fi</sup>lled. We consider two methods for the selection of these judgements:

Option 1a: Select the judgement with the smallest variability. In this case, the empty entry with least variance is judgement (2,3). We <sup>fi</sup>ll this judgement with the geometric mean value (as in the AIJ matrix); the PCCM, extended with this judgement, is given in Table 11. The priority vector and the indicator values can now be calculated.

Option 1b: Select the judgement with the least rejection index. In this case, the judgement is (2,5). The augmented PCCM is given in Table 12.

Another possibility is to <sup>fi</sup>ll all the judgements for which the rejection index is less than a given threshold (Option 2). In this case, the rejection index values vary from 0.015 for entry (2,5) to 6.573 for entry (1,4). We decided to select those judgements for which the rejection index is less than 1 {(2,5), (4,5) and (2,3)}. This means that even though there is no intersection between the consistency stability intervals of all the decision makers, their values differ by no more than 1 unit. The new augmented PCCM, adding these 3 judgements, is given in Table 13.

Finally, we <sup>fi</sup>ll all the empty judgements with the geometric mean values (Option 3); the new matrix is given in Table 14.

The priority vectors for these four matrices (Tables 11–14) are shown in Table 15.

It should be noted that the ranking is always the same. The values of the indicators for these options are given in Table 16.

With respect to the indicators that measure the consistency (GCI and CVN), the values are better for the different options for augmenting the PCCM with different numbers of judgements: the GCI of the worst option for the PCCM, GCI(PCCM O2) = 0.046 is considerably better than the GCI(AIJ) = 0.073, and the CVN values for all the k-judgement augmented PCCMs are also better than those of the CVN(AIJ) = 0.3.

With regard to the compatibility between the group priorities obtained with the k-judgement augmented PCCMs and those provided by the AIJ, the values for the AIJ (GCOMPI(AIJ) = 2.867) are slightly better (maximum 5%) than those of the k-judgement augmented PCCMs (the highest value is GCOMPI(PCCM O1a) = 3.019). Finally, the analysis of the number of violations (ordinal compatibility) revealed that all the methods gave the same result $( \mathrm { P V N } ( \mathrm { A I J } ) = \mathrm { P V N } ( \mathrm { P C C M O n } ) = 0 . 1 8 7 )$

Table 17  
Precise Consistency Consensus Matrix (PCCM) for r = 4 and weights.

<table><tr><td>PCCM</td><td>DUV</td><td>IUV</td><td>PUV</td><td>EV</td><td>BV</td></tr><tr><td>DUV</td><td>1</td><td>2.47</td><td>0</td><td>0</td><td>0</td></tr><tr><td>IUV</td><td>0.41</td><td>1</td><td>0</td><td>0</td><td>0</td></tr><tr><td>PUV</td><td>0</td><td>0</td><td>1</td><td>1.01</td><td>0.62</td></tr><tr><td>EV</td><td>0</td><td>0</td><td>0.99</td><td>1</td><td>0</td></tr><tr><td>BV</td><td>0</td><td>0</td><td>1.61</td><td>0</td><td>1</td></tr></table>

Table 18  
1-judgement augmented PCCM for r = 4 and weights (Option 1a). In bold: the values of judgements that have been <sup>fi</sup>lled.

<table><tr><td>PCCM O1a</td><td>DUV</td><td>IUV</td><td>PUV</td><td>EV</td><td>BV</td></tr><tr><td>DUV</td><td>1</td><td>2.47</td><td>0</td><td>0</td><td>0</td></tr><tr><td>IUV</td><td>0.41</td><td>1</td><td>1.56</td><td>0</td><td>0</td></tr><tr><td>PUV</td><td>0</td><td>0.64</td><td>1</td><td>1.01</td><td>0.62</td></tr><tr><td>EV</td><td>0</td><td>0</td><td>0.99</td><td>1</td><td>0</td></tr><tr><td>BV</td><td>0</td><td>0</td><td>1.61</td><td>0</td><td>1</td></tr></table>

## Case 4. (r = 4 with weights)

If we consider different weights for the four decision makers $( \alpha _ { 1 } = 3 ;$ $\alpha _ { 2 } = 4 ; \alpha _ { 3 } = 2 ; \alpha _ { 4 } = 2 )$ , the PCCM is given in Table 17.

Once again it can be noted that the PCCM is incomplete and exactly the same judgements are missing. We therefore have the same three options as in the previous case. If we only <sup>fi</sup>ll the minimum number of judgements (Option 1) required for deriving the priorities, we again have 6 possibilities. We consider the two possibilities for selecting one of them:

Option 1a: The entry with least variance is once again judgement (2,3). The 1-judgement augmented PCCM <sup>fi</sup>lling this judgement with the geometric mean value is given in Table 18.

Option 1b: the entry with least value for the rejection index is (4,5) but adding this judgement will not allow us to derive the priority vector as it does not connect all the judgements. The next judgement with the least rejection index is entry (2,5) which does allow us to derive the priority vector, therefore, it is the one that we select. The new 1-judgement augmented PCCM is given in Table 19.

Option 2 selects those judgements for which the rejection index is less than a previously <sup>fi</sup>xed threshold. We established the value of threshold as equal to 1, so the judgements that were selected were (4,5), (2,5), and (2,3). The 3-judgement augmented PCCM is given in Table 20.

Finally, if we <sup>fi</sup>ll all the empty judgements with the geometric mean values (Option 3) we have the new matrix that is shown in Table 21.

The priority vectors for these matrices (Tables 18–21) are summarised in Table 22.

It can be seen that the rankings that are obtained are very similar, but not always the same: there are differences in the ranking between the second alternative (IUV) and the <sup>fi</sup>fth (BV). The values of the indicators are given in Table 23.

With regard to the indicators that measure consistency (GCI and CVN), the values are better for the different options considered for augmenting the PCCM with different numbers of judgements. The GCI of the worst option for the PCCM, $\operatorname { G C I } ( \operatorname { P C C M } \mathrm { O 3 } ) = 0 . 0 5 6$ is considerably better than the $\operatorname { G C I } ( { \mathrm { A I J } } ) = 0 . 0 8 8$ , and the CVN values for all the k-judgement augmented PCCMs are also better than those of the $\mathrm { C V N } ( \mathrm { A I J } ) = 0 . 2$

With respect to the compatibility between the group priorities obtained with the k-judgement augmented PCCMs and those provided by the AIJ, the values for the AIJ $( \mathrm { G C O M P I } ( \mathrm { A I J } ) = 2 . 3 9 5 )$ are slightly better (maximum 6.8%) than those of the k-judgement augmented PCCMs (the highest value is GCOMPI(PCCM O1a) = 2.584). Finally, the analysis of the number of violations (ordinal compatibility) found that the AIJ and two of the augmented PCCMS (O1b and O3) gave the same result $( \mathrm { P V N } ( \mathrm { A I J } ) = \mathrm { P V N } ( \mathrm { P C C M } 0 \mathrm { n } ) = 0 . 1 3 6 )$ whilst with the other two options for augmenting the PCCM (O1a and O2) the result is worse $( \mathrm { P V N } = 0 . 1 8 2 )$ than the former value. This is due to the different rankings that are obtained for these two options, as was seen in Table 22.

Table 19  
1-judgement augmented PCCM for r = 4 and weights (Option 1b). In bold: the values of judgements that have been <sup>fi</sup>lled.

<table><tr><td>PCCM O1b</td><td>DUV</td><td>IUV</td><td>PUV</td><td>EV</td><td>BV</td></tr><tr><td>DUV</td><td>1</td><td>2.47</td><td>0</td><td>0</td><td>0</td></tr><tr><td>IUV</td><td>0.41</td><td>1</td><td>0</td><td>0</td><td>1.09</td></tr><tr><td>PUV</td><td>0</td><td>0</td><td>1</td><td>1.01</td><td>0.62</td></tr><tr><td>EV</td><td>0</td><td>0</td><td>0.99</td><td>1</td><td>0</td></tr><tr><td>BV</td><td>0</td><td>0.92</td><td>1.61</td><td>0</td><td>1</td></tr></table>

Table 20  
3-judgements augmented PCCM for r = 4 and weights (Option 2). In bold: the values of judgements that have been <sup>fi</sup>lled.

<table><tr><td>PCCM O2</td><td>DUV</td><td>IUV</td><td>PUV</td><td>EV</td><td>BV</td></tr><tr><td>DUV</td><td>1</td><td>2.47</td><td>0</td><td>0</td><td>0</td></tr><tr><td>IUV</td><td>0.41</td><td>1</td><td>1.56</td><td>0</td><td>1.09</td></tr><tr><td>PUV</td><td>0</td><td>0.64</td><td>1</td><td>1.01</td><td>0.62</td></tr><tr><td>EV</td><td>0</td><td>0</td><td>0.99</td><td>1</td><td>0.38</td></tr><tr><td>BV</td><td>0</td><td>0.92</td><td>1.61</td><td>2.66</td><td>1</td></tr></table>

In the four cases, the GCI for the PCCM is always considerably better when it is complete and this is true for the k-judgement augmented PCCM when incomplete; the CVN is better for the different PCCM options than that for the AIJ matrix (except in one case in which they are equal); the GCOMPI value is slightly better for the AIJ matrix than for the PCCM options and the PVN almost always takes the same values for the AIJ and the PCCM options.

As we have said, the objective of this tool is to identify unanimously accepted consensus positions from the point of view of consistency; the positions are not ‘vetoed’ by the decision makers because the judgements considered for the collective matrix fall inside the individual consistency stability intervals. Therefore, as could be expected, for reasons of construction, CVN(PCCM) ≤ CVN(AIJ). The PCCM does not seek to minimise cardinal compatibility; the analysed cases verify that GCOMPI(AIJ) ≤ GCOMPI(PCCM). Nevertheless (and this is not the objective of this paper), procedures for the improvement of PCCM compatibility can be established by following an approximation that is similar to that of Dong et al. [12].

As with our approach, the Dong et al. [12] model contemplates the construction of a consensus matrix in AHP-GDM with multiplicative preference relations, utilising the row geometric mean prioritisation procedure. Both algorithms (the PCCM and Dong et al.) help decision makers to reach consensus. The PCCM algorithm assumes all the decision makers present acceptable consistency and it is therefore unnecessary to include an iterative procedure to improve the initial individual consistencies; the PCCM does not modify the initial judgements in its search for consistency. Finally, in the analysed cases, the PCCM also veri<sup>fi</sup>es the Pareto principle, although its theoretical justi<sup>fi</sup>cation has not yet been resolved. It is our intention to complete an extensive comparative study of both methods in due course.

## 5. Conclusions

In this paper, we have rede<sup>fi</sup>ned the original algorithm that obtains the Precise Consensus Consistency Matrix [2] by adapting it to the case of multiple decision makers with different weights although this means that it is signi<sup>fi</sup>cantly more dif<sup>fi</sup>cult to solve the optimisation problem for the iterations of the algorithm. We have also strengthened the idea of consistency by guaranteeing that the values of the PCCM belong to the initial consistency stability intervals. This avoids the rejection (veto) inherent in moving away from the initial positions to a degree that is superior to that which is assumed by the accepted inconsistency.

Table 21  
6-judgements augmented PCCM for r = 4 and weights (Option 3). In bold: the values of judgements that have been <sup>fi</sup>lled.

<table><tr><td>PCCM O3</td><td>DUV</td><td>IUV</td><td>PUV</td><td>EV</td><td>BV</td></tr><tr><td>DUV</td><td>1</td><td>2.47</td><td>3.35</td><td>3.83</td><td>2.75</td></tr><tr><td>IUV</td><td>0.41</td><td>1</td><td>1.56</td><td>3.04</td><td>1.09</td></tr><tr><td>PUV</td><td>0.3</td><td>0.64</td><td>1</td><td>1.01</td><td>0.62</td></tr><tr><td>EV</td><td>0.26</td><td>0.33</td><td>0.99</td><td>1</td><td>0.38</td></tr><tr><td>BV</td><td>0.36</td><td>0.92</td><td>1.61</td><td>2.66</td><td>1</td></tr></table>

Table 22  
Priorities and rankings for the different options with r = 4 and weights.

<table><tr><td colspan="2">Priorities (r = 4, AIJ with weights)</td><td>PCCM O1a</td><td>PCCM O1b</td><td>PCCM O2</td><td>PCCM O3</td></tr><tr><td>DUV</td><td>0.411</td><td>0.427</td><td>0.447</td><td>0.446</td><td>0.419</td></tr><tr><td>IUV</td><td>0.198</td><td>0.173</td><td>0.181</td><td>0.181</td><td>0.199</td></tr><tr><td>PUV</td><td>0.125</td><td>0.111</td><td>0.103</td><td>0.104</td><td>0.112</td></tr><tr><td>EV</td><td>0.071</td><td>0.110</td><td>0.102</td><td>0.085</td><td>0.086</td></tr><tr><td>BV</td><td>0.194</td><td>0.179</td><td>0.166</td><td>0.184</td><td>0.184</td></tr><tr><td>Rankings</td><td>1-2-5-3-4</td><td>1-5-2-3-4</td><td>1-2-5-3-4</td><td>1-5-2-3-4</td><td>1-2-5-3-4</td></tr></table>

Moreover, we have proposed different options for action when the procedure is not able to obtain a complete matrix. The options considered varied from only <sup>fi</sup>lling the minimum number of judgements necessary to derive the priorities, to the case in which all the judgements are <sup>fi</sup>lled. For incomplete matrices, we have also rede<sup>fi</sup>ned the four indicators considered by Aguarón et al. [2] in order to compare the results obtained using the PCCM with those obtained by the AIJ.

The procedure was applied to a real-life experience concerned with the analysis of the integral viability of public investment projects. In the application, the constructed PCCM showed (as was expected by de<sup>fi</sup>nition) signi<sup>fi</sup>cantly better values for the GCI, and for the CVN, in most of the cases, than those of traditional AHP-GDM approaches (AIJ and AIP) for both scenarios: complete and incomplete matrices. The PCCM also provided very close or similar values to those of the AIJ and AIP for the PVN and slightly worse values for the GCOMPI.

It should be emphasised that unlike other consensus methods, the PCCM offers values for the group consensus matrix (except those additionally included in order to derive the priorities) that are very close to those of the initial individual judgement matrices. The procedure maintains the group values around the individual initial values in a range that is acceptable when taking into account the inconsistency allowed for the decision makers. The preservation of initial positions is a logical criterion that should be considered and respected when synthesising individual positions to reach a collective one.

Mainly due to its mathematical properties, it was decided to utilise the RGM method as the prioritisation procedure for the PCCM. Furthermore, at least from a deterministic point of view, the RGM gives the same results for two (AIJ and the AIP) of the most widely used procedures in AHP-GDM. There are still some questions that can be examined in future works, for example, (i) a comparison of the behaviour of the PCCM and other consensus methods used in AHP-GDM and (ii) an extension of the analysis to other prioritisation procedures.

One of the hypothetical limitations of this new procedure for AHPmultiactor decision making is the possibility of reaching incomplete matrices for the PCCM; we should underline the fact that this constructive method automatically provides (without the direct intervention of the actors) relevant knowledge for the resolution process. The PCCM identi<sup>fi</sup>es the entries for the group matrix at the point where agreement between all decision makers is reached, and where some of them are in disagreement. This information could be considered as an initial stage in any future negotiation process with personal participation (establishing agreement or consensus paths).

Indicators for r = 4 and weights. In bold: the best value of the <sup>fi</sup>ve methods, for each indicator.

<table><tr><td>r = 4 with weights</td><td>AIJ</td><td>PCCM O1a</td><td>PCCM O1b</td><td>PCCM O2</td><td>PCCM O3</td></tr><tr><td>GCI</td><td>0.088</td><td>0</td><td>0</td><td>0.054</td><td>0.056</td></tr><tr><td>CVN</td><td>0.2</td><td>0</td><td>0.045</td><td>0.091</td><td>0.182</td></tr><tr><td>GCOMPI</td><td>2.395</td><td>2.584</td><td>2.569</td><td>2.463</td><td>2.439</td></tr><tr><td>PVN</td><td>0.136</td><td>0.182</td><td>0.136</td><td>0.182</td><td>0.136</td></tr></table>

In short, the PCCM is a new decisional tool that will support complex multiactor decision making from a cognitive perspective [6]. It allows the identi<sup>fi</sup>cation of the critical points and decisional opportunities of the resolution process in addition to identifying the actors and judgements where discrepant positions appear. Even though the PCCM was de<sup>fi</sup>ned for a local context (a single criterion), it can naturally be extended to a hierarchy; all that is required is that it is applied to each node.

## Acknowledgements

This research was partially <sup>fi</sup>nanced by the project “Social Cognocracy Network” (Ref. ECO2011-24181), supported by the Spanish Ministry of Science and Innovation. The authors are grateful to the editor and the three anonymous referees for their comments and suggestions that have improved the quality of the article. The authors would also like to acknowledge the efforts of English language translation professional David Jones in preparing and proofreading the <sup>fi</sup>nal draft.

## References

[1] J. Aguarón, M.T. Escobar, J.M. Moreno-Jiménez, Consistency stability intervals for a judgement in AHP decision support systems, European Journal of Operational Research 145 (2) (2003) 382–393.

[2] J. Aguarón, M.T. Escobar, J.M. Moreno-Jiménez, The precise consistency consensus matrix in a local AHP-group decision making context, Annals of Operations Research (2014) http://dx.doi.org/10.1007/s10479-014-1576-8.

[3] J. Aguarón, J.M. Moreno-Jiménez, The geometric consistency index: approximate thresholds, European Journal of Operational Research 147 (1) (2003) 137–145.

[4] S. Alonso, E. Herrera-Viedma, F. Chiclana, F. Herrera, A web based consensus support system for group decision making problems and incomplete preferences, Information Sciences 180 (2010) 4477–4495.

[5] A. Altuzarra, J.M. Moreno-Jiménez, M. Salvador, A Bayesian priorization procedure for AHP-group decision making, European Journal of Operational Research 182 (1) (2007) 367–382.

[6] A. Altuzarra, J.M. Moreno-Jiménez, M. Salvador, Consensus building in AHP-group decision making: a Bayesian approach, Operations Research 58 (6) (2010) 1755-1773

[7] N. Bryson, Group decision making and the analytic hierarchy process: exploring the consensus-relevant information content, Computers and Operations Research 23 (1996) 27–35.

[8] D. Cao, L.C. Leung, J.S. Law, Modifying inconsistent comparison matrix in analytic hi erarchy process: a heuristic approach, Decision Support Systems 44 (2008) 944–953.

[9] F. Chiclana, F. Mata, L. Martínez, E. Herrera-Viedma, S. Alonso, Integration of a consistency control module within a consensus decision making model, International Journal of Uncertainty, Fuzziness & Knowledge Based Systems 16 (1) (2008) 35–53

[10] A.K. Choudhury, R. Shankar, M.K. Tiwari, Consensus-based intelligent group decision-making model for the selection of advanced technology, Decision Support Systems 42 (2006) 1776–1799.

[11] G. Crawford, C. Williams, A note on the analysis of subjective judgement matrices, Journal of Mathematical Psychology 29 (1985) 387–405.

[12] Y. Dong, G. Zhang, W.H. Hong, Y. Xu, Consensus models for AHP group decision making under row geometric mean prioritization method, Decision Support Systems 49 (2010) 281–289

[13] E. Forman, K. Peniwati, Aggregating individual judgements and priorities with the analytic hierarchy process, European Journal of Operational Research 108 (1998) 165–169.

[14] B. Golany, M. Kress, A multicriteria evaluation of methods for obtaining weights from ratio-scale matrices, European Journal of Operational Research 69 (1993) 210-220

[15] F. Herrera, E. Herrera-Viedma, J.L. Verdegay, A model of consensus in group decision making under linguistic assessments, Fuzzy Sets and Systems 78 (1996) 73–87.

[16] R.E. Jensen, Comparison of consensus methods for priority ranking problems, Decision Sciences 17 (1986) 195–211.

[17] J.M. Moreno-Jiménez, J. Aguarón, M.T. Escobar, The core of consistency in AHP-group decision making, Group Decision and Negotiation 17 (3) (2008) 249–265.

[18] J.M. Moreno-Jiménez, J. Aguarón, A. Raluy, A. Turón, A spreadsheet module for consistent AHP-consensus building, Group Decision and Negotiation 14 (2) (2005) 89–108.

[19] J.M. Moreno-Jiménez, J. Cardeñosa, C. Gallardo, M.A. de la Villa-Moreno, A new e-learning tool for cognitive democracies in the Knowledge Society, Computers in Human Behavior 30 (2014) 9–18

[20] J.M. Moreno-Jiménez, C. Gómez-Bahillo, J. Sanaú, Viabilidad Integral de Proyectos de Inversión Pública. Valoración económica de los aspectos sociales, in: J.R. Pires, J. Dioniso Monteiro (Eds.), Anales de Economía Aplicada, XXIII, Delta, Madrid 2009, pp. 2551–2562.

[21] J.M. Moreno-Jiménez, M. Salvador, P. Gargallo, A. Altuzarra, Systemic decision making in AHP: a Bayesian approach, Annals of Operations Research (2014)http://dx. doi.org/10.1007/s10479-014-1637-z.

[22] R. Ramanathan, L.S. Ganesh, Group preference aggregation methods employed in AHP: an evaluation and intrinsic process for deriving members' weightages, European Journal of Operational Research 79 (1994) 249–265.

[23] T.L. Saaty, Multicriteria Decision Making: the Analytic Hierarchy Process, Mc Graw-Hill, New York, 1980. (2nd impression 1990, RSW Pub. Pittsburgh).

[24] T.L. Saaty, Fundamentals of Decision Making, RSW Publications, 1994.

[25] T.L. Saaty, A ratio scale metric and compatibility of ratio scales: the possibility of Arrows's impossibility, Applied Mathematics Letters 7 (1994) 51–57.

[26] T.L. Saaty, K. Peniwati, Group Decision Making: Drawing Out and Reconciling Differences, RWS Publications, Pittsburgh, 2008.

[27] B. Srdjevic, Linking analytic hierarchy process and social choice methods to support group decision-making in water management, Decision Support Systems 42 (2007) 2261–2273.

[28] K. Tone, Two Technical Notes on the AHP Based on the Geometric Mean Method, Proceedings of ISAHP'96 1996, pp. 375–381.

[29] Z. Xu, X.Q. Cai, Group consensus algorithms based on preferences relations, Information Sciences 181 (2011) 150–162.

[30] J.M. Yeh, B. Kreng, C.H. Lin, A consensus approach for synthesizing the elements of comparison matrix in the analytic hierarchy process, International Journal of Systems Science 32 (2001) 1353–1363.

[31] Z. Yue, An extended TOPSIS for determining weights of decision makers with interval numbers, Knowledge-Based Systems 24 (2011) 146–153.

[32] L. Yu, K.K. Lai, A distance-based group decision-making methodology for multiperson multi-criteria emergency decision support, Decision Support Systems 51 (2011) 307–315.

[33] L.F. Wang, Compatibility and group decision making, System Engineering Theory and Practice 20 (2000) 92–96

[34] Z.B. Wu, J.P. Xu, A consistency and consensus based decision support model for group decision making with multiplicative preference relations, Decision Support Systems 52 (2012) 757–767.

[35] G.Q. Zhang, Y.C. Dong, Y.F. Xu, Linear optimization modelling of consistency issues in group decision making based on fuzzy preference relations, Expert Systems with Applications 39 (2012) 2415–2420.

María Teresa Escobar Urmeneta is an Associate Professor of Statistics and Operations Research at the Business and Economics Faculty of the University of Zaragoza. She holds a Ph.D. in Mathematics by the University of Zaragoza. She belongs to the Multicriteria Decision Making Group at this same university (, http://gdmz.unizar.es), and her main research interests are Multicriteria Decision Making, especially with the Analytic Hierarchy Process (AHP) and its application to several <sup>fi</sup>elds such as Logistics, Environment, and E-Government. She has published several papers in journals like European Journal of Operational Research, Omega, Group Decision and Negotiation, Computers and Human Behaviour or Annals of Operations Research, as well as many book chapters and proceedings. ORCID: 0000-0003-4419-1905.

Juan Aguarón Joven is an Associate Professor of Statistics and Operations Research at the Business and Economics Faculty of the University of Zaragoza. He holds a Ph.D. in Mathematics by the University of Zaragoza and belongs to the Multicriteria Decision Making Group at this same university. His main research interests are Multicriteria Decision Making, Decision Support Systems, and Information Systems. He has published several papers in journals like European Journal of Operational Research, Group Decision and Negotiation, or Annals of Operations Research, as well as many book chapters and proceedings. ORCID: 0000-0003-3138-7597.

José María Moreno-Jiménez received the degrees in Mathematics and Economics as well as the Ph.D. degree in Applied Mathematics from the University of Zaragoza. He is a Full Professor of Operations Research and Multicriteria Decision Making in the Faculty of Economics and Business of the University of Zaragoza, Spain. He is also the Head of the Zaragoza Multicriteria Decision Making Group (, http://gdmz.unizar.es), a research group attached to the Aragon Institute of Engineering Research (I3A) that has been typi<sup>fi</sup>ed as “Excellent” by the Government of Aragón, and the Chair of the Spanish Multicriteria Decision Making Group. His main <sup>fi</sup>elds of interest are multicriteria decision making, environmental selection, strategic planning, knowledge management, evaluation of systems, logistics, and public decision making (e-government, e-participation, e-democracy and e-cognocracy). He has published more than 200 papers in scienti<sup>fi</sup>c books (LNCS, LNAI, CCIS, Advances in Soft Computing…) and journals such as Operations Research, European Journal of Operational Research, Group Decision and Negotiation, Omega, Annals of Operations Research, Computer, Standards and Interface, Mathematical and Computer Modelling, Computers in Human Behaviour, International Journal of Production Research, Government Information Quarterly, Journal of Multi-Criteria Analysis, Int. J. Social and Humanistic Computing, EPIO (Argentina), Pesquisa Operativa (Brasil), Revista Eletrônica de Sistemas de Informação (Brasil), TOP (España), Estudios de Economía Aplicada (España), and Computación y Sistemas (Méjico), among others.
