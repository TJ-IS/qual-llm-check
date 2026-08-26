---
otero_id: 30
otero_key: "SXTCM6EW"
title: "Classification by vertical and cutting multi-hyperplane decision tree induction"
authors: "Marco Better; Fred Glover; Michele Samorani"
year: "2010"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2009.06.004"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Classi<sup>fi</sup>cation by vertical and cutting multi-hyperplane decision tree induction ☆

Marco Better <sup>a</sup>, Fred Glover <sup>a,</sup>⁎, Michele Samorani <sup>b</sup>

<sup>a</sup> OptTek Systems, Inc., 1919 Seventh Street, Boulder, Colorado 80302, United States

<sup>b</sup> Leeds School of Business, University of Colorado at Boulder, Campus Box 419, Boulder, Colorado 80309, United States

## a r t i c l e i n f o

Available online 17 June 2009

Keywords: Data mining Discrimination analysis Piecewise-linear models Mathematical programming

## a b s t r a c t

Two-group classi<sup>fi</sup>cation is a key task in decision making and data mining applications. We introduce two new mixed integer programming formulations that make use of multiple separating hyperplanes. They represent a generalization of previous piecewise-linear models that embed rules having the form of hyperplanes, which are used to successively separate the two groups. In fact, the classi<sup>fi</sup>ers obtained are particular types of decision trees which are allowed to grow in depth and not in width. Computational results show that our models achieve better classi<sup>fi</sup>cation accuracy in less time than previous approaches.

© 2009 Elsevier B.V. All rights reserved

## 1. Introduction

One of the key tools for classifying data in real-world data mining applications [15] is Discriminant Analysis. This technique is fundamental to business applications in marketing, accounting, advertizing, sales, manufacturing <sup>fi</sup>nancial analysis, strategic planning and many other domains [5,6,16,17,19,22,23,26]. It is a crucial component of any decision that involves determining which people, groups, elements or processes to target in order to achieve desired goals or to implement particular policies most effectively. Recent contributions to this area grow out of mathematical programming approaches based on multivariate decision trees, piecewise-linear models, data envelopment analysis and kernelbased classi<sup>fi</sup>ers [2,7,10]. These models are commonly formulated with the goal of classifying data into two groups, although they can be easily adapted to accommodate more classes.

The induction of multivariate decision trees (MDTs) consists in <sup>fi</sup>nding a binary tree where, at each internal node, the data set is recursively split by a hyperplane into two parts, and where each leaf node is associated with one group, determining in this fashion the predicted group for each object [21]. The methods to build MDTs, such as OC1 [18], are often based on a two-step procedure: a construction step, which consists of a heuristic algorithm that builds the initial MDT, and a pruning step, which aims to reduce its size, enhancing both the accuracy and the interpretability of the <sup>fi</sup>nal result. Support Vector Machine (SVM) methods [7] usually rely on a limited number of known kernel transformations to project the data set into a high-dimensional space with the hope of rendering it linearly separable. Despite their good performance (provided that a suitable kernel is available), they do not provide interpretable classi<sup>fi</sup>cation rules. Finally, piecewise-linear models solve the classi<sup>fi</sup>cation problem directly, <sup>fi</sup>nding a set of hyperplanes that forms, in fact, a MDT. Therefore, they have both advantages of optimality and interpretability. An additional advantage is that these models, including the reigning one, proposed by [12], have stringent requirements that limit their ability to handle complex structures. For example, they require that the elements of one group lie in a convex region, so they must be solved twice: each time constraining one group to lie in the convex region. Recently, [25] have explored the application of discriminant analysis and have compared it to the use of data envelopment analysis in a detailed assessment of corporate failure. The authors additionally employ these tools to analyze performance in the Japanese construction industry in [24]. Our present work may be viewed as an extension of the types of classi<sup>fi</sup>cation methodology used in these studies, and provides a basis for carrying out this classi<sup>fi</sup>cation analysis in greater depth to re<sup>fi</sup>ne the inferences obtained.

In this paper, in order to provide models that have useful features for classi<sup>fi</sup>cation problems arising in real-world contexts, we present two mixed integer formulations for the induction of MDTs, which we call Vertical Decision Tree and Cutting Decision Tree. These new formulations build on the sequence of progressively more advanced classi<sup>fi</sup>cation models that began with the original goal programming models of [9]. By this connection, our present work may be viewed as having a link to the goal programming model conceptions of [3] and of [4]. Our models overcome many of the defects of the existing classi<sup>fi</sup>ers based on similar techniques. We overcome them by the following efforts:

1. Constructing a MDT through an exact algorithm, without relying on any heuristic and/or pruning procedures;

2. Generalizing piecewise-linear approaches by eliminating the requirement that one group must lie in a convex region, and by using signi<sup>fi</sup>cantly fewer binary variables (about a 50% reduction), and

3. Not projecting the data into high-dimensional space, which avoids the problem of <sup>fi</sup>nding a suitable kernel.

b

Both models prevent the tree from growing in width by guaranteeing the presence of at least one leaf node at each depth (or level) of the tree. Furthermore, in the case of the Cutting Decision Tree, the model requires that the misclassi<sup>fi</sup>cations – if any – happen only at the maximum depth of the tree. We show that this apparent limitation allows the depth of the tree to be parametrically decided and does not lead to a decrease in classi<sup>fi</sup>cation accuracy. In fact, the Cutting Decision Tree model uses fewer binary variables and its solution times are signi<sup>fi</sup>cantly shorter. Our models outperform the one proposed by Glen [10–12], both in terms of accuracy and computing time, and obtain similar or better results than SVMs and OC1. Our models are particularly suitable for those real-world classi<sup>fi</sup>cation problems whose classi<sup>fi</sup>cation rules can be expressed as a logical expression involving many conditions (rather than a single condition), where a “condition” refers to a linear combination of attributes. For example, consider the following logical expression involving 4 attributes a, b, c, and d:

## a ≥ b AND c ≤ 2d

Due to its tree structure, our approach may <sup>fi</sup>nd a classi<sup>fi</sup>cation rule that uses this expression to discriminate between the two groups of objects. On the other hand, approaches using a single separating hyperplane cannot <sup>fi</sup>nd this kind of logical pattern. For example, DEA cannot <sup>fi</sup>nd any set of coef<sup>fi</sup>cients that yields the logical expression above.

