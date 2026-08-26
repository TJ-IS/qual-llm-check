---
otero_id: 378
otero_key: "PWBHUM8Y"
title: "Using domain-specific knowledge in generalization error bounds for support vector machine learning"
authors: "Enes Eryarsoy; Gary J. Koehler; Haldun Aytug"
year: "2009"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2008.09.001"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Using domain-speci<sup>fi</sup>c knowledge in generalization error bounds for support vector machine learning

Enes Eryarsoy <sup>a,</sup>⁎, Gary J. Koehler <sup>b</sup>, Haldun Aytug

<sup>a</sup> Faculty of Management, Sabanci University, of Management, Sabanci University, Orhanli, Istanbul, 34956, Turkey

<sup>b</sup> Department of Information Systems and Operations Management, Warrington College of Business, University of Florida, 351 STZ, P.O. Box 117169, Gainesville, Florida 32611-7169, USA

## a r t i c l e i n f o

Article history: Received 12 September 2007 Received in revised form 8 August 2008 Accepted 4 September 2008 Available online 11 September 2008

Keywords: Prior knowledge Support vector machines Ellipsoid method Error bounds Fat-shattering dimension

## a b s t r a c t

In this study we describe a methodology to exploit a speci<sup>fi</sup>c type of domain knowledge in order to <sup>fi</sup>nd tighter error bounds on the performance of classi<sup>fi</sup>cation via Support Vector Machines. The domain knowledge we consider is that the input space lies inside of a speci<sup>fi</sup>ed convex polytope. First, we consider prior knowledge about the domain by incorporating upper and lower bounds of attributes. We then consider a more general framework that allows us to encode prior knowledge in the form of linear constraints formed by attributes. By using the ellipsoid method from optimization literature, we show that, this can be exploited to upper bound the radius of the hyper-sphere that contains the input space, and enables us to tighten generalization error bounds. We provide a comparative numerical analysis and show the effectiveness of our approach.

© 2008 Elsevier B.V. All rights reserved.

## 1. Introduction

Many knowledge discovery applications rely on machine learning algorithms. Using a training set of examples, a learning machine chooses one of a set of hypotheses to predict labels of unseen cases. For the pattern recognition task, the learning ability of a learning machine corresponds to how well the algorithm is calibrated to classify off-the set examples (OTS). This ability is called the “generalization ability of the learning machine.” An ideal learning machine would require less effort (i.e., fewer training points and a fast training process) and produce good quality results (i.e., good generalization ability).

Classi<sup>fi</sup>cation algorithms such as neural networks [13], decision trees [36], and Support Vector Machines (SVMs) [33] have been used on a number of pattern recognition problems successfully. A classi<sup>fi</sup>cation algorithm that performs extremely well on one task may fail to perform well on another. In the literature, this phenomenon is captured by the “No free lunch” (NFL) theorems [40]. Loosely speaking, the NFL theorems prove that unless domain knowledge is incorporated in the learning process, no learning machine can out-perform another, in general. Note that incorporating domain knowledge may not be suf<sup>fi</sup>cient to escape NFL but it is necessary.

In this study we focus on SVMs which have a strong theoretical underpinning in statistical learning theory [34,35]. SVMs have been applied in many areas including going concern opinions [22], web page <sup>fi</sup>ltering [7], document <sup>fi</sup>ltering [30], credit rating [14,32] and many others [8]. Research on incorporating domain knowledge in SVMs is still in its infancy [4].

In this paper we look at general methods to incorporate domain knowledge into SVMs and study the impact on their generalization ability. As we review below, some attempts have been made to incorporate speci<sup>fi</sup>c knowledge about a domain into SVMs. These approaches are interesting but do not generalize. The main approach has been to capture domain knowledge by the choice/design of kernel functions. However, it is important to note that the majority of such studies have made use of generic kernels such as Gaussian, polynomial, and radial basis function to incorporate domain knowledge but lack any speci<sup>fi</sup>c reason why they might perform well for these domains. Generating kernels tailored to problems in hand often requires trial and error methods and suffers from a lack of a priori knowledge for the problem domain.

We propose an approach where knowledge about the domain can be used to sharpen theoretical bounds on SVMs's generalization ability. Generalization error bounds in SVMs are based on probably approximately correct (PAC) learning theory [31]. There has been signi<sup>fi</sup>cant work on developing generalization error bounds. The bestknown and earliest bounds are based on VC-dimension due to [35]. However, these bounds only consider separability of class instances, and do not take into account the ease of separation. Other well-known error bounds, e.g., the fat-shattering dimension [1] and luckiness framework [28] bounds, capture these ideas.

In this study, we show how incorporating domain knowledge can improve the generalization error bounds that are based on the fatshattering dimension and the luckiness framework. We consider two forms of domain knowledge. First, we assume the instance space is bounded by a known hyper-rectangle. For example, if we know bounds on the attributes of the instances under consideration, we have such a hyper-rectangle. Second, we consider the case where the input space is contained in a bounded polyhedron (i.e., a polytope). This is possible whenever the input space is bounded. Our results also show that even when the input space cannot be bounded, translating the training set (i.e., re-centering it) at the origin tightens the bounds.

From a business point of view, an immediate implication of our results is that one can achieve the same level of con<sup>fi</sup>dence with a smaller dataset when the dataset is contained in a polytope compared to one that is not. Most often business and demographic data are bounded from below and above (e.g., age, family size, income, education level, etc.), and some of the attributes are bounded by linear relationships (e.g., consider the items of a balance sheet or income statement), and therefore can make use of our results. For example, many companies pay large sums on data collection. A signi<sup>fi</sup>cant portion of this expense is proportional to the size of the dataset to be collected (typically companies pay \$5 to as high as \$100 per completed survey). Our study can help organizations lower such costs by requiring a smaller dataset without sacri<sup>fi</sup>cing generalization ability.

The remainder of this paper is organized as follows (notation is summarized in Table 1). In Section 2 we provide a literature review. Section 3 provides a theoretical background of our framework to encode prior knowledge in SVMs, followed by computational experiments in Section 4. Section 5 is dedicated to summary, discussion about limitations, and future extensions.

## 2. Literature review

The NFL theorems have caused a good deal of excitement in machine learning research when they <sup>fi</sup>rst were released. Wolpert [37,38] studies the NFL theorems for learning and claims that a learning methodology that depends only on low empirical misclassi<sup>fi</sup>cation rate, small VCdimension, and a large training set cannot guarantee a small generalization error. In summary, there are two claims [39]. One, for a learning algorithm there are as many situations in which it is superior to another algorithm as vice versa. Two, the generalization performance depends on how much the selected classi<sup>fi</sup>er based on prior belief, or sample set actually coincides with the posterior distribution, or target function. According to NFL, no learning algorithm performs better than random guessing over all possible learning situations. To avoid these problems, it is necessary to incorporate domain knowledge into the induction process. To the best of our knowledge, there is no study that incorporates domain knowledge to compute error bounds. Below, we brie<sup>fl</sup>y mention domain knowledge-related SVMs literature. The literature contains three primary ways:

Table 1 Summary of notation

<table><tr><td> $Fat_{F}$ </td><td>Fat shattering dimension</td></tr><tr><td>X</td><td>Input space</td></tr><tr><td>d</td><td>VC dimension</td></tr><tr><td>l</td><td>Number of examples in the training set</td></tr><tr><td>δ</td><td>Level of significance</td></tr><tr><td>h∈H</td><td>A hypothesis/classifier h in the hypothesis space H</td></tr><tr><td>f∈F</td><td>Selected eligible classifier f in the set of eligible classifiers F</td></tr><tr><td>|H|</td><td>Cardinality of the hypothesis space</td></tr><tr><td>D</td><td>An arbitrary probability distribution</td></tr><tr><td>S</td><td>Training set</td></tr><tr><td>γ</td><td>Margin of the separating hyperplane with respect to a training set S</td></tr><tr><td>SD</td><td>Length of the space diagonal</td></tr><tr><td>P⊆Rn</td><td>n-dimensional polytope P</td></tr><tr><td>R</td><td>Polytope diameter</td></tr><tr><td>R</td><td>Upper bound on the polytope diameter</td></tr><tr><td>K⊆Rn</td><td>n-dimensional convex body</td></tr><tr><td>D</td><td>An nxn positive semi-definite symmetric matrix (characteristic matrix of the ellipsoid)</td></tr><tr><td>E(D,d)</td><td>Ellipsoid characterized by D, and centered at d.</td></tr><tr><td>λi</td><td>ith eigenvalue of D</td></tr><tr><td>α</td><td>A parameter that controls the depth of the cut (smaller for shallow, larger for deep cuts)</td></tr><tr><td>HR</td><td>Hyper-rectangle</td></tr><tr><td>ubm</td><td>Upper bound on the metric diameter of the polytope</td></tr></table>

• Incorporating domain knowledge with kernels

• Incorporating domain knowledge explicitly (e.g. in SVMs formulation)

• Studying the theoretical impact of domain knowledge on learning.

Kernels represent the main method of capturing domain knowledge. In theory, kernels have a great potential to tailor SVMs learning to the problem on hand. However, many SVM applications using kernels merely compare different generic kernels in terms of their relative performances. These incorporate domain knowledge by accident, at best.

