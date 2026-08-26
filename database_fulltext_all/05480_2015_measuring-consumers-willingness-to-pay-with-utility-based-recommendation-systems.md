---
otero_id: 5480
otero_key: "FJ4E5VCA"
title: "Measuring consumers' willingness to pay with utility-based recommendation systems"
authors: "Michael Scholz; Verena Dorner; Markus Franz; Oliver Hinz"
year: "2015"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2015.02.006"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Measuring consumers' willingness to pay with utility-based recommendation systems

Michael Scholz <sup>a,</sup>⁎, Verena Dorner <sup>b</sup>, Markus Franz <sup>c</sup>, Oliver Hinz <sup>c</sup>

<sup>a</sup> Faculty of Business Administration and Economics, University of Passau, Innstr. 43, 94032 Passau, Germany

<sup>b</sup> Institute of Information Systems and Marketing, Karlsruhe Institute of Technology, Englerstr. 14, 76131 Karlsruhe, Germany

<sup>c</sup> TU Darmstadt, Hochschulstr. 1, 64289 Darmstadt, Germany

## a r t i c l e i n f o

Article history: Received 22 January 2014 Received in revised form 5 November 2014 Accepted 6 February 2015 Available online 14 February 2015

Keywords: Willingness to pay Utility-based recommendation system Utility function e-commerce

## a b s t r a c t

Our paper addresses two gaps in research on recommendation systems: <sup>fi</sup>rst, leveraging them to predict consumers' willingness to pay; second, estimating non-linear utility functions – which are generally held to provide better approximations of consumers' preference structures than linear functions – at a reasonable level of cognitive consumer effort. We develop an approach to simultaneously estimate exponential utility functions and willingness to pay at a low level of cognitive consumer effort. The empirical evaluation of our new recommendation system's utility and willingness to pay estimates with the estimates of a system based on linear utility functions indicates that exponential utility functions are better suited for predicting optimal recommendation ranks for products. Linear utility functions perform better in estimating consumers' willingness to pay. Based on our experimental data set, we show how retailers can use these willingness to pay estimates for pro<sup>fi</sup>t-maximizing pricing decisions. © 2015 Elsevier B.V. All rights reserved.

## 1. Introduction

Consumers' willingness to pay (WTP) and their utilities for different products are indispensable inputs for many prediction and optimization models that support core business decisions and processes. They help decision makers de<sup>fi</sup>ne ef<sup>fi</sup>cient pricing strategies (e.g. [1,2]), estimate market share (e.g. [3]), determine the optimal pace for product updates (e.g. [4]), realign service operations (e.g. [5]), or identify optimal product assortments (e.g. [6]).

These decision models will, of course, yield reliable results only if valid estimates for consumer preferences and WTP are available, which is dif<sup>fi</sup>cult for two reasons. First, the cost of estimating current utility values and WTP is high. Eliciting this information empirically is expensive because valid estimates for WTP can often be obtained only at the time of purchase and under the prevailing marketing mix conditions [7]. This problem is exacerbated by the fact that consumer preferences change over time. Hence, preference elicitation must be repeated at regular intervals to monitor the estimates' validity. Second, consumers are typically not willing to expend a lot of effort and time (repeatedly, no less) for specifying their preferences [8], which reduces the reliability of their inputs and, in consequence, reduces recommendation accuracy [9].

These two issues can be solved with utility-based recommendation systems. Recommendation systems are very frequently employed as consumer decision support systems in online retailing, and most consumers use them regularly. That consumers are intrinsically motivated to use them, and to use them repeatedly, makes it possible to recognize structural changes in consumer preferences and WTP immediately, and to obtain utility estimates for new products almost at once. Despite these advantages, recommendation systems data are seldom suggested as inputs for marketing and management decision models [10] or as inputs for WTP estimation.

We contribute to recent research in operations research, information systems and marketing by proposing a utility-based recommendation system which measures consumer preferences and WTP 1) reliably and 2) at low costs for companies and 3) low cognitive effort for consumers. Speci<sup>fi</sup>cally, we develop a new low-effort approach, based on Butler et al.'s [11] utility exchange approach. This approach proposes that utility in one attribute can be exchanged for utility in another. We propose to exchange utility in price for the utility of entire products to estimate consumers' WTP.

We extend utility-based recommendation systems to estimate consumers' individual WTP for zero-switch utility functions [12]: linear and exponential utility functions. In addition, our research sheds light on the question which of the two most popular single-attribute utility (SAU) functions from operations and marketing research – exponential [13,14] or linear functions [15,16] – are better suited for utility-based recommendation systems.

The remainder of our paper is organized as follows. The next section brie<sup>fl</sup>y introduces the utility and WTP model we are proposing. Section 3 shows how this model can be integrated into recommendation systems. Section 4 describes our design and setting for testing this model in a laboratory experiment. Section 5 presents the results of this experiment. Section 6 provides a closer look at how this information can be used to optimize pricing decisions and discusses economic implications. Section 7 concludes the paper with an outlook on future research.

## 2. Modeling utility-based recommendation systems

Utility-based recommendation systems are a rather novel feature of online retailing. Usually, recommendations are generated with collaborative <sup>fi</sup>ltering or content-based techniques [17]. Content-based techniques recommend items similar to those a consumer has bought in the past. Collaborative <sup>fi</sup>ltering techniques recommend items to a consumer based on purchase decisions by other consumers who have similar tastes and preferences. But though ubiquitous, both techniques frequently produce low quality recommendations, which is due to three major issues [18]. First and most important is the cold-start problem [19]. Content-based and collaborative <sup>fi</sup>ltering techniques cannot provide recommendations unless multiple-item purchasing pro<sup>fi</sup>les for a number of consumers, or at least for the consumer currently using the system, are available. Second, preference estimates based on purchasing pro<sup>fi</sup>les are inaccurate when, as is often the case, these pro<sup>fi</sup>les contain products purchased as gifts for or on behalf of other consumers. Third, purchasing pro<sup>fi</sup>les are historical data, revealing past but not necessarily current preferences.

None of these issues arises in utility-based recommendation systems. Utility-based recommendation systems compute consumers' individual utilities for all products of a given category [9,20]. Individual multipleattribute utility (MAU) functions are constructed based on explicit preference statements provided by the consumers (i.e. ratings of attributes or products). This preference information can then be used to obtain estimates for consumers' individual WTP [21]. However, the drawback of utility-based recommendation systems is the fact that consumers must actively provide input before a recommendation is possible.

Designing a utility-based recommendation system for estimating consumers' WTP poses three major challenges. First, recommendation systems ought to be <sup>fl</sup>exible with regard to the shape of the estimated utility function. Utility functions for different attributes and consumers may be linear, convex or concave [14], and the shape of utility functions must be de<sup>fi</sup>ned prior to estimating and generating recommendations. In other words, only if all attribute levels' utility values are known (in theory, consumers need to specify utility values for each attribute level for each attribute), or at least predictable, can the system generate recommendations. Estimating utility values for only a few attribute levels and manually selecting an appropriate utility function based on these utility values – as done in many marketing studies [e.g. 22,15] – is not feasible for a recommendation system. Flexible recommendation systems thus require higher consumer effort, whose level depends on the methods used for measuring attribute weights (Section 2.1), SAU functions (Section 2.2) and WTP (Section 2.4). This raises the second challenge for utility-based recommendation system design: system usage ought to be easy and require little effort. Consumers are typically unwilling to invest much time and cognitive effort in eliciting preferences or utility functions [8]. High-effort systems have a negative in<sup>fl</sup>uence both on consumers' willingness to use these systems and on the reliability of consumers' inputs. And third, consumers' WTP must be computed for all conceivable products.

In the next sections, we show how these challenges can be met by adapting the utility model and system interaction design, and propose a new model for a utility-based recommendation system.

## 2.1. Utility estimation

Utility estimation methods have been applied to a wide range of issues including vendor selection [23], the evaluation of knowledge portal development tools [24], the prediction of market shares [25], WTP estimation [21] and product recommendation [9]. But despite their importance and the large number of different approaches to estimating utilities, no model has been proven superior so far (e.g. [26–28]). Table 1 provides an overview of utility estimation methods that have been put forward as core methods for utility-based recommendation systems.

Table 1  
Utility estimation methods in utility-based recommendation systems.

<table><tr><td>Utility Estimation</td><td>Input</td><td>Effort</td><td>Accuracy</td><td>References</td></tr><tr><td>DR</td><td>Attribute weights</td><td>Low</td><td>High</td><td>[29–31]</td></tr><tr><td>SMARTER</td><td>Attribute weights</td><td>High</td><td>High</td><td>[9]</td></tr><tr><td>RBFN</td><td>Attribute weights</td><td>Low</td><td>Low</td><td>[9]</td></tr><tr><td>RBCA</td><td>Product ratings</td><td>High</td><td>High</td><td>[20]</td></tr><tr><td>CBCA</td><td>Product choices</td><td>High</td><td>High</td><td>[32]</td></tr></table>

The majority of commonly used utility estimation methods have severe shortcomings with respect to at least one criterion, accuracy or consumer effort. Methods such as SMARTER [9] or rating-based conjoint analysis (RBCA) [20] generate highly accurate estimates, but they are cognitively very expensive [32]. Radial basis function networks (RBFN) are easier to use, but less accurate than SMARTER [9]. Using product ratings for estimating individual utility functions poses much the same problems as using content-based and collaborative <sup>fi</sup>ltering systems: consumers rate only a fraction of available products, and these ratings become obsolete over time [18].

One particularly simple method, direct rating (DR), has been shown to generate surprisingly accurate attribute weights [31], outperforming more complex approaches like AHP and requiring much less consumer effort [27,33]. Attribute weights are, however, only a part of utility estimates and need to be combined with single-attribute utility functions for computing overall product utilities. Recent research often assumes linear single-attribute utility functions with a utility of 0 for the worst and a utility of 1 for the best level of a particular attribute [29,30]. These linear functions can be estimated without incurring user effort and are easily combined with attribute weights elicited with direct rating, direct ranking or AHP (see Section 2.2).

In the following sections, we show how reliable WTP and utility values can be estimated based on consumer inputs elicited with DR, which are then combined in multi-attribute utility functions.

## 2.2. Multi-attribute utility model

