---
otero_id: 9636
otero_key: "9VYGMRU2"
title: "Optimal product positioning with consideration of negative utility effect on consumer choice rule"
authors: "X.G. Luo; C.K. Kwong; J.F. Tang; Y.L. Tu"
year: "2012"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2012.06.002"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Optimal product positioning with consideration of negative utility effect on consumer choice rule

X.G. Luo <sup>a,b,</sup>⁎, C.K. Kwong <sup>b</sup>, J.F. Tang <sup>a</sup>, Y.L. Tu <sup>c</sup>

<sup>a</sup> Department of Systems Engineering, State Key Lab of Synthetic Automation of Process Industries, Northeastern University, Shenyang, PR China

<sup>b</sup> Department of Industrial and Systems Engineering, The Hong Kong Polytechnic University, Hung Hom, Kowloon, Hong Kong, PR China

<sup>c</sup> Department of Mechanical and Manufacturing Engineering, University of Calgary, 2500 University Drive, NW, Calgary, Alberta, Canada

## a r t i c l e i n f o

Article history: Received 8 March 2011 Received in revised form 30 May 2012 Accepted 14 June 2012 Available online 23 June 2012

Keywords: Product positioning Consumer choice rule Interval analysis Tabu search

## a b s t r a c t

In most studies related to product positioning, probabilistic consumer choice rules assume that a product always gains some market share no matter how small a product's utility value is or even if the utility value is negative. Some researchers have considered this problem in multidimensional-scaling-based model or share-of-surplus choice rule. In this study, we consider this problem for multinomial logit rule by introducing a piecewise function and establishing a conjoint-analysis-based one-step optimization model for product positioning. Interval analysis is applied to obtain the optimal price of the new product from the model, and the mathematical properties of the pro<sup>fi</sup>t-maximizing model are analyzed. An interval-analysis-embedded Tabu Search (TS) algorithm is developed for solving the model. An industrial application employing the proposed model and the interval-analysis-based enumeration method is presented and sensitivity analysis is performed. An experiment for randomly created large-scale product positioning problems is carried out to evaluate the feasibility of the proposed TS algorithm.

© 2012 Elsevier B.V. All rights reserved.

## 1. Introduction

In the early stages of product development, a key decision that a development team makes is concerning product positioning [3]. Product positioning involves the determination of the levels of attributes of a new product to be developed given a data set containing customer preferences and information on competitors' products [43].

In the simulation of consumers' purchasing behaviors on product positioning, two kinds of consumer purchase rules have been widely applied in the extant research papers. The <sup>fi</sup>rst one is called the deterministic rule [37]. Under the deterministic rule, a consumer is assumed to be always choosing the product with the highest utility. However, the <sup>fi</sup>rst choice rule seems to represent an assumption too restrictive for many product categories and individual choice situations [38]. Moreover, evidence exists that for frequently purchased consumer nondurables, consideration set sizes are typically larger than one [25].

Another consumer choice rule, the probabilistic rule, more realistically represents consumer behavior toward purchase decisions [35]. Under the probabilistic rule, utility is assumed to be a random variable whereas the consumer purchase decision process is stochastic. Although there are many kinds of probabilistic rules (e.g., share-of-utility rule and multinomial logit rule), the expressions of the choice probabilities always have an ‘us/(us+them)’ form and a high product utility usually means a high choice probability.

The probabilistic rules employed in most research papers on product positioning assume that each product has a nonzero consumer choice probability. Hence, no matter how small a product's utility value is or even if the utility value is negative, the product always gains some market share. This negative utility effect on consumer choice rule is apparently unreasonable in practical scenarios because a consumer would not purchase a product that does not interest him/her. It may result in an estimation bias of market share toward a product and eventually affect product positioning [29].

Having realized this problem, a few researchers developed extended probabilistic rules to improve the estimation of choice probability. For example, Sudharshan, May, and Shocker [40] established a multidimensional scaling-based product positioning model which assumes that a consumer selects only the k closer products around the ideal point in the space and the choice probabilities of other products are zero. Kraus and Yano [29] developed a mixed-integer model for product line selection under a share-of-surplus choice rule. They constructed a constraint in their model to prevent those products with negative utility surplus from being selected. However, to the best of our knowledge, a research tackling this problem under multinomial logit rule has not yet been conducted.

The existing modeling approaches for product positioning can be classi<sup>fi</sup>ed into two categories, namely, the one-step approach and the two-step approach [28]. In the two-step approach, the set of feasible product pro<sup>fi</sup>les is reduced to a smaller reference set, and then an optimization model is established to <sup>fi</sup>nd the best product pro<sup>fi</sup>le from the reference set. On the other hand, the one-step approach aims at constructing product pro<sup>fi</sup>les directly from part-worth utilities and <sup>fi</sup>nding the optimal product pro<sup>fi</sup>le in a single step.

Most of the previous studies on product positioning adopted the two-step approach and focused on the second step, that is, the identi-<sup>fi</sup>cation of the best product pro<sup>fi</sup>le from a given set [8,10,11,15,29]. However, a number of product positioning problems in the real world involve a large number of attributes and levels, resulting in a large quantity of feasible product pro<sup>fi</sup>les, thus making it dif<sup>fi</sup>cult to determine a reduced set of few product pro<sup>fi</sup>les [34].

In this research, we extend the multinomial logit rule by integrating the dollar-scaled utility with a piecewise logit function, formulate a pro<sup>fi</sup>t-oriented one-step model under this rule for maximizing the total expected pro<sup>fi</sup>t in a multi-segment market, analyze the mathematical properties of the model, and develop algorithms to solve the model.

The rest of this paper is organized as follows. In Section 2, the research related to product positioning is brie<sup>fl</sup>y reviewed. In Section 3, a conjoint analysis-based one-step optimization model that considers the negative utility effect on consumer choice rule is formulated. In Section 4, solving strategy is discussed and interval-analysis-based algorithms are developed for the proposed model. In Section 5, an application of product positioning of digital cameras is described, and an experiment for randomly generated large-scale problems is performed to evaluate the feasibility of the proposed interval-analysis-embedded Tabu Search algorithm. Finally, conclusions are drawn in Section 6.

## 2. Literature review

In Section 2.1, we <sup>fi</sup>rst classify the optimization models of the product positioning problem according to consumer preference measurement, consumer choice rule, modeling strategy, product price, and objective function. In Section 2.2, we brie<sup>fl</sup>y introduce recent research papers applying probabilistic consumer choice rules.

## 2.1. Background

2.1.1. Consumer preference measurement: multidimensional scaling (MDS) or conjoint analysis (CA)

Two basic approaches have been used for modeling consumer preference in product positioning problems [32], namely, the multidimensional scaling (MDS) approaches and the conjoint analysis (CA) approaches.

In MDS approaches, each product is represented as a point in the multi-attributed perceptual space, whereas consumers are represented by their ideal point in the same space [22]. The ultimate goal of positioning is to identify an optimal new product position de<sup>fi</sup>ned by appropriate design attribute speci<sup>fi</sup>cations.

CA approaches consider a <sup>fi</sup>nite number of levels for each attribute and permit a preference function to bear an arbitrary relation to attribute levels through the use of dummy variables [37]. To calibrate the part-worth utilities in CA utility function, a number of respondents are invited to collect scaled preference evaluations with regard to a subset of multi-attribute product pro<sup>fi</sup>les (stimuli).

## 2.1.2. Consumer choice rule: deterministic or probabilistic

Optimization models under a deterministic rule typically have a relatively simple expression; many of them have been modeled as linear forms [9,11,33].

Compared with deterministic rules, probabilistic rules offer higher <sup>fl</sup>exibility in calibrating actual choice behavior. In general, there are two types of probabilistic choice rules [6], namely, the generalized (or powered) Bradley–Terry–Luce (BTL) share-of-utility rule (α-rule) and the multinomial logit (MNL) choice rule.

## 2.1.3. Modeling strategy: one-step or two step

The computation ef<sup>fi</sup>ciency of two-step approaches largely depends on the reference set. For problems using a large number of attributes and attribute levels, reference-set enumeration can become formidable if most multi-attribute items are feasible [28]. Another problem is that two-step approaches may miss the optimal product because the optimal solution may not be in the reference set at all.

In one-step approaches, part-worth utilities for product attributes are estimated according to the result of the ratings of some selected product pro<sup>fi</sup>les. In extrapolating other product pro<sup>fi</sup>les that have not been rated, simpli<sup>fi</sup>ed assumptions are made, such as additive utility structure and partial homogeneity across consumers. Moreover, the process of estimating part-worth utilities and segmentation is sensitive and prone to errors [11].

## 2.1.4. Product price as an attribute or separate variable

A higher product price may bring more market income, but it may also result in less market share since price clearly affects the choice behavior of most consumers [7,35]. The most convenient way to deal with product price would be treating it as one of the product's attributes [34]. Nevertheless, if there are large quantities of price levels, evaluating product pro<sup>fi</sup>les for part-worth utilities would be tedious work for respondents and the consistency of evaluations would be dif<sup>fi</sup>cult to maintain.

Another approach to treat product price, which has been applied in many economics-based product positioning models [11,33], is to consider price as a separate decision variable. Models treating price as a separate decision variable typically have a nonlinear form, and thus show a high computation complexity.

## 2.1.5. Objective function

The following objective functions have been used in the optimization models on product positioning:

1) Maximizing the total utility across consumers [15]. An optimization problem with this objective is called the buyers' welfare problem.

2) Maximization of seller's marginal utility [28], that is, to maximize the total value to a seller of the products chosen by consumers. This is called the seller's welfare problem.

3) Maximizing the number of consumers choosing the new products [26]. This objective function assumes that each consumer purchases one product; this objective actually is the same as maximization of gross product demand. A problem with this objective is called the share-of-choice problem.

