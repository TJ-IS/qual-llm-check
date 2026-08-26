---
otero_id: 15892
otero_key: "WW4CGKV9"
title: "How to preserve the conflict as an alarm in the combination of belief functions?"
authors: "Eric Lefèvre; Zied Elouedi"
year: "2013"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2013.06.012"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# How to preserve the con<sup>fl</sup>ict as an alarm in the combination of belief functions?

Eric Lefèvre <sup>a,</sup>⁎, Zied Elouedi <sup>b</sup>

<sup>a</sup> Univ. Lille Nord de France, UArtois, EA 3926 LGI2A, France

<sup>b</sup> University of Tunis, Institut Supérieur de Gestion de Tunis, LARODEC, Tunisia

## a r t i c l e i n f o

Article history: Received 14 February 2012 Received in revised form 26 June 2013 Accepted 27 June 2013 Available online xxxx

Keywords: Belief function theory Data fusion Alarm of singular source Con<sup>fl</sup>ict management

## a b s t r a c t

In the belief function framework, a unique function is induced from the use of a combination rule so allowing to synthesize all the knowledge of the initial belief functions. When information sources are reliable and independent, the conjunctive rule of combination, proposed by Smets, may be used. This rule is equivalent to the Dempster rule without the normalization process. The conjunctive combination provides interesting properties, as the commutativity and the associativity. However, it is characterized by having the empty set, called also the con<sup>fl</sup>ict, as an absorbing element. So, when we apply a signi<sup>fi</sup>cant number of conjunctive combinations, the mass assigned to the con<sup>fl</sup>ict tends to 1 which makes impossible returning the distinction between the problem arisen during the fusion and the effect due to the absorption power of the empty set. The objective of this paper is then to de<sup>fi</sup>ne a formalism preserving the initial role of the con<sup>fl</sup>ict as an alarm signal announcing that there is a kind of disagreement between sources. More exactly, that allows to preserve some con<sup>fl</sup>ict, after the fusion by keeping only the part of con<sup>fl</sup>ict re<sup>fl</sup>ecting the opposition between the belief functions. This approach is based on dissimilarity measures and on a normalization process between belief functions. Our proposed formalism is tested and compared with the conjunctive rule of combination on synthetic belief functions.

© 2013 Elsevier B.V. All rights reserved.

## 1. Introduction

Since many years, the belief function theory [8,43] has known an increasing interest from scienti<sup>fi</sup>c community since it allows to deal with imperfect data (imprecise and uncertain) and to combine them using a combination rule. One of the classical combination rules is the conjunctive rule. This latter, introduced by Smets [44,48], is equivalent to the Dempster rule of combination [8,43] without the normalization process. Properties and also hypotheses that sources should satisfy before being combined by this rule are well established.

This rule has an orthogonal behavior which is very precious because it permits a fast and clear convergence towards a solution, but in return, the empty set is an absorbing element. Smets supports that the existence of this mass on the empty set, called also con<sup>fl</sup>ict, can play a role of alarm. So, contrary to Dempster's rule where the con<sup>fl</sup>ict is reallocated proportionally to the other masses of the focal elements, this con<sup>fl</sup>ict must not be redistributed since it may be at the origin of important information concerning the progress of the fusion process and show the disagreement between sources. In fact, if the con<sup>fl</sup>ict is small, it means that the joint bba <sup>fi</sup>ts with the opinions given by the sources to fuse and consequently try to reinforce them, whereas when the con<sup>fl</sup>ict is high, it means that the induced bba is largely in contradiction with the previous opinions. Nevertheless, due to its absorbing conjunctive effect, a series of combinations aims at getting the empty set equal to 1, making impossible the distinction between a real problem between sources to fuse and an effect caused by the absorbing of the empty set.

In addition to the con<sup>fl</sup>ict de<sup>fi</sup>nition of Smets, other works have been dealt with the con<sup>fl</sup>ict de<sup>fi</sup>nition namely Liu [30] proposes a quantitative measure taking into account the mass on the empty set induced from the combination of two or more bbas and the distance between betting commitments of these same bbas after applying the pignistic transformation. However, this mass on the empty set remains not suf<sup>fi</sup>cient to exactly express the con<sup>fl</sup>ict. On the other hand, in [38], Osswald and Martin present another interpretation of the con<sup>fl</sup>ict by de<sup>fi</sup>ning the auto-con<sup>fl</sup>ict as the amount of intrinsic con<sup>fl</sup>ict of a belief function, in other words it is the con<sup>fl</sup>ict generated by such a function relative to one information source.

Besides in [11], Destercke and Burger present some properties that a measure of extrinsic con<sup>fl</sup>ict should satisfy. They de<sup>fi</sup>ned con<sup>fl</sup>ict as the inconsistency arising from a conjunctive combination, and based on properties, they also proposed con<sup>fl</sup>ict measurements making no a priori assumptions regarding the dependence between sources.

Thus, two types of con<sup>fl</sup>ict can be de<sup>fi</sup>ned:

• The con<sup>fl</sup>ict which allows the estimation of the confusion rate of a source and which will be called intrinsic con<sup>fl</sup>ict [5,20,38,42],

• The con<sup>fl</sup>ict which evaluates the discordance between two bodies of evidence and will be labeled extrinsic con<sup>fl</sup>ict [23,39,49].

In this paper, we characterize the opposition between belief functions by means of a measure of dissimilarity. This measure is then used in our proposed approach named Combination With Adapted Con<sup>fl</sup>ict (CWAC) providing an adaptive weighting between Dempster's rule and conjunctive rule, allowing to keep the initial meaning of the con<sup>fl</sup>ict obtained during the combination and so to restore its initial role of alarm. Thus, it permits to the con<sup>fl</sup>ict to take back its initial sense by only mentioning that there is a problem somewhere and reducing its absorbing power. Our proposal is not a con<sup>fl</sup>ict measure but a combination rule preserving the main role of a con<sup>fl</sup>ict as a signal making aware of this opposition between sources. A preliminary work of this approach has been proposed in [29].

This paper is organized as follows. Section 2 presents the basics of the belief function theory. Combination rules, proposed in the belief function framework, are detailed in Section 3. The de<sup>fi</sup>nition and properties of our CWAC rule are exposed in Section 4. Section 5 brings to light our proposed approach by comparing its behavior with that of the conjunctive combination in the case of synthetic data. Section 6 concludes our study and presents some future works.

## 2. Belief function theory: background

The belief function theory is considered as a useful theory for representing and managing uncertain knowledge. In this Section, we shall brie<sup>fl</sup>y recall some basics of this theory. More details can be found in [43,44,48].

## 2.1. Representing information

Let Ω be a <sup>fi</sup>nite non-empty set including all the elementary events related to a given problem. These events are assumed to be exhaustive and mutually exclusive. Such set Ω is named frame of discernment.

