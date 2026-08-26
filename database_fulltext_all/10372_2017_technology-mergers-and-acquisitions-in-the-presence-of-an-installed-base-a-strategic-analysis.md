---
otero_id: 10372
otero_key: "HGU3A9TC"
title: "Technology Mergers and Acquisitions in the Presence of an Installed Base: A Strategic Analysis"
authors: "Qiu-Hong Wang; Kai-Lung Hui"
year: "2017"
journal: "Information Systems Research"
doi: "10.1287/isre.2016.0659"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
This article was downloaded by: [132.239.1.231] On: 22 January 2017, At: 12:18 Publisher: Institute for Operations Research and the Management Sciences (INFORMS) INFORMS is located in Maryland, USA

# Information Systems Research

## HSR

![](/api/attachments/HGU3A9TC/fulltext/images/6fc18f7d30ad8eea52e6533c6d1db688d33757415df3d006b72cbb8494983fc3.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

## Technology Mergers and Acquisitions in the Presence of an Installed Base: A Strategic Analysis

Qiu-Hong Wang, Kai-Lung Hui

To cite this article:

Qiu-Hong Wang, Kai-Lung Hui (2017) Technology Mergers and Acquisitions in the Presence of an Installed Base: A Strategic Analysis. Information Systems Research

Published online in Articles in Advance 18 Jan 2017

http://dx.doi.org/10.1287/isre.2016.0659

Full terms and conditions of use: http://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

Copyright © 2017, INFORMS

Please scroll down for article—it is on subsequent pages

![](/api/attachments/HGU3A9TC/fulltext/images/b08b6b874e1b7f28ffd36baced0794481cd687abeae709c32f0c36a2cee8dd78.jpg)

INFORMS is the largest professional society in the world for professionals in the fields of operations research, management science, and analytics.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# Technology Mergers and Acquisitions in the Presence of an Installed Base: A Strategic Analysis

Qiu-Hong Wang,<sup>a</sup> Kai-Lung Hui<sup>b</sup>

<sup>a</sup> School of Information Systems, Singapore Management University, Singapore 188065; <sup>b</sup> School of Business and Management, Hong Kong University of Science and Technology, Clear Water Bay, Hong Kong

Contact: qiuhongwang@smu.edu.sg (QhW); klhui@ust.hk (KlH)

Received: October 5, 2012 Accepted: June 15, 2016 Published Online in Articles in Advance: January 18, 2017

https://doi.org/10.1287/isre.2016.0659

Copyright: © 2017 INFORMS

Abstract. We study the strategic benefits of mergers and acquisitions (M&As) when competing information technology vendors sell diferent generations of the same product with diferent quality. We assume the new product arrives unexpectedly when an installed base of the old product exists. We show that the combination of consumers’ purchase history and heterogeneity leads to new demand complexity that gives rise to innovative product strategies. We find that shelving the old product is an important motivation for M&A. The acquirer may exercise static or intertemporal price discrimination depending on whether it can exercise upgrade pricing. M&A may speed up or slow down new product consumption, and it can lead to delayed new product introduction in some markets. However, it always increases the acquirer’s profit and can sometimes help maximize social welfare. We discuss relevant managerial and policy implications.

History: Ram Gopal, Senior Editor; Xianjun Geng, Associate Editor. Funding: This research was supported in part by the National Science Foundation of China [Project 71371082] and the Hong Kong SAR General Research Fund [Project 142808]. Supplemental Material: The online appendix is available at https://doi.org/10.1287/isre.2016.0659.

Keywords: mergers and acquisitions • installed base • depreciation • price discrimination

## 1. Introduction

Mergers and acquisitions (M&As) are rife in information technology (IT) industries. The global M&A deals in the IT industry reached \$459.6 billion in 2015 (EY 2015). Many of these M&A deals involved new technologies or patents. For example, Oracle acquired Eloqua and Compendium in 2012–2013 to add new capabilities to its cloud-based online marketing platform. Microsoft acquired Skype in 2011 to expand its presence in the instant messenger and voice over Internet protocol market. It also acquired Fox Software for its celebrated FoxPro database package in the early 1990s. These M&As help the acquirers strengthen their product portfolios and expand their customer bases.

However, M&As can be costly. Oracle paid \$810 million to acquire Eloqua, a 31% premium over Eloqua’s prevailing trading price in the stock market, when Eloqua had yet to post a profit (Jones and Rubin 2012). Microsoft paid \$8.56 billion to acquire Skype when Skype was barely profitable and Microsoft itself already had a strong presence via its Windows Life Messenger in the instant messaging and video- and voice-chat markets (Bright 2011). These high-stakes M&A deals raise the following questions: In addition to acquiring new technologies or increasing market shares, do the acquirers obtain other strategic benefits from M&A? If so, what is the nature of these benefits? How do such M&As afect social welfare?

To analyze the strategic benefits of technology M&As, we need to identify its unique features. First, the acquirer will inherit the existing customers from the acquired firm. It has to plan for its future products and pricing in view of these customers’ preferences and the installed base of old products that they possess. People using Microsoft’s Windows Live Messenger may be less willing to pay for Skype calls, and people with FoxPro will have a lower need for Microsoft’s future database products.

Second, many IT products feature continuous upgrades with improved functionality or quality. Hence, consumers may prefer diferent product generations at diferent times and may buy multiple generations of the same product over time (Dogan et al. 2011, Goettler and Gordon 2011, Mehra et al. 2012). Consumers who have more urgent needs for online marketing solutions may be willing to purchase Eloqua’s services and subsequently upgrade to use Oracle’s platform solutions. Other consumers may wait and use Oracle’s integrated platform solutions at a later time.

Third, there is economic obsolescence, meaning the product will “expire” after a certain period of time, perhaps because of discontinuation of support services or retirement or obsolescence of the complementary platform needed for product consumption (Lee and Lee 1998). For example, it may no longer be safe to use

Windows XP because of unknown security vulnerabilities after Microsoft discontinued its support in 2014. An Apple iPhone may stop functioning after its battery dies in a few years.

These characteristics imply despite that a vendor can evade competition by acquiring a rival firm, it will face other challenges such as cannibalization and product obsolescence. Although the existing literature has variously analyzed related problems, it lacks specific consideration for the IT industry—limited product life span due to economic obsolescence, negligible marginal costs, the coexistence of multiple product generations, and, most importantly, the rapid pace of research and development (R&D) from diferent parties leading to innovative solutions that are often unanticipated by incumbent vendors and that spawn new opportunities for M&A. In particular, because of overlapping product generations, a vendor selling a new product often faces a partially covered market, i.e., only some but not all consumers own the old product. This incomplete coverage allows vendors to sell old and new products to diferent consumers at diferent times, leading to many possibilities of static and intertemporal price discrimination. In such a setting, M&A may bring new benefits that have not been well explicated in the prior literature.

In this study, we analyze the strategic options available to an acquirer after M&A and evaluate whether it brings benefits to consumers and social welfare. We start by analyzing a benchmark competition model where two vendors compete to sell two generations of a product with difering quality. The incumbent sells a low-quality “old” product followed by an entrant selling a high-quality “new” product. The vendors separately decide whether, when, and for how much to sell their products. We then compare the outcome of this benchmark with another similar setting where the vendors can form a coalition through M&A. As is customary with most analyses of IT products, we assume zero marginal costs (Choudhary 2010, Xu et al. 2011) and constant product quality in the products’ life span (Lee and Lee 1998). Our consumers stay in the market throughout the game. Hence, we extend the vendors’ planning horizon to examine how they can dynamically sell their products.

Our model explicitly accommodates an interesting demand dynamic—the service delivered by the old product tends to make buying the new product less imminent for existing customers. As the old product depreciates over time, however, these existing customers may have a higher willingness to pay for the new product than new consumers. Together with the presence of new consumers, the vendors face an aggregate demand structure that is highly dynamic and heterogeneous.

We find that in the competitive market, the incumbent will sell the old product to consumers who have not bought it, but the entrant will target consumers who place a higher valuation on quality despite they already owning the old product. M&A helps alleviate competition and will often lead to shelving of the old product. More importantly, it can lead to several interesting product consumption patterns. In some markets, low-type consumers will prefer the new product more than high-type consumers in the early periods, but their preferences will reverse in the latter periods. This unique and dynamic preference structure presents an opportunity for the acquirer to exercise perfect intertemporal price discrimination to extract all consumer surplus.

Furthermore, M&A may variously speed up or slow down new product consumption. It can even cause the new product to be introduced later despite it depreciating over time. Such delayed new product introduction does not benefit consumers. Nevertheless, we find that M&A can increase and sometimes even maximize social welfare, which will never happen in the competitive market. M&A is also economically attractive as the acquirer will mostly earn a higher profit than the vendors’ combined profits in the competitive market. Allowing the acquirer to identify existing consumers and ofer upgrade pricing will further strengthen the incentive for the merger.

In addition to M&As, our theory applies to more general settings with an installed base of old products. Examples include changes in internal management (new management inheriting an installed base from predecessors) or the exit of prominent competitors in a concentrated market (the remaining vendors then have to face an installed base created by the exited competitors).<sup>1</sup> The common feature of these examples is that the vendors face an exogenous pool of existing customers and have to make long-term product and pricing plans. Similarly, our findings help policy makers assess the long-term efects of M&A in the IT industry, particularly its implications on product upgrade, replacement and general consumption profiles, and social welfare.

The remainder of this paper is organized as follows. Section 2 reviews the related literature. Section 3 presents our research model and characterizes the demand dynamics. Section 4 reports the analysis and findings. Section 5 discusses the implications of this research. Section 6 concludes this paper.

## 2. Related Literature

This paper is related to several streams of research in the literature. The first stream studies how consumer heterogeneity afects dynamic pricing of products (Bergemann and Välimäki 2006, Su 2007, Chen and

Pearcy 2010, Liu 2010, Liu and Zhang 2013). In general, heterogeneity in quality valuation, taste, patience, or purchase history, or strategic consumer behavior, afects consumers’ product preferences, leading to various strategies such as markup (increasing), markdown (skimming), or penetration pricing. The focus of these works lies mainly in designing the optimal pricing strategies given specific market structures or demand characteristics, but not comparing the firms’ strategies across market structures (e.g., monopoly versus duopoly).

Another closely related stream of work studies versioning of software or information products (Chen and Seshadri 2007, Bhargava and Choudhary 2008, Boulding and Christen 2009, Choudhary 2010, Dogan et al. 2011, Calzada and Valletti 2012). The general conclusion in this literature is that the utility specification of consumers, production costs, and demand variability and other market risks may afect firms’ versioning decisions (see, e.g., Koca et al. 2010, Mehra et al. 2012). The focus of these works lies in identifying the necessary and/or suficient conditions for product versioning, but not whether firms have incentives to ease multiproduct competition or facilitate new product introduction through structural changes such as M&A.

Our research does not focus on product pricing or versioning per se. Instead, we study the vendors’ strategies when they can variously compete or form a coalition. Our model adopts some commonly used market characteristics—vertically diferentiated products, overlapping product generations, competition, and the possibility to ofer upgrade pricing (Li and Graves 2012, Mehra et al. 2012, Liu and Zhang 2013), but we want to identify and characterize additional product line and pricing strategies available to a coalition. Our setting is related to the one in Goettler and Gordon (2011), which compares innovation rates and social welfare between a monopoly and a duopoly in the microprocessor industry. Unlike Goettler and Gordon (2011), our vendors and consumers are partially strategic—they are forward looking and so can plan ahead only for the existing product (i.e., the one already launched in the market). As we shall see in Section 4, this introduces new complexity that gives rise to many novel results.

Our theoretical foundation is the celebrated literature of price discrimination (Mussa and Rosen 1978, Stokey 1979, Moorthy 1984), durable goods pricing (Coase 1972; Bulow 1982, 1986; Waldman 2003), and time inconsistency (Stokey 1981, Fudenberg and Tirole 1998, Lee and Lee 1998). A common feature in these theories is that the market is often incompletely covered within the product life cycle, which sets the stage for our analysis (for a formal analysis, see Besanko and Winston 1990, Nair 2007). From there, we extend the model to allow for dynamic pricing of the new product and M&A in the presence of an installed base of old products.

Finally, our work is related to the literature in horizontal mergers and technological acquisitions. Studies in horizontal mergers mostly analyze the benefit of a merger in Cournot or Bertrand price-setting games (Deneckere and Davidson 1985, Perry and Porter 1985) or in the presence of market expansion or competition efects (Shaked and Sutton 1990). Our study departs from this literature in that the incentive to merge stems not only from being able to raise prices or expand market potential but also the possibility to manage a broader product portfolio taking into consideration the strategic dynamics of market demand (Banker et al. 2011).

The technological acquisition literature studies how technology innovation afects a firm’s preacquisition decisions (Zhao 2009, Ransbotham and Mitra 2010) and postacquisition management (Puranam et al. 2006, Kapoor and Lim 2007, Sears and Hoetker 2014). A recurring interest has been to relate technology similarity and the gap in knowledge bases between the acquiring and target firms with acquisition performance. The empirical evidence indicates that redundancy in technology will afect the performance of the acquirer in the market (Ahuja and Katila 2001, Makri et al. 2010, Sears and Hoetker 2014). Our study builds on this literature by assuming the acquirer and target firms sell diferent generations of the same product. Hence, the products overlap in the quality space. We add analytical insights to the empirical literature (Puranam et al. 2006, Kapoor and Lim 2007, Sears and Hoetker 2014) by scrutinizing novel ways to improve acquisition performance in view of overlapping technology generations. Furthermore, we extend this literature by considering whether market characteristics such as consumer heterogeneity or mix would afect acquisition performance.

## 3. The Model

An incumbent vendor (I) sells an old product (O), which delivers a constant quality, $q _ { O } ,$ in each of the n periods in its life span, $\hat { n } \geq 3 . ^ { 2 }$ The product’s life span is fixed from the day when it is developed. It will stop functioning after n periods regardless of when consumers make the purchase. If a consumer buys the product in period t, then she can use it for only $n - t$ instead of n periods. Let $U ( \cdot , \cdot )$ denote the sum of discounted quality (utility) provided by the product. The first argument in $U ( \cdot , \cdot )$ is the product’s quality. The second argument is the product’s remaining life span. For simplicity, we assume zero fixed and marginal costs of production.<sup>3</sup>

The market consists of $d _ { H }$ high-type (H) and $d _ { L }$ lowtype (L) consumers, who difer in their valuations for quality, $v _ { H } > v _ { L } ,$ , and $d _ { H } + d _ { L } = 1$ . The vendor can sell the product in any period $t = 0 , 1 , \ldots , n - 1$ , but it cannot make product or price commitments, or identify individual consumers $( \mathrm { i . e . , }$ perfect price discrimination is infeasible). The vendor and consumers discount future utility by δ, where $0 < \delta < 1$ . Therefore, a product with quality $q _ { i }$ and durability n gives $U ( q _ { i } , n ) = q _ { i } + \delta q _ { i } +$ $\therefore + \dot { \delta ^ { n - 1 } } q _ { i } = q _ { i } ( 1 - \delta ^ { n } ) / ( \dot { 1 } - \delta )$

Consider the vendor’s decision. If it wants to sell the product to all consumers in period $0 ,$ it has to charge a penetration price equal to low-type consumers’ utility, $v _ { L } U ( q _ { O } , n )$ , which is also its profit because the market size is 1. It will not be able to sell any product in the future as all consumers will buy the product and leave the market.

The vendor can also exercise intertemporal price discrimination by selling to high-type consumers first followed by selling to low-type consumers at a lower price (Besanko and Winston 1990, Nair 2007). Suppose high-type consumers buy the product in period 0. Then, immediately in period 1, the vendor can sell the product to low-type consumers at price $p _ { 1 } =$ $v _ { L } U ( q _ { O } , n \mathrm { ~ - ~ } 1 )$ . High-type consumers foresee this. Therefore, to incentivize them to buy the product in period 0, the vendor must ensure they obtain higher utility from buying in period 0 than buying in period 1, $\mathrm { i . e . , } v _ { H } U ( q _ { O } , n ) \stackrel { - } { - } p _ { 0 } \stackrel { - } { \geq } \delta [ v _ { H } U ( q _ { O } , n - \bar { 1 } ) - p _ { 1 } ]$ which implies $p _ { 0 } = v _ { H } U ( q _ { O } , 1 ) + \delta v _ { L } U ( q _ { O } , n - 1 )$ . Summing over periods 0 and $^ { 1 , }$ the vendor’s profit from intertemporal price discrimination is $d _ { H } p _ { 0 }$ + $d _ { L } \delta p _ { 1 } = d _ { H } \big [ v _ { H } \hat { U } ( q _ { O } , 1 ) + \delta v _ { L } U ( q _ { O } , n - 1 ) \big ] + d _ { L } \big [ \delta v _ { L } \dot { U } ( q _ { O } ,$ $n - 1 ) ] = d _ { H } v _ { H } U ( q _ { O } , 1 ) + \delta v _ { L } U ( q _ { O } , n - 1 )$ , which exceeds its profit from penetration pricing, $v _ { L } U ( q _ { O } , n )$ , if and only if $d _ { H } v _ { L } ^ { H } > \hat { 1 }$ , where $v _ { L } ^ { H } \overset { - } { \equiv } v _ { H } / \overset { - } { v _ { L } } > \overset { - } { 1 }$ measures consumer heterogeneity (Moorthy and Png 1992).

Accordingly, when consumers are suficiently heterogeneous, and with a suficient number of high-type consumers, the vendor will prefer selling only to hightype consumers first and defer selling to low-type consumers to the next period. In the remaining analysis, we assume these conditions are satisfied.

Assumption 1. $d _ { H } v _ { L } ^ { H } > 1$

Assumption 1 implies that monopoly matters, as the vendor has an incentive to restrict output and not sell to low-type consumers (Lee and Lee 1998). When this happens, an installed base of the old product will form after period 0. Nair (2007) and Liu (2010) show that video-game sellers exercise price skimming, leading to incomplete coverage of the market before they reduce their products’ prices. Such incomplete coverage is commonly observed in other digital product markets, such as computer software, e-books and electronic media, and entertainment, which often comprise consumers with heterogeneous valuations and vendors with monopolistic pricing power.

## 3.1. Game Sequence

By Assumption 1, all high-type consumers will buy the old product in period 0. Suppose in period 1 an entrant (E) enters the market with a new product (N), which has a higher quality than the old product but the same durability, $n . ^ { \hat { 4 } }$ Let $0 < q _ { O } < q _ { N } = 1$ . The term $q _ { O }$ then inversely measures the extent of quality improvement. We further assume rapid technological development (Dhebar 1994, Kornish 2001).

Assumption 2. The technology improves in present value, $i . e . , \delta q _ { N } > q _ { O }$

Assumption 2 gives the entrant a stronger incentive to sell the new product earlier and removes the less interesting case where it waits until the incumbent sells to all consumers before launching the new product.<sup>5</sup> We assume the production of the old and new products are restricted by exclusive patents. Hence, only the incumbent can sell the old product and the entrant can sell the new product. The only way for either vendor to sell both products is to acquire the other party.

Starting from period 1, the incumbent and entrant need to decide when to sell their products and how much to charge in any period $t = 1 , 2 , \dots , n$ . Consumers do not buy the same product over time, but they can buy the old product and new product sequentially if doing so gives them higher utility. There is no secondhand market, meaning the old product is retired and provides zero usage or residual value once a consumer buys the new product. Figure 1 presents the event timeline.

We assume the incumbent and consumers do not anticipate the new product in period 0. This happens when they are myopic or the new product embodies unexpected new technologies. As argued by Banker et al. (2011, p. 2), “incumbent players are often blindsided by entrants who introduce products to occupy the incumbents’ blind spot because the former fail to anticipate all possible threats.”

Assumption 3. The incumbent and consumers do not anticipate the new product.

By Assumptions 1–3, high-type consumers will buy the old product in period 0. From period 1 onward, the incumbent can sell the old product to low-type consumers. The entrant can sell the new product to high- and/or low-type consumers. We apply the subgame-perfect Bertrand–Nash equilibrium concept in all analysis.

## 3.2. Demand Characteristics

We first characterize the consumers’ preferences for the new product. If consumer j does not own the old product, her utility from the new product in period $t ,$ $t \ge 1 , \mathrm { i s } b _ { N t } ^ { j } = v _ { j } U ( q _ { N } , n - t + 1 )$ . The corresponding discounted utility is $B _ { N t } ^ { j } = \delta ^ { t - 1 } b _ { N t } ^ { j }$ . If consumer $j$ owns the old product, which has a remaining life span of $n - t$ in period $t ,$ then her utility from upgrading to the new product in period t is $h _ { N t } ^ { j } = v _ { j } U ( q _ { N } , n - \bar { t } + 1 ) -$ $v _ { j } U ( q _ { O } , n - t )$ . The first term in $h _ { N t } ^ { j }$ is the utility she obtains from the new product. The second term is the remaining consumption value of the old product given that it has been used for t periods. The corresponding discounted utility is $H _ { N t } ^ { j } \stackrel { \textstyle \cdot } { = } \delta ^ { t - 1 } h _ { N t } ^ { j } \le B _ { N t } ^ { j } ;$ i.e., having the old product decreases consumer j’s desire to get the new product.

Figure 1. Event Timeline  
![](/api/attachments/HGU3A9TC/fulltext/images/8bb206716c6d19997f99e118bc49500d5d87feaf505372ff5edd562ed365b4ec.jpg)

Therefore, if consumer j does not own the old product, then $h _ { N t } ^ { j } = b _ { N t } ^ { j }$ and $H _ { N t } ^ { j } = B _ { N t } ^ { j }$ . As t increases, $\bar { b } _ { N , t + 1 } ^ { j }$ $< b _ { N t } ^ { j }$ and $B _ { N , t + 1 } ^ { j } < B _ { N t } ^ { j } ;$ i.e., she obtains a higher utility from an earlier purchase. We can quantify her marginal utility of waiting, $\Delta B _ { t } ^ { j } = B _ { N , t + 1 } ^ { j } - B _ { N t } ^ { j } = - \delta ^ { t - 1 } v _ { j } q _ { N } < 0 .$ By contrast, if she owns the old product, her marginal utility of waiting is $\Delta H _ { t } ^ { j } = \dot { H _ { N , t + 1 } ^ { j } } - \dot { H _ { N t } ^ { j } } = \delta ^ { t - 1 } \dot { v _ { j } ( q _ { O } - q _ { N } ) }$ $< 0 ,$ but $\Delta H _ { t } ^ { j } > \Delta B _ { t } ^ { j }$ . Hence, she sufers less from waiting than those who do not own the old product. This is because the old product ofers a consumption benefit before she upgrades to the new product.

By Assumption 1, only high-type consumers own the old product upon entering period 1. They are less willing to buy the new product than low-type consumers in a certain period t if and only if $\begin{array} { r } { \dot { h } _ { N t } ^ { \dot { H } } \le b _ { N t } ^ { L } , } \end{array}$ or $v _ { L } ^ { H } \leq \Upsilon ( t ) \equiv U ( \dot { q } _ { N } , n - t + 1 ) / ( U ( q _ { N } , n - t + 1 ) ^ { \ast * } -$ ${ U ( q _ { O } , n - t ) ) }$ . They are more willing to buy the new product than low-type consumers in period $i + 1$ if and only if $h _ { N , t + 1 } ^ { H } \geq b _ { N , t + 1 } ^ { L ^ { \sim } } , \mathrm { o r } v _ { L } ^ { H } \geq \Upsilon ( t + \mathbf { \dot { \tau } } ) \equiv U ( q _ { N } , n - t ) / $ $( U ( q _ { N } , n - t ) - U ( q _ { O } , n - t - 1 ) )$ , where $\Upsilon ( t + 1 ) < \Upsilon ( t )$ for all t. Proposition 1 summarizes this intricate demand dynamics. All proofs are available in the appendix.

Proposition 1. Suppose only high-type consumers own the old product upon entering period 1. For any $n \geq 3 ,$ , there exist $v _ { L } ^ { H }$ and $\hat { t } < \dot { n , } \Upsilon ( \hat { t } + 1 ) \overset { \smile } { \leq } \dot { v } _ { I } ^ { H } \leq \Upsilon ( \hat { t } )$ , such that $h _ { N t } ^ { H } \leq b _ { N t } ^ { L } f o r$ all $t \leq \widehat { t }$ and $h _ { N t } ^ { H } \geq b _ { N t } ^ { L }$ for all $t \geq \widehat { t } + 1$

Figure 2. Consumer Preferences Over Time  
![](/api/attachments/HGU3A9TC/fulltext/images/93bc2867baf0ae412952fe5251764a4b9eba772122036215b8cbe48453b1ee39.jpg)

Figure 2 plots the preferences of consumers with diferent heterogeneity over time when $n = 2 0 , \ q _ { O } =$ $0 . 8 ,$ and $\delta = 0 . 9 5$ . Proposition 1 results from the interaction between consumer heterogeneity and purchase history. The installed base of the old product decreases high-type consumers’ willingness to buy the new product, but it depreciates over time. Hence, as t increases, the new product gradually becomes more attractive to high-type consumers (compared with lowtype consumers who do not own the old product). This dynamic change in relative consumer preferences increases the complexity of intertemporal pricing.

In particular, when consumer heterogeneity is moderate, viz., $\Upsilon ( t + 1 ) \leq v _ { I } ^ { H } \leq \Upsilon ( t )$ , the preferences of the two consumer types “cross” from period t to period $t + 1$ . To our knowledge, such preference “crossing” among consumers has not been considered in the prior literature. It happens when consumers have diferent purchase histories and the product is subject to depreciation or economic obsolescence (Lee and Lee 1998). These features are common among multigeneration IT products.

## 4. Analysis

## 4.1. Competition

The demand dynamics characterized above pose great challenges to both the incumbent and entrant. The incumbent wants to sell the old product to low-type consumers, but it has to compete with the entrant who sells a new and better product. The entrant, in addition to competing with the incumbent, has to tackle the installed base of the old product if it wants to sell the new product to high-type consumers. In this section, we characterize the equilibrium outcomes when the incumbent and entrant compete with each other independently to maximize their profits.

In general, three forces suppress the new product’s price. First, the incumbent can always charge a low price for the old product. This competition from the incumbent limits the price that the entrant can charge to low-type consumers. To sell to low-type consumers, the new product’s price cannot exceed the incremental utility brought by technological improvement, i.e., $p _ { t } ^ { N } \leq v _ { L } [ \mathcal { U } ( q _ { N } , \stackrel { \sim } { n } - t + 1 ) - U ( q _ { O } , n - t ) ]$

Second, the installed base of the old product cannibalizes the new product. To sell to high-type consumers, the new product’s price cannot exceed the incremental utility brought by the new product relative to the remaining consumption value of the old product, i.e., $p _ { t } ^ { N } \leq v _ { H } [ \bar { U } ( q _ { N } , n - \hat { t } + 1 ) - U ( q _ { O } , n - t ) ]$

Third, because the entrant cannot make a price commitment, it sufers from time inconsistency; i.e., its incentive to reduce price in the future limits the price that it can charge in the current period (Stokey 1981, Fishman and Rob 2000). Consumers, expecting price reduction, are willing to pay only the time-discounted price in the future plus the utility obtained from using the new product in the current period. The cannibalization from the old product further dampens the expected future price of the new product.

The competition makes selling to low-type consumers in period 1 unattractive to the entrant. Instead, the entrant will be better of selling to high-type consumers first. Even then, the price that it can charge will be suppressed because of cannibalization and time inconsistency. Furthermore, the new product’s price in period 2 is constrained by cannibalization, as, by then, the incumbent would have sold the old product to lowtype consumers. Accordingly, all consumers will enjoy a positive surplus. Proposition 2 summarizes the equilibrium outcomes under competition. For brevity, we report the equilibrium prices and profits in the online appendix.

Proposition 2. Under competition, the incumbent will sell the old product to low-type consumers in period 1. The entrant will sell the new product sequentially to high- and low-type consumers in periods 1 and 2. All consumers earn a positive surplus.

Despite that the incumbent can sell the old product to low-type consumers in period 1, the price that it can charge is adversely afected by the new product; i.e., it sufers from the entrant’s competition. The incumbent can charge a high price for the old product if and only if consumers are suficiently heterogeneous. Even then, it can only extract low-type consumers’ surplus from using the old product in period 1 instead of the old product’s full life span because low-type consumers expect to buy the new product in period 2. Similarly, because of cannibalization and time inconsistency, the entrant will always price the new product such that all consumers enjoy a positive surplus.

Proposition 2 gives two interesting insights. First, the entrant will serve high-type consumers first even if they have a lower preference for the new product than low-type consumers because they already have the old product. By not serving low-type consumers immediately, the entrant can avoid competing with the incumbent in period 1. Deferring selling to lowtype consumers also allows the entrant to charge a higher price in period 2, as by then the old product will be worth less because of depreciation. This eases the old product’s cannibalization of the new product. Essentially, Proposition 2 implies that when the market is partly covered by an old product, an unforeseen new entrant will serve consumers with the new product sequentially, according to consumers’ valuation of quality, regardless of their relative preferences for the new product.<sup>6</sup>

Second, although the entrant will sell the new product immediately in period 1, it will deliberately price it so that low-type consumers will defer purchasing it until period 2. The market will not be eficient, as the new product will depreciate despite that it is not sold to low-type consumers (whose valuation exceeds its marginal cost, zero). This ineficiency arises from the entrant’s excessive incentive to avoid competition and the cannibalization from the installed base of the old product.

## 4.2. The Benefits of M&A

The analysis above suggests that competition, cannibalization, and time inconsistency limit the profit that the entrant can earn from the new product. It is dificult to alleviate time inconsistency without price commitment, but the competition and cannibalization efects can be reduced if the two vendors can coordinate through a merger. In particular, price competition will not arise with M&A, and the merged vendor (“acquirer”) can optimally plan for the entire product line to minimize cannibalization.

In Section 4.2.1, we start by assuming the acquirer cannot ofer an upgrade policy. This happens when the acquirer cannot determine whether consumers have bought the old product, or when the administration of upgrade is prohibitively costly. We present the case with an upgrade policy in Section 4.2.2.

4.2.1. No Upgrade Policy. Here, the acquirer can charge only one price for each of its products to all consumers. Proposition 2 establishes the “benchmark” competition outcome. With M&A, the acquirer’s strategy space is broader because it can sell the old product to low-type consumers and the new product to high- or low-type consumers in any period $t = 1 , 2 , \dots , n$ . Let $\Upsilon _ { 1 } \equiv \hat { U } ( q _ { N } , 1 ) / ( U ( q _ { N } , 1 ) - \hat { U } ( \hat { q } _ { O } , 1 ) ) .$ $\Upsilon _ { 2 } \equiv U ( q _ { N } , n ) / ( U ( q _ { N } , n ) - U ( q _ { O } , n - 1 ) ) ,$ and $\Upsilon _ { 3 } \equiv$ $U ( q _ { N } , n - 1 ) / ( U ( q _ { N } , n - 1 ) - U ( q _ { O } , n - 2 ) ) , \Upsilon _ { 1 } > \Upsilon _ { 2 } > \Upsilon _ { 3 } .$ The following proposition summarizes the equilibrium outcomes in this scenario.

Proposition 3. With M&A and no upgrade policy, the acquirer will

(i) sell the new product to low-type consumers in period 1 and high-type consumers in period 2, i.e., $\{ 1 \colon \dot { N }  L ;$ $2 \colon N  H \}$ , if and only if

$$
\begin{array}{c} v _ {L} ^ {H} <   d _ {L} \Upsilon_ {1}, \quad o r \\ \Upsilon_ {3} <   v _ {L} ^ {H} <   \Upsilon_ {2} \cdot \left(1 + \frac {1 - d _ {L}}{d _ {L}} \cdot \frac {U (q _ {N} , 1) - U (q _ {O} , 1)}{U (q _ {N} , n) - U (q _ {O} , n - 1)}\right) ^ {- 1}, \\ w h e r e d _ {L} \Upsilon_ {1} \leq \Upsilon_ {3}; \end{array}
$$

(ii) sell the new product to both high- and low-type consumers in period $1 , i . e . , \{ 1 { : } N  H , \bar { L } \}$ , if and only if

$$
\begin{array}{c} d _ {L} \Upsilon_ {1} \leq v _ {L} ^ {H} \leq \Upsilon_ {3}, \quad o r \\ \Upsilon_ {2} \cdot \left(1 + \frac {1 - d _ {L}}{d _ {L}} \cdot \frac {U (q _ {N} , 1) - U (q _ {O} , 1)}{U (q _ {N} , n) - U (q _ {O} , n - 1)}\right) ^ {- 1} \leq v _ {L} ^ {H} \leq \Upsilon_ {1}, \end{array}
$$

where

$$
\Upsilon_ {3} <   \Upsilon_ {2} \cdot \left(1 + \frac {1 - d _ {L}}{d _ {L}} \cdot \frac {U (q _ {N} , 1) - U (q _ {O} , 1)}{U (q _ {N} , n) - U (q _ {O} , n - 1)}\right) ^ {- 1},
$$

or, when $v _ { L } ^ { H } > \Upsilon _ { 1 }$

$$
\begin{array}{r l} & v _ {L} ^ {H} \leq \min \biggl \{\frac {\Upsilon_ {1}}{1 - d _ {L}}, \Upsilon_ {1} + \frac {d _ {L}}{1 - d _ {L}} \\ & \qquad + \frac {\delta U (q _ {O} , n - 2)}{(1 - d _ {L}) [ U (q _ {N} , 1) - U (q _ {O} , 1) ]} \biggr \}, \quad a n d \\ & v _ {L} ^ {H} \leq \frac {U (q _ {N} , 2) - d _ {L} U (q _ {O} , 2)}{\delta (1 - d _ {L}) [ U (q _ {N} , 1) - U (q _ {O} , 1) ]}, \quad w h e n n = 3; \end{array}
$$

(iii) sell the new product to high-type consumers in period 1 and low-type consumers in period $2 , i . e . , \{ 1 { : } N \stackrel { \cdot } { \to } H ;$ 2: $N  L \}$ , if and only if

$$
\begin{array}{l} d _ {L} <   \frac {\delta U (q _ {O} , n - 2)}{U (q _ {O} , 1)} \quad a n d \quad v _ {L} ^ {H} > \frac {\Upsilon_ {1}}{1 - d _ {L}}, \\ a n d \\ v _ {L} ^ {H} \geq \frac {d _ {L} U (q _ {O} , 2) - \delta U (q _ {N} , 1)}{(1 - \delta) (1 - d _ {L}) [ U (q _ {N} , 1) - U (q _ {O} , 1) ]}, \quad w h e n n = 3; \end{array}
$$

(iv) sell the old product to low-type consumers in period 1, and the new product to high- and low-type consumers in periods 2 and 3, i.e., $\{ \breve { 1 } \colon O \to L ; \ \overleftarrow { 2 \colon } N \to H ;$ 3: $N  \dot { L } \dot  \}$ , if and only if

$$
n = 3, \quad v _ {L} ^ {H} > \Upsilon_ {1}, \quad \max \left\{\frac {1}{(1 + \delta) q _ {O}}, \frac {1}{q _ {O}} - \delta^ {2} \right\} <   d _ {L} <   1,
$$

and

$$
\begin{array}{c} \frac {U (q _ {N} , 2) - d _ {L} U (q _ {O} , 2)}{\delta (1 - d _ {L}) [ U (q _ {N} , 1) - U (q _ {O} , 1) ]} \\ <   v _ {L} ^ {H} <   \min \biggl \{\frac {d _ {L} U (q _ {O} , 2) - \delta U (q _ {N} , 1)}{(1 - \delta) (1 - d _ {L}) [ U (q _ {N} , 1) - U (q _ {O} , 1) ]}, \\ \frac {\delta (1 + d _ {L}) U (q _ {O} , 1) - \delta U (q _ {N} , 1)}{(1 - \delta) (1 - d _ {L}) [ U (q _ {N} , 1) - U (q _ {O} , 1) ]} \biggr \}; \quad a n d \end{array}
$$

(v) sell the old product to low-type consumers and the new product to high-type consumers in period 1, and the new product to low-type consumers in period $2 , i . e . , \{ 1 \colon N  H , $ $\stackrel { \cdot } { O }  L ; 2 \colon N  \stackrel { \cdot } { L } \}$ , if and only if

$$
\begin{array}{c} d _ {L} \geq \frac {\delta U (q _ {O} , n - 2)}{U (q _ {O} , 1)}, \\ v _ {L} ^ {H} > \Upsilon_ {1} + \frac {d _ {L}}{1 - d _ {L}} + \frac {\delta U (q _ {O} , n - 2)}{(1 - d _ {L}) [ U (q _ {N} , 1) - U (q _ {O} , 1) ]}, \quad a n d \\ v _ {L} ^ {H} \geq \frac {\delta (1 + d _ {L}) U (q _ {O} , 1) - \delta U (q _ {N} , 1)}{(1 - \delta) (1 - d _ {L}) [ U (q _ {N} , 1) - U (q _ {O} , 1) ]}, \quad w h e n n = 3. \end{array}
$$

Figure 3 illustrates the outcomes with M&A and no upgrade policy when $n = 3 , q _ { O } = 0 . 8 ,$ , and $\delta = 0 . 9 5$ . We

Figure 3. Equilibrium Outcomes with M&A and No Upgrade Policy

Log(v<sub>L</sub><sup>H</sup>)

![](/api/attachments/HGU3A9TC/fulltext/images/7db946078ecd4cd616826293fcbfa5713ba67e4dfc80bb4f191a82219779d0f4.jpg)

plot Figure 3 in log scale to show all optimal strategies. Evidently, the outcomes here are often diferent from the case with competition (Proposition 2). As shown in Proposition 3(v), the product sequence under competition, i.e., $\{ 1 { : } N \to H , { \overset { } { O } } \to L ; 2 { : } \hat { N } \to L \}$ , is optimal only if consumers are heterogeneous, i.e., $v _ { L } ^ { H }$ is large, and there are many low-type consumers, i.e., $d _ { L }$ is large.

One interesting observation from parts (i) to (iii) of Proposition 3 and Figure 3 is that the acquirer may prefer shelving the old product. When consumers are homogeneous, selling the old product will severely constrain the price chargeable for the new product. This is not desirable to the acquirer because consumers value the new product more than the old product. The M&A can alleviate this cannibalization by discontinuing the old product. When this happens, ironically, the acquirer obtains the exclusive patent to retire instead of selling a product. The M&A serves a strategic but not market expansion purpose (cf. Shaked and Sutton 1990).<sup>7</sup>

Observation 1. The acquirer prefers to shelve the old product in all markets characterized in parts (i) to (iii) of Proposition 3.

Even if the acquirer shelves the old product, it still has several options to sell the new product. One intriguing option is to sell the new product to low-type consumers in period 1 and high-type consumers in period 2. Importantly, this strategy helps the acquirer achieve perfect intertemporal price discrimination in some markets.

Observation 2. When

$$
\Upsilon_ {3} <   v _ {L} ^ {H} <   \frac {\Upsilon_ {2}}{1 + \frac {1 - d _ {L}}{d _ {L}} \cdot \frac {U (q _ {N} , 1) - U (q _ {O} , 1)}{U (q _ {N} , n) - U (q _ {O} , n - 1)}},
$$

the acquirer can extract all consumer surplus by selling the new product to low-type consumers in period 1 and high-type consumers in period 2.

The shaded area in Figure 3 highlights the markets corresponding to Observation 2, which results from the demand dynamics characterized in Proposition 1. Because high-type consumers own the old product, their marginal utility of waiting is higher than that of low-type consumers. Hence, low-type consumers value the new product more than high-type consumers in period 1, causing the acquirer to serve them first.

Nevertheless, high-type consumers value quality more than low-type consumers. Hence, as the old product depreciates, their valuation for the new product will gradually exceed that of low-type consumers. When $\begin{array} { r } { \Upsilon _ { 3 } < v _ { L } ^ { H } \le \Upsilon _ { 2 } , } \end{array}$ , corresponding to the consumer heterogeneity in Proposition 1, the valuations of the two consumer types toward the new product “cross” from period 1 to period 2. This allows the acquirer to fully exercise its pricing power despite not being able to target consumers individually. With proper prices, low-type consumers will buy the new product in period 1 because they will get a negative surplus if they wait. High-type consumers will wait until period 2 because their old product still gives high usage value in period 1. All consumers will get zero surplus.

Note that, in principle, such perfect intertemporal price discrimination is feasible for all $v _ { L } ^ { H } \in [ \Upsilon _ { 3 } ^ { \bullet } , \Upsilon _ { 2 } ]$ The acquirer will exercise it only under the condition specified in Observation 2 because, outside this range, the valuation of high-type consumers toward the new product is suficiently high so that the acquirer will prefer selling to them immediately. It is instructive to compare the product sequences in Observation 2 and Proposition 2. With competition, the entrant can never extract the full surplus from low-type consumers, so it prefers to serve high-type consumers first.

This powerful pricing mechanism results from the dynamic change in consumer valuation, not consumer identification instruments such as purchase history (Levinthal and Purohit 1989, Fudenberg and Tirole 1998, Lee and Lee 1998) or cross-market information sales (Taylor 2004, Hermalin and Katz 2006). To our knowledge, that a vendor can achieve perfect intertemporal price discrimination without identifying consumers is a novel result. It comes from the interaction of depreciation and heterogeneous consumer valuation, both of which are commonly observed in consumer durables or products subject to economic obsolescence, such as computer software.

Figure 3 shows that perfect intertemporal price discrimination is an optimal strategy in a small set of markets. The enabling characteristics are as follows: (i) consumers have moderate heterogeneity in quality valuation; (ii) those holding an old product have a higher valuation toward product quality; (iii) the product is subject to depreciation or economic obsolescence; (iv) the arrival of the new product is unexpected; and (v) the sales of the old and new products can be coordinated after the new product arrives, perhaps via a merger. With these characteristics, the existing consumers who own the old product will gradually value the new product more than other consumers over time, giving the monopoly vendor a chance to skim consumers sequentially.

Together with Proposition $^ { 2 , }$ we find an interesting diference in the vendors’ behaviors across competition and M&A. Under competition, a new-product vendor will sell to high-valuation consumers first despite that they might already own an old product. By contrast, a merger will sometimes sell to new consumers who have lower valuation for product quality first. Other than expanding clientele to build critical mass (Clemons and Weber 1996, Van de Ven 2005) or to cultivate network efects (Lee and Mendelson 2007, Jiang and Sarkar 2009, Liu et al. 2011), we show that exercising the price discrimination power granted by M&As can be a novel motivation.

Proposition 3 also highlights another interesting new strategy.

Observation 3. The acquirer will delay selling the new product in the markets characterized in Proposition 3(iv).

In general, when consumers are suficiently heterogeneous, the acquirer will want to sell the new product to high-type consumers at a high price. It may want to sell to low-type consumers too when they are prevalent in the market. However, the installed base of the old product limits the price chargeable to high-type consumers in period 1. The low valuation of low-type consumers also makes selling the new product to them in period 1 unattractive. One way to alleviate these pricing constraints is to postpone selling the new product. This would allow the installed base to depreciate further, so the acquirer can charge a higher price for the new product after period 1. The acquirer can sell the old product to low-type consumers in period 1 to make up for the “opportunity loss” from such deferred selling. This is more likely to happen when $d _ { L }$ increases.

Observation 3 provides a novel justification for a paradoxical strategy—delay selling a new and better product after M&A. Dhebar (1994), Fishman and Rob (2000), and Kornish (2001) have shown that such delays can help resolve time inconsistency. Here, the motivation is to alleviate cannibalization from an existing installed base that depreciates over time. Previous studies have not scrutinized this interesting motivation. We emphasize that Observation 3 applies despite that the new product improves in present value (Assumption 2) and the delay does not address time inconsistency.

The practical implication of Observation 3 is that when an existing installed base cannibalizes a new product, the vendor can delay selling the new product and in the meantime serve new consumers with the old product. This strategy is attractive when the old product has a short remaining life span and there are many new consumers.

Proposition 2 and Observation 3 also imply M&As can slow down the pace of new product introduction in some markets. This finding echoes the previous literature showing a monopoly may impede new product introduction (Fishman and Rob 2000, Kornish 2001). Our analysis adds another perspective to the continuing debate of whether competition afects product innovation (Grossman and Helpman 1991, Aghion et al. 2005). Other than market structure, the path of product purchase and the timing of structural change, such as a merger, also matter (Goettler and Gordon 2011).

From Propositions 2 and 3, we see that M&A may variously trigger diferent product sequences. With low consumer heterogeneity, they may speed up selling the new product to low-type consumers and lead to shelving of the old product. With high consumer heterogeneity, a large proportion of low-type consumers, and a short product life span, they may lead to delayed selling of the new product. Overall, after M&A, lowtype consumers can get the new product earlier in a large set of markets, whereas all consumers can get the new product later in a (disjoint) small set of markets.

We next consider how M&As afects social welfare. In our setting, as both products have zero marginal costs and life spans of $n ,$ and the new product has a higher quality than the old product, social welfare is maximized if and only if all consumers get the new product in period 1. This implies only the product sequence, <sup>{</sup>1: $N  H , L \}$ , can maximize social welfare. Obviously, it is often not the equilibrium choice.

Proposition 4. Social welfare is not maximized with competition. Without an upgrade policy, M&A will help maximize social welfare only in the markets characterized in Proposition 3(ii).

Upon entering the market in period 1, the entrant faces a price war from the incumbent and the cannibalization from the existing installed base, which tend to erode its profit from selling the new product (Goettler and Gordon 2011). To avoid competition, the entrant will target high-type consumers first. This causes inefficiency as low-type consumers also benefit from using the new product earlier. As shown in Proposition 2, low-type consumers will not get the new product in period 1 under competition.

With M&A, the acquirer can minimize the negative impacts caused by competition and the cannibalization between the two products. However, its incentive to maximize profits through intertemporal price discrimination remains. Hence, it will still prefer to disperse selling the new product in diferent time periods in many markets. As Proposition 4 and Figure 3 suggest, when consumers are heterogeneous and the market contains more high-type consumers, the acquirer often prefers to delay selling the new product to low-type consumers (Goettler and Gordon 2011).

To summarize, with the presence of an installed base, it is often dificult to maximize social welfare by coordinating the path of future product introduction and pricing. M&A may help but it is obviously not the solution in all markets.

4.2.2. With Upgrade Policy. We now suppose the acquirer can ofer an upgrade price to existing consumers, perhaps because the consumer record is part of the transferred assets in the M&A, or the vendor can identify their sold products in the market. Our setting with the upgrade policy is similar to that in Lee and Lee (1998) and the “semianonymous” case in Fudenberg and Tirole (1998). The essential features are that (1) consumers must have the old product to enjoy the upgrade price and (2) consumers with the old product can pretend to be nonpatrons and buy the new product afresh. To exercise upgrade pricing, the acquirer has to take an extra step to identify the existing installed base and ofer multiple prices for the same product. Hence, it applies to a more restricted set of M&As.

In our setting, only high-type consumers own the old product upon entering period 1. The upgrade policy allows them to reveal their purchase history if their incremental utility from the new product is lower than that of low-type consumers. The acquirer can then differentiate consumers and charge low-type consumers an even higher price if necessary. This will happen when consumers are homogeneous.

On the other hand, when consumers are suficiently heterogeneous, the new product will give a higher incremental utility to high-type consumers than to lowtype consumers. In this case, an upgrade policy will not afect high-type consumers. However, it allows the acquirer to credibly charge a high price for the new product if consumers cannot present the old product. Hence, it encourages low-type consumers to buy the old product to qualify for the new product’s upgrade price in the future. The next proposition summarizes the outcomes in M&As with an upgrade policy.

Proposition 5. With M&A and an upgrade policy, the acquirer will

(i) sell the new product to both high- and low-type consumers in period $\dot { \iota , } i . e . , \left\{ 1 : N \to H , \breve { L } \right\}$ , if and only if

$$
\begin{array}{c} v _ {L} ^ {H} \leq \Upsilon_ {2} \quad o r \\ \Upsilon_ {2} <   v _ {L} ^ {H} \leq \min \biggl \{\frac {\Upsilon_ {1}}{1 - d _ {L}}, \Upsilon_ {1} + \frac {d _ {L}}{1 - d _ {L}} + \frac {\delta U (q _ {O} , n - 2)}{U (q _ {N} , 1) - U (q _ {O} , 1)} \biggr \}; \end{array}
$$

(ii) sell the new product to high-type consumers in period 1 and low-type consumers in period $2 , i . e . , \{ 1 { : } N \to H ;$ $2 \colon N  L \}$ , if and only if

$$
\begin{array}{c} v _ {L} ^ {H} > \Upsilon_ {2}, \qquad v _ {L} ^ {H} > \frac {\Upsilon_ {1}}{1 - d _ {L}}, \quad a n d \\ d _ {L} <   \frac {\delta U (q _ {O} , n - 2)}{U (q _ {O} , n - 1)}; \quad a n d \end{array}
$$

(iii) sell the old product to low-type consumers and new product to high-type consumers in period 1, and the new product to low-type consumers in period 2, i.e., $\{ 1 \colon N \to H$ $O  L ; 2 \colon N  \bar { L } \}$ , if and only if

$$
v _ {L} ^ {H} > \Upsilon_ {2}, v _ {L} ^ {H} > \Upsilon_ {1} + \frac {d _ {L}}{1 - d _ {L}} + \frac {\delta U (q _ {O} , n - 2)}{U (q _ {N} , 1) - U (q _ {O} , 1)},
$$

Figure 4. Equilibrium Outcomes with M&A and an Upgrade Policy  
![](/api/attachments/HGU3A9TC/fulltext/images/2c5397b20c93689d8f445cb520345b9c8e15ae47677b8a2c62c9b02cd8fb906c.jpg)

and

$$
d _ {L} \geq \frac {\delta U (q _ {O} , n - 2)}{U (q _ {O} , n - 1)}.
$$

Figure 4 illustrates the outcomes with M&A and an upgrade policy using the same parameters and scale as Figure 3. Analogous to Observation 1, the acquirer will shelve the old product when consumers are homogeneous. In addition, upgrade pricing facilitates static price discrimination. When consumers are homogeneous, viz., when $v _ { L } ^ { H } \leq \Upsilon _ { 2 } ,$ , high-type consumers have a lower incremental utility from the new product than low-type consumers in period 1. Without an upgrade policy, the acquirer may use intertemporal price discrimination as in Proposition 3(i), selling the new product sequentially to low- and high-type consumers. With an upgrade policy, the acquirer can directly charge low-type consumers a higher price than hightype consumers because they do not have the old product. Such static price discrimination helps advance selling the new product to high-type consumers to period 1. It also enables the acquirer to extract all consumer surplus because consumers can now be diferentiated by purchase history.

More importantly, with such static price discrimination, the acquirer does not need to wait for the installed base to depreciate before selling the new product to high-type consumers (note that deferring selling the new product to high-type consumers itself causes wastage, as the unsold new product also depreciates over time). Hence, it helps minimize the opportunity loss due to waiting, and so it strictly dominates the intertemporal price discrimination strategy, $\{ 1 \colon N \to L ;$ 2: $N  { \hat { H } } \}$ , even though the latter can sometimes extract consumer surplus perfectly. Observation 2—the perfect intertemporal price discrimination result—no longer applies. In fact, the acquirer will never want to serve low-type consumers exclusively before high-type consumers now. This static price discrimination facilitated by upgrade pricing, when applied, also enhances social welfare, as all consumers will get the new product in period 1.

On the other hand, when consumers are heterogeneous, viz., when $v _ { L } ^ { H } > \Upsilon _ { 2 } ,$ upgrade pricing will not afect high-type consumers. However, it helps the acquirer pose a credible threat to low-type consumers—if they do not buy the old product in period 1, then they will have to pay a higher price for the new product in the future. This threat of (future) price discrimination based on purchase history helps alleviate the cannibalization caused by selling the old and new products sequentially to low-type consumers. The acquirer can sell the new product to high-type consumers in period 1 concurrently because its price exceeds what low-type consumers are willing to pay.

Accordingly, the option to ofer upgrade pricing empowers the acquirer to make more profit from simultaneously selling the old and new products to low- and high-type consumers in period 1 without worrying about cannibalization in the future. This result applies even when consumers are heterogeneous and the market contains many low-type consumers (recall that these two conditions are the facilitators for delayed product introduction in Section 4.2.1), meaning Observation 3 no longer applies. The competitive market outcome, which difers from delayed product introduction by sequentially selling the products to low-type consumers earlier, will now more likely occur.

Observation 4. With M&A and an upgrade policy, the acquirer can earn more from the product sequence in competition, $\{ 1 \colon N \to H , O \to L ; \hat { 2 } \colon N \to L \}$ . In addition to the markets characterized in Proposition 3(v), the competition outcome will also occur in all markets characterized in Proposition 5(iii) with $d _ { L } < \delta U ( q _ { O } , n - 2 ) / ( U ( q _ { O } , 1 ) ) , v _ { L } ^ { H } \overset {  } { \leq } \Upsilon _ { 1 } + d _ { L } / ( 1 - d _ { L } ) +$ $( \delta U ( q _ { O } , n - 2 ) ) / ( ( 1 - d _ { L } ) [ U ( q _ { N } , \tilde { 1 ) } - U ( q _ { O } , 1 ) ] ) ,$ or $v _ { L } ^ { H } <$ $( \delta ( 1 + d _ { L } ) U ( q _ { O } , 1 ) - \delta U ( q _ { N } , 1 ) ) / ( ( 1 - \delta ) ( 1 - d _ { L } ) [ U ( q _ { N } , 1 )$ $- U ( q _ { O } , 1 ) ] )$ when $n = 3 .$

Interestingly, Proposition 5(ii) shows that when consumers are heterogeneous and the market does not contain many low-type consumers, the acquirer will not sell the new product to low-type consumers in period 1 because doing so will constrain the price chargeable to high-type consumers. Furthermore, in the markets characterized in the second condition of Proposition 5(i), i.e., when consumers are moderately heterogeneous, although the acquirer wants to serve low-type consumers in period 1, it will not be able to diferentiate low- and high-type consumers by upgrade pricing. Taken together, these two conditions characterize markets in which upgrade pricing will not be deployed because it will not be efective anyway. They may explain why in some real-world markets firms do not ofer upgrade pricing despite it being feasible to do so. For example, Apple does not ofer an upgrade policy for its celebrated iPhone. We wonder if it is because Apple has many high-valuation customers who are willing to pay a high price for the nextgeneration iPhone despite that they already have an older-generation one.

Finally, Proposition 4 applies with maximum social welfare achieved in the markets characterized in Proposition 5(i). Comparing Propositions 3 and 5, and Figures 3 and 4, ofering an upgrade policy after M&A can sometimes help even high-type consumers get the new product earlier, specifically in all markets characterized in Proposition 3(i) and 3(iv). This is again because the acquirer can exercise static instead of intertemporal price discrimination, and so cannibalization is of less concern.

Nevertheless, this power to exercise static price discrimination after M&A can decrease social welfare too. Because the acquirer can now segment the market by selling the old product to low-type consumers, it has less urgency to sell the new product to them. (Deferring selling the new product to low-type consumers may allow the acquirer to charge a higher price to the hightype consumers.) Hence, in some markets, allowing for upgrade pricing can decrease social welfare because the acquirer will shift from strategy <sup>{</sup>1: $N  H , L \}$ to strategy $\{ 1 \colon N \to H , O \to L ; 2 \colon N \to L \}$ . Even with this proviso, however, because the upgrade policy is optional, the acquirer’s profit with an upgrade policy will never be lower than that without an upgrade policy.

Proposition 6. After M&A, the acquirer’s profits with an upgrade policy weakly dominate its profits without an upgrade policy. Compared with the case of M&A without an upgrade policy, M&A with an upgrade policy will

(i) maximize social welfare in all markets characterized in Proposition 3(i) and Proposition 5(i) with $v _ { L } ^ { H } > ( U ( q _ { N } , 2 ) -$ $d _ { L } \dot { U } ( q _ { O } , 2 ) ) / ( \delta ( 1 - d _ { L } ) \dot { [ } U ( q _ { N } , 1 ) - U ( q _ { O } , \tilde { 1 } ) ] ) \ w h e n \ n = 3 ,$ and

(ii) decrease social welfare when

$$
\begin{array}{r l} & {\Upsilon_ {1} + \frac {d _ {L}}{1 - d _ {L}} + \frac {\delta U (q _ {O} , n - 2)}{U (q _ {N} , 1) - U (q _ {O} , 1)} <   v _ {L} ^ {H}} \\ & {\quad \leq \Upsilon_ {1} + \frac {d _ {L}}{1 - d _ {L}} + \frac {\delta U (q _ {O} , n - 2)}{(1 - d _ {L}) [ U (q _ {N} , 1) - U (q _ {O} , 1) ]}} \end{array}
$$

$$
\begin{array}{c} \leq \frac {\Upsilon_ {1}}{1 - d _ {L}}, \quad a n d \\ v _ {L} ^ {H} \leq \frac {U (q _ {N} , 2) - d _ {L} U (q _ {O} , 2)}{\delta (1 - d _ {L}) [ U (q _ {N} , 1) - U (q _ {O} , 1) ]} \quad w h e n n = 3. \end{array}
$$

To conclude, the upgrade policy facilitates static price discrimination, which tends to favor selling the new product to consumers who already own the old product. For consumers who do not own any product, it helps ease the cannibalization between the old and new products, which allows the acquirer to make more profit from sequentially selling the old and new products to them (compared to having no upgrade policy). This additional profit, ironically, may cause low-type consumers to get the new product later when their valuation for quality is considerably lower than that of high-type consumers.

Proposition 6 ofers a novel insight on why firms seek customer records in M&A. For example, when Toysmart.com filed for bankruptcy protection in 2000, it listed its customer database as one salable asset. Amazon.com (2016) states on its privacy notice, “As we continue to develop our business, we might sell or buy stores, subsidiaries, or business units. In such transactions, customer information generally is one of the transferred business assets.” An ostensible reason for firms to acquire customer records is to predict consumer preferences or ofer customized services (Garfinkel et al. 2007, Li et al. 2011, Tsai et al. 2011). Our analysis suggests they may use such records simply for static price discrimination (Taylor 2004, Fudenberg and Villas-Boas 2006).

## 4.3. Will A Merger Happen?

For M&A to happen, the benefit must be compatible with the vendors’ incentives, meaning the acquirer must earn a greater profit than the incumbent and entrant. Otherwise, they will not acquire the other party. As discussed above, the vendors sufer from competition, cannibalization, and time inconsistency in the competitive market. A merger can help evade competition and ease cannibalization. Hence, it should lead to increased overall profit. The next proposition shows that this is indeed the case.

Proposition 7. The acquirer’s profits after M&A weakly dominate the sum of the incumbent’s and entrant’s profits in the competitive market.

Given that M&A brings benefits, the vendors should have incentives to merge with others. This may be the underlying motivation for many IT M&As (Banker et al. 2011, Tanriverdi and Uysal 2011, EY 2015). Instead of acquiring new technologies, our analysis suggests that they may be motivated by product portfolio planning or simply just the option to remove competitors’ products from the market.

## 4.4. Diferent Discount Factors

We now consider an extension where the vendors and consumers have diferent discount factors. Let θ and δ be the vendors’ and consumers’ discount factors. Following similar analysis as in Section 3, for the installed base to form in period 0, we must have $d _ { H } v _ { L } ^ { H } > 1 \ .$ + $( d _ { L } U ( q _ { O } , n - 1 ) / \hat { U ( q _ { O } , 1 ) } ) ( \delta - \theta )$ . Compared to Assumption 1, if the incumbent is less patient, $\mathrm { i . e . , } \theta < \delta ,$ then intertemporal price discrimination becomes less attractive. The incumbent will more likely serve the entire market in period 0. By contrast, if the incumbent is more patient, $\mathrm { i . e . , ~ } \theta > \mathrm { ~ \bar { \delta } ~ }$ , then intertemporal price discrimination is more attractive, meaning an installed base of the old product will more likely form after period 0.

In general, when the vendors are less patient, i.e., $\theta < \delta ,$ they tend to favor strategies that sell the products earlier. This can change the equilibrium product sequence in the competition setting. In particular, Proposition 2 may not hold because if θ is suficiently small, the entrant may choose to penetrate the market with the new product immediately in period 1 instead of delaying selling it to low-type consumers in period 2. When this happens, the incumbent will not be able to sell any product in period 1. Proposition 2 will continue to apply if the entrant is more patient than consumers.

By contrast, allowing for diferent discount factors will not alter the equilibrium strategies under M&A with or without an upgrade policy. It will only shift the boundaries between the optimal strategies in Figures 3 and 4. Accordingly, most of the results in the M&A setting will continue to apply. Because Observations 2 and 3 involve delayed revenues for the acquirer, the corresponding strategies, namely, perfect intertemporal price discrimination and delayed product introduction, will be less (more) likely to occur when the acquirer is relatively less (more) patient than consumers.

Finally, we have assumed $\delta < 1$ . What if δ <sup></sup> 1, i.e., the vendors and consumers are perfectly patient? As the vendors want to sell to consumers earlier under competition and upgrade policy can resolve the cannibalization caused by the existing installed base, the outcomes in the competitive market and M&A with an upgrade policy will remain unchanged. In M&A without an upgrade policy, strategy $\{ 1 \colon \cdot N \to H , O \to L ; 2 \colon N \to L \}$ will become suboptimal because the acquirer is not eager to capture early profits from low-type consumers (doing so will reduce the profit it can earn from selling the new product to them in the future). Hence, the competitive market outcome, <sup>{</sup>1: $N \to H , O \to L ;$ $2 \colon N  \hat { L } \}$ , which causes the greatest cannibalization among the new product and the existing installed base, will not occur. This diference, however, will not afect the qualitative insights of all propositions and observations derived above.

## 4.5. Strategic Players

We next explore the outcomes when Assumption 3 is violated, i.e., if the incumbent anticipates the new product. Referring to Proposition 2, with competition, the incumbent will sell the old product in period 1 to low-type consumers. However, it now foresees it will not be able to charge a high price for the old product in period 1. Hence, its expected profit from intertemporal price discrimination will decrease (cf. when it is myopic). This implies that consumers have to be more heterogeneous than the condition in Assumption 1 for the incumbent to prefer intertemporal price discrimination. The incumbent will more likely cover the market completely in period 0. When this happens, all consumers will own the old product in period 1. The problem will degenerate to a standard multiperiod pricing problem with heterogeneous consumers (see, for example, the analyses in Acquisti and Varian 2005, Bhargava and Choudhary 2008, Choudhary 2010).

What if M&A can happen in period 0, i.e., before the new product arrives? For example, IT vendors such as Apple and Google often acquire start-up firms with forthcoming technologies that complement their existing products. If consumers are myopic, then Proposition 7 will apply because the acquirer can always use the strategies discussed in Section 4.2. Interestingly, being myopic means consumers are willing to pay a higher price for the old product, and so the acquirer will want to sell it to them in period 0. This will happen, for example, in the markets characterized in Propositions 3(iii) and 5(ii). Hence, although our analysis assumes M&A can occur only in period 1, some of its results may continue to apply if the M&A happens earlier. The case of M&A happening in period t > 1 is trivial. Hence, we omit it from the paper.

Finally, what if the consumers are also strategic, i.e., they anticipate the new product? Then, it will be difficult for the incumbent to sell the old product in period 0 because consumers know they will have more options in the future. This implies the incumbent’s price in period 0 will be subject to more constraints. Resolving all of these pricing constraints is challenging but necessary in characterizing the full benefits of

M&A. We defer such analysis to future research. In any case, the assumption of myopic or naïve consumers is customary in many studies of dynamic consumer choices (see, e.g., Taylor 2004, Acquisti and Varian 2005, Liu and Zhang 2013).

## 5. Implications

Table 1 summarizes the observations of product strategies in diferent markets. In general, an entrant with a new and better product will prefer to sell to existing consumers who own the earlier generation of the same product as soon as possible. Competition will not maximize social welfare. M&A can help maximize social welfare in some markets, but it can decrease social welfare too (e.g., when delayed product introduction occurs). The vendors in a competitive (duopoly) market have an economic incentive to form a coalition. This incentive is stronger when the acquirer can determine who possesses the old product and exercise upgrade pricing accordingly.

Our analysis provides a number of important implications for the ongoing research on M&A and product line design and pricing. First, it shows that product nature can interact with market structure to afect consumers’ product consumption and welfare. When the product is subject to depreciation or economic obsolescence and when there is an existing installed base, competition need not be good and consolidation need not be bad for consumers. Future research should integrate product nature as one key consideration in studying the optimal market structure for IT products.

Second, we theoretically establish “shelving a product” and “delayed new product introduction” via M&A as feasible product strategies in IT markets. These strategies can be optimal because they help ease cannibalization despite that the vendor cannot alleviate time inconsistency through controlling the pace of R&D (cf. Dhebar 1994, Fishman and Rob 2000, Kornish 2001). It is important for future work to account for the vendor’s options to retire or postpone a product on top of its ability to influence the progress of technological development.

Table 1. Summary of Observations

<table><tr><td></td><td>Competition</td><td>M&amp;A without upgrade policy</td><td>M&amp;A with upgrade policy</td></tr><tr><td>Observation 1: Shelving the old product</td><td>No</td><td>All markets in Proposition 3(i)-3(iii)</td><td>All markets in Proposition 5(i) and 5(ii)</td></tr><tr><td>Observation 2: Perfect intertemporal price discrimination</td><td>No</td><td>All markets in Proposition 3(i), second condition</td><td>No</td></tr><tr><td>Observation 3: Delayed new product introduction</td><td>No</td><td>All markets in Proposition 3(iv); only when n = 3</td><td>No</td></tr><tr><td>Observation 4: Competitive market product sequence (1: N → H, O → L; 2: N → L)</td><td>Yes</td><td>All markets in Proposition 3(v); only when δ &lt; 1</td><td>All markets in Proposition 5(iii)</td></tr></table>

Third, we find that second-degree, or indirect, price discrimination can be perfect in terms of capturing consumer surplus. This finding is striking, as previous research suggests even monopoly vendors cannot capture all consumer surplus with second-degree price discrimination (Mussa and Rosen 1978, Moorthy 1984). It is founded on the setting where some consumers possess an old product that depreciates over time, and hence the intertemporal change in consumer valuations allows the vendor to “sort” consumers perfectly. It highlights the importance of identifying dynamic changes in consumer valuations when assessing diferent price discrimination strategies.

Finally, most IT products encompass multiple generations because of technological improvement. It is important to address the existing installed bases of old products when studying the optimal timing and pricing of new IT products. Such installed bases may cannibalize new product sales but at the same time provide another instrument for vendors to segment consumers or exercise price discrimination.

What are the managerial implications of our findings? Obviously, launching a new product requires careful planning, especially when there is an existing installed base of old products. The key decision parameters are consumer heterogeneity, $\dot { v } _ { L } ^ { H } ,$ , and mix, $d _ { L } ,$ and whether M&A and upgrade pricing are feasible. The main advantage of M&A is that the acquirer will have many more options in timing and pricing its products. The main advantage of upgrade pricing is that it facilitates static pricing discrimination, allowing the acquirer to ofer a cheaper price to high-type consumers (when consumers are homogeneous) or encourage low-type consumers to buy the old product (when consumers are heterogeneous). These advantages can be realized only when the acquirer gains a deep understanding of market characteristics and the mix of consumers.

We find that the acquirer weakly prefers upgrade pricing after M&A, meaning it will often seek to ofer a diferent price for the new product to former patrons. The social welfare implication of such upgrade pricing is not unequivocal. In the markets characterized in Observation 4 and Proposition 6(i), i.e., when consumers are heterogeneous with many low-type consumers or homogeneous with a moderate number of low-type consumers, allowing firms to transfer customer databases or identify previously sold products in M&A can be good, at least in terms of speeding up new product consumption. This may apply to IT markets with frequent product innovations and entry and exit of vendors (e.g., mobile communications services or computer software).

However, upgrade pricing can be bad or inefective in other markets. When this is the case, the acquirer’s urge to ofer upgrade pricing should be suppressed, perhaps by helping consumers conceal their purchase history. Here again, having an accurate assessment of consumer heterogeneity and mix is fundamental to making proper judgments on whether upgrade pricing should be encouraged.

Furthermore, our analysis establishes an intriguing incentive for M&A, namely, to shelve an old product (instead of expanding market size or product portfolio; see, e.g., Shaked and Sutton 1990, Banker et al. 2011). If a vendor finds it challenging to compete with other vendors selling low-quality products, then a good strategy is to acquire the competitors and retire their products. The additional revenue obtained from raising the new product’s price after the merger may well be suficient to fund the acquisition.

Finally, competition will not maximize social welfare in our setting. In the markets characterized in Propositions 3(ii) (without upgrade policy) and 5(i) (with upgrade policy), the policy maker should encourage M&A as it will increase social welfare. Ironically, when competition and cannibalization are imminent, a good way to facilitate early consumption of better products by all consumers is to encourage a merger instead of promoting competition. The acquirer will then be able to optimize the path of product introduction, which, by our theoretical analysis, can often benefit consumers.

At this point it is important to acknowledge our limitations. This study is normative in nature. Our objective is to explore how an IT vendor should react when facing competition from another vendor, when new product entry is unexpected, and when some consumers have variously purchased an old product to form an installed base. We integrate the key economic considerations—competition, cannibalization, and time inconsistency—in a single framework to advise what the vendors can do to maximize their profits and social welfare. Because of such holistic consideration, we can pin down some novel strategies that have not been well articulated in the literature. Our strategies help plan for the optimal price and product paths in general IT markets.

However, our study is not positivist in nature. We do not intend to explain what has actually happened in any real-world IT market. There are obvious drawbacks in our model—we study only a duopoly, assume negligible marginal costs that may apply only to some IT products, and assume exogenous R&D that seems more applicable to technologies of general interest. We also assume a closed market without new players, and M&A can occur only from period 1 onward. We argue that our setting captures an unexpected entry of new products, which is not uncommon in the IT world (for example, the entry of Apple to the watch market and

Google to the global positioning system market may have caught the incumbents by surprise). Obviously, future research may relax some of these assumptions.

## 6. Conclusions

We study an important source of consumer heterogeneity, namely, purchase history, and illustrate how it afects demand dynamics when the vendors and consumers cannot anticipate future products in an IT market. We show that vendors have economic incentives to form a coalition, which may variously increase or decrease social welfare and does not always speed up new product introduction. We identify the motivations of several intriguing strategies, including forming a coalition to shelve the old product, targeting lowvaluation consumers followed by high-valuation consumers, and delaying selling the new product. They present novel strategic justifications for M&A.

How are our results relevant to real-life practice? As discussed above, we observe experiences of firms such as Apple and Microsoft that seem reasonably consistent with the strategic choices identified here. Delayed new product introduction seems common in some IT markets. For example, the technologies for fourth generation mobile telephone services have been available for some time, but to date, many service providers are still ofering third or even second generation cellular services. Some software vendors such as Microsoft have been pushing back selling new versions of their software. It is entirely possible that their new products are not ready, but they could well be tackling cannibalization through the mechanisms identified in this paper as well.

Future research may extend this work in several meaningful ways. First, we should examine whether prompting consumers about future products (i.e., relaxing Assumption 3) would afect the benefits of M&A. Second, analyzing the case with positive marginal costs may extend our insights to other markets. Finally, empirically testing our theory using market-level data will help validate our recommendations.

## Acknowledgments

The authors thank the seminar participants at the University of California at Irvine, University of Southern California, National University of Singapore, and the Hong Kong University of Science and Technology for helpful comments and suggestions. The authors also thank Terrance Fung, Ivan Png, and the senior editor, associate editor, and reviewers for their constructive advice and guidance. A substantial part of this research was completed when the first author was with the School of Management, Huazhong University of Science and Technology.

## Appendix

The computations of the vendors’ pricing, profit, and equilibrium strategies and their comparisons in the three scenarios—under competition, with acquisition and no upgrade policy, and with acquisition and upgrade policy—are reported in Sections A–C $\mathsf { A } { \ - } - \mathsf { C }$ in the online appendix. In this appendix we present only the summary proofs of the propositions.

Proof of Proposition 1 Note that

$$
\begin{array}{r l} \Upsilon (t + 1) - \Upsilon (t) & = \frac {U (q _ {N} , n - t)}{U (q _ {N} , n - t) - U (q _ {O} , n - t - 1)} \\ & \quad - \frac {U (q _ {N} , n - t + 1)}{U (q _ {N} , n - t + 1) - U (q _ {O} , n - t)} \\ & = \frac {q _ {N} (1 - \delta^ {n - t})}{q _ {N} (1 - \delta^ {n - t}) - q _ {O} (1 - \delta^ {n - t - 1})} \\ & \quad - \frac {q _ {N} (1 - \delta^ {n - t + 1})}{q _ {N} (1 - \delta^ {n - t + 1}) - q _ {O} (1 - \delta^ {n - t})}, \end{array}
$$

which has the sign of $- q _ { N } q _ { O } \delta ^ { n - t - 2 } ( 1 - \delta ) ^ { 2 } < 0$ for all t. Hence, Υ<sup>(</sup>t<sup>)</sup> is monotonically decreasing in t. This also implies, for any $t < n ,$ , there must exist some $v _ { L } ^ { H }$ such that $\Upsilon ( t + 1 ) \leq$ $v _ { L } ^ { \bar { H } } \leq \Upsilon ( t ) .$ , as $\Upsilon ( t ) > 1$ for all $t < n .$

Now, pick any one such $v _ { I . } ^ { H }$ and the corresponding $t = \hat { t } < n$ such that $\Upsilon ( \hat { t } + \dot { 1 } ) \leq v _ { t } ^ { H } \leq \Upsilon ( \ddot { \hat { t } } )$ . Because Υ<sup>(</sup>t<sup>)</sup> is monotonically decreasing in $t , v _ { \scriptscriptstyle { L } } ^ { \cal H } \le \Upsilon ( \hat { t } )$ implies $v _ { I . } ^ { H } \leq \Upsilon ( t ) .$ , or $h _ { N t } ^ { H } \leq b _ { N t } ^ { L } ,$ for all $t \leq \widehat { t } .$ Similarly, $v _ { I . } ^ { H } \geq \Upsilon ( \hat { t } + 1 )$ <sup>)</sup> implies $v _ { I . } ^ { H } \geq \Upsilon ( t )$ , or $h _ { N t } ^ { H } \geq b _ { N t } ^ { L } ,$ , for all $t \geq \widehat { t } + 1$ . Finally, note that if $v _ { L } ^ { H } \geq \Upsilon ( 1 )$ , then $h _ { N t } ^ { \bar { H } ^ { ' } } \geq b _ { N t } ^ { \bar { L } ^ { ' } }$ for all t.

