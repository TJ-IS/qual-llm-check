---
otero_id: 9422
otero_key: "H6VCXRH3"
title: "A decision support system for product design in concurrent engineering"
authors: "Lida Xu; Zongbin Li; Shancang Li; Fengming Tang"
year: "2007"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2004.11.007"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
Decision Support Systems 42 (2007) 2029– 2042

www.elsevier.com/locate/dss

# A decision support system for product design in concurrent engineering

Lida Xu <sup>a,b,\*</sup>, Zongbin Li <sup>a</sup>, Shancang Li <sup>a</sup>, Fengming Tang

<sup>a</sup> State Key Laboratory of Mechanical Manufacturing Systems Engineering, College of Mechanical Engineering, Xian Jiaotong University, Xian 710049, China

<sup>b</sup> Department of Information Technology and Decision Sciences, Old Dominion University, Norfolk, VA 23529-0218, USA

Available online 24 December 2004

## Abstract

Compared with the traditional sequential design method, concurrent engineering is a systematic approach to integrate concurrent design of products and their related processes. One of the key factors to successfully implement concurrent engineering is information technology. In order to design a product and its manufacturing process simultaneously, information on product features, manufacturing requirements, and customer demands must be processed while the design is concurrently going on. There is an increased understanding of the importance of the correct decisions being made at the conceptual design and development stages that involve many complex evaluation and decision-making tasks. In order to promote the efficiency in concurrent product development, appropriate evaluation and decision tools need to be provided. In this paper, the characteristics of fuzzy, multi-stage evaluation and decision making in concurrent product development process are analyzed and a decision support system for product design in concurrent engineering is presented. An example is given to illustrate the application of the system.

<sup>D</sup> 2004 Elsevier B.V. All rights reserved.

Keywords: Decision support systems; Concurrent engineering; Concurrent product development; Fuzzy sets

## 1. Introduction

The manufacturing environment has dramatically changed in the last few years. Worldwide competition among manufacturers and the development of new manufacturing technologies have contributed to today’s competitive situations in manufacturing industries [13]. Such competition has stimulated rapid changes in manufacturing industries, causing a significant shift in how products are designed, manufactured, and delivered. Customers demand products of higher quality, lower price, and better performance in an ever-shorter delivery time. Competition in the marketplace for new products is forcing changes in the way product designers and manufacturing engineers develop products. In conventional product development, conceptual design, detailed design, process planning, prototype manufacturing, and testing are considered as sequential processes. Compared with the traditional sequential method, concurrent engineering is a systematic approach to integrate the concurrent design of products and their related processes. Concurrent engineering is intended to stimulate product designers/developers to consider all elements of the product life cycle in the early stage of product development.

In order to improve product quality, lower cost, shorten the product development cycle, and fulfill customers’ requirements, concurrent engineering requires product designers to take all the factors involved in the life cycle of a product into consideration. As a result, quite a few related concepts have been proposed such as design for assembly (DFA), design for manufacturability (DFM), design for serviceability (DFS), and design for environment (DFE) [9,11]. Concurrent engineering requires designers to take all stages in the life cycle of a product into account when making decisions. Manufacturing, assembling, maintenance, and environmental protection are typical stages of the life cycle of a product. DFA, DFM, DFS, and DFE reflect different aspects of product design. It is obvious that the overemphasis of one stage over another may not be a good choice; therefore, it is suggested that designers should take all stages such as DFA, DFM, DFS, and DFE as well as related methods into consideration [12,25].

Concurrent product design stages can be classified into stages such as initiation, DFA, DFM, DFS, and DFE. Careful evaluation and appropriate decisions regarding design alternatives must be made at each stage [25]. From a systems point of view, product design is considered as a process characterized by <sup>b</sup>design-evaluation-redesign<sup>Q</sup> [13,14,21]. Such an evaluation process is a complicated one for a number of reasons: (1) it is necessary to take all design objectives into account. However, some objectives conflict with one another such as precision versus manufacturing cost, material performance versus material cost, and so forth; (2) in the design stage, especially the early development stage, it is difficult to quantify and weigh design objectives precisely due to lack of information or vague objectives; (3) designers subjective preference makes the evaluation more complicated. However, proper decisions are needed for product design in concurrent engineering.

To cope with this, utility theory or fuzzy sets theory can be employed to evaluate and select design alternatives. With utility theory, design alternatives can be evaluated if numerical data is available. Since the information available in the early design stage is most likely imprecise and fuzzy, and decision problems in concurrent engineering are generally difficult to define and structure, it is proper to apply the fuzzy sets approach to the process [10]. As mentioned above, all design factors including assembling, manufacturing, and maintenance, which affect the product design in the life cycle of a product, should be taken into account in concurrent design. A concurrent design process can be classified into several stages in which both evaluation and decision are needed. Each stage can be considered as a subsystem for decision making; subsystems together form a multi-stage fuzzy decision system.

Many complex decisions need to be made in the concurrent product development process [27]. As a result, complex concurrent engineering design problems require decision aids such as decision support systems. Given the nature of decision support problems, the research emphasis of decision support systems development has been focused on modeling issues [4]. In this paper, fuzzy sets theory is used to evaluate design alternatives and facilitate decision making. With comprehensive evaluation models based on fuzzy sets theory and dynamic programming, a decision support system is developed in this study to provide support for multi-stage decision making in concurrent engineering design and selecting best design alternatives. The overall objective of this research is to develop a decision support system for helping project managers and design/development engineers in their decision-making activities within a concurrent engineering environment.

## 2. Fuzzy evaluation

Numerous studies characterize concurrent product design processes as a fuzzy process, especially early stages that are characterized by ill-defined and illstructured information [10,18]. One of the primary reasons for this is that information about the process of product development is incomplete at the beginning and develops gradually over time. The product design process is characterized by complex deliberation over a series of interdependent decisions that lead to design solutions [15]. In the product design process, many attributes related to the design, structure, and layout of the product need to be evaluated. In the initial design stage, due to lack of sufficient information, design alternatives are usually evaluated fuzzily such as <sup>b</sup>the design is kind of feasible<sup>Q</sup>, <sup>b</sup>the product sounds reliable<sup>Q</sup>, etc. [27]. Let R stand for the universe for fuzzy linguistic values, attributes are evaluated in terms of <sup>b</sup>good<sup>Q</sup>, <sup>b</sup>somewhat good<sup>Q</sup>, <sup>b</sup>fair<sup>Q</sup>, <sup>b</sup>somewhat bad<sup>Q</sup>, and <sup>b</sup>bad<sup>Q</sup> which form the evaluation universe $U ,$ $U { = } ( ^ { \mathrm { 6 6 } } \mathrm { g o o d } ^ { \mathrm { 9 9 } } , $ <sup>b</sup>somewhat good<sup>Q</sup>, <sup>b</sup>fair<sup>Q</sup>, <sup>b</sup>somewhat bad<sup>Q</sup>, <sup>b</sup>bad<sup>Q</sup>), and are represented with membership functions [3]. Here the concept of fuzzy number is introduced [14],

