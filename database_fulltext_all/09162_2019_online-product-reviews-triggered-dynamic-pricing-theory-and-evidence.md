---
otero_id: 9162
otero_key: "43ZRESQQ"
title: "Online Product Reviews-Triggered Dynamic Pricing: Theory and Evidence"
authors: "Juan Feng; Xin Li; Xiaoquan (Michael) Zhang"
year: "2019"
journal: "Information Systems Research"
doi: "10.1287/isre.2019.0852"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
This article was downloaded by: [128.59.222.107] On: 05 December 2019, At: 17:20 Publisher: Institute for Operations Research and the Management Sciences (INFORMS) INFORMS is located in Maryland, USA

![](/api/attachments/43ZRESQQ/fulltext/images/9d80f432436144bbed1710784ebad71ad076c29298d37a837d4c9d2106941218.jpg)

# Information Systems Research

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

# Online Product Reviews-Triggered Dynamic Pricing: Theory and Evidence

Juan Feng, Xin Li, Xiaoquan (Michael) Zhang

To cite this article:

Juan Feng, Xin Li, Xiaoquan (Michael) Zhang (2019) Online Product Reviews-Triggered Dynamic Pricing: Theory and Evidence Information Systems Research

Published online in Articles in Advance 05 Dec 2019

https://doi.org/10.1287/isre.2019.0852

Full terms and conditions of use: https://pubsonline.informs.org/Publications/Librarians-Portal/PubsOnLine-Terms-and-Conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

Copyright © 2019, INFORMS

Please scroll down for article—it is on subsequent pages

## inferms

With 12,500 members from nearly 90 countries, INFORMS is the largest international association of operations research (O.R.) and analytics professionals and students. INFORMS provides unique networking and learning opportunities for individual professionals, and organizations of all types and sizes, to better understand and use O.R. and analytics tools and methods to transform strategic visions and achieve better outcomes.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# Online Product Reviews-Triggered Dynamic Pricing: Theory and Evidence

Juan Feng,<sup>a</sup> Xin Li,<sup>a</sup> Xiaoquan (Michael) Zhang

<sup>a</sup> Department of Information Systems, College of Business, City University of Hong Kong, Kowloon, Hong Kong; <sup>b</sup> Department of Decision Sciences and Managerial Economics, Business School, Chinese University of Hong Kong, New Territories, Hong Kong Contact: juafeng@cityu.edu.hk, http://orcid.org/0000-0002-0548-1531 (JF); xin.li.phd@gmail.com, D http://orcid.org/0000-0002-0041-3134 (XI): zhang@cuhk.edu,hk. D http://orcid.org/0000-0003-0690-2331 (X(M)Z)

Received: Revised: May 1 Accepted: Published Online in Articles in Advance: December 5, 2019

https://doi.org/10.1287/isre.2019.0852

Copyright:

Abstract. Prior works offer compelling evidence that, on the demand side of the market, user-generated online product reviews play a very important role in informing consumers purchase decisions. On the supply side, however, the interplay between online product reviews and firm strategies is less understood. We build an analytical model that differentiates products based on consumers’ preference for tastes (horizontal differentiation) or quality (vertical differentiation) and show that a firm is able to not only manipulate its pricing to influence online product reviews (thus influencing sales) but also, adjust pricing dynamically in response to online word of mouth. Our model derives rich and testable results on possible price trajectories. To offer empirical support for the analytical predictions, we conduct a panel data study of prices and reviews. We adopt a difference-in differences framework to address endogeneity challenges.

History: Anindya Ghose, Senior Editor; Jeffrey Hu, Associate Editor. Funding: This research is partially supported by the Hong Kong Research Grants Council [GRF 644511, 11500216, 11501414, 11503115, 11504815, 11507218, 14503818, and 16504614], the National Natural Sci ence Foundation of China [Grants 71572169 and 71401148], and the CityU Shenzhen Research Institute Supplemental Material: The online appendix is available at https://doi.org/10.1287/isre.2019.0852.

Keywords: pricing • online product reviews • analytical model • empirical stud

## 1. Introduction

Online word of mouth (WOM) plays an important role in both the demand and supply sides of the market. On the demand side, it empowers online consumers by reducing uncertainty, allowing consumers to learn about products and services and make smart purchase decisions (Dellarocas 2003, Wang et al. 2018). The majority of the extensive and growing literature examines online reviews from the demand side and finds that WOM has a significant impact on sales (e.g., Chevalier and Mayzlin 2006, Wang and Zhang 2009).

If consumers rely on WOM information to make purchase decisions, it is imperative for firms to maintain a good online WOM profile. On the supply side of the market, how firms make use of WOM information becomes an important and interesting question. Despite the important strategic value of WOM on the supply side, surprisingly few studies address how WOM affects firms’ decision making.

There are several institutional reasons why WOM plays an important role in supply-side strategies. First, firms no longer fully control information. In a traditional market, a firm can choose what information to release and how it is released. Today, various social media channels disseminate user-generated content that complements and competes with firmgenerated information (Zhang and Zhu 2011). Consumers often consider user-generated content to be more credible than information provided by firms (Bickart and Schindler 2011). Second, the availability of tremendous individual-level behavioral data on users and advancements in data analytics enable firms to react more quickly to consumer activities and gain a profit Organizations, such as Amazon and Harrah’s, have increased their revenue dramatically by making use of the consumer data that they collect (Davenport 2006 Brynjolfsson and McAfee 2014). Firms’ investments in information technology (IT) allow them to monitor and analyze a large amount of data in a short period of time, making real-time personalization possible (Sun et al. 2019). Third, an often-neglected effect comes from the tremendous reduction in menu costs. Given the ease of changing product prices online (i.e., reduced menu costs), firms can easily implement pricing strategies that rely on dynamic feeds of consumer and product data (Brynjolfsson and Smith 2000, Zhang and Feng 2011). Taken together, WOM can potentially have a significant impact on firms’ strategies.

Firms are known to leverage channels of consumer reviews in several ways. The first, downright illegal, way is to post fake reviews (Dellarocas 2006). There is plenty of anecdotal evidence suggesting that firms fake WOM in their own favor. In September 2013, New York’s attorney general fined 19 firms and several “reputation-enhancement” companies a total of \$350,000 for posting fake reviews.<sup>1</sup> When there is a whole industry offering the service of providing fake reviews, it is not hard to imagine the size and magnitude of such activities. A recent study by Mayzlin et al. (2014), using a clever empirical design, finds convincing and economically significant evidence that hotels post fake positive reviews for themselves and negative reviews for competitors.

A second, sometimes unethical, way to manipulate WOM is to reward positive reviews and punish negative ones. For example, Ye et al. (2014) find that low-quality sellers may coerce buyers to revoke their negative feedback through retaliation. Many shops encourage people to click the “Like” button on their Facebook pages. Figure 1 shows an advertisement that encourages positive reviews by offering a raffle to win a \$100 gift card. In an attempt to discourage negative reviews, a hotel in Hudson, New York charged wedding couples \$500 for each bad review posted by guests. The policy backfired and resulted in many negative reviews from angry visitors.<sup>2</sup>

These illegal or unethical ways of managing WOM show firms’ desperation with respect to new challenges in marketing. Moving toward more legal means of WOM manipulation, a third way that firms can respond to WOM is to engage actively with consumers on social media platforms. Gu and Ye (2013) report that management response to consumers comments can significantly improve future satisfaction of complaining customers. Adomavicius et al. (2013) find that consumer perceptions can be anchored by online recommendations. Shen et al. (2015) empirically show that platforms, such as Amazon.com (henceforth Amazon) and Barnes & Noble (henceforth BN), can design online review systems to improve book reviewers’ reputations by allowing them to choose the right product to review and the right rating to post.

Figure 1. (Color online) Reward for Positive WOM  
![](/api/attachments/43ZRESQQ/fulltext/images/c78a185af43a97fd44aacc6ab15e0078691a1347fcabbef02e515d154ede4870.jpg)

This study looks at how WOM analysis enables supply-side strategies that go beyond direct intervention with WOM content. Consistent with existing literature, we argue that sellers can influence WOM generation through pricing, a traditional marketing tool. We model how a profit-maximizing seller needs to strategically monitor and react to online reviews and therefore, change price dynamics for potential online reviews. In our model, consumers’ utilities are influenced by both consumer characteristics (e.g., misfit costs) and product characteristics (e.g., product quality). These two dimensions are consistent with the horizontal differentiation of tastes and the vertical differentiation of quality levels in the literature.

By incorporating misfit cost and quality level with online reviews, our theoretical model generates some interesting insights into a firm’s optimal price trajectory. The impact of online reviews can be quite different on products with different quality levels and misfit costs.

1. Not every seller is affected by online reviews, and we identify conditions under which it is optimal for a seller to act as if online reviews do not exist.

2. Contrary to the conventional wisdom that firms need to cut the initial price to induce preferential future reviews, we find that a price-cutting strategy is not always needed, and it may even be beneficial for firms to charge a high initial price. Consequently, both the firm’s initial price and profit are nonmonotonic on the perceived quality of the product or consumers’ misfit cost.

3. As a result, the arrival of information makes it impossible to judge whether the firm is adopting a penetration or skimming pricing strategy solely from the price trend over time: a downward price trend can be observed even when the firm initially charges a low price, and an upward pricing trend can be observed even when the firm charges a high initial price.

We offer empirical support for these theoretical predictions with a panel data set of books. We collect data from two sources (Amazon and BN) to overcome the endogeneity problem of unobservable product and seller characteristics. The causal relationship is established with a difference-in-differences (DID) design, which has been used in the context of WOM by other studies (e.g., Chevalier and Mayzlin 2006, Zu and Zhang 2010). Using the data set, our empirical analysis supports the key findings of the analytical model and identifies firms’ different pricing behaviors in response to reviews.

Our study is closely related to several prior studies and generates additional results by extending them. Li and Hitt (2010) propose the importance of considering perceived value (the difference between price and quality) in generating WOM. Their two-period model studies how first-period price may influence reviews and how a seller should choose an optimal strategy when facing such “price effects.” They also use a linear empirical model to provide supporting evidence that online ratings react differently to price and perceived value. A key difference between their study and our study is that they focus more on how initial price may influence subsequent WOM, whereas our model goes beyond that and examines how price needs to be adjusted in response to WOM.

Yu et al. (2016) study the impact of consumergenerated quality information on a firm’s pricing strategy. Different from their study, our model considers misfit costs and product characteristics and offers a more general theoretical framework. As a result, our model generates more realistic and more complex price patterns. In our model, the price can go up or down depending on these contingent factors. Finally, Kwark et al. (2014) build an analytical model to study the effect of WOM on vertical channel competition. In their model, WOM provides information to consumers about product quality and fit. Our model also captures these two dimensions of differentiation. Our work is different in that we do not study upstream competition; instead, we focus our attention on firm’s price adjustment decisions.

We contribute to the literature in several ways. First, although most prior WOM literature examines online product reviews’ impact on demand, we offer theoretical and empirical implications on how WOM interacts with the sellers’ pricing strategy on the supply side. Second, building on studies of customer acquisition, we contribute to the pricing literature by describing a mechanism that dynamically determines products’ price trajectories. The dynamic nature of our model makes it highly relevant to e-commerce in the big data era when real-time and dynamic information is constantly available and the cost of changing price is converging to zero (Brynjolfsson and Smith 2000). We show that the pricing strategies are more sophisticated than “penetration” or “skimming” pricing depending on the product’s misfit cost and perceived quality levels. Third, this research complements prior arguments for price’s impact on WOM (e.g., Li and Hitt 2010, Kwark et al. 2014, Yu et al. 2016). Different from these previous studies that model the indirect pricing effect on sales through WOM, this research theoretically and empirically examines sellers’ explicit use of WOM in their dynamic pricing strategies. Overall, we first propose a theoretical model to study how firms can improve their pricing by using WOM and then offer empirical evidence that such dynamic pricing strategies may have already been adopted by sellers in some e-commerce markets.

