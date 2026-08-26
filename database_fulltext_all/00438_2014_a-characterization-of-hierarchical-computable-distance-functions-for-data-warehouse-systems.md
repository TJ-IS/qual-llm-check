---
otero_id: 438
otero_key: "9KYC7BS8"
title: "A characterization of hierarchical computable distance functions for data warehouse systems"
authors: "Matteo Golfarelli; Elisa Turricchia"
year: "2014"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2014.03.011"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A characterization of hierarchical computable distance functions for data warehouse systems

Matteo Golfarelli ⁎, Elisa Turricchia

DISI, University of Bologna, Italy

## a r t i c l e i n f o

Article history: Received 22 August 2013 Received in revised form 10 March 2014 Accepted 30 March 2014 Available online 12 April 2014

Keywords: Testing Similarity measures Hierarchical data Categorical data

## a b s t r a c t

A data warehouse is a huge multidimensional repository used for statistical analysis of historical data. In a data warehouse events are modeled as multidimensional cubes where cells store numerical indicators while dimensions describe the events from different points of view. Dimensions are typically described at different levels of details through hierarchies of concepts. Computing the distance/similarity between two cells has several applications in this domain. In this context distance is typically based on the least common ancestor between attribute values, but the effectiveness of such distance functions varies according to the structure and to the number of the involved hierarchies. In this paper we propose a characterization of hierarchy types based on their structure and expressiveness, we provide a characterization of the different types of distance functions and we verify their effectiveness on different types of hierarchies in terms of their intrinsic discriminant capacity.

© 2014 Elsevier B.V. All rights reserved

## 1. Introduction

Effectively measuring the similarity, or symmetrically the distance, between objects is a generic research issue whose solution changes depending on the characteristics of the involved data. In this paper we focus on the distance functions for categorical and hierarchical attributes. On the one hand categorical data are intrinsically unordered and this limits the possibility of de<sup>fi</sup>ning an effective distance measure [1]. On the other hand, the presence of hierarchies of concepts enriches the description of the objects and provides a tool for partially restoring an ordering between them.

Categorical and hierarchical attributes are particularly relevant since they are one of the building bricks for multidimensional data spaces, where a single data object is described by several of this attributes. We will refer to such data spaces as Hierarchical Non-Ordered Discrete Data Spaces — HNODDSs that extend the acronym NODDS coined in [2]. Similarity search for HNODDSs is becoming increasingly important for several application domains such as multimedia information retrieval, statistical data analysis, scienti<sup>fi</sup>c databases and data mining [3]. In particular, HNODDSs are at the core of data warehouses that are huge multidimensional repositories used for statistical analysis of historical data [4]. In a data warehouse events are modeled as multidimensional cubes where cells store numerical indicators while dimensions describe the events from different points of view. For example, a SALE cube would store the quantity sold and the corresponding sale amount; each sale would be de<sup>fi</sup>ned by a CITY, a PRODUCT and a DATE. All the attributes are categorical, except DATE. Fig. 1 shows an example for the CITY hierarchy. Identifying the distance between a couple of cube cells/events has several applications. For example a user would bene<sup>fi</sup>t in automatically retrieving events that are similar to those she is currently browsing. On the other hand, the identi<sup>fi</sup>cation of events that are very dissimilar from all of the others (i.e. outliers) would be very useful to both endusers (e.g. detection of anomalous behaviors) and system administrators (e.g. detection of erroneous data during the data warehouse ETL)

Distance functions for hierarchical data have been proposed in many different contexts. [5] de<sup>fi</sup>nes a set of measures for assessing the distance between words exploiting a taxonomy of concepts, [6] shows that these methods work well on a large set of a taxonomies of medical terms. [7] analyzes different similarity criteria and tests them in the area of data warehousing on user labeled data to understand which is the one that matches the human perception of similarity at best. All the previous papers state that, when categorical and hierarchical attributes are involved the least common ancestor — LCA between values at the lowest level of the hierarchy plays a crucial role in de<sup>fi</sup>ning a user-meaningful distance function. [7] uses the term hierarchical computable for such type of distances. Please note that distances included in this class do not keep information coming from a corpus into account (e.g. the frequency a particular city has in the data set). All the previous papers investigate the effectiveness of hierarchical computable distances that is measured a posteriori typically through a manual tagging of the results. The authors also debate on the weakness of their measures, but limit their discussion to empirical considerations, failing to provide a well-founded answer due to the lack of an analytic model.

Effectiveness of hierarchical computable distances depends on both the LCA's features used to de<sup>fi</sup>ne them (e.g. the level of the LCA or the distance from it or the number of data objects subsumed by the LCA) and on the hierarchy structure. In particular the quantity of information coded in a hierarchy, and consequently the level of precision of a hierarchical computable distance, changes with its depth and size.

![](/api/attachments/9KYC7BS8/fulltext/images/76958c79af16b3f1ade1f3f10b6f13d91c1b1e169408f811ccfb6b6f4d57dd2e.jpg)  
Fig. 1. A hierarchy and its instances.

When multidimensional objects are involved a clear understanding of the characteristics that in<sup>fl</sup>uence the effectiveness of distance functions is even more crucial since the presence of several hierarchies, possibly with different characteristics, could make correctly capturing similarity more complex or even impossible. As shown in the paper, HNODDSs are subject to the so called curse of dimensionality, thus it is important to know to which extent similarity queries (e.g. range and nearest neighbor queries) make sense.

To the best of our knowledge no paper in the literature proposes a precise characterization of the effectiveness and limitations of hierarchical computable distances in terms of the structure and size of the hierarchy. In this paper we move a <sup>fi</sup>rst relevant step in this direction, by providing:

• a characterization of hierarchical and categorical attributes according to the structure of their hierarchies (see Section 4);

• a characterization of hierarchical computable distances based on the type of information they consider (see Section 4);

• a probabilistic model that analytically de<sup>fi</sup>nes the discriminant capabilities of the distance functions. The model works in the mono-dimensional case (see Section 5.1) as well as in the multidimensional one (see Section 5.2). Together with the model some indicators are provided to evaluate the discriminant capacity of hierarchies, distance function and HNODDS: some of them are original, while others are enabled in HNODDSs by the model (e.g. Intrinsic dimensionality).

• a set of experimental results, carried out on both real and synthetic data sets, that provide an empirical evaluation of the effectiveness and ef<sup>fi</sup>ciency of hierarchical computable distances, both for a single categorical and hierarchical attribute and for HNODDSs (see Section 6).

Our contributions are valuable tools for both practitioners and researchers involved in de<sup>fi</sup>ning similarity functions or in designing hierarchy structures. Indeed, no techniques are currently available to estimate a priori the capabilities/limits of a given similarity measure when applied on a given categorical hierarchy or a given HNODDS. All the evaluations are carried out a posteriori through subjective user's feedbacks. Conversely, the characterization we propose de<sup>fi</sup>nes a formal framework for such evaluation, gives some rules of thumb for coupling measures and hierarchies and it <sup>fi</sup>nally provides indicators (original and non original) for evaluating, at design time and on an objective basis, the discriminant capacity of distance functions and hierarchies.

## 2. Related literature

The de<sup>fi</sup>nition of similarity and distance functions is a wide research area that covers several application domains ranging from information retrieval to multimedia applications. Each domain requires a speci<sup>fi</sup>c de<sup>fi</sup>nition of distance that should exploit the characteristics of the involved data and should be meaningful for the application users as well. When data are numeric, distances can be derived starting from the classic Euclidean distance function or the Minkowski one that generalizes it. Several more sophisticated concepts have been devised in the literature [8], for example the Mahalanobis distance improves over Euclidean one since it is scale-invariant and it takes into account the correlations of the data set. Recently, with the increasing complexity of data entities across various domains, an increasing interest has been raised by nonmetric distances. Although this type of distances allows the modeling of complex distance concepts, they cannot exploit the nice topological properties of the metric ones and thus require ad-hoc techniques for ef<sup>fi</sup>ciently running a similarity search [9].

