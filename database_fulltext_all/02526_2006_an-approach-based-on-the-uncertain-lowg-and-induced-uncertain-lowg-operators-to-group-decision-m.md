---
otero_id: 2526
otero_key: "6EBCK73S"
title: "An approach based on the uncertain LOWG and induced uncertain LOWG operators to group decision making with uncertain multiplicative linguistic preference relations"
authors: "Zeshui Xu"
year: "2006"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2004.08.011"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# An approach based on the uncertain LOWG and induced uncertain LOWG operators to group decision making with uncertain multiplicative linguistic preference relations

Zeshui Xu

College of Economics and Management, Southeast University, Nanjing, Jiangsu 210096, China

Received 6 June 2004; received in revised form 18 August 2004; accepted 19 August 2004 Available online 25 September 2004

## Abstract

In this paper, we define the concept of uncertain multiplicative linguistic preference relation, and introduce some operational laws of uncertain multiplicative linguistic variables. We propose some new aggregation operators including the uncertain linguistic geometric mean (ULGM) operator, uncertain linguistic weighted geometric mean (ULWGM) operator, uncertain linguistic ordered weighted geometric (ULOWG) operator, and induced uncertain linguistic ordered weighted geometric (IULOWG) operator. The IULOWG operator is a more general type of aggregation operator, which is based on the ULGM and ULOWG operators. Moreover, based on the ULOWG and IULOWG operators and the formula for the comparison between two uncertain multiplicative linguistic variables, we develop an approach to group decision making with uncertain multiplicative linguistic preference relations, and, finally, an application of the approach to group decision-making problem with uncertain multiplicative linguistic preference relations is pointed out. <sup>D</sup> 2004 Elsevier B.V. All rights reserved.

Keywords: Aggregation; Group decision making; Operator; Uncertain linguistic variable; Uncertain multiplicative linguistic preference relation

## 1. Introduction

The increasing complexity of the socio-economic environment makes it less and less possible for a single decision maker (DM) to consider all relevant aspects of a problem [16,22]. As a result, many decision-making processes, in the real world, take place in group settings. Group decision-making problems follow a common resolution scheme [17,8,20] composed by the following two phases:

1) Aggregation phase: It combines individual preferences to obtain a collective preference value for each alternative.

2) Exploitation phase: It orders collective preference values to obtain the best alternative(s).

A number of studies have recently focused on group decision making with linguistic preference relations [10–12,6,7]. Herrera et al. [10] developed a consensus model for group decision making under linguistic assessments. It is based on the use of linguistic preferences to provide individuals’ opinions, and on the use of fuzzy majority of consensus, represented by means of a linguistic quantifier. Herrera et al. [11] combined the linguistic ordered weighted averaging (LOWA) operator with linguistic preference relations and the concept of dominance and nondominance to show its use in the field of group decision making, and presented three models of group decision making based on the LOWA operator. Herrera et al. [12] presented a consensus model in complete linguistic framework for group decision making guided by consistency and consensus measures. The measures allow analyzing, controlling, and monitoring the consensus reaching process, describing the current consensus and current consistency stage. Herrera and Herrera-Viedma [6] defined various linguistic choice sets of alternatives characterized by means of the concept of linguistic choice function, and presented a set of linguistic choice functions based on the linguistic conjunctive function min and the LOWA operator, and then proposed a linguistic choice mechanism that allows the DMs to obtain more precise and coherent solutions. Herrera and Herrera-Viedma [7] analyzed the steps to follow in the linguistic decision analysis of a group decisionmaking problem with linguistic preference relations. Sometimes, however, the DMs are willing or able to provide only uncertain linguistic information because of time pressure, lack of knowledge, or data, and their limited expertise related to the problem domain. Up to now, there is no approach developed for dealing with group decision making with uncertain multiplicative linguistic preference relations. Therefore, it is neces sary to pay attention to this issue.

The aim of this paper is to develop an approach to group decision making with uncertain multiplicative linguistic preference relations. In order to do so, the rest of this paper is organized as follows. In Section 2, we introduce some operational laws of uncertain multiplicative linguistic variables and the formula for the comparison between two uncertain multiplicative linguistic variables. In Section 3, we propose some new aggregation operators including the uncertain linguistic geometric mean (ULGM) operator, uncertain linguistic weighted geometric mean (ULWGM) operator, uncertain linguistic ordered weighted geometric (ULOWG) operator, and induced uncertain linguistic ordered weighted geometric (IULOWG) operator. In Section 4, we develop an approach, based on the ULOWG and IULOWG operators and the formula for the comparison between two uncertain linguistic variables, to group decision making with uncertain multiplicative linguistic preference relations. In Section 5, an illustrative example is pointed out. Concluding remarks are included in Section $^ { 6 , }$ and, finally, an appendix (Appendix A) is given.

## 2. Uncertain linguistic variables and some operational laws

Let $S = \{ s _ { \alpha } | \alpha { = } 1 / t , . . . , 1 / 2 , 1 , 2 , . . . , t \}$ be a multiplicative linguistic label set with odd cardinality. Any label, $s _ { \alpha } ,$ , represents a possible value for a linguistic variable, and it is required that the multiplicative linguistic label set should satisfy the following characteristics:

1) The set is ordered: $s _ { \alpha } { > } s _ { \beta } \mathrm { ~ i f ~ } \alpha { > } \beta ;$

2) There is the reciprocal operator: $\mathrm { r e c } ( s _ { \alpha } ) { = } s _ { \beta }$ such that $\alpha \beta { = } 1$

We call this multiplicative linguistic label set S the multiplicative linguistic scale. For example, S can be defined as:

$$
\begin{array}{l} S = \left\{s _ {1 / 5} = \text { extremely   low }, \quad s _ {1 / 4} = \text { very   low }, \right. \\ s _ {1 / 3} = \text { low }, \quad s _ {1 / 2} = \text { slightly   low }, \quad s _ {1} = \text { medium }, \\ s _ {2} = \text { slightly   high }, \quad s _ {3} = \text { high }, \quad s _ {4} = \text { very   high }, \\ s _ {5} = \text { extremely   high } \} \end{array}
$$

To preserve all the given information, we extend the discrete multiplicative linguistic label S set to a continuous multiplicative linguistic label set $\bar { S } =$ $\{ s _ { \alpha } | \alpha { \in } [ 1 / q , q ] \}$ , where $q ( q { > } t )$ is a sufficiently large positive integer. If $s _ { \alpha } { \in } S _ { i }$ , then we call $s _ { \alpha }$ the original multiplicative linguistic label; otherwise, we call the virtual multiplicative linguistic label. In general, the DM uses the original multiplicative linguistic labels to evaluate alternatives, and the virtual multiplicative linguistic labels can only appear in operations.

Let $\scriptstyle \widetilde { s } = \left[ s _ { \alpha } , s _ { \beta } \right]$ , where $s _ { \alpha } , s _ { \beta } { \in } \bar { S } , s _ { \alpha } ,$ , and $s _ { \beta }$ are the lower and upper limits, respectively. We then call s˜ the uncertain multiplicative linguistic variable. Let $\tilde { S }$ be the set of all the uncertain multiplicative linguistic variables.

Consider any three uncertain multiplicative linguistic variables $\widetilde { s } = [ s _ { \alpha } , s _ { \beta } ] , \widetilde { s } _ { 1 } = [ s _ { \alpha _ { 1 } } , s _ { \beta _ { 1 } } ]$ , and $\widetilde { s } _ { 2 } =$ $[ s _ { \alpha _ { 2 } } s _ { \beta _ { 2 } } ] ,$ and let $\lambda , ~ \lambda _ { 1 } , ~ \lambda _ { 2 } { \in } [ 0 , 1 ]$ . Then we define their operational laws as follows:

$$
\begin{array}{l} 1) \tilde {s} _ {1} \otimes \tilde {s} _ {2} = [ s _ {\alpha_ {1}}, s _ {\beta_ {1}} ] \otimes [ s _ {\alpha_ {2}}, s _ {\beta_ {2}} ] = [ s _ {\alpha_ {1}} \otimes s _ {\alpha_ {2}}, s _ {\beta_ {1}} \otimes s _ {\beta_ {2}} ] \\ = [ s _ {\alpha_ {1} \alpha_ {2}}, s _ {\beta_ {1} \beta_ {2}} ] \end{array}
$$

2) $\widetilde { s } _ { 1 } \otimes \widetilde { s } _ { 2 } { = } \widetilde { s } _ { 2 } \otimes \widetilde { s } _ { 1 }$

3) $\tilde { s } ^ { \lambda } { = } [ s _ { \alpha } , s _ { \beta } ] ^ { \lambda } { = } [ s _ { \alpha } , s _ { \beta } { : } ]$

4) $\widetilde { s } ^ { \lambda _ { 1 } } \otimes \widetilde { s } ^ { \lambda _ { 2 } } { = } ( \widetilde { s } ) ^ { \lambda _ { 1 } + \lambda _ { 2 } }$

5) $( \widetilde { s } _ { 1 } { \otimes } \widetilde { s } _ { 2 } ) ^ { \lambda } { = } \widetilde { s } _ { 1 } ^ { \lambda } { \otimes } \widetilde { s } _ { 2 } ^ { \lambda } .$

Definition 1. Let $\widetilde { s } _ { 1 } { = } [ s _ { \alpha _ { 1 } } , s _ { \beta _ { 1 } } ]$ and $\widetilde { s } _ { 2 } { = } [ s _ { \alpha _ { 2 } } , s _ { \beta _ { 2 } } ]$ be two uncertain multiplicative linguistic variables, and let len $( \widetilde { s } _ { 1 } ) { = } \beta _ { 1 } { - } \alpha _ { 1 }$ and len $( \widetilde { s } _ { 2 } ) { = } \beta _ { 2 } { - } \alpha _ { 2 }$ , then the degree of possibility of $\widetilde { s } _ { 1 } \widetilde { \supseteq } \widetilde { s } _ { 2 }$ is defined as:

$$
p \left(\tilde {s} _ {1} \geq \tilde {s} _ {2}\right) = \frac {\max \left\{0 , \operatorname{len} \left(\tilde {s} _ {1}\right) + \operatorname{len} \left(\tilde {s} _ {2}\right) - \max \left(\beta_ {2} - \alpha_ {1} , 0\right) \right\}}{\operatorname{len} \left(\tilde {s} _ {1}\right) + \operatorname{len} \left(\tilde {s} _ {2}\right)}\tag{1}
$$

Similarly, the degree of possibility of $\widetilde { s } _ { 2 } { \geq } \widetilde { s } _ { 1 }$ is defined as:

$$
p \left(\tilde {s} _ {2} \geq \tilde {s} _ {1}\right) = \frac {\max \left\{0 , \operatorname{len} \left(\tilde {s} _ {1}\right) + \operatorname{len} \left(\tilde {s} _ {2}\right) - \max \left(\beta_ {1} - \alpha_ {2} , 0\right) \right\}}{\operatorname{len} \left(\tilde {s} _ {1}\right) + \operatorname{len} \left(\tilde {s} _ {2}\right)}\tag{2}
$$

From Definition 1, we can get the following results easily:

(1) $0 { \le } p ( \tilde { s } _ { 1 } { \geq } \tilde { s } _ { 2 } ) { \le } 1 , 0 { \le } p ( \tilde { s } _ { 2 } { \geq } \tilde { s } _ { 1 } ) { \le } 1$

(2) $p ( \tilde { s } _ { 1 } { \geq } \tilde { s } _ { 2 } ) + p ( \tilde { s } _ { 2 } { \geq } \tilde { s } _ { 1 } ) { = } 1$ . Especially,

$$
p (\tilde {s} _ {1} \geq \tilde {s} _ {1}) = p (\tilde {s} _ {2} \geq \tilde {s} _ {2}) = 0. 5.
$$

## 3. The ULOWG and IULOWG operators

