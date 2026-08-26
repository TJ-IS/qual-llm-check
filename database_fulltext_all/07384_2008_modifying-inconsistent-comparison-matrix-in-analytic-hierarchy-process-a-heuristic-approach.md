---
otero_id: 7384
otero_key: "3RS954WV"
title: "Modifying inconsistent comparison matrix in analytic hierarchy process: A heuristic approach"
authors: "D. Cao; L.C. Leung; J.S. Law"
year: "2008"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2007.11.002"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Modifying inconsistent comparison matrix in analytic hierarchy process: A heuristic approach

D. Cao <sup>a</sup>, L.C. Leung <sup>b,⁎</sup>, J.S. Law

<sup>a</sup> Department of Industrial Engineering, University of Québec at Trois-Rivières, Trois-Rivières, QC, Canada G9A 5H7 b Department of Decision Sciences and Managerial Economics, Chinese University of Hong Kong, Hong Kong

Received 13 July 2007; received in revised form 23 October 2007; accepted 10 November 2007 Available online 17 November 2007

## Abstract

Test of consistency is a critical step in the AHP methodology. When a pairwise comparison matrix fails to satisfy the consistency requirement, a decision maker needs to make revisions. To aid the decision maker's revising process, several approaches identify changes to the consistency requirement with respect to changes to a single entry in the original inconsistent matrix [P.T. Harker, Derivatives of the Perron root of a positive reciprocal matrix: with application to the analytic hierarchy process, Applied Mathematics and Computation, 22, 217–232 (1987); T.L. Saaty, Decision-making with the AHP: Why is the principal eigenvector necessary, European Journal of Operational Research, 145, 85–91 (2003)]. Instead of revising single entries, Xu and Wei [Z. Xu and C. Wei, A consistency improving method in the analytic hierarchy process, European Journal of Operational Research, V.116, 443–449 (1999)] derived a consistent matrix by an auto-adaptive process based on the original inconsistent matrix. In this paper, we develop a heuristic approach that auto-generates a consistent matrix based on the original inconsistent matrix. Expressing the inconsistent matrix in terms of a deviation matrix, an iterative process adjusts the deviation matrix to improve the consistency ratio, while preserving most of the original comparison information. We show that the proposed method is able to preserve more original comparison information than Xu and Wei [Z. Xu and C. Wei, A consistency improving method in the analytic hierarchy process, European Journal of Operational Research, V.116, 443–449 (1999)]. It is also shown that the heuristic approach can be used to examine the effects of revising a sub-bloc as well as revising a single entry of the original matrix. © 2007 Elsevier B.V. All rights reserved.

Keywords: AHP; Inconsistent pairwise comparison matrix; Information preservation

## 1. Introduction

Analytic Hierarchy Process (AHP) is a multiattribute decision-making methodology widely used in many real-life problems [1,6,11]. Developed by Saaty [8], AHP uses pairwise comparisons to capture relative importance of attributes, which forms the basis of priority determination. But before a pairwise comparison matrix can be used, it needs to pass a consistency test.

The element $a _ { i j }$ of a pairwise comparison n × n matrix is the decision maker's relative preference of attribute i over attribute $j ,$ where $a _ { i j } > 0$ , and $a _ { i j } { = } 1 / a _ { j i } .$ A pairwise comparison matrix is perfectly consistent if $a _ { i j } { = } a _ { i k } \ : a _ { k j }$ holds for all element pairs. However, when performing pairwise comparisons involving intangibles, it is unrealistic to expect a pairwise comparison matrix that is perfectly consistent. Saaty [8] developed a consistency test that allows a certain level of acceptable deviations. The consistency test involves the use of a “consistency ratio”: $\begin{array} { r } { \mathrm { C R } = \frac { \lambda _ { \operatorname* { m a x } } - n } { n - 1 } / \mathrm { R I } } \end{array}$ , where $\lambda _ { \operatorname* { m a x } }$ is the maximum eigenvalue of the pairwise comparison matrix, and RI is a random index whose value depends on n. If $\mathrm { C R } > 0 . 1$ , the decision-maker is asked to revise his judgments until an acceptable level of consistency is reached. Further discussions on consistency ratio can be found in Lance and Verdini [5], Murphy [7], Saaty [9], and Finan and Hurley [2].

Several approaches have been developed to aid the revising process. Based on the sensitivity analysis of positive reciprocal matrices [4], Harker [3] identified an entry whose adjustment would result in the largest rate of change in the matrix's consistency level. Saaty [10] also discussed two similar approaches for revising a single entry, both of which use the relationship nk $\operatorname* { m a x } - n = \sum _ { \stackrel { i , j = 1 } { i \neq i } } ^ { n } \left( \varepsilon _ { i j } + { \frac { 1 } { \varepsilon _ { i } } } \right)$ where $\varepsilon _ { i j }$ is determined by the Hadamard product relationship $A = W \circ E$ in which $\boldsymbol { w } { = } ( w _ { 1 } . . . w _ { i } . . . w _ { n } ) ^ { T }$ is the principal eigenvector, $W { = } [ w _ { i } / w _ { j } ]$ and $E { = } ( \varepsilon _ { i j } )$ . The first approach identifies the $\varepsilon _ { i j }$ that is farthest from one and a change of the corresponding $a _ { i j }$ would result in a new pairwise comparison matrix with a smaller eigenvalue. The second approach is to modify the $a _ { i j }$ with the largest $\lambda _ { \mathrm { m a x } }$ resulting from perturbing each single entry of the pairwise comparison matrix A. Both methods suggest that the decision maker can improve the consistency by iteratively modifying a single entry of the pairwise comparison matrix.

Instead of revising single entries, Xu and Wei [13] proposed to develop a consistent matrix by an autoadaptive process based on the original inconsistent matrix. Here, the element $a _ { i j }$ of the entire inconsistent pairwise comparison matrix A is replaced by $b _ { i j } = a _ { i j } ^ { \alpha }$ $( w _ { i } / w _ { j } ) ^ { 1 - \alpha }$ , where $\boldsymbol { w } = ( w _ { 1 } \dots w _ { i } . . . \ w _ { n } ) ^ { T }$ is the priority vector derived from A, and α is a positive value less than but approaching 1.0. The new ratio is the weighted geometric mean of the pairwise comparison ratio and the prescribed ratio. The generated matrix $\pmb { B } = [ b _ { i j } ]$ has a reduced CR. This process is to be repeated many times, until a pairwise comparison matrix with $\mathrm { C R } \leq 0 . 1$ has been achieved. Once a consistent matrix is obtained, the decision maker can use this new matrix as a reference for revising the original inconsistent matrix.