Multi-attribute utility theory (MAUT) assumes that products are bundles of attributes and that consumers evaluate products by evaluating their attributes. Each attribute i that affects the purchase decision is described by a weighted single-attribute utility (SAU) function w u (x ), $x _ { i }$ being the level of attribute i and w the weight for attribute i. Linear SAU functions are easier to estimate than non-linear SAU functions, but the latter are held to be a better approximation of consumers' preferences [14] and to generate more accurate estimates.

For linear SAU functions, estimating the scaling parameters a and b

$$
u _ {i} (x _ {i}) = a _ {i} + b _ {i} x _ {i}\tag{1}
$$

does not pose a large problem. We assign a utility value of 0 to the worst level $x _ { i } ^ { w o r s t }$ of attribute i and a utility value of 1 to the best level $x _ { i } ^ { b e s t }$ , assuming that x is normalized in [0; 1] [34]. The scaling parameters are now given as $a _ { i } = 0$ and $b _ { i } = 1$

For modeling non-linear SAU functions, we choose the more <sup>fl</sup>exible exponential shape [13,11,14].

$$
u _ {i} (x _ {i}) = a _ {i} - b _ {i} e ^ {c _ {i} x _ {i}}\tag{2}
$$

If empirical SAU functions are non-linear [14], exponential SAU functions provide more accurate utility estimates. By introducing the scaling constant $c _ { i } ,$ SAU functions can now be modeled as linear, convex or concave. Despite its great <sup>fl</sup>exibility, however, Eq. (2) is an unpopular choice for practical applications of utility-based recommendation systems [34,20]. Estimating c requires additional consumer input and thus effort, which increases the likelihood of consumers terminating the recommendation process prematurely and of obtaining less reliable preference and WTP estimates.

We propose a new effort-minimizing approach for estimating $c _ { i }$ which requires consumers merely to specify their utility for the average attribute level x <sup>average</sup>. We suggest that the additional effort will be overcompensated by better recommendations due to more accurate utility estimates.

Given that $x _ { i } ^ { w o r s t } = 0 , x _ { i } ^ { b e s t } = 1 , u _ { i } ( x _ { i } ^ { w o r s t } ) = 0 ,$ , and $u _ { i } ( x _ { i } ^ { b e s t } ) = 1$ , we can then estimate $c _ { i } \left( \operatorname { E q s . } \left( 3 \right) \right.$ and (4)).

$$
\begin{array}{l} c _ {i} = \ln \left(\left(\frac {1 - \sqrt {1 - 4 u _ {i} (x _ {i} ^ {\text { average }}) (1 - u _ {i} (x _ {i} ^ {\text { average }}))}}{2 u _ {i} (x _ {i} ^ {\text { average }})}\right) ^ {2}\right) \quad \text { if } u _ {i} (x _ {i} ^ {\text { average }}) > 0. 5 \\ c _ {i} = \ln \left(\left(\frac {1 + \sqrt {1 - 4 u _ {i} (x _ {i} ^ {\text { average }}) (1 - u _ {i} (x _ {i} ^ {\text { average }}))}}{2 u _ {i} (x _ {i} ^ {\text { average }})}\right) ^ {2}\right) \quad \text { if } u _ {i} (x _ {i} ^ {\text { average}}) \leq 0. 5 \\ c _ {i} = 0 \quad \text { if } u _ {i} (x _ {i} ^ {\text { average }}) = 0. 5 \end{array}\tag{3}
$$

Parameters $a _ { i }$ and $b _ { i }$ are now given by

$$
\begin{array}{l} a _ {i} = \frac {1}{1 - e ^ {c _ {i}}} \\ b _ {i} = a _ {i}. \end{array}\tag{4}
$$

Depending on the level of $u _ { i } ( x _ { i } ^ { a v e r a g e } )$ , the exponential SAU function is either convex $( u _ { i } ( x _ { i } ^ { a v e r a g e } ) < 0 . 5 )$ , concave $( u _ { i } ( x _ { i } ^ { a v e r a g e } ) > 0 . 5 )$ or linear $( u _ { i } ( x _ { i } ^ { a \nu e r a g e } ) = 0 . 5 )$ . Compared to the speci<sup>fi</sup>cation effort for linear SAU functions, exponential SAU functions thus require only one additional step per function (i.e. per attribute) in which the consumer states her utility for $x _ { i } ^ { a v e r a g e }$

To compute the overall product utility $U ( X _ { k } )$ , SAU functions are aggregated in a MAU function [9]. The additive MAU function is

$$
U (X _ {k}) = \sum_ {i = 1} ^ {n} w _ {i} u _ {i} (x _ {i})\tag{5}
$$

where $0 \leq w _ { i } \leq 1$ , and $\sum _ { i } ^ { n } { } _ { = 1 } { w _ { i } } = 1$

Specifying additive functions requires the lowest consumer effort, but they rest on two strict assumptions: mutual utility independence for each pair of attributes and additive independence among all attributes. Attributes are mutually utility independent if and only if each subset of attribute levels ${ \boldsymbol { x } } = ( x _ { 1 } , x _ { 2 } , . . . , x _ { n } )$ is independent of its complementary subset in terms of its utility. Attributes are additively independent if the interaction between two or more attributes has no effect on alternatives' utilities. Clearly, these assumptions hold in few decision scenarios. But additive models have been shown to be robust even if additive independence does not hold [35,36]. Combining I exponential SAU functions in an additive MAU function requires consumer input on I parameters for w and I parameters for $u _ { i } ( x _ { i } ^ { a v e r a g e } )$ ; combining linear SAU functions additively requires input on I parameters. In the following sections, we suggest a new approach for estimating WTP with a MAUT-based approach.

## 2.3. Willingness to pay estimation

WTP estimation methods suitable for practical application must meet two criteria: one, that they yield valid measurements for products and product categories, and two, that they require very little consumer input. Empirical studies usually apply WTP estimation methods that elicit WTP i) directly, ii) based on auction bids for a product or iii) from utility functions (e.g. conjoint analysis).

For direct WTP elicitation, consumers are simply asked to state their WTP, for instance by way of an open question. Direct WTP measurements are surprisingly accurate, considering the low level of consumer effort required [37]. However, this only holds true for one or few products. In cases where WTP for a greater number of products or even an entire product category needs to be elicited, direct WTP elicitation is quite taxing for the consumer. Also, consumers may not like to openly state their WTP if they feel that companies use this information for price discrimination.

In auctions like the Vickrey auction, <sup>fi</sup>rst price auction, or the BDM mechanism, the dominant bidding strategy is to exactly bid the WTP. It is therefore not surprising that auctions measure consumers' WTP with high accuracy [38]. Drawbacks of auctions are, <sup>fi</sup>rst, that auction fever [39], market competition [40] and other factors can bias WTP measurement. Second, WTP estimates based on auctions are limited to the products used in the auction. It is not possible to infer the WTP for other products in the same category. As with direct WTP measurement, one data point must be elicited for each (new) product.

Methods which estimate WTP from utility functions do not share this drawback. WTP for all products in a category for which a set of utility functions is valid can be estimated without further consumer input for each product. Some utility-based methods, like direct rating or self-explication approaches (e.g. [41]), require direct input on SAU functions. Others, like rating-based or choicebased conjoint analysis, measure SAU functions by decomposing consumer evaluations of entire products (e.g. [21]). Direct utility elicitation methods are cognitively less demanding than compensatory approaches [8,32].

Yet another data source for WTP estimation is market data: scanner data, for instance, are often used for estimating demand curves [42,43]. Their major advantage is that real purchases are used. Their major drawback is their aggregation level, which makes them unsuitable for estimating individual WTP. Perhaps even more importantly, data for estimating demand curves must contain a suf<sup>fi</sup>ciently high level of price variation which, in practice, it may not always be feasible to induce.

Comparing methods for WTP measurement (Table 2) shows that most methods are designed for single-point measurements. Repeated measurements with conjoint experiments, auctions, or surveys lead to high effort on part of the consumer and high costs on part of the executing company. We propose to solve this problem by integrating direct utility elicitation (see Section 2) in recommendation systems. Direct utility elicitation methods require little consumer effort (Table 2), but, as stated by [44], they need to be adapted for WTP measurement. We introduce an extension to direct utility elicitation, which is based on the utility exchange approach [11], in the next section.

## 2.4. Willingness to pay model

A consumer's WTP for a speci<sup>fi</sup>c product $X _ { k }$ is de<sup>fi</sup>ned as the price at which she is indifferent between buying and not buying $X _ { k }$ [49]. Consumer $j ^ { \prime } s$ utility function for product $X _ { k }$ is given by $U _ { j } ( X _ { k } , y _ { j } )$ , where $y _ { j }$ refers to the composite product consisting of all products other than $X _ { k }$ which consumer j purchases. She uses her budget $m _ { j }$ for purchasing both the composite product y and zero or one units of product $X _ { k } .$ Consumer $j \mathrm { \ " { s } }$ budget equation is

$$
m _ {j} = p (X _ {k}) + p \left(y _ {j}\right)\tag{6}
$$

where $p ( X _ { k } )$ is the price of product $X _ { k }$ and $p ( y _ { j } )$ is the price of the composite product $y _ { j } .$ Her utility function is $U _ { j } ( X _ { k } , ( m _ { j } - p ( X _ { k } ) ) / p ( y _ { j } ) )$ $\mathrm { i f } X _ { k }$ is attractive enough to be purchased. This is only the case if the utility of $X _ { k }$ exceeds the so-called utility threshold $\tau _ { j } \ [ 2 0 ]$ . All products whose utilities lie below the threshold $\tau _ { j }$ are not attractive enough to consumer j for her to seriously consider purchasing them. In that case, her utility function equals $U _ { j } ( 0 , m _ { j } / p ( y _ { j } ) )$ and her WTP equals<sup>1</sup>

Comparison of WTP estimation methods

<table><tr><td>Method</td><td>Individual measurement</td><td>Revealed preferences</td><td>WTP prediction for similar products</td><td>Repeated measurement</td><td>Consumer effort</td><td>References</td></tr><tr><td>Direct WTP elicitation</td><td>Yes</td><td>No</td><td>No</td><td> $No^*$ </td><td>Low</td><td>[45,46,37]</td></tr><tr><td>Auctions</td><td>Yes</td><td>Yes</td><td>No</td><td>Yes</td><td>Low</td><td>[46,40,38]</td></tr><tr><td>Direct utility elicitation</td><td>Yes</td><td>No</td><td>Yes</td><td> $No^*$ </td><td>Low</td><td>[47,44]</td></tr><tr><td>Conjoint analyses</td><td>Yes</td><td>No</td><td>Yes</td><td> $No^*$ </td><td>High</td><td>[48,46,21]</td></tr><tr><td>Market data</td><td>No</td><td>Yes</td><td>No</td><td>Yes</td><td>Low</td><td>[42,43]</td></tr><tr><td>UBRS</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Low</td><td>This study</td></tr></table>

