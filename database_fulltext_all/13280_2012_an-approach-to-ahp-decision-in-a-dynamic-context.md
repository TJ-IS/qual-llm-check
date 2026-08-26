---
otero_id: 13280
otero_key: "V2S6Q6UY"
title: "An approach to AHP decision in a dynamic context"
authors: "J. Benítez; X. Delgado-Galván; J. Izquierdo; R. Pérez-García"
year: "2012"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2012.04.015"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# An approach to AHP decision in a dynamic context

J. Benítez, X. Delgado-Galván, J. Izquierdo ⁎, R. Pérez-García

Instituto de Matemática Multidisciplinar, Universitat Politècnica de València, Camino de Vera s/n, 46022 Valencia, Spain

## a r t i c l e i n f o

Article history: Received 30 August 2011 Received in revised form 31 March 2012 Accepted 29 April 2012 Available online 8 May 2012

Keywords: Analytic hierarchy process Dynamic decision-making Leakage control Water supply systems

## a b s t r a c t

AHP (analytic hierarchy process) is used to construct coherent aggregate results from preference data provided by decision makers. Pairwise comparison, used by AHP, shares a common weakness with other input formats used to represent user preferences, namely, that the input mode is static. In other words, users must provide all the preference data at the same time, and the criteria must be completely de<sup>fi</sup>ned from the start. To overcome this weakness, we propose a framework that allows users to provide partial and/or incomplete preference data at multiple times. Since this is a complicated issue, we speci<sup>fi</sup>cally focus on a particular aspect as a <sup>fi</sup>rst attempt within this framework. For that reason, we re-examine a mechanism to achieve consistency in AHP, i.e. a linearization process, which provides consistency when adding a new element to the decision process or when withdrawing an obsolete criterion under the dynamic input mode assumption. An algorithm is developed to determine the new priority vector from the users' new input. Finally, we apply the new process to a problem of interest in the water <sup>fi</sup>eld, speci<sup>fi</sup>cally, the adoption of a suitable leak control policy in urban water supply.

© 2012 Elsevier B.V. All rights reserved.

## 1. Introduction

AHP (analytic hierarchy process) is a multicriteria decision process [23] that involves aggregating various comparisons to obtain a priority vector that is representative of coherent results. In other words, AHP generates consolidated priorities about a number of alternatives that represent the will, likes, or decisions revealed by the preference data provided by one or more actors, or groups of actors, involved in the decision-making process. Achieving consistency in AHP has become an important issue [11,14,18,21,22] and different methods have been proposed [2,3,5–7,9,12,15,17,24,29].

AHP uses a speci<sup>fi</sup>c input format for decision makers to express their preferences regarding multiple criteria and alternatives, namely, pairwise comparisons. This format may be not perfect — yet it expresses user preferences reasonably well in many practical situations. After all the preference data has been collected, an algorithm is applied to generate consistent consolidated results.

However, a limitation of pair-wise comparisons is that before applying the decision model the experts must provide judgment data representing their preference with respect to all the elements involved. This kind of input is impossible in many practical situations. Consider, for example, the following two scenarios. Firstly, let us suppose that not all the elements for comparison are known or evident from the start. In leakage control, for example, only economic aspects have so far been widely considered. Nevertheless, environmental aspects have started to be considered as important, and even more recently, social elements have also started to play important roles in decision making on leakage control policies. A second scenario is when the consulted actors are unfamiliar with the effects of various items. As a result, it is dif-<sup>fi</sup>cult to collect complete preference information from decision makers at one time. It would be reasonable to allow decision makers to express their preferences at multiple times at their own convenience. In the meanwhile, partial results based on partial preference data could be generated from the data collected at multiple times — and this data could eventually be consolidated when the information is complete.

To consider the above mentioned scenarios, the input mode of the traditional AHP needs to be extended from a static mode to a dynamic mode. The dynamic mode involves the dimension of time. In other words, it will not be compulsory for users to provide input preference data at one point in time. A user will be able to input his/her preferences at multiples times. The user only needs to express his/her preference each time for a subset of elements, rather than the complete set. A change from static to dynamic mode will probably have many repercussions in future studies. It is impossible to address all of these issues at this time. Therefore, in this study we initiate a new approach and focus on a speci<sup>fi</sup>c sub-problem. In this paper, we restrict ourselves to the case where a new criterion is added to the pool of previously considered criteria. This case can obviously be extended to the case of adding more than one criterion. The withdrawal of an obsolete criterion is readily obtained as a corollary.

The remainder of this paper is organized as follows. First, a short review of the linearization process [5] to achieve consistency is presented.

In the methodology section, new results are presented that enable an ef<sup>fi</sup>cient calculation of the new consistent matrix and its corresponding vector of priority after introducing a new criterion or withdrawing an obsolete criterion. Finally, the proposed methodology is applied to a real-world case in water leakage management, and conclusions are presented to close the paper.

## 2. Related work

In this section, we <sup>fi</sup>rst review the pertinent literature on AHP and related work for the proposed methodology. We then provide a summary of our recent work and propose a method to achieve consistency for a non-consistent matrix based on a linearization procedure [5]. We have also extended this process to the case where a speci<sup>fi</sup>c judgment should be changed [4]. In this paper we provide a new extension to consider the case in which a new decision element is introduced.

## 2.1. Some basics about consistency

Let us <sup>fi</sup>rst recall the main facts about consistent matrices.

Let us consider an n×n real matrix A. A is positive if $a _ { i j } > 0$ for every i, j; A is homogeneous if $a _ { i i } = 1$ for every $i ; A$ is reciprocal if $a _ { i j } = 1 / a _ { j i } ,$ , for every i, j. These are the typical properties of comparison matrices generally found in AHP. In addition, A is consistent if $\dot { a } _ { i k } = a _ { i j } a _ { j k }$ for every $i , j , k .$ . Among the different characterizations of consistent matrices, we recall the following which makes use of the mapping: J, associating to a positive matrix $A = ( a _ { i j } )$ the matrix whose entry $( i , j )$ is $1 / a _ { i j } .$ If X is any matrix, then $X ^ { \mathrm { { T } } }$ denotes the transpose of X. Throughout this paper, it is assumed that the vectors of IR<sup>n</sup> are column vectors.

The following result was established in a slightly different manner in [5].

Theorem 1. (Theorem 2.1, (ii) of [5]). A positive matrix A is consistent if and only if there is a vector x in $\mathbb { R } ^ { \mathrm { n } }$ such that $A { = } x J ( { \mathbf { x } } ) ^ { \mathrm { T } }$

For a consistent matrix, the leading eigenvalue and the principal (Perron) eigenvector of a comparison matrix provide information to deal with complex decisions, the normalized Perron eigenvector giving the sought priority vector [22,23]. In the general case, however, A is not consistent. The hypothesis that the estimates of these values are small perturbations of the “right” values guarantees a small perturbation of the eigenvalues (see, e.g., [26]). For non-consistent matrices, the problem to solve is the eigenvalue problem $A \mathbf { w } { = } \lambda _ { \operatorname* { m a x } } \mathbf { w }$ , where $\lambda _ { \mathrm { m a x } }$ is the unique largest eigenvalue of A that gives the Perron eigenvector as an estimate of the priority vector. As a measurement of inconsistency, Saaty proposed using the consistency index $C I = ( \lambda _ { \operatorname* { m a x } } - n ) / ( n - 1 )$ and the consistency ratio $C R = C I / R I$ , where RI is the so-called average consistency index [23]. If $C R { < } 0 . 1$ , the estimate is accepted; otherwise, a new comparison matrix is solicited until CRb0.1.

## 2.2. Linearization process

From now on, $M _ { n , m }$ will denote the set of n×m real matrices, $M _ { n , m } ^ { + }$ the set of n×m positive matrices, and $t r ( A )$ the trace of the matrix $A \in M _ { n , n } .$ It is well known that if we de<sup>fi</sup>ne $\langle A , B \rangle = t r ( A ^ { \mathrm { T } } B )$ for $A , B \in M _ { n , m } ,$ then $\langle \cdot , \cdot \rangle$ is an inner product. The derived norm from this inner product is customarily termed the Frobenius norm, and we denote it by ‖⋅‖ , i.e., $| | A | | _ { \mathrm { F } } ^ { 2 } { = } t r ( A ^ { \mathrm { T } } A )$ . We de<sup>fi</sup>ne the map $L \colon M _ { n , m } ^ { + } { \to } M _ { n , m }$ associating it with a positive matrix $A = ( a _ { i j } )$ whose $( i , j )$ entry is log $( a _ { i j } )$ . Its inverse mapping $E \colon M _ { n , \ m } \to M _ { n , \ m } ^ { + }$ associates a matrix $B = ( b _ { i j } )$ with the matrix whose entry (i, j) is exp $( b _ { i j } )$