## Proof of Proposition 2

Referring to Section A of the online appendix, the optimal strategies for the incumbent and entrant are $\{ 1 \colon O \to L \}$ and $\{ \bar { 1 } \colon N \to H ; 2 \colon N \to L \}$ , which is the first part of the result. With these strategies, the combined utility of all consumers is $d _ { H } v _ { H } U ( q _ { N } , n ) + d _ { L } v _ { L } [ U ( q _ { O } , 1 ) + \delta U ( q _ { N } , n - 1 ) ]$ , which always exceeds the sum of the incumbent’s and entrant’s profits.

## Proof of Proposition 3 and Observations 1–3

We refer the reader to the summary table in Section B of the online appendix, which characterizes all parameterization and equilibrium strategies listed in Proposition 3. Observation 1 corresponds to the first seven rows. Observation 2 corresponds to the third row, which is the only case involving intertemporal price discrimination and satisfying Proposition 1. The acquirer’s total profit here is $d _ { L } { \dot { v } } _ { L } { \bar { U } } ( q _ { N } , \bar { n } ) + \delta d _ { H } { v } _ { H } [ U ( q _ { N } , n - 1 ) - U ( q _ { O } , n - 2 ) ]$ , which is the sum of consumers’ utility from the new product. Observation 3 corresponds to the eighth row, i.e., the strategy $\{ 1 \colon O \to L ; 2 \colon N { \overset { \vartriangle } { \to } } H ; 3 \colon N \to L \}$