Repeated measurements are possible, but usually expensive

$$
U _ {j} \left(X _ {k}, \frac {m _ {j} - W T P _ {j} (X _ {k})}{p (y _ {j})}\right) - \tau_ {j} \equiv 0.\tag{7}
$$

Once we know consumer $j ^ { \prime } s$ utility threshold $\tau _ { j } ,$ we can predict her purchase decision for any product $X _ { k } .$ Prediction accuracy thus depends on obtaining reliable estimates for consumers' utility thresholds $\tau _ { j \cdot }$ We propose to identify $\tau _ { j }$ and $W T P _ { j } ( X _ { k } )$ for product $X _ { k }$ by combining MAUT with Butler et al.'s [11] utility exchange approach (Fig. 1).

At a given level of WTP for product $X _ { k } ,$ the utility threshold $\tau _ { j }$ expresses the utility of product $X _ { k }$ with a price of $W T P _ { j } ( X _ { k } )$ ). Consumer j is indifferent between purchasing and not purchasing the product. We now need to <sup>fi</sup>nd, for all other attractive products, the prices which would render their utilities equal to $\tau _ { j \cdot }$ In order to do that, we use the utility exchange approach as proposed by [11]. This approach is based on the idea of even swaps [50,51].

Consider a consumer whose utility threshold is $\tau _ { j } = 9$ and for whom $U ( X _ { k } ) = 1 0$ . If we were to downgrade one of the attributes of $X _ { k }$ just so much that the consumer's utility for $\cdot X _ { k ^ { \prime } }$ decreased by one utility unit to 9 units, she would still perceive the product to be attractive. Now assume that the attribute in question is the price. A reduction in utility corresponds to an increase in price, and the new increased price equals the consumer's WTP for $X _ { k ^ { \prime } }$ . Thus one utility unit has been “exchanged” for price units, at the consumer's individual “exchange rate”.

In Eqs. (8) and (9), price is assumed to be attribute $i = 1$ and the underlying MAU function to be additive. In the case of exponential SAU functions, WTP for product $X _ { k ^ { \prime } }$ is given by

$$
W T P _ {j} (X _ {k ^ {\prime}}) = l n \left(\frac {a _ {1} - \left(\frac {(\tau_ {j} - \sum_ {i = 2} ^ {n} w _ {i} u _ {i} (x _ {i}))}{w _ {1}}\right)}{b _ {1}}\right) / c _ {1}.\tag{8}
$$

For linear SAU functions, WTP for product $X _ { k }$ can be computed as:

$$
W T P _ {j} (X _ {k ^ {\prime}}) = \frac {\frac {\tau_ {j} - \sum_ {i = 2} ^ {n} w _ {i} u _ {i} (x _ {i})}{w _ {1}} - a _ {1}}{b _ {1}}.\tag{9}
$$

The next section describes the design of a utility-based recommendation system implementing our approach (Fig. 1), in particular how attribute weights $w _ { i } ,$ average attribute level utility $\bar { u _ { i } } ( x _ { i } ^ { a v e r a g e } )$ and WTP for any product $X _ { k }$ are elicited and estimated.

## 3. Recommendation system design

In designing our recommendation system, we must balance consumer effort and recommendation accuracy. The level of consumer effort depends on the methods used for measuring attribute weights, SAU functions and WTP. We use DR for eliciting attribute weights $w _ { i } ,$ a method both simple and accurate (Section 2.1; [27]).

For estimating single attribute utilities, we use linear and exponential SAU functions (Section 2.2). Exponential SAU functions can generate more accurate recommendations than linear functions (Section 2) but require additional information about the average attribute levels' utilities (Eq. (3)). We elicit this information by displaying the lower and upper bounds, $u _ { i } ( x _ { i } ^ { b e s t } ) = 1$ and $u _ { i } ( x _ { i } ^ { w o r s t } ) = 0 ,$ , of the attribute level intervals to the consumer and asking her to state $u _ { i } ( x _ { i } ^ { a v e r a g e } )$ (Fig. 2; [16,41]).

Finally, we need to elicit consume $j ^ { \prime } s$ utility threshold $\tau _ { j }$ to estimate WTP. Butler et al. [11] suggest asking her: “If products A and B are identical on all criteria except price and product A costs P, what is the lowest price of B that could make you feel that B is signi<sup>fi</sup>cantly better than $A ? ^ { \mathfrak { p } }$

Unfortunately, this approach has shown low empirical validity [20]. For one, thinking in utility units and thinking in price units appear to be two cognitively different tasks. For another, rational consumers will feel that B is signi<sup>fi</sup>cantly better (i.e. they will prefer it over A) even if the price difference is extremely small. Extremely small price differences, however, lead to an overestimation of the utility threshold $\tau _ { j }$ [20]. WTP elicitation can be a sensitive issue when stated WTP is used to predict WTP for other products. We avoid this issue by asking consumers to state their individual WTP for a hypothetical product $X _ { k } .$ Because our approach requires WTP for $X _ { k }$ to be greater than zero, we de<sup>fi</sup>ne $X _ { k }$ as a modi<sup>fi</sup>ed version of the best expected product. Speci<sup>fi</sup>cally, we take the best expected product and decrease the level of its least important attribute (only if $w _ { i } > 0 )$ to $x _ { i } ^ { w o r s t }$ to generate the hypothetical product $X _ { k } ,$ , which ensures that the probability for $W T P _ { j } ( X _ { k } ) > 0$ is high. After consumer j stated her $W T P _ { j } ( X _ { k } )$ , we can compute her utility threshold $\tau _ { j \cdot }$ Applying Eqs. (8) or (9) yields the WTP estimates for all real products.

Consumers typically do not know exactly how much they are willing to pay for a product — they seldom possess perfect information about product quality [52]. It is easier for consumers to specify WTP as a range than a price point, and results are generally more valid [53,54]. WTP is therefore elicited as a range over three price points [53]:

1. Floor WTP: The highest price at which a consumer will (still) de<sup>fi</sup>- nitely purchase the product, i.e. 100% purchase probability.

2. Indifference WTP: The price at which a consumer is indifferent between purchasing and not purchasing the product, i.e. 50% purchase probability.

3. Ceiling WTP: The lowest price at which a consumer will de<sup>fi</sup>nitely not purchase the product (anymore), i.e. 0% purchase probability.

WTP is elicited directly with open questions because they are of low cognitive complexity and measure consumers' WTP as validly as more complex methods like choice-based conjoint analysis [37].

## 4. Empirical investigation

We conducted two laboratory experiments with between-subject designs. The main experiment was used to compare the performance of linear and exponential SAU functions, speci<sup>fi</sup>cally with regard to the accuracy of utility function and WTP estimates. We implemented one

![](/api/attachments/FJ4E5VCA/fulltext/images/a0141335fa3b8823ed38d86b666bf2e7658a36f0fedf68216ab870ebcfb88d23.jpg)  
\* adapted from Butler et al. (2001)  
\*\* Jedidi and Zhang (2002); Keeney and Raiffa (1993)

Fig. 1. Estimating WTP from recommendation data.

recommendation system for each treatment (linear and exponential). Both recommendation systems (treatments) operated on a product data base of 162 camera models by 16 manufacturers, which re<sup>fl</sup>ected the actual market situation at the time of the experiment quite well. Each camera was described by eight attributes: photo resolution, optical zoom, camera size, display resolution, video resolution, range of settings options, ISO sensitivity and price.

We chose a search good because estimating product utilities requires attribute levels to be operationalized objectively and reliably [34], which is impossible for experience goods. Their attribute levels can be determined, subjectively, only after purchase and use [55,56]. Digital cameras are a very popular category of search goods, which we could assume all our participants to be reasonably familiar with [57]. To ensure a minimal level of product expertise, we provided all participants with information on each of the eight camera attributes.

Since one of our goals was to measure participants' WTP, we did not display product pictures or prices to participants when measuring WTP, thus excluding two potential sources of bias. Product pictures can affect consumers' WTP [58], and prices can serve as an anchor for consumers' WTP [59].

We conducted a supplementary experiment for checking three important assumptions inherent in our approach and empirical setting, namely that SAU functions were monotonous, that participants in our subject pool were indeed suf<sup>fi</sup>ciently familiar with the product category to state their preferences, and that there existed no systematic genderrelated differences in expertise between participants in our subject pool, as have sometimes been found for technical products [60]. Setting and instructions remained unchanged from the main experiment, but the SAU functions in this experiment were “free” in the sense that no prior shape (linear or exponential or otherwise) was assumed, and additional questions on participant familiarity with digital cameras were added to the post-experimental survey (see Section 4.1).

The following subsections describe the experimental procedure and results.

## 4.1. Experimental procedure

All recommendation systems (treatments) implement the screening and evaluation stages of the purchasing process as described by [61] and [62] (Fig. 3).

In the screening task (Task A in Fig. 3), designed to remove unattractive cameras from the recommendation set, participants speci<sup>fi</sup>ed aspiration levels for all attributes. In the evaluation task (Task B in Fig. 3), participants indicated attribute weights w by directly allocating between one and eleven points to each attribute. Participants in the exponential treatment additionally stated for each attribute how attractive they would consider a camera equipped with an average level (x<sup>average</sup>) of that particular attribute.<sup>2</sup> Participants in the supplementary experiment were asked the same questions for 5 levels for each attribute so that we could test the shape of the SAU functions and estimate more <sup>fl</sup>exible SAU functions.<sup>3</sup> The information from tasks A and B was used to compute overall product utilities.

In the third task (Task C in Fig. 3), participants speci<sup>fi</sup>ed their WTP for a modi<sup>fi</sup>ed version (Section 3) of the best recommended product. This information was then used to estimate participants' utility thresh olds $\tau _ { j }$ (Section 2.4).

In the fourth task (Task D in Fig. 3), recommendation set evaluation, we displayed the top 10 recommended products in descending order of their utilities. Participants rated these products on an eleven-point scale and speci<sup>fi</sup>ed their WTP for each product in three open questions (Section 3). We used task D for validating both utility and WTP accuracy.<sup>4</sup>