4) Maximizing the pro<sup>fi</sup>t [10]. The total pro<sup>fi</sup>t is computed by aggregating the pro<sup>fi</sup>ts of each product in each segment, and then subtracting the <sup>fi</sup>xed cost.

5) Maximization of the total market share [40], including market share from the new products and the company's existing products.

6) Maximization of the shared surplus [24]. Shared surplus is a measurement for leveraging both customer and engineering concerns.

## 2.2. A brief review of related work

A large number of research papers on product positioning problem have been published in the past several decades. A discussion and comparison of methods can be found in the survey papers [5,16,25,35,36,46]. Here, we only review the recent research papers that have employed probabilistic rules.

Bachem and Simon [2] proposed an MDS model for optimal product positioning. The choice rule in their research is probabilistic and based on the Euclidean distance between a product position and the ideal point position in product attribute space. Costs are classi<sup>fi</sup>ed into three types and assumed linear to product position. The objective of the optimization is to minimize the total cost, with product price considered as a discrete product attribute.

Sudharshan, May, and Shocker [40] conducted a simulation study to examine and compare several algorithms for product positioning in an MDS space where both competition and demand are modeled. In their model, they assumed that a consumer selects only the k closer products around the ideal point in MDS space and the choice probabilities of other products are zero.

Chen and Hausman [8] developed a pro<sup>fi</sup>t maximization model for product line selection and pricing. In their two-step model, MNL is employed and price is treated as a separate discrete decision variable. They proved that the model is strictly quasi-concave; hence, standard nonlinear programming codes can be used. However, the mathematical properties that lead to an ef<sup>fi</sup>cient optimal algorithm will disappear if the <sup>fi</sup>xed cost is considered or the product market is multi-segmented.

Steiner and Hruschka [38] established a one-step model for product line design. Conjoint analysis is applied to measure consumer preference and the MNL rule is adopted as the probabilistic consumer choice rule. The objective of the model is to maximize the total pro<sup>fi</sup>t of a <sup>fi</sup>rm. In their model, variable costs are assumed available at the individual attribute level, and price is treated as a separate discrete decision variable.

Gruca and Klemz [18] presented an MDS model that aims at maximizing the total expected product demand from the market. The probabilistic consumer choice rule in their model is based on Euclidean distance. In particular, it supports the selection of a number of closer products to the ideal point in attribute space. Price is not considered in their model.

Kraus and Yano [29] established a two-step optimization model to maximize the total pro<sup>fi</sup>t of a product line. Unlike the previously mentioned research, they treated price as a continuous decision variable. In their model, a share-of-surplus rule, which is a variant of the BTL [6] rule, is adopted. They further indicated the negative utility problem and constructed a constraint in their mathematical model to prevent those products with negative utility surplus from being selected.

Jiao and Zhang [24] established a non-linear mixed-integer model to maximize the shared surplus of a product line. Shared surplus is a measurement used to indicate a customer's expectations of product quality in relation to the actual amount paid for it. The objective of the optimization is to leverage both customer and engineering concerns. The model follows a one-step strategy: MNL is applied to model the consumer choice and price is regarded as product attribute. A costing approach based on the standard time estimation technique is employed to process resource sharing in mass customization.

Albritton and McMullen [1] focused on solving the optimal product design problem for maximizing market share. In their research, the consumer choice process is modeled as an additive function of individual product attributes with a component of randomness included. The optimization model is not explicitly given in their paper.

## 3. Development of an optimization model

## 3.1. Partitioning market segments

Consumers who have different beliefs with respect to social issues (e.g., religion, politics, work, drugs, or women's rights) or personal interests (e.g., family, home, job, food, self-achievement, health, clubs, friends, or shopping) may have different purchasing behavior or preferences [45]. Product market consumers may have different responses toward a new product and make different selections if a family of new products is provided [41]. A market can often be partitioned into several segments such that in each segment, customers tend to have very similar purchasing preferences. First, a market survey needs to be conducted to understand the consumers' desired levels of product attributes. On the basis of the survey data, market segments can be identi<sup>fi</sup>ed using proper clustering techniques [23] and the size of each market segment (i.e., the expected number of consumers) can also be estimated.

## 3.2. Problem description

Consider a company that is going to develop a new product. The product is characterized by a set of K product attributes. The kth product attribute possesses $L _ { k }$ levels $( k = 1 , 2 , . . . , K )$ . Assuming that any combination of the attribute levels is valid, a product pro<sup>fi</sup>le can then be determined based on these combinations. Suppose that after partitioning a market, I market segments are identi<sup>fi</sup>ed and the ith segment contains $Q _ { i }$ customers $( i = 1 , ~ 2 , . . . , ~ I )$ . In the market, there are N competitor products. The price of the jth competitor's product in the market is $p _ { j } \left( j = 1 , 2 , . . . , N \right)$

In the present research, the aim of product positioning is to identify the optimal product pro<sup>fi</sup>le to maximize the total expected pro<sup>fi</sup>t of the new product. The decision variables of the optimization problem involved in the two aspects are as follows:

1) determining the price of a new product and

2) determining which level of each product attribute should be selected for the new product.

To facilitate the modeling, we use the following decision variables:

1) p: a continuous variable, denotes the price of the new product; and

2) $x _ { k l } ( k = 1 , 2 , \ldots , K ; l = 1 , 2 , \ldots L _ { k } ) \colon$ : a binary variable such that $x _ { k l } = 1$ if the lth level of the kth product attribute is selected for the new product, otherwise $x _ { k l } = 0$

## 3.3. Modeling customer preference

By following the part-worth utility model widely used in CA [28], the utility of a product pro<sup>fi</sup>le is considered a linear function of the part-worth utilities of the attribute levels of the product, that is,

$$
U _ {i} = \sum_ {k = 1} ^ {K} \sum_ {l = 1} ^ {L _ {k}} u _ {i k l} x _ {k l}\tag{1}
$$

where $U _ { i }$ is the utility of the new product in the ith market segment and u is the part-worth utility of the lth level of the kth attribute in the ith market segment. Many methods are available for estimating part-worth utilities, such as full-pro<sup>fi</sup>le conjoint, adaptive conjoint, hybrid conjoint, experimental choice, and choice-based conjoint analyses [24].

## 3.4. Consumer purchase choice

By following the popular MNL choice rule [6], the consumer choice rule can be modeled as follows:

$$
P _ {i} = \frac {e ^ {\mu U _ {i}}}{e ^ {\mu U _ {i}} + \sum_ {j = 1} ^ {N} e ^ {\mu U _ {i j}}}\tag{2}
$$

where $P _ { i }$ is the choice probability indicating the likelihood of a customer in the ith segment choosing a product, $U _ { i j }$ is the utility value of the jth competitor's product to the ith segment, and μ is a scaling parameter. If μ is very large, the model behaves like a deterministic rule, whereas if μ is close to zero, it becomes a uniform distribution [44].

We propose an improved consumer choice rule by integrating the dollar-scaled utility [10] with a piecewise logit function. The difference between the utility of a product (measured in dollars) and product price, which is called consumer surplus, is a measurement of a consumer's gain from purchasing a product. If the value is positive, the consumer bene<sup>fi</sup>ts; if it is negative, the consumer loses. Assuming that a consumer will never choose a product if the consumer surplus is negative, the consumer choice probability can then be formulated as follows:

$$
P _ {i} = \frac {\Gamma (U _ {i} , p)}{\Gamma (U _ {i} , p) + \sum_ {j = 1} ^ {N} \Gamma \left(U _ {i j} , p _ {j}\right)}\tag{3}
$$

where U is de<sup>fi</sup>ned as the utility of the new product measured in dollars in the ith segment, Γ is a piecewise function which satis<sup>fi</sup>es

