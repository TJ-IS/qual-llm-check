---
otero_id: 14084
otero_key: "A2HHEW2G"
title: "Measuring interestingness of discovered skewed patterns in data cubes"
authors: "Navin Kumar; Aryya Gangopadhyay; Sanjay Bapna; George Karabatis; Zhiyuan Chen"
year: "2008"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2008.08.003"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Measuring interestingness of discovered skewed patterns in data cubes

Navin Kumar <sup>a</sup>, Aryya Gangopadhyay <sup>b,</sup>⁎, Sanjay Bapna <sup>c</sup>, George Karabatis <sup>b</sup>, Zhiyuan Chen <sup>b</sup>

<sup>a</sup> Advisory Board Company, United States

<sup>b</sup> Department of Information Systems, University of Maryland Baltimore County (UMBC), United States

<sup>c</sup> Department of Information Systems, Morgan State University, United States

## a r t i c l e i n f o

Article history: Received 18 August 2006 Received in revised form 15 August 2008 Accepted 25 August 2008 Available online 13 September 2008

Keywords: OLAP Data cube navigation Data warehousing Navigation rules Skewness

## a b s t r a c t

This paper describes a methodology of OLAP cube navigation to identify interesting surprises by using a skewness based approach. Three different measures of interestingness of navigation rules are proposed. The navigation rules are examined for their interestingness in terms of their expectedness of skewness from neighborhood rules. A novel Axis Shift Theory (AST) to determine interesting navigation paths is presented along with an attribute in<sup>fl</sup>uence approach for generalization of rules, which measures the interestingness of dimensional attributes and their relative in<sup>fl</sup>uence on navigation paths. Detailed examples and extensive experiments demonstrate the effectiveness of interestingness of navigation rules.

Published by Elsevier B.V.

## 1. Introduction

With an ever-increasing volume of data collected and archived by organizations, it has become critical to ef<sup>fi</sup>ciently and effectively navigate through large, multidimensional cubes to identify interesting hidden surprises. While On-Line Analytical Processing (OLAP) tools provide various operations such as roll-up, drill-down, and slicingdicing for viewing datasets from different angles [13], they offer only minimal guidance to the users in the actual knowledge discovery process. Moreover, the viewing possibilities are combinatorially explosive in number, making it a daunting task to manually detect interesting hidden surprises in the voluminous and complex lattices of multidimensional cubes.

As the size of database increases, the number of navigation paths grows which may overwhelm the users. It then becomes dif<sup>fi</sup>cult for users to manually go through enormous sets of rules to identify interesting ones. This problem could be alleviated if users were presented with a short list of rules, or a list of navigation paths for analytical studies. We approach the issue of cube navigation by using skewness based navigation rules, also called sk-navigation rules, which identify interesting surprises in data cube lattices. In this context, a surprise reveals how anomalous a set of transactions is, when compared with another set of closely related transactions in the fact table. The anomalous transactions could be de<sup>fi</sup>ned either by few outliers in the datasets in<sup>fl</sup>uencing the aggregated datasets or by a group of transactions showing substantial difference on facts, such as pro<sup>fi</sup>t or cost, from the remaining transactions. Because the notion of a surprise is an intuitive one, different users may have different impressions on what constitutes a surprise. Our rule-driven system allows the users to control the knowledge discovery process by letting them set the baseline for surprises by simply adjusting the skewness level of signi<sup>fi</sup>cance.

The contributions of this paper are as follows. We evaluate the interestingness of discovered sk-navigation rules and then assist users to selectively navigate along the paths that lead to interesting surprises in data lattices. Using the measures of interestingness, users can simply prune the large number of generated rules to only the ones that are interesting. Since sk-navigation rules are discovered based on a measure of skewness, we adopt the interestingness of rules in terms of their expectedness of skewness from the rules in the neighborhood. We also introduce an Axis Shift Theory (AST) to determine interesting navigation paths based on the global measures of axis shifts of sk-navigation rules. The rules complement each other to yield interesting navigation paths leading to low-level interesting surprises. Lastly, we introduce a method of generalizing sk-navigation rules to identify interesting dimensional attributes to augment cube navigation. Speci<sup>fi</sup>cally, we measure the interestingness of attributes in terms of their attribute influence, a metric based on the unique navigation paths provided by sk-navigation rules.

The rest of the paper is organized as follows. Section 2 presents the related work while Section 3 provides the preliminaries on data cube model and discovery of sk-navigation rules. In Section 4 we present the different measures of interestingness of sk-navigation rules, and in

Section 5 we discuss applying our methodology in the context of a real-world application. An experimental evaluation of interestingness is presented in Section 6 followed by a comparison with previous work in Section 7. Section 8 presents the conclusions and future work.

## 2. Related work

Interestingness measures are used to <sup>fi</sup>lter out irrelevant or mundane patterns from a set of mined patterns such as association or classi<sup>fi</sup>cation rules. A large number of interestingness measures have been proposed in the literature on data mining and knowledge discovery (see [8,19] for a comprehensive discussion). These interestingness measures can be categorized into objective, subjective, and semantic measures. Objective measures require no user input and can be further categorized into probability-based measures and formdependent measures. Thirty eight probability-based objective measures have been discussed in [8], some examples of which are support, coverage, example and counter example rate, and Laplace correction. Form-dependent objective measures [4,5,7] such as neighborhoodbased unexpectedness, surprisingness and logical redundancy have been applied for ranking and clustering patterns such as association rules. Subjective interestingness measures require some form of user input in determining the utility of a mined pattern [18,21,27]. Utilitybased measures have been used for objective-oriented association mining (for example, [26,33]), with user-speci<sup>fi</sup>ed objectives. In addition, numerous interestingness measures for summaries have been proposed in the literature including diversity (e.g., [12,33]), conciseness and generality [5], peculiarity [22–25], and surprisingness/unexpectedness [9]. Most of these methods with the exception of [9,10,20,30,32] have been applied for identifying patterns that have been mined from a given static dataset as opposed to providing guidance for navigating through multi-dimensional data cubes of graphs, which is the focus of our paper. Hence, in the rest of this section we focus on those methods that are closely related to our work.

Query driven knowledge discovery [6] and discovery-driven exploration of OLAP data cubes [22–25] have been proposed to address identi<sup>fi</sup>cation of surprises. The authors in [22–23] have used precomputed measures indicating exceptions as surprises. Being precomputed, the surprises cannot be de<sup>fi</sup>ned by users. Furthermore, it is overwhelming for users to examine surprises by looking at data values in a large number of rows and columns. This work was further extended in [24,25] by discovering surprises in unexplored parts of a data cube using maximum entropy principles computed on the aggregate differences. However, these studies deal with aggregated datasets which often hide the characteristic of detailed data: an “extremely high” value and an “extremely ${ \mathsf { l o w } } ^ { * }$ value could be aggregated to a “moderate” value, hiding both extreme values. Other work in the area of subgroup patterns [16] addresses the general problem of de<sup>fi</sup>ning and identifying local subgroups. While important, such methods also presume how a surprise is de<sup>fi</sup>ned and do not provide a generalized navigational methodology. Another recent approach is presented in [5] where the authors use Simpson's paradox as the basis for de<sup>fi</sup>ning surprises in multidimensional data but do not address the navigational techniques to reach surprises of interest. Recently, in [17], skewness based navigation rules for data cube exploration were proposed. These rules provide navigation support to users to explore data cubes at the transaction level. While the authors address the navigational techniques to reach surprises of interest, they focus only on the skewness metric to reach surprises.

In another closely related work, interestingness has been used in attribute selection, for attribute-oriented generalization [2], where the authors examine different strategies for choosing the next attribute for generalization. Also, the discovery of interesting summaries in generalization space graphs has been studied in [17,22], using the expectations of users, and relative variance as an interestingness measure. However, unlike the method described in [17,22] we do not require users to specify probability distributions. In addition we deal with the lowest level transactions instead of summaries.

An examination of interestingness measures for data mining appears in [19] and a comprehensive categorization of interestingness measures including analysis of their properties is found in [8]. A rule trivial to one user may not be trivial to another; therefore, with proper guidance users can explore the ruleset by only examining the rules which match their expectations. System guidance is also necessary because it is unrealistic to expect every discovered rule to be a surprise [31]. We model cube navigation by measures of interestingness of navigation rules, so that the users can quickly identify rules of interest, aided by the system's pruning of uninteresting rules. Our work differs from previous work in the sense that we measure the interestingness of navigation rules by their skewness based differences. We use skeweness measure to discover useful interesting rules. These rules assist in the cube navigation resulting in the identi<sup>fi</sup>cation of interesting paths. The paths together with the selected rules, ensure that users reach interesting low level surprises in data cubes.

## 3. Preliminaries

## 3.1. Overview of the data cube model