## Proof of Proposition 4

In considering social welfare, the transfer payment from consumers to sellers does not matter. In our setting, social welfare is maximized if all consumers buy the new product as early as possible. Proposition 2 shows that this will not happen with competition. Referring to the summary table in Section B of the online appendix, the acquirer will choose strategy $\{ 1 { : } N \to H , L \}$ in the second and fourth to sixth rows. The range of $v _ { L } ^ { H }$ in these four rows corresponds to the conditions in Proposition 3(ii).

## Proof of Proposition 5 and Observation 4

We refer the reader to the summary table in Section C of the online appendix, which characterizes all parameterization and equilibrium strategies listed in Proposition 5. The conditions in Observation 4 are obtained by comparing the parameterization in the fourth row in that table against the last row of the summary table in Section B of the online appendix. Figure 4 shows that the product sequence under competition, $\{ 1 \colon O \to L , N \to H ; 2 \colon \hat { N } \to L \}$ , will occur in a wide range of parameterization.

## Proof of Proposition 6

Comparing the first and third rows in the summary table in Section B of the online appendix with the first row in the summary table in Section C, in the parameterization in Proposition 3(i), the acquirer will choose strategy $\{ 1 \colon N \to L ; \bar { 2 } \colon N \to H \}$ without upgrade policy, but strategy $\{ 1 \colon N \to H , L \}$ with an upgrade policy. Similarly, the other conditions leading to increasing or decreasing social welfare can be obtained by comparing the parameterization in the sixth row in the summary table in Section B with the second row in the summary table in Section $C ,$ both of which concern the strategy <sup>{</sup>1: N <sup>→</sup> H, L<sup>}</sup>.

