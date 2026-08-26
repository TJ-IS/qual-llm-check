---
otero_id: 28272
otero_key: "WSBKJBBK"
title: "Seller Organization and Percentage Fee Design in the Daily Deal Market"
authors: "Yao Tang; Xu Guan"
year: "2022"
journal: "Information Systems Research"
doi: "10.1287/isre.2021.1070"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Seller Organization and Percentage Fee Design in the Daily Deal Market

Yao Tang,<sup>a</sup> Xu Guan<sup>b,</sup>\*

<sup>a</sup> School of Business Administration, Zhongnan University of Economics and Law, Wuhan 430073, China; <sup>b</sup> School of Management, Huazhong University of Science and Technology, Wuhan 430074, China

Contact: tangyao0512@zuel.edu.cn, https://orcid.org/0000-0002-6739-6279 (YT); guanxu@hust.edu.cn, https://orcid.org/0000-0003-1444-9004 (XG)

Received: Revised: October 30, 2020; June 12, 2021 Accepted: <sup>August 21, 2021</sup>Published Online in Articles in Advance: November 16, 2021

https://doi.org/10.1287/isre.2021.1070

Copyright:

Abstract. Motivated by the prosperity of the daily deal market, this paper investigates the interplay between a platform and sellers, wherein the platform selects a limited number of competing sellers from the seller pool to conduct daily deal campaigns under a certain organization format. We consider two prevalent seller organization formats in practice: one is the seller agglomeration strategy, under which the platform does not distinguish the sellers’ type when selecting them from the seller pool, and the other one is the seller segmentation strategy, under which the platform organizes sellers of the same type to compete in each round of the campaign. We show that different seller organization formats can signi<sup>fi</sup>- cantly in<sup>fl</sup>uence the platform’s and sellers’ pricing strategies, leading to adverse effects on the platform’s and sellers’ pro<sup>fi</sup>tability. In comparison with the agglomeration strategy, the segmentation strategy eliminates internal information asymmetry between the sellers, which enables them to make more adequate pricing decisions and improves sales revenue. This result reversely incentivizes the platform to charge a higher percentage fee and thus obtain a higher pro<sup>fi</sup>t. However, the increase in the percentage fee further decentralizes the vertical relationship between the platform and sellers; as a result, the sellers’ and system’s pro<sup>fi</sup>ts decrease under the segmentation strategy. We also examine alternative game settings based on heterogenous potential demand, consumer retention behavior, platform competition, percentage fee discrimination, and whether the number of competing sellers is endogenous and show that the main results are quite robust.

History: Ravi Bapna, Martin Bichler, Bob Day, and Wolfgang Ketter, Senior Editors; Bill Rand, Associate Editor. This paper has been accepted for the Information Systems Research Special Section on Market Design and Analytics

Funding: Y. Tang received <sup>fi</sup>nancial support from the National Natural Science Foundation of China [Grants 72101271 and 71701212]. X. Guan received <sup>fi</sup>nancial support from the National Natural Science Foundation of China [Grants 71922010, 71821001, and 7191101004].

Supplemental Material: The online appendices are available at https://doi.org/10.1287/isre.2021.1070.

Keywords: daily deal market <sub>•</sub> online platform <sub>•</sub> seller organization <sub>•</sub> percentage fee <sub>•</sub> information asymmetry

## 1. Introduction

As an innovative business practice, the daily deal market has attracted substantial attention from both industry and academia in the last decade. In this mode, an online platform (e.g., a daily deal website) serves as a marketplace to connect consumers by offering discounted deals from different sellers: The platform <sup>fi</sup>rst asks the sellers to submit their deals for speci<sup>fi</sup>c product categories and at discounted prices and then selects a limited number of deals from these submissions to conduct daily deal campaigns. By doing so, consumers can enjoy a variety of goods and services with deep discounts, sellers can increase their awareness and generate additional revenues, and the platform can collect pro<sup>fi</sup>ts from enlisted sellers by charging a percentage fee.

As an industry pioneer founded in 2008, Groupon initially exercised a “one deal-one day” practice to achieve market penetration (Liu and Sutanto 2012). That is, Groupon would select only one deal to pre sent each day and apply a new deal the next day. As such, consumers could observe new deals rapidly. After years of development, Groupon currently hosts thousands of deals for different product categories on its website, varying from food, beauty, and automotive to personalized items. Although the median life span of a deal on the website has been extended to four days, the number of deals being selected is still quite limited compared with the total number of proposed deals submitted to the platform (Cao et al. 2018). According to a report, Groupon has a wait list of more than 35,000 businesses seeking to be featured on the site; however, Groupon can only promote approximately one in every eight interested businesses on its website (Dholakia 2011c).

The change from a one deal-one day approach to a “multiple deals-one day” approach undoubtedly brings new challenges to sellers. First, unlike a single seller involved in the one deal-one day campaign, a seller who participates in the current daily deal campaign inevitably encounters other sellers from the same product category who also offer strong deals. Although more product variety may often attract more consumers, as indicated by Li et al. (2018) and Stephen and Toubia (2010), potential head-head competition may decrease the sales of a deal. Second, given that a group of competing sellers are enrolled in the daily deal campaign, they may be heterogenous in product quality. That is, an enlisted seller may not know what type (the seller’s product quality in our paper) of competitors it may encounter. This subsequently prevents sellers from making adequate pricing decisions, as the sellers are required to price their products when proposing to the platform (Bhardwaj and Sajeesh 2017, Li et al. 2018).

Addressing these challenges requires the platform to organize its sellers more ef<sup>fi</sup>ciently under the daily deal campaign; in practice, we have seen that some platforms indeed strategically organize their sellers under the daily deal campaign, while others do not. For example, Groupon and LivingSocial seem to not impose a strict organization format on their sellers who are intended to participate in the daily deal campaign.<sup>1</sup> On Groupon’s of<sup>fi</sup>cial website, although the platform has classi<sup>fi</sup>ed its deals into various categories and each category is further divided into multiple subcategories, it does not distinguish the seller’s type. Taking wireless mouse in the electronics category as an example, as shown in Figure 1, the prices of deals range from 5.46 to 114.95 USD, implying a signi<sup>fi</sup>cant heterogeneity among the enlisted sellers, that is, a seller of high product quality might charge a high price, whereas a seller of low product quality charges a low price.<sup>2</sup> Similar phenomena can be observed on Living-Social’s website.

In contrast, some other leading daily deal platforms such as JD and Juhuasuan actually organize their sellers into different types and launch corresponding daily deal campaigns. For example, unlike Groupon that posts all selected deals together, JD provides two channels that exercise daily deals on its website: Pin Pai Shan Gou for premium brands and Mei Ri Te Jia for common brands. Every day, JD updates its deals in one or the other channel interchangeably. Again, taking wireless mouse in the electronics category in JD’s Pin Pai Shan Gou and Mei Ri Te Jia as an example, as shown in Figure 2, it is evident that for premium brands, sellers should adopt high standards such that their prices are apparently higher than those of common brands, which are sold by sellers with lower standards.<sup>3</sup> This observation indicates that JD has indeed distinguished its sellers’ type on organizing them to conduct daily deal campaigns.

Motivated by the previous discussion, especially the different seller organization formats adopted by daily deal platforms, in this paper, we seek to gain a better understanding of the interplay between a platform and a group of competing sellers in the daily deal market, wherein sellers are of the same product category (i.e., wireless mouse in electronics) but of differential product quality. Speci<sup>fi</sup>cally, we are interested in the role of the platform. How should the platform organize its sellers in each round of the daily deal campaign? How should the platform design the percentage fee to maximize its pro<sup>fi</sup>tability? How should sellers make their pricing decisions under competition? How do different seller organization formats in<sup>fl</sup>uence <sup>fi</sup>rms’ equilibrium strategies and pro<sup>fi</sup>ts?

To answer these questions, we consider the stylized daily deal market setting in which one platform contracts with multiple sellers to execute daily deal cam paigns. There are two types of sellers based on their product quality: a high-type seller (namely, a seller of high product quality) and a low-type seller (namely, a seller of low product quality). These sellers can be directly mapped to our motivating example of JD: a high-type (low-type) seller is referred to the premium brand (common brand) for Pin Pai Shan Gou (Mei Ri Te Jia). All interested sellers need to submit their deals to the platform with signing a contract that speci<sup>fi</sup>es the offered product, dealing price, and percentage fee (Bhardwaj and Sajeesh 2017, Li et al. 2018), and then the platform selects a limited number of sellers from the seller pool to conduct the daily deal campaign. We speci<sup>fi</sup>cally consider two seller organization formats. The <sup>fi</sup>rst is the seller agglomeration strategy, in which case the platform does not deliberately distinguish the type of sellers when organizing them to conduct daily deal campaigns, that is, the example of Groupon. The second is the seller segmentation strategy, under which the platform organizes sellers of the same type to compete in each round of the campaign, that is, the example of JD.<sup>4</sup> Both seller organization formats are prevalent in practice and the key difference between them lies in the information structure present among the competing sellers: Under the segmentation strategy, a seller should expect to be confronted by the same type of seller in the daily deal campaign, whereas under the agglomeration strategy, a seller is uncertain about its competitor’s type.

Figure 1. Prices of Wireless Mouse Deals on Groupon on March 27, 2021  
![](/api/attachments/WSBKJBBK/fulltext/images/b32fa209986e4397b8e7efa8ede27213fcbe79f4fca4449d0fd464a906ab924c.jpg)

Figure 2. (Color online) Prices of Wireless Mouse Deals on Pin Pai Shan Gou and Mei Ri Te Jia of JD  
![](/api/attachments/WSBKJBBK/fulltext/images/48b6c5f6ebe42908890c9c6e6c134d53f7b85e6bc58464da23715559e44f0a3f.jpg)

We show that different seller organization formats have prominent effects on platform’s percentage fees and sellers’ pricing strategies, as well as on their pro<sup>fi</sup>tability. Intuitively, unlike the agglomeration strategy, the segmentation strategy can eliminate information asymmetry between competing sellers and thus can enable them to provide more adequate prices in daily deal campaigns. This result could indicate the bene<sup>fi</sup>ts of the segmentation strategy, as it increases the sales revenue of daily deal campaigns. Nonetheless, in anticipating that sellers will become more adequate at making pricing decisions, the platform charges a higher percentage fee to extract more surplus from the sellers. In contrast, under the agglomeration strategy, because of information asymmetry, sellers make inadequate pricing decisions and thus obtain lower revenues from daily deal campaigns, which causes the platform to charge a lower percentage fee to partially compensate for the sellers’ losses in the market.