In this paper, we develop a heuristic approach to arrive at a consistent matrix that can retain more information than Xu and Wei [13]. Firstly, the original matrix is decomposed as the Hadamard product of a consistent matrix and a reciprocal deviation matrix. Then a modified matrix is constructed via a convex combination of the reciprocal deviation matrix and a zero deviation matrix. We provide the conditions under which the modified matrix would have a reduced maximum eigenvalue, thus reducing the CR. An algorithm, which consists of autoadaptive modifications using such convex combinations, is provided. This auto-generating process will converge to an acceptable CR. We illustrate the heuristic approach using numerical examples from Xu and Wei [13]. It is also shown that the heuristic approach can be used to examine the effects of revising a sub-bloc as well as revising a single entry of the original matrix.

## 2. Notations and definitions

The matrix A can be expressed as Hadamard product of two matrices:

$$
\boldsymbol {A} = \boldsymbol {W} \circ \boldsymbol {D}
$$

where $A = [ a _ { i j } ]$ is any $n \times n$ inconsistent reciprocal matrix; $W \mathrm { = } [ \tilde { w _ { i } } / w _ { j } ] , w = ( w _ { 1 } \mathrm { ~ } . . . w _ { i } \mathrm { ~ } . . . \mathrm { ~ } w _ { n } ) ^ { T }$ is the priority vector derived from $\pmb { A } ; \pmb { D } \mathrm { = } [ d _ { i j } ]$ is a reciprocal positive matrix; and is the symbol of Hadamard product ${ \bf \Xi } ( A { = } B \circ C$ means $a _ { i j } { = } b _ { i j } c _ { i j }$ for $i { = } 1 , { \ldots } , n , j { = } 1 , { \ldots } , n )$ . The matrix D has the maximum eigenvalue $\lambda _ { \mathrm { m a x } } ( D )$ equal to $\lambda _ { \mathrm { m a x } } ( A )$ [12].

When A is a consistent matrix, all $d _ { i j } = 1$ and $\lambda _ { \mathrm { m a x } } ( { \pmb D } ) =$ $\lambda _ { \mathrm { m a x } } ( A ) = n .$ . Otherwise, at least some $d _ { i j } \neq I _ { \mathrm { : } }$ , and $\lambda _ { \mathrm { m a x } } ( { \pmb D } ) =$ $\lambda _ { \operatorname* { m a x } } ( A ) { > } n [ 8 , 1 2 ]$ . The elements in D show whether there exists deviation of the generated priorities from the pairwise dominance information. We call the matrix $\mathbf { \delta } _ { D _ { \eta } }$ a deviation matrix. The particular deviation matrix where all $d _ { i j } = 1$ is referred to as a zero deviation matrix and is denoted as D1. Our approach is to improve the consistency ratio by modifying the deviation matrix. It is analogous to the exponential smoothening technique in time-series analysis.

Definition 1. A convex combination of a deviation matrix D and a zero deviation matrix D1 is defined as:

$$
\boldsymbol {D} ^ {\prime} = \left[ d _ {i j} ^ {\prime} \right] = \gamma \boldsymbol {D} \oplus (1 - \gamma) \boldsymbol {D} \boldsymbol {I}\tag{2.1}
$$

where $\ O \leq \gamma \leq I$

$$
d _ {i j} ^ {\prime} = \gamma d _ {i j} + (1 - \gamma), \text {   for   } i, j \in \{i, j: d _ {i j} \geq 1 \} \text {   and   }
$$

$$
d _ {i j} ^ {\prime} = 1 / d _ {j i} ^ {\prime}, \text {   for   } i, j \in \{i, j: d _ {i j} <   1 \}.
$$

The modified pairwise comparison matrix $A ^ { \prime }$ is structured as the Hadamard product of the matrix W and that of the modified deviation matrix $\pmb { D } ^ { \prime }$ :

$$
\boldsymbol {A} ^ {\prime} = \boldsymbol {W} \circ \boldsymbol {D} ^ {\prime}.
$$

The properties of the modified pairwise comparison matrix $A ^ { \prime }$ are investigated next.

## 3. Main theoretical results and an algorithm

Let $\lambda _ { \mathrm { m a x } } ( D ^ { \prime } )$ and $\lambda _ { \mathrm { m a x } } ( A ^ { \prime } )$ be the maximum eigenvalues of matrix $\pmb { D } ^ { \prime }$ and $A ^ { \prime }$ respectively; and $w _ { D ^ { \prime } } { = } ( w _ { D ^ { \prime } 1 } . . .$ $w _ { D ^ { \prime } i \cdot \cdot \cdot } w _ { D ^ { \prime } n } ) ^ { T } , w ^ { \prime } = ( w ^ { \prime } { } _ { 1 \cdot \cdot \cdot } w ^ { \prime } { } _ { i \cdot \cdot \cdot } w ^ { \prime } { } _ { n } ) ^ { T }$ be the priority vector derived from matrices $\pmb { D } ^ { \prime }$ and $A ^ { \prime }$ , respectively.

By Definition 1, $\pmb { D } ^ { \prime }$ is a positive reciprocal matrix. The following lemma gives the relationship between $\lambda _ { \mathrm { m a x } } ( D ^ { \prime } )$ and $\lambda _ { \mathrm { m a x } } ( A ^ { \prime } )$ , as well as the relationship between $\lambda _ { \mathrm { m a x } } ( A )$ and $\lambda _ { \mathrm { m a x } } ( D )$ .

Lemma 1. (Horn and Johnson [4], Saaty [8])

$$
1) \lambda_ {\max} (A ^ {\prime}) = \lambda_ {\max} (D ^ {\prime}); w ^ {\prime} = w ^ {\circ} w _ {D} ^ {\prime}
$$