The ordered weighted geometric (OWG) operator is an aggregation operator that Chiclana et al. [1] defined and characterized to design multiplicative decision-making models [2,14,15]. It is based on the ordered weighted averaging (OWA) operator [30] and on the geometric mean. Xu and Da [26,28] presented some families of OWG operators. The OWG operator can only be used in situations where the input arguments are the exact numerical values. Recently, Xu [24] extended the OWG operator to accommodate the situations where the input arguments are linguistic variables.

Definition 2. A linguistic ordered weighted geometric (LOWG) operator of dimension n is a mapping LOWG: $\bar { S } ^ { n } { \longrightarrow } \bar { S } .$ , which has associated with it an exponential weighting vector $\omega = ( \omega _ { 1 } , \omega _ { 2 } , . . . , \omega _ { n } ) ^ { T } ;$ with $\omega _ { j } { \in } [ 0 , 1 ]$ and $\textstyle \sum _ { j = 1 } ^ { n } \omega _ { j } = 1$ , such that:

$$
\begin{array}{l} \operatorname{LOWG} _ {\omega} (s _ {\alpha_ {1}}, s _ {\alpha_ {2}}, \dots , s _ {\alpha_ {n}}) \\ = (s _ {\beta_ {1}}) ^ {\omega_ {1}} \otimes (s _ {\beta_ {2}}) ^ {\omega_ {2}} \otimes \dots \otimes (s _ {\beta_ {n}}) ^ {\omega_ {n}} \\ = (s _ {\beta_ {1} ^ {\omega_ {1}}}) \otimes (s _ {\beta_ {2} ^ {\omega_ {2}}}) \otimes \dots \otimes (s _ {\beta_ {n} ^ {\omega_ {n}}}) = s _ {\bar {\beta}} \end{array}
$$

where $\begin{array} { r } { \bar { \boldsymbol { \beta } } = \prod _ { j = 1 } ^ { n } \boldsymbol { \beta } _ { j } ^ { \omega _ { j } } , \ s _ { \beta _ { j } } } \end{array}$ is the jth largest of the $s _ { \alpha _ { j } }$ [24].

Sometimes, however, the DMs are willing or able to provide only uncertain linguistic information because of time pressure, lack of knowledge or data, and their limited expertise related to the problem domain. In the following, we shall develop some operators for aggregating uncertain multiplicative linguistic information.

Definition 3. Let ULGM: $\tilde { S } ^ { n } {  } \tilde { S }$ , if:

$$
\begin{array}{l} \text { ULGM } (\tilde {s} _ {1}, \tilde {s} _ {2}, \ldots , \tilde {s} _ {n}) \\ = (\tilde {s} _ {1} \otimes \tilde {s} _ {2} \otimes \dots \otimes \tilde {s} _ {n}) ^ {1 / n} \end{array}\tag{3}
$$

where $\widetilde { s } _ { i } { \in } \widetilde { S } , \ i { = } 1 , 2 , . . . , n .$ , then ULGM is called the uncertain linguistic geometric mean (ULGM) operator.

Example 1. Assume $\scriptstyle \widetilde { s } _ { 1 } = \left[ s _ { 1 / 3 } , s _ { 1 / 2 } \right] , \quad \widetilde { s } _ { 2 } = \left[ s _ { 1 , S _ { 2 } } \right]$ $ \widetilde { s } _ { 3 } { = } [ s _ { 1 / 4 } , s _ { 1 / 3 } ]$ , and $\widetilde { s } _ { 4 } { = } [ s _ { 4 } , s _ { 5 } ]$ , then by the operational laws of uncertain multiplicative linguistic variables, we have:

$$
\begin{array}{l} \text { ULGM } (\tilde {s} _ {1}, \tilde {s} _ {2}, \tilde {s} _ {3}, \tilde {s} _ {4}) \\ = \left(\left[ s _ {1 / 3}, s _ {1 / 2} \right] \otimes \left[ s _ {1}, s _ {2} \right] \otimes \left[ s _ {1 / 4}, s _ {1 / 3} \right] \otimes \left[ s _ {4}, s _ {5} \right]\right) ^ {1 / 4} \\ = [ s _ {0. 7 4}, s _ {1. 1 4} ] \end{array}
$$

Definition 4. Let ULWGM: ${ \tilde { S } } ^ { n } { \longrightarrow } { \tilde { S } } ,$ if:

$$
\begin{array}{l} \text { ULWGM } _ {\omega} (\tilde {s} _ {1}, \tilde {s} _ {2}, \dots \tilde {s} _ {n}) \\ = \tilde {s} _ {1} ^ {\omega_ {1}} \otimes \tilde {s} _ {2} ^ {\omega_ {2}} \otimes \dots \otimes \tilde {s} _ {n} ^ {\omega_ {n}} \end{array}\tag{4}
$$

where $\omega = ( \omega _ { 1 } , \omega _ { 2 } , . . . , \omega _ { n } ) ^ { T }$ is the exponential weighting vector of the $\widetilde { s } _ { i } ; \widetilde { s } _ { i } { \in } \widetilde { S } , i { = } 1 , 2 , . . . , n$ , then is called the uncertain linguistic weighted geometric mean (ULWGM) operator.

Example 2. Assume ${ \widetilde { S } } _ { 1 } \mathrm { { = } } \big [ S _ { 1 / 3 } , S _ { 1 / 2 } \big ] , { \widetilde { S } } _ { 2 } \mathrm { { = } } \big [ S _ { 1 , S _ { 2 } } \big ] , { \widetilde { S } } _ { 3 } \mathrm { { = } } \big [ S _ { 1 / 4 } ,$ $s _ { 1 / 3 } ] .$ , and $\widetilde { s } _ { 4 } { = } [ s _ { 4 } , s _ { 5 } ]$ and $\omega = ( 0 . 3 , 0 . 2 , 0 . 3 , 0 . 2 ) ^ { T }$ , then by the operational laws of uncertain multiplicative lin guistic variables, we have:

$$
\begin{array}{l} \mathrm{ULWGM} _ {\omega} (\tilde {s} _ {1}, \tilde {s} _ {2}, \tilde {s} _ {3}, \tilde {s} _ {4}) \\ = [ s _ {1 / 3}, s _ {1 / 2} ] ^ {0. 3} \otimes [ s _ {1}, s _ {2} ] ^ {0. 2} \otimes [ s _ {1 / 4}, s _ {1 / 3} ] ^ {0. 3} \otimes [ s _ {4}, s _ {5} ] ^ {0. 2} \\ = [ s _ {0. 6 3}, s _ {0. 9 3} ] \end{array}
$$

Definition 5. An uncertain linguistic ordered weighted geometric (ULOWG) operator of dimension n is a mapping $\operatorname { U L O W G : } \tilde { S } ^ { n } { \longrightarrow } \tilde { S }$ , which has, associated with it, an exponential weighting vector $\omega = ( \omega _ { 1 } , \omega _ { 2 } , . . . , \omega _ { n } ) ^ { T }$ such that $\begin{array} { r } { \omega _ { j } { \in } [ 0 , 1 ] , j = 1 , 2 , \ldots , n , \sum _ { j = 1 } ^ { n } \omega _ { j } = 1 } \end{array}$ . Furthermore:

$$
\mathrm{ULOWG} _ {\omega} \left(\tilde {s} _ {1}, \tilde {s} _ {2}, \dots , \tilde {s} _ {n}\right) = \tilde {r} _ {1} ^ {\omega_ {1}} \otimes \tilde {r} _ {2} ^ {\omega_ {2}} \otimes \dots \otimes \tilde {r} _ {n} ^ {\omega_ {n}}\tag{5}
$$

where $\tilde { r } _ { j }$ is the jth largest of the $\tilde { s } _ { i } , \tilde { s } _ { i } { \in } \tilde { S } .$ . Especially, if $\omega { = } ( 1 / n , 1 / n , . . . . , 1 / n ) ^ { T }$ , then the ULOWG operator is reduced to the ULGM operator.

To rank these arguments $\widetilde { s } _ { i } ( i { = } 1 , 2 , \dotsc . . . , n )$ , we first compare each argument $\tilde { s } _ { i }$ with all arguments $\widetilde { s } _ { j } ( j { = } 1 , 2 , \ldots . , n )$ by using Eq. (1), and let $p _ { i j } { = } p ( \tilde { s } _ { i } { \geq } \tilde { s } _ { j } )$ Then we construct a complementary matrix [2,19,27, 21,29,23,25] $\scriptstyle \mathbf { P } = ( p _ { i j } ) _ { n \times n } ,$ where:

$$
p _ {i j} \geq 0, \quad p _ {i j} + p _ {j i} = 1, \quad p _ {i i} = 0. 5, \quad i, j = 1, 2, \dots , n\tag{6}
$$

Summing all elements in each line of matrix P, we have:

$$
p _ {i} = \sum_ {j = 1} ^ {n} p _ {i j}, \quad i = 1, 2, \dots , n\tag{7}
$$

Then we can rank the arguments $\widetilde { \mathtt { s } } _ { i } ( i { = } 1 , 2 , . . . . , n )$ in descending order in accordance with the values of $p _ { i } ( i { = } 1 , 2 , . . . , n )$

Example 3. Assume $\omega = ( 0 . 2 , 0 . 3 , 0 . 3 , 0 . 2 ) ^ { T } , \tilde { s } _ { 1 } = [ s _ { 2 } , s _ { 3 } ] ,$ $ \widetilde { s } _ { 2 } { = } [ s _ { 1 } , s _ { 3 } ] , \widetilde { s } _ { 3 } { = } [ s _ { 2 } , s _ { 4 } ]$ , and $\widetilde { s } _ { 4 } { = } [ s _ { 3 } , s _ { 4 } ]$ . To rank these arguments, we first compare each argument $\tilde { s } _ { i }$ with all arguments $\widetilde { s } _ { j } ( j = 1 , 2 , 3 , 4 )$ by using Eq. (1), and then construct a complementary matrix:

$$
\mathbf {P} = \left[ \begin{array}{c c c c} 0. 5 & 0. 6 6 6 7 & 0. 3 3 3 3 & 0 \\ 0. 3 3 3 3 & 0. 5 & 0. 2 5 & 0 \\ 0. 6 6 6 7 & 0. 7 5 & 0. 5 & 0. 3 3 3 3 \\ 1 & 1 & 0. 6 6 6 7 & 0. 5 \end{array} \right]
$$

Summing all elements in each line of matrix P, we have:

$$
\begin{array}{l l} p _ {1} = 1. 5 0 0 0, & p _ {2} = 1. 0 8 3 3, \quad p _ {3} = 2. 2 5 0 0, \\ p _ {4} = 3. 1 6 6 7 \end{array}
$$

Then we rank the arguments $\scriptstyle { \tilde { s } } _ { i } ( i = 1 , 2 , 3 , 4 )$ in descending order in accordance with the values of $p _ { i } ( i { = } 1 , 2 , 3 , 4 )$

$$
\begin{array}{l l} \tilde {\boldsymbol {r}} _ {1} = \tilde {\boldsymbol {s}} _ {4} = [ s _ {3}, s _ {4} ], & \tilde {\boldsymbol {r}} _ {2} = \tilde {\boldsymbol {s}} _ {3} = [ s _ {2}, s _ {4} ], \\ \tilde {\boldsymbol {r}} _ {3} = \tilde {\boldsymbol {s}} _ {1} = [ s _ {2}, s _ {3} ], & \tilde {\boldsymbol {r}} _ {4} = \tilde {\boldsymbol {s}} _ {2} = [ s _ {1}, s _ {3} ] \end{array}
$$

Thus,

$$
\begin{array}{l} \mathrm{ULOWG} _ {\omega} (\tilde {s} _ {1}, \tilde {s} _ {2}, \tilde {s} _ {3}, \tilde {s} _ {4}) \\ = [ s _ {3}, s _ {4} ] ^ {0. 2} \otimes [ s _ {2}, s _ {4} ] ^ {0. 3} \otimes [ s _ {2}, s _ {3} ] ^ {0. 3} \otimes [ s _ {1}, s _ {3} ] ^ {0. 2} \\ = [ s _ {1. 8 9}, s _ {3. 4 9} ] \end{array}
$$

