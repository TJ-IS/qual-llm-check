---
otero_id: 14898
otero_key: "JVCG2KQ7"
title: "Online Cash-back Shopping: Implications for Consumers and e-Businesses"
authors: "Yi-Chun (Chad) Ho; Yi-Jen (Ian) Ho; Yong Tan"
year: "2017"
journal: "Information Systems Research"
doi: "10.1287/isre.2017.0693"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
This article was downloaded by: [132.239.1.231] On: 29 April 2017, At: 17:59 Publisher: Institute for Operations Research and the Management Sciences (INFORMS) INFORMS is located in Maryland, USA

# Information Systems Research

## HSR

![](/api/attachments/JVCG2KQ7/fulltext/images/73115143848d6e12ae250dd2f69ad228f76fd762dab93e4ad1878bd8baf8a21d.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

# Online Cash-back Shopping: Implications for Consumers and e-Businesses

Yi-Chun (Chad) Ho, Yi-Jen (Ian) Ho, http://orcid.org/0000-0001-8087-3423Yong Tan

To cite this article:

Yi-Chun (Chad) Ho, Yi-Jen (Ian) Ho, http://orcid.org/0000-0001-8087-3423Yong Tan (2017) Online Cash-back Shopping: Implications for Consumers and e-Businesses. Information Systems Research

Published online in Articles in Advance 28 Apr 2017

http://dx.doi.org/10.1287/isre.2017.0693

Full terms and conditions of use: http://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

Copyright © 2017, INFORMS

Please scroll down for article—it is on subsequent pages

![](/api/attachments/JVCG2KQ7/fulltext/images/6b7e5c8f6e67bd9142bfb9d3131cafdc4344a9ba854e84c4995929fca1eaedcd.jpg)

INFORMS is the largest professional society in the world for professionals in the fields of operations research, management science, and analytics.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# Online Cash-back Shopping: Implications for Consumers and e-Businesses

Yi-Chun (Chad) Ho,<sup>a</sup> Yi-Jen (Ian) Ho,<sup>b</sup> Yong Tan<sup>c,</sup> <sup>d</sup>

<sup>a</sup> School of Business, George Washington University, Washington, DC 20052; <sup>b</sup> Smeal School of Business, Pennsylvania State University, University Park, Pennsylvania 16802; <sup>c</sup> Michael G. Foster School of Business, University of Washington, Seattle, Washington 98195; <sup>d</sup> School of Economics and Management, Tsinghua University, 100084 Beĳing, China

Contact: chadho@gwu.edu (Y-C(C)H); ian.ho@psu.edu (Y-J(I)H); ytan@uw.edu, http://orcid.org/0000-0001-8087-3423 (YT)

Received: August 2, 2013 Revised: September 19, 2014; October 29, 2015; July 12, 2016 Accepted: October 14, 2016 Published Online in Articles in Advance: April 28, 2017

https://doi.org/10.1287/isre.2017.0693

Copyright: © 2017 INFORMS

Abstract. Through reimbursing a portion of the transactional amount to some consumers in a form of cash back, merchants are able to exercise third-degree price discrimination by ofering two asymmetric prices via an online dual channel. To better understand such a novel pricing mechanism, we develop a game theoretical model and start our analyses with a market consisting of one merchant, one afiliate site, and consumers heterogeneous in their product valuation. From a price point of view, cash-back shopping appears to provide site users with a saving opportunity since the efective post-cash-back price they pay is perceived to be lower than the regular price targeted at nonusers. However, we find that under some conditions, this seemingly lower price could be actually higher, compared with the optimal uniform price when the merchant does not price discriminate. An important implication is that all consumers may end up sufering from higher prices in the presence of the cash-back mechanism. This surprising result, referred to as the cash-back paradox, defies a common intuition that a price-discriminating firm must raise the price for one segment of consumers but decrease it for the other. We also develop two extensions to seek explanations behind various industry practices. We find that it is in a merchant’s best interest to afiliate with multiple sites, and the resulting competition improves overall market eficiency. Moreover, merchants who are disadvantageous in brand valuation should target price-sensitive consumers by strategically ofering cash-back deals. Our results, consistent with several real-world observations, have useful implications for marketers.

History: Anindya Ghose, Senior Editor; Amit Mehra, Associate Editor.

Funding: Yong Tan was supported in part by the National Science Foundation of China [Grants 71490723, 71531013, and 71572004].

Supplemental Material: The online appendix is available at https://doi.org/10.1287/isre.2017.0693.

Keywords: cash back • price discrimination • promotions • electronic commerce • digital marketing • game theory • double marginalization dual channel

One good way to find deals is to find the cheapest price on a comparison-shopping site and then check at Ebates.com to see if there’s a rebate ofered for the merchant you found. (Rand 2005)

## 1. Introduction

The rise of the Internet and the surging popularity of online shopping have ofered rapid growth in e-commerce and garnished e-businesses’ interest in adopting various digital marketing strategies. Specifically, afiliate marketing, a digital marketing where a merchant pays its afiliates for every visitor or sale brought in by the afiliates’ own efort, has become a prevalent strategy for online businesses to boost sales volume at low costs (Swan 2010b). Table 1 shows the breakdown of afiliate type among the top 20 salesgenerating websites in the United Kingdom from 2006 to 2012 (Swan 2011). The statistics highlight a dynamic shift in digital marketing practice, moving from ordinary methods such as pay-per-click (PPC) to the novel cash-back model. Over the years, the cash-back afiliate model—which incentivizes consumers to purchase by reimbursing them with a certain portion of the transactional amount—has received substantial acceptance among online merchants because of its capability to convert trafic into sales in a more cost-eficient way.

Websites built simply on the cash-back concept, such as Ebates.com and MrRebates.com, are extremely successful. Ebates, the leading cash-back site in the United States, with 12 million registered users, has reimbursed over \$250 million to its members since 1998.<sup>1</sup> In 2011 it brokered \$900 million in merchandise sales for its 1,800 partnered merchants. Its revenue growth has trended 50% higher for the second year in a row since 2010 (Hoge 2011). Moreover, cash-back sites are not the only ones trying to exploit this new marketing concept. Software giant Microsoft in 2008 implemented the cash-back feature that allows its search engine Bing to act as a cash-back publisher. One year later, Google also introduced its Google Checkout as a platform for rewarding its customers. In addition, major consumer banks in the United States gradually roll out cashback features on their own online shopping outlets, such as the Ultimate Reward Mall by Chase, ThankYou Bonus Center by Citibank, and Discover Deals Program by Discover. In August 2012, Bank of America further leveraged the cash-back concept by launching BankAmeriDeals, an innovative program that allows consumers to earn cash back from shopping at physical stores.

Table 1. Breakdown of Afiliate Models Among the Top 20 Sales-Generating Websites

<table><tr><td>Affiliate method</td><td>2006</td><td>2007</td><td>2008</td><td>2009</td><td>2010</td><td>2011</td><td>2012</td></tr><tr><td>PPC</td><td>13</td><td>14</td><td>9</td><td>7</td><td>5</td><td>2</td><td>3</td></tr><tr><td>Coupon code</td><td>0</td><td>0</td><td>3</td><td>3</td><td>3</td><td>5</td><td>3</td></tr><tr><td>Cash back</td><td>2</td><td>2</td><td>2</td><td>4</td><td>5</td><td>6</td><td>7</td></tr><tr><td>Content/others</td><td>5</td><td>4</td><td>6</td><td>6</td><td>7</td><td>7</td><td>6</td></tr></table>

The cash-back afiliate model is a novel marketing solution featuring both promotions and price discrimination in an online context. On one hand, it allows online merchants to expand their market. Once afiliating with a cash-back site, a merchant can post a referral link, a hyperlink that redirects trafic to the merchant’s own online storefront where the actual purchase transactions take place. Thanks to the advance in web technologies, merchants are able to trace back whether a transaction was led via a referral link or not. If consumers make purchases through those links, the cash-back site, as an intermediary, collects an afiliate fee from the merchant. It then entices consumers into purchasing by rewarding them with a preannounced percentage of the transactional amount, also known as cash back (Williams 2014). Such momentary incentives have the ability to induce further spending in the same channel they originated from (Vana et al. 2015), making the cash-back afiliate one of the most efective promotional devices in generating more sales. On the other hand, the cash-back model also serves as a pricing device to achieve market segmentation. Products can be listed for one price for noncash-back shoppers and a lower price for cash-back shoppers at the same time, allowing the merchant to exercise third-degree price discrimination among consumers.

A key diferentiator of the cash-back model from traditional promotional vehicles is the pricing power possessed by the afiliate sites. In the case of coupons and mail-in rebates, a price-discriminating firm has the absolute market power and hence can dictate the discriminatory prices all by itself. In the cash-back model, however, an afiliating merchant loses some control over the prices because of the afiliate fees demanded by the intermediary sites. Depending on the format of the fees, the current cash-back practice can be further categorized into two diferent models: the commission-based fee model and the lead-based fee model.<sup>2</sup> With the commission-based fee model, a merchant first decides a commission percentage, which determines the amount of fees that will be paid to the afiliate site. The site then sets a cash-back rate to incentivize its users. With the lead-based fee model, however, the two parties move in a reverse order. The site first announces a fixed charge for every lead it generates, followed by the merchant’s choice of the cashback rate. In either model, the site pays the cash-back reward to consumers (Williams 2014) and handles all of the cash-back-related issues such as missing transactions, incorrect amount of rewards, and so on. From an economic perspective, the presence of the afiliates alters the channel structure and therefore has an adverse impact on the profitability of discriminating.

## 1.1. Questions and Findings

Motivated by the lack of a theoretical examination of the novel cash-back model, we are interested in answering the following questions:

• How does the presence of the cash-back afiliate impact the optimal pricing scheme?

• Should an online merchant adopt a single-homing or a multihoming strategy when making afiliate decisions?

• What types of merchants are more attracted to utilizing the cash-back model in a competitive setting?

To address these questions, we develop a game theoretical model and start our analyses by considering a market consisting of one merchant, one cash-back site, and consumers heterogeneous in their valuation of a product. Our results show that cash-back pricing is profitable as long as consumer product valuation is suficiently diverse and the fraction of low-valuation consumers is relatively small. The intuition behind this is that the advantage of cash-back pricing, over uniform pricing, prevails as the valuation gap between cash-back users and nonusers gets more salient. On the other hand, the profitability of the afiliate model increases as the fraction of cash-back users diminishes, because the amount of afiliate fees would be relatively small in this case. From a price standpoint, pricesensitive consumers enjoy cash-back shopping because the discounted prices they pay are perceived as lower relative to the regular prices faced by nonusers. Surprisingly, we show that cash-back deals, in fact, may not be as good as they seem to be. Under some conditions, all consumers will end up sufering from higher prices compared with the uniform price they would have faced if the merchant did not price discriminate. We refer to such an interesting phenomenon as the cash-back paradox. The increase in prices is driven by the fact that both members independently seek their own highest margin, giving rise to a problem analogous to double marginalization in a supply chain setting. The presence of the cash-back intermediary—the unique aspect of this paper—leads to an upward price distortion, which, in turn, raises the price targeted at cashback users over the uniform price. An implication for consumers is that none of them could benefit from the seemingly attractive concept of cash-back shopping.

After having a clear understanding of the cash-back mechanism, we develop two extensions to seek explanations behind various industry practices. In the first extension, we incorporate consumer choice between two competing sites into the basic model. Understanding the impact of afiliate competition on the underlying mechanism is of much significance, as its presence reallocates the relative market power among afiliate members. Our results show that it is in the merchant’s best interest to introduce afiliate competition through a multihoming strategy. The resulting competition partially moderates the upward price distortion stemming from double marginalization, leading to a higher profit for the afiliating merchant. We also find that while afiliate competition lowers the price targeted at cashback users, the phenomenon of the cash-back paradox will still occur as long as competing sites are horizontally diferentiated.

To examine the strategic role of cash back in the presence of merchant competition, we finally consider another extension in which two asymmetric merchants can flexibly choose whether to adopt cash-back pricing. The objective here is to see what type of merchants are more attracted to the cash-back model. We find that a single merchant’s adoption of cash back may lead to a win–win situation in which both merchants are better of. As suggested by our analysis on asymmetric equilibria, the low-valuation merchants should use the cash-back model more aggressively as they have a higher incentive to compete for price-oriented consumers by engaging in a price war.

This research provides useful managerial implications for e-business owners. For example, when making afiliate decisions, a merchant should adopt a multihoming strategy as the resulting competition will place a downward pressure on the afiliate fees. From a social perspective, the reduction in the afiliate fees, in turn, improves the market eficiency—the merchant reaps a higher margin, and cash-back users enjoy a reduced price. Furthermore, merchants with relatively inferior brand valuation should aggressively exploit the afiliate model to compete for price-oriented consumers. Our findings, consistent with multiple real-world observations, shed light on the economic impact the cash-back model has on merchants’ pricing strategies.

## 1.2. Literature Review

The efect of a promotional vehicle on the firm’s profit has long been studied. Since Narasimhan (1984) empirically showed that coupons have the ability to provide a lower price to a particular segment of consumers, a variety of coupons have been invented by practitioners and the profitability of each of them has been closely examined by researchers. For example, coupons take various forms such as direct mail coupons (e.g., Bawa and Shoemaker 1987), newspaper coupons (e.g., Neslin 1990), package coupons (e.g., Raju et al. 1994), cross-ruf coupons $( \mathrm { e . g . }$ , Dhar and Raju 1998), and mail-in rebates (e.g., Chen et al. 2005). While those pricing devices have their own advantages, the various underlying mechanisms share a fundamental similarity: the firm issuing coupons possesses absolute market power and hence can reap all of the benefits from price discrimination. Under the cash-back model, on the contrary, a merchant needs to afiliate with third-party websites through which a second, discriminated price can be operationalized. From a pricing point of view, the presence of the intermediary lessens the merchant’s market power, obscuring the profitability of discriminating. The identification of the cashback paradox casts doubts on an intuition regarding the efect of discrimination on prices—discriminating mechanisms raise the price for some consumers but lower the price for others. Our work, in this respect, is unique to the economic research on promotions.

An exceptional paper that investigates the efect promotions have in an analogous supply chain setting is that by Neslin (1990). Using scanner panel data, he shows that coupons have an evident efect on market share after controlling for competitive couponing activity. Despite the similarity in a channel-like structure, our research is diferent in the following two aspects. First, the goal of Neslin’s (1990) work is to empirically test whether couponing results in incremental sales. However, our focus is to analytically characterize market conditions under which discriminating is profitable. Second, and more importantly, in Neslin’s (1990) framework, each of the supply chain members can make its own promotion decision, whereas in our research the depth of promotions is jointly determined by the afiliate members through the cash-back mechanism.

Some prior analytical work has investigated the role of price discrimination in competitive settings (e.g., Borenstein 1985, Katz 1984). Most of the papers in this research stream consider symmetric firms and examine how the discriminatory mechanisms impact total profits and market equilibrium. For example, Shafer and Zhang (1995) consider a market in which two competing firms can distribute coupons either to targeted consumers or via mass media. They conclude that coupon targeting leads to a prisoner’s dilemma in which both firms lose. This is because a firm’s couponing efort helps to maintain its market share, and, as a result, total profits diminish because of the discount given to coupon users. The implication is that both firms may wish to refrain from price discrimination. Corts (1998) finds a similar result by showing that thirddegree price discrimination may yield a prisoner’sdilemma outcome. To avoid profit losses as a result of price competition, firms may desire to make unilateral commitments not to price discriminate. Holmes (1989) explores the efect of discrimination on profits with a focus on diferent types of elasticity of demand. In particular, he assumes that the market is composed of two segments, each of which has diferent firm-level and cross-price elasticity of demand. His results show that the efect of price discrimination on total profits is mixed: the total profits will increase when the lowprice market has a higher firm-level elasticity. All of the equilibria identified in these papers are symmetric, meaning that it is best for firms to adopt the same strategy. On the contrary, we consider an asymmetric case in which firms difer in their brand valuation. This modeling advantage allows us to identify and characterize asymmetric equilibria wherein competing firms may desire to utilize opposite strategies—one of the real-world observations we attempt to explain.

This paper is also related to existing studies that use discrete consumer types in the context of promotions (Banks and Moorthy 1999, Coughlan and Soberman 2005, Gerstner and Hess 1991, Gerstner et al. 1994, Iyer 1998, Jeuland and Narasimhan 1985, Lu and Moorthy 2007). All these papers assume that consumer segments vary in both reservation prices for a same product and redemption costs of a particular promotion. In line with them, we also consider a positive correlation between those two consumer characteristics—a desired property that allows for consumer self-selection—as a building block of our model. It is imperative for us to stress that we base our model on a widely accepted setting mainly because using a stylized model may cast doubts on the validity of our results. Once we introduce the afiliate’s role on the merchant’s pricing strategy in Section 2, readers will be able to see a clear diference between cash back and other discriminating mechanisms like coupons or rebates, as demonstrated in Lu and Moorthy (2007).

The rest of this paper is organized as follows. In Section 2, we develop our model by considering a market consisting of a monopolist merchant, a cash-back site, and heterogeneous consumers. The objective of this basic model is to better understand the market force under the cash-back mechanism. Section 3 investigates the impact of afiliate competition on the merchant’s afiliate and pricing strategies. Section 4 examines the strategic role of cash back in a competitive setting where merchants are asymmetric in their brand valuation. Concluding remarks are provided in Section 5.

## 2. Basic Model

In this section, we first introduce consumer response, consumer segments, and the merchant’s pricing alternatives in the absence of cash back. The preliminaries developed from noncash-back pricing serve as a benchmark for our analysis of the cash-back afiliate model. Next, we set up a model for cash-back pricing and derive firms’ optimal afiliate and pricing decisions at equilibrium. The results obtained from our basic model provide useful insights into the cash-back mechanism.

## 2.1. Non-Cash-Back Pricing—A Benchmark

2.1.1. Consumer Response. Consider a market consisting of a monopolist merchant m who sells a product to consumers with heterogeneous product preferences. In the spirit of a spatial model (Mehra et al. 2017), we assume that consumers are uniformly distributed on a line segment and the merchant’s product is located at one edge of the segment. Without loss of generality, the length of the line segment is normalized to 1. Let V denote the highest valuation consumers would possibly have for their ideal products. The location of a consumer represents the valuation she would have toward the product ofered by m. As a result, a consumer at distance x away from the product has a product valuation of $V - x . ^ { \overline { { 3 } } }$ Suppose that the merchant ofers the product at price p and the same consumer derives a transactional utility of $U ( x ) = V - x - p$ . Each consumer has a unitary demand and will buy the product if her transactional utility is nonnegative. In this setting, a general demand function can be expressed as $Q ( p ) =$ $V - p .$ , where $Q ( p ) \leq 1$ . Note that V is a general form for product valuation and its value is segment specific, as introduced in the next paragraph.

2.1.2. Consumer Segments. We normalize the total market size to one and consider the market with two types of consumers, l and h, with fractions θ and $1 - \theta ,$ respectively. The highest valuations are $V = v$ for type h consumers and $\bar { V = } \delta \boldsymbol { v }$ for type l consumers, where $\delta \in ( 0 , 1 )$ . Such an asymmetry in reservation price is widely accepted in marketing and economics literature on promotions $( \mathrm { e . g . }$ , Lu and Moorthy 2007). When type l’s valuation is relatively low (i.e., δ is small), we say the valuation gap between two segments is salient. Following the general demand function, we can formulate the demand from the type l and type h segments as $Q _ { l } ( p ) =$ $\theta \cdot ( \delta v - p )$ and $Q _ { h } \bar { ( p ) } = ( 1 - \bar { \theta ) \cdot } ( v - p \bar { ) }$ , respectively.

2.1.3. Uniform Pricing. Under the simplest pricing scheme, the merchant charges a uniform price $p _ { u }$ to the entire market and faces the following pricing problem:

$$
\underset {p _ {u}} {\text { maximize }} \pi_ {m} ^ {U} = p _ {u} \cdot Q _ {l} (p _ {u}) + p _ {u} \cdot Q _ {h} (p _ {u}).\tag{1}
$$

Maximizing (1) we can obtain the optimal uniform price. A remark from the analysis with uniform pricing is that the optimal price and market coverage depend on the regions market parameters $( v , \theta , \delta )$ fall in. 4

2.1.4. Discriminatory Pricing. Now suppose that the merchant can perfectly discern consumer types by using an ordinary promotional vehicle (e.g., issuing coupons) with an exogenous cost of K. Under this pricing model, the monopolist charges a lower price $p _ { l }$ to the low type and a higher price $p _ { h }$ to the high type. We call pricing terms $( p _ { l } , p _ { h } )$ the discriminatory prices. The merchant’s problem under discriminatory pricing can be expressed as

$$
\underset {p _ {l}, p _ {h}} {\text { maximum }} \pi_ {m} ^ {D} = p _ {l} \cdot Q _ {l} (p _ {l}) + p _ {h} \cdot Q _ {h} (p _ {h}) - K.\tag{2}
$$

Solving (2) yields the optimal discriminatory prices under an uncovered market $( p _ { l } ^ { * } , p _ { l } ^ { * } ) = ( \delta v / 2 , \dot { v / 2 } )$ . Perfect segmentation allows the price-setting merchant to exploit its monopoly power in both segments, and the merchant has an incentive to do so if $\pi _ { m } ^ { D * } - \pi _ { m } ^ { U * } \geq K .$ Since the lump-sum cost K is usually high, marketers with limited budgets may find discriminatory pricing unattractive. This issue is especially serious for small online business owners (Garth 2012).

Comparing the pricing terms across two pricing schemes yields the following remark.

Remark 1. The discriminatory pricing mechanism increases the price for consumers with higher valuation and decreases the price for those with lower valuation, compared to the optimal uniform price; that ${ \mathrm { i } } \mathbf { s } ,$ (1) $p _ { h } ^ { * } \geq p _ { u } ^ { * }$ and $( 2 ) p _ { l } ^ { * } < p _ { u } ^ { * }$

Proof. All proofs are available in the online appendix.

Remark 1 presents a common wisdom regarding the price change with an ordinary promotional device in place. After adopting discriminatory pricing, the merchant raises the price for one segment and lowers the price for the other (relative to the uniform price). In other words, the uniform price must be bound between the two discriminatory prices. However, we ask, can this intuition carry over in the cash-back afiliate model?

## 2.2. Cash-Back Pricing

A merchant listing on a cash-back site operates a digital dual channel. When a consumer desires to buy a certain product, she can either purchase it directly from the merchant’s online storefront (called the direct channel<sup>5</sup>) or via the referral link posted on a cash-back site (called cash-back channel). Of course, shopping through the cash-back channel is not costless. Cash-back users incur transaction costs including the disutility derived from extra work throughout the reward-earning process, such as registering on the cash-back site, connecting to merchants’ landing page, clicking through afiliate links, concerns with privacy and security, etc. Nevertheless, a consumer would still choose to use the site if the monetary incentive obtained from cash back was greater than the transaction costs. In the case where transaction costs are perceived to be higher, the consumer is assumed to make the purchase via the direct channel.

Denote the transaction costs incurred from cash-back shopping by $c _ { i } \ ( i = l , h )$ . Since the values of time are diferent across segments, we assume that the costs are lower for type l consumers, i.e., $c _ { l } < c _ { h }$ . The assumption that transaction cost is positively correlated with product valuation is widely used in the prior literature (e.g., Coughlan and Soberman 2005). Without loss of generality, we normalize $c _ { l }$ to zero. This normalization is justifiable in the following senses. From a consumer’s perspective, cash-back shoppers are a group of consumers who value saving beyond the time associated with getting discounts (Swan 2010). From an analytical perspective, the incentive for price discrimination still holds even if $c _ { l } > 0 .$ , as long as $c _ { l } < c _ { h }$ (Gerstner et al. 1994).

Consumers self-select whether to pay a regular price p or a promotional price ${ p _ { p } } ,$ depending on whether they shop through the cash-back site. In the context of online cash back, this low price is an ex post price perceived by consumers after factoring in cash-back rewards. We call this discounted price the post-cash-back price throughout this paper. The relative magnitude between one’s transaction cost $c _ { i } ,$ and the monetary incentive obtained from cash-back shopping, $\Delta p$ (we defined $\Delta p = p _ { r } - p _ { p } )$ , determines the outcome of the underlying self-selection mechanism (see Figure 1).

To best model the current cash-back practice, we consider a three-stage Stackelberg game with two players: a merchant and a cash-back site. In this paper, we examine two major afiliate fee models: the commission-based fee model and the lead-based fee model. In either model, the site collects the afiliate fees and pays consumer cash-back rewards (Williams 2014).

Commission-Based Fee Model. In the first stage, the merchant decides whether or not to afiliate with the cash-back site. If the merchant decides to afiliate, it then chooses a regular price $p _ { r }$ and a commission rate b $( b \in [ 0 , 1 ] )$ in the second stage. From the merchant’s point of view, the commission paid to the afiliate can be considered the cost of being able to price discriminate. In the third stage, the intermediary site makes b times the total revenue it brokers. Meanwhile, it chooses a cash-back rate a $( a \in [ 0 , b ] )$ and rewards its site users with a times the transactional amount in a form of cash back. The merchant’s marginal cost is assumed constant and can be normalized to zero by interpreting consumers’ product valuation as net of marginal cost. The afiliate incurs a zero marginal cost since it merely operates as an intermediary and does not directly deal with purchase transactions or shipping and handling. Two firms work independently and maximize their own profits. With the commissionbased fee model, the merchant’s and the site’s problems can be respectively formulated as

Figure 1. Consumer’s Self-Selecting Process Under the Cash-Back Mechanism  
![](/api/attachments/JVCG2KQ7/fulltext/images/9af064cd96aab74aba723e885b157d3f035e5f3272054687db01fb358f1f5579.jpg)

$$
\underset {p _ {r}, b} {\text { maximize }} \pi_ {m} ^ {C} = p _ {r} (1 - b) \cdot Q _ {l} (p _ {r} (1 - a)) + p _ {r} \cdot Q _ {h} (p _ {r}),\tag{3}
$$

$$
\underset {a} {\text { maximize }} \pi_ {s} ^ {C} = p _ {r} (b - a) \cdot Q _ {l} (p _ {r} (1 - a)).\tag{4}
$$

We use a superscript C to denote the commissionbased fee model and subscripts m and s to denote the merchant and the site, respectively.

For the cash-back model to work as a price-discrimination device, type h consumers’ incentive compatibility (IC) constraints must be satisfied.<sup>6</sup> Critical readers may argue that the merchant’s desire to sort out consumers is not necessarily aligned with the site’s best interest, as the site may have an incentive to entice type h consumers as well by setting a higher cash-back rate. In fact, this would never happen in theory. Once both types of consumers became cash-back shoppers, all consumers would pick the cash-back channel and pay the lower price: nominal asymmetric prices actually work like a single price. The merchant’s net profit, defined as sales revenue minus commission, would be strictly less than the level that could be achieved by the optimal uniform price. If this were the case, the merchant would rather simply set a uniform price and leave the site, which would end up making a zero profit without any commission revenue. Such a credible threat tightly aligns the interests of two afiliate partners under the cash-back pricing model.

Lead-Based Fee Model. Under the lead-based fee model, the afiliate moves first by announcing a fixed charge f for every transaction led via the referral link. Observing this preannounced fee, the merchant then makes its afiliate decision. If the merchant decides to afiliate, it then sets a regular price $p _ { r }$ and chooses a cash-back rate a. In this pricing scheme, the merchant is able to dictate the two asymmetric prices by accepting the fixed charge f ofered by the afiliate. As a result, the problems faced by two firms with the lead-based fee model (L) are given by

$$
\underset {f} {\text { maximize }} \pi_ {s} ^ {L} = f \cdot Q _ {l} (p _ {r} (1 - a)),\tag{5}
$$

$$
\begin{array}{c} \underset {p _ {r}, a} {\text {maximize}} \pi_ {m} ^ {L} = [ p _ {r} (1 - a) - f ] \cdot Q _ {l} (p _ {r} (1 - a)) \\ + p _ {r} \cdot Q _ {h} (p _ {r}). \end{array}\tag{6}
$$

Solving equation systems (3)–(6) using backward induction gives us optimal pricing terms.

Lemma 1(1). Under the commission-based fee model, the merchant sets the regular price $p _ { r } ^ { * } = v / 2$ and the commission rate $b ^ { * } = 1 - \delta$ . The afiliate site chooses the cash-back rate $a ^ { * } = 1 - 3 \delta / 2$

Lemma 1(2). Under the lead-based fee model, the afiliate site announces a fixed charge $f ^ { * } = \mathrm { \ i } v / 2$ for every sale it leads. The merchant sets the regular price $p _ { r } ^ { * } = v / 2$ and the cash-back rate $a ^ { * } = 1 - 3 \delta / 2$

As a pricing device, the cash-back mechanism allows the merchant to simultaneously charge a regular price $p _ { r } ^ { * } = v / 2$ and a lower post-cash-back price $\bar { p } _ { p } ^ { * } = 3 \bar { \delta } v / 4$ (given that $\delta < 2 / 3 )$ to diferent types of consumers. We call $( p _ { r } ^ { * } , p _ { p } ^ { * } )$ the asymmetric prices to distinguish them from the discriminatory prices introduced earlier. A cross-check between Lemmas 1(1) and 1(2) reveals that the asymmetric prices are identical across the two diferent fee models. An implication is that the choice of either model has no efect on the afiliate members’ joint profit nor various welfare measures; it only impacts how the joint profit is shared between the two afiliate members.

## 2.3. Afiliate Decision

We start our discussion on the merchant’s afiliate decision by analyzing the profitability of the two diferent fee models. Setting $\pi _ { m } ^ { \hat { C } * } \geq \pi _ { m } ^ { U * }$ and rearranging terms, we can characterize the conditions under which the commission-based fee model is profitable. Similarly, by evaluating $\pi _ { m } ^ { L * } \geq \pi _ { m } ^ { U * }$ we can derive the profitable conditions for the lead-based fee model.

Lemma 2(1). The commission-based fee model is profitable as long as $( \theta , \delta ) \in R _ { P } ^ { C }$ , where

$$
R _ {P} ^ {C} = \left\{(\theta , \delta) \Bigg | 0 <   \theta <   1 - \frac {\delta^ {2}}{2 (1 - \delta) ^ {2}}, 0 <   \delta <   2 - \sqrt {2} \right\}.
$$

Lemma 2(2). The lead-based fee model is profitable as long as $( \theta , \delta ) \in R _ { P } ^ { L }$ , where

$$
R _ {P} ^ {L} = \left\{(\theta , \delta) \middle | 0 <   \theta <   1 - \frac {3 \delta^ {2}}{4 (1 - \delta) ^ {2}}, 0 <   \delta <   4 - 2 \sqrt {3} \right\}.
$$

Clearly, whether cash-back pricing outperforms uniform pricing is determined by market configuration.

In what follows, we discuss the efects of two market parameters, θ and δ, on the profitability of the cashback model, respectively. On one hand, given that the fraction of two segments (θ) is held fixed, the value of δ has an adverse efect on the cash-back model. This is because when δ is large, the asymmetric prices will be close to the uniform level, implying that the advantage of price discriminating diminishes. Nevertheless, when δ is small, the asymmetric prices will deviate from the uniform price to a large extent. In this case, the ability to segment the market will lead to a higher incremental profit. On the other hand, given that δ is held fixed, the efect of θ on the profitability of cash back is also negative. As the fraction of the lowtype goes up, a bigger portion of the merchant’s total revenue is generated through the cash-back channel, implying that the afiliate would demand larger afiliate fees. Combined, these two efects suggest that the cash-back afiliate model is profitable if and only if θ and δ are suficiently small. As (θ, δ) become smaller (larger), the merchant’s preference will shift toward (away from) cash-back pricing.

## 2.4. The Cash-Back Paradox

The cash-back mechanism allows the merchant to extract the highest surplus from high-valuation consumers by raising the price to the monopoly optimum, $p _ { h } ^ { * }$ . Such a price hike is consistent with the first inequality ${ p } _ { h } ^ { * } \ge { p } _ { u } ^ { * }$ specified in Remark 1. Following the second inequality, $p _ { l } ^ { * } < p _ { u } ^ { * }$ , we should expect the postcash-back price faced by low-valuation consumers to be lower than the uniform price. However, as the following proposition shows, this intuition is not necessarily true in the context of online cash back.<sup>8</sup>

Proposition 1. The “cash-back paradox,” meaning that the post-cash-back price is higher than the uniform level, will occur as long as the market configuration falls in the paradox region $R _ { X } ,$ where

$$
\begin{array}{l} R _ {X} = \big \{(v, \theta , \delta)   |   v <   2, \underline {{\theta}} <   \theta <   \bar {\theta}, \delta <   \frac {1}{2} \big \}, \\ \underline {{\theta}} = \left\{ \begin{array}{l l} \underline {{\theta}} _ {1} = \frac {1 - 2 \delta}{(1 - \delta) ^ {2}}, & i f    0 <   \delta \leq \frac {1}{3}, \\ \underline {{\theta}} _ {2} = \frac {2 - 3 \delta}{2 - 2 \delta}, & i f    \frac {1}{3} <   \delta <   \frac {1}{2}, \end{array} \right. a n d \\ \bar {\theta} = 1 - \frac {\delta^ {2}}{2 (1 - \delta) ^ {2}}. \end{array}
$$

Proposition 1 suggests a surprising result from the consumer’s perspective. Cash-back shopping seems to provide a savings opportunity for deal hunters, as the post-cash-back price they pay is perceived as lower than the regular price. Under some circumstances, however, this seemingly “low” price is actually “high” relative to the uniform level. In this situation, all consumers will end up facing higher prices under cash-back pricing; that is, $p _ { r } ^ { * } > p _ { p } ^ { * } > p _ { u } ^ { * }$ . In the following analysis, we characterize the paradox region and provide intuitive explanations behind such an uncommon phenomenon.

Figure 2. (Color online) Feasible Region of the Cash-Back Paradox  
![](/api/attachments/JVCG2KQ7/fulltext/images/def7c2c2fa148274612af311e687a5f3a7d76fe723f5fe59cd441d5bb7dbefd0.jpg)

For exposition purposes, we plot the paradox region, $R _ { X } ,$ on a θ–δ coordinate. From Figure 2, we can see that $R _ { X }$ is enveloped by three lines, each of which represents one constraint as a function of segment parameters. The first and an essential constraint is $p _ { p } ^ { * } > p _ { u } ^ { * } ,$ which we call the paradox constraint. Graphically, the paradox constraint is satisfied when <sup>(</sup>θ, δ<sup>)</sup> fall into the region above the dashed line. Next, we need to verify that $\pi _ { m } ^ { C * } \geq \pi _ { m } ^ { U } ,$ or the merchant’s rationality constraint, since the post-cash-back price will exist only when cash-back pricing is profitable. The rationality constraint is satisfied when <sup>(</sup>θ, δ<sup>)</sup> fall into the region below the solid line. Last, as discussed in the noncashback pricing, the merchant may desire to serve the type h segment only by setting the uniform price at the monopoly level $( \mathrm { i } . \mathrm { e } . , v / 2 )$ . In this situation, the cashback paradox would never happen because the cashback model would allow the monopolist merchant to charge a second, strictly lower price on the second channel. To rule out this special case, $( \theta , \delta )$ must fall into the region above the dotted line, which depicts the boundary of the service constraint. When segment parameters satisfy all three constraints simultaneously (as depicted in the shaded area), all consumers will suffer from higher prices under the cash-back mechanism. The identification of the cash-back paradox challenges a common wisdom regarding how price should change under a third-degree discriminating mechanism.

To investigate the market force driving the cash-back paradox, we plot various prices as a function of θ in Figure 3, with the optimal uniform price being normalized to 1. Note that $p _ { r } ^ { * }$ and $p _ { p } ^ { * }$ are truncated at $\theta = \bar { \theta }$ since the merchant’s rationality constraint is violated when $\theta > \bar { \theta }$ . To see the efect of $\theta$ on various pricing terms, consider the following extreme cases. When $\theta = 1 , p _ { u } ^ { * } = p _ { l } ^ { * }$ because all consumers are of the low type; when $\theta = 0 , p _ { u } ^ { * } = p _ { h } ^ { * }$ because all consumers are now of the high type. When the value of θ falls between these two extremes, we should expect that the uniform

Figure 3. Comparison of Various Prices (δ <sup></sup> 0.4)  
![](/api/attachments/JVCG2KQ7/fulltext/images/77203312a86746b0975a4cbee5ff85e860c167a8ab012b28c7ec10519958acff.jpg)  
price is bound between two discriminatory prices, $\mathrm { i . e . , }$ $p _ { l } ^ { * } < p _ { u } ^ { * } \le p _ { h } ^ { * } .$ , as presented in Remark 1. According to industry practice, the merchants and the afiliate work independently and seek their own respective highest profits. The allocation of pricing power between two afiliate members in the cash-back model is analogous to that in a traditional reselling model where the manufacturer and the retailer independently set their respective prices. As seen in various online settings (Abhishek et al. 2016, Dellarocas 2012), this wellknown problem of double marginalization leads to an upward price distortion, raising the post-cash-back price above the monopoly level, $p _ { l } ^ { * } .$ . When $\theta > \underline { { \theta } } .$ , the <sup>¯</sup>strength of the upward price distortion would prevail such that $p _ { p } ^ { * } > p _ { u } ^ { * } .$ , satisfying the paradox constraint defined earlier. In this situation, while two asymmetric prices both exceed the uniform level, the merchant can still make an incremental profit with cash-back pricing. The intuition behind this anomalous outcome is as follows. The price changes on afiliating have two opposing efects on the merchant’s profit. On one hand, the afiliating merchant enjoys a revenue gain from the type h segment because the regular price is raised to the monopoly level. On the other hand, it sufers a revenue loss from type l segment as the post-cashback price is suboptimal due to the upward distortion. When $\theta < \bar { \theta } .$ , the revenue gain from the more lucrative segment will outweigh the revenue loss from the other, making cash-back pricing a preferable strategy. As a result, the phenomenon of the cash-back paradox will happen only when $\theta \in [ \theta , \bar { \theta } ]$ . If θ is too small, the <sup>¯</sup>strength of the upward distortion will be too weak such that the paradox constraint is violated. Yet, if θ is too large, the revenue loss due to the price distortion will dominate, violating the rationality constraint.

## 3. Pricing Decisions Under Afiliate Competition

As introduced in Section 2.2, a cash-back afiliate merely serves as an online intermediary and is not responsible for most operations such as holding inventory, shipping and handling, providing postpurchase services, etc. This low entry barrier attracts huge afiliate competition as we observe in practice. Understanding how such competition impacts the cash-back mechanism is of much significance because its presence reallocates market power among the afiliate members. In this section, we develop our first extension by incorporating consumers’ choice between two competing sites into the basic model.

It is imperative for us to point out some notable characteristics of cash-back shopping before going into modeling details. Cash-back users are savvy deal hunters who highly appreciate saving to be available on the Internet (Swan 2010). Thanks to the cash-back comparison service $( \mathrm { e . g . }$ , cashbackholic.com), they can easily compare deals across various sites and switch to whichever site ofers the deepest discount. While most cash-back sites operate in a similar way, each shopper has her own site preference for many reasons (Williams 2014). For example, one prefers to use a particular site perhaps because she had pleasant shopping experiences with that site before, or because she had a habit of collecting rewards at the same site for a bigger redemption check. In practice, cash-back sites implement various policies and features to encourage repurchases and retain customers. For example, MrRebates has a redemption policy that users can cash out their cash-back rewards only when the balance reaches \$10 or above.<sup>9</sup> As a consequence, cash-back users will take into account not only the discount depth but also their own site preference when making an afiliate choice (Williams 2014). It is worth noting that these priceoriented consumers are loyal to the idea of saving money rather than to particular cash-back sites (Swan 2010). In other words, they are willing to switch to a less-preferred site if the merchant is not listed on their more preferred ones.

We now consider a market served by one merchant and two cash-back sites $( S _ { 1 }$ and $S _ { 2 } )$ . The merchant first decides whether to adopt cash-back pricing at all. If it does, it then chooses either to afiliate with $S _ { 1 }$ only, $S _ { 2 }$ only, or both of them. For ease of discussion, we refer to the first two scenarios as the single-afiliating cases and the third scenario as the multiafiliating case. In line with our basic model and the discussion earlier, we assume that all type l consumers are aware of the existence of both sites. Such a realistic assumption has an important implication—the single-afiliating merchant would not be able to reach new consumers by the mere action of listing on the second site. From a modeling perspective, this feature allows us to tease out the efect of the introduction of a competing site. We model consumer preference for the two afiliates in a Hotelling manner: given the same cash-back rate, a consumer will choose the afiliate that is closer to her. For now, we consider a symmetric setting in which there is no vertical diferentiation between two sites. Note that consumers’ site preference merely impacts their afiliate choice; it plays no role in the net transactional utility derived from shopping through either site. With these settings, the single-afiliating case is identical to the basic model. Accordingly, we can formulate the afiliate-specific demand in the multiafiliating case (denoted by the superscript AC) as

$$
Q _ {l, i} ^ {A C} (p _ {p, i}, p _ {p, - i}) = \frac {\theta}{2} \left[ (\delta v - p _ {p, i}) + \frac {- p _ {p , i} + p _ {p , - i}}{2} \right],\tag{7}
$$

where $i = S _ { 1 }$ or $S _ { 2 } ; - i = S _ { 2 }$ if $i = S _ { 1 }$ and $- i = S _ { 1 }$ otherwise. This demand function characterizes the important characteristics we have discussed earlier. First, it models the market response from consumers with heterogeneous site presence. Specifically, the terms inside the first parentheses represent site i’s demand from consumers who have a strong preference in site i’s favor, where the terms inside the second parentheses represent site $i \prime \mathrm { s }$ demand from those who are relatively indiferent between the two sites.<sup>10</sup> Second, observant readers may have noted that $Q _ { l , i } ^ { A C } = Q _ { l , - i } ^ { A C } = Q _ { l } / 2$ if $p _ { p , i } = p _ { p , - i }$ . This desired property implies that the market is irresponsive to the merchant’s mere action of enlisting with the second site. Instead, demand would depend only on the price changes as a result of afiliate competition.

Since each site may use either fee model, three cases arise:

• Case CC, where both sites use the commissionbased fee model;

• Case LL, where both sites use the lead-based fee model;

• Case LC, where $S _ { 1 }$ uses the lead-based model while $S _ { 2 }$ uses the commission-based model.

The sequence of the game is contingent on the choice of the fee models. In Case CC, the merchant moves first by choosing the regular price and the commission rates, followed by the choice of the cash-back rates by two sites. Accordingly, we can express the afiliate members’ profit-maximization problems as

$$
\underset {p _ {r}, b _ {1}, b _ {2}} {\text { maximize }} \pi_ {m} ^ {C C} = p _ {r} (1 - b _ {1}) \cdot Q _ {l, 1} ^ {A C} (p _ {p, 1}, p _ {p, 2}) + p _ {r} (1 - b _ {2})
$$

$$
\cdot Q _ {l, 2} ^ {A C} (p _ {p, 2}, p _ {p, 1}) + p _ {r} \cdot Q _ {h} (p _ {r}),\tag{8}
$$

$$
\underset {a _ {1}} {\text { maximize }} \pi_ {S _ {1}} ^ {C C} = p _ {r} (b _ {1} - a _ {1}) \cdot Q _ {l, 1} ^ {A C} (p _ {p, 1}, p _ {p, 2}),\tag{9}
$$

$$
\underset {a _ {2}} {\text { maximize }} \pi_ {S _ {2}} ^ {C C} = p _ {r} (b _ {2} - a _ {2}) \cdot Q _ {l, 2} ^ {A C} (p _ {p, 2}, p _ {p, 1}).\tag{10}
$$

In Case $\scriptstyle { \mathrm { L L } } ,$ afiliates move first by simultaneously announcing their respective fixed charges, and the merchant, in turn, sets the regular price and cash-back rates. Firms face the following problems:

$$
\underset {f _ {1}} {\text { maximize }} \pi_ {S _ {1}} ^ {L L} = f _ {1} \cdot Q _ {l, 1} ^ {A C} (p _ {p, 1}, p _ {p, 2}),\tag{11}
$$

$$
\underset {f _ {2}} {\text { maximize }} \pi_ {S _ {2}} ^ {L L} = f _ {1} \cdot Q _ {l, 2} ^ {A C} (p _ {p, 2}, p _ {p, 1}),\tag{12}
$$

$$
\begin{array}{r l} \underset {p _ {r}, a _ {1}, a _ {2}} {\text { maximize }} \pi_ {m} ^ {L L} & = (p _ {p, 1} - f _ {1}) \cdot Q _ {l, 1} ^ {A C} (p _ {p, 1}, p _ {p, 2}) + (p _ {p, 2} - f _ {2}) \\ & \quad \cdot Q _ {l, 2} ^ {A C} (p _ {p, 2}, p _ {p, 1}) + p _ {r} \cdot Q _ {h} (p _ {r}). \end{array} \tag {13}
$$

In Case $\operatorname { L C } , S _ { 1 }$ announces a fixed fee in the first stage. The merchant then sets the regular price, the cashback rate listed on $S _ { 1 } ,$ and the commission rate for $S _ { 2 }$ Finally, $S _ { 2 }$ determines the cash-back rate listed on its site. Firms’ problems can be written as

maximize $\pi _ { S _ { 1 } } ^ { L C } = f _ { 1 } \cdot Q _ { l , 1 } ^ { A C } ( p _ { p , 1 } , p _ { p , 2 } ) ,$ f<sub>1</sub>

$$
\underset {p _ {r}, a _ {1}, b _ {2}} {\text { maximize }} \pi_ {m} ^ {L C} = (p _ {p, 1} - f _ {1}) \cdot Q _ {l, 1} ^ {A C} (p _ {p, 1}, p _ {p, 2}) + p _ {r} (1 - b _ {2})\tag{14}
$$

$$
\cdot Q _ {l, 2} ^ {A C} (p _ {p, 2}, p _ {p, 1}) + p _ {r} \cdot Q _ {h} (p _ {r}),
$$

$$
\underset {a _ {2}} {\text { maximize }} \pi_ {S _ {2}} ^ {L C} = p _ {r} (b _ {2} - a _ {2}) \cdot Q _ {l, 2} ^ {A C} (p _ {p, 2}, p _ {p, 1}).\tag{15}
$$

(16)

Using backward induction, we can solve for the optimal pricing terms, which are presented in the following lemma.

Lemma 3. (a) Case CC. The merchant sets symmetric commission rates $b _ { 1 } ^ { C C } = b _ { 2 } ^ { C C } = 1 - \delta ,$ , and two afiliates choose symmetric cash-back rates $a _ { 1 } ^ { C C } = a _ { 2 } ^ { C C } = 1 - 7 \ddot { \delta } / 5$

(b) Case LL. Two afiliates announce symmetric fixed charges $f _ { 1 } ^ { L L } = f _ { 2 } ^ { L L } = 2 \delta \ddot { v / 5 }$ , and the merchant sets symmetric cash-back rates $\stackrel {  } { a } _ { 1 } ^ { L L } = a _ { 2 } ^ { L \dot { L } } = 1 - 7 \delta / 5$

(c) Case LC. $S _ { 1 }$ announces the fixed charge $f _ { 1 } ^ { L C } = 7 \delta v / 1 7 ,$ and $S _ { 2 }$ chooses the cash-back rate $a _ { \scriptscriptstyle 7 } ^ { \scriptscriptstyle L C } = 1 - \bar { 1 4 } 3 \delta / 1 0 2$ . The merchant lists the cash-back rate $a _ { 1 } ^ { L C } = 1 - 2 4 \delta / 1 7$ on $S _ { 1 }$ and sets the commission rate $b _ { \gamma } ^ { L C } = 1 - \stackrel { \cdot } { \delta } f o r S _ { 2 }$

The merchant sets the regular price at $v / 2$ in all cases.

The choice of fee models has an impact on the optimal cash-back rates. If the two afiliates use the same model (CC and LL), the post-cash-back prices are identical; however, if the two afiliates use diferent models (LC), the prices available on $S _ { 1 }$ and $S _ { \gamma }$ are $1 2 \delta v / 1 7$ and 143δv<sup>/</sup>204, respectively. In Case ${ \mathrm { L C } } ,$ the Stackelberg leader $S _ { 1 }$ possesses more pricing power and therefore can set a higher price than $S _ { 2 }$ . A comparison between Lemmas 1(1) and 1(2) and Lemma 3 reveals insight into the impact of afiliate competition on the optimal asymmetric prices. While the regular price remains at the monopoly level still, the post-cash-back prices across all three cases are lower than the one from the basic model. The intuition is that the competition between afiliates poses a downward pressure on the afiliate fees, leading to a decrease in the post-cash-back price. Such a market force helps moderate the problem of double marginalization in the cash-back channel. As a result, the merchant makes a higher profit and cashback users enjoy a reduced price. We formally conclude the associated discussions in the proposition below.

Proposition 2. It is in the merchant’s best interest to afiliate with multiple cash-back sites. The resulting competition improves market eficiency, resulting in higher merchant profit and greater consumer surplus.

Proposition 2 echoes a real-world observation that merchants who adopt cash-back pricing often list on multiple cash-back sites. The presence of afiliate competition suppresses the upward price distortion and hence drives down the post-cash-back price. An immediate follow-up question is, will the cash-back paradox continue to happen under the situation of afiliate competition? Proposition 3 provides the answer.

Proposition 3. The cash-back paradox phenomenon will still arise as long as market configuration $( \theta , \delta ) .$ falls in $R _ { X } ^ { C C }$ for Case CC, $R _ { X } ^ { \breve { L } L } f o r$ Case $L L ,$ and $R _ { X } ^ { L C }$ for Case $L C ,$ where

$$
R _ {X} ^ {C C} = \{(\theta , \delta) | \underline {{\theta}} _ {1} <   \theta <   \bar {\theta} _ {1}, \delta <   1 / 2 \},
$$

$$
\underline {{\theta}} _ {1} = \left\{ \begin{array}{l l} 1 - \frac {\delta^ {2}}{(1 - \delta) ^ {2}} & \text {   if   } 0 <   \delta \leq \frac {2}{7}, \\ 1 - \frac {2 \delta}{5 (1 - \delta)} & \text {   if   } \frac {2}{7} <   \delta <   \frac {1}{2}, \end{array} \right. \quad \bar {\theta} _ {1} = 1 - \frac {2 \delta^ {2}}{5 (1 - \delta) ^ {2}},
$$

$$
R _ {X} ^ {L L} = \{(\theta , \delta) | \underline {{\theta}} _ {2} <   \theta <   \bar {\theta} _ {2}, \delta <   5 / 1 3 \},
$$

$$
\underline {{\theta}} _ {2} = \left\{ \begin{array}{l l} 1 - \frac {\delta^ {2}}{(1 - \delta) ^ {2}} & \text {   if   } 0 <   \delta \leq \frac {2}{7}, \\ 1 - \frac {2 \delta}{5 (1 - \delta)} & \text {   if   } \frac {2}{7} <   \delta <   \frac {5}{1 3}, \end{array} \right. \quad \bar {\theta} _ {2} = 1 - \frac {1 6 \delta^ {2}}{2 5 (1 - \delta) ^ {2}},
$$

$$
R _ {X} ^ {L C} = \{(\theta , \delta) | \underline {{\theta}} _ {3} <   \theta <   \bar {\theta} _ {3}, \delta <   1 6 4 / 3 7 9 \},
$$

$$
\begin{array}{l} \underline {{\theta}} _ {3} = \left\{ \begin{array}{l l} 1 - \frac {\delta^ {2}}{(1 - \delta) ^ {2}} & \text { if } 0 <   \delta \leq \frac {4 1}{1 4 3}, \\ 1 - \frac {4 1 \delta}{1 0 2 (1 - \delta)} & \text { if } \frac {4 1}{1 4 3} <   \delta <   \frac {1 6 4}{3 7 9}, \end{array} \right. \\ \bar {\theta} _ {3} = 1 - \frac {2 1 5 \delta^ {2}}{4 0 8 (1 - \delta) ^ {2}}. \end{array}
$$

The insight we have established from Proposition 1 remains applicable in the multiafiliate scenario; that is, the cash-back paradox will occur as long as the following three conditions are all satisfied: the paradox constraint, the merchant’s rationality constraint, and the service constraint. Since the third constraint is irresponsive to the asymmetric prices, the introduction of the second afiliate plays no role here; yet, it does have two opposing efects on the first two constraints. As Proposition 2 suggests, the sites’ desire to compete for type l consumers drives the post-cash-back price down. This first impact, which we call the price efect of afiliate competition, tightens the paradox constraint. Nevertheless, such a price drop also increases the profitability of cash-back pricing. This second impact, which we call the profitability efect of competition, loosens the rationality constraint. As depicted in Figure 4, the price efect of competition moves the paradox constraint upward (from the dashed line to the solid line in the left panel) and shrinks the feasible region of the cash-back paradox. On the contrary, the profitability efect of competition expands the paradox region by moving the rationality constraints upward (as shown in the right panel). Combined, these two opposing efects shift the paradox region away from the origin of the $\theta { - } \delta$ coordinate. In the end, cash-back users may still sufer from the upward-distorted prices under the situation of afiliate competition.

For completeness, we also consider an asymmetric scenario where one site is more favored by consumers than the other site. To accommodate this feature in our Hotelling competitive model, we allow the two afiliates to have asymmetric heights (vertical distance from the merchant to the horizontal line) and interpret the height diference as the extent to which an average consumer prefers one site to the other. The advantage of the Stackelberg leader is still applicable in this setting. Intuitively, since the more-favored site possesses more pricing power, it will enjoy a higher margin for every sale it leads and thus make a higher profit. Despite the nuances of firms’ optimal pricing schemes, the main insights established from the symmetric scenario carry over.

## 4. Strategic Role of Cash Back

Our analysis of afiliate competition has ofered a useful implication for e-business owners: the merchant can increase its profits by engaging competition among cash-back sites. What remains unclear so far is the economic impact of cash back in the presence of merchant competition. A real-world observation is that some merchants choose to adopt cash-back pricing but some do not. To search for reasons behind this phenomenon, in this section we develop an extension to better understand what type of merchants are more attracted to the cash-back model.

Suppose that the market consists of one cash-back site and two merchants $( M _ { 1 }$ and $M _ { 2 } )$ who sell diferentiated products. We consider a general setting in which the product diferentiation is both vertical and horizontal. On one hand, two merchants difer in brand valuation perceived by consumers. Several factors may determine a merchant’s valuation such as its brand image, level of customer services, reputation, and so on. In line with our basic model, we assume that type h consumers have brand valuation $v _ { j }$ and type l consumers have brand valuation $\delta \boldsymbol { v } _ { j }$ for merchant $M _ { j } \left( j = \right.$ 1, 2). Without loss of generality, we further assume that $v _ { 1 } = v > \Delta \cdot v = v _ { 2 } .$ , where $\Delta \in ( 0 , 1 )$ .

On the other hand, the products ofered by the two merchants have various combinations of attributes as well. We model such diferences in product attributes as Hotelling-like horizontal diferentiation. Two merchants are located at two edges of the consumers’ preference line with unit length. The distance between a consumer and a given merchant represents the degree of a misfit between her ideal product and the product ofered by the merchant. The consumer at distance x away from $M _ { 1 }$ incurs a misfit cost $T x$ for the product ofered by $M _ { 1 }$ and $T ( 1 - x )$ for the product ofered by $M _ { 2 } .$ Parameter $T$ captures the consumer trade-of between the price and product attributes, and we can interpret its reciprocal as the intensity of merchant completion. When $T$ is large, we say that consumers are more product oriented and less willing to sacrifice their preferred product attributes. In this situation, competition is milder and the merchants possess more market power. As T continues to increase, our duopoly model will reduce to the basic model in which the two merchants simply act as two local monopolists. It is straightforward that as long as $T$ is suficiently large, the cash-back paradox will continue to occur even in the presence of merchant competition.

Figure 4. (Color online) Impact of Afiliate Competition on the Cash-Back Paradox  
(a) Shifting in paradox constraint  
![](/api/attachments/JVCG2KQ7/fulltext/images/455f8831738557c497dc6a81732a57ffd79ab0b07b1a7d845558ebd8cb216ce5.jpg)

We flexibly allow $T$ to vary across the two segments. Denote the misfit cost of type h and type l consumers by t and $d \cdot t ,$ where $d \in ( 0 , \dot { 1 } )$ , respectively. $^ { 1 1 }$ This setting of asymmetric misfit cost is commonly adopted in the segmentation literature (e.g., Coughlan and Soberman 2005, Shafer and Zhang 1995). Suppose that $M _ { j }$ sells its product at a nonnegative price $p _ { j } .$ . Type h consumers derive net utilities $U _ { h , 1 } ^ { - } ( x ) = \boldsymbol { v } - p _ { 1 } - \boldsymbol { t } \boldsymbol { x }$ and $U _ { h , 2 } ( x ) =$ $\Delta v - p _ { 2 } - t ( 1 - x )$ , and type l consumers derive net utilities $U _ { l , 1 } ( x ) = \delta v - p _ { 1 } - d t x$ and $U _ { l , 2 } ( x ) = \Delta \delta v -$ $p _ { 2 } - d t ( 1 - x ) ,$ , from the products ofered by $M _ { 1 }$ and $M _ { 2 } ,$ , respectively. Accordingly, we can formulate the merchant-specific, segment-specific demand in general forms as follows:

$$
Q _ {l, j} (p _ {p, j}, p _ {p, - j}) = \frac {\theta}{2} \left[ (\delta \nu - p _ {p, i}) + \frac {- p _ {p , i} + p _ {p , - i}}{2} \right],\tag{17}
$$

$$
Q _ {h, j} \left(p _ {r, j}, p _ {r, - j}\right) = (1 - \theta) \cdot \frac {1 + I _ {j} \cdot (1 - \Delta) v - p _ {r , j} + p _ {r , - j}}{2 t},\tag{18}
$$

where $j = M _ { 1 }$ or $M _ { 2 } ; - j = M _ { 2 } { \mathrm { ~ i f ~ } } i = M _ { 1 } .$ , and $- j = M _ { 1 }$ otherwise; and $I _ { j }$ indicates $M _ { j } ^ { \prime } \mathbf { s }$ relative advantage (or disadvantage) in vertical diferentiation such that $I _ { i } = 1$ if $j = M _ { 1 }$ , and $I _ { i } = - 1$ if $j = M _ { 2 }$ . If $M _ { j }$ afiliates, then $p _ { p , j } = p _ { r , j } ( 1 - a _ { j } ) ; p _ { r , j } = p _ { p , j }$ otherwise.

A challenge that arises from our two-merchant extension is that the site would have no incentive to ofer cash-back deals to consumers when both merchants decide to afiliate. This issue arises because of the assumption of constant demand in a classic Hotelling model. To overcome this dificulty, we consider that the afiliate members negotiate through a bargaining mechanism as follows. Suppose $M _ { j } ' \boldsymbol { \mathbf { s } }$ and the cash-back site’s relative bargaining power is $\varphi _ { j }$ and $1 - \varphi _ { j } ,$ respectively. Following Dukes et al. (2006), the values of bargaining parameters are exogenous and depend on each party’s relative market power such as market value, consumer base, etc. Each merchant and the site bargain over the afiliate fees. If bargaining fails, two firms resort to their outside options. In our research context, a merchant’s outside option is naturally the highest profit with uniform pricing. On the afiliate’s side, her outside option equals the fees she can collect from the other merchant; it will be zero if the other merchant does not afiliate. If bargaining succeeds, afiliate members split the total cash-backchannel revenue based on their respective bargaining power and bargaining position (Dukes et al. 2006). From an economic perspective, we can interpret the magnitude of $\varphi _ { j }$ as the attractiveness of cash back to $M _ { j } . \operatorname { A s } \varphi _ { j }$ gets larger, $M _ { i }$ will be more attracted to the cash-back model, because it will keep a bigger portion of the channel revenue. The Nash (1950) bargaining solution is the optimal afiliate fee that maximizes the following equation, given other pricing terms being at optimum:

(b) Shifting in rationality constrain  
![](/api/attachments/JVCG2KQ7/fulltext/images/9226985f3b9b6153819508ce49cb1f85e45d1200c0972d7815c5b07fce111817.jpg)

$$
\begin{array}{c} \underset {b _ {j} ^ {B}} {\text { maximize }} \Pi^ {B} = \varphi_ {j} [ p _ {r, j} ^ {*} (1 - b _ {j} ^ {B}) Q _ {l, j} + p _ {r, j} ^ {*} Q _ {h, j} - \tilde {\pi} _ {j} ] \\ \cdot (1 - \varphi_ {j}) [ p _ {r, j} ^ {*} (b _ {j} ^ {B} - a _ {j} ^ {*}) Q _ {l, j} - \tilde {\pi} _ {s} ], \end{array}\tag{19}
$$

where superscript B denotes the quantities associated with the bargaining process, and $\tilde { \pi } _ { j }$ and $\tilde { \pi } _ { s }$ represent $M _ { j } ' s$ and the site’s outside options, respectively. Exogenous bargaining parameters serve to allocate the incremental profit achieved through price discrimination. $\mathrm { A g a i n } , M _ { j } ' \mathbf { s }$ incentive to afiliate is monotonically increasing in the value of $\varphi _ { j }$

Since each firm can decide whether to afiliate or not, four possible cases arise: $M _ { 1 }$ afiliates alone (Case 1A, or $\mathrm { C _ { 1 A } }$ for short), $M _ { 2 }$ afiliates alone (Case 2A, or $\mathrm { C } _ { 2 \mathrm { A } }$ for short), both merchants afiliate, and neither merchant afiliates. We shall note that a merchant’s profit depends not only on its own pricing strategy but also on its rival’s. This nature adds extra dificulty to our duopoly model as the profit functions of all firms are discontinuous in the parameter space. Since our goal is to investigate which merchant has a higher incentive to adopt cash-back pricing, our analyses focus on the two asymmetric cases where one merchant afiliates alone (Cases 1A and 2A). Using backward induction, we can solve for the optimal pricing terms of the three afiliate members.

Lemma 4. In the asymmetric cases where one merchant afiliates alone, the optimal pricing terms are as follows:

$$
p _ {r, 1} ^ {*} = \left\{ \begin{array}{l l} \frac {4 d t + 2 \tilde {d} + [ \theta (1 - \delta) + 2 \tilde {d} ] (1 - \Delta) v}{6 \tilde {d}} & \text {if C_{1A}}, \\ \frac {2 d t + \tilde {d} + [ \theta \delta + (1 - \theta) d ] (1 - \Delta) v}{3 \tilde {d}} & \text {if C_{2A}}, \end{array} \right.
$$

$$
p _ {r, 2} ^ {*} = \left\{ \begin{array}{l l} \frac {4 d t - \tilde {d} - [ \theta \delta + (1 - \theta) d ] (1 - \Delta) v}{3 \tilde {d}} & \text {if C_{1A}}, \\ \frac {8 d t + 6 \theta (1 - d) t - 2 \tilde {d} - [ \theta (1 - \delta) + 2 \tilde {d} ] (1 - \Delta) v}{6 \tilde {d}} & \text {if C_{2A}}, \end{array} \right.
$$

$$
\begin{array}{r l r} & & {a _ {1} ^ {*} = \frac {3 \tilde {d} (1 - \delta) (1 - \Delta) v}{4 d t + 2 \tilde {d} + [ \theta (1 - \delta) + 2 \tilde {d} ] (1 - \Delta) v} \quad i f C _ {\mathrm{1A}},} \\ & & {a _ {2} ^ {*} = \frac {3 \tilde {d} [ 2 (1 - d) t - (1 - \delta) (1 - \Delta) v ]}{8 d t + 6 \theta (1 - d) t - 2 \tilde {d} - [ \theta (1 - \delta) + 2 \tilde {d} ] (1 - \Delta) v}} \\ & & {i f C _ {\mathrm{2A}},} \end{array}
$$

where $\tilde { d } = \theta + ( 1 - \theta ) d .$

Although we have solved for the optimal pricing terms, the solutions themselves do not constitute equilibrium. To derive equilibrium conditions, we need to verify that it is in the best interest of both merchants to stick to a given solution set. The process proceeds as follows. First, we compute two merchants’ profits given the optimal pricing terms presented in Lemma 4. We then identify conditions under which neither of them has an incentive to deviate by switching its afiliate decision (from afiliating to nonafiliating and vice versa). For example, in Case 1A, we check that (1) $M _ { 1 }$ has no incentive to cease cash-back pricing and that (2) $M _ { 2 }$ does not desire to enlist with the cash-back site. Lemma 5 presents the equilibrium conditions for the two asymmetric cases.

Lemma 5. We characterize the equilibrium conditions using the cutof values with respect to product valuation, v, and the two merchants’ bargaining power relative to the cash-back site $( \varphi _ { 1 } , \varphi _ { 2 } )$

(1) The equilibrium where $M _ { 1 }$ afiliates alone exists when $( v , \varphi _ { 1 } , \varphi _ { 2 } ) \in R _ { 1 A }$

(2) The equilibrium where $M _ { 2 }$ afiliates alone exists when $( v , \varphi _ { 1 } , \varphi _ { 2 } ) \in R _ { 2 A } ,$ , where

$$
\begin{array}{c} R _ {1 A} = \Bigg \{(v, \varphi_ {1}, \varphi_ {2}) \bigg | 4 \tilde {v} / 3 <   v, \\ 1 - \left(\frac {4 (1 - d) t - (1 - \delta) (1 - \Delta) v}{2 (1 - \delta) (1 - \Delta) v}\right) ^ {2} = \tilde {\varphi} _ {1} <   \varphi_ {1} <   1, \\ 0 <   \varphi_ {2} <   1 \Bigg \}, \end{array}
$$

$$
\begin{array}{c} R _ {2 A} = \Bigg \{(v, \varphi_ {1}, \varphi_ {2}) | 6 \tilde {v} <   v, 0 <   \varphi_ {1} <   1, \\ 1 - \frac {1}{4} \bigg (\frac {2 (1 - d) t - (1 - \delta) (1 - \Delta) v}{2 (1 - d) t + (1 - \delta) (1 - \Delta) v} \bigg) ^ {2} = \tilde {\varphi} _ {2} <   \varphi_ {2} <   1 \Bigg \} \\ a n d \quad \tilde {v} = \frac {(1 - d) t}{(1 - \delta) (1 - \Delta)}. \end{array}
$$

For exposition purposes, let us define $R ^ { 1 2 } \equiv \left\{ R ^ { 1 A } \cap \right.$ $R ^ { 2 A } \}$ . An immediate implication from Lemma 5 is that $R ^ { 1 2 } \in \mathcal { O }$ , suggesting that the two asymmetric equilibria would coexist when parameters fall in $R ^ { 1 2 }$ . Economists refer to such a special outcome as a chicken game (also known as a hawk-dove or snowdrift game), an anticoordination game where it is mutually beneficial for both merchants to play opposite afiliate strategies. To see the intuition behind it, consider the equilibrium in Case 1A. Clearly, $M _ { 1 }$ will adopt cash-back pricing only when its rationality constraint is satisfied. If this is the case, the cash-back mechanism will naturally raise $M _ { 1 } ^ { \prime } \boldsymbol { \mathrm { s } }$ regular price, lessening the competition in the type h segment. The lessened competition in the more lucrative type h segment may, in turn, give rise to a higher profit for $M _ { 2 }$ as well. In this “win–win” situation, two competing firms have no incentive to move alone but prefer their rival to do so. The identification of such an anticoordination game, to our knowledge, has not yet been discovered in the promotions literature. We attribute this interesting finding to the presence of the afiliate site in the cash-back model—which has been the unique aspect of this research.

To examine which merchant is more attracted to cash-back pricing, we investigate equilibrium attraction, an approach often used in games with multiple equilibria coexisting (Fudenberg and Levine 1998). By evaluating the cutof values with respect to the same parameter, we can measure the relative strength of multiple equilibria and conclude which of them are most likely to emerge. Since $M _ { j } ' s$ profit strictly increases with $\varphi _ { j } ,$ we can interpret $\tilde { \varphi } _ { j }$ as the minimal value of $\varphi _ { j }$ satisfying $M _ { j } ' s$ rationality constraint. We can show that $\tilde { \varphi } _ { 1 } > \tilde { \varphi } _ { 2 }$ when $( v _ { 1 } , \varphi _ { 1 } , \varphi _ { 2 } ) \in R _ { 1 2 }$ The inequality indicates that the equilibrium wherein $M _ { 2 }$ afiliates alone is more likely to emerge. To illustrate, we plot $\tilde { \varphi } _ { j }$ as a function of v in Figure 5. When

Figure 5. Cutof Values of $\varphi _ { j }$ Under Asymmetric Equilibria $( \theta = \delta = \Delta = d = t = 0 . 5 )$  
![](/api/attachments/JVCG2KQ7/fulltext/images/3f15d35c07fbf4333501229ae5163f402b98575dc5243af4d232a9cf4e3a4e93.jpg)  
$v = 9 \tilde { v } , M _ { 2 }$ will afiliate as long as its bargaining power is higher than a moderate threshold $( \varphi _ { 2 } > \tilde { \varphi } _ { 2 } = 0 . 3 8 )$ Ceteris paribus, $M _ { 1 }$ in contrast will follow the same strategy only when its bargaining power is excessively high $( \varphi _ { 1 } > \tilde { \varphi } _ { 1 } = 0 . 9 2 )$ . Based on this result, we formally conclude our asymmetric-equilibria analysis in Proposition 4.

Proposition 4. In a scenario where merchants are asymmetric in their brand valuations, those with relatively low valuation are more attracted to the cash-back model. One is more likely to observe low-valuation merchants listing on cash-back sites alone, compared to high-valuation merchants afiliating alone.

Proposition 4 ofers a sharp insight into the strategic role of cash back in a competitive setting. Online merchants with relatively inferior brand valuation, perhaps because of their positioning strategy or disadvantage in operational aspects, have a higher incentive to compete for price-oriented consumers. The cashback afiliate model, as a discriminating device, provides them with the ability to segment the market. As a result, low-valuation merchants should engage in a price war through strategically ofering cash-back deals. Superior merchants, on the contrary, should refrain from engaging in price competition because doing so would weaken their existing advantage in brand valuation. This finding explains why most premium brands are often absent on cash-back sites (e.g., Apple in consumer electronics and various high-end designer brands in the fashion industry).

## 5. Conclusion

The primary objective of this paper has been to examine the economic impact of the cash-back afiliate model on merchants’ pricing strategies. Through afiliating with the cash-back site, merchants are able to exercise third-degree price discrimination by operating a digital dual channel. To obtain a basic understanding of such a novel mechanism, we begin our analyses by characterizing the conditions under which cash-back pricing outperforms uniform pricing. We show that the presence of the intermediary not only undermines the advantages of price discriminating, but causes an upward distortion on prices targeted at cash-back users. Under some conditions, all consumers (both cash-back users and nonusers) end up facing higher prices, compared with the uniform price they would have faced in the absence of discrimination. This finding is especially surprising to the cash-back shoppers since the perceived lower price turns out to be high.

This research also provides several managerial implications for online merchants in the following aspects. First, online merchants have an incentive to adopt a multihoming strategy by afiliating with multiple cash-back sites as the resulting competition will drive the afiliate fees down and improve market eficiency. Moreover, while such competition puts a downward pressure on prices, cash-back shoppers may still face a higher price as long as they have heterogeneous preferences for the competing sites. Finally, merchants that are disadvantageous in brand valuation should strategically utilize cash-back pricing to compete for price-oriented consumers.

Like other analytical work, our model certainly makes a few assumptions. First, the demand function faced by the merchants and the afiliates is assumed to be linear in our model. Yet, none of our results depends on this linearity assumption. For example, the upward price distortion stemming from double marginalization would be even stronger if the marginal revenue curve were assumed to be convex, as the afiliate would try to get a bigger pie by setting a cash-back rate further deviating from the channel optimum. Second, we assume in our basic model that the consumers’ sensitivity to horizontal diferentiation is identical across two segments $( t _ { h } = t _ { l } )$ . In fact, our results remain qualitatively the same if we release this assumption. When $t _ { h } > t _ { l }$ , a monopolist merchant would have a higher incentive to price discriminate, making our extant analysis on afiliate decision conservative. In other words, the profitable region of cash back would expand under this circumstance. Third, we do not investigate the role of demand elasticity on the profitability of cash back. Mathematically speaking, the efect of demand elasticity on a merchant’s profit is similar to that of the misfit cost discussed above. If we assume that the demand of the type l segment is more elastic than the demand of the other, the profitability of cash back would increase with the elasticity diference between two segments.

It is our hope that this research may simulate further interests in such a novel and still-nascent online afiliate model. An interesting research direction would be to examine the efect of cash back on consumer repurchasing behavior. Recent research has shown that the receipts of cash-back rewards significantly increase both the likelihood and the total amount of subsequent purchasing transactions due to mental accounting (Vana et al. 2015). Although traditional promotional vehicles also provide a similar saving opportunity, none of them can convert it into repurchases in the same channel because coupon users may spend the money they have saved elsewhere. Another interesting line of further inquiry would be to systematically examine the diference between cash back and couponing in terms of the eficiency of segmentation. Couponing utilizes push or outbound advertising in which marketers proactively distribute deals to the general public who may or may not have purchase intent. Since push marketing requires a great deal of reach typically via mass media, it is expensive, and its performance is hard to guarantee and measure (Garth 2012). Cash back, on the contrary, adopts a novel pull or inbound advertising. Instead of sending deals out, the cash-back concept attracts consumers who already have high purchase intent to the afiliate sites with publicly and constantly available discounts (Swan 2010). Since the cash-back sites collect fees based only on revenue they bring in, merchants without a large-sized budget are now able to pursue segmentation in a more cost-eficient and easy-to-measure manner.

## Acknowledgments

The authors thank the senior editor, the associate editor, and the anonymous reviewers for their constructive suggestions throughout the review process. The authors also thank the participants at the 2013 International Conference on Information Systems, 2012 INFORMS Conference on Information Systems Technology, 2012 Workshop on Information Technology and Systems, 2012 Workshop on e-Business, and ISOM research seminar at the University of Washington for their helpful comments and discussions.

## Endnotes

<sup>1</sup> See http://www.ebates.com/help/how\_ebates\_works.htm.

<sup>2</sup> The authors thank Mr. C. Cassata, the president of MrRebates.com, and sales associates at multiple cash-back sites (such as eBates.com, FatWallet.com, BeFrugal.com, CouponCactus.com, Dubli.com, and Shop.com) for sharing valuable industry practices.

<sup>3</sup> This setting is a typical spatial model with the transportation cost normalized to 1. We will relax this assumption in the analysis of a competitive market in Section 4.

<sup>4</sup> Please refer to Online Appendix A.1 for the full details of the solutions and parameter spaces.

<sup>5</sup> By the direct channel, we mean a merchant’s e-commerce site, though the term can be generalized to include the merchant’s physical stores, as merchants have recently begun to allow consumers to earn cashback rewards by shopping at their physical stores as well.

<sup>6</sup> The IC constraint of type h consumers is $0 < \Delta p < c _ { h } . \mathrm { ~ I f ~ } c _ { h }$ is extremely small such that the interior solution does not exist, then the optimal cash-back rate will be a corner solution, $a ^ { * } = c _ { h } / p _ { r }$ , and the problem faced by the merchant would degenerate to a simple problem with a single decision variable p. This scenario fails to produce insightful results and deviates from the main interest of this study. For this reason, we restrict our attentions to the scenario in which the interior solutions exist.

<sup>7</sup> Here we list and discuss the optimal solutions under an uncovered market only. When the market is fully covered, the site’s problem will become linear. In this case, the merchants’ optimal prices will reduce to corner solutions (i.e., profitability of the cash-back model will solely rely on the revenue shares between the two firms). In Section 4, we will revisit the case with full market coverage in a competitive setting.

<sup>8</sup> For brevity, we do not present the paradox region under the leadbased model since all of the associated results are qualitatively the same as those under the commission-based model.

<sup>9</sup> See http://www.mrrebates.com/support/faqs.asp#Payments.

<sup>10</sup> The relative portion of consumers who have strong or weak site preference does not have an efect on the results. To see this, we can rewrite (7) as $Q _ { l , i } ^ { A C } ( p _ { p , i } , p _ { p , - i } ) = ( \theta / 2 ) ( ( \delta v - p _ { p , i } - d / 2 ) + ( ( d -$ $p _ { p , i } + p _ { p , - i } ) / 2 ) )$ , where d represents the relative size of consumers who may switch between sites. Clearly, the terms inside the second parentheses take the same form as the outcome under a classic Hotelling competition.

<sup>11</sup> Our duopoly setting can be generalized to model a marketplace where two retailers sell an identical product by interpreting a consumer’s location as her brand preference or loyalty to the two competing merchants. See Abhishek et al. (2016) and Tan et al. (2016) for examples.

## References

Abhishek V, Jerath K, Zhang ZJ (2016) Agency selling or reselling? Channel structures in electronic retailing. Management Sci. 62(8):2259–2280.

Banks J, Moorthy S (1999) A model of price promotions with consumer search. Internat. J. Indust. Organ. 17(3):371–398.

Bawa K, Shoemaker RW (1987) The efects of a direct mail coupon on brand choice behavior. J. Marketing Res. 24(4):370–376.

Borenstein S (1985) Price discrimination in free-entry markets. RAND J. Econom. 16(3):380–397.

Chen Y, Moorthy S, Zhang ZJ (2005) Research note–Price discrimination after the purchase: Rebates as state-dependent discounts. Management Sci. 51(7):1131–1140.

Corts KS (1998) Third-degree price discrimination in oligopoly: Allout competition and strategic commitment. RAND J. Econom. 29(2):306–323.

Coughlan AT, Soberman DA (2005) Strategic segmentation using outlet malls. Internat. J. Res. Marketing 22(1):61–86.

Dellarocas C (2012) Double marginalization in performance-based advertising: Implications and solutions. Management Sci. 58(6): 1178–1195.

Dhar SK, Raju JS (1998) The efects of cross-ruf coupons on sales and profits. Management Sci. 44(11):1501–1516.

Dukes AJ, Gal-Or E, Srinivasan K (2006) Channel bargaining with retailer asymmetry. J. Marketing Res. 43(1):84–97.

Fudenberg D, Levine DK (1998) The Theory of Learning in Games, Vol. 2 (MIT Press, Cambridge, MA).

Garth G (2012) Pull marketing vs. push marketing: Definition, explanation and benefits. White Shark Media (July 27), http:// blog.whitesharkmedia.com/why-every-small-mid-sized-business -focus-pull-marketing.

Gerstner E, Hess JD (1991) A theory of channel price promotions. Amer. Econom. Rev. 81(4):872–886.

Gerstner E, Hess JD, Holthausen DM (1994) Price discrimination through a distribution channel: Theory and evidence. Amer. Econom. Rev. 84(5):1437–1445.

Hoge P (2011) Shopping site Ebates rings up revenue growth. San Francisco Bus. Times (May 20), http://www.bizjournals.com/ sanfrancisco/print-edition/2011/05/20/shopping-site-ebates -rings-up-revenue.html?page<sup></sup>all.

Holmes TJ (1989) The efects of third-degree price discrimination in oligopoly. Amer. Econom. Rev. 79(1):244–250.

Iyer G (1998) Coordinating channels under price and nonprice competition. Marketing Sci. 17(4):338–355.

Jeuland AP, Narasimhan C (1985) Dealing-temporary price cuts-by seller as buyer discrimination mechanism. J. Bus. 58(3):295–308.

Katz ML (1984) Price discrimination and monopolistic competition. Econometrica 52(6):1453–1471.

Lu Q, Moorthy S (2007) Coupons versus rebates. Marketing Sci. 26(1):67–82.

Mehra A, Kumar S, Raju JS (2017) Competitive strategies for brickand-mortar stores to counter showrooming. Management Sci. Forthcoming.

Narasimhan C (1984) A price discrimination theory of coupons. Marketing Sci. 3(2):128–147.

Nash JF Jr (1950) The bargaining problem. Econometrica 18(2): 155–162.

Neslin SA (1990) A market response model for coupon promotions. Marketing Sci. 9(2):125–145.

Raju JS, Dhar SK, Morrison DG (1994) The efect of package coupons on brand choice. Marketing Sci. 13(2):145–164.

Rand M (2005) Comparison shopping on sale. Forbes (December 14), http://www.forbes.com/2005/12/14/bow05121401.html.

Shafer G, Zhang ZJ (1995) Competitive coupon targeting. Marketing Sci. 14(4):395–416.

Swan M (2010a) Should marketers use cashback sites? Econsultancy (October 22), http://econsultancy.com/us/blog/6724 -overview-of-cashback-sites.

Swan M (2010b) How can retailers use afiliates for customer acquisition? Econsultancy (November 11), http://econsultancy.com/ us/blog/6839-how-can-retailers-use-afiliates-for-customer -acquisition.

Swan M (2011) Afiliate marketing: How promotional methods are changing. Econsultancy (February 2), http://econsultancy.com/ us/blog/7109-afiliate-marketing-how-promotional-methods -have-changed.

Tan X, Ho Y-CC, Tan Y (2016) Money maker or money loser? The dilemma of membership free shipping. Working paper, University of Washington, Seattle.

Vana P, Lambrecht A, Bertini M (2015) Cashback is cash forward: Delaying a discount to increase future spending. Working paper, London Business School, London.

Williams G (2014) How to get the most out of cash-back sites. U.S. News World Rep. (November 4), http://money.usnews.com/ money/personal-finance/articles/2014/11/04/how-to-get-the -most-out-of-cash-back-sites.
