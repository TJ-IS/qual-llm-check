---
otero_id: 12770
otero_key: "F5PVDSVD"
title: "An approach to avoiding rank reversal in AHP"
authors: "Ying-Ming Wang; Taha M.S. Elhag"
year: "2006"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2005.12.002"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# An approach to avoiding rank reversal in AHP<sup>☆</sup>

Ying-Ming Wang <sup>a,b,⁎</sup>, Taha M.S. Elhag

<sup>a</sup> Project Management Division, School of Mechanical, Aerospace and Civil Engineering, The University of Manchester, PO Box 88, Manchester M60 1QD, UK

School of Public Administration, Fuzhou University, Fuzhou 350002, PR China

Received 20 September 2005; accepted 1 December 2005 Available online 18 January 2006

## Abstract

Analytic hierarchy process (AHP) has been considerably criticized for possible rank reversal phenomenon caused by the addition or deletion of an alternative. This paper looks into the cause of rank reversal phenomenon and finds that rank reversal is caused by change of local priorities before and after an alternative is added or deleted. An approach is therefore proposed to keep the local priorities unchanged to avoid rank reversal phenomenon. Two well-known numerical examples are re-examined using the proposed approach to demonstrate its validity and practicability in rank preservation. © 2005 Elsevier B.V. All rights reserved.

Keywords: Analytic hierarchy process; Multiple criteria decision making; Rank reversal; Rank preservation

## 1. Introduction

Analytic hierarchy process (AHP), as a very popular multiple criteria decision making (MCDM) tool, has been considerably criticized for its possible rank reversal phenomenon, which means changes of the relative rankings of the other alternatives after an alternative is added or deleted. Such a phenomenon was first noticed and pointed out by Belton and Gear [3], which leads to a long-lasting debate about the validity of AHP [5,6,8–

10,13,15,18,19,23–25,29,31,32,34,35], especially about the legitimacy of rank reversal [7,12,16,17,21,26].

In order to avoid the rank reversal, Belton and Gear [3] suggested normalizing the eigenvector weights of alternatives using their maximum rather than their sum, which was usually called B–G modified AHP. Saaty and Vargas [21] provided a counterexample to show that B– G modified AHP was also subject to rank reversal. Belton and Gear [4] argued that their procedure was misunderstood and insisted that their approach would not result in any rank reversal if criteria weights were changed accordingly. Schoner and Wedley [25] presented a referenced AHP to avoid rank reversal phenomenon, which requires the modification of criteria weights when an alternative is added or deleted. Schoner et al. [27] also suggested a method of normalization to the minimum and a linking pin AHP (see also [28]), in which one of the alternatives under each criterion is chosen as the link for criteria comparisons and the values in the linking cells are assigned a value of one, with proportional values in the other cells. Barzilai and Golany [1] showed that no normalization could prevent rank reversal and suggested a multiplicative aggregation rule, which replaces normalized weight vectors with weight–ratio matrices, to avoid rank reversal. Lootsma [11] and Barzilai and Lootsma [2] suggested a multiplicative AHP for rank preservation. Vargas [33] provided a practical counterexample to show the invalidity of the multiplicative AHP. Triantaphyllou [30] offered two new cases to demonstrate that the rank reversals do not occur with the multiplicative AHP, but do occur with the AHP and some of its additive variants. Leung and Cao [10] showed that Sinarchy, a particular form of analytic network process (ANP), could prevent rank reversal. As an integrative view, the AHP now supports four modes, called Absolute, Distributive, Ideal and Supermatrix modes, respectively, for scaling weights to rank alternatives [12,15,19,22]. In absolute mode, alternatives are rated one at a time and there is no rank reversal when new alternatives are added or removed. The distributive mode normalizes alternative weights under each criterion so that they sum to one, which does not preserve rank. The ideal mode preserves rank by dividing the weight of each alternative only by the weight of the best alternative under each criterion. The supermatrix mode allows one to consider dependencies between different levels of a feedback network. More recently, Ramanathan [14] suggested a DEAHP, which is claimed to have no rank reversal phenomenon. But in fact, it still suffers from rank reversal.

Our literature review shows that the rank reversal phenomenon has not been perfectly resolved and there still exist debates about the ways of avoiding rank reversals. So, this paper looks again into the cause of rank reversal and offers an alternative approach to avoid rank reversal.

The paper is organized as follows. In Section 2, we examine the rank reversal phenomenon using the numerical examples provided by Belton and Gear [3] and Saaty and Vargas [21]. In Section 3, we analyse the cause of rank reversal and propose an approach to avoid it. The two numerical examples are re-examined using the proposed approach to verify its validity and practicability in rank preservation. The paper is concluded in Section 4.

## 2. The rank reversal phenomenon