Referring to the summary table in Section C of the online appendix, for all $v _ { I . } ^ { H } \leq \Upsilon _ { 2 }$ , the acquirer’s profit with upgrade pricing is $d _ { H } v _ { H } [ \tilde { U } ( q _ { N } , n ) - U ( \bar { q } _ { O } , n - \bar { 1 } ) ] + d _ { L } v _ { L } { \bar { U ( q _ { N } , n ) } } .$ which is the total utility that consumers can obtain and so the maximum profit that the acquirer can earn from consuming the new product in period 1. This implies that its profit with upgrade pricing dominates those in the first four rows in the summary table in Section B.

Next, when $v _ { L } ^ { H } > \Upsilon _ { 2 } ,$ , as shown in the summary table in Section C of the online appendix, the acquirer has three candidate strategies. Referring to the summary table in Section B, these three strategies are also candidate optimal strategies when the acquirer cannot exercise upgrade pricing. Hence, we simply need to show that each of the three strategies in Section C (with upgrade pricing) weakly dominates the strategies in Section B (without upgrade pricing). As is clear from the tables, specifically the rows where $v _ { L } ^ { H } > \Upsilon _ { 2 } ,$ the acquirer will earn the same profits with or without upgrade pricing with strategies $\{ 1 \colon \mathrm { ~ \dot { \cal { N } } ~ }  { \cal { H } } , { \cal { L } } \}$ and $\{ 1 \colon N \to { \bf \bar { { H } } } ; 2 \colon N \to L \}$ With strategy $\{ 1 \colon \ N \to H , \ O \to L ; \ 2 \colon \ N \to L \}$ , its profit with upgrade pricing is $d _ { L } v _ { L } U ( q _ { O } , n - 1 ) + d _ { H } v _ { H } [ U ( q _ { N } , 1 ) -$ $U ( q _ { O } , \bar { 1 } ) \bar { ] } + \delta \bar { v _ { L } } [ U ( q _ { N } , n - 1 ) - U ( q _ { O } , n - 2 ) ]$ , which exceeds its profit from the same strategy without upgrade pricing, $d _ { L } \bar { v _ { L } } U ( q _ { O } , 1 ) + d _ { H } v _ { H } [ U ( q _ { N } , 1 ) - \bar { U } ( q _ { O } , 1 ) ] + \delta \bar { v _ { L } } \bar { [ } U ( q _ { N } , n - 1 ) \bar { - } \bar { - } \bar { - } \bar { - } \bar { - } \bar { - } \bar { - } \bar { - } \bar { - } \bar { - } \bar { - } \bar { - } \bar { - } \bar { - } \bar { - } \bar { - } \bar { - } \bar { - } \bar { - } \bar { - } \bar { - } \bar { - } \bar { - } \bar { - } \bar { - } \bar { - } \bar { - } \bar { - } \bar { - } \bar { - } \bar { - } \bar { - } \bar { - } \bar { } \bar { - } \bar { - } \bar { } \bar { - } \bar { } \bar { - } \bar { } \bar { - } \bar { } \bar { - } \bar { } \bar { - } \bar { } \bar { - } \bar { } \bar { - } \bar { } \bar { - } \bar { } \bar { - } \bar { } \bar { - } \bar { } \bar { - } \bar { } \bar { - } \bar { } \bar { - } \bar { } \bar { - } \bar { } \bar { - } \bar { } \bar { - } \bar { } \bar { - } \bar { } \bar { - } \bar { } \bar { - } \bar { } \bar { - } \bar { } \bar { - } \bar { } \bar { - } \bar { } \bar { - } \bar { } \bar { - } \bar { } \bar { - } \bar { } \bar { - } \bar { } \bar { - } \bar { } \bar { - } \bar { } \bar { - } \bar { } \bar { - } \bar { } \bar { - } \bar { } \bar { - } \bar { } \bar { - } \bar { } \bar { - } \bar { } \bar { - } \bar { } \bar { - } \bar { } \bar { - } \bar { } \bar { - } \bar { } \bar { - } \bar { } \bar { - } \bar { } \bar { - } \bar { } \bar { - } \bar$ $U ( q _ { O } , n - 2 ) ] , \mathrm { a n d i t s p r o f i t f r o m s t r a t e g y } \{ 1 { : } O \to L ; 2 { : } N \to H ;$ 3: $N  L \} , \ d _ { L } v _ { L } U ( q _ { o } , 2 ) \ + \ \delta d _ { H } v _ { H } [ U ( q _ { N } , 1 ) \ - \ U ( q _ { o } , 1 ) ] \ +$ $\delta ^ { 2 } v _ { L } [ U ( q _ { N } , n - 2 ) - U ( q _ { O } , n - 3 ) ]$ . This completes the proof.