## 2. Prior Literature 2.1. Dynamic Pricing

Finding an optimal pricing plan is a very challenging task for retailers (Stigler 1964, Shapiro 1983, Villas-Boas 2004). In the current environment of rapid market development, firms need to continually react to changes (Athey and Bagwell 2008). Although useful, static models cannot describe the intricacies of the market in many situations (Zhang and Feng 2011, Mehra et al. 2012). The literature has seen an increased number of studies on dynamic pricing.

There are two commonly observed pricing strategies for new products: penetration pricing and skimming pricing (Hotler and Armstrong 2012). A pen-etration pricing strategy is helpful for building the reputation of a (perceived) low-quality product (Shapiro 1983) or for a seller of niche products to extract surplus from buyers with low willingness to pay (Bergemann and Valimaki 2006). Skimming pricing is effective when the market is highly differentiated and consumers are not price sensitive (Noble and Gruca 1999).

Wernerfelt (1986) studies the implications of experience curves and brand loyalty for optimal dy namic pricing policy. Prices should decrease over time for high discount rates and steeper exogenous declines in variable costs. Conversely, prices should increase over time if experience curves affect fixed costs and if consumers are brand loyal. Zhao (2000) investigates firms’ optimal advertising and pricing strategies when introducing a new product with a duopoly model. Advertising is used both to raise awareness about the product and to signal its quality. A low-quality firm has a strong incentive to increase its advertising spending from its optimal level. To deter the low-quality firm’s pooling strategy, the high-quality firm should decrease its advertising spending so that mimicry is not appealing to the lowquality firm. Alba et al. (1999) explore the effects of the frequency and depth of discounts on consumers’ price knowledge for competing stores and brands. Their results illustrate the importance of context in determining consumers’ price knowledge in a competitive environment. Interestingly, in some situations, firms should increase the price to maximize the profit. Similarly, Krishna et al. (2007) argue that price in creases, although rare in practice, may be a valid strategy for firms. They study when firms should raise prices and whether to increase prices across the board or target a specific segment of the customer base. Depending on market conditions, such as the market shares of the two firms and price knowledge across consumer segments, a firm may wish to implement targeted price increases in some situations, introduce across the board price increases in others, and keep the prices unchanged in still others. Su (2007) develops a model of dynamic pricing with endogenous intertemporal demand. It is found that, when high-value customers are proportionately less patient, markdown pricing policies are effective, because high-value customers buy early at high prices, whereas low-value customers are willing to wait. In contrast, when highvalue customers are more patient than low-value customers, prices should increase over time to discourage inefficient waiting. Erdem et al. (2008) develop a structural model of household behavior in an environment where there is uncertainty about brand attributes and where both prices and advertising signal brand quality. They show that price is an important signal of brand quality, and frequent price promotions may have the unintended consequence of reducing brand equity.

Although these prior studies generally examine dynamic price patterns, the driving force of dynamic pricing is not the continuous arrival of new information. In contrast to these studies, this paper explores how firms should be constantly aware of changes in the market environment and keep updating their knowledge by monitoring WOM. We argue that WOM-based dynamic pricing opens a new door for firms to achieve competitive advantage.

## 2.2. Pricing with Consumer Data

With the increasing availability of consumer data, in the age of big data, firms are able to improve their business decisions. Our study is aligned with the literature on dynamic price optimization using consumer data (Kohavi et al. 2002). In this stream of research, Lewis (2005) takes a dynamic programming approach to inspect optimal pricing when consumers transaction history is available through customer relationship management systems. The study uses a latent-class logit model to examine customer buying behavior. The dynamic optimization procedure yields profit-maximizing price paths. In the same vein, Bertsimas and Perakis (2006) discuss a situation when the consumer demand function is not known ex ante. They present an optimization approach for jointly learning the demand as a function of price and dynamically setting product prices. In a recent study, Farias and Van Roy (2010) examine a dynamic pricing problem faced by a vendor with limited inventory and uncertainty about demand in a framework with an infinite time horizon. Because the vendor learns from transaction data, the strategy must take into consideration the impact of price on both revenue and future observations. Their proposed heuristic approach to pricing can lead to significant revenue gains over previously proposed methods. Pathak et al. (2010) find that more information regarding quality and fit of products can increase demand. At the same time, providing value-added services, such as WOM and recommendations, allows retailers to charge higher prices. The results of these studies can benefit not only e-commerce companies but also, traditional retailers because consumer transaction data are available even without the internet.

Transaction data are by no means the only source of consumer data that sellers can use. Rusmevichientong et al. (2006) develop a model of price optimization that leverages consumer preferences data that can be collected through a website’s recommender system. Similarly, consumer shopping path data in traditional stores (Hui et al. 2009a, b) or browsing records in the form of clickstream data on e-commerce websites (Moe and Fader 2004a, b) can be valuable resources for sellers to optimize operations.

Different from these studies, in this paper, we explore how online product reviews can be useful for sellers, specifically for pricing optimization.

## 2.3. Online Word of Mouth

One major type of WOM is online product reviews that inform consumers about product/service attributes. Ba and Pavlou (2002) and Chen and Xie (2008) argue that consumer reviews provide productmatching information that helps consumers find products that match their needs. Such supplementary information helps reduce consumers’ uncertainty about products and facilitates sales. From this perspective, the elements and writing style of reviews affect their effectiveness. For example, Li and Zhan (2011) find that users prefer product reviews that are comprehensive (providing evidence and referring to product features) and easy to read. They also find that positive emotions in reviews increase perceived helpfulness. Along this line of research, other studies find that product types (experiential or utilitarian) moderate the effect of review features on perceived review helpfulness (Mudambi and Schuff 2010, Pan and Zhang 2011). Some recent studies find that earlier reviews affect later reviews (Li and Hitt 2008, Wu and Huberman 2008) and that social dynamics affect online reviews (e.g., Trusov et al. 2009, Moe and Trusov 2011, Samiei and Tripathi 2014). There are also studies exploring how to develop WOM systems to induce truthful reporting (Fan et al. 2005) and how user reporting habits may bias ratings (Hu et al. 2009). This stream of studies generally examines the usefulness of online WOM, but such studies look at WOM from only the consumers’ point of view.

From the sellers’ point of view, one important problem is the causal implications of online WOM on demand. There is a long-standing debate on whether online WOM is a predictor or an influencer of sales (Elberse and Eliashberg 2003). Several studies establish the causal effects of the valence, volume, and variation of online reviews (Godes and Mayzlin 2004, Chevalier and Mayzlin 2006, Duan et al. 2008, Chintagunta et al. 2010, Sun 2012). Although generally, review valence is associated with more sales (Dellarocas et al. 2007, Zhang et al. 2010), Berger et al. (2010) show that even negative reviews may have positive effects on sales, because they may increase product publicity, especially for lesser-known products. Lee et al. (2008) argue that the effects of negative reviews depend on the type of consumers. A high proportion of negative reviews will increase the conformity of high-involvement consumers only when the quality of those reviews is high. Kwark et al. (2016) show that the mean rating of online reviews of substitutive products has a negative role in purchasing, whereas the rating of complementary products has a positive role. The causal link between online WOM and sales is found to be affected by product and consumer characteristics or even the textual content of reviews (Forman et al. 2008, Hu et al. 2008, Zu and Zhang 2010, Archak et al. 2011, Ghose and Ipeirotis 2011, Lee and BradLow 2011). These studies, although appealing to sellers, only examine how WOM changes demand. Fundamentally, they are still studies of consumer decision making. Different from these studies, our paper examines how WOM may affect seller decision making in pricing.

The aggregation of a seller’s online WOM becomes its reputation (Utz et al. 2012). On business to consumer (B2C) websites, online reviews are generally on products. On consumer to consumer websites (and third-party sellers on B2C websites), seller reputation can either be aggregated from product reviews or be given by consumers separately. A high reputation may indicate a high level of seller trustworthiness, accurate product descriptions, and better services (McDonald and Slawson 2002). In general, consumers are willing to pay price premiums to sellers with better service and higher reputation (Ba and Pavlou 2002, Liu 2006, Venkatesan et al. 2006, Rabinovich et al. 2008, Li et al. 2009). There are exceptions, however; some studies find the opposite in the context of e-commerce. For example, Baylis and Perloff (2002) show that “good” internet retailers of digital cameras and scanners provide superior service and charge relatively low prices, whereas “bad” internet retailers charge relatively high prices for poor service. Ba et al. (2008) identify the “adverse price effect” and show that “low-recognition” sellers may decrease their product prices when they improve their services. Recently, Liu et al. (2012) suggest that a highreputation seller could set higher or lower prices under different conditions. Aggarwal et al. (2012) study the impact of WOM on venture financing and find that negative WOM has greater impact than positive WOM. Although reputation is based on WOM, it is a long-term and relatively static concept.

Different from these prior studies on reputation, this paper focuses more on short-term and dynamic firm strategies in response to WOM changes.

## 2.4. Firm Pricing Strategies and WOM

Firms’ use of pricing and other operations, such as recommender systems (Oestreicher-Singer and Sundararajan 2012), to influence consumer decision making is an increasingly important topic in the literature. Dou et al. (2017) study firms’ selling versus leasing models for information goods when the consumer valuation depreciates. Wathieu and Bertini (2007) argue that the posted price has a critical impact on consumers’ willingness to pay. Depending on how consumers perceive the price, a monopolistic firm should either overprice (“transgressive pricing”) or underprice (“regressive pricing”). In the preinternet era, Kalish (1985) inspected “epidemic” information diffusion and adoption through advertising and traditional offline WOM, where information from early adopters reduces uncertainty for later adopters. If there is no uncertainty, the optimal price decreases monotonically. If early adopters can generate enough information, then the price can increase, because people are willing to pay a premium for reduced uncertainty. This pioneering paper established the first study of price trajectory patterns.

With the rise of online WOM, firms’ control over available product information is significantly weakened. The literature offers several possible firm strategies related to WOM. Firms can (1) manipulate WOM directly (Dellarocas 2006, Mayzlin et al. 2014), (2) improve WOM-specific services (Adomavicius et al. 2013, Gu and Ye 2013), or (3) use pricing to influence WOM (Jiang and Chen 2007, Kuksov and Xie 2010, Li and Hitt 2010, Jing 2011, Kwark et al. 2014, Yu et al. 2016). The third strategy is most relevant to our study.

Among the studies on using price to influence WOM, Jiang and Chen (2007) examine a seller’s pricing strategy when the product can either match or mismatch a consumer’s taste. They find that it is optimal to set a low price initially to attract expert users to give more positive reviews. Li and Hitt (2010) investigate the impact of pricing on consumer reviews and find that unidimensional ratings can be substantially biased by price. Supporting this view, Chen et al. (2011) find that WOM volume and ratings are correlated with sellers’ price setup. The intuition is that some consumers want to wait for initial online reviews before making an adoption decision. This social learning allows sellers to use pricing as a mechanism to manage and manipulate initial online WOM. Jing (2011) studies the market conditions under which ex ante homogeneous consumers may delay their purchases. Because consumers are inclined to postpone adoption to make more informed purchases, the firm can lower the first-period price to attract early adopters. Similarly, Kuksov and Xie (2010), using a two-period game, explore how a firm should use frills together with price changes to affect customer ratings. Li et al. (2011) examine the repeated purchase scenario and argue that consumer reviews may intensify price competition by altering consumers’ propensity to switch among products. Yu et al. (2016) show that, via the initial price, a firm not only influences its revenue but also, controls the quality information over time.