The impact of a piece of evidence on the different subsets of the frame of discernment Ω is represented by the so-called basic belief assignment (bba), called initially by Shafer [43] basic probability assignment.

The bba m is a function $m : 2 ^ { \Omega }  [ 0 , 1 ]$ that satis<sup>fi</sup>es:

$$
\sum_ {A \subseteq \Omega} m (A) = 1.\tag{1}
$$

The basic belief mass $m ( A ) ,$ expresses the part of belief exactly committed to the event A of Ω given a piece of evidence. Due to the lack of information, this quantity cannot be apportioned to any strict subset of A.

Shafer [43] has initially proposed a normality condition expressed by:

$$
m (\emptyset) = 0\tag{2}
$$

Such bba is called a normalized basic belief assignment.

Smets [44,45] relaxes this condition by considering $m ( \emptyset )$ as the amount of con<sup>fl</sup>ict between the pieces of evidence or as the part of belief given to the fact that none of the hypotheses in Ω is true. All the subsets A of Ω such that m(A) is strictly positive, are called the focal elements of m.

Associated with m is the belief function, denoted bel, corresponding to a speci<sup>fi</sup>c bba m, assigns to every subset A of Ω the sum of masses of belief committed to every subset of A by m [43]. This belief function, bel, represents the total belief that one commits to A without being also committed to A. The belief function bel : $2 ^ { \Omega }  [ 0 , 1 ]$ is de<sup>fi</sup>ned so that:

$$
b e l (A) = \sum_ {\emptyset \neq B \subseteq A} m (B), \forall A \subseteq \Omega\tag{3}
$$

$$
b e l (\emptyset) = 0.\tag{4}
$$

The plausibility function pl $\colon 2 ^ { \Omega }  [ 0 , 1 ]$ quanti<sup>fi</sup>es the maximum amount of belief that could be given to a subset A of Ω. It is equal to the sum of the masses given to subsets B compatible with A:

$$
p l (A) = \sum_ {A \cap B \neq \emptyset} m (B), \forall A \subseteq \Omega
$$

$$
p l (\emptyset) = 0.\tag{5}
$$

ð<sup>6</sup>Þ

## 2.2. Special belief functions

In this subsection, we propose some belief functions used to express particular situations related generally to uncertainty. A vacuous bba is de<sup>fi</sup>ned as follows [43]:

$$
m (\Omega) = 1 \text { and } m (A) = 0 \quad \forall A \neq \Omega .\tag{7}
$$

Such function quanti<sup>fi</sup>es the state of total ignorance by having only Ω as a focal element.

A categorical bba is a normalized bba de<sup>fi</sup>ned as follows:

$$
m (A) = 1 \quad \forall A \subset \Omega \quad \text { and } \quad m (B) = 0 \quad \forall B \subseteq \Omega , B \neq A.\tag{8}
$$

This function has a unique focal element different from the frame of discernment Ω.

A certain bba is a particular categorical bba such that its focal element is a singleton. A certain bba is de<sup>fi</sup>ned as follows:

$$
m (A) = 1 \text { and } m (B) = 0 \quad \forall B \neq A \text { and } B \subseteq \Omega \text { and } | A | = 1\tag{9}
$$

where A is a singleton event of Ω. This function represents a state of total certainty on the focal element.

A simple support function (ssf) if it has at most one focal element different from the frame of discernment Ω. A simple support function is de<sup>fi</sup>ned as follows [46]:

$$
m (X) = \left\{ \begin{array}{l l} w & \text { if } X = \Omega \\ 1 - w & \text { if } X = A \quad \forall A \subseteq \Omega \\ 0 & \text { otherwise } \end{array} \right.\tag{10}
$$

where A is the focal element and $w \in [ 0 , 1 ]$ . It presents a belief function induced by a piece of evidence supporting A (with $1 - w )$ and leaving the remaining beliefs for Ω. This bba can also be noted $A ^ { w }$

A Bayesian bba is a particular case of belief functions where all the focal elements are singletons. The corresponding bba is de<sup>fi</sup>ned as follows:

$$
m (A) > 0 \text {   only   when   } | A | = 1.\tag{11}
$$

In this case, bel = pl and they are considered as a probability distribution.

A consonant bba is a bba when all its focal elements $( A _ { 1 } , A _ { 2 } , . . . , A _ { n } )$ are nested, that is $A _ { 1 } \subseteq A _ { 2 } \subseteq \ldots \subseteq A _ { n } .$ It is a special case of possibilities.

A dogmatic belief function is de<sup>fi</sup>ned such that $m ( \Omega ) = 0$ . Inversely a non-dogmatic belief function is de<sup>fi</sup>ned such that $m ( \Omega ) > 0 [ 4 6 ]$ .

## 2.3. The discounting operation

Handling evidence given by experts requires to take into account the level of expertise of each information source. Indeed, reliability differs from one expert to another and a discounting method is imperative to update experts' beliefs based on weighting most heavily the opinions of the best experts and conversely for the less reliable ones.

Please cite this article as: E. Lefèvre, Z. Elouedi, How to preserve the con<sup>fl</sup>ict as an alarm in the combination of belief functions?, Decision Support Systems (2013), http://dx.doi.org/10.1016/j.dss.2013.06.012

Let $\alpha \in [ 0 , 1 ]$ , be the discounting rate, and consequently $1 - \alpha$ is regarded as a degree of con<sup>fi</sup>dence on the expert. Updating the expert's opinions leads to:

$$
\left\{ \begin{array}{l} m ^ {\alpha} (A) = (1 - \alpha) m (A), \quad \forall A \subset \Omega , \\ m ^ {\alpha} (\Omega) = (1 - \alpha) m (\Omega) + \alpha \end{array} \right..\tag{12}
$$

The larger α, the closer $m ^ { \alpha }$ is from the vacuous belief function. ${ \mathsf { S } } 0 ,$ when $\alpha = 1$ , it means that the expert is not reliable at all, and his opinions should be totally ignored. On the other hand, when $\alpha = 0$ it means that the expert is totally reliable.

## 2.4. Pignistic transformation

To make a decision, Smets proposes to transform beliefs to a probability measure, denoted BetP [48]. The link between these two measures is achieved by the pignistic transformation such that:

$$
B e t P (A) = \sum_ {B \subseteq \Omega} \frac {| A \cap B |}{| B |} \frac {m (B)}{1 - m (\varnothing)}, \forall A \in \Omega\tag{13}
$$

BetP can be extended as a function on $2 ^ { \Omega }$ as:

$$
\operatorname{Bet} P (A) = \sum_ {\omega \in A} \operatorname{Bet} P (\omega) \quad \forall A \subseteq \Omega \text { and } \omega \in \Omega .\tag{14}
$$

## 2.5. Distance between bbas

Several researchers have proposed distances under a belief function framework. Some of them are based on the pignistic transformation [1,16,49,55], where an unavoidable step is the pignistic transformation of the bbas. On the other hand, some distances based directly on bbas, are also proposed [17,23] de<sup>fi</sup>ned on the power set of the frame of discernment.

In this paper, we will focus on the Jousselme distance [23] considered as one of the most known distances.

Let m and m two bbas, the Jousselme distance [23] is de<sup>fi</sup>ned as follows:

$$
d _ {J} (m _ {1}, m _ {2}) = \sqrt {\frac {1}{2} (m _ {1} - m _ {2}) ^ {t} \mathcal {D} (m _ {1} - m _ {2})}\tag{15}
$$

where is the Jaccard index de<sup>fi</sup>ned by:

$$
\mathcal {D} (A, B) = \left\{ \begin{array}{c c} 0 & \text { if } \quad A = B = \varnothing \\ \frac {| A \cap B |}{| A \cup B |} & \forall A, B \in 2 ^ {\Omega}. \end{array} \right.\tag{16}
$$

## 3. Combination of pieces of evidence

In the case of imperfect data (uncertain, imprecise and incomplete), data fusion becomes an interesting solution allowing to obtain more relevant information. The belief function theory offers appropriate tools for ensuring fusion. The objective of the combination is then to synthesize the information issued of a set of belief functions in a unique function. Based on the fusion of bbas induced from several sources, the con<sup>fl</sup>ict between these sources may be arisen. The con<sup>fl</sup>ict is de<sup>fi</sup>ned as a measure of a disagreement between the sources. In the belief function framework, several combination approaches were developed. They can be classi<sup>fi</sup>ed in two categories according whether sources are reliable or not.

## 3.1. Reliable sources

When information sources, inducing belief functions, are considered as reliable, the used operators are based on the conjunctive combination. Hence, the induced result of the conjunctive combinations of two bbas $m _ { 1 }$ and $m _ { 2 } ,$ is noted $m _ { \textcircled { \scriptsize { \infty } } }$ and is de<sup>fi</sup>ned by [48]:

$$
m _ {\text { \circledcirc }} (A) = \sum_ {B \cap C = A} m _ {1} (B) m _ {2} (C) \quad \forall A, B, C \subseteq \Omega .\tag{17}
$$

This rule considers $m _ { \odot } ( \emptyset )$ as the discord between sources implied in the fusion process and called it con<sup>fl</sup>ict.

Another kind of conjunctive combination is Dempster's rule [8], based on the orthogonal sum, and is considered as the standard fusion rule used in the case of reliable sources. The induced bba is noted $m _ { \oplus }$ and is de<sup>fi</sup>ned by:

$$
m _ {\oplus} (A) = \frac {1}{1 - m _ {\textcircled {O}} (\emptyset)} m _ {\textcircled {O}} (A) \quad \forall A \neq \emptyset \qquad a n d \qquad m _ {\oplus} (\emptyset) = 0\tag{18}
$$

where $\frac { 1 } { 1 - m \textcircled { \cap } ( \emptyset ) }$ is the normalization factor making $m _ { \oplus } ( \emptyset ) = 0$

These two combination rules namely the conjunctive and the Dempster rules are commutative and associative but not idempotent. Therefore, they cannot be used when the sources are not independent.<sup>1</sup>

In addition, Denœux [10] has developed the cautious conjunctive rule having also a conjunctival behavior. This rule is idempotent, and can consequently be applied when information sources are dependent. It is de<sup>fi</sup>ned by the following relation:

$$
m _ {1} \textcircled {\wedge} m _ {2} = \bigcap_ {A \subset \Omega} A ^ {\omega_ {1} (A) \wedge \omega_ {2} (A)}\tag{19}
$$

where $\wedge$ is the minimum operator and $\omega _ { i }$ is the weights obtained from the decomposition based on the conjunctive combination of m in simple support functions such as:

$$
m _ {i} = \bigcap_ {A \subset \Omega} A ^ {\omega_ {i} (A)}.\tag{20}
$$

It is useful to note that these various combinations can also be applied even in the case of unreliable information sources. In such a case, a discounting is then necessary to be applied before the combination. This approach was used in several works [36,50]. The dif<sup>fi</sup>culty remains then in the assessment of the degrees of reliability. There are several strategies to estimate this reliability. One of them is based on the calculation of a measure of dissimilarity between the belief functions to be combined. This measure is used as a degree of discounting. Hence, contradictory belief functions are discounted before fusion phase. This approach was studied by several authors [26,31–33,41,53]. Another technique consists in using further information on the belief functions to de<sup>fi</sup>ne the discounting degree coef<sup>fi</sup>cients [15,16].

## 3.2. Unreliable sources

If one source in the fusion process is not reliable and there is no possible adjustment then combinations based exclusively on the conjunctive rule cannot be used. As a <sup>fi</sup>rst rule dealing with such a case, is the disjunctive rule of combination proposed by Dubois and Prade [12]. Then, in the case of two bbas $m _ { 1 }$ and $m _ { 2 } ,$ this rule is de<sup>fi</sup>ned by:

$$
m _ {\textcircled {U}} (A) = \sum_ {B \cup C = A} m _ {1} (B) m _ {2} (C) \quad \forall A, B, C \subseteq \Omega .\tag{21}
$$

E. Lefèvre, Z. Elouedi / Decision Support Systems xxx (2013) xxx–xxx

This kind combination is the dual of the conjunctive combination. It is discussed within the Generalized Bayes Theorem by Smets [45]. As the conjunctive one, this rule is also associative and commutative but not idempotent. In the case where sources are dependent, Denœux [10] suggests using the bold disjunctive rule. For combining two bbas $m _ { 1 }$ and $m _ { 2 }$ , this rule is de<sup>fi</sup>ned in the following way:

$$
m _ {1} \textcircled {\vee} m _ {2} = \bigcup_ {A \neq \emptyset} A _ {\nu_ {1} (A) \wedge \nu_ {2} (A)}\tag{22}
$$

where $\nu _ { 1 }$ and $\nu _ { 2 }$ represent the disjunctive decomposition<sup>2</sup> of m and m based on simple generalized masses such that:

$$
m _ {i} = \bigcup_ {A \neq \emptyset} A _ {\nu_ {i} (A)}.\tag{23}
$$

Besides, rules having intermediate behavior between the conjunctive and disjunctive rules of combination were developed these last years [7,13,14,19]. Among these rules, we mention the one introduced by Florea [19] which allows to de<sup>fi</sup>ne a family of rules having an intermediate behavior between conjunctive and disjunctive operators according to two functions $\gamma _ { 1 }$ and $\gamma _ { 2 }$ dependent on the con<sup>fl</sup>ict $m _ { \odot } ( \emptyset )$ . This rule is de<sup>fi</sup>ned in the following way:

$$
m _ {F} (A) = \gamma_ {1} (m _ {\textcircled {0}} (\emptyset)) m _ {\textcircled {0}} (A) + \gamma_ {2} (m _ {\textcircled {0}} (\emptyset)) m _ {\textcircled {0}} (A) \quad \forall A \neq \emptyset\tag{24}
$$

Several de<sup>fi</sup>nitions for the functions $\gamma _ { 1 }$ and $\gamma _ { 2 }$ were proposed. However, the authors recommend the use of logarithmic forms which better correspond to the non-symmetric distribution of the con<sup>fl</sup>ict. This rule is called robust rule of combination. For other combination rules, it is a question to redistribute the partial con<sup>fl</sup>ict [4,18,35,52]. Finally, we can also note the other rules, less used, which allow too to combine bbas [21,22,37,51,54]. The objective of all these rules is to redistribute the con<sup>fl</sup>ict induced during the combination.

## 3.3. Discussion

Some tricky situations may often happen, when it is necessary to combine a set of sources where some of them are contradictory. The term of singular sources can be de<sup>fi</sup>ned for sources that supply different information of what the other sources propose [27]. So, being singular or not depends on the fact to be in agreement with the majority. This discord with the majority can result [28,47]:

• That the source at the origin of the discord is not reliable. For example, a failing sensor or working outside his range of functioning can disagree with the other information sources. In that case, the information induced from this source is not relevant.

• Or what this source possesses as information not perceived by the others. For example in the case of the detection of target, several sensors cannot see a target hidden by an obstacle while a source positioned in a different way sees perfectly this target. This source is then very instructive.

So, for a given application, the selection of a combination operator, among those proposed, is relatively sensitive to handle. In fact, in most of the situations, it is impossible to know if some sources are (or will become) reliable or not reliable. The use of a strategy of combination of reliable sources (for example conjunctive rule) containing one or several non-informative singular sources is so going to end in a process of less robust fusion. In the same manner, the use of a combination of unreliable sources with informative singular sources means, generally, redistributing some con<sup>fl</sup>ict. Redistribution which may be likened to a loss of information.

To identify the situation and thus select the appropriate combination, recent works [6,27,30,33,40,41] introduced measures of con<sup>fl</sup>ict, other than the value of m(∅), allowing to quantify the opposition between belief functions. However, these measures are decoupled by the combination belief functions. So, these solutions produce a set of measures. Each of these measures re<sup>fl</sup>ecting the opposition between a source and the other sources involved in the process of fusion. This set of measures remains still dif<sup>fi</sup>cult to interpret and thus the identi<sup>fi</sup>- cation of the situation (reliable or unreliable sources) is tricky. In the following section, a formalism, which allows to protect the part of opposition between belief functions during the combination, is presented. This formalism supplies an alarm to the decision maker, concerning his process of fusion, allowing him to choose adequate measures as for example to strengthen the weight of the singular source if it is informative or to treat it as an erroneous source in the opposite case. This approach allows to obtain the result of the combination and a measure of the quality of the fusion process.

## 4. Combination With Adapted Con<sup>fl</sup>ict (CWAC)

In this paper, belief functions are considered as outcomes of independent information sources. In this frame, the con<sup>fl</sup>ict m(∅) obtained during the combination of belief functions allows to draw the attention on a possible problem like bad modeling, to an unreliable source now and more generally the presence of a singular source. Most of the combinations proposed in the literature (see Section 3) try to redistribute this con<sup>fl</sup>ict and not to use it as indicator. Only the conjunctive combination allows to preserve the mass on the empty set.

However, when the conjunctive combination is applied on a large number of belief functions, the con<sup>fl</sup>ict can take important proportions without re<sup>fl</sup>ecting a real problem. In such a case, this value does not represent a real opposition. This phenomenon is due to the absorbing character of the empty set.

Based on this analysis, we intend to develop a method allowing to transform the mass on the empty set as a real indicator of problems even if the number of sources to be combined is important. Our approach is named Combination With Adapted Con<sup>fl</sup>ict (CWAC).

Considering that there is a problem when sources produce strongly different belief functions, the con<sup>fl</sup>ict must be kept during the fusion. On the contrary, in the case of the combination of information sources for which the distributions of masses are equivalent, the con<sup>fl</sup>ict does not have to exist. The spirit of CWAC is to keep the con<sup>fl</sup>ict exclusively re<sup>fl</sup>ecting the disagreement between sources without taking into account the part that could be called auto-con<sup>fl</sup>ict is de<sup>fi</sup>ned for only one source [34,38]. To de<sup>fi</sup>ne CWAC rule, a measure allowing to determine the resemblance between bbas is necessary.

So, one of the interests of our CWAC rule is to detect the unreliable source(s). In fact, an information source is not usually reliable and its reliability may change from time to time. Two solutions are then possible. The <sup>fi</sup>rst one consists in checking before fusing if each source is reliable or not. It is then necessary to compute the reliability of each source at each time and then fuse them (if sources are identi<sup>fi</sup>ed enough as reliable). The second solution has only one phase, using CWAC for combination, so get at the meantime, the fusion result and the disagreement measure (so potentially the unreliability of a source). According to the value of this measure, the expert may accept or not the results of the fusion. If he does not accept it, he should then look for the unreliable source(s) (like the <sup>fi</sup>rst solution). Hence, our proposed solution needs less time than the <sup>fi</sup>rst one.

So, through CWAC, we can discover this through the mass on the empty set, whereas as mentioned using the conjunctive rule, it is not so obvious due to the absorbing behavior of the empty set and also especially when the number of the sources is important.

## 4.1. With two belief functions

At <sup>fi</sup>rst, only the case of two bbas $m _ { 1 }$ and $m _ { 2 }$ is considered. The dissimilarity notion may be obtained from a measure of distance. This distance may be calculated by the method proposed in Section 2.5 and is noted $d ( m _ { 1 } , m _ { 2 } ) . ^ { 3 }$ The borders of the function d are:

$d ( m _ { 1 } , m _ { 2 } ) = 0 ;$ m and m are similar (and consequently in agreement) and their combination should not generate a con<sup>fl</sup>ict. In this case, the con<sup>fl</sup>ict must be redistributed in the same manner as the combination rule of Dempster.

$d ( m _ { 1 } , \ m _ { 2 } ) = 1 ; \ m _ { 1 }$ and $m _ { 2 }$ are antinomic (i.e. $m _ { 1 } ( \{ \omega _ { j } \} ) = 1$ and $m _ { 2 } ( \{ \omega _ { i } \} ) = 1$ with $\omega _ { i } \neq \omega _ { j } , \omega _ { i } \in \Omega$ and $\omega _ { j } \in \Omega )$ . Their combination produces a con<sup>fl</sup>ictual mass expressing their opposition. This value must be kept in the same way as with the conjunctive combination.

CWAC combination is de<sup>fi</sup>ned by an adaptive weighting between the conjunctive and Dempster's rules. This adaptive weighting allows to obtain a behavior similar to that of the conjunctive rule when belief functions are antinomic and equivalent to that of the Dempster rule when belief functions are similar. Between these two extremes, a gradual passage may be considered. The combination rule which we propose noted can be written then in the following way:

$$
m _ {\textcircled {H}} (A) = \gamma_ {1} m _ {\textcircled {O}} (A) + \gamma_ {2} m _ {\oplus} (A) \quad \forall A \subseteq \Omega\tag{25}
$$

with:

$$
m _ {\oplus} (A) = (m _ {1} \oplus m _ {2}) (A) \quad \forall A \Omega\tag{26}
$$

$$
m _ {\text { \circledcirc }} (A) = (m _ {1} \text { \circledcirc } m _ {2}) (A) \quad \forall A \subseteq \Omega\tag{27}
$$

where $\gamma _ { 1 }$ and $\gamma _ { 2 }$ are dependent functions of distance $d ( m _ { 1 } , m _ { 2 } )$ . These functions should satisfy the following constraints:

$$
\gamma_ {1} = f _ {1} (d (m _ {1}, m _ {2})) \quad \text { with } \quad f _ {1} (0) = 0 \quad \text { and } \quad f _ {1} (1) = 1\tag{28}
$$

$$
\gamma_ {2} = f _ {2} (d (m _ {1}, m _ {2})) \quad \text { with } \quad f _ {2} (0) = 1 \quad \text { and } \quad f _ {2} (1) = 0\tag{29}
$$

with $\gamma _ { 1 } + \gamma _ { 2 } = 1$ . However other functions are possible, we can choose at <sup>fi</sup>rst, linear functions such that:

$$
\gamma_ {1} = d (m _ {1}, m _ {2})\tag{30}
$$

$$
\gamma_ {2} = 1 - d (m _ {1}, m _ {2}).\tag{31}
$$

Hence, our rule can be written ∀ A Ω and $m _ { \odot } ( \emptyset ) \neq 1$

$$
m _ {\textcircled {+}} (A) = m _ {1} \textcircled {\leftrightarrow} m _ {2} (A) = d (m _ {1}, m _ {2}) m _ {\textcircled {n}} (A) + (1 - d (m _ {1}, m _ {2}))   m _ {\oplus} (A).\tag{32}
$$

when $m _ { \odot } ( \emptyset ) = 1$ , then we have $m _ { \bigodot } ( \emptyset ) = 1$

## 4.2. General case

The generalization of this approach arises when more than two bbas are to be merged. Indeed, in a classic way the measures of dissimilarity are de<sup>fi</sup>ned only between two bba functions. Let N bbas noted m , …, $m _ { i } . . . , m _ { N }$ which should be fused. The measure of dissimilarity between these functions, which it is necessary to use in the case of the proposed approach, may be a synthesis of the distances between bbas. The objective of the proposed approach is to offer to the decision maker, after the fusion, a measure of con<sup>fl</sup>ict which allows to distinguish the presence of a singular source among bbas. It seems then natural to make this synthesis by using, for example, the maximal value of the set of distances.<sup>4</sup> In that case, the value of D may be de<sup>fi</sup>ned by:

$$
D = \max _ {i, j} \left[ d (m _ {i}, m _ {j}) \right]\tag{33}
$$

with $i \in [ 1 , N ] \mathrm { a n d } j \in [ 1 , N ] .$ . Our rule can be generalized as the following manner ∀ A Ω and $m _ { \odot } ( \emptyset ) \neq 1 $

$$
m _ {\bigoplus} (A) = \binom{\bigoplus m _ {i}}{i} (A) = D m _ {\textcircled {1}} (A) + (1 - D) m _ {\oplus} (A)\tag{34}
$$

and

$$
m _ {\textcircled {\leftrightarrow}} (\emptyset) = 1 \quad \text { when } \quad m _ {\textcircled {\cap}} (\emptyset) = 1\tag{35}
$$

with:

$$
m _ {\bigodot} (A) = \left(\underset {i} {\bigcap} m _ {i}\right) (A) \quad \text { and } \quad m _ {\oplus} (A) = \left(\underset {i} {\oplus} m _ {i}\right) (A) \quad \forall i \in [ 1, N ].\tag{36}
$$

## 4.3. Properties

Here are some properties characterizing our CWAC rule:

• Commutativity: CWAC is commutative, for all m<sub>1</sub>, m<sub>2</sub>:

$$
m _ {1} \circledast m _ {2} = m _ {2} \circledast m _ {1}.
$$

• Associativity: CWAC is not associative, for all m , m , and m :

$$
m _ {1} \circledast (m _ {2} \circledast m _ {3}) \neq (m _ {1} \circledast m _ {2}) \circledast m _ {3}.
$$

• Neutral element: The neutral element of the CWAC is Ω. Let m be the vacuous bba. So for all m:

$$
m \circledast m _ {0} = m.
$$

• Absorbing element: The absorbing element of the CWAC is ∅. Let m be a bba having ∅ has the unique focal element (m(∅) = 1). So, for all m:

$$
m \circledast m _ {e} = m _ {e}.
$$

• Idempotent: CWAC is not idempotent, for all m:

$$
m \circledast m \neq m.
$$

## 5. Experimental results

In this Section, the proposed combination is compared to the conjunctive combination on synthetic data. The <sup>fi</sup>rst experimentation more emphasizes on the study of the behavior of the different operators in the case of a reduced number of belief functions. Then, the second and the third experimentations allow to study the behavior of the operators according to the number of bbas and to the similarity between them.

## 5.1. Example no. 1

For this <sup>fi</sup>rst experimentation, we consider a frame of discernment $\Omega = \{ \omega _ { 1 } , \omega _ { 2 } , \omega _ { 3 } \}$ . At <sup>fi</sup>rst, we consider 5 bbas de<sup>fi</sup>ned in Table 1. We notice that these bbas are relatively similar. In this Table, we <sup>fi</sup>nd the results of the combination of these 5 sources with the conjunctive operator $( m _ { \odot } ^ { 1 , \dots , 5 } )$ and our CWAC operator $( ^ { J } m _ { \odot } ^ { 1 , \ldots , 5 }$ with Jousselme's distance). The con<sup>fl</sup>ict induced by the conjunctive combination is relatively important which is not the case with our approach (0.9317 against 0.1118 if we use the Jousselme distance).

Now, let us consider the case, where a 6th source is added. This source is singular with regard to 5 <sup>fi</sup>rst ones. Results of the combination of these 6 bbas are also presented in Table 1. These results allow to deduce that there is an important increase of the value of the con<sup>fl</sup>ict in the case of our proposed approach. This value is, according to the used distance, from 5 to 6 times more important than during the <sup>fi</sup>rst combination. On the other hand, in the conjunctive combination case, the increase is only 6.4% (that is only 1.06 more important). So, the detection of the presence of a singular source in the fusion process is more easier with our CWAC operator. These conclusions are consolidated by the experimentations presented in the following sections.

## 5.2. Example no. 2

For this experimentation, we are going to study the evolution of the con<sup>fl</sup>ict, according to the maximal distance, in a set of N belief functions. The focal elements as well as degrees of beliefs are randomly generated according to a normal law. The focal elements are altogether selected in $2 ^ { \Omega }$ with the cardinal of Ω equal to 3. Results presented in Fig. 1 are the average of 100 experiences. In that case, the behavior of our proposal is almost linear according to the maximal distance. This conclusion is usually true for any chosen distance and also for any number of belief functions involved in the fusion process. In case with more than 10 belief functions and when the maximum distance is greater than 0.5, the conjunctive combination produces already a con<sup>fl</sup>ictual mass close to 1, this is not the case for our proposal. In this situation, the proposed approach yet allows us to distinguish the opposition between the belief functions.

We can also note that when the maximal distance is low, the con<sup>fl</sup>ict is almost null. On the contrary, and in the same case, the use of the conjunctive combination induces a signi<sup>fi</sup>cant con<sup>fl</sup>ict (superior or equal to 0.5 according to the number of the belief functions combined) while bbas are similar. Furthermore, the convergence towards a maximal value of con<sup>fl</sup>ict is fast as the number of bbas is important.

While both approaches have the same behavior, the dynamics obtained by CWAC function is more important. Indeed, the combination CWAC, the con<sup>fl</sup>icting mass ranges from 0 (no con<sup>fl</sup>ict) to 0.8 (con<sup>fl</sup>ict situation). In this case, the dynamics is then 0.8. With the conjunctive combination in the best case, this value is only 0.5. With a variation range greater, it is more easily to de<sup>fi</sup>ne the threshold at which the system can be questioned (unreliable source or singular source). Finally, for a given combination rule, the results vary according to the number of sources (N = 10, 20 or 30). However, these variations are more important in the case of conjunctive combination and remain very limited with CWAC.

Behavior of the different combinations.

<table><tr><td>bba</td><td> $\emptyset$ </td><td> $\{ {\omega }_{1}\}$ </td><td> $\{ {\omega }_{2}\}$ </td><td> $\{ {\omega }_{1},{\omega }_{2}\}$ </td><td> $\{ {\omega }_{3}\}$ </td><td> $\{ {\omega }_{1},{\omega }_{3}\}$ </td><td> $\{ {\omega }_{2},{\omega }_{3}\}$ </td><td> $\Omega$ </td></tr><tr><td> ${m}_{1}$ </td><td>0</td><td>0.55</td><td>0</td><td>0</td><td>0.40</td><td>0</td><td>0.05</td><td>0</td></tr><tr><td> ${m}_{2}$ </td><td>0</td><td>0.50</td><td>0</td><td>0</td><td>0.30</td><td>0</td><td>0.2</td><td>0</td></tr><tr><td> ${m}_{3}$ </td><td>0</td><td>0.60</td><td>0</td><td>0</td><td>0.25</td><td>0.</td><td>0.15</td><td>0</td></tr><tr><td> ${m}_{4}$ </td><td>0</td><td>0.52</td><td>0</td><td>0</td><td>0.25</td><td>0</td><td>0.23</td><td>0</td></tr><tr><td> ${m}_{5}$ </td><td>0</td><td>0.59</td><td>0</td><td>0</td><td>0.22</td><td>0</td><td>0.19</td><td>0</td></tr><tr><td> ${m}_{1}^{1,\ldots ,5}$ </td><td>0.9317</td><td>0.0506</td><td>0</td><td>0</td><td>0.0176</td><td>0</td><td>0.0001</td><td>0</td></tr><tr><td> $J{m}_{1}^{1,\ldots ,5}$ </td><td>0.1118</td><td>0.6580</td><td>0</td><td>0</td><td>0.2294</td><td>0</td><td>0.0009</td><td>0</td></tr><tr><td> ${m}_{6}$ </td><td>0</td><td>0</td><td>0.5</td><td>0</td><td>0.30</td><td>0</td><td>0.2</td><td>0</td></tr><tr><td> ${m}_{1}^{1,\ldots ,6}$ </td><td>0.9911</td><td>0.0001</td><td>0</td><td>0</td><td>0.0088</td><td>0</td><td>0</td><td>0</td></tr><tr><td> $J{m}_{1}^{1,\ldots ,6}$ </td><td>0.5628</td><td>0.0016</td><td>0</td><td>0</td><td>0.4349</td><td>0</td><td>0.0006</td><td>0</td></tr></table>

![](/api/attachments/WW4CGKV9/fulltext/images/81a23a3a1a1bc8303825a277cc968494788726edd0f83cb2236770acb8b5acc8.jpg)  
Fig. 1. Behavior of con<sup>fl</sup>ict when the distance between bbas varies.

## 5.3. Example no. 3

In this experimentation, two sets of belief functions $S _ { 1 }$ and $S _ { 2 }$ are considered. Within every set, bbas are identical. On the other hand, between both sets, bbas are randomly generated so as to obtain maximal distances according to 3 categories:

• D′ category: where the maximal distance between bbas of the two sets is included in [0; 0.3]

• D″ category: where the maximal distance between bbas of the two sets is included in ]0.3; 0.6]

• D‴ category: where the maximal distance between bbas of the two sets is included in ]0.6; 0.9]