<sup>2</sup><sub>Þ</sub> $\lambda _ { \operatorname* { m a x } } ( A ) = \lambda _ { \operatorname* { m a x } } ( D ) .$

The following theorem states that if a certain condition is satisfied when matrix A is modified as $\scriptstyle A ^ { \prime } = W \circ D ^ { \prime }$ , then the modified matrix $A ^ { \prime }$ has a reduced maximum eigenvalue.

Theorem 1. When the inconsistent pairwise comparison matrix A is modified as $\pmb { A } ^ { \prime } = \pmb { W } \circ \pmb { D } ^ { \prime } \left( \pmb { D } ^ { \prime } \right.$ defined in $E q . ( 2 . 1 ) ) , \lambda _ { m a x } ( A ^ { \prime } )$ is less than $\lambda _ { m a x } ( A )$ , when the following condition is satisfied

$$
\max _ {i} \left\{\sum_ {j = 1} ^ {n} d _ {i j} \right\} \leq \lambda \max (\boldsymbol {D}).\tag{3.1}
$$

Proof. Let $\lambda _ { \mathrm { m a x } } ( D ^ { \prime } )$ be the maximum eigenvalue of the modified deviation matrix $\pmb { D } ^ { \prime } .$

By the Perron theorem [4], we have

$$
\lambda_ {\max} \left(\boldsymbol {D} ^ {\prime}\right) \leq \min _ {x \in \mathfrak {R} _ {n} ^ {+}} \max _ {i} \sum_ {j = 1} ^ {n} d _ {i j} ^ {\prime} \frac {x _ {j}}{x _ {i}}
$$

where $x { = } ( x _ { 1 } , \ x _ { 2 } { , } . . . , \ x _ { n } )$ is an arbitrary set of positive numbers. Setting $x _ { i } { = } 1 , i { = } 1 , . . . , n$ , the following inequality holds:

$$
\lambda_ {\max} \left(\boldsymbol {D} ^ {\prime}\right) \leq \max _ {i} \sum_ {j = 1} ^ {n} d _ {i j} ^ {\prime}\tag{3.2}
$$

$$
\leq \max _ {i} \left\{\sum_ {j = 1} ^ {n} \left(\gamma d _ {i j} + 1 - \gamma\right) \right\}.
$$

When the condition (3.1) is satisfied, the following inequality holds:

$$
\max _ {i} \left\{\sum_ {j - 1} ^ {n} \left(\gamma d _ {i j} + 1 - \gamma\right) \right\} \leq \gamma \lambda \max (\boldsymbol {D}) + n (1 - \gamma).\tag{3.3}
$$

Since $\pmb { A }$ is an inconsistent matrix with $\lambda _ { \operatorname* { m a x } } ( \pmb { D } ) = \lambda _ { \operatorname* { m a x } }$ $\left( A \right) > n ,$ , we have

$$
\lambda_ {\max} (\boldsymbol {D} ^ {\prime}) <   \lambda_ {\max} (\boldsymbol {D})
$$

Hence, by Lemma 1, we have $\lambda _ { \operatorname* { m a x } } ( A ^ { \prime } ) { < } \lambda _ { \operatorname* { m a x } } ( A )$ . □

Whether the inequality in Eq. (3.1) holds largely depends on how the priority vector is determined. This condition is obviously satisfied when the eigenvector method is used to generate the priority vector since the following equality holds: $\lambda _ { \operatorname* { m a x } } ( \pmb { D } ) = \overset { n } { \sum } d _ { i j } , i = 1 , \ldots , n$ <sup>j</sup>[8]. Recently, Saaty [10] has provided further insights on the validity of using the eigenvector method. We will leave the exploration of whether other prominent methods of determining the priority vector (e.g. geometric mean) will satisfy the inequality in Eq. (3.1) for future research. In the remainder of this paper, we assume that eigenvector method is used to generate the priority vector.

## 3.1. An algorithm

In this section, an iterative process is developed to find a modified pairwise comparison matrix with acceptable consistency level while retaining most of the original comparison information. The algorithm consists of a series of self-generated modifications with each modification in accordance to Theorem 1. To retain most of the original comparison information, γ should take on a value approaching 1.0.

Let k be the number of iterations and γ be a positive value less than but approaching 1.0. The steps are:

Step 1 Let $A ^ { ( 0 ) } = [ a _ { i j } ^ { ( 0 ) } ] = [ a _ { i j } ] , \mathrm { C R } ^ { * } = 0 . 1$ and $k { = } 0 .$

Step 2 Calculate the maximum eigenvalue $\lambda _ { \operatorname* { m a x } } ( A ^ { ( k ) } )$ of $\boldsymbol { A } ^ { ( k ) }$ the priority vector $\mathbf { \Psi } _ { w } ^ { ( k ) } { = } ( w _ { 1 } ^ { ( k ) } , . . . , w _ { i } ^ { ( k ) } , . . . , w _ { n } ^ { ( k ) } ) ^ { T }$ based on ${ \cal A } ^ { ( k ) } .$ , and the deviation matrix $\pmb { D } ^ { ( k ) } =$ $[ a _ { i j } ^ { ( k ) } / ( w _ { i } ^ { ( k ) } / w _ { j } ^ { ( k ) } ) ]$

Step 3 Calculate the consistency ratio $\mathrm { C R } ^ { ( k ) }$

Step 4 $\mathrm { I f } { C R } ^ { ( k ) } \le \mathrm { C R } ^ { * }$ , go to Step 6. Otherwise, proceed.

Step 5 Let ${ \cal A } ^ { ( k + 1 ) } { = } [ w _ { i } ^ { \top k ) } / w _ { j } ^ { ( k ) } ] \dot { \circ } { \cal D } ^ { \prime ( k ) }$ where $\pmb { D } ^ { \prime ( k ) }$ is the modified deviation matrix ${ \cal D ^ { \prime } } ^ { ( k ) } { = } [ d ^ { \prime } { } _ { i j } ^ { ( k ) } ] { = } \gamma { \bf D } ^ { ( k ) } \oplus ( 1 - \gamma ) { \cal D } I$ defined in Eq. (2.1). Let $k = k + 1$ , go to Step 2.