Adapting from the terminology given in [29] let us assume that the data cube consists of m dimensions, $d _ { 1 } , d _ { 2 } , . . . , d _ { m } . \mathrm { ~ A ~ }$ dimension $d _ { i }$ is associated with a concept hierarchy containing one or more levels of aggregation. Level $l _ { i j }$ represents the jth level of dimension $d _ { i } ,$ such that $1 \leq j \leq L _ { i }$ where $L _ { i }$ is the number of levels associated with d . A level $l _ { i j }$ contains a set of attributes. Let $\nu _ { i j k }$ be the kth attribute at level $l _ { i j } .$ The facts are numerical measures, usually the objects of analysis. Assume that there are s facts, $f _ { 1 } , f _ { 2 } , . . . , f _ { s }$ in the fact table, and $w _ { p q }$ is the qth value for fact $f _ { p } ,$ where 1≤p≤s, $w _ { p q } \in W _ { p }$ where $W _ { p }$ is the domain of possible values of fact $f _ { p } .$ The fact table contains the complete transaction set $T \mathbf { \tau } = \left[ \tau _ { 1 } , \ \tau _ { 2 } , . . . , \ \tau _ { n } \right]$ where n is the total number of transactions. A transaction, τ is represented as $\{ ( x _ { 1 } , x _ { 2 } , . . . . , x _ { i } , . . . . , x _ { m } ) , ( f _ { 1 } ,$ $f _ { 2 } , . . . , f _ { p } , . . . , f _ { s } ) \}$ , where x is an attribute $\left( \nu _ { i j k } \right)$ from the lowest level $\left( = { \cal L } _ { i } \right)$ of $d _ { i } , \operatorname { a n d } f _ { p }$ is an associated fact. In the data warehouse literature, data cubes formed at different levels of dimensional hierarchies store data at different degrees of aggregation, each of which is called a cuboid. The highest level of aggregation is called the apex cuboid, often denoted as “ALL” [11]. We follow the same nomenclature in this paper. However, instead of storing the aggregates, we utilize the lowest level transactions that are used for calculating the aggregates at each cuboid. Aggregation often hides characteristics of the detailed data: an “extremely high” value and an “extremely low” value can be aggregated to a “moderate” value, hiding both extreme values. Using the lowest level of granularity, the problem of hiding a surprise as a side effect of aggregation is avoided [17].

Fig. 1 illustrates a partial lattice for a grocery database with product (P), time (T) and store (S) dimensions. Every node in the lattice corresponds to a set of transactions, also referred to as a dataset. A cuboid consists of a set of nodes. For example, $\left( P _ { 1 } \right)$ represents a one-dimensional cuboid containing level-1 (product category) for the product dimension. Similarly, $\left( P _ { 1 } , T _ { 1 } \right)$ represents a two-dimensional cuboid constructed by level-1 of product (category) and time (year) dimensions. Given m dimensions, latt(m) is a lattice of cuboids, each being a distinct combination of hierarchical levels of dimensions. An edge shows the possible navigation from one cuboid to another, for instance from (P ) to $( P _ { 1 } , T _ { 1 } ) .$ . A navigation path describes a traversal through the nodes in the lattice. For example, the path $( P _ { 1 } ) {  } ( P _ { 2 } ) {  } ( P _ { 2 } , T _ { 1 } ) {  } ( P _ { 2 } , T _ { 1 } , S _ { 1 } )$ suggests that a user <sup>fi</sup>rst looks at a node at $\left( P _ { 1 } \right)$ Product category, drills down to a node at $\left( P _ { 2 } \right)$ product subcategory, and subsequently views the nodes at $\left( P _ { 2 } , T _ { 1 } \right)$ product subcategory and year and <sup>fi</sup>nally $\left( P _ { 2 } , T _ { 1 } , S _ { 1 } \right)$ product subcategory, year, and region. Given a node in a navigation path, subsequent nodes are determined either by drilling down one dimension from a preceding node or by including a new dimension that does not exist in the preceding node. One drill-down operation may only involve navigation by one level in a given dimension or traversing to a different dimension, but not both. This process may continue until there are no more nodes to traverse. For example, starting from a current node containing the rule $\ " \mathrm { Y e a r } = 1 9 9 2 "$ , the candidate nodes to be examined for traversal include the rules $\{ ^ { * } \mathrm { Q u a r t e r } = \mathrm { Q } 1 - 1 9 9 2 ^ { \circ } , \ ^ { * } \mathrm { Q u a r t e r } = \mathrm { Q } 2 - 1 9 9 2 ^ { \circ } , \ . . . , \ ^ { * } \mathrm { Y e a r } = 1 9 9 2 ^ { \circ }$ and Product Category=Drinks”, …, “Year= 1992 and Region = Eastern”, …}.

![](/api/attachments/A2HHEW2G/fulltext/images/a2866d8edd1e988b26eec91afa6a043171c7f16c6ce36400d06da5a039f7e147.jpg)  
Fig. 1. A partial lattice of cuboids.

## 3.2. Discovery of sk-navigation rules

To discover the surprises in data cubes, the property of skewness, a measure of the asymmetry in data distribution, has been applied in a four-step recursive algorithm [15] as follows. (1) Given a current node, generate a set of candidate nodes, (2) Measure the skewness of candidate nodes, (3) Apply the test of signi<sup>fi</sup>cance of skewness on candidate nodes, and (4) Transform nodes with signi<sup>fi</sup>cant skewness into sk-navigation rules. Each candidate node in the data cube corresponds to a subset of transactions. Thus, the skewness is computed for the sample values of the random variable fact attribute in the set of transactions corresponding to that node e.g., for a node “category= drinks” and fact as pro<sup>fi</sup>t, the skewness of that node is computed over the pro<sup>fi</sup>t values of all transactions with “category=drinks”.

Once a node with signi<sup>fi</sup>cant skewness is identi<sup>fi</sup>ed, it acts as the current node for generating candidate nodes at the next level. The algorithm terminates when either it reaches the lowest level nodes in the lattice, or no more nodes exhibit signi<sup>fi</sup>cant skewness in the current iteration.

An sk-navigation rule skr, as shown below, contains information about the dimensional levels, facts, their corresponding values and the level of signi<sup>fi</sup>cance and skewness.

$$
\begin{array}{l}(d _ {1}: l _ {1 j} = v _ {1 j k}, d _ {2}: l _ {2 j} = v _ {2 j k, \ldots , d _ {i}}: l _ {i j} = v _ {i j k, \ldots , d _ {m}}: l _ {m j} = v _ {m j k}) \rightharpoonup f _ {p}\\\qquad = w _ {p q} \left[ \alpha , \sqrt {b _ {1}} \right].\end{array}
$$

Here α and $\sqrt { b _ { 1 } }$ are the level of signi<sup>fi</sup>cance and skewness of the random variable fact [3,17]. For instance, if the pro<sup>fi</sup>t for a node “category = drinks” is positively skewed at $\alpha { = } 0 . 0 5$ and $\sqrt { b _ { 1 } } = 2 . 6 3$ the corresponding sk-navigation rule would be “product category = drinks → pro<sup>fi</sup>t = sk-high [0.05, 2.63].” relative to its parent node “product category = All”. Sk-high in the consequent means a positive skewness in pro<sup>fi</sup>t. Similarly, a negatively skewed node is represented by sk-low.

A partial discovery of sk-navigation rules is illustrated in Fig. 2. Starting from the sk-navigation rule 2: “year=1993→pro<sup>fi</sup>t=sk-low”, the next set of rules that can be generated are “year=1993: quarter=1993- Q2→pro<sup>fi</sup>t=sk-low”, and “year=1993: quarter=1993-Q4→pro<sup>fi</sup>t=skhigh” assuming that both the two new set of rules are signi<sup>fi</sup>cantly skewed at $\scriptstyle \alpha = 0 . 0 5$ . Cube navigation is facilitated by comparing the discrete sk-high or sk-low values at a prespeci<sup>fi</sup>ed α value for the parent and the child nodes as described in greater details in Section 4.

## 3.3. Cube navigation using sk-navigation rules

We use the discovered sk-navigation rules to assist users in the cube navigation process. A rule is also called a node of surprise, because it essentially represents a lattice node containing a signi<sup>fi</sup>cant skewed pattern relative to its parent. A user begins the navigation with a root node, and drills down to children nodes. Similarly, a node is rolled up by moving to its parent. A navigation path is de<sup>fi</sup>ned by the complete traversal from a root node to a leaf node, and comprises the nodes visited during the traversal.

![](/api/attachments/A2HHEW2G/fulltext/images/2d5d94f2c2f39b1848dcd883c79b11e210560ad9d3293c5dc4f1058be99361dd.jpg)  
Fig. 2. Navigation paths based on sk-navigation rules at α=0.05.

## 4. Interestingness of sk-navigation rules

In this section, we formally de<sup>fi</sup>ne measures of interestingness. Since our cube exploration approach is based on detecting surprises using skewness, we adopt the interestingness of rules in terms of unexpectedness of skewness and explain how sk-navigation rules can yield interesting navigation paths and dimensional attributes. Speci-<sup>fi</sup>cally, we propose three measures of interestingness as follows.

(1) Expectedness of sk-navigation rules. This measure determines interestingness of rules in terms of their unexpected patterns of skewness from the rules in the neighborhood.

(2) Axis shift in navigation paths. This measure identi<sup>fi</sup>es interestingness of navigation paths based on the global measures of axis shifts of sk-navigation rules.

(3) Generalization of sk-navigation rules. This measure quanti<sup>fi</sup>es the interestingness of attributes by computing their in<sup>fl</sup>uence on lattice nodes of surprises.The three measures of interestingness are complementary to each other as each may generate different interesting rules (see examples using a real life data set in Section 5). Put together, these interestingness measures provide a high degree of <sup>fl</sup>exibility to effectively and ef<sup>fi</sup>ciently navigate combinatorially explosive data cubes. We now present each of the three measures in detail.

## 4.1. Expectedness of rules

To determine the interestingness of discovered sk-navigation rules, we introduce a neighborhood-based categorization of rules and then examine the rules for their expectedness based on their skewness. The rules are grouped into three categories, ‘expected’, ‘unexpected’, and ‘not applicable (NA)’, according to speci<sup>fi</sup>c business rules prede<sup>fi</sup>ned on skewness patterns for the pairs of navigation rules. An example of such a business rule is “pro<sup>fi</sup>t increases with lower costs”. A navigation rule is called expected if it complies with other discovered navigation rules, i.e., it exhibits a consistent pattern with respect to the other discovered rules. On the contrary, an unexpected rule indicates a directional change of skewness on pairs of parent-child rules. The antecedents of two rules are identical if they correspond to the same lattice node, whereas they are different if they correspond to parentchild lattice nodes. Let ante(skr ) represent the antecedent of a rule. Let skew $\mathrm { d i f f } ( f _ { p _ { 1 } } , f _ { p _ { 2 } } )$ be the difference in the pattern of skewness of two facts $f _ { p _ { 1 } }$ and $f _ { p _ { 2 } }$ which is determined as follows.