When data compared are categorical, they are typically modeled as sets of elements (e.g. Overlap Coef<sup>fi</sup>cient, Jacard's Coef<sup>fi</sup>cient). The distance between two collections is then computed on the basis of their set or bag intersection [8]. Based on this idea several more advanced approaches have been proposed for categorical attributes (see [1] for a comprehensive analysis). Basically they exploit the cardinality of the different elements (e.g. Eskin [10]) or the frequency of the considered attribute values (e.g. Inverse Occurrence Frequency — IOF [11], Goodall [12]) to differentiate the similarity between couple of objects. Such information allows the computation of accurate similarity measures.

Intersection-based measures do not accurately capture similarity when data are sparse or when there are known relationships between items. This is the case for hierarchically organized domains whose similarity has been studied <sup>fi</sup>rst in [13]. In that paper the authors generalize the cosine-similarity to take the hierarchy into account. In the generalized-cosine-similarity — GCSM two unit vectors (i.e. two vectors modeling a single leaf of the hierarchy), are no more perpendicular if such leafs share a common ancestor in the hierarchy. In other words, the closer the common ancestor the more similar the two elements. The idea of computing the path through the hierarchy for exploiting hierarchical information has been adopted in many other approaches, for example in [14] it is used to model the semantic similarity in an ontology. A similarity/ distance measure is also necessary in outlier detection applications. To the best of our knowledge the only approach that poses the problem in a HNODDS like context and exploits aggregated information is [15] that models criminal incidents as multidimensional cells whose dimensions describe the incident (e.g. type of incident, weapon-used). The distance function used to compute the extremeness of a cell is based on the frequency of events in the current cell compared to those of its neighborhood (i.e. all the possible aggregations of the current cell on the available dimensions). Unfortunately the approach does not use hierarchies: each dimension is characterized by one attribute and aggregations are obtained by considering or dropping it.

As to effectiveness of distance functions for hierarchical data, an interesting paper is the one by Baiakousi et al. [7]. The paper experimentally assesses the effectiveness of some known similarity measures based on a user study. Interestingly the study con<sup>fi</sup>rms that the functions that seem to <sup>fi</sup>t the user needs at best are those choosing as the closest point the one with the shortest path through the hierarchy. Unfortunately the study does not evaluate the discriminant capacity of the proposed measures and it considers only data with a very limited dimensionality.

When dimensionality increases the data space becomes progressively sparser and this could lead to the occurrence of the curse of dimensionality: all the objects in the data space become dissimilar. Curse of dimensionality [16] initially affects the ef<sup>fi</sup>ciency of similarity search algorithms and common data organization strategies and it progressively makes the concept of proximity meaningless from a qualitative perspective. In such a case, the nearest neighbor problem becomes ill de<sup>fi</sup>ned, since the contrast between the distances to different data points does not exist. The proximity meaningfulness criterion provided in [16], is further investigated in [17,18] for $L _ { k }$ metrics. In particular in [17] the authors show that the problem of meaningfulness in high dimensionality is sensitive to the value of k. Several alternative de<sup>fi</sup>nition of nearest neighbor have been provided for lessen the effects of curse of dimensionality; for example [18] de<sup>fi</sup>nes Generalized Nearest Neighbors and proposes a quality criterion to assess the importance of the dimensions with respect to a given query and then carry out similarity search on the selected dimensions only. [19] de<sup>fi</sup>nes Shared-Neighbor Distances that are secondary similarity measures obtained by the rankings induced by a speci<sup>fi</sup>ed primary measure such as an $L _ { k } .$ . Similarly many others heuristics, working with the Euclidean distance, have been proposed or evaluated for clustering [20–23], outlier detection [24,25], and indexing or similarity search [26,27] that seek to mitigate the effects of the curse of dimensionality.

Another interesting concept related to high-dimensional data spaces is their intrinsic dimensionality [28,29] that tries to capture the real dimensionality of a vector space and that can be used to measure the dif<sup>fi</sup>culty of searching in it. The de<sup>fi</sup>nition of intrinsic dimensionality is extended to metric spaces in [30] that models it in terms of statistical properties of the object distance distribution. Such measure is then used to compute a lower bound on the performance of large classes of proximity search algorithms. To the best of our knowledge no study examines in-depth the effects of high dimensionality for HNODDS and hierarchical computable distances.

The effectiveness of hierarchical computable distances is a topic discussed in many papers and the need for analytical tools that enable an accurate analysis is felt in many areas. In [5] the effectiveness of the proposed distance is measured using the correlation between the computed semantic similarity values and the human ratings on a benchmark including 30 word couples; all the considerations have been derived from a limited set of subjective tests. The same holds in [31] that studies hierarchical computable distances in hierarchical nets of semantic terms. Here tests are carried out in the medical contexts and the role of experts has been played by 20 university students. Beyond empirical evaluations the paper reports a set of open-questions about how to structure the hierarchy in order to improve its effectiveness. Similar examples can be found in many other research areas such as information retrieval and data mining. In particular, researches related to On-line Analytical Mining (OLAM) apply mining algorithms on top of data warehouses [32]. The growing interest in such type of applications makes HNODDS more and more relevant and asks for a precise analysis of hierarchically computable distance effectiveness.

## 3. Basic de<sup>fi</sup>nitions and background

In this section we introduce a basic formal setting to manipulate objects in HNODDS.

Hierarchy Given a set $A = \{ a _ { 0 } , . . . a _ { l } \}$ of hierarchical computable attributes $- H C A ,$ , each de<sup>fi</sup>ned on a categorical domain $D o m ( a _ { k } )$ , a hierarchy h is de<sup>fi</sup>ned by (1) a roll-up total order $\succcurlyeq h$ of A; and $( 2 )$ a family of roll-up functions including a function $R o l l _ { a _ { k } } ^ { a _ { i } }$ $D o m ( a _ { k } ) {  } D o m ( a _ { i } )$ for each pair of attributes $a _ { k }$ and $a _ { i }$ such that $a _ { k } \succcurlyeq _ { h } a _ { i } .$

The top attribute of the order is denoted by dim $= { a _ { k } } \in A | { a _ { k } } \succcurlyeq { _ { h } } { a _ { i } } \forall { a _ { i } }$ $\in A$ and determines the <sup>fi</sup>nest aggregation level for the hierarchy. Conversely, the bottom attribute is denoted by ALL, has a single possible value All, and it determines the coarsest aggregation level. The level of an attribute $a \in A$ is de<sup>fi</sup>ned by the cardinality of the set of attributes it determines:

$$
l e v e l (a) = | \overline {{A}} | \text { where } \overline {{A}} = \{a _ {i} \in A | a _ {i} \succcurlyeq_ {h} a \}.
$$

The attribute level models the total ordering between attributes, thus i $\dot { \mathbf { \zeta } } a _ { i } \succcurlyeq a _ { j }$ then $j \geq i . A$ total order roll-up implies that hierarchy instances are organized in a tree having All as the root and the values of dim as leafs. The hierarchy tree includes $L + 1$ levels, where L = level $( A L L ) ;$ roll-up functions allow for values of <sup>fi</sup>ne-grained attributes to be mapped into values of coarse-grained ones. The values at a lower level of the hierarchy rolling-up to a single value at a higher level are called its descendants:

$$
\operatorname{Desc} (x) _ {a _ {k}} ^ {a _ {i}} = \left\{z \in \operatorname{Dom} \left(a _ {k}\right) | x = \operatorname{RollUp} _ {a _ {k}} ^ {a _ {i}} (z) \right\}.
$$

We call children of x its descendants belonging to $a _ { k } | l e v e l ( a _ { k } ) =$ leve $l ( a _ { i } ) - 1$

Example. With reference to Fig. 1 City ≽ Country ≽ Region $\succcurlyeq A L L ;$ Dom(Region) = (Europe,America); Roll ${ \cal J } p _ { C i t y } ^ { R e g i o n } ( R o m e ) ~ =$ Europe; level(Country) = 1. Finally Rome and Milan are Italy's children.

Least common ancestor Given a hierarchy h and two attribute values x and y at level i and j respectively, their least common ancestor is the attribute value z at level $k \geq i , j$ such that:

$$
\begin{array}{c} l c a (x, y) = \{z | z = R o l l U p _ {a _ {i}} ^ {a _ {k}} (x) \wedge z = R o l l U p _ {a _ {j}} ^ {a _ {k}} (y) \\ \wedge \nexists a _ {k} ^ {\prime} \succ_ {h} a _ {k} | R o l l U p _ {a _ {i}} ^ {a _ {k} ^ {\prime}} (x) = R o l l U p _ {a _ {j}} ^ {a _ {k} ^ {\prime}} (y) \}. \end{array}
$$

We denote with $a t t r ( l c a ( x , y ) ) = a _ { k }$ the attribute whose domain lca belongs to.

Data space Given a set of hierarchies $H \ = \ \{ h _ { 1 } , . . . h _ { d } \} ,$ , a ddimensional HNODDS $\Delta$ is de<sup>fi</sup>ned as a subset of the cartesian product of dimension attributes dim ${ \bf \nabla } \times \ldots \times d i m _ { d } .$

Data space object An object x ∈ Δ is de<sup>fi</sup>ned by a value from the domain of the each dimension in $\Delta \colon x = ( x _ { 1 } , . . . , x _ { d } )$ where x ∈ Dom(dim ). A function Meas(x) maps each object either to a numerical value called measure or to NULL. Each object x, such that Meas(x) ≠ NULL is called a fact of Δ. For each value x of a hierarchy attribute, we de<sup>fi</sup>ne its frequency Freq(x ) as the fraction of objects in Δ that holds that value $x _ { i \cdot }$ If the attribute is not a dimension such fraction is computed as the fraction of objects that holds values rolling-up to x .

## 4. Distance characterization

The type of hierarchy de<sup>fi</sup>ned in Section 3 encodes an IS-A taxonomy with single inheritance and same depth for all branches. A hierarchy encodes semantic relationships between its concepts, the higher the level the more general the concepts. The basic idea of hierarchical computable distances is that, given two concepts, the more general the concept that subsumes them, the more distant they will be. According to this intuition, and given that the most speci<sup>fi</sup>c subsumer of two concepts is their LCA, the problem of determining the distance between two objects is turned in determining how to measure the level of generalization of the LCA.

We initially note that the structure of a hierarchy intrinsically determines its capability to correctly model the level of generality of the LCA. The structure can be well characterized by the hierarchy depth L and by the out-degree D of the nodes of the tree they induce at the instance level. Based on such elements we distinguish between:

• Regular hierarchies, where D is the same for all the levels and for all the instances of each level. As a consequence they are suitable to model hierarchies of concepts where the level of generalization increases proportionally to the level of the concepts and it is the same for all the concepts at the same level.

• Level-regular hierarchies, where D is the same for all the instances at a given level, but can change for different levels. In this type of hierarchy moving between levels can entail different variations of the generalization degree.

• Irregular hierarchies, where D can change even for instances at the same level of the hierarchy. In this type of hierarchy two concepts at the same level can have a different level of generalization.

The three proposed classes (see Fig. 2) are progressively more <sup>fl</sup>exible in modeling the semantic relationships between concepts and thus have an increasing expressiveness. Obviously the values of the two parameters L and D are strictly related: given the dim cardinality, the higher D, the lower L. For regular hierarchies such relationship can be expressed through the following formulas:

$$
L = \log_ {D} | D o m (d i m) | \quad D = \sqrt [ L ]{| D o m (d i m) |}.\tag{1}
$$

Intuitively, a hierarchy with a low value for D and a high value for L should be preferred since it carries more information and describes with more details how the concepts in the hierarchy are related. Properly determining the level of generalization of the LCA thus depends on the information actually provided by the hierarchy structure and on the capability of the distance function to properly exploit it.

We distinguish two basic distance categories based on the two types of information related to the LCA: its level,<sup>1</sup> and the number of dimensional objects – occurrences – it subsumes. The same holds for measures based on the path through the hierarchy tree between x and y (that is the double of the distance from x or y to their LCA).

• Level-based distances, compute the level of generalization of the LCA considering its level only. Eq. (2) reports the simplest and most used measure in this category.

$$
D i s t _ {h} ^ {L e v} (x, y) = l e v e l (a t t r (l c a (x, y))).\tag{2}
$$

Noticeably, $D i s t _ { h } ^ { L e v }$ is at the core of the Generalized Cosine Similarity [13] and, according to [7], it matches very well the human perception of similarity. Nonetheless, we expect such measures to be suitable for regular hierarchies only, since the reduction/increase of the generalization is constant through the levels.

• Occurrence-based distances, compute the level of generalization of the LCA based on the fraction of values in dim it subsumes: the larger such portion the more general the LCA.

$$
D i s t _ {h} ^ {O c c} (x, y) = | D e s c _ {d i m} ^ {a t t r (l c a (x, y))} (l c a (x, y)) |.\tag{3}
$$

This type of distances correctly captures the number of concepts subsumed by the LCA for all the types of hierarchies, but it requires a precise knowledge of the hierarchy instance. Other measures approximate such knowledge so that the distance can be computed based on the hierarchy structure only. We propose two representatives for this category, both of them approximate the number of subsumed values exploiting the structural parameter D: the one reported in Eq. (4)

considers D as a constant, while the one reported in Eq. (5) considers D as a variable whose values can be different for different levels of the hierarchy.

$$
D i s t _ {h} ^ {O c c D C} (x, y) = \left\{ \begin{array}{l l} 0 & \text { if } l e v e l (a t t r (l c a (x, y))) = 0 \\ D ^ {l e v e l (a t t r (l c a (x, y)))} & \text { otherwise } \end{array} \right.\tag{4}
$$

$$
D i s t _ {h} ^ {\text { OccDV }} (x, y) = \left\{ \begin{array}{l l} 0 & \text { if   } \text { level } (\text { attr } (l c a (x, y))) = 0 \\ \prod_ {1 \leq i \leq \text { level } (\text { attr } (l c a (x, y)))} D _ {i} & \text { otherwise } \end{array} \right.\tag{5}
$$

$D i s t _ { h } ^ { O c c D C }$ improves over $D i s t _ { h } ^ { L e v }$ since it relies on a more precise value for the number of subsumed concepts (i.e. the approximation function is not linear but it is a function of the actual hierarchy structure). Nonetheless, differently from $D i s t _ { h } ^ { O c c D V } ,$ , it fails in computing the correct value when level-regular hierarchies are involved (i.e. when $D _ { i }$ is not a constant).

We initially note that the number of distinct distance values – nDD – returned is equal to $L + 1$ for level-based distances (i.e. it is 0 i ${ \dot { x } } = y ,$ it is L when the LCA is All). As to the occurrence-based ones, the number of distinct distances is higher than in the previous case, since two couples of points having their LCAs at the same level could have different distances due to the different numbers of objects subsumed by the corresponding LCAs. In this case the upper bound to the number of distinct distances is the number of internal nodes in the hierarchy tree, plus the case of zero-distance. As expected, in case of regular hierarchy, this number turns out to be $L + 1$ since all the nodes at the same level of the hierarchy tree subsume the same number of nodes.

When an irregular hierarchy is involved only the occurrencebased distances seem to correctly capture the number of subsumed objects. However the information about the hierarchy instances they need could not be available, or it could be too expansive to collect/update.

The distances de<sup>fi</sup>ned in formulas 2, 3, 4, and 5 are well-known and general examples of the corresponding categories. In many domains different and typically more speci<sup>fi</sup>c functions could be necessary. For example, in the geographic domain a user could assert the distance between two cities having their LCA at the Region level is much higher than the one occurring between two cities having their LCA at the Country level since cities in a country have much more in common than cities belonging to the same region. We generalize the previous examples in the following de<sup>fi</sup>nition.

Hierarchically computable distance — HCD Given a hierarchy h, and two dimensional attribute values x and $y ,$ a hierarchically computable distance between x and y is either a function of the level of their $\mathrm { L C A } D i s t _ { h } ( x , y ) = f ( l e v e l ( a t t r ( l c a ( x , y ) ) )$ ) or a function of the number of descendants of their LCA $D i s t _ { h } ( x , y ) = f ( | D e s c _ { d i m } ^ { a t t r ( l c a ( x , y ) ) } ( l c a ( x , y ) ) | )$ ) such that $D i s t _ { h } ( x , y ) \in [ 0 , \infty )$ and f is a strictly monotonically increasing function such that $f ( 0 ) = 0$

When the distances between the values of a CHA are computed through an HCD they give rise to an ultrametric space. More formally an ultrametric space is a pair, $\mathcal { U } = ( a , D i s t )$ , where Dom(a) is the <sup>U ¼ ð Þ</sup>domain of the feature – Ű the values of the $\mathrm { C H A } - \ddot { \mathrm { U } }$ and Dist is a function Dom $\iota ( a ) \times D o m ( a ) \mathrel { - } \textgreater$ ℝ with the following properties:

$D i s t ( x , y ) = D i s t ( y , x )$ (symmetry)

$D i s t ( x , y ) > 0 \ x \neq y )$ and $D i s t ( x , x ) = 0$ (non negativity)

$D i s t ( x , y ) \leq m a x \{ D i s t ( x , z ) , D i s t ( y , z ) \}$ (strong triangular inequality).

In an ultrametric all the triangles are isosceles, that is any given three points can be relabeled as x, y, z so that $d ( x , y ) \leq d ( x , z ) = d ( y , z )$ . This property is also called three-point condition [33,34].

![](/api/attachments/9KYC7BS8/fulltext/images/0d4b7a736949c0bad10666668a66af83d0e052b7adabafb7e1a9516c68733bf6.jpg)  
Fig. 2. Hierarchy trees corresponding to the three different hierarchy types.

Theorem 4.1. $D i s t _ { h } ( x , y )$ is an ultrametric and thus a metric.

Proof. Non-negativity is easily veri<sup>fi</sup>ed considering that $D i s t _ { h } ( x , y )$ $\in \ [ 0 , \infty )$ . Identity of indiscernibles holds by de<sup>fi</sup>nition since both level(attr(lca(x,y))) and $| D e s c _ { d i m } ^ { a t t r ( l c a ( x , y ) ) } ( l c a ( x , y ) ) |$ are equal to zero $\operatorname { i f } x =$ y while they are greater than zero in all the other cases due to f strict monotonicity. Symmetry is veri<sup>fi</sup>ed since the properties (i.e. distance and number of subsumed objects) are intrinsically symmetric. As to the strong triangle inequality we should consider that, since the values are hierarchically organized, given three points x $, y , z$ only two con<sup>fi</sup>gurations are possible for their LCA. The points can share the same LCA, that is $l c a ( x , y ) = l c a ( x , z ) = l c a ( y , z )$ , or the LCA of two of them, x and y without loss of generality, must be closer $( \mathrm { i . e . , ~ } l e \nu e l ( a t t r ( l c a ( x , y ) ) )$ $< l e v e l ( a t r ( l c a ( x , z ) ) ) = l e v e l ( a t t r ( l c a ( y , z ) ) ) )$ . In the <sup>fi</sup>rst case, it will be $D i s t _ { h } ( x , y ) = D i s t _ { h } ( x , z ) = D i s t _ { h } ( y , z )$ . In the second case, we will have $D i s t _ { h } ( x , y ) < D i s t _ { h } ( x , z ) = D i s t _ { h } ( y , z )$ that respects the three-point condition. The second part of the theorem holds because an ultrametric is always a metric. □

Ultrametricity is a valuable property that can be exploited to reduce the computational complexity of the range query costs. In a metric space, given an attribute a and a query point $q \in D o m ( a )$ pruning of objects is based on the distance from a pivot p $\in D o m ( a )$ . Exploiting triangle inequality, we can discard the objects $x \in D o m ( a )$ that satisfy one of the following inequalities: $D i s t _ { h } ( p , x )$ $< D i s t _ { h } ( p , q ) - r \ \mathrm { o r } \ D i s t _ { h } ( p , x ) > D i s t _ { h } ( p , q ) + r ,$ where $r > 0$ is the range of the query. In other words, we must compute $D i s t _ { h } ( q , x )$ only for the points x belonging to the annular ring centered in p and with a 2r thickness. In an ultrametric space we further know that triangles are equilateral or isosceles with the different sides shorten than the others. This enables the following result:

Theorem 4.2. Le $\boldsymbol { ! } \mathcal { U } = ( a , D i s t )$ be an ultrametric space and let p a point in with known distances from all points $x \in D o m ( a )$ (i.e. p is a pivot). A <sup>U</sup>range query on with query range r from the query point q can be solved computing $D i s t ( q , p )$ only if the distances from p are stored in ascending order.

Proof. Due to ultrametric properties, one of the following conditions hold:

1. If $\cdot D i s t ( p , x ) \leq D i s t ( q , p )$ then $D i s t ( q , x ) = D i s t ( q , p )$ 2. I $\ f D i s t ( p , x ) > D i s t ( q , p )$ then $D i s t ( q , x ) = D i s t ( p , x ) .$

According to the previous cases we can always infer $D i s t ( q , x )$ from the known values of either $D i s t ( q , p )$ or Dist(p,x). Thus no additional distances need to be computed at query time. More precisely, if $D i s t ( q , p ) > r$ the result set is always empty since

$\mathrm { I f } D i s t ( p , x ) \leq D i s t ( q , p )$ then $D i s t ( q , x ) = D i s t ( q , p ) > r$

$$
\bullet \text {   If   } D i s t (p, x) > D i s t (q, p) \text {   then   } D i s t (q, x) = D i s t (p, x) > D i s t (q, p) > r.
$$

Conversely if $D i s t ( q , p ) \leq r ,$ according to Case 2, we can stop the search as soon as we <sup>fi</sup>nd an x such that $D i s t ( p , x ) > r$ since whatever points x′ that follows will have $D i s t ( p , x ^ { \prime } ) > D i s t ( p , x ) > r .$ □

Example. With reference to Table 1 $\mathrm { i f } \ D i s t _ { h } ( q , p ) = 2$ and $r = 3$ the range query returns $\{ x _ { 1 } , x _ { 2 } , x _ { 3 } \}$ , with distances of the three points from q equal to 2, 2 and 3 respectively. Conversely, $\mathfrak { i f } D i s t _ { h } ( q , p ) = 4$ and $r =$ 3 the result set is empty and the distances $D i s t _ { h } ( q , x _ { i } )$ are 4, 4, 4, and 5 respectively.

## 5. An analytical model for hierarchically computable distances

The discriminant capacity of a distance function is bounded by the number of distinct distances it can determine and by the distribution of such values. For example using a Minkowski distance in a multidimensional Euclidean space with n objects, we can have up $\mathbf { t } \mathbf { 0 } { \frac { n \times ( n - 1 ) } { 2 } } + 1$ distinct distances. This is not the case for HCDs since the information stored in the hierarchy does not always provide detailed information about the distances between objects. Distance distribution also affects similarity function capabilities as shown in case of curse of dimensionality where all the distances between objects tend to be large. In Subsections 5.1 and 5.2, we de<sup>fi</sup>ne a statistical model to describe the behavior of HCDs in the mono-dimensional and multi-dimensional cases respectively.

## 5.1. The mono-dimensional case

Given two leaf values of a hierarchy, we de<sup>fi</sup>ne the probability they have a speci<sup>fi</sup>c distance i, distinguishing between regular and irregular hierarchies. Please note that distance distributions do not depend on the speci<sup>fi</sup>c user-defined-function f since it always maps distinct distance values to distinct distance values due to its strict monotonicity.

As to regular hierarchies, we remark once again that level-based and occurrence-based distance functions return the same number of distinct distances nDD, and they have the same distance distributions since all and only the nodes at the same level subsume the same number of occurrences. Considering a regular hierarchy h with depth L and out-degree D, the probability two points have distance i can be obtained counting the number of couples of objects having their LCA at level $i \in [ 0 , n D D ]$ where $n D D = L .$

Distances from the pivot p for the ultrametric distance function Dist (p,x).

<table><tr><td> $x_{i} \in Dom(a)$ </td><td> $Dist_{h}(p,x_{i})$ </td></tr><tr><td> $x_{1}$ </td><td>1</td></tr><tr><td> $x_{2}$ </td><td>2</td></tr><tr><td> $x_{3}$ </td><td>3</td></tr><tr><td> $x_{4}$ </td><td>4</td></tr><tr><td> $x_{5}$ </td><td>5</td></tr></table>

$$
\begin{array}{l} P (D i s t _ {h} (x, y) = i) = \frac {1}{| D o m (d i m) | ^ {2}} \\ \qquad \times \left\{ \begin{array}{l} | D o m (d i m) |, \text {   if   } i = 0 \\ \frac {| D o m (d i m) |}{D ^ {i}} \times \frac {D !}{(D - 2) !} \times D ^ {i - 1} \times D ^ {i - 1}, \text {   if   } i \in [ 1, L ] \end{array} \right. \end{array}
$$

where:

$| D o m ( d i m ) | = D ^ { L }$ is the number of dimensional values;

<sub>j</sub> <sub>j</sub> <sup>Dom</sup> <sup>dim</sup> <sub>ð</sub> <sub>Þi</sub> is the number of nodes at level i of the hierarchy (each including D<sup>i</sup> dimensional values);

$\frac { D ! } { ( D - 2 ) ! }$ is the number ways the children of a given node of the hierarchy <sup>ð Þ</sup>can be coupled; it is computed as the 2-permutations of $D ;$

$D ^ { i - 1 } \times D ^ { i - 1 }$ is the number of distances generated by dimensional values rolling-up to two children of a given node at level i. Each child includes $D ^ { i ^ { \star } - 1 }$ dimensional values.

The previous formula can be algebraically simpli<sup>fi</sup>ed to:

$$
P (D i s t _ {h} (x, y) = i) = \frac {1}{D ^ {L}} \left\{ \begin{array}{l l} 1, & \text { if   } i = 0 \\ \left(D ^ {i} - D ^ {i - 1}\right), & \text { if   } i \in [ 1, L ] \end{array} \right..\tag{6}
$$

Example. Considering the regular hierarchy proposed in Fig. 1, where $L = 3 , D = 2$ and $| D o m ( d i m ) | = 8 ,$ , the probability two points have level-based distance 1 is computed as follows: P $( D i s t ( x , y ) = 1 ) = \textstyle { \frac { 1 } { 6 4 } } \times 4 \times 2 \times 1 \times 1 = 0 . 1 2 5$

In case of non-regular hierarchies the probabilities cannot be computed through a combinatorial formula but they can still be derived through a depth-<sup>fi</sup>rst visit of the hierarchy tree. Two different formulas are necessary for level-based and occurrence-based functions. Where necessary we will denote them using the apexes Lev and Occ respectively.

$$
\begin{array}{l} P \left(D i s t _ {h} ^ {L e v} (x, y) = i\right) = \frac {1}{| D o m (d i m) | ^ {2}} \times \\ \left\{ \begin{array}{l} | D o m (d i m) |, \text {   if   } i = 0 \\ \sum_ {z \in D o m (a)} \sum_ {\substack {t \in D o m (a ^ {\prime}) \text {s.t.} \\ \text {s.t. level} (a) = i}} | D e s c (t) _ {d i m} ^ {a ^ {\prime}} | \times (| D e s c (z) _ {d i m} ^ {a} | - | D e s c (t) _ {d i m} ^ {a ^ {\prime}} |), \text {if} i \in [ 1, L ] \\ t \text {is a child of z} \end{array} \right. \end{array}\tag{7}
$$

where:

• z ranges in the values of the attribute at level i of the hierarchy.

• t ranges in the children of each z;

$| D e s c ( t ) _ { d i m } ^ { a ^ { \prime } }$ is the number of the dimensional values that roll-up to t; $| D e s c ( z ) _ { d i m } ^ { a } | - | D e s c ( t ) _ { d i m } ^ { a ^ { \prime } } |$ is the number of dimensional values at <sup>j ð Þ j j ð Þ j</sup>distance i from the t's descendants.

The depth-<sup>fi</sup>rst traversal is necessary to make $| D e s c ( t ) _ { d i m } ^ { a ^ { \prime } } |$ available for each z value.

The formula to be adopted for occurrence-based distances is similar to the previous one, where i ranges in the number of occurrences instead of levels:

$$
\begin{array}{l} P \Big (D i s t _ {h} ^ {O c c} (x, y) = i \Big) = \frac {1}{| D o m (d i m) | ^ {2}} \times \\ \left\{ \begin{array}{l} | D o m (d i m) |, \text {   if   } i = 0 \\ \sum_ {z \in D o m (a) \text {   s.t.   }} \sum_ {t \in D o m (a ^ {\prime}) \text {   s.t.   }} | D e s c (t) _ {d i m} ^ {a ^ {\prime}} | \times \Big (| D e s c (z) _ {d i m} ^ {a} | - | D e s c (t) _ {d i m} ^ {a ^ {\prime}} | \Big) \text {   o.w.   } \\ | D e s c (z) _ {d i m} ^ {a} | = i \qquad t \text {   is   a   child   of   } z \end{array} \right. \end{array}\tag{8}
$$

where:

• z ranges in all the attribute values that subsume i descendants;

• t ranges in the children of each z.

The remaining parts of the formula have the same meaning as in Eq. (7). Also in this case a depth-<sup>fi</sup>rst visit of the hierarchy tree is necessary to practically compute the probability.

Example. Referring to Fig. 1, the probability two points have occurrencebased distance 4 (that is equivalent to a level-based distance of 2) is computed as follows: P Dist x; $\begin{array} { r } { y ) = 4 ) = \frac { 1 } { 6 4 } \times \sum _ { z \in Z } \sum _ { t \in T ^ { z } } 2 \times ( 4 - 2 ) = 0 . 2 5 } \end{array}$ <sup>ð ð Þ</sup>where Z = {Europe,America}, $T ^ { E u r o p e } = \{ I t a l y , E n g l a n d \}$ <sup>- ð</sup>, and $T ^ { a m e r i c a } =$ {Canada,Usa}.

The previous formulas allow us to draw the distance distribution for different hierarchies and give an intuition of their discriminant capabilities. Fig. 3 shows the distance distributions for regular hierarchies with different features and the same cardinality for dim. Although it was expected that the lower the value of L (the higher the value of D) the more skewed the distribution, it is interesting to note that for $L \leq 5$ more than 70% of the couples of leaf values determine the highest distance and consequently it turns in a very low discriminant capacity. Table 2 con-<sup>fi</sup>rms this result also in case of irregular hierarchies (both for levelbased and occurrence-based distances). Please note that although the occurrence-based distance returns much more distinct distances, the 90% of the couples of dimensional values return a limited number of distinct distances, that con<sup>fi</sup>rms a strong skewness of the distance distribution.

A quantitative measure of the discriminant capability of a speci<sup>fi</sup>c distance function would be a highly desirable tool to evaluate the distance effectiveness when applied to a speci<sup>fi</sup>c hierarchy. For example, we could be interested in evaluating the trade-off between maintaining a more complex hierarchy and having a higher discriminant capacity. With this aim we propose the following concept:

![](/api/attachments/9KYC7BS8/fulltext/images/6a9617b5340bef53f44ff247c2185d87a9c14628ac2058ef18a06facf0c10294.jpg)  
Fig. 3. Level-based distance distributions for different hierarchies; |Dom(dim)| = 1024

Irregular hierarchies: (a) number of distinct distances; (b) number of distinct distances returned by the 90% of the couples $\left( x , y \right)$ of dimensional values; (c) intrinsic discriminant capacity. All the data are computed for two different types of distance functions and for three types of irregular hierarchies.

<table><tr><td rowspan="2">Hierarchy features</td><td colspan="3"> $Dist^{Lev}(x,y)$ </td><td colspan="3"> $Dist^{Occ}(x,y)$ </td></tr><tr><td>nDD</td><td>90th dist. %ile</td><td>IDC</td><td>nDD</td><td>90th dist. %ile</td><td>IDC</td></tr><tr><td>D ∈ [1,4], L = 10</td><td>11</td><td>6</td><td>72%</td><td>58</td><td>8</td><td>74%</td></tr><tr><td>D ∈ [1,6], L = 5</td><td>6</td><td>2</td><td>44%</td><td>48</td><td>3</td><td>47%</td></tr><tr><td>D ∈ [1,40], L = 2</td><td>3</td><td>1</td><td>6%</td><td>26</td><td>1</td><td>6%</td></tr></table>

Intrinsic discriminant capacity — IDC Given a hierarchy $h ,$ we de<sup>fi</sup>ne the discriminant capacity of a distance function $D i s t _ { h }$ applied to $h ,$ as the probability two couples of leaf values determine different distances.

$$
I D C (D i s t _ {h}) = \sum_ {i = 0} ^ {n D D - 1} P (D i s t _ {h} (x, y) = i) \times (1 - P (D i s t _ {h} (v, w) = i)).\tag{9}
$$

The higher the IDC, the higher the number of cases where it will be possible to identify the couple of values that is more similar. The IDC is proportional to the number of distinct distances (i.e. nDD) and to the uniformity of the distance distribution, and it will be 0 if all the couples of values would determine the same distance (i.e. the dummy distance function). The IDC can be used to de<sup>fi</sup>ne the optimal hierarchy structure (i.e. the one that determines the highest IDC) that is characterized by a low D value and a high L. This can be intuitively explained since the lower the number of children of a node in the hierarchy, the higher the number of couples of values that can be ordered. In case of regular hierarchies we can analytically derive the previous result since the distance distribution can be expressed through a combinatorial formula.

Theorem 5.1. Let $D i s t _ { h }$ be an HCD applied to a regular hierarchy h with $| D o m ( d i m ) | = D ^ { L }$ leaf values. The IDC for $D i s t _ { h }$ is maximized when the out-degree of the hierarchy nodes, D, is minimal and the hierarchy depth, L, is maximal.

Proof. We initially recall that occurrence-based and level-based distance functions are equivalent when applied to regular hierarchies (i.e. they determine the same distance distributions even if they return different distance values); thus we will prove the theorem for the first family only.

The maximization of Eq. (9) can be formalized as:

$$
\max (I D C (D i s t _ {h})) = \max (\sum_ {i = 0} ^ {L} P (D i s t _ {h} (x, y) = i) \times (1 - P (D i s t _ {h} (v, w) = i)).
$$

Substituting Eq. (6) in the above and applying a set of algebraic simpli fications we obtain:

$$
\max (I D C (D i s t _ {h})) = \max \left(\frac {2 - 2 \times | D o m (d i m) | ^ {- 2}}{1 + D}\right)
$$

that is maximal when D is minimal (i.e. D = 2 for regular hierarchies). Due to the relationship encoded in Eq. (1), L will assume the maximal value. □

The IDC computed for the distance distributions reported in Fig. 3 is 67%, 40% and 6% respectively; the IDCs for the irregular hierarchies in Table 2 are directly reported in the table.

We emphasize that, given a hierarchical distance function, IDC is related to the hierarchy structure since it considers all the possible couples of leaf objects. Speci<sup>fi</sup>c data spaces, including only a subset of the possible values, could have a different distribution. Furthermore, we note that IDC quanti<sup>fi</sup>es the potential expressiveness of an HCD, but it is not related to its capability of correctly modeling the userperceived distance. We will argue on both these aspects in Section 6.

## 5.2. The multi-dimensional case

In d-dimensional HNODDSs, where data objects are characterized by several HCAs, the distance between two objects is typically computed composing the distance on the single hierarchies. In the following we will consider the family of distance functions obtained through a linear composition of mono-dimensional HCDs:

$$
D i s t (x, y) = \frac {\sum_ {i = 1} ^ {d} w _ {i} \times D i s t _ {h _ {i}} (x , y)}{\sum_ {i = 1} ^ {d} w _ {i}}\tag{10}
$$

where $D i s t _ { h _ { i } }$ is a mono-dimensional distance and $w _ { i } > 0$ is the weight hierarchy $h _ { i }$ has in the overall distance. Since the weights are the users' knobs to tune the multidimensional distance according to the relevance of the single HCA we can set, without loss of generality, $w _ { i } = 1$ for all the hierarchies.

We initially note that in the multidimensional case the HCD Dist(x,y) is no more an ultrametric but it is still a metric since linear composition does not preserve the strong triangular inequality property but it preserves the non-strong one. The <sup>fi</sup>rst part of this statement can be veri<sup>fi</sup>ed by a simple counterexample while we provide a formal proof for the second one.

Example. Let $d = 2$ and ∀ $i , w _ { i } = 1$ ; let $x , y , z \in \Delta$ three points such that D $i s t _ { h _ { 1 } } ( x , y ) = D i s t _ { h _ { 2 } } ( x , y ) = 3 , D i s t _ { h _ { 1 } } ( x , z ) = D i s t _ { h _ { 2 } } ( y , z ) = 3 \mathrm { a n d } D i s$ $t _ { h _ { 2 } } ( x , z ) = D i s t _ { h _ { 1 } } ( y , z ) = 2 .$ <sup>Þ ¼ ð Þ ¼ ð Þ ¼</sup>. The points respect the strong triangular <sup>ð Þ ¼ ð Þ ¼</sup>inequality on each dimension, while this is not the case for their linear combination since:

$$
\frac {3 + 3}{2} > \max \left(\frac {3 + 2}{2}, \frac {2 + 3}{2}\right).
$$

Theorem 5.2. Given a set of mono-dimensional HCD distances $D i s t _ { h _ { i } } ( x , y )$ on an HNODDS, their linear composition is a metric.

Proof. Let's initially consider that each mono-dimensional HCD respects all the metric properties for Theorem 4.2. Non-negativity is easily veri<sup>fi</sup>ed considering that $w _ { i } > 0 .$ . Symmetry is veri<sup>fi</sup>ed since the linear composition will sum up the same values due to the symmetry of the composing distances. Triangle inequality can be veri<sup>fi</sup>ed substituting in the inequality the distance de<sup>fi</sup>nition (see formula 10) and noting that the inequality is composed of d mono-dimensional partsw $\times D i s t _ { h _ { i } }$ $( x , y ) \leq w _ { i } \times D i s t _ { h _ { i } } ( y , z ) + w _ { i } \times D i s t _ { h _ { i } } ( x , z )$ <sup>-</sup>each respecting the inequality. <sup>ð Þ - ð Þ þ - ð Þ</sup>The sum of the left-hand sides and of the right-hand sides of the inequalities will respect it too. □

The discriminant capability of a multi-dimensional distance depend on both the discriminant capability of its mono-dimensional distances when applied to a speci<sup>fi</sup>c hierarchy and on the data distribution in the HNODDS. In this section we evaluate the <sup>fi</sup>rst factor from an analytical point of view, in Section 6 we will empirically study the second one. All the results reported in this section work under the assumption that mono-dimensional data distributions are mutually independent and that multidimensional objects are uniformly distributed in the data space. Under these assumptions the probability that two objects have a speci<sup>fi</sup>c distance i can be computed as follows:

$$
\begin{array}{l} P (D i s t (x, y) = i) \\ = \bigvee_ { \begin{array}{c} (i _ {1}.. i _ {d}) | i _ {z} \in D i s t _ {h _ {t}} \\ \wedge \sum_ {z = 1} ^ {d} i _ {z} = i \end{array} } P \Big (D i s t _ {h _ {1}} (x _ {1}, y _ {1}) = i _ {1} \Big) \wedge \dots \wedge D i s t _ {h _ {d}} ((x _ {d}, y _ {d}) = i _ {d}). \end{array}\tag{11}
$$

In other words, the probability of a distance i is computed summing up the probabilities of all the combinations of single hierarchy distances that sum up to i. Fig. 4 shows the distance distribution for HNODDSs characterized by an increasing number of the mono-dimensional hierarchies whose distributions are shown in Fig. 3. It is apparent that even in presence of a limited number of dimensions most of the distances are very high and that turns in a low discriminant capacity. To characterize such generic concept we will apply to our domain the concepts of curse of dimensionality and intrinsic dimensionality whose computations are enabled in our domain by Formula 11.

![](/api/attachments/9KYC7BS8/fulltext/images/a01531ec70b5ec7ff40070809fe296f09c2e8207f0d538dde39bf8c976cbc155.jpg)  
Fig. 4. Level-based distance distributions for different hierarchies.

## 5.2.1. Curse of dimensionality

We initially recall the important result discussed in Beyer et Al. [16] which shows that in high dimensional spaces nearest neighbor becomes unstable. More formally, [16] states that under certain rather general preconditions the difference between the distances from a query point y of the nearest and farthest points in a data space Δ becomes negligible:

$$
\lim _ {d \rightarrow \infty} P \left(\frac {D M a x \Delta}{D M i n _ {\Delta}} - 1 \leq \epsilon\right) = 1\tag{12}
$$

$$
\begin{array}{l} \text { where } D M i n _ {\Delta} = m i n (D i s t (x, y) | x, y \in \Delta), D M a x _ {\Delta} = m a x (D i s t (x, y) | x, y \\ \in \Delta). \end{array}
$$

[16] formalizes the phenomenon and provides a trend for d going to in<sup>fi</sup>nity but it does not quantify how fast the problem arises as dimensionality increases. Such trend can be analytically de<sup>fi</sup>ned as follows:

$$
\begin{array}{l} P (D M a x _ {\Delta} / D M i n _ {\Delta} \leq 1 + \epsilon) \\ = \sum_ {(i, j) | j \leq (1 + \epsilon) \times i} P (D M i n _ {\Delta} = i) \times P (D M a x _ {\Delta} = j). \end{array}\tag{13}
$$

Formula 13 can be computed in terms of $P ( D i s t ( x , y ) )$ as shown in Appendix A and it analytically describes how quick curse of dimensionality reduces the meaningfulness of nearest neighbor and distances. The probability value is inversely proportional to the discriminant capability of the distance functions and to the hierarchies expressiveness, while it is directly proportional to the data set cardinality (please note that data are assumed to be independently distributed with respect to hierarchies). Fig. 5 shows that the probability curse of dimensionality takes place for HNODDSs with an increasing dimensionality (see Fig. 3 for the distance distribution of the involved mono-dimensional hierarchies). We note that even in the best case $( \mathrm { i } . { \mathsf { e } } . L = 1 0 , | \Delta | =$ 100k) the probability of the ratio to be lower than 2 (i.e. ϵ = 1) go to 1 with 8 dimensions or more, and that in most cases nearest neighbor becomes unstable working with more than 4 dimensions. This is a tight limit on the expressiveness of HCDs when compared with

Euclidean distances where curse of dimensionality takes place considerably later [30].

## 5.2.2. Intrinsic dimensionality

It is well-known that proximity search algorithms degrade systematically as the data space dimensionality increases. Such trend is indeed related to the intrinsic dimension of the data space rather than its representational one. For example, if in a 50-dimensional vector space all points lie in a plane, smart search algorithms can behave like if searching on a two-dimensional space. Several authors tried to de<sup>fi</sup>ne the fuzzy concept of intrinsic dimensionality [28], in this paper we will refer to the one by Chavez et al. [30] since their de<sup>fi</sup>nition can be applied to general metric spaces, it is simply de<sup>fi</sup>ned in terms of statistical properties of the distance distribution, and it is cheap to estimate. Furthermore, intrinsic dimensionality is practically important since it allows to bound the complexity of the main similarity search algorithms [30].

Intrinsic dimensionality [30] The intrinsic dimensionality of a metric space is de<sup>fi</sup>ned as $\rho = \frac { \mu ^ { 2 } } { 2 \sigma ^ { 2 } }$ where μ and σ are the mean and the variance of its histogram of distances. In our case mean and variance can be computed as follows:

$$
\mu = \sum_ {i = 0} ^ {n D D} i \times P (D i s t (x, y) = i) \quad \sigma^ {2} = \sum_ {i = 0} ^ {n D D} (i - \mu) ^ {2} P (D i s t (x, y) = i).
$$

Intrinsic dimensionality grows with the mean and decreases with the variance of the distance distribution. Fig. 6 shows its values for data spaces with increasing dimensionality where distances are based on $D i s t ^ { L e v }$ . The trend can be better understood if compared with the one obtained on a data space with the same dimensionality where distances are based on the Euclidean distance $- ~ L _ { 2 } ( )$ . To obtain such data space each unordered label in the HNODDS has been mapped in an integer coordinate thus determining a multidimensional vector space. Intrinsic dimensionality emphasizes the low discriminant capability of the HNODDS with $\dot { D i } s t ^ { L e v }$ that is mainly induced by the low variance of the distance distribution. Such result will be re<sup>fl</sup>ected in a low performance of similarity search algorithms as shown in Section 6.3.

![](/api/attachments/9KYC7BS8/fulltext/images/9676de09760d476772abd3c8ad540abe0d79670d6da26fd1063a862ec229e1b2.jpg)

![](/api/attachments/9KYC7BS8/fulltext/images/eb5f879e0bb494d424ab521911ebf230133377b15c55e95ea972c57876d0973b.jpg)

![](/api/attachments/9KYC7BS8/fulltext/images/a4d3b0c7e5e9722b15e245c3aacbfe2756d09d7fb0dacbe930905887ed3c48fb.jpg)

![](/api/attachments/9KYC7BS8/fulltext/images/12aa242fd782a06e6aedf83af0efdbd5ad2169a3da9788d9c3716db1c9569589.jpg)  
Fig. 5. Probability of having $P ( D M a x _ { \Delta } / D M i n _ { \Delta } \leq 1 + \epsilon )$ for ϵ ranging in [0.5,3], for two different hierarchy con<sup>fi</sup>guration $( D = 2 , L = 1 0$ and $D = 4 , L = 5 )$ and two different data set sizes (|Δ| = 10k and $| \Delta | = 1 0 0 k )$ . The distance adopted is Dist<sup>Lev</sup>.

## 6. Empirical results and discussion

In this section we complete our analysis through a set of experi ments aimed at:

• appraising, independently from our statistical model, the ability of HCDs to catch object similarity (Section 6.1 and 6.2);

• evaluating the capability of our model and of the related indicators (i.e. IDC, Intrinsic dimensionality, Curse of dimensionality) to measure such ability (Section 6.1 and 6.3);

• analyzing the performance of HCD even on HNODDS characterized by non-uniformly distributed data that are not supported by our analytical model (Section 6.2 and 6.3);

• showing how our <sup>fi</sup>ndings can be used in practice by designers and researchers (Section 6.1 and 6.3).

The correctness of our model (i.e. Formulae 6, 7, 8 and 11) has been empirically veri<sup>fi</sup>ed on the data sets reported in Section 4. Each formula has been tested calculating, independently from the model, the real distance distributions of the data sets. These values have been obtained computing the all-against-all distances between the hierarchy leaf values <sup>fi</sup>rst, and then counting the actual number of couples of objects at distance i. Empirical results perfectly match the model ones. In the multidimensional case computing all the distances between objects is unfeasible, thus we took random samples with cardinality 1 k from a set of uniformly distributed HNODDSs with different dimensionalities and hierarchy features. The differences between the theoretical probability distributions and the data set ones are reported in Table 3 and are measured in terms of Average Relative Gap as de<sup>fi</sup>ned in Formula 14: Dist is the HCDs adopted, $P ( D i s t ( x , y ) = i )$ is the distance probability computed through our model and $\hat { P } ( D i s t ( x , y ) = i )$ is the corresponding probability derived from the all-against-all distance distribution on the random samples (i.e. ≈500,000 distances in our tests).

![](/api/attachments/9KYC7BS8/fulltext/images/288b1a076b9d840b13cde57f53879b2b1beb3cb530343bcf8fee348e9a3f84b2.jpg)  
Fig. 6. Intrinsic dimensionality for data spaces with increasing dimensionality. Values are reported for $| \Delta | = 1 0 0 k$ (data set objects follow a uniform distribution) and for both Dist<sup>Lev</sup> and $L _ { 2 }$ distances.

$$
\text { AvgRelGap } _ {\text { Dist }} = \sum_ {i = 0} ^ {n D D - 1} \frac {\left| P (\text { Dist } (x , y) = i) - \hat {P} (\text { Dist } (x , y) = i) \right|}{\hat {P} (\text { Dist } (x , y) = i)}.\tag{14}
$$

Noticeably, AvgRelGap is always lower than 4.4%, a very limited value considering the sampling process and that some of the measured probabilities are very low making the relative error more unstable.

## 6.1. HCD effectiveness

In previous sections we have shown that HCD capabilities in modeling distances between objects vary according to the hierarchy features and the speci<sup>fi</sup>c distance adopted. Here we verify how well HCDs match a natural concept of distance/similarity. This goal requires a benchmark with known similarities between its objects based on a globally accepted (i.e. objective) distance; to this end we will use the Euclidean distance between geographical points. Our benchmark is extracted from IPUMS, a public database storing census micro data for social and economic research [35]. The benchmark includes 1024 census blocks with known positions extracted from different states and USA regions. Blocks are grouped in an irregular hierarchy h with $L = 6$ as shown in Fig. 7. The goal is now to measure the capability of HCDs to capture the Euclidean distance, $D i s t _ { h } ^ { G e o }$ , between blocks. This can be achieved computing the correlation between the distances returned by $D i s t _ { h } ^ { G e o }$ and those returned by an HCD: a positive correlation means that high/low distances in $D i s t _ { h } ^ { G e o }$ correspond to high/low distances in the considered HCD. Since different distance functions are considered a normalization step is needed. As shown below a min–max normalization has been applied.

AvgRelGap for HNODDSs with different dimensionalities and regular hierarchies with different features. The distance function used is Dist<sup>Lev</sup>(x,y).

<table><tr><td></td><td>2-dim</td><td>8-dim</td><td>16-dim</td></tr><tr><td>D=2,L=10</td><td>3.63%</td><td>4.25%</td><td>2.89%</td></tr><tr><td>D=4,L=5</td><td>3.71%</td><td>3.55%</td><td>4.37%</td></tr></table>

![](/api/attachments/9KYC7BS8/fulltext/images/3e129db89f6971ba55ac7ad917f74d58bcf52725a68640667e0aa4be462594e6.jpg)  
Fig. 7. The geographical hierarchy: besides the blocks represented as dots, the map shows the levels Region (different colors), Subregion (different shades of the Region color) and, State (through their borders).

$$
\text { Normalize } (D i s t _ {h} (x, y)) = \frac {D i s t _ {h} (x , y) - D M i n _ {\Delta}}{D M a x _ {\Delta} - D M i n _ {\Delta}}.
$$

In the previous formula $\Delta$ is the Census data set and includes 1024 blocks. Correlation has been computed through the Pearson Coef<sup>fi</sup>cient:

$$
\operatorname{Corr} (V, W) = \frac {\sum_ {i} ^ {N} \left(v _ {i} - \bar {v}\right) \times \left(w _ {i} - \bar {w}\right)}{\sqrt {\sum_ {i = 1} ^ {N} \left(v _ {i} - \bar {v}\right) ^ {2} \times \sum_ {i = 1} ^ {N} \left(w _ {i} - \bar {w}\right) ^ {2}}}
$$

where V includes the set of all-against-all normalized $D i s t _ { h } ^ { G e o }$ values for blocks in $\Delta \left( N = \left| \Delta \right| \times \left( \left| \Delta \right| - 1 \right) \right)$ ), the same holds for W but here the normalized distances are computed using one of the HCDs discussed so far. More precisely, we considered $D i s t _ { h } ^ { L e \nu }$ and $D i s t _ { h } ^ { O c c }$ , plus two user-de<sup>fi</sup>ned HCDs, $D i s t _ { h } ^ { L e v U D F }$ and $D i s t _ { h } ^ { O c c U D F }$ where the role of function f in De<sup>fi</sup>nition 5 is taken by polynomial functions of degrees 4 and 3 respectively. Such functions approximate the non-linear increasing of geographical distances as the LCA becomes more general. Through such functions we encode the user knowledge about the domain. The following formulae report their de<sup>fi</sup>nitions, the parameter values have been determined through an optimization process.

$$
\begin{array}{l} \text { Dist } _ {h} ^ {\text { LevUDF }} (x, y) = 2. 9 \times 1 0 ^ {- 3} \times i ^ {4} - 0. 0 3 3 \times i ^ {3} + 0. 1 4 \times i ^ {2} - 0. 2 3 \times i + 0. 1 3 \\ \text { Dist } _ {h} ^ {\text { OccUDF }} (x, y) = 1 0 ^ {- 1 0} \times j ^ {3} - 4. 1 \times 1 0 ^ {- 7} \times j ^ {2} + 9. 9 \times 1 0 ^ {- 4} \times j - 1. 6 1 \times 1 0 ^ {- 3} \end{array}
$$

where $\dot { \iota } = l e v e l ( a t t r ( l c a ( x , y ) ) )$ ) and $j = | D e s c _ { d i m } ^ { a t t r ( l c a ( x , y ) ) } ( l c a ( x , y ) )$ |. Results are reported in Fig. 8 that compares the average normalized distance values between couple of points with an increasing LCA level.

We initially note that $D i s t _ { h } ^ { G e o }$ shows a non-linear trend since Block, Group and County are considerably more compact than State, Subregion and Region. As expected, distances returned by user-de<sup>fi</sup>ned functions are, in the average, the most effective (i.e. given two blocks x and y the distances returned are in the average the most similar to those returned by $D i s t _ { h } ^ { G e o } ( x , y ) )$ since the user-de<sup>fi</sup>ned functions correctly capture non-linearity.

The correlation values are reported in Table 4. It is apparent that, when all the hierarchy levels are exploited HCDs are strongly correlated with $D i s t _ { h } ^ { G e o }$ but, differently from what is shown in Fig. 8, the performances of all the considered HCDs appear to be quite close. A more in-depth analysis carried out considering IDC can explain such behavior. Similar IDC values imply that, independently from the returned absolute values, the HCDs have a similar capability in returning distinct values for distinct couples of blocks. Since this capability is similar and quite limited for all the HCDs considered, couples of blocks sharing the same hierarchical distance value may have their geographic distances spanning in a wide range thus impacting on the correlation values.

![](/api/attachments/9KYC7BS8/fulltext/images/a27b98f2ba2553188b4917caf03d0c0835dfdd031d4e2aebd585733011892365.jpg)  
Fig. 8. Average normalized distance between couple of points having their LCA at different levels of the geographical hierarchy. Values are computed using the Euclidean distance $( D i s t _ { h } ^ { G e o } )$ and a set of HCDs.

Correlation with $D i s t ^ { G e o }$ and IDC for a set of HCDs. Values are computed for both the full hierarchy h in Fig. 8 and for a simpli<sup>fi</sup>ed version h′ where two out of seven levels have been dropped.

<table><tr><td rowspan="2">Distance</td><td colspan="2">h (7 levels)</td><td colspan="2">h&#x27; (5 levels)</td></tr><tr><td>Corr</td><td>IDC</td><td>Corr</td><td>IDC</td></tr><tr><td> $Dist^{Lev}$ </td><td>0.595</td><td>45.3%</td><td>0.33</td><td>11.9%</td></tr><tr><td> $Dist^{Occ}$ </td><td>0.635</td><td>46.5%</td><td>0.36</td><td>11.9%</td></tr><tr><td> $Dist^{UdfLev}$ </td><td>0.637</td><td>45.3%</td><td>0.36</td><td>11.9%</td></tr><tr><td> $Dist^{UdfOcc}$ </td><td>0.636</td><td>46.5%</td><td>0.36</td><td>11.9%</td></tr></table>

Table 4 also shows the effect of reducing the hierarchy expressiveness by removing two out of seven hierarchy levels. Once again we note that the number of levels plays the most important role in de<sup>fi</sup>ning the hierarchy expressiveness that is strongly reduced with less than <sup>fi</sup>ve attributes. We <sup>fi</sup>nally note the IDC correctly models attribute discriminant capacity since it properly varies with the correlation levels.

Results in Table 4 exemplify how IDC can be practically exploited. It enables an in-depth comparison of the performances of different distances and it allows in evaluating the impact of a design choice (e.g. using 7 vs. 5 levels in the hierarchy). In both cases evaluations are based on an objective measure (i.e. without the need of users that manually tag similarity levels).

## 6.2. Discriminant capacity in HNODDS with non-uniformly distributed data

The model proposed in Section 5.2 works under the assumption that mono-dimensional data distributions are mutually independent and that multidimensional objects are uniformly distributed in the data space. In the following we will empirically study the discriminant analysis of HCDs in the general case. To this end we created a set of multidimensional data sets where objects are distributed according to multidimensional Gaussian distributions centered on speci<sup>fi</sup>c points in the data space. Fig. 9 shows two examples for the 2-dimensional data space. Our data sets differ in the number of dimensions, that ranges from 2 to 16, in the structure of the hierarchies whose levels vary between 5 and 10 (the cardinality of dim is fixed to 1024), and in the skewness and distances of the object distributions. All the tests have been carried out ten times in order to avoid distortions due to sampling.

Fig. 10 shows, for the different data sets, the distance distributions computed from the all-against-all distances between objects. The presence of clusters of points determine a more uniform distribution of distances with respect to the ones determined by data sets including uniformly distributed objects (see Fig. 4) and this implies a higher capability in identifying similar/dissimilar objects as con<sup>fi</sup>rmed by Figs. 11 and by 13. It is easy to verify that up to 8 dimensions the probability of having the distance to the farthest object to be double to the nearest one $( \mathrm { i . e . ~ } \epsilon = 1 )$ is high. Conversely, similarity remains an ill de<sup>fi</sup>ned concept when working with a 16-dimensional data space.

## 6.3. Range query effectiveness

We close this section with a brief analysis on the effectiveness of range queries when HCAs and HCDs are involved. Although it is out of the scope of this paper the evaluation of speci<sup>fi</sup>c types of queries, we believe that such analysis can be useful to prove that the models, the indicators and more in general the results provided are correct and aligned to practical evidences.

A range query is a popular database operation that retrieves all data objects whose distance is lower than a given threshold from a query point. The effectiveness of a range query can be better understood if compared with a similar query run on a multidimensional vector space data space, with the same dimensionality, where distances are based on the Euclidean distanc $\mathrm { ~ : ~ } - L _ { 2 } ( )$ . To obtain this second data space each unordered label in the HNODDS has been mapped on an integer coordinate. We run the test on both the HNODDS with uniformly distributed data used in Section 5 and on the one with Gaussian distributed data used in the current section. The distance function used is $D i s t ^ { L e \nu }$ . As in [30] we considered a simple pivot-based indexing technique based on random pivots and we run a set of similarity search queries in data spaces with increasing dimensionality.

As to range queries on uniformly distributed data Fig. 12 shows the costs (expressed in number of distance calculations) for retrieving a <sup>fi</sup>xed, small, fraction of neighbors in a data set with $| \Delta | = 1 0 0 k 0 \mathrm { b j e c t s } .$ It becomes apparent that the ef<sup>fi</sup>ciency of the search algorithm degenerates with more than 2 dimensions, while similarity becomes unstable with 8 dimensions since the distance range must be set to 6.5 out of 10 to return a non-empty result-set (i.e. all the data objects are far: curse of dimensionality takes place). This result perfectly matches with the one in Fig. 5 that shows that, in an 8-dimensional data space, it is very unlikely to <sup>fi</sup>nd two objects with distance lower or equal to 5 (i.e. ϵ = 1 and $D M A X _ { \Delta } = 1 0 )$ ). Besides empirically proving the correctness of our model, this test is a further example about its practical use: instead of implementing the similarity search system a designer could have a precise estimate of its effectiveness just computing Formula 13 exploiting the model.

As to range queries on data spaces with Gaussian distributed data Fig. 14 con<sup>fi</sup>rms that range queries can be ef<sup>fi</sup>ciently carried out with no more than 4 dimensions. This result is aligned with the results in Figs. 11 and 13, where, in case of 4 dimensions, the low probabilities of $P ( D M a x _ { \Delta } / D M i n _ { \Delta } \leq 1 + \epsilon )$ for all the ϵ values, denote that the neighborhood of a point is suf<sup>fi</sup>ciently large to effectively apply the cut condi tion of the pivot-based search algorithm.

![](/api/attachments/9KYC7BS8/fulltext/images/5d6f824d2620366e9093a27a68fb9647433e453fd003ed9241aa8db91596908f.jpg)  
Fig, 9. 2-dimensional data sets. Both of them include ten thousand obiects distributed according a Gaussian distribution with different variances

![](/api/attachments/9KYC7BS8/fulltext/images/7cb8939ae9ac633f118a27ee980c8df8fe6bf9d6802d2d24009370d53172a5cc.jpg)  
Fig. 10. Distance distributions for HNODDS with different dimensionalities and different hierarchy types.

## 6.4. Guidelines for designers

Data warehouse design is ruled by a set of criteria aimed at maximizing ef<sup>fi</sup>ciency and expressiveness of the multidimensional schema [4]. The need of computing the distance between cells determines additional criteria the designer must consider during the design phase. In the following, based on the outcomes of the present research, we propose a set of rules of thumb that can be used as a baseline for obtaining an effective design:

• The hierarchies involved in the HCD should be known at design time in order to in<sup>fl</sup>uence the multidimensional schema structure.

• Include in the hierarchy as many levels as available: the height of hierarchy largely determines the level of detail the distance between points can be computed.

• The evaluation of the effectiveness of two alternative hierarchy structures can be quantitatively carried out using the IDC index.

• User-de<sup>fi</sup>ned functions should be considered whenever the distance between objects varies in a non-linear fashion through different levels of the hierarchy.

• Distance functions exploiting more than four hierarchies are useless if data are uniformly distributed. In these cases a feature selection approach should be adopted to limit the number of hierarchies the HCD considers. Obviously, such choice implies a trade-off between the structural discriminant capacity of the hierarchy and its relevance to the natural concept of distance in the speci<sup>fi</sup>c domain.

![](/api/attachments/9KYC7BS8/fulltext/images/aaf99886b4873d07f1f3ca1fc1a9634e133be9aa1f95cda8d6e41816bdc51006.jpg)

![](/api/attachments/9KYC7BS8/fulltext/images/d7ae625f204a9ed2400a18286b5a3dda40737e3abefb4a0b1195fcc7a91e98f7.jpg)

![](/api/attachments/9KYC7BS8/fulltext/images/36be4eb057137d5a7f09632013ae5997446e3599df783f0612fe029047b34faf.jpg)

![](/api/attachments/9KYC7BS8/fulltext/images/99611db30a2448cb5f63fec1924dcd17b6d3f9e8b9aa61280a4240a0ac49e465.jpg)  
Fig. 11. Probability of having $P ( D M a x _ { \Delta } / D M i n _ { \Delta } \leq 1 $ + ϵ) for 4 data sets with different sizes $( | \Delta | = 1 0 k \mathrm { a n d } | \Delta | = 1 0 0 k )$ and structure of the hierarchies (D = 2,L = 10 and D = 4, L = 5). Data set objects follow a gaussian distribution with $\sigma ^ { 2 } = 2 5 , \epsilon \in [ 0 . 5 , 3 ] .$

![](/api/attachments/9KYC7BS8/fulltext/images/d1ce1c41cb689784a16db44fde1644238465fb5b95f941c17b029d9b2e95f52c.jpg)  
Fig. 12. Range query costs in data spaces with increasing dimensionality using a pivotbased algorithm. Costs are reported for a uniformly distributed data set with cardinality 100 k and with hierarchy parameters D = 2 and L = 10. The range query radius is adjusted to retrieve the 0.01% of the neighbors.

• When selecting the features/hierarchies to be involved in the HCD the designer should prefer those subsets that induce clusters in the multidimensional data that, in turn, delay the effects of the curse of dimensionality.

## 7. Conclusions

In this paper we analyzed the discriminant capabilities of the family of hierarchical computable distances when applied to a single hierarchical and categorical attribute or to a multi-dimensional HNODDS. The evidences obtained from the proposed analytical model and the empirical experiments prove that, hierarchical computable distances properly model the distance between data objects but their discriminant capacity is quickly reduced as dimensionality increases. This problem arises much earlier than in numerical data spaces where, for example, the $L _ { k }$ metric family can be adopted. The problem is due to the intrinsic disorder of categorical data that is only partially recovered by the additional information provided by hierarchical relationships. Starting from this intuition we gave a formal de<sup>fi</sup>nition of intrinsic discriminant capacity when applied to a speci<sup>fi</sup>c hierarchical and categorical attribute and we used such de<sup>fi</sup>nition to formally derive the hierarchy features that provide the optimal performances.

![](/api/attachments/9KYC7BS8/fulltext/images/18129c9277fba0ada2ebe9fc6086acd898000fbdd1c3305f3138e2312b909c9e.jpg)  
Fig. 14. Range query costs in data spaces with increasing dimensionality using a pivotbased algorithm. Costs are reported for a Gaussian distributed data set with cardinalit 100 k and with hierarchy parameters D = 2 and L = 10. The range query radius is adjusted to retrieve the 0.01% of the neighbors.

Our future works concern the study of techniques that can delay the occurrence of curse of dimensionality. In particular, we are currently studying how approaches based on Shared-Neighbor and dimensional projection can be applied to HNODDSs with speci<sup>fi</sup>c data distributions. We are also working toward reducing the computational complexity of multidimensional range queries, by extending the computation tech nique we proposed for the mono-dimensional case to the multidimensional one.

## Acknowledgment

Thanks to Paolo Ciaccia for his comments and discussion of these ideas.

![](/api/attachments/9KYC7BS8/fulltext/images/2293229b1ee2d705a4b2f735230ed6aede6b3646013b64831730624bc4bea78f.jpg)

![](/api/attachments/9KYC7BS8/fulltext/images/359bd26b75a272d5b7410dd81ce633c7740e6683a5e800c9a3214efd0a1e8718.jpg)

![](/api/attachments/9KYC7BS8/fulltext/images/d5cbb154a157b2990eea1d64f660360daf5cadb8b0b4198e58db863eaea924fb.jpg)

![](/api/attachments/9KYC7BS8/fulltext/images/bc6d3a2a7dae4c9d9b9ac0c30fc721dbdc19cb7b5805fe79f0b5111c48479afc.jpg)  
Fig. 13. Probability of having $P ( D M a x _ { \Delta } / D M i n _ { \Delta } \leq 1 $ + ϵ) for 4 data sets with different sizes $( | \Delta | = 1 0 k \mathrm { a n d } | \Delta | = 1 0 0 k )$ and structure of the hierarchies $( D = 2 , L = 1 0$ and $D = 4 , L = 5 )$ . Data set objects follow a gaussian distribution with $\sigma ^ { 2 } = 5 0 , \epsilon \in [ 0 . 5 , 3 ] .$

Appendix A. Derivation for $P ( D M a x _ { \Delta } / D M i n _ { \Delta } \leq 1 + \epsilon )$

Let $P ( D M a x _ { \Delta } / D M i n _ { \Delta } \leq 1 + \epsilon )$ be the probability of the ratio between the maximum and minimum distance in the data set Δ to be lower or equal to $1 + \epsilon { : }$

$$
P (D M a x _ {\Delta} / D M i n _ {\Delta} \leq 1 + \epsilon) = \sum_ {(i, j) | j \leq (1 + \epsilon) \times i} P (D M i n _ {\Delta} = i) \times P (D M a x _ {\Delta} = j)
$$

where:

$$
\cdot P (D M i n _ {\Delta} = i) = P (\exists (x, y) \in \Delta | D i s t (x, y) = i \wedge \nexists (v, w) \in \Delta | D i s t (v, w) <   i);
$$

$$
\cdot P (D M a x _ {\Delta} = j) = P (\exists (x, y) \in \Delta | D i s t (x, y) = j \land \nexists (v, w) \in \Delta | D i s t (v, w) > j).
$$

The previous formula can be expressed in terms of $P ( D i s t ( x , y ) )$ ) as follows:

$$
\begin{array}{l} P (D M i n _ {\Delta} = i) = P (\exists (x, y) \in \Delta | D i s t (x, y) = i) \\ \qquad \times \prod_ {h = 0} ^ {h <   i} P (\not \exists (v, w) \in \Delta | D i s t (v, w) = h) \end{array}\tag{A.1}
$$

$$
\begin{array}{l} P (D M a x _ {\Delta} = j) = P (\exists (x, y) \in \Delta | D i s t (x, y) = j) \\ \qquad \times \prod_ {h = j + 1} ^ {d} P (\not \exists (v, w) \in \Delta | D i s t (v, w) = h). \end{array}\tag{A.2}
$$

Finally, the existential quanti<sup>fi</sup>er in the two formulas can be then expressed applying the Cardenas' formula to the distance distribution:

$$
\begin{array}{l} P (\exists (x, y) \in \Delta | D i s t (x, y) = i) = 1 - (1 - P (D i s t (x, y) = i)) ^ {| \Delta |} \\ P (\nexists (v, w) \in \Delta | D i s t (v, w) = h) = (1 - P (D i s t (v, w) = h)) ^ {| \Delta |}. \end{array}
$$

## References

[1] S. Boriah, V. Chandola, V. Kumar, Similarity measures for categorical data: a comparative evaluation, Proc. SIAM Int. Conf. on Data Mining, 2008, pp. 243–254.