After both experiments, participants answered a questionnaire on basic demographic information; their perceptions of the system (perceived ease of use, perceived satisfaction with the system, perceived usefulness, perceived reuse intention and perceived task dif<sup>fi</sup>culty); and their e-shop usage. Thus we were able to control for potential effects of participant and system characteristics on utility and WTP estimation accuracy.

After the supplementary experiment, participants answered an additional expertise questionnaire with two comprehension questions for each attribute. We examined both “theoretical” knowledge, i.e. how attribute functionality is de<sup>fi</sup>ned, and “applied” knowledge, i.e. how to use different functions in a real setting.

## 4.2. Pretest

We tested the treatments with 13 undergraduate students in think aloud protocols [63], which are particularly well suited for exploring user-system interactions and user decision making [64]. After completing the experiment, participants answered a small questionnaire on treatment comprehensibility and perceived effort of system use. We conducted four rounds of pretests with three or four participants each, adjusting the system according to the feedback from each round until no further suggestions for improvement were made.

## 4.3. Samples

77 undergraduate and graduate students of a German university took part in the supplementary experiment. 55 were female and 22 were male. In this experiment, we speci<sup>fi</sup>cally tested for gender-

Photo Resolution: 20 Megapixel Photo Resolution: 12,5 Megapixel (?) Photo Resolution 5 Megapixel

![](/api/attachments/FJ4E5VCA/fulltext/images/c0881995ac297e9d2b3e509c0db41fc7e4c0e376eff708007939149b97c9874f.jpg)  
Fig. 2. Elicitation of parameter c of exponential SAU functions.

related differences in camera expertise. More precisely, we compared, for each attribute, the percentages of male and female participants who were able to answer the two expertise questions correctly. Participants had to select the correct answer out of four given answers. There were no signi<sup>fi</sup>cant differences between male and female participants' comprehension of camera attributes with the exception of ISO sensitivity. Although a greater percentage of female than male participants knew what ISO sensitivity is (F = 96.4% and $\mathsf { M } = 8 1 . 8 \% , \mathsf { p } = 0 . 0 3 4 )$ , male participants had a better idea of how to apply this knowledge in practice $( \mathrm { F } = 5 2 . 7 \%$ and $\mathsf { M } = 7 7 . 2 \% , \mathsf { p } = 0 . 0 4 9 \%$ ). For all other attributes, at least 78% of participants (male and female respectively) were able to answer both questions correctly; indeed for most attributes, over 90% could do so. These results are much higher than the 25% criterion (randomly choosing one out of the given four answers). We conclude that in our sample, the level of product expertise was suf<sup>fi</sup>ciently high for attribute-level preference elicitation, and that differences in expertise could not be explained with gender.

In the main experiment, 93 students from the same university took part. The samples for both experiments were drawn randomly from the same subject pool (without replacement), and we have no indication that they differed substantially. The sample was evenly distributed across treatments with 43 participants in the linear treatment and 50 in the exponential treatment. Participants were aged between 19 and 32 years. 61 participants were female, 32 were male.

Ordered logit regressions did not show any signi<sup>fi</sup>cant differences with respect to gender (p = 0.60), e-shop usage frequency $( p = 0 . 2 6 )$ perceived ease of use (p = 0.45), perceived usefulness $( p = 0 . 8 4 )$ , end user satisfaction (p = 0.33) or reuse intentions (p = 0.49) between treatments. We did <sup>fi</sup>nd a signi<sup>fi</sup>cant difference in age between treatment groups $( p = 0 . 0 2 )$ , but no effect of age on utility accuracy $( p > 0 . 3 ) ^ { 5 }$ or WTP accuracy $( p = 0 . 6 6 ) . ^ { 6 }$ Results indicate that differences in accuracy depend on the different SAU functions only.

## 5. Analysis and results

As suggested by [17], we used search time to approximate the level of cognitive effort during the use of the recommendation system (Section 5.1) and to determine the additional effort of specifying exponential utility functions. To ensure that WTP estimates were based on reliable and valid input, we examined the accuracy of utility estimates (Section 5.2) before comparing the accuracy of WTP estimates (Section 5.3) of the two experimental groups in the main experiment.

## 5.1. Effort

Search time was measured as time lapsed between participants' <sup>fi</sup>rst interaction (de<sup>fi</sup>ning aspiration levels) and last interaction (rating recommended products) with the recommendation agent (tasks A–D in Fig. 3). Task dif<sup>fi</sup>culty was measured with 4 items ranging from 1 (very easy) to 7 (very dif<sup>fi</sup>cult). All items referred to the measurement of the utility parameters.

It took our participants on average 804 $. 7 2 1 \ s ( \mathrm { S D } = 3 2 5 . 1 5 3 )$ to complete the search task with the linear system and 889.640 s $\mathrm { ( S D = 2 8 0 . 4 3 8 ) }$ with the exponential system. In other words, participants spent signi<sup>fi</sup>cantly more time (gamma regression; $p < 0 . 1 )$ on specifying exponential functions. Despite this difference in time, however, perceptions of task dif<sup>fi</sup>culty did not differ between treatments (ordered logit regression; $p = 0 . 2 0 0 )$ . All participants considered the task to be quite easy on a seven-point scale ranging from 1 (very easy) to 7 (very hard) (linear: 2.634 (SD = 1.009); exponential: 2.430 (SD = 1.080)).

The supplementary experiment with “free” function shapes, allowing for instance U-shaped SAU functions, was by far the most strenuous for participants. It took them on average 1038.038 s $( \mathrm { S D } = 2 7 9 . 3 7 0 )$ to complete the search task. In other words, participants in the supplementary experiment spent 16% more time on that task than participants in the exponential treatment and nearly 30% more than participants in the linear treatment.

## 5.2. Utility accuracy

Before assessing the utility accuracy for linear and exponential systems, we checked whether treatments affected participants' preferences. We found no effect of preference elicitation method on the stated preferences.

Average attribute weights in the two treatments indicate that there was virtually no difference in overall attribute rankings between treatments. Moderately high standard deviations point to heterogeneous preferences within the two treatments (Table 3).

We found no signi<sup>fi</sup>cant differences for estimated utility thresholds τ<sub>j</sub> (t-test, p N 0.1). Participants in the linear treatment had an average utility threshold of 28.345 $( \mathrm { S D } = 7 . 2 7 7 )$ , and participants in the exponential treatment a threshold of 29.315 $( \mathrm { S D } = 1 0 . 0 7 0 )$ ).

Exponential SAU functions were predominantly concave $( u _ { i } ( x _ { i } ^ { a v e r a g e } ) > 0 . 5 ;$ Table 3). Only 16% of participants in the exponential treatment speci<sup>fi</sup>ed the scaling parameter $c _ { i }$ such that the function shape was equivalent to a linear SAU function $( u _ { i } ( x _ { i } ^ { a \nu e r a g e } ) = 0 . 5 )$ ) for most attributes. This is consistent with previous <sup>fi</sup>ndings indicating that consumers generally do not perceive linear relationships between attribute levels and utilities [14] and underlines the importance of estimating exponential functions.

We used our supplementary experiment to test the notion that SAU functions may be of (inverted) U-shape. For most attributes, the great majority of participants speci<sup>fi</sup>ed monotonously increasing SAU functions (i.e. utility is increasing from the worst to the best attribute level), except size and the range of settings options (Table 4).

Apparently, participants perceived these attributes not as unidimensional but containing trade-offs between several factors; “size”, for instance, may imply a trade-off between “ease of transportation” and “fragility”. All remaining attributes were considered independently of other attributes by most participants. This suggests that by splitting multi-dimensional attributes into atomic attributes, the performance of our approach could be further improved due to better SAU estimation.

The accuracy of the utility estimates in both treatments was similar to that reported in other empirical studies on utility estimation and prediction of consumers' purchase decisions (Table 5). Note that the studies' settings were very diverse, which somewhat reduces comparability. For instance, task complexity ranged from 12 attributes and 42 levels [41] to 5 attributes and 10 levels [48]. Required effort varied widely, with rating-based conjoint methods requiring as many as 24 attribute-level ratings and 24 product-level pairwise comparisons and self-explicated approaches only 24 attribute-level ratings [41]. Choicebased conjoint methods typically required greater effort, for instance in [21] with 12 choice sets containing 3 products each. Predictive accuracy was computed with differently sized and constructed choice sets, ranging from four [21,41] to twelve [65], which brings random FCHR to between 25% and 8.33%, and ratings were given on different scales (e.g. 4-point scales in [65], 100-point scale in [48]). Overall, our results for <sup>fi</sup>rst-choice hit rate – 66.7% (linear) and 56% (exponential) – fall within the bounds of previously attained accuracy values (35.5% to 74%); rank correlations are slightly worse. Bearing in mind that the best-performing methods are variants of conjoint analysis and thus cognitively very challenging and not easily applicable for repeated measurement, our low-effort approach performed very well.

<table><tr><td rowspan="5">Main experiment</td><td rowspan="2"></td><td>Task A</td><td>Task B</td><td>Task C</td><td>Task D</td></tr><tr><td>Screening</td><td>Evaluation</td><td>Utility exchange</td><td>Recommendation set evaluation</td></tr><tr><td>Linear SAU functions</td><td rowspan="3">Define aspiration levels</td><td>Define attribute weights ...</td><td rowspan="3">Specify WTP for modified version of best recommended product</td><td rowspan="3">Rate top ten recommended products and specify WTPs</td></tr><tr><td>Exponential SAU functions</td><td>... and rate average attribute levels</td></tr><tr><td>Free SAU functions</td><td>... and rate 5 levels for each attribute</td></tr></table>

Fig. 3. Research procedure.

Surprisingly, <sup>fi</sup>rst-choice hit rate was higher in the linear treatment and, on average, participants in the linear treatment rated the top 10 recommended products higher although the exponential system predicted product ranks beyond <sup>fi</sup>rst place better. The exponential system produced slightly higher correlations between product ranks and participant ratings.<sup>7</sup> One possible explanation might be the fact that specifying exponential SAU functions is cognitively more complex and leads to higher error levels than does specifying linear functions. This supposition is supported by our system usage log data: participants in the exponential treatment spent on average 10% more time on specifying their preferences than participants in the linear treatment.