![](/api/attachments/WW4CGKV9/fulltext/images/88527b87ce070f190762677652ef74dc88e0a61c6e35a0b8bdb2cbb19ae5ce1e.jpg)  
Fig. 2. Behavior of con<sup>fl</sup>ict when the proportion of con<sup>fl</sup>ictual bbas varies. The CWAC operator is obtained with Jousselme's distance.

Please cite this article as: E. Lefèvre, Z. Elouedi, How to preserve the con<sup>fl</sup>ict as an alarm in the combination of belief functions?, Decision Support Systems (2013), http://dx.doi.org/10.1016/j.dss.2013.06.012

The generation of bbas is realized in the following way. We generate randomly, according to a normal law, the focal elements of the bba belonging to the set $S _ { 1 } .$ . Then, we generate, according to a normal law, the degree of belief to be assigned to each of these focal elements. The same process will be repeated for bbas belonging to the set $S _ { 2 }$ by verifying the constraint imposed on the maximal distance. Once these bbas were obtained, we duplicate them in each of the sets according to the wished proportion. For that purpose, we note r the proportion of the set $S _ { 1 }$ which expresses itself in the following way:

$$
r = \frac {| S _ {1} |}{N}\tag{37}
$$

where $N = \left| S _ { 1 } \right| + \left| S _ { 2 } \right| \mathrm { a n d } \left| . \right|$ represent the cardinal of the considered set. In this example, we consider N = 20 and $| \Omega | = 3$ . This experiment is 100 times realized and then the results are averaged and represented in Fig. 2 with Jousselme's distance.