The next section of the paper provides background information about the classi<sup>fi</sup>cation problem and reviews relevant literature on single and multiple hyperplane formulations that provide the context for our models. Then, we introduce our two new mathematical models mentioned above and report on computational tests that evaluate the accuracy on two well-established benchmark data sets to demonstrate the advantages of our approaches with respect to state-of-the-art alternatives. Finally, we summarize our conclusions and opportunities for future research.

## 2. Hyperplane-based classi<sup>fi</sup>cation

Let $a _ { i j }$ denote the value of a speci<sup>fi</sup>c characteristic of an element in a data set, where each element $i ( i { = } 1 , . . . , m )$ is described by a range of attributes ${ \mathrm { ~ ~ } } ( j = 1 , . . . , n )$ . We seek to classify these elements in such a manner that correctly identi<sup>fi</sup>es whether a vector $A _ { i } { = } ( a _ { i 1 } { , } { \ldots } , a _ { i n } )$ for a given element i should result in classifying the element as belonging to Group 1 or Group 2 (denoted $G _ { 1 }$ and $G _ { 2 } ,$ respectively).

The decision rules we investigate here are based on hyperplane separation approaches, viewing the A<sub>i</sub> vectors as points in an ndimensional space. In the simplest case, these approaches use a single hyperplane, characterized by a vector $X { = } ( x _ { 1 } { , } . . . , x _ { n } )$ and a scalar $b ,$ to differentiate the points $A _ { i }$ for i ∈ $G _ { 1 }$ from the points for i∈ $G _ { 2 } ,$ , according to the following decision rule:

$$
A _ {i} X <   b \text {   for   } i \in G _ {1} \text {   and   } A _ {i} X > b \text {   for   } i \in G _ {2}\tag{1}
$$

Previous studies have proposed mixed integer formulations that aim to minimize the number of misclassi<sup>fi</sup>cations by a single separating hyperplane (see [1,10,11,13,22]). However, these formulations have various de<sup>fi</sup>ciencies, and generally require an excessive number of variables. For example, recent formulations [10,11] require doubling the number of original $x _ { j }$ variables by splitting each one into a positive and negative part, and then introducing a normalization constraint that sets the sum of these variables to 1.

On the other hand, the common goal of piecewise-linear models and MDTs is to approximate more complex structures in the underlying data than those that can be achieved by a single hyperplane, as shown in Fig.1. Thus, we refer to these techniques as Multi-hyperplane approaches.

![](/api/attachments/SXTCM6EW/fulltext/images/3e5c2be5283b41a5a602fdd3095a7cca8261cc4e901d8bcdfa78d52831542a6a.jpg)

![](/api/attachments/SXTCM6EW/fulltext/images/3415e18e53eefa0ec5d2bbb48fcaf95cea3e0d03aa09960bb0c6ec8366e326d3.jpg)  
Fig. 1. Single and multiple separating hyperplanes, where we separate round elements from diamonds elements

Glen (see [12]) introduced a mixed integer model that constructs a set of piecewise-linear segments in order to separate elements into two groups, requiring that the elements in one of the groups lie in a convex region (i.e. the piecewise-linear segments must form a convex region). Because of the convexity assumption, the model must be solved twice to determine which group should be treated as convex to provide better results. Apart from doubling the number of x variables by splitting them into $x _ { j } ^ { + }$ and $\bar { x _ { j } }$ <sup>−</sup> (as in a special ordered set), the model also makes use of additional binary variables in every hyperplane constraint to determine whether the element lies in the convex region or not.

## 3. Multi-hyperplane models for multivariate decision trees

This section describes our two proposed Multi-hyperplane models, which aim to build a Vertical Decision Tree and a Cutting Decision Tree, respectively. We begin by de<sup>fi</sup>ning each type of decision tree as follows:

De<sup>fi</sup>nition 1. Vertical Decision Tree.

A Vertical Decision Tree (VDT) is a MDT for which each internal node is a parent of at least one leaf node.

Thus, at each depth except for its maximum depth $d ^ { * } ,$ , the elements lying on one side of the hyperplane are classi<sup>fi</sup>ed into one of the two groups, while the classi<sup>fi</sup>cation of the residual elements is delegated to the hyperplane at the subsequent depth. Fig. 2 illustrates the structure of a general VDT whose depth is $d ^ { * } { = } 3$ (it uses 3 hyperplanes). We seek to separate points represented as circles (which belong to $G _ { 1 } )$ from points represented as diamonds (which belong to $G _ { 2 } ) _ { }$ . In illustrations throughout this paper, the left child of any internal node corresponds to $G _ { 1 } ,$ and the right child corresponds to $G _ { 2 } .$ . This implies that leaf nodes associated with $G _ { 1 }$ can appear only as left children, and leaf nodes associated with $G _ { 2 }$ only as right children. Note that this assumption re<sup>fl</sup>ects only on the graphical notation that we use, and does not cause any loss of generality. The points are separated by three hyperplanes, denoted by $h _ { 1 } , h _ { 2 }$ and $h _ { 3 } .$ . The decision boundary is formed by segments PQ, QR and RS of the three hyperplanes. The dark diamonds depicted in Fig. 2a, $o _ { 1 }$ and $^ { 0 _ { 2 } , }$ , are misclassi<sup>fi</sup>ed by the tree. Fig. 2b indicates the leaf nodes where they fall. We consider that an element e “falls into” a (leaf or internal) node n if e encounters n throughout the path made by classifying e [20].

## De<sup>fi</sup>nition 2. Cutting Decision Tree.

A Cutting Decision Tree (CDT) is a VDT where misclassi<sup>fi</sup>cations at intermediate leaves are not allowed.

![](/api/attachments/SXTCM6EW/fulltext/images/41d200bbbcde51d95c0561e706135a77b1abcc45330d8a0db07726cb53eca6be.jpg)  
Fig. 2. a) Shows a data set where circles belong to $G _ { 1 }$ and diamonds to $G _ { 2 } ;$ The corresponding VDT wit $1 d ^ { * } = 3$ is shown in b) the numbers in the leaf nodes indicate the associated group. Objects $o _ { 1 }$ and o are misclassi<sup>fi</sup>ed: they fall into the wrong leaf node at respectively depths 1 and 3.

Thus, classi<sup>fi</sup>cation errors – if any – may only occur at maximum depth d⁎. The classi<sup>fi</sup>cation procedure aims to “cut” part of the data set at each level by compelling all the elements of one group to lie on one side of the hyperplane. The VDT in Fig. 2b is not a CDT, since $o _ { 2 }$ is misclassi<sup>fi</sup>ed at depth $d = 1 .$ . However, if we deleted $o _ { 2 }$ from the data set the tree would be a CDT, because $o _ { 1 }$ , which would then be the only misclassi<sup>fi</sup>ed element and falls in a leaf node located at the last level of the tree.