Step 6 $\boldsymbol { A } ^ { ( k ) }$ is the modified pairwise comparison matrix with acceptable consistency level; $w ^ { ( k ) }$ is the generated priorities vector.

## Step 7 End

It can be observed from Theorem 1 that the algorithm converges to any predetermined value of CR, provided that the value of $\gamma$ is chosen accordingly.

## 4. A comparison

Here, a comparison is made between the proposed method and that of Xu and Wei [13]. We will first examine the situation when the parameters for the two methods are identical $( \mathrm { i } . \mathrm { e } . \ \alpha = \gamma )$ . Letting $\alpha = \gamma$ merely serves as a reference point, as the two parameters have different meanings in their respective methods. We will have more discussion on this in Section 5. For Xu and Wei's method, the modified pairwise comparison matrix would be $\pmb { B } =$ $[ b _ { i j } ] { = } [ a _ { i j } ^ { \gamma } ( w _ { i } / w _ { j } ) ^ { 1 - \gamma } ]$ , where $0 \leq \gamma \ < 1$ . Using the concept of Hadamard product, B can be expressed $= [ w _ { i } / w _ { j } ]$ O $[ a _ { i j } / ( w _ { i } / w _ { j } ) ] ^ { \gamma }$ . Since $a _ { i j } / ( w _ { i } / w _ { j } ) { = } d _ { i j }$ where $\pmb { D } = [ d _ { i j } ]$ is the deviation matrix, $\pmb { D } ^ { \prime } = [ d _ { i j } ^ { \prime } ] = [ \bar { d } _ { i j } ^ { \gamma } ]$ is the modified deviation matrix in our context. And we have $\pmb { B } { = } [ w _ { i } / w _ { j } ] \circ \pmb { D } ^ { \prime }$

## 4.1. One-step modification

Let us first consider the closeness between the original matrix and a one-step modified one, for the two methods when the parameter values are the same. The closeness between the two matrices is proportional to $d _ { i } - d ^ { \prime } { } _ { i j } .$ Let $O _ { i j } { = } d _ { i j } { - } d ^ { \gamma } { _ { i j } }$ be the difference between $d _ { i j }$ and $d ^ { \prime } { } _ { i j }$ when Xu and Wei's method is used; $N _ { i j } { = } d _ { i j } { - } d { ' } _ { i j }$ the difference between $d _ { i j }$ and $d ^ { \prime } { } _ { i j }$ when our method is used. By Definition 1, we have

$$
N _ {i j} = \left\{ \begin{array}{l} (1 - \gamma) \big (d _ {i j} - 1 \big), \text {when} d _ {i j} \geq 1 \\ \frac {(1 - \gamma) \big (d _ {i j} - 1 \big)}{\gamma d _ {j i} + (1 - \gamma)}, \text {when} d _ {i j} <   1 \end{array} \right.\tag{4.1}
$$

It can be proved that

$$
\lim _ {\gamma \rightarrow 1} \frac {O _ {i j}}{N _ {i j}} = \left\{\begin{array}{l l}\frac {d _ {i j} \ln d _ {i j}}{d _ {i j} - 1} > 1&\text { when } d _ {i j} > 1\\1,&\text { when } d _ {i j} = 1. \text { In   this   case }, O _ {i j} = N _ {i j} = 0\\\frac {\ln d _ {i j}}{d _ {i j} - 1} > 1,&\text { when } d _ {i j} <   1\end{array}\right.\tag{4.2}
$$

This means that the modifications by our method are less than those by Xu and Wei's method when the parameter γ approaches 1.0. It also means that for onestep modification, our method preserves more original comparison information than Xu and Wei's method does. Next, we discuss the closeness properties for the sequences of modified comparison matrices generated by implementing the two methods.

## 4.2. k-step modification sequences

Define $A _ { N } ^ { ( k ) } , A _ { O } ^ { ( k ) }$ as the sequentially modified comparison matrices generated by implementing our method and Xu and Wei's respectively. In implementing these two methods, the parameter $\gamma$ is assigned the same value (approaching 1.0). Also, let $A _ { N } ^ { ( 0 ) } { = } \stackrel { \bf \tilde { \cal A } } { \cal O } ^ { ( 0 ) } { = } A$ (the original inconsistent matrix). Here we investigate the following series of modified comparison matrices emanating from the initial inconsistent matrix A:

$$
\boldsymbol {A}, \boldsymbol {A} _ {\boldsymbol {N}} ^ {(1)}, \boldsymbol {A} _ {\boldsymbol {N}} ^ {(2)}, \dots , \boldsymbol {A} _ {\boldsymbol {N}} ^ {(k)}, \dots , \dots \boldsymbol {A} _ {\boldsymbol {N}} ^ {(\infty)}\tag{4.3}
$$

$$
\boldsymbol {A}, \boldsymbol {A} _ {\boldsymbol {O}} ^ {(1)}, \boldsymbol {A} _ {\boldsymbol {O}} ^ {(2)}, \dots , \boldsymbol {A} _ {\boldsymbol {O}} ^ {(k)}, \dots , \dots \boldsymbol {A} _ {\boldsymbol {O}} ^ {(\infty)}\tag{4.4}
$$

By Theorem 1, the series (4.3) is convergent. The series (4.4) is a convergent one as well [13]. We have the following result:

Theorem 2. With the value γ approaching 1.0 used in both methods, the convergent matrix $A _ { N } ^ { ( \infty ) }$ preserves more original comparison information than the matrix ${ \cal A } _ { \cal O } ^ { ( \infty ) }$

Proof. In order to prove the above theorem, we investigate two different cases:

Case 1): By Eq. (4.2) we know that at iteration 1, the modified matrix $\overset { \cdot } { A } _ { N } ^ { ( 1 ) }$ preserves more original comparison information than the modified matrix $\mathbf { \hat { \mathbf { A } } } _ { O } ^ { ( 1 ) }$ when both methods use the same value approaching 1.0 for the parameter $\gamma .$ . This means that when γ approaches 1.0, $A _ { N } ^ { ( 1 ) } \twoheadrightarrow \dot { A } _ { O } ^ { ( 1 ) }$ where the symbol $" \gg "$ denotes the closeness superiority relationship. Such a relationship is with respect to the original matrix A in that the deviation of the left hand side matrix is less than that of the right hand side one with respect to the original matrix A.

Case 2): Given two matrices $A ^ { * } , A ^ { * * }$ , where $A ^ { * } { } _ { \gg } A ^ { * * }$ It can be derived that $A _ { N } ^ { * } { \gg } A _ { N } ^ { * * }$ and $A _ { O } ^ { * } { \gg } A _ { O } ^ { * * }$ for γ or α approaching 1.0 , where $A _ { N } ^ { * } , A _ { O } ^ { * }$ are the modified matrices generated using our method and Xu and Wei's method respectively.