On these <sup>fi</sup>gures, when the proportion is equal to 0 or to 1, the involved bbas in the fusion process belong all to the same set. In that case, the conjunctive combination gives nevertheless an important con<sup>fl</sup>icting mass.<sup>5</sup>

The evolution of r only modi<sup>fi</sup>es very slightly this value especially in the case of a low distance. In the case of our CWAC operator, when all the bbas arise from the same set $( r = 0 \mathrm { o r } r = 1 )$ ), the con<sup>fl</sup>icting mass is null.

As soon as a singular source is involved in the fusion process, our rule allows to reach a maximal value which will remain unchanged. This maximum stays in reasonable proportions when the maximal distance is included between [0; 0.3], that is when bbas of both sets are considered as relatively similar. This remark is not veri<sup>fi</sup>ed in case of the conjunctive combination.

## 6. Conclusion

In this paper, we have proposed an approach with adapted con<sup>fl</sup>ict preserving the initial role of the con<sup>fl</sup>ict which is an alarm signal for the combination of belief functions. CWAC presents an adaptive weighting between Dempster's and conjunctive rules based on Jousselme et al.'s distance. Experimentations have shown that through CWAC, the absorbing power of the con<sup>fl</sup>ict is reduced compared with the conjunctive rule of combination. As future works, we intend to deal with the interpretation of the con<sup>fl</sup>ict when sources are dependent. Besides, the dual of CWAC will be proposed in the disjunctive behavior where the frame of discernment Ω is the absorbing element.