## Proof of Proposition 7

We first compare the combined profits of the entrant and incumbent in the competitive market against the vendor’s profits in the case with acquisition but no upgrade policy. Referring to Section A of the online appendix, when $v _ { L } ^ { \dot { H } } \leq \dot { \Upsilon _ { 1 } } .$ the combined profit of the incumbent and entrant is

$$
\begin{array}{r l} & {\Pi_ {C} = (v _ {H} - d _ {L} v _ {L}) [ U (q _ {N}, 1) - U (q _ {O}, 1) ]} \\ & {\qquad + \delta v _ {L} [ U (q _ {N}, n - 1) - U (q _ {O}, n - 2) ].} \end{array}\tag{1}
$$

Referring to Section B of the online appendix, specifically, case 4 in period 1, when $v _ { L } ^ { H } \leq \Upsilon _ { 1 } ,$ the vendor’s profit is exactly $\Pi _ { C } .$ . Accordingly, the vendor’s profit with acquisition is identical to the combined profit of the incumbent and entrant whenever $\{ 1 \colon N \to H , \hat { O } \to L ; 2 \colon N \to L \}$ is a candidate strategy. Referring to the summary table in Section B of the online appendix, this strategy is always dominated by other strategies. Hence, acquisition always gives higher overall profits.

Next, when $\hat { v } _ { L } ^ { H } > \Upsilon _ { 1 }$

