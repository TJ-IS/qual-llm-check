---
otero_id: 11608
otero_key: "GSCHNKVJ"
title: "Recommender System Rethink: Implications for an Electronic Marketplace with Competing Manufacturers"
authors: "Lusi Li; Jianqing Chen; Srinivasan Raghunathan"
year: "2018"
journal: "Information Systems Research"
doi: "10.1287/isre.2017.0765"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
This article was downloaded by: [130.63.180.147] On: 17 December 2018, At: 15:28 Publisher: Institute for Operations Research and the Management Sciences (INFORMS) INFORMS is located in Maryland, USA

# Information Systems Research

![](/api/attachments/GSCHNKVJ/fulltext/images/d1382af02e6bfe2f5d6e8d2ea2428b69a41ba5daf22429249dc5fc052b360089.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

# Recommender System Rethink: Implications for an Electronic Marketplace with Competing Manufacturers

Lusi Li, Jianqing Chen, Srinivasan Raghunathan

To cite this article: Lusi Li, Jianqing Chen, Srinivasan Raghunathan (2018) Recommender System Rethink: Implications for an Electronic Marketplace with Competing Manufacturers. Information Systems Research

Published online in Articles in Advance 17 Dec 2018

https://doi.org/10.1287/isre.2017.0765

Full terms and conditions of use: http://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

Copyright © 2018, INFORMS

Please scroll down for article—it is on subsequent pages

INFORMS is the largest professional society in the world for professionals in the fields of operations research, management science, and analytics. For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# Recommender System Rethink: Implications for an Electronic Marketplace with Competing Manufacturers

Lusi Li,<sup>a</sup> Jianqing Chen,<sup>b</sup> Srinivasan Raghunathan<sup>b</sup>

<sup>a</sup> College of Business and Economics, California State University, Los Angeles, Los Angeles, California 90032; <sup>b</sup> Jindal School of Management, The University of Texas at Dallas, Richardson, Texas 75080

Contact: lli57@calstatela.edu, http://orcid.org/0000-0001-5270-9765 (LL); chenjq@utdallas.edu,

http://orcid.org/0000-0001-5907-2680 (JC); sraghu@utdallas.edu, http://orcid.org/0000-0002-2782-3520 (SR)

Received: February 9, 2015

Revised: May 3, 2016; July 8, 2017

Accepted: October 11, 2017

Published Online in Articles in Advance: December 17, 2018

https://doi.org/10.1287/isre.2017.076

Copyright: © 2018 INFORMS

Abstract. Recommender systems that inform consumers about their likely ideal products have become the cornerstone of e-commerce platforms that sell products from competing manufacturers. Using a model of an electronic marketplace in which two competing manufacturers sell their products through a common retail platform, we study the efect of recommender systems on the retail platform, manufacturers, consumer surplus, and social welfare. In our setting, consumers are diferentiated with respect to their preference for the two products (locational diferentiation) and awareness about the two products (informational diferentiation). A recommender system selects the recommendation based on a recommendation score, which is a weighted sum of expected retailer profit and expected consumer value. We find that the recommender system may benefit or hurt the retailer and the manufacturers depending on the signs and magnitudes of the substitution efect and demand efect of the recommender system. The substitution efect of the recommender system either intensifies or softens the price competition between two manufacturers through two forces—its direct influence alters the informational diferentiation of consumers (which afects the markup that manufacturers can charge), and its strategic influence motivates the manufacturers to use price as a lever to attract more recommendations in their favor. The demand efect of the recommender system increases overall consumer awareness, but, depending on the substitution efect, may increase or decrease the demand. The recommendation strategy, namely, the relative weight assigned to retailer profit vis-á-vis consumer value in computing the recommendation score, along with recommender system precision and the relative sizes of segments of consumers with diferent awareness levels, determines whether the retailer benefits from the recommender system and by how much. We find that the retailer’s optimal recommendation strategy is mildly profit oriented in the sense that it assigns a larger, but not too large, weight to retailer profit compared to consumer value, and that under the optimal strategy, the price competition is less intense and the retailer profit is higher compared to when there is no recommender system. Furthermore, an increase in either the recommender system precision or the fraction of consumers that are aware of at least one product induces the retailer to adopt a more profit-oriented recommendation strategy.

History: Kai-Lung Hui, Senior Editor; Xiaoquan (Michael) Zhang, Associate Editor.

Funding: Jianqing Chen acknowledges financial support from the National Natural Science Foundation of China [Grants 71528004, 71431002, and 71671036]. Supplemental Material: The e-companion is available at https://doi.org/10.1287/isre.2017.0765.

Keywords: analytical modeling • economics of IS • recommender system • electronic commerce

## 1. Introduction

Recommender systems, which have become ubiquitous in e-commerce platforms, are touted as sales support tools that help consumers find their “ideal” product among the vast variety of products sold in those platforms (Hennig-Thurau et al. 2012). A recommender system provides consumers with product recommendations based on criteria such as user-specific preference, a user’s shopping history, or choices made by other consumers with similar profiles (Xiao and Benbasat 2007). Over 35% of sales on Amazon and more than 60% of the rentals on Netflix result from recommendations (Hosanagar et al. 2013).

Commercial recommender systems vary along different dimensions such as the algorithm used to generate recommendations, the timing related to when recommendations are presented to a consumer, the manner in which recommendations are presented, the type of products (complementary or competing) recommended, and the objective to be achieved through the recommendation. For instance, while content-based recommender systems use product characteristics (e.g., genre, mood, author, and price in the case of books)

to recommend items that are similar to products that a target consumer previously bought or liked, collaborative filter-based recommender systems recommend products based on purchase history or taste of similar consumers. On the timing and product type dimensions, while some systems recommend complementary products after a consumer has made a purchase, others recommend competing products before the purchase (e.g., when the consumer visits the platform or searches for a product). Although it is widely assumed that recommender systems are designed to benefit consumers by recommending the products they desire (Xiao and Benbasat 2007), some are designed not just to benefit consumers but also to steer them toward products that serve the seller’s own interests (Häubl and Murray 2006). For example, instead of recommending solely based on preference match, firms can bias the recommendation by recommending products with certain characteristics (e.g., high profit margin products and soon-to-be discontinued products) to attain higher profits (Das et al. 2009, Xiao and Benbasat 2015).

Research indicates that recommender systems afect consumer decision making (Tam and Ho 2006). For instance, recommender systems could inform consumers about products they are unaware of and enlarge the consumers’ consideration set (informative role), or increase the purchase probability of the recommended product if the consumer is already aware of it (persuasive role) (Gretzel and Fesenmaier 2006, Tam and Ho 2005, Fleder and Hosanagar 2009). Research has also examined the impact of recommender systems on product sales. For instance, some studies argue that recommender systems contribute to the long tail efect by exposing consumers to niche products, but others argue that some recommender system designs increase the popularity of already popular products (Mooney and Roy 2000, Fleder and Hosanagar 2009). Departing from these studies, in this paper we aim to study how a recommender system deployed by a retail platform afects the competition between manufacturers that sell competing products via the platform and the payofs of players such as manufacturers, platform, consumers, and society, and the consequent implications for the recommendation strategy to be adopted by the retail platform.

The question of how recommender systems afect the price competition between substitutable products is important to both practitioners and academics. The question becomes especially important in the context of a dominant e-commerce platform that sells competing products from diferent manufacturers while simultaneously recommending a subset of these products. Such a two-level channel structure with one dominant e-commerce platform is commonly observed in practice (e.g., Amazon’s online marketplace). In such contexts, although each manufacturer views the substitutable products from other manufacturers as competitors, the platform may view the products as satisfying the diferent needs of diferent consumers. Therefore, from a platform’s perspective, an analysis of recommender systems’ efects on both consumers (demand side) and manufacturers (supply side) is essential for a more complete understanding of the implications of recommender systems. In particular, while extant empirical research finds evidence for increased sales for recommended products, it is unknown whether and under what conditions recommender systems increase the platform’s profitability. The efect of recommender systems on the manufacturers also remains unexplored and unclear despite the ubiquity of these systems in e-commerce platforms. Furthermore, how recommender system design afects the platform and manufacturers is yet another important question for the platform.

To address these questions, we develop an analytical model in which two manufacturers sell substitutable products through a common retail platform (hereafter referred to as the retailer).<sup>1</sup> Manufacturers set the sales prices, and the retailer charges a percentage of the sales price as a fixed commission. Consumers visiting the retailer have heterogeneous preferences. While some are loyal consumers that buy only from the manufacturer they are loyal to, others are shoppers that are seeking to buy the product that ofers a higher surplus. Shoppers are heterogeneous in their awareness of the two products, which could be a consequence of diferent advertising venues, such as TV, newspapers, and the Internet, accessible to manufacturers and consumers. We distinguish three types of shoppers based on their awareness about products when they visit the retailer: partially informed consumers, who are aware of only one product; fully informed consumers, who are aware of both products; and unin formed consumers, who are aware of neither product. The retailer employs a recommender system that ranks the products based on a recommendation score that is a weighted sum of expected consumer value and expected retailer profit if the product is recommended. While making the recommendation, the retailer knows the profit that it will receive from the sale of a product, but is uncertain about the consumer preference and the product the consumer will buy after the recommendation. We model the uncertainty using recommender system precision, which refers to the accuracy with which the recommender system infers the consumer preference. Under this model, we first derive the impacts of a recommender system (with exogenously specified characteristics) on the retailer, manufacturers, consumers, and the society, and examine how the recommender system characteristics and market characteristics such as the product awareness levels among consumers in the absence of recommender system afect the impacts. This analysis allows us to articulate the key drivers of recommender system impacts. Then, we investigate the retailer’s optimal recommendation strategy in terms of the relative weight the retailer should assign to its own profit while choosing the recommendation. This analysis allows us to derive significant implications pertaining to the retailer’s choice of recommendation strategy.

One key finding from our analysis is that when manufacturers strategically respond to the retailer’s deployment of the recommender system, the retailer and manufacturers may benefit or be hurt, depending on recommender system and market characteristics. The impacts of the recommender system are dictated by the signs and magnitudes of the substitution efect, which either intensifies or softens the price competition between manufacturers, and the demand efect, which either increases or decreases the demand.

The substitution efect arises because of the strategic interactions between manufacturers and can be attributed to two influences. First, the direct influence of the recommender system in changing the price competition is that recommendations alter the relative sizes of the consumer group that manufacturers compete for (common turf ) and the consumer groups the manufacturers cannot compete for (monopoly turf ), which afect the markups that manufacturers can charge. On the one hand, recommendations convert uninformed shoppers to partially informed shoppers, which increases each manufacturer’s monopoly turf. On the other hand, recommendations convert some partially informed shoppers to fully informed shoppers, which makes more shoppers aware of both products and increases the common turf. Reacting to the changes in the sizes of the monopoly turf and common turf, manufacturers price diferently in the presence of the recommender system. Second, the strategic influence of the recommender system in changing the price competition is that the recommender system presents manufacturers an opportunity to use price as a lever to attract more recommendations in their favor—when an increase in price increases (decreases) the chance of being recommended, manufacturers have an incentive to increase (decrease) prices to attract more recommendations. Depending on the magnitudes of the two influences, the substitution efect may be positive for the sellers (softening the price competition) or negative (intensifying the price competition).

The demand efect of the recommender system is attributed to the following. The recommender system increases the product awareness among shoppers, which increases the demand from shoppers; however, the demand from loyal consumers may increase or decrease depending on whether the substitution efect increases or decreases the prices. Consequently, the overall demand can be higher or lower in the presence of the recommender system than in its absence.

Whether the recommender system benefits or hurts the sellers depends on the recommender system precision, the recommendation strategy (i.e., the relative weight assigned to retailer profit vis-a-vis consumer value in computing the recommendation score), and market characteristics such as the relative sizes of the three consumer segments pertaining to product awareness. We identify two types of recommendation strategies that generally have qualitatively different impacts on sellers and consumers. When the relative weight assigned to the retailer profit is high (low) such that an increase in price increases (decreases) the recommendation score for the product, we refer to it as a profit-oriented (consumer-oriented) recommender system. While a highly profit-oriented recommender system induces manufacturers to set high prices, which provides high profit margins to the retailer and manufacturers, it may significantly decrease the demand from loyal consumers. As a result, ironically, a highly profit-oriented recommender system may hurt the manufacturers and the retailer. On the other hand, a consumer-oriented recommender system, although inducing manufacturers to undercut each other’s price, can increase consumer awareness and spur the demand from loyal consumers, and thus may benefit the manufacturers and the retailer. We thus show that a profit-oriented system does not necessarily benefit the retailer, nor does a consumeroriented system necessarily hurt the retailer. Furthermore, when the recommender system is consumer oriented, an increase in precision softens the price competition and increases the sellers’ benefit from the recommender system; however, when the recommender system is profit oriented, an increase in precision intensifies the price competition and decreases the sellers’ benefit from the recommender system if the profit orientation is not too high. Similarly, the impacts of consumer awareness levels also depend on whether the recommender system is consumer oriented or profit oriented. Therefore, it is critical for the retailer to choose an optimal recommendation strategy that accounts for recommender system precision and market characteristics.

We find that the optimal recommender system that maximizes the retailer’s profit is mildly profit oriented. Under the optimal recommendation strategy, the price competition is less intense and the retailer profit is higher compared to when there is no recommender system. Furthermore, an increase in either the recommender system precision or the fraction of consumers that are aware of at least one product induces the retailer to adopt a more profit-oriented recommendation strategy.

Consumers benefit from the recommender system only when the recommendation strategy does not assign too large a relative weight to the retailer profit. Ironically, an increase in precision improves the consumer surplus when the recommender system is profit oriented, but may not improve consumer surplus if the recommender system is consumer oriented. Consequently, if the retailer deploys the optimal recommendation strategy, then the consumers are also better of if the recommender system’s precision is high. The impacts of the recommender system on the social welfare are qualitatively similar to those on consumers.

Altogether, our results reveal that when the recommender system is highly profit oriented, all players in the marketplace—the retailer, manufacturers, consumers, and the society—are hurt by the recommender system. In particular, the intention of increasing profit by deploying a highly profit-oriented recommender system can hurt the retailer itself because of the strategic interactions among the diferent players. On the other hand, if the retailer deploys the optimal recommendation strategy that maximizes its own profit, every player in the market place—the retailer, manufacturers, consumers, and the society—is better of in the presence of the recommender system than in its absence if the recommender system has a high precision.

The rest of this paper is organized as follows. In the next section, we review the related literature. In Section 3, we develop an analytical framework to model the impact of a recommender system in a channel structure where two competing sellers sell on a common platform. Section 4 examines the implication of the recommender system by comparing the scenario in which consumers purchase without recommendations with the scenario with recommendations. In Section 5, we examine the impact of recommender system and market characteristics on the results. In Section 6, we examine the characteristics and impacts of the optimal recommendation strategy that maximizes the retailer’s payof. Section 7 concludes this paper with a discussion on managerial implications.

## 2. Related Literature

The existing literature on recommender systems generally falls into three streams. The first stream focuses on recommendation algorithms. Much of the work in this stream has focused on predicting consumer preference (e.g., Häubl and Trifts 2000, Hostler et al. 2005). Adomavicius and Tuzhilin (2005) provide a review of this work. Burke (2002) proposes a recommender system that considers attributes such as price, quality, and delivery date while choosing the recommendation for a user. Wang and Zhang (2011) develop an algorithm that uses consumer net utility and show that their algorithm outperforms the widely used collaborative filtering-based recommender systems that do not use net utility. Algorithms to increase recommendation diversity have also been proposed (McNee et al. 2006, Vargas and Castells 2011, Pu et al. 2011). Algorithms that focus on consumer preference or utility do not explicitly incorporate firm revenue or profit in their recommendation algorithm, and they implicitly assume that recommending the product that ofers the highest value to the consumer benefits the firm both in the short run, based on the notion that recommendations that are not likely to be followed by the users are worthless, and in the long run, based on the idea that good recommendations increase consumer satisfaction and trust. Some recent studies have focused on revenue-driven recommendations. Chen et al. (2008) model purchase probabilities and recommend k-highest-ranked items in terms of expected revenue (purchase probability times price). Das et al. (2009) consider the trust between users and the recommender system to predict the purchase probability. Hosanagar et al. (2008) examine two trade-ofs faced by a vendor when designing a recommender system—the trade-of between the relevance of a product to a consumer and the firm’s margin from selling the product, and the trade-of between increasing near-term profit and increasing long-run future profit. Shani et al. (2005) treat the problem of generating recommendations as a sequential optimization problem that takes into account the long-term efects and shortterm efects of a recommendation. Unlike the studies in this stream of research, we focus on the economic impact of recommender systems on upstream manufacturers and the consequence of strategic manufacturer responses to the retailers. Consistent with the two broad foci of recommender systems—consumer and seller—we adopt a recommendation strategy that uses a weighted sum of seller revenue and consumer value.

The second stream of literature focuses on the impact of recommender systems on consumers’ decision making and choices. Senecal and Nantel (2004) show that recommended products are selected twice as often as nonrecommended products. This influence is moderated by the type of recommendation source and the type of product. Cooke et al. (2002) find that context and familiarity can afect a consumer’s reaction to recommendations. Consistent with empirical findings in this stream of research, we develop a model in which recommended products have a higher average chance of being bought than nonrecommended products, but whether the recommended product is purchased depends on consumer preference, price, and awareness about the competing product.

The third stream of research examines recommender systems’ efect on product sales and sales diversity. Using a simulation model, Fleder and Hosanagar (2009)

show that recommendations made on the basis of sales and ratings reinforce the popularity of already popular products. Hosanagar et al. (2013) empirically show that recommender systems can lead to consumers purchasing more similar items. Using data from a video-on-demand retailer, Hinz and Eckert (2010) show how diferent classes of search and recommendation tools afect the distribution of sales across products, total sales, and consumer surplus. Brynjolfsson et al. (2011) find that a firm’s online sales channel has a slightly higher diversity than its ofline channel, and they attribute the diference to recommender systems. Oestreicher-Singer and Sundararajan (2012a) empirically show that recommender systems induce significantly flatter demand and revenue distributions. Oestreicher-Singer and Sundararajan (2012b) show that, on average, the explicit visibility of a copurchase relationship can amplify the influence of complementary products on each other’s demand. Pathak et al. (2010) find that the strength of recommendations has a positive efect on sales and prices and that this efect is moderated by the recency efect. Jabr and Zheng (2014) analyze the efect of recommendations and word-of-mouth reviews on product sales in a competitive environment and show that higher referral centrality of competing products is associated with lower product sales. In contrast to this stream of research, we examine the impact of recommender systems on competing products using an analytical model and study upstream efects of downstream deployment of a recommender system.

Much of the previously discussed research uses a technical or empirical research methodology. Theoretical research that has examined the impact of recommender systems is limited. Hervas-Drane (2015) shows that when recommender systems based on consumer taste are introduced alongside traditional word of mouth, there is a positive impact on consumers’ interest in niche products and a decrease in market concentration. Bergemann and Ozmen (2006) use a twostage game to show how a firm can strategically choose its price in the first stage to generate recommendations in the second stage. Our study departs from these in that we examine the efect of recommender systems in the setting of competing sellers in a channel structure, while previous studies consider a single seller and ignore the strategic interactions between sellers.

Our study is also related to the marketing literature on informative advertising and competition. Bester and Petrakis (1995) and Grossman and Shapiro (1984) predict an inverse relationship between advertising level and prices in a diferentiated product market when advertising provides uninformed consumers with price information. Soberman (2004) extends Grossman and Shapiro (1984) to show that informative advertising alone can lead to either higher or lower prices depending on the level of diferentiation between competing firms. While these studies consider uniform advertising, another stream of literature considers targeted advertising. Iyer et al. (2005) investigate how competing firms in a horizontally diferentiated market choose the advertising strategy when they can target consumer segments according to their preferences. Gal-Or et al. (2006) examine how an advertiser should allocate resources to increase the quality of targeting. Gal-Or and Gal-Or (2005) study firms’ advertising strategy when they use a single media distributor such as television cable company as the channel for advertising. Diferent from these studies, our focus is on the impact of various recommender systems on competing sellers’ profits.

## 3. Model

We consider a two-level channel structure with two manufacturers (A and B), one common retailer (R), and a continuum of consumers with heterogeneous preferences. Manufacturer A (B) produces product A (B) and sells the product via R. Each manufacturer sets the price of its product, and the retailer charges the manufacturers a commission equal to α fraction of the price on each sale.<sup>2</sup> We assume that the fixed and marginal production costs are zero.

The two products are horizontally diferentiated and have diferent levels of misfit to diferent consumers. In particular, we assume that the products are located at the two end points of a Hotelling line of a unit length, with product A being at 0 and product B being at 1. Consumers are uniformly distributed along the Hotelling line. The distance between a product and a consumer measures the degree of misfit of the product to the consumer. We refer to consumers’ diferentiation along the Hotelling line as locational diferentiation.

We distinguish two types of consumers—loyal consumers and shoppers—that difer with respect to whether and how recommendations afect their purchase decisions. Loyal consumers consider purchasing only the product from the manufacturer that they are loyal to. They are aware of the product from the manufacturer they are loyal to, but they may or may not purchase the product depending on its price and their misfit cost. On the other hand, shoppers are looking to purchase a product but are not loyal to any specific manufacturer. They will buy the product that ofers the highest net utility from the set of products they are aware of. Thus, while the purchase decisions of shoppers are influenced by recommendations, those of loyal consumers are not. We normalize the number of shoppers in the market to one and let γ be the number of consumers loyal to each manufacturer.

## 3.1. Loyal Consumers

For a loyal consumer, the utility of the product she is loyal to is $v _ { L } ,$ and the unit misfit cost is ${ t _ { L } } . ^ { 3 }$ Thus, for a consumer loyal to product A and located at z on the Hotelling line, the net utility from buying product A is $U _ { A L } = v _ { L } - z t _ { L } - p _ { A }$ . Analogously, for a consumer loyal to product B and located at $z ,$ the net utility from buying product B is $U _ { { \scriptscriptstyle B L } } = v _ { { \scriptscriptstyle L } } - ( 1 - z ) t _ { { \scriptscriptstyle L } } - p _ { { \scriptscriptstyle B } } . \dot { \mathrm {  ~ A ~ } }$ loyal consumer buys the product that she is loyal to if and only if her net utility is nonnegative. We can thus formulate the demand for product i from its loyal consumers as $D _ { i L } = ( \gamma / t _ { L } ) ( v _ { L } - \mathbf { \bar { \gamma } } p _ { i } ) , i \in \{ A , B \}$ . For expositional clarity, we define $h \equiv \gamma v _ { L } / t _ { L }$ and $\mu \equiv \gamma / t _ { L }$ . Then, we have

$$
D _ {i L} = h - \mu p _ {i},\tag{1}
$$

in which $\mu$ measures the price sensitivity of its loyal consumers, and h represents the potential market size of loyal consumers for a product.

## 3.2. Shoppers

For a shopper, the utility of either product is $v ,$ and the unit misfit cost is t. Thus, for a shopper located at $z ,$ the net utility from buying product A is $U _ { A } = v - z t - p _ { A } ,$ and that from buying product B is $U _ { B } = v - ( 1 - z ) t - p _ { B } .$ Shoppers may have diferent levels of awareness of the two products: fully informed shoppers are aware of both products, uninformed shoppers are aware of neither product, and partially informed shoppers include two groups—consumers who are aware of only product A and consumers who are aware of only product B. In the absence of recommendations, we assume that the fraction of the fully informed shopper segment is $\theta _ { b . }$ , the fraction of each partially informed shopper group is θ, and the proportion of uninformed shoppers is $1 - 2 \theta - \theta _ { b }$ . This basic awareness structure is implied by the existence of advertising venues accessible to manufacturers and consumers, such as TV, newspapers, and the Internet. A shopper’s awareness is independent of her location. We refer to consumers’ diferentiation along the awareness dimension as informational diferentiation.

## 3.3. Recommendation Precision

The recommender system is uncertain about a consumer’s true preference or location on the Hotelling line and uses information such as purchase data, rating data, and profile data to estimate her location. The estimate may be imperfect, and we use a commonly used approach to model this estimation $( \mathrm { e . g . }$ , Lewis and Sappington 1994, Johnson and Myatt 2006). In particular, we assume that the retailer observes a signal s regarding consumer’s location. The signal could be viewed as the output of the consumer preference prediction model that is ubiquitous in recommender systems. The signal equals the consumer’s true location with probability $\beta ,$ and with probability $( 1 - \beta )$

the signal is uninformative and follows the prior (uniform) distribution of consumer location; that is, for a consumer whose true location is y, $P ( s = y \mid z = y ) = \beta$ and $P ( s \neq y \vert z = y ) = 1 - \beta ,$ where $y \in \left[ 0 , 1 \right]$ . As shown in the appendix, using Bayesian updating, we can derive the consumer’s expected location given the signal as

$$
\mathbb {E} (z \mid y) = \frac {1 - \beta}{2} + \beta y.\tag{2}
$$

Thus, the model indicates that the signal is informative $( \mathrm { i . e . , }$ , provides useful information for the retailer to estimate the consumer’s preference) but noisy $( \mathrm { i . e . } $ , does not perfectly reveal the true preference). We refer to $\beta$ as the precision of the recommender system.

## 3.4. Recommendation Strategy

In the base model, we consider that when a consumer comes to the retailer’s site, the retailer recommends one product to this consumer. In the extension, we also examine the case where the retailer recommends both products. The retailer considers two factors when deciding which product to recommend: the retailer’s profit and the consumer’s net utility. The retailer’s profit from a product is determined by the price of the product and the commission rate for each transaction. If the consumer purchases product $i ,$ the retailer gets a profit of $\alpha p _ { i } , i \in \{ A , B \}$ . We assume that the retailer assigns a relative weight of w to its own profit vis-a-vis consumer’s net utility. A high (low) value for w suggests that the recommender system is more profit (consumer) oriented. Because the retailer does not know the consumer’s type (loyal consumer or shopper) or true location, we define the score used by the recommender system for product i using expected retailer profit and expected consumer net utility as follows:

$$
\begin{array}{l} R _ {i} = \mathbb {E} (\text { consumer   net   utility } \mid i \text { is   recommended }) \\ \quad + w \mathbb {E} (\text { retailer   profit } \mid i \text { is   recommended }). \end{array}\tag{3}
$$

The retailer recommends the product that has a higher score. A model extension with the retailer recommending both products can be found in the e-companion.

The sequence of events is as follows. In Stage 1, manufacturers set prices $p _ { A }$ and $p _ { B }$ simultaneously. In Stage 2, consumers visit the platform and make their purchase decisions. Two scenarios are considered: one without the recommender system and the other with the recommender system. We use the scenario without the recommender system as the benchmark to analyze the efect of the recommender system. In the scenario without the recommender system, consumers make their purchase decisions based on their awareness and preferences of the products. In the scenario with the recommender system, the retailer recommends one product to each consumer in Stage $^ { 2 , }$ and consumers make their purchase decisions with this additional information.

Table 1. Summary of Notations

<table><tr><td>Notation</td><td>Definition and comments</td></tr><tr><td> $v$ </td><td>Utility for a product of a shopper</td></tr><tr><td> $t$ </td><td>Unit misfit cost of a shopper</td></tr><tr><td> $v_{L}$ </td><td>Utility for a product of a loyal consumer</td></tr><tr><td> $t_{L}$ </td><td>Unit misfit cost of a loyal consumer</td></tr><tr><td> $\gamma$ </td><td>The size of the loyal consumers for a product</td></tr><tr><td> $h$ </td><td> $h \equiv \gamma v_{L}/t_{L}$ , indicates the potential demand from the loyal consumers for a product</td></tr><tr><td> $\mu$ </td><td> $\mu \equiv \gamma/t_{L}$ , indicates the price sensitivity of the loyal consumers for a product</td></tr><tr><td> $\theta$ </td><td>Proportion of each partially informed consumer segment</td></tr><tr><td> $\theta_{b}$ </td><td>Proportion of fully informed consumers</td></tr><tr><td> $\beta$ </td><td>Probability of getting a correct signal about consumer location</td></tr><tr><td> $w$ </td><td>Weight on profit in the recommendation score</td></tr><tr><td> $R_{i}$ </td><td>Recommendation score for product  $i, i \in \{A, B\}$ </td></tr><tr><td> $p_{i}$ </td><td>Price of product  $i, i \in \{A, B\}$ </td></tr><tr><td> $\alpha$ </td><td>Commission rate charged by the retailer</td></tr></table>

We assume that the cost of developing the recommender system and the cost of providing a recommendation are zero. A consumer’s type, her awareness about a product, and her preference are private information. All other model parameters are common knowledge. All players are risk neutral. Table 1 summarizes the parameters used in the paper.

Finally we make the following technical assumptions for our base model to rule out trivial or unrealistic cases.

Assumption 1.

$$
\max \left\{\frac {(2 \theta + \theta_ {b}) t}{\theta_ {b} + 2 \mu t}, \frac {\beta t}{(1 - \alpha w) (1 - \theta - \theta_ {b}) + \beta (\theta + \theta_ {b}) + 2 \beta \mu t} \right\} <   v _ {L} <   t _ {L}.
$$

Assumption 2.

$$
\begin{array}{c} v > \max \Bigg \{t \frac {2 (\theta + \theta_ {b}) + 2 (2 \mu t + h)}{\theta_ {b} + 4 \mu t}, \\ t \frac {(1 - \alpha w) (1 - \theta - \theta_ {b}) + \beta (1 + \theta + \theta_ {b}) + 2 \beta (2 \mu t + h)}{(1 - \alpha w) (1 - \theta - \theta_ {b}) + \beta (\theta + \theta_ {b}) + 4 \beta \mu t} \Bigg \} \end{array}
$$

Assumption 3.

$$
\beta > \frac {(1 - \theta - \theta_ {b}) (\alpha w - 1)}{\theta + \theta_ {b} + 2 \mu t}.
$$

Assumption 1 ensures that the demand from loyal consumers is positive in the equilibrium $( \mathrm { i . e . , }$ , sellers do not target only shoppers) and loyal consumers are not fully covered. Assumption 2 ensures that all shoppers except the uninformed ones buy. Assumption 3 ensures that sellers’ profit functions in the presence of recommendation are concave in their respective prices, which guarantees a unique pure strategy equilibrium.

## 4. Impacts of the Recommender System

In this section, using backward induction, we first derive the subgame perfect equilibrium for the case without the recommender system and for the case with the recommender system. We then analyze the impacts of the recommender system by comparing the equilibrium outcomes in the two cases.

## 4.1. Benchmark Case (No Recommendation)

A shopper buys the product that ofers a higher net utility from the set of products she is aware of. We denote as $z _ { 0 }$ the location of the marginal shopper who would be indiferent between the two products if she were fully informed. Based on the utility function, we have

$$
z _ {0} = \frac {p _ {B} - p _ {A} + t}{2 t}.\tag{4}
$$

Shoppers located at $z < z _ { 0 }$ would, if fully informed, purchase product $A ,$ and shoppers located at $z > z _ { 0 }$ would purchase product B. Therefore, the demands for the two products from shoppers can be formulated as $\bar { D } _ { A S } = \bar { \theta ^ { + } } z _ { 0 } \theta _ { b }$ and $D _ { B S } = \mathbf { \bar { \theta } } + ( 1 - z _ { 0 } ) \theta _ { b }$ . The total demand for product i is given by

$$
D _ {i} = D _ {i S} + D _ {i L},\tag{5}
$$

where $D _ { i L }$ is defined in Equation (1). The manufacturers maximize their profits by choosing their optimal prices:

$$
\max _ {p _ {i}} \pi_ {i} = (1 - \alpha) p _ {i} D _ {i}.\tag{6}
$$

Based on their best responses to each other, we obtain the equilibrium price and demand for each manufacturer. The following lemma summarizes the equilibrium outcome.

Lemma 1. In the absence of the recommender system, the equilibrium prices, demands, manufacturer profits, retailer profit, consumer surplus, and social welfare are as follows:

(a) Price:

$$
\bar {p} _ {A} ^ {*} = \bar {p} _ {B} ^ {*} = t + 2 t \left(\frac {\theta + h - 2 \mu t}{\theta_ {b} + 4 \mu t}\right).\tag{7}
$$

(b) Demand:

$$
\bar {D} _ {A} ^ {*} = \bar {D} _ {B} ^ {*} = \left(\frac {2 \theta + \theta_ {b}}{2} + h\right) \left(1 - \frac {2 \mu t}{\theta_ {b} + 4 \mu t}\right).\tag{8}
$$

(c) Manufacturer profit:

$$
\bar {\pi} _ {A} ^ {*} = \bar {\pi} _ {B} ^ {*} = (1 - \alpha) t \left(\frac {2 \theta + \theta_ {b} + 2 h}{\theta_ {b} + 4 \mu t}\right) ^ {2} \left(\frac {\theta_ {b}}{2} + \mu t\right).\tag{9}
$$

(d) Retailer profit:

$$
\bar {\pi} _ {R} ^ {*} = \alpha t \left(\frac {2 \theta + \theta_ {b} + 2 h}{\theta_ {b} + 4 \mu t}\right) ^ {2} (\theta_ {b} + 2 \mu t).\tag{10}
$$

(e) Consumer surplus:

$$
\begin{array}{r} \bar {C S} ^ {*} = (2 \theta + \theta_ {b}) \left(v - t \frac {2 \theta + \theta_ {b} + 2 h}{\theta_ {b} + 4 \mu t}\right) - t \frac {4 \theta + \theta_ {b}}{4} \\ + \frac {[ \theta_ {b} h - (2 \theta + \theta_ {b} - 2 h) \mu t ] ^ {2}}{\mu (\theta_ {b} + 4 \mu t) ^ {2}}. \end{array}\tag{11}
$$

(f) Social welfare:

$$
\begin{array}{l} \bar {W} ^ {*} = (2 \theta + \theta_ {b}) v - t \frac {4 \theta + \theta_ {b}}{4} \\ \qquad + \frac {[ \theta_ {b} h - (2 \theta + \theta_ {b} - 2 h) \mu t ] [ \theta_ {b} h + (6 \theta + 3 \theta_ {b} + 1 0 h) \mu t ]}{\mu (\theta_ {b} + 4 \mu t) ^ {2}}. \end{array}\tag{12}
$$

Proof. All proofs are in the appendix unless indicated otherwise.

The price expression in Lemma 1(a) has a simple interpretation. The first term is the price when there are only shoppers and all consumers are aware of both products; that is, the first term is the equilibrium price when the market includes only consumers that both manufacturers compete for; in other words, the market consists only of common turf (of consumers) that manufacturers compete in. The second term is the markup manufacturers can charge because of the presence of monopoly turf in which there is no competition between manufacturers. Two sources contribute to the presence of monopoly turf for a manufacturer: consumers loyal to the manufacturer and partially informed shoppers who are aware of only this manufacturer. Efectively, the informational diferentiation that exists among consumers—because of heterogeneity in awareness among shoppers and loyalty to one product among loyal consumers—shapes the equilibrium price, and the fraction $( \theta + h - \mathsf { \bar { 2 } } \mu t ) / ( \theta _ { b } \overset { \cdot } { + } 4 \mu t )$ measures, in some sense, the extent of informational diferentiation. A higher informational diferentiation results in a lower elasticity of demand; that is, holding everything else constant, a higher informational diferentiation among consumers softens the competition and increases the price. Therefore, the equilibrium price and profit are increasing in θ and h but decreasing in $\theta _ { b }$ . Intuitively, any increase in the size of the monopoly turf softens the price competition and an increase in the size of the common turf intensifies the price competition between manufacturers. It is also intuitive that an increase in θ, $\theta _ { b }$ or h increases the demand for both manufacturers because the total market size increases in this case.

## 4.2. With the Recommender System

When the recommender system is in place, each consumer is recommended the product that has a higher recommendation score given the signal received by the retailer regarding the consumer’s location. In this section, we first derive the recommendation score of each product based on the signal that the retailer receives about a consumer’s location. We then formulate the demand function for each manufacturer and solve for the equilibrium outcome.

We consider the retailer observes signal y regarding a consumer’s location. With probability $\gamma / ( 1 + 2 \gamma )$ this consumer is a loyal consumer of product $i ,$ and with probability $1 / ( 1 + 2 \gamma )$ , this consumer is a shopper. Suppose the consumer is a shopper. If product A is recommended, the consumer becomes fully informed with probability $\theta + \theta _ { b }$ because this case occurs if this consumer was only aware of B or fully informed before recommendation. Otherwise, this consumer becomes informed about A only, which occurs with probability $1 - \theta - \theta _ { b }$ . Analogously, if product B is recommended to this consumer, the consumer becomes fully informed with probability $\theta + \theta _ { b }$ and becomes informed about B only with probability $1 - \theta - \theta _ { b }$ . On the other hand, if the consumer is a loyal one, then regardless of the recommendation, she makes the same purchase decisions. Thus, the recommendation scores for the two products difer only in the case when a shopper is partially informed after the recommendation. We derive the diference in recommendation score as follows:

$$
\begin{array}{c} R _ {A} - R _ {B} = \frac {1 - \theta - \theta_ {b}}{1 + 2 \gamma} [ (v - \mathbb {E} (z | y) t - p _ {A}) + w \alpha p _ {A} ] \\ - \frac {1 - \theta - \theta_ {b}}{1 + 2 \gamma} [ (v - (1 - \mathbb {E} (z | y)) t - p _ {B}) + w \alpha p _ {B} ]. \end{array}\tag{13}
$$

By substituting $\mathbb { E } ( z \mid y )$ from Equation (2), we get the diference in recommendation score as

$$
R _ {A} - R _ {B} = (1 - \theta - \theta_ {b}) [ \beta (1 - 2 y) t + (1 - w \alpha) (p _ {A} - p _ {B}) ].\tag{14}
$$

We denote as $y _ { 0 }$ the marginal signal under which the recommendation scores for the two products are equal $( \mathrm { i . e . , } R _ { A } = R _ { B } )$ , which, based on Equation (14), can be derived as

$$
y _ {0} = \frac {1}{2} + \frac {(p _ {B} - p _ {A}) (1 - \alpha w)}{2 \beta t}.\tag{15}
$$

If the recommender system receives a signal less than $y _ { 0 } ,$ the retailer recommends A to the consumer; otherwise, the retailer recommends product B.

Next, we formulate the demand function for each manufacturer. Since recommendations do not afect the demand from loyal consumers, the loyal consumer demand remains the same as that given in Equation (1). For the demand from shoppers, we provide the derivation details for the case $y _ { 0 } \geq z _ { 0 } .$ . The derivation for the case $y _ { 0 } < z _ { 0 }$ is analogous. We first consider the shopper segment that is only aware of product A prior to receiving the recommendation. Within this segment, a shopper whose location is less than $z _ { 0 }$ buys product A regardless of the recommendation she receives.

A shopper whose location is between $z _ { 0 }$ and 1 buys A if she is recommended A because she is aware of only A. If she is recommended B and so is aware of both products, she buys product B. A shopper located between $z _ { 0 }$ and $y _ { 0 }$ receives a recommendation for product A (and thus buys product A) with probability $( 1 - \beta ) y _ { 0 } + \beta$ A shopper located between $y _ { 0 }$ and 1 receives recommendation for product A (and thus buys product A) with probability $( 1 - \beta ) y _ { 0 } ,$ . Combining all together, the demand for A from shoppers who are aware of only product A is

$$
\begin{array}{l} d _ {A S} = \theta \bigg [ z _ {0} + \int_ {z _ {0}} ^ {y _ {0}} P (s \leq y _ {0} | z) d z + \int_ {y _ {0}} ^ {1} P (s \leq y _ {0} | z) d z \bigg ] \\ = \theta [ y _ {0} + z _ {0} (1 - y _ {0}) (1 - \beta) ], \end{array}
$$

and the demand for product B is $d _ { B S } = \theta - d _ { A S }$

Using a similar logic, we can derive the demand functions for other shopper segments. Aggregating the demand functions for all shopper segments, we derive the demand for product i from shoppers as

$$
D _ {i S} = \frac {1}{2} + \frac {\beta (\theta + \theta_ {b}) + (1 - \theta - \theta_ {b}) (1 - \alpha w)}{2 \beta t} (p _ {\bar {i}} - p _ {i}).\tag{16}
$$

The total demand for product i is $D _ { i } = D _ { i S } + D _ { i L } ,$ in which $D _ { i L }$ is as in Equation (1). Similar to the benchmark case, we can formulate the manufacturers’ optimization problems. Based on their best responses to each other, we obtain the equilibrium price and demand for each manufacturer. The following lemma summarizes the equilibrium outcome.

Lemma 2. When the retailer uses the recommender system, the equilibrium prices, demands, manufacturer profits, retailer profit, consumer surplus, and social welfare are as follows:

(a) Price:

$$
p _ {A} ^ {*} = p _ {B} ^ {*} = \frac {\beta (1 + 2 h) t}{(1 - \alpha w) (1 - \theta - \theta_ {b}) + \beta (\theta + \theta_ {b} + 4 \mu t)}.\tag{17}
$$

(b) Demand:

$$
\begin{array}{l} D _ {A} ^ {*} = D _ {B} ^ {*} = \left(\frac {1}{2} + h\right) \\ \cdot \left(1 - \frac {2 \beta \mu t}{(1 - \alpha w) (1 - \theta - \theta_ {b}) + \beta (\theta + \theta_ {b} + 4 \mu t)}\right). \end{array}\tag{18}
$$

(c) Manufacturer profit:

$$
\begin{array}{l} \pi_ {A} ^ {*} = \pi_ {B} ^ {*} = (1 - \alpha) \beta t \\ \quad . \frac {(1 + 2 h) ^ {2} [ (1 - \alpha w) (1 - \theta - \theta_ {b}) + \beta (\theta + \theta_ {b} + 2 \mu t) ]}{2 [ (1 - \alpha w) (1 - \theta - \theta_ {b}) + \beta (\theta + \theta_ {b} + 4 \mu t) ] ^ {2}}. \end{array}\tag{19}
$$

(d) Retailer profit:

$$
\pi_ {R} ^ {*} = \alpha \beta t \frac {(1 + 2 h) ^ {2} [ (1 - \theta - \theta_ {b}) (1 - \alpha w) + \beta (\theta + \theta_ {b} + 2 \mu t) ]}{[ (1 - \alpha w) (1 - \theta - \theta_ {b}) + \beta (\theta + \theta_ {b} + 4 \mu t) ] ^ {2}}.\tag{20}
$$

(e) Consumer surplus:

$$
\begin{array}{l} C S ^ {*} = v - \frac {t [ 1 + (1 - \beta) (1 - \theta - \theta_ {b}) ]}{4} \\ \quad - \frac {\beta t (1 + 2 h)}{(1 - \alpha w) (1 - \theta - \theta_ {b}) + \beta (\theta + \theta_ {b} + 4 \mu t)} \\ \quad + \frac {1}{\mu} \left[ h - \frac {\beta \mu t (1 + 2 h)}{(1 - \alpha w) (1 - \theta - \theta_ {b}) + \beta (\theta + \theta_ {b} + 4 \mu t)} \right] ^ {2}. \end{array} \tag {2}\tag{21}
$$

(f) Social welfare:

$$
\begin{array}{l} W ^ {*} = v - \frac {t [ 1 + (1 - \beta) (1 - \theta - \theta_ {b}) ]}{4} + \frac {h ^ {2}}{\mu} \\ \qquad + \frac {2 \beta t (1 + 2 h) h}{(1 - \alpha w) (1 - \theta - \theta_ {b}) + \beta (\theta + \theta_ {b} + 4 \mu t)} \\ \qquad - 3 \mu \left[ \frac {\beta t (1 + 2 h)}{(1 - \alpha w) (1 - \theta - \theta_ {b}) + \beta (\theta + \theta_ {b} + 4 \mu t)} \right] ^ {2}. \end{array}\tag{22}
$$

The price expression given in Lemma $2 ( \mathsf { a } )$ provides insights into how the price competition between manufacturers is shaped by the recommender system. The price expression enables easier interpretation when written as

$$
\begin{array}{r l} & p _ {A} ^ {*} = p _ {B} ^ {*} = \frac {\beta (\theta + \theta_ {b} + 4 \mu t)}{(1 - \alpha w) (1 - \theta - \theta_ {b}) + \beta (\theta + \theta_ {b} + 4 \mu t)} \\ & \qquad \cdot \left[ t + 2 t \left(\frac {(1 - \theta - \theta_ {b}) / 2 + h - 2 \mu t}{\theta + \theta_ {b} + 4 \mu t}\right) \right] \\ & \qquad \equiv K \bigg [ t + 2 t \left(\frac {(1 - \theta - \theta_ {b}) / 2 + h - 2 \mu t}{\theta + \theta_ {b} + 4 \mu t}\right) \bigg ]. \end{array}\tag{23}
$$

As in the price expression for the benchmark case, t is the price under full information when there are only shoppers. In the equilibrium, $1 - \theta - \theta _ { b }$ proportion of shoppers are partially informed, and $\theta + \theta _ { b }$ proportion of shoppers are fully informed. The second term inside the brackets, $2 t ( ( \dot { 1 } - \theta - \theta _ { b } ) / 2 + h - 2 \mu t ) / ( \theta +$ $\theta _ { b } + 4 \mu t )$ , is the markup that manufacturers can charge because of the informational diferentiation that exists after the recommendation. Therefore, the expression in the brackets, $t + 2 t ( ( 1 - \theta - \theta _ { b } ) / 2 + h - 2 \hat { \mu } t ) / ( \theta +$ $\theta _ { b } + 4 \mu t )$ , can be viewed as the myopic price when manufacturers ignore the efect of pricing on which product would be recommended. The myopic prices take the same form as the ones in the benchmark case, although the sizes of partially informed shoppers and fully informed shoppers change in the presence of the recommender system, which is the direct influence of the recommender system on pricing. Another main difference from the benchmark case lies in that the myopic price term in the brackets is moderated by a coeficient, $K ,$ which captures the strategic influence of the recommender system on pricing. The strategic influence arises because, in addition to informing shoppers, the recommender system also alters manufacturers’ pricing behavior, as the prices might afect which product to be recommended for a user. When $w < 1 / \alpha ,$ , the coefficient is less then 1, and the strategic influence tends to decrease the price because a lower price for a product leads to a higher recommendation score and thus more recommendations in its favor. In contrast, when $w > 1 / \alpha ,$ the coeficient is greater than 1, and the strategic influence tends to increase the price.

We find that several qualitative results regarding the impacts of the recommender system depend on whether $w < 1 / \alpha$ . Therefore, we refer to the recommender system with $w < 1 / \alpha$ as the consumer-oriented recommender system and that with $w > 1 / \alpha$ as the profitoriented recommender system.

The implication of $\theta$ or $\theta _ { b }$ for price competition is diferent from the case with no recommender system. On one side, an increase in $\theta$ or $\theta _ { b }$ decreases the informational diferentiation and the markup that manufacturers can charge (i.e., $( ( 1 - \theta - \theta _ { b } ) / 2 + \hat { h ^ { - } } 2 \mu t ) / ( \theta + \theta _ { b } .$ + $4 \mu t )$ decreases in both θ and $\theta _ { b } )$ ). On the other side, an increase in $\theta$ or $\theta _ { b }$ increases (decreases) the strategic force (coeficient $K )$ when the recommender system is consumer (profit) oriented. Consequently, an increase in θ or $\theta _ { b }$ increases the price only when w is small or the consumer orientation is high $( \mathrm { i . e . , } w < ( 1 - \beta ) / \alpha )$ .