The following map d: $M _ { n , m } ^ { + } { \times } M _ { n , m } ^ { + } { \ - } $ IR de<sup>fi</sup>ned by $\mathsf { d } ( A , B ) = \| L ( A ) -$ L(B)‖ is easily proven to be a distance. We propose using this distance in $M _ { n , m } ^ { + }$ instead of the distance derived from the Frobenius norm. To motivate this proposal, note that we intend to solve approximation problems in $M _ { n , \astrosun } ^ { + }$ and not in $M _ { n , \ m } ;$ thus it is more natural to have a distance de<sup>fi</sup>ned in $M _ { n , m } ^ { + }$ than a distance de<sup>fi</sup>ned in a larger set. Furthermore, let us consider the following example,

$$
A _ {1} = \left[ \begin{array}{c c} 1 & 1 \\ 1 & 1 \end{array} \right], \quad B _ {1} = \left[ \begin{array}{c c} 1 & 2 \\ 1 / 2 & 1 \end{array} \right], \quad A _ {2} = \left[ \begin{array}{c c} 1 & 8 \\ 1 / 8 & 1 \end{array} \right], \quad B _ {2} = \left[ \begin{array}{c c} 1 & 9 \\ 1 / 9 & 1 \end{array} \right].
$$

We have $| | A _ { 1 } - B _ { 1 } | | _ { \mathrm { F } } \simeq 1 . 1 1 8$ and $\| A _ { 2 } - B _ { 2 } \| _ { \mathrm { F } } { \simeq } 1 . 0 0 1 ;$ which give the impression that the gap between $A _ { 1 }$ and $B _ { 1 }$ is similar to the gap between $A _ { 2 }$ and $B _ { 2 } .$ . This is not very intuitive because matrix $A _ { 1 }$ re<sup>fl</sup>ects the fact that the two criteria are equivalent, while $B _ { 1 }$ re<sup>fl</sup>ects that the second criterion is twice as important as the second criterion. Let us observe that the importance of the criteria in $A _ { 2 }$ and $B _ { 2 }$ are very close. Thus, in an intuitive point of view, the distance between $A _ { 1 }$ and $B _ { 1 }$ must be much greater than the distance between $A _ { 2 }$ and $B _ { 2 } .$ . Numerically, we have $\operatorname { d } ( A _ { 1 } , B _ { 1 } ) \simeq 0 . 9 8 0 3$ and $\mathrm { d } ( A _ { 2 } , B _ { 2 } ) \simeq 0 . 1 6 6 6$

The linearization process derived in [5] states that the closest consistent matrix to an n×n comparison matrix A is given by the orthogonal projection of $L ( A )$ onto

$$
\mathcal {L} _ {n} = \left\{L (A): A \in M _ {n, n} ^ {+}, A \text {   is   consistent } \right\}.\tag{1}
$$

Obviously, $. X { \in } { \mathcal { L } } _ { n }$ if and only if $E ( X )$ is consistent. This subset ${ \mathcal { L } } _ { n }$ is a <sup>L</sup>linear subspace of $M _ { n , \ n }$ whose dimension is $n - 1$ <sup>L</sup>. The orthogonal projection from $M _ { n , \ n } \ t o \ \mathcal { L } _ { n }$ will be denoted by $p _ { n } : M _ { n , n } {  } \mathcal { L } _ { n }$ and is given by a suitable Fourier expansion. In this expansion, use is made of the map given by

$$
\phi_ {n} (\mathbf {v}) = \mathbf {v 1} _ {n} ^ {\mathrm{T}} - 1 _ {n} \mathbf {v} ^ {\mathrm{T}}, \quad \mathbf {v} \in \mathrm{IR} ^ {n},\tag{2}
$$

where the symbol $1 _ { n }$ denotes the vector of $\mathbb { R } ^ { \mathrm { n } }$ having all its coordinates equal to $1 \colon 1 _ { n } = [ 1 \cdots 1 ] ^ { \mathrm { T } } { \in } \mathrm { I R } ^ { \mathrm { n } }$ (this vector will play an important role in the sequel). We also use the standard inner product in $\displaystyle { \mathrm { I R } } ^ { \mathrm { n } } ( \mathrm { i } . \mathrm { e } .$ $\langle \mathbf { u } , \mathbf { v } \rangle = \mathbf { u } ^ { \mathrm { T } } \mathbf { v } )$ ) and the Euclidean norm in $\mathsf { I R } ^ { \mathrm { n } } \left( \mathrm { i . e . , } \| \mathbf { \bar { u } } \| _ { 2 } = ( \mathbf { u } ^ { \mathrm { T } } \mathbf { u } ) ^ { 1 / 2 } \right)$

For the sake of clarity, we summarize the linearization theorem as follows:

Theorem 2. The subset ${ \mathcal { L } } _ { n }$ is a linear subspace of $M _ { n , n }$ satisfying ${ \mathcal { L } } _ { n } =$ Im $\phi _ { n }$ and dim $\begin{array} { r } { | \mathcal { L } _ { n } = n - 1 } \end{array}$ <sup>L</sup>. Furthermore, let $A \in M _ { n , \cdot } ^ { + }$ <sub>n</sub>.

(i) There exists a unique consistent matrix $Y \in { \cal M } _ { n , { \mathrm { ~ } } n } ^ { + }$ such that

$$
\mathrm{d} (A, Y) \leq \mathrm{d} \left(A, Y ^ {\prime}\right) \forall Y ^ {\prime} \text {   consistent   in   } M _ {n, n} ^ {+}.
$$

This matrix Y is given by $Y = E ( p _ { n } ( L ( A ) ) )$

(ii) If $\left\{ \mathbf { y } _ { 1 } , . . . , \mathbf { y } _ { n - 1 } \right\}$ is an orthogonal basis of the orthogonal complement to span{1 }, then $\left\{ \phi _ { n } ( \mathbf { y } _ { 1 } ) , . . . , \phi _ { n } ( \mathbf { y } _ { n - 1 } ) \right\}$ is an orthogonal basis in ${ \mathcal { L } } _ { n }$

$$
\| \phi_ {n} (\mathbf {y} _ {i}) \| _ {\mathrm{F}} ^ {2} = 2 n \| \mathbf {y} _ {i} \| _ {2} ^ {2}, \forall i = 1, \dots , n - 1,
$$

and the following matrix

$$
\frac {1}{2 n} \sum_ {i = 1} ^ {n - 1} \frac {t r (L (A) ^ {\mathrm{T}} \phi_ {n} (\mathbf {y} _ {i}))}{| | \mathbf {y} _ {i} | | _ {2} ^ {2}} \phi_ {n} (\mathbf {y} _ {i})
$$

is the orthogonal projection of $L ( A )$ onto ${ \mathcal { L } } _ { n } .$

A simple computation shows that from Eq. (2), there is $[ \phi _ { n } (  { \mathbf { v } } ) ] ^ { \mathrm { T } } =$ $- \phi _ { n } ( \mathbf { v } )$ for any $\mathbf { v } \in { \mathrm { I R } } ^ { \mathrm { n } }$ , which, in view of Theorem $^ { 2 , }$ , shows that any matrix in ${ \mathcal { L } } _ { n }$ is skew-Hermitian, in particular, $p _ { n } ( X )$ is skew-Hermitian for any $X \in { \cal M } _ { n } ,$ <sub>n</sub>.

The following result enables the discovery of an orthogonal basis of span{1 } without any computations.

Theorem 3. (Theorem 2.6, [5]). Let $( Y _ { n } ) _ { n } ^ { \infty } = 2$ be the sequence of matrices de<sup>fi</sup>ned as follows:

$$
Y _ {2} = \left[ \begin{array}{c} 1 \\ - 1 \end{array} \right], \qquad Y _ {n + 1} = \left[ \begin{array}{c c} Y _ {n} & 1 _ {n} \\ 0 & - n \end{array} \right],   n \geq 2.
$$

Then for every $n \geq 2 ,$ the columns of $Y _ { n }$ are orthogonal and belong to (span{ $1 \} ) ^ { \perp }$ . Furthermore, $\mathrm { i f } \ \mathbf { y } _ { 1 , \ n } , . . . , \mathbf { y } _ { n - 1 , }$ are the columns of $Y _ { n } ,$ then $\| \mathbf { y } _ { k , n } \| _ { 2 } ^ { 2 } = k + k ^ { 2 }$ for $1 \leq k \leq n - 1$

## 3. Methodology

In this section we develop ef<sup>fi</sup>cient calculation methods of the new consistent matrix and its corresponding vector of priority — either after introducing a new decision element or after withdrawing an obsolete element.

## 3.1. Adding a new criterion