skewXdiff $\left( f _ { p _ { 1 } } , f _ { p _ { 2 } } \right)$

$$
= \left\{ \begin{array}{l} 0, \text {   if   } f _ {p _ {1}} \text {   and   } f _ {p _ {2}} \text {   comply   with   the   business   rule }, \\ 1, \text {   if   } f _ {p _ {1}} \text {   and   } f _ {p _ {2}} \text {   do   not   comply   with   the   business   rule } \end{array} \right\}
$$

An example business rule applied on two facts cost and pro<sup>fi</sup>t is that “the pro<sup>fi</sup>t increases (decreases) when the cost decreases (increases), assuming that the revenue is constant.” Therefore, if two sknavigation rules show positive skewness on pro<sup>fi</sup>t and negative skewness on cost, they comply with the business rule, hence, skew\_diff(pro<sup>fi</sup>t, cost)=0. However, if the navigation rules show the same pattern of skewness (either positive or negative) for both cost and pro<sup>fi</sup>t, they do not satisfy the business rule, thus skew\_diff(pro<sup>fi</sup>t, cost)=1. For example, if pro<sup>fi</sup>t is positively skewed for one navigation rule and negatively skewed for another navigation rule, skew\_diff (pro<sup>fi</sup>t, pro<sup>fi</sup>t) equals 1 for this pair of rules. Note that the skewness difference between two navigation rules for an identical fact, skew\_diff $( f _ { p _ { i } } , f _ { p _ { i } } ) .$ , can also be measured.

We now discuss the three possible cases which measure the expectedness of navigation rules based on the skewness difference as illustrated in Fig. 3. Lattice node 1 is a parent node and lattice node 2 is a child node. The link b is a result of drilling-down, the links a, and c come about due to users examining different facts. The navigation rules sk ${ \dot { \mathbf { \eta } } } _ { i 2 } ,$ skr , and skr are in the neighborhood of navigation rule skr .

![](/api/attachments/A2HHEW2G/fulltext/images/b9a18f854d2305ed780c06815a71d0a119e479b04da4c7ec5968d5981895eac4.jpg)  
Fig. 3. sk-navigation rules and their neighborhood

4.1.1. Case (a) same lattice node, different facts

The navigation rules $\mathsf { s k r } _ { i 1 }$ and $\mathsf { s k r } _ { i 2 }$ represent the same lattice node (identical antecedent) but contain different facts in the consequent i.e. ante $( s \mathbf { k } \mathbf { r } _ { i 1 } ) { = } \mathbf { a n t e } \ ( s \mathbf { k } \mathbf { r } _ { i 2 } )$ and $f _ { \mathrm { p } _ { 1 } } ( s k r _ { i 1 } ) { \neq } f _ { \mathrm { p } _ { 2 } } ( { \mathrm { s k r } } _ { i 2 } ,$ ). The expectedness is measured as follows:

(a) $\mathsf { s k r } _ { i 1 }$ and $\mathsf { s k r } _ { i 2 }$ are expected if skew\_ $\mathrm { d i f f } ( f _ { p _ { 1 } } ( { \sf s k } _ { i 1 } ) , f _ { p _ { 2 } } ( { \sf s k } _ { i 2 } ) ) = 0$ (b) $\mathsf { s k r } _ { i 1 }$ and $\mathsf { s k r } _ { i 2 }$ are unexpected if skew\_ $\mathrm { d i f f } ( f _ { p _ { 1 } } ( \mathsf { s k } _ { i 1 } ) , \mathsf { \bar { f } } _ { p _ { 2 } } ( \mathsf { s k } _ { i 2 } ) ) = 1$ (c) $\mathsf { s k r } _ { i 1 }$ and sk $\Gamma _ { i 2 }$ are NA if there is no business rules that include $f _ { p _ { 1 } }$ and $f _ { p _ { 2 } } .$

Example 1. Let the following set of navigation rules represent different facts at the same lattice node.

skr<sub>1</sub>: $\dot { } ^ { \mathrm { ~ * ~ } } \mathrm { y e a r } = 1 9 9 6 \longrightarrow \mathrm { p r o f i t } = \mathrm { s k } \mathrm { - } \mathrm { h i g h } ^ { \mathrm { * } }$

skr : “year=1996→cost=sk-high”

skr<sub>3</sub>: $\mathrm { ^ { 4 } y e a r = 1 9 9 6 \to t e m p e r a t u r e = s k \mathrm { - } l o w " }$

Assume that a business rule is de<sup>fi</sup>ned on pro<sup>fi</sup>t and cost such that pro<sup>fi</sup>t and cost are negatively correlated. Then, $\mathsf { s k r } _ { 1 }$ is NA when compared with skr but is unexpected when compared to skr .

## 4.1.2. Case (b) different lattice nodes, same fact

The navigation rules $\mathsf { s k r } _ { i 1 }$ and $\mathsf { s k r } _ { j 1 }$ are connected by a parent-child relationship and share the same fact in the consequent, i.e. ante $( \mathsf { s k r } _ { i 1 } ) \subset \mathsf { a n t e } ( \mathsf { s k r } _ { j 1 } )$ and $f _ { \mathfrak { p } _ { 1 } } ( \mathsf { s k r } _ { i 1 } ) \mathop { = } f _ { \mathfrak { p } _ { 1 } } ( \mathsf { s k r } _ { j 1 } )$

Based on the skewness patterns of navigation rules, we measure the expectedness as follows.

(a) $s \mathrm { k r } _ { j 1 }$ is expected if skew\_diff $( f _ { p _ { 1 } } ( \mathrm { s k r } _ { i 1 } ) , f _ { p _ { 1 } } ( \mathrm { s k r } _ { j 1 } ) ) = 0 .$

(b) $s \mathrm { k r } _ { j 1 }$ is unexpected skew\_diff $\begin{array} { r } { { \bf \nabla } ^ { \prime } f _ { p _ { 1 } } ( \mathrm { s k r } _ { i 1 } ) , f _ { p _ { 1 } } ( \mathrm { s k r } _ { j 1 } ) ) = 1 . } \end{array}$

(c) $\mathsf { s k r } _ { i 1 }$ is NA if $l _ { \mathrm { n a v i g } } ~ ( \mathrm { s k r } _ { i 1 } ) { = } 1$ or $\mathsf { s k r } _ { i 1 }$ is a root node in its navigation path.

Example 2. The following set of navigation rules represents the same fact at different lattice nodes.

skr : “year=1996→pro<sup>fi</sup>t=sk-high”

skr<sub>2</sub>: $\mathrm { ^ { 4 9 } y e a r = 1 9 9 6 , \ m o n t h = } \mathrm { { J a n } \mathrm { { \to } p r o f i t = s k \mathrm { { - } h i g h ^ { \prime } } } }$

skr<sub>3</sub>: $^ { 4 \cdot } \mathrm { y e a r } = 1 9 9 6 , \mathrm { m o n t h } = \mathrm { M a y } \longrightarrow \mathrm { p r o f i t } = \mathrm { s k } \mathrm { - l o w } ^ { \mathrm { * } }$

skr<sub>4</sub>: ${ } ^ { \ast } \mathrm { y e a r } = 1 9 9 6 , \ \mathrm { p r o d u c t \ c a t e g o r y } = \mathrm { D r i n k s }  \mathrm { p r o f i t } = \mathrm { s k } \mathrm { - h i g h } ^ { \mathrm { \prime } }$

Here the parent skr shows a high pro<sup>fi</sup>t for year 1996. The children navigation rules representing ‘Jan 1996’ and ‘1996, drinks’ contribute to high pro<sup>fi</sup>ts in 1996, and are identi<sup>fi</sup>ed as expected rules. However, the pro<sup>fi</sup>t was low for the same year in the month of May (see rule skr ). This is a surprise, which the user would not have expected by just looking at the parent, thus it is an unexpected rule.

## 4.1.3. Case (c) different lattice nodes, different facts

The navigation rules $\mathsf { s k r } _ { i 1 }$ and skr represent different lattice nodes such that one rule's antecedent is a subset of another and they contain different facts in the consequent, i.e. ante $( s \mathbf { k } \mathbf { r } _ { i 1 } ) { \top } \mathbf { a n t e } ( s \mathbf { k } \mathbf { r } _ { j 2 } )$ and $f _ { p _ { 1 } } ( \mathrm { s k r } _ { i 1 } ) { \neq } f _ { p _ { 2 } } ( \mathrm { s k r } _ { j 2 } )$

Based on the skewness difference of navigation rules, we measure the expectedness as follows.

(a) $\mathsf { s k r } _ { i 1 }$ and $\mathsf { s k r } _ { j 2 }$ are expected if skew $\scriptstyle { \mathrm { d i f f } } ( f _ { p _ { 1 } } ( \operatorname { s k r } _ { i 1 } ) , f _ { p _ { 2 } } ( \operatorname { s k r } _ { j 2 } ) ) = 0$

(b) skr<sub>i1</sub> and skr<sub>j2</sub> are unexpected if skew $\begin{array} { r } { \mathrm { ~ d i f f } ( f _ { p _ { 1 } } ( \mathrm { s k r } _ { i 1 } ) , f _ { p _ { 2 } } ( \mathrm { s k r } _ { j 2 } ) ) = 1 } \end{array}$ (c) $\mathsf { s k r } _ { i 1 }$ and $\mathsf { s k r } _ { j 2 }$ are NA if $f _ { p _ { 1 } }$ and $f _ { p _ { 2 } }$ do not de<sup>fi</sup>ne any business rule with each other.