## 3.1. A model for vertical decision trees

We <sup>fi</sup>rst provide a model for inducing a VDT. For the sake of simplicity, we limit our formulation to the case of VDTs of depth $d ^ { * } { = } 3 .$ . The type of tree induced is determined by the position of its internal nodes and leaf nodes. Fig. 3 shows all possible VDT types for the case where $d ^ { * } { = } 3$ . The top two rows shown in Fig. 3 denote the meaning of special binary variables $s l _ { 1 }$ and $s \mathbf { l } _ { 2 } ,$ which we will call slicing variables. These variables constitute our structure variables, since they de<sup>fi</sup>ne the particular structure of the induced tree. Speci<sup>fi</sup>cally, if $\dot { s } l _ { 1 } = 0 ,$ the tree will be “sliced” to the right at depth 1. Hence, the right node at depth 2 must be a leaf node associated with $G _ { 2 } .$ Conversely, i $\boldsymbol { \mathrm { ~ f ~ } } \boldsymbol { s l _ { 1 } = 1 }$ , the right node will be an internal node and the left node a leaf node associated with $G _ { 1 } .$ The same logic applies for depth 2, where $s l _ { 2 }$ indicates whether the tree is sliced on the right $( s l _ { 2 } = 0 )$ or on the left $( s l _ { 2 } = 1 )$ ).

Fig. 3 lists the 4 types of tree: tree (0, 0), (0, 1), (1, 0) and (1, 1), where the numbers in parenthesis correspond respectively to the value of $s l _ { 1 }$ and $s l _ { 2 } .$ . The complete mathematical model for a VDT of maximum depth $d ^ { * } { = } 3$ can be expressed as follows:

$$
\begin{array}{l} \text { Let } z _ {i} ^ {*} = \left\{ \begin{array}{l} 0 \text { if   object } i \text { is   correctly   classified   by   the   tree } \\ 1 \text { otherwise } \end{array} \right\} \\ \text { Let } z _ {i d} = \left\{ \begin{array}{l} 0 \text { if   object } i \text { is   correctly   classified   by   hyperplane } h _ {\mathrm{d}}, \text { according   to   Eq. (1) } \\ 1 \text { otherwise } \end{array} \right\} \end{array}
$$

Because the goal is to minimize the number of misclassi<sup>fi</sup>ed elements, the objective function is simply:

Minimiz $\sum _ { i = 1 } ^ { n } z _ { i } ^ { * }$

First, we include the hyperplane constraints that are based on inequalities (1) for each depth d of the tree:

$$
\begin{array}{l l} A _ {i} X _ {d} - M z _ {i d} \leq b _ {d} - \varepsilon & \text { for } i \in G _ {1}, d = 1, 2, 3 \\ A _ {i} X _ {d} + M z _ {i d} \geq b _ {d} + \varepsilon & \text { for } i \in G _ {2}, d = 1, 2, 3 \end{array}
$$

where ε is a constant quantity that we treat parametrically to induce a “separation zone” in order to prevent points of both groups from ending up exactly on the boundary.

![](/api/attachments/SXTCM6EW/fulltext/images/19b76a58501f7664404b9953042c0a685c4905f7ab41e6b278ef1adf73bc680d.jpg)  
Fig. 3. All possible VDT types for $d ^ { * } = 3 .$

We then include constraints that identify the optimal tree structure for the data set for classi<sup>fi</sup>cation purposes. Thus, for tree type (0,0), we write:

$$
\begin{array}{l} M (s l _ {1} + s l _ {2}) + z _ {i} ^ {*} \geq z _ {i 1} + z _ {i 2} + z _ {i 3} - 2 \text { for } i \in G _ {1} \\ M (s l _ {1} + s l _ {2}) + M z _ {i} ^ {*} \geq z _ {i 1} + z _ {i 2} + z _ {i 3} \text { for } i \in G _ {2} \end{array}
$$

where M is a large constant. Only when $s l _ { 1 } = 0$ and $s l _ { 2 } = 0$ , the actual constraints will $z _ { i } ^ { * } \ge z _ { i 1 } + z _ { i 2 } + z _ { i 3 } - 2$ (for $i \in G _ { 1 } )$ and $M z _ { i } ^ { * } \geq z _ { i 1 } { \mathrm { ~ + ~ } }$ $z _ { i 2 } + z _ { i 3 } ( \mathrm { f o r } i \in G _ { 2 } )$ be “activated.” So, for a (0,0) tree, an object of $G _ { 1 }$ is misclassi<sup>fi</sup>ed only if it is misclassi<sup>fi</sup>ed by all 3 hyperplanes, while an object of $G _ { 2 }$ is misclassi<sup>fi</sup>ed if it is misclassi<sup>fi</sup>ed by at least one hyperplane. Similarly, constraints for tree type (1,1) will only be activated when sl and sl are both equal to 1. These constraints are:

$$
\begin{array}{l} M (2 - s l _ {1} - s l _ {2}) + M z _ {i} ^ {*} \geq z _ {i 1} + z _ {i 2} + z _ {i 3} \text { for } i \in G _ {1} \\ M (2 - s l _ {1} - s l _ {2}) + z _ {i} ^ {*} \geq z _ {i 1} + z _ {i 2} + z _ {i 3} - 2 \text { for } i \in G _ {2} \end{array}
$$

For tree types (0,1) and (1,0), the logic is similar in that the appropriate part of the constraints will be active when the slicing variables have the corresponding value. However, for these types of trees, the decision structure requires additional constraints. We use an additional binary variable $w _ { i }$ to activate or deactivate certain “either-$0 \mathrm { { r } } ^ { \prime \prime }$ constraints. For example, the constraints for tree (0,1) are:

$$
\begin{array}{l l} M (1 + s l _ {1} - s l _ {2}) + z _ {i} ^ {*} \geq z _ {i 1} - M w _ {i} & \text { for } i \in G _ {1} \\ M (1 + s l _ {1} - s l _ {2}) + M z _ {i} ^ {*} \geq z _ {i 2} + z _ {i 3} - M (1 - w _ {i}) & \text { for } i \in G _ {1} \\ M (1 + s l _ {1} - s l _ {2}) + z _ {i} ^ {*} \geq z _ {i 1} & \text { for } i \in G _ {2} \\ M (1 + s l _ {1} - s l _ {2}) + z _ {i} ^ {*} \geq z _ {i 2} + z _ {i 3} - 1 & \text { for } i \in G _ {2} \end{array}
$$