Let us consider the following problem: suppose that we have a reciprocal matrix $A \in M _ { n , \textit { n } } ^ { + }$ and by means of Theorem 2, we have at our disposal the nearest consistent matrix $Y _ { A } .$ We then add an extra judgment corresponding to a new decision element, thus obtaining a new reciprocal matrix B as follows

$$
B = \left[ \begin{array}{c c} A & \mathbf {v} \\ J \Big (\mathbf {v} ^ {\mathrm{T}} \Big) & 1 \end{array} \right] \in M _ {n + 1, n + 1} ^ {+},\tag{3}
$$

where $\begin{array} { r } { \mathbf { v } \in \mathrm { I R } ^ { \mathrm { n } } , } \end{array}$ all of whose components are positive, and represent the preferences of this new decision element when compared pairwise with the others. Obviously, the reciprocity of A leads to the reciprocity of B. The questions are now: how can we <sup>fi</sup>nd the nearest consistent matrix to B without again using Theorem 2? Can we take advantage of the computations made when $Y _ { A }$ was computed?

Indeed, we shall later see that Theorem 5 will provide a positive answer to those questions. Before presenting the proof of this theorem, we need some notations and previous results. Firstly, let us recall the basic properties of the trace, which are collected immediately and used throughout the proof of Theorem 5.

i) The trace is linear, ${ \mathrm { i . e . , i f } } X , Y { \in } M _ { n , r }$ and $\alpha , \beta \in \operatorname { I R } ,$ then $t r ( \alpha X +$ $\beta Y ) = \alpha t r ( X ) + \beta t r ( Y ) .$

ii) For any $X \in { \cal M } _ { n , n } ,$ one has $t r ( X ) = t r ( X ^ { \mathrm { T } } )$

iii) I $\mathsf { X } \in M _ { n , m }$ and $Y \in { \cal M } _ { m , n } ,$ then $t r ( X Y ) = t r ( Y X )$ . Observe that it is not necessary that $m = n$

Let us remark that if $\mathbf { w } \in \mathrm { I R } ^ { \mathrm { n } }$ , then ${ \mathbf w } ^ { \mathrm { T } } \boldsymbol { 1 } _ { n } / n$ is the arithmetic mean of the coordinates of w. Thus, it is natural to define

$$
\text { mean }: \mathrm{IR} ^ {n} \rightarrow \mathrm{IR}, \quad \text { mean } (\mathbf {w}) = \frac {\mathbf {w} ^ {\mathrm{T}} 1 _ {n}}{n}.\tag{4}
$$

It is also clear that ${ \bf w } - m e a n ( { \bf w } ) \boldsymbol { 1 } _ { r }$ is the vector w ‘displaced to its arithmetic mean’. We shall denote

$$
\operatorname{centr}: \mathrm{IR} ^ {n} \rightarrow \mathrm{IR} ^ {n}, \quad \operatorname{centr} (\mathbf {w}) = \mathbf {w} - \operatorname{mean} (\mathbf {w}) 1 _ {n}.\tag{5}
$$

We shall not use the subscript n for the mappings mean and centr (contrary to the mapping $\phi _ { n }$ de<sup>fi</sup>ned in Eq. (2)) because it is unnecessary. Some basic and useful properties for these mappings are collected in the next lemma.

Lemma 1. Let the mappings $\phi _ { n } ,$ mean, and centr be de<sup>fi</sup>ned in Eqs. (2), (4), and (5), respectively. Then

i) $\phi _ { n } ,$ mean, and centr are linear mappings.

ii) $m e a n [ c e n t r ( \mathbf { w } ) ] { = } 0$ for all w ∈ IR<sup>n</sup>.

iii) $\phi _ { n } [ c e n t r ( \mathbf { w } ) ] { = } \phi _ { n } ( \mathbf { w } )$ for all $\mathbf { w } \in \mathrm { I R } ^ { \mathrm { n } } ,$ iv) $( n + 1 ) m e a n ( \mathbf { w } ) 1 _ { n } + c e n t r ( \mathbf { w } ) = ( 1 _ { n } 1 _ { n } ^ { \operatorname { T } } + I _ { n } ) \mathbf { w }$ for all $\mathbf { x } \in \mathrm { I R } ^ { \mathrm { n } }$ where $I _ { n }$ denotes the identity matrix of order n.

Proof. items i) and ii) are trivial to be proven. The proofs of iii) and iv) follow from the following computations: for $\mathbf { w } \in \mathrm { I R } ^ { \mathrm { n } }$ , one has

$$
\begin{array}{c} \phi_ {n} [ c e n t r (\mathbf {w}) ] = [ \mathbf {w} - m e a n (\mathbf {w}) 1 _ {n} ] 1 _ {n} ^ {\mathrm{T}} - 1 _ {n} [ \mathbf {w} - m e a n (\mathbf {w}) 1 _ {n} ] ^ {\mathrm{T}} \\ = \mathbf {w} 1 _ {n} ^ {\mathrm{T}} - 1 _ {n} \mathbf {w} ^ {\mathrm{T}} = \phi_ {n} (\mathbf {w}). \end{array}
$$

and

$$
\begin{array}{l} (n + 1) \text {mean} (\mathbf {w}) 1 _ {n} + \text {centr} (\mathbf {w}) = (n + 1) \text {mean} (\mathbf {w}) 1 _ {n} + \mathbf {w} - \text {mean} (\mathbf {w}) 1 _ {n} \\ \qquad = n \text {mean} (\mathbf {w}) 1 _ {n} + \mathbf {w} \\ \qquad = \left(1 _ {n} ^ {\mathrm{T}} \mathbf {w}\right) 1 _ {n} + \mathbf {w} \\ \qquad = 1 _ {n} \left(1 _ {n} ^ {\mathrm{T}} \mathbf {w}\right) + \mathbf {w} \\ \qquad = \left(1 _ {n} 1 _ {n} ^ {\mathrm{T}} + I _ {n}\right) \mathbf {w}. \end{array}
$$

Furthermore, we shall use the following result (which can be found in any standard textbook of linear algebra, see e.g., [16, Section 5.4]):

Theorem 4. $\operatorname { I f } \mathbf { x } _ { 1 } , . . . , \mathbf { x } _ { n }$ is an orthogonal basis of IR<sup>n</sup>, then any $\mathbf { u } \in \mathrm { I R } ^ { \mathrm { n } }$ can be written as

$$
\mathbf {u} = \sum_ {j = 1} ^ {n} \frac {\langle \mathbf {u} , \mathbf {x} _ {j} \rangle}{| | \mathbf {x} _ {j} | | _ {2} ^ {2}} \mathbf {x} _ {j}.
$$

Now, we shall state and prove the main result of this section.

Theorem 5. Let $A \in M _ { n , n } ^ { + } .$ . If B is de<sup>fi</sup>ned as in Eq. (3), then $p _ { n + 1 } ( L ( B ) )$ is the following block matrix:

$$
\left[ \begin{array}{c c} n p _ {n} (L (A)) + \phi_ {n} [ L (\mathbf {v}) ] & \left(1 _ {n} 1 _ {n} ^ {\mathrm{T}} + I _ {n}\right) L (\mathbf {v}) + p _ {n} (L (A)) 1 _ {n} \\ \underset {*} {n + 1} & \underset {0} {n + 1} \end{array} \right],\tag{6}
$$

being the block denoted with ‘\*’ determined, since $p _ { n } ( L ( B ) )$ is skew-Hermitian.

Proof. Obviously, one has

$$
L (B) = \left[ \begin{array}{c c} L (A) & L (\mathbf {v}) \\ - L (\mathbf {v}) ^ {\mathrm{T}} & 0 \end{array} \right].\tag{7}
$$

Moreover, if $\left\{ \mathbf { y } _ { 1 } , . . . , \mathbf { y } _ { n - 1 } \right\}$ is the orthogonal basis of $( \mathsf { s p a n } \{ 1 _ { n } \} ) ^ { \perp }$ obtained in Theorem 3, the following vectors of $\boldsymbol { \mathrm { I R } } ^ { n + 1 }$

$$
\mathbf {z} _ {1} = \left[ \begin{array}{c} \mathbf {y} _ {1} \\ 0 \end{array} \right], \quad \mathbf {z} _ {2} = \left[ \begin{array}{c} \mathbf {y} _ {2} \\ 0 \end{array} \right], \ldots , \quad \mathbf {z} _ {n - 1} = \left[ \begin{array}{c} \mathbf {y} _ {n - 1} \\ 0 \end{array} \right], \quad \mathbf {z} _ {n} = \left[ \begin{array}{c} 1 _ {n} \\ - n \end{array} \right]\tag{8}
$$

form an orthogonal basis of $( { \mathsf { s p a n } } \{ 1 _ { n + 1 } \} ) ^ { - }$ <sup>⊥</sup>. In view of Theorem 2, we have to relate