Example 3. Assume the following set of navigation rules.

skr<sub>1</sub>: $\mathrm { ^ { 4 } y e a r = 1 9 9 6 \to p r o f i t = s k \mathrm { - } h i g h ^ { \prime \prime } }$

$$
\mathrm{skr} _ {2}: \text {   "year = 1996,   month = Jan\to cost = sk - high"}
$$

skr : “year=1996, month=May→cost=sk-low”

$$
\mathrm{skr} _ {4}: \text {   "year = 1996,   month = Dec\rightarrowinventory = sk - low"}
$$

In this example the navigation rules represent different lattice nodes. Drilling down on $\mathsf { s k r } _ { 1 }$ reveals $\mathsf { s k r } _ { 2 }$ and $\mathsf { s k r } _ { 3 }$ while following another navigation path reveals skr . Based on the business rule, skr is expected when compared with skr . However, $\mathsf { s k r } _ { 2 }$ is unexpected compared to skr . The navigation rule skr is NA when compared to skr .

4.1.3.1. Using the expectedness of navigation rules in path selection. The expectedness of navigation rules reveals useful information for selecting navigation paths. For instance, the paths can be ranked by the number of unexpected navigation rules. Users can simply drill down on paths that contain a large number of unexpected navigation rules, and examine the corresponding datasets that contain many highs and lows in the transaction set. Fig. 2 illustrates an example in path selection using the unexpectedness measure (a path is constructed by a set of sk-navigation rules). Starting with navigation rules 1 (year = 1991→ pro<sup>fi</sup>t = skhigh) and 2 (year= 1993 →pro<sup>fi</sup>t = sk-low), the <sup>fi</sup>rst level navigation paths are the following: 1→4, 1→5, 1→6, 1→7, 2→12, and $2 \to 1 3 .$ From these navigation paths, rules $5 , 6 ,$ and 13 are unexpected since the skewness difference for these nodes compared to their parent nodes is 1. A preference may be given to navigate the path $1 \to 5 \to 9$ $1 \to 6 \to 1 1 2 \to 1 3$ over the other navigation paths.

## 4.2. Axis shift in navigation paths

While expectedness is a useful characteristic of individual sknavigation rules, the interestingness of navigation paths is another valuable property. In practice, a user may seek a short list of paths from a multitude of navigation paths that may lead to potentially interesting surprises. If a measure of interestingness of paths is provided, users can be selective in cube navigation by comparing numerous paths. The following example demonstrates the need for interestingness of paths and reveals that simply applying the expectedness of navigation rules may not be suf<sup>fi</sup>cient to differentiate between navigation paths.

Consider two navigation paths np and np with an equal number of expected, unexpected, and NA navigation rules at the level of signi<sup>fi</sup>cance α. Using the expectedness of navigation rules measure, the user cannot discriminate between these paths since they contain the same number of expected and unexpected surprises. However a closer examination may suggest a difference in extremity of surprises of individual navigation rules in the two paths. For instance, np may contain the navigation rules representing surprises with very high skewness. On the other hand, np may contain navigation rules that have been identi<sup>fi</sup>ed as surprises but are just above the signi<sup>fi</sup>cance level α. While $\mathrm { n p } _ { 1 }$ is a more interesting path than $\scriptstyle \mathrm { n p } _ { 2 } ,$ users may initially navigate np due to the lack of discriminatory power related to the level of signi<sup>fi</sup>cance for the expectedness measure.

To address this problem, we propose an Axis Shift Theory (AST) to measure the interestingness of navigation paths. AST uses shift metrics to discriminate between paths that contain multiple interesting navigation rules. A shift is measured by the movement of the mean reference axis when navigating from a parent to a child node. AST evaluates the shifts made by individual navigation rules to determine the overall interestingness of a navigation path. As mentioned earlier, the navigation rules are discovered in parent–child pairs where both parent and child represent their respective datasets and the characteristics of datasets such as mean $( \mu ) ,$ standard deviation (σ) and variance $( \sigma ^ { 2 } ) .$ . Given tha $\cdot \overline { { f } } _ { p [ \mathrm { p a r e n t } ] } \mathrm { a n d } \overline { { f } } _ { p [ \mathrm { c h i l d } ] }$ are the respective means for parent and child node on a fact $f _ { p } , \mathsf { a }$ shift in the mean reference axis is calculated by the difference $( \overline { { f } } _ { p [ \mathrm { p a r e n t } ] } ^ { \cdot } - \overline { { f } } _ { p [ \mathrm { c h i l d } ] } ) .$ . We call it a shift because the reference axis essentially shifts from $\overline { { f } } _ { p [ \mathrm { p a r e n t } ] } \mathrm { t o } \overline { { f } } _ { p }$ <sub>[child]</sub>. Once moved to $\mathrm { { n o d } _ { \mathrm { c h i l d } } } ,$ the new mean $\overline { { f } } _ { p [ \mathrm { c h i l d } ] }$ is subsequently used as the reference axis for discovering its children nodes.

Assume that a navigation path np contains t sk-navigation rules. Then, $\boldsymbol { \mathrm { n p } } _ { x } = \{ \mathrm { s k r } _ { i } ; 1 \leq i \leq t \}$ . Let $f _ { p }$ be the fact in the consequent for navigation rule skr and $\bar { f } _ { p [ i ] }$ be the mean value for $f _ { p } .$ In order to measure the interestingness of navigation paths, we de<sup>fi</sup>ne three shift metrics as follows.

## 4.2.1. Linear shift (linSh)

We measure the linear shift of a navigation path by taking the cumulative sum of shifts of individual navigation rules as follows.

$$
\operatorname{linSh} \left(\mathrm{np} _ {x}\right) = \sum_ {\mathrm{i} = 1} ^ {\mathrm{t}} \left(\bar {f} _ {p [ i ]} - \bar {f} _ {p [ i - 1 ]}\right), \mathrm{skr} _ {i} \in \mathrm{np} _ {x}.
$$

The linear shift, $\mathrm { l i n S h } ( \boldsymbol { \mathrm { n p } _ { x } } ) ,$ measures the relative shift of the mean reference axis when drilling down from the root node to a leaf node (lowest level navigation rule) in the path. It identi<sup>fi</sup>es the paths that contain a signi<sup>fi</sup>cant positive or negative movement of the mean reference axis during navigation. Based on such individual shifts in a path, the linear shift of a path can be positive, negative, or zero. We consider the three cases individually as follows.

$$
\operatorname{linSh} \left(\mathrm{np} _ {x}\right) > 0\tag{i}
$$

A positive linear shift of a path indicates a signi<sup>fi</sup>cant movement of the root mean reference axis on its right side (positive skewness). It also suggests that the corresponding datasets in the path are likely to be either less negatively or more positively skewed when drilling down to low level sk-navigation rules. An interesting linear shift is observed if a child of a root node is negatively skewed but the linear shift for the path is positive, thereby indicating some unexpected navigation rules with large axis shifts in the navigation path. The path $1 \to 4 \to 8$ in Fig. 2 illustrates a positive linear shift. The path $1  6 $ 11may indicate an interesting linear shift.

$$
\operatorname{linSh} \left(\mathrm{np} _ {x}\right) <   0\tag{ii}
$$

A negative linear shift of a path indicates a signi<sup>fi</sup>cant movement of the root mean reference axis on its left side (negative skewness), which also suggests the likelihood of less positively skewed or more negatively skewed datasets at lower hierarchical levels. An interesting linear shift is observed if a child of a root node is positively skewed but the linear shift for the path is negative, thereby suggesting one or more unexpected navigation rules with large axis shifts in the navigation path. The path $2  1 2  1 4$ in Fig. 2 indicates a negative linear shift.

$$
\operatorname{linSh} \left(\mathrm{np} _ {x}\right) = 0\tag{iii}
$$

If a child of a root node is skewed (positively or negatively) but the total linear shift of the path is zero, then the path contains both positively and negatively skewed datasets which balance out each other and result in a zero axis shift. In this case, it is interesting to examine the square shift or absolute shift (described later) to further examine the navigation path for its interestingness. Based on Fig. 2, it is unclear whether the navigation path $1 \to 5 \to 9$ has a positive or a negative linear shift.

The paths can be ranked according to their degree of interestingness, by arranging them in a descending order of the magnitude of linear shifts, |linSh(np )|. The paths with higher linear shifts (positive or negative) thus appear at the top for the user's selection list.

## 4.2.2. Absolute shift (absSh)

The absolute shift measures the total shift of navigation rules in a navigation path irrespective of the direction of individual axis shifts. We de<sup>fi</sup>ne the absolute shift by taking the cumulative sum of scalar axis shifts as follows.

$$
\operatorname{absSh} \left(\mathrm{np} _ {x}\right) = \sum_ {\mathrm{i} = 1} ^ {\mathrm{t}} \left| \bar {f} _ {p [ i ]} - \bar {f} _ {p [ i - 1 ]} \right|, s k r _ {i} \in n p _ {x}.
$$

The absolute shift is a useful metric to identify the navigation paths that contain larger shifts of mean reference axis regardless of individual negative or positive shifts. It preserves the magnitude of total shift by avoiding nulli<sup>fi</sup>cation of positive and negative axis shifts. For example, a path $\Pi \mathbb { P } _ { x }$ having two axis shifts of +s and −s results in zero linear shift, however it has an absolute shift of 2s. A nonzero absolute shift implies a de<sup>fi</sup>nite axis shift for the path. The larger the absolute shift, the greater the axis shifts of navigation rules are expected to be. In conjunction with linear shifts, users can select paths by their absolute shifts. While the linear shift for path $\mathrm { n p } _ { 2 }$ is approximately zero, the absolute shift has a larger value. This suggests that the path $\mathrm { n p } _ { 2 }$ is the result of signi<sup>fi</sup>cant shifts on both the right and the left side of the root mean reference axis, rather than an overall signi<sup>fi</sup>cant yet static shift in one direction.

