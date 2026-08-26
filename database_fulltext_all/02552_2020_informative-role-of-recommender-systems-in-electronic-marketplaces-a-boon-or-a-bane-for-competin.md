---
otero_id: 2552
otero_key: "QTH8AQJ8"
title: "Informative Role of Recommender Systems in Electronic Marketplaces: A Boon or a Bane for Competing Sellers"
authors: "Lusi Li; Jianqing Chen; Srinivasan Raghunathan"
year: "2020"
journal: "MIS Quarterly"
doi: "10.25300/misq/2020/14614"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# INFORMATIVE ROLE OF RECOMMENDER SYSTEMS IN ELECTRONIC MARKETPLACES: A BOON OR A BANE FOR COMPETING SELLERS<sup>1</sup>

Lusi Li College of Business and Economics, California State University, Los Angeles, 5151 State University Drive, Los Angeles, CA 90032 U.S.A. {lli57@calstatela.edu}

Jianqing Chen Jindal School of Management, The University of Texas at Dallas, 800 West Campbell Road, Richardson, TX 75080 U.S.A. {chenjq@utdallas.edu}

Jindal School of Management, The University of Texas at Dallas, 800 West Campbell Road, Richardson, TX 75080 U.S.A. {sraghu@utdallas.edu}

Recommender systems have become the cornerstone of electronic marketplaces that sell products from competing sellers. Similar to traditional advertising, recommender systems can introduce consumers to new products and increase the market size which benefits sellers. This informative role of recommender systems in electronic marketplaces seems attractive to sellers because sellers do not pay the marketplaces for receiving recommendations. We show that in a marketplace that deploys a recommender system helping consumers discover the product that provides them the highest expected net utility, sellers do not necessarily benefit from the “free” exposure provided by the recommender system. The impacts of the recommender system are the result of a subtle interaction between advertising effect and competition effect. The advertising effect causes sellers to advertise less on their own and the competition effect causes them to decrease prices in the presence of a recommender system. Essentially, sellers “pay” in the form of more intense price competition because of the recommender system. Furthermore, the competition effect is exacerbated by the advertising effect because the recommender system alters a seller’s own strategies related to advertising intensity and price from being strategic substitutes in the absence of the recommender system to being strategic complements in its presence. As a result of these two effects, we find that sellers are more likely to benefit from the recommender system only when it has a high precision. The results do not change qualitatively whether sellers use targeted advertising or uniform advertising. However, we find that a recommender system that benefits sellers when they do not employ targeted advertising may actually hurt them when they adopt targeted advertising with a high precision. On the other hand, in the presence of the recommender system, an increase in sellers’ targeting precision beyond a threshold softens price competition, increases seller profits, and reduces consumer surplus. Finally, we find that when the recommender system assigns a larger weight to product fit than price, the adverse impacts of the recommender system on sellers are mitigated, thereby expanding the region in the parameter space where the recommender system is beneficial to sellers

Keywords: Recommender system, electronic commerce, online advertising, analytical modeling, economics of IS

## Introduction

Electronic marketplaces such as Amazon Marketplace and Ebay deploy recommender systems as sales support tools to help buyers find their “ideal” product in the vast variety of products sold on those marketplaces (Hennig-Thurau et al. 2012). Recommender systems have been reported to increase sales on these marketplaces: over 35% of sales on Amazon.com and more than 60% of the rentals on Netflix result from recommendations (Hosanagar et al. 2013). Research indicates that a recommender system affects consumer decision making by informing consumers about products about which they may not be aware (Tam and Ho 2006); this is referred to as the informative role of recommender systems. In this sense, a recommender system deployed by an electronic marketplace functions as a medium for targeted advertising for sellers, analogous to traditional advertising media such as TV, newspaper, and, recently, the Internet. However, some key differences exist between traditional advertising and recommendations. First, the sellers do not “buy” or explicitly pay for recommendations and, therefore, recommendations are “free,” whereas traditional advertising is costly for sellers. Second, while the traditional advertising strategy, including the budget or advertising intensity, is under the direct control of the advertisers or sellers, the recommendation strategy is under the control of the electronic marketplace that deploys the recommender system.

When the purpose of both recommendations as well as seller advertising is creating consumer awareness about products, the presence of the recommender system poses new challenges to sellers in electronic marketplaces regarding their advertising and pricing decisions. One could argue that recommender systems and traditional media are substitutes, and therefore sellers would decrease their traditional advertising in the presence of the recommender system. However, one could also make the argument that the two are complements in the sense that a seller would increase his advertising in the presence of the recommender system in order to mitigate the potential disadvantage it may suffer if the recommender system recommends the competitor’s product. Furthermore, when the recommender system chooses to recommend the product that a consumer is likely to buy, sellers have to reconsider both pricing and advertising strategies. This paper examines the intricate interaction between competing sellers’ advertising and pricing strategies in the presence of a recommender system in an electronic marketplace.

A recommender system uses different information sources such as user’s purchase history, search and browsing behavior, demographic information, product attributes, and product ratings to predict a consumer’s preference and recommend the product the consumer is most likely to buy or prefer (Resnick and Varian 1997). Marketplaces such as Amazon Marketplace deploy a variety of recommender systems that differ along various dimensions and, furthermore, the recommender systems have been constantly evolving. For instance, on Amazon Marketplace, when a visitor searches for a specific product, Amazon displays several related products under the following categories: (a) “Frequently bought together,” (b)(b.1) “Customers who bought this item also bought,” and/or (b.2) “Customers who viewed this item also viewed,” depending on different products, (c) “Sponsored products related to this item,” and (d) “Compare to similar items.” Furthermore, when a registered user logs into Amazon, it explicitly recommends several products under “Today’s recommendations for you.” The products recommended under categories (a) and (b.1) are generally complementary products, whereas those recommended under categories (b.2), (c), (d) and “Today’s recommendations for you” are generally competing products. In this study, we focus on recommendations for competing products.

We develop an analytical model in which two competing sellers sell their products through a common electronic marketplace. Such a two-level channel structure with one dominant e-commerce platform is commonly observed in practice (e.g., Amazon’s marketplace). Consumers are heterogeneous with respect to their preferences for the two products. If the marketplace deploys a recommender system, it recommends a product when a consumer visits the marketplace. Consistent with the broad literature in recommender systems, we model that recommender system chooses to recommend the product that offers the highest expected net utility to the consumer. Sellers can also advertise their products in traditional advertising channels. Both traditional advertising and the recommender system have an informative role in the sense both influence only consumers’ awareness of the products.

Our analysis reveals that the overall impacts of the recommender system are governed by the subtle interaction between two effects: advertising effect and competition effect. The advertising effect causes firms to advertise less and the competition effect causes firms to decrease prices in the presence of the recommender system. More importantly, we find that while a seller’s own strategies related to advertising intensity and price are strategic substitutes in the absence of the recommender system, they are strategic complements and hence reinforce each other in the presence of the recommender system. As a result of these two effects, although the recommendations provided by the recommender system are free, sellers may be better off or worse off in the presence of the recommender system than in the absence. The magnitudes of the competition and advertising effects depend on the recommender system precision and the advertising cost. Sellers are better off in the presence of the recommender system than in the absence when the recommender system precision is high and the advertising cost is low. On the other hand, consumers benefit when the marketplace deploys the recommender system not only because of the increase in the awareness but also because of the competition effect induced by the recommender system.

Since recommender systems have become ubiquitous in electronic marketplaces and the precision of these systems has been continuously improving, a pertinent question relates to how recommender system precision affects sellers and consumers in marketplaces. We find that an increase in the recommender system precision softens the price competition, because an improved precision reduces the relative role of prices vis-à-vis consumer preference in the recommender system’s choice of the product to recommend. As a result of softened price competition, sellers benefit and consumers hurt when precision improves. The increase in precision also affects sellers’ advertising levels. On the one hand, the mitigation of price competition provides an incentive for sellers to advertise more when recommender system precision improves. On the other hand, increased recommender system precision implies that consumers are more likely to buy the product recommended by the marketplace, thus reducing the marginal benefit from sellers’ advertising and limiting their incentive to advertise. Consequently, sellers’ advertising levels follow an inverse U-shape with recommender system precision.

The main results regarding the impacts of the recommender system and the recommender system precision on sellers and consumers do not change qualitatively whether sellers use targeted advertising or uniform advertising. The key additional results when sellers adopt targeted advertising relate to how the sellers’ targeting precision affects these impacts. Interestingly, we find that a recommender system that benefits sellers when they do not employ targeted advertising may actually hurt them when they adopt targeted advertising with a high precision. On the other hand, in electronic marketplaces with the recommender system, an increase in sellers targeting precision beyond a threshold softens price competition, increases seller profits, and reduces consumer surplus. Consequently, in electronic marketplaces with recommender systems, sellers are better off under targeted advertising only when the targeting precision is sufficiently high.

Finally, we find that when the recommender system assigns a larger weight to product fit than price, the adverse impacts of the recommender system on sellers are mitigated, thereby expanding the region in the parameter space where the recommender system is beneficial to sellers.

The rest of this paper is organized as follows. In the next section, we review the related literature. We then develop an analytical framework to model the impact of a recommender system in a channel structure where two competing sellers sell on a common platform. In the subsequent section, we examine the implication of the recommender system by comparing the scenarios with and without recommendations. We follow this with by examining the case in which sellers can target consumers and show how targeted advertising by sellers would affect the implications of the recommender system, after which we examine a more general recommendation strategy that allows for a different relative weight for the product price vis-à-vis fit in choosing the recommendation. Finally, we conclude the paper with discussion on managerial implications.

## Literature Review

The recommender system literature has examined technical (or algorithmic) and economic aspects of recommender systems. Adomavicius and Tuzhilin (2005) provide a review of work related to recommender system algorithms. Existing studies have proposed various metrics to evaluate recommendation algorithms, such as prediction accuracy, recommendation diversity, consumer trust in recommendations, and seller profitability (Bodapati 2008; Chen et al. 2008; Shani and Gunawardana 2011). In this study, we take the recommendation algorithm as exogenously given and focus on the economic impact of recommender systems on sellers. In particular, we assume that the recommender system recommends the product that offers the highest expected net utility to the consumer, consistent with the notion that the primary goal of recommendations is to match the consumer with her preferred product. Wang and Zhang (2011) develop an algorithm that uses consumer’s net utility, and show that their algorithm outperforms the widely used collaborative filtering-based algorithm.

Research on the economics aspects of recommender systems has focused on their impacts on product sales. Fleder and Hosanagar (2009) show that some recommender system designs reinforce the popularity of already popular products. Hosanagar et al. (2013) show recommender systems can lead to consumers purchasing more similar items. Oestreicher-Singer and Sundararajan (2012a) show that a recommender system can flatten demand distributions. Oestreicher-Singer and Sundararajan (2012b) show that, on average, the explicit visibility of a co-purchase relationship can amplify the influence of complementary products on each other’s demands. Pathak et al. (2010) show that the strength of recommendations has a positive effect on sales and prices and that this effect is moderated by the recency effect. Jabr and Zheng (2014) analyze the effect of recommendations and word-ofmoth reviews on product sales in a competitive environment and show that higher referral centrality of competing products is associated with lower product sales. Zhang et al. (2021) focus on the impacts of seller-oriented and consumer-oriented recommender systems on consumer surplus when a monopolistic firm controls prices and the type of recommender system, and show that the consumer surplus decreases by 8.44% and the social welfare decreases by 2.0% when a firm uses a profit-maximizing recommender system compared to a consumer-surplus-maximizing recommender system.

Research that uses an analytical model to examine the impact of recommender systems is limited. Hervas-Drane (2015) shows that recommender systems based on consumer taste enhance consumers’ interest in niche products and decrease market concentration. Bergemann and Ozmen (2006) use a two-stage game to examine how a firm can strategically choose its first-stage price to generate recommendations in the second stage. Choudhary and Zhang (2019) examine the optimal recommender system strategy of an online firm by considering the influence of the recommender system on the consumer’s search behavior. They show that when the accuracy of the recommender system is high, it is profitable for the firm to mislead consumers by not giving them their ideal products. In their model, the prices of all products are assumed to be exogenous and identical. Ghoshal et al. (2015) examine recommender systems in a competitive setting. They show that a recommender system can influence the profit of not only the firm that implements a recommender system but also the firm that does not implement a recommender system. In their analysis, they emphasize the strategic behavior of consumers: consumers may distribute their purchases across two firms to maximize surplus over a planning horizon. Our study differs from prior studies that use analytical modeling in the following important way. We are interested in how recommender systems affect the competition between upstream manufacturers that sell through a retail platform. Consequently, we consider a recommender system deployed by a downstream retail platform in a channel structure where competing upstream firms sell their products via a common retail platform by paying a fraction of the sale price (which they set) to the platform. Therefore, while the retailer deploys the recommender system, it does not set product prices. On the other hand, while competing sellers set prices, they can not directly manipulate the recommender system. In contrast, the previous studies either examine a single retailer setting that ignores the strategic interactions between sellers or examine a multi-retailer setting that focuses on competition between sellers that deploy different recommender systems. Furthermore, different from prior studies, we emphasize the informative role of recommender systems and the trade off faced by the sellers: use advertising to inform their consumers and rely on the recommender system to inform their consumers.

Our study is also related to the marketing literature on informative advertising and competition. Bester and Petrakis (1995) and Grossman and Shapiro (1984) predict an inverse relationship between advertising level and prices in a differentiated product market when advertising provides uninformed consumers with price information. Soberman (2004) extends the work of Grossman and Shapiro to show that informative advertising alone can lead to either higher or lower prices depending on the level of differentiation between competing firms. While these studies consider uniform advertising, another stream of literature considers targeted advertising. Iyer et al. (2005) investigate how competing firms in a hori zontally differentiated market choose the advertising strategy when they can target consumer segments according to their preferences. Gal-Or et al. (2006) examine how an advertiser should allocate resources to increase the quality of targeting. Gal-Or and Gal-Or (2005) study firms’ advertising strategies when they use a single media distributor such as a television cable company as the channel for advertising. Different from these studies, our focus is on the interaction between seller advertising and recommender systems.

## Model

We consider a channel structure with two competing sellers (A and B), an electronic marketplace (R), and a continuum of consumers with heterogeneous preferences. Seller A(B) sells product A(B) and both sell their products only via R. Each seller sets the price of its product, and the marketplace charges the sellers a commission equal to á fraction of the price on each sale. The two products are horizontally differentiated and have different degrees of misfit to different consumers. In particular, we assume that the products are located at the two end points of a Hotelling line of unit length, with product A being at 0 and product B being at 1. Consumers are uniformly distributed along the line. The distance between a product and a consumer measures the degree of misfit of the product to the consumer. The misfit cost is the degree of misfit times a unit misfit cost t. A consumer’s net utility for product $i , i \in \{ A , B \}$ , is equal to the value of the products v less the misfit cost and product price $p _ { i } .$ . Specifically, for a consumer located at z, the net utility from buying product A is $U _ { _ { A } } = \nu - z t - p _ { _ A }$ and from buying product B is $U _ { B } = \nu - ( 1$ $- z ) t - p _ { B } .$ We refer to consumer’s differentiation along the Hotelling line as locational differentiation.

Sellers can inform the consumers about their products and prices by advertising their products in media channels such as

TV, newspaper, and the Internet. Without a recommender system, the only way a consumer becomes informed about a seller’s product is by receiving its advertisement. Advertising is assumed to be informative and has no effect on consumer’s willingness to pay. In the baseline model, firms use uniform advertising; that ${ \mathrm { i s } } ,$ all consumers have equal chance of receiving a given advertisement. Following the standard procedure in modeling informative advertising (e.g., Tirole 1988), we denote $\phi _ { i }$ as the probability that a consumer receives the advertisement from seller i and is aware of product i, and refer to $\phi _ { i }$ as the advertising intensity of seller i. An advertising intensity of $\phi _ { i }$ costs $a \phi _ { i } ^ { 2 } / 2$ , where a measures the cost of advertising. The convexity of the cost function reflects the fact that some consumers are harder to reach than others. As a consequence of sellers’ advertisements, consumers become heterogeneous in their awareness about products. In particular, three types of consumers exist in the marketplace in terms of their product awareness: fully informed consumers, uninformed consumers, and partially informed consumers. Fully informed consumers are aware of both products. The size of the fully informed consumer segment is $\phi _ { { _ A } } \phi _ { _ B }$ Uninformed consumers are aware of neither product. The size of the uninformed consumer segment is $\left( 1 - \phi _ { _ A } \right) \left( 1 - \phi _ { _ B } \right)$ . The partially informed consumer segment includes consumers who are only aware of product A and consumers who are only aware of product $B .$ The size of the group aware of product A only is $\phi _ { _ A } ( 1 - \phi _ { _ B } )$ and the size of group aware of product B only is $\phi _ { B } \left( 1 - \phi _ { A } \right)$ . We refer to the consumer’s differentiation along the awareness dimension as informational differentiation.

Each consumer has a unit demand and can only purchase a product that she is aware of. We denote $z _ { 0 }$ as the location of the marginal consumer who would be indifferent between the two products if she were fully informed. Based on the utility function, we have

$$
z _ {0} = \frac {p _ {B} - p _ {A} + t}{2 t}\tag{1}
$$

Consumers located at $z < z _ { 0 }$ would, if fully informed, buy product A. On the contrary, a fully informed consumer located at ${ z > z _ { 0 } }$ would buy product B. For partially informed consumers, demand is determined by individual rationality; that is, all consumers who are only aware of product i buy from firm i as long as they obtain positive surplus from product i. Consistent with the extant literature (e.g., Grossman 1984; Tirole 1988), we assume that the value of a product to a consumer v is large enough such that both products provide all consumers in the market with a positive surplus; that ${ \mathrm { i } } \mathbf { s } ,$ all partially informed consumers make a purchase in the equilibrium.

The marketplace deploys a recommender system. In the baseline model, the recommender system is assumed to be consumer-centric in that the primary goal of the recommender system is to help a consumer find her best product. In particular, we assume that the recommender system recommends the product that offers a greater expected net utility to a consumer based on the information it has about her. In the extension, we allow the recommender system to assign a larger weight to product fit than price in choosing the recommendation. The recommender system is uncertain about a consumer’s true preference or location on the Hotelling line, and uses information such as purchase data, rating data, and profile data to estimate her location. The estimate may be imperfect and we use a commonly used approach to model this estimation (e.g., Johnson and Myatt 2006; Kwark et al. 2014). In particular, we assume that the retailer observes a signal s regarding consumer’s location. The signal could be viewed as the output of the consumer preference prediction model that is ubiquitous in recommender systems. These predictive models typically estimate the likely consumer rating of a product based on other available information and the rating is used as a measure of the likely consumer preference $( \mathrm { i . e . , }$ , location on the Hotelling line). The signal equals the consumer’s true location with probability $\beta ,$ and with proba bility $( 1 - \beta )$ the signal is uninformative and follows the distribution of consumer locations. That is, $P ( z = y | s = y ) = \beta$ and $P ( z \neq y | s = y ) = 1 - \beta ,$ where y 0 [0, 1]. The model indicates that the signal is informative (i.e, provides useful information for the recommender system to estimate the consumer’s preference) but noisy (i.e, does not perfectly reveal the true preference). We refer to $\beta$ as the precision of the recommender system. An increase in $\beta$ implies that the retailer’s information about the consumer reveals her preference more accurately; when $\beta = 1$ , the information reveals the consumer preference perfectly.