$$
p _ {n} (L (A)) = \frac {1}{2 n} \sum_ {i = 1} ^ {n - 1} \frac {\operatorname{tr} \left[ L (A) ^ {\mathrm{T}} \phi_ {n} (\mathbf {y} _ {i}) \right]}{\| \mathbf {y} _ {i} \| _ {2} ^ {2}} \phi_ {n} (\mathbf {y} _ {i})\tag{9}
$$

with

$$
p _ {n + 1} (L (B)) = \frac {1}{2 (n + 1)} \sum_ {i = 1} ^ {n} \frac {\operatorname{tr} \left[ L (B) ^ {\mathrm{T}} \phi_ {n + 1} (\mathbf {z} _ {i}) \right]}{\| \mathbf {z} _ {i} \| _ {2} ^ {2}} \phi_ {n + 1} (\mathbf {z} _ {i}).\tag{10}
$$

To this purpose, let us start splitting the set of indexes on the righthand side of Eq. (10) into two subsets, namely $\{ 1 , . . . , n - 1 \}$ } and {n}.

Pick any $i { \in } \{ 1 , . . . , n { - } 1 \}$ . Since

$$
\begin{array}{r l} \phi_ {n + 1} (\mathbf {z} _ {i}) & = \mathbf {z} _ {i} \mathbf {1} _ {n + 1} ^ {\mathrm{T}} - \mathbf {1} _ {n + 1} \mathbf {z} _ {i} ^ {\mathrm{T}} = \left[ \begin{array}{c} \mathbf {y} _ {i} \\ 0 \end{array} \right] \left[ \begin{array}{c c} 1 _ {n} ^ {\mathrm{T}} & 1 \end{array} \right] - \left[ \begin{array}{c} 1 _ {n} \\ 1 \end{array} \right] \left[ \begin{array}{c c} \mathbf {y} _ {i} ^ {\mathrm{T}} & 0 \end{array} \right] \\ & = \left[ \begin{array}{c c} \phi_ {n} (\mathbf {y} _ {i}) & \mathbf {y} _ {i} \\ - \mathbf {y} _ {i} ^ {\mathrm{T}} & 0 \end{array} \right] \end{array}\tag{11}
$$

and having in mind Eq. (7) we have

$$
\begin{array}{c} L (B) ^ {\mathrm{T}} \phi_ {n + 1} (\mathbf {z} _ {i}) = \left[ \begin{array}{c c} L (A) ^ {\mathrm{T}} & - L (\mathbf {v}) \\ L (\mathbf {v}) ^ {\mathrm{T}} & 0 \end{array} \right] \left[ \begin{array}{c c} \phi_ {n} (\mathbf {y} _ {i}) & \mathbf {y} _ {i} \\ - \mathbf {y} _ {i} ^ {\mathrm{T}} & 0 \end{array} \right] \\ = \left[ \begin{array}{c c} L (A) ^ {\mathrm{T}} \phi_ {n} (\mathbf {y} _ {i}) + L (\mathbf {v}) \mathbf {y} _ {i} ^ {\mathrm{T}} & * \\ * & L (\mathbf {v}) ^ {\mathrm{T}} \mathbf {y} _ {i} \end{array} \right]. \end{array}
$$

To simplify the right-hand of Eq. (10), we must simplify $t r ( L ( B ) ^ { \mathrm { T } } \phi _ { n + 1 } ( \mathbf { z } _ { i } ) )$ , thus, there is no need to calculate the entries off the main diagonal of $L ( B ) ^ { \mathrm { T } } \phi _ { n + 1 } ( \mathbf { z } _ { i } )$ . Therefore,

$$
\operatorname{tr} \left[ L (B) ^ {\mathrm{T}} \phi_ {n + 1} (\mathbf {z} _ {i}) \right] = \operatorname{tr} \left[ L (A) ^ {\mathrm{T}} \phi_ {n} (\mathbf {y} _ {i}) \right] + 2 L (\mathbf {v}) ^ {\mathrm{T}} \mathbf {y} _ {i} \quad \text {   for   } 1 \leq i \leq n - 1. \tag {12}
$$

Furthermore, if $1 \leq i \leq n - 1$ , then Eq. (8) leads to $| | \mathbf { y } _ { i } | | _ { 2 } = | | \mathbf { z } _ { i } | | _ { 2 }$ Now, we simplify the last summand on the right-hand side of Eq. (10): Since

$$
\begin{array}{l} \phi_ {n + 1} (\mathbf {z} _ {n}) = \mathbf {z} _ {n} \mathbf {1} _ {n + 1} ^ {\mathrm{T}} - \mathbf {1} _ {n + 1} \mathbf {z} _ {n} ^ {\mathrm{T}} = \\ \qquad = \left[ \begin{array}{c c} \mathbf {1} _ {n} \\ - n \end{array} \right] \left[ \begin{array}{c c} \mathbf {1} _ {n} ^ {\mathrm{T}} & 1 \end{array} \right] - \left[ \begin{array}{c} \mathbf {1} _ {n} \\ 1 \end{array} \right] \left[ \begin{array}{c c} \mathbf {1} _ {n} ^ {\mathrm{T}} & - n \end{array} \right] = \left[ \begin{array}{c c} 0 & (1 + n) \mathbf {1} _ {n} \\ - (1 + n) \mathbf {1} _ {n} ^ {\mathrm{T}} & 0 \end{array} \right], \end{array}\tag{13}
$$

by using Eq. (7), one has (again, we mark with an asterisk the entries that we are not interested in)

$$
\begin{array}{c} L (B) ^ {\mathrm{T}} \phi_ {n + 1} (\mathbf {z} _ {n}) = \left[ \begin{array}{c c} L (A) ^ {\mathrm{T}} & - L (\mathbf {v}) \\ L (\mathbf {v}) ^ {\mathrm{T}} & 0 \end{array} \right] \left[ \begin{array}{c c} 0 & (1 + n) 1 _ {n} \\ - (1 + n) 1 _ {n} ^ {\mathrm{T}} & 0 \end{array} \right] \\ = \left[ \begin{array}{c c} (1 + n) L (\mathbf {v}) 1 _ {n} ^ {\mathrm{T}} & * \\ * & (1 + n) L (\mathbf {v}) ^ {\mathrm{T}} 1 _ {n} \end{array} \right]. \end{array}
$$

Therefore,

$$
\operatorname{tr} \left[ L (B) ^ {\mathrm{T}} \phi_ {n + 1} (\mathbf {z} _ {n}) \right] = 2 (n + 1) L (\mathbf {v}) ^ {\mathrm{T}} 1 _ {n}.\tag{14}
$$

Furthermore, Eq. (8) leads to $| | \mathbf { z } _ { n } | | ^ { 2 } = n ( 1 + n )$

Now, we express $p _ { n + 1 } ( L ( B ) )$ in terms of $p _ { n } ( L ( A ) )$ . To this end, we use Eqs. (10), (11), (12), (13), and (14), $| | \mathbf { z } _ { n } | | ^ { 2 } = n ( 1 + n )$ , and $| | \mathbf { z } _ { i } | | ^ { 2 } { = } | | \mathbf { y } _ { i } | |$ for 1 i n 1.

$$
\begin{array}{l} p _ {n + 1} (L (B)) = \frac {1}{2 (n + 1)} \sum_ {i = 1} ^ {n} \frac {t r \left[ L (B) ^ {\mathrm{T}} \phi_ {n + 1} (\mathbf {z} _ {i}) \right]}{| | \mathbf {z} _ {i} | | _ {2} ^ {2}} \phi_ {n + 1} (\mathbf {z} _ {i}) \\ = \frac {1}{2 (n + 1)} \Bigg (\frac {t r \left[ L (B) ^ {\mathrm{T}} \phi_ {n + 1} (\mathbf {z} _ {n}) \right]}{| | \mathbf {z} _ {n} | | _ {2} ^ {2}} \phi_ {n + 1} (\mathbf {z} _ {n}) + \\ \quad + \sum_ {i = 1} ^ {n - 1} \frac {t r \left[ L (B) ^ {\mathrm{T}} \phi_ {n + 1} (\mathbf {z} _ {i}) \right]}{| | \mathbf {z} _ {i} | | _ {2} ^ {2}} \phi_ {n + 1} (\mathbf {z} _ {i}) \Bigg) = \frac {L (\mathbf {v}) ^ {\mathrm{T}} 1 _ {n}}{n} \left[ \begin{array}{c c} 0 & 1 _ {n} \\ - 1 _ {n} ^ {\mathrm{T}} & 0 \end{array} \right] + \\ \quad + \frac {1}{2 (n + 1)} \sum_ {i = 1} ^ {n - 1} \frac {t r \left[ L (A) ^ {\mathrm{T}} \phi_ {n} (\mathbf {y} _ {i}) \right] + 2 L (\mathbf {v}) ^ {\mathrm{T}} \mathbf {y} _ {i}}{| | \mathbf {y} _ {i} | | _ {2} ^ {2}} \left[ \begin{array}{c c} \phi_ {n} (\mathbf {y} _ {i}) & \mathbf {y} _ {i} \\ - \mathbf {y} _ {i} ^ {\mathrm{T}} & 0 \end{array} \right]. \end{array}\tag{15}
$$