Belton and Gear [3] demonstrated the rank reversal phenomenon in AHP using a numerical example, which involves three consistent comparison matrices over four alternatives A, B, C and D with respect to three criteria a, b and $^ { c , }$ respectively, where D is a copy of B and the three criteria were assumed to be equally important. They first took no account of the alternative D and derived a ranking for A, B and C, and then considered the four alternatives together and derived a ranking for A, B, C and D, only to find that the ranking between A and B was reversed after the alternative D was added. Tables 1 and 2 show the local and composite weights for the alternatives before and after the addition of D.

As can been seen from Table 2, the ranking between A and B is B ≻ A before D is introduced, but becomes A ≻ B after D is added. The ranking is reversed. Such a phenomenon is referred to as rank reversal, which may occur not only when an alternative is added, but also when an alternative is removed. Belton and Gear thought the reason for rank reversal to happen was due to improper normalization, which normalizes the weights of alternatives to sum to one. To avoid the rank reversal, they suggested normalizing the weights of alternatives using their maximum rather than their sum. That is to say, the weights of alternatives under each criterion should be divided by their maximum, which can be expressed as:

$$
\bar {w} _ {i} = \frac {w _ {i}}{\max _ {k \in \{1 , \dots , n \}} \left\{w _ {k} \right\}}, \quad i = 1, \dots , n\tag{1}
$$

where $W { = } ( w _ { 1 } , . . . , w _ { n } ) ^ { T }$ is eigenvector weight vector and $\overline { { \boldsymbol { W } } } = ( \overline { { w } } _ { 1 } , ~ . . . , ~ \overline { { w } } _ { n } ) ^ { T }$ is B–G normalized weight vector, which we call BG weights for short. Such a modification is referred to as B–G modified AHP. The corresponding B–G normalized weights are presented in the last column of Table 1 and the second part of Table 2.

Comparison matrices and the local weights for alternatives A, B, C and D under three criteria

<table><tr><td>Criterion (importance)</td><td>Alternatives</td><td>A</td><td>B</td><td>C</td><td>D</td><td>EM weights</td><td>BG weights</td></tr><tr><td rowspan="3">Criterion a(1/3)</td><td>A</td><td>1</td><td>1/9</td><td>1</td><td></td><td>1/11</td><td>1/9</td></tr><tr><td>B</td><td>9</td><td>1</td><td>9</td><td></td><td>9/11</td><td>1</td></tr><tr><td>C</td><td>1</td><td>1/9</td><td>1</td><td></td><td>1/11</td><td>1/9</td></tr><tr><td rowspan="3">Criterion b(1/3)</td><td>A</td><td>1</td><td>9</td><td>9</td><td></td><td>9/11</td><td>1</td></tr><tr><td>B</td><td>1/9</td><td>1</td><td>1</td><td></td><td>1/11</td><td>1/9</td></tr><tr><td>C</td><td>1/9</td><td>1</td><td>1</td><td></td><td>1/11</td><td>1/9</td></tr><tr><td rowspan="3">Criterion c(1/3)</td><td>A</td><td>1</td><td>8/9</td><td>8</td><td></td><td>8/18</td><td>8/9</td></tr><tr><td>B</td><td>9/8</td><td>1</td><td>9</td><td></td><td>9/18</td><td>1</td></tr><tr><td>C</td><td>1/8</td><td>1/9</td><td>1</td><td></td><td>1/18</td><td>1/9</td></tr><tr><td rowspan="4">Criterion a(1/3)</td><td>A</td><td>1</td><td>1/9</td><td>1</td><td>1/9</td><td>1/20</td><td>1/9</td></tr><tr><td>B</td><td>9</td><td>1</td><td>9</td><td>1</td><td>9/20</td><td>1</td></tr><tr><td>C</td><td>1</td><td>1/9</td><td>1</td><td>1/9</td><td>1/20</td><td>1/9</td></tr><tr><td>D</td><td>9</td><td>1</td><td>9</td><td>1</td><td>9/20</td><td>1</td></tr><tr><td rowspan="4">Criterion b(1/3)</td><td>A</td><td>1</td><td>9</td><td>9</td><td>9</td><td>9/12</td><td>1</td></tr><tr><td>B</td><td>1/9</td><td>1</td><td>1</td><td>1</td><td>1/12</td><td>1/9</td></tr><tr><td>C</td><td>1/9</td><td>1</td><td>1</td><td>1</td><td>1/12</td><td>1/9</td></tr><tr><td>D</td><td>1/9</td><td>1</td><td>1</td><td>1</td><td>1/12</td><td>1/9</td></tr><tr><td rowspan="4">Criterion c(1/3)</td><td>A</td><td>1</td><td>8/9</td><td>8</td><td>8/9</td><td>8/27</td><td>8/9</td></tr><tr><td>B</td><td>9/8</td><td>1</td><td>9</td><td>1</td><td>9/27</td><td>1</td></tr><tr><td>C</td><td>1/8</td><td>1/9</td><td>1</td><td>1/9</td><td>1/27</td><td>1/9</td></tr><tr><td>D</td><td>9/8</td><td>1</td><td>9</td><td>1</td><td>9/27</td><td>1</td></tr></table>