Definition 1. A fuzzy number $\tilde { \mathrm { R } }$ is a fuzzy set, its membership function satisfies,

$$
\begin{array}{l l} 1 & \mu_ {\tilde {R}} (x) = 0 (r <   c \text {or} r > d) \\ 2 & \mu_ {\tilde {R}} (x) = 1 (a \leq r \leq b) \\ 3 & \mu_ {\tilde {R}} (x) = 1 (c \leq r \leq a) \\ 4 & \mu_ {\tilde {R}} (x) = 1 (b \leq r \leq d) \end{array}
$$

In which, [c,d] is called the subset of fuzzy number ${ \tilde { \operatorname { R } } } ,$ and [a,b] is called the core of fuzzy number $\tilde { \mathrm { R } }$ [14,18,19]. Here five triangle fuzzy numbers $( \tilde { \mathrm { u } } _ { 1 } ,$ $\tilde { \mathbf { u } } _ { 2 } , . . . , \tilde { \mathbf { u } } _ { 5 } )$ are used to represent five fuzzy variables: $\tilde { \mathrm { u } } _ { 1 } -$ bad; $\tilde { \mathbf { u } } _ { 2 } -$ —somewhat bad; $\tilde { \mathrm { u } } _ { 3 } { \mathrm { - } } \mathrm { f a i r } ; \tilde { \mathrm { u } } _ { 4 } -$ —somewhat good; $\tilde { \mathbf { u } } _ { 5 } -$ good. The membership functions are shown as Fig. 1,