The sequence of events is as follows. In stage 1, sellers set prices $p _ { i }$ and advertising intensities $\phi _ { i }$ simultaneously. In stage 2, consumers visit the marketplace and make their purchase decisions. Two scenarios are considered: one without the recommender system and the other with the recommender system. We use the scenario without the recommender system as the benchmark to analyze the impacts of the recommender system. In the scenario without the recommender system, the purchase decisions are made solely based on consumers’ awareness about products resulting from sellers advertising. In the scenario with the recommender system, the recommender system recommends one product to each consumer, and the consumer observes the recommendation and then makes her purchase decision. A consumer’s awareness and her preference are private information. All other model parameters are common knowledge. All players are risk neutral.

We focus on the interesting case where the competition between sellers plays a role in the equilibrium, and, accordingly, make the following technical assumptions for our analysis. We denote $\tau = a / ( 1 - \alpha )$

Assumption 1:

$$
\begin{array}{l} \max \left\{\left[ 3 t ^ {2} - 4 t v + \sqrt {(v - 5 t) (v - t) ^ {3}} + v ^ {2} \right] / (4 t), t / 2 \right\} \\ <   \tau <   (v - t) ^ {2} / (2 t) \end{array}
$$

Assumption 2:

$$
\begin{array}{l} 1 6 (1 - \beta) ^ {6} t ^ {2} \tau \left[ \beta (1 - \beta) ^ {2} t + 6 \tau - 6 \sqrt {\tau^ {2} - (1 - \beta) ^ {2} \beta y \tau} \right] \\ > \left[ (1 - \beta) ^ {2} t + 2 \tau - 2 \sqrt {\tau^ {2} - (1 - \beta) ^ {2} \beta t \tau} \right] ^ {4} \end{array}
$$

In Assumption 1, $\tau > t / 2$ guarantees that the advertising cost is not too low such that the advertising intensities for both sellers are less than 1. $\tau > \left[ 3 t ^ { 2 } - 4 t \nu + \sqrt { \big ( \nu - 5 t \big ) \big ( \nu - t \big ) ^ { 3 } } + \nu ^ { 2 } \right] \bigg / \big ( 4 t \big )$

is to rule out the trivial case in which sellers only serve the partially informed consumers and ignore the fully informed consumers. The assumption $\tau ^ { < } ( \nu - t ) ^ { 2 } / ( 2 t )$ guarantees that all partially informed consumers make a purchase in the equilibrium $( \mathrm { i } . \mathrm { e } . , p ^ { * } < \nu - t )$ . Assumption 2 guarantees a pure strategy equilibrium for the game when the recommender system is in place. The condition in Assumption 2 is always satisfied when $\beta > 1 / 2 5$

## Impacts of Recommender System

In this section, we first derive the sub-game perfect equilibrium for the scenario without the recommender system and for the scenario with the recommender system using the backward induction approach. Then, we analyze the impact of the recommender system by comparing the equilibria in the two scenarios.

## Benchmark (No Recommender System)

Without the recommender system, a consumer who is only aware of product i would purchase product $i , i \in \{ A , B \}$ . A consumer who is aware of both products would purchase the product that yields a higher net utility. A consumer who is aware of neither product would not buy any product. Therefore, the demand functions for the two products can be formulated as:

$$
\begin{array}{l} D _ {A} = \phi_ {A} (1 - \phi_ {B}) + \phi_ {A} \phi_ {B} \frac {p _ {B} - p _ {A} + t}{2 t} \\ D _ {B} = (1 - \phi_ {A}) \phi_ {B} + \phi_ {A} \phi_ {B} \frac {p _ {A} - p _ {B} + t}{2 t} \end{array}\tag{2}
$$

Sellers maximize their profits by choosing their optimal prices and advertising levels:

$$
\max _ {p _ {i}, \phi_ {i}} \pi_ {i} = (1 - \alpha) p _ {i} D _ {i} - a \phi_ {i} ^ {2} / 2\tag{3}
$$

Based on the first-order conditions, we obtain the equilibrium price and advertising level for each seller. The following lemma summarizes the equilibrium outcomes.

Lemma 1 When the marketplace does not use the recommender system, the equilibrium prices, advertising levels, seller profits, and consumer surplus are as follows:

(a) Prices:

$$
p _ {A} ^ {*} = p _ {B} ^ {*} = \sqrt {2 \tau t}\tag{4}
$$

(b) Advertising intensities:

$$
\phi_ {A} ^ {*} = \phi_ {B} ^ {*} = \frac {2 t}{\sqrt {2 \tau t} + t}\tag{5}
$$

(c) Seller profits:

$$
\pi_ {A} ^ {*} = \pi_ {B} ^ {*} = (1 - \alpha) \frac {2 \tau t}{(\sqrt {2 \tau} + \sqrt {t}) ^ {2}}\tag{6}
$$

(d) Consumer surplus:

$$
C S = \frac {4 \sqrt {2 \tau t}}{(\sqrt {2 \tau} + \sqrt {t}) ^ {2}} v + \frac {t ^ {2} - 2 t (\sqrt {2 \tau t} + 4 \tau)}{(\sqrt {2 \tau} + \sqrt {t}) ^ {2}}\tag{7}
$$

Proof. All proofs are in the appendix.

The sellers’ best response functions, $p _ { i } ^ { * } = \left( 2 / \phi _ { i } ^ { * } - 1 \right) t$ , reveal the following insight that drives the results shown in the lemma—seller’s own equilibrium strategies, $p _ { i } ^ { * }$ and ${ \boldsymbol { \phi } } _ { i } ^ { * }$ , are strategic substitutes in the absence of the recommender system. An increase in $\phi$ has two effects on consumers: it decreases the informational differentiation among partially informed consumers, and it decreases the number of uninformed consumers. While the former effect intensifies competition between sellers by enlarging the “common turf”

of consumers that sellers compete for, the latter increases the “monopoly turf” of each seller. We find that the former effect dominates the latter in the equilibrium, leading to a decrease in price when $\phi$ increases. Consequently, in the absence of the recommender system, when advertising cost a increases (which implies ô increases), while the advertising intensities decrease, the product prices increase. Interestingly, seller profits also increase, because the increase in prices offsets the decrease in demands caused by a decrease in advertising intensities. Meanwhile, consumer surplus decreases in the advertising cost because consumers are hurt by the price increase and the demand decrease.

## With Recommender System

When the recommender system is in place, the marketplace observes a signal s regarding the consumer’s preference. Using Bayesian updating, we can derive the marketplace’s expected location for the consumer conditional on the signal being equal to $y _ { 0 }$ to be:

$$
\mathbb {E} (z \mid s = y) = \beta y + \frac {1 - \beta}{2}\tag{8}
$$