## 4.3. Recommender System Impacts

We can now assert the impacts of the recommender system by comparing equilibrium outcomes in the scenario without the recommender system with those in the scenario with the recommender system.

Proposition 1. Compared to the scenario without the recommender system, in the presence of the recommender system we have the following:

(a) Each product’s price is lower $( i . e . , \ p _ { i } ^ { * } < \bar { p } _ { i } ^ { * } )$ if and only if

$$
w <   \frac {1}{\alpha} + \frac {\beta}{\alpha (1 - \theta - \theta_ {b})} \left[ \theta - \frac {(1 - 2 \theta - \theta_ {b}) (\theta_ {b} + 4 \mu t)}{2 \theta + \theta_ {b} + 2 h} \right].\tag{24}
$$

(b) Each product’s demand is higher $( i . e . , D _ { i } ^ { * } > \bar { D } _ { i } ^ { * } )$ if and only if

$$
\begin{array}{r l} & w <   \frac {1}{\alpha} + \frac {\beta}{\alpha (1 - \theta - \theta_ {b})} \\ & \qquad \cdot \left[ \theta + \frac {(1 - 2 \theta - \theta_ {b}) (\theta_ {b} + 4 \mu t) (\theta_ {b} + 2 \mu t)}{(1 - 2 \theta - \theta_ {b}) (\theta_ {b} + 2 \mu t) + 2 \mu t (1 + 2 h)} \right]. \end{array}\tag{25}
$$