## 4.2.3. Root square shift (rsSh)

The root square shift measures the interestingness of a path to distinctively account for the in<sup>fl</sup>uence of individual high axis shifts. For instance, individual axis shifts, when combined together, may lead to a high absolute shift even if the individual shifts are not high enough. On the other hand, even a single high value shift can dictate the total shift of a path and is interesting to examine. The root square shift identi<sup>fi</sup>es these highs and lows in axis shifts to assist in comparing the navigation paths. We de<sup>fi</sup>ne the root square shift as follows.

$$
\operatorname{rsSh} \left(\mathrm{np} _ {x}\right) = \sqrt {\sum_ {i = 1} ^ {t} \left(\bar {f} _ {p [ i ]} - \bar {f} _ {[ i - 1 ]}\right) ^ {2}}, \operatorname{skr} _ {i} \in \mathrm{np} _ {x}.
$$

## 4.2.4. Using the three shift metrics

The three shift metrics complement each other. The linear shift can be used to examine the paths with a signi<sup>fi</sup>cantly high positive or negative movement of the root mean reference axis. The absolute shift can be used to identify paths with high traversals of the root mean reference axis. The root square shift can be used to reveal paths that contain an unexpectedly high axis shift made by at least one navigation rule. An example which describes the different shifts is provided next.

Example 4. Assume two navigation paths $\scriptstyle \mathrm { { n p } } _ { 1 }$ and $\scriptstyle \mathrm { n p } _ { 2 } .$ The individual node shifts and the three shift metrics for both paths are shown in Table 1. In this case, the root square shift clearly distinguishes between the interestingness of $\mathrm { n p } _ { 1 }$ and $\mathrm { n p } _ { 2 }$ , which would not have been identi<sup>fi</sup>ed using linear and/or absolute shifts.

## 4.3. Generalization of sk-navigation rules

The axis shift theory determines which navigation paths are interesting as established by the shift metrics. As the size of database increases, the number of sk-navigation rules (and thus the paths) can also grow signi<sup>fi</sup>cantly thus overwhelming the users who typically need to retrieve only a short list of navigation rules or paths for analysis, and also expect proper system guidance with minimal intervention. This can be achieved if the system provides the interestingness information at the earliest possible stages of navigation. It also helps users to have apriori knowledge about the types of surprises hidden in subsequent lower level lattice nodes. For instance, if there are four product categories, “Food”, “Drinks”, “Supplies”, and “Gifts” and all of them provide sets of navigation paths to reach the surprises, a question arises as to which of these dimensional attributes are more interesting than others. While “Food” may provide more sk-navigation rules than the others, “Gifts” may lead to more unique surprises. Therefore, a measure of interestingness of attributes can effectively help users navigate only through the paths containing interesting attributes. To determine the interestingness of attributes, we introduce a simple and effective method of generalization of sk-navigation rules, which determines the attributes from dimensional hierarchies that substantially contribute to the discovery of surprises. For example, when a user is given the information that a large number of surprises exists when “Quar-$\mathrm { t e r } = 1 9 9 7 – 0 3 "$ , then it is bene<sup>fi</sup>cial to navigate along the paths that contain 1997-Q3 as the navigation rules' antecedent.

Comparison of shift metrics for two navigation paths

<table><tr><td rowspan="2">Path</td><td colspan="3">Node shifts</td><td rowspan="2">linear shift</td><td rowspan="2">absolute shift</td><td rowspan="2">root square shift</td></tr><tr><td>node_shift1</td><td>node_shift2</td><td>node_shift3</td></tr><tr><td> $np_1$ </td><td>30</td><td>35</td><td>40</td><td>105</td><td>105</td><td>61.03</td></tr><tr><td> $np_2$ </td><td>3</td><td>2</td><td>100</td><td>105</td><td>105</td><td>100.06</td></tr></table>

We examine the navigation rules' antecedents to determine the relative in<sup>fl</sup>uence or signi<sup>fi</sup>cance of attributes from different dimensions and also detect the unique navigation paths that the attributes belong to. To determine the attribute in<sup>fl</sup>uence (attrInf) of an attribute $\nu _ { i j k }$ of dimension $d _ { i }$ at level $l _ { i j } ,$ we perform a two-step generalization of navigation rules on the attribute as follows:

Step 1) Identify the navigation ruleset skr $( \boldsymbol { v } _ { i j k } )$ , at a skewness signi<sup>fi</sup>cance level of $\alpha _ { \ast }$ in which every navigation rule must either contain the attribute $\nu _ { i j k }$ or an attribute $\nu _ { i ^ { \prime } j ^ { \prime } k ^ { \prime } }$ in the antecedent such that $\boldsymbol { v } _ { i ^ { \prime } j ^ { \prime } k ^ { \prime } }$ is a lower level attribute $( i { = } i ^ { \prime } , j { < } j ^ { \prime } )$ from dimensional hierarchy of dimension $d _ { i } ,$ and $\nu _ { i j k }$ is an ancestor of $\begin{array} { r } { v _ { i ^ { \prime } j ^ { \prime } k ^ { \prime } } . } \end{array}$

Step 2) Determine the attribute in<sup>fl</sup>uence for $\nu _ { i j k }$ as follows. attrInf $\begin{array} { r } { { \bf \Pi } ^ { { \bf { \dot { \rho } } } } ( \nu _ { i j k } ) = \frac { | { \bf { n } } { \bf { p } } _ { x } ( \nu _ { i j k } ) | } { \sum _ { { \bf { \dot { \eta } } } : i , j , k } | { \bf { n } } { \bf { p } } _ { x } ( \nu _ { i j k } ) | } . } \end{array}$

where $\boldsymbol { \mathrm { n p } } _ { x } ( \nu _ { i j k } )$ is identi<sup>fi</sup>ed by a navigation from the navigation rule $\ " d i : l _ { i j } = \nu _ { i j k } \ "$ to a leaf rule skr such that ${ \sf s k r } _ { j } { \sf { e s k r } } ( \nu _ { i j k } )$ and $| \boldsymbol { \mathrm { n p } } _ { x } ( \nu _ { i j k } ) |$ represents the total number of paths belonging to attribute $\nu _ { i j k } .$ The value of attrInf $\dot { \boldsymbol { v } } _ { i j k } \big )$ ranges from 0 to 1. If an attribute does not lead to any surprises, its attribute in<sup>fl</sup>uence equals zero, suggesting that the attribute is not an interesting one. On the contrary, an attribute in<sup>fl</sup>uence of 1 identi<sup>fi</sup>es a highly in<sup>fl</sup>uential attribute.

To measure attribute in<sup>fl</sup>uence we choose navigation paths as opposed to the number of leaf nodes (lowest level surprises) to avoid the de<sup>fi</sup>ciencies associated by the latter measure. A path essentially considers both the leaf nodes and their accessibility from the attribute. Two or more attributes can lead to an equal number of leaf nodes but exhibit different number of paths to reach them. ${ \mathrm { A l s o } } ,$ an attribute can link to multiple paths leading to the same leaf node since a leaf node will connect to at least one navigation path. However, the reverse is not true $\mathrm { i . e . , }$ , two leaf nodes cannot be reached through the same navigation path. If we consider the leaf nodes as the basis of a comparison, two or more dimensional attributes with equal number of leaf nodes will not be distinguishable using attribute in<sup>fl</sup>uence despite the fact that one attribute guides the users through higher number of paths to reach the surprises. We illustrate such a scenario in Fig. 2: using this navigation ruleset, we determine the unique navigation paths to measure the attribute in<sup>fl</sup>uence for year 1991 and 1993. For this navigation ruleset, rules 8 and 10 on one hand, and rules 9 and 11 on the other, are identical even though they were generated by different traversals. Table 2 presents the attributes, their attribute in<sup>fl</sup>uence (given that the total number of paths by all dimensional attributes is 15), and their leaf node counts.

Table 2  
Attribute in<sup>fl</sup>uence for 1991 and 1993

<table><tr><td>Attribute</td><td>Paths(using rule_id)</td><td>attrInf</td><td># leaf nodes identified</td></tr><tr><td rowspan="4">1991</td><td>1→4→8</td><td rowspan="4">0.267</td><td rowspan="4">2(“quarter=1991-Q1, state=VA”, “quarter=1991-Q3, product category=Food”)</td></tr><tr><td>1→5→9</td></tr><tr><td>1→6→11</td></tr><tr><td>1→7→10</td></tr><tr><td rowspan="2">1993</td><td>2→12→14</td><td rowspan="2">0.133</td><td rowspan="2">2(“quarter=1993-Q2, product category=Drinks”, “quarter=1993-Q4, state=TX”)</td></tr><tr><td>2→13→15</td></tr></table>

While both 1991 and 1993 lead to equal number of leaf nodes,1991 is a more in<sup>fl</sup>uential attribute than 1993 since it provides the users with a higher number of unique paths to reach the surprises as determined by attrInf(1991)NattrInf(1993).

## 5. Interestingness measures on a real world dataset

In 2003, motor vehicle crashes ranked third in terms of the number of years of life lost, behind cancer and heart diseases [28] where the number of years of life lost is estimated as the additional number of years an individual is expected to live had he/she not died in the crash. Using a combination of OLAP, GIS, and statistical tools, managers of the road infrastructure are able to determine problem roads and intersections and take corrective actions. Enforcement of<sup>fi</sup>cers can implement different tactics based on external factors e.g., time and day of week, weather conditions, driving under in<sup>fl</sup>uence, etc. A prototype system named MSAC was described in [1], which described a crash reduction system which provides OLAP capabilities to all stakeholders through a uni<sup>fi</sup>ed architecture to facilitate collaborative decision-making. MSAC users manually navigate paths of interest to them. Based on our experience with the system implementation and with discussions with various stakeholders, we identi<sup>fi</sup>ed that guided knowledge discovery would be extremely desirable for improving the functionality of the prototype.

