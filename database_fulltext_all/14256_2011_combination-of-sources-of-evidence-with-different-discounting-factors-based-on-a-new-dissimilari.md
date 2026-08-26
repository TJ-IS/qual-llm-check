---
otero_id: 14256
otero_key: "GPDCEQXF"
title: "Combination of sources of evidence with different discounting factors based on a new dissimilarity measure"
authors: "Zhun-ga Liu; Jean Dezert; Quan Pan; Grégoire Mercier"
year: "2011"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2011.06.002"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Combination of sources of evidence with different discounting factors based on a new dissimilarity measure

Zhun-ga Liu <sup>a,c,</sup>⁎, Jean Dezert <sup>b</sup>, Quan Pan <sup>a</sup>, Grégoire Mercier <sup>c</sup>

<sup>a</sup> School of Automation, Northwestern Polytechnical University, Xi'an, 710072, PR China

<sup>b</sup> Onera, The French Aerospace Lab, F-91761 Palaiseau, France

<sup>c</sup> Telecom Bretagne, Technopole Brest-Iroise, 29238, France

## a r t i c l e i n f o

Article history: Received 8 October 2010 Received in revised form 1 June 2011 Accepted 5 June 2011 Available online 12 June 2011

Keywords: Belief functions Dissimilarity measure Discounting rule Pignistic transformation DST

## a b s t r a c t