(c) The retailer and manufacturers are better of $( i . e . , \pi _ { i } ^ { * } > \bar { \pi } _ { i } ^ { * } )$ if and only $i f$

$$
w _ {1} <   w <   w _ {2}\tag{26}
$$

where

$$
\begin{array}{l} w _ {1} = \frac {1}{\alpha} + \frac {\beta [ (\theta + \theta_ {b}) + 4 \mu t ]}{\alpha (1 - \theta - \theta_ {b})} - \frac {\beta}{\alpha (1 - \theta - \theta_ {b})} \\ \cdot \frac {4 \mu t}{1 - \sqrt {1 - 8 \mu t [ (2 \theta + \theta_ {b} + 2 h) / ((\theta_ {b} + 4 \mu t) (1 + 2 h)) ] ^ {2} (\theta_ {b} + 2 \mu t)}}, \\ w _ {2} = \frac {1}{\alpha} + \frac {\beta [ (\theta + \theta_ {b}) + 4 \mu t ]}{\alpha (1 - \theta - \theta_ {b})} - \frac {\beta}{\alpha (1 - \theta - \theta_ {b})} \\ \cdot \frac {4 \mu t}{1 + \sqrt {1 - 8 \mu t [ (2 \theta + \theta_ {b} + 2 h) / ((\theta_ {b} + 4 \mu t) (1 + 2 h)) ] ^ {2} (\theta_ {b} + 2 \mu t)}}. \end{array} \tag {27}\tag{27}
$$