An alternative is to build kernels that re<sup>fl</sup>ect speci<sup>fi</sup>c domain knowledge. In an earlier study, [27], domain knowledge is incorporated to construct task-speci<sup>fi</sup>c kernels for image classi<sup>fi</sup>cation. Several other studies focused on building task-speci<sup>fi</sup>c kernels. For example [17], and [18] build domain-speci<sup>fi</sup>c kernels for text categorization. Barzilay and Brailovsky [3] studied data domain description in SVMs learning. Another example on task speci<sup>fi</sup>c kernels in the SVMs literature is latent semantic kernels [9]. Cecchini [6] developed a kernel for <sup>fi</sup>nancial applications.

Another alternative approach is to inject domain knowledge directly into the SVMs formulation. To the best of our knowledge, this idea was <sup>fi</sup>rst introduced by Fung et al. [11]. In their study, domain knowledge was explicitly introduced to the formulation of a linear SVMs classi<sup>fi</sup>er in the form of polyhedral sets. Each polyhedron represents a set of points that are known to belong to a speci<sup>fi</sup>c class whether these points are in the sample set or not. With the help of such domain knowledge, an instance that is included in one of these sets is automatically classi<sup>fi</sup>ed correctly. Each of the polyhedral sets, called a knowledge set for a speci<sup>fi</sup>c class, is incorporated into the SVMs formulation. The SVMs formulation incorporating domain knowledge is slightly different since the constraint set now includes polyhedral sets, and the resulting hyperplane is found to be signi<sup>fi</sup>cantly different than that found with a standard SVMs. One of the advantages of their approach is that the proposed method has the potential of replacing missing training data with prior knowledge in terms of knowledge sets. However, from their study it can be observed that the shape of the knowledge-set-dependent hyperplane is different from a no-knowledge-set-dependent hyperplane only when at least one of the knowledge sets contains a point that could be a support vector.

In a follow-up study, Fung et al. [10] studied incorporating prior knowledge in the formulation of non-linear kernels. They illustrated the power of prior knowledge on a checkerboard example. With 16 points, each located at the center of 16 squares, and showed that including prior knowledge about two of the sixteen squares and using a Gaussian kernel, the accuracy dramatically increased to a level which can be achieved by as many as 39,000 training points and no prior knowledge. One must note that this remarkable improvement is due to and subject to the availability of very particular knowledge of the domain.

Le et al. [21] take a complementary approach to the work done by Fung et al. [10] and consider the case where a knowledge set violates linear separability. They form knowledge sets by using prior knowledge to modify the hypothesis space rather than the optimization problem.

In real life datasets the knowledge sets assumed by Fung et al. [10] might not be available or might be recondite due to the problem's nature. For example, for complex input spaces, knowledge sets may be dif<sup>fi</sup>cult to observe. Moreover, even when they are available, they might not affect or improve the results as they may incorporate inessential knowledge (i.e., the knowledge sets that lie further from the separating hyperplane than training points). Intuitively, the ef<sup>fi</sup>ciency of such <sup>fi</sup>nedrawn knowledge sets requires an abundance of prior information and their encodability. Due to these reasons the applicability might be limited in many domains. At the very least, this is a very speci<sup>fi</sup>c use of apriori knowledge. We propose an approach requiring less knowledge where rather general information about the input space is taken into account.

The third approach to incorporating domain knowledge is to consider its theoretical impact on learning. Within the SVMs context, Niyogi et al. [24] study “prior information” from the suf<sup>fi</sup>ciency of size of the training set. They show that in the absence of prior information, a larger training set might be needed to learn well.

In this paper we focus on generalization error bounds, and we assume that we know general [linear] properties about the attributes of the problem regardless of the class membership, that involve all points of the problem. We investigate the impact of this knowledge on learning bounds. In order to introduce our approach, in the following we provide some background theorems that evolve from PAC theory [31], VC dimension, fat-shattering [1], and luckiness framework [28]. We then turn to a characterization of the SVMs input space.

## 3. An alternative approach to incorporate domain knowledge in SVMs

According to PAC learning theory [31], given the performance of the classi<sup>fi</sup>er on a training set, OTS for the classi<sup>fi</sup>er could be upper bounded by $\varepsilon \left( l , H , \delta \right) = 1 / l$ ln (|H|/δ)where l is the number of examples in the training set, δ is the level of signi<sup>fi</sup>cance, |H| is the cardinality of the hypothesis space H which contains the classi<sup>fi</sup>er.

The bound involves |H|, which in return affects hypothesis selection in SVMs case. Therefore, one may say that even if the error bounds are loose, error bounds reveal some information about the tradeoff involving the number of instances in a training set, and the selected classi<sup>fi</sup>er. This is captured in statistical learning theory (SLT) [34,35].

Three main approaches to upper bound the cardinality of a hypothesis class are considered in this paper: (a) VC dimension [35], (b) fat-shattering dimension [1], (c) the luckiness framework [28]. Below we give corresponding error bounds for each of these approaches by using available literature.

Theorem 1 (VC-Theorem by Vapnik and Chervonenkis). Let H be a hypothesis space having VC-dimension d. For any probability distribution on $X \times \{ - 1 , 1 \}$ , with probability 1−δ over l random examples in S, any hypothesis h∈H that is consistent with S has error no more than er $\Gamma ( h ) _ { \mathcal { D } } \leq \varepsilon ( l , H , \delta ) = 2 / l ( d \log ( 2 e l / d ) + \log ( 2 / \delta ) )$ , provided d≤l and $l { > } 2 / \varepsilon \left( \bar { [ 8 ] } , \mathsf { p } . 5 6 \right)$

For higher VC-dimensions a learner needs a larger training set to achieve low generalization error, and the bound is independent of distribution and data. However, for some benign distributions it must be possible to derive tighter bounds by taking a functional margindependent VC-dimension into account. This was originally addressed in a fat-shattering theorem by [1]. Later Shawe–Taylor et al. [28] developed bounds for the case of a class of hyperplanes by taking fatshattering results into account. Below, Corollary 1 uses the fat shattering dimension results due to [15] for tighter bounds.

Corollary 1. Consider thresholding linear functions with real-valued unit weight vectors on input space X. Assume that all inputs $X \times \{ - 1 , 1 \}$ are drawn identically and independently according to an unknown distribution whose support is contained in a ball Ba of radius R in <sup>n</sup> <sup>D</sup>centered at the origin. With probability (1−δ) over training set S with l random examples, any hypothesis that has a margin m (f) of γ or bigger has error no more than err $_ { \mathrm { p } } ( f ) { \leq } \varepsilon ( l , F , \delta , \gamma ) { = } 2 / l ( d$ log (8el /dγ)log(32l /δ)) provided $l { > } 2 / \varepsilon , l { > } ( 8 R / \gamma ) ^ { 2 } { + } 5 / 4 ,$ , where $d { = } ( 8 r / \gamma ) ^ { 2 } { + } 5 / 4$

The above bound has important implications. First, by incorporating a margin of the linear classi<sup>fi</sup>er one can take advantage of benign distributions with large margins to tighten the generalization error bound. Secondly, in Theorem 1, the bound depended on the VCdimension. Corollary 1's bound suggests that for benign distributions even in in<sup>fi</sup>nitely large dimensions it could be possible to derive tight generalization bounds.

However, the fat shattering framework above assumes that the entire input space X is included in a ball centered at the origin, denoted by Ba, and the generalization error depends on the radius of Ba, which is dif<sup>fi</sup>cult to compute. This important shortcoming was <sup>fi</sup>rst addressed in [28]. Intuitively, with R <sup>fi</sup>xed, a potential generalization error bound that depends on the assumption “training set is contained in a ball of radius R centered at the origin” would yield a somewhat looser bound than that of the one depending on the assumption “entire input space is contained in a ball of radius R centered at the origin”. In [28], authors de<sup>fi</sup>ne a “luckiness framework” to recover the results of Corollary 1 by bounding the ratio of unseen data points that may not be contained in the ball of radius R that contains the sample set. Without getting into technical details, in Corollary 2, we give the generalization error in the luckiness framework, and state an updated version by taking [15] as well as $\mathfrak { R } ^ { n } \to \{ - 1 , 1 \}$ classi<sup>fi</sup>cation into account.

Corollary 2. Suppose $P _ { d } ,$ for $d = 1 , \ldots , 2 l ,$ , are positive numbers satisfying $\sum _ { d = 1 } ^ { 2 l } p _ { d } = 1$ : Suppose $0 { < } \delta { < } 1 / \ 2 ,$ , and the target function $t { \in } F ,$ and is a <sup>¼</sup>probability distribution on the input space X. With con<sup>fi</sup>dence leve $\left( 1 - \delta \right)$ over the sample set S with l elements, if the sample set is consistent with an hypothesis f, that is err $( f ) = 0 ,$ then the generalization error of f is no more than the following:

$$
\begin{array}{l} \varepsilon (l, i, \delta) = \frac {2}{l} \\ \qquad \times \left(\log \phi + 1 + \log \frac {4}{p _ {i} \delta} \left(\log 2 ^ {9} l ^ {4}\right) + \left(2 d \log \frac {8 e l}{d \gamma} \log \frac {3 2 l}{\gamma^ {2}} + 2 \log (4 l + 2) + 8\right) \log 4 l\right) \end{array}
$$

Corollary 2, is the generalization error for the classi<sup>fi</sup>cation problem for which the support of the sample set obtained lies in a ball centered at the origin with radius R. However, Corollary 1 gives the generalization error for the problem for which the entire input space is included inside of such a ball.

In the luckiness framework we observed that the distance of the furthest point from the origin is one of the determinants of the fat shattering dimension and the generalization bound. Because of this we observe that generalization bounds tend to be very loose if the input space is not assumed to be bounded. Table 2 shows generalization error bounds' performances under different scenarios. In Table 2, the “VC dimension” column (Theorem 1) represents the bound obtained by using the VC-dimension and “fat and radius $R "$ column (Corollary 1s) represents the bound obtained when the input space is assumed to be inside of the ball of radius R. The “Luckiness framework” column (Corollary 2) represents the bound when the radius R merely represents the radius of the ball containing training sets. We see that fat-shattering dimension dependent bounds provide insights only when the margin between classes is large, and bounds with luckiness framework are too loose.

Generalization error bound performances under different settings

<table><tr><td rowspan="2">d</td><td rowspan="2">R</td><td rowspan="2">γ</td><td rowspan="2">l</td><td rowspan="2">δ</td><td colspan="3">Bounds on</td></tr><tr><td>VC dimension</td><td> $fat_F$  and radius R</td><td>Luckiness framework</td></tr><tr><td>20</td><td>100</td><td>0.1</td><td>1000</td><td>0.1</td><td>0.33</td><td>n/a</td><td>n/a</td></tr><tr><td>20</td><td>100</td><td>0.1</td><td>1000</td><td>0.1</td><td>0.33</td><td>n/a</td><td>n/a</td></tr><tr><td>20</td><td>100</td><td>0.1</td><td>1000</td><td>0.1</td><td>0.33</td><td>0.74</td><td>n/a</td></tr><tr><td>20</td><td>100</td><td>0.1</td><td>1000</td><td>0.1</td><td>0.33</td><td>0.39</td><td>n/a</td></tr><tr><td>20</td><td>100</td><td>0.1</td><td>1000</td><td>0.1</td><td>0.33</td><td>0.24</td><td>n/a</td></tr><tr><td>20</td><td>100</td><td>0.1</td><td>1000</td><td>0.1</td><td>0.33</td><td>0.16</td><td>n/a</td></tr><tr><td>20</td><td>100</td><td>0.1</td><td>1000000</td><td>0.1</td><td>1.00E-03</td><td>1.70E-03</td><td>n/a</td></tr><tr><td>20</td><td>100</td><td>0.1</td><td>10000000</td><td>0.1</td><td>8.64E-05</td><td>3.00E-04</td><td>0.88</td></tr></table>

n/a means that the bound is too loose to provide any information.

The dramatic difference between the rightmost two columns is simply due to the fact that the values in the rightmost column are derived without assuming that the input space is bounded.

## 3.1. Characterizing the input space with box constraints

Often, attributes of instances are naturally bounded. For example, age, income levels, education level, weight, height, etc. are bounded from above as well as below. In many situations, attributes can be bounded using simple box constraints (see Fig. 1).

In Fig. 1, Part A, the larger ball containing most of the points denotes the ball of radius R centered at the origin that contains the training set. Three outlier points on the upper right part depict OTS points that lie outside of the ball. The gap between the luckiness framework and fat-shattering bounds are simply due to those points. If upper and lower bounds are not known, potentially there could be many such points.

A rectangle is formed by using the upper and lower bounds on the two attributes. In Fig. 1, Part B, using a linear transformation $\mathrm { ( H R _ { o l d } - }$ $[ ( x _ { i } + x _ { j } ) / 2 ] = \mathrm { H R } _ { \mathrm { n e w } }$ where $\boldsymbol { x } _ { i } , \boldsymbol { x } _ { j } \in \mathrm { H R } ^ { \prime }$ are two vectors furthest apart in $\mathrm { H R } _ { \mathrm { o l d } } )$ the rectangle is re-centered at the origin and everything is included inside of it. As the fat shattering dimension depends on the margin as well as the diameter of the ball, and the generalization bounds are smaller.

The space diagonal is the length of the longest line segment connecting opposite polyhedral vertices in a hyper-rectangle or other similar solid. The space diagonal of a hyper-rectangle can be computed easily as follows. Let $\mathbf { u b } _ { 1 } , . . . , \mathbf { u b } _ { n }$ and $\mathbb { b } _ { 1 } , . . . , \mathbb { b } _ { n }$ denote upper and lower bounds for attributes 1 through n respectively. Then $\mathsf { S D } ^ { 2 } = \sum _ { i = 1 } ^ { n } \left( \boldsymbol { \mathsf { u b } } _ { i } \boldsymbol { \mathsf { - l b } } _ { i } \right) ^ { 2 }$ . The ¼diameter of the ball can be upper bounded by the space diagonal.

## 3.2. Characterizing the input space with a polytope

For some situations more knowledge than simple attribute bounds may be available. Now we investigate the case where we can bound the instance space with a polyhedron, or in rarer cases, when we can denote the relationships between the attributes in the form of linear constraints. Both cases enable us to bound the instance space with a polyhedron. We now assume that the input space is contained inside of a polytope P. We <sup>fi</sup>rst state that the R in the fat-shattering dimension expression will be the radius of the n-dimensional ball corresponding to half of the distance between two points furthest apart (half of the metric diameter of the polytope). If x,y ∈P are the two points furthest apart in a polytope P, then the fat<sub>F</sub>(γ) dimension for $P - ( x + y ) / 2$ satis<sup>fi</sup>es

$$
\operatorname{fat} _ {\mathrm{F}} (\gamma) \leq \min \left\{\frac {| | x - y | | ^ {2}}{4 \gamma^ {2}} + \frac {5}{4}, n + 1 \right\}
$$

(using fat-shattering bounds in [15]).

The problem of <sup>fi</sup>nding the metric diameter can be stated as follows:

max $\left( x - y \right) ^ { \prime } ( x - y )$

s:t:AxVa; AyVa

Unfortunately, calculating the metric diameter of the polytope is a convex maximization problem, and is very dif<sup>fi</sup>cult to solve. Therefore, we focus on <sup>fi</sup>nding an upper bound on the metric diameter.

ubm $( A , a ) { \geq } \operatorname* { m a x } ( x - y ) ^ { \prime } ( x - y )$

s:t:AxVa; AyVa

Our goal is to <sup>fi</sup>nd good upper bounds to the metric diameter to improve our estimate of the fat-shattering dimension and thus to improve the generalization error bound.

In order to compute u $\mathfrak { d } _ { \mathrm { m } } ( A , a )$ on the metric diameter, we work with ellipsoids. The idea is to <sup>fi</sup>nd an ellipsoid that tightly <sup>fi</sup>ts the polytope and use the diameter (the length of the longest axis) of the ellipsoid to upper bound the metric diameter of the polytope. This is called the ellipsoid method. The fact that calculating the diameter of an ellipsoid is simple, and it upper bounds the metric diameter of any polytope it contains makes this approach attractive. An ideal ellipsoid is the Löwner–John (L–J) ellipsoid:

De<sup>fi</sup>nition (The Löwner and John Ellipsoid). For any bounded convex body with non-empty interior K, there exists a unique minimumvolume ellipsoid enclosing the body. This ellipsoid is called the Löwner– John ellipsoid of K.

Unfortunately, there is no known way of explicitly computing the L–J ellipsoid for polytopes. However, computational considerations provide compelling reasons to work with ellipsoids. In general, the L–J ellipsoid of a convex body denotes a special ellipsoid with the property that the convex body contains the ellipsoid obtained from the L–J ellipsoid by shrinking it n-times where n is the dimension of the convex body. This is illustrated in Fig. 2. We will see a similar phenomenon later.

![](/api/attachments/PWBHUM8Y/fulltext/images/2a0de26a660493a3f7a4c36fb165c4d843bd06ffc0a0c93c541e3671de989c5a.jpg)  
Fig. 1. Using box constraints for characterizing the input space.

![](/api/attachments/PWBHUM8Y/fulltext/images/af11dbbf8e34830e6b4de43acbc10bd74d6d277aff126c7f9f2c4d3df6856e18.jpg)  
Fig. 2. The L–J Ellipsoid for a polytope. A) Illustration for the L–J Ellipsoid for the polytope. B) For this 3-dimensional polytope, the ellipsoid that is formed by shrinking L–J ellipsoid three times lies completely inside of the polytope.

There are known polynomial time algorithms [20,25,26] to tightly approximate the L–J ellipsoid that contains all the vertices. The complexity of the problem is linear in the number of vertices. In some applications, e.g., in robotics, the vertices are known. Also in robotics, dimensionality is limited (all objects are three dimensional) and therefore computation of vertices is less complex than the m-dimensional case.

