---
otero_id: 11590
otero_key: "35BDM6JA"
title: "A hybrid heuristic approach for attribute-oriented mining"
authors: "Maybin K. Muyeba; Keeley Crockett; Wenjia Wang; John A. Keane"
year: "2014"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2013.08.012"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A hybrid heuristic approach for attribute-oriented mining

Maybin K. Muyeba <sup>a,</sup>⁎, Keeley Crockett <sup>a</sup>, Wenjia Wang <sup>b</sup>, John A. Keane <sup>c</sup>

<sup>a</sup> SCMDT, Manchester Metropolitan University, UK

<sup>b</sup> School of Computing Sciences, University of East Anglia, UK

<sup>c</sup> School of Computer Science, University of Manchester, UK

## a r t i c l e i n f o

Article history: Received 16 February 2012 Received in revised form 18 July 2013 Accepted 22 August 2013 Available online 4 September 2013

Keywords: Induction Heuristic Threshold Interestingness Cluster Algorithm

## a b s t r a c t

We present a hybrid heuristic algorithm, clusterAOI, that generates a more interesting generalised table than obtained via attribute-oriented induction (AOI). AOI tends to overgeneralise as it uses a <sup>fi</sup>xed global static threshold to cluster and generalise attributes irrespective of their features, and does not evaluate intermediate interestingness. In contrast, clusterAOI uses attribute features to dynamically recalculate new attribute thresholds and applies heuristics to evaluate cluster quality and intermediate interestingness. Experimental results show improved interestingness, better output pattern distribution and expressiveness, and improved runtime.

© 2013 Elsevier B.V. All rights reserved.

## 1. Introduction

Pattern interestingness is determined by an objective measure [18] or by subjective user interpretation [15]. Threshold-driven algorithms [18,12] generate many rules which need to be <sup>fi</sup>ltered to determine interestingness [15]. Attribute-oriented induction (AOI) [9] extracts high-level generalised rules by repeatedly replacing and clustering [14,16] attribute values using domain knowledge<sup>1</sup> [9,17]. AOI uses attribute and relation generalisation thresholds to limit the number of distinct attributes and rules generated.

## 1.1. Problem and approach

We aim to obtain generalised and hence more interesting rules than AOI. AOI overgeneralises to “ANY” values [3,13,14] as it uses a <sup>fi</sup>xed global static threshold to generalise attributes irrespective of their features and does not dynamically evaluate interestingness. The aim here is to use attribute features to dynamically recalculate new thresholds, and to apply heuristics to evaluate cluster quality and interestingness. The most interesting rules consist of mostly interior concepts [6,7,14].

This paper presents clusterAOI, a hybrid heuristic algorithm based on [16], which produces a more interesting generalised table than AOI. A three-fold strategy is used: (1) generalise conservatively [14] selected clusters of attribute values that share common properties and satisfy a newly computed local attribute threshold; (2) evaluate intermediate interestingness result for each attribute and of the algorithm, using heuristic functions [16]; (3) apply Kullback–Leibler (KL) divergence and cluster quality (CQ) interestingness [16] to the output [10]. Experiments show improved interestingness (up to 4 times), better output pattern distribution and expressiveness (about 1.5 times), and improved runtime (about 2 times).

The process is as follows: (1) pre-clusterAOI analyses attribute features to dynamically generate local thresholds; (2) intermediateclusterAOI uses probabilistic semantic similarity between clusters of attribute values and evaluates cluster interestingness, resulting in improved interestingness and runtime; (3) in post-clusterAOI the <sup>fi</sup>nal output table's interestingness is determined using CQ (a global harmonic mean) and KL.

As an example we apply AOI and clusterAOI to the cancer Wisconsin dataset [19] (Table 1). We calculate KL for divergence and cluster quality (CQ). clusterAOI gave 0% overgeneralisation while AOI gave 50%; KL was 1.7 times higher and CQ 3 times higher. clusterAOI also produced twice as many informative rules (NOT-ANY), i.e. 100% compared to 50% for AOI. Similar weaknesses were highlighted in [21]. Overall, clusterAOI improves pattern understandability, intelligent interpretation and interestingness.

The rest of the paper is structured as follows: Section 2 discusses related work; Section 3 presents prerequisites and de<sup>fi</sup>nitions; Section 4 introduces pre-clusterAOI; Section 5 presents intermediate-clusterAOI and post-clusterAOI; Section 6 describes experimentation; and Section 7 concludes. A running Case Study (Table 2) is extended as each aspect of the approach is introduced.

Table 1  
Comparing <sup>fi</sup>nal output on NOT-ANY values, breast cancer dataset [19].

<table><tr><td>Algorithm</td><td>cellSize</td><td>bNuclei</td><td>nNuclei</td><td>Mitoses</td><td>Count</td><td>%ANY</td><td>%NOT-ANY</td></tr><tr><td rowspan="2">AOI</td><td>AboutAve</td><td>AboutAve</td><td>Any</td><td>Any</td><td>485</td><td>50</td><td>50</td></tr><tr><td>AboutAve</td><td>AboveAve</td><td>Any</td><td>Any</td><td>93</td><td></td><td></td></tr><tr><td colspan="8">G.Thr = 2, KL = 0.63, CQ = 11.59</td></tr><tr><td rowspan="3">clusterAOI</td><td>AboutAve</td><td>AboutAve</td><td>AboutAve</td><td>AboutAve</td><td>483</td><td>0</td><td>100</td></tr><tr><td>AboutAve</td><td>AboveAve</td><td>AboutAve</td><td>AboutAve</td><td>99</td><td></td><td></td></tr><tr><td>AboveAve</td><td>AboveAve</td><td>AboveAve</td><td>AboutAve</td><td>71</td><td></td><td></td></tr><tr><td colspan="8">G.Thr = 2, KL = 1.08, CQ = 34.6</td></tr></table>

## 2. Related work

Generally, AOI algorithms [3,4,8,9,13,14] are threshold-driven i.e. they stop generalisation when thresholds are reached (the only interestingness measure used), and do not consider attribute features and proprieties [3]. Further, most AOI algorithms evaluate interestingness before (pre-AOI) and after (post-AOI) generalisation, less so during (intermediate-AOI) generalisation. Differences still exist in these algorithms. For pre-AOI, [21] removes discriminating data that may affect interestingness. Others [1,7] analyse depths and weighted heights of concept hierarchies to determine interestingness, but only use a single <sup>fi</sup>xed weight value for interior concepts which, naturally, may vary between hierarchies. For intermediate-AOI, [3] uses multiple-level support thresholds per attribute and order generalised tuples according to association strength. Others [1,11] select the next attribute generalisation path to follow but are computationallyintensive. In [13], repeating attribute values are preserved to minimize overgeneralisation and produce many output rules. In post-AOI [6,16], the number of interior concepts in the output is applied as an interestingness measure using only the original global thresholds. Further the algorithm in [21] is unsuitable for large datasets (its order complexity being $O ( n ^ { 3 } ) )$

Existing work has been applied in isolation and largely overgeneralises the rules. Still, there remain issues such as manual selection of thresholds that may be unsuitable to apply globally to all attributes (one size <sup>fi</sup>ts all problem). Secondly, no AOI algorithm evaluates interestingness in all three phases: pre-, intermediate- and post-. Our earlier work suggests that there can be improvements in interestingness of generalised patterns [16].

We propose a coordinated hybrid algorithm, clusterAOI, to address these limitations: clusterAOI has three phases: pre- (Section 4)— addresses attribute feature measure (or entropy); intermediate-(Section 5)—evaluates interestingness during generalisation (locally and globally) using attribute clustering functions [16,17]; and post-(Section 5)—evaluates interestingness of rules (from clusters) using cluster similarity, tightness and local interestingness functions; and overall via the KL function [10], often used in information theory, which gives differences in information divergence between data distributions in the rules.

<table><tr><td>Diameter</td><td>Colour</td></tr><tr><td>2</td><td>Red</td></tr><tr><td>7</td><td>Blue</td></tr><tr><td>34</td><td>Yellow</td></tr><tr><td>25</td><td>Green</td></tr><tr><td>28</td><td>Orange</td></tr><tr><td>8</td><td>Violet</td></tr><tr><td>16</td><td>Red</td></tr></table>

## 3. Prerequisites and de<sup>fi</sup>nitions

