---
otero_id: 6390
otero_key: "MMTD83BM"
title: "An Economic Analysis of Product Recommendation in the Presence of Quality and Taste-Match Heterogeneity"
authors: "Zhan (Michael) Shi; T. S. Raghu"
year: "2020"
journal: "Information Systems Research"
doi: "10.1287/isre.2019.0893"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
This article was downloaded by: [129.100.58.76] On: 13 June 2020, At: 06:06 Publisher: Institute for Operations Research and the Management Sciences (INFORMS) INFORMS is located in Maryland, USA

# Information Systems Research

![](/api/attachments/MMTD83BM/fulltext/images/303f329bb838ea61001880e6afdab4cb3de3672d2f1f499224ab0e4fc912992b.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

## An Economic Analysis of Product Recommendation in the Presence of Quality and Taste-Match Heterogeneity

Zhan (Michael) Shi, T. S. Raghu

To cite this article:

Zhan (Michael) Shi, T. S. Raghu (2020) An Economic Analysis of Product Recommendation in the Presence of Quality and Taste Match Heterogeneity. Information Systems Research

Published online in Articles in Advance 10 Jun 2020

https://doi.org/10.1287/isre.2019.0893

Full terms and conditions of use: https://pubsonline.informs.org/Publications/Librarians-Portal/PubsOnLine-Terms-and-Conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

Copyright © 2020, INFORMS

Please scroll down for article—it is on subsequent pages

## inferms

With 12,500 members from nearly 90 countries, INFORMS is the largest international association of operations research (O.R.) and analytics professionals and students. INFORMS provides unique networking and learning opportunities for individual professionals, and organizations of all types and sizes, to better understand and use O.R. and analytics tools and methods to transform strategic visions and achieve better outcomes.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# An Economic Analysis of Product Recommendation in the Presence of Quality and Taste-Match Heterogeneity

Zhan (Michael) Shi,<sup>a</sup> T. S. Raghu<sup>a</sup>

<sup>a</sup> Department of Information Systems, W. P. Carey School of Business, Arizona State University, Tempe, Arizona 8528 Contact: zmshi@asu.edu, https://orcid.org/0000-0002-2815-252X (Z(M)S); raghu.santanam@asu.edu, https://orcid.org/0000-0003-1071-6339 (TSR)

Received: October 26, 2017<sub>Revised:</sub> June Accepted: Published Online in Articles in Advance: June 10, 2020

https://doi.org/10.1287/isre.2019.089

Copyright:

Abstract. This paper investigates the strategy for product recommendation. Specifically, we analyze a platform-based market where consumers search and purchase products that potentially differ in quality. In addition, consumers have idiosyncratic tastes for a product, and the extent of this heterogeneity may vary from one product to another. In other words, there may be products with low taste dispersion (products for which there is less heterogeneity among consumers), as well as products with high taste dispersion. Our modeling framework elucidates how platform recommendation influences the market-level equi librium outcomes, thereby informing the optimal recommendation strategy. We find that the quality and taste-dispersion dimensions can interact to affect the overall effectiveness of product-recommendation strategies. Conditioning on taste dispersion, recommending high-quality products increases both producer profits and consumer surplus. Conditioning on quality, recommending high-taste-dispersion products may, however, increase or decrease producer profits, depending on the joint effect of profit margin and purchase probability. The direction of change in consumer surplus is also uncertain—recommending a high-taste-dispersion product is more likely to increase (decrease) consumer surplus if the quality is low (high). Importantly, we show that when the platform cannot discern product types, recommendation strategies based on observed price or sales signals cannot guarantee the optimal outcome in the general case.

History: Anand Gopal, Senior Editor; Sanjukta Smith, Associate Editor. Funding: Z. Shi received W. P. Carey School of Business Summer Research Grants 2018 and 2019. Supplemental Material: The online appendix is available at https://doi.org/10.1287/isre.2019.0893.

Keywords: platform recommendation • consumer search • market equilibrium • recommendation strategy • platform economics

## 1. Introduction

Consumers search and evaluate a large number of alternatives in crowded markets to buy the products that meet their specific needs. The success of products, especially new products, critically depends on consumer discovery during the search process (e.g., Goeree 2008, Brynjolfsson et al. 2011). To reduce the search burden, market platforms deploy product recommendations, which range from price- or sales-based recommendations to human-curated recommendations. Amazon’s “Best Sellers” page, for instance, features products with the highest sales in the past hour, while its “Interesting Finds”<sup>1</sup> site recommends product lists selected by in-house curators. Another example is Apple’s iOS App Store, where the platform publishes rankings of most-downloaded apps and highlights editor-curated lists such as “App of the Day,” “Game of the Day,” and featured new apps.<sup>2</sup>

The majority of the existing research on platform recommendation is focused on the accuracy of preference prediction (see survey in Adomavicius and Tuzhilin 2005, Ricci et al. 2011) or the effectiveness of recommendation at the individual product level (e.g., Senecal and Nantel 2004, Lin 2014). Although there are several papers that have investigated some broader market impacts of platform recommendation (e.g., Fleder and Hosanagar 2009 on sales diversity and Liang et al. 2019 on spillover to related products), to the best of our knowledge, there are no formal analyses of how the platform should select products for recommendation. This is the fundamental gap that motivates our present study. Answering this question requires an understanding of the equilibrium implications of platform recommendation at the market level. When the platform recommends a product, consumers are more likely to discover and purchase the recommended product. Everything else equal, the products that are not recommended would have less exposure and sales. Therefore, recommendation can be seen as a platform intervention that shifts (a portion of) consumer search effort and demand from the rest of the market to the recommended products. Hence, in deciding its recommendation strategy to optimize market-level outcomes, the platform should evaluate the trade-off between the potential gains for consumers and producers of the recommended products and the potential losses incurred on the nonrecommended products. This research focuses on analyzing the equilibrium market outcomes and the entailed trade-offs when the platform recommends different types of products. Specifically, we examine the following salient questions: (1) How will platform recommendation impact equilibrium consumer surplus and producer profits? (2) What type of products should the platform select for recommendation under different objectives? (3) Are the commonly used recommendation strategies based on price and sales optimal in terms of platformlevel outcomes?

We develop a model of platform-based market to systematically analyze the impact of platform recommendation on market equilibrium. Specifically, we consider a heterogeneous product market where the utility for the product is composed of a quality dimension that all consumers agree upon and a taste-match dimension that varies across consumers (following the product-differentiation literature, we henceforth use the terms vertical and horizontal dimensions for the two components). Consumers have incomplete information about the products, and they incur a search cost to learn the consumption utility and price for any given product. During the search process, consumers sample products sequentially and adopt a rational stopping rule. We progressively explore a set of scenarios where products differ in quality and/or taste match. In each scenario, we first consider the benchmark case where consumers sample products in a random order and derive the equilibrium condition. We then assume that platform recommendation exogenously alters the consumer search sequence by placing the recommended products at the top of the list and compare how producer profits and consumer surplus would change relative to the benchmark case when different types of products are selected for recommendation. The analysis thus yields the theoretically optimal recommendation strategy for the platform, provided it is able to discern product heterogeneity in quality and taste match. Using the results on optimal product selection as the basis for comparison, we then examine whether relying on the observed price or sales signals can help the platform to achieve the optimum when it cannot determine product types.

The main findings are as follows. First, if there is no systematic difference between products, platform recommendation has no aggregate effect on total producer profits and consumer surplus. Second, if products differ in their quality (i.e., when conditioning on taste dispersion), then recommending high-quality products can increase both producer profits and consumer surplus. Third, if products differ in the dispersion of consumer taste match (i.e., when conditioning on quality), then recommending high-taste-dispersion products may increase or decrease producer profits, depending on the joint effect of profit margin and purchase probability. The direction of change in consumer surplus is also uncertain—recommending a high-taste-dispersion product is more likely to increase (decrease) consumer surplus if the product quality is low (high). Remarkably, recommendation strategies based on price or sales will not guarantee optimum in the general case where heterogeneity exists in both the vertical and horizontal dimensions.

This research joins the literature that studies the market implications of platform recommendation Fleder and Hosanagar (2009) modeled how popularity based platform recommendation would influence con sumer choice at the micro level and used simulation to demonstrate that the effect of recommendation on product variety at the individual level and that at the platform level can be different. Based on the view-rank data of the camcorder section on Amazon, the numerical results of Kim et al. (2010) suggested that almost al consumers benefited from the platform’s collaborativefiltering-based product recommendation. Recently, Liang et al. (2019) examined the spillover effects of platform-provided editorial recommendation on related products. Although these papers examined various aspects of the market implications of platform recommendation, they did not focus on studying how the platform should choose products for recommendation. Our paper contributes to this emerging literature by providing a systematic analysis on the equilibrium im plications of platform recommendation. Our mode yields predictions on what types of products should be selected for optimizing specific market outcomes, and the analysis allows us to compare the different impli cations of product type- and popularity-based recommendation strategies, Our analytical framework draws upon the important prior work that models consumer search (e.g., Weitzman 1979, Perloff and Salop 1985. Wolinsky 1986. Anderson and Renault 1999 Armstrong et al. 2009). On top of the consumer-search framework, we analyze the market implications of platform recommendation. By explicitly considering product heterogeneity in the vertical and horizontal dimensions, we show that they have very different im plications on optimal platform recommendation strategy and demonstrate that optimality cannot always be guaranteed using observed price and sales signals.

## 2. Basic Model Setup

In this section, we introduce our modeling framework Our setup builds on the consumer search models of Wolinsky (1986) and Anderson and Renault (1999). Using the basic consumer-search framework, we will then, in the following sections, introduce platform recommendation into the model, analyze how it changes the market equilibrium, and discuss the strategic implications.

The basic model setup is as follows. Suppose $u _ { i j }$ is the utility that consumer i would get from consuming product $j ,$ and it is composed of two parts:

$$
u _ {i j} = v _ {j} + h _ {i j},\tag{1}
$$

where $v _ { j }$ is product $j ^ { \prime } \boldsymbol { \mathrm { s } }$ quality that is valued in common by all consumers, and $h _ { i j } ,$ , independently distributed across consumer–product pairs, captures the match between product $j ^ { \prime } \boldsymbol { \mathrm { s } }$ design and consumer $i ^ { \prime } \mathrm { s }$ idiosyncratic taste.<sup>3</sup> At price $p _ { j }$ for product $j ,$ consumer i’s net utility of choosing j is $u _ { i j } - p _ { j }$ . The range of $v _ { j }$ measures vertical heterogeneity across different products. For a particular $j ,$ the variance of $h _ { i j }$ over i measures the dispersion of product $j ^ { \prime } \mathbf { s }$ consumer taste match (in other words, to what extent different consumers’ preferences to product $j$ agree with each other). Thus, as illustrated in Figure 1, the distribution of consumer valuation of a product in the population is characterized by both its quality and the dispersion of its consumer taste match. These two factors will determine the products’ types when we discuss differentiated products in the following sections.

The product space on most market platforms is very large. For simplicity, we assume that there is an infinite number of products, and each consumer is looking to purchase at most one product. Additionally, consumers must incur a search cost of s to discover the consumption utility and price for any given product available in the market. The search cost in the model encompasses the total time and cognitive cost incurred by consumers in finding and evaluating a product. Consumers are assumed to sample products sequentially: At any given time, consumers can either purchase a product they have already learned about, continue searching by sampling another product (and paying the search cost), or leave the market without purchase.<sup>4</sup>

The model timing is as follows. The producers set the price given product quality. Then, consumers search products to purchase. We assume that consumers know the distributions of $v _ { j }$ and $h _ { i j }$ in the market, but not the specific $v _ { j }$ and $h _ { i j }$ for any product $j . ^ { 5 }$ Producers maximize their expected profit, and consumers maximize their expected surplus. Without loss of generality, we further assume that the number of consumers is one,<sup>6</sup> and the marginal cost of producing one unit of product is the same for all products, which we normalize to zero.

In Sections 3–5, we derive the model equilibrium and analyze the product-recommendation strategies under three different assumptions regarding product heterogeneity in the market. We start from the setting where the products are ex ante homogeneous in the sense that they have the same quality and taste-match dispersion (Section 3), and then gradually increase the complexity to allow for product differentiation, first only in quality (Section 4) and then in both quality and taste-match dispersion (Section 5). Figure 2 shows th roadmap. For each setting, we first analyze the case where consumers sample products in a random order. The equilibrium condition of this case serves as the benchmark for comparison. We subsequently consider scenarios where the consumer search sequence is exogenously changed by different platform-recommendation strategies, including product-type-based recommendation and sales- or price-based recommendation, and examine the resulting implications on market equilibrium. We particularly focus on characterizing the effects on equilibrium producer profits and consumer surplus. Producer profit is defined as producer revenue minus production cost, and consumer surplus is defined as the consumption utility net of buying price and search cost. Producer profits and consumer surplus are the key equilibrium quantities of interest because, as discussed in the literature on two-sided markets $( \mathrm { e . g . , }$ Rochet and Tirole 2003, Armstrong 2006), they are most likely to be the source of revenue for the platform. For instance, some commonly adopted business models for market platforms include (1) charging producers persale royalties $( \mathrm { e . g . }$ , Apple iOS App Store and Google Play Store), (2) charging consumers a membership fee (e.g., Netflix), and (3) accruing direct revenues from hardware sales (e.g., Apple iOS devices and Microsoft Xbox). Each of the business models can be considered as extracting a fraction of the total producer profits (1) or consumer surplus (2 and 3). For ease of reference, we summarize the important notations in Table 1.

Figure 1. (Color online) Illustration of Product Quality and Taste Match  
![](/api/attachments/MMTD83BM/fulltext/images/8608b6ac9df30790fa56ea9e7f4ed8952c923b9c93006860c17533fe808faa60.jpg)  
Notes. The utility consumer i gets from consuming product j is composed of two parts: $v _ { j }$ the quality of product j that is commonly valued by all consumers and $h _ { i j }$ the idiosyncratic taste match. The thick vertical line represents the range of consumption utility in the consumer population. Quality $v _ { j }$ determines the mean consumption utility for the product, and the range of possible $h _ { i j }$ values determines the dispersion of taste match, which is also the dispersion of consumption utility for the product.

Figure 2. Roadmap of Analyses in Sections 3, 4, and 5  
![](/api/attachments/MMTD83BM/fulltext/images/ef24ace5303347b3e0ebc7f5f01e7c78e66c26e03942a8b0c205f130da86044a.jpg)

## 3. Setting 1: Ex Ante Homogeneous Products

We start by considering the simplest case, where all products in the market are ex ante homogeneous from the consumer’s perspective. We use this case to illustrate the derivation of market equilibrium with and without platform recommendation. Specifically, we assume that the vertical dimension (product quality, v ) is identical for all products and that the horizontal dimension (idiosyncratic taste match, $h _ { i j } )$ follows a uniform distribution. As such, the products are ex ante homogeneous in the sense that the consumption utilities provided by different products all have identical mean and variance. Note that the products are still heterogeneous ex post because the consumer will draw different $h _ { i j }$ values for different j. Formally, we introduce the following assumption on the distributions of v<sub>j</sub> and $h _ { i j }$ in the market.

Assumption P1. For all $\begin{array} { r } { j , v _ { j } = v \geq 0 , } \end{array}$ , and $h _ { i j } { \sim } \mathrm { U n i f o r m } [ - t , t ] .$ $t > 0 .$

## 3.1. Market Equilibrium Without Recommendation Under Setting 1

When there is no platform recommendation, we assume that the consumer searches for products in a completely random order. The equilibrium condition derived here will serve as the benchmark for evaluating the effects of platform recommendation.

Assumption C1 <sup>(Without Recommendation)</sup>. The consumer samples products in a random order.

Under Assumptions P1 and C1, a symmetric market equilibrium results where all producers charge the same price. In such an equilibrium, the consumer faces a stationary environment—that is, at each time point during the search process, the utility distribution of unsampled products stays the same. The search theory has established the following optimal stopping rule for consumer search in a stationary environment (which also holds in the other settings we will consider later). The optimal stopping rule is given by a threshold such that the consumer buys the first product she finds where the net utility (consumption utility minus price) exceeds the threshold (e.g., see MacQueen and Miller 1960, McCall 1970, Weitzman 1979). The threshold can be interpreted as the consumer’s reservation utility. Using the result on optimal search behavior, we establish the existence of market equilibrium and characterize the conditions that determine the key equilibrium quantities in the following proposition.

Table 1. Notations

<table><tr><td colspan="2">Model primitives</td></tr><tr><td> $v_j$ </td><td>The quality of product  $j$ </td></tr><tr><td> $h_{ij}$ </td><td>The idiosyncratic taste match of consumer  $i$  for product  $j$ </td></tr><tr><td> $u_{ij} (= v_j + h_{ij})$ </td><td>The consumption utility of product  $j$  for consumer  $i$ </td></tr><tr><td> $p_j$ </td><td>The price of product  $j$ </td></tr><tr><td> $s$ </td><td>The search cost</td></tr><tr><td colspan="2">Distributions of quality and taste match</td></tr><tr><td> $v$ </td><td>The common quality in Setting 1</td></tr><tr><td> $\underline{v}, \overline{v}$ </td><td>The low and high quality in Settings 2 and 3</td></tr><tr><td> $t$ </td><td>The common taste dispersion in Setting 1</td></tr><tr><td> $\underline{t}, \overline{t}$ </td><td>The low and high taste dispersion in Setting 3</td></tr><tr><td colspan="2">Equilibrium quantities</td></tr><tr><td> $p_0^*$ </td><td>Equilibrium price, subindex indicating product type</td></tr><tr><td> $q_0^*$ </td><td>Equilibrium conditional probability of purchase, subindex indicating product type</td></tr><tr><td> $\pi^*, \pi'', \pi'''$ </td><td>Expected total industry (producer) profits in Settings 1, 2, and 3, respectively</td></tr><tr><td> $y^*, y'', y'''$ </td><td>Expected consumer surplus in Settings 1, 2, and 3, respectively</td></tr></table>

Proposition 1. Under Assumptions P1 and C1, if the search cost is moderate (to ensure the consumer participates in the market so there is positive demand), there exists a symmetric equilibrium characterized by product price p∗ and consumer reservation utility $y ^ { * } \geq 0$ such that

1. Given consumer reservation utility y∗, p∗ maximizes each producer’s expected profit, and

2. Given prices $p ^ { * } .$ , the search stopping rule given by reservation utility y∗ maximizes the consumer’s expected surplus. Specifically, p∗ and y∗ satisfy:

$$
p ^ {*} = \underset {p _ {j}} {\arg \max} p _ {j} q _ {j}
$$

$$
= \arg \max _ {p _ {j}} \int_ {- t} ^ {t} I (v + h - p _ {j} - y ^ {*} \geq 0) \frac {1}{2 t} d h,\tag{2}
$$

$$
\int_ {- t} ^ {t} \max \bigl (0, v + h - p ^ {*} - y ^ {*} \bigr) \frac {1}{2 t} d h = s.\tag{3}
$$

Proof. All proofs are in the online appendix. □

Equation (2) is the pricing equation, and it sets the profit-maximization condition for producer $j .$ In the equation, I is the indicator function, and the integral gives the probability that the consumer buys product j conditional on discovering the product, which, per the optimal stopping rule, is the probability that the net utility, $v + h - p _ { j } ,$ is larger than the reservation utility, $y ^ { * }$ . Note that when setting the price, each producer takes the prices of other products as given. As a result, a product’s own price does not affect the probability that the consumer finds the product. Therefore, the expected demand of product j is the integral in Equation (2) multiplied by a constant. Equation (3) states that the reservation utility the consumer holds in her stopping rule is optimal. Intuitively, if the consumer has already found a product that gives her net utility $y ^ { * } ,$ , then the left-hand side of Equation (3) gives the expected gain (over y∗) to the consumer by sampling another product. Because the right-hand side of Equation (3), s, is the cost of sampling another product, the two sides being equal indicates that the consumer is just indifferent between continuing searching and stopping. In other words, the consumer should stop searching if she has found a product that provides a utility greater than $y ^ { * }$ (hence, $y ^ { * }$ is the reservation utility). Note that $y ^ { * }$ is also the expected consumer surplus, so $y ^ { * } \geq 0$ has to be met to ensure that the consumer participates in search at all. For a nonnegative $y ^ { * }$ solution to exist for Equations (2) and (3), the search cost s cannot be too large. For instance, if the search cost is so large that it exceeds the best possible consumption utility, then it is not rational for the consumer to search at all

When a nonnegative $y ^ { * }$ solution does exist, the first-order condition of Equation (2) gives the equilibrium price

$$
p ^ {*} = \frac {v + t - y ^ {*}}{2}.\tag{4}
$$

Ex ante, the expected total sales is 1 and industry profit is $p ^ { * }$ because with infinite products, the consumer will find a match almost surely. But the expected profit for each producer individually is zero because the probability of being chosen is negligible. With zero marginal cost, the producer of the product that the consumer purchases earns a profit of $p ^ { * } .$ which is also the profit of the industry as a whole. The expected consumer surplus is just the reservation utility $y ^ { * }$ . We summarize the equilibrium quantities in the following corollary.

Corollary 1. In the equilibrium defined in Proposition 1, the expected industry profit $\pi ^ { * } = p ^ { * } .$ , and the expected consumer surplus is $y ^ { * }$

## 3.2. Platform Recommendation Under Setting 1

Now consider that the market platform intervenes in the search process by recommending an ordered list of l products, which we index by $j \in \left\{ { 1 , 2 , \dots , l } \right\}$ . With the intervention in place, the consumer is more likely to discover the recommended products. However, if the consumer does not purchase any of the recommended products in the ordered list, she would have to continue sampling the remaining nonrecommended products. We therefore assume that the consumer first follows the platform recommendation by sequentially sampling from product 1 to product $l ,$ and after that, she searches the remaining products in a completely random fashion.

Assumption C2 <sup>(With Recommendation)</sup>. The consumer first samples the recommended products in the predetermined order and then randomly samples the remaining products.

We claim that in the new equilibrium, all producers, including those of the recommended products, still charge the price p∗, and the consumer still adopts the stopping rule that is characterized by reservation utility $y ^ { * } ,$ where $p ^ { * }$ and $y ^ { * }$ are the same as given in Proposition 1.

Proposition 2. Under Assumptions P1 and C2, the product price $p ^ { * }$ and consumer reservation utility $y ^ { * }$ defined by Equations (2) and (3) still constitute a market equilibrium.

The equilibrium result follows by backward induction. First, note that after searching the l recommended products without purchase, the market functions exactly as before, so the producers of the nonrecommended products charge p∗, and the consumer expects a surplus of $y ^ { * }$ . Anticipating the remaining products charging $p ^ { * } ,$ Equation (3) shows that the consumer will hold reservation utility $y ^ { * }$ if she is currently considering the last recommended product, l. Given the expected reservation utility, Equation (2) still characterizes producer $l { ' } s$ profit-maximization problem, so $p _ { l } ^ { * } = p ^ { * }$ Expecting that producer l will be charging $p ^ { * } .$ , the consumer will again hold the reservation utility $y ^ { * }$ at product l <sub>−</sub> 1 (Equation (3)).

Because products are ex ante homogeneous and the equilibrium prices and reservation utility are the same as in the case of random search, the expected consumer surplus does not change with platform recommendation $( \mathrm { i . e . , } \ y ^ { \ast } )$ . The expected total producer profit is still $\pi ^ { * } = p ^ { * } ,$ , which is ex post earned by the product that is actually chosen.

Corollary 2. Under Assumption P1, platform recommendation does not change the expected industry profit and expected consumer surplus.

In contrast to the case of random search, the expected profit does vary between producers due to platform recommendation. In the following, we show how recommendation shifts profits between producers (though it does not alter industry profit as a whole). Let $q ^ { * }$ be the probability that the consumer buys a product conditioning on discovering it (the integral in Equation (2) evaluated at $p _ { j } = p ^ { * } )$ ·

$$
q ^ {*} = \int_ {- t} ^ {t} I (v + h - p ^ {*} - y ^ {*} \geq 0) \frac {1}{2 t} d h = \frac {v + t - y ^ {*}}{4 t}.\tag{5}
$$

Because the consumer will search the first product in the recommendation list with certainty, the expected sales for the product at the top of the list is $q ^ { * } .$ , and the expected profit is $p ^ { * } q ^ { * }$ . The consumer will continue to search the second product in the list if she does not purchase the first product, so the expected sales for the second product in the recommendation list is $( 1 - q ^ { * } ) q ^ { * }$ and the expected profit is $p ^ { * } ( 1 - q ^ { * } ) q ^ { * }$ . In general, for the jth product, $j \leq l ,$ , the expected sales is $\stackrel { \smile } { ( 1 - q ^ { * } ) } { } ^ { j - 1 } q ^ { * } .$ and the expected profit is $\hat { p ^ { * } } ( 1 - q ^ { * } ) ^ { j - 1 } q ^ { * }$ . The expected total sales of the recommended products is $1 - ( \dot { 1 } - q ^ { * } ) _ { \ } ^ { l }$ and that of the remaining products is $( 1 - q ^ { * } ) ^ { l }$ . For the nonrecommended products, the expected sales and profit are individually negligible. In other words, the recommended products have larger sales and profit than the nonrecommended products. Among the recommended products, the expected sales and profit decrease exponentially in the recommendation sequence.

In summary, for ex ante homogenous products, no matter whether the platform maximizes total producer profits or consumer surplus, it would be indifferent between using and not using recommenda tion. Recommendation would only shift profits between producers: The recommended products benefit from the preferential exposure (which leads to higher sales), but the gain to the recommended products equals the loss to the nonrecommended products. Because the products do not have any systematic difference, on expectation, the consumer would not benefit either. When recommendation does exist, the recommended products would expect larger profits. As such, producers have an incentive to compete for recommendation, and they will want their products to be listed high up in the recommendation sequence.

## 4. Setting 2: Products with Heterogeneous Quality and Identical Taste Dispersion

In this section, we allow products to have different quality (i.e., heterogenous in vertical dimension). For ease of exposition, we assume that half of the products are of low quality and the other half are of high quality.<sup>7</sup> Formally, we replace Assumption P1 with Assumption P2.

Assumption P2. For al $j ,$

$$
v _ {j} = \left\{ \begin{array}{l l} \underline {{v}}, & \mathrm{prob=1/2} \\ \overline {{v}}, & \mathrm{prob=1/2}, \end{array} \right.
$$

where $0 < \underline { { v } } < \overline { { v } } ,$ , and $h _ { i j } \sim \mathrm { U n i f o r m } [ - t , t ] , t > 0$

Similar to the approach in Setting 1, we first characterize the market equilibrium under random search and then analyze the implications of product recommendation.

## 4.1. Market Equilibrium Without Recommendation Under Setting 2

In the symmetric equilibrium under random search (Assumption C1), all producers with $v _ { j } = \underline { { v } }$ charge $p _ { \underline { { v } } } ^ { * } ,$ all producers with $v _ { j } = \overline { { v } }$ charge $p _ { \overline { { v } } } ^ { * } ,$ , and the consumer adopts a stopping rule with reservation utility $y ^ { \prime * }$ Formally, we characterize the equilibrium conditions in the following proposition.

Proposition 3. Under Assumptions P2 and C1, $i f$ the search cost is moderate (to ensure the consumer participates in the market and both types of products have positive demand), there exists a symmetric equilibrium characterized by product prices $( p _ { \underline { { v } } } ^ { * } , ~ p _ { \overline { { v } } } ^ { * } )$ and consumer reservation utility $y ^ { \prime * } \geq 0$ such that

1. Given consumer reservation utility $y ^ { \prime \ast } , p _ { v } ^ { \ast }$ and $p _ { \overline { { v } } } ^ { * }$ maximize expected profits for type v and type v producers, respectively, and

2. Given prices $( p _ { v } ^ { * } , p _ { \overline { { v } } } ^ { * } )$ , the search stopping rule given by reservation utility y∗ maximizes the consumer’s expected surplus. Specifically, $( p _ { \underline { { v } } } ^ { * } , p _ { \overline { { v } } } ^ { * } )$ and $y ^ { \prime * }$ satisfy:

$$
\begin{array}{l} p _ {v _ {j}} ^ {*} = \underset {p _ {j}} {\arg \max} p _ {j} q _ {j} \\ \qquad = \underset {p _ {j}} {\arg \max} p _ {j} \int_ {- t} ^ {t} I (v _ {j} + h - p _ {j} - y ^ {\prime *} \geq 0) \frac {1}{2 t} d h, \\ \qquad v _ {j} \in \{\underline {{v}}, \overline {{v}} \}, \\ \qquad \frac {1}{2} \int_ {- t} ^ {t} \max \bigl (0, \underline {{v}} + h - p _ {\underline {{v}}} ^ {*} - y ^ {\prime *} \bigr) \frac {1}{2 t} d h \\ \qquad + \frac {1}{2} \int_ {- t} ^ {t} \max \bigl (0, \overline {{v}} + h - p _ {\overline {{v}}} ^ {*} - y ^ {\prime *} \bigr) \frac {1}{2 t} d h = s. \end{array}\tag{6}
$$

(<sup>7</sup>)

Similar to Equation (2), Equation (6) characterizes producer $j ^ { \prime } \mathbf { s }$ profit-maximization problem, given its product quality $v _ { j }$ and consumer reservation utility $y ^ { \prime * }$ Equation $( 7 )$ states that $y ^ { \prime * }$ is the optimal reservation utility, given $p _ { v } ^ { * }$ for low-quality products and $p _ { \overline { { v } } } ^ { * }$ for high-quality products in the market. The expected increase in utility from discovering one more product in this setting is the average of the expected gain from a lowquality product and that from a high-quality product, respectively. Under random search, the two product types are encountered with equal probability.

The first-order condition gives<sup>8</sup>

$$
p _ {\underline {{v}}} ^ {*} = \frac {\underline {{v}} + t - y ^ {\prime *}}{2},\tag{8}
$$

$$
p _ {\overline {{v}}} ^ {*} = \frac {\overline {{v}} + t - y ^ {\prime *}}{2}.\tag{9}
$$

$p _ { \overline { { v } } } ^ { * } > p _ { \underline { { v } } } ^ { * } .$ —that is, high-quality products charge a higher price than low-quality products. The realized industry profit is $p _ { \underline { { v } } } ^ { * }$ or $p _ { \overline { { v } } } ^ { * } ,$ , depending on whether the consumer buys a low-quality or high-quality product. The expected profit for each individual producer is negligible. To calculate the expected industry profit, note that the probability (conditional on discovery) of purchasing a low-quality product and that for a highquality product are

$$
q _ {\underline {{v}}} ^ {*} = \frac {\underline {{v}} + t - y ^ {\prime *}}{4 t},\tag{10}
$$

$$
q _ {\overline {{v}}} ^ {*} = \frac {\overline {{v}} + t - y ^ {\prime *}}{4 t},\tag{11}
$$

respectively. Hence, the expected sales of low-quality products is $q _ { \underline { { v } } } ^ { * } / q _ { \underline { { v } } } ^ { * } + q _ { \overline { { v } } } ^ { * }$ and that for high-quality products is $q _ { \overline { { v } } } ^ { * } / q _ { \underline { { v } } } ^ { * } + q _ { \overline { { v } } } ^ { * }$ . The expected total industry profit is $q _ { \underline { { v } } } ^ { * } p _ { \underline { { v } } } ^ { * } + q _ { \overline { { v } } } ^ { * } p _ { \overline { { v } } } ^ { * } / q _ { \underline { { v } } } ^ { * } + q _ { \overline { { v } } } ^ { * }$ . We summarize the equilibrium quantities in the following corollary.

Corollary 3. In the equilibrium defined in Proposition 3, the expected industry profit

$$
\pi^ {\prime *} = \frac {q _ {\underline {{v}}} ^ {*} p _ {\underline {{v}}} ^ {*} + q _ {\overline {{v}}} ^ {*} p _ {\overline {{v}}} ^ {*}}{q _ {\underline {{v}}} ^ {*} + q _ {\overline {{v}}} ^ {*}},
$$

$p _ { \underline { { v } } } ^ { * } < \pi ^ { \prime * } < p _ { \overline { { v } } } ^ { * } .$ , and the expected consumer surplus is $y ^ { \prime * }$ .

## 4.2. Platform Recommendation Under Setting 2

As in Setting 1, the platform recommends an ordered list of l products, and the consumer’s behavior changes to first search the recommended products in the determined order and then sample the remaining products randomly (Assumption C2). We further assume that the consumer does not know which types of products are being recommended. Following the same backwardinduction logic as in the analysis of homogeneous products, the recommended products will still charge $p _ { v } ^ { * }$ or p∗ in the new equilibrium, depending only on their quality. The consumer will still use a reservation utility of $y ^ { \prime * }$

To analyze the impact of recommendation on pro ducer profits, suppose the platform can discern the quality difference between products. The platform can increase the expected total producer profits by recommending high-quality products. To illustrate the idea, let $l \stackrel { \smile } { = } 1$ . The consumer samples the recommended product first. If she buys the product, which happens with probability $q _ { \underline { { v } } } ^ { * }$ or q∗ , the profit earned is $p _ { \underline { { v } } } ^ { * }$ or $p _ { \overline { { v } } } ^ { * } ,$ depending on whether the recommended product is of low or high quality. If the consumer is unsatisfied with the first product, which happens with probability $1 - q _ { v } ^ { * } \mathrm { o r } 1 - \bar { q } _ { \overline { { v } } } ^ { * } ,$ she then searches the other products randomly, so the expected industry profit from the second product onward is $\pi ^ { \prime \ast }$ (Corollary 3). Thus, the new expected industry profit when a lowquality product is recommended is $q _ { \underline { { v } } } ^ { * } p _ { \underline { { v } } } ^ { * } + ( 1 - q _ { \underline { { v } } } ^ { * } ) \pi ^ { \prime * } ,$ and $q _ { \overline { { v } } } ^ { * } p _ { \overline { { v } } } ^ { * } + ( 1 - q _ { \overline { { v } } } ^ { * } ) \pi ^ { \prime * }$ when a high-quality product is recommended. Observe that $q _ { \underline { { v } } } ^ { * } p _ { \underline { { v } } } ^ { * }$ (or $q _ { \overline { { v } } } ^ { * } p _ { \overline { { v } } } ^ { * } )$ is the expected profit gain on the recommended product, and $- q _ { v } ^ { * } \hat { \pi } ^ { \prime * } \left( \mathrm { o r } - q _ { \overline { { v } } } ^ { * } \pi ^ { \prime * } \right)$ is the expected profit loss on the nonrecommended products. Because $p _ { \underline { { v } } } ^ { * } < \pi ^ { \prime * } < p _ { \overline { { v } } } ^ { * }$ and $q _ { \underline { { v } } } ^ { * } < q _ { \overline { { v } } } ^ { * } ,$ , the expected gain outweighs the expected loss when the recommended product is of high quality, and the reverse is true when the recommended product is of low quality. More generally, if the platform recommends l high-quality products, the expected in dustry profit becomes

$$
q _ {\overline {{v}}} ^ {*} p _ {\overline {{v}}} ^ {*} + q _ {\overline {{v}}} ^ {*} p _ {\overline {{v}}} ^ {*} \big (1 - q _ {\overline {{v}}} ^ {*} \big) + \ldots + q _ {\overline {{v}}} ^ {*} p _ {\overline {{v}}} ^ {*} \big (1 - q _ {\overline {{v}}} ^ {*} \big) ^ {l - 1} + \big (1 - q _ {\overline {{v}}} ^ {*} \big) ^ {l} \pi^ {\prime *}
$$

$$
= \left(1 - \left(1 - q _ {\overline {{v}}} ^ {*}\right) ^ {l}\right) p _ {\overline {{v}}} ^ {*} + \left(1 - q _ {\overline {{v}}} ^ {*}\right) ^ {l} \pi^ {\prime *},
$$

which approaches the best possible industry profit $p _ { \overline { { v } } } ^ { * }$ as l —when a large number of high-quality products are recommended, the consumer will have to reject all of them before she encounters a lowquality product, so she will almost surely purchase a high-quality product. Therefore, it is in the platform’s best interest to recommend high-quality products if the goal is to maximize the total producer profits.

To explain the impact on expected consumer surplus, we discuss the basic intuition using the case when only a single product is recommended $( l = 1 )$ Under the equilibrium stopping rule, the consumer’s expected surplus is the sum of three parts: the search cost incurred for sampling the recommended product ( s), the expected surplus gain from the recommended product, and the option value of continued searching (the expected surplus from randomly searching the remaining products, i.e., $y ^ { \prime * } )$ . Because the search cost and option value do not depend on the recommended product, we determine whether recommending a highquality (low-quality) product will increase or decrease consumer surplus by comparing the expected utility gain from finding a high-quality product with that from finding a low-quality product—that ${ \mathrm { i } } \mathbf { s } ,$ the two integrals in Equation (7). We find that the expected net utility gain from finding a high-quality product is larger than that from finding a low-quality product (the calculation is provided in the online appendix). Therefore, recommending high-quality products can increase the expected consumer surplus. We summarize the impacts of platform recommendation on expected producer profits and consumer surplus in the proposition below.

Proposition 4. Under Assumption P2, recommending a type v product generates a larger expected industry profit and a larger expected consumer surplus than recommending a type v product.

When conditioning on taste dispersion—that is, considering products that are heterogeneous only in the vertical quality dimension—the theoretically optimal recommendation strategy for the platform is clear and also intuitive from Proposition 4—it should always recommend high-quality products, regardless of whether the platform’s incentive is to maximize total producer profits or consumer surplus.

If the platform is unable to distinguish between highand low-quality products, then the platform may still use observed market signals for selecting recommended products. Two strategies commonly employed by platforms are based on price and past sales, respectively. Under the current setting, we know high-quality products will charge a higher price than low-quality products $\begin{array} { r } { ( p _ { \overline { { v } } } ^ { * } > p _ { v } ^ { * } ) } \end{array}$ see Equations (8) and (9)), and high-quality products are also expected to have larger sales than low-quality products $( q _ { \overline { { v } } } ^ { * } > q _ { \underline { { v } } } ^ { * } ;$ see Equations (10) and (11)). Thus, even if the platform does not observe product quality directly, it can still leverage the price and sales signals to identify high-quality products. As such, the platform can increase expected producer profits and consumer surplus by recommending highprice products and/or high-sales products. As we will show in the next section, this convenient result will not hold when products differ in the horizontal dimension.

## 5. Setting 3: Products with Heterogeneous Quality and Taste Dispersion

In this section, we relax Assumption P2 by assuming the products differ not only in the vertical dimension, but also in the horizontal dimension.

Assumption P3. For al $j ,$

$$
v _ {j} = \left\{ \begin{array}{l l} \underline {{v}}, & \mathrm{prob=1/2} \\ \overline {{v}}, & \mathrm{prob=1/2,} \end{array} \right.
$$

where $0 < \underline { { v } } < \overline { { v } }$ , and

$$
h _ {i j} \sim \mathrm{Uniform} \bigl [ - t _ {j}, t _ {j} \bigr ], t _ {j} = \left\{ \begin{array}{l l} \frac {t}{2}, & \mathrm{prob=1/2} \\ \frac {t}{2}, & \mathrm{prob=1/2,} \end{array} \right.
$$

where $0 < \underline { { t } } < \overline { { t } } .$ The draw of ${ \bf \dot { \boldsymbol { t } } } _ { j }$ is independent of that of $\dot { v } _ { j }$ .

Under Assumption P3, there are four product types: $( \underline { { v } } , \underline { { t } } ) , ( \underline { { v } } , \overline { { t } } ) , ( \overline { { v } } , \underline { { t } } ) .$ , and (v, t). Each type accounts for one-quarter of all products in the market.<sup>9</sup> The difference in the horizontal dimension (t versus t) does not affect the mean consumption utility (determined by $v _ { j } )$ , but measures the dispersion of the tastematch distribution. A product with $t _ { j } = \overline { { t } }$ has a larger consumer taste dispersion than a product with $t _ { j } = \underline { { t } } .$ A simple interpretation is that a product with $t _ { j } = { \overline { { t } } }$ has a more radical design than a product with $t _ { j } = \underline { { t } } - \mathrm { t h e }$ consumer either likes the high-taste-dispersion product a lot or hates it. When producers set price, they know their own product’s type. The consumer knows the distributions of $v _ { j }$ and $t _ { j }$ in the market, but not any specific $v _ { j }$ or $t _ { j }$ value.

## 5.1. Market Equilibrium Without Recommendation Under Setting 3

In the symmetric equilibrium under random search (Assumption C1), producers of the same type charge the same price, and the consumer adopts a stopping rule with reservation utility $y ^ { \prime \prime \ast }$ . Formally, we characterize the equilibrium conditions in the following proposition.

Proposition 5. Under Assumptions P3 and $C 1 , \ i f$ the search cost is moderate (to ensure the consumer participates in the market and all four types of products have positive demand), there exists a symmetric equilibrium characterized by product prices $( p _ { \underline { { v } } , \underline { { t } } } ^ { * } , \dot { p } _ { \underline { { v } } , \overline { { t } } } ^ { * } , p _ { \overline { { v } } , \underline { { t } } } ^ { * } , p _ { \overline { { v } } , \overline { { t } } } ^ { * } ) .$ , and consumer reservation utility $y ^ { \prime \prime \ast } \geq 0$ such that

1. Given consumer reservation utility $y ^ { \prime \prime \ast } , p _ { \underline { { v } } , \underline { { t } } } ^ { \ast } , p _ { \underline { { v } } , \overline { { t } } } ^ { \ast } , p _ { \overline { { v } } , \underline { { t } } } ^ { \ast } ,$ and $p _ { \overline { { v } } , \overline { { t } } } ^ { * } ,$ , respectively, maximize expected profits for products of type $( \underline { { v } } , \underline { { t } } ) , ( \underline { { v } } , \overline { { t } } ) , ( \overline { { v } } , \underline { { t } } ) .$ , and (v, t), and

2. Given prices $( p _ { \underline { { v } } , \underline { { t } } } ^ { * } , p _ { v , \bar { t } } ^ { * } , p _ { \overline { { v } } , \underline { { t } } } ^ { * } , p _ { \overline { { v } } , \bar { t } } ^ { * } ) .$ , the search stopping rule given by the reservation utility $y ^ { \prime \prime \ast }$ maximizes the consumer’s expected surplus. Specifically, $( p _ { \underline { { v } } , \underline { { t } } } ^ { * } , ~ p _ { \underline { { v } } , \overline { { t } } } ^ { * } , ~ p _ { \overline { { v } } , \underline { { t } } } ^ { * } ,$ $p _ { \overline { { v } } , \overline { { t } } } ^ { * } )$ and y∗ satisfy:

$$
\begin{array}{l} p _ {v _ {j}, t _ {j}} ^ {*} = \underset {p _ {j}} {\arg \max} p _ {j} q _ {j} \\ = \underset {p _ {j}} {\arg \max} p _ {j} \int_ {- t _ {j}} ^ {t _ {j}} I \big (v _ {j} + h - p _ {j} - y ^ {\prime \prime *} \geq 0 \big) \frac {1}{2 t _ {j}} d h, \\ v _ {j} \in \{\underline {{v}}, \overline {{v}} \} t _ {j} \in \{\underline {{t}}, \overline {{t}} \}, \end{array}\tag{12}
$$

$$
\begin{array}{r l} & {\frac {1}{4} \int_ {- \underline {{t}}} ^ {\underline {{t}}} \max \Big (0, \underline {{v}} + h - p _ {\underline {{v}}, \underline {{t}}} ^ {*} - y ^ {\prime \prime *} \Big) \frac {1}{2 \underline {{t}}} d h} \\ & {\quad + \frac {1}{4} \int_ {- \overline {{t}}} ^ {\overline {{t}}} \max \Big (0, \underline {{v}} + h - p _ {\underline {{v}}, \overline {{t}}} ^ {*} - y ^ {\prime \prime *} \Big) \frac {1}{2 \overline {{t}}} d h} \\ & {\quad + \frac {1}{4} \int_ {- \underline {{t}}} ^ {\underline {{t}}} \max \Big (0, \overline {{v}} + h - p _ {\overline {{v}}, \underline {{t}}} ^ {*} - y ^ {\prime \prime *} \Big) \frac {1}{2 \underline {{t}}} d h} \\ & {\quad + \frac {1}{4} \int_ {- \overline {{t}}} ^ {\overline {{t}}} \max \Big (0, \overline {{v}} + h - p _ {\overline {{v}}, \overline {{t}}} ^ {*} - y ^ {\prime \prime *} \Big) \frac {1}{2 \overline {{t}}} d h = s.} \end{array}\tag{13}
$$

Similar to Equations (2) and $( 6 )$ , given type $( v _ { j } , t _ { j } )$ and consumer reservation utility $y ^ { \prime \prime \ast }$ , Equation (12) characterizes producer $j ^ { \prime } \mathbf { s }$ profit-maximization problem. The first-order condition gives<sup>10</sup>

$$
p _ {\underline {{v}}, \underline {{t}}} ^ {*} = \frac {\underline {{v}} + \underline {{t}} - y ^ {\prime \prime *}}{2}, p _ {\underline {{v}}, \overline {{t}}} ^ {*} = \frac {\underline {{v}} + \overline {{t}} - y ^ {\prime \prime *}}{2},\tag{14}
$$

$$
p _ {\overline {{v}}, \underline {{t}}} ^ {*} = \frac {\overline {{v}} + \underline {{t}} - y ^ {\prime \prime *}}{2}, p _ {\overline {{v}}, \overline {{t}}} ^ {*} = \frac {\overline {{v}} + \overline {{t}} - y ^ {\prime \prime *}}{2}.\tag{15}
$$

Given the prices in Equations (14) and (15), Equation (13) characterizes the optimal reservation utility. The leftand side of the equation is the expected increase in utility from sampling one more product—the four integrals are the expected gains from discovering each of the four product types. Under random search, each case happens with probability 1/4.

In the equilibrium, the probabilities of purchasing the four product types conditional on discovery are

$$
q _ {\underline {{v}}, \underline {{t}}} ^ {*} = \frac {\underline {{v}} + \underline {{t}} - y ^ {\prime \prime *}}{4 \underline {{t}}}, q _ {\underline {{v}}, \overline {{t}}} ^ {*} = \frac {\underline {{v}} + \overline {{t}} - y ^ {\prime \prime *}}{4 \overline {{t}}},\tag{16}
$$

$$
q _ {\overline {{v}}, \underline {{t}}} ^ {*} = \frac {\overline {{v}} + \underline {{t}} - y ^ {\prime \prime *}}{4 \underline {{t}}}, q _ {\overline {{v}}, \overline {{t}}} ^ {*} = \frac {\overline {{v}} + \overline {{t}} - y ^ {\prime \prime *}}{4 \overline {{t}}},\tag{17}
$$

respectively. Analogous to Corollary 3, we have the following result on the expected industry profit and consumer surplus.

Corollary 4. In the equilibrium defined in Proposition $5 ,$ the expected total industry profit

$$
\pi^ {\prime \prime *} = \frac {q _ {\underline {{v}} , \underline {{t}}} ^ {*} p _ {\underline {{v}} , \underline {{t}}} ^ {*} + q _ {\underline {{v}} , \underline {{t}}} ^ {*} p _ {\underline {{v}} , \underline {{t}}} ^ {*} + q _ {\overline {{v}} , \underline {{t}}} ^ {*} p _ {\overline {{v}} , \underline {{t}}} ^ {*} + q _ {\overline {{v}} , \overline {{t}}} ^ {*} p _ {\overline {{v}} , \overline {{t}}} ^ {*}}{q _ {\underline {{v}} , \underline {{t}}} ^ {*} + q _ {\underline {{v}} , \overline {{t}}} ^ {*} + q _ {\overline {{v}} , \underline {{t}}} ^ {*} + q _ {\overline {{v}} , \overline {{t}}} ^ {*}},
$$

and the expected consumer surplus is $y ^ { \prime \prime \ast }$

## 5.2. Platform Recommendation Under Setting 3

We now analyze the impact of platform recommen dation. As before, we assume that the consumer does not know which types of products are being recommended, and, when searching, she first goes through the recommended products in the predetermined order and subsequently samples the remaining products randomly (Assumption C2). Using the same backward-induction argument from the previous analyses, we know the recommended products in the new equilibrium will still charge the same price given in Equations (14) and (15).

When conditioning on taste dispersion, our analysis in Section 4.2 has provided results on optimal product selection with respect to quality. As such, we now examine the difference between recommending high-taste-dispersion products and recommending low-taste-dispersion products, conditioning on quality In other words, we compare recommending type $( v _ { j } , \ \underline { { t } } )$ products and recommending type $( v _ { j } , \ \bar { t } )$ products in terms of the impact on total producer profits and consumer surplus.

If the consumer purchases the recommended product, the transaction generates a profit of $p _ { v _ { j } , \underline { { t } } } ^ { * } \left( \mathrm { f o r } \left( v _ { j } , \underline { { t } } \right) \right)$ ) or $p _ { v _ { i } , \overline { { t } } } ^ { * } \left( \mathrm { f o r } \ ( v _ { j } , \overline { { t } } ) \right)$ . From Equations (14) and (15), we observe tha $p _ { v _ { i } , \overline { { t } } } ^ { * } > p _ { v _ { j } , \underline { { t } } } ^ { * }$ . That is, the high-taste-dispersion products have a larger profit margin than the lowtaste-dispersion products. However, recommending a high-profit-margin product does not necessarily maximize industry profit. The underlying reason for the decoupling of producer profit and industry profit is the following. When product heterogeneity exists only in the vertical dimension, a high-profit-margin product (i.e., high-quality product) is also more likely to be accepted by the consumer than a low-profitmargin product $( \mathrm { i . e . , }$ low-quality product). When taste dispersion in the horizontal dimension is introduced, whether recommending a high-taste-dispersion product would increase or decrease the expected industry profit depends on the joint effect of profit margin (price) and purchase probability (proportional to sales). The probability that the consumer accepts a high-taste-dispersion product can actually be smaller under some conditions. To see when low-taste-dispersion products are more likely to be accepted than high-tastedispersion products, refer to Equations (16) and (17). Specifically, the equations show $q _ { v _ { i } , \overline { { t } } } ^ { * } < q _ { v _ { j } , \underline { { t } } } ^ { * }$ if and only if $v _ { j } > y ^ { \prime \prime \ast }$ . The condition $v _ { j } > y ^ { \prime \prime \ast }$ is more likely to hold when both product quality and search cost are simultaneously high (because the reservation utility $y ^ { \prime \prime \ast }$ decreases with the search cost). As before, if the consumer rejects the recommended product (which happens with probability $1 - q _ { v _ { j } , \underline { { t } } } ^ { * } \operatorname { o r } 1 - q _ { v _ { j } , \overline { { t } } } ^ { * } ) ,$ , she then searches the remaining products in a random order, so the expected industry profit from the remaining products would be $\pi ^ { \prime \prime \ast }$ (Corollary 4). Calculating and comparing the expectations yield the result on industry profit in Proposition 6.

In general, neither the price signal nor the sales signal alone can help the platform select the recommended product to maximize total producer profits. An interesting implication from Proposition 6 is that it is feasible to combine the observed price and sales signals to achieve the theoretical optimum. Note that $\pi ^ { \prime \prime \ast }$ is a function of equilibrium prices and sales. Therefore, even if the platform has no knowledge of product types $( v _ { j } , \ t _ { j } )$ , it can nonetheless compute $q _ { v _ { j } , t _ { j } } ^ { * } ( p _ { v _ { j } , t _ { j } } ^ { * } -$ $\pi ^ { \prime \prime \ast } )$ for each product using the observed prices and sales. Then, as the condition indicates, recommending product(s) where $q _ { v _ { j } , t _ { j } } ^ { * } ( p _ { v _ { j } , t _ { j } } ^ { * } - \pi ^ { \prime \prime * } )$ is the largest maximizes industry profit.

Unlike the setting of Section 4.2, where recommending high-quality products is always aligned with maximizing consumer surplus, we find here that the recommendation’s impact on consumer surplus is conditional on a quality-level threshold. Specifically, if $v _ { j } > y ^ { \prime \prime \ast } + \sqrt { \underline { { t } } \overline { { t } } } ,$ , recommending a low-taste-dispersion product will increase the expected consumer surplus, and if $v _ { j } < y ^ { \prime \prime \ast } + \sqrt { \underline { { t } } \overline { { t } } } ,$ , recommending a high-tastedispersion product will increase the expected consumer surplus. Taking the search cost and product horizontal heterogeneity as given, recommending a type t product is more likely to increase (decrease) expected consumer surplus if product quality is low (high). Because high dispersion means larger probability mass on extreme values of taste match, an intuitive understanding of the result would be the following: If the quality level is low, then the upside potential is more important, so it would be beneficial to recommend a “riskier” product (high dispersion); if the quality level is already high, then minimizing the downside risk is more important, so it would be beneficial to recommend a “safer” product (low dispersion).

Relying on price or sales signals will not necessarily lead to optimal recommendation for maximizing consumer surplus. Because the sign of the price difference between the high-dispersion and low-dispersion products is independent of the level of quality $( \boldsymbol { p } _ { \boldsymbol { v } _ { j } , \overline { { t } } } ^ { * }$ is larger than $p _ { v _ { j } . \underline { { t } } } ^ { * }$ regardless of v<sub>j</sub>; see Equations (14) and (15)), price-based recommendations will not be optimal for the same reasons discussed above. For the sales signal, observe that $q _ { v _ { j } , \overline { { t } } } ^ { * } \{ \stackrel { < } { = } { q } _ { v _ { j } , \underline { { t } } } ^ { * }$ when $v _ { j } \equiv _ { y ^ { \prime \prime * } }$ (see Equations (16) and (17)). Thus, the productquality threshold for sales-signal reversal (due to taste dispersion) is lower than the threshold specified in the condition for consumer surplus. Hence, the switch between high- versus low-taste-dispersion product recommendation occurs at a lower product quality threshold than needed for optimizing consumer surplus.

Therefore, recommendations based on sales cannot guarantee the best result either.

Proposition 6. Under Assumption P3, recommending a type $( v _ { j } , \ \bar { t } )$ product generates a larger expected industr profit than recommending a type (v<sub>j</sub>, t) product if and only $i f \ \bar { q } _ { v _ { j } , \bar { t } } ^ { * } ( p _ { v _ { j } , \bar { t } } ^ { * } - \pi ^ { \prime \prime * } ) \ge q _ { v _ { j } , \underline { { t } } } ^ { * } ( \bar { p } _ { v _ { j } , \underline { { t } } } ^ { * } - \pi ^ { \prime \prime * } ) ;$ ; recommending a type $( v _ { j } , \bar { t } )$ product generates a larger expected consumer surplus than recommending a type $( v _ { j } , \ \underline { { t } } )$ product if and only if $v _ { j } \leq y ^ { \prime \prime \ast } + \sqrt { \underline { { t } } \overline { { t } } } .$

In summary, when products are differentiated by their consumer taste dispersion, the platform’s optimal product recommendation strategy is more complicated. Specifically, when the goal is to maximize industry profit, the type of products the platform should recommend is determined by the interaction of price and sales, as specified in Proposition 6. The theoretical optimum can be achieved by combining the observed price and sales signals. When the goal is to maximize consumer surplus, the platform should recommend high-taste-dispersion (low-taste-dispersion) products to maximize consumer surplus if the product quality is low (high). However, if the platform cannot discern product type, recommendation based on price or sales will not guarantee optimal strategy for maximizing consumer surplus. In the online appendix, we provide numerical examples to demonstrate the results on optimal recommendations as well as to show that recommendations based on the price or sales signal can be suboptimal.

## 6. Discussion and Conclusion

There is a consensus among practitioners and academics that platform recommendation would, in general, benefit the selected products. As such, product recommendation has become an integral component of platform strategy (Boudreau 2010, Tiwana et al. 2010, Qiu et al. 2017) to enhance market outcomes. Extant research, however, has not systematically addressed the impact of recommendation on producer profits and consumer surplus at the market level. Consequently, there is very little theoretical guidance on how the platform should select products for recommendation This work develops an analytical model by adapting the consumer-search framework of Wolinsky (1986) and Anderson and Renault (1999) to elucidate the tension between the product- and market-level outcomes (Huber et al. 2017) induced by platform recommen dation. Our model characterizes the equilibrium implications of platform recommendation, which entails the trade-off between the potential gains from the recommended products and the potential losses from the nonrecommended products. Our analysis regarding optimal product recommendation emphasizes the selection of recommended products to balance this trade-off.

We contribute to the platform-recommendation literature by systematically analyzing changes in producer profits and consumer surplus under platform recommendation. We compare the promotion of the recommended products in the consumer search sequence vis-a-vis the benchmark case where consumers \` search products randomly. The analysis provides the theoretical basis on which types of products the platform should select for recommendation to optimize platformlevel outcomes. The key insights of our findings come from the separate analyses regarding product heterogeneity in the vertical and horizontal dimensions (i.e., product quality and idiosyncratic taste match). Our results indicate that recommending high-quality products will increase both industry profit and consumer surplus. Recommending high-taste-dispersion products, however, may increase or decrease industry profit and consumer surplus depending on the interaction of price and sales as well as the relationship between product quality and taste heterogeneity. Importantly, when the platform cannot discern product types, recommendation strategies based on observed price or sales signals cannot guarantee optimality in the general case.

The analyses in our paper also provide several conceptual and practical implications beyond the immediate scope of product selection for recommendation. Our result on sales-based recommendation complements the existing knowledge about the market effects of platform-published sales rankings, such as bestseller lists. The literature has documented that bestseller lists not only reflect consumers’ past purchases, but also oftentimes directly influence consumer behavior (Sorensen 2007, Hendricks and Sorensen 2009). In fact, consumers use the bestseller lists in crowded markets as a product-discovery channel (e.g., see Bresnahan et al. 2015 in the context of the mobile app market). As a result, bestseller lists create a market environment that favors the already-successful products, so they tend to hurt product variety—that is, they reinforce the superstar or rich-get-richer effect (Sorensen 2007). To the extent that bestseller lists are used by consumers as a product-discovery channel, we conceptualize that their role is essentially to promote the best-selling products in the consumer search sequence. In this sense, bestseller lists can be seen as sales-based recommendation within our analytical framework. Our finding, then, shows that, in addition to having drawbacks for product variety and equality, the effects of bestseller lists can be suboptimal, even in terms of pure market efficiency (because sales-based recommendation cannot achieve either optimal total industry profit or consumer surplus).

The optimal product recommendation that our theoretical model suggests is based on the assumption that the platform is able to determine product types in terms of heterogeneity in the vertical and horizontal dimensions. If the platform cannot distinguish different product types (for example, in the case of a nascent market platform that has not built the editorial and data-analytical capability for assessing product heterogeneity), recommendations based on readily available price or sales signals can be suboptimal in the general case. From this point of view, providing platform recommendation can be thought of as a way of shifting the costs of product search and evaluation from individual consumers to the platform owner. Presumably, the platform owner’s search costs would be considerably lower than the aggregate costs for individual consumers, so it should be beneficial for the whole ecosystem to have the platform provide product recommendation.

Our analytical results have useful implications for generating personalized recommendations through algorithm-based recommender systems. Many algorithmic recommender systems predict to what extent a given user would like a given product (often as a preference score) and also provide a precision esti mate associated with the prediction (e.g., in the form of a confidence interval). Then, for a particular user and a number of candidate products, the recom mender system would output a series of preferencescore and confidence-interval pairs. If we interpret our model’s vertical utility component as the preference score and the horizontal component as a measure of the confidence interval, then our results can potentially be applied to determine the optimal ranking of these personalized recommendations. Of course, the success of using the method will depend on the reliability of the predictions generated by the recommender system.

We identify several directions to extend the current research. Future studies can explore ways to incorporate platform recommendation as part of the market outcome rather than as an exogenous intervention. Given the product heterogeneity in the market, we have examined how the platform should select the types of products for recommendation. Future research can build on our framework to analyze how the size of market-level gains would change with the degree of product heterogeneity. One approach to endogenizing the extensive and intensive margins of platform recommendation is through formally modeling the platform’s revenue structure and the costs associated with conducting product search and evaluation. Such an approach would then lead to a characterization of the threshold at which point making a recommendation becomes unprofitable for the platform owner.

In the current setting of the model, the distribution of different types of products is given and fixed in the market. In other words, we implicitly assume that the producers have designed and developed their products, and the model only considers producers producing and selling copies of their existing products. Taking a longer-term view, researchers could investigate whether and how platform recommendation will influence producers’ strategic decisions, such as entry, investment, and innovation. Answering these questions can help us understand the longterm implications of platform recommendation on product quality and variety in the marketplace and, more broadly, contribute to our knowledge about the influence of platform governance on the coevolution of ecosystems and modules (Tiwana et al. 2010). The current model in the paper assumes that consumers are uninformed about all products without recommendation. Future research may seek to relax this assumption and reanalyze the implications on the platform-recommendation strategy—for example, by assuming the coexistence of well-established incumbent products and lesser-known new entrants. From a practical perspective, one can then study producers best responses when the platform recommends their own products or their competitors’ products.

## Endnotes

<sup>1</sup> See https://techcrunch.com/2016/11/28/amazon-expands-its-online -gift-shop-interesting-finds-adds-human-curation/.

<sup>2</sup> See https://www.macrumors.com/2017/07/21/editorial-app-store-ios -11-beta/. Industry reports and practitioner-oriented publications suggest that these App Store recommendations require significant editorial efforts (https://mashable.com/2017/09/23/inside-the-new-apple-app -store/#N2aWCf3PPZqR) and have an outsized impact on the recommended apps’ commercial success (https://sensortower.com/blog/ ios-11-featuring-impact). Moreover, a recent change of the App Store reflects even greater emphasis on platform recommendations through editorial content, which has been observed as a strategic move by Apple to improve the discovery of quality new apps and the long-term health of the store ecosystem (https://www.storemaven.com/ios-11-app -store-updates-and-its-impact-on-app-discovery/).

<sup>3</sup> Without loss of generality, $. h _ { i j }$ is assumed to have a mean of zero over i because any nonzero mean can be absorbed into $v _ { j }$ as part of the quality.

<sup>5</sup> That consumers know the distributions of $v _ { j }$ and $h _ { i j }$ can be justified by making the assumption that consumers search the market repeatedly, and they learn the distributions over time. Alternatively, we can assume consumers have beliefs about the distributions, and they behave according to their beliefs; as part of the equilibrium condition, the beliefs are required to be consistent with the true distributions.

<sup>6</sup> Thus, the probability that the consumer purchases a particular product can be interpreted as the market share of the product.

product—the high-quality ones—would sell in such a market. The analysis would reduce to the homogeneous-product case. To avoid discussing such corner solutions, we focus on the scenario where both types of products have positive demand—the reservation utility is not too large, meaning the search cost is not too low.

<sup>9</sup> The results will not change qualitatively if we assume a continuous distribution for $t _ { j } .$

<sup>10</sup> Here, we are assuming that all four types of products have positive demand similar to footnote 8.

## References

Adomavicius G, Tuzhilin A (2005) Toward the next generation of recommender systems: A survey of the state-of-the-art and possible extensions. IEEE Trans. Knowledge Data Engrg. 17(6):734–749.

Anderson SP, Renault R (1999) Pricing, product diversity, and search costs: A Bertrand-Chamberlin-Diamond model. RAND J. Econom. 30(4):719–735.

Armstrong M (2006) Competition in two-sided markets. RAND J. Econom. 37(3):668–691.

Armstrong M, Vickers J, Zhou J (2009) Prominence and consumer search. RAND J. Econom. 40(2):209–233.

Boudreau K (2010) Open platform strategies and innovation: Granting access vs. devolving control. Management Sci. 56(10):1849–1872

Bresnahan TF, Davis JP, Yin PL (2015) Economic value creation in mobile applications. Jaffe AB, Jones BF, eds. The Changing Frontier: Rethinking Science and Innovation Policy (University of Chicago Press, Chicago), 233–286.

Brynjolfsson E, Hu Y, Simester D (2011) Goodbye pareto principle, hello long tail: The effect of search costs on the concentration of product sales. Management Sci. 57(8):1373–1386.

Fleder D, Hosanagar K (2009) Blockbuster culture’s next rise or fall: The impact of recommender systems on sales diversity. Man agement Sci. 55(5):697–712

Goeree MS (2008) Limited information and advertising in the US personal computer industry. Econometrica 76(5):1017–1074.

Hendricks K, Sorensen A (2009) Information and the skewness of music sales. J. Political Econom. 117(2):324–369.

Huber TL, Kude T, Dibbern J (2017) Governance practices in platform ecosystems: Navigating tensions between cocreated value and governance costs. Inform. Systems Res. 28(3):563–584.

Kim JB, Albuquerque P, Bronnenberg BJ (2010) Online demand unde limited consumer search. Marketing Sci. 29(6):1001–1023.

Liang C, Shi ZM, Raghu TS (2019) The spillover of spotlight: Platform recommendation in the mobile app market. Inform. Systems Res. 30(4):1296–1318.

Lin Z (2014) An empirical investigation of user and system recom mendations in e-commerce. Decision Support Systems 68:111–124.

MacQueen J, Miller Jr RG (1960) Optimal persistence policies. Oper. Res. 8(3):362–380.

McCall JJ (1970) Economics of information and job search. Quart J. Econom. 84(1):113–126.

Morgan P, Manning R (1985) Optimal search. Econometrica 53(4): 923–944.

Perloff JM, Salop SC (1985) Equilibrium with product differentiation. Rev. Econom. Stud. 52(1):107–120.

Qiu Y, Gopal A, Hann I-H (2017) Logic pluralism in mobile platform ecosystems: A study of indie app developers on the iOS app store. Inform. Systems Res. 28(2):225–249.

Ricci F, Rokach L, Shapira B (2011) Introduction to Recommender Systems Handbook. Ricci F, Rokach L, Shapira B,Kantor PB, eds. Recom mender Systems Handbook (Springer, Cham, Switzerland), 1–35

Rochet J-C, Tirole J (2003) Platform competition in two-sided markets J. Eur. Econom. Assoc. 1(4):990–1029.

Senecal S, Nantel J (2004) The influence of online product recom mendations on consumers’ online choices. J. Retailing 80(2):159–169.

Sorensen AT (2007) Bestseller lists and product variety. J. Indust. Econom. 55(4):715–738.

Tiwana A, Konsynski B, Bush AA (2010) Research commentary: Platform evolution: Coevolution of platform architecture,

governance, and environmental dynamics. Inform. Systems Res. 21(4):675–687.

Weitzman ML (1979) Optimal search for the best alternative. Econ ometrica 47(3):641–654

Wolinsky A (1986) True monopolistic competition as a result of imperfect information. Quart. J. Econom. 101(3):493–511.