By focusing our attention to the “north-west” block of $p _ { n + 1 } ( L ( B ) )$ in Eq. (15) and using Eq. (9), one has

$$
\begin{array}{l} \frac {1}{2 (n + 1)} \sum_ {i = 1} ^ {n - 1} \frac {t r \left[ L (A) ^ {\mathrm{T}} \phi_ {n} (\mathbf {y} _ {i}) \right] + 2 L (\mathbf {v}) ^ {\mathrm{T}} \mathbf {y} _ {i}}{| | \mathbf {y} _ {i} | | _ {2} ^ {2}} \phi_ {n} (\mathbf {y} _ {i}) \\ = \frac {1}{2 (n + 1)} \Bigg (2 n p _ {n} (L (A)) + 2 \sum_ {i = 1} ^ {n - 1} \frac {L (\mathbf {v}) ^ {\mathrm{T}} \mathbf {y} _ {i}}{| | \mathbf {y} _ {i} | | _ {2} ^ {2}} \phi_ {n} (\mathbf {y} _ {i}) \Bigg) \\ = \frac {n}{n + 1} p _ {n} (L (A)) + \frac {1}{n + 1} \sum_ {i = 1} ^ {n - 1} \frac {L (\mathbf {v}) ^ {\mathrm{T}} \mathbf {y} _ {i}}{| | \mathbf {y} _ {i} | | _ {2} ^ {2}} \phi_ {n} (\mathbf {y} _ {i}). \end{array}\tag{16}
$$

Since $\left\{ 1 _ { n } , \mathbf { y } _ { 1 } , . . . , \mathbf { y } _ { n - 1 } \right\}$ is an orthogonal basis of $\boldsymbol { \mathrm { I R } } ^ { n }$ , by applying Theorem 4, one has

$$
L (\mathbf {v}) = \sum_ {i = 1} ^ {n - 1} \frac {L (\mathbf {v}) ^ {\mathrm{T}} \mathbf {y} _ {i}}{| | \mathbf {y} _ {i} | | _ {2} ^ {2}} \mathbf {y} _ {i} + \frac {L (\mathbf {v}) ^ {\mathrm{T}} \mathbf {1} _ {n}}{| | \mathbf {1} _ {n} | | _ {2} ^ {2}} \mathbf {1} _ {n},\tag{17}
$$

Let us remark $\| 1 _ { n } \| _ { 2 } = n .$ . By recalling the de<sup>fi</sup>nition of the mapping centr made in Eq. (5), the expression (17) can be equivalently written as

$$
\sum_ {i = 1} ^ {n - 1} \frac {L (\mathbf {v}) ^ {\mathrm{T}} \mathbf {y} _ {i}}{| | \mathbf {y} _ {i} | | _ {2} ^ {2}} \mathbf {y} _ {i} = c e n t r (L (\mathbf {v})).\tag{18}
$$

Now we use the de<sup>fi</sup>nition of $\phi _ { n }$ made in Eqs. (2) and (18) and Lemma 1:

$$
\begin{array}{l} \sum_ {i = 1} ^ {n - 1} \frac {L (\mathbf {v}) ^ {\mathrm{T}} \mathbf {y} _ {i}}{| | \mathbf {y} _ {i} | | _ {2} ^ {2}} \phi_ {n} (\mathbf {y} _ {i}) = \sum_ {i = 1} ^ {n - 1} \frac {L (\mathbf {v}) ^ {\mathrm{T}} \mathbf {y} _ {i}}{| | \mathbf {y} _ {i} | | _ {2} ^ {2}} \left(\mathbf {y} _ {i} 1 _ {n} ^ {\mathrm{T}} - 1 _ {n} \mathbf {y} _ {i} ^ {\mathrm{T}}\right) \\ \qquad = \left(\sum_ {i = 1} ^ {n - 1} \frac {L (\mathbf {v}) ^ {\mathrm{T}} \mathbf {y} _ {i}}{| | \mathbf {y} _ {i} | | _ {2} ^ {2}} \mathbf {y} _ {i}\right) 1 _ {n} ^ {\mathrm{T}} - 1 _ {n} \left(\sum_ {i = 1} ^ {n - 1} \frac {L (\mathbf {v}) ^ {\mathrm{T}} \mathbf {y} _ {i}}{| | \mathbf {y} _ {i} | | _ {2} ^ {2}} \mathbf {y} _ {i}\right) ^ {\mathrm{T}} \\ \qquad = \phi_ {n} [ c e n t r (L (\mathbf {v})) ] \\ \qquad = \phi_ {n} [ L (\mathbf {v}) ], \end{array}\tag{19}
$$

hence, the “north-west” block of $p _ { n + 1 } ( L ( B ) )$ in Eq. (15), by using Eqs. (16) and (19), is,

$$
\frac {n}{n + 1} p _ {n} (L (A)) + \frac {1}{n + 1} \phi_ {n} [ L (\mathbf {v}) ].
$$

The “north-east” block of $p _ { n + 1 } ( L ( B ) )$ in Eq. (15) is

$$
\frac {L (\mathbf {v}) ^ {\mathrm{T}} 1 _ {n}}{n} 1 _ {n} + \frac {1}{2 (n + 1)} \sum_ {i = 1} ^ {n - 1} \frac {t r \left[ L (A) ^ {\mathrm{T}} \phi_ {n} (\mathbf {y} _ {i}) \right] + 2 L (\mathbf {v}) ^ {\mathrm{T}} \mathbf {y} _ {i}}{\| \mathbf {y} _ {i} \| _ {2} ^ {2}} \mathbf {y} _ {i}.
$$

Let us recall that

$$
\begin{array}{l} p _ {n} (L (A)) = \frac {1}{2 n} \sum_ {i = 1} ^ {n - 1} \frac {t r \left[ L (A) ^ {\mathrm{T}} \phi_ {n} (\mathbf {y} _ {i}) \right]}{| | \mathbf {y} _ {i} | | _ {2} ^ {2}} \phi_ {n} (\mathbf {y} _ {i}) \\ = \frac {1}{2 n} \sum_ {i = 1} ^ {n - 1} \frac {t r \left[ L (A) ^ {\mathrm{T}} \phi_ {n} (\mathbf {y} _ {i}) \right]}{| | \mathbf {y} _ {i} | | _ {2} ^ {2}} \left(\mathbf {y} _ {i} 1 _ {n} ^ {\mathrm{T}} - 1 _ {n} \mathbf {y} _ {i} ^ {\mathrm{T}}\right), \end{array}\tag{20}
$$

$1 _ { n } ^ { \mathrm { T } } 1 _ { n } = n ,$ , and ${ \bf y } _ { i } ^ { \mathrm { T } } \boldsymbol { 1 } _ { n } = 0$ (since $\mathbf { y } _ { i } { \in } ( \mathsf { s p a n } \{ 1 _ { n } \} ) ^ { \perp } )$ . Postmultiplying $\operatorname { E q } .$ (20) by $1 _ { n }$ leads to

$$
\begin{array}{l} p _ {n} (L (A)) 1 _ {n} = \frac {1}{2 n} \sum_ {i = 1} ^ {n - 1} \frac {t r \left[ L (A) ^ {\mathrm{T}} \phi_ {n} (\mathbf {y} _ {i}) \right]}{| | \mathbf {y} _ {i} | | _ {2} ^ {2}} \left(\mathbf {y} _ {i} 1 _ {n} ^ {\mathrm{T}} - 1 _ {n} \mathbf {y} _ {i} ^ {\mathrm{T}}\right) 1 _ {n} \\ = \frac {1}{2} \sum_ {i = 1} ^ {n - 1} \frac {t r \left[ L (A) ^ {\mathrm{T}} \phi_ {n} (\mathbf {y} _ {i}) \right]}{| | \mathbf {y} _ {i} | | _ {2} ^ {2}} \mathbf {y} _ {i}. \end{array}\tag{21}
$$

By Eqs. (18) and (21), the “north-east” of $p _ { n + 1 } ( L ( B ) )$ reduces to

$$
\begin{array}{l} \frac {L (\mathbf {v}) ^ {T} 1 _ {n}}{n} 1 _ {n} + \frac {p _ {n} (L (A)) 1 _ {n} + c e n t r (L (\mathbf {v}))}{n + 1} \\ = m e a n (L (\mathbf {v})) 1 _ {n} + \frac {p _ {n} (L (A)) 1 _ {n} + c e n t r (L (\mathbf {v}))}{n + 1}. \end{array}\tag{22}
$$