clusterAOI addresses interestingness as follows: let relation R be de-<sup>fi</sup>ned on dataset $D \subseteq R$ with n tuples; attribute A and attribute hierarchy $H _ { i }$ pairs exist for m attributes i.e. $\{ ( A _ { 1 } , H _ { 1 } ) , ( A _ { 2 } , H _ { 2 } ) , . . . , ( A _ { m } , H _ { m } ) \} , A _ { m + 1 }$ <sub>1</sub> is an attribute storing the count of tuples in R and t is a global threshold. Then $\sum \left| A _ { m + 1 } , \emptyset \right| = n ,$ with domain values Dom $( A _ { m + 1 } , \emptyset ) \in Z ^ { + }$ , where $Z ^ { + }$ are positive integers, with $H _ { m + 1 } = \emptyset$ . Given a generalisation space $B _ { i } = A _ { i } \cup H _ { i }$ for each attribute, we use entropy function $\nabla ( A _ { i } )$ to generate new local thresholds $\{ L . t h r _ { i } : L . T h r _ { i } \geq G . T h r , i = 1 , . . . , m \}$ , for each $A _ { i } ,$ where G.Thr is the global threshold. $L . T h r _ { i } \geq G .$ Thr means at most |L.Thr<sub>i</sub>| distinct values per attribute, thus minimising over generalisation. With a description language ${ \mathrm { L } } = ( { \mathrm { B } } _ { \mathrm { i } } f )$ there is a level-by-level “nearest parent” generalisation function $f \colon B _ { i } \to D o m ( H _ { i } )$ and a partial order $\left( \prec , B _ { i } \right)$ for <sup>fi</sup>nding parents (or descriptions) $\left\{ \varphi _ { 1 } , \varphi _ { 2 } , . . . , \varphi _ { k } \right\}$ in B i.e. a cluster $\{ \varphi _ { 1 } , . . . , \varphi _ { j } \}$ has parent $\varphi ^ { \prime } = m i n \left\{ f ( \varphi _ { 1 } ) , \ldots f ( \varphi _ { j } ) \right\}$ [17]. This leads to De<sup>fi</sup>nitions 1 and 2.

De<sup>fi</sup>nition 1. Cluster. Given attribute $A _ { i } = \{ a _ { 1 } ^ { i } . . . , a _ { k } ^ { i } \}$ , an attribute cluster of $A _ { i }$ is de<sup>fi</sup>ned as ${ \cal C } _ { j } = \{ c _ { 1 } , . . . , c _ { n } \} , C _ { j } \subseteq A _ { i } , n \leq k .$

De<sup>fi</sup>nition 2. Generalisable cluster. Given a cluster $C _ { j } = \{ c _ { 1 } , . . . . , c _ { n } \}$ of $A _ { i }$ and local threshold $\alpha = L . T h r _ { i } ,$ cluster $C _ { j }$ is generalisable $\mathrm { ~ f ~ } | C _ { j } | \geq \epsilon$ α and $f ( c _ { k } ) = f ( c _ { l } ) , \forall k , l \leq n , k \neq l .$

Generalisation of each attribute stops when its optimal value (a local interestingness value) is reached (De<sup>fi</sup>nition 3, Section 5.1), and in the global case, when a global optimal value is encountered (Theorem 1, Section 5.1). We derive these values by applying heuristic functions to attribute clusters. Without loss of generality, interestingness [16] can be described by both distance and cluster tightness [17] depending on tuple distribution in a summary table [10] (a cluster of attribute values). The agglomerative hierarchical clustering distance $\delta _ { n }$ and tightness $\tau _ { n }$ functions [17] are used for overall interestingness: $G _ { n } : ( \delta _ { n } , \tau _ { n } ) {  } \Re ^ { + }$ . These functions exhibit both monotone and anti-monotone properties during generalisation. Therefore, the problem of mining generalised patterns is a 4-tuple $( \nabla , I _ { L } ^ { i } f , I _ { g } ^ { T } )$ (see Appendix E) de<sup>fi</sup>ned as follows:

(1) Find attribute signi<sup>fi</sup>cance (entropy) $\nabla ( A _ { i } )$ and generate new local threshold $L . T h r _ { i } ;$ discussed in Sections 4.1 and 4.2;

(2) Find local attribute interestingness in iteration k and aggregate values using a cluster tightness function $\dot { I _ { L } ^ { i } } ( A _ { i } )$ discussed in Section 5.1;

(3) Generalise values using distance function $f ( B _ { i } )$ subject to L.Thr ;

(4) Find global cluster interestingness $I _ { g } ^ { T } ( . . . )$ of table T by aggregating local values from (2) using Eq. (7) discussed in Sections 5.2–5.4.

After rule generation, we then measure divergence (using KL) and cluster quality (CQ) in the rules. KL is an information divergence measure between two probability distributions (uniform and actual): higher values show good distribution and variety of output values, indicating improved interestingness [10]. Given m tuples in a table $T = \{ t _ { 1 } , . . . , t _ { m } \}$ and actual probabilities $\{ p _ { 1 } , . . . , p _ { m } \}$ , the divergence is $K L ( T ) = \log _ { 2 } m - \sum _ { i = 1 } ^ { m } p _ { i } \log _ { 2 } p _ { i } ,$ , where $K L ( T ) \geq 0$ , bounded by log m. CQ is an interestingness heuristic function [16] applied to the top k rules of the output (Eq. (7), Section 5.2), similar to heuristics in $[ 1 , 7 ] . ^ { 2 }$

## 4. Pre-clusterAOI

Pre-clusterAOI aims to <sup>fi</sup>nd each attribute's local threshold L.Thr (from G.Thr) using attribute features such as concept hierarchy and distinct values.

![](/api/attachments/35BDM6JA/fulltext/images/8863cdbbcfbdd9067ec7a6fa819817bfeaed0119aaa671997b8b544ce5ef0f16.jpg)  
Fig. 1. Concept hierarchies for Diameter and Colour.

Case Study (1). Table 2 shows a soccer dataset with concept hierarchies given in Fig. 1. Given $G . T h r = 2 ,$ , Diameter and Colour have 7 and 6 distinct values respectively, while prime Table 3 (the first generalised table) and Table 4 have 2 and 3 distinct values respectively (see Section 5.2 for the generalisation process, where Colour is generalised one step more than Diameter).

## 4.1. Attribute feature significance

We adapt a query-based approach [14] to determine attribute significance from distinct values in D and concept hierarchy node values in $H _ { i }$ [6,16]. Attribute signi<sup>fi</sup>cance is used to compute local thresholds by entropy function $\nabla ( A )$ ; entropy $e _ { i } ( A _ { i } )$ is calculated by Eq. (1):

$$
\nabla (A _ {i}) = - \left(\sum_ {i} ^ {m} \log p (c _ {i}) + \log \frac {| D |}{\operatorname{dist} (D , A _ {i})}\right) = e _ {i} = \operatorname{sig} (A _ {i})\tag{1}
$$

where dist(D,A ) or dist(A ) is the distinct values of attribute A in D, taking the absolute value of Eq. (1) and each $c _ { i } \in H _ { i }$ is a non-leaf concept.

Case Study (2). Note that dist(D,A<sub>i</sub>) is initially calculated from Table 2. Merging Table 3 gives Table 4, and generalising “Colour” further (see Section 4.2) finally gives Table 5. We can calculate attribute significance values:

$$
e _ {d i a m t e r} = \operatorname{sig} (\text { diameter }) = \nabla (A _ {\text { diameter }}) = 4. 7 6.
$$

Similarly, $e _ { c o l o u r } = 9 . 7 8 ,$ , meaning that Colour is more significant than Diameter. From this, thresholds can be recalculated.

## 4.2. Multi-threshold generation

Using Eq. (1) for entropy $e _ { i } ,$ different local thresholds (L.Thr ) can be generated for each attribute $A _ { i }$ by a linear function $D _ { 1 } ( e _ { i } , G . T h r )$ in $e _ { i } ,$ where we de<sup>fi</sup>ne $E = M A X ( e _ { 1 } , e _ { 2 } , . . . , e _ { m } )$ . Eq. (2) states that $L . T h r _ { i } \ge G . T h r$ (i.e. in the worst case each attribute is generalised using G.Thr). Hence, choosing the maximum entropy value is justi<sup>fi</sup>ed.

$$
D _ {1} \left(e _ {i}, G. T h r\right) = \frac {(G . T h r * E) + \left| E - e _ {i} \right|}{E} = G. T h r + \frac {\left| E - e _ {i} \right|}{E} = L. T h r _ {i}.\tag{2}
$$

Case Study (3). Using Table 2 and $G . T h r = 2 ,$ we obtain entropy values for Diameter $e _ { 1 } = 4 . 7 6$ and Colour $e _ { 2 } = 9 . 7 8$ with L.Thr as follows:

$$
L. T h r _ {\text { colour }} = \frac {(2 * 9 . 7 8) + | 9 . 7 8 - 9 . 7 8 |}{9 . 7 8} = G. T h r = 2
$$

Generalised (or prime) table.

<table><tr><td>Diameter</td><td>Colour</td><td>Count</td></tr><tr><td>Small</td><td>Bluish</td><td>1</td></tr><tr><td>Small</td><td>Bluish</td><td>1</td></tr><tr><td>Medium</td><td>Reddish</td><td>1</td></tr><tr><td>Small</td><td>Reddish</td><td>2</td></tr><tr><td>Medium</td><td>Yellowish</td><td>2</td></tr></table>

$$
L. T h r _ {\text { diameter }} = \frac {(2 * 9 . 7 8) + | 9 . 7 8 - 4 . 7 6 |}{9 . 7 8} = 2. 5 1 > G. T h r
$$

where Max $( 4 . 7 6 , 9 . 7 8 ) = 9 . 7 8 .$ . With value rounding $L . T h r _ { c o l o u r } = 2$ as $| E - e _ { i } | = 0$ while $L . T h r _ { d i a m e t e r } = 3 .$ . Generating $L . T h r _ { i }$ affects each attribute's interestingness (shown in Section 5).