Our study differs from these prior studies in several important ways. First, although all previous studies examine how pricing may influence WOM, we consider the mechanism through which WOM influences pricing. In previous studies, such manipulation of pricing is a strategy of second-order impact, because its influence on sales is exerted through WOM. In our paper, pricing is a strategy of first-order impact, because it directly influences profit. Bockstedt and Goh (2011) suggest that, when the market becomes more competitive, firm visibility-enhancing and quality-signaling discretionary attributes become more effective tools affecting sales, whereas seller feedback scores become less effective. Therefore, the mechanisms behind the direction of influence are fundamentally different. Second, the empirical work in our paper specifically considers and addresses the endogeneity with a difference-in-differences approach to eliminate unobservable confounding factors. Although DID designs are often used in examining demand-side causal relations, this study is perhaps the first one adopting this technique on the supply side. Third, this paper differs from previous studies in that we focus on price trajectory and dynamic pricing. Dynamic pricing is achieved owing to fast development of data analytics tools that can process WOM information in real time and the reduced cost of modifying prices according to pricing rules.

## 3. Analytical Model

Consider a firm that sells a new product to a population of consumers who are uniformly distributed in a straight line segment [0,1] with density 1.<sup>3</sup> Consumers are differentiated by their horizontal taste θ: that ${ \mathrm { i } } \mathbf { s } ,$ θ U 0, 1 . Without loss of generality, assume that the product is located at zero in this line segment.<sup>4</sup> Let C denote the misfit cost of a consumer when buying a product that is not at its ideal “location” or “fit.” Holding the product quality as a constant, on the horizontal dimension, a high misfit cost C indicates a “niche” product, because only small portions of consumers enjoy the product and their utility drops quickly as they move away from the product location. A low misfit cost C indicates that consumers’ utilities are not heavily affected by their locations, and therefore, the product is likely to be a mass market product.

Assume that all of the consumers arrive at the beginning of the game. Because consumer perceptions about the product are affected by the information available in the market and because such information updates frequently in internet businesses, we model information updating in two stages $( t = 0 , 1 )$ ), where t 0 represents the stage without any user-generated information and t 1 represents the stage when user-generated information is produced and available. In practice, when a product is first released $( t = 0 )$ , there are no online reviews, and therefore consumers make purchase decisions without such information. In the next stage (t 1), both consumers and the seller learn from consumer feedback and can form their respective strategies.

The firm sets its price $p _ { t }$ for each stage based on the distribution of consumer valuations as well as the information available in the market. More specifically, in the initial stage $( t = 0 )$ , consumers form their expectations about the product quality $( q _ { 0 } )$ without any user-generated information. Consumer utility from consuming the product in stage 0 can then be represented by $U _ { 0 } ( \theta ) = q _ { 0 } - C \theta - p _ { 0 }$ .

After consuming the product, consumers who purchase the product in stage 0 may comment on the product based on their own experiences. Such information can be viewed by the remaining consumers before they make purchase decisions in stage 1. With such user-generated information, the remaining consumers update their opinions about the product quality to be $q _ { 1 } ,$ , which can be either higher or lower than $q _ { 0 } ,$ based on the outcome of the review.

In this study, we focus on the strategies of firms and consider consumers in the simplest case. We assume that consumers are not forward looking such that they do not need to form expectations about future product reviews and product prices. Following Caminal and Vives (1996) and Liu et al. (2017), we assume that consumers can observe current prices but cannot observe the previous prices. This is because although technologies, such as price comparison and price tracking, are commonly observed nowadays $( \mathrm { e . g . }$ thetracktor.com), it remains difficult for every consumer to accurately monitor the exact price history owing to (1) sellers’ “price obfuscation” (Ellison and Ellison 2009) (for example, firms may bundle two or more products together with a single bundling price, or they may offer free shipping/low-price shipping on a product or a bundle of products, etc.), (2) firms prevention of price comparisons (Wilson 2010), or (3) the existence of “uninformed” consumers who do not search or compare (Chen and Xie 2008, Xu et al. 2011, Geng and Lee 2013).

Then, in each stage, the consumers who are indifferent between purchasing and not purchasing can be determined from $E [ U _ { t } ( \theta ) ] = 0 ;$ that is,

