---
otero_id: 8098
otero_key: "HKKTDEHY"
title: "A consistency and consensus based decision support model for group decision making with multiplicative preference relations"
authors: "Zhibin Wu; Jiuping Xu"
year: "2012"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2011.11.022"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# A consistency and consensus based decision support model for group decision making with multiplicative preference relations

Zhibin Wu, Jiuping Xu ⁎

Uncertainty Decision-making Laboratory, Sichuan University, Chengdu 610064, PR China

## a r t i c l e i n f o

Article history: Received 26 December 2010 Received in revised form 11 September 2011 Accepted 24 November 2011 Available online 2 December 2011

Keywords: Group decision making Multiplicative preference relation Consistency Consensus Decision support mode

## a b s t r a c t

In group decision making (GDM) with multiplicative preference relations (also known as pairwise comparison matrices in the Analytical Hierarchy Process), to come to a meaningful and reliable solution, it is preferable to consider individual consistency and group consensus in the decision process. This paper provides a decision support model to aid the group consensus process while keeping an acceptable individual consistency for each decision maker. The concept of an individual consistency index and a group consensus index is introduced based on the Hadamard product of two matrices. Two algorithms are presented in the designed support model. The <sup>fi</sup>rst algorithm is utilized to convert an unacceptable preference relation to an acceptable one. The second algorithm is designed to assist the group in achieving a prede<sup>fi</sup>ned consensus level. The main characteristics of our model are that: (1) it is independent of the prioritization method used in the consensus process; (2) it ensures that each individual multiplicative preference relation is of acceptable consistency when the prede<sup>fi</sup>ned consensus level is achieved. Finally, some numerical examples are given to verify the effectiveness of our model.

© 2011 Elsevier B.V. All rights reserved.

## 1. Introduction

Over the past few decades, a number of multiple criteria decision making theories, methods, and applications have been developed in the <sup>fi</sup>elds of management science, operational research, and industrial engineering [6,8,22,30,34,37,52,54]. Because of the increasing complexity of the socio-economic environment nowadays, many decision-making processes in the real world take place in group settings. Preference relations are popular and powerful techniques to model experts' preferences in group decision making (GDM). The three commonly used preference relations are multiplicative preference relations (also known as pairwise comparison matrix in the Analytical Hierarchy Process) [34,38,40,41,44], fuzzy preference relations [33,42], and linguistic preference relations [1,15,47].

Pairwise comparison focuses exclusively on two alternatives at a time and facilitates experts in expressing their preferences. However, this way of providing preferences limits the experts' global perception of the alternatives [11]. As a consequence, the provided preference relations may lead to irrational or inconsistent conclusions. Therefore, it is important to study the conditions under which consistency is satis<sup>fi</sup>ed. For GDM using preference relations, the consistency measure itself includes two sub-problems [17,26]: (1) When can a decision maker, considered individually, be said to be consistent? (2) When can the aggregated group as a whole be considered consistent and in consensus? It is important to differentiate group consistency from group consensus. Group consistency explores the rationality of the aggregated group preference relation itself and group consensus measures the degree of agreement between individual opinions and the group opinion. Therefore, in essence there are three problems: an individual consistency problem, a collective consistency problem and a consensus problem.

When carrying out rational decision making, consistent information is more appropriate than information containing some contradictions. If we were to secure consensus and only thereafter consistency, we would destroy the consensus in favor of individual consistency and the <sup>fi</sup>nal solution might not be acceptable to the decision makers [12]. Clearly, it is preferable that the set of decision makers reach a high degree of individual consistency and group consensus before applying the selection process. In a rational GDM process, both consensus and consistency should be pursued and sought after. A solution with a high level of consensus is desirable, but also that solution should be derived from information that is consistent enough [2,12]. There are cases where each individual is consistent, but the group solution is not in accordance with any one of the group. We assume that the decision makers expect an internal logic to their judgments, but at the same time they expect a consensus in the group.

The aim of this paper is to propose a consistency and consensus based support model to support the consensus reaching process in GDM with multiplicative preference relations. The remainder of this paper is structured as follows. Section 2 brie<sup>fl</sup>y reviews the related work on consistency and consensus of preference relations. Section 3 develops a consistency measure of multiplicative preference relation and supplies a method to deal with inconsistency. Section 4 discusses the consensus measure and the consensus reaching process. Section 5 is devoted to presenting a complete support model for GDM. In Section 6, three illustrative examples are provided. Concluding remarks are made in Section 7.

## 2. Literature review

In this section, we <sup>fi</sup>rst review the pertinent literature on the consensus models of GDM with preference relations. Then we discuss the basic methodology and motivation of our work.

## 2.1. Consistency measures

Preference relations are a common format for expressing preferences by using pairwise comparisons. The decision maker makes a direct choice of one object over another when comparing two objects. However, inconsistencies are not unexpected, as making value judgments can be dif<sup>fi</sup>cult in some situations [34]. Hitherto, many authors have paid attention to the individual consistency problems of preference relations [7,11,15,33,38,46]. For multiplicative preference relations, there are two well established methods to create a consistency index. One of these is the consistency ratio based on Saaty's eigenvector method [38]. The other method proposed by Crawford and Williams [14] is the geometric consistency index based on a row geometric mean prioritization method (RGMM). Furthermore, many methods have been shown to modify multiplicative preference relations with unacceptable consistency to ones of acceptable consistency (see for example, [7,46]). The <sup>fi</sup>rst issue addressed in this study provides an alternative method to help decision makers improve the consistency of their multiplicative preference relations.

## 2.2. Consensus models

The consensus measure is used to measure the difference among decision makers and is a vital element of consensus models. A consensus process can be viewed as a dynamic and iterative group discussion process with several consensus rounds, in which the decision makers agree to change their preferences following advice given by a moderator. The moderator knows the agreement at each moment of the consensus process by means of the computation of various consensus measures and is in charge of supervising and moving the consensus process towards success [5]. Different models that guide the moderator and the decision makers in achieving the consensus process have been developed for GDM problems (see for example, [3,13,20,24,32,36,48]). For preference relations, the well-known consensus models are the ones for multiplicative preference relations [4,17,39,53], fuzzy preference relations [2,25,31,49], and linguistic preference relations [5,16,21,27,35]. These studies have made great progress in GDM consensus models.

Saaty [39] developed a metric for the compatibility of two multiplicative preference relations. Bryson [4] and Yeh et al. [53] presented two indicators to estimate the level of group consensus: the group strong agreement quotient and the group strong disagreement quotient. Dong et al. [17] proposed interesting consensus indexes to measure consensus degree among multiplicative preference relations for AHP group decision making using RGMM. Kacprzyk et al. [31] presented ‘soft’ degrees of consensus for fuzzy preference relations and employed fuzzy linguistic quanti<sup>fi</sup>ers to represent a fuzzy majority. Xu [49] presented a number of goal programming models and quadratic programming models based on the idea of maximizing group consensus to determine the importance weight of each preference relation. For incomplete fuzzy preference relations, Herrera-Viedma et al. [25] developed a feedback mechanism to generate advice on how experts should change or complete their preferences in order to reach a solution with high consensus and consistency degrees. For GDM using linguistic preference relations, Herrera et al. [21] introduced a consensus model, which is based on the use of a fuzzy majority represented by means of a linguistic quanti<sup>fi</sup>er. The model is guided by some linguistic consensus and linguistic consistency measures. Herrera-Viedma et al. developed further a consensus support system model for GDM with multi-granular linguistic preference relations. Cabrerizo et al. [5] discussed a consensus process for linguistic preference relations in GDM with an unbalanced fuzzy linguistic context with incomplete information. There are also a few papers that discuss the consensus reaching process for multiple attribute group decision making (MAGDM) problems [20,36,45,48].

## 2.3. The proposed work

As mentioned earlier, in GDM with preference relations both consistency and consensus should be addressed. There are a few papers that address both of these, particularly for multiplicative preference relations [2,12,17,25]. Dong et al. presented consensus models dealt with multiplicative preference relations [17]. Their consensus models are concise and can be applied to GDM based on the row geometric prioritization method. In [2,12,25], the authors managed consistency and consensus criteria simultaneously for GDM with fuzzy preference relations. They de<sup>fi</sup>ned a new measure called consistency/consensus level (CCL), $C C L = ( 1 - \delta ) \cdot C L + \delta \cdot C R ,$ , where CL is the global consistency level, CR is the global consensus degree and δ is the tradeoff parameter between consistency and consensus. These methods are very useful and interesting yet they do not explicitly show if the <sup>fi</sup>nal individual consistency is limited to an acceptable level.

We note that it is possible to convert a multiplicative preference relation into a fuzzy preference relation and vice versa, by means of adequate transformation functions such as proposed in [9,10,23]. In general, research progress in GDM with one kind of preference relations can bene<sup>fi</sup>t research in another kind. Nevertheless, the multiplicative preference relation as a typical preference relation has been widely used and accepted in the <sup>fi</sup>eld of decision making. It is very important in the decision process to look for consistency and consensus models which directly facilitate decision makers. In addition, it is necessary to develop new simple yet effective consensus models for GDM with preference relations.

Previous studies have made signi<sup>fi</sup>cant contributions to the consensus models of GDM problems. However, a detailed survey of the literature revealed that consensus modeling of multiplicative preference relations has not been adequately considered. Therefore, based on the fundamental methodology for GDM with preference relations, we focus on a consistency and consensus based support model for multiplicative preference relations. In the designed model, the group multiplicative preference relation is selected as a reference point to modify the decision maker's preference relation which has a maximum group consensus index in each round. Our model has the following characteristics: (1) it is independent of the prioritization method used in the consensus process; (2) it makes each individual multiplicative preference relation still be of acceptable consistency when the prede<sup>fi</sup>ned consensus level is achieved. Thus, a more <sup>fl</sup>exible and reliable GDM model based on multiplicative preference relations is obtained.

## 3. Consistency measure

In this section, in order for this paper to be as self-contained as possible, we <sup>fi</sup>rst introduce the concept of multiplicative preference relations and their aggregation in the context of GDM, then we focus our discussion on consistency measure.

## 3.1. Concepts and properties of the consistency measure

Denote $N { = } \{ 1 , 2 , \cdots , n \}$ and $M = \{ 1 , 2 , \cdots , m \} .$ . Let $X = \{ x _ { 1 } , x _ { 2 } , \cdots , x _ { n } \}$ be a <sup>fi</sup>nite set of alternatives, where x denotes the ith alternative. In a preference relation, an expert provides judgments for every pair of alternatives which re<sup>fl</sup>ect the degree of preference of the <sup>fi</sup>rst alternative over the second one. The concept of the multiplicative preference relation (pairwise comparison matrix) is given below.

De<sup>fi</sup>nition 1. ([38]) A multiplicative preference relation on a set of alternatives X is represented by a matrix, $A = ( a _ { i j } ) _ { n \times n } \subset X \times X ,$ , being $a _ { i j }$ belonged precisely to the Saaty 1–9 scale and is interpreted as the ratio of the preference intensity of alternative $x _ { i }$ to that of $x _ { j } ,$ and multiplicative reciprocity is assumed, i.e., $a _ { i j } \cdot a _ { j i } = 1 , \forall i , j \in N .$