## <sub>5.</sub> Intermediate <sub>and</sub> post-clusterAOI

This section considers interestingness evaluation during generalisation (intermediate-clusterAOI) and of the <sup>fi</sup>nal output table (postclusterAOI).

## 5.1. Attribute interestingness

Higher level concepts are more interesting than leaf nodes [6]; in contrast, “ANY” is uninteresting [7]. This represents a bounded interestingness problem (Proposition 1). AOI [9] uses a distance-driven generalisation method and interestingness should naturally be a distance function [16]. For simplicity, all attribute and concept hierarchy values in the space $B _ { i }$ will be referred to as concepts unless speci<sup>fi</sup>c meanings are required.

## Proposition 1. Concept value interestingness

A concept value $y \in B _ { i }$ is interesting if it is an interior concept. See Appendix A for proof.

Case Study (4). Fig. 1 (Section 4) shows a concept hierarchy for Diameter with interior concepts {small, medium, large} {ANY}. Novices may find range [1…60] and $\ " A N Y "$ values both meaningless and uninteresting. However, they become interesting when diameter size can be determined without knowing specific ball measurements.

Given Proposition 1, generalised attribute A has concept collections $\bigcup _ { k = 1 } ^ { n } c _ { k }$ that give the highest interestingness value, an aggregation of indi-<sup>¼</sup>vidual interestingness values. Section 5.2 de<sup>fi</sup>nes further heuristics for intra-cluster tightness $I _ { 1 } ^ { k } ,$ inter-cluster similarity I<sup>k</sup> and cluster quality I<sup>k</sup> to calculate highest aggregated interestingness at any kth iteration [16], called local (L) interestingness, for each $A _ { i } ,$ denoted $[ I _ { L } ^ { i } ( A _ { i } ) ] ^ { k }$ or simply l<sub>i</sub><sup>k</sup>(X<sup>k</sup>). When L is found, generalisation stops. As values $X ^ { k }$ vary between attributes at each iteration, we aggregate them using a simple harmonic function.

De<sup>fi</sup>nition 3. Local attribute interestingness. Given an attribute $A _ { i } ,$ local heuristic value $X ^ { k } = \{ x _ { 1 } ^ { k } , x _ { 2 } ^ { k } , x _ { 3 } ^ { k } \}$ , and a harmonic aggregation function l<sup>k</sup>(X<sup>k</sup>) with value $\boldsymbol { \nu } ^ { k } = l _ { i } ^ { k } ( \boldsymbol { X } ^ { k } )$ at the kth iteration, the local attribute interestingness of the attribute is $\boldsymbol { \nu } ^ { k + 1 } = l _ { i } ^ { k + 1 } ( \dot { \boldsymbol { X } } ^ { k + 1 } )$ obtained at the (k + 1)th iteration, where $\boldsymbol { \nu } ^ { k } = \operatorname* { m a x } \{ \boldsymbol { \nu } ^ { 0 } , . . . , \boldsymbol { \nu } ^ { k } , \boldsymbol { \nu } ^ { k + 1 } \}$ and $\nu ^ { k } \geq \nu ^ { k + 1 }$

Table 4 Merged prime table.

<table><tr><td>Diameter</td><td>Colour</td><td>Count</td></tr><tr><td>Small</td><td>Bluish</td><td>2</td></tr><tr><td>Medium</td><td>Reddish</td><td>1</td></tr><tr><td>Small</td><td>Reddish</td><td>2</td></tr><tr><td>Medium</td><td>Yellowish</td><td>2</td></tr></table>

Table 5  
clusterAOI <sup>fi</sup>nal table.

<table><tr><td>Diameter</td><td>Colour</td><td>Count</td></tr><tr><td>Medium</td><td>Non-dark</td><td>3</td></tr><tr><td>Small</td><td>Dark</td><td>2</td></tr><tr><td>Small</td><td>Non-dark</td><td>2</td></tr></table>

Note from De<sup>fi</sup>nition 3 that $\nu ^ { k } ,$ the maximum local interestingness (optimum) value, is greater than $\nu ^ { k + 1 }$ . At this point, no further generalisation occurs.

Lemma 1. Interestingness function I monotonically increases for the first k iterations to an optimal value $\nu ^ { k } { \in } \Re ^ { + }$ and then monotonically decreases from the k + 1th iteration. See Appendix B for proof.

It is easy to determine global interestingness simply by a harmonic aggregation at each iteration and <sup>fi</sup>nding the maximum so far.

Case Study (5). From Table 2, G.Thr = 2, local and global interestingness values at each iteration were: Diameter {0.0, 0.14, 0.66, 1.0,…}, Colour {0.0, 0.29, 1.5, 0.78} and clusterAOI {0.0, 0.21, 1.1, 0.91} respectively. Diameter has no optimal value yet but Colour converged at iteration 3 at 0.78 (optimal value 1.5) and clusterAOI at 0.91 (optimal value 1.1). Although Diameter monotonically increases, further generalisation stops at iteration 3 at 1.0 (Diameter) and at 0.91(clusterAOI). This prevents overgeneralisation of both attributes (local case) and clusterAOI (global case). Further, run-time performance is improved. Lemma 1 helps to formulate a theorem based on these observations.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Input: Dataset D with attributes Ai; Concept hierarchies Hi, Global threshold t
Output: A compact table T, Kullback measure KL, Cluster measure I$^{T}_{g}$
BEGIN
Step 1. Get each Ai, find attribute significance and new local thresholds, iter←1
Step 2. Process attributes
L2.1    stillInteresting=true
L2.2    convergenceValues [Ai]= false
L2.3    While (stillInteresting) // check Global interestingness
L2.4    For each Ai in D
L2.5    attrConv= convergenceValues (Ai)
L2.6    if ( not(attrConv))
L2.7    D←processAttribute(D, Hi, Ai)
L2.8    D←mergeData(D)
L2.9    attrHeur[i]←computeHeuristics(interC,intraC, I$^{i}_{L}$) // [16]
L2.10    hashStore=IterationObject(attrHeur[i], iter)
L2.11    harm_total←0
L2.12    I$^{i}_{g}$←0
L2.13    For each Ai //check attribute convergence
L2.14    if(iter&gt;0)
L2.15    attrConv←isAttribConv(iter, i, hashStore)
L2.16    if(attConv= true)// Check Local interestingness
L2.17    convergenceValues(i)←attrConv
L2.18    I$^{i}_{g}$ ← computeGlobal_I(hashStore (iter, Ai)) // eqn (5)
L2.19    harm_total← harm_total +I$^{i}_{g}$
L2.20    I$^{D}_{g}$=harm_total/m //eqn (6)
L2.21    setHarmValues(I$^{D}_{g}$ ))
L2.22    stillInteresting←isInteresting(getHarmValues())
L2.23    iter←iter+1
Step 3. Generate final table
L3.1    D←merge and Copy(D)
L3.2    D←generaliseLeaf(D)
L3.3    T←topKRules(D, newThreshold)
L3.4    KL←KullbackMeasure(T)
L3.5    I$^{T}_{g}$←TableClusterQuality(T) //eqn (7)
L3.6    Output(T, KL, I$^{T}_{g}$)
END
</div>

Table 6  
Clusters for Diameter and Colour at generalisation iteration 1.

<table><tr><td>Diameter</td><td>IntraC</td><td>InterC</td><td> $I_{L}^{i}$ </td><td> $I_{g}^{i}$  (Eq. (5))</td></tr><tr><td>[2,7,8,16] → small</td><td></td><td>0.0</td><td>0.0</td><td></td></tr><tr><td>[25,34,28] → medium</td><td>0.143</td><td></td><td></td><td></td></tr><tr><td>Total</td><td></td><td></td><td></td><td>0.143</td></tr><tr><td>Colour [red, orange, red] → reddish [blue, violet] → bluish [yellow, green] → yellowish</td><td>0.167</td><td>1.0</td><td>0.0</td><td></td></tr><tr><td>Total</td><td></td><td></td><td></td><td>0.286</td></tr><tr><td></td><td colspan="3">Average H. Mean (Eq. (6))</td><td>0.429/2 = 0.215</td></tr></table>

clusterAOI and AOI <sup>fi</sup>nal table comparisons.

<table><tr><td></td><td>Diameter</td><td>Colour</td><td>Count</td><td> $I^T_g$  (Eq. (7))</td><td>KL</td></tr><tr><td rowspan="3">clusterAOI</td><td>Medium</td><td>Non-dark</td><td>3</td><td>4.61</td><td>1.56</td></tr><tr><td>Small</td><td>Dark</td><td>2</td><td></td><td></td></tr><tr><td>Small</td><td>Non-dark</td><td>2</td><td></td><td></td></tr><tr><td rowspan="2">AOI</td><td>ANY</td><td>Non-dark</td><td>5</td><td>1.34</td><td>0.86</td></tr><tr><td>ANY</td><td>Dark</td><td>2</td><td></td><td></td></tr></table>