[2] G. Qian, Q. Zhu, Q. Xue, S. Pramanik, Dynamic indexing for multidimensional nonordered discrete data spaces using a data-partitioning approach, ACM Transactions on Database Systems 31 (2) (2006) 439–484.

[3] P. Zezula, G. Amato, V. Dohnal, M. Batko, Similarity Search: The Metric Space Approach, Springer, 2002.

[4] M. Golfarelli, S. Rizzi, Data Warehouse Design: Modern Principles and Methodologies McGraw-Hill.2009

[5] Y. Li, Z. Bandar, D. McLean, An approach for measuring semantic similarity between words using multiple information sources, IEEE Transactions on Knowledge and Data Engineering 15 (4) (2003) 871–882.

[6] T. Pedersen, S.V.S. Pakhomov, S. Patwardhan, C.G. Chute, Measures of semantic similarity and relatedness in the biomedical domain, Journal of Biomedical Informatics 40 (3) (2007) 288–299.

[7] E. Baikousi, G. Rogkakos, P. Vassiliadis, Similarity measures for multidimensional data. Proc. ICDE. 2011, pp. 171–182.

[8] P. Tan, M. Steinbach, V. Kumar, Introduction to Data Mining, Addison-Wesley, 2005

[9] T. Skopal, B. Bustos, On nonmetric similarity search problems in complex domains, ACM Computing Surveys 43 (4) (October 2011) 34:1–34:50.