Based on manual cube navigation using MSAC, the following prior knowledge was known to the enforcement of<sup>fi</sup>cers: the vehicle crash costs are the highest on Friday nights after 8:00 pm, and in districts with a large number of highways. In order to test the identi<sup>fi</sup>cation of navigation paths with high degree of interestingness, we obtained the dataset containing 534,941 commercial vehicle crash records from the MSAC researchers that ranged from 1993 to 2001 in the state of Maryland. Each individual crash record details the crash location, day and time, severity of crash, and the crash cost. We examined the interestingness of the skewed patterns for this dataset for the three measures: expectedness of the navigation rules, axis shift in paths, and attribute in<sup>fl</sup>uence.

On the expectedness measure, 372 expected and 52 unexpected sk-navigation rules were discovered within a total of 2.06 min. Using the axis shift skewed interestingness measure, the most interesting path identi<sup>fi</sup>ed by linear shift, absolute shift, and root square shift all led to the following sk-navigation rule “District=3-Greenbelt, County=Prince George, Day\_Of\_Week=Tuesday, and Time\_Interval=4 pm– 8 pm” with high positive shifts in the crash costs at each navigation level. This fact is interesting since it does not conform to the apriori knowledge that most crashes take place on Friday after 8:00 pm. Without this information, users would have spent considerable amount of time navigating the paths that have Friday as a node. The second most interesting measures for navigation paths were different at the second navigation level for linear shift, absolute shift, and root square shift; however, in all three of these shifts, “District = 3- Greenbelt” was identi<sup>fi</sup>ed as the root navigation node.

Table 3  
Seven best attribute influence for crash dataset

<table><tr><td>Dimensional attribute</td><td>Attribute influence</td></tr><tr><td>District = ‘Frederick’</td><td>0.390244</td></tr><tr><td>District = ‘Annapolis’</td><td>0.317073</td></tr><tr><td>District = ‘Greenbelt’</td><td>0.195122</td></tr><tr><td>Day of week = ‘Tuesday’</td><td>0.195122</td></tr><tr><td>County = ‘Anne Arundel’</td><td>0.170732</td></tr><tr><td>County = ‘Frederick’</td><td>0.170732</td></tr><tr><td>Day of week = ‘Saturday’</td><td>0.170732</td></tr><tr><td>Day of week = ‘Friday’</td><td>0.170732</td></tr><tr><td>Day of week = ‘Sunday’</td><td>0.146341</td></tr></table>

Table 3 shows the attribute in<sup>fl</sup>uence of the top seven attributes. Interestingly “District= 7-Frederick” was identi<sup>fi</sup>ed as the attribute with the largest in<sup>fl</sup>uence on the interesting navigation paths. While, apriori, the user might suspect that Frederick district would be interesting, since two Interstate Highways pass through the district, the attribute in<sup>fl</sup>uence clearly identi<sup>fi</sup>es this as an interesting starting node. Thus, there are ample opportunities for enforcement of<sup>fi</sup>cials to navigate starting from the Frederick node in order to gain more understanding on crashes.

## 6. Experimental results

In this section, we present a set of experiments to evaluate the measures of interestingness and their scalability. Speci<sup>fi</sup>cally, we demonstrate the interestingness from: (a) expectedness of rules, (b) navigation paths using axis shifts, (c) generalization of attributes, along with (d) the execution time, and (e) the space overhead. All experiments were performed on a 1.7 GHz Pentium IV machine with 512 MB RAM running Windows XP. The algorithms were implemented in PL/SQL on an Oracle 10g database.

## 6.1. Experimental setup

We adapted the Grocery database [14] to produce <sup>fi</sup>ve test datasets as shown in Table 4. The number of navigation nodes is obtained by adding all lattice nodes in all possible cuboids. Each of the datasets contains three dimensions, Product, Time, and Store, and two facts, Pro<sup>fi</sup>t and Cost. The dimensional hierarchies are Product {Category, Subcategory, Brand}, Time {Year, Quarter, Month}, and Store {Region, State. City}. The number of attributes at the lowest level varied from 16 to 64 for Product, 20 to 192 for Time, and 14 to 31 for Store dimension. We generated surprises which represent transactions containing 15– 20% high or low pro<sup>fi</sup>t values compared to the rest of the transaction set. The numbers of transactions with surprises varied from 1 to 25 for each of the datasets. The surprises were also generated in a manner such as to conceal their presence at the higher levels of aggregations (for example, the aggregate “Product category=Drinks” would not show the surprises in transactions “Product Brand= Pepsi” and “Product Brand=Ahold 2% Milk”).

Due to the nature of navigating the lattice nodes, a surprise at the lowest level affects its higher level lattice nodes, such as a surprise at a node “city=Fairfax” will in<sup>fl</sup>uence two additional nodes, “state=VA” and “region=Eastern”. We measure this phenomenon by de<sup>fi</sup>ning an in<sup>fl</sup>uence rate, which is calculated as the number of nodes affected divided by the total number of nodes. Fig. 4 shows the number of nodes in the grocery cube lattice that were affected by the lowest level surprises. For instance in dataset DS-5, the existence of only one lowest level surprise (affecting a single transaction) “Product subcategory=Orange Juice, month=1991-Q1\_Jan, city=Baltimore” affected 62 nodes from a total 1,035,893 nodes in the lattice giving an in<sup>fl</sup>uence rate of 0.005%. As expected, increasing the number of surprises to 5 in the same dataset resulted in a higher in<sup>fl</sup>uence rate of 0.020% by affecting a total of 215 nodes. At the maximum, when 25 lowest level surprises existed in DS-5, the in<sup>fl</sup>uence rate was 0.071% affecting 738 nodes.

Table 4  
Summary of the <sup>fi</sup>ve experimental datasets

<table><tr><td>Dataset</td><td># records</td><td># nodes of navigation</td></tr><tr><td>DS-1</td><td>4480</td><td>5893</td></tr><tr><td>DS-2</td><td>32,240</td><td>37,119</td></tr><tr><td>DS-3</td><td>97,384</td><td>107,095</td></tr><tr><td>DS-4</td><td>20,736</td><td>131,759</td></tr><tr><td>DS-5</td><td>190,464</td><td>1,035,893</td></tr></table>

![](/api/attachments/A2HHEW2G/fulltext/images/3063f83f3daebfeb921bbab7057235a90ddeac20a4bd57113bb7e9135a5b9025.jpg)  
Fig. 4. Surprise vs. total affected nodes

Apart from varying the number of surprises, we also discovered the navigation rules at various levels of signi<sup>fi</sup>cance (α) ranging from 0.005 to 0.1.

## 6.2. Interestingness from expectedness of navigation rules

Fig. 5 examines the effect of α on the expectedness of discovered navigation rules for the dataset DS-5 when the number of surprises was set to 25. The plot “pos\_exp” shows the percentage of expected navigation rules with positive skewness; “neg\_unexp” shows the percentage of unexpected navigation rules with negative skewness, and so on. While the total number of expected navigation rules is always greater than the total number of unexpected navigation rules, we observe a higher percentage of unexpected navigation rules discovered with an increase in the value of α. When α was increased to 0.05, 8.17% unexpected navigation rules were discovered. It further increased to 31.62% at α=0.1. This happened as a result of a decrease in critical skewness with higher α's. At lower α's, only the very highly skewed patterns, which were more prominent and mostly expected, were detected. The discovery of 31.62% unexpected navigation rules also suggests that a large number of unexpected skewed patterns were concealed in low level lattice nodes and were not noticeable at higher levels of aggregation at smaller α's. Finally, we notice that there is a relatively larger drop in the percentage of navigation rules for neg\_exp (from 46.67% to 25.15%) curve compared to pos\_exp curve (52.08% to 42.55%). It is attributed to the discovery of large number of unexpected navigation rules at higher α's. It also suggests that there are more positively skewed patterns than negatively skewed patterns in the dataset.

![](/api/attachments/A2HHEW2G/fulltext/images/9dce5920071a653b21c23a4704501700cee86334f04775fec11a758925a5e7f2.jpg)  
Fig. 5. Interestingness of rules for DS-5 at surprises = 25.

![](/api/attachments/A2HHEW2G/fulltext/images/0d9c36574306d3772b7de2ff0ea74f6c9454578de2bda7b9391cf984e8a79f42.jpg)  
Fig. 6. Discovered unexpectedness rules for DS-5

Fig. 6 further illustrates the discovery of unexpected skewed patterns in DS-5 at various values of α and number of surprises. In each of the instances, the percentage of unexpected navigation rules increased with an increase in α. For example, when α increased from 0.025 to 0.05, the number of unexpected navigation rules increased from 5 (1.93% of total) to 41(8.17% of total) for 25 surprises. At the maximum, 45.63% unexpected skewed patterns were detected for 2 surprises and α=0.1.

Fig. 7 compares the percentages of interesting navigation rules for the <sup>fi</sup>ve datasets when the number of surprises and α were set to 25 and 0.05 respectively. We observe that DS-3 contained a higher percentage of unexpected navigation rules (24.19%) compared to other datasets. Also, this 24.19% was almost equally divided between positively skewed unexpected (12.39%) and negatively skewed unexpected (11.80%), highlighting an important issue with data aggregation: it is dif<sup>fi</sup>cult to detect skewed patterns by looking at aggregated datasets. However, sk-navigation rules detect these skewed patterns as explained in DS-3.