When $s l _ { 1 } = 0$ and $s l _ { 2 } = 1$ , these constraints are activated, in which case the variables w are used to express the fact that a correctly classi<sup>fi</sup>ed element of $G _ { 1 }$ is correctly classi<sup>fi</sup>ed either by hyperplane $h _ { 1 }$ or by both hyperplane $h _ { 2 }$ and hyperplane $h _ { 3 } .$ An element of $G _ { 2 } ,$ on the other hand, will be correctly classi<sup>fi</sup>ed by the tree if it is correctly classi<sup>fi</sup>ed either by hyperplanes $h _ { 1 }$ and $h _ { 2 }$ or by hyperplanes $h _ { 1 }$ and $h _ { 3 } ,$ . The case that corresponds to tree type (1,0) is just a mirror image of the previous case.

Let M be a “large” constant as a proxy for an unknown upper bound<sup>1</sup>; let ε be a “small” constant to induce a strict (non-zero) displacement from a hyperplane, and let G be the union of $G _ { 1 }$ and $G _ { 2 }$ We can now formulate the full $d ^ { * } { = } 3$ VDT model as follows:

Minimize $\sum _ { i = 1 } ^ { n } \ z _ { i } ^ { * }$

1:1

Subject to

$$
A _ {i} X _ {d} - M z _ {d i} \leq b _ {d} - \varepsilon
$$

$$
\text { for } i \in G _ {1}, d = 1, 2, 3\tag{1.2}
$$

$$
A _ {i} X _ {d} + M z _ {d i} \geq b _ {d} - \varepsilon
$$

$$
\text { for   } i \in G _ {2}, d = 1, 2, 3\tag{1.3}
$$

$$
M (s l _ {1} + s l _ {2}) + z _ {i} ^ {*} \geq z _ {i 1} + z _ {i 2} + z _ {i 3} - 2 \quad \text { for } i \in G _ {1}\tag{1.4}
$$

$$
M (s l _ {1} + s l _ {2}) + M z _ {i} ^ {*} \geq z _ {i 1} + z _ {i 2} + z _ {i 3} \quad \text { for } i \in G _ {2}\tag{1.5}
$$

$$
M (2 - s l _ {1} - s l _ {2}) + M z _ {i} ^ {*} \geq z _ {i 1} + z _ {i 2} + z _ {i 3} \quad \mathrm{for} i \in G _ {1}
$$

$$
M (2 - s l _ {1} - s l _ {2}) + z _ {i} ^ {*} \geq z _ {i 1} + z _ {i 2} + z _ {i 3} - 2 \quad \text { for } i \in G _ {2}\tag{1.6}
$$

1:7

$$
M (1 + s l _ {1} - s l _ {2}) + z _ {i} ^ {*} \geq z _ {i 1} - M w _ {i}
$$

$$
\text { for } i \in G _ {1}\tag{1.8}
$$

$$
M (1 + s l _ {1} - s l _ {2}) + M z _ {i} ^ {*} \geq z _ {i 2} + z _ {i 3} - M (1 - w _ {i}) \quad \text { for } i \in G _ {1}\tag{1.9}
$$

$$
M (1 + s l _ {1} - s l _ {2}) + z _ {i} ^ {*} \geq z _ {i 1}
$$

$$
\text { for } i \in G _ {2}\tag{1.10}
$$

$$
M (1 + s l _ {1} - s l _ {2}) + z _ {i} ^ {*} \geq z _ {i 2} + z _ {i 3} - 1
$$

$$
\text { for } i \in G _ {2}\tag{1.11}
$$

$$
M (1 - s l _ {1} + s l _ {2}) + z _ {i} ^ {*} \geq z _ {i 1}
$$

$$
\text { for } i \in G _ {1}\tag{1.12}
$$

$$
M (1 - s l _ {1} + s l _ {2}) + z _ {i} ^ {*} \geq z _ {i 2} + z _ {i 3} - 1
$$

$$
\text { for } i \in G _ {1}\tag{1.13}
$$

$$
M (1 - s l _ {1} + s l _ {2}) + z _ {i} ^ {*} \geq z _ {i 1} - M w _ {i}
$$

$$
\text { for } i \in G _ {2}\tag{1.14}
$$

$$
M (1 - s l _ {1} + s l _ {2}) + M z _ {i} ^ {*} \geq z _ {i 2} + z _ {i 3} - M (1 - w _ {i})
$$

$$
\text { for } i \in G _ {2}\tag{1.15}
$$

$$
\sum_ {j = 1} ^ {n} \sum_ {d = 1} ^ {3} x _ {j d} = 1
$$

normalization

$$
z _ {i} ^ {*} \in \{0, 1 \}\tag{1.16}
$$

$$
i \in G\tag{1.17}
$$

$$
z _ {i d} \in \{0, 1 \}
$$

$$
i \in G, d = 1, 2, 3\tag{1.18}
$$

$$
w _ {i} \in \{0, 1 \}
$$

$$
i \in G\tag{1.19}
$$

$$
s l _ {k} \in \{0, 1 \}
$$

$$
k = 1, 2\tag{1.20}
$$

$x ,$ <sub>b</sub> unrestricted

1:21

The normalization constraint (1.16) sets the sum of al $x _ { j }$ variables to 1 (or any constant value), and is necessary to avoid problems arising from rotations or translations of the data and to be able to handle negative data. To cover the possible cases, this normalization must utilize both a positive and a negative constant term $( \mathrm { i } . \mathrm { e } . , - 1$ as well as 1). We have chosen the positive variant for convenience, but more general considerations about this and other forms of normalization are discussed in [14].

Although this model performs well for $d ^ { * } { = } 3$ (as shown later in our Experiments and results section), it has a clear limitation: the formulation strongly depends on $d ^ { * } ,$ which is clearly a disadvantage. Also, as $d ^ { * }$ increases the number of tree types increases at the rate of $2 ^ { d ^ { * } }$ and so do the binary slicing variables. Given these limitations, we developed a general model for CDTs which, on one hand, introduces the limitation of allowing misclassi<sup>fi</sup>cations only at depth $d = d ^ { * } .$ But, on the other hand, it is fully general for any given maximum depth and the number of variables grows linearly with $d ^ { * } .$

## 3.2. A model for cutting decision trees