By means of item iv) of Lemma 1, equality Eq. (22) yields that the “north-east” block of $p _ { n + 1 } ( L ( B ) )$ is

$$
\frac {\left(1 _ {n} 1 _ {n} ^ {\mathrm{T}} + I _ {n}\right) L (\mathbf {v}) + p _ {n} (L (A)) 1 _ {n}}{n + 1}.
$$

The proof of this theorem is <sup>fi</sup>nished since $p _ { n + 1 } ( L ( B ) )$ is skew-Hermitian. ■

In formula (6) the original matrix of pairwise comparisons, A, is used to obtain the new consistent matrix corresponding to the enlarged decision problem. Nevertheless, it is quite likely for that original matrix to have already been overridden by its associated consistent matrix. It is, thus, more natural to use the latter instead of the original matrix to build the consistent matrix for the enlarged problem. The next corollary shows that identical results are obtained in both cases. Before establishing this result, let us introduce the following notation: for a given reciprocal matrix $X ,$ let us denote by $Y _ { X }$ the consistent matrix closest to X in the sense of Theorem 2.

Corollary 1. Let $A \in M _ { n , \ n } ^ { + }$ be a reciprocal matrix and $\mathbf { v } \in M _ { n , 1 } ^ { + } . \operatorname { I f }$

$$
B = \left[ \begin{array}{c c} A & \mathbf {v} \\ J \big (\mathbf {v} ^ {\mathrm{T}} \big) & 1 \end{array} \right] \qquad \text { and } \qquad D = \left[ \begin{array}{c c} Y _ {A} & \mathbf {v} \\ J \big (\mathbf {v} ^ {\mathrm{T}} \big) & 1 \end{array} \right],
$$

then $Y _ { B } = Y _ { D }$

Proof. Item (i) of Theorem 2 leads to $L ( Y _ { A } ) = p _ { n } ( L ( A ) )$ . Having in mind that $p _ { n } ^ { 2 } = p _ { n }$ (because $p _ { n }$ is a projection), one has $p _ { n } ( L ( Y _ { A } ) ) =$ $p _ { n } [ p _ { n } ( L ( A ) ) ] = p _ { n } ( L ( A ) )$ ). On the other hand, Theorem 5 yields

$$
p _ {n + 1} (L (B)) = \left[ \begin{array}{c c} \frac {n p _ {n} (L (A)) + \phi_ {n} [ L (\mathbf {v}) ]}{n + 1} & \frac {\left(1 _ {n} 1 _ {n} ^ {\mathrm{T}} + I _ {n}\right) L (\mathbf {v}) + p _ {n} (L (A)) 1 _ {n}}{n + 1} \\ * & 0 \end{array} \right]
$$

and

$$
p _ {n + 1} (L (D)) = \left[ \begin{array}{c c} \frac {n p _ {n} (L (Y _ {A})) + \phi_ {n} [ L (\mathbf {v}) ]}{n + 1} & \frac {\left(1 _ {n} 1 _ {n} ^ {\mathrm{T}} + I _ {n}\right) L (\mathbf {v}) + p _ {n} (L (Y _ {A})) 1 _ {n}}{n + 1} \\ * & 0 \end{array} \right].
$$

Since $p _ { n } ( L ( A ) ) = p _ { n } ( L ( Y _ { A } ) )$ one gets $p _ { n + 1 } ( L ( B ) ) = p _ { n + 1 } ( L ( D ) )$ Item (i) of Theorem 2 leads to $Y _ { B } = Y _ { D } .$

## 3.2. Withdrawing an obsolete criterion from a comparison process

Now, we shall consider the inverse problem to that studied in the previous section. Imagine that we have an $( n + 1 ) \times ( n + 1 )$ reciprocal matrix B and its closest consistent matrix $Y _ { B } .$ Now, let us suppose that a concrete judgment, say $i { \in } \{ 1 , . . . , n , n { + } 1 \}$ , becomes obsolete and thus, we obtain a new matrix A by deleting the ith row and ith column to B. How can we obtain the closest consistent matrix to A making use of our knowledge of Y ? We can assume without loss of generality that $i = n + 1$ (by making a suitable permutation).

To solve the problem stated in the previous paragraph, let us write B as in Eq. (3). We have at our disposal the matrix given in Eq. (6).

Our purpose is to <sup>fi</sup>nd the matrix $p _ { n } ( L ( A ) )$ . If P is the ‘north-west’ block of the matrix given in Eq. (6), then

$$
p _ {n} (L (A)) = \frac {1}{n} [ (n + 1) P - \phi_ {n} (L (\mathbf {v})) ].
$$

## 4. Incorporating social and environmental costs to leakage control

In this section, we discuss how the algorithm given by Theorem 5 is used in a decision process and then evaluate the effectiveness of the method.

The application uses the opinions of a group of experts from a water company in Valencia (Spain) about the relative importance of various criteria regarding the adoption of a certain leakage control policy. Water leakage is a major problem for any urban water system. The main goal is the minimization of water loss [27,19,20,1,28] by means of suitable leakage control. Vast sums are devoted annually to this aim worldwide. In a simpli<sup>fi</sup>ed setting, two main alternatives are considered: ALC (active leakage control) and PLC (passive leakage control). The former involves taking a priori actions in the supply system in a preventive manner, while the latter consists in just repairing reported or evident leaks [13]. Various criteria, involving both tangible factors and intangible or qualitative factors, may be used to decide on the alternatives. To illustrate the application of Theorem 5, we <sup>fi</sup>rst consider a set of four criteria, namely:

$\mathsf C _ { 1 }$ planning development cost and its implementation;

$\mathsf C _ { 2 }$ budget and credits;

$\mathsf C _ { 3 }$ investment retrieval;

$\mathsf { C } _ { 4 }$ environmental cost (such as ${ \mathrm { C O } } _ { 2 }$ emissions produced by the used energy, mainly by pumps);

and then we add a <sup>fi</sup>fth criterion:

${ \mathsf C } _ { 5 }$ social cost (such as damage to properties and other service networks; effects of supply disruptions such as compensations; inconveniences caused by closed or restricted streets, etc.).

The hierarchical structure for the <sup>fi</sup>rst problem is presented in Fig. 1.

For this problem, Table 1 gathers the experts' opinions, compiled after comprehensive discussion, according to the Saaty nine-point scale. As a consequence, the entries of this matrix represent the expert knowledge of the company managers.

For this matrix, the consistency index and the consistency ratio are, respectively:

$$
\mathrm{CI} = 0.3677, \text { and } \mathrm{CR} = 41.31 \% .
$$

As a consequence, the matrix in Table 1 is not consistent, and consistency improvement is necessary. After applying the linearization process described in [5] the consistent matrix in Table 2 is obtained; this matrix, after feedback with the experts, is accepted.

This matrix uses the same Saaty nine-point scale, and the only difference is that intermediate values are shown in the calculations. Given that this is the result of a numerical process, the entries for this matrix do not strictly follow the integer semantics inherent in the Saaty nine-point scale. Nevertheless, both matrices share the same verbal scale and enable us to <sup>fi</sup>nd a reliable vector of priorities:

$$
Z _ {4} = [ 0. 3 5 0. 2 3 0. 3 5 0. 0 7 ] ^ {\mathrm{T}},
$$

that shows a clear preponderance of economic criteria, especially ${ \sf C } _ { 1 }$ and $\mathsf { C } _ { 3 } .$

![](/api/attachments/V2S6Q6UY/fulltext/images/8248db93ef607fcd073f00082d19dfda463a86cac9af1d203280b85a7050d7a4.jpg)  
Fig. 1. Initial hierarchical structure of the decision-making problem.

However, based on a number of reasons irrelevant for this study, it was decided to include a new criterion that could take into consideration a new category of costs, in our case, social costs. The hierarchical structure of the new decision-making problem is represented in Fig. 2.

Accordingly, the 4×4 matrix in Table 2 must be enlarged to a new 5×5 matrix incorporating the pairwise comparisons between ${ \sf C } _ { 3 }$ and the other four criteria. After consulting the team of experts, comparison values in the last column of the matrix in Table 3 are produced, with reciprocal values in the last row, and these have been pasted to the consistent matrix in Table 2, according to Corollary 1.

This matrix again does not pass the test of consistency (CI=0.1714 and CR=15.44). The new consistent matrix corresponding to this new problem, Table 4, may be accomplished without starting calculations from scratch by using formula (6) in Theorem 5.

It is worth noting that this formula is clearly explicit, involving just a few simple matrix calculations. As a consequence, its implementation does not involve any computation burden at all. In fact, it can be straightforwardly implemented in just one expression within a computational environment that includes matrix computation functions.