## Theorem 1. Global interestingness

Given attributes $\{ A _ { i } \} , 1 \le i \le$ m of table T, each attribute has a local interestingness value v<sup>k</sup> for some iteration $k > 0$ , global interestingness $\nu _ { g } ^ { k + 1 } \mathrm { i s } \mathrm { t h e } ( k + 1 ) \mathrm { t h }$ value computed when the maximum value of aggregated local interestingness values in the kth iteration has been computed. The aggregated maximum value in $\boldsymbol { \nu } _ { g } ^ { k } = \operatorname* { m a x } \{ \cup I _ { g } ^ { T } ( \boldsymbol { \nu } _ { 1 } ^ { k } , \boldsymbol { \nu } _ { 2 } ^ { k } , . . . , \boldsymbol { \nu } _ { m } ^ { k } ) \}$ and global interestingness is reached when $\nu _ { g } ^ { k } \geq \nu _ { g } ^ { k } ^ { + 1 } ~ ( \mathrm { E q . ~ \rho ( 7 ) } )$ Section 5.3). See Appendix C for proof.

To reiterate, we calculate attribute interestingness (Eq. (3), [16]) of a value c by a distance-based linear metric, $I _ { c } : [ 0 , 1 ] \to [ 0 , 1 ] .$ . For example, a leaf concept $x _ { i } \in A _ { i }$ has interestingness value $\begin{array} { r } { I x _ { i } = 1 - \frac { d ( x _ { i } , ^ { * } A N Y ^ { * } ) } { d e p t h ( ^ { * } A N Y ^ { * } ) } = 0 . } \end{array}$ Similarly, $I _ { c = A N Y } = 1 - 0 = 1$ , a complement of the leaf concept mapping. This function is unreliable as “ANY” has maximum value 1.

$$
I _ {c} = 1 - \frac {d (c , “ A N Y ”)}{d e p t h (“ A N Y ”)}, c \neq “ A N Y ”.\tag{3}
$$

clusterAOI and AOI results (50 K Census-income dataset1 [19])

<table><tr><td rowspan="2">G.Thr</td><td colspan="2">KL</td><td colspan="2"> $I^T_g$ </td><td colspan="2">Runtime (×10 s)</td></tr><tr><td>AOI</td><td>clusterAOI</td><td>AOI</td><td>clusterAOI</td><td>AOI</td><td>clusterAOI</td></tr><tr><td>1</td><td>0.00</td><td>0.97</td><td>0.00</td><td>22.36</td><td>26.20</td><td>20.50</td></tr><tr><td>2</td><td>0.86</td><td>1.54</td><td>5.80</td><td>10.22</td><td>26.20</td><td>20.50</td></tr><tr><td>3</td><td>1.46</td><td>1.94</td><td>0.002</td><td>13.19</td><td>26.20</td><td>21.00</td></tr><tr><td>4</td><td>1.46</td><td>2.24</td><td>0.018</td><td>23.10</td><td>26.20</td><td>21.00</td></tr><tr><td>5</td><td>2.26</td><td>1.83</td><td>0.0029</td><td>25.00</td><td>26.00</td><td>21.00</td></tr><tr><td>6</td><td>2.26</td><td>1.83</td><td>0.0029</td><td>25.60</td><td>26.00</td><td>21.00</td></tr><tr><td>7</td><td>2.26</td><td>1.83</td><td>26.00</td><td>25.60</td><td>26.00</td><td>21.00</td></tr><tr><td>8</td><td>2.94</td><td>1.83</td><td>26.00</td><td>25.60</td><td>26.00</td><td>21.00</td></tr><tr><td>9</td><td>2.94</td><td>1.83</td><td>26.00</td><td>25.60</td><td>26.00</td><td>21.00</td></tr><tr><td>10</td><td>2.94</td><td>1.83</td><td>26.00</td><td>25.60</td><td>26.00</td><td>21.00</td></tr><tr><td>Avg.</td><td colspan="2"># times = 0.91</td><td colspan="2"># times = 2.65</td><td colspan="2"># times = 1.25</td></tr></table>

![](/api/attachments/35BDM6JA/fulltext/images/875e98c616c23af6222c146b674f2cfcd38f0c91d41644038a5e10893c17da5f.jpg)  
(a) KL

![](/api/attachments/35BDM6JA/fulltext/images/2d85302ed4bed7faf4405e915b934b78cfcc5b2b8c094c63a5d40ce405ef3761.jpg)  
Fig. 3. 50 K census-income: (a) KL. (b) Global interestingness.  
(b) Global Interestingness

Eq. (3) satis<sup>fi</sup>es the following three axioms for any given universal set X:

Axiom 1. Boundary conditions: $I _ { c } ( \mu _ { \infty } = 0 ) = 1 \mathrm { a n d } I _ { c } ( \mu _ { x } = 1 ) = 0 .$

Axiom 2. Monoticity: $I _ { c } ( a ) > I _ { c } ( b )$ if a b b. For example, given two values $x _ { 1 } = { ^ { \ast } r e d ^ { \ast } } \prec x _ { 2 } = { ^ { \ast } A N Y ^ { \ast } } , a = \mu _ { x 1 } = 0 , b = \mu _ { x 2 } = 1$ , then $I _ { r e d } ( 0 ) = 1 > I _ { A N Y } ( 1 ) = 0 .$ . This metric is unreliable for interestingness: c such that $" r e d " < c < " A N Y$ ,and $\mathrm { i f } \mu _ { c } = 0 . 5$ then $I _ { c } ( 0 . 5 ) > I _ { c } = _ { A N Y } ( 1 )$ and $I _ { c = r e d } ( 0 ) > I _ { c } ( 0 . 5 )$ . This violates Proposition 1 and Lemma 1. A nonlinear metric (see Eq. (4)) may be more suitable.

## Axiom 3. Involutive: It is easily shown that $I _ { c } ( I _ { c } ( 0 ) ) = 0 \mathrm { o r } I _ { c } ( I _ { c } ( 1 ) ) = 1$

We infer that interestingness is non-linearly distributed between leaf and root nodes, so a probability density function given by Eq. (4) (input from Eq. (3)) determines interestingness of a value:

$$
H (I _ {c}) = \frac {1}{\sigma \sqrt {2 \pi}} e ^ {- (x _ {i} - \mu) ^ {2} / (2 \sigma^ {2})}\tag{4}
$$

where $0 \leq I _ { c } \leq 1$ with mean and variance values $( \mu , \sigma ) , \forall c \in B _ { i } .$

Case Study (6). Using Table 1, mean $\mu = 0 . 5 2 4 ,$ , variance $\sigma = 0 . 0 6 9$ for Colour and $\mu = 0 . 6 2 5 , \sigma = 0 . 0 6 2 5$ for Diameter. Observe that Eq. (4) gives $H ( I _ { r e d } ) = H ( 0 ) = 1 . 4 8 ^ { \ast } 1 0 ^ { - \dot { 1 } 2 }$ while $H ( I _ { A N Y } ) = H ( 1 ) = 0 . 0 2 2 \ ^ { * }$ $\bar { 1 } 0 ^ { - 1 2 } .$ . So interestingness of interior node “reddish”, $I _ { r e d d i s h } = 0 . 3 3 ,$ $\begin{array} { r } { H ( I _ { r e d d i s h } ) = 0 . 1 2 4 , } \end{array}$ and any cluster $C \ i s \ \sum _ { i = 1 } ^ { n } H ( c _ { i } )$ . Note $H ( I _ { r e d d i s h } ) \geq$ $H ( I _ { r e d } ) \geq H ( I _ { A N Y } )$ <sup>¼</sup>, thus confirming that root and leaf nodes are less interesting than interior nodes.

## 5.2. Generalisation process

For each attribute we <sup>fi</sup>nd and generalise clusters of values that share nearest common parents [16] and compute interestingness heuristics (L2.7–L2.10, Fig. 2, see Tables 3–6). Generalised clusters are stored in a hash table. As clusterAOI may not generalise all clusters, we use an approach in section 5.4 based on Axiom 2. To derive interesting patterns we measure cluster tightness (Eq. (5)). A general theory of monotonically non-increasing tightness functions $\tau _ { n }$ that measure the number of attribute values in clusters is given in [17] i.e. if $c < c ^ { \prime } , \tau _ { n } ( c ) \succ \tau _ { n } ( c ^ { \prime } )$ . We require $\tau _ { n } ( c ^ { \prime } ) \succ \tau _ { n } ( c )$ to hold for $c \prec c ^ { \prime }$ , where the tightness function increases monotonically to an optimal value. Following similar generalisation approach to AOI, the output stores new parent clusters; similarity, tightness and CQ heuristics (L2.9, Fig. 2), aggregated using Eq. (5). The <sup>fi</sup>nal generalised table is produced in Step 3 (L3.6, Fig. 2). In Table 2, cluster {2, 7, 8, 16} is generalised to its nearest common parent “small” because $4 > L . T h r _ { d i a m e t e r } = 3$ . This guarantees conservative generalisation. clusterAOI uses this step to produce better patterns than AOI.

## 5.3. clusterAOI algorithm