## 6.3. Interestingness from navigation paths using Axis Shift

Fig. 8(a) illustrates how the Axis Shift Theory is used in DS-5 to reach surprises through interesting navigation paths when the number of surprises and α were set to 25 and 0.05 respectively. We <sup>fi</sup>rst calculated the linear shift (linSh), absolute shift (absSh), and root square shift (rsSh) for discovered navigation paths. Then, the paths were ranked from highest to lowest interestingness by arranging them in descending order of shifts, for each of the three shift metrics. We then examined the percentage of surprises detected by various sizes of top interesting paths.

![](/api/attachments/A2HHEW2G/fulltext/images/4f00d159cd05d4850a471350649afcc31d42f935bbab1022ef46e1e8430efeee.jpg)  
Fig. 7. Interestingness of rules for <sup>fi</sup>ve datasets with α=0.05

(a)  
![](/api/attachments/A2HHEW2G/fulltext/images/7f89c0012290f882ddbd371ed0e39c5cf2e4d22c6e539ee2da99e7d5d646989a.jpg)

(b)  
![](/api/attachments/A2HHEW2G/fulltext/images/d45da49ba8d33b2bbdd3804dd4ccc4ce333fe4b5206a9c39bbc82a015675fc6c.jpg)  
Fig. 8. Interestingness of paths for (a) DS-5, and (b) Five datasets at α=0.05.

Fig. 8(a) shows that every shift metric required only a small set of interesting paths to reach all surprises discovered by sk-navigation rules (88% of total implanted surprises). For instance, only the top 15% (most interesting) paths were able to reach all discovered surprises using linSh. Also, both absSh and rsSh reached the surprises by using only 10% of the paths. We observe that rsSh is the steepest of the three shifts, thereby indicating that it performed better than linSh and absSh to reach the discovered surprises. A horizontal straight line after 15% paths for linSh (and 10% for absSh and rsSh) suggests that the same sets of surprises were reached afterwards using the less interesting navigation paths.

Fig. 8(b) further illustrates the use of rsSh to determine interesting paths for <sup>fi</sup>ve datasets when the number of surprises and α were set to 25 and 0.05 respectively. We observe that only the top 15% (32 out of a total of 218 paths) and the top 10% (23 out of a total of 235 paths) of most interesting paths were able to reach the surprises in DS-4 and DS-5 respectively. This clearly shows that the surprises were reachable by a signi<sup>fi</sup>cantly smaller set of pruned paths. Also, the top 35% and 30% paths were able to reach all the surprises in DS-2 and DS-3. A highest 45% of the paths were needed to reach every surprise in DS-1 but in reality the top 21% paths had detected 96% of the surprises. Only one less-skewed surprise “product subcategory =Juice, quarter=1993-Q2, city=San Diego” was reached by the 64th most interesting path from a total 142 paths, thus requiring 45% paths to reach every surprise in the dataset.

## 6.4. Interestingness from generalization of sk-navigation rules

Fig. 9 shows the top three most interesting attributes for the <sup>fi</sup>ve datasets when the number of surprises and α were set at 25 and 0.05 respectively. These attributes were identi<sup>fi</sup>ed based on the frequency of their presence in navigation paths leading to surprises as discussed in the section on generalization of attributes. As shown in the <sup>fi</sup>gure, ‘MD’, ‘Supplies’, and ‘PA’ were the top three most interesting attributes in DS-1, DS-2, and DS-3, though they showed different attribute in<sup>fl</sup>uences for different datasets. For instance, ‘MD’ in DS-1 identi<sup>fi</sup>ed 53.52% of the possible navigation paths leading to surprises, whereas the same attribute identi<sup>fi</sup>ed 49.33% and 45.91% of the paths in DS-2 and DS-3 respectively. The ‘Eastern’ region was identi<sup>fi</sup>ed as the most interesting attribute in DS-5 with a 50.21% attribute in<sup>fl</sup>uence. It is important to note that this interestingness measure identi<sup>fi</sup>ed one attribute in each of the datasets that led to the discovery of at least 45% of the surprises. The attributes ranked byattribute in<sup>fl</sup>uence provide guidance to users in cube navigation. For example, when navigating through DS-1, users are most likely to reach the surprises if they drill down on ‘MD’ followed by ‘Supplies’, and ‘PA’.

## 6.5. Execution time and space overhead

Fig. 10(a) shows the total time to identify the interesting navigation paths in DS-5 as a function of α. We <sup>fi</sup>rst deduced the navigation paths from sk-navigation rules and then applied the axis shift theory to measure the interestingness of paths in terms of linSh, absSh, and rsSh. The graph suggests an increase in execution time for higher α's. This is expected because at higher α's, a larger number of paths are discovered. However, even for the largest dataset DS-5, the interesting paths were discovered with a very low processing time. For instance, it took only 2083 ms to discover 147 interesting paths with 10 surprises and α set at 0.05. The execution time reached a maximum 2613 ms when 495 interesting paths were identi<sup>fi</sup>ed in DS-5 at a peak α value of 0.1 and 25 surprises. Fig.10(b) shows the execution time for different datasets at α=0.05. The interesting navigationpaths were discovered within a low processing time for each of the <sup>fi</sup>ve datasets: it took only 1810 and 1882 ms to discover interesting paths in DS-3 and DS-4 respectively for 20 surprises. It took the maximum 2464 ms to discover 235 interesting paths in DS-5 for 25 surprises.

The space overhead to store the interesting navigation rules and navigation paths for the datasets at α=0.05 is very low. It ranges from 0.22% (in DS-5) to 2.05% (in DS-4). This small overhead is due to the fact that the number of navigation rules does not increase in direct proportion to the size of the datasets.

## 7. Comparison with previous work

We used the motor vehicle crash data described in the previous section for comparing our method with previous work. Even though the literature provides many interestingness measures such as support, con<sup>fi</sup>dence, lift, conviction, surprisingness and novelty, none of these measures have been developed for navigating multi-dimensional data cubes. To the best of our knowledge, the only method other than what we describe in this paper was discovery driven cube exploration, developed by Sarawagi et al. [22–25]. The crash dataset has nine dimensions and several facts, of which, we will consider only one measure, namely, crash\_cost. The dimensions and the number of distinct values for each level of the dimensional hierarchies are shown in the Table 5. The lowest level is shown as “NONE” as there is no possible navigation from there. Some of the dimensions have been <sup>fl</sup>attened out for simpli<sup>fi</sup>cation but this does not impact the generality or the comparison of the two methods. In the method described in [22–25], a user has to view 10,439 screens of all possible exception values (InExp, SelfExp, and PathExp) which is the total number of possible cuboids [11] since the navigation is based on the values of the dimensions at each level. In addition, for each screen, the user will have to visually inspect tables with number of rows ranging from 2 to 9497. Both of the above are impractical for user-driven navigation.

![](/api/attachments/A2HHEW2G/fulltext/images/df07c9af9fa1ad78b426430d2ec90cc876f71dcf9ebd30b9a830cc90515fed42.jpg)  
Fig. 9. Attribute in<sup>fl</sup>uence for datasets at α=0.05

(a)  
![](/api/attachments/A2HHEW2G/fulltext/images/b1dd4749c67dfe8e24515cf4c8d1cc7f380472d00bdf267fef212ae136e92f56.jpg)  
(b)

![](/api/attachments/A2HHEW2G/fulltext/images/a6ba92032ac8ebabd5c4f7ede417731b9f95b24e14becb929df15a9cf736f5ef.jpg)  
Fig. 10. Execution Time for (a) DS-5 as a function of α, and (b) <sup>fi</sup>ve datasets at α=0.05.

In contrast, our method lists the rules instead of the actual values of the dimensions. So a user can select a rule to drill-down the same dimension or drill across another dimensions which limits the number of cuboids visited. In our proposed method, the maximum number of dimensional values is 88, calculated by counting the total number of possible navigations. Each screen will have a rank-ordered set of 10 rules. It means that in the worst case, the user can view 880 possible screens. Both of the above are worst case scenarios for userdriver cube navigation as summarized in the Fig. 11 below.

Table 5  
Description of dimensions

<table><tr><td>Dimension</td><td>Level 1</td><td>Level 2</td><td>Level 3</td><td>Total</td></tr><tr><td>Time</td><td>9</td><td>12</td><td>7</td><td>756</td></tr><tr><td>Location</td><td>25</td><td>1</td><td>None</td><td>25</td></tr><tr><td>Collision</td><td>2</td><td>25</td><td>None</td><td>50</td></tr><tr><td>Vehicle</td><td>24</td><td>None</td><td>None</td><td>24</td></tr><tr><td>Route</td><td>9497</td><td>None</td><td>None</td><td>9497</td></tr><tr><td>Environment</td><td>23</td><td>None</td><td>None</td><td>23</td></tr><tr><td>Severity</td><td>2</td><td>None</td><td>None</td><td>2</td></tr><tr><td>Junction</td><td>9</td><td>None</td><td>None</td><td>9</td></tr><tr><td>Contribution</td><td>53</td><td>None</td><td>None</td><td>53</td></tr><tr><td>Total</td><td></td><td></td><td></td><td>10,439</td></tr></table>

## 8. Conclusions and future work

In this paper, we presented the measures of interestingness of skewness based navigation rules which are used to discover interesting surprises hidden in multidimensional cubes. We investigated interestingness in three different ways examining: unexpectedness of navigation rules; an axis shift in the navigation path, and generalization of navigation rules. First, unexpected navigation rules are discovered by examining their skewness' differences from the navigation rules in the neighborhood. Second, the theory on axis shifts identi<sup>fi</sup>es the interesting navigation paths in terms of linear shift, absolute shift, and root square shift, which are tested on a real-world dataset. Finally, the generalization of navigation rules identi<sup>fi</sup>es interesting dimensional attributes which lead to large numbers of low level interesting surprises. We also conducted detailed experiments on <sup>fi</sup>ve different sets of grocery data to evaluate these measures of interestingness.