Consider a GDM problem with multiplicative preference relations. Let $D = \{ d _ { 1 } , d _ { 2 } , \dots , d _ { m } \}$ be the set of decision makers, and let $\lambda = \{ \lambda _ { 1 } , \lambda _ { 2 } ,$ $\cdots , \lambda _ { m } \}$ be the weight vector of decision makers, where $\lambda _ { k } > 0 ,$ $k { \in } M , \sum _ { k = 1 } ^ { m } \lambda _ { k } { = } 1$ . GDM involves aggregating individual preferences into a single collective preference. Individual judgments can be aggregated in different ways by aggradation operators such as the OWAlike operators proposed by Yager [50,51]. For multiplicative preference relation in AHP, the methods that have been found to be most useful are the aggregation of individual judgments (AIJ) and the aggregation of priorities (AIP) [18,19]. Since the group is assumed to act together as a unit, AIJ is appropriate for our study. In this paper, we choose a geometric average operator to obtain the group preference relation.

De<sup>fi</sup>nition 2. Let $A _ { 1 } , A _ { 2 } , \cdots , A _ { m }$ be m multiplicative preference relations, where $A _ { k } = ( a _ { i j } ^ { ( k ) } ) _ { n \times n }$ then $A ^ { c } = ( a _ { i j } ^ { c } ) _ { n \times n } ,$ where

$$
a _ {i j} ^ {c} = \prod_ {k = 1} ^ {m} \left(a _ {i j} ^ {(k)}\right) ^ {\lambda_ {k}},\tag{1}
$$

is called the group multiplicative preference relation.

The test of consistency measures is a critical step in decision making using preference relations. Consistent information which does not imply any kind of contradiction is more relevant or important than information containing some contradictions. When a multiplicative preference relation fails to satisfy the consistency requirement, it is necessary to make revisions. In this section, we introduce a consistency measure based on the Hadamard product.

De<sup>fi</sup>nition 3. ([38]) A multiplicative preference relation $A = ( a _ { i j } ) _ { n \times n }$ is consistent if

$$
a _ {i j} = a _ {i k} a _ {k j}, \forall i, j, k \in N.\tag{2}
$$

From (2), it follows that

$$
a _ {i j} = \frac {1}{a _ {k i}} a _ {k j} = a _ {i k} \frac {1}{a _ {j k}}, \forall k \in N.\tag{3}
$$

Expression (3) shows that for a consistent multiplicative preference relation, any element in the preference relation can be obtained by any row or any column of that preference relation. Multiplying both sides of (3) for all $k ,$ we can get that

$$
a _ {i j} = \left(\prod_ {k = 1} ^ {n} a _ {i k} a _ {k j}\right) ^ {1 / n} = \prod_ {k = 1} ^ {n} \left(a _ {i k} a _ {k j}\right) ^ {1 / n}.\tag{4}
$$

If A is consistent, then (2) and (4) are equivalent. We note that for a multiplicative preference relation, a matrix can be constructed by (4). That is, for a multiplicative preference relation $A = ( a _ { i j } ) _ { n \times n } ,$ we can construct a corresponding matrix $\begin{array} { r } { G = ( g _ { i j } ) _ { n \times n } , } \end{array}$ where

$$
g _ {i j} = \prod_ {k = 1} ^ {n} \left(a _ {i k} a _ {k j}\right) ^ {1 / n}.\tag{5}
$$

In order to de<sup>fi</sup>ne the consistency index, we introduce the Hadamard product of two matrices.

De<sup>fi</sup>nition 4. ([28]) The Hadamard product of $A = ( a _ { i j } ) _ { n \times n }$ and $B = ( b _ { i j } ) _ { n \times n }$ is de<sup>fi</sup>ned by $C = A \circ B = ( c _ { i j } ) _ { n \times n } ,$ , where $c _ { i j } = a _ { i j } b _ { i j } .$

De<sup>fi</sup>nition 5. Let $A = ( A _ { i j } ) _ { n \times n }$ and $B = ( b _ { i j } ) _ { n \times n }$ be two multiplicative preference relations, then we de<sup>fi</sup>ne the deviation degree between A and B as follows

$$
d (A, B) = \frac {1}{n ^ {2}} e ^ {T} A \circ B ^ {T} e = \frac {1}{n ^ {2}} \sum_ {i = 1} ^ {n} \sum_ {j = 1} ^ {n} a _ {i j} b _ {j i}, \text {   where   } e = (1, 1, \dots , 1) _ {n \times 1} ^ {T}.\tag{6}
$$

Remark 1. From the above de<sup>fi</sup>nition, we have the following property. Let A and B be two multiplicative preference relations with the same dimension, then: $( 1 ) \ d ( A , B ) \geq 1$ . Especially, $d ( A , B ) = 1$ if and only i $\stackrel { . } { A } = B . ( 2 ) d ( A , B ) = d ( B , A )$ . From the reciprocity of A and B it follows that

$$
\begin{array}{l} d (A, B) = \frac {1}{n ^ {2}} \sum_ {i = 1} ^ {n - 1} \sum_ {j = i + 1} ^ {n} \left(a _ {i j} b _ {j i} + a _ {j i} b _ {i j}\right) + \left(1 / n ^ {2}\right) \sum_ {i = 1} ^ {n} a _ {i i} b _ {i i} \\ = \frac {1}{n ^ {2}} \sum_ {i = 1} ^ {n - 1} \sum_ {j = i + 1} ^ {n} \left(a _ {i j} b _ {j i} + a _ {j i} b _ {i j}\right) + \frac {1}{n}. \end{array}\tag{7}
$$

De<sup>fi</sup>nition 6. Let $A = ( a _ { i j } ) _ { n \times n }$ be a multiplicative preference relation. The corresponding consistent preference relation obtained by (5) is denoted by G. Given a threshold value ${ \overline { { C I } } } ,$ if the consistency index satis<sup>fi</sup>es the following,

$$
C I _ {H} (A) = d (A, G) \leq \overline {{C I}},\tag{8}
$$

then we call A a multiplicative preference relation with acceptable consistency.

Here, the consistency measure of A is concerned with the compatibility of the consistent preference relation derived from A with A itself. As was suggested by [39,43], using the Hadamard product is more reliable to measure the compatibility of two matrices constructed by ratio scales. Note that $C I _ { H } ( A ) = 1$ if and only if A is a consistent multiplicative preference relation. By using the above deviation degrees based on the Hadamard product, the representation of individual consistency and group consensus is uni<sup>fi</sup>ed. Thus we use the threshold that was used to test the compatibility of two multiplicative preference relations to set the acceptable level of consistency. Both Saaty [39] and Wang [43] suggested that the admissible bounds for checking the consistency of A can be set at 1.1.

Lemma 1. Let $x _ { i } { > } 0 , \lambda _ { i } { > } 0 ,$ , i∈N and $\sum { _ i ^ { n } } _ { = 1 } ^ { n } \lambda _ { i } { = } 1$ , then

$$
\prod_ {i = 1} ^ {n} \left(x _ {i}\right) ^ {\lambda_ {i}} \leq \sum_ {i = 1} ^ {n} \lambda_ {i} x _ {i}.\tag{9}
$$

Proof. This is the weighted arithmetic–geometric mean inequality, see ([28], P535).

Lemma 2. Suppose $x > 0 , 0 < \theta < 1$ , then

$$
\left(\frac {1}{x}\right) ^ {\theta} + x ^ {\theta} \leq \frac {1}{x} + x.\tag{10}
$$

The equality holds if and only $i f x = 1$

Proof. The proof of Lemma 2 is straightforward.

Theorem 1. Let $A _ { 1 } , A _ { 2 } , \cdots , A _ { m }$ be m multiplicative preference relations provided by m decision makers. $A ^ { c }$ is the group multiplicative preference relation utilizing a geometric average operator. Then,

$$
C I _ {H} (A ^ {c}) \leq \max _ {k} \left\{C I _ {H} (A _ {k}) \right\}.\tag{11}
$$

Proof. By De<sup>fi</sup>nition 5 and Lemma 1, we can complete the proof of Theorem 1.

Corollary 1. $L e t A _ { 1 } , A _ { 2 } , \cdots , A _ { m }$ and $A ^ { c }$ be as before. Then, $C I _ { H } ( A ^ { c } )$ ≤α under the condition that $C I _ { H } ( A _ { k } ) \leq \alpha ,$ ∀k∈M.

Corollary 2. I ${ } ^ { \circ } C I _ { H } ( A _ { k } ) = 1 ,$ , then $C I _ { H } ( A ^ { c } ) = 1$

Under this measure, Theorem 1 proves that the inconsistency of the group is smaller than the largest individual inconsistency. Corollary 1 guarantees that if individual multiplicative preference relations are of acceptable consistency, then the group multiplicative preference relation is also of acceptable consistency. Corollary 2 implies that if every multiplicative preference relation is consistent, then the group multiplicative preference relation is also consistent.

## 3.2. Consistency improving method

When the individual multiplicative preference relation A is not of acceptable consistency, we need to return A to the decision maker to reconsider constructing a new relation. A basic procedure for the consistency improving process is depicted in Fig. 1.

Generally, this process is guided by a moderator who helps the decision makers alter their preferences to move toward more consistency. The following algorithm can support the moderator in the consistency improving process.

Algorithm 1. Input: The original individual multiplicative preference relation $A = ( a _ { i j } ) _ { n \times n } ,$ the parameter θ∈(0,1) and the threshold ${ \overline { { C I } } } = \alpha .$

<sup>¼</sup>Output: The adjusted multiplicative preference relation A and the consistency index $\overset { \cdot } { C } I _ { H } \left( \overline { { A } } \right)$ .

Step 1. Let $A _ { 0 } = ( a _ { i j , 0 } ) _ { n \times n } = ( a _ { i j } ) _ { n \times n }$ and $h = 0$

Step 2. Compute $G _ { h }$ by (5) and the consistency index $C I _ { H } ( A _ { h } )$ , where

$$
C I _ {H} (A _ {h}) = d (A _ {h}, G _ {h}).\tag{12}
$$

Step 3. If $C I _ { H } ( A _ { h } ) \leq \alpha ,$ then go to Step 5; otherwise, go to the next step.

Step 4. Apply the following strategy to update the last matrix $A _ { h } = ( a _ { i j , h } ) _ { n \times n } .$

$$
A _ {h + 1} = (A _ {h}) ^ {\theta} \circ (G _ {h}) ^ {1 - \theta},\tag{13}
$$

where $\theta { \in } ( 0 , 1 )$ . Let $h = h + 1$ , and return to Step 2. Step 5. Let $\overline { { A } } = A _ { h }$ . Output A and $C I _ { H } \Big ( \overline { { A } } \Big )$ Step 6. End.

From Algorithm 1, we have the following theorem.

Theorem 2. Algorithm 1 is convergent. That is, we have $C I _ { H } ( A _ { h + 1 } ) <$ $C I _ { H } ( A _ { h } )$ for each h, and lim $C I _ { H } ( A _ { h } ) \leq \alpha , \forall \alpha > 1$ h→∞

Proof. The proof of Theorem 2 is provided in Appendix A.

For an inconsistent multiplicative preference relation $A = ( a _ { i j } ) _ { n \times n } ,$ Saaty de<sup>fi</sup>ned a consistency index in terms of the principal eigenvalue $\lambda _ { m a x }$ of A as follows [38]:

$$
C I (A) = \frac {\lambda_ {m a x} (A) - n}{n - 1}.\tag{14}
$$