Fig. 2 shows clusterAOI; Step 1 performs pre-clusterAOI.

Let $C _ { i j }$ be cluster j for a group of similar property values of $A _ { i } ,$ $1 \leq j \leq n ,$ for n tuples with clusters $C = \{ \bigcup _ { j = 1 } ^ { k } C _ { i j } \}$ e.g. equal distances from the root node and the same parents. From Eq. (5) (global harmonic mean), we get an attribute's global interesting value by cluster similarity (IntraC), tightness (InterC) and local interestingness $( I _ { L } ^ { i } ) , ( \mathrm { I } = ( \mathrm { I } _ { 1 } , \mathrm { I } _ { 2 } , \mathrm { I } _ { 3 } )$ respectively).<sup>3</sup>

$$
I _ {g} ^ {i} (I) = \frac {n}{\sum_ {i = 1} ^ {n} 1 / I _ {i}}\tag{5}
$$

$$
I _ {g} ^ {D} = \frac {\sum_ {i = 1} ^ {m} I _ {g} ^ {i}}{m}\tag{6}
$$

$$
I _ {g} ^ {T} = \sum_ {i = 1} ^ {m} I _ {L} ^ {i}.\tag{7}
$$

After computing $I _ { g } ^ { i } ,$ we store the global interestingness values $I _ { g } ^ { D }$ for all table attributes (Eq. (6)). To further generalise (or avoiding generalisation) an attribute, the latest and previous $I _ { g } ^ { i }$ values are compared to determine the next step. Global interestingness values are compared in the same way therefore avoiding overgeneralisation. The cluster quality of table T i.e. $I _ { g , } ^ { T }$ is a summation of all local $I _ { L } ^ { i }$ values (Eq. (7)).

$$
\overline {{^ {3} \text { Defined as}}} I _ {1} (C) = \frac {\alpha}{\underset {i = 1} {\overset {k} {\cup}} C _ {i j} |}, \alpha = 1, I _ {2} (C) = \sum_ {i = 1} ^ {k} | C _ {i j} | - \underset {i = 1} {\overset {k} {\cup}} C _ {i j} |, I _ {3} (C) = \sum_ {i = 1} ^ {n} H (c _ {i}).
$$

![](/api/attachments/35BDM6JA/fulltext/images/6acf28f766b96a23e9a2746c5b8817ecbb48152b4fe64410ca128fb5330aa3fe.jpg)  
(a) Runtime 50K

![](/api/attachments/35BDM6JA/fulltext/images/752da40de7fc563e5138fbd79d6cd7cbfaa7edd89cb5d40592ac0af454de475a.jpg)  
(b) Algorithm convergence  
Fig. 4. (a) Runtime 50 K (b) algorithm convergence.

Step 2 sets global interestingness, processes each attribute, merges resulting values and stores $I _ { L } ^ { i }$ values (Eq. (5)). Each iteration makes parent clusters per attribute, generalises and processes them (L2.7, Fig. 2). computeHeuristics() (L2.9) computes interestingness heuristics. We check each attribute's local (L2.15) and global convergence (L2.22) using the heuristics. Global interestingness is checked by the global harmonic mean of all local interestingness values (L2.20, Eq. (6)). Step 3 merges the table rows into a new smaller prime table.

Case Study (7). Table 6 shows the initial clusters generated using a global threshold $G . T h r = 2 .$ . Global harmonic means are stored for the entire generalisation process as sets of vector values. The first iteration's global harmonic mean is 0.215. Local interestingness values for Diameter were [0.0,0.143,0.66,1.03] and for Colour [0.0,0.286,1.5,0.78]. Eq. (5) gives the second local harmonic mean of Colour as $\frac { 2 } { \left( ^ { 1 } / _ { 0 . 1 6 7 } \right) + \left( ^ { 1 } / _ { 1 } \right) } = 0 . 2 8 6$ . Local cluster interestingness values $( \boldsymbol { I } _ { L } ^ { i } )$ are zero as we only have leaf concepts. Further, the algorithm only iterates 3 times up to global harmonic value 0.907 in the list [0.0, 0.215, 1.08, 0.907,…] and generalisation stops. Colour essentially converges at iteration 3 (as $1 . 5 > 0 . 7 8 )$ . As Diameter has not converged yet (since $0 . 6 6 < 1 . 3 3 )$ , generalisation should continue after iteration 3. Consequently, as global algorithm convergence occurs at iteration 3, no further generalisation of Diameter occurs, preventing overgeneralisation and further iterative steps.

The complexity analysis of clusterAOI is discussed in Section 6.4.

![](/api/attachments/35BDM6JA/fulltext/images/da21c97f4a0321e1e11a7bfe96a34266ca767c403b0c2496b9cf133df50e4376.jpg)  
Fig. 5. Convergence of age.

## 5.4. Post-clusterAOI interestingness

Case study (8). Table 7 compares outputs: each row represents a rule in descending order of tuple numbers. clusterAOI recalculates thresholds and gives three rules containing interior concepts while AOI overgeneralises Diameter to $\ " A N Y ^ { \prime }$ and gives two rules. clusterAOI is superior to AOI: global interestingness $( I _ { g } ^ { T } ,$ 5th column) is 3 times and KL is 1.8 times better.

In clusterAOI, ungeneralisable attribute clusters may appear as leaf concepts in the output [16]. To improve overall interestingness, generaliseLeaf() (L3.2, Fig. 2) searches for an optimal generalisation point for any given leaf concept. Following Axiom 2, there is an interior level l (or group of interior parent concept values at this level) which is more interesting than those at levels l − 1 and l + 1. For performance, we deterministically <sup>fi</sup>nd the most “interior” level of a concept hierarchy, the ‘median’, and generalise the leaf to this level (Proposition 1 and Fig. 1). (depthOfHierarchy)/2 generalisation steps are used for an even number of levels; one more for an odd number.

## 6. Experimental analysis

Experiments have been performed on three datasets: two Census income datasets and Cancer Wisconsin [19] (See Appendix H). We analysed results in terms of KL measure, interestingness and runtime. Section 6.1 analyses a small census income dataset1 (50 K tuples, 3 attributes), Section 6.2 the Cancer Wisconsin dataset (700 tuples, 4 attributes) and Section 6.3 a larger census income dataset2 (200 K tuples, 6 attributes). Experiments were run 5 times to obtain average results on an Intel (R) Pentium (R) Dual 2 GHz processor with 2 GB RAM.

![](/api/attachments/35BDM6JA/fulltext/images/b1be75e9da570a15c6be289cf0cf0955e2b23b6b6e2cab0e62392fa17b692b1b.jpg)  
Fig. 6. Convergence of education.

Fig. 8. KL: 200 K.  
![](/api/attachments/35BDM6JA/fulltext/images/bb196a5c8877e7457bd50b5387b5537f5a4acce8b084e560fc0fd3b0bb876913.jpg)  
Fig. 7. Convergence for NumWorkedFor.

## 6.1. Census-income dataset1 (50 K tuples, 3 attributes)

Table 8 compares performance with global thresholds from 1 to 10, with concept hierarchies given in Appendix F. Threshold 1 guarantees excessive generalisation in traditional AOI while higher thresholds do the opposite. For clusterAOI, mean and variance were calculated and their signi<sup>fi</sup>cance was evaluated as follows: sig(age) = 18.87, sig(educ) = 9.99 and sig(numWorked) = 1.63, and local thresholds recalculated.

Comparing global interestingness $( I _ { g } ^ { T }$ values) in Table 8 (see also Fig. 3(b)), clusterAOI is 2.65 times better on average. For thresholds 1 to 4, often a desirable level to set in AOI, clusterAOI's interestingness is 12 times better, meaning it generates more interesting patterns. Higher thresholds (7 and over) appear to not differentiate interestingness between the two algorithms on this dataset. Unsurprisingly, threshold 1 gives interestingness of 22.36 and clusterAOI recalculated L.Thr as 2 and produced two rules with values (aged, average education, few) and (aged, basic education, few); in contrast, AOI produced one overgeneralised rule with values (ANY, ANY, ANY).

The KL measure for clusterAOI is on average 1.76 times better for thresholds 1 to 4, and 0.91 times better for thresholds 1 to 10 (Fig. 3(a)). The results indicate that clusterAOI generalises better for smaller thresholds (better distribution or divergence of output patterns) than for larger ones. clusterAOI is also 1.25 times faster (Fig. 4(a), Table 8). Generally, for smaller thresholds, more clustering, generalisation and merging is done.

Table 9  
clusterAOI and AOI results (Cancer Wisconsin dataset [19]).