Table 2  
Composite weights of the four alternatives A, B, C and D

<table><tr><td rowspan="3">Method</td><td rowspan="3">Alternative</td><td colspan="3">Criteria weights</td><td rowspan="3">Composite weights</td></tr><tr><td>Criterion a</td><td>Criterion b</td><td>Criterion c</td></tr><tr><td>1/3</td><td>1/3</td><td>1/3</td></tr><tr><td rowspan="7">EM</td><td>A</td><td>1/11</td><td>9/11</td><td>8/18</td><td>0.4512</td></tr><tr><td>B</td><td>9/11</td><td>1/11</td><td>9/18</td><td>0.4697</td></tr><tr><td>C</td><td>1/11</td><td>1/11</td><td>1/18</td><td>0.0791</td></tr><tr><td>A</td><td>1/20</td><td>9/12</td><td>8/27</td><td>0.3654</td></tr><tr><td>B</td><td>9/20</td><td>1/12</td><td>9/27</td><td>0.2889</td></tr><tr><td>C</td><td>1/20</td><td>1/12</td><td>1/27</td><td>0.0568</td></tr><tr><td>D</td><td>9/20</td><td>1/12</td><td>9/27</td><td>0.2889</td></tr><tr><td rowspan="7">BG</td><td>A</td><td>1/9</td><td>1</td><td>8/9</td><td>0.6667</td></tr><tr><td>B</td><td>1</td><td>1/9</td><td>1</td><td>0.7037</td></tr><tr><td>C</td><td>1/9</td><td>1/9</td><td>1/9</td><td>0.1111</td></tr><tr><td>A</td><td>1/9</td><td>1</td><td>8/9</td><td>0.6667</td></tr><tr><td>B</td><td>1</td><td>1/9</td><td>1</td><td>0.7037</td></tr><tr><td>C</td><td>1/9</td><td>1/9</td><td>1/9</td><td>0.1111</td></tr><tr><td>D</td><td>1</td><td>1/9</td><td>1</td><td>0.7037</td></tr></table>

It is obvious that BG weights do preserve the rank for this example. However, Saaty and Vargas [21] subsequently provided a counterexample to show that the B–G modified AHP still suffers from rank reversal. The counterexample involves three consistent comparison matrices over three alternatives A, B and C with respect to three criteria 1, 2 and 3 of equal importance. They first considered only the alternatives

Comparison matrices and the local weights for alternatives A, B and C under three criteria

<table><tr><td>Criterion</td><td>Alternatives</td><td>A</td><td>B</td><td>C</td><td>EM weights</td><td>BG weights</td></tr><tr><td rowspan="2">Criterion 1(1/3)</td><td>A</td><td>1</td><td>1/2</td><td></td><td>1/3</td><td>1/2</td></tr><tr><td>B</td><td>2</td><td>1</td><td></td><td>2/3</td><td>1</td></tr><tr><td rowspan="2">Criterion 2(1/3)</td><td>A</td><td>1</td><td>7/6</td><td></td><td>7/13</td><td>1</td></tr><tr><td>B</td><td>6/7</td><td>1</td><td></td><td>6/13</td><td>6/7</td></tr><tr><td rowspan="2">Criterion 3(1/3)</td><td>A</td><td>1</td><td>3</td><td></td><td>3/4</td><td>1</td></tr><tr><td>B</td><td>1/3</td><td>1</td><td></td><td>1/4</td><td>1/3</td></tr><tr><td rowspan="3">Criterion 1(1/3)</td><td>A</td><td>1</td><td>1/2</td><td>1/2</td><td>1/5</td><td>1/2</td></tr><tr><td>B</td><td>2</td><td>1</td><td>1</td><td>2/5</td><td>1</td></tr><tr><td>C</td><td>2</td><td>1</td><td>1</td><td>2/5</td><td>1</td></tr><tr><td rowspan="3">Criterion 2(1/3)</td><td>A</td><td>1</td><td>7/6</td><td>1</td><td>7/20</td><td>1</td></tr><tr><td>B</td><td>6/7</td><td>1</td><td>6/7</td><td>6/20</td><td>6/7</td></tr><tr><td>C</td><td>1</td><td>7/6</td><td>1</td><td>7/20</td><td>1</td></tr><tr><td rowspan="3">Criterion 3(1/3)</td><td>A</td><td>1</td><td>3</td><td>1/2</td><td>3/10</td><td>1/2</td></tr><tr><td>B</td><td>1/3</td><td>1</td><td>1/6</td><td>1/10</td><td>1/6</td></tr><tr><td>C</td><td>2</td><td>6</td><td>1</td><td>6/10</td><td>1</td></tr></table>