The sources of evidence may have different reliability and importance in real applications for decision making. The estimation of the discounting (weighting) factors when the prior knowledge is unknown have been regularly studied until recently. In the past, the determination of the weighting factors focused only on reliability discounting rule and it was mainly dependent on the dissimilarity measure between basic belief assignments (bba's) represented by an evidential distance. Nevertheless, it is very dif<sup>fi</sup>cult to characterize ef<sup>fi</sup>ciently the dissimilarity only through an evidential distance. Thus, both a distance and a con<sup>fl</sup>ict coef<sup>fi</sup>cient based on probabilistic transformations BetP are proposed to characterize the dissimilarity. The distance represents the difference between bba's, whereas the con<sup>fl</sup>ict coef<sup>fi</sup>cient reveals the divergence degree of the hypotheses that two belief functions strongly support. These two aspects of dissimilarity are complementary in a certain sense, and their fusion is used as the dissimilarity measure. Then, a new estimation method of weighting factors is presented by using the proposed dissimilarity measure. In the evaluation of weight of a source, both its dissimilarity with other sources and their weighting factors are considered. The weighting factors can be applied in the both importance and reliability discounting rules, but the selection of the adapted discounting rule should depend on the actual application. Simple numerical examples are given to illustrate the interest of the proposed approach.

Crown Copyright © 2011 Published by Elsevier B.V. All rights reserved.

## 1. Introduction

The theories of evidence [2,16–18], also called theories of belief functions, are widely used in information fusion for decision making [3,8,14] as soon as the information to deal with are uncertain and possibly con<sup>fl</sup>icting and represented by basic belief assignments (bba's). In some real applications, all the sources of evidence to be combined may not have the same reliability, neither the same importance, even if no prior knowledge about the reliability and importance is known. If all the sources are considered equally reliable, the commutative and associative Dempster-Shafer's rule (DS), which has a low computation burden, will generate counter-intuitive results when the sources are highly con<sup>fl</sup>icting as pointed out by Zadeh in [22]. Since few years, many works on the discounting methods for the unreliable sources of evidence have emerged [3,12–14] to solve the problem. The basic idea of the discounting method is that if one source of evidence has the large dissimilarity with the other sources, its reliability should be low. Evidential distance [9] is always used as the dissimilarity measure in the discounting method. Nevertheless, evidential distance captures only one aspect of the dissimilarity between bba's mainly associated with a distance metric, and it is not enough to characterize the dissimilarity precisely. The determination of the discounting(weighting) factors (reliability or importance factors) in many works mainly lies in the mean of dissimilarity with the other sources without considering the in<sup>fl</sup>uence of the weight of those other sources. Moreover, these works only focus on the application of the reliability discounting rule, and the notions of importance and reliability have generally been considered as similar until very recently. However, reliability represents ability of the source to provide the correct assessment of the given problem, and importance means somehow the weight of importance granted to the source by the fusion system designer. Therefore, the reliability and the importance of sources are quite distinct notions [19].

The dissimilarity measure between two bba's plays a crucial role in the discounting method, but it is actually dif<sup>fi</sup>cult to quantify it because several aspects of dissimilarity need to be involved when establishing an ef<sup>fi</sup>cient and precise measure. In previous works, important research efforts have been done to <sup>fi</sup>nd good scalar measures to characterize the dissimilarity between two bba's, but all these proposed measures did capture only one aspect of the dissimilarity. From authors opinion, the dissimilarity between two bba's is not only characterized by a well chosen distance, but also by another aspect which re<sup>fl</sup>ects somehow the level of con<sup>fl</sup>ict between the bba's. Hence both aspects must count together when de<sup>fi</sup>ning a good and useful measure of dissimilarity. The evidential distance proposed in [9] is commonly considered as an interesting distance measure, but it is not good enough to capture the difference between bba's in some cases as it will be seen, and its computation burden can become important. The mass of belief committed to the empty set resulting from the conjunctive rule of sources is generally used to measure the degree of con<sup>fl</sup>ict [20], but such measure is not always very appropriate, especially for equal and cognitively independent belief functions as shown in [13]. In other words, the mass of belief committed to the empty set cannot ef<sup>fi</sup>ciently measure the divergence between distinct hypotheses strongly supported by each source. When working in the probabilistic framework, the focal elements are singletons and exclusive, and the degree of the con<sup>fl</sup>ict and distance become easier to compute regardless the intrinsic relationship between bba's. The well known probabilistic transformation BetP, introduced in [21] is an easy way to approximate any bba into a subjective probability measure and this is the transformation we have adopted in this work. A more ef<sup>fi</sup>cient (but more complex) transformation can be found in [18].

In this paper, the dissimilarity measure between two bba's is de<sup>fi</sup>ned from both a distance criterion and their intrinsic level of con<sup>fl</sup>ict criterion based on BetP. The distance criterion measures the total difference between the bba's, whereas the con<sup>fl</sup>ict criterion reveals the degree of divergences between the distinct hypotheses strongly supported by each source. These two criteria are mutually compensable in a certain sense. So the fusion of the distance and the con<sup>fl</sup>ict criteria by Hamacher T-conormes fusion rule [7] is used <sup>fi</sup>nally as the new scalar dissimilarity measure. We propose also to compute the discounting (weighting) factors of sources from the Perron–Frobenius eigenvalue of the agreement matrix de<sup>fi</sup>ned from the dissimilarities of bba's. The discounting factors can be applied in the importance discounting rule or in the reliability discounting rule. The interest of our new dissimilarity measure and the determination of discounting factors are illustrated through simple numerical examples. This paper is organized as follows. In Section 2, the distance between bba's is introduced. In Section 3, the measure of intrinsic con<sup>fl</sup>ict is presented. In Section $^ { 4 , }$ the new dissimilarity measure obtained from the fusion of the distance criterion and the con<sup>fl</sup>ict criterion is explained. A new method for automatic determination of discounting factors is presented in section 5 and a numerical example is given in Section 6. Section 7 concludes this paper.

## 2. Distance between bba's

Usually a distance between two bba's is de<sup>fi</sup>ned to characterize the dissimilarity measure between two sources of evidence. The choice for a well-adapted distance is not easy and many distances have been proposed as shown in [10]. In this paper, we present some commonly used distances including Jousselme's evidential distance $d _ { J }$ [9], Bhattacharyya's distance $d _ { B }$ [15], and the MaxDiff distance proposed in Liu.

## 2.1. Jousselme's distance and Bhattacharyya's distance

## • Jousselme's distance

Jousselme's distance $d _ { J } [ 9 ]$ is commonly used because it takes into account both the mass and the cardinality of focal elements of each bba's. d between $\mathbf { m } _ { 1 } = m _ { 1 } ( . )$ and $\begin{array} { r } { \mathbf { m } _ { 2 } = m _ { 2 } ( . ) } \end{array}$ is de<sup>fi</sup>ned by:

$$
d _ {J} (\mathbf {m} _ {1}, \mathbf {m} _ {2}) = \sqrt {\frac {1}{2} (\mathbf {m} _ {1} - \mathbf {m} _ {2}) ^ {\prime} \mathbf {D} (\mathbf {m} _ {1} - \mathbf {m} _ {2})}\tag{1}
$$

where D is a $2 ^ { | \Theta | } \times 2 ^ { | \Theta | }$ (conjectured positive) matrix with elements given by $\begin{array} { r } { D _ { i j } \triangleq \frac { | A _ { i } \cap B _ { j } | } { | A _ { i } \cup B _ { i } | } , A _ { i } , \dot { B _ { j } } { \in } \bar { { 2 } } ^ { \Theta } } \end{array}$

In the worst case (when all elements of the power set are focal elements), the computational complexity of this distance can become very important when the cardinality of the frame increases. A main drawback of such distance measure is that it cannot ef<sup>fi</sup>ciently consider the difference between belief of a single element and of non speci<sup>fi</sup>c element in some cases as clearly shown in the Example 1.

• Bhattacharyya's distance

Bhattacharyya's distance has been proposed in [15] as:

$$
d _ {B} = (1 - \sqrt {\mathbf {m} _ {1}} ^ {\prime} \sqrt {\mathbf {m} _ {1}}) ^ {p}\tag{2}
$$

For simplicity, we take $p = 1$ here. This distance doesn't take account of the relative speci<sup>fi</sup>city of focal elements of each bba. So it cannot ef<sup>fi</sup>ciently characterize the dissimilarity, especially between the singletons and the ignorance.

Example 1. Let's consider the frame $\Theta = \{ \theta _ { 1 } , ~ \theta _ { 2 } , ~ \cdots , ~ \theta _ { n } \}$ and the following three independent bba's

$$
\begin{array}{l l} \mathbf {m} _ {1}: & m _ {1} (\theta_ {1}) = m _ {1} (\theta_ {2}) = \dots = m _ {1} (\theta_ {n}) = 1 / n \\ \mathbf {m} _ {2}: & m _ {2} (\Theta) = 1 \\ \mathbf {m} _ {3}: & m _ {3} (\theta_ {l}) = 1, \text {   for   some   } l \in \{1, 2,... n \} \end{array}
$$

According to Eqs. (1) and (2), one gets:

$$
\begin{array}{l} d _ {J} (\mathbf {m} _ {1}, \mathbf {m} _ {2}) = d _ {J} (\mathbf {m} _ {1}, \mathbf {m} _ {3}) = \sqrt {\frac {1}{2} \left(1 - \frac {1}{n}\right)} \\ d _ {B} (\mathbf {m} _ {1}, \mathbf {m} _ {2}) = 1, \quad d _ {B} (\mathbf {m} _ {1}, \mathbf {m} _ {3}) = 1 - \frac {1}{n} \end{array}
$$

In this example, one sees that ${ \bf m } _ { 3 }$ is absolutely con<sup>fi</sup>dent in $\theta _ { l } ,$ but m and m can be considered both as very uncertain sources. Actually ${ \bf m } _ { 2 }$ corresponds to the full ignorant source, whereas the Bayesian bba $\mathbf { m } _ { 1 }$ has a full randomness, i.e. the maximal entropy. Although the intrinsic nature of uncertainty of $\mathbf { m } _ { 1 }$ and of ${ \bf m } _ { 2 }$ is different, from a decision-making point of view, the decision-maker is face to the full uncertainty for taking his/her decision. Intuitively, it is expected that $\mathbf { m } _ { 1 }$ is closer to ${ \bf m } _ { 2 }$ than to ${ \bf m } _ { 3 }$ because both sources $\mathbf { m } _ { 1 }$ and $\mathbf { m } _ { 2 }$ carry uncertainty and they yield to the complete indeterminacy in the decision-making problem. As we see, $d _ { J }$ doesn't characterize well the difference between these two very different cases because $\mathbf { m } _ { 1 }$ is at the same distance to ${ \bf m } _ { 2 }$ or to $\mathbf { m } _ { 3 } .$ The $d _ { B }$ distance between $\mathbf { m } _ { 1 }$ and ${ \bf m } _ { 2 }$ is larger than between $\mathbf { m } _ { 1 }$ and m which is not a good behavior in authors opinions because $\mathbf { m } _ { 1 }$ and ${ \bf m } _ { 2 }$ must be considered as quite similar since they represent a full uncertainty decision-making state. From such a very simple example, one sees that $d _ { J }$ and $d _ { B }$ are not well adapted to fully measure the dissimilarity between bba's.

## 2.2. Probabilistic-based distances

The main problem for evaluating the dissimilarity between two bba's lies in the relationship among their focal elements. Probabilistic transformations allow to approximate any bba into a subjective probability measure based on an underlying frame of discernment whose atomic elements are exhaustive and exclusive.

The probabilistic distance between $\mathbf { m } _ { 1 }$ and ${ \bf m } _ { 2 }$ through their approximate subjective probability measures is proposed here. Many transformations exist to approximate a bba into a subjective probability including BetP, DSmP [5], etc. We concentrate only on the well known and used transformations BetP here. Let $m ( \cdot )$ be a given bba related with Θ, and the associated BetP for any singleton $Y { \in } \Theta$ is given by [21]

$$
B e t P (Y) = \sum_ {X \subset 2 ^ {\Theta}, Y \subseteq X} \frac {1}{| X |} m (X)\tag{3}
$$

where is the cardinality of subset X. For notation convenience, we denote $P _ { \mathrm { m _ { i } } } ( . ) \triangleq B e t P _ { \mathrm { m _ { i } } } ( . )$

## • The MaxDiff distance

In 2006, Liu proposed MaxDiff distance in [11] as

$$
\operatorname{MaxDiff} \left(\mathbf {m} _ {1}, \mathbf {m} _ {2}\right) = \max _ {A \in \Theta} \left| P _ {\mathbf {m} _ {1}} (A) - P _ {\mathbf {m} _ {2}} (A) \right|\tag{4}
$$

MaxDiff distance re<sup>fl</sup>ects the variation only by the maximal distance between the pignistic probabilities of a pair of the individual element. However, it is not adapted for measuring precisely the total amount of difference between two bba's.

## • Minkowski's based distance

In this paper, we propose to use the DistP distance based on Minkowski's distance de<sup>fi</sup>ned as follows: for t≥1, one takes

$$
DistP_{t}(m_{1},m_{2}) = \left(\frac{1}{2}\sum_{\substack{\theta_{i}\in \Theta \\ |\theta_{i}| = 1}}|P_{\mathbf{m}_{1}}(\theta_{i}) - P_{\mathbf{m}_{2}}(\theta_{i})|^{t}\right)\frac{1}{t}\tag{5}
$$

The coef<sup>fi</sup>cient ${ \frac { 1 } { 2 } } \mathrm { i n } \left( 5 \right)$ allows to have $D i s t P _ { t } ( \cdot ) \in [ 0 , 1 ] .$ . The larger t leads to a larger complexity burden. As shown in the example 2, such distance is not recommended when t N1.

Example 2. Let's consider the frame $\Theta = \{ \theta _ { 1 } , ~ \theta _ { 2 } , ~ . . . , ~ \theta _ { 2 n } \}$ and the following two independent bba's

$$
\begin{array}{l l} \mathbf {m} _ {1}: & m _ {1} (\theta_ {1}) = m _ {1} (\theta_ {2}) = \dots = m _ {1} (\theta_ {n}) = 1 / n \\ \mathbf {m} _ {2}: & m _ {2} (\theta_ {n + 1}) = m _ {2} (\theta_ {n + 2}) = \dots = m _ {2} (\theta_ {2 n}) = 1 / n \end{array}
$$

In this example m<sub>1</sub> and ${ \bf m } _ { 2 }$ totally contradict. The diiferent distance measures between $\mathbf { m } _ { 1 }$ and $\mathbf { m } _ { 2 }$ are shown in Fig. 1.

The plots for DistP and $d _ { J }$ coincide on this <sup>fi</sup>gure since m and m are Bayesian bba's. The values of $D i s t P _ { 2 } , \ D i s t P _ { 3 }$ and MaxDiff tend towards $^ { 0 , }$ meaning that $\mathbf { m } _ { 1 }$ and m are closer and closer with the increase of n, which is obviously abnormal. Only $D i s t P _ { 1 } = 1$ is constant, and it indicates that $\mathbf { m } _ { 1 }$ and m are completely different. Moreover, the computation burden is lowest when using t= 1, and that is why we choose to take t=1 in this paper. DistP characterizes the dissimilarity by the absolute distance between their associate subjective probabilities.

![](/api/attachments/GPDCEQXF/fulltext/images/c4c1f3e43895df33f58223b685286f2a3d113a303391f318cf2d359f5fc8bdb0.jpg)  
Fig.1. Different distance measures between m and $\mathbf { m } _ { 2 } .$

Lemma 1. Let $\mathbf { m } _ { 1 } , \mathbf { m } _ { 2 }$ be two bba's defined on $2 ^ { \Theta } .$ . The probabilisticbased distance $\begin{array} { r l } { { D i s t P _ { t } } ( \mathbf m _ { 1 } , \mathbf m _ { 2 } ) { \in } [ 0 , 1 ] . } \end{array}$

• If $\mathbf { m } _ { 1 } = \mathbf { m } _ { 2 }$ , then $D i s t P ( \mathbf m _ { 1 } , \mathbf m _ { 2 } ) = 0$ , but its reciprocal is not true.

• If Dist $\mathbf { \Psi } ( \mathbf { m } _ { 1 } , \ \mathbf { m } _ { 2 } ) = 1$ , then m<sub>1</sub> and m<sub>2</sub> totally contradict and therefore there is no compatible elements supported by the both bb $\therefore s ,$ and its reciprocal is true.

In the example 1, one has $D i s t P ( \mathbf { m } _ { 1 } , \mathbf { m } _ { 2 } ) = 0$ and $D i s t P ( { \bf m } _ { 1 } , { \bf m } _ { 3 } ) =$ 1 $) i s t P ( { \bf m } _ { 2 } , { \bf m } _ { 3 } ) = ( n - 1 ) / n ,$ which indicates the distance between m and $\mathbf { m } _ { 2 }$ is much smaller than that of $\mathbf { m } _ { 1 }$ and ${ \bf m } _ { 3 }$

In the dissimilarity measure, the degree of the divergence between the distinct hypotheses strongly supported by each source must play an important role. Unfortunately, DistP is unable to reveal such divergence which makes it not a good candidate for a good dissimilarity measure if we use it as sole criteria.

Lemma 2. Even $i f$ the distance/dissimilarity measure is high, it is possible in some cases that the two bba's strongly support the same hypothesis. Reciprocally, if the distance measure is low, it is possible in some cases that the bba's commit the most of their masses of belief to different incompatible elements of the frame.

## This lemma is illustrated through the next Example 3.

Example 3. Let's consider the frame $\Theta = \{ \theta _ { 1 } , ~ \theta _ { 2 } , ~ \theta _ { 3 } \}$ with Shafer's model and the following three independent bba's

$$
\begin{array}{l l} \mathbf {m} _ {1}: & m _ {1} (\theta_ {1}) = 0. 5, m _ {1} (\theta_ {2}) = 0. 3, m _ {1} (\theta_ {3}) = m _ {1} (\Theta) = 0. 1 \\ \mathbf {m} _ {2}: & m _ {2} (\theta_ {1}) = 0. 8, m _ {2} (\theta_ {3}) = 0. 2 \\ \mathbf {m} _ {3}: & m _ {3} (\theta_ {1}) = 0. 3, m _ {3} (\theta_ {2}) = 0. 5, m _ {3} (\Theta) = 0. 2 \end{array}
$$

The various distances between these bba's are:

$$
\begin{array}{c c} d _ {J} (\mathbf {m} _ {1}, \mathbf {m} _ {2}) = 0. 3 1 0 9, & d _ {J} (\mathbf {m} _ {1}, \mathbf {m} _ {3}) = 0. 2 1 6 0 \\ M a x D i f f (\mathbf {m} _ {1}, \mathbf {m} _ {2}) = 0. 2 6 6 7, & M a x D i f f (\mathbf {m} _ {1}, \mathbf {m} _ {3}) = 0. 2 3 3 3 \\ D i s t P (\mathbf {m} _ {1}, \mathbf {m} _ {2}) = 0. 3 3 3 3, & D i s t P (\mathbf {m} _ {1}, \mathbf {m} _ {3}) = 0. 2 3 3 3. \end{array}
$$

Although m and m strongly support the same hypothesis $\theta _ { 1 } ,$ whereas ${ \bf m } _ { 3 }$ strongly supports $\theta _ { 2 } ,$ the dissimilarity between $\mathbf { m } _ { 1 }$ and m is larger than that between m and ${ \bf m } _ { 3 }$ according to the distance measures. We see that the divergence between the hypotheses strongly supported by each source is not taken into account ef<sup>fi</sup>ciently with DistP and other distance measures. Thissimple example shows that such distance measures are not good enough to properly characterize the dissimilarity between bba's. Therefore, we propose to use another criterion to re<sup>fl</sup>ect more ef<sup>fi</sup>ciently the degree of divergence/con<sup>fl</sup>ict among the belief functions. This new criterion will be a complementary criterion of the probabilistic-based distance measure $D i s t P ( . , . )$ and help to de<sup>fi</sup>ne a new re<sup>fi</sup>ned and ef<sup>fi</sup>cient dissimilarity measure.

## 3. Intrinsic con<sup>fl</sup>ict of belief functions

As in [11], a qualitative de<sup>fi</sup>nition of con<sup>fl</sup>ict between two beliefs in the context of DST is given.

De<sup>fi</sup>nition 1. A con<sup>fl</sup>ict between two beliefs can be interpreted qualitatively as the fact that one source strongly supports one hypothesis and the other strongly supports another hypothesis, and the two hypotheses are not compatible (their intersection is empty).

This de<sup>fi</sup>nition is intuitively consistent, and it will be adopted here. According this de<sup>fi</sup>nition, the con<sup>fl</sup>ict mainly comes from pairs of incompatible hypotheses which are separately strongly supported by two different sources of evidence. So the extent of con<sup>fl</sup>ict should be re<sup>fl</sup>ected by the con<sup>fl</sup>icting belief of the pair of incompatible hypotheses strongly supported by their sources. Let m<sub>1</sub>(.) and $m _ { 2 } ( . )$ be two independent bba's over Θ. Their degree of con<sup>fl</sup>ict, as de<sup>fi</sup>ned by Shafer in [17] and interpreted by Smets, is given by

$$
m_{12}(\emptyset)\triangleq \sum_{\substack{X_{1},X_{2}\in 2^{\Theta}\\ X_{1}\cap X_{2} = \emptyset}}m_{1}(X_{1})m_{2}(X_{2})\tag{6}
$$

$m _ { \oplus } ( \emptyset ) \equiv m _ { 1 2 } ( \emptyset )$ is generally used to evaluate the level of con<sup>fl</sup>ict [20] between the two sources of evidence. Nevertheless, $m _ { \oplus } ( \emptyset )$ is the sum of all the masses of belief committed to the empty set through the conjunctive rule of combination. However, such measure is not very appropriate to really characterize the con<sup>fl</sup>ict between bba's, particularly in case of two equal bba's as already reported in several published works [13,11].

Actually, one needs to pay more attention to the hypothesis which gets the most credibility in the bba's. If two sources of evidence commit the most plausibility to compatible or same elements, we argue that they are consistent in the element they strongly support, and they do not contradict with each other. Otherwise, they are considered in con<sup>fl</sup>ict. In order to overcome the limitation of $m _ { \oplus } ( \emptyset )$ as the traditional measure of the con<sup>fl</sup>ict, a new measure of level of con<sup>fl</sup>ict, called conflict coefficient is proposed using probabilistic-based transformations and based on the de<sup>fi</sup>nition 1.

De<sup>fi</sup>nition 2 (con<sup>fl</sup>ict coef<sup>fi</sup>cient). Let m and m be two bba's on $2 ^ { \Theta } .$ Their associated subjective probabilities are $P _ { \mathbf { m } _ { \mathrm { i } } } ( . ) , ~ i { = } 1 , ~ 2 ;$ . The Con<sup>fl</sup>ict coef<sup>fi</sup>cient denoted by ConfP is de<sup>fi</sup>ned by

$$
C o n f P (\mathbf {m} _ {1}, \mathbf {m} _ {2}) = \left\{ \begin{array}{l} 0, i f X _ {m a x} ^ {m _ {1}} \cap X _ {m a x} ^ {m _ {2}} \neq \emptyset \\ P _ {m _ {l}} (X _ {m a x} ^ {m _ {l}}) P _ {m _ {2}} (X _ {m a x} ^ {m _ {2}}), o t h e r w i s e. \end{array} \right.\tag{7}
$$

$$
\text { where } X _ {m a x} ^ {\mathbf {m} _ {i}} = \underset {x \in 2 ^ {\Theta}} {\operatorname{argmax}} P _ {m _ {i}} (x), i = 1, 2
$$

The con<sup>fl</sup>ict coef<sup>fi</sup>cient is de<sup>fi</sup>ned in using the maximal approximate subjective probability of the bba's. If two sources of evidence distribute most of their mass of belief to compatible elements, there is no con<sup>fl</sup>ict between the two sources in such conditions. Otherwise, the amount of con<sup>fl</sup>ict will be represented by the product of the pair of maximal subjective probability from different sources.

Lemma 3. Let m and m be two independent bba's on $2 ^ { \Theta } .$ m<sup>12</sup> $( \varnothing ) \in ( 0 , 1 )$ , even if $C o n f P ( { \bf m } _ { 1 } , { \bf m } _ { 2 } ) = 0 .$ . Also, $\begin{array} { r } { \mathbf { m } _ { \oplus } ^ { 1 2 } ( \emptyset ) = 1 , \mathrm { i f } C o n f P ( \mathbf { m } _ { 1 } , } \end{array}$ ${ \bf m } _ { 2 } ) = 1$

Proof. The former part of the Lemma 3 occurs in many cases, especially when considering two equal bba's. The later part can be proved easily. If $C o n f P ( \mathbf { m } _ { 1 } , \mathbf { m } _ { 2 } ) { = } 1$ , it means m and m assign the mass to totally different focal elements. Therefore, one gets $m _ { \oplus } ^ { 1 \bar { 2 } } ( \emptyset ) = 1$

This lemma implies that $m _ { \oplus } ( \emptyset )$ is not very ef<sup>fi</sup>cient when the bba's are not in con<sup>fl</sup>ict, and $m _ { \oplus } ( \emptyset )$ is similar to ConfP in case of highly con<sup>fl</sup>icting situations. The con<sup>fl</sup>ict coef<sup>fi</sup>cient re<sup>fl</sup>ects well the divergence of incompatible hypotheses that two sources of evidence commit most of their belief to. However, it ignores the other elements of bba's. This is shown in the next example.

Example 4. Let's consider the frame $\Theta = \{ \theta _ { 1 } , \theta _ { 2 } \}$ with Shafer's model and the following three independent bba's

$$
\begin{array}{r l} \mathbf {m} _ {1}: & m _ {1} (\theta_ {1}) = 1 \\ \mathbf {m} _ {2}: & m _ {2} (\Theta) = 1 \\ \mathbf {m} _ {3}: & m _ {3} (\theta_ {1}) = 0. 9, m _ {3} (\Theta) = 0. 1 \end{array}
$$

$\mathbf { m } _ { 1 }$ and ${ \bf m } _ { 3 }$ are much closer than m and $\mathbf { m } _ { 2 } ,$ , since m and ${ \bf m } _ { 3 }$ distribute most of their mass of belief to the same hypothesis $\theta _ { 1 } ,$ whereas m is fully ignorant $( { \mathrm { i . e . } }$ m is the vacuous belief assign ment). Nevertheless, from the formula (6) and (7), one gets

$$
C o n f P (\mathbf {m} _ {1}, \mathbf {m} _ {2}) = C o n f P (\mathbf {m} _ {1}, \mathbf {m} _ {3}) = 0
$$

$$
m _ {\oplus} ^ {1 2} (\emptyset) = m _ {\oplus} ^ {1 3} (\emptyset) = 0.
$$

So in such case, we cannot make a distinction between m and $\mathbf { m } _ { 2 } ,$ and between $\mathbf { m } _ { 1 }$ and ${ \bf m } _ { 3 }$ at all only from these con<sup>fl</sup>ict measures.

If the proposed probabilistic-based distance is used in this example, one gets

$$
\left\{ \begin{array}{l} D i s t P (\mathbf {m} _ {1}, \mathbf {m} _ {2}) = 0. 5, \\ D i s t P (\mathbf {m} _ {1}, \mathbf {m} _ {3}) = 0. 0 5 \end{array} \right.
$$

Naturally, the dissimilarity between m and m is quite larger than between m and ${ \bf m } _ { 3 }$ according to the probabilistic-based distance measure.

Actually, the probabilistic-based distance DistP and the con<sup>fl</sup>ict coef<sup>fi</sup>cient ConfP are complementary and they separately capture different aspects of the dissimilarity of bba's. If the dissimilarity is only characterized by DistP, it cannot show whether the two sources of evidence con<sup>fl</sup>ict or not in the hypothesis they strongly support. Reciprocally, if ConfP is considered as the unique criterion to measure the dissimilarity, the level of the difference between the two bba's is not taken into account. Taking into account both criteriaDistP and ConfP in the elaboration of a new measure of dissimilarity seems therefore a natural way to improve existing measures of dissimilarity in order to capture two of its main aspects.

## 4. A new dissimilarity measure

In this section, we propose a new dissimilarity mixing both DistP and ConfP to characterize more ef<sup>fi</sup>ciently the dissimilarity between two bba's. The new dissimilarity measure, denoted DismP, will be de<sup>fi</sup>ned by the fusion of DistP and ConfP complementary measures/criteria. The fusion rule f( ) we propose to use to de<sup>fi</sup>ne DismP must satisfy the two following important properties:

(1) Commutativity f(x, $y ) { = } f ( y , x ) ;$

(2) Monotonicity f(x, y)≤ f(x′, y)≤ f(x′, y′)≤ f(1, 1)=1, ifx≤x′, y′≤y′;

Hence, the dissimilarity measure dismP obtained from the fusion DistP and ConfP should be no less than any one of them. Also, DismP cannot be larger than the sum of DistP and ConfP, nor 1, which corresponds to the following inequality constraints: max{x, y}≤ f(x, y)≤ min{1, (x + y)}.

Hamacher T-conorm fusion rule [7], denoted $T ( . ) ,$ , satis<sup>fi</sup>es these constraints and that's why we take $f ( . ) { = } T ( . )$ . Therefore, we <sup>fi</sup>nally de<sup>fi</sup>ne Dism $P ( . , . )$

$$
\begin{array}{c} D i s m P (\mathbf {m} _ {1}, \mathbf {m} _ {2}) \triangleq T (D i s t P (\mathbf {m} _ {1}, \mathbf {m} _ {2}), C o n f P (\mathbf {m} _ {1}, \mathbf {m} _ {2})) \\ = \frac {D i s t P (\mathbf {m} _ {1} , \mathbf {m} _ {2}) + C o n f P (\mathbf {m} _ {1} , \mathbf {m} _ {2})}{1 + D i s t P (\mathbf {m} _ {1} , \mathbf {m} _ {2}) C o n f P (\mathbf {m} _ {1} , \mathbf {m} _ {2})} \end{array}\tag{8}
$$

The dissimilarity measure is useful in many domains [10], for instance for belief functions approximation algorithms [1], for de<sup>fi</sup>ning the agreement between sources of evidence as a basis for discounting factors [6,3], for combination rules parameters estimation [4,23], as well as for selecting an adapted combination rule [12], etc. In this paper, we are interested in using it for the automatic determination of discounting factors of the sources of evidence.

For a comparison between the different dissimilarity measures, we now use an example drawn from [9] to show the behavior of $\dot { \boldsymbol { d } } _ { J } , \boldsymbol { d } _ { B } ,$ Maxdiff, m(t), DistP, ConfP, and DismP.

Example 5. Let Θ be a frame of discernment with element $\theta _ { 1 } , \theta _ { 2 } ,$ , etc. For notation conciseness, we use 1, 2, etc. to denote $\theta _ { 1 } , \theta _ { 2 } ,$ etc., and the notation $m ( \theta _ { i } \cup \theta _ { j } )$ is also replaced by $m ( i , j )$ in the sequel. The two bba's are de<sup>fi</sup>ned as follows:

$$
\begin{array}{l l} \mathbf {m} _ {1}: & m _ {1} (2, 3, 4) = 0. 0 5, m _ {1} (7) = 0. 0 5 \\ & m _ {1} (\Theta) = 0. 1, m _ {1} (A) = 0. 8 \\ \mathbf {m} _ {2}: & m _ {2} (1, 2, 3, 4, 5) = 1 \end{array}
$$

A is the subset of Θ. We consider twenty cases where subset A is progressively augmented by including a new element in it. In other words, for case $i = 1 , 2 , 3 , . . . , 2 0 , A _ { i } = \{ 1 , 2 , \cdots , i \}$

The comparison of the aforementioned dissimilarity measures between m and m for the 20 cases is graphically illustrated in Fig. 2. 2

As we can see, $d _ { J }$ and DistP present a similar behavior in this example, but the computation of DistP is easier. In this example DismP mainly depends on DistP since ConfP is small here, and this explains why plots of DismP and DistP are very close. MaxDiff becomes very small from case 2, and its value even decreases from case 8 to 13, which is abnormal since we expect a growth of the dissimilarity measure. $d _ { B }$ always indicates that $\mathbf { m } _ { 1 }$ and ${ \bf m } _ { 2 }$ are totally different but in case 5, and it cannot distinguish the variation among these cases. In case $5 , A = \{ 1 , 2 , 3 , 4 , 5 \}$ is the same with the only focal element in athbfm , which leads d to decrease substantially in this case. ConfP implies that both bba's commit the most plausibility to the compatible element from the cases 1 to 6, but $\mathbf { m } _ { 1 }$ begins to distribute its most belief to another element which is different from the element strongly supported by ${ \bf m } _ { 2 }$ from case 7. The divergence degree, re<sup>fl</sup>ecting the strong support of sources in different hypotheses, is becoming lower and lower. Indeed, since m becomes more and more uncertain, all singletons get small probability gain through the probabilistic transformation. Nevertheless, the con<sup>fl</sup>icting mass of belief m(t) keeps a low value around 0.05 and is not representative of the divergence between the sources.

## 5. Discounting factors of sources of evidence

In this section, we propose a new method for determining the discounting(weighting) factors of the sources based on the dissimilarity measure. The derivation of the weights of the sources is based on the underlying (and usually well-adopted) principle that the Truth lies in the majority opinion. When one has a set of n sources of evidence to combine, the scalar dissimilarity measure DismP between each pair of sources must be obtained by (8) at <sup>fi</sup>rst, and the mutual support degree among these sources will be given by:

![](/api/attachments/GPDCEQXF/fulltext/images/4b21970ab1fe1ea0f0080caaa9759fd4828c55baf119f26351ef506ae880bff5.jpg)  
Fig.2. Different dissimilarity measures between m and $\mathbf { m } _ { 2 } .$

$$
\sup \left(m _ {i}, m _ {j}\right) = \left(1 - D i s m P \left(m _ {i}, m _ {j}\right) ^ {q}\right) ^ {\frac {1}{q}}\tag{9}
$$

For simplicity, one suggests to take $q = 1 .$ . The mutually support degree n×n matrix is then de<sup>fi</sup>ned by

$$
\mathbf {S} = \left[ \begin{array}{c c c c} 1 & s u p _ {1 2} & ... & s u p _ {1 n} \\ s u p _ {2 1} & 1 & ... & s u p _ {2 n} \\ \vdots & \vdots & \vdots & \vdots \\ s u p _ {n 1} & s u p _ {n 2} & ... & 1 \end{array} \right]\tag{10}
$$

where $s u p _ { i j } { \triangleq } s u p ( m _ { i } , m _ { j } )$

The weight of each source of evidence is denoted by $w _ { i } , i = 1 , 2 , . . . ,$ n. We argue that the weighting factors should be relative, not only with the support degree gained from the other sources, but also with the weights of those other sources. The problem of joint estimation of all weighting factors consists in solving for $i = 1 , 2 , 3 , \cdots , n ,$

$$
\lambda w _ {i} = w _ {1} s u p _ {1 i} + w _ {2} s u p _ {2 i} + \dots + w _ {n} s u p _ {n i}\tag{11}
$$

or more concisely written as

$$
\lambda \mathbf {w} = \mathbf {S w}\tag{12}
$$

where w $\mathsf { \Pi } _ { : } ^ { \ast } [ w _ { 1 } , w _ { 2 } , . . . , w _ { n } ] ^ { \prime }$ and λ is the proportion coef<sup>fi</sup>cient. The Perron–Frobenius vector (the eigen vector associated to the maximal positive eigen value ) of S is used as the credibility factor, that is $\lambda _ { m a x } \cdot \mathbf { w } { = } \pmb { S } \cdot \mathbf { w } .$

The source with the largest weighting factor is considered as totally reliable and important, and there is no need to revise it. The other sources are discounted with the factor as

$$
w _ {i} ^ {\prime} = w _ {i} / m a x (w) <   1\tag{13}
$$

w<sub>i</sub> is called the relative weighting factor of the source i.

In the discounting process, the reliability discounting rule and importance discounting rule must be selected by the system designer according to his/her application. The reliability and importance represent two distinct notions. Reliability represents ability of the source to provide the correct assessment of the given problem, whereas importance means somehow the weight of importance granted to the source.

## • Reliability discounting rule

Two kinds of approaches, including the average bba's method [3,14] and Shafer's discounted bba's method [17], have been proposed for the combination of unreliable sources of evidence. The average bba's method [14] combines iteratively (sequentially) the arithmetic mean of all the bba's. Deng at al. in [3] modi<sup>fi</sup>ed this method to compute the weighted average bba's by taking into account the evidential distance $d _ { J } ,$ but we know that $d _ { J }$ is no good enough in all cases to precisely measure the dissimilarity. Moreover, in the average bba's method, all the independent sources of evidence are represented by the same average of bba's, and the distinctness of the different sources is not taken into account ef<sup>fi</sup>ciently. The combination results are nothing but the iterative combination of the average bba's. So this method is too sensitive to the weighting factors. Since the determination of reliability factors is not robust enough, this can lead to wrong decision. The classical Shafer's discounting method [17] distributes the discounted mass to the ignorance according to the corresponding reliability factor, and all the discounted bba's remain distinct and independent. Shafer's discounting method seems more reasonable, and that's why it is applied here. We recall brie<sup>fl</sup>y how it is applied:

$$
\left\{ \begin{array}{l} m ^ {\prime} (A) = \alpha \cdot m (A), A \neq \Theta \\ m ^ {\prime} (\Theta) = 1 - \sum_ {A \in 2 ^ {\Theta}} m ^ {\prime} (A) \\ A \neq \Theta \end{array} \right.\tag{14}
$$

where α is the reliability (discounting) factor of m( ). The discounted mass is committed to the ignorance $m ^ { \prime } ( \Theta )$

• Importance discounting rule

The recent importance discounting method proposed in [19] is de<sup>fi</sup>ned by:

$$
\left\{ \begin{array}{l} m ^ {\prime} (A) = \beta \cdot m (A), A \neq \emptyset \\ m ^ {\prime} (\emptyset) = 1 - \sum_ {A \in 2 ^ {\ominus}} m ^ {\prime} (A) \\ A \neq \emptyset \end{array} \right.\tag{15}
$$

where $\beta$ is the importance (discounting) factor of $m ( \cdot )$ . This importance discounting rule allows to have $m ( \emptyset ) \geq 0 ,$ , and preserves the speci<sup>fi</sup>city of the primary information since all focal elements are discounted with same importance factor.

If we assume that all the sources of evidence are reliable but they don't share the same importance, the importance discounting rule can be applied. Otherwise, the reliability discounting rule is selected. One can take either $\alpha { = } w _ { i } ^ { \prime }$ for the reliability discounting, or $\beta = w _ { i } ^ { \prime }$ for the importance discounting, depending on the rule we prefer to apply in the given application under consideration. If the importance discounting rule is applied, DS rule de<sup>fi</sup>ned in [17] will be useless since it will not respond to the discounting of sources towards the empty set (see proof in [19]), and $P C R 5 _ { \varnothing }$ can be used as an ef<sup>fi</sup>cient combination rule instead. The fusion result $m _ { P C R 5 _ { \mathrm { 0 } } }$ will be normalized by redistributing the mass of belief committed to the empty set to the other focal elements and proportionally to their masses as it is shown in the examples given in [19]. If the reliability discounting rule is chosen, all the combination rules can be used, since such discounting doesn't commit a strictly positive mass of belief to the empty set.

## 6. Numerical examples

The proposed approach provides a new alternative to combine uncertain sources of evidence with different reliability/importance without a priori knowledge on the sources. It can be well adapted for the fusion of highly con<sup>fl</sup>icting sources of information for decisionmaking support. The sources which are highly con<sup>fl</sup>icting with the majority of other sources will be automatically assigned with a very low reliability/importance factor thanks to the new dissimilarity measure in order to decrease their bad in<sup>fl</sup>uence in the fusion process. Two simple illustrative examples are presented in this section to show the interest of our new approach with respect to other methods.

The context of these examples could correspond to an automatic target identi<sup>fi</sup>cation system using some independent sensors where the signals arising from these sensors are supposed to have been processed into bba's by some given methods. The construction of bba's is application dependent and is out of the scope of this paper. Here, we assume no prior knowledge about reliability, nor importance about the sources of evidence.

Example 6 Bayesian bba's. In this example, we want to show how the proposed method works for the decision making from Bayesian bba's. Let's consider three simple Bayesian bba's over the frame $\Theta =$ $\{ \theta _ { 1 } , \theta _ { 2 } , \theta _ { 3 }$ as in Table 1. It is assumed that sources of evidence No.3 can provide possibly two similar bba's denoted $m _ { 3 A }$ and $m _ { 3 B } ,$ and let's see how the small difference affects the fusion results.

Table 1 Three bba's to be combined.

<table><tr><td></td><td> $\mathbf{m}_{1}$ </td><td> $\mathbf{m}_{2}$ </td><td> $\mathbf{m}_{3A}$ </td><td> $\mathbf{m}_{3B}$ </td></tr><tr><td> $\theta_{1}$ </td><td>0</td><td>0.6</td><td>0.75</td><td>0.7</td></tr><tr><td> $\theta_{2}$ </td><td>0.9</td><td>0.25</td><td>0.15</td><td>0.2</td></tr><tr><td> $\theta_{3}$ </td><td>0.1</td><td>0.15</td><td>0.1</td><td>0.1</td></tr></table>

After the determination of the discounting factors of each source, both the reliability discounting rule and the importance discounting rule will be applied and analyzed separately.

Dempster–Shafer's rule (DS) provides a good compromise between the speci<sup>fi</sup>city of the result and the computation burden but this rule can lead to very counter-intuitive results in case of high con<sup>fl</sup>icting situation. Applying reliability discounting technique (when used judiciously with proper discounting factors) can indeed decrease the degree of con<sup>fl</sup>ict between the bba's by committing the discounted the mass to ignorance. In this example, we compare DS rule with PCR5 rule for combining discounted bba's when reliability discounting is used. We use only $P C R 5 _ { \varnothing }$ fusion rule when the importance discounting is used because DS rule is not responding to such kind of importance discounting. The bba's will be fused sequentially using $P C R 5 _ { \varnothing }$ as explained in details in [19]. The results obtained for this example are shown in the Tables 2 and 3. In the <sup>fi</sup>rst row of the Tables 2 and 3, m<sup>i</sup> corresponds to the (sequential) fusion of sources $\mathbf { m } _ { 1 } , \mathbf { m } _ { 2 } , . . . , \mathbf { m } _ { i } .$ This corresponds to $\mathbf { m } _ { 1 } ^ { \mathbf { i } } = \Delta \mathbf { m } _ { 1 } \oplus \mathbf { m } _ { 2 } \oplus \cdots \oplus \mathbf { m } _ { \mathbf { i } } ,$ $\begin{array} { r } { { \bf m } _ { 1 } ^ { 3 { \tt A } } = \Delta { \bf m } _ { 1 } \oplus { \bf m } _ { 2 } \oplus { \bf m } _ { 3 { \tt A } } , \mathrm { a n d } \ { \bf m } _ { 1 } ^ { 3 { \tt B } } = \Delta { \bf m } _ { 1 } \oplus { \bf m } _ { 2 } \oplus \dot { \bf m } _ { 3 { \tt B } } , } \end{array}$ , where ⊕ denotes either DS, PCR5 or $P C R 5 _ { \varnothing } .$ The <sup>fi</sup>rst column of the Tables 2 and 3 describes the method used for combining the sources of evidence and the underlying measure of dissimilarity used to automatically derive the discounting factors of each source. For example, average bba's & DS″ indicates that the arithmetic mean of all the bba's are iteratively combined by DS rule as in [14]. $" d _ { J }$ & $\mathrm { D } \mathsf { S } ^ { \prime \prime }$ means that the averaged distance $\overline { { d _ { J } } }$ has been used to compute the (reliability) discounting factors and that DS rule has been used to combine discounted sources, and so on.

Analysis of the results. We can see that the bba's ${ \bf m } _ { 2 }$ and $\mathbf { m } _ { 3 A }$ or $\mathbf { m } _ { 3 B }$ commit most belief on $\theta _ { 1 } ,$ , and $\mathbf { m } _ { 3 A }$ is very close to $\mathbf { m } _ { 3 B } ,$ but m , which distributes the largest belief to $\theta _ { 2 } ,$ highly con<sup>fl</sup>icts with $\mathbf { m } _ { 2 }$ and $\mathbf { m } _ { 3 A / B } .$ Thus, m won't be considered so reliable or important as the other ones according to our assumed underlying principle.

For decision-making purpose, the fusion results presented in Tables 2 and 3 show that m<sup>3A</sup> or $\mathbf { m } _ { 1 } ^ { 3 B }$ are very similar except with the average bba's method because both $\mathbf { m } _ { 3 A }$ and $\mathbf { m } _ { 3 B }$ commit the largest mass of belief to $\theta _ { 1 } ,$ , and the difference between the different methods is quite small. However, $\mathbf { m } _ { 1 } ^ { 3 A }$ obtained with the average bba's method consider that $\theta _ { 1 }$ is most likely to be true, whereas $\mathbf { m } _ { 1 } ^ { 3 \bar { B } }$ believes that $\theta _ { 2 }$ should correspond to the truth, and therefore they lead to opposite conclusion for decision-making support. This indicates that the average bba's method is not robust enough and it is very risky for the decision-making support in such cases because all the sources of evidence are considered equally in the average bba's method.

Combination results using reliability discounting rule.

<table><tr><td></td><td> $m_{1}^{3A}(\theta_{1})$ </td><td> $m_{1}^{3B}(\theta_{1})$ </td><td> $m_{1}^{3A}(\theta_{2})$ </td><td> $m_{1}^{3B}(\theta_{2})$ </td><td> $m_{1}^{3A}(\theta_{3})$ </td><td> $m_{1}^{3B}(\theta_{3})$ </td></tr><tr><td>No discount &amp; DS</td><td>0</td><td>0</td><td>0.9574</td><td>0.9677</td><td>0.0426</td><td>0.0323</td></tr><tr><td>No discount &amp; PCR5</td><td>0.5489</td><td>0.5118</td><td>0.4259</td><td>0.4628</td><td>0.0252</td><td>0.0253</td></tr><tr><td>Average bba&#x27;s &amp; DS</td><td>0.5235</td><td>0.4674</td><td>0.4674</td><td>0.5235</td><td>0.0091</td><td>0.0091</td></tr><tr><td> $\overline{d}_{J}$  &amp; DS</td><td>0.6498</td><td>0.6078</td><td>0.3267</td><td>0.3722</td><td>0.0235</td><td>0.0201</td></tr><tr><td> $d_{J}$  &amp; DS</td><td>0.7264</td><td>0.6823</td><td>0.2502</td><td>0.2968</td><td>0.0234</td><td>0.0209</td></tr><tr><td>Dismp &amp; DS</td><td>0.8332</td><td>0.7958</td><td>0.1454</td><td>0.1829</td><td>0.0214</td><td>0.0213</td></tr></table>

The maximum of the belief of the element in the combination results is labeled by bold data in Table 2, and it is similar in the following tables

Combination results using importance discounting rule.

<table><tr><td></td><td> $m_{1}^{3A}(\theta_{1})$ </td><td> $m_{1}^{3B}(\theta_{1})$ </td><td> $m_{1}^{3A}(\theta_{2})$ </td><td> $m_{1}^{3B}(\theta_{2})$ </td><td> $m_{1}^{3A}(\theta_{3})$ </td><td> $m_{1}^{3B}(\theta_{3})$ </td></tr><tr><td> $\overline{d_{j}}$  &amp;  $PCR5_{\emptyset}$ </td><td>0.6233</td><td>0.5936</td><td>0.3486</td><td>0.3780</td><td>0.0280</td><td>0.0284</td></tr><tr><td> $d_{j}$  &amp;  $PCR5_{\emptyset}$ </td><td>0.6730</td><td>0.6392</td><td>0.2979</td><td>0.3316</td><td>0.0291</td><td>0.0292</td></tr><tr><td>Dismp &amp;  $PCR5_{\emptyset}$ </td><td>0.8154</td><td>0.7815</td><td>0.1522</td><td>0.1860</td><td>0.0324</td><td>0.0325</td></tr></table>

Five bba's to be combined.

<table><tr><td></td><td> $m_1$ </td><td> $m_2$ </td><td> $m_3$ </td><td> $m_4$ </td><td> $m_5$ </td></tr><tr><td> $\theta_1$ </td><td>0.8</td><td>0.4</td><td>0</td><td>0.3</td><td>0.45</td></tr><tr><td> $\theta_2$ </td><td>0.1</td><td>0.2</td><td>0.95</td><td>0.2</td><td>0.1</td></tr><tr><td> $\theta_3$ </td><td>0</td><td>0.1</td><td>0.05</td><td>0.25</td><td>0</td></tr><tr><td> $\{ \theta_1, \theta_2 \}$ </td><td>0</td><td>0.3</td><td>0</td><td>0.2</td><td>0</td></tr><tr><td> $\{ \theta_2, \theta_3 \}$ </td><td>0</td><td>0</td><td>0</td><td>0</td><td>0.15</td></tr><tr><td> $\Theta$ </td><td>0.1</td><td>0</td><td>0</td><td>0.05</td><td>0.3</td></tr></table>

The fusion results obtained with the different methods are shown in Tables 5 and 6

DS rule provides the unreasonable result that $\theta _ { 1 }$ is impossible to happen, which is illogical since there are two sources among three that consider $\theta _ { 1 }$ as being most possibly true. Once the discounting approach by ${ \overline { { d _ { J } } } } , d _ { J } ,$ or DismP is applied before the fusion of DS, we get the largest mass of belief to $\theta _ { 1 }$ as expected. The results of PCR5 suggests that $\theta _ { 1 }$ takes the most mass of belief, and the results become more speci<sup>fi</sup>c and more ef<sup>fi</sup>cient for decision-making when the importance discounting method is additionally applied before the fusion of PCR5 as shown in Table 3. Moreover, we can see that if DismP is used as the criterion of dissimilarity coupled with the proposed method of reliability/importance weight determination, it can produce the most speci<sup>fi</sup>c results for decision-making support. This example illustrates that our proposed method can work well with Bayesian bba's even in high con<sup>fl</sup>icting cases.

Example 7. Now let's consider another set of <sup>fi</sup>ve normalized bba's with imprecise focal elements over the frame of discernment $\Theta = \{ \theta _ { 1 }$ $\theta _ { 2 } , \theta _ { 3 } \}$ as given in Table 4. In this example ${ \bf m } _ { 3 }$ is a Bayesian bba, whereas all other bba's are non-Bayesian.

Analysis of the results. From the Table $^ { 4 , }$ one sees that the bba's ${ \bf m } _ { 1 } ,$ $\mathbf { m } _ { 2 } , \mathbf { m } _ { 4 }$ and ${ \bf m } _ { 5 }$ assign most of their belief to $\theta _ { 1 } ,$ , but ${ \bf m } _ { 3 }$ oppositely commits its largest mass of belief to $\theta _ { > } .$ Therefore ${ \bf m } _ { 3 }$ is considered as the least reliable or unimportant source based on the aforementioned underlying principle, and it can be considered as a noisy source (outlier).

From the Tables 5 and 6 and after the combination of all the sources, one sees that the DS rule (without discounting process) concludes that the hypothesis $\theta _ { 1 }$ is very unlikely to happen whereas $\theta _ { 2 }$ is almost sure to happen. Such result is unreasonable since the majority sources assign most of their belief t ${ } _ { ) } \theta _ { 1 } ,$ but only one source distributes its largest mass of belief to $\theta _ { 2 } .$ Such unexpected behavior shows that DS rule is risky to use to combine sources of evidence in a high con<sup>fl</sup>icting situation. The result of PCR5 (with no discounting of bba's) indicates that $\theta _ { 1 }$ has a higher mass of belief than $\theta _ { 2 }$ (as expected) after the sequential fusion of the <sup>fi</sup>ve sources, even if $\theta _ { 2 }$ has got a bigger mass than $\theta _ { 1 }$ after some intermediate steps of the sequential fusion process. This behavior of PCR5 rule may cause troubles for fast decision-making support (in the case we don't want to wait to process all the sources). To avoid such problem due to the non-associativity property of PCR rules, it is better to combine the sources altogether in a unique and global fusion step. Once importance (or reliability) discounting method is applied, thbfm becomes strongly discounted because of its largest dissimilarity with the other sources. One sees that the proposed dissimilarity measure coupled with the automatic discounting factors determination generates a more speci<sup>fi</sup>c result than using the method proposed in [3,13] which was only based on the mean of evidential distance $d _ { J }$ to determine the reliability factor. Therefore, our new approach improves the decision-making support. If d is used instead of titDismP as the bba's distance in our method for automatic discounting factors determination, one still gets better speci<sup>fi</sup>c results than those obtained with the method presented in [3,13]. These results show the effectiveness and the interest of this new method for the estimation of discounting factors of the sources of evidence.

The interest of the new method proposed in this work lies in the elaboration of a more ef<sup>fi</sup>cient dissimilarity measure which can be used for the determination of the discounting factors of the sources involved in the fusion process. The new dissimilarity measure is obtained from the T-conorm fusion of two components: a distance measure and a new measure of the con<sup>fl</sup>ict between two bba's. This new measure is larger than its two components. The sources of evidence in high con<sup>fl</sup>ict with the majority of other sources get a bigger dissimilarity measure than the averaged evidential distance. The discounting (weighting) factors of the sources are computed based on the dissimilarities of the sources taken altogether. The small group of highly con<sup>fl</sup>icting sources always gets small weights, whereas the majority of normal sources (i.e. the sources in agreement) get large weights. The few highly con<sup>fl</sup>icting sources generally get lower weighting factors in our new method of determination of weights than in the arithmetic average method used in [3,13]. Therefore the majority of non (or low) con<sup>fl</sup>icting sources play a more important role in the fusion (as intuitively expected for a rational and good behavior). Such new method can provide interesting results and valuable help for automatic or semi-automatic decision-making support systems. The choice of the two discounting rules (importance versus reliability) is left to the users according to their own purposes.

Combination results using reliability discounting rule.

<table><tr><td></td><td> $m_{1}^{2}$ </td><td> $m_{1}^{3}$ </td><td> $m_{1}^{4}$ </td><td> $m_{1}^{5}$ </td></tr><tr><td rowspan="4">No discount &amp; DS</td><td> $m(\theta_1) = 0.8451$ </td><td></td><td></td><td></td></tr><tr><td> $m(\theta_2) = 0.0986$ </td><td> $m(\theta_2) = 0.9948$ </td><td> $m(\theta_2) = 0.9965$ </td><td> $m(\theta_2) = 0.9971$ </td></tr><tr><td> $m(\theta_3) = 0.0140$ </td><td> $m(\theta_3) = 0.0052$ </td><td> $m(\theta_3) = 0.0035$ </td><td> $m(\theta_3) = 0.0029$ </td></tr><tr><td> $m(\theta_1, \theta_2) = 0.0423$ </td><td></td><td></td><td></td></tr><tr><td rowspan="4">No discount &amp; PCR5</td><td> $m(\theta_1) = 0.8311$ </td><td> $m(\theta_1) = 0.4076$ </td><td> $m(\theta_1) = 0.4037$ </td><td> $m(\theta_1) = 0.5196$ </td></tr><tr><td> $m(\theta_2) = 0.1150$ </td><td> $m(\theta_2) = 0.5850$ </td><td> $m(\theta_2) = 0.5100$ </td><td> $m(\theta_2) = 0.4154$ </td></tr><tr><td> $m(\theta_3) = 0.0239$ </td><td> $m(\theta_3) = 0.0068$ </td><td> $m(\theta_3) = 0.0848$ </td><td> $m(\theta_3) = 0.0482$ </td></tr><tr><td> $m(\theta_1, \theta_2) = 0.03$ </td><td> $m(\theta_1, \theta_2) = 0.0006$ </td><td> $m(\theta_1, \theta_2) = 0.0015$ </td><td> $m(\theta_1, \theta_2) = 0.0004$  $m(\theta_2, \theta_3) = 0.0164$ </td></tr><tr><td rowspan="4"> $\overline{d}_J$  &amp; DS</td><td> $m(\theta_1) = 0.7611$ </td><td> $m(\theta_1) = 0.5705$ </td><td> $m(\theta_1) = 0.6361$ </td><td> $m(\theta_1) = 0.7086$ </td></tr><tr><td> $m(\theta_2) = 0.1177$ </td><td> $m(\theta_2) = 0.3367$ </td><td> $m(\theta_2) = 0.3159$ </td><td> $m(\theta_2) = 0.2662$ </td></tr><tr><td> $m(\theta_3) = 0.0303$ </td><td> $m(\theta_3) = 0.0246$ </td><td> $m(\theta_3) = 0.0144$ </td><td> $m(\theta_3) = 0.0097$ </td></tr><tr><td> $m(\theta_1, \theta_2) = 0.0909$ </td><td> $m(\theta_1, \theta_2) = 0.0682$ </td><td> $m(\theta_1, \theta_2) = 0.0336$ </td><td> $m(\theta_1, \theta_2) = 0.0155$ </td></tr><tr><td rowspan="4"> $d_J$  &amp; DS</td><td> $m(\theta_1) = 0.7659$ </td><td> $m(\theta_1) = 0.6239$ </td><td> $m(\theta_1) = 0.6858$ </td><td> $m(\theta_1) = 0.7528$ </td></tr><tr><td> $m(\theta_2) = 0.1166$ </td><td> $m(\theta_2) = 0.2791$ </td><td> $m(\theta_2) = 0.2645$ </td><td> $m(\theta_2) = 0.2217$ </td></tr><tr><td> $m(\theta_3) = 0.0294$ </td><td> $m(\theta_3) = 0.0252$ </td><td> $m(\theta_3) = 0.0146$ </td><td> $m(\theta_3) = 0.0096$ </td></tr><tr><td> $m(\theta_1, \theta_2) = 0.0881$ </td><td> $m(\theta_1, \theta_2) = 0.0718$ </td><td> $m(\theta_1, \theta_2) = 0.0351$ </td><td> $m(\theta_1, \theta_2) = 0.0159$ </td></tr><tr><td rowspan="5">DismP &amp; DS</td><td> $m(\theta_1) = 0.7503$ </td><td> $m(\theta_1) = 0.7157$ </td><td> $m(\theta_1) = 0.7670$ </td><td> $m(\theta_1) = 0.8254$ </td></tr><tr><td> $m(\theta_2) = 0.1196$ </td><td> $m(\theta_2) = 0.1598$ </td><td> $m(\theta_2) = 0.1655$ </td><td> $m(\theta_2) = 0.1424$ </td></tr><tr><td> $m(\theta_3) = 0.0319$ </td><td> $m(\theta_3) = 0.0308$ </td><td> $m(\theta_3) = 0.0194$ </td><td> $m(\theta_3) = 0.0120$ </td></tr><tr><td> $m(\theta_1, \theta_2) = 0.0957$ </td><td> $m(\theta_1, \theta_2) = 0.0913$ </td><td> $m(\theta_1, \theta_2) = 0.0477$ </td><td> $m(\theta_1, \theta_2) = 0.0198$ </td></tr><tr><td> $m(\Theta) = 0.0025$ </td><td> $m(\Theta) = 0.0024$ </td><td> $m(\Theta) = 0.0004$ </td><td> $m(\theta_2, \theta_3) = 0.0002$  $m(\Theta) = 0.0002$ </td></tr></table>

Table 6  
Combination results using importance discounting rule.

<table><tr><td></td><td> $m_{1}^{2}$ </td><td> $m_{1}^{3}$ </td><td> $m_{1}^{4}$ </td><td> $m_{1}^{5}$ </td></tr><tr><td rowspan="4"> $\overline{d}_{J}$  &amp;  $PCR5_{\phi}$ </td><td> $\mathbf{m}(\theta_1) = 0.7897$ </td><td> $\mathbf{m}(\theta_1) = 0.5848$ </td><td> $\mathbf{m}(\theta_1) = 0.5668$ </td><td> $\mathbf{m}(\theta_1) = 0.6583$ </td></tr><tr><td> $m(\theta_2) = 0.1237$ </td><td> $m(\theta_2) = 0.4046$ </td><td> $m(\theta_2) = 0.3475$ </td><td> $m(\theta_2) = 0.2763$ </td></tr><tr><td> $m(\theta_3) = 0.0292$ </td><td> $m(\theta_3) = 0.0058$ </td><td> $m(\theta_3) = 0.0834$ </td><td> $m(\theta_3) = 0.0480$ </td></tr><tr><td> $m(\theta_1, \theta_2) = 0.0574$ </td><td> $m(\theta_1, \theta_2) = 0.0048$ </td><td> $m(\theta_1, \theta_2) = 0.0023$ </td><td> $m(\theta_1, \theta_2) = 0.0007$  $m(\theta_2, \theta_3) = 0.0167$ </td></tr><tr><td rowspan="4"> $d_{J}$  &amp;  $PCR5_{\phi}$ </td><td> $\mathbf{m}(\theta_1) = 0.7915$ </td><td> $\mathbf{m}(\theta_1) = 0.6342$ </td><td> $\mathbf{m}(\theta_1) = 0.6119$ </td><td> $\mathbf{m}(\theta_1) = 0.6968$ </td></tr><tr><td> $m(\theta_2) = 0.1233$ </td><td> $m(\theta_2) = 0.3556$ </td><td> $m(\theta_2) = 0.3038$ </td><td> $m(\theta_2) = 0.2384$ </td></tr><tr><td> $m(\theta_3) = 0.0290$ </td><td> $m(\theta_3) = 0.0053$ </td><td> $m(\theta_3) = 0.0820$ </td><td> $m(\theta_3) = 0.0470$ </td></tr><tr><td> $m(\theta_1, \theta_2) = 0.0562$ </td><td> $m(\theta_1, \theta_2) = 0.0049$ </td><td> $m(\theta_1, \theta_2) = 0.0023$ </td><td> $m(\theta_1, \theta_2) = 0.0007$  $m(\theta_2, \theta_3) = 0.0171$ </td></tr><tr><td rowspan="5">DismP &amp;  $PCR5_{\phi}$ </td><td> $\mathbf{m}(\theta_1) = 0.7865$ </td><td> $\mathbf{m}(\theta_1) = 0.8389$ </td><td> $\mathbf{m}(\theta_1) = 0.7995$ </td><td> $\mathbf{m}(\theta_1) = 0.8448$ </td></tr><tr><td> $m(\theta_2) = 0.1240$ </td><td> $m(\theta_2) = 0.1498$ </td><td> $m(\theta_2) = 0.1300$ </td><td> $m(\theta_2) = 0.0982$ </td></tr><tr><td> $m(\theta_3) = 0.0293$ </td><td> $m(\theta_3) = 0.0040$ </td><td> $m(\theta_3) = 0.0680$ </td><td> $m(\theta_3) = 0.0374$ </td></tr><tr><td> $m(\theta_1, \theta_2) = 0.0595$ </td><td> $m(\theta_1, \theta_2) = 0.0073$ </td><td> $m(\theta_1, \theta_2) = 0.0025$ </td><td> $m(\theta_1, \theta_2) = 0.0008$  $m(\theta_2, \theta_3) = 0.0188$ </td></tr><tr><td> $m(\Theta) = 0.0006$ </td><td></td><td></td><td></td></tr></table>

## 7. Conclusions

In this paper, a new combination approach of sources of evidence with different discounting (weighting) factors has been proposed based on a new dissimilarity measure between bba's. We have shown through simple examples that the notion of dissimilarity includes at least two aspects represented by the difference between bba's and also by their level of con<sup>fl</sup>ict. After analyzing the limitation of the classical dissimilarity measures, a new dissimilarity measure mixing the probabilistic-based distances with the degree of con<sup>fl</sup>ict was developed. In this paper the BetP transformation was used in the de<sup>fi</sup>nition of the distance between two bba's to measure the difference between two bba's. A new con<sup>fl</sup>ict coef<sup>fi</sup>cient was also introduced to overcome the limitations of the classical degree of con<sup>fl</sup>ict represented traditionally by the mass committed to the empty set through the conjunctive rule. This new con<sup>fl</sup>ict coef<sup>fi</sup>cient allows to measure more ef<sup>fi</sup>ciently the divergence between distinct hypotheses strongly supported by each source of evidence. The distance and con<sup>fl</sup>ict measures characterize two different aspects of the dissimilarity between bba's. A new method for the automatic determination of weighting factors of the sources has been also presented when no prior knowledge is given about the reliability or the importance of the sources. All the weighting factors are computed jointly from a global optimization problem based on the dissimilarities among bba's, and this makes the evaluation of weighting factors more precise and reasonable. The weighting factors can be applied with the reliability discounting method or with the importance discounting method as well. The numerical examples presented in this paper illustrate clearly the potential interest of this new approach for applications dealing with evidential reasoning for decision-making support. The extension of this approach can naturally be done in the DSmT (Dezert–Smarandache Theory) framework as well, and using DSmP transformation instead of classical Pignistic transformation. This is left for future investigations and out of the scope of this paper.

## Acknowledgements

The authors want to thank anonymous reviewers for their remarks which helped us to improve the quality of this paper. This work has been partially supported by the China Natural Science Foundation (No. 61075029) and PhD Thesis Innovation Fund from Northwestern Polytechnical University (No. cx201015).

## References

[1] F. Cuzzolin, A geometric approach to the theory of evidence IEEE transactions on systems, Man, and Cybernetics - Part C : Applications and Reviews 38 (4) (2008) 522-534

[2] A.P. Dempster, A generalization of Bayesian inference, Journal of the Royal Statistical Society, Series B 30 (1968) 205–247.

[3] Y. Deng, W.K. Shi, Z.F. Zhu, Q. Liu, Combining belief functions based on Distance of evidence, Decision Support Systems 38 (3) (2004) 489–493.

[4] T. Denoeux, Conjunctive and disjunctive combination of belief functions induced by nondistinct bodies of evidence, Artificial Intelligence 172 (2008) 234–264

[5] J. Dezert, F. Smarandache, A new probabilistic transformation of belief mass assignment, in Proceedings of Fusion 2008 Conference, Cologne, Germany, July, 2008.

[6] M.C. Florea, E. Bosse, A.L. Jousselme, Metrics, distances and dissimilarity measures within Dempster–Shafer theory to characterize sources' reliability, Proceeding of Cognitive Systems with Interactive Sensors Conference (COGIS '09), 2009.

[7] H. Hamacher, Uber logische Aggregationen nicht-binar explizierter Entscheidungskriterien, Rita G, Fischer Verlag, Frankfurt, Germany, 1978.

[8] J.Y. Jaffray, Linear utility theory for belief functions, Operations Research Letters 8 (1989) 107–112.

[9] A.L. Jousselme, D. Grenier, E. Bossé, A new distance between two bodies of evidence, Information Fusion 2 (1) (2001) 91–101.

[10] A.L. Jousselme, P. Maupin, On some properties of distances in evidence theory, in Proceeding of workshop on the theory of belief functions, Brest, France, April, 2010.

[11] W. Liu, Analyzing the degree of con<sup>fl</sup>ict among belief functions, Arti<sup>fi</sup>cial Intelligence 170 (11) (2006) 909–924.

[12] Z. Liu, Q. Pan, Y. Cheng, J. Dezert, Sequential adaptive combination of unreliable sources of evidence, in Proceeding of workshop on the theory of belief functions, Brest France April.2010

[13] A. Martin, A.L. Jousselme, C. Osswald, Con<sup>fl</sup>ict measure for the discounting operation on belief functions, in Proceeding of Fusion 2008 Conference, Cologne, Germany, July, 2008.

[14] C.K. Murphy, Combining belief functions when evidence con<sup>fl</sup>icts, Decision Support Systems 29 (1) (2000) 1–9.

[15] B. Ristic, P. Smets, The TBM global distance measure for the association of uncertain combat ID declarations, Information Fusion 7 (3) (2006) 276–284.

[16] G. Shafer, J. Pearl (Eds.), Readings in uncertain reasoning, Morgan Kaufmann, 1990.

[17] G. Shafer, A mathematical theory of evidence, Princeton University Press, Princeton, New Jersey, 1976.

[18] E. Smarandache I. Dezert Advances and Applications of DSmT for Information Fusion Vol. 1-3 American Research Press Rehoboth 2004-2009 available at http://fs.gallup.unm.edu//DSmT.htm

[19] F. Smarandache, J. Dezert, J.-M. Tacnet, Fusion of sources of evidence with different importances and reliabilities, in Proceedings of Fusion 2010 Conference, Edinburgh, UK, July, 2010.

[20] P. Smets, Analyzing the combination of con<sup>fl</sup>icting belief functions, Information Fusion 8 (4) (2007) 387–412.

[21] P. Smets, Decision making in the TBM: the necessity of the pignistic transformation, International Joural of Approximate Reasoning 38 (2) (2005) 133–147.

[22] L.A. Zadeh, A simple view of the Dempster–Shafer theory of evidence and its implication for the rule of combination, AI magzine 7 (2) (1986) 85–90.

[23] L.M. Zouhal, T. Denoeux, An evidence-theoretic k-NN rule with parameter optimization, IEEE Transactions on Systems, Man and Cybernetics – Part C 28 (2) (1998) 263–271.

![](/api/attachments/GPDCEQXF/fulltext/images/397db4d5dcedb716c0f419d6b59047513aa1c148d9601a13800540dbd29365e3.jpg)  
Zhun-ga Liu was born in China, 1984. He received the Bachelor and Master degree from Northwestern Polytechnical university in 2007 and 2010. He started the Ph.D course in Northwestern Polytechnical university since Sep 2009, and he has been studying in Telecom Bretagne since Aug. 2010. His research work focus on belief functions theory and its application.

Jean Dezert was born in France, 1962. He received the electrical engineering degree from Ecole Française de Radioélectricité Electronique and Informatique (EFREI), Paris, in 1985, the D.E.A. degree in 1986 from the University Paris VII and his Ph.D from the University Paris XI, Orsay, in 1990. Since 1993, he is senior research scientist in the Information Modeling and Processing Department (DTIM) at ONERA. His current research interest focus on belief functions theory, especially for DSmT which has been developed by him and Prof. Smarandache.

Quan Pan was born in China 1961. He received the Bachelor degree in Huazhong University of Science and Technology, and he received the master and doctor degree in Northwestern Polytechnical University (NWPU) in 1991 and 1997. He has been professor since 1998 in NWPU. His current research interests are information fusion, data analysis and pattern recognition.

Grégoire Mercier was born in France 1971. He received the Engineering Degree from Institut National des Télécommunications (INT), Évry, France, in 1993, and the Ph.D. degree from the University of Rennes, France, in 1999. Since 1999, he has been with Telecom Bretagne, where he is currently Professor in the Image and Information Processing Department. His research interests are image processing and information fusion.