Based on the closeness superiority relationships in cases 1 and 2, we have the following closeness superiority properties for the modified matrices ${ A } _ { N } ^ { ( 2 ) }$ and $A _ { O } ^ { ( 2 ) }$

$$
\boldsymbol {A} _ {N} ^ {(1)} \gg \boldsymbol {A} _ {\boldsymbol {O}} ^ {(1)}, \boldsymbol {A} _ {N} ^ {(2)} \gg \boldsymbol {A} _ {N \boldsymbol {O}} ^ {(2)} \gg \boldsymbol {A} _ {\boldsymbol {O}} ^ {(2)}
$$

where ${ \cal A } _ { N } ^ { ( 2 ) }$ is the pairwise comparison matrix modified from ${ \bf \cal A } _ { O } ^ { ( 1 ) }$ using our method. Similarly, the same closeness superiority relationships can be derived at iteration $k = 3$ $\cdots 9 9 ,$

$$
A _ {N} ^ {(k)} \gg A _ {N O} ^ {(k)} \gg A _ {O} ^ {(k)}
$$

where $A _ { N O } ^ { ( k ) }$ is the pairwise comparison matrix modified from $A _ { O } ^ { ( k - 1 ) }$ using our method.

That is, the closeness superiority relationship $A _ { N } ^ { ( k ) } \gg A _ { O } ^ { ( k ) }$ exists for the two series of sequentially generated modified comparison matrices $A _ { N } ^ { ( k ) }$ and $A _ { o } ^ { ( k ) }$ . Finally we have $A _ { N } ^ { ( \infty ) } \twoheadrightarrow A _ { O } ^ { ( \infty ) , }$ which means that when $\gamma$ approaches 1.0, the convergent matrix ${ \cal A } _ { N } ^ { ( \infty ) }$ preserves more original comparison information than the matrix $A _ { O } ^ { ( \infty ) }$ □

The above theorem shows that our method preserves more original information than Xu and Wei's method for the sequences of modification. The results are proved using the particular sub-sequences with $\alpha = \gamma$ approaching 1.0. Since any sub-sequence converges to the same convergence results, we can derive the results utilizing a particular sub-sequences (e.g. the subsequences with $\alpha = \gamma )$ . However, it should be noted that in the proof, the preservation of the original comparison information was discussed based on the converged matrices ${ \cal A } _ { N } ^ { ( \infty ) } , { \cal A } _ { O } ^ { ( \infty ) }$ . In practice, we do not generate an infinite series of modification matrices, but stop the sequential matrix updating process when the updated matrix ${ A _ { N } } ^ { ( k ) }$ passes the consistency test (i.e., $\bar { \mathrm { C R } } ^ { ( k ) } { \leq } 0 . 1 )$ . Thus, it is plausible that Xu and Wei's method could obtain a matrix that is closer to the original matrix.

## 5. Numerical illustration and comparison

Consider a simple situation where a company is selecting a trucking company to ship its goods. The selection of a trucking company is based on the performance of the following eight attributes: punctuality, delivery time, temperature control, track and trace, error rate, service reputation, damage or loss, and GPS features

Fig. 1 shows an AHP model where the overall goal depends on the attributes and each of the attributes will be rated against the respective trucking companies being considered. For this AHP model, an $8 \times 8$ pairwise comparison matrix (with respect to the overall goal and comparing the eight attributes) will have to be determined. Here, we let the inconsistent matrix be the one shown in Xu and Wei [13]:

$$
\boldsymbol {A} = \left( \begin{array}{c c c c c c c c} 1 & 5 & 3 & 7 & 6 & 6 & 1 / 3 & 1 / 4 \\ 1 / 5 & 1 & 1 / 3 & 5 & 3 & 3 & 1 / 5 & 1 / 7 \\ 1 / 3 & 3 & 1 & 6 & 3 & 4 & 6 & 1 / 5 \\ 1 / 7 & 1 / 5 & 1 / 6 & 1 & 1 / 3 & 1 / 4 & 1 / 7 & 1 / 8 \\ 1 / 6 & 1 / 3 & 1 / 3 & 3 & 1 & 1 / 2 & 1 / 5 & 1 / 6 \\ 1 / 6 & 1 / 3 & 1 / 4 & 4 & 2 & 1 & 1 / 5 & 1 / 6 \\ 3 & 5 & 1 / 6 & 7 & 5 & 5 & 1 & 1 / 2 \\ 4 & 7 & 5 & 8 & 6 & 6 & 2 & 1 \end{array} \right)
$$

For this matrix, the $\lambda _ { \mathrm { m a x } } ( A )$ and CR, and the principal right eigenvector $w = \left( \ w _ { 1 } \ldots w _ { i } \ldots w _ { n } \right) ^ { T }$ are:

$$
\lambda_ {\max} (\boldsymbol {A}) = 9. 6 6 9, \mathrm{CR} = 0. 1 6 9, w = (0. 1 7 3 0. 0 5 4 0. 1 8 8 0. 0 1 8 0. 0 3 1 0. 0 3 6 0. 1 6 7 0. 3 3 3) ^ {T}.
$$

Since the CR is greater than 0.1, we use the proposed heuristic approach to modify the inconsistent matrix. Here, we examine two cases: $\gamma$ is set to be 0.5 and 0.98, respectively. Xu and Wei [13] has given two criteria to measure the closeness between the original matrix A and the modified matrix $A ^ { ( m ) }$

$$
\delta = \max _ {i, j} \left\{\left| a _ {i j} ^ {(m)} - a _ {i j} \right| \right\}, i, j = 1, \dots , n\tag{C1}
$$