(d) Consumer surplus is higher $( i . e . , C S ^ { * } > \bar { C S ^ { * } } )$ if and only $i f w < w _ { c s } ,$ , where $w _ { c s }$ is the root of

$$
\begin{array}{c} (1 - 2 \theta - \theta_ {b}) \bigg [ v - \frac {(2 - \beta) t}{4} - p _ {i} ^ {*} \bigg ] + \frac {\theta (1 + \beta) t}{4} \\ + (\bar {p} _ {i} ^ {*} - p _ {i} ^ {*}) [ 2 \theta + \theta_ {b} + 2 h - \mu (\bar {p} _ {i} ^ {*} + p _ {i} ^ {*}) ] = 0. \end{array}\tag{28}
$$

(e) Social welfare is higher $\left( i . e . , W ^ { * } > \bar { W } ^ { * } \right) i f ( 1 - \theta - \theta _ { b } ) /$ $\beta + ( \theta + \theta _ { b } ) < ( 2 + 3 / h ) \mu t$ and $w < w _ { w } ,$ where $w _ { w }$ is the root of

$$
\begin{array}{c} (1 - 2 \theta - \theta_ {b}) \bigg [ v - \frac {(2 - \beta) t}{4} \bigg ] + \frac {\theta (1 + \beta) t}{4} \\ + (\bar {p} _ {i} ^ {*} - p _ {i} ^ {*}) [ 3 \mu (\bar {p} _ {i} ^ {*} + p _ {i} ^ {*}) - 2 h ] = 0. \end{array}\tag{29}
$$

Proposition 1(a) reveals that the price competition between manufacturers can be intensified or softened by the recommender system, depending on model parameters. Such an efect of the recommender system is captured by the change in the elasticity of the demand function, or the change in the slopes of the demand functions, as illustrated in Figure 1. Figure 1 shows the demand of product i as a function of $p _ { i }$ given the competitor’s price $p _ { \bar { i } } .$ . We refer to the change in slope of the demand function as the substitution efect of the recommender system. Clearly, the recommender system can make the demand function more elastic, inducing a negative substitution efect that intensifies price competition, or less elastic, inducing a positive substitution efect that softens the price competition. We find that when the recommendation strategy does not assign too large a weight on the retailer’s profit in deciding which product to recommend, the recommender system intensifies the price competition, and when the weight on the retailer’s profit is large, the recommender system softens the price competition.

The comparison of the equilibrium prices with and without the recommender system alludes to the direct influence and the strategic influence of the recommender system on pricing, which together contribute (b) Positive substitution effect and negative demand effect

Figure 1. Demand and Substitution Efects  
(a) Negative substitution effect and positive demand effect  
![](/api/attachments/GSCHNKVJ/fulltext/images/b1e691774f63fbe25dda9f7c37d73f3fa39a45529486c7e80a9d3a373718cd15.jpg)

to the substitution efect. First, the recommender system changes the informational diferentiation among consumers. The recommender system converts some partially informed shoppers to fully informed shoppers, and, simultaneously, converts uninformed shoppers to partially informed shoppers. This change in the informational diferentiation because of recommendation alters the elasticity of firms’ demand functions, which is the direct influence of the recommender system. Second, the recommender system’s strategic influence on manufacturers induces them to use price as a lever to increase the likelihood of their product being recommended, and this also alters the elasticity of demand functions. Whether the two influences together cause a positive or a negative substitution efect depends critically on the weight assigned to retailer’s profit. Corollary 1 reveals the sharp contrast between a consumer-oriented recommender system and a profit-oriented recommender system regarding how the recommender system afects the price competition.

Corollary 1. (a) When the recommender system is consumer oriented $( i . e .$ , if $w < 1 / \alpha )$ , each product’s price is lower in the presence of the recommender system than in its absence if and only if

$$
\begin{array}{c} \theta > \frac {\sqrt {(3 \theta_ {b} + 8 \mu t + 2 h) ^ {2} + 8 (4 \mu t + \theta_ {b}) (1 - \theta_ {b})} - 3 \theta_ {b} - 8 \mu t - 2 h}{4} \\ o r \quad \beta <   \frac {(1 - \theta - \theta_ {b}) (1 - \alpha w) (2 \theta + \theta_ {b} + 2 h)}{\theta_ {b} - (2 \theta + \theta_ {b}) (\theta + \theta_ {b}) + 4 \mu t (1 - 2 \theta - \theta_ {b}) - 2 \theta h}. \end{array}
$$

(b) When the recommender system is profit oriented $( i . e . ,$ $i f w > 1 / \alpha )$ , each product’s price is lower in the presence $o f$ the recommender system than in its absence if and only if

$$
\begin{array}{c} \theta > \frac {\sqrt {(3 \theta_ {b} + 8 \mu t + 2 h) ^ {2} + 8 (4 \mu t + \theta_ {b}) (1 - \theta_ {b})} - 3 \theta_ {b} - 8 \mu t - 2 h}{4} \\ a n d \quad \beta > \frac {(1 - \theta - \theta_ {b}) (1 - \alpha w) (2 \theta + \theta_ {b} + 2 h)}{\theta_ {b} - (2 \theta + \theta_ {b}) (\theta + \theta_ {b}) + 4 \mu t (1 - 2 \theta - \theta_ {b}) - 2 \theta h}. \end{array}
$$

![](/api/attachments/GSCHNKVJ/fulltext/images/8b91e2a2d43fd517508c84a1c7474fd07ec940157030d71f83f0d7b731cec7a1.jpg)

When the recommender system is consumer oriented, if the relative size of partially informed shoppers in the absence of recommender system is large (or, alternatively, the size of uninformed shoppers is small), the recommender system decreases the informational diferentiation because more shoppers are likely to be fully informed after the recommendation, which tends to increase the competition and decrease the price. Moreover, manufacturers have strategic incentives to lower the prices to increase the chance of recommendations for their products. Therefore, if $\theta$ is large (as prescribed in Corollary 1(a)), each product’s price is lower in the presence of the recommender system. If θ is small, the direct influence of recommender system tends to increase the informational diferentiation and soften the competition. On the other hand, the strategic influence still tends to increase the competition. If the strategic influence dominates the direct influence $( \mathrm { i . e . , }$ if the condition on $\beta ,$ as prescribed in Corollary 1(a), is satisfied), each product’s price is lower in the presence of the recommender system.

When the recommender system is profit oriented, the direct influence of the recommender system works in the same way as when the recommender system is consumer oriented: if the relative size of partially informed consumers in the absence of recommender system is large (small), the recommender system decreases (increases) the informational diferentiation, which tends to drive down (up) the price. However, in contrast to the case with the consumer-oriented recommender system, manufacturers have strategic incentives to increase the prices to increase the chance of recommendations for their products. Therefore, each product’s price is lower in the presence of the recommender system only if direct influence tends to drive down the price (i.e., if θ is large) and the strategic influence is mild (i.e., if $\beta$ is large).

Proposition 1(b) shows that the recommender system increases (decreases) the total demand when w is low (high). Two factors contribute to the recommender system’s impact on the demand. First, the recommender system increases shoppers’ awareness of at least one product, which increases the demand among shoppers. Second, the recommender system either increases or decreases the demand among loyal consumers depending on whether it decreases the price or increases the price as indicated in Proposition 1(a). Clearly, if the recommender system induces a decrease in price, then the demand for each product increases because demand from loyal consumers as well as shoppers increases; on the other hand, if the recommender system induces a price increase, then the demand increases only if the demand increase from shoppers ofsets the demand decrease from loyal consumers. We refer to the change in demands as the demand efect of the recommender system. In Figure 1, the change in the intercept of the demand functions with the vertical axis reflects the demand efect. Contrary to substitution efect, the demand efect tends to be positive (negative) when w is small (large).

Proposition 1(c) shows that the retailer and manufacturers do not necessarily benefit from the recommender system; whether the retailer and manufacturers benefit from the recommender system depends on the signs and magnitudes of the substitution efect and the demand efect. A positive (negative) demand efect and a positive (negative) substitution efect benefit (hurt) the retailer and manufacturers. Figure 2 illustrates the impacts of the recommender system on seller profits. The conditions stated in Proposition 1(c) show that the sellers benefit from the recommender system only when the weight assigned to the profit is neither too high nor too low. More importantly, as shown in Figure 2, neither a consumer-oriented recommender system nor a profit-oriented recommender system ensures that the sellers are better of with the recommender system than without. The following result illustrates the contrast between the consumeroriented recommender system and profit-oriented recommender system regarding the conditions that favor a higher seller profit with the recommender system.

Corollary 2. Let $w _ { 1 }$ and $w _ { 2 }$ be defined as in Equation (27).

(a) When the recommender system is consumer oriented (i.e., when $w < 1 / \alpha )$ , the retailer and manufacturers are worse of in the presence of the recommender system than in its absence $i f w < \operatorname* { m i n } \{ 1 / \alpha , w _ { 1 } \}$

(b) When the recommender system is profit oriented $( i . e . ,$ when $w > 1 / \alpha )$ , the retailer and manufacturers are worse of in the presence of the recommender system than in its absence $i f w > w _ { 2 }$

Corollary 2(a) shows that when the recommender system is consumer oriented, the sellers can be better of only when the recommender system is not highly consumer oriented. As seen in Proposition 1(a), a highly consumer-oriented recommender system intensifies the price competition. Even though the demand increases in this case, the increase in demand does not compensate the loss in profit margin. A similar observation applies when the recommender system is highly profit oriented. In this case, while the profit margin increases, the decline in demand from loyal consumers ofsets the gain from higher profit margin. We thus show that a profit-oriented system does not necessarily benefit the retailer, nor does a consumer-oriented system necessarily hurt the retailer.

Propositions 1(d) and 1(e) show that the recommendation strategy that assigns a very high weight to retailer profit hurts consumer surplus and social welfare. Intuitively, a low weight on retailer profit benefits consumers because in this case consumers benefit from lower prices, higher demand from both loyal consumers and shoppers, and lower misfit costs for shoppers in the presence of the recommender system. Analogously, the lower misfit costs for shoppers and higher demand from loyal consumers and shoppers benefit the social welfare when the recommender system uses a low weight on the retailer profit. Interestingly, we find that when the recommender system is very highly profit oriented (i.e., when $w > \mathrm { m a x } \{ w _ { 2 } , w _ { c s } , \dot { w } _ { w } \} )$ , all players in the marketplace—the retailer, manufacturers, consumers, and the society—are hurt by the recommender system.

Figure 2. Impact of the Recommender System on Profits $( \theta _ { b } = 0 . 2 , t = 0 . 3 , \alpha = 0 . 2 , \mu = 1 . 5 ,$ and h <sup></sup> 2.5)  
![](/api/attachments/GSCHNKVJ/fulltext/images/058d43613bae865ea8eb5e0a6c64a8839824d6e2aa8c887ea747e2360c28a841.jpg)

![](/api/attachments/GSCHNKVJ/fulltext/images/0ecd9707daa1429ce8fe34a41b3f44aee8fa4eec46b579ac3d03683cff90781d.jpg)

In summary, the analysis in this section reveals that when manufacturers strategically respond to retailer’s deployment of the recommender system, the impacts on sellers, consumers, and the society depend critically on the recommendation strategy, the recommender system precision, and consumers’ awareness about products. In the next section, we examine the roles of these factors on the recommender system impacts more closely.

## 5. Roles of the Recommender System and Market Characteristics

In our model, the recommender system is characterized by its precision (β) and recommendation strategy (w). The market characteristics is primarily captured by the proportion of partially informed consumers (θ) in the absence of the recommender system. In this section, we examine the roles of these parameters on the impacts of the recommender system. We denote the benefit from the recommender system to seller i by $\Delta \pi _ { i } = \pi _ { i } ^ { * } - \bar { \pi } _ { i } ^ { * } , i \in \{ A , B , R \}$ , the benefit to consumers by $\Delta C S \stackrel { \cdot } { = } C \dot { S } ^ { * } - \bar { C S } ^ { * }$ , the benefit to society by $\Delta W = W ^ { * } - \bar { W } ^ { * }$ , and the impact on price competition by $\Delta p _ { i } = { p } _ { i } ^ { * } - \bar { p } _ { i } ^ { * }$

We further note that since the benchmark is unaffected by recommender system parameters, the results regarding the roles of recommender system parameters can also be interpreted as how changes in these parameters afect the various players (i.e., manufacturers, the retailer, consumers, and the society) in the presence of the recommender system.

## 5.1. Role of Recommender System Precision

Proposition 2. When recommender system precision $\beta$ increases,

(a) the efect of the recommender system on softening price competition increases $( i . e . , \partial \triangle p _ { i } / \partial \dot { \beta } > 0 )$ if and only if the recommender system is consumer oriented;

(b) the efect of the recommender system on demand enhancement increases $( i . e . , \partial \triangle D _ { i } / \partial \beta > \mathsf { \bar { 0 } } )$ if and only if the recommender system is profit oriented;

(c) the benefit of the recommender system to a seller increases $( i . e . , \bar { \partial \triangle } \pi _ { i } ^ { \cdot } / \partial \beta > 0 )$ if and only if the recommender system is consumer oriented, or the recommender system is profit oriented and $w > 1 / \alpha + \beta ( \theta + \theta _ { b } ) / [ \alpha ( 1 - \theta - \theta _ { b } ) ] ;$

(d) the efect of the recommender system on consumer surplus decreases $( i . e . , \ \partial \triangle C S / \partial \beta < 0 \bar { ) }$ if and only if the recommender system is consumer oriented and $( { \bar { 2 h } } { \bar { + } } 1 ) ^ { 2 }$ $> [ ( 1 - \alpha w ) ( 1 - \theta - \theta _ { b } ) + \beta ( \theta + \theta _ { b } + 4 \mu t ) ] ^ { 3 } / ( 4 ( 1 - \alpha w ) \cdot$ $[ ( 1 - \alpha w ) ( 1 - \theta - \theta _ { b } ) + \beta ( \dot { \theta } + \theta _ { b } + 2 \mu t ) ] ) ;$

(e) the efect of the recommender system on social welfare decreases $( i . e . , \partial \triangle W / \partial \beta < 0 )$ if and only $i f 8 ( 1 + 2 h ) ( 1 -$ $\alpha w ) [ 3 \beta \mu t - h ( 1 - \alpha w ) ( 1 - \theta - \theta _ { b } ) - \beta \bar { h } ( \theta + \theta _ { b } - 2 \mu t ) ] >$ $[ ( 1 - \dot { \alpha } \dot { w } ) ( 1 - \theta - \theta _ { b } ) + \beta ( \theta + \theta _ { b } + 4 \mu t ) ] ^ { 3 }$

Propositions $2 ( \mathsf { a } ) \mathsf { - } 2 ( \mathsf { c } )$ reveal that the impact of $\beta$ on sellers is diferent under diferent recommendation strategies. If the recommender system is consumer oriented or highly profit oriented $( w > 1 / \alpha + \beta ( \theta +$ $\theta _ { b } ) / [ \alpha ( 1 - \theta - \mathsf { \bar { \theta } } _ { b } ) ] )$ , the sellers benefit from improving the recommender system’s precision. Under these conditions, in particular, if the recommender system benefits the sellers, an improvement in $\beta$ enhances the benefit, and if the recommender system hurts the sellers, an improvement in $\beta$ mitigates this negative impact. If the recommender system is mildly profit oriented, the sellers are hurt from improving the recommender system’s precision. The recommender system precision afects the seller profits via its impact on the demand efect (Proposition 2(b)) and substitution efect (Proposition 2(a)).

We note from Equation (23) that an improvement in precision does not alter the direct influence but alters the strategic influence of the recommender system. When the recommender system is consumer (profit) oriented, the strategic influence represented by K in Equation (23) increases (decreases) in $\beta .$ The intuition is as follows. Under a consumer-oriented (profit-oriented) recommender system, a decrease (an increase) in the price of a product, ceteris paribus, increases the likelihood of that product being recommended. However, the marginal increase in this likelihood is greater when the recommender system precision is low than when that precision is high. When the precision is low, the recommender system cannot estimate consumer preference well and highly relies on prices to recommend product because the recommender system perceives most consumers as being concentrated in the middle of the Hotelling line. As a result, a small decrease (increase) in the price of a product induces recommendation of that product to a large number of consumers if the recommender system is consumer (profit) oriented. On the other hand, when the precision is high, from the recommender system’s perspective, the consumers are spread more evenly throughout the line; therefore, a decrease (increase) in price leads to recommendation of that product to a smaller number of consumers if the recommender system is consumer (profit) oriented. Consequently, when the recommender system is consumer (profit) oriented, an increase in precision reduces manufacturers’ incentive to decrease (increase) price, which softens (intensifies) price competition. On the other hand, the softening (intensification) of the price competition by an improvement in precision reduces (increases) the demand when the recommender system is consumer (profit) oriented. The net impact of recommender system precision is that sellers benefit only when the recommender system is consumer oriented or highly profit oriented.