However, when a polytope is de<sup>fi</sup>ned in terms of the intersection of a <sup>fi</sup>nite number of halfspaces $( \mathrm { i } . \mathsf { e } . , P = \{ x { \in } \mathfrak { R } ^ { n } | A x { \le } a \} )$ , rather than a set of vertices, then the above mentioned algorithms lose their attraction as there is no known algorithm that can compute the vertices in time polynomial in m, n [2].

## 3.3. The ellipsoid method

An algorithm to approximate the L–J ellipsoid can be built on top of the ellipsoid method, a method developed in the 1970's initially by Shor, [29], and Iudin [16] to solve convex, not necessarily differentiable, optimization problems [5]. The ellipsoid method was initially used to <sup>fi</sup>nd a feasible solution to a system of linear inequalities. Later Khachiyan [19] showed how the ellipsoid method can be implemented in polynomial time to solve linear programming problems. A more comprehensive review of ellipsoid methods can be found in [5] and [12]. Below, we introduce the ellipsoid method, and show how we can use it for error bounding.

De<sup>fi</sup>nition (ellipsoid). An ellipsoid centered at $a { \in } \Re ^ { n }$ can be de<sup>fi</sup>ned by a setofvectorsEinRn of theform $E = E ( \mathbf { D } , d ) = \left\{ x { \in } \Re ^ { n } | ( x { - } d ) ^ { ' } \mathbf { D } ^ { - 1 } ( x { - } d ) { \le } \overline { { 1 } } \right\}$ <sup>¼ ð Þ ¼ jð Þ ð Þ</sup>where D is an n×n positive de<sup>fi</sup>nite symmetric matrix. Moreover, D is called the characteristic matrix of the ellipsoid.

Eigenvalues and eigenvectors have very useful geometric interpretation for ellipsoids. Principal axes of an ellipsoid coincide with the eigenvectors of D, and the radius of the ellipsoid along an axis is the reciprocal of the square root of that eigenvalue.

De<sup>fi</sup>nition (spectral radius). For any n×n matrix Z, the spectral radius of Z, denoted by ρ(z) is $\rho ( \mathbf { Z } ) = \operatorname* { m a x } _ { 1 \leq i \leq n } | \gamma _ { i } |$ where |λ | is the modulus of λ .

The distance between any two points in P, is less than or equal to the length of the major axis of E. Therefore, the diameter of a polytope $P \subseteq \Re ^ { n }$ , with L–J ellipsoid E, is bounded by max $\left\{ \left( 2 / \sqrt { \lambda _ { i } } \right) \right\}$ <sup>o</sup><sub>.</sub>

When maximizing (minimizing) a linear function over an ellipsoid, the center of the ellipsoid lies between the points that maximize (minimize) the function (Fig. 3). We will use this fact later in discussing the ellipsoid method. Note that the center of the ellipsoid lies between $z ^ { \mathrm { m i n } }$ and $z ^ { \mathrm { m a x } }$ . Also observe that the shaded ellipsoid is the minimal ellipsoid containing one half of the ellipsoid divided with respect to c′x through the center. Since half of the ellipsoid is a convex body, say K, then it is the L–J Ellipsoid of K.

![](/api/attachments/PWBHUM8Y/fulltext/images/96523b523df29e5d38348772ec52e3884f3f18ed6b00b0c34c631f48621fdb80.jpg)  
Fig. 3. When maximizing a linear function c′x over an ellipsoid E(D,d), the center of the ellipsoid lies between z<sup>min</sup> and z<sup>max</sup>.

So, K contains the ellipsoid obtained from its L–J ellipsoid by shrinking it n-times. Hence, if $E ( D , d )$ is the L–J Ellipsoid in n dimensions, and ellipsoid $\textstyle E { \left( { \frac { D } { n ^ { 2 } } } , d \right) }$ is the ellipsoid formed by shrinking the axes, then ellipsoid $\textstyle E { \left( { \frac { D } { n ^ { 2 } } } , d \right) }$ is contained in K.

The ellipsoid method works as follows. We start with a ball that contains P. The method generates a sequence of ellipsoids $E _ { 1 } , . . . , E _ { k }$ with centers $d _ { 1 } , \ldots , d _ { k }$ iteratively. In each iteration, if the center of the ellipsoid generated at that iteration doesn't lie inside of polytope, then its center point violates one or more constraints de<sup>fi</sup>ning the polytope. For example, let $E _ { i } ( D _ { i } , d _ { i } )$ be the ellipsoid centered at $d _ { i }$ at the ith iteration,. If the polytope $P = \{ x { \in } \Re ^ { n } | A x { \le } a \}$ , where A can be written as $A ^ { \prime } { = } [ A ^ { \prime } { _ { 1 } } { , } { \ldots } { } , A ^ { \prime } { _ { m } } ] ,$ is <sup>¼ f</sup>not contained in $E _ { i } ,$ <sup>gj</sup>then d violates at least one of the m constraints, say the kth, so $A _ { k } x _ { i } { > } \alpha _ { k }$ for some 1≤k≤m. The amount of violation in every cut can be found by computing the distance between a violated constraint and the centroid of the ellipsoid. Thus, we know that P is contained in the halfspace $A _ { k } x \leq A _ { k } x _ { i } .$ . In the next iteration, a new smaller volume ellipsoid that contains “the intersection of the halfspace that contains P and current ellipsoid” is generated.

At this point we should point out that there is a strong relationship between the ellipsoid method and the L–J Ellipsoid as illustrated in Fig. 2. In each iteration, the next ellipsoid is generated according to a hyperplane passing through the center of the current ellipsoid. Suppose that, at some iteration i, the violating constraint is $A _ { k } x { = } c ^ { \prime } x { < } c ^ { \prime } d _ { i }$ . Then we know that the center of the current ellipsoid does not lie inside of the polytope (e.g., use Fig. 4). Therefore, in the next iteration we are only considering the half ellipsoid that contains the polytope. Also, the center of the next ellipsoid generated lies between $z ^ { \mathrm { { \bar { m i n } } } }$ and $z ^ { \mathrm { m a x } }$ (Fig. 3).

In the literature, the general methodology we covered above is referred as the “Central Cut” as the cut goes right through the centroid of the ellipsoid. The algorithm is illustrated in Fig. 4. Starting with a large ball containing the polytope, the next ellipsoid generated <sup>fi</sup>ts the convex body tighter than the previous one.

Note that in the ellipsoid method, the hyperplane which is used to cut off the ellipsoid must go through the ellipsoid. Depending on the location of the cut there are different variations of the ellipsoid methods, such as deep cut (greedy elimination), and shallow cut (slower elimination).

The central cut method terminates once the origin of the generated ellipsoid lies inside of the convex body. The idea with shallow-cuts is that it can proceed further even when the center of the new ellipsoid is found to be inside of the polytope. Iteration continues until the ellipsoid is declared as “tough” then stops. This is described in detail in the Appendix.

![](/api/attachments/PWBHUM8Y/fulltext/images/1e7be7f4c50fa508bcfc1b99f966b23b3a36d66671354e775b1447d624cf695a.jpg)  
Fig. 4. In every iteration the polytope is contained in a smaller ellipsoid

Table 3  
CPU time and number of vertices for polytopes

<table><tr><td>Number of constraints</td><td>Dimension</td><td>CPU time</td><td>Vertices</td><td>Upper bound on number of vertices</td></tr><tr><td>5</td><td>2</td><td>&lt;1</td><td>5</td><td>5</td></tr><tr><td>10</td><td>2</td><td>&lt;1</td><td>10</td><td>10</td></tr><tr><td>5</td><td>3</td><td>&lt;1</td><td>6</td><td>6</td></tr><tr><td>10</td><td>3</td><td>&lt;1</td><td>16</td><td>16</td></tr><tr><td>20</td><td>3</td><td>1.76</td><td>36</td><td>36</td></tr><tr><td>50</td><td>3</td><td>9.11</td><td>96</td><td>96</td></tr><tr><td>20</td><td>5</td><td>28.46</td><td>170</td><td>272</td></tr></table>

When approximating the L–J ellipsoid of a polytope, we tried different combinations of the above methodologies. We used centralcut method results as benchmarks. Then we approximated L–J ellipsoid by generating cuts according to maximum violated constraints <sup>fi</sup>rst. Then we tested the shallow-cut methodology with different α values. Finally we picked the best performing methodology and combined it with the “toughness” idea described above. In the next section we talk about computational ef<sup>fi</sup>ciency of approximating the L–J ellipsoid as well as its implication on fat-shattering dimension and generalization error bound.

## 4. Computational analysis

In this part we use the methodology developed in the last section and compute the fat-shattering dimensions of different domain poly topes. First, we give an overview of our analysis, and testing methodology. Next, we perform numerical analyses for domains bounded only by upper/lower bounds and then by a polytope described by linear constraints. For box constraints, we compute the space diagonal and upper bounds on γ. For polytopes, we perform a series of analyses with various ellipsoid methods and combinations, and compute a bound on the metric diameter of the polytope. We compare our results to ε-approximate L–J ellipsoids. Finally, we compare the luckiness framework and our methodology.

## 4.1. Overview

All of our computational analyses were performed using Matlab 6.5 and run on a Pentium III — 900 Mhz PC under Windows XP. We randomly generated polytopes of different dimensions. Table 3 sh ows that computation of all of the vertices is a time consuming task as the number of vertices grows very rapidly in the number of dimension and constraints. In Table 3, the upper bounds on the number of vertices are due to McMullen [23]. Note that the minimum number of vertices in n dimensions is n+1, and the size of the vertex set depends on the number of constraints, and degeneracy (for example, if a vertex lies on more than n hyperplanes then the number of vertices is lower than the case when a vertex lies on only n hyperplanes).

Our random polytope generation process can be summarized as follows. First, by using m-random weight vectors $A _ { 1 } , \dotsc , A _ { m } ,$ we randomly generate a set of m-hyperplanes such that $h _ { i } ; \langle A _ { i } { \cdot } x \rangle = \alpha _ { i }$ . The bias factor, $\alpha _ { i } ,$ <sup>h i</sup>can be thought as a scale, and therefore is <sup>fi</sup>xed at 1 for convenience. These hyperplanes are used to generate inequalities for half-spaces as $h _ { i } \colon \langle A _ { i } { \cdot } x \rangle \leq \alpha _ { i } .$ . Such a generation results in polytopes that always contain the origin as $x = 0$ is the trivial solution to the set of inequalities. In order to randomize the process further, we moved each polytope away from the origin by using a random transformation vector depending on the diameter of the polytope. The amount of shift is determined by multiplying a random number drawn from the interval [0, [5]] with the diameter of the polytope.

![](/api/attachments/PWBHUM8Y/fulltext/images/2998e5473a1532d08f3f7e4797dba665dcaef5923e451426c0d19ceb6daf85fe.jpg)  
Fig. 5. The L–J approximation for $\Lambda ) \ \varepsilon { = } 1 0 ^ { - 4 }$ and 500 iterations, $\mathrm { B } ) \ \varepsilon { = } 1 0 ^ { - 4 }$ and 1000 iterations, $\mathsf { C } ) \ \varepsilon = 1 0 ^ { - 4 }$ and 5000 iterations, D) $\mid \varepsilon = 1 0 ^ { - 4 }$ and 50000 iterations.