Table 4  
Composite weights of the three alternatives A, B and C

<table><tr><td rowspan="3">Method</td><td rowspan="3">Alternative</td><td colspan="3">Criteria Weights</td><td rowspan="3">Composite weights</td></tr><tr><td>Criterion 1</td><td>Criterion 2</td><td>Criterion 3</td></tr><tr><td>1/3</td><td>1/3</td><td>1/3</td></tr><tr><td rowspan="5">EM</td><td>A</td><td>1/3</td><td>7/13</td><td>3/4</td><td>0.5406</td></tr><tr><td>B</td><td>2/3</td><td>6/13</td><td>1/4</td><td>0.4594</td></tr><tr><td>A</td><td>1/5</td><td>7/20</td><td>3/10</td><td>0.2833</td></tr><tr><td>B</td><td>2/5</td><td>6/20</td><td>1/10</td><td>0.2667</td></tr><tr><td>C</td><td>2/5</td><td>7/20</td><td>6/10</td><td>0.4500</td></tr><tr><td rowspan="5">BG</td><td>A</td><td>1/2</td><td>1</td><td>1</td><td>0.8333</td></tr><tr><td>B</td><td>1</td><td>6/7</td><td>1/3</td><td>0.7302</td></tr><tr><td>A</td><td>1/2</td><td>1</td><td>1/2</td><td>0.6667</td></tr><tr><td>B</td><td>1</td><td>6/7</td><td>1/6</td><td>0.6746</td></tr><tr><td>C</td><td>1</td><td>1</td><td>1</td><td>1.0000</td></tr></table>

A and B and utilized the B–G modified AHP to obtain a ranking A≻B, and then took into consideration the three alternatives together and found that the B–G modified AHP produced a ranking B≻A. The comparison matrices and the local and composite weights are shown in Tables 3 and 4, from which it can be seen very clearly that the eigenvector method (EM) preserves the ranking between A and B in this example when C is added, but the B–G modified AHP does not. The reason why the B–G modified AHP fails to preserve the ranking in this example will be investigated in next section.

## 3. An approach for rank preservation

Sometimes, it may be argued that rank reversal is a normal phenomenon in some situations where avoiding it does not make sense. In what follows, we deal with the situations where the rank reversal phenomenon is thought to be unacceptable and should be avoided.

It can be observed from Table 2 that for the EM, original alternatives A, B and C take different priorities (local weights) under some or all criteria before and after the introduction of an alternative D. For example, the alternative A takes respectively the values of 1/11, 9/11 and 8/18 under criteria a, b and c before D is added, but takes the values of 1/20, 9/12 and 8/27 under the three criteria after the addition of D. In multiple criteria decision analysis (MCDA), these priority values are seen as utilities. There is no wonder that any changes in utilities may result in the changes of final ranking. This is the reason why the ranking between A and B is reversed when D is added. The reason for the B–G modified AHP to preserve the ranking among A, B and C is because this procedure enables A, B and C to keep their original priorities unchanged when D is added. For example, the alternative A takes respectively the priorities of 1/9, 1 and 8/9 under criteria a, b, and c both before and after the addition of D. Its composite weight remains unchanged. This is also true for the alternatives B and C. So, the ranking among A, B and C is preserved. No rank reversal phenomenon occurs in this example with the B–G modified AHP.

It is also observed from Table 4 that the B–G modified AHP fails to keep unchanged the priorities of the alternatives A and B under the criterion 3 after the alternative C is introduced. The alternatives A and B take respectively the priorities of 1 and 1/2 under criterion 3 before C is introduced, but take the values of 1/2 and 1/6 after the addition of C. So, rank reversal happens in this example with the B–G modified AHP.

For the first example or similar examples, Harker and Vargas [8], Saaty [17], and Saaty and Takizawa [20] argued that an exact replica or a copy of an alternative should not be added to the choice set because it adds nothing to the choice set. The composite weight of D should be computed using the same local weights as those of B [17]. If an alternative is added as a new one, which is not an exact replica or a copy of an alternative and does add new information to the choice set, then the original ranking must be ignored [17]. Saaty and Takizawa [20] also argued that if an apple and an orange were being compared and one adds another apple to the set, a new criterion such as “the number of elements of a certain type (number of apples and number of oranges)” should be added to the hierarchy to preserve one's expectations, and thus one should alter the criteria set and the priorities assigned to them.

For the second example, Belton and Gear [4] argued that the weight of criterion 3 should be changed when C is added because the introduction of C changed the local priorities of alternatives A and B. If the weight of the criterion 3 were doubled after the addition of C, then the rank reversal would not occur with the B–G modified AHP. Schoner et al. [25–28] also have the same opinion, namely, the weights of criteria should be adjusted if an alternative is added or removed. Based on this opinion, they suggested the referenced AHP, normalization to minimum and the linking pin AHP for avoiding rank reversal.