<table><tr><td rowspan="2">G.Thr</td><td colspan="2">KL</td><td colspan="2"> $I^T_g$ </td><td colspan="2">Runtime (×10 s)</td></tr><tr><td>AOI</td><td>clusterAOI</td><td>AOI</td><td>clusterAOI</td><td>AOI</td><td>clusterAOI</td></tr><tr><td>1</td><td>0.0</td><td>0.66</td><td>0.0</td><td>23.2</td><td>18.4</td><td>16.40</td></tr><tr><td>2</td><td>0.63</td><td>1.08</td><td>17.4</td><td>34.6</td><td>17.0</td><td>16.00</td></tr><tr><td>3</td><td>1.08</td><td>1.36</td><td>23.0</td><td>46.4</td><td>17.0</td><td>16.00</td></tr><tr><td>4</td><td>1.08</td><td>1.36</td><td>0.75</td><td>46.4</td><td>19.0</td><td>16.00</td></tr><tr><td>5</td><td>1.44</td><td>1.36</td><td>0.90</td><td>46.0</td><td>19.0</td><td>16.00</td></tr><tr><td>6</td><td>1.59</td><td>1.36</td><td>1.06</td><td>46.4</td><td>20.0</td><td>15.60</td></tr><tr><td>7</td><td>1.71</td><td>1.36</td><td>1.21</td><td>46.3</td><td>21.0</td><td>15.60</td></tr><tr><td>8</td><td>1.83</td><td>1.36</td><td>1.36</td><td>46.4</td><td>20.0</td><td>16.00</td></tr><tr><td>9</td><td>1.92</td><td>1.36</td><td>1.51</td><td>46.4</td><td>21.0</td><td>16.00</td></tr><tr><td>10</td><td>2.01</td><td>1.36</td><td>31.88</td><td>46.4</td><td>27.0</td><td>16.00</td></tr><tr><td>Avg.</td><td colspan="2"># times = 0.94</td><td colspan="2"># times = 5.42</td><td colspan="2"># times = 1.24</td></tr></table>

Table 10  
clusterAOI and AOI results (Census-income dataset2 200 K tuples).

<table><tr><td rowspan="2">G.Thr</td><td colspan="2">KL</td><td colspan="2"> $I^T_g$ </td><td colspan="2">Runtime (×10 s)</td></tr><tr><td>AOI</td><td>clusterAOI</td><td>AOI</td><td>clusterAOI</td><td>AOI</td><td>clusterAOI</td></tr><tr><td>1</td><td>0.00</td><td>1.53</td><td>0.00</td><td>49.44</td><td>96.00</td><td>32.00</td></tr><tr><td>2</td><td>0.92</td><td>178</td><td>0.00</td><td>40.60</td><td>68.00</td><td>26.00</td></tr><tr><td>3</td><td>1.86</td><td>2.11</td><td>9.07</td><td>56.00</td><td>59.00</td><td>26.00</td></tr><tr><td>4</td><td>2.31</td><td>2.35</td><td>6.84</td><td>71.56</td><td>57.00</td><td>26.00</td></tr><tr><td>5</td><td>2.55</td><td>2.50</td><td>8.21</td><td>91.00</td><td>57.00</td><td>26.00</td></tr><tr><td>6</td><td>2.63</td><td>2.57</td><td>14.55</td><td>113.75</td><td>57.00</td><td>26.00</td></tr><tr><td>7</td><td>2.89</td><td>2.57</td><td>42.11</td><td>140.00</td><td>54.00</td><td>24.00</td></tr><tr><td>8</td><td>3.00</td><td>2.67</td><td>47.80</td><td>140.00</td><td>54.00</td><td>26.00</td></tr><tr><td>9</td><td>3.14</td><td>2.71</td><td>53.50</td><td>152.00</td><td>54,000</td><td>26.00</td></tr><tr><td>10</td><td>3.27</td><td>2.74</td><td>59.20</td><td>165.80</td><td>54.00</td><td>26.00</td></tr><tr><td>Avg.</td><td colspan="2"># times = 1.04</td><td colspan="2"># times = 4.20</td><td colspan="2"># times = 2.31</td></tr></table>

Fig. 4(b) shows how clusterAOI reaches a global optimal value $\nu _ { g } ^ { k } = 4 . 5$ at iteration 2 before <sup>fi</sup>nally converging at iteration 3 at $\nu _ { g } ^ { \mathcal { \bar { k } } + 1 } = 1 . 5 7$ . Each attribute also has a local optimal value $\boldsymbol { \nu } ^ { k }$ before stopping at the next iteration (See Figs. 5–7). Signi<sup>fi</sup>cance values were calculated as: age (18.87), education (9.98) and NumWorkedFor ( 1.63) meaning that age has the smallest local threshold and should be generalised further.

Note their convergence graphs in Figs. 5, 6 and 7 are similar to the clusterAOI convergence pattern in Fig. 4(b).

## 6.2. Cancer Wisconsin dataset (700 tuples, 4 attributes)

Section 1 introduced this dataset: values distribution (with concept hierarchy and distinct attribute values given in Appendix G) is narrow with a low value for KL. Each attribute has similar signi<sup>fi</sup>cance values other than mitoses: sig(cellSize) = 5.04, sig(bareNuclei) = 5.04, sig(normalNuclei) = 5.04 and sig(mitoses) = 4.89. As seen in Table 1, mitoses is not overgeneralised by clusterAOI even with the lowest signi<sup>fi</sup>cance, unlike by AOI. Convergence of the attributes follows a similar pattern to Figs. 5, 6 and 7. Table 9 shows clusterAOI is better than AOI in terms of global interestingness $( I _ { g } ^ { T }$ values): 5.42 times better on average; KL for small thresholds (1 to 4): 1.5 times, overall it is 0.94 times better on average; and interestingness and runtime: 5.84 and 1.24 times respectively.

![](/api/attachments/35BDM6JA/fulltext/images/7fc308122677dbe5f2834cb7d5d06f2d5b6a9fdcf36008e000c83bb6d9c349e1.jpg)

![](/api/attachments/35BDM6JA/fulltext/images/4919cb9af337fc4ebc880b02dfa8554823094057b734645b1d9063f48178bcb4.jpg)  
Fig. 9. Global interestingness: 200 K.

## 6.3. Census-income dataset2 (200 K tuples, 6 attributes)

Signi<sup>fi</sup>cant values and distinct values $( d i s t ( A _ { i } ) )$ were calculated as follows: sig(age) = 27.94, dist(age) = 91; sig(education) = 8.01, dist $( { \mathsf { e d u c a t i o n } } ) = 1 7 ;$ sig(det ailHHold) = 64.20,dist(detailedHHold) = 38, sig(majIndCode) = 98,dist(majIndCode) = 24, sig(instWeight) = $- 4 . 4 , \mathrm { d i s t } ( \mathrm { i n s t W e i g h t } ) = 4$ and $s i g ( n u m W o r k e d F o r ) = - 3 . 6 ,$ dist (numWorkedFor) = 7. Global thresholds were set from 1 to 10 and performance results are shown in Table 10. clusterAOI generates patterns of 4 times more interest (Table 10, Column $I _ { g } ^ { T }$ and Fig. 9) and 1.04 times better in terms of pattern divergence (KL in Fig. 8) than AOI. However, when averaging for thresholds 1 to 4 as previously, clusterAOI generates patterns that are 14 times more interesting; KL for thresholds 1 to 4 is about 1.5 times better than AOI. KL (value divergence) for clusterAOI increases with more data. The greater the divergence, the more interesting patterns are produced (Fig. 8) i.e. clusterAOI shows larger interestingness values (Fig. 9). Hence, small thresholds may be used for many purposes e.g. readability, interpretability etc. clusterAOI is about twice as fast (Table 10, Fig. 10); with lower thresholds (e.g. 1 to 4), and overall average run-time is about three times better. Note that for attribute signi<sup>fi</sup>cant values lower than zero (e.g. instance weight), convergence $\Breve { \boldsymbol { \nu } } ^ { k + 1 } = 1 . 9 8$ and optimal values $\nu ^ { k } = 1 . 9 9$ are close.

This is similar to the experiment in Section 6.1 with attribute NumWorkedFor (Fig. 7). Other positive signi<sup>fi</sup>cant values follow a nearly normal probability distribution (Fig. 6, Education attribute) similar to clusterAOI convergence at iteration 3 (Fig. 11). Attribute convergence obtained similar patterns to those of Sections 6.1 and

![](/api/attachments/35BDM6JA/fulltext/images/ea70cfb63880e6a9edd77b9b048f5be1777645e3c21cf6531a49219cae29d8d4.jpg)  
Fig. 10. Runtime: 200 K.

![](/api/attachments/35BDM6JA/fulltext/images/2564e4ae44700886ddcae3253744a1b7f555d0569781d4c04dbb62a1876450dc.jpg)  
Fig. 11. clusterAOI convergence: 200 K.

6.2. Moreover, clusterAOI also follows a nearly normal probability showing the necessity of searching for optimal turning points (interestingness values) during generalisation (see Figs. 4(b) and 11). The same argument holds for positively signi<sup>fi</sup>cant attributes. clusterAOI and AOI are also compared in terms of NOT-ANY/ANY values.

Using a global threshold of 3, clusterAOI on average obtained 100% NOT-ANY values (meaning 0% “ANY” values), across all datasets (see Table 11). In contrast, AOI gave 41% NOT-ANY values. Clearly clusterAOI derives more useful, meaningful and informative patterns than those obtained by AOI. These are consistent with Table 1 results. The top 4 rules from clusterAOI applied to Census dataset2 are given in Table 12. Notable differences lie in the “age” groups, “education” and $" \mathrm { C o u n t } "$ . Most surprising is the rule (Row 4) showing that 6% are older people 41–60 with “HighSchool” education, in contrast to Row 3 showing that 8% aged 10–20 are fairly educated and not married. Overall, the general population is in employment and healthy but remarkable differences exist in education.