$$
\theta_ {t} = \left\{ \begin{array}{l l} \frac {q _ {t} - p _ {t}}{C} & \text { if } 0 <   q _ {t} - p _ {t} <   C; \\ 0 & \text { if } q _ {t} - p _ {t} \leq 0; \\ 1 & \text { if } q _ {t} - p _ {t} \geq C, \end{array} \right.\tag{1}
$$

where $t = 0 , 1$ . Based on Equation (1), the stage 0 demand of the firm is then $\theta _ { 0 } .$ , and the stage 1 demand is $\theta _ { 1 } - \theta _ { 0 }$ if $\theta _ { 1 } > \theta _ { 0 }$ and 0 otherwise.

## 3.1. The Interaction Between Price and Online Reviews

The relationship between price and online reviews is complex: on one hand, consumer reviews are affected by the stage 0 price $\left( p _ { 0 } \right)$ (Li and Hitt 2010); on the other hand, late-stage consumers’ perception about the product quality $\left( q _ { 1 } \right)$ is affected by earlier reviews and then, determines the product price in that stage. Here, we assume that consumers’ perception about the product quality in stage 1 is affected by the stage 0 consumers’ reviews (which in turn, are affected by the stage 0 product price) in the following way:

$$
q _ {1} = \left\{ \begin{array}{l l} q _ {0} + \frac {q _ {0} - p _ {0} - \mu}{C} & \text { if } p _ {0} <   q _ {0}; \\ q _ {0} & \text { if } \text { otherwise }. \end{array} \right.\tag{2}
$$

In Equation (2), the term $( q _ { 0 } - p _ { 0 } - \mu ) / C$ can be either positive or negative. It is a function of stage 0 consumer welfare and can be understood as the impact of online reviews on consumers’ stage 1 perception about the product quality. The parameter $\mu$ can be understood as the consumer “harshness,” measuring how difficult it is to satisfy a customer, given the product quality and price. The higher the $\mu ,$ the more difficult it is for a consumer to be satisfied and give a “favorable” review, and thus, the lower the perceived quality $q _ { 1 }$ in stage 1. The lower the original price, the more likely consumers are to be satisfied with the product and thus, give good reviews, which in turn, will lead to a higher stage 1 perception about the product quality. Note that this assumption is consistent with the single-dimension rating framework in both Liu et al. (2017) and Li and Hitt (2010). The rationale is that consumers would compare their utility with the price that they pay. For any given leve of utility, a lower price is associated with higher satisfaction. As a result, a lower price induces better reviews.

## 3.2. Pricing Under the In<sup>fl</sup>uence of Review Generation

The game proceeds as follows. In each stage $t ,$ the firm sets a price $p _ { t }$ based on (1) the distribution of consumer valuations in the market and (2) the quality perceived by consumers $\left( q _ { t } \right)$ , where the perceived quality in stage 1 is determined by Equation (2). Consumers decide whether to purchase based on $p _ { t }$ (as well as previous consumer reviews about the product if in stage 1). After purchase, they provide product reviews and leave the market.

We use backward induction to solve this game. The firm’s stage 1 decision problem is

$$
\max _ {p _ {1}} \pi_ {1} = \left\{ \begin{array}{l l} \Big (\frac {q _ {1} - p _ {1}}{C} - \theta_ {0} \Big) p _ {1} & \text { if } \frac {q _ {1} - p _ {1}}{C} > \theta_ {0}; \\ \text { any   price } & \text { otherwise }, \end{array} \right.\tag{3}
$$

from which we can obtain that, in equilibrium, $p _ { 1 } ^ { * } =$ $( q _ { 1 } - C \theta _ { 0 } ) / 2 \mathrm { i f } ( q _ { 1 } - p _ { 1 } ) / C > \theta _ { 0 } .$ . Plugging in $\theta _ { 0 } = ( q _ { 0 } -$ $p _ { 0 } ) / C$ and calculating the firm’s profit, we have the equilibrium profit as $\pi _ { 1 } ^ { * } = ( q _ { 0 } - ( \hat { 1 } - C ) p _ { 0 } - \mu ) ^ { 2 } / ( 4 C ^ { 3 } )$

In stage 0, knowing that the price set in stage 0 will affect consumer reviews, which will, in turn, affect consumers’ perception about the product quality in stage 1, the firm solves the following decision problem, which maximizes the total profit in the two stages:

$$
\max _ {p _ {0}} \pi_ {0} = \Big (\frac {q _ {0} - p _ {0}}{C} \Big) p _ {0} + \frac {\big (q _ {0} - (1 - C) p _ {0} - \mu \big) ^ {2}}{4 C ^ {3}}.\tag{4}
$$

Solving the optimal prices $p _ { 0 . }$ , $p _ { 1 }$ , we have the following lemmas.

Lemma 1. When $C > \frac { 1 } { 3 }$ and $\alpha < q _ { 0 } < \beta ,$

$$
\left\{ \begin{array}{l} p _ {0} ^ {*} = \frac {2 C - 1}{3 C - 1} q _ {0} + \frac {1 - C}{(1 + C) (3 C - 1)} \mu ; \\ p _ {1} ^ {*} = \max \biggl \{0, \frac {C q _ {0} - 2 C \mu}{3 C - 1} \mu \biggr \}, \end{array} \right.\tag{5}
$$

where $\begin{array} { r } { \alpha = \frac { 1 - C } { C ( 1 + C ) } \mu + 3 C - 1 } \end{array}$

$$
a n d \beta = \left\{ \begin{array}{l l} \frac {1 - C}{(1 + C) (1 - 2 C)} \mu & w h e n \frac {1}{3} <   C <   \frac {1}{2}; \\ \infty & w h e n C \geq \frac {1}{2}. \end{array} \right.
$$

Lemma 2. When $\begin{array} { r } { C < \frac { 1 } { 3 } , \ q _ { 0 } \leq \alpha , o r \ q _ { 0 } \geq \beta , } \end{array}$

$$
p _ {0} ^ {*} = \left\{ \begin{array}{l l} q _ {0} - C & \text {   if   } \frac {q _ {0}}{2} > C; \\ \frac {q _ {0}}{2} & \text {   if   otherwise;   } \end{array} \right.
$$

$$
p _ {1} ^ {*} = \left\{ \begin{array}{l l} \frac {C + 1}{4 C} q _ {0} + \frac {\mu}{2 C} & \text { if } q _ {0} > \frac {2}{C + 1} \mu ; \\ \text { anyprice } & \text { if   otherwise }, \end{array} \right.\tag{6}
$$

where in stage 0, the firm’s price is the same as the optimal price if there is only one single stage without information arrival.

It is surprising to see that, when the product quality is perceived to be very high $\left( q _ { 0 } > \beta \right)$ , the firm’s pricing strategy is the same as that when the product quality is perceived to be very low $( q _ { 0 } < \alpha ) - \mathrm { i r }$ n both cases, it is optimal to just maximize the stage 0 profit as if there is only one single stage without information arrival. This result is actually intuitive to understand. When the quality of the product is very low, no matter how much the price is cut, it is hard to generate favorable reviews; when the quality of the product is very high, consumers are willing to give favorable reviews even when the product is sold at a high price. In both cases, the firm is better off to maximize the single-stage profit without the influence of online reviews. It is possible, however, that, in stage 1, the firm cannot make any sales even with a zero price (if $q _ { 0 } \leq 1 / ( C + 1 ) \}$ ).

## 3.3. Benchmark: When There Are No Online Reviews

We are interested in the impact of online reviews on the firm’s pricing strategy. That is, how should the firm adjust its pricing to optimally make use of online reviews? To answer this question, consider a benchmark case where there are no online reviews in both stages. In this case, consumers’ stage 1 perception about the product quality is the same as that in stage 0 $( { \mathrm { i . e . , ~ } } q _ { 1 } = q _ { 0 }$ , because there is no additional information arrival). Using backward induction, the firm’s stage 2 decision problem is

$$
\max _ {p _ {1}} \pi_ {1} = \left\{ \begin{array}{l l} \Big (\frac {q _ {0} - p _ {1}}{C} - \theta_ {0} \Big) p _ {1} & \text { if } \frac {q _ {0} - p _ {1}}{C} > \theta_ {0}; \\ 0 & \text { otherwise }. \end{array} \right.\tag{7}
$$

From this, we can obtain that, in equilibrium, $p _ { 1 } ^ { * } =$ $( q _ { 0 } - C \theta _ { 0 } ) / 2$ if $( q _ { 0 } - p _ { 1 } ) / C > \theta _ { 0 }$ . Plugging in $\theta _ { 0 } = ( q _ { 0 } -$ $p _ { 0 } ) / C$ and Equation (2) and calculating the firm’s profit, we have $\pi _ { 1 } ^ { * } = ( q _ { 0 } - C \theta _ { 0 } ) ^ { 2 } / ( 4 C )$

In stage 0, the firm solves the following decision problem:

$$
\max _ {p _ {0}} = \Big (\frac {q _ {0} - p _ {0}}{C} \Big) p _ {0} + \frac {\big (q _ {0} - C \theta_ {0} \big) ^ {2}}{4 C}.\tag{8}
$$

Solving the optimal prices $p _ { 0 } ^ { b } , \ p _ { 1 } ^ { b } .$ , where the superscript b represent the benchmark case, we have

$$
p _ {0} ^ {b *} = \left\{ \begin{array}{l l} \frac {2}{3} q _ {0} & \quad \text { if } q _ {0} \leq 3 C; \\ q _ {0} - C & \quad \text { if   otherwise }; \end{array} \right.
$$

$$
p _ {1} ^ {b *} = \left\{ \begin{array}{l l} \frac {1}{3} q _ {0} & \text {if} q _ {0} \leq 3 C; \\ \text {any price} & \text {if otherwise.} \end{array} \right.\tag{9}
$$

Note that, when there are no online reviews, the stage 1 price (if there is any positive sale) is lower than the stage 0 price, the same as in a standard sequential game.

## 3.4. The Impact of Information Arrival on the Pricing Strategy

3.4.1. Impact of Information Arrival on Stage 0 Price. Comparing Equation (6) with Equation (9), we can obtain the difference in firm’s stage 0 prices attributable to information arrival through online reviews. Define $\Delta P _ { 0 } \equiv p _ { 0 } ^ { b * } - p _ { 0 } ^ { * }$ . We are interested in examining the sign of $\Delta P _ { 0 } ,$ , which indicates whether the firm has an incentive to cut its price in stage 0 to attract favorable online reviews in stage 1. We define a pricing strategy as a “price-cutting” strategy if $\Delta P _ { 0 } > 0$

Intuitively, when there exist online reviews, because the initial price of the product affects consumers’ utility and in turn, the reviews of the product, which ultimately, affect later consumers’ perception of the product, the firm has an incentive to cut its price to generate favorable online reviews. This pricecutting strategy, however, is contingent on the misfit cost as well as the product quality. For products with high misfit cost, consumers “far away” from the “ideal location” of the product are hard to satisfy, and thus, they are less likely to give good reviews. Then, the firm has less incentive to encourage these consumers to purchase the product by cutting its initial price or may even raise its price to discourage them from buying the product. Similarly, for products with very high quality, because consumers are likely to give favorable reviews even with a relatively high price, the firm does not need to lower its initial price. In summary, whether a price-cutting strategy should be adopted depends on the product characteristics (the initially perceived quality level $q _ { 0 } ,$ , for example) and how likely consumers are to give favorable reviews (misfit cost C as well as $\mu )$

Proposition 1. Compared with the benchmark case, where there are no online reviews, the firm’s pricing strategy under the influence of online reviews depends on both product characteristics and how likely consumers are to give favorable reviews $( C , q _ { 0 } ,$ , and $\mu )$

1. The firm adopts a price-cutting strategy in stage 0 (compared with the benchmark case) when the perceived quality, q<sub>0</sub>, satisfies $( 1 ) q _ { 0 } > 3 ( 1 - C ) \mu / ( 1 + C ) , \alpha < q _ { 0 } < \beta ,$ and $C > 1 / 3 \ o r \ ( 2 ) \ q _ { 0 } > 3 C$ and $C < 1 / 3 , q _ { 0 } < \alpha , o r q _ { 0 } > \beta .$

2. The firm is able to set a higher price in stage 1 than the benchmark case if consumers give good reviews relatively easily (that is, when $q _ { 0 } > 1 0 C \mu / ( 2 C + 1 ) )$ ).

Intuitively, a price-cutting strategy is helpful (Shapiro 1983, Bergemann and Valimaki 2006, Liu et al. 2017) either when the perceived quality is low (so that cutting price helps generate favorable reviews and boosts up the quality perception in stage 1) or when the misfit cost is not too large (so that the impact of favorable reviews is not too small). Proposition 1, however, shows that whether a price-cutting strategy is used is nonmonotonic in either the perceived product quality or the misfit cost. Rather, it depends on the tradeoff between the cost and the benefit of adopting a price-cutting strategy. According to Equation (2), the impact of online reviews on consumers’ stage 1 product perception is decreasing in the misfit cost. When the misfit cost is very low $( \mathrm { e . g . } ,$ $C < 1 / 3 )$ , although it is very effective for favorable reviews to enhance consumers’ quality perception, the price-cutting strategy may not be necessary if the perceived quality of the product is not too low $( q _ { 0 } > 3 C )$ and consumers are already satisfied even with a high price. When the misfit cost is higher $( C > 1 / 3 )$ , cutting price cannot effectively enhance consumers’ stage 1 perception about the product if consumers are relatively “harsh” $( q _ { 0 } < 3 ( \dot { 1 } - C ) \mu / ( 1 + C )$ . Therefore, a pricecutting strategy will be used only when it is relatively easy for consumers to offer favorable reviews $( q _ { 0 } > ^ { \cdot } ( 1 - \dot { C } ) \mu / ( 1 + C ) )$ .

Interestingly, Proposition 1 also shows that it is sometimes beneficial for the firm to charge a high stage 0 price when it expects information arrival in stage 1 when the perceived quality is either very low or very high. This is because, when the perceived quality is very low $( q _ { 0 } < \alpha )$ with an expectation of negative reviews in stage 1, it is better for the firm to give up its stage 1 profit and sell as if there is only one single stage by setting a high price in stage 0. When the perceived product quality is high $( \mathrm { e . g . } , q _ { 0 } > \beta \mu )$ the firm can also charge a high price in stage 0 without worrying about online reviews, because consumers will be satisfied by the high quality level and will offer favorable reviews even at a high price.

3.4.2. Impact of Information Arrival on Firm’s Pro<sup>fi</sup>t. Given the differences in stage 0 pricing strategies between the cases with and without information arrival, we further study how the existence of online reviews affects a firm’s profit level.

Figure 2. (Color online) Effect of Expected New Reviews on Profit  
![](/api/attachments/43ZRESQQ/fulltext/images/261fd87d6f439f3ab393b487cf0aaddf044e1b908568c75bbe6ec1f5245ce993.jpg)

Corollary 1. Compared with the benchmark case where online reviews do not exist,

1. the firm’s profits are the same with or without online reviews if the misfit cost is very low or the firm’s quality level is extremely high or extremely low: $q _ { 0 } > 3 C$ and $C < 1 / 3 , q _ { 0 } < \alpha ( \mu , C )$ , or $q _ { 0 } > \beta ( \mu , C )$

2. online reviews can either enhance or hurt the firm in terms of profit depending on the level of consumers’ misfit cost

Figure 2 illustrates the profits in different scenarios. When the misfit cost is very low, the firm’s profit is not affected by future information arrival, because it adopts a pricing strategy as if there is only one single stage. When the misfit cost is higher, it is possible that the market is not fully covered and that online reviews can possibly affect the firm profit. When the misfit cost is in the medium range, online reviews can be relatively effective in influencing consumer perceptions about the product. The firm is enticed to implement a costly price-cutting strategy. If such a cost is too high and the firm cannot make it up through future sales, online reviews hurt the firm’s profit. The lower the quality level of the product, the more likely the price-cutting strategy will hurt the firm’s profit. When the misfit cost is relatively high, the effect of a price cut in inducing favorable reviews is limited, and therefore, the firm does not need to implement the costly price-cutting strategy. Interestingly, it can even charge a high initial price to prevent unwanted consumers who are likely to offer unfavorable reviews from purchasing the product. In this case, the presence of online reviews helps the firm, although the higher the misfit cost is, the less significant the impact of online reviews.

3.4.3. Effect of Information Arrival on the Price Trend over Time. Proposition 1 shows the impact of in formation arrival on the firm’s pricing strategy. Note that setting a lower price in stage 0 than in the benchmark case does not necessary imply that we will observe an upward price trend over time. It is possible that the stage 1 price is lower than the stage 0 price even with an initial price-cutting strategy, if the online reviews are not sufficiently favorable to boost up the price, or if it sells too many products in stage 0 and the remaining consumers’ valuations are not sufficiently high. Define the price change between the two stages as $\Delta P \equiv p _ { 1 } ^ { * } - p _ { 2 } ^ { * }$ . Proposition 2 studies the firm’s prices over the two stages through the sign of ΔP.

![](/api/attachments/43ZRESQQ/fulltext/images/544a7dfe9c2e79267f186e0979c543a498ca7b3577fd430e3118e11d981fb2b9.jpg)

Proposition 2. Expecting that consumers will be influenced by online reviews, the firm’s stage 0 price is higher than the stage 1 price in the following scenarios:

1. when $C < 1 / 3 \colon ( C - 1 ) q _ { 0 } + 2 \mu > 0 , q _ { 0 } > \beta , o r \ q _ { 0 } < \alpha ,$

2. when $1 / 3 < C < 1 : q _ { 0 } < ( 2 C ^ { 2 } + C + 1 ) \mu / ( ( 1 - C ) ( 1 + C ) ) ,$

3. when $C > 1$

We illustrate Proposition 2 in Figure 3, where the arrows show the upward or downward price trend in each region defined based on the misfit cost and quality. Combining Propositions 1 and 2, we can see that, even with a price-cutting strategy, we can observe a downward price trend. Similarly, even when the firm raises its price in stage 0, we may still observe an upward price trend. The firm is able to set a higher stage 1 price when it induces sufficiently favorable online reviews, but this may (when $C < 1 / 3$ and $q _ { 0 } <$ $( 2 C ^ { 2 } + C + 1 ) \mu / ( ( 1 - C ) ( 1 + C ) ) )$ or may not (when C < $1 / 3$ and $( C - 1 ) q _ { 0 } + 2 \mu > 0 )$ be because of an initial low price. An upward price trend can occur if the product quality is so high that consumers give good reviews even when the product is sold at a high initial price.

Similarly, a downward price trend can be observed either because it is not able to generate favorable online reviews (when $C < 1 / 3$ and $( C - 1 ) q _ { 0 } + 2 \mu < 0 )$ or because consumers have a sufficiently high misfit cost $( C > 1 )$ such that the impact of online reviews is limited and the firm either does not need to cut its price in stage 0 or only needs a very limited price cut.

Figure 3. (Color online) Price Change from Stage 0 to Stage 1  
![](/api/attachments/43ZRESQQ/fulltext/images/3087dce9e300a8461e505f224e173babb7be6612c08b8e91de89893094b437d6.jpg)

In summary, a downward price trend can be observed even when the firm initially sets a low price, and an upward price trend can be observed even when the firm has a high initial price. The arrival of information enriches the pricing literature about penetration and skimming pricing in the literature (Shapiro 1983, Noble and Gruca 1999, Bergemann and Valimaki 2006, Hotler and Armstrong 2012).

## 4. Empirical Support

Our analytical model suggests that the seller has different optimal pricing strategies in response to product reviews given differences in product quality and consumers’ misfit cost. In this part, we empirically examine whether such a phenomenon exists in practice.

## 4.1. Testable Hypotheses

We focus on companies’ pricing strategy along with the change of market information. In the analytical model, the change of market information is simplified to two stages, where the second stage has more information than the first stage. Empirically, a product’s market information can be reflected in the product description and consumer reviews, where consumer reviews are the part that changes in most cases. In this research, we use the number of reviews as a proxy of the market information that can help consumers better understand the product and examine how price changes with the change of the number of reviews.

As shown in Figure 3, the relationship between price and number of reviews has different characteristics in the zones defined by different quality and misfit cost. Based on the analytical propositions, we make the following hypotheses.

Hypothesis 1a. A firm would increase its price with the increase of number of reviews when product quality is low and misfit cost is low.

Hypothesis 1b. A firm would reduce its price with the increase of number of reviews when product quality is high and misfit cost is low.

Hypothesis 2a. A firm would reduce its price with the increase of number of reviews when product quality is low and misfit cost is medium.

Hypothesis 2b. A firm would increase its price with the increase of number of reviews when product quality is high and misfit cost is medium.

Hypothesis 3a. A firm would reduce its price with the increase of number of reviews when product quality is low and misfit cost is high.

Hypothesis 3b. A firm would reduce its price with the increase of number of reviews when product quality is high and misfit cost is high.

## 4.2. Data

In this study, we use data on books to test the hypotheses. Books are chosen, because they are an experience with both a product quality dimension and a consumer taste dimension that matches well with our theoretical model. Moreover, books have unified International Standard Book Number (ISBN) identifications that allow us to match entries on different websites to build an econometric model.

We collect a panel data set of matched books from Amazon and BN.<sup>6</sup> We choose five categories of books on Amazon for data collection (contemporary fiction, general science, international politics, investing, and pregnancy & childbirth) and collect price and review information every three days during the period from July 13, 2010 to November 7, 2010. Because of the limitations of Amazon’s application programming interface, we could not collect all items from each category. Instead, we collect the most popular books and latest books in these five categories to a maximum number that is allowed by Amazon and then, find the corresponding items at BN. In our data set, some popular books are old (up to 55 years old). Because the pricing and sales of these books may be quite different from relatively newer books, we keep only the books published within five years of the time of data collection. To have a stable observation of price, we keep items with at least 10 price records. It is also necessary to have both review and sales rank records on both websites to implement the empirical study. After data cleaning, we have a total of 1,095 books in 40 periods. In this paper, we conduct the analysis on books with one-, three-, and five-year histories for robustness tests.

Because of the great variations in prices, we do not directly use price as the dependent variable. We normalize prices by defining a variable called pricerate, which is an item’s sale price divided by its vendor-provided list price (i.e., pricerate = 1 <sup>−</sup> percentage discount). This operation absorbs many factors that may explain price differences across items. One major factor that affects product pricing is sales volume. We follow previous studies and use logRank = ln(Sales Rank) to proxy for sales volume (Brynjolfsson et al. 2003). In addition, we use the number of consumer reviews and average rating to characterize the online WOM. Because the distribution of the number of reviews is highly skewed, we use logNReview = ln(Nreview + 1) to represent review volume.

## 4.3. General Setup of the DID Model

Although this paper studies the impact of online reviews on the supply side of products, the endogeneity problem that plagues the demand side continues to pose empirical challenges. We develop a DID model by extending Chevalier and Mayzlin (2006) to rule out possible endogenous factors. In the DID model, the first difference of the model is across the two websites; thus, we are able to remove observable and unobservable productlevel characteristics. The second difference is on dif ferent times of a product’s lifecycle through panel data analysis; therefore, we are able to control for timevarying factors that influence both websites. We adopt a fixed effect model to estimate the model parameters. We are cautious and always conduct poolability and Hausman tests to make sure that the fixed effect model is appropriate for our data set.

To explain the setup of the DID model, let us look at the impact of determinants X on the dependent variable pricerate. We can build two models on seller A (Amazon) or B (BN), respectively, in the tth time period after item i is on the market. If we assume a one-period time lag between the independent and dependent variables, the model is

$$
\begin{array}{r} p r i c e r a t e _ {i, t} ^ {A; B} = \lambda_ {\tau} + \psi_ {i} + \eta_ {i, t - 1} + \phi^ {A; B} + \zeta_ {\tau} ^ {A; B} + \nu_ {t - 1} ^ {A; B} \\ + \mu_ {i} ^ {A; B} + \mathbf {X} _ {i, t - 1} ^ {A; B} \Gamma^ {A; B} + \epsilon_ {i, t} ^ {A; B}, \end{array}\tag{10}
$$

where the variable τ is the calendar date corresponding to t for product i. The variable $\lambda _ { \tau }$ captures marketlevel effects, such as the macroeconomic environment and the seasonal price changes. The variable $\psi _ { i }$ is a product time-invariant effect, which may be caused by the nature of the product, such as author or product quality. The variable $\eta _ { i , t - 1 }$ is a product time-variant effect, such as the discount caused by product lifecycle. The variables $\phi ^ { A }$ and $\phi ^ { B }$ are website-specific time-invariant effects, such as price differences caused by their supply chains or targeted markets. The variables $\zeta _ { \tau } ^ { A }$ and $\dot { \zeta } _ { \tau } ^ { B }$ are website time-variant effects, such as website-specific promotions. The variables $\nu _ { t - 1 } ^ { A }$ and $\nu _ { t - 1 } ^ { B }$ are website-level strategies to promote products according to their lifecycle. (This strategy is the same across products but changes with respect to t.) The variables $\bar { \mu } _ { i } ^ { A }$ and $\mu _ { i } ^ { B }$ are product-website time-invariant effects, such as websitelevel special offers for certain types of products. The variables $\mathbf { \boldsymbol { x } } _ { i , t - 1 } ^ { A ; B }$ are our focal independent variables that vary across time, products, and websites. The remaining variables are random noise terms for the two websites, $\varepsilon _ { i , t - 1 } ^ { A }$ and $\varepsilon _ { i , t - 1 } ^ { B } .$ , which may include product-website time-varying effects.

With this model setup, the time dimension is the age of products on the market. Thus, the variable $\eta _ { i , t - 1 }$ captures the possible price change if there is no extra information over time and if price is decided solely based on product lifecycle. By taking the differences across the two websites, we can eliminate the impact, the seasonality effect, and the unobserved product quality effect shared by the two websites. We get the following model:

$$
\begin{array}{r l} & {\Delta p r i c e r a t e _ {i, t} = p r i c e r a t e _ {i, t} ^ {A} - p r i c e r a t e _ {i, t} ^ {B}} \\ & {\qquad = \phi + \zeta_ {\tau} + \nu_ {t - 1} + \mu_ {i} + \mathbf {X} _ {i, t - 1} ^ {A} \Gamma^ {A} - \mathbf {X} _ {i, t - 1} ^ {B} \Gamma^ {B} + \varepsilon_ {i, t},} \end{array}\tag{11}
$$

where $\phi = \phi ^ { A } - \phi ^ { B } , \zeta _ { \tau } = \zeta _ { \tau } ^ { A } - \zeta _ { \tau } ^ { B } , \nu _ { t - 1 } = \nu _ { t - 1 } ^ { A } - \nu _ { t - 1 } ^ { B } ,$ $\mu _ { i } = \mu _ { i } ^ { A } - \mu _ { i } ^ { B } .$ , and $\varepsilon _ { i , t - 1 } = \varepsilon _ { i , t - 1 } ^ { A } - \varepsilon _ { i , t - 1 } ^ { B }$ . In the second difference of the DID model, the variables $\phi$ and $\zeta$ would be captured by the time fixed effects. In addition, we also incorporate dummy variables on product age to $\nu ,$ and $\mu$ is captured by item fixed effects. After this operation, we are able to obtain the coefficients for $\dot { \mathbf { X } } _ { i , t - 1 } ^ { A ; B }$

Similar to Chevalier and Mayzlin (2006), we use a two-way panel model with time fixed effects to conduct the second differencing with respect to time. After this differencing, the parameter estimates Γ will give us unbiased estimates of the effects of online review arrival on price.

4.4. The Impact of Market Information on Book Price In our econometric model, we consider the number of reviews as the independent variable that is a proxy for market information that helps consumers better understand the product. Moreover, in a traditional dynamic pricing model, a seller would inspect the sales volume of a product $( \mathrm { i . e . , }$ , demand) when making changes to pricing. Thus, we capture sales volume using control variables $l o g R a n k _ { i , t - 1 } ^ { A ; B ^ { \star } } .$ We also control the online product reviews valence $R a t i n g _ { i , t - 1 } ^ { A ; B } ,$ reflecting consumers perception of the product. We modify Equation (11) to

$$
\begin{array}{r l} \Delta p r i c e r a t e _ {i, t} & = \beta_ {1} l o g N R e v i e w _ {i, t - 1} ^ {A} + \beta_ {2} l o g N R e v i e w _ {i, t - 1} ^ {B} \\ & \quad + \gamma_ {1} l o g R a n k _ {i, t - 1} ^ {A} + \gamma_ {2} l o g R a n k _ {i, t - 1} ^ {B} \\ & \quad + \gamma_ {3} R a t i n g _ {i, t - 1} ^ {A} + \gamma_ {4} R a t i n g _ {i, t - 1} ^ {B} \\ & \quad + \phi + \zeta_ {\tau} + \nu_ {t - 1} + \mu_ {i} + \varepsilon_ {i, t}. \end{array}\tag{12}
$$

According to the analytical model’s prediction, the impact of market information (number of reviews) on product pricing depends on consumers’ misfit costs and product quality. For book quality, we use the Amazon rating at the end of our data collection period as an indicator of product quality $( Q u a l i t y ) . ^ { 8 }$ We create an interaction between Quality and number of reviews to capture quality’s effect and modify Equation (12) to

$$
\begin{array}{r l} \Delta p r i c e r a t e _ {i, t} = & \beta_ {1} l o g N R e v i e w _ {i, t - 1} ^ {A} + \beta_ {2} l o g N R e v i e w _ {i, t - 1} ^ {B} \\ & + \beta_ {3} Q u a l i t y _ {i} \cdot l o g N R e v i e w _ {i, t - 1} ^ {A} \\ & + \beta_ {4} Q u a l i t y _ {i} \cdot l o g N R e v i e w _ {i, t - 1} ^ {B} \\ & + \gamma_ {1} l o g R a n k _ {i, t - 1} ^ {A} + \gamma_ {2} l o g R a n k _ {i, t - 1} ^ {B} \\ & + \gamma_ {3} R a t i n g _ {i, t - 1} ^ {A} + \gamma_ {4} R a t i n g _ {i, t - 1} ^ {B} \\ & + \phi + \zeta_ {\tau} + \mu_ {i} + \nu_ {t - 1} + \varepsilon_ {i, t}. \end{array}\tag{13}
$$

For misfit cost, following Sun (2012), we use the standard deviation of user ratings on BN in our data collection period to represent book misfit cost. A higher variance means that the book is niche and that misfit cost is higher. To ensure that the measurement on standard deviation is valid, we restrict the analysis to products with more than five ratings, resulting in 430 books. The rating standard deviation of these books ranges from 0 to 2.67 with a bell shape. Because the analytical model predicts that misfit cost’s effect varies in three levels, we incorporate a quadratic variable of misfit cost and create interactions between it and other independent variables in Equation (13):

$$
\begin{array}{r l} \Delta p r i c e r a t e _ {i, t} = & \beta_ {1} l o g N R e v i e w _ {i, t - 1} ^ {A} + \beta_ {2} l o g N R e v i e w _ {i, t - 1} ^ {B} \\ & + \beta_ {3} Q u a l i t y _ {i} \cdot l o g N R e v i e w _ {i, t - 1} ^ {A} \\ & + \beta_ {4} Q u a l i t y _ {i} \cdot l o g N R e v i e w _ {i, t - 1} ^ {B} \\ & + \beta_ {5} l o g N R e v i e w _ {i, t - 1} ^ {A} \cdot M i s f i t _ {i} \\ & + \beta_ {6} l o g N R e v i e w _ {i, t - 1} ^ {B} \cdot M i s f i t _ {i} \\ & + \beta_ {7} Q u a l i t y _ {i} \cdot l o g N R e v i e w _ {i, t - 1} ^ {A} \cdot M i s f i t _ {i} \\ & + \beta_ {8} Q u a l i t y _ {i} \cdot l o g N R e v i e w _ {i, t - 1} ^ {B} \cdot M i s f i t _ {i} \\ & + \beta_ {9} l o g N R e v i e w _ {i, t - 1} ^ {A} \cdot M i s f i t _ {i} ^ {2} \\ & + \beta_ {1 0} l o g N R e v i e w _ {i, t - 1} ^ {B} \cdot M i s f i t _ {i} ^ {2} \\ & + \beta_ {1 1} Q u a l i t y _ {i} \cdot l o g N R e v i e w _ {i, t - 1} ^ {A} \cdot M i s f i t _ {i} ^ {2} \\ & + \beta_ {1 2} Q u a l i t y _ {i} \cdot l o g N R e v i e w _ {i, t - 1} ^ {B} \cdot M i s f i t _ {i} ^ {2} \\ & + \gamma_ {1} l o g R a n k _ {i, t - 1} ^ {A} + \gamma_ {2} l o g R a n k _ {i, t - 1} ^ {B} \\ & + \gamma_ {3} R a t i n g _ {i, t - 1} ^ {A} + \gamma_ {4} R a t i n g _ {i, t - 1} ^ {B} \\ & + \phi + \zeta_ {\tau} + \mu_ {i} + \nu_ {t - 1} + \varepsilon_ {i, t}. \end{array}\tag{14}
$$

## 4.5. Results

Table 1 shows the summary statistics of our data set. There are 40 time periods of data in the two data sets.

Table 1. Descriptive Statistics for the Time Period November 7, 2011 on Books

<table><tr><td></td><td>n</td><td>Mean</td><td>Standard deviation</td></tr><tr><td> $Price^A$ </td><td>1,021</td><td>1,692.23</td><td>1,772.37</td></tr><tr><td> $Price^B$ </td><td>1,021</td><td>1,830.53</td><td>1,731.75</td></tr><tr><td>ListPrice</td><td>1,021</td><td>2,368.52</td><td>2,351.01</td></tr><tr><td> $pricerate^A$ </td><td>1,021</td><td>0.73</td><td>0.13</td></tr><tr><td> $pricerate^B$ </td><td>1,021</td><td>0.79</td><td>0.10</td></tr><tr><td> $Rank^A$ </td><td>1,021</td><td>261,336.40</td><td>531,589.50</td></tr><tr><td> $Rank^B$ </td><td>996</td><td>181,516.60</td><td>193,772.60</td></tr><tr><td> $logRank^A$ </td><td>1,021</td><td>11.02</td><td>2.07</td></tr><tr><td> $logRank^B$ </td><td>996</td><td>11.18</td><td>1.83</td></tr><tr><td> $Rating^A$ </td><td>1,019</td><td>4.26</td><td>0.61</td></tr><tr><td> $Rating^B$ </td><td>1,021</td><td>4.14</td><td>0.82</td></tr><tr><td> $NReview^A$ </td><td>1,021</td><td>82.88</td><td>295.20</td></tr><tr><td> $NReview^B$ </td><td>1,021</td><td>64.87</td><td>495.46</td></tr><tr><td> $logNReview^B$ </td><td>1,021</td><td>3.07</td><td>1.43</td></tr><tr><td> $logNReview^B$ </td><td>1,021</td><td>2.03</td><td>1.53</td></tr></table>

Table 2. Reviews’ Impact on Book Price

<table><tr><td rowspan="2"></td><td colspan="2">Main result</td><td colspan="2">Subsample</td><td colspan="2">Amazon standard deviation as misfit</td></tr><tr><td>Coefficient</td><td>Standard error</td><td>Coefficient</td><td>Standard error</td><td>Coefficient</td><td>Standard error</td></tr><tr><td> $logRank_{t-1}^{A}$ </td><td>0.003**</td><td>(0.001)</td><td>0.004**</td><td>(0.002)</td><td>0.003***</td><td>(0.001)</td></tr><tr><td> $logRank_{t-1}^{B}$ </td><td>-0.004**</td><td>(0.002)</td><td>-0.003</td><td>(0.002)</td><td>-0.009***</td><td>(0.003)</td></tr><tr><td> $Rating_{t-1}^{A}$ </td><td>0.010</td><td>(0.008)</td><td>0.011</td><td>(0.012)</td><td>0.020*</td><td>(0.012)</td></tr><tr><td> $Rating_{t-1}^{B}$ </td><td>0.005</td><td>(0.005)</td><td>-0.004</td><td>(0.005)</td><td>0.003</td><td>(0.006)</td></tr><tr><td> $logNReview_{t-1}^{A}$ </td><td>-0.188*</td><td>(0.096)</td><td>-0.348*</td><td>(0.193)</td><td>0.124</td><td>(0.107)</td></tr><tr><td> $logNReview_{t-1}^{B}$ </td><td>-0.006</td><td>(0.397)</td><td>0.906*</td><td>(0.523)</td><td>0.023</td><td>(0.067)</td></tr><tr><td> $Quality \cdot logNReview_{t-1}^{A}$ </td><td>0.062**</td><td>(0.026)</td><td>0.107**</td><td>(0.047)</td><td>-0.023</td><td>(0.024)</td></tr><tr><td> $Quality \cdot logNReview_{t-1}^{B}$ </td><td>-0.003</td><td>(0.094)</td><td>-0.246**</td><td>(0.125)</td><td>-0.005</td><td>(0.015)</td></tr><tr><td> $logNReview_{t-1}^{A} \cdot Misfit$ </td><td>0.671**</td><td>(0.264)</td><td>0.784*</td><td>(0.453)</td><td>0.421</td><td>(0.874)</td></tr><tr><td> $logNReview_{t-1}^{B} \cdot Misfit$ </td><td>-0.040</td><td>(0.565)</td><td>-1.484**</td><td>(0.733)</td><td>-1.974**</td><td>(0.805)</td></tr><tr><td> $Quality \cdot logNReview_{t-1}^{A} \cdot Misfit$ </td><td>-0.187***</td><td>(0.066)</td><td>-0.228**</td><td>(0.108)</td><td>-0.175</td><td>(0.204)</td></tr><tr><td> $Quality \cdot logNReview_{t-1}^{B} \cdot Misfit$ </td><td>0.017</td><td>(0.133)</td><td>0.400**</td><td>(0.175)</td><td>0.554***</td><td>(0.210)</td></tr><tr><td> $logNReview_{t-1}^{A} \cdot Misfit^{2}$ </td><td>-0.330*</td><td>(0.178)</td><td>-0.262</td><td>(0.273)</td><td>-1.576</td><td>(1.538)</td></tr><tr><td> $logNReview_{t-1}^{B} \cdot Misfit^{2}$ </td><td>0.012</td><td>(0.210)</td><td>0.531**</td><td>(0.262)</td><td>6.089**</td><td>(2.446)</td></tr><tr><td> $Quality \cdot logNReview_{t-1}^{A} \cdot Misfit^{2}$ </td><td>0.090**</td><td>(0.043)</td><td>0.079</td><td>(0.063)</td><td>0.549</td><td>(0.387)</td></tr><tr><td> $Quality \cdot logNReview_{t-1}^{B} \cdot Misfit^{2}$ </td><td>-0.005</td><td>(0.049)</td><td>-0.141**</td><td>(0.062)</td><td>-1.708**</td><td>(0.677)</td></tr><tr><td colspan="7">Coefficients of dummy variables on seasonal effect omitted</td></tr><tr><td>Number of items</td><td>430</td><td></td><td>253</td><td></td><td>871</td><td></td></tr><tr><td>Number of data points</td><td>12,895</td><td></td><td>6,684</td><td></td><td>26,823</td><td></td></tr><tr><td> $R^{2}$ </td><td>0.813</td><td></td><td>0.833</td><td></td><td>0.777</td><td></td></tr><tr><td> $Adj-R^{2}$ </td><td>0.796</td><td></td><td>0.808</td><td></td><td>0.764</td><td></td></tr></table>

\*p < 0.1; \*\*p < 0.05; \*\*\*p < 0.01.

We only provide a summary of the last period for illustration. The table contains variables Price (in cents), pricerate, Rank (sales rank), logRank, Rating, NReview, and logNReview. In general, Amazon prices are lower than BN prices. Amazon generally has more reviews than BN. The average rating levels on Amazon and BN are similar.

The empirical results of the model are reported in Table 2. In building the model, we calculate robust standard errors with clustering at individual item level to control for potential heteroskedasticity and withincluster correlation in error terms.<sup>9</sup> The coefficients on control variables are consistent with prior studies. Sales rank has a significant impact on price. For example, the sales rank coefficient for Amazon is positive and statistically significant, suggesting that there is a negative relation between demand and price. If the sales of a book are higher (sales rank is lower), the retailer will have room to reduce the price.<sup>10</sup>

As predicted by the analytical model, the response of the seller’s price to the market information (number of reviews) varies with misfit cost and product quality. In our main model, Amazon Reviews’ effects are significant on all of the related variables. Figure 4 illustrates the joint effects of these variables. In the figure, we vary the values of quality and misfit cost to create different combinations of zones. Within each zone, we calculate the coefficient on logNReview to make the color of the zone, where positive coefficients are colored red and negative coefficients are colored blue. We also put up arrows and down arrows to annotate the direction of the correlations. We find that the visualization of the empirical results perfectly matches with the major part of the analytical model’s predictions in Figure 3.

First, when books’ misfit cost is low (the standard deviation of BN ratings is less than 1.8 according to the quadratic variable’s curve) and book quality is low, product price increases with the availability of more market information. In other words, sellers tend to take a price penetration strategy and set a low initial price to gain positive reviews, and later, they raise the price to gain profit. When book quality is high, product price decreases with market information, which thus shows the price-skimming effect. Hypotheses 1a and 1b are supported.

Figure 4. (Color online) The Relationship Between Price and Number of Reviews Under Different Quality and Misfit Costs  
![](/api/attachments/43ZRESQQ/fulltext/images/3c9fb9e539004a9bbc4546552db6cac6ef3adaf0e499faac328b14d8c6939168.jpg)

Second, when misfit cost is relatively high (when the standard deviation of BN ratings is greater than or equal to 1.8), sellers tend to increase price for highquality products, taking advantage of the previously accumulated reviews. For low-quality products, sellers tend to set a high price initially to grab the possibly interested buyers to gain profits. Hypotheses 2a and 2b are supported.

Limited by the data set that we have, we do not fully capture the effect if misfit cost continues to increase in our empirical analysis (there are only 20 products with higher than 2.1 standard deviation of the BN rating in our data set). Thus, we do not empirically observe the theoretical prediction that both high-quality and lowquality products will take a price-skimming strategy on high misfit cost. However, our empirical analysis generally offers supporting evidence to the theoretical predictions.

To alleviate the concern about unobservable website-product factors that may affect the results, we conduct the same analysis on a subsample with similar demand across websites as a robustness check. We select products that have a similar number of reviews on the two websites; specifically, the number of reviews on one website is not more than three times the number of reviews on the other website. The subsample accounts for about 35.5% of the entire data. The descriptive statistics of the sample are reported in Online Appendix 3. The results of the regression are reported in the second column of Table 2. As we can see, the signs of the coefficients of the two samples are consistent, except that BN reviews’ effects become significant.

As another robustness check, we use the standard deviation of Amazon ratings as a measure of misfit cost. The major problem of using this measure is that Amazon reports the average rating, which essentially smooths their variations. However, its standard deviation still has a correlation with the standard deviation of individual ratings and a relative value in indicating the misfit cost. We restrict the misfit cost calculation to products with more than five ratings, resulting in 871 books with the Amazon rating standard deviation ranging from 0 to 0.7 with a bell shape. The results of the robustness check are reported as the third column in Table 2. As we can see, the Amazon-related variables are not significant, because misfit cost essentially is based on Amazon information. However, the signs of the significant coefficients of BN variables are consistent with the first robustness check and consistent with the coefficients on Amazon variables in the main results. In Online

Appendix 3, we also illustrate the joint effect of quality and misfit cost on the relationship between price and number of reviews.<sup>11</sup> As we can see, it is very much consistent with our main result, with the cutoff of low and medium misfit cost becoming 0.35.

In the model, we use quadratic terms of misfit cost to capture the nonlinear relations between variables. One may be concerned that the quadratic term may have multicollinearity with the main term. To address this concern, we mean centered misfit cost and repeated the experiments as a robustness check. Although the numerical values of regression coefficients changed slightly, we find that the general results are consistent and that the findings remain valid.

## 5. Conclusion

This paper argues that sellers can use online product reviews to develop better pricing strategies. We first build a theoretical model to examine a seller’s optimal pricing strategy when online WOM information is taken into consideration. Without con sumer reviews or the WOM effect, the optimal price should go down over time owing to reduced demand. With consumer reviews, online WOM’s effect on pricing depends on both the consumer characteristics (such as misfit cost) and product characteristics (such as product quality). We find that online reviews have a nonmonotonic impact on a firm’s pricing strategy as well as on a firm’s profit in the dimensions of both product quality and misfit cost. Surprisingly, the impact of online reviews is quite limited when the product quality is at an extreme (extremely high or extremely low) or when the misfit cost is very low. Expecting future information arrival (online reviews), the firm can either use a pricecutting strategy or raise its stage 0 price. The price adjustment strategy is sufficiently sophisticated such that we can no longer conclude whether a priceskimming or penetration strategy is adopted just from observing an upward or downward price trend. That is, when there is information arrival such that the firm can dynamically change the prices, prior pricing insights from static models no longer hold. Predictions of the analytical models are supported by evidence from our empirical study. Extending prior studies on the price effects on reviews (Li and Hitt 2010, Yu et al. 2016), we show empirical evidence of reviews’ impact on pricing strategies used by market leaders.

Online product reviews are arguably one of the most easily accessible sources of marketing data for online retailers. It is possible to build analytical tools to learn consumers’ opinions from online WOM. Few prior studies examine this strategic variable in pricing. We fill this gap by developing a theoretical model to address firms’ optimal dynamic pricing problem with a unified framework that features quality uncertainty, risk aversion, and online product reviews. Because menu cost is practically trivial for online retailers and because it is not difficult to program automatic price changes based on live feeds of online review data, sellers should be able to adopt similar pricing strategies and respond rapidly to online reviews.

Our work can be improved on in several ways. First, we only examine the case when the seller has sufficient market power to change its price. Consequently, our results are applicable only to dominant players in various markets. Small retailers may not have such power to influence price and therefore, will not be able to adopt the strategies suggested in this paper. In an extension in the online appendix, we examine a case where two firms are competing. A possible future direction would be to study a fully competitive market and examine followers’ strategies under the influence of dominant players. Second, this research only examines the seller’s pricing decision assuming zero marginal production cost. Future work can also look at the case when the costs of producing/acquiring the products are nonzero and examine how such cost influences the seller’s price adjustments in the presence of online reviews. Third, the theoretical model has only two stages. Although we believe that it successfully captures the key features of the market for relatively new products, it is desirable to examine multiple stages of products lifecycles in future studies. Such models may offer a more nuanced view of learning, competition, and strategic reactions and make it possible to extend our empirical study to a longer term. Fourth, by taking a DID framework, our empirical model makes assumptions about the commonalities of two websites pricing strategies in considering the product’s lifecycle and the unobservable product-website timevarying factors to be random and independent and identically distributed In the future, with more detailed data from the sellers, it is possible to build more sound econometric models to capture the different factors’ impacts in a more accurate manner. Fifth, the products that we examined are physical books, which can be quite different from other products/services. However, our theoretical model does not have assumptions on product categories and is general enough to offer insights for other products/services as well. For virtual products, such as ebooks or online videos, with lower marginal cost and reduced complexity of logistics, the results obtained are likely to carry over. Additional empirical analysis should be conducted to verify the results for other products, such as home appliances, restaurants, and so forth. Sixth, other than modeling manipulating online reviews through price adjustments, this paper does not consider other forms of review manipulations, such as fake reviews. We believe that examining the impact of such “fake reviews” on firm pricing is a promising future direction.

Finally, even with the empirical evidence of such dynamic pricing strategies, we have to caution the reader that the strategies derived from our theoretical model may not have been adopted by practitioners. The reason is that we cannot rule out the possibility that these book sellers could obtain the information from other channels, such as traditional offline WOM and firm-initiated market research, etc. However, clearly information acquisition from online WOM is cheaper and timelier compared with these more traditional channels. To this end, consistency between our empirical findings and the theoretical predictions should offer support for firms to explore the application of such strategies in more settings.

## Endnotes

<sup>1</sup> See http://www.theguardian.com/world/2013/sep/23/new-york -fake-online-reviews-yoghurt. Accessed January 2019.

<sup>2</sup> See http://www.cnet.com/news/hotels-500-fine-policy-for-bad -reviews-gets-low-marks/. Accessed January 2019.

<sup>3</sup> In this paper, we examine firm pricing in a monopoly setting. We provide the formulation of a duopoly problem in Online Appendix 1. Our initial results indicate that, although firms have less incentive to invest in price-cutting strategies to induce good reviews, they may still end up cutting prices significantly when the competition is fierce.

<sup>4</sup> This is to facilitate the comparison with the duopoly case.

<sup>5</sup> All proofs of the lemmas and propositions are in Online Appendix 2. <sup>6</sup> In this study, the data collected from Amazon are for products sold by Amazon, not those sold by third-party sellers.

<sup>7</sup> As discussed in previous research, there is a linear correlation between log sales rank and sales volume. The coefficient may vary across websites. In our model, this difference is absorbed in the mode coefficients.

<sup>8</sup> Note that the smallest Amazon rating increment is 0.5. In our data set, the ratings range between 1.5 and 5.

<sup>9</sup> Clustering at the Amazon book category level yields similar significant results.

<sup>10</sup> The dependent variable of the DID model is the price difference between Amazon and BN. Because the left-hand side variable is Amazon minus BN, the opposite signs of variables on the two websites mean the same direction of effect. Note that we do not study the price difference in this research. Through the differencing, we are able to extract the unbiased effect of information arrival (through online reviews) on price.

<sup>11</sup> Because the significant coefficients are all on BN reviews, the figure corrects the sign to reflect the relationship between price and review increase.

## References

Adomavicius G, Bockstedt JC, Curley SP, Zhang JJ (2013) Do recommender systems manipulate consumer preferences? A stud of anchoring effects. Inform. Systems Res. 24(4):956–975.

Aggarwal R, Gopal R, Gupta A, Singh H (2012) Putting money where the mouths are: The relation between venture financing

and electronic word-of-mouth. Inform. Systems Res. 23(3): 976–992.

Alba JW, Mela CF, Shimp TA, Urbany JE (1999) The effect of discount frequency and depth on consumer price judgments. J. Consume Res. 26(2):99–114.

Archak N, Ghose A, Ipeirotis PG (2011) Deriving the pricing power of product features by mining consumer reviews. Management Sci. 57(8):1485–1509.

Athey S, Bagwell K (2008) Collusion with persistent cost shocks. Econometrica 76(3):493–540.

Ba S, Stallaert J, Zhang ZJ (2008) Oligopolistic price competition and adverse price effect in online retailing markets. Decision Support Systems 45(4):858–869.

Ba SL, Pavlou PA (2002) Evidence of the effect of trust building technology in electronic markets: Price premiums and buyer behavior. Management Inform. Systems Quart. 26(3):243–268.

Baylis K, Perloff JM (2002) Price dispersion on the Internet: Good firms and bad firms. Rev. Indust. Organ. 21(3):305–324.

Bergemann D, Valimaki J (2006) Dynamic pricing of new experience goods. J. Political Econom. 114(4):713–743.

Berger J, Sorensen AT, Rasmussen SJ (2010) Positive effects of negative publicity: When negative reviews increase sales. Marketing Sci. 29(5):815–827.

Bertsimas D, Perakis G (2006) Dynamic Pricing: A Learning Approach (Springer, Boston).

Bickart B, Schindler RM (2011) Internet forums as influential sources of consumer information. J. Interactive Marketing 15(3):31–40.

Bockstedt J, Goh KH (2011) Seller strategies for differentiation in highly competitive online auction markets. J. Management Inform. Systems 28(3):235–267.

Brynjolfsson E, McAfee A (2014) The Second Machine Age: Work Progress, and Prosperity in a Time of Brilliant Technologies (WW Norton & Company, New York).

Brynjolfsson E, Smith M (2000) Frictionless commerce? A comparison of Internet and conventional retailers. Management Sci. 46(4): 563–585.

Brynjolfsson E, Hu YJ, Smith MD (2003) Consumer surplus in the digital economy: Estimating the value of increased product variety at online booksellers. Management Sci. 49(11):1580–1596.

Caminal R, Vives X (1996) Why market shares matter: An information-based theory. RAND J. Econom. 27(2):221–239.

Chen Y, Xie J (2008) Online consumer review: Word-of-mouth as a news element of marketing communication mix. Management Sci. 54(3):477–491.

Chen Y, Fay S, Wang Q (2011) The role of marketing in social media: How online consumer reviews evolve. J. Interactive Marketing 25(2):85–94.

Chevalier JA, Mayzlin D (2006) The effect of word of mouth on sales: Online book reviews. J. Marketing Res. 43(3):345–354.

Chintagunta PK, Gopinath S, Venkataraman S (2010) The effects of online user reviews on movie box office performance: Accounting for sequential rollout and aggregation across local markets. Marketing Sci. 29(5):944–957.

Davenport TH (2006) Competing on analytics. Harvard Bus. Rev. 84(1): 98–107.

Dellarocas C (2003) The digitization of word of mouth: Promise and challenges of online feedback mechanisms. Management Sci. 49(10):1401–1424.

Dellarocas C (2006) Strategic manipulation of Internet opinion forums: Implications for consumers and firms. Management Sci. 52(10):1577–1593.

Dellarocas C, Zhang X, Awad NF (2007) Exploring the value of online product reviews in forecasting sales: The case of motion pictures. J. Interactive Marketing 21(4):23–45.

Dou Y, Hu YJ, Wu DJ (2017) Selling or leasing? Pricing information goods with depreciation of consumer valuation. Inform. Systems Res. 28(3):585–602.

Duan W, Gu B, Whinston AB (2008) Do online reviews matter? - An empirical investigation of panel data. Decision Support System 45(4):1007–1016.

Elberse A, Eliashberg J (2003) Demand and supply dynamics for sequentially released products in international markets: The case of motion pictures. Marketing Sci. 22(3):329–354.

Ellison G, Ellison SF (2009) Search, obfuscation, and price elasticities on the Internet. Econometrica 77(2):427–452

Erdem T, Keane MP, Sun B (2008) A dynamic model of brand choice when price and advertising signal product quality. Marketing Sci. 27(6):1111–1125.

Fan M, Tan Y, Whinston AB (2005) Evaluation and design of online cooperative feedback mechanisms for reputation management. IEEE Trans. Knowledge Data Engrg. 17(2):244–254.

Farias VF, Van Roy B (2010) Dynamic pricing with a prior on market response. Oper. Res. 58(1):16–29.

Forman C, Ghose A, Wiesenfeld B (2008) Examining the relationship between reviews and sales: The role of reviewer identity dis closure in electronic markets. Inform. Systems Res. 19(3):291–313.

Geng X, Lee Y-J (2013) Competing with piracy: A multichannel sequential search approach. J. Management Inform. Systems 30(2): 159–184.

Ghose A, Ipeirotis PG (2011) Estimating the helpfulness and economic impact of product reviews: Mining text and reviewer characteristics. IEEE Trans. Knowledge Data Engrg. 23(10): 1498–1512.

Godes D, Mayzlin D (2004) Using online conversations to study word-of-mouth communication. Marketing Sci. 23(4):545–560.

Gu B, Ye Q (2013) First step in social media: Measuring the influence of online management responses on customer satisfaction. Production Oper. Management 23(4):570–582.

Hotler P, Armstrong G (2012) Principles of Marketing, 14th ed. (Prentice Hall, Upper Saddle River, NJ).

Hu N, Liu L, Zhang J (2008) Do online reviews affect product sales? the role of reviewer characteristics and temporal effects. Inform. Tech. Management 9(3):201–214.

Hu N, Pavlou PA, Zhang J (2009) Overcoming the J-shaped distri bution of product reviews. Comm. ACM 52(10):144–147.

Hui S, Bradlow E, Fader P (2009a) Testing behavioral hypotheses using an integrated model of grocery store shopping paths. J. Consumer Res. 36(3):478–493.

Hui S, Fader P, Bradlow E (2009b) Path data in marketing: An integrative framework and prospectus for model-building. Marketing Sci. 28(2):320–335.

Jiang B, Chen P (2007) An economic analysis of online product reviews and ratings. Working paper, Washington University in St. Louis, St. Louis.

Jing B (2011) Social learning and dynamic pricing of durable goods. Marketing Sci. 30(5):851–865.

Kalish S (1985) A new product adoption model with price, adver tising, and uncertainty. Management Sci. 31(12):1569–1585.

Kohavi R, Rothleder NJ, Simoudis E (2002) Emerging trends in business analytics. Comm. ACM 45(8):45–48.

Krishna A, Feinberg FM, Zhang ZJ (2007) Should price increases be targeted? Pricing power and selective vs. across-the-board price increases. Management Sci. 53(9):1407–1422.

Kuksov D, Xie Y (2010) Pricing, frills, and customer ratings. Marketing Sci. 29(5):925–943.

Kwark Y, Chen J, Raghunathan S (2014) Online product reviews: Implications for retailers and competing manufacturers. Inform. Systems Res. 25(1):93–110

Kwark Y, Lee GM, Pavlou P, Qiu L (2016) The spillover effects of usergenerated online product reviews on purchases: Evidence from clickstream data. Proc. Internat. Conf. Inform. Systems (AIS, Atlanta).

Lee J, Park D-H, Han I (2008) The effect of negative online consumer reviews on product attitude: An information processing view. Electronic Commerce Res. Appl. 7(3):341–352.

Lee TY, BradLow ET (2011) Automated marketing research using online customer reviews. J. Marketing Res. 48(5):881–894.

Lewis M (2005) Research note: A dynamic programming approach to customer relationship pricing. Management Sci. 51(6): 986–994.

Li J, Zhan L (2011) Online persuasion: How the written word drives wom evidence from consumer-generated product reviews. J. Advertising Res. 51(1):239–257.

Li S, Srinivasan K, Sun B (2009) Internet auction features as quality signals. J. Marketing 73(1):75–92.

Li X, Hitt LM (2008) Self-selection and information role of online product reviews. Inform. Systems Res. 19(4):456–474.

Li X, Hitt LM (2010) Price effects in online product reviews: An analytical model and empirical analysis. Management Inform. Systems Quart. 34(4):809–831.

Li X, Hitt LM, Zhang ZJ (2011) Product reviews and competition in markets for repeat purchase products. J. Management Inform. Systems 27(4):9–41.

Liu Y (2006) Word of mouth for movies: Its dynamics and impact on box office revenue. J. Marketing 70(3):74–89.

Liu Y, Feng J, Liao X (2017) When online review meet sales volume information: Is more or accurate information always better. Inform. Systems Res. 28(4):723–743.

Liu Y, Feng J, Wei KK (2012) Negative price premium effect in online market: The impact of competition and buyer informativeness on the pricing strategies of sellers with different reputation. Decision Support Systems 54(1):681–690.

Mayzlin D, Dover Y, Chevalier J (2014) Promotional reviews: An empirical investigation of online review manipulation. Amer. Econom. Rev. 104(8):2421–2455.

McDonald CG, Slawson CV (2002) Reputation in an Internet auction market. Econom. Inquiry 40(4):633–650.

Mehra A, Bala R, Sankaranarayanan R (2012) Competitive behaviorbased price discrimination for software upgrades. Inform. Sys tems Res. 23(1):60–74.

Moe W, Fader P (2004a) Capturing evolving visit behavior in clickstream data. J. Interactive Marketing 18(1):5–19.

Moe W, Fader P (2004b) Dynamic conversion behavior at e-commerce sites. Management Sci. 50(3):326–335.

Moe W, Trusov M (2011) The value of social dynamics in online product ratings forums. J. Marketing Res. 48(3):444–456.

Mudambi SM, Schuff D (2010) What makes a helpful online review? a study of customer reviews on amazon. com. Management Inform. Systems Quart. 34(1):185–200.

Noble P, Gruca T (1999) Industrial pricing: Theory and managerial practice. Marketing Sci. 18(3):435–454.

Oestreicher-Singer G, Sundararajan A (2012) Recommendation networks and the long tail of electronic commerce. Management Inform. Systems Quart. 36(1):65–83.

Pan Y, Zhang JQ (2011) Born unequal: A study of the helpfulness of user-generated product reviews. J. Retailing 87(4):598–612.

Pathak B, Garfinkel R, Gopal RD, Venkatesan R, Yin F (2010) Empirical analysis of the impact of recommender systems on sales. J. Management Inform. Systems 27(2):159–188.

Rabinovich E, Maltz A, Sinha RK (2008) Assessing markups, service quality, and product attributes in music cds’ Internet retailing. Production Oper. Management 17(3):320–337.

Rusmevichientong P, Salisbury JA, Truss LT, Van Roy B, Glynn PW (2006) Opportunities and challenges in using online preference data for vehicle pricing: A case study at general motors. J. Revenue Pricing Management 5(1):45–61.

Samiei P, Tripathi AK (2014) Effect of social networks on online reviews. Proc. Hawaii Internat. Conf. System Sci. (IEEE, Piscataway, NJ), 1444–1453.

Shapiro C (1983) Optimal pricing of experience goods. Bell J. Econom 14(2):497–507.

Shen W, Hu YJ, Ulmer JR (2015) Competing for attention: An empirical study of online reviewers’ strategic behavior. Management Inform. Systems Quart. 39(3):683–696.

Stigler GJ (1964) A theory of oligopoly. J. Political Econom. 72(1):44C61.

Su X (2007) Intertemporal pricing with strategic customer behavior. Management Sci. 53(5):726–741.

Sun M (2012) How does the variance of product ratings matter? Management Sci. 58(4):696–707.

Sun M, Zhang X(M), Zhu F (2019) U-shaped conformity in online social networks. Marketing Sci. 38(3):461–480.

Trusov M, Bucklin RE, Pauwels K (2009) Effects of word-of-mouth vs. traditional marketing: Findings from an internet social networking site. J. Marketing 73(5):90–102.

Utz S, Kerkhof P, van den Bos J (2012) Consumers rule: How consumer reviews influence perceived trustworthiness of online stores. Electronic Commerce Res. Appl. 11(1):49–58.

Venkatesan R, Mehta K, Bapna R (2006) Understanding the confluence of retailer characteristics, market characteristics and online pricing strategies. Decision Support Systems 42(3):1759–1775.

Villas-Boas JM (2004) Consumer learning, brand loyalty, and com petition. Marketing Sci. 23(1):134–145.

Wang C, Zhang X(M) (2009) Sampling of information goods. Decision Support Systems 48(1):14–22.

Wang C, Zhang X(M), Hann I-H (2018) Socially nudged: A quasiexperimental study of friends’ social influence in online product ratings. Inform. Systems Res. 29(3):641–655.

Wathieu L, Bertini M (2007) Price as a stimulus to think: The case for willful overpricing. Marketing Sci. 26(1):118–129.

Wernerfelt B (1986) A special case of dynamic pricing policy. Man agement Sci. 32(12):1562–1566.

Wilson CM (2010) Ordered search and equilibrium obfuscation. Internat. J. Indust. Organ. 25(5):496–506.

Wu F, Huberman BA (2008) How public opinion forms. Papadimitriou C, Zhang S, eds. Internet and Network Economics—WINE 2008, Lecture Notes in Computer Science, vol. 5385 (Springer, Berlin, Heidelberg), 334–341.

Xu L, Chen J, Whinston A (2011) Price competition and endogenous valuation in search advertising. J. Marketing Res. 48(3):566–586.

Ye S, Gao G, Viswanathan S (2014) Strategic behavior in online reputation systems: Evidence from revoking on ebay. Manage ment Inform. Systems Quart. 38(4):1033–1056.

Yu M, Debo L, Kapuscinski R (2016) Strategic waiting for consumergenerated quality information: Dynamic pricing of new expe rience goods. Management Sci. 62(2):410–435.

Zhang J, Craciun G, Shin D (2010) When does electronic word-ofmouth matter? A study of consumer product reviews. J. Bus. Res. 63(12):1336–1341.

Zhang X(M), Feng J (2011) Cyclical bid adjustments in search-engine advertising. Management Sci. 57(9):1703–1719

Zhang X(M), Zhu F (2011) Group size and incentives to contribute: A natural experiment at chinese wikipedia. Amer. Econom. Rev. 101(4):1601–1615.

Zhao H (2000) Raising awareness and signaling quality to uninformed consumers: A price advertising model. Marketing Sci. 19(4):390–396.

Zhu F, Zhang X(M) (2010) Impact of online consumer reviews on sales: The moderating role of product and consumer characteristics. J. Marketing 74(2):133–148.