The measures of interestingness suitably <sup>fi</sup>t into business intelligence arena. Executives and analysts can navigate through OLAP cubes using sknavigation rules to gain useful insights into multidimensional datasets. In BI dashboards, the interestingness measures can <sup>fi</sup>ttingly work as a set of cues to provide visibility into datasets and to help organizations reach stated goals by leveraging information and analytics. For instance, executives can begin cube navigation by <sup>fi</sup>rst looking at attribute generalization measure to instantly know about interesting attributes. Then, they can select an interesting attribute and navigate through unexpected sk-navigation rules. They can also <sup>fi</sup>lter on navigation paths based on axis shifts so as to view the paths that interest them.

The measures of interestingness can suitably be applied to business domains where metrics are real-valued to measure for skewnesss and where the rules can be compared relative to each other (such as rules for their unexpectedness or attributes for their attribute in<sup>fl</sup>uence). Metrics such as time (production time, shipment time, product assembly time), cost (production cost, operational cost, cost of inventory), revenue, pro<sup>fi</sup>t, units of product sold, <sup>fi</sup>t our measures of interestingness quite well.

As an example, reducing the “production time” is usually a goal for manufacturing companies. A positively skewed production time (i.e. it is taking longer than average) might suggest to the executives to look for inef<sup>fi</sup>ciency factors by product by region. They can drill down on navigation rules to identify the products in regions that have longer than expected production times. This knowledge can then be used to determine the underlying reasons for the production bottlenecks. On the other hand, a negative skewness on production time metric is a good sign.

![](/api/attachments/A2HHEW2G/fulltext/images/f46b843ad367d6138c1b47d1bdd3c6d7b7d671e74f091ab41aabdc7aa005243d.jpg)  
Fig. 11. Comparison with Sarawagi et al. [24,25]

We are currently extending our work on the concept of cube navigation to allow users to view in a tree structure, all possible navigation paths from a navigation rule and then delve directly into a navigation rule of interest. We are further enhancing our work to allow users to investigate the corresponding transaction set for a navigation rule such that the highly skewed transactions are displayed clearly at the top.

## References

[1] S. Bapna, A. Gangopadhyay, A web-based GIS for analyzing commercial motor vehicle crashes, Information Resources Management Journal 18 (2005) 1–12.

[2] B. Barber, H.J. Hamilton, A comparison of attribute selection strategies for attribute-oriented generalization, presented at International Symposium on Methodologies for Intelligent Systems (ISMIS'97), Charlotte, NC, 1997.

[3] R.B. D'Agostino, M.A. Stephens, Goodness-of-Fit Techniques, Marcel Dekker, Inc., New York, NY, 1986.

[4] G. Dong, J. Li, Interestingness of discovered association rules in terms of neighborhood-based unexpectedness, presented at Second Paci<sup>fi</sup>c-Asia Conference on Research and Development in Knowledge Discovery and Data Mining, 1998.

[5] C.C. Fabris, A.A. Freitas, Discovering surprising instances of Simpson's Paradox in hierarchical multidimensional data, International Journal of Data Warehousing and Mining 2 (2006) 27–49.

[6] M. Garcia, M. Quitales, F. Penalvo, M. Martin, Building knowledge discovery-driven models for decision support in project management, Decision Support Systems 38 (2) (2004) 305–317.

[7] L. Geng, H.J. Hamilton, Finding interesting summaries in Genspace graphs ef<sup>fi</sup>ciently, presented at Canadian Arti<sup>fi</sup>cial Intelligence Conference (AI 2004), London, ON, Canada, 2004.

[8] L. Geng, H.J. Hamilton, Interestingness measures for data mining: a survey, ACM Computing Surveys 38 (2006).

[9] H.J. Hamilton, L. Geng, L. Findlater, D.J. Randall, Ef<sup>fi</sup>cient spatio-temporal data mining with genspace graphs, Journal of Applied Logic 4 (2006) 192–214.

[10] J. Han, Towards on-line analytical mining in large databases, presented at ACM SIGMOD International Conference on Management of Data, 1998.

[11] J. Han, M. Kamber, Data Mining: Concepts and Techniques, 2nd edMorgan Kaufmann, 2006.

[12] R.J. Hilderman, H.J. Hamilton, Knowledge Discovery and Measures of Interest, Kluwer Academic, Boston, MA, 2001.

[13] W.H. Inmon, Building the Data Warehouse, John Wiley & Sons, New York, 1996

[14] R. Kimball, M. Ross, The Data Warehouse Toolkit, Second edWiley Computer Publishing, 2002.

[15] M. Klemettinen, H. Mannila, H. Toivonen, Interactive exploration of interesting <sup>fi</sup>ndings in the telecommunication network alarm sequence analyzer Tasa, Informa tion and Software Technology 41 (1999) 557–567.

[16] W. Klosgen, Subgroup discovery, in: W. Klosgen, J.M. Zytkow (Eds.), Handbook of Data Mining and Knowledge Discovery Oxford University Press New York 2002 pp. 354–361

[17] N. Kumar, A. Gangopadhyay, G. Karabatis, S. Bapna, Z. Chen, Navigation rules for exploring large multidimensional data cubes, International Journal of Data Warehousing & Mining 2 (2006) 27–48.

[18] B. Liu, W. Hsu, Post-analysis of learned rules, presented at Thirteenth National Conference on Arti<sup>fi</sup>cial Intelligence (AAAI-96), Portland, Oregon, USA, 1996.

[19] K. McGarry, A survey of interestingness measures for knowledge discovery, Journal of Knowledge Engineering Review 20 (2005) 39–61.

[20] B. Padmanavan, A. Tuzhilin, Knowledge re<sup>fi</sup>nement based on discovery of unexpected patterns, Decision Support Syetems 33 (3) (July 2002) 309–321.

[21] S. Sahar, Interestingness via what is not interesting, presented at Fifth ACM SIGKDD international conference on Knowledge discovery and data mining, 1999.

[22] S. Sarawagi, Indexing Olap data, presented at IEEE Data Engineering Bulletin, 1997.

[23] S. Sarawagi, Explaining differences in multidimensional aggregates, presented at VLDB Conference. 1999.

[24] S. Sarawagi, User-adaptive exploration of multidimensional data, presented at VLDB.2000.

[25] S. Sarawagi, R. Agrawal, N. Megiddo, Discovery-driven exploration of Olap data cubes, presented at International Conference on Extending Database Technology, 1998.

[26] Y.D. Shen, Z. Zhang, Q. Yang, Objective-Oriented Utility-based Association Rule Mining, ICDM, 2002, pp. 426–433.

[27] A. Silberschatz, A. Tuzhilin, What makes patterns interesting in knowledge discovery systems, IEEE Transactions on Knowledge and Data Engineering 8 (6) (1996) 970–974.

[28] R. Subramanian, Motor Vehicle Traf<sup>fi</sup>c Crashes as a Leading Cause of Death in the United States, National Center for Statistics and Analysis, NHTSA, Washington DC, 2003.

[29] J.S. Vitter, M. Wang, Approximate computation of multidimensional aggregates of sparse data using wavelets, presented at ACM SIGMOD International Conference on Management of Data, Philadelphia, PA, 1999.

[30] K. Wang, Y. Jiang, L.V.S. Lakshmanan, Mining unexpected rules by pushing user dynamics, presented at ACM SIGKDD, 2003.

[31] N. Wu, J. Zhang, Factor analysis based anomaly detection and clustering, Decision Support Systems 42 (1) (2006) 375–389.

[32] H. Zang, B. Padmanavan, A. Tuzhilin, On the discovery of signi<sup>fi</sup>cant statistical quantitative rules, KDD 2004, 2004, pp. 374–383.

[33] N. Zibidi, S. Faiz, M. Limam, On mining summaries by objective measures of interestingness, Machine Learning 62 (3) (2006) 175–198.

![](/api/attachments/A2HHEW2G/fulltext/images/b71f6d80272c2370220118731806ddd87086bac72426a144431b2ce261dc76c8.jpg)  
Navin Kumar has a PhD in Information Systems from University of Maryland, Baltimore County. His main research interests are in data warehousing solutions and data mining.

Aryya Gangopadhyay is a Professor of Information Systems at the University of Maryland Baltimore County (UMBC). His research interests include privacy preserving data mining, OLAP data cube navigation, and core and applied research on data mining.

![](/api/attachments/A2HHEW2G/fulltext/images/b4a2ad794d91e6ce7ee089430c8812442262e761b48ad0ae86690a7ca89468d5.jpg)

![](/api/attachments/A2HHEW2G/fulltext/images/4fa6adf5879f2a215c2420f16317c540cefa18e6284437721280cfc77dfb1d9f.jpg)

Sanjay Bapna is an Associate Professor of Information Science and Systems at Morgan State University. His research has appeared in Decision Sciences, and elsewhere. His research interests include data mining, analytics, and security.

George Karabatis is an Associate Professor of Information Systems at the University of Maryland, Baltimore County (UMBC). His current research interests are semantic information integration and mining, and applications for mobile handheld devices.

![](/api/attachments/A2HHEW2G/fulltext/images/b84bde85875b0f26460f841dfd01135ffa35b7bdc94e4bc84c18d08b98440df1.jpg)

Zhiyuan Chen is an Assistant Professor at information systems department, UMBC. His research interests include privacy preserving data mining, data navigation and visualization, XML, automatic database tuning, and database compression.

![](/api/attachments/A2HHEW2G/fulltext/images/3eaadd2f516704887599d922dc333d2a3846c7d8c0ec527863a7aab703ba5831.jpg)