Based on the <sup>fi</sup>ve attribute levels for which participants speci<sup>fi</sup>ed preferences in the supplementary experiment, we computed piecewise linear SAU functions to assess preference <sup>fi</sup>t.<sup>8</sup> Although most <sup>fl</sup>exible, utility accuracy of the “free” speci<sup>fi</sup>cation of SAU functions was below the accuracy of both linear and exponential utility functions (Table 5).

## 5.3. Willingness-to-pay accuracy

For the top 10 products, participants speci<sup>fi</sup>ed their WTP as a range and our systems estimated each participant's WTP as a range. We assume that both WTP ranges follow a truncated normal distribution [68] with $\mathcal { N } \Big ( W T P ^ { i n d . } , \sigma , W T P ^ { f l o o r } , W T P ^ { c e i l } \Big )$ . If a participant's WTP is estimated accurately, its range must be within the stated WTP range (see overlapping area in Fig. 4).

We computed the percentage of the estimated WTP range within the stated WTP range as:

$$
\begin{array}{r l} \text { Accuracy } & = F \left(W T P _ {\text { direct }} ^ {\text { ceil }}, W T P _ {\text { est. }} ^ {\text { ind. }}, \sigma_ {\text { est. }}, W T P _ {\text { est. }} ^ {\text { floor }}, W T P _ {\text { est. }} ^ {\text { ceil }}\right) \\ & - F \left(W T P _ {\text { direct }} ^ {\text { floor }}, W T P _ {\text { est. }} ^ {\text { ind. }}, \sigma_ {\text { est. }}, W T P _ {\text { est. }} ^ {\text { floor }}, W T P _ {\text { est. }} ^ {\text { ceil }}\right) \end{array}\tag{10}
$$

with

$$
\begin{array}{l} F \left(W T P _ {\text {direct}} ^ {\pi}, W T P _ {\text {est.}} ^ {\text {ind.}}, \sigma_ {\text {est.}}, W T P _ {\text {est.}} ^ {\text {floor}}, W T P _ {\text {est.}} ^ {\text {ceil}}\right) \\ = \frac {\phi \left(\frac {W T P _ {\text {direct}} ^ {\pi} - W T P _ {\text {est.}} ^ {\text {ind.}}}{\sigma_ {\text {est.}}}\right) - \phi \left(\frac {W T P _ {\text {est.}} ^ {\text {floor}} - W T P _ {\text {est.}} ^ {\text {ind.}}}{\sigma_ {\text {est.}}}\right)}{\phi \left(\frac {W T P _ {\text {est.}} ^ {\text {ceil}} - W T P _ {\text {est.}} ^ {\text {ind.}}}{\sigma_ {\text {est.}}}\right) - \phi \left(\frac {W T P _ {\text {est.}} ^ {\text {floor}} - W T P _ {\text {est.}} ^ {\text {ind.}}}{\sigma_ {\text {est.}}}\right)} \end{array}\tag{11}
$$

where $\sigma _ { e s t . }$ $( W T P _ { e s t . } ^ { c e i l } - W T P _ { e s t . } ^ { f l o o r } ) _ { . }$ /s and ϕ is the cumulative distribution function of $\mathcal { N } \Big ( W T P ^ { i n d . } , \sigma , W T P ^ { f l o o r } , W T P ^ { c e i l } \Big )$ . We used 10 variations of s (2, 4, 6, 8, 10, 12, 14, 16, 18, 20).

WTP accuracy was much higher in the linear treatment than in the exponential treatment (Fig. 5). This result is due to the higher <sup>fi</sup>rstchoice hit rate in the linear treatment, which indicates that the product with the highest expected utility was identical with product perceived to be the best by a participant more frequently. We used variants of the products with the highest expected utilities to estimate a participant's WTP for all products (Section 3). WTP accuracy for the supplementary experiment was much worse than for either treatment in the main experiment at values between 13.04% and 15.52%.

We also found evidence that, on average, estimated WTP was lower than stated WTP in both treatments. For <sup>fl</sup>oor WTP, differences between estimated and stated indifference WTP were larger in the exponential

## Table 3

Elicited utility parameters (minimum = 0, maximum = 1).

<table><tr><td rowspan="3">Attribute</td><td colspan="2">Linear</td><td colspan="4">Exponential</td></tr><tr><td colspan="2">Weights</td><td colspan="2">Weights</td><td colspan="2"> $u_{i}(x_{i}^{average})$ </td></tr><tr><td>Mean</td><td>SD</td><td>Mean</td><td>SD</td><td>Mean</td><td>SD</td></tr><tr><td>Photo resolution</td><td>0.789</td><td>0.193</td><td>0.736</td><td>0.229</td><td>0.670</td><td>0.158</td></tr><tr><td>Zoom factor</td><td>0.611</td><td>0.267</td><td>0.632</td><td>0.157</td><td>0.662</td><td>0.178</td></tr><tr><td>Size</td><td>0.586</td><td>0.266</td><td>0.484</td><td>0.264</td><td>0.550</td><td>0.212</td></tr><tr><td>Display size</td><td>0.448</td><td>0.278</td><td>0.432</td><td>0.225</td><td>0.638</td><td>0.147</td></tr><tr><td>Video resolution</td><td>0.448</td><td>0.287</td><td>0.472</td><td>0.281</td><td>0.626</td><td>0.159</td></tr><tr><td>Settings</td><td>0.595</td><td>0.241</td><td>0.544</td><td>0.252</td><td>0.542</td><td>0.142</td></tr><tr><td>Photosensitivity</td><td>0.650</td><td>0.255</td><td>0.714</td><td>0.175</td><td>0.568</td><td>0.158</td></tr><tr><td>Price</td><td>0.714</td><td>0.222</td><td>0.720</td><td>0.257</td><td>0.582</td><td>0.199</td></tr></table>

Table 4  
Supplementary experiment: percentage of participants' SAU shapes.

<table><tr><td>Attribute</td><td>Monotonously increasing</td><td>U-shaped</td><td>Other shape</td></tr><tr><td>Photo resolution</td><td>81.58</td><td>13.16</td><td>5.26</td></tr><tr><td>Zoom factor</td><td>71.05</td><td>23.68</td><td>5.27</td></tr><tr><td>Size</td><td>23.68</td><td>76.32</td><td>0.00</td></tr><tr><td>Display size</td><td>76.32</td><td>21.05</td><td>2.63</td></tr><tr><td>Video resolution</td><td>86.84</td><td>13.16</td><td>0.00</td></tr><tr><td>Settings</td><td>42.11</td><td>55.26</td><td>2.63</td></tr><tr><td>Photosensitivity</td><td>84.21</td><td>10.53</td><td>5.26</td></tr><tr><td>Price</td><td>52.63</td><td>36.84</td><td>10.53</td></tr></table>

Bold values indicate the shape the majority of consumers has speci<sup>fi</sup>ed.

treatment. For ceiling WTP, average differences were virtually identical in both treatments. In summary, stated WTP was underestimated in both treatments, and the exponential system was more prone to underestimation than the linear system. Identical utility thresholds $\tau _ { j }$ in both treatments $( p = 0 . 5 9 5 )$ ) and identical attribute weights $w _ { i }$ (see Table 3) indicate that the utility parameters $( a _ { i } , b _ { i }$ and $c _ { i } )$ of the exponential SAU functions were subject to a higher estimation error than the utility parameters (a and $b _ { i } )$ of the linear SAU functions.<sup>9</sup>

Logit regressions showed that WTP accuracy was not in<sup>fl</sup>uenced by any differences in participants' preference structures. We also controlled for effects of demographic factors, e-shop usage and system perception on accuracy but found no signi<sup>fi</sup>cant differences between treatments $( p > 0 . 1 )$ ).

Linear system WTP estimates outperformed exponential system WTP estimates in terms of correlation between estimated WTP and stated WTP. Indifference and ceiling WTP were estimated accurately by the linear system, but predictions for <sup>fl</sup>oor WTP were less accurate than those of the exponential system (Table 6). Again, the supplementary experiment results show that piecewise linear (i.e. free) SAU functions lead to less rather than more accurate WTP estimates.

Compared to most other WTP estimation methods, WTP accuracy was outstanding with correlations of nearly 50% in both groups in the main experiment. Prior studies report correlations between 10% and 21% for choice-based conjoint analysis and correlations of 33% to 42% for adapted choice-based conjoint analysis [21], and correlations of 15% to 43% for augmented conjoint analysis [48]. We conclude that our recommendation systems estimated WTP as accurately as or better than established methods.

## 6. Implications

Knowledge about a consumer's utility threshold and willingness to pay makes it possible to compute revenue-maximizing market prices and pro<sup>fi</sup>t-maximizing individual product con<sup>fi</sup>gurations. We discuss both practical implications in the following subsections.

## 6.1. Pricing

The WTP estimates of our proposed utility-based recommendation systems can be used to compute revenue-maximizing market prices. To compare the effect of both treatments on revenue, we followed a four-step procedure. In the <sup>fi</sup>rst step, we extracted all products that had been rated in Task D (see Fig. 3) by at least 10 participants (32 out of 162) to obtain robust estimates for the demand functions. In the step $^ { 2 , }$ we estimated the demand function $d ( p )$ for each of these products. We used a logit model of the form $d ( p ) = ( e ^ { \alpha { } + \beta p } ) / ( 1 + e ^ { \alpha { } + { } ^ { . } \bar { \beta } p } )$ [68,37,7], where p denotes participants' stated indifference price and $d ( p )$ is the ratio of participants willing to purchase the product at price p. In step $^ { 3 , }$ we predicted a revenue-optimal price $p ^ { * }$ <sub>prediction</sub> based on the WTP estimates. We selected the revenue-maximizing value (i.e. price multiplied with number of participants willing to purchase at this price) for WTP $\mathsf { a s p } _ { p r e d i c t i o n } ^ { * } .$ In step 4, we computed revenue as $r ( p ) = d ( p ) p$ for real mar-$p _ { r e a l }$ $p ^ { * }$ $d ( p )$ is the predicted probability that a consumer will purchase a product at price $p ,$ revenues were calculated for each consumer considering the product.

Table 5  
Utility accuracy compared to other studies.