$$
\Gamma (U, p) = \left\{ \begin{array}{c l} e ^ {\mu (U - p)} & \text { if } U - p \geq 0 \\ 0 & \text { otherwise } \end{array} \right.\tag{4}
$$

Eq. (3) implies that if $U - p { < } 0 ,$ , a consumer will not purchase a product; otherwise, the possibility of purchasing the product follows the MNL choice rule.

A comparison among deterministic choice rule, MNL choice rule, and the proposed choice rule is depicted in Fig. 1. Under the deterministic rule, the choice probability equals one only if utility is larger than $U ^ { * }$ (the maximal utility of all competitive products). Under the MNL rule, every possible utility value corresponds to a choice probability and the curve is continuous, whereas in the proposed choice rule, the probability curve can be divided into two parts: a line if $U ^ { * }$ is smaller than p and an MNL curve if $U ^ { * }$ is equal or larger than p.

## 3.5. Expected profit

The expected number of customers purchasing the new product can be described as

$$
Q = \sum_ {i = 1} ^ {I} Q _ {i} P _ {i}\tag{5}
$$

and the expected pro<sup>fi</sup>t from the new product can be formulated as

$$
\Pi = Q (p - C ^ {\text { var }}) - C ^ {\text { fix }}\tag{6}
$$

where $C ^ { \mathrm { f i x } }$ is the <sup>fi</sup>xed cost relevant to the new product development, such as project setup, administrative, and <sup>fi</sup>xed investment costs (e.g., special tools/equipments); and $C ^ { \mathrm { v a r } }$ is the unit variable cost to produce the new product (e.g., component purchasing cost). $C ^ { \mathrm { v a r } }$ is related to the determination of levels of attributes of the new product; hence, $C ^ { \mathrm { v a r } }$ is also a variable based on the decision variable $x _ { k l } .$ By following the linear-additive cost model of Green and Krieger [17], the unit variable cost can be further formulated as follows:

$$
C ^ {\text { var }} = \sum_ {k = 1} ^ {K} \sum_ {l = 1} ^ {L _ {k}} c _ {k l} ^ {\text { var }} x _ {k l}\tag{7}
$$

where $c _ { k l } ^ { \mathrm { v a r } }$ is the unit cost for the lth level of kth attributes and can be estimated by applying the conjoint analysis method on the basis of a cost survey of product pro<sup>fi</sup>les [27].

![](/api/attachments/9VYGMRU2/fulltext/images/6a09aa6ae25c85a43628d8464971811033525dc4f64802c9d75d86843716f30c.jpg)  
Fig. 1. The relationship between utility value and choice probability.

## 3.6. Optimization model

By combining Eqs. (1) to (7), the problem can be formulated as an optimization model as follows:

$$
\Pi = \sum_ {i = 1} ^ {I} Q _ {i} \frac {\Gamma (U _ {i} , p)}{\Gamma (U _ {i} , p) + \sum_ {j = 1} ^ {N} \Gamma (U _ {i j} , p _ {j})} (p - C ^ {\text { var }}) - C ^ {\text { fix }}\tag{8}
$$

subject to

$$
\sum_ {l = 1} ^ {L _ {k}} x _ {k l} = 1, k = 1, 2, \dots , K\tag{9}
$$

$$
U _ {i} = \sum_ {k = 1} ^ {K} \sum_ {l = 1} ^ {L _ {k}} u _ {i k l} x _ {k l}, i = 1, 2,..., I\tag{10}
$$

$$
C ^ {\text { var }} = \sum_ {k = 1} ^ {K} \sum_ {l = 1} ^ {L _ {k}} c _ {k l} ^ {\text { var }} x _ {k l}, i = 1, 2,..., I\tag{11}
$$

$$
x _ {k l} = 0 \text { or } 1, k = 1, 2,..., K, l = 1, 2,... L _ {k}; p > 0
$$

where Constraint (9) ensures that only one level for each product attribute can be selected. $C ^ { f i x }$ is a constant in the model; hence, the objective function (8) is the same as the following objective function:

$$
\text { Max } \Pi = \sum_ {i = 1} ^ {I} Q _ {i} \frac {\Gamma (U _ {i} , p)}{\Gamma (U _ {i} , p) + \sum_ {j = 1} ^ {N} \Gamma \left(U _ {i j} , p _ {j}\right)} \left(p - C ^ {\text { var }}\right)\tag{12}
$$

Let $U _ { i } ^ { C } = \sum _ { j = 1 } ^ { N } { \cal { T } } \Big ( U _ { i j } , p _ { j } \Big )$ where N, $U _ { i j } ,$ and $p _ { j }$ are all given constants; Eq. (12) can be rewritten in a simpler form as follows:

$$
\Pi = \sum_ {i = 1} ^ {I} Q _ {i} \frac {\Gamma (U _ {i} , p)}{\Gamma (U _ {i} , p) + U _ {i} ^ {C}} \left(p - C ^ {\text { var }}\right)\tag{13}
$$

## 4. Solving the optimization model

The optimization model described in Section 3 is a nonlinear model and has a number of discrete decision variables $\left( x _ { k l } \right)$ as well as a continuous decision variable (p). The model can be regarded as an aggregate of product con<sup>fi</sup>guration (to determine the optimal levels of product attributes) and product pricing (to determine the optimal price). We propose an interval-analysis-based enumeration method for small-scale problems in Section 4.1, and an intervalanalysis-embedded TS algorithm for large-scale problems in Section 4.2.

## 4.1. Interval-analysis-based enumeration method for small-scale problems

If the problem scale is small, all combinations of the attribute levels can be enumerated within a tolerable computation time. Suppose that in the abovementioned optimization model, all the discrete decision variables $x _ { k l }$ are already given by the enumeration <sup>fl</sup>ow, the model is then degraded to a one-dimensional optimization model as follows:

$$
\text { Max } \Pi (p) = \sum_ {i = 1} ^ {I} Q _ {i} \frac {\Gamma (U _ {i} , p)}{\Gamma (U _ {i} , p) + U _ {i} ^ {C}} \left(p - C ^ {\text { var }}\right)\tag{14}
$$

where the only decision variable is the continuous variable $p .$ Therefore, if the con<sup>fi</sup>guration of a product pro<sup>fi</sup>le is already given, the optimization problem is then degraded to obtain the optimal price with the objective of maximizing the expected pro<sup>fi</sup>t.

One can see from Eq. (14) that, if the product price increases, the marginal pro<sup>fi</sup>t for a product will increase, hence the expected pro<sup>fi</sup>t may be improved. However, increasing price may lead to losing some consumers, thereby reducing market share. Therefore, a compromised price needs to be determined.

In the following section, we <sup>fi</sup>rst analyze the properties of the pro<sup>fi</sup>tmaximizing model in an unpartitioned product market in Section 4.1.1, and then discuss the characteristics of a model in a multi-segment product market. Finally, we propose a solution algorithm in Section 4.1.2.

## 4.1.1. Unpartitioned product market

In an unpartitioned product market, all consumers are assumed to have similar product preferences. This sounds unrealistic, but it was actually used as an assumption in the models of some studies related to product positioning such as that of Chen and Hausman [8]. Following this assumption, we consider the total number of market segments as one in Eq. (14); hence the model can be simpli<sup>fi</sup>ed as

$$
\text { Max } \Pi (p) = Q _ {1} \frac {\Gamma (U _ {1} , p)}{\Gamma (U _ {1} , p) + U _ {1} ^ {C}} \left(p - C ^ {\text { var }}\right), \quad p > 0\tag{15}
$$

If the price is higher than the utility $\left( p > U _ { 1 } \right)$ , no consumer will purchase the product (Γ $( U _ { 1 } , \ p ) = 0 )$ and the pro<sup>fi</sup>t will be zero. Hence, Eq. (15) can be further simpli<sup>fi</sup>ed as

$$
\text { Max } \Pi (p) = Q _ {1} \frac {e ^ {\mu (U _ {1} - p)}}{e ^ {\mu (U _ {1} - p)} + U _ {1} ^ {C}} (p - C ^ {\text { var }}), U _ {1} > p > 0\tag{16}
$$

Theorem 1. A local optimal solution for Eq. (16) is a global optimal solution.

## Proof. See Appendix A.

Theorem 1 shows that the objective function of the model is unimodal. Hence many traditional nonlinear programming algorithms can be used to solve this model, such as golden section search, Newton' method, and Fibonacci algorithm [31].

## 4.1.2. Multi-segment market

In practical scenarios, consumers may have different purchasing behavior or preferences, hence models supporting multi-segment market are more appropriate. A popular approach for grouping consumers with similar purchasing preferences into segments is clustering analysis [30,39].

According to Eq. (14), the total pro<sup>fi</sup>t of a <sup>fi</sup>rm is the aggregate of pro<sup>fi</sup>ts of all market segments. Although the pro<sup>fi</sup>t function of each segment is a unimodal function as proved in Theorem 1, the aggregate of a set of unimodal function is not necessarily unimodal. Fig. 2 shows an example of a pro<sup>fi</sup>t function with three market segments. Green curve $( \Pi ^ { \bar { 1 } } \left( p \right) )$ , red curve $( \Pi ^ { 2 } \left( p \right) )$ and blue curve $( \Pi ^ { 3 } ( \bar { p } ) )$ represent the expected pro<sup>fi</sup>t of the <sup>fi</sup>rst, second, and third market segment, respectively. If $p { < } C ^ { \mathrm { v a r } }$ , the total pro<sup>fi</sup>t Π will be negative; hence the optimal price is located in this region; if $p { > } U _ { i } \ ( i { = } 1 ,$ , 2, 3), the pro<sup>fi</sup>t for the ith segment $( \Pi ^ { i } \left( p \right) )$ is zero due to the piecewise function Γ. Therefore, the effective section of Π<sup>i</sup> (p) is con<sup>fi</sup>ned within $[ C ^ { \mathrm { v a r } } , U _ { i } ] .$ . The function Π (p) is an aggregate of $\Pi ^ { 1 } ( p ) , \Pi ^ { 2 } ( p )$ , and $\Pi ^ { 3 }$ (p). Π (p) appears as a piecewise function and can be divided into the following segments: 1) $p { < } C ^ { \mathrm { v a r } } ; ~ 2 ) ~ C ^ { \mathrm { v a r } } { \leq } p { < } U _ { 3 } ; ~ 3 ) ~ U _ { 3 } { \leq } p { < } U _ { 2 } ; ~ 4 )$ $U _ { 2 } \leq p < U _ { 1 } ; ~ 5 ) ~ p \geq U _ { 1 } .$ . Apparently, Π (p) is negative in Segment 1 and zero in Segment $5 ,$ , and the optimal solution is within one of the Segments 2, 3 and 4.

Although the model described in Eq. (14) is mathematically complex, some global optimization methods, such as interval analysis [19] or Lipschitz optimization [21], can be applied to solve this onedimensional model. We develop a bi-search algorithm based on interval analysis (BS-IA) to determine the optimal price.

The main procedure of the BS-IA is given in Appendix B. In BS-IA, interval analysis is applied to calculate the lower and upper bounds for the objective function, the <sup>fi</sup>rst and the second derivative of the function. The interval bound information is used in the bi-search with pruning strategy to cut off the fruitless sections of the feasible variable region. The interval functions involved in the BS-IA are computed according to interval arithmetic operations and functions [20].

## 4.2. Interval-analysis-embedded Tabu Search (IAE-TS) for large-scale problems

If the scale of optimization problem is large, enumeration of the combinations of the product attribute levels will lead to a combination explosion. In this case, a meta-heuristic algorithm is a good option to achieve near-optimal solutions for the model.

Introduced by Glover [12,13], Tabu Search is a heuristic procedure designed to guide a search through the trap of local optimal solutions. It has been proved as an ef<sup>fi</sup>cient meta-heuristic algorithm that has simple computation and robust search abilities for complex combinatorial optimization problems [14].

We propose an interval-analysis-embedded Tabu Search (IAE-TS) algorithm to solve the proposed optimization model for a large-scale problem. The fundamentals of tabu search can be found in the works of Glover [12,13]. The main characteristics of the proposed IAE-TS are described in the following sub-sections.