$$
\mu_ {\tilde {u} _ {1}} (r) = \left\{ \begin{array}{c c} 0 & r <   0 \text {   or   } r > 1 / 4 \\ 1 - 4 r & 0 \leq r \leq 1 / 4 \end{array} \right.
$$

$$
\mu_ {\tilde {u} _ {2}} (r) = \left\{ \begin{array}{c c} 0 & r <   0 \text {   or   } r > 1 / 2 \\ 2 r + 1 / 2 & 0 \leq r \leq 1 / 4 \\ 2 - 4 r & 1 / 4 \leq r \leq 1 / 2 \end{array} \right.
$$

![](/api/attachments/H6VCXRH3/fulltext/images/54215e98586b1c6e6b3b6dc34a51a7feffd45fa23706a29493311faf5d4d2391.jpg)  
Fig. 1. Membership function for fuzzy numbers.

The membership functions of $\tilde { \mathrm { u } } _ { 3 } , \tilde { \mathrm { u } } _ { 4 } , \tilde { \mathrm { u } } _ { 5 }$ are as follows,

$$
\mu_ {\tilde {u} _ {3}} (r) = \left\{ \begin{array}{c c} 0 & r <   1 / 4 \text {   or   } r > 3 / 4 \\ 4 r - 1 & 1 / 4 \leq r \leq 2 / 4 \\ 3 - 4 r & 2 / 4 \leq r \leq 3 / 4 \end{array} \right.
$$

$$
\mu_ {\tilde {u} _ {4}} (r) = \left\{ \begin{array}{c c} 0 & r <   2 / 4 \text {   or   } r > 1 \\ 4 r - 2 & 2 / 4 \leq r \leq 3 / 4 \\ 4 - 4 r & 3 / 4 \leq r \leq 1 \end{array} \right.
$$

$$
\mu_ {\tilde {u} _ {5}} (r) = \left\{ \begin{array}{c c} 0 & r <   3 / 4 \text {   or   } r > 1 \\ 4 r - 3 & 3 / 4 \leq r \leq 1 \end{array} \right.
$$

The evaluation universe U can be represented as $U { = } \tilde { \mathbf { u } } _ { 1 } , ~ \tilde { \mathbf { u } } _ { 2 } , . . . , ~ \tilde { \mathbf { u } } _ { 5 }$ . The advantages of using triangle fuzzy numbers include simple representation, speedy calculation, and sufficient precision.

## 3. Product design evaluation

## 3.1. Fuzzy line segment

In the above, we have described the evaluation universe and fuzzy numbers in which the evaluation universe is not continuous. As a result, the concept of fuzzy line segment is used to make the evaluation universe continuous for a more accurate evaluation of fuzzy numbers [3].

Definition 2. Assuming $\tilde { \mathrm { v } } _ { 1 } , \tilde { \mathrm { v } } _ { 2 }$ are two fuzzy numbers, then the fuzzy line segment $F ( \tilde { \mathbf { v } } _ { 1 } , \tilde { \mathbf { v } } _ { 2 } )$ between $ { \widetilde { \mathrm { v } } } _ { 1 }$ and $\tilde { \bf v } _ { 2 }$ are consisted of a set of fuzzy numbers as,

$$
\begin{array}{l} F (\tilde {\mathbf {v}} _ {1}, \tilde {\mathbf {v}} _ {2}) = \left\{\tilde {\mathbf {v}} | \mu_ {\tilde {\mathbf {v}}} (z) \right. \\ \quad = \underset {\alpha x _ {1} + (1 - \alpha) x _ {2} = z} {\text { Sup }} \left[ \mu_ {\tilde {\mathbf {v}} _ {1}} (x _ {1}) \wedge \mu_ {\tilde {\mathbf {v}} _ {2}} (x _ {2}) \right], \alpha \in [ 0, 1 ] \Bigg \} \end{array}
$$

It is not difficult to know that, if $\tilde { \mathbf { v } } _ { 1 } , ~ \tilde { \mathbf { v } } _ { 2 }$ are two fuzzy numbers, and $[ c _ { 1 } , d _ { 2 } ] , [ c _ { 2 } , d _ { 2 } ]$ are their subsets, their cores are $[ a _ { 1 } , b _ { 1 } ] , [ a _ { 2 } , b _ { 2 } ]$ , respectively. If there is a fuzzy number $\nu { \in } F ( \tilde { \mathbf { v } } _ { 1 } , \tilde { \mathbf { v } } _ { 2 } )$ , its membership function is,

$$
\mu^ {\tilde {v}} (z) = \left\{ \begin{array}{c c} 0 & z \leq \alpha c _ {1} + (1 - \alpha) c _ {2} \text {   or   } z \geq \alpha d _ {1} + (1 - \alpha) d _ {2} \\ \mu^ {\tilde {v}} [ \alpha f _ {1} (r) + (1 - \alpha) f _ {2} (r) ] & \alpha c _ {1} + (1 - \alpha) c _ {2} \leq z \leq \alpha a _ {1} + (1 - \alpha) a _ {2} \\ \mu^ {\tilde {v}} [ \alpha g _ {1} (r) + (1 - \alpha) g _ {2} (r) ] & \alpha b _ {1} + (1 - \alpha) b _ {2} \leq z \leq \alpha d _ {1} + (1 - \alpha) d _ {2} \\ 1 & \alpha c _ {1} + (1 - \alpha) c _ {2} \leq z \leq \alpha b _ {1} + (1 - \alpha) b _ {2} \end{array} \right.
$$

In which $r { = } \mu _ { \mathfrak { d } } ( z )$ and $f _ { i } ( r ) , g _ { i } ( r )$ are the inverse function of $r { = } \mu _ { \tilde { \mathrm { v } } } ( z )$ in $[ c _ { i } , a _ { i } ] , [ b _ { i } , d _ { i } ] , ( i { = } 1 , 2 )$ . When an alternative is evaluated, if the evaluation of a certain attribute u˜ is located somewhere between the two fuzzy numbers $\tilde { \mathbf { u } } _ { k }$ and $\tilde { \mathrm { u } } _ { k + 1 }$ , the membership of u˜ can be determined based on the relative distance between $\tilde { \mathrm { u } } _ { k }$ and $\widetilde { \mathbf { u } } _ { k + 1 } ( k { = } 1 , 2 , . . . , 5 )$ , and u˜ is represented as $( \tilde { \mathrm { u } } _ { k } , ~ \tilde { \mathrm { u } } _ { k + 1 } , ~ \alpha )$ . If the evaluation of a certain attribute is the estimated value (number value) $t , t _ { r } { = } ( t { - } t _ { \operatorname* { m i n } } ) / ( t _ { \operatorname* { m a x } } { - } t _ { \operatorname* { m i n } } )$ should be calculated to find the value of $t _ { r }$ which represents the two fuzzy numbers that are closest to one another, as a is determined, the membership function is obtained [14].

## 3.2. Fuzzy linguistic evaluation

As described above, since much information needed in the design process is imprecise and vague, evaluations can be represented in terms of fuzzy linguistic variables and the evaluation universe $U { = } ( u _ { 1 } , \ u _ { 2 } , . \ . . , \ u _ { 5 } )$ . In this study the grey theory is used to determine the fuzzy linguistic value of related attributes [6,26,23].

(1) Function construction. There are five fuzzy numbers in universe $U ,$ and five variables correspond to the fuzzy numbers: bad, somewhat bad, fair, somewhat good, and good, assuming their functions are $f _ { i } ( x ) ( i { =                          } 1 , 2 , . . . , 5 )$ respectively.

$$
f _ {1} (x) = \left\{ \begin{array}{c c} 0 & x <   0 \text {   or   } x > 2 \\ 1 - x / 2 & 0 \leq x \leq 2 \end{array} \right.
$$

$$
f _ {2} (x) = \left\{ \begin{array}{c c} 0 & x <   0 \text {   or   } x > 4 \\ x / 4 + 1 / 2 & 0 \leq x \leq 2 \\ 2 - x / 2 & 2 \leq x \leq 4 \end{array} \right.
$$

$$
f _ {3} (x) = \left\{ \begin{array}{c c} 0 & x <   2 \text {   or   } x > 6 \\ x / 2 - 1 & 2 \leq x \leq 4 \\ 3 - x / 2 & 4 \leq x \leq 6 \end{array} \right.
$$

$$
f _ {4} (x) = \left\{ \begin{array}{c c} 0 & x <   4 \text {   or   } x > 8 \\ x / 2 - 2 & 4 \leq x \leq 6 \\ 4 - x / 2 & 6 \leq x \leq 8 \end{array} \right.
$$

$$
f _ {5} (x) = \left\{ \begin{array}{c c} 0 & x <   6 \text {   or   } r > 8 \\ x / 2 - 3 & 6 \leq x \leq 8 \end{array} \right.
$$

$f _ { i } ( x ) ( i { = } 1 , 2 , . . . , 5 )$ is shown in Fig. 2.

(2) Construct evaluation matrix D. The evaluation matrix D is constructed according to the scores provided by experts,

$$
\mathrm{D} = \left\lfloor d _ {i j} \right\rfloor_ {M \times N}
$$

in which, $d _ { i j }$ is the ith expert group score for the ith attribute (determinable value), M is the number of expert groups and N is the number of attributes.

![](/api/attachments/H6VCXRH3/fulltext/images/cba73454b7a2d0df6bb9f1fe59a81d985b7cfe90bb0a8d6c38308bd821b8c7be.jpg)  
Fig. 2. Function construction.

(3) Calculate the decision coefficient $n _ { j k }$ . Decision coefficient is the coefficient for the jth attribute in kth ranking $( k { = } 1 , 2 , . . . . , 5 )$ , it is calculated as,

$$
n _ {j k} = \sum_ {i = 1} ^ {M} f _ {k} (d _ {i j}) \times N _ {i}
$$

where $N _ { i }$ is the number of experts in the ith expert group.

(4) Define the decision weight vector $r _ { j } ,$ and evaluation variables to which the attribute relates. The decision weight vector represents the weight that the $i _ { \mathrm { t h } }$ attribute has in the ranking. It is calculated as,

$$
r _ {j} = \left(r _ {j 1}, r _ {j 2},..., r _ {j 5}\right)
$$

in which, $\begin{array} { r } { r _ { j k } = n _ { j k } / n _ { j } ( k { = } 1 , \ 2 , . . . , \ 5 ) , \ n _ { j } = \sum _ { k = 1 } ^ { 5 } n _ { j k } } \end{array}$

If the $r _ { j k ^ { * } }$ is the largest in $r _ { j k } , r _ { j k * } = \operatorname* { m a x } _ { k } \left. r _ { j k } \right.$ then the jth attribute belongs to the jth grey ranking. According to the corresponding relation between grey ranking and fuzzy linguistic variables, the jth fuzzy linguistic evaluation value can be obtained.

## 3.3. Weights on evaluation criteria

Evaluation weights can be represented in two different ways. One way to represent weights is to assign them numeric values. Another way is to use fuzzy linguistic variables such as <sup>b</sup>important,<sup>Q b</sup>very important<sup>Q</sup>, and so on. Assuming the weights of attributes are represented with fuzzy linguistics, the method introduced in Section 3.2 can be used to determine weights. There are five grey rankings that correspond to the evaluation universe. The fuzzy linguistic weights can be determined by using grey statistic methods and there are several methods for normalizing weights.

Analytical Hierarchical Process (AHP) technique is a popular method that has been widely used [8,16,22]. One of the strengths of AHP lies in its ability to structure multi-attribute and multi-period problems hierarchically. AHP provides remarkable versatility and power in structuring and analyzing complex multi-attribute decision-making problems.

The AHP solution process consists of three steps with an optional concurrent fourth step as follows: (1) determination of the relative importance of attributes and sub-attributes if any; (2) determination of relative standing (weight) of each alternative with respect to each sub-attribute, if applicable, and then successively with respect to each attribute; (3) determination of the overall priority weight (score) of each alternative; and (4) determination of consistency indicator(s) in making pairwise comparisons.

As indicated by Sun et al. [17], pairwise comparison begins with comparing the relative importance of two selected items, the ith item and the jth item, for evaluation. If n items are associated with n weights, $w _ { 1 } , \quad w _ { 2 } , . . . , \quad w _ { n } ,$ the relative importance, $a _ { i j } ,$ is obtained as $a _ { i j } { = } w _ { i } / w _ { j }$ . The evaluation matrix is as follows,

$$
A = \left[ \begin{array}{c c c c} a _ {1 1} & a _ {1 2} & \dots & a _ {1 n} \\ a _ {2 1} & a _ {2 2} & \dots & a _ {2 n} \\ \vdots & \vdots & \vdots & \vdots \\ a _ {n 1} & a _ {n 2} & \dots & a _ {n n} \end{array} \right]
$$

In which, $a _ { i i } { = } 1 , a _ { i j } { = } 1 / a _ { j i } ,$ since an item is equally important as itself, the value of a diagonal element in the matrix is 1, and values of the elements in the upper triangle of the matrix are the reciprocal values of the elements in the lower triangle of this matrix, only $n ( n { - } 1 ) / 2$ times of comparisons are needed [17]. In a general case, instead of having the precise values of $w _ { i } / w _ { j }$ , only estimates of them are available. Estimation errors may result in inconsistency of the data in the pairwise ratio matrix. Therefore, a consistency index CI is developed to evaluate the deviation from consistency of the pair wise ratios. When values of the elements of a reciprocal matrix are randomly generated, the CI for the matrixes is represented as RI. The ratio of CI to RI for the same order matrices is called the consistency ratio (CR).

In identifying the importance measure of items, it is necessary to specify how a particular item is more important than the other. The comparison values, $a _ { i j } ,$ are defined on a scale of 1 to 9, as shown in Table 1. The calculated weights for items are scaled to a range between 0 and 1 for representing the importance measures. Five fuzzy measures have been developed for modeling the importance of attributes such as bad, somewhat bad, fair, somewhat good, and good.

Table 1  
Scales for comparison of factors [14,17]

<table><tr><td> $a_{ij}$ </td><td>Comparison of the  $i$ th factor and the  $j$ th factor</td></tr><tr><td>1</td><td> $i$ th factor is equally important as the  $j$ th factor</td></tr><tr><td>3</td><td> $i$ th factor is slightly more important than the  $j$ th factor</td></tr><tr><td>5</td><td> $i$ th factor is much more important than the  $j$ th factor</td></tr><tr><td>7</td><td> $i$ th factor is far more important than the  $j$ th factor</td></tr><tr><td>9</td><td> $i$ th factor is extremely more important than the  $j$ th factor</td></tr><tr><td>2, 4, 6, 8 Reciprocal</td><td>intermediate comparison values these values are the inverse comparison of  $a_{ij}$ </td></tr></table>

## 3.4. Comprehensive fuzzy evaluation

Single factor evaluation of attributes should be made before a comprehensive evaluation. Those single factors can be represented with numeric values or fuzzy numbers. If the numeric values or fuzzy numbers were not within the evaluation universe $U ,$ the concept of a fuzzy line segment is used to determine membership functions and the membership functions for the weights of attributes. If there are m alternatives, n evaluation criteria, and n weights for each alternative, then a fuzzy number $\tilde { \mathbf { u } } _ { i j } \ ( i { = } 1 , \ 2 , \ldots ,$ $m ; j { = } 1 , 2 , . . . , n )$ is used to represent fuzzy numbers of alternatives, and $\tilde { \mathbf { w } } _ { j } ( j { =                         } 1 , 2 , . . . . , n )$ for weights.

Based on the membership function of design alternatives’ evaluation criteria and the membership function of fuzzy objectives, the evaluation value of the attribute and the absolute value of the attribute with a fuzzy objective can be calculated, and then those alternatives can be evaluated using the weight mean values.

Fuzzy difference and fuzzy absolute difference: Assuming $\tilde { \mathrm { u } } _ { i j }$ is the evaluation of the jth attribute of the ith alternative, $\tilde { \mathrm { G } } j$ is the fuzzy objective of the jth attribute, according to the definition of fuzzy difference [7],

$$
\tilde {D} _ {i j} = \tilde {\boldsymbol {u}} _ {i j} \Theta \tilde {G} _ {j} = \tilde {\boldsymbol {u}} _ {i j} \oplus (- \tilde {G} _ {j})
$$

In which, the membership function of $( - \tilde { \mathrm { G } } _ { j } )$ is,

$$
\mu_ {\left(- \tilde {G} _ {j}\right)} (z) = \mu_ {\tilde {G} _ {j}} (- z)
$$

Fuzzy absolute difference $| \widetilde { \mathrm { D } } _ { i j } |$ is,

$$
\mu_ {| \widetilde {D} _ {j} |} = \left\{ \begin{array}{c l} \max \Bigl \lfloor \mu_ {\widetilde {D} _ {i j}} (z), \mu_ {\bigl (- \widetilde {D} _ {i j} \bigr)} (z) \Bigr \rfloor & z \geq 0 \\ 0 & z <   0 \end{array} \right.
$$

Comprehensive fuzzy evaluation: According to the fuzzy absolute difference $| \tilde { \mathrm { D } } _ { i j } |$ of the fuzzy evaluation $\tilde { \mathrm { u } } _ { i j }$ with the fuzzy goal $\tilde { \mathrm { G } } _ { j }$ and the fuzzy weights of attributes $\tilde { \mathrm { W } } _ { j } ,$ , the comprehensive fuzzy evaluation matrix $\tilde { \mathrm { R } } _ { i }$ can be obtained,

$$
\tilde {R} _ {i} = \sum_ {j = 1} ^ {n} \tilde {W} _ {j} | \tilde {D} _ {i j} | (i = 1, 2,.., m)
$$

With the extensive principle in fuzzy theory, we can obtain [19],

$$
\begin{array}{c} \mu_ {\tilde {R} _ {i}} (z) = \sup _ {g (y) = z} \left\{\left[ \bigwedge_ {j = 1} ^ {n} \mu_ {\tilde {W} _ {i}} \left(W _ {j}\right) \right] \bigwedge_ {j = 1} ^ {n} \left[ \mu_ {| \mathcal {D} _ {i j} |} \left(d _ {i j}\right) \right] \right\} \\ (i = 1, 2,.., m) \end{array}
$$

In which $g ( y ) = \sum _ { j = 1 } ^ { n } W _ { j } d _ { i j } .$

## 3.5. Ranking fuzzy numbers

We can obtain the fuzzy evaluation value $\tilde { \mathrm { R } } _ { i }$ based on the comparison of the design alternatives. $\tilde { \mathrm { R } } _ { i }$ is a fuzzy number. In order to observe how satisfied the alternatives are and how close the alternatives are to the fuzzy goal, a ranking process is needed on the fuzzy numbers. Numerous methods have been proposed to compare fuzzy numbers including the one proposed by Chen [5]. Due to its simplicity, the method has been very popular.

According to this method, we should find the maximum limitation $S _ { \mathrm { m a x } }$ and minimum limitation $S _ { \mathrm { m i n } }$ in the subset of fuzzy numbers for comparison, and draw two lines through point $( S _ { \mathrm { m a x } } , \ 1 )$ , point $( S _ { \mathrm { m i n } } , 0 )$ and point $( S _ { \mathrm { m a x } } , 0 )$ , point $( S _ { \mathrm { m i n } } , 1 )$ as Fig. 3 shows; two lines cross with the membership functions of fuzzy numbers, and the cross points are $K _ { g }$ and $K _ { m } .$

According to $K _ { g }$ and $K _ { m }$ , the permutation value of $\tilde { \mathrm { R } } _ { i }$ can be obtained as,

$$
K (i) = K _ {m} (i) + 1 - K _ {g (i)}
$$

![](/api/attachments/H6VCXRH3/fulltext/images/e8fa443e2b289a3da76ed13374336a9685d9642d0206d65c12644d6e98d1d294.jpg)  
Fig. 3. Comparison of fuzzy numbers.

The smaller the K(i) is, the closer the alternative to the goal is [14,24]; as a result, the alternative which has the smallest order value is the best alternative.

## 4. Decision support systems for concurrent engineering design

There are two kinds of decision support systems in concurrent engineering design. One is a distributed decision support system in a networking environment; the other is stand alone system. Stand alone decision support systems in concurrent engineering are concurrent in macro and serial in micro, as shown in Fig. 4 [14]. There are two concurrent subsystems in this model: one is an external concurrent subsystem that is consisted of market investigation, material, and external components, which can offer designers accurate external information. The other is an internal subsystem that is consisted of conceptual design, assembly design, manufacturing design, and so forth.

Many alternatives from each design stage can be accommodated for evaluation, and related decisions must be made based on such evaluations. In addition, systems simulation can be conducted to check the quality of decision. Due to the complexity involved, it may not be possible to reach perfect solutions subject to all constraints; however, we can obtain the solution that makes an overall good design and takes all important factors into consideration.

## 4.1. Multi-stage fuzzy decision-making model

The optimal product design plays a significant role in new product development and becomes one of the most crucial tasks in manufacturing. Many research ers have studied optimal product design [1]. There are so many factors in concurrent engineering design that each of them should be taken into account; meanwhile, there are so many design alternatives that have been generated in different design stages that need to be evaluated. Obviously, the impact of decisions from one stage to another is critical. As indicated by Zhao et al. [27], a decision for the current stage depends on the decisions result from previous stage, and the final design is reached through the evolution of a design process stage by stage. In this study, concurrent engineering product design is treated as a multi-stage fuzzy decision process as Fig. 5 shows, and the decisions are made based on the practice of concurrent engineering, dynamic programming, and fuzzy sets theory [19,20,2,25,1]. In Fig. 5, $S _ { k } ~ ( k { = } 1$ $2 , . . . , N )$ are state variables which represent alternatives in kth stages, $S _ { k }$ is a value in status space $X _ { k } { = } \{ x _ { k } ^ { ( 1 ) } , x _ { k } ^ { ( 2 ) } , { \textrm { - } } { \bot } x _ { k } ^ { ( n ) } \}$ , and $X _ { k }$ is the set of alternatives in kth stages, and $r _ { k }$ is used to represent the number of alternatives.

![](/api/attachments/H6VCXRH3/fulltext/images/624b14038f93a9dc274730132935b369b69ab89c2436e79176e4ef99e5aadffc.jpg)  
Fig. 4. Single computer concurrent evaluation model.

![](/api/attachments/H6VCXRH3/fulltext/images/be002b95c50c6d6495425dcca8319790a747c02cca62790875048a1fc6cb7dae.jpg)  
Fig. 5. Multiclass fuzzy decision-making model.

![](/api/attachments/H6VCXRH3/fulltext/images/0f807ddc5b05387d628a146bba4f642934f4872e3ece4c129dd5870d204c11f1.jpg)  
(a) Alternative 1

![](/api/attachments/H6VCXRH3/fulltext/images/1df0e2cdcb06a9a6b26d6519c2ebf96729710c1550b828a4b59fb2e176d46154.jpg)  
(b) Alternative 2  
Fig. 6. Design stage.

In the following, $u _ { k }$ is a decision variable that represents the design decision of kth stage; it also represents the state from the current stage to the next stage. $\mu _ { k } ( u _ { k } )$ is the membership function for the decision variable $u _ { k }$ subject to fuzzy constraints; it is also the membership function for a certain state with fuzzy objectives from the kth stage to the next stage. $\mu _ { N } ^ { \textit { G } } ( S _ { N } )$ is the membership function for the design

![](/api/attachments/H6VCXRH3/fulltext/images/c67909618d3b65a3b166f2de3b6ba88ef638aac50506bf601c6f20f6b7809901.jpg)  
Fig. 7. DFA stage.

![](/api/attachments/H6VCXRH3/fulltext/images/900b63faa237a11b703a2c24a222981f23e59a3d01d1848855bbd339389a6544.jpg)  
Fig. 8. DFM stage.

state $S _ { N }$ in the latest stage subject to its fuzzy objectives. k is a stage variable that represents the stage of product design; if N stages are available, then $k { = } 1 , 2 , . . . , N$

In a multi-stage fuzzy decision system, a number of decisions, $u _ { 1 } , ~ u _ { 2 } , . . . , u _ { N - 1 } ,$ are combined into a general strategy with membership function to the fuzzy goal as,

$$
\begin{array}{l} \mu_ {p} (u _ {1}, u _ {2},.., u _ {N - 1}) \\ = \mu_ {1} (u _ {1}) \wedge \mu_ {2} (u _ {2}) \wedge \dots \wedge \mu_ {N - 1} (u _ {N - 1}) \wedge \mu_ {N} ^ {G} (S _ {N}) \end{array}
$$

The last system state $S _ { N }$ can be obtained through the state transfer function as,

$$
s _ {k + 1} = T _ {k} (s _ {k}, u _ {k}) \quad k = 1, 2,..., N - 1
$$

Let $u _ { 1 } ^ { m } , u _ { 2 } ^ { m } , . . . , u _ { N - 1 } ^ { m }$ represent the optimal strategy, then

$$
\begin{array}{l} \mu_ {p} \big (u _ {1} ^ {m}, u _ {2} ^ {m},..., u _ {N - 1} ^ {m} \big) \\ = \max \big \{\mu_ {1} \big (u _ {1} \big) \wedge \mu_ {2} \big (u _ {2} \big) \wedge \cdot \cdot \wedge \mu_ {N - 1} \big (u _ {N - 1} \big) \wedge \mu_ {N} ^ {G} (S _ {N}) \big \} \end{array}
$$

According to the dynamic programming principle, a backward procedure that calculates backward recursively is used. The formula is,

$$
\begin{array}{l} \mu_ {p} (u _ {1}, u _ {2},.., u _ {N - 1}) \\ = \mu_ {1} (u _ {1}) \wedge \mu_ {2} (u _ {2}) \wedge \dots \wedge \mu_ {N - 1} (u _ {N - 1}) \wedge \mu_ {N} ^ {G} (S _ {N}) \end{array}
$$

where

$$
\begin{array}{l} u _ {p} \big (u _ {1} ^ {m}, u _ {2} ^ {m},..., u _ {N - 1} ^ {m} \big) = \max \big \{\mu_ {N - 1} (u _ {N - 1}) \wedge \mu_ {N} ^ {G} (S _ {N}) \big \} \\ = \max \big \{\mu_ {1} (u _ {1}) \wedge \mu_ {2} (u _ {2}) \wedge \dots \wedge \mu_ {N - 1} (u _ {N - 1}) \wedge \mu_ {N} ^ {G} (S _ {N}) \big \} \\ = \dots = \max \big \{\mu_ {1} (u _ {1}) \wedge \mu_ {2} ^ {G} (s _ {2}) \big \} = \mu_ {1} ^ {G} (s _ {1}) \end{array}
$$

Here,

$$
\mu_ {N - i} ^ {G} (s _ {N - i}) = \max \bigl \{\mu_ {N - i} (u _ {N - i}) \wedge \mu_ {N - i + 1} ^ {G} (s _ {N - i + 1}) \bigr \}
$$

$$
s _ {N - i + 1} = T _ {N - i} (s _ {N - 1}, u _ {N - i}) \quad i = 1, 2,.., N - 1
$$

We can obtain $\mu _ { N - 1 } ^ { G } ( s _ { N - 1 } ) , \mu _ { N - 2 } ^ { G } ( s _ { N - 2 } ) , . . . , \mu _ { 1 } ^ { G } ( s _ { 1 } ) .$ In which $\mu _ { 1 } ^ { G } ( s _ { 1 } )$ is the answer for $u _ { p } ( u _ { 1 } ^ { m } , \ u _ { 2 } ^ { m } , . . . ,$

Stage one fuzzy linguistic evaluation

<table><tr><td>Alternative</td><td> $x_{1}^{(1)}$ </td><td> $x_{1}^{(2)}$ </td></tr><tr><td>Evaluation</td><td> $\tilde{u}_{5}$ </td><td> $(\tilde{u}_{4},\tilde{u}_{5},0.8)$ </td></tr></table>

Stage two fuzzy linguistic evaluation

<table><tr><td>Alternative</td><td> $x_{2}^{(1)}$ </td><td> $x_{2}^{(2)}$ </td><td> $x_{2}^{(3)}$ </td><td> $x_{2}^{(4)}$ </td></tr><tr><td>Evaluation</td><td> $(\tilde{u}_{4},\tilde{u}_{5},0.8)$ </td><td> $\tilde{u}_{4}$ </td><td> $(\tilde{u}_{4},\tilde{u}_{5},0.5)$ </td><td> $\tilde{u}_{5}$ </td></tr></table>

$u _ { N - 1 } ^ { ~ m } )$ . The $u _ { i }$ which satisfies the equation is represented as $u _ { i } ^ { m } ( i { =               { 1 } , \ { 2 } , . . . , \ N { - 1 } ) }$ ; the optimal strategy is $u _ { 1 } ^ { m } , u _ { 2 } ^ { m } , . . . , u _ { N - 1 } ^ { m }$

## 4.2. Compute $\mu _ { N } ^ { G } ( s _ { N } )$ and l<sub>k</sub>(s<sub>N</sub>)

As described above, $\mu _ { N } ^ { G } ( s _ { N } )$ is the membership function for the latest design state with fuzzy goals, and the latest design state is a value of the set $X _ { N } { = } \{ x _ { N } ^ { ( 1 ) } , ~ x _ { N } ^ { ( 2 ) } { , } . . . , ~ x _ { N } ^ { ( r _ { n } ) } \} ; ~ { \mu } _ { k } ( u _ { k } )$ represents the membership function of the kth stage with fuzzy goals, that is $\mu _ { k } ( u _ { k } ) { = } \mu _ { k } ( s _ { k } ) , s _ { k }$ is the value of the set $X _ { k } { = } \{ x _ { k } ^ { ( 1 ) } , x _ { k } ^ { ( 2 ) } , . . . , x _ { k } ^ { ( r _ { n } ) } \} , k { = } 1 , 2 , . . . , N { - } 1$ . After making fuzzy evaluation on each alternative, a ranking value $K ( i )$ as described in Section 3.5 can be obtained. If $r _ { k }$ alternatives are available in the kth design stage, there must be $r _ { k }$ ranking values as $K ( i )$ 4 $( i { = } 1 , 2 , . . . . , r _ { k } )$ . Assuming that $\begin{array} { r } { K _ { \operatorname* { m i n } } = \mathrm { M i n } _ { i = 1 } ^ { r _ { k } } \{ K ( i ) \} } \end{array}$ , since the smaller the $K ( i )$ is, the closer the alternative is to the design goal, $K _ { \mathrm { m i n } } / K ( i )$ is used to represent the membership function of alternatives that correspond to the goal. The formula is,

$$
\mu_ {N} ^ {G} (s _ {N}) = \frac {K _ {\mathrm{min}}}{K (i)}
$$

in which, $K _ { \operatorname* { m i n } } = \operatorname* { M i n } _ { i = 1 } ^ { r _ { k } } \{ K ( i ) \}$

$$
\mu_ {k} (u _ {k}) = \frac {K _ {\mathrm{min}}}{K (i)}
$$

$$
\text { where } K _ {\min} = \underset {i = 1} {\overset {r _ {k}} {\operatorname{Min}}} \left\{K (i) \right\} \quad (k = 1, 2,..., N - 1)
$$

## 5. Implementation

Based on the methods and techniques introduced earlier, a decision support system called Decision

<table><tr><td colspan="6">Table 4Stage three fuzzy linguistic evaluation</td></tr><tr><td>Alternative</td><td> $x_{3}^{(1)}$ </td><td> $x_{3}^{(2)}$ </td><td> $x_{3}^{(3)}$ </td><td> $x_{3}^{(4)}$ </td><td> $x_{3}^{(5)}$ </td></tr><tr><td>Evaluation</td><td> $(\tilde{u}_{3}, \tilde{u}_{4}, 0.5)$ </td><td> $(\tilde{u}_{4}, \tilde{u}_{5}, 0.8)$ </td><td> $(\tilde{u}_{4}, \tilde{u}_{5}, 0.5)$ </td><td> $(\tilde{u}_{4}, \tilde{u}_{5}, 0.5)$ </td><td> $\tilde{u}_{5}$ </td></tr></table>

![](/api/attachments/H6VCXRH3/fulltext/images/351b34fedeffb5df93dee9d5e65bba2822558c50f7579bf77afbb19d3a85506c.jpg)  
Fig. 9. Membership function in stage one.

Support System for Concurrent Engineering (DSSF-CD) is developed and implemented in real-world environment. In this example run, conceptual design alternatives for a machining center are analyzed using the decision support system developed. Example alternatives are shown in Figs. 6–8. The design procedure consists of three steps: (1) initial design (Fig. 6); (2) design for assembly (DFA, Fig. 7); and (3) design for manufacturing (DFM, Fig. 8).

The evaluation criterion for stage one is <sup>b</sup>comprehensiveness of functionalities<sup>Q</sup>, for stage two is <sup>b</sup>reliability<sup>Q</sup>, and for stage three is <sup>b</sup>compactness<sup>Q</sup> (Tables 2–4).

Assuming the fuzzy goals of each stage are all ${ \tilde { \mathsf { u } } } _ { 5 } ,$ according to the absolute difference of evaluation goal with the alternatives’ fuzzy evaluations, we can obtain the membership function of each fuzzy evaluation as,

The alternatives’ fuzzy evaluation membership functions in three stages are shown in Figs. 9–11 and Tables 5–7. Based on the multi-stage fuzzy decision-making model in the DSSFCD, corresponding to the fuzzy goal, we can obtain the optimal membership function to fuzzy goal $\mu _ { p } { = } 0 . 8 3 3$ , the optimal strategy is $x _ { 1 } ^ { ( 2 ) } , x _ { 2 } ^ { ( 4 ) } , x _ { 3 } ^ { ( 5 ) }$ , and the optimal alternative is $\overline { { x _ { 3 } ^ { ( 5 ) } } }$ . Finally the best product scheme is selected.

![](/api/attachments/H6VCXRH3/fulltext/images/847ab2650dbeb8ac6e34cb11d4187f4521683148121dac5b7e3e749b39cb8a75.jpg)  
Fig. 10. Membership function in stage two.

![](/api/attachments/H6VCXRH3/fulltext/images/880a6864dd5c1bbe9255a7906946e136eaea500badd6aff0acf121692baac030.jpg)  
Table 6  
Fig. 11. Membership function in stage three.

## 6. Conclusion

In concurrent engineering product design, it is crucial to evaluate the design comprehensively. Due to lack of information, in the early design process, problems can arise when information is fuzzy and goals are known imprecisely which makes the design evaluation difficult. It is not easy for designers to evaluate alternatives precisely. The designer should take the concurrent effects of the product design into consideration. If the previous decision is incorrect, the following design stages will be affected significantly. Concurrent product development processes need effective decision support systems. In view of this, a decision support system has been proposed for the multi-stage fuzzy decision-making tasks in concurrent engineering.

The concept of fuzzy line segments is introduced to make the universe of discourse continuous, which makes it possible to not restrict the designer to a small set of fuzzy inputs. The fuzzy line segment also makes it possible to better reflect the designers<sup>T</sup> estimate of the performance of design alternatives and the relative weight assigned to each attribute. It facilitates more accurate and precise linguistic inputs, and provides a way to <sup>b</sup>fuzzify<sup>Q</sup> numeric inputs. This paves the way for AHP to assist designers in the determination of attribute weights.

Table 5  
Membership function in stage one  
Table 7

<table><tr><td>Alternative</td><td> $x_{1}^{(1)}$ </td><td> $x_{1}^{(2)}$ </td></tr><tr><td>Evaluation</td><td>1.00</td><td>0.833</td></tr></table>

Membership function in stage two

<table><tr><td>Alternative</td><td> $x_{2}^{(1)}$ </td><td> $x_{2}^{(2)}$ </td><td> $x_{2}^{(3)}$ </td><td> $x_{2}^{(4)}$ </td></tr><tr><td>Evaluation</td><td>0.4</td><td>0.5</td><td>0.667</td><td>1.00</td></tr></table>

In this paper, after introducing the concept of fuzzy numbers and fuzzy line segments, fuzzy linguistics and estimate value with fuzzy numbers were discussed. How the grey theory can be used to determine the evaluation of attributes and weights was also described. After analyzing the nature of decision-making in concurrent engineering design, a multi-stage decision-making model in concurrent engineering product design was proposed. The reason for developing the system was to improve the concurrent engineering process or practices by improving related decision-making processes. The system is able to evaluate alternatives comprehensively using weighted means absolute difference, and rank the alternatives. The system is beneficial in improving design capability in terms of enabling engineers to evaluate design alternatives with interrelated criteria such as functionality, reliability, manufacturability to achieve DFx (Design for x), with x as one of the criteria [10,17]. The system provides decision support aids to not only capture the features of different concurrent design stages, but also to perform automated decision support for DFx. The what-if-analysis, i.e., what would happen if a particular decision is taken, is one of the most useful functionalities provided by the system. The implementation results show that the system is practical and useful for concurrent engineering product design.

Membership function in stage three

<table><tr><td>Alternative</td><td> $x_{3}^{(1)}$ </td><td> $x_{3}^{(2)}$ </td><td> $x_{3}^{(3)}$ </td><td> $x_{3}^{(4)}$ </td><td> $x_{3}^{(5)}$ </td></tr><tr><td>Evaluation</td><td>0.445</td><td>0.667</td><td>0.5</td><td>0.833</td><td>1.00</td></tr></table>

## Acknowledgement

This research was supported in part by the National Natural Science Foundation of China (NSFC) under the Grant 50982005. The collaboration between the authors was made possible by a research grant provided by the Chinese Ministry of Education and the Chinese State Key Laboratory of Mechanical Manufacturing Systems Engineering.

## References

[1] G. Alexouda, A user-friendly marketing decision support system for the product line design using evolutionary algorithms, Decision Support Systems 38 (4) (2005) 495–509.

[2] P. Balakrishnan, V. Jacob, Triangulation in decision support systems: algorithms for product design, Decision Support Systems 14 (1995) 313–327.

[3] J. Carnahan, D. Thurston, T. Liu, Fuzzy ratings for multiattribute design decision-making, Journal of Mechanical Design 116 (2) (1994) 511 –521.

[4] A. Chang, C. Holsapple, A. Whinston, Model management issues and directions, Decision Support Systems 9 (1) (1993) 19– 38.

[5] S. Chen, Ranking fuzzy numbers with maximizing sets and minimizing sets, Fuzzy Sets and Systems 17 (2) (1985) 113–129.

[6] P. Chen, J. Jou, Adaptive arithmetic coding using fuzzy reasoning and grey prediction, Fuzzy Sets and Systems 114 (2000) 239–254.

[7] D. Dubois, H. Prade, Operations on fuzzy numbers, International Journal of Systems Science 9 (1978) 613– 626.

[8] S. Feng, L. Xu, Decision support for fuzzy comprehensive evaluation of urban development, Fuzzy Sets and Systems 105 (1999) 1 –12.

[9] S. Gupta, D. Nau, Systematic approach to analyzing the manufacturability of machined parts, CAD Computer Aided Design 27 (5) (1995) 323– 342.

[10] B. Haque, R. Belecheanu, R. Barson, K. Pawar, Towards the application of case based reasoning to decision-making in concurrent product development, Knowledge-Based Systems 13 (2000) 101–112.

[11] K. Ishii, Life-cycle engineering design, Journal of Mechanical Design 117B (1995) 42– 47.

[12] G. Kim, Case-based design for assembly, CAD Computer Aided Design 29 (7) (1997) 497– 506.

[13] H. Li, L. Li, Integrating systems concepts into manufacturing information systems, Systems Research and Behavioral Science 17 (2000) 135– 147.

[14] S. Li, Z. Li, A Rapid and Comprehensive Evaluation Method for Conceptual Design. Research Report, CIMS Center, Xian Jiaotong University, 2004.

[15] B. Ramesh, A. Tiwana, Supporting collaborative process knowledge management in new product development teams, Decision Support Systems 27 (1999) 213–235.

[16] T. Saaty, L. Vargas, Models, Methods, Concepts and Applications of the Analytical Hierarchy process, Kluwer Academic Publishers, Boston, 2001.

[17] J. Sun, D. Kalenchuk, D. Xue, P. Gu, Design candidate identification using neural network-based fuzzy reasoning, Robotics and Computer-Integrated Manufacturing 16 (2000) 383– 396.

[18] A. Tiwana, B. Ramesh, A design knowledge management system to support collaborative information product evolution, Decision Support Systems 31 (2001) 241 – 262.

[19] T. Tseng, C. Klein, New algorithm for the ranking procedure in fuzzy decision-making, IEEE Transactions on Systems, Man, and Cybernetics 19 (5) (1989) 1289– 1295.

[20] L. Xu, A fuzzy multi-objective programming algorithm in decision support systems, Annals of Operation Research 12 (1989) 315– 320.

[21] L. Xu, The contribution of systems sciences to information systems research, Systems Research and Behavioral Science 17 (2) (2000) 105–116.

[22] S. Xu, L. Xu, X. Chen, Determining optimum edible films for kiwifruits using an analytical hierarchy process, Computers & Operations Research 30 (2003) 877– 886.

[23] P. Yang, J. Zhu, Gray evaluation of attributes for the multiattribute design decision-making, Proceedings of 1999 International Conference on Advanced Manufacturing Technology, Xian, China, 1999, pp. 738–739.

[24] P. Yang, J. Zhu, Research on Product Design Process within Concurrent Environment, Xian Jiaotong University Press, 2000.

[25] P. Yang, J. Zhu, S. Wen, Decision-making of product design for concurrent engineering, Journal of Xi’an Jiaotong University 34 (2) (2000) 85– 88.

[26] D. Yi, G. Pin, Gray Theory and Methods, Petroleum Industry Press, Beijing, 1992.

[27] H. Zhao, Y. Zhang, Z. Wang, S. Lee, W. Kwong, Research on group decision support system for concurrent product development process, Journal of Materials Processing Technology 139 (2003) 619– 623.

Dr. Lida Xu is Professor of Information Technology at Old Dominion University, Norfolk, USA. He is also Professor of Computer Science/Information Technology at institutions including Graduate School of Chinese Academy of Sciences, Institute of Computing Technology of Chinese Academy of Sciences, Institute of Automation of Chinese Academy of Sciences, Xian Jiaotong University, Shanghai Jiaotong University, Huazhong University of Science and Technology, and Harbin Institute of Technology. He is the author of more than 100 papers.

Dr. Zongbin Li is a professor at Xian Jiaotong University (XJTU). He received his PhD in mechanical engineering in 1995 from Georgian Technical University, Tbilisi, Georgia, Soviet Union. He holds BS and MS degrees in Mechanical Engineering from XJTU. Currently, Dr. Li is the Deputy Director of the Chinese State Key Laboratory of Manufacturing System Engineering and Deputy Director of the CIMS Research Center at XJTU. His research interests include conceptual design, manufacturing systems modeling, simulation and optimization, knowledge engineering, and intelligent systems.

Shanchang Li was a graduate student at Xian Jiaotong University. He received his BS degree in mechanical engineering in 2001. His research interest is product conceptual design.

Fengming Tang was a graduate student at Xian Jiaotong University. She received her BS degree in mechanical engineering in 1999. Her research interest is product conceptual design.