An improvement in recommender system precision enhances the benefit or mitigates the hurt to consumers if the recommender system is profit oriented. On the other hand, if the recommender system is consumer oriented, an improvement in precision exacerbates the hurt or diminishes the benefit to consumers when the market potential of loyal consumers is large compared to the number of shoppers. We note that the recommender system can benefit consumers in three ways: demand enhancement, intensification of price competition, and reduction in misfit costs. An improvement in precision always reduces the misfit costs, whether the recommender system is consumer oriented or profit oriented. If the recommender system is profit oriented, since an improvement in precision intensifies the price competition (Proposition 2(a)) and enhances the demand, consumers end up benefiting from it. On the other hand, if the recommender system is consumer oriented, the adverse impacts of precision on demand and price competition ofset the beneficial impact on the misfit costs if the market potential of loyal consumers is large relative to the number of shoppers who are the ones that benefit from a reduction in misfit costs because of the recommender system. The impact of precision on social welfare is analogous to that on consumer surplus except that only the impacts on the demand and misfit costs play roles.

## 5.2. Role of Recommendation Strategy

Proposition 3. When the weight assigned to the retailer profit component of recommendation score w increases,

(a) the efect of the recommender system on softening price competition increases $( i . e . , \partial \triangle p _ { i } / \bar { \partial } w > 0 )$ ;

(b) the efect of the recommender system on increasing demand decreases $( i . e . , \partial \triangle D _ { i } / \partial w < 0 )$ ;

(c) the benefit of the recommender system to seller increases $( i . e . , \partial \triangle \pi _ { i } / \partial w > 0 )$ if and only $i f \dot { w } { < } 1 / \alpha + \beta ( \theta + \theta _ { b } ) /$ $[ \alpha ( 1 - \theta - \theta _ { b } ) ] ;$

(d) the benefit of the recommender system on consumer surplus decreases $( \dot { i } . e . , \partial \triangle C S / ( \partial w < 0 ) )$ 41

(e) the benefit of the recommender system on social welfare decreases $\dot { ( } i . e . , \dot { \partial } \triangle W / \partial w < 0 )$ if and only $i f w > 1 / \alpha +$ $\mathring { \beta } ( \theta + \theta _ { b } ) / [ \alpha ( 1 - \theta - \theta _ { b } ) ] - \beta ( 3 + \mathring { 2 } h ) \mu t / [ \alpha \dot { h } ( 1 - \theta - \theta _ { b } ) ]$

Similar to recommender system precision, the recommendation strategy does not afect the direct influence of the recommender system on price competition.

Meanwhile, as w increases, the strategic influence of recommender system increases—manufacturers have greater incentives to increase their prices to increase the number of recommendations in their favor. As a result, the equilibrium price increases, which explains Proposition 3(a). However, as the price goes up, fewer loyal consumers will purchase in the presence of recommender system. Consequently, when w exceeds a threshold, the demand decreasing efect dominates the price increasing efect, and thus an increase in w hurts the retailer’s profit. Proposition 3(c) implies that there exist an optimal w that maximizes retailer profit, and we explore the characteristics of this optimal recommendation strategy in Section 6. Furthermore, the adverse impact of w from consumer perspective, both in terms of softening of price competition and demand reduction, hurts consumer surplus, and a demand reduction caused by an increase in w hurts social welfare.

5.3. Role of the Size of Partially Informed Shoppers Proposition 4. When the proportion of partially informed consumers θ increases,

(a) the efect of the recommender system on softening price competition increases $( i . e . , \partial \triangle p _ { i } / \partial \theta > 0 )$ if and only $i f w < ( 1 - \beta ) / \alpha ~ a n d ~ \theta > ( 1 - \alpha w + 4 \beta \mu t ) / ( 1 - \alpha w - \beta ) -$ $\sqrt { \beta ( 1 + 2 h ) ( \theta _ { b } + 4 \mu t ) / [ 2 ( 1 - \alpha w - \beta ) ] } - \theta _ { b } ;$

(b) the efect of the recommender system on increasing demand increases $( i . e . , \ \partial \triangle D _ { i } / \partial \theta > 0 )$ if and only if $w > ( 1 - \beta ) / \alpha$ and $\theta < ( 1 - \alpha w + 4 \beta \mu t ) / ( 1 - \alpha w - \beta ) +$ $\sqrt { \beta \mu t ( 1 + 2 h ) ( \theta _ { b } + 4 \mu t ) / [ ( \theta _ { b } + 2 \mu t ) ( \alpha w + \beta - 1 ) ] } - \theta _ { b } ;$

(c) the benefit of recommender system to sellers (i.e., $\partial \triangle \pi _ { i } / \partial \theta > 0 )$ increases if and only $i f \ ( 1 - \alpha w \ - \beta )$ $[ ( 1 - \alpha w ) ( 1 - \theta - \theta _ { b } ) + \beta ( \dot { \theta } + \theta _ { b } ) ] > \dot { 0 }$ and

$$
\begin{array}{l} \frac {(1 + 2 h) ^ {2}}{(2 \theta + \theta_ {b} + 2 h)} \\ > \frac {4 (2 \mu t + \theta_ {b}) [ (1 - \alpha w) (1 - \theta - \theta_ {b}) + \beta (\theta + \theta_ {b}) + 4 \beta \mu t ] ^ {3}}{\beta (4 \mu t + \theta_ {b}) ^ {2} (1 - \alpha w - \beta) [ (1 - \alpha w) (1 - \theta - \theta_ {b}) + \beta (\theta + \theta_ {b}) ]}; \end{array}
$$

(d) the benefit of recommender system to consumers increases $( i . e . , \partial \triangle C S / \partial \theta > 0 )$ if and only if

$$
\begin{array}{r l} & 2 v - \frac {5 - \beta}{4} t <   4 t \frac {(2 \theta + \theta_ {b} + 2 h) (\theta_ {b} + 3 \mu t)}{(4 \mu t + \theta_ {b}) ^ {2}} - \beta t (1 + 2 h) ^ {2} \\ & \quad \cdot (1 - \alpha w - \beta) \frac {(1 - \alpha w) (1 - \theta - \theta_ {b}) + \beta (\theta + \theta_ {b}) + 2 \beta \mu t}{[ (1 - \alpha w) (1 - \theta - \theta_ {b}) + \beta (\theta + \theta_ {b}) + 4 \beta \mu t ] ^ {3}}; \end{array}
$$

(e) the benefit of recommender system to social welfare decreases $( i . e . , \partial \triangle W / \partial \theta > 0 ) i f$

$$
\begin{array}{l} 2 v - \frac {5 - \beta}{4} t <   4 t \frac {(6 \theta + 3 \theta_ {b} + 2 h) \mu t - \theta_ {b} h}{(4 \mu t + \theta_ {b}) ^ {2}} + 2 \beta t (1 + 2 h) \\ \cdot (1 - \alpha w - \beta) \frac {(3 + 2 h) \beta \mu t - h (1 - \alpha w) (1 - \theta - \theta_ {b}) + \beta h (\theta + \theta_ {b})}{[ (1 - \alpha w) (1 - \theta - \theta_ {b}) + \beta (\theta + \theta_ {b}) + 4 \beta \mu t ] ^ {3}}. \end{array}
$$

An increase in θ moderates the substitution efect by afecting both the direct influence and the strategic influence of the recommender system. When θ increases, on the one hand, informational diferentiation among shoppers without the recommender system $( \mathrm { i . e . , ~ } \bar { \theta } / \theta _ { b } )$ increases and the informational differentiation among shoppers with the recommender system (i.e., $( 1 - \breve { \theta } - \theta _ { b } ) \dot { / } [ 2 ( \theta + \theta _ { b } ) ] )$ decreases, and, hence, the direct influence of the recommender system on softening competition decreases. On the other side, with a larger $\theta ,$ fewer uninformed consumers are influenced through recommendations (which in turn are influenced by price), and more partially informed consumers might become fully informed because of recommendations. As a result, manufacturers have less incentive to use price as a lever to attract recommendations. In particular, an increase in θ increases (decreases) the strategic influence of the recommender system on softening competition under a consumer-oriented (profit-oriented) recommender system. Together, as stated in Proposition 4, an increase in θ reduces the substitution efect on softening price competition when $w > ( 1 - \beta ) / \alpha$ . When $w < ( 1 - \beta ) / \alpha ,$ an increase in θ can either enhance or diminish the efect. In particular, if the consumer orientation is not too high, the result obtained for a profit-oriented recommender system still applies. The strategic influence dominates the direct influence if the value of θ is big enough, and thus an increase in θ increases the efect of the recommender system on softening price competition, as prescribed by the conditions in Proposition 4(a).

An increase in θ reduces the demand gain from shoppers, but may increase or decrease the demand gain from loyal consumers depending on the substitution efect. The efect on the benefit to the sellers can be positive only if a decrease in the demand efect is dominated by an increase in the substitution efect or an increase in the demand efect dominates a decrease in the substitution efect, which requires the conditions stated in Proposition 4(c). The reduction in demand from shoppers also has a negative efect on consumers, but the change in the substitution efect might be in favor of consumers. Proposition 4(d) characterizes the condition—when the reduction in consumer utility $( \mathrm { i . e . , } 2 v - ( 5 - \beta ) t / 4 )$ is not too high—under which the benefit of the recommender system increases when θ increases.

In summary, the analysis in this section characterizes how the recommender system and market characteristics afect the magnitudes of the recommender system impacts. First, an improvement in precision softens the price competition and increases the sellers’ benefit from the recommender system when the system is consumer oriented; however, when the recommender system is profit oriented, an increase in precision intensifies the price competition and decreases the sellers’ benefit from the recommender system if the profit orientation is not too high. Second, an increase in the relative weight assigned to retailer profit vis-a-vis consumer value in computing the recommendation score always softens the price competition, but decreases sellers’ benefit from the recommender system if the profit orientation is excessive. Third, an increase in the size of partially informed consumers decreases the sellers’ benefit from the recommender system when the system is highly consumer oriented or when the system is mildly profit oriented. These results indicate that it is critical for the retailer to choose an optimal recommendation strategy that accounts for recommender system precision and market characteristics. In the next section, we examine the optimal recommendation strategy from the retailer’s perspective.

## 6. Retailer’s Optimal

## Recommendation Strategy

The results of the previous sections demonstrate that the recommendation strategy employed by the retailer, among other factors, determines whether the recommender system benefits the retailer. In practice, a retailer might not employ a recommendation strategy that hurts it. In this section, we endogenize the recommendation strategy by allowing the retailer to choose w that maximizes its profit in the presence of the recommender system given by Equation (20).

Proposition 5. The optimal weighting factor assigned to retailer profit is

$$
w ^ {*} = \frac {\beta (\theta + \theta_ {b}) + (1 - \theta - \theta_ {b})}{\alpha (1 - \theta - \theta_ {b})},\tag{30}
$$

which increases in $\beta$ and $\theta + \theta _ { b }$

Two observations are worth highlighting. First, we notice that $w ^ { * } > 1 / \alpha ,$ which means that the retailer will choose a profit-oriented recommender system. Meanwhile, the retailer does not prefer a recommender system with too large of a profit orientation. A high profit orientation provides excessive incentives to manufacturers to increase their prices, which hurts the retailer by decreasing the demand. Therefore, it is in the best interest of the retailer to limit w. On the other hand, a low w may provide manufacturers incentives to engage in excessive price competition, which also hurts the retailer.

Second, the extent of profit orientation $( \mathrm { i } . \mathrm { e } . , \ w ^ { * } - $ $1 / \alpha )$ in the optimal recommendation strategy depends on the recommender system precision as well as the market characteristics captured by $\theta + \theta _ { b }$ . Surprisingly, the retailer chooses a more profit-oriented recommender system if the precision is higher. On the one hand, an improvement in precision induces the manufacturers to decrease prices if the recommender system is profit oriented, as seen from Proposition $2 ( \mathsf { a } )$ . On the other hand, an increase in w induces manufacturers to increase prices, as observed from Proposition 3(a). Consequently, the optimal w increases in recommender system precision in balancing these two factors in changing price. A similar reasoning applies for the result that $w ^ { * }$ increases in $\theta + \theta _ { b }$

By substituting the optimal weighting factor w<sup>∗</sup> into the results in Lemma $^ { 2 , }$ we can derive the equilibrium prices, demands, manufacturer profits, retailer profit, consumer surplus, and social welfare. We can now assert the impact of the optimal recommender system by comparing equilibrium quantities in the scenario without the recommender system and the scenario with the optimal recommender system.

Proposition 6. Compared to the scenario without the recommender system, in the presence of the recommender system with the optimal recommendation strategy,

(a) each product’s price is higher $( i . e . , p _ { i } ^ { * } > \bar { p } _ { i } ^ { * } ) .$

(b) each product’s demand is higher $( i . e . , D _ { i } ^ { * } > \bar { D } _ { i } ^ { * } )$ if and only $i f h < ( 1 - 2 \theta - \theta _ { b } ) ( \theta _ { b } + 2 \mu t ) / \theta _ { b } - 1 / 2 ;$

(c) the retailer and manufacturers are better of $( i . e . ,$ $\pi _ { i } ^ { * } > \bar { \pi } _ { i } ^ { * } )$ ;

(d) consumer’s surplus increases if and only if

$$
\begin{array}{l} \beta > [ (1 + 2 h) \theta_ {b} + 4 \mu t (1 - 2 \theta - \theta_ {b}) ] \\ \quad \cdot [ (2 h + 2 \theta + \theta_ {b}) \theta_ {b} + (4 \mu t + \theta_ {b}) (4 h + 6 \theta + 3 \theta_ {b} - 1) ] \\ \quad \cdot [ 4 \mu t (\theta_ {b} + 4 \mu t) ^ {2} (1 - \theta - \theta_ {b}) ] ^ {- 1} \\ \quad - \frac {(4 v - 2 t - (1 + 2 h) / \mu) (1 - 2 \theta - \theta_ {b})}{t (1 - \theta - \theta_ {b})} - \frac {\theta}{1 - \theta - \theta_ {b}}; \end{array}
$$

(e) social welfare increases if and only if

$$
\begin{array}{r l} & {\beta > [ (1 + 2 h) \theta_ {b} + 4 \mu t (1 - 2 \theta - \theta_ {b}) ]} \\ & {\qquad \cdot [ (3 - 2 h) \theta_ {b} + 4 \mu t (4 h + 6 \theta + 3 \theta_ {b} + 3) ]} \\ & {\qquad \cdot [ 4 \mu t (\theta_ {b} + 4 \mu t) ^ {2} (1 - \theta - \theta_ {b}) ] ^ {- 1}} \\ & {\qquad - \frac {2 (2 v - t) (1 - 2 \theta - \theta_ {b})}{t (1 - \theta - \theta_ {b})} - \frac {\theta}{1 - \theta - \theta_ {b}}.} \end{array}
$$

We find that the optimal recommendation strategy relaxes the price competition between manufacturers and benefits the retailer and manufacturers, compared to the case without recommendation. However, the optimal recommender strategy does not necessarily increase the demand. More importantly, we find that both consumer surplus and social welfare are higher under the optimal recommendation strategy than under the benchmark if the recommender system precision is high. This result is especially noteworthy because it shows that if the retailer deploys the optimal recommendation strategy that maximizes its own profit, every player in the market place—retailer, manufacturers, consumers, and the society—is better of in the presence of the recommender system than in its absence if the recommender system precision is higher than a threshold value. This is in contrast to the result that when the recommendation strategy is not optimal, all players can actually be worse of, as seen in the discussion following Corollary 2.

## 7. Discussion and Conclusions

We examine the efect of recommender systems in a channel structure with a retail platform and two competing manufacturers selling substitute products. Manufacturers set the prices for their products, and the retail platform takes a fraction of the sales price as a commission for each transaction. The recommendations have an informative role and increase the consumer awareness of products. The retail platform recommends the product based on a predetermined strategy: the platform assigns a weight on the retailer profit factor and a weight on the consumer value factor. We identify two efects of recommender system: demand efect and substitution efect. The demand efect of the recommender system increases the proportion of consumers that are aware of at least one of the products and alters the overall market size. The substitution efect of the recommender system changes the price competition between two manufacturers. The recommender system may benefit or hurt the retailer and the manufacturers depending on the relative magnitudes of these two efects of the recommender system. We find that the retail platform and the manufacturers do not always benefit from the recommender system. The benefit of a recommender system depends critically on the type of recommender system employed (profit oriented or consumer oriented), the recommender system precision, and consumers’ awareness about products. We find that the optimal recommendation strategy for the retailer is mildly profit oriented, and under this optimal recommendation strategy, the retailer and manufacturers always benefit from the recommender system but the consumers and the society may not.