## References

[1] M. Bauer, Approximations algorithm and decision making in the Dempster– Shafer theory of evidence — an empirical study, International Journal of Approximate Reasoning 17 (2–3) (1997) 217–237.

[2] F. Cuzzolin, Two new Bayesian approximation of belief functions based on convex geometry, IEEE Transactions on Systems, Man, and Cybernetics, Part B 37 (4) (2007) 993–1008.

[3] F. Cuzzolin, Geometric conditioning of belief functions, Proceedings of 1st Workshop on the Theory of Belief Functions, 2010.

[4] M. Daniel, Associativity in combination of belief functions; a derivation of minC combination, Soft computing A Fusion of foundation, Methodologies and Application 7 (5) (2003).288-296

[5] M. Daniel, Con<sup>fl</sup>icts within and between belief functions, Proceedings of 13th International Conference on Information Processing and Management of Uncer tainty (IPMU'10), Springer-Verlag, 2010, pp. 696–705.

[6] M. Daniel, Non-con<sup>fl</sup>icting and con<sup>fl</sup>icting parts of belief functions, Proceedings of 7th International Symposium on Imprecise Probability: Theories and Applications (ISIPTA'11), 2011, pp. 149–158.

[7] F. Delmotte, L. Dubois, A.M. Desodt, P. Borne, Using trust in uncertainty theories, Information and Systems Engineering 1 (1995) 303–314.

[8] A.P. Dempster, Upper and lower probabilities induced by a multivalued mapping Annals of Mathematical Statistics 38 (1967) 325–339

[9] T. Denoeux, The cautious rule of combination for belief functions and some extensions, Proceedings of International Conference on, Information Fusion (FUSION'06), 2006.

[10] T. Denoeux, Conjunctive and disjunctive combination of belief functions induced by non distinct bodies of evidence, Arti<sup>fi</sup>cial Intelligence 172 (23) (2008) 234–264.

[11] S. Destercke, T. Burger, Toward an axiomatic de<sup>fi</sup>nition of con<sup>fl</sup>ict between belief functions, IEEE Transactions on Systems, Man, and Cybernetics. Part B 13 (2) (2013) 585–596.

[12] D. Dubois, H. Prade, A set theoretic view of belief functions: logical operation and approximations by sets, International Journal of General Systems 12 (3) (1986) 193–226.

[13] D. Dubois, H. Prade, Representation and combination of uncertainty with belief functions and possibility measures, Computational Intelligence 4 (1988) 244–264.

[14] D. Dubois, H. Prade, Reliability data collection and analysis, Chapter On the Combination of Evidence in Various Mathematical Frameworks, J. Flamm and T. Luisi, Brussels 1992, 213–241.

[15] E. Elouedi, E. Lefevre, D. Mercier, Discountings of a belief function using a confusion matrix, 22th IEEE International Conference on Tools with Arti<sup>fi</sup>cial Intelligence (ICTAI'2010), vol. 1, 2010, pp. 287–294.

[16] Z. Elouedi, K. Mellouli, P. Smets, Assessing sensor reliability for multisensor data fusion with the transferable belief model, IEEE Transactions on Systems, Man, and Cybernetics. Part B 34 (2004) 782–787.

[17] D. Fixsen, R.P.S. Mahler, The modi<sup>fi</sup>ed Dempster–Shafer approach to classi<sup>fi</sup>cation, IEEE Transactions on Systems, Man, and Cybernetics. Part A 27 (1997) 96–104.

[18] M.C. Florea, J. Dezert, P. Valin, F. Smarandache, A.-L. Jousselme, Adaptative combination rule and proportional con<sup>fl</sup>ict redistribution rule for information fusion, Proceedings of Cognitive Systems with Interactive Sensors (COGIS'06), 2006

[19] M.C. Florea, A.-L. Jousselme, E. Boisé, D. Grenier, Robust combination rules for evidence theory, Information Fusion 10 (2) (2009) 183–197.

[20] T. George, N.R. Pal, Quanti<sup>fi</sup>cation of con<sup>fl</sup>ict in Dempster–Shafer framework: a new approach, International Journal of General Systems 24 (4) (1996) 407–423.

[21] A. Josang, The consensus operator for combining beliefs, Arti<sup>fi</sup>cial Intelligence 141 (1–2) (2002) 157–170.

[22] A. Josang, J. Diaz, M. Rifqi, Cumulative and averaging fusion of beliefs, Information Fusion 11 (2) (2010) 192–200.

[23] A.-L. Jousselme, D. Grenier, E. Boissé, A new distance between two bodies of evidence, Information Fusion 2 (2001) 91–101.

[24] A.-L. Jousselme, P. Maupin, On some properties of distance in evidence theory, Proceedings of 1st Workshop on the Theory of Belief Functions, 2010.

[25] A.-L. Jousselme, P. Maupin, Distances in evidence theory: comprehensive survey and generalizations, International Journal of Approximate Reasoning 53 (2) (2012) 118–145.

[26] J. Klein, O. Colot, Automatic discounting rate computation using a dissent criterion, Proceedings of 1st Workshop on the Theory of the Belief Functions. 2010

[27] J. Klein, O. Colot, Singular sources mining using evidential con<sup>fl</sup>ict analysis, International Journal of Approximate Reasoning 52 (9) (2011) 1433–1451.

[28] E. Lefevre, O. Colot, P. Vannoorenberghe, Belief function combination and con<sup>fl</sup>ict management, Information Fusion 3 (2002) 149–162

[29] E. Lefevre, Z. Elouedi, D. Mercier, Towards an alarm for opposition con<sup>fl</sup>ict in a conjunctive combination of belief functions, 11th European Conference on Symbolic and Quantitative Approaches to Reasoning with Uncertainty (ECSQARU'11), Springer-Verlag, 2011, pp. 314–325.

[30] W. Liu, Analyzing the degree of con<sup>fl</sup>ict among belief functions, Arti<sup>fi</sup>cial Intelligence 170 (11) (2006) 909–924.

[31] Z.G. Liu, J. Dezert, Q. Pan, G. Mercier, Combination of sources of evidence with different discounting factors based on a new dissimilarity measure, Decision Support Systems 52 (1) (2011) 133–141.

[32] Z.G. Liu, Q. Pan, Y.-M. Cheng, J. Dezert, Proceedings of 1st Workshop on the Theory of Belief Functions, 2010.

[33] A. Martin, A.L. Jousselme, C. Osswald, Con<sup>fl</sup>ict measure for the discounting operation on belief functions, Proceedings of International Conference on, Information Fusion (FUSION'08), 2008, pp. 1003–1010

[34] A. Martin, C. Osswald, Human experts fusion for image classi<sup>fi</sup>cation, Information Security: An International Journal, Special issue on fusing uncertain, imprecise and paradoxist information (DSmT) 20 (2006) 122–143

[35] A. Martin, C. Osswald, Toward a combination rule to deal with partial con<sup>fl</sup>ict and speci<sup>fi</sup>city in belief functions theory, Proceedings of International Conference On, Information Fusion (Fusion'07), 2007.

[36] D. Mercier, G. Cron, T. Denoeux, M.-H. Masson, Decision fusion for postal address recognition using belief functions, Expert Systems with Applications 36 (3, part 1) (2009) 5643–5653.

[37] C.K. Murphy, Combining belief functions with evidence con<sup>fl</sup>icts, Decision Support Systems 29 (1) (2000) 1–9.

[38] C. Osswald, A. Martin, Understanding the large family of Dempster–Shafer theory's fusion operators — a decision-based measure, Proceedings of International Conference On Information Fusion (FUSION'06) 2006

[39] B. Ristic, P. Smets, The TBM global distance measure for the association of uncertain combat ID declaration, Information Fusion 7 (2006) 276–284.

[40] J. Schubert, Specifying nonspeci<sup>fi</sup>c evidence, International Journal of Intelligence Systems 11 (2006) 525–563

[41] J. Schubert, Con<sup>fl</sup>ict management in Dempster–Shafer theory using the degree of falsity, International Journal of Approximate Reasoning 52 (3) (2011) 449–460.

[42] J. Schubert, J. Schubert, The internal con<sup>fl</sup>ict of a belief function, 2rd International Conference on Belief Functions, Springer Verlag, 2012, pp. 169–177.

[43] G. Shafer, A Mathematical Theory of Evidence, Princeton University Press, Princeton, NJ, 1976.

[44] P. Smets, The combination of evidence in the transferable belief model, IEEE Transactions on Pattern Analysis and Machine Intelligence 12 (5) (1990) 447–458.

[45] P. Smets, Belief functions: the disjunctive rule of combination and the generalized Bayesian theorem, International Journal of Approximate Reasoning 9 (1993) 1–35.

[46] P. Smets, The canonical decomposition of a weighted belief, Inter. Joint Conf. On Arti<sup>fi</sup>cial Intelligence, Morgan Kaufmann, San Mateo, CA, 1995, pp. 1896–1901.

[47] P. Smets, Analyzing the combination of con<sup>fl</sup>icting belief functions, Information Fusion 8 (4) (2007) 387–412.

[48] P. Smets, R. Kennes, The transferable belief model, Arti<sup>fi</sup>cial Intelligence 66 (1994) 191–234.

[49] B. Tessem, Approximations for ef<sup>fi</sup>cient computation in the theory of evidence, Arti<sup>fi</sup>cial Intelligence 61 (2) (1993) 315–329.

[50] A. Veremme, E. Lefevre, G. Morvan, D. Dupont, D. Jolly, Evidential calibration process of multi-agent based system: an application to forensic entomology, Expert Systems with Applications 39 (3) (2012) 2361–2374.

[51] R. Yager, On the Dempster–Shafer framework and new combination rules, Information Sciences 41 (1987) 93-138

[52] K. Yamada, A new combination of evidence based on compromise, Fuzzy Sets and Systems 159 (13) (2008) 1689–1708.

[53] D. Yong, S. Wenkang, Z. Zhenfu, L. Qi, Combining belief functions based on distance of evidence, Decision Support Systems 38 (3) (2004) 489–493.

[54] L. Zhang, Representation, independence and combination of evidence in the Dempster–Shafer theory, Book Title Advances in the Dempster–Shafer Theory of Evidence, 1994. 51–69.

[55] L.M. Zouhal, T. Denoeux, An evidence-theoretic k-NN rule with parameter optimization, IEEE Transactions on Systems, Man, and Cybernetics. Part C 28 (2) (1998) 263–271.

![](/api/attachments/WW4CGKV9/fulltext/images/5b012acaf842bfda971beb69f5ba59ef6e7cebc67a347fc8d76c9e9877a98514.jpg)

![](/api/attachments/WW4CGKV9/fulltext/images/b2c12139617e50385a074c15b489f7b141327812062361ae175ce7d8531dd16c.jpg)

Eric Lefevre was born in Calais, France, on March the 31th, of 1973. He received his Ph.D. degree in Computer Science in 2002 from the INSA of Rouen. He is currently an Associate Professor at the University of Artois. His main research inter ests, within the LGI2A (Laboratoire de Génie Informatique et d'Automatique de l'Artois) include information fusion and reasoning with uncertainty.

Zied Elouedi is a Professor in Computer Science at the Tunis Higher Institute of Management and a member of the LARODEC Laboratory. He received his PhD in 2002. His research papers have been published in refereed journals such as the International Journal of Approximate Reasoning, Fuzzy Sets and Systems, IEEE Transactions on Systems Man and Cybernetics — Part B, etc. His research topics are related to uncertainty theories, machine learning, data mining, rough sets, intrusion detection, etc.