Combining these con<sup>fl</sup>icting effects, under the segmentation strategy, the negative effect of the increase in the percentage fee dominates the positive effect of pricing ef<sup>fi</sup>ciency such that the sellers’ pro<sup>fi</sup>t is lower than that under the agglomeration strategy. In contrast, the platform’s pro<sup>fi</sup>t increases under the segmentation strategy, as it can extract additional surplus from the sellers’ side by setting a more aggressive percentage fee. Given that a higher percentage fee would decentralize the platform and sellers, the entire system’s pro<sup>fi</sup>t is hindered by the segmentation strategy. Moreover, we show that the value of seller organization hinges largely on the composition of sellers in the daily deal market. When the ratio between high- and low-type sellers is closer to the midpoint, the surplus of the segmentation strategy over the agglomeration strategy on the platform becomes more prominent. Otherwise, the gap between these two seller organization formats diminishes when the ratio is suf<sup>fi</sup>ciently high or low.

We further extend the basic model to several alternative settings to verify the robustness of our main results. We <sup>fi</sup>nd that when the gap in product quality between two types of sellers increases or the platform can organize more sellers to conduct daily deal campaigns, it is more bene<sup>fi</sup>cial for the platform to adopt the segmentation strategy. In contrast, when a competitive platform enters the market or the platform can set differential percentage fees for sellers of different types, the bene<sup>fi</sup>t of the segmentation strategy would diminish. With an entrant platform, the incumbent platform cannot fully eliminate information asymmetry among the competing sellers by segmentation, which further reduces the bene<sup>fi</sup>t of this seller organization format. Consequently, the incumbent platform’s pro<sup>fi</sup>t and the gap between the two seller organization formats are inevitably reduced. With pricing <sup>fl</sup>exibility, the platform can set differential percentage fees for the sellers under the agglomeration strategy but the same percentage fee under the segmentation strategy, as the sellers are of the same type. Thus, the effect of percentage fee discrimination is more signi<sup>fi</sup>cant under the agglomeration strategy, and this result narrows the gap between the two seller organization formats.

The remainder of this paper proceeds as follows. In Section 2, we review the related literature. In Section $^ { 3 , }$ we describe the model setup. Section 4 presents an analysis of equilibrium percentage fee design and sellers’ pricing strategies under either seller organization format. Section 5 discusses some extensions, and Section 6 provides conclusions from this paper.

## 2. Literature Review

Our paper belongs to the emerging literature that researches the daily deal market. One particular focus of this stream concerns how this novel business mode in-<sup>fl</sup>uences consumers’ purchasing decisions because of different behavioral factors, such as social interaction (Jing and Xie 2011, Hu et al. 2013, Subramanian and Rao 2016), voucher redemption (Luo et al. 2014, Song et al. 2016), herding and word of mouth (Li and Wu 2018), and searching and learning (Hu et al. 2019). Another focus is to examine the marketing strategies and pro<sup>fi</sup>tability of sellers who are engaged in daily deal campaigns. In particular, Byers et al. (2011), Dholakia (2011c), Kumar and Rajan (2012), Edelman et al. (2016), and Reiner and Skiera (2019) investigate sellers’ performance in daily deal campaigns by highlighting various determinant forces, such as the platform’s percentage fees, number of attracted consumers, depth of deal discounts, retention rates of new consumers, and so on. More recent papers are empirical studies that validate marketing strategies under seller competition in the daily deal market (Bai et al. 2017, Kitchens et al. 2018, Li et al. 2018). For example, Kitchens et al. (2018) explore how the introduction of daily deal campaigns can in<sup>fl</sup>uence the marketing strategies of competing sellers in a particular geographic cluster.

Unlike the previous works that focus on the downstream market (between consumers and sellers), this paper sheds light on the interactions between a platform and multiple sellers. Speci<sup>fi</sup>cally, we are interested in the role of the platform, wherein it can not only strategically organize its potential sellers to conduct daily deal campaigns but also design an optimal percentage fee to maximize its own pro<sup>fi</sup>t. Especially for different seller organization formats (i.e., segmentation and agglomeration), although they are prevalent in practice, their impacts have never been adequately investigated.

Some papers study the platform’s design of percentage fee adopted in the platform-based markets. For example, Zhao et al. (2016) examine how the platform’s percentage fee can help signal product quality in the daily deal market. Bhardwaj and Sajeesh (2017) investigate the optimal percentage fee applied under a bargaining game between the platform and sellers in the daily deal market. Muthers and Wismer (2013) show that by setting a percentage fee, the platform can mitigate the holdup problem whereby sellers fear the platform’s entry into their respective markets. However, none of these works consider horizontal competition among sellers, which is an important feature of the modern daily deal market (Bai et al. 2017, Kitchens et al. 2018, Li et al. 2018). For a competitive environment, some scholars have examined the effects of sellers’ heterogeneity (Dholakia 2011a, Edelman et al. 2016, Reiner and Skiera 2019) and have shown that it signi<sup>fi</sup>cantly in<sup>fl</sup>uences the platform’s design of percentage fee (Wang and Wright 2017, 2018). In another related paper, Jiang and Zou (2020) study the platform’s percentage fee and the pricing game among competing sellers. Their primary focus is on how con sumer searching behavior could affect the pricing strate gies of the platform and sellers.

In our paper, we also explore horizontal competition between sellers and simultaneous vertical interactions between the platform and sellers, although our work presents the following major differences. Notably, we distinguish between two seller organization formats available for the platform to exercise daily deal cam paigns, that is, the agglomeration strategy and the segmentation strategy. Based on this point, we assume that a group of heterogeneous sellers are engaged in Bertrand competition when participating in daily deal campaigns. Although seller competition and seller heterogeneity have been studied before, the platform can reshape the competing nature of sellers by utilizing its seller organization formats. Particularly, we show that when sellers have differential quality levels, different seller organization formats can change the information structure present among the competing sellers, which further leverages the equilibrium pricing decisions of the platform and sellers.

## 3. Model Setup

## 3.1. Daily Deal Market

We consider the daily deal market wherein a platform contracts with multiple competing sellers of the same product category (i.e., wireless mouse in electronics) to exercise daily deal campaigns. The platform <sup>fi</sup>rst announces its seller organization format and accordingly the charged percentage fee based on the dealing price that is determined by the seller. Then, the sellers are required to submit their deals with prices to the platform, and the platform selects a limited number of sellers to conduct the daily deal campaign according to its seller organization format (Dholakia 2011c). Moreover, one can view the daily deal campaign as a promotion repeatedly executed between the platform and sellers (Dholakia 2011b, Pentina and Taylor 2013, Song et al. 2016). Thus, the number of quali<sup>fi</sup>ed sellers in the seller pool is constant such that the daily deal campaign can be cycled in a stable manner over time. This assumption can be understood as follows: In each round, the sellers, irrespective of being organized or not, remain in the seller pool and become candidates for the next round of the campaign. In the basic model, we speci<sup>fi</sup>cally assume that the platform organizes two sellers to conduct daily deal campaigns in each round. This assumption allows us to derive suf<sup>fi</sup>- cient managerial insights from comparing different seller organization formats. In Section 5.1, we relax this constraint to show that the results remain robust when more sellers can be selected or when the number of sellers can be endogenously determined by the platform.

## 3.2. Seller Heterogeneity

There are two types of sellers in the pool that are heterogenous in their product quality, as implied by our motivating examples. In the basic model, we characterize this quality differentiation by assuming that a seller offering higher product quality applies a higher production cost. This assumption is not uncommon in the literature (Shivendu and Zhang 2013), as providing higher product quality usually requires the seller to invest more in the production process, thus leading to a higher production cost. Moreover, the production cost has been viewed as a key factor determining a <sup>fi</sup>rm’s selling strategy in the daily deal market (Dholakia 2011a, 2012; Zhang and Chung 2020), which highlights our intention to focus on strategic interactions between a platform and competing sellers. In particular, we denote the high production cost as $c _ { h }$ and the proportion of sellers with high costs as $\lambda ,$ and we denote the low production cost as $c _ { l }$ and the proportion of sellers with low costs as $1 - \lambda . \operatorname { L e t } 0 < c _ { l } < c _ { h }$ and $0 < \lambda < 1$ . Such cost and proportion information are publicly observable to all <sup>fi</sup>rms in the market. In Section 4.4, we conduct a more general discussion of the effect of quality differentiation by assuming that a seller offering higher product quality applies not only a higher production cost but also higher potential demand. We demonstrate that the main results are not materially changed.

## 3.3. Seller Organization Format

Regarding the platform, we assume that it is informed of the types of all proposed sellers, which enables it to make the appropriate arrangement under each seller organization format. This is reasonable for our game settings, as the platform can observe the sellers’ submitted deals and thus rationally infer their types.<sup>5</sup> We then elaborate on how the platform selects and arranges its sellers to conduct daily deal campaigns under two seller organization formats. For either format, the platform <sup>fi</sup>rst sets a speci<sup>fi</sup>c date on which interested sellers can submit their deals.

Under the seller agglomeration strategy, as the platform does not distinguish sellers, it chooses sellers in the seller pool with an equal likelihood of applying the daily deal campaign. This arrangement subsequently leads to three possible compositions of competing sellers in each round of the campaign: Two high-type sellers, two low-type sellers, and one hightype seller and one low-type seller. One can infer that under such conditions, if a seller is selected, it cannot know its competitor’s type and only has a prior belief that the competitor may be a high-type competitor with probability λ or a low-type competitor with probability 1 λ.

In contrast, under the seller segmentation strategy, the platform deliberately arranges sellers with the same type to conduct the campaign in each round. This situation implies that if a seller is selected under the segmentation strategy, it can always con<sup>fi</sup>rm that its competitor should have the same type. As a result, there are only two possible compositions of compet ing sellers in the campaign: Two high-type sellers with probability λ and two low-type sellers with probability 1 λ. Although in one round of the campaign the platform cooperates with one type of sellers under the segmentation strategy, we assume that in a long-term perspective the platform cannot choose only one certain type of sellers to conduct daily deals. This condition is <sup>fi</sup>rst applied to ensure fairness. For example, Juhuasuan is a daily deal platform owned by Tmall, and thus it should be open to all registered sellers of Tmall regardless of their types. Besides, in practice, a platform may encounter competition from other daily deal platforms. Then, reducing the seller type would drive some consumers away and cause them to transfer to other platforms, and this may not be wise for a platform in competitive environments.<sup>6</sup> As a result, it is rare for a platform to only accept one type of sellers to conduct daily deals in practice.