<table><tr><td>Method</td><td>FCHR (%)</td><td>Rank correlation (%)</td><td>Study</td></tr><tr><td>RBCA</td><td>38.0–74.0</td><td>52.0–67.7</td><td>[8,66,28,67,20,65]</td></tr><tr><td>Adaptive RBCA</td><td>35.5–39.8</td><td>63.5</td><td>[65,41]</td></tr><tr><td>CBCA</td><td>38.0–67.0</td><td>-</td><td>[21,66,28,67]</td></tr><tr><td>Adaptive CBCA</td><td>56.5–58.5</td><td>-</td><td>[21]</td></tr><tr><td>Augmented CA</td><td>54.7–62.3</td><td>-</td><td>[48]</td></tr><tr><td>Self-explicated</td><td>43.6–44.0</td><td>53.7</td><td>[65,41]</td></tr><tr><td>Adaptive self-explicated</td><td>61.0</td><td>-</td><td>[41]</td></tr><tr><td>DR + linear SAU</td><td>66.7</td><td>47.7</td><td></td></tr><tr><td>DR + exponential SAU</td><td>56.0</td><td>49.4</td><td>This study</td></tr><tr><td>DR + free SAU</td><td>36.1</td><td>41.0</td><td></td></tr></table>

FCHR = First choice hit rate.  
CBCA = Choice-based conjoint analysis; RBCA = Ranking-based conjoint analysis.  
CA = Conjoint analysis.  
DR = Direct rating.

For each estimated demand function $d ( p )$ , we conducted a likelihood-ratio test, computed Nagelkerke's $R ^ { 2 }$ and checked whether the function was monotonously decreasing. All estimated demand functions were monotonously decreasing and <sup>fi</sup>tted our data well with signi<sup>fi</sup>cant likelihood-ratio tests $( p < 0 . 0 5 )$ ). On average Nagelkerke's $R ^ { 2 }$ was 69.73% $\mathrm { ( S D ~ = ~ 5 . 2 6 \% ) }$ indicating validly estimated demand functions.

We found that, on average, $p _ { \ p r e d i c t i o n } ^ { * }$ was signi<sup>fi</sup>cantly lower than the market price $p _ { r e a l }$ for both treatments. This is not surprising considering that both treatments underestimated stated WTP. Still, market prices calculated based on the WTP estimates of either system led to an increase in revenue in all but one case (Table 7).

![](/api/attachments/FJ4E5VCA/fulltext/images/56395f3cf79ad699607e035d7fdb9c21093a06adbe88eeb23424615f615d18c3.jpg)  
Fig. 4. WTP density functions.

![](/api/attachments/FJ4E5VCA/fulltext/images/e7547d3cdcda483e8d16655fbd54290480bd3436eb0ee9d50552aa47f944f9f8.jpg)  
Fig. 5. WTP accuracy.

Table 6  
WTP correlation (in %).

<table><tr><td>WTP point</td><td>Linear</td><td>Exponential</td><td>Free</td></tr><tr><td>Floor</td><td>41.51</td><td>44.54</td><td>40.25</td></tr><tr><td>Indifference</td><td>50.38</td><td>47.33</td><td>44.59</td></tr><tr><td>Ceiling</td><td>67.48</td><td>44.94</td><td>41.51</td></tr></table>

Bold values indicate the system with the higher WTP correlation (i.e. more accurate WTP prediction).

Increase in revenue is highest when calculated based on linear system indifference WTP estimates. As a reference, we computed maximal revenue improvements based on the estimated demand functions d(p) and found a maximal improvement of 18.35%. Although WTP accuracy was only moderate, WTP estimates were accurate enough for improving pricing strategies.

## 6.2. Special offers

Establishing new market prices is often impossible due to high price transparency, especially in online markets. However, knowledge about a consumer's willingness to pay and utility threshold can be employed to create individually optimal and pro<sup>fi</sup>t-optimal product con<sup>fi</sup>gurations (e.g. digital cameras or racing bikes) or special offers (Table 8).

Consider a consumer who is planning to purchase a new notebook and has recently used our utility-based recommendation system to search for attractive products. Based on the elicited utility functions for processor speed $( w _ { i } = 6 \mathrm { ~ a n d ~ } u _ { i } ( x _ { i } ) = - 1 . 2 5 + 0 . 6 2 5 x _ { i } )$ , memory size $( w _ { i } = 5$ and $u _ { i } ( x _ { i } ) = - 0 . 1 4 3 + 0 . 0 7 1 x _ { i } )$ , HDD size $( w _ { i } = 7$ and $u _ { i } ( x _ { i } ) = - 0 . 3 3 3 + 0 . 0 0 1 3 x _ { i } )$ and price $( w _ { i } = 8$ and $u _ { i } ( x _ { i } ) = 1 . 6 6 7 \mathrm { ~ - ~ }$ 0.0017x ), we can compute each notebook's utility.

Let us assume that the retailer offers a notebook X with 2.8 GHz processor speed, 4 GB memory size and 500 GB HDD for a regular price of 600 EUR. We further assume that the retailer has purchased this notebook for 450 EUR. Because its utility $( U ( X ) = 1 1 . 1 )$ lies below the consumer's utility threshold $( \tau _ { j } = 1 2 . 0 )$ , she will not be tempted to buy it. If the retailer wishes to attract this particular consumer, they might consider giving her a special offer applying a price discrimination strategy. In this case, the retailer can realize a pro<sup>fi</sup>t of 83 EUR, since the consumer has a willingness to pay of $W T P _ { X } = 5 3 3 .$ . Alternatively, the retailer might offer her one of the three other notebooks (notebooks A, B, and C in Table 8). Assuming that prices for A, B, and C are identical, notebook A is most attractive from the retailer's point of view because its procurement costs are lowest. However, notebook C leads to the highest utility improvement for our consumer. In other words, our consumer has the highest willingness to pay (701 Euro) for product $C \left( W T P _ { A } = \right.$ 644 Euro and $W T P _ { B } = 6 3 8 \mathrm { E u r o } )$ . Selling notebook C at 701 Euro will maximize the retailer's pro<sup>fi</sup>t (181 Euro).

## 7. Summary and future research

Our proposed recommendation system generates real-time data on consumer purchasing behavior, especially consumers' WTP, which are the basis for many models of market share estimation, pricing or product design. Because such data are (theoretically) easy to collect online, the increasing popularity of e-commerce has led to renewed interest in developing methods for estimating consumers' preferences and WTP in operations research [6,69,37,21]. Speci<sup>fi</sup>cally, a low-effort method for repeated measurements of consumers' WTP and attribute-level utilities is needed. Our approach is a promising step towards the development of such a method, extending utility-based recommendation systems.

Table 7  
Average revenue improvement with WTP estimates (in %).

<table><tr><td>Point in estimated WTP-range</td><td>Linear system</td><td>Exponential system</td></tr><tr><td>Floor WTP</td><td>+1.87</td><td>-5.57</td></tr><tr><td>Indifference WTP</td><td>+6.05</td><td>+1.53</td></tr><tr><td>Ceil WTP</td><td>+1.61</td><td>+2.78</td></tr></table>

Bold values indicate the system with the highest revenue improvement

Table 8  
Special offer opportunities.

<table><tr><td>Notebook</td><td>Processor in GHz</td><td>Memory in GB</td><td>HDD in GB</td><td>Procurement costs in EUR</td></tr><tr><td>A</td><td>3.2</td><td>4</td><td>500</td><td>500</td></tr><tr><td>B</td><td>2.8</td><td>8</td><td>500</td><td>550</td></tr><tr><td>C</td><td>2.8</td><td>4</td><td>750</td><td>520</td></tr></table>

The empirical evaluation shows that our proposed recommendation system predicts consumers' utility functions and, ultimately, their WTP with high accuracy. Considering that prior studies which reported similar levels of accuracy used more complex and cognitively exhausting measurement methods (e.g. choice-based or ranking-based conjoint analysis), our approach performed very well. Our results indicate that, contrary to prior suppositions, linear SAU functions are better suited for estimating WTP. Exponential SAU functions provide better approximations of consumers' preference structures and are therefore better suited for predicting product ranks. That overall utility accuracy for exponential functions is lower than for linear functions, although SAU functions were predominantly concave, suggests that more complex and therefore challenging methods lead to higher error levels in SAU function speci<sup>fi</sup>cation, which then accumulate in the overall utility function. This supposition is supported by the fact that complex conjoint analysis methods often do not attain much higher accuracy levels than simpler approaches although they too model utility at the attribute level. We suggest that for utility estimation, other approaches are as well suited as ours, but for combined individual utility and WTP estimation, our approach seems to perform above average.

Our research is subject to some limitations. First, our approach is designed for products with at least ordinal attributes for which it is possible to estimate reliable SAU functions, not for experience goods with nominal attributes such as “design” or “color”. Second, as shown in our supplementary experiment, SAU functions can be of (inverted) U-shape if consumers think about trade-offs between two attributes during the evaluation of one attribute (e.g. between “ease of transportation” and “fragility” when evaluating the attribute “size”). Exponential approximation of SAU functions was particularly robust when consumers did not consider within-attribute trade-offs during evaluation. Splitting multi-dimensional attributes into atomic attributes would likely improve accuracy and reduce effort. Third, the accuracy of utility estimates on the product level was only slightly better in the exponential system than in the linear system although preference structure (SAU functions) was approximated much better with exponential functions. It is possible that the 10-point scale we used to determine SAU function curvature was not precise enough, resulting in small discrepancies at the SAU function level (see Fig. A.6) which might then have added up to a larger discrepancy between estimated and actual, or perceived, utilities at the product level. Fourth, user preferences may be in<sup>fl</sup>uenced by exogenous factors like the decision support system used for measuring utility functions and WTP [70]. Our proposed approach for estimating exponential utility functions is interactive, requiring user input for several parameters, and may affect user preference building. The extent to which and the circumstances under which decision support systems change users' preferences are as yet not fully understood and provide an avenue for future research.

The practical implications from our <sup>fi</sup>ndings are threefold. First, it is relatively easy to use and generates good recommendations. These results suggest that online consumers could bene<sup>fi</sup>t from using it in their purchasing process, saving effort in the process of <sup>fi</sup>nding attractive products. Since multi-dimensional attributes make utility estimation more dif<sup>fi</sup>cult and increase consumer effort without improving utility or WTP estimates, designers of utility-based decision support systems ought to make sure their systems are based on atomic attributes only. Second, online retailers could easily extend existing utilitybased recommendation systems, such as the Dell Computer Advisor, to include WTP estimation. As illustrated in Section 6, retailers could use this information as a basis for a number of business decisions, e.g. product pricing. Third, online retailers could generate new revenue streams by selling the recommendation data to product manufacturers, who can then determine individual pro<sup>fi</sup>t-maximizing product con<sup>fi</sup>gurations more easily. Open questions that remain in this area are the degree of consumer acceptance and the pro<sup>fi</sup>tability of WTP-based pricing strategies. Both still need to be evaluated in <sup>fi</sup>eld studies to shed more light on consumers' reactions and decision processes in real-life situations.