$$
\begin{array}{r} \Pi_ {C} = d _ {L} v _ {L} U (q _ {O}, 1) + d _ {H} v _ {H} [ U (q _ {N}, 1) - U (q _ {O}, 1) ] \\ + \delta v _ {L} [ U (q _ {N}, n - 1) - U (q _ {O}, n - 2) ]. \end{array}\tag{2}
$$

Referring to Section B of the online appendix, this is again exactly identical to the vendor’s profit with strategy $\{ \Breve { 1 } \colon N \to H , \mathbf { \bar { O } } \to L ; 2 \colon N \to L \}$ in case 4 in period 1, which, according to the summary table, is a candidate equilibrium strategy when $v _ { I . } ^ { H } > \mathsf { \bar { Y } } _ { 1 }$ . Hence, the vendor’s profits with acquisition will weakly dominate the combined profit of the incumbent and entrant. (The profits are equal when $\{ 1 \colon N \to H , O \to L ; 2 \colon N \to H \}$ is the equilibrium strategy.)

We next compare the combined profit of the incumbent and entrant in the competition case against the vendor’s profits in the case with acquisition and upgrade policy. Referring to Section C of the online appendix, specifically, case 4 in period 1, the vendor’s profit with strategy $\{ 1 \colon N { \stackrel { \cdot } { \to } } H , O \to L ;$ $\bar { 2 } \colon N  L \}$ always exceeds the $\Pi _ { C }$ in (1) when $v _ { L } ^ { H } \leq \Upsilon _ { 1 } ,$ and the $\Pi _ { C }$ in (2) when $v _ { L } ^ { H } > \Upsilon _ { 1 }$ . Accordingly, acquisition always gives higher overall profits.