## 4.2. Generating polytopes

If a polytope is given in the form of a set of vertices, there are known polynomial time algorithms to approximate the L–J ellipsoid containing the polytope [20,25,26]. We use the ε-approximate L–J ellipsoid to serve as a benchmark for our results. Unfortunately as the number of vertices grows, such algorithms become impractical. For this reason, we consider only a limited number of cases.

A total of 140 random polytopes were generated. We used a Matlab script called GBT $7 . 0 ^ { 1 }$ that implements a method to compute L–J ellipsoids with successive space dilation controlled by two parameters: iterations (set to 50,000) and accuracy (set to $\varepsilon = 1 0 ^ { - 8 } )$ . When either of the two bounds is reached, the ε-approximate L–J ellipsoid is computed, and algorithm stops. Fig. 5 shows the L–J approximation and the tightness of the ellipsoid's <sup>fi</sup>t for four different parameters.

The diameters of the generated polytopes (Table 4) are computed by <sup>fi</sup>nding the maximum distance between all pairs of vertices. The column $^ { * } \mathrm { L - J }$ Diameter” in Table 4 is the diameter of the ε-approximate L–J ellipsoid computed in 50,000 iterations (with $1 0 ^ { - 8 }$ accuracy). Note that the diameter of the ellipsoid is not necessarily the same as the diameter of the polytope. Finally, the average percentage difference between the diameter of the polytope and the diameter of its L–J ellipsoid is 23.19%. We observed that if the dimension is <sup>fi</sup>xed, as the number of constraints are increased this percentage difference decreases.

## 4.3. Using the ellipsoid method to upper bound the polytope diameter

The ellipsoid method starts with a ball centered at the origin that is large enough to contain the polytope and then with successive volume reducing iterations <sup>fi</sup>nds a feasible point. Finding such a ball, or ensuring that a ball contains the polytope is not trivial. The enclosing ball is found by using the theory of encoding length of integer numbers and matrices with integer data. The details of encoding length can be found in [12].

As mentioned earlier, there are various approaches used in the ellipsoid method. In the following we brie<sup>fl</sup>y discuss these.

## 4.3.1. Central cut ellipsoid method

Fig. 6 illustrates the methodology on a 3-dimensional polytope with 10 constraints that we randomly generated. Note that, the diameter does not necessarily decrease in every iteration. Also note that the improvement in terms of bounding the diameter is not very signi<sup>fi</sup>cant.

The overall performance of using the central cut ellipsoid method is given in Table 4. In the table, note that a large number of iterations (Column: “Iters”) is not necessarily an indicator of a good approximation as the diameter can get bigger. For some problems the smaller volume ellipsoids obtained by the method had actually larger diameters than the starting ellipsoids. Perhaps the most important observation is that neither a large reduction in volume (Column: “Volume Reduct”), nor a large number of iterations necessarily indicate a substantial diameter reduction (Column: “Diam Reduct”). Overall, the central-cut method did not perform very well.

## Table 4

The central cut ellipsoid method application on 2 and 3 dimensional datasets

<table><tr><td>Number of constraints</td><td>Dims</td><td>Iters</td><td>Polytope</td><td>LJ diameter</td><td>Ending diam</td><td>Diam reduct (%)</td><td>Volume reduct (%)</td></tr><tr><td>5</td><td>2</td><td>9.2</td><td>5.69</td><td>6.47</td><td>29.3</td><td>48.49</td><td>77.88</td></tr><tr><td>10</td><td>2</td><td>5.2</td><td>3.07</td><td>3.76</td><td>25.29</td><td>17.56</td><td>52.99</td></tr><tr><td>5</td><td>3</td><td>31</td><td>24.63</td><td>34.71</td><td>177.89</td><td>27.77</td><td>99.25</td></tr><tr><td>10</td><td>3</td><td>16.4</td><td>6.06</td><td>7.33</td><td>60.77</td><td>-0.26</td><td>87.13</td></tr><tr><td>20</td><td>3</td><td>14.6</td><td>3.18</td><td>3.46</td><td>19.77</td><td>37.92</td><td>87.20</td></tr><tr><td>50</td><td>3</td><td>16.5</td><td>2.4</td><td>2.61</td><td>35.56</td><td>-10.98</td><td>89.87</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td>Average</td><td>20.80</td><td>82.39</td></tr></table>

![](/api/attachments/PWBHUM8Y/fulltext/images/373ff39c8c8958db2d601fa2029439cc8b9579076dbd4d85a264e9d8122d80ff.jpg)  
A

![](/api/attachments/PWBHUM8Y/fulltext/images/08984a62ba4023eb8ae0b2f25974a4326cbf37bc7ceed558d92ef315ede5c8b3.jpg)

![](/api/attachments/PWBHUM8Y/fulltext/images/735f43363731838c93ce83fb3a3b1bb8221ac5190b94d5aa6369a483f20489e0.jpg)

![](/api/attachments/PWBHUM8Y/fulltext/images/a1aa5190bf43d6d16bbaf5dc20220b8e9bd2bc7d21856e71c366575fc0c2a526.jpg)  
C  
Fig. 6. The central-cut ellipsoid method illustrated on a 3-dimensional polytope which has a diameter of 3.77. A) First iteration: the polytope is contained in a large ball centered at the origin with a diameter of 37.7, B) Second iteration: new ellipsoid has a diameter of 39.98, and its volume is 84% of the initial ball, C) Third iteration: diameter is 42.41 and its volume is 71.1% of the initial ball. D) Eighth and the final iteration: diameter is 34.67, and volume is 30.4% of the initial ball's volume

The reason behind the poor performance of the central cut is rather intuitive. The naïve implementation searches for violated constraints and picks the <sup>fi</sup>rst violated one and makes the cut according to that constraint. Neither a selection criterion nor a cut pattern is utilized. In Fig. 6-B, even though consecutive cuts result in volume reductions, they may also cause the diameter to increase.

## 4.3.2. Shallow/deep cuts

Here we refer to the deepest cut as a deep cut and everything else as shallow. In order to <sup>fi</sup>nd a good value for shallowness, numerically we assign a parameter that controls shallowness for every cut. Earlier we termed this α. However coming up with an α value that will work well for all datasets is not possible as the value of α depends on the amount of violation. As the maximum value for α $( \alpha _ { \mathrm { m a x } } ; - 1 / n \le \alpha < 1 )$ that could be assigned depends on the amount of violation, we form a percentage grid $- 1 / n { \le } \alpha { < } \alpha _ { \mathrm { m a x } }$ for α at each iteration to observe performance level at various α levels. The results are shown in Table 5. We set grids at 0.05 intervals and test our dataset at each value. In the table, as 100% corresponds to deep cut and greediness, the average of best performing percentages is named “average greediness” (Column: Avg Greed”). Except for a very few number of cases, we found that being greedy is the best approach computationally. This also makes sense in that with deep cuts the same constraint is not violated twice in a row.

With deep cuts method converges faster and generated ellipsoids are of smaller size