As is known, the weights of criteria are usually assumed to be independent of the number of alternatives in most of the real world MCDM problems and MCDM approaches. Although this assumption is also under debate in the AHP [5,25], it is not easy to accept the assumption that the weights or the number of criteria should vary with the number of alternatives. As a matter of fact, if the weights or the number of criteria are changed, then there will be no need to preserve rank. The rank reversal should be acceptable in this situation. So, if there is an approach that can perverse rank without the need of changing the weights or the number of criteria when an alternative is added or removed, it will be much easier to be accepted.

Based on our previous observations on Tables 2 and 4, we may come to the conclusion that the rank reversal is caused by alteration of local priorities under some or all criteria before and after an alternative is added or removed. Therefore, in order to avoid rank reversal, original local priorities of each alternative under every criterion have to remain unchanged when an alternative is added or removed. In what follows, we discuss how to keep the original priorities unchanged when an alternative is added.

Table 5  
Rescaled weight vectors for the four alternatives A, B, C and D under the three criteri

<table><tr><td>Criterion</td><td>Alternatives</td><td>A</td><td>B</td><td>C</td><td>D</td><td>EM weights</td><td>Rescaled EM weights</td><td>BG weights</td><td>Rescaled BG weights</td></tr><tr><td rowspan="4">Criterion a</td><td>A</td><td>1</td><td>1/9</td><td>1</td><td>1/9</td><td>1/20</td><td>1/11</td><td>1/9</td><td>1/11</td></tr><tr><td>B</td><td>9</td><td>1</td><td>9</td><td>1</td><td>9/20</td><td>9/11</td><td>1</td><td>9/11</td></tr><tr><td>C</td><td>1</td><td>1/9</td><td>1</td><td>1/9</td><td>1/20</td><td>1/11</td><td>1/9</td><td>1/11</td></tr><tr><td>D</td><td>9</td><td>1</td><td>9</td><td>1</td><td>9/20</td><td>9/11</td><td>1</td><td>9/11</td></tr><tr><td rowspan="4">Criterion b</td><td>A</td><td>1</td><td>9</td><td>9</td><td>9</td><td>9/12</td><td>9/11</td><td>1</td><td>9/11</td></tr><tr><td>B</td><td>1/9</td><td>1</td><td>1</td><td>1</td><td>1/12</td><td>1/11</td><td>1/9</td><td>1/11</td></tr><tr><td>C</td><td>1/9</td><td>1</td><td>1</td><td>1</td><td>1/12</td><td>1/11</td><td>1/9</td><td>1/11</td></tr><tr><td>D</td><td>1/9</td><td>1</td><td>1</td><td>1</td><td>1/12</td><td>1/11</td><td>1/9</td><td>1/11</td></tr><tr><td rowspan="4">Criterion c</td><td>A</td><td>1</td><td>8/9</td><td>8</td><td>8/9</td><td>8/27</td><td>8/18</td><td>8/9</td><td>8/18</td></tr><tr><td>B</td><td>9/8</td><td>1</td><td>9</td><td>1</td><td>9/27</td><td>9/18</td><td>1</td><td>9/18</td></tr><tr><td>C</td><td>1/8</td><td>1/9</td><td>1</td><td>1/9</td><td>1/27</td><td>1/18</td><td>1/9</td><td>1/18</td></tr><tr><td>D</td><td>9/8</td><td>1</td><td>9</td><td>1</td><td>9/27</td><td>9/18</td><td>1</td><td>9/18</td></tr></table>

Table 6  
Rescaled composite weights of the four alternatives A, B, C and D

<table><tr><td rowspan="3">Alternative</td><td colspan="3">Criteria weights</td><td rowspan="3">Composite weights</td><td rowspan="3">Normalized composite weights</td></tr><tr><td>Criterion a</td><td>Criterion b</td><td>Criterion c</td></tr><tr><td>1/3</td><td>1/3</td><td>1/3</td></tr><tr><td>A</td><td>1/11</td><td>9/11</td><td>8/18</td><td>0.4512</td><td>0.3070</td></tr><tr><td>B</td><td>9/11</td><td>1/11</td><td>9/18</td><td>0.4697</td><td>0.3196</td></tr><tr><td>C</td><td>1/11</td><td>1/11</td><td>1/18</td><td>0.0791</td><td>0.0538</td></tr><tr><td>D</td><td>9/11</td><td>1/11</td><td>9/18</td><td>0.4697</td><td>0.3196</td></tr></table>