Yager and Filev [32] introduced an induced ordered weighted averaging (IOWA) operator, which takes as its argument pairs, called OWA pairs, in which one component is used to induce an ordering over the second components, which are exact numerical values and then aggregated. Xu and Da [28] developed an induced ordered weighted geometric (IOWG) operator that is based on the IOWA operator, and the geometric mean, which can be used to aggregate multiplicative preference relations with exact numerical values in group decision-making problems [3].

Definition 6. An IOWG operator is defined as follows:

$$
\mathrm{IOWG} _ {\omega} \left(\left\langle u _ {1}, a _ {1} \right\rangle , \left\langle u _ {2}, a _ {2} \right\rangle , \dots , \left\langle u _ {n}, a _ {n} \right\rangle\right) = \prod_ {j = 1} ^ {n} b _ {j} ^ {\omega_ {j}}\tag{8}
$$

where $\omega = ( \omega _ { 1 } , \omega _ { 2 } , . . . , \omega _ { n } ) ^ { T }$ is an exponential weighting vector, such that $\omega _ { j } { \in } [ 0 , 1 ] , j = 1 , 2 , \ldots n .$

$\begin{array} { r } { \sum _ { j = 1 } ^ { n } \omega _ { j } = 1 , \ b _ { j } } \end{array}$ is the $a _ { i }$ value of the OWG pair $\left. \dot { u _ { i } } , \boldsymbol { a } _ { i } \right.$ having the jth largest $u _ { i } ,$ , and $u _ { i }$ in $\left. { u _ { i } , a _ { i } } \right.$ is referred to as the order inducing variable and $a _ { i }$ as the argument variable, $a _ { i } { \in } R ^ { + } , i { = } 1 , 2 , . . . , n , R ^ { + }$ is the set of all the positive real numbers. Especially, if $\omega { = } ( 1 / n , 1 / n , . . . . , 1 / n ) ^ { T } ,$ , then it is reduced to the IOWG geometric mean operator; if $u _ { i } { = } a _ { i } ,$ , for all $i ,$ then IOWG is reduced to the OWG operator; if $u _ { i } { = } \mathrm { N o }$ . i, for all i, where No. i is the ordered position of the $a _ { i } ,$ then IOWG is the weighted geometric mean operator [28].

In the following, we shall develop an induced ULOWG (IULOWG) operator to accommodate the situations where the input arguments are uncertain multiplicative linguistic variables.

Definition 7. An IULOWG operator is defined as follows:

$$
\begin{array}{l} \text { IULOWG } _ {\omega} (\langle u _ {1}, \tilde {s} _ {1} \rangle , \langle u _ {2}, \tilde {s} _ {2} \rangle , \dots , \langle u _ {n}, \tilde {s} _ {n} \rangle) \\ = (\tilde {s} _ {\gamma_ {1}}) ^ {\omega_ {1}} \otimes (\tilde {s} _ {\gamma_ {2}}) ^ {\omega_ {2}} \otimes \dots \otimes (\tilde {s} _ {\gamma_ {n}}) ^ {\omega_ {n}} \end{array}\tag{9}
$$

where $\omega = \left( \omega _ { 1 } , \omega _ { 2 } , . . . , \omega _ { n } \right) ^ { T }$ is an exponential weighting vector, such that $\omega _ { j } { \in } [ 0 , 1 ] , j = 1 , 2 , \ldots ,$ $\begin{array} { r } { n , \ \sum _ { j = 1 } ^ { n } \omega _ { j } = \mathrm { ~ 1 , ~ } \tilde { s } _ { \gamma _ { j } } \mathrm { i s } } \end{array}$ the value of the ULOWG pair $\left. u _ { i } , \tilde { s } _ { i } \right.$ having the jth largest $u _ { i } ,$ and $u _ { i }$ in $\left. u _ { i } , \tilde { s } _ { i } \right.$ is referred to as the order-inducing variable and $\tilde { s } _ { i }$ as the uncertain multiplicative linguistic argument variable. Especially, if $\scriptstyle \omega = ( 1 / n , 1 / n , \ldots , 1 /$ $n ) ^ { \widecheck { T } }$ , then IULOWG is reduced to the ULGM operator; if $u _ { i } , { = } \widetilde s _ { i }$ for all $i ,$ then IULOWG is reduced to the ULOWG operator; if $u _ { i } { = } \mathrm { N o } , \ i ,$ for all i, where No. i is the ordered position of the $\tilde { s } _ { i } ,$ then IULOWG is reduced to the ULWGM operator.

However, if there is a tie between $\left. u _ { i } , \tilde { s } _ { i } \right.$ and $\langle u _ { j } , \tilde { s } _ { j } \rangle$ with respect to order-inducing variables, in this case, we can follow the policy presented by Yager and Filev [32]—to replace the arguments of the tied objects by the mean of the arguments of the tied objects [i.e., we replace the argument component of each of $\left. u _ { i } , \tilde { s } _ { i } \right.$ and $\langle u _ { j } , \tilde { s } _ { j } \rangle$ by their geometric mean $( \tilde { s } _ { i } \otimes \tilde { s } _ { j } ) ^ { 1 / 2 } ]$ . If k items are tied, we replace these by k replicas of their geometric mean.

In the following, we shall give two examples to specify the special cases with respect to the inducing variables.

Example 4. Consider the following collection of ULOWG pairs:

$$
\begin{array}{l} \langle s _ {3}, [ s _ {1 / 4}, s _ {1 / 2} ] \rangle , \langle s _ {1}, [ s _ {4}, s _ {5} ] \rangle , \langle s _ {4}, [ s _ {1 / 2}, s _ {1} ] \rangle , \\ \langle s _ {2}, [ s _ {3}, s _ {4} ] \rangle \end{array}
$$

Performing the ordering the ULOWG pairs with respect to the first component, we have:

$$
\begin{array}{l} \langle s _ {4}, [ s _ {1 / 2}, s _ {1} ] \rangle , \langle s _ {3}, [ s _ {1 / 4}, s _ {1 / 2} ] \rangle , \langle s _ {2}, [ s _ {3}, s _ {4} ] \rangle , \\ \langle s _ {1}, [ s _ {4}, s _ {5} ] \rangle \end{array}
$$

This ordering induces the ordered linguistic arguments:

$$
\begin{array}{l} \tilde {\boldsymbol {s}} _ {\gamma_ {1}} = \left[ s _ {1 / 2}, s _ {1} \right], \quad \tilde {\boldsymbol {s}} _ {\gamma_ {2}} = \left[ s _ {1 / 4}, s _ {1 / 2} \right], \quad \tilde {\boldsymbol {s}} _ {\gamma_ {3}} = \left[ s _ {3}, s _ {4} \right], \\ \tilde {\boldsymbol {s}} _ {\gamma_ {4}} = \left[ s _ {4}, s _ {5} \right] \end{array}
$$

If the weighting vector $\omega = ( 0 . 2 , 0 . 3 , 0 . 3 , 0 . 2 ) ^ { T } ;$ , then we get an aggregated value:

$$
\begin{array}{l} \text { IULOWG } _ {\omega} \big (\langle s _ {3}, [ s _ {1 / 4}, s _ {1 / 2} ] \rangle , \langle s _ {1}, [ s _ {4}, s _ {5} ] \rangle , \\ \langle s _ {4}, [ s _ {1 / 2}, s _ {1} ] \rangle , \langle s _ {2}, [ s _ {3}, s _ {4} ] \rangle \big) \\ = [ s _ {1 / 2}, s _ {1} ] ^ {0. 2} \otimes [ s _ {1 / 4}, s _ {1 / 2} ] ^ {0. 3} \otimes [ s _ {3}, s _ {4} ] ^ {0. 3} \\ \otimes [ s _ {4}, s _ {5} ] ^ {0. 2} = [ s _ {1. 0 5}, s _ {1. 7 0} ] \end{array}
$$

Example 5. Consider the following collection of ULOWG pairs:

$$
\begin{array}{l} \langle [ s _ {3}, s _ {4} ], [ s _ {1 / 4}, s _ {1 / 2} ] \rangle , \langle [ s _ {2}, s _ {4} ], [ s _ {4}, s _ {5} ] \rangle , \\ \langle [ s _ {3}, s _ {5} ], [ s _ {1 / 2}, s _ {1} ] \rangle , \langle [ s _ {1}, s _ {4} ], [ s _ {3}, s _ {4} ] \rangle \end{array}
$$

To rank the first components $u _ { i } ( i { = } 1 , 2 , 3 , 4 )$ of the ULOWG pairs, we first compare each $u _ { i }$ with all these first components $u _ { i } ( i { = } 1 , 2 , 3 , 4 )$ by using Eq. (1), and then construct a complementary matrix:

$$
\mathbf {P} = \left[ \begin{array}{c c c c} 0. 5 & 0. 6 6 6 7 & 0. 3 3 3 3 & 0. 7 5 \\ 0. 3 3 3 3 & 0. 5 & 0. 2 5 & 0. 6 \\ 0. 6 6 6 7 & 0. 7 5 & 0. 5 & 0. 8 \\ 0. 2 5 & 0. 4 & 0. 2 & 0. 5 \end{array} \right]
$$

Summing all elements in each line of matrix P, we have:

$$
\begin{array}{l} p _ {1} = 2 0. 2 5 0 0, \quad p _ {2} = 1. 6 8 3 3, \quad p _ {3} = 2. 7 1 6 7, \\ p _ {4} = 1. 3 5 0 0 \end{array}
$$

Then we rank all the arguments $u _ { i } ( i { = } 1 , 2 , 3 , 4 )$ in descending order in accordance with the values of $p _ { i } ( i { = } 1 , 2 , 3 , 4 )$

$$
u _ {3} = \left[ s _ {3}, s _ {5} \right], u _ {1} = \left[ s _ {3}, s _ {4} \right], u _ {2} = \left[ s _ {2}, s _ {4} \right], u _ {4} = \left[ s _ {1}, s _ {4} \right]
$$

Performing the ordering the ULOWG pairs with respect to the first component, we have:

$$
\begin{array}{l} \langle [ s _ {3}, s _ {5} ], [ s _ {1 / 2}, s _ {1} ] \rangle , \langle [ s _ {3}, s _ {4} ], [ s _ {1 / 4}, s _ {1 / 2} ] \rangle , \\ \langle [ s _ {2}, s _ {4} ], [ s _ {4}, s _ {5} ] \rangle , \langle [ s _ {1}, s _ {4} ], [ s _ {3}, s _ {4} ] \rangle \end{array}
$$

This ordering induces the ordered linguistic arguments: s˜<sub>c1</sub> ¼ s<sub>1=2</sub>; s<sub>1</sub> ; s˜<sub>c2</sub> ¼ s<sub>1=4</sub>; s<sub>1=2</sub> ; s˜<sub>c3</sub> ¼ ½  s<sub>4</sub>; s<sub>5</sub> ; s˜<sub>c</sub> ¼ ½  s<sub>3</sub>; s<sub>4</sub>

If the weighting vector $\omega = ( 0 . 2 , 0 . 3 , 0 . 3 , 0 . 2 ) ^ { T } ,$ , then we get an aggregated value:

$$
\begin{array}{l} \text { IULOWG } _ {\omega} \big (\langle [ s _ {3}, s _ {4} ], [ s _ {1 / 4}, s _ {1 / 2} ] \rangle , \langle [ s _ {2}, s _ {4} ], [ s _ {4}, s _ {5} ] \rangle , \\ \langle [ s _ {3}, s _ {5} ], [ s _ {1 / 2}, s _ {1} ] \rangle , \langle [ s _ {1}, s _ {4} ], [ s _ {3}, s _ {4} ] \rangle \big) \\ = [ s _ {1 / 2}, s _ {1} ] ^ {0. 2} \otimes [ s _ {1 / 4}, s _ {1 / 2} ] ^ {0. 3} \otimes [ s _ {4}, s _ {5} ] ^ {0. 3} \otimes [ s _ {3}, s _ {4} ] ^ {0. 2} \\ = [ s _ {1. 0 9}, s _ {1. 7 3} ] \end{array}
$$

