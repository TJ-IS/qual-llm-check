---
otero_id: 4084
otero_key: "KEVY3VW4"
title: "Price of Identical Product with Gray Market Sales: An Analytical Model and Empirical Analysis"
authors: "Zhongju Zhang; Juan Feng"
year: "2017"
journal: "Information Systems Research"
doi: "10.1287/isre.2017.0692"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Information Systems Research

## HSR

![](/api/attachments/KEVY3VW4/fulltext/images/621fb083102342e005d763c92615c33f60e26f60032c0c063548e4b1540faeaf.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

## Price of Identical Product with Gray Market Sales: An Analytical Model and Empirical Analysis

Zhongju Zhang, Juan Feng

To cite this article:

Zhongju Zhang, Juan Feng (2017) Price of Identical Product with Gray Market Sales: An Analytical Model and Empirical Analysis. Information Systems Research

Published online in Articles in Advance 07 Apr 2017

http://dx.doi.org/10.1287/isre.2017.0692

Full terms and conditions of use: http://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

Copyright © 2017, INFORMS

Please scroll down for article—it is on subsequent pages

![](/api/attachments/KEVY3VW4/fulltext/images/e4d81dcfcb2128d0842285a88fe18e7674c7c2907e423f9d24577906fa7ea4df.jpg)

INFORMS is the largest professional society in the world for professionals in the fields of operations research, management science, and analytics.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# Price of Identical Product with Gray Market Sales: An Analytical Model and Empirical Analysis

Zhongju Zhang,<sup>a</sup> Juan Feng<sup>b</sup>

<sup>a</sup> W. P. Carey School of Business, Arizona State University, Tempe, Arizona 85287; <sup>b</sup> City University of Hong Kong, Kowloon, Hong Kong Contact: zhongju.zhang@asu.edu (ZZ); juafeng@cityu.edu.hk (JF)

Received: October 20, 2014 Revised: October 29, 2015; August 26, 2016 Accepted: November 16, 2016 Published Online in Articles in Advance: April 7, 2017

https://doi.org/10.1287/isre.2017.0692

Copyright: © 2017 INFORMS

Abstract. The sale of genuinely branded products through unauthorized channels (also known as gray markets) is a growing problem for many firms that operate in separate markets. It is generally believed that the existence of such unauthorized sales will cannibalize the profits of brand owners. In this paper, we develop a pricing model for a firm that sells an identical product in two distinct markets but faces the threat of potential gray market sales. The firm chooses prices in each market. A consumer chooses whether to buy the product from one of the markets including a gray market. We derive the optimal prices in the two markets and examine their efects on consumer demand and the total profit. We show that the higher price in one market transfers part of its demand into the gray market, thus influencing the consumer demand in the low-priced market as well. Additionally, the price gap between the two separate markets positively influences gray market sales and, under certain conditions, can lead to an increase in firm profit. Using authorized sales data from a Fortune 100 company and a separate data set on online gray market sales, we find empirical evidence in support of our model results.

History: Vĳay Mookerjee, Senior Editor; Ming Fan, Associate Editor.

Funding: The second author acknowledges support from the General Research Fund from the University Grants Committee in Hong Kong [Grant 9042133], the Strategic Research Grant from the City University of Hong Kong [Grant 7004118], and the National Natural Science Foundation of China [Grant 71401148].

Keywords: gray markets • unauthorized channels • market leakage • price discrimination

## 1. Introduction

In a networked economy where information on prices for identical products across diferent distribution channels is easy to obtain, gray (or grey) markets (also known as unauthorized markets) boom. Gray markets refer to the trade of genuinely branded merchandise through distribution channels that, while legal, are unauthorized or unintended by the trademark owner (Duhan and Shefet 1988, Bucklin 1993). In other words, price is the only major diference for the same product sold across diferent channels. Gray markets take place in both online marketplaces (e.g., eBay, Taobao) and traditional brick-and-mortar stores. In a series of recent high-profile lawsuits on copyright infringement between manufacturers and retailers (Costco, Walmart), U.S. courts ruled in favor of the (unauthorized) retailers, who can continue to sell goods at lower prices (Barrett 2013, Stohr 2013, Post 2015). Gray markets exist because there is a significant price diference in how the same product is sold in diferent markets/regions. The price diference allows arbitrage opportunities in which the product can be bought from the low-priced market and then resold in the more expensive market at a profit.

The phenomenon of the gray market is not new (Hilke 1987, Lipner 1990). In the past, many well-known companies found their products sold in the gray market. These products range across various industries, including electronics, automobiles, fashion, pharmaceuticals, computer hardware, and games (Duhan and Shefet 1988). According to KPMG, the value of gray market products in the information technology (IT) sector alone averaged \$58 billion in 2007.<sup>1</sup>

This issue was exacerbated in recent years, for the most part, by the rise of e-commerce and online trade platforms that bring manufacturers, suppliers, consumers, exporters, and importers into one marketplace. This IT-enabled marketplace provides transparent product information (e.g., price, model number), drastically reduces consumer search and transaction costs, and achieves significant economies of scale (Shapiro and Varian 1998). The ability to shop online overseas, fueled by better and faster technology, growing numbers of low-cost smartphones in the emerging world, more robust global retail platforms, and simpler, more secure payment options (Walsh and Marcus 2013), is transforming the buying behaviors of consumers who are driven by lower price, better quality, and brand authenticity. Haitao or daigou, practices that involve cross-border shopping from overseas markets, have boomed in China (Swanson 2014). Nielsen and PayPal estimates that the Chinese cross-border shopping market alone will increase to \$161 billion by 2018.

While gray market sales might be attractive to consumers, retailers, and online trade platform providers, they can significantly influence the bottom line of manufacturers and brand owners. Many multinational firms have claimed that their domestic sales are being illegally undercut. An analysis by Deloitte in 2009 reported that imports of gray market products to the United States cost manufacturers as much as \$63 billion in sales a year. Additionally, gray market sales can have other negative impacts such as the loss of profit margins, erosion of the brand name, and damaged relationships with authorized distributors (Assmus and Wiese 1995). As a result, firms have been taking a number of measures to control gray market activities (Palia and Keown 1991). These include price coordination methods (Assmus and Wiese 1995), a framework based on sensing, speed, and severity (Antia et al. 2004), and dynamic quantity discounts (Su and Mukhopadhyay 2012).

Online commerce platform providers are also under pressure to curb unauthorized vendors and clean up the gray market in the online marketplace. Alibaba, the Chinese e-commerce company, rolled out an incentive in February 2014 to attract brand owners to open their own oficial stores on Alibaba’s Tmall<sup>2</sup> (Chu and Chiu 2014). However, a simple comparison of the price for the same product on the oficial Tmall store and that on the store overseas still reveals a large diference in prices.<sup>3</sup> Kucher and Simon (1995) argued that if prices of the same product in diferent markets converge, that will reduce the chance for arbitrage and eliminate gray market players. With such huge price diferences, however, it will be dificult to clear away gray market sales.

In our empirical analysis of estimating demand (see Section 5) for two popular electrical products for a Fortune 100 company, we observed an upward-slope demand curve.<sup>4</sup> This deviates from the so-called “law of demand” in the traditional economic literature. We argue that this phenomenon, even though conceptually counterintuitive, can be explained reasonably well from the perspective of unauthorized gray market sales. The more interesting questions, in our view, are why the brand owner practices drastically diferent pricing schemes for the same product sold across separate markets, how the prices in separate markets influence consumer demand, and if there is economic incentive for the brand owner to use diferent pricing schemes.

In this paper, we develop a pricing scheme for a firm that sells an identical product in two distinct markets but faces the threat of potential gray market sales. The firm chooses prices in each market. A consumer chooses whether to buy the product from one of the markets including a gray market. We derive the optimal prices in the two markets and examine their efects on consumer demand and the total profit. We show that the higher price in one market transfers part of the consumer demand into the gray market, thus influencing the demand in the low-priced market as well. Additionally, the price gap between the two separate markets positively influences gray market sales and, under certain conditions, can lead to an increase in firm profit. We note that brand owners should be cognizant of various strategies in terms of price discrimination and channel coordination when it comes to gray market sales of their products.

The rest of this paper is organized as follows. After reviewing relevant literature in Section 2, we develop an analytic model where a firm sells an identical product in two distinct markets in Section 3. We analyze the case when the two markets are completely independent as well as that when there is leakage between the two markets; i.e., consumers in one market are aware of the other and are allowed to buy through an unauthorized channel. In Section 4, we discuss several model extensions including a situation where a retailer enters the market and two scenarios where the market leakage is endogenized. In Section 5, we present our data and empirical models. We discuss the mechanism that helps explain our empirical findings. Section 6 concludes and discusses the limitations of the study as well as directions for future research.

## 2. Literature Review

The pricing of (either physical or information) products has long been studied in the literature. It is well known that product discrimination, if possible, enhances the profit of a seller as well as social welfare (Varian 1985, Tirole 1988, Stole 2007). In general, price discrimination requires the seller to be able to either perfectly identify each individual consumer (first-degree discrimination) or design diferent pricing schemes to diferentiate consumers based on quantity purchased (second-degree price discrimination) or consumer groups (such as senior discounts, thirddegree price discrimination; Tirole 1988).

Price discrimination has also been broadly classified (McAfee 2008) as direct price discrimination (based on geographic areas, nationality, age, employer, etc.) or indirect price discrimination (such as quantity discount, coupons, bundling, nonlinear pricing, etc.). Direct price discrimination may be dificult to maintain in the face of arbitrage, where consumers ofered lower prices buy large quantities of a firm’s goods and sell these goods to other consumers who face higher prices. Therefore, many firms engage in indirect price discrimination practices. Generally speaking, indirect price discrimination refers to a setting where a menu of options (involving price and other features of a product) is ofered and consumers selfselect which option is the best for them (McAfee 2008). Literature in this area abounds, on topics ranging from coupons (Kumar and Rajan 2012) and quantity discounts (Weng 1995) to more drastic measures involving product diferentiation (e.g., Tirole 1988, Vandenbosch and Weinberg 1995, Ba et al. 2010). Empirical studies (e.g., Brynjolfsson and Smith 2000, Ancarani and Shankar 2004, Ba et al. 2012) have found evidence of persistent and widespread price dispersion (variation) for identical products in both online and of-line markets.

As discussed earlier, the gray market is the result of direct price discrimination across geographic regions (nations) by a single brand owner. The price diference for the same product is not intended to be exploited by consumers and/or retailers. Traditionally, this is not a serious concern as the markets for the same product are separated geographically. Additionally, under U.S. copyright law, copyright holders are granted the exclusive right to reproduce and sell their copyrighted goods. However, copyrighted goods, once sold lawfully to a buyer, are no longer subject to the exclusive right of the original copyright holder (Mortimer 2007). These products can then be resold according to the “first sale doctrine,” which has been cited as providing the legal basis for such markets as video rentals and resales of books and paintings (Mortimer 2007, Stohr 2013). The recent court ruling backing gray market sales (Stohr 2013, Post 2015) was a huge victory for consumers and will further fuel the growth of gray market activities.

A number of policy-oriented reviews have examined the issue of parallel trade from the perspectives of intellectual property, copyrights, and law (e.g., Hilke 1987, Duhan and Shefet 1988). Most of the technical papers consider parallel trade in the context of price discrimination (Szymanski and Valletti 2005). Ahmadi and Yang (2000) develop a sequential game-theoretical model where parallel importers can enter the higher priced market and set their price and quantity after observing the manufacturer’s prices in both countries. The authors show that, under some circumstances, the manufacturer should embrace parallel imports because they may actually increase the manufacturer’s profits. In separate studies, Gerstner and Holthausen (1986) and Raf and Schmitt (2007) also demonstrate that there are circumstances under which it benefits a manufacturer to allow retailers to engage in parallel trade. Autrey and Bova (2012) examine the gray market from a tax perspective and show that domestic tax revenues are higher under certain conditions. Xiao et al. (2011) study various channel structures. They show that a manufacturer can benefit from parallel importation by a third party or by an authorized dealer, and the channel structure is critical in determining the benefits.

It is worth noting some of the empirical studies in this arena. One stream of research (Myers 1999, Antia et al. 2006) attempted to assess the causes of parallel trade. Another stream of empirical studies focused on the economic implications of price discrimination on profits, consumer welfare, and eficiency, but stopped short because data on the quantity of unauthorized sales are dificult to observe and collect (Verboven 2008). Leslie (2004) examined monopoly price discrimination including both second-degree and third-degree price discrimination. Using data from a Broadway play, the author found that direct price discrimination can actually improve the firm’s profit, relative to the uniform pricing. Maskus and Chen (2002) tried to empirically test a few propositions derived from a model of vertical distribution and parallel imports, but did so indirectly using international wholesale prices from a single manufacturer. Using a panel data of digital cameras traded on an Internet shopbot, Thompson (2009) showed that the presence of parallel imports significantly lowers prices across markets.

## 3. The Model

A firm is selling an identical product in two separate markets (for example, the global market and the domestic market). Because of the disparity in factors such as consumer purchase power and exchange rate, the firm charges diferent prices $p _ { i } ( i = 1 ,$ 2 and $p _ { 2 } > p _ { 1 } )$ in the two markets. Consumers are heterogeneous in their valuations or willingness to pay, which are assumed to follow a uniform distribution. More specifically, the consumer valuation in market 1 is U<sup>[</sup>0, 1<sup>]</sup> and that in market 2 is U<sup>[</sup>V, W<sup>]</sup>, where $W > 1 . ^ { 5 }$ Additionally, let λ denote the density of market 2, so that the total market size for market 2 can be represented as $\lambda ( W - V )$ . The utility function of a consumer with valuation v is given by $u = v - p ,$ , where $p$ is the price of the product. Consumers with $u \geq 0$ will buy one unit of the product, and those with $u < 0$ will choose not to buy. The firm needs to choose prices $p _ { 1 }$ and $p _ { 2 }$ such that the total profit from both markets is maximized.

We first consider a benchmark situation where there is no leakage between the two markets; i.e., consumers in one market are not aware of the existence of the other market or have no access to the product in the other market. In this case, the firm will charge monopoly prices in each market to maximize profit. Given $p _ { 1 }$ and ${ \displaystyle p _ { 2 } , }$ it is straightforward to show that the demand in market 1 is $\bar { D } _ { 1 } = 1 - p _ { 1 }$ and the demand in market 2 is $D _ { 2 } = \lambda \operatorname* { m i n } \{ W - p _ { 2 } , W - V \}$ . Therefore, the firm’s problem, assuming the marginal cost is zero, can be written as

$$
\max _ {p _ {1}, p _ {2}} \pi = p _ {1} D _ {1} + p _ {2} D _ {2}.
$$

The optimal prices can be derived as

$$
p _ {1} ^ {*} = \frac {1}{2} \quad \text { and } \quad p _ {2} ^ {*} = \left\{ \begin{array}{l l} W / 2 & \text { if   } W \geq 2 V, \\ V & \text { otherwise }. \end{array} \right.
$$

At optimal prices, the total profit for the firm can be represented as

$$
\pi_ {b} ^ {*} = \left\{ \begin{array}{l l} (1 + \lambda W ^ {2}) / 4 & \text { if } W \geq 2 V, \\ \frac {1}{4} + \lambda (W - V) V & \text { otherwise }. \end{array} \right.\tag{1}
$$

Now, let us consider the situation where the same product is available through an unauthorized channel (gray market) in addition to the two authorized markets. The existence of the gray market has two impacts on consumers. First, when consumers in market 2 (with a higher price) become aware of the price diference, they have the incentive to explore the possibility of buying the product through the unauthorized channel with a lower price, but may be subject to some uncertainties. Let γ represent the probability that a consumer in market 2 would switch over to buy from the gray market. In other words, among those who originally purchase in market 2, a percentage of γ consumers would buy from the gray market.

Additionally, the existence of the gray market also has an impact on consumers who could not aford to buy the product previously. A portion of these consumers can now choose to purchase the product. Let φ represent the probability that a consumer (who could not aford to purchase from her own market previously) can now buy the product from the gray market. The price of the product in the gray market is given by $p _ { u } = p _ { 1 } + \delta$ , where δ represents the extra cost (on top of $p _ { 1 } )$ associated with searching, shipping, traveling, and the import/export process. Obviously, $p _ { u } > p _ { 1 }$ because $\delta > 0$

Here, we do not explicitly model the existence and the utilities of resellers in the gray market. This is not uncommon in the context of IT-enabled marketplaces $( \mathrm { e . g . }$ , Taobao, AmazonGlobal, WeChat). In recent years, cross-border shopping on these marketplaces has become a common practice. Some daigou shops on Taobao provide direct cross-border shopping services for consumers by charging them a fixed percentage of commission (e.g., 30% of the lower product price). An individual in the high-priced market can also ask her friend to buy the product from the lowpriced market and ship (or bring) it back to her. In Section 4, we extend the analysis to a situation where a reseller can enter the high-priced market. The reseller sets the price premium (δ) to maximize her profit in the gray market.

Below we present the solutions when the following conditions hold:

$$
\delta <   \frac {2 (1 - \gamma) (W - 1) + (\phi - \gamma) (1 + \lambda W)}{(1 - \gamma) (4 + \lambda (1 + \gamma + \phi)) - \lambda (1 - \phi)}
$$

and

(i)

$$
\begin{array}{r l} W > & \left(\lambda (1 - \phi) ^ {2} (\delta - V) + (1 - \gamma) \right. \\ & \quad \cdot [ (4 + \lambda (1 + \gamma + 2 \phi)) V - (4 + \lambda + \lambda \gamma) \delta - 2 ] \\ & \quad \cdot (\lambda (1 - \gamma) (\gamma + \phi)) ^ {- 1}. \end{array} \tag {5}\tag{ii}
$$

Condition (i) ensures that the price of the product in the gray market is less than that in market $2 \left( p _ { u } < p _ { 2 } \right)$ Condition (ii) ensures that the high-priced market is not fully covered and some consumers will choose not to buy from any market. When condition (i) fails, the gray market will not exist. Hence, no attempt is made to address the violation of condition (i) in this paper. When condition (ii) does not hold, market 2 is completely covered. Consumer demand in the gray market will change slightly and so will the total demand<sup>6</sup> in market 1. The optimal solutions can be obtained in a similar fashion and analytical results presented below still hold.

With unauthorized channels, the consumer demand in market 2 can be represented by $D _ { 2 } = \lambda ( 1 - \gamma ) ( W - p _ { 2 } )$ In market 1, the demand includes the “original” portion of consumers $( 1 - p _ { 1 } )$ from market 1, as well as those consumers $D _ { u } = \lambda \gamma ( W - p _ { 2 } ) + \lambda \phi ( p _ { 2 } - p _ { 1 } - \delta )$ who purchase through the unauthorized channel. The first term of $D _ { u }$ represents the consumers who originally purchase from market 2 (but now switch to the gray market), and the second term represents those who would not have purchased if there were no gray market. The total consumer demand in market 1 is therefore $D _ { 1 } = ( 1 - p _ { 1 } ) + \lambda \gamma ( W - p _ { 2 } ) + \lambda \phi ( p _ { 2 } - p _ { 1 } - \delta )$

It should be pointed out that $\gamma$ and $\phi$ together capture the severity of the sales “leakage” to the gray market. Two extreme cases can arise. When $\gamma = \phi = 0 .$ , this case subsumes to the benchmark where the two markets are completely separated and there is no leakage. When $\gamma = \phi \neq 0$ , the consumer demand in market 1 becomes $\overset { \cdot } { D _ { 1 } } = ( 1 - p _ { 1 } ) + \lambda \gamma ( W - p _ { 1 } - \delta )$ , which is independent of the cross-channel price $p _ { 2 }$ . In this case as well, the firm charges the static “monopoly” price in each market, yet taking into account the proportion of consumers switching over from market $\bar { 2 }$ to market 1. In the following, we analyze the scenario where $\phi \neq \gamma$ It is also entirely possible that the magnitude of the market leakage (captured by γ and $\phi )$ could depend on some internal parameters; $\mathrm { e . g . }$ , the consumer valuation v or the price diference $p _ { 2 } - p _ { 1 }$ between the two markets. We examine these scenarios in Section 4.

Note that $\partial D _ { 1 } / \partial p _ { 1 } = - ( 1 + \lambda \phi ) < 0$ and $\partial D _ { 1 } / \partial p _ { 2 } =$ $\lambda ( \phi - \gamma )$ , but $\partial D _ { 2 } / \partial p _ { 1 } = 0$ and $\partial D _ { 2 } / \partial p _ { 2 } = - \lambda ( 1 - \gamma ) < 0$ In other words, as the price of the product in its own channel increases, consumer demand for the product in each market will decrease. As the product price in the cross channel changes, only the consumer demand in the low-priced market will change. Furthermore, how it changes depends on the net efect of the consumers buying from the gray market. Therefore:

Lemma 1. Consumer demand, $D _ { 1 } ,$ , in the low-priced market exhibits own- as well as cross-channel price sensitivity. It decreases as its own-channel price, $p _ { 1 } ,$ increases, but increases (decreases) as the cross-channel price, $\displaystyle p _ { 2 } ,$ increases when $\phi > \gamma \ ( \phi < \gamma )$ .

The own-channel price sensitivity is easy to understand. The cross-channel price sensitivity, however, depends on who switches to purchase from unauthorized channels $( \phi$ and $\gamma )$ . Intuitively, when the price of a product (for example, the Burberry watch) in the more expensive Chinese market $\left( { { p } _ { 2 } } \right)$ increases, some of the consumers in the Chinese market will switch to purchase from unauthorized channels. Thus, the consumer demand for the same watch in the U.S. market will rise because of the potential gray market opportunities. However, if more high-valuation consumers (with respect to the low ones) in the Chinese market switch $( \mathrm { e . g . } , \gamma > \phi )$ , the firm in the U.S. market may need to respond by increasing her own-channel price $\left( { { p } _ { 1 } } \right)$ , resulting in decreased overall consumer demand in the U.S. market $( D _ { 1 } )$ . Either situation could lead to discontented customers and policy changes in the lowpriced market 1. For instance, strict limits have been put into place in certain markets (Hong Kong, Britain) on the amount of products that can be carried out of the territory (Wong 2013, Swanson 2014).

Given that the two key forces at play are the market 2 consumers that switch to the gray market and the new customers that enter because of the presence of the gray market, it is meaningful to examine how the gray market sales $D _ { u }$ will respond to price changes in the authorized channels. It is clear that $\partial D _ { u } / \partial p _ { 1 } = - \lambda \phi < 0$ and $\partial D _ { u } / \partial p _ { 2 } = \lambda ( \phi - \gamma )$ , which depend on the magnitude of market leakage φ and $\gamma .$ .

Lemma 2. Consumer demand through unauthorized channels, $D _ { u } ,$ decreases as the price $p _ { 1 }$ in market 1 increases, and increases (decreases) as the price $p _ { 2 }$ in market 2 increases when $\phi > \gamma \ ( \phi < \gamma )$

Lemma 2 implies that when the price gap between the two markets narrows (either through an increase in $p _ { 1 }$ or a decrease in $p _ { 2 } ) _ { \cdot }$ , gray market sales will drop.<sup>7</sup> This is consistent with the literature (Assmus and Wiese 1995) that advocates using price coordination mechanisms to address gray market threat.

The firm’s total profit when there are unauthorized sales can be presented as

$$
\begin{array}{r l} \max _ {p _ {1}, p _ {2}} \pi_ {u} & = [ (1 - p _ {1}) + \lambda \gamma (W - p _ {2}) + \lambda \phi (p _ {2} - p _ {1} - \delta) ] p _ {1} \\ & \quad + \lambda (1 - \gamma) p _ {2} (W - p _ {2}), \end{array} \tag {2}
$$

where the first term represents the profit from market 1 including the unauthorized channel, and the second term represents the profit from market 2. Solving from the set of first-order equations simultaneously and noting that the Hessian is negative definite,<sup>8</sup> we get

$$
\begin{array}{l} p _ {1} ^ {*} = \frac {(1 - \gamma) [ 2 + \lambda \gamma W + \lambda \phi (W - 2 \delta) ]}{(1 - \gamma) [ 4 + \lambda (1 + \gamma + 2 \phi) ] - \lambda (1 - \phi) ^ {2}} \text {and} \\ p _ {2} ^ {*} = \frac {W (1 - \gamma) (2 + \lambda \phi + \lambda \gamma) + (\phi - \gamma) (1 + \lambda W - \lambda \delta \phi)}{(1 - \gamma) [ 4 + \lambda (1 + \gamma + 2 \phi) ] - \lambda (1 - \phi) ^ {2}}. \end{array}\tag{3}
$$

Below we examine how the optimal prices will change with various model parameters. All proofs are given in the appendix.

Lemma 3. The optimal prices in the two markets, $p _ { i } ^ { * } ,$ , exhibit the following properties:

• both $p _ { i } ^ { * } s$ increase with W, the consumer valuation of the product in market 2;

$p _ { 1 } ^ { * }$ always decreases with $\delta ,$ the cost associated with buying from the gray market, and $p _ { 2 } ^ { * }$ decreases with δ when $\gamma < \phi$ and increases with δ otherwise.

Lemma 3 shows that when consumer valuation in the high-priced market (W) increases, prices in both markets will rise. In the high-priced market 2, the increase in consumer valuation allows the firm to charge a higher price premium. In the low-priced market 1, the volume of demand through the unauthorized channel rises, leading to a higher price as well. When the cost of parallel trade (δ) increases, it becomes more expensive to purchase from the gray market (at price $p _ { 1 } + \delta )$ and the total demand in market 1 will decrease. To compensate for this, a profit maximizing firm will lower the price $p _ { 1 }$ to make unauthorized sales still attractive. The efect of δ on $p _ { 2 } ^ { * } ,$ however, depends on the magnitude of the leakage. Essentially, the presence of the unauthorized distribution channel leads to a cross-market resegmentation. As the gray market attracts some consumers from the high-priced market, consumers in market 2 can become more polarized, allowing the firm to charge a higher price $p _ { 2 }$ . However, when relatively more price-sensitive consumers $( \phi > \gamma )$ migrate to purchase from the gray market, the firm will need to lower $p _ { 2 }$ to control the size of the gray market.

We now turn our attention to the price gap between the two markets. When there is no gray market, $\Delta p _ { b } =$ $p _ { 2 } ^ { * } - p _ { 1 } ^ { * } = ( W - 1 ) / 2$ . With a gray market,

$$
\begin{array}{l} \Delta p _ {u} = p _ {2} ^ {*} - p _ {1} ^ {*} \\ = \frac {2 (1 - \gamma) (W - 1) + (\phi - \gamma) (1 + \lambda W) + \lambda \phi \delta (2 - \phi - \gamma)}{(1 - \gamma) [ 4 + \lambda (1 + \gamma + 2 \phi) ] - \lambda (1 - \phi) ^ {2}}. \end{array}
$$

Therefore:

Lemma 4. With a gray market, the price gap, $\Delta p _ { u } ,$ , between the two markets

• increases with $W ,$ the consumer valuation of the product in market $2 ;$

• increases with $\delta ,$ the cost associated with buying from the gray market.

Figure 1. (Color online) Optimal Prices $p _ { 1 } ^ { * }$ and $p _ { 2 } ^ { * }$ as Functions of $\phi$ and $\gamma$  
![](/api/attachments/KEVY3VW4/fulltext/images/1b57e70bd7154e0441f46f2a2c18c4b886e7357960d83ef59fb60954adbb7c27.jpg)

Intuitively, when there is leakage between the two markets, the firm should reduce the price gap to control price arbitrage opportunities. It is possible, however, that the price gap between the two markets widens. For example, the optimal prices in both markets increase when there are more high-valuation consumers in market 2 (because of an increase in W, see Lemma 3). However, because the firm has room to extract more surplus from those high-valuation consumers in market $^ { 2 , }$ the firm can aford to increase the price in the high-priced market at a larger rate, resulting in a bigger price gap between the two markets. When the cost of parallel trade (δ) increases, the gray market becomes less attractive because the price through the unauthorized channel increases. The only way for the firm to counter this is to widen the price gap between the two authorized channels, thus providing more incentive for gray market activities.

Even though the price gap $\Delta p _ { u }$ widens when the cost of parallel trade increases, it is not clear whether the existence of gray market sales can benefit the firm. What matters to the firm is whether the extra demand generated through the unauthorized channel can outweigh the loss of consumers switching to buy from the gray market, which depends on the magnitude of $\phi$ and $\gamma .$ Mathematically this becomes cumbersome. In the following, we first present the results from our numerical analysis of the optimal prices and the profit with respect to changes in $\phi$ and $\gamma .$ . We subsequently derive analytically tractable results and discuss insights for a special case where the probability of new customers buying from the gray market is rescaled and normalized such that $\phi = 1$

Figure 1 plots how the optimal prices, derived in Equation (3), change with $\phi$ and $\gamma$ when $\lambda = 1 . 2 ,$ $\delta = 0 . 2$ , and $W = 3$ . It can be seen that, in general, both prices are sensitive to the “leakage” between the two markets. Additionally, $p _ { 1 } ^ { * }$ seems to monotonically increase with $\gamma$ . The optimal price $p _ { 2 } ^ { * } ,$ , on the other hand, increases monotonically when $\phi$ increases. When comparing the total profit of the firm against that without gray market sales (Figure 2), we note that it can be higher if the leakage γ to the gray market is low.

![](/api/attachments/KEVY3VW4/fulltext/images/a2d7abc0464e969e023c9c6268bc491eaba1ed747a5357eba7290f3122ed8b3f.jpg)

Figure 2. (Color online) Total Profit as a Function of φ and $\gamma$  
![](/api/attachments/KEVY3VW4/fulltext/images/663d329459a803bb39dd83217b7124f7bc5e3fe6136f86dc80e7bd961c73a358.jpg)

In Figures 3 and $^ { 4 , }$ respectively, we fix one probability of market leakage and examine how the optimal prices and the price gap between the two markets will change with the other probability. It can be seen that as more new customers enter to buy from the gray market, the firm is better of increasing the price gap (Figure 3). On the other hand, the optimal prices between the two markets converge (Figure 4) when more existing customers switch to buy from the gray market. Finally, Figure 5 plots the unauthorized consumer demand $( D _ { u } = D _ { n } + D _ { s } )$ that is redistributed

Figure 3. (Color online) Optimal Prices as Functions of φ Where $\gamma = 0 .$ 4  
![](/api/attachments/KEVY3VW4/fulltext/images/a6cd58dbc692ea82722a3bc872803eb81003724c4d1c0a3b9816b4b666e02d08.jpg)

Figure 4. (Color online) Optimal Prices as Functions of γ Where $\phi = 0 . 3$  
![](/api/attachments/KEVY3VW4/fulltext/images/e756223b63d5744b263ccd806a241592573dcc8c6f49c075182812a4935c18b6.jpg)  
from market 2 to market 1 when φ changes. While the new consumers $( D _ { n } )$ that enter the market increase with $\phi ,$ consumers that switch to the gray market $( D _ { s } )$ actually decrease.

Figure 5. (Color online) Market Leakage as Functions of φ Where $\gamma = 0 .$ 4  
![](/api/attachments/KEVY3VW4/fulltext/images/0d419108f0bdd325b0dd112313fd280120893be932c11d48d121247bdbc7bee3.jpg)

## 3.1. Special Case: All New Consumers Buy from the Gray Market

To simplify notations and derive explicit conditions under which the firm is better of with a higher price gap, we rescale and normalize the probabilities such that $\phi = 1$ and $\xi = \gamma / \phi$ . Recall that φ represents the probability for those consumers who originally could not aford but can now buy the product from the gray market. Parameter $\xi \left( \xi < 1 \right)$ then measures the relative magnitude of the switching probability of the highvaluation consumers with respect to the low-valuation consumers in market 2. With this, the optimal prices can be represented as

$$
\begin{array}{l} p _ {1} ^ {*} = \frac {2 + \lambda \xi W + \lambda W - 2 \lambda \delta}{4 + 3 \lambda + \lambda \xi} \quad \text { and } \\ p _ {2} ^ {*} = \frac {1 + 2 W + \lambda \xi W + 2 \lambda W - \lambda \delta}{4 + 3 \lambda + \lambda \xi}. \end{array}\tag{4}
$$

Proposition 1. When there is a gray market (as opposed to no gray market), a firm can expand the price gap between the two markets when the size of market 2 is large, ξ is small, and δ is moderate. More specifically, $\Delta p _ { u } - \Delta p _ { b } > 0 \ i f$

$$
\begin{array}{r l} & {\max \Bigg \{\frac {\lambda W (1 + \xi) - \lambda (3 + \xi) - 2}{2 \lambda},} \\ & {\qquad \frac {(4 + \lambda \xi + 3 \lambda) V - \lambda W (1 + \xi) - 2}{4 + \lambda \xi + \lambda}, 0 \Bigg \}} \\ & {<   \delta <   \frac {2 W + \lambda W - 1}{4 + \lambda \xi + 2 \lambda}.} \end{array}
$$

The proof of the proposition can be found in the appendix. Proposition 1 is a little surprising. Conventional wisdom would suggest that, when there is a gray market, the firm might want to reduce the price gap in separate markets to mitigate the negative efect of the gray market. We explicitly show that this is not always true. When the size of market 2 is large (either because of a large range of consumer valuations of the product or a high density of the market) and the cost of purchasing from the gray market is moderate, it is beneficial for the firm to increase the price gap between the two markets, thus encouraging some degree of gray market activity.

Substituting the optimal prices (4) into the profit function (2), we get

$$
\pi_ {u} ^ {*} = \frac {\lambda (1 + \lambda - \xi) W ^ {2} + \lambda (1 + \xi) (1 - \lambda \delta) W + (1 - \lambda \delta) ^ {2}}{4 + 3 \lambda + \lambda \xi}.\tag{5}
$$

When we compare the firm’s total profit $\pi _ { u } ^ { * }$ in Equation (5) with $\pi _ { b } ^ { * }$ in Equation (1) in the benchmark situation, it is worth noting that the firm might be better of when there are unauthorized sales. Specifically, we have the following proposition.

Proposition 2. A gray market benefits the firm (in terms $o f$ a higher profit) if sales from such market are below a certain threshold, i.e., $\begin{array} { r } { \dot { \xi } \le ( \lambda ( \operatorname { W } - 2 \delta ) ^ { 2 } + 4 ( W - 2 \delta ) - 3 ) / ( \lambda W ^ { 2 } + } \end{array}$ $( 2 W - 1 ) ^ { 2 } + 4 \lambda W \delta )$

Proposition 2 can have important implications for the firm. Many manufacturers and brand owners express serious concerns about gray markets. Some of them have started taking steps to control and eliminate unauthorized sales. Our analysis demonstrates that firms need to be prudent when facing the gray market threat. While excessive sales in the gray market can erode firm profit, a reasonable level of gray market activity can actually benefit the brand owner. A key message to the brand owner is to figure out ways to (1) accurately track product flows in the value chain and estimate the probabilities of market leakage and (2) better manage and coordinate prices among various distribution channels, thus efectively managing the magnitude and severity of sales from unauthorized channels.

## 4. Model Extensions

In this section, we discuss several model extensions that look into the key model parameters and assumptions. So far, we have assumed that the cost δ is fixed and exogenously given. It is possible that δ could depend on some model parameters (such as market leakage $\phi$ and $\gamma ,$ and prices in both markets). Instead of making any specific assumption about the relationship, we endogenize δ and consider a situation where a reseller enters the market. Additionally, the driving forces behind our main results are the probabilities of φ and $\gamma$ that measure the sales leakage to the gray market. In the previous section, we assumed both probabilities are fixed. We now relax this assumption and consider two diferent cases: (1) $\phi$ and $\gamma$ depend on the consumer valuation, and (2) $\phi$ and $\gamma$ are endogenized and modeled as functions of the price gap (∆p) between the two markets.

## 4.1. The Case of a Reseller in the Gray Market

A reseller, after observing the large price diference between the two markets, enters and operates in the high-priced market. Without loss of generality, we assume that the marginal cost for the reseller is zero. The reseller chooses δ to maximize his profit

$$
\max _ {\delta} \pi_ {r} = \delta [ \lambda \gamma (W - p _ {2}) + \lambda \phi (p _ {2} - p _ {1} - \delta) ].\tag{6}
$$

Since $\partial ^ { 2 } \pi _ { r } / \partial \delta ^ { 2 } = - 2 \lambda \phi < 0 .$ , the optimal solution is obtained at

$$
\delta = \frac {\lambda \gamma (W - p _ {2}) + \lambda \phi (p _ {2} - p _ {1})}{2 \lambda \phi}.\tag{7}
$$

Intuitively, when $p _ { 1 }$ increases, the reseller will lower the cost δ to “compensate” consumers that are willing to buy from the gray market, but only to a certain extent. The total cost to purchase from the gray market $\left( p _ { u } \right)$ still increases because the product is more “expensive.” How δ (or $p _ { u } )$ changes with $p _ { 2 }$ depends on the relative magnitude of new entering customers and the existing customers that switch to the gray market. When more new (existing) customers enter the gray market, δ increases (decreases).

Now, substituting $\delta$ into the brand owner’s profit function, we get

$$
\begin{array}{c} \max _ {p _ {1}, p _ {2}} \pi_ {u} = p _ {1} \left[ (1 - p _ {1}) + \frac {\lambda \phi (p _ {2} - p _ {1}) + \lambda \gamma (W - p _ {2})}{2} \right] \\ + \lambda (1 - \gamma) p _ {2} (W - p _ {2}). \end{array}\tag{8}
$$

The optimal prices for the above profit function<sup>9</sup> are given by

$$
\begin{array}{l} p _ {1} ^ {*} = \frac {4 (1 - \gamma) (2 + \lambda \gamma W) + 2 \lambda W (1 - \gamma) (\phi - \gamma)}{4 (1 - \gamma) (4 + 2 \lambda \phi) - \lambda (\phi - \gamma) ^ {2}} \\ p _ {2} ^ {*} = \frac {2 W (1 - \gamma) (4 + 2 \lambda \phi) + (2 + \lambda \gamma W) (\phi - \gamma)}{4 (1 - \gamma) (4 + 2 \lambda \phi) - \lambda (\phi - \gamma) ^ {2}}. \end{array}\tag{and}
$$

(9)

The price gap is given by

$$
\Delta p _ {u} = \frac {8 (1 - \gamma) (W - 1) + (2 + 2 \lambda W - \lambda W \gamma) (\phi - \gamma)}{4 (1 - \gamma) (4 + 2 \lambda \phi) - \lambda (\phi - \gamma) ^ {2}}.
$$

One can verify that both prices and the price gap increase with $W ,$ consistent with observations from Lemmas $3$ and 4.

## 4.2. Market Leakage Depends on Consumer Valuations

Here, φ and $\gamma$ are functions of the consumer valuation v. It is reasonable to assume that when consumer valuation (v) of the product increases, consumers are less likely to buy from the gray market. In other words, φ and $\gamma$ are negatively related to v. For example, consumers that are bargain hunters (low valuation) of a product are more price sensitive and are more likely to purchase especially if a low-priced option is available (Darke et al. 1995). Let $\gamma = \alpha ( W - v ) / W$ and $\phi =$ $\beta ( W - v ) / W$ denote the probabilities of leakage for a consumer of valuation $v ,$ where α and $\beta$ are the potential maximum propensity to switch. In this case, the consumer demand in market 2 is given by

$$
\begin{array}{c} D _ {2} = \lambda (W - p _ {2}) - \lambda \int_ {p _ {2}} ^ {W} \frac {\alpha (W - v)}{W} d v \\ = \lambda (W - p _ {2}) \bigg [ 1 - \frac {\alpha}{2 W} (W - p _ {2}) \bigg ], \end{array}
$$

Figure 6. (Color online) Optimal Prices and Price Gap When φ and γ Depend on Consumer Valuation  
![](/api/attachments/KEVY3VW4/fulltext/images/84fdad5f3081155ce6a68eb570ba19414d8d310a8a765749e61b90a396406825.jpg)  
and the demand in market 1 is

$$
\begin{array}{l} D _ {1} = (1 - p _ {1}) + \lambda \int_ {p _ {2}} ^ {W} \frac {\alpha (W - v)}{W}   d v + \lambda \int_ {p _ {1} + \delta} ^ {p _ {2}} \frac {\beta (W - v)}{W}   d v \\ \qquad = 1 - p _ {1} + \frac {\lambda \alpha}{2 W} (W - p _ {2}) ^ {2} \\ \qquad + \frac {\lambda \beta}{2 W} (p _ {2} - p _ {1} - \delta) [ 2 W - (p _ {1} + p _ {2} + \delta) ]. \end{array}
$$

The firm’s decision problem can then be written as

$$
\begin{array}{l} \max _ {p _ {1}, p _ {2}} \pi_ {u}, \quad \text {where} \\ \pi_ {u} = p _ {1} D _ {1} + p _ {2} D _ {2} \\ \qquad = p _ {1} \bigg [ 1 - p _ {1} + \frac {\lambda \alpha}{2 W} (W - p _ {2}) ^ {2} \\ \qquad + \frac {\lambda \beta}{2 W} (p _ {2} - p _ {1} - \delta) [ 2 W - (p _ {1} + p _ {2} + \delta) ] \bigg ] \\ \qquad + \lambda p _ {2} (W - p _ {2}) \bigg [ 1 - \frac {\alpha}{2 W} (W - p _ {2}) \bigg ]. \end{array}
$$

The above profit function is cubic in terms of $p _ { i } .$ . Hence, analytical solutions are still available though they are mathematically cumbersome. Without getting buried in complicated mathematical details, we present in Figure 6 the optimal prices and the price gap between the two markets when $W = 3 , \lambda = 1 . \hat { 2 } , \delta = \bar { 0 } . \hat { 2 } ,$ , and $\alpha = 0 . 3$ One can see that the behavior of the price gap with respect to $\beta$ mimics that presented in Figure 3. Sensitivity analyses of the results with other parameters also exhibit similar patterns as those in the previous section.

## 4.3. Market Leakage Depends on Price Gap

Here, φ and γ are endogenized and modeled as functions of the price gap between the two markets. We assume that $\bar { \gamma } = \alpha \bar { ( } p _ { 2 } - p _ { 1 } ) / W$ and $\phi = \beta ( p _ { 2 } - p _ { 1 } ) / W$ The rationale for this is that φ and γ should increase $( \mathrm { i . e . , }$ more consumers will switch to buy from the gray market) when the price gap increases.

Figure 7. (Color online) Optimal Prices When φ and γ Depend on Price Gap (W <sup></sup> 3, λ <sup></sup> 1.2, δ <sup></sup> 0.2, and α <sup></sup> 0.3)  
![](/api/attachments/KEVY3VW4/fulltext/images/a933df00f2319ad78c8daa7739f8b90a162ca82f7b62a75f9eac4b5c9da85e18.jpg)  
In this case, the consumer demands are given by

$$
\begin{array}{l} D _ {1} = (1 - p _ {1}) + \frac {\lambda \alpha}{W} (p _ {2} - p _ {1}) (W - p _ {2}) \\ \qquad + \frac {\lambda \beta}{W} (p _ {2} - p _ {1}) (p _ {2} - p _ {1} - \delta), \\ D _ {2} = \lambda \left[ 1 - \frac {\alpha}{W} (p _ {2} - p _ {1}) \right] (W - p _ {2}). \end{array}
$$

The firm’s decision problem becomes

$$
\begin{array}{l} \max _ {p _ {1}, p _ {2}} \pi_ {u}, \quad \text {where} \\ \pi_ {u} = p _ {1} D _ {1} + p _ {2} D _ {2} \\ \qquad = p _ {1} \bigg [ (1 - p _ {1}) + \frac {\lambda \alpha}{W} (p _ {2} - p _ {1}) (W - p _ {2}) \\ \qquad + \frac {\lambda \beta}{W} (p _ {2} - p _ {1}) (p _ {2} - p _ {1} - \delta) \bigg ] \\ \qquad + \lambda p _ {2} (W - p _ {2}) \bigg [ 1 - \frac {\alpha}{W} (p _ {2} - p _ {1}) \bigg ]. \end{array}
$$

Once again the profit function is cubic in terms of $p _ { i } .$ The trends of the optimal prices and the price gap outlined earlier still hold in this situation (see Figure 7). In Figure 8, we plot how the market leakage will change with the size of the market. It can be seen that when the size of the more expensive market increases, the firm should price the product such that more consumers will switch to the gray market. The marginal benefit of additional gray market sales, however, is diminishing, consistent with our previous finding that the gray market benefits the firm only if sales from such market are below a certain threshold (Proposition 2).

## 5. Data and Empirical Analysis

In this section, we seek to empirically test some of the model findings in the previous section, especially those in Lemmas 1 and 2 on how the consumer demands (authorized sales in each channel, total authorized sales, and unauthorized sales) change with prices in diferent markets.

Figure 8. (Color online) Optimal φ and γ as Functions of W (λ <sup></sup> 1.2, δ <sup></sup> 0.2, α <sup></sup> 0.3, and β <sup></sup> 0.4)  
![](/api/attachments/KEVY3VW4/fulltext/images/d0e720164b14c6b112fe8c73fdcfd71ca2848d3af62ea663968fc7c233502d16.jpg)

Table 1. Description of Data Set

<table><tr><td></td><td>Product 1</td><td>Product 2</td></tr><tr><td>No. of observations</td><td>2,539</td><td>22,704</td></tr><tr><td>Date window</td><td>1/1/2001–3/16/2010</td><td>1/1/2001–3/16/2010</td></tr><tr><td>No. of customers</td><td>539</td><td>1,123</td></tr><tr><td>Average CPI adjusted price</td><td>4.16 (2.10)</td><td>0.53 (0.15)</td></tr><tr><td>Average purchase quantity (number)</td><td>4.50 (11.29)</td><td>5.03 (12.83)</td></tr></table>

Note. Standard deviations are in parentheses.

## 5.1. Analysis of Efects of Channel Prices on Authorized Sales

Our first data source includes all of the authorized sales transactions of two popular electrical products from a Fortune 100 company. The company sells these products through a number of independent and nonoverlapping channels: the domestic market where products are sold to domestic warehouse distributors, the overseas market where products are sold and distributed through an export channel, and the original equipment manufacturer (OEM) market where products are sold to OEMs who assemble the company’s products into their own finished products. Each transaction in the data details the customer number, customer type, transaction number, transaction date, shipping quantity, price, sales channel, and total revenue of the transaction. We adjusted for inflation by dividing each transaction price by the corresponding consumer price index (CPI). Table 1 provides a summary of the data.

In Figure 9, we plot the linear trends of the daily transaction prices for each product in the three channels. We note that, for both products, the domestic market is the most expensive channel, while the OEM market is the least expensive. Additionally, the price for the same product exhibits considerable variation both within and across the three channels. It also seems that the price gap between the domestic market and the other two channels grows bigger over time. It is, however, not clear if the company is aware of the large price gap between diferent markets and its potential implications on product sales and revenue. In the following, we present our empirical analysis that estimates how the demand for each product changes with channel prices as well as the efect of the price gap on the revenue of the product.

Empirical Models and Results on Authorized Sales Data. Our data set is an unbalanced panel that contains sales transactions for the two products over unequally spaced time periods between 2001 and 2010. It is also hierarchical in that there are many customers in each market who made multiple purchases in diferent time periods. In our subsequent analysis, we aggregate the transactions for each individual customer on a monthly basis between 2001 and 2010.

Our variable of interest is the sales quantity $q _ { i j t }$ purchased by individual i from market j at time period t (month). The individual-level covariate is the transaction price $p _ { i j t }$ . There are four market-level covariates. One of them is a categorical variable, channel, which takes one of three values: domestic, export, or OEM. The other three are the average prices $ { p _ { t } ^ { ( j ) } }$ aggregated over all individuals who purchased the product in market j at time period t.

We used a hierarchical mixed efects model in our empirical analysis. Equation (10) presents the complete empirical model

$$
\begin{array}{c} \log (q _ {i j t}) = \mu + \alpha_ {i} + \beta p _ {i j t} + \psi \bar {\mathbf {p}} _ {t} + \eta   c h a n n e l _ {j} + \epsilon_ {i j t}, \\ i = 1, \ldots , n;   j = 1, 2, 3;   t = 1, \ldots , T, \end{array}\tag{10}
$$

where

$\mu$ is the overall intercept, $q _ { i j t }$ is the quantity purchased by individual i from market j at time $t ,$

$p _ { i j t }$ is the transaction price by individual i from market j at time $t ,$

$\bar { \mathbf { p } } _ { t } = ( p _ { t } ^ { ( 1 ) } , p _ { t } ^ { ( 2 ) } , p _ { t } ^ { ( 3 ) } )$ is the vector of average prices in the three markets at time $t ,$

$\beta ,$ ψ are coeficients of the fixed efect of prices,

η is the coeficient of the market efect,

$\alpha _ { i }$ is the random efect of individual $i ,$

$\epsilon _ { i j t }$ is the error term.

There are various views and tests on whether to treat $\alpha _ { i }$ as fixed or random. Green and Tukey (1960) and Allison (2005) provide excellent discussions on this topic. In this research, we would like to make inferences to a broader population than just the sample data in hand. More importantly, some individuals in our data set have only one observation over the time periods. Thus, we treated $\alpha _ { i }$ as a random variable that has a normal distribution with a mean of 0 and constant variation.<sup>10</sup>

Figure 9. Linear Trends of Daily Product Prices Over Time  
![](/api/attachments/KEVY3VW4/fulltext/images/cafba4e74bab2c42fccea2b7d6e0e9464a094ec28e3e2baaabbb623888df4a39.jpg)

The above mixed efects model can be estimated using PROC MIXED in SAS. Singer (1998), Bryk and Raudenbush (2002), and Allison (2005) provide indepth discussions on fitting multilevel models. Here, the first level of our analysis is individual i, and the second level of analysis is the time period t. The variance structure of the dependent variable is modeled as variance components (Singer 1998, Searle et al. 2006) consisting of variation in intercepts between customers and variation within customers.

The results of fitting the complete model are reported in Table 2. It can be seen that the “total variation explained” is about 19% for product 1 and 30% for product 2. When comparing the results to an unconditional means model, we note that the conditional component for the variance within customers (the residual component representing ${ \sigma _ { \epsilon } } ^ { 2 } )$ has decreased (from 0.04689 to 0.04594). So has the variance component representing variation between customers (from 0.01282 to 0.01123). Additionally, we can measure the percentage by which the variance component has diminished between the two models. This is computed as <sup>(</sup>0.01282 <sup>−</sup> 0.01123<sup>)/</sup>0.01282, which yields about 12% (21%) “net variation explained” for product 1 (2) in Table 2. In other words, about 12% (21%) of the total variation in customer mean order quantity is explained by the transaction price as well as the aggregate average market prices.

When examining the efects of prices on order quantity, we note that the estimates for $p _ { i j t }$ are statistically significant and negative for both product categories. This means that as the transaction price increases, the demand for the product will decrease—a downwardslope demand curve, as we would have expected. An interesting observation is that the consumer demand is afected not only by the sale price of the product but also by the aggregate average prices in the other channels. This indicates that the markets are not completely separate/independent as the firm had wished.

![](/api/attachments/KEVY3VW4/fulltext/images/bc4a940b8206aed5460cb9db38f6c5cb997d362e0e0c91a7fc7181a523155976.jpg)

Table 2. Estimates of Mixed Efects Model

<table><tr><td></td><td colspan="2">Product 1</td><td colspan="2">Product 2</td></tr><tr><td>Intercept</td><td>0.55</td><td>(0.076)***</td><td>0.69</td><td>(0.081)***</td></tr><tr><td>Transaction price</td><td>-0.0093</td><td>(0.0037)**</td><td>-0.34</td><td>(0.017)***</td></tr><tr><td>Domestic market price</td><td>-0.026</td><td>(0.011)**</td><td>0.30</td><td>(0.13)**</td></tr><tr><td>Export market price</td><td>0.0029</td><td>(0.0048)</td><td>-0.0051</td><td>(0.016)</td></tr><tr><td>OEM market price</td><td>-0.026</td><td>(0.013)**</td><td>0.0019</td><td>(0.031)</td></tr><tr><td>Channel</td><td></td><td></td><td></td><td></td></tr><tr><td>Domestic</td><td>-0.087</td><td>(0.032)***</td><td>-0.18</td><td>(0.035)***</td></tr><tr><td>Export</td><td>0.080</td><td>(0.041)*</td><td>0.0052</td><td>(0.044)</td></tr><tr><td>OEM</td><td colspan="2">—</td><td colspan="2">—</td></tr><tr><td>Year dummies</td><td colspan="2">Yes</td><td colspan="2">Yes</td></tr><tr><td>Variance components</td><td></td><td></td><td></td><td></td></tr><tr><td>Customer variance ( $\sigma_a^2$ )</td><td>0.011</td><td>(0.0011)***</td><td>0.023</td><td>(0.0013)***</td></tr><tr><td>Residual variance ( $\sigma_e^2$ )</td><td>0.046</td><td>(0.0013)***</td><td>0.051</td><td>(0.00049)***</td></tr><tr><td>Total variation explained (%)</td><td colspan="2">19.64</td><td colspan="2">30.67</td></tr><tr><td>Net variation explained (%)</td><td colspan="2">12.40</td><td colspan="2">21.48</td></tr></table>

p < 0.1; p < 0.05; p < 0.01.

From Table 2, we observe that the average price in the domestic market statistically and significantly influences the demand of both products, and the price in the OEM market significantly influences the demand of product 1.

In addition, the efect of the cross-channel prices $p _ { t } ^ { ( j ) }$ on consumer demand for the two products is not homogeneous. For instance, as the price from the domestic market or that from the OEM market increases, the demand for product 1 decreases. However, the average price in the domestic market has a statistically significant yet positive efect on consumer demand for product 2, meaning that as the price from the domestic market (a channel with a higher price) increases, the average demand for product 2 increases. This seems a little out of the ordinary, but can be explained reasonably well from the perspective of a gray market. When an identical product is ofered in separate markets with price being the only diferentiator, information (product prices) leakage is inevitable. As the price of the product from the domestic (more expensive) market increases, the price gap between diferent channels widens. This in turn creates more opportunities for consumers from the low-priced market $( \mathrm { e . g . }$ , export, OEM) to buy more of the product and potentially sell them (via unauthorized channels) to consumers in the high-priced market.

To further examine the cross-channel price sensitivities of demand for the two product categories, we divided the data into subsets based on the transaction channel and performed analysis of model (10) on each subset of the data. The results of fitting the mixed efects models on the subsets of data are presented in Table 3. It can be seen that the results are consistent with what we observed in Table 2. As the transaction price of the product increases, consumers buy less of the product from that market (ceteris paribus). However, we continue to observe the counterintuitive result for product 2 in the domestic market. The average price in the export market and that in the OEM market both have a significant and positive efect on the sales in the domestic channel. This means that as the prices from the low-priced markets (export and OEM channels) increase, the price gaps between these markets and the domestic market become smaller, so consumers in the domestic market are less likely to switch to buy through unauthorized channels. This in turn leads to an increase of demand in the domestic (high price) market. As before, when the price of product 2 increases in the domestic market, the demand of the product in the export channel will increase. It is also worth noting that the price in the export market and that in the OEM market do not have a significant efect on the demand of product 1 in the domestic market. Similarly, the price in the OEM market does not have a significant efect on the demand of product 2 in the export market. Recall that the domestic market is the most expensive channel, while the OEM market is the least expensive. These results essentially demonstrate that $\partial \bar { D _ { 2 } } / \partial p _ { 1 } = 0$

We now turn our attention to examining the efect of the price gap between diferent markets on the firm’s revenue. We aggregated sales by individuals and markets on a monthly basis and calculated the monthly revenue $R e v _ { t }$ of the firm, where $t =$ $1 , \ldots , T$ . This resulted in 81 month observations for product 1 and 111 month observations for product 2 between January 2001 and March $2 0 1 0 . ^ { 1 1 }$ The Durbin–Watson test detected a significant and positive autocorrelation (Durbin–Watson $\dot { d } = 1 . 0 4 8 , p < \dot { 0 } . 0 0 0 1 )$ between the values of revenue for product 2, but not those for product 1 (Durbin–Watson $d = 2 . 0 0 4 , \ p =$ 0.4947). Therefore, regression models with autocorrelated errors were needed to correct for autocorrelation. A stepwise autoregression method was specified and showed that autoregressive parameters at only lags 1 and 3 are significant. Therefore the following autoregressive model is estimated:

$$
\begin{array}{c} \log (R e v _ {t}) = \mu + \psi_ {1}   \Delta p _ {t} ^ {(d e)} + \psi_ {2} \Delta p _ {t} ^ {(d o)} + \beta \log (R e v _ {t - 1}) \\ + \eta \log (R e v _ {t - 3}) + \epsilon_ {t}, \quad t = 1, \ldots , T, \end{array} \tag {7}\tag{11}
$$

where

µ is the overall intercept,

$\Delta p _ { t } ^ { ( d \dot { e } ) }$ is the price gap between the domestic and the export market at time t,

$\Delta p _ { t } ^ { ( d o ) }$ is the price gap between the domestic and the OEM market at time $t ,$

$\psi _ { 1 } , \psi _ { 2 }$ are coeficients of the efect of the price gap,

$\beta , \eta$ are coeficients of lags,

$\epsilon _ { t }$ is the error term.

The results of fitting the autoregressive model are reported in Table 4. It should be pointed out that estimates of fitting an ordinary regression model on product 1 revenue were not statistically significant and hence are not reported here. From Table 4, we observed that the coeficient estimates at lags 1 and 3 are both negative and significant, indicating the firm’s monthly revenue from product 2 decreases over time. However, we caution against indiscriminately attributing the loss of the revenue to the unauthorized sales of the product. From Table 4, we find that the coeficient estimate for $\Delta p ^ { ( d e ) }$ is positive and statistically significant $( p < 0 . 1 )$ . In other words, there is empirical evidence that as the price diference between the domestic market and the export market increases $( \mathrm { i . e . }$ , signaling potential increase in gray market sales), the firm’s revenue increases. Hence, the loss of revenue might be due to other factors (such as counterfeits, competition, quality of the product). Of course, further empirical analysis is needed to pinpoint the exact cause of the loss of revenue.

## 5.2. Analysis of Efects of Channel Prices on Unauthorized Sales

It is noted in the previous section that we were not able to track the product flows in the value chain and to determine which transaction leads to unauthorized sales. Therefore, we cannot measure the actual leakage (both new and switched customers) to the gray market. As can be seen from Lemma 2, consumer demand through unauthorized channels is influenced by the prices of the same product sold in diferent channels.

To test this result, we collected and assembled a data set of brand name product sales on Taobao.com, which is one of the main marketplaces for online gray market sales in China. This data set contains the transaction information of products from 21 luxury brands including Apple, Fitbit, Amazon Kindle, Coach, Clinique, Dior, Chanel, Rolex, and Omega. The data collection was performed from March 22 through June 23,

Table 3. Estimates of Mixed Efects Models According to Sales Channel

<table><tr><td rowspan="2"></td><td colspan="3">Product 1</td><td colspan="3">Product 2</td></tr><tr><td>Domestic</td><td>Export</td><td>OEM</td><td>Domestic</td><td>Export</td><td>OEM</td></tr><tr><td>Intercept</td><td>0.39 (0.022)***</td><td>1.08 (0.27)***</td><td>0.86 (0.13)***</td><td>0.68 (0.013)***</td><td>-0.33 (0.38)</td><td>2.01 (0.31)***</td></tr><tr><td>Transaction price</td><td>-0.0093 (0.003)***</td><td>-0.071 (0.04)*</td><td>0.047 (0.038)</td><td>-0.32 (0.016)***</td><td>-0.41 (0.19)**</td><td>-0.73 (0.23)***</td></tr><tr><td>Domestic market price</td><td>—</td><td>-0.052 (0.048)</td><td>-0.070 (0.023)***</td><td>—</td><td>2.36 (0.62)***</td><td>-1.73 (0.50)***</td></tr><tr><td>Export market price</td><td>0.0032 (0.0046)</td><td>—</td><td>0.017 (0.013)</td><td>0.045 (0.013)***</td><td>—</td><td>0.0027 (0.11)</td></tr><tr><td>OEM market price</td><td>-0.0006 (0.011)</td><td>-0.10 (0.09)</td><td>—</td><td>0.079 (0.024)***</td><td>-0.072 (0.23)</td><td>—</td></tr><tr><td>Variance components</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Customer variance ( $\sigma_a^2$ )</td><td>0.0084 (0.0008)***</td><td>0.045 (0.02)**</td><td>0.015 (0.006)***</td><td>0.018 (0.001)***</td><td>0.10 (0.02)***</td><td>0.052 (0.018)***</td></tr><tr><td>Residual variance ( $\sigma_e^2$ )</td><td>0.038 (0.0012)***</td><td>0.12 (0.015)***</td><td>0.052 (0.003)***</td><td>0.047 (0.0004)***</td><td>0.13 (0.007)***</td><td>0.093 (0.005)***</td></tr><tr><td>Total variation explained (%)</td><td>18.11</td><td>26.81</td><td>23.16</td><td>27.78</td><td>42.95</td><td>35.84</td></tr></table>

<sup>∗</sup> p < 0.1; <sup>∗∗</sup> p < 0.05; <sup>∗∗∗</sup> p < 0.01.

Table 4. Estimates of Autoregressive Model

<table><tr><td></td><td>Estimate</td></tr><tr><td>Intercept</td><td>4.9253 (0.0574)***</td></tr><tr><td> $\Delta p^{(de)}$ </td><td>0.1360 (0.0771)*</td></tr><tr><td> $\Delta p^{(do)}$ </td><td>0.0353 (0.1426)</td></tr><tr><td>AR1</td><td>-0.3006 (0.0899)***</td></tr><tr><td>AR3</td><td>-0.4744 (0.0929)***</td></tr><tr><td colspan="2">Total  $R^2 = 0.3627$ </td></tr></table>

<sup>∗</sup> p < 0.1; <sup>∗∗∗</sup> p < 0.01.

2016. The information we collected from Taobao.com includes the product name, description, stores that sell the product, store reputation level (heart, diamond, crown, golden crown), store ratings (description matching, service, shipping speed) on Taobao.com, listing price of the product, and quantity of the product sold by each store in the past month.<sup>12</sup> In addition, we collected the oficial price of the product in the U.S. market as well as that in the Chinese market. These oficial product prices were obtained directly from the company websites. If a company website did not list the product price in the Chinese market, we obtained it through the company’s oficial Tmall store.<sup>13</sup> We converted the product price in the U.S. market using the exchange rate of USD 1 <sup></sup> CNY 6.5. Table 5 provides a summary of the data we collected on Taobao.com. On average, the price for the identical product in the U.S. market is about CNY 1,000 less than that in the Chinese market. It is worth highlighting that the average Taobao listing price is slightly lower than the oficial U.S. market price.<sup>14</sup> Since these variables are highly skewed, we take the log transformations in our later analysis.

Empirical Models and Results on Gray Market Sales. Similar to the previous section, our model specification is given by

$$
\begin{array}{r l} & {\log (q _ {i j}) = \mu + \alpha_ {i} + \beta p _ {i j} + \psi_ {1} p _ {i} ^ {(1)} + \psi_ {2} p _ {i} ^ {(2)}} \\ & {\qquad + \eta_ {1} r e p u t a t i o n _ {j} + \eta_ {2} r a t i n g _ {j} + \epsilon_ {i j},} \end{array}\tag{12}
$$

Table 5. Description of Data Collected on Taobao.com

<table><tr><td></td><td>Values</td></tr><tr><td>No. of observations</td><td>272</td></tr><tr><td>Date window</td><td>3/22/2016–6/23/2016</td></tr><tr><td>No. of brands</td><td>21</td></tr><tr><td>No. of products</td><td>76</td></tr><tr><td>Average official U.S. price (in CNY)</td><td>3,874 (10,731)</td></tr><tr><td>Average official China price (in CNY)</td><td>4,901 (12,282)</td></tr><tr><td>Average Taobao listing price (in CNY)</td><td>3,758 (10,216)</td></tr><tr><td>Average monthly sales on Taobao (number)</td><td>119 (237)</td></tr></table>

Note. Standard deviations are in parentheses.

where

$\mu$ is the overall intercept,

$q _ { i j }$ is the monthly sales of product i by store $j ,$

$p _ { i j }$ is the listing price of product i by store $j ,$

$p _ { i } ^ { ( 1 ) } , p _ { i } ^ { ( 2 ) }$ are oficial prices of product i in market 1 and market 2,

$\beta ,$ ψ are coeficients of the fixed efect of channel prices,

η are coeficients of store level control variables including store reputation and ratings,

$\alpha _ { i }$ is the random efect of brand $i ,$

$\epsilon _ { i j }$ is the error term.

Table 6 presents the results of fitting the mixed efects model. We note a few interesting observations. First, the listing price of a product on Taobao.com (the unauthorized channel) does not seem to influence the consumer demand through the unauthorized channel; the efect is in the right direction though $( \beta = - 0 . 3 4$ $p = 0 . 2 1 )$ . However, the oficial prices of the product in markets 1 and 2 both significantly influence gray market sales. Moreover, the efects of the two prices are in diferent directions. While consumer demand through the unauthorized channel drops when the U.S. market price $\left( { { p } _ { 1 } } \right)$ increases, it goes up when the Chinese market price $\left( { { p } _ { 2 } } \right)$ increases. These results provide further empirical evidence of our findings in the previous section (Lemma 2). Finally, store reputation (golden crown status) has a significant and positive efect on gray market sales. The efects of store ratings on unauthorized sales are, however, negligible.

Table 6. Estimates of Mixed Efects Model on Unauthorized Sales

<table><tr><td></td><td>Estimate</td></tr><tr><td>Intercept</td><td>7.65 (5.76)</td></tr><tr><td>Listing price</td><td>-0.34 (0.27)</td></tr><tr><td>Official U.S. price</td><td>-0.83 (0.44)*</td></tr><tr><td>Official China price</td><td>0.64 (0.34)*</td></tr><tr><td>Store reputation</td><td></td></tr><tr><td>Crown</td><td>0.42 (0.30)</td></tr><tr><td>Diamond</td><td>0.16 (0.25)</td></tr><tr><td>Golden crown</td><td>1.39 (0.39)***</td></tr><tr><td>Heart</td><td>—</td></tr><tr><td>Rating of description</td><td>-0.75 (2.13)</td></tr><tr><td>Rating of service</td><td>1.46 (2.18)</td></tr><tr><td>Rating of shipping speed</td><td>-0.98 (1.88)</td></tr><tr><td>Variance components</td><td></td></tr><tr><td>Brand variance ( $\sigma_a^2$ )</td><td>1.35 (0.52)***</td></tr><tr><td>Residual variance ( $\sigma_e^2$ )</td><td>1.26 (0.11)***</td></tr><tr><td>Total variation explained (%)</td><td>51.91</td></tr></table>

<sup>∗</sup> p < 0.1; <sup>∗∗∗</sup> p < 0.01.

## 6. Conclusion

Sales of genuinely branded products through unauthorized distribution channels, fueled by advanced online trade and social platforms, have become increasingly popular in recent years. The ability for consumers to shop from diferent geographical locations poses a number of challenges with significant implications and consequences. While brand owners have expressed concerns about the potential negative efects of gray market sales on their bottom lines, they can also design a nimble price discrimination strategy and use the gray market to their advantage.

In this paper, we develop a model where a single firm sells an identical product in two distinct markets. Consumers in the two markets are geographically separated but have the opportunity to trade the product through an unauthorized distribution channel. We derive the optimal prices in the two markets and examined how they influence consumer demands and the firm profit. Several model extensions are also discussed. We demonstrate that an increase in the price gap resulting from diferential pricing in the two markets leads to higher gray market sales and, under certain conditions, a higher firm profit. Using sales data from a Fortune 100 company, we found a seemingly counterintuitive relationship between channel prices and consumer demands. We argue that our theoretical model ofers a lens to help understand this phenomenon. Additionally, we assembled a data set of brand name product sales on Taobao.com to examine how oficial product prices in separate markets influence gray market sales. Our analysis provides further empirical evidence of the model findings.

There are several limitations of the study. Some of the model results could not be empirically tested because consumer valuations, the cost of purchasing in the gray market, and the probabilities of market leakage are hardly observable. Our data are also limited. We had the sales data of two products through authorized distribution channels from a single company. Because of the sensitivity and the secretive nature of activities in gray markets, it is dificult to precisely track the product flows in the entire value chain and to determine which transactions lead to unauthorized sales. Still, we later assembled a data set of brand name product sales (gray market sales) on Taobao.com, which is one of the main marketplaces for online gray market sales in China. With this data set, we were able to conduct additional tests and provide further empirical evidence on how a firm’s pricing strategy can influence the sales of their products in the gray market. However, we still cannot precisely measure the actual leakage (both new and switched customers) to the gray market over time and directly test how gray market sales influence the firm profit.

In addition, it is possible that the consumer demand and the firm profit are afected by many other microlevel (such as company advertising) as well as macrolevel (such as entry and exit of competitors) factors. Using the limited data at hand, we cannot rule out the potential efects of these factors. We argue that the mechanism of the underlining theoretical foundation that drives our empirical analysis is that the price gap between diferent channels leads to gray market sales, which can then influence the total demand through authorized channels, thus resulting in a change in firm profit. This study provides some supporting evidence for this mechanism. However, caution must be exercised when generalizing our findings beyond the bounded context of our settings. We call for future empirical studies to triangulate and validate this line of logic to build a comprehensive understanding of the gray market phenomenon.

Finally, given that a significant portion of gray market activities can now be tracked in some leading online marketplaces, we believe that it will be an interesting exercise to collect sales data through unauthorized channels. With such data, one can examine whether gray markets have diferent impacts for diferent product categories and how that will influence the brand owner’s strategies in terms of pricing, channel coordination, and product diferentiation.

## Acknowledgments

The authors would like to thank the senior editor, the associate editor, and the anonymous reviewers for their constructive suggestions and directions to improve this paper. The first author also acknowledges the tremendous support from edgelab, a former research lab at the School of Business, University of Connecticut.

## Appendix. Proofs

## Proof of Lemma 3

The first-order derivatives of $p _ { 1 } ^ { * }$ with respect to W and δ are straightforward and thus omitted. The sign of the first-order derivative of $p _ { 2 } ^ { * }$ with respect to W is the same as the sign of $( 1 - \gamma ) ( 2 + \bar { \lambda } \phi + \lambda \gamma ) \bar { + } \lambda ( \phi - \gamma )$ . From condition (i), we know $2 \dot { ( 1 - \gamma ) } ( \dot { W } - 1 ) \dot { + } ( \phi - \dot { \gamma } ) ( \dot { 1 } + \lambda W ) > 0 .$ Thus, $\phi - \gamma >$ $- ( 2 W ( 1 - \gamma ) ) / ( 1 + \lambda W )$ . Hence,

$$
\begin{array}{r l} & {(1 - \gamma) (2 + \lambda \phi + \lambda \gamma) + \lambda (\phi - \gamma)} \\ & {\quad > (1 - \gamma) (2 + \lambda \phi + \lambda \gamma) - \frac {2 \lambda W (1 - \gamma)}{1 + \lambda W}} \\ & {\quad = \frac {1 - \gamma}{1 + \lambda W} [ (1 + \lambda W) (2 + \lambda \phi + \lambda \gamma) - 2 \lambda W ] > 0.} \end{array}
$$

It is also easy to show that the sign of the first-order derivative of $p _ { 2 } ^ { * }$ with respect to δ is the same as the sign of $\lambda \phi ( \gamma - \phi )$

## Proof of Lemma 4

Taking the first-order derivative of $\Delta p _ { u }$ with respect to δ and W accordingly, we get

$$
\begin{array}{c} \frac {\partial \Delta p _ {u}}{\partial \delta} = \frac {\lambda \phi (2 - \phi - \gamma)}{(1 - \gamma) [ 4 + \lambda (1 + \gamma + 2 \phi) ] - \lambda (1 - \phi) ^ {2}}, \\ \frac {\partial \Delta p _ {u}}{\partial W} = \frac {2 (1 - \gamma) + \lambda (\phi - \gamma)}{(1 - \gamma) [ 4 + \lambda (1 + \gamma + 2 \phi) ] - \lambda (1 - \phi) ^ {2}}. \end{array}
$$

It is clear that $\partial \Delta p _ { u } / \partial \delta > 0$ since both $\gamma \leq 1$ and $\phi \leq 1$ From condition ${ \mathrm { ( i ) } } ,$ we get $2 ( 1 - \gamma ) ( W - 1 ) + ( \phi - \gamma ) ( 1 + \lambda W )$ $> 0 .$ . Therefore, $2 ( 1 - \gamma ) \bar { + } \lambda ( \phi - \gamma ) > ( 2 - \gamma - \phi ) / W > 0$ and $\partial \Delta p _ { u } / \partial W > 0$

## Proof of Proposition 1

Given $\Delta p _ { u }$ and $\Delta p _ { b } ,$ we can calculate

$$
\Delta p _ {u} - \Delta p _ {b} = \frac {2 \lambda \delta - \lambda W (1 + \xi) + \lambda (3 + \xi) + 2}{2 (4 + 3 \lambda + \lambda \xi)}.
$$

Therefore, $\Delta p _ { u } - \Delta p _ { b } > 0 \mathrm { i f } \delta > ( \lambda W ( 1 + \xi ) - \lambda ( 3 + \xi ) - 2 ) / ( 2 \lambda )$ Recall the two boundary conditions in (i) and (ii) as well as $\delta > 0 ,$ we can express the final condition for $\Delta p _ { u } - \Delta p _ { b } > 0$ in terms of δ as given in the proposition. In other words, the firm can expand the price gap between the two markets when the cost (δ) of purchasing from the gray market is within a certain range, which can be shown to be nonempty under certain conditions.<sup>15</sup>

## Proof of Proposition 2

Subtracting (1) from (5), we get

$$
\begin{array}{l} \pi_ {u} ^ {*} - \pi_ {b} ^ {*} \\ = \frac {\lambda [ (\lambda - \xi (4 + \lambda)) W ^ {2} + 4 (1 + \xi) (1 - \lambda \delta) W - 3 - \xi - 8 \delta + 4 \lambda \delta^ {2} ]}{4 (4 + 3 \lambda + \lambda \xi)}. \end{array}
$$

Thus, $\pi _ { u } ^ { * } - \pi _ { b } ^ { * } \geq 0 \mathrm { ~ i f ~ } ( \lambda - \xi ( 4 + \lambda ) ) W ^ { 2 } + 4 ( 1 + \xi ) ( 1 - \lambda \delta ) W -$ $3 - \xi - 8 \delta + 4 \lambda \delta ^ { 2 } \geq 0 .$ Collecting terms and simplifying with respect to $\xi ,$ we have $\lambda ( W - 2 \breve { \delta } ) ^ { 2 } + 4 ( W - 2 \delta ) \dot { - } 3 \dot { \geq } ( \breve { \lambda } W ^ { 2 } +$ $( 2 \bar { W } - 1 ) ^ { 2 } + 4 \lambda W \delta ) \xi$ . Thus, $\xi \le ( \lambda ( W - 2 \delta ) ^ { 2 } + 4 ( W - 2 \delta )$ $- 3 ) / ( \lambda W ^ { 2 } + ( 2 W - 1 ) ^ { 2 } + 4 \lambda W \delta )$ . It can be shown that the threshold is positive when λ and/or W is large.

## Endnotes

<sup>1</sup> See KPMG (2008).

<sup>2</sup> See http://www.tmall.com (accessed March 25, 2017). Luxury brands that have opened oficial stores on Tmall include Amazon, Apple, BMW, Burberry, Estee Lauder, Hugo Boss, Microsoft, Nike, Sony, Ugg, and many others.

<sup>3</sup> For instance, the Burberry BBY1201 43 mm Automatic Watch sells for RMB 18,380 (or \$2,965) on Burberry’s oficial Tmall store, but sells for only \$1,795 on Burberry’s U.S. store.

<sup>4</sup> Some economists have pointed out the possibility of an upwardsloping demand curve for certain inferior (Gifen) goods (Masuda and Newman 1981) as well as luxury (Veblen) goods (Leibenstein 1950). Empirical evidence for either concept, however, is lacking, and the electronic products in our analysis certainly do not fit into either the inferior or luxury product category.

<sup>5</sup> Depending on the magnitude of V and W, the distribution of the consumer valuation of the product in the two markets can overlap or be completely separated.

<sup>6</sup> When market 2 is covered, the total consumer demand in market 1 is $D _ { 1 } = ( 1 - p _ { 1 } ) + \lambda \gamma ( W - p _ { 2 } ) + \lambda \phi ( p _ { 2 } - V )$ as opposed to $D _ { 1 } =$ $( 1 - p _ { 1 } ) + \lambda \gamma ( W - p _ { 2 } ) + \lambda \phi ( p _ { 2 } - p _ { 1 } - \delta )$

<sup>7</sup> It should be highlighted that gray market sales could also drop even if $p _ { 2 }$ increases (thus the price gap between the two markets widens) when consumers in market 2 are much more likely to switch to the gray market $( \mathrm { i . e . , \gamma }$ is large). However, it is dificult to observe and precisely measure the probabilities of market leakage in reality.

<sup>8</sup> The Hessian of the profit function is given by

$$
H = \left| \begin{array}{c c} - 2 (1 + \lambda \phi) & \lambda (\phi - \gamma) \\ \lambda (\phi - \gamma) & - 2 \lambda (1 - \gamma) \end{array} \right|.
$$

It can be shown that the corresponding Hessian matrix is negative definite when $( 1 - \gamma ) ( 4 + \lambda ( 1 + \gamma + \phi ) ) - \lambda ( 1 - \phi ) > 0$

<sup>9</sup> The Hessian of the profit function is given by

$$
H = \left| \begin{array}{c c} - 2 - \lambda \phi & \lambda (\phi - \gamma) / 2 \\ \lambda (\phi - \gamma) / 2 & - 2 \lambda (1 - \gamma) \end{array} \right|.
$$

Its matrix is negative definite since $( 1 - \gamma ) ( 4 + \lambda ( 1 + \gamma + \phi ) ) - \lambda ( 1 - \phi )$ $> 0 .$

<sup>10</sup> One could also perform fixed efects panel analysis by removing those individuals with only one observation, but that, in our minds, represents a significant loss of information.

<sup>11</sup> In 30 of the months between January 2001 and March 2010, we did not observe any sales of product 1 in the export or OEM market. In other words, the aggregate average prices in the export and OEM markets do not exist for those 30 months, which are not used in our regression analysis.

<sup>12</sup> We did not include the stores with zero transaction quantity of the product.

<sup>13</sup> Tmall.com is a leading business-to-consumer platform enabling businesses worldwide to reach China’s consumer market. Unlike Taobao.com, listings on Tmall.com are either brand owners or authorized distributors of the brand.

<sup>14</sup> There are several possible reasons. First, some brands such as Chanel, Dior, and Rolex are headquartered in Europe. In general, product prices for these brands are lower in Europe than in the U.S. market. Consumers may buy the products from the European market and then resell them on Taobao.com. It is also possible some Taobao listings are not authentic merchandise. There is no way for us to make the distinction based on store information and listing description.

<sup>15</sup> For example, when $V = 0 , W < 1 + 2 ( 1 + \lambda ) / ( \lambda ( 1 + \xi ) )$ , the range for δ is given by $0 < \delta < ( 2 W + \lambda W - 1 ) / ( 4 + \lambda \xi + 2 \lambda )$

## References

Ahmadi R, Yang R (2000) Parallel imports: Challenges from unauthorized distribution channels. Management Sci. 19(3):279–294.

Allison P (2005) Fixed Efects Regression Models for Longitudinal Data Using SAS (SAS Institute Inc., Cary, NC).

Ancarani F, Shankar V (2004) Price levels and price dispersion within and across multiple retailer types: Further evidence and extension. J. Acad. Marketing Sci. 32(2):176–187.

Antia KD, Bergen M, Dutta S (2004) Competing with gray markets. Sloan Management Rev. 46(1):63–69.

Antia KD, Bergen M, Dutta S, Fisher RJ (2006) How does enforcement deter gray market incidence? J. Marketing 70(1):92–106.

Assmus G, Wiese C (1995) How to address the gray market threat using pricing coordination. Sloan Management Rev. 36(3):31–41.

Autrey RL, Bova F (2012) Gray markets and multinational transfer pricing. Accounting Rev. 87(2):393–421.

Ba S, Stallaert J, Zhang Z (2010) Balancing IT with the human touch: Optimal investment in IT-based customer service. Inform. Systems Res. 21(3):423–442.

Ba S, Stallaert J, Zhang Z (2012) Online price dispersion: A game theoretic perspective and empirical evidence. Inform. Systems Res. 23(2):575–592.

Barrett P (2013) A high court gray market win for Costco, eBay. Bloomberg Businessweek (March 19), https://www.bloomberg .com/news/articles/2013-03-19/a-high-court-gray-market-win -for-costco-ebay.

Bryk AS, Raudenbush SW (2002) Hierarchical Linear Models: Applications and Data Analysis Methods, 2nd ed. (Sage Publications Inc., Thousand Oaks, CA).

Brynjolfsson E, Smith M (2000) Frictionless commerce? A comparison of Internet and conventional retailers. Management Sci. 46(4):563–585.

Bucklin LP (1993) Modeling the international gray market for public policy decisions. Internat. J. Res. Marketing 10(4):387–405.

Chu K, Chiu J (2014) Alibaba cleans up gray market for some prestigious brands. Wall Street Journal (August 10), https://www .wsj.com/articles/alibaba-cleans-up-gray-market-for-some-prestigious -brands-1407699693.

Darke P, Freedman J, Chaiken S (1995) Percentage discounts, initial price, and bargain hunting: A heuristic-systematic approach to price search behavior. J. Appl. Psych. 80(5):580–586.

Duhan DF, Shefet MJ (1988) Gray markets and the legal status of parallel importation. J. Marketing 52(3):75–83.

Gerstner E, Holthausen D (1986) Profitable pricing when market segments overlap. Marketing Sci. 5(1):55–69.

Green BF, Tukey JW (1960) Complex analysis of variance: General problems. Psychometrika 25(2):127–152.

Hilke JC (1987) Free trading or free riding: An examination of the theories and available empirical evidence on gray market imports. Working paper, Bureau of Economics, Federal Trade Commission, Washington, DC.

KPMG (2008) Efective channel management is critical in combating the gray market and increasing technology companies’ bottom line. KPMG Gray Market Study Update White Paper. http://www.agmaglobal.org/cms/uploads/whitePapers/7-10 -08KPMGWhitePaperGrayMarketStudy.pdf.

Kucher E, Simon H (1995) Pricing in the new Europe—A time bomb? Pricing Strategy Practice 3(1):4–13.

Kumar V, Rajan V (2012) Social coupons as a marketing strategy: A multifaceted perspective. J. Acad. Marketing Sci. 40(1):120–136.

Leibenstein H (1950) Bandwagon, snob, and Veblen efects in the theory of consumers’ demand. Quart. J. Econom. 64(2):183–207.

Leslie P (2004) Price discrimination in Broadway theater. RAND J. Econom. 35(3):520–541.

Lipner SE (1990) The Legal and Economic Aspects of Gray Market Goods (Quorum Books, Westport, CT).

Maskus KE, Chen Y (2002) Parallel imports in a model of vertical distribution: Theory, evidence and policy. Pacific Econom. Rev. 7(2):319–334.

Masuda E, Newman P (1981) Gray and Gifen goods. Econom. J. 91(364):1011–1014.

McAfee PR (2008) Price discrimination. Issues in Competition Law and Policy, Vol. 1 (American Bar Association, Chicago), 465–484.

Mortimer JH (2007) Price discrimination, copyright law, and technological innovation: Evidence from the introduction of DVDs. Quart. J. Econom. 122(3):1307–1350.

Myers M (1999) Incidents of gray market activity among U.S. exporters: Occurrences, characteristics, and consequences. J. Internat. Bus. Stud. 30(1):105–126.

Palia AP, Keown CF (1991) Combating parallel importing: Views of exporters to the Asian-Pacific region. Internat. Marketing Rev. 8(1):47–56.

Post D (2015) You bought it, you can re-sell it: Costco can keep selling gray market Omega watches at a discount without copyright liability. Washington Post (January 21), https://www .washingtonpost.com/news/volokh-conspiracy/wp/2015/01/ 21/you-bought-it-you-can-re-sell-it-costco-can-keep-selling-gray -market-omega-watches-at-a-discount-without-copyright-liability/ ?utm\_term<sup></sup>.3e1abd753144.

Raf H, Schmitt N (2007) Why parallel trade may raise producers profits. J. Internat. Econom. 71(2):434–447.

Searle SR, Casella CE, McCulloch E (2006) Variance Components (Wiley, Hoboken, NJ).

Shapiro C, Varian H (1998) Information Rules: A Strategic Guide to the Network Economy (Harvard Business Review Press, Boston).

Singer JD (1998) Using SAS PROC MIXED to fit multilevel models, hierarchical models, and individual growth models. J. Educational Behavioral Statist. 24(4):323–355.

Stohr G (2013) eBay wins as top court backs gray market discount goods. Bloomberg Businessweek (March 19), https://www .bloomberg.com/news/articles/2013-03-19/-gray-market-backed -by-high-court-in-win-for-discounters.

Stole LA (2007) Price discrimination and competition. Armstrong M, Porter R, eds. Handbook of Industrial Organization, Vol. 3 (North-Holland, Amsterdam), 2221–2299.

Su X, Mukhopadhyay SK (2012) Controlling power retailer’s gray activities through contract design. Production Oper. Management 21(1):145–160.

Swanson A (2014) China’s growing gray market for all that’s foreign. Foreign Policy (August 20), http://foreignpolicy.com/2014/08/ 20/chinas-growing-gray-market-for-all-thats-foreign/.

Szymanski S, Valletti T (2005) Parallel trade, price discrimination, investment, and price gaps. Econom. Policy 20(44):705–749.

Thompson S (2009) Grey power: An empirical investigation of the impact of parallel imports on market prices. J. Indust., Competition Trade 9(3):219–232.

Tirole J (1988) The Theory of Industrial Organization (MIT Press, Cambridge, MA).

Vandenbosch MB, Weinberg CB (1995) Product and price competition in a two-dimensional vertical diferentiation model. Marketing Sci. 14(2):224–249.

Varian H (1985) Price discrimination and social welfare. Amer. Econom. Rev. 75(4):870–875.

Verboven F (2008) Price discrimination: Empirical studies. Durlauf SN, Blume LE, eds. The New Palgrave Dictionary of Economics (MacMillan, London), 623–625.

Walsh M, Marcus DP (2013) Modern spice routes: The cultural impact and economic opportunity. Paypal Report. https://www .paypalobjects.com/webstatic/mktg/2014design/paypalcorporate/ PayPal\_ModernSpiceRoutes\_Report\_Final.pdf.

Weng ZK (1995) Channel coordination and quantity discounts. Management Sci. 41(9):1509–1522.

Wong E (2013) Chinese search for infant formula goes global. New York Times (July 25), http://www.nytimes.com/2013/07/26/ world/asia/chinas-search-for-infant-formula-goes-global.html.

Xiao Y, Palekar U, Liu Y (2011) Shades of gray—The impact of gray markets on authorized distribution channels. Quant. Marketing Econom. 9(2):155–178.