[10] E. Eskin, A. Arnold, M. Prerau, L. Portnoy, S. Stolfo, A Geometric Framework for Unsupervised Anomaly Detection, Kluwer Academic Publishers. 2002.

[11] K.S. Jones, A statistical interpretation of the term speci<sup>fi</sup>city and its application in retrieval, Journal of Documentation 28 (1) (1972) 11–21.

[12] D. Goodall, A new similarity index based on probability, Biometrics 22 (1966) 882–907.

[13] P. Ganesan, H. Garcia-Molina, J. Widom, Exploiting hierarchical domain structure to compute similarity, ACM Transactions on Information Systems 21 (1) (2003) 64–93.

[14] G. Salton, A. Wong, C. Yang, A vector space model for automatic indexing, Communications of the ACM 18 (November 1975) 613–620.

[15] S. Lin, D.E. Brown, An outlier-based data association method for linking criminal incidents, Decision Support Systems 41 (3) (2006) 604–615.

[16] K. Beyer, J. Goldstein, R. Ramakrishnan, U. Shaft, When is “nearest neighbor” meaningful? Proc. ICDT, 1999, pp. 217–235.

[17] C.C. Aggarwal, A. Hinneburg, D.A. Keim, On the surprising behavior of distance metrics in high dimensional spaces, Proc. ICDT, 2001, pp. 420–434.