In contrast, AOI generated 2 rules with “majIndCode” having only two NOT-ANY values “public”, “not-public”, which provided little meaning.

In summary, the results show that clusterAOI when compared to AOI:

1. is superior in terms of runtime, interestingness and divergence (KL);

2. does not <sup>fl</sup>uctuate between small and large datasets;

3. generates higher interestingness values, up to 13 times, with lower thresholds (G.Thr 1 to 5);

4. has a run-time complexity of approximately half (Section 6.4);

5. has better KL divergence, 1.5 times for smaller thresholds (up to 4)

Table 11  
Comparing NOT-ANY and ANY values $( G . T h r = 3 ) $

<table><tr><td rowspan="2">Dataset</td><td>AOI</td><td>AOI</td><td>clusterAOI</td><td>clusterAOI</td></tr><tr><td>ANY</td><td>NOT-ANY</td><td>ANY</td><td>NOT-ANY</td></tr><tr><td>Census-income 2</td><td>15</td><td>9</td><td>0</td><td>30</td></tr><tr><td>Cancer Wisconsin</td><td>8</td><td>8</td><td>0</td><td>16</td></tr><tr><td>Census-income 1</td><td>29</td><td>20</td><td>0</td><td>12</td></tr><tr><td>Avg % ANY</td><td>59%</td><td></td><td>0%</td><td></td></tr><tr><td>Avg % NOT-ANY</td><td>41%</td><td></td><td>100%</td><td></td></tr></table>

clusterAOI rules: 200 K Census-income Dataset2, G.Thr = 3.

<table><tr><td colspan="7">Attributes</td></tr><tr><td>Age</td><td>Education</td><td>majIndCode</td><td>detHHold</td><td>instWeight</td><td>numWorkedFor</td><td>Count</td></tr><tr><td>21–40</td><td>Basic Educ</td><td>PersonalServ</td><td>NotMarrNonsub</td><td>lowRisk</td><td>Few</td><td>50,482</td></tr><tr><td>10–20</td><td>HighSchool</td><td>PersonalServ</td><td>NotMarrNonsub</td><td>lowRisk</td><td>Few</td><td>35,721</td></tr><tr><td>10–20</td><td>FairlyEduc</td><td>PersonalServ</td><td>NotMarrNonsub</td><td>lowrisk</td><td>Few</td><td>16,506</td></tr><tr><td>41–60</td><td>HighSchool</td><td>Manufact</td><td>HouseOwner</td><td>lowRisk</td><td>Few</td><td>12,122</td></tr></table>

## 6.4. Algorithm space and time complexity analysis

AOI has order complexities ranging from O(np) [8], O(nlogp) [9] to O(n) ([4,2]) for n input tuples, p generalised tuples and $p \leq \log n .$

Lemma 2. clusterAOI's time complexity is O(np) with space complexity of $2 * O ( n ) o r ( O ( n p ) + O ( n ) )$ , for n input tuples, p tuples in the prime table and child concept values stored in their parent cluster hash tables (see Appendix D for proof).

clusterAOI has better runtime than AOI because it scans the input data once and creates parent clusters during input (Fig. 2: Steps 1, 2). Figs. 4a and 10 show the differences in runtime performance.

## 7. Conclusions

A heuristic algorithm, clusterAOI, is introduced that, when compared to AOI, improves expressiveness and interestingness, divergence and distribution of concepts in the output, and runtime. Experimental results show improvement on average of up to 1.5 times on KL, 4 times on interestingness and 2 times on runtime compared to AOI. The <sup>fi</sup>nal output has better pattern distribution and is more expressive and meaningful than from AOI. clusterAOI determines attribute signi<sup>fi</sup>cance, preserves attribute interestingness and evaluates the output. clusterAOI has similar order complexity to established algorithms $[ 2 , 4 ] , { \cal O } ( n p )$ , and storage requirements, $2 * O ( n p )$ . Our approach is applicable to generalisation algorithms using concept hierarchies [12]. Further work will investigate heuristic optimisation to better exploit the search space.

## Acknowledgements

Thanks to Prof Howard J. Hamilton (University of Regina) for technical input.

## Appendix A. Proof of Proposition 1

Proof. A generalisation function is <sup>fi</sup>nite and bounded by leaf and root nodes, [a, b], respectively (Fig. 1). Hence, $\exists ~ o _ { i } \in H _ { i } ,$ , with property $a \prec o _ { i } \prec b$ for some partial order. As leaf and root node values are uninteresting [6], then for any interestingness function $I , I ( a ) < I ( o _ { i } )$ and $I ( o _ { i } ) > I ( b )$ if a is a leaf and b is a root concept. Thus $o _ { i }$ is an interesting interior concept. {end proof}

## Appendix B. Proof of Lemma 1

Proof. The proof is a consequence of Proposition 1 and case study (4). Assuming initial attribute interestingness as $\alpha \geq 0 ,$ ∃ iteration k where clusters with heuristic values $X ^ { k }$ give a value greater than α i.e. $I _ { k } ^ { i } ( X ^ { k } ) = \nu ^ { k } > \alpha , \nu ^ { k } { \in } \Re ^ { + }$ . Using [16] and stating that further generalisation reduces the interestingness value at a (k + 1)th iteration, then $I _ { k + 1 } ^ { i } ( X ^ { k + 1 } ) = b = \nu ^ { k + 1 } \leq \nu ^ { k }$ . Thus interestingness I increases in interval [α,v<sup>k</sup>] and decreases in interval $[ \nu ^ { k + 1 } , \ldots ] .$ . {end proof}.

## Appendix C. Proof of Theorem 1

Proof. Following De<sup>fi</sup>nition 3, let the aggregate harmonic values (local interestingness values) be $\{ \nu _ { 1 } ^ { k } . . . , \nu _ { m } ^ { k } \} , 1 \leq i \leq$ m for m attributes at iteration k. Generalisation interestingness functions [16] and heuristic aggregation functions are monotonically increasing [17] up to some optimal iteration $k ,$ where $\boldsymbol { \nu } _ { g } ^ { k } = I _ { g } ^ { T } ( \nu _ { 1 } ^ { k } , \nu _ { 2 , \ldots , \nu _ { m } ^ { k } ) } ^ { \bar { k } }$ . After further generalisation, iteration k + 1 has value $\begin{array} { r } {  { \boldsymbol { \nu } } _ { g } ^ { k + 1 } =  { \boldsymbol { I } } _ { g } ^ { T } (  { \boldsymbol \nu } _ { 1 } ^ { k + 1 } , . . . ,  { \boldsymbol \nu } _ { m } ^ { k + 1 } ) \ge  { \boldsymbol \nu } _ { g } ^ { k + 1 } } \end{array}$ , reaching a global interestingness value, else generalisation continues to iteration k + 2 and so on {end proof}.

## Appendix D. Proof of Lemma 2

Proof. Time complexity: Let n = input size, p = prime table size and m = number of attributes. AOI [9] reads the input, generalises each attribute, sorts the table in O(n log n) time before merging the prime table, giving complexity O(np) + O(n log n) = O(n log n), $p < < n .$ . The total time complexity O(n log $n ) \approx { \cal O } ( n$ log $n ) + O ( p )$ . At input, clusterAOI clusters values $C _ { j i }$ for each A on-the-<sup>fl</sup>y and stores them under a parent value in a hash table. Given a jth cluster as $C _ { j i }$ for k parents, the time complexity is $O ( k | C _ { j i } | )$ . For h clusters and global threshold $G . T h r = g > 0 ,$ , the time to store concepts is bound by $O ( k * m * h * g * \sum | C _ { j i } | .$ Note that $m ^ { * } \sum | C i _ { j } | = n , k \ll \mathrm { n } , h \ll n$ and $g \ll n$ in the worst case if each ${ \mathsf { C } } _ { j i }$ is generalised $j = 1 , . . . , h .$ . Thus time complexity is O(n). Further generalisation and insertion in a prime table is O(np). Applying a merge sort to the prime table for a <sup>fi</sup>nal table of size q, complexity is O (plogp) ∗ O(q) or ${ \cal O } ( p q ) \approx { \cal O } ( p )$ . Thus total is $O ( n p ) + O ( p )$ or at most O(np) in the worst case (or O(n) in the best case).

Space complexity: Intuitively, we need $O ( n ) + O ( n )$ to store initial input and attribute child clusters (unless we only store child leaf index positions [2]). Adding prime and <sup>fi</sup>nal table sizes, O(p) and $O ( q )$ gives $2 * O ( n p )$ ). {end proof}

## Appendix E. Table of notation