The IULOWG operator has many desirable properties similar to those of the IOWG operator [28]:

Theorem 1 (Commutativity). $I U L O W G _ { \omega } ( \langle u _ { I } , \tilde { s } _ { I } \rangle$ $\langle u _ { 2 } , \tilde { s } _ { 2 } \rangle , . . . , \langle u _ { n } , \tilde { s } _ { n } \rangle \rangle { = } I U L O W G _ { \omega } ( \langle u _ { I } { } ^ { \prime } , \tilde { s } _ { I } { } ^ { \prime } \rangle , \langle u _ { 2 } { } ^ { \prime } { } ^ { \prime } , \tilde { s } _ { I } { } ^ { \prime } \rangle ) ,$ $\tilde { s } _ { 2 } { ' } \rangle , . . . , \langle u _ { n } { ' } , \tilde { s } _ { n } { ' } \rangle )$ w h e re $( \langle u _ { \mathit { \mathit { I } } } ^ { \prime } , \tilde { s } _ { \mathit { I } } ^ { \prime } \rangle , \quad \langle u _ { \mathit { 2 } } ^ { \prime } ,$ $\tilde { s } _ { 2 } { ' } \rangle , . . . , \langle u _ { n } ^ { \prime } , \tilde { s } _ { n } { ' } \rangle )$ is any permutation of $\ d ( \langle u _ { I } , \tilde { s } _ { I } \rangle$ $\left. \boldsymbol { u } _ { 2 } , \tilde { s } _ { 2 } \right. , \ldots . . , \left. \boldsymbol { u } _ { n } , \tilde { s } _ { n } \right. )$

Theorem 2 (Idempotency). If s˜<sub>j</sub>=s˜, for all j, then: IULOWG<sub>x</sub>ð Þ ¼ hu<sub>1</sub>; s˜<sub>1</sub>i; hu<sub>2</sub>; s˜<sub>2</sub>i; . . . ; hu<sub>n</sub>; s˜<sub>n</sub>i s˜

Theorem 3 (Monotonicity). $I f \tilde { s } _ { j } { \le } \tilde { s } _ { j } ^ { \prime }$ , for all j, then: $I U L O W G _ { j } ( \langle u _ { 1 } , \tilde { s } _ { 1 } \rangle , \langle u _ { 2 } , \tilde { s } _ { 2 } \rangle , \dots , \langle u _ { n } , \tilde { s } _ { n } \rangle ) { \le } I U L O W G _ { \omega }$ ð Þ hu<sub>1</sub>; s˜<sub>1</sub>Vi; hu<sub>2</sub>; s˜<sub>2</sub>Vi; . . . ; hu<sub>n</sub>; s˜<sub>n</sub>Vi

## 4. An approach to group decision making with uncertain multiplicative linguistic preference relations

Consider a group decision-making problem with uncertain linguistic preference information. Let $X = \{ x _ { 1 } , x _ { 2 } , . ~ . ~ . , x _ { n } \}$ be the set of alternatives, and $D { = } \{ d _ { 1 } , d _ { 2 } , . . . . , d _ { n } \}$ be the set of DMs. Let $\nu =$ $( \nu _ { 1 } , \nu _ { 2 } , . . . , . , r _ { m } ) ^ { T }$ be the weight vector of DMs, where $\nu _ { l } { \geq } 0 , l = 1 , 2 , \ldots , m , \sum _ { l = 1 } ^ { m } \nu _ { l } = 1$ . The DM $d _ { l } { \in } D$ compares these alternatives with respect to a single criterion by the multiplicative linguistic terms in the set $S { = } \{ s _ { \alpha } | \alpha { = } 1 / t , . . . , 1 / 2 , 1 / 2 , . . . , t \}$ , and constructs the uncertain multiplicative linguistic preference relation $\tilde { A _ { l } } { = } ( \tilde { a } _ { i j } ^ { ( l ) } ) _ { n { \times } n }$ , whose element $\widetilde { a } _ { i j } ^ { ( l ) } { = } [ a _ { i j } ^ { ( l ) } , a _ { i j } ^ { ( l ) ^ { + } } ] { \in } \widetilde { S }$ estimates the preference degree of alternative $x _ { i }$ over $x _ { j } ,$ and meets $s _ { l / t } { \le } a _ { i j } ^ { ( l ) ^ { - } } { \le } a _ { i j } ^ { ( l ) ^ { + } } { \le } s _ { t } , a _ { i j } ^ { ( l ) ^ { - } } { \otimes } a _ { j i } ^ { ( l ) ^ { + } } { = } a _ { i j } ^ { ( l ) ^ { + } } { \otimes }$ $a _ { j i } ^ { ( l ) \cdot } { = } s _ { 1 } , ~ a _ { i j } ^ { ( l ) \cdot } { = } a _ { i i } ^ { ( l ) \cdot } { = } s _ { 1 }$ , for all $l { = } 1 , 2 , . . . . , m ; ~ i ,$ $j { = } 1 , 2 , . . . . , n$

Theorem 4. Let $A _ { I } , A _ { 2 } , \ldots . A _ { m }$ be the uncertain multiplicative linguistic preference relations provided by m DMs $d _ { l } ( l { = } l , 2 , . ~ . ~ . , m )$ , where $\tilde { A _ { l } } { = } ( \tilde { a } _ { i j } ^ { ( l ) } ) _ { n { \times } n } ,$ $\begin{array} { r } { \tilde { a } _ { i j } ^ { \oslash } { \in } \tilde { S } ( l { = } l , 2 , . . . , m ; ~ i , j { = } l , 2 , . . . , n ) , } \end{array}$ , then their collective linguistic preference relation $\tilde { A _ { l } } { = } ( \tilde { a } _ { i j } ) _ { n { \times } n }$ is also an uncertain multiplicative linguistic preference relation with:

$$
\begin{array}{l} \tilde {\boldsymbol {a}} _ {i j} = I O L O W G _ {\omega} \Big (\langle v _ {1}, \tilde {\boldsymbol {a}} _ {i j} ^ {(1)} \rangle , \langle v _ {2}, \tilde {\boldsymbol {a}} _ {i j} ^ {(2)} \rangle , \dots , \langle v _ {m}, \tilde {\boldsymbol {a}} _ {i j} ^ {(m)} \rangle \Big) \\ = \Big (\tilde {\boldsymbol {b}} _ {i j} ^ {(1)} \Big) ^ {\omega_ {1}} \otimes \Big (\tilde {\boldsymbol {b}} _ {i j} ^ {(2)} \Big) ^ {\omega_ {2}} \otimes \dots \otimes \Big (\tilde {\boldsymbol {b}} _ {i j} ^ {(m)} \Big) ^ {\omega_ {m}} \end{array}
$$

where $\tilde { b } _ { i j } ^ { ( k ) }$ is the $\tilde { a } _ { i j } ^ { \ : ( l ) }$ value of the UOWG pair $\langle \nu _ { l } ,$ $\tilde { a } _ { i j } { } ^ { ( l ) } \rangle$ having the kth largest $\nu _ { l } ,$ with $\widetilde { a } _ { i j } { = } \ / L \widetilde { a } _ { i j } ^ { - } , \widetilde { a } _ { i j } ^ { + } \ / J { \in } \widetilde { S } ,$ $s _ { I / t } \le a _ { i j } ^ { - } \le a _ { i j } ^ { + } \le s _ { t } , \ : a _ { i j } ^ { - } \otimes a _ { i j } ^ { + } = a _ { i j } ^ { + } \otimes a _ { i j } ^ { - } = s _ { I } , \ : a _ { i i } ^ { - } = a _ { i i } ^ { + } = s _ { I } ,$ for all $l = 1 , 2 , . . . , m ; ~ i , \ j = I , 2 , . . . , n .$

Proof. Since $A _ { 1 } , A _ { 2 } , . . . . A _ { m }$ are the uncertain multiplicative linguistic preference relations, we have $s _ { l / t } \le a _ { i j } ^ { ( l ) ^ { - } } \le a _ { i j } ^ { \smile } ( l ) ^ { + } \le s _ { t } , \quad a _ { i j } ^ { ( l ) ^ { - } } \otimes a _ { j i } ^ { ( l ) ^ { + } } = a _ { i j } ^ { ( l ) ^ { + } } \otimes a _ { j i } ^ { ( l ) ^ { - } } = s _ { 1 } ,$ $a _ { i i } ^ { ( l ) } { = } a _ { i i } ^ { ( l ) ^ { + } } { = } s _ { 1 }$ , for all $l { = } 1 , 2 , . . . . , m ; i , j { = } 1 , 2 , . . . , n$ and then:

$$
\begin{array}{l} \tilde {\boldsymbol {a}} _ {i j} = \text { IULOWG } _ {\omega} \Big (\langle v _ {1}, \tilde {\boldsymbol {a}} _ {i j} ^ {(1)} \rangle , \langle v _ {2}, \tilde {\boldsymbol {a}} _ {i j} ^ {(2)} \rangle , \ldots , \langle v _ {m}, \tilde {\boldsymbol {a}} _ {i j} ^ {(m)} \rangle \Big) \\ = \left(\tilde {\boldsymbol {b}} _ {i j} ^ {(1)}\right) ^ {\omega_ {1}} \otimes \left(\tilde {\boldsymbol {b}} _ {i j} ^ {(2)}\right) ^ {\omega_ {2}} \otimes \dots \otimes \left(\tilde {\boldsymbol {b}} _ {i j} ^ {(m)}\right) ^ {\omega_ {m}} \end{array}
$$

It follows that:

$$
\begin{array}{l} a _ {i j} ^ {-} = \left(\tilde {\boldsymbol {b}} _ {i j} ^ {(1) ^ {-}}\right) ^ {\omega_ {1}} \otimes \left(\tilde {\boldsymbol {b}} _ {i j} ^ {(2) ^ {-}}\right) ^ {\omega_ {2}} \otimes \dots \otimes \left(\tilde {\boldsymbol {b}} _ {i j} ^ {(m) ^ {-}}\right) ^ {\omega_ {m}} \\ \geq \left(s _ {1 / t}\right) ^ {\omega_ {1}} \otimes \left(s _ {1 / t}\right) ^ {\omega_ {2}} \otimes \dots \otimes \left(s _ {1 / t}\right) ^ {\omega_ {m}} \\ = \left(s _ {1 / t}\right) \sum_ {l = 1} ^ {m} \omega_ {l} = s _ {1 / t}, \end{array}
$$

for all $i , j = 1 , 2 , \ldots , n$

$$
\begin{array}{l} a _ {i j} ^ {+} = \left(\tilde {\boldsymbol {b}} _ {i j} ^ {(1) ^ {+}}\right) ^ {\omega_ {1}} \otimes \left(\tilde {\boldsymbol {b}} _ {i j} ^ {(2) ^ {+}}\right) ^ {\omega_ {2}} \otimes \dots \otimes \left(\tilde {\boldsymbol {b}} _ {i j} ^ {(m) ^ {+}}\right) ^ {\omega_ {m}} \\ \leq (s _ {t}) ^ {\omega_ {1}} \otimes (s _ {t}) ^ {\omega_ {2}} \otimes \dots \otimes (s _ {t}) ^ {\omega_ {m}} = (s _ {t}) \sum_ {l = 1} ^ {m} \omega_ {l} = s _ {t}, \end{array}
$$

for all $i , j = 1 , 2 , \ldots , n$

$$
\begin{array}{l} a _ {i j} ^ {-} = \left(\tilde {\boldsymbol {b}} _ {i j} ^ {(1) ^ {-}}\right) ^ {\omega_ {1}} \otimes \left(\tilde {\boldsymbol {b}} _ {i j} ^ {(2) ^ {-}}\right) ^ {\omega_ {2}} \otimes \dots \otimes \left(\tilde {\boldsymbol {b}} _ {i j} ^ {(m) ^ {-}}\right) ^ {\omega_ {m}} \\ \leq \left(\tilde {\boldsymbol {b}} _ {i j} ^ {(1) ^ {+}}\right) ^ {\omega_ {1}} \otimes \left(\tilde {\boldsymbol {b}} _ {i j} ^ {(2) ^ {+}}\right) ^ {\omega_ {2}} \otimes \dots \otimes \left(\tilde {\boldsymbol {b}} _ {i j} ^ {(m) ^ {+}}\right) ^ {\omega_ {m}} = a _ {i j} ^ {+} \end{array}
$$

$$
\begin{array}{l} a _ {i j} ^ {-} \otimes a _ {j i} ^ {+} = \left(\tilde {\boldsymbol {b}} _ {i j} ^ {(1) ^ {-}}\right) ^ {\omega_ {1}} \otimes \left(\tilde {\boldsymbol {b}} _ {i j} ^ {(2) ^ {-}}\right) ^ {\omega_ {2}} \otimes \dots \otimes \left(\tilde {\boldsymbol {b}} _ {i j} ^ {(m) ^ {-}}\right) ^ {\omega_ {m}} \\ \qquad \otimes (\tilde {\boldsymbol {b}} _ {j i} ^ {(1) ^ {+}}) ^ {\omega_ {1}} \otimes \left(\tilde {\boldsymbol {b}} _ {j i} ^ {(2) ^ {+}}\right) ^ {\omega_ {2}} \otimes \dots \otimes \left(\tilde {\boldsymbol {b}} _ {j i} ^ {(m) ^ {+}}\right) ^ {\omega_ {m}} \\ = \left(\tilde {\boldsymbol {b}} _ {i j} ^ {(1) ^ {-}} \otimes \tilde {\boldsymbol {b}} _ {j i} ^ {(1) ^ {+}}\right) ^ {\omega_ {1}} \otimes \left(\tilde {\boldsymbol {b}} _ {j i} ^ {(2) ^ {-}} \otimes \tilde {\boldsymbol {b}} _ {j i} ^ {(2) ^ {+}}\right) ^ {\omega_ {2}} \\ \qquad \otimes \dots \otimes \left(\tilde {\boldsymbol {b}} _ {i j} ^ {(m) ^ {-}} \otimes \tilde {\boldsymbol {b}} _ {j i} ^ {(m) ^ {+}}\right) ^ {\omega_ {m}} \\ = (s _ {1}) ^ {\omega_ {1}} \otimes (s _ {1}) ^ {\omega_ {2}} \otimes \dots \otimes (s _ {1}) ^ {\omega_ {m}} \\ = (s _ {1}) \sum_ {l = 1} ^ {m} \omega_ {l} = s _ {1}, \end{array}
$$

for all $i , j = 1 , 2 , \ldots , n$

$$
\begin{array}{l} a _ {i j} ^ {+} \otimes a _ {j i} ^ {-} = \left(\tilde {\boldsymbol {b}} _ {i j} ^ {(1) ^ {+}}\right) ^ {\omega_ {1}} \otimes \left(\tilde {\boldsymbol {b}} _ {i j} ^ {(2) ^ {+}}\right) ^ {\omega_ {2}} \otimes \dots \otimes \left(\tilde {\boldsymbol {b}} _ {i j} ^ {(m) ^ {+}}\right) ^ {\omega_ {m}} \\ \qquad \otimes \left(\tilde {\boldsymbol {b}} _ {j i} ^ {(1) ^ {-}}\right) ^ {\omega_ {1}} \otimes \left(\tilde {\boldsymbol {b}} _ {j i} ^ {(2) ^ {-}}\right) ^ {\omega_ {2}} \otimes \ldots \otimes \left(\tilde {\boldsymbol {b}} _ {j i} ^ {(m) ^ {-}}\right) ^ {\omega_ {m}} \\ = \left(\tilde {\boldsymbol {b}} _ {i j} ^ {(1) ^ {+}} \otimes \tilde {\boldsymbol {b}} _ {j i} ^ {(1) ^ {-}}\right) ^ {\omega_ {1}} \otimes \left(\tilde {\boldsymbol {b}} _ {j i} ^ {(2) ^ {+}} \otimes \tilde {\boldsymbol {b}} _ {j i} ^ {(2) ^ {-}}\right) ^ {\omega_ {2}} \\ \qquad \otimes \dots \otimes \left(\tilde {\boldsymbol {b}} _ {i j} ^ {(m) ^ {+}} \otimes \tilde {\boldsymbol {b}} _ {j i} ^ {(m) ^ {-}}\right) ^ {\omega_ {m}} \\ = (s _ {1}) ^ {\omega_ {1}} \otimes (s _ {1}) ^ {\omega_ {2}} \otimes \dots \otimes (s _ {1}) ^ {\omega_ {m}} \\ = (s _ {1}) \sum_ {l = 1} ^ {m} \omega_ {l} = s _ {1}, \end{array}
$$

for all $i , j = 1 , 2 , \ldots , n$

$$
\begin{array}{l} a _ {i i} ^ {-} = \left(\tilde {\boldsymbol {b}} _ {i i} ^ {(1) ^ {-}}\right) ^ {\omega_ {1}} \otimes \left(\tilde {\boldsymbol {b}} _ {i i} ^ {(2) ^ {-}}\right) ^ {\omega_ {2}} \otimes \dots \otimes \left(\tilde {\boldsymbol {b}} _ {i i} ^ {(m) ^ {-}}\right) ^ {\omega_ {m}} \\ = (s _ {1}) ^ {\omega_ {1}} \otimes (s _ {1}) ^ {\omega_ {2}} \otimes \dots \otimes (s _ {1}) ^ {\omega_ {m}} = (s _ {1}) \sum_ {l = 1} ^ {m} \omega_ {l} = s _ {1}, \end{array}
$$

for all $i , j = 1 , 2 , \ldots , n$

$$
\begin{array}{l} a _ {i i} ^ {+} = \left(\tilde {\boldsymbol {b}} _ {i i} ^ {(1) ^ {+}}\right) ^ {\omega_ {1}} \otimes \left(\tilde {\boldsymbol {b}} _ {i i} ^ {(2) ^ {+}}\right) ^ {\omega_ {2}} \otimes \dots \otimes \left(\tilde {\boldsymbol {b}} _ {i i} ^ {(m) ^ {+}}\right) ^ {\omega_ {m}} \\ = (s _ {1}) ^ {\omega_ {1}} \otimes (s _ {1}) ^ {\omega_ {2}} \otimes \dots \otimes (s _ {1}) ^ {\omega_ {m}} = (s _ {1}) \sum_ {l = 1} ^ {m} \omega_ {l} = s _ {1}, \end{array}
$$

for all $i , j = 1 , 2 , . . . , n$

Thus, $\tilde { A }$ is an uncertain multiplicative linguistic preference relation, which completes the proof of Theorem 4.

In the following, we shall develop an approach based on the ULOWG and IULOWG operators to group decision making with uncertain multiplicative linguistic preference relations.

Step 1. For a group decision-making problem with uncertain linguistic preference information. Let $X { = } \{ x _ { 1 } , x _ { 2 } , . ~ . ~ . , x _ { n } \}$ be the set of alternatives, and $D { = } \{ d _ { 1 } , d _ { 2 } , . . . . , d _ { m } \}$ be the set of DMs. Let $\pmb { \nu } \mathrm { = } ( \nu _ { 1 } , \nu _ { 2 } , \ldots . , \nu _ { m } ) ^ { T }$ be the weight vector of DMs, where $\nu _ { l } { \geq } 0 , \quad l = 1 , 2 , \ldots , m , \quad \sum _ { l = 1 } ^ { m } \nu _ { l } = 1$ . The DM $d _ { l } { \in } D$ compares these alternatives with respect to a single criterion by the multiplicative linguistic labels in $S ,$ , and constructs the uncertain multiplicative linguistic preference relation $A _ { l } { = } ( \tilde { a } _ { i j } ^ { ( l ) } ) _ { n { \times } n } ,$ where $\tilde { a } _ { i j } ^ { \enspace \enspace \tilde { ( l ) } } { = } [ a _ { i j } ^ { \enspace ( l ) ^ { - } } , \acute { a } _ { i j } ^ { \enspace ( l ) ^ { + } } ] { \in } \tilde { S } , s _ { l / t } { \le } a _ { i j } ^ { \enspace ( l ) ^ { - } } { \le }$ $\begin{array} { r l } { a _ { i j } ^ { ( l ) ^ { + } } { \preceq } s _ { t } , } & { a _ { i j } ^ { ( l ) ^ { - } } { \otimes } a _ { j i } ^ { ( l ) ^ { + } } { = } a _ { i j } ^ { ^ { ( l ) ^ { + } } } { \otimes } a _ { j i } ^ { ^ { ( l ) ^ { - } } } { = } s _ { 1 } , \quad a _ { i i } ^ { ( l ) ^ { - } } { = } a _ { i i } ^ { ^ { ( l ) ^ { + } } } { = } s _ { 1 } , } \end{array}$ for all $l { = } 1 , 2 , . . . , m ; ~ i , ~ j { = } 1 , 2 , . . . , n .$

Step 2. Utilize the IULOWG operator:

$$
\tilde {\boldsymbol {a}} _ {i j} = \operatorname{IULOWG} _ {\omega} \left(\left\langle v _ {1}, \tilde {\boldsymbol {a}} _ {i j} ^ {(1)} \right\rangle , \left\langle v _ {2}, \tilde {\boldsymbol {a}} _ {i j} ^ {(2)} \right\rangle , \dots , \left\langle v _ {m}, \tilde {\boldsymbol {a}} _ {i j} ^ {(m)} \right\rangle\right),
$$

$$
i, j = 1, 2, \dots , n
$$

to aggregate all the uncertain multiplicative linguistic preference relations $A _ { l } \mathsf { = } ( \tilde { a } _ { i j } ^ { ( l ) } ) _ { n \times n } ~ ( l \mathsf { = } 1 , 2 , . . . , m )$ into a collective uncertain multiplicative linguistic preference relation $\scriptstyle \tilde { A } = ( \tilde { a } _ { i j } ) _ { n \times n } ,$ where ${ \omega } = \left( \omega _ { 1 } , \omega _ { 2 } , . . . , \omega _ { n } \right) ^ { T }$ is the exponential weighting vector associated with the IULOWG operator, such that $\omega _ { j } { \in } [ 0 , I ] , \ j { = } I , 2 , . . . , n ,$ and $\textstyle \sum _ { j = 1 } ^ { m } \omega _ { j } = 1$

Step 3. Utilize the ULOWG operator:

$$
\tilde {a} _ {i} = \operatorname{ULOWG} _ {\omega^ {\prime}} \left(\tilde {a} _ {i 1}, \tilde {a} _ {i 2}, \dots , \tilde {a} _ {i n}\right), \quad i = 1, 2, \dots , n
$$

to aggregate $\tilde { a } _ { i j }$ corresponding to the alternative $x _ { i } ,$ and then get the collective uncertain linguistic preference degree $\widetilde { a } _ { i } ( j { = } 1 , 2 , . . . , n )$ of the ith alternative over all the other alternatives, where $\omega ^ { \prime } \mathrm { = } ( \omega _ { 1 } ^ { \prime } , \omega _ { 2 } ^ { \prime } , . . . , \omega _ { n } ^ { \prime } ) ^ { T }$ is the exponential weighting vector associated with the ULOWG operator, such that $\begin{array} { r } { \omega _ { j } { ' } { \in } [ 0 , 1 ] , \sum _ { i = 1 } ^ { n } \omega _ { j } { ' } = 1 } \end{array}$

Step 4. To rank these collective preference degrees $\widetilde { a } _ { j } ( j { = } 1 , 2 , . . . . , n )$ , we first compare each $\tilde { a } _ { i }$ with all $\bar { a } _ { j } ( j { = } 1 , 2 , . . . , n )$ by using Eq. (1). For simplicity, we let $p _ { i j } { = } p ( \tilde { a } _ { i } { \geq } \tilde { a } _ { j } )$ , then we develop a complementary matrix as $\scriptstyle \mathbf { P } = ( p _ { i j } ) _ { n \times n } ,$ , where:

$p _ { i j } \ge 0 , p _ { i j } + p _ { j i } = 1 , p _ { i i } = 0 . 5 , i , j = 1 , 2 , . . . , n$ Summing all elements in each line of matrix $\mathbf { P } ,$ we have:

$$
p _ {i} = \sum_ {j = 1} ^ {n} p _ {i j}, \quad i = 1, 2, \dots , n
$$

Then we rank the $\widetilde { a } _ { i } ( i { = } 1 , 2 , . . . . , n )$ in descending order in accordance with the values of $p _ { i } ( i { = } 1 , 2 , . . . , n )$ .

Step 5. Rank all the alternatives $x _ { i } ( i { = } 1 , 2 , \ldots . . , n )$ and select the best one(s) in accordance with the $\widetilde { a } _ { i } ( i { = } 1 , 2 , . ~ . . , n )$

Step 6. End.

## 5. Illustrative example

Let us suppose that there is an investment company, which wants to invest a sum of money in the best option (adapted from Ref. [13]). There is a panel with five possible alternatives in which to invest the money:

1) $x _ { 1 }$ is a car industry.

2) $x _ { 2 }$ is a food company.