[18] A. Hinneburg, C.C. Aggarwal, D.A. Keim, What is the nearest neighbor in high dimensional spaces? Proc. VLDB, 2000, pp. 506–515.

[19] M.E. Houle, H.P. Kriegel, P. Kröger, E. Schubert, A. Zimek, Can shared-neighbor distances defeat the curse of dimensionality? Proc. SSDBM, 2010, pp. 482–500.

[20] G. Moise, A. Zimek, P. Kröger, H.P. Kriegel, J. Sander, Subspace and projected clustering: experimental evaluation and analysis, Knowledge and Information Systems 21 (3) (2009) 299–326.

[21] H.P. Kriegel, P. Krï¿½ger, E. Schubert, A. Zimek, A general framework for increasing the robustness of PCA-based correlation clustering algorithms, Proc. SSDBM, 2008.

[22] E. Müller, S. Günnemann, I. Assent, T. Seidl, Evaluating clustering in subspace projections of high dimensional data, PVLDB 2 (1) (2009) 1270–1281.

[23] H.P. Kriegel, P. Kröger, A. Zimek, Clustering high-dimensional data: a survey on subspace clustering, pattern-based clustering, and correlation clustering, TKDD 3 (1) (2009).

[24] E. Müller, I. Assent, U. Steinhausen, T. Seidl, Outrank: ranking outliers in high dimensional data, ICDE Workshops, 2008, pp. 600–603.