For each depth d we use variables $x _ { d } ,$ b and $z _ { i d } ,$ corresponding to the same variables of the VDT model. Since misclassi<sup>fi</sup>cations at intermediate depths are not allowed, now the objective function involves only the last level of the tree:

$$
\text { Minimize } \sum_ {i \in G} z _ {i d ^ {*}}
$$

Note that, at each depth d of a CDT, one group is entirely correctly classi<sup>fi</sup>ed. Otherwise, there would be forbidden misclassi<sup>fi</sup>cations. For each depth $d = 1 , \ldots d ^ { * } - 1 ,$ a binary variable y indicates which group is correctly classi<sup>fi</sup>ed at depth d:

0 if all of8 $G _ { 1 }$ is correctly classified by hyperplane $h _ { d }$ according to Eq: 1 ; y<sub>d</sub> = 1 if all of $G _ { 2 }$ is correctly classified by hyperplane $h _ { d }$ according to Eq: 1

This de<sup>fi</sup>nition implies that if $y _ { d } = 0$ , then $z _ { i d } = 0$ for all $i \in G _ { 1 } .$ Conversely, if $y _ { d } = 1$ , then $z _ { i d } = 0$ for all $i \in G _ { 2 } .$ . At any given depth d except the <sup>fi</sup>nal one,

$$
y _ {d} \cdot z _ {i d} \quad \text {   for   all   } i \in G _ {1}
$$

$$
1 - y _ {d} \cdot z _ {i d} \quad \text { for   all } i \in G _ {2}
$$

so that all elements of either group $G _ { 1 }$ or $G _ { 2 }$ are correctly classi<sup>fi</sup>ed. Also, variable $y _ { d }$ automatically determines the direction in which the tree grows at depth d: if $y _ { d } = 0$ , the tree grows to the left (Fig. 4a). If $y _ { d } = 1 ,$ , the tree grows to the right (Fig. 4b). Whether or not element i falls into the leaf node at level d is indicated by the binary variables $\nu _ { i d }$ (one for each element i∈G and depth $d = 1 , . . . , d ^ { * } - 1 )$