The findings have several implications for electronic marketplaces that deploy recommender systems. First, our study pinpoints the possible negative efect of recommender systems even if they are cost free, which calls for marketplace managers’ attention. Sensibly, recommender systems can hurt the retailer platform that implements the recommender system, when they focus solely on the additional sales or demand created by them and ignore strategic price responses from manufacturers who sell in the marketplace. Furthermore, even though taking into account of manufacturers’ strategic interaction, recommender systems can also hurt the retailer platform when they are oriented too much toward the retailer’s profit or consumer value in determining which product to recommend. When the cost of developing recommender systems is also accounted for, the value of these systems diminishes further.

Second, we identify various factors, such as the recommendation strategy, recommender system precision, and relative sizes of segments of consumers with diferent awareness levels, that determine whether the retailer benefits from the recommender system, and characterize how these factors afect the benefit. In particular, our study reveals that improvement in recommender system precision benefits the retailer only when the system is consumer oriented or when the system is highly profit oriented; when the recommender system is mildly profit oriented, improvement in recommender system hurts the retailer, even if it is cost free.

Third, we underscore the efects of diferent types of recommender systems: a consumer-oriented recommender system does not always hurt the sellers, nor does a profit-oriented recommender system always benefit the sellers. We prescribe the optimal recommender system that maximizes the retailer’s profit to be the one that is mildly profit oriented in the sense that it assigns a larger but not too large a weight to retailer profit compared to consumer value. The retailer should adopt a more profit-oriented recommendation strategy with an increase in either the recommender system precision or the fraction of consumers that are aware of at least one product.

Finally, when the retailer deploys a recommendation strategy that maximizes its own benefit, the consumers and the society may also benefit from the recommender system if it has a high precision. Consequently, it may be in the best interest of consumers to reveal their preferences to the retailer, and social planners should facilitate the revelation of consumer preference information to retailers.

This study can be further extended in several directions. One particularly interesting extension relates to the empirical validation of the hypotheses alluded to by the implications we listed previously. This being a theoretical study, it is limited to developing insights regarding the impacts of recommender systems. Clearly, an empirical validation of the insights is valuable and critical. However, we would also point out that an empirical study is challenging because data about specific recommendation strategies used by retailers are generally private information that is dificult, if not impossible, to obtain. On the theoretical side, future research could further examine the economic impact of recommender systems in other contexts or manners in which recommender systems are employed. For instance, recommender systems vary in terms of when recommendations are presented to the user and the role they play (whether informative or persuasive). As a first study to examine the upstream impact of recommender systems, we have analyzed a specific context in this paper using a stylized model of two firms. Future research could extend this study by changing any of the aforementioned dimensions to enrich our understanding of recommender systems economic impact.

## Acknowledgments

The authors thank the review team for detailed and constructive comments that greatly improved this paper. They also thank participants at the 2014 Workshop on Information Systems and Economics and seminar participants at Dalian University of Technology and the University of Texas at Dallas for their helpful feedback.

## Appendix. Proofs

## Proof of Conditional Expectation of Misfit

The cumulative density function of s, conditional on the consumer’s true location λ being z, can be formulated as

$$
P (s \leqslant y \mid \lambda = z) = (1 - \beta) y + \beta H (y - z),\tag{A.1}
$$

where $H ( \cdot )$ is the Heaviside step function that evaluates to zero if the argument is negative and to one otherwise. The corresponding probability density function is

$$
P (s = y \mid \lambda = z) = (1 - \beta) + \beta \delta (y - z),\tag{A.2}
$$

where δ<sup>(</sup>x<sup>)</sup> is the Dirac delta distribution that satisfies $\textstyle \int _ { - \infty } ^ { \infty } \delta ( x ) d x = 1$ and $\delta ( x ) = 0 { \mathrm { i f ~ } } x \neq 0 .$ , and δ<sup>(</sup>x<sup>)  ∞</sup> if x <sup></sup> 0.

Using the Bayes Law,

$$
P (\lambda = z \mid s = y) = \frac {P (s = y \mid \lambda = z) P (\lambda = z)}{P (s = y)} = (1 - \beta) + \beta \delta (y - z),\tag{A.3}
$$

and the conditional expectation is

$$
\mathbb {E} (\lambda = z \mid s = y) = \frac {1 - \beta}{2} + \beta y.\tag{A.4}
$$

Proof of Lemma 1

(a) Each manufacturer’s best response to its competitor in Stage 1 is characterized by the first-order conditions of Equation (6):

$$
\begin{array}{r l} & {\frac {\partial \pi_ {A}}{\partial p _ {A}} = (1 - \alpha) \Bigg (\theta + \frac {p _ {B} - 2 p _ {A} + t}{2 t} \theta_ {b} + h - 2 \mu p _ {A} \Bigg) = 0;} \\ & {\frac {\partial \pi_ {B}}{\partial p _ {B}} = (1 - \alpha) \Bigg (\theta + \frac {p _ {A} - 2 p _ {B} + t}{2 t} \theta_ {b} + h - 2 \mu p _ {B} \Bigg) = 0.} \end{array}
$$

Based on these equations, we can derive the manufacturer equilibrium prices as in Equation (7).

(b) Substituting the equilibrium prices into Equation (5), we can derive the equilibrium demands as in Equation (8).

(c) Substituting the equilibrium prices into Equation (6), we can derive the equilibrium profits as in Equation (9). Assumption 1 guarantees that some loyal consumers will purchase in the equilibrium, and Assumption 2 guarantees that the shopper with the largest misfit cost has incentive to purchase if she is aware of the product.

(d) According to the commission scheme, we have $\pi _ { R } / ( \pi _ { A } + \pi _ { B } ) = \alpha / ( 1 - \alpha )$ . Based on $\pi _ { i } ^ { * } ,$ we can derive $\pi _ { R } ^ { * }$ as in Equation (10).

(e) The consumer surplus from the loyal consumers is

$$
\bar {C S} _ {L} = 2 \gamma \int_ {0} ^ {(v _ {L} - \bar {p} ^ {*}) / t _ {L}} (v _ {L} - \bar {p} ^ {*} - z t _ {L}) d z = \gamma \frac {(v _ {L} - \bar {p} ^ {*}) ^ {2}}{t _ {L}}.\tag{A.5}
$$

Next we derive the consumer surplus for shoppers. The consumer surplus from each partially informed segment is

$$
\bar {C S} _ {S} ^ {p} = \theta \int_ {0} ^ {1} (v - \bar {p} ^ {*} - z t) d z = \theta \left(v - \bar {p} ^ {*} - \frac {t}{2}\right),\tag{A.6}
$$

and that from the fully informed segment is

$$
\begin{array}{l} \bar {C S} _ {S} ^ {f} = \theta_ {b} \left[ \int_ {0} ^ {1 / 2} (v - \bar {p} ^ {*} - z t) d z + \int_ {1 / 2} ^ {1} [ v - \bar {p} ^ {*} - (1 - z) t ] d z \right] \\ = \theta_ {b} \left(v - \bar {p} ^ {*} - \frac {t}{4}\right). \end{array} \tag {A.}\tag{A.7}
$$

The consumer surplus from the uninformed segment is zero. Aggregating the consumer surplus from the loyal consumers, the two partially informed shopper segments, and one fully informed shopper segment, we have

$$
\begin{array}{l} \bar {C S} = \bar {C S} _ {L} + \bar {C S} _ {S} ^ {p} + \bar {C S} _ {S} ^ {f} \\ \qquad = \gamma \frac {(v _ {L} - \bar {p} ^ {*}) ^ {2}}{t _ {L}} + (2 \theta + \theta_ {b}) (v - \bar {p} ^ {*}) - t \left(\theta + \frac {\theta_ {b}}{4}\right). \end{array}\tag{A.8}
$$

Substituting p¯ in Equation (7), we derive the total surplus as in Equation (11).

(f) Social welfare is the sum of the consumer surplus, manufacturer’s profits, and retailer’s profit; that is, $\bar { \boldsymbol { W } } = \bar { \boldsymbol { C } } \bar { \boldsymbol { S } } +$ $\bar { \pi } _ { A } ^ { * } + \bar { \pi } _ { B } ^ { * } + \bar { \pi } _ { R } ^ { * } ,$ which can be derived as in Equation (12).

## Proof of Lemma 2

The manufacturers maximize their profits by choosing their optimal prices; that is,

$$
\max _ {p _ {i}} \pi_ {i} = (1 - \alpha) p _ {i} (D _ {i L} + D _ {i S}),\tag{A.9}
$$

where $D _ { i L }$ is defined as in Equation (1), and $D _ { i S }$ is defined as in Equation (16).

(a) Each manufacturer’s best response to its competitor in Stage 1 is characterized by the first-order conditions of Equation (A.9)

$$
\begin{array}{c} \frac {\partial \pi_ {A}}{\partial p _ {A}} = (1 - \alpha) \bigg [ \frac {1}{2} + \frac {\beta (\theta + \theta_ {b}) + (1 - \theta - \theta_ {b}) (1 - \alpha w)}{2 \beta t} \\ \qquad \cdot (p _ {B} - 2 p _ {A}) + h - 2 \mu p _ {A} \bigg ] = 0; \\ \frac {\partial \pi_ {B}}{\partial p _ {B}} = (1 - \alpha) \bigg [ \frac {1}{2} + \frac {\beta (\theta + \theta_ {b}) + (1 - \theta - \theta_ {b}) (1 - \alpha w)}{2 \beta t} \\ \qquad \cdot (p _ {A} - 2 p _ {B}) + h - 2 \mu p _ {B} \bigg ] = 0. \end{array}
$$

Based on these equations, we can derive the manufacturer equilibrium prices as in Equation (17).

We next check the second-order derivatives,

$$
\begin{array}{r} \frac {\partial^ {2} \pi_ {A}}{\partial p _ {A} ^ {2}} = - (1 - \alpha) \frac {\beta (\theta + \theta_ {b}) + (1 - \theta - \theta_ {b}) (1 - \alpha w) + 2 \beta \mu t}{\beta t}, \\ \frac {\partial^ {2} \pi_ {B}}{\partial p _ {B} ^ {2}} = - (1 - \alpha) \frac {\beta (\theta + \theta_ {b}) + (1 - \theta - \theta_ {b}) (1 - \alpha w) + 2 \beta \mu t}{\beta t}. \end{array}
$$

Assumption 3 guarantees that the profit function is concave and the maximization problem is well behaved.

(b) Part (b) follows by substituting the equilibrium prices into Equations (1) and (16).

(c) Part (c) follows by substituting the equilibrium prices into Equation (A.9). Assumption 1 guarantees that some loyal consumers will purchase in the equilibrium, and Assumption 2 guarantees that the shopper with the largest misfit cost has incentive to purchase if she is aware of the product.

(d) According to the commission scheme, we have $\pi _ { R } / ( \pi _ { A } + \pi _ { B } ) = \alpha / ( 1 - \alpha )$ <sup>)</sup>. Based on $\pi _ { i } ^ { * } ,$ we can derive $\pi _ { R } ^ { * }$ as in Equation (20)

(e) The consumer surplus from the loyal consumers for manufacturer i is similar to that Equation (A.5); that is, $C S _ { L } =$ $\gamma ( { v _ { L } } - { p ^ { * } } ) ^ { 2 } / t _ { L }$

The consumer surplus from each partially informed segment of shoppers is

$$
\begin{array}{l} C S _ {S} ^ {p} = \theta \left[ \int_ {0} ^ {1 / 2} (v - p ^ {*} - z t) d z + \frac {1 - \beta}{2} \int_ {1 / 2} ^ {1} (v - z t - p ^ {*}) d z \right. \\ \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad + \frac {1 + \beta}{2} \int_ {1 / 2} ^ {1} [ v - (1 - z) t - p ^ {*} ] d z \Bigg ] \\ \qquad \qquad \qquad = \theta \left[ v - p ^ {*} - \frac {t}{2} + \frac {(1 + \beta) t}{8} \right]. \end{array}
$$

The consumer surplus from the fully informed segment of shoppers is

$$
\begin{array}{l} C S _ {S} ^ {f} = \theta_ {b} \left[ \int_ {0} ^ {1 / 2} (v - p ^ {*} - z t) d z + \int_ {1 / 2} ^ {1} [ v - p ^ {*} - (1 - z) t ] d z \right] \\ = \theta_ {b} \left(v - p ^ {*} - \frac {t}{4}\right). \end{array}
$$

The consumer surplus from the uninformed segment of shoppers is

$$
\begin{array}{l} C S _ {S} ^ {u} = 2 (1 - 2 \theta - \theta_ {b}) \bigg [ \frac {1 + \beta}{2} \int_ {0} ^ {1 / 2} (v - p ^ {*} - z t) d z \\ \qquad \qquad + \frac {1 - \beta}{2} \int_ {0} ^ {1 / 2} [ v - p ^ {*} - (1 - z) t ] d z \bigg ] \\ \qquad = (1 - 2 \theta - \theta_ {b}) \bigg [ v - p ^ {*} - \frac {t}{4} - \frac {(1 - \beta) t}{4} \bigg ]. \end{array}
$$

Aggregating the consumer surplus from the loyal consumers and the shoppers, we can derive the total surplus as follows:

$$
\begin{array}{r l} & C S = C S _ {L} + C S _ {S} ^ {p} + C S _ {S} ^ {f} \\ & \qquad = v - \frac {t}{4} [ 1 + (1 - \beta) (1 - \theta - \theta_ {b}) ] - p ^ {*} + \gamma \frac {(v _ {L} - p ^ {*}) ^ {2}}{t _ {L}}. \end{array}\tag{A.10}
$$

By substituting the equilibrium price $p ^ { * }$ in Equation (17), we derive the total surplus as in Equation (21).

(f) Social welfare is the sum of the consumer surplus, manufacturer’s profits, and retailer’s profit; that ${ \mathrm { i s , ~ } } W = C S +$ $\pi _ { A } ^ { * } + \pi _ { B } ^ { * } + \pi _ { R } ^ { * } ,$ which can be derived as in Equation (22).

## Proof of Proposition 1

(a) For ease of exposition, we denote ${ \cal M } \equiv ( 1 - \alpha w ) ( 1 -$ $\theta - \theta _ { b } ) + \beta ( \theta + \theta _ { b } ) \bar { + } 4 \beta \mu t .$ . Note that

$$
\begin{array}{r l} p _ {i} ^ {*} - \bar {p} _ {i} ^ {*} = & t \big (\beta (1 - 2 \theta - \theta_ {b}) (\theta_ {b} + 4 \mu t) - \beta \theta (2 \theta + \theta_ {b} + 2 h) \\ & - (1 - \alpha w) (1 - \theta - \theta_ {b}) (2 \theta + \theta_ {b} + 2 h) \big) \cdot (M (\theta_ {b} + 4 \mu t)) ^ {- 1}. \end{array}
$$

Therefore, $p _ { i } ^ { * }$ is less than $\bar { p } _ { i } ^ { * }$ if the numerator is negative, which leads to the condition in part (a).

(b) Note that

$$
\begin{array}{r l} D _ {i} ^ {*} - \bar {D} _ {i} ^ {*} = & \big ([ (1 - \alpha w) (1 - \theta - \theta_ {b}) + \beta \theta ] [ (1 - 2 \theta - \theta_ {b}) (\theta_ {b} + 2 \mu t) \\ & + 2 \mu t (1 + 2 h) ] + \beta (1 - 2 \theta - \theta_ {b}) (\theta_ {b} + 4 \mu t) (\theta_ {b} + 2 \mu t) \big) \\ & \cdot (2 M (\theta_ {b} + 4 \mu t)) ^ {- 1}. \end{array}
$$

Therefore, $D _ { i } ^ { * }$ is less than $\bar { D } _ { i } ^ { * }$ if the numerator is positive, which leads to the condition in part (b).

(c) Note that

$$
\begin{array}{r} \pi_ {i} ^ {*} - \bar {\pi} _ {i} ^ {*} = - (1 - \alpha) \frac {t}{M ^ {2}} \left[ \left(\frac {2 \theta + \theta_ {b} + 2 h}{\theta_ {b} + 4 \mu t}\right) ^ {2} \left(\frac {\theta_ {b}}{2} + \mu t\right) M ^ {2} \right. \\ \left. - (1 + 2 h) ^ {2} \frac {\beta}{2} M + (1 + 2 h) ^ {2} \beta^ {2} \mu t \right]. \end{array}
$$

Therefore, $\pi _ { i } ^ { * } - \bar { \pi } _ { i } ^ { * } > 0$ when

$$
\left(\frac {2 \theta + \theta_ {b} + 2 h}{\theta_ {b} + 4 \mu t}\right) ^ {2} \left(\frac {\theta_ {b}}{2} + \mu t\right) M ^ {2} - (1 + 2 h) ^ {2} \frac {\beta}{2} M + (1 + 2 h) ^ {2} \beta^ {2} \mu t <   0.
$$