Taken together, the vendor’s profits with acquisition (with or without upgrade policy) weakly dominate the combined profit of the incumbent and entrant in the competitive market.

## Endnotes

<sup>1</sup> For example, after OS/2 was withdrawn from the operating system market in 2006, Microsoft faced a sizable pool of consumers who had been using OS/2 in their computer systems. These consumers may switch or upgrade to future versions of the Windows operating system.

<sup>2</sup> The assumption that quality stays constant throughout a product’s life span is common in the literature (see, e.g., Moorthy and Png 1992, Fishman and Rob 2000, Goettler and Gordon 2011). It particularly fits software products, which are prone to economic obsolescence, for example, because of aging of complementary hardware platforms, instead of physical obsolescence.

<sup>3</sup> It is customary to assume zero marginal costs for IT products (see, e.g., Choudhary 2010, Xu et al. 2011). It allows us to focus on the firm’s strategic decisions in response to demand variations arising from the coexistence of multiple versions of the same product, which is typical in the IT industry (Padmanabhan et al. 1997, Dogan et al. 2011, Li and Graves 2012).

<sup>4</sup> Because the new product is introduced later, it will retire after the old product. Note that if the new product arrives in any period $t > 1 ,$ the incumbent would have sold the old product to all consumers by the time the entrant appears. The entrant would then face a simple pricing problem with trivial solutions. To focus on the strategic consideration related to M&As, we assume the new product arrives in period 1. In Section 4, we show that M&As may cause delayed introduction of the new product.