Let $A = ( a _ { i j } ) _ { n \times n }$ be a comparison matrix with respect to some criterion and $B { = } ( b _ { i j } ) _ { ( n + 1 ) \times ( n + 1 ) }$ be the augmented comparison matrix with the same criterion after the $\left( n + 1 \right) ^ { \mathrm { t h } }$ alternative is added. Their eigenvector weights are denoted by $W _ { A } { = } ( w _ { 1 A } , ~ . . . , ~ w _ { n A } ) ^ { T }$ and $W _ { B } { = } ( w _ { 1 } , ~ . . . , ~ w _ { n + 1 } ) ^ { T } ,$ , respectively. Since $W _ { B }$ is the normalized principal right eigenvector of the comparison matrix B, namely, $B W _ { B } { = } \lambda W _ { B } ,$ , it follows that B $( k W _ { B } ) { = } \lambda _ { \operatorname* { m a x } } ( k W _ { B } )$ for any $k { > } 0 ,$ , which means $k W _ { B }$ is also a principal right eigenvector of B. The only difference between $W _ { B }$ and $\hat { W } _ { B } { = } k W _ { B }$ is that $\begin{array} { r } { \sum _ { i = 1 } ^ { n + 1 } w _ { i B } = } \end{array}$ 1 while $\textstyle \sum _ { i = 1 } ^ { n + 1 } { \hat { w } } _ { i B } = { \bar { k } } \neq 1$ <sup>¼</sup>. In order to keep the original <sup>¼</sup>priorities of the first n alternatives unchanged, the following condition has to be met:

$$
\sum_ {i = 1} ^ {n} w _ {i A} = \sum_ {i = 1} ^ {n} k w _ {i}.\tag{2}
$$

Since $\textstyle \sum _ { i = 1 } ^ { n } w _ { i A } = 1$ , we get from Eq. (2)

$$
k = 1 / \sum_ {i = 1} ^ {n} w _ {i}.\tag{3}
$$

Table 8  
Rescaled composite weights of the three alternatives A, B and C

<table><tr><td rowspan="3">Alternative</td><td colspan="3">Criteria weights</td><td rowspan="3">Composite weights</td><td rowspan="3">Normalized composite weights</td></tr><tr><td>Criterion 1</td><td>Criterion 2</td><td>Criterion 3</td></tr><tr><td>1/3</td><td>1/3</td><td>1/3</td></tr><tr><td>A</td><td>1/3</td><td>7/13</td><td>3/4</td><td>0.5406</td><td>0.2843</td></tr><tr><td>B</td><td>2/3</td><td>6/13</td><td>1/4</td><td>0.4594</td><td>0.2416</td></tr><tr><td>C</td><td>2/3</td><td>7/13</td><td>6/4</td><td>0.9017</td><td>0.4742</td></tr></table>

Accordingly,

$$
\begin{array}{l} \hat {W} _ {B} = k W _ {B} \\ = \left( \begin{array}{c c c c c} \frac {w _ {1}}{\sum_ {i = 1} ^ {n} w _ {i}}, & \frac {w _ {2}}{\sum_ {i = 1} ^ {n} w _ {i}}, & \ldots , & \frac {w _ {n}}{\sum_ {i = 1} ^ {n} w _ {i}}, & \frac {w _ {n + 1}}{\sum_ {i = 1} ^ {n} w _ {i}} \end{array} \right) ^ {T}, \end{array}
$$

4

where $\hat { W } _ { B }$ can be interpreted as the normalization with respect to the original n alternatives. Therefore, as long as we use the rescaled eigenvector $\hat { W } _ { B }$ instead of the original eigenvector $W _ { B } ,$ the original priorities of the first n alternatives under each criterion will be kept unchanged. Accordingly, the ranking among them will be able to be preserved. Such an approach is also applicable to the B–G modified AHP.

If an alternative is going to be removed, then the remaining alternatives should keep unchanged their original local priorities with respect to each criterion. Accordingly, their composite weights will not change and there will be no rank reversal to happen in this situation.

To verify the validity of our proposed approach in avoiding rank reversal, we now re-examine the previous two numerical examples using Eq. (4). The results are shown in Tables 5–8, where the composite weights are computed using the traditional AHP synthesis method. It is very clear from Tables 6 and 8 that our proposed approach produces a ranking $\mathrm { B } \sim \mathrm { D } > \mathrm { A } > \mathrm { C }$ for the first example and a ranking $\mathrm { C } \succ \mathrm { A } \succ \mathrm { B }$ for the second example. The former preserves the rank among A, B and C, while the latter preserves the rank between A and B. So, there is no rank reversal with our proposed approach.

Table 7  
Rescaled weight vectors for the three alternatives A, B and C under the three criteria