Research into collaborative recommendation systems could pro<sup>fi</sup>t from our approach. Currently, one of the most commonly used collaborative recommendation algorithms is matrix factorization (e.g. [71]), which helps identify latent product features that contribute most to product utility. However, these features are generally not identical to product attributes, which makes it more dif<sup>fi</sup>cult to use the information in business decisions and to compute WTP. Combining our approach, which produces data on the individual level, with collaborative data on the user group level could generate better insights into the composition of latent features and preference differences between consumers. Conversely, integrating collaborative recommendation system data in our approach may further increase recommendation quality and decrease the level of consumer effort during the purchasing process, especially if consumer preferences can be estimated to a satisfactory degree during the speci<sup>fi</sup>cation process and recommendations provided at an early stage.

## Acknowledgment

The authors thank Christian Schlereth for his insightful comments. The authors also thank the editor and two anonymous reviewers for their helpful comments and suggestions.

## Appendix A. Proof for Eqs. (3) and (4)

Exponential utility functions consist of three parameters. We hence need three points of such a function for estimation. We suggest using the best, the worst and the average attribute level and the utility values of these levels to estimate an exponential utility function. Assuming that both, the attribute levels as well as the utility values of an attribute, are scaled to [0; 1], the <sup>fi</sup>rst two points are given by

$$
P _ {1} \left(x _ {i} ^ {\text { worst }}; u _ {i} \left(x _ {i} ^ {\text { worst }}\right)\right) = (0; 0)\tag{A.1}
$$

$$
P _ {2} \left(x _ {i} ^ {\text { best }}; u _ {i} \left(x _ {i} ^ {\text { best }}\right)\right) = (1; 1)\tag{A.2}
$$

The utility of the third point is speci<sup>fi</sup>ed by the consumer on a 11-point scale (see Fig. 2) and re-scaled to [0; 1]. The third point is hence given as:

$$
P _ {3} (x _ {i} ^ {\text { average }}; u _ {i} (x _ {i} ^ {\text { average }})) = (0. 5; u _ {i} (x _ {i} ^ {\text { average }})).\tag{A.3}
$$

Based on these three points, we can de<sup>fi</sup>ne the following three equations that can be solved with Gaussian elimination:

$$
0 = a _ {i} - b _ {i},\tag{A.4}
$$

$$
1 = a _ {i} - b _ {i} e ^ {c _ {i}},\tag{A.5}
$$

$$
u _ {i} (x _ {i} ^ {\text { average }}) = a _ {i} - b _ {i} e ^ {0. 5 c _ {i}}.\tag{A.6}
$$

Eq. A.4 indicates that $a _ { i } = b _ { i }$ whereas Eq. A.5 indicates that $\begin{array} { r } { a _ { i } = \frac { 1 } { 1 - e ^ { c _ { i } } } . } \end{array}$ By substituting $a _ { i }$ and $b _ { i }$ in Eq. (A.6) we get:

$$
u _ {i} \left(x _ {i} ^ {\text { average }}\right) = \frac {1 - e ^ {0 . 5 c _ {i}}}{1 - e ^ {c _ {i}}}.\tag{A.7}
$$

Next, we can substitute $e ^ { c _ { i } }$ by $z ^ { 2 }$ with $z \ge 0$ to get a simple quadratic equation:

$$
0 = u _ {i} (x _ {i} ^ {\text { average }}) z ^ {2} - z - u _ {i} (x _ {i} ^ {\text { average }}) + 1.\tag{A.8}
$$

Isolating z, gives:

$$
z _ {1 / 2} = \frac {1 \pm \sqrt {1 - 4 u _ {i} (x _ {i} ^ {\text { average }}) (1 - u _ {i} (x _ {i} ^ {\text { average }}))}}{2 u _ {i} (x _ {i} ^ {\text { average }})}.\tag{A.9}
$$

$\operatorname { I f } u _ { i } ( x _ { i } ^ { a \nu e r a g e } ) = 0 . 5$ we have $z _ { 1 } = z _ { 2 } = 1$ and therefore $c _ { i } = l n ( z ^ { 2 } ) = 0 .$ If $u _ { i } ( x _ { i } ^ { a v e r a g e } > 0 . 5 )$ then $. z _ { 2 }$ is the only non-negative solution whereas only $z _ { 1 }$ is a non-negative solution if $u _ { i } ( x _ { i } ^ { a v e r a g e } ) < 0 . 5$

Based on the rating r of the average attribute leve $x _ { i } ^ { a v e r a g e }$ , an attribute utility function is de<sup>fi</sup>ned as one of the functions given in Fig. A.6.

![](/api/attachments/FJ4E5VCA/fulltext/images/eba0da219b99a87bd50f95079f0894a368be59027dfca53df7ec66fc954027d1.jpg)  
Fig. A.6. Possible attribute utility functions.

## References

[1] C. Schlereth, B. Skiera, Measurement of consumer preferences for bucket pricing plans with different service attributes, International Journal of Research in Marketing 29 (2) (2012) 167–180

[2] J. Wu, L. Li, L.D. Xu, A randomized pricing decision support system in electronic commerce, Decision Support Systems 58 (2014) 43–52.

[3] K. Jedidi, R. Kohli, W. DeSarbo, Consideration sets in conjoint analysis, Journal of Marketing Research 33 (3)(1996) 364-372

[4] C. Druehl, G. Schmidt, G. Souza, The optimal pace of product updates, European Journal of Operational Research 192 (2) (2009) 621–633.

[5] T. Coltman, J. Gattorna, S. Whiting, Realigning service operations strategy at DHL Express, Interfaces 40 (3) (2010) 175–183.

[6] P. Rusmevichientong, Z.-J. Shen, D. Shmoys, Dynamic assortment optimization with a multinomial logit choice model and capacity constraint, Operations Research 58 (6) (2010) 1666–1680.

[7] K. Wertenbroch, B. Skiera, Measuring consumers' willingness to pay at the point of purchase, Journal of Marketing Research 39 (2) (2002) 228–241.

[8] A. De Bruyn, J. Liechty, E. Huizingh, G. Lilien, Offering online recommendations with minimum customer input through conioint-based decision aids Marketing Science 27 (3) (2008) 443–460.

[9] S. Huang, Designing utility-based recommender systems for e-commerce: evaluation of preference-elicitation methods, Electronic Commerce Research and Applications 10 (4) (2011) 398–407.

[10] A. Denguir-Rekik, J. Montmain, G. Mauris, A possibilistic-valued multi-criteria decision-making support for marketing activities in e-commerce: feedback based diagnosis system, European Journal of Operational Research 195 (3) (2009) 876–888.

[11] J. Butler, D. Morrice, P. Mullarkey, A multiple attribute utility theory approach to ranking and selection, Management Science 47 (6) (2001) 800–816.

[12] A. Abbas, D. Bell, One-switch conditions for multiattribute utility functions, Operations Research 60 (5) (2012) 1199–1212.

[13] C. Harvey, Conditions on risk attitude for a single attribute, Management Science 27 (2) (1981) 190–203.

[14] K. van Ittersum, J. Pennings, Attribute-value functions as global interpretations of attribute importance, Organizational Behavior and Human Decision Processes 119 (1) (2012) 89–102.

[15] P. Green, A. Krieger, Y. Wind, Thirty years of conjoint analysis: re<sup>fl</sup>ections and prospects, Interfaces 31 (3) (2001) 56–73.

[16] S. Scholz, M. Meissner, R. Decker, Measuring consumer preferences for complex products: a compositional approach based on paired comparisons, Journal of Marketing Research 47 (4) (2010) 685–698.

[17] B. Xiao, I. Benbasat, E-commerce product recommendation agents: use, characteristics, and impact, MIS Quarterly 31 (1) (2007) 137–209.

[18] A. Ansari, S. Essegaier, R. Kohli, Internet recommendation systems, Journal of Marketing Research 37 (3) (2000) 363–375.

[19] H.-N. Kim, A. El-Saddik, G.-S. Jo, Collaborative error-re<sup>fl</sup>ected models for cold-start recommender systems, Decision Support Systems 51 (3) (2011) 519–531.

[20] M. Scholz, V. Dorner, Estimating optimal recommendation set sizes for individual consumers, Proceedings of the 33rd International Conference on Information Systems, 2012.

[21] S. Gensler, O. Hinz, B. Skiera, S. Theysohn, Willingness-to-pay estimation with choice-based conjoint analysis: addressing extreme response behavior with individually adapted designs, European Journal of Operational Research 219 (2) (2012) 368–378.

[22] W. DeSarbo, V. Ramaswamy, S. Cohen, Market segmentation with choice-based conjoint analysis, Marketing Letters 6 (2) (1995) 137–147.

[23] M.-C. Yu, M. Goh, H.-C. Lin, Fuzzy multi-objective vendor selection under lean procurement, European Journal of Operational Research 219 (2) (2012) 305-311.

[24] V.B. Kreng, C.-Y. Wu, Evaluation of knowledge portal development tools using a fuzzy AHP approach: the case of Taiwanese stone industry, European Journal of Operational Research 176 (3) (2007) 1795–1810.

[25] D. Gensch, E. Soo<sup>fi</sup>, A minimum discrimination information estimation of multiattribute market share models, Marketing Science 11 (1) (1992) 54–63.

[26] J. Corner, J. Buchanan, Capturing decision maker preference: experimental comparison of decision analysis and MCDM techniques, European Journal of Operational Research 98 (1) (1997) 85–97.

[27] M. Pöyhönen, R. Hämäläinen, On the convergence of multiattribute weighting methods, European Journal of Operational Research 129 (3) (2001) 569–585.

[28] W. Moore, A cross-validity comparison of ratings-based and choice-based conjoint analysis models, International Journal of Research in Marketing 21 (3) (2004) 299-312.

[29] Y. Cao, Y. Li, An intelligent fuzzy-based recommendation system for consumer electronic products. Expert Systems with Applications 33 (1) (2007) 230–240.

[30] C. Theetranont, P. Haddawy, D. Krairit, Integrating visualization and multi-attribute utility theory for online product selection, International Journal of Information Technology & Decision Making 6 (4) (2007) 723–750.