<table><tr><td>Number of constraints</td><td>Dims</td><td>Iters</td><td>Polytope</td><td>LJ diameter</td><td>Ending diam</td><td>Diam reduct (%)</td><td>Volume reduct (%)</td><td>Avg greed</td></tr><tr><td>5</td><td>2</td><td>7.4</td><td>5.69</td><td>6.47</td><td>17.72</td><td>68.85</td><td>95.05</td><td>0.99</td></tr><tr><td>10</td><td>2</td><td>6.75</td><td>3.07</td><td>3.76</td><td>11.89</td><td>61.23</td><td>87.46</td><td>0.93</td></tr><tr><td>5</td><td>3</td><td>16.3</td><td>24.63</td><td>34.71</td><td>94.48</td><td>61.64</td><td>97.26</td><td>1.00</td></tr><tr><td>10</td><td>3</td><td>12.5</td><td>6.06</td><td>7.33</td><td>21.74</td><td>64.13</td><td>97.39</td><td>0.99</td></tr><tr><td>20</td><td>3</td><td>5.4</td><td>3.18</td><td>3.46</td><td>15.39</td><td>51.65</td><td>95.47</td><td>0.97</td></tr><tr><td>50</td><td>3</td><td>7</td><td>2.41</td><td>2.59</td><td>14.73</td><td>65.29</td><td>98.61</td><td>1.00</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td>Average</td><td>62.13</td><td>95.20</td><td>0.98</td></tr></table>

We indicated that consecutive cuts result in volume reductions, but they may also cause the diameter to increase. However, we believe that the main reason is that as the amount of penetration is larger with deep cuts, when shallower cuts are made before achieving that magnitude of penetration a feasible point may be found and the method may be terminated before reaching that desired amount of penetration. An illustration is given in Fig. 7.

## 4.3.3. Proceeding after a feasible point is found

Numerically, the results suggest that deep cuts are able to reduce the diameter more than shallow ones. However, taking shallow cuts prove themselves useful when a feasible point is reached and yet we would like to continue to shrink the ellipsoid further. In other words, we can use shallow cuts if we would like to <sup>fi</sup>nd a point that is not only feasible but also deep in the polytope. Grötschel et al. [12], de<sup>fi</sup>ne the framework as <sup>fi</sup>nding the minimum volume ellipsoid containing a point in the polytope that is deep enough to satisfy $c ^ { \prime } x { \leq } c ^ { \prime } d + { \sqrt { c ^ { \prime } D c / } } ( n + 1 ) . A$ point that satis<sup>fi</sup>es this constraint is called a tough point, all others are called weak points (Fig. 8).

We used deep cuts to enter the feasible region, and then we proceeded with shallow cuts to <sup>fi</sup>nd a “tough” point in the polytope. When the new ellipsoid is formed, we set α to its maximum possible. Table 6. gives results for such approach. Especially for lower dimensions the diameters that we found (Column: “Ending Diam”) are good approx imations to L–J Diameters.

![](/api/attachments/PWBHUM8Y/fulltext/images/983d56f9c8b87e16123f29eea6909187f9094d5c82cad05a4f618b607f7c5265.jpg)

![](/api/attachments/PWBHUM8Y/fulltext/images/c0341f3e344173ed7de033caed3af31c8e2b68d7610763ed2cd376c4b7683481.jpg)  
Fig. 7. A) A series of shallow cuts with respect to one constraint until it is not violated. The <sup>fi</sup>nal ellipsoid generated in the <sup>fi</sup>gure has a diameter of 384. B) A deep cut with respect to the same constraint. The ellipsoid generated with the cut has a diameter of 330 and its volume is about 56.9% of the <sup>fi</sup>nal ellipsoid in A.

![](/api/attachments/PWBHUM8Y/fulltext/images/37371228762d2fe4fe1a310acbdb0f5dfa09760bef779c954fb65f6bc2f4dea3.jpg)  
Fig, 8. The shallow cut method can continue even after the feasible region is found. The largest ball is the starting ball centered at the origin. The next smaller ball is the bal whose center is a feasible point. The smallest ball above that contains the polytope is the one obtained by using shallow cut method.

## 4.3.4. Fat shattering dimension and luckiness framework

In this section we present a comparison of our approach with other methodologies for <sup>fi</sup>nding generalization error bounds for SVMs learning. Let us illustrate our results on one of our randomly generated 3-dimensional polytopes formed by intersecting 5 halfspaces (Fig. 9). Assume that our input space is contained in such a polytope. The diameter of the polytope is 39.67, and the minimum ellipsoid that we found is 54.57 which is 3.7% bigger than an ε-approximate L–J ellipsoid diameter of 50.59. The polytope has 6 vertices. The vertexorigin distances for the vertex furthest from the origin and for the vertex closest to the origin are 63.07 and 58.69, respectively.

Table 6  
Results for proceeding after a feasible point is found via deep cuts

<table><tr><td>Number of constraints</td><td>Dims</td><td>Iters</td><td>Polytope</td><td>LJ diameter</td><td>Ending diam</td><td>Diam reduct (%)</td><td>Volume reduct (%)</td></tr><tr><td>5</td><td>2</td><td>214</td><td>5.69</td><td>6.47</td><td>7.62</td><td>86.60</td><td>98.84</td></tr><tr><td>10</td><td>2</td><td>270</td><td>3.07</td><td>3.76</td><td>4.43</td><td>85.56</td><td>98.05</td></tr><tr><td>5</td><td>3</td><td>366</td><td>24.63</td><td>34.71</td><td>38.77</td><td>84.26</td><td>99.98</td></tr><tr><td>10</td><td>3</td><td>549</td><td>6.06</td><td>7.33</td><td>9.6</td><td>84.16</td><td>99.74</td></tr><tr><td>20</td><td>3</td><td>674</td><td>3.18</td><td>3.46</td><td>6.4</td><td>79.90</td><td>99.30</td></tr><tr><td>50</td><td>3</td><td>694</td><td>2.41</td><td>2.59</td><td>6.14</td><td>86.46</td><td>99.80</td></tr><tr><td>20</td><td>5</td><td>1043</td><td>8.49</td><td>11.45</td><td>11.59</td><td>91.18</td><td>99.99</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td>Average</td><td>85.45</td><td>99.39</td></tr></table>

In this scenario, the smallest ball that contains any training set has at least a diameter of 58.69. Similarly, the smallest ball that contains any training set has a diameter of 63.07 at most, and the largest achievable margin is therefore 39.67/2=19.84.

The VC-dimension is 4, δ is set to 0.10, and the error bound based on VC-dimension is 0.012 for a sample size of 10,000. Table 7 illustrates how incorporating domain knowledge may help bounding errors. The accuracy of the table is only suf<sup>fi</sup>cient enough to compare domain incorporation effects. We know that the smaller the fat shattering dimension is, the larger the chance of achieving a tighter error bound.

In Table 7, part A illustrates the case where domain knowledge is not taken into account. In this case, the radius that contains all the sample points is at least 58.69 (rows 1 through 5), and the margin γ is at most 19.84. The radius of the ball containing all the points is 63.07 only if the maximum possible margin is achieved (rows 6 through 9). For a sample size of 10,000, the results suggest that the luckiness framework bounds are much looser. Part B contains the results with domain knowledge taken into account. R is 27.29 (half of 54.57, the diameter of the minimum ellipsoid found). In part B, the bounds, are tighter than those in part A due to the shift to the origin. Also, the results in part B are tighter. However, if the input space is already included in a polytope one does not need luckiness framework. Rows 7 through 9 and 16 through 18 are given to show numerically how tight the error bounds based on luckiness are.

Our approach has two main potential bene<sup>fi</sup>ts compared to the luckiness framework. The <sup>fi</sup>rst one is indirect. In the case of unbounded attributes, we can <sup>fi</sup>nd the minimum enclosing ball or the training points and linearly transform the input space to center the training set at the origin. The luckiness framework [28] does not suggest any linear transformation. This approach does not alter the framework, but the generalization bound would be tighter.

![](/api/attachments/PWBHUM8Y/fulltext/images/9ec2ab15372c6476f6a2dc7707f89194391c218d4675c9d1d46bd8a27d53047b.jpg)  
Fig. 9. The approximate L–J ellipsoid for the polytope.

Table 7  
Generalization bounds for the cases generated