$$
\sigma = \sqrt {\sum_ {i = 1} ^ {n} \sum_ {j = 1} ^ {n} \left(a _ {i j} ^ {(m)} - a _ {i j}\right) ^ {2}} / n\tag{C2}
$$

It is considered that the smaller the values of $\delta$ and $\sigma ,$ the more effective the modification. Using $\mathrm { C R } ^ { * } { = } 0 . 1$ , the resulting $\boldsymbol { A } ^ { ( m ) } , \boldsymbol { D } ^ { ( m ) } , \boldsymbol { w } ^ { ( m ) } , \lambda _ { \mathrm { m a x } } ( \boldsymbol { A } ^ { ( m ) } ) , \mathrm { C R } ^ { ( m ) } , \boldsymbol { \delta }$ , σ are given in the following.

![](/api/attachments/3RS954WV/fulltext/images/c5ea564d2a53306a419e07338d0fa1bc3884f01c4151d53b8b7a4c285825da0e.jpg)  
Fig. 1. A simple AHP for the selection of a trucking company.

For γ = 0.50, the modified pairwise comparison matrix $\boldsymbol { A } ^ { ( m ) }$ is:

<table><tr><td>1.0000</td><td>4.1027</td><td>1.9599</td><td>8.1951</td><td>5.7867</td><td>5.3817</td><td>0.5045</td><td>0.3375</td></tr><tr><td>0.2437</td><td>1.0000</td><td>0.3101</td><td>4.0415</td><td>2.3693</td><td>2.2430</td><td>0.2472</td><td>0.1518</td></tr><tr><td>0.5102</td><td>3.2244</td><td>1.0000</td><td>7.7000</td><td>4.0131</td><td>4.5138</td><td>3.5638</td><td>0.2954</td></tr><tr><td>0.1220</td><td>0.2474</td><td>0.1299</td><td>1.0000</td><td>0.4190</td><td>0.3292</td><td>0.1239</td><td>0.0888</td></tr><tr><td>0.1728</td><td>0.4221</td><td>0.2492</td><td>2.3866</td><td>1.000</td><td>0.6309</td><td>0.1930</td><td>0.1299</td></tr><tr><td>0.1858</td><td>0.4458</td><td>0.2215</td><td>3.0373</td><td>1.5850</td><td>1.0000</td><td>0.2085</td><td>0.1378</td></tr><tr><td>1.9821</td><td>4.0455</td><td>0.2806</td><td>8.0710</td><td>5.1803</td><td>4.7966</td><td>1.0000</td><td>0.5004</td></tr><tr><td>2.9629</td><td>6.5865</td><td>3.3856</td><td>11.2647</td><td>7.6971</td><td>7.2548</td><td>1.9986</td><td>1.0000</td></tr></table>

The modified deviation matrix $\pmb { D } ^ { \dag ( m ) }$ is:

<table><tr><td>1.0000</td><td>1.2799</td><td>2.1308</td><td>0.8293</td><td>1.0383</td><td>1.1298</td><td>0.4865</td><td>0.6500</td></tr><tr><td>0.7813</td><td>1.0000</td><td>1.0808</td><td>1.3109</td><td>1.3627</td><td>1.5094</td><td>0.7640</td><td>0.9372</td></tr><tr><td>0.4693</td><td>0.9252</td><td>1.0000</td><td>0.7167</td><td>0.6623</td><td>0.8716</td><td>3.1607</td><td>0.5232</td></tr><tr><td>1.2059</td><td>0.7628</td><td>1.3954</td><td>1.0000</td><td>0.7430</td><td>0.6830</td><td>1.1806</td><td>1.6894</td></tr><tr><td>0.9631</td><td>0.7338</td><td>1.5099</td><td>1.3460</td><td>1.0000</td><td>0.7382</td><td>1.0374</td><td>1.3944</td></tr><tr><td>0.8851</td><td>0.6625</td><td>1.1474</td><td>1.4640</td><td>1.3547</td><td>1.0000</td><td>0.9576</td><td>1.2644</td></tr><tr><td>2.0556</td><td>1.3088</td><td>0.3164</td><td>0.8470</td><td>0.9639</td><td>1.0443</td><td>1.0000</td><td>0.9993</td></tr><tr><td>1.5386</td><td>1.0670</td><td>1.9114</td><td>0.5919</td><td>0.7172</td><td>0.7909</td><td>1.0007</td><td>1.0000</td></tr></table>

And

$$
w ^ {(m)} = (0. 1 7 2 7 0. 0 5 5 4 0. 1 8 3 3 0. 0 1 7 7 0. 0 3 1 6 0. 0 3 7 2 0. 1 6 7 2 0. 3 3 4 8) ^ {T}.
$$

$$
\lambda_ {\max} \left(A ^ {(m)}\right) = 8. 5 9 7 8, \mathrm{CR} ^ {(m)} = 0. 0 6 0 6, \delta = 3. 2 6 5, \sigma = 0. 7 8 6 3.
$$

For γ = 0.98, the modified pairwise comparison matrix $A ^ { ( m ) }$ is:

<table><tr><td>1.0000</td><td>4.4412</td><td>2.3682</td><td>7.6743</td><td>5.8559</td><td>5.6079</td><td>0.4201</td><td>0.2968</td></tr><tr><td>0.2252</td><td>1.0000</td><td>0.3210</td><td>4.4224</td><td>2.6175</td><td>2.5392</td><td>0.2268</td><td>0.1486</td></tr><tr><td>0.4223</td><td>3.1151</td><td>1.0000</td><td>6.9149</td><td>3.5351</td><td>4.2774</td><td>4.5105</td><td>0.2487</td></tr><tr><td>0.1303</td><td>0.2261</td><td>0.1446</td><td>1.0000</td><td>0.3805</td><td>0.2927</td><td>0.1313</td><td>0.1030</td></tr><tr><td>0.1708</td><td>0.3820</td><td>0.2829</td><td>2.6278</td><td>1.0000</td><td>0.5722</td><td>0.1960</td><td>0.1444</td></tr><tr><td>0.1783</td><td>0.3938</td><td>0.2338</td><td>3.4166</td><td>1.7478</td><td>1.0000</td><td>0.2055</td><td>0.1494</td></tr><tr><td>2.3804</td><td>4.4099</td><td>0.2217</td><td>7.6136</td><td>5.1012</td><td>4.8661</td><td>1.0000</td><td>0.5004</td></tr><tr><td>3.3689</td><td>6.7293</td><td>4.0215</td><td>9.7130</td><td>6.9235</td><td>6.6949</td><td>1.9984</td><td>1.0000</td></tr></table>