The priority vector for this matrix, the normalized (so that the components add 1) Perron eigenvector, is

$$
Z _ {5} = \left[ \begin{array}{l l l l l} 0. 3 2 & 0. 2 1 & 0. 2 5 & 0. 0 6 & 0. 1 6 \end{array} \right] ^ {\mathrm{T}}.
$$

Among other problem-speci<sup>fi</sup>c interpretations that the experts could produce, let us remark on the following. The consistency improvement process has managed to detect some bias in the experts' opinions regarding the newly introduced social costs. In fact, a few days before the experts provided the new comparison values a couple of major accidents (producing casualties) were caused by water leaks in two Spanish towns. These accidents had angered public opinion. As a consequence, the importance given to social costs were (unconsciously) magni<sup>fi</sup>ed by the experts, as they responded a posteriori.

Matrix of criteria comparison, $A _ { 4 \times 4 }$

<table><tr><td></td><td> $C_1$ </td><td> $C_2$ </td><td> $C_3$ </td><td> $C_4$ </td></tr><tr><td> $C_1$ </td><td>1</td><td>1/3</td><td>3</td><td>5</td></tr><tr><td> $C_2$ </td><td>3</td><td>1</td><td>1/3</td><td>3</td></tr><tr><td> $C_3$ </td><td>1/3</td><td>3</td><td>1</td><td>5</td></tr><tr><td> $C_4$ </td><td>1/5</td><td>1/3</td><td>1/5</td><td>1</td></tr></table>

Observe, for example, that the social impact was initially considered <sup>fi</sup>ve times more important than the environmental impact and even twice as important as investment retrieval. After achieving consistency, these values are suitably placed in their true position. In addition, neither social nor environmental costs seem to unbalance this group of experts toward criteria less related to economic aspects. This can be observed from the fact that the new priority vector, $Z _ { 5 }$ exhibits values very close to $Z _ { 4 }$ with respect to the <sup>fi</sup>rst three components, while the environmental and social criteria only manage to get a couple of tenths from the others. Yet, this fact is worthwhile emphasizing: environmental and social costs have taken more than 20% of the total importance placed on the <sup>fi</sup>ve criteria.

The next step in AHP, as a multi-criteria decision-making process, consists in comparing the alternatives in relation with all the criteria. The values provided by the experts, together with the associated priority vectors, are compiled in Table 5.

Finally, the main target is accomplished by aggregating these scores – a synthesis of priorities – to determine the best decision. A decision score is computed for any alternative by multiplying its priority value by the priority of a given criterion and then summing for all the criteria:

$$
W = [ 0. 6 4 0. 3 6 ] ^ {\mathrm{T}}.
$$

In this case, according to [25], the largest coordinate of W, corresponding to active leakage control, is clearly preferred over passive leakage control due to the fact that ALC is considered more important than PLC for all except the <sup>fi</sup>rst criteria. In fact, ALC, which hinges on having a project (with all its associated costs), is less preferred than PLC (no project consideration) regarding C =planning development cost and its implementation. Moreover, the other criteria (including environmental and social costs, but especially the prospective of investment retrieval) drag the decision toward ALC.

Consistent matrix closest to $A _ { 4 \times 4 }$

<table><tr><td></td><td> $C_1$ </td><td> $C_2$ </td><td> $C_3$ </td><td> $C_4$ </td></tr><tr><td> $C_1$ </td><td>1.00</td><td>1.50</td><td>0.98</td><td>4.87</td></tr><tr><td> $C_2$ </td><td>0.67</td><td>1.00</td><td>0.66</td><td>3.25</td></tr><tr><td> $C_3$ </td><td>1.02</td><td>1.52</td><td>1.00</td><td>4.96</td></tr><tr><td> $C_4$ </td><td>0.21</td><td>0.31</td><td>0.2</td><td>1.00</td></tr></table>

![](/api/attachments/V2S6Q6UY/fulltext/images/49b81c1fe57b9914515c1137b83b2742e49bf6c26b2e567922f1b44a5bf38d4c.jpg)  
Fig. 2. Enlarged decision-making problem.

## 5. Conclusions

In this work, we consider a new dimension in the traditional AHP methodology by considering that input may be either static or dynamic, depending on whether actors provide their preferences all at once or at multiple times. We think that this will open a window to various new variants of AHP methodology in the future. However, since it is not possible to address all potential related issues at once, in this paper we aim to solve a particular variant in which the introduction of a new criterion or the withdrawal of an obsolete criteria are allowed while avoiding the need for repeating all the calculations from scratch. This novel method is computationally inexpensive and is based on a linearization process previously introduced by the authors [5]. To check the performance of the algorithm, an experiment is performed that considers a decisionmaking problem in water supply regarding the adoption of either an active or a passive leakage control policy.

Many future extensions regarding dynamic AHP may be devised. For example, in the second scenario considered in the introduction the consulted actors are unfamiliar with the effects of various items. In this case, collecting complete and quality preference information from decision makers at the same time cannot be expected. It is necessary to allow user preference data to be input at multiple times at their own convenience. As a result, the static input mode could be changed in such a way that partial results based on partial preference data could be generated from the data collected at multiple times, and new results could eventually be obtained when all the information is complete. Allowing for this dynamic input mode in traditional approaches would open the door to a large array of future research issues.

Table 3  
Enlarged criteria comparison matrix, $D _ { 5 \times 5 } .$

<table><tr><td></td><td> $C_1$ </td><td> $C_2$ </td><td> $C_3$ </td><td> $C_4$ </td><td> $C_5$ </td></tr><tr><td> $C_1$ </td><td>1.00</td><td>1.50</td><td>0.98</td><td>4.87</td><td>5</td></tr><tr><td> $C_2$ </td><td>0.67</td><td>1.00</td><td>0.66</td><td>3.25</td><td>3</td></tr><tr><td> $C_3$ </td><td>1.02</td><td>1.52</td><td>1.00</td><td>4.96</td><td>1/2</td></tr><tr><td> $C_4$ </td><td>0.21</td><td>0.31</td><td>0.2</td><td>1.00</td><td>1/5</td></tr><tr><td> $C_5$ </td><td>1/5</td><td>1/3</td><td>2</td><td>5</td><td>1</td></tr></table>

Table 4  
Consistent matrix closest to $D _ { 5 \times 5 } .$

<table><tr><td></td><td> $C_1$ </td><td> $C_2$ </td><td> $C_3$ </td><td> $C_4$ </td><td> $C_5$ </td></tr><tr><td> $C_1$ </td><td>1.00</td><td>1.53</td><td>1.26</td><td>5.83</td><td>1.99</td></tr><tr><td> $C_2$ </td><td>0.65</td><td>1.00</td><td>0.82</td><td>3.80</td><td>1.30</td></tr><tr><td> $C_3$ </td><td>0.79</td><td>1.22</td><td>1.00</td><td>4.62</td><td>1.58</td></tr><tr><td> $C_4$ </td><td>0.17</td><td>0.26</td><td>0.22</td><td>1.00</td><td>0.34</td></tr><tr><td> $C_5$ </td><td>0.50</td><td>0.77</td><td>0.63</td><td>2.93</td><td>1.00</td></tr></table>

Another issue worth exploring is the way a new criterion is added in a context of group decision making [8,10]. Various approaches can be devised. Individual judgments could be considered for the new criterion, then the geometric mean of the expert judgments obtained, and the process described in this paper applied to the resulting matrix. Another alternative could be the individual application of the process to the individual enlarged expert matrices and, <sup>fi</sup>nally, some type of voting system could be used to produce the <sup>fi</sup>nal priority vector. Another possibility would compute interval bounds for the expert judgments regarding the new criterion and then perform the calculations using some interval arithmetic. In the case of many decision makers, various voting systems could be considered with different purposes, such as eliminating outliers, aggregating values, etc.

## Acknowledgments

This work has been performed under the support of the project IDAWAS, DPI2009-11591 of the Dirección General de Investigación del Ministerio de Ciencia e Innovación (Spain), with the supplementary support of ACOMP/2011/188 of the Conselleria d'Educació of the Generalitat Valenciana, and the support given to the <sup>fi</sup>rst author by Spanish project MTM2010-18539. The third author is also indebted to the Universitat Politècnica de València for the sabbatical leave granted during the <sup>fi</sup>rst semester of 2011. The use of English in this paper was revised by John Rawlins.

Table 5  
Alternative comparisons for each criterion together with their priority vectors $( \mathrm { e i g } ) .$

<table><tr><td colspan="3"> ${\mathrm{C}}_{1}$ </td><td>eig</td></tr><tr><td></td><td>ALC</td><td>PLC</td><td></td></tr><tr><td>ALC</td><td>1</td><td>1/3</td><td>0.25</td></tr><tr><td>PLC</td><td>3</td><td>1</td><td>0.75</td></tr></table>