Given the signal, the expected consumer net utility from product A is $U _ { \scriptscriptstyle A } = \nu - t \mathbb { E } ( z | s = y )$ $p _ { A }$ and expected consumer net utility from product B is $U _ { B } = \nu - t ( 1 - \mathbb { E } ( z | s = y ) - p _ { B } .$ The recommender system recommends product A if $U _ { A } > U _ { B }$ and recommends product B if $U _ { A } < U _ { B }$ . If $U _ { A } = U _ { B } ,$ then the recommender system recommends either product with equal probability. We denote $y _ { 0 }$ as the marginal signal for which the expected consumer net utility is the same for both products. Using Equation (8), we can derive the marginal signal $y _ { 0 }$ as follows:

$$
y _ {0} = \frac {p _ {B} - p _ {A}}{2 \beta t} + \frac {1}{2}\tag{9}
$$

If the signal is less than $y _ { 0 } ,$ , the recommender system recommends product A; otherwise, it recommends product B.

We next formulate the demand functions for A and B. Suppose $p _ { A } \leq p _ { B } ,$ which implies $z _ { 0 } \ge 1 / 2$ and $y _ { 0 } \geq z _ { 0 } .$ A consumer located between 0 and $z _ { 0 }$ purchases A if she gets an advertisement from A or she is recommended A. The probability that this consumer receives an advertisement from A is $\phi _ { _ A }$ The probability that this consumer does not receive an advertisement about A but is recommended A is $( 1 - \phi _ { { \scriptscriptstyle A } } ) [ \beta + ( 1 -$ $\beta ) y _ { 0 } ]$ Therefore, the demand for A from all consumers located between 0 and $z _ { 0 }$ is $\int _ { 0 } ^ { z _ { 0 } } \biggl [ \phi _ { \it A } + \bigl ( 1 - \phi _ { \it A } \bigr ) \bigl ( \beta + \bigl ( 1 - \beta \bigr ) y _ { 0 } \bigr ) \biggr ] \mathrm { d } z$

Similarly, a consumer located between $z _ { 0 }$ and $y _ { 0 }$ purchases A if and only if she does not receive an advertisement from B and is recommended A, which has the probability $( 1 - \phi _ { B } ) [ \beta$ $+ ( 1 - \beta ) y _ { 0 } ]$ . A consumer located between $y _ { 0 }$ and 1 purchases A if and only if she does not receive an advertisement from B and is recommended A, which has the probability $( 1 - \phi _ { B } ) ( 1$ $- \beta ) y _ { 0 } .$ . Aggregating the demand of each consumer segment, we can derive the demand function of product A as follows:

$$
\begin{array}{r l} D _ {A} & = z _ {0} \left[ (1 - \beta) (1 - y _ {0}) \phi_ {A} + (\beta + (1 - \beta) y _ {0}) \phi_ {B} \right] \\ & + y _ {0} (1 - \phi_ {B}) \end{array}\tag{10}
$$

Using a similar logic, we can derive the demand function of product B when $p _ { A } \leq p _ { B }$ as follows:

$$
\begin{array}{r l} D _ {B} & = (1 - z _ {0}) \left[ \phi_ {B} + (1 - \beta) (1 - y _ {0}) (\phi_ {A} - \phi_ {B}) \right] \\ & + (1 - y _ {0}) \left[ 1 - \phi_ {A} + \beta (\phi_ {A} - \phi_ {B}) \right] \end{array}\tag{11}
$$

We can get the demand function when $p _ { A } > p _ { B }$ using derivation steps analogous to those discussed for the case $p _ { A } \leq p _ { B } .$ After substituting $z _ { 0 }$ from Equation (1) and $y _ { 0 }$ from Equation (9), we have

$$
D _ {A} = \left\{ \begin{array}{l l} \frac {\left(1 - \beta\right) \left(\phi_ {B} - \phi_ {A}\right) \left(p _ {B} - p _ {A}\right) ^ {2} + t \left(p _ {B} - p _ {A}\right) \left[ 2 - \left(1 - \beta^ {2}\right) \phi_ {B} - (1 - \beta) ^ {2} \phi_ {A} \right] + \beta t ^ {2} \left[ 2 - (1 - \beta) \left(\phi_ {B} - \phi_ {A}\right) \right]}{4 \beta t ^ {2}}, & p _ {A} \leq p _ {B} \\ \frac {\left(1 - \beta\right) \left(\phi_ {B} - \phi_ {A}\right) \left(p _ {B} - p _ {A}\right) ^ {2} + t \left(p _ {B} - p _ {A}\right) \left[ 2 - \left(1 - \beta^ {2}\right) \phi_ {A} - (1 - \beta) ^ {2} \phi_ {B} \right] + \beta t ^ {2} \left[ 2 - (1 - \beta) \left(\phi_ {B} - \phi_ {A}\right) \right]}{4 \beta t ^ {2}}, & p _ {A} > p _ {B} \end{array} \right.\tag{12}
$$

$$
D _ {B} = \left\{ \begin{array}{l l} \frac {(1 - \beta) (\phi_ {\mathrm{A}} - \phi_ {\mathrm{B}}) (p _ {B} - p _ {A}) ^ {2} + t (p _ {A} - p _ {B}) [ 2 - (1 - \beta^ {2}) \phi_ {\mathrm{B}} - (1 - \beta) ^ {2} \phi_ {\mathrm{A}} ] + \beta t ^ {2} [ 2 - (1 - \beta) (\phi_ {\mathrm{A}} - \phi_ {\mathrm{B}}) ]}{4 \beta t ^ {2}}, & p _ {A} \leq p _ {B} \\ \frac {(1 - \beta) (\phi_ {\mathrm{A}} - \phi_ {\mathrm{B}}) (p _ {A} - p _ {B}) ^ {2} + t (p _ {A} - p _ {B}) [ 2 - (1 - \beta^ {2}) \phi_ {\mathrm{A}} - (1 - \beta) ^ {2} \phi_ {\mathrm{B}} ] + \beta t ^ {2} [ 2 - (1 - \beta) (\phi_ {\mathrm{A}} - \phi_ {\mathrm{B}}) ]}{4 \beta t ^ {2}}, & p _ {A} > p _ {B} \end{array} \right.\tag{13}
$$

Sellers maximize their profits by choosing their optimal prices and advertising intensities. The following lemma characterizes the equilibrium when the marketplace uses the recommender system.

Lemma 2 When the marketplace uses the recommender system, the equilibrium prices, advertising intensities, seller profits, and consumer surplus are as follows:

(a) Prices:

$$
\hat {p} _ {A} ^ {*} = \hat {p} _ {B} ^ {*} = \frac {2 \tau - 2 \sqrt {\tau^ {2} - \beta (1 - \beta) ^ {2} t \tau}}{(1 - \beta) ^ {2}}\tag{14}
$$

(b) Advertising intensities:

$$
\hat {\phi} _ {A} ^ {*} = \hat {\phi} _ {B} ^ {*} = \frac {1}{2 (1 - \beta)} - \frac {\sqrt {\tau^ {2} - \beta (1 - \beta) ^ {2} t \tau}}{2 \tau (1 - \beta)}\tag{15}
$$

(c) Seller profits:

$$
\hat {\pi} _ {A} ^ {*} = \hat {\pi} _ {B} ^ {*} = (1 - \alpha) \frac {6 \tau + \beta (1 - \beta) ^ {2} t - 6 \sqrt {\tau^ {2} - \beta (1 - \beta) ^ {2} t \tau}}{8 (1 - \beta) ^ {2}}\tag{16}
$$

(d) Consumer surplus:

$$
\hat {C} S = \nu - \frac {2 \left(\tau - \sqrt {\tau^ {2} - \beta (1 - \beta) ^ {2} t \tau}\right)}{(1 - \beta) ^ {2}} - \frac {t}{8} \left(3 - 2 \beta + \frac {\sqrt {\tau^ {2} - \beta (1 - \beta) ^ {2} t \tau}}{\tau}\right)\tag{17}
$$

Examining the sellers’ best response functions when the marketplace uses the recommender system reveals a sharp contrast in how the equilibrium price and advertising intensity of a firm relate to each other in the scenario with the recommender system and the one without. When the recommender system is present, we find that $\hat { \boldsymbol p } _ { i } ^ { * } = \beta t \biggl / \biggl [ 1 - \bigl ( 1 - \beta \bigr ) \hat { \phi } _ { i } ^ { * } \biggr ]$ , which implies $\hat { p } _ { i } ^ { * }$ and $\hat { \phi } _ { i } ^ { * }$ are strategic complements. Therefore, the presence of the recommender system alters the relationship between price and advertising intensity fundamentally, from strategic substitutes to strategic complements. The reason for this switch is as follows. In the presence of the recommender system, price, in addition to advertising, plays a role in determining the extent of informational differentiation among consumers: a price decrease by a seller generates more recommendations in his favor and hence an informational advantage for him among uninformed consumers and partially informed consumers that were aware of his product, ceteris paribus. On the other hand, recommendations and hence prices do not alter the informational differentiation among fully informed consumers. An increase in advertising intensity increases the size of the fully informed consumer segment, and reduces the total size of the uniformed consumer segment and the partially informed segment that is aware of only one product. Consequently, when advertising intensity increases, the marginal impact of price on informational differentiation through recommendations decreases. Therefore, an increase in advertising intensity leads to an increase in price. In sharp contrast to the case without a recommender system, because of the strategic complementarity between price and advertising intensity in the presence of the recommender system, when advertising cost increases, the advertising levels decrease, but the product prices and seller profits decrease and consumer surplus increases.

## Impacts of the Recommender System

We next examine the impacts of the recommender system by comparing equilibrium outcome in the scenarios with and without the recommender system.

Proposition 1 Compared to the scenario without the recommender system, in the presence of the recommender system:

(a) sellers’ advertising intensity is lower; that is, $\hat { \phi } _ { i } ^ { * } \leq \phi _ { i } ^ { * }$

(b) product price is lower; that is, $\hat { \boldsymbol { p } } _ { i } ^ { * } \le p _ { i } ^ { * }$

$$
\begin{array}{l} \text {(c)} \quad \text {the sellers are better off (i.e.,} \hat {\pi} _ {i} ^ {*} > \pi_ {i} ^ {*}) \text {if and only if} \\ \frac {\beta t}{8} + \frac {3 \left[ \tau - \sqrt {\tau^ {2} - \beta \tau t (1 - \beta) ^ {2}} \right]}{4 (1 - \beta) ^ {2}} > \frac {2 t \tau}{(\sqrt {2 \tau} + \sqrt {t}) ^ {2}}; \end{array}
$$

(d) consumer surplus is higher.

Proposition 1(a) shows that sellers would reduce advertising intensity in the presence of the recommender system. This finding supports the notion that the recommender system functions as a substitute to traditional advertising, which also suggests that using traditional advertising is too costly for sellers to mitigate the potential informational disadvantage resulting from recommendations received by the competitor. We call the impact of recommender system on sellers’ advertising the advertising effect. Proposition 1(b) shows that sellers would lower product prices in the presence of recommender system, indicating that recommender system intensifies the competition between sellers. We call this effect the competition effect of the recommender system. The competition effect stems from two driving forces. The direct driver is that sellers have incentive to use price as a lever to attract more recommendations and increase their informational advantage. This incentive tends to increase the competition. Furthermore, because the recommender system alters the relationship between equilibrium price and equilibrium advertising level from strategic substitutability to strategic complementarity, the advertising effect of the recommender system indirectly contributes to the competition effect as well.

Proposition 1(c) reveals that the recommender system does not always benefit sellers. While the competition effect hurts sellers, the advertising effect resulting from the “free” advertising provided by the recommender system reduces sellers advertising cost and benefits sellers. The tradeoff between these two determines whether sellers benefit from the recommender system. Figure 1 illustrates Proposition 1(c), and shows that the recommender system is more likely to benefit sellers when the recommender system precision is high and, surprisingly, the advertising cost is relatively low. One would intuitively expect that the free advertising offered by the recommender system will benefit sellers when the cost of traditional advertising is high. The explanation for this counterintuitive finding is the alteration of the relationship between advertising intensity and price by the recommender system as explained earlier—as a result of the strategic substitution relationship, an increase in advertising cost increases sellers’ profit in the no-recommender system scenario; in contrast, as a result of the strategic complementarity relationship, an increase in advertising cost decreases the sellers’ profit in the recommender system scenario. Therefore, an increase in advertising cost reduces the benefit offered by the recommender system to sellers.

![](/api/attachments/QTH8AQJ8/fulltext/images/91b17f420fa23b7bee0dc9ccc41a6b6881224b6da8d529e1ebfdc09fe04aa644.jpg)  
Figure 1. Impact of Recommender System on Seller Profits under Uniform Advertising (v = 2.8, t = 1, and á = 0.1)

Proposition 1(d) shows that the recommender system always benefits consumers. Three factors contribute to this result. First, the recommender system expands the market by increasing consumer awareness, and more consumers make a purchase in the presence of recommender system. Second, the competition between two sellers increases in the presence of recommender system, which drives the prices down. Third, by recommending the product which offers a higher expected utility for the consumer, the recommender system reduces consumers’ misfits costs.

Clearly, the recommender system precision plays an important role in determining whether sellers and the marketplace benefit from the recommender system. We examine the role of recommender system precision next.

Proposition 2 The impact of recommendation precision $\beta$ is as follows:

(a) $\hat { \boldsymbol { p } } _ { i } ^ { * }$ increases in $\beta ;$

(b) $\hat { \phi } _ { i } ^ { * }$ follows an inverse U-shape with $\beta ,$ that $i s ,$ $\hat { \sigma } \hat { \phi } _ { i } ^ { * } \big / \hat { \sigma } \beta > 0$ if and only $i f 4 \tau ( 1 - 2 \beta ) > ( 1 - \beta ) ^ { 4 } t ;$

(c) $\hat { \pi } _ { i } ^ { * }$ increases in $\beta ;$

(d) $\hat { C } S$ decreases in $\beta .$

Proposition 2(a) shows that an increase in the recommender system precision softens the price competition between sellers. Intuitively, regardless of the recommender system precision, a decrease in the price of a product increases the likelihood of that product being recommended, ceteris paribus. However, the marginal increase in this likelihood is greater when the recommender system precision is low than when it is high. When the precision is low, the recommender system only has a rough idea about consumer preference and thus relies more on prices in recommending product. Technically, when the precision is low, from the recommender system’s perspective, most consumers are concentrated in the middle of the Hotelling line (as reflected by the expected location in Equation (8)), and therefore a small decrease in the price of a product induces recommendation of that product to a large number of consumers (as seen in the marginal signal in Equation (9)). Consequently, sellers’ incentives to compete on price are higher when recommender system precision is low than when it is high.

Proposition 2(b) indicates that firm’s advertising intensity follows an inverse U-shape with recommender system precision, as shown in Figure 2. An increase in recommendation precision $\beta$ has two implications for the sellers’ advertising choices. First, an increase in $\beta$ increases the price as suggested by Proposition 2(a), and thus sellers can make more profit from each additional consumer they get, which induces sellers to advertise more to get more demand. Second, an increase in $\beta$ decreases the marginal demand each seller gets from additional advertising. For instance, we consider the extreme situation when recommender system has perfect preciprecision $( \mathrm { i . e . , } \beta = 1 )$ . In this case, because consumers buy only the product recommended to them, a seller’s advertising has no impact on his demand, which discourages sellers from advertising. The same reasoning applies to the general case with imperfect precision. The two implications work in the opposite direction, and the relationship between $\hat { \phi } _ { i } ^ { * }$ and $\beta$ varies depending on which implication dominates. Proposition 2(b) states that the first (second) implication dominates the second (first) implication when precision is low (high).

![](/api/attachments/QTH8AQJ8/fulltext/images/e96b6d75cf034f89a66ee314f0eddc4f12af8968964f76d109666847efb26d8b.jpg)  
Figure 2. Effect of Recommendation Precision on Advertising Intensity under Uniform Advertising (t = 1 and ô = 0.6)

Propositions 2(c) and (d) imply that sellers benefit but consumers are hurt from an improvement in recommender precision. The primary driver of these two results is the softening of the price competition induced by an increase in recommender system precision.

## Targeted Advertising

In the previous section, we examined the case in which sellers use uniform advertising and do not target consumers; that is, every consumer has the same probability of receiving the advertisement from a seller. Over years, sellers have increasingly been able to target advertising to specific consumers. In this section, we investigate how targeted advertising by sellers would affect the implications of the recommender system.

The approach we use to model the targeting ability of sellers is similar to that we use for the recommender system. In particular, for a consumer located at z, seller i receives signal $\eta _ { i }$ about z. The probability that the signal equals the consumer’s true location is $\gamma ;$ that is, $P ( z = y | \eta _ { i } = y ) = \gamma ;$ otherwise, the signal is uninformative and follows the prior distribution of z.

A larger ã indicates that firms have a better targeting ability. We assume that both sellers have the same targeting precision and that their signals are conditionally independent given the true location. We assume that the sellers use the signal only to target their advertising, but they do not engage in price discrimination; that is, each charges the same price for all consumers.

The timeline for the game under targeted advertising is as follows. In stage 1, sellers set prices and advertising strategies simultaneously. In stage 2, sellers observe private signals about consumer locations, and follow the advertising strategies made in stage 1. In stage 3, consumers visit the marketplace. If the marketplace employs a recommender system, then the recommender system makes the recommendation following the same policy discussed in the “Model” section. Finally, consumers purchase the product based on their awareness and preferences. We use Bayesian Nash Equilibrium (BNE) as the solution concept.

In order to obtain an interior equilibrium in both with- and without-recommendation scenarios, we make the following technical assumption.

Assumption 3: $2 t \leq \tau$

## No Recommender System

Following the standard procedure to derive a BNE, we first propose each seller’s set of beliefs, derive rational strategies for sellers under this belief set, and then show that their strategies and beliefs are consistent with each other (e.g., Vives 1984). Without loss of generality, we first examine seller’s optimization problem in stage 1. We consider the following belief about seller B’s strategy as function of its signal $\eta _ { B } .$

$$
\phi_ {B} \left(\eta_ {B}\right) = \left\{ \begin{array}{l l} \phi_ {B} ^ {L}, & \text { if } \eta_ {B} \leq z _ {0} \\ \phi_ {B} ^ {H}, & \text { if } \eta_ {B} > z _ {0} \end{array} \right.\tag{18}
$$

where $\phi _ { B } ^ { L }$ and $\phi _ { B } ^ { H }$ are constants. We denote $\mathbb { E } [ \pi _ { A } | \eta _ { A } ]$ as the expected profit function of seller A conditional on its own signal $\eta _ { A } ,$ which can be formulated as follows:

$$
\begin{array}{r l} & {\mathbb {E} \left[ \pi_ {_ A} \mid \eta_ {_ A} \right] = (1 - \alpha) p _ {_ A} \phi_ {_ A} \left[ \int_ {0} ^ {z _ {0}} f (z \mid \eta_ {_ A}) \mathrm{d} z + \right.} \\ & {\qquad \left. \int_ {z _ {0}} ^ {1} (1 - \mathbb {E} \left[ \phi_ {_ B} (\eta_ {_ B}) \mid z \right]) f (z \mid \eta_ {_ A}) \mathrm{d} z \right] - \frac {a}{2} \phi_ {_ A} ^ {2}} \end{array}\tag{19}
$$

where $f ( z | \eta _ { A } )$ is the probability density function of location z given signal $\eta _ { A } .$ Under $\boldsymbol { A } ^ { * } \boldsymbol { \mathrm { s } }$ belief about $B ^ { \prime } { \bf s }$ strategy, the expected advertising intensity of seller B is

$$
\mathbb {E} \left[ \phi_ {B} (\eta_ {B}) | z \right] = \phi_ {B} ^ {L} (1 - \gamma) z _ {0} + \phi_ {B} ^ {H} [ \gamma + (1 - \gamma) (1 - z _ {0}) ]\tag{20}
$$

when $z _ { 0 } < z < 1$ . Given $\eta _ { A } ,$ , seller A chooses advertising intensity to maximize $\mathbb { E } \left[ \phi _ { B } \vert \eta _ { A } \right]$ . Substituting Equation (20) into A’s profit function and maximizing it, we derive the following optimal advertising strategy for seller A:

$$
\phi_ {A} ^ {*} \left(\eta_ {A}\right) = \left\{ \begin{array}{l l} p _ {A} \left[ \frac {1}{\tau} + \frac {(1 - \gamma) (p _ {B} - p _ {A} - t)}{4 t ^ {2} \tau} s \right], & \text { if } \eta_ {A} \leq z _ {0} \\ p _ {A} \left[ \frac {1}{\tau} + \frac {\left((1 - \gamma) (p _ {B} - p _ {A} - t) - 2 \gamma t\right)}{4 t ^ {2} \tau} s \right], & \text { if } \eta_ {A} > z _ {0} \end{array} \right.\tag{21}
$$

where $S \equiv \Big ( \phi _ { B } ^ { L } - \phi _ { B } ^ { H } \Big ) \big ( 1 - \gamma \big ) \big ( p _ { B } - p _ { A } + t \big ) + 2 t \phi _ { B } ^ { H }$

Denoting A’s advertising intensity when $\eta _ { _ { A } } \leq z _ { _ { 0 } }$ as $\phi _ { A } ^ { H }$ and A’s advertising intensity when $\eta _ { _ A } > z _ { 0 }$ as $\phi _ { _ { A } } ^ { L }$ , we verify that the sellers’ strategies and belief sets are consistent with each other. In stage 1, each seller sets product price by maximizing the overall expected profit function:

$$
\max _ {p _ {i}} \mathbb {E} (\pi_ {i}) = \int_ {0} ^ {1} \mathbb {E} (\pi_ {i} | \eta_ {i}) f (\eta_ {i}) \mathrm{d} \eta_ {i}\tag{22}
$$

We summarize the symmetric BNE as the following lemma.

Lemma 3 In the absence of the recommender system, the BNE prices, advertising intensities, seller profits, and consumer surplus when sellers use targeted advertising are as follows:

(a) Prices: $p _ { A } ^ { * } = p _ { B } ^ { * } = p ^ { * }$ where $p ^ { * }$ is the real root of

$$
\begin{array}{c} p ^ {4} \left(\gamma^ {4} - \gamma^ {3}\right) + p ^ {3} \tau \gamma (1 - 2 \gamma) + p ^ {2} \tau (2 \tau - \gamma^ {4} t - \gamma^ {2} t) + \\ 4 p t \tau^ {2} \gamma^ {2} - 4 t \tau^ {3} = 0 \end{array}\tag{23}
$$

(b) Advertising intensities:

$$
\phi_ {A} ^ {H ^ {*}} = \phi_ {B} ^ {H ^ {*}} = \phi^ {H ^ {*}} = \frac {p ^ {*} [ 2 \tau + (1 - \gamma) \gamma p ^ {*} ]}{\tau [ 2 \tau + (1 - \gamma^ {2}) p ^ {*} ]}\tag{24}
$$

$$
\phi_ {A} ^ {L ^ {*}} = \phi_ {B} ^ {L ^ {*}} = \phi^ {L ^ {*}} = \frac {p ^ {*} [ 2 \tau - (1 + \gamma) \gamma p ^ {*} ]}{\tau [ 2 \tau + (1 - \gamma^ {2}) p ^ {*} ]}\tag{25}
$$

(c) Seller profits:

$$
\pi_ {A} ^ {*} = \pi_ {B} ^ {*} = (1 - \alpha) \frac {(p ^ {*}) ^ {2} \left[ (\gamma^ {4} + \gamma^ {2}) (p ^ {*}) ^ {2} - 4 \gamma^ {2} p ^ {*} \tau + 4 \tau^ {2} \right]}{2 \tau ((1 - \gamma^ {2}) p ^ {*} + 2 \tau) ^ {2}}\tag{26}
$$

(d) Consumer surplus:

$$
C S = p ^ {*} \frac {4 (v - p ^ {*}) [ \gamma^ {2} (\gamma^ {2} + 1) (p ^ {*}) ^ {2} - 4 \gamma^ {2} \tau p ^ {*} + 4 \tau^ {2} ] - t [ 3 \gamma^ {2} (\gamma^ {2} + 1) (p ^ {*}) ^ {2} - 2 \tau (5 \gamma^ {2} + 1) p ^ {*} + 8 \tau^ {2} ]}{2 \tau (2 \tau + (1 - \gamma^ {2}) p ^ {*}) ^ {2}}\tag{27}
$$

A few observations are worth highlighting. First, when $\gamma = 0 ,$ the targeted advertising case reduces to the uniform advertising case where sellers set the same adverting intensity for all consumers. Second, similar to that under the uniform advertising in the absence of a recommender system, when sellers use targeted advertising, an increase in advertising cost decreases advertising intensity to all consumers, increases product prices and seller profits, and decreases consumer surplus. Third, $\phi ^ { H ^ { * } } \geq \phi ^ { L ^ { * } }$ , which implies that a seller advertises more to consumers that are located closer to him as indicated by the signal. Furthermore, as targeting precision improves, sellers increase the differentiation in advertising intensity between consumers located closer to them vis-à-vis those located closer to their competitor.

Although an increase in precision enables the sellers to target consumers more effectively, we find that it does not always increase their profits. In particular, improving targeting precision hurts sellers when the precision is low. Two drivers contribute to the impact of targeting precision on seller profits. One, an increase in targeting precision induces sellers to increase their overall advertising and hence the advertising costs. Two, sellers may engage in more intense competition to attract marginal consumers that are located closer to their competitor in response to a reduction in their own advertising and an increase in competitor’s advertising to those consumers. The second driver is particularly strong when the targeting precision is low or the cost of advertising is low. On the other hand, consumers always benefit with better targeting by sellers because more consumers become aware of at least one product when sellers increase their overall advertising.

## With Recommender System

When the recommender system is in place, we find that sellers use a similar strategy as in the scenario without recommender system. We present the detailed derivation in the appendix and summarize the equilibrium in the following lemma.

Lemma 4 When the marketplace uses the recommender system, the BNE prices, advertising intensities, seller profits, and consumer surplus under targeted advertising are as follows:

(a) Prices:

$$
\hat {p} _ {A} ^ {*} = \hat {p} _ {B} ^ {*} = \frac {2 \tau - 2 \sqrt {\tau^ {2} - t \tau \beta (1 - \beta) ^ {2} [ (1 + \beta) \gamma^ {2} + 1 - \beta \gamma / 2 ]}}{(1 - \beta) ^ {2} [ (1 + \beta) \gamma^ {2} + 1 - \beta \gamma / 2 ]}\tag{28}
$$

(b) Advertising intensities:

$$
\hat {\phi} _ {A} ^ {H ^ {*}} = \hat {\phi} _ {B} ^ {H ^ {*}} = \hat {\phi} ^ {H ^ {*}} = (1 + \gamma) \frac {\tau - \sqrt {\tau^ {2} - t \tau \beta (1 - \beta) ^ {2} [ (1 + \beta) \gamma^ {2} + 1 - \beta \gamma / 2 ]}}{2 \tau (1 - \beta) [ (1 + \beta) \gamma^ {2} + 1 - \beta \gamma / 2 ]}\tag{29}
$$

$$
\hat {\phi} _ {A} ^ {L ^ {*}} = \hat {\phi} _ {B} ^ {L ^ {*}} = \hat {\phi} ^ {L ^ {*}} = (1 - \gamma) \frac {\tau - \sqrt {\tau^ {2} - t \tau \beta (1 - \beta) ^ {2} [ (1 + \beta) \gamma^ {2} + 1 - \beta \gamma / 2 ]}}{2 \tau (1 - \beta) [ (1 + \beta) \gamma^ {2} + 1 - \beta \gamma / 2 ]}\tag{30}
$$

(c) Seller profits:

$$
\hat {\pi} _ {A} ^ {*} = \hat {\pi} _ {B} ^ {*} = \beta t \tau (1 - \alpha) \frac {8 \tau + 8 \sqrt {\tau^ {2} - t \tau \beta (1 - \beta) ^ {2} [ (1 + \beta) \gamma^ {2} / 2 ]} - \beta t (1 - \beta) ^ {2} (1 + \gamma^ {2})}{8 (\sqrt {\tau^ {2} - t \tau \beta (1 - \beta) ^ {2} [ (1 + \beta) \gamma^ {2} + 1 - \beta \gamma / 2 ]} + \tau) ^ {2}}\tag{31}
$$

(d) Consumer surplus:

$$
\hat {C} S = v - \frac {t (2 - \beta)}{4} - \frac {\tau - \sqrt {\tau^ {2} - t \tau \beta (1 - \beta) ^ {2} [ (1 + \beta) \gamma^ {2} + 1 - \beta \gamma / 2 ]}}{(1 + \beta) \gamma^ {2} + 1 - \beta \gamma / 2} \left[ \frac {2}{(1 - \beta) ^ {2}} - \frac {t (1 + \gamma^ {2})}{8 \tau} \right]\tag{32}
$$

Similar to the scenario without recommender system under targeted advertising, we notice that, first, when ã = 0 the targeted advertising case reduces to the uniform advertising case. Second, as same as under the uniform advertising, an increase in advertising cost decreases advertising intensity to all consumers, and decreases product prices and seller profits. Third, sellers advertise more to consumers that are located closer to them.

## Impacts of the Recommender System

In this section, we compare the equilibrium outcome in Lemmas 3 and 4 to derive the implications of the recommender system when sellers use targeted advertising.

Proposition 3 When sellers use targeted advertising, compared to the scenario without the recommender system, in the presence of the recommender system:

(a) each product’s price is lower; that is, $\hat { p } _ { i } ^ { * } \leq p _ { i } ^ { * } , i \in \left\{ A , B \right\}$

(b) each product’s advertising intensity is lower; that is, $\hat { \phi } ^ { H ^ { * } }$ is lower than $\phi ^ { H ^ { * } }$ , and $\hat { \phi } ^ { L ^ { * } }$ is lower than $\phi ^ { L ^ { * } }$ ;

(c) the firms is better off if and only if $\beta > \tilde { \beta }$ , where $\tilde { \beta }$ is the root of

$$
\begin{array}{r l} & \frac {8 \tau + 8 \sqrt {\tau^ {2} - t \tau \beta (1 - \beta) ^ {2} \left[ (1 + \beta) \gamma^ {2} + 1 - \beta \gamma / 2 \right]} - \beta t (1 - \beta) ^ {2} (1 + \gamma^ {2})}{(p ^ {*}) ^ {2} \left[ (\gamma^ {4} + \gamma^ {2}) (p ^ {*}) ^ {2} - 4 \gamma^ {2} \tau p ^ {*} + 4 \tau^ {2} \right]} \\ & = \frac {4 (\sqrt {\tau^ {2} - t \tau \beta (1 - \beta) ^ {2} [ (1 + \beta) \gamma^ {2} + 1 - \beta \gamma / 2 ]} + \tau) ^ {2}}{\beta t (2 \tau^ {2} + (1 - \gamma^ {2}) \tau p ^ {*}) ^ {2}} \end{array}
$$

(d) consumer surplus is higher.

We find that the impacts of the recommender system on price competition and advertising intensity are qualitatively identical in the targeted and uniform advertising cases—namely, the recommender system induces both competition effect and advertising effect on sellers in both cases. The impact of the recommender system on seller profit is also similar in both cases except that the sellers’ targeting precision also plays a role in determining whether sellers benefit from the recommender system under targeted advertising. Proposition 3(c) is illustrated by Figure 3. For any fixed targeting precision, the recommender system would make sellers better off only when recommender system has a high precision, and this result is similar to that we find in the uniform advertising case. An improvement in targeting precision first increases the area in the parameter space where the recommender system benefits sellers, but when targeting precision is sufficiently high, improving targeting precision decreases the area where the recommender system benefits sellers. This finding reveals that when the marketplace deploys a recommender system—a common current business practice—improving their own targeting precision may not necessarily offset the negative impacts of the recommender system on sellers. In contrast, this strategy can worsen the impact of the recommender system.

Clearly, both the recommender system precision and the sellers’ targeting precision play important roles in determining the equilibrium in the presence of the recommender system under targeted advertising. We examine the impacts of these two precisions next.

Proposition 4 When sellers use targeted advertising, in the presence of the recommender system,

![](/api/attachments/QTH8AQJ8/fulltext/images/ca0d0ae305728b66333327271b04bff004083236445668c3ba863579b23f8829.jpg)  
Figure 3. Impact of Recommender System on Seller Profits under Targeted Advertising (t = 1 and ô = 2)

![](/api/attachments/QTH8AQJ8/fulltext/images/dddeafe8acb82b121388ccdd9331da814566266f1894bc38bb403723265a4b5a.jpg)  
(a) Effect of ã on $\hat { \boldsymbol { p } } _ { i } ^ { * }$

![](/api/attachments/QTH8AQJ8/fulltext/images/c10778cea105d24a797ee950c28fd971f7e76e2a4d60fd351405982f46d8dda1.jpg)  
(b) Effect of ã on $\hat { \phi } ^ { H ^ { * } }$ and $\hat { \phi } ^ { L ^ { * } }$

![](/api/attachments/QTH8AQJ8/fulltext/images/1fade9b5b53058913781a65dba1239be168f488bc1a0c78d4caa049509e1f36d.jpg)  
(c) Effect of ã on $\hat { \pi } _ { i } ^ { * }$

![](/api/attachments/QTH8AQJ8/fulltext/images/02867e804f630ad5cf0bec47660982bd8ef229c237ba3805afd6ebb96a0d6ed1.jpg)  
(d) Effect of ã on  
Figure 4. Effect of Targeting Precision in the Presence of Recommender System (t = 1, á = 0.1, ô = 2, â = 0.7, and v =2.8)

(a) $\hat { \boldsymbol { p } } _ { i } ^ { * }$ increases in $\beta ;$

(b) $\hat { \phi } ^ { H ^ { * } }$ and $\hat { \phi } ^ { L ^ { * } }$ follow an inverse U-shape with $\beta ;$ that $i s ,$ , $\hat { \partial } \hat { \phi } ^ { H ^ { * } } / \hat { \sigma } \beta > 0$ and $\hat { \partial } \hat { \phi } ^ { L ^ { * } } / \hat { \sigma } \beta > 0$ if and only if 4τ(1−2β)(2βγ² − βγ + γ /2 +1)>(1− β) (γ² +1) t;

(c) $\hat { \pi } _ { i } ^ { * }$ increases in $\beta ;$

(d) $\hat { C } S$ decreases in $\beta .$

Comparing Proposition 4 with Proposition 2, we find that the recommender system precision has the same qualitative impact on sellers and consumers when sellers use targeted advertising and when they use uniform advertising. The following result shows the impact of sellers’ targeting precision.

Proposition 5 When sellers use targeted advertising, in the presence of the recommender system,

(a) $\hat { \boldsymbol p } _ { i } ^ { * }$ first decreases and then increases in $\gamma ;$ that $i s ,$ ${ \hat { \sigma } } { \hat { p } } _ { i } ^ { * } / { \hat { \sigma } } \gamma < 0$ if and only if $\gamma < \beta / ( 4 + 4 \beta ) ,$

(b) $\hat { \phi } ^ { H ^ { * } }$ increases in ã and $\hat { \phi } ^ { L ^ { * } }$ decreases in $\gamma ;$

(c) $\hat { \pi } _ { i } ^ { * }$ first decreases and then increases in ã; that $i s ,$

$\partial \hat { \pi } _ { i } ^ { * } / \partial \gamma < 0$ if and only if $\gamma < \tilde { \gamma }$ , where $\tilde { \gamma }$ is the root of 4(4βγ +3γ − β)√τ2 −tτβ(1− β)2[(1+ β)γ2 +1− βγ /2]+τ] −(1−β)2 β²t(γ2 +4γ −1)= 0

(d) increases in ã if and only if

$$
\begin{array}{l} 8 \gamma \sqrt {\tau^ {2} - t \tau \beta (1 - \beta) ^ {2} [ (1 + \beta) \gamma^ {2} + 1 - \beta \gamma / 2 ] +} \\ 8 \tau [ 2 \beta^ {2} - 8 \beta (1 + \beta) \gamma + \gamma ] > \\ \beta (1 - \beta) ^ {2} t (4 \beta \gamma^ {3} - 3 \beta \gamma^ {2} - 4 \beta \gamma + \beta + 4 \gamma^ {3} + 4 \gamma) \end{array}
$$

Figure 4 illustrates Proposition 5. It is intuitive that an improvement in sellers’ targeting precision increases the differentiation in sellers’ advertising intensities for consumers located closer to them vis-à-vis those located closer to the competitor. While an improvement in targeting precision intensifies the price competition when the targeting precision is low, it softens the price competition beyond a threshold value. Consequently, sellers start to benefit from improved targeting precision when precision is sufficiently high. While an increase in sellers’ targeting precision benefits consumers when there is no recommender system, it can hurt consumers when the recommender system is present. The primary reason for this difference is that all consumers are aware of at least one product when the marketplace deploys a recommender system and hence an increase in targeting precision does not increase the total demand—the key reason for the higher consumer surplus under a higher targeting precision when there is no recommender system. Propositions 4 and 5 also show that the impacts of an increase in targeting precision and recommender system precision can be different even though both seller targeting and recommender system seek to identify consumer preferences. The primary reason for the difference is that the nature of price competition is different in these two modes of consumer targeting.

## Seller Targeting in the Presence of the Recommender System

The previous analysis shows how the deployment of a recommender system by the marketplace affects the sellers when they use uniform advertising and when they use targeted advertising, respectively. Given that recommender systems have been ubiquitous in marketplaces and targeting advertising has emerged as a viable option, one question becomes particularly pertinent: in the presence of the recommender system, under what conditions should sellers adopt targeted advertising? Furthermore, if sellers adopt targeted advertising, how does their targeting precision affect the impact of the recommender system? In this section, we shed light to these questions.

Proposition 6 In the presence of the recommender system,

(a) when $\gamma > \beta / ( 2 \beta + 2 )$ , the price under targeted advertising is higher than that under uniform advertising;

(b) the advertising intensity under uniform advertising is between $\hat { \phi } _ { \ / L }$ and $\hat { \phi } _ { \scriptscriptstyle H }$ under targeted advertising;

(c) when $\gamma > \gamma _ { 1 }$ , the seller’s profit under targeted advertising is higher than that under uniform advertising, where $\gamma _ { 1 }$ is the root to

$$
\begin{array}{r l} & \frac {\beta_ {t}}{8} + \frac {3 \left[ \tau - \sqrt {\tau^ {2} - \beta \tau t (1 - \beta) ^ {2}} \right]}{4 (1 - \beta) ^ {2}} \\ = & \beta \tau \frac {\tau + \sqrt {\tau^ {2} - t \tau \beta (1 - \beta) ^ {2} [ (1 + \beta) \gamma^ {2} + 1 - \beta \gamma / 2 ]} - \beta t (1 - \beta) ^ {2} (1 + \gamma^ {2}) / 8}{\left(\sqrt {\tau^ {2} - t \tau \beta (1 - \beta) ^ {2} [ (1 + \beta) \gamma^ {2} + 1 - \beta \gamma / 2 ]} + \tau\right) ^ {2}} \end{array}\tag{33}
$$

(d) the consumer surplus under targeted advertising is higher than that under uniform advertising if and only $i f$

$$
\frac {\left[ \tau - \sqrt {\tau^ {2} - t \tau \beta (1 - \beta) ^ {2} ((1 + \beta) \gamma^ {2} + 1 - \beta \gamma / 2)} \right] \left[ t (1 + \gamma^ {2}) (1 - \beta) ^ {2} - 1 6 \tau t \right]}{(1 + \beta) \gamma^ {2} + 1 - \beta \gamma / 2} > \left[ \tau - \sqrt {\tau^ {2} - t \tau \beta (1 - \beta) ^ {2}} \right] \left[ t (1 - \beta) ^ {2} - 1 6 \tau \right]\tag{34}
$$

![](/api/attachments/QTH8AQJ8/fulltext/images/e09142355c2802ac9f78b9befabdb947cce0fd0633b27972bff6f41ef96f4095.jpg)  
(a) Effect of ã on Äp

![](/api/attachments/QTH8AQJ8/fulltext/images/b11fdd509a2f10152d646a5d0800cee402a2f63c082a7b91acee5c5e58033fe7.jpg)

![](/api/attachments/QTH8AQJ8/fulltext/images/d0a71c58882ee47375edf60b491fb465caaadda9fe4eaf000e8d29a25c6f8549.jpg)  
(c) Effect of ã on Äð

(b) Effect of ã on Ä  
![](/api/attachments/QTH8AQJ8/fulltext/images/edf6e465f0468a00698397cd62357ac613a2e0eb0d8b2a05a9586aed485a585f.jpg)  
(d) Effect of ã on ÄCS  
Figure 5. Effect of Targeting Precision on the Impact of Recommender System (t = 1, á = 0.1, ô = 2.1, and â = 0.9)

The above proposition shows that in the presence of the recommender system, the sellers can benefit from using targeted advertising, compared to uniform advertising, only when the targeting precision is high (Proposition 6(c)). This benefit comes from two sources. First, when the targeting precision is high, the price competition is softened (Proposition 6(a)). Second, targeting efficiency may save the advertising costs for sellers (Proposition 6(b)).

Next, we numerically illustrate the role of targeting precision in the impact of the recommender system (because of the lack of closed-from solutions). We denote the impact of the recommender system on seller’s profit, price competition, advertising intensity, and consumer surplus as $\Delta \pi _ { i } = \hat { \pi } _ { i } ^ { * } - \pi _ { i } ^ { * }$ $\Delta p _ { i } = \hat { p } _ { i } ^ { * } - p _ { i } ^ { * } , \Delta \phi = \left( \hat { \phi } ^ { H ^ { * } } + \hat { \phi } ^ { L ^ { * } } \right) \left/ 2 - \left( \phi _ { A } ^ { H ^ { * } } + \phi _ { A } ^ { L ^ { * } } \right) \right/ 2$ , and $\Delta C S = \hat { C } S ^ { ^ { * } } - C S ^ { ^ { * } }$ , respectively.

Figure 5 illustrates the results. Figure 5(a) indicates that an increases in ã may increase or decrease the competition effect based on targeting precision; the intensification of price competition by the recommender system is weaker when the targeting precision is low. Figure 5(b) indicates that the decrease in the average advertising intensity caused by the recommender system is weakened by an increase in the targeting precision; that is, the positive advertising effect of recommender system is reduced when sellers implement targeted advertising. As a result of these two effects, an increase in the targeting precision enhances (mitigates) the positive (negative) impact of the recommender system only when the precision is not too high. The results demonstrate that in the presence of a recommender system, there is an optimal level of targeting precision for sellers. Because of nonmonotonicity in the change of the competition effect, the impact of targeting precision on the change of consumer surplus because of the recommender system is also nonmonotonic, as illustrated in Figure 5(d).

## Model Extension

In the main model, we consider the case when the recommender system recommends the product that offers a higher consumer net utility. Essentially, the recommender system assigns an equal weight to the misfit cost and price in its recommendation strategy. In this section, we consider a more general model in which the recommender system can assign a higher weight to the misfit cost compared to price. In particular, we assume that the relative weight assigned to price in the recommendation score used to choose the recommendation is $k , 0 \leq k \leq 1$ . From the platform’s perspective, we define the consumer benefit for a consumer located at x as V – $x t - k p _ { A }$ if the consumer purchases product A and $V - ( 1 - x ) t$ $- k p _ { B }$ if the consumer purchases product B, where $k \in [ 0$ , 1]. Two special cases are worth highlighting. When k = 1, the general model reduces to the baseline model. When $k = 0 ,$ , the recommender system uses only the misfit cost to choose recommendations. We present the results only for the case when sellers use uniform advertising. The following lemma summarizes the equilibrium outcomes in the presence of recommender system.

Lemma 5 When the marketplace uses the recommender system which assigns a relative weight of k for product price, the equilibrium prices, advertising intensities, seller profits, and consumer surplus are as follows:

(a) Prices:

$$
\hat {p} _ {A} ^ {*} = \hat {p} _ {B} ^ {*} = \frac {2 \left[ k \tau - \sqrt {k ^ {2} \tau^ {2} - (1 - \beta) (k - \beta) \beta t \tau} \right]}{(1 - \beta) (k - \beta)}\tag{35}
$$

(b) Advertising intensities:

$$
\hat {\phi} _ {A} ^ {*} = \hat {\phi} _ {B} ^ {*} = \frac {k}{2 (k - \beta)} - \frac {\sqrt {k ^ {2} \tau^ {2} - (1 - \beta) (k - \beta) \beta t \tau}}{2 \tau (k - \beta)}\tag{36}
$$

(c) Seller profits:

$$
\begin{array}{r l} \hat {\pi} _ {A} ^ {*} = & \hat {\pi} _ {B} ^ {*} = (1 - \alpha) \frac {\beta (1 - \beta) t}{8 (k - \beta)} \\ & + (1 - \alpha) \frac {(\beta k + 3 k - 4 \beta) [ k \tau - \sqrt {k ^ {2} \tau^ {2} - (1 - \beta) (k - \beta) \beta t \tau} ]}{4 (1 - \beta) (k - \beta) ^ {2}} \end{array}\tag{37}
$$

(d) Consumer surplus:

$$
\begin{array}{l} \hat {C S} = v - \frac {2 \left[ k \tau - \sqrt {k ^ {2} \tau^ {2} - (1 - \beta) (k - \beta) \beta t \tau} \right]}{(1 - \beta) (k - \beta)} - \frac {t}{4} \\ - \frac {\left[ 2 \tau (k - \beta) - k \tau - \sqrt {k ^ {2} \tau^ {2} - (1 - \beta) (k - \beta) \beta t \tau} \right] (1 - \beta) t}{8 \tau (k - \beta)} \end{array}\tag{38}
$$

Similarly, we can examine the impacts of the recommender system by comparing equilibrium outcome in the scenarios with and without the recommender system.

Proposition 7 Compared to the scenario without the recommender system, in the presence of the recommender system:

(a) product price is lower if and only if

$$
k > \frac {\beta (\beta + 1) [ (1 - \beta) t + 2 \sqrt {2 t \tau} ]}{8 \tau - (1 - \beta) ^ {2} t}
$$

(b) sellers’ advertising intensity is lower;

(c) sellers are better off (i.e., $\hat { \pi } _ { i } ^ { * } > \pi _ { i } ^ { * } )$ ) if and only if

$$
\frac {\beta (1 - \beta) t}{8 (k - \beta)} + \frac {(\beta k + 3 k - 4 \beta) \left[ k \tau - \sqrt {k ^ {2} \tau^ {2} - (1 - \beta) (k - \beta) \beta t \tau} \right]}{4 (1 - \beta) (k - \beta) ^ {2}} > \frac {2 t \tau}{(\sqrt {2 \tau} + \sqrt {t}) ^ {2}}
$$

We find that the impacts of the recommender system on advertising intensity and seller profits under the general model are qualitatively identical to those in the baseline model. The impact on price is also qualitatively the same under the baseline model and the extended model when the relative weight on price is not too low. However, when the relative weight of price is very low, as given by the condition in Proposition 7(a), recommender system may actually increase the product prices. The primary explanation for this finding is that when price plays a minor role in the choice of recommendations, sellers do not have much incentive to use prices (i.e., reduce prices) to generate more recommendations in their favor.

Similarly, the impacts of the recommendation precision are not qualitatively different under baseline and extended models. In addition, we show the following result that provides insights into the role played by the relative weight of price in the recommendation strategy in recommender system impact.

Proposition 8 In the presence of the recommender system, $\hat { p } _ { i } ^ { * } , \hat { \phi } _ { i } ^ { * }$ , and $\hat { \pi } _ { i } ^ { * }$ decrease in k.

The proposition reveals that as the weight of price decreases (or, equivalently, as the importance of product fit increases) in the recommendation strategy, the competition effect is mitigated, advertising effect is enhanced, and the positive (negative) impact on seller profits is enhanced (mitigated). The results of this more general model that allows for different relative weight for product price in determining the recommendation show that the region in the parameter space in which the recommender system benefits sellers expands when the recommender system places more emphasis on the product fit relative to price.

## Discussion and Conclusions

We show in this paper that the impacts of the recommender system on competing sellers in an electronic marketplace are the result of a subtle interaction between advertising effect and competition effect. The advertising effect causes firms to advertise less and the competition effect causes firms to decrease prices in the presence of a recommender system. The recommender system alters the seller’s own strategies related to advertising intensity and price from being strategic substitutes in the absence of the recommender system to being strategic complements in the presence of the recommender system, as a result of these two effects. Although the advertising provided by the recommender system is free, sellers may be better off or worse off in the presence of the recommender system than in the absence—sellers are more likely to benefit from recommender system only when it has a high precision. The results do not change qualitatively whether sellers use targeted advertising or uniform advertising. However, when sellers are able to target consumers with a high degree of precision, even a high recommender system precision may not benefit sellers.

Our results have implications for electronic marketplaces and offer a few testable hypotheses. The implications fall under two categories. The first set of implications relates to whether sellers and consumers benefit when electronic marketplaces deploy recommender systems as compared to when marketplaces do not deploy these systems. Clearly, the overall awareness of consumers about products, and thus overall demand (in terms of sales units) is higher in the marketplace with recommender systems. However, whether the sellers’ revenue and profit are higher in marketplaces with recommender systems compared to those without recommender systems is unclear. While existing empirical research tout the increased sales contributed by recommender systems, these studies use unit sales or its proxies. Our results suggest that empirical studies that examine the seller revenue or profit will provide a more complete understanding of the recommender systems’ impact. Another direct implication is that the overall advertisement levels from sellers in electronic marketplaces with recommender systems are likely be lower than in marketplaces without recommender systems. The lower demand for traditional advertising may lead to a decrease in the price of traditional advertising, contributing to a further decline in revenue for traditional advertisers. A worthwhile empirical study is to examine the trend of total revenue of the advertising industry and isolate the role played by marketplaces with recommender systems in this revenue.

The second set of implications relates to the scenario in which recommender systems are inevitable. Regardless of whether recommender systems benefit or hurt the sellers and the marketplace, if recommender systems are indeed here to stay, an improvement in precision benefits sellers and the marketplace. This result provides partial support to marketplaces continuing efforts to improve the accuracy of recommender system in predicting consumer preference. On the other hand, the findings also suggest that while consumers can expect better recommendations from the marketplaces, consumers may end up paying more than the value of such recommendations in the form of increased prices. Sellers need to carefully choose the advertising approach; when the seller cannot accurately target consumers (targeting precision is relatively low), it is better to adopt uniform advertising.

This study can be extended in several directions. First, a valuable extension of this research is to empirically examine the theoretical predictions resulting from the model and analysis. For instance, the analysis shows a positive relationship between recommender system precision and sellers’ profits and a non-monotonic relationship between sellers’ targeting precision and their profits. Such predictions can be validated through empirical data or field experiments if possible. Second, we investigate the impact of recommender systems under the platform business model where sellers pay commissions to the platform. Future studies may investigate the impact of recommender systems under wholesale business models, where the platform purchases products from upstream sellers and set the product prices. Third, we examine the impact of recommender systems which recommend competing products. Recommender systems which recommend complementary products are also widely used in the practice (e.g., the “Frequently bought together” feature in Amazon). Future studies may investigate the impacts of those recommender systems. Finally, both advertising and recommender systems have similar roles in informing consumers about products, possibly by targeting specific consumers using information about them. However, such targeting strategies could be costly; for instance, developing and maintaining the recommender systems is not free. Therefore, a natural question is whether it is profitable for the sellers to engage in targeting through advertising or the retailer to engage in targeting through recommender systems. An examination of this question requires a richer model than the one we employ in this paper, and future research can look into this question.

## Acknowledgments

We thank the detailed and constructive comments from the review team, which have greatly improved the paper. We also thank participants at the Workshop on Information Systems and Economics (2015), as well as seminar participants at Dalian University of Technology and The University of Texas at Dallas for their helpful feedback. Jianqing Chen acknowledges the financial support from the NSFC [Grants No.71528004 and 71431002].

## References

Adomavicius, G., and Tuzhilin, A. 2005. “Toward the Next Generation of Recommender Systems: A Survey of the State-ofthe-art and Possible Extensions,” IEEE Transactions on Knowledge and Data Engineering (17:6), pp. 734-749.

Bergemann, D., and Ozmen, D. 2006. “Optimal Pricing with Recommender Systems,” in Proceedings of the 7<sup>th</sup> ACM Conference on Electronic Commerce, New York: ACM, pp. 43-51.

Bester, H., and Petrakis, E. 1995. “Price Competition and Advertising in Oligopoly,” European Economic Review (39:6), pp. 1075-1088.

Bodapati, A. V. 2008. “Recommendation Systems with Purchase Data,” Journal of Marketing Research (45:1), pp. 77-93.

Chen, L-S., Hsu, F-H., Chen, M-C., and Hsu, Y-C. 2008. “Developing Recommender Systems with the Consideration of Product Profitability for Sellers,” Information Sciences (178:4), pp. 1032-1048.

Choudhary, V., and Zhang, Z. J. 2019. “Product Recommender and and Consumer Search,” Working Paper (available at http://dx.doi.org/10.2139/ssrn.3398994).

Fleder, D., and Hosanagar, K. 2009. “Blockbuster Culture’s Next Rise or Fall: The Impact of Recommender Systems on Sales Diversity,” Management Science (55:5), pp. 697-712.

Gal-Or, E., and Gal-Or, M. 2005. “Customized Advertising Via a Common Media Distributor,” Marketing Science (24:2), pp. 241-253.

Gal-Or, E., Gal-Or, M., May, J. H., and Spangler, W. E. 2006. “Targeted Advertising Strategies on Television,” Management Science (52:5), pp. 713-725.

Ghoshal, A., Kumar, S., and Mookerjee, V. 2015. “Impact of Recommender System on Competition between Personalizing and Non-personalizing Firms,” Journal of Management Information Systems (31:4), pp. 243-277.

Grossman, G. M., and Shapiro, C. 1984. “Informative Advertising with Differentiated Products,” The Review of Economic Studies (51:1), pp. 63-81.

Hennig-Thurau, T., Marchand, A., and Marx, P. 2012. “Can Automated Group Recommender Systems Help Consumers Make Better Choices?,” Journal of Marketing (76:5), pp. 89-109.

Hervas-Drane, A. 2015. “Recommended for You: The Effect of Word of Mouth on Sales Concentration,” International Journal of Research in Marketing (32:2), pp. 207-218.

Hosanagar, K., Fleder, D., Lee, D., and Buja, A. 2013. “Will the Global Village Fracture into Tribes? Recommender Systems and Their Effects on Consumer Fragmentation,” Management Science (60:4), pp. 805-823.

Iyer, G., Soberman, D., and Villas-Boas, J. M. 2005. “The Targeting of Advertising,” Marketing Science (24:3), pp. 461-476.

Jabr, W., and Zheng, E. 2014. “Know Yourself and Know Your Enemy: An Analysis of Firm Recommendations and Consumer Reviews in a Competitive Environment,” MIS Quarterly (38:3), pp. 635-654.

Johnson, J. P., and Myatt, D. P. 2006. “On the Simple Economics of Advertising, Marketing, and Product Design,” The American Economic Review (96:3), pp. 756-784.

Kwark, Y., Chen, J., and Raghunathan, S. 2014. “Online Product Reviews: Implications for Retailers and Competing Manufacturers,” Information Systems Research (25:1), pp. 93-110.

Oestreicher-Singer, G., and Sundararajan, A. 2012a. “Recommendation Networks and the Long Tail of Electronic Commerce,” MIS Quarterly (36:1), pp. 65-83.

Oestreicher-Singer, G., and Sundararajan, A. 2012b . “The Visible Hand? Demand Effects of Recommendation Networks in Electronic Markets,” Management Science (58:11), pp. 1963-1981.

Pathak, B., Garfinkel, R., Gopal, R. D., Venkatesan, R., and Yin, F. 2010. “Empirical Analysis of the Impact of Recommender Systems on Sales,” Journal of Management Information Systems (27:2), pp. 159-188.

Resnick, P., and Varian, H. R. 1997. “Recommender Systems,” Communications of the ACM (40:3), pp. 56-58.

Shani, G., and Gunawardana, A. 2011. “Evaluating Recommendation Systems,” in Recommender Systems Handbook, F. Ricci, L. Rokach, B. Shapira, and P. Kantor (eds.), Boston: Springer, pp. 257-297.

Soberman, D. 2004. “Research Note: Additional Learning and Implications on the Role of Informative Advertising,” Management Science (50:12), pp. 1744-1750.

Tam, K. Y., and Ho, S. Y. 2006. “Understanding the Impact of Web Personalization on User Information Processing and Decision Outcomes, MIS Quarterly (30:4), pp. 865-890.

Tirole, J. 1988. The Theory of Industrial Organization, Cambridge, MA: MIT Press.

Vives, X. 1984. “Duopoly Information Equilibrium: Cournot and Bertrand,” Journal of Economic Theory (34:1), pp. 71-94.

Wang, J., and Zhang, Y. 2011. “Utilizing Marginal Net Utility for Recommendation in E-Commerce,” in Proceedings of the 34<sup>th</sup> International ACM SIGIR Conference on Research and Development in Information Retrieval, New York: ACM, pp. 1003-1012.

Zhang, X., Ferreira, P., Godinho de Matos, M., and Belo, R. 2021. “Welfare Properties of Profit Maximizing Recommender Systems: Theory and Results from a Randomized Experiment,” MIS Quarterly (45:1), forthcoming.

## About the Authors

Lusi Li is an assistant professor of information systems at California State University, Los Angeles. She received her Ph.D. in Management Science from Naveen Jindal School of Management at The University of Texas at Dallas and her master’s and bachelor’s degrees in Management Information Systems from Harbin Institute of Technology. Her research interests include economics of information systems, use of online recommender systems and crowdfunding.

Jianqing Chen is a professor in information systems at the Naveen Jindal School of Management, The University of Texas at Dallas. He received his Ph.D. from the McCombs School of Business at The University of Texas at Austin in 2008. His general research interests are in business models and strategies of online platforms, social media and user-generated content, search engine advertising, and economics of information systems. His papers have been published in academic journals, including Information Systems Research, MIS Quarterly, Management Science, Journal of Marketing Research, Journal of Marketing, Production and Operations Management, Journal of Management Information Systems, Economics Letters, Decision Analysis, and Decision Support Systems. He received the ISS Sandra A. Slaughter Early Career Award of INFORMs in 2016. He was the co-recipient of the Best Paper award for the fifteenth Conference on Information Systems and Technology in 2010 and of the Best Paper award for the first, sixth, and ninth China Summer Workshop on Information Management in 2007, 2012, and 2015. He is currently an associate editor for Information Systems Research and a senior editor of Production and Operations Management.

Srinivasan Raghunathan is a Professor of Information Systems in Naveen Jindal School of Management, The University of Texas at Dallas. His current research interests are in the economics of information security and economic impact of e-commerce technologies such as review platforms and recommendation systems. His papers have been published in journals such as Management Science, Operations Research, Information Systems Research, Decision Analysis, Journal of MIS, Decision Support Systems, various IEEE transactions, IIE transactions, European Journal of Operational Research, and Production and Operations Management. He has served on the editorial boards of Information Systems Research, Information Technology and Management, and Journal of Electronic Commerce Research.

## Appendix A

Proofs

## Proof of Conditional Expectation of Misfit

Proof. The cumulative density function of <sub>??,</sub> conditional on the consumer’s true location <sub>??</sub> being <sub>??</sub>, can be formulated as:

$$
P (s \leq y | z = \lambda) = (1 - \beta) y + \beta H (y - \lambda)\tag{39}
$$

where $H ( )$ is the Heaviside step function that evaluates to zero if the argument is negative, and to one otherwise. The corresponding probability density function is:

$$
P (s = y | z = \lambda) = (1 - \beta) + \beta \delta (y - \lambda)\tag{40}
$$

where $\delta ( x )$ is the Dirac delta distribution that satisfies $\begin{array} { r } { \int _ { - \infty } ^ { \infty } \delta ( x ) d x = 1 \mathrm { a n d } \delta ( x ) = 0 \mathrm { i f } x \neq 0 , \delta ( x ) = \infty \mathrm { i f } x = 0 } \end{array}$

Using the Bayes Law,

$$
P (z = \lambda | s = y) = \frac {P (s = y | z = \lambda) P (z = \lambda)}{P (s = y)} = (1 - \beta) + \beta \delta (y - \lambda)\tag{41}
$$

and the conditional expectation is:

$$
\mathbb {E} (z | s = y) = \frac {1 - \beta}{2} + \beta y\tag{42}
$$

## Proof of Lemma 1

Proof. (a) and (b) Firm’s optimization problem in stage 1 is characterized by the first-order conditions of Equation (3):

$$
\frac {\partial \pi_ {A}}{\partial p _ {A}} = (1 - \alpha) \phi_ {A} (1 - \phi_ {B} + \phi_ {B} \frac {p _ {B} - 2 p _ {A} + t}{2 t}) = 0\tag{43}
$$

$$
\frac {\partial \pi_ {A}}{\partial \phi_ {A}} = (1 - \alpha) p _ {A} (1 - \phi_ {B} + \phi_ {B} \frac {p _ {B} - p _ {A} + t}{2 t}) - a \phi_ {\mathrm{A}} = 0\tag{44}
$$

$$
\frac {\partial \pi_ {B}}{\partial p _ {B}} = (1 - \alpha) \phi_ {B} (1 - \phi_ {A} + \phi_ {A} \frac {p _ {A} - 2 p _ {B} + t}{2 t}) = 0\tag{45}
$$

$$
\frac {\partial \pi_ {B}}{\partial \phi_ {B}} = (1 - \alpha) p _ {B} (1 - \phi_ {A} + \phi_ {A} \frac {p _ {A} - p _ {B} + t}{2 t}) - a \phi_ {B} = 0\tag{46}
$$

Solving Equations (43) and (45) , we can derive $p _ { A }$ and $p _ { B }$ as functions of $\phi _ { A }$ and $\phi _ { B }$ as follows:

$$
p _ {A} = \frac {t}{3} (\frac {2}{\phi_ {A}} + \frac {4}{\phi_ {B}} - 3)\tag{47}
$$

$$
p _ {B} = \frac {t}{3} (\frac {4}{\phi_ {A}} + \frac {2}{\phi_ {B}} - 3)\tag{48}
$$

By substituting $p _ { A }$ and $p _ { B }$ in above equations into Equations (44) and (46) , we have

$$
- 1 8 a \phi_ {A} + \frac {(1 - \alpha) (4 - 3 \phi_ {B}) ^ {2} t}{\phi_ {B}} + \frac {4 (1 - \alpha) \phi_ {B} t}{\phi_ {A} ^ {2}} = \frac {4 (1 - \alpha) (3 \phi_ {B} - 4) t}{\phi_ {A}}\tag{49}
$$

$$
- 1 8 a \phi_ {B} + \frac {(1 - \alpha) t (4 - 3 \phi_ {A}) ^ {2}}{\phi_ {A}} + \frac {4 (1 - \alpha) \phi_ {A} t}{\phi_ {B} ^ {2}} = \frac {4 (1 - \alpha) (3 \phi_ {A} - 4) t}{\phi_ {B}}\tag{50}
$$

In the symmetric equilibrium, $\phi _ { A } = \phi _ { B }$ . Solving the three equations together, we derive the advertising intensity in the equilibrium as $\phi _ { A } ^ { * } =$ $\begin{array} { r } { \phi _ { B } ^ { * } = \frac { 2 t } { \sqrt { 2 a t / ( 1 - \alpha ) } + t } } \end{array}$ . Substituting $\phi _ { A } ^ { * }$ and $\phi _ { B } ^ { * }$ into Equations (47) and (48), we derive the prices in the equilibrium as $p _ { A } ^ { * } = p _ { B } ^ { * } =$ $\sqrt { 2 a t / ( 1 - \alpha ) }$ . By replacing $\tau = a / ( 1 - \alpha )$ , we get the equilibrium prices and advertising intensities in Equation (4) and Equation (5). Under the assumption $\begin{array} { r } { \frac { t } { 2 } < \tau < \frac { ( v - t ) ^ { 2 } } { 2 t } , } \end{array}$ we can verify that the equilibrium advertising level $\phi _ { i } ^ { * } \in [ 0 , 1 ]$ and equilibrium price $p _ { i } ^ { * } \in [ 0 , \boldsymbol { v } - \boldsymbol { t } ]$

(c) Substituting the equilibrium prices and advertising intensities into Equation (3), we can derive the equilibrium profits as in Equation (6). Next, we show there are no profitable deviations from the equilibrium under the assumption. One possible deviation is that one firm (for example, firm <sub>??</sub>) increases price to $v - t ;$ that is, firm <sub>??</sub> only serves partially informed consumers. In this case, the demand function becomes $D _ { A } = \phi _ { A } ( 1 - \phi ^ { * } )$ and the profit function becomes $\pi _ { A } = \phi _ { A } ( 1 - \phi ^ { * } ) p _ { A } ( 1 - \alpha ) - a \phi _ { A } ^ { 2 } / 2$ . The best response of <sub>??</sub> is $p _ { A } ^ { d e v } = v - t$ and $\begin{array} { r } { \phi _ { A } ^ { d e v } = \frac { ( \sqrt { 2 t \tau } - t ) ( v - t ) } { \tau \left( \sqrt { 2 t \tau } + t \right) } } \end{array}$ , and the optimal deviation profit is $\begin{array} { r } { \pi _ { A } ^ { d e v } = \frac { ( 1 - \alpha ) ( \sqrt { 2 t \tau } - t ) ^ { 2 } ( v - t ) ^ { 2 } } { 2 \tau ( \sqrt { 2 t \tau } + t ) ^ { 2 } } . \ \mathrm { I f } \ \pi _ { A } ^ { d e v } < \pi _ { A } ^ { * } , } \end{array}$ , firm would not deviate from the equilibrium. When $v < 5 t , \pi _ { A } ^ { d e v }$ is always less than $\pi _ { A } ^ { * }$ , and there is no profitable deviation. When $v > 5 t$ , from $\pi _ { A } ^ { d e v } < \pi _ { A } ^ { * }$ , we derive $\begin{array} { r } { \frac { 3 t ^ { 2 } - 4 t v + \sqrt { ( v - 5 t ) ( v - t ) ^ { 3 } } + v ^ { 2 } } { \ A t } < \tau } \end{array}$ . Under this condition, firms have no incentive to deviate from a pure price strategy to the reservation price for partially informed consumers. We can verify other possible deviations always lead to lower profits

(d) The consumer surplus from consumers who only receive advertising from one seller is:

$$
C S _ {p} = 2 \phi^ {*} (1 - \phi^ {*}) \int_ {0} ^ {1} (v - p ^ {*} - z t) \mathrm{d} z = 2 \phi^ {*} (1 - \phi^ {*}) (v - p ^ {*} - \frac {t}{2})
$$

The consumer surplus from consumers who receive advertising from both sellers is:

$$
C S _ {f} = (\phi^ {*}) ^ {2} [ \int_ {0} ^ {\frac {1}{2}} (v - p ^ {*} - z t) \mathrm{d} z + \int_ {\frac {1}{2}} ^ {1} (v - p ^ {*} - (1 - z) t) \mathrm{d} z ] = (\phi^ {*}) ^ {2} (v - p ^ {*} - \frac {t}{4})
$$

Aggregating consumers surplus from these two segments, we get

$$
C S = C S _ {p} + C S _ {f} = \phi^ {*} (2 - \phi^ {*}) (v - p ^ {*} - \frac {t}{4}) - \phi^ {*} (1 - \phi^ {*}) \frac {t}{2}\tag{51}
$$

Substituting $p ^ { * }$ and $\phi ^ { * }$ with the equilibrium as showed in Equation (4) and Equation (5) and aggregating the consumer surplus above, we can derive the total surplus as in Equation (7).

## Proof of Lemma 2

Proof. (a) and (b) Firm’s optimization problem in stage 1 is characterized by the first-order conditions of Equation (3) with $D _ { A }$ and $D _ { B }$ specified in Equation (12) and Equation (13):

$$
\begin{array}{r l} & {\frac {\partial \pi_ {A}}{\partial p _ {A}} = \frac {(1 - \alpha) (1 - \beta) (p _ {B} - p _ {A}) (p _ {B} - 3 p _ {A}) (\phi_ {B} - \phi_ {A})}{4 \beta t ^ {2}} + \frac {(1 - \alpha) (p _ {B} - 2 p _ {A}) [ 2 - (1 - \beta^ {2}) \phi_ {B} - (1 - \beta) ^ {2} \phi_ {A} ]}{4 \beta t} + \frac {(1 - \alpha) [ (1 - \beta) (\phi_ {A} - \phi_ {B}) + 2 ]}{4} = 0} \\ & {\frac {\partial \pi_ {B}}{\partial p _ {B}} = \frac {(1 - \alpha) (1 - \beta) (p _ {A} - p _ {B}) (p _ {A} - 3 p _ {B}) (\phi_ {A} - \phi_ {B})}{4 \beta t ^ {2}} + \frac {(1 - \alpha) (p _ {A} - 2 p _ {B}) [ 2 - (1 - \beta^ {2}) \phi_ {B} - (1 - \beta) ^ {2} \phi_ {A} ]}{4 \beta t} + \frac {(1 - \alpha) [ (1 - \beta) (\phi_ {B} - \phi_ {A}) + 2 ]}{4} = 0} \\ & {\qquad \frac {\partial \pi_ {A}}{\partial \phi_ {A}} = - a \phi_ {A} + p _ {A} \frac {(1 - \alpha) (1 - \beta) (p _ {B} - p _ {A} + t) (p _ {A} - p _ {B} + \beta t)}{4 \beta t ^ {2}} = 0} \\ & {\qquad \frac {\partial \pi_ {B}}{\partial \phi_ {B}} = - a \phi_ {B} + p _ {B} \frac {(1 - \alpha) (1 - \beta) [ (p _ {A} - p _ {B} + t) (p _ {B} - p _ {A} + \beta t) - 2 t \beta (p _ {A} - p _ {B}) ]}{4 \beta t ^ {2}} = 0} \end{array}
$$

Solving the above equations, we derive equilibrium prices as in Equation (14) and advertising intensities as in Equation (15). Under the assumption $\begin{array} { r } { \frac { t } { 2 } < \tau < \frac { ( v - t ) ^ { 2 } } { 2 t } . } \end{array}$ , the equilibrium advertising intensity $\hat { \phi } _ { i } ^ { * } \in [ 0 , 1 ]$ and equilibrium price $\hat { p } _ { i } ^ { * } \in [ 0 , v - t ]$

(c) Substituting the equilibrium prices and advertising intensities into Equation (3), we derive the equilibrium profits as in Equation (16). Next, we show there are no profitable deviations from the equilibrium under Assumption 2. One possible deviation is firm increases price from the equilibrium such that recommender system always recommends <sub>??</sub>. In this case, the demand for product <sub>??</sub> is $\phi _ { \mathrm { A } } ( \hat { p } _ { B } ^ { * } - p _ { A } + t ) / ( 2 t )$

and the profit is $\begin{array} { r } { \frac { \phi _ { \mathrm { A } } ( \hat { p } _ { B } ^ { * } - p _ { A } + t ) } { 2 t } p _ { A } ( 1 - \alpha ) - \frac { a \phi _ { A } ^ { 2 } } { 2 } . } \end{array}$ . The best response of is $p _ { A } ^ { d e v } = ( \hat { p } _ { B } ^ { * } + t ) / 2 \mathrm { ~ a n d } \phi _ { A } ^ { d e v } = ( \hat { p } _ { B } ^ { * } + t ) ^ { 2 } / ( 8 \tau t )$ , and the optimal deviation profit is $\begin{array} { r } { \pi _ { A } ^ { d e v } = \frac { ( 1 - \alpha ) ( \hat { p } _ { B } ^ { * } + t ) ^ { 2 } } { 1 2 8 t ^ { 2 } \tau } . \pi _ { A } ^ { d e v } < \hat { \pi } _ { A } ^ { * } } \end{array}$ requires $X > 0$ , where

$$
X \equiv 1 6 (1 - \beta) ^ {6} t ^ {2} \tau [ \beta (1 - \beta) ^ {2} t + 6 \tau - 6 \sqrt {\tau^ {2} - (1 - \beta) ^ {2} \beta t \tau} ] - ((1 - \beta) ^ {2} t + 2 \tau - 2 \sqrt {\tau (\tau - (1 - \beta) ^ {2} \beta t)}) ^ {4}
$$

Because increases in and $\tau \geq t / 2$ , the minimum value of is

$$
X | _ {\tau = \frac {t}{2}} = 1 6 (1 - \beta) ^ {6} t [ \beta (1 - \beta) ^ {2} - 3 \sqrt {1 - 2 (1 - \beta) ^ {2} \beta} + 3 ] + 2 t [ (2 - \beta) \beta + \sqrt {1 - 2 (1 - \beta) ^ {2} \beta} + 2 ]
$$

which is always positive when $\beta > \frac { 1 } { 2 5 } .$

(d) The consumer surplus from consumers who only receive advertising from one seller is:

$$
\begin{array}{r l} & {\hat {C} S _ {p} = \phi^ {*} (1 - \phi^ {*}) [ 2 \int_ {0} ^ {\frac {1}{2}} (v - p ^ {*} - z t) d z + (1 - \beta) \int_ {\frac {1}{2}} ^ {1} (v - z t - p ^ {*}) d z + (1 + \beta) \int_ {\frac {1}{2}} ^ {1} (v - (1 - z) t) ]} \\ & {\qquad = 2 \phi^ {*} (1 - \phi^ {*}) [ v - p ^ {*} - \frac {t}{4} - \frac {(1 - \beta) t}{8} ]} \end{array}
$$

The consumer surplus from consumers who receive advertising from both sellers is:

$$
\hat {C} S _ {f} = (\phi^ {*}) ^ {2} [ \int_ {0} ^ {\frac {1}{2}} (v - p ^ {*} - z t) \mathrm{d} z + \int_ {\frac {1}{2}} ^ {1} (v - p ^ {*} - (1 - z) t) \mathrm{d} z ] = (\phi^ {*}) ^ {2} (v - p ^ {*} - \frac {t}{4})
$$

Consumer surplus from consumers who do not receive any advertising is:

$$
\hat {C} S _ {u} = 2 (1 - \phi^ {*}) ^ {2} [ \frac {1 + \beta}{2} \int_ {0} ^ {1} (v - p ^ {*} - z t) \mathrm{d} z - \beta \int_ {\frac {1}{2}} ^ {1} (v - p ^ {*} - z t) \mathrm{d} z ] = (1 - \phi^ {*}) ^ {2} [ v - p ^ {*} - \frac {(2 - \beta) t}{4} ]
$$

Aggregating the consumer surplus above, the total surplus is:

$$
\hat {C} S = \hat {C} S _ {p} + \hat {C} S _ {f} + \hat {C} S _ {u} = v - p ^ {*} - \frac {t}{4} - (1 - \phi^ {*}) \frac {1 - \beta}{4} t\tag{52}
$$

Substituting $p ^ { * }$ and $\phi ^ { * }$ with the equilibrium as showed in Equation (14) and Equation (15) and aggregating the consumer surplus above, we derive the total surplus as in Equation (17).

## Proof of Proposition 1

Proof. (a) Because $\hat { p } _ { i } ^ { * }$ increases in $\beta$ according to Proposition $2 ( \mathbf { a } ) .$ , its maximum value is $\hat { p } _ { i } ^ { * } | _ { \beta = 1 } = t$ , which is less than $p _ { i } ^ { * } = \sqrt { 2 \tau t }$ Therefore, $\hat { p } _ { i } ^ { * } \leq p _ { i } ^ { * }$

(b) Note that

$$
\hat {\phi} _ {i} ^ {*} - \phi_ {i} ^ {*} = \frac {1}{2 (1 - \beta)} - \frac {\sqrt {\tau^ {2} - \beta (1 - \beta) ^ {2} t \tau}}{2 \tau (1 - \beta)} - \frac {2 t}{\sqrt {2 \tau t} + t}\tag{53}
$$

$\hat { \phi } _ { i } ^ { * } - \phi _ { i } ^ { * } < 0$ requires $\begin{array} { r } { \frac { 1 } { 2 ( 1 - \beta ) } - \frac { \sqrt { \tau ^ { 2 } - \beta ( 1 - \beta ) ^ { 2 } t \tau } } { 2 \tau ( 1 - \beta ) } - \frac { 2 t } { \sqrt { 2 \tau t } + t } < 0 , } \end{array}$ , which is equivalent to $1 6 t \tau ( 1 - \beta ) - 8 \tau ( \sqrt { 2 \tau t } + t ) < ( \sqrt { 2 \tau t } + t ) ^ { 2 } \beta ( 1 - \beta )$ Because $\tau \geq \mathrm { t } / 2 ,$ <sub>,</sub> we have <sub>8</sub> $\tau ( \sqrt { 2 \tau t } + t ) > 1 6 \tau t > 1 6 t \tau ( 1 - \beta )$ . Therefore, $\cdot ( 1 - \beta ) - 8 \tau ( \sqrt { 2 \tau t } + t ) < 0 < ( \sqrt { 2 \tau t } + t ) ^ { 2 } \beta ( 1 - \beta )$ and we get $\hat { \phi } _ { i } ^ { * } < \phi _ { i } ^ { * }$

(c) From Equation (6) and Equation $( 1 6 ) , \hat { \pi } _ { i } ^ { * } > \pi _ { i } ^ { * }$ requires:

$$
\frac {\beta t}{8} + \frac {3 [ \tau - \sqrt {\tau^ {2} - \beta \tau t (1 - \beta) ^ {2}} ]}{4 (1 - \beta) ^ {2}} > \frac {2 t \tau}{(\sqrt {2 \tau} + \sqrt {t}) ^ {2}}\tag{54}
$$

(d) From Equation (52) and Equation (51) we ge<sub>t</sub>

$$
\begin{array}{r l} & {\hat {C S} - C S = v - \hat {p} _ {i} ^ {*} - \frac {t}{4} - (1 - \hat {\phi} _ {i} ^ {*}) \frac {1 - \beta}{4} t - (\phi_ {i} ^ {*} (2 - \phi_ {i} ^ {*}) (v - p _ {i} ^ {*} - \frac {t}{4}) - \phi_ {i} ^ {*} (1 - \phi_ {i} ^ {*}) \frac {t}{2})} \\ & {\qquad = (1 - \phi_ {i} ^ {*}) ^ {2} (v - \hat {p} _ {i} ^ {*} - \frac {t}{4}) + \phi_ {i} ^ {*} (1 - \phi_ {i} ^ {*}) \frac {t}{2} + \phi_ {i} ^ {*} (2 - \phi_ {i} ^ {*}) (p _ {i} ^ {*} - \hat {p} _ {i} ^ {*}) - (1 - \hat {\phi} _ {i} ^ {*}) \frac {1 - \beta}{4} t} \end{array}
$$

The first term, $( 1 - \phi _ { i } ^ { * } ) ^ { 2 } ( v - \hat { p } _ { i } ^ { * } - t / 4 )$ , is positive. The second term, $\phi _ { i } ^ { * } ( 1 - \phi _ { i } ^ { * } ) t / 2$ , is positive. Because $\phi _ { i } ^ { * } ( 2 - \phi _ { i } ^ { * } ) ( p _ { i } ^ { * } - \hat { p } _ { i } ^ { * } ) - ( 1 -$ $\hat { \phi } _ { i } ^ { * } ) ( 1 - \beta ) t / 4 > \phi _ { i } ^ { * } ( p _ { i } ^ { * } - \hat { p } _ { i } ^ { * } ) - ( 1 - \beta ) t / 4 _ { : }$ , as long as $\phi _ { i } ^ { * } ( p _ { i } ^ { * } - \hat { p } _ { i } ^ { * } ) > ( 1 - \beta ) t / 4$ , we can get $\hat { C } S > C S$ . By substituting $p _ { i } ^ { * }$ in Equation (4) and $\hat { p } _ { i } ^ { * }$ in Equation (14) into inequality $\phi _ { i } ^ { * } ( p _ { i } ^ { * } - \hat { p } _ { i } ^ { * } ) > ( 1 - \beta ) t / 4 .$ , we have

$$
\frac {2 t}{\sqrt {2 \tau t} + t} (\sqrt {2 \tau t} - \frac {2 [ \tau - \sqrt {\tau^ {2} - \beta (1 - \beta) ^ {2} t \tau} ]}{(1 - \beta) ^ {2}}) > \frac {1 - \beta}{4} t
$$

Simplifying the above inequality, we get

$$
\mathrm{Y} \equiv 8 (1 - \beta) ^ {2} \sqrt {2 \pi t} - 1 6 (\tau - \sqrt {\tau^ {2} - \beta (1 - \beta) ^ {2} t \tau}) - (1 - \beta) ^ {3} (\sqrt {2 \pi t} + t) > 0
$$

We can verify that $\partial Y / \partial \beta < 0$ , and thus the minimum value of <sub>??</sub> is $Y | _ { \beta = 1 } = 0$ . Therefore, $Y \geq 0$ and $\hat { C } S > C S$

## Proof of Proposition 2

Proof. (a) Note that

$$
\frac {\partial \hat {p} _ {i} ^ {*}}{\partial \beta} = \frac {\tau [ 4 \sqrt {\tau^ {2} - (1 - \beta) ^ {2} \beta t \tau} + (1 + \beta) (1 - \beta) ^ {2} t - 4 \tau ]}{(1 - \beta) ^ {3} \sqrt {\tau^ {2} - (1 - \beta) ^ {2} \beta t \tau}}
$$

$\partial \hat { p } _ { i } ^ { * } / \partial \beta > 0$ requires $4 \sqrt { \tau ^ { 2 } - ( 1 - \beta ) ^ { 2 } \beta t \tau } > 4 \tau - ( 1 + \beta ) ( 1 - \beta ) ^ { 2 } t$ , which is equivalent to condition $\tau > ( 1 + \beta ) ^ { 2 } ( 1 - \beta ) t / 8$ . This condition always holds because $\tau > t / 2 > ( 1 + \beta ) ^ { 2 } ( 1 - \beta ) t / 8 .$

(b) Note that

$$
\frac {\partial \widehat {\phi} _ {i} ^ {*}}{\partial \beta} = \frac {2 \sqrt {\tau^ {2} - \beta (1 - \beta) ^ {2} t \tau} + (1 - \beta) ^ {3} t - 2 \tau}{4 (1 - \beta) ^ {2} \sqrt {\tau^ {2} - \beta (1 - \beta) ^ {2} t \tau}}
$$

$\partial \hat { \phi } _ { i } ^ { * } / \partial \beta > 0$ requires $2 \sqrt { \tau ^ { 2 } - ( 1 - \beta ) ^ { 2 } \beta t \tau } + ( 1 - \beta ) ^ { 3 } t - 2 \tau > 0$ , which leads to the condition $4 \tau ( 1 - 2 \beta ) > ( 1 - \beta ) ^ { 4 } t$

(c) Note that

$$
\frac {\partial \widehat {\pi} _ {i} ^ {*}}{\partial \beta} = (1 - \alpha) \frac {((1 - \beta) ^ {3} t + 1 2 \tau) \sqrt {\tau^ {2} - \beta (1 - \beta) ^ {2} t \tau} + 3 (1 + \beta) (1 - \beta) ^ {2} t \tau - 1 2 \tau^ {2}}{8 (1 - \beta) ^ {3} \sqrt {\tau^ {2} - \beta (1 - \beta) ^ {2} t \tau}}
$$

In part (a), we showed that $4 \sqrt { \tau ^ { 2 } - ( 1 - \beta ) ^ { 2 } \beta t \tau } > 4 \tau - ( 1 + \beta ) ( 1 - \beta ) ^ { 2 } t$ . Therefore, $1 2 \tau \sqrt { \tau ^ { 2 } - \beta ( 1 - \beta ) ^ { 2 } t \tau } + 3 ( 1 + \beta ) ( 1 - \beta ) ^ { 2 } t \tau -$ $1 2 \tau ^ { 2 } > 0$ , and we get $\partial \hat { \pi } _ { i } ^ { * } / \partial \beta > 0$

(d) Note that $\begin{array} { r } { \frac { \partial \hat { C } S } { \partial \beta } = - \frac { \mathrm { Z } } { 1 6 ( 1 - \beta ) ^ { 3 } \sqrt { \tau ^ { 2 } - \beta ( 1 - \beta ) ^ { 2 } t \tau } } , } \end{array}$ where

$$
Z \equiv (- 4 (1 - \beta) ^ {3} t + 6 4 \tau) \sqrt {\tau^ {2} - \beta (1 - \beta) ^ {2} t \tau} + 1 6 (1 + \beta) (1 - \beta) ^ {2} t \tau - 6 4 \tau^ {2} - (1 - 3 \beta) (1 - \beta) ^ {4} t ^ {2}
$$

$\partial \hat { C } S / \partial \beta < 0$ requires $Z \equiv ( - 4 ( 1 - \beta ) ^ { 3 } t + 6 4 \tau ) \sqrt { \tau ^ { 2 } - \beta ( 1 - \beta ) ^ { 2 } t \tau } + 1 6 ( 1 + \beta ) ( 1 - \beta ) ^ { 2 } t \tau - 6 4 \tau ^ { 2 } - ( 1 - 3 \beta ) ( 1 - \beta ) ^ { 4 } t ^ { 2 } > 0$ . We verify that $\partial Z / \partial \beta < 0$ , and the minimum value of <sub>??</sub> is $Z | _ { \beta = 1 } = 0$ . Therefore, $Z > 0$ <sup>and</sup> ∂??<sup>̂</sup>??/ ∂?? < 0<sup>.</sup>

## Proof of Lemma 3

Proof. (a) and (b): Firm <sub>??</sub>’s optimal advertising strategy is as in Equation (21) and optimal price is characterized by the first-order condition of Equation (22). In a symmetric equilibrium, firms use the same price and advertising intensity; that is, $p _ { A } = p _ { B } = p ^ { * } , \phi _ { A } ^ { H } = \phi _ { B } ^ { H } = \phi ^ { H * }$ and $\phi _ { A } ^ { L } = \phi _ { B } ^ { L } = \phi ^ { L * }$ . By substituting the prices and advertising intensities into Equation (21) and the first-order conditions of Equation (22), we have

$$
\phi^ {H *} = \frac {p ^ {*}}{4 t ^ {2} \tau} [ 4 t ^ {2} - (1 - \gamma) t ^ {2} ((\phi^ {L *} - \phi^ {H *}) (1 - \gamma) + 2 \phi^ {H *}) ]
$$

$$
\phi^ {L *} = \frac {p ^ {*}}{4 t ^ {2} \tau} [ 4 t ^ {2} - (1 + \gamma) t ^ {2} ((\phi^ {L *} - \phi^ {H *}) (1 - \gamma) + 2 \phi^ {H *}) ]
$$

$$
\frac {\partial \mathbb {E} (\pi_ {i})}{\partial p _ {i}} = \frac {1 - \alpha}{8 t} [ 2 [ (\phi^ {H *}) ^ {2} - (\phi^ {L *}) ^ {2} ] \tau - [ (\phi^ {H *}) ^ {2} + (\phi^ {L *}) ^ {2} ] [ (1 - \gamma) ^ {2} p ^ {*} + (1 - \gamma^ {2}) t ] - 4 (\phi^ {H *} - \phi^ {L *}) p ^ {*}
$$

$$
+ 4 (\phi^ {H *} + \phi^ {L *}) t - 2 \phi^ {H *} \phi^ {L *} [ 2 \gamma p ^ {*} + p ^ {*} - \gamma^ {2} p ^ {*} + (1 + \gamma^ {2}) t ] ] = 0
$$

Solving the above equations, we derive the equilibrium advertising intensities in Equations (24) and (25), and the equilibrium price in Equation (23). Denote $F \equiv ( p ^ { * } ) ^ { 4 } ( \gamma ^ { 4 } - \gamma ^ { 3 } ) + ( \dot { p } ^ { * } ) ^ { 3 } \tau ( \gamma - 2 \gamma ^ { 2 } ) + ( \bar { p } ^ { * } ) ^ { 2 } \tau ( 2 \tau - \gamma ^ { 4 } t - \dot { \gamma } ^ { 2 } t ) + 4 p ^ { * } t \gamma ^ { 2 } \tau ^ { 2 } - 4 t \tau ^ { 3 }$ . Under the assumption $\tau >$ 2 , $F | _ { p = 0 } < 0$ and $F | _ { p = \tau } > 0$ . Therefore, there is a solution $p ^ { * } \in [ 0 , \tau ] , \phi ^ { H * } \in [ 0 , 1 ]$ <sub>,</sub> and $\phi ^ { L * } \in [ 0 , 1 ]$

(c) Substituting $\phi ^ { H * }$ in Equation (24) and $\phi ^ { L * }$ in Equation (25) into profit function in Equation (22), we get the equilibrium profits in Equation (26).

(d) For a consumer whose true location is between and $1 / 2$ , with probability $\begin{array} { r } { \frac { 1 + \gamma } { 2 } \phi ^ { H * } + \frac { 1 - \gamma } { 2 } \phi ^ { L * } } \end{array}$ , the consumer receives an advertisement from <sub>??</sub> and becomes aware of product <sub>??</sub>. With probability $\begin{array} { r } { \frac { 1 - \gamma } { 2 } \phi ^ { H * } + \frac { 1 + \gamma } { 2 } \phi ^ { L * } } \end{array}$ , the consumer receives an advertisement from <sub>??</sub> and becomes aware of product . Therefore, consumer surplus for consumers whose true locations are between and $1 / 2$ is as follows:

$$
\begin{array}{r l} & C S = \int_ {0} ^ {\frac {1}{2}} (v - p ^ {*} - z t) \frac {(1 + \gamma) \phi^ {H *} + (1 - \gamma) \phi^ {L *}}{2} d z \\ & \qquad + \int_ {0} ^ {\frac {1}{2}} [ v - p ^ {*} - (1 - z) t ] [ \frac {2 - (1 + \gamma) \phi^ {H *} - (1 - \gamma) \phi^ {L *}}{2} ] [ \frac {(1 + \gamma) \phi^ {L *} + (1 - \gamma) \phi^ {H *}}{2} ] d z \end{array}
$$

Because the two firms and consumers are symmetric, the total consumer surplus is <sub>2??</sub> . Substituting $\phi ^ { H * }$ and $\phi ^ { L * }$ with the equilibrium as showed in Equations (24) and (25), we derive the total consumer surplus as in Equation (27).

## Proof of Lemma 4

Proof. In the presence of recommender system, we can show that sellers use similar advertising strategies as in the no recommendation scenario under targeted advertising. Without loss of generality, we assume $p _ { A } \leq p _ { B }$ . We first consider seller $A ^ { * } { \bf s }$ advertising strategy in stage 1 given firm $B ^ { * } { \bf s }$ advertising strategy as in Equation (18). Denoting the true location as and the signal received by recommender system as , we can formulate the demand function and profit function of seller conditional on its own signal $\eta _ { A }$ as follows:

$$
\mathbb {E} [ D _ {A} | \eta_ {A} ] = \int_ {0} ^ {z _ {0}} (\phi_ {A} + (1 - \phi_ {A}) P (s \leq y _ {0} | z)) f (z | \eta_ {A}) \mathrm{d} z + \int_ {z _ {0}} ^ {1} (1 - \mathbb {E} [ \phi_ {B} (\eta_ {B}) | z ]) P (s \leq y _ {0} | z) f (z | \eta_ {A}) \mathrm{d} z
$$

$$
\mathbb {E} [ \pi_ {A} | \eta_ {A} ] = (1 - \alpha) p _ {A} \mathbb {E} [ D _ {A} | \eta_ {A} ] - \frac {a}{2} \phi_ {A} ^ {2}\tag{55}
$$

where $f ( z | \eta _ { A } )$ is the probability density function of location given signal $\eta _ { A } ,$ , and $P ( s \leq y _ { 0 } | z )$ is the probability that the signal <sub>??</sub> received by recommender system is less than $y _ { 0 }$ given the location <sub>??</sub>. Given a signal $\eta _ { A } ,$ , firm <sub>??</sub> maximizes its expected profit by choosing the optimal advertising level. Firm $A ^ { * } { \bf s }$ advertising strategy is summarized as follows:

$$
\phi_ {A} ^ {*} (\eta_ {A}) = \left\{ \begin{array}{l l} \frac {(1 - \beta) p _ {A}}{4 \beta t ^ {2} \tau} (p _ {A} - p _ {B} + \beta t) [ (1 - \gamma) (p _ {B} - p _ {A}) + t (1 + \gamma) ], & \eta_ {A} \leq z _ {0} \\ \frac {(1 - \beta) p _ {A}}{4 \beta t ^ {2} \tau} (1 - \gamma) (p _ {A} - p _ {B} + \beta t) (p _ {B} - p _ {A} + t), & \eta_ {A} > z _ {0} \end{array} \right.\tag{56}
$$

Denoting ’s advertising intensity when $\eta _ { A } \leq z _ { 0 }$ as $\phi _ { A } ^ { H }$ , A’s advertising intensity when $\eta _ { A } > z _ { 0 }$ as $\phi _ { A } ^ { L }$ , we verify that the sellers’ strategies and belief sets are consistent with each other. In stage 1, each seller chooses price by maximizing the overall expected profit:

$$
\max _ {p _ {i}} \mathbb {E} (\pi_ {i}) = \int_ {0} ^ {1} \mathbb {E} (\pi_ {i} | \eta_ {i}) f (\eta_ {i}) \mathrm{d} \eta_ {i}\tag{57}
$$

Firm’s optimization problem in stage 1 is characterized by Equation (56) and the first-order conditions of Equation $( 5 7 ) .$ . In the symmetric equilibrium, firms will set the same price and advertising intensify; that is, $p _ { A } = p _ { B } = \hat { p } ^ { * } , \phi _ { A } ^ { H } = \phi _ { B } ^ { H } = \mathcal { \bar { \phi } } ^ { H * }$ , and $\phi _ { A } ^ { L } = \phi _ { B } ^ { L } = \hat { \phi } ^ { L * }$ . By substituting the price and advertising intensity into Equation (56) and the first-order conditions of Equation (57), we get the following equations:

$$
\hat {\phi} ^ {H *} = \hat {p} ^ {*} \frac {(1 - \beta) (1 + \gamma)}{4 \tau}
$$

$$
\hat {\phi} ^ {L *} = \hat {p} ^ {*} \frac {(1 - \beta) (1 - \gamma)}{4 \tau}
$$

$$
\begin{array}{r} \frac {\partial \mathbb {E} (\pi_ {i})}{\partial p _ {i}} = \frac {(1 - \alpha)}{4 \beta t} [ ((\hat {\phi} ^ {H *}) ^ {2} - (\hat {\phi} ^ {L *}) ^ {2}) \beta \tau + 2 \beta t - 2 \hat {p} ^ {*} + (1 - \beta^ {2}) \hat {p} ^ {*} \gamma (\hat {\phi} ^ {H *} - \hat {\phi} ^ {L *}) \\ + (1 - \beta) \hat {p} ^ {*} (\hat {\phi} ^ {H *} (1 - \beta) + \hat {\phi} ^ {L *} (1 + \beta)) ] = 0 \end{array}\tag{58}
$$

Solving the above equations simultaneously, we get the equilibrium product prices and advertising intensities as in Lemma 4. Under the assumption $2 t \leq \tau$ , it is easy to verify that the equilibrium advertising leve $\hat { \phi } ^ { \hat { H } * } \in [ 0 , 1 ]$ and $\hat { \phi } ^ { H * } \in [ 0 , 1 ]$

(d) Next we derive consumer surplus in the presence of recommender system. For a consumer whose true location is between and $1 / 2 .$ with probability $( 1 + \beta ) / 2$ , recommender system receives a signal $s \leq 1 / 2$ and recommends <sub>??</sub>. Otherwise, recommender system receives a signal $s > 1 / 2$ and recommends . Therefore, consumer surplus for consumers between and 1/2 is as follows:

$$
\begin{array}{r l} & {\hat {C} S = \int_ {0} ^ {\frac {1}{2}} (v - \hat {p} ^ {*} - z t) \left(\frac {(1 + \gamma) \hat {\phi} ^ {H *} + (1 - \gamma) \hat {\phi} ^ {L *}}{2} + \frac {2 - (1 + \gamma) \hat {\phi} ^ {H *} - (1 - \gamma) \hat {\phi} ^ {L *}}{4} (1 + \beta)\right) d z} \\ & {\qquad + \int_ {0} ^ {\frac {1}{2}} (v - \hat {p} ^ {*} - (1 - z) t) (1 - \beta) \frac {2 - (1 + \gamma) \hat {\phi} ^ {H *} - (1 - \gamma) \hat {\phi} ^ {L *}}{4} d z = \frac {v - \hat {p} ^ {*}}{2} - \frac {t (2 - \beta)}{8} + \frac {(1 - \beta) ^ {2} (1 + \gamma^ {2}) t}{3 2 \tau} \hat {p} ^ {*}} \end{array}
$$

Because the two firms and consumers are symmetric, the total consumer surplus is $2 { \hat { C } } S .$ . Substituting $\hat { p } ^ { * }$ with the equilibrium as showed in Equation (28), we derive the total consumer surplus as in Equation (32).

## Proof of Proposition 3

Proof. (a) Because $\hat { p } ^ { * }$ increases with $\beta ,$ , the maximum value of $\hat { p } ^ { * }$ is $\hat { p } ^ { * } | _ { \beta = 1 } = t$ . Next we show that $p ^ { * } > t$ . Because $p ^ { * }$ is the root of Equation (23), $p ^ { * } > t$ is equivalent $\mathrm { t o } \ \frac { ( \gamma ^ { 4 } + \gamma ^ { 2 } ) ( p ^ { * } ) ^ { 2 } - 4 \gamma ^ { 2 } p ^ { * } \tau + 4 \tau ^ { 2 } } { - ( 1 - \gamma ) \gamma ^ { 3 } ( p ^ { * } ) ^ { 2 } + ( 1 - 2 \gamma ) \gamma p ^ { * } \tau + 2 \tau ^ { 2 } } > \frac { p ^ { * } } { \tau }$ . The last inequality is true because $p ^ { * } < \tau$ and $0 < \gamma < 1$ Therefore, we get $p ^ { * } > t > \hat { p } ^ { * }$

(b) $\phi ^ { H * } > \hat { \phi } ^ { H * }$ is equivalent to $\begin{array} { r } { \frac { 2 \tau p ^ { * } + ( 1 - \gamma ) \gamma ( p ^ { * } ) ^ { 2 } } { 2 \tau ^ { 2 } + ( 1 - \gamma ^ { 2 } ) \tau p ^ { * } } > \frac { ( 1 - \beta ) ( 1 + \gamma ) \hat { p } ^ { * } } { 4 \tau } } \end{array}$ . We already showed that $p ^ { * } > \hat { p } ^ { * }$ in part (a). Therefore, $\phi ^ { H * } > \hat { \phi } ^ { H * }$ is true as long as $\begin{array} { r } { \frac { 2 \tau + ( 1 - \gamma ) \gamma p ^ { * } } { 2 \tau + ( 1 - \gamma ^ { 2 } ) p ^ { * } } > \frac { ( 1 + \gamma ) } { 4 } } \end{array}$ . Because $p ^ { * } < \tau$ and $0 < \gamma < 1$ , the last inequality is true. Similarly, $\phi ^ { L * } > \hat { \phi } ^ { L * }$ is equivalent to $\begin{array} { r } { \frac { 2 \tau p ^ { * } - ( 1 - \gamma ) \gamma ( p ^ { * } ) ^ { 2 } } { 2 \tau ^ { 2 } + ( 1 - \gamma ^ { 2 } ) \tau p ^ { * } } > \frac { ( 1 - \beta ) ( 1 - \gamma ) \hat { p } ^ { * } } { 4 \tau } , } \end{array}$ . Because $\tau > p ^ { * } > \hat { p } ^ { * }$ and $0 < \gamma < 1$ , we can verify that this inequality always holds true.

(c) Because $\hat { \pi } ^ { * }$ increases in $\beta ,$ the maximum value of $\hat { \pi } ^ { * } | _ { \beta = 1 } = ( 1 - \alpha ) t / 2 . \mathrm { I f } \pi ^ { * } > ( 1 - \alpha ) t / 2$ , or, equivalently, $( p ^ { * } ) ^ { 2 } [ ( \gamma ^ { 4 } + \gamma ^ { 2 } ) ( p ^ { * } ) ^ { 2 } -$ $4 \gamma ^ { 2 } ( p ^ { * } ) \tau + 4 \tau ^ { 2 } ] > t \tau ( 2 \tau + ( 1 - \gamma ^ { 2 } ) p ^ { * } ) ^ { 2 } , \pi ^ { * }$ is always greater than $\hat { \pi } ^ { * }$ . Otherwise, $\pi ^ { * }$ can be less than $\hat { \pi } ^ { * }$ when $\beta$ is high.

(d) Because $\hat { C } S$ decreases in $\beta ,$ the minimum value is $\hat { C } S | _ { \beta = 1 } = v - 5 t / 4$ . Because $p ^ { * } < \tau$ and $v > 2 t$ , we can verify that

$$
C S = p ^ {*} \frac {4 (v - p ^ {*}) [ (\gamma^ {4} + \gamma^ {2}) (p ^ {*}) ^ {2} - 4 \gamma^ {2} \tau p ^ {*} + 4 \tau^ {2} ] - t [ 3 (\gamma^ {4} + \gamma^ {2}) (p ^ {*}) ^ {2} - 2 p ^ {*} (5 \gamma^ {2} \tau + \tau) + 8 \tau^ {2} ]}{2 \tau (2 \tau + (1 - \gamma^ {2}) p ^ {*}) ^ {2}} <   v - \frac {5 t}{4} <   \hat {C} S
$$

## Proof of Proposition 4

Proof. For ease of exposition, we denote $\begin{array} { r } { M \equiv \sqrt { \tau ^ { 2 } - t \tau \beta ( 1 - \beta ) ^ { 2 } [ ( 1 + \beta ) \gamma ^ { 2 } + 1 - \frac { \beta \gamma } { 2 } ] } . } \end{array}$

(a) Note that

$$
\frac {\partial \hat {p} ^ {*}}{\partial \beta} = \tau^ {2} t \frac {2 M + 2 \tau - (1 - \beta) \beta t [ (2 \beta^ {2} + \beta + 1) \gamma^ {2} + 1 + \beta - \gamma \beta^ {2} ]}{M (M + \tau) ^ {2}}
$$

The third term in the numerator, $( 1 - \beta ) \beta t [ ( 2 \beta ^ { 2 } + \beta + 1 ) \gamma ^ { 2 } + 1 + \beta - \gamma \beta ^ { 2 } ]$ , increases in . When $\gamma = 1$ , the maximum value is $t \beta ( 2 -$ $\beta ^ { 3 } + \beta ^ { 2 } ) < 2 \tau$ . Therefore, the numerator is positive and $\partial \hat { p } ^ { * } / \partial \beta > 0$

(b) Note that

$$
\begin{array}{r} \frac {\partial \hat {\phi} ^ {H}}{\partial \beta} = t \tau (1 + \gamma) \frac {2 (1 - 2 \beta) (M + \tau) - (1 - \beta) ^ {3} \beta (\gamma^ {2} + 1) t}{4 M (M + \tau) ^ {2}} \\ \frac {\partial \hat {\phi} ^ {L}}{\partial \beta} = t \tau (1 - \gamma) \frac {2 (1 - 2 \beta) (M + \tau) - (1 - \beta) ^ {3} \beta (\gamma^ {2} + 1) t}{4 M (M + \tau) ^ {2}} \end{array}
$$

The denominators in both equations are positive. The numerators are the same. Therefore, as long as

$$
(1 - \beta) ^ {3} \beta (\gamma^ {2} + 1) t <   2 (1 - 2 \beta) (\sqrt {\tau^ {2} - t \tau \beta (1 - \beta) ^ {2} [ (1 + \beta) \gamma^ {2} + 1 - \beta \gamma / 2 ]} + \tau)
$$

$\partial \hat { \phi } _ { i } ^ { H } / \partial \beta > 0$ and $\partial \hat { \phi } _ { i } ^ { L } / \partial \beta > 0$ . By simplifying the above inequality, we get the condition $\begin{array} { r } { \frac { ( 1 - \beta ) ^ { 4 } } { ( 1 - 2 \beta ) ( 1 + 2 \beta \gamma ^ { 2 } + \frac { \gamma } { 2 } - \beta \gamma ) } < \frac { 4 \tau } { t ( \gamma ^ { 2 } + 1 ) ^ { 2 } } . } \end{array}$ Otherwise, $\partial \hat { \phi } _ { i } ^ { H } / \partial \beta < 0$ and $\partial \hat { \phi } _ { i } ^ { L } / \partial \beta < 0$

(c) Because $\begin{array} { r } { \hat { \pi } ^ { * } = ( 1 - \alpha ) \hat { p } ^ { * } \frac { 1 6 \tau - ( \beta - 1 ) ^ { 2 } ( \gamma ^ { 2 } + 1 ) \hat { p } ^ { * } } { 3 2 \tau } } \end{array}$ , we can get

$$
\frac {\partial \hat {\pi} ^ {*}}{\partial \beta} = (1 - \alpha) \frac {[ 8 \tau - (1 - \beta) ^ {2} (\gamma^ {2} + 1) \hat {p} _ {i} ^ {*} ] \frac {\partial \hat {p} ^ {*}}{\partial \beta} + (1 - \beta) (\gamma^ {2} + 1) \hat {p} ^ {* 2}}{1 6 \tau}
$$

Because $( 1 - \beta ) ^ { 2 } ( \gamma ^ { 2 } + 1 ) \hat { p } ^ { * } < 2 \hat { p } ^ { * } <$ 8?? and $\partial \hat { p } ^ { * } / \partial \beta > 0 ,$ , we get $\partial \hat { \pi } ^ { * } / \partial \beta > 0$

(d) Because $\begin{array} { r } { \hat { C } S = v - \hat { p } ^ { * } - \frac { t } { 4 } ( 2 - \beta ) + \frac { t ( 1 - \beta ) ^ { 2 } ( 1 + \gamma ^ { 2 } ) } { 1 6 \tau } \hat { p } ^ { * } } \end{array}$ , we can get

$$
\frac {\partial \hat {C} S}{\partial \beta} = \frac {t}{4} - [ t \tau (1 - \gamma) \frac {2 (1 - 2 \beta) (M + \tau) - (1 - \beta) ^ {3} \beta (\gamma^ {2} + 1) t}{4 M (M + \tau) ^ {2}} ] \frac {\partial \hat {p} _ {i} ^ {*}}{\partial \beta} - \hat {p} _ {i} ^ {*} \frac {t (1 + \gamma^ {2}) (1 - \beta)}{8 \tau}
$$

$\begin{array} { r } { \frac { \partial \hat { C } S } { \partial \beta } < 0 \mathrm { ~ i f ~ } \frac { t } { 4 } - [ 1 - \frac { t ( 1 - \beta ) ^ { 2 } ( 1 + \gamma ^ { 2 } ) } { 1 6 \tau } ] \frac { \partial \hat { p } _ { i } ^ { * } } { \partial \beta } < 0 , } \end{array}$ , or, equivalently, $\begin{array} { r } { \frac { \partial \hat { p } _ { i } ^ { * } } { \partial \beta } > \frac { 4 t \tau } { 1 6 \tau - ( 1 - \beta ) ^ { 2 } ( \gamma ^ { 2 } + 1 ) t } . } \end{array}$ which is true because

$$
\frac {\partial \hat {p _ {i} ^ {*}}}{\partial \beta} = \tau^ {2} t \frac {2 K + 2 \tau - (1 - \beta) \beta t [ (2 \beta^ {2} + \beta + 1) \gamma^ {2} + 1 + \beta - \gamma \beta^ {2} ]}{K (K + \tau) ^ {2}} > \frac {2 \tau^ {2} t}{(K + \tau) ^ {2}} > \frac {4 t \tau}{1 6 \tau - (1 - \beta) ^ {2} (\gamma^ {2} + 1) t}.
$$

## Proof of Proposition 5

Proof. For ease of exposition, we denote $N \equiv \sqrt { \tau ^ { 2 } - t \tau \beta ( 1 - \beta ) ^ { 2 } [ ( 1 + \beta ) \gamma ^ { 2 } + 1 - \frac { \beta \gamma } { 2 } ] } .$

(a) Note that

$$
\frac {\partial \hat {p} ^ {*}}{\partial \gamma} = \frac {(1 - \beta) ^ {2} \beta^ {2} t ^ {2} \tau^ {2} (4 (\beta + 1) \gamma - \beta)}{2 N (N + \tau) ^ {2}}
$$

$\partial \hat { p } ^ { * } / \partial \gamma > 0$ requires $4 ( \beta + 1 ) \gamma - \beta > 0$ , which is equivalent to $\gamma > \beta / ( 4 + 4 \beta )$ . Otherwise, $\partial \hat { p } ^ { * } / \partial \gamma < 0$

(b) Note that

$$
\frac {\partial \widehat {\phi} ^ {H *}}{\partial \gamma} = t \tau \beta (1 - \beta) \frac {4 N + 4 \tau - t \beta (1 - \beta) ^ {2} (4 + \beta - 5 \beta \gamma - 4 \gamma)}{8 N (N + \tau)}
$$

The third term in the numerator, $t \beta ( 1 - \beta ) ^ { 2 } ( 4 + \beta - 5 \beta \gamma - 4 \gamma )$ , decreases in $\gamma$ . When $\gamma = 0$ , the maximum value is $t \beta ( 1 - \beta ) ^ { 2 } ( 4 +$ $\beta ) < 4 \tau$ . Therefore, the numerator is always positive and $\partial \hat { \phi } ^ { H } / \partial \gamma > 0$

$$
\frac {\partial \widehat {\phi} ^ {L *}}{\partial \gamma} = t \tau \beta (1 - \beta) \frac {t \beta (1 - \beta) ^ {2} (4 - \beta + 3 \beta \gamma + 4 \gamma) - 4 \tau - 4 N}{8 N (N + \tau) ^ {2}}
$$

The first term in the numerator, $t \beta ( 1 - \beta ) ^ { 2 } ( 4 - \beta + 3 \beta \gamma + 4 \gamma )$ , increases in <sub>??</sub>. When $\gamma = 1$ , the maximum value is $t \beta ( 1 - \beta ) ^ { 2 } ( 8 - 2 \beta ) <$ <sub>4??</sub>. Therefore, the numerator is always negative and $\partial \hat { \phi } ^ { L } / \partial \gamma < 0$

(c) Denoting $M \equiv 4 ( 4 \beta \gamma - \beta + 3 \gamma ) ( K + \tau ) - ( 1 - \beta ) ^ { 2 } \beta ^ { 2 } t ( \gamma ^ { 2 } + 4 \gamma - 1 )$ , we get $\begin{array} { r } { \frac { \partial \widehat { \pi } ^ { * } } { \partial \gamma } = \frac { ( 1 - \alpha ) ( 1 - \beta ) ^ { 2 } \beta ^ { 2 } t ^ { 2 } \tau ^ { 2 } } { 1 6 N ( N + \tau ) ^ { 3 } } M . \frac { \partial \widehat { \pi } _ { i } ^ { * } } { \partial \gamma } > 0 } \end{array}$ requires $M > 0$ Because $\begin{array} { r } { \frac { \partial M } { \partial \gamma } > 0 , M | _ { \gamma = 0 } < 0 } \end{array}$ and $M | _ { \gamma = 1 } > 0$ . Therefore, there exists $\tilde { \gamma } .$ , where $\tilde { \gamma }$ is the root of $M = 0$ such that if $\gamma < \tilde { \gamma } , \partial \hat { \pi } ^ { * } / \partial \gamma < 0$ Otherwise, $\partial \hat { \pi } ^ { * } / \partial \gamma > 0$

(d) Note that

$$
\begin{array}{r l} & {\frac {\partial \hat {C S}}{\partial \gamma} = \frac {(1 - \beta) ^ {2} \beta t ^ {2} \tau}{3 2 N (N + \tau) ^ {2}} [ 8 \gamma N + 8 \tau (2 \beta^ {2} - 8 \beta (1 + \beta) \gamma + \gamma)} \\ & {- \beta (1 - \beta) ^ {2} t (4 \beta \gamma^ {3} - 3 \beta \gamma^ {2} - 4 \beta \gamma + \beta + 4 \gamma^ {3} + 4 \gamma) ]} \end{array}
$$

By simplifying $\partial \hat { C } S / \partial \gamma > 0$ , we derive the condition in part (d).

## Proof of Proposition 6

Proof. To differentiate, we use notation $\hat { p } _ { u } ^ { * } , \hat { \phi } _ { u } ^ { * } , \hat { \pi } _ { u } ^ { * }$ , and $\hat { C } S _ { u }$ to denote the equilibrium outcomes when sellers adopt uniform advertising in the presence of recommender system (i.e., we add subscript for uniform advertising).

(a) When $\gamma = \beta / ( 2 + 2 \beta )$ , from Equation (28), we get the equilibrium price $\begin{array} { r } { \hat { p } _ { | \gamma = \beta / ( 2 + 2 \beta ) } ^ { * } = \frac { 2 [ \tau - \sqrt { \tau ^ { 2 } - \beta t \tau ( 1 - \beta ) ^ { 2 } } ] } { ( 1 - \beta ) ^ { 2 } } = \hat { p } _ { u } ^ { * } } \end{array}$ . According to Proposition 4(a), the price increases in <sub>??</sub> when $\gamma > \beta / ( 4 + 4 \beta )$ , and thus $\hat { p } _ { | \gamma > \beta / ( 2 + 2 \beta ) } ^ { * } > \hat { p } _ { u } ^ { * }$

(b) When $\gamma = 0$ , we get $\hat { \phi } ^ { H * } = \hat { \phi } ^ { L * } = \hat { \phi } _ { u } ^ { * }$ . According to Proposition $5 ( \boldsymbol { \mathrm { b } } ) , \hat { \phi } ^ { H * }$ increases in <sub>??</sub> and $\hat { \phi } ^ { L * }$ decreases in <sub>??</sub>, so we get $\hat { \phi } ^ { H * } > \hat { \phi } _ { u } ^ { * } >$ $\hat { \phi } ^ { L * }$ when $\gamma \neq 0$

(c) When $\gamma = 1$ , we can verify that the profit in the targeting case is higher than that in the uniform case. Meanwhile, according to Proposition 4(c), sellers’ profits first decrease then increase with <sub>??</sub>. Therefore, if and only $\mathrm { i f } \gamma > \gamma _ { 1 } , \hat { \pi } ^ { * } \ge \hat { \pi } _ { u } ^ { * }$ , where $\gamma _ { 1 }$ is defined as the root of Equation (33).

(d) Substituting $\hat { C } S$ in Equation (32) and $\hat { C } S _ { u }$ in Equation (17) into $\hat { C } S - \hat { C } S _ { u } > 0$ and solving the inequality, we get the condition in Proposition 5(d).

## Proof of Lemma 5

Proof. (a) and (b) Using an similar approach as in the main model, we can derive the demand functions:

$$
D _ {A} = \left\{ \begin{array}{l l} \frac {(1 - \beta) k (\phi_ {\mathrm{B}} - \phi_ {\mathrm{A}}) (p _ {B} - p _ {A}) ^ {2} + t (p _ {B} - p _ {A}) [ 2 k - (1 + \beta) (k - \beta) \phi_ {\mathrm{B}} - (1 - \beta) (k - \beta) \phi_ {\mathrm{A}} ] + \beta t ^ {2} [ 2 - (1 - \beta) (\phi_ {\mathrm{B}} - \phi_ {\mathrm{A}}) ]}{4 \beta t ^ {2}}, & p _ {A} \leq p _ {B} \\ \frac {(1 - \beta) k (\phi_ {\mathrm{B}} - \phi_ {\mathrm{A}}) (p _ {B} - p _ {A}) ^ {2} + t (p _ {B} - p _ {A}) [ 2 k - (1 + \beta) (k - \beta) \phi_ {\mathrm{A}} - (1 - \beta) (k - \beta) \phi_ {\mathrm{B}} ] + \beta t ^ {2} [ 2 - (1 - \beta) (\phi_ {\mathrm{B}} - \phi_ {\mathrm{A}}) ]}{4 \beta t ^ {2}}, & p _ {A} > p _ {B} \end{array} \right.\tag{59}
$$

$$
D _ {B} = \left\{ \begin{array}{l l} \frac {(1 - \beta) k (\phi_ {\mathrm{A}} - \phi_ {\mathrm{B}}) (p _ {A} - p _ {B}) ^ {2} + t (p _ {A} - p _ {B}) [ 2 k - (1 + \beta) (k - \beta) \phi_ {\mathrm{B}} - (1 - \beta) (k - \beta) \phi_ {\mathrm{A}} ] + \beta t ^ {2} [ 2 - (1 - \beta) (\phi_ {\mathrm{A}} - \phi_ {\mathrm{B}}) ]}{4 \beta t ^ {2}}, & p _ {A} \leq p _ {B} \\ \frac {(1 - \beta) k (\phi_ {\mathrm{A}} - \phi_ {\mathrm{B}}) (p _ {A} - p _ {B}) ^ {2} + t (p _ {A} - p _ {B}) [ 2 k - (1 + \beta) (k - \beta) \phi_ {\mathrm{A}} - (1 - \beta) (k - \beta) \phi_ {\mathrm{B}} ] + \beta t ^ {2} [ 2 - (1 - \beta) (\phi_ {\mathrm{A}} - \phi_ {\mathrm{B}}) ]}{4 \beta t ^ {2}}, & p _ {A} > p _ {B} \end{array} \right.\tag{60}
$$

Firm’s optimization problem in stage 1 is characterized by the first-order conditions of Equation (3) with $D _ { A }$ and $D _ { B }$ specified in Equation (59) and Equation (60):

$$
\frac {\partial \pi_ {A}}{\partial p _ {A}} = \frac {(1 - \alpha) (1 - \beta) k (p _ {B} - p _ {A}) (p _ {B} - 3 p _ {A}) (\phi_ {B} - \phi_ {A})}{4 \beta t ^ {2}} + \frac {(1 - \alpha) [ (1 - \beta) (\phi_ {A} - \phi_ {B}) + 2 ]}{4} + \frac {(1 - \alpha) (p _ {B} - 2 p _ {A}) [ 2 k - (1 + \beta) (k - \beta) \phi_ {B} - (1 - \beta) (k - \beta) \phi_ {A} ]}{4 \beta t} = 0
$$

$$
\frac {\partial \pi_ {A}}{\partial \phi_ {A}} = - a \phi_ {A} + p _ {A} \frac {(1 - \alpha) (1 - \beta) (p _ {B} - p _ {A} + t) (k p _ {A} - k p _ {B} + \beta t)}{4 \beta t ^ {2}} = 0
$$

$$
\frac {\partial \pi_ {B}}{\partial p _ {B}} = \frac {(1 - \alpha) (1 - \beta) k (p _ {A} - p _ {B}) (p _ {A} - 3 p _ {B}) (\phi_ {A} - \phi_ {B})}{4 \beta t ^ {2}} + \frac {(1 - \alpha) [ (1 - \beta) (\phi_ {B} - \phi_ {A}) + 2 ]}{4} + \frac {(1 - \alpha) (p _ {A} - 2 p _ {B}) [ 2 k - (1 + \beta) (k - \beta) \phi_ {B} - (1 - \beta) (k - \beta) \phi_ {A} ]}{4 \beta t} = 0
$$

$$
\frac {\partial \pi_ {B}}{\partial \phi_ {B}} = - a \phi_ {B} + p _ {B} \frac {(1 - \alpha) (1 - \beta) [ (p _ {A} - p _ {B} + t) (k p _ {B} - k p _ {A} + \beta t) - 2 t \beta (p _ {A} - p _ {B}) ]}{4 \beta t ^ {2}} = 0\tag{61}
$$

Solving the above equations, we can derive equilibrium prices as in Equation (35) and advertising intensities as in Equation (36).

(c) Substituting the equilibrium prices and advertising intensities into Equation (3), we can derive the equilibrium profits as in Equation (37).

(d) Consumer surplus is the same as in Equation (52) with $p ^ { * }$ and $\phi ^ { * }$ specified in Equation (35) and (36).

## Proof of Proposition 7

Proof. (a) As we shall prove that $\hat { p } _ { i } ^ { * }$ decreases in <sub>??</sub> in Proposition 8(a) and $\begin{array} { r } { \left. \hat { p } _ { i } ^ { * } \right| _ { k = \frac { \beta ( \beta + 1 ) [ ( 1 - \beta ) t + 2 \sqrt { 2 t \tau } ] } { 8 \tau - ( 1 - \beta ) ^ { 2 } t } } = p _ { i } ^ { * } } \end{array}$ , when $\begin{array} { r } { k > \frac { \beta ( \beta + 1 ) [ ( 1 - \beta ) t + 2 \sqrt { 2 t \tau } ] } { 8 \tau - ( 1 - \beta ) ^ { 2 } t } } \end{array}$ , we get $\hat { p } _ { i } ^ { * } < p _ { i } ^ { * }$

(b) As we shall prove that $\hat { \phi } _ { i } ^ { * }$ decreases in <sub>??</sub> in Proposition 8(b), its maximum value is $\hat { \phi } _ { i } ^ { * } | _ { k = 0 } = \sqrt { ( 1 - \beta ) \beta ^ { 2 } t \tau } / ( 2 \beta \tau ) < \phi _ { i } ^ { * }$ . Therefore, $\hat { \phi } _ { i } ^ { * } < \phi _ { i } ^ { * }$

(c) From Equation (6) and Equation (37), $\hat { \pi } _ { i } ^ { * } > \pi _ { i } ^ { * }$ requires:

$$
\frac {\beta (1 - \beta) t}{8 (k - \beta)} + \frac {(\beta k + 3 k - 4 \beta) [ k \tau - \sqrt {k ^ {2} \tau^ {2} - (1 - \beta) (k - \beta) \beta t \tau} ]}{4 (1 - \beta) (k - \beta) ^ {2}} > \frac {2 t \tau}{(\sqrt {2 \tau} + \sqrt {t}) ^ {2}}\tag{62}
$$

## Proof of Proposition 8

Proof. (a) Note that

$$
\frac {\partial \hat {p} _ {i} ^ {*}}{\partial k} = - \frac {\beta \tau [ 2 \sqrt {k ^ {2} \tau^ {2} - (1 - \beta) (k - \beta) \beta t \tau} + t (k - \beta) (1 - \beta) - 2 k \tau ]}{(k - \beta) ^ {2} (1 - \beta) \sqrt {k ^ {2} \tau^ {2} - (1 - \beta) (k - \beta) \beta t \tau}}
$$

When $k \geq \beta$ , we get $2 \sqrt { k ^ { 2 } \tau ^ { 2 } - ( 1 - \beta ) ( k - \beta ) \beta t \tau } \geq 2 k \tau > 2 k \tau - t ( k - \beta ) ( 1 - \beta )$ . Therefore, the numerator is positive and $\partial \hat { p } _ { i } ^ { * } / \partial k <$ <sub>0</sub>. When $k < \beta , \partial \hat { p } _ { i } ^ { * } / \partial k < 0$ is equivalent to $2 \sqrt { k ^ { 2 } \tau ^ { 2 } + ( 1 - \beta ) ( \beta - k ) \beta t \tau } > 2 k \tau - t ( k - \beta ) ( 1 - \beta )$ . Solving this inequality, we get $4 \tau > ( 1 - \beta ) t$ , which always holds.

(b) Note that

$$
\frac {\partial \widehat {\phi} _ {i} ^ {*}}{\partial k} = - \frac {\beta [ 2 \sqrt {k ^ {2} \tau^ {2} - (1 - \beta) (k - \beta) \beta t \tau} + t (k - \beta) (1 - \beta) - 2 k \tau ]}{4 (k - \beta) ^ {2} \sqrt {k ^ {2} \tau^ {2} - (1 - \beta) (k - \beta) \beta t \tau}}
$$

In part(a), we show that $2 \sqrt { k ^ { 2 } \tau ^ { 2 } - ( 1 - \beta ) ( k - \beta ) \beta t \tau } > 2 k \tau - t ( k - \beta ) ( 1 - \beta )$ for all values of <sub>??</sub>. Therefore, we get $\partial \hat { \phi } _ { i } ^ { * } / \partial k < 0$

(c) From Equation (61), we get $\phi ^ { * } = ( 1 - \alpha ) ( 1 - \beta ) p ^ { * } / ( 4 a )$ <sub>)</sub>. Substituting $p _ { A } = p _ { B } = p _ { i } ^ { * }$ and $\phi _ { A } = \phi _ { B } = ( 1 - \alpha ) ( 1 - \beta ) p _ { i } ^ { * } / ( 4 a )$ into profit function Equation (3), we get $\pi _ { i } ^ { * } = ( 1 - \alpha ) p _ { i } ^ { * } [ 1 6 \tau - ( 1 - \beta ) ^ { 2 } p _ { i } ^ { * } ] / ( 3 2 \tau )$ . Therefore,

$$
\frac {\partial \pi_ {i} ^ {*}}{\partial k} = \frac {(1 - \alpha) [ 8 \tau - (\beta - 1) ^ {2} p _ {i} ^ {*} ]}{1 6 \tau} \frac {\partial \hat {p} _ {i} ^ {*}}{\partial k}\tag{63}
$$

Because $\partial \hat { p } _ { i } ^ { * } / \partial k < 0$ (as showed in $\mathrm { p a r t } ( \mathrm { a } ) )$ and the minimum value of $8 \tau - ( \beta - 1 ) ^ { 2 } p _ { i } ^ { * } \mathrm { ~ i s ~ } 8 \tau - ( 1 - \alpha ) ( \beta - 1 ) ^ { 2 } p _ { i } ^ { * } | _ { k = 0 } = 8 \tau - 2 ( 1 -$ $\beta ) \sqrt { ( 1 - \beta ) t \tau } > 0$ , we get $\partial \pi _ { i } ^ { * } / \partial k < 0$

Li, Chen & Raghunathan/Informative Role of Recommender Systems in E-Marketplaces