The modified deviation matrix $\pmb { D } ^ { \prime ( m ) }$ =

<table><tr><td>1.0000</td><td>1.4161</td><td>2.5347</td><td>0.7836</td><td>1.0668</td><td>1.1998</td><td>0.4073</td><td>0.5740</td></tr><tr><td>0.7062</td><td>1.0000</td><td>1.0776</td><td>1.4162</td><td>1.4955</td><td>1.7038</td><td>0.6896</td><td>0.9012</td></tr><tr><td>0.3945</td><td>0.9280</td><td>1.0000</td><td>0.6597</td><td>0.6017</td><td>0.8551</td><td>4.0862</td><td>0.4493</td></tr><tr><td>1.2761</td><td>0.7061</td><td>1.5158</td><td>1.0000</td><td>0.6789</td><td>0.6133</td><td>1.2472</td><td>1.9497</td></tr><tr><td>0.9374</td><td>0.6687</td><td>1.6620</td><td>1.4729</td><td>1.0000</td><td>0.6720</td><td>1.0434</td><td>1.5332</td></tr><tr><td>0.8335</td><td>0.5869</td><td>1.1695</td><td>1.6303</td><td>1.4881</td><td>1.0000</td><td>0.9313</td><td>1.3500</td></tr><tr><td>2.4550</td><td>1.4501</td><td>0.2447</td><td>0.8018</td><td>0.9584</td><td>1.0737</td><td>1.0000</td><td>0.9980</td></tr><tr><td>1.7422</td><td>1.1096</td><td>2.2258</td><td>0.5129</td><td>0.6522</td><td>0.7407</td><td>1.0020</td><td>1.0000</td></tr></table>

$$
w ^ {(m)} = \left( \begin{array}{l l l l l l l l} 0. 1 7 2 7 & 0. 0 5 5 1 & 0. 1 8 4 7 & 0. 0 1 7 6 & 0. 0 3 1 5 & 0. 0 3 7 0 & 0. 1 6 7 5 & 0. 3 3 4 0 \end{array} \right) ^ {T}.
$$

$$
\lambda_ {\max} \left(A ^ {(m)}\right) = 8. 9 8 4 4, \mathrm{CR} ^ {(m)} = 0. 0 9 9 7, \delta = 1. 7 1 3, \sigma = 0. 4 4 8.
$$

## 6. Discussion

Tables 1 and 2 summarize the results for these two cases; and, for comparison, we also include the results from Xu and Wei's approach (using identical parameter values respectively).

For both methods, it is quite obvious that the results obtained using 0.98 is significantly better than those using 0.5. That is, there is no reason to use the 0.5 parameter, other than for computational efficiency only. In the case of $\begin{array} { r } { \alpha = \gamma = 0 . 5 . } \end{array}$ , it represents a one-step modification as both methods take one iteration to pass the required Critical Ratio. And in the case of $\alpha { = } \gamma { = } 0 . 9 8$ , it represents a k-step modification where our approach takes quite a number of iterations more, as it makes finer perturbations. While our method, in these two particular cases, is able to achieve either very close values or better values in δ and σ than Xu and Wei, two issues need to be pointed out.

First, Xu and Wei's method makes relatively larger perturbation when using the same parameter value. In both cases, it reaches a Critical Ratio that is lower than ours (that is, it went beyond the requirement of $\mathrm { C R } \leq 0 . 1 )$ , and a lower Critical Ratio typically means higher values in δ and σ. Second and the more important issue, there is no reason that one should compare the two approaches using the same parameter value. It can easily be shown that Xu and Wei is able to achieve the same “smaller perturbation” with a higher value of α. On the other hand, if our method uses that higher value of α, our method will again achieve a finer perturbation and so on.

It is clear that the parameters (α and γ) in the two methods have different meanings, and comparing the two methods by setting $\alpha = \gamma$ can be misleading. However, in both methods, the parameters should be set to a value as close to 1.0 as possible. Our contention is that, when both α and γ approach the limit of 1, our method can retain more original information for the 1- step case as well as the k-step case. For the k-step case, we show that when $k \longrightarrow \infty$ (to converge to the Critical

Table 1  
8×8 example when α=γ=0.5

<table><tr><td></td><td>Iterations needed for CR $^{(m)}$  ≤ 0.1</td><td>CR $^{(m)}$ </td><td>δ</td><td>Σ</td></tr><tr><td>Xu and Wei</td><td>1</td><td>0.03689</td><td>4.339</td><td>0.987</td></tr><tr><td>Our method</td><td>1</td><td>0.06056</td><td>3.265</td><td>0.786</td></tr></table>

Table 2  
8 × 8 example when $\alpha = \gamma = 0 . 9 8$

<table><tr><td></td><td>Iterations needed for CR $^{(m)}$ ≤0.1</td><td>CR $^{(m)}$ </td><td>δ</td><td>Σ</td></tr><tr><td>Xu and Wei</td><td>12</td><td>0.0972</td><td>1.845</td><td>0.434</td></tr><tr><td>Our method</td><td>18</td><td>0.0997</td><td>1.713</td><td>0.448</td></tr></table>

Ratio of zero), our method would retain more original information as well. However, as mentioned in Section 4, the revision process stops at $\mathrm { C R } \leq 0 . 1$ and, as such, our method might not arrive at a superior result.

## 6.1. Convergence behavior

Based on the numerical example, we examine the convergence behavior with respect to different parameter values using our method and Xu and Wei respectively (Figs. 2 and 3). As expected, the higher the parameter value the slower the rate of convergence. And between the two methods, our method is less sensitive. As a future research, it would be interesting if an analytical relationship between γ and the number of iterations required to obtain the required critical ratio can be developed.