The consistency test involves the use of a consistency ratio: $C R = C I / R I ,$ where RI is a random index. If $C R > 0 . 1$ , the decision maker is asked to revise his judgment until an acceptable level of consistency is reached. In the consistency improvement method, it is required that $\lambda _ { m a x } ( A _ { h + 1 } ) < \lambda _ { m a x } ( A _ { h } )$ . In the following, we show that the proposed consistency improvement method in this section meets such a requirement. The following lemma is useful, see P361-362 of [29].

Lemma 3. Suppose that $A , B \in M _ { n } ( R ) _ { \mathrm { \Omega } }$ , where $M _ { n }$ is a set of n-dimensional nonnegative matrices on the real number set, and 0bαb1. Then,

$$
\rho \left(A ^ {\alpha} \circ B ^ {1 - \alpha}\right) \leq (\rho (A)) ^ {\alpha} (\rho (B)) ^ {1 - \alpha},\tag{15}
$$

where $\rho ( A ) = \lambda _ { m a x } ( A )$ denotes the spectral radium.

Theorem 3. In Algorithm 1, we have

$$
\lambda_ {m a x} (A _ {h + 1}) <   \lambda_ {m a x} (A _ {h}).\tag{16}
$$

Proof. The proof of Theorem 3 is provided in Appendix A.

Theorem 3 reveals the relationship of our consistency measure and consistency improvement method with the Saaty's traditional consistency concepts. As the modi<sup>fi</sup>ed matrix has a reduced maximum eigenvalue, our improvement method will converge to an acceptable CR in the sense of Saaty's consistency measure.

![](/api/attachments/HKKTDEHY/fulltext/images/8b8d90f278a0c0bb3f8a53843ae9530d10725dec9e42d3839174ab9213966e40.jpg)  
Fig. 1. Consistency control process.

## 4. Consensus measure

In group context, consensus decision making is often considered a desirable outcome. When consensus schemes are utilized, the experts involved are supposed to participate in the discussions towards a consensus solution. In this section, we introduce a consensus index to measure the consensus level between the group members. How to reach a prede<sup>fi</sup>ned consensus level is described and some theoretical foundations are also given.

## 4.1. Definition and property

The following de<sup>fi</sup>nition is used to measure the closeness amongst experts' opinions in order to obtain the consensus level.

De<sup>fi</sup>nition 7. Let $A _ { 1 } , A _ { 2 } , \cdots , A _ { m }$ be m multiplicative preference relations provided by m decision makers. Suppose A<sup>c</sup> is the group multiplicative preference relation utilizing the geometric average operator. Then the group consensus index of $\textstyle \mathrm { \mathrm { A } } _ { l }$ is de<sup>fi</sup>ned by

$$
G C I _ {H} (A _ {l}) = d \left(A _ {l}, A ^ {c}\right) = \frac {1}{n ^ {2}} \sum_ {i = 1} ^ {n} \sum_ {j = 1} ^ {n} a _ {i j} ^ {(k)} a _ {j i} ^ {c},\tag{17}
$$

where

$$
a _ {i j} ^ {c} = \prod_ {k = 1} ^ {m} \left(a _ {i j} ^ {(k)}\right) ^ {\lambda_ {k}}, \quad i, j \in N.\tag{18}
$$

In this way, consensus can be somehow understood as closeness between the individual opinions and the group opinion. If $G C I _ { H } ( A _ { l } ) = 1$ then the lth decision maker has full consensus with the group preference. Otherwise, the smaller the value of $G C I _ { H } ( A _ { l } )$ , the closer that decision maker is to the group. According to the actual situation, the decision makers establish the threshold GCI for the deviation degree between the individual preference relation and the group preference relation. If for all $l , G C I _ { H } ( A _ { l } ) { \le } \overline { { G C I } }$ , we conclude that an acceptable level of consensus <sup>ð Þ</sup>is achieved among the decision makers.

From the above de<sup>fi</sup>nition, we can get the following properties.

Theorem 4. Let $A _ { 1 } , A _ { 2 } , \cdots , A _ { m }$ be m multiplicative preference relations provided by m decision makers. $A ^ { c }$ is the group multiplicative preference relation utilizing a geometric average operator. Then,

$$
d (A ^ {c}, A _ {k}) \leq \max _ {l} \{d (A _ {l}, A _ {k}) \}.\tag{19}
$$

Proof. The proof of Theorem 4 is provided in Appendix A.

Theorem 4 shows that the deviation degree between multiplicative preference relation $A _ { k }$ of $A _ { 1 } , A _ { 2 } , \cdots , A _ { m }$ and their group multiplicative preference relation A<sup>c</sup> is no greater than the largest deviation degree between any two of the multiplicative preference relations in $A _ { 1 } , A _ { 2 } , \cdots A _ { m } .$

## 4.2. Consensus reaching process

As consensus is the major goal of GDM, in the GDM process, before aggregation we need to apply consensus models to help decision makers reach consensus. Inspired by [27], a rational consensus model for a GDM problem based on multiplicative preference relations can be shown in Fig. 2.

In the model, there is often a moderator, via the exchange of information and rational arguments, trying to persuade the experts to alter their opinions to bring these opinions closer. In the following, we give an iterative model to achieve consensus.

Let $\{ A _ { 1 } , A _ { 2 } , \cdots , A _ { m } \}$ and $\lambda { = } \{ \lambda _ { 1 } , \lambda _ { 2 } , \cdots , \lambda _ { m } \}$ be as before. $A ^ { c }$ is the group multiplicative preference relation utilizing the geometric average operator. Without loss of generality, suppose that multiplicative preference relation $A _ { \tau }$ has the largest consensus index. The main step for the proposed consensus model is constructing a new multiplicative preference relation $\overline { { A } } _ { \tau }$ according to $A _ { \tau }$ . When establishing the new preference relation, we adopt the following strategy

$$
\bar {a} _ {i j} ^ {(\tau)} = \left(a _ {i j} ^ {(\tau)}\right) ^ {\gamma} \left(a _ {i j} ^ {c}\right) ^ {1 - \gamma}, 0 <   \gamma <   1.\tag{20}
$$

Follow this strategy until all the multiplicative preference relations reach a prede<sup>fi</sup>ned level of acceptable consensus or the maximum number of iterations is obtained. Details of our consensus model are depicted in Algorithm 2.

Algorithm 2. Input: Individual multiplicative preference relations $\{ A _ { 1 } , A _ { 2 } , \cdots , A _ { m } \} ,$ the weight vector of decision makers $\lambda { = } \{ \lambda _ { 1 } , \lambda _ { 2 } , \cdots , \lambda _ { m } \}$ the prede<sup>fi</sup>ned threshold GCI, the maximum number of iterative times $h _ { m a x } \ge 1$ and $0 < \gamma < 1$

Output: Modi<sup>fi</sup>ed multiplicative preference relations $\left\{ \overline { { A } } _ { 1 } , \overline { { A } } _ { 2 } , \cdots , \overline { { A } } _ { m } \right\}$ the consensus index of each preference relation $G C I _ { H } \left( \overline { { A } } _ { k } \right) , k = 1 , 2 , \cdots , m$ and the number of iterations h.

Step 1. Set h=0 and $A _ { k , 0 } = ( a _ { i j , 0 } ^ { ( k ) } ) _ { n \times n } = A _ { k } = ( a _ { i j } ^ { ( k ) } ) _ { n \times n } .$

Step 2. Calculate the group multiplicative preference relation $A _ { h } ^ { c } { = } ( a _ { i j , h } ^ { c } ) _ { n \times n }$ corresponding to $\{ A _ { 1 , h } , A _ { 2 , h } , \cdots A _ { m , h } \}$ , where $a _ { i j , h } = ( \bar { a } _ { i j , h } ^ { ( 1 ) } ) ^ { \lambda _ { 1 } } ( a _ { i j , h } ^ { ( 2 ) } ) ^ { \lambda _ { 1 } } \cdots ( a _ { i j , h } ^ { ( m ) } ) ^ { \lambda _ { m } } .$

Step 3. Calculate the group consensus index $G C I _ { H } ( A _ { k , h } ) , k = 1 , 2 , \cdots , m$ $\mathrm { I f } \ { } _ { \leq G C I _ { H } } ^ { G C I _ { H } ( A _ { k , h } ) }$ , ∀k∈M or h≥h , then go to step 5; otherwise, continue with the next step.

Step 4. Suppose that $G C I _ { H } ( A _ { \tau , h } ) = \mathrm { m a x } _ { k } \left\{ G C I _ { H } ( A _ { k , h } ) \right\}$ . Let $A _ { k , h + 1 } =$ $( a _ { i j , h + 1 } ^ { ( k ) } ) _ { n \times n } ,$ where