## 4.2.1. Basic idea of IAE-TS

The basic idea of the proposed IAE-TS is somewhat similar to that of the linear programming-embedded simulated annealing algorithm [42]. Given that there is only one continuous variable p and p is highly related to the discrete variables $x _ { k l } ,$ we only process the discrete variables $x _ { k l }$ in Tabu Search and use the interval-analysis-based algorithm described in Section 4.1.2 to determine the optimal value of p and the maximal pro<sup>fi</sup>t for the given setting of discrete variables.

## 4.2.2. Main procedure of IAE-TS

The main steps of the proposed IAE-TS are given in Appendix C.

## 4.2.3. Neighborhood structure

An integer coding is used to represent the status of the level selection of product attributes. $\operatorname { L e t } x = [ x _ { 1 } , x _ { 2 } , . . . , x _ { k } , . . . , x _ { K } ]$ be a solution of new product positioning, where x<sub>k</sub> is an integer variable denoting that the $x _ { k } { \mathrm { t h } }$ level of the kth product attribute is selected for the new product. The optimal price p and the objective function value denoted by f (x) can be calculated using the interval-analysis-based algorithm described in Section 4.1.2. A move in IAE-TS is a shift from a solution to its neighbor, where a neighbor of x can be obtained by increasing or decreasing one of $x _ { k }$ in x on the condition that the increased or decreased $x _ { k }$ is within the range of attribute levels. The set of neighbors of x forms the neighborhood of x denoted by N (x), and the maximal size of the neighborhood is 2K.

![](/api/attachments/9VYGMRU2/fulltext/images/d0ad81bb35498b50b4189c71e34d41d8c1a5e3389d32459409bb8f8652586809.jpg)  
Fig. 2. An example of the pro<sup>fi</sup>t function Π(p).

For example, a solution $x = [ 3 , 1 , 5 ]$ represents that the third, <sup>fi</sup>rst, and <sup>fi</sup>fth levels are selected for the <sup>fi</sup>rst, second, and third product attribute, respectively. The neighborhood $N ( x ) = \{ [ 2 , 1 , 5 ] , [ 4 , 1 , 5 ] , [ 3 , 2 , 5 ]$ [3,1,4],[3,1,6]} and the size of $N \left( x \right)$ is <sup>fi</sup>ve.

## 4.2.4. Adaptive control of tabu list size

If the size of a tabu list is small, the search is not constrained too much by the tabu list and thus has a good diversi<sup>fi</sup>cation capability but the possibility of search cycles increases. If the size of a tabu list is large, the search is capable of avoiding cycles but may lose some good solutions in neighborhood. In the present research, a simple approach proposed by Battiti and Tecchiolli [4] is applied to adaptively control the size of the tabu list. The basic idea is to use a hash table to record the visited solutions and detect possible cycles: if a solution has been visited, the size of the tabu list is gradually increased; if a solution is visited repeatedly, the search jumps to another solution and restarts the tabu search process. On the other hand, if the search continuously explores new solutions, the size of the tabu list is gradually decreased. Steps 8, 9, and 10 in Section 4.2.2 present the control <sup>fl</sup>ow of this approach.

## 4.2.5. Jump mechanism

When the search jumps to a new start point as indicated in Steps 3 and 9 in Section 4.2.2, we employ the following method to <sup>fi</sup>nd the new start point and keep the search more diversi<sup>fi</sup>ed. First, randomly generate a number of solutions as the possible solution seeds; then select the solution with the largest distance from the last used solution, i.e.,

$$
i d x = \arg \max \sum_ {k = 1} ^ {K} \left(x _ {k} ^ {i} - x _ {k}\right) ^ {2}, i = 1, 2, \dots , N ^ {\text { Seed }}\tag{17}
$$

where x<sup>i</sup> is the kth element of the ith generated solution, and idx is the index number of the selected solution in the generated N<sup>Seed</sup> solutions.

## 4.2.6. Aspiration level check

Given that the tabu list can sometimes be too restrictive (good moves are forbidden), aspiration level check can be applied to override the tabu status for these moves. We employ the simplest and most frequently used aspiration criterion to accept a tabu move, for example, if a move leads to a new solution better than the current best, then it is accepted even if it is in tabu list. Step 5 in Section 4.2.2 presents the aspiration level check.

## 5. Case studies

All algorithms implemented in the case studies were coded in the programming language Visual C++ and ran on a laptop computer (2 GB RAM, 1.86 GHz CPU using Windows 7).

## 5.1. Application

The proposed optimization model and algorithms were applied to the product positioning of digital cameras. A list of product attributes of digital cameras and their levels are shown in Table 1.

To reduce the complexity of the market survey and avoid possible combination explosion [24], Taguchi Orthogonal Array Selector provided in the SPSS software package (www.spss.com) was applied to de<sup>fi</sup>ne a number of orthogonal product pro<sup>fi</sup>les. Table 2 shows the generated L16 orthogonal product pro<sup>fi</sup>les array for conducting the market survey. A cell marked with “1” indicates that the corresponding level of an attribute (in column) has been selected for the corresponding product pro-<sup>fi</sup>le (in row) whereas a cell with “0” means that it has not been selected.

A market survey based on the de<sup>fi</sup>ned L16 product pro<sup>fi</sup>les was conducted to collect customers' preferences on these product pro<sup>fi</sup>les. Thirty-<sup>fi</sup>ve users of digital cameras were invited to rank each product pro<sup>fi</sup>le by giving a perceived utility value measured in HK dollars. The simplest way for market segmentation is regarding each invited user as a market segment, but the complexity of the optimization model will increase greatly. We applied the clustering analysis function in SPSS software to group these thirty-<sup>fi</sup>ve ranking data sets (each contains ranking values for sixteen product pro<sup>fi</sup>les) into three clusters, each cluster represents a market segment in which some users with similar preference are classi<sup>fi</sup>ed. We consider the center of a cluster as the representative ranking data for this market segment and the <sup>fi</sup>nal cluster centers of the segments output by SPSS are shown in Table 3. The sizes of the three segments are estimated by marketing department of the company as 61,000, 33,000, and 42,000, respectively, and the estimated <sup>fi</sup>xed cost is HK\$3.8 million.

Based on the information shown in Tables 1, 2 and 3, least-square linear regression in SPSS software was applied to estimate the partworth utility of each level of attributes in the three market segments. The results of the regressions are shown in Table 4.

The variable unit cost of digital cameras based on the 16 product pro-<sup>fi</sup>les were estimated by the product development team of the company. The estimates are listed in the last column of Table 3. By using regression calculation similar to that of part-worth utility estimation, the variable unit costs of all levels of attributes were determined, as shown in Table 5. The con<sup>fi</sup>gurations and prices of the major competitors' products are shown in Table 6. The scaling parameter of the probability is calibrated as 0.5.

Since the number of the level combinations is only $2 ^ { 6 } \times 4 ^ { 2 } = 1 0 2 4 ,$ the case can be considered a small-scale problem. Therefore, the intervalanalysis-based enumeration method described in Section 4.1 was applied to solve the problem. The obtained optimal solution $\scriptstyle ( \varepsilon = 0 . 0 1 )$ includes the following: selecting the product pro<sup>fi</sup>le with ConFig. 1 (Pixel: 10; Anti-shock: Y; Screen: 3.0; Battery: Lith; Face dete: N; Mode: 18; Weight: 140–160; Zoom: 9); product price at HK\$593; and maximal expected pro<sup>fi</sup>t of HK\$10.06 million. The computation time is 1.96 s.