<table><tr><td>Criterion</td><td>Alternatives</td><td>A</td><td>B</td><td>C</td><td>EM weights</td><td>Rescaled EM weights</td><td>BG weights</td><td>Rescaled BG weights</td></tr><tr><td rowspan="3">Criterion 1</td><td>A</td><td>1</td><td>1/2</td><td>1/2</td><td>1/5</td><td>1/3</td><td>1/2</td><td>1/3</td></tr><tr><td>B</td><td>2</td><td>1</td><td>1</td><td>2/5</td><td>2/3</td><td>1</td><td>2/3</td></tr><tr><td>C</td><td>2</td><td>1</td><td>1</td><td>2/5</td><td>2/3</td><td>1</td><td>2/3</td></tr><tr><td rowspan="3">Criterion 2</td><td>A</td><td>1</td><td>7/6</td><td>1</td><td>7/20</td><td>7/13</td><td>1</td><td>7/13</td></tr><tr><td>B</td><td>6/7</td><td>1</td><td>6/7</td><td>6/20</td><td>6/13</td><td>6/7</td><td>6/13</td></tr><tr><td>C</td><td>1</td><td>7/6</td><td>1</td><td>7/20</td><td>7/13</td><td>1</td><td>7/13</td></tr><tr><td rowspan="3">Criterion 3</td><td>A</td><td>1</td><td>3</td><td>1/2</td><td>3/10</td><td>3/4</td><td>1/2</td><td>3/4</td></tr><tr><td>B</td><td>1/3</td><td>1</td><td>1/6</td><td>1/10</td><td>1/4</td><td>1/6</td><td>1/4</td></tr><tr><td>C</td><td>2</td><td>6</td><td>1</td><td>6/10</td><td>6/4</td><td>1</td><td>6/4</td></tr></table>

## 4. Conclusions

In this paper, we have looked into the cause of rank reversal and pointed out the rank reversal is caused by alteration of local priorities under some or all criteria before and after an alternative is added or removed. In view of this interpretation, we have worked out an approach to avoid the rank reversal in AHP. The re-examination of the two well-known numerical examples has shown the validity and practicability of our proposed approach in rank preservation.

Compared with the existing approaches for avoiding rank reversal, our proposed approach requires no changes in the weights or the number of criteria when an alternative is added or removed. Our proposed approach also normalizes the eigenvector weights, but in a quite different way from the conventional AHP, the B–G modified AHP and the linking pin AHP.

Finally, we point out our proposed approach is in no conflict with Barzilai and Golany's claim [1] that no normalization can prevent rank reversal. What they proved is that the composite weights computed respectively in terms of normalized local weights and non-normalized local weights may lead to two different rankings. But they did not prove which ranking was true. If non-normalization gives a correct ranking, then normalization may give a wrong ranking; if normalization gives a correct ranking, then non-normalization may be wrong. As is well known, normalization is necessary for most MCDM problems and approaches in order to eliminate the dimensions of different decision attributes. The rank reversal they talked about is caused by the normalization of local weights rather than by the addition or deletion of an alternative and is therefore different from the one we discussed in this paper.

## Acknowledgements

The authors are very grateful for the comments and suggestions of three anonymous referees, which have been helpful in improving the paper.

## References

[1] J. Barzilai, B. Golany, AHP rank reversal, normalization and aggregation rules, INFOR 32 (2) (1994) 57–63.

[2] J. Barzilai, F.A. Lootsma, Power relations and group aggregation in the multiplicative AHP and SMART, Journal of Multi-Criteria Decision Analysis 6 (1997) 155–165.

[3] V. Belton, T. Gear, On a shortcoming of Saaty's method of analytic hierarchies, Omega 11 (3) (1983) 228–230.

[4] V. Belton, T. Gear, The legitimacy of rank reversal – a comment, Omega 13 (3) (1985) 143–144.

[5] J.S. Dyer, Remarks on the analytic hierarchy process, Management Science 36 (1990) 249–258.

[6] J.S. Dyer, A clarification of “Remarks on the Analytic Hierarchy Process”, Management Science 36 (1990) 274–275.

[7] E.H. Forman, AHP is intended for more than expected value calculations, Decision Sciences 36 (1990) 671–673.

[8] P.T. Harker, L.G. Vagas, The theory of ratio scale estimation: Saaty's analytic hierarchy process, Management Science 33 (1987) 1383–1403.

[9] P.T. Harker, L.G. Vargas, Reply to “Remarks on the Analytic Hierarchy Process” by J.S. Dyer, Management Science 36 (1990) 269–273.

[10] L.C. Leung, D. Cao, On the efficacy of modeling multi-attribute decision problems using AHP and Sinarchy, European Journal of Operational Research 132 (2001) 39–49.

[11] F.A. Lootsma, Scale sensitivity in the multiplicative AHP and SMART, Journal of Multi-Criteria Decision Analysis 2 (1993) 87–110.

[12] I. Millet, T.L. Saaty, On the relativity of relative measures – accommodating both rank preservation and rank reversals in the AHP, European Journal of Operational Research 121 (2000) 205–212.

[13] J. Pérez, Some comments on Saaty's AHP, Management Science 41 (1995) 1091–1095.

[14] R. Ramanathan, Data envelopment analysis for weight derivation and aggregation in the analytic hierarchy process, Computers & Operations Research 33 (2006) 1289–1307.