It is evident that the key difference between two seller organization formats lies in the information structure between the competing sellers, that is, whether a seller can con<sup>fi</sup>rm its competitor’s type. We show below that such a change in the information structure can have a signi<sup>fi</sup>cant impact on the sellers’ equilibrium pricing decisions, as they are required to determine dealing prices before being selected.

## 3.4. Demand and Decision Timing

Based on the previous discussion, we provide the selected seller’s demand for each round of the campaign in (1), which has been widely used in the literature on online markets with seller competition (Abhishek et al. 2016, Tian et al. 2018):

$$
d _ {t} = b - p _ {t} + \theta (p _ {3 - t} - p _ {t}), 0 <   \theta <   1, t = 1, 2.\tag{1}
$$

In (1), d denotes the realized demand of a selected seller t, b denotes the seller’s potential demand, $p _ { t }$ is the dealing price set by seller t, and θ measures the intensity of price competition, where a higher θ indicates a greater degree of product substitution between two sellers. In Section 4.4, we consider the situation that the potential demand for a high-quality (highcost) product is larger than that for a low-quality (low-cost) product. Also note that in Section 4.5, we consider the long-term promotional effect of daily deal campaigns by incorporating consumer retention into the current model.

The sequence of events is illustrated in Figure 3 and proceeds as follows. First, the platform announces its seller organization format so that the sellers can con-<sup>fi</sup>rm which kind of daily deal campaign they are participating in. Second, the platform designs the percentage fee to maximize its pro<sup>fi</sup>t collected from competing sellers. We require the percentage fee to be uniform for all sellers and to not change with respect to the seller’s type (Shivendu and Zhang 2013) because percentage fee discrimination may lead to serious fairness concerns among competing sellers. Moreover, as shown in Section 5.3, percentage fee discrimination does not materially change our main conclusions. Third, given the seller organization format (agglomeration or segmentation) and the corresponding percentage fee, the sellers set their dealing prices for products when submitting them to the platform. Finally, the platform selects sellers to execute daily deal campaigns according to its seller organization format, and all involved entities collect their pro<sup>fi</sup>ts based on the speci<sup>fi</sup>ed contract terms.

Consistent with the literature (Hao and Fan 2014, Abhishek et al. 2016), we normalize the <sup>fi</sup>xed service fee charged by the platform to the sellers to zero, because it does not have any strategic effect on our equilibrium results. The platform and sellers are risk neutral to maximize their pro<sup>fi</sup>ts. Because the game involves multiple rounds of strategic interaction, backward induction is applied to ensure subgame perfection.

## 4. Analysis

In this section, we <sup>fi</sup>rst derive the equilibrium results under two seller organization formats. We then compare the outcomes to identify the optimal seller organization format from either the platform’s or the seller’s perspective. After that, we incorporate two effects to consolidate the basic model, that is, the effect of quali ty differentiation on the seller’s potential demand and the effect of consumer retention on the seller’s longterm demand. For ease of exposition, we use a to denote the results obtained under the agglomeration strategy and s to denote the results obtained under the segmentation strategy. We use h to denote the hightype seller and l to denote the low-type seller.

## 4.1. Agglomeration Strategy

We begin with the scenario of the seller agglomeration strategy, under which the platform does not distinguish the sellers’ type when selecting them from the pool. Therefore, a seller cannot con<sup>fi</sup>rm which type of seller it will encounter once it has been selected by the platform to conduct the daily deal campaign. Thus, a seller determines the dealing price based on its expectation. Given the composition of sellers in the pool, it is evident that the probability of a high-type seller being organized is λ and that the probability of a low-type seller being organized is 1 λ: Therefore, for a seller being selected, given its own type $i , \ i = h$ or l, its pro<sup>fi</sup>t from the campaign is given by

$$
\pi_ {i} ^ {a} (p _ {i} ^ {a}) = ((1 - \gamma_ {a}) p _ {i} ^ {a} - c _ {i}) d _ {i} ^ {a}, i = h \mathrm{or} l,\tag{2}
$$

where $\gamma _ { a }$ denotes the percentage fee, $p _ { i } ^ { a }$ denotes the dealing price, and $d _ { i } ^ { a }$ denotes the realized demand for seller i organized under the agglomeration strategy. Speci<sup>fi</sup>cally, depending on the seller’s type, we formulate its realized demand as