If we do not consider the negative utility effect and replace the right of Eq. (4) with $e ^ { \mu ( U - p ) } ,$ which represents the traditional MNL rule, the obtained optimal product pro<sup>fi</sup>le is ConFig. 2 (Pixel: 10; Anti-shock: Y; Screen: 3.0; Battery: AA; Face dete.: N; Mode: 18; Weight: 140–160;

Product attributes and attribute levels of digital cameras.

<table><tr><td>Index</td><td>Attribute name</td><td>Attribute levels</td></tr><tr><td>1</td><td>Mega pixel (million)</td><td>7; 10</td></tr><tr><td>2</td><td>Anti-shock functions</td><td>No; yes</td></tr><tr><td>3</td><td>Screen size (cm)</td><td>2.5; 3</td></tr><tr><td>4</td><td>Battery</td><td>AA battery; lithium battery</td></tr><tr><td>5</td><td>Face detection</td><td>No; yes</td></tr><tr><td>6</td><td>Number of shooting modes</td><td>12; 18</td></tr><tr><td>7</td><td>Weight (grams)</td><td>100–120; 120–140; 140–160; 160–180</td></tr><tr><td>8</td><td>Optical zoom</td><td>3, 5, 7, 9</td></tr></table>

Table 2  
Orthogonal product pro<sup>fi</sup>les of digital cameras.

<table><tr><td rowspan="2">Profile</td><td colspan="2">Pixel</td><td colspan="2">Antishock</td><td colspan="2">Screen</td><td colspan="2">Battery</td><td colspan="2">Face dete.</td><td colspan="2">Mode</td><td colspan="4">Weight</td><td colspan="4">Zoom</td></tr><tr><td>7</td><td>10</td><td>N</td><td>Y</td><td>2.5</td><td>3.0</td><td>AA</td><td>Lith</td><td>N</td><td>Y</td><td>12</td><td>18</td><td>100-120</td><td>120-140</td><td>140-160</td><td>160-180</td><td>3</td><td>5</td><td>7</td><td>9</td></tr><tr><td>1</td><td>1</td><td>0</td><td>1</td><td>0</td><td>1</td><td>0</td><td>1</td><td>0</td><td>1</td><td>0</td><td>1</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td></tr><tr><td>2</td><td>0</td><td>1</td><td>0</td><td>1</td><td>1</td><td>0</td><td>0</td><td>1</td><td>1</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td></tr><tr><td>3</td><td>1</td><td>0</td><td>0</td><td>1</td><td>0</td><td>1</td><td>0</td><td>1</td><td>0</td><td>1</td><td>1</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td></tr><tr><td>4</td><td>0</td><td>1</td><td>1</td><td>0</td><td>0</td><td>1</td><td>1</td><td>0</td><td>0</td><td>1</td><td>0</td><td>1</td><td>0</td><td>0</td><td>1</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td></tr><tr><td>5</td><td>1</td><td>0</td><td>1</td><td>0</td><td>0</td><td>1</td><td>0</td><td>1</td><td>0</td><td>1</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td>1</td></tr><tr><td>6</td><td>0</td><td>1</td><td>0</td><td>1</td><td>0</td><td>1</td><td>1</td><td>0</td><td>0</td><td>1</td><td>1</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td></tr><tr><td>7</td><td>1</td><td>0</td><td>0</td><td>1</td><td>1</td><td>0</td><td>1</td><td>0</td><td>1</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>1</td><td>0</td><td>0</td></tr><tr><td>8</td><td>0</td><td>1</td><td>1</td><td>0</td><td>1</td><td>0</td><td>0</td><td>1</td><td>1</td><td>0</td><td>1</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td></tr><tr><td>9</td><td>0</td><td>1</td><td>0</td><td>1</td><td>1</td><td>0</td><td>1</td><td>0</td><td>0</td><td>1</td><td>0</td><td>1</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td></tr><tr><td>10</td><td>1</td><td>0</td><td>1</td><td>0</td><td>1</td><td>0</td><td>0</td><td>1</td><td>0</td><td>1</td><td>1</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td></tr><tr><td>11</td><td>0</td><td>1</td><td>1</td><td>0</td><td>0</td><td>1</td><td>0</td><td>1</td><td>1</td><td>0</td><td>0</td><td>1</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td></tr><tr><td>12</td><td>1</td><td>0</td><td>0</td><td>1</td><td>0</td><td>1</td><td>1</td><td>0</td><td>1</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td></tr><tr><td>13</td><td>0</td><td>1</td><td>0</td><td>1</td><td>0</td><td>1</td><td>0</td><td>1</td><td>1</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>1</td><td>0</td><td>0</td><td>0</td></tr><tr><td>14</td><td>1</td><td>0</td><td>1</td><td>0</td><td>0</td><td>1</td><td>1</td><td>0</td><td>1</td><td>0</td><td>0</td><td>1</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td></tr><tr><td>15</td><td>0</td><td>1</td><td>1</td><td>0</td><td>1</td><td>0</td><td>1</td><td>0</td><td>0</td><td>1</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td><td>1</td><td>0</td></tr><tr><td>16</td><td>1</td><td>0</td><td>0</td><td>1</td><td>1</td><td>0</td><td>0</td><td>1</td><td>0</td><td>1</td><td>0</td><td>1</td><td>0</td><td>1</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td></tr></table>

Table 3  
The obtained cluster centers and unit variable cost (HK\$) of the pro<sup>fi</sup>les.

<table><tr><td rowspan="2">Profile</td><td colspan="3">Perceived utility</td><td rowspan="2">Estimated unit variable cost</td></tr><tr><td>Cluster1</td><td>Cluster 2</td><td>Cluster 3</td></tr><tr><td>1</td><td>386</td><td>188</td><td>620</td><td>120</td></tr><tr><td>2</td><td>600</td><td>750</td><td>740</td><td>220</td></tr><tr><td>3</td><td>571</td><td>688</td><td>760</td><td>300</td></tr><tr><td>4</td><td>514</td><td>325</td><td>640</td><td>180</td></tr><tr><td>5</td><td>643</td><td>575</td><td>660</td><td>270</td></tr><tr><td>6</td><td>614</td><td>625</td><td>620</td><td>250</td></tr><tr><td>7</td><td>571</td><td>413</td><td>620</td><td>135</td></tr><tr><td>8</td><td>586</td><td>475</td><td>680</td><td>240</td></tr><tr><td>9</td><td>786</td><td>563</td><td>720</td><td>350</td></tr><tr><td>10</td><td>400</td><td>413</td><td>620</td><td>170</td></tr><tr><td>11</td><td>543</td><td>500</td><td>620</td><td>230</td></tr><tr><td>12</td><td>614</td><td>450</td><td>620</td><td>180</td></tr><tr><td>13</td><td>414</td><td>550</td><td>680</td><td>160</td></tr><tr><td>14</td><td>471</td><td>313</td><td>600</td><td>150</td></tr><tr><td>15</td><td>400</td><td>350</td><td>600</td><td>130</td></tr><tr><td>16</td><td>500</td><td>663</td><td>620</td><td>290</td></tr></table>

Zoom: 9). A comparison of ConFig. 1 and ConFig. 2 under the two consumer choice rules is shown in Table 7.

A comparison of the dataset in Table 7 shows that the maximal pro<sup>fi</sup>t and optimal price under the proposed choice rule are higher than those under the traditional MNL rule. The reason for this phenomenon is that the values of the Γ function of some competitors' products (Cmp.1 in S1 and S2, Cmp.2 in S2) are reduced to zero under the proposed choice rule; hence, the market share of the new product increases accordingly. Under the traditional MNL rule, those competitors' products with negative utility surplus are still assumed to occupy some market share. As a result, the expected pro<sup>fi</sup>t of the new product is underestimated.

To observe the relationship between the optimal solution and the prices of the competitors' products, an experiment was conducted assuming that the prices of the competitors' products are reduced with a series of discounts. The result is shown in Fig. 3. The optimal price and pro<sup>fi</sup>t decline monotonously with the decrease in the prices of the competitors' products. When the price discount is smaller than 0.4, a negative pro<sup>fi</sup>t of the new product occurs because the low prices of competitors' products increase the choice probabilities of the competitors' products, decrease the market share of the new product, depress the price of the new product, and eventually reduce the expected pro<sup>fi</sup>t.

## 5.2. Experiment for large-scale problems

To evaluate the feasibility of the IAE-TS algorithm described in Section 4.2, we constructed some large-scale product positioning problems with randomly generated data. Part-worth utility is assumed to be U (\$3, \$6),that is, a random number uniformly distributed within HK\$3–6; unit variable cost is assumed to be U (\$1, \$3); product demand in each segment is assumed to be U (1 million, 2 million); ten competitive products are generated by selecting the product attribute levels at random; and the number of market segments and the <sup>fi</sup>xed cost are assumed to be both HK\$5 million. (Note that the ranges and values of some parameters are given in the experiment since random generation may cause large number of infeasible solutions.)

A rule-based method was also programmed to compare with the IAE-TS algorithm. The idea of the rule-based method is to use a heuristic rule to set the values of discrete variables x , and then use the interval-analysis-based algorithm described in Section 4.1.2 to determine the optimal value of p and the overall pro<sup>fi</sup>t. Five-level selection rules for product attribute were applied and listed as follows:

1) R\_MAX\_U: select the level with maximal part-worth utility in all market segments;

2) R\_MAX\_P: select the level with maximal part-worth utility minus part-worth cost in all market segments;

Table 4  
The achieved part-worth utilities of the levels.

<table><tr><td rowspan="2">Market Segm.</td><td colspan="2">Pixel</td><td colspan="2">Antishock</td><td colspan="2">Screen</td><td colspan="2">Battery</td><td colspan="2">Face dete.</td><td colspan="2">Mode</td><td colspan="4">Weight</td><td colspan="4">Zoom</td><td rowspan="2">Regr. const.</td></tr><tr><td>7</td><td>10</td><td>N</td><td>Y</td><td>2.5</td><td>3.0</td><td>AA</td><td>Lith</td><td>N</td><td>Y</td><td>12</td><td>18</td><td>100-120</td><td>120-140</td><td>140-160</td><td>160-180</td><td>3</td><td>5</td><td>7</td><td>9</td></tr><tr><td>S1</td><td>0</td><td>38</td><td>0</td><td>91</td><td>0</td><td>19</td><td>0</td><td>-12</td><td>0</td><td>30</td><td>0</td><td>80</td><td>0</td><td>-29</td><td>-40</td><td>-65</td><td>0</td><td>79</td><td>57</td><td>204</td><td>364</td></tr><tr><td>S2</td><td>0</td><td>54</td><td>0</td><td>195</td><td>0</td><td>26</td><td>0</td><td>173</td><td>0</td><td>70</td><td>0</td><td>45</td><td>0</td><td>34</td><td>0</td><td>-13</td><td>0</td><td>56</td><td>94</td><td>84</td><td>144</td></tr><tr><td>S3</td><td>0</td><td>23</td><td>0</td><td>43</td><td>0</td><td>-3</td><td>0</td><td>43</td><td>0</td><td>8</td><td>0</td><td>3</td><td>0</td><td>-50</td><td>-25</td><td>-40</td><td>0</td><td>-20</td><td>35</td><td>30</td><td>611</td></tr></table>

Table 5  
Unit cost of levels of the digital camera.

<table><tr><td rowspan="2">Attributes</td><td colspan="2">Pixel</td><td colspan="2">Antishock</td><td colspan="2">Screen</td><td colspan="2">Battery</td><td colspan="2">Face dete.</td><td colspan="2">Mode</td><td colspan="4">Weight</td><td colspan="4">Zoom</td><td rowspan="2">Regr. const.</td></tr><tr><td>7</td><td>10</td><td>N</td><td>Y</td><td>2.5</td><td>3.0</td><td>AA</td><td>Lith</td><td>N</td><td>Y</td><td>12</td><td>18</td><td>100-120</td><td>120-140</td><td>140-160</td><td>160-180</td><td>3</td><td>5</td><td>7</td><td>9</td></tr><tr><td>Variable unit cost</td><td>0</td><td>18.1</td><td>0</td><td>49.4</td><td>0</td><td>8.1</td><td>0</td><td>48.1</td><td>0</td><td>63.1</td><td>0</td><td>34.4</td><td>0</td><td>-17.5</td><td>-62.5</td><td>-76.3</td><td>0</td><td>8.7</td><td>12.5</td><td>72.5</td><td>116</td></tr></table>