<table><tr><td rowspan="2"></td><td rowspan="2">R</td><td rowspan="2"> $\gamma$ </td><td rowspan="2">l</td><td colspan="3">Bounds on</td></tr><tr><td> $fat_F$  and radius R</td><td>Luckiness framework</td><td>Row</td></tr><tr><td rowspan="9">A</td><td>58.7</td><td>3</td><td>10,000</td><td>N/A</td><td>N/A</td><td>1</td></tr><tr><td>58.7</td><td>6</td><td>10,000</td><td>N/A</td><td>N/A</td><td>2</td></tr><tr><td>58.7</td><td>9</td><td>10,000</td><td>0.95</td><td>N/A</td><td>3</td></tr><tr><td>58.7</td><td>12</td><td>10,000</td><td>0.53</td><td>N/A</td><td>4</td></tr><tr><td>58.7</td><td>15</td><td>10,000</td><td>0.34</td><td>N/A</td><td>5</td></tr><tr><td>63.1</td><td>19.84</td><td>10,000</td><td>0.22</td><td>N/A</td><td>6</td></tr><tr><td>63.1</td><td>19.84</td><td>7.84E+06</td><td>≈0</td><td>N/A</td><td>7</td></tr><tr><td>63.1</td><td>19.84</td><td>4.62E+07</td><td>≈0</td><td>0.99</td><td>8</td></tr><tr><td>63.1</td><td>19.84</td><td>1.00E+07</td><td>≈0</td><td>3.27</td><td>9</td></tr><tr><td rowspan="9">B</td><td>27</td><td>3</td><td>10,000</td><td>N/A</td><td>N/A</td><td>10</td></tr><tr><td>27</td><td>6</td><td>10,000</td><td>0.61</td><td>N/A</td><td>11</td></tr><tr><td>27</td><td>9</td><td>10,000</td><td>0.28</td><td>N/A</td><td>12</td></tr><tr><td>27</td><td>12</td><td>10,000</td><td>0.16</td><td>N/A</td><td>13</td></tr><tr><td>27</td><td>15</td><td>10,000</td><td>0.11</td><td>N/A</td><td>14</td></tr><tr><td>27</td><td>19.84</td><td>10,000</td><td>0.07</td><td>N/A</td><td>15</td></tr><tr><td>27</td><td>19.84</td><td>7.84E+06</td><td>≈0</td><td>0.99</td><td>16</td></tr><tr><td>27</td><td>19.84</td><td>4.62E+07</td><td>≈0</td><td>0.25</td><td>17</td></tr><tr><td>27</td><td>19.84</td><td>5.00E+07</td><td>≈0</td><td>0.23</td><td>18</td></tr></table>

The second bene<sup>fi</sup>t emerges if the input space is contained in a polytope. In this case the luckiness framework will not be needed. Table 7 indicates that a bound depending on R can be numerically tighter than a bound obtained through luckiness framework.

## 5. Conclusion and future research

In this research, we proposed methods to incorporate domainspeci<sup>fi</sup>c knowledge in SVMs. We showed that taking domain knowledge into account can enhance error bounds signi<sup>fi</sup>cantly. We represented domain knowledge as a polytope. We considered two cases. First, we bounded the input space with an hyper-rectangle (i.e., box-constraints formed by upper and lower bounds on the attributes). With this, our contribution is two folds: the need for luckiness framework can be eliminated, and by recentering the hyper-rectangle, the radius R can be reduced and a theoretical bound improved. Second, as a more general case we considered an input space bounded by a general polytope. In each case, we showed that the error bounds can be enhanced by simply <sup>fi</sup>nding the metric diameter of these convex bodies containing the input space. Although <sup>fi</sup>nding the space diagonal of a hyper-rectangle is simple, <sup>fi</sup>nding the metric diameter of the polytope is dif<sup>fi</sup>cult problem requiring a convex maximization. We proposed, instead, using the diameter of minimal containing ellipsoids (L–J ellipsoids) for polytopes as an upper bound on the metric diameter. We then shown how to approximate the L–J ellipsoids and performed an empirical study on these. For domains that are bounded but not convex, our results can be applied by using a polytope that contains the domain.

We observed that often the error bounds under the luckiness framework for SVMs are too loose to provide any useful insights about the sample and learning. When domain knowledge is utilized not only does the need for the luckiness framework become unnecessary, but also the error bounds depending on the fat shattering dimension are tighter for the problems we studied. Tighter bound can be interpreted as increased con<sup>fi</sup>dence, and/or suf<sup>fi</sup>ciency of a smaller sample set for the learning task.

Our study has several limitations and therefore several research opportunities. Perhaps the most important one is that if kernels are used, the attributes in the feature space change, and so the bounding polytope may not remain a polytope or, worse, may be unbounded after the mapping, negating the use of our methodology. If it remains bounded, one can use the polytope formed by the convex hull of the (<sup>fi</sup>nite) sample set in the feature space.

We give two scenarios where a bounding polytope may be used. In the general case, any polytope that contains the instance space can be used. However, the more tightly this encloses the instance space, the better it is. Ideally, one would prefer the convex hull of the instance space. The more limited case arises when we have known, linear relationships between the attributes. Both have limitations. In the former case we may not know how to construct a polytope that tightly bounds the instance case. In the latter case, the known relationships may not be linear. In both cases constructing a bounding polytope may not be trivial for some domains.

Another limitation is that sometimes not all of the attributes can be bounded, and the input space can only be included in an unbounded polyhedron. For such cases, our methodology doesn't directly apply and the need for the luckiness framework remains. Intuitively, if some of the attributes can be bounded, then error bounds tighter than those in the luckiness frameworks may be derived. An immediate extension of this document is to study the unboundedness of the input space for some variables by modifying the luckiness framework to tighten the error bounds by using the existing constraints.

In conclusion, we believe more research should focus on incorporating domain knowledge in learning. Encoding prior knowledge about a domain into a learning problem increases the con<sup>fi</sup>dence of the learner, and probably and more importantly the resulting accuracy of the induced concepts.

## Appendix A

## Theorem 2

Let $E = E \ ( D , d )$ be an ellipsoid in $\Re ^ { n } .$ , and let $A _ { k } = \mathbf { c }$ be a non-zero n-vector. Consider the halfspace $H = \{ x { \in } \Re ^ { n } | c ^ { \prime } x { \le } \gamma \} . \ E _ { i + 1 } ( D , d , c , \gamma ) =$ $E _ { i } ( D , d ) \cap \{ x { \in } \Re ^ { n } | c ^ { \prime } x { \leq } \gamma \} , \operatorname { t h e } \mathrm { { L } } - \jmath$ Ellipsoid for the next iteration is

$$
E _ {i + 1} = E _ {i} (D, d), \text { if } - 1 \leq \alpha \leq - 1 / n
$$

$$
E _ {i + 1} = E _ {i + 1} (D _ {i + 1}, d _ {i + 1}) \text {   if   } - 1 / n \leq \alpha \leq - 1 \text {   where   } D _ {i + 1}, d _ {i + 1}
$$

are

$$
d _ {i + 1} = d - \frac {1 + n \alpha}{n + 1} b
$$

and

$$
D _ {i + 1} = \frac {n ^ {2}}{n ^ {2} - 1} (1 - \alpha^ {2}) \left(D - \frac {2 (1 - n \alpha)}{(n + 1) (1 + \alpha)} b b ^ {\prime}\right)
$$

where $\begin{array} { r } { b = \frac { D c } { \sqrt { c ^ { \prime } D c } } } \end{array}$ and $\begin{array} { r } { \alpha = \frac { c ^ { \prime } d - \gamma } { \sqrt { c ^ { \prime } D c } } . } \end{array}$

The matrix $D _ { i + 1 }$ is symmetric and positive de<sup>fi</sup>nite and thus $E _ { i + 1 } =$ $E ( D _ { i + 1 } , d _ { i + 1 } )$ is an ellipsoid. Moreover, $( E \cap H ) \subset E _ { i + 1 }$ , and for $\gamma { = } c ^ { \prime } d _ { i }$

$$
\operatorname{Vol} (E _ {i + 1}) <   e ^ {- 1 / (2 (n + 1))} \operatorname{Vol} (E)
$$

[12].

Notice in Theorem 2, for $\gamma { = } c ^ { \prime } d _ { i }$ the cut is right through the center of the ellipsoid. In the ellipsoid method literature, the location of the cut determines the type of the cut as well as modi<sup>fi</sup>cations to the ellipsoid method. The type of the cut is determined by the following:

For $\gamma { = } c ^ { \prime } d _ { i }$ the cut is through the center, and called “central cut”, $\alpha { = } 0 .$

For 0<sup>b</sup>α1 then we can make a deeper cut, and this is called “deep cut”.

For −1/n<sup>b</sup>α<sup>b</sup>0 then we include more than the half ellipsoid in our cut, and is called “shallow cut”.

The amount of violation in every cut can be found by computing the distance between a violated constraint and the centroid of the ellipsoid: $| c ^ { \prime } d - \alpha _ { i } | / \langle c ^ { \prime } \cdot c \rangle$ where $c ^ { \prime } x { \leq } \alpha _ { i }$ is the violated constraint, and d is the center of the ellipsoid. When approximating to L–J ellipsoid maximum violated constraint could be selected for the next cut.

The shallow-cut method does not necessarily stop when the center of the ellipsoid lies in the polytope. For a given polytope P the stopping criterion of the shallow-cut method is the membership of the ellipsoid $E _ { \mathrm { M } } ( D / ( n + 1 ) ^ { 2 } ,$ d) in the polytope. If ellipsoid $E _ { \mathrm { M } }$ lies completely inside P, then the method terminates and the ellipsoid is declared to be tough [12]. To determine this we check all constraints of the polytope $\mathrm { i f } A _ { i } ^ { \prime } D A _ { i } /$ $( n + 1 ) ^ { 2 } { \leq } ( \alpha _ { i } { - } A _ { i } ^ { \prime } A ) ^ { 2 }$ is violated for any i. If so the method continues by making a cut according to constraint i, otherwise it declares $E _ { \mathrm { M } }$ tough and terminates.