3) $x _ { 3 }$ is a computer company.

4) $x _ { 4 }$ is an arms company.

5) $x _ { 5 }$ is a TV company.

One main criterion used is growth analysis. There are three DMs $d _ { l } ( l { = } 1 , 2 , 3 )$ , whose weight vector $\nu \mathrm { = } ( 0 . 2 , 0 . 5 , 0 3 ) ^ { T }$ . If the DMs are familiar with Saaty’s analytic hierarchy process (AHP) and can compare these five companies with respect to the criterion growth analysis by using a one-to-nine scale [18], then we suppose that the DMs construct, respectively, the multiplicative numerical preference relations $R _ { l } { = } ( r _ { i j } ^ { ( l ) } ) _ { 5 \times 5 } ~ ( l { = } 1 , 2 , 3 )$ (see Tables 1–3).

To get the most desirable alternative(s), we first utilize the weighted geometric mean (WGM) operator:

$$
\begin{array}{l} r _ {i j} = \mathrm{WGM} _ {\nu} \left(r _ {i j} ^ {(1)}, r _ {i j} ^ {(2)}, r _ {i j} ^ {(3)}\right) \\ = \left(r _ {i j} ^ {(1)}\right) ^ {\nu_ {1}} \left(r _ {i j} ^ {(2)}\right) ^ {\nu_ {2}} \left(r _ {i j} ^ {(3)}\right) ^ {\nu_ {3}}, \quad i, j = 1, 2, 3, 4, 5 \end{array}
$$

