---
otero_id: 11372
otero_key: "BAB2HHTV"
title: "Potential optimality and robust optimality in multiattribute decision analysis with incomplete information: A comparative study"
authors: "Guiwu Wei; Jiamin Wang; Jian Chen"
year: "2013"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2013.02.005"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Potential optimality and robust optimality in multiattribute decision analysis with incomplete information: A comparative study

Guiwu Wei <sup>a,</sup>⁎, Jiamin Wang <sup>b</sup>, Jian Chen <sup>c</sup>

<sup>a</sup> School of Economics and Management, Chongqing University of Arts and Sciences, 319 Honghe Road, Yongchuan District, Chongqing, 402160, China

<sup>b</sup> College of Management, Long Island University Post, 720 Northern Blvd, Brookville, NY, 11548-1300, USA

<sup>c</sup> Research Center for Contemporary Management, Tsinghua University, Beijing 100084, China

## a r t i c l e i n f o

Article history: Received 24 May 2012 Received in revised form 22 November 2012 Accepted 4 February 2013 Available online 27 February 2013

Keywords: Multiattribute decision analysis Incomplete information Potential optimality Robust optimality Minmax regret

## a b s t r a c t

The traditional approach for multiple attribute decision analysis with incomplete information on alternative values and attribute weights is to identify alternatives that are potentially optimal. However, the results of potential optimality analysis may be misleading as an alternative is evaluated under the best-case scenario of attribute weights only. Robust optimality analysis is a conservative approach that is concerned with an assured level of payoff for an alternative across all possible scenarios of weights. In this study, we introduce two measures of robust optimality that extend the robust optimality analysis approach and classify alternatives in consideration into three groups: strong robust optimal, weak robust optimal and robust non-optimal. Mathematical models are developed to compute these measures. It is claimed that robust optimality analysis and potential optimality analysis together provide a comprehensive picture of an alternative's variable payoff. © 2013 Elsevier B.V. All rights reserved.

## 1. Introduction

In a multiattribute decision making (MADM) problem [5] the decision maker (DM) is faced with the task of identifying the best alternative in terms of a number of criteria (attributes). When precise information of the DM's preference is known the choice of the best alternative can be handled in a relatively straightforward manner, say, by evaluating the weighted sum of each alternative's values under all attributes as an aggregate value to gauge the alternative's payoff. However, in reality the DM is usually unable to elicit exact estimations of all decision parameters, such as alternative values and attribute weights [20]. Hence, multiattribute decision analysis with incomplete, or imprecise, or partial, information has become an important research direction in decision analysis.

Under incomplete information the exact parameters are not known but the constraints they satisfy, e.g., ordinal or interval judgments on them, might have been extracted. Various approaches to process incomplete information were proposed. Simulation studies showed that the rank order centroid weights and the maximum entropy weights are good approximates for ranked attribute weights [1,2,4]. Sarabando and Dias [15] developed centroid-based decision rules with a high likelihood of identifying the best alternative when both attribute weights and alternative values under every attribute are fully ranked.

Pairwise comparisons and potentially optimality analysis (PO analysis) are commonly used for incomplete information not restricted to the ordinal form [3,8,9,11–14]. While these approaches help narrow the DM's choices to a subset of the available alternatives, called nondominated (ND) alternatives and potentially optimal (PO) alternatives, the identi<sup>fi</sup>cation of the best alternative still eludes the DM unless there exists an alternative that outperforms its peers in all attributes. Furthermore, the quality of the alternatives recommended by these approaches is questionable. As Dias and Climaco [7] noted, the binary preference relations established on the basis of pairwise comparisons are not easy to utilize meaningfully. PO analysis assesses alternatives in their best-case scenarios only. Wang [19] demonstrated that choosing alternatives for PO may cause a signi<sup>fi</sup>cant loss if an unfavorable scenario occurs making the selected alternative severely inferior.

Given incomplete information on both alternative values and attribute weights, Park [13] introduced a three-level PO classi<sup>fi</sup>cation scheme: strong potentially optimal (strong PO), weak potentially optimal (weak PO) and potentially non-optimal (NPO). As summarized in Table 1, an alternative is strong PO if it is better than its peers for all possible scenarios of values and at least one vector of weights. An alternative is weak PO if it is the best for at least some scenarios of feasible values and weights. An alternative is NPO if it is not better than other alternatives under any scenario of decision parameters. Table 1 also presents robust optimality (RO), which will be detailed later in this paper.

In contrast to the optimistic attitude in PO analysis, the minmax regret analysis <sup>fi</sup>rst proposed by Savage [16,17] is a conservative approach. The term “regret” means the discrepancy between the actual payoff of an alternative and the best one that could have been rendered with a different choice. Fishburn [9] suggested the use of the minmax regret criterion as a secondary principle for ranking PO alternatives if an optimal alternative cannot be identi<sup>fi</sup>ed with the available information on weights (state probabilities). However, his exposition was limited to a few special forms of probability information. Wang [19] applied the minmax regret criterion to develop a RO analysis framework for MADM problems with incomplete information on both alternative values and attribute weights. The suggested approach ranks alternatives in terms of their regrets in the worstcase scenarios of unknown decision parameters.

Table 1 Optimality analysis.

<table><tr><td rowspan="2" colspan="2"></td><td colspan="2">Imprecise weights</td></tr><tr><td>Best-case</td><td>Worst-case</td></tr><tr><td rowspan="2">Imprecise values</td><td>Best-case</td><td>Weak PO</td><td>Weak RO</td></tr><tr><td>Worst-case</td><td>Strong PO</td><td>Strong RO</td></tr></table>

It is noted that robustness has been de<sup>fi</sup>ned and interpreted differently in the literature [6]. The maxmin criterion [10,18] captures the DM's aversion to the worst possible outcome of an alternative. However, it is generally believed that the minmax regret criterion adopted in the current study is not so extreme in its conservatism as the maxmin criterion [16]. In this study robustness is in the sense of immunizing an alternative's regret to the changes of attribute weights. Given exact values, an alternative is RO if it is better than its peers even in the worst-case scenario of weights. Compared to PO analysis, research on RO analysis is underdeveloped for MADM problems with incomplete information on both values and weights. Since RO analysis shall be attractive for a DM who has to make decisions under incomplete information, our study is motivated by the gap between its theoretical development and practical signi<sup>fi</sup>cance.