Because $[ ( 1 + 2 h ) ^ { 2 } ( \beta / 2 ) ] ^ { 2 } - 4 ( ( 2 \theta + \theta _ { b } + 2 h ) / ( \theta _ { b } + 4 \mu t ) ) ^ { 2 }$ $( \theta _ { b } / 2 + \mu t ) ( 1 + 2 h ) ^ { 2 } \dot { \beta } ^ { 2 } \mu t > 0 ,$ there are two roots $M _ { 1 }$ and $M _ { 2 }$ such that when $M _ { 1 } < M < M _ { 2 } ,$ , we get $\pi _ { i } ^ { * } - \bar { \pi } _ { i } ^ { * } > 0 .$ . By solving the previous inequality, we get the condition in part (c).

(d) From Equations (A.10) and (A.8), we get

$$
\begin{array}{r l} & C S ^ {*} - \bar {C S} ^ {*} = v - \frac {t}{4} [ 1 + (1 - \beta) (1 - \theta - \theta_ {b}) ] - p _ {i} ^ {*} + \gamma \frac {(v _ {l} - p ^ {*}) ^ {2}}{t _ {L}} \\ & \qquad - \left[ (2 \theta + \theta_ {b}) (v - \bar {p} _ {i} ^ {*}) - t \left(\theta + \frac {\theta_ {b}}{4}\right) + \gamma \frac {(v _ {l} - \bar {p} _ {i} ^ {*}) ^ {2}}{t _ {L}} \right] \\ & \qquad = (1 - 2 \theta - \theta_ {b}) \bigg [ v - \frac {t}{4} (2 - \beta) - p _ {i} ^ {*} \bigg ] + \frac {t}{4} \theta (1 + \beta) \\ & \qquad + (\bar {p} _ {i} ^ {*} - p _ {i} ^ {*}) [ 2 \theta + \theta_ {b} + \mu (2 v _ {L} - \bar {p} _ {i} ^ {*} - p _ {i} ^ {*}) ]. \end{array}
$$

We can verify that $\partial ( C S - \bar { C S } ) / \partial w < 0$ (which is rigorously proved in Proposition $3 ( \mathrm { d } ) )$ . Therefore, if and only if w $< w _ { C S } ,$ $\stackrel { \cdot } { C } S ^ { * } \geq \bar { C } \bar { S } ^ { * }$ , where $w _ { C S }$ is defined as the root of Equation (28).

(e) From Equations (A.10) and (A.8), we get

$$
\begin{array}{r} W ^ {*} - \bar {W} ^ {*} = (1 - 2 \theta - \theta_ {b}) \bigg [ v - \frac {t}{4} (2 - \beta) \bigg ] + \frac {t}{4} \theta (1 + \beta) \\ + (\bar {p} _ {i} ^ {*} - p _ {i} ^ {*}) [ 3 \mu (\bar {p} ^ {*} - p _ {i} ^ {*}) - 2 h ]. \end{array}
$$