<table><tr><td>Term</td><td>Meaning</td></tr><tr><td> $Sig, e_i, \nabla$ </td><td>Significance or entropy of an attribute</td></tr><tr><td> $\tau(C_i, A)$ </td><td>Tightness of a cluster C of attribute A</td></tr><tr><td>Thr</td><td>Threshold (G.Thr, L.Thr)—Global and local threshold</td></tr><tr><td> $l_1^k$ </td><td>Intra cluster tightness in k clusters (heuristic value 1)</td></tr><tr><td> $l_2^k$ </td><td>Inter cluster tightness in k clusters (heuristic value 2)</td></tr><tr><td> $l_3^k$ </td><td>Cluster quality of k clusters (heuristic value 3)</td></tr><tr><td> $v^k = l_i^k$ </td><td>Local attribute interestingness (harmonic aggregation) in iteration k</td></tr><tr><td> $X^k$ </td><td>Local attribute heuristic values (1, 2 and 3) in iteration k</td></tr><tr><td> $I_c$ </td><td>Interestingness linear function on concept value c</td></tr><tr><td> $H(I_c)$ </td><td>Interestingness non-linear function (probability density function—pdf)</td></tr><tr><td> $l_g^i$ </td><td>Global interestingness for attribute i (harmonic aggregation)</td></tr><tr><td> $l_g^D$ </td><td>Global interestingness for table D (harmonic aggregation)</td></tr><tr><td> $l_L^i$ </td><td>Total local cluster interestingness of attribute i</td></tr><tr><td> $l_g^T$ </td><td>Total global cluster interestingness of table T</td></tr></table>

Appendix F. Conc. Hierarchies—Census data  
![](/api/attachments/35BDM6JA/fulltext/images/741bc11ea6b65a17a055cbb54429885e831eb47359a90175d087f7f8b4cbcbf1.jpg)

![](/api/attachments/35BDM6JA/fulltext/images/6a5f0bfa0bc83837208e58e8c49570ab1061cee8541efdab3be5ea47cf347b58.jpg)

![](/api/attachments/35BDM6JA/fulltext/images/459dced07f7f09fde1e5b8a763ea22ec8acd901de9c76d72afe340e3e02e8f52.jpg)

![](/api/attachments/35BDM6JA/fulltext/images/6504ac7631ad9e14da1b2924a23121044a6e8d2fce7bcd89a0ed69a74366e0f9.jpg)

Appendix G. Conc. Hierarchies—Cancer data  
![](/api/attachments/35BDM6JA/fulltext/images/0babe80c2934678eaaec0ae2e4924e07c6df20825f101fa4496a65c38b124bc4.jpg)

Appendix H. List of datasets

<table><tr><td colspan="3">Datasets</td></tr><tr><td></td><td>SIZE (tuples)</td><td>Chosen attributes</td></tr><tr><td>Cancer Wisconsin</td><td>0.7 K</td><td>bareNuclei, normalNuclei, cellSize, mitosis</td></tr><tr><td>Census-income 1</td><td>50 K</td><td>Age, education, numWorkedFor</td></tr><tr><td>Census-income 2</td><td>200 K</td><td>Age, education, majIndCode, detailHHold, instanceWeight, numWorkedFor</td></tr></table>

## References

[1] B. Barber, H.J. Hamilton, A comparison of attribute selection strategies for attribute-oriented generalisation, Symposium on Methodologies for Intelligent Systems (ISMIS'97), 1997, pp. 106–116.

[2] C.L. Carter, H.J. Hamilton, Ef<sup>fi</sup>cient attribute-oriented generalisation for knowledge discovery from large databases, IEEE Transactions on Knowledge and Data Engineering 10 (2) (1998) 193–208.

[3] Y.L. Chen, Y.Y. Wu, R.I. Chang, From data to global generalised knowledge, Decision Support Systems 52 (2) (2012) 295–307.

[4] D.W. Cheung, A.W. Fu, J. Han, Ef<sup>fi</sup>cient rule-based attribute-oriented induction for data mining, Intelligent Information Systems 15 (2000) 175–200.

[5] U.M. Fayyad, G. Piatetsky-Shapiro, R. Uthurusamy, Data mining: the next 10 years, SIGKDD Explorations 5 (2) (2003) 191–196.

[6] D.R. Fudger, H.J. Hamilton, A heuristic for evaluating databases for knowledge discovery with DBLEARN, Rough Sets and Knowledge Discovery, 1993. 29–39.

[7] H.J. Hamilton, D.R. Fudger, Estimating DBLEARN's potential for knowledge discovery in databases, Computational Intelligence 11 (2) (1995) 280–296.

[8] J. Han, Towards ef<sup>fi</sup>cient inductive mechanisms, Theoretical Computer Science 133 (1994) 361–385.

[9] J. Han, Y. Fu, Exploration of the power of attribute-oriented induction in data mining, Advances in Knowledge Discovery and Data Mining, AAAI/MIT Press, 1996. 399–421.

[10] R.J. Hilderman, H.J. Hamilton, Knowledge discovery and measures of interest, Kluwer Academic Publishers. 2001.

[11] R.J. Hilderman, H.J. Hamilton, N. Cercone, Data mining in large databases using domain generalisation graphs, Journal of Intelligent Information Systems 13 (3) (1999) 195–234.

[12] Y.-F. Huang, C.-M. Wu, Mining generalised association rules using pruning techniques, ICDM, 2002, pp. 227–234.

[13] C.-C. Hsu, Extending attribute-oriented induction algorithm for major values and numeric values, Expert Systems with Applications 27 (2) (2004) 187–202.

[14] K. Julisch, Clustering intrusion detection alarms to support root cause analysis, ACM Transactions on Information and System Security 6 (4) (2003) 443–471.

[15] B. Liu, K. Zhao, J. Benkler, W. Xiao, Rule interestingness analysis using OLAP operations, 12th ACM SIGKDD Conference on Knowledge Discovery and Data Mining, USA, 2006, pp. 297–306.

[16] M.K. Muyeba, K. Crockett, J.A. Keane, A hybrid interestingness heuristic approach for attribute-oriented mining, LNCS 6682 (2011) 414–424.

[17] L. Pitt, R.E. Reinke, Criteria for polynomial-time (conceptual) clustering, Machine Learning 2 (4)(1988) 371-396.

[18] P.-N. Tan, V. Kumar, J. Srivastava, Selecting the right objective measure for association analysis, Information Systems 29 (4) (2004) 293–313.

[19] UCI Datasets, http://archive.ics.uci.edu/ml/index.html (accessed 27/11/12).

[20] X. Wu, 10 years of data mining research: retrospect and prospect, IEEE International Conference on Data Mining (ICDM), 2010, p. 7.

[21] C. Yen-Liang, S. Ching-Cheng, Mining generalised knowledge from ordered data through attribute-oriented induction techniques, European Journal of Operationa Research 166 (1) (2005) 221–245.

![](/api/attachments/35BDM6JA/fulltext/images/d79905468de3b010b0f32e0cbc34c011cdd3925d5c1434b7e87bca990072e688.jpg)

Dr Maybin Muyeba is a Senior Lecturer in the School of Computing, Mathematics and Digital Technology at Manchester Metropolitan University. He gained a BSc. in Mathematics from the University of Zambia in 1989, an MSc in Computing in 1991 (from Hull University, UK) and a PhD in data mining from University of Manchester Institute of Science and Technology (UMIST), UK in 2002. He has industrial experience as a Software Engineer. He is involved in many conferences and journals as a reviewer, session chair and committee member. He also has collaborative research links with the University of Manchester, University of Liverpool, University of Regina (Canada) and Macau University (China). His research interests are in data mining, fuzzy logic, intelligent systems and evolutionary computing.

![](/api/attachments/35BDM6JA/fulltext/images/8c4f0cb4898e294689a441599fa5e67ad2cd7b76c77731e32a4da5a8c6c0ff39.jpg)

Dr Keeley Crockett gained a B.Sc. degree in Computation from the University of Manchester Institute of Science and Technology (UMIST) in 1993, and a PhD in Fuzzy Rule Induction from Data Domains from the Manchester Metropolitan University in 1998. She currently leads the Intelligent Systems group at Manchester Metropolitan University, UK. Her research interests: fuzzy decision trees, Dialogue systems, rule induction, and data mining.

![](/api/attachments/35BDM6JA/fulltext/images/4f51f311d541ac8a23a8218487b788fa25928bffe6da2c146c049c418596758b.jpg)

Dr Wenjia Wang is a senior lecturer in the School of Com: puting at University of East Anglia since September 2002. Dr Wang received his B.Eng (1982) and M.Eng (1985) degrees from the NEU (North Eastern University, China) in Automatic Control Engineering, and PhD degree in Advanced Computing in 1996 from the University of Manchester Institute of Science and Technology (UMIST), UK. His research in terests are in the areas of data mining/knowledge discovery, ensemble approach and arti<sup>fi</sup>cial intelligence.

Professor John Keane holds the MG Singh Chair in Data Engineering in the School of Computer Science and the Manchester Institute for Biotechnology at the University of Manchester. He is also an Honorary Professor of Data Analytics at Manchester Business School, where he co-directs the Decision and Cognitive Sciences Research Centre. His research is in the area of data analytics and decision support. He is an Associate Editor of IEEE Transactions on Fuzzy Systems