We present in this article two measures of RO and introduce RO de<sup>fi</sup>nitions. As Table 1 indicates, under the worst-case scenario of weights, strong RO represents RO for all scenarios of values, while weak RO signi<sup>fi</sup>es RO for at least one scenario of values. This development facilitates the notion that incomplete information on values and weights leads to an alternative's variable optimality, quanti<sup>fi</sup>ed by its regret, for which the upper bound and lower bound are yielded by RO analysis and PO analysis, respectively. This study extends the RO analysis method Wang [19] proposed and greatly improves our understanding of optimality under incomplete information.

The remainder of the paper is organized as follows. In Section 2, we set the stage by overview the background of our study. In Section 3, RO analysis models are presented and RO classi<sup>fi</sup>cations are introduced. We further discuss solving these models using mathematical programming techniques. In Section 4, a computational example is analyzed to illustrate RO analysis. Finally, concluding remarks are offered.

## 2. Background

Suppose that the DM evaluates a discrete set of alternatives $M = \{ 1 , 2 , \cdots , m \}$ in terms of a set of attributes $N = \{ 1 , 2 , \cdots , n \}$ . The simplest and most common evaluation approach, namely the linear aggregation method, can be summarized as follows.

Let $w _ { j }$ be the weight of attribute $j \in N$ and $x _ { i j }$ be the value of alternative $i \in M$ with respect to attribute $j \in N .$ It is assumed that the values $x _ { i j }$ associated with each attribute j are scaled to the interval [0,1], with 0 and 1 designating respectively the worst and best possible levels. Denote by $\mathbf { w } = ( w _ { 1 } , w _ { 2 } \cdots , w _ { n } ) ^ { t }$ and $\mathbf { x } _ { j } = ( x _ { 1 j } , x _ { 2 j } \ – , x _ { m j } ) ^ { t }$ respectively, the vectors of attribute weights and values associated with each attribute $j \in N .$ Given a n-tuple of value vectors $\mathbf { U } = \left( \mathbf { x } _ { 1 } , \mathbf { x } _ { 2 } , \cdots , \mathbf { x } _ { n } \right)$ we can construct $\mathbf { x } ^ { i } ( \mathbf { U } ) = ( x _ { i 1 } , x _ { i 2 } , \cdots , x _ { i n } ) ^ { t }$ , the vector of values for each alternative i M. When precise information is available, i.e., w and U are known exactly, the multiattribute value (MAV) of an alternative i is assessed using a linear additive weighting function $V _ { i } ( { \bf w } , { \bf U } ) = { \bf w } ^ { t } { \bf x } ^ { i } ( { \bf U } )$