Table 6  
Product pro<sup>fi</sup>les and prices of the competitor's products.

<table><tr><td rowspan="2">Profile</td><td colspan="2">Pixel</td><td colspan="2">Antishock</td><td colspan="2">Screen</td><td colspan="2">Battery</td><td colspan="2">Face dete.</td><td colspan="2">Mode</td><td colspan="4">Weight</td><td colspan="4">Zoom</td><td rowspan="2">Price</td></tr><tr><td>7</td><td>10</td><td>N</td><td>Y</td><td>2.5</td><td>3.0</td><td>AA</td><td>Lith</td><td>N</td><td>Y</td><td>12</td><td>18</td><td>100-120</td><td>120-140</td><td>140-160</td><td>160-180</td><td>3</td><td>5</td><td>7</td><td>9</td></tr><tr><td>Cmp. 1</td><td>0</td><td>1</td><td>1</td><td>0</td><td>1</td><td>0</td><td>0</td><td>1</td><td>1</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td>410</td></tr><tr><td>Cmp. 2</td><td>1</td><td>0</td><td>0</td><td>1</td><td>0</td><td>1</td><td>1</td><td>0</td><td>0</td><td>1</td><td>1</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td>470</td></tr><tr><td>Cmp. 3</td><td>0</td><td>1</td><td>0</td><td>1</td><td>0</td><td>1</td><td>0</td><td>1</td><td>0</td><td>1</td><td>0</td><td>1</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>580</td></tr></table>

3) R\_MAX\_AVG\_U: select the level with maximal average (part-worth utility) in all market segments;

4) R\_MAX\_AVG\_P: select the level with maximal average (part-worth utility minus part-worth cost) in all market segments; and

5) R\_MIN\_C: select the level with minimal part-worth cost.

The running result of the experiment is shown in Fig. 4. Given that many random variables are involved in the algorithms, we ran the algorithms ten times and obtained the average values. The number of trials of the IAE\_TS was set as 1000 in the experiment, while a trial was de-<sup>fi</sup>ned as a call to the interval-analysis-based procedure in Section 4.1.2.

As shown in Fig. 4, the performance of the IAE\_TS is better than the rule-based method under the <sup>fi</sup>ve abovementioned heuristic rules. The average running time of a rule-based method is 4 ms. The average running time of the IAE\_TS (1000 trials) is 3.87 s, which is still tolerable in engineering applications.

## 6. Conclusions

Based on the discussions made in the present paper, the following points are summarized and concluded:

1) A conjoint analysis-based one-step optimization model for product positioning is established that considers the negative utility effect on consumer choice rule. Consumer choice rule is then formulated as a piecewise function based on dollar-scaled utility and multinomial logit rule.

2) To analyze the proposed model, the discrete decision variables are isolated and a pro<sup>fi</sup>t-maximizing sub-model is formulated. Interval analysis is applied to obtain the optimal price and maximal expected pro<sup>fi</sup>t for the sub-model. The objective function of the sub-model in an unpartitioned product market has been proved unimodal; hence, many ef<sup>fi</sup>cient nonlinear programming algorithms can be directly applied. The application of digital cameras shows that the proposed interval-analysis-based enumeration method is effective in obtaining global optimal solutions.

![](/api/attachments/9VYGMRU2/fulltext/images/d9ac92a588b804679b539f93e3a5e13619c6479ccbc02ba1ff43bf7203a226fa.jpg)

![](/api/attachments/9VYGMRU2/fulltext/images/95e52f5b05c9970132924613c4d42215c86731b3a65209192dcf2aaa2e6e18ac.jpg)  
Fig. 3. Optimal prices and pro<sup>fi</sup>ts with different price discounts of competitive products.

3) An interval-analysis-embedded TS algorithm is developed to solve the proposed model with a number of large-scale parameters. An experiment for randomly created large-scale product positioning problems shows that the algorithm has better performance than the rule-based approach. The computation time is longer but still tolerable for engineering applications.

Further work may extend our research to product line positioning problems. Product line positioning involves more decision variables given that each product pro<sup>fi</sup>le has its own level settings for product attributes. The price of each product in the product line, in particular, is required to determine whether the objective function maximizes the pro<sup>fi</sup>ts. Therefore, the interval-analysis algorithm in this research may not be applicable because it presents many continuous variables that may deteriorate the performance of global optimal search. An extended optimization model needs to be established and a hybrid heuristic search may be developed to solve product line positioning problems.

Table 7  
ConFig.1 and ConFig.2 under the two consumer choice rules

<table><tr><td rowspan="3"></td><td colspan="5">Under traditional MNL rule</td><td colspan="5">Under the proposed rule</td></tr><tr><td colspan="3">Choice probability</td><td rowspan="2">Optimal price ($)</td><td rowspan="2">Maximal profit (m$)</td><td colspan="3">Choice probability</td><td rowspan="2">Optimal price ($)</td><td rowspan="2">Maximal profit (m$)</td></tr><tr><td>S1</td><td>S2</td><td>S3</td><td>S1</td><td>S2</td><td>S3</td></tr><tr><td>ConFig.1</td><td>0.34</td><td>0.33</td><td>0.22</td><td>574</td><td>8.05</td><td>0.36</td><td>0.43</td><td>0.21</td><td>593</td><td>10.06</td></tr><tr><td>ConFig.2</td><td>0.40</td><td>0.20</td><td>0.22</td><td>533</td><td>8.20</td><td>0.43</td><td>0.29</td><td>0.21</td><td>546</td><td>10.01</td></tr></table>

(a)  
![](/api/attachments/9VYGMRU2/fulltext/images/ee1d90017c7f4a3426c4c31dcea98cc0cdf001bb57f9dc1a57f891738bd810dc.jpg)

(b)  
![](/api/attachments/9VYGMRU2/fulltext/images/87dfd0276267433696267ec1f3784956b72b0fba625ca0f5e539fd83de469848.jpg)

(c)  
![](/api/attachments/9VYGMRU2/fulltext/images/8389272d200334fb88d035bf56d461d0d5b157e816edd4afb1a4f16c37efbd4d.jpg)  
Fig. 4. The optimal pro<sup>fi</sup>ts obtained by IAE\_TS and the rule-based approaches.

## Acknowledgments

This research was <sup>fi</sup>nancially supported by the National Science Foundation of China (NSFC Proj. 71171039, 70871020 and 71021061) and the Fundamental Research Funds for Central Universities (Proj. N110204005). The work described in this paper was supported by a grant from the Hong Kong Polytechnic University (Project No. G-YJ09).

## Appendix A. Proof of Theorem 1

Proof. Proof by contradiction. Assume that there is more than one local optimal solution. Arbitrarily select two local optimal solutions, denote the solution with the smaller value as p and the other one as p .

The derivative of Π (p) in Eq. (16) is

$$
\begin{array}{l} \Pi^ {\prime} (p) = \left[ \frac {Q _ {1} (p - C ^ {\text { var }}) e ^ {\mu (U _ {1} - p)}}{e ^ {\mu (U _ {1} - p)} + U _ {1} ^ {C}} \right] ^ {\prime} \\ = Q _ {1} e ^ {\mu U _ {1}} \frac {e ^ {\mu U _ {1}} + U _ {1} ^ {C} e ^ {\mu p} [ 1 - (p - C ^ {\text { var }}) \mu ]}{(e ^ {\mu U _ {1}} + U _ {1} ^ {C} e ^ {\mu p}) ^ {2}}. \end{array}\tag{A.1}
$$

As a local optimum, $p _ { 1 }$ satis<sup>fi</sup>es $\dot { \cal I } \dot { \cal ( p _ { 1 } ) } = 0 $ . Thus, we have

$$
e ^ {\mu U _ {1}} + U _ {1} ^ {C} e ^ {\mu p _ {1}} \left[ 1 - (p _ {1} - C ^ {\text { var }}) \mu \right] = 0\tag{A.2}
$$

Similarly, $p _ { 2 }$ also satis<sup>fi</sup>es $\dot { \cal I } \dot { \cal ( p _ { 2 } ) } = 0$ We have

$$
e ^ {\mu U _ {1}} + U _ {1} ^ {C} e ^ {\mu p _ {2}} \left[ 1 - (p _ {2} - C ^ {\text { var }}) \mu \right] = 0\tag{A.3}
$$

Let $\Delta p = p _ { 2 } - p _ { 1 } ;$ the left part of Eq. (A.3) can then be rewritten as

$$
e \mu U _ {1} + U _ {1} ^ {C} e ^ {\mu (p _ {1} + \Delta p)} [ 1 - (p _ {1} + \Delta p - C ^ {\text { var }}) \mu ] = e ^ {\mu U _ {1}} (1 - e ^ {\mu \Delta p})\tag{A.4}
$$

$$
+ e ^ {\mu \Delta p} \left\{e ^ {\mu U _ {1}} + U _ {1} ^ {C} e ^ {\mu p _ {1}} \left[ 1 - (p _ {1} - C ^ {\text { var }}) \mu \right] \right\} - \mu \Delta p U _ {1} ^ {C} e ^ {\mu \Delta p} e ^ {\mu p _ {1}}
$$

Based on Eq. (A.2), the expression inside the brace of Eq. (A.4) equals to zero. Therefore, the left part of Eq. (A.3) can be further rewritten as

$$
e ^ {\mu U _ {1}} + U _ {1} ^ {C} e ^ {\mu p _ {2}} \left[ 1 - \left(p _ {2} - C ^ {\text { var }}\right) \mu \right] = e ^ {\mu U _ {1}} \left(1 - e ^ {\mu \Delta p}\right) - \mu \Delta p U _ {1} ^ {C} e ^ {\mu \Delta p} e ^ {\mu p _ {1}}\tag{A.5}
$$