We have $\partial ( W ^ { * } - \bar { W } ^ { * } ) / \partial w = 2 ( \partial p _ { ; } ^ { * } / \partial w ) ( h - 3 \mu p _ { ; } ^ { * } )$ . Under the condition $( 1 - \theta - \theta _ { b } ) / \beta + ( \theta + ' \theta _ { b } ) < ( 2 + \dot { 3 } / h ) \mu t$ , we have $h - 3 \mu p _ { i } ^ { * } < 0$ and thus $\partial ( W ^ { \ast } - \bar { W } ^ { \ast } ) / \partial w < 0 .$ Therefore, if $w < w _ { w } ,$ $W ^ { * } \geq \bar { W } ^ { * } ,$ , where $w _ { w }$ is defined as the root of Equation (29).

## Proof of Corollary 1

(a) When the recommender system is consumer oriented $( \mathrm { i . e . }$ $w \leq 1 / \alpha )$ , by inequality (24), p<sup>∗</sup> is always less than $\bar { p } _ { i } ^ { * } \mathrm { i f } \theta _ { b } -$ $( 2 \theta + \theta _ { b } ) ( \stackrel { . . } { \theta _ { b } } + \theta ) - 2 \stackrel { . . } { \theta } h + 4 \mu ( \stackrel { . } { 1 } - 2 \theta - \theta _ { b } ) t < 0 ,$ or, equivalently, if $\theta > ( \sqrt { ( 3 \theta _ { b } + 8 \mu t + 2 h ) ^ { 2 } + 8 ( 4 \mu t + \theta _ { b } ) ( 1 - \theta _ { b } ) } - 3 \theta _ { b } -$ $8 \mu t - 2 h ) / 4 .$ Otherwise, $p _ { i } ^ { * } \le \bar { p } _ { i } ^ { * } \mathrm { ~ i f ~ } \beta \dot { < } ( 1 - \theta - \theta _ { b } ) ( 1 - \alpha w )$ $( \dot { 2 } \theta + \theta _ { b } + 2 h ) / [ \theta _ { b } - ( 2 \theta + \dot { \theta } _ { b } ) ( \dot { \theta } + \theta _ { b } ) + 4 \mu t ( 1 - 2 \theta - \theta _ { b } ) - 2 \theta h ]$ (by solving inequality (24)).

(b) When the recommender system is profit oriented $( \mathrm { i . e . , }$ $w > 1 / \alpha )$ , by inequality $( 2 4 ) , p _ { i } ^ { * }$ is always greater than $\bar { p } _ { i } ^ { * }$ if $\theta _ { b } - ( 2 \theta + \bar { \theta _ { b } } ) ( \theta _ { b } \stackrel { \cdot } { + } \theta ) - \bar { 2 } \theta h + \dot { 4 } \bar { \mu } ( 1 - 2 \theta \stackrel { \cdot } { - } \theta _ { b } ^ { - } ) t > 0$ . Therefore, $\hat { p } _ { i } < p _ { i }$ <sub>i</sub> requires $\theta > \left( \sqrt { ( 3 \theta _ { b } + 8 \mu t + 2 h ) ^ { 2 } + 8 ( 4 \mu t + \theta _ { b } ) ( 1 - \theta _ { b } ) } - \right.$ $3 \theta _ { b } - 8 \mu \bar { { \mathrm { ~ - ~ } } } 2 h ) / 4$ and $\beta > ( 1 - \theta - \theta _ { b } ) ( 1 - \dot { \alpha  w } ) ( 2 \theta + \theta _ { b } + 2 h ) /$ $[ \theta _ { b } - ( \dot { 2 } \theta + \theta _ { b } ) ( \theta + \theta _ { b } ) + 4 \mu t ( 1 - 2 \theta - \theta _ { b } ) - 2 \theta h ]$ (by solving inequality (24)).

## Proof of Corollary 2

Because

$$
\theta + \theta_ {b} + 4 \mu t > \frac {4 \mu t}{1 + \sqrt {1 - 8 \mu t \left(\frac {2 \theta + \theta_ {b} + 2 h}{\left(\theta_ {b} + 4 \mu t\right) (1 + 2 h)}\right) ^ {2} \left(\theta_ {b} + 2 \mu t\right)}},
$$

we get

$$
\begin{array}{c} w _ {2} = \frac {1}{\alpha} + \frac {\beta [ (\theta + \theta_ {b}) + 4 \mu t ]}{\alpha (1 - \theta - \theta_ {b})} - \frac {\beta}{\alpha (1 - \theta - \theta_ {b})} \\ \cdot \frac {4 \mu t}{1 + \sqrt {1 - 8 \mu t \left(\frac {2 \theta + \theta_ {b} + 2 h}{(\theta_ {b} + 4 \mu t) (1 + 2 h)}\right) ^ {2} (\theta_ {b} + 2 \mu t)}} > \frac {1}{\alpha}. \end{array}
$$

When $8 \mu t [ ( 2 \theta + \theta _ { b } + 2 h ) / ( ( \theta _ { b } + 4 \mu t ) ( 1 + 2 h ) ) ] ^ { 2 } ( \theta _ { b } + 2 \mu t ) +$ $( 1 - 4 \mu t / ( \theta + \theta _ { b } + 4 \mu t ) ) ^ { 2 } > 1$ , we can get $w _ { 1 } > 1 / \alpha$ . Otherwise, $w _ { 1 } < 1 / \alpha$

(a) When the recommender system is consumer oriented $( \mathrm { i } . \mathrm { e } . , w \leq 1 / \alpha )$ , based on Proposition $1 ( \mathbf { c } ) , \pi _ { i } ^ { * }$ is greater than $\bar { \pi } _ { i } ^ { * }$ if and only if $w _ { 1 } < w$ . Since $w \leq 1 / \alpha , \pi _ { i } ^ { * }$ is less than $\bar { \pi } _ { i } ^ { * }$ if w <sup>≤</sup> min $\{ 1 / \alpha , w _ { 1 } \}$

(b) When the recommender system is profit oriented $( \mathrm { i . e . , }$ $w > 1 / \alpha ) .$ , based on Proposition $1 ( \mathbf { c } ) , \pi _ { i } ^ { * }$ is greater than $\bar { \pi } _ { i } ^ { * } \operatorname { i f }$ and only if $w _ { 1 } < w < w _ { 2 } .$ . Since $w _ { 2 } > 1 / \bar { \alpha _ { , } } \pi _ { i } ^ { * } < \bar { \pi } _ { i } ^ { * } \mathrm { i f } w > w _ { 2 } $

## Proof of Proposition 2

(a) Because $\triangle p _ { i } = p _ { i } ^ { * } - \bar { p } _ { i } ^ { * }$ and $\beta$ does not afect $\bar { p } _ { i } ^ { * } ,$

$$
\frac {\partial \triangle p _ {i}}{\partial \beta} = \frac {\partial p _ {i} ^ {*}}{\partial \beta} = \frac {t (1 - \alpha w) (1 - \theta - \theta_ {b}) (1 + 2 h)}{[ (1 - \alpha w) (1 - \theta - \theta_ {b}) + \beta (\theta + \theta_ {b}) + 4 \beta \mu t ] ^ {2}}.
$$

Because all terms are positive except $( 1 - \alpha w ) , \partial \triangle p _ { i } / \partial \beta > 0 \mathrm { i }$ f and only if $w < 1 / \alpha$

(b) Because $\triangle D _ { i } = D _ { i } ^ { * } - \bar { D } _ { i } ^ { * }$ and $\beta$ does not afect $\bar { D } _ { i } ^ { * } ,$

$$
\frac {\partial \triangle D _ {i}}{\partial \beta} = \frac {\partial D _ {i} ^ {*}}{\partial \beta} = \frac {t (\alpha w - 1) (1 - \theta - \theta_ {b}) (1 + 2 h)}{[ (1 - \alpha w) (1 - \theta - \theta_ {b}) + \beta (\theta + \theta_ {b}) + 4 \beta \mu t ] ^ {2}}.
$$

Because all terms are positive except $( \alpha w - 1 ) , \partial \triangle D _ { i } / \partial \beta > 0 \mathrm { i }$ f and only if $w > 1 / \alpha$

(c) Because $\Delta \pi _ { i } = \pi _ { i } ^ { * } - \bar { \pi } _ { i } ^ { * }$ and $\beta$ does not afect $\bar { \pi } _ { i } ^ { * } ,$

$$
\begin{array}{r l} \frac {\partial \triangle \pi_ {i}}{\partial \beta} = & \frac {\partial \pi_ {i} ^ {*}}{\partial \beta} = t (1 + 2 h) ^ {2} (1 - \alpha) (1 + 2 h) (1 - \theta - \theta_ {b}) (1 - \alpha w) \\ & \cdot [ (1 - \alpha w) (1 - \theta - \theta_ {b}) + \beta (\theta + \theta_ {b}) ] \\ & \cdot \left(2 [ (1 - \alpha w) (1 - \theta - \theta_ {b}) + \beta (\theta + \theta_ {b}) + 4 \beta \mu t ] ^ {3}\right) ^ {- 1}. \end{array}
$$

Because all terms are positive except $( 1 - \alpha w ) [ ( 1 - \alpha w ) ( 1 -$ $\theta - \theta _ { b } ) + \beta ( \theta + \theta _ { b } ) ] , \partial \triangle \bar { \pi } _ { i } / \partial \beta > 0 \mathrm { i f } \bar { w } < 1 / \alpha ,$ or if w $> 1 /$ α and $w > ( \beta ( \dot { \theta _ { } } + \theta _ { b } ) + ( 1 - \theta - \theta _ { b } ) ) / ( \alpha ( 1 - \theta - \theta _ { b } ) )$

(d) Note that

$$
\begin{array}{r l} \frac {\partial \triangle C S}{\partial \beta} = & - \frac {t (1 - \theta - \theta_ {b})}{4 M ^ {3}} [ 4 (2 h + 1) ^ {2} (1 - \alpha w) \\ & \cdot [ (1 - \alpha w) (1 - \theta - \theta_ {b}) + \beta (\theta + \theta_ {b} + 2 \mu t) ] - M ^ {3} ]. \end{array}
$$

Therefore, $\partial \triangle C S / \partial \beta < 0 \mathrm { w h e n } ( 1 - \alpha w ) [ ( 1 - \alpha w ) ( 1 - \theta - \theta _ { b } ) +$ $\beta ( \theta + \theta _ { b } + 2 \mu t ) ] > M ^ { 3 } / ( 4 ( 2 h + 1 ) ^ { 2 } )$ . By solving the previous inequality, we get the condition in part (d).

(e) Note that

$$
\begin{array}{r} \frac {\partial_ {\triangle} W}{\partial \beta} = - \frac {t (1 - \theta - \theta_ {b})}{4 M ^ {3}} [ 8 (1 + 2 h) (1 - \alpha w) (3 \beta \mu t - h [ (1 - \alpha w) \\ \cdot (1 - \theta - \theta_ {b}) + \beta (\theta + \theta_ {b} - 2 \mu t) ]) - M ^ {3} ]. \end{array}
$$

Therefore, $\partial \triangle W / \partial \beta < 0$ when $( 1 - \alpha w ) [ 3 \beta \mu t - h ( 1 - \alpha w ) ( 1 -$ $\theta - \theta _ { b } ) - \beta h ( \theta + \theta _ { b } - 2 \mu t ) ] > M ^ { 3 } / ( 8 ( 1 + 2 h ) )$ . Solving the inequality leads to the condition in part (e).

## Proof of Proposition 3

(a) Part (a) follows from

$$
\frac {\partial \triangle p _ {i}}{\partial w} = \frac {\partial p _ {i} ^ {*}}{\partial w} = \frac {\alpha \beta t (1 - \theta - \theta_ {b}) (1 + 2 h)}{[ (1 - \alpha w) (1 - \theta - \theta_ {b}) + \beta (\theta + \theta_ {b}) + 4 \beta \mu t ] ^ {2}} > 0.
$$

(b) Part (b) follows from

$$
\frac {\partial \triangle D _ {i}}{\partial w} = \frac {\partial D _ {i} ^ {*}}{\partial w} = - \frac {\alpha \beta \mu t (1 - \theta - \theta_ {b}) (1 + 2 h)}{[ (1 - \alpha w) (1 - \theta - \theta_ {b}) + \beta (\theta + \theta_ {b}) + 4 \beta \mu t ] ^ {2}} <   0.
$$

(c) Part (c) follows from

$$
\begin{array}{r l} \frac {\partial \triangle \pi_ {i}}{\partial w} = \frac {\partial \pi_ {i} ^ {*}}{\partial w} = \alpha (1 - \alpha) \beta t (1 + 2 h) ^ {2} \\ & \cdot (1 - \theta - \theta_ {b}) [ (1 - \alpha w) (1 - \theta - \theta_ {b}) + \beta (\theta + \theta_ {b}) ] \\ & \cdot \left([ (1 - \alpha w) (1 - \theta - \theta_ {b}) + \beta (\theta + \theta_ {b}) + 4 \beta \mu t ] ^ {3}\right) ^ {- 1}. \end{array}
$$

Therefore, $\partial \triangle \pi _ { i } / \partial w > 0$ if and only if $( 1 - \alpha w ) ( 1 - \theta - \theta _ { b } ) +$ $\beta ( \theta + \theta _ { b } ) > 0 .$ , or, equivalently, $w \dot { < } 1 / \alpha + \beta ( \theta + \theta _ { b } ) / [ \alpha ( 1 -$ $\theta - \theta _ { b } ) ] .$

(d) Part (d) follows from $\partial \Delta C S / \partial w = - ( \partial p _ { i } ^ { * } / \partial w ) ( 1 + 2 h -$ $2 \mu p _ { i } ^ { * } ) > 0 .$

(e) Part (e) follows from $\partial \Delta W / \partial w = 2 ( \partial p _ { i } ^ { * } / \partial w ) ( h - 3 \mu p _ { i } ^ { * } )$ Solving $h - 3 \mu p _ { i } ^ { * } < 0$ leads to the condition on w in part (e).

## Proof of Proposition 4

(a) Notice that

$$
\frac {\partial \triangle p _ {i}}{\partial \theta} = \frac {\beta t (1 + 2 h) (1 - w \alpha - \beta)}{[ (1 - \alpha w) (1 - \theta - \theta_ {b}) + \beta (\theta + \theta_ {b}) + 4 \beta \mu t ] ^ {2}} - \frac {2 t}{\theta_ {b} + 4 \mu t}.
$$

When $1 - w \alpha - \beta < 0 ,$ the first fraction on the right-hand side is negative, and thus $\partial \triangle p _ { i } / \partial \theta < 0$ . When $1 - \bar { w } \alpha - \beta > 0 ,$ or, equivalently, when $w < ( 1 - \beta ) / \alpha ,$ , solving $\partial \triangle p _ { i } / \partial \theta > 0$ leads to the condition on θ in part (a).

(b) Notice that

$$
\frac {\partial \triangle D _ {i}}{\partial \theta} = - \frac {\beta \mu t (1 + 2 h) (1 - w \alpha - \beta)}{[ (1 - \alpha w) (1 - \theta - \theta_ {b}) + \beta (\theta + \theta_ {b}) + 4 \beta \mu t ] ^ {2}} - \frac {\theta_ {b} + 2 \mu t}{\theta_ {b} + 4 \mu t}.
$$

When $1 - w \alpha - \beta > 0 ,$ the first fraction on the right-hand side is negative, and thus $\partial \triangle D _ { i } / \partial \theta < 0$ . When $1 - w \alpha - \beta < 0 ,$ , or, equivalently, when $w > ( 1 - \beta ) / \alpha .$ , solving $\partial \triangle D _ { i } / \partial \theta \dot { > } 0$ leads to the condition on θ in part (b).

(c) Notice that

$$
\begin{array}{l} \frac {\partial \triangle \pi_ {i}}{\partial \theta} = \frac {t (1 - \alpha)}{2} \\ \quad \cdot \left(\frac {(1 + 2 h) ^ {2} \beta (1 - \alpha w - \beta) [ (1 - \alpha w) (1 - \theta - \theta_ {b}) + \beta (\theta + \theta_ {b}) ]}{[ (1 - \alpha w) (1 - \theta - \theta_ {b}) + \beta (\theta + \theta_ {b}) + 4 \beta \mu t ] ^ {3}} \right. \\ \quad \left. - \frac {4 (2 \mu t + \theta_ {b}) (2 \theta + \theta_ {b} + 2 h)}{(4 \mu t + \theta_ {b}) ^ {2}}\right). \end{array}
$$

When $( 1 - \alpha w - \beta ) [ ( 1 - \alpha w ) ( 1 - \theta - \theta _ { b } ) + \beta ( \theta + \theta _ { b } ) ] < 0 ,$ the first term in the brackets is negative, and we get ∂<sup>4</sup> $\pi _ { i } / \partial \theta < 0$ When $( 1 - \alpha w - \beta ) [ ( 1 - \alpha w ) ( 1 - \theta - \theta _ { b } ) + \beta ( \theta + \theta _ { b } ) ] > 0 ,$ , solving $\partial \triangle \pi _ { i } / \partial \theta > 0$ leads to the condition in part (c).

(d) Note that

$$
\begin{array}{l} \frac {\partial \triangle C S}{\partial \theta} \\ = - 2 v + \frac {(5 - \beta) t}{4} + 4 t \frac {(2 \theta + \theta_ {b} + 2 h) (\theta_ {b} + 3 \mu t)}{(4 \mu t + \theta_ {b}) ^ {2}} - \beta t (1 + 2 h) ^ {2} \\ \cdot (1 - \alpha w - \beta) \frac {(1 - \alpha w) (1 - \theta - \theta_ {b}) + \beta (\theta + \theta_ {b}) + 2 \beta \mu t}{[ (1 - \alpha w) (1 - \theta - \theta_ {b}) + \beta (\theta + \theta_ {b}) + 4 \beta \mu t ] ^ {3}}. \end{array}
$$

Solving $\partial \triangle C S / \partial \theta > 0$ leads to the condition in part (d).

(e) Part (e) follows from that

$$
\begin{array}{r l} & {\frac {\partial \triangle W}{\partial \theta}} \\ & {= - 2 v + \frac {(5 - \beta) t}{4} + 4 t \frac {\mu t (6 \theta + 3 \theta_ {b} + 2 h) - \theta_ {b} h}{(4 \mu t + \theta_ {b}) ^ {2}} + 2 t \beta (1 + 2 h)} \\ & {\quad \cdot (1 - \alpha w - \beta) \frac {(3 + 2 h) \beta \mu t - h [ (1 - \alpha w) (1 - \theta - \theta_ {b}) + \beta (\theta + \theta_ {b}) ]}{[ (1 - \alpha w) (1 - \theta - \theta_ {b}) + \beta (\theta + \theta_ {b}) + 4 \beta \mu t ] ^ {3}}.} \end{array}
$$

Solving $\partial \triangle W / \partial \theta > 0$ leads to the condition in part (e).

## Proof of Proposition 5

Given w, the equilibrium outcome is described in Lemma 2 as long as $\beta > ( 1 - \theta - \theta _ { b } ) ( \alpha w - 1 ) / ( \theta + \theta _ { b } + 2 \mu t )$ , or $w < 1 / \alpha +$ $\beta ( \theta + \theta _ { b } + 2 \mu t ) / ( \alpha ( 1 - \theta - \theta _ { b } ) )$ . The retailer chooses w that maximizes $\pi _ { R } ^ { * } ,$ , where $\pi _ { R } ^ { * }$ is defined as in Equation (20), and the optimal w is characterized by its first-order derivative:

$$
\frac {\partial \pi_ {R} ^ {*}}{\partial w} = \frac {\beta t \alpha^ {2} (1 + 2 h) ^ {2} (1 - \theta - \theta_ {b}) [ (1 - \alpha w) (1 - \theta - \theta_ {b}) + \beta (\theta + \theta_ {b}) ]}{[ (1 - \alpha w) (1 - \theta - \theta_ {b}) + \beta (\theta + \theta_ {b}) + 4 \beta \mu t ] ^ {3}}.
$$

We can thus derive the optimal w as in Equation (30). We can verify that the optimal w in Equation (30) is less than $1 / \alpha +$ $\beta ( \theta + \theta _ { b } + 2 \mu t ) / ( \alpha ( 1 - \theta - \theta _ { b } ) )$ . We can verify that ∂w $\dot { \left/ { \partial \beta } \right. } > 0$ and ∂w<sup>∗</sup> $/ \partial ( \theta + \theta _ { b } ) > 0$

## Proof of Proposition 6

(a) Part (a) follows because

$$
p _ {i} ^ {*} - \bar {p} _ {i} ^ {*} = \frac {(1 + 2 h) \theta_ {b} + 4 \mu t (1 - 2 \theta - \theta_ {b})}{4 \mu (\theta_ {b} + 4 \mu t)} > 0.
$$

(b) Note that

$$
D _ {i} ^ {*} - \bar {D} _ {i} ^ {*} = \frac {1}{4} \left(1 - 2 \theta - \theta_ {b} - \frac {\theta_ {b} (2 h + 2 \theta + \theta_ {b})}{\theta_ {b} + 4 \mu t}\right).
$$

Solving $D _ { i } ^ { * } - \bar { D } _ { i } ^ { * } > 0$ leads to the condition in part (b).

(c) Part (c) follows because

$$
\pi_ {i} ^ {*} - \bar {\pi} _ {i} ^ {*} = \frac {1 - \alpha}{1 6 \mu} \left[ (1 + 2 h) ^ {2} - 8 \mu t (\theta_ {b} + 2 \mu t) \left(\frac {2 \theta + \theta_ {b} + 2 h}{\theta_ {b} + 4 \mu t}\right) ^ {2} \right] > 0.
$$

(d) Note that

$$
\begin{array}{l} C S ^ {*} - \bar {C S} ^ {*} = \beta \frac {t (1 - \theta - \theta_ {b})}{4} + \frac {(4 v - 2 t - (1 + 2 h) / \mu) (1 - 2 \theta - \theta_ {b})}{4} \\ \qquad + \frac {t \theta}{4} - [ (1 + 2 h) \theta_ {b} + 4 \mu t (1 - 2 \theta - \theta_ {b}) ] \\ \qquad \cdot [ (2 h + 2 \theta + \theta_ {b}) \theta_ {b} + (4 \mu t + \theta_ {b}) (4 h - 1 + 6 \theta + 3 \theta_ {b}) ] \\ \qquad \cdot (1 6 \mu (\theta_ {b} + 4 \mu t) ^ {2}) ^ {- 1}. \end{array}
$$

Solving $C S ^ { * } - \bar { C S } ^ { * } > 0$ leads to the condition in part (d).

(e) Note that

$$
\begin{array}{r l} W ^ {*} - \bar {W} ^ {*} & = \left[ v - \frac {t (2 - \beta)}{4} \right] (1 - 2 \theta - \theta_ {b}) + \frac {t (1 + \beta) \theta}{4} \\ & \quad - [ (1 + 2 h) \theta_ {b} + 4 \mu t (1 - 2 \theta - \theta_ {b}) ] [ (3 - 2 h) \theta_ {b} \\ & \quad + 4 \mu t (3 + 6 \theta + 3 \theta_ {b} + 4 h) ] \cdot (1 6 \mu (\theta_ {b} + 4 \mu t) ^ {2}) ^ {- 1}. \end{array}
$$

Solving $W ^ { * } - \bar { W } ^ { * } > 0$ leads to the condition in part (e).

## Endnotes

<sup>1</sup> The results do not require these sellers to be manufacturers. If they are resellers, the production cost in our model should be interpreted as the procurement cost for these resellers.

<sup>2</sup> An alternative setting is one in which R buys from manufacturers and resells to consumers. Amazon.com uses such a wholesale scheme for some products and the platform scheme we consider in this paper for other products. It is noteworthy that Amazon.com sells 93% of products in the Electronics category, 83.3% of Shoes, 96.9% of products in the Sports and Outdoors category, and 96.8% of products in the Jewelry category using the platform scheme Jiang et al. (2011).

<sup>3</sup> The utility for the product she is not loyal to can be assumed to be zero.

## References

Adomavicius G, Tuzhilin A (2005) Toward the next generation of recommender systems: A survey of the state-of-the-art and possible extensions. IEEE Trans. Knowledge Data Engrg. 17(6):734–749.

Bergemann D, Ozmen D (2006) Optimal pricing with recommender systems. Proc. 7th ACM Conf. Electronic Commerce (Association for Computing Machinery, New York), 43–51.

Bester H, Petrakis E (1995) Price competition and advertising in oligopoly. Eur. Econom. Rev. 39(6):1075–1088.

Brynjolfsson E, Hu Y, Simester D (2011) Goodbye Pareto principle, hello long tail: The efect of search costs on the concentration of product sales. Management Sci. 57(8):1373–1386.

Burke R (2002) Hybrid recommender systems: Survey and experiments. User Modeling User-Adapted Interaction 12(4):331–370.

Chen L-S, Hsu F-H, Chen M-C, Hsu Y-C (2008) Developing recommender systems with the consideration of product profitability for sellers. Inform. Sci. 178(4):1032–1048.

Cooke ADJ, Sujan H, Sujan M, Weitz BA (2002) Marketing the unfamiliar: The role of context and item-specific information in electronic agent recommendations. J. Marketing Res. 39(4):488–497.

Das A, Mathieu C, Ricketts D (2009) Maximizing profit using recommender systems. arXiv preprint arXiv:0908.3633.

Fleder D, Hosanagar K (2009) Blockbuster culture’s next rise or fall: The impact of recommender systems on sales diversity. Management Sci. 55(5):697–712.

Gal-Or E, Gal-Or M (2005) Customized advertising via a common media distributor. Marketing Sci. 24(2):241–253.

Gal-Or E, Gal-Or M, May JH, Spangler WE (2006) Targeted advertising strategies on television. Management Sci. 52(5):713–725.

Gretzel U, Fesenmaier D (2006) Persuasion in recommender systems. Internat. J. Electronic Commerce 11(2):81–100.

Grossman GM, Shapiro C (1984) Informative advertising with diferentiated products. Rev. Econom. Stud. 51(1):63–81.

Häubl G, Murray K (2006) Double agents: Assessing the role of electronic product recommendation systems. Sloan Management Rev. 47(3):8–12.

Häubl G, Trifts V (2000) Consumer decision making in online shopping environments: The efects of interactive decision aids. Marketing Sci. 19(1):4–21.

Hennig-Thurau T, Marchand A, Marx P (2012) Can automated group recommender systems help consumers make better choices? J. Marketing 76(5):89–109.

Hervas-Drane A (2015) Recommended for you: The efect of word of mouth on sales concentration. Internat. J. Res. Marketing 32(2):207–218.

Hinz O, Eckert J (2010) The impact of search and recommendation systems on sales in electronic commerce. Bus. Inform. Systems Engrg. 2(2):67–77.

Hosanagar K, Krishnan R, Ma L (2008) Recommended for you: The impact of profit incentives on the relevance of online recommendations. Proc. 29th Internat. Conf. Information Systems (ACM Press, Paris), 31.

Hosanagar K, Fleder D, Lee D, Buja A (2013) Will the global village fracture into tribes? Recommender systems and their efects on consumer fragmentation. Management Sci. 60(4):805–823.

Hostler RE, Yoon VY, Guimaraes T (2005) Assessing the impact of internet agent on end users’ performance. Decision Support Systems 41(1):313–323.

Iyer G, Soberman D, Villas-Boas JM (2005) The targeting of advertising. Marketing Sci. 24(3):461–476.

Jabr W, Zheng E (2014) Know yourself and know your enemy: An analysis of firm recommendations and consumer reviews in a competitive environment. MIS Quart. 38(3):635–654.

Jiang B, Jerath K, Srinivasan K (2011) Firm strategies in the “mid tail” of platform-based retailing. Marketing Sci. 30(5):757–775.

Johnson JP, Myatt DP (2006) On the simple economics of advertising, marketing, and product design. Amer. Econom. Rev. 96(3): 756–784.

Lewis TR, Sappington DEM (1994) Supplying information to facilitate price discrimination. Internat. Econom. Rev. 35(2):309–327.

McNee SM, Riedl J, Konstan JA (2006) Being accurate is not enough: How accuracy metrics have hurt recommender systems. CHI’06 Extended Abstr. Human Factors Comput. Systems (Association for Computing Machinery, New York), 1097–1101.

Mooney RJ, Roy L (2000) Content-based book recommending using learning for text categorization. Proc. Fifth ACM Conf. Digital Libraries (Association for Computing Machinery, New York), 195–204.

Oestreicher-Singer G, Sundararajan A (2012a) Recommendation networks and the long tail of electronic commerce. MIS Quart. 36(1):65–83.

Oestreicher-Singer G, Sundararajan A (2012b) The visible hand? Demand efects of recommendation networks in electronic markets. Management Sci. 58(11):1963–1981.

Pathak B, Garfinkel R, Gopal RD, Venkatesan R, Yin F (2010) Empirical analysis of the impact of recommender systems on sales. J. Management Inform. Systems 27(2):159–188.

Pu P, Chen L, Hu R (2011) A user-centric evaluation framework for recommender systems. Proc. Fifth ACM Conf. Recommender Systems (Association for Computing Machinery, New York), 157–164.

Senecal S, Nantel J (2004) The influence of online product recommendations on consumers’ online choices. J. Retailing 80(2): 159–169.

Shani G, Brafman R, Heckerman D (2005) An MDP-based recommender system. J. Machine Learning Res. 6(September): 1265–1295.

Soberman D (2004) Research note: Additional learning and implications on the role of informative advertising. Management Sci. 50(12):1744–1750.

Tam KY, Ho SY (2005) Web personalization as a persuasion strategy: An elaboration likelihood model perspective. Inform. Systems Res. 16(3):271–291.

Tam KY, Ho SY (2006) Understanding the impact of web personalization on user information processing and decision outcomes. MIS Quart. 30(4):865–890.

Vargas S, Castells P (2011) Rank and relevance in novelty and diversity metrics for recommender systems. Proc. Fifth ACM Conf. Recommender Systems (Association for Computing Machinery, New York), 109–116.

Wang J, Zhang Y (2011) Utilizing marginal net utility for recommendation in e-commerce. Proc. 34th Internat. ACM SIGIR Conf. Res. Development Inform. Retrieval (Association for Computing Machinery, New York), 1003–1012.

Xiao B, Benbasat I (2007) E-commerce product recommendation agents: Use, characteristics, and impact. MIS Quart. 31(1): 137–209.

Xiao B, Benbasat I (2015) Designing warning messages for detecting biased online product recommendations: An empirical investigation. Inform. Systems Res. 26(4):793–811.