## References

[1] N. Alon, S. Ben-David, N. Cesa-Bianchi, D. Haussler, Scale-sensitive dimensions uniform convergence, and learnability, Journal of the ACM 44 (4) (1997) 615–631

[2] D. Avis, L. Devroye, Estimating the number of vertices of a polyhedron, Information Processing Letters 73 (137–143) (2001) 137.

[3] O. Barzilay, V.L. Brailovsky, On domain knowledge and feature selection using a support vector machine, Pattern Recognition Letters 20 (1999) 475–484.

[4] J.C. Bennett, C. Campbel, Support vector machines: hype or hallelujah, SIGKDD Explorations 2 (2) (2000) 1–13.

[5] R.G. Bland, D. Goldfarb, M.J. Todd, The ellipsoid method: a survey, Operations Research 29 (6) (1981) 1039–1091.

[6] M. Cecchini, Timely Discovery of Financial Events using Publicly Available Company Information. Phd Dissertation, University of Florida, 2005.

[7] M. Chau, H. Chen, A machine learning approach to web page <sup>fi</sup>ltering using content and structure analysis, Decision Support Systems 44 (2) (2008) 482–494.

[8] N. Cristianini, J. Shawe-Taylor, An Introduction to Support Vector Machines and Other Kernel-Based Learning Methods, Cambridge University Press, Cambridge, UK, 2000.

[9] N. Cristianini, J. Shawe-Taylor, H. Lodhi, Latent semantic kernels, Journal of Intelligent Information Systems 18 (2/3) (2002) 127–152

[10] G. Fung, O. Mangasarian, J. Shavlik, Knowledge-based Nonlinear Kernel Classi<sup>fi</sup>ers. Data Mining Institute, Computer Sciences Department, University of Wisconsin Madison, Wisconsin, 2003, Technical Report 03-02, Retrieved Sept 11, 2005, from ftp://ftp.cs.wisc.edu/pub/dmi/tech-reports/03-02.ps

[11] G. Fung, O. Mangasarian, J. Shavlik, Knowledge-based Support Vector Machine Classi<sup>fi</sup>ers. Data Mining Institute, Computer Sciences Department, University of Wisconsin, Madison, Wisconsin, 2001, Technical Report 01-09 Retrieved Sept 11, 2007 from ftp://ftp.cs.wisc.edu/pub/dmi/tech-reports/01-09.pdf

[12] M. Grötschel, L. Lovazs, A. Schrijver, Geometric Algorithms and Combinatorial Optimization, Algorithms and Combinatorics: Study and Research Texts, vol. 2, Springer–Verlag, Berlin, 1988.

[13] R.M. Hristev, The ANN Book, , 1998 Retrieved September 11, 2007 from ftp://math chtf.stuba.sk/pub/vlado/NN\_books\_texts/Hritsev\_The\_ANN\_Book.pdf.

[14] Z. Huang, H. Chen, C. Hsu, W. Chen, S. Wu, Credit rating analysis with support vector machines and neural networks: a market comparative study, Decision Support Systems 37 (4) (2004) 543–558.

[15] D. Hush, C. Scovel, Fat-Shattering of Af<sup>fi</sup>ne Functions, 2003, Los Alamos National Laboratory Technical Report LA-UR-03-0937.

[16] D.B. Iudin. A.S. Nemiroyskii. Informational complexity and efficient methods for solving complex extremal problems Translated in Matekon: Translations of Russian and East European Mathematical Economics, vol. 13, 1976, pp. 25–45.

[17] T. Joachims, Text categorization with support vector machines: learning with many relevant features, Proceedings of the European Conference on Machine Learning (ECML), Springer, 1998.

[18] T. Joachims, N. Cristianini, J. Shawe-Taylor, Composite kernels for hypertext categorisation, Proceedings of the International Conference on Machine Learning (ICML), 2001.

[19] L.G. Khachiyan, A polynomial algorithm for linear programming, Soviet Mathematics Doklady 20 (1979) 191–194.

[20] P. Kumar, A.E. Yıldırım, Minimum volume enclosing ellipsoids and core sets, Journal of Optimization Theory and Applications 126 (1) (2005) 1–21.

[21] Q.V. Le, A.J. Smola, T. Gartner, Simpler knowledge-based support vector machines, Proceedings of the 23rd International Conference on Machine Learning, Pittsburgh, PA, 2006.

[22] Martens, D., Bruynseels, L., Baesens, B., Willekens, M., & Vanthienen, J., (in press) Predicting Going Concern Opinion with Data Mining. Decision Support Systems,

[23] P. McMullen, The maximum number of faces of a convex polytope, Mathematika XVIL(1970).179-184

[24] P. Niyogi, T. Poggio, F. Girosi, Incorporating prior information in machine learning by creating virtual examples, IEEE Proceedings on Intelligent Signal Processing 86 (1998) 2196–2209.

[25] E. Rimon, S.P. Boyd, Ef<sup>fi</sup>cient Distance Computation Using the Best Ellipsoid Fit. Technical Report, Stanford University, 1992.

[26] E. Rimon, S.P. Boyd, Obstacle collision detection using best ellipsoid <sup>fi</sup>t, Journal of Intelligent and Robotic Systems 18 (1997) 105–126.

[27] B. Schölkopf, P. Simard, A. Smola, V. Vapnik, Prior knowledge in support vector kernels, in: M. Jordan, M. Kearns, S. Solla (Eds.), Advances in Neural Information Processing Systems 10, Cambridge, MA, 1998, pp. 640–646.

[28] J. Shawe-Taylor, P.L. Bartlett, R.C. Williamson, M. Anthony, Structural risk minimization over data-dependent hierarchies, IEEE Transactions on Information Theory 44 (1998) 1926–1940.

[29] N.Z. Shor, Convergence rate of the gradient descent method with dilatation of the space, translated in Cybernetics 6 (2) (1970) 102–108.

[30] D. Song, R.Y.K. Lau, P.D. Bruza, K. Wong, D. Chen, An intelligent information agent for document title classi<sup>fi</sup>cation and <sup>fi</sup>ltering in document-intensive domains, Decision Support Systems 44 (1) (2007) 251–265.

[31] L.G. Valiant, Atheoryof thelearnable, Communications of theACM27(1984) 1134–1142.

[32] T. Van Gestel, B. Baesens, P. Van Dijcke, J. Garcia, J.A.K. Suykens, J. Vanthienen, A process model to develop an internal rating system: sovereign credit ratings, Decision Support Systems 42 (2) (2006) 1131–1151.

[33] N.V. Vapnik, Statistical Learning Theory, John Wiley & Sons, Toronto, CA, 1998.

[34] N.V. Vapnik, Estimation Dependences Based on Empirical Data, Springer–Verlag NY, 1982.

[35] N.V. Vapnik, A.Y. Chervonenkis, On the uniform convergence of relative frequencies of events to their probabilities, Theory of Probability and Its Applications 16 (2) (1971) 264–280.

[36] P.W. Wagacha, Induction of Decision Trees, University of Nairobi, 2003.

[37] D.H. Wolpert, The existence of a priori distinctions between learning algorithms, Neural Computation 8 (7) (1996) 1391–1420.

[38] D.H. Wolpert, The lack of a priori distinctions between learning algorithms, Neural Computation 8 (7) (1996) 1341–1390.

[39] D.H. Wolpert, The supervised learning no-free-lunch theorems, Proceedings of the 6th Online World Conference on Soft Computing in Industrial Applications, 2001.

[40] D.H. Wolpert, W.G. Macready, No free lunch theorems for search, Technical Report, Santa Fe Institute, 1995 SFI-TR-95-02-010

Enes Eryarsoy is an assistant professor in the Faculty of Management at Sabanci University. His research focuses on applications of OR and machine learning/data mining techniques on problems that are important from business point of view. He particularly concentrates on SVMs, information retrieval, association rule mining. His other research areas are pricing of information goods, software piracy, scheduling, and telecommunications (network design).

Gary J. Koehler is the John B. Higdon Eminent Scholar and Professor of Decision and Information Sciences in the Warrington School of Business at the University of Florida. He was recently Professor and Area Head at the Krannert Graduate School of Management at Purdue University. He has published in Decision Support Systems, Operations Research, Management Science, ORSA Journal on Computing, EÍolutionaryComputations, SIAM Journal on Control and Optimization, Annals of Operations Research, European Journal of Operational Research, Decision Sciences, Annals of Mathematics and Arti<sup>fi</sup>cial Intelligence, Computers and Operations Research, Complex Systems, Neural Networks, IEEE Transactions on Engineering Management, Managerial and Decision Economics, Naval Research Logistics Quarterly, Discrete Applied Mathematics, Journal of Finance and others. His current research interests are in e-commerce related areas.

Haldun Aytug is an associate professor in the Warrington School of Business at the University of Florida. Dr. Aytug's research focuses on machine learning applications, theory and applications of genetic algorithms and scheduling. His research has been funded by the National Science Foundation, Intel Corporation and Applied Materials. His teaching interests include database design, system analysis and design, knowledgebased systems, heuristics and simulation. He has served on the faculty at UNC-Charlotte and Michigan Technological University.