[31] P. Bottomley, J. Doyle, R. Green, Testing the reliability of weight elicitation methods: direct rating versus point allocation, Journal of Marketing Research 37 (4) (2000) 508–513.

[32] J. Pfeiffer, M. Scholz, A low-effort recommendation system with high accuracy: A new approach with ranked pareto-fronts, Business & Information Systems Engineering 5 (6).

[33] G. Häubl, V. Trifts, Consumer decision making in online shopping environments: the effects of interactive decision aids, Marketing Science 19 (1) (2000) 4–21.

[34] J. Butler, J. Dyer, J. Jia, K. Tomak, Enabling e-transactions with multi-attribute preference models, European Journal of Operational Research 186 (2) (2008) 748–765.

[35] R. Dawes, The robust beauty of improper linear models in decision making, American Psychologist 34 (7) (1979) 571–582.

[36] J. Butler, J. Jia, J. Dyer, Simulation techniques for the sensitivity analysis of multicriteria decision models, European Journal of Operational Research 103 (3) (1997) 531–545.

[37] K. Miller, R. Hofstetter, H. Krohmer, Z. Zhang, How should consumers' willingness to pay be measured? An empirical comparison of state-of-the-art approaches, Journal of Marketing Research 48 (1) (2011) 172–184.

[38] C. Barrot, S. Albers, B. Skiera, B. Schäfers, Vickrey vs. ebay: why second-price sealedbid auctions lead to more realistic price-demand functions International Journal of Electronic Commerce 14 (4) (2010) 7-38

[39] M.T. Jones, Bidding fever in ebay auctions of amazon.com gift certi<sup>fi</sup>cates, Economics Letters 113 (1) (2011) 5–7.

[40] T.Y. Chan, V. Kadiyali, Y.-H. Park, Willingness to pay and competition in online auctions, Journal of Marketing Research 44 (2) (2007) 324–333.

[41] O. Netzer, V. Srinivasan, Adaptive self-explication of multi-attribute preferences, Journal of Marketing Research 48 (1) (2011) 140–156.

[42] P.S.H. Lee<sup>fl</sup>ang, D.R. Wittink, Diagnosing competitive reactions using (aggregated) scanner data, International Journal of Research in Marketing 9 (1) (1992) 39–57.

[43] W.A. Kamakura, G.J. Russell, Measuring brand value with scanner data, International Journal of Research in Marketing 10 (1) (1993) 9–22

[44] Y.-H. Park, M. Ding, V.R. Rao, Eliciting preference for complex products: a web-based upgrading method, Journal of Marketing Research 45 (5) (2008) 562–574.

[45] K. Backhaus, R. Wilken, M. Voeth, C. Sichtmann, An empirical comparison of methods to measure willingness to pay by examining the hypothetical bias, International Journal of Market Research 47 (5) (2005) 543–562

[46] F. Voelckner, An empirical comparison of methods for measuring consumers' willingness to pay, Marketing Letters 17 (2) (2006) 137–149.

[47] J.J. Louviere, T. Islam, A comparison of importance weights and willingness-to-pay measures derived from choice-based conjoint, constant sum scales and best– worst scaling, Journal of Business Research 61 (9) (2008) 903–911.

[48] K. Jedidi, Z.J. Zhang, Augmenting conjoint analysis to estimate consumer reservation price, Management Science 48 (10) (2002) 1350–1368.

[49] S. Moorthy, B. Ratchford, D. Talukar, Consumer information search revisited: theory and empirical analysis, Journal of Consumer Research 23 (4) (1997) 263–277.

[50] J.S. Hammond, R.L. Keeney, H. Raiffa, Even swaps: a rational method for making trade-offs, Harvard Business Review 76 (2) (1998) 137–150.

[51] J. Mustajoki, R. Hämäläinen, Smart-swaps — a decision support system for multicriteria decision analysis with the even swaps method, Decision Support Systems 44 (1) (2007) 313–325.

[52] J. March, Rationality, ambiguity, and the engineering of choice, Bell Journal of Economics 9 (2) (1978) 587–608.

[53] T. Wang, R. Venkatesh, R. Chatterjee, Reservation price as a range: an incentivecompatible measurement approach, Journal of Marketing Research 44 (2) (2007) 200–213.

[54] C. Schlereth, C. Eckert, B. Skiera, Using discrete choice experiments to estimate willingness-to-pay intervals, Marketing Letters 23 (3) (2012) 761–776.

[55] P. Nelson, Information and consumer behavior, Journal of Political Economy 78 (2) (1970) 311–329.

[56] S. Mudambi, D. Schuff, What makes a helpful online review? A study of customer reviews on amazon.com, MIS Quarterly 34 (1) (2010) 185–200.

[57] W. Wang, I. Benbasat, Recommendation agents for electronic commerce: effects of explanation facilities on trusting beliefs, Journal of Management Information Systems 23 (4)(2007) 217–246

[58] M. Dewally, L. Ederington, Reputation, certi<sup>fi</sup>cation, warranties, and information as remedies for seller–buyer information asymmetries: lessons from the online comic book market, The Journal of Business 79 (2) (2006) 693–729.

[59] P. Bohm, J. Linden, J. Sonnengard, Eliciting reservation prices: Becker–Degroot– Marschak mechanisms, The Economic Journal 107 (443) (1997) 1079–1089.

[60] R. Meeds, Cognitive and attitudinal effects of technical advertising copy: the roles of gender, self-assessed and objective consumer knowledge, International Journal of Advertising 23 (3) (2004) 177–192.

[61] J. Payne, Task complexity and contingent processing in decision making: an information search and protocol analysis, Organizational Behavior and Human Performance 16 (2) (1976) 366–387.

[62] I. Hauser, B. Wernerfelt An evaluation cost model of consideration sets Journal of Consumer Research 16 (4)(1990) 393-408

[63] C. Gena. S. Weibelzahl. The adaptive web: methods and strategies of web personalization, Ch. Usability Engineering for the Adaptive Web, Springer, 2007. 720-762

[64] W. Isaacs, P. Senge, Overcoming limits to learning in computer-based learning environments, European Journal of Operational Research 59 (1) (1992) 183–196.

[65] P. Green, A. Krieger, M. Agarwal, A cross validation test of four models for quantifying multiattribute preferences, Marketing Letters 4 (4) (1993) 391–406

[66] E.V. Karniouchina, W.L. Moore, B. van der Rhee, R. Verma, Issues in the use of ratingsbased versus choice-based conjoint analysis in operations management research, European Journal of Operational Research 197 (1) (2009) 340–348.

[67] W. Moore, J. Gray-Lee, J. Louviere, A cross-validity comparison of ratings-based and choice-based conjoint analysis models, Marketing Letters 9 (2) (1998) 195–208.

[68] F. Dost, R. Wilken, Measuring willingness to pay as a range, revisited: When should we care? International Journal of Research in Marketing 29 (2) (2012) 148–166.

[69] A. Abbas, D. Bell, One-switch independence for multiattribute utility functions, Operations Research 59 (3) (2011) 764–771.

[70] G. Adomavicius, J.C. Bockstedt, S.P. Curley, J. Zhang, Do recommender systems manipulate consumer preferences? A study of anchoring effects, Information Systems Research 24 (4) (2013) 956–975.

[71] G. Yong, X. Hui, A. Tuzhilin, L. Qi, Cost-aware collaborative <sup>fi</sup>ltering for travel tour recommendations, ACM Transactions on Information Systems 32 (1).

Michael Scholz (1981) studied Information Systems at the Martin-Luther-University Halle Wittenberg with main focus on Software Engineering and Information Management. After receiving his diploma (equiv. to Masters degree) he started working as a Research Assistant at the Chair of Business Informatics II at the University of Passau. He received his Ph.D. in December 2009. Since May 2010 he is an Assistant Professor at the University of Passau. Michael's research has been published in journals such as Business & Information Systems Engineering (BISE) or Journal of Electronic Commerce Research (JECR) and in several conference proceedings. His research focuses on recommendation systems, customer reviews and electronic marketplaces.

Verena Dorner (1981) is a post-doc research assistant at the Chair of Business Informatics II at the University of Passau. She studied business administration at the University of Passau with majors in information systems and operations research and received her PhD in February 2012. Verena's research interests are focussed on consumer behavior and decision support in e-commerce, in particular the effects of recommendation systems and online consumer reviews. Her research has been published in Business & Information Systems Engineering (BISE) and in a number of conference proceedings, among them the International Conference on Information Systems (ICIS).

Markus Franz (1984) studied economics at the Johann Wolfgang Goethe-University of Frankfurt. The focus of his studies was on Marketing and Finance. In January of 2011 he <sup>fi</sup>nished university with a diploma in business administration. His <sup>fi</sup>nal thesis, “Visualizing product spaces in recommendation agents via correspondence analysis”, empirically investigates the in<sup>fl</sup>uence of graphical information provision on search performance and loyalty of recommendation system users. He gained practical experiences in the market research department of the Arcor AG & Co. KG. Since April 2011 he is staffed as Research Assistant at the Chair of Business Informatics especially Electronic Markets.

Oliver Hinz (1974) studied at the TU Darmstadt Business Administration and Information Systems with main focus on Marketing, Software Engineering and Computer Graphics. After receiving his diploma (equiv. to Masters degree) he worked several years for the Dresdner Bank as a consultant for business logic. Oliver started working as a Research Assistant in March 2004 at the Chair of Electronic Commerce and received his Ph.D. in October 2007. Oliver Hinz joined the Marshall School of Business (University of Southern California) as visiting scholar for 4 months and received the SinnerSchrader stipend (10.000 EUR) for young researcher for 2007. He has also been awarded with the dissertation prize of the Alcatel-Lucent-Stiftung 2008, the Erich-Gutenberg-Prize 2008 and the science prize “Retailing 2009” of the EHI Retail Institute. He is also the winner of the honorable Schmalenbach prize for young researchers in 2008. He supported the E-Finance Lab as Assistant Professor for E-Finance & Electronic Markets, joined the TU Darmstadt in April 2011 and heads the Chair of Information Systems | Electronic Markets. Oliver's research has been published or is forthcoming in journals like Information System Research (ISR), Management Information Systems Quarterly (MISQ), Journal of Marketing (JM), European Journal of Operational Research (EJOR), Journal of Management Information Systems (JMIS), Decision Support Systems (DSS), Journal of Business Research, Electronic Markets (EM), Business & Information Systems Engineering (BISE) and in a number of proceedings.