<sup>5</sup> For analysis of multiperiod pricing of information goods with heterogeneous consumers, see Bhargava and Choudhary (2008) and

Choudhary (2010). An extreme strategy for the entrant is to wait for the old product to retire before selling the new product in period n for consumers to use it in just one period. This can be attractive when the discount factor, δ, is suficiently close to 1 and cannibalization by the old product is significant, i.e., q is large. Although theoretically possible, this strategy will cause the two products to be disconnected in time. Any discussion of competition, acquisition, and product planning will then become moot. We do not consider such an extreme strategy in this paper.

<sup>6</sup> Recall that Assumption 1 favors intertemporal price discrimination, which causes the incomplete coverage of the market upon entering period 1. Proposition 2 may not apply without Assumption 1, but then all consumers would buy the old product in period 0. This does not seem realistic. In a related setting, Choudhary (2010) identifies conditions for homogeneous sellers to avoid price competition using diferent pricing schemes when consumers are heterogeneous and would buy multiple units of an information product. Here, consumers buy at most one unit from each vendor, but the entrant can minimize price competition by timing its product properly. For a classical analysis of how a monopolist vendor can exploit product timing to alleviate cannibalization, see Moorthy and Png (1992).

<sup>7</sup>This result parallels Proposition 2 of Bhargava and Choudhary (2008), which shows that a monopoly may not want to version an information product when consumers are homogeneous. Here, as we shall see in Section 4.3, specifically, Proposition 7, other than not wanting to version, a vendor may even be willing to pay (acquire a competitor) to shelve the old product.

## References

Acquisti A, Varian HR (2005) Conditioning prices on purchase history. Marketing Sci. 24(3):367–381.

Aghion P, Bloom N, Blundell R, Grifith R, Howitt P (2005) Competition and innovation: An inverted-U relationship. Quart. J. Econom. 120(2):701–728.

Ahuja G, Katila R (2001) Technological acquisitions and the innovation performance of acquiring firms: A longitudinal study. Strategic Management J. 22(3):197–220.

Amazon.com (2016) Privacy notice, updated September 30. https:// www.amazon.com/gp/aw/help/id<sup></sup>468496.

Banker RD, Wattal S, Plehn-Dujowich JM (2011) R&D versus acquisitions: Role of diversification in the choice of innovation strategy by information technology firms. J. Management Inform. Systems 28(2):109–144.

Bergemann D, Välimäki J (2006) Dynamic pricing of new experience goods. J. Political Econom. 114(4):713–743.

Besanko D, Winston WL (1990) Optimal price skimming by a monopolist facing rational consumers. Management Sci. 36(5):555–567.

Bhargava HK, Choudhary V (2008) Research note—When is versioning optimal for information goods? Management Sci. 54(5): 1029–1035.

Boulding W, Christen M (2009) Pioneering plus a broad product line strategy: Higher profits or deeper losses? Management Sci. 55(6):958–967.

Bright P (2011) Microsoft buys Skype for \$8.5 billion. Why, exactly? Wired (May 10), https://www.wired.com/2011/05/microsoft -buys-skype-2/.

Bulow J (1986) An economic theory of planned obsolescence. Quart. J. Econom. 101(4):729–749.

Bulow JI (1982) Durable-goods monopolists. J. Political Econom. 90(2):314–332.

Calzada J, Valletti TM (2012) Intertemporal movie distribution: Versioning when customers can buy both versions. Marketing Sci. 31(4):649–667.

Chen Y, Pearcy J (2010) Dynamic pricing: When to entice brand switching and when to reward consumer loyalty. RAND J. Econom. 41(4):674–685.

Chen YJ, Seshadri S (2007) Product development and pricing strategy for information goods under heterogeneous outside opportunities. Inform. Systems Res. 18(2):150–172.

Choudhary V (2010) Use of pricing schemes for diferentiating information goods. Inform. Systems Res. 21(1):78–92.

Clemons EK, Weber BW (1996) Alternative securities trading systems: Tests and regulatory implications of the adoption of technology. Inform. Systems Res. 7(2):163–188.

Coase RH (1972) Durability and monopoly. J. Law Econom. 15(1): 143–149.

Deneckere R, Davidson C (1985) Incentives to form coalitions with Bertrand competition. RAND J. Econom. 16(4):473–486.

Dhebar A (1994) Durable-goods monopolists, rational consumers, and improving products. Marketing Sci. 13(1):100–120.

Dogan K, Ji Y, Mookerjee VS, Radhakrishnan S (2011) Managing the versions of a software product under variable and endogenous demand. Inform. Systems Res. 22(1):5–21.

EY (2015) Global technology M&A update. Technical report, EY, London.

Fishman A, Rob R (2000) Product innovation by a durable-good monopoly. RAND J. Econom. 31(2):237–252.

Fudenberg D, Tirole J (1998) Upgrades, tradeins, and buybacks. RAND J. Econom. 29(2):235–258.

Fudenberg D, Villas-Boas JM (2006) Behavior-based price discrimination and customer recognition. Hendershott T, ed. Handbook in Information Systems (Emerald Group Publishing, Bingley, UK), 377–436.

Garfinkel R, Gopal R, Thompson S (2007) Releasing individually identifiable microdata with privacy protection against stochastic threat: An application to health information. Inform. Systems Res. 18(1):23–41.

Goettler RL, Gordon BR (2011) Does AMD spur Intel to innovate more? J. Political Econom. 119(6):1141–1200.

Grossman GM, Helpman E (1991) Quality ladders in the theory of growth. Rev. Econom. Stud. 58(1):43–61.

Hermalin BE, Katz ML (2006) Privacy, property rights and eficiency: The economics of privacy as secrecy. Quant. Marketing Econom. 4(3):209–239.

Jones SD, Rubin BF (2012) Oracle to buy Eloqua in \$810 million deal. Wall Street Journal (December 20), http://www.wsj.com/ articles/SB10001424127887323777204578191171409150846.

Jiang Z, Sarkar S (2009) Speed matters: The role of free software ofer in software difusion. J. Management Inform. Systems 26(3): 207–239.

Kapoor R, Lim K (2007) The impact of acquisitions on the productivity of inventors at semiconductor firms: A synthesis of knowledge-based and incentive-based perspectives. Acad. Management J. 50(5):1133–1155.

Koca E, Souza GC, Druehl CT (2010) Managing product rollovers. Decision Sci. 41(2):403–423.

Kornish LJ (2001) Pricing for a durable-goods monopolist under rapid sequential innovation. Management Sci. 47(11): 1552–1561.

Lee D, Mendelson H (2007) Adoption of information technology under network efects. Inform. Systems Res. 18(4): 395–413.

Lee IH, Lee J (1998) A theory of economic obsolescence. J. Indust. Econom. 46(3):383–401.

Levinthal DA, Purohit D (1989) Durable goods and product obsolescence. Marketing Sci. 8(1):35–56.

Li H, Graves SC (2012) Pricing decisions during inter-generational product transition. Production Oper. Management 21(1): 14–28.

Li X, Hitt LM, Zhang ZJ (2011) Product reviews and competition in markets for repeat purchase products. J. Management Inform. Systems 27(4):9–42.

Liu CZ, Gal-Or E, Kemerer CF, Smith MD (2011) Compatibility and proprietary standards: The impact of conversion technologies in IT markets with network efects. Inform. Systems Res. 22(1): 188–207.

Liu H (2010) Dynamics of pricing in the video game console market: Skimming or penetration? J. Marketing Res. 47(3):428–443.

Liu Q, Zhang D (2013) Dynamic pricing competition with strategic customers under vertical product diferentiation. Management Sci. 59(1):84–101.

Makri M, Hitt MA, Lane PJ (2010) Complementary technologies, knowledge relatedness, and invention outcomes in high technology mergers and acquisitions. Strategic Management J. 31(6): 602–628.

Mehra A, Bala R, Sankaranarayanan R (2012) Competitive behaviorbased price discrimination for software upgrades. Inform. Systems Res. 23(1):60–74.

Moorthy KS (1984) Market segmentation, self-selection, and product line design. Marketing Sci. 3(4):288–307.

Moorthy KS, Png IPL (1992) Market segmentation, cannibalization, and the timing of product introductions. Management Sci. 38(3):345–359.

Mussa M, Rosen S (1978) Monopoly and product quality. J. Econom. Theory 18(2):301–317.

Nair H (2007) Intertemporal price discrimination with forwardlooking consumers: Application to the U.S. market for console video-games. Quant. Marketing Econom. 5(3):239–292.

Padmanabhan V, Rajiv S, Srinivasan K (1997) New products, upgrades, and new releases: A rationale for sequential product introduction. J. Marketing Res. 34(4):456–472.

Perry MK, Porter RH (1985) Oligopoly and the incentive for horizontal merger. Amer. Econom. Rev. 75(1):219–227.

Puranam P, Singh H, Zollo M (2006) Organizing for innovation: Managing the coordination-autonomy dilemma in technology acquisitions. Acad. Management J. 49(2):263–280.

Ransbotham S, Mitra S (2010) Target age and the acquisition of innovation in high-technology industries. Management Sci. 56(11): 2076–2093.

Sears J, Hoetker G (2014) Technological overlap, technological capabilities, and resource recombination in technological acquisitions. Strategic Management J. 35(1):48–67.

Shaked A, Sutton J (1990) Multiproduct firms and market structure. RAND J. Econom. 21(1):45–62.

Stokey NL (1979) Intertemporal price discrimination. Quart. J. Econom. 93(3):355–371.

Stokey NL (1981) Rational expectations and durable goods pricing. Bell J. Econom. 12(1):112–128.

Su X (2007) Intertemporal pricing with strategic customer behavior. Management Sci. 53(5):726–741.

Tanriverdi H, Uysal VB (2011) Cross-business information technology integration and acquirer value creation in corporate mergers and acquisitions. Inform. Systems Res. 22(4):703–720.

Taylor CR (2004) Consumer privacy and the market for customer information. RAND J. Econom. 35(4):631–650.

Tsai JY, Egelman S, Cranor L, Acquisti A (2011) The efect of online privacy information on purchasing behavior: An experimental study. Inform. Systems Res. 22(2):254–268.

Van de Ven AH (2005) Running in packs to develop knowledgeintensive technologies. MIS Quart. 29(2):365–377.

Waldman M (2003) Durable goods theory for real world markets. J. Econom. Perspect. 17(1):131–154.

Xu L, Chen J, Whinston A (2011) Oligopolistic pricing with online search. J. Management Inform. Systems 27(3):111–142.

Zhao X (2009) Technological innovation and acquisitions. Management Sci. 55(7):1170–1183.