It is more realistic to presume that the DM is able to obtain incomplete information on decision parameters only. Similar to Eum et al. [8] and Park [13], we assume that the weight vector w satis<sup>fi</sup>es linear constraints, i.e., $\mathbf { w } \in S _ { \mathbf { w } } = \{ \mathbf { w } | \mathbf { A w } \leq \mathbf { a } \} ,$ , where $S _ { \mathbf { w } }$ is the set of all feasible weight vectors, A is a p × n matrix containing the constraint coef<sup>fi</sup>cients, p is the number of constraints and a is the vector of constraint righthand-side values. Similarly, for each attribute $j \in N$ it is assumed that incomplete information on x leads to the set of feasible value vectors $S _ { \mathbf { x } _ { j } } = \{ \mathbf { x } _ { j } | \mathbf { B } _ { j } \mathbf { x } _ { j } \{ \pmb { \mathrm { b } } _ { j } \} _ { }$ , where $\mathbf { B } _ { j } \mathrm { ~ i s ~ a ~ } q _ { j } \times m$ matrix containing constraint coef<sup>fi</sup>cients and b is the right-hand-side value vector with $q _ { j }$ elements. As Park [13] suggested, the constraints may have various con<sup>fi</sup>gurations such as weak orders $( w _ { j } \ge w _ { f } , j , f \in N$ and $j \neq f )$ , interval estimates $( x _ { i j } ^ { L } \leq x _ { i j } \leq x _ { i j } ^ { U } , x _ { i j } ^ { L }$ and x<sub>ij</sub><sup>U</sup> are constants, $j \in N$ and $i \in M )$ and ratio bounds $( \nu _ { j f } ^ { L } \leq w _ { j } / w _ { f } \leq \nu _ { j f } ^ { U } , \nu _ { j f } ^ { L }$ and $v _ { j f } ^ { U }$ are constants, $j f \in N )$ relations.

Let $S _ { \mathbf { U } } = S _ { \mathbf { x } _ { 1 } } \times S _ { \mathbf { x } _ { 2 } } \times \cdots \times S _ { \mathbf { x } _ { n } }$ be the Cartesian product of the sets $S _ { \mathbf { x } _ { i } } , \forall j \in N .$ Recall that given a tuple of value vectors $\mathbf { U } \in S _ { \mathbf { U } } , \mathbf { x } ^ { i } ( \mathbf { U } )$ represents a feasible realization of the values of alternative i. We require that the sets $S _ { \mathbf { w } }$ and $S _ { \mathbf { U } }$ be not empty, i.e., the MADM problem is feasible. Not knowing exact parameters, the DM is prone to make a decision that could be proven “wrong” later, which would make the DM feel regret. The perspective of regret is adopted throughout this study.

A feasible scenario of decision parameters can be characterized by $( \mathbf { w } , \mathbf { U } )$ , where $\mathbf { w } \in S _ { \mathbf { w } }$ and $\mathbf { U } \in S _ { \mathbf { U } } .$ Let ϕ be the set of all these feasible scenarios. The DM's regret associated with a scenario $( { \pmb w } , { \pmb U } ) \in \phi$ for selecting alternative k, rather than alternative h, is triggered by the disparity between their actual payoffs. If we gauge the payoff of an alternative by its MAV, then the regret, denoted by $c _ { k h } ( \boldsymbol { \mathsf { w } } , \boldsymbol { \mathsf { U } } )$ , is calculated as $c _ { k h } ( \mathbf { w } , \mathbf { U } ) = \mathbf { w } ^ { t } ( \mathbf { x } ^ { h } ( \mathbf { U } ) - \hat { \mathbf { x } } ^ { k } ( \mathbf { U } ) )$ .

We now present important concepts in the existing literature in terms of regret.

De<sup>fi</sup>nition 2.1. Alternative k is dominated by alternative h if $c _ { k h } ( \boldsymbol { \mathbf { w } } , \boldsymbol { \mathbf { U } } ) > 0$ holds for any $\mathbf { w } \in S _ { \mathbf { w } }$ and $\mathbf { U } \in S _ { \mathbf { U } }$

De<sup>fi</sup>nition 2.2. An alternative is nondominated if it is not dominated by any other alternative.

De<sup>fi</sup>nition 2.3. Alternative k is weak PO if $\alpha _ { k } = \underset { ( \mathbf { w } , \mathbf { U } ) \in \phi } { m i n } \underset { h \in M } { a x } c _ { k h } ( \mathbf { w } , \mathbf { U } ) = 0 .$

De<sup>fi</sup>nition 2.4. Alternative k is strong PO if $\beta _ { k } = m a x m i n m a x ~ c _ { k h }$ $( \mathbf { w } , \ \mathbf { U } ) = 0 .$

For an overview of identifying dominance and potential optimality with incomplete information using mathematical programming techniques the reader is referred to [13].

Given a feasible scenario w; U ; $C _ { k } ( { \mathbf { w } } , { \mathbf { U } } ) = \operatorname* { m a x } _ { h \in { \cal M } } { c _ { k h } ( { \mathbf { w } } , { \mathbf { U } } ) }$ measures the loss that results from choosing alternative k without prior knowledge that (w, U) is the true scenario. It is evident that $C _ { k } ( \mathbf { w } , \mathbf { U } ) \geq 0 ,$ , while $C _ { k } ( \mathbf { w } , \mathbf { U } ) = 0$ indicates that alternative k is optimal under the scenario. By de<sup>fi</sup>nition, an alternative is weak PO if it is optimal for some feasible scenarios of values and weights, while an alternative is strong PO if it is optimal for all feasible scenarios of values and at least one feasible vector of weights. Note $\beta _ { k } \geq \alpha _ { k } .$ . It follows that there exists at least one ND alternative and one weak PO alternative, but a strong PO alternative may not be available. We hence call an alternative k strong potentially quasi optimal (strong PQO) if $\beta _ { k } = m i n \beta _ { h } .$ . As shown in Table 1, we can classify alternatives into three groups Using the two PO measures: strong PO (strong PQO), weak PO, and NPO.

PO analysis assesses an alternative's optimality in terms of the most favorable scenario of attribute weights. As Wang [19] demonstrated, adopting an alternative by its potentially optimality may eventually lead to a signi<sup>fi</sup>cant loss if the true scenario de<sup>fi</sup>es optimistic expectations. In contrast to PO analysis, minmax regret analysis is a conservative approach that advocates adopting an alternative even suboptimal in the best-case scenario of weights so as to minimize the worst-case loss. Applying the minmax regret criterion, Wang [19] introduced a measure of RO, $\gamma _ { k } = \operatorname* { m } _ { ( \mathbf { w } , \mathbf { U } ) \in \phi } \operatorname* { m a x } _ { h \in M } c _ { k h } ( \mathbf { w } , \mathbf { U } )$ , which is the maximum regret for choosing alternative k across all possible scenarios. Robust optimality de<sup>fi</sup>ned in terms of the measure $\gamma _ { k }$ is referred to as strong RO in this study so as to be distinguished from weak RO, which we will develop in the next section.

De<sup>fi</sup>nition 2.5. Alternative k is strong RO if $\gamma _ { k } = m i n \ \gamma _ { h } = 0$ and strong robust quasi optimal (strong RQO) if $\gamma _ { k } = m i n \ \gamma _ { h } > 0$

The concept of strong RQO is introduced because a perfect strong RO alternative may not exist. $\gamma _ { k }$ is a stringent measure of RO. In the next section, we extend RO analysis by introducing a relaxed measure of RO.

## 3. Robust optimality analysis

In Section 3.1, we develop weak robust optimality analysis (weak RO analysis). We also discuss the relationships between RO and PO. In Section 3.2, mathematical programming developments are provided.

## 3.1. Weak RO

Let $\delta _ { k } = \underset { \mathbf { U } \in S _ { \mathbf { U } } \mathbf { w } \in S _ { \mathbf { w } } h \in M } { m i n } a x \{ c _ { k h } ( \mathbf { w } , \ \mathbf { U } )$ . Note $\delta _ { k } = \underset { \mathbf { U } \in S _ { \mathbf { U } } \mathbf { W } \in S \mathbf { W } } { m i n } a x \ : C _ { k } ( \mathbf { w } _  \mathrm  $ ; U ≥0 for any alternative k. We now de<sup>fi</sup>ne the concept of weak RO in terms of $\delta _ { k } .$

De<sup>fi</sup>nition 3.1. Alternative k is weak RO if $\delta _ { k } = \operatorname* { m i n } _ { h \in M } \ \delta _ { h } = 0$ and weak robust quasi optimal (weak RQO) if $\delta _ { k } = \operatorname* { m i n } _ { h \in M } \delta _ { h } > 0 .$

Fig. 1 shows the difference between strong RO and weak RO. It is assumed that no weight information is available and all values of the alternatives in consideration lie within given intervals. Note that under exact values an alternative k is RO if it is not component-wise dominated, i.e. $x _ { k j } \ge x _ { h j }$ holds $\forall h \in M , \ \forall j \in N ,$ and PO if it not dominated by any convex combination of its peers. By de<sup>fi</sup>nitions, it is easy to see that alternative 6 is strong RO and weak RO as it is RO even under the worst-case scenario for its values, while alternative 4 is weak RO (but not strong RO) because there exists at least one scenario of values for which it is not dominated, component-wise, by any other alternatives. In other words, alternative 6 is always RO, while alternative 4 is sometimes RO. We note that alternative 6 is also weak PO and strong PO. It is clear that alternatives 2, 3, and 5 are dominated, while alternatives 1 and 4 are not dominated by a convex combination of the other alternatives under the respective best-case scenario of values and therefore are weak PO.

![](/api/attachments/BAB2HHTV/fulltext/images/ae0cbd1171cc3d52b37beffbcccfc5d0266f7d49e09faefb9d251cd081e0f250.jpg)  
Fig. 1. Illustration of strong robust optimality and weak robust optimality.

In Fig. 2, alternative 6 is replaced by alternative 6′. Now only alternative 5 is dominated. We realize that a weak RO must reach point A and a strong RO, if available, should be in the region "east and north" of point B. It is clear that no alternative in consideration is strong RO, but alternative 4 is the only alternative that is weak RO. By de<sup>fi</sup>nition, alternatives 1, 2, 4 and $6 ^ { \prime }$ are weak PO as their ranges of values overlap with the region con<sup>fi</sup>ned by the straight lines. It seems dif<sup>fi</sup>cult to discriminate the quality of alternatives 1, 2, 4, and 6′ if we rely on PO analysis only. Combining the results of PO analysis and RO analysis, though, we note that the payoff of choosing alternative 4 is reasonably well compared to the other alternatives at least under the best-case scenario of values. This example suggests that PO analysis may not provide a complete picture of the quality of an alternative and RO analysis is necessary for our thorough understanding.

Since $\delta _ { k } \leq \gamma _ { k } ,$ an alternative k that is strong RO must be weak RO. However, it is possible that none of the alternatives is strong RO or weak RO. We now can divide alternatives into three sub-groups in terms of measures $\delta _ { k }$ and γ : strong RO (RQO), weak RO (RQO) and robust non-optimal (NRO).

As proven in Wang [19], a strong RO or a strong RQO alternative is not dominated. Next we show that an alternative that is weak RO or weak RQO is also nondominated. We note that this characterization is absolutely necessary for any alternative optimal in some sense.

Proposition 3.1. A weak RO alternative or a weak ROQ alternative is nondominated.

Proof. It is suf<sup>fi</sup>cient to prove that a weak ROQ alternative is nondominated. Assume that alternative k is weak ROQ and dominated by alternative h. It follows that $c _ { k h } ( \boldsymbol { \mathbf { w } } , \boldsymbol { \mathbf { U } } ) > 0$ holds for every scenario $( \mathbf { w } , \mathbf { U } ) \in \phi$ and $\delta _ { k } = m i n \ \delta _ { g }$ . We thus claim $c _ { k m } ( \boldsymbol { \mathbf { w } } , \boldsymbol { \mathbf { U } } ) > c _ { h m } ( \boldsymbol { \mathbf { w } } , \boldsymbol { \mathbf { U } } )$ $\forall m \in M$ . Let $\delta _ { k } = c _ { k i } ( \mathbf { \bar { w } } ^ { * } , \mathbf { U } ^ { * } )$ and $\delta _ { h } = c _ { h q } ( \mathbf { w } ^ { \prime } , \mathbf { U } ^ { \prime } )$ where alternatives i and q are not necessarily identical. Note $\delta _ { k } \geq c _ { k q } ( \mathbf { w } ^ { \prime } , \mathbf { U } ^ { * } ) > c _ { h q } ( \mathbf { w } ^ { \prime }$ $\mathbf { U } ^ { * } ) \geq \delta _ { h } ,$ which contradicts our knowledge that alternative k is weak ROQ. □

In a similar way, we can prove that weak PO, strong PO and strong PQO imply nondominance. Given an alternative $k , C _ { k } ( \mathbf { w } , \mathbf { U } )$ can be regarded as a function of scenario (w, U). $\alpha _ { k }$ and $\gamma _ { k }$ bound $C _ { k } ( \mathbf { w } , \mathbf { U } )$ from below and above, respectively. As $\alpha _ { k } \le \beta _ { k } \le \gamma _ { k }$ and $\alpha _ { k } \le \delta _ { k } \le \gamma _ { k } ,$ strong RO leads to strong PO and weak PO, while weak RO indicates weak PO only.

![](/api/attachments/BAB2HHTV/fulltext/images/aed0241be68972a37f3f21e9d99cc05d16c66339df38600df15a3317d11b2764.jpg)  
Fig. 2. Illustration of potential optimality and robust optimality.

Table 2  
Imprecise information on values.

<table><tr><td></td><td>Cost</td><td>Vendor</td><td>Functionality</td><td>Ease of use</td></tr><tr><td>SMERP</td><td>0.8</td><td>1st</td><td>[0.5, 0.75]</td><td>1</td></tr><tr><td>Dezone</td><td>1</td><td>3rd</td><td>[0, 0.25]</td><td>1</td></tr><tr><td>Kweb</td><td>0.4</td><td>4th</td><td>[0.75, 1]</td><td>[0.7, 0.8]</td></tr><tr><td>Single</td><td>0.4</td><td>5th</td><td>[0.5, 0.75]</td><td>1</td></tr><tr><td>UniERP</td><td>0</td><td>1st</td><td>1</td><td>0</td></tr></table>

## 3.2. Computational methods

## 3.2.1. Strong RO analysis

Wang [19] suggested that the strong RO measure $\gamma _ { k }$ can be obtained by a pair-wise evaluation approach. To complete our investigation of RO analysis, we describe brie<sup>fl</sup>y this computational method below.

For a given pair of alternatives k and h, let $r _ { k h } = \underset { ( \mathbf { w } , \mathbf { u } ) \in \phi } { m a x } ~ c _ { k h } ( \mathbf { w } , \mathbf { U } )$ It was shown in Wang [19] that $\gamma _ { k } = \operatorname* { m a x } _ { h \in M } \ r _ { k h } .$ where $r _ { k k } = 0 \mathrm { a n d } r _ { k h }$ is returned by the following model for h ≠ k:

$$
\begin{array}{c} r _ {k h} = \max _ {\mathbf {w}, \mathbf {x} _ {j} \forall j \in N} \mathbf {w} ^ {t} \left(\mathbf {x} ^ {h} - \mathbf {x} ^ {k}\right) \\ s. t. \\ \mathbf {A w} \leq \mathbf {a}, \\ \mathbf {B} _ {j} \mathbf {x} _ {j} \leq \mathbf {b} _ {j}, \quad \forall j \in N \end{array}\tag{1}
$$

Adopting a variable-alternation method suggested by Lee et al. [12], additional nonnegative variables are introduced: $y _ { i j } = w _ { j } x _ { i j } ,$ $\forall \ : i \in M$ and $\forall j \in N$ and model (1) can be shown to be equivalent to the linear program below:

$$
\begin{array}{c} \max _ {\mathbf {w}, \mathbf {y} _ {j} \forall j \in N} \mathbf {1} ^ {t} \left(\mathbf {y} ^ {h} - \mathbf {y} ^ {k}\right) \\ s. t \\ \mathbf {A w} \leq \mathbf {a}, \\ \mathbf {B} _ {j} \mathbf {y} _ {j} - w _ {j} \mathbf {b} _ {j} \leq 0, \quad \forall j \in N, \\ \mathbf {y} _ {j} \geq 0, \quad \forall j \in N, \end{array}\tag{2}
$$

where 1 is the unit column vector, $\mathbf { y } _ { j } = ( y _ { 1 j } , y _ { 2 j } , . . . , y _ { m j } ) ^ { t }$ and $\mathbf { y } ^ { i } = ( y _ { i 1 } , y _ { i 2 } , . . . , y _ { i n } ) ^ { t }$

An alternative method to solve the nonlinear programming model (Eq. (1)) is to convert imprecise values to exact values for some forms of incomplete information, such as bounded and ordinal values and then solve the resulting linear program,

$$
\begin{array}{c} r _ {k h} = \max _ {\mathbf {w}, \mathbf {v} _ {j} \forall j \in N} \mathbf {w} ^ {t} \left(\mathbf {v} ^ {h} - \mathbf {v} ^ {k}\right) \\ s. t. \\ \mathbf {A w} \leq \mathbf {a} \end{array}\tag{3}
$$

with $\nu _ { i j }$ denoting the value of alternative i under attribute j and $\mathbf { v } ^ { i } = ( \dot { \nu } _ { i 1 } , \nu _ { i 2 } , . . . , \nu _ { i n } ) ^ { t }$

Recall that strong RO analysis assesses an alternative's regret under the worst-case scenario of values. If all values lie within <sup>fi</sup>xed bounds, i.e., $x _ { i j } \in [ x _ { i j } ^ { L } , x _ { i j } ^ { U } ] ,$ , we can choose exact values $\begin{array} { r } { \nu _ { k j } = x _ { k j } ^ { L } } \end{array}$ and $\nu _ { h j } = x _ { h j } ^ { U }$ for model (3).

Now assume that the following strict order relations are present for the values with respect to attribute j:

$$
x _ {1 j} - x _ {2 j} \geq \varepsilon_ {1}, x _ {2 j} - x _ {3 j} \geq \varepsilon_ {2}, \dots , x _ {m - 1, j} - x _ {m j} \geq \varepsilon_ {m - 1},\tag{4}
$$

where $\varepsilon _ { i } s$ are known positive numbers with $\sum _ { i = 1 } ^ { m - 1 } \varepsilon _ { i } \le 1 , x _ { 1 j } = 1$ and $x _ { m j } = 0 .$ . It is easy to derive that in model (3) $\stackrel { \cdot \mathrm { ~ \wedge ~ } } { \boldsymbol { \nu } } _ { 1 j } = 1 , ~ \boldsymbol { \nu } _ { k j } = \sum _ { i = k } ^ { m - 1 } \varepsilon _ { i }$ $\mathrm { i f } 1 < k < m , \ : v _ { h j } = 1 - \sum _ { i = k } ^ { h - 1 } \varepsilon _ { i } \mathrm { ~ i f ~ } 2 \leq h < k , \ : v _ { h j } = v _ { k j } - \sum _ { i = k } ^ { h - 1 } \varepsilon _ { i } \mathrm { ~ i f ~ } k < h \leq$ $m - 1$ and $\nu _ { m j } = 0 .$

If values are in weak orders, we set $\varepsilon _ { i } = 0 \forall \ \mathrm { i }$ i and obtain $\nu _ { 1 j } = 1$ $\nu _ { k j } = 0 \mathrm { ~ i f ~ } 1 < k < m , \nu _ { h j } = 1 \mathrm { ~ i f ~ } 2 \leq h < k , \nu _ { h j } = \nu _ { k j } \mathrm { ~ i f ~ } k < h \leq \bar { m } - 1$ and $\nu _ { m j } = 0$

## 3.2.2. Weak RO analysis

Computing the weak RO measure $\delta _ { k }$ via its de<sup>fi</sup>nition directly involves multistage optimization. Here we suggest a method that derives an approximate of $\delta _ { k }$ by solving the following linear programming model for each pair of alternatives k and $h \neq k \colon$

$$
\begin{array}{c} d _ {k h} = \underset {\boldsymbol {\lambda}, \mathbf {x} _ {j} \forall \in N} {\text { min }} \mathbf {a} ^ {t} \lambda \\ s. t. \\ \mathbf {A} ^ {t} \lambda \geq \mathbf {x} ^ {h} - \mathbf {x} ^ {k}, \\ \mathbf {B} _ {j} \mathbf {x} _ {j} \leq \mathbf {b} _ {j}, \quad \forall j \in N, \\ \lambda \geq 0, \end{array}\tag{5}
$$

where $\mathsf { \pmb { \Lambda } } = ( \lambda _ { 1 } , \lambda _ { 2 } , \cdots , \lambda _ { p } ) ^ { t }$ is a vector of $p$ components (recall that $S _ { \mathbf { w } }$ is de<sup>fi</sup>ned by p weight constraints). Given the value vector x for any attribute $j ,$ the above model is dual to model (1) with λ being the vector of dual variables to constraints Aw ≤ a.

Note $d _ { k k } = 0$ . We can make the following proposition.

Proposition 3.2. For any alternatives k and h $, d _ { k h } = \underset { \mathbf { U } \in S _ { \mathbf { U } } \mathbf { W } \in S _ { \mathbf { w } } } { \mathit { m i n m a x } } ~ c _ { k h } ( \mathbf { w } , \ \mathbf { U } )$ Proof. Given a scenario of values $\mathbf { U } \in S _ { \mathbf { U } } ,$ we can construc $\mathbf { x } ^ { h } ( \mathbf { U } )$ and $\mathbf { x } ^ { k } ( \mathbf { U } )$ and the objective function value of model (5) equals max $c _ { k h } ( \boldsymbol { \mathbf { w } } , \boldsymbol { \mathbf { U } } )$ as it is dual to model (1) with exact values. The propw∈S<sub>w</sub> osition follows because the model is a minimization problem over U ∈ S . □

Let $\delta _ { k } = m a x \ d _ { k h } .$ . By the above proposition, we have $\delta _ { k } \ge \delta _ { k } \ : \mathsf { a s } \ : \delta _ { k } =$ $\operatorname* { m i n } _ { \mathbf { U } \in S _ { \mathbf { U } } \mathbf { w } \in S _ { \mathbf { w } } h \in M } { a \overset { h \in M } { x } } ( \mathbf { w } , \mathbf { \textbf { U } } ) { \geq } \operatorname* { m i n } _ { \mathbf { U } \in S _ { \mathbf { U } } \mathbf { w } \in S _ { \mathbf { w } } } \ c _ { k h } ( \mathbf { w } , \mathbf { \textbf { U } } ) = d _ { k h }$ holds for any alternative h. $\delta _ { k }$ is easier to obtain and therefore can be used to approximate $\delta _ { k } , \delta _ { k }$ and γ also bound the interval where $\delta _ { k }$ falls into.

For a given alternative $k , \delta _ { k }$ and $\delta _ { k }$ are not necessarily equal in a general case. But the equality holds if there exists a scenario of values $\mathbf { U } \in S _ { \mathbf { U } } ,$ , which is optimal to model (5) for all pairs of $( k , h )$ . It is therefore certain that our suggested approach returns the true value of $\delta _ { k }$ when the values follow special con<sup>fi</sup>gurations, such as <sup>fi</sup>xed bounds, strict orders and weak orders. For these relations, model (5) reduces to the following simple linear program,

Exact values $\nu _ { i 2 }$ for computing $r _ { k h }$ in model (7).

<table><tr><td>i</td><td>k</td><td>SMERP</td><td>Dezone</td><td>Kweb</td><td>Single</td><td>UniERP</td></tr><tr><td>SMERP</td><td></td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td></tr><tr><td>Dezone</td><td></td><td> $1 - \varepsilon_1$ </td><td> $\varepsilon_2 + \varepsilon_3$ </td><td> $1 - \varepsilon_1$ </td><td> $1 - \varepsilon_1$ </td><td> $1 - \varepsilon_1$ </td></tr><tr><td>Kweb</td><td></td><td> $1 - \varepsilon_1 - \varepsilon_2$ </td><td> $\varepsilon_3$ </td><td> $\varepsilon_3$ </td><td> $1 - \varepsilon_1 - \varepsilon_2$ </td><td> $1 - \varepsilon_1 - \varepsilon_2$ </td></tr><tr><td>Single</td><td></td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>UniERP</td><td></td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td></tr></table>

Exact values $\nu _ { i 2 }$ for computing $d _ { k h }$ in model (8).

<table><tr><td>i k</td><td>SMERP</td><td>Dezone</td><td>Kweb</td><td>Single</td><td>UniERP</td></tr><tr><td>SMERP</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td></tr><tr><td>Dezone</td><td> $\varepsilon_2 + \varepsilon_3$ </td><td> $1 - \varepsilon_1$ </td><td> $1 - \varepsilon_1$ </td><td> $\varepsilon_2 + \varepsilon_3$ </td><td> $\varepsilon_2 + \varepsilon_3$ </td></tr><tr><td>Kweb</td><td> $\varepsilon_3$ </td><td> $\varepsilon_3$ </td><td> $1 - \varepsilon_1 - \varepsilon_2$ </td><td> $\varepsilon_3$ </td><td> $\varepsilon_3$ </td></tr><tr><td>Single</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>UniERP</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td></tr></table>

$$
\begin{array}{c} d _ {k h} = m i n _ {\lambda} \mathbf {a} ^ {t} \lambda \\ s. t. \end{array}\tag{6}
$$

$$
\begin{array}{c} \mathbf {A} ^ {t} \lambda \geq \mathbf {v} ^ {h} - \mathbf {v} ^ {k}, \\ \lambda \geq 0 \end{array}
$$

with $v _ { k j } = x _ { k j } ^ { U }$ and $\nu _ { h j } = x _ { h j } ^ { L }$ if any value $x _ { i j }$ belongs to a <sup>fi</sup>xed interval $[ x _ { i j } ^ { L } , x _ { i j } ^ { U } ]$ , and $\nu _ { 1 j } = 1 , \ \nu _ { k j } = 1 - \sum _ { i = 1 } ^ { k - 1 } \varepsilon _ { i } { \mathrm { ~ i f ~ } } 1 < k < m , \nu _ { h j } = \nu _ { k j } + \sum _ { i = h } ^ { k - 1 } \varepsilon _ { i }$ if $2 \leq h < k , ~ \nu _ { h j } = \sum _ { 1 = h } ^ { m - 1 } \varepsilon _ { i }$ if $k < h \leq m - 1$ and $\nu _ { m j } = 0$ if all values under an attribute j are in strict orders as speci<sup>fi</sup>ed in Eq. (4).

## 4. Illustrative example

Park [13] conducted PO analysis on a procurement decision problem of a small Korean company on the basis of its assessment on <sup>fi</sup>ve ERP (Enterprise Resource Planning) systems. We analyze this application to demonstrate the expositions above.

The <sup>fi</sup>ve ERP systems in consideration are treated as potential alternatives: SMERP (alternative 1), Dezone (alternative 2), Kweb (alternative 3), Single (alternative 4) and UniEPR (alternative 5). These alternatives are evaluated in terms of four key attributes: Cost (attribute 1), Vendor Support (attribute 2), Functionality (attribute 3) and Ease of Use (attribute 4). The values of attribute 1 are exact, the values of attribute 2 are in ordinal relations, the values of attribute 3 are bounded and the values of attribute 4 are a mix of exact data and bounded data.

The information and data available on these values are presented in Table 2. Preference information of weights was also collected, which can be described as $w _ { 1 } \geq w _ { 2 } \geq w _ { 3 } \geq w _ { 4 } , w _ { 1 } - w _ { 2 } \leq w _ { 2 } -$ $w _ { 3 }$ and $w _ { 2 } - w _ { 3 } \geq w _ { 3 } - w _ { 4 } ,$

In RO analysis, we can apply the exact value approach developed in Sections 3.2.1 and 3.2.2. Given alternative k, we have $\gamma _ { k } =$ max r , $\delta _ { k } = \delta _ { k } = \operatorname* { m } _ { h \in M } \ d _ { k h }$ , where $r _ { k k } = d _ { k k } = 0$ , r<sub>kh</sub> and $d _ { k h }$ are h M

returned, respectively, by models (3) and (6), presented below in scalar form rather than in matrix form to facilitate understanding:

s:t:

$$
r _ {k h} = \max _ {w _ {j}, j = 1, 2, 3, 4} \sum_ {j = 1} ^ {4} w _ {j} \left(v _ {h j} - v _ {k j}\right), \quad h = 1, 2, 3, 4, 5, h \neq k\tag{7}
$$

$$
\begin{array}{c} w _ {1} \geq w _ {2} \geq w _ {3} \geq w _ {4} \geq 0 \\ w _ {1} - 2 w _ {2} + w _ {3} \leq 0 \\ w _ {2} - 2 w _ {3} + w _ {4} \geq 0 \\ w _ {1} + w _ {2} + w _ {3} + w _ {4} = 1. 0. \end{array}
$$

$$
d _ {k h} = \min _ {\lambda_ {q}, q = 1, 2, \dots , 7} \lambda_ {6} - \lambda_ {7}, h = 1, 2, 3, 4, 5, h \neq k
$$

s:t:

$$
\begin{array}{c} - \lambda_ {1} + \lambda_ {4} + \lambda_ {6} - \lambda_ {7} \geq v _ {h 1} - v _ {k 1} \\ \lambda_ {1} - \lambda_ {2} - 2 \lambda_ {4} - \lambda_ {5} + \lambda_ {6} - \lambda_ {7} \geq v _ {h 2} - v _ {k 2} \\ \lambda_ {2} - \lambda_ {3} + \lambda_ {4} + 2 \lambda_ {5} + \lambda_ {6} - \lambda_ {7} \geq v _ {h 3} - v _ {k 3} \\ \lambda_ {3} - \lambda_ {5} + \lambda_ {6} - \lambda_ {7} \geq v _ {h 4} - v _ {k 4} \\ \lambda_ {q} \geq 0, q = 1, 2, \dots , 7. \end{array}\tag{8}
$$

We note model (8) follows from Eq. (6) because incomplete information of alternative values is presented in the forms of <sup>fi</sup>xed bounds and orders only and therefore the exact values of each alternative at the optimal solution can be determined in advance. It is clear that in both models $\nu _ { 1 1 } = 0 . 8 , \nu _ { 2 1 } = 1 , \nu _ { 3 1 } = \nu _ { 4 1 } = 0 . 4 , \nu _ { 5 1 } = 0 , \nu _ { 1 4 } =$ $\nu _ { 2 4 } = \nu _ { 4 4 } = 1$ , and $\nu _ { 5 4 } = 0$ . For bounded values, it is natural to set $\nu _ { h 3 } = x _ { h } ^ { U } , \nu _ { k 3 } = x _ { k } ^ { L } , \nu _ { 3 4 } = 0 . 7 \mathrm { ~ i f ~ } k = 3$ and $\nu _ { 3 4 } = 0 . 8$ otherwise in model (7), and $\nu _ { h 3 } = x _ { h } ^ { L } , \nu _ { k 3 } = x _ { k } ^ { U } , \nu _ { 3 4 } = 0 . 8 { \mathrm { ~ i f ~ } } k = 3$ and $\nu _ { 3 4 } = 0 . 7$ otherwise in model (8).

We can mathematically present the incomplete information on the values of attribute 2 in the following form: $x _ { 1 2 } = x _ { 5 2 } = 1$ $x _ { 1 2 } - x _ { 2 2 } \geq \varepsilon _ { 1 } , x _ { 2 2 } - x _ { 3 2 } \geq \varepsilon _ { 2 } , x _ { 3 2 } - x _ { 4 2 } \geq \varepsilon _ { 3 } ,$ , and $x _ { 4 2 } = 0$ (following [13] we set $\varepsilon _ { i } = 0$ to designate weak order relations and $\varepsilon _ { i } = 0 . 1$ strict order relations). Table 3 and Table 4 list the values assigned to alternatives k and h for attribute 2 in the above models, which are derived using the exact value approach for order relations developed in Section 3. The <sup>fi</sup>rst row in these tables indicates alternative k, the alternative under evaluation. For instance, according to Table 3, for model (7) with $k = 1$ and $h = 2$ , we have $\nu _ { k 2 } = 1$ and $\nu _ { h 2 } = 1 - \varepsilon _ { 1 }$

The optimality measures are summarized in Table 5 under $\varepsilon _ { i } = 0$ and $\varepsilon _ { i } = 0 . 1$ separately (the PO measure $\alpha _ { k }$ and $\beta _ { k }$ were provided in [13]). As the results show, alternative 1 (SMERP) is weak PO, strong PO, weak RO and strong RQO, while alternative 2 (Dezone) is weak PO. The overall quality of these two alternatives is signi<sup>fi</sup>cantly better than that of the others under both $\varepsilon _ { i } = 0$ and $\varepsilon _ { i } = 0 . 1$ , with SMERP ranked the best and Dezone ranked the second. Among the other three alternatives, alternative 3 (Kweb) and alternative 5 (UniERP) appear to be the one to prefer when the values are favorable and not favorable, respectively.

## 5. Concluding remarks

RO analysis is a conservative procedure that identi<sup>fi</sup>es the alternative with the minimum regret for the least favorable vector of attribute weights. In the current study, a weak RO measure is introduced that completes the framework of RO analysis when information on values is incomplete. It is shown that strong RO (weak RO) analysis evaluates the payoff of an alternative in the worst-case scenario (best-case scenario) for values.

Table 5 Optimality measures.

<table><tr><td rowspan="2">k</td><td colspan="2"> $\alpha_k$ </td><td colspan="2"> $\beta_k$ </td><td colspan="2"> $\delta_k$ </td><td colspan="2"> $\gamma_k$ </td></tr><tr><td> $\varepsilon_i = 0$ </td><td> $\varepsilon_i = 0.1$ </td><td> $\varepsilon_i = 0$ </td><td> $\varepsilon_i = 0.1$ </td><td> $\varepsilon_i = 0$ </td><td> $\varepsilon_i = 0.1$ </td><td> $\varepsilon_i = 0$ </td><td> $\varepsilon_i = 0.1$ </td></tr><tr><td>SMERP</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0.133</td><td>0.1</td></tr><tr><td>Dezone</td><td>0</td><td>0</td><td>0.2</td><td>0.133</td><td>0.0125</td><td>0.0375</td><td>0.47</td><td>0.39</td></tr><tr><td>Kweb</td><td>0.025</td><td>0.075</td><td>0.425</td><td>0.04</td><td>0.04</td><td>0.433</td><td>0.8</td><td>0.7</td></tr><tr><td>Single</td><td>0.2875</td><td>0.2875</td><td>0.4125</td><td>0.4125</td><td>0.7</td><td>0.7</td><td>0.8</td><td>0.75</td></tr><tr><td>UniERP</td><td>0.22</td><td>0.22</td><td>0.27</td><td>0.27</td><td>0.533</td><td>0.533</td><td>0.667</td><td>0.633</td></tr></table>

The regret of choosing an alternative is variable due to incomplete information on values as well as weights. It lies in a range that is bounded by the strong PO measure from below and the strong RO measure from above. Hence, integrating the results of PO analysis and RO analysis is essential to a complete and reliable understanding of an alternative's optimality.

To compute the strong RO measure for an alternative, a pairwise evaluation approach is suggested and m-1 nonlinear programming models are to be solved. We can transform each nonlinear programming model into a linear program by either applying a variable alternation method or converting imprecise values into exact values for some special forms of judgments on values. For the weak RO measure, a similar approach is proposed. However, this approach may return an approximate only unless the incomplete information of values follows selected con<sup>fi</sup>gurations.

## Acknowledgment

The authors would like to thank the referee for the comments to help improve the quality of the presentation. The second author also would like to thank the Academic Partners Program (APP) of FICO for providing Xpress-MP. This study was supported by the National Natural Science Foundation of China under Grant No. 61174149 and the Natural Science Foundation Project of CQ CSTC of the People's Republic of China under Grant No. CSTC 2011BA0035.

## References

[1] B.S. Ahn, Compatible weighting method with rank order centroid: Maximum entropy ordered weighted averaging approach, Enropean Journal of Operational Research 212 (2011) 552–559.

[2] B.S. Ahn, K.S. Park, Comparing methods for multiattribute decision making with ordinal weights, Computers and Operations Research 35 (2008) 1265–1279.

[3] A.D. Athanassopoulos, V.V. Podinovski, Dominance and potential optimality in multiple criteria decision analysis with incomplete information, Journal of the Operational Research Society 48 (1997) 142-150

[4] F.H. Barron, B.E. Barrett, Decision quality using ranked attribute weights, Management Science 42 (1996) 1515-1523.

[5] V. Belton, T. Stewart, Multiple Criteria Decision Analysis: An Integrated Approach Kluwer Academic Dordrech 2002

[6] L.C. Dias, A note on the role of robustness analysis in decision-aiding processes, in: B. Roy, M. Aloulou, R. Kalai (Eds.), Robustness in OR-DA, Lamsade. 53–70.

[7] L.C. Dias, J.N. Climaco, Additive aggregation with variable interdependent parameters: the VIP analysis software, Journal of the Operational Research Society 51 (2000) 1070–1082.

[8] Y.S. Eum, K.S. Park, S.H. Kim, Establishing dominance and potential optimality in multi-criteria analysis with imprecise weight and value, Computers and Operations Research 28 (2001) 397–409.

[9] P.C. Fishburn, Analysis of decisions with incomplete knowledge of probabilities, Operations Research 13 (1965) 217–237.

[10] I. Gilboa, D. Schmeidler, Maxmin expected utility with non-unique prior, Journal of Mathematical Economics 18 (1989) 141–153.

[11] G.B. Hazen, Partial information, dominance, and potential optimality in multiattribute utility theory, Operations Research 34 (1986) 296–310.

[12] K.S. Lee, K.S. Park, Y.S. Eum, K. Park, Extended methods for identifying dominance and potential optimality in multi-criteria analysis with imprecise information European Journal of Operational Research 134 (2001) 557–563.

[13] K.S. Park, Mathematical programming models for characterizing dominance and potential optimality when multicriteria alternative values and weights are simultaneously incomplete, IEEE Transactions on Systems, Man, and Cybernetics - Part A: Systems and Humans 34 (2004) 601–614

[14] A. Salo, R. Hamalainen, Preference ratio in multiattribute evaluation PRIME — elicitation and decision procedures under incomplete information, IEEE Transactions on Systems Man and Cybernetic: Part A 31 (2001) 338–356.

[15] P. Sarabando, L. Dias, Simple procedures of choice in multicriteria problems without precise information about the alternatives' values, Computers and Operations Research 37 (2010) 2239–2247

[16] L.J. Savage, The theory of statistical decision, Journal of the American Statistical Association 46 (1951) 55–67.

[17] L.J. Savage, The Foundations of Statistics, John Wiley and Sons, New York, 1954. [18] A. Wald, Statistical Decision Functions, John Wiley, New York, 1950.

[19] J. Wang, Robust optimization analysis for multiple attribute decision making problems with imprecise information. Annals of Operations Research 197 (2012) 109–122

[20] M. Weber, Decision making with incomplete information, European Journal of Operational Research 28 (1987) 44–57.

Guiwu Wei has an MSc and a PhD degree in applied mathematics from SouthWest Petroleum University, Business Administration from school of Economics and Management at SouthWest Jiaotong University, China, respectively. From May 2010 to April 2012, he was a Postdoctoral Researcher with the School of Economics and Management, Tsinghua University, Beijing, China. He is a Professor in the Department of Economics and Management at Chongqing University of Arts and Sciences. He has published more than 90 papers in journals, books and conference proceedings including journals such as Expert Systems with Applications, Applied Soft Computing, Knowledge and Information Systems, Knowledge-based Systems, International Journal of Uncertainty, Fuzziness and Knowledge-Based Systems, International Journal of Computational Intelligence Systems and Information: An International Journal. He has published 1 book. He has participated in several scienti<sup>fi</sup>c committees and serves as a reviewer in a wide range of journals including Computers & Industrial Engineering, International Journal of Information Technology and Decision Making, Knowledge-based Systems, Information Sciences, International Journal of Computational Intelligence Systems and European Journal of Operational Research. He is currently interested in Decision Making and Computing with Words.

Dr. Wang is an associate professor at the Department of Management in the College of Management, C.W. Post Campus of Long Island University. In 2000 he obtained his Ph.D. in management science and engineering from Tsinghua University, Beijing, China. From September 2000 to August 2002, he served as a postdoctorate fellow in Operations Management at Joseph L. Rotman School of Business, University of Toronto, Canada. Dr. Wang's research activities focus on facility location, decision analysis, logistics and service operations. He has published research articles in Operations Research, IIE Transactions, European Journal of Operational Research and Annals of Operations Research.

Chen Jian (cheni@sem tsinghua edu.cn) received the B.Sc. degree in Electrical Engineering from Tsinghua University. Bejjing, China, in 1983, and the M.Sc. and the Ph.D. degree both in Systems Engineering from Tsinghua University in 1986 and 1989. He is the Lenovo Chair Professor and Chairman of the Management Science Department, and Director of the Research Center for Contemporary Management, Tsinghua University. His main research interests include supply chain management, e-commerce, and decision support systems. Dr. Chen has published over 150 papers in refereed journals and has been a principal investigator for over 30 grants and research contracts with the National Science Foundation of China, governmental organizations and companies. He has been invited to present several plenary lectures. He is a past recipient of multiple awards and recognitions, including a Ministry of Education Changjiang Scholar Award, an IBM Faculty Award, and an Outstanding Contribution Award from the IEEE Systems, Man and Cybernetics Society. He has also been elected as an IEEE Fellow. He is the editor of Journal of Systems Science and Systems Engineering, an area editor of Electronic Commerce Research and Applications, and an associate editor of IEEE Transactions on Systems, Man and Cybernetics: Part A, IEEE Transactions on Systems, Man and Cybernetics: Part C, and the Asia Paci<sup>fi</sup>c Journal of Operational Research. He also serves on multiple editorial boards of leading journals, including Flexible Services and Manufacturing, the International Journal of Electronic Business, International Journal of Information Technology and Decision Making, and Systems Research and Behavioral Science.
