---
otero_id: 2944
otero_key: "GVHBNGPB"
title: "Combining partially independent belief functions"
authors: "Mouna Chebbah; Arnaud Martin; Boutheina Ben Yaghlane"
year: "2015"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2015.02.017"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
Mouna Chebbah <sup>a,b</sup>, Arnaud Martin <sup>b</sup>, Boutheina Ben Yaghlane <sup>c</sup>

<sup>a</sup> LARODEC Laboratory, University of Tunis, ISG Tunis, Tunisia

<sup>b</sup> IRISA, University of Rennes 1, Lannion, France

<sup>c</sup> LARODEC Laboratory, University of Carthage, IHEC Carthage, Tunisia

## a r t i c l e i n f o

Article history: Received 28 November 2013 Received in revised form 17 January 2015 Accepted 26 February 2015 Available online 7 March 2015

Keywords: Theory of belief functions Combination rules Clustering Independence Sources' independence Combination rule choice

## a b s t r a c t

The theory of belief functions manages uncertainty and also proposes a set of combination rules to aggregate opinions of several sources. Some combination rules mix evidential information where sources are independent; other rules are suited to combine evidential information held by dependent sources. In this paper we have two main contributions: First we suggest a method to quantify sources' degree of independence that may guide the choice of the more appropriate set of combination rules. Second, we propose a new combination rule that takes consideration of sources' degree of independence. The proposed method is illustrated on generated mass functions.

© 2015 Elsevier B.V. All rights reserved.

## 1. Introduction

Uncertainty theories like the theory of probabilities, the theory of fuzzy sets[1], the theory of possibilities[2] and the theory of belief functions[3,4] model and manage uncertain data. The theory of belief functions can deal with imprecise and/or uncertain data provided by several belief holders and also combine them.

Combining several evidential information held by distinct belief holders aggregates their points of view by stressing common points. In the theory of belief functions, many combination rules are proposed, some of them like [2,5–9] are <sup>fi</sup>tted to the aggregation of evidential information provided by cognitively independent sources whereas the cautious, bold[10] and mean combination rules can be applied when sources are cognitively dependent. The choice of combination rules depends on sources' independence.

Some researches are focused on doxastic independence of variables such as [11,12]; others [4,13] tackled cognitive and evidential independence of variables. This paper is focused on measuring the independence of sources and not that of variables. We suggest a statistical approach to estimate the independence of sources on the bases of all evidential information that they provide. The aim of estimating the independence of sources is to guide the choice of the combination rule to be used when combining their evidential information.

We propose also a new combination rule to aggregate evidential information and take into account the independence degree of their sources. The proposed combination rule is weighted with that degree of independence leading to the conjunctive rule [14] when sources are fully independent and to the cautious rule [10] when they are fully dependent.

In the sequel, we introduce in Section 2 preliminaries of the theory of belief functions. In the Section 3, an evidential clustering algorithm is detailed. This clustering algorithm will be used in the <sup>fi</sup>rst step of the independence measure process. Independence measure is then detailed in Section 4. It is estimated in four steps: In the <sup>fi</sup>rst step the clustering algorithm is applied. Second a mapping between clusters is performed; then independence of clusters and sources is deduced in the last two steps. Independence is learned for only two sources and then generalized for a greater number of sources. A new combination rule is proposed in the Section 5 taking into account the independence degree of sources. The proposed method is tested on random mass functions in Section 6. Finally, conclusions are drawn.

## 2. Theory of belief functions

The theory of belief functions was introduced by Dempster [3] and formalized by Shafer [4] to model imperfect data. The frame of discernment also called universe of discourse, $\Omega = \{ \omega _ { 1 } , \omega _ { 2 } , . . . , \omega _ { N } \}$ , is an exhaustive set of N mutually exclusive hypotheses ω . The power set $2 ^ { \Omega }$ is a set of all subsets of Ω; it is made of hypotheses and unions of hypotheses from. The basic belief assignment (BBA) commonly called mass function is a function de<sup>fi</sup>ned on the power set $2 ^ { \Omega }$ and spans the interval [0,1] such that:

$$
\sum_ {A \subseteq \Omega} m (A) = 1.\tag{1}
$$

A basic belief mass (BBM) also called mass, $m ( A ) ,$ , is a degree of faith on the truth of A. The bbm, m(A), is a degree of belief on A which can be committed to its subsets if further information justi<sup>fi</sup>es it [7].

Subsets A having a strictly positive mass are called focal elements. Union of all focal elements is called core. Shafer [4] assumed a normality condition such that $m ( \emptyset ) = 0$ , thereafter Smets [14] relaxed this condition in order to tolerate $m ( { \emptyset } ) > 0$

The frame of discernment can also be a focal element; its bbm, $m ( \Omega )$ is interpreted as a degree of ignorance. In the case of total ignorance, $m ( \Omega ) = 1$

A simple support function is a mass function with two focal elements including the frame of discernment. A simple support function m is de-<sup>fi</sup>ned as follows:

$$
m (A) = \left\{ \begin{array}{l l} 1 - w & \text { if   } A = B \text {   for   some   } B \subset \Omega \\ w & \text { if   } A = \Omega \\ 0 & \text { otherwise } \end{array} \right.\tag{2}
$$

where A is a focus of that simple support function and $\mathsf { w } \in [ 0 , 1 ]$ is its weight. A simple support function is simply noted as $A ^ { w }$ . A nondogmatic mass function can be obtained by the combination of several simple support functions. Therefore, any nondogmatic mass function can be decomposed into several support functions using the canonical decomposition proposed by Smets [15].

The belief function (bel) is computed from a BBA m. The amount bel(A) is the minimal belief on A justi<sup>fi</sup>ed by available information on $B \left( B \subseteq A \right)$

$$
b e l (A) = \sum_ {B \subseteq A, B \neq} m (B).\tag{3}
$$

The plausibility function (pl) is also derived from a BBA m. The amount $p l ( A )$ is the maximal belief on A justi<sup>fi</sup>ed by information on B which are not contradictory with $\mathsf { 1 } ( A \cap B \neq \emptyset )$ :

$$
p l (A) = \sum_ {A \cap B \neq \emptyset} m (B).\tag{4}
$$

Pignistic transformation computes pignistic probabilities from mass functions in the purpose of making a decision. The pignistic probability of a single hypothesis A is given by:

$$
B e t P (A) = \sum_ {B \subseteq \Omega , B \neq \emptyset} \frac {| B \cap A |}{| B |} \frac {m (B)}{1 - m (\emptyset)}.\tag{5}
$$

Decision is made according to the maximum pignistic probability The single point having the greatest BetP is the most likely hypothesis.

## 2.1. Discounting

Sources of information are not always reliable, they can be unreliable or even a little bit reliable. Taking into account reliability of sources, we adjust their beliefs proportionally to degrees of reliability. Discounting mass functions is a way of taking consideration of sources' reliabilities into their mass functions. If reliability rate α of a source is known or can be quanti<sup>fi</sup>ed; discounting its mass function m is de<sup>fi</sup>ned as follows:

$$
\left\{ \begin{array}{l l} m ^ {\alpha} (A) & = \alpha \times m (A) \\ m ^ {\alpha} (\Omega) & = 1 - \alpha \times (1 - m (\Omega)) \end{array} , \forall A \subset \Omega \right.\tag{6}
$$

This discounting operator can be used not only to take consideration of source's reliability, but also to consider any information which can be integrated into the mass function, $( 1 - \alpha )$ is called discounting rate.

## 2.2. Combination rules

In the theory of belief functions, a great number of combination rules are used to summarize a set of mass functions into only one. Let $s _ { 1 }$ and $s _ { 2 }$ be two distinct and cognitively independent sources providing two different mass functions $m _ { 1 }$ and $m _ { 2 }$ de<sup>fi</sup>ned on the same frame of discernment Ω. Combining these mass functions induces a third one $m _ { 1 2 }$ de<sup>fi</sup>ned on the same frame of discernment Ω.

There is a great number of combination rules [2,5–9], but we enumerate in this section only Dempster, conjunctive, disjunctive, Yager, Dubois and Prade, mean, cautious and bold combination rules. The <sup>fi</sup>rst combination rule was proposed by Dempster in [3] to combine two distinct mass functions $m _ { 1 }$ and $m _ { 2 }$ as follows:

$$
m _ {1 \oplus 2} (A) = (m _ {1} \oplus m _ {2}) (A) = \left\{ \begin{array}{l l} \frac {\sum_ {B \cap C = A} m _ {1} (B) \times m _ {2} (C)}{1 - \sum_ {B \cap C = \varnothing} m _ {1} (B) \times m _ {2} (C)} & \forall A \subseteq \Omega , A \neq \varnothing \\ 0 & i f A = \varnothing \end{array} \right..\tag{7}
$$

The BBM of the empty set is null $( m ( \emptyset ) = 0 )$ . This rule veri<sup>fi</sup>es the normality condition and works under a closed world where Ω is exhaustive.

In order to solve the problem highlighted by Zadeh's counter example [16] where Dempster's rule of combination produced unsatisfactory results, many combination rules appeared. Smets [14] proposed an open world where a positive mass can be allocated to the empty set. Hence the conjunctive rule of combination for two mass functions m and m is de<sup>fi</sup>ned as follows:

$$
m _ {1} \circledast 2 (A) = \left(m _ {1} \circledast m _ {2}\right) (A) = \sum_ {B \cap C = A} m _ {1} (B) \times m _ {2} (C)\tag{8}
$$

Even if Smets [17] interpreted the bbm, $m _ { 1 } m _ { 1 } \bigodot 2 ( \emptyset ) _ { 2 } ( \emptyset )$ , as an amount of con<sup>fl</sup>ict between evidences that induced $m _ { 1 }$ and $m _ { 2 } ;$ that amount is not really a con<sup>fl</sup>ict because it includes a certain degree of auto-con<sup>fl</sup>ict due to the non-idempotence of the conjunctive combination [18].

The conjunctive rule is used only when both sources are reliable. Smets [14] proposed also to use a disjunctive combination when an unknown source is unreliable. The disjunctive rule of combination is de-<sup>fi</sup>ned for two bbas $m _ { 1 }$ and $m _ { 2 }$ as follows:

$$
m _ {1 \textcircled {U} 2} (A) = (m _ {1} \textcircled {U} m _ {2}) (A) = \sum_ {B \cup C = A} m _ {1} (B) \times m _ {2} (C)\tag{9}
$$

Yager in [8] interpreted m(∅) as an amount of ignorance; consequently it is allocated to Ω. Yager's rule of combination is also de<sup>fi</sup>ned to combine two mass functions $m _ { 1 }$ and $m _ { 2 }$ as follows:

$$
\left\{ \begin{array}{l l} m _ {Y} (X) = m _ {1 \textcircled {0} 2} (X) & \forall X \subset \Omega ,   X \neq \emptyset \\ m _ {Y} (\Omega) = m _ {1 \textcircled {0} 2} (\Omega) + m _ {1 \textcircled {0} 2} (\emptyset) \\ m _ {Y} (\emptyset) = 0 \end{array} \right.\tag{10}
$$

Dubois and Prade's solution [2] was to affect the mass resulting from the combination of con<sup>fl</sup>icting focal elements to the union of these subsets:

$$
\left\{ \begin{array}{l l} m _ {D P} (B) = m _ {1 \textcircled {1}} 2 (B) + \sum_ {A \cap X = \emptyset , A \cup X = B} m _ {1} (X) m _ {2} (A) & \forall A \subseteq \Omega , A \neq \emptyset \\ m _ {D P} (\emptyset) = 0 \end{array} \right.\tag{11}
$$

Conjunctive, disjunctive and Dempster's rules are associative and commutative, but Yager and Dubois and Prade's rules are not associative, even if they are commutative. Unfortunately, all combination rules described above are not idempotent because $m m \textcircled {  } m \neq m m \neq$ m and $m m ( \bigcirc ) m \neq m m \neq m .$

Mean combination rule detailed in [6], m , of two mass functions m and m is the average of these ones. Therefore, for each focal element A of M mass functions, the combined one is de<sup>fi</sup>ned as follows:

$$
m _ {M e a n} (A) = \frac {1}{M} \sum_ {i = 1} ^ {M} m _ {i} (A)\tag{12}
$$

Besides idempotence, this combination rule veri<sup>fi</sup>es normality condition $( \mathbf { m } ( \emptyset ) = 0 )$ if combined mass functions are normalized $( \forall i \in M , m _ { i } ( \emptyset ) = 0 )$ . We note also that this combination rule is commutative but not associative.

All combination rules described above work under a strong assumption of cognitive independence since they are used to combine mass functions induced by two distinct sources. This strong assumption is always assumed but never veri<sup>fi</sup>ed. Denoeux [10] proposed a family of conjunctive and disjunctive rules based on triangular norms and conorms. Cautious and bold rules are members of that family and combine mass functions for which independence assumption is not veri<sup>fi</sup>ed. Cautious combination of two mass functions $m _ { 1 }$ and $m _ { 2 }$ issued from probably dependent sources is de<sup>fi</sup>ned as follows:

$$
m _ {1} \textcircled {\wedge} m _ {2} = \textcircled {\cap} _ {A \subset \Omega} A ^ {w _ {1} (A) \wedge w _ {2} (A)}\tag{13}
$$

where $A ^ { w _ { 1 } ( A ) }$ and $A ^ { w _ { 2 } ( A ) }$ are simple support functions focused on A with weights $w _ { 1 }$ and $w _ { 2 }$ issued from the canonical decomposition [15] of m and m respectively, note also that ⋀ is a min operator of simple support functions weights. The bold and cautious combination rules are commutative, associative and idempotent.

To summarize, the choice of the combination rule is based on the dependence of sources. Combination rules like [2,5–8] combine mass functions which sources are independent, whereas cautious, bold and mean rules are the most <sup>fi</sup>tted to combine mass functions issued from dependent sources.

In this paper, we propose a method to quantify sources' degrees of independence that may be used in a new mixed combination rule. In fact, we propose a statistical approach to learn sources' degrees of independence from all provided evidential information. Indeed, two sets of evidential information assessed by two different sources are classi<sup>fi</sup>ed into two sets of clusters. Clusters of both sources are matched and the independence of each couple of matched clusters is quanti<sup>fi</sup>ed in order to estimate sources' degrees of independence. Therefore, a clustering technique is used to gather similar objects into the same cluster in order to study the source's overall behavior. Before introducing our learning method, we detail in the next section the evidential clustering algorithm that will be used in the learning of sources' degrees of independence.

## 3. Evidential clustering

In this paper, we propose a new clustering technique to classify objects; their attributes' values are evidential and classes are unknown.

Proposed clustering algorithm uses a distance on belief functions given by Jousselme et al. [19] such as proposed by Ben Hariz et al. [20].

Ben Hariz et al. [20] detailed a belief K-modes classi<sup>fi</sup>er in which Jousselme distance [19] is adapted to quantify distances between objects and clusters' modes. These are sets of mass functions; each one is the combination of an attribute's values of all objects classi<sup>fi</sup>ed into that cluster. An object is attributed to the cluster having the minimum distance to its mode.

Temporal complexity of clustering algorithm proposed by Ben Hariz et al. [20] is quite high as clusters' modes and distances are computed in each iteration. The combination by the mean rule to compute modes' values leads to mass functions with a high number of focal elements. Hence, the bigger the cluster is, the least signi<sup>fi</sup>cant is the distance.

We propose a clustering technique to classify objects that attributes' values are uncertain. However uncertainty is modeled with the theory of belief functions detailed in Section 2. In the proposed algorithm, we do not use any cluster mode to avoid the growth of the number of focal elements in clusters' modes. Temporal complexity is also signi<sup>fi</sup>- cantly reduced because all distances are computed only once.

In this section, K is the number of clusters $C l _ { k } \left( 1 \le k \le K \right) ;$ n is the number of objects to be classi<sup>fi</sup>ed; $n _ { k }$ is the number of objects classi<sup>fi</sup>ed into cluster $C l _ { k } ; o _ { i }$ are objects to classify $o _ { i } \colon 1 \leq i \leq n ;$ c is the number of evidential attributes aj: $1 \leq j \leq { \mathfrak { c } }$ which domains are $\Omega _ { a _ { j } }$ and <sup>fi</sup>nally $m _ { i j } \mathrm { i }$ is a mass function value of attribute $" j "$ for object “i”. Mass functions $m _ { i j }$ can be certain, probabilistic, possibilistic, evidential and even missing.

To classify objects $o _ { i }$ into K clusters, we use a clustering algorithm with a distance on belief functions given by [19]. The number of clusters K is assumed to be known. The proposed clustering technique is based on a distance which quanti<sup>fi</sup>es how much is far an object $o _ { i }$ from a cluster ${ { C l } _ { k } } .$ This distance is the mean of distances between $o _ { i } ,$ and all objects $o _ { q }$ that are classi<sup>fi</sup>ed into cluster ${ { C l } _ { k } }$ as follows:

$$
D (o _ {i}, C l _ {k}) = \frac {1}{n _ {k}} \sum_ {q = 1} ^ {n _ {k}} d i s t \left(o _ {i}, o _ {q}\right)\tag{14}
$$

and

$$
\operatorname{dist} \left(o _ {i}, o _ {q}\right) = \frac {1}{c} \sum_ {j = 1} ^ {c} d \left(m _ {i j}, m _ {q j}\right)\tag{15}
$$

with:

$$
d \left(m _ {i j}, m _ {q j}\right) = \sqrt {\frac {1}{2} \left(m _ {i j} - m _ {q j}\right) ^ {t} \underline {{\underline {{D}}}}} \left(m _ {i j} - m _ {q j}\right)\tag{16}
$$

such that:

$$
\underline {{\underline {{D}}}} (A, B) = \left\{ \begin{array}{l l} 1 & \text {   if   } A = B = \varnothing \\ \frac {A \cap B}{A \cup B} & \forall A, B \in 2 ^ {\Omega_ {a _ {j}}} \end{array} \right..\tag{17}
$$

Each object is affected to the most similar cluster in an iterative way till reaching an unchanged cluster partition. It is obvious that the number of clusters K must be known. Temporal complexity of the proposed algorithm is signi<sup>fi</sup>cantly optimized as pairwise distances are computed once a time from the beginning. We do not use any cluster mode. Consequently, there will be no problem of increasing number of focal elements because attributes' values are not combined. Indeed, the evidential clustering algorithm provides a cluster partition that minimizes distances between objects into the same cluster and maximizes the distance between objects classi<sup>fi</sup>ed into different clusters. The main asset of the evidential clustering algorithm according to the belief K-modes proposed by Ben Hariz et al. [20] is the optimization of the temporal complexity. In fact, run-time of the evidential clustering algorithm is improved. The optimization of run-time depends on the size of the frame of discernment $| \Omega _ { a _ { j } } |$ , the number of clusters K and number of objects n. For example, Fig. 1 shows a big gain in the run-time of evidential clustering according to the belief K-modes when the number of mass functions varies, $n \in [ 1 0 , 1 0 0 0 ]$ . Temporal complexity of the evidential clustering algorithm is optimized and that optimization is especially noticed when the number of mass functions to classify is high and also when the frame of discernment contains many hypotheses. Thanks to the improvement of the temporal complexity, this clustering algorithm is used in the following sections.

![](/api/attachments/GVHBNGPB/fulltext/images/06779b0e2459b8d875f7c4e2f7c82cd228ec86d838cb306f13d5883fadc3391a.jpg)  
Fig. 1. Run-time optimization of the evidential clustering and the belief K-modes [20] according to n ∈ [10,1000], $| \varOmega _ { a _ { j } }$ = 5and $K = 5$

## 4. Learning sources' independence degree

In this section we extend paper [21] for many sources, and propose a combination rule emphasizing sources' independence degree. In the theory of probabilities, two hypotheses X and Y are assumed to be statistically independent if $P ( X \cap Y ) = P ( X ) \times P ( Y ) \ { \mathrm { o r } } \ P ( X | Y ) = P ( X )$ . In the context of the theory of belief functions, Shafer [4] de<sup>fi</sup>ned cognitive and evidential independence.

De<sup>fi</sup>nition 1. “Two frames of discernment may be called cognitively independent with respect to the evidence if new evidence that bears on only one of them will not change the degree of support for propositions discerned by the other”.<sup>1</sup>

The cognitive independence is a weak independence; two variables are independent with respect to a mass function if new evidence that bears on only one of the two variables does not change propositions discerned by the other one. For two variables X and Y such that $\Omega _ { X }$ and $\Omega _ { Y }$ their domains (frames of discernment) and $\Omega _ { X } \times \Omega _ { Y }$ the product space of domains $\Omega _ { X }$ and $\Omega _ { Y } .$ Variables X and Y are cognitively independent with respect to $m ^ { \Omega \times \Omega \times }$ if:

$$
p l ^ {\Omega_ {X} \times \Omega_ {Y}} (x, y) = p l ^ {\Omega_ {X} \times \Omega_ {Y} \downarrow \Omega_ {X}} (x) \times p l ^ {\Omega_ {X} \times \Omega_ {Y} \downarrow \Omega_ {Y}} (y)\tag{18}
$$

Note that $\Omega _ { X } \times \Omega _ { Y } \downarrow \Omega _ { X }$ is the marginalization of $\Omega _ { X } \times \Omega _ { Y } \mathrm { i n } \Omega _ { X } [ 7 , 2 2 ]$ Shafer [4] de<sup>fi</sup>ned also a strong independence called evidential independence as follows:

De<sup>fi</sup>nition 2. “Two frames of discernment are evidentially independent with respect to a support function if that support function could be obtained by combining evidence that bears on only one of them with evidence that bears on only the other”.

Two variables are evidentially independent if their joint mass function can be obtained by combining marginal mass functions that bears on each one of them. Variables X and Y are evidentially independent with respect to $m ^ { \Omega _ { X } \times \Omega _ { Y } }$ if:

$$
\left\{ \begin{array}{l} p l ^ {\Omega_ {X} \times \Omega_ {Y}} (x, y) = p l ^ {\Omega_ {X} \times \Omega_ {Y} \downarrow \Omega_ {X}} (x) \times p l ^ {\Omega_ {X} \times \Omega_ {Y} \downarrow \Omega_ {Y}} (y) \\ b e l ^ {\Omega_ {X} \times \Omega_ {Y}} (x, y) = b e l ^ {\Omega_ {X} \times \Omega_ {Y} \downarrow \Omega_ {X}} (x) \times b e l ^ {\Omega_ {X} \times \Omega_ {Y} \downarrow \Omega_ {Y}} (y) \end{array} . \right.\tag{19}
$$

Independence can also be de<sup>fi</sup>ned in terms of irrelevance. The knowledge of the value of one variable does not change the belief on the other one. In the theory of belief functions, irrelevance is based on the conditioning. Variables X and Y are irrelevant with respect to m, $I R _ { m } ( { \boldsymbol { X } } , Y )$ if the marginal mass function on X is obtained by conditioning the joint mass function on values y of Y and marginalizing this conditioned joint mass function on X:

$$
m _ {[ y ]} ^ {\Omega_ {X} \times \Omega_ {Y} \downarrow \Omega_ {X}} (x) \propto m ^ {\Omega_ {X} \times \Omega_ {Y} \downarrow \Omega_ {X}} (x).\tag{20}
$$

Note that proportionality ∝ is replaced by equality when m $\boldsymbol { \imath } _ { [ \boldsymbol { y } ] } ^ { \Omega _ { \boldsymbol { x } } \times \Omega _ { Y } \downarrow \Omega _ { \boldsymbol { X } } }$ and $m ^ { \Omega _ { X } \times \Omega _ { Y } \downarrow \Omega _ { X } }$ are normalized.

Doxastic independence is especially proposed in the theory of belief functions by [11,12] and it is de<sup>fi</sup>ned as follows:

De<sup>fi</sup>nition 3. “Two variables are considered as doxastically independent only when they are irrelevant and this irrelevance is preserved under Dempster's rules of combination”.

In other words, two variables X and Y are doxastically independent if they are irrelevant with respect to m $m _ { 0 }$ when they are irrelevant with respect to m and $m _ { 0 } .$ Indeed, if X and Y are irrelevant according to any mass function m and if they are also irrelevant with respect to another mass function $m _ { 0 , }$ they are assumed to be doxastically independent if they are irrelevant with respect to the orthogonal sum of m and $m _ { 0 } .$ Thus, $\mathrm { ~ f ~ } I R _ { m } ( X , Y ) , I R _ { m o } ( X , Y )$ and $I R _ { m \oplus m _ { 0 } } ( X , Y$ are veri<sup>fi</sup>ed then X and Y are doxastically independent.

This paper is not focused on variables' independence [11,12,4] but on sources' independence. Sources' independence is computed according to a set of different belief functions provided by each source separately. Sources are dependent when all their beliefs are correlatedand there is a link between all mass functions they provide. This problem is not tackled till now, since we noticed a lack of references treating this problem. To study sources' independence, a great number of mass functions provided by both sources is needed. This set of mass functions must be de<sup>fi</sup>ned on the same frame of discernment according to the same problems. For example, two distinct doctors provide n diagnoses in the examination of the same n patients. In that case, the frame of discernment contains all diseases and is already the same for both doctors. We de<sup>fi</sup>ne sources' independence as follows:

De<sup>fi</sup>nition 4. Two sources are cognitively independent if they do not communicate and if their evidential corpora are different.

De<sup>fi</sup>nition 5. Evidential corpus is the set of all pieces of evidence held by a source.

Not only communicating sources are considered dependent but also sources having the same background of knowledge since their beliefs are correlated. The aim of estimating sources' independence is either to guide the choice of combination rules when aggregating their beliefs, or to integrate this degree of independence in a new combination rule.

In this paper, mass functions provided by two sources are studied in order to reveal any dependence between them. In the following, we de-<sup>fi</sup>ne an independence measure ${ \mathrm { I } } _ { \mathrm { d } } , { \mathrm { I } } _ { \mathrm { d } } ( s _ { 1 } , s _ { 2 } )$ , as the independence of $s _ { 1 }$ on $s _ { 2 }$ verifying the following axioms:

1. Non-negativity: The independence of a source $s _ { 1 }$ on another source $s _ { 2 } , \operatorname { I _ { d } } ( s _ { 1 } , s _ { 2 } )$ cannot be negative, it is either positive or null.

2. Normalization: The degree of independence $\mathrm { I _ { d } }$ is a degree over [0, 1], it is null when the <sup>fi</sup>rst source is dependent on the second one, equal to 1 when it is completely independent and a degree from [0, 1] otherwise.

3. Non-symmetry: In the case where $s _ { 1 }$ is independent on $s _ { 2 } , s _ { 2 }$ is not necessarily independent on $s _ { 1 }$ . Even if $s _ { 1 }$ and $s _ { 2 }$ are mutually independent, degrees of independence are not necessarily equal.

4. Identity: Any source is completely dependent on itself and $\mathrm { I } _ { \mathrm { d } } ( s _ { 1 } , s _ { 1 } ) = 0$

I $\dot { \cdot } s _ { 1 }$ and $s _ { 2 }$ are independent, there will be no correlation between their mass functions. The main idea of this paper is: First, classify mass functions provided by each source separately. Then, study similarities between cluster partitions to reveal any dependence between sources. By using clustering algorithm, sources overall behavior is studied. The proposed method is in three steps: First, mass functions of each source are classi<sup>fi</sup>ed. Then, similar clusters are matched. Finally, weights of linked clusters and sources' independence are quanti<sup>fi</sup>ed.

## 4.1. Clustering

Clustering algorithm detailed in Section 3 is used to classify two sets of n mass functions respectively provided by sources $s _ { 1 }$ and $s _ { 2 } .$ Clustering algorithm is performed on all mass functions o $\dot { \boldsymbol { s } } _ { 1 }$ independently of the clustering performed on those $\operatorname { o f } s _ { 2 }$ . We remind that all mass functions of both sources are de<sup>fi</sup>ned on the same frame of discernment and so considered as values of only one attribute when classifying their corresponding objects. For the same example of doctors, patients are objects to classify according to an attribute disease. Values of this attribute are mass functions de<sup>fi</sup>ned on the frame of discernment enumerating all possible diseases. Distance (14) can be simpli<sup>fi</sup>ed as follows because we have only one attribute:

$$
D (o _ {i}, C l _ {k}) = \frac {1}{n _ {k}} \sum_ {q = 1} ^ {n _ {k}} d \left(m _ {i}, m _ {q}\right)\tag{21}
$$

In this paper, we <sup>fi</sup>x the number of clusters to the number of hypotheses in the frame of discernment. In a classi<sup>fi</sup>cation point of view, the number of hypotheses is the number of possible classes. For example, the frame of discernment of the attribute disease enumerates all possible diseases. Hence, when a doctor examines a patient, he gives a mass function as a classi<sup>fi</sup>cation of the patient in some possible diseases.

## 4.2. Cluster matching

After the clustering technique, both mass functions provided by $s _ { 1 }$ and $s _ { 2 }$ are distributed separately on K clusters. In this section, we try to <sup>fi</sup>nd a mapping between clusters in order to link those containing the same objects. If clusters are perfectly linked, meaning all objects are classi<sup>fi</sup>ed similarly for both sources, we can conclude that sources are dependent as they are choosing similar focal elements (not contradictory at least) when providing mass functions for the same objects. If clusters are weakly linked, sources choose similar focal elements for different objects and so they are independent. Clusters' independence degree is proportional to the number of objects similarly classi<sup>fi</sup>ed. The more clusters contain the same objects, the more they are dependent as they are correlated.

We note $C l _ { k _ { 1 } } ^ { 1 }$ where $1 \leq k _ { 1 } \leq K$ for clusters of $s _ { 1 }$ and $C l _ { k _ { 2 } } ^ { 2 }$ where $1 \le k _ { 2 } \le K$ for those of $s _ { 2 } .$ The similarity between two clusters $C l _ { k _ { 1 } } ^ { 1 }$ and $C l _ { k _ { 2 } } ^ { 2 }$ is the proportion of objects simultaneously classi<sup>fi</sup>ed into $C l _ { k _ { 1 } } ^ { 1 }$ and $C l _ { k _ { 2 } } ^ { 2 }$ :

$$
\beta_ {k _ {i} k _ {j}} ^ {i} = \beta^ {i} \left(C l _ {k _ {i}} ^ {i}, C l _ {k _ {j}} ^ {j}\right) = \frac {\left| C l _ {k _ {i}} ^ {i} \cap C l _ {k _ {j}} ^ {j} \right|}{\left| C l _ {k _ {i}} ^ {i} \right|}\tag{22}
$$

with $i , j \in \{ 1 , 2 \}$ and $i \neq j , \beta _ { k _ { 1 } k _ { 2 } } ^ { 1 }$ quanti<sup>fi</sup>es a proportion of objects classi<sup>fi</sup>ed simultaneously in clusters $C l _ { k _ { 1 } } ^ { 1 }$ and $C l _ { k _ { 2 } } ^ { 2 }$ with regard to objects in $C l _ { k _ { 1 } } ^ { 1 }$ , and analogically $\beta _ { k _ { 2 } k _ { 1 } } ^ { 2 }$ is a proportion of objects simultaneously in $C l _ { k _ { 1 } } ^ { 1 }$ and $C l _ { k _ { 2 } } ^ { 2 }$ with regard to those in $C l _ { k _ { 2 } } ^ { 2 }$ . Note that $\beta _ { k _ { 1 } k _ { 2 } } ^ { 1 } \neq \beta _ { k _ { 2 } k _ { 1 } } ^ { 2 }$ since the number of objects classi<sup>fi</sup>ed into $C l _ { k _ { 1 } } ^ { 1 }$ and $C l _ { k _ { 2 } } ^ { 2 }$ is different $( | C l _ { k _ { 1 } } ^ { 1 } | \neq | C l _ { k _ { 2 } } ^ { 2 } | )$

We remind that $\beta ^ { 1 }$ are similarities towards $s _ { 1 }$ and $\beta ^ { 2 }$ are those towards $s _ { 2 } .$ It is obvious that $\beta ^ { i } \left( C l _ { k _ { i } } ^ { i } , C l _ { k _ { j } } ^ { j } \right) = 0$ when $C l _ { k _ { i } } ^ { i }$ and $C l _ { k _ { i } } ^ { j }$ do not contain any common object; however they are completely different. $\beta ^ { i } \left( C l _ { k _ { i } } ^ { i } , C l _ { k _ { j } } ^ { j } \right) = 1$ when these clusters are strongly similar so they contain the same objects. $\mathsf { A }$ similarity matrix $M _ { 1 }$ containing similarities of clusters of s according to those of $\cdot _ { s _ { 2 } } ( \beta ^ { 1 } )$ , and $M _ { 2 }$ the similarity matrix between clusters of $s _ { 2 }$ and those of $s _ { 1 } ~ ( \beta ^ { 2 } )$ are de<sup>fi</sup>ned as follows:

$$
M _ {1} = \left( \begin{array}{c c c c} \beta_ {1 1} ^ {1} & \beta_ {1 2} ^ {1} & ... & \beta_ {1 K} ^ {1} \\ ... & ... & ... & ... \\ \beta_ {k 1} ^ {1} & \beta_ {k 2} ^ {1} & ... & \beta_ {k K} ^ {1} \\ ... & ... & ... & ... \\ \beta_ {K 1} ^ {1} & \beta_ {K 2} ^ {1} & ... & \beta_ {K K} ^ {1} \end{array} \right) \quad a n d \quad M _ {2} = \left( \begin{array}{c c c c} \beta_ {1 1} ^ {2} & \beta_ {1 2} ^ {2} & ... & \beta_ {1 K} ^ {2} \\ ... & ... & ... & ... \\ \beta_ {k 1} ^ {2} & \beta_ {k 2} ^ {2} & ... & \beta_ {k K} ^ {2} \\ ... & ... & ... & ... \\ \beta_ {K 1} ^ {2} & \beta_ {K 2} ^ {2} & ... & \beta_ {K K} ^ {2} \end{array} \right)\tag{23}
$$

We note that $M _ { 1 }$ and $M _ { 2 }$ are different since $\beta _ { k _ { 1 } k _ { 2 } } ^ { 1 } \neq \beta _ { k _ { 2 } k _ { 1 } } ^ { 2 }$ . Clusters of $s _ { 1 }$ are matched to those of $s _ { 2 }$ according to the maximum of $\beta ^ { 1 }$ such that each cluster $C l _ { k _ { 1 } } ^ { 1 }$ is linked to only one cluster $C l _ { k _ { 2 } } ^ { 2 }$ and each cluster $C l _ { k _ { 2 } } ^ { 2 }$ has only one cluster $C l _ { k _ { 1 } } ^ { 1 }$ linked to it. The idea is to link iteratively clusters having the maximal $\beta ^ { 1 }$ in $M _ { 1 }$ then eliminate these clusters and the corresponding line and column from the matrix until having a bijective cluster matching. Algorithm 1 details cluster matching process.

We note that different matchings are obtained for $s _ { 1 }$ and $s _ { 2 }$ because $M _ { 1 }$ and $M _ { 2 }$ are different. Even if this algorithm is quite simple, it provides a matching of clusters in order to compare evidential information provided by both sources. The assignment algorithm proposed in [23] for square matrices and that for rectangular matrices [24] can also be used to minimize the dissimilarity between matched clusters. Other methods for cluster matching [25] and [26] can also be used.

## Algorithm 1. Cluster matching

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Require: Similarity matrix M.
1: while M is not empty do
2: Find  $max(M)$  and indexes c and l of clusters having this maximal similarity.
3: Map clusters l and c.
4: Delete line l and column c from M.
5: end while
6: return Cluster matching.
</div>

## 4.3. Clusters' independence

Once cluster matching is obtained, a degree of independence/dependence of matched clusters is quanti<sup>fi</sup>ed in this step. A set of matched clusters is obtained for both sources and a mass function can be used to quantify each couple of clusters independence. Assume that cluster $C l _ { k _ { 1 } } ^ { 1 }$ is matched to $C l _ { k _ { 2 } } ^ { 2 }$ , a mass function $m ^ { \Omega _ { I } 2 }$ de<sup>fi</sup>ned on the frame of discernment Ω<sub>I</sub> = {Dependent Dep, Independent Ind} describes how much this couple of clusters is independent or dependent as follows:

$$
\left\{ \begin{array}{l} m _ {k _ {i} k _ {j}} ^ {\Omega_ {l}, i} (D e p) = \alpha_ {k _ {i}} ^ {i} \beta_ {k _ {i} k _ {j}} ^ {1} \\ m _ {k _ {i} k _ {j}} ^ {\Omega_ {l}, i} (I n d) = \alpha_ {k _ {i}} ^ {i} \Big (1 - \beta_ {k _ {i} k _ {j}} ^ {1} \Big) \\ m _ {k _ {i} k _ {j}} ^ {\Omega_ {l}, i} (D e p \cup I n d) = 1 - \alpha_ {k _ {i}} ^ {i} \end{array} \right.\tag{24}
$$

A mass function quanti<sup>fi</sup>es the degree of independence of each couple of clusters according to each source; $m _ { k _ { i } k _ { j } } ^ { \Omega _ { I } , i }$ is a mass function for the independence of each linked clusters $C l _ { k _ { i } } ^ { i }$ and $C l _ { k _ { i } } ^ { j }$ according to $s _ { i }$ with $i j \in \{ 1 , 2 \}$ and $i \neq j .$ Coef<sup>fi</sup>cient $\alpha _ { k _ { i } } ^ { i }$ is used to take into account the number of mass functions in each cluster $C l _ { k _ { i } }$ of the source i. Reliability factor $\alpha _ { k _ { i } } ^ { i }$ is not the reliability of any source but it can be seen as the reliability of the clusters' independence estimation. Consequently, independence estimation is more reliable when clusters contain enough mass functions. For example, assume two clusters; one containing only one mass function and the second one containing 100 mass functions. It is obvious that the independence estimation of the second cluster is more precise and signi<sup>fi</sup>cant than the independence estimation of the <sup>fi</sup>rst one.

Reliability factors $\alpha _ { k _ { i } } ^ { i }$ are proportional to the number of hypotheses in the frame of discernment |Ω|, and the number of objects classi<sup>fi</sup>ed in $C l _ { k _ { i } } ^ { i }$ as follows:

$$
\alpha_ {k _ {i}} ^ {i} = f \left(| \Omega |, | C l _ {k _ {i}} ^ {i} |\right)\tag{25}
$$

The bigger |Ω| is, the more mass functions are needed to have a reliable clusters' independence estimation. For example, i ${ \mathrm { : } } | \Omega | = 5$ then there are $2 ^ { 5 }$ possible focal elements, also independence estimation of a cluster containing 20 objects cannot be precise. No existing method to de<sup>fi</sup>ne such function f. Hence, we use simple heuristics as follows:

$$
\alpha_ {k _ {i}} ^ {i} = 1 - \frac {1}{| C l _ {k _ {i}} ^ {i} | ^ {\frac {1}{| \Omega |}}}\tag{26}
$$

As shown in Fig. 2, if |Ω| and number of mass functions in a cluster are big enough, cluster independence mass function is almost not discounted. Reliability factor is an increasing function of |Ω| and $| C l _ { k _ { i } } ^ { i } |$ which favors big clusters.<sup>3</sup>

## 4.4. Sources' independence

Obtained mass functions quantify the independence of each couple of matched clusters according to each source. Therefore, K mass functions are obtained for each source such that each mass function quanti<sup>fi</sup>es the independence of each couple of matched clusters. The combination of K mass functions for each source using the mean, de-<sup>fi</sup>ned by Eq. (12), is a mass function $m ^ { \varOmega _ { I } }$ de<sup>fi</sup>ning the whole independence of one source on another one:

$$
m ^ {\Omega_ {l}, s _ {i}} (A) = \frac {1}{K} \sum_ {k _ {i} = 1} ^ {K} m _ {k _ {i} k _ {j}} ^ {\Omega_ {l}, i} (A) \quad \forall A \subseteq 2 ^ {\Omega}\tag{27}
$$

With $k _ { j }$ is the cluster matched to $k _ { i }$ according to $s _ { i \cdot }$ Two different mass functions $m ^ { \Omega _ { I } , S _ { 1 } }$ and $m ^ { \Omega _ { I } , S _ { 2 } }$ 2 are obtained for $s _ { 1 }$ and $s _ { 2 }$ respectively. We note that $m ^ { \Omega _ { I } , S _ { 1 } }$ is the combination of K mass functions representing the independence of matched clusters according to $s _ { 1 }$ de<sup>fi</sup>ned using Eq. (24). Mass functions $m ^ { \Omega _ { I } , S _ { 1 } }$ and $m ^ { \Omega _ { I } , S _ { 2 } }$ are different since cluster matchings are different which veri<sup>fi</sup>es the axiom of non-symmetry. $\beta _ { k _ { 1 } k _ { 2 } } ^ { 1 } , \beta _ { k _ { 2 } k _ { 1 } } ^ { 2 } \in [ 0 , 1 ]$ verify the non-negativity and the normalization axioms. Finally, pignistic probabilities are computed from these mass functions in order to decide about sources' independence $\mathrm { I _ { d } }$ such that:

$$
\left\{ \begin{array}{l} I _ {d} (s _ {1}, s _ {2}) = B e t P (I n d) \\ \overline {{I}} _ {d} (s _ {1}, s _ {2}) = B e t P (D e p) \end{array} \right.\tag{28}
$$

$\mathrm { I f } \ \mathrm { I } _ { \mathrm { d } } ( s _ { 1 } , s _ { 2 } ) > \overline { { \mathrm { I } _ { \mathrm { d } } } } ( s _ { 1 } , s _ { 2 } )$ we claim that sources $s _ { 1 }$ and $s _ { 2 }$ are independent otherwise they are dependent.

## 4.5. General case

The method detailed above estimates the independence of one source on another one. Independence measure is non-symmetric because if a source $s _ { 1 }$ is independent on a source $s _ { 2 }$ then $s _ { 2 }$ is not necessarily independent on $s _ { 1 }$ and even if it is the case, degrees of independence are not necessarily the same.

It is wise to choose the minimum independence from $\mathrm { I } _ { \mathrm { d } } ( s _ { 1 } , s _ { 2 } )$ and $\mathrm { I _ { d } } ( s _ { 2 } , s _ { 1 } )$ as the overall independence. Consequently, if at least one of two sources is dependent on the other, then sources are considered dependent. In other words, two sources are independent only if they are mutually independent. Hence, overall independence that is denoted $I ( s _ { 1 } , s _ { 2 } )$ is given by:

$$
I (s _ {1}, s _ {2}) = \min (\mathrm{I} _ {\mathrm{d}} (s _ {1}, s _ {2}), \mathrm{I} _ {\mathrm{d}} (s _ {2}, s _ {1}))\tag{29}
$$

We note that $I ( s _ { 1 } , s _ { 2 } )$ is non-negative, normalized, symmetric and identical.

We de<sup>fi</sup>ne an independence measure, noted I, generalizing the independence for more than two sources verifying the following axioms:

1. Non-negativity: Many sources' independence $\{ s _ { 1 } , s _ { 2 } , s _ { 3 } , . . . , s _ { n s } \}$ , noted $\operatorname { I _ { d } } ( s _ { 1 } , s _ { 2 } , . . . , s _ { n s } )$ cannot be negative, it is either positive or null.

2. Normalization: Sources' independence I is a degree in [0, 1]. The min imum 0 is reached when sources are completely dependent and the maximum 1 is reached when they are completely independent.

3. Symmetry: $I ( s _ { 1 } , s _ { 2 } , s _ { 3 } , . . . , s _ { n s } )$ is the sources' overall independence and $I ( s _ { 1 } , s _ { 2 } , s _ { 3 } , . . . , s _ { n s } ) = I ( s _ { 2 } , s _ { 1 } , s _ { 3 } , . . . , s _ { n s } ) = I ( s _ { 3 } , s _ { 1 } , s _ { 2 } , . . . , s _ { n s } ) .$

4. Identity: $I ( s _ { 1 } , s _ { 1 } , s _ { 1 } ) = 0 .$ . It is obvious that any source is completely dependent on itself.

![](/api/attachments/GVHBNGPB/fulltext/images/82a448688c254448bee776b3960eb487751aeb5083bfbf041c1a6fc778247e97.jpg)  
Fig. 2. Reliability factors $\alpha _ { k _ { i } } ^ { i }$

5. Increasing with inclusion: $I ( s _ { 1 } , s _ { 2 } ) \ : \le \ : I ( s _ { 1 } , s _ { 2 } , s _ { 3 } )$ , more there are sources, more they are likely to be independent.

To compute the overall independence of ns sources $\{ s _ { 1 } , s _ { 2 } , . . . s _ { n s } \}$ , independencies of pairs of sources are computed and the maximum<sup>4</sup> independence is the sources overall independence:

$$
I (s _ {1}, s _ {2}, \dots , s _ {n s}) = \max \left(I \left(s _ {i}, s _ {j}\right)\right), \quad \forall i \in [ 1, n s ] \quad , j \in ] i, n s ]\tag{30}
$$

or equivalently:

$$
I (s _ {1}, s _ {2}, \dots , s _ {n s}) = \max \left(\min \left(I _ {d} \left(s _ {i}, s _ {j}\right), I _ {d} \left(s _ {j}, s _ {i}\right)\right)\right), \quad \forall i, j \in [ 1, n s ] \quad i \neq j\tag{31}
$$

Independence degree of sources is then integrated in the combination step using the following mixed combination rule.

## 5. Combination rule

Combination rules using conjunctive and/or disjunctive rules such as [2,5–8] are used when sources are completely independent but cautious and bold rules [10l tolerate redundant information and consequently can be used to combine mass functions which sources are dependent. In the combination step, sources dependence or independence hypothesis is intuitively made without any possibility of check. Sources' independence degree is neither 0 nor 1 but a level over [0,1]. The main question is “which combination rule to use when combining partially independent\dependent mass functions?”

In this paper, we propose a new mixed combination rule using conjunctive and cautious rules detailed in Eqs. (8) and (13). In the case of totally dependent sources (where independence is 0), the cautious and proposed mixed combination rules are similar; whereas in the case of totally independent sources (independence is 1), the conjunctive and proposed combination rules are similar. In the case of an independence degree in ]0,1[, combined mass function is the average of conjunctive and cautious combinations weighted by sources' independence degree.

Assume that two sources $s _ { 1 }$ and $s _ { 2 }$ are independent with a degree γ such that $\gamma = I ( s _ { 1 } , s _ { 2 } )$ ; m and $m _ { 2 }$ are mass functions provided by s and $s _ { 2 } .$ The proposed mixed combination rule is de<sup>fi</sup>ned as follows:

$$
m _ {M i x e d} (A) = \gamma * m _ {\textcircled {0}} (A) + (1 - \gamma) * m _ {\textcircled {0}} (A), \quad \forall A \subseteq \Omega\tag{32}
$$

The degree of independence of a set of sources is given by Eq. (30), and the mixed combination of a set of mass functions $\{ m _ { 1 } , m _ { 2 } , . . . m _ { n s } \}$ provided by sources $\{ s _ { 1 } , s _ { 2 } , . . . , s _ { n s } \}$ is also a weighted average such that:

$$
\gamma = I (s _ {1}, s _ {2}, \dots , s _ {n s})\tag{33}
$$

Properties of the proposed mixed combination rule

• Commutativity: Conjunctive and cautious rules are commutative. Independence measure is symmetric because sources' degree of independence is the same for a set of sources. Then the proposed rule is commutative.

• Associativity: Conjunctive and cautious rules are associative but the proposed rule is not because independence degree of n sources and n + 1 ones is not necessarily the same.

• Idempotent: Degree of independence of one source to itself is 0, in that case the proposed rule is equivalent to the cautious rule. As the cautious rule is idempotent, it is the case of the proposed mixed rule.

• Neutral element: Mixed combination rule does not have any neutral element.

• Absorbing element: No absorbing element also.

Combination of two mass functions.

<table><tr><td> $2^{\Omega}$ </td><td> $m_1$ </td><td> $m_2$ </td><td> $m_{\textcircled{A}}$ </td><td> $m_{\textcircled{C}}$ </td><td> $m_{\text{Mixed}}$  $\gamma = 0$ </td><td> $m_{\text{Mixed}}$  $\gamma = 0.3$ </td><td> $m_{\text{Mixed}}$  $\gamma = 0.6$ </td><td> $m_{\text{Mixed}}$  $\gamma = 1$ </td></tr><tr><td> $\emptyset$ </td><td>0</td><td>0</td><td>0.1071</td><td>0.06</td><td>0.1071</td><td>0.093</td><td>0.0789</td><td>0.06</td></tr><tr><td> $a$ </td><td>0.3</td><td>0.3</td><td>0.2679</td><td>0.45</td><td>0.2679</td><td>0.3225</td><td>0.3771</td><td>0.45</td></tr><tr><td> $b$ </td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td> $a \cup b$ </td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td> $c$ </td><td>0.2</td><td>0</td><td>0.1786</td><td>0.14</td><td>0.1786</td><td>0.167</td><td>0.1554</td><td>0.14</td></tr><tr><td> $a \cup c$ </td><td>0.2</td><td>0.4</td><td>0.2551</td><td>0.26</td><td>0.2551</td><td>0.2566</td><td>0.2580</td><td>0.26</td></tr><tr><td> $b \cup c$ </td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td> $a \cup b \cup c$ </td><td>0.3</td><td>0.3</td><td>0.1913</td><td>0.09</td><td>0.1913</td><td>0.1609</td><td>0.1305</td><td>0.09</td></tr></table>

![](/api/attachments/GVHBNGPB/fulltext/images/6ad23cf3858f4c279808d696758847fdd07f6270921e012a08d5065444b3900b.jpg)  
Fig. 3. Distances between combined mass functions

Example. Assume a frame of discernment $\Omega = \{ a , b , c \}$ and two sources s and s providing two mass functions m and m . Table 1 illustrates conjunctive and cautious combinations as well as mixed combination in the cases where $\gamma = 0 , \gamma = 0 . 3 , \gamma = 0 . 6$ and γ = 1. When $\gamma = 0 ,$ mixed and cautious combinations are equivalent; when γ = 1, mixed and conjunctive combinations are equivalent, otherwise it is a weighted average by γ ∈]0,1[.

Finally, to illustrate the proposed mixed combination rule and compare it to other combination rules, three mass functions are generated randomly using Algorithm 2. These mass functions are combined with conjunctive, Dempster, Yager, disjunctive, cautious and mean combination rules. They are also combined with the mixed combination rule with different independence levels.

Fig. 3 illustrates distances<sup>5</sup> between the mixed combination with several degrees of independence and combined mass functions using conjunctive, Dempster, Yager, disjunctive, cautious and mean combination rules. Distances between mixed combination with several independence degrees; and Yager, disjunctive, mean and Dempster's rules are linear and decreasing proportionally to γ.

## 6. Experiments

Because of the lack of real evidential data, we use generated mass functions to test the method detailed above. Moreover, it is dif<sup>fi</sup>cult to simulate all situations with all possible combinations of focal elements for several degrees of independence between sources. First, we generate two sets of mass functions for two sources s and s ; then we illustrate for three sources.

## 6.1. Generated data depiction

Generating sets of n mass functions for several sources depends on sources' independence. We discern cases of independent and depen dent sources.

## 6.1.1. Independent sources

In general, to generate mass functions some information are needed: the number of hypotheses in the frame of discernment, |Ω| and the number of mass functions. We note that number of focal elements, and masses are chosen randomly.

In the case of independent sources, masses can be anywhere and focal elements of both sources are chosen independently. Mass functions o $\dot { \boldsymbol { s } } _ { 1 }$ and $s _ { 2 }$ are generated following Algorithm 2. We note that focal elements, their number and bbms are chosen randomly according to the universal low.

## Algorithm 2. Independent mass functions generating

Require: |Ω|, n : number of mass functions

1: for i = 1 to n do

2: Choose randomly | F |, the number of focal elements on [1, |2Ω|].

3: Choose randomly | F | focal elements noted F

4 Divvy the interval [0, 1] into |F| continuous sub-intervals

5: Focal elements BBMs are intervals sizes

6: end for

7: return n mass functions

## 6.1.2. Dependent sources

The case of dependent sources is a bit dif<sup>fi</sup>cult to simulate as several scenarios can occur. In this section, we will try to illustrate the most common situations.

Generated mass functions for dependent sources are supposed to be consistent and do not enclose any internal con<sup>fl</sup>ict [27]. Consistent mass functions contain at least one focal element common to all focal sets. Fig. 4 illustrates a consistent mass function where all focal elements {A, B, C, D} intersect.

Algorithm 3 generates a set of n consistent mass functions<sup>6</sup> de<sup>fi</sup>ned on a frame of discernment of size |Ω|. In the case of dependent sources, they are almost consistent and at least one of them is dependent on the other. To simulate the case where one source is dependent on another one, consistent mass functions of the <sup>fi</sup>rst one are generated following Algorithm 3, then those of the second source are generated knowing decisions of the <sup>fi</sup>rst one. Algorithm 4 generates a set of mass functions that are dependent on another set of mass functions. Dependence is due to the knowledge of another source's decisions.

## Algorithm 3. Consistent mass functions generating

Require: |Ω|, n : number of mass functions

1: for i = 1 to n do

2 Choose randomly a focal set ω; (it can be a single point) from Ω

3: Find the set S of all focal sets including ωi.

4 Choose randomly | F |, the number of focal elements on [1, |S|]

5: Choose randomly | F | focal elements from S noted F.

6: Divvy the interval [0, 1] into |F| continuous sub-intervals

7: BBMs of focal elements are intervals sizes.

8: end for

9: return n consistent mass functions

![](/api/attachments/GVHBNGPB/fulltext/images/b5143abcbcb3106283f663f51bb4cf0dcacec696be5e922c8a94688709b9794b.jpg)  
Fig. 4. Consistent belief function.

## Algorithm 4. Dependent mass functions generating

<table><tr><td colspan="2">Require: |Ω|, n : number of mass functions, d decision of another source</td></tr><tr><td colspan="2">1: for i = 1 to n do</td></tr><tr><td colspan="2">2: Find the set S of all focal sets including d.</td></tr><tr><td colspan="2">3: Choose randomly | F |, the number of focal elements on [1, |S)].</td></tr><tr><td colspan="2">4: Choose randomly | F | focal elements from S noted F.</td></tr><tr><td colspan="2">5: Divvy the interval [0, 1] into |F| continuous sub-intervals.</td></tr><tr><td colspan="2">6: Focal elements BBMs are intervals sizes.</td></tr><tr><td colspan="2">7: end for</td></tr><tr><td colspan="2">8: return n consistent mass functions</td></tr></table>

## 6.2. Results of tests

Algorithms detailed in the previous section are used to test some cases of sources' dependence and independence. We note that in extreme cases where mass functions are certain or even when focal elements do not intersect, maximal values of independence are obtained. In the case of perfect dependence; mass functions have the same focal elements; however, clusters contain mass functions with consistent focal elements. Clustering is performed according to focal elements and clusters are perfectly linked.

## 6.2.1. Independent sources

In this paragraph, mass functions are independent. Focal elements and bbms are randomly chosen ensuing Algorithm 2. For tests, we choose |Ω| = 5 which is considered as medium-sized frame of discernment and n = 100. Table 2 illustrates the mean of 100 tests in the case of independent sources. The mean of 100 tests for two dependent sources yields to a degree of independence $\gamma = 0 . 6 8 ,$ , thus sources are independent. Assume that $m _ { 1 }$ and $m _ { 2 } ,$ given in Table 1, are provided by two sources $s _ { 1 }$ and $s _ { 1 }$ which independence degree is given in Table 2. Combination of $m _ { 1 }$ and $m _ { 2 }$ is given in Table 3.

Table 2  
Mean of 100 tests on 100 generated mass functions for two sources.

<table><tr><td>Dependence type</td><td>Degree of independence</td><td>Overall independence</td></tr><tr><td rowspan="2">Independence</td><td> $I_d(s_1,s_2) = 0.68, \bar{I}_d(s_1,s_2) = 0.32$ </td><td rowspan="2"> $\gamma = 0.68$ </td></tr><tr><td> $I_d(s_2,s_1) = 0.68, \bar{I}_d(s_2,s_1) = 0.32$ </td></tr><tr><td rowspan="2">Dependence</td><td> $I_d(s_1,s_2) = 0.34, \bar{I}_d(s_1,s_2) = 0.66$ </td><td rowspan="2"> $\gamma = 0.34$ </td></tr><tr><td> $I_d(s_2,s_1) = 0.35, \bar{I}_d(s_2,s_1) = 0.65$ </td></tr></table>

Table 3  
Mixed combination of m and m .

<table><tr><td> $2^{\Omega}$ </td><td> $m_1$ </td><td> $m_2$ </td><td> $m_{Mixed}$  $\gamma = 0.68$ </td><td> $m_{Mixed}$  $\gamma = 0.34$ </td></tr><tr><td> $\emptyset$ </td><td>0</td><td>0</td><td>0.092</td><td>0.076</td></tr><tr><td> $a$ </td><td>0.3</td><td>0.3</td><td>0.3262</td><td>0.3881</td></tr><tr><td> $b$ </td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td> $a \cup b$ </td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td> $c$ </td><td>0.2</td><td>0</td><td>0.1662</td><td>0.1531</td></tr><tr><td> $a \cup c$ </td><td>0.2</td><td>0.4</td><td>0.2567</td><td>0.2583</td></tr><tr><td> $b \cup c$ </td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td> $a \cup b \cup c$ </td><td>0.3</td><td>0.3</td><td>0.1589</td><td>0.1244</td></tr></table>

Table 4  
Mean of 100 tests on 100 generated mass functions for three independent sources.

<table><tr><td>Sources</td><td>Degree of independence</td><td>Pairwise independence</td><td>Overall independence</td></tr><tr><td> $s_{1}-s_{2}$ </td><td> $I_d(s_1,s_2)=0.67, \bar{I}_d(s_1,s_2)=0.33$  $I_d(s_2,s_1)=0.67, \bar{I}_d(s_2,s_1)=0.33$ </td><td> $I(s_1,s_2)=0.67$ </td><td> $\gamma=0.68$ </td></tr><tr><td> $s_{1}-s_{3}$ </td><td> $I_d(s_1,s_3)=0.68, \bar{I}_d(s_1,s_3)=0.32$  $I_d(s_3,s_1)=0.68, \bar{I}_d(s_3,s_1)=0.32$ </td><td> $I(s_1,s_3)=0.68$ </td><td></td></tr><tr><td> $s_{2}-s_{3}$ </td><td> $I_d(s_2,s_3)=0.68, \bar{I}_d(s_2,s_3)=0.32$  $I_d(s_3,s_2)=0.68, \bar{I}_d(s_3,s_2)=0.32$ </td><td> $I(s_2,s_3)=0.68$ </td><td></td></tr></table>

Table 5  
Mean of 100 tests on 100 generated mass functions for three dependent sources.

<table><tr><td>Sources</td><td>Degree of independence</td><td>Pairwise independence</td><td>Overall independence</td></tr><tr><td rowspan="2"> $s_{1}-s_{2}$ </td><td> $I_{d}(s_{1},s_{2}) = 0.35, \bar{I}_{d}(s_{1},s_{2}) = 0.65$ </td><td rowspan="2"> $I(s_{1},s_{2}) = 0.34$ </td><td rowspan="2"> $\gamma = 0.35$ </td></tr><tr><td> $I_{d}(s_{2},s_{1}) = 0.34, \bar{I}_{d}(s_{2},s_{1}) = 0.66$ </td></tr><tr><td rowspan="2"> $s_{1}-s_{3}$ </td><td> $I_{d}(s_{1},s_{3}) = 0.32, \bar{I}_{d}(s_{1},s_{3}) = 0.68$ </td><td rowspan="2"> $I(s_{1},s_{3}) = 0.31$ </td><td rowspan="2"></td></tr><tr><td> $I_{d}(s_{3},s_{1}) = 0.31, \bar{I}_{d}(s_{3},s_{1}) = 0.69$ </td></tr><tr><td rowspan="2"> $s_{1}-s_{3}$ </td><td> $I_{d}(s_{2},s_{3}) = 0.36, \bar{I}_{d}(s_{2},s_{3}) = 0.64$ </td><td rowspan="2"> $I(s_{2},s_{3}) = 0.35$ </td><td rowspan="2"></td></tr><tr><td> $I_{d}(s_{3},s_{2}) = 0.35, \bar{I}_{d}(s_{3},s_{2}) = 0.65$ </td></tr></table>

To illustrate the case of three independent sources, three sets of 100 independent mass functions are generated following Algorithm 2 with $| \Omega | = 5 .$ The mean of 100 tests are illustrated in Table 4.

## 6.2.2. Dependent sources

In the case of dependent sources, mass functions are generated ensuing Algorithms 3 and 4. For tests, we choose $| \Omega | = 5$ and $n = 1 0 0$ We generate 100 mass functions of both s and s for 100 times and then compute the average of $\mathrm { I _ { d } } ( s _ { 1 } , s _ { 2 } ) , \mathrm { I _ { d } } ( s _ { 2 } , s _ { 1 } )$ ) and $I ( s _ { 1 } , s _ { 2 } )$ ). Table 2 illustrates the mean of 100 independence degrees of two dependent sources providing each one 100 randomly generated mass functions. These sources are dependent with a degree $1 - \gamma = 0 . 6 6 .$ . In Table $3 , m _ { 1 }$ and m are combined using the mixed rule when $\gamma = 0 . 3 4 .$

To illustrate the case of three dependent sources, three sets of 100 dependent mass functions are generated following Algorithms 3 and 4 when |Ω| = 5. The mean of 100 degrees of independence are illustrated in Table 5.

Finally, assume that $m _ { 1 } , m _ { 2 }$ and $m _ { 3 }$ of Table 6 are three mass functions de<sup>fi</sup>ned on a frame of discernment $\Omega = \{ a , b , c \}$ and provided by three dependent sources. The mixed combined mass function when their degree of independence is $\gamma = 0 . 3 5$ is also given in Table 6.

Table 6  
Mixed combination of m , m and $m _ { 3 } .$

<table><tr><td> $2^{\Omega}$ </td><td> $m_{1}$ </td><td> $m_{2}$ </td><td> $m_{1}$ </td><td> $m_{Mixed}$  $\gamma = 0.35$ </td></tr><tr><td> $\emptyset$ </td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>a</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>b</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td> $a \cup b$ </td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>c</td><td>0.03</td><td>0.05</td><td>0</td><td>0.32</td></tr><tr><td> $a \cup c$ </td><td>0.39</td><td>0.07</td><td>0.04</td><td>0.24</td></tr><tr><td> $b \cup c$ </td><td>0.3</td><td>0.47</td><td>0.22</td><td>0.29</td></tr><tr><td> $a \cup b \cup c$ </td><td>0.28</td><td>0.41</td><td>0.74</td><td>0.15</td></tr></table>

## 7. Conclusion

In this paper, we proposed a method to learn sources cognitive independence in order to use the appropriate combination rule either when sources are cognitively dependent or independent. Sources are cognitively independent if they are different, not communicating and they have distinct evidential corpora. The proposed statistical approach is based on a clustering algorithm applied to mass functions provided by several sources. A pair of sources' independence is deduced from weights of linked clusters after a matching of their clusters. Independence degree of sources can either guide the choice of the combination rule if it is either 1 or 0; when it is a degree over ]0,1[, we propose a new combination rule that weights the conjunctive and cautious combinations with sources' independence degree.

## References

[1] L.A. Zadeh, Fuzzy sets, Inf. Control. 8 (3) (1965) 338–353.

[2] D. Dubois, H. Prade, Representation and combination of uncertainty with belief functions and possibility measures, Comput. Intell. 4 (3) (1988) 244–264.

[3] A.P. Dempster, Upper and lower probabilities induced by a multivalued mapping, Ann. Math. Stat. 38 (2) (1967) 325–339.

[4] G. Shafer, A Mathematical Theory of Evidence, Princeton University Press, 1976.

[5] A. Martin, C. Osswald, Toward a combination rule to deal with partial con<sup>fl</sup>ict and speci<sup>fi</sup>city in belief functions theory, International Conference on Information Fusion, Québec, Canada, 2007, pp. 1–8.

[6] C.K. Murphy, Combining belief functions when evidence con<sup>fl</sup>icts, Decis. Support. Syst. 29 (1) (2000) 1–9.

[7] P. Smets, R. Kennes, The transferable belief model, Artif. Intell. 66 (2) (1994) 191–234.

[8] R.R. Yager, On the Dempster–Shafer framework and new combination rules, Inf. Sci. 41 (2) (1987) 93–137.

[9] E. Lefèvre, Z. Elouedi, How to preserve the con<sup>fl</sup>ict as an alarm in the combination of belief functions? Decis, Support, Syst, 56 (2013) 326–333

[10] T. Denœux, Conjunctive and disjunctive combination of belief functions induced by nondistinct bodies of evidence, Artif Intell 172 (2–3) (2008) 234–264

[11] B. Ben Yaghlane, P. Smets, K. Mellouli, Belief function independence: I. The marginal case, Int. J. Approx. Reason. 29 (1) (2002) 47–70.

[12] B. Ben Yaghlane, P. Smets, K. Mellouli, Belief function independence: II. The conditional case, Int. J. Approx. Reason. 31 (1–2) (2002) 31–75.

[13] P. Smets, Belief functions: the disjunctive rule of combination and the generalized Bayesian theorem, Int. J. Approx. Reason. 9 (1) (1993) 1–35.

[14] P. Smets, The combination of evidence in the transferable belief model, IEEE Trans. Pattern Anal. Mach. Intell. 12 (5) (1990) 447–458.

[15] P. Smets, The canonical decomposition of a weighted belief, International Joint Conference on Artificial Intelligence vol. 2. Morgan Kaufman Montréal Ouébec Canada. 1995, pp. 1896–1901.

[16] L.A. Zadeh, A mathematical theory of evidence (book review), AI Mag. 5 (3) (1984) 81-83.

[17] P. Smets, The nature of the unnormalized beliefs encountered in the transferable belief model, in: D. Dubois, M.P. Wellman (Eds.), International Conference on Uncertainty in Arti<sup>fi</sup>cial Intelligence, Morgan Kaufmann, Stanford, California, USA, 1992, pp. 292–297.

[18] A. Martin, A.-L. Jousselme, C. Osswald, Con<sup>fl</sup>ict measure for the discounting operation on belief functions, International Conference on Information Fusion, Cologne, Germany, 2008, pp. 1–8.

[19] A.-L. Jousselme, D. Grenier, E. Bossé, A new distance between two bodies of evidence, Inf. Fusion 2 (2) (2001) 91–101.

[20] S. Ben Hariz, Z. Elouedi, K. Mellouli, Clustering approach using belief function theory, in: J. Euzenat, J. Domingue (Eds.), 7th Conference of the European Society for Fuzzy Logic and Technology, Lecture Notes in Computer Science, Vol. 4183, Atlantis Press Varna, Bulgaria, 2006, pp. 162–171.

[21] M. Chebbah, A. Martin, B. Ben Yaghlane, About sources dependence in the theory of belief functions, in: T. Denœux, M.-H. Masson (Eds.), International Conference on Belief Functions, Vol. 164 of Advances in Intelligent and Soft Computing, Springer Berlin Heidelberg, Compiègne, France, 2012, pp. 239–246.

[22] P. Smets, R. Kruse, Uncertainty Management in Information Systems: From Needs to SolutionsCh. The Transferable Belief Model for Belief Representation, Springer US, Boston, 1997, pp. 343–368.

[23] J. Munkres, Algorithms for the Assignment and Transportation Problems, J. Soc. Ind. Appl, Math, 5 (1) (1957) 32-38

[24] F. Bourgeois, J.-C. Lassalle, An Extension of the Munkres Algorithm for the Assignment Problem to Rectangular Matrices, Commun. ACM 12 (14) (1971) 802–804.

[25] C. Wemmert, P. Gançarski, A multi-view voting method to combine unsupervised classi<sup>fi</sup>cations, IASTED International Conference on Arti<sup>fi</sup>cial Intelligence and Applications, Málaga, Spain, 2002, pp. 447–453.

[26] P. Gançarski, C. Wemmert, Collaborative multi-strategy classi<sup>fi</sup>cation: Application to per-pixel analysis of images, International Workshop on Multimedia Data Mining: Mining Integrated Media and Complex Data, Chicago, Illinois, USA, 2005, pp. 15–22

[27] M. Daniel, Con<sup>fl</sup>icts Within and Between Belief Functions, IPMU, 2010. 696–705.

Mouna Chebbah was a temporary assistant professor (ATER) in computer science at IUT of Lannion in France. She received her Master's degree from the University of Tunis, Higher Institute of Management in 2010. She has a Ph. D. degree in computer science at the University of Tunis and the University of Rennes 1. She is member of the Laboratory of Operations Research, Decision and Control of Processes (LARODEC); and the Institute for Research in Computer Science and Random Systems (IRISA). Her researches are focused on the theory of belief functions, con<sup>fl</sup>ict management and dependence.

Arnaud Martin is a professor at IUT of Lannion and is the head of computer science department. He received his Master's degree in Probability in 1998 and his Ph.D. degree in Signal Processing from the University of Rennes in 2001. Afterward, he received a HDR (“Habilitation à Diriger des Recherches”) in computer sciences in 2009. Pr. Arnaud Martin worked on speech recognition during three years from 1998 to 2001 at France Telecom R&D, Lannion, France. He worked in the department of statistic and data mining (STID) of the IUT of Vannes, France, as a temporary assistant professor (ATER) during two years from 2001 to 2003. In 2003, he joined the laboratory E3I2 at the ENSTA Bretagne, Brest, France, as a teacher and researcher till 2010. Afterwards, he joined the laboratory IRISA UMR 6074 at the University of Rennes 1 as a full professor. His research interests are mainly related to the belief functions for the classi<sup>fi</sup>cation, data fusion and data mining.

Boutheina Ben Yaghlane is a professor at Business School of Carthage (IHEC Carthage, University of Carthage) and is a member of the Laboratory of Operations Research, Decision and Control of Processes (LARODEC). She received her Ph.D. degree in 2002 from the University of Tunis (The Higher Institute of Management of Tunis), with a thesis enti tled “Uncertainty Representation and Reasoning in Directed Evidential Networks" cosupervised by Professor Khaled Mellouli (LARODEC, IHEC — Tunisia) and Professor Philippe Smets (IRIDIA. ULB — Belgium). She obtained the “Habilitation à Diriger des Recherches” from the same institution in 2006. Her research interests concern the theory of belief functions, graphical models, data mining, conflict management, and, more precisely, the management of uncertainty in evidential networks.