[15] T.L. Saaty, Axiomatic foundation of the analytic hierarchy process, Management Science 32 (1986) 841–855.

[16] T.L. Saaty, Rank generation, preservation, and reversal in the analytic hierarchy decision process, Decision Sciences 18 (1987) 157–177.

[17] T.L. Saaty, Decision making, new information, ranking and structure, Mathematical Modelling 8 (1987) 125–132.

[18] T.L. Saaty, An exposition of the AHP in reply to the paper “Remarks on the Analytic Hierarchy Process”, Management Science 36 (1990) 259–268.

[19] T.L. Saaty, Highlights and critical points in the theory and application of the Analytic Hierarchy Process, European Journal of Operational Research 74 (1994) 426–447.

[20] T.L. Saaty, M. Takizawa, Dependence and independence: from linear hierarchies to nonlinear networks, European Journal of Operational Research 26 (1986) 229–237.

[21] T.L. Saaty, L.G. Vargas, The legitimacy of rank reversal, Omega 12 (5) (1984) 513–516.

[22] T.L. Saaty, L.G. Vargas, Experiments on rank preservation and reversal in relative measurement, Mathematical and Computer Modelling 17 (4–5) (1993) 13–18.

[23] T.L. Saaty, L.G. Vargas, R.E. Wendell, Assessing attribute weights by ratios, Omega 11 (1983) 9–13.

[24] S. Schenkerman, Avoiding rank reversal in AHP decisionsupport models, European Journal of Operational Research 74 (1994) 407–419.

[25] B. Schoner, W.C. Wedley, Ambiguous criteria weights in AHP: consequences and solutions, Decision Sciences 20 (1989) 462–475.

[26] B. Schoner, W.C. Wedley, E.U. Choo, A rejoinder to Forman on AHP, with emphasis on the requirements of composite ratio scales, Decision Sciences 23 (1992) 509–517.

[27] B. Schoner, W.C. Wedley, E.U. Choo, A unified approach to AHP with linking pins, European Journal of Operational Research 64 (1993) 384–392.

[28] B. Schoner, E.U. Choo, W.C. Wedley, A comment on “Rank disagreement: a comparison of multicriteria methodologies”, Journal of Multi-Criteria Decision Analysis 6 (1997) 197–200.

[29] T.J. Stewart, A critical survey on the status of multiple criteria decision making theory and practice, Omega 20 (1992) 569–586.

[30] E. Triantaphyllou, Two new cases of rank reversals when the AHP and some of its additive variants are used that do not occur with the multiplicative AHP, Journal of Multi-Criteria Decision Analysis 10 (2001) 11–25.

[31] M.D. Troutt, Rank reversal and the dependence of priorities on the underlying MAV function, Omega 16 (1988) 365–367.

[32] L.G. Vargas, Reply to Schenkerman's avoiding rank reversal in AHP decision support models, European Journal of Operational Research 74 (1994) 420–425.

[33] L.G. Vargas, Why the multiplicative AHP is invalid: a practical example, Journal of Multi-Criteria Decision Analysis 6 (3) (1997) 169–170.

[34] S.R. Watson, A.N.S. Freeling, Assessing attribute weights, Omega 10 (1982) 582–583.

[35] S.R. Watson, A.N.S. Freeling, Comment on: assessing attribute weights by ratios, Omega 11 (1983) 13.

![](/api/attachments/F5PVDSVD/fulltext/images/fee90d3b078ccbc998ee4e03626d1dd1e81115a909e3595092423ef3887d9987.jpg)

Dr. Ying-Ming Wang is a professor of Management Science in the School of Public Administration, Fuzhou University, PR China. He received his BEng degree in Industrial Electric Automation from Jiangsu University of Science and Technology in 1984, MEng and PhD degrees both in Systems Engineering, respectively, from Huazhong University of Science and Technology in 1987 and Southeast University in 1991. His research interests include multiple attribute decision analysis

(MADA), data envelopment analysis (DEA), analytic hierarchy process (AHP), evidential reasoning and neural network. He has published more than one hundred academic papers in a wide variety of journals such as European Journal of Operational Research, Fuzzy Sets and Systems, Computers and Operations Research, Information Sciences, Expert Systems with Applications, Applied Mathematics and Computation, China Soft Science, and so on.

Dr. Taha M.S. Elhag is a lecturer of Project Management in the School of Mechanical, Aerospace and Civil Engineering, University of Manchester, UK. He holds a PhD degree in Construction Project Management from the University of Liverpool. His research interests include cost modelling and tender price estimation, knowledge management and organisational learning, neural networks and fuzzy logic in project management, and infrastructure management systems such as highways, bridges and railways. His work has been published in journals such as International Journal of Project Management, International Journal of IT in Architecture, Engineering and Construction, Journal of Financial Management of Property and Construction, Expert Systems with Applications, and European Journal of Operational Research.