According to the premise $p _ { 1 } { < } p _ { 2 } , \Delta p$ must be positive. On the other hand, μ and U<sup>C</sup> are both positive parameters. Therefore, the right part of Eq. (A.5) must be negative, that is,

$$
e ^ {\mu U _ {1}} + U _ {1} ^ {C} e ^ {\mu p _ {2}} \left[ 1 - (p _ {2} - C ^ {\text { var }}) \mu \right] <   0\tag{A.6}
$$

However, this contradicts Eq. (A.3). Thus, we have a contradiction.

## Appendix B. Steps of the BS-IA

The main procedure of the BS-TS is explained as follows:

X a set of initial price points;

$S$ a set of intervals;

$x ^ { * }$ the optimal price;

$\Pi ^ { * }$ the maximal expected pro<sup>fi</sup>t;

$\phi$ empty set;

|S| the number of elements in S;

s an interval in S, the lower and upper values of s are denoted as a and b, respectively, that $\mathrm { i } s , s = [ a , b ]$ ;

$\varepsilon$ the computation tolerance;

$L \left( s \right) , U \left( s \right)$ the lower and upper values of interval s, respectively; and $I I , \boldsymbol { \Pi } ^ { " }$ the <sup>fi</sup>rst and second derivative of function Π, respectively;

Step 1: Set $X = \{ C ^ { \mathrm { v a r } } , U _ { 1 } , U _ { 2 } , . . . , U _ { I } \}$ ; compute for the current best solutions with $X ,$ that is, $\Pi ^ { * } = \Pi \mathrm { a x } _ { i = 2 } ^ { I + 1 } I I ( X ( i ) )$ $x ^ { * } =$ $\begin{array} { r } { \{ X ( j ) \vert X ( j ) = \vert \mathrm { m a x } _ { i = 2 } ^ { I + 1 } / I ( X ( i ) ) \} ; } \end{array}$ The purpose of this step is to create the initial price points for further calculation. Since the points in X are possible optimal solution, their objective functions are computed and the best solution is recorded for later comparisons.

Step 2: Arrange X in ascending order; set $S = \{ [ X ( 1 ) , X ( 2 ) ] , [ X ( 2 ) ,$ $X ( 3 ) ] , . . . , [ X ( I ) , X ( I + 1 ) ] \}$ where $[ X ( i ) , X ( i + 1 ) ] ~ ( i { = } 1 , 2 , . . . , I )$ represents an interval ranging from X (i) to X (i+1), and X (i) represents the ith element of X.

In this step, the initial price points are arranged in ascending order, and a group of intervals are formed for interval analysis.

Step 3: $\operatorname { I f } S = \phi ,$ then the algorithm ends, the optimal solution set is $x ^ { * } ;$ otherwise go to the next step. This step controls the loop of the algorithm.

Step 4: $\operatorname { I f } | S | = 1$ and $L ( \varPi ^ { ' } ( S ( 1 ) ) ) { < } 0$ and $U ( \pi ^ { \prime \prime } ( S ( 1 ) ) ) { < } 0$ , then the algorithm ends and standard non-linear algorithms can be used to solve the problem in interval S (1); otherwise go to the next step. This step checks whether there is only one remaining interval $( | S | = 1 )$ , and the function in this interval is convex $( L ( \pi ^ { " } ( S ( 1 ) ) ) { < } 0$ and $U ( \pi ^ { \prime \prime } ( S ( 1 ) ) ) { < } 0$ , that is, the second derivative of the function is always negative in this interval).

Step 5: Select an interval in S and denote it as $s = [ a , b ]$ . The selection strategy could be: maximal function value of the upper endpoint, minimal absolute value of <sup>fi</sup>rst derivative value of lower endpoint, or random selection. Remove s from S. This step heuristically selects an interval in the interval pool for further analysis.

Step 6: If $L ( \varPi ^ { \prime } ( [ a , b ] ) ) ^ { * } U ( \varPi ^ { \prime } ( [ a , b ] ) ) { \leq } 0$ and $U ( H ( [ a , b ] ) ) { \geq } H ^ { * }$ , then set $m = ( a + b ) / 2 ,$ , computer Π (m), set $x ^ { * } = m$ and $\Pi ^ { * } { = } \Pi$ (m) if Π $( m ) { > } \Pi ^ { * }$ , then go to the next step; otherwise go back to Step 3.

In this step, two pruning strategies are applied to cut off the fruitless intervals: if the lower and upper values of $\varPi ^ { ' ( [ a , b ] ) }$ are all positive or negative, the function curve of $\varPi ^ { ' ( [ a , b ] ) }$ is monotonic increasing or decreasing. Therefore, the optimal price is not possible to locate within (a, b). Moreover, the pro<sup>fi</sup>t function values of the endpoints a and b have been computed and compared with ${ \mathbf { x } } ^ { * }$ in the previous steps. Therefore, the interval [a, b] can be ignored if $L ( \varPi ^ { ' } ( [ a , b ] ) ) ^ { * } U ( \varPi ^ { ' } ( [ a , b ] ) ) { \leq } 0 .$ If the upper value of Π([a,b]) is smaller than $\Pi ^ { * }$ , which means that any price points in [a, b] are inferior to the current best solution, [a, b] can also be ignored.

If the interval [a, b] can escape from the abovementioned pruning strategies, this indicates that at least one local optimum exists in [a, b] and that may be the global optimum. The midpoint between a and b is selected as the demarcation point to bisect [a, b] into two smaller intervals. The pro<sup>fi</sup>t function value of this midpoint is computed and compared with the current best solution.

Step 7: If $b - a > \varepsilon ,$ , then append [a, m] and [m, b] into S; go back to Step 3.

This step partitions the interval [a, b] into two new intervals, [a, m] and [m, b], and then update the set of intervals. If the left and right value of the interval is very close (smaller than the given computation tolerance), the algorithm does not attempt to partition the current interval any more.

Note: Step 4 can be omitted if one does not want to integrate other non-linear optimization algorithms. However, if Step 4 is omitted, the algorithm can still perform a bisection search when one interval remains and the function in this interval is convex.

## Appendix C. Steps of the IAE-TS

The main procedure of the proposed IAE-TS is explained as follows:

k, c \_ dec, c \_ esc counter in the loop;

$x$ the solution of the current iteration;

$x ^ { * }$ the best solution so far;

$f ( x )$ objective function of x;

$A \left( x \right)$ aspiration level function of x;

N (x) neighborhood of x;

$T$ Tabu list containing the last accepted moves in reverse order;

size\_T the adaptive size of T to be controlled;

$s i z e \ ( T )$ number of elements currently contained in T; $x _ { N b } ^ { b e s t }$ the best solution in N (x);

$x _ { N h } ^ { n e x t }$ the best solution in N (x) which is not restricted by T; $N ^ { I t e r }$ number of iterations;

$N ^ { S e e d }$ number of randomly generated seed solutions;

$n \_ d e c$ number of iterations triggering a shrink of Tabu list; $n \_ e s c$ number of iterations triggering an escape action;

$\omega ^ { I n } , \omega ^ { D e }$ increase rate and decrease rate of size\_T, respectively;

hash hash table for recording the visited x in iterations.

Step 1: Initialization

Initialize x using random method or rule-based methods and calculate f (x) using the interval-analysis-based algorithm described in Section 4.1.2; initialize hash; set ${ \boldsymbol { x } } ^ { * } = { \boldsymbol { x } } ,$ $f \left( x ^ { \ast } \right) = f \left( x \right) , T = \phi , k = 0 , c _ { - } d e c = 0 , c _ { - } e s c = 0 ;$

Step 2: if $k { < } N ^ { I t e r }$ , go to the next step; otherwise, the algorithm stops;

Step 3: Neighborhood formulation

Add x to hash and set $k = k + 1 ;$ <sup>fi</sup>nd all the neighbors of x and <sup>fi</sup>ll them into $N \left( x \right)$ , and calculate the objective function of each neighbor. If all the solutions in N (x) are restricted by T, go to Step11.

Step 4: Recording the best

Find x<sub>Nb</sub><sup>best</sup> in N (x), set $x ^ { * } = x _ { N b } ^ { b e s t } , f ( x ^ { * } ) = f ( x _ { N b } ^ { b e s t } )$

Step 5: Aspiration level check

$\mathrm { I f } f ( x _ { N b } ^ { b e s t } ) > A ( x )$ , set $\ x = x _ { N b } ^ { b e s t }$ and go back to Step 2.

Step 6: Neighborhood move

Find x<sub>Nb</sub><sup>next</sup> in N (x), set $\boldsymbol { x } = \boldsymbol { x } _ { N b } ^ { n e x t }$

Step 7: Updating Tabu list

Insert the reverse direction of the current move into the head of T. If size (T)>size\_T, remove the size (T)− size\_T elements from the tail of T.

Step 8: Adaptive control of Tabu list size

If x is already in hash, set size ${ \cal T } { = } s i z e _ { - } T ^ { * } \omega ^ { I n } , \ c _ { - } d e c { = } 0 ,$ c\_esc=c\_esc+1 and go to Step 9; otherwise, set c\_dec=c\_dec+1 and go to Step10.

Step 9: if c\_esc = n\_esc, go to Step11.

Step 10: if c\_dec=n\_dec, set size $\scriptstyle - { \cal T } = \operatorname* { m a x } ( 1 , s i z e \_ { \cal T } { } ^ { * } \omega ^ { D e } ) , c \_ d e c = 0$ and go back to Step 2.

Step 11: Jump mechanism

Randomly generate $N ^ { S e e d }$ solutions as seeds, and set x as the one with the largest distance from the last x. Set $c \_ d e c = 0$ c\_esc=0 and go back to Step 2.

## References

[1] M.D. Albritton, P.R. McMullen, Optimal product design using a colony of virtual ants, European Journal of Operational Research 176 (2007) 498–520.

[2] A. Bachem, H. Simon, Product positioning model with costs and prices, European Journal of Operational Research 7 (1981) 362–370.

[3] P.V. Balakrishnan, R. Gupta, V.S. Jacob, Development of hybrid genetic algorithms for product line designs, IEEE Transactions on Systems, Man, and Cybernetics Part B, Cybernetics 34 (2004) 468–483.

[4] R. Battiti, G. Tecchiolli, The reactive tabu search, Journal on Computing 6 (1994) 126–140.

[5] A. Belloni, R.M. Freund, Optimizing product line designs: ef<sup>fi</sup>cient methods and comparisons, Management Science 54 (2008) 1544–1552

[6] M. Ben-Akiva, S. Lerman, Discrete Choice Analysis: Theory and Application to Travel Demand, The MIT Press, Cambridge, MA, 1985.

[7] S.L. Chan, W.H. Ip, A dynamic decision support system to predict the value of customer for new product development, Decision Support Systems 52 (2011) 178–188.

[8] K.D. Chen, W.H. Hausman, Mathematical properties of the optimal product line selection problem using choice-based conjoint analysis, Management Science 46 (2000) 327–332.

[9] J.M. Day, M.A. Venkataramanan, Pro<sup>fi</sup>tability in product line pricing and composition with manufacturing commonalities, European Journal of Operational Research 175 (2006)1782-1797

[10] G. Dobson, S. Kalish, Positioning and pricing a product line, Marketing Science 7 (1988) 107–125.

[11] G. Dobson, S. Kalish, Heuristics for pricing and positioning a product-line using conjoint and cost data, Management Science 39 (1993) 160–175.

[12] F. Glover, Tabu search: part I, ORSA Journal on Computing 1 (1989) 190–206.

[13] F. Glover, Tabu search: part II, ORSA Journal on Computing 2 (1990) 4–32.

[14] F. Glover, M. Laguna, Tabu Search, Kluwer Academic, 1997.

[15] P.E. Green, A.M. Krieger, Models and heuristics for product line selection, Marketing Science 4 (1985) 1-19.

[16] P.E. Green, A.M. Krieger, Recent contributions to optimal product positioning and buyer segmentation, European Journal of Operational Research 41 (1989) 127–141.

[17] P.E. Green, A.M. Krieger, Individualized hybrid models for conjoint analysis, Management Science 42 (1996) 850–870.

[18] T.S. Gruca, B.R. Klemz, Optimal new product positioning: a genetic algorithm approach, European Journal of Operational Research 146 (2003) 621–633.

[19] E.R. Hansen, Global optimization using interval analysis—the one-dimensional case, Journal of Optimization Theory and Applications 29 (1979) 331–344.

[20] E.R. Hansen, G.W. Walster, Global Optimization Using Interval Analysis, Marcel Dekker, New York, 2004.

[21] R. Horst, H. Tuy, Global Optimization: Deterministic Approaches, Springer-Verlag Berlin, 1993.

[22] C.H. Hsieh, S.H. Chen, Model and algorithm of fuzzy product positioning, Information Sciences 121 (1999) 61–82.

[23] T.H. Hsu, K.M. Chu, H.C. Chan, Fuzzy clustering on market segment, In: IEEE International Conference on Fuzzy Systems, San Antonio, TX, USA, 2000

[24] J. Jiao, Y. Zhang, Product portfolio planning with customer–engineering interaction, IIE Transactions (Institute of Industrial Engineers) 37 (2005) 801–814.

[25] A. Kaul, V.R. Rao, Research for product positioning and design decisions: an integrative review, International Journal of Research in Marketing 12 (1995) 293–320.

[26] R. Kohli, R. Krishnamurti, A heuristic approach to product design, Management Science.33 (1987).1523-1533

[27] R. Kohli, R. Krishnamurti, Optimal product design using conjoint analysis: computational complexity and algorithms, European Journal of Operational Research 40 (1989) 186–195.

[28] R. Kohli, R. Sukumar, Heuristics for product-line design using conjoint analysis, Management Science 36 (1990) 1464–1478.

[29] U.G. Kraus, C.A. Yano, Product line selection and pricing under a share-of-surplus choice model, European Journal of Operational Research 150 (2003) 653–671.

[30] R.J. Kuo, L.M. Ho, C.M. Hu, Cluster analysis in industrial market segmentation through arti<sup>fi</sup>cial neural network, Computers and Industrial Engineering 42 (2002) 391–399.

[31] D.G. Luenberger, Linear and Nonlinear Programming, Addison-Wesley Pub. Co., Massachusetts, 1973.

[32] R.D. McBride, F.S. Zufryden, An integer programming approach to the optimal product line selection problem, Marketing Science 7 (1988) 126–140.

[33] L.O. Morgan, R.L. Daniels, P. Kouvelis, Marketing/manufacturing trade-offs in product line management, IIE Transactions (Institute of Industrial Engineers) 33 (2001) 949–962.

[34] S.K. Nair, L.S. Thakur, K.-W. Wen, Near optimal solutions for product line design and selection. Beam search heuristics, Management Science 41 (1995) 767.

[35] R. Schmalensee, J.-F. Thisse, Perceptual maps and the optimal location of new products: an integrative essay, International Journal of Research in Marketing (1988) 225–249.

[36] A.D. Shocker, V. Srinivasan, Consumer-based methodology for the identi<sup>fi</sup>cation of new product ideas, Management Science 20 (1974) 921–937.

[37] A.D. Shocker, V. Srinivasan, Multiattribute approaches for product concept evaluation and generation: a critical review, Journal of Marketing Research 16 (1979) 159–180.

[38] W. Steiner, H. Hruschka, A probabilistic one-step approach to the optimal product line design problem using conjoint and cost data, In: Review of Marketing Science, Working paper, 2002.

[39] D.S. Stewart, Segmentation and positioning for strategic marketing decisions, Journal of Marketing Research 35 (1998) 128–129.

[40] D. Sudharshan, J.H. May, A.D. Shocker, A simulation comparison of methods for new product location. Marketing Science 6 (1987) 182

[41] W.K. Tan, C.H. Tan, H.H. Teo, Consumer-based decision aid that explains which to buy: decision con<sup>fi</sup>rmation or overcon<sup>fi</sup>dence bias? Decision Support Systems 53 (2011) 127–141.

[42] J. Teghem, M. Pirlot, C. Antoniadis, Embedding of linear programming in a simulated annealing algorithm for solving a mixed integer production planning problem, Journal of Computational and Applied Mathematics 64 (1995) 91-102.

[43] L.S. Thakur, S.K. Nair, K.W. Wen, et al., New model and solution method for product line design with pricing, Journal of the Operational Research Society 51 (2000) 90–101.

[44] K.E. Train, Discrete Choice Methods with Simulation, Cambridge University Press, Cambridge, UK, 2003.

[45] G.L. Urban, J.R. Hauser, Design and Marketing of New Products, Prentice Hall, Englewood Cliffs, 1993.

[46] C. Yano, G. Dobson, Pro<sup>fi</sup>t-optimizing product line design, selection and pricing with manufacturing cost considerations, In: in: T.-H. Ho, C.S. Tang (Eds.), Product variet management: research advances, Kluwer, Norwell, MA, 1998, pp. 145–176

X. G. Luo received the M.Sc. degree in mechanical design and manufacturing and the Ph.D. degree in System Engineering, both from the Northeastern University, Shenyang, PR China. He is a Professor in the Department of System Engineering, Northeastern University, PR China. He is currently a research fellow with the Department of Industrial and Systems Engineering, The Hong Kong Polytechnic University, Hong Kong, PR China. He is the author or coauthor of eighteen research papers published in refereed international journals such as International Journal of Production Research, IEEE Transactions on Engineering Management, International Journal of Production Economics, European Journal of Operations Research, Engineering Optimization, Computers & Industrial Engineering, Computers in Industry, Expert Systems with Applications, International Journal of Computer Integrated Manufacturing, International Journal of Advanced Manufacturing Technology. His research interests include new product development, product planning, quality function deployment, and product family design.

C. K. Kwong received the M.Sc. degree in advanced manufacturing system from the University of Nottingham, Nottingham, U.K., and the Ph.D. degree in manufacturing engineering from the University of Warwick, Warwick, U.K. He is currently an Associate Professor in the Department of Industrial and Systems Engineering, The Hong Kong Polytechnic University, Kowloon Hong Kong, His research interests include new product development, product family design and integrated product, and process design.

J. F. Tang received the M.Sc. degree in automation and the Ph.D. degree in system engineering, both from the Northeastern University, Shenyang, PR China. He is currently a Professor and the Head of the Department of System Engineering, Northeastern University, Shenyang, PR China. He is the author or coauthor of more than 100 papers published in international and local journals, among which 40 are in refereed international journals. His research interests include fuzzy optimization theory and its applications supply chain planning and logistics management, quality design in new product development, and quality function deployment.

Yiliu Tu received a BSc in Electronic Engineering and an MSc in Mechanical Engineering both from Huazhong University of Science and Technology (HUST) in the People's Repub lic of China, and a PhD from Aalborg University (AU) in Denmark. He had worked in the

Department of Mechanical Engineering (1) of HUST, the Department of Production of AU, the Department of Manufacturing Engineering and Engineering Management of City University of Hong Kong, and the Department of Mechanical Engineering of University of Canterbury (New Zealand). He is now a full professor at the Department of Mechanical and Manufacturing Engineering, University of Calgary, Canada. His present research interests are One-of-a-Kind Production (OKP) product design and manufacture, ultra-fast laser micromachining, and modeling and simulation of networked critical infrastructure. He has published numerous research papers on international academic journals. He is a senior member of SME (Society of Manufacture Engineers), member of IPENZ (Institution of Professional Engineers New Zealand) and a professional engineer of APEGGA (The Association of Professional Engineers, Geologists, and Geophysicists of Alberta).