to aggregate all the multiplicative numerical preference relations $R _ { l } { = } ( r _ { i j } ^ { ( l ) } ) _ { 5 \times 5 } ( l { = } 1 , 2 , 3 )$ into the collective multiplicative numerical preference relation $R = ( r _ { i j } ) _ { 5 \times 5 }$ (see Table 4).Then, by the famous eigenvector method (EM) [18], we get the normalized principal right eigenvector $\pmb { w } = ( w _ { 1 } , w _ { 2 } , . . . , w _ { 5 } ) ^ { T }$ as follows:

Table 1  
The multiplicative numerical preference relation $R _ { 1 }$

<table><tr><td></td><td> $x_{1}$ </td><td> $x_{2}$ </td><td> $x_{3}$ </td><td> $x_{4}$ </td><td> $x_{5}$ </td></tr><tr><td> $x_{1}$ </td><td>1</td><td>3</td><td>1/3</td><td>5</td><td>1/3</td></tr><tr><td> $x_{2}$ </td><td>1/3</td><td>1</td><td>3</td><td>3</td><td>1/3</td></tr><tr><td> $x_{3}$ </td><td>3</td><td>1/3</td><td>1</td><td>4</td><td>5</td></tr><tr><td> $x_{4}$ </td><td>1/5</td><td>1/3</td><td>1/4</td><td>1</td><td>3</td></tr><tr><td> $x_{5}$ </td><td>3</td><td>3</td><td>1/5</td><td>1/3</td><td>1</td></tr></table>

Table 2  
The multiplicative numerical preference relation $R _ { 2 }$

<table><tr><td></td><td> $x_{1}$ </td><td> $x_{2}$ </td><td> $x_{3}$ </td><td> $x_{4}$ </td><td> $x_{5}$ </td></tr><tr><td> $x_{1}$ </td><td>1</td><td>3</td><td>1</td><td>5</td><td>1</td></tr><tr><td> $x_{2}$ </td><td>1/3</td><td>1</td><td>3</td><td>4</td><td>1/3</td></tr><tr><td> $x_{3}$ </td><td>1</td><td>1/3</td><td>1</td><td>3</td><td>5</td></tr><tr><td> $x_{4}$ </td><td>1/5</td><td>1/4</td><td>1/3</td><td>1</td><td>3</td></tr><tr><td> $x_{5}$ </td><td>1</td><td>3</td><td>1/5</td><td>1/3</td><td>1</td></tr></table>

$$
\boldsymbol {w} = (0. 2 4 1 4, 0. 2 1 0 4, 0. 2 4 1 8, 0. 1 2 2 3, 0. 1 8 4 1) ^ {T}
$$

Hence, the ranking of all the alternatives $x _ { i } ( i { = } 1 , 2 , 3 , 4 , 5 )$ is:

$$
x _ {3} \succ x _ {1} \succ x _ {2} \succ x _ {5} \succ x _ {4}
$$

and thus, the most desirable alternative is $x _ { 3 }$

However, sometimes, the DMs are willing or able to provide only uncertain linguistic information because of time pressure, lack of knowledge or data, and their limited expertise related to the problem domain. In this case, we suppose that the DMs compare these five companies with respect to the criterion growth analysis by using the multiplicative linguistic scale:

$$
S = \left\{s _ {1 / 5} = \text { extremely   low }, s _ {1 / 4} = \text { very   low }, \right.
$$

$$
s _ {1 / 3} = \text { low }, s _ {1 / 2} = \text { slightly   low }, s _ {1} = \text { medium },
$$

$$
s _ {2} = \text { slightly   high }, s _ {3} = \text { high }, s _ {4} = \text { very   high },
$$

$$
s _ {5} = \text { extremely   high } \}
$$

and construct, respectively, the uncertain multiplicative linguistic preference relations $\tilde { A _ { l } } ( l { = } 1 , 2 , 3 )$ as listed in Tables 5–7.

Table 3  
The multiplicative numerical preference relation $R _ { 3 }$

<table><tr><td></td><td> $x_{1}$ </td><td> $x_{2}$ </td><td> $x_{3}$ </td><td> $x_{4}$ </td><td> $x_{5}$ </td></tr><tr><td> $x_{1}$ </td><td>1</td><td>4</td><td>2</td><td>3</td><td>1/4</td></tr><tr><td> $x_{2}$ </td><td>1/4</td><td>1</td><td>4</td><td>3</td><td>1/3</td></tr><tr><td> $x_{3}$ </td><td>1/2</td><td>1/4</td><td>1</td><td>5</td><td>3</td></tr><tr><td> $x_{4}$ </td><td>1/3</td><td>1/3</td><td>1/5</td><td>1</td><td>4</td></tr><tr><td> $x_{5}$ </td><td>4</td><td>3</td><td>1/3</td><td>1/4</td><td>1</td></tr></table>

Table 4  
The collective multiplicative numerical preference relation R

<table><tr><td></td><td> $x_{1}$ </td><td> $x_{2}$ </td><td> $x_{3}$ </td><td> $x_{4}$ </td><td> $x_{5}$ </td></tr><tr><td> $x_{1}$ </td><td>1</td><td>3.2704</td><td>0.9883</td><td>4.2896</td><td>0.5296</td></tr><tr><td> $x_{2}$ </td><td>0.3058</td><td>1</td><td>3.2704</td><td>3.4641</td><td>0.3333</td></tr><tr><td> $x_{3}$ </td><td>1.0118</td><td>0.3058</td><td>1</td><td>3.7039</td><td>4.2899</td></tr><tr><td> $x_{4}$ </td><td>0.2331</td><td>0.2887</td><td>0.2700</td><td>1</td><td>3.2704</td></tr><tr><td> $x_{5}$ </td><td>1.8882</td><td>3</td><td>0.2331</td><td>0.3058</td><td>1</td></tr></table>

As Saaty’s AHP requires a point estimate of preference from each DM in a group, it is thus unsuitable for group decision making with uncertain multiplicative linguistic preference relations. In the following, we shall utilize the approach developed in this paper to get the most desirable alternative(s):

Step 1. Utilize the IULOWG operator (let its weighting vector be w=(0.2, 06, 0.2)<sup>T</sup>)

$$
\begin{array}{l} \tilde {\boldsymbol {a}} _ {i j} = \text { IULOWG } _ {\omega} \Big (\langle v _ {1}, \tilde {\boldsymbol {a}} _ {i j} ^ {(1)} \rangle , \langle v _ {2}, \tilde {\boldsymbol {a}} _ {i j} ^ {(2)} \rangle , \langle v _ {3}, \tilde {\boldsymbol {a}} _ {i j} ^ {(3)} \rangle \Big), i, j \\ = 1, 2, 3, 4, 5 \end{array}
$$

to aggregate all the multiplicative linguistic preference relations $\tilde { A } _ { l } { = } ( \tilde { a } _ { i j } ^ { ( l ) } ) _ { 5 \times 5 } \ \ : \ : ( \bar { l } { = } 1 , 2 , 3 )$ into the collective uncertain multiplicative linguistic preference relation $\tilde { A } { = } ( \tilde { a } _ { i j } ) _ { 5 { \times } 5 }$ (see Table 8).

Step 2. Utilize the ULOWG operator [let its weighting vector be $\omega ^ { \prime } \mathrm { = } ( 0 . 1 5 , 0 2 , 0 . 3 , 0 . 2 , 0 . 1 5 ) ^ { T } ]$

$$
\tilde {\boldsymbol {a}} _ {i} = \mathrm{ULOWG} _ {\omega} (\tilde {\boldsymbol {a}} _ {i 1}, \tilde {\boldsymbol {a}} _ {i 2}, \tilde {\boldsymbol {a}} _ {i 3}, \tilde {\boldsymbol {a}} _ {i 4}, \tilde {\boldsymbol {a}} _ {i 5})
$$

to aggregate $\tilde { a } _ { i j } ( j { = } 1 , 2 , 3 , 4 , 5 )$ corresponding to the alternative $x _ { i } ,$ and then get the collective uncertain linguistic preference degree $\tilde { a } _ { i }$ of the ith alternative over all the other alternatives:

$$
\begin{array}{l} \tilde {\boldsymbol {a}} _ {1} = [ s _ {1}, s _ {1. 3 4} ], \quad \tilde {\boldsymbol {a}} _ {2} = [ s _ {0. 9 0}, s _ {1. 1 4} ], \quad \tilde {\boldsymbol {a}} _ {3} = [ s _ {1. 2 7}, s _ {1. 8 3} ], \\ \tilde {\boldsymbol {a}} _ {4} = [ s _ {0. 4 9}, s _ {0. 6 4} ], \qquad \tilde {\boldsymbol {a}} _ {5} = [ s _ {0. 8 3}, s _ {1. 0 4} ] \end{array}
$$