From a practical point of view, we wish to report that the computation time is largely insignificant even for a large number of iterations. We implement the algorithm as a program written in Matlab language, run by the software Matlab (R2007a) on a personal computer with

Intel Pentium Core Dual 800 MHz CPU and 1 G RAM. For the 8 × 8 matrix, the computation time for 100 iterations is about 0.056 sec. And since the dimension of an AHP matrix usually does not get very large, γ could be set to a value very close to 1.0 and it still requires only a short computation time.

## 6.2. Extension to sub-bloc and single entry adjustment

Our heuristic approach can be used to see the effects of adjusting a particular sub-bloc or a particular single entry of a pairwise comparison matrix. For these two cases, the convergence of the auto-adaptive process can be proved similarly as in Sections 3 and 4. But it does not guarantee in a converged consistent matrix. In the following, we use the above example problem to investigate how the consistency can be improved by adjusting a sub-bloc or a single entry of the inconsistent matrix. Again, we set the parameter γ to 0.98.

## 6.3. Case 1: adjust the sub-bloc formed by rows and columns (1, 2, 4, 6)

The consistency levels starts from CR = 0.1689 and iteratively converge to 0.1476, which is not an acceptable consistency level. By partially adjusting the pairwise comparison matrix (i.e. sub-blocs), the consistency level will improve but may not satisfy the consistency requirement since the inconsistency may be caused by entries not included in the sub-bloc. Here the decision maker may choose go ahead with adjusting these sub-blocs or choose to seek the potential of adjusting other sub-blocs.

![](/api/attachments/3RS954WV/fulltext/images/7cd06344154242e95004b127b69caca013d5e1190e49117b1d5fa1e4c9fcb518.jpg)  
Fig. 2. Convergence behavior of our method using different γ values.

![](/api/attachments/3RS954WV/fulltext/images/fa9667df7633bf4d306c6055aab6bcbda9615f2c51128ebb9e2ccd5e2a085f14.jpg)  
Fig. 3. Convergence behavior of Xu and Wie using different α values.

## 6.4. Case 2: adjust the single entry $a _ { 4 6 } ( a _ { 6 4 } ) .$

The consistency levels starts from CR = 0.1689 and converges to 0.1633. It is interesting to note that Harker's method [3] also arrived at the same improved consistency ratio of 0.1633. This is true in general. Because when adjusting a single entry by our iterative process, it converges to the new entry $\begin{array} { r } { a _ { i j } = \frac { w _ { i } } { w _ { i } } , } \end{array}$ , which is exactly the new entry determined by Harker's method.

## 7. Conclusions

This paper proposes a heuristic approach to derive a consistency matrix from an inconsistent one. The analytical results show that the proposed method is able to converge to a matrix that preserves more original comparison information than Xu and Wei when the parameter is close to 1.0. However, since the process stops at the requirement that $\mathrm { C R } \leq 0 . 1$ , there is no guarantee that our result will be a superior one. It must be emphasized that such an approach should only be considered as a decision aid, which the decision maker uses as a reference to help modify his own pairwise comparison matrix. A future research issue is on the assessment of modification effectiveness. Currently, two effectiveness criteria are given in Xu and Wei [13]. These two criteria are measures of variation. Alternative measures that can capture the change in preference structure during the modification process could prove to be a more valid way of measuring the effectiveness of the modification. Also, developing an analytical relationship between the Critical Ratio, the number of iterations and the γ value would be a valuable contribution. Lastly, efforts should be made to explore whether other prominent methods of priority determination would satisfy the inequality in Eq. (3.1).

## References

[1] M.C. Carnero, Selection of diagnostic techniques and instrumentation in a predictive maintenance program — a case study, Decision Support Systems vol. 38 (4) (2005) 539–555.

[2] J.S. Finan, W.J. Hurley, The analytic hierarchy process: does adjusting a pairwise comparison matrix to improve the consistency ratio help? Computer and Operations Research 24 (8) (1997) 749–755.

[3] P.T. Harker, Derivatives of the Perron root of a positive reciprocal matrix: with application to the analytic hierarchy process, Applied Mathematics and Computation 22 (1987) 217–232.

[4] R.A. Horn, C.R. Johnson, Matrix Analysis, Cambridge University Press, 1985.

[5] E.F. Lance, W.A. Verdini, A consistency test for AHP decision makers, Decision Sciences 20 (3) (1989) 575–590.

[6] Y. Lee, K. Kozar, Investigating the effect of website quality on ebusiness success: an analytic hierarchy process (AHP) approach, Decision Support Systems vol. 42 (3) (2006) 1383–1401.

[7] C.K. Murphy, Limits on the Analytic Hierarchy Process from its consistency index, European Journal of Operational Research 65 (1993) 138–139.

[8] T.L. Saaty, The Analytic Hierarchy Process, (McGraw–Hill, New York, 1980.

[9] T.L. Saaty, Homogeneity and clustering in AHP ensures the validity of the scale, European Journal of Operational Research 72 (1994) 598–601.

[10] T.L. Saaty, Decision-making with the AHP: why is the principal eigenvector necessary, European Journal of Operational Research 145 (2003) 85–91.

[11] B. Srdjevic, Linking analytic hierarchy process and social choice methods to support group decision-making in water management, Decision Support Systems vol.42 (4) (2007) 2261–2273.

[12] L.G. Vargas, Analysis of sensitivity of reciprocal matrices, Applied Mathematics and Computation vol. 12 (4) (1983) 201–320.

[13] Z. Xu, C. Wei, A consistency improving method in the analytic hierarchy process, European Journal of Operational Research vol. 116 (1999) 443–449.

Dr. Dong Cao is an Associate professor of the department of Industrial Engineering at the University of Québec at Trois-Rivières, Canada. He received his PhD in Operations Research from the University of Louvain, in Belgium.

Dr. Lawrence C. Leung is a Professor of the department of Decision Sciences and Managerial Economics at the Chinese University of Hong Kong. He received his PhD in Industrial Engineering from Virginia Tech, USA.

Dr. Japhet S. Law is a Professor of the department of Decision Sciences and Managerial Economics at the Chinese University of Hong Kong. He received his PhD in Industrial Engineering from the University of Texas (Austin), USA.