[25] H.P. Kriegel, M. Schubert, A. Zimek, Angle-based outlier detection in highdimensional data, Proc. KDD 2008, 2008, pp. 444–452.

[26] C.C. Aggarwal, P.S. Yu, On high dimensional indexing of uncertain data, Proc. ICDE 2008, 2008, pp. 1460–1461.

[27] M.E. Houle, J. Sakuma, Fast approximate similarity search in extremely highdimensional data sets, Proc. ICDE, 2005, pp. 619–630.

[28] V. Pestov, An axiomatic approach to intrinsic dimension of a dataset, Neural Networks 21 (2–3) (2008) 204–213.

[29] D. Mo, S.H. Huang, Fractal-based intrinsic dimension estimation and its application in dimensionality reduction, IEEE Transactions on Knowledge and Data Engineering 24 (2012) 59–71.

[30] E. Chávez, G. Navarro, R.A. Baeza-Yates, J.L. Marroquín, Searching in metric spaces, ACM Computing Surveys 33 (3) (2001) 273–321.

[31] R. Roy, M. Hafedh, B. Ellen, B. Maria, Development and application of a metric on semantic nets, IEEE Transactions on Systems, Man, and Cybernetics 19 (1) (1989) 17–30.

[32] C.C. Hsu, Y.P. Huang, Incremental clustering of mixed data based on distance hierarchy, Expert Systems with Applications 35 (3) (2008) 1177–1185.