Step 3. To rank these collective preference degrees $\tilde { a } _ { i } ( i { = } 1 , 2 , 3 , 4 , 5 )$ , we first compare each $\tilde { a } _ { i }$ with all $\tilde { a } _ { i } ( i { = } 1 , 2 , 3 , 4 , 5 )$ by using Eq. (1), and then develop a complementary matrix:

The uncertain multiplicative linguistic preference relation $\tilde { A _ { 1 } }$

<table><tr><td></td><td> $x_{1}$ </td><td> $x_{2}$ </td><td> $x_{3}$ </td><td> $x_{4}$ </td><td> $x_{5}$ </td></tr><tr><td> $x_{1}$ </td><td> $[s_{1},s_{1}]$ </td><td> $[s_{3},s_{4}]$ </td><td> $[s_{1/4},s_{1/2}]$ </td><td> $[s_{4},s_{5}]$ </td><td> $[s_{1/3},s_{1/2}]$ </td></tr><tr><td> $x_{2}$ </td><td> $[s_{1/4},s_{1/3}]$ </td><td> $[s_{1},s_{1}]$ </td><td> $[s_{3},s_{4}]$ </td><td> $[s_{3},s_{4}]$ </td><td> $[s_{1/4},s_{1/2}]$ </td></tr><tr><td> $x_{3}$ </td><td> $[s_{2},s_{4}]$ </td><td> $[s_{1/4},s_{1/3}]$ </td><td> $[s_{1},s_{1}]$ </td><td> $[s_{3},s_{4}]$ </td><td> $[s_{4},s_{5}]$ </td></tr><tr><td> $x_{4}$ </td><td> $[s_{1/5},s_{1/4}]$ </td><td> $[s_{1/4},s_{1/3}]$ </td><td> $[s_{1/4},s_{1/3}]$ </td><td> $[s_{1},s_{1}]$ </td><td> $[s_{3},s_{4}]$ </td></tr><tr><td> $x_{5}$ </td><td> $[s_{2},s_{3}]$ </td><td> $[s_{2},s_{4}]$ </td><td> $[s_{1/5},s_{1/4}]$ </td><td> $[s_{1/4},s_{1/3}]$ </td><td> $[s_{1},s_{1}]$ </td></tr></table>

Table 6  
The uncertain multiplicative linguistic preference relation ${ \tilde { A } } _ { 2 }$

<table><tr><td></td><td> $x_{1}$ </td><td> $x_{2}$ </td><td> $x_{3}$ </td><td> $x_{4}$ </td><td> $x_{5}$ </td></tr><tr><td> $x_{1}$ </td><td> $[s_{1},s_{1}]$ </td><td> $[s_{3},s_{4}]$ </td><td> $[s_{1/2},s_{1}]$ </td><td> $[s_{4},s_{5}]$ </td><td> $[s_{1/2},s_{1}]$ </td></tr><tr><td> $x_{2}$ </td><td> $[s_{1/4},s_{1/3}]$ </td><td> $[s_{1},s_{1}]$ </td><td> $[s_{3},s_{4}]$ </td><td> $[s_{3},s_{4}]$ </td><td> $[s_{1/4},s_{1/3}]$ </td></tr><tr><td> $x_{3}$ </td><td> $[s_{1},s_{2}]$ </td><td> $[s_{1/4},s_{1/3}]$ </td><td> $[s_{1},s_{1}]$ </td><td> $[s_{2},s_{4}]$ </td><td> $[s_{4},s_{5}]$ </td></tr><tr><td> $x_{4}$ </td><td> $[s_{1/5},s_{1/4}]$ </td><td> $[s_{1/4},s_{1/3}]$ </td><td> $[s_{1/4},s_{1/2}]$ </td><td> $[s_{1},s_{1}]$ </td><td> $[s_{3},s_{4}]$ </td></tr><tr><td> $x_{5}$ </td><td> $[s_{1},s_{1/2}]$ </td><td> $[s_{3},s_{4}]$ </td><td> $[s_{1/5},s_{1/4}]$ </td><td> $[s_{1/4},s_{1/3}]$ </td><td> $[s_{1},s_{1}]$ </td></tr></table>

$$
\mathbf {P} = \left[ \begin{array}{c c c c c} 0. 5 & 0. 7 5 8 6 & 0. 0 7 7 8 & 1 & 0. 9 2 7 3 \\ 0. 2 4 1 4 & 0. 5 & 0 & 1 & 0. 6 8 8 9 \\ 0. 9 2 2 2 & 1 & 0. 5 & 1 & 1 \\ 0 & 0 & 0 & 0. 5 & 0 \\ 0. 0 7 2 7 & 0. 3 1 1 1 & 0 & 1 & 0. 5 \end{array} \right]
$$

Summing all elements in each line of matrix P, we have:

$$
\begin{array}{l} p _ {1} = 3. 2 6 3 7, \quad p _ {2} = 2. 4 3 0 3, \quad p _ {3} = 4. 4 2 2 2, \\ p _ {4} = 0. 5, \quad p _ {5} = 1. 8 8 3 8 \end{array}
$$

Then we rank $\tilde { a } _ { i } ( i { = } 1 , 2 , 3 , 4 , 5 )$ in descending order in accordance with the values of $p _ { i } ( i { = } 1 , 2 , 3 , 4 , 5 )$ :

$$
\tilde {a} _ {3} > \tilde {a} _ {1} > \tilde {a} _ {2} > \tilde {a} _ {5} > \tilde {a} _ {4}
$$

Step 4. Rank all the alternatives $x _ { i } ( i { = } 1 , 2 , 3 , 4 , 5 )$ in accordance with $\tilde { a } _ { i } ( i { = } 1 , 2 , 3 , 4 , 5 )$ , and we have:

$$
x _ {3} \succ x _ {1} \succ x _ {2} \succ x _ {5} \succ x _ {4}
$$

and thus, the most desirable alternative is x<sub>3</sub>.

At present, there is no other approach for dealing with group decision making with uncertain multiplicative linguistic preference relations. The approach developed in this paper is very suitable for solving this issue because the ULOWG operator combines the uncertain multiplicative linguistic variables giving weights to the values in relation to their ordering position, diminishing the importance of extreme values by increasing the importance of central ones. The IULOWG operator allows the introduction of semantics or meaning in the aggregation of uncertain multiplicative linguistic variables, and therefore allows for better control over the aggregation stage developed in the resolution process. Furthermore, by using a formula for comparing uncertain linguistic variables, all pairwise comparisons information about the collective uncertain linguistic preference degrees of each alternative over all the other alternatives is included in a complementary matrix and no loss of information is produced; hence, the final results are precise and rational. These arguments have just been demonstrated with the theoretical analysis and the numerical results above.

Table 7  
The uncertain multiplicative linguistic preference relation ${ \tilde { A } } _ { 3 }$

<table><tr><td></td><td> $x_{1}$ </td><td> $x_{2}$ </td><td> $x_{3}$ </td><td> $x_{4}$ </td><td> $x_{5}$ </td></tr><tr><td> $x_{1}$ </td><td> $[s_{1},s_{1}]$ </td><td> $[s_{3},s_{4}]$ </td><td> $[s_{1/2},s_{1}]$ </td><td> $[s_{2},s_{3}]$ </td><td> $[s_{1/5},s_{1/4}]$ </td></tr><tr><td> $x_{2}$ </td><td> $[s_{1/4},s_{1/3}]$ </td><td> $[s_{1},s_{1}]$ </td><td> $[s_{3},s_{5}]$ </td><td> $[s_{3},s_{4}]$ </td><td> $[s_{1/4},s_{1/3}]$ </td></tr><tr><td> $x_{3}$ </td><td> $[s_{1},s_{2}]$ </td><td> $[s_{1/5},s_{1/3}]$ </td><td> $[s_{1},s_{1}]$ </td><td> $[s_{4},s_{5}]$ </td><td> $[s_{3},s_{4}]$ </td></tr><tr><td> $x_{4}$ </td><td> $[s_{1/3},s_{1/2}]$ </td><td> $[s_{1/4},s_{1/3}]$ </td><td> $[s_{1/5},s_{1/4}]$ </td><td> $[s_{1},s_{1}]$ </td><td> $[s_{4},s_{5}]$ </td></tr><tr><td> $x_{5}$ </td><td> $[s_{4},s_{5}]$ </td><td> $[s_{3},s_{4}]$ </td><td> $[s_{1/4},s_{1/3}]$ </td><td> $[s_{1/5},s_{1/4}]$ </td><td> $[s_{1},s_{1}]$ </td></tr></table>

The collective uncertain multiplicative linguistic preference relation A<sup>˜</sup>

<table><tr><td></td><td> $x_{1}$ </td><td> $x_{2}$ </td><td> $x_{3}$ </td><td> $x_{4}$ </td><td> $x_{5}$ </td></tr><tr><td> $x_{1}$ </td><td> $[s_{1},s_{1}]$ </td><td> $[s_{3},s_{4}]$ </td><td> $[s_{0.44},s_{0.87}]$ </td><td> $[s_{2.64},s_{3.68}]$ </td><td> $[s_{0.27},s_{0.38}]$ </td></tr><tr><td> $x_{2}$ </td><td> $[s_{0.25},s_{0.33}]$ </td><td> $[s_{1},s_{1}]$ </td><td> $[s_{3},s_{4.57}]$ </td><td> $[s_{3},s_{4}]$ </td><td> $[s_{0.25},s_{0.36}]$ </td></tr><tr><td> $x_{3}$ </td><td> $[s_{1.15},s_{2.27}]$ </td><td> $[s_{0.22},s_{0.33}]$ </td><td> $[s_{1},s_{1}]$ </td><td> $[s_{3.29},s_{4.57}]$ </td><td> $[s_{3.37},s_{4.37}]$ </td></tr><tr><td> $x_{4}$ </td><td> $[s_{0.27},s_{0.38}]$ </td><td> $[s_{0.25},s_{0.33}]$ </td><td> $[s_{0.22},s_{0.30}]$ </td><td> $[s_{1},s_{1}]$ </td><td> $[s_{3.57},s_{5}]$ </td></tr><tr><td> $x_{5}$ </td><td> $[s_{2.63},s_{3.70}]$ </td><td> $[s_{2.78},s_{4}]$ </td><td> $[s_{0.23},s_{0.30}]$ </td><td> $[s_{0.20},s_{0.28}]$ </td><td> $[s_{1},s_{1}]$ </td></tr></table>

## 6. Concluding remarks

In this paper, we have defined the concept of uncertain multiplicative linguistic preference relation and have introduced some operational laws of uncertain multiplicative linguistic variables. Some aggregation operators, including the ULGM operator, ULWGM operator, ULOWG operator, and IULOWG operator, for the uncertain linguistic information have been presented. We have utilized the IULOWG operator to aggregate the individual uncertain multiplicative preference relations into a collective uncertain multiplicative preference relation, and then utilized the ULOWG operator to aggregate the collective uncertain multiplicative preference to get the collective uncertain linguistic preference degrees. Based on the collective uncertain linguistic preference degrees, a formula for comparing uncertain linguistic variables has been used to rank all the given alternatives. Theoretical analysis and the numerical results have shown that the developed approach is straightforward and has no loss of information.

## Acknowledgements

The author is very grateful to the anonymous referees for their valuable comments and suggestions. The work was supported by China Postdoctoral Science Foundation under Project (2003034366).

## Appendix A

Herrera and Herrera-Viedma [5–7], Herrera and Verdegay [9], and Herrera et al. [10–13] presented a linguistic ordered weighted averaging (LOWA) operator, which is based on the ordered weighted averaging (OWA) operator defined by Yager [30], and on the convex combination of linguistic labels defined by Delgado et al. [4], as follows:

Let $S { = } \{ s _ { i } | i { = } 0 , 1 , . . . . , g \}$ be a finite and totally ordered label set, which must have the following characteristics: (1) the set is ordered: $s _ { i } { > } s _ { j }$ if i<sup>N</sup>j; (2) there is the negation operator: $\mathrm { n e g } ( s _ { i } ) { = } s _ { j }$ such that $\mathrm { } j = g - i .$ . Let $S ^ { \prime } { = } \{ a _ { 1 } , a _ { 2 } , . ~ . ~ . , a _ { n } \}$ be a set of labels to be aggregated, where $a _ { i } { \in } S , i { = } 1 , 2 , . \ . \ . n$ , then the LOWA operator:

$$
\begin{array}{l} \text { LOWA } _ {w} (a _ {1}, a _ {2}, \ldots , a _ {n}) = w ^ {T} \delta = C ^ {n} \{w _ {k}, \delta_ {k}, \\ k = 1, 2, \ldots , n \} = w _ {1} \delta_ {1} \otimes (1 - w _ {1}) C ^ {n - 1} \{\beta_ {h}, \delta_ {h}, \\ h = 2, \ldots , n \} \end{array}
$$

where $\pmb { w } = \left\{ w _ { 1 } , w _ { 2 } , . . . , w _ { n } \right\} ^ { T }$ is a weighting vector, such that $w _ { j } \in [ 0 , 1 ] , j = 1 , 2 , . . . , \mathtt { n } ,$ and $\begin{array} { r } { \bar { \sum _ { i = 1 } ^ { n } w _ { j } } = 1 . ~ \beta _ { h } = } \end{array}$ ${ \frac { w _ { h } } { \sum _ { k = 2 } ^ { n } w _ { k } } } , \ h = 2 , \ \cdot \cdot \cdot , m _ { \cdot }$ ; and $\boldsymbol { \delta } = ( \delta _ { 1 } ^ { ' } , \delta _ { 2 } , \dots , \delta _ { n } ) ^ { T }$ is a vector associated to $S ^ { \prime }$ , such that,

$$
\delta = \sigma (S ^ {\prime}) = \left(a _ {\sigma (1)}, \dots , a _ {\sigma (n)}\right) ^ {T}
$$

where $a _ { \sigma ( j ) } { \leq } a _ { \sigma ( i ) } ,$ for all i Vj , with r being a permutation over the set of labels $S ^ { \prime } , C ^ { n }$ is the convex combination operator of m labels and if $n { = } 2$ , then it is defined as:

$$
C ^ {2} \left\{w _ {i}, \delta_ {i}, i = 1, 2 \right\} = w _ {1} s _ {j} \otimes (1 - w _ {j}) s _ {i} = s _ {k}, s _ {j}, s _ {i} \in S (j \geq i)
$$

such that:

$$
k = \min \{g, i + \operatorname{round} (w _ {1} (j - i)) \}
$$

where <sup>b</sup>round<sup>Q</sup> is the usual round operation, and $\delta _ { 1 } { = } s _ { j }$ $\delta _ { 2 } { = } s _ { i }$

If $w _ { j } { = } 1$ and $w _ { i } { = } 0$ with $i { \neq } j$ , for all i, then the convex combination is defined as:

$$
C ^ {n} \{w _ {i}, \delta_ {i}, i = 1, 2, \dots , n \} = \delta_ {j}
$$

An interesting way to compute the weights $w _ { i } ( i = 1$ $2 , \ldots , n )$ was proposed by Yager [30,31] by means of a fuzzy linguistic quantifier, which, in the case of a nondecreasing proportional fuzzy linguistic quantifier $\mathcal { Q } ,$ , is given by this expression:

$$
w _ {i} = Q \left(\frac {i}{n}\right) - Q \left(\frac {i - 1}{n}\right), \quad i = 1, 2, \dots , n
$$

being the membership function of $Q ,$ , as follows [33]:

$$
Q (r) = \left\{ \begin{array}{c l} 0, & \text { if } r <   a \\ \frac {r - a}{b - a}, & \text { if } a \leq r \leq b \\ 1, & \text { if } r > b \end{array} \right.
$$

with $a , b , r { \in } [ 0 , 1 ]$ . Some examples of nondecreasing proportional fuzzy linguistic quantifiers are [10– 12,7,13,5]: <sup>b</sup>most<sup>Q</sup> (0.3, 0.8), <sup>b</sup>at least half<sup>Q</sup> (0, 0.5), and <sup>b</sup>as many as possible<sup>Q</sup> (0.5, 1).

Herrera and Herrera-Viedma [5–7], Herrera and Verdegay [9], and Herrera et al. [10–13] used the LOWA operator to aggregate the individual linguistic performance values to get the collective linguistic preference relation, and then utilized various linguistic choice mechanisms to find a solution set of alternatives. These approaches are straightforward and can be applied to many group settings with linguistic information, yet they are unsuitable for group decision making with uncertain multiplicative linguistic preference relations.

## References

[1] F. Chiclana, F. Herrera, E. Herrera-Viedma, The ordered weighted geometric operator: properties and application, Proceedings of the 8th International Conference on Information Processing and Management of Uncertainty in Knowledge-Based Systems, Madrid, Spain, 2000, pp. 985–991.

[2] F. Chiclana, F. Herrera, E. Herrera-Viedma, Integrating multiplicative preference relations in a multipurpose decision

making model based on fuzzy preference relations, Fuzzy Sets and Systems 112 (2001) 277– 291.

[3] F. Chiclana, E. Herrera-Viedma, F. Herrera, S. Alonso, Induced ordered weighted geometric operators and their use in the aggregation of multiplicative preference relations, International Journal of Intelligent Systems 19 (2004) 233– 255.

[4] M. Delgado, J.L. Verdegay, M.A. Vila, Linguistic decision making models, International Journal of Intelligent Systems 8 (1993) 351– 370.

[5] F. Herrera, E. Herrera-Viedma, Aggregation operators for linguistic weighted information, IEEE Transactions on Systems, Man and Cybernetics. Part A. Systems and Humans 27 (1997) 646– 656.

[6] F. Herrera, E. Herrera-Viedma, Choice functions and mechanisms for linguistic preference relations, European Journal of Operational Research 120 (2000) 144 – 161.

[7] F. Herrera, E. Herrera-Viedma, Linguistic decision analysis: steps for solving decision problems under linguistic information, Fuzzy Sets and Systems 115 (2000) 67 – 82.

[8] F. Herrera, L. Martı´nez, A 2-tuple fuzzy linguistic representation model for computing with words, IEEE Transactions on Fuzzy Systems 8 (2000) 746–752.

[9] F. Herrera, J.L. Verdegay, Linguistic assessments in group decision, Proceedings of the 11th European Congress of Fuzzy Intelligent Technology, Aachen, Germany, 1993, pp. 941– 948.

[10] F. Herrera, E. Herrera-Viedma, J.L. Verdegay, A model of consensus in group decision making under linguistic assessments, Fuzzy Sets and Systems 78 (1996) 73– 87.

[11] F. Herrera, E. Herrera-Viedma, J.L. Verdegay, Direct approach processes in group decision making using linguistic OWA operators, Fuzzy Sets and Systems 79 (1996) 175 – 190.

[12] F. Herrera, E. Herrera-Viedma, J.L. Verdegay, A rational consensus model in group decision making using linguistic assessments, Fuzzy Sets and Systems 88 (1997) 31 – 49.

[13] F. Herrera, E. Herrera-Viedma, L. Martı´nez, A fusion approach for managing multi-granularity linguistic term sets in decision making, Fuzzy Sets and Systems 114 (2000) 43 – 58.

[14] F. Herrera, E. Herrera-Viedma, F. Chiclana, Multiperson decision making based on multiplicative preference relations, European Journal of Operational Research 129 (2001) 372– 385.

[15] F. Herrera, E. Herrera-Viedma, F. Chiclana, A study of the origin and uses of the ordered weighted geometric operator in multicriteria decision making, International Journal of Intelligent Systems 18 (2003) 689 – 707.

[16] S.H. Kim, S.H. Choi, J.K. Kim, An interactive procedure for multiple attribute group decision making with incomplete information: range-based approach, European Journal of Operational Research 118 (1999) 139–152.

[17] M. Roubens, Fuzzy sets and decision analysis, Fuzzy Sets and Systems 90 (1997) 199–206.

[18] T.L. Saaty, The Analytic Hierarchy Process, McGraw-Hill, New York, 1980.

[19] Z.S. Xu, Study on the relation between two classes of scales in AHP, Systems Engineering-Theory & Practice 19 (7) (1999) 97– 101.

[20] Z.S. Xu, Study on methods for multiple attribute decision making under some situations, PhD thesis, Southeast University, Nanjing, China, 2002.

[21] Z.S. Xu, Two methods for ranking alternatives in group decision making with different preference information, Information: An International Journal 6 (2003) 389– 394.

[22] Z.S. Xu, Uncertain Multiple Attribute Decision Making: Methods and Applications, Tsinghua University Press, Beijing, 2004a.

[23] Z.S. Xu, Goal programming models for obtaining the priority vector of incomplete fuzzy preference relation, International Journal of Approximate Reasoning 36 (2004b) 261 – 270.

[24] Z.S. Xu, A method based on linguistic aggregation operators for group decision making with linguistic preference relations, Information Sciences, in press.

[25] Z.S. Xu, A least deviation method for priorities of fuzzy preference matrix, European Journal of Operational Research, in press.

[26] Z.S. Xu, Q.L. Da, The ordered weighted geometric averaging operators, International Journal of Intelligent Systems 17 (2002a) 709– 716.

[27] Z.S. Xu, Q.L. Da, The uncertain OWA operator, International Journal of Intelligent Systems 17 (2002b) 569– 575.

[28] Z.S. Xu, Q.L. Da, An overview of operators for aggregating information, International Journal of Intelligent Systems 18 (2003a) 953– 969.

[29] Z.S. Xu, Q.L. Da, An approach to improving consistency of fuzzy preference matrix, Fuzzy Optimization and Decision Making 2 (2003b) 3 – 12.

[30] R.R. Yager, On ordered weighted averaging aggregation operators in multicriteria decision making, IEEE Transactions on Systems, Man, and Cybernetics 18 (1988) 183– 190.

[31] R.R. Yager, Families and extension of OWA aggregation, Fuzzy Sets and Systems 59 (1993) 125 – 148.

[32] R.R. Yager, D.P. Filev, Induced ordered weighted averaging operators, IEEE Transactions on Systems, Man and Cybernetics. Part B. Cybernetics 29 (1999) 141 – 150.

[33] L.A. Zadeh, A computational approach to fuzzy quantifiers in natural languages, Computers and Mathematics with Applications 9 (1983) 149– 184.

![](/api/attachments/6EBCK73S/fulltext/images/f36ce5aaf8330c0c980e7e8325a95c3e4267f36f99ac2ec7e1e758b496240c46.jpg)

Zeshui Xu is a Professor of Sciences Institute, PLA University of Science and Technology, Nanjing, China. He received a PhD degree in management science and engineering from Southeast University, Nanjing, China. He is a research fellow of Economics and Management College, Southeast University. He services on the Editorial Board of Information: An International Journal. He has authored a book, Uncertain Multiple Attribute Decision

Making: Methods and Applications (Tsinghua University Press, Beijing, 2004) and has contributed over 150 journal articles to professional journals such as European Journal of Operational Research, Journal of Optimization Theory and Applications, International Journal of Intelligent Systems, International Journal of Approximate Reasoning, Information Sciences, Omega, Information Fusion, and Fuzzy Optimization and Decision Making. He is also a paper reviewer of many professional journals such as IEEE Transactions on Systems, Man, and Cybernetics, IEEE Transactions on Fuzzy Systems, Information Sciences, European Journal of Operational Research, Fuzzy Optimization and Decision Making, and International Journal of Information Technology and Decision Making. His current research interests include information fusion, multicriteria decision making, computing with words, and aggregation operators.