<table><tr><td colspan="3"> ${\mathrm{C}}_{2}$ </td><td>eig</td></tr><tr><td></td><td>ALC</td><td>PLC</td><td></td></tr><tr><td>ALC</td><td>1</td><td>5</td><td>0.83</td></tr><tr><td>PLC</td><td>1/5</td><td>1</td><td>0.17</td></tr></table>

<table><tr><td colspan="3"> ${\mathrm{C}}_{4}$ </td><td>eig</td></tr><tr><td></td><td>ALC</td><td>PLC</td><td></td></tr><tr><td>ALC</td><td>1</td><td>3</td><td>0.75</td></tr><tr><td>PLC</td><td>1/3</td><td>1</td><td>0.25</td></tr></table>

<table><tr><td colspan="3"> ${\mathrm{C}}_{3}$ </td><td>eig</td></tr><tr><td></td><td>ALC</td><td>PLC</td><td></td></tr><tr><td>ALC</td><td>1</td><td>5</td><td>0.83</td></tr><tr><td>PLC</td><td>1/5</td><td>1</td><td>0.17</td></tr></table>

<table><tr><td colspan="3"> ${\mathrm{C}}_{5}$ </td><td>eig</td></tr><tr><td></td><td>ALC</td><td>PLC</td><td></td></tr><tr><td>ALC</td><td>1</td><td>5</td><td>0.83</td></tr><tr><td>PLC</td><td>1/5</td><td>1</td><td>0.17</td></tr></table>

## References

[1] S. Alvisi, M. Franchini, Multiobjective optimization of rehabilitation and leakage detection scheduling in water distribution systems, Journal of Water Resources Planning and Management (ASCE) 135 (2009) 426–439.

[2] J. Barzilai, Deriving weights from pairwise comparison matrices, The Journal of the Operational Research Society 48 (12) (1997) 1226–1232.

[3] J. Benítez, X. Delgado-Galván, J. Izquierdo, R. Pérez-García, Consistent matrices and consistency improvement in decision-making processes, in: B.H.V. Topping, J.M. Adam, F.J. Pallarés, R. Bru, M.L. Romero (Eds.), Proceedings of the Seventh International Conference on Engineering Computational Technology, Civil-Comp Press, Stirlingshire, United Kingdom, 2010, http://dx.doi.org/10.4203/ccp.94.21, paper 21.

[4] J. Benítez, X. Delgado-Galván, J.A. Gutiérrez, J. Izquierdo, Balancing consistency and expert judgment in AHP, Mathematical and Computer Modelling 54 (2011) 1785–1790.

[5] J. Benítez, X. Delgado-Galván, J. Izquierdo, Rafael Pérez-García, Achieving matrix consistency in AHP through linearization, Applied Mathematical Modelling 35 (2011) 4449–4457.

[6] N. Bryson, A goal programming method for generating priorities vectors, The Journal of the Operational Research Society 46 (5) (1995) 641–648.

[7] D. Cao, L.C. Leung, J.S. Law, Modifying inconsistent comparison matrix in analytic hierarchy process: a heuristical approach, Decision Support Systems 44 (2008) 944–953.

[8] B. Chandran, B. Golden, E. Wasil, Linear programming models for estimating weights in the analytic hierarchy process, Computers and Operations Research 32 (2005) 2235–2254.

[9] A.T.W. Chu, R.E. Kalaba, K. Springarn, A comparison of two methods for determining the weights of belonging to fuzzy sets, Journal of Optimization Theory and Applications 27 (4) (1979) 531–541.

[10] E. Condon, B. Golden, E. Wasil, Visualizing group decisions in the analytic hierarchy process Computers and Operations Research 30 (2003) 1435–1445

[11] G. Crawford, C. Williams, A note on the analysis of subjective judgement matrices, Journal of Mathematical Psychology 29 (4) (1985) 387–405.

[12] X. Delgado-Galván, R. Pérez-García, J. Izquierdo, J. Mora-Rodríguez, Analytic hierarchy process for assessing externalities in water leakage management, Mathematical and Computer Modelling 52 (2010) 1194–1202.

[13] M. Farley, S. Trow, Losses in water distribution networks, A Practitioner's Guide to Assessment, Monitoring and Control, IWA Publishing, UK, 2003.

[14] J.S. Finan, W.J. Hurley, The analytic hierarchy process: does adjusting a pairwise comparison matrix to improve the consistency ratio help? Computers and Operations Research 24 (1997) 749–755

[15] C.-C. Lin, An enhanced goal programming method for generating priority vectors, The Journal of the Operational Research Society 57 (12) (2006) 1491–1496.

[16] C.D. Meyer, Matrix Analysis and Applied Linear Algebra, SIAM, 2000.

[17] L. Mikhailov, A fuzzy programming method for deriving priorities in the analytic hierarchy process, The Journal of the Operational Research Society 51 (3) (2000) 341–349.

[18] H. Monsuur, An intrinsic consistency threshold for reciprocal matrices, European Journal of Operational Research 96 (1996) 387–391.

[19] M. Nicolini, C. Giacomello, K. Deb, Calibration and optimal leakage management for a real water distribution network, Journal of Water Resources Planning and Management (ASCE) 137 (2011) 134–142.

[20] R. Puust, Z. Kapelan, D.A. Savic, T. Koppel, A review of methods for leakage management in pipe networks, Urban Water Journal 7 (2010) 25–45.

[21] R. Ramanathan, U. Ramanahan, A qualitative perspective to deriving weights from pairwise comparison matrices, Omega 38 (2010) 228–232.

[22] T.L. Saaty, Decision-making with the AHP: why is the principal eigenvector necessary, European Journal of Operational Research 145 (2003) 85–91.

[23] T.L. Saaty, Relative measurement and its generalization in decision making. Why pairwise comparisons are central in mathematics for the measurement of intangible factors. The analytic hierarchy/network process, Revista de la Real Academia de Ciencias Serie A: Matemáticas 102 (2) (2008) 251–318.

[24] T.L. Saaty, L.G. Vargas, Comparison of eigenvalue, logarithmic least squares and least squares methods in estimating ratios, Mathematical Modelling 5 (5) (1984) 309–324.

[25] B. Srdjevic, Linking analytic hierarchy process and social choice methods to support group decision-making in water management, Decision Support Systems 42 (2007) 2261–2273.

[26] G.W. Stewart, Matrix Algorithms, vol. II, SIAM, 2001.

[27] M. Tabesh, A.H. Asadiyani Yekta, R. Burrows, An integrated model to evaluate losses in water distribution systems, Water Resources Management 23 (2009) 477–492.

[29] Z. Xu, C. Wei, A consistency improving method in the analytic hierarchy process, European Journal of Operational Research 116 (1999) 443–449.

Julio Benítez Born in 1968. Graduated in Mathematical Sciences in 1992. Ph.D. in Mathematical Sciences in 2001. Professor at the Universitat Politècnica de València (Spain) since 1993. His current research activities: Matrix algebra, C\*-algebras, rings, applications of matrix analysis to Engineering problems, and applications of the new technologies to teaching.

Xitlali V Delgado-Galván. Graduated in Economical Sciences in 2002. Ph.D. in Hydraulic and Environmental Engineering at the Universitat Politècnica de València (Spain) in 2011 with the title ‘Application of the method of analytic hierarchy process (AHP) to the management of water losses in water supply systems’. She is currently developing postdoctoral studies at the University of Guanajuato (Mexico) in coordination with the Universitat Politècnica de València.

Joaquín Izquierdo Ph.D. in Mathematics, Full Professor of Applied Mathematics. Educational career developed in the Universitat Politècnica de València (Spain), teaching Algebra, Calculus, Differential Equations, Numerical Methods applied to Engineering, etc. Research activity in the application of soft computing techniques into the water <sup>fi</sup>eld: Consulting in water resources; Continuous Professional development for Spanish and Latin–American professionals; Research: author and editor of books, research pa pers and contributions to international events; tutor of several doctoral dissertations; author of commercial computer simulation packages; co-organizer of periodically international scienti<sup>fi</sup>c Events; Participant in R&D projects: local, regional (Comunitat Valenciana), national (CICYT), European (COMETT, TEMPUS, ERASMUS, EUROFORM, ADAPT FEDER UE DGEnvironment) and international (NATO).

Rafael Pérez-García M.Sc. and Ph.D. in Industrial Engineering, Full Professor in the Department of Hydraulic Engineering of the Universitat Politècnica de València (Spain). Since 1989 he has dictated different courses at the graduate, postgraduate and doctorate levels. His research activity includes, among others, the co-ordination of both public and private research projects, the direction of projects of hydraulic software, the tutoring of PhD theses and the organization of four editions of the Latin–American seminar on water supply systems (SEREA).