$$
v _ {i d} = \left\{ \begin{array}{l} 0 \text {   if   } i \text {   does   not   fall   into   the   leaf   node   at   depth   } d. \\ 1 \text {   if   } i \text {   falls   into   the   leaf   node   at   depth   } d. \end{array} \right.
$$

The relationships among $y _ { d } , \nu _ { i d }$ and $z _ { i d }$ are represented in Fig. 4. Considering Fig. 4a (Fig. 4b is analogous), the objects of $G _ { 2 }$ falling into the leaf node have $z _ { i d } = 0$ and $\nu _ { i d } = 1$ , and the objects of $G _ { 2 }$ falling into the internal node at depth $d + 1$ have $z _ { i d } = 1$ and ${ \nu } _ { i d } = 0 .$ . Meanwhile, the objects of $G _ { 1 } ,$ which all fall into the internal node at depth $d + 1 ,$ have $z _ { i d } = 0$ and ${ \nu _ { i d } } = 0$ . These conditions are expressed through the constraints:

$$
v _ {i d} \leq y _ {d} \quad i \in G _ {1}, d = 1, \dots , d ^ {*} - 1
$$

$$
v _ {i d} \leq 1 - y _ {d} \quad i \in G _ {2}, d = 1, \dots , d ^ {*} - 1
$$

$$
v _ {i d} \leq 1 - z _ {i d} \quad i \in G, d = 1, \dots , d ^ {*} - 1
$$

It follows that the necessary conditions for an element i to be misclassi<sup>fi</sup>ed by a CDT are:

1. It does not fall into any leaf at depth $d { < } d ^ { * }$ ; that is, ${ \nu } _ { i d } = 0$ for each $d { < } d ^ { * }$ ;

2. The last hyperplane misclassi<sup>fi</sup>es it, that is $z _ { i d ^ { * } } = 1$

Then, the hyperplane constraints become:

$$
A _ {i} x _ {d} - M \left(\sum_ {h = 1} ^ {d - 1} v _ {i h} + z _ {i d}\right) \leq b _ {d} - \varepsilon \quad i \in G _ {1}, d = 1, \dots , d ^ {*}
$$

$$
A _ {i} x _ {d} + M \left(\sum_ {h = 1} ^ {d - 1} v _ {i h} + z _ {i d}\right) \geq b _ {d} + \varepsilon \quad i \in G _ {2}, d = 1, \dots , d ^ {*}
$$

Thus, the complete formulation of the CDT model is:

Minimize $: \sum _ { i \in G } z _ { i D }$

2:1

Subject to:

$$
A _ {i} x _ {d} - M \left(\sum_ {h = 1} ^ {d - 1} v _ {i h} + z _ {i d}\right) \leq b _ {d} - \varepsilon \quad i \in G _ {1}, d = 1, \dots , d ^ {*}\tag{2.2}
$$

$$
A _ {i} x _ {d} + M \left(\sum_ {h = 1} ^ {d - 1} v _ {i h} + z _ {i d}\right) \geq b _ {d} + \varepsilon \quad i \in G _ {2}, d = 1, \dots , d ^ {*}\tag{2.3}
$$

$$
y _ {d} \geq z _ {i d} \quad i \in G _ {1}, d = 1, \dots , d ^ {*} - 1\tag{2.4}
$$

$$
1 - y _ {d} \geq z _ {i d} \quad i \in G _ {2} d = 1, \dots , d ^ {*} - 1\tag{2.5}
$$

$$
v _ {i d} \leq y _ {d} \quad i \in G _ {1}, d = 1, \dots , d ^ {*} - 1\tag{2.6}
$$

$$
v _ {i d} \leq 1 - y _ {d} \quad i \in G _ {2}, d = 1, \dots , d ^ {*} - 1\tag{2.7}
$$

$$
v _ {i d} \leq 1 - z _ {i d} \quad i \in G, d = 1, \dots , d ^ {*} - 1\tag{2.8}
$$

$$
\sum_ {d = 1} ^ {D} \sum_ {j = 1} ^ {F} x _ {j d} = 1 \quad \text {   "Normalization"   }\tag{2.9}
$$

$$
x _ {d}, b _ {d} \text { unrestricted } d = 1, \dots , d ^ {*}\tag{2.10}
$$

$$
z _ {i d} \in \{0, 1 \} \quad d = 1, \dots , d ^ {*}\tag{2.11}
$$

$$
y _ {i d} \in \{0, 1 \} \quad d = 1,..., d ^ {*} - 1\tag{2.12}
$$

$$
0 \leq v _ {i d} \leq 1 \quad d = 1, \dots , d ^ {*} - 1\tag{2.13}
$$

Since the objective functions of both VDT and CDT models aim at minimizing the number of misclassi<sup>fi</sup>ed points, both models may have multiple equivalent optimal solutions of value v, each corresponding to a set of misclassi<sup>fi</sup>ed points whose cardinality is v. A possible improvement is to de<sup>fi</sup>ne an objective function that has the second goal of maximizing the distance of the correctly classi<sup>fi</sup>ed points to the misclassi<sup>fi</sup>cation region.

## 4. Experiments and results

We tested our models on two benchmark data sets from real-world applications, providing a basis to compare our outcomes with other models. In particular, the performance of the VDT and CDT models is compared to our implementation of the piecewise-linear model proposed by [12], which separates the two groups with 3 hyperplanes and requires one group to lie in a convex region. We <sup>fi</sup>rst tested the 3 models on the Japanese Banks data set, provided by [23], which Glen showed to be separable by three hyperplanes. For this reason, we used depth $d ^ { * } { = } 3$ for all of our tests. In order to eliminate large discrepancies in scale among the attribute values, we <sup>fi</sup>rst standardized the data using the following standardization:

$$
V _ {i j} = \frac {(v _ {i j} - \overline {{v}} _ {j})}{s _ {j}},
$$

where $V _ { i j }$ is the standardized value of attribute j for element $i , \nu _ { i j }$ is the original value of attribute j for element $i , \overline { { \mathsf { V } } } _ { j }$ is the sample mean for attribute j and $s _ { j }$ is the sample standard deviation for attribute j.

We used the leave-one-out (LOO) testing procedure, which is an n-fold cross validation, where n is the cardinality of the data set (in the Japanese Banks data set, $n = 1 0 0 )$ . The LOO “hit rate” is the percentage of correct classi<sup>fi</sup>cations of the holdout element with respect to the total number of tests performed [8]. We treated ε as a parameter in all three models (VDT, CDT, and Glen), testing for various “separation zone” widths. We ran Glen's model twice, alternating the convexity requirement between $G _ { 1 }$ and $G _ { 2 } ,$ , and recorded the outcome that produced the best LOO classi<sup>fi</sup>cation. Even if our main goal is to compare against Glen (see [12]), we also report the results obtained by OC1 and SVM. We used the implementation of OC1 available at http://www.cs.jhu.edu/ \~salzberg/announce-oc1.html (accessed on 5th December 2008), and the implementation of SVMs called SMO, available in Weka [27]. All tests were performed using CPLEX version 10.0, on a Dell Dimension 8400 workstation equipped with a Pentium 4 processor at 3.60 GHz and 1.0 GB RAM. We used parameter $M = 1 0 0 0$ Tables 1 and 2 summarize our results.

As Table 1 shows, both tree-based models perform comparatively well and neither dominates the other. However, in terms of computational complexity and scalability, the CDT model shows a slight advantage even at the present level (although $2 ^ { 3 }$ , which identi<sup>fi</sup>es the complexity of the VDT model, is not a large number). Compared to Glen in terms of testing accuracy, our models perform better in the majority of cases. Furthermore, on average, each LOO test (meant as the set of all 100 runs, each composed by training and testing the classi<sup>fi</sup>er) takes 245.4 s for the VDT model and 100.9 s for the CDT model. Our implementation of Glen's piecewise-linear model takes an average of 228.3 s for each LOO test. Notably, our models obtain a higher accuracy than OC1 and SVM.

![](/api/attachments/SXTCM6EW/fulltext/images/ec5d06f4027bd855b7fab65caf28d663979e37971845b636ef7bc57991917cdc.jpg)  
Table 1  
Fig. 4. Relation among $y _ { d } , z _ { i d }$ and $\nu _ { i d } . \operatorname { I f } y _ { d } = 0 ( \mathsf { a } ) ,$ , the tree grows to the left, then the objects of $G _ { 2 }$ that fall on the right (into a leaf node associated with $G _ { 2 } )$ are correctly classi<sup>fi</sup>ed by the tree at depth $d \left( z _ { i d } = 0 , \nu _ { i d } = 1 \right)$ . Conversely, objects of both groups may fall on the left: those o $\lceil G _ { 1 }$ have $z _ { i d } = 0 , \nu _ { i d } = 0$ , those of $G _ { 2 }$ have $z _ { i d } = 1 , \nu _ { i d } = 0 . \operatorname { I f } y _ { d } = 1 ( \mathrm { b }$ ), the situation is symmetric.

Next, we tested our models on another well-known data set: the Wisconsin Breast Cancer database, available online from the UCI data management repository (http://archive.ics.uci.edu/ml/ accessed on 5th December 2008). The data set consists of 683 patients screened for breast cancer (cases with missing values excluded), and 9 attributes per case. The class variable is binary, representing a benign or a malignant tumor. Since the domain and scale of all the descriptive attributes are the same, no standardization of the data was necessary.

As with the Japanese Banks, we ran various tests for different values of ε. It should be noted that for these tests, given the size of the data set, we decided to set a time limit of 120 s per holdout element test, at which time we recorded the best solution found. We found that, in most cases, the solution was either optimal (0 misclassi<sup>fi</sup>cations in the training set) or very close to optimal (1 or 2 misclassi<sup>fi</sup>cations). The trade-off between classi<sup>fi</sup>cation accuracy and the time to obtain an optimal solution greatly justi<sup>fi</sup>ed the use of a time limit. Table 3 summarizes the results for $\varepsilon = 0 . 0 0 0 0 4 , 0 . 0 0 0 0 5$ and 0.00006. We ran experiments with different orders of magnitude for $\varepsilon ,$ but the results did not vary signi<sup>fi</sup>cantly from the ones reported here.

LOO hit rates for Japanese Banks.

<table><tr><td>ε</td><td>VDT</td><td>CDT</td><td>Glen</td><td>SVM</td><td>OC1</td></tr><tr><td>0.0005</td><td>84</td><td>84</td><td>86</td><td>87</td><td>80</td></tr><tr><td>0.0010</td><td>89</td><td>88</td><td>86</td><td></td><td></td></tr><tr><td>0.0100</td><td>88</td><td>88</td><td>85</td><td></td><td></td></tr><tr><td>0.0200</td><td>86</td><td>90</td><td>85</td><td></td><td></td></tr><tr><td>0.0300</td><td>87</td><td>86</td><td>81</td><td></td><td></td></tr><tr><td>0.0400</td><td>92</td><td>89</td><td>85</td><td></td><td></td></tr><tr><td>0.0450</td><td>88</td><td>90</td><td>90</td><td></td><td></td></tr></table>

Table 2  
Time (in seconds) for each LOO test for the Japanese Banks data set.

<table><tr><td>ε</td><td>VDT</td><td>CDT</td><td>Glen</td><td>SVM</td><td>OC1</td></tr><tr><td>0.0005</td><td>201.0</td><td>7.5</td><td>126.9</td><td>10.2</td><td>181.9</td></tr><tr><td>0.0010</td><td>240.2</td><td>8.5</td><td>126.6</td><td></td><td></td></tr><tr><td>0.0100</td><td>245.8</td><td>165.2</td><td>113.6</td><td></td><td></td></tr><tr><td>0.0200</td><td>258.1</td><td>120.5</td><td>142.2</td><td></td><td></td></tr><tr><td>0.0300</td><td>256.4</td><td>117.4</td><td>168.1</td><td></td><td></td></tr><tr><td>0.0400</td><td>254.4</td><td>186.3</td><td>414.4</td><td></td><td></td></tr><tr><td>0.0450</td><td>261.9</td><td>101.0</td><td>506.2</td><td></td><td></td></tr></table>

As Table 3 shows, the CDT model outperforms both the VDT model and Glen's model. It must be noted that our models can separate this data set by using three hyperplanes, while the piecewise-linear model, due to its convexity requirement, fails to do so. Both OC1 and SVM obtain a higher accuracy than CDT, but solving CDT takes less time (see Table 4) than OC1 and may <sup>fi</sup>nd interpretable rules, unlike SVM. CDT is almost twice as fast as Glen, while the VDT model does not scale up ef<sup>fi</sup>ciently to this large data set (average LOO test times were above 12,000 s). Although CDT is signi<sup>fi</sup>cantly faster than Glen, we believe that it would be computationally impractical to solve exactly our model in order to classify very large data sets (e.g. hundreds of attributes and millions of observations).

For both data sets, we performed a paired Student's t-test to assess whether there is a statistically signi<sup>fi</sup>cant difference between the accuracy obtained by our methods and the one obtained by Glen, for the same value of ε. The accuracy obtained by CDT is signi<sup>fi</sup>cantly higher $( \mathrm { a t } \ \alpha { = } 0 . 0 5 )$ than the one obtained by Glen (the p-value is equal to 0.0253 for the test on the Japanese Banks data set, and 0.004 for the one on the Breast Cancer data set). On the other hand, the accuracy obtained by VDT is not signi<sup>fi</sup>cantly higher than the one obtained by Glen. Therefore, we can conclude that CDT dominates Glen's approach.

In terms of the model complexity, Table 5 shows the number of binary variables, total variables, and constraints for each model. Glen's model is very complex, in that it uses a large number of binary variables, both in absolute terms and in comparison to the number of total variables. Although Glen's model uses fewer constraints than our models, its hyperplane constraints involve the use of two types of binary variables (due to the convexity requirement) and twice the number of continuous variables.

Table 3  
LOO hit rates for Breast Cancer data set.

<table><tr><td>ε</td><td>VDT</td><td>CDT</td><td>Glen</td><td>SVM</td><td>OC1</td></tr><tr><td>0.00004</td><td>80.4</td><td>92.8</td><td>84.6</td><td>97.07</td><td>96.19</td></tr><tr><td>0.00005</td><td>86.6</td><td>94.2</td><td>84.6</td><td></td><td></td></tr><tr><td>0.00006</td><td>84.2</td><td>91.5</td><td>84.6</td><td></td><td></td></tr></table>

Table 4  
Average time (in seconds) for each LOO test for the Breast Cancer data set.

<table><tr><td>VDT</td><td>CDT</td><td>Glen</td><td>SVM</td><td>OC1</td></tr><tr><td>12,000</td><td>600</td><td>1200</td><td>86</td><td>1232.1</td></tr></table>

Table 5  
Size of the optimization problems for Breast Cancer data.

<table><tr><td>Model characteristics</td><td>VDT</td><td>CDT</td><td>Glen</td></tr><tr><td>Binary variables</td><td>3412</td><td>2048</td><td>4396</td></tr><tr><td>Total variables</td><td>3442</td><td>4124</td><td>4453</td></tr><tr><td>Equality constraints</td><td>1</td><td>1</td><td>3</td></tr><tr><td>Total constraints</td><td>6139</td><td>6139</td><td>4574</td></tr></table>

## 5. Conclusions and future research

VDTs and CDTs constitute an innovation in the area of decision trees that has a broad application to important problems in real-world data mining. Our models produce particular tree structures that are constrained not to grow in width. The bene<sup>fi</sup>t of this constraint consists in the simplicity of the models and – in the case of the CDT – their straight-forward generalization to any maximum depth. Our results show that this apparent limitation does not affect the accuracy obtained.

Both models compare favorably in accuracy and speed to the main previous mixed integer Multi-hyperplane model. The improved speed promises to have valuable consequences for solving larger and more complex classi<sup>fi</sup>cation problems. Finally, the ability of our approach to operate without being con<sup>fi</sup>ned by the convexity requirement of the piecewise-linear model yields additional advantages for dealing with problems where this requirement is inappropriate. On the other hand, our approach would not be suitable to classify very large data sets; furthermore it can handle only cross-sectional data, i.e. the observations in the data set are independent items that can be thought of as belonging to a sample taken at the same time. To perform a longitudinal analysis, where information relative to different times is available for each items, an appropriate design of the attributes is needed to represent the trend of the characteristics of each item through time.

The advances in modeling <sup>fl</sup>exibility and in classi<sup>fi</sup>cation power made possible by our new formulations represent one more link in the chain of contributions originally stimulated by the goal programming model conception of [4]. The present formulations may in this sense be viewed as a way of generalizing and adapting the goal programming framework to include special forms of discrete conditions that enable it to apply more effectively to non-convex decision spaces in the context of classi<sup>fi</sup>cation analysis.

We envision several avenues for future research. First, our mixed integer models exhibit special structure that makes them susceptible to tailored accelerated and scalable solution methods. These tailored methods can take greater advantage of the linear programming relaxations of these models than customary procedures in today's state-of-the-art MIP software packages, by means of post-optimality analysis. In addition, the mechanisms underlying linear programming post-optimality analysis can also be used to generate new attributes for classi<sup>fi</sup>cation, to yield special non-linear and logic-based combinations of the original attributes. This provides a dynamic method for generating kernel functions and gives a new design for treating such functions that can supplement the usual procedures for creating kernel functions proposed in the SVM domain. The mutually reinforcing nature of these research avenues strongly motivates their exploration in future work as a natural outgrowth of our present study.

## References

[1] P.L. Abad, W.J. Banks, New LP based heuristics for the classi<sup>fi</sup>cation problem, European Journal of Operational Research 67 (1993) 88–100.

[2] K.P. Bennett, J.A. Blue, A support vector machine approach to decision trees, in: J.A. Blue (Ed.), Proceedings of the IEEE World Congress on Computational Intelligence, Anchorage, AK, USA, 1998, pp. 2396–2401.

[3] A. Charnes, W.W. Cooper, Management models and industrial applications of linear programming, Wiley, New York, 1961.

[4] A. Charnes, W.W. Cooper, R.O Ferguson, Optimal estimation of executive compensation by linear programming, Management Science 1 (1955) 138–151

[5] M. Chau, H. Chen, A machine learning approach to web page <sup>fi</sup>ltering using content and structure analysis, Decision Support Systems 44 (2008) 482–494.

[6] K. Cheung, J.T. Kwok, M. Law, K. Tsui, Mining customer product ratings for personalized marketing, Decision Support Systems 35 (2003) 231–243.

[7] N. Cristianini, J. Shawe-Taylor, An Introduction to Support Vector Machines and Other Kernel-based Learning Methods, Cambridge University Press, New York, 2000.

[8] A.J. Feelders, Statistical Concepts, Intelligent Data Analysis, Springer-Verlag New York Inc., New York, 2003.

[9] N. Freed, F. Glover, Simple but powerful goal programming models for discriminant problems, European Journal of Operational Research 7 (1981) 44–60.

[10] J.J. Glen, Integer programming methods for normalisation and variable selection in mathematical programming discriminant analysis models, Journal of the Operational Research Society 50 (1999) 1043–1053.

[11] J.J. Glen, An iterative mixed integer programming method for classi<sup>fi</sup>cation accuracy maximizing discriminant analysis, Computers & Operations Research 30 (2003) 181–198.

[12] J.J. Glen, Mathematical programming models for piecewise-linear discriminant analysis, Journal of the Operational Research Society 56 (2004) 331–341.

[13] F. Glover, Improved linear programming models for discriminant analysis⁎, Decision Sciences 21 (1990) 771–785.

[14] F. Glover, G. Kochenberger, M. Better, Improved Classi<sup>fi</sup>cation and Discrimination by Successive Hyperplane and Multi-hyperplane Separation, Working Paper, University of Colorado, Boulder, Boulder, 2006.

[15] J. Han, M. Kamber, Data Mining: Concepts and Techniques, Morgan Kaufmann Publishers Inc., San Francisco, CA, 2000

[16] H. Ince, T.B. Trafalis, A hybrid model for exchange rate prediction, Decision Support Systems 42 (2006) 1054–1062.

[17] X. Li, A scalable decision tree system and its application in pattern recognition and intrusion detection, Decision Support Systems 41 (2005) 112–130

[18] S.K. Murthy, S. Kasif, S. Salzberg, A system for the induction of oblique decision trees, Journal of Arti<sup>fi</sup>cial Intelligence Research 2 (1994) 1–32.

[19] Y. Peng, G. Kou, Y. Shi, Z. Chen, A multi-criteria convex quadratic programming model for credit data analysis, Decision Support Systems 44 (2008) 1016–1030

[20] J.R. Quinlan, Induction of decision trees, Machine Learning 1 (1986) 81–106.

[21] L. Rokach, O. Maimon, Top-down induction of decision trees classi<sup>fi</sup>ers – a survey, IEEE Transactions on Systems, Man, and Cybernetics Part C: Applications and Reviews 35 (2005) 476-487

[22] A. Stam, C.T. Ragsdale, On the classi<sup>fi</sup>cation gap in mathematical programmingbased approaches to the discriminant problem, Naval Research Logistics 39 (1992) 545–559.

[23] T. Sueyoshi, Extended DEA-discriminant analysis, European Journal of Operational Research 131 (2001) 324–351.

[24] T. Sueyoshi, M. Goto, DEA-DA for bankruptcy-based performance assessment: misclassi<sup>fi</sup>cation analysis of Japanese Construction Industry, European Journal of Operational Research 199 (2009) 579–594.

[25] T. Sueyoshi, M. Goto, Methodological Comparison between DEA (Data Envelopment Analysis) and DEA-DA (Discriminant Analysis) from the perspective of bankruptcy assessment, European Journal of Operational Research, Accepted Manuscript 199 (2009) 561–575.

[26] M. Sun, M. Xiong, A mathematical programming approach for gene selection and tissue classification. Bioinformatics 19 (2003) 1243–1251.

[27] I.H. Witten, E. Frank, Data mining: practical machine learning tools and techniques, Morgan Kaufman, Boston, MA, 2005.

Dr. Marco Better is the Director of Custom Solutions of OptTek Systems, Inc. He obtained his Ph.D. in Operations Research from the Leeds School of Business of the University of Colorado at Boulder. He holds a B.S. in industrial engineering and an M.B.A. Dr. Better has over 15 years of professional work experience in the automobile, banking, and telecommunications industries, both in the US and in Latin America. His current interests lie in the application of optimization and data mining technology to solve complex problems in the industry.

Dr. Fred Glover is Chief Technology Of<sup>fi</sup>cer for OptTek Systems, Inc., and a Distinguished Professor at the University of Colorado, Boulder. He has authored or co-authored more than 370 published articles and eight books in the <sup>fi</sup>elds of mathematical optimization, computer science and arti<sup>fi</sup>cial intelligence. He is the recipient of the von Neumann Theory Prize, and is an elected member of the National Academy of Engineering. His numerous other awards include those from the American Association for the Advancement of Science (AAAS), the NATO Division of Scienti<sup>fi</sup>c Affairs, the Institute of Operations Research and Management Science (INFORMS), the Decision Sciences Institute (DSI), the Energy Research Institute (ERI), the Institute of Cybernetics of the Ukrainian Academy of Science, and the Miller Institute for Basic Research in Science.

Michele Samorani is a PhD student at the Leeds School of Business of the University of Colorado at Boulder His research interests include the application of operations research to solve data mining problems and the application of data mining techniques to enhance optimization procedures.