$$
\begin{array}{l} d _ {i} ^ {a} = \lambda (b - p _ {i} ^ {a} + \theta (p _ {h} ^ {a *} - p _ {i} ^ {a}) + (1 - \lambda) (b - p _ {i} ^ {a} + \theta (p _ {l} ^ {a *} - p _ {i} ^ {a})) \\ i = h \text {   or   } l, \end{array} \tag {3}
$$

Figure 3. Timing of Events  
Daily deal campaigns  
![](/api/attachments/WSBKJBBK/fulltext/images/e987eba4081259080bb0ffd9f300c6d9f6c7c86d2c878c9493410f2b28459ea3.jpg)

where $p _ { h } ^ { a * }$ and $p _ { l } ^ { a * }$ are the competitor’s optimal dealing prices conditional on its type. We solve the pricing game between the two organized sellers with the following lemma.

Lemma 1. Under the agglomeration strategy with percent-$a g e f e e \gamma _ { a } ,$ the following results apply.

1. The optimal dealing price and realized demand are $\begin{array} { r } { p _ { h } ^ { a * } = \frac { b } { 2 + \theta } + \frac { c _ { h } } { 1 - \gamma _ { a } } \frac { 1 + \theta } { 2 + \theta } - ( 1 - \lambda ) \frac { c _ { h } - c _ { l } } { 1 - \gamma _ { a } } \frac { \theta } { 2 ( 2 + \theta ) } } \end{array}$ and $d _ { h } ^ { a * } = \left( 1 + \theta \right)$ $\begin{array} { r } { \Big ( p _ { h } ^ { a * } - \frac { c _ { h } } { 1 - \gamma _ { a } } \Big ) . } \end{array}$ for the organized high-type seller, respectively.

2. The optimal dealing price and realized demand are $p _ { l } ^ { a * } =$ $\begin{array} { r } { \frac { b } { 2 + \theta } + \frac { c _ { l } } { 1 - \gamma _ { a } } \frac { 1 + \theta } { 2 + \theta } + \lambda \frac { c _ { h } - c _ { l } } { 1 - \gamma _ { a } } \frac { \theta } { 2 \left( 2 + \theta \right) } } \end{array}$ and $\begin{array} { r } { d _ { l } ^ { a * } = ( 1 + \theta ) \Big ( p _ { l } ^ { a * } - \frac { c _ { l } } { 1 - \gamma _ { a } } \Big ) f o r } \end{array}$ the organized low-type seller, respectively.

In Lemma 1, we derive the organized sellers’ optimal dealing prices and realized demand in each round of the campaign under the agglomeration strategy. First, it shows that each seller’s dealing price increases with the percentage fee $\gamma _ { a }$ charged by the platform, as the seller must increase its dealing price to cover its selling cost from the platform. Accordingly, the realized demand for each seller type decreases with the increasing percentage fee. Second, if the proportion of high-type sellers increases, both types of organized sellers charge higher dealing prices. To elaborate, when λ increases, an organized seller infers that its competitor is more likely to be a high-type seller and thus intends to set a higher dealing price because of the decrease in competition intensity resulting from the potential competitor’s higher production costs. In contrast, if λ decreases, an organized seller is more likely to encounter a low-type competitor, and intensi<sup>fi</sup>ed competition induces the seller to charge a lower dealing price. In this manner, the realized demand for both types of organized sellers increases with λ because of a higher probability of competing with a high-type seller.

We then derive the expected demand for each type of seller in the daily deal market, which is the multiplication of the probability of being organized and the realized demand in each round of the campaign. That is, the expected demand for high- and low-type sellers is given by $2 \lambda d _ { h } ^ { a * }$ and $2 ( 1 - \lambda ) d _ { l } ^ { a * }$ , respectively. The <sup>fi</sup>rst equation shows that the expected demand for the high-type seller monotonically increases with its proportion λ because a higher λ not only increases the seller’s realized demand but also the probability of being organized in each round of the campaign. In contrast, the increase in λ has two con<sup>fl</sup>icting effects on the expected demand for the low-type seller wherein a low-type seller can obtain higher realized demand, but its probability of being organized decreases in each round of the campaign. Combining these results shows that the low-type seller’s expected demand decreases with an increasing λ:

Building on the sellers’ pricing decisions in the daily deal market, we identify the platform’s optimal percentage fee design under the seller agglomeration strategy. The platform seeks to maximize its pro<sup>fi</sup>t wherein

$$
\begin{array}{l} \underset {\gamma_ {a}} {M a x} \pi_ {p} ^ {a} (\gamma_ {a}) = \gamma_ {a} (2 \lambda p _ {h} ^ {a *} d _ {h} ^ {a *} + 2 (1 - \lambda) p _ {l} ^ {a *} d _ {l} ^ {a *}). \\ \text {s.t.} \left\{ \begin{array}{l} \pi_ {h} ^ {a} (p _ {h} ^ {a *}) \geq 0 \\ \pi_ {l} ^ {a} (p _ {l} ^ {a *}) \geq 0 \end{array} . \right. \end{array}\tag{4}
$$

In (4), the platform’s pro<sup>fi</sup>t is represented by the multiplication of its percentage fee and the sellers’ total sales revenue, that is, $2 \lambda p _ { h } ^ { a * } d _ { h } ^ { a * }$ for the high-type seller and $2 ( 1 - \lambda ) p _ { l } ^ { a * } d _ { l } ^ { a * }$ for the low-type seller. Constraints $\pi _ { h } ^ { a } ( p _ { h } ^ { a * } ) \ge 0$ and $\overline { { { \pi } } } _ { l } ^ { a } ( p _ { l } ^ { a * } ) \geq 0$ ensure that both types of sellers are the least incentivized to participate in the daily deal campaign, which sets the upper bound of the percentage fee. We solve this problem with the following proposition.

Proposition 1. Under the agglomeration strategy, the platform’s profit is quasiconcave in $\gamma _ { a }$ . Optimal percentage fee $\gamma _ { a } ^ { \ast }$ meets condition $f _ { a } ( \gamma _ { a } ^ { * } ) = 0 ,$ , wherein $f _ { a } ( \gamma _ { a } ^ { * } ) =$ $b ^ { 2 } \bigl ( 1 - \gamma _ { a } ^ { * } \bigr ) ^ { 3 } + b ( \lambda c _ { h } + ( 1 - \lambda ) c _ { l } ) \theta \bigl ( 1 - \gamma _ { a } ^ { * } \bigr ) - \bigl ( \lambda c _ { h } ^ { 2 } + ( 1 - \lambda ) c _ { l } ^ { 2 } \bigr )$ $\begin{array} { r } { ( 1 + \theta ) \big ( 1 + \gamma _ { a } ^ { * } \big ) - \lambda ( 1 - \lambda ) \frac { ( c _ { h } - c _ { l } ) ^ { 2 } \theta ^ { 2 } } { 4 } \big ( 1 + \gamma _ { a } ^ { * } \big ) . } \end{array}$

Proposition 1 characterizes the platform’s optimal percentage fee under the seller agglomeration strategy. The explanation is straightforward, that is, a higher percentage fee allows the platform to extract more surplus from the competing sellers in each round of the campaign. However, this arrangement also inhibits the seller’s pricing ability, as the sellers must charge higher dealing prices to compensate for their selling cost. This result subsequently reduces the realized demand and thus revenues of the daily deal cam paign. The tradeoff between these two con<sup>fl</sup>icting effects determines the platform’s optimal percentage fee. It can also be veri<sup>fi</sup>ed that optimal percentage fee $\gamma _ { a } ^ { * }$ monotonically decreases with the increasing proportion of high-type sellers and production cost of each seller type. When either of these factors increases, it inevitably reduces the seller’s potential revenue from the daily deal campaign and thus the optimal percentage fee of the platform.

## 4.2. Segmentation Strategy

We now consider the seller segmentation strategy, under which the platform organizes sellers of the same type to conduct daily deals in each round. In this case, a seller can perfectly infer that its competitor will be of the same type. This arrangement allows the seller to determine its dealing price without information asymmetry. We then provide an organized seller’s pro<sup>fi</sup>t in each round of the campaign under the segmentation strategy as follows:

$$
\pi_ {i} ^ {s} (p _ {i} ^ {s}) = ((1 - \gamma_ {s}) p _ {i} ^ {s} - c _ {i}) d _ {i} ^ {s}, i = h \mathrm{or} l,\tag{5}
$$

where $\gamma _ { s }$ denotes the percentage fee, $p _ { i } ^ { s }$ denotes the dealing price, and $d _ { i } ^ { s }$ denotes the realized demand for seller i organized under the segmentation strategy. Speci<sup>fi</sup>cally, depending on the seller’s type, we formulate its realized demand as

$$
d _ {i} ^ {s} = b - p _ {i} ^ {s} + \theta (p _ {i} ^ {s *} - p _ {i} ^ {s}), i = h \mathrm{or} l,\tag{6}
$$

where $p _ { i } ^ { s * }$ is the competitor’s optimal dealing price conditional on its type. We solve the pricing game between the two organized sellers with the following lemma.

Lemma 2. Under the segmentation strategy with percentage fee $\gamma _ { s } ,$ the following results apply.

1. The optimal dealing price and realized demand are $p _ { h } ^ { s * } =$ $\begin{array} { r } { \frac { b } { 2 + \theta } + \frac { c _ { h } } { 1 - \gamma _ { s } } \frac { 1 + \theta } { 2 + \theta } } \end{array}$ and $\begin{array} { r } { d _ { h } ^ { s * } = ( 1 + \theta ) \Big ( p _ { h } ^ { s * } - \frac { c _ { h } } { 1 - \gamma _ { s } } \Big ) } \end{array}$ for the organized high-type seller, respectively.

2. The optimal dealing price and realized demand are $p _ { l } ^ { s * } =$ $\begin{array} { r } { \frac { b } { 2 + \theta } + \frac { c _ { l } } { 1 - \gamma _ { s } } \frac { 1 + \theta } { 2 + \theta } } \end{array}$ and $\begin{array} { r } { d _ { l } ^ { s * } = ( 1 + \theta ) \Big ( p _ { l } ^ { s * } - \frac { c _ { l } } { 1 - \gamma _ { s } } \Big ) } \end{array}$ for the organized low-type seller, respectively.

In Lemma $^ { 2 , }$ we identify the organized sellers’ optimal dealing prices and realized demand in each round of the campaign under the segmentation strategy. As found for the agglomeration strategy, the seller’s optimal dealing price increases but realized demand decreases with the increasing percentage fee charged by the platform because a higher percentage fee requires the seller to set a higher dealing price to compensate for its selling cost and thus reduces realized demand. Nonetheless, given the platform’s strategic organization under the segmentation strategy, the composition of sellers in the pool no longer in<sup>fl</sup>uences an organized seller’s pro<sup>fi</sup>t in each round of the campaign, as the organized seller can con<sup>fi</sup>rm that its competitor is of the same type. We can also obtain the expected demand for each seller type under the segmentation strategy, that is, $2 \lambda d _ { h } ^ { s * }$ for the high-type seller and $2 ( 1 - \lambda ) d _ { I } ^ { s * }$ for the low-type seller. It is evident that the expected demand for the high-type (low-type) seller increases (decreases) with $\lambda ,$ , given that its likelihood of being organized increases (decreases).

We then move to derive the platform’s optimal percentage fee under the segmentation strategy. Similar to that of the agglomeration strategy, the platform’s optimization problem under this scenario is given as follows:

$$
\begin{array}{r l} \underset {\gamma_ {s}} {M a x} & \pi_ {p} ^ {s} (\gamma_ {s}) = \gamma_ {s} (2 \lambda p _ {h} ^ {s *} d _ {h} ^ {s *} + 2 (1 - \lambda) p _ {l} ^ {s *} d _ {l} ^ {s *}). \\ & \text {s.t.} \left\{ \begin{array}{l} \pi_ {h} ^ {s} (p _ {h} ^ {s *}) \geq 0 \\ \pi_ {l} ^ {s} (p _ {l} ^ {s *}) \geq 0 \end{array} \right.. \end{array}\tag{7}
$$

Constraints $\pi _ { h } ^ { s } ( p _ { h } ^ { s * } ) \geq 0$ and $\pi _ { l } ^ { s } ( p _ { l } ^ { s * } ) \geq 0$ still ensure that both types of sellers are the least incentivized to participate under the segmentation strategy. We solve this problem with the following proposition.

Proposition 2. Under the segmentation strategy, the platform’s profit is quasiconcave in $\gamma _ { s }$ . Optimal percentage fee $\gamma _ { s } ^ { * }$ meets condition $f _ { s } \left( \gamma _ { s } ^ { * } \right) = 0$ wherein $f _ { s } ( \gamma _ { s } ^ { * } ) =$ $b ^ { 2 } \bigl ( 1 - \gamma _ { s } ^ { * } \bigr ) ^ { 3 } + b \bigl ( \lambda c _ { h } + ( 1 - \lambda ) c _ { l } \bigr ) \theta \bigl ( 1 - \gamma _ { s } ^ { * } \bigr ) - \bigl ( \lambda c _ { h } ^ { 2 } + ( 1 - \lambda ) c _ { l } ^ { 2 } \bigr )$ $\left( 1 + \theta \right) \left( 1 + \gamma _ { s } ^ { * } \right)$

As described in Proposition 1, the effect of the percentage fee on the platform’s pro<sup>fi</sup>t is qualitatively similar to that under the agglomeration strategy, fo which the platform’s pro<sup>fi</sup>t exhibits an inverse U-shaped relationship with the percentage fee. Thus, under the segmentation strategy, the optimal percentage fee is still driven by two con<sup>fl</sup>icting effects whereby a higher percentage fee increases the platform’s pro<sup>fi</sup>t margin but reduces realized demand (and thus total revenues) in each round of the campaign.

Building on the equilibrium outcomes, we then examine how different seller organization formats could in<sup>fl</sup>uence the platform’s and sellers’ equilibrium pricing strategies; the results are illustrated in the following corollary.

Corollary 1. In equilibrium, after comparing percentage fees, dealing prices, and realized demand under the two seller organization formats, we have the following results.

1. Regarding percentage fees, $\gamma _ { s } ^ { * } > \gamma _ { a } ^ { * }$

2. Regarding dealing prices and realized demand for the high-type seller, $p _ { h } ^ { s * } ( \gamma _ { s } ^ { * } ) > p _ { h } ^ { a * } ( \gamma _ { a } ^ { * } )$ and $d _ { h } ^ { s * } ( \gamma _ { s } ^ { * } ) > d _ { h } ^ { a * } ( \gamma _ { a } ^ { * } )$

3. Regarding dealing prices and realized demand for the low-type seller, $p _ { l } ^ { s * } ( \gamma _ { s } ^ { * } ) < p _ { l } ^ { a * } ( \gamma _ { a } ^ { * } )$ and $d _ { l } ^ { s * } ( \gamma _ { s } ^ { * } ) < d _ { h } ^ { a * } ( \gamma _ { a } ^ { * } )$

First, for the platform, it is interesting to <sup>fi</sup>nd that the optimal percentage fee is higher under the segmen tation strategy than under the agglomeration strategy. For any identical percentage fee, that is, $\gamma _ { a } = \gamma _ { s } = \gamma ,$ it can be veri<sup>fi</sup>ed that the sales revenue is higher under the segmentation strategy than under the ag glomeration strategy, that is, $2 \bar { \lambda } p _ { h } ^ { s * } d _ { h } ^ { s * } + 2 ( 1 - \lambda ) p _ { l } ^ { s * } d _ { l } ^ { s * } >$ $2 \lambda p _ { h } ^ { a * } d _ { h } ^ { a * } + 2 ( 1 - \lambda ) p _ { l } ^ { a * } d _ { l } ^ { a * }$ . This occurs because the seg mentation strategy eliminates information asymmetry between the two competing sellers such that the sellers can make more adequate pricing decisions to improve sales revenue. Because in equilibrium, the sellers can have higher sales revenue, the platform is reversely incentivized to charge a higher percentage fee to extract more surplus from the sellers.

Second, the high-type seller charges a higher dealing price and achieve more realized demand from the segmentation strategy. In this sense, the segmentation strategy alleviates the market competition of the hightype seller, because it no longer competes with the lowtype seller in the daily deal campaign. In contrast, relative to the agglomeration strategy, the segmentation strategy intensi<sup>fi</sup>es market competition for the lowtype seller by enrolling the same seller type with a low production cost. Consequently, the low-type seller must charge a lower dealing price, but its realized demand is still reduced by intensi<sup>fi</sup>ed competition.

## 4.3. Payoff Implications

In this section, we compare pro<sup>fi</sup>ts made under the two scenarios to identify the optimal seller organization format from the perspectives of the platform, seller, and system.

Proposition 3. In equilibrium, after comparing the profits of the involved entities under the two seller organizing formats, we have the following results.

1. The platform obtains a higher profit under the seller segmentation strategy than under the agglomeration strategy.

2. The seller’s profit is higher under the agglomeration strategy.

3. The system obtains a higher profit under the agglomeration strategy than under the segmentation strategy.

Proposition 3 identi<sup>fi</sup>es the adverse effects of the seller agglomeration and segmentation strategies on the pro<sup>fi</sup>tability of different entities. First, for the platform, it is always more bene<sup>fi</sup>cial to deliberately organize sellers of the same type to conduct the daily deal campaign rather than arbitrarily arranging two sellers from the seller pool. The key difference between these two seller organization formats is that by segmentation, the organized seller can always make adequate selling decisions without information asymmetry. This ability is bene<sup>fi</sup>cial to the sellers but is utilized by the platform. As shown by Corollary 1, in anticipation that the sales revenue will outperform under the segmentation strategy, the platform would charge a higher percentage fee to the sellers and thus extract more surplus from the market. Otherwise, under the agglomeration strategy, the sales revenue from the daily deal campaign is restricted by the sellers’ inadequate selling decisions because of information asymmetry. This restriction prevents the platform from charging a higher percentage fee and reduces its pro<sup>fi</sup>tability.

In contrast, although sellers with different types may react adversely to the segmentation strategy, in general, the seller’s pro<sup>fi</sup>t (the sum of the pro<sup>fi</sup>ts for two types of sellers) is undermined by the segmentation strategy. This is the case because segmentation incentivizes the platform to charge a more aggressive percentage fee, whose negative effect dominates the bene<sup>fi</sup>t from making adequate selling decisions in the market. Similarly, it can be veri<sup>fi</sup>ed that the entire system (the sum of the platform’s and seller’s pro<sup>fi</sup>ts) performs better under the agglomeration strategy than under the segmentation strategy. This is the case because although information asymmetry reduces sellers’ decision ef<sup>fi</sup>ciency in the market, it can also alleviate vertical decentralization between the platform and sellers, which is more valuable to the system. Equivalently, the segmentation strategy ampli<sup>fi</sup>es double marginalization between the platform and sellers, which undermines the system’s pro<sup>fi</sup>t.

Basing on Proposition 3, we further examine the value of seller organization by comparing the platform’s pro<sup>fi</sup>t under the agglomeration strategy and that under the segmentation strategy with respect to the composition of the seller pool, which is captured by the proportion of high-type sellers (λ). Figure 4 provides a graphical illustration.

Figure 4 explicitly shows that the pro<sup>fi</sup>t gap for the platform between the two seller organization formats exhibits an inverse U-shaped relationship with λ: Intuitively, one can refer to λ as the index of the sellers heterogeneity, where the magnitude of this heteroge neity remains low when λ is low or high, while it becomes high when λ falls within an intermediate range. When sellers’ heterogeneity is high, compared with the agglomeration strategy, the segmentation strategy is quite effective at eliminating such heterogeneity by arranging the same seller type in each round of the campaign. Therefore, the pro<sup>fi</sup>t gap expands. Otherwise, if sellers’ heterogeneity is low, the segmentation strategy does not generate much value, so the pro<sup>fi</sup>t gap narrows. When there is no seller heterogeneity (e.g., λ 0 or λ 1), there is no difference between the effects of the two seller organization formats on the platform. A similar principle applies to the sellers side, in which the pro<sup>fi</sup>t gap between the agglomeration strategy and segmentation strategy <sup>fi</sup>rst increases and then decreases with increasing heterogeneity among sellers. When sellers’ heterogeneity is high, the segmentation strategy is effective, and thus the platform charges a high percentage fee from the sellers. This result undermines the sellers’ pro<sup>fi</sup>ts and thus widens the pro<sup>fi</sup>t gap.

Figure 4. (Color online) Impact of Seller Composition on the Pro<sup>fi</sup>t Gap (b 3, c 1, c 0:5, θ 0:5)  
![](/api/attachments/WSBKJBBK/fulltext/images/cbfcc148cba2d8c8eac50a6475890fef3e07ab3708c223a1b029e10fe1e8334c.jpg)

The previous discussion reveals the value of seller organization in the daily deal market as the key insight of this paper and provides a theoretical explanation for why platforms should carefully organize sellers when conducting the daily deal campaign, although considerable efforts and high costs are required to enroll sellers. This tactic enables the platform to charge high percentage fees in the daily deal market without information asymmetry among competing sellers. The previous discussion also highlights the value of sellers operational information, which should be carefully protected in online markets (Jiang et al. 2011). That is, sellers should not share their quality or cost information with the upstream platform to prevent the latter’s strategic use of such information via segmentation.

## 4.4. Potential Demand

Our basic model characterizes the heterogeneity among sellers by quality differentiation, which is built upon different production costs. To focus on the effect of production cost, we assume that the potential demand is the same for two seller types, as given in (1). In this section, we relax this assumption to examine how different potential demand can in<sup>fl</sup>uence <sup>fi</sup>rms equilibrium decisions and pro<sup>fi</sup>ts. Particularly, we assume that a seller offering higher product quality applies not only a higher production cost but also higher potential demand. Then, given seller organization format $j , j = s$ or a and seller type $i , i = h$ or l, an organized seller’s pro<sup>fi</sup>t in each round of the campaign is rewritten as

$$
\pi_ {i} ^ {j} \Big (p _ {i} ^ {j} \Big) = \Big ((1 - \gamma_ {j}) p _ {i} ^ {j} - c _ {i} \Big) d _ {i} ^ {j},\tag{8}
$$

in which the realized demand functions for seller i organized under different seller organization formats are given as follows:

$$
\begin{array}{r l} & {\mathrm{Agglomeration:} d _ {i} ^ {a} = \lambda (b _ {i} - p _ {i} ^ {a} + \theta (p _ {h} ^ {a *} - p _ {i} ^ {a})} \\ & {\qquad + (1 - \lambda) (b _ {i} - p _ {i} ^ {a} + \theta (p _ {l} ^ {a *} - p _ {i} ^ {a})),} \\ & {\qquad i = h \mathrm{or} l.} \end{array}
$$

Segmentation: $d _ { i } ^ { s } = b _ { i } - p _ { i } ^ { s } + \theta ( p _ { i } ^ { s * } - p _ { i } ^ { s } ) , \quad i = h \mathrm { o r } l .$

(9)

(10)

In (9) and (10), $b _ { h } = b + \varepsilon$ and $b _ { l } = b - \varepsilon ,$ , and $\varepsilon \in ( 0 , b )$ denotes the difference of potential demand between the two seller types. In this manner, product quality is positively correlated with potential demand, wherein higher product quality leads to greater potential demand for the seller. Thus, a higher ε might result from a larger quality differentiation, and the model reduces to the basic model when $\varepsilon = 0$ . We follow a similar principle to derive equilibrium pricing and percentage fee decisions made under the agglomeration and segmentation strategies, respectively. With the following proposition, we show how different potential demand in<sup>fl</sup>uences the platform’s equilibrium strategies and pro<sup>fi</sup>ts.

Proposition 4. Considering different potential demand, in equilibrium, the platform sets a higher percentage fee and obtains a higher profit under the segmentation strategy than under the agglomeration strategy, whose surplus increases with ε:

Proposition 4 demonstrates that the key insights obtained from the basic model are robust to different potential demand: The platform remains better off under the segmentation strategy (rather than the agglomeration strategy) by charging a higher percentage fee. Moreover, it is evident that the pro<sup>fi</sup>t gap between the two formats increases with ε. That is, the bene<sup>fi</sup>t of seller segmentation becomes more pronounced to the platform when quality differentiation (potential demand) between the two seller types increases. This is the case because when the gap in product quality expands, the heterogeneity between the two seller types increases. This result ampli<sup>fi</sup>es the negative effect of the agglomeration strategy because the sellers’ pricing decisions become less adequate when they cannot identify the competitor’s quality. In contrast, the segmentation strategy still allows the sellers to make adequate pricing decisions by eliminating information asymmetry between them and thus allows the platform to extract more surplus from the sellers.

## 4.5. Consumer Retention

In addition to attracting new consumers, an important function of daily deal campaigns is to persuade consumers who have purchased daily deals to later visit the regular market. This is de<sup>fi</sup>ned as the consumer retention effect of daily deal campaigns. In this section, we examine how the equilibrium outcomes are in<sup>fl</sup>u enced by consumer retention.

Consistent with the literature (Kumar and Rajan 2012, Edelman et al. 2016), we assume that the population of consumers who reenter the regular market after the daily deal campaign is linear and proportional to the population of consumers who purchase a daily deal. That is, the population of returning consumers for the i type seller under the j organization format is given by $\dot { \alpha { d _ { i } ^ { j } } }$ wherein $i = h$ or l and j <sub>-</sub> s or a. Note that $\alpha \in ( 0 , 1 )$ indicates the retention rate of consumers, whose value is constant and exogenously given. When $\alpha = 0$ , the model reduces to the basic model. To focus on the daily deal campaign and avoid trivial discussions, we also assume that prices in the regular market are exogenously given and independent of dealing prices in the campaign, which has been widely adopted in the literature (Kumar and Rajan 2012,

Edelman et al. 2016). Particularly, we de<sup>fi</sup>ne prices in the regular market as $p _ { h } ^ { 0 } \ ( p _ { l } ^ { 0 } )$ for the high-type (lowtype) seller with $p _ { h } ^ { 0 } > c _ { h } \stackrel { . . . } { ( p _ { l } ^ { 0 } > c _ { l } ) }$ . Other settings remain unchanged from those of the basic model.

With consumer retention, the seller’s pro<sup>fi</sup>t from the daily deal campaign then has two sources: Consumers’ immediate purchases of daily deals and reentered consumers’ purchases in the regular market. Therefore, for seller type $i , i = h$ or l in the organization format $j , j = s$ or $^ { a , }$ its pro<sup>fi</sup>t can be rewritten as

$$
\pi_ {i} ^ {j} \Big (p _ {i} ^ {j} \Big) = \underbrace {((1 - \gamma_ {j}) p _ {i} ^ {j} - c _ {i}) d _ {i} ^ {j}} _ {\text {Immediate purchase}} + \underbrace {(p _ {i} ^ {0} - c _ {i}) \alpha d _ {i} ^ {j}} _ {\text {Consumer retention}},\tag{11}
$$

where realized demand $d _ { i } ^ { j }$ remains unchanged from the baseline model.

Given the seller’s pro<sup>fi</sup>t function, one can follow a similar principle to derive equilibrium pricing and percentage fee decisions made under the agglomeration and segmentation strategies. With the following proposition, we suggest how consumer retention in-<sup>fl</sup>uences <sup>fi</sup>rms’ equilibrium strategies and pro<sup>fi</sup>ts.

Proposition 5. Considering consumer retention, in equilibrium, the following results apply.

1. The seller sets a lower dealing price, whose value decreases with $\alpha ,$ relative to those of the basic model under either seller organization format.

2. The platform increases the percentage fee, whose value increases with $\alpha ,$ relative to those of the basic model under either seller organization format.

3. The platform sets a higher percentage fee and obtains a higher profit under the segmentation strategy than under the agglomeration strategy, wherein this profit gap increases with α.

This proposition shows that with consumer retention, a seller will set a lower dealing price to increase realized demand for the daily deal campaign. This tactic allows the seller to motivate more consumers to buy the product in the regular market. When the proportion of consumer retention increases, the seller has a stronger incentive to reduce the dealing price to extract more surplus from the regular market. The increased demand for the daily deal campaign allows the platform to charge a higher percentage fee. Moreover, the platform still obtains a higher pro<sup>fi</sup>t by choosing the seller segmentation strategy instead of the agglomeration strategy wherein this pro<sup>fi</sup>t gap increases with the retention rate α. This result demonstrates that our main conclusions remain robust when considering consumer retention. Intuitively, one can view the effect of consumer retention as a reduction of the seller’s production cost in the daily deal selling season, that is, from $c _ { i }$ to $c _ { i } - ( p _ { i } ^ { 0 } - c _ { i } ) \alpha$ . Therefore, sellers bene<sup>fi</sup>t from consumer retention as their production costs decrease. This result incentivizes the platform to charge a higher percentage fee and extract more surplus from the sellers. In this sense, both the platform and sellers bene<sup>fi</sup>t from consumer retention, from which pro<sup>fi</sup>tability monotonically increases with the rate of consumer retention (see more details in Online Appendix C).

We next brie<sup>fl</sup>y discuss what occurs when the retention rates differ between the two seller types. For example, the population of returning consumers for the high-type seller is $\alpha _ { h } d _ { h } ^ { j }$ and that for the low-type seller is $\overset { \cdot } { \alpha _ { l } } d _ { l } ^ { j } , \overset { \cdot } { j } = s$ or a, and $\alpha _ { h } \neq \alpha _ { l }$ . One can infer that the effect of consumer retention on the platform remains qualitatively similar to that speci<sup>fi</sup>ed by Proposition $5 ,$ according to which consumer retention allows the platform to charge a higher percentage fee and obtain a higher pro<sup>fi</sup>t. Nonetheless, consumer retention now does not necessarily bene<sup>fi</sup>t sellers and may negatively affect them under certain conditions. This result occurs when the gap between the retention rates of the two seller types is suf<sup>fi</sup>ciently large. That is, for the seller type with a low consumer retention rate, the bene<sup>fi</sup>t from cost reduction cannot compensate for the higher percentage fee charged by the platform, and the effect of consumer retention may be deleterious (details are shown in Online Appendix C).

## 5. Extensions

In this section, we consider three extensions. First, we examine a more general daily deal setting in which there are n sellers participating in the campaign. We also explore how the platform should determine the optimal number of sellers organized in each round of the campaign. Second, we assume that there is more than one daily deal platform to identify the effect of platform competition. Third, we investigate what happens when the platform can exercise percentage fee discrimination for two types of sellers.

## 5.1. Number of Sellers

Let us consider a general setup in which there are n $\left( n \geq 2 \right)$ sellers enrolled in the daily deal campaign. When there is only one seller involved in the daily deal campaign, the agglomeration strategy and segmentation strategy are identical, and the analysis therefore reduces to a standard two-echelon pricing game.<sup>7</sup> In this section, we examine how the number of organized sell ers in<sup>fl</sup>uences <sup>fi</sup>rms’ equilibrium strategies and pro<sup>fi</sup>ts. We still assume that there are two types of sellers in the seller pool, and the proportions of high- and lowtype sellers are given by λ and $1 - \lambda ,$ , respectively. We provide a seller’s demand function in (12), wherein there are n sellers organized in the campaign.

$$
\begin{array}{l} {d _ {t} = \frac {1 + 2 \theta}{1 + n \theta} \Bigg [ b - p _ {t} + \sum_ {k \neq t} \theta (p _ {k} - p _ {t}) \Bigg ],} \\ {0 <   \theta <   1, t = 1, 2, \ldots , n, k = 1, 2, \ldots , n.} \end{array}\tag{12}
$$

This equation captures pricing competition among n sellers under the two seller organization formats, which is consistent with classic works in economics, that is, Bulow et al. (1985), Gox (¨ 2000), and Arya and Mittendorf (2007).<sup>8</sup> It is easy to be veri<sup>fi</sup>ed that when n increases, each seller’s potential demand decreases because the market is more crowded and competition is intensi<sup>fi</sup>ed, that is, $\partial \mathopen { } \mathclose \bgroup \left( \frac { 1 + 2 \theta } { 1 + n \theta } b \aftergroup \egroup \right) / \partial n < 0$ . When $n = 2$ , the demand function reduces to our basic model setting (Equation (1)). We <sup>fi</sup>rst provide the seller’s pro<sup>fi</sup>t function under a certain seller organization format. That is, for the organized seller of type $i , i = h$ or $l ,$ under the agglomeration strategy, its pro<sup>fi</sup>t is

$$
\begin{array}{c} \pi_ {i} ^ {a} (p _ {i} ^ {a}) = \frac {1 + 2 \theta}{1 + n \theta} ((1 - \gamma_ {a}) p _ {i} ^ {a} - c _ {i}) (b - (1 + (n - 1) \theta) p _ {i} ^ {a} \\ \qquad + (n - 1) \lambda \theta p _ {h} ^ {a *} + (n - 1) (1 - \lambda) \theta p _ {l} ^ {a *}). \end{array}\tag{13}
$$

Under the segmentation strategy for the organized seller of type $i , i = h$ or $l ,$ its pro<sup>fi</sup>t is

$$
\begin{array}{c} \pi_ {i} ^ {s} (p _ {i} ^ {s}) = \frac {1 + 2 \theta}{1 + n \theta} ((1 - \gamma_ {s}) p _ {i} ^ {s} - c _ {i}) (b - (1 + (n - 1) \theta) p _ {i} ^ {s} \\ + (n - 1) \theta p _ {i} ^ {s *}). \end{array}\tag{14}
$$

We can also present the platform’s pro<sup>fi</sup>t function with n competing sellers under a certain seller organization format wherein

$$
\pi_ {p} ^ {j} (\gamma_ {j}) = n \gamma_ {j} \Bigl (\lambda p _ {h} ^ {j *} d _ {h} ^ {j *} + (1 - \lambda) p _ {l} ^ {j *} d _ {l} ^ {j *} \Bigr), j = a \mathrm{or} s.\tag{15}
$$

We follow a similar principle to derive the equilibrium outcomes under the agglomeration and segmentation strategies, respectively. The analysis is routine, and we include further details in Online Appendix B. In the following proposition, we show how the generalization of the number of sellers in<sup>fl</sup>uences <sup>fi</sup>rms equilibrium strategies and pro<sup>fi</sup>ts.

Proposition 6. Unlike for the basic model, when there are more sellers organized in the daily deal campaign, we obtain the following results.

1. Under both seller organization formats, the seller’s dealing price decreases with $n ,$ but the total market demand increases with n:

2. The platform obtains a higher profit under the segmentation strategy than under the agglomeration strategy, and the profit gap increases with n.

From Proposition $^ { 6 , }$ the main conclusions are qualitatively similar to those obtained in the basic model, indicating that the key insights are robust to the number of sellers. First, when there are more competing sellers enlisted, each seller’s dealing price decreases because of the higher competition intensity, but this situation leads to more total market demand for the daily deal campaign. Second, the platform always bene<sup>fi</sup>ts from more intense downstream competition as the total market demand for and the total sales revenue of the daily deal campaign increase. Third, the platform still obtains a higher pro<sup>fi</sup>t under the segmentation strategy, whose surplus over the agglomeration strategy increases with the number of sellers enrolled in the campaign, as shown graphically in Figure 5. This is the case because with the increasing number of sellers, the degree of information asymmetry increases under the agglomeration strategy. In contrast, the seg mentation strategy can fully eliminate this information asymmetry, and thus, its advantages over the agglom eration strategy become more prominent.

Figure 5. (Color online) Impact of the Number of Sellers on the Pro<sup>fi</sup>t Gap $( b = 3 , c _ { h } = 1 , \overline { { c _ { l } } } = 0 . 5 , \theta = 0 . 5 )$  
![](/api/attachments/WSBKJBBK/fulltext/images/dedeac1c540a0a196f846159a51d87d99b2f0d8421fed533b98a46ba51a58d69.jpg)

We also discuss which number of sellers enrolled in one round of the daily deal campaign is most bene<sup>fi</sup>- cial to the platform. Based on the previous results, the platform’s pro<sup>fi</sup>t certainly increases with the number of sellers involved in the daily deal campaign, and this bene<sup>fi</sup>t can be further ampli<sup>fi</sup>ed by adopting the segmentation strategy. However, it shows that the marginal bene<sup>fi</sup>t of enrolling a new seller lessens with respect to the number of sellers that can be organized in the campaign. This result implies that the platform may need to balance the additional gain and cost of expanding the seller pool involved in the daily deal campaign. To successfully implement the segmentation strategy, the platform should <sup>fi</sup>rst identify each seller’s type and then organize the same seller type in every round of the campaign, which inevitably increases management costs. Another factor that may in<sup>fl</sup>uence the optimal number of sellers is the fact that each seller’s pro<sup>fi</sup>t is reduced when increasing the number of sellers. This result sets an upper bound on the number of sellers, which should ensure that each seller’s pro<sup>fi</sup>t is no lower than its reserved pro<sup>fi</sup>t.

## 5.2. Platform Competition

In this section, we extend our basic model by considering platform competition, that is, an entrant platform can also exercise daily deal campaigns. We assume that in each round of the campaign, the incumbent platform still selects two sellers from the seller pool according to the previous two seller organization formats, and the entrant platform selects one seller from the pool with probability λ (1 <sub>−</sub> λ) to be a high-type (low-type) seller. It is understood that an entrant platform has a limited capability to organize more sellers in the daily deal campaign. For example, in its start-up phase, Groupon involved only one seller for its daily deals in a particular region. More importantly, the key insights remain qualitatively similar when we allow the entrant platform to select more sellers in each round of the campaign. We also assume that the incumbent and entrant platforms charge the same percentage fee. This situation can be understood that the entrant platform simply chooses a strategy to follow the incumbent platform. Moreover, when this assumption is violated, the sellers would choose only the platform with a lower percentage fee. In this sense, in equilibrium, the two platforms’ percentage fees should converge to the same level.

We next investigate the effect of platform competition on the incumbent platform’s equilibrium strategies and pro<sup>fi</sup>ts. We <sup>fi</sup>rst provide the sellers’ demand functions on the incumbent platform, which depend on the incumbent platform’s seller organization format. Under the agglomeration strategy, the incumbent platform organizes its sellers such that each organized seller’s demand should be

$$
\begin{array}{c} d _ {i} ^ {a} (p _ {i} ^ {a}) = \frac {1 + 2 \theta}{1 + 3 \theta} \big (b - (1 + 2 \theta) p _ {i} ^ {a} + 2 \lambda \theta p _ {h} ^ {a *} \\ + 2 (1 - \lambda) \theta p _ {l} ^ {a *}), i = h \text {or} l. \end{array}\tag{16}
$$

In (16), the demand function can be derived directly based on (12) by assuming that n <sub>-</sub> 3. Under the segmentation strategy, the incumbent platform chooses sellers of the same type, whereas the entrant platform chooses its seller arbitrarily. Thus, for a seller organized on the incumbent platform, its demand is given by

$$
\begin{array}{r} d _ {h} ^ {s} (p _ {h} ^ {s}) = \frac {1 + 2 \theta}{1 + 3 \theta} \big [ \lambda (b - p _ {h} ^ {s} + 2 \theta (p _ {h} ^ {s *} - p _ {h} ^ {s})) \\ + (1 - \lambda) (b - p _ {h} ^ {s} + \theta (p _ {h} ^ {s *} - p _ {h} ^ {s}) + \theta (p _ {l} ^ {s *} - p _ {h} ^ {s})) \big ], \end{array}\tag{17}
$$

and

$$
\begin{array}{c} d _ {l} ^ {s} (p _ {l} ^ {s}) = \frac {1 + 2 \theta}{1 + 3 \theta} \big [ \lambda (b - p _ {l} ^ {s} + \theta (p _ {l} ^ {s *} - p _ {l} ^ {s}) + \theta (p _ {h} ^ {s *} - p _ {l} ^ {s})) \\ + (1 - \lambda) (b - p _ {l} ^ {s} + 2 \theta (p _ {l} ^ {s *} - p _ {l} ^ {s})) \big ]. \end{array}\tag{18}
$$

Based on (16)–(18), we solve the sellers’ optimal dealing prices and realized demand (details are shown in

Online Appendix B). Then, we derive the incumbent platform’s pro<sup>fi</sup>t functions under the two seller organization formats. In a standard manner, we compare the equilibrium outcomes under the two formats and present the main results as follows.

Proposition 7. Unlike those of the basic model, we find the following results for platform competition.

1. The incumbent platform charges a lower percentage fee and obtains a lower profit under each seller organization format.

2. The incumbent platform’s profit is higher under the segmentation strategy than under the agglomeration strategy, but the profit gap decreases.

Proposition 7(1) indicates that the incumbent plat form suffers from platform competition whereby its percentage fee and pro<sup>fi</sup>t decrease because of market erosion from the entrant platform. Proposition 7(2) shows that the incumbent platform still bene<sup>fi</sup>ts more from the seller segmentation strategy; however, its surplus over the agglomeration strategy diminishes. That is because, unlike under the basic model, in the presence of the entrant platform, the incumbent platform cannot fully eliminate information asymmetry for its enrolled sellers by adopting the segmentation strategy. In other words, the incumbent platform can eliminate only the internal information asymmetry between its sellers while outside information asymmetry still exists (from the entrant platform). This arrangement prevents the sellers on the incumbent platform from making pricing decisions as adequately as they could without platform competition. Given that the positive effect of the segmentation strategy is weakened by platform competition, its surplus over the agglomeration strategy decreases. Moreover, it can be inferred that when the entrant platform can organize more sellers to use daily deals or more platforms entering the market, the pro<sup>fi</sup>t gap between the segmentation and agglomeration strategies is further reduced. Similar to the basic model, this result again highlights the inherent difference between the two seller organization formats for the platform: Information structure. The value of the segmentation strategy relative to the agglomeration strategy hinges largely on the extent to which the former can eliminate information asymmetry among competing sellers in the daily deal campaign.

## 5.3. Percentage Fee Discrimination

In the basic model, we assume that the platform sets the same percentage fee for two types of sellers. As mentioned, this assumption is very prevalent in practice, because percentage fee discrimination may result in fairness issues in the business transactions between the platform and sellers. Nonetheless, it remains worthwhile to examine what occurs when the platform can exercise percentage fee discrimination for different types of sellers. Thus, in this section, we relax the assumption of a uniform percentage fee. Given a certain seller organization format, the platform <sup>fi</sup>rst sets the percentage fees for two types of sellers, and then the sellers are engaged in the daily deal campaign. The other settings remain unchanged from those of the basic model. Because this analysis is quite challenging and the analytical result is therefore intractable, we solve this game via numerical studies (details are shown in Online Appendix C). We then elaborate on the effects of percentage fee discrimination on the equilibrium outcomes as follows.

First, it can be inferred that percentage fee discrimination endows the platform with more leeway in making decisions, which undoubtedly bene<sup>fi</sup>ts the platform. However, this result has adverse effects on sellers’ pro<sup>fi</sup>tability. The high-type seller bene<sup>fi</sup>ts from discrimination, as the platform will charge a lower percentage fee to compensate for its high production cost. In contrast, the low-type seller is negatively affected by discrimination, as the platform will now set a more aggressive percentage fee to extract more surplus from it.

Second, it shows that the pro<sup>fi</sup>t gap for the platform between the two seller organization formats narrows due to percentage fee discrimination. This is because the platform may charge different percentage fees for enlisted sellers in each round of the campaign under the agglomeration strategy but will charge the same percentage fee for enlisted sellers under the segmentation strategy (under segmentation, competition always arises between sellers with the same type, so it is unnecessary for the platform to set different percentage fees). In this sense, the effect of percentage fee discrimination is not substantial under the segmentation strategy. In contrast, under the agglomeration strategy, when competition arises between high- and lowtype sellers, the platform will charge a higher (lower) percentage fee to the low-type (high-type) seller. This percentage fee discrimination, as mentioned, allows the platform to extract more surplus from the sellers, resulting in a more substantial improvement of the platform’s pro<sup>fi</sup>t under the agglomeration strategy.

## 6. Conclusion

Motivated by the prosperity of platform-based markets, this paper investigates the interplay between a platform and multiple competing sellers involved in a daily deal business setting. We assume that the platform can <sup>fi</sup>rst select two sellers from the seller pool to exercise one representative round of the daily deal campaign and charge a percentage fee. Then, the sellers are engaged in Bertrand competition by simultaneously determining their dealing prices. We speci<sup>fi</sup>cally identify two seller organization formats for the platform, both of which are prevalent in practice. The <sup>fi</sup>rst is the seller agglomeration strategy, under which the platform does not distinguish the types of sellers to involve when selecting them from the seller pool, and the second is the seller segmentation strategy, under which the platform deliberately selects sellers of the same type to compete in each round of the campaign. Our analysis uncovers prominent effects of the seller organization format on <sup>fi</sup>rms’ equilibrium pricing strategies and percentage fees and on their pro<sup>fi</sup>tability.

We show that unlike under the agglomeration strategy, when using seller segmentation, the platform can eliminate internal information asymmetry between the competing sellers, which enables them to make more adequate pricing decisions. This result allows the sell ers to extract more sales revenue from the daily dea market but reversely incentivizes the platform to charge a higher percentage fee under the segmentation. In strict contrast, under the seller agglomeration strategy, sellers make inadequate pricing decisions because of information asymmetry, which induces the platform to charge a lower percentage fee to compensate for the sellers’ losses. Overall, we show that the segmentation strategy increases the platform’s percentage fee, which decentralizes the vertical relationship between the platform and sellers, and it is bene<sup>fi</sup>cial to the platform but detrimental to the sellers. The entire system is also negatively affected by seller segmentation because of ampli<sup>fi</sup>ed double marginalization.

We also <sup>fi</sup>nd that the value of the seller organization format hinges largely on the composition of sellers in the daily deal market, wherein the surplus of the seg mentation strategy over the agglomeration strategy (to the platform) exhibits an inverse U-shaped relationship with the proportion of high-type sellers. Moreover, when the difference in product quality between the two types of sellers increases or the platform can select more sellers for the campaign, it is more bene<sup>fi</sup>cial for the platform to adopt the segmentation strategy to organize sellers in the daily deal market. In contrast, when an entrant platform enters or the platform can adopt percentage fee discrimination for sellers of different types, the bene<sup>fi</sup>t of the segmentation strategy diminishes. With platform competition, the incumbent platform’s pro<sup>fi</sup>t and the pro<sup>fi</sup>t gap between the two seller organization formats are inevitably reduced. That is because the incumbent platform cannot fully eliminate information asymmetry among the competing sellers through segmentation, which further reduces the bene<sup>fi</sup>t of this seller organization strategy. With pricing <sup>fl</sup>exibility, the platform may set different percentage fees for the competing sellers under the ag glomeration strategy but sets the same percentage fee under the segmentation strategy given that the sellers are of the same type. This situation also narrows the pro<sup>fi</sup>t gap between the two seller organization formats.

Our paper certainty presents limitations. First, we consider a single-round daily deal campaign as a representative case to examine strategic interactions between a platform and multiple competing sellers. This approach is suitable when the daily deal market reaches a stable state. Nonetheless, it would be worth considering more variances in the daily deal market that might change the equilibrium outcomes. For example, a seller might not only participate in daily deal campaigns but also simultaneously sell products in the regular market; then, how the seller’s regular selling channel in<sup>fl</sup>uences its interaction with the platform. This possibility is quite interesting to consider. Second, as mentioned, we assume that percentage fees are identical across the competing platforms. Relaxing this constraint may lead to interesting questions regarding how sellers should choose appropriate daily deal platforms and how platforms should determine their percentage fees to attract sellers. These questions are challenging but worth exploring in the future.

## Acknowledgments

The authors acknowledge the invaluable contributions of the senior editors, associate editor, and anonymous reviewers, whose constructive comments signi<sup>fi</sup>cantly im proved our work in many ways. The authors contributed equally.

## Endnotes

<sup>1</sup> Groupon and LivingSocial are two leading daily deal websites from the United States (Zhang and Chung 2020); find more information on the websites at www.groupon.com and www. livingsocial.com, respectively.

<sup>2</sup> We collected data on March 27, 2021, by searching for wireless mouse deals on Groupon in the electronics category. We identified 16 wireless mouse deals from different sellers on that day. We chose wireless mouse to reduce possible heterogeneity between deals except in relation to product quality which might lead to disparate prices.

<sup>3</sup> We collected data by searching for wireless mouse deals under the electronics category of the Pin Pai Shan Gou on March 27, 2021, and Mei Ri Te Jia on March 28, 2021. Again, we chose wireless mouse to reduce possible heterogeneity (except in product quality) among deals that might lead to disparate prices. We identified 32 and 29 deals on wireless mouse from the two channels, respectively, from different sellers on that day. The mean price of a wireless mouse on the Pin Pai Shan Gou channel is 161.6 CNY and that on the Mei Ri Te Jia channel is 35.3 CNY. We conducted an analysis of variance (ANOVA) to show that prices listed on the two daily deal channels are significantly different. This conclusion indicates that the enlisted sellers of the two channels are probably from two different seller segments exhibiting potential heterogeneity in product quality.

<sup>4</sup> We illustrate these two seller organization formats with screenshots taken from Groupon’s and JD’s websites in Online Appendix A.

<sup>5</sup> Specifically, the platform can directly infer the seller’s type based on its price: high prices for high types and low prices for low types.

<sup>6</sup> That is, our paper implicitly assumes that enrolling both types of sellers is an ultimate equilibrium outcome for a daily deal platform in competitive environments. This argument is theoretically supported by Karle et al. (2020), documenting that for competition between plat forms, one potential outcome should involve one dominant platform and all types of sellers participating in this platform. This assumption also fits well the practice of the daily deal business, which usually has one dominant daily deal platform, like Groupon in the United State and Juhuasuan in China.

<sup>7</sup> We provide a detailed comparison between the cases of a single seller and two competing sellers participating in the daily deal cam paign in Online Appendix C.

<sup>8</sup> To remain consistent with our basic model, we make slight changes to the classic demand function with pricing competition, which has no effects on our equilibrium outcomes.

## References

Abhishek V, Jerath K, Zhang ZJ (2016) Agency selling or reselling? Channel structures in electronic retailing. Management Sci. 62(8): 2259–2280.

Arya A, Mittendorf B (2007) Interacting supply chain distortions: The pricing of internal transfers and external procurement. Ac counting Rev. 82(3):551–580.

Bai X, Marsden JR, Ross WT Jr, Wang G (2017) How e-WOM and local competition drive local retailers’ decisions about daily deal offerings. Decis. Support Syst. 101:82–94.

Bhardwaj P, Sajeesh S (2017) Strategic revenue sharing with daily deal sites: A competitive analysis. Decision Sci. 48(6):1228–1261.

Bulow JI, Geanakoplos JD, Klemperer PD (1985) Multimarket oligopoly: Strategic substitutes and complements. J. Political Econom. 93(3):488–511.

Byers JW, Mitzenmacher M, Zervas G (2011) Daily deals: Prediction, social diffusion, and reputational rami<sup>fi</sup>cations. Proc. 5th ACM WSDM Conf, Web Search Data Mining (ACM, New York), 543–552.

Cao Z, Hui KL, Xu H (2018) When discounts hurt sales: The case of daily-deal markets. Inform. Systems Res. 29(3):567–591.

Dholakia UM (2011a) A startup’s experience with running a Group on promotion. Working paper, Rice University, Houston, TX.

Dholakia UM (2011b) How businesses fare with daily deals: A mul tisite analysis of Groupon, LivingSocial, OpenTable, Travel zoo, and Buy With Me promotions. Working paper, Rice University, Houston, TX.

Dholakia UM (2011c). What makes Groupon promotions pro<sup>fi</sup>table for businesses. Working paper, Rice University, Houston, TX.

Dholakia UM (2012). How businesses fare with daily deals as they gain experience: A multi-time period study of daily deal performance. Working paper, Rice University, Houston, TX.

Edelman B, Jaffe S, Kominers SD (2016) To Groupon or not to Groupon: The pro<sup>fi</sup>tability of deep discounts. Marketing Lett. 27(1):39–53.

Gox RF (2000) Strategic transfer pricing, absorption costing, and ob-¨ servability. Management Accounting Res. 11(3):327–348.

Hao L, Fan M (2014) An analysis of pricing models in the electronic book market. MIS Quart. 38(4):1017–1032.

Hu M, Dang C, Chintagunta PK (2019) Search and learning at a dai ly deals website. Marketing Sci. 38(4):609–642.

Hu M, Shi M, Wu J (2013) Simultaneous vs. sequential groupbuying mechanisms. Management Sci. 59(12):2805–2822.

Jiang BJ, Zou TX (2020) Consumer search and <sup>fi</sup>ltering on online retail platforms. J. Marketing Res. 57(5):900–916.

Jiang BJ, Jerath K, Srinivasan K (2011) Firm strategies in the “Mid Tail” of platform-based retailing. Marketing Sci. 30(5):757–775.

Jing X, Xie J (2011) Group buying: A new mechanism for selling through social interactions. Management Sci. 57(8):1354–1372.

Karle H, Peitz M, Reisinger M (2020) Segmentation vs. agglomeration: Competition between platforms with competitive sellers. J. Political Econom. 128(6):2329–2374.

Kitchens B, Kumar A, Pathak P (2018) Electronic markets and geographic competition among small, local <sup>fi</sup>rms. Inform. Systems Res. 29(4):928–946.

Kumar V, Rajan B (2012) Social coupons as a marketing strategy: A multifaceted perspective. J. Acad. Marketing Sci. 40(1):120–136.

Li X, Wu L (2018) Herding and social media word-of-mouth: Evidence from Groupon. MIS Quart. 42(4):1331–1351.

Li H, Shen Q, Bart Y (2018) Local market characteristics and onlineto-of<sup>fl</sup>ine commerce: An empirical analysis of Groupon. Man agement Sci. 64(4):1860–1878.

Liu Y, Sutanto J (2012) Buyers’ purchasing time and herd behavior on deal-of-the-day group-buying websites. Electronic Marketing 22(2):83–93.

Luo X, Andrews M, Song Y, Aspara J (2014) Group-buying deal popularity. J. Marketing 78(2):20–33.

Muthers J, Wismer S (2013) Why do platforms charge proportional fees? Commitment and seller participation. Working paper, University of Wuerzburg, Wurzburg, Germany.

Pentina I, Taylor DG (2013) Regulatory focus and daily-deal message framing: Are we saving or gaining with Groupon? J. Inter active Advertising 13(2):67–75.

Reiner J, Skiera B (2019) Helping merchants to assess the pro<sup>fi</sup>tability of deal-of-the-day promotions. Interfaces 48(3):247–259.

Shivendu S, Zhang Z (2013) Economics of daily-deal website: Advertising and sampling effects. Working paper, University of California, Irvine.

Song M, Park E, Yoo B, Jeon S (2016) Is the daily deal social shopping? An empirical analysis of customer panel data. J. Interactive Marketing 33(1):57–76.

Stephen AT, Toubia O (2010) Deriving value from social commerce networks. J. Marketing Res. 47(2):215–228.

Subramanian U, Rao RC (2016) Leveraging experienced consumers to attract new consumers: An equilibrium analysis of displaying deal sales by daily deal websites. Management Sci. 62(12): 3555–3575.

Tian L, Vakharia AJ, Tan YL, Xu YF (2018) Marketplace, reseller, or hybrid: Strategic analysis of an emerging e-commerce model. Production Oper. Management 27(8):1595–1610.

Wang Z, Wright J (2017) Ad valorem platform fees, indirect taxes, and ef<sup>fi</sup>cient price discrimination. RAND J. Econom. 48(2): 467–484.

Wang Z, Wright J (2018) Should platforms be allowed to charge ad valorem fees. J. Industry Econom. 66(3):739–760.

Zhang L, Chung DJ (2020) Price bargaining and competition in online platforms: An empirical analysis of the daily deal market. Marketing Sci. 39(4):687–706.

Zhao M, Wang Y, Gan X (2016) Signaling effect of daily deal promotion for a start-up service provider. J. Oper. Res. Soc. 67(2): 280–293.

C<sub>opy</sub>ri<sub>g</sub>ht 2022 b<sub>y</sub> INFORMS <sub>a</sub>ll ri<sub>g</sub>ht<sub>s</sub> r<sub>ese</sub>r<sub>ve</sub>d<sub>.</sub> C<sub>opy</sub>ri<sub>g</sub>ht <sub>o</sub>f Inf<sub>o</sub>rm<sub>a</sub>ti<sub>o</sub>n S<sub>ys</sub>t<sub>e</sub>m<sub>s</sub> R<sub>esea</sub>r<sub>c</sub>h i<sub>s</sub> th<sub>e</sub> <sub>p</sub>r<sub>ope</sub>rt<sub>y</sub> <sub>o</sub>f INFORMS <sub>:</sub> In<sub>s</sub>tit<sub>u</sub>t<sub>e</sub> f<sub>o</sub>r O<sub>pe</sub>r<sub>a</sub>ti<sub>o</sub>n<sub>s</sub> R<sub>esea</sub>r<sub>c</sub>h <sub>a</sub>nd it<sub>s</sub> <sub>co</sub>nt<sub>e</sub>nt m<sub>ay</sub> <sub>no</sub>t b<sub>e cop</sub>i<sub>e</sub>d <sub>or ema</sub>il<sub>e</sub>d t<sub>o mu</sub>lti<sub>p</sub>l<sub>e s</sub>it<sub>es or pos</sub>t<sub>e</sub>d t<sub>o a</sub> li<sub>s</sub>t<sub>serv w</sub>ith<sub>ou</sub>t th<sub>e copyr</sub>i<sub>g</sub>ht h<sub>o</sub>ld<sub>er</sub><sup>'</sup><sub>s</sub> <sub>expres s</sub> <sub>wr</sub>itt<sub>en</sub> <sub>perm</sub>i<sub>s s</sub>i<sub>on.</sub> H<sub>owever</sub> <sub>users</sub> <sub>may</sub> <sub>pr</sub>i<sub>n</sub>t d<sub>own</sub>l<sub>oa</sub>d <sub>or</sub> <sub>ema</sub>il <sub>ar</sub>ti<sub>c</sub>l<sub>es</sub> f<sub>or</sub> i<sub>n</sub>di<sub>v</sub>id<sub>ua</sub>l <sub>use</sub>