$$
a _ {i j, h + 1} ^ {(k)} = \left\{ \begin{array}{c c} \left(a _ {i j, h} ^ {(k)}\right) ^ {\gamma} \left(a _ {i j, h} ^ {c}\right) ^ {1 - \gamma} & k = \tau \\ a _ {i j, h} ^ {(k)} & k \neq \tau \end{array} \right..\tag{21}
$$

Set $h = h + 1$ and go to Step 2.

Step 5. Let $\overline { { A _ { k } } } = A _ { k , h }$ . Output the modi<sup>fi</sup>ed multiplicative preference <sup>¼</sup>relationA , $k = 1 , 2 , \cdots , m _ { \mathrm { { \ell } } }$ , the group consensus index for each preference relation $G C I _ { H } ( \bar { A } _ { k } ) , k = 1 , 2 , \cdots , m$ , and the number of iterations h.

Step 6. End.

Remark 2. The main advantage of our proposed consensus scheme is that it does not use any priority methods in the process. In Algorithm 2, the group multiplicative preference relation $A _ { h } ^ { c }$ is considered a reference point in the improvement process in the hth round We modify only one preference relation that has a maximum group consensus level in each round. If there is more than one decision maker simultaneously obtaining the maximum group level, then we can change their preferences in the same round. As mentioned in the <sup>fi</sup>rst section, the decision makers are assumed to change their preferences following the moderator's advice. All team members agree to support the decision. What if there are extreme outliers still outside the consensus level after the given maximal rounds (rather unlikely, but possible)? If this is the case, as it was recommended by [4,36,43], the moderator may prefer as an arbiter and ignore the preferences of the outliers in order to achieve the decision goal.

On the one hand, the proposed model can be considered an interactive method, and the decision makers have the right to participate in the consensus reaching process in each round. On the other hand, since the proposed consensus model can run automatically, a minimum requirement for decision makers is that they only need to provide their preferences in the <sup>fi</sup>rst round. In the following, we discuss the properties of the above consensus model. We show that Algorithm 2 is convergent.

![](/api/attachments/HKKTDEHY/fulltext/images/3170fd8a90e43a39397043b841329d064d9ed103e5aa943ca02595d7f9cba7fe.jpg)  
Fig. 2. GDM problem consensus process.

Theorem 5. In Algorithm 2, suppose the kth decision maker has to change his?/her multiplicative preference relation in the $( h + 1 )$ th iteration. Let $A _ { k , h + 1 }$ be the preference relation generated by Algorithm 2 for the decision maker k. Then, we have

$$
G C I _ {H} \left(A _ {k, h + 1}\right) <   G C I _ {H} \left(A _ {k, h}\right).\tag{22}
$$

Proof. The proof of Theorem 5 is provided in Appendix A.

From Theorem $5 ,$ we know that in each step, a decision maker who modi<sup>fi</sup>es their multiplicative preference relation has a better group consensus index. Generally, the group consensus indexes of those who don't modify their preference relations at this time will not exceed the maximum group consensus index of the last time. Thus, the proposed algorithm is convergent in a general sense. At the same time, the modi<sup>fi</sup>ed multiplicative preference relation has an acceptable individual consistency index under the condition that the consensus reaching process starts with multiplicative preference relations of acceptable consistency.

Theorem 6. Let $A _ { 1 } , A _ { 2 } , \cdots , A _ { m }$ and $A ^ { c }$ be m multiplicative preference relations and the group multiplicative preference relation, respectively. Let $\{ A _ { l , h } \}$ and {A<sup>c</sup>} be the sequences generated by Algorithm 2. If max $\{ C I _ { H } ( A _ { l } ) \} { \le } \overline { { C I } } ,$ l M, then we have

$$
\max _ {l} \left\{C I _ {H} \left(A _ {l, h + 1}\right) \right\} \leq \max _ {l} \left\{C I _ {H} \left(A _ {l, h}\right) \right\} \leq \overline {{C I}}.\tag{23}
$$

Proof. The proof of Theorem 6 is provided in Appendix A.

Therefore, the consistency index for every multiplicative preference relation is still acceptable after the implementation of Algorithm 2. It implies that when we start with preference relations that are acceptable, we end with modi<sup>fi</sup>ed preference relations which not only achieve the prede<sup>fi</sup>ned consensus level but are also of acceptable individual consistency. These theorems provide theoretical foundations and are of vital importance for GDM problems based on multiplicative preference relations.

## 5. A decision support model for the GDM process

The complete support model for a GDM problem with multiplicative preference relations is depicted as a <sup>fl</sup>owchart in Fig. 3. Following the procedure in Fig. 3, the optimum alternative or the rating order of n alternatives will be regarded as a <sup>fi</sup>nal consensus solution to the given GDM problem.

Both in the consistency control process and the consensus reaching process, there are advice rules generated from Algorithm 1 and Algorithm 2. The guidance advice system integrated in the support model acts as a feedback mechanism. In some situations, the moderator can be replaced by the guidance advice system. However, the decision makers are responsible for the <sup>fi</sup>nal decision [27], so they decide whether or not to follow the advice generated by the support model. Thus, our decision support model plays a role in assisting the decision makers and the moderator in the decision process.

The main features of the above support model are emphasized as follows. (1) The consensus reaching process proposed in the model is independent of which priority method is used in the process. (2) It automatically adjusts each multiplicative preference relation to one meeting the prede<sup>fi</sup>ned consensus requirements. (3) Before conducting the consensus reaching process, the consistency control process is carried out to ensure the rationality of each decision maker. (4) Some theoretical results serve as a foundation for the whole group decision model. When the group achieves the prede<sup>fi</sup>ned level of consensus, the consistency of each decision maker is also guaranteed. After obtaining the <sup>fi</sup>nal multiplicative group preference relation, either the eigenvector method or the row geometric mean prioritization method can be used in the selection process. As a result, a general decision support model for solving GDM problems with multiplicative preference relations considering consistency and consensus is presented.

## 6. Illustrative examples

This section presents several examples to show the implementation process and the validity of the proposed approach in practice.

Example 1. Consider the numerical example which was discussed by Dong et al. [17]. Suppose we have a set of <sup>fi</sup>ve decision makers providing the following multiplicative preference relations $\{ A _ { 1 } , A _ { 2 } , A _ { 3 } , A _ { 4 } , A _ { 5 } \}$ on a set of four alternatives $\{ X _ { 1 } , X _ { 2 } , X _ { 3 } , X _ { 4 } \}$ which need to be ranked from the best to the worst. Let $\begin{array} { r } { \dot { w ^ { ( k ) } } = ( w _ { \mathrm { 1 } } ^ { ( k ) } , w _ { \mathrm { 2 } } ^ { ( k ) } , w _ { \mathrm { 3 } } ^ { ( k ) } , w _ { \mathrm { 4 } } ^ { ( k ) } ) ^ { T } } \end{array}$ be the individual priority vector derived from multiplicative preference relation $A _ { k }$ using the eigenvector method. It should be noted that other prioritization methods can also be used in the computation process. Srdjevic [40] presented a multicriteria preference synthesis (MPS) procedure across a Euclidean distance (ED) and minimum violations (MV) criterion to choose the most appropriate method for a given multiplicative preference relation. The main conclusion is that there is no prioritization method that is superior to the others in all cases [40]. $A _ { k }$ and $w ^ { ( k ) } \left( k = 1 , 2 , 3 , 4 , 5 \right)$ are given below.

$$
A _ {1} = \left( \begin{array}{c c c c} 1 & 4 & 6 & 7 \\ 1 / 4 & 1 & 3 & 4 \\ 1 / 6 & 1 / 3 & 1 & 2 \\ 1 / 7 & 1 / 4 & 1 / 2 & 1 \end{array} \right), A _ {2} = \left( \begin{array}{c c c c} 1 & 5 & 7 & 9 \\ 1 / 5 & 1 & 4 & 6 \\ 1 / 7 & 1 / 4 & 1 & 2 \\ 1 / 9 & 1 / 6 & 1 / 2 & 1 \end{array} \right),
$$

$$
\begin{array}{l} w ^ {(1)} = (0. 6 1 6 8, 0. 2 2 3 8, 0. 0 9 7 2, 0. 0 6 2 1) ^ {T}, \\ w ^ {(2)} = (0. 6 5 2 6, 0. 2 2 4 7, 0. 0 7 6 2, 0. 0 4 6 5) ^ {T}, \end{array}
$$

$$
A _ {3} = \left( \begin{array}{c c c c} 1 & 3 & 5 & 8 \\ 1 / 3 & 1 & 4 & 5 \\ 1 / 5 & 1 / 4 & 1 & 2 \\ 1 / 8 & 1 / 5 & 1 / 2 & 1 \end{array} \right), \qquad A _ {4} = \left( \begin{array}{c c c c} 1 & 4 & 5 & 6 \\ 1 / 4 & 1 & 3 & 3 \\ 1 / 5 & 1 / 3 & 1 & 2 \\ 1 / 6 & 1 / 3 & 1 / 2 & 1 \end{array} \right),
$$

$$
\begin{array}{l} w ^ {(3)} = (0. 5 7 0 5, 0. 2 7 7 1, 0. 0 9 5 9, 0. 0 5 6 5) ^ {T}, \\ w ^ {(4)} = (0. 5 9 7 0, 0. 2 2 1 7, 0. 1 0 8 4, 0. 0 7 2 8) ^ {T}, \end{array}
$$

![](/api/attachments/HKKTDEHY/fulltext/images/7cca841ce74bfb2cf9f0ae0f99bb3d49a26b67d0be6715aafd3ee60d6d03e62b.jpg)  
Fig. 3. A GDM process framework with multiplicative preference relations.

$$
\begin{array}{l} A _ {5} = \left( \begin{array}{c c c c} 1 & 1 / 2 & 1 & 2 \\ 2 & 1 & 2 & 3 \\ 1 & 1 / 2 & 1 & 4 \\ 1 / 2 & 1 / 3 & 1 / 4 & 1 \end{array} \right), \\ w ^ {(5)} = (0. 2 1 8 5,   0. 4 1 2 3,   0. 2 6 7 9,   0. 1 0 1 3) ^ {T}. \end{array}
$$

$\mathrm { L e t } \lambda = \{ 0 . 1 , 0 . 3 , 0 . 1 , 0 . 2 , 0 . 3 \}$ be the weights of decision makers. From the above multiplicative preference relations, we calculate the group multiplicative preference relation $A ^ { c }$ using (1) and the corresponding priority vector $w ^ { c } = ( w _ { 1 } ^ { c } , w _ { 2 } ^ { c } , w _ { 3 } ^ { c } , w _ { 4 } ^ { c } ) ^ { T }$ which are listed below. We can see that the ranking order of alternatives in $w ^ { c }$ is the same as that of $w _ { 1 } , w _ { 2 } , w _ { 3 }$ and $w _ { 4 }$ but is very different from that of $w _ { 5 }$ .

$$
\begin{array}{l} A ^ {c} = \left( \begin{array}{c c c c} 1. 0 0 0 0 & 2. 2 2 7 0 & 3. 4 7 5 6 & 5. 0 9 3 7 \\ 0. 4 4 9 0 & 1. 0 0 0 0 & 2. 9 8 0 4 & 4. 0 0 0 5 \\ 0. 2 8 7 7 & 0. 3 3 5 5 & 1. 0 0 0 0 & 2. 4 6 2 3 \\ 0. 1 9 6 3 & 0. 2 5 0 0 & 0. 4 0 6 1 & 1. 0 0 0 0 \end{array} \right), \\ w ^ {c} = (0. 4 9 0 9,   0. 2 9 8 8,   0. 1 3 6 8,   0. 0 7 3 4) ^ {T}. \end{array}
$$

In the following, we show how to apply the GDM support model described in Section 4 to obtain a solution based on consistency and consensus.

## Stage 1: Consistency control process.

By consistency measure, the initial consistency indexes are

$$
\begin{array}{l} C I _ {H} (A _ {1}) = 1. 0 2 5 5, C I _ {H} (A _ {2}) = 1. 0 4 5 0, C I _ {H} (A _ {3}) = 1. 0 2 2 6, \\ C I _ {H} (A _ {4}) = 1. 0 3 1 4, C I _ {H} (A _ {5}) = 1. 0 2 4 1, C I _ {H} \big (A ^ {c} \big) = 1. 0 2 1 5. \end{array}
$$

If we <sup>fi</sup>x a minimum threshold value $\overline { { C I } } = 1 . 1$ , we see that all <sup>¼</sup>the multiplicative preference relations are of acceptable consistency. Using Saaty's consistency ratio (CR), we have

$$
C R (A _ {1}) = 0. 0 3 7 9, C R (A _ {2}) = 0. 0 6 7 1, C R (A _ {3}) = 0. 0 3 3 5,
$$

$$
C R (A _ {4}) = 0. 0 4 6 6, C R (A _ {5}) = 0. 0 3 5 9, C R \left(A ^ {c}\right) = 0. 0 3 1 9,
$$

which also shows that the given preference relations are of acceptable consistency.

## Stage 2: Consensus reaching process.

The group consensus indexes for each decision makers are

$$
G C I _ {H} (A _ {1}) = 1. 0 5 0 2, G C I _ {H} (A _ {2}) = 1. 1 1 4 4, G C I _ {H} (A _ {3}) = 1. 0 3 8 2,
$$

$$
G C I _ {H} (A _ {4}) = 1. 0 4 0 0, G C I _ {H} (A _ {5}) = 1. 3 6 6 6.
$$

Here, the consensus level is set at GCI = 1.1. As $A _ { 2 }$ and $A _ { 5 }$ do <sup>¼</sup>not reach the consensus level, we continue to carry out Algorithm 2. Set $\gamma = 0 . 9 ,$ , the algorithm is terminated after ten steps. The consistency and consensus indexes for each decision maker at each step are listed in Table 1.

From Table 1, we <sup>fi</sup>nd only $A _ { 5 }$ is modi<sup>fi</sup>ed. The consistency indexes of the modi<sup>fi</sup>ed multiplicative preference relation are decreasing in the <sup>fi</sup>rst nine steps but increase a little in the tenth step. The consistency index of the group multiplicative preference relation is no greater than the largest consistency index of the individual multiplicative preference relation at every step. The group consensus indexes for every decision maker at each step are also decreasing. If we use Saaty's consistency ratio (CR), we have ${ \bar { C } } { \bar { R } } { \bar { ( A _ { 5 } ) } } =$ 0:0265, $\stackrel { \cdot } { C } R \left( \overline { { A ^ { c } } } \right) = 0 . 0 \dot { 3 } 8 8$ <sup>¼</sup>. We <sup>fi</sup>nd that the results in this <sup>¼</sup>example are in accordance with the theorems in Sections 2 and 3.

The modi<sup>fi</sup>ed multiplicative preference relations $\overline { { A _ { 5 } } }$ are as follows.

$$
\begin{array}{c} \overline {{A _ {5}}} = \left( \begin{array}{c c c c} 1 & 1. 3 9 1 4 & 2. 3 4 7 9 & 3. 7 9 4 8 \\ 0. 7 1 8 7 & 1 & 2. 6 2 8 6 & 3. 6 5 3 9 \\ 0. 4 2 5 9 & 0. 3 8 0 4 & 1 & 2. 8 6 8 7 \\ 0. 2 6 3 5 & 0. 2 7 3 7 & 0. 3 4 8 6 & 1 \end{array} \right), \\ \overline {{A ^ {c}}} = \left( \begin{array}{c c c c} 1 & 3. 0 2 7 3 & 4. 4 8 9 9 & 6. 1 7 2 8 \\ 0. 3 3 0 3 & 1 & 3. 2 3 5 0 & 4. 2 4 4 2 \\ 0. 2 2 2 7 & 0. 3 0 9 1 & 1 & 2. 2 2 8 6 \\ 0. 1 6 2 0 & 0. 2 3 5 6 & 0. 4 4 8 7 & 1 \end{array} \right), \end{array}
$$

Table 1  
Consistency and consensus indexes for Example 1.

<table><tr><td>Step</td><td>Consistency indexes</td><td>Consensus indexes</td><td> $CI_H(A^c)$ </td></tr><tr><td>k=1</td><td>(1.0255,1.0450,1.0226,1.0314,1.0241)</td><td>(1.0502,1.1144,1.0382,1.0400,1.3666)</td><td>1.0215</td></tr><tr><td>k=2</td><td>(1.0255,1.0450,1.0226,1.0314,1.0220)</td><td>(1.0429,1.1028,1.0324,1.0345,1.3115)</td><td>1.0221</td></tr><tr><td>k=3</td><td>(1.0255,1.0450,1.0226,1.0314,1.0204)</td><td>(1.0366,1.0927,1.0275,1.0299,1.2652)</td><td>1.0227</td></tr><tr><td>k=4</td><td>(1.0255,1.0450,1.0226,1.0314,1.0192)</td><td>(1.0313,1.0838,1.0234,1.0261,1.2263)</td><td>1.0232</td></tr><tr><td>k=5</td><td>(1.0255,1.0450,1.0226,1.0314,1.0184)</td><td>(1.0268,1.0760,1.0200,1.0230,1.1935)</td><td>1.0237</td></tr><tr><td>k=6</td><td>(1.0255,1.0450,1.0226,1.0314,1.0179)</td><td>(1.0229,1.0691,1.0172,1.0204,1.1657)</td><td>1.0243</td></tr><tr><td>k=7</td><td>(1.0255,1.0450,1.0226,1.0314,1.0176)</td><td>(1.0196,1.0630,1.0149,1.0184,1.1421)</td><td>1.0248</td></tr><tr><td>k=8</td><td>(1.0255,1.0450,1.0226,1.0314,1.0176)</td><td>(1.0168,1.0577,1.0130,1.0167,1.1219)</td><td>1.0253</td></tr><tr><td>k=9</td><td>(1.0255,1.0450,1.0226,1.0314,1.0176)</td><td>(1.0145,1.0529,1.0114,1.0154,1.1048)</td><td>1.0257</td></tr><tr><td>k=10</td><td>(1.0255,1.0450,1.0226,1.0314,1.0179)</td><td>(1.0125,1.0487,1.0102,1.0143,1.0901)</td><td>1.0252</td></tr></table>

$$
\overline {{w ^ {(5)}}} = (0. 3 9 5 1, 0. 3 4 4 0, 0. 1 7 6 4, 0. 0 8 4 6) ^ {T},
$$

Stage 3: Selection process.

The <sup>fi</sup>nal group multiplicative preference relation is shown above. Thus the ranking of the alternatives is $X _ { 1 } { > } X _ { 2 } { > } X _ { 3 } { > } X _ { 4 } ,$ which indicates that $X _ { 1 }$ is the best option.

Our ranking order of the alternatives is the same as Dong et al.'s paper but with different degrees of one alternative over another [17]. The consensus model is different from previous papers. The consistency and consensus measures are based on the compatibility of two ratio matrices based on the Hadamard product proposed by Saaty. The consistency and consensus based model is more simple and straightforward. We use the group multiplicative preference relation as the reference point matrix at every step. It is not necessary to compute any priority vector in the consensus reaching process. In [17], both the consensus measure and the consensus model depend on a row geometric mean prioritization method.

Example 2. As we have mentioned, the two aggregation methods (AIJ and AIP) discussed in [19] are widely used for comparisons in literature. For AIP, a consensus degree was proposed by comparing the position of each alternative in the decision makers' individual priorities and in the group priorities [17]. Let $w ^ { ( k ) }$ and $w ^ { c }$ be the individual and collective priority vector respectively. Let $\boldsymbol { \nu } ^ { ( k ) } = ( \nu \{ ^ { k ) } , \nu \{ ^ { k ) } , \cdots , \nu _ { n } ^ { ( k ) } )$ where $\nu _ { i } ^ { ( k ) }$ is the position of the ith alternative in $w _ { ( k ) } .$ Similarly, let $\boldsymbol { \nu } ^ { c } = ( \nu _ { 1 } ^ { c } , \nu _ { 2 } ^ { c } , \cdots , \nu _ { n } ^ { c } )$ , where v<sup>c</sup> is the position of the ith alternative in $w ^ { c } .$ Then, the ordinal consensus index of $A _ { k }$ is de<sup>fi</sup>ned by $O C I ( A _ { k } ) = ( 1 /$ n) $\sum { } _ { i = 1 } ^ { n } \lvert \nu _ { i } ^ { ( k ) } - \nu _ { i } ^ { c } \rvert .$ . If $O C I \left( A ^ { ( k ) } \right)$ <sup></sup>≤OCI,∀k, where OCI is a prede<sup>fi</sup>ned threshold, we conclude that an acceptable ordinal consensus is reached. A similar algorithm to Algorithm 2 can be established based on these indicators. To show the proposed decision support model works under these indicators, we still use the data from Example 1. When setting OCI 0 and $\gamma = 0 . 9 ,$ we apply the proposed <sup>¼</sup>model to adjust the given multiplicative preference relations. The algorithm ends after 8 steps. Resulting indicators are listed in Table 2. We <sup>fi</sup>nd only $A _ { 5 }$ is modi<sup>fi</sup>ed. The modi<sup>fi</sup>ed preference relation for the 5th decision maker and the <sup>fi</sup>nal group preference relation are denoted as $\overline { { A _ { 5 } } }$ and $\overline { { A _ { c } } } .$ The corresponding priority vectors w and w are also listed below. The results show that the proposed model is suitable for dealing with ordinal consensus.

$$
\begin{array}{c} \overline {{\overline {{A _ {5}}}}} = \left( \begin{array}{c c c c} 1. 0 0 0 0 & 1. 1 6 9 8 & 2. 0 3 1 6 & 3. 4 0 4 4 \\ 0. 8 5 4 9 & 1. 0 0 0 0 & 2. 5 0 9 6 & 3. 5 3 3 8 \\ 0. 4 9 2 2 & 0. 3 9 8 5 & 1. 0 0 0 0 & 3. 0 3 5 0 \\ 0. 2 9 3 7 & 0. 2 8 3 0 & 0. 3 2 9 5 & 1. 0 0 0 0 \end{array} \right), \\ \overline {{\overline {{A _ {c}}}}} = \left( \begin{array}{c c c c} 1. 0 0 0 0 & 2. 8 7 3 8 & 4. 2 9 9 2 & 5. 9 7 5 0 \\ 0. 3 4 8 0 & 1. 0 0 0 0 & 3. 1 9 0 4 & 4. 2 0 1 9 \\ 0. 2 3 2 6 & 0. 3 1 3 4 & 1. 0 0 0 0 & 2. 2 6 6 6 \\ 0. 1 6 7 4 & 0. 2 3 8 0 & 0. 4 4 1 2 & 1. 0 0 0 0 \end{array} \right), \end{array}
$$

w 0:3613; 0:3588; 0:1917; 0:0882 <sup>T</sup>;

$$
\overline {{\overline {{w _ {c}}}}} = (0. 5 4 3 7, \quad 0. 2 7 2 2, \quad 0. 1 1 7 2, \quad 0. 0 6 6 9) ^ {T}.
$$

Example 3. Consider the following problem [53]. There are three individuals, who are managers from the design, manufacturing and marketing departments, participating in a group decision about new product development strategy through AHP. The <sup>fi</sup>ve decision criteria for new product development are cost, manufacturability, quality, technological improvement and market share, denoted as $C _ { 1 } , C _ { 2 } , C _ { 3 } ,$ $C _ { 4 } , C _ { 5 }$ respectively. The three managers give their preferences over the <sup>fi</sup>ve criteria by multiplicative preference relations. The multiplicative preference relations $A _ { k }$ and the corresponding weight vector $w ^ { k }$ (k = 1, 2, 3) for criteria are calculated accordingly.

$$
A _ {1} = \left( \begin{array}{c c c c c} 1 & 5 & 7 & 3 & 1 / 3 \\ 1 / 5 & 1 & 3 & 1 / 3 & 1 / 5 \\ 1 / 7 & 1 / 3 & 1 & 1 / 7 & 1 / 9 \\ 1 / 3 & 3 & 7 & 1 & 1 / 3 \\ 3 & 5 & 9 & 3 & 1 \end{array} \right), A _ {2} = \left( \begin{array}{c c c c c} 1 & 1 / 3 & 7 & 1 / 2 & 3 \\ 3 & 1 & 3 & 1 & 5 \\ 1 & 1 / 3 & 1 & 1 / 3 & 3 \\ 2 & 1 & 3 & 1 & 5 \\ 1 / 3 & 1 / 5 & 1 / 3 & 1 / 5 & 1 \end{array} \right),
$$

$$
\begin{array}{l} w ^ {(1)} = (0. 2 8 1 3, 0. 0 6 9 5, 0. 0 3 2 1, 0. 1 5 9 0, 0. 4 5 8 1) ^ {T}, \\ w ^ {(2)} = (0. 1 4 1 8, 0. 3 4 9 7, 0. 1 3 1 2, 0. 3 2 1 7, 0. 0 5 5 5) ^ {T} \end{array}
$$

$$
A _ {3} = \left( \begin{array}{c c c c c} 1 & 7 & 5 & 4 & 3 \\ 1 / 7 & 1 & 1 / 3 & 1 / 4 & 1 / 5 \\ 1 / 5 & 3 & 1 & 1 / 3 & 1 / 4 \\ 1 / 4 & 4 & 3 & 1 & 1 \\ 1 / 3 & 5 & 4 & 1 & 1 \end{array} \right),
$$

$$
A ^ {c} = \left( \begin{array}{c c c c c} 1. 0 0 0 0 & 2. 2 6 8 0 & 3. 2 7 1 1 & 1. 8 1 7 1 & 1. 4 4 2 2 \\ 0. 4 4 0 9 & 1. 0 0 0 0 & 1. 4 4 2 2 & 0. 4 3 6 8 & 0. 5 8 4 8 \\ 0. 3 0 5 7 & 0. 6 9 3 4 & 1. 0 0 0 0 & 0. 2 5 1 3 & 0. 4 3 6 8 \\ 0. 5 5 0 3 & 2. 2 8 9 4 & 3. 9 7 9 1 & 1. 0 0 0 0 & 1. 1 8 5 6 \\ 0. 6 9 3 4 & 1. 7 1 0 0 & 2. 2 8 9 4 & 0. 8 4 3 4 & 1. 0 0 0 0 \end{array} \right),
$$

$$
w ^ {(3)} = (0. 4 8 7 8, 0. 0 4 3 6, 0. 0 8 0 9, 0. 1 7 8 0, 0. 2 0 9 8) ^ {T},
$$

$$
w ^ {c} = (0. 3 2 6 4, 0. 1 2 3 2, 0. 0 8 4 1, 0. 2 5 7 4, 0. 2 0 8 8) ^ {T}
$$

Without loss of generality, each manager is assumed to have equal importance and let $\lambda { = } ( 1 / 3 , 1 / 3 , 1 / 3 )$ be their weight vector. From the above multiplicative preference relations, we calculate the group multiplicative preference relation $A ^ { c }$ using (1) and the corresponding priority vector $\overline { { w ^ { c } } }$ which are listed above.

In the following, we show how to apply the GDM support model described in Section 4 to obtain a solution based on consistency and consensus.

Stage 1: Consistency control process.

The initial consistency indexes are shown in Table 2. If we <sup>fi</sup>x a minimum threshold value CI 1:1, we see that all the multiplicative preference relations are of acceptable consistency, which is consistent with the results of Saaty's consistency ratio (CR) [53].

Table 2  
Consistency and consensus indexes for Example 2.

<table><tr><td></td><td>Consistency indexes</td><td>Ordinal consensus indexes</td><td> $CI_H(A^c)$ </td></tr><tr><td>Original</td><td>(1.0255, 1.0450, 1.0226, 1.0314, 1.0241)</td><td>(0, 0, 0, 0, 1)</td><td>1.0215</td></tr><tr><td>Modified</td><td>(1.0255, 1.0450, 1.0226, 1.0314, 1.0176)</td><td>(0, 0, 0, 0, 0)</td><td>1.0253</td></tr></table>

Stage 2: Consensus reaching process.

The group consensus indexes for each decision maker are listed in Table 2. Here, the consensus level is set at GCI 1:1. As all the preference relations do not reach the consensus level, we continue to carry out Algorithm 2. Set γ=0.9, the algorithm is terminated after 20 steps. We <sup>fi</sup>nd that all three preference relations are modi<sup>fi</sup>ed. Speci<sup>fi</sup>cally, $A _ { 1 } , A _ { 2 }$ and $A _ { 3 }$ have been modi<sup>fi</sup>ed 4, 14, and 2 times respectively. The <sup>fi</sup>nal modi<sup>fi</sup>ed individual multiplicative preference relations and group multiplicative preference relation and their corresponding prioritization vectors are given below.

$$
\overline {{A _ {1}}} = \left( \begin{array}{c c c c c} 1. 0 0 & 4. 5 3 & 5. 9 7 & 2. 8 4 & 0. 5 3 \\ 0. 2 2 & 1. 0 0 & 2. 1 7 & 0. 3 4 & 0. 2 4 \\ 0. 1 7 & 0. 4 7 & 1. 0 0 & 0. 1 7 & 0. 1 5 \\ 0. 3 5 & 2. 9 5 & 5. 8 7 & 1. 0 0 & 0. 4 6 \\ 1. 9 0 & 4. 1 9 & 6. 6 3 & 2. 1 9 & 1. 0 0 \end{array} \right),
$$

$$
\overline {{A _ {2}}} = \left( \begin{array}{c c c c c} 1. 0 0 & 1. 9 6 & 2. 9 7 & 1. 6 5 & 1. 5 7 \\ 0. 5 1 & 1. 0 0 & 1. 4 8 & 0. 4 6 & 0. 6 9 \\ 0. 3 4 & 0. 6 7 & 1. 0 0 & 0. 2 6 & 0. 5 1 \\ 0. 6 1 & 2. 1 5 & 3. 8 5 & 1. 0 0 & 1. 3 5 \\ 0. 6 4 & 1. 4 4 & 1. 9 5 & 0. 7 4 & 1. 0 0 \end{array} \right),
$$

$$
\begin{array}{l} \overline {{w ^ {(1)}}} = (0. 3 1 6 0, 0. 0 7 5 5, 0. 0 4 2 5, 0. 1 8 2 3, 0. 3 8 3 7) ^ {T}, \\ \overline {{w ^ {(2)}}} = (0. 3 1 4 9, 0. 1 3 6 0, 0. 0 9 0 2, 0. 2 6 8 4, 0. 1 9 0 5) ^ {T} \end{array}
$$

$$
\overline {{A _ {3}}} = \left( \begin{array}{c c c c c} 1. 0 0 & 6. 2 6 & 4. 8 9 & 3. 6 9 & 2. 5 7 \\ 0. 1 6 & 1. 0 0 & 0. 4 2 & 0. 2 7 & 0. 2 2 \\ 0. 2 0 & 2. 4 1 & 1. 0 0 & 0. 3 1 & 0. 2 5 \\ 0. 2 7 & 3. 7 7 & 3. 1 9 & 1. 0 0 & 0. 9 7 \\ 0. 3 9 & 4. 5 6 & 3. 9 4 & 1. 0 3 & 1. 0 0 \end{array} \right),
$$

$$
\overline {{A ^ {c}}} = \left( \begin{array}{c c c c c} 1. 0 0 0 0 & 3. 8 1 7 1 & 4. 4 2 5 5 & 2. 5 8 5 1 & 1. 2 8 4 7 \\ 0. 2 6 2 0 & 1. 0 0 0 0 & 1. 0 9 7 9 & 0. 3 4 7 1 & 0. 3 3 1 0 \\ 0. 2 2 6 0 & 0. 9 1 0 9 & 1. 0 0 0 0 & 0. 2 4 0 4 & 0. 2 6 9 7 \\ 0. 3 8 6 8 & 2. 8 8 1 4 & 4. 1 6 0 5 & 1. 0 0 0 0 & 0. 8 4 1 9 \\ 0. 7 7 8 4 & 3. 0 2 1 0 & 3. 7 0 7 4 & 1. 1 8 7 8 & 1. 0 0 0 0 \end{array} \right),
$$

$$
\begin{array}{l} \overline {{w ^ {(3)}}} = (0. 4 6 6 9, 0. 0 4 9 2, 0. 0 7 8 8, 0. 1 8 6 3, 0. 2 1 8 7) ^ {T}, \\ \overline {{w ^ {c}}} = (0. 3 7 2 2, 0. 0 8 2 2, 0. 0 6 9 1, 0. 2 1 7 7, 0. 2 5 8 7) ^ {T} \end{array}
$$

The consistency and consensus indexes are listed in Table 3. Stage 3: Selection process. Thus the ranking of <sup>fi</sup>ve criteria is $C _ { 1 } { > } C _ { 5 } { > } C _ { 4 } { > } C _ { 2 } { > } C _ { 3 } ,$ which indicates that $C _ { 1 }$ is the most important criterion.

Table 3  
Consistency and consensus indexes for Example 3.

<table><tr><td></td><td>Consistency indexes</td><td>Consensus indexes</td><td> $CI_{H}(A^{c})$ </td></tr><tr><td>Original</td><td>(1.0543, 1.0112, 1.0407)</td><td>(1.1.4133, 1.9800, 1.2953)</td><td>1.0110</td></tr><tr><td>Modified</td><td>(1.0326, 1.0103, 1.0319)</td><td>(1.0964, 1.0911, 1.0898)</td><td>1.0138</td></tr></table>

In [53], the <sup>fi</sup>nal weight vector of <sup>fi</sup>ve criteria is $w =$ (0.3743, 0.1228, 0.0833, 0.1867, 0.2270)<sup>T</sup>, which leads to the same results as our paper. Our results also verify the consensus criteria based on a group strong agreement quotient (GSAQ) and a group strong disagreement quotient (GSDQ) [53]. Compared to the method in [53], our decision support model is very effective due to its simpler structure and reduced computation complexity.

## 7. Conclusions

In a GDM context, prior to the selection of the best alternative, it would be desirable that decision makers achieve a high degree of consensus while keeping their preferences rational. In this paper we have investigated a decision support model which simultaneously addresses the individual consistency and group consensus. The main work presented in this paper is summarized as follows:

(1) We have proposed a new consistency measure for multiplicative preference relations. An algorithm has been presented to make a multiplicative preference relation of acceptable consistency. We have shown that our consistency improvement method is related to Saaty's consistency index.

(2) We have also proposed a consensus index to measure the consensus level. For both the consistency and consensus measures, the concept of a deviation measure has been used based on the Hadamard product of two matrices. A consensus reaching process has been put forward to help the group reach a prede<sup>fi</sup>ned consensus level.

(3) A framework for the decision support model has been presented to aid the whole GDM process based on preference relations. The effectiveness of the proposed model has been illustrated by three numerical examples.

Our model's main improvement is that it is independent of the prioritization method used in the entire consensus scheme. The model guarantees that each of the individual multiplicative preference relation is still rational and of acceptable consistency. As a consequence, the proposed model allows us to achieve a higher level of consistency and consensus solutions for a GDM with preference relations. The consistency concepts and corresponding properties of our GDM model can be extended to deal with other kinds of preference relations.

## Acknowledgments

The authors are very grateful to the Editor-in-Chief, Professor A.B. Whinston, and the three anonymous referees, for their constructive comments and suggestions that have improved the quality of the paper. This research was supported by the Key Program of National Natural Science Foundation of China (Grant No. 70831005), and Major Bidding Program of National Social Science Foundation of China (Grant No. 08&ZD009), and also supported by Projects of International Cooperation and Exchanges NSFC (Grant No. 71011140076).

## Appendix A

Proof of Theorem 2. From step 4 of Algorithm 1 and (5), we have that

$$
\begin{array}{l} a _ {i j, h + 1} = \Big (a _ {i j, h} \Big) ^ {\theta} \Big (g _ {i j, h} \Big) ^ {1 - \theta}, \\ g _ {i j, h + 1} = \prod_ {l = 1} ^ {n} \Big (a _ {i l, h + 1} a _ {l j, h + 1} \Big) ^ {1 / n} = \prod_ {l = 1} ^ {n} \left[ \Big (a _ {i l, h} a _ {l j, h} \Big) ^ {\theta} \Big (g _ {i l, h} g _ {l j, h} \Big) ^ {1 - \theta} \right] ^ {1 / n} = g _ {i j, h}. \end{array}
$$

Consequently, we obtain

$$
\begin{array}{c} a _ {i j, h + 1} g _ {j i, h + 1} = \left(a _ {i j, h}\right) ^ {\theta} \Big (g _ {i j, h} \Big) ^ {1 - \theta} g _ {j i, h} = \left(a _ {i j, h}\right) ^ {\theta} \Big (g _ {j i, h} \Big) ^ {\theta - 1} g _ {j i, h} \\ = \left(a _ {i j, h} g _ {j i, h}\right) ^ {\theta}. \end{array}
$$

From Lemma 2, it follows that

$$
\begin{array}{l} a _ {i j, h + 1} g _ {j i, h + 1} + a _ {j i, h + 1} g _ {i j, h + 1} = \left(a _ {i j, h} g _ {j i, h}\right) ^ {\theta} + \left(a _ {j i, h} g _ {i j, h}\right) ^ {\theta} \leq a _ {i j, h} g _ {j i, h} \\ \quad + a _ {j i, h} g _ {i j, h}. \end{array}
$$

Since $A ^ { ( h ) } \neq G ^ { ( h ) }$ , there is at least one pair $( i , j )$ such that the above expression strictly holds. Thus, we have

$$
\begin{array}{l} \frac {1}{n ^ {2}} \sum_ {i = 1} ^ {n - 1} \sum_ {j = i + 1} ^ {n} \left(a _ {i j, h + 1} g _ {j i, h + 1} + a _ {j i, h + 1} g _ {i j, h + 1}\right) \\ \quad + \frac {1}{n} <   \frac {1}{n ^ {2}} \sum_ {i = 1} ^ {n - 1} \sum_ {j = i + 1} ^ {n} \left(a _ {i j, h} g _ {j i, h} + a _ {j i, h} g _ {i j, h}\right) + \frac {1}{n}. \end{array}
$$

That is, $C I _ { H } ( A _ { h + 1 } ) { < } C I _ { H } ( A _ { h } )$ . From De<sup>fi</sup>nition $6 ,$ we have $C I _ { H } ( A _ { h } ) \geq 1$ ∀h. Therefore, the sequence $\{ C I _ { H } ( A _ { h } ) \}$ is monotone decreasing and has a lower bound. Applying the limit existence theorem for a sequence, we know that $\operatorname* { l i m } _ { h \to \infty } C I _ { H } ( A _ { h } )$ exists. Let $\boldsymbol { A } ^ { \infty } = \operatorname* { l i m } _ { h  \infty } \boldsymbol { A } _ { h }$ . Assume that

$$
C I _ {H} \left(A ^ {\infty}\right) = \lim _ {h \rightarrow \infty} C I _ {H} \left(A _ {h}\right) = i n f \left\{C I _ {H} \left(A _ {h}\right)\right\}
$$

Using proof by contradiction, it can be shown that $\operatorname* { l i m } _ { h  \infty } C I _ { H } ( A _ { h } ) { \leq } \alpha \cdot$ . This completes the proof of Theorem 2.

Proof of Theorem 3. From step 4 of Algorithm 1, we have

$$
A _ {h + 1} = (A _ {h}) ^ {\theta} \circ (G _ {h}) ^ {1 - \theta}.
$$

Since $G _ { h }$ is a virtual consistent multiplicative preference relation, we have $\lambda _ { m a x } ( G _ { h } ) = n$ and $\lambda _ { m a x } ( G _ { h } ) < \lambda _ { m a x } ( A _ { h } )$ . Therefore, from Lemma 3, we have

$$
\rho \left(A _ {h + 1}\right) \leq \left(\rho \left(A _ {h}\right)\right) ^ {\alpha} \left(\rho \left(G _ {h}\right)\right) ^ {1 - \alpha} <   \left(\rho \left(A _ {h}\right)\right) ^ {\alpha} \left(\rho \left(A _ {h}\right)\right) ^ {1 - \alpha} = \rho \left(A _ {h}\right).
$$

This completes the proof of Theorem 3.

Proof of Theorem 4. From De<sup>fi</sup>nition 7, we have

$$
d \left(A ^ {c}, A _ {k}\right) = \frac {1}{n ^ {2}} \sum_ {i = 1} ^ {n} \sum_ {j = 1} ^ {n} a _ {i j} ^ {c} a _ {j i} ^ {(k)}, \quad d \left(A _ {l}, A _ {k}\right) = \frac {1}{n ^ {2}} \sum_ {i = 1} ^ {n} \sum_ {j = i} ^ {n} a _ {i j} ^ {(l)} a _ {j i} ^ {(k)}.
$$

At the same time, from Lemma 1, we have

$$
a _ {i j} ^ {c} a _ {j i} ^ {(k)} = \prod_ {l = 1} ^ {m} \left(a _ {i j} ^ {(l)}\right) ^ {\lambda_ {l}} a _ {j i} ^ {(k)} \leq \sum_ {l = 1} ^ {m} \lambda_ {l} a _ {i j} ^ {(l)} a _ {j i} ^ {(k)}.
$$

It follows that

$$
\begin{array}{l} d (A ^ {c}, A _ {k}) \leq \frac {1}{n ^ {2}} \sum_ {i = 1} ^ {n} \sum_ {j = 1} ^ {n} \left(\sum_ {l = 1} ^ {m} \lambda_ {l} a _ {i j} ^ {(l)} a _ {j i} ^ {(k)}\right) = \frac {1}{n ^ {2}} \sum_ {l = 1} ^ {m} \lambda_ {l} \sum_ {i = 1} ^ {n} \sum_ {j = 1} ^ {n} \left(a _ {i j} ^ {(l)} a _ {j i} ^ {(k)}\right) \\ = \sum_ {l = 1} ^ {m} \lambda_ {l} d (A _ {l}, A _ {k}) \leq \sum_ {l = 1} ^ {m} \lambda_ {l} \max _ {l} \left\{d (A _ {l}, A _ {k}) \right\} = \max _ {l} \left\{d (A _ {l}, A _ {k}). \right. \end{array}
$$

This completes the proof of Theorem 4.

Proof of Theorem 5. From (1) and (21), we have

$$
\begin{array}{l} a _ {i j, h + 1} ^ {c} = \prod_ {p = 1} ^ {m} \left(a _ {i j, h + 1} ^ {(p)}\right) ^ {\lambda_ {p}} = \prod_ {p = 1, p \neq k} ^ {m} \left(a _ {i j, h + 1} ^ {(p)}\right) ^ {\lambda_ {p}} \left(a _ {i j, h + 1} ^ {(k)}\right) ^ {\lambda_ {k}} \\ = \prod_ {p = 1, p \neq k} ^ {m} \left(a _ {i j, h} ^ {(p)}\right) ^ {\lambda_ {p}} \left(\left(a _ {i j, h} ^ {(k)}\right) ^ {\gamma} \left(a _ {i j, h} ^ {c}\right) ^ {1 - \gamma}\right) ^ {\lambda_ {k}} \\ = \prod_ {p = 1, p \neq k} ^ {m} \left(a _ {i j, h} ^ {(p)}\right) ^ {\lambda_ {p}} \left(a _ {i j, h} ^ {(k)}\right) ^ {\lambda_ {k}} \left(\left(a _ {i j, h} ^ {(k)}\right) ^ {\gamma - 1} \left(a _ {i j, h} ^ {c}\right) ^ {1 - \gamma}\right) ^ {\lambda_ {k}} \\ = a _ {i j, h} ^ {c} \left(a _ {j i, h} ^ {(k)} a _ {i j, h}\right) ^ {(1 - \gamma) \lambda_ {k}}. \end{array}
$$

For the decision maker k, we get the following

$$
\begin{array}{c} a _ {i j, h + 1} ^ {(k)} a _ {j i, h + 1} ^ {c} = \left(a _ {i j, h} ^ {(k)}\right) ^ {\gamma} \left(a _ {i j, h} ^ {c}\right) ^ {1 - \gamma} a _ {j i, h} ^ {c} \left(a _ {i j, h} ^ {(k)} a _ {j i, h} ^ {c}\right) ^ {(1 - \gamma) \lambda_ {k}} \\ = \left(a _ {i j, h} ^ {(k)} a _ {j i, h} ^ {c}\right) ^ {\gamma} \left(a _ {i j, h} ^ {(k)} a _ {j i, h} ^ {c}\right) ^ {(1 - \gamma) \lambda_ {k}} = \left(a _ {i j, h} ^ {(k)} a _ {j i, h} ^ {c}\right) ^ {\gamma + (1 - \gamma) \lambda_ {k}}. \end{array}
$$

Letting $\theta = \gamma + ( 1 - \gamma ) \lambda _ { k }$ , then 0bθb1. From Lemma 2, for $i \neq j$ , we have

$$
a _ {i j, h + 1} ^ {(k)} a _ {j i, h + 1} ^ {c} + a _ {j i, h + 1} ^ {(k)} a _ {i j, h + 1} ^ {c} = \left(a _ {i j, h} ^ {(k)} a _ {j i, h} ^ {c}\right) ^ {\theta} + \left(a _ {j i, h} ^ {(k)} a _ {i j, h} ^ {c}\right) ^ {\theta} <   a _ {i j, h} ^ {(k)} a _ {j i, h} ^ {c} + a _ {j i, h} ^ {(k)} a _ {i j, h} ^ {c}.
$$

It implies that

$$
\begin{array}{l} \frac {1}{n ^ {2}} \sum_ {i = 1} ^ {n - 1} \sum_ {j = i + 1} ^ {n} \left(a _ {i j, h + 1} ^ {(k)} a _ {j i, h + 1} ^ {c} + a _ {j i, h + 1} ^ {(k)} a _ {i j, h + 1} ^ {c}\right) \\ \quad + \frac {1}{n} <   \frac {1}{n ^ {2}} \sum_ {i = 1} ^ {n - 1} \sum_ {j = i + 1} ^ {n} \left(a _ {i j, h} ^ {(k)} a _ {j i, h} ^ {c} + a _ {j i, h} ^ {(k)} a _ {i j, h} ^ {c}\right) + \frac {1}{n}. \end{array}
$$

Hence, we have $G C I _ { H } ( A _ { k , h + 1 } ) { < } G C I _ { H } ( A _ { k , h } )$ . This completes the proof of Theorem 5.

Proof of Theorem 6. We suppose the kth decision maker has to change his\her multiplicative preference relation in the hth iteration. We consider two cases. For $l { = } k ,$ , since $A _ { k , h + 1 }$ is a weighted combination of $A _ { k , h }$ and $A _ { h } ^ { c } ,$ from Theorem 1, we have

$$
C I _ {H} \left(A _ {k, h + 1}\right) \leq \max \left\{C I _ {H} \left(A _ {k, h}\right), C I _ {H} (A _ {h}) \right\}.
$$

Then, from the de<sup>fi</sup>nition of $A _ { h } ^ { c } ,$ we obtain that $C I _ { H } ( A _ { h } ^ { c } ) \leq$ max<sub>l</sub> $\left\{ C I _ { H } \left( A _ { l , h } \right) \right\}$ . Consequently,

$$
C I _ {H} \left(A _ {k, h + 1}\right) \leq \max \left\{C I _ {H} \left(A _ {k, h}\right), \max _ {l} \left\{C I _ {H} \left(A _ {l, h}\right) \right\} \right\} = \max _ {l} \left\{C I _ {H} \left(A _ {l, h}\right) \right\}.
$$

For $l \neq k ,$ , we have $C I _ { H } ( A _ { l , h + 1 } ) = C I _ { H } ( A _ { l , h } )$ . Summarizing both cases, we have

$$
\max _ {l} \left\{C I _ {H} \left(A _ {l, h + 1}\right) \right\} \leq \max _ {l} \left\{C I _ {H} \left(A _ {l, h}\right) \right\}.
$$

This completes the proof of Theorem 6.

## References

[1] S. Alonso, F.J. Cabrerizo, F. Chiclana, F. Herrera, E. Herrera-Viedma, Group decision making with incomplete fuzzy linguistic preference relations, International Journal of Intelligent Systems 24 (2009) 201–222.

[2] S. Alonso, E. Herrera-Viedma, F. Chiclana, F. Herrera, A web based consensus support system for group decision making problems and incomplete preferences, Information Sciences 180 (2010) 4477–4495

[3] D. Ben-Arieh, T. Easton, Multi-criteria group consensus under linear cost opinion elasticity, Decision Support Systems 43 (2007) 713–721.

[4] N. Bryson, Group decision-making and the analytic hierarchy process: exploring the consensus-relevant information content, Computers and Operations Research 23 (1996).27-35

[5] F.J. Cabrerizo, J.M. Moreno, I.J. Pérez, E. Herrera-Viedma, Analyzing consensus approaches in fuzzy group decision making: advantages and drawbacks, Soft Computing 14 (2010) 451–463.

[6] G. Campanella, R.A. Ribeiro, A framework for dynamic multiple-criteria decision making, Decision Support Systems (2011), doi:10.1016/j.dss.2011.05.003.

[7] D. Cao, L.C. Leung, J.S. Law, Modifying inconsistent comparison matrix in analytic hierarchy process: a heuristic approach, Decision Support Systems 44 (2008) 944–953.

[8] Y.L. Chen, L.C. Cheng, An approach to group ranking decisions in a dynamic environment, Decision Support Systems 48 (2010) 622–634.

[9] F. Chiclana, F. Herrera, E. Herrera-Viedma, Integrating three representation models in fuzzy multipurpose decision making based on fuzzy preference relations, Fuzzy Sets and Systems 97 (1998) 33–48.

[10] F. Chiclana, F. Herrera, E. Herrera-Viedma, Integrating multiplicative preference relations in a multipurpose decision-making model based on fuzzy preference relations, Fuzzy Sets and Systems 122 (2001) 277–291.

[11] F. Chiclana, E. Herrera-Viedma, S. Alonso, F. Herrera, Cardinal consistency of reciprocal preference relations: a characterization of multiplicative transitivity, IEEE Transactions on Fuzzy Systems 17 (2009) 14–23.

[12] F. Chiclana, F. Mata, L. Martínez, E. Herrera-Viedma, S. Alonso, Integration of a consistency control module within a consensus decision making model, International Journal of Uncertainty, Fuzziness and Knowledge-Based Systems 16 (1) (2008) 35–53.

[13] A.K. Choudhury, R. Shankar, M.K. Tiwari, Consensus-based intelligent group decision-making model for the selection of advanced technology, Decision Support Systems 42 (2006) 1776–1799.

[14] G. Crawford, C. Williams, A note on the analysis of subjective judgement matrices, Journal of Mathematical Psychology 29 (1985) 387–405.

[15] Y. Dong, Y. Xu, H. Li, On consistency measures of linguistic preference relations, European Journal of Operational Research 189 (2008) 430–444.

[16] Y. Dong, Y. Xu, H. Li, B. Feng, The OWA-based consensus operator under linguistic representation models using position indexes, European Journal of Operational Research 203 (2010) 455–463.

[17] Y. Dong, G. Zhang, W.-H. Hong, Y. Xu, Consensus models for AHP group decision making under row geometric mean prioritization method, Decision Support Systems 49 (2010) 281–289.

[18] M.T. Escobar, J.M. Moreno-Jiménez, Aggregation of individual preference structures in AHP group decision making, Group Decision and Negotiation 16 (2007) 287–301.

[19] E. Forman, K. Peniwati, Aggregating individual judgments and priorities with the analytic hierarchy process, European Journal of Operational Research 108 (1998) 165–169.

[20] C. Fu, S.L. Yang, The group consensus based evidential reasoning approach for multiple attributive group decision analysis, European Journal of Operational Research 206 (2010) 601–608.

[21] F. Herrera, E. Herrera-Viedma, J.L. Verdegay, A rational consensus model in group decision making using linguistic assessments, Fuzzy Sets and Systems 88 (1997) 31–49.

[22] F. Herrera, S. Alonso, F. Chiclana, E. Herrera-Viedma, Computing with words in decision making: foundations, trends and prospects, Fuzzy Optimization and Decision Making 8 (2009) 337–364

[23] F. Herrera, E. Herrera-Viedma, F. Chiclana, Multiperson decision-making based on multiplicative preference relations, European Journal of Operational Research 129 (2001) 372–385.

[24] E. Herrera-Viedma, F. Herrera, F. Chiclana, A consensus model for multiperson decision making with different preference structures, IEEE Transactions on Systems, Man, and Cybernetics Part A: Systems and Humans 32 (2002) 394–402.

[25] E. Herrera-Viedma, S. Alonso, F. Chiclana, F. Herrera, A consensus model for group decision making with incomplete fuzzy preference relations, IEEE Transactions on Fuzzy Systems 15 (2007) 863–877.

[26] E. Herrera-Viedma, F. Herrera, F. Chiclana, M. Luque, Some issues on consistency of fuzzy preference relations, European Journal of Operational Research 154 (2004) 98–109.

[27] E. Herrera-Viedma, L. Martínez, F. Mata, F. Chiclana, A consensus support systems model for group decision making problems with multigranular linguistic preference relations, IEEE Transactions on Fuzzy Systems 13 (2005) 644–658.

[28] R.A. Horn, C.R. Johnson, Matrix Analysis, Cambridge University Press, Cambridge, 1985.

[29] R.A. Horn, C.R. Johnson, Topics in Matrix Analysis, Cambridge University Press, Cambridge, 1991.

[30] S.M. Huang, W.H. Hung, D.C. Yen, I.C. Chang, D. Jiang, Building the evaluation model of the IT general control for CPAs under enterprise risk management, Decision Support Systems 50 (2011) 692–701.

[31] J. Kacprzyk, M. Fedrizzi, H. Nurmi, Group decision making and consensus under fuzzy preferences and fuzzy majority, Fuzzy Sets and Systems 49 (1992) 21–31.

[32] J. Kacprzyk, S. Zadrożny, Soft computing and web intelligence for supporting consensus reaching, Soft Computing 14 (2010) 833–846.

[33] J. Ma, Z.-P. Fan, Y.-P. Jiang, J.-Y. Mao, L. Ma, A method for repairing the inconsistency of fuzzy preference relations, Fuzzy Sets and Systems 157 (2006) 210–233.

[34] L.C. Ma, H.L. Li, Using Gower Plots and Decision Balls to rank alternatives involving inconsistent preferences, Decision Support Systems 51 (2011) 712–719.

[35] F. Mata, L. Martínez, E. Herrera-Viedma, An adaptive consensus support model for group decision-making problems in a multigranular fuzzy linguistic context, IEEE Transactions on Fuzzy Systems 17 (2009) 279–290.

[36] R.O. Parreiras, P.Ya. Ekel, J.S.C. Martini, R.M. Palhares, A <sup>fl</sup>exible consensus scheme for multicriteria group decision making under linguistic assessments, Information Sciences 180 (2010) 1075–1089.

[37] R.A. Ribeiro, A.M. Moreira, P. van den Broek, A. Pimentel, Hybrid assessment method for software engineering decisions, Decision Support Systems 51 (2011) 208–219.

[38] T.L. Saaty, The Analytical Hierarchy Process, McGraw-Hill, New York, 1980.

[39] T.L. Saaty, A ratio scale metric and compatibility of ratio scales: the possibility of Arrow's impossibility theorem, Applied Mathematics Letters 7 (1994) 51–57.

[40] B. Srdjevic, Combining different prioritization methods in the analytic hierarchy process synthesis, Computers and Operations Research 32 (2005) 1897–1919.

[41] B. Srdjevic, Linking analytic hierarchy process and social choice methods to support group decision-making in water management, Decision Support Systems 42 (2007) 2261–2273.

[42] T. Tanino, Fuzzy preference orderings in group decision making, Fuzzy Sets and Systems 12 (1984) 117–131.

[43] L.F. Wang, Compatibility and group decision making, Systems Engineering Theory and Practice 20 (2000) 92–96.

[44] Y.M. Wang, K.S. Chin, G.K.K. Poon, A data envelopment analysis method with assurance region for weight generation in the analytic hierarchy process, Decision Support Systems 45 (2008) 913–921.

[45] J. Xu, Z. Wu, A discrete consensus support model for multiple attribute group decision making, Knowledge-Based Systems 24 (2011) 1196–1202.

[46] Z. Xu, C. Wei, A consistency improving method in the analytic hierarchy process, European Journal of Operational Research 116 (1999) 443–449.

[47] Z. Xu, Deviation measures of linguistic preference relations in group decision making, Omega 33 (2005) 249–254.

[48] Z. Xu, An automatic approach to reaching consensus in multiple attribute group decision making, Computers and Industrial Engineering 56 (2009) 1369–1374.

[49] Z. Xu, X.Q. Cai, Group consensus algorithms based on preference relations, Information Sciences 181 (2011) 150–162

[50] R.R. Yager, Lexicographic ordinal OWA aggregation of multiple criteria, Information Fusion 11 (2010) 374–380

[51] R.R. Yager, Weighted maximum entropy OWA aggregation with applications to decision making under risk, IEEE Transactions on Systems, Man, and Cybernetics Part A: Systems and Humans 39 (2009) 555–564.

[52] R.R. Yager, On the fusion of imprecise uncertainty measures using belief structures, Information Sciences 181 (2011) 3199–3209.

[53] J.M. Yeh, B. Kreng, C. Lin, A consensus approach for synthesizing the elements of comparison matrix in the Analytic Hierarchy Process, International Journal of Systems Science 32 (2001) 1353–1363.

[54] L. Yu, K.K. Lai, A distance-based group decision-making methodology for multiperson multi-criteria emergency decision support, Decision Support Systems 51 (2011) 307–315.

Zhibin Wu is a Ph.D. candidate at the School of Management, Sichuan University, Sichuan, China. He received his B.S. degree from the Department of Information and Computation Science, Chongqing University, China, in 2005, and his M.S. degree from the Department of Operational Research and Cybernetics, Chongqing University, China, in 2008. His research results have been published in Fuzzy Sets and Systems and Knowledge-Based Systems. His research interests include group decision making, soft computing, aggregation operators, multi-criteria decision analysis and applications, and decision support systems.

Jiuping Xu is a professor at the School of Management, Sichuan University, Sichuan, China. He obtained his Ph.D. in applied mathematics from Tsinghua University, Beijing, China and Ph.D. in physical chemistry from Sichuan University, Chengdu, China, in 1995 and 1999, respectively. His current research interests include group decision making, project management, uncertain programming, supply chain management, and applied mathematics. His research results have been published in IEEE Transaction on Fuzzy Systems, Information Sciences, Expert Systems with Applications, International Journal of Production Economics, Fuzzy Sets and Systems, Computers & Industrial Engineering, Mathematical Analysis and Applications, among others.