[33] P. Buneman, A note on the metric properties of trees, Journal of Combinatorial Theory, Series B 17 (August 1974) 48–50.

[34] T. Faver, K. Kochalski, M. Murugan, H. Verheggen, E. Wesson, A. Weston, Classi<sup>fi</sup>cations of ultrametric spaces according to roundness, ArXiv e-prints, January 2012.

[35] Minnesota Population Center, Integrated public use microdata series, http://www. ipums.org 2008.

Matteo Golfarelli received his Ph.D. for his work on autonomous agents in 1998, In 2000 he joined the University of Bologna as a researcher. Since 2005 he is Associate Professor, teaching Information Systems, Database Systems and Data Mining, He has published over 80 papers in refereed journals and international conferences in the fields of data warehousing, pattern recognition, mobile robotics, multi-agent systems. He is co-author of the book Data Warehouse Design: Modern Principles and Methodologies. He served in the PC of several international conferences and as a reviewer in journals. Matteo Golfarelli has been co-chair of DOLAP 2012, he is permanent co-chair of the Business Information System conference; he is member of the editorial board of the International Journal of Data Mining, Modelling and Management (IJDMMM). His current research interests include all the aspects related to business intelligence and data warehousing, in particular multidimensional modeling, Business Intelligence on Social Data and Data Mining.

Elisa Turricchia received her degree cum laude in Computer Science from the University of Bologna, Italy, in March 2009, presenting a thesis about interoperability issues among heterogeneous data warehouse systems. In 2012 she received her Ph.D. for her work on Pervasive Business Intelligence. Her current research interests include the study of methods for expressing and executing OLAP preference queries and for managing distributed data warehouses. She has published 8 papers in refereed journals and international conferences on these topics.
